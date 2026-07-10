"""
Phase 5: Computational Analyses A (Feature Matrix), B (Benchmark Landscape), C (Temporal)
Analyses 1-14 from the moral psychology benchmarks meta-evaluation plan.

Input:
  - 20260404-extended-feature-matrix-v3.json  (54 benchmarks x 162 features)
  - 20260403-moral-psych-benchmark-candidates.json  (221 candidates)
  - 20260404-vault-sweep-v2-report.json  (71 new candidates)

Output:
  - ANALYSIS/20260404-analyses-A-C.json
"""
from __future__ import annotations

import json
import math
import os
import sys
from pathlib import Path
from collections import Counter

import numpy as np
from scipy import stats
from scipy.cluster.hierarchy import linkage, fcluster, dendrogram
from scipy.spatial.distance import squareform, pdist
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import silhouette_score
import warnings
warnings.filterwarnings("ignore")

# Try UMAP -- available per package check
try:
    import umap
    HAS_UMAP = True
except ImportError:
    HAS_UMAP = False

# ---------- paths ----------
BASE = Path(__file__).resolve().parent.parent  # MORAL-PSYCH/
FM_PATH = BASE / "20260404-extended-feature-matrix-v3.json"
CAND_PATH = BASE / "20260403-moral-psych-benchmark-candidates.json"
SWEEP_PATH = BASE / "20260404-vault-sweep-v2-report.json"
OUT_PATH = BASE / "ANALYSIS" / "20260404-analyses-A-C.json"

# ---------- load data ----------
print("Loading data...")
with open(FM_PATH) as f:
    fm_data = json.load(f)
with open(CAND_PATH) as f:
    cand_data = json.load(f)
with open(SWEEP_PATH) as f:
    sweep_data = json.load(f)

matrix = fm_data["matrix"]  # 54 entries
candidates = cand_data["candidates"]  # 221 entries

# ---------- helpers ----------

def extract_score(entry: dict, feature: str) -> float | None:
    """Extract numeric score from new_scores or original_scores."""
    if feature in entry.get("new_scores", {}):
        v = entry["new_scores"][feature]
        if v is None:
            return None
        if isinstance(v, dict):
            return v.get("score")
        return v
    if feature in entry.get("original_scores", {}):
        return entry["original_scores"][feature]
    return None


def build_feature_matrix(entries: list[dict], features: list[str]) -> np.ndarray:
    """Build n_entries x n_features matrix, NaN for missing."""
    n = len(entries)
    m = len(features)
    X = np.full((n, m), np.nan)
    for i, e in enumerate(entries):
        for j, feat in enumerate(features):
            s = extract_score(e, feat)
            if s is not None:
                X[i, j] = float(s)
    return X


def impute_col_mean(X: np.ndarray) -> np.ndarray:
    """Replace NaN with column mean. If column all NaN, use 0."""
    X_imp = X.copy()
    for j in range(X.shape[1]):
        col = X_imp[:, j]
        mask = np.isnan(col)
        if mask.all():
            X_imp[:, j] = 0.0
        elif mask.any():
            X_imp[mask, j] = np.nanmean(col)
    return X_imp


def safe_float(v):
    """Convert numpy types to Python float for JSON."""
    if isinstance(v, (np.floating, np.integer)):
        if np.isnan(v) or np.isinf(v):
            return None
        return float(v)
    if isinstance(v, float):
        if math.isnan(v) or math.isinf(v):
            return None
    return v


def safe_list(arr):
    """Convert numpy array to list of safe floats."""
    return [safe_float(x) for x in arr]


# ---------- feature definitions ----------

# New features D1-G29
D_FEATS = sorted([k for k in matrix[0]["new_scores"] if k.startswith("D")])
E_FEATS = sorted([k for k in matrix[0]["new_scores"] if k.startswith("E")])
F_FEATS = sorted([k for k in matrix[0]["new_scores"] if k.startswith("F")])
G_FEATS = sorted([k for k in matrix[0]["new_scores"] if k.startswith("G")])
NEW_FEATS = D_FEATS + E_FEATS + F_FEATS + G_FEATS

# Original features A1-C5
ORIG_FEATS = sorted([k for k in matrix[0]["original_scores"] if not k.startswith("P") and k != "CI"])
ALL_FEATS = ORIG_FEATS + NEW_FEATS

print(f"Features: {len(D_FEATS)} D, {len(E_FEATS)} E, {len(F_FEATS)} F, {len(G_FEATS)} G = {len(NEW_FEATS)} new + {len(ORIG_FEATS)} original = {len(ALL_FEATS)} total")

# Build main matrices
X_new = build_feature_matrix(matrix, NEW_FEATS)
X_all = build_feature_matrix(matrix, ALL_FEATS)
X_new_imp = impute_col_mean(X_new)
X_all_imp = impute_col_mean(X_all)

benchmark_names = [e["short_title"] for e in matrix]
benchmark_years = [e["year"] for e in matrix]
benchmark_has_trial = [e["has_trial"] for e in matrix]

print(f"Matrix shape (new features): {X_new.shape}")
print(f"Matrix shape (all features): {X_all.shape}")

results = {}

# ============================================================
# A1. Exploratory Factor Analysis
# ============================================================
print("\n=== A1: Factor Analysis ===")

# PCA for scree plot
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_new_imp)

pca_full = PCA()
pca_full.fit(X_scaled)

eigenvalues = pca_full.explained_variance_
var_ratios = pca_full.explained_variance_ratio_
cum_var = np.cumsum(var_ratios)

# Parallel analysis: compare with random data eigenvalues
n_iter = 100
n_samples, n_features = X_scaled.shape
random_eigenvalues = np.zeros((n_iter, min(n_samples, n_features)))
for i in range(n_iter):
    random_data = np.random.normal(size=(n_samples, n_features))
    random_pca = PCA()
    random_pca.fit(random_data)
    random_eigenvalues[i] = random_pca.explained_variance_

# 95th percentile of random eigenvalues
threshold = np.percentile(random_eigenvalues, 95, axis=0)
suggested_factors = int(np.sum(eigenvalues > threshold))

