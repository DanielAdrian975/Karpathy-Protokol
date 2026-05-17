---
id: E005
name: "OTE Zone"
type: entry
category: B
related: [E006, E002, E001]
strategies: ["3-9", "3-10", "3-11", "3-12"]
---

# OTE Zone — Optimal Trade Entry

Zona Fibonacci 0.618–0.786 sebagai area masuk optimal dalam metodologi ICT Chris Lori.

## Definisi

Setelah bias HTF terkonfirmasi dan market structure event (BOS/CHoCH) terdeteksi, harga sering retrace ke zona 61.8%–78.6% dari swing terakhir sebelum melanjutkan arah bias. Zona ini disebut OTE.

| Level | Nama | Keterangan |
|---|---|---|
| 0.618 | OTE Lower Bound | Batas atas zona untuk bullish (batas bawah harga) |
| 0.705 | OTE Midpoint | Zona tengah, entry optimal |
| 0.786 | OTE Upper Bound | Batas bawah zona untuk bullish (batas atas harga) |

## Cara Menggambar

- **Bullish**: Fibonacci dari swing LOW ke swing HIGH. OTE = retrace ke 61.8%–78.6%.
- **Bearish**: Fibonacci dari swing HIGH ke swing LOW. OTE = retrace ke 61.8%–78.6%.

## Invalidasi

Jika harga close di bawah swing low (untuk bullish OTE) atau di atas swing high (untuk bearish OTE), setup diinvalidasi — gambar ulang Fibonacci dari swing baru.

## Confluence Score

Harga berada di OTE zone saat signal detection → +2 poin ke skor confluence.

## Referensi Kode

`hermes/market/fibonacci.py:FibLevels.in_ote()` — mengecek apakah harga saat ini di dalam OTE zone.
