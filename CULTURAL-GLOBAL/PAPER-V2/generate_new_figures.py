#!/usr/bin/env python3
"""Generate Figures 5-10 for PAPER-V2 main text."""
from __future__ import annotations
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.patheffects as pe
import numpy as np
import os

BASE = os.path.dirname(os.path.abspath(__file__))
FIG_DIR = os.path.join(BASE, "figures")

# ── Shared style ──────────────────────────────────────────────
plt.rcParams.update({
    "figure.facecolor": "white",
    "axes.facecolor": "#fafafa",
    "font.family": "sans-serif",
    "font.size": 10,
    "axes.titlesize": 12,
    "axes.labelsize": 11,
    "xtick.labelsize": 9,
    "ytick.labelsize": 9,
    "legend.fontsize": 9,
    "figure.dpi": 200,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.15,
})

# Okabe-Ito palette (colorblind-safe)
OI = {
    "orange": "#E69F00", "sky": "#56B4E9", "green": "#009E73",
    "yellow": "#F0E442", "blue": "#0072B2", "vermillion": "#D55E00",
    "purple": "#CC79A7", "black": "#000000", "grey": "#999999",
}


# ══════════════════════════════════════════════════════════════
# FIG 5 — Benchmark Landscape: 2-Cluster Structure
# ══════════════════════════════════════════════════════════════
def fig5_benchmark_clusters():
    fig, axes = plt.subplots(1, 2, figsize=(12, 5.5), gridspec_kw={"width_ratios": [1, 1.4]})

    # Left: Cluster composition donut
    ax = axes[0]
    sizes = [47, 168]
    labels = ["Non-Western\nFocused\n(n=47, 21.9%)", "LLM-Ready\n(n=168, 78.1%)"]
    colors = [OI["vermillion"], OI["sky"]]
    wedges, texts = ax.pie(sizes, labels=labels, colors=colors,
                           startangle=90, pctdistance=0.75,
                           wedgeprops=dict(width=0.45, edgecolor="white", linewidth=2))
    for t in texts:
        t.set_fontsize(10)
        t.set_fontweight("bold")
    ax.set_title("A. Benchmark Landscape Clusters", fontweight="bold", pad=15)

    # Right: Feature comparison bars
    ax = axes[1]
    features = ["NW Framework\nCount", "LLM\nAdministrability", "Data\nAvailability",
                "Indigenous\nContent", "Non-English\nPrimary", "Format\nComplexity"]
    c1_vals = [0.915, 0.40, 1.9, 0.277, 0.574, 1.2]  # Non-Western Focused
    c2_vals = [0.012, 0.952, 2.1, 0.000, 0.351, 1.7]  # LLM-Ready

    x = np.arange(len(features))
    w = 0.35
    bars1 = ax.bar(x - w/2, c1_vals, w, label="Non-Western Focused (n=47)",
                   color=OI["vermillion"], edgecolor="white", linewidth=0.5)
    bars2 = ax.bar(x + w/2, c2_vals, w, label="LLM-Ready (n=168)",
                   color=OI["sky"], edgecolor="white", linewidth=0.5)
    ax.set_xticks(x)
    ax.set_xticklabels(features, ha="center")
    ax.set_ylabel("Mean Score")
    ax.set_title("B. Cluster Feature Profiles", fontweight="bold")
    ax.legend(loc="upper right", framealpha=0.9)
    ax.set_ylim(0, 2.5)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    # Annotate the bifurcation
    ax.annotate("~15 benchmarks\nat intersection",
                xy=(0, 0.5), xytext=(2.5, 2.2),
                fontsize=9, fontstyle="italic", color=OI["grey"],
                arrowprops=dict(arrowstyle="->", color=OI["grey"], lw=1.2))

    plt.tight_layout()
    out = os.path.join(FIG_DIR, "benchmark-landscape-clusters.png")
    fig.savefig(out)
    plt.close()
    print(f"  Fig 5: {out}")


