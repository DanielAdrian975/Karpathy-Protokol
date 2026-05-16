# Raw Source Policy

`wiki/raw/` is reserved for immutable source material.

## Rules

- Do not edit, normalize, rename, or delete raw source files after ingestion.
- Do not store credentials, passwords, tokens, or private keys here.
- Assign every ingested source a `SourceID` using the format `S-YYYYMMDD-slug`.
- Create a corresponding source page under `wiki/sources/` before using the source for factual claims.
- Cite SourceID and location for every factual claim in `wiki/`.

## Intake Flow

1. Place new source material in `wiki/raw/inbox/`.
2. Assign SourceID.
3. Create `wiki/sources/<SourceID>.md`.
4. Update related wiki pages.
5. Update `wiki/index.md`.
6. Append an entry to `wiki/log.md`.

## Current State

No raw source files have been ingested into root `wiki/raw/` yet.

Legacy source memory exists in `LLM Wiki Karpathy/00_SOURCE_REGISTRY.md` and should be reconciled before migration.
