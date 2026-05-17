# PROJECT START PROMPT — Trigger Aktivasi Semua Protokol

> Salin prompt di bawah ini ke awal sesi baru. Sesuaikan bagian `[...]` dengan konteks proyek.
> Prompt ini mengaktifkan: PMO Governance · LLM Wiki · MAS+C4ET · Boris Workflow · Autoresearch · Skills

---

## PROMPT (salin seluruhnya)

---

```
Kita memulai project baru. Jalankan full protocol activation sequence berikut sebelum menerima task apapun.

---

## CONTEXT

Nama project    : [nama project]
Domain          : [trading research / analisis medis / software / lainnya]
Goal utama      : [satu kalimat tujuan]
Output target   : [deliverable yang diharapkan: wiki / laporan / kode / dashboard / lainnya]
Deadline/urgency: [ada/tidak; jika ada, sebutkan]
Scope:
  - [item scope 1]
  - [item scope 2]
Constraint:
  - [misal: no external API, data hanya dari folder X, tidak ada buy/sell advice]

---

## STEP 1 — PMO INTAKE

Sebelum mengerjakan apapun:
1. Buat beads issue: `bd create --title="[nama project]: [goal singkat]" --type=feature --priority=2`
2. Set ke in_progress: `bd update <id> --status=in_progress`
3. Baca `PROJECT_DASHBOARD.md` untuk memahami current workspace state
4. Baca `MASTER_INDEX.md` untuk routing cepat
5. Konfirmasi: apakah ada blocking issue atau open risk yang relevan?

---

## STEP 2 — TRIAGE & PROTOCOL ROUTING

Tentukan protokol primer berdasarkan TASK_ROUTING.md:

| Jika task mengandung... | Gunakan protokol |
|---|---|
| Klaim faktual, causal, benchmark, compliance | MAS Evidence-First → assessor → retrieval → redteam → judge |
| Keputusan kapasitas/tim/bottleneck | C4-ET Gate → A1-A4 → B1-B4 → ET1-ET3 → one-pager |
| Coding, MCP operations, implementasi | Boris Workflow → Plan Mode → Execute → Verify |
| Research iteratif, optimization loop | Autoresearch → plan → retrieval → synthesis → unresolved |
| Ingest docs/decisions ke memori | Wiki Maintenance → index → frontmatter → log entry |
| Review, audit, readiness | Review/Audit → findings → severity → residual risk |

Nyatakan eksplisit: "Protokol primer yang digunakan: [X]. Alasan: [Y]."

---

## STEP 3 — SCOPE & RISK PLAN

Sebelum menulis satu baris pun:
- Goal yang akan dicapai sesi ini: [...]
- File yang akan dibaca (maks 3): [...]
- File yang akan ditulis/diubah: [...]
- Quality gate yang akan digunakan: `docs/process/QUALITY_GATES.md`
- Risiko yang teridentifikasi: [...]
- Progress metric yang diharapkan berubah: [...]

---

## STEP 4 — EKSEKUSI

Jalankan sesuai protokol primer. Rules wajib:

### Jika Boris Workflow (implementasi/MCP):
- Mulai dengan Plan Mode (`/plan` atau explicit planning artifact)
- TradingView: `chart_get_state` PERTAMA, simpan entity IDs, jangan panggil ulang
- `summary=true` pada semua `data_get_ohlcv`
- `study_filter=` pada semua pine tools
- Verify step wajib sebelum closure

### Jika MAS Evidence-First:
- Assessor mendefinisikan atomic claims terlebih dahulu
- Setiap klaim harus punya primary source (bukan inferensi)
- Redteam wajib sebelum judge
- Output: `[Sumber] → [Temuan] → [Batasan]`
- Jika data tidak cukup → output "Insufficient Evidence", jangan lanjutkan

### Jika C4-ET Gate:
- Jalankan hanya jika trigger: kapasitas/tim/WIP/bottleneck/lead-time
- A1-A4 checklist → B1-B4 metrics → ET1-ET3 → GO/NO-GO/GO-TRIAL
- Output: one-pager decision artifact

### Jika Autoresearch:
- Definisikan research question dan scope sebelum retrieval
- Evidence table dengan source, claim, confidence per item
- Unresolved claims harus eksplisit di output akhir

### Jika Wiki Maintenance:
- Index dulu, ringkasan 3-5 kalimat, frontmatter lengkap
- Update `wiki/index.md` dan append `wiki/log.md`
- Jangan buka seluruh subfolder; routing: global index → topic index → target file

---

## STEP 5 — SKILL ACTIVATION (jika relevan)

Gunakan skill yang tersedia:

| Kebutuhan | Skill |
|---|---|
| Trading hypothesis + evidence | `/trading-research-wiki` |
| Full MAS pipeline | `/mas-orchestrator` |
| Input apapun → knowledge graph | `/graphify` |
| Journal keputusan | `/atomic-journal` |
| C4-ET one-pager | `/c4et-onepager` |
| Research loop optimization | `autoresearch-optimize` |
| Boris plan phase | `/pipeline-plan` |

---

## STEP 6 — CLOSURE GATE (wajib sebelum selesai)

Jalankan checklist ini sebelum menyatakan "selesai":

```
[ ] Task di-close di beads: bd close <id>
[ ] Wiki diperbarui: wiki/log.md append, wiki/index.md update jika ada entri baru
[ ] PROGRESS.md diperbarui jika ada perubahan score
[ ] RISK_REGISTER.md diperbarui jika ada risiko baru/tertutup
[ ] DECISION_LOG.md diperbarui jika ada keputusan material
[ ] git status → hanya file relevan yang di-stage
[ ] git add <files> → NO broad git add .
[ ] bd sync
[ ] git commit -m "..." (pesan commit: what + why)
[ ] bd sync (post-commit)
[ ] git push
```

---

## GUARDRAILS (berlaku seluruh sesi)

- Trading research only — tidak ada buy/sell/hold/leverage recommendation
- Tidak membaca file credential (`Bahan/.streamlit/`, `.env`, `secrets.*`)
- Tidak staging broad source corpus (`Bahan/`, `LLM Wiki Karpathy/`, `_tmp_*`) kecuali ada explicit provenance audit
- Maksimal 3 file per query (MCP tool calls tidak dihitung)
- Archive folder (`99_Archive`, `_archive`, `raw`) hanya jika diminta eksplisit
- Format semua output: `[Sumber] → [Temuan] → [Batasan/Ketidakpastian]`

---

Konfirmasi dengan menjawab:
1. Protokol primer yang dipilih dan alasannya
2. Scope eksekusi sesi ini (file yang akan dibaca/ditulis)
3. Blocking issue atau risiko yang teridentifikasi sebelum mulai

Jangan eksekusi task apapun sebelum konfirmasi ini selesai.
```

