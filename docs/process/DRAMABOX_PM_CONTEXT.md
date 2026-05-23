# Dramabox PM Context — Token-Efficient Session Anchor

Last updated: 2026-05-23

Purpose: reduce token waste by avoiding full rereads of stable project files. Read this file first for Dramabox PM sessions, then only read targeted files/sections when needed.

## Active PM issue

- `Karpathy-b9b` — Dramabox governance: license, consent, watermark checks — in_progress.

## Backlog

- `Karpathy-cwq` — Phase 1 no-install capability map.
- `Karpathy-vv0` — Phase 2 prompt library and Indonesian tests.
- `Karpathy-isg` — Phase 3 hardware and minimal inference route.
- `Karpathy-e5c` — Phase 4 workspace integration and experiment log.

## Canonical files

- PM plan: `docs/process/DRAMABOX_PROJECT_MANAGEMENT.md`
- Experiment log: `docs/process/DRAMABOX_EXPERIMENT_LOG.md`
- Implementation plan: `docs/plans/2026-05-23-dramabox-adoption.md`
- Roadmap: `wiki/syntheses/dramabox-execution-roadmap.md`
- Operator HTML: `wiki/DRAMABOX_OPERATOR_WORKFLOW.html`
- Model source page: `wiki/sources/S-20260523-resembleai-dramabox-model-card.md`
- Entity page: `wiki/entities/dramabox.md`

## Current stop conditions

- No voice cloning without explicit consent.
- No public/commercial use before license review.
- No local full inference before hardware/VRAM/storage check.
- No Indonesian quality claim before verified WAV + listening notes.
- No broad source corpus staging.

## Token-efficiency rules

1. Do not reread `AGENTS.md`, full `wiki/index.md`, full `wiki/log.md`, or full process docs unless a task explicitly needs them.
2. Use this context file plus `bd show <issue>` as the session anchor.
3. For wiki/log/index updates, use targeted patch/append instead of full rewrite when practical.
4. For external model facts, read only the primary source needed for the active issue.
5. For verification, prefer file existence, `git diff --stat`, and targeted `read_file` snippets.
6. Keep final reports short: complete, files changed, checks, bd/git state, next action.

## Next Kaizen microtask

Execute `Karpathy-b9b`:

1. Fetch/read Dramabox `LICENSE` only.
2. Create `docs/process/DRAMABOX_GOVERNANCE_CHECKLIST.md`.
3. Update `wiki/entities/dramabox.md` only if governance facts change.
4. Append concise wiki log entry.
5. Close or update `Karpathy-b9b` based on license clarity.
