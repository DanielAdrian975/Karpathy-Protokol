# Wiki Log

Append-only log for root wiki activity.

## 2026-05-16 | init | root-wiki-scaffold | Process initialization

Created root wiki scaffold requested by Project Process Orchestrator:

- `wiki/index.md`
- `wiki/log.md`
- `wiki/schema.md`
- `wiki/raw/README.md`

No raw sources were ingested. Legacy wiki material remains in `LLM Wiki Karpathy/`.

## 2026-05-16 | decision | AGENTS.md | Adopt operating constitution

Replaced the initial root `AGENTS.md` draft with the user-supplied Project Operating Constitution. Filled the repository orientation section using observed workspace facts. No raw sources were ingested.

## 2026-05-16 | decision | process-os | Universal task operating system

Added a reusable process layer for all task types:

- `docs/process/OPERATING_SYSTEM.md`
- `docs/process/TASK_ROUTING.md`
- `docs/process/QUALITY_GATES.md`

Updated `AGENTS.md`, `PLANS.md`, `skills/README.md`, and `wiki/index.md` so future sessions can route tasks, verify quality gates, and report progress consistently. No raw sources were ingested.

## 2026-05-16 | decision | evidence-research-templates | MAS and AutoResearch templates

Added reusable root templates:

- `docs/process/MAS_EVIDENCE_PACKET_TEMPLATE.md`
- `docs/process/AUTORESEARCH_ARTIFACT_TEMPLATE.md`

Updated process progress, decision log, and wiki index. No raw sources were ingested.

## 2026-05-16 | decision | process-go-trial-review | Review/Audit validation

Ran a GO-TRIAL universal process validation on a small Review/Audit task: consistency review across `AGENTS.md`, `OPERATING_SYSTEM.md`, `TASK_ROUTING.md`, `QUALITY_GATES.md`, `PLANS.md`, and `PROGRESS.md`.

Corrected stale process references in `PLANS.md`, updated progress scoring in `docs/process/PROGRESS.md`, and recorded decision `D-0008`. Gate 6 remains blocked by repository boundary and `bd` mismatch. No raw sources were ingested.

## 2026-05-16 | decision | repository-boundary-audit | Boundary repair decision

Ran a read-only Repository Boundary Repair Audit. Findings:

- Current working directory is `C:\Users\Gysje P\Documents\Adi File\Karpathy`.
- Actual Git root is `C:\Users\Gysje P`.
- Active remote is `https://github.com/DanielAdrian975/casemix-bpjs-analisis-2026.git`.
- Karpathy has no project-local `.git` or `.beads`.
- Parent `.beads` reports a repository ID mismatch.

Decision recorded as `D-0009`: commit/push/`bd sync` remain NO-GO until a project-local Git root and safe `bd` state are established. No raw sources were ingested.

## 2026-05-16 | decision | local-repo-initialization | Project-local Git and bd

Performed Local Repo Initialization Repair without commit, push, `bd sync`, remote changes, or file deletion.

- Added project-local `.gitignore` before Git initialization.
- Initialized Git at `C:\Users\Gysje P\Documents\Adi File\Karpathy`.
- Verified Git root is now the Karpathy project root.
- Initialized project-local `bd` with issue prefix `Karpathy`.
- Adjusted `AGENTS.md` so push/`bd sync` are mandatory only after a safe project remote/upstream exists.

Decision recorded as `D-0010`: selective local commit is allowed after manual staging review; broad staging, push, remote changes, and `bd sync` remain blocked. No raw sources were ingested.

## 2026-05-16 | decision | first-local-commit | Selective process-only staging

Ran a Selective Staging Audit before the first local commit.

- Verified project-local Git root.
- Verified `.streamlit` secrets are ignored.
- Inventoried nested project markers and found `Bahan\Karpathy RAG system\llm-wiki\.git`.
- Found build/test markers in `Bahan\Enhance Pengetahuan Ekstraktor\requirements.txt` and `_tmp_autoresearch_template\autoresearch_template_python_mas_c4et_boris\requirements.txt`.
- Decided to stage only process docs, root wiki process pages, `skills/README.md`, `.gitignore`, and safe `.beads` metadata.

Decision recorded as `D-0011`. No raw sources were ingested.

## 2026-05-16 | decision | source-subproject-inventory | Corpus staging decision

Ran Source/Subproject Inventory Decision before the next staging batch.

