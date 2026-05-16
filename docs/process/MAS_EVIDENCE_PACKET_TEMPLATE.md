# MAS Evidence Packet Template

Use this template for factual, research, compliance, benchmark, standards, API, vendor, performance, or causal claims.

## Packet Metadata

- Packet ID:
- Task / question:
- Prepared by:
- Date:
- Review mode: assessor | retriever | red-team | judge | final
- Evidence standard:
- Primary source rule:
- Secondary source use: navigation only | not used

## Claim Register

| ClaimID | Atomic claim | Source type | Primary source requirement | Evidence anchor | MethodTransparency | Data/Artifact | Independence check | Red-team notes | Judge score | Final status |
|---|---|---|---|---|---|---|---|---|---:|---|
| C-001 |  | official doc |  |  |  |  |  |  |  | unresolved |

Final status values:

- supported
- partially_supported
- contradicted
- unresolved
- out_of_scope

Judge score values:

- `0`: no usable support
- `1`: weak or indirect support
- `2`: partial support with caveats
- `3`: direct primary-source support
- `4`: direct primary-source support plus independent corroboration, when independence is required

## Evidence Packet Detail

### ClaimID

`C-___`

### Atomic Claim

Write one factual claim only. Do not combine multiple claims in one row.

### Source Type

Examples:

- official documentation
- regulation / statute / standard
- vendor specification
- source code / commit / release note
- dataset / benchmark artifact
- peer-reviewed paper
- institutional report

### Primary Source Requirement

Define what counts as a valid primary source for this claim.

```text
Valid primary sources:
-

Invalid or secondary-only sources:
-
```

### Evidence Anchor

Provide a precise anchor that allows another reviewer to verify the claim.

```text
SourceID or URL:
Document title:
Section / page / line / table / commit:
Access date:
Relevant quote or paraphrase:
```

### MethodTransparency

Explain how the evidence was obtained and interpreted.

```text
Retrieval method:
Search targets:
Filters / date limits:
Extraction method:
Reasoning from evidence to claim:
Known limitations:
```

### Data/Artifact

Link or identify the supporting data, file, benchmark output, screenshot, spec table, commit, or artifact.

```text
Artifact path or URL:
Artifact type:
Version / timestamp:
Checksum or stable identifier, if available:
```

### Independence Check

Required when corroboration matters.

```text
Is this source independent of the claim maker? yes | no | unclear | not_required
Relationship / dependency:
Corroborating source, if any:
Conflict check:
```

### Red-Team Notes

Audit the claim for overclaiming.

```text
Unsupported leap:
Scope mismatch:
Ambiguous terms:
Conflicting evidence:
Missing primary source:
Revision needed:
```

### Judge Score

```text
Score:
Reason:
Confidence: low | medium | high
```

### Final Status

```text
Status:
Accepted wording:
Unresolved remainder:
Next evidence action:
```

## Final Synthesis

- Supported claims:
- Partially supported claims:
- Contradicted claims:
- Unresolved claims:
- Out-of-scope claims:

## Citation List

Use stable primary-source citations only.

-

## Reviewer Checklist

- [ ] Each ClaimID is unique.
- [ ] Each claim is atomic.
- [ ] Each claim has a source type.
- [ ] Primary source requirement is explicit.
- [ ] Evidence anchor is precise enough to verify.
- [ ] MethodTransparency explains retrieval and interpretation.
- [ ] Data/Artifact is identified where applicable.
- [ ] Independence check is completed or marked not required.
- [ ] Red-team notes are completed.
- [ ] Judge score is assigned.
- [ ] Final status is assigned.
- [ ] Unsupported claims are marked unresolved.
