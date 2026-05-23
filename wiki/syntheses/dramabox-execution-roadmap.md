---
title: Dramabox Execution Roadmap
source_id: S-20260523-resembleai-dramabox-project-management
source_path: docs/process/DRAMABOX_PROJECT_MANAGEMENT.md
created: 2026-05-23
updated: 2026-05-23
type: synthesis
confidence: medium
status: active
---

# Dramabox Execution Roadmap

## Summary

This page converts the Dramabox adoption recommendation into a managed execution roadmap. The work is tracked in `bd`, governed by stop conditions, and updated through LLM Wiki Karpathy after each durable learning or verified output.

## Active bd issues

- `Karpathy-c11` — Dramabox adoption project management (closed after PM artifacts verified).
- `Karpathy-b9b` — governance: license, consent, watermark checks.
- `Karpathy-cwq` — Phase 1 no-install capability map.
- `Karpathy-vv0` — Phase 2 prompt library and Indonesian tests.
- `Karpathy-isg` — Phase 3 hardware and minimal inference route.
- `Karpathy-e5c` — Phase 4 workspace integration and experiment log.

## Claims

Claim ID: C-S-20260523-resembleai-dramabox-project-management-001
Claim: Dramabox adoption should begin with governance and no-install capability mapping before local inference.
Evidence: `docs/process/DRAMABOX_PROJECT_MANAGEMENT.md` @ Stop conditions and Execution sequence
Status: supported
Confidence: medium
Notes: This is a project-management decision based on model-card hardware/license constraints, not a model capability claim.

Claim ID: C-S-20260523-resembleai-dramabox-project-management-002
Claim: Indonesian quality and local runtime feasibility remain unresolved until a verified experiment is performed.
Evidence: `docs/process/DRAMABOX_EXPERIMENT_LOG.md` @ Unresolved until first run
Status: supported
Confidence: high
Notes: No output WAV has been generated or listened to yet.

## Current next action

Run `Karpathy-b9b`: license/consent/watermark governance checklist.

## Stop conditions

- Do not use non-consented voice references.
- Do not perform public/commercial use before license review.
- Do not attempt full local inference before hardware/storage check.
- Do not claim output quality without verified audio file and listening notes.

## Links

- [[dramabox]]
- [[dramabox-adoption-plan]]
- `docs/process/DRAMABOX_PROJECT_MANAGEMENT.md`
- `docs/process/DRAMABOX_EXPERIMENT_LOG.md`
