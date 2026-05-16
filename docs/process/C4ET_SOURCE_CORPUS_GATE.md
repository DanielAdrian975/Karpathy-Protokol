# C4-ET Source Corpus Staging Gate

Date: 2026-05-16
Mode: C4-ET Gate + Review/Audit
Question: Should broad source corpus staging proceed now?

## Gate Result

Result: **NO-GO**

Staging the broad source corpus should not proceed now. Only narrow, explicitly audited process/wiki batches should be staged.

## A1-A4 Checklist

| Check | Question | Finding | Status |
|---|---|---|---|
| A1 | Is the decision about capacity, bottleneck, WIP, lead time, or deadlock? | Yes. The active bottleneck is repository readiness and staging WIP across a large unreviewed corpus. | pass |
| A2 | Is the current system state observable? | Partially. Git status shows 515 untracked entries; source inventory identifies risky groups. | pass |
| A3 | Are constraints explicit? | Yes: no push, no `bd sync`, no remote changes, no broad staging, no credential reads. | pass |
| A4 | Is there a reversible small trial? | Yes: continue curated batch audits and process-only commits. | pass |

## B1-B4 Metrics

| Metric | Current Value | Evidence | Interpretation |
|---|---:|---|---|
| B1 WIP breadth | 515 untracked entries | `git status --short --untracked-files=all` count | Too broad for safe batch staging. |
| B2 Known credential-risk zones | 1 protected root pattern family | `Bahan\.streamlit\*` in source inventory and `.gitignore` | Requires permanent exclusion. |
| B3 Nested repo count | 1 known nested `.git` under `Bahan\Karpathy RAG system\llm-wiki\.git` | Source/subproject inventory | Needs submodule/separate repo decision. |
| B4 Release blocker count | 2 primary blockers | no remote/upstream, no `bd sync` | Push/release remains blocked. |

## ET1-ET3 Evaluation

| Evaluation | Finding | Decision |
|---|---|---|
| ET1 Expected throughput | Broad staging would create high review load and increase chance of accidental secret/data inclusion. | negative |
| ET2 Error tolerance | Error tolerance is low because credential-like files and nested repositories exist. | negative |
| ET3 Trial design | Curated batch staging gives reversible, inspectable increments. | positive |

## Decision

**NO-GO** for broad source corpus staging.

Allowed:

- Continue process/wiki artifact commits.
- Run targeted sensitivity/provenance reviews.
- Stage explicitly audited small batches only.

Blocked:

- `git add .`
- broad `Bahan/` staging
- broad `LLM Wiki Karpathy/` staging
- `_tmp*/` staging
- archives, media, local DBs, generated artifacts
- push and `bd sync` before remote/upstream verification

## Recommended Next Experiment

Run a small **Legacy Wiki Sensitivity/Provenance Audit** over `LLM Wiki Karpathy/INDEX.md`, `00_SOURCE_REGISTRY.md`, and `UNRESOLVED.md` only. Do not stage the legacy wiki folder until the audit determines which pages are safe and useful as tracked project memory.
