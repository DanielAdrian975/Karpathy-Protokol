"""
hermes_engine.models
--------------------
Pydantic models for Hermes Things strategy engine.
Covers: strategies, categories, entities, signals, risk, and agent config.
"""

from __future__ import annotations
from enum import Enum
from typing import Any
from pydantic import BaseModel, field_validator, model_validator


# ── Enums ────────────────────────────────────────────────────────────────────

class CategoryCode(str, Enum):
    A = "A"  # Market Structure
    B = "B"  # Fibonacci / OTE
    C = "C"  # Session Killzones
    D = "D"  # PDH/PDL Levels
    E = "E"  # Confluence Scoring
    F = "F"  # HTF Bias
    G = "G"  # Trade Execution & Pipeline


CATEGORY_NAMES: dict[str, str] = {
    "A": "Market Structure",
    "B": "Fibonacci OTE",
    "C": "Session Killzones",
    "D": "PDH PDL Levels",
    "E": "Confluence Scoring",
    "F": "HTF Bias",
    "G": "Trade Execution Pipeline",
}


class EntityType(str, Enum):
    pattern    = "pattern"
    level      = "level"
    indicator  = "indicator"
    risk       = "risk"
    framework  = "framework"
    execution  = "execution"
    routine    = "routine"
    entry      = "entry"


class BiasDirection(str, Enum):
    bullish = "bullish"
    bearish = "bearish"
    neutral = "neutral"


class StructureEvent(str, Enum):
    bos_bull   = "bos_bullish"
    bos_bear   = "bos_bearish"
    choch_bull = "choch_bullish"
    choch_bear = "choch_bearish"
    none       = "none"


class SignalStrength(str, Enum):
    STRONG = "STRONG"
    MEDIUM = "MEDIUM"
    SKIP   = "SKIP"


class TradeDirection(str, Enum):
    long  = "long"
    short = "short"
    none  = "none"


class SessionName(str, Enum):
    london   = "london"
    new_york = "new_york"
    asian    = "asian"
    none     = "none"


# ── Core Strategy Models ──────────────────────────────────────────────────────

