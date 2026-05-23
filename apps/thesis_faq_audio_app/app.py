#!/usr/bin/env python3
"""
Thesis/FAQ Text-to-Audio App

Local-first MVP for private thesis-presentation and FAQ audio.
- No external Python dependencies.
- On Windows, uses built-in SAPI via powershell.exe/System.Speech.
- Produces WAV chunks plus a manifest JSON for repeatability.
- Dramabox integration is intentionally deferred behind the PM route/hardware gate.
"""

from __future__ import annotations

import argparse
import html
import json
import os
import re
import subprocess
import sys
import tempfile
import textwrap
from datetime import datetime
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Dict, Iterable, List, Optional
from urllib.parse import parse_qs, urlparse

APP_NAME = "Thesis/FAQ Text-to-Audio"
DEFAULT_OUTPUT_DIR = Path(__file__).resolve().parent / "outputs"
MAX_CHARS_PER_CHUNK = 1800


def sanitize_filename(value: str, default: str = "audio") -> str:
    value = (value or "").strip().lower()
    value = re.sub(r"[^a-z0-9A-Z._ -]+", "", value)
    value = re.sub(r"[\s-]+", "-", value).strip("-._")
    return value[:80] or default


def split_text(text: str, max_chars: int = MAX_CHARS_PER_CHUNK) -> List[str]:
    """Split text into TTS-friendly chunks by paragraphs, then sentence-ish boundaries."""
    cleaned = re.sub(r"\r\n?", "\n", text or "").strip()
    if not cleaned:
        return []

    paragraphs = [p.strip() for p in re.split(r"\n\s*\n", cleaned) if p.strip()]
    chunks: List[str] = []

    def push_long(block: str) -> None:
        if len(block) <= max_chars:
            chunks.append(block)
            return
        sentences = re.split(r"(?<=[.!?。！？])\s+", block)
        buf = ""
        for sent in sentences:
            sent = sent.strip()
            if not sent:
                continue
            if len(buf) + len(sent) + 1 <= max_chars:
                buf = f"{buf} {sent}".strip()
            else:
                if buf:
                    chunks.append(buf)
                if len(sent) <= max_chars:
                    buf = sent
                else:
                    # Hard split very long sentence/paragraph.
                    for i in range(0, len(sent), max_chars):
                        part = sent[i : i + max_chars].strip()
                        if part:
                            chunks.append(part)
                    buf = ""
        if buf:
            chunks.append(buf)

    for paragraph in paragraphs:
        push_long(paragraph)
    return chunks


def build_manifest(
    *,
    title: str,
    content_type: str,
    engine: str,
    voice: str,
    rate: int,
    chunks: List[str],
    outputs: List[Path],
    dry_run: bool,
) -> Dict[str, object]:
    return {
        "app": APP_NAME,
        "created_at": datetime.now().isoformat(timespec="seconds"),
        "scope": "private personal-development audio: thesis presentation and FAQ listening",
        "title": title,
        "content_type": content_type,
        "engine": engine,
        "voice": voice or "default",
        "rate": rate,
        "dry_run": dry_run,
        "chunk_count": len(chunks),
        "chunks": [
            {
                "index": i + 1,
                "chars": len(chunk),
                "output": str(outputs[i]) if i < len(outputs) else None,
                "text_preview": chunk[:160],
            }
            for i, chunk in enumerate(chunks)
        ],
        "governance": {
            "public_distribution": False,
            "commercial_use": False,
            "voice_cloning": False,
            "note": "Local Windows SAPI fallback, not Dramabox. If any output is shared outside private use, disclose it as AI/computer-generated audio.",
        },
    }