# Kaiser criterion (eigenvalue > 1 for correlation-matrix PCA)
# Since we used StandardScaler, eigenvalue > 1 in original units maps to
# explained_variance > (total_var / n_features)
kaiser_count = int(np.sum(eigenvalues > 1.0))

# How do factors align with D/E/F/G tiers?
# Get loadings for first few components
n_show = min(suggested_factors, 10)
loadings = pca_full.components_[:n_show]  # n_show x n_features

# For each component, find dominant tier
tier_alignment = []
for comp_idx in range(n_show):
    abs_loadings = np.abs(loadings[comp_idx])
    tier_loads = {
        "D": np.mean(abs_loadings[:len(D_FEATS)]),
        "E": np.mean(abs_loadings[len(D_FEATS):len(D_FEATS)+len(E_FEATS)]),
        "F": np.mean(abs_loadings[len(D_FEATS)+len(E_FEATS):len(D_FEATS)+len(E_FEATS)+len(F_FEATS)]),
        "G": np.mean(abs_loadings[len(D_FEATS)+len(E_FEATS)+len(F_FEATS):])
    }
    dominant = max(tier_loads, key=tier_loads.get)
    tier_alignment.append({
        "component": comp_idx + 1,
        "dominant_tier": dominant,
        "tier_mean_abs_loadings": {k: round(v, 4) for k, v in tier_loads.items()},
        "variance_explained_pct": round(float(var_ratios[comp_idx]) * 100, 2)
    })

# Summary text
aligned_tiers = set(ta["dominant_tier"] for ta in tier_alignment[:4])
if aligned_tiers == {"D", "E", "F", "G"}:
    align_text = "Strong alignment: first 4 components each dominated by a different tier (D/E/F/G), confirming the a priori structure."
elif len(aligned_tiers) >= 3:
    align_text = f"Partial alignment: first {n_show} components span {len(aligned_tiers)} of 4 tiers. Some tiers share components."
else:
    align_text = f"Weak alignment: first {n_show} components dominated by only {len(aligned_tiers)} tier(s). Tier structure not empirically recovered."

results["A1_factor_analysis"] = {
    "eigenvalues_top20": safe_list(eigenvalues[:20]),
    "variance_explained_top20": safe_list(var_ratios[:20]),
    "cumulative_variance_top20": safe_list(cum_var[:20]),
    "parallel_analysis_threshold_top20": safe_list(threshold[:20]),
    "suggested_factors_parallel": suggested_factors,
    "kaiser_criterion_count": kaiser_count,
    "component_tier_alignment": tier_alignment,
    "tier_alignment_summary": align_text,
    "total_variance_first5": round(float(cum_var[4]) * 100, 2) if len(cum_var) >= 5 else None,
    "total_variance_first10": round(float(cum_var[9]) * 100, 2) if len(cum_var) >= 10 else None
}
print(f"  Suggested factors (parallel): {suggested_factors}")
print(f"  Kaiser criterion: {kaiser_count}")
print(f"  Variance explained (5 PC): {cum_var[4]*100:.1f}%")
print(f"  Tier alignment: {align_text}")


# ============================================================
# A2. Feature Correlation Structure
# ============================================================
print("\n=== A2: Correlation Structure ===")

corr_matrix = np.corrcoef(X_new_imp.T)  # n_features x n_features

# Highly correlated pairs (r > 0.80)
high_corr_pairs = []
for i in range(len(NEW_FEATS)):
    for j in range(i + 1, len(NEW_FEATS)):
        r = corr_matrix[i, j]
        if not np.isnan(r) and abs(r) > 0.80:
            high_corr_pairs.append({
                "feature_1": NEW_FEATS[i],
                "feature_2": NEW_FEATS[j],
                "r": round(float(r), 4)
            })
high_corr_pairs.sort(key=lambda x: abs(x["r"]), reverse=True)

# Hierarchical clustering of features at r=0.70 threshold
# Distance = 1 - |correlation|
# Replace NaN correlations (from zero-variance features) with 0 before computing distance
corr_matrix_clean = np.nan_to_num(corr_matrix, nan=0.0)
dist_matrix = 1.0 - np.abs(corr_matrix_clean)
np.fill_diagonal(dist_matrix, 0)
# Ensure symmetry and non-negative
dist_matrix = np.maximum(dist_matrix, 0)
dist_matrix = (dist_matrix + dist_matrix.T) / 2.0
# Replace any remaining non-finite values
dist_matrix = np.nan_to_num(dist_matrix, nan=1.0, posinf=1.0, neginf=0.0)

condensed_dist = squareform(dist_matrix, checks=False)
Z = linkage(condensed_dist, method="average")
clusters_070 = fcluster(Z, t=0.30, criterion="distance")  # 1 - 0.70 = 0.30

n_clusters = len(set(clusters_070))
cluster_map = {}
for idx, cl in enumerate(clusters_070):
    cl = int(cl)
    if cl not in cluster_map:
        cluster_map[cl] = []
    cluster_map[cl].append(NEW_FEATS[idx])

# Find multi-member clusters
multi_clusters = {k: v for k, v in cluster_map.items() if len(v) > 1}

# Bridge features: features that correlate moderately (0.4 < r < 0.7) with features in multiple clusters
bridge_features = []
for feat_idx, feat in enumerate(NEW_FEATS):
    connected_clusters = set()
    for other_idx, other in enumerate(NEW_FEATS):
        if feat_idx == other_idx:
            continue
        r = abs(corr_matrix[feat_idx, other_idx])
        if 0.4 < r < 0.7:
            connected_clusters.add(int(clusters_070[other_idx]))
    if len(connected_clusters) >= 3:
        bridge_features.append({
            "feature": feat,
            "connects_clusters": len(connected_clusters),
            "own_cluster": int(clusters_070[feat_idx])
        })
bridge_features.sort(key=lambda x: x["connects_clusters"], reverse=True)

