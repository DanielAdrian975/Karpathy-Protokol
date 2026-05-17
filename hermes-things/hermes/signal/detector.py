"""
hermes.signal.detector
----------------------
Main signal detector. Combines data fetching, market analysis,
and confluence scoring into a single Signal output.
"""

from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime, timezone

from hermes.data.fetcher import OHLCVData
from hermes.market import structure as mkt_structure
from hermes.market import fibonacci as fib_calc
from hermes.market import levels as lvl_calc
from hermes.market import sessions as sess_check
from hermes.signal.confluence import ConfluenceResult, score as confluence_score, ConfluenceWeights


@dataclass
class Signal:
    symbol: str
    timestamp: datetime
    direction: str            # "long" | "short" | "none"
    strength: str             # "STRONG" | "MEDIUM" | "SKIP"
    confluence: ConfluenceResult
    entry_zone_low: float
    entry_zone_high: float
    suggested_sl: float
    suggested_tp: float
    notes: list[str]


def detect(
    symbol: str,
    htf_data: OHLCVData,      # D1 or H4 bars for bias
    structure_data: OHLCVData, # H1 bars for structure events
    entry_data: OHLCVData,     # M15 bars for OTE entry
    pip_size: float = 0.0001,
    sl_pips: float = 15.0,
    tp_ratio: float = 2.0,
    weights: ConfluenceWeights | None = None,
    min_strong: int = 6,
    min_medium: int = 4,
) -> Signal:
    """
    Run the full Chris Lori signal detection pipeline for one symbol.
    """
    notes: list[str] = []

    # 1. HTF bias from higher timeframe data
    htf_result = mkt_structure.analyze(
        highs=htf_data.highs,
        lows=htf_data.lows,
        closes=htf_data.closes,
    )
    notes.append(f"HTF bias ({htf_data.timeframe}): {htf_result.bias.value}")

    # 2. Structure event from H1
    struct_result = mkt_structure.analyze(
        highs=structure_data.highs,
        lows=structure_data.lows,
        closes=structure_data.closes,
    )
    notes.append(f"Structure event ({structure_data.timeframe}): {struct_result.event.value}")

    # 3. Fibonacci OTE from latest swing on H1
    if struct_result.last_swing_high and struct_result.last_swing_low:
        # Guard: ensure swing_high > swing_low for valid fib calculation
        raw_sh = struct_result.last_swing_high.price
        raw_sl = struct_result.last_swing_low.price
        true_sh = max(raw_sh, raw_sl)
        true_sl = min(raw_sh, raw_sl)
        fib = fib_calc.from_structure(
            last_swing_high=true_sh,
            last_swing_low=true_sl,
            bias=htf_result.bias.value,
        )
        notes.append(f"OTE zone: {fib.ote_low:.5f} - {fib.ote_high:.5f}")
    else:
        # Fallback: use entry_data range
        true_sh = max(entry_data.highs[-50:]) if entry_data.highs else 1.0
        true_sl = min(entry_data.lows[-50:])  if entry_data.lows  else 0.9
        fib = fib_calc.from_structure(true_sh, true_sl, htf_result.bias.value)
        notes.append("OTE: estimated from recent range (no clear swing)")

    # 4. PDH/PDL from daily bars
    lvl_result = lvl_calc.calculate(entry_data.bars, pip_size=pip_size)
    notes.append(f"PDH: {lvl_result.pdh:.5f}  PDL: {lvl_result.pdl:.5f}")

    # 5. Session check (now)
    sess_result = sess_check.check()
    notes.append(f"Session: {sess_result.active_session or 'none'} | killzone={sess_result.is_killzone}")

    # 6. Confluence score
    current_price = entry_data.closes[-1] if entry_data.closes else 0.0
    conf = confluence_score(
        structure=htf_result,
        fib=fib,
        levels=lvl_result,
        session=sess_result,
        current_price=current_price,
        weights=weights,
        min_strong=min_strong,
        min_medium=min_medium,
    )

    # 7. Compute entry zone, SL, TP
    sl_price = tp_price = 0.0
    sl_delta = sl_pips * pip_size

    if conf.direction == "long":
        entry_low  = fib.ote_low
        entry_high = fib.ote_high
        sl_price   = entry_low - sl_delta
        tp_price   = entry_high + (sl_delta * tp_ratio)
    elif conf.direction == "short":
        entry_low  = fib.ote_low
        entry_high = fib.ote_high
        sl_price   = entry_high + sl_delta
        tp_price   = entry_low - (sl_delta * tp_ratio)
    else:
        entry_low = entry_high = current_price

    return Signal(
        symbol=symbol,
        timestamp=datetime.now(timezone.utc),
        direction=conf.direction,
        strength=conf.strength.value,
        confluence=conf,
        entry_zone_low=entry_low,
        entry_zone_high=entry_high,
        suggested_sl=sl_price,
        suggested_tp=tp_price,
        notes=notes,
    )
