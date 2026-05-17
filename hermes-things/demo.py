"""
Hermes Things — Pipeline Demo
Jalankan full pipeline dengan mock data untuk semua 7 forex majors.
Menunjukkan: signal detection, backtest summary, dan optimizer output.

Usage: python demo.py
"""

from __future__ import annotations
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

# Force UTF-8 on Windows console
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")  # type: ignore[union-attr]

from hermes.data.mock import make_forex_dataset
from hermes.signal.detector import detect
from hermes.execution.backtest import run as backtest_run
from hermes.execution.optimizer import grid_search
from hermes.signal.confluence import ConfluenceWeights

PAIRS = [
    ("EURUSD", "bullish",  0.0001, 42),
    ("GBPUSD", "bullish",  0.0001, 77),
    ("USDJPY", "bearish",  0.01,   55),
    ("USDCHF", "ranging",  0.0001, 33),
    ("AUDUSD", "bullish",  0.0001, 88),
    ("USDCAD", "bearish",  0.0001, 21),
    ("NZDUSD", "ranging",  0.0001, 66),
]


def run_signal_scan() -> None:
    print("\n" + "="*60)
    print("HERMES THINGS — SIGNAL SCAN (mock data)")
    print("="*60)
    weights = ConfluenceWeights()

    for symbol, trend, pip, seed in PAIRS:
        ds = make_forex_dataset(symbol, trend, seed)
        try:
            sig = detect(
                symbol=symbol,
                htf_data=ds["D"],
                structure_data=ds["60"],
                entry_data=ds["15"],
                pip_size=pip,
            )
            bar = "#" * sig.confluence.score + "." * (sig.confluence.max_score - sig.confluence.score)
            print(
                f"  {symbol:<8} | {sig.direction.upper():<5} | {sig.strength:<6} "
                f"| [{bar}] {sig.confluence.score}/{sig.confluence.max_score} "
                f"| entry {sig.entry_zone_low:.4f}-{sig.entry_zone_high:.4f}"
            )
        except Exception as e:
            print(f"  {symbol:<8} | ERROR: {e}")


def run_backtest_report() -> None:
    print("\n" + "="*60)
    print("HERMES THINGS — BACKTEST REPORT (mock data)")
    print("="*60)
    print(f"  {'Symbol':<8} {'Trades':>7} {'Wins':>6} {'WR%':>7} {'PnL(p)':>9} {'PF':>7}")
    print("  " + "-"*52)

    for symbol, trend, pip, seed in PAIRS:
        ds = make_forex_dataset(symbol, trend, seed)
        try:
            result = backtest_run(
                symbol=symbol,
                htf_data=ds["D"],
                structure_data=ds["60"],
                entry_data=ds["15"],
                pip_size=pip,
                sl_pips=15,
                tp_ratio=2.0,
                min_strong=6,
                lookback=50,
            )
            s = result.summary()
            print(
                f"  {symbol:<8} {s['total_trades']:>7} {s['wins']:>6} "
                f"{s['win_rate']*100:>6.1f}% {s['total_pnl_pips']:>9.1f} "
                f"{s['profit_factor']:>7.2f}"
            )
        except Exception as e:
            print(f"  {symbol:<8} | ERROR: {e}")


def run_optimizer_best() -> None:
    print("\n" + "="*60)
    print("HERMES THINGS — OPTIMIZER TOP PARAMS (mock, profit_factor)")
    print("="*60)

    symbol, trend, pip, seed = PAIRS[0]  # Demo on EURUSD only
    ds = make_forex_dataset(symbol, trend, seed)
    print(f"  Running grid search on {symbol}...")
    opt = grid_search(
        symbol=symbol,
        htf_data=ds["D"],
        structure_data=ds["60"],
        entry_data=ds["15"],
        pip_size=pip,
        metric="profit_factor",
        sl_pips_range=[10.0, 15.0, 20.0],
        tp_ratio_range=[1.5, 2.0, 2.5],
        min_strong_range=[5, 6],
    )
    print(f"\n  Best params: {opt.best_params}")
    print(f"  Best profit_factor: {opt.best_score:.2f}")
    print(f"\n  Top 5 combinations:")
    for r in opt.all_results[:5]:
        print(
            f"    sl={r['sl_pips']:4.0f}p  tp={r['tp_ratio']:.1f}x  "
            f"ms={r['min_strong']}  => "
            f"trades={r['total_trades']}  wr={r['win_rate']*100:.0f}%  "
            f"pf={r['profit_factor']:.2f}"
        )


if __name__ == "__main__":
    run_signal_scan()
    run_backtest_report()
    run_optimizer_best()
    print("\n[research only — not financial advice]\n")