# ══════════════════════════════════════════════════════════════
# FIG 6 — Tradition Coverage: Concept Operationalization Gaps
# ══════════════════════════════════════════════════════════════
def fig6_concept_coverage():
    traditions = ["Confucian", "Ubuntu", "Islamic", "Dharmic", "Buddhist", "Indigenous", "Buen Vivir"]
    total_concepts = [9, 5, 7, 6, 6, 6, 5]
    measured = [2, 1, 0, 0, 0, 0, 0]
    unmeasured = [t - m for t, m in zip(total_concepts, measured)]

    fig, ax = plt.subplots(figsize=(10, 5))
    y = np.arange(len(traditions))
    h = 0.6

    bars_m = ax.barh(y, measured, h, label="Measured concepts", color=OI["green"], edgecolor="white")
    bars_u = ax.barh(y, unmeasured, h, left=measured, label="Unmeasured concepts",
                     color=OI["vermillion"], alpha=0.7, edgecolor="white")

    ax.set_yticks(y)
    ax.set_yticklabels(traditions, fontsize=11)
    ax.set_xlabel("Number of Moral Concepts", fontsize=11)
    ax.set_title("Non-Western Moral Concept Operationalization in 218 Benchmarks",
                 fontweight="bold", fontsize=12)
    ax.legend(loc="lower right", framealpha=0.9, fontsize=10)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    # Annotate measured concepts
    concept_labels = {
        0: "ren, li",
        1: "ubuntu",
    }
    for i, (m, t) in enumerate(zip(measured, total_concepts)):
        if m > 0:
            ax.text(m / 2, i, concept_labels.get(i, ""), ha="center", va="center",
                    fontsize=8, fontweight="bold", color="white")
        # Total label
        ax.text(t + 0.15, i, f"{m}/{t}", ha="left", va="center", fontsize=9, color=OI["black"])

    # Overall stat
    ax.text(0.98, 0.02, "3 of 44 concepts measured (6.8%)\n5 traditions at 0% coverage",
            transform=ax.transAxes, ha="right", va="bottom",
            fontsize=10, fontstyle="italic", color=OI["vermillion"],
            bbox=dict(boxstyle="round,pad=0.4", facecolor="#fff3f0", edgecolor=OI["vermillion"], alpha=0.8))

    ax.set_xlim(0, 11)
    plt.tight_layout()
    out = os.path.join(FIG_DIR, "concept-coverage-gaps.png")
    fig.savefig(out)
    plt.close()
    print(f"  Fig 6: {out}")


# ══════════════════════════════════════════════════════════════
# FIG 7 — Claude's Cultural Map Position (Inglehart-Welzel)
# ══════════════════════════════════════════════════════════════
def fig7_cultural_map():
    # Approximate Inglehart-Welzel positions (Survival-SelfExpr x Trad-SecRat)
    # x = Survival(-2) to Self-expression(+2), y = Traditional(-2) to Secular-rational(+2)
    countries = {
        "Germany":       (1.4, 1.6),
        "United States": (1.6, 0.3),
        "Japan":         (0.5, 1.5),
        "Brazil":        (0.4, -0.8),
        "China":         (-0.2, 1.2),
        "India":         (-0.8, -0.6),
        "Nigeria":       (-0.6, -1.5),
        "Saudi Arabia":  (-0.4, -1.8),
    }
    # Claude's estimated position (extreme secular-rational / self-expression)
    claude_pos = (1.8, 1.9)

    fig, ax = plt.subplots(figsize=(9, 8))

    # Quadrant shading
    ax.axhline(0, color="#cccccc", linewidth=0.8, zorder=1)
    ax.axvline(0, color="#cccccc", linewidth=0.8, zorder=1)
    ax.fill_between([-2.5, 0], -2.5, 0, color="#ffe8e8", alpha=0.3, zorder=0)  # Trad/Surv
    ax.fill_between([0, 2.5], 0, 2.5, color="#e8f4ff", alpha=0.3, zorder=0)    # Sec/Self

    # Quadrant labels
    ax.text(-1.2, -2.2, "Traditional /\nSurvival", fontsize=9, color="#cc4444",
            ha="center", fontstyle="italic")
    ax.text(1.5, 2.2, "Secular-Rational /\nSelf-Expression", fontsize=9, color="#4466cc",
            ha="center", fontstyle="italic")
    ax.text(-1.2, 2.2, "Secular-Rational /\nSurvival", fontsize=9, color="#888888",
            ha="center", fontstyle="italic")
    ax.text(1.5, -2.2, "Traditional /\nSelf-Expression", fontsize=9, color="#888888",
            ha="center", fontstyle="italic")

    # Country scatter
    distances = {
        "Germany": 0.538, "United States": 0.884, "Japan": 0.990,
        "Brazil": 1.062, "China": 1.332, "India": 1.560,
        "Nigeria": 1.760, "Saudi Arabia": 1.974,
    }
    for name, (x, y) in countries.items():
        d = distances[name]
        size = max(40, 200 - d * 80)
        alpha = max(0.4, 1.0 - d * 0.35)
        ax.scatter(x, y, s=size, color=OI["blue"], alpha=alpha, edgecolor="white",
                   linewidth=1, zorder=3)
        offset_x = 0.12 if name not in ("Japan", "China") else -0.15
        offset_y = 0.12 if name not in ("Brazil",) else -0.15
        ax.annotate(f"{name}\n(d={d:.2f})", (x, y), (x + offset_x, y + offset_y),
                    fontsize=8, ha="left", va="bottom", zorder=4)

    # Claude marker (large star)
    ax.scatter(*claude_pos, s=400, color=OI["vermillion"], marker="*",
              edgecolor="white", linewidth=1.5, zorder=5)
    ax.annotate("Claude Opus 4.6\n(< 15% of humanity)",
                claude_pos, (claude_pos[0] - 0.3, claude_pos[1] - 0.5),
                fontsize=10, fontweight="bold", color=OI["vermillion"],
                ha="center", va="top",
                arrowprops=dict(arrowstyle="->", color=OI["vermillion"], lw=1.5),
                zorder=6)

    # Region box for <15% population
    rect = plt.Rectangle((0.8, 0.8), 1.7, 1.7, linewidth=1.5, edgecolor=OI["vermillion"],
                         facecolor="none", linestyle="--", zorder=2)
    ax.add_patch(rect)
    ax.text(2.3, 0.9, "<15% of\nglobal pop.", fontsize=8, color=OI["vermillion"],
            fontstyle="italic", ha="left")

    ax.set_xlabel("Survival  <<<  >>>  Self-Expression", fontsize=11)
    ax.set_ylabel("Traditional  <<<  >>>  Secular-Rational", fontsize=11)
    ax.set_title("Claude's Position on the Inglehart-Welzel Cultural Map",
                 fontweight="bold", fontsize=13)
    ax.set_xlim(-2.5, 2.7)
    ax.set_ylim(-2.5, 2.7)
    ax.set_aspect("equal")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.tight_layout()
    out = os.path.join(FIG_DIR, "cultural-map-position.png")
    fig.savefig(out)
    plt.close()
    print(f"  Fig 7: {out}")


