# PROJECT DASHBOARD — Trading Basis Workspace

> Control tower tunggal untuk semua protokol, pekerjaan aktif, dan keputusan operasional.
> Sumber: `PLANS.md`, `docs/process/PROGRESS.md`, `deep-research-report(1).md`, `MASTER_INDEX.md`
> Terakhir diperbarui: 2026-05-17

---

## Status Proyek

| Item | Nilai |
|---|---|
| Progress baseline | **82.25%** (target sprint: 75% — PASS) |
| Branch aktif | `main` → `origin/main` |
| Beads prefix | `Karpathy` |
| Remote | `https://github.com/DanielAdrian975/Karpathy-Protokol.git` |
| PMO Governance Layer | **ACTIVE** (integrated 2026-05-17) |

---

## PMO Governance Layer — Alur Kendali Microtask

> Diadaptasi dari `deep-research-report(1).md`: PMO Microtask Governance dengan model hybrid control tower + dispatch office.

```
INTAKE → TRIAGE → ASSIGNMENT → EXECUTION → CLOSURE
```

| Tahap | Owner di workspace ini | Kontrol utama | SLA baseline |
|---|---|---|---|
| **Intake** | User + Claude Code | Task masuk via `bd create` atau session request | P1: 1 jam; P2: 4 jam; P3: 1 hari |
| **Triage** | TASK_ROUTING.md routing rules | Tentukan protokol: MAS / Boris / C4-ET / Wiki / Autoresearch | Sebelum eksekusi dimulai |
| **Assignment** | Claude Code (session agent) | Pilih skill/mode, alokasikan konteks, set scope | Saat session start |
| **Execution** | Boris Workflow / MAS / Autoresearch | Jalankan sesuai protokol terpilih; log di wiki/log.md | Per task; update status real-time |
| **Closure** | `bd close` + `bd sync` + `git push` | Evidence of done, wiki updated, risk register updated | Sebelum session end |

**RACI workspace:**

| Aktivitas | User | Claude Code | Beads (bd) | Protocol Engine |
|---|---|---|---|---|
| Submit request | R | I | | |
| Triage ke protokol | | R/A | | C |
| Assign mode/skill | | R/A | C | C |
| Eksekusi task | | R | I | A |
| Log & update wiki | | R | I | |
| Closure & push | C | R | A | |

---

## Matrix Protokol

> Enam protokol aktif. Setiap task harus melewati triage sebelum eksekusi.

### 1. LLM Wiki Karpathy — Knowledge Management
- **Lokasi**: `wiki/`, `LLM Wiki Karpathy/`
- **Trigger**: Ingest docs, decisions, meeting notes, durable research
- **Alur**: Index dulu (`wiki/index.md`) → frontmatter → 3-5 kalimat ringkasan → append `wiki/log.md`
- **Status**: Root scaffold aktif; legacy wiki (`LLM Wiki Karpathy/`) belum dimigrasikan
- **Gap**: Rekonsiliasi legacy ↔ root wiki masih open
- **Output kunci**: `wiki/index.md`, `wiki/log.md`, `wiki/schema.md`

### 2. MAS Evidence-First + C4-ET Gate — Analisis & Keputusan
- **Lokasi**: `Bahan/Knowledge_Management_System/Claude CLI/02_MAS_System/`, `03_C4ET_Framework/`
- **Trigger MAS**: Klaim faktual, kausal, performa, compliance, benchmark
- **Trigger C4ET**: Kapasitas tim, WIP, bottleneck, lead-time — bukan default semua analisis
- **Alur MAS**: Assessor → Retriever Academic → Retriever Official → Redteam → Judge
- **Alur C4ET**: Data audit (A1-A4) → Metrics (B1-B4) → Gate decision (ET1-ET3) → One-pager
- **Status**: Trial selesai; `MAS_EVIDENCE_PACKET_TRIAL.md` & `C4ET_SOURCE_CORPUS_GATE.md` validated
- **Output kunci**: Evidence packets, atomic claims, judge verdict, gate decision one-pager

### 3. Boris Workflow — Implementasi
- **Trigger**: Semua coding, TradingView MCP operations, Pine Script development, multi-step implementation
- **Alur**: Plan Mode → Execute → Verify
- **Rules**:
  - `chart_get_state` pertama sebelum semua MCP calls — simpan entity IDs
  - `summary=true` pada `data_get_ohlcv`
  - `study_filter=` pada semua pine tools
  - Tidak boleh skip verify step
- **Status**: Aktif; digunakan untuk semua TradingView MCP work
- **Output kunci**: Plan artifact, implementation, test/verify result

