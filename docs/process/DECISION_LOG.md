# Decision Log

This log records durable process decisions. Append new entries; do not rewrite history except to fix clear typos.

## 2026-05-16 | D-0001 | Root process scaffold

Decision: Create root-level process artifacts for Codex orchestration without changing code.

Rationale: The workspace contains multiple subprojects, a legacy LLM wiki, AutoResearch templates, and a modular skills bundle. A root process layer is needed so future sessions route work consistently.

Status: Accepted

## 2026-05-16 | D-0002 | Root `wiki/` as normalized memory layer

Decision: Use root `wiki/` for normalized future memory while treating `LLM Wiki Karpathy/` as legacy project memory.

Rationale: The user explicitly requested `wiki/raw/README.md`, `wiki/index.md`, `wiki/log.md`, and `wiki/schema.md`. Existing `LLM Wiki Karpathy/` already contains useful material but does not match the requested root paths.

Status: Accepted

## 2026-05-16 | D-0003 | Do not force `bd` migration

Decision: Do not run `bd migrate --update-repo-id`, remove `.beads`, or ignore repository mismatch automatically.

Rationale: `bd` reported a repository ID mismatch in the parent repo. Forcing sync or migration without user approval could corrupt issue data.

Status: Accepted

## 2026-05-16 | D-0004 | Docs-only initialization

Decision: Do not write application code during process initialization.

Rationale: The user explicitly said "JANGAN menulis kode dulu."

Status: Accepted

## 2026-05-16 | D-0005 | Adopt user-supplied operating constitution

Decision: Replace the initial root `AGENTS.md` draft with the user-supplied Project Operating Constitution and fill repository orientation fields from observed workspace facts.

Rationale: The user provided a more concise constitution with explicit work modes, stop conditions, progress scoring, and Boris-style workflow constraints.

Status: Accepted

## 2026-05-16 | D-0006 | Add universal process OS

Decision: Add `docs/process/OPERATING_SYSTEM.md`, `docs/process/TASK_ROUTING.md`, and `docs/process/QUALITY_GATES.md` as the reusable operating layer for all task types.

Rationale: The workspace needs to support implementation, research, wiki maintenance, review/audit, C4-ET gates, and release/handoff without relying on ad hoc task handling.

Status: Accepted

## 2026-05-16 | D-0007 | Add evidence and research templates

Decision: Add root process templates for MAS evidence packets and AutoResearch artifacts.

Rationale: The operating system needs concrete artifacts for primary-source factual claims and reusable research tasks before those workflows can be validated in real work.

Status: Accepted

## 2026-05-16 | D-0008 | Accept GO-TRIAL review validation

Decision: Treat the process consistency review as the first GO-TRIAL validation of the universal process OS for Review/Audit work.

Rationale: The task used `TASK_ROUTING.md` for mode selection, `QUALITY_GATES.md` for gate checks, and `OPERATING_SYSTEM.md` for the intake-execute-verify-log-handoff loop. Remaining validation is still required for implementation and research tasks.

Status: Accepted

## 2026-05-16 | D-0009 | Repository boundary remains NO-GO

Decision: Do not commit, push, sync `bd`, migrate `bd`, or change remotes from the current state.

Rationale: The Karpathy project directory is nested inside the Git root `C:\Users\Gysje P`, whose remote is `casemix-bpjs-analisis-2026`. The Karpathy project root has no local `.git` or `.beads`, while the active parent `.beads` reports a repository ID mismatch. Committing now could mix Karpathy files, credential-like files, and unrelated home-directory changes into the wrong remote.

Status: Accepted

## 2026-05-16 | D-0010 | Initialize project-local Git and bd

Decision: Keep the project in `C:\Users\Gysje P\Documents\Adi File\Karpathy` as a nested but project-local Git repository, with a local `.gitignore` and local `bd` database.

Rationale: The user identified this path as the correct project root. Moving/copying the full workspace would be safer for isolation but more disruptive. A nested project-local repo is acceptable if commits are made only from the Karpathy root, secrets/data/generated artifacts stay ignored, and no parent repo staging is used.

