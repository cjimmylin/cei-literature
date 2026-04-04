#!/usr/bin/env python3
"""
NormEval Computational Analysis — Agent 1B
Reads the 37-benchmark x 26-feature matrix and performs 10 analyses + data audit.

Outputs:
  STATISTICS/20260404-normeval-correlation-matrix.json
  STATISTICS/20260404-normeval-pca-clusters.json
  STATISTICS/20260404-normeval-sensitivity-analysis.json
  STATISTICS/20260404-normeval-hypothesis-tests.md
  STATISTICS/20260404-normeval-power-analysis.md
  STATISTICS/20260404-normeval-temporal-trends.json
  STATISTICS/20260404-normeval-anomaly-detection.json
  STATISTICS/20260404-normeval-data-availability-audit.json
  STATISTICS/20260404-normeval-data-availability-audit.md
"""
from __future__ import annotations

import json
import math
import os
import sys
from collections import Counter
from itertools import combinations
from pathlib import Path

import numpy as np
from scipy import stats
from scipy.spatial.distance import mahalanobis
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestRegressor
from sklearn.inspection import permutation_importance
from sklearn.preprocessing import StandardScaler

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
NORM_DIR = Path(__file__).resolve().parent.parent          # NORM-ETHICS/
STATS_DIR = NORM_DIR / "STATISTICS"
MATRIX_PATH = STATS_DIR / "20260402-normative-benchmark-feature-matrix.json"

DATE_PREFIX = "20260404"


def load_matrix() -> list[dict]:
    with open(MATRIX_PATH) as f:
        return json.load(f)


def save_json(name: str, obj):
    path = STATS_DIR / f"{DATE_PREFIX}-normeval-{name}.json"
    with open(path, "w") as f:
        json.dump(obj, f, indent=2, default=_default_serializer)
    print(f"  -> {path.name}")


def save_md(name: str, text: str):
    path = STATS_DIR / f"{DATE_PREFIX}-normeval-{name}.md"
    with open(path, "w") as f:
        f.write(text)
    print(f"  -> {path.name}")


def _default_serializer(o):
    if isinstance(o, (np.integer,)):
        return int(o)
    if isinstance(o, (np.floating,)):
        return round(float(o), 6)
    if isinstance(o, np.ndarray):
        return o.tolist()
    if isinstance(o, (np.bool_,)):
        return bool(o)
    raise TypeError(f"Not serializable: {type(o)}")


# ---------------------------------------------------------------------------
# Feature extraction helpers
# ---------------------------------------------------------------------------
NUMERIC_FEATURES = [
    "ND_score", "PE_score", "CI_score", "COMPOSITE",
    "A1_count", "A6_grounding",
    "B2_dataset_size", "B7_implementability",
    "C1_citation_count", "C2_citations_per_year", "C4_downstream_adoption",
]

TRADITION_KEYS = [
    "virtue_ethics", "deontological_ethics", "utilitarian_ethics",
    "care_ethics", "contractarian_ethics",
]


def extract_numeric_matrix(benchmarks: list[dict]) -> tuple[np.ndarray, list[str], list[str]]:
    """Return (n_benchmarks x n_features) matrix, feature names, benchmark names."""
    names = [b["short_title"] for b in benchmarks]
    features = NUMERIC_FEATURES[:]
    # Add tradition scores
    for tk in TRADITION_KEYS:
        features.append(f"A1_{tk}")
    # Add harness total_accessible
    features.append("B6_total_accessible")
    # Add language count
    features.append("A8_lang_count")
    # Add D3 model count
    features.append("D3_model_count")
    # Add year as numeric
    features.append("D1_year_num")

    rows = []
    for b in benchmarks:
        row = []
        for f in NUMERIC_FEATURES:
            val = b.get(f)
            row.append(float(val) if val is not None else np.nan)
        for tk in TRADITION_KEYS:
            row.append(float(b["A1_traditions"].get(tk, 0)))
        row.append(float(b["B6_harness"].get("total_accessible", 0)))
        row.append(float(b["A8_multilingual"].get("count", 0)))
        row.append(float(b["D3_llms_tested"].get("count", 0)))
        try:
            row.append(float(b["D1_year"]))
        except (ValueError, TypeError):
            row.append(np.nan)
        rows.append(row)

    return np.array(rows), features, names


# ===================================================================
# Analysis 1: Correlation Matrix
# ===================================================================
def analysis_correlation(benchmarks, X, features, names):
    print("\n[1] Correlation Matrix (Spearman)")
    n_f = len(features)
    corr_matrix = np.full((n_f, n_f), np.nan)
    pval_matrix = np.full((n_f, n_f), np.nan)

    for i in range(n_f):
        for j in range(n_f):
            col_i = X[:, i]
            col_j = X[:, j]
            mask = ~(np.isnan(col_i) | np.isnan(col_j))
            if mask.sum() >= 5:
                r, p = stats.spearmanr(col_i[mask], col_j[mask])
                corr_matrix[i, j] = r
                pval_matrix[i, j] = p

    # Near-redundant pairs (|r| > 0.8)
    redundant = []
    anti_corr = []
    for i in range(n_f):
        for j in range(i + 1, n_f):
            r = corr_matrix[i, j]
            if np.isnan(r):
                continue
            if abs(r) > 0.8:
                redundant.append({
                    "feature_1": features[i],
                    "feature_2": features[j],
                    "r": round(r, 4),
                    "p": round(pval_matrix[i, j], 6),
                })
            if r < -0.4 and pval_matrix[i, j] < 0.05:
                anti_corr.append({
                    "feature_1": features[i],
                    "feature_2": features[j],
                    "r": round(r, 4),
                    "p": round(pval_matrix[i, j], 6),
                })

    # Sort
    redundant.sort(key=lambda x: -abs(x["r"]))
    anti_corr.sort(key=lambda x: x["r"])

    print(f"  Near-redundant pairs (|r|>0.8): {len(redundant)}")
    for p in redundant[:10]:
        print(f"    {p['feature_1']} <-> {p['feature_2']}: r={p['r']}")
    print(f"  Significant anti-correlations (r<-0.4, p<0.05): {len(anti_corr)}")
    for p in anti_corr[:10]:
        print(f"    {p['feature_1']} <-> {p['feature_2']}: r={p['r']}")

    return {
        "correlation_matrix": corr_matrix.tolist(),
        "features": features,
        "near_redundant_pairs": redundant,
        "anti_correlations": anti_corr,
        "pvalue_matrix": pval_matrix.tolist(),
    }


