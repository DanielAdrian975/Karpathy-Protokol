---
id: T-A
name: "Market Structure Events"
category: A
strategies: 4
articles: [2]
entities: [E002, E003, E004, E010]
---

# Topic A — Market Structure Events

BOS dan CHoCH sebagai sinyal struktur pada H1 yang mengkonfirmasi arah bias.

## Ringkasan

Setelah HTF bias terkonfirmasi, market structure events pada H1 memberikan konfirmasi tambahan. BOS (Break of Structure) mengkonfirmasi kontinuasi — harga menembus swing high/low terakhir sesuai arah bias. CHoCH (Change of Character) menandakan potensi reversal — harga menembus struktur berlawanan arah. Kedua event ini bernilai +2 pada confluence score.

## Strategies

| No | Name | Trigger |
|---|---|---|
| 5 | BOS Bullish | Close > last swing high in bullish bias |
| 6 | BOS Bearish | Close < last swing low in bearish bias |
| 7 | CHoCH Bullish | Close > last LH in bearish bias |
| 8 | CHoCH Bearish | Close < last HL in bullish bias |

## Kode

`hermes/market/structure.py` — `detect_structure_event()`, `StructureEvent` enum.
