# Task Routing Matrix

Use this matrix at intake to route work consistently.

## Routing Table

| User Intent | Primary Mode | Required Framework | Required Artifacts |
|---|---|---|---|
| Change code or scripts | Implementation | Boris-style workflow | Plan, diff, tests/checks, progress update |
| Fix bug | Implementation | Review/Audit support | Repro or hypothesis, patch, tests, risk note |
| Add tests | Implementation | Test skill | Test files, test command, result |
| Explain code | Review/Audit | None unless factual external claims appear | File references, limits |
| Review code/docs | Review/Audit | Review skill | Findings, severity, file references, residual risk |
| Research a topic | Research / AutoResearch | MAS Evidence-First | Research plan, primary evidence, synthesis, unresolved claims |
| Compare tools/APIs/standards | Research / AutoResearch | MAS Evidence-First | Primary docs/specs, comparison table, unresolved claims |
| Ingest source into memory | Wiki Maintenance | LLM Wiki | SourceID, source page, index update, log entry |
| Update process docs | Wiki Maintenance | LLM Wiki + Review/Audit | Process file update, index/log if durable |
| Decide team/capacity | C4-ET Gate | C4-ET | A1-A4, B1-B4, ET1-ET3, GO/NO-GO/GO-TRIAL |
| Release or finish session | Release / Handoff | Release skill | Quality gates, issue status, git status, handoff |

## Stop And Escalate

Stop before execution when:

- The required test command is unknown for a code change.
- The repo or issue tracker state makes commit/push unsafe.
- Required evidence is unavailable for a factual claim.
- The request would require reading secrets.
- Product, security, legal, or financial-advice boundaries are unclear.

## Default Outputs By Mode

### Implementation

- Goal.
- Files touched.
- Tests/checks run.
- Diff summary.
- Risks.
- Progress update.

### Research / AutoResearch

- Research question.
- Evidence standard.
- Primary sources used.
- Atomic claims and status.
- Synthesis.
- Unresolved claims.

### C4-ET Gate

- A1-A4 checklist.
- B1-B4 metrics.
- ET1-ET3 evaluation.
- Gate result.
- Recommended experiment or next action.

### Wiki Maintenance

- Source or decision basis.
- Pages updated.
- Index entry.
- Log entry.
- Contradictions or stale claims.

### Review/Audit

- Findings first.
- Severity.
- Evidence and file references.
- Open questions.
- Residual risk.
