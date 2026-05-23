---
title: Dramabox No-Install Capability Map
source_id: S-20260523-resembleai-dramabox-model-card; S-20260523-ltx2-community-license; S-20260523-user-dramabox-personal-use-scope
source_path: wiki/sources/S-20260523-resembleai-dramabox-model-card.md
created: 2026-05-23
confidence: medium
status: active
---

# Dramabox No-Install Capability Map

## Scope

Active user scope is private personal-development audio: thesis presentation narration and selected FAQ audio for repeated private listening. Public/commercial distribution is out of scope unless a new governance review is opened.

This page completes `Karpathy-cwq` without installing Dramabox or downloading model weights.

## Capability matrix

| Capability | Source-backed facts | Fit for thesis/FAQ private audio | Current status |
|---|---|---|---|
| Expressive TTS | Prompt-driven TTS; prompt controls speaker identity, emotion, delivery, laughs, sighs, breaths, pauses, transitions. | High potential for thesis rehearsal sections if Indonesian quality is acceptable. | Source-supported, not locally verified. |
| Optional voice reference | Optional 10+ second `voice_ref` clones target timbre. | Not needed for MVP; safer to avoid until explicit consent and route are logged. | GO only with consent. |
| Prompt format | Spoken text must be inside double quotes; stage directions outside quotes. | Useful for section-based narration: speaker style outside, thesis/FAQ text inside. | Source-supported. |
| Reproducibility | `seed` default 42 supports repeatable generation. | Useful for comparing prompt versions. | Source-supported. |
| Duration control | `duration_multiplier` and `gen_duration` control length. | Useful for long thesis sections, but long scenes may need chunking. | Source-supported; local behavior unverified. |
| Watermark | Watermark default is on; `--no-watermark` can disable. | Keep ON for governed outputs; log setting. | Required default. |
| Language | Model card metadata lists `en`. | Indonesian thesis/FAQ quality is unresolved. | Must test before quality claim. |
| Hardware | Model card says ~24 GB peak VRAM warm server; weights include 6.6 GB + 1.9 GB + ~8 GB text encoder. | Local full model is risky on this host until hardware/storage check. | HOLD for local full inference. |
| Demo/hosted route | Model card links a Hugging Face ZeroGPU Space. | Best first Dramabox-specific path if available; avoids local install. | GO-TRIAL after availability check. |

## Parameter matrix

| Parameter | Default | Use in thesis/FAQ workflow | Risk / note |
|---|---:|---|---|
| `prompt` | required | Put narration text in double quotes; put style outside quotes. | Bad quote discipline can make stage directions spoken literally. |
| `voice_ref` / `--voice-sample` | `None` | Leave empty for MVP. | Consent required if used. |
| `cfg_scale` | 2.5 | Start default; adjust only after listening tests. | Higher may be more text-faithful but more dramatic. |
| `stg_scale` | 1.5 | Start default for expressive emphasis. | Environment/model behavior unverified locally. |
| `duration_multiplier` | 1.1 | Keep default for breathing room. | Long thesis paragraphs should be chunked anyway. |
| `gen_duration` | 0 auto | Leave auto for short sections; test explicit duration only later. | 20-60 s long scenes mentioned for music/long scenes, not verified for thesis. |
| `ref_duration` | 10.0 | Not used unless voice reference is explicitly consented. | 3-30 s range; longer captures richer timbre but slower encode. |
| `seed` | 42 | Record in experiment log for repeatability. | Same seed may still vary if route/model revision changes. |
| `rescale_scale` | auto | Leave default. | Advanced; avoid changing in early tests. |
| `watermark` | True | Keep true. | If disabled for debugging, do not disseminate and record reason. |

## Route decision matrix

| Route | Pros | Cons | Decision for this project |
|---|---|---|---|
| Local Windows SAPI fallback app | Available now, no model download, can produce private WAV files for thesis/FAQ immediately. | Not Dramabox quality/expressiveness; no Resemble watermark. | GO for MVP text-to-audio application. |
| Hugging Face Space | No local install; likely best Dramabox trial path. | Availability/queue/network may vary; output handling must be logged. | GO-TRIAL next for Dramabox-specific audio. |
| Hosted GPU | Feasible for 24GB+ VRAM route and reproducibility. | Cost/setup; credentials and storage governance needed. | HOLD until Space or MVP workflow proves need. |
| Local full Dramabox | Full control; offline after setup. | Requires ~24GB VRAM and large downloads; Windows host feasibility unverified. | HOLD until hardware/storage check. |
| Quantized/community variant | May reduce hardware needs. | Not yet identified/verified; governance/source risk. | RESEARCH LATER. |

## Recommended prompt pattern for thesis/FAQ

```text
A calm Indonesian academic narrator speaks clearly and steadily for private study, "<paste one thesis section or FAQ answer here>"
```

Rules:

1. Use one concept/paragraph per generation chunk.
2. Keep stage directions outside the quotes.
3. Avoid cloning a third-party voice.
4. Log route, seed, params, output path, and listening notes.
5. Mark Indonesian quality as observed-per-output, not generally proven.

## Kaizen findings

Blind spot:
- The project originally focused on Dramabox, but the user need is broader: reliable private thesis/FAQ audio. Waiting for 24GB VRAM or Dramabox setup would delay value.

Hidden potential:
- A no-install Windows TTS application can immediately convert thesis/FAQ text to WAV while Dramabox remains the higher-quality future route.

## Acceptance criteria for Karpathy-cwq

- Capability matrix exists: done.
- Parameter matrix exists: done.
- Route options compared: done.
- Performance claims marked source-based/not locally verified: done.
- Scope narrowed to private thesis/FAQ audio: done.

## Links

- `wiki/entities/dramabox.md`
- `docs/process/DRAMABOX_GOVERNANCE_CHECKLIST.md`
- `docs/process/DRAMABOX_PM_CONTEXT.md`
- `apps/thesis_faq_audio_app/README.md`
