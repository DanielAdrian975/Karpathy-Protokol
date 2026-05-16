# Wiki Schema

## Mission

Maintain a structured Markdown wiki from immutable raw sources. The wiki is a compiled knowledge layer. Raw sources are the source of truth.

## Directory Contract

```text
wiki/
  raw/
    README.md
    inbox/
    assets/
  sources/
  entities/
  concepts/
  syntheses/
  comparisons/
  index.md
  log.md
  schema.md
```

Directories may be created when first needed.

## Invariants

1. `wiki/raw/` is immutable after ingest.
2. Every factual claim must cite a SourceID and location.
3. `wiki/log.md` is append-only.
4. `wiki/index.md` must list active durable pages.
5. Unsupported claims must be marked `Insufficient Evidence` or `Unresolved`.
6. Do not ingest credential files.

## SourceID Convention

Format:

```text
S-YYYYMMDD-slug
```

Rules:

- Lowercase slug.
- Letters, numbers, and hyphens only.
- Stable enough to recognize without opening the file.

Example:

```text
S-20260516-legacy-karpathy-source-registry
```

## Source Page Contract

Location:

```text
wiki/sources/<SourceID>.md
```

Required sections:

- Source metadata.
- Source location.
- Summary.
- Key claims with location pointers.
- Extracted entities/concepts.
- Open questions.
- Related pages.

## Claim Format

Use atomic claims:

```text
Claim ID: C-<SourceID>-001
Claim: <single factual statement>
Evidence: <SourceID> @ <location>
Status: supported | partially_supported | contradicted | unresolved
Confidence: low | medium | high
Notes: <limits, conflicts, or caveats>
```

## MAS Evidence Packet Contract

For MAS work, capture:

- Atomic claims.
- Evidence standard.
- Primary sources searched.
- Evidence packets.
- Red-team findings.
- Judge result.
- Unresolved claims.
- Citation list.

## AutoResearch Contract

For research tasks, capture:

- Research question.
- Research plan.
- Retrieval strategy.
- Sources retrieved.
- Synthesis.
- Citations.
- Unresolved claims.
- Next retrieval steps.

## Logging Contract

Append entries using:

```text
## YYYY-MM-DD | <mode> | <SourceID-or-artifact> | <title>

- What changed.
- Why it changed.
- Evidence or source basis.
- Remaining unresolved items.
```

Modes:

- `init`
- `ingest`
- `synthesis`
- `query`
- `lint`
- `migration`
- `decision`

## Lint Checklist

- Orphan pages.
- Missing SourceIDs.
- Claims without locations.
- Index entries missing.
- Log entries missing.
- Unresolved claims not tracked.
- Legacy wiki divergence.
