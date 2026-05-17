---
id: IDX-001
title: "Hermes Things — LLM Wiki Master Index"
source: STRATEGY_DATABASE.csv
strategy_count: 38
article_count: 10
category_count: 7
version: "1.0"
updated: "2026-05-18"
---

# Hermes Things — LLM Wiki

> Knowledge base untuk Chris Lori ICT/Institutional trading methodology.
> Digunakan oleh Hermes Agent untuk signal detection, risk validation, dan trade execution.

## Statistik

| Item | Count |
|---|---|
| Total strategies | 38 |
| Articles | 10 |
| Categories | 7 (A-G) |
| Entities | 14 |
| Query surfaces | 5 |

---

## Navigasi

### Categories
| Code | Name | Strategies |
|---|---|---|
| A | Market Structure | 4 (5-8) |
| B | Fibonacci / OTE | 4 (9-12) |
| C | Session Killzones | 5 (13-17) |
| D | PDH/PDL Levels | 5 (18-22) |
| E | Confluence Scoring | 4 (23-26) |
| F | HTF Bias | 4 (1-4, 27-28) |
| G | Trade Execution & Pipeline | 12 (29-38) |

### Entities
- [E001 HTF Bias](../01_ENTITIES/entity-htf-bias.md)
- [E002 Market Structure](../01_ENTITIES/entity-market-structure.md)
- [E003 BOS](../01_ENTITIES/entity-bos.md)
- [E004 CHoCH](../01_ENTITIES/entity-choch.md)
- [E005 OTE Zone](../01_ENTITIES/entity-ote-zone.md)
- [E006 Fibonacci](../01_ENTITIES/entity-fibonacci.md)
- [E007 PDH PDL](../01_ENTITIES/entity-pdh-pdl.md)
- [E008 Killzone](../01_ENTITIES/entity-killzone.md)
- [E009 Confluence Score](../01_ENTITIES/entity-confluence-score.md)
- [E010 Swing Point](../01_ENTITIES/entity-swing-point.md)
- [E011 SL Placement](../01_ENTITIES/entity-sl-placement.md)
- [E012 RR Ratio](../01_ENTITIES/entity-rr-ratio.md)
- [E013 Session](../01_ENTITIES/entity-session.md)
- [E014 Pipeline](../01_ENTITIES/entity-pipeline.md)

### Topics (per category)
- [T-A Market Structure](../02_TOPICS/topic-A-market-structure.md)
- [T-B Fibonacci OTE](../02_TOPICS/topic-B-fibonacci-ote.md)
- [T-C Session Killzones](../02_TOPICS/topic-C-sessions.md)
- [T-D PDH PDL Levels](../02_TOPICS/topic-D-pdh-pdl.md)
- [T-E Confluence Scoring](../02_TOPICS/topic-E-confluence.md)
- [T-F HTF Bias](../02_TOPICS/topic-F-htf-bias.md)
- [T-G Execution Pipeline](../02_TOPICS/topic-G-execution.md)

### Query Surfaces
- [QS-001 Pattern Lookup](../06_QUERY_SURFACES/qs-pattern-lookup.md)
- [QS-002 Signal Detection](../06_QUERY_SURFACES/qs-signal-detection.md)
- [QS-003 Risk Query](../06_QUERY_SURFACES/qs-risk-query.md)
- [QS-004 Category Filter](../06_QUERY_SURFACES/qs-category-filter.md)
- [QS-005 Pipeline Builder](../06_QUERY_SURFACES/qs-pipeline-builder.md)

---

## Strategy Flow (Chris Lori Institutional)

```
[F] HTF BIAS (D1+H4)
        |
    [A] MARKET STRUCTURE (H1: BOS / CHoCH)
        |
    [B] FIBONACCI OTE (0.618-0.786 retrace)
        |
    [D] PDH/PDL LEVELS (magnet & confirmation)
        |
    [C] SESSION KILLZONE (London/NY active?)
        |
    [E] CONFLUENCE SCORE (0-8)
        |
    STRONG(>=6) -> [G] EXECUTE
    MEDIUM(4-5) -> [G] REDUCED SIZE
    SKIP(<4)    -> WAIT
```