results["A2_correlation_structure"] = {
    "high_corr_pairs_above_080": high_corr_pairs[:30],
    "n_high_corr_pairs": len(high_corr_pairs),
    "n_clusters_at_070": n_clusters,
    "multi_member_clusters": {str(k): v for k, v in sorted(multi_clusters.items())},
    "n_multi_member_clusters": len(multi_clusters),
    "bridge_features_top10": bridge_features[:10],
    "mean_abs_correlation": round(float(np.mean(np.abs(corr_matrix[np.triu_indices_from(corr_matrix, k=1)]))), 4)
}
print(f"  High-corr pairs (r>0.80): {len(high_corr_pairs)}")
print(f"  Clusters at r=0.70: {n_clusters}")
print(f"  Multi-member clusters: {len(multi_clusters)}")
print(f"  Bridge features: {len(bridge_features)}")


# ============================================================
# A3. Feature Importance Ranking
# ============================================================
print("\n=== A3: Feature Importance ===")

feature_stats = []
for j, feat in enumerate(NEW_FEATS):
    col = X_new[:, j]
    non_null = np.sum(~np.isnan(col))
    pct_non_null = round(float(non_null / len(col) * 100), 1)
    if non_null > 1:
        variance = float(np.nanvar(col))
        mean_val = float(np.nanmean(col))
    else:
        variance = 0.0
        mean_val = 0.0
    feature_stats.append({
        "feature": feat,
        "tier": feat[0],
        "variance": round(variance, 2),
        "mean": round(mean_val, 2),
        "pct_non_null": pct_non_null,
        "n_non_null": int(non_null)
    })

# Sort by variance descending
by_variance = sorted(feature_stats, key=lambda x: x["variance"], reverse=True)

# Dead features
dead_features = [f for f in feature_stats if f["variance"] < 1.0 or f["pct_non_null"] < 10.0]
zero_variance = [f for f in feature_stats if f["variance"] == 0.0]

results["A3_feature_importance"] = {
    "top20_most_discriminating": by_variance[:20],
    "bottom20_least_discriminating": by_variance[-20:],
    "dead_features_count": len(dead_features),
    "dead_features": [f["feature"] for f in dead_features],
    "zero_variance_features": [f["feature"] for f in zero_variance],
    "tier_mean_variance": {
        "D": round(float(np.mean([f["variance"] for f in feature_stats if f["tier"] == "D"])), 2),
        "E": round(float(np.mean([f["variance"] for f in feature_stats if f["tier"] == "E"])), 2),
        "F": round(float(np.mean([f["variance"] for f in feature_stats if f["tier"] == "F"])), 2),
        "G": round(float(np.mean([f["variance"] for f in feature_stats if f["tier"] == "G"])), 2)
    }
}
print(f"  Dead features (var<1 or >90% null): {len(dead_features)}")
print(f"  Zero variance: {len(zero_variance)}")
print(f"  Top discriminator: {by_variance[0]['feature']} (var={by_variance[0]['variance']})")


# ============================================================
# A4. Redundancy Analysis
# ============================================================
print("\n=== A4: Redundancy Analysis ===")

redundant_pairs = []
for i in range(len(NEW_FEATS)):
    for j in range(i + 1, len(NEW_FEATS)):
        r = corr_matrix[i, j]
        if not np.isnan(r) and abs(r) > 0.85:
            redundant_pairs.append({
                "feature_1": NEW_FEATS[i],
                "feature_2": NEW_FEATS[j],
                "r": round(float(r), 4)
            })
redundant_pairs.sort(key=lambda x: abs(x["r"]), reverse=True)

# Map redundancy clusters via connected components
from collections import defaultdict

adj = defaultdict(set)
for pair in redundant_pairs:
    adj[pair["feature_1"]].add(pair["feature_2"])
    adj[pair["feature_2"]].add(pair["feature_1"])

visited = set()
redundancy_clusters = []
for feat in adj:
    if feat in visited:
        continue
    # BFS
    cluster = []
    queue = [feat]
    while queue:
        node = queue.pop(0)
        if node in visited:
            continue
        visited.add(node)
        cluster.append(node)
        for neighbor in adj[node]:
            if neighbor not in visited:
                queue.append(neighbor)
    if len(cluster) > 1:
        redundancy_clusters.append(sorted(cluster))

# For each cluster, suggest which to keep (highest variance)
collapse_suggestions = []
var_lookup = {f["feature"]: f["variance"] for f in feature_stats}
for cl in redundancy_clusters:
    best = max(cl, key=lambda x: var_lookup.get(x, 0))
    collapse_suggestions.append({
        "cluster": cl,
        "keep": best,
        "drop": [f for f in cl if f != best],
        "max_internal_r": max(
            abs(corr_matrix[NEW_FEATS.index(a), NEW_FEATS.index(b)])
            for a in cl for b in cl if a != b
        ) if len(cl) > 1 else None
    })

results["A4_redundancy_analysis"] = {
    "n_redundant_pairs_above_085": len(redundant_pairs),
    "redundant_pairs": redundant_pairs[:20],
    "n_redundancy_clusters": len(redundancy_clusters),
    "redundancy_clusters": redundancy_clusters,
    "collapse_suggestions": collapse_suggestions,
    "features_in_redundant_clusters": sum(len(c) for c in redundancy_clusters),
    "potential_reduction": sum(len(c) - 1 for c in redundancy_clusters)
}
print(f"  Redundant pairs (r>0.85): {len(redundant_pairs)}")
print(f"  Redundancy clusters: {len(redundancy_clusters)}")
print(f"  Potential feature reduction: {sum(len(c)-1 for c in redundancy_clusters)}")


# ============================================================
# A5. Tier Composite Analysis
# ============================================================
print("\n=== A5: Tier Composite Analysis ===")

tier_means = {"D": [], "E": [], "F": [], "G": []}
composites = []
for entry in matrix:
    tc = entry.get("tier_composites", {})
    for tier in ["D", "E", "F", "G"]:
        tier_means[tier].append(tc.get(f"{tier}_mean", np.nan))
    composites.append(entry.get("composite", np.nan))

tier_means_arr = {k: np.array(v) for k, v in tier_means.items()}
composites_arr = np.array(composites)

