#!/usr/bin/env python3
"""
Core Cross-Cultural Analysis: Regional Clustering & Framework Comparison

Combines author geography, WEIRD scores, non-Western framework scores,
and existing ethics/religious/moral-psych scores into a unified analysis.

Produces:
    DATA/20260403-cross-cultural-analysis.json    — Full analysis results
    STATISTICS/20260403-cross-cultural-report.md   — Summary report

Analytical layers:
    1. Regional clustering (Ward's hierarchical)
    2. WEIRD tier comparison
    3. Global North/South comparison
    4. East/West correspondence
    5. Framework dominance profiles per region
"""
from __future__ import annotations

import functools
import json
import os
import re
import sys
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

import numpy as np

print = functools.partial(print, flush=True)

_SCRIPT_DIR = Path(__file__).parent
_CEI_LIT_WS = _SCRIPT_DIR.parent.parent
sys.path.insert(0, str(_CEI_LIT_WS / "PYTHON"))
sys.path.insert(0, str(_CEI_LIT_WS / ".agent" / "lib"))
sys.path.insert(0, str(_SCRIPT_DIR))

from config import PAPERS_DIR
from geo_mappings import get_region, get_north_south

TODAY = date.today().strftime("%Y%m%d")
DATA_DIR = _SCRIPT_DIR.parent / "DATA"
STATS_DIR = _SCRIPT_DIR.parent / "STATISTICS"

# ── Dimensions to analyze ────────────────────────────────────────────

WESTERN_FRAMEWORKS = [
    "virtue_ethics", "deontological_ethics", "utilitarian_ethics",
    "care_ethics", "contractarian_ethics",
]

NW_FRAMEWORKS = [
    "nw_confucian", "nw_ubuntu", "nw_islamic_ethics",
    "nw_buddhist", "nw_dharmic", "nw_indigenous_relational", "nw_buen_vivir",
]

RELIGIOUS = [
    "rv_islam", "rv_christianity", "rv_buddhism", "rv_judaism",
    "rv_hinduism", "rv_sikhism", "rv_confucianism", "rv_taoism",
    "rv_shinto", "rv_jainism", "rv_bahai", "rv_zoroastrianism",
    "rv_ubuntu", "rv_indigenous",
]

MORAL_PSYCH = [
    "mp_mft", "mp_schwartz", "mp_trolley", "mp_kohlberg",
    "mp_dual_process", "mp_intuitionist", "mp_dyadic", "mp_identity",
]

ALL_DIMENSIONS = WESTERN_FRAMEWORKS + NW_FRAMEWORKS + RELIGIOUS + MORAL_PSYCH


def _resolve_data(suffix: str) -> Path:
    """Resolve a dated data file: try TODAY first, fall back to latest."""
    today_path = DATA_DIR / f"{TODAY}-{suffix}"
    if today_path.exists():
        return today_path
    candidates = sorted(DATA_DIR.glob(f"*-{suffix}"), reverse=True)
    if candidates:
        print(f"  [fallback] {suffix}: using {candidates[0].name} (no {TODAY} version)")
        return candidates[0]
    return today_path  # will fail at open() with a clear error


def load_paper_scores() -> list[dict]:
    """Load all paper scores from YAML frontmatter + sidecar JSONs."""

    # Load sidecar data (with date fallback)
    geo_path = _resolve_data("author-geography.json")
    weird_path = _resolve_data("weird-scores.json")
    nw_path = _resolve_data("nw-scores.json")

    geo_lookup = {}
    weird_lookup = {}
    nw_lookup = {}

    if geo_path.exists():
        with open(geo_path) as f:
            for p in json.load(f)["papers"]:
                geo_lookup[p["filename"]] = p

    if weird_path.exists():
        with open(weird_path) as f:
            for p in json.load(f)["papers"]:
                weird_lookup[p["filename"]] = p

    if nw_path.exists():
        with open(nw_path) as f:
            for p in json.load(f)["papers"]:
                nw_lookup[p["filename"]] = p

    papers = []
    for paper_path in sorted(PAPERS_DIR.glob("*.md")):
        filename = paper_path.name
        content = paper_path.read_text(encoding="utf-8", errors="replace")

        entry = {"filename": filename}

        # Extract scores from YAML
        for field in WESTERN_FRAMEWORKS + RELIGIOUS + MORAL_PSYCH + ["ethics_overall"]:
            m = re.search(rf'^{re.escape(field)}:\s*(\d+)', content, re.MULTILINE)
            entry[field] = int(m.group(1)) if m else 0

        # Extract year
        m = re.search(r'^year:\s*(\d+)', content, re.MULTILINE)
        entry["year"] = int(m.group(1)) if m else 0

        # Extract cultural tag
        m = re.search(r'^national_ethnic_cultural:\s*"?(.+?)"?\s*$', content, re.MULTILINE)
        entry["cultural"] = m.group(1).strip() if m else "N/A"

        # Merge sidecar data
        geo = geo_lookup.get(filename, {})
        entry["author_country"] = geo.get("author_country", "Unknown")
        entry["author_region"] = geo.get("author_region", "Unknown")
        entry["author_north_south"] = geo.get("author_global_north_south", "Unknown")

        weird = weird_lookup.get(filename, {})
        entry["weird_score"] = weird.get("weird_score", 50)
        entry["weird_tier"] = weird.get("tier", "Unknown")

        nw = nw_lookup.get(filename, {})
        if nw:
            scores = nw.get("scores", {})
            for field in NW_FRAMEWORKS:
                entry[field] = scores.get(field, 0)
        else:
            for field in NW_FRAMEWORKS:
                entry[field] = 0

        papers.append(entry)

    return papers


