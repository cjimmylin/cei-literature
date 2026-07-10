#!/usr/bin/env python3
"""
Statistical Clustering Analysis for Cross-Cultural AI Values Alignment.

Performs:
    1. Hierarchical clustering (Ward's method) on 10 regional profile vectors
    2. k-means validation with silhouette scores (k=2..8)
    3. Dendrogram generation
    4. Cluster assignment and profiling

Output:
    DATA/20260403-clustering-results.json
    PAPER/figures/dendrogram.png
    PAPER/figures/silhouette.png
    PAPER/figures/heatmap-regions-frameworks.png
"""
from __future__ import annotations

import functools
import json
import os
import sys
from datetime import date
from pathlib import Path

import numpy as np

print = functools.partial(print, flush=True)

_SCRIPT_DIR = Path(__file__).parent
_CEI_LIT_WS = _SCRIPT_DIR.parent.parent
sys.path.insert(0, str(_CEI_LIT_WS / "PYTHON"))
sys.path.insert(0, str(_CEI_LIT_WS / ".agent" / "lib"))

TODAY = date.today().strftime("%Y%m%d")
DATA_DIR = _SCRIPT_DIR.parent / "DATA"
FIG_DIR = _SCRIPT_DIR.parent / "PAPER" / "figures"
FIG_DIR.mkdir(parents=True, exist_ok=True)

# Dimensions for clustering
WESTERN = ["virtue_ethics", "deontological_ethics", "utilitarian_ethics",
           "care_ethics", "contractarian_ethics"]
NW = ["nw_confucian", "nw_ubuntu", "nw_islamic_ethics",
      "nw_buddhist", "nw_dharmic", "nw_indigenous_relational", "nw_buen_vivir"]
ALL_FRAMEWORKS = WESTERN + NW

# Okabe-Ito colors
REGION_COLORS = {
    "North America": "#E69F00", "Western Europe": "#56B4E9",
    "East Asia": "#009E73", "MENA": "#F0E442",
    "South Asia": "#0072B2", "Southeast Asia": "#D55E00",
    "Latin America & Caribbean": "#CC79A7",
    "Eastern Europe & Central Asia": "#999999",
    "Oceania": "#332288", "Sub-Saharan Africa": "#882255",
}

REGIONS_ORDERED = [
    "North America", "Western Europe", "East Asia", "MENA",
    "South Asia", "Southeast Asia", "Latin America & Caribbean",
    "Eastern Europe & Central Asia", "Oceania", "Sub-Saharan Africa",
]


