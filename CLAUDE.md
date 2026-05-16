# CLAUDE.md — Workspace: Trading Basis

> Workspace-level rules. Override global CLAUDE.md jika ada konflik.

---

## Konteks

Workspace ini untuk **trading research** menggunakan Claude Code + TradingView MCP.
Bukan untuk financial advice. Output = research, hypothesis, evidence.

---

## Protokol Aktif (urutan prioritas)

| Task | Protokol | Trigger |
|---|---|---|
| Analisis market / signal research | **MAS Evidence-First** | Klaim faktual, causal, performance |
| TradingView chart operations | **Boris Workflow** | Semua MCP tool calls |
| Trading hypothesis & wiki | **trading-research-wiki** skill | Market data, hypothesis tracking |
| Dokumentasi / notes | **Karpathy Style** | Index dulu, frontmatter, 3-5 kalimat |
| Autoresearch loop | **Boris + autoresearch-optimize** | `_tmp_autoresearch_template/` |

---

## Routing Rules (Trading-Specific)

1. **Baca MASTER_INDEX.md dulu** jika konteks tidak jelas
2. **TradingView MCP**: selalu `chart_get_state` pertama, simpan entity IDs
3. **Data query**: pakai `summary=true` di `data_get_ohlcv`, `study_filter` di pine tools
4. **Screenshot > data dump**: `capture_screenshot` lebih efisien untuk visual context
5. **Max 3 file** per query (kecuali MCP tool calls)
6. **Archive = last resort**: `99_Archive/`, `_archive/`, `raw/` hanya jika diminta

---

## TradingView MCP — Aturan Wajib

```
SELALU:
- chart_get_state() dulu → simpan entity IDs, reuse sepanjang sesi
- summary=true pada data_get_ohlcv
- study_filter= pada semua pine tools jika nama indicator diketahui

JANGAN:
- verbose=true kecuali user minta raw data
- dump seluruh OHLCV tanpa summary
- panggil chart_get_state berulang kali
```

---

## Pine Script Development

```
Alur: pine_set_source → pine_smart_compile → pine_get_errors → pine_get_console
Catatan: pine_get_source bisa return 200KB+ — hindari kecuali perlu edit
```

---

## Guardrails Trading

- **Tidak ada** buy/sell/hold recommendation
- **Tidak ada** leverage atau position-size instruction untuk user spesifik
- Semua interpretasi harus dilabel "research, not advice"
- Jika data kurang/stale → output `Insufficient Evidence`

---

## Format Jawaban Default

```
[Sumber/Tool] → [Temuan] → [Batasan/Ketidakpastian]
```

---

*Terakhir diperbarui: 2026-05-07*
