# Skills Map

This file maps repeated workflows for this workspace. Some skills exist in `_tmp_skills_modular_build/skills_modular_build/skills/`; others are process-level contracts until installed as Codex skills.

## Required Workflow Skills

| Skill | Trigger | Existing Reference | Required Output |
|---|---|---|---|
| `test` | Code or executable workflow changed | No root skill found | Test command, result, failures, next action |
| `review` | Before handoff, PR, or risky change | No root skill found | Findings, risks, missing tests, residual risk |
| `research` | Research, factual, trading, compliance, performance claims | MAS and AutoResearch bundles | Research plan, evidence packets, citations, unresolved claims |
| `docs` | Durable docs/wiki/process updates | `llm-wiki-builder`, `trading-research-wiki` references | Updated docs, index/log updates |
| `c4-et-gate` | Capacity, team, WIP, lead-time, bottleneck, blocked-work, deadlock | `c4et-gate`, `c4et-*` references | Data audit, metrics, gate decision, one-pager |
| `release` | Session close, publish, commit, push | No root skill found | Quality gates, issue updates, commit/push status, handoff |
| `router` | Any substantial task intake | `docs/process/TASK_ROUTING.md` | Primary mode, supporting modes, required artifacts |
| `quality-gates` | Before marking work done | `docs/process/QUALITY_GATES.md` | Gate pass/fail status and blockers |

## Available Local Skill References

The modular skill bundle reports 27 skills, including:

- `mas-orchestrator`
- `mas-assessor`
- `mas-retriever-academic`
- `mas-retriever-official`
- `mas-redteam`
- `mas-judge`
- `c4et-gate`
- `c4et-data-audit`
- `c4et-metrics-calculator`
- `c4et-gate-decision`
- `c4et-team-type-selector`
- `c4et-onepager-writer`
- `workflow-capture`
- `llm-wiki-builder`
- `atomic-journal`
- `trading-research-wiki`
- `ai-output-evaluator`

Reference root:

```text
_tmp_skills_modular_build/skills_modular_build/skills/
```

## Default Skill Routing

- Use `router` at task intake.
- Use `research` plus MAS for factual claims.
- Use `docs` for wiki/process/documentation changes.
- Use `test` before claiming code work is complete.
- Use `review` before handoff or release.
- Use `c4-et-gate` only when capacity trigger terms are present.
- Use `quality-gates` before final handoff.
- Use `release` at session close when Git and `bd` are healthy.

## Installation Gap

No root `.codex/skills` directory was found during baseline inspection. Until skills are installed, use this file as the operational map and manually apply the referenced workflows.
