---
title: LTX-2 Community License Agreement
source_id: S-20260523-ltx2-community-license
source_path: wiki/raw/inbox/S-20260523-ltx2-community-license.md
created: 2026-05-23
confidence: high
status: active
---

# LTX-2 Community License Agreement

## Source metadata

- SourceID: `S-20260523-ltx2-community-license`
- Source URL: https://huggingface.co/ResembleAI/Dramabox/raw/main/LICENSE
- Raw source: `wiki/raw/inbox/S-20260523-ltx2-community-license.md`
- SHA256 body: `7c8ef302fa1444a3a5650c2dfa09c6927a52b233202431023abb32519f354397`
- Retrieved: 2026-05-23

## Summary

The Dramabox model card links to the LTX-2 Community License Agreement. This source page extracts only operational governance anchors needed for Dramabox project management. This is not legal advice.

## Key claims with source anchors

Claim ID: C-S-20260523-ltx2-community-license-001
Claim: Use or distribution of any portion/element of LTX-2 binds the user to the Agreement.
Evidence: S-20260523-ltx2-community-license @ LICENSE lines 5-6
Status: supported
Confidence: high
Notes: Applies before use/distribution.

Claim ID: C-S-20260523-ltx2-community-license-002
Claim: The license grants a limited non-exclusive, worldwide, non-transferable, royalty-free license to use/reproduce/distribute/display/perform/sublicense/copy/create derivatives/modify, subject to restrictions.
Evidence: S-20260523-ltx2-community-license @ LICENSE lines 79-86
Status: supported
Confidence: high
Notes: Restrictions include Attachment A and commercial-entity threshold.

Claim ID: C-S-20260523-ltx2-community-license-003
Claim: Entities with annual revenues of at least USD 10,000,000 need a paid commercial use license for LTX-2 and derivatives.
Evidence: S-20260523-ltx2-community-license @ LICENSE lines 87-96
Status: supported
Confidence: high
Notes: Revenue threshold is entity-wide including affiliates/common control per lines 41-48.

Claim ID: C-S-20260523-ltx2-community-license-004
Claim: Licensor claims no rights in generated Output except as stated, but the user is accountable for input, output, and downstream uses, and output use must not violate the Agreement.
Evidence: S-20260523-ltx2-community-license @ LICENSE lines 159-163
Status: supported
Confidence: high
Notes: This supports output logging and responsibility controls.

Claim ID: C-S-20260523-ltx2-community-license-005
Claim: Generated/disseminated machine-generated content must be expressly and intelligibly disclosed as machine generated.
Evidence: S-20260523-ltx2-community-license @ LICENSE lines 310-314
Status: supported
Confidence: high
Notes: Applies to content disclosure; pair with watermark/log policy.

Claim ID: C-S-20260523-ltx2-community-license-006
Claim: Impersonation/deepfakes without consent are prohibited.
Evidence: S-20260523-ltx2-community-license @ LICENSE lines 316-319
Status: supported
Confidence: high
Notes: This directly supports the voice-reference consent stop condition.

Claim ID: C-S-20260523-ltx2-community-license-007
Claim: Medical advice and medical-results interpretation are prohibited uses.
Evidence: S-20260523-ltx2-community-license @ LICENSE lines 341-342
Status: supported
Confidence: high
Notes: Important because user works in healthcare/casemix contexts; generated audio must not be used as medical advice.

## Operational governance implications

- Internal experiment use can proceed only inside the listed restrictions.
- Public/commercial use requires explicit revenue-threshold review and may require separate commercial license.
- Voice cloning requires explicit consent and logging.
- Generated audio/content must disclose machine-generated status.
- Medical advice/medical-result interpretation use is NO-GO.

## Links

- [[dramabox]]
- `docs/process/DRAMABOX_GOVERNANCE_CHECKLIST.md`