# ══════════════════════════════════════════════════════════════
# FIG 8 — MFQ Profile Comparison
# ══════════════════════════════════════════════════════════════
def fig8_mfq_profiles():
    foundations = ["Care/\nHarm", "Fairness/\nCheating", "Loyalty/\nBetrayal",
                   "Authority/\nSubversion", "Sanctity/\nDegradation"]
    claude = [4.80, 4.70, 1.80, 1.20, 0.80]
    liberal = [3.5, 3.5, 2.5, 2.5, 2.5]
    conservative = [3.0, 3.0, 3.5, 3.5, 3.5]
    non_weird = [3.0, 3.0, 3.5, 3.5, 3.5]

    fig, ax = plt.subplots(figsize=(10, 6))
    x = np.arange(len(foundations))
    w = 0.2

    ax.bar(x - 1.5*w, claude, w, label="Claude Opus 4.6", color=OI["vermillion"],
           edgecolor="white", linewidth=0.5)
    ax.bar(x - 0.5*w, liberal, w, label="Human Liberal", color=OI["sky"],
           edgecolor="white", linewidth=0.5)
    ax.bar(x + 0.5*w, conservative, w, label="Human Conservative", color=OI["blue"],
           edgecolor="white", linewidth=0.5)
    ax.bar(x + 1.5*w, non_weird, w, label="Non-WEIRD", color=OI["green"],
           edgecolor="white", linewidth=0.5)

    # Divider between individualizing and binding
    ax.axvline(1.5, color="#cccccc", linewidth=1, linestyle="--")
    ax.text(0.75, 5.2, "INDIVIDUALIZING", ha="center", fontsize=9,
            color=OI["grey"], fontstyle="italic")
    ax.text(3.0, 5.2, "BINDING", ha="center", fontsize=9,
            color=OI["grey"], fontstyle="italic")

    # Ratio annotations
    ax.text(0.75, 4.95, "Claude I:B = 3.75", ha="center", fontsize=9,
            fontweight="bold", color=OI["vermillion"])
    ax.text(0.75, 4.72, "Liberal I:B = 1.40", ha="center", fontsize=8, color=OI["sky"])
    ax.text(0.75, 4.52, "Non-WEIRD I:B = 0.86", ha="center", fontsize=8, color=OI["green"])

    ax.set_xticks(x)
    ax.set_xticklabels(foundations, fontsize=10)
    ax.set_ylabel("MFQ Score (0-5)", fontsize=11)
    ax.set_title("Moral Foundations Profile: Claude vs. Human Populations",
                 fontweight="bold", fontsize=12)
    ax.legend(loc="upper right", framealpha=0.9, fontsize=9)
    ax.set_ylim(0, 5.5)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.tight_layout()
    out = os.path.join(FIG_DIR, "mfq-profile-comparison.png")
    fig.savefig(out)
    plt.close()
    print(f"  Fig 8: {out}")


