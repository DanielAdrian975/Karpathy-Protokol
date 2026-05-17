"""
hermes.signal.confluence
------------------------
Confluence scoring engine.
Combines all Chris Lori elements into a numeric score.

Score weights (configurable via strategy.yaml):
  htf_bias_aligned    : +2  (D1+H4 bias aligned with trade direction)
  market_structure    : +2  (BOS or CHoCH confirms entry direction)
  ote_zone            : +2  (price in Fibonacci OTE 0.618-0.786)
  killzone_active     : +1  (London or NY session active)
  pdh_pdl_confluence  : +1  (price reacting at PDH or PDL level)

STRONG signal : score >= 6
MEDIUM signal : score >= 4
SKIP          : score <  4
"""

from __future__ import annotations
from dataclasses import dataclass
from enum import Enum

from hermes.market.structure import StructureResult, Bias, StructureEvent
from hermes.market.fibonacci import FibLevels
from hermes.market.levels import LevelsResult
from hermes.market.sessions import SessionResult


class SignalStrength(Enum):
    STRONG = "STRONG"
    MEDIUM = "MEDIUM"
    SKIP   = "SKIP"


@dataclass
class ConfluenceWeights:
    htf_bias_aligned:    int = 2
    market_structure:    int = 2
    ote_zone:            int = 2
    killzone_active:     int = 1
    pdh_pdl_confluence:  int = 1


@dataclass
class ConfluenceResult:
    score: int
    max_score: int
    strength: SignalStrength
    direction: str        # "long" | "short" | "none"
    breakdown: dict[str, int]
    reasons: list[str]


def score(
    structure: StructureResult,
    fib: FibLevels,
    levels: LevelsResult,
    session: SessionResult,
    current_price: float,
    weights: ConfluenceWeights | None = None,
    min_strong: int = 6,
    min_medium: int = 4,
) -> ConfluenceResult:
    """
    Calculate confluence score from all market analysis components.
    """
    w = weights or ConfluenceWeights()
    breakdown: dict[str, int] = {}
    reasons: list[str] = []
    total = 0
    direction = "none"

    # 1. HTF Bias
    if structure.bias == Bias.BULLISH:
        breakdown["htf_bias_aligned"] = w.htf_bias_aligned
        total += w.htf_bias_aligned
        reasons.append(f"HTF bias: BULLISH (+{w.htf_bias_aligned})")
        direction = "long"
    elif structure.bias == Bias.BEARISH:
        breakdown["htf_bias_aligned"] = w.htf_bias_aligned
        total += w.htf_bias_aligned
        reasons.append(f"HTF bias: BEARISH (+{w.htf_bias_aligned})")
        direction = "short"
    else:
        breakdown["htf_bias_aligned"] = 0
        reasons.append("HTF bias: NEUTRAL (+0)")

    # 2. Market Structure event
    struct_events = {StructureEvent.BOS_BULL, StructureEvent.BOS_BEAR,
                     StructureEvent.CHOCH_BULL, StructureEvent.CHOCH_BEAR}
    if structure.event in struct_events:
        breakdown["market_structure"] = w.market_structure
        total += w.market_structure
        reasons.append(f"Structure event: {structure.event.value} (+{w.market_structure})")
    else:
        breakdown["market_structure"] = 0
        reasons.append("No structure event (+0)")

    # 3. OTE zone
    if fib.in_ote(current_price):
        breakdown["ote_zone"] = w.ote_zone
        total += w.ote_zone
        reasons.append(f"Price in OTE zone {fib.ote_low:.5f}–{fib.ote_high:.5f} (+{w.ote_zone})")
    else:
        breakdown["ote_zone"] = 0
        reasons.append(f"Price NOT in OTE zone (+0)")

    # 4. Killzone
    if session.is_killzone:
        breakdown["killzone_active"] = w.killzone_active
        total += w.killzone_active
        reasons.append(f"Killzone active: {session.active_session} (+{w.killzone_active})")
    else:
        breakdown["killzone_active"] = 0
        reasons.append("No killzone active (+0)")

    # 5. PDH/PDL confluence
    if levels.confluence:
        breakdown["pdh_pdl_confluence"] = w.pdh_pdl_confluence
        total += w.pdh_pdl_confluence
        reasons.append(f"PDH/PDL confluence at {levels.pdh:.5f}/{levels.pdl:.5f} (+{w.pdh_pdl_confluence})")
    else:
        breakdown["pdh_pdl_confluence"] = 0
        reasons.append("No PDH/PDL confluence (+0)")

    max_score = sum(vars(w).values())

    if total >= min_strong:
        strength = SignalStrength.STRONG
    elif total >= min_medium:
        strength = SignalStrength.MEDIUM
    else:
        strength = SignalStrength.SKIP
        direction = "none"

    return ConfluenceResult(
        score=total,
        max_score=max_score,
        strength=strength,
        direction=direction,
        breakdown=breakdown,
        reasons=reasons,
    )
