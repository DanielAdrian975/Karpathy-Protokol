---
id: T-C
name: "Session Killzones"
category: C
strategies: 5
articles: [4]
entities: [E008, E013]
---

# Topic C — Session Killzones

Timing filter menggunakan sesi forex untuk entri berkualitas tinggi.

## Ringkasan

Killzone adalah jendela waktu saat smart money/institusi paling aktif, menciptakan pergerakan harga yang tajam dan terarah. London Open (02:00–05:00 EST) dan New York Open (07:00–10:00 EST) adalah killzone primer, masing-masing bernilai +1 pada skor confluence. Asian session bernilai 0.5 dan hanya valid untuk setup skor >= 7. Di luar killzone, sinyal tidak dihitung.

## Session Times (EST)

| Session | Start | End | Weight |
|---|---|---|---|
| London | 02:00 | 05:00 | 1.0 (+1) |
| New York | 07:00 | 10:00 | 1.0 (+1) |
| Asian | 20:00 | 00:00 | 0.5 |

## Kode

`hermes/market/sessions.py` — `SessionConfig`, `check()`, `SESSIONS`.
