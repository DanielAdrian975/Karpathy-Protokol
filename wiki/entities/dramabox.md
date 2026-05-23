---
title: Dramabox
source_id: S-20260523-resembleai-dramabox-model-card
source_path: wiki/sources/S-20260523-resembleai-dramabox-model-card.md
created: 2026-05-23
updated: 2026-05-23
type: entity
confidence: medium
status: active
---

# Dramabox

## Summary

Dramabox is an expressive, prompt-driven TTS and voice-cloning model from Resemble AI. It can generate speech where the prompt controls speaker identity, emotion, delivery, laughs, sighs, breaths, pauses, and transitions. The canonical public model ID is `ResembleAI/Dramabox`, not `ResambleAI/Dramabox`.

## What it can be used for

1. Expressive narration: warm, angry, whispering, comedic, dramatic, presenter-style delivery.
2. Voice cloning: optional 10+ second reference audio conditions target timbre.
3. Dialogue production: spoken text inside double quotes with stage directions outside quotes.
4. Character/audio prototyping: villains, hosts, commentators, fictional characters, multi-style demos.
5. Long-scene experiments: explicit `gen_duration` can target longer scenes, with caution on stability.
6. Repeatable generation: `seed` supports reproducibility.
7. Governance-aware output: watermarking is on by default via Resemble Perth.

## Operational facts

- Pipeline: text-to-speech.
- Library tag: `ltx-audio-tts`.
- Base: `Lightricks/LTX-2.3` fine-tune.
- Key parameters: `prompt`, `voice_ref`, `cfg_scale`, `stg_scale`, `duration_multiplier`, `gen_duration`, `ref_duration`, `seed`, `rescale_scale`, `watermark`.
- Model card files: `dramabox-dit-v1.safetensors` (~6.6 GB), `dramabox-audio-components.safetensors` (~1.9 GB), and auto-downloaded `unsloth/gemma-3-12b-it-bnb-4bit` (~8 GB).
- Model card says peak VRAM is around 24 GB for warm server use.

## Prompt rule

Use this pattern:

```text
<speaker description>, "<dialogue>" <action direction> "<more dialogue>"
```

- Put literal spoken words inside double quotes.
- Put performance direction outside quotes.
- Avoid words like `Sigh`, `Gasp`, `Cough`, `Ahem`, `Pfft` inside quotes unless you want them spoken literally.

## Risks / constraints

- License: LTX-2 Community License; must be reviewed before business/public deployment.
- Language: source metadata lists English; Indonesian output quality requires test evidence.
- Hardware: local full model likely needs high VRAM; this host should start with hosted Space/API or smaller/quantized variants before local install.
- Voice cloning: only use voices with consent; keep reference clips auditable.

## Evidence / Source Anchors

- `S-20260523-resembleai-dramabox-model-card` @ model card frontmatter, Quick Start, Inference Parameters, Prompt Format, Files, Watermarking.

## Links

- [[dramabox-adoption-plan]]
- `wiki/sources/S-20260523-resembleai-dramabox-model-card.md`
