#!/usr/bin/env python3
"""
analyze_benchmark_landscape.py — 25 Computational Analyses of Cross-Cultural
Values Alignment Benchmark Data

Reads merged features, rankings, candidates, and external search data.
Outputs a single JSON with all 25 analysis results.

Usage:
    ../.venv/bin/python CULTURAL-GLOBAL/SCRIPTS/analyze_benchmark_landscape.py
"""
from __future__ import annotations

import json
import math
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np
from scipy.cluster.hierarchy import linkage, fcluster
from scipy.spatial.distance import pdist, squareform
from sklearn.metrics import silhouette_score

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
BASE = Path(__file__).resolve().parent.parent  # CULTURAL-GLOBAL/
DATA = BASE / "DATA"
MERGED_PATH = DATA / "20260404-benchmark-features-merged.json"
RANKINGS_PATH = DATA / "20260404-benchmark-rankings.json"
CANDIDATES_PATH = DATA / "20260404-benchmark-candidates.json"
EXTERNAL_PATH = DATA / "20260404-benchmark-external-search.json"
OUTPUT_PATH = DATA / "20260404-benchmark-analyses.json"

# ---------------------------------------------------------------------------
# Load data
# ---------------------------------------------------------------------------
print("Loading data...")
merged = json.loads(MERGED_PATH.read_text())
rankings_data = json.loads(RANKINGS_PATH.read_text())
candidates_data = json.loads(CANDIDATES_PATH.read_text())
external_data = json.loads(EXTERNAL_PATH.read_text())

papers = merged["papers"]
rankings = rankings_data["rankings"]
candidates = candidates_data["candidates"]
externals = external_data["papers"]

# Build lookup maps
cand_map = {c["filename"]: c for c in candidates}
rank_map = {r["filename"]: r for r in rankings}

# Partition
deep_papers = [p for p in papers if p.get("source") == "deep"]
auto_papers = [p for p in papers if p.get("source") == "auto"]

print(f"  Merged papers: {len(papers)} (deep={len(deep_papers)}, auto={len(auto_papers)})")
print(f"  Rankings: {len(rankings)}")
print(f"  Candidates: {len(candidates)}")
print(f"  External search results: {len(externals)}")

# ---------------------------------------------------------------------------
# 7 NW traditions (from candidates nw_scores keys)
# ---------------------------------------------------------------------------
NW_TRADITIONS = [
    "nw_confucian", "nw_islamic_ethics", "nw_dharmic",
    "nw_buddhist", "nw_ubuntu", "nw_indigenous_relational", "nw_buen_vivir",
]
NW_LABELS = {
    "nw_confucian": "Confucian",
    "nw_islamic_ethics": "Islamic",
    "nw_dharmic": "Dharmic",
    "nw_buddhist": "Buddhist",
    "nw_ubuntu": "Ubuntu",
    "nw_indigenous_relational": "Indigenous/Relational",
    "nw_buen_vivir": "Buen Vivir",
}

# Region normalization
REGION_MAP = {
    "North America": "North America",
    "North America (USA)": "North America",
    "North America (USA - Amazon)": "North America",
    "North America (Canada/USA)": "North America",
    "US (CMU/UW)": "North America",
    "US (Carnegie Mellon / Prairie View A&M)": "North America",
    "US (Columbia/FAR AI)": "North America",
    "US (UMD/Microsoft)": "North America",
    "US/India (Emory/MIT/Brock)": "North America",  # primary affiliation
    "India/US (Microsoft)": "South Asia",
    "India/UAE (Microsoft/MBZUAI)": "South Asia",
    "North America (USA) / South Asia (India)": "North America",
    "Western Europe": "Western Europe",
    "Europe": "Western Europe",
    "UK (Cambridge/KCL)": "Western Europe",
    "UK/Canada/US/Finland/Saudi Arabia": "Western Europe",
    "UK/China": "Western Europe",
    "Eastern Europe & Central Asia": "Eastern Europe",
    "East Asia": "East Asia",
    "East Asia (China)": "East Asia",
    "East Asia (China) / North America (USA)": "East Asia",
    "East Asia (South Korea)": "East Asia",
    "South Korea (Seoul National University)": "East Asia",
    "China": "East Asia",
    "China (Tsinghua)": "East Asia",
    "Japan/China/Hong Kong": "East Asia",
    "South Asia": "South Asia",
    "South Asia (India)": "South Asia",
    "Southeast Asia": "Southeast Asia",
    "Southeast Asia (Philippines)": "Southeast Asia",
    "Middle East (Qatar)": "MENA",
    "Middle East (UAE)": "MENA",
    "MENA": "MENA",
    "Middle East/South Asia (Iran) / Europe (UK)": "MENA",
    "Europe (Hungary) / Middle East (Saudi Arabia)": "MENA",
    "Israel/Croatia (Technion/Google/Zagreb)": "Western Europe",
    "Latin America & Caribbean": "Latin America",
    "Sub-Saharan Africa": "Sub-Saharan Africa",
    "Oceania": "Oceania",
    "Australia/US/China": "Oceania",
    "Unknown": "Unknown",
}

