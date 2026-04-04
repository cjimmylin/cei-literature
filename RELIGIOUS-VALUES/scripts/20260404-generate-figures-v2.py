"""Generate figures 5-9 and S3 for the Religious Values Benchmark paper.

Reads from RELIGIOUS-VALUES/data/ and writes PNGs to RELIGIOUS-VALUES/PAPER/figures/.
"""
from __future__ import annotations

import json
import math
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import seaborn as sns

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
BASE = Path(__file__).resolve().parent.parent          # RELIGIOUS-VALUES/
DATA = BASE / "data"
FIG_DIR = BASE / "PAPER" / "figures"
FIG_DIR.mkdir(parents=True, exist_ok=True)

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
TRADITION_FAMILY_COLORS = {
    "Abrahamic":  "#4C78A8",   # blue
    "Dharmic":    "#54A24B",   # green
    "East Asian": "#E45756",   # orange-red
    "Other":      "#9D9D9D",   # gray
    "African/Indigenous": "#9D9D9D",
}

def family_color(family: str) -> str:
    return TRADITION_FAMILY_COLORS.get(family, "#9D9D9D")

# ---------------------------------------------------------------------------
# Load data
# ---------------------------------------------------------------------------
sensitivity   = json.loads((DATA / "20260404-sensitivity-analysis.json").read_text())
correlation   = json.loads((DATA / "20260404-correlation-matrix.json").read_text())
claims        = json.loads((DATA / "20260404-claim-robustness-tests.json").read_text())
void_factors  = json.loads((DATA / "20260404-void-factor-taxonomy.json").read_text())
batch1        = json.loads((DATA / "20260404-claude-assessment-batch1.json").read_text())
batch2        = json.loads((DATA / "20260404-claude-assessment-batch2.json").read_text())
feature_mat   = json.loads((DATA / "20260404-religious-benchmark-feature-matrix-v2.json").read_text())

# Gate-passers with tradition family info
gp_entries = [e for e in feature_mat["entries"] if e.get("passes_gates")]

