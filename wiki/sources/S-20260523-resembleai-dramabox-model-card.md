---
title: ResembleAI Dramabox Model Card
source_id: S-20260523-resembleai-dramabox-model-card
source_path: wiki/raw/inbox/S-20260523-resembleai-dramabox-model-card.md
created: 2026-05-23
confidence: high
status: active
---

# ResembleAI Dramabox Model Card

## Source metadata

- SourceID: `S-20260523-resembleai-dramabox-model-card`
- URL: https://huggingface.co/ResembleAI/Dramabox/raw/main/README.md
- Raw source: `wiki/raw/inbox/S-20260523-resembleai-dramabox-model-card.md`
- SHA256 body: `9895fc21b4d144b57e50b8f4edfff600797118169a986443eecb35f36009a2c8`
- Retrieved: 2026-05-23

## Summary

Dramabox is Resemble AI's expressive text-to-speech model with optional voice cloning. It is prompt-driven: dialogue inside double quotes is spoken literally, while directions outside quotes control speaker identity, emotion, delivery, laughs, sighs, breaths, pauses, and transitions.

## Key claims with locations

Claim ID: C-S-20260523-resembleai-dramabox-model-card-001
Claim: Dramabox is an expressive TTS model with optional voice cloning.
Evidence: S-20260523-resembleai-dramabox-model-card @ README title and opening description
Status: supported
Confidence: high
Notes: Model card states optional 10-second voice reference clones target timbre.

Claim ID: C-S-20260523-resembleai-dramabox-model-card-002
Claim: Dramabox is an IC-LoRA fine-tune of LTX-2.3 3.3B audio-only model using Diffusion Transformer and flow matching, conditioned on Gemma 3 12B text embeddings.
Evidence: S-20260523-resembleai-dramabox-model-card @ README opening description
Status: supported
Confidence: high
Notes: Hardware requirements make local use non-trivial.

Claim ID: C-S-20260523-resembleai-dramabox-model-card-003
Claim: Recommended warm-server Python use reports about 2.5 seconds per generation on H100 after warmup.
Evidence: S-20260523-resembleai-dramabox-model-card @ Quick start and Files sections
Status: supported
Confidence: medium
Notes: Performance is environment-specific; not verified on this Windows host.

Claim ID: C-S-20260523-resembleai-dramabox-model-card-004
Claim: Peak VRAM is about 24 GB for warm server; model weights include 6.6 GB DiT, 1.9 GB audio components, and about 8 GB Gemma 3 12B 4-bit text encoder download.
Evidence: S-20260523-resembleai-dramabox-model-card @ Files section
Status: supported
Confidence: high
Notes: This implies CPU/low-VRAM deployment needs quantized/community variants or hosted inference.

Claim ID: C-S-20260523-resembleai-dramabox-model-card-005
Claim: Outputs are watermarked by default with Resemble Perth unless disabled.
Evidence: S-20260523-resembleai-dramabox-model-card @ Watermarking section
Status: supported
Confidence: high
Notes: Important for disclosure and downstream audio governance.

## Extracted entities/concepts

- [[dramabox]]
- [[dramabox-adoption-plan]]
- Resemble AI
- LTX-2.3
- Expressive TTS
- Voice cloning
- Watermarking

## Open questions

- License constraints under LTX-2 Community License need direct review before commercial or clinical/official use.
- Indonesian quality is unresolved because model card lists language `en`.
- Local GPU feasibility on this machine is unresolved; model card suggests approximately 24 GB VRAM peak.

## Related pages

- `wiki/entities/dramabox.md`
- `wiki/syntheses/dramabox-adoption-plan.md`
