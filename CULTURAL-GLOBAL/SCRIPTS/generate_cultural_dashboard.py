#!/usr/bin/env python3
"""Generate data.js for the Cross-Cultural AI Values Alignment Dashboard.

Reads JSON data files from CULTURAL-GLOBAL/DATA/ and pre-computes all
analytics needed by the 12-tab ECharts dashboard.

Usage:
    python generate_cultural_dashboard.py
"""
from __future__ import annotations

import json
import os
import sys
from collections import Counter, defaultdict
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
SCRIPT_DIR = Path(__file__).resolve().parent
DATA_DIR = SCRIPT_DIR.parent / "DATA"
DASHBOARD_DIR = SCRIPT_DIR.parent / "DASHBOARD"

DATE_PREFIX = "20260403"

# ---------------------------------------------------------------------------
# Load data
# ---------------------------------------------------------------------------

def load_json(name: str) -> dict:
    path = DATA_DIR / f"{DATE_PREFIX}-{name}.json"
    if not path.exists():
        print(f"ERROR: {path} not found", file=sys.stderr)
        sys.exit(1)
    with open(path) as f:
        return json.load(f)


clustering = load_json("clustering-results")
correspondence = load_json("correspondence-analysis")
cross = load_json("cross-cultural-analysis")
author_geo = load_json("author-geography")
nw_scores = load_json("nw-scores")
weird_scores = load_json("weird-scores")
baseline = load_json("baseline-snapshot")

# ---------------------------------------------------------------------------
# Colour palette  (Okabe-Ito colorblind-safe)
# ---------------------------------------------------------------------------
REGION_COLORS = {
    "North America": "#E69F00",
    "Western Europe": "#56B4E9",
    "East Asia": "#009E73",
    "MENA": "#F0E442",
    "South Asia": "#0072B2",
    "Southeast Asia": "#D55E00",
    "Latin America & Caribbean": "#CC79A7",
    "Eastern Europe & Central Asia": "#999999",
    "Oceania": "#332288",
    "Sub-Saharan Africa": "#882255",
    "Unknown": "#666666",
}

REGIONS_ORDERED = [
    "North America", "Western Europe", "East Asia", "MENA", "South Asia",
    "Southeast Asia", "Latin America & Caribbean", "Eastern Europe & Central Asia",
    "Oceania", "Sub-Saharan Africa",
]

NW_FRAMEWORKS = [
    "nw_confucian", "nw_ubuntu", "nw_islamic_ethics",
    "nw_buddhist", "nw_dharmic", "nw_indigenous_relational", "nw_buen_vivir",
]
NW_LABELS = {
    "nw_confucian": "Confucian",
    "nw_ubuntu": "Ubuntu",
    "nw_islamic_ethics": "Islamic Ethics",
    "nw_buddhist": "Buddhist",
    "nw_dharmic": "Dharmic",
    "nw_indigenous_relational": "Indigenous Relational",
    "nw_buen_vivir": "Buen Vivir",
}

WESTERN_FRAMEWORKS = [
    "virtue_ethics", "deontological_ethics", "utilitarian_ethics",
    "care_ethics", "contractarian_ethics",
]
WESTERN_LABELS = {
    "virtue_ethics": "Virtue Ethics",
    "deontological_ethics": "Deontological",
    "utilitarian_ethics": "Utilitarian",
    "care_ethics": "Care Ethics",
    "contractarian_ethics": "Contractarian",
}

RV_FIELDS = [
    "rv_christianity", "rv_islam", "rv_buddhism", "rv_judaism", "rv_hinduism",
    "rv_sikhism", "rv_confucianism", "rv_taoism", "rv_shinto", "rv_jainism",
    "rv_bahai", "rv_zoroastrianism", "rv_ubuntu", "rv_indigenous",
]
RV_LABELS = {
    "rv_christianity": "Christianity", "rv_islam": "Islam",
    "rv_buddhism": "Buddhism", "rv_judaism": "Judaism",
    "rv_hinduism": "Hinduism", "rv_sikhism": "Sikhism",
    "rv_confucianism": "Confucianism", "rv_taoism": "Taoism",
    "rv_shinto": "Shinto", "rv_jainism": "Jainism",
    "rv_bahai": "Baha'i", "rv_zoroastrianism": "Zoroastrianism",
    "rv_ubuntu": "Ubuntu", "rv_indigenous": "Indigenous",
}

