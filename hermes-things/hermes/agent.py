"""
hermes.agent
------------
Hermes Things — main orchestrator agent.
Decides pipeline mode and routes to backtest, optimize, or live.
This is the "brain" of the agent loop.
"""

from __future__ import annotations
import yaml
from pathlib import Path
from dataclasses import dataclass

from hermes.data.fetcher import get_fetcher
from hermes.execution.live import LiveConfig, run_once, run_loop
from hermes.execution.backtest import run as backtest_run
from hermes.execution.optimizer import grid_search
from hermes.signal.confluence import ConfluenceWeights


CONFIG_PATH = Path(__file__).parent.parent / "config"


def _load_yaml(name: str) -> dict:
    with open(CONFIG_PATH / name) as f:
        return yaml.safe_load(f)


@dataclass
class AgentContext:
    mode: str        # "live" | "backtest" | "optimize" | "scan"
    pairs: list[str]
    config: dict
    pairs_config: dict


def build_context(mode: str, pairs: list[str] | None = None) -> AgentContext:
    cfg = _load_yaml("strategy.yaml")
    pairs_cfg = _load_yaml("pairs.yaml")

    if pairs is None:
        pairs = [p["symbol"] for p in pairs_cfg["pairs"]]

    return AgentContext(
        mode=mode,
        pairs=pairs,
        config=cfg,
        pairs_config={p["symbol"]: p for p in pairs_cfg["pairs"]},
    )


def _weights_from_config(cfg: dict) -> ConfluenceWeights:
    w = cfg.get("strategy", {}).get("confluence", {}).get("weights", {})
    return ConfluenceWeights(
        htf_bias_aligned=w.get("htf_bias_aligned", 2),
        market_structure=w.get("market_structure", 2),
        ote_zone=w.get("ote_zone", 2),
        killzone_active=w.get("killzone_active", 1),
        pdh_pdl_confluence=w.get("pdh_pdl_confluence", 1),
    )


def run(mode: str, pairs: list[str] | None = None, dry_run: bool = False) -> None:
    """
    Main agent entry point.
    mode: "live" | "backtest" | "optimize" | "scan"
    """
    ctx = build_context(mode, pairs)
    weights = _weights_from_config(ctx.config)
    strat = ctx.config.get("strategy", {})
    bt_cfg = ctx.config.get("backtest", {})
    optim_cfg = ctx.config.get("optimizer", {})

    sl_pips  = float(bt_cfg.get("default_sl_pips", 15))
    tp_ratio = float(bt_cfg.get("default_tp_ratio", 2.0))
    min_strong = int(strat.get("confluence", {}).get("min_score", 6))

    if dry_run:
        print(f"[dry-run] mode={mode} pairs={ctx.pairs}")
        print(f"  sl_pips={sl_pips} tp_ratio={tp_ratio} min_strong={min_strong}")
        print("  Config loaded OK. Exiting dry run.")
        return

    if mode == "scan":
        _run_scan(ctx, weights, sl_pips, tp_ratio, min_strong)

    elif mode == "live":
        live_cfg = LiveConfig(
            pairs=ctx.pairs,
            sl_pips=sl_pips,
            tp_ratio=tp_ratio,
            min_strong=min_strong,
        )
        run_loop(live_cfg, weights)

    elif mode == "backtest":
        _run_backtest(ctx, weights, sl_pips, tp_ratio, min_strong, bt_cfg)

    elif mode == "optimize":
        _run_optimize(ctx, weights, optim_cfg)

    else:
        raise ValueError(f"Unknown mode: {mode}. Use: live | backtest | optimize | scan")


def _run_scan(ctx: AgentContext, weights: ConfluenceWeights, sl: float, tp: float, ms: int) -> None:
    """Single scan pass — no loop."""
    live_cfg = LiveConfig(pairs=ctx.pairs, sl_pips=sl, tp_ratio=tp, min_strong=ms)
    signals = run_once(live_cfg, weights)
    if not signals:
        print("No signals found above threshold.")
    else:
        print(f"{len(signals)} signal(s) found.")


def _run_backtest(ctx: AgentContext, weights: ConfluenceWeights, sl: float, tp: float, ms: int, bt_cfg: dict) -> None:
    fetcher = get_fetcher("csv", data_dir="data/csv")
    for pair in ctx.pairs:
        pip = ctx.pairs_config.get(pair, {}).get("pip_size", 0.0001)
        try:
            htf_data       = fetcher.fetch(pair, "D",  200)
            structure_data = fetcher.fetch(pair, "60", 500)
            entry_data     = fetcher.fetch(pair, "15", 1000)

            result = backtest_run(
                symbol=pair,
                htf_data=htf_data,
                structure_data=structure_data,
                entry_data=entry_data,
                pip_size=pip,
                sl_pips=sl,
                tp_ratio=tp,
                weights=weights,
                min_strong=ms,
            )
            summary = result.summary()
            print(f"{pair}: {summary}")

        except FileNotFoundError as e:
            print(f"{pair}: no CSV data — {e}")


def _run_optimize(ctx: AgentContext, weights: ConfluenceWeights, optim_cfg: dict) -> None:
    fetcher = get_fetcher("csv", data_dir="data/csv")
    metric = optim_cfg.get("metric", "profit_factor")

    for pair in ctx.pairs:
        pip = ctx.pairs_config.get(pair, {}).get("pip_size", 0.0001)
        try:
            htf_data       = fetcher.fetch(pair, "D",  200)
            structure_data = fetcher.fetch(pair, "60", 500)
            entry_data     = fetcher.fetch(pair, "15", 1000)

            opt = grid_search(
                symbol=pair,
                htf_data=htf_data,
                structure_data=structure_data,
                entry_data=entry_data,
                pip_size=pip,
                metric=metric,
            )
            print(f"{pair}: best params={opt.best_params} | {metric}={opt.best_score:.2f}")

        except FileNotFoundError as e:
            print(f"{pair}: no CSV data — {e}")
