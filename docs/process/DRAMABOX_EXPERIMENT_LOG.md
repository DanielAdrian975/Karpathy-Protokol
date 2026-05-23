# Dramabox Experiment Log

Purpose: every Dramabox run must be reproducible, auditable, and linked back to the LLM Wiki Karpathy memory layer.

## Logging rule

Do not claim a generation succeeded unless the output file exists on disk and the path is recorded here.

## Run template

```text
Run ID:
Date:
bd issue:
Model: ResembleAI/Dramabox
Model commit/SHA:
Execution route: Hugging Face Space | hosted GPU | local full model | quantized/community variant
Hardware checked: yes/no; summary
Prompt:
Voice reference: none | path | consent status
Parameters:
  cfg_scale:
  stg_scale:
  duration_multiplier:
  gen_duration:
  ref_duration:
  seed:
  rescale_scale:
  watermark:
Output path:
Output file verified: yes/no
Listening notes:
Language result:
Issues/artifacts:
Next change:
Wiki pages updated:
```

## Runs

No Dramabox-generated audio runs have been verified yet.

## Local fallback app smoke runs

Run ID: local-sapi-smoke-20260523-181924
Date: 2026-05-23
bd issue: Karpathy-cwq / app MVP follow-through
Model: Windows SAPI local fallback, not ResembleAI/Dramabox
Model commit/SHA: not applicable
Execution route: local Windows SAPI via `powershell.exe` + `System.Speech`
Hardware checked: yes; `powershell.exe` available and Python 3.10.10 available
Prompt/text: `Halo Gysje. Ini tes audio singkat untuk presentasi tesis.`
Voice reference: none
Parameters: voice=default; rate=0; chunk_count=1; watermark=not applicable to SAPI fallback
Output path: `apps/thesis_faq_audio_app/outputs/20260523-181924-smoke-test/smoke-test-001.wav`
Output file verified: yes; 243416 bytes
Listening notes: not yet human-reviewed
Language result: generated Indonesian test file exists; pronunciation quality unresolved until listened to
Issues/artifacts: local fallback app created at `apps/thesis_faq_audio_app/app.py`
Next change: create thesis/FAQ prompt library and listening rubric before larger batch conversion
Wiki pages updated: `wiki/syntheses/dramabox-capability-map.md`, `wiki/entities/dramabox.md`, `wiki/index.md`, `wiki/log.md`

## Unresolved until first Dramabox run / listening review

- Indonesian pronunciation quality: local fallback WAV exists, but human listening notes are still missing.
- Local full Dramabox runtime feasibility on this Windows host.
- Best cfg/stg ranges for narration vs emotional dialogue.
- Whether Space/hosted/local route gives the most practical repeatability.