- No files larger than 10MB were found.
- Nested Git repo found at `Bahan\Karpathy RAG system\llm-wiki\.git`.
- Build/test markers found in `Bahan\Enhance Pengetahuan Ekstraktor\requirements.txt` and `_tmp_autoresearch_template\autoresearch_template_python_mas_c4et_boris\requirements.txt`.
- Credential-like files found under `Bahan\.streamlit\`; these remain ignored and NO-GO.
- `.gitattributes` only configures `bd` merge behavior and is safe for a future selective metadata batch.

Decision recorded as `D-0012`: hold large source corpus pending curated reviews. No raw sources were ingested.

## 2026-05-16 | decision | curated-source-docs | Orientation docs committed

Ran Curated Source Docs Staging Audit for `.gitattributes`, `CLAUDE.md`, and `MASTER_INDEX.md`.

- Byte-level UTF-8 checks passed for all three files.
- Mojibake was not present in file content; earlier mojibake was a terminal decoding display issue.
- Credential-like scan found no secret assignments or private-key material.
- Only the explicit three-file staged set was committed locally in `8d284b6`.
- No large source corpus, credential files, archives, media, local DBs, generated folders, remote changes, push, or `bd sync` were included.

Decision recorded as `D-0013`: commit curated source orientation docs while keeping broad corpus staging NO-GO.

## 2026-05-16 | audit | process-maturity-sprint | Local workflow trials to 75% target

Ran Process Maturity Sprint using local-only artifacts.

- `docs/process/REMOTE_UPSTREAM_SAFETY_AUDIT.md`: project Git root is correct, but remote/upstream are not configured; push and `bd sync` remain NO-GO.
- `docs/process/TEST_COMMAND_DISCOVERY.md`: no root test/build marker exists; implementation work needs authoritative subproject selection.
- `docs/process/MAS_EVIDENCE_PACKET_TRIAL.md`: validated MAS Evidence-First mechanics with atomic local claims, primary local evidence, red-team notes, judge scores, and final statuses.
- `docs/process/AUTORESEARCH_ARTIFACT_TRIAL.md`: validated AutoResearch mechanics with local scope, search targets, evidence table, synthesis, confidence, and unresolved claims.
- `docs/process/C4ET_SOURCE_CORPUS_GATE.md`: C4-ET dry run returned NO-GO for broad source corpus staging.

Decisions recorded as `D-0014` through `D-0017`. No source corpus, credential files, remote changes, push, or `bd sync` were included.

## 2026-05-16 | decision | gate-6-remote-closure | Remote and bd sync enabled

Closed the remote/upstream blocker after the user provided the project remote:

- Remote: `https://github.com/DanielAdrian975/Karpathy-Protokol.git`
- Verified the remote was reachable and empty before first push.
- Added `origin`, renamed local branch from `master` to `main`, and pushed to `origin/main`.
- Migrated project-local `bd` repository ID from `dd2a206c` to `97d26813` after the remote change.
- Ran `bd --no-daemon sync`: 0 local issues, 0 remote issues, no changes to commit, sync complete.
- Broad source corpus staging remains NO-GO; only audited tracked commits were pushed.

Decision recorded as `D-0018`. No raw source corpus was ingested.

## 2026-05-20 | documentation | pmo-prompting-html-wiki | PMO prompting guide and human LLM Wiki HTML

Created human-readable HTML documentation requested by the user:

- `docs/process/PMO_PROMPTING_GUIDE.html`
- `wiki/KARPATHY_LLM_WIKI_HUMAN.html`
- `PROJECT_PMO_PROMPTING_WIKI.html`

The guide converts PMO Microtask Governance into prompting workflows from intake/planning through assignment, execution, closure, and evaluation. The wiki HTML is a Karpathy-style index-first portal over existing legacy/root wiki anchors. Raw source files were not mutated.

## 2026-05-20 | documentation | interactive-prompt-advisor | Context-to-prompt advisor page

Created `docs/process/INTERACTIVE_PROMPT_ADVISOR.html`, a static interactive page where the user enters context, goal, output, constraints, and evidence requirements. The page generates a prompt explanation and a ready-to-use prompt in one code block, with copy/download helpers and PMO protocol routing. Updated `PROJECT_PMO_PROMPTING_WIKI.html`, `wiki/index.md`, and `docs/process/PROGRESS.md`. Raw source files were not mutated.

