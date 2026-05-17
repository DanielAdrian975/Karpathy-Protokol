"""
hermes.data.fetcher
-------------------
OHLCV data fetcher. Primary source: TradingView MCP.
Fallback: CSV files for backtesting.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional
import json
import subprocess


@dataclass
class Bar:
    time: datetime
    open: float
    high: float
    low: float
    close: float
    volume: float


@dataclass
class OHLCVData:
    symbol: str
    timeframe: str
    bars: list[Bar] = field(default_factory=list)

    @property
    def closes(self) -> list[float]:
        return [b.close for b in self.bars]

    @property
    def highs(self) -> list[float]:
        return [b.high for b in self.bars]

    @property
    def lows(self) -> list[float]:
        return [b.low for b in self.bars]

    @property
    def opens(self) -> list[float]:
        return [b.open for b in self.bars]


class TVMCPFetcher:
    """
    Fetches OHLCV data via TradingView MCP tool calls.
    Requires TradingView MCP server running.
    """

    def fetch(self, symbol: str, timeframe: str, bars: int = 200) -> OHLCVData:
        """
        Call data_get_ohlcv via MCP. Always uses summary=False internally
        to get individual bars for analysis.
        """
        result = self._call_mcp("data_get_ohlcv", {
            "symbol": symbol,
            "timeframe": timeframe,
            "count": bars,
            "summary": False,
        })
        return self._parse(symbol, timeframe, result)

    def _call_mcp(self, tool: str, params: dict) -> dict:
        # In production: called via MCP bridge.
        # In test/backtest: returns mock data or raises.
        raise NotImplementedError(
            "TVMCPFetcher._call_mcp must be wired to MCP server. "
            "Use CSVFetcher for backtesting without live MCP."
        )

    def _parse(self, symbol: str, timeframe: str, raw: dict) -> OHLCVData:
        data = OHLCVData(symbol=symbol, timeframe=timeframe)
        for item in raw.get("bars", []):
            data.bars.append(Bar(
                time=datetime.fromisoformat(item["time"]),
                open=float(item["open"]),
                high=float(item["high"]),
                low=float(item["low"]),
                close=float(item["close"]),
                volume=float(item.get("volume", 0)),
            ))
        return data


class CSVFetcher:
    """
    Loads OHLCV from CSV for backtesting.
    Expected columns: time,open,high,low,close,volume
    """

    def __init__(self, data_dir: str):
        self.data_dir = data_dir

    def fetch(self, symbol: str, timeframe: str, bars: int = 500) -> OHLCVData:
        import csv, os
        path = os.path.join(self.data_dir, f"{symbol}_{timeframe}.csv")
        if not os.path.exists(path):
            raise FileNotFoundError(f"No CSV data for {symbol} {timeframe} at {path}")

        data = OHLCVData(symbol=symbol, timeframe=timeframe)
        with open(path, newline="") as f:
            reader = csv.DictReader(f)
            rows = list(reader)[-bars:]
            for row in rows:
                data.bars.append(Bar(
                    time=datetime.fromisoformat(row["time"]),
                    open=float(row["open"]),
                    high=float(row["high"]),
                    low=float(row["low"]),
                    close=float(row["close"]),
                    volume=float(row.get("volume", 0)),
                ))
        return data


def get_fetcher(mode: str = "live", data_dir: str = "data/csv") -> TVMCPFetcher | CSVFetcher:
    if mode == "live":
        return TVMCPFetcher()
    return CSVFetcher(data_dir)
