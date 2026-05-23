# Dramabox PM Context — Token-Efficient Session Anchor

Last updated: 2026-05-23

Purpose: reduce token waste by avoiding full rereads of stable project files. Read this file first for Dramabox PM sessions, then only read targeted files/sections when needed.

## Active PM issue

- `Karpathy-vv0` — Phase 2 prompt library and Indonesian tests.
- `Karpathy-cwq` — closed; no-install capability map exists.
- `Karpathy-b9b` — closed; governance baseline exists.

## Current user-declared scope

- Personal development/private learning only.
- Convert thesis presentation text to audio.
- Convert selected FAQ content to audio.
- Listen privately anytime/anywhere.
- No public/commercial distribution in current scope.
- Source: `wiki/sources/S-20260523-user-dramabox-personal-use-scope.md`.

## Backlog

- `Karpathy-cwq` — Phase 1 no-install capability map. CLOSED.
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
- Capability map: `wiki/syntheses/dramabox-capability-map.md`
- Text-to-audio MVP app: `apps/thesis_faq_audio_app/app.py`
- Text-to-audio MVP README: `apps/thesis_faq_audio_app/README.md`
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

Execute `Karpathy-vv0`:

1. Create prompt templates for private thesis narration and FAQ listening.
2. Include Windows SAPI fallback wording and future Dramabox prompt format.
3. Add a listening rubric: pronunciation, pacing, section clarity, fatigue, and re-listen value.
4. Keep Indonesian quality marked per-output until verified by listening notes.