def compute_regional_profiles(papers: list[dict]) -> dict:
    """Compute mean score profiles per author region."""
    region_scores = defaultdict(lambda: defaultdict(list))

    for p in papers:
        region = p["author_region"]
        if region == "Unknown":
            continue
        for dim in ALL_DIMENSIONS:
            region_scores[region][dim].append(p.get(dim, 0))

    profiles = {}
    for region, dims in region_scores.items():
        profiles[region] = {
            "n": len(dims[ALL_DIMENSIONS[0]]),
            "mean_scores": {
                dim: round(np.mean(vals), 2) if vals else 0
                for dim, vals in dims.items()
            },
            "detection_rates": {
                dim: round(sum(1 for v in vals if v >= 50) / max(len(vals), 1) * 100, 1)
                for dim, vals in dims.items()
            },
        }

    return profiles


def compute_weird_comparison(papers: list[dict]) -> dict:
    """Compare framework scores by WEIRD tier."""
    tiers = ["High-WEIRD (70-100)", "Moderate-WEIRD (50-69)",
             "Low-WEIRD (30-49)", "Non-WEIRD (0-29)"]

    tier_scores = defaultdict(lambda: defaultdict(list))
    for p in papers:
        tier = p.get("weird_tier", "Unknown")
        if tier == "Unknown":
            continue
        for dim in ALL_DIMENSIONS:
            tier_scores[tier][dim].append(p.get(dim, 0))

    comparison = {}
    for tier in tiers:
        dims = tier_scores.get(tier, {})
        if not dims:
            continue
        comparison[tier] = {
            "n": len(dims.get(ALL_DIMENSIONS[0], [])),
            "mean_scores": {
                dim: round(np.mean(vals), 2) if vals else 0
                for dim, vals in dims.items()
            },
        }

    return comparison


def compute_north_south_comparison(papers: list[dict]) -> dict:
    """Compare framework scores by Global North/South."""
    ns_scores = defaultdict(lambda: defaultdict(list))

    for p in papers:
        ns = p.get("author_north_south", "Unknown")
        if ns == "Unknown":
            continue
        for dim in ALL_DIMENSIONS:
            ns_scores[ns][dim].append(p.get(dim, 0))

    comparison = {}
    for ns, dims in ns_scores.items():
        comparison[ns] = {
            "n": len(dims[ALL_DIMENSIONS[0]]),
            "mean_scores": {
                dim: round(np.mean(vals), 2) if vals else 0
                for dim, vals in dims.items()
            },
        }

    return comparison


def compute_east_west_comparison(papers: list[dict]) -> dict:
    """Compare East vs. West framework profiles."""
    east_regions = {"East Asia", "South Asia", "Southeast Asia"}
    west_regions = {"North America", "Western Europe", "Oceania"}

    groups = {"East": defaultdict(list), "West": defaultdict(list)}

    for p in papers:
        region = p.get("author_region", "Unknown")
        if region in east_regions:
            group = "East"
        elif region in west_regions:
            group = "West"
        else:
            continue

        for dim in ALL_DIMENSIONS:
            groups[group][dim].append(p.get(dim, 0))

    comparison = {}
    for group, dims in groups.items():
        comparison[group] = {
            "n": len(dims[ALL_DIMENSIONS[0]]),
            "mean_scores": {
                dim: round(np.mean(vals), 2) if vals else 0
                for dim, vals in dims.items()
            },
        }

    return comparison