# Correlate each tier mean with original composite
tier_corr = {}
for tier in ["D", "E", "F", "G"]:
    valid = ~np.isnan(tier_means_arr[tier]) & ~np.isnan(composites_arr)
    if valid.sum() > 3:
        r, p = stats.pearsonr(tier_means_arr[tier][valid], composites_arr[valid])
        rho, rho_p = stats.spearmanr(tier_means_arr[tier][valid], composites_arr[valid])
        tier_corr[tier] = {
            "pearson_r": round(float(r), 4),
            "pearson_p": round(float(p), 6),
            "spearman_rho": round(float(rho), 4),
            "spearman_p": round(float(rho_p), 6),
            "mean": round(float(np.nanmean(tier_means_arr[tier])), 2),
            "std": round(float(np.nanstd(tier_means_arr[tier])), 2)
        }
    else:
        tier_corr[tier] = {"pearson_r": None, "note": "insufficient data"}

# Inter-tier correlations
inter_tier = {}
for t1 in ["D", "E", "F", "G"]:
    for t2 in ["D", "E", "F", "G"]:
        if t1 >= t2:
            continue
        valid = ~np.isnan(tier_means_arr[t1]) & ~np.isnan(tier_means_arr[t2])
        if valid.sum() > 3:
            r, p = stats.pearsonr(tier_means_arr[t1][valid], tier_means_arr[t2][valid])
            inter_tier[f"{t1}-{t2}"] = {
                "pearson_r": round(float(r), 4),
                "pearson_p": round(float(p), 6)
            }

# Are new tiers orthogonal?
all_rs = [abs(v["pearson_r"]) for v in tier_corr.values() if v.get("pearson_r") is not None]
mean_abs_r = np.mean(all_rs) if all_rs else 0
if mean_abs_r > 0.7:
    ortho_text = "New tiers strongly predict original composite -- they are extensions, not orthogonal dimensions."
elif mean_abs_r > 0.4:
    ortho_text = "New tiers moderately correlate with original composite -- partially overlapping information."
else:
    ortho_text = "New tiers are largely orthogonal to original composite -- they capture genuinely new dimensions."

results["A5_tier_composite"] = {
    "tier_vs_composite_correlations": tier_corr,
    "inter_tier_correlations": inter_tier,
    "orthogonality_assessment": ortho_text,
    "mean_abs_r_with_composite": round(float(mean_abs_r), 4),
    "composite_stats": {
        "mean": round(float(np.nanmean(composites_arr)), 2),
        "std": round(float(np.nanstd(composites_arr)), 2),
        "min": round(float(np.nanmin(composites_arr)), 2),
        "max": round(float(np.nanmax(composites_arr)), 2)
    }
}
print(f"  Mean |r| tier-vs-composite: {mean_abs_r:.3f}")
print(f"  {ortho_text}")


# ============================================================
# B6. Benchmark Clustering
# ============================================================
print("\n=== B6: Benchmark Clustering ===")

X_cluster = X_all_imp.copy()
X_cluster_scaled = StandardScaler().fit_transform(X_cluster)

# Silhouette scores for k=2..10
sil_scores = {}
cluster_assignments = {}
for k in range(2, 11):
    agg = AgglomerativeClustering(n_clusters=k, linkage="ward")
    labels = agg.fit_predict(X_cluster_scaled)
    sil = silhouette_score(X_cluster_scaled, labels)
    sil_scores[k] = round(float(sil), 4)
    cluster_assignments[k] = labels.tolist()

optimal_k = max(sil_scores, key=sil_scores.get)
best_labels = cluster_assignments[optimal_k]

# Archetype labels: compute cluster means on tier composites
archetype_info = []
for cl in range(optimal_k):
    members = [i for i, l in enumerate(best_labels) if l == cl]
    member_names = [benchmark_names[i] for i in members]
    cl_tier_means = {}
    for tier in ["D", "E", "F", "G"]:
        vals = [tier_means_arr[tier][i] for i in members if not np.isnan(tier_means_arr[tier][i])]
        cl_tier_means[tier] = round(float(np.mean(vals)), 1) if vals else None
    cl_composite = [composites[i] for i in members if not np.isnan(composites[i])]
    mean_comp = round(float(np.mean(cl_composite)), 1) if cl_composite else None

    # Generate archetype label based on feature profile
    dominant_tiers = []
    if cl_tier_means.get("D") and cl_tier_means["D"] > 35:
        dominant_tiers.append("Psychometric")
    if cl_tier_means.get("E") and cl_tier_means["E"] > 20:
        dominant_tiers.append("LLM-Adapted")
    if cl_tier_means.get("F") and cl_tier_means["F"] > 20:
        dominant_tiers.append("Socially-Aware")
    if cl_tier_means.get("G") and cl_tier_means["G"] > 40:
        dominant_tiers.append("Future-Ready")
    label = "+".join(dominant_tiers) if dominant_tiers else "Minimal"

    archetype_info.append({
        "cluster": cl,
        "archetype_label": label,
        "size": len(members),
        "tier_means": cl_tier_means,
        "mean_composite": mean_comp,
        "members": member_names
    })

# 2D UMAP projection
umap_coords = None
if HAS_UMAP:
    try:
        reducer = umap.UMAP(n_components=2, random_state=42, n_neighbors=min(15, len(X_cluster_scaled) - 1))
        embedding = reducer.fit_transform(X_cluster_scaled)
        umap_coords = [
            {"benchmark": benchmark_names[i], "x": round(float(embedding[i, 0]), 4), "y": round(float(embedding[i, 1]), 4), "cluster": int(best_labels[i])}
            for i in range(len(benchmark_names))
        ]
    except Exception as e:
        print(f"  UMAP failed: {e}")

results["B6_benchmark_clustering"] = {
    "silhouette_scores": sil_scores,
    "optimal_k": optimal_k,
    "cluster_archetypes": archetype_info,
    "umap_2d": umap_coords,
    "method": "Ward linkage agglomerative clustering on StandardScaled features"
}
print(f"  Optimal k: {optimal_k} (silhouette={sil_scores[optimal_k]})")
for a in archetype_info:
    print(f"  Cluster {a['cluster']}: {a['archetype_label']} (n={a['size']})")


# ============================================================
# B7. Theory Coverage Landscape
# ============================================================
print("\n=== B7: Theory Coverage ===")