MP_FIELDS = [
    "mp_mft", "mp_schwartz", "mp_trolley", "mp_kohlberg",
    "mp_dual_process", "mp_intuitionist", "mp_dyadic", "mp_identity",
]

# ---------------------------------------------------------------------------
# Helper: format label
# ---------------------------------------------------------------------------
def fmt(key: str) -> str:
    """Convert field key to display label."""
    if key in NW_LABELS:
        return NW_LABELS[key]
    if key in WESTERN_LABELS:
        return WESTERN_LABELS[key]
    if key in RV_LABELS:
        return RV_LABELS[key]
    return key.replace("_", " ").replace("mp ", "").title()


# ===========================================================================
# TAB 1: Overview
# ===========================================================================
def build_overview() -> dict:
    total = cross["total_papers"]
    regions = author_geo["region_distribution"]
    # Remove Unknown for display
    region_counts = {k: v for k, v in regions.items() if k != "Unknown"}

    # Country distribution for choropleth
    country_counts: Counter = Counter()
    for p in author_geo["papers"]:
        cc = p.get("author_country", "")
        if cc:
            country_counts[cc] += 1

    # Headline stats
    weird_mean = weird_scores["mean_weird_score"]
    tier_dist = weird_scores["tier_distribution"]
    high_weird_pct = round(tier_dist.get("High-WEIRD (70-100)", 0) / total * 100, 1)
    global_south_n = author_geo["north_south_distribution"].get("Global South", 0)
    global_south_pct = round(global_south_n / total * 100, 1)

    nw_any = sum(nw_scores["field_counts_gte50"].values())

    return {
        "total_papers": total,
        "mean_weird": weird_mean,
        "high_weird_pct": high_weird_pct,
        "global_south_pct": global_south_pct,
        "global_south_n": global_south_n,
        "nw_framework_papers": nw_any,
        "region_counts": region_counts,
        "country_counts": dict(country_counts.most_common()),
        "top_countries": dict(country_counts.most_common(15)),
    }


# ===========================================================================
# TAB 2: Regional Clusters
# ===========================================================================
def build_regional_clusters() -> dict:
    profiles = cross["regional_profiles"]
    # Build radar data: for each region, pick the 12 most-interesting dimensions
    # Use all western + nw frameworks for radar
    radar_dims = WESTERN_FRAMEWORKS + NW_FRAMEWORKS
    radar_labels = [fmt(d) for d in radar_dims]

    radar_series = {}
    for region in REGIONS_ORDERED:
        if region not in profiles:
            continue
        p = profiles[region]
        radar_series[region] = [round(p["mean_scores"].get(d, 0), 2) for d in radar_dims]

    # Heatmap: regions x all frameworks (detection rates)
    all_fw = WESTERN_FRAMEWORKS + NW_FRAMEWORKS
    heatmap_data = []
    for ri, region in enumerate(REGIONS_ORDERED):
        if region not in profiles:
            continue
        dr = profiles[region]["detection_rates"]
        for fi, fw in enumerate(all_fw):
            val = round(dr.get(fw, 0), 1)
            heatmap_data.append([fi, ri, val])

    return {
        "radar_dims": radar_labels,
        "radar_series": radar_series,
        "heatmap_x": [fmt(f) for f in all_fw],
        "heatmap_y": REGIONS_ORDERED,
        "heatmap_data": heatmap_data,
        "region_n": {r: profiles[r]["n"] for r in REGIONS_ORDERED if r in profiles},
    }


