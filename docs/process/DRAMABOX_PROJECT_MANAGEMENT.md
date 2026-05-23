# Dramabox Project Management Plan

Protocol Precheck
- Goal: menjalankan rekomendasi teknis Dramabox secara terukur, auditable, dan terus berkembang dalam LLM Wiki Karpathy.
- Expected output: roadmap, backlog bd, quality gates, experiment log, stop conditions, dan Kaizen cadence.
- Primary mode: Wiki Maintenance.
- Supporting protocols: Project Management, LLM Wiki Karpathy, MAS Evidence-First untuk klaim faktual/model/license, Boris workflow untuk eksekusi docs/process, Kaizen loop.
- Skills loaded: protocol-router-precheck, project-management-closure, llm-wiki-karpathy-workflow, writing-plans, huggingface-hub.
- Files likely touched: docs/process/DRAMABOX_PROJECT_MANAGEMENT.md, docs/process/DRAMABOX_EXPERIMENT_LOG.md, docs/plans/2026-05-23-dramabox-adoption.md, wiki/syntheses/dramabox-execution-roadmap.md, wiki/index.md, wiki/log.md, docs/process/PROGRESS.md, docs/process/DECISION_LOG.md, docs/process/RISK_REGISTER.md.
- Evidence standard: primary source first; Hugging Face model card/source page for model facts; local file outputs for experiment claims; license/consent claims unresolved until reviewed.
- Verification plan: confirm files exist, read back key artifacts, inspect git diff/stat, bd issue state.
- bd issue / tracking: Karpathy-c11 plus follow-up issues Karpathy-cwq, Karpathy-vv0, Karpathy-isg, Karpathy-e5c, Karpathy-b9b.
- Stop conditions checked: no credential reads; no broad corpus staging; no local inference until GPU/VRAM feasibility is checked; no commercial/public use until license reviewed; no voice cloning without consent.
- Proceed / Stop: Proceed for project management artifacts only; stop before inference/install.

## Objective

Build an operational project-management layer so `ResembleAI/Dramabox` can be used for text-to-audio experiments without losing provenance, safety, or repeatability.

## Project outcome

A Dramabox workflow is considered operational when:

1. Capability map exists and cites source anchors.
2. Prompt library exists for target use cases.
3. Hardware/route decision is recorded before inference.
4. At least one minimal WAV generation is produced and logged with prompt, seed, parameters, model SHA, route, watermark setting, and output path.
5. License/consent/watermark governance is explicit.
6. Each experiment updates the LLM Wiki Karpathy memory layer.

## Work breakdown and bd tracking

| Phase | bd issue | Owner | Status | Deliverable | Acceptance criteria |
|---|---|---|---|---|---|
| PM setup | Karpathy-c11 | Hermes/Gysje | closed | This plan + wiki roadmap | Files exist; wiki index/log updated; risks recorded |
| Phase 1 capability map | Karpathy-cwq | Hermes/Gysje | open | Dramabox capability matrix | Parameters, files, VRAM, prompt rules, Space/local options cited from source |
| Phase 2 prompt library | Karpathy-vv0 | Hermes/Gysje | open | Reusable prompt templates | Narrator, Obsidian note, trading explainer, emotional dialogue, Indonesian test prompts created; Indonesian marked unresolved until reviewed |
| Phase 3 inference route | Karpathy-isg | Hermes/Gysje | open | Route decision + first WAV | GPU/VRAM check done; route selected; output WAV exists and is logged |
| Phase 4 integration | Karpathy-e5c | Hermes/Gysje | open | Workspace integration | Repeatable text-to-audio workflow tied to Obsidian/text files and experiment log |
| Governance | Karpathy-b9b | Hermes/Gysje | open | License/consent/watermark checklist | LTX-2 license reviewed; consent rule defined; watermark disclosure rule defined |

## Kaizen operating loop

Run this loop for each Dramabox session:

1. Blindspot scan: what could be false, unsafe, unverified, or stale?
2. Potential scan: what useful output can be produced in <=15 minutes?
3. Select one microtask.
4. Execute with provenance.
5. Verify file/output exists.
6. Update `docs/process/DRAMABOX_EXPERIMENT_LOG.md` if an experiment ran.
7. Update relevant wiki page when knowledge changed.
8. Update bd issue state.
9. Record unresolved claims instead of guessing.

## Execution sequence

### Step 0 — Governance gate first

Do before public/commercial output or voice cloning:

- Read the model LICENSE from Hugging Face.
- Decide allowed internal/private use vs public/commercial use.
- Define consent rule for voice references.
- Decide default watermark policy.

Stop if license or consent is unclear.

### Step 1 — No-install capability map

Tasks:

- Re-read `wiki/sources/S-20260523-resembleai-dramabox-model-card.md`.
- Extract parameter table into a matrix.
- Add route options: Space, hosted GPU, local full model, quantized/community variant.
- Mark all performance claims as environment-specific unless locally verified.

Output:

- Update `wiki/entities/dramabox.md` or create a comparison/query page.

### Step 2 — Prompt library

Create prompt templates for:

- calm Indonesian narrator
- formal Obsidian/process-guide narrator
- trading strategy explainer
- emotional dialogue
- short voice-clone consented test
- failure-mode prompts: too long, unclear stage direction, Indonesian mixed with English

Output:

- `docs/process/DRAMABOX_PROMPT_LIBRARY.md` in a future task.

### Step 3 — Hardware/route decision

Before local inference:

- Check OS/GPU/VRAM/RAM.
- If VRAM < 24 GB, prefer Space/hosted GPU/quantized variant.
- Avoid full local download until storage and hardware are confirmed.

Output:

- Route decision recorded in wiki and experiment log.

### Step 4 — Minimal generation

Acceptance criteria:

- WAV output exists on disk.
- Prompt and parameters are recorded.
- Model ID and commit/SHA recorded.
- Watermark setting recorded.
- Subjective listening notes recorded.
- If Indonesian is tested, result is labeled as observed test result, not general model support.

### Step 5 — Integration

Candidate integrations:

- Convert Obsidian note sections into narration prompts.
- Generate audio summaries for process guides.
- Generate trading explainer audio for research review.
- Maintain a query surface for “prompt → result → improvement”.

## Quality gates

| Gate | Required check | Pass condition |
|---|---|---|
| Evidence | Source cited | Model facts cite Hugging Face/source page |
| File | Output exists | Generated WAV or markdown file exists on disk |
| Reproducibility | Params logged | Prompt, seed, cfg/stg, duration, route, model SHA captured |
| Safety | Consent | Voice reference has explicit consent or is not used |
| License | Usage allowed | License reviewed before commercial/public use |
| Hardware | Route feasible | GPU/VRAM checked before local inference |
| Wiki | Memory updated | index/log and relevant page updated |
| Git/bd | Scoped state | No broad source staging; bd issue updated |

## Stop conditions

- Voice cloning requested without consent.
- Commercial/public use requested before license review.
- Local install requested without hardware/storage check.
- Output path cannot be verified.
- Prompt/result claim cannot be backed by source or actual file.
- bd/Git state indicates unsafe repo boundary.

## Current next microtask

Recommended next 15-minute Kaizen microtask:

`Karpathy-b9b`: review the Hugging Face LICENSE and create a one-page governance checklist before any voice cloning or public output.

Reason: it protects all later work and prevents unsafe reuse of voices or licensed outputs.
