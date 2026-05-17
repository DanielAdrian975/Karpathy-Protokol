"""
hermes.market.fibonacci
-----------------------
Fibonacci retracement levels + OTE zone detection.
Chris Lori OTE: 0.618 – 0.786 retracement from swing.
"""

from __future__ import annotations
from dataclasses import dataclass


@dataclass
class FibLevels:
    swing_high: float
    swing_low: float
    direction: str  # "bullish" | "bearish"
    levels: dict[float, float]  # ratio -> price
    ote_low: float
    ote_high: float

    def in_ote(self, price: float) -> bool:
        lo = min(self.ote_low, self.ote_high)
        hi = max(self.ote_low, self.ote_high)
        return lo <= price <= hi

    def nearest_level(self, price: float) -> tuple[float, float]:
        """Returns (ratio, price) of nearest fib level to given price."""
        return min(self.levels.items(), key=lambda kv: abs(kv[1] - price))


def calculate(
    swing_high: float,
    swing_low: float,
    direction: str = "bullish",
    ratios: list[float] | None = None,
    ote_low: float = 0.618,
    ote_high: float = 0.786,
) -> FibLevels:
    """
    Calculate Fibonacci retracement levels from a swing.

    Bullish: retracing DOWN from swing_high to swing_low.
      Level price = swing_high - ratio * (swing_high - swing_low)

    Bearish: retracing UP from swing_low to swing_high.
      Level price = swing_low + ratio * (swing_high - swing_low)
    """
    if ratios is None:
        ratios = [0.236, 0.382, 0.5, 0.618, 0.705, 0.786]

    rng = swing_high - swing_low
    levels: dict[float, float] = {}

    for r in ratios:
        if direction == "bullish":
            levels[r] = swing_high - r * rng
        else:
            levels[r] = swing_low + r * rng

    if direction == "bullish":
        price_ote_low  = swing_high - ote_high * rng
        price_ote_high = swing_high - ote_low  * rng
    else:
        price_ote_low  = swing_low + ote_low  * rng
        price_ote_high = swing_low + ote_high * rng

    return FibLevels(
        swing_high=swing_high,
        swing_low=swing_low,
        direction=direction,
        levels=levels,
        ote_low=price_ote_low,
        ote_high=price_ote_high,
    )


def from_structure(
    last_swing_high: float,
    last_swing_low: float,
    bias: str,
    ote_low: float = 0.618,
    ote_high: float = 0.786,
) -> FibLevels:
    """
    Convenience: build Fibonacci from market structure swings.
    Bias determines retracement direction.
    """
    return calculate(
        swing_high=last_swing_high,
        swing_low=last_swing_low,
        direction=bias,
        ote_low=ote_low,
        ote_high=ote_high,
    )