### 4. Autoresearch — Research Loop
- **Lokasi**: `_tmp_autoresearch_template/autoresearch_template_python_mas_c4et_boris/`
- **Trigger**: Research tasks yang membutuhkan iterasi; optimization loops; benchmark research
- **Alur**: Research plan → retrieval log → synthesis → citations → unresolved claims
- **Status**: Template initialized; `AUTORESEARCH_ARTIFACT_TRIAL.md` validated
- **Skill tersedia**: `autoresearch-optimize` di `_tmp_autoresearch_template/.../.claude/skills/`
- **Output kunci**: Research artifact dengan scope, evidence table, confidence score, unresolved claims

### 5. Skills — Automated Workflow Inventory
- **Lokasi root**: `skills/`, `_tmp_skills_modular_build/`, `_tmp_autoresearch_template/`
- **Status**: Map initialized; validation pending untuk installed skills

| Skill | Trigger | Lokasi |
|---|---|---|
| `/trading-research-wiki` | Trading data input | global skill |
| `/mas-orchestrator` | Full MAS pipeline | global skill |
| `/graphify` | Any input → knowledge graph | `~/.claude/skills/graphify/` |
| `/atomic-journal` | Journal/log request | global skill |
| `/pipeline-fx` | FX signal pipeline | MASTER_INDEX.md |
| `/pipeline-mas` | MAS hemat token | MASTER_INDEX.md |
| `/pipeline-plan` | Boris Phase 1 | MASTER_INDEX.md |
| `/pipeline-execute` | Boris execute phase | MASTER_INDEX.md |
| `autoresearch-optimize` | Research loop optimization | `_tmp_autoresearch_template/` |
| `c4et-onepager` | C4-ET decision one-pager | `_tmp_autoresearch_template/` |
| `boris-workflow` | Plan→Execute→Verify | global skill |

### 6. Project Management — Beads + Process Docs
- **Sistem**: `bd` (beads), prefix `Karpathy`, sync ke remote
- **Process docs**: `docs/process/` — OPERATING_SYSTEM.md, TASK_ROUTING.md, QUALITY_GATES.md, DECISION_LOG.md
- **Alur harian**: `bd ready` → `bd update --status=in_progress` → kerja → `bd close` → `bd sync` → `git push`
- **Status**: Operational; remote push aktif ke `origin/main`

---

## PMO KPI Dashboard — Metrik Workspace

> Diadaptasi dari threshold KPI `deep-research-report(1).md`. Target baseline untuk workspace ini.

| Metrik | Definisi workspace | Target hijau | Status saat ini |
|---|---|---|---|
| **Intake completeness** | % tasks masuk via `bd create` atau formal session request (bukan hanya chat) | ≥ 80% | Belum diukur |
| **Triage routing accuracy** | % tasks yang langsung ke protokol yang tepat tanpa re-routing | ≥ 90% | Belum diukur |
| **Closure rate** | % tasks yang di-close dengan evidence of done (wiki update + bd close + push) | ≥ 75% | Estimasi ~70% |
| **Hidden work ratio** | % pekerjaan yang dikerjakan tanpa `bd` issue atau formal tracking | ≤ 10% | Belum diukur |
| **Reopen rate** | % tasks yang di-close lalu muncul lagi sebagai masalah | ≤ 5% | Tidak ada data |
| **Wiki freshness** | % protocol trials/decisions yang masuk `wiki/log.md` dalam sesi yang sama | ≥ 85% | ~75% |
| **Protocol compliance** | % tasks yang mengikuti protokol yang ditentukan TASK_ROUTING.md | ≥ 90% | Estimasi ~80% |
| **Context switching index** | Rata-rata jumlah protokol berbeda per sesi | ≤ 3 per sesi | ~3-4 |

---

## Progress Scorecard

> Sumber: `docs/process/PROGRESS.md` — last updated 2026-05-16

| Area | Bobot | Score | Status |
|---|---:|---:|---|
| Constitution & routing | 15% | 100% | DONE |
| Wiki memory discipline | 20% | 75% | Legacy migration open |
| MAS evidence workflow | 20% | 75% | Trial validated |
| AutoResearch workflow | 15% | 75% | Trial validated |
| C4-ET gate discipline | 10% | 75% | NO-GO for corpus staging |
| Skills workflow map | 10% | 85% | Installed validation pending |
| Git/bd operational closure | 10% | 100% | DONE |
| **TOTAL** | **100%** | **82.25%** | **PASS (target 75%)** |

---

## Pekerjaan Aktif & Antrian

> Format: `[Prioritas] Task — Protokol — Owner — Status`

