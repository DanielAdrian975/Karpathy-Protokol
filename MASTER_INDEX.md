# MASTER_INDEX.md — Trading Basis Workspace

> **Baca ini pertama** sebelum membuka file lain di workspace ini.

---

## Konteks Workspace

Workspace ini adalah basis untuk trading research + AI decision-making tools menggunakan Claude Code + TradingView MCP.

**Domain utama**: Trading research, market analysis, automated signal research (bukan advice)
**Stack**: Claude Code (Sonnet/Opus), TradingView MCP (78 tools), Pine Script

---

## Navigasi Cepat

| Kebutuhan | Lokasi | Protokol |
|---|---|---|
| Analisis market / evidence | `Bahan/Knowledge_Management_System/` | MAS Evidence-First |
| Trading research wiki | `/trading-research-wiki` skill | trading-research-wiki |
| TradingView chart operations | MCP tools (`mcp__tradingview__*`) | Boris Workflow |
| Knowledge extraction | `Bahan/Enhance Pengetahuan Ekstraktor/` | Karpathy Style |
| Autoresearch loop | `_tmp_autoresearch_template/` | Boris + C4-ET |
| Protokol referensi | `Bahan/Knowledge_Management_System/Claude CLI/` | — |

---

## Protokol Routing (Trading Context)

```
Query type               → Protokol
─────────────────────────────────────────────────
Market signal / analisis → MAS Evidence-First
TradingView operations   → Boris Workflow (plan→exec→verify)
Research dokumentasi     → Karpathy Style
Trading hypothesis       → trading-research-wiki skill
Team/capacity decision   → C4-ET Gate (jika relevan)
```

---

## Skills Tersedia (Trading-Relevant)

```
/trading-research-wiki   → Buat research wiki dari data primer
/mas-orchestrator        → Full MAS evidence pipeline
/pipeline-fx             → FX Trading signal pipeline
/pipeline-mas            → MAS pipeline hemat token
/pipeline-plan           → Boris Workflow Phase 1 (Architect)
/pipeline-execute        → Eksekusi subtask dari plan
/graphify                → Input apapun → knowledge graph
/atomic-journal          → Journal keputusan & eksperimen
```

---

## TradingView MCP — Quick Reference

```
chart_get_state          → Selalu panggil pertama, dapatkan entity IDs
quote_get                → Real-time price snapshot
data_get_ohlcv           → OHLCV bars (selalu summary=true)
data_get_pine_labels     → Custom indicator text output
data_get_pine_tables     → Table data dari indicator
capture_screenshot       → Visual context (lebih efisien dari data dump)
pine_set_source          → Inject Pine Script
pine_smart_compile       → Compile + check errors
```

---

## Guardrails

- **Trading research only** — tidak ada buy/sell/hold advice
- **Primary sources** untuk klaim faktual (price data, backtests)
- **Insufficient Evidence** jika data tidak cukup atau stale
- Konsultasikan profesional untuk keputusan investasi

---

*Terakhir diperbarui: 2026-05-07*
