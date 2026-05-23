# Thesis/FAQ Text-to-Audio App

MVP lokal untuk kebutuhan Gysje: mengubah teks presentasi tesis dan FAQ menjadi audio WAV untuk pembelajaran pribadi.

Status:

- Backend aktif: Windows SAPI lokal via `powershell.exe` + `System.Speech`.
- Tidak butuh install Python package tambahan.
- Tidak mengunduh model besar.
- Dramabox belum dijalankan di app ini; Dramabox tetap rute kualitas/ekspresif berikutnya setelah gate PM/hardware.

## Menjalankan aplikasi web

Dari root repo Karpathy:

```bash
python apps/thesis_faq_audio_app/app.py serve --host 127.0.0.1 --port 7860
```

Buka:

```text
http://127.0.0.1:7860
```

Isi:

1. Judul run/file.
2. Jenis konten: presentasi tesis / FAQ / catatan.
3. Teks yang ingin dijadikan audio.
4. Klik `Buat audio WAV`.

Output berada di:

```text
apps/thesis_faq_audio_app/outputs/<timestamp>-<judul>/
```

Setiap run berisi:

- `*.wav` per chunk teks
- `manifest.json`
- `DISCLOSURE.txt`

## CLI: generate dari file teks

```bash
python apps/thesis_faq_audio_app/app.py synthesize \
  --input path/to/teks_tesis.txt \
  --title tesis-bab-1 \
  --content-type thesis
```

Dry-run tanpa membuat WAV:

```bash
python apps/thesis_faq_audio_app/app.py synthesize \
  --input path/to/teks_tesis.txt \
  --title tes-manifest \
  --dry-run
```

## Batasan penting

- Ini bukan Dramabox; ini fallback lokal agar workflow tesis/FAQ bisa langsung berjalan.
- Kualitas Bahasa Indonesia tergantung voice Windows yang tersedia di mesin.
- Voice cloning tidak digunakan.
- Untuk output yang dibagikan keluar dari penggunaan pribadi, beri disclosure bahwa audio dibuat/dibantu komputer/AI.
- Jika nanti menggunakan Dramabox, gunakan `docs/process/DRAMABOX_EXPERIMENT_LOG.md` untuk mencatat prompt, seed, parameter, model SHA, route, watermark, output path, dan catatan dengar.

## PM alignment

Sesuai PM Dramabox:

- Phase 1 `Karpathy-cwq`: capability map tanpa install selesai.
- App ini adalah hidden-potential MVP: private thesis/FAQ audio dapat berjalan tanpa menunggu 24GB VRAM/Dramabox install.
- Phase 2 berikutnya: prompt library untuk thesis/FAQ Indonesian narration.
- Phase 3 berikutnya: route Dramabox/Space/hosted/local setelah hardware dan availability check.

## Test

Unit test ringan:

```bash
python -m unittest apps.thesis_faq_audio_app.test_app
```

Smoke test audio kecil:

```bash
printf 'Halo Gysje. Ini tes audio singkat untuk presentasi tesis.' > /tmp/tts-smoke.txt
python apps/thesis_faq_audio_app/app.py synthesize --input /tmp/tts-smoke.txt --title smoke-test --content-type thesis
```

Jika sukses, cek path WAV pada JSON output dan buka file WAV tersebut.
