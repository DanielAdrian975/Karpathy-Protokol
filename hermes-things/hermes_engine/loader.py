"""
hermes_engine.loader
--------------------
CSV loader for STRATEGY_DATABASE.csv.
Handles semicolons in Rules field via custom parser.
"""

from __future__ import annotations
import csv
from pathlib import Path
from hermes_engine.models import (
    Strategy, Article, Category, CategoryCode, CATEGORY_NAMES
)


def _parse_row(fields: list[str]) -> dict:
    """
    Parse a CSV row where Rules field may contain semicolons.
    Expected: Article_ID;Title;Strategy_No;Name;Image_URL;...Rules...;Category;Duplicate_Group
    """
    article_id    = int(fields[0])
    article_title = fields[1].strip()
    strategy_no   = int(fields[2])
    strategy_name = fields[3].strip()
    # image_url = fields[4]  (skipped)
    category       = fields[-2].strip()
    duplicate_group = int(fields[-1])
    rules          = ";".join(fields[5:-2]).strip().strip(";")
    return {
        "article_id":      article_id,
        "article_title":   article_title,
        "strategy_no":     strategy_no,
        "strategy_name":   strategy_name,
        "rules":           rules,
        "category":        category,
        "duplicate_group": duplicate_group,
    }


def load(csv_path: str | Path) -> list[Strategy]:
    """Load all strategies from CSV. Returns validated Strategy list."""
    strategies: list[Strategy] = []
    path = Path(csv_path)

    with open(path, encoding="utf-8", newline="") as f:
        reader = csv.reader(f, delimiter=";")
        next(reader)  # skip header
        for line_no, row in enumerate(reader, start=2):
            if not row or not row[0].strip():
                continue
            try:
                data = _parse_row(row)
                strategies.append(Strategy(**data))
            except Exception as e:
                raise ValueError(f"Line {line_no}: {e} | row={row}")

    return strategies


def build_articles(strategies: list[Strategy]) -> list[Article]:
    """Group strategies by article_id into Article objects."""
    groups: dict[int, dict] = {}
    for s in strategies:
        if s.article_id not in groups:
            groups[s.article_id] = {"article_id": s.article_id, "title": s.article_title, "strategies": []}
        groups[s.article_id]["strategies"].append(s)
    return [Article(**v) for v in sorted(groups.values(), key=lambda x: x["article_id"])]


def build_categories(strategies: list[Strategy]) -> list[Category]:
    """Group strategies by category into Category objects."""
    groups: dict[str, list[Strategy]] = {}
    for s in strategies:
        groups.setdefault(s.category.value, []).append(s)
    return [
        Category(
            code=CategoryCode(code),
            name=CATEGORY_NAMES.get(code, code),
            strategies=strats,
        )
        for code, strats in sorted(groups.items())
    ]


def get_by_category(strategies: list[Strategy], code: str) -> list[Strategy]:
    return [s for s in strategies if s.category.value == code]


def get_by_article(strategies: list[Strategy], article_id: int) -> list[Strategy]:
    return [s for s in strategies if s.article_id == article_id]


def get_by_duplicate_group(strategies: list[Strategy], group: int) -> list[Strategy]:
    return [s for s in strategies if s.duplicate_group == group]


def summary(strategies: list[Strategy]) -> dict:
    cats = {}
    for s in strategies:
        cats[s.category.value] = cats.get(s.category.value, 0) + 1
    return {
        "total_strategies": len(strategies),
        "articles": len({s.article_id for s in strategies}),
        "categories": cats,
        "duplicate_groups": len({s.duplicate_group for s in strategies}),
    }