def _powershell_sapi_script() -> str:
    return r'''
param(
  [Parameter(Mandatory=$true)][string]$Text,
  [Parameter(Mandatory=$true)][string]$Out,
  [int]$Rate = 0,
  [int]$Volume = 100,
  [string]$Voice = ""
)
Add-Type -AssemblyName System.Speech
$synth = New-Object System.Speech.Synthesis.SpeechSynthesizer
$synth.Rate = $Rate
$synth.Volume = $Volume
if ($Voice -and $Voice.Trim().Length -gt 0) {
  $synth.SelectVoice($Voice)
}
$parent = Split-Path -Parent $Out
if ($parent -and !(Test-Path $parent)) { New-Item -ItemType Directory -Force -Path $parent | Out-Null }
$synth.SetOutputToWaveFile($Out)
$synth.Speak($Text)
$synth.Dispose()
'''.strip()


def synthesize_chunk_windows_sapi(text: str, output: Path, *, rate: int = 0, voice: str = "") -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    if not shutil_which("powershell.exe"):
        raise RuntimeError("powershell.exe tidak ditemukan; Windows SAPI backend tidak tersedia.")
    with tempfile.NamedTemporaryFile("w", suffix=".ps1", delete=False, encoding="utf-8") as tmp:
        tmp.write(_powershell_sapi_script())
        script_path = tmp.name
    try:
        cmd = [
            "powershell.exe",
            "-NoProfile",
            "-ExecutionPolicy",
            "Bypass",
            "-File",
            script_path,
            "-Text",
            text,
            "-Out",
            str(output),
            "-Rate",
            str(rate),
            "-Volume",
            "100",
            "-Voice",
            voice or "",
        ]
        result = subprocess.run(cmd, text=True, capture_output=True, timeout=180)
        if result.returncode != 0:
            raise RuntimeError(result.stderr.strip() or result.stdout.strip() or f"powershell exit {result.returncode}")
        if not output.exists() or output.stat().st_size == 0:
            raise RuntimeError(f"Output WAV tidak terbentuk: {output}")
    finally:
        try:
            os.unlink(script_path)
        except OSError:
            pass


def shutil_which(name: str) -> Optional[str]:
    from shutil import which

    return which(name)


def generate_audio(
    *,
    text: str,
    title: str,
    content_type: str,
    output_dir: Path = DEFAULT_OUTPUT_DIR,
    engine: str = "windows_sapi",
    voice: str = "",
    rate: int = 0,
    dry_run: bool = False,
) -> Dict[str, object]:
    chunks = split_text(text)
    if not chunks:
        raise ValueError("Teks kosong; tidak ada audio yang dibuat.")
    safe_title = sanitize_filename(title, default=content_type or "audio")
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    run_dir = output_dir / f"{stamp}-{safe_title}"
    run_dir.mkdir(parents=True, exist_ok=True)
    outputs = [run_dir / f"{safe_title}-{i + 1:03d}.wav" for i in range(len(chunks))]

    if engine != "windows_sapi":
        raise ValueError("Backend yang tersedia saat ini hanya: windows_sapi")

    if not dry_run:
        for chunk, output in zip(chunks, outputs):
            synthesize_chunk_windows_sapi(chunk, output, rate=rate, voice=voice)

    manifest = build_manifest(
        title=title,
        content_type=content_type,
        engine=engine,
        voice=voice,
        rate=rate,
        chunks=chunks,
        outputs=outputs,
        dry_run=dry_run,
    )
    manifest_path = run_dir / "manifest.json"
    manifest["manifest_path"] = str(manifest_path)
    write_json(manifest_path, manifest)
    disclosure = run_dir / "DISCLOSURE.txt"
    disclosure.write_text(
        "Pengungkapan: Audio ini dibuat untuk pembelajaran pribadi dari teks presentasi tesis/FAQ. "
        "Backend MVP saat ini adalah Windows SAPI lokal, bukan Dramabox. Jika dibagikan keluar, "
        "beri label bahwa audio dibuat/dibantu komputer/AI.\n",
        encoding="utf-8",
    )
    return manifest