# ===================================================================
# Fig 5: Bootstrap CI Forest Plot
# ===================================================================
def fig5():
    cis = sensitivity["bootstrap"]["benchmark_cis"]
    # Sort descending by composite_mean
    cis_sorted = sorted(cis, key=lambda x: x["composite_mean"], reverse=True)

    # Build a lookup from id -> tradition family
    id_to_family = {}
    for e in gp_entries:
        id_to_family[e["id"]] = e.get("D6_tradition_family", "Other")

    n = len(cis_sorted)
    fig, ax = plt.subplots(figsize=(10, max(12, n * 0.32)))

    y_pos = np.arange(n)
    means = [c["composite_mean"] for c in cis_sorted]
    lowers = [c["composite_ci_lower"] for c in cis_sorted]
    uppers = [c["composite_ci_upper"] for c in cis_sorted]
    labels = [c["short_title"][:55] for c in cis_sorted]
    colors = [family_color(id_to_family.get(c["id"], "Other")) for c in cis_sorted]

    xerr_low = [m - lo for m, lo in zip(means, lowers)]
    xerr_high = [hi - m for m, hi in zip(means, uppers)]

    ax.barh(y_pos, means, xerr=[xerr_low, xerr_high], height=0.6,
            color=colors, edgecolor="white", linewidth=0.3,
            error_kw=dict(ecolor="#555555", capsize=2, linewidth=0.8))

    ax.set_yticks(y_pos)
    ax.set_yticklabels(labels, fontsize=7)
    ax.invert_yaxis()
    ax.set_xlabel("Composite Score", fontsize=11)
    ax.set_title("Bootstrap 95% CI for Composite Scores (n=10,000)", fontsize=13, weight="bold")

    # Top-15 cutoff: score of 15th item
    if n >= 15:
        cutoff = means[14]
        ax.axvline(cutoff, color="#E45756", linestyle="--", linewidth=1.2, label=f"Top-15 cutoff ({cutoff:.1f})")
        ax.legend(loc="lower right", fontsize=9)

    # Legend for families
    patches = [mpatches.Patch(color=c, label=f) for f, c in TRADITION_FAMILY_COLORS.items()
               if f != "African/Indigenous"]
    leg2 = ax.legend(handles=patches, loc="lower left", fontsize=8, title="Tradition Family")
    ax.add_artist(leg2)
    if n >= 15:
        ax.legend(loc="lower right", fontsize=9)  # re-add cutoff legend

    ax.grid(axis="x", alpha=0.3)
    fig.tight_layout()
    out = FIG_DIR / "fig5-bootstrap-ci-forest.png"
    fig.savefig(out, dpi=200, bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved {out}")


# ===================================================================
# Fig 6: Void Factor Radar
# ===================================================================
def fig6():
    traditions_data = {t["tradition"]: t for t in void_factors["traditions"]}
    exemplars = ["Islam", "Judaism", "Indigenous Spirituality"]
    factors = ["digital_corpus", "nlp_community", "formalizability",
               "data_sovereignty", "institutional_support", "publication_infrastructure"]
    factor_labels = ["Digital\nCorpus", "NLP\nCommunity", "Formal-\nizability",
                     "Data\nSovereignty", "Institutional\nSupport", "Publication\nInfra."]

    n_factors = len(factors)
    angles = np.linspace(0, 2 * np.pi, n_factors, endpoint=False).tolist()
    angles += angles[:1]  # close polygon

    colors_radar = ["#4C78A8", "#E45756", "#54A24B"]
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

    for i, trad in enumerate(exemplars):
        d = traditions_data.get(trad)
        if d is None:
            continue
        values = [d[f] for f in factors]
        values += values[:1]
        ax.plot(angles, values, "o-", linewidth=2, label=trad, color=colors_radar[i])
        ax.fill(angles, values, alpha=0.15, color=colors_radar[i])

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(factor_labels, fontsize=10)
    ax.set_ylim(0, 5.5)
    ax.set_yticks([1, 2, 3, 4, 5])
    ax.set_yticklabels(["1", "2", "3", "4", "5"], fontsize=8)
    ax.set_title("Void Factor Profiles: Three Tradition Archetypes", fontsize=13,
                 weight="bold", pad=20)
    ax.legend(loc="upper right", bbox_to_anchor=(1.25, 1.1), fontsize=10)

    fig.tight_layout()
    out = FIG_DIR / "fig6-void-factor-radar.png"
    fig.savefig(out, dpi=200, bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved {out}")


# ===================================================================
# Fig 7: Values Relevance Distribution
# ===================================================================
def fig7():
    a3_scores = []
    for a in batch1["assessments"]:
        v = a.get("features", {}).get("A3_values_relevance")
        if v is not None:
            a3_scores.append(v)
    for a in batch2["assessments"]:
        v = a.get("features", {}).get("A3_values_alignment_relevance")
        if v is not None:
            a3_scores.append(v)

    if not a3_scores:
        print("  WARNING: No A3 scores found, skipping fig7")
        return

    mean_a3 = np.mean(a3_scores)

    fig, ax = plt.subplots(figsize=(9, 5))
    bins = np.arange(0, 105, 10)
    ax.hist(a3_scores, bins=bins, color="#4C78A8", edgecolor="white", linewidth=0.8, alpha=0.85)
    ax.axvline(50, color="#E45756", linestyle="--", linewidth=1.5, label="Minimal relevance (50)")
    ax.axvline(75, color="#54A24B", linestyle="--", linewidth=1.5, label="Strong relevance (75)")
    ax.axvline(mean_a3, color="#F58518", linestyle="-", linewidth=2, label=f"Mean = {mean_a3:.1f}")

    ax.set_xlabel("A3 Values Alignment Relevance Score", fontsize=11)
    ax.set_ylabel("Count", fontsize=11)
    ax.set_title("Values Alignment Relevance (A3) Distribution Across Gate-Passing Benchmarks",
                 fontsize=12, weight="bold")
    ax.legend(fontsize=9)
    ax.grid(axis="y", alpha=0.3)

    fig.tight_layout()
    out = FIG_DIR / "fig7-values-relevance-histogram.png"
    fig.savefig(out, dpi=200, bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved {out}")


# ===================================================================
# Fig 8: Claim Robustness Summary
# ===================================================================
def fig8():
    claim_data = claims["claims"]

    # Extract one p-value per claim (primary test)
    labels = []
    pvals = []
    for c in claim_data:
        num = c["claim_number"]
        text = c["claim_text"][:60]
        labels.append(f"C{num}: {text}")

        # Get p-value: from 'tests' list (first entry) or top-level 'p_value'
        if "tests" in c and isinstance(c["tests"], list):
            pv = c["tests"][0].get("p_value", 1.0)
        elif "p_value" in c:
            pv = c["p_value"]
        else:
            pv = 1.0
        # Handle p=0.0 (extremely significant) -- set to a small floor for log display
        if pv == 0.0:
            pv = 1e-15
        pvals.append(pv)

    n = len(labels)
    fig, ax = plt.subplots(figsize=(10, 5))

    y_pos = np.arange(n)
    bar_colors = []
    for pv in pvals:
        if pv < 0.05:
            bar_colors.append("#54A24B")   # green = supported
        elif pv < 0.10:
            bar_colors.append("#F58518")   # yellow/orange = marginal
        else:
            bar_colors.append("#E45756")   # red = not supported

    # Plot -log10(p) for visual clarity
    neg_log_p = [-math.log10(pv) for pv in pvals]
    bars = ax.barh(y_pos, neg_log_p, color=bar_colors, edgecolor="white", height=0.6)

    # Significance threshold line at p=0.05 -> -log10(0.05) = 1.301
    ax.axvline(-math.log10(0.05), color="#333333", linestyle="--", linewidth=1.2,
               label="p = 0.05")

    ax.set_yticks(y_pos)
    ax.set_yticklabels(labels, fontsize=8)
    ax.invert_yaxis()
    ax.set_xlabel("-log10(p-value)", fontsize=11)
    ax.set_title("Statistical Support for Paper Claims", fontsize=13, weight="bold")

    # Add p-value text annotations
    for i, (pv, nlp) in enumerate(zip(pvals, neg_log_p)):
        if pv < 0.001:
            txt = "p < 0.001"
        else:
            txt = f"p = {pv:.3f}"
        ax.text(nlp + 0.15, i, txt, va="center", fontsize=8, color="#333333")

    # Color legend
    green_patch = mpatches.Patch(color="#54A24B", label="p < 0.05 (supported)")
    yellow_patch = mpatches.Patch(color="#F58518", label="0.05 < p < 0.10 (marginal)")
    red_patch = mpatches.Patch(color="#E45756", label="p > 0.10 (not supported)")
    ax.legend(handles=[green_patch, yellow_patch, red_patch], loc="lower right", fontsize=8)

    ax.grid(axis="x", alpha=0.3)
    fig.tight_layout()
    out = FIG_DIR / "fig8-claim-robustness.png"
    fig.savefig(out, dpi=200, bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved {out}")


# ===================================================================
# Fig 9: Gate Threshold vs Tradition Coverage
# ===================================================================
def fig9():
    gt = sensitivity["gate_threshold"]
    results = gt["results"]

    thresholds = [r["threshold"] for r in results]
    n_passers = [r["gate_passers"] for r in results]
    n_traditions = [r["traditions_represented"] for r in results]

    fig, ax1 = plt.subplots(figsize=(10, 5.5))
    color1 = "#4C78A8"
    color2 = "#E45756"

    ax1.plot(thresholds, n_passers, "o-", color=color1, linewidth=2, markersize=7,
             label="Gate-passers")
    ax1.set_xlabel("RD Gate Threshold", fontsize=11)
    ax1.set_ylabel("Number of Gate-Passers", fontsize=11, color=color1)
    ax1.tick_params(axis="y", labelcolor=color1)

    ax2 = ax1.twinx()
    ax2.plot(thresholds, n_traditions, "s--", color=color2, linewidth=2, markersize=7,
             label="Traditions Represented")
    ax2.set_ylabel("Traditions Represented", fontsize=11, color=color2)
    ax2.tick_params(axis="y", labelcolor=color2)

    # Highlight current threshold (30) and NormEval threshold (40)
    ax1.axvline(30, color="#54A24B", linestyle=":", linewidth=2, alpha=0.8)
    ax1.text(30.5, max(n_passers) * 0.92, "Current (30)", fontsize=9, color="#54A24B",
             weight="bold")
    ax1.axvline(40, color="#F58518", linestyle=":", linewidth=2, alpha=0.8)
    ax1.text(40.5, max(n_passers) * 0.85, "NormEval (40)", fontsize=9, color="#F58518",
             weight="bold")

    # Annotate void traditions gained at low thresholds
    for r in results:
        gained = r.get("void_traditions_gained", [])
        if gained and r["threshold"] <= 25:
            txt = ", ".join(gained[:3])
            if len(gained) > 3:
                txt += f" +{len(gained)-3}"
            # Position annotation above the gate-passers line
            idx = thresholds.index(r["threshold"])
            ax1.annotate(txt, xy=(r["threshold"], n_passers[idx]),
                         xytext=(r["threshold"] - 1, n_passers[idx] + max(n_passers) * 0.06),
                         fontsize=7, color="#666666",
                         arrowprops=dict(arrowstyle="->", color="#999999", lw=0.8))

    ax1.set_title("Gate Threshold vs Tradition Coverage", fontsize=13, weight="bold")
    # Combined legend
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper right", fontsize=9)

    ax1.grid(axis="both", alpha=0.3)
    fig.tight_layout()
    out = FIG_DIR / "fig9-gate-threshold-sensitivity.png"
    fig.savefig(out, dpi=200, bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved {out}")


# ===================================================================
# Fig S3: Spearman Correlation Heatmap
# ===================================================================
def fig_s3():
    corr_data = correlation["spearman_correlations"]
    features = corr_data["features"]
    matrix = np.array(corr_data["matrix"])

    fig, ax = plt.subplots(figsize=(9, 7.5))
    sns.heatmap(matrix, annot=True, fmt=".2f", cmap="RdBu_r", center=0,
                xticklabels=features, yticklabels=features,
                vmin=-1, vmax=1, linewidths=0.5, linecolor="white",
                square=True, ax=ax,
                annot_kws={"fontsize": 8})
    ax.set_title("Spearman Rank Correlation Matrix (Gate-Passers, n=47)",
                 fontsize=13, weight="bold")
    ax.tick_params(axis="both", labelsize=9)
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right")

    fig.tight_layout()
    out = FIG_DIR / "fig-s3-correlation-heatmap.png"
    fig.savefig(out, dpi=200, bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved {out}")


# ===================================================================
# Main
# ===================================================================
if __name__ == "__main__":
    print("Generating Religious Values Benchmark figures...")
    fig5()
    fig6()
    fig7()
    fig8()
    fig9()
    fig_s3()
    print("Done. All figures saved to", FIG_DIR)
