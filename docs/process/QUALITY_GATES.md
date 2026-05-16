# Quality Gates

This file defines reusable gates for all task types.

## Gate 0 - Safety

- No credential files read unless explicitly required and approved by the user.
- No raw wiki source mutated.
- No unrelated files intentionally changed.
- No financial advice; trading output is research only.

## Gate 1 - Scope

- Goal restated.
- Mode selected.
- Files likely touched identified.
- Verification plan identified.
- Stop conditions checked.

## Gate 2 - Evidence

Required when factual, research, compliance, benchmark, standard, API, or vendor claims appear:

- Claims are atomic.
- Primary source standard is defined.
- Evidence packets cite source and location.
- Unsupported claims are marked unresolved.
- Red-team or review pass checks overclaiming.

## Gate 3 - Implementation

Required when code/config/executable workflow changes:

- Tests identified before editing.
- Patch is scoped.
- Tests/lint/typecheck run when available.
- Failures documented.
- Diff inspected.

## Gate 4 - Documentation And Wiki

Required when durable knowledge, process, architecture, or behavior changes:

- Process docs updated.
- `wiki/index.md` updated when new durable pages are created.
- `wiki/log.md` appended for durable knowledge/process changes.
- Decision log updated for material decisions.
- Risk register updated for new or changed risks.

## Gate 5 - Progress

- `docs/process/PROGRESS.md` updated.
- Progress percentage and evidence are clear.
- Remaining blockers listed.

## Gate 6 - Release / Handoff

Only pass when repo and issue tracker are safe:

- `bd` status updated or blocker recorded.
- Git status checked.
- Relevant changes staged/committed/pushed when repo ownership is clear.
- Final response includes complete, incomplete, checks, risks, and progress.

Current workspace note: Gate 6 is blocked until a correct project remote/upstream exists and `bd sync` is safe. The project-local Git root and local `bd` database are initialized, but push and `bd sync` remain NO-GO.
