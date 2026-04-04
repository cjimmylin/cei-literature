"""
20260404-statistical-analysis.py
Task 1: Inter-Feature Correlations + Hierarchical Clustering
for the Religious Values Benchmark Survey (Wave 4).

Reads the v2 feature matrix, computes Spearman correlations on all 401 entries,
and runs hierarchical clustering on 47 gate-passers.

Output: RELIGIOUS-VALUES/data/20260404-correlation-matrix.json
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
from scipy import stats
from scipy.cluster.hierarchy import linkage, fcluster
from scipy.spatial.distance import pdist
from sklearn.metrics import adjusted_rand_score
from sklearn.preprocessing import StandardScaler

# ── paths ────────────────────────────────────────────────────────────────────
BASE = Path(__file__).resolve().parent.parent
DATA_DIR = BASE / "data"
INPUT_FILE = DATA_DIR / "20260404-religious-benchmark-feature-matrix-v2.json"
OUTPUT_FILE = DATA_DIR / "20260404-correlation-matrix.json"

NUMERIC_FEATURES = [
    "R2_depth", "R3_scriptural", "R4_denominational", "R5_pluralism",
    "R6_grounding", "P7_implementability", "PE_score", "RD_score",
    "CI_score", "COMPOSITE",
]

CLUSTER_FEATURES = [
    "R2_depth", "R3_scriptural", "R4_denominational", "R5_pluralism",
    "R6_grounding", "PE_score", "CI_score",
]


def load_data() -> tuple[list[dict], list[dict]]:
    """Return (all_entries, gate_passers)."""
    with open(INPUT_FILE) as f:
        data = json.load(f)
    entries = data["entries"]
    gate_passers = [e for e in entries if e.get("passes_gates")]
    return entries, gate_passers


# ── 1A  Spearman correlations ────────────────────────────────────────────────

def compute_spearman(entries: list[dict]) -> dict:
    """Pairwise Spearman rank correlations for NUMERIC_FEATURES."""
    n_feat = len(NUMERIC_FEATURES)
    matrix = np.zeros((len(entries), n_feat))
    for i, e in enumerate(entries):
        for j, feat in enumerate(NUMERIC_FEATURES):
            val = e.get(feat)
            matrix[i, j] = float(val) if val is not None else 0.0

    corr_matrix = np.ones((n_feat, n_feat))
    p_matrix = np.zeros((n_feat, n_feat))

    for a in range(n_feat):
        for b in range(a + 1, n_feat):
            r, p = stats.spearmanr(matrix[:, a], matrix[:, b])
            corr_matrix[a, b] = r
            corr_matrix[b, a] = r
            p_matrix[a, b] = p
            p_matrix[b, a] = p

    high_pairs = []
    low_pairs = []
    for a in range(n_feat):
        for b in range(a + 1, n_feat):
            r = corr_matrix[a, b]
            p = p_matrix[a, b]
            rec = {
                "f1": NUMERIC_FEATURES[a],
                "f2": NUMERIC_FEATURES[b],
                "r": round(float(r), 4),
                "p": float(f"{p:.6g}"),
            }
            if abs(r) > 0.7:
                high_pairs.append(rec)
            if abs(r) < 0.1:
                low_pairs.append(rec)

    # Sort by |r| descending for high, ascending for low
    high_pairs.sort(key=lambda x: -abs(x["r"]))
    low_pairs.sort(key=lambda x: abs(x["r"]))

    return {
        "features": NUMERIC_FEATURES,
        "matrix": [[round(float(corr_matrix[i, j]), 4)
                     for j in range(n_feat)] for i in range(n_feat)],
        "high_correlation_pairs": high_pairs,
        "low_correlation_pairs": low_pairs,
    }


# ── 1B  Hierarchical clustering ─────────────────────────────────────────────

def run_clustering(gate_passers: list[dict]) -> dict:
    """Ward-linkage clustering on z-scored features; ARI against tradition & format."""
    n = len(gate_passers)
    n_feat = len(CLUSTER_FEATURES)

    raw = np.zeros((n, n_feat))
    for i, e in enumerate(gate_passers):
        for j, feat in enumerate(CLUSTER_FEATURES):
            val = e.get(feat)
            raw[i, j] = float(val) if val is not None else 0.0

    # z-score normalize
    scaler = StandardScaler()
    Z = scaler.fit_transform(raw)

    # Ward linkage
    dist = pdist(Z, metric="euclidean")
    link = linkage(dist, method="ward")

    # Ground-truth labels
    tradition_labels = [e.get("D6_tradition_family", "Unknown") for e in gate_passers]
    format_labels = [e.get("P1_format", "Unknown") for e in gate_passers]

    k_values = [3, 4, 5, 6]
    results = []
    for k in k_values:
        clusters = fcluster(link, t=k, criterion="maxclust")
        ari_trad = adjusted_rand_score(tradition_labels, clusters)
        ari_fmt = adjusted_rand_score(format_labels, clusters)
        results.append({
            "k": k,
            "ari_vs_tradition": round(float(ari_trad), 4),
            "ari_vs_format": round(float(ari_fmt), 4),
            "cluster_sizes": [int((clusters == c).sum()) for c in range(1, k + 1)],
        })

    # Best k by max ARI vs tradition
    best_trad = max(results, key=lambda r: r["ari_vs_tradition"])
    best_fmt = max(results, key=lambda r: r["ari_vs_format"])

    # Determine interpretation
    trad_wins = best_trad["ari_vs_tradition"] > best_fmt["ari_vs_format"]
    if trad_wins:
        interp = (
            f"Benchmarks cluster more by tradition family (best ARI={best_trad['ari_vs_tradition']:.3f} "
            f"at k={best_trad['k']}) than by format (best ARI={best_fmt['ari_vs_format']:.3f} "
            f"at k={best_fmt['k']}). Religious tradition is the stronger organizing dimension."
        )
    else:
        interp = (
            f"Benchmarks cluster more by format (best ARI={best_fmt['ari_vs_format']:.3f} "
            f"at k={best_fmt['k']}) than by tradition (best ARI={best_trad['ari_vs_tradition']:.3f} "
            f"at k={best_trad['k']}). Methodological format is the stronger organizing dimension."
        )

    return {
        "features_used": CLUSTER_FEATURES,
        "n_gate_passers": n,
        "k_values_tested": k_values,
        "results": results,
        "interpretation": interp,
    }


# ── main ─────────────────────────────────────────────────────────────────────

def main() -> None:
    entries, gate_passers = load_data()
    print(f"Loaded {len(entries)} entries, {len(gate_passers)} gate-passers")

    print("Computing Spearman correlations...")
    spearman = compute_spearman(entries)
    print(f"  High |r|>0.7 pairs: {len(spearman['high_correlation_pairs'])}")
    print(f"  Low  |r|<0.1 pairs: {len(spearman['low_correlation_pairs'])}")

    print("Running hierarchical clustering...")
    clustering = run_clustering(gate_passers)
    for r in clustering["results"]:
        print(f"  k={r['k']}: ARI(tradition)={r['ari_vs_tradition']:.3f}, "
              f"ARI(format)={r['ari_vs_format']:.3f}, sizes={r['cluster_sizes']}")
    print(f"  => {clustering['interpretation']}")

    output = {
        "generated": "20260404",
        "spearman_correlations": spearman,
        "clustering": clustering,
    }

    with open(OUTPUT_FILE, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nOutput written to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