---

## VERSI PENDEK (minimal, untuk task sederhana)

```
Project baru: [nama]. Goal: [satu kalimat].
Jalankan protocol activation:
1. bd create untuk issue tracking
2. Baca PROJECT_DASHBOARD.md
3. Tentukan protokol primer (MAS / Boris / C4ET / Wiki / Autoresearch)
4. Nyatakan scope sebelum eksekusi
5. Jalankan closure gate sebelum selesai (bd close → wiki → commit → push)
Konfirmasi protokol dan scope sebelum mulai.
```

---

## MAPPING PROTOKOL → ARTIFACT OUTPUT

| Protokol | Artifact wajib di output |
|---|---|
| MAS Evidence-First | Atomic claims + evidence table + judge verdict |
| C4-ET Gate | A1-A4 checklist + B1-B4 metrics + GO/NO-GO one-pager |
| Boris Workflow | Plan artifact + implementation + verify result |
| Autoresearch | Research question + evidence table + synthesis + unresolved claims |
| Wiki Maintenance | Index entry + log entry + frontmatter |
| Review/Audit | Findings + severity + residual risk |
| PMO Closure | bd close + wiki update + commit + push |

---

*Prompt ini merefleksikan: `PROJECT_DASHBOARD.md`, `CLAUDE.md`, `TASK_ROUTING.md`, `deep-research-report(1).md`*
*Terakhir diperbarui: 2026-05-18*