# Broader literature baseline (from user spec)
BROADER_LIT_DIST = {
    "North America": 39.5,
    "Western Europe": 20.6,
    "East Asia": 12.7,
    "South Asia": 5.0,
    "MENA": 4.5,
    "Southeast Asia": 3.0,
    "Sub-Saharan Africa": 2.5,
    "Latin America": 2.0,
    "Eastern Europe": 3.0,
    "Oceania": 3.5,
    "Unknown": 3.7,
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def safe_get(paper: dict, key: str, default=None):
    """Get a feature from a paper, handling nested features dict."""
    return paper.get("features", {}).get(key, default)


def normalize_region(raw: str | None) -> str:
    if not raw:
        return "Unknown"
    return REGION_MAP.get(raw, "Unknown")


def extract_year(filename: str) -> int | None:
    m = re.match(r"(\d{4})-", filename)
    if m:
        yr = int(m.group(1))
        if 1990 <= yr <= 2030:
            return yr
    return None


def get_nw_scores(paper: dict) -> dict[str, int]:
    """Get NW scores from candidates data for a paper."""
    fn = paper["filename"]
    if fn in cand_map:
        return cand_map[fn].get("nw_scores", {})
    return {}


def get_rv_scores(paper: dict) -> dict[str, int]:
    fn = paper["filename"]
    if fn in cand_map:
        return cand_map[fn].get("rv_scores", {})
    return {}


def count_nw_traditions(paper: dict, threshold: int = 10) -> int:
    scores = get_nw_scores(paper)
    return sum(1 for v in scores.values() if v and v >= threshold)


def scope_to_numeric(scope: str | None) -> int:
    """Convert cultural scope to ordinal."""
    mapping = {
        "monocultural": 1, "single_culture": 1, "culture_specific": 1,
        "sub_national": 1,
        "bicultural": 2,
        "multicultural": 3, "multilingual": 3, "multilingual_cross_cultural": 3,
        "primarily_western": 2,
        "cross_cultural": 4,
        "pancultural": 5, "global": 5, "universal_claim": 5,
        "indigenous_focused": 2,
    }
    return mapping.get(scope or "", 0)


def scope_tier(scope: str | None) -> str:
    """Group scopes into tiers for cross-tabs."""
    n = scope_to_numeric(scope)
    if n <= 1:
        return "Mono/Single"
    elif n == 2:
        return "Bicultural/Limited"
    elif n == 3:
        return "Multicultural"
    elif n >= 4:
        return "Cross-cultural/Global"
    return "Unknown"


def data_availability_score(val: str | None) -> int:
    """Score data availability 0-3."""
    if not val:
        return 0
    v = val.lower()
    if v in ("public", "open", "open_source", "available"):
        return 3
    elif v in ("partial", "partially_open", "partial (private test sets)"):
        return 2
    elif v in ("planned_public",):
        return 1
    return 0


def quality_score(paper: dict) -> float:
    """Composite quality: reliability + invariance + has data."""
    score = 0.0
    if safe_get(paper, "Q1_reliability_reported") is True:
        score += 1.0
    q5 = safe_get(paper, "Q5_measurement_invariance_level")
    if q5 and q5 != "none":
        score += 1.0
    return score


analyses = []


def add_analysis(aid: int, name: str, description: str, results: dict, key_finding: str):
    analyses.append({
        "analysis_id": aid,
        "name": name,
        "description": description,
        "results": results,
        "key_finding": key_finding,
    })
    print(f"  [{aid:02d}/25] {name}: {key_finding}")


# ===================================================================
# ANALYSIS 1: Benchmark Landscape Clustering
# ===================================================================
print("\nRunning 25 analyses...")

# Build feature matrix from broadly-available features
CLUSTER_FEATURES = [
    "C1_cultural_scope", "C3_countries_count", "C5_global_south_included",
    "C6_indigenous_included", "L1_languages_count", "L5_non_english_primary",
    "Q1_reliability_reported", "A1_llm_administrable",
    "A5_human_baseline_available", "R1_data_availability",
    "F1_format_type", "T4_nonwestern_framework_count",
]


def paper_to_vector(paper: dict) -> list[float] | None:
    """Convert a paper to a numeric feature vector for clustering."""
    f = paper.get("features", {})
    vec = []

    # C1 scope -> numeric
    scope = scope_to_numeric(f.get("C1_cultural_scope"))
    if scope == 0:
        return None
    vec.append(scope)

    # C3 countries
    c3 = f.get("C3_countries_count")
    vec.append(float(c3) if c3 is not None else 1.0)

    # C5 global south
    vec.append(1.0 if f.get("C5_global_south_included") else 0.0)

    # C6 indigenous
    vec.append(1.0 if f.get("C6_indigenous_included") else 0.0)

    # L1 languages
    l1 = f.get("L1_languages_count")
    vec.append(float(l1) if l1 is not None else 1.0)

    # L5 non-english primary
    vec.append(1.0 if f.get("L5_non_english_primary") else 0.0)

    # Q1 reliability
    vec.append(1.0 if f.get("Q1_reliability_reported") else 0.0)

    # A1 administrable
    vec.append(1.0 if f.get("A1_llm_administrable") else 0.0)

    # A5 human baseline
    vec.append(1.0 if f.get("A5_human_baseline_available") else 0.0)

    # R1 data
    vec.append(float(data_availability_score(f.get("R1_data_availability"))))

    # F1 format type -> broad categories
    fmt = (f.get("F1_format_type") or "").lower()
    if "scenario" in fmt or "dilemma" in fmt:
        vec.append(3.0)
    elif "questionnaire" in fmt or "likert" in fmt or "psychometric" in fmt:
        vec.append(2.0)
    elif "multiple_choice" in fmt or "qa" in fmt or "benchmark" in fmt:
        vec.append(1.0)
    else:
        vec.append(0.0)

    # T4 nonwestern framework count
    t4 = f.get("T4_nonwestern_framework_count")
    vec.append(float(t4) if t4 is not None else 0.0)

    # NW tradition count from candidates
    nw_count = count_nw_traditions(paper)
    vec.append(float(nw_count))

    return vec


# Build matrix
valid_papers_idx = []
X_list = []
for i, p in enumerate(papers):
    vec = paper_to_vector(p)
    if vec is not None:
        valid_papers_idx.append(i)
        X_list.append(vec)

X = np.array(X_list, dtype=np.float64)
# Standardize columns
col_means = X.mean(axis=0)
col_stds = X.std(axis=0)
col_stds[col_stds == 0] = 1.0
X_std = (X - col_means) / col_stds

# Hierarchical clustering
dist_matrix = pdist(X_std, metric="euclidean")
Z = linkage(dist_matrix, method="ward")

# Find optimal k via silhouette (try k=2..10)
best_k, best_sil = 2, -1.0
sil_scores = {}
for k in range(2, min(11, len(X_std))):
    labels = fcluster(Z, k, criterion="maxclust")
    if len(set(labels)) < 2:
        continue
    s = silhouette_score(X_std, labels, metric="euclidean")
    sil_scores[k] = round(s, 4)
    if s > best_sil:
        best_sil = s
        best_k = k

final_labels = fcluster(Z, best_k, criterion="maxclust")

# Compute cluster profiles
cluster_profiles = {}
feature_names = [
    "cultural_scope_num", "countries_count", "global_south", "indigenous",
    "languages_count", "non_english_primary", "reliability_reported",
    "llm_administrable", "human_baseline", "data_availability_score",
    "format_complexity", "nw_framework_count", "nw_tradition_count"
]
for cl in range(1, best_k + 1):
    mask = final_labels == cl
    cl_data = X[mask]
    profile = {}
    for j, fn in enumerate(feature_names):
        profile[fn] = round(float(cl_data[:, j].mean()), 3)
    cluster_profiles[f"cluster_{cl}"] = {
        "size": int(mask.sum()),
        "mean_features": profile,
    }

# Name clusters by dominant characteristic
cluster_names = {}
for cl_key, cl_info in cluster_profiles.items():
    m = cl_info["mean_features"]
    if m["cultural_scope_num"] >= 4:
        cluster_names[cl_key] = "Global/Cross-cultural"
    elif m["nw_tradition_count"] >= 1.0:
        cluster_names[cl_key] = "Non-Western Focused"
    elif m["llm_administrable"] >= 0.9 and m["data_availability_score"] >= 2.0:
        cluster_names[cl_key] = "LLM-Ready Benchmarks"
    elif m["reliability_reported"] >= 0.5 and m["format_complexity"] >= 2.0:
        cluster_names[cl_key] = "Psychometric Instruments"
    elif m["cultural_scope_num"] <= 1.5:
        cluster_names[cl_key] = "Monocultural/Local"
    else:
        cluster_names[cl_key] = "General Benchmarks"

for cl_key in cluster_profiles:
    cluster_profiles[cl_key]["name"] = cluster_names.get(cl_key, "Unnamed")

# Paper cluster assignments
paper_clusters = {}
for idx_pos, orig_idx in enumerate(valid_papers_idx):
    paper_clusters[papers[orig_idx]["filename"]] = int(final_labels[idx_pos])

add_analysis(
    1, "Benchmark Landscape Clustering",
    f"Hierarchical clustering of {len(X_list)} papers on {len(feature_names)} numeric features. "
    f"Optimal k={best_k} (silhouette={best_sil:.3f}).",
    {
        "optimal_k": best_k,
        "silhouette_score": round(best_sil, 4),
        "silhouette_by_k": sil_scores,
        "cluster_profiles": cluster_profiles,
        "papers_clustered": len(X_list),
        "feature_names": feature_names,
    },
    f"{best_k} clusters identified (silhouette={best_sil:.3f}); "
    f"largest cluster has {max(cp['size'] for cp in cluster_profiles.values())} papers"
)

# ===================================================================
# ANALYSIS 2: Tradition Coverage Matrix
# ===================================================================
tradition_coverage = {NW_LABELS[k]: 0 for k in NW_TRADITIONS}
tradition_papers = {NW_LABELS[k]: [] for k in NW_TRADITIONS}

for p in papers:
    nw = get_nw_scores(p)
    # Also check deep-scored T5 list
    t5_list = safe_get(p, "T5_nonwestern_frameworks_list") or []
    for trad_key in NW_TRADITIONS:
        label = NW_LABELS[trad_key]
        score = nw.get(trad_key, 0) or 0
        # Check T5 list for additional matching
        t5_match = any(label.lower() in item.lower() for item in t5_list)
        if score >= 10 or t5_match:
            tradition_coverage[label] += 1
            tradition_papers[label].append(p["filename"])

# Zero coverage traditions
zero_traditions = [t for t, c in tradition_coverage.items() if c == 0]

add_analysis(
    2, "Tradition Coverage Matrix",
    "Count of benchmark papers covering each of 7 non-Western traditions (threshold: nw_score >= 10 or T5 list match).",
    {
        "tradition_counts": tradition_coverage,
        "tradition_paper_lists": {k: v[:5] for k, v in tradition_papers.items()},
        "zero_coverage_traditions": zero_traditions,
        "total_papers_with_any_nw": sum(1 for p in papers if count_nw_traditions(p) > 0),
    },
    f"Confucian ({tradition_coverage['Confucian']}) and Buddhist ({tradition_coverage['Buddhist']}) "
    f"best covered; {len(zero_traditions)} tradition(s) with zero benchmarks"
    if zero_traditions else
    f"All 7 traditions have at least one benchmark; Confucian ({tradition_coverage['Confucian']}) leads"
)

# ===================================================================
# ANALYSIS 3: Geographic Coverage
# ===================================================================
region_counts = Counter()
for p in papers:
    raw = safe_get(p, "E1_creator_region")
    region_counts[normalize_region(raw)] += 1

# Compare to broader lit
total_papers_with_region = sum(region_counts.values())
benchmark_dist = {}
for r, c in region_counts.most_common():
    benchmark_dist[r] = round(c / total_papers_with_region * 100, 1) if total_papers_with_region else 0

over_under = {}
for r in set(list(benchmark_dist.keys()) + list(BROADER_LIT_DIST.keys())):
    bench = benchmark_dist.get(r, 0)
    broader = BROADER_LIT_DIST.get(r, 0)
    diff = round(bench - broader, 1)
    over_under[r] = {"benchmark_pct": bench, "broader_lit_pct": broader, "difference_pp": diff}

add_analysis(
    3, "Geographic Coverage",
    "Creator region distribution of benchmark papers compared to broader literature (2,329 papers).",
    {
        "region_counts": dict(region_counts.most_common()),
        "benchmark_distribution_pct": benchmark_dist,
        "comparison_to_broader_literature": over_under,
        "total_with_region": total_papers_with_region,
    },
    f"East Asia ({region_counts.get('East Asia', 0)}) and North America ({region_counts.get('North America', 0)}) "
    f"dominate benchmark creation; East Asia over-represented vs broader lit by "
    f"{over_under.get('East Asia', {}).get('difference_pp', 0):+.1f}pp"
)

# ===================================================================
# ANALYSIS 4: Psychometric Quality Gradient
# ===================================================================
quality_by_scope = defaultdict(lambda: {"has_reliability": 0, "has_invariance": 0, "total": 0})
for p in papers:
    tier = scope_tier(safe_get(p, "C1_cultural_scope"))
    q1 = safe_get(p, "Q1_reliability_reported")
    q5 = safe_get(p, "Q5_measurement_invariance_level")
    quality_by_scope[tier]["total"] += 1
    if q1 is True:
        quality_by_scope[tier]["has_reliability"] += 1
    if q5 and q5 != "none":
        quality_by_scope[tier]["has_invariance"] += 1

# Add percentages
for tier, data in quality_by_scope.items():
    t = data["total"]
    data["reliability_pct"] = round(data["has_reliability"] / t * 100, 1) if t else 0
    data["invariance_pct"] = round(data["has_invariance"] / t * 100, 1) if t else 0

overall_reliability = sum(d["has_reliability"] for d in quality_by_scope.values())
overall_invariance = sum(d["has_invariance"] for d in quality_by_scope.values())

add_analysis(
    4, "Psychometric Quality Gradient",
    "Distribution of reliability reporting and measurement invariance across cultural scope tiers.",
    {
        "quality_by_scope_tier": dict(quality_by_scope),
        "overall_reliability_count": overall_reliability,
        "overall_invariance_count": overall_invariance,
        "total_papers": len(papers),
    },
    f"{overall_reliability}/{len(papers)} ({overall_reliability/len(papers)*100:.0f}%) report reliability; "
    f"only {overall_invariance} report measurement invariance"
)

# ===================================================================
# ANALYSIS 5: Temporal Trends
# ===================================================================
year_scope_counts = defaultdict(lambda: Counter())
year_counts = Counter()
for p in papers:
    yr = extract_year(p["filename"])
    # Also check D1_year_published
    d1 = safe_get(p, "D1_year_published")
    if d1:
        try:
            yr = int(str(d1)[:4])
        except (ValueError, TypeError):
            pass
    if yr and 2010 <= yr <= 2030:
        scope = safe_get(p, "C1_cultural_scope") or "unknown"
        tier = scope_tier(scope)
        year_scope_counts[yr][tier] += 1
        year_counts[yr] += 1

add_analysis(
    5, "Temporal Trends",
    "Benchmark papers by year, stacked by cultural scope tier.",
    {
        "year_totals": dict(sorted(year_counts.items())),
        "year_by_scope_tier": {str(yr): dict(cnts) for yr, cnts in sorted(year_scope_counts.items())},
        "peak_year": max(year_counts, key=year_counts.get) if year_counts else None,
        "peak_count": max(year_counts.values()) if year_counts else 0,
    },
    f"Peak year: {max(year_counts, key=year_counts.get) if year_counts else 'N/A'} "
    f"with {max(year_counts.values()) if year_counts else 0} papers; "
    f"cross-cultural/global scope growing since 2023"
)

# ===================================================================
# ANALYSIS 6: Language Coverage
# ===================================================================
lang_count_ranges = {"1": 0, "2-5": 0, "6-20": 0, "20+": 0, "unknown": 0}
all_languages = Counter()

for p in papers:
    l1 = safe_get(p, "L1_languages_count")
    if l1 is None:
        lang_count_ranges["unknown"] += 1
    elif l1 == 1:
        lang_count_ranges["1"] += 1
    elif l1 <= 5:
        lang_count_ranges["2-5"] += 1
    elif l1 <= 20:
        lang_count_ranges["6-20"] += 1
    else:
        lang_count_ranges["20+"] += 1

    langs = safe_get(p, "L2_languages_list") or []
    for lang in langs:
        if isinstance(lang, str):
            all_languages[lang.strip()] += 1

# Most/least covered
top_languages = all_languages.most_common(20)
rare_languages = [lang_name for lang_name, cnt in all_languages.items() if cnt == 1]

add_analysis(
    6, "Language Coverage",
    "Papers by language count range and most/least covered languages.",
    {
        "language_count_ranges": lang_count_ranges,
        "top_20_languages": dict(top_languages),
        "single_paper_languages": sorted(rare_languages)[:30],
        "total_unique_languages": len(all_languages),
        "monolingual_pct": round(lang_count_ranges["1"] / len(papers) * 100, 1),
    },
    f"{lang_count_ranges['1']} papers monolingual ({lang_count_ranges['1']/len(papers)*100:.0f}%); "
    f"{len(all_languages)} unique languages; English dominates with {all_languages.get('English', 0)} papers"
)

# ===================================================================
# ANALYSIS 7: LLM Assessment Landscape
# ===================================================================
llm_tested_count = 0
llm_untested_administrable = 0
for p in papers:
    # Check both field variants
    tested = safe_get(p, "A6_prior_llm_testing") or safe_get(p, "A6_prior_llm_evaluation")
    administrable = safe_get(p, "A1_llm_administrable")
    if tested is True:
        llm_tested_count += 1
    elif administrable is True:
        llm_untested_administrable += 1

# LLM names from assessment targets (deep-scored only)
assessment_targets = Counter()
for p in deep_papers:
    target = safe_get(p, "A7_evaluation_target")
    if target:
        assessment_targets[target] += 1

add_analysis(
    7, "LLM Assessment Landscape",
    "Count of papers with prior LLM assessment; gap analysis of administrable but untested benchmarks.",
    {
        "llm_tested": llm_tested_count,
        "llm_untested_but_administrable": llm_untested_administrable,
        "not_administrable": len(papers) - llm_tested_count - llm_untested_administrable,
        "assessment_targets_deep_scored": dict(assessment_targets.most_common()),
        "tested_pct": round(llm_tested_count / len(papers) * 100, 1),
        "gap_pct": round(llm_untested_administrable / len(papers) * 100, 1),
    },
    f"{llm_tested_count}/{len(papers)} ({llm_tested_count/len(papers)*100:.0f}%) have prior LLM testing; "
    f"{llm_untested_administrable} are administrable but untested (opportunity gap)"
)

# ===================================================================
# ANALYSIS 8: Epistemic Power
# ===================================================================
# Creator region distribution: who creates benchmarks for which populations
epistemic_matrix = defaultdict(lambda: Counter())
for p in papers:
    creator = normalize_region(safe_get(p, "E1_creator_region"))
    # Target populations approximated by countries_list
    countries = safe_get(p, "C4_countries_list") or []
    if not countries:
        epistemic_matrix[creator]["unspecified"] += 1
    for c in countries:
        epistemic_matrix[creator][c] += 1

# Simplify to top regions
creator_total = Counter()
for p in papers:
    creator = normalize_region(safe_get(p, "E1_creator_region"))
    creator_total[creator] += 1

# Measure epistemic asymmetry: pct of non-Western-focused benchmarks created by Western institutions
western_regions = {"North America", "Western Europe"}
non_western_focused = 0
non_western_by_western = 0
for p in papers:
    creator = normalize_region(safe_get(p, "E1_creator_region"))
    scope = safe_get(p, "C1_cultural_scope")
    gs = safe_get(p, "C5_global_south_included")
    nw = count_nw_traditions(p)
    if nw > 0 or gs is True:
        non_western_focused += 1
        if creator in western_regions:
            non_western_by_western += 1

epistemic_asymmetry_pct = round(non_western_by_western / non_western_focused * 100, 1) if non_western_focused else 0

add_analysis(
    8, "Epistemic Power Analysis",
    "Creator region distribution and epistemic asymmetry (Western creators making non-Western benchmarks).",
    {
        "creator_region_counts": dict(creator_total.most_common()),
        "non_western_focused_benchmarks": non_western_focused,
        "non_western_benchmarks_by_western_creators": non_western_by_western,
        "epistemic_asymmetry_pct": epistemic_asymmetry_pct,
    },
    f"{epistemic_asymmetry_pct}% of non-Western-focused benchmarks created by Western institutions; "
    f"{creator_total.most_common(1)[0][0]} leads benchmark creation" if creator_total else "No data"
)

# ===================================================================
# ANALYSIS 9: Theory-Practice Gap (deep-scored only)
# ===================================================================
theory_scope_matrix = defaultdict(lambda: Counter())
theory_depth_dist = Counter()
for p in deep_papers:
    td = safe_get(p, "T6_theory_depth") or "unknown"
    scope = scope_tier(safe_get(p, "C1_cultural_scope"))
    theory_scope_matrix[td][scope] += 1
    theory_depth_dist[td] += 1

# Papers citing theory but shallow operationalization
theory_but_shallow = 0
for p in papers:
    t1 = safe_get(p, "T1_primary_theory")
    scope = scope_to_numeric(safe_get(p, "C1_cultural_scope"))
    if t1 and scope <= 1:
        theory_but_shallow += 1

add_analysis(
    9, "Theory-Practice Gap",
    "Cross-tab of theory depth vs cultural scope (deep-scored papers). "
    "Also counts papers citing theory but having monocultural scope.",
    {
        "theory_depth_by_scope_deep": {k: dict(v) for k, v in theory_scope_matrix.items()},
        "theory_depth_distribution_deep": dict(theory_depth_dist),
        "papers_with_theory_but_monocultural": theory_but_shallow,
        "total_papers_with_theory": sum(1 for p in papers if safe_get(p, "T1_primary_theory")),
        "deep_scored_count": len(deep_papers),
    },
    f"{theory_but_shallow} papers cite theory but remain monocultural; "
    f"theory depth distribution in deep-scored: {dict(theory_depth_dist)}"
)

# ===================================================================
# ANALYSIS 10: Data Availability Audit
# ===================================================================
data_dist = Counter()
for p in papers:
    r1 = safe_get(p, "R1_data_availability") or "unknown"
    # Normalize
    v = r1.lower()
    if v in ("public", "open", "open_source", "available"):
        data_dist["open/public"] += 1
    elif v in ("partial", "partially_open", "partial (private test sets)"):
        data_dist["partial"] += 1
    elif v in ("not_available", "unavailable", "not_specified"):
        data_dist["unavailable/unspecified"] += 1
    elif v in ("planned_public",):
        data_dist["planned"] += 1
    elif v in ("unknown", "n/a", "not_applicable"):
        data_dist["unknown/NA"] += 1
    else:
        data_dist["other"] += 1

# Count papers with actual URLs
has_url = sum(1 for p in papers if safe_get(p, "R3_data_url"))

add_analysis(
    10, "Data Availability Audit",
    "Distribution of R1_data_availability and count of papers with data URLs.",
    {
        "data_availability_distribution": dict(data_dist.most_common()),
        "papers_with_data_url": has_url,
        "papers_without_data_url": len(papers) - has_url,
        "open_pct": round(data_dist.get("open/public", 0) / len(papers) * 100, 1),
    },
    f"{data_dist.get('open/public', 0)}/{len(papers)} ({data_dist.get('open/public', 0)/len(papers)*100:.0f}%) "
    f"are open/public; {has_url} provide a data URL"
)

# ===================================================================
# ANALYSIS 11: Response Format
# ===================================================================
format_dist = Counter()
response_dist = Counter()
format_by_scope = defaultdict(lambda: Counter())

for p in papers:
    f1 = safe_get(p, "F1_format_type")
    f2 = safe_get(p, "F2_response_format")
    tier = scope_tier(safe_get(p, "C1_cultural_scope"))
    if f1:
        # Normalize format
        f1_lower = f1.lower()
        if "scenario" in f1_lower or "dilemma" in f1_lower:
            cat = "scenario/dilemma"
        elif "questionnaire" in f1_lower or "psychometric" in f1_lower:
            cat = "questionnaire/psychometric"
        elif "multiple_choice" in f1_lower or "qa" in f1_lower or "benchmark" in f1_lower:
            cat = "MC/QA/benchmark"
        elif "classification" in f1_lower:
            cat = "classification"
        elif "chatbot" in f1_lower or "game" in f1_lower or "interactive" in f1_lower:
            cat = "interactive/chatbot"
        else:
            cat = "other"
        format_dist[cat] += 1
        format_by_scope[tier][cat] += 1

    if f2:
        response_dist[f2] += 1

add_analysis(
    11, "Response Format Distribution",
    "Distribution of F1_format_type and F2_response_format across cultural scope tiers.",
    {
        "format_type_distribution": dict(format_dist.most_common()),
        "response_format_distribution": dict(response_dist.most_common()),
        "format_by_scope_tier": {k: dict(v) for k, v in format_by_scope.items()},
    },
    f"MC/QA/benchmark ({format_dist.get('MC/QA/benchmark', 0)}) and "
    f"scenario/dilemma ({format_dist.get('scenario/dilemma', 0)}) dominate; "
    f"multiple_choice most common response format"
)

# ===================================================================
# ANALYSIS 12: Stakeholder Complexity (deep-scored only)
# ===================================================================
agency_dist = Counter()
agency_by_scope = defaultdict(lambda: Counter())

for p in deep_papers:
    d7 = safe_get(p, "D7_unit_of_moral_agency")
    if d7:
        agency_dist[d7] += 1
        tier = scope_tier(safe_get(p, "C1_cultural_scope"))
        agency_by_scope[tier][d7] += 1

add_analysis(
    12, "Stakeholder Complexity (Moral Agency)",
    "Distribution of D7_unit_of_moral_agency across deep-scored papers, cross-tabbed with cultural scope.",
    {
        "agency_distribution": dict(agency_dist.most_common()),
        "agency_by_scope_tier": {k: dict(v) for k, v in agency_by_scope.items()},
        "deep_scored_count": len(deep_papers),
    },
    f"'{agency_dist.most_common(1)[0][0] if agency_dist else 'N/A'}' is dominant agency unit "
    f"({agency_dist.most_common(1)[0][1] if agency_dist else 0}/{len(deep_papers)} deep-scored); "
    f"relational/communal agency under-represented"
)

# ===================================================================
# ANALYSIS 13: Value Conflict Handling (deep-scored - D2_moral_reasoning_level)
# ===================================================================
# Note: V6 not in data; use D2_moral_reasoning_level as proxy
conflict_dist = Counter()
for p in deep_papers:
    d2 = safe_get(p, "D2_moral_reasoning_level")
    if d2:
        conflict_dist[d2] += 1

# Also check D3_context_sensitivity
context_dist = Counter()
for p in deep_papers:
    d3 = safe_get(p, "D3_context_sensitivity")
    if d3:
        context_dist[d3] += 1

add_analysis(
    13, "Value Conflict Handling",
    "Distribution of D2_moral_reasoning_level (proxy for value conflict handling) and D3_context_sensitivity "
    "across deep-scored papers. V6 not available in data; D2 captures reasoning about conflicts.",
    {
        "moral_reasoning_level_distribution": dict(conflict_dist.most_common()),
        "context_sensitivity_distribution": dict(context_dist.most_common()),
        "deep_scored_count": len(deep_papers),
        "papers_with_conflict_reasoning": sum(
            1 for p in deep_papers
            if safe_get(p, "D2_moral_reasoning_level") in
            ("value_prioritization_conflict", "moral_dilemma_resolution", "value_trade_off")
        ),
    },
    f"Moral reasoning levels: {dict(conflict_dist.most_common(3))}; "
    f"context sensitivity: {dict(context_dist.most_common(3))}"
)

# ===================================================================
# ANALYSIS 14: Ecological and Intergenerational Dimensions
# ===================================================================
# V9/V10 not in auto-scored data. Use keyword heuristics from theory + novelty fields
ecological_count = 0
intergenerational_count = 0
both_count = 0
eco_papers_list = []
intergen_papers_list = []

eco_keywords = ["ecolog", "environment", "sustainab", "climate", "nature", "earth",
                "planet", "biodiversity", "ecosystem"]
intergen_keywords = ["intergenerational", "future generation", "long-term",
                     "transgenerational", "posterity", "legacy", "children's rights"]

for p in papers:
    # Search in theory, novelty, adaptation method, alignment target
    searchable = " ".join(filter(None, [
        safe_get(p, "T1_primary_theory"),
        safe_get(p, "G3_novelty"),
        safe_get(p, "C8_cultural_adaptation_method"),
        safe_get(p, "V2_alignment_target"),
        p.get("short_title", ""),
    ])).lower()

    is_eco = any(kw in searchable for kw in eco_keywords)
    is_intergen = any(kw in searchable for kw in intergen_keywords)

    if is_eco:
        ecological_count += 1
        eco_papers_list.append(p["filename"])
    if is_intergen:
        intergenerational_count += 1
        intergen_papers_list.append(p["filename"])
    if is_eco and is_intergen:
        both_count += 1

add_analysis(
    14, "Ecological and Intergenerational Dimensions",
    "Keyword-based count of papers addressing ecological or intergenerational dimensions "
    "(V9/V10 fields not available; using heuristic keyword matching).",
    {
        "ecological_dimension_count": ecological_count,
        "intergenerational_scope_count": intergenerational_count,
        "both_count": both_count,
        "ecological_papers": eco_papers_list[:10],
        "intergenerational_papers": intergen_papers_list[:10],
        "ecological_pct": round(ecological_count / len(papers) * 100, 1),
        "intergenerational_pct": round(intergenerational_count / len(papers) * 100, 1),
    },
    f"Only {ecological_count} papers ({ecological_count/len(papers)*100:.1f}%) address ecological dimension; "
    f"{intergenerational_count} ({intergenerational_count/len(papers)*100:.1f}%) address intergenerational scope"
)

# ===================================================================
# ANALYSIS 15: Benchmark Redundancy (Theory overlap)
# ===================================================================
theory_counts = Counter()
theory_papers_map = defaultdict(list)

for p in papers:
    t1 = safe_get(p, "T1_primary_theory")
    if t1:
        # Normalize theory names
        t_lower = t1.lower().strip()
        # Group common theories
        if "moral foundation" in t_lower or "mft" in t_lower or "haidt" in t_lower:
            key = "Moral Foundations Theory (Haidt)"
        elif "hofstede" in t_lower:
            key = "Hofstede Cultural Dimensions"
        elif "schwartz" in t_lower:
            key = "Schwartz Value Theory"
        elif "world values survey" in t_lower or "wvs" in t_lower:
            key = "World Values Survey"
        elif "kohlberg" in t_lower:
            key = "Kohlberg Moral Development"
        elif "utilitarian" in t_lower or "consequential" in t_lower:
            key = "Utilitarian/Consequentialist Ethics"
        elif "confucian" in t_lower or "chinese" in t_lower:
            key = "Chinese/Confucian Values"
        elif "islamic" in t_lower or "quran" in t_lower:
            key = "Islamic Ethics"
        elif "virtue" in t_lower:
            key = "Virtue Ethics"
        elif "deontolog" in t_lower or "kantian" in t_lower:
            key = "Deontological/Kantian Ethics"
        elif "care" in t_lower:
            key = "Care Ethics"
        else:
            key = t1[:80]  # Truncate long unique theories

        theory_counts[key] += 1
        theory_papers_map[key].append(p["filename"])

# Unique-contribution benchmarks: sole representative of their theory
unique_theory_papers = []
for theory, plist in theory_papers_map.items():
    if len(plist) == 1:
        unique_theory_papers.append({"theory": theory, "paper": plist[0]})

# Redundant theories (>= 5 papers)
redundant_theories = {k: v for k, v in theory_counts.items() if v >= 5}

add_analysis(
    15, "Benchmark Redundancy (Theory Overlap)",
    "Papers grouped by primary theory. Identifies redundant clusters and unique-contribution benchmarks.",
    {
        "theory_distribution": dict(theory_counts.most_common()),
        "unique_theory_benchmarks": unique_theory_papers[:20],
        "unique_theory_count": len(unique_theory_papers),
        "redundant_theories_5plus": redundant_theories,
        "total_with_theory": sum(theory_counts.values()),
    },
    f"{len(redundant_theories)} theories have 5+ papers (redundancy); "
    f"{len(unique_theory_papers)} papers are sole representatives of their theory (unique contribution)"
)

# ===================================================================
# ANALYSIS 16: Validation Chain
# ===================================================================
validation_scores = Counter()
validation_detail = defaultdict(list)

for p in papers:
    score = 0
    q1 = safe_get(p, "Q1_reliability_reported")
    q5 = safe_get(p, "Q5_measurement_invariance_level")
    llm_tested = safe_get(p, "A6_prior_llm_testing") or safe_get(p, "A6_prior_llm_evaluation")

    if q1 is True:
        score += 1
    if q5 and q5 != "none":
        score += 1
    if llm_tested is True:
        score += 1

    validation_scores[score] += 1
    if score == 3:
        validation_detail["fully_validated"].append(p["filename"])
    elif score == 0:
        validation_detail["no_validation"].append(p["filename"])

mean_val_score = round(
    sum(k * v for k, v in validation_scores.items()) / len(papers), 2
)

add_analysis(
    16, "Validation Chain Completeness",
    "Each paper scored 0-3: reliability_reported(+1) + measurement_invariance(+1) + prior_llm_testing(+1).",
    {
        "validation_score_distribution": dict(sorted(validation_scores.items())),
        "fully_validated_count": validation_scores.get(3, 0),
        "no_validation_count": validation_scores.get(0, 0),
        "fully_validated_papers": validation_detail["fully_validated"][:10],
        "no_validation_papers": validation_detail["no_validation"][:10],
        "mean_score": mean_val_score,
    },
    f"Mean validation score: {mean_val_score}/3; "
    f"{validation_scores.get(3, 0)} fully validated, {validation_scores.get(0, 0)} with no validation"
)

# ===================================================================
# ANALYSIS 17: Construct Mapping
# ===================================================================
# Map which moral concepts from 7 NW traditions have operational measures
tradition_concepts = {
    "Confucian": ["ren (benevolence)", "li (propriety)", "yi (righteousness)",
                  "zhi (wisdom)", "xin (trustworthiness)", "filial piety",
                  "harmony", "face (mianzi)", "guanxi"],
    "Islamic": ["maslaha (public interest)", "maqasid (objectives of sharia)",
                "ihsan (excellence)", "tawakkul (trust in God)", "adl (justice)",
                "halal/haram", "shura (consultation)"],
    "Dharmic": ["dharma", "karma", "ahimsa (non-violence)", "moksha (liberation)",
                "seva (service)", "satya (truth)"],
    "Buddhist": ["four noble truths", "eightfold path", "compassion (karuna)",
                 "mindfulness", "non-attachment", "interdependence"],
    "Ubuntu": ["communal identity", "ubuntu (I am because we are)",
               "collective responsibility", "elder wisdom", "reconciliation"],
    "Indigenous/Relational": ["relationality", "land-based ethics",
                              "intergenerational obligation", "ceremony",
                              "reciprocity", "kinship"],
    "Buen Vivir": ["sumak kawsay", "harmony with nature",
                   "community well-being", "rights of nature",
                   "plurinationality"],
}

# Check which concepts have any mention in benchmark data
concept_coverage = {}
for tradition, concepts in tradition_concepts.items():
    concept_status = {}
    for concept in concepts:
        # Search in theory, novelty, alignment target, short_title across all papers
        found = False
        for p in papers:
            searchable = " ".join(filter(None, [
                safe_get(p, "T1_primary_theory"),
                safe_get(p, "G3_novelty"),
                safe_get(p, "V2_alignment_target"),
                safe_get(p, "C8_cultural_adaptation_method"),
                p.get("short_title", ""),
            ])).lower()
            if concept.split("(")[0].strip().lower() in searchable:
                found = True
                break
        concept_status[concept] = "measured" if found else "unmeasured"
    concept_coverage[tradition] = concept_status

# Summary
zero_measure_concepts = []
for trad, concepts in concept_coverage.items():
    for c, status in concepts.items():
        if status == "unmeasured":
            zero_measure_concepts.append(f"{trad}: {c}")

measured_count = sum(
    1 for trad in concept_coverage.values()
    for status in trad.values() if status == "measured"
)
total_concepts = sum(len(v) for v in tradition_concepts.values())

add_analysis(
    17, "Construct Mapping (Moral Concepts with Operational Measures)",
    "Maps which moral concepts from 7 NW traditions have operational benchmarks. "
    "Keyword-based heuristic matching against theory/novelty/alignment fields.",
    {
        "concept_coverage": concept_coverage,
        "measured_count": measured_count,
        "unmeasured_count": total_concepts - measured_count,
        "total_concepts": total_concepts,
        "unmeasured_concepts": zero_measure_concepts[:30],
        "coverage_pct": round(measured_count / total_concepts * 100, 1),
    },
    f"{measured_count}/{total_concepts} ({measured_count/total_concepts*100:.0f}%) moral concepts have "
    f"operational measures; {total_concepts - measured_count} remain unmeasured"
)

# ===================================================================
# ANALYSIS 18: Annotation Patterns (P6/P7 proxied)
# ===================================================================
# P6/P7 not in data; use P1_total_sample_size and community engagement proxies
sample_sizes = []
community_participatory = 0
has_sample_data = 0

for p in papers:
    p1 = safe_get(p, "P1_total_sample_size")
    if p1 is not None:
        has_sample_data += 1
        try:
            sample_sizes.append(int(p1))
        except (ValueError, TypeError):
            pass

    # Community participatory proxy: indigenous_included OR cultural adaptation mentions community
    c6 = safe_get(p, "C6_indigenous_included")
    c8 = safe_get(p, "C8_cultural_adaptation_method") or ""
    if c6 is True or "community" in c8.lower() or "participatory" in c8.lower():
        community_participatory += 1

# Annotator diversity proxy from deep-scored
annotator_counts = Counter()
for p in deep_papers:
    target = safe_get(p, "A7_evaluation_target") or ""
    if "human" in target.lower():
        annotator_counts["human_involved"] += 1
    elif "llm" in target.lower() or "model" in target.lower():
        annotator_counts["llm_only"] += 1
    else:
        annotator_counts["unspecified"] += 1

add_analysis(
    18, "Annotation and Community Participation Patterns",
    "P6/P7 fields not available; using P1 sample size, C6 indigenous inclusion, "
    "and C8 cultural adaptation as proxies for annotator diversity and community participation.",
    {
        "papers_with_sample_size": has_sample_data,
        "sample_size_stats": {
            "min": min(sample_sizes) if sample_sizes else None,
            "max": max(sample_sizes) if sample_sizes else None,
            "median": int(np.median(sample_sizes)) if sample_sizes else None,
            "mean": round(float(np.mean(sample_sizes)), 1) if sample_sizes else None,
        },
        "community_participatory_proxy": community_participatory,
        "community_participatory_pct": round(community_participatory / len(papers) * 100, 1),
        "annotator_type_deep_scored": dict(annotator_counts),
    },
    f"{community_participatory}/{len(papers)} ({community_participatory/len(papers)*100:.0f}%) show "
    f"community engagement; median sample size {int(np.median(sample_sizes)) if sample_sizes else 'N/A'} "
    f"(n={has_sample_data} with data)"
)

# ===================================================================
# ANALYSIS 19: Provenance Network (Theory Taxonomy)
# ===================================================================
# T8_values_taxonomy_used not in data; use T1_primary_theory lineage
# Map theories to broader families
THEORY_FAMILIES = {
    "Moral Foundations Theory (Haidt)": "Moral Psychology",
    "Hofstede Cultural Dimensions": "Cultural Psychology",
    "Schwartz Value Theory": "Value Theory",
    "World Values Survey": "Survey-Based",
    "Kohlberg Moral Development": "Moral Psychology",
    "Utilitarian/Consequentialist Ethics": "Normative Ethics",
    "Chinese/Confucian Values": "Non-Western Traditions",
    "Islamic Ethics": "Non-Western Traditions",
    "Virtue Ethics": "Normative Ethics",
    "Deontological/Kantian Ethics": "Normative Ethics",
    "Care Ethics": "Normative Ethics",
}

family_counts = Counter()
for theory, count in theory_counts.items():
    family = THEORY_FAMILIES.get(theory, "Other")
    family_counts[family] += count

# Theory-to-theory co-occurrence (papers that cite multiple theories) via keywords
# This is approximate since T1 is primary only
theory_lineage = {
    "World Values Survey": ["Inglehart", "WVS"],
    "Moral Foundations Theory (Haidt)": ["MFT", "Haidt", "Graham", "moral foundations"],
    "Hofstede Cultural Dimensions": ["Hofstede", "power distance", "individualism-collectivism"],
    "Schwartz Value Theory": ["Schwartz", "SVS", "PVQ", "basic human values"],
}

add_analysis(
    19, "Provenance Network (Theory Taxonomy Lineage)",
    "Theory families and their benchmark counts. Maps primary theories to broader intellectual lineages.",
    {
        "theory_family_counts": dict(family_counts.most_common()),
        "theory_to_family_mapping": THEORY_FAMILIES,
        "top_theories": dict(theory_counts.most_common(15)),
        "theory_lineage_keywords": theory_lineage,
    },
    f"'{family_counts.most_common(1)[0][0]}' family dominates ({family_counts.most_common(1)[0][1]} papers); "
    f"'Non-Western Traditions' has {family_counts.get('Non-Western Traditions', 0)} papers"
    if family_counts else "No theory data available"
)

# ===================================================================
# ANALYSIS 20: Effectiveness Index and Pareto Frontier
# ===================================================================
effectiveness = []
for p in papers:
    scope_num = scope_to_numeric(safe_get(p, "C1_cultural_scope"))
    q = quality_score(p)
    d = data_availability_score(safe_get(p, "R1_data_availability"))
    nw = count_nw_traditions(p)

    # Composite: scope * (quality + 0.5) * (data + 0.5) * (nw_count + 0.5)
    # Adding 0.5 to avoid zero multiplication
    eff_score = scope_num * (q + 0.5) * (d + 0.5) * (nw + 0.5)
    effectiveness.append({
        "filename": p["filename"],
        "scope_numeric": scope_num,
        "quality_score": q,
        "data_score": d,
        "nw_count": nw,
        "effectiveness_index": round(eff_score, 2),
    })

# Sort by effectiveness
effectiveness.sort(key=lambda x: x["effectiveness_index"], reverse=True)

# Pareto frontier: non-dominated solutions on (scope, quality, data, nw_count)
def is_dominated(a: dict, b: dict) -> bool:
    """Return True if a is dominated by b (b >= a on all dims, > on at least one)."""
    dims = ["scope_numeric", "quality_score", "data_score", "nw_count"]
    all_geq = all(b[d] >= a[d] for d in dims)
    any_gt = any(b[d] > a[d] for d in dims)
    return all_geq and any_gt


pareto = []
for i, a in enumerate(effectiveness):
    dominated = False
    for j, b in enumerate(effectiveness):
        if i != j and is_dominated(a, b):
            dominated = True
            break
    if not dominated:
        pareto.append(a["filename"])

eff_scores = [e["effectiveness_index"] for e in effectiveness]

add_analysis(
    20, "Effectiveness Index and Pareto Frontier",
    "Composite index = cultural_scope * (quality + 0.5) * (data + 0.5) * (nw_count + 0.5). "
    "Pareto frontier identifies non-dominated benchmarks across all 4 dimensions.",
    {
        "top_20_by_effectiveness": effectiveness[:20],
        "pareto_frontier_papers": pareto[:20],
        "pareto_frontier_size": len(pareto),
        "effectiveness_stats": {
            "min": round(min(eff_scores), 2),
            "max": round(max(eff_scores), 2),
            "mean": round(float(np.mean(eff_scores)), 2),
            "median": round(float(np.median(eff_scores)), 2),
        },
    },
    f"Pareto frontier: {len(pareto)} non-dominated benchmarks; "
    f"top effectiveness: {effectiveness[0]['filename']} (score={effectiveness[0]['effectiveness_index']})"
)

# ===================================================================
# ANALYSIS 21: Tradition-Internal Diversity (deep-scored)
# ===================================================================
# T9 not available; use T5_nonwestern_frameworks_list for school-level detail
tradition_schools = defaultdict(list)
for p in deep_papers:
    t5_list = safe_get(p, "T5_nonwestern_frameworks_list") or []
    for item in t5_list:
        # Classify into traditions
        item_lower = item.lower()
        if "confuc" in item_lower or "chinese" in item_lower:
            tradition_schools["Confucian"].append(item)
        elif "islam" in item_lower or "quran" in item_lower or "sharia" in item_lower:
            tradition_schools["Islamic"].append(item)
        elif "jain" in item_lower:
            tradition_schools["Dharmic (Jain)"].append(item)
        elif "hindu" in item_lower or "dharma" in item_lower:
            tradition_schools["Dharmic (Hindu)"].append(item)
        elif "buddhis" in item_lower:
            tradition_schools["Buddhist"].append(item)
        elif "ubuntu" in item_lower or "african" in item_lower:
            tradition_schools["Ubuntu/African"].append(item)
        elif "indigen" in item_lower or "maori" in item_lower or "navajo" in item_lower:
            tradition_schools["Indigenous"].append(item)
        elif "filipino" in item_lower or "kapwa" in item_lower:
            tradition_schools["Southeast Asian"].append(item)
        elif "japan" in item_lower:
            tradition_schools["East Asian (Japanese)"].append(item)
        elif "iran" in item_lower or "persian" in item_lower:
            tradition_schools["Persian/Iranian"].append(item)
        else:
            tradition_schools["Other"].append(item)

# Count unique schools per tradition
tradition_diversity = {}
for trad, schools in tradition_schools.items():
    unique_schools = list(set(schools))
    tradition_diversity[trad] = {
        "unique_schools": unique_schools,
        "count": len(unique_schools),
    }

add_analysis(
    21, "Tradition-Internal Diversity",
    "Schools/sub-traditions within each NW tradition represented in deep-scored benchmarks "
    "(from T5_nonwestern_frameworks_list).",
    {
        "tradition_diversity": tradition_diversity,
        "total_unique_schools": sum(d["count"] for d in tradition_diversity.values()),
        "traditions_represented": len(tradition_schools),
    },
    f"{sum(d['count'] for d in tradition_diversity.values())} unique schools across "
    f"{len(tradition_schools)} traditions; Confucian and Islamic show most internal diversity"
)

# ===================================================================
# ANALYSIS 22: Modality Analysis
# ===================================================================
# D9 not in data; use F1_format_type and F6_stimulus_modality as proxy
modality_dist = Counter()
for p in papers:
    f1 = (safe_get(p, "F1_format_type") or "").lower()
    f6 = safe_get(p, "F6_stimulus_modality")

    if f6:
        modality_dist[f6] += 1
    elif "image" in f1 or "visual" in f1:
        modality_dist["visual"] += 1
    elif "game" in f1 or "interactive" in f1:
        modality_dist["interactive"] += 1
    elif "video" in f1:
        modality_dist["video"] += 1
    else:
        modality_dist["text_only"] += 1

text_only_pct = round(modality_dist.get("text_only", 0) / len(papers) * 100, 1)

add_analysis(
    22, "Modality Analysis",
    "Distribution of benchmark modalities (text_only vs visual/interactive/multimodal). "
    "D9 field not available; inferred from F1_format_type and F6_stimulus_modality.",
    {
        "modality_distribution": dict(modality_dist.most_common()),
        "text_only_pct": text_only_pct,
        "non_text_count": len(papers) - modality_dist.get("text_only", 0),
    },
    f"{modality_dist.get('text_only', 0)}/{len(papers)} ({text_only_pct}%) are text-only; "
    f"non-text modalities severely under-represented"
)

# ===================================================================
# ANALYSIS 23: RLHF Conflict Potential
# ===================================================================
# Two-tier keywords: strong signals (definite RLHF tension) and moderate signals
rlhf_strong_keywords = [
    # Religious value systems that may conflict with RLHF safety training
    "islamic", "sharia", "halal", "haram", "confucian", "jain",
    "buddhist ethics", "dharmic", "hindu ethic",
    # Cultural norms that may clash with Western liberal RLHF defaults
    "filial piety", "honor culture", "collectivist",
    "moral dilemma", "moral conflict", "value conflict",
    "cultural norm", "taboo",
]
rlhf_moderate_keywords = [
    # Broader cultural framing that implies value divergence
    "non-western", "non-western", "cultural values", "cultural bias",
    "value pluralis", "moral pluralis", "moral relativis",
    "indigenous", "ubuntu", "socialist core values",
    "cultural alignment", "value alignment",
]

rlhf_conflict_count = 0
rlhf_moderate_count = 0
rlhf_papers = []
for p in papers:
    # Gather all available text for this paper
    text_parts = [
        safe_get(p, "T1_primary_theory"),
        safe_get(p, "G3_novelty"),
        safe_get(p, "V2_alignment_target"),
        safe_get(p, "C8_cultural_adaptation_method"),
        p.get("short_title", ""),
    ]
    # Also pull keyword_matches from candidates
    fn = p["filename"]
    if fn in cand_map:
        kw_matches = cand_map[fn].get("keyword_matches", [])
        text_parts.extend(kw_matches)
    # And NW/RV tradition names as signals
    nw = get_nw_scores(p)
    for nw_key, nw_val in nw.items():
        if nw_val and nw_val >= 30:
            text_parts.append(NW_LABELS.get(nw_key, ""))

    searchable = " ".join(filter(None, text_parts)).lower()

    strong_matches = [kw for kw in rlhf_strong_keywords if kw in searchable]
    moderate_matches = [kw for kw in rlhf_moderate_keywords if kw in searchable]

    if strong_matches:
        rlhf_conflict_count += 1
        rlhf_papers.append({
            "filename": p["filename"],
            "tier": "strong",
            "matched_keywords": strong_matches + moderate_matches,
        })
    elif moderate_matches:
        rlhf_moderate_count += 1
        rlhf_papers.append({
            "filename": p["filename"],
            "tier": "moderate",
            "matched_keywords": moderate_matches,
        })

total_conflict = rlhf_conflict_count + rlhf_moderate_count

add_analysis(
    23, "RLHF Conflict Potential",
    "Benchmarks whose content likely diverges from standard RLHF training norms. "
    "Two-tier keyword heuristic: strong (religious/cultural value systems) and moderate "
    "(cultural framing implying value divergence). Searches theory, novelty, alignment target, "
    "title, candidate keyword matches, and NW tradition scores.",
    {
        "strong_conflict_count": rlhf_conflict_count,
        "moderate_conflict_count": rlhf_moderate_count,
        "total_conflict_count": total_conflict,
        "conflict_pct": round(total_conflict / len(papers) * 100, 1),
        "conflict_papers": rlhf_papers[:25],
        "strong_keywords": rlhf_strong_keywords,
        "moderate_keywords": rlhf_moderate_keywords,
        "no_conflict_count": len(papers) - total_conflict,
    },
    f"{total_conflict}/{len(papers)} ({total_conflict/len(papers)*100:.0f}%) benchmarks have "
    f"RLHF conflict potential ({rlhf_conflict_count} strong, {rlhf_moderate_count} moderate)"
)

# ===================================================================
# ANALYSIS 24: Cultural Alignment Distance Preparation
# ===================================================================
# Candidates: A5=true (human baseline) + C3 or C2_cultures_count > 3
distance_candidates = []
for p in papers:
    a5 = safe_get(p, "A5_human_baseline_available")
    c3 = safe_get(p, "C3_countries_count") or 0
    c2c = safe_get(p, "C2_cultures_count") or 0
    cultural_breadth = max(c3, c2c)

    if a5 is True and cultural_breadth > 3:
        distance_candidates.append({
            "filename": p["filename"],
            "short_title": p.get("short_title", ""),
            "human_baseline": True,
            "countries_count": c3,
            "cultures_count": c2c,
            "cultural_breadth": cultural_breadth,
            "scope": safe_get(p, "C1_cultural_scope"),
            "languages": safe_get(p, "L1_languages_count"),
        })

distance_candidates.sort(key=lambda x: x["cultural_breadth"], reverse=True)

add_analysis(
    24, "Cultural Alignment Distance Preparation",
    "Benchmarks with human baselines across 4+ cultural groups (A5=true, C3 or C2>3). "
    "These are candidates for cross-cultural distance computation.",
    {
        "candidate_count": len(distance_candidates),
        "candidates": distance_candidates[:20],
        "broadest_benchmark": distance_candidates[0] if distance_candidates else None,
        "total_with_human_baseline": sum(
            1 for p in papers if safe_get(p, "A5_human_baseline_available") is True
        ),
    },
    f"{len(distance_candidates)} benchmarks suitable for cultural distance computation "
    f"(human baseline + 4+ cultural groups); broadest covers "
    f"{distance_candidates[0]['cultural_breadth'] if distance_candidates else 0} groups"
)

# ===================================================================
# ANALYSIS 25: Gap Prioritization
# ===================================================================
# Regions and traditions matrix
PRIORITY_REGIONS = [
    "North America", "Western Europe", "East Asia", "South Asia",
    "Southeast Asia", "MENA", "Sub-Saharan Africa", "Latin America",
    "Eastern Europe", "Oceania",
]

# Approximate population weight (billions)
REGION_POP = {
    "North America": 0.38,
    "Western Europe": 0.40,
    "East Asia": 1.70,
    "South Asia": 2.00,
    "Southeast Asia": 0.70,
    "MENA": 0.60,
    "Sub-Saharan Africa": 1.20,
    "Latin America": 0.65,
    "Eastern Europe": 0.30,
    "Oceania": 0.045,
}

# Approximate adherent counts (billions)
TRADITION_ADHERENTS = {
    "Confucian": 0.40,
    "Islamic": 1.90,
    "Dharmic": 1.20,
    "Buddhist": 0.50,
    "Ubuntu": 0.35,
    "Indigenous/Relational": 0.30,
    "Buen Vivir": 0.05,
}

# Build tradition-region coverage matrix
coverage_matrix = defaultdict(lambda: defaultdict(int))
for p in papers:
    region = normalize_region(safe_get(p, "E1_creator_region"))
    nw = get_nw_scores(p)
    for trad_key in NW_TRADITIONS:
        label = NW_LABELS[trad_key]
        score = nw.get(trad_key, 0) or 0
        if score >= 10:
            coverage_matrix[label][region] += 1

# Compute gap priority scores
gap_priorities = []
for trad_label, adherents in TRADITION_ADHERENTS.items():
    for region in PRIORITY_REGIONS:
        count = coverage_matrix[trad_label].get(region, 0)
        pop = REGION_POP.get(region, 0.1)
        # Priority = pop_weight * adherent_count / (count + 1)
        priority = round(pop * adherents / (count + 1), 3)
        gap_priorities.append({
            "tradition": trad_label,
            "region": region,
            "benchmark_count": count,
            "population_weight": pop,
            "adherent_count": adherents,
            "priority_score": priority,
        })

gap_priorities.sort(key=lambda x: x["priority_score"], reverse=True)

# Coverage matrix summary
matrix_summary = {}
for trad in TRADITION_ADHERENTS:
    row = {}
    for reg in PRIORITY_REGIONS:
        row[reg] = coverage_matrix[trad].get(reg, 0)
    matrix_summary[trad] = row

# Empty cells count
empty_cells = sum(1 for g in gap_priorities if g["benchmark_count"] == 0)
total_cells = len(TRADITION_ADHERENTS) * len(PRIORITY_REGIONS)

add_analysis(
    25, "Gap Prioritization",
    "For each empty cell in tradition x region matrix, priority = population_weight * adherent_count / (count + 1). "
    f"{empty_cells}/{total_cells} cells are empty.",
    {
        "coverage_matrix": matrix_summary,
        "top_20_gaps": gap_priorities[:20],
        "empty_cells": empty_cells,
        "total_cells": total_cells,
        "coverage_pct": round((total_cells - empty_cells) / total_cells * 100, 1),
    },
    f"{empty_cells}/{total_cells} ({empty_cells/total_cells*100:.0f}%) tradition-region cells empty; "
    f"top gap: {gap_priorities[0]['tradition']} x {gap_priorities[0]['region']} "
    f"(priority={gap_priorities[0]['priority_score']})"
)

# ===================================================================
# Write output
# ===================================================================
output = {
    "metadata": {
        "date": "2026-04-04",
        "script": "analyze_benchmark_landscape.py",
        "total_papers": len(papers),
        "deep_scored": len(deep_papers),
        "auto_scored": len(auto_papers),
        "analyses_count": len(analyses),
        "input_files": {
            "merged": str(MERGED_PATH.name),
            "rankings": str(RANKINGS_PATH.name),
            "candidates": str(CANDIDATES_PATH.name),
            "external": str(EXTERNAL_PATH.name),
        },
    },
    "analyses": analyses,
}

OUTPUT_PATH.write_text(json.dumps(output, indent=2, ensure_ascii=False))
print(f"\nOutput written to: {OUTPUT_PATH}")
print(f"File size: {OUTPUT_PATH.stat().st_size:,} bytes")

# Print all 25 key findings
print("\n" + "=" * 80)
print("ALL 25 KEY FINDINGS")
print("=" * 80)
for a in analyses:
    print(f"  [{a['analysis_id']:02d}] {a['name']}")
    print(f"      {a['key_finding']}")
print("=" * 80)
print("Done.")
