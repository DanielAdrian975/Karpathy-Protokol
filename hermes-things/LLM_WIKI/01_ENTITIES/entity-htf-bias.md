---
id: E001
name: "HTF Bias"
type: framework
category: F
related: [E002, E010]
strategies: ["1-1", "1-2", "1-3", "1-4", "7-27", "7-28"]
---

# HTF Bias

Higher Timeframe Bias — fondasi utama semua keputusan trading dalam metodologi Chris Lori.

## Definisi

HTF Bias ditentukan dari struktur swing pada D1 (Daily) dan H4 (4-Hour). Kedua timeframe harus setuju untuk bias berkonfiden tinggi.

| Kondisi | Bias |
|---|---|
| D1 HH+HL dan H4 HH+HL | BULLISH |
| D1 LH+LL dan H4 LH+LL | BEARISH |
| Konflik D1 vs H4 | NEUTRAL |
| Data tidak cukup | NEUTRAL |

## Aturan Implementasi

- Minimum lookback: 20 bars untuk swing detection
- Re-evaluate setiap awal London dan NY session
- NEUTRAL = maximum confluence score dikap di 5 (tidak bisa STRONG)
- Swing detection: pivot dengan window 3 bar kiri dan kanan

## Referensi Kode

`hermes/market/structure.py:determine_bias()` — mengimplementasi logika ini dengan `Bias` enum (BULLISH, BEARISH, NEUTRAL).
