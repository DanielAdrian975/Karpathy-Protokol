---
id: T-F
name: "HTF Bias Analysis"
category: F
strategies: 6
articles: [1, 7]
entities: [E001, E010]
---

# Topic F — HTF Bias Analysis

Penentuan arah pasar dari timeframe tinggi sebelum eksekusi apapun.

## Ringkasan

HTF Bias adalah prerequisit mutlak dalam strategi Chris Lori. Sebelum mencari entry, trader harus menetapkan bias pada D1 dan H4. Kedua timeframe harus setuju; jika konflik, bias = NEUTRAL dan trading dihindari atau dikurangi drastis. Bias di-refresh setiap awal London dan NY session. Swing detection menggunakan window 3 bar.

## Strategies

| No | Name | Rule |
|---|---|---|
| 1 | D1 Bullish | HH+HL on Daily |
| 2 | H4 Bullish Confirmation | H4 agrees with D1 |
| 3 | D1 Bearish | LH+LL on Daily |
| 4 | H4 Bearish Confirmation | H4 agrees with D1 |
| 27 | Bias Alignment Check | H4 must match D1 |
| 28 | Bias Refresh Protocol | Re-eval each London/NY open |

## Kode

`hermes/market/structure.py` — `detect_swings()`, `determine_bias()`, `analyze()`.
