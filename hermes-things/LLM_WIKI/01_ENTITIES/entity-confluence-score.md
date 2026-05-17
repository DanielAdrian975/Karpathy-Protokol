---
id: E009
name: "Confluence Score"
type: framework
category: E
related: [E001, E002, E005, E007, E008]
strategies: ["6-23", "6-24", "6-25", "6-26"]
---

# Confluence Score

Sistem penilaian 0–8 yang mengkombinasikan semua elemen strategi Chris Lori menjadi satu angka keputusan.

## Komponen Scoring

| Faktor | Bobot | Kondisi |
|---|---|---|
| HTF bias aligned | +2 | D1+H4 BULLISH atau BEARISH (bukan NEUTRAL) |
| Market structure event | +2 | BOS atau CHoCH terdeteksi |
| OTE zone | +2 | Harga berada di Fibonacci 0.618–0.786 |
| Killzone active | +1 | London (02:00-05:00 EST) atau NY (07:00-10:00 EST) |
| PDH/PDL confluence | +1 | Harga bereaksi di PDH atau PDL (dalam tolerance 5 pips) |
| **TOTAL** | **8** | |

## Threshold Keputusan

| Score | Strength | Aksi |
|---|---|---|
| >= 6 | STRONG | Execute full size |
| 4–5 | MEDIUM | Execute reduced size (50%), butuh M15 konfirmasi |
| < 4 | SKIP | Jangan trade, tunggu sesi berikutnya |

## Override Rules

- HTF bias = NEUTRAL → score maksimal dikap di 5, tidak bisa STRONG
- Asian session active (bukan London/NY) → killzone weight = 0.5, tidak menambah poin penuh

## Referensi Kode

`hermes/signal/confluence.py:score()` — fungsi utama yang mengimplementasi semua komponen ini.
