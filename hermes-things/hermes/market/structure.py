"""
hermes.market.structure
-----------------------
Market structure analysis: swing detection, HH/HL/LH/LL,
Break of Structure (BOS), Change of Character (CHoCH).

Chris Lori methodology: HTF bias determined by D1+H4 swing structure.
"""

from __future__ import annotations
from dataclasses import dataclass
from enum import Enum
from typing import Optional


class Bias(Enum):
    BULLISH = "bullish"
    BEARISH = "bearish"
    NEUTRAL = "neutral"


class StructureEvent(Enum):
    BOS_BULL  = "bos_bullish"   # Break of Structure — continuation bull
    BOS_BEAR  = "bos_bearish"   # Break of Structure — continuation bear
    CHOCH_BULL = "choch_bullish" # Change of Character — reversal to bull
    CHOCH_BEAR = "choch_bearish" # Change of Character — reversal to bear
    NONE = "none"


@dataclass
class SwingPoint:
    index: int
    price: float
    kind: str  # "high" | "low"


@dataclass
class StructureResult:
    bias: Bias
    last_swing_high: Optional[SwingPoint]
    last_swing_low: Optional[SwingPoint]
    event: StructureEvent
    swing_highs: list[SwingPoint]
    swing_lows: list[SwingPoint]


def detect_swings(highs: list[float], lows: list[float], lookback: int = 3) -> tuple[list[SwingPoint], list[SwingPoint]]:
    """
    Identify swing highs and lows using a simple pivot method.
    A swing high: high[i] is the highest in window [i-lookback : i+lookback+1]
    A swing low: low[i] is the lowest in same window.
    """
    swing_highs: list[SwingPoint] = []
    swing_lows: list[SwingPoint] = []
    n = len(highs)

    for i in range(lookback, n - lookback):
        window_h = highs[i - lookback: i + lookback + 1]
        window_l = lows[i - lookback: i + lookback + 1]

        if highs[i] == max(window_h):
            swing_highs.append(SwingPoint(index=i, price=highs[i], kind="high"))
        if lows[i] == min(window_l):
            swing_lows.append(SwingPoint(index=i, price=lows[i], kind="low"))

    return swing_highs, swing_lows


def determine_bias(swing_highs: list[SwingPoint], swing_lows: list[SwingPoint]) -> Bias:
    """
    Determine HTF bias from last 2 swing highs and 2 swing lows.
    HH + HL = BULLISH
    LH + LL = BEARISH
    Mixed   = NEUTRAL
    """
    if len(swing_highs) < 2 or len(swing_lows) < 2:
        return Bias.NEUTRAL

    hh = swing_highs[-1].price > swing_highs[-2].price  # Higher High
    hl = swing_lows[-1].price > swing_lows[-2].price    # Higher Low
    lh = swing_highs[-1].price < swing_highs[-2].price  # Lower High
    ll = swing_lows[-1].price < swing_lows[-2].price    # Lower Low

    if hh and hl:
        return Bias.BULLISH
    if lh and ll:
        return Bias.BEARISH
    return Bias.NEUTRAL


def detect_structure_event(
    swing_highs: list[SwingPoint],
    swing_lows: list[SwingPoint],
    closes: list[float],
    prev_bias: Bias,
) -> StructureEvent:
    """
    Detect BOS or CHoCH on the most recent close.
    BOS = price breaks last swing high/low in direction of bias (continuation).
    CHoCH = price breaks against the bias swing (reversal signal).
    """
    if not swing_highs or not swing_lows or not closes:
        return StructureEvent.NONE

    last_close = closes[-1]
    last_sh = swing_highs[-1].price
    last_sl = swing_lows[-1].price

    if prev_bias == Bias.BULLISH:
        if last_close > last_sh:
            return StructureEvent.BOS_BULL
        if last_close < last_sl:
            return StructureEvent.CHOCH_BEAR
    elif prev_bias == Bias.BEARISH:
        if last_close < last_sl:
            return StructureEvent.BOS_BEAR
        if last_close > last_sh:
            return StructureEvent.CHOCH_BULL

    return StructureEvent.NONE


def analyze(
    highs: list[float],
    lows: list[float],
    closes: list[float],
    swing_lookback: int = 3,
) -> StructureResult:
    """
    Full market structure analysis.
    Returns bias, swing points, and latest structure event.
    """
    swing_highs, swing_lows = detect_swings(highs, lows, lookback=swing_lookback)
    bias = determine_bias(swing_highs, swing_lows)
    event = detect_structure_event(swing_highs, swing_lows, closes, bias)

    last_sh = swing_highs[-1] if swing_highs else None
    last_sl = swing_lows[-1] if swing_lows else None

    return StructureResult(
        bias=bias,
        last_swing_high=last_sh,
        last_swing_low=last_sl,
        event=event,
        swing_highs=swing_highs,
        swing_lows=swing_lows,
    )
