---
title: Dramabox Adoption Plan
source_id: S-20260523-resembleai-dramabox-model-card
source_path: wiki/sources/S-20260523-resembleai-dramabox-model-card.md
created: 2026-05-23
updated: 2026-05-23
type: synthesis
confidence: medium
status: draft
---

# Dramabox Adoption Plan

## Goal

Use `ResembleAI/Dramabox` for controlled text-to-audio workflows while preserving Karpathy wiki evidence, reproducibility, and operational safety.

## Correct repository

The user-provided URL used `ResambleAI/Dramabox`; Hugging Face public search and model card show the canonical model is:

```text
https://huggingface.co/ResembleAI/Dramabox
```

## Phased use plan

### Phase 1 — no-install capability map

- Use Hugging Face model card and demo Space to identify supported controls.
- Capture prompt patterns that work.
- Record every experiment in the wiki with prompt, parameters, voice reference status, output path, and subjective/technical result.

### Phase 2 — prompt library

Build reusable prompt templates for:

- narrator calm / warm / serious
- explainer for Obsidian notes
- dialogue with pauses and breaths
- high-emotion scene
- Indonesian test prompt set, clearly marked as unresolved until heard
- voice-reference cloning test with consented reference only

### Phase 3 — minimal inference test

Preferred first route: demo Space or hosted GPU, because model card indicates ~24 GB VRAM peak. Local install should be attempted only after GPU/RAM check.

Minimum acceptance criteria:

- output WAV exists on disk
- exact prompt and seed recorded
- model source and commit noted
- watermark setting recorded
- license status recorded

### Phase 4 — workflow integration

Potential integrations for this workspace:

- text-to-audio generation from Obsidian notes
- voice memo/narration for process guides
- trading strategy explainer audio
- prompt-engineering experiments stored as query surfaces
- comparison page vs other TTS tools after evidence exists

## Starter prompt template

```text
A calm Indonesian male narrator speaks warmly and clearly, with measured pacing and a professional educational tone, "Hari ini kita akan membahas ringkasan strategi dengan bahasa sederhana." He pauses briefly. "Fokus kita adalah bukti, risiko, dan langkah berikutnya."
```

Note: Indonesian quality is unresolved until tested; source metadata lists English.

## Experiment log schema

For each run, record:

```text
Run ID:
Date:
Model: ResembleAI/Dramabox
Commit/SHA:
Execution route: Space | hosted GPU | local
Prompt:
Voice reference: none | file path | consent status
Parameters: cfg_scale, stg_scale, duration_multiplier, gen_duration, ref_duration, seed, watermark
Output path:
Result notes:
Issues:
Next change:
```

## Stop conditions

- Do not use non-consented voice references.
- Do not claim Indonesian support until audio is generated and reviewed.
- Do not attempt full local inference unless hardware check shows sufficient GPU/VRAM or a quantized path is selected.
- Do not use commercially until license review is completed.

## Links

- [[dramabox]]
- `wiki/sources/S-20260523-resembleai-dramabox-model-card.md`
