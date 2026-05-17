---
id: T-E
name: "Confluence Scoring System"
category: E
strategies: 4
articles: [6]
entities: [E001, E002, E005, E007, E008, E009]
---

# Topic E — Confluence Scoring System

Sistem penilaian terpadu yang menggabungkan HTF bias, market structure, OTE, PDH/PDL, dan session timing menjadi satu skor keputusan.

## Ringkasan (3-5 kalimat)

Confluence scoring adalah lapisan keputusan final sebelum entry. Setiap elemen strategi Chris Lori diberi bobot numerik; total skor menentukan apakah setup layak dieksekusi. STRONG (>=6) dieksekusi penuh, MEDIUM (4-5) dengan ukuran diperkecil, SKIP (<4) diabaikan. Sistem ini mencegah overtrading dengan mewajibkan minimum beberapa faktor terpenuhi secara bersamaan. Override rule memastikan bias NEUTRAL tidak pernah menghasilkan STRONG signal.

## Strategies in This Topic

| No | Name | Key Rule |
|---|---|---|
| 23 | STRONG Signal | Score >= 6, execute full |
| 24 | MEDIUM Signal | Score 4-5, 50% size + M15 confirmation |
| 25 | SKIP Signal | Score < 4, no trade |
| 26 | Max Score Override | NEUTRAL bias caps score at 5 |

## Relasi ke Komponen Lain

- Menerima input dari: F (HTF bias), A (structure event), B (OTE), D (PDH/PDL), C (killzone)
- Output ke: G (execution — position size decision)
- Kode: `hermes/signal/confluence.py`, `hermes/signal/detector.py`
