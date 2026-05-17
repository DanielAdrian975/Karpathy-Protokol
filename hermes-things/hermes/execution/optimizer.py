"""
hermes.execution.optimizer
--------------------------
Grid-search optimizer for Hermes Things strategy parameters.
Iterates over sl_pips, tp_ratio, min_strong combinations and
reports the best configuration by selected metric.
"""

from __future__ import annotations
from dataclasses import dataclass
from itertools import product

from hermes.data.fetcher import OHLCVData
from hermes.execution.backtest import run as backtest_run, BacktestResult


@dataclass
class OptimizeResult:
    best_params: dict
    best_score: float
    metric: str
    all_results: list[dict]


def grid_search(
    symbol: str,
    htf_data: OHLCVData,
    structure_data: OHLCVData,
    entry_data: OHLCVData,
    pip_size: float = 0.0001,
    metric: str = "profit_factor",  # "profit_factor" | "win_rate" | "total_pnl_pips"
    sl_pips_range:   list[float] | None = None,
    tp_ratio_range:  list[float] | None = None,
    min_strong_range: list[int]  | None = None,
) -> OptimizeResult:
    """
    Grid search over strategy parameters.
    Returns best parameter set by chosen metric.
    """
    if sl_pips_range is None:
        sl_pips_range = [10.0, 15.0, 20.0]
    if tp_ratio_range is None:
        tp_ratio_range = [1.5, 2.0, 2.5, 3.0]
    if min_strong_range is None:
        min_strong_range = [5, 6, 7]

    all_results: list[dict] = []
    best_score = float("-inf")
    best_params: dict = {}

    for sl, tp, ms in product(sl_pips_range, tp_ratio_range, min_strong_range):
        try:
            result: BacktestResult = backtest_run(
                symbol=symbol,
                htf_data=htf_data,
                structure_data=structure_data,
                entry_data=entry_data,
                pip_size=pip_size,
                sl_pips=sl,
                tp_ratio=tp,
                min_strong=ms,
            )
        except Exception:
            continue

        summary = result.summary()
        score = float(summary.get(metric, 0))

        params = {"sl_pips": sl, "tp_ratio": tp, "min_strong": ms}
        all_results.append({**params, **summary, "score": score})

        if score > best_score:
            best_score = score
            best_params = params

    all_results.sort(key=lambda r: r["score"], reverse=True)

    return OptimizeResult(
        best_params=best_params,
        best_score=best_score,
        metric=metric,
        all_results=all_results,
    )