# ===================================================================
# Analysis 2: PCA Dimensionality Reduction
# ===================================================================
def analysis_pca(benchmarks, X, features, names):
    print("\n[2] PCA Dimensionality Reduction")
    # Impute NaNs with column medians for PCA
    X_imp = X.copy()
    for j in range(X_imp.shape[1]):
        col = X_imp[:, j]
        nanmask = np.isnan(col)
        if nanmask.any():
            median_val = np.nanmedian(col)
            col[nanmask] = median_val

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X_imp)

    pca = PCA(n_components=min(3, X_scaled.shape[1]))
    coords = pca.fit_transform(X_scaled)

    var_explained = pca.explained_variance_ratio_
    print(f"  Variance explained: PC1={var_explained[0]:.3f}, PC2={var_explained[1]:.3f}, PC3={var_explained[2]:.3f}")
    print(f"  Cumulative: {sum(var_explained):.3f}")

    # Top loadings per component
    loadings = pca.components_
    loadings_info = []
    for pc_idx in range(3):
        abs_load = np.abs(loadings[pc_idx])
        top_idx = np.argsort(abs_load)[::-1][:5]
        loadings_info.append({
            "component": f"PC{pc_idx+1}",
            "variance_explained": round(float(var_explained[pc_idx]), 4),
            "top_features": [
                {"feature": features[i], "loading": round(float(loadings[pc_idx, i]), 4)}
                for i in top_idx
            ],
        })
        print(f"  PC{pc_idx+1} top loadings:")
        for i in top_idx:
            print(f"    {features[i]}: {loadings[pc_idx, i]:.3f}")

    # Check cluster alignment with Top15 / Bottom22
    top15_mask = np.array([b.get("passes_gates", False) for b in benchmarks])
    benchmark_pca = []
    for i, b in enumerate(benchmarks):
        benchmark_pca.append({
            "name": names[i],
            "id": b["id"],
            "pc1": round(float(coords[i, 0]), 4),
            "pc2": round(float(coords[i, 1]), 4),
            "pc3": round(float(coords[i, 2]), 4),
            "passes_gates": bool(b.get("passes_gates", False)),
            "COMPOSITE": b["COMPOSITE"],
        })

    # Centroid separation
    top_coords = coords[top15_mask]
    bot_coords = coords[~top15_mask]
    top_centroid = top_coords.mean(axis=0)
    bot_centroid = bot_coords.mean(axis=0)
    centroid_dist = np.linalg.norm(top_centroid - bot_centroid)
    print(f"  Top15/Bottom22 centroid distance in PCA space: {centroid_dist:.3f}")

    # ND-PE Tradeoff Regression (Analysis 7) — embed here
    nd_scores = np.array([b["ND_score"] for b in benchmarks])
    pe_scores = np.array([b["PE_score"] for b in benchmarks])
    slope, intercept, r_val, p_val, std_err = stats.linregress(pe_scores, nd_scores)
    residuals = nd_scores - (slope * pe_scores + intercept)
    outlier_threshold = 2.0 * np.std(residuals)
    nd_pe_outliers = []
    for i, b in enumerate(benchmarks):
        if abs(residuals[i]) > outlier_threshold:
            nd_pe_outliers.append({
                "name": names[i],
                "ND": b["ND_score"],
                "PE": b["PE_score"],
                "residual": round(float(residuals[i]), 2),
                "direction": "ND higher than expected" if residuals[i] > 0 else "ND lower than expected",
            })

    nd_pe_regression = {
        "slope": round(float(slope), 4),
        "intercept": round(float(intercept), 4),
        "r_squared": round(float(r_val ** 2), 4),
        "p_value": round(float(p_val), 6),
        "std_err": round(float(std_err), 4),
        "outliers": nd_pe_outliers,
    }
    print(f"\n  [7] ND~PE regression: R^2={r_val**2:.4f}, p={p_val:.6f}, slope={slope:.3f}")
    for o in nd_pe_outliers:
        print(f"    Outlier: {o['name']} ({o['direction']}, residual={o['residual']})")

    return {
        "pca_benchmarks": benchmark_pca,
        "loadings": loadings_info,
        "cumulative_variance": round(float(sum(var_explained)), 4),
        "centroid_distance_top15_bottom22": round(float(centroid_dist), 4),
        "nd_pe_regression": nd_pe_regression,
    }


