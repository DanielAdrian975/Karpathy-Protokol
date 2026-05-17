---
id: T-D
name: "PDH PDL Levels"
category: D
strategies: 5
articles: [5]
entities: [E007]
---

# Topic D — PDH/PDL Levels

Previous Day High dan Previous Day Low sebagai level institusional kunci.

## Ringkasan

PDH (Previous Day High) dan PDL (Previous Day Low) adalah level yang paling diperhatikan oleh institusi besar. Harga yang break dan close di atas PDH sinyal bullish intent; close di bawah PDL sinyal bearish intent. Sebaliknya, harga yang menolak di PDH/PDL menambah konfirmasi. Tolerance 5 pips digunakan untuk mendeteksi "at level" confluence, menambah +1 ke skor.

## Scenarios

| Kondisi | Bias Arah | Confluence Bonus |
|---|---|---|
| Close > PDH | Bullish expansion | +1 |
| Close < PDL | Bearish expansion | +1 |
| Wick di PDH, close below | Bearish rejection | +1 |
| Wick di PDL, close above | Bullish rejection | +1 |
| Price at midpoint | Tidak ada | 0 |

## Kode

`hermes/market/levels.py` — `LevelsResult`, `calculate()`.