def write_json(path: Path, data: Dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")


class AppHandler(BaseHTTPRequestHandler):
    def _send_html(self, body: str, status: int = 200) -> None:
        data = body.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self) -> None:  # noqa: N802
        parsed = urlparse(self.path)
        if parsed.path.startswith("/outputs/"):
            return self._serve_output(parsed.path)
        return self._send_html(render_form())

    def do_POST(self) -> None:  # noqa: N802
        length = int(self.headers.get("Content-Length", "0"))
        payload = self.rfile.read(length).decode("utf-8", errors="replace")
        form = parse_qs(payload)
        text = form.get("text", [""])[0]
        title = form.get("title", ["thesis-audio"])[0]
        content_type = form.get("content_type", ["thesis"])[0]
        voice = form.get("voice", [""])[0]
        try:
            rate = int(form.get("rate", ["0"])[0])
        except ValueError:
            rate = 0
        dry_run = form.get("dry_run", [""])[0] == "on"
        try:
            manifest = generate_audio(
                text=text,
                title=title,
                content_type=content_type,
                voice=voice,
                rate=max(-10, min(10, rate)),
                dry_run=dry_run,
            )
            self._send_html(render_result(manifest))
        except Exception as exc:  # web UI should report cleanly
            self._send_html(render_form(error=str(exc), text=text, title=title), status=400)

    def _serve_output(self, request_path: str) -> None:
        rel = request_path.removeprefix("/outputs/")
        target = (DEFAULT_OUTPUT_DIR / rel).resolve()
        base = DEFAULT_OUTPUT_DIR.resolve()
        if not str(target).startswith(str(base)) or not target.exists() or not target.is_file():
            self.send_error(404)
            return
        ctype = "audio/wav" if target.suffix.lower() == ".wav" else "application/octet-stream"
        data = target.read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)


def render_form(error: str = "", text: str = "", title: str = "") -> str:
    return f"""<!doctype html>
<html lang="id">
<head>
<meta charset="utf-8">
<title>{APP_NAME}</title>
<style>
body {{ font-family: Segoe UI, Arial, sans-serif; max-width: 920px; margin: 32px auto; line-height: 1.45; }}
textarea {{ width: 100%; min-height: 260px; font-size: 16px; }}
input, select {{ font-size: 16px; padding: 6px; }}
button {{ font-size: 18px; padding: 10px 16px; }}
.card {{ border: 1px solid #ddd; border-radius: 10px; padding: 16px; margin: 16px 0; }}
.error {{ background: #fff0f0; border-color: #ffb0b0; }}
.note {{ color: #444; }}
</style>
</head>
<body>
<h1>{APP_NAME}</h1>
<p class="note">MVP lokal untuk membuat WAV dari teks presentasi tesis dan FAQ pribadi. Backend saat ini: Windows SAPI lokal. Dramabox tetap disiapkan sebagai rute kualitas lebih tinggi setelah gate PM/hardware.</p>
{f'<div class="card error"><b>Error:</b> {html.escape(error)}</div>' if error else ''}
<form method="post">
<div class="card">
<label>Judul file/run<br><input name="title" value="{html.escape(title or 'tesis-faq-audio')}" style="width:100%"></label><br><br>
<label>Jenis konten<br>
<select name="content_type"><option value="thesis">Presentasi tesis</option><option value="faq">FAQ</option><option value="note">Catatan pribadi</option></select>
</label><br><br>
<label>Voice SAPI opsional (kosongkan untuk default)<br><input name="voice" placeholder="contoh: Microsoft David Desktop" style="width:100%"></label><br><br>
<label>Kecepatan (-10 lambat, 0 normal, 10 cepat)<br><input name="rate" type="number" min="-10" max="10" value="0"></label><br><br>
<label><input type="checkbox" name="dry_run"> Dry run: buat manifest saja, tanpa WAV</label>
</div>
<div class="card">
<label>Teks<br><textarea name="text" placeholder="Tempel teks presentasi tesis atau FAQ di sini...">{html.escape(text)}</textarea></label>
</div>
<button type="submit">Buat audio WAV</button>
</form>
</body>
</html>"""


