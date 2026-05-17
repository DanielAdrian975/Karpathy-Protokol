"""
hermes_engine.engine
--------------------
Signal detection engine. Evaluates MarketCondition against
the full Chris Lori confluence framework and returns SignalDetection.
"""

from __future__ import annotations
from hermes_engine.models import (
    MarketCondition, TLSConfluence, SignalDetection, TradeSetup,
    RiskParams, BiasDirection, StructureEvent, SessionName, TradeDirection,
    Strategy, SignalStrength,
)


# Keyword → category mapping for strategy matching
PATTERN_KEYWORDS: dict[str, list[str]] = {
    "htf_bias":    ["bias", "htf", "bullish", "bearish", "hh", "hl", "lh", "ll"],
    "structure":   ["bos", "choch", "break of structure", "change of character", "swing"],
    "ote":         ["ote", "fibonacci", "0.618", "0.786", "optimal trade entry"],
    "session":     ["london", "new york", "killzone", "session", "est"],
    "pdh_pdl":     ["pdh", "pdl", "previous day", "magnet"],
    "execution":   ["sl", "tp", "stop loss", "take profit", "position", "risk"],
    "pipeline":    ["backtest", "optimize", "live", "scan", "pipeline"],
}


def evaluate_tls(condition: MarketCondition) -> TLSConfluence:
    """Evaluate TLS confluence from a MarketCondition."""
    bias_score = 2 if condition.htf_bias != BiasDirection.neutral else 0

    struct_events = {
        StructureEvent.bos_bull, StructureEvent.bos_bear,
        StructureEvent.choch_bull, StructureEvent.choch_bear,
    }
    structure_score = 2 if condition.structure_event in struct_events else 0

    ote_score = 2 if condition.in_ote_zone else 0

    killzone_score = 1 if condition.session in (SessionName.london, SessionName.new_york) else 0

    pdh_pdl_score = 1 if condition.pdh_pdl_conf else 0

    return TLSConfluence(
        bias_score=bias_score,
        structure_score=structure_score,
        ote_score=ote_score,
        killzone_score=killzone_score,
        pdh_pdl_score=pdh_pdl_score,
    )


def _direction_from_condition(condition: MarketCondition) -> TradeDirection:
    if condition.htf_bias == BiasDirection.bullish:
        return TradeDirection.long
    if condition.htf_bias == BiasDirection.bearish:
        return TradeDirection.short
    return TradeDirection.none


def match_strategies(condition: MarketCondition, strategies: list[Strategy]) -> list[str]:
    """Return strategy_ids relevant to current market condition."""
    matched: list[str] = []
    query_terms: set[str] = set()

    if condition.htf_bias != BiasDirection.neutral:
        query_terms.update(PATTERN_KEYWORDS["htf_bias"])
    if condition.structure_event != StructureEvent.none:
        query_terms.update(PATTERN_KEYWORDS["structure"])
    if condition.in_ote_zone:
        query_terms.update(PATTERN_KEYWORDS["ote"])
    if condition.session != SessionName.none:
        query_terms.update(PATTERN_KEYWORDS["session"])
    if condition.pdh_pdl_conf:
        query_terms.update(PATTERN_KEYWORDS["pdh_pdl"])

    for s in strategies:
        rules_lower = s.rules.lower()
        if any(term in rules_lower for term in query_terms):
            matched.append(s.strategy_id)

    return matched


def detect(
    condition: MarketCondition,
    strategies: list[Strategy],
    swing_high: float = 0.0,
    swing_low: float = 0.0,
) -> SignalDetection:
    """Full signal detection: TLS evaluation + strategy matching."""
    tls = evaluate_tls(condition)
    direction = _direction_from_condition(condition)

    if tls.strength == SignalStrength.SKIP:
        direction = TradeDirection.none

    matched = match_strategies(condition, strategies)

    # Entry zone: use swing-based OTE if available, else price
    if swing_high > swing_low > 0:
        rng = swing_high - swing_low
        if direction == TradeDirection.long:
            entry_low  = swing_high - 0.786 * rng
            entry_high = swing_high - 0.618 * rng
        elif direction == TradeDirection.short:
            entry_low  = swing_low + 0.618 * rng
            entry_high = swing_low + 0.786 * rng
        else:
            entry_low = entry_high = condition.current_price
    else:
        entry_low = entry_high = condition.current_price

    reasoning = [
        f"HTF bias: {condition.htf_bias.value} ({tls.bias_score}/2)",
        f"Structure: {condition.structure_event.value} ({tls.structure_score}/2)",
        f"OTE zone: {condition.in_ote_zone} ({tls.ote_score}/2)",
        f"Session: {condition.session.value} ({tls.killzone_score}/1)",
        f"PDH/PDL: {condition.pdh_pdl_conf} ({tls.pdh_pdl_score}/1)",
        f"Score: {tls.score}/{tls.max_score} -> {tls.strength.value}",
    ]

    return SignalDetection(
        symbol=condition.symbol,
        direction=direction,
        tls=tls,
        matched_strategies=matched,
        entry_zone_low=round(entry_low, 5),
        entry_zone_high=round(entry_high, 5),
        reasoning=reasoning,
    )


def build_trade_setup(
    signal: SignalDetection,
    sl_pips: float = 15.0,
    tp_ratio: float = 2.0,
    pip_size: float = 0.0001,
    account_risk_pct: float = 1.0,
) -> TradeSetup:
    """Build complete validated trade setup from a signal."""
    risk = RiskParams(sl_pips=sl_pips, tp_ratio=tp_ratio, account_risk_pct=account_risk_pct)
    entry = (signal.entry_zone_low + signal.entry_zone_high) / 2.0
    sl_delta = sl_pips * pip_size

    if signal.direction == TradeDirection.long:
        sl_price = entry - sl_delta
        tp_price = entry + sl_delta * tp_ratio
    elif signal.direction == TradeDirection.short:
        sl_price = entry + sl_delta
        tp_price = entry - sl_delta * tp_ratio
    else:
        sl_price = tp_price = entry

    return TradeSetup(
        signal=signal,
        risk=risk,
        entry_price=round(entry, 5),
        sl_price=round(sl_price, 5),
        tp_price=round(tp_price, 5),
        pip_size=pip_size,
        notes=[f"Confluence: {signal.tls.strength.value}", signal.tls.recommendation],
    )
