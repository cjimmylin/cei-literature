#!/usr/bin/env python3
"""
WEIRD Scoring for CEI Literature Vault papers.

Operationalizes Henrich, Heine & Norenzayan (2010) "The weirdest people in the
world?" as a composite 0-100 score combining:

    W = Western         (author institution + study population geography)
    E = Educated        (university sample, student participants)
    I = Industrialized  (country income tier)
    R = Rich            (GDP per capita)
    D = Democratic      (democracy index)

Each sub-dimension scored 0-20, sum = 0-100.

The score answers: "How WEIRD-population-centric is this paper's perspective?"
Higher = more WEIRD. This is NOT a quality judgment — it's a descriptive measure.

Usage:
    python score_weird.py [--dry-run]
"""
from __future__ import annotations

import functools
import json
import os
import re
import sys
from collections import Counter
from datetime import date
from pathlib import Path

print = functools.partial(print, flush=True)

_SCRIPT_DIR = Path(__file__).parent
_CEI_LIT_WS = _SCRIPT_DIR.parent.parent
sys.path.insert(0, str(_CEI_LIT_WS / "PYTHON"))
sys.path.insert(0, str(_CEI_LIT_WS / ".agent" / "lib"))
sys.path.insert(0, str(_SCRIPT_DIR))

from config import PAPERS_DIR
from ethics_scoring import load_extract
from geo_mappings import (
    get_region,
    get_weird_tier,
    weird_country_score,
    HIGH_WEIRD_COUNTRIES,
    MODERATE_WEIRD_COUNTRIES,
    LOW_WEIRD_COUNTRIES,
)

TODAY = date.today().strftime("%Y%m%d")
DATA_DIR = _SCRIPT_DIR.parent / "DATA"
STATS_DIR = _SCRIPT_DIR.parent / "STATISTICS"
GEO_DATA_PATH = DATA_DIR / f"{TODAY}-author-geography.json"


# =====================================================================
# WEIRD SUB-DIMENSION SCORERS
# =====================================================================

def score_western(author_country: str, study_regions: list[str]) -> int:
    """W = Western: 0-20 based on author country + study focus."""
    if not author_country or author_country == "Unknown":
        return 10  # default middle

    region = get_region(author_country)

    # Author in Western region
    if region in ("North America", "Western Europe", "Oceania"):
        author_w = 14
    elif region in ("Eastern Europe & Central Asia",):
        author_w = 8
    else:
        author_w = 2

    # Study population Western
    if not study_regions:
        study_w = 6  # unknown = mild Western assumption
    elif any(r in ("North America", "Western Europe", "Oceania") for r in study_regions):
        study_w = 6
    else:
        study_w = 0

    return min(20, author_w + study_w)


def score_educated(text: str) -> int:
    """E = Educated: 0-20 based on university/student sample indicators."""
    if not text:
        return 10

    text_lower = text.lower()
    score = 0

    edu_signals = [
        (r"\buniversity\s+student", 5),
        (r"\bundergraduate", 5),
        (r"\bgraduate\s+student", 4),
        (r"\bcollege\s+student", 5),
        (r"\bstudent\s+(?:sample|population|participants?|subjects?)\b", 5),
        (r"\bmturk\b", 4),  # Amazon Mechanical Turk = typically educated
        (r"\bprolific\b(?=.*(?:participant|sample|crowd))", 4),
        (r"\bcrowdsourc", 3),
        (r"\bannotator", 2),
    ]

    non_edu_signals = [
        (r"\bfield\s+study\b", -3),
        (r"\bethno", -3),
        (r"\bcommunity-based", -3),
        (r"\brural\b(?=.*(?:participant|population|community))", -4),
        (r"\billiterat", -4),
        (r"\blow-?income\s+(?:participant|community|population)", -4),
    ]

    for pat, weight in edu_signals + non_edu_signals:
        if re.search(pat, text_lower):
            score += weight

    return max(0, min(20, score + 10))  # centered at 10