# 11 theories from mp_scores + vault sweep theories
theories_main = ["mp_mft", "mp_schwartz", "mp_trolley", "mp_kohlberg",
                 "mp_dual_process", "mp_intuitionist", "mp_dyadic", "mp_identity"]
theories_sweep = ["islamic", "confucian", "ubuntu", "buddhist", "indigenous"]

# Count from candidates (221)
theory_counts = {}
for t in theories_main:
    theory_counts[t] = sum(1 for c in candidates if c.get("mp_scores", {}).get(t, 0) >= 50)

# Add vault sweep counts
sweep_summary = sweep_data.get("summary", {}).get("by_theory", {})
for t in theories_sweep:
    theory_counts[t] = sweep_summary.get(t, len(sweep_data.get("theory_hits", {}).get(t, [])))

# Shannon entropy
total_count = sum(theory_counts.values())
if total_count > 0:
    probs = [c / total_count for c in theory_counts.values() if c > 0]
    shannon_entropy = -sum(p * math.log2(p) for p in probs)
    max_entropy = math.log2(len(theory_counts))
    evenness = shannon_entropy / max_entropy if max_entropy > 0 else 0
else:
    shannon_entropy = 0
    evenness = 0

# Deserts and monocultures
deserts = [t for t, c in theory_counts.items() if c == 0]
near_deserts = [t for t, c in theory_counts.items() if 0 < c <= 3]
monocultures = sorted(theory_counts.items(), key=lambda x: x[1], reverse=True)[:3]

results["B7_theory_coverage"] = {
    "theory_counts": theory_counts,
    "total_candidates": len(candidates),
    "total_sweep_new": 71,
    "shannon_entropy": round(shannon_entropy, 4),
    "max_possible_entropy": round(max_entropy, 4),
    "evenness_index": round(evenness, 4),
    "deserts_zero_coverage": deserts,
    "near_deserts_1to3": near_deserts,
    "top3_monocultures": [{"theory": t, "count": c} for t, c in monocultures],
    "mft_dominance_pct": round(theory_counts.get("mp_mft", 0) / total_count * 100, 1) if total_count > 0 else 0
}
print(f"  Shannon entropy: {shannon_entropy:.3f} (max {max_entropy:.3f}, evenness {evenness:.3f})")
print(f"  Deserts: {deserts}")
print(f"  MFT dominance: {theory_counts.get('mp_mft', 0)}/{total_count} = {theory_counts.get('mp_mft', 0)/total_count*100:.1f}%")


# ============================================================
# B8. Theory-Feature Gap Matrix
# ============================================================
print("\n=== B8: Theory-Feature Gap Matrix ===")

# For each of the 54 scored benchmarks, identify primary theory from candidates data
# Build lookup by filename
cand_lookup = {c["file"]: c for c in candidates}

benchmark_theories = []
for entry in matrix:
    cand = cand_lookup.get(entry["file"], {})
    mp_scores = cand.get("mp_scores", {})
    # Primary theory = highest mp_score
    if mp_scores:
        primary = max(mp_scores.items(), key=lambda x: x[1])
        benchmark_theories.append(primary[0] if primary[1] >= 50 else "none")
    else:
        benchmark_theories.append("none")

# Cross-tab: theory x tier mean
theory_tier_means = {}
theory_tier_entropy = {}
for theory in set(benchmark_theories):
    if theory == "none":
        continue
    indices = [i for i, t in enumerate(benchmark_theories) if t == theory]
    if not indices:
        continue
    tier_vals = {}
    for tier in ["D", "E", "F", "G"]:
        vals = [tier_means_arr[tier][i] for i in indices if not np.isnan(tier_means_arr[tier][i])]
        tier_vals[tier] = round(float(np.mean(vals)), 2) if vals else None
    theory_tier_means[theory] = {
        "n_benchmarks": len(indices),
        "tier_means": tier_vals
    }
    # Per-theory entropy: how diverse are benchmarks within this theory?
    if len(indices) > 1:
        features_for_theory = X_new_imp[indices]
        variances = np.var(features_for_theory, axis=0)
        mean_var = float(np.mean(variances))
        theory_tier_entropy[theory] = round(mean_var, 2)
    else:
        theory_tier_entropy[theory] = 0.0

# Zero-coverage theory x tier
gaps = []
for theory, info in theory_tier_means.items():
    for tier, val in info["tier_means"].items():
        if val is not None and val < 10:
            gaps.append({"theory": theory, "tier": tier, "mean": val})

results["B8_theory_feature_gap"] = {
    "theory_tier_means": theory_tier_means,
    "theory_internal_variance": theory_tier_entropy,
    "low_coverage_gaps": gaps,
    "note": "Theory assigned by highest mp_score among 54 scored benchmarks"
}
print(f"  Theories represented in scored benchmarks: {len(theory_tier_means)}")
print(f"  Low-coverage gaps (mean<10): {len(gaps)}")


# ============================================================
# B9. Benchmark Completeness
# ============================================================
print("\n=== B9: Benchmark Completeness ===")

completeness = []
for i, entry in enumerate(matrix):
    non_null = 0
    total = len(NEW_FEATS)
    for feat in NEW_FEATS:
        s = extract_score(entry, feat)
        if s is not None:
            non_null += 1
    pct = round(non_null / total * 100, 1)
    completeness.append({
        "benchmark": entry["short_title"],
        "pct_complete": pct,
        "n_scored": non_null,
        "n_total": total,
        "has_trial": entry["has_trial"]
    })

completeness.sort(key=lambda x: x["pct_complete"], reverse=True)

# Compare trialed vs non-trialed
trialed = [c for c in completeness if c["has_trial"]]
non_trialed = [c for c in completeness if not c["has_trial"]]
mean_trialed = np.mean([c["pct_complete"] for c in trialed]) if trialed else 0
mean_non_trialed = np.mean([c["pct_complete"] for c in non_trialed]) if non_trialed else 0

# Mann-Whitney test
if trialed and non_trialed:
    u_stat, u_p = stats.mannwhitneyu(
        [c["pct_complete"] for c in trialed],
        [c["pct_complete"] for c in non_trialed],
        alternative="two-sided"
    )