def main():
    from scipy.cluster.hierarchy import linkage, dendrogram, fcluster
    from scipy.spatial.distance import pdist
    from sklearn.cluster import KMeans
    from sklearn.metrics import silhouette_score
    from sklearn.preprocessing import StandardScaler
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import matplotlib.colors as mcolors

    # Load analysis data
    analysis_path = DATA_DIR / f"{TODAY}-cross-cultural-analysis.json"
    if not analysis_path.exists():
        # Try without today's date
        candidates = sorted(DATA_DIR.glob("*-cross-cultural-analysis.json"), reverse=True)
        if candidates:
            analysis_path = candidates[0]
        else:
            print("ERROR: No cross-cultural analysis JSON found")
            return 1

    with open(analysis_path) as f:
        analysis = json.load(f)

    regional_profiles = analysis["regional_profiles"]

    # Build feature matrix (regions × frameworks)
    regions = [r for r in REGIONS_ORDERED if r in regional_profiles]
    n_regions = len(regions)
    n_dims = len(ALL_FRAMEWORKS)

    print(f"Clustering {n_regions} regions × {n_dims} framework dimensions")

    # Build matrix
    X = np.zeros((n_regions, n_dims))
    region_sizes = []
    for i, region in enumerate(regions):
        profile = regional_profiles[region]
        region_sizes.append(profile["n"])
        for j, fw in enumerate(ALL_FRAMEWORKS):
            X[i, j] = profile["mean_scores"].get(fw, 0)

    print(f"Feature matrix shape: {X.shape}")
    print(f"Region sizes: {dict(zip(regions, region_sizes))}")

    # Standardize for clustering
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # ── Hierarchical Clustering ──────────────────────────────────────
    print("\nHierarchical clustering (Ward's method)...")
    Z = linkage(X_scaled, method="ward")

    # Dendrogram
    fig, ax = plt.subplots(figsize=(12, 7))
    fig.patch.set_facecolor("#0d1117")
    ax.set_facecolor("#0d1117")

    dendro = dendrogram(
        Z,
        labels=regions,
        leaf_rotation=35,
        leaf_font_size=10,
        color_threshold=Z[-2, 2],  # Color by 3-cluster cut
        above_threshold_color="#888888",
    )

    ax.set_title("Regional Clustering of AI Values Alignment Approaches",
                 fontsize=14, fontweight="bold", color="white", pad=15)
    ax.set_ylabel("Ward Distance", fontsize=11, color="white")
    ax.tick_params(colors="white")
    ax.spines["bottom"].set_color("white")
    ax.spines["left"].set_color("white")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.tight_layout()
    dendro_path = FIG_DIR / "dendrogram.png"
    fig.savefig(dendro_path, dpi=150, facecolor="#0d1117", bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved dendrogram to {dendro_path}")

    # Cluster assignments at k=3
    clusters_3 = fcluster(Z, t=3, criterion="maxclust")
    cluster_assignments_3 = {regions[i]: int(clusters_3[i]) for i in range(n_regions)}
    print(f"  3-cluster assignments: {cluster_assignments_3}")

    # ── k-means Validation with Silhouette ───────────────────────────
    print("\nk-means validation (k=2..8)...")
    silhouette_results = {}
    for k in range(2, min(9, n_regions)):
        km = KMeans(n_clusters=k, random_state=42, n_init=10)
        labels = km.fit_predict(X_scaled)
        sil = silhouette_score(X_scaled, labels)
        silhouette_results[k] = round(float(sil), 4)
        print(f"  k={k}: silhouette={sil:.4f}")

    best_k = max(silhouette_results, key=silhouette_results.get)
    print(f"  Best k={best_k} (silhouette={silhouette_results[best_k]:.4f})")

    # Silhouette plot
    fig, ax = plt.subplots(figsize=(8, 5))
    fig.patch.set_facecolor("#0d1117")
    ax.set_facecolor("#0d1117")

    ks = sorted(silhouette_results.keys())
    sils = [silhouette_results[k] for k in ks]
    ax.plot(ks, sils, "o-", color="#56B4E9", linewidth=2, markersize=8)
    ax.axvline(x=best_k, color="#E69F00", linestyle="--", alpha=0.7, label=f"Best k={best_k}")

    ax.set_xlabel("Number of Clusters (k)", fontsize=11, color="white")
    ax.set_ylabel("Silhouette Score", fontsize=11, color="white")
    ax.set_title("Silhouette Analysis for Optimal Cluster Count",
                 fontsize=13, fontweight="bold", color="white")
    ax.tick_params(colors="white")
    ax.spines["bottom"].set_color("white")
    ax.spines["left"].set_color("white")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.legend(facecolor="#161b22", edgecolor="#30363d", labelcolor="white")

    plt.tight_layout()
    sil_path = FIG_DIR / "silhouette.png"
    fig.savefig(sil_path, dpi=150, facecolor="#0d1117", bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved silhouette plot to {sil_path}")

    # ── Heatmap: Regions × Frameworks ────────────────────────────────
    print("\nGenerating heatmap...")
    fig, ax = plt.subplots(figsize=(14, 8))
    fig.patch.set_facecolor("#0d1117")
    ax.set_facecolor("#0d1117")

    # Framework labels (cleaned)
    fw_labels = [fw.replace("_ethics", "").replace("nw_", "NW:").replace("_", " ").title()
                 for fw in ALL_FRAMEWORKS]

    im = ax.imshow(X, cmap="YlOrRd", aspect="auto")
    ax.set_xticks(range(n_dims))
    ax.set_xticklabels(fw_labels, rotation=45, ha="right", fontsize=9, color="white")
    ax.set_yticks(range(n_regions))
    ax.set_yticklabels([f"{r} (n={region_sizes[i]})" for i, r in enumerate(regions)],
                       fontsize=9, color="white")

    # Add text annotations
    for i in range(n_regions):
        for j in range(n_dims):
            val = X[i, j]
            if val >= 1.0:
                color = "white" if val > 10 else "black"
                ax.text(j, i, f"{val:.1f}", ha="center", va="center",
                       fontsize=7, color=color, fontweight="bold")

    cbar = fig.colorbar(im, ax=ax, shrink=0.8)
    cbar.ax.yaxis.set_tick_params(color="white")
    cbar.ax.yaxis.label.set_color("white")
    plt.setp(plt.getp(cbar.ax.axes, "yticklabels"), color="white")
    cbar.set_label("Mean Score", color="white", fontsize=10)

    ax.set_title("Regional Normative Framework Profiles\n(Mean Scores, 0-100 Scale)",
                 fontsize=13, fontweight="bold", color="white", pad=15)

    plt.tight_layout()
    heatmap_path = FIG_DIR / "heatmap-regions-frameworks.png"
    fig.savefig(heatmap_path, dpi=150, facecolor="#0d1117", bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved heatmap to {heatmap_path}")

    # ── Save results ─────────────────────────────────────────────────
    results = {
        "date": TODAY,
        "n_regions": n_regions,
        "n_dimensions": n_dims,
        "regions": regions,
        "frameworks": ALL_FRAMEWORKS,
        "feature_matrix": X.tolist(),
        "region_sizes": dict(zip(regions, region_sizes)),
        "hierarchical_clustering": {
            "method": "ward",
            "linkage_matrix": Z.tolist(),
            "cluster_assignments_k3": cluster_assignments_3,
        },
        "silhouette_analysis": {
            "scores": silhouette_results,
            "best_k": best_k,
            "best_silhouette": silhouette_results[best_k],
        },
        "cluster_profiles_k3": {},
    }

    # Profile each cluster
    for c in sorted(set(clusters_3)):
        c = int(c)
        member_regions = [regions[i] for i in range(n_regions) if clusters_3[i] == c]
        member_sizes = [region_sizes[i] for i in range(n_regions) if clusters_3[i] == c]
        mean_profile = X[[i for i in range(n_regions) if clusters_3[i] == c]].mean(axis=0)
        results["cluster_profiles_k3"][f"cluster_{c}"] = {
            "regions": member_regions,
            "total_papers": sum(member_sizes),
            "mean_profile": {ALL_FRAMEWORKS[j]: round(float(mean_profile[j]), 2)
                           for j in range(n_dims)},
        }

    out_path = DATA_DIR / f"{TODAY}-clustering-results.json"
    tmp = out_path.with_suffix(f".tmp.{os.getpid()}.json")
    tmp.write_text(json.dumps(results, indent=2))
    os.replace(str(tmp), str(out_path))
    print(f"\nSaved clustering results to {out_path}")

    # Print cluster summary
    print(f"\n{'='*60}")
    print("CLUSTER SUMMARY (k=3)")
    print(f"{'='*60}")
    for c_name, c_data in results["cluster_profiles_k3"].items():
        top_fw = max(c_data["mean_profile"], key=c_data["mean_profile"].get)
        print(f"\n{c_name}: {c_data['regions']}")
        print(f"  Total papers: {c_data['total_papers']}")
        print(f"  Dominant framework: {top_fw} ({c_data['mean_profile'][top_fw]:.1f})")

    return 0


if __name__ == "__main__":
    sys.exit(main())