# ===========================================================================
# TAB 3: WEIRD Analysis
# ===========================================================================
def build_weird() -> dict:
    tiers = weird_scores["tier_distribution"]
    tier_order = ["Non-WEIRD (0-29)", "Low-WEIRD (30-49)", "Moderate-WEIRD (50-69)", "High-WEIRD (70-100)"]

    # Histogram buckets (0-10, 10-20, ..., 90-100)
    buckets = [0] * 10
    for p in weird_scores["papers"]:
        s = p["weird_score"]
        idx = min(s // 10, 9)
        buckets[idx] += 1

    # Sub-dimension means by tier
    weird_comp = cross["weird_comparison"]
    sub_dims = ["w", "e", "i", "r", "d"]
    sub_dim_labels = ["Western", "Educated", "Industrialized", "Rich", "Democratic"]

    # Compute sub-dim means per tier from paper data
    tier_subdim = {}
    tier_papers = defaultdict(list)
    for p in weird_scores["papers"]:
        tier_papers[p["tier"]].append(p)

    for tier in tier_order:
        papers = tier_papers.get(tier, [])
        if not papers:
            tier_subdim[tier] = [0] * 5
            continue
        means = []
        for d in sub_dims:
            vals = [pp[d] for pp in papers if d in pp]
            means.append(round(sum(vals) / len(vals), 1) if vals else 0)
        tier_subdim[tier] = means

    # WEIRD tier framework comparison
    tier_fw_means = {}
    for tier in tier_order:
        if tier in weird_comp:
            ms = weird_comp[tier]["mean_scores"]
            tier_fw_means[tier] = {
                "western": [round(ms.get(f, 0), 2) for f in WESTERN_FRAMEWORKS],
                "non_western": [round(ms.get(f, 0), 2) for f in NW_FRAMEWORKS],
            }

    return {
        "histogram_buckets": buckets,
        "histogram_labels": [f"{i*10}-{i*10+9}" for i in range(10)],
        "tier_distribution": {t: tiers.get(t, 0) for t in tier_order},
        "tier_order": tier_order,
        "sub_dim_labels": sub_dim_labels,
        "tier_subdim": tier_subdim,
        "tier_fw_means": tier_fw_means,
        "mean_weird": weird_scores["mean_weird_score"],
    }


# ===========================================================================
# TAB 4: North/South
# ===========================================================================
def build_north_south() -> dict:
    ns = cross["north_south_comparison"]
    groups = ["Global North", "Global South", "Ambiguous"]

    fw_all = WESTERN_FRAMEWORKS + NW_FRAMEWORKS
    fw_labels = [fmt(f) for f in fw_all]

    group_means = {}
    for g in groups:
        if g in ns:
            ms = ns[g]["mean_scores"]
            group_means[g] = [round(ms.get(f, 0), 2) for f in fw_all]

    group_n = {g: ns[g]["n"] for g in groups if g in ns}

    # Detection rates for stacked bar
    group_detection = {}
    for g in groups:
        if g not in ns:
            continue
        # re-compute detection rates from paper data
        # Use mean scores as proxy (already available)
        ms = ns[g]["mean_scores"]
        group_detection[g] = {
            "western_total": round(sum(ms.get(f, 0) for f in WESTERN_FRAMEWORKS), 2),
            "nw_total": round(sum(ms.get(f, 0) for f in NW_FRAMEWORKS), 2),
        }

    return {
        "groups": groups,
        "group_n": group_n,
        "fw_labels": fw_labels,
        "group_means": group_means,
        "group_detection": group_detection,
        "ns_distribution": author_geo["north_south_distribution"],
    }


# ===========================================================================
# TAB 5: East/West
# ===========================================================================
def build_east_west() -> dict:
    ew = cross["east_west_comparison"]
    groups = ["East", "West"]
    fw_all = WESTERN_FRAMEWORKS + NW_FRAMEWORKS
    fw_labels = [fmt(f) for f in fw_all]

    group_means = {}
    group_n = {}
    for g in groups:
        if g in ew:
            ms = ew[g]["mean_scores"]
            group_means[g] = [round(ms.get(f, 0), 2) for f in fw_all]
            group_n[g] = ew[g]["n"]

    return {
        "groups": groups,
        "group_n": group_n,
        "fw_labels": fw_labels,
        "group_means": group_means,
    }


# ===========================================================================
# TAB 6: Normative Frameworks
# ===========================================================================
def build_normative() -> dict:
    profiles = cross["regional_profiles"]
    all_fw = WESTERN_FRAMEWORKS + NW_FRAMEWORKS
    fw_labels = [fmt(f) for f in all_fw]

    # Heatmap: regions x frameworks (mean scores)
    heatmap_data = []
    for ri, region in enumerate(REGIONS_ORDERED):
        if region not in profiles:
            continue
        ms = profiles[region]["mean_scores"]
        for fi, fw in enumerate(all_fw):
            val = round(ms.get(fw, 0), 2)
            heatmap_data.append([fi, ri, val])

    # Detection counts
    western_counts = baseline.get("western_frameworks_gte50", {})
    nw_counts = nw_scores.get("field_counts_gte50", {})

    detection = {}
    for fw in WESTERN_FRAMEWORKS:
        detection[fmt(fw)] = western_counts.get(fw, 0)
    for fw in NW_FRAMEWORKS:
        detection[fmt(fw)] = nw_counts.get(fw, 0)

    return {
        "fw_labels": fw_labels,
        "regions": REGIONS_ORDERED,
        "heatmap_data": heatmap_data,
        "detection_counts": detection,
    }


# ===========================================================================
# TAB 7: Religious Traditions
# ===========================================================================
def build_religious() -> dict:
    profiles = cross["regional_profiles"]
    rv_labels = [RV_LABELS[f] for f in RV_FIELDS]

    # Heatmap: regions x traditions (detection rates)
    heatmap_data = []
    for ri, region in enumerate(REGIONS_ORDERED):
        if region not in profiles:
            continue
        dr = profiles[region]["detection_rates"]
        for fi, rv in enumerate(RV_FIELDS):
            val = round(dr.get(rv, 0), 1)
            heatmap_data.append([fi, ri, val])

    # Global detection counts
    rv_counts = baseline.get("religious_traditions_gte50", {})
    detection = {RV_LABELS[k]: v for k, v in rv_counts.items() if k in RV_LABELS}

    return {
        "rv_labels": rv_labels,
        "regions": REGIONS_ORDERED,
        "heatmap_data": heatmap_data,
        "detection_counts": detection,
    }


# ===========================================================================
# TAB 8: Positionality
# ===========================================================================
def build_positionality() -> dict:
    region_dist = author_geo["region_distribution"]
    method_dist = author_geo["method_distribution"]

    # For Sankey: region -> cultural tag (from baseline cultural_distribution)
    cultural_dist = baseline.get("cultural_distribution", {})
    # Top 15 cultural tags excluding N/A
    cultural_top = {k: v for k, v in cultural_dist.items() if k != "N/A"}
    cultural_top = dict(sorted(cultural_top.items(), key=lambda x: -x[1])[:15])

    # Build region -> cultural tag links from paper data
    # We need to join author_geo with baseline cultural tags
    # Since we don't have per-paper cultural tags in author_geo, use region distribution as pie/bar
    # and method distribution as secondary

    return {
        "region_distribution": {k: v for k, v in region_dist.items() if k != "Unknown"},
        "method_distribution": method_dist,
        "ns_distribution": author_geo["north_south_distribution"],
        "cultural_top": cultural_top,
    }


# ===========================================================================
# TAB 9: Temporal Trends
# ===========================================================================
def build_temporal() -> dict:
    trends = cross["temporal_trends"]
    years = sorted(trends.keys())

    # Filter to years with enough data
    years = [y for y in years if trends[y]["total"] >= 5]

    papers_per_year = [trends[y]["total"] for y in years]
    mean_weird = [round(trends[y]["mean_weird"], 1) for y in years]
    nw_pct = [round(trends[y]["nw_pct"], 1) for y in years]
    region_diversity = [trends[y]["region_diversity"] for y in years]

    # Region stacked area
    region_by_year = {}
    for region in REGIONS_ORDERED:
        region_by_year[region] = []
        for y in years:
            region_by_year[region].append(trends[y]["region_counts"].get(region, 0))

    return {
        "years": years,
        "papers_per_year": papers_per_year,
        "mean_weird": mean_weird,
        "nw_pct": nw_pct,
        "region_diversity": region_diversity,
        "region_by_year": region_by_year,
    }


# ===========================================================================
# TAB 10: Gap Analysis
# ===========================================================================
def build_gap_analysis() -> dict:
    profiles = cross["regional_profiles"]

    # Underrepresented regions (< 50 papers)
    underrep = []
    for region in REGIONS_ORDERED:
        if region in profiles and profiles[region]["n"] < 50:
            underrep.append({"region": region, "n": profiles[region]["n"]})
    underrep.sort(key=lambda x: x["n"])

    # Frameworks with low detection
    nw_counts = nw_scores.get("field_counts_gte50", {})
    low_fw = []
    for fw in NW_FRAMEWORKS:
        c = nw_counts.get(fw, 0)
        if c < 20:
            low_fw.append({"framework": fmt(fw), "count": c})
    low_fw.sort(key=lambda x: x["count"])

    # Regions with zero detection for key frameworks
    zero_cells = []
    for region in REGIONS_ORDERED:
        if region not in profiles:
            continue
        dr = profiles[region]["detection_rates"]
        for fw in NW_FRAMEWORKS:
            if dr.get(fw, 0) == 0:
                zero_cells.append({"region": region, "framework": fmt(fw)})

    # Regional concentration index (HHI)
    region_n = {r: profiles[r]["n"] for r in REGIONS_ORDERED if r in profiles}
    total = sum(region_n.values())
    hhi = round(sum((n / total * 100) ** 2 for n in region_n.values()), 1)

    return {
        "underrepresented_regions": underrep,
        "low_detection_frameworks": low_fw,
        "zero_cells": zero_cells[:20],  # cap
        "hhi": hhi,
        "region_n": region_n,
    }


# ===========================================================================
# TAB 11: Literature Landscape
# ===========================================================================
def build_landscape() -> dict:
    # Scatter: WEIRD score (x) vs total NW score (y), colored by region
    points = []
    for wp, np_ in zip(weird_scores["papers"], nw_scores["papers"]):
        fn = wp["filename"]
        ws = wp["weird_score"]
        region = "Unknown"
        # Find region from author_geo
        for ap in author_geo["papers"]:
            if ap["filename"] == fn:
                region = ap.get("author_region", "Unknown")
                break
        nw_total = sum(np_["scores"].values())
        points.append([ws, nw_total, region, fn[:50]])

    # Compute score distributions for box-plot-like data
    fw_distributions = {}
    for fw in NW_FRAMEWORKS:
        vals = [p["scores"][fw] for p in nw_scores["papers"] if p["scores"].get(fw, 0) > 0]
        if vals:
            vals.sort()
            n = len(vals)
            fw_distributions[fmt(fw)] = {
                "count": n,
                "mean": round(sum(vals) / n, 1),
                "median": vals[n // 2],
                "max": vals[-1],
            }

    return {
        "scatter_points": points[:2046],  # all papers
        "fw_distributions": fw_distributions,
    }


# ===========================================================================
# TAB 12: Methods
# ===========================================================================
def build_methods() -> dict:
    return {
        "total_papers": cross["total_papers"],
        "dimensions": cross["dimensions_analyzed"],
        "method_distribution": author_geo["method_distribution"],
        "western_frameworks": [fmt(f) for f in WESTERN_FRAMEWORKS],
        "nw_frameworks": [fmt(f) for f in NW_FRAMEWORKS],
        "rv_traditions": [RV_LABELS[f] for f in RV_FIELDS],
        "mp_frameworks": [f.replace("mp_", "").replace("_", " ").title() for f in MP_FIELDS],
        "weird_sub_dims": ["Western", "Educated", "Industrialized", "Rich", "Democratic"],
    }


# ===========================================================================
# TAB 13: DENDROGRAM
# ===========================================================================
def build_dendrogram_tree() -> dict:
    linkage = clustering["hierarchical_clustering"]["linkage_matrix"]
    regions = clustering["regions"]

    nodes: dict[int, dict] = {}
    for i, region in enumerate(regions):
        nodes[i] = {"name": region, "value": 0}

    for idx, row in enumerate(linkage):
        i, j, dist, size = int(row[0]), int(row[1]), round(row[2], 3), int(row[3])
        new_id = len(regions) + idx
        nodes[new_id] = {
            "name": f"d={dist}",
            "value": dist,
            "children": [nodes[i], nodes[j]],
        }

    root = nodes[len(regions) + len(linkage) - 1]
    return root


# ===========================================================================
# TAB 14: CA BIPLOT
# ===========================================================================
def build_correspondence() -> dict:
    return correspondence


# ===========================================================================
# Assemble and write
# ===========================================================================
def main():
    data = {
        "REGION_COLORS": REGION_COLORS,
        "REGIONS_ORDERED": REGIONS_ORDERED,
        "overview": build_overview(),
        "regional": build_regional_clusters(),
        "weird": build_weird(),
        "north_south": build_north_south(),
        "east_west": build_east_west(),
        "normative": build_normative(),
        "religious": build_religious(),
        "positionality": build_positionality(),
        "temporal": build_temporal(),
        "gap": build_gap_analysis(),
        "landscape": build_landscape(),
        "methods": build_methods(),
        "DENDROGRAM": build_dendrogram_tree(),
        "CORRESPONDENCE": build_correspondence(),
    }

    # Write data.js
    out = DASHBOARD_DIR / "data.js"
    lines = []
    for key, val in data.items():
        lines.append(f"const {key} = {json.dumps(val, ensure_ascii=False)};")

    out.write_text("\n".join(lines), encoding="utf-8")
    size_kb = out.stat().st_size / 1024
    print(f"Wrote {out}  ({size_kb:.1f} KB)")
    print(f"  {len(data)} top-level constants")


if __name__ == "__main__":
    main()