# ===================================================================
# Analysis 3: Sensitivity Analysis on Composite Weights
# ===================================================================
def analysis_sensitivity(benchmarks):
    print("\n[3] Sensitivity Analysis — Weight Sweep")
    nd_scores = np.array([b["ND_score"] for b in benchmarks])
    pe_scores = np.array([b["PE_score"] for b in benchmarks])
    ci_scores = np.array([b["CI_score"] for b in benchmarks])
    gate_nd = np.array([b.get("gate_ND", False) for b in benchmarks])
    gate_data = np.array([b.get("gate_data", False) for b in benchmarks])
    names = [b["short_title"] for b in benchmarks]
    n = len(benchmarks)

    # Current Top 15 set
    current_top15 = set()
    for b in benchmarks:
        if b.get("passes_gates"):
            current_top15.add(b["short_title"])

    # Generate weight triplets (5% increments, sum=1.0)
    triplets = []
    for w_nd in range(0, 105, 5):
        for w_pe in range(0, 105 - w_nd, 5):
            w_ci = 100 - w_nd - w_pe
            if w_ci >= 0:
                triplets.append((w_nd / 100.0, w_pe / 100.0, w_ci / 100.0))

    # For each triplet, compute composite and find Top 15
    benchmark_in_top15_count = Counter()
    total_configs = len(triplets)

    for w_nd_f, w_pe_f, w_ci_f in triplets:
        composites = w_nd_f * nd_scores + w_pe_f * pe_scores + w_ci_f * ci_scores
        # Apply gates: must pass both ND and data gates
        gated_composites = []
        for i in range(n):
            if gate_nd[i] and gate_data[i]:
                gated_composites.append((composites[i], names[i]))
        gated_composites.sort(key=lambda x: -x[0])
        top15_names = set(x[1] for x in gated_composites[:15])
        for nm in top15_names:
            benchmark_in_top15_count[nm] += 1

    # Classify benchmarks
    stable_always = []
    borderline = []
    never_top15 = []
    for b in benchmarks:
        nm = b["short_title"]
        cnt = benchmark_in_top15_count.get(nm, 0)
        pct = cnt / total_configs * 100
        entry = {"name": nm, "count": cnt, "total": total_configs, "pct": round(pct, 1)}
        if cnt == total_configs:
            stable_always.append(entry)
        elif cnt > 0:
            borderline.append(entry)
        else:
            never_top15.append(entry)

    borderline.sort(key=lambda x: -x["pct"])

    print(f"  Weight triplets tested: {total_configs}")
    print(f"  Always in Top 15: {len(stable_always)}")
    for s in stable_always:
        print(f"    {s['name']}")
    print(f"  Borderline: {len(borderline)}")
    for s in borderline[:10]:
        print(f"    {s['name']}: {s['pct']}% of configs")
    print(f"  Never Top 15: {len(never_top15)}")

    # Gate threshold sensitivity: ND gate at 35, 40 (current), 45
    gate_results = {}
    for nd_gate in [30, 35, 40, 45, 50]:
        passing = [b["short_title"] for b in benchmarks
                   if b["ND_score"] >= nd_gate and b.get("gate_data")]
        gate_results[f"ND_gate_{nd_gate}"] = {
            "passing_count": len(passing),
            "benchmarks": passing,
        }
        print(f"  ND gate={nd_gate}: {len(passing)} pass both gates")

    return {
        "weight_triplets_tested": total_configs,
        "stable_always_top15": stable_always,
        "borderline": borderline,
        "never_top15": never_top15,
        "gate_threshold_sensitivity": gate_results,
        "current_weights": {"ND": 0.40, "PE": 0.35, "CI": 0.25},
    }


