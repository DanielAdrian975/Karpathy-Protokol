"""
Hermes Things — CLI entry point
Usage:
  python main.py --mode=scan
  python main.py --mode=live
  python main.py --mode=backtest --pair=EURUSD
  python main.py --mode=optimize --pair=EURUSD
  python main.py --mode=scan --dry-run
"""

import argparse
from hermes.agent import run


def main() -> None:
    parser = argparse.ArgumentParser(description="Hermes Things — Chris Lori Strategy Orchestrator")
    parser.add_argument(
        "--mode",
        choices=["live", "backtest", "optimize", "scan"],
        default="scan",
        help="Pipeline mode (default: scan)",
    )
    parser.add_argument(
        "--pair",
        nargs="*",
        default=None,
        help="One or more forex pairs (default: all configured pairs)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Validate config and exit without running pipeline",
    )
    args = parser.parse_args()

    run(
        mode=args.mode,
        pairs=args.pair,
        dry_run=args.dry_run,
    )


if __name__ == "__main__":
    main()
