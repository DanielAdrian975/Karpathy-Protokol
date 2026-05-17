---
id: CL-001
title: "Empirical Claims — Chris Lori ICT Methodology"
status: research_only
updated: "2026-05-18"
---

# Empirical Claims

> Status: research-only. Semua klaim di bawah ini adalah hipotesis yang memerlukan backtesting dengan data primer sebelum dianggap valid.

## Klaim Yang Diimplementasi

| ID | Klaim | Basis | Status |
|---|---|---|---|
| CL-1 | HTF bias dari D1+H4 HH/HL atau LH/LL prediktif terhadap arah intraday | Chris Lori methodology, ICT | Hipotesis — perlu backtest |
| CL-2 | OTE zone 0.618-0.786 memiliki probabilitas reversal lebih tinggi dari zona lain | ICT Fibonacci methodology | Hipotesis — perlu backtest |
| CL-3 | London/NY killzones menghasilkan sinyal lebih berkualitas dari waktu lain | Session timing research | Hipotesis — perlu backtest |
| CL-4 | PDH/PDL berperan sebagai level magnet institusional | Institutional price action | Hipotesis — perlu backtest |
| CL-5 | Skor confluence >= 6/8 menghasilkan win rate > 50% | Implementasi hermes-things | Belum divalidasi dengan data nyata |

## Batasan

- Semua hasil dari `demo.py` menggunakan **mock data deterministik**, bukan data pasar nyata
- 100% win rate pada mock data TIDAK mencerminkan performa live
- Backtesting perlu dilakukan dengan data historis tick-level untuk validitas
- Forward testing wajib sebelum aplikasi apapun

## Unresolved Questions

Lihat: [07_UNRESOLVED/unresolved-questions.md](../07_UNRESOLVED/unresolved-questions.md)
