# AGENTS.md - Project Operating Constitution

## 0. Prime Directive

Do not optimize for speed before correctness.
Always preserve auditability: plan, diff, tests, evidence, progress update.

## 1. Active Frameworks

- LLM Wiki: maintain `wiki/index.md`, `wiki/log.md`, and source provenance.
- MAS Evidence-First: use only primary sources for factual/research/compliance claims.
- AutoResearch: use for research tasks, benchmarks, technical comparison, standards, APIs.
- C4-ET: trigger only for team/capacity/bottleneck/WIP/lead-time/deadlock decisions.
- Boris-style workflow: plan first, parallelize only when explicitly requested, verify before done.
- Skills: use task-specific skills when available.

## 2. Repository Orientation

- Source code: not yet mapped at root; multiple candidate subprojects exist under `Bahan/` and `_tmp_autoresearch_template/`.
- Tests: not yet mapped at root; `_tmp_autoresearch_template/autoresearch_template_python_mas_c4et_boris/tests/` exists as a template test area.
- Docs: root process docs are in `docs/process/`; legacy project docs exist in `Bahan/`, `LLM Wiki Karpathy/`, and top-level `CLAUDE.md` / `MASTER_INDEX.md`.
- Config: no root config baseline confirmed; subproject configs exist under `Bahan/` and templates. Do not read credential files.
- Wiki: normalized root wiki is `wiki/`; legacy compiled wiki is `LLM Wiki Karpathy/`.
- Process logs: `docs/process/PROGRESS.md`, `docs/process/DECISION_LOG.md`, `docs/process/RISK_REGISTER.md`, and `wiki/log.md`.

## 3. Work Modes

### Mode A - Implementation

Use when changing code.
Required output: plan, files touched, tests run, risks, progress update.

### Mode B - Research / AutoResearch

Use when answering factual, causal, benchmark, standards, vendor, or API questions.

Rules:

- Primary sources only for claims.
- Secondary sources only as navigation.
- Unsupported claims must be marked unresolved.

### Mode C - C4-ET Gate

Use only for capacity/team/bottleneck/deadlock questions.

Required:

- Checklist A1-A4
- Metrics B1-B4
- ET1-ET3
- GO / NO-GO / GO-TRIAL

### Mode D - Wiki Maintenance

Use when ingesting docs, decisions, issues, meeting notes, or research.

Required:

- Update wiki page(s)
- Update `wiki/index.md`
- Append `wiki/log.md`
- Flag contradictions/stale claims

### Mode E - Review/Audit

Use when evaluating code, docs, process, architecture, evidence, readiness, or risk.

Required:

- Findings first when defects or risks exist.
- Evidence and file references when possible.
- Open questions or assumptions.
- Residual risk.
- Progress update when process state changes.

## 4. Planning Rule

Before code changes:

1. Restate goal.
2. Identify impacted files.
3. Identify verification commands.
4. Identify risks.
5. Ask only if blocked.

For all substantial non-code work, still provide a short alignment plan with goal, active framework, assumptions, likely files, verification plan, and progress metric.

## 5. Verification Rule

Before marking work done:

- Run relevant tests.
- Run lint/typecheck if available.
- Inspect diff.
- Update progress.
- Update wiki/process logs when knowledge changed.

Use `docs/process/QUALITY_GATES.md` for reusable gate checks and `docs/process/TASK_ROUTING.md` for mode routing.

## 6. Definition of Done

A task is Done only if:

- Acceptance criteria are satisfied.
- Tests/checks pass or failures are documented.
- No unrelated changes are introduced.
- Documentation/wiki updated if behavior or architecture changed.
- Progress score updated in `docs/process/PROGRESS.md`.

## 7. Progress Scoring

Use weighted completion:

- 0.00 = not started
- 0.25 = planned
- 0.50 = implemented/drafted
- 0.75 = verified
- 1.00 = accepted

Overall progress =
sum(task_weight x task_status) / sum(task_weight).

## 8. Stop Conditions

Stop and report if:

- Required test command is unknown.
- Requirements conflict.
- Evidence is missing for factual claims.
- The change needs product/security/legal decision.
- Git or `bd` state makes commit, push, or issue sync unsafe.

## Landing the Plane (Session Completion)

**When ending a work session**, complete the checklist below when the repository has a safe remote and upstream configured. If no safe remote/upstream exists, record that Gate 6 is blocked and do not force `git push`, `bd sync`, or remote changes.

**MANDATORY WORKFLOW:**

1. **File issues for remaining work** - Create issues for anything that needs follow-up
2. **Run quality gates** (if code changed) - Tests, linters, builds
3. **Update issue status** - Close finished work, update in-progress items
4. **PUSH TO REMOTE** - Mandatory only after a safe project remote/upstream exists:
   ```bash
   git pull --rebase
   bd sync
   git push
   git status  # MUST show "up to date with origin"
   ```
5. **Clean up** - Clear stashes, prune remote branches
6. **Verify** - All changes committed AND pushed
7. **Hand off** - Provide context for next session

**CRITICAL RULES:**
- Work is not release-complete until `git push` succeeds on a safe project remote.
- If no safe remote/upstream exists, do not invent one or push to an unrelated remote.
- Never run `bd sync` when repository ownership or sync configuration is unsafe.
- If push fails after a safe remote is configured, resolve and retry until it succeeds or record the blocker.
