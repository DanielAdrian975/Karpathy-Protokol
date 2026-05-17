"""
hermes.data.mcp_bridge
----------------------
TradingView MCP bridge for Hermes Things.

When running inside Claude Code (with MCP server active), this module
provides a ClaudeCodeBridge that receives pre-fetched bar data injected
by the orchestrating Claude Code session.

When running standalone, use TVMCPHTTPFetcher with a local MCP HTTP proxy,
or fall back to CSVFetcher.

Usage pattern (from Claude Code session):
    bars = mcp_tool("data_get_ohlcv", symbol="EURUSD", timeframe="60", count=200)
    fetcher = ClaudeCodeBridge()
    fetcher.inject("EURUSD", "60", bars_payload)
    data = fetcher.fetch("EURUSD", "60")
"""

from __future__ import annotations
from datetime import datetime, timezone
from hermes.data.fetcher import OHLCVData, Bar


class ClaudeCodeBridge:
    """
    In-memory bridge: Claude Code calls MCP tools, parses results,
    and injects OHLCVData into this fetcher for hermes to consume.
    """

    def __init__(self) -> None:
        self._store: dict[str, OHLCVData] = {}

    def inject(self, symbol: str, timeframe: str, raw_bars: list[dict]) -> None:
        """
        Inject bar data from a TradingView MCP data_get_ohlcv result.
        raw_bars: list of dicts with keys: time, open, high, low, close, volume
        """
        data = OHLCVData(symbol=symbol, timeframe=timeframe)
        for b in raw_bars:
            t = b.get("time", "")
            if isinstance(t, (int, float)):
                dt = datetime.fromtimestamp(t, tz=timezone.utc)
            else:
                dt = datetime.fromisoformat(str(t).replace("Z", "+00:00"))
            data.bars.append(Bar(
                time=dt,
                open=float(b["open"]),
                high=float(b["high"]),
                low=float(b["low"]),
                close=float(b["close"]),
                volume=float(b.get("volume", 0)),
            ))
        key = f"{symbol}_{timeframe}"
        self._store[key] = data

    def fetch(self, symbol: str, timeframe: str, bars: int = 200) -> OHLCVData:
        key = f"{symbol}_{timeframe}"
        if key not in self._store:
            raise KeyError(
                f"No data injected for {symbol} {timeframe}. "
                "Call inject() first with MCP bar data."
            )
        data = self._store[key]
        if bars < len(data.bars):
            trimmed = OHLCVData(symbol=data.symbol, timeframe=data.timeframe)
            trimmed.bars = data.bars[-bars:]
            return trimmed
        return data

    def available(self) -> list[str]:
        return list(self._store.keys())


class TVMCPHTTPFetcher:
    """
    Fetches OHLCV via a local MCP HTTP proxy server.
    Start the proxy with: mcp-proxy --port 8765
    Then set HERMES_MCP_URL=http://localhost:8765
    """

    def __init__(self, base_url: str = "http://localhost:8765") -> None:
        self.base_url = base_url

    def fetch(self, symbol: str, timeframe: str, bars: int = 200) -> OHLCVData:
        import urllib.request, json
        payload = json.dumps({
            "tool": "data_get_ohlcv",
            "params": {"symbol": symbol, "timeframe": timeframe, "count": bars, "summary": False},
        }).encode()
        req = urllib.request.Request(
            f"{self.base_url}/call",
            data=payload,
            headers={"Content-Type": "application/json"},
        )
        with urllib.request.urlopen(req, timeout=10) as resp:
            result = json.loads(resp.read())

        data = OHLCVData(symbol=symbol, timeframe=timeframe)
        bridge = ClaudeCodeBridge()
        bridge.inject(symbol, timeframe, result.get("bars", []))
        return bridge.fetch(symbol, timeframe)