def score_industrialized(author_country: str) -> int:
    """I = Industrialized: 0-20 based on country's industrial development."""
    if not author_country or author_country == "Unknown":
        return 10

    tier = get_weird_tier(author_country)
    return {
        "High-WEIRD": 18,
        "Moderate-WEIRD": 14,
        "Low-WEIRD": 8,
        "Non-WEIRD": 3,
    }[tier]


def score_rich(author_country: str) -> int:
    """R = Rich: 0-20 based on GDP per capita tier."""
    # Same mapping as Industrialized for simplicity
    # (these dimensions are highly correlated in practice)
    if not author_country or author_country == "Unknown":
        return 10

    tier = get_weird_tier(author_country)
    return {
        "High-WEIRD": 18,
        "Moderate-WEIRD": 13,
        "Low-WEIRD": 7,
        "Non-WEIRD": 3,
    }[tier]


def score_democratic(author_country: str) -> int:
    """D = Democratic: 0-20 based on democracy level."""
    if not author_country or author_country == "Unknown":
        return 10

    # High democracy (Economist Intelligence Unit full democracies)
    full_democracy = {"NO", "SE", "FI", "DK", "NZ", "IE", "CH", "NL",
                      "IS", "LU", "DE", "AU", "CA", "AT", "UY",
                      "GB", "CR", "JP", "KR", "ES", "FR", "PT", "TW"}

    flawed_democracy = {"US", "IT", "GR", "BE", "IL", "CZ", "PL", "SI",
                        "EE", "LT", "LV", "SK", "HR", "HU", "RO", "BG",
                        "IN", "BR", "AR", "CL", "CO", "MX", "ID", "PH",
                        "MY", "SG", "ZA", "NG", "GH", "KE", "TZ", "SN"}

    authoritarian = {"CN", "RU", "IR", "SA", "AE", "QA", "KW", "BH",
                     "EG", "VN", "TH", "MM", "KH", "LA", "BY",
                     "TM", "UZ", "TJ", "KZ", "SY", "YE",
                     "AF", "CD", "SD", "SS", "ER", "DJ"}

    cc = author_country.upper()
    if cc in full_democracy:
        return 18
    elif cc in flawed_democracy:
        return 12
    elif cc in authoritarian:
        return 3
    else:
        return 8  # hybrid/unknown


def compute_weird_score(author_country: str, text: str,
                        study_regions: list[str] | None = None) -> dict:
    """
    Compute composite WEIRD score (0-100) with sub-dimension breakdown.

    Returns dict with keys: weird_score, w, e, i, r, d
    """
    if study_regions is None:
        study_regions = []

    w = score_western(author_country, study_regions)
    e = score_educated(text)
    i = score_industrialized(author_country)
    r = score_rich(author_country)
    d = score_democratic(author_country)

    return {
        "weird_score": w + e + i + r + d,
        "w": w, "e": e, "i": i, "r": r, "d": d,
    }


# =====================================================================
# MAIN
# =====================================================================

