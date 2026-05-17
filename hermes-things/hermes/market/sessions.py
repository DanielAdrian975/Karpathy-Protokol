"""
hermes.market.sessions
----------------------
Session killzone detection.
Chris Lori killzones (EST):
  London  : 02:00 – 05:00
  New York: 07:00 – 10:00
  Asian   : 20:00 – 00:00 (next day)
"""

from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime, time, timezone, timedelta


EST = timezone(timedelta(hours=-5))  # Standard EST; does not auto-adjust DST


@dataclass
class SessionConfig:
    name: str
    start: time
    end: time
    weight: float = 1.0


@dataclass
class SessionResult:
    active_session: str | None  # Name of active session, or None
    weight: float
    is_killzone: bool
    london: bool
    new_york: bool
    asian: bool


SESSIONS: list[SessionConfig] = [
    SessionConfig("london",   time(2, 0),  time(5, 0),  1.0),
    SessionConfig("new_york", time(7, 0),  time(10, 0), 1.0),
    SessionConfig("asian",    time(20, 0), time(23, 59), 0.5),
]


def _in_window(t: time, start: time, end: time) -> bool:
    if start <= end:
        return start <= t <= end
    # Overnight window
    return t >= start or t <= end


def check(dt: datetime | None = None, sessions: list[SessionConfig] | None = None) -> SessionResult:
    """
    Check which killzone is active at the given datetime (default: now).
    dt should be timezone-aware; converted to EST internally.
    """
    if sessions is None:
        sessions = SESSIONS

    if dt is None:
        dt = datetime.now(tz=EST)
    elif dt.tzinfo is None:
        dt = dt.replace(tzinfo=EST)
    else:
        dt = dt.astimezone(EST)

    t = dt.time()
    active = None
    weight = 0.0
    flags: dict[str, bool] = {s.name: False for s in sessions}

    for s in sessions:
        if _in_window(t, s.start, s.end):
            flags[s.name] = True
            if active is None or s.weight > weight:
                active = s.name
                weight = s.weight

    return SessionResult(
        active_session=active,
        weight=weight,
        is_killzone=active is not None,
        london=flags.get("london", False),
        new_york=flags.get("new_york", False),
        asian=flags.get("asian", False),
    )
