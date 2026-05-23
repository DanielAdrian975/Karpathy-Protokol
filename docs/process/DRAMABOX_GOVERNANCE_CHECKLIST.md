# Dramabox Governance Checklist

Date: 2026-05-23
bd issue: Karpathy-b9b
Source basis: `wiki/sources/S-20260523-ltx2-community-license.md` and raw license `wiki/raw/inbox/S-20260523-ltx2-community-license.md`
Scope: ResembleAI/Dramabox use inside this Karpathy text-to-audio workflow.
Status: ACCEPTED FOR INTERNAL GOVERNED EXPERIMENTS; public/commercial use remains gated.
Current user-declared scope: personal development only — thesis presentation text-to-audio and selected FAQ audio for private listening anytime/anywhere. Source: `wiki/sources/S-20260523-user-dramabox-personal-use-scope.md`.

## Current personal-use scope

GO-TRIAL scope is narrowed to:

- private/personal learning audio
- thesis presentation rehearsal audio
- FAQ audio for repeated private listening
- no public distribution
- no commercial deployment
- no third-party voice cloning unless consent is explicitly recorded

This lowers operational risk but does not remove the checklist: consent, watermark logging, disclosure for any shared/disseminated copy, and output-path verification still apply.

## MAS Evidence Packet

Research / claim question: What governance rules are required before using Dramabox for voice generation, voice cloning, and public/commercial outputs?

Evidence standard: primary source only. Source used: Hugging Face Dramabox `LICENSE`, retrieved as `S-20260523-ltx2-community-license`.

### Atomic claims

1. Claim: Using or distributing LTX-2 binds the user to the Agreement.
   Status: SUPPORTED
   Evidence anchor: `S-20260523-ltx2-community-license` @ LICENSE lines 5-6
   Limits: Not legal advice.

2. Claim: License grants broad limited use/reproduction/distribution/derivative rights, subject to restrictions.
   Status: SUPPORTED
   Evidence anchor: `S-20260523-ltx2-community-license` @ LICENSE lines 79-86
   Limits: Attachment A and commercial threshold must still be followed.

3. Claim: Entities with annual revenues >= USD 10,000,000 need a paid commercial use license.
   Status: SUPPORTED
   Evidence anchor: `S-20260523-ltx2-community-license` @ LICENSE lines 87-96
   Limits: Entity aggregation terms also matter; revenue status must be confirmed by user/org.

4. Claim: The licensor claims no rights in outputs except as stated, but the user is accountable for inputs, outputs, and downstream use.
   Status: SUPPORTED
   Evidence anchor: `S-20260523-ltx2-community-license` @ LICENSE lines 159-163
   Limits: Does not override restricted uses.

5. Claim: Machine-generated content must be expressly and intelligibly disclosed as machine generated when generated/disseminated.
   Status: SUPPORTED
   Evidence anchor: `S-20260523-ltx2-community-license` @ LICENSE lines 310-314
   Limits: Exact disclosure wording can be adapted to context.

6. Claim: Impersonation/deepfakes without consent are prohibited.
   Status: SUPPORTED
   Evidence anchor: `S-20260523-ltx2-community-license` @ LICENSE lines 316-319
   Limits: Consent evidence must be retained outside the model output.

7. Claim: Medical advice and medical-results interpretation are prohibited uses.
   Status: SUPPORTED
   Evidence anchor: `S-20260523-ltx2-community-license` @ LICENSE lines 341-342
   Limits: Healthcare/casemix narration must remain administrative/educational, not medical advice.

## Governance decision

GO-TRIAL for internal, auditable, non-public Dramabox experiments if all checklist items pass.

NO-GO until separate review for:

- public release or commercial deployment
- use by/for an entity that may meet the USD 10M annual revenue threshold
- non-consented voice reference or speaker imitation
- medical advice or interpretation of medical results
- undisclosed machine-generated content

## Required checklist before every generated audio run

| Check | Required answer | Status |
|---|---|---|
| Purpose is internal experiment/research? | Yes | Required |
| Public/commercial deployment? | No, unless separate license review completed | Required |
| Entity revenue threshold reviewed? | Yes/No recorded | Required before commercial use |
| Voice reference used? | None or explicit consent recorded | Required |
| Speaker impersonation risk? | No, unless consented and disclosed | Required |
| Medical advice/result interpretation? | No | Required |
| Machine-generated disclosure included? | Yes for disseminated content | Required |
| Watermark setting logged? | Yes | Required |
| Prompt, params, seed, model SHA logged? | Yes | Required |
| Output file verified on disk? | Yes before success claim | Required |

## Default disclosure text

For generated audio:

```text
Disclosure: This audio was generated with AI text-to-speech using ResembleAI/Dramabox. It is synthetic/machine-generated audio. Voice references, if any, were used only with consent recorded in the experiment log.
```

For Indonesian:

```text
Pengungkapan: Audio ini dibuat dengan AI text-to-speech ResembleAI/Dramabox. Ini adalah audio sintetis/dihasilkan mesin. Referensi suara, bila digunakan, hanya dipakai dengan persetujuan yang dicatat dalam log eksperimen.
```

## Consent rule

A voice reference may be used only when one of these is true:

1. The speaker is the user and the user explicitly authorizes the reference for the run.
2. The speaker is a collaborator and written/verifiable consent is recorded.
3. The reference is licensed for this purpose and the license path is recorded.

If consent is unclear: STOP.

## Watermark rule

- Keep Dramabox watermark enabled by default.
- If disabled for debugging, record `watermark=False`, reason, and do not disseminate the output without separate approval.

## Healthcare/casemix guardrail

Permitted: administrative narration, documentation workflow explanation, non-clinical training notes.

NO-GO: patient-specific medical advice, interpretation of medical results, diagnosis, treatment recommendation, or output that could be heard as clinical instruction.

## Red-team notes

- The license is not permissive in the Apache/MIT sense; it is a restricted community license.
- Voice cloning is high-risk even for internal tests if consent is not explicit.
- Machine-generated disclosure is mandatory for disseminated content.
- Indonesian output quality remains unresolved until a verified audio run is listened to and logged.

## Final synthesis

Karpathy-b9b can be closed for governance setup. Next safe Kaizen task is `Karpathy-cwq`: create the no-install capability matrix using the existing model card and this governance checklist.
