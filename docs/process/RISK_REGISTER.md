# Risk Register

| ID | Risk | Impact | Likelihood | Status | Mitigation |
|---|---|---:|---:|---|---|
| R-0001 | Workspace is nested inside parent Git repo `C:\Users\Gysje P`, but now also has a project-local Git root. | High | Medium | Mitigated | Run Git only from `C:\Users\Gysje P\Documents\Adi File\Karpathy`; never stage Karpathy from the parent repo. |
| R-0002 | Parent `bd` repository ID mismatch may corrupt sync if accidentally used. | High | Medium | Mitigated | Project-local `bd` is initialized and synced with `origin/main`; continue running `bd` only from the Karpathy root. |
| R-0003 | No canonical root test/lint/build command exists. | Medium | High | Open | Define quality gates per subproject and root docs-only verification. |
| R-0004 | Existing source tree contains credential-like files. | High | Medium | Open | Avoid reading secrets; document protected paths; consider `.gitignore` review after repo ownership is fixed. |
| R-0005 | Legacy wiki and new root wiki may diverge. | Medium | High | Open | Migrate or cross-index with explicit SourceIDs and log entries. |
| R-0006 | Some Markdown output appears mojibake in terminal. | Medium | Medium | Open | Audit file encodings before broad edits; avoid blind rewrite of existing docs. |
| R-0007 | Trading research may be mistaken for advice. | High | Medium | Open | Keep research-only guardrails in `AGENTS.md`; mark stale data as `Insufficient Evidence`. |
| R-0008 | MAS/C4-ET/AutoResearch workflows may be over-applied. | Medium | Medium | Mitigated | Use trigger matrix in `AGENTS.md`, `docs/process/TASK_ROUTING.md`, and `docs/process/QUALITY_GATES.md`. |
| R-0009 | Karpathy contains nested or copied Git-enabled subprojects that may complicate a new root repository. | Medium | Medium | Open | Initial inventory found `Bahan\Karpathy RAG system\llm-wiki\.git`; do not stage nested source trees until submodule/ignore/flatten decision is made. |
| R-0010 | Karpathy Git repository had no remote or upstream configured. | Medium | High | Mitigated | User-approved `origin` is configured as `https://github.com/DanielAdrian975/Karpathy-Protokol.git`; branch `main` tracks `origin/main`. |
| R-0011 | Large untracked source/document corpus remains outside the first commit. | Medium | High | Open | Keep first commit process-only; run separate source inventory before staging `Bahan/`, legacy wiki folders, or generated/template bundles. |
| R-0012 | Credential-like files exist in the source corpus under `Bahan\.streamlit`. | High | High | Mitigated | `.gitignore` excludes `Bahan/.streamlit/`; keep this path permanently NO-GO for staging. |
| R-0013 | Source corpus includes archives, local DBs, generated bundles, and copied subprojects. | Medium | High | Open | Stage only curated batches after inventory; keep `_tmp*/`, archives, DB files, and generated folders ignored. |
| R-0014 | `.gitattributes` was needed for durable `bd` JSONL merge behavior. | Low | Medium | Mitigated | Committed in `8d284b6` with curated orientation docs; no Git LFS is needed now. |
| R-0015 | Local Git line-ending settings warn that LF files may be rewritten as CRLF when Git touches them. | Low | Medium | Open | Decide later whether to enforce Markdown text eol rules in `.gitattributes`; do not broaden the current staging scope for this. |
| R-0016 | Push target was undefined because the project had no configured remote or upstream. | High | High | Mitigated | First push to `origin/main` succeeded after the user provided the Karpathy-Protokol remote URL. |
| R-0017 | Implementation work could run the wrong tests because no authoritative subproject or root test command exists. | Medium | High | Open | Use docs/process structural checks for process work; stop before implementation until subproject and test command are selected. |
| R-0018 | Broad source corpus staging has excessive WIP and multiple risk classes. | High | High | Open | Follow C4-ET NO-GO; continue only narrow curated audits and explicit staging. |
| R-0019 | GitHub CLI auth has multiple accounts and can time out when listing repositories. | Low | Medium | Open | Prefer explicit user-provided remote URLs and `git ls-remote` verification over repo-name guessing. |
