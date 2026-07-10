#!/usr/bin/env python3
"""
compute_rankings.py — Merge deep-scored benchmark features and compute
composite rankings using TOPSIS methodology with ELECTRE III veto.

Inputs:
  - 20260404-benchmark-features.json         (auto-scored, 200 papers)
  - 20260404-benchmark-features-deep-batch1.json (deep-scored, top 25)
  - 20260404-benchmark-features-deep-batch2.json (deep-scored, papers 26-50)
  - 20260404-benchmark-candidates.json        (original relevance scores)

Outputs:
  - 20260404-benchmark-features-merged.json   (merged auto+deep features)
  - 20260404-benchmark-rankings.json          (TOPSIS-based composite rankings)

Usage:
  ../.venv/bin/python CULTURAL-GLOBAL/SCRIPTS/compute_rankings.py
"""
from __future__ import annotations

import json
import math
import sys
from pathlib import Path
from typing import Any

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
DATA_DIR = Path(__file__).resolve().parent.parent / "DATA"
AUTO_FILE = DATA_DIR / "20260404-benchmark-features.json"
DEEP1_FILE = DATA_DIR / "20260404-benchmark-features-deep-batch1.json"
DEEP2_FILE = DATA_DIR / "20260404-benchmark-features-deep-batch2.json"
CAND_FILE = DATA_DIR / "20260404-benchmark-candidates.json"
MERGED_OUT = DATA_DIR / "20260404-benchmark-features-merged.json"
RANKINGS_OUT = DATA_DIR / "20260404-benchmark-rankings.json"


# ---------------------------------------------------------------------------
# Categorical → numeric conversion tables
# ---------------------------------------------------------------------------
CULTURAL_SCOPE_MAP: dict[str, float] = {
    "monocultural": 1, "single_culture": 1, "sub_national": 1,
    "culture_specific": 2, "primarily_western": 2, "indigenous_focused": 2,
    "bicultural": 3,
    "multicultural": 4, "multilingual": 4, "cross_cultural": 4,
    "multilingual_cross_cultural": 4,
    "pancultural": 5, "global": 5,
    "universal_claim": 4,
}

EVALUATION_DEPTH_MAP: dict[str, float] = {
    "shallow": 1, "conceptual": 1,
    "moderate": 2,
    "comprehensive": 3, "high": 3,
    "deep_reasoning": 3,  # not seen yet, but spec asks for it
    "philosophical_engagement": 4, "meta-evaluation": 4, "meta-analysis": 4,
    "meta_ethical": 5,
}

# "surface_keyword" from spec not present in data; map shallow→1 covers it
DATA_AVAILABILITY_MAP: dict[str, float] = {
    "unavailable": 0, "not_available": 0, "not_applicable": 0,
    "N/A": 0, "not_specified": 0, "unknown": 0,
    "upon_request": 1, "planned_public": 1,
    "restricted_access": 2, "commercial": 2, "partial": 2,
    "partially_open": 2, "partial (private test sets)": 2,
    "available": 3, "public": 3,
    "open_source": 4, "open": 4,
}

LLM_ADMIN_MAP: dict[str, float] = {
    "no": 0, "false": 0, "False": 0,
    "partial": 1, "likely": 1, "unknown": 0.5,
    "yes": 2, "true": 2, "True": 2,
}

THEORY_DEPTH_MAP: dict[str, float] = {
    "atheoretical": 0, "none": 0,
    "citation_only": 1, "shallow": 1,
    "operationalized": 2, "moderate": 2,
    "extended": 3, "deep": 3, "high": 3,
    "novel_synthesis": 4,
}

MEASUREMENT_INVARIANCE_MAP: dict[str, float] = {
    "none": 0,
    "configural": 1,
    "metric": 2,
    "scalar": 3,
    "strict": 4,
}

NOVELTY_MAP: dict[str, float] = {
    "replication": 1, "low": 1,
    "extension": 2, "moderate": 2,
    "new_construct": 3, "high": 3,
    "new_methodology": 4,
    "paradigm_shift": 5,
}

ALIGNMENT_RELEVANCE_MAP: dict[str, float] = {
    "none": 0, "tangential": 1,
    "indirect": 2, "low": 1,
    "moderate": 2,
    "direct": 3, "high": 3,
}