else:
    u_stat, u_p = None, None

results["B9_benchmark_completeness"] = {
    "completeness_ranking": completeness,
    "mean_pct_complete": round(float(np.mean([c["pct_complete"] for c in completeness])), 1),
    "trialed_mean": round(float(mean_trialed), 1),
    "non_trialed_mean": round(float(mean_non_trialed), 1),
    "trialed_count": len(trialed),
    "non_trialed_count": len(non_trialed),
    "mann_whitney_U": safe_float(u_stat),
    "mann_whitney_p": safe_float(u_p),
    "trialed_advantage": "Yes" if mean_trialed > mean_non_trialed else "No"
}
print(f"  Mean completeness: {np.mean([c['pct_complete'] for c in completeness]):.1f}%")
print(f"  Trialed: {mean_trialed:.1f}% vs Non-trialed: {mean_non_trialed:.1f}%")
print(f"  Mann-Whitney p={u_p}")


# ============================================================
# B10. Composite Score Distribution
# ============================================================
print("\n=== B10: Composite Distribution ===")

# From all 221 candidates, get composite if available (or compute from mp_scores)
# The feature matrix has composites for 54 -- use those
# For other candidates, report what we have (mp_max)
all_composites = [e.get("composite") for e in matrix if e.get("composite") is not None]

# Histogram bins
hist_counts, hist_edges = np.histogram(all_composites, bins=10)

# Tier-level distributions (box plot data)
tier_dist = {}
for tier in ["D", "E", "F", "G"]:
    vals = [v for v in tier_means_arr[tier] if not np.isnan(v)]
    if vals:
        arr = np.array(vals)
        tier_dist[tier] = {
            "min": round(float(np.min(arr)), 2),
            "q1": round(float(np.percentile(arr, 25)), 2),
            "median": round(float(np.median(arr)), 2),
            "q3": round(float(np.percentile(arr, 75)), 2),
            "max": round(float(np.max(arr)), 2),
            "mean": round(float(np.mean(arr)), 2),
            "std": round(float(np.std(arr)), 2)
        }

# Outliers (> 1.5 IQR)
comp_arr = np.array(all_composites)
q1 = np.percentile(comp_arr, 25)
q3 = np.percentile(comp_arr, 75)
iqr = q3 - q1
outlier_low = q1 - 1.5 * iqr
outlier_high = q3 + 1.5 * iqr
outliers = []
for i, entry in enumerate(matrix):
    c = entry.get("composite")
    if c is not None and (c < outlier_low or c > outlier_high):
        outliers.append({"benchmark": entry["short_title"], "composite": c, "direction": "high" if c > outlier_high else "low"})

results["B10_composite_distribution"] = {
    "n_scored": len(all_composites),
    "histogram_counts": hist_counts.tolist(),
    "histogram_edges": safe_list(hist_edges),
    "descriptive": {
        "mean": round(float(np.mean(comp_arr)), 2),
        "std": round(float(np.std(comp_arr)), 2),
        "min": round(float(np.min(comp_arr)), 2),
        "q1": round(float(q1), 2),
        "median": round(float(np.median(comp_arr)), 2),
        "q3": round(float(q3), 2),
        "max": round(float(np.max(comp_arr)), 2),
        "skewness": round(float(stats.skew(comp_arr)), 4),
        "kurtosis": round(float(stats.kurtosis(comp_arr)), 4)
    },
    "tier_distributions": tier_dist,
    "outliers": outliers,
    "iqr_bounds": {"low": round(float(outlier_low), 2), "high": round(float(outlier_high), 2)}
}
print(f"  Composite: mean={np.mean(comp_arr):.1f}, std={np.std(comp_arr):.1f}")
print(f"  Range: [{np.min(comp_arr):.1f}, {np.max(comp_arr):.1f}]")
print(f"  Outliers: {len(outliers)}")


# ============================================================
# C11. Temporal Trends
# ============================================================
print("\n=== C11: Temporal Trends ===")

years_arr = np.array(benchmark_years, dtype=float)
unique_years = sorted(set(benchmark_years))

# Per-year means for key features
yearly_stats = {}
for year in unique_years:
    idx = [i for i, y in enumerate(benchmark_years) if y == year]
    if not idx:
        continue
    yearly_stats[year] = {
        "n": len(idx),
        "A6_mean": round(float(np.nanmean([extract_score(matrix[i], "A6") or np.nan for i in idx])), 2),
        "D_mean": round(float(np.nanmean([tier_means_arr["D"][i] for i in idx])), 2),
        "E_mean": round(float(np.nanmean([tier_means_arr["E"][i] for i in idx])), 2),
        "F_mean": round(float(np.nanmean([tier_means_arr["F"][i] for i in idx])), 2),
        "G_mean": round(float(np.nanmean([tier_means_arr["G"][i] for i in idx])), 2),
        "composite_mean": round(float(np.nanmean([composites[i] for i in idx])), 2)
    }

# Spearman trend test: feature vs year
trend_tests = {}
features_to_test = {
    "A6": [extract_score(matrix[i], "A6") for i in range(len(matrix))],
    "D_mean": list(tier_means_arr["D"]),
    "E_mean": list(tier_means_arr["E"]),
    "F_mean": list(tier_means_arr["F"]),
    "G_mean": list(tier_means_arr["G"]),
    "composite": composites
}

for feat_name, values in features_to_test.items():
    vals = np.array(values, dtype=float)
    valid = ~np.isnan(vals) & ~np.isnan(years_arr)
    if valid.sum() > 5:
        rho, p = stats.spearmanr(years_arr[valid], vals[valid])
        trend_tests[feat_name] = {
            "spearman_rho": round(float(rho), 4),
            "p_value": round(float(p), 6),
            "significant_005": bool(p < 0.05),
            "direction": "improving" if rho > 0 else "declining" if rho < 0 else "flat",
            "n": int(valid.sum())
        }

improving = [k for k, v in trend_tests.items() if v.get("significant_005") and v.get("direction") == "improving"]
declining = [k for k, v in trend_tests.items() if v.get("significant_005") and v.get("direction") == "declining"]
stagnant = [k for k, v in trend_tests.items() if not v.get("significant_005")]