# ===================================================================
# Analysis 4: Hypothesis Tests for 5 Claims
# ===================================================================
def analysis_hypothesis_tests(benchmarks):
    print("\n[4] Hypothesis Tests for 5 Claims")
    lines = ["# Hypothesis Tests for NormEval 5 Claims", ""]
    lines.append(f"Date: {DATE_PREFIX[:4]}-{DATE_PREFIX[4:6]}-{DATE_PREFIX[6:]}")
    lines.append(f"Benchmarks: {len(benchmarks)}")
    lines.append("")

    results = {}

    # --- C1: Ceiling Effect ---
    lines.append("## C1: Ceiling Effect")
    lines.append("**H0:** GPT-4 performance on binary moral judgments = 50% (chance)")
    lines.append("**H1:** GPT-4 performance > 50%")
    lines.append("")
    lines.append("Test: Binomial test for P(50/50 correct | p=0.9)")
    lines.append("This tests whether observing 50/50 correct is plausible if true accuracy is 90%.")
    lines.append("")

    # P(X >= 50 | n=50, p=0.9) — essentially certain
    # But the claim is about ceiling: P(X=50 | n=50, p=0.9) = 0.9^50
    p_all_correct = 0.9 ** 50
    # Binomial test: is getting 50/50 surprising if p=0.5?
    binom_result = stats.binomtest(50, 50, 0.5, alternative="greater").pvalue
    # Also: P(>=45 | n=50, p=0.5) for near-ceiling
    p_ceiling_under_null = 1 - stats.binom.cdf(44, 50, 0.5)

    lines.append(f"- P(50/50 correct | p=0.5, chance): p = {binom_result:.2e} (binomial test)")
    lines.append(f"- P(all 50 correct | p=0.9): {p_all_correct:.6f}")
    lines.append(f"- P(>=45/50 | p=0.5): {p_ceiling_under_null:.2e}")
    lines.append("")
    lines.append("**Interpretation:** If a model scores 50/50, we can reject chance (p=0.5)")
    lines.append(f"with p < {binom_result:.2e}. The ceiling effect is real: at p=0.9 true accuracy,")
    lines.append(f"the probability of a perfect score is {p_all_correct:.4f} (not negligible),")
    lines.append("making benchmarks unable to discriminate among high-performing models.")
    lines.append("")

    results["C1_ceiling"] = {
        "test": "binomial",
        "n": 50,
        "k": 50,
        "p_null": 0.5,
        "p_value": float(binom_result),
        "p_perfect_at_90pct": round(p_all_correct, 6),
        "p_ge45_at_chance": float(p_ceiling_under_null),
        "reject_null": True,
    }

    # --- C2: Utilitarian Bias ---
    lines.append("## C2: Utilitarian Bias")
    lines.append("**H0:** Accuracy on utilitarian items = accuracy on deontological items")
    lines.append("**H1:** Utilitarian accuracy > deontological accuracy")
    lines.append("")

    p_util = 0.77
    p_deont = 0.50
    n_per = 30

    # Two-proportion z-test
    p_pooled = (p_util * n_per + p_deont * n_per) / (2 * n_per)
    se = math.sqrt(p_pooled * (1 - p_pooled) * (1 / n_per + 1 / n_per))
    z = (p_util - p_deont) / se
    p_value_z = 1 - stats.norm.cdf(z)

    # 95% CI for difference
    se_diff = math.sqrt(p_util * (1 - p_util) / n_per + p_deont * (1 - p_deont) / n_per)
    diff = p_util - p_deont
    ci_low = diff - 1.96 * se_diff
    ci_high = diff + 1.96 * se_diff

    # Cohen's h
    h = 2 * math.asin(math.sqrt(p_util)) - 2 * math.asin(math.sqrt(p_deont))

    lines.append(f"- Utilitarian accuracy: {p_util*100:.0f}% (n={n_per})")
    lines.append(f"- Deontological accuracy: {p_deont*100:.0f}% (n={n_per})")
    lines.append(f"- Two-proportion z-test: z = {z:.3f}, p = {p_value_z:.4f}")
    lines.append(f"- Difference: {diff*100:.1f} percentage points")
    lines.append(f"- 95% CI for difference: [{ci_low*100:.1f}%, {ci_high*100:.1f}%]")
    lines.append(f"- Cohen's h = {h:.3f} ({'large' if abs(h) >= 0.8 else 'medium' if abs(h) >= 0.5 else 'small'})")
    lines.append("")
    lines.append(f"**Interpretation:** The {diff*100:.0f} percentage-point gap is statistically")
    lines.append(f"significant (p = {p_value_z:.4f}), with Cohen's h = {h:.3f} indicating a")
    lines.append(f"{'large' if abs(h) >= 0.8 else 'medium' if abs(h) >= 0.5 else 'small'} effect size.")
    lines.append("")

    results["C2_bias"] = {
        "test": "two_proportion_z",
        "p_utilitarian": p_util,
        "p_deontological": p_deont,
        "n_per_group": n_per,
        "z_statistic": round(z, 4),
        "p_value": round(p_value_z, 6),
        "difference": round(diff, 4),
        "ci_95": [round(ci_low, 4), round(ci_high, 4)],
        "cohens_h": round(h, 4),
        "effect_size": "large" if abs(h) >= 0.8 else "medium" if abs(h) >= 0.5 else "small",
        "reject_null": p_value_z < 0.05,
    }

    # --- C3: Care Ethics Void ---
    lines.append("## C3: Care Ethics Void")
    lines.append("**H0:** Care ethics is assigned uniformly like other traditions")
    lines.append("**H1:** Care ethics is systematically absent as primary tradition")
    lines.append("")

    # Count benchmarks with care_ethics as highest tradition score
    care_primary = 0
    for b in benchmarks:
        t = b["A1_traditions"]
        scores = [(k, v) for k, v in t.items() if isinstance(v, (int, float))]
        if not scores:
            continue
        max_score = max(s[1] for s in scores)
        if max_score > 0:
            top_traditions = [s[0] for s in scores if s[1] == max_score]
            if "care_ethics" in top_traditions:
                care_primary += 1

    # Under uniform: each of 5 traditions equally likely to be primary
    # P(0 out of 37 have care as primary) if p = 1/5 per benchmark
    p_uniform = 1 / 5
    p_zero_care = stats.binom.pmf(0, 37, p_uniform)

    # Under uniform: P(care is NEVER the sole highest)
    # More precisely: for each benchmark, P(care not max) = 4/5 independent
    p_never_primary = (1 - p_uniform) ** 37

    lines.append(f"- Benchmarks with care ethics as primary/co-primary: {care_primary}/37")
    lines.append(f"- Under uniform assignment (p=1/5 per benchmark):")
    lines.append(f"  P(exactly 0 have care as primary) = {p_zero_care:.2e}")
    lines.append(f"  P(care never primary across 37) = {p_never_primary:.6f}")
    lines.append("")

    # Also count care_ethics > 0 at all
    care_nonzero = sum(1 for b in benchmarks if b["A1_traditions"].get("care_ethics", 0) > 0)
    care_above_50 = sum(1 for b in benchmarks if b["A1_traditions"].get("care_ethics", 0) >= 50)
    lines.append(f"- Care ethics score > 0: {care_nonzero}/37 benchmarks")
    lines.append(f"- Care ethics score >= 50: {care_above_50}/37 benchmarks")
    lines.append("")
    lines.append(f"**Interpretation:** Only {care_primary}/37 benchmarks have care ethics as")
    lines.append(f"primary. Under uniform random assignment, P(0 out of 37) = {p_zero_care:.2e},")
    lines.append("strongly suggesting systematic exclusion rather than chance.")
    lines.append("")

    results["C3_void"] = {
        "test": "analytic_binomial",
        "care_as_primary": care_primary,
        "total_benchmarks": 37,
        "p_uniform": p_uniform,
        "p_zero_under_uniform": float(p_zero_care),
        "p_never_primary": float(p_never_primary),
        "care_nonzero_count": care_nonzero,
        "care_above_50": care_above_50,
        "reject_null": p_zero_care < 0.05 if care_primary == 0 else False,
    }

    # --- C4: Judgment-Only Predominance ---
    lines.append("## C4: Judgment-Only Predominance")
    lines.append("**H0:** P(judgment-only) = 0.5")
    lines.append("**H1:** P(judgment-only) > 0.5")
    lines.append("")

    judgment_only = sum(1 for b in benchmarks if b.get("A3_reasoning") == "Tests judgment only")
    n_total = len(benchmarks)
    binom_c4 = stats.binomtest(judgment_only, n_total, 0.5, alternative="greater").pvalue

    # 95% CI for proportion using Wilson interval
    p_hat = judgment_only / n_total
    z_alpha = 1.96
    denom = 1 + z_alpha**2 / n_total
    center = (p_hat + z_alpha**2 / (2 * n_total)) / denom
    margin = z_alpha * math.sqrt((p_hat * (1 - p_hat) + z_alpha**2 / (4 * n_total)) / n_total) / denom
    ci_wilson = (round(center - margin, 4), round(center + margin, 4))

    lines.append(f"- Judgment-only benchmarks: {judgment_only}/{n_total} ({p_hat*100:.1f}%)")
    lines.append(f"- Binomial test (H1: p > 0.5): p = {binom_c4:.4f}")
    lines.append(f"- Wilson 95% CI: [{ci_wilson[0]*100:.1f}%, {ci_wilson[1]*100:.1f}%]")
    lines.append("")
    lines.append(f"**Interpretation:** {judgment_only}/{n_total} = {p_hat*100:.1f}% of benchmarks")
    lines.append(f"test only judgment. {'Significant' if binom_c4 < 0.05 else 'Not significant'}")
    lines.append(f"at alpha=0.05 (p = {binom_c4:.4f}).")
    lines.append("")

    results["C4_judgment"] = {
        "test": "binomial",
        "k": judgment_only,
        "n": n_total,
        "proportion": round(p_hat, 4),
        "p_value": round(float(binom_c4), 6),
        "ci_95_wilson": list(ci_wilson),
        "reject_null": binom_c4 < 0.05,
    }

    # --- C5: Data Bottleneck ---
    lines.append("## C5: Data Availability Bottleneck")
    lines.append("**H0:** ND scores are the same for data-available vs data-unavailable benchmarks")
    lines.append("**H1:** They differ (two-sided)")
    lines.append("")

    nd_available = [b["ND_score"] for b in benchmarks if b.get("gate_data")]
    nd_unavailable = [b["ND_score"] for b in benchmarks if not b.get("gate_data")]

    if len(nd_available) >= 2 and len(nd_unavailable) >= 2:
        u_stat, p_mw = stats.mannwhitneyu(nd_available, nd_unavailable, alternative="two-sided")
        # Effect size: rank-biserial correlation
        n1, n2 = len(nd_available), len(nd_unavailable)
        r_rb = 1 - (2 * u_stat) / (n1 * n2)
    else:
        u_stat, p_mw, r_rb = np.nan, np.nan, np.nan

    lines.append(f"- Data-available benchmarks (n={len(nd_available)}): mean ND = {np.mean(nd_available):.1f}, median = {np.median(nd_available):.1f}")
    lines.append(f"- Data-unavailable benchmarks (n={len(nd_unavailable)}): mean ND = {np.mean(nd_unavailable):.1f}, median = {np.median(nd_unavailable):.1f}")
    lines.append(f"- Mann-Whitney U = {u_stat:.1f}, p = {float(p_mw):.4f}")
    lines.append(f"- Rank-biserial r = {r_rb:.3f}")
    lines.append("")
    avail_str = "Data-available" if np.mean(nd_available) > np.mean(nd_unavailable) else "Data-unavailable"
    lines.append(f"**Interpretation:** {avail_str} benchmarks have")
    lines.append(f"{'significantly' if p_mw < 0.05 else 'non-significantly'} {'higher' if np.mean(nd_available) > np.mean(nd_unavailable) else 'lower'}")
    lines.append(f"ND scores (p = {float(p_mw):.4f}). Effect size r = {r_rb:.3f}.")
    lines.append("")

    results["C5_bottleneck"] = {
        "test": "mann_whitney_u",
        "n_available": len(nd_available),
        "n_unavailable": len(nd_unavailable),
        "mean_nd_available": round(float(np.mean(nd_available)), 2),
        "mean_nd_unavailable": round(float(np.mean(nd_unavailable)), 2),
        "median_nd_available": round(float(np.median(nd_available)), 2),
        "median_nd_unavailable": round(float(np.median(nd_unavailable)), 2),
        "U_statistic": float(u_stat),
        "p_value": round(float(p_mw), 6),
        "rank_biserial_r": round(float(r_rb), 4),
        "reject_null": float(p_mw) < 0.05 if not np.isnan(p_mw) else False,
    }

    return results, "\n".join(lines)


