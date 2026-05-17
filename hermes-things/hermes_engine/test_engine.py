"""
hermes_engine.test_engine
-------------------------
Test & validation suite for Hermes Engine.

Test 1: CSV loader - count, validity, category breakdown
Test 2: Signal detection - TLS scoring, recommendation
Test 3: Risk validation - RR, position sizing
Test 4: Trade setup builder - TLS + risk + strategy
Test 5: Hermes config generation - 6 tools, prompt, save JSON

Run: python hermes_engine/test_engine.py
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from hermes_engine import loader, engine
from hermes_engine.models import (
    MarketCondition, BiasDirection, StructureEvent, SessionName,
    RiskParams, SignalStrength, TradeDirection,
)
from hermes_engine.hermes import build_agent_config, save_config


CSV_PATH = os.path.join(os.path.dirname(__file__), "..", "STRATEGY_DATABASE.csv")
PASS = "PASS"
FAIL = "FAIL"


def test_csv_loader() -> bool:
    print("\n[TEST 1] CSV Loader")
    strategies = loader.load(CSV_PATH)
    s = loader.summary(strategies)
    print(f"  Total strategies: {s['total_strategies']}")
    print(f"  Articles: {s['articles']}")
    print(f"  Categories: {s['categories']}")

    ok = s["total_strategies"] >= 30
    print(f"  -> {PASS if ok else FAIL}: >= 30 strategies loaded")

    cat_f = loader.get_by_category(strategies, "F")
    ok2 = len(cat_f) >= 4
    print(f"  -> {PASS if ok2 else FAIL}: Category F has >= 4 strategies ({len(cat_f)} found)")

    return ok and ok2


def test_signal_detection() -> bool:
    print("\n[TEST 2] Signal Detection")
    strategies = loader.load(CSV_PATH)

    # Full confluence: all factors present
    cond_strong = MarketCondition(
        symbol="EURUSD",
        current_price=1.0950,
        htf_bias=BiasDirection.bullish,
        structure_event=StructureEvent.bos_bull,
        in_ote_zone=True,
        session=SessionName.london,
        pdh_pdl_conf=True,
        swing_high=1.1050,
        swing_low=1.0900,
    )
    sig = engine.detect(cond_strong, strategies)
    print(f"  STRONG test: score={sig.tls.score}/{sig.tls.max_score} strength={sig.tls.strength.value}")
    ok1 = sig.tls.strength == SignalStrength.STRONG and sig.direction == TradeDirection.long
    print(f"  -> {PASS if ok1 else FAIL}: STRONG LONG signal detected")

    # Neutral bias: should SKIP
    cond_skip = MarketCondition(
        symbol="GBPUSD",
        current_price=1.2700,
        htf_bias=BiasDirection.neutral,
        structure_event=StructureEvent.none,
        in_ote_zone=False,
        session=SessionName.none,
        pdh_pdl_conf=False,
    )
    sig2 = engine.detect(cond_skip, strategies)
    ok2 = sig2.tls.strength == SignalStrength.SKIP
    print(f"  -> {PASS if ok2 else FAIL}: Neutral bias -> SKIP (score={sig2.tls.score})")

    # TLS recommendation text
    ok3 = "ENTRY" in sig.tls.recommendation
    print(f"  -> {PASS if ok3 else FAIL}: Recommendation contains ENTRY")

    return ok1 and ok2 and ok3


def test_risk_validation() -> bool:
    print("\n[TEST 3] Risk Validation")
    # Valid params
    try:
        r = RiskParams(sl_pips=15.0, tp_ratio=2.0, account_risk_pct=1.0)
        ok1 = r.is_valid
        print(f"  -> {PASS if ok1 else FAIL}: Valid params accepted (sl=15, tp=2.0, risk=1%)")
    except Exception as e:
        print(f"  -> {FAIL}: Unexpected error: {e}")
        ok1 = False

    # Invalid SL < 10 pips
    try:
        RiskParams(sl_pips=5.0, tp_ratio=2.0)
        ok2 = False
        print(f"  -> {FAIL}: SL < 10 should have raised error")
    except Exception:
        ok2 = True
        print(f"  -> {PASS}: SL < 10 correctly rejected")

    # Invalid TP ratio < 1.5
    try:
        RiskParams(sl_pips=15.0, tp_ratio=1.0)
        ok3 = False
        print(f"  -> {FAIL}: TP < 1.5 should have raised error")
    except Exception:
        ok3 = True
        print(f"  -> {PASS}: TP ratio < 1.5 correctly rejected")

    return ok1 and ok2 and ok3


def test_trade_setup() -> bool:
    print("\n[TEST 4] Trade Setup Builder")
    strategies = loader.load(CSV_PATH)

    cond = MarketCondition(
        symbol="EURUSD",
        current_price=1.0950,
        htf_bias=BiasDirection.bullish,
        structure_event=StructureEvent.bos_bull,
        in_ote_zone=True,
        session=SessionName.new_york,
        pdh_pdl_conf=True,
        swing_high=1.1050,
        swing_low=1.0900,
    )
    sig = engine.detect(cond, strategies)
    setup = engine.build_trade_setup(sig, sl_pips=15, tp_ratio=2.0, pip_size=0.0001)

    ok1 = setup.sl_pips >= 10
    ok2 = setup.rr_ratio >= 1.5
    ok3 = len(sig.matched_strategies) > 0

    print(f"  entry={setup.entry_price:.5f}  SL={setup.sl_price:.5f}  TP={setup.tp_price:.5f}")
    print(f"  sl_pips={setup.sl_pips:.1f}  rr={setup.rr_ratio:.2f}  matched={len(sig.matched_strategies)} strategies")
    print(f"  -> {PASS if ok1 else FAIL}: SL >= 10 pips")
    print(f"  -> {PASS if ok2 else FAIL}: RR >= 1.5")
    print(f"  -> {PASS if ok3 else FAIL}: Strategies matched")

    return ok1 and ok2 and ok3


def test_hermes_config() -> bool:
    print("\n[TEST 5] Hermes Agent Config")
    config = build_agent_config(strategy_count=38)

    ok1 = len(config.tools) == 6
    ok2 = len(config.system_prompt) > 100
    ok3 = len(config.pairs) == 7
    ok4 = "EURUSD" in config.pairs

    print(f"  tools={len(config.tools)}  pairs={len(config.pairs)}  prompt_len={len(config.system_prompt)}")
    print(f"  -> {PASS if ok1 else FAIL}: 6 tools defined")
    print(f"  -> {PASS if ok2 else FAIL}: System prompt non-empty")
    print(f"  -> {PASS if ok3 else FAIL}: 7 forex majors configured")

    # Save config JSON
    config_path = os.path.join(os.path.dirname(__file__), "hermes_config.json")
    try:
        save_config(config_path)
        ok5 = os.path.exists(config_path)
        print(f"  -> {PASS if ok5 else FAIL}: Config JSON saved to {config_path}")
    except Exception as e:
        ok5 = False
        print(f"  -> {FAIL}: Save failed: {e}")

    return ok1 and ok2 and ok3 and ok4 and ok5


if __name__ == "__main__":
    results = [
        test_csv_loader(),
        test_signal_detection(),
        test_risk_validation(),
        test_trade_setup(),
        test_hermes_config(),
    ]
    passed = sum(results)
    total  = len(results)
    print(f"\n{'='*50}")
    print(f"Results: {passed}/{total} test groups passed")
    print(f"{'='*50}")
    if passed < total:
        sys.exit(1)