results["C11_temporal_trends"] = {
    "yearly_stats": {str(k): v for k, v in yearly_stats.items()},
    "trend_tests": trend_tests,
    "improving_features": improving,
    "declining_features": declining,
    "stagnant_features": stagnant,
    "year_range": {"min": min(benchmark_years), "max": max(benchmark_years)},
    "n_benchmarks": len(benchmark_years)
}
print(f"  Year range: {min(benchmark_years)}-{max(benchmark_years)}")
print(f"  Improving: {improving}")
print(f"  Declining: {declining}")
print(f"  Stagnant: {stagnant}")


# ============================================================
# C12. Theory Evolution
# ============================================================
print("\n=== C12: Theory Evolution ===")

# From all 221 candidates: count theory detections per year
theory_by_year = {}
for c in candidates:
    year = c.get("year")
    if year is None:
        continue
    if year not in theory_by_year:
        theory_by_year[year] = Counter()
    mp = c.get("mp_scores", {})
    for t in theories_main:
        if mp.get(t, 0) >= 50:
            theory_by_year[year][t] += 1

# Add sweep candidates (they don't have year in sweep -- use theory only)
# For sweep, we have theory labels but no year -- skip for per-year analysis

# Sort by year
yearly_theory = {}
for year in sorted(theory_by_year.keys()):
    yearly_theory[str(year)] = dict(theory_by_year[year])

# MFT dominance trend
mft_by_year = {}
total_by_year = {}
for year in sorted(theory_by_year.keys()):
    mft_by_year[year] = theory_by_year[year].get("mp_mft", 0)
    total_by_year[year] = sum(theory_by_year[year].values())

# Spearman: MFT share vs year
if len(mft_by_year) > 3:
    y_vals = sorted(mft_by_year.keys())
    mft_shares = [mft_by_year[y] / total_by_year[y] if total_by_year[y] > 0 else 0 for y in y_vals]
    rho_mft, p_mft = stats.spearmanr(y_vals, mft_shares)
else:
    rho_mft, p_mft = None, None

# Emerging theories
emerging = {}
for theory in theories_sweep:
    sweep_hits = len(sweep_data.get("theory_hits", {}).get(theory, []))
    # Count from candidates
    cand_hits = sum(1 for c in candidates
                    if c.get("moral_psychology", "").lower().find(theory) >= 0)
    emerging[theory] = {
        "candidates_221": cand_hits,
        "sweep_new": sweep_hits,
        "total": cand_hits + sweep_hits,
        "emerging": sweep_hits > 0
    }

results["C12_theory_evolution"] = {
    "theory_by_year": yearly_theory,
    "mft_dominance_trend": {
        "spearman_rho": safe_float(rho_mft),
        "p_value": safe_float(p_mft),
        "direction": "increasing" if rho_mft and rho_mft > 0 else "decreasing" if rho_mft and rho_mft < 0 else "unknown",
        "shares_by_year": {str(y): round(mft_by_year[y] / total_by_year[y] * 100, 1) if total_by_year[y] > 0 else 0 for y in sorted(mft_by_year.keys())}
    },
    "emerging_theories": emerging,
    "n_candidates_with_year": sum(1 for c in candidates if c.get("year") is not None)
}
print(f"  MFT trend: rho={rho_mft}, p={p_mft}")
for t, info in emerging.items():
    print(f"  {t}: {info['total']} total ({info['candidates_221']} cand + {info['sweep_new']} sweep)")


# ============================================================
# C13. Pre/Post RLHF Comparison
# ============================================================
print("\n=== C13: Pre/Post RLHF Comparison ===")

# Split at 2022
pre_idx = [i for i, y in enumerate(benchmark_years) if y < 2022]
post_idx = [i for i, y in enumerate(benchmark_years) if y >= 2022]

pre_post_tests = {}
for tier in ["D", "E", "F", "G"]:
    pre_vals = [tier_means_arr[tier][i] for i in pre_idx if not np.isnan(tier_means_arr[tier][i])]
    post_vals = [tier_means_arr[tier][i] for i in post_idx if not np.isnan(tier_means_arr[tier][i])]
    if len(pre_vals) >= 2 and len(post_vals) >= 2:
        u_stat, u_p = stats.mannwhitneyu(pre_vals, post_vals, alternative="two-sided")
        # Also try t-test
        t_stat, t_p = stats.ttest_ind(pre_vals, post_vals, equal_var=False)
        pre_post_tests[tier] = {
            "pre_n": len(pre_vals),
            "post_n": len(post_vals),
            "pre_mean": round(float(np.mean(pre_vals)), 2),
            "post_mean": round(float(np.mean(post_vals)), 2),
            "diff": round(float(np.mean(post_vals) - np.mean(pre_vals)), 2),
            "mann_whitney_U": safe_float(u_stat),
            "mann_whitney_p": safe_float(u_p),
            "welch_t": safe_float(t_stat),
            "welch_p": safe_float(t_p),
            "significant_005": bool(u_p < 0.05)
        }
    else:
        pre_post_tests[tier] = {
            "pre_n": len(pre_vals),
            "post_n": len(post_vals),
            "note": "insufficient sample"
        }

# Also test composite
pre_comp = [composites[i] for i in pre_idx if not np.isnan(composites[i])]
post_comp = [composites[i] for i in post_idx if not np.isnan(composites[i])]
if len(pre_comp) >= 2 and len(post_comp) >= 2:
    u_stat, u_p = stats.mannwhitneyu(pre_comp, post_comp, alternative="two-sided")
    t_stat, t_p = stats.ttest_ind(pre_comp, post_comp, equal_var=False)
    pre_post_tests["composite"] = {
        "pre_n": len(pre_comp),
        "post_n": len(post_comp),
        "pre_mean": round(float(np.mean(pre_comp)), 2),
        "post_mean": round(float(np.mean(post_comp)), 2),
        "diff": round(float(np.mean(post_comp) - np.mean(pre_comp)), 2),
        "mann_whitney_U": safe_float(u_stat),
        "mann_whitney_p": safe_float(u_p),
        "welch_t": safe_float(t_stat),
        "welch_p": safe_float(t_p),
        "significant_005": bool(u_p < 0.05)
    }