def render_result(manifest: Dict[str, object]) -> str:
    chunks = manifest.get("chunks", [])
    rows = []
    for chunk in chunks:  # type: ignore[assignment]
        out = chunk.get("output")
        link = "-"
        if out and not manifest.get("dry_run"):
            try:
                rel = Path(out).resolve().relative_to(DEFAULT_OUTPUT_DIR.resolve()).as_posix()
                link = f'<audio controls src="/outputs/{html.escape(rel)}"></audio><br><a href="/outputs/{html.escape(rel)}">download WAV</a>'
            except Exception:
                link = html.escape(str(out))
        rows.append(f"<tr><td>{chunk.get('index')}</td><td>{chunk.get('chars')}</td><td>{link}</td><td>{html.escape(str(chunk.get('text_preview', '')))}</td></tr>")
    manifest_path = html.escape(str(manifest.get("manifest_path", "")))
    return f"""<!doctype html><html lang="id"><head><meta charset="utf-8"><title>Audio selesai</title>
<style>body{{font-family:Segoe UI,Arial,sans-serif;max-width:980px;margin:32px auto}}td,th{{border:1px solid #ddd;padding:8px;vertical-align:top}}table{{border-collapse:collapse;width:100%}}</style></head><body>
<h1>Audio selesai</h1>
<p>Manifest: <code>{manifest_path}</code></p>
<p>Chunk: {manifest.get('chunk_count')} | Backend: {html.escape(str(manifest.get('engine')))} | Dry-run: {manifest.get('dry_run')}</p>
<table><tr><th>#</th><th>Chars</th><th>Audio</th><th>Preview</th></tr>{''.join(rows)}</table>
<p><a href="/">Buat audio lain</a></p>
</body></html>"""


def serve(host: str, port: int) -> None:
    DEFAULT_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    server = ThreadingHTTPServer((host, port), AppHandler)
    print(f"{APP_NAME} running: http://{host}:{port}")
    print(f"Output directory: {DEFAULT_OUTPUT_DIR}")
    server.serve_forever()


def parse_args(argv: Optional[List[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=APP_NAME)
    sub = parser.add_subparsers(dest="command")

    serve_p = sub.add_parser("serve", help="Run local web app")
    serve_p.add_argument("--host", default="127.0.0.1")
    serve_p.add_argument("--port", type=int, default=7860)

    gen_p = sub.add_parser("synthesize", help="Generate WAV chunks from a text file")
    gen_p.add_argument("--input", required=True, help="Input .txt/.md file")
    gen_p.add_argument("--title", default="tesis-faq-audio")
    gen_p.add_argument("--content-type", default="thesis", choices=["thesis", "faq", "note"])
    gen_p.add_argument("--output-dir", default=str(DEFAULT_OUTPUT_DIR))
    gen_p.add_argument("--voice", default="")
    gen_p.add_argument("--rate", type=int, default=0)
    gen_p.add_argument("--dry-run", action="store_true")

    parser.set_defaults(command="serve")
    return parser.parse_args(argv)


def main(argv: Optional[List[str]] = None) -> int:
    args = parse_args(argv)
    if args.command == "serve":
        serve(args.host, args.port)
        return 0
    if args.command == "synthesize":
        text = Path(args.input).read_text(encoding="utf-8")
        manifest = generate_audio(
            text=text,
            title=args.title,
            content_type=args.content_type,
            output_dir=Path(args.output_dir),
            voice=args.voice,
            rate=max(-10, min(10, args.rate)),
            dry_run=args.dry_run,
        )
        print(json.dumps(manifest, indent=2, ensure_ascii=False))
        return 0
    raise SystemExit(f"Unknown command: {args.command}")


if __name__ == "__main__":
    raise SystemExit(main())