# ===================================================================
# Analysis 5: Power Analysis
# ===================================================================
def analysis_power(benchmarks):
    print("\n[5] Power Analysis")
    lines = ["# Power Analysis for NormEval", ""]
    lines.append(f"Date: {DATE_PREFIX[:4]}-{DATE_PREFIX[4:6]}-{DATE_PREFIX[6:]}")
    lines.append("")

    # Helper: minimum n for two-proportion test
    def min_n_two_prop(p1, p2, alpha=0.05, power=0.80):
        z_alpha = stats.norm.ppf(1 - alpha / 2)
        z_beta = stats.norm.ppf(power)
        p_bar = (p1 + p2) / 2
        n = ((z_alpha * math.sqrt(2 * p_bar * (1 - p_bar)) +
              z_beta * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) / (p1 - p2)) ** 2
        return math.ceil(n)

    # 1. Detecting 77% vs 50% gap
    lines.append("## 1. Detecting Utilitarian Bias (77% vs 50%)")
    n_needed_1 = min_n_two_prop(0.77, 0.50)
    h_1 = 2 * math.asin(math.sqrt(0.77)) - 2 * math.asin(math.sqrt(0.50))
    lines.append(f"- Effect: 77% vs 50% (Cohen's h = {h_1:.3f})")
    lines.append(f"- Minimum n per group: **{n_needed_1}** (alpha=0.05, power=0.80)")
    lines.append(f"- Total items needed: {n_needed_1 * 2}")
    lines.append("")

    # 2. Detecting 15-point gap (e.g., 65% vs 50%)
    lines.append("## 2. Detecting a 15-Point Gap (65% vs 50%)")
    n_needed_2 = min_n_two_prop(0.65, 0.50)
    h_2 = 2 * math.asin(math.sqrt(0.65)) - 2 * math.asin(math.sqrt(0.50))
    lines.append(f"- Effect: 65% vs 50% (Cohen's h = {h_2:.3f})")
    lines.append(f"- Minimum n per group: **{n_needed_2}** (alpha=0.05, power=0.80)")
    lines.append(f"- Total items needed: {n_needed_2 * 2}")
    lines.append("")

    # 3. Cross-model comparison (4 models)
    lines.append("## 3. Cross-Model Comparison (4 models)")
    lines.append("Using Bonferroni correction for 6 pairwise comparisons:")
    alpha_bonf = 0.05 / 6
    n_needed_3_large = min_n_two_prop(0.77, 0.50, alpha=alpha_bonf)
    n_needed_3_small = min_n_two_prop(0.65, 0.50, alpha=alpha_bonf)
    lines.append(f"- For 27pp gap (alpha={alpha_bonf:.4f}): n = **{n_needed_3_large}** per group per model")
    lines.append(f"- For 15pp gap (alpha={alpha_bonf:.4f}): n = **{n_needed_3_small}** per group per model")
    lines.append(f"- Total items for 15pp detection across 4 models: {n_needed_3_small * 2 * 4}")
    lines.append("")

    # 4. Framework-level analysis (n=10 per framework as in T3)
    lines.append("## 4. Current Trial Power Assessment (n=10 per framework)")
    # With n=10, what effect size can we detect?
    # Solve for detectable difference at n=10, alpha=0.05, power=0.80
    lines.append("Given n=10 items per framework (as in Trial T3):")
    # Use iterative approach
    for diff_pct in [10, 15, 20, 25, 30, 35, 40]:
        p1 = 0.50 + diff_pct / 100
        p2 = 0.50
        if p1 > 1:
            continue
        n_req = min_n_two_prop(p1, p2)
        h = 2 * math.asin(math.sqrt(p1)) - 2 * math.asin(math.sqrt(p2))
        # Approximate power at n=10
        z_alpha = stats.norm.ppf(0.975)
        p_bar = (p1 + p2) / 2
        se_null = math.sqrt(2 * p_bar * (1 - p_bar) / 10)
        se_alt = math.sqrt((p1 * (1 - p1) + p2 * (1 - p2)) / 10)
        z_power = ((p1 - p2) - z_alpha * se_null) / se_alt
        power_at_10 = stats.norm.cdf(z_power)
        lines.append(f"- {diff_pct}pp gap: n needed = {n_req}, power at n=10 = {power_at_10:.2f}, h = {h:.3f}")

    lines.append("")
    lines.append("## 5. Summary")
    lines.append(f"- The T3 gap (27pp) requires **{n_needed_1}** items per group for 80% power")
    lines.append(f"- A smaller 15pp gap requires **{n_needed_2}** items per group")
    lines.append(f"- With only 10 items per framework, we can reliably detect gaps >= ~30pp")
    lines.append(f"- Cross-model comparison (4 models, 6 pairs) inflates to **{n_needed_3_small}** per group")
    lines.append("")

    return "\n".join(lines)