sig_tiers = [t for t, v in pre_post_tests.items() if v.get("significant_005")]

results["C13_pre_post_rlhf"] = {
    "split_year": 2022,
    "pre_count": len(pre_idx),
    "post_count": len(post_idx),
    "tier_comparisons": pre_post_tests,
    "significant_differences": sig_tiers,
    "summary": f"{'|'.join(sig_tiers) if sig_tiers else 'No tiers'} show significant pre/post-RLHF differences at p<0.05."
}
print(f"  Pre-2022: {len(pre_idx)}, Post-2022: {len(post_idx)}")
for t, v in pre_post_tests.items():
    if "pre_mean" in v:
        print(f"  {t}: pre={v['pre_mean']:.1f} -> post={v['post_mean']:.1f} (p={v.get('mann_whitney_p', 'N/A')})")


# ============================================================
# C14. Citation Dynamics
# ============================================================
print("\n=== C14: Citation Dynamics ===")

# Extract C1 (citations) and year
citations = []
for i, entry in enumerate(matrix):
    c1 = extract_score(entry, "C1")
    year = entry["year"]
    if c1 is not None:
        citations.append({
            "benchmark": entry["short_title"],
            "year": year,
            "citations": float(c1),
            "age": 2026 - year
        })

# Mean citations per year
cit_by_year = {}
for c in citations:
    if c["year"] not in cit_by_year:
        cit_by_year[c["year"]] = []
    cit_by_year[c["year"]].append(c["citations"])

yearly_cit_mean = {str(y): round(float(np.mean(v)), 2) for y, v in sorted(cit_by_year.items())}

# Expected: older papers have more citations
# Residuals from linear regression of citations on age
if len(citations) >= 3:
    ages = np.array([c["age"] for c in citations])
    cits = np.array([c["citations"] for c in citations])
    slope, intercept, r_val, p_val, std_err = stats.linregress(ages, cits)
    predicted = slope * ages + intercept
    residuals = cits - predicted

    # Unusual: residual > 1.5 SD
    res_std = np.std(residuals)
    unusual = []
    for i, c in enumerate(citations):
        if abs(residuals[i]) > 1.5 * res_std:
            unusual.append({
                "benchmark": c["benchmark"],
                "year": c["year"],
                "age": c["age"],
                "citations_score": c["citations"],
                "expected": round(float(predicted[i]), 1),
                "residual": round(float(residuals[i]), 1),
                "direction": "over-cited" if residuals[i] > 0 else "under-cited"
            })
    unusual.sort(key=lambda x: abs(x["residual"]), reverse=True)
else:
    slope, r_val, p_val = None, None, None
    unusual = []

results["C14_citation_dynamics"] = {
    "n_benchmarks_with_citations": len(citations),
    "mean_citations_by_year": yearly_cit_mean,
    "age_citation_regression": {
        "slope": safe_float(slope),
        "r_squared": safe_float(r_val ** 2 if r_val is not None else None),
        "p_value": safe_float(p_val)
    },
    "unusual_citation_rates": unusual,
    "note": "C1 is a normalized citation score (0-100), not raw citation count"
}
print(f"  Age-citation R2: {r_val**2:.3f}" if r_val else "  Insufficient data")
print(f"  Unusual citation rates: {len(unusual)}")
for u in unusual[:5]:
    print(f"    {u['benchmark'][:40]}: {u['direction']} (residual={u['residual']})")


# ============================================================
# Summary
# ============================================================
print("\n=== Generating Summary ===")

summary_lines = []

# A1
summary_lines.append(f"Factor analysis suggests {suggested_factors} factors (parallel analysis), vs 4 a priori tiers. {align_text}")

# A2
summary_lines.append(f"Correlation structure reveals {len(high_corr_pairs)} highly-correlated pairs (r>0.80) and {n_clusters} clusters at r=0.70 threshold.")

# A3
summary_lines.append(f"Feature importance: {len(dead_features)} dead features (variance<1 or >90% null). Tier D has highest mean variance ({results['A3_feature_importance']['tier_mean_variance']['D']}), indicating strongest discriminating power.")

# A5
summary_lines.append(f"{ortho_text} Mean |r| with composite = {mean_abs_r:.3f}.")

# B6
archetype_strs = [a['archetype_label'] + ' (n=' + str(a['size']) + ')' for a in archetype_info]
summary_lines.append(f"Benchmark clustering: optimal k={optimal_k} (silhouette={sil_scores[optimal_k]}). Archetypes: {', '.join(archetype_strs)}.")

# B7
summary_lines.append(f"Theory coverage: Shannon H={shannon_entropy:.2f} (evenness={evenness:.2f}). MFT dominates at {results['B7_theory_coverage']['mft_dominance_pct']}%. Deserts: {deserts}.")

# C11
summary_lines.append(f"Temporal trends: improving features = {improving or 'none'}, declining = {declining or 'none'}, stagnant = {stagnant or 'all tested'}.")

# C13
summary_lines.append(f"Pre/Post-RLHF: {len(sig_tiers)} tier(s) show significant change. {results['C13_pre_post_rlhf']['summary']}")

summary = " | ".join(summary_lines)

# ============================================================
# Output
# ============================================================
output = {
    "date": "2026-04-04",
    "analyses": results,
    "summary": summary,
    "metadata": {
        "n_benchmarks_scored": len(matrix),
        "n_candidates_total": len(candidates),
        "n_sweep_new": 71,
        "n_features_new": len(NEW_FEATS),
        "n_features_all": len(ALL_FEATS),
        "feature_tiers": {
            "D": len(D_FEATS),
            "E": len(E_FEATS),
            "F": len(F_FEATS),
            "G": len(G_FEATS)
        }
    }
}

with open(OUT_PATH, "w") as f:
    json.dump(output, f, indent=2, default=safe_float)

print(f"\n=== DONE ===")
print(f"Results written to: {OUT_PATH}")
print(f"File size: {OUT_PATH.stat().st_size / 1024:.1f} KB")
