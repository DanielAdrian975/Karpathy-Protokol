---
id: T-B
name: "Fibonacci OTE Zone"
category: B
strategies: 4
articles: [3]
entities: [E005, E006]
---

# Topic B — Fibonacci OTE Zone

Entry precision zone menggunakan retracement 61.8%–78.6%.

## Ringkasan

Fibonacci OTE (Optimal Trade Entry) adalah zona harga dimana probabilitas reversal ke arah bias tertinggi. Zona ini dihitung dari swing terakhir yang signifikan pada H1. Entry dilakukan saat harga retrace ke zona 0.618–0.786, memberikan risk-reward yang optimal dengan SL di luar swing origin. Jika harga menembus swing origin tanpa entry, setup diinvalidasi.

## Strategies

| No | Name | Key Rule |
|---|---|---|
| 9 | OTE Long | Retrace to 0.618-0.786 in bullish bias |
| 10 | OTE Short | Retrace to 0.618-0.786 in bearish bias |
| 11 | 50% Equilibrium | Acceptable if score >= 5 |
| 12 | Invalidation | Close beyond swing origin = redraw |

## Kode

`hermes/market/fibonacci.py` — `FibLevels`, `calculate()`, `from_structure()`.