Status: Accepted

## 2026-05-16 | D-0011 | First local commit uses selective process-only staging

Decision: Stage and commit only the project operating system, process logs, root wiki process pages, `skills/README.md`, `.gitignore`, and safe `.beads` metadata.

Rationale: The workspace contains credential-like files, large data/media, generated artifacts, archives, and nested source subprojects. A first commit should establish process governance without accidentally tracking secrets or source corpora that need separate review.

Status: Accepted

## 2026-05-16 | D-0012 | Hold source corpus pending curated reviews

Decision: Do not stage `Bahan/`, `LLM Wiki Karpathy/`, `_tmp*/`, generated bundles, archive/media/data files, or nested source projects in the next batch. Allow `.gitattributes` in a future selective process metadata batch, and hold `CLAUDE.md` / `MASTER_INDEX.md` for a small curated orientation-doc review.

Rationale: Inventory found credential-like files under `Bahan/.streamlit`, archive/data files, local DB files, generated template folders, and a nested Git repo at `Bahan/Karpathy RAG system/llm-wiki/.git`. No files exceed 10MB, so Git LFS is not required now.

Status: Accepted

## 2026-05-16 | D-0013 | Commit curated source orientation docs

Decision: Commit `.gitattributes`, `CLAUDE.md`, and `MASTER_INDEX.md` as a narrow curated orientation-doc batch, while continuing to block broad source corpus staging.

Rationale: Byte-level UTF-8 checks passed, mojibake was not present in file content, credential-like scanning found no secret assignments or private-key material, and cached diff checks showed only the explicit three-file staged set. The only credential-like match was the non-secret phrase `hemat token`.

Status: Accepted

## 2026-05-16 | D-0014 | Keep push and bd sync blocked until remote is explicit

Decision: Treat push and `bd sync` as NO-GO until the user selects and verifies the correct Karpathy project remote/upstream.

Rationale: Remote audit found `NO_REMOTE_CONFIG`, `NO_BRANCH_UPSTREAM_CONFIG`, and 515 untracked entries outside tracked process scope. Local commits are safe only after explicit staging review; release/push is not safe without a verified remote.

Status: Accepted

## 2026-05-16 | D-0015 | Root test command remains unresolved

Decision: Use structural docs/process verification for root process work, and stop before implementation work until an authoritative subproject and canonical test command are selected.

Rationale: Test discovery found no root `package.json`, `pyproject.toml`, `Makefile`, pytest/tox/nox config, or Docker compose file. Candidate Python subprojects exist, but they are in source corpus or ignored template paths and require separate audit.

Status: Accepted

## 2026-05-16 | D-0016 | Accept local MAS and AutoResearch trials

Decision: Count the local MAS evidence packet and AutoResearch artifact trials as workflow validation for process maturity, while keeping real product/research validation as future work.

Rationale: The trials used primary local files and read-only command outputs, included unresolved claims, and avoided external or credential evidence. This validates the artifact mechanics without overstating product-level research completeness.

Status: Accepted

## 2026-05-16 | D-0017 | C4-ET gate blocks broad source corpus staging

Decision: Broad source corpus staging remains NO-GO. Continue only with narrow, explicitly audited process/wiki/source-doc batches.

Rationale: The C4-ET dry run found high WIP breadth, known credential-risk zones, a nested Git repo, and missing release remote/upstream. A curated batch process is the safer throughput experiment.

Status: Accepted

## 2026-05-16 | D-0018 | Use Karpathy-Protokol as project remote

Decision: Configure `origin` as `https://github.com/DanielAdrian975/Karpathy-Protokol.git`, rename the local branch to `main`, push to `origin/main`, and use `bd --no-daemon sync` for issue sync.

Rationale: The user provided the explicit project remote URL. The remote was reachable and had no existing heads before first push. `bd sync` expected `origin/main`, so using `main` avoids sync mismatch while preserving the local commit history.

Status: Accepted