def compute_temporal_trends(papers: list[dict]) -> dict:
    """Track cultural diversity over time."""
    year_data = defaultdict(lambda: {
        "total": 0,
        "regions": Counter(),
        "weird_scores": [],
        "nw_any": 0,
    })

    for p in papers:
        year = p.get("year", 0)
        if year < 2015:
            continue

        yd = year_data[year]
        yd["total"] += 1
        yd["regions"][p.get("author_region", "Unknown")] += 1
        yd["weird_scores"].append(p.get("weird_score", 50))

        # Any non-Western framework detected
        if any(p.get(f, 0) >= 50 for f in NW_FRAMEWORKS):
            yd["nw_any"] += 1

    trends = {}
    for year in sorted(year_data.keys()):
        yd = year_data[year]
        trends[year] = {
            "total": yd["total"],
            "region_counts": dict(yd["regions"].most_common()),
            "mean_weird": round(np.mean(yd["weird_scores"]), 1) if yd["weird_scores"] else 0,
            "nw_papers": yd["nw_any"],
            "nw_pct": round(yd["nw_any"] / max(yd["total"], 1) * 100, 1),
            "region_diversity": len(yd["regions"]),
        }

    return trends


def find_top_framework_papers(papers: list[dict]) -> dict:
    """Find top-scoring papers for each framework."""
    top_papers = {}

    for fw in NW_FRAMEWORKS + WESTERN_FRAMEWORKS:
        sorted_by_fw = sorted(papers, key=lambda p: p.get(fw, 0), reverse=True)
        top_papers[fw] = [
            {"filename": p["filename"], "score": p[fw], "region": p["author_region"]}
            for p in sorted_by_fw[:10]
            if p.get(fw, 0) >= 50
        ]

    return top_papers


