# Project Plans

Status: Gate 6 remote/upstream closure completed
Progress baseline: 82.25%
Last updated: 2026-05-16

## Repo Summary

This workspace is a knowledge and trading research workspace, not a single clean application repository. Root artifacts include `CLAUDE.md`, `MASTER_INDEX.md`, `Bahan/`, `LLM Wiki Karpathy/`, `_tmp_autoresearch_template/`, `_tmp_skills_modular_build/`, and skill archives.

Observed components:

- `LLM Wiki Karpathy/`: existing compiled wiki with source registry, index, unresolved questions, and query surfaces.
- `Bahan/`: source/reference materials, knowledge extractor projects, LLM wiki variants, MAS/C4-ET materials, and trading research assets.
- `_tmp_autoresearch_template/`: Python AutoResearch template with tests, benchmarks, prompts, MAS, and C4-ET references.
- `_tmp_skills_modular_build/`: generated skill bundle with MAS, C4-ET, workflow, wiki, and reporting skills.
- `Claude Up Skills/`: Claude-oriented skill material and workspace/global guidance.

No root `package.json`, `pyproject.toml`, `Makefile`, or unified test command was found at the workspace root during baseline inspection.

## Operational Workflow

### 1. Intake

- Read `AGENTS.md`, `MASTER_INDEX.md`, and relevant process files.
- Use `docs/process/TASK_ROUTING.md` to choose a primary mode.
- Identify whether the task is docs, research, trading analysis, code, release, or capacity planning.
- Route factual/research/compliance/performance claims through MAS Evidence-First.
- Route research tasks through AutoResearch.
- Route capacity/team/bottleneck questions through C4-ET only when trigger conditions match.

### 2. Planning

- Inspect the smallest relevant file set.
- Define write scope.
- Identify quality gates before editing.
- Create or update a `bd` issue when `bd` is usable.
- Record material decisions in `docs/process/DECISION_LOG.md`.

### 3. Implementation

- Keep edits scoped to the requested surface.
- Do not change raw sources.
- Do not read credential files.
- Prefer existing project structure and skill references.
- Do not write code when the user asks only for process initialization or planning.

### 4. Verification

- Use `docs/process/QUALITY_GATES.md` as the gate checklist.
- For code changes: run the nearest test/lint/build command.
- For docs/process-only changes: verify file existence, links, and required sections.
- For research claims: verify evidence packets, citations, red-team findings, and judge status.
- For wiki changes: verify `wiki/index.md` and `wiki/log.md` are updated.

### 5. Review

- Review diff and ensure no unrelated files or credentials were touched.
- Identify residual risks and unresolved claims.
- Update `docs/process/RISK_REGISTER.md` when needed.

### 6. Wiki Update

- New durable knowledge goes into `wiki/`.
- Legacy wiki material in `LLM Wiki Karpathy/` can be cited as existing project memory.
- Append all durable ingest, synthesis, lint, or structural wiki changes to `wiki/log.md`.

### 7. Progress Scoring

- Update `docs/process/PROGRESS.md` with percent, evidence, completed items, and next actions.
- Progress changes after verified process milestones, validated workflow trials, completed evidence artifacts, or safe issue/release closure.

### 8. Release / Handoff

- Use `docs/process/OPERATING_SYSTEM.md` for final handoff requirements.
- Do not push until Git root, remote ownership, and `bd` repository state are safe.

## Definition Of Done

Project work is done when all applicable items pass:

- Requirement is implemented or explicitly marked out of scope.
- Follow-up work is filed in `bd` or documented when `bd` is unavailable.
- Quality gates run, pass, and are recorded, or their absence is explained.
- MAS claims have atomic claim status and evidence packets.
- AutoResearch work includes plan, retrieval, synthesis, citations, and unresolved claims.
- C4-ET is used only for capacity/team/bottleneck cases and produces a gate decision.
- Wiki raw sources remain immutable.
- `wiki/index.md` and `wiki/log.md` are updated for durable knowledge.
- Progress, decisions, and risks are updated.
- Git status is checked.
- Commit and push complete when a valid repo and remote are available.

## Framework Compliance Matrix

| Framework | Trigger | Required Artifacts | Current Baseline | Gap |
|---|---|---|---|---|
| AGENTS.md constitution | Every session | `AGENTS.md` | Initialized | Needs adoption in future sessions |
| LLM Wiki Karpathy | Durable memory, ingest, synthesis | `wiki/index.md`, `wiki/log.md`, `wiki/schema.md`, `wiki/raw/README.md` | Initialized at root; legacy wiki exists | Legacy and root wiki need reconciliation |
| MAS Evidence-First | Factual, research, performance, compliance claims | Atomic claims, evidence packets, red-team, judge | Template initialized | Needs validation on a real factual claim |
| AutoResearch | Research tasks and optimization loops | Research plan, retrieval log, synthesis, citations, unresolved claims | Template initialized | Needs validation on a real research task |
| C4-ET | Capacity, team, WIP, lead-time, blocked-work, deadlock | Data audit, metrics, gate decision, one-pager | Trigger limited by constitution | No active capacity metrics baseline |
| Skills | Repeated workflows | `skills/README.md` or installed `.codex/skills` | Map initialized | Root skills are mapped, not installed |
| Universal process OS | All task types | `docs/process/OPERATING_SYSTEM.md`, `TASK_ROUTING.md`, `QUALITY_GATES.md` | GO-TRIAL review task validated | Needs implementation and research trials |

## Known Gaps

- Workspace now has a project-local Git root at `C:\Users\Gysje P\Documents\Adi File\Karpathy`.
- Project-local Git uses `origin` at `https://github.com/DanielAdrian975/Karpathy-Protokol.git`.
- Project-local branch `main` tracks `origin/main`.
- Project-local `bd` is initialized with issue prefix `Karpathy`; `bd --no-daemon sync` completed with 0 issues and no changes to commit.
- First local commit completed via selective staging only; broad staging remains prohibited.
- Source/subproject inventory decision completed; corpus staging remains mostly NO-GO pending curated reviews.
- Curated source orientation docs were committed locally in `8d284b6`; no large source corpus was staged.
- Remote/upstream safety audit completed; first push to `origin/main` and `bd --no-daemon sync` succeeded.
- Test command discovery completed; no root test, lint, or build command is defined.
- MAS Evidence-First, AutoResearch, and C4-ET were validated on local process trials.
- Multiple subprojects exist with independent commands; no unified quality gate has been selected.
- Existing wiki lives under `LLM Wiki Karpathy/`; new process expects root `wiki/`.
- Some existing Markdown files show encoding/mojibake in terminal output and may need normalization.
- Credential-like files exist under `Bahan/.streamlit/`; they were not read and should remain protected.

## Blocking Questions

- Should nested Git-enabled source folders be kept as nested repos, converted to submodules, ignored, or flattened?
- Which subproject is the authoritative implementation target for future code work?
- What is the canonical test command for root-level verification?

## Next 5 Tasks

1. Run sensitivity/provenance review for `LLM Wiki Karpathy/` and `Claude Up Skills/` before any source-doc staging.
2. Select the authoritative implementation subproject and define its canonical test command.
3. Run a real implementation GO-TRIAL on the selected subproject.
4. Convert validated process trials into reusable checklist snippets or skills if repetition increases.
5. Decide treatment for nested Git-enabled source folders: submodule, separate repo, ignore, or curated flattening.