CONTEXT_SENSITIVITY_MAP: dict[str, float] = {
    "low": 1,
    "moderate": 2,
    "high": 3,
    "very_high": 4,
}

MORAL_REASONING_MAP: dict[str, float] = {
    "none": 0, "N/A": 0, "N/A (linguistic)": 0,
    "knowledge_retrieval": 1, "cultural_knowledge": 1,
    "cultural_representation": 1, "opinion_representation": 1,
    "low": 1, "social_norm_judgment": 1,
    "knowledge_and_alignment": 2, "knowledge_grounding_and_abstention": 2,
    "moral_judgment": 2, "value_alignment": 2, "value_preference_selection": 2,
    "moderate": 2, "construct_validity_analysis": 2,
    "moral_judgment_classification_response": 2, "moral_judgment_with_explanation": 2,
    "moral_reasoning": 3, "moral_reasoning_with_justification": 3,
    "high": 3, "value_conflict_resolution": 3,
    "value_prioritization_conflict": 3,
    "full_pipeline (perception_to_consequence)": 4,
}


# ---------------------------------------------------------------------------
# TOPSIS dimension definitions (feature → dimension mapping + weights)
# ---------------------------------------------------------------------------
# Each dimension maps to a list of (feature_key, converter) pairs
# and has a weight and a benefit direction (True = higher is better)

def _to_float(val: Any) -> float:
    """Convert a value to float. Booleans, ints, strings."""
    if val is None:
        return 0.0
    if isinstance(val, bool):
        return 1.0 if val else 0.0
    if isinstance(val, (int, float)):
        return float(val)
    s = str(val).strip().lower()
    if s in ("true", "yes"):
        return 1.0
    if s in ("false", "no", "", "n/a", "none", "unknown", "not_applicable",
             "not_available", "not_specified"):
        return 0.0
    try:
        return float(s)
    except (ValueError, TypeError):
        return 0.0


def _map_cat(val: Any, mapping: dict[str, float]) -> float:
    """Map a categorical value using a lookup table."""
    if val is None:
        return 0.0
    s = str(val).strip()
    # Try exact match first, then lowercase
    if s in mapping:
        return mapping[s]
    sl = s.lower()
    for k, v in mapping.items():
        if k.lower() == sl:
            return v
    # Long novelty strings from deep scoring — try to infer
    if "paradigm" in sl:
        return 5.0
    if "first" in sl or "only" in sl or "novel" in sl:
        return 4.0
    if "high" in sl:
        return 3.0
    if "moderate" in sl:
        return 2.0
    return 0.0


# Dimension specifications: (dimension_name, [(feature_key, converter), ...], weight, is_benefit)
DIMENSION_SPECS: list[tuple[str, list[tuple[str, Any]], float, bool]] = [
    # Values alignment relevance (V1, V2, alignment_relevance)
    ("alignment_relevance", [
        ("V1_alignment_relevance", lambda v: _map_cat(v, ALIGNMENT_RELEVANCE_MAP)),
        ("V2_alignment_target", lambda v: 1.0 if v and str(v).strip() not in ("", "None", "null") else 0.0),
    ], 0.20, True),

    # Cross-cultural scope (C1, C2, C3, C5, C6, L1)
    ("cross_cultural_scope", [
        ("C1_cultural_scope", lambda v: _map_cat(v, CULTURAL_SCOPE_MAP)),
        ("C2_cultures_count", lambda v: min(_to_float(v), 10.0)),  # cap at 10
        ("C3_countries_count", lambda v: min(_to_float(v), 20.0)),  # cap at 20
        ("C5_global_south_included", _to_float),
        ("C6_indigenous_included", _to_float),
        ("L1_languages_count", lambda v: min(_to_float(v), 15.0)),  # cap at 15
    ], 0.20, True),

    # Non-Western framework coverage (T4, T5, G1)
    ("nonwestern_coverage", [
        ("T4_nonwestern_framework_count", lambda v: min(_to_float(v), 5.0)),
        ("T5_nonwestern_frameworks_list", lambda v: min(float(len(v)), 5.0) if isinstance(v, list) else (1.0 if v and str(v).strip() not in ("", "None", "null", "[]") else 0.0)),
        ("G1_tradition_gap_filled", lambda v: 1.0 if v and str(v).strip() not in ("", "None", "null") else 0.0),
    ], 0.15, True),

    # LLM administrability (A1, A5, A6)
    ("llm_administrability", [
        ("A1_llm_administrable", lambda v: _map_cat(v, LLM_ADMIN_MAP)),
        ("A5_human_baseline_available", _to_float),
        # Handle both deep (A6_prior_llm_evaluation) and auto (A6_prior_llm_testing)
        ("A6_prior_llm_evaluation", _to_float),
    ], 0.12, True),

    # Psychometric quality (Q1, Q5)
    ("psychometric_quality", [
        ("Q1_reliability_reported", _to_float),
        ("Q5_measurement_invariance_level", lambda v: _map_cat(v, MEASUREMENT_INVARIANCE_MAP)),
    ], 0.10, True),

    # Evaluation depth (D1, D2, D3, D7)
    ("evaluation_depth", [
        ("D1_evaluation_depth", lambda v: _map_cat(v, EVALUATION_DEPTH_MAP)),
        ("D2_moral_reasoning_level", lambda v: _map_cat(v, MORAL_REASONING_MAP)),
        ("D3_context_sensitivity", lambda v: _map_cat(v, CONTEXT_SENSITIVITY_MAP)),
        ("D7_unit_of_moral_agency", lambda v: 1.0 if v and str(v).strip().lower() in ("model", "llm", "ai_system") else 0.5),
    ], 0.10, True),

    # Data availability (R1, R3)
    ("data_availability", [
        ("R1_data_availability", lambda v: _map_cat(v, DATA_AVAILABILITY_MAP)),
        ("R3_data_url", lambda v: 1.0 if v and str(v).strip() not in ("", "None", "null") else 0.0),
    ], 0.08, True),

    # Epistemic provenance (E1)
    ("epistemic_provenance", [
        ("E1_creator_region", lambda v: _score_epistemic(v)),
    ], 0.05, True),
]


