# Wiki Index

Last updated: 2026-05-23
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
| `docs/process/SOURCE_SUBPROJECT_INVENTORY.md` | Decision table for source corpus, nested project, archive/data, credential-like, and `.gitattributes` treatment. |
| `docs/process/REMOTE_UPSTREAM_SAFETY_AUDIT.md` | Local Git/remote/upstream and `bd` safety audit; push remains NO-GO. |
| `docs/process/TEST_COMMAND_DISCOVERY.md` | Root and subproject test/build marker discovery; root command remains unresolved. |
| `docs/process/MAS_EVIDENCE_PACKET_TRIAL.md` | Local MAS Evidence-First workflow validation using primary local evidence. |
| `docs/process/AUTORESEARCH_ARTIFACT_TRIAL.md` | Local AutoResearch workflow validation with bounded scope, evidence table, synthesis, and unresolved claims. |
| `docs/process/C4ET_SOURCE_CORPUS_GATE.md` | C4-ET dry-run decision blocking broad source corpus staging. |
| `docs/process/INTERACTIVE_PROMPT_ADVISOR.html` | Interactive single-page prompt advisor: user enters context and receives explanation plus ready-to-use prompt in one code block. |
| `docs/process/PMO_PROMPTING_GUIDE.html` | Human-readable PMO prompting guide from intake/planning through execution, closure, and evaluation. |
| `wiki/KARPATHY_LLM_WIKI_HUMAN.html` | Human-readable Karpathy-style LLM Wiki portal with entity/topic/query surfaces and wiki roadmap. |
| `wiki/KARPATHY_WORKSPACE_AWARE_REPORT.html` | Wikipedia-style workspace-aware report with protocol architecture diagram, readiness chart, priority roadmap, evidence anchors, guardrails, and next development options. |
| `PROJECT_PMO_PROMPTING_WIKI.html` | Root HTML portal linking PMO prompting guide and LLM Wiki Karpathy HTML. |
| `CLAUDE.md` | Root legacy orientation rules for trading research workspace behavior. |
| `MASTER_INDEX.md` | Root legacy orientation index for trading research workspace context and routing. |
| `wiki/sources/S-20260523-resembleai-dramabox-model-card.md` | Source page for ResembleAI Dramabox model card: expressive TTS, voice cloning, parameters, files, VRAM, watermarking, open questions. |
| `wiki/entities/dramabox.md` | Entity page for Dramabox TTS/voice-cloning model, capabilities, prompt rule, constraints, and operational facts. |
| `wiki/syntheses/dramabox-adoption-plan.md` | Adoption plan for using Dramabox in this workspace with experiment logging, prompt templates, stop conditions, and integration targets. |
| `docs/process/DRAMABOX_PROJECT_MANAGEMENT.md` | Project-management layer for executing Dramabox recommendations with bd tracking, Kaizen cadence, gates, and stop conditions. |
| `docs/process/DRAMABOX_EXPERIMENT_LOG.md` | Reproducible log template for every Dramabox generation run; no audio runs verified yet. |
| `docs/plans/2026-05-23-dramabox-adoption.md` | Bite-sized implementation plan for governance, capability map, prompt library, route decision, first WAV, and integration. |
| `wiki/syntheses/dramabox-execution-roadmap.md` | Managed execution roadmap for Dramabox adoption linked to bd issues and stop conditions. |
| `wiki/DRAMABOX_OPERATOR_WORKFLOW.html` | Human-readable operator workflow portal for Dramabox readiness, execution order, bd issues, and stop conditions. |

## Legacy Memory To Reconcile

The existing legacy wiki describes a Forex Trading Strategy Development System with video processing, strategy generation, backtesting, live trading, MT5 integration, and knowledge management. It includes a source registry and unresolved questions. Future migration should preserve SourceIDs, source locations, confidence notes, and unresolved items.

## Open Wiki Tasks

- Create `wiki/sources/` and migrate legacy source registry into normalized source pages.
- Create `wiki/entities/`, `wiki/concepts/`, `wiki/syntheses/`, and `wiki/comparisons/` when first needed.
- Run sensitivity/provenance review before staging legacy wiki or large source corpus folders.
- Select the authoritative implementation subproject and canonical test command.
- Configure a safe remote/upstream before push or `bd sync`.

| `wiki/sources/S-20260523-ltx2-community-license.md` | Source page for LTX-2 Community License anchors governing Dramabox use, distribution, output accountability, disclosure, consent, and prohibited uses. |
| `docs/process/DRAMABOX_GOVERNANCE_CHECKLIST.md` | Governance checklist for Dramabox experiments: license threshold, consent, watermark, disclosure, healthcare/casemix guardrails, and GO/NO-GO rules. |
| `docs/process/DRAMABOX_PM_CONTEXT.md` | Token-efficient session anchor for Dramabox PM to avoid rereading stable process/wiki files. |