# ══════════════════════════════════════════════════════════════
# FIG 9 — RLHF Conflict Taxonomy
# ══════════════════════════════════════════════════════════════
def fig9_rlhf_conflicts():
    categories = [
        "Individual\nautonomy\ndefault",
        "Secular\nepistemology",
        "Consequentialist\noptimization",
        "Anti-authority\nbias",
        "Gender equality\nlock",
        "Harm principle\nabsolutism",
    ]
    counts = [51, 35, 31, 8, 6, 2]
    pcts = [21.5, 14.8, 13.1, 3.4, 2.5, 0.8]

    fig, axes = plt.subplots(1, 2, figsize=(13, 5.5), gridspec_kw={"width_ratios": [1.3, 1]})

    # Left: Horizontal bar chart
    ax = axes[0]
    y = np.arange(len(categories))
    colors_list = [OI["vermillion"], OI["orange"], OI["yellow"],
                   OI["sky"], OI["blue"], OI["purple"]]
    bars = ax.barh(y, counts, 0.65, color=colors_list, edgecolor="white", linewidth=1)

    ax.set_yticks(y)
    ax.set_yticklabels(categories, fontsize=10)
    ax.set_xlabel("Conflict Instances", fontsize=11)
    ax.set_title("A. RLHF Conflict Categories\n(n=237 total; 116 'Other' not shown)",
                 fontweight="bold", fontsize=11)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.invert_yaxis()

    for bar, pct in zip(bars, pcts):
        ax.text(bar.get_width() + 0.8, bar.get_y() + bar.get_height()/2,
                f"{pct}%", va="center", fontsize=9, color=OI["black"])

    # Right: Tradition impact matrix
    ax = axes[1]
    traditions = ["Ubuntu", "Confucian", "Islamic", "Buddhist", "Dharmic", "Indigenous", "Buen Vivir"]
    conflict_names = ["Autonomy", "Secular", "Conseq.", "Anti-auth", "Gender", "Harm"]

    # Impact matrix (0=low, 1=medium, 2=high) — how each conflict zone affects each tradition
    impact = np.array([
        [2, 2, 1, 1, 1, 2, 1],  # Autonomy: high for Ubuntu, Confucian, Indigenous, Buen Vivir
        [0, 0, 2, 2, 2, 1, 1],  # Secular: high for Islamic, Buddhist, Dharmic
        [2, 2, 1, 2, 1, 1, 2],  # Consequentialist: high for Ubuntu, Confucian, Buddhist, Buen Vivir
        [1, 2, 2, 1, 1, 0, 0],  # Anti-auth: high for Confucian, Islamic
        [0, 1, 2, 0, 1, 0, 0],  # Gender: high for Islamic
        [0, 0, 1, 1, 2, 1, 0],  # Harm absolutism: high for Dharmic (purity)
    ])

    cmap = matplotlib.colors.ListedColormap(["#f0f0f0", OI["orange"], OI["vermillion"]])
    im = ax.imshow(impact, cmap=cmap, aspect="auto", vmin=0, vmax=2)

    ax.set_xticks(np.arange(len(traditions)))
    ax.set_xticklabels(traditions, rotation=45, ha="right", fontsize=9)
    ax.set_yticks(np.arange(len(conflict_names)))
    ax.set_yticklabels(conflict_names, fontsize=9)
    ax.set_title("B. Impact on Non-Western Traditions", fontweight="bold", fontsize=11)

    # Cell labels
    labels_map = {0: "", 1: "med", 2: "high"}
    for i in range(len(conflict_names)):
        for j in range(len(traditions)):
            txt = labels_map[impact[i, j]]
            color = "white" if impact[i, j] == 2 else OI["black"]
            ax.text(j, i, txt, ha="center", va="center", fontsize=7, color=color,
                    fontweight="bold" if impact[i, j] == 2 else "normal")

    # Colorbar
    cbar = plt.colorbar(im, ax=ax, ticks=[0, 1, 2], shrink=0.7, pad=0.08)
    cbar.ax.set_yticklabels(["Low", "Medium", "High"], fontsize=8)

    plt.tight_layout()
    out = os.path.join(FIG_DIR, "rlhf-conflict-taxonomy.png")
    fig.savefig(out)
    plt.close()
    print(f"  Fig 9: {out}")