def main():
    args = sys.argv[1:]
    dry_run = "--dry-run" in args

    # Load author geography data
    if not GEO_DATA_PATH.exists():
        print(f"ERROR: Author geography data not found at {GEO_DATA_PATH}")
        print(f"Run enrich_author_geography.py first.")
        return 1

    with open(GEO_DATA_PATH) as f:
        geo_data = json.load(f)

    # Build filename → country lookup
    geo_lookup = {}
    for p in geo_data["papers"]:
        cc = p["author_country"]
        geo_lookup[p["filename"]] = cc if cc != "Unknown" else None

    papers = sorted(PAPERS_DIR.glob("*.md"))
    print(f"Computing WEIRD scores for {len(papers)} papers...")

    results = []
    score_dist = Counter()  # tier → count
    total_score = 0

    for idx, paper_path in enumerate(papers, 1):
        if idx % 200 == 0:
            print(f"  Progress: {idx}/{len(papers)}")

        filename = paper_path.name
        author_country = geo_lookup.get(filename)

        # Load text for education dimension
        content = paper_path.read_text(encoding="utf-8", errors="replace")
        abstract_m = re.search(r'^abstract:\s*"?(.+?)"?\s*$', content, re.MULTILINE)
        abstract = abstract_m.group(1) if abstract_m else ""
        stem = paper_path.stem
        extract = load_extract(stem)
        text = f"{abstract} {extract[:5000]}"

        scores = compute_weird_score(author_country or "", text)
        ws = scores["weird_score"]
        total_score += ws

        # Categorize
        if ws >= 70:
            tier = "High-WEIRD (70-100)"
        elif ws >= 50:
            tier = "Moderate-WEIRD (50-69)"
        elif ws >= 30:
            tier = "Low-WEIRD (30-49)"
        else:
            tier = "Non-WEIRD (0-29)"
        score_dist[tier] += 1

        entry = {
            "filename": filename,
            "author_country": author_country or "Unknown",
            **scores,
            "tier": tier,
        }
        results.append(entry)

    # ── Save ─────────────────────────────────────────────────────────
    out_path = DATA_DIR / f"{TODAY}-weird-scores.json"
    report_path = STATS_DIR / f"{TODAY}-weird-score-report.md"

    if not dry_run:
        output = {
            "date": TODAY,
            "total_papers": len(results),
            "mean_weird_score": round(total_score / max(len(results), 1), 1),
            "tier_distribution": dict(score_dist.most_common()),
            "papers": results,
        }
        tmp = out_path.with_suffix(f".tmp.{os.getpid()}.json")
        tmp.write_text(json.dumps(output, indent=2))
        os.replace(str(tmp), str(out_path))
        print(f"\nSaved to {out_path}")

    # ── Summary ──────────────────────────────────────────────────────
    mean = total_score / max(len(results), 1)
    print(f"\n{'='*60}")
    print(f"WEIRD SCORING RESULTS")
    print(f"{'='*60}")
    print(f"Papers: {len(results)}, Mean WEIRD score: {mean:.1f}")
    print(f"\nTier distribution:")
    for tier in ["High-WEIRD (70-100)", "Moderate-WEIRD (50-69)",
                 "Low-WEIRD (30-49)", "Non-WEIRD (0-29)"]:
        c = score_dist.get(tier, 0)
        print(f"  {tier}: {c} ({c/len(results)*100:.1f}%)")

    # Save report
    if not dry_run:
        report = [
            "# WEIRD Score Report",
            "",
            f"**Date:** {TODAY}",
            f"**Papers:** {len(results)}",
            f"**Mean WEIRD score:** {mean:.1f} / 100",
            "",
            "## Tier Distribution",
            "",
            "| Tier | Count | % |",
            "|------|-------|---|",
        ]
        for tier in ["High-WEIRD (70-100)", "Moderate-WEIRD (50-69)",
                     "Low-WEIRD (30-49)", "Non-WEIRD (0-29)"]:
            c = score_dist.get(tier, 0)
            report.append(f"| {tier} | {c} | {c/len(results)*100:.1f}% |")

        report.extend([
            "",
            "## Sub-Dimension Means",
            "",
            "| Dimension | Mean (0-20) |",
            "|-----------|------------|",
        ])
        for dim in ["w", "e", "i", "r", "d"]:
            dim_total = sum(r[dim] for r in results)
            dim_mean = dim_total / max(len(results), 1)
            labels = {"w": "Western", "e": "Educated", "i": "Industrialized",
                      "r": "Rich", "d": "Democratic"}
            report.append(f"| {labels[dim]} ({dim.upper()}) | {dim_mean:.1f} |")

        report_path.write_text("\n".join(report))
        print(f"Saved report to {report_path}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