### In Progress
- `[P2]` Pilih authoritative implementation subproject — Boris Workflow — Claude Code — BLOCKED (user decision needed)

### Antrian Siap
- `[P2]` Jalankan GO-TRIAL implementasi pada subproject terpilih — Boris Workflow
- `[P3]` Rekonsiliasi legacy wiki (`LLM Wiki Karpathy/`) dengan root `wiki/` — Wiki Maintenance
- `[P3]` Validasi installed skills di workspace — Skills review
- `[P3]` Tetapkan canonical test command untuk root verification — Implementation

### Blocked (menunggu keputusan)
- `[P2]` Staging source corpus subprojects — C4-ET NO-GO aktif; butuh explicit provenance audit
- `[P3]` Nested Git treatment (`Bahan/Karpathy RAG system/llm-wiki/.git`) — butuh user decision

---

## Risk Register Summary

> Sumber: `docs/process/RISK_REGISTER.md` + analisis PMO `deep-research-report(1).md`

| Risk | Probabilitas | Dampak | Mitigasi |
|---|---|---|---|
| Hidden work tidak ter-track (pekerjaan lewat chat tanpa `bd` issue) | Tinggi | Medium | Enforce intake via `bd create` setiap session start |
| Legacy wiki diverge dari root wiki | Medium | Medium | Schedule rekonsiliasi sebelum ingest baru |
| Protocol mismatch (task salah diRoute) | Medium | Medium | Review TASK_ROUTING.md setiap session start |
| Source corpus staging tanpa provenance audit | Rendah | Tinggi | C4-ET NO-GO tetap berlaku |
| Skill validation tertinggal dari implementasi | Medium | Rendah | Run validation after each new skill install |
| Context window overload (> 3 file per query) | Medium | Medium | Ikuti routing rules: index → topic → target |

---

## Navigasi Cepat

| Kebutuhan | File | Protokol |
|---|---|---|
| Routing task baru | `docs/process/TASK_ROUTING.md` | — |
| Quality gate check | `docs/process/QUALITY_GATES.md` | — |
| Decision log | `docs/process/DECISION_LOG.md` | — |
| Progress update | `docs/process/PROGRESS.md` | — |
| Risk update | `docs/process/RISK_REGISTER.md` | — |
| PMO governance referensi | `deep-research-report(1).md` | — |
| MAS template | `docs/process/MAS_EVIDENCE_PACKET_TEMPLATE.md` | MAS |
| AutoResearch template | `docs/process/AUTORESEARCH_ARTIFACT_TEMPLATE.md` | Autoresearch |
| C4-ET gate | `docs/process/C4ET_SOURCE_CORPUS_GATE.md` | C4-ET |
| TradingView MCP | `MASTER_INDEX.md` — TradingView section | Boris |
| Wiki index | `wiki/index.md` | Wiki |

---

## Session Close Checklist (PMO Closure Gate)

```
[ ] 1. git status                    — periksa perubahan
[ ] 2. git add <files>               — stage hanya file yang relevan
[ ] 3. bd sync                       — commit beads changes
[ ] 4. git commit -m "..."           — commit code/docs
[ ] 5. bd sync                       — commit beads post-commit changes
[ ] 6. git push                      — push ke origin/main
[ ] 7. wiki/log.md updated           — semua durable knowledge masuk wiki
[ ] 8. PROGRESS.md updated           — score diperbarui jika ada perubahan
```

---

## PMO Governance Reference — Sumber

> `deep-research-report(1).md` — Desain Organisasi PMO Untuk Microtask Governance Lintas Proyek

**Inti rekomendasi yang diadopsi di workspace ini:**
1. Semua microtask harus melewati intake → triage sebelum eksekusi
2. Setiap task harus punya satu Accountable Owner (user atau Claude Code)
3. Hidden work = pekerjaan tanpa ID/ticket — harus diminimalkan dengan enforce `bd create`
4. Dashboard mengukur bukan hanya throughput, tapi juga hidden work ratio, reopen rate, protocol compliance
5. Closure semu (ditutup tanpa evidence) harus dicegah dengan closure gate checklist di atas

**Kapabilitas tooling yang digunakan:**
- Beads (`bd`) = system-of-record untuk task tracking (analog Jira/ClickUp)
- `docs/process/` = governance docs layer
- `wiki/` = knowledge base dan audit trail
- Claude Code skills = automation layer untuk repeated workflows
- TradingView MCP = execution surface untuk trading research

---

*Dashboard ini adalah living document. Update setelah setiap task closure atau protocol change.*
*Format: `[Sumber] → [Temuan] → [Batasan/Ketidakpastian]`*