def _score_epistemic(val: Any) -> float:
    """Score epistemic provenance — non-Western/Global South origin scores higher."""
    if val is None:
        return 0.0
    s = str(val).lower()
    # Multi-region (collaborative) is highest
    if "/" in s or "," in s or "+" in s:
        return 3.0
    # Non-Western regions score higher
    nw_indicators = ["asia", "africa", "latin", "middle east", "south",
                     "china", "india", "korea", "japan", "brazil",
                     "iran", "turkey", "indonesia", "arab"]
    for ind in nw_indicators:
        if ind in s:
            return 2.0
    # Western but named region
    if s.strip():
        return 1.0
    return 0.0


# ---------------------------------------------------------------------------
# Step 1: Merge features (deep overrides auto)
# ---------------------------------------------------------------------------
def load_json(path: Path) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def merge_features() -> list[dict]:
    """Merge auto + deep features. Deep overrides auto where both exist."""
    auto_data = load_json(AUTO_FILE)
    deep1_data = load_json(DEEP1_FILE)
    deep2_data = load_json(DEEP2_FILE)

    # Build deep feature index by filename
    deep_index: dict[str, dict] = {}
    for paper in deep1_data["papers"]:
        deep_index[paper["filename"]] = paper
    for paper in deep2_data["papers"]:
        deep_index[paper["filename"]] = paper

    merged_papers: list[dict] = []
    for auto_paper in auto_data["papers"]:
        fname = auto_paper["filename"]
        merged = {
            "filename": fname,
            "short_title": auto_paper.get("short_title", ""),
            "relevance_score": auto_paper.get("relevance_score", 0),
            "features": dict(auto_paper.get("features", {})),  # copy
            "source": "auto",
        }

        if fname in deep_index:
            deep_paper = deep_index[fname]
            # Deep features override auto features
            for key, val in deep_paper["features"].items():
                merged["features"][key] = val
            merged["source"] = "deep"
            merged["relevance_score"] = deep_paper.get("relevance_score",
                                                        merged["relevance_score"])
            if "scoring_notes" in deep_paper:
                merged["scoring_notes"] = deep_paper["scoring_notes"]
            if "confidence" in deep_paper:
                merged["confidence"] = deep_paper["confidence"]

        # Also add deep-only papers not in auto (batch2 had 18 not in auto)
        merged_papers.append(merged)

    # Add deep papers not in auto set
    auto_names = {p["filename"] for p in auto_data["papers"]}
    for fname, deep_paper in deep_index.items():
        if fname not in auto_names:
            merged_papers.append({
                "filename": fname,
                "short_title": deep_paper.get("short_title", ""),
                "relevance_score": deep_paper.get("relevance_score", 0),
                "features": dict(deep_paper.get("features", {})),
                "source": "deep_only",
                "scoring_notes": deep_paper.get("scoring_notes", ""),
                "confidence": deep_paper.get("confidence", ""),
            })

    return merged_papers