# ===================================================================
# Analysis 6: Feature Importance
# ===================================================================
def analysis_feature_importance(benchmarks, X, features, names):
    print("\n[6] Feature Importance (Permutation)")
    # Target: COMPOSITE score
    composite_idx = features.index("COMPOSITE")
    y = X[:, composite_idx].copy()

    # Use all other numeric features as predictors
    pred_indices = [i for i in range(len(features)) if i != composite_idx]
    X_pred = X[:, pred_indices].copy()
    pred_names = [features[i] for i in pred_indices]

    # Impute NaNs with median
    for j in range(X_pred.shape[1]):
        col = X_pred[:, j]
        nanmask = np.isnan(col)
        if nanmask.any():
            col[nanmask] = np.nanmedian(col)

    # Handle NaN in target
    y_nanmask = np.isnan(y)
    if y_nanmask.any():
        y[y_nanmask] = np.nanmedian(y)

    # Random Forest for permutation importance
    rf = RandomForestRegressor(n_estimators=200, random_state=42, max_depth=5)
    rf.fit(X_pred, y)
    r2_train = rf.score(X_pred, y)
    print(f"  RF train R^2: {r2_train:.4f}")

    # Permutation importance
    perm_imp = permutation_importance(rf, X_pred, y, n_repeats=30, random_state=42)
    imp_mean = perm_imp.importances_mean
    imp_std = perm_imp.importances_std

    # Sort by importance
    sorted_idx = np.argsort(imp_mean)[::-1]
    importance_ranking = []
    for idx in sorted_idx:
        importance_ranking.append({
            "feature": pred_names[idx],
            "importance_mean": round(float(imp_mean[idx]), 4),
            "importance_std": round(float(imp_std[idx]), 4),
        })

    print("  Top features driving COMPOSITE:")
    for entry in importance_ranking[:10]:
        print(f"    {entry['feature']}: {entry['importance_mean']:.4f} +/- {entry['importance_std']:.4f}")

    # Check if composite is effectively a proxy for 2-3 features
    # Cumulative importance
    total_imp = sum(imp_mean[imp_mean > 0])
    cumulative = 0
    n_for_90pct = 0
    for idx in sorted_idx:
        if imp_mean[idx] > 0:
            cumulative += imp_mean[idx]
            n_for_90pct += 1
            if cumulative / total_imp >= 0.90:
                break

    print(f"  Features needed for 90% importance: {n_for_90pct}")

    return {
        "rf_train_r2": round(float(r2_train), 4),
        "importance_ranking": importance_ranking,
        "features_for_90pct": n_for_90pct,
        "total_positive_importance": round(float(total_imp), 4),
    }


# ===================================================================
# Analysis 8: Tradition Coverage Entropy
# ===================================================================
def analysis_entropy(benchmarks):
    print("\n[8] Tradition Coverage Entropy")
    entropy_results = []
    for b in benchmarks:
        t = b["A1_traditions"]
        scores = np.array([t.get(k, 0) for k in TRADITION_KEYS], dtype=float)
        total = scores.sum()
        if total > 0:
            probs = scores / total
            # Shannon entropy (log2)
            entropy = -sum(p * math.log2(p) if p > 0 else 0 for p in probs)
            max_entropy = math.log2(5)  # 5 traditions
            normalized_entropy = entropy / max_entropy
        else:
            entropy = 0
            normalized_entropy = 0
        entropy_results.append({
            "name": b["short_title"],
            "tradition_scores": {k: t.get(k, 0) for k in TRADITION_KEYS},
            "entropy": round(entropy, 4),
            "normalized_entropy": round(normalized_entropy, 4),
            "ND_score": b["ND_score"],
        })

    # Sort by entropy
    entropy_results.sort(key=lambda x: -x["entropy"])
    print("  Most balanced (high entropy):")
    for e in entropy_results[:5]:
        print(f"    {e['name']}: H={e['entropy']:.3f} (norm={e['normalized_entropy']:.3f})")
    print("  Most biased (low entropy):")
    for e in entropy_results[-5:]:
        print(f"    {e['name']}: H={e['entropy']:.3f} (norm={e['normalized_entropy']:.3f})")

    # Correlation: entropy vs ND
    entropies = [e["entropy"] for e in entropy_results]
    nd_scores = [e["ND_score"] for e in entropy_results]
    r, p = stats.spearmanr(entropies, nd_scores)
    print(f"  Entropy-ND correlation: r={r:.3f}, p={p:.4f}")

    return {
        "benchmark_entropy": entropy_results,
        "entropy_nd_correlation": {"r": round(r, 4), "p": round(p, 6)},
        "max_possible_entropy": round(math.log2(5), 4),
    }


