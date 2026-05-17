# Hermes Things

Python orchestrator untuk otomasi strategi trading Chris Lori (ICT/Institutional).

## Strategi

Implementasi berbasis metodologi Chris Lori:

| Elemen | Detail |
|---|---|
| HTF Bias | D1 + H4: HH/HL = bullish, LH/LL = bearish |
| Market Structure | H1: BOS (continuation), CHoCH (reversal) |
| OTE Zone | Fibonacci 0.618–0.786 dari last significant swing |
| PDH/PDL | Previous Day High/Low sebagai magnet levels |
| Killzones | London 02:00–05:00 EST, NY 07:00–10:00 EST |
| Confluence | Score 0–8; STRONG >= 6, MEDIUM >= 4, SKIP < 4 |

## Arsitektur

```
hermes/
├── agent.py              ← Orchestrator utama
├── pipeline.py
├── data/fetcher.py       ← OHLCV via TradingView MCP atau CSV
├── market/
│   ├── structure.py      ← HH/HL/LH/LL, BOS, CHoCH
│   ├── fibonacci.py      ← OTE zone 0.618-0.786
│   ├── levels.py         ← PDH/PDL
│   └── sessions.py       ← London/NY killzones
├── signal/
│   ├── detector.py       ← Pipeline detection per symbol
│   └── confluence.py     ← Scoring engine
└── execution/
    ├── backtest.py       ← Backtest engine
    ├── optimizer.py      ← Grid search optimizer
    └── live.py           ← Live signal runner
```

## Penggunaan

```bash
pip install -e ".[dev]"

# Scan semua pair (satu kali)
python main.py --mode=scan

# Live loop (polling setiap 60 detik)
python main.py --mode=live

# Backtest (butuh CSV data di data/csv/)
python main.py --mode=backtest --pair EURUSD GBPUSD

# Optimize parameter
python main.py --mode=optimize --pair EURUSD

# Dry run (validasi config saja)
python main.py --mode=scan --dry-run
```

## Data CSV (backtest)

Letakkan file CSV di `data/csv/` dengan format:
```
EURUSD_D.csv   ← Daily
EURUSD_60.csv  ← H1
EURUSD_15.csv  ← M15
```
Kolom: `time,open,high,low,close,volume`

## Tests

```bash
python -m pytest tests/ -v
```

## Guardrails

- Output adalah research signal, bukan financial advice
- Tidak ada eksekusi order nyata; ini adalah signal generator dan backtest engine
- Selalu validasi sinyal dengan analisis manual sebelum eksekusi di akun nyata