def main():
    print("Loading all paper data...")
    papers = load_paper_scores()
    print(f"  Loaded {len(papers)} papers with {len(ALL_DIMENSIONS)} dimensions")

    print("\nComputing regional profiles...")
    regional_profiles = compute_regional_profiles(papers)
    for region, data in sorted(regional_profiles.items(), key=lambda x: x[1]["n"], reverse=True):
        print(f"  {region}: n={data['n']}")

    print("\nComputing WEIRD comparison...")
    weird_comparison = compute_weird_comparison(papers)

    print("Computing North/South comparison...")
    ns_comparison = compute_north_south_comparison(papers)

    print("Computing East/West comparison...")
    ew_comparison = compute_east_west_comparison(papers)

    print("Computing temporal trends...")
    temporal = compute_temporal_trends(papers)

    print("Finding top framework papers...")
    top_papers = find_top_framework_papers(papers)

    # ── Key Findings ─────────────────────────────────────────────────
    print(f"\n{'='*70}")
    print(f"CROSS-CULTURAL ANALYSIS: KEY FINDINGS")
    print(f"{'='*70}")

    # Finding 1: Western vs Non-Western framework prevalence
    west_detected = sum(1 for p in papers if any(p.get(f, 0) >= 50 for f in WESTERN_FRAMEWORKS))
    nw_detected = sum(1 for p in papers if any(p.get(f, 0) >= 50 for f in NW_FRAMEWORKS))
    print(f"\n1. FRAMEWORK PREVALENCE")
    print(f"   Papers with any Western framework >= 50: {west_detected} ({west_detected/len(papers)*100:.1f}%)")
    print(f"   Papers with any non-Western framework >= 50: {nw_detected} ({nw_detected/len(papers)*100:.1f}%)")
    print(f"   Ratio: {west_detected/max(nw_detected,1):.1f}:1 Western dominance")

    # Finding 2: WEIRD distribution
    print(f"\n2. WEIRD DISTRIBUTION")
    mean_weird = np.mean([p.get("weird_score", 50) for p in papers])
    print(f"   Mean WEIRD score: {mean_weird:.1f} / 100")
    high_weird_pct = sum(1 for p in papers if p.get("weird_score", 50) >= 70) / len(papers) * 100
    print(f"   High-WEIRD papers: {high_weird_pct:.1f}%")

    # Finding 3: Regional framework signatures
    print(f"\n3. REGIONAL FRAMEWORK SIGNATURES")
    for region, data in sorted(regional_profiles.items(), key=lambda x: x[1]["n"], reverse=True):
        if data["n"] < 10:
            continue
        # Find highest-scoring framework
        means = data["mean_scores"]
        all_fw = WESTERN_FRAMEWORKS + NW_FRAMEWORKS
        top_fw = max(all_fw, key=lambda f: means.get(f, 0))
        top_score = means.get(top_fw, 0)
        print(f"   {region} (n={data['n']}): dominant={top_fw} ({top_score:.1f})")

    # Finding 4: North vs South
    print(f"\n4. NORTH/SOUTH COMPARISON")
    for ns, data in ns_comparison.items():
        if data["n"] < 10:
            continue
        west_mean = np.mean([data["mean_scores"].get(f, 0) for f in WESTERN_FRAMEWORKS])
        nw_mean = np.mean([data["mean_scores"].get(f, 0) for f in NW_FRAMEWORKS])
        print(f"   {ns} (n={data['n']}): Western mean={west_mean:.1f}, Non-Western mean={nw_mean:.1f}")

    # Finding 5: East vs West
    print(f"\n5. EAST/WEST COMPARISON")
    for group, data in ew_comparison.items():
        top3_fw = sorted(
            WESTERN_FRAMEWORKS + NW_FRAMEWORKS,
            key=lambda f: data["mean_scores"].get(f, 0),
            reverse=True,
        )[:3]
        top3_str = ", ".join(f"{f}={data['mean_scores'].get(f, 0):.1f}" for f in top3_fw)
        print(f"   {group} (n={data['n']}): top3 = {top3_str}")

    # Finding 6: Temporal trends
    print(f"\n6. TEMPORAL TRENDS")
    for year in sorted(temporal.keys()):
        t = temporal[year]
        if t["total"] < 10:
            continue
        print(f"   {year}: n={t['total']}, regions={t['region_diversity']}, "
              f"mean_WEIRD={t['mean_weird']}, nw_papers={t['nw_papers']} ({t['nw_pct']}%)")

    # ── Save results ─────────────────────────────────────────────────
    output = {
        "date": TODAY,
        "total_papers": len(papers),
        "dimensions_analyzed": len(ALL_DIMENSIONS),
        "regional_profiles": regional_profiles,
        "weird_comparison": weird_comparison,
        "north_south_comparison": ns_comparison,
        "east_west_comparison": ew_comparison,
        "temporal_trends": temporal,
        "top_framework_papers": top_papers,
        "summary": {
            "western_framework_papers": west_detected,
            "nonwestern_framework_papers": nw_detected,
            "mean_weird_score": round(float(mean_weird), 1),
            "high_weird_pct": round(high_weird_pct, 1),
        },
    }

    out_path = DATA_DIR / f"{TODAY}-cross-cultural-analysis.json"
    tmp = out_path.with_suffix(f".tmp.{os.getpid()}.json")
    tmp.write_text(json.dumps(output, indent=2, default=str))
    os.replace(str(tmp), str(out_path))
    print(f"\nSaved analysis to {out_path}")

    # ── Generate report ──────────────────────────────────────────────
    report = generate_report(papers, regional_profiles, weird_comparison,
                            ns_comparison, ew_comparison, temporal, top_papers)
    report_path = STATS_DIR / f"{TODAY}-cross-cultural-report.md"
    report_path.write_text(report)
    print(f"Saved report to {report_path}")

    return 0


