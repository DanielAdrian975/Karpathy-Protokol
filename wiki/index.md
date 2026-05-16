# Wiki Index

Last updated: 2026-05-16
Status: root wiki scaffold initialized

## Purpose

This root wiki is the normalized project memory for future Codex work. It complements the existing legacy memory under `LLM Wiki Karpathy/`.

## Required Entry Points

| Path | Purpose | Status |
|---|---|---|
| `wiki/index.md` | Catalog of active root wiki pages | Initialized |
| `wiki/log.md` | Append-only audit trail | Initialized |
| `wiki/schema.md` | Wiki structure and invariants | Initialized |
| `wiki/raw/README.md` | Raw source immutability policy | Initialized |
| `LLM Wiki Karpathy/INDEX.md` | Legacy compiled wiki | Existing legacy memory |
| `LLM Wiki Karpathy/00_SOURCE_REGISTRY.md` | Legacy source registry | Existing legacy memory |
| `LLM Wiki Karpathy/UNRESOLVED.md` | Legacy unresolved questions | Existing legacy memory |

## Active Root Pages

| Page | Summary |
|---|---|
| `wiki/schema.md` | Structure, SourceID rules, artifact contract, and logging rules for root wiki. |
| `wiki/raw/README.md` | Raw source policy and intake flow. |
| `docs/process/OPERATING_SYSTEM.md` | Universal task loop, planning, verification, progress, and handoff contract. |
| `docs/process/TASK_ROUTING.md` | Intake routing matrix for implementation, research, C4-ET, wiki, review, and release work. |
| `docs/process/QUALITY_GATES.md` | Reusable quality gates for safety, scope, evidence, implementation, docs/wiki, progress, and release. |
| `docs/process/MAS_EVIDENCE_PACKET_TEMPLATE.md` | Template for atomic factual claims, primary-source evidence anchors, red-team review, judge scoring, and final status. |
| `docs/process/AUTORESEARCH_ARTIFACT_TEMPLATE.md` | Template for research question, scope, retrieval criteria, primary evidence table, synthesis, confidence, and next actions. |

## Legacy Memory To Reconcile

The existing legacy wiki describes a Forex Trading Strategy Development System with video processing, strategy generation, backtesting, live trading, MT5 integration, and knowledge management. It includes a source registry and unresolved questions. Future migration should preserve SourceIDs, source locations, confidence notes, and unresolved items.

## Open Wiki Tasks

- Create `wiki/sources/` and migrate legacy source registry into normalized source pages.
- Create `wiki/entities/`, `wiki/concepts/`, `wiki/syntheses/`, and `wiki/comparisons/` when first needed.
- Validate MAS evidence packet template on a real factual claim task.
- Validate AutoResearch artifact template on a real research task.
