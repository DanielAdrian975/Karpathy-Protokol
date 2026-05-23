# Dramabox Adoption Implementation Plan

> **For Hermes:** Use project-management-closure and llm-wiki-karpathy-workflow to execute this plan task-by-task. Use subagent-driven-development only after the user asks for parallel execution.

**Goal:** Make Dramabox usable as an auditable text-to-audio workflow in the Karpathy workspace.

**Architecture:** Keep the model/source facts in `wiki/`; keep operational PM and logs in `docs/process/`; use `bd` as the task tracker; use Kaizen microtasks to avoid unsafe large installs or unverified claims.

**Tech Stack:** Hugging Face Hub, Dramabox model card/source page, Markdown wiki, bd, Git, optional hosted GPU/Space/local Python later.

---

### Task 1: Close PM setup

**Objective:** Verify the PM artifacts and close `Karpathy-c11` once docs are accepted.

**Files:**
- Read: `docs/process/DRAMABOX_PROJECT_MANAGEMENT.md`
- Read: `wiki/syntheses/dramabox-execution-roadmap.md`

**Steps:**
1. Read both files.
2. Confirm issue IDs are listed.
3. Confirm stop conditions exist.
4. Close `Karpathy-c11` only after verification.

### Task 2: License and consent governance

**Objective:** Prevent unsafe voice cloning or public/commercial use.

**Files:**
- Create: `docs/process/DRAMABOX_GOVERNANCE_CHECKLIST.md`
- Modify: `wiki/entities/dramabox.md`

**Steps:**
1. Fetch/read Hugging Face `LICENSE` for `ResembleAI/Dramabox`.
2. Extract allowed/prohibited use as direct quotes or conservative summary.
3. Add consent rule for voice references.
4. Add watermark disclosure rule.
5. Update `Karpathy-b9b`.

### Task 3: Capability matrix

**Objective:** Convert the model card into an operator-ready capability table.

**Files:**
- Create: `wiki/syntheses/dramabox-capability-matrix.md`

**Steps:**
1. Read source page `S-20260523-resembleai-dramabox-model-card`.
2. Extract parameters, defaults, effect, risk.
3. Compare route options: Space, hosted GPU, local, quantized.
4. Mark unverified local performance claims.
5. Update `Karpathy-cwq`.

### Task 4: Prompt library

**Objective:** Create reusable prompts for the user's target workflows.

**Files:**
- Create: `docs/process/DRAMABOX_PROMPT_LIBRARY.md`

**Steps:**
1. Add narrator templates.
2. Add Obsidian/process guide templates.
3. Add trading explainer templates.
4. Add Indonesian test prompts with unresolved quality label.
5. Add voice-reference test template with consent warning.
6. Update `Karpathy-vv0`.

### Task 5: Hardware/route decision

**Objective:** Decide where inference should run before downloading large models.

**Files:**
- Create: `docs/process/DRAMABOX_ROUTE_DECISION.md`

**Steps:**
1. Check GPU/VRAM/RAM/storage.
2. Compare requirements to model card.
3. Choose Space/hosted/local/quantized route.
4. Record rationale and risks.
5. Update `Karpathy-isg`.

### Task 6: First verified audio run

**Objective:** Produce one verified output WAV and log it.

**Files:**
- Modify: `docs/process/DRAMABOX_EXPERIMENT_LOG.md`

**Steps:**
1. Run selected route.
2. Verify output WAV exists.
3. Record prompt, seed, parameters, model SHA, route, output path.
4. Add listening notes.
5. Update wiki with observed facts only.

### Task 7: Workspace integration

**Objective:** Turn successful run into repeatable workflow.

**Files:**
- Create/modify future scripts or docs only after route is proven.
- Modify: `wiki/syntheses/dramabox-execution-roadmap.md`

**Steps:**
1. Select one integration target: Obsidian note narration or trading explainer.
2. Define input format.
3. Define output folder and naming convention.
4. Add verification checklist.
5. Update `Karpathy-e5c`.