## 2026-05-21 | documentation | workspace-aware-html-report | Karpathy workspace-aware report

Created `wiki/KARPATHY_WORKSPACE_AWARE_REPORT.html`, a Wikipedia-style HTML report summarizing the Karpathy workspace contents, protocol architecture, operational status, readiness chart, priority roadmap, and guardrails. Source basis: local workspace audit from `AGENTS.md`, `PROJECT_DASHBOARD.md`, `MASTER_INDEX.md`, `docs/process/PROGRESS.md`, `docs/process/SOURCE_SUBPROJECT_INVENTORY.md`, `docs/process/TEST_COMMAND_DISCOVERY.md`, `docs/process/RISK_REGISTER.md`, `hermes-things/README.md`, `hermes-things/pyproject.toml`, and Git/bd status. Updated `wiki/index.md`. Raw source files and credential-like paths were not mutated or read.

## 2026-05-23 | ingest | S-20260523-resembleai-dramabox-model-card | ResembleAI Dramabox model card

- Ingested Hugging Face model card for `ResembleAI/Dramabox` into `wiki/raw/inbox/S-20260523-resembleai-dramabox-model-card.md` with SHA256 provenance.
- Created source page `wiki/sources/S-20260523-resembleai-dramabox-model-card.md` with atomic claims for expressive TTS, voice cloning, model base, parameters, files, VRAM, and watermarking.
- Created entity page `wiki/entities/dramabox.md` and synthesis page `wiki/syntheses/dramabox-adoption-plan.md` to guide use in this workspace.
- Updated `wiki/index.md`.
- Remaining unresolved items: LTX-2 Community License constraints for intended use; Indonesian output quality; local GPU feasibility.

## 2026-05-23 | decision | S-20260523-resembleai-dramabox-project-management | Dramabox project management and Kaizen roadmap

- Created project-management artifacts for executing the Dramabox technical recommendations:
  - `docs/process/DRAMABOX_PROJECT_MANAGEMENT.md`
  - `docs/process/DRAMABOX_EXPERIMENT_LOG.md`
  - `docs/plans/2026-05-23-dramabox-adoption.md`
  - `wiki/syntheses/dramabox-execution-roadmap.md`
  - `wiki/DRAMABOX_OPERATOR_WORKFLOW.html`
- Created bd tracking issues: `Karpathy-c11`, `Karpathy-b9b`, `Karpathy-cwq`, `Karpathy-vv0`, `Karpathy-isg`, and `Karpathy-e5c`.
- Updated `wiki/index.md`.
- Evidence basis: prior ingested Hugging Face model card source `S-20260523-resembleai-dramabox-model-card` and local project-management decision.
- Remaining unresolved items: license constraints, voice-consent policy, Indonesian output quality, hardware/route feasibility, first verified WAV output.

## 2026-05-23 | decision | S-20260523-ltx2-community-license | Dramabox governance checklist

- Ingested the LTX-2 Community License from the Dramabox model repository into `wiki/raw/inbox/S-20260523-ltx2-community-license.md` and normalized it as `wiki/sources/S-20260523-ltx2-community-license.md`.
- Created `docs/process/DRAMABOX_GOVERNANCE_CHECKLIST.md` for license threshold, consent, watermark, machine-generated disclosure, and healthcare/casemix guardrails.
- Updated `wiki/entities/dramabox.md` with a concise governance baseline.
- Updated `docs/process/DRAMABOX_PM_CONTEXT.md` so future sessions can continue from `Karpathy-cwq` without rereading stable files.
- Kaizen result: highest-risk gate closed first; next microtask is no-install capability matrix.
- Remaining unresolved items: commercial/public deployment still requires separate legal/revenue-threshold review; Indonesian quality and local runtime remain unverified.

## 2026-05-23 | decision | S-20260523-user-dramabox-personal-use-scope | Dramabox personal-use scope

- Captured the user's scope clarification as raw source `wiki/raw/inbox/S-20260523-user-dramabox-personal-use-scope.md` and normalized source page `wiki/sources/S-20260523-user-dramabox-personal-use-scope.md`.
- Updated Dramabox governance/context pages to narrow active use to personal development: thesis presentation text-to-audio and FAQ audio for private listening anytime/anywhere.
- Evidence basis: direct user statement in the current session.
- Remaining unresolved items: Indonesian output quality, route feasibility, and whether FAQ content needs extra healthcare/casemix guardrails.
