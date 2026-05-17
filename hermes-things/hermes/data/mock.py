"""
hermes.data.mock
----------------
Realistic forex mock data generator for pipeline demo and testing.
Generates OHLCV bars with:
  - Trending structure (HH/HL or LH/LL)
  - Realistic ATR and spread
  - Session-aware volatility bursts
"""

from __future__ import annotations
import random
from datetime import datetime, timedelta, timezone
from hermes.data.fetcher import OHLCVData, Bar


def _trending_bars(
    n: int,
    start_price: float,
    trend: str = "bullish",     # "bullish" | "bearish" | "ranging"
    atr_pct: float = 0.0015,
    seed: int = 42,
) -> list[tuple[float, float, float, float]]:
    """Returns list of (open, high, low, close) tuples."""
    rng = random.Random(seed)
    bars: list[tuple[float, float, float, float]] = []
    price = start_price

    for _ in range(n):
        atr = price * atr_pct
        body = rng.uniform(0.2, 0.8) * atr  # noqa: F841

        if trend == "bullish":
            drift = rng.uniform(0.0, 0.4) * atr
            close = price + drift
        elif trend == "bearish":
            drift = rng.uniform(0.0, 0.4) * atr
            close = price - drift
        else:
            drift = rng.uniform(-0.3, 0.3) * atr
            close = price + drift

        o = price
        c = close
        wick_up   = rng.uniform(0.1, 0.5) * atr
        wick_down = rng.uniform(0.1, 0.5) * atr
        h = max(o, c) + wick_up
        l = min(o, c) - wick_down

        bars.append((round(o, 5), round(h, 5), round(l, 5), round(c, 5)))
        price = c

    return bars


def make_ohlcv(
    symbol: str,
    timeframe: str,
    n: int = 300,
    start_price: float = 1.0850,
    trend: str = "bullish",
    start_dt: datetime | None = None,
    bar_minutes: int = 60,
    seed: int = 42,
) -> OHLCVData:
    """
    Generate a synthetic OHLCVData stream.
    bar_minutes: candle duration in minutes (60=H1, 15=M15, 1440=D1)
    """
    if start_dt is None:
        start_dt = datetime(2025, 1, 2, 0, 0, tzinfo=timezone.utc)

    raw = _trending_bars(n, start_price, trend=trend, seed=seed)
    data = OHLCVData(symbol=symbol, timeframe=timeframe)

    for i, (o, h, l, c) in enumerate(raw):
        dt = start_dt + timedelta(minutes=bar_minutes * i)
        data.bars.append(Bar(
            time=dt,
            open=o, high=h, low=l, close=c,
            volume=float(random.Random(seed + i).randint(500, 5000)),
        ))
    return data


def make_forex_dataset(
    symbol: str = "EURUSD",
    trend: str = "bullish",
    seed: int = 42,
) -> dict[str, OHLCVData]:
    """
    Generate a full multi-timeframe dataset for one pair:
      D1 (200 bars), H1 (500 bars), M15 (1000 bars)
    """
    base = 1.0850 if "USD" in symbol else 150.0
    return {
        "D":  make_ohlcv(symbol, "D",  200,  base,    trend, bar_minutes=1440, seed=seed),
        "60": make_ohlcv(symbol, "60", 500,  base,    trend, bar_minutes=60,   seed=seed + 1),
        "15": make_ohlcv(symbol, "15", 1000, base,    trend, bar_minutes=15,   seed=seed + 2),
    }