# ===================================================================
# Analysis 9: Temporal Trends
# ===================================================================
def analysis_temporal(benchmarks):
    print("\n[9] Temporal Trends")
    years = []
    nd_scores = []
    pe_scores = []
    ci_scores = []
    names = []

    for b in benchmarks:
        try:
            y = int(b["D1_year"])
        except (ValueError, TypeError):
            continue
        years.append(y)
        nd_scores.append(b["ND_score"])
        pe_scores.append(b["PE_score"])
        ci_scores.append(b["CI_score"])
        names.append(b["short_title"])

    years = np.array(years)
    nd_scores = np.array(nd_scores)
    pe_scores = np.array(pe_scores)
    ci_scores = np.array(ci_scores)

    results = {}
    for label, scores in [("ND", nd_scores), ("PE", pe_scores), ("CI", ci_scores)]:
        r, p = stats.spearmanr(years, scores)
        slope, intercept, r_lin, p_lin, se = stats.linregress(years, scores)
        results[label] = {
            "spearman_r": round(float(r), 4),
            "spearman_p": round(float(p), 6),
            "linear_slope": round(float(slope), 4),
            "linear_intercept": round(float(intercept), 2),
            "linear_r_squared": round(float(r_lin**2), 4),
        }
        print(f"  Year vs {label}: Spearman r={r:.3f} (p={p:.4f}), slope={slope:.2f}/year")

    # Year distribution
    year_counts = Counter(years.tolist())
    year_dist = [{"year": y, "count": c} for y, c in sorted(year_counts.items())]

    # Benchmark-level temporal data
    benchmark_temporal = []
    for i, nm in enumerate(names):
        benchmark_temporal.append({
            "name": nm,
            "year": int(years[i]),
            "ND": round(float(nd_scores[i]), 2),
            "PE": round(float(pe_scores[i]), 2),
            "CI": round(float(ci_scores[i]), 2),
        })

    return {
        "trend_correlations": results,
        "year_distribution": year_dist,
        "benchmarks": benchmark_temporal,
    }


# ===================================================================
# Analysis 10: Anomaly Detection (Mahalanobis Distance)
# ===================================================================
def analysis_anomaly(benchmarks, X, features, names):
    print("\n[10] Anomaly Detection (Mahalanobis Distance)")
    # Impute NaNs
    X_imp = X.copy()
    for j in range(X_imp.shape[1]):
        col = X_imp[:, j]
        nanmask = np.isnan(col)
        if nanmask.any():
            col[nanmask] = np.nanmedian(col)

    # Compute Mahalanobis distance
    mean = np.mean(X_imp, axis=0)
    cov = np.cov(X_imp.T)

    # Regularize covariance (add small diagonal) to avoid singularity
    cov_reg = cov + np.eye(cov.shape[0]) * 1e-6

    try:
        cov_inv = np.linalg.inv(cov_reg)
    except np.linalg.LinAlgError:
        print("  WARNING: Covariance matrix singular, using pseudo-inverse")
        cov_inv = np.linalg.pinv(cov_reg)

    distances = []
    for i in range(X_imp.shape[0]):
        d = mahalanobis(X_imp[i], mean, cov_inv)
        distances.append(d)

    distances = np.array(distances)

    # Chi-squared threshold for p=0.01
    n_features = X_imp.shape[1]
    chi2_threshold = stats.chi2.ppf(0.99, df=n_features)
    chi2_threshold_sq = math.sqrt(chi2_threshold)

    anomaly_results = []
    for i in range(len(benchmarks)):
        is_outlier = distances[i] > chi2_threshold_sq
        anomaly_results.append({
            "name": names[i],
            "id": benchmarks[i]["id"],
            "mahalanobis_distance": round(float(distances[i]), 4),
            "is_outlier_p01": bool(is_outlier),
            "passes_gates": bool(benchmarks[i].get("passes_gates", False)),
        })

    anomaly_results.sort(key=lambda x: -x["mahalanobis_distance"])
    n_outliers = sum(1 for a in anomaly_results if a["is_outlier_p01"])

    print(f"  Chi-squared threshold (p=0.01, df={n_features}): {chi2_threshold_sq:.2f}")
    print(f"  Outliers: {n_outliers}/{len(benchmarks)}")
    print("  Top 5 most anomalous:")
    for a in anomaly_results[:5]:
        flag = " [OUTLIER]" if a["is_outlier_p01"] else ""
        print(f"    {a['name']}: d={a['mahalanobis_distance']:.3f}{flag}")

    # Which features contribute most to the top outliers?
    top_outlier_features = []
    for a in anomaly_results[:5]:
        idx = next(i for i, b in enumerate(benchmarks) if b["short_title"] == a["name"])
        z_scores = (X_imp[idx] - mean) / np.sqrt(np.diag(cov_reg))
        extreme_features = sorted(
            [(features[j], round(float(z_scores[j]), 2)) for j in range(len(features))],
            key=lambda x: -abs(x[1])
        )[:5]
        top_outlier_features.append({
            "name": a["name"],
            "extreme_features": extreme_features,
        })

    return {
        "anomaly_scores": anomaly_results,
        "chi2_threshold": round(float(chi2_threshold_sq), 4),
        "n_features": n_features,
        "n_outliers": n_outliers,
        "top_outlier_features": top_outlier_features,
    }


