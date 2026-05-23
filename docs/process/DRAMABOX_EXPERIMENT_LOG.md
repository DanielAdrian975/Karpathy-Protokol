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

No generated audio runs have been verified yet.

## Unresolved until first run

- Indonesian pronunciation quality.
- Local runtime feasibility on this Windows host.
- Best cfg/stg ranges for narration vs emotional dialogue.
- Whether Space/hosted/local route gives the most practical repeatability.