def save_merged(papers: list[dict]) -> None:
    """Write the merged features JSON."""
    deep_count = sum(1 for p in papers if p.get("source") in ("deep", "deep_only"))
    auto_count = sum(1 for p in papers if p.get("source") == "auto")

    output = {
        "metadata": {
            "date": "2026-04-04",
            "total_papers": len(papers),
            "deep_scored": deep_count,
            "auto_scored_only": auto_count,
            "merge_strategy": "deep overrides auto where both exist",
        },
        "papers": papers,
    }
    with open(MERGED_OUT, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    print(f"Merged features written: {MERGED_OUT}")
    print(f"  Total: {len(papers)}, Deep: {deep_count}, Auto-only: {auto_count}")


# ---------------------------------------------------------------------------
# Step 2: TOPSIS computation
# ---------------------------------------------------------------------------
def extract_dimension_scores(paper: dict) -> dict[str, float]:
    """Extract raw dimensional scores for a paper by aggregating features."""
    features = paper.get("features", {})
    dim_scores: dict[str, float] = {}

    for dim_name, feat_specs, _weight, _is_benefit in DIMENSION_SPECS:
        components: list[float] = []
        for feat_key, converter in feat_specs:
            val = features.get(feat_key)
            # Handle auto-file's A6_prior_llm_testing vs deep-file's A6_prior_llm_evaluation
            if feat_key == "A6_prior_llm_evaluation" and val is None:
                val = features.get("A6_prior_llm_testing")
            components.append(converter(val))

        # Aggregate: average of components, normalized to [0, 1] is done later
        # For now, just sum so we preserve magnitude
        dim_scores[dim_name] = sum(components)

    return dim_scores


def compute_topsis(papers: list[dict]) -> list[dict]:
    """
    Full TOPSIS computation:
    1. Build decision matrix
    2. Vector-normalize each column
    3. Apply weights
    4. Determine ideal best/worst
    5. Euclidean distances
    6. TOPSIS score
    """
    n = len(papers)
    dim_names = [spec[0] for spec in DIMENSION_SPECS]
    weights = [spec[2] for spec in DIMENSION_SPECS]
    is_benefit = [spec[3] for spec in DIMENSION_SPECS]
    m = len(dim_names)

    # Step a: Build decision matrix
    matrix: list[list[float]] = []
    for paper in papers:
        scores = extract_dimension_scores(paper)
        row = [scores[d] for d in dim_names]
        matrix.append(row)

    # Step b: Vector normalization
    norm_matrix: list[list[float]] = [[0.0] * m for _ in range(n)]
    for j in range(m):
        col_sum_sq = sum(matrix[i][j] ** 2 for i in range(n))
        denom = math.sqrt(col_sum_sq) if col_sum_sq > 0 else 1.0
        for i in range(n):
            norm_matrix[i][j] = matrix[i][j] / denom

    # Step c: Apply weights
    weighted: list[list[float]] = [[0.0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            weighted[i][j] = norm_matrix[i][j] * weights[j]

    # Step d: Ideal best (A+) and ideal worst (A-)
    a_plus: list[float] = []
    a_minus: list[float] = []
    for j in range(m):
        col_vals = [weighted[i][j] for i in range(n)]
        if is_benefit[j]:
            a_plus.append(max(col_vals))
            a_minus.append(min(col_vals))
        else:
            a_plus.append(min(col_vals))
            a_minus.append(max(col_vals))

    # Step e: Euclidean distances
    d_plus: list[float] = []
    d_minus: list[float] = []
    for i in range(n):
        dp = math.sqrt(sum((weighted[i][j] - a_plus[j]) ** 2 for j in range(m)))
        dm = math.sqrt(sum((weighted[i][j] - a_minus[j]) ** 2 for j in range(m)))
        d_plus.append(dp)
        d_minus.append(dm)

    # Step f: TOPSIS score
    topsis_scores: list[float] = []
    for i in range(n):
        denom = d_plus[i] + d_minus[i]
        score = d_minus[i] / denom if denom > 0 else 0.0
        topsis_scores.append(score)

    # Build results with dimensional scores
    results: list[dict] = []
    for i, paper in enumerate(papers):
        dim_raw = extract_dimension_scores(paper)
        results.append({
            "index": i,
            "filename": paper["filename"],
            "short_title": paper.get("short_title", ""),
            "relevance_score": paper.get("relevance_score", 0),
            "topsis_score": round(topsis_scores[i], 6),
            "dimensional_scores": {d: round(dim_raw[d], 4) for d in dim_names},
            "weighted_normalized": {dim_names[j]: round(weighted[i][j], 6) for j in range(m)},
            "d_plus": round(d_plus[i], 6),
            "d_minus": round(d_minus[i], 6),
            "source": paper.get("source", "unknown"),
        })

    # Sort by TOPSIS score descending
    results.sort(key=lambda x: x["topsis_score"], reverse=True)

    # Assign ranks
    for rank, r in enumerate(results, 1):
        r["rank"] = rank

    return results


# ---------------------------------------------------------------------------
# Step 3: ELECTRE III veto
# ---------------------------------------------------------------------------
def apply_veto(results: list[dict], papers_by_name: dict[str, dict]) -> list[dict]:
    """
    ELECTRE III veto: monocultural AND T4=0 AND C5=false
    Mark but do not remove.
    """
    for r in results:
        fname = r["filename"]
        paper = papers_by_name.get(fname, {})
        features = paper.get("features", {})

        c1 = str(features.get("C1_cultural_scope", "")).lower()
        is_mono = c1 in ("monocultural", "single_culture", "sub_national")

        t4 = _to_float(features.get("T4_nonwestern_framework_count"))
        c5 = _to_float(features.get("C5_global_south_included"))

        veto = is_mono and t4 == 0 and c5 == 0
        r["veto_flag"] = veto

    return results


# ---------------------------------------------------------------------------
# Step 4: Sensitivity analysis
# ---------------------------------------------------------------------------
def perturb_weights(base_weights: list[float], boost_idx: int,
                    factor: float = 0.20) -> list[float]:
    """
    Increase weight at boost_idx by factor, decrease others proportionally.
    Returns a new weight vector summing to 1.0.
    """
    new_w = list(base_weights)
    delta = new_w[boost_idx] * factor
    new_w[boost_idx] += delta
    # Redistribute loss across other dimensions
    remaining_indices = [i for i in range(len(new_w)) if i != boost_idx]
    total_others = sum(new_w[i] for i in remaining_indices)
    if total_others > 0:
        for i in remaining_indices:
            new_w[i] -= delta * (new_w[i] / total_others)
    # Normalize to exactly 1.0
    s = sum(new_w)
    return [w / s for w in new_w]


def run_topsis_with_weights(papers: list[dict],
                            custom_weights: list[float]) -> list[dict]:
    """Run TOPSIS with custom weights, return ranked results."""
    dim_names = [spec[0] for spec in DIMENSION_SPECS]
    is_benefit = [spec[3] for spec in DIMENSION_SPECS]
    m = len(dim_names)
    n = len(papers)

    # Build matrix
    matrix: list[list[float]] = []
    for paper in papers:
        scores = extract_dimension_scores(paper)
        matrix.append([scores[d] for d in dim_names])

    # Normalize
    norm_matrix: list[list[float]] = [[0.0] * m for _ in range(n)]
    for j in range(m):
        col_sum_sq = sum(matrix[i][j] ** 2 for i in range(n))
        denom = math.sqrt(col_sum_sq) if col_sum_sq > 0 else 1.0
        for i in range(n):
            norm_matrix[i][j] = matrix[i][j] / denom

    # Weight
    weighted: list[list[float]] = [[0.0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            weighted[i][j] = norm_matrix[i][j] * custom_weights[j]

    # Ideal solutions
    a_plus: list[float] = []
    a_minus: list[float] = []
    for j in range(m):
        col_vals = [weighted[i][j] for i in range(n)]
        if is_benefit[j]:
            a_plus.append(max(col_vals))
            a_minus.append(min(col_vals))
        else:
            a_plus.append(min(col_vals))
            a_minus.append(max(col_vals))

    # Distances + scores
    scores: list[tuple[int, float]] = []
    for i in range(n):
        dp = math.sqrt(sum((weighted[i][j] - a_plus[j]) ** 2 for j in range(m)))
        dm = math.sqrt(sum((weighted[i][j] - a_minus[j]) ** 2 for j in range(m)))
        denom = dp + dm
        s = dm / denom if denom > 0 else 0.0
        scores.append((i, s))

    # Sort and rank
    scores.sort(key=lambda x: x[1], reverse=True)
    rank_map: dict[int, int] = {}
    for rank, (idx, _) in enumerate(scores, 1):
        rank_map[idx] = rank

    return [{"index": idx, "rank": rank_map[idx]} for idx in range(n)]


def sensitivity_analysis(papers: list[dict], base_results: list[dict]) -> tuple[list[dict], float]:
    """
    Run 5 sensitivity schemes (boost each of top-5-weighted dimensions by +20%)
    and one scheme with -20% on the heaviest dimension.
    Report rank stability for top 15.
    """
    base_weights = [spec[2] for spec in DIMENSION_SPECS]
    dim_names = [spec[0] for spec in DIMENSION_SPECS]

    # Build index map from base results
    fname_to_base_rank: dict[str, int] = {}
    for r in base_results:
        fname_to_base_rank[r["filename"]] = r["rank"]

    # 5 perturbation schemes: boost each of the top-5 weighted dims
    # Sort dims by weight descending, pick top 5
    sorted_dims = sorted(range(len(base_weights)), key=lambda i: base_weights[i], reverse=True)
    boost_indices = sorted_dims[:5]

    sensitivity_schemes: list[dict[str, float]] = []
    all_perturbed_ranks: list[dict[str, int]] = []  # scheme -> {filename: rank}

    for scheme_idx, dim_idx in enumerate(boost_indices):
        perturbed_w = perturb_weights(base_weights, dim_idx)
        sensitivity_schemes.append({
            "scheme": f"boost_{dim_names[dim_idx]}_+20%",
            "weights": {dim_names[j]: round(perturbed_w[j], 4) for j in range(len(dim_names))},
        })

        pert_results = run_topsis_with_weights(papers, perturbed_w)
        rank_map: dict[str, int] = {}
        for pr in pert_results:
            rank_map[papers[pr["index"]]["filename"]] = pr["rank"]
        all_perturbed_ranks.append(rank_map)

    # Add rank_stability to base results (top 15)
    for r in base_results:
        fname = r["filename"]
        r["rank_stability"] = [
            all_perturbed_ranks[s].get(fname, 999)
            for s in range(len(all_perturbed_ranks))
        ]

    # Compute Kendall's W for top 15
    kendall_w = compute_kendall_w(base_results[:15], all_perturbed_ranks)

    return sensitivity_schemes, kendall_w


def compute_kendall_w(top_papers: list[dict],
                      perturbed_ranks: list[dict[str, int]]) -> float:
    """
    Kendall's W (coefficient of concordance) for k rankers on n items.
    W = 12 * S / (k^2 * n * (n^2 - 1))
    where S = sum of squared deviations of rank sums from mean rank sum.
    """
    n = len(top_papers)
    k = len(perturbed_ranks) + 1  # +1 for base ranking

    if n < 2 or k < 2:
        return 1.0

    # Collect rank vectors: base + perturbed
    rank_matrix: list[list[int]] = []

    # Base ranks
    base_ranks = [p["rank"] for p in top_papers]
    rank_matrix.append(base_ranks)

    # Perturbed ranks
    for pr_map in perturbed_ranks:
        ranks = [pr_map.get(p["filename"], 999) for p in top_papers]
        rank_matrix.append(ranks)

    # Compute rank sums for each item
    rank_sums = [0.0] * n
    for j in range(n):
        for ranker in range(k):
            rank_sums[j] += rank_matrix[ranker][j]

    mean_rank_sum = sum(rank_sums) / n
    s = sum((rs - mean_rank_sum) ** 2 for rs in rank_sums)

    w = (12.0 * s) / (k ** 2 * n * (n ** 2 - 1))
    return round(min(w, 1.0), 4)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main() -> None:
    print("=" * 70)
    print("TOPSIS Benchmark Ranking — Merge & Compute")
    print("=" * 70)

    # Step 1: Merge
    print("\n--- Step 1: Merging features ---")
    merged_papers = merge_features()
    save_merged(merged_papers)

    # Build lookup
    papers_by_name = {p["filename"]: p for p in merged_papers}

    # Step 2: TOPSIS
    print("\n--- Step 2: TOPSIS computation ---")
    results = compute_topsis(merged_papers)
    print(f"  Ranked {len(results)} papers")

    # Step 3: ELECTRE III veto
    print("\n--- Step 3: ELECTRE III veto ---")
    results = apply_veto(results, papers_by_name)
    veto_count = sum(1 for r in results if r["veto_flag"])
    print(f"  Veto flags applied: {veto_count} papers")

    # Step 4: Sensitivity analysis
    print("\n--- Step 4: Sensitivity analysis ---")
    sensitivity_schemes, kendall_w = sensitivity_analysis(merged_papers, results)
    print(f"  Kendall's W concordance: {kendall_w}")

    # Build output JSON
    weight_scheme = {
        spec[0]: spec[2] for spec in DIMENSION_SPECS
    }

    top_15_summary = []
    for r in results[:15]:
        top_15_summary.append({
            "rank": r["rank"],
            "filename": r["filename"],
            "short_title": r["short_title"],
            "topsis_score": r["topsis_score"],
            "veto_flag": r["veto_flag"],
            "rank_stability": r.get("rank_stability", []),
        })

    output = {
        "metadata": {
            "date": "2026-04-04",
            "method": "TOPSIS with ELECTRE III veto",
            "papers_ranked": len(results),
            "veto_count": veto_count,
            "weight_scheme": weight_scheme,
            "sensitivity_schemes": len(sensitivity_schemes),
            "sensitivity_details": sensitivity_schemes,
            "kendall_w": kendall_w,
        },
        "rankings": [
            {
                "rank": r["rank"],
                "filename": r["filename"],
                "short_title": r["short_title"],
                "relevance_score": r["relevance_score"],
                "topsis_score": r["topsis_score"],
                "dimensional_scores": r["dimensional_scores"],
                "veto_flag": r["veto_flag"],
                "rank_stability": r.get("rank_stability", []),
                "source": r["source"],
            }
            for r in results
        ],
        "top_15_summary": top_15_summary,
        "sensitivity_kendall_w": kendall_w,
    }

    with open(RANKINGS_OUT, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    print(f"\nRankings written: {RANKINGS_OUT}")

    # Print top 20
    print("\n" + "=" * 100)
    print(f"{'Rank':<5} {'TOPSIS':>7} {'Veto':>5} {'Src':>5}  {'Filename'}")
    print("-" * 100)
    for r in results[:20]:
        veto_str = "VETO" if r["veto_flag"] else ""
        src_str = "D" if r["source"] in ("deep", "deep_only") else "A"
        print(f"{r['rank']:<5} {r['topsis_score']:>7.4f} {veto_str:>5} {src_str:>5}  {r['filename']}")

    # Print dimensional breakdown for top 5
    print("\n--- Dimensional breakdown (top 5) ---")
    dim_names = [spec[0] for spec in DIMENSION_SPECS]
    header = f"{'Rank':<5} " + " ".join(f"{d[:12]:>12}" for d in dim_names)
    print(header)
    print("-" * len(header))
    for r in results[:5]:
        vals = " ".join(f"{r['dimensional_scores'][d]:>12.2f}" for d in dim_names)
        print(f"{r['rank']:<5} {vals}")

    # Print rank stability for top 15
    print("\n--- Rank stability (top 15) ---")
    print(f"{'Base':>5} {'Filename':<55} {'S1':>4} {'S2':>4} {'S3':>4} {'S4':>4} {'S5':>4}")
    print("-" * 90)
    for r in results[:15]:
        stab = r.get("rank_stability", [])
        stab_str = " ".join(f"{s:>4}" for s in stab)
        print(f"{r['rank']:>5} {r['filename'][:54]:<55} {stab_str}")

    print(f"\nKendall's W concordance coefficient: {kendall_w}")
    print(f"  (1.0 = perfect agreement, 0.0 = no agreement)")
    print(f"  Interpretation: {'Strong' if kendall_w >= 0.7 else 'Moderate' if kendall_w >= 0.5 else 'Weak'} rank stability")


if __name__ == "__main__":
    main()
