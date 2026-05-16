# Risk Register

| ID | Risk | Impact | Likelihood | Status | Mitigation |
|---|---|---:|---:|---|---|
| R-0001 | Workspace is nested inside parent Git repo `C:\Users\Gysje P`, but now also has a project-local Git root. | High | Medium | Mitigated | Run Git only from `C:\Users\Gysje P\Documents\Adi File\Karpathy`; never stage Karpathy from the parent repo. |
| R-0002 | Parent `bd` repository ID mismatch may corrupt sync if accidentally used. | High | Medium | Mitigated | Project-local `bd` is initialized; do not run `bd` from parent root and do not run `bd sync` until project remote/upstream is safe. |
| R-0003 | No canonical root test/lint/build command exists. | Medium | High | Open | Define quality gates per subproject and root docs-only verification. |
| R-0004 | Existing source tree contains credential-like files. | High | Medium | Open | Avoid reading secrets; document protected paths; consider `.gitignore` review after repo ownership is fixed. |
| R-0005 | Legacy wiki and new root wiki may diverge. | Medium | High | Open | Migrate or cross-index with explicit SourceIDs and log entries. |
| R-0006 | Some Markdown output appears mojibake in terminal. | Medium | Medium | Open | Audit file encodings before broad edits; avoid blind rewrite of existing docs. |
| R-0007 | Trading research may be mistaken for advice. | High | Medium | Open | Keep research-only guardrails in `AGENTS.md`; mark stale data as `Insufficient Evidence`. |
| R-0008 | MAS/C4-ET/AutoResearch workflows may be over-applied. | Medium | Medium | Mitigated | Use trigger matrix in `AGENTS.md`, `docs/process/TASK_ROUTING.md`, and `docs/process/QUALITY_GATES.md`. |
| R-0009 | Karpathy contains nested or copied Git-enabled subprojects that may complicate a new root repository. | Medium | Medium | Open | Initial inventory found `Bahan\Karpathy RAG system\llm-wiki\.git`; do not stage nested source trees until submodule/ignore/flatten decision is made. |
| R-0010 | Karpathy Git repository has no remote or upstream configured. | Medium | High | Open | Local selective commits are possible, but push and `bd sync` remain blocked until a correct project remote is configured. |
| R-0011 | Large untracked source/document corpus remains outside the first commit. | Medium | High | Open | Keep first commit process-only; run separate source inventory before staging `Bahan/`, legacy wiki folders, or generated/template bundles. |
