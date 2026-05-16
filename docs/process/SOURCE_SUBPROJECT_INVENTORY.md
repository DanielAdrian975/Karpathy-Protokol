# Source And Subproject Inventory Decision

Date: 2026-05-16
Mode: Review/Audit + Wiki Maintenance
Scope: large source corpus, nested projects, `.gitattributes`, `_tmp*/`, generated/output folders, and source/document folders before the next staging batch.

## Inventory Summary

- Git root: `C:\Users\Gysje P\Documents\Adi File\Karpathy`
- Current remote: none
- Local `bd`: initialized and healthy; no `bd sync` run
- Files larger than 10MB: none found
- Nested `.git` directories:
  - `.git`
  - `Bahan\Karpathy RAG system\llm-wiki\.git`
- Build/test markers:
  - `Bahan\Enhance Pengetahuan Ekstraktor\requirements.txt`
  - `_tmp_autoresearch_template\autoresearch_template_python_mas_c4et_boris\requirements.txt`
- Archive/media/data counts:
  - `.csv`: 43
  - `.zip`: 15
  - `.db`: 2
  - `.canvas`: 2
  - `.vtt`: 1
- Credential-like filenames:
  - `Bahan\.streamlit\mt5_secrets.toml`
  - `Bahan\.streamlit\Pass MT5 demo.txt`
  - `Bahan\.streamlit\Pass MT5 real.txt`
  - `Bahan\.streamlit\secrets.toml`
  - `LLM Wiki Karpathy\03_WIKI\entities\mt5-integration.md` is a documentation filename match, not a credential file by name, but may contain sensitive trading account references and needs content review before staging.

## `.gitattributes` Decision

Current content:

```text
# Use bd merge for beads JSONL files
.beads/issues.jsonl merge=beads
```

Decision: safe to commit in a future process metadata batch.

Rationale:

- It does not configure Git LFS.
- It only declares the `bd` merge driver for `.beads/issues.jsonl`.
- It is useful once `.beads/issues.jsonl` is tracked.
- It is safe before remote configuration because it does not depend on a remote.

Git LFS decision: not needed now. No files larger than 10MB were found, and archive/media/data files are not approved for staging.

Follow-up status: `.gitattributes`, `CLAUDE.md`, and `MASTER_INDEX.md` passed a curated source docs staging audit and were committed locally in `8d284b6`. No large source corpus was staged.

## Decision Table

| Path | Type | Risk | Recommended Treatment | Staging Decision |
|---|---|---|---|---|
| `.gitattributes` | Git metadata | Low | Commit as process metadata in next selective batch | GO next batch |
| `Bahan\.streamlit\*` | Credentials/config secrets | Critical | Ignore permanently; never version | NO-GO |
| `Bahan\Enhance Pengetahuan Ekstraktor\` | Python source subproject + local data | High | Separate source audit; commit source only after excluding DB/data/secrets | NO-GO now |
| `Bahan\Enhance Pengetahuan Ekstraktor\memory_storage\*.db` | Local DB | High | Ignore permanently or move to external data storage | NO-GO |
| `Bahan\Karpathy RAG system\llm-wiki\.git` | Nested Git repo | High | Submodule candidate or separate repo; do not flatten accidentally | NO-GO now |
| `Bahan\Karpathy RAG system\` | Mixed RAG/wiki source corpus | Medium | Raw source archive or separate repo after provenance review | NO-GO now |
| `Bahan\Knowledge_Management_System\` | Mixed docs, schemas, examples, archives, scripts | Medium | Raw source archive or separate repo after inventory | NO-GO now |
| `Bahan\llm-wiki-*` | Copied wiki subprojects/templates | Medium | Separate repo candidate or curated import only | NO-GO now |
| `Bahan\Youtube Video Extractor Hermes\` | Scripts and research notes | Medium | Separate source audit; decide if active source | NO-GO now |
| `Bahan\*.zip`, `skills_modular_build(1).zip` | Archives | Medium | Ignore; extract only curated content into tracked docs if needed | NO-GO |
| `_tmp_autoresearch_template\` | Temporary/template workspace | Medium | Keep ignored; copy curated templates into `docs/process/` only | NO-GO |
| `_tmp_skills_modular_build\` | Generated skill bundle | Medium | Keep ignored; copy curated skill map into `skills/README.md` only | NO-GO |
| `LLM Wiki Karpathy\` | Legacy compiled wiki | Medium | Candidate for curated source commit after sensitivity/provenance review | HOLD |
| `Claude Up Skills\` | Skill reference docs | Low/Medium | Candidate for curated source commit after review | HOLD |
| `CLAUDE.md`, `MASTER_INDEX.md` | Root legacy orientation docs | Low/Medium | Candidate for next selective source-doc batch after encoding/sensitivity review | HOLD |
| `docs/process\*`, `wiki\*`, `skills\README.md` | Process operating system | Low | Already committed / continue tracking | GO |

## Batch Recommendations

### Approved For Next Batch

- Process log reconciliation only; `.gitattributes`, `CLAUDE.md`, and `MASTER_INDEX.md` are already committed in `8d284b6`.

### Hold For Separate Review

- `LLM Wiki Karpathy\`
- `Claude Up Skills\`
- `Bahan\Enhance Pengetahuan Ekstraktor\`
- `Bahan\Youtube Video Extractor Hermes\`

### Keep Ignored

- `Bahan\.streamlit\*`
- `*.db`
- `*.zip`
- `_tmp*/`
- generated/output/build/cache folders
- media/data files until a data policy exists

## Next Loop Prompt

Use this prompt for the next source staging loop:

```text
Lakukan Curated Source Docs Staging Audit.

JANGAN push, jangan bd sync, jangan git add ., jangan staging source corpus besar.

Scope hanya:
- .gitattributes
- CLAUDE.md
- MASTER_INDEX.md

Tugas:
1. Baca file.
2. Cek encoding/mojibake.
3. Cek credential-like content.
4. Cek apakah aman sebagai orientation docs.
5. Jika aman, stage path eksplisit saja.
6. Jalankan git diff --cached --check, --name-only, --stat.
7. Commit lokal jika aman.

Output: GO/NO-GO, staged files, commit hash bila berhasil, risiko tersisa.
```
