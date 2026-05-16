# Project Operating System

Purpose: make this workspace usable for all task types while preserving correctness, auditability, evidence, and progress tracking.

## Universal Task Loop

Every non-trivial task follows this loop:

1. Intake
2. Mode selection
3. Scope and risk plan
4. Execute within write scope
5. Verify
6. Review/audit
7. Update progress and logs
8. Handoff

## Intake

Capture:

- User goal.
- Expected output.
- Deadline or urgency, if stated.
- Whether code, docs, research, wiki, review, release, or capacity work is involved.
- Known constraints, credentials, privacy concerns, or external dependencies.

If the task has factual, causal, benchmark, standards, API, vendor, or compliance claims, route through Research / AutoResearch and MAS Evidence-First.

## Mode Selection

Use exactly one primary mode and optional supporting modes.

| Primary Mode | Use When | Supporting Modes |
|---|---|---|
| Implementation | Code, scripts, config, executable workflow, tests | Review/Audit, Wiki Maintenance |
| Research / AutoResearch | Factual, causal, benchmark, technical comparison, standards, APIs, vendor claims | Wiki Maintenance |
| C4-ET Gate | Capacity, staffing, bottleneck, WIP, lead-time, blocked-work, deadlock | Review/Audit |
| Wiki Maintenance | Ingesting docs, decisions, issue notes, meeting notes, durable research | Research / AutoResearch |
| Review/Audit | Reviewing changes, architecture, docs, process, risk, evidence, or readiness | Wiki Maintenance |
| Release / Handoff | Session close, commit, push, PR, publish, operational handoff | Review/Audit |

## Planning Contract

Before making code changes, output:

- Goal.
- Active framework.
- Assumptions.
- Files likely touched.
- Verification plan.
- Progress metric expected to change.

For docs-only changes, this planning contract still applies, but verification may be file/link/content checks instead of tests.

## Execution Rules

- Do not broaden scope without recording the reason.
- Do not read credential files.
- Do not edit raw sources.
- Prefer existing structure and local conventions.
- Keep changes inspectable and reversible.
- Record material decisions in `docs/process/DECISION_LOG.md`.
- Record durable knowledge changes in `wiki/log.md`.

## Verification Contract

Minimum verification by task type:

| Task Type | Required Verification |
|---|---|
| Code | Tests, lint/typecheck when available, focused diff review |
| Config | Validation command or dry-run when available, diff review |
| Docs/process | File existence, required headings, cross-link/search check |
| Research | Primary-source evidence packets, unresolved claims, citation audit |
| Wiki | `wiki/index.md` updated, `wiki/log.md` appended, SourceID/provenance checked |
| Review/audit | Findings first, file/line references when possible, residual risks |
| Release | Quality gates, issue status, git status, commit/push when repo is safe |

If the required command is unknown, stop and report the gap unless the task is purely documentation and can be verified structurally.

## Progress Contract

Use weighted completion:

```text
overall = sum(task_weight x task_status) / sum(task_weight)
```

Task status:

- `0.00`: not started
- `0.25`: planned
- `0.50`: drafted or implemented
- `0.75`: verified
- `1.00`: accepted

Update `docs/process/PROGRESS.md` after each completed session or material milestone.

## Handoff Contract

Final response must include:

- What is complete.
- What remains incomplete.
- Tests/checks run.
- Residual risks.
- New progress percentage.

Do not claim completion if:

- Tests are required but unknown or not run.
- Evidence is missing for factual claims.
- Requirements conflict.
- The change needs product, security, legal, or repo ownership decision.
