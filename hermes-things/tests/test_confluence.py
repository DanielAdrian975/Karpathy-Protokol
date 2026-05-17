"""
Tests for hermes.signal.confluence scoring engine.
Run: python -m pytest tests/ -v
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from datetime import datetime, timezone
from hermes.market.structure import StructureResult, Bias, StructureEvent, SwingPoint
from hermes.market.fibonacci import FibLevels
from hermes.market.levels import LevelsResult
from hermes.market.sessions import SessionResult
from hermes.signal.confluence import score, ConfluenceWeights, SignalStrength


def _make_structure(bias: Bias, event: StructureEvent, sh: float = 1.1050, sl: float = 1.0900) -> StructureResult:
    return StructureResult(
        bias=bias,
        last_swing_high=SwingPoint(index=10, price=sh, kind="high"),
        last_swing_low=SwingPoint(index=5,   price=sl, kind="low"),
        event=event,
        swing_highs=[SwingPoint(index=10, price=sh, kind="high")],
        swing_lows=[SwingPoint(index=5,   price=sl, kind="low")],
    )


def _make_fib(ote_low: float, ote_high: float) -> FibLevels:
    return FibLevels(
        swing_high=1.1050,
        swing_low=1.0900,
        direction="bullish",
        levels={0.618: ote_high, 0.786: ote_low},
        ote_low=ote_low,
        ote_high=ote_high,
    )


def _make_levels(pdh: float = 1.1060, pdl: float = 1.0880, confluence: bool = False) -> LevelsResult:
    return LevelsResult(
        pdh=pdh, pdl=pdl, mid=(pdh + pdl) / 2,
        price_vs_pdh="below", price_vs_pdl="above",
        bos_pdh=False, bos_pdl=False,
        confluence=confluence,
    )


def _make_session(active: bool, name: str = "london") -> SessionResult:
    return SessionResult(
        active_session=name if active else None,
        weight=1.0 if active else 0.0,
        is_killzone=active,
        london=active,
        new_york=False,
        asian=False,
    )


def test_strong_signal_all_factors():
    """All 5 factors present → STRONG signal with max score."""
    structure = _make_structure(Bias.BULLISH, StructureEvent.BOS_BULL)
    fib       = _make_fib(ote_low=1.0992, ote_high=1.1015)   # OTE zone
    levels    = _make_levels(confluence=True)
    session   = _make_session(active=True)
    price     = 1.1000   # inside OTE

    result = score(structure, fib, levels, session, price)

    assert result.strength == SignalStrength.STRONG
    assert result.score == 8
    assert result.direction == "long"


def test_skip_neutral_bias():
    """Neutral bias → no HTF score → SKIP if other factors are weak."""
    structure = _make_structure(Bias.NEUTRAL, StructureEvent.NONE)
    fib       = _make_fib(ote_low=1.0992, ote_high=1.1015)
    levels    = _make_levels(confluence=False)
    session   = _make_session(active=False)
    price     = 1.0800   # outside OTE

    result = score(structure, fib, levels, session, price)

    assert result.strength == SignalStrength.SKIP
    assert result.direction == "none"
    assert result.score == 0


def test_medium_signal_partial_factors():
    """HTF + structure only (no OTE, no killzone, no PDH/PDL) → MEDIUM."""
    structure = _make_structure(Bias.BULLISH, StructureEvent.BOS_BULL)
    fib       = _make_fib(ote_low=1.0992, ote_high=1.1015)
    levels    = _make_levels(confluence=False)
    session   = _make_session(active=False)
    price     = 1.0800   # outside OTE

    result = score(structure, fib, levels, session, price)

    assert result.strength == SignalStrength.MEDIUM
    assert result.score == 4   # htf(2) + structure(2)
    assert result.direction == "long"


def test_bearish_direction():
    """Bearish bias + BOS → short signal."""
    structure = _make_structure(Bias.BEARISH, StructureEvent.BOS_BEAR)
    fib       = _make_fib(ote_low=1.0992, ote_high=1.1015)
    levels    = _make_levels(confluence=True)
    session   = _make_session(active=True)
    price     = 1.1000

    result = score(structure, fib, levels, session, price)

    assert result.direction == "short"
    assert result.strength in (SignalStrength.STRONG, SignalStrength.MEDIUM)


def test_custom_weights():
    """Custom weights are applied correctly."""
    structure = _make_structure(Bias.BULLISH, StructureEvent.BOS_BULL)
    fib       = _make_fib(ote_low=1.0992, ote_high=1.1015)
    levels    = _make_levels(confluence=False)
    session   = _make_session(active=False)
    price     = 1.1000

    w = ConfluenceWeights(htf_bias_aligned=1, market_structure=1, ote_zone=3, killzone_active=0, pdh_pdl_confluence=0)
    result = score(structure, fib, levels, session, price, weights=w)

    # htf(1) + structure(1) + ote(3) = 5
    assert result.score == 5


if __name__ == "__main__":
    test_strong_signal_all_factors()
    test_skip_neutral_bias()
    test_medium_signal_partial_factors()
    test_bearish_direction()
    test_custom_weights()
    print("All tests passed.")