class Strategy(BaseModel):
    model_config = {"frozen": True}

    article_id:    int
    article_title: str
    strategy_no:   int
    strategy_name: str
    rules:         str
    category:      CategoryCode
    duplicate_group: int

    @property
    def strategy_id(self) -> str:
        return f"{self.article_id}-{self.strategy_no}"

    @property
    def rule_list(self) -> list[str]:
        return [r.strip() for r in self.rules.split(";") if r.strip()]

    @field_validator("article_id")
    @classmethod
    def validate_article_id(cls, v: int) -> int:
        if v < 1:
            raise ValueError("article_id must be >= 1")
        return v

    @field_validator("strategy_no")
    @classmethod
    def validate_strategy_no(cls, v: int) -> int:
        if v < 1:
            raise ValueError("strategy_no must be >= 1")
        return v

    @field_validator("rules")
    @classmethod
    def validate_rules(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("rules must not be empty")
        return v


class Article(BaseModel):
    model_config = {"frozen": True}

    article_id:    int
    title:         str
    strategies:    list[Strategy]

    @property
    def strategy_count(self) -> int:
        return len(self.strategies)

    @property
    def categories(self) -> list[str]:
        return list({s.category.value for s in self.strategies})


class Category(BaseModel):
    model_config = {"frozen": True}

    code:        CategoryCode
    name:        str
    strategies:  list[Strategy]
    description: str = ""

    @property
    def strategy_count(self) -> int:
        return len(self.strategies)


class Entity(BaseModel):
    model_config = {"frozen": True}

    entity_id:   str
    name:        str
    entity_type: EntityType
    category:    CategoryCode
    related:     list[str] = []
    description: str = ""


# ── Market Condition Models ───────────────────────────────────────────────────

class MarketCondition(BaseModel):
    """Input for signal detection."""
    symbol:          str
    current_price:   float
    htf_bias:        BiasDirection
    structure_event: StructureEvent  = StructureEvent.none
    in_ote_zone:     bool            = False
    session:         SessionName     = SessionName.none
    pdh_pdl_conf:    bool            = False
    swing_high:      float           = 0.0
    swing_low:       float           = 0.0

    @field_validator("current_price", "swing_high", "swing_low")
    @classmethod
    def validate_prices(cls, v: float) -> float:
        if v < 0:
            raise ValueError("Price values must be non-negative")
        return v


class TLSConfluence(BaseModel):
    """Trend + Level + Signal scoring."""
    bias_score:      int = 0   # 0 or 2
    structure_score: int = 0   # 0 or 2
    ote_score:       int = 0   # 0 or 2
    killzone_score:  int = 0   # 0 or 1
    pdh_pdl_score:   int = 0   # 0 or 1

    @property
    def score(self) -> int:
        return self.bias_score + self.structure_score + self.ote_score + self.killzone_score + self.pdh_pdl_score

    @property
    def max_score(self) -> int:
        return 8

    @property
    def strength(self) -> SignalStrength:
        if self.score >= 6:
            return SignalStrength.STRONG
        if self.score >= 4:
            return SignalStrength.MEDIUM
        return SignalStrength.SKIP

    @property
    def recommendation(self) -> str:
        s = self.strength
        if s == SignalStrength.STRONG:
            return "ENTRY — full position size"
        if s == SignalStrength.MEDIUM:
            return "ENTRY — 50% size, require M15 confirmation"
        return "SKIP — insufficient confluence"

    @model_validator(mode="after")
    def validate_scores(self) -> "TLSConfluence":
        if self.bias_score not in (0, 2):
            raise ValueError("bias_score must be 0 or 2")
        if self.structure_score not in (0, 2):
            raise ValueError("structure_score must be 0 or 2")
        if self.ote_score not in (0, 2):
            raise ValueError("ote_score must be 0 or 2")
        if self.killzone_score not in (0, 1):
            raise ValueError("killzone_score must be 0 or 1")
        if self.pdh_pdl_score not in (0, 1):
            raise ValueError("pdh_pdl_score must be 0 or 1")
        return self


class SignalDetection(BaseModel):
    """Complete signal detection result."""
    symbol:            str
    direction:         TradeDirection
    tls:               TLSConfluence
    matched_strategies: list[str]       # strategy_ids
    entry_zone_low:    float
    entry_zone_high:   float
    reasoning:         list[str] = []


# ── Risk Models ───────────────────────────────────────────────────────────────

class RiskParams(BaseModel):
    """Trade risk parameters with validation."""
    sl_pips:      float
    tp_ratio:     float
    account_risk_pct: float = 1.0

    @field_validator("sl_pips")
    @classmethod
    def validate_sl(cls, v: float) -> float:
        if v < 10.0:
            raise ValueError("SL must be at least 10 pips")
        return v

    @field_validator("tp_ratio")
    @classmethod
    def validate_tp(cls, v: float) -> float:
        if v < 1.5:
            raise ValueError("TP ratio must be at least 1.5 (minimum RR 1:1.5)")
        return v

    @field_validator("account_risk_pct")
    @classmethod
    def validate_risk(cls, v: float) -> float:
        if v > 2.0:
            raise ValueError("Account risk must not exceed 2% per trade")
        return v

    @property
    def is_valid(self) -> bool:
        return self.sl_pips >= 10.0 and self.tp_ratio >= 1.5 and self.account_risk_pct <= 2.0


class TradeSetup(BaseModel):
    """Complete validated trade setup."""
    signal:      SignalDetection
    risk:        RiskParams
    entry_price: float
    sl_price:    float
    tp_price:    float
    pip_size:    float = 0.0001
    notes:       list[str] = []

    @property
    def sl_pips(self) -> float:
        return abs(self.entry_price - self.sl_price) / self.pip_size

    @property
    def tp_pips(self) -> float:
        return abs(self.tp_price - self.entry_price) / self.pip_size

    @property
    def rr_ratio(self) -> float:
        return self.tp_pips / self.sl_pips if self.sl_pips > 0 else 0.0


# ── Agent Models ──────────────────────────────────────────────────────────────

class HermesToolCall(BaseModel):
    """Tool definition schema for Hermes agent."""
    name:        str
    description: str
    parameters:  dict[str, Any]


class HermesAction(BaseModel):
    """Agent output action."""
    tool:       str
    arguments:  dict[str, Any]
    reasoning:  str
    confidence: float   # 0.0 - 1.0


class HermesAgentConfig(BaseModel):
    """Complete Hermes agent configuration."""
    agent_name:    str = "hermes-things"
    version:       str = "1.0"
    system_prompt: str
    tools:         list[HermesToolCall]
    strategy_count: int
    pairs:         list[str]
    guardrails:    list[str]
