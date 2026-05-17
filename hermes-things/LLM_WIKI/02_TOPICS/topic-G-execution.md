---
id: T-G
name: "Trade Execution and Pipeline"
category: G
strategies: 12
articles: [8, 9, 10]
entities: [E011, E012, E014]
---

# Topic G — Trade Execution and Pipeline

Aturan eksekusi trade dan otomasi pipeline penuh.

## Ringkasan

Setelah confluence score mencapai threshold, eksekusi mengikuti aturan SL/TP yang ketat. SL ditempatkan di luar swing origin (min 10 pips, default 15 pips). TP = SL x RR ratio (default 2.0). Posisi dimasukkan di midpoint OTE zone. Pipeline otomasi mencakup tiga mode: backtest (walk-forward historical), optimizer (grid search parameter), dan live scan (polling real-time setiap 60 detik).

## Execution Rules

| Aturan | Detail |
|---|---|
| SL | Di luar swing low/high, minimum 10 pips |
| TP | SL x RR (default 2.0, minimum 1.5) |
| Entry | Midpoint OTE zone, limit order |
| BE Move | Setelah +1R, pindah SL ke break-even |
| Max Risk | 1-2% per trade |
| Daily Limit | Stop setelah 3 losses berturut atau -5% account |
| Pairs | 7 forex majors only |

## Pipeline Modes

| Mode | Command | Use Case |
|---|---|---|
| Scan | `--mode=scan` | Single pass, cek sinyal saat ini |
| Live | `--mode=live` | Polling loop 60 detik |
| Backtest | `--mode=backtest` | Walk-forward historical |
| Optimize | `--mode=optimize` | Grid search parameter |

## Kode

`hermes/execution/backtest.py`, `hermes/execution/live.py`, `hermes/execution/optimizer.py`, `hermes/agent.py`.
