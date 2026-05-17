"""
hermes.execution.backtest
-------------------------
Backtesting engine for Hermes Things.
Walks through historical bars, detects signals on each bar,
and simulates trade outcomes.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime

from hermes.data.fetcher import OHLCVData, Bar
from hermes.signal.detector import Signal, detect
from hermes.signal.confluence import ConfluenceWeights


@dataclass
class Trade:
    symbol: str
    entry_time: datetime
    direction: str
    entry_price: float
    sl: float
    tp: float
    exit_time: datetime | None = None
    exit_price: float | None = None
    pnl_pips: float | None = None
    outcome: str | None = None  # "win" | "loss" | "be" | "open"


@dataclass
class BacktestResult:
    symbol: str
    trades: list[Trade] = field(default_factory=list)

    @property
    def total(self) -> int:
        return len(self.trades)

    @property
    def wins(self) -> int:
        return sum(1 for t in self.trades if t.outcome == "win")

    @property
    def losses(self) -> int:
        return sum(1 for t in self.trades if t.outcome == "loss")

    @property
    def win_rate(self) -> float:
        if not self.total:
            return 0.0
        return self.wins / self.total

    @property
    def total_pnl_pips(self) -> float:
        return sum(t.pnl_pips or 0.0 for t in self.trades)

    @property
    def profit_factor(self) -> float:
        gross_win  = sum(t.pnl_pips for t in self.trades if (t.pnl_pips or 0.0) > 0.0)  # type: ignore[misc]
        gross_loss = abs(sum(t.pnl_pips for t in self.trades if (t.pnl_pips or 0.0) < 0.0))  # type: ignore[misc]
        return gross_win / gross_loss if gross_loss else float("inf")

    def summary(self) -> dict:
        return {
            "symbol":        self.symbol,
            "total_trades":  self.total,
            "wins":          self.wins,
            "losses":        self.losses,
            "win_rate":      round(self.win_rate, 3),
            "total_pnl_pips": round(self.total_pnl_pips, 1),
            "profit_factor": round(self.profit_factor, 2),
        }


def _simulate_trade(
    trade: Trade,
    future_bars: list[Bar],
    pip_size: float,
) -> Trade:
    """Walk future bars to determine trade outcome via SL/TP hit."""
    for bar in future_bars:
        if trade.direction == "long":
            if bar.low <= trade.sl:
                trade.exit_time = bar.time
                trade.exit_price = trade.sl
                trade.pnl_pips = (trade.sl - trade.entry_price) / pip_size
                trade.outcome = "loss"
                break
            if bar.high >= trade.tp:
                trade.exit_time = bar.time
                trade.exit_price = trade.tp
                trade.pnl_pips = (trade.tp - trade.entry_price) / pip_size
                trade.outcome = "win"
                break
        elif trade.direction == "short":
            if bar.high >= trade.sl:
                trade.exit_time = bar.time
                trade.exit_price = trade.sl
                trade.pnl_pips = (trade.entry_price - trade.sl) / pip_size
                trade.outcome = "loss"
                break
            if bar.low <= trade.tp:
                trade.exit_time = bar.time
                trade.exit_price = trade.tp
                trade.pnl_pips = (trade.entry_price - trade.tp) / pip_size
                trade.outcome = "win"
                break
    else:
        trade.outcome = "open"
        trade.pnl_pips = 0.0

    return trade


def run(
    symbol: str,
    htf_data: OHLCVData,
    structure_data: OHLCVData,
    entry_data: OHLCVData,
    pip_size: float = 0.0001,
    sl_pips: float = 15.0,
    tp_ratio: float = 2.0,
    weights: ConfluenceWeights | None = None,
    min_strong: int = 6,
    lookback: int = 100,
) -> BacktestResult:
    """
    Walk entry_data bars from index `lookback` to end,
    run signal detection on each window, simulate trades.
    """
    result = BacktestResult(symbol=symbol)
    n = len(entry_data.bars)

    for i in range(lookback, n - 1):
        # Slice data up to bar i
        window = OHLCVData(
            symbol=entry_data.symbol,
            timeframe=entry_data.timeframe,
            bars=entry_data.bars[:i],
        )

        try:
            signal: Signal = detect(
                symbol=symbol,
                htf_data=htf_data,
                structure_data=structure_data,
                entry_data=window,
                pip_size=pip_size,
                sl_pips=sl_pips,
                tp_ratio=tp_ratio,
                weights=weights,
                min_strong=min_strong,
            )
        except Exception:
            continue

        if signal.strength == "SKIP" or signal.direction == "none":
            continue

        entry_price = (signal.entry_zone_low + signal.entry_zone_high) / 2.0
        trade = Trade(
            symbol=symbol,
            entry_time=entry_data.bars[i].time,
            direction=signal.direction,
            entry_price=entry_price,
            sl=signal.suggested_sl,
            tp=signal.suggested_tp,
        )

        future_bars = entry_data.bars[i + 1: i + 50]
        trade = _simulate_trade(trade, future_bars, pip_size)
        result.trades.append(trade)

    return result
