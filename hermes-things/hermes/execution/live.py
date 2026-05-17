"""
hermes.execution.live
---------------------
Live signal runner for Hermes Things.
Polls all configured forex pairs via TradingView MCP,
runs signal detection, and outputs active signals.
"""

from __future__ import annotations
import time
from dataclasses import dataclass
from datetime import datetime, timezone

from hermes.data.fetcher import get_fetcher, OHLCVData
from hermes.signal.detector import Signal, detect
from hermes.signal.confluence import ConfluenceWeights


@dataclass
class LiveConfig:
    pairs: list[str]
    htf_timeframe:       str   = "D"
    structure_timeframe: str   = "60"
    entry_timeframe:     str   = "15"
    htf_bars:            int   = 100
    structure_bars:      int   = 200
    entry_bars:          int   = 300
    pip_sizes:           dict  = None   # type: ignore[assignment]
    sl_pips:             float = 15.0
    tp_ratio:            float = 2.0
    min_strong:          int   = 6
    poll_interval_sec:   int   = 60

    def __post_init__(self) -> None:
        if self.pip_sizes is None:
            self.pip_sizes = {p: 0.0001 for p in self.pairs}
            for p in self.pairs:
                if "JPY" in p:
                    self.pip_sizes[p] = 0.01


def run_once(config: LiveConfig, weights: ConfluenceWeights | None = None) -> list[Signal]:
    """
    Single scan pass across all configured pairs.
    Returns list of non-SKIP signals.
    """
    fetcher = get_fetcher("live")
    signals: list[Signal] = []

    for pair in config.pairs:
        pip = config.pip_sizes.get(pair, 0.0001)
        try:
            htf_data       = fetcher.fetch(pair, config.htf_timeframe,       config.htf_bars)
            structure_data = fetcher.fetch(pair, config.structure_timeframe,  config.structure_bars)
            entry_data     = fetcher.fetch(pair, config.entry_timeframe,      config.entry_bars)

            sig = detect(
                symbol=pair,
                htf_data=htf_data,
                structure_data=structure_data,
                entry_data=entry_data,
                pip_size=pip,
                sl_pips=config.sl_pips,
                tp_ratio=config.tp_ratio,
                weights=weights,
                min_strong=config.min_strong,
            )

            if sig.strength != "SKIP":
                signals.append(sig)
                _print_signal(sig)

        except Exception as e:
            print(f"[{datetime.now(timezone.utc).isoformat()}] {pair}: error — {e}")

    return signals


def run_loop(config: LiveConfig, weights: ConfluenceWeights | None = None) -> None:
    """
    Continuous polling loop. Runs run_once every poll_interval_sec.
    Ctrl+C to stop.
    """
    print(f"Hermes Things — live mode | pairs: {config.pairs} | interval: {config.poll_interval_sec}s")
    while True:
        now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
        print(f"\n[{now}] Scanning {len(config.pairs)} pairs...")
        run_once(config, weights)
        time.sleep(config.poll_interval_sec)


def _print_signal(sig: Signal) -> None:
    print(
        f"  SIGNAL | {sig.symbol} | {sig.direction.upper()} | {sig.strength} | "
        f"score={sig.confluence.score}/{sig.confluence.max_score} | "
        f"entry={sig.entry_zone_low:.5f}–{sig.entry_zone_high:.5f} | "
        f"SL={sig.suggested_sl:.5f} | TP={sig.suggested_tp:.5f}"
    )