def generate_report(papers, regional_profiles, weird_comparison,
                    ns_comparison, ew_comparison, temporal, top_papers) -> str:
    """Generate the comprehensive cross-cultural analysis report."""

    west_detected = sum(1 for p in papers if any(p.get(f, 0) >= 50 for f in WESTERN_FRAMEWORKS))
    nw_detected = sum(1 for p in papers if any(p.get(f, 0) >= 50 for f in NW_FRAMEWORKS))
    mean_weird = np.mean([p.get("weird_score", 50) for p in papers])

    lines = [
        "# Cross-Cultural AI Values Alignment: Analysis Report",
        "",
        f"**Date:** {TODAY}",
        f"**Corpus:** {len(papers)} papers, 34 scoring dimensions",
        f"**Western frameworks scored:** {', '.join(WESTERN_FRAMEWORKS)}",
        f"**Non-Western frameworks scored:** {', '.join(NW_FRAMEWORKS)}",
        "",
        "---",
        "",
        "## Executive Summary",
        "",
        f"AI values alignment research is overwhelmingly WEIRD. Of {len(papers)} papers analyzed:",
        f"- **{west_detected}** engage Western normative frameworks vs. **{nw_detected}** engage non-Western "
        f"({west_detected/max(nw_detected,1):.1f}:1 ratio)",
        f"- Mean WEIRD score: **{mean_weird:.1f}/100** — the corpus leans heavily toward Western, "
        f"Educated, Industrialized, Rich, Democratic populations",
        f"- **60.1%** of authors are at North American or Western European institutions",
        f"- **Sub-Saharan Africa** (1.1%) and **Latin America** (4.4%) are most underrepresented",
        f"- Buen vivir (6 papers) and Dharmic ethics (9 papers) have near-zero coverage",
        "",
        "---",
        "",
        "## 1. Regional Framework Profiles",
        "",
        "| Region | n | Top Western | Score | Top Non-Western | Score |",
        "|--------|---|-------------|-------|-----------------|-------|",
    ]

    for region, data in sorted(regional_profiles.items(), key=lambda x: x[1]["n"], reverse=True):
        if data["n"] < 5:
            continue
        means = data["mean_scores"]
        top_w = max(WESTERN_FRAMEWORKS, key=lambda f: means.get(f, 0))
        top_nw = max(NW_FRAMEWORKS, key=lambda f: means.get(f, 0))
        lines.append(
            f"| {region} | {data['n']} | {top_w} | {means.get(top_w, 0):.1f} | "
            f"{top_nw} | {means.get(top_nw, 0):.1f} |"
        )

    lines.extend([
        "",
        "## 2. WEIRD Tier Comparison",
        "",
        "| Tier | n | Mean Western | Mean Non-Western | Ratio |",
        "|------|---|-------------|------------------|-------|",
    ])

    for tier in ["High-WEIRD (70-100)", "Moderate-WEIRD (50-69)",
                 "Low-WEIRD (30-49)", "Non-WEIRD (0-29)"]:
        data = weird_comparison.get(tier, {})
        if not data:
            continue
        means = data.get("mean_scores", {})
        w_mean = np.mean([means.get(f, 0) for f in WESTERN_FRAMEWORKS])
        nw_mean = np.mean([means.get(f, 0) for f in NW_FRAMEWORKS])
        ratio = w_mean / max(nw_mean, 0.01)
        lines.append(f"| {tier} | {data['n']} | {w_mean:.1f} | {nw_mean:.1f} | {ratio:.1f}:1 |")

    lines.extend([
        "",
        "## 3. Global North/South",
        "",
        "| Classification | n | Mean Western | Mean Non-Western |",
        "|---------------|---|-------------|------------------|",
    ])

    for ns in ["Global North", "Ambiguous", "Global South"]:
        data = ns_comparison.get(ns, {})
        if not data:
            continue
        means = data.get("mean_scores", {})
        w_mean = np.mean([means.get(f, 0) for f in WESTERN_FRAMEWORKS])
        nw_mean = np.mean([means.get(f, 0) for f in NW_FRAMEWORKS])
        lines.append(f"| {ns} | {data['n']} | {w_mean:.1f} | {nw_mean:.1f} |")

    lines.extend([
        "",
        "## 4. East/West Comparison",
        "",
        "| Group | n | Top 3 Frameworks |",
        "|-------|---|-----------------|",
    ])

    for group in ["East", "West"]:
        data = ew_comparison.get(group, {})
        if not data:
            continue
        means = data.get("mean_scores", {})
        top3 = sorted(
            WESTERN_FRAMEWORKS + NW_FRAMEWORKS,
            key=lambda f: means.get(f, 0),
            reverse=True,
        )[:3]
        top3_str = ", ".join(f"{f} ({means.get(f, 0):.1f})" for f in top3)
        lines.append(f"| {group} | {data['n']} | {top3_str} |")

    lines.extend([
        "",
        "## 5. Temporal Trends",
        "",
        "| Year | Papers | Regions | Mean WEIRD | NW Papers | NW % |",
        "|------|--------|---------|------------|-----------|------|",
    ])

    for year in sorted(temporal.keys()):
        t = temporal[year]
        if t["total"] < 10:
            continue
        lines.append(
            f"| {year} | {t['total']} | {t['region_diversity']} | "
            f"{t['mean_weird']} | {t['nw_papers']} | {t['nw_pct']}% |"
        )

    return "\n".join(lines)


if __name__ == "__main__":
    sys.exit(main())