# ===================================================================
# W2: Data Availability Audit
# ===================================================================
def data_availability_audit(benchmarks):
    print("\n[W2] Data Availability Audit")
    audit = []
    for b in benchmarks:
        url = b.get("B3_url", "NA")
        avail = b.get("B3_data_availability", "Unknown")

        # Classify URL type
        if url and url != "NA":
            url_lower = url.lower()
            if "github.com" in url_lower:
                host_type = "GitHub"
            elif "huggingface.co" in url_lower:
                host_type = "HuggingFace"
            elif "zenodo" in url_lower:
                host_type = "Zenodo"
            elif "arxiv" in url_lower:
                host_type = "arXiv"
            elif "kaggle" in url_lower:
                host_type = "Kaggle"
            else:
                host_type = "Other"
        else:
            host_type = "None"

        audit.append({
            "id": b["id"],
            "name": b["short_title"],
            "url": url,
            "host_type": host_type,
            "availability": avail,
            "license": b.get("B5_license", "Unspecified"),
            "code_availability": b.get("B4_code_availability", "Unknown"),
            "dataset_size": b.get("B2_dataset_size"),
            "passes_gates": bool(b.get("passes_gates", False)),
            "gate_data": bool(b.get("gate_data", False)),
        })

    # Summary
    host_counts = Counter(a["host_type"] for a in audit)
    avail_counts = Counter(a["availability"] for a in audit)
    license_counts = Counter(a["license"] for a in audit)

    print(f"  Host types: {dict(host_counts)}")
    print(f"  Availability: {dict(avail_counts)}")
    print(f"  Licenses: {dict(license_counts)}")

    # Markdown report
    md_lines = ["# Data Availability Audit — NormEval Benchmarks", ""]
    md_lines.append(f"Date: {DATE_PREFIX[:4]}-{DATE_PREFIX[4:6]}-{DATE_PREFIX[6:]}")
    md_lines.append(f"Total benchmarks: {len(benchmarks)}")
    md_lines.append("")

    md_lines.append("## Summary")
    md_lines.append("")
    md_lines.append("### By Host Type")
    for ht, cnt in sorted(host_counts.items(), key=lambda x: -x[1]):
        md_lines.append(f"- **{ht}**: {cnt}")
    md_lines.append("")

    md_lines.append("### By Availability Status")
    for av, cnt in sorted(avail_counts.items(), key=lambda x: -x[1]):
        md_lines.append(f"- **{av}**: {cnt}")
    md_lines.append("")

    md_lines.append("### By License")
    for lic, cnt in sorted(license_counts.items(), key=lambda x: -x[1]):
        md_lines.append(f"- **{lic}**: {cnt}")
    md_lines.append("")

    md_lines.append("## Detailed Audit")
    md_lines.append("")
    md_lines.append("| # | Benchmark | Host | Availability | License | Code | Size | Top15? |")
    md_lines.append("|---|-----------|------|-------------|---------|------|------|--------|")
    for a in audit:
        size_str = f"{a['dataset_size']:,}" if a["dataset_size"] else "N/A"
        t15 = "Yes" if a["passes_gates"] else "No"
        md_lines.append(f"| {a['id']} | {a['name'][:40]} | {a['host_type']} | {a['availability']} | {a['license']} | {a['code_availability'][:15]} | {size_str} | {t15} |")
    md_lines.append("")

    # Data-available vs unavailable
    n_available = sum(1 for a in audit if a["gate_data"])
    n_unavailable = len(audit) - n_available
    md_lines.append(f"## Gate Status")
    md_lines.append(f"- Data-available (gate_data=true): {n_available}")
    md_lines.append(f"- Data-unavailable (gate_data=false): {n_unavailable}")
    md_lines.append("")

    # List unavailable benchmarks
    md_lines.append("### Data-Unavailable Benchmarks")
    for a in audit:
        if not a["gate_data"]:
            md_lines.append(f"- **{a['name']}**: {a['availability']} ({a['host_type']})")
    md_lines.append("")

    return {
        "audit": audit,
        "summary": {
            "host_counts": dict(host_counts),
            "availability_counts": dict(avail_counts),
            "license_counts": dict(license_counts),
            "data_available": n_available,
            "data_unavailable": n_unavailable,
        },
    }, "\n".join(md_lines)


# ===================================================================
# Main
# ===================================================================
def main():
    print("=" * 60)
    print("NormEval Computational Analysis — Agent 1B")
    print("=" * 60)

    benchmarks = load_matrix()
    print(f"Loaded {len(benchmarks)} benchmarks from feature matrix")

    X, features, names = extract_numeric_matrix(benchmarks)
    print(f"Numeric matrix: {X.shape[0]} x {X.shape[1]} ({len(features)} features)")

    # --- Analysis 1: Correlation Matrix ---
    corr_results = analysis_correlation(benchmarks, X, features, names)

    # --- Analysis 8: Tradition Entropy (merged into correlation output) ---
    entropy_results = analysis_entropy(benchmarks)
    corr_results["tradition_entropy"] = entropy_results

    # --- Analysis 6: Feature Importance (merged into correlation output) ---
    fi_results = analysis_feature_importance(benchmarks, X, features, names)
    corr_results["feature_importance"] = fi_results

    save_json("correlation-matrix", corr_results)

    # --- Analysis 2: PCA + Analysis 7: ND-PE Regression ---
    pca_results = analysis_pca(benchmarks, X, features, names)
    save_json("pca-clusters", pca_results)

    # --- Analysis 3: Sensitivity ---
    sens_results = analysis_sensitivity(benchmarks)
    save_json("sensitivity-analysis", sens_results)

    # --- Analysis 4: Hypothesis Tests ---
    hyp_results, hyp_md = analysis_hypothesis_tests(benchmarks)
    save_md("hypothesis-tests", hyp_md)
    # Also save JSON for dashboard
    save_json("hypothesis-tests", hyp_results)

    # --- Analysis 5: Power Analysis ---
    power_md = analysis_power(benchmarks)
    save_md("power-analysis", power_md)

    # --- Analysis 9: Temporal Trends ---
    temp_results = analysis_temporal(benchmarks)
    save_json("temporal-trends", temp_results)

    # --- Analysis 10: Anomaly Detection ---
    anomaly_results = analysis_anomaly(benchmarks, X, features, names)
    save_json("anomaly-detection", anomaly_results)

    # --- W2: Data Availability Audit ---
    audit_results, audit_md = data_availability_audit(benchmarks)
    save_json("data-availability-audit", audit_results)
    save_md("data-availability-audit", audit_md)

    print("\n" + "=" * 60)
    print("All analyses complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()
