"""
hermes.market.levels
--------------------
Previous Day High/Low (PDH/PDL) and key institutional levels.
These act as magnet levels; BOS at PDH/PDL signals directional intent.
"""

from __future__ import annotations
from dataclasses import dataclass
from datetime import date
from hermes.data.fetcher import Bar


@dataclass
class DayLevels:
    date: date
    pdh: float   # Previous Day High
    pdl: float   # Previous Day Low
    mid: float   # PDH/PDL midpoint


@dataclass
class LevelsResult:
    pdh: float
    pdl: float
    mid: float
    price_vs_pdh: str   # "above" | "below" | "at"
    price_vs_pdl: str
    bos_pdh: bool       # Price closed above PDH
    bos_pdl: bool       # Price closed below PDL
    confluence: bool    # Price reacting at PDH or PDL (within tolerance)


def _day_group(bars: list[Bar]) -> dict[date, list[Bar]]:
    groups: dict[date, list[Bar]] = {}
    for bar in bars:
        d = bar.time.date()
        groups.setdefault(d, []).append(bar)
    return groups


def calculate(bars: list[Bar], tolerance_pips: float = 5.0, pip_size: float = 0.0001) -> LevelsResult:
    """
    Calculate PDH/PDL from daily bars.
    If intraday bars are passed, groups them by date first.
    """
    tol = tolerance_pips * pip_size
    groups = _day_group(bars)
    sorted_days = sorted(groups.keys())

    if len(sorted_days) < 2:
        raise ValueError("Need at least 2 days of data to calculate PDH/PDL.")

    prev_day = sorted_days[-2]
    prev_bars = groups[prev_day]

    pdh = max(b.high for b in prev_bars)
    pdl = min(b.low for b in prev_bars)
    mid = (pdh + pdl) / 2.0

    # Use last close as current price proxy
    last_close = bars[-1].close

    bos_pdh = last_close > pdh
    bos_pdl = last_close < pdl
    confluence = abs(last_close - pdh) <= tol or abs(last_close - pdl) <= tol

    if last_close > pdh + tol:
        vs_pdh = "above"
    elif last_close < pdh - tol:
        vs_pdh = "below"
    else:
        vs_pdh = "at"

    if last_close > pdl + tol:
        vs_pdl = "above"
    elif last_close < pdl - tol:
        vs_pdl = "below"
    else:
        vs_pdl = "at"

    return LevelsResult(
        pdh=pdh,
        pdl=pdl,
        mid=mid,
        price_vs_pdh=vs_pdh,
        price_vs_pdl=vs_pdl,
        bos_pdh=bos_pdh,
        bos_pdl=bos_pdl,
        confluence=confluence,
    )