# ══════════════════════════════════════════════════════════════
# FIG 10 — Triple-Bind Synthesis Diagram
# ══════════════════════════════════════════════════════════════
def fig10_triple_bind():
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    ax.set_aspect("equal")
    ax.axis("off")

    # Three circles in a triangle
    import matplotlib.patches as mpatches

    r = 1.6
    positions = {
        "scholarship": (0, 3.0),
        "benchmarks": (-3.0, -1.5),
        "models": (3.0, -1.5),
    }

    circle_data = {
        "scholarship": {
            "label": "WEIRD\nScholarship",
            "stats": "60.1% from N.Am + W.Eur\n6.9% NW engagement\nMean WEIRD: 64.5",
            "color": OI["vermillion"],
        },
        "benchmarks": {
            "label": "Broken\nBenchmarks",
            "stats": "0/218 meas. invariance\n6.8% concepts measured\n55.5% Western-created",
            "color": OI["orange"],
        },
        "models": {
            "label": "Monocultural\nModels",
            "stats": "I:B ratio 3.75\n100% Western default\n92.5% knowledge gap",
            "color": OI["blue"],
        },
    }

    for key, (cx, cy) in positions.items():
        data = circle_data[key]
        circle = plt.Circle((cx, cy), r, facecolor=data["color"], alpha=0.15,
                           edgecolor=data["color"], linewidth=2.5)
        ax.add_patch(circle)
        ax.text(cx, cy + 0.4, data["label"], ha="center", va="center",
                fontsize=12, fontweight="bold", color=data["color"])
        ax.text(cx, cy - 0.5, data["stats"], ha="center", va="center",
                fontsize=8, color="#333333", linespacing=1.4)

    # Curved arrows between circles
    arrow_style = "Simple,tail_width=3,head_width=12,head_length=8"
    arrow_kw = dict(arrowstyle=arrow_style, color="#555555", lw=1.5,
                    connectionstyle="arc3,rad=0.25")

    # Scholarship -> Benchmarks
    ax.annotate("", xy=(-2.0, -0.2), xytext=(-1.0, 1.8),
                arrowprops=arrow_kw)
    ax.text(-2.2, 1.0, "informs\nconstruct\nchoice", fontsize=8, color="#555555",
            ha="center", fontstyle="italic", rotation=30)

    # Benchmarks -> Models
    ax.annotate("", xy=(1.8, -1.5), xytext=(-1.5, -1.5),
                arrowprops=dict(arrowstyle=arrow_style, color="#555555", lw=1.5,
                               connectionstyle="arc3,rad=-0.15"))
    ax.text(0, -2.5, "optimizes\nalignment target", fontsize=8, color="#555555",
            ha="center", fontstyle="italic")

    # Models -> Scholarship
    ax.annotate("", xy=(0.8, 2.0), xytext=(2.2, -0.1),
                arrowprops=arrow_kw)
    ax.text(2.2, 1.2, "reinforces\nnormative\nvocabulary", fontsize=8, color="#555555",
            ha="center", fontstyle="italic", rotation=-30)

    # Center label
    ax.text(0, 0.2, "THE\nTRIPLE\nBIND", ha="center", va="center",
            fontsize=16, fontweight="bold", color="#333333",
            path_effects=[pe.withStroke(linewidth=3, foreground="white")])

    # Bottom annotation
    ax.text(0, -4.3, "Each layer inherits and reinforces the monoculture of the layer before it.\n"
                      "Breaking the cycle requires coordinated intervention at all three levels.",
            ha="center", va="center", fontsize=9, fontstyle="italic", color="#666666",
            bbox=dict(boxstyle="round,pad=0.5", facecolor="#f8f8f8", edgecolor="#cccccc"))

    ax.set_title("The Triple Bind: Self-Reinforcing WEIRD Bias Across Three Layers",
                 fontweight="bold", fontsize=13, pad=20)

    out = os.path.join(FIG_DIR, "triple-bind-diagram.png")
    fig.savefig(out)
    plt.close()
    print(f"  Fig 10: {out}")


# ══════════════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════════════
if __name__ == "__main__":
    print("Generating PAPER-V2 Figures 5-10...")
    fig5_benchmark_clusters()
    fig6_concept_coverage()
    fig7_cultural_map()
    fig8_mfq_profiles()
    fig9_rlhf_conflicts()
    fig10_triple_bind()
    print("All 6 figures generated.")
