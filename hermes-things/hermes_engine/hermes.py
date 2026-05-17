"""
hermes_engine.hermes
--------------------
Hermes Agent configuration builder.
Generates system prompt, 6 tool definitions, and HermesAgentConfig.
"""

from __future__ import annotations
import json
from pathlib import Path
from hermes_engine.models import HermesAgentConfig, HermesToolCall

FOREX_MAJORS = ["EURUSD", "GBPUSD", "USDJPY", "USDCHF", "AUDUSD", "USDCAD", "NZDUSD"]

SYSTEM_PROMPT = """You are Hermes Things, an autonomous trading research agent implementing Chris Lori's ICT/Institutional methodology.

## Core Framework: TLS Confluence

Before any signal evaluation, check:
1. **T — Trend (HTF Bias)**: D1+H4 swing structure. HH+HL=bullish, LH+LL=bearish, conflict=neutral.
2. **L — Level (PDH/PDL + OTE)**: Price at Previous Day High/Low or in Fibonacci OTE zone (0.618-0.786).
3. **S — Signal (Structure Event)**: BOS (continuation) or CHoCH (reversal) on H1.

## Confluence Scoring

| Factor | Score |
|--------|-------|
| HTF bias aligned | +2 |
| Market structure event | +2 |
| OTE zone | +2 |
| Killzone active (London/NY) | +1 |
| PDH/PDL confluence | +1 |
| **TOTAL** | **8** |

- STRONG (>=6): Execute at full size
- MEDIUM (4-5): Execute at 50% size, require M15 confirmation
- SKIP (<4): No trade

## Risk Rules

- Max risk per trade: 1-2% of account
- Min SL: 10 pips from entry
- Min RR: 1.5 (default 2.0)
- Stop after 3 consecutive losses or -5% daily
- Forex majors only: EURUSD, GBPUSD, USDJPY, USDCHF, AUDUSD, USDCAD, NZDUSD
- Session filter: only trade London (02:00-05:00 EST) and NY (07:00-10:00 EST) killzones

## Output Format

All responses: [Source] -> [Finding] -> [Limitation/Uncertainty]
This is research output, not financial advice.

## Guardrails

- Never recommend specific position sizes in dollar terms
- Never guarantee profit or win rate
- Always label output as "research signal, not advice"
- If data is stale or insufficient -> output "Insufficient Evidence"
"""

TOOLS: list[dict] = [
    {
        "name": "detect_signal",
        "description": "Detect a trading signal from current market conditions using TLS confluence scoring.",
        "parameters": {
            "type": "object",
            "properties": {
                "symbol":          {"type": "string", "description": "Forex pair (e.g. EURUSD)"},
                "current_price":   {"type": "number", "description": "Current market price"},
                "htf_bias":        {"type": "string", "enum": ["bullish", "bearish", "neutral"]},
                "structure_event": {"type": "string", "enum": ["bos_bullish", "bos_bearish", "choch_bullish", "choch_bearish", "none"]},
                "in_ote_zone":     {"type": "boolean", "description": "Is price in Fibonacci 0.618-0.786 zone?"},
                "session":         {"type": "string", "enum": ["london", "new_york", "asian", "none"]},
                "pdh_pdl_conf":    {"type": "boolean", "description": "Is price reacting at PDH or PDL?"},
                "swing_high":      {"type": "number", "description": "Last significant swing high"},
                "swing_low":       {"type": "number", "description": "Last significant swing low"},
            },
            "required": ["symbol", "current_price", "htf_bias"],
        },
    },
    {
        "name": "validate_risk",
        "description": "Validate trade risk parameters against Chris Lori risk rules.",
        "parameters": {
            "type": "object",
            "properties": {
                "sl_pips":          {"type": "number", "description": "Stop loss in pips (min 10)"},
                "tp_ratio":         {"type": "number", "description": "Take profit RR ratio (min 1.5)"},
                "account_risk_pct": {"type": "number", "description": "Account risk percentage (max 2.0)"},
            },
            "required": ["sl_pips", "tp_ratio"],
        },
    },
    {
        "name": "get_strategies_by_category",
        "description": "Retrieve all strategies for a given category code.",
        "parameters": {
            "type": "object",
            "properties": {
                "category": {"type": "string", "enum": ["A", "B", "C", "D", "E", "F", "G"],
                             "description": "A=Structure B=Fibonacci C=Sessions D=PDH/PDL E=Confluence F=Bias G=Execution"},
            },
            "required": ["category"],
        },
    },
    {
        "name": "get_strategies_by_pattern",
        "description": "Search strategies by keyword (e.g. 'OTE', 'BOS', 'killzone', 'PDH').",
        "parameters": {
            "type": "object",
            "properties": {
                "keyword": {"type": "string", "description": "Search keyword"},
                "max_results": {"type": "integer", "default": 5},
            },
            "required": ["keyword"],
        },
    },
    {
        "name": "build_trade_setup",
        "description": "Build a complete validated trade setup (entry, SL, TP) from a detected signal.",
        "parameters": {
            "type": "object",
            "properties": {
                "symbol":       {"type": "string"},
                "direction":    {"type": "string", "enum": ["long", "short"]},
                "entry_low":    {"type": "number", "description": "OTE zone lower price"},
                "entry_high":   {"type": "number", "description": "OTE zone upper price"},
                "sl_pips":      {"type": "number", "default": 15},
                "tp_ratio":     {"type": "number", "default": 2.0},
                "pip_size":     {"type": "number", "default": 0.0001},
            },
            "required": ["symbol", "direction", "entry_low", "entry_high"],
        },
    },
    {
        "name": "get_routine",
        "description": "Get session-based trading routine: what to check at London open, NY open, or session close.",
        "parameters": {
            "type": "object",
            "properties": {
                "session": {"type": "string", "enum": ["london", "new_york", "pre_session", "post_session"]},
                "pairs":   {"type": "array", "items": {"type": "string"}, "description": "Pairs to scan"},
            },
            "required": ["session"],
        },
    },
]


def build_agent_config(strategy_count: int = 38) -> HermesAgentConfig:
    tools = [HermesToolCall(**t) for t in TOOLS]
    return HermesAgentConfig(
        system_prompt=SYSTEM_PROMPT,
        tools=tools,
        strategy_count=strategy_count,
        pairs=FOREX_MAJORS,
        guardrails=[
            "No specific dollar position sizing",
            "No guaranteed profit claims",
            "Label all output as research signal, not financial advice",
            "Insufficient Evidence if data stale or missing",
            "Forex majors only — no exotic pairs",
        ],
    )


def save_config(output_path: str | Path = "hermes_engine/hermes_config.json") -> None:
    config = build_agent_config()
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(config.model_dump(), f, indent=2, ensure_ascii=False)
    print(f"Hermes config saved: {path}")
