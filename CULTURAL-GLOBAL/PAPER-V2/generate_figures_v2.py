#!/usr/bin/env python3
"""Generate publication-quality Figures 5-10 for PAPER-V2.

Changes from generate_new_figures.py:
  - figure.dpi: 100, savefig.dpi: 600 (per Expert 2)
  - axes.facecolor: white (removed #fafafa)
  - Font: Arial with Helvetica Neue / DejaVu Sans fallback
  - Font verification assertion
  - Dual output: PNG (600 DPI) + PDF (vector)
  - Fig 8: hatching patterns for grayscale
  - Fig 9: cividis colormap + cell borders
  - Fig 10: complete redesign — triangular flow diagram
  - All figures sized to Nature column widths (88mm / 180mm)
"""
from __future__ import annotations
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.patheffects as pe
import matplotlib.font_manager as fm
import numpy as np
import os
import sys

# ── Font verification ────────────────────────────────────────
resolved = fm.findfont("Arial")
assert "Arial" in resolved or "arial" in resolved.lower(), (
    f"Arial font not found. Resolved to: {resolved}"
)
print(f"Font verification: Arial resolved to {resolved}")

BASE = os.path.dirname(os.path.abspath(__file__))
FIG_DIR = os.path.join(BASE, "figures")
os.makedirs(FIG_DIR, exist_ok=True)

# ── Shared style (publication-quality) ───────────────────────
plt.rcParams.update({
    "figure.facecolor": "white",
    "axes.facecolor": "white",
    "font.family": "sans-serif",
    "font.sans-serif": ["Arial", "Helvetica Neue", "DejaVu Sans"],
    "font.size": 8,
    "axes.titlesize": 9,
    "axes.labelsize": 9,
    "xtick.labelsize": 7,
    "ytick.labelsize": 7,
    "legend.fontsize": 7,
    "figure.dpi": 100,
    "savefig.dpi": 600,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.15,
    "pdf.fonttype": 42,
    "ps.fonttype": 42,
})

# Okabe-Ito palette (colorblind-safe)
OI = {
    "orange": "#E69F00", "sky": "#56B4E9", "green": "#009E73",
    "yellow": "#F0E442", "blue": "#0072B2", "vermillion": "#D55E00",
    "purple": "#CC79A7", "black": "#000000", "grey": "#999999",
}

# Nature column widths in inches
SINGLE_COL = 88 / 25.4    # 3.46 in
DOUBLE_COL = 180 / 25.4   # 7.09 in


def save_figure(fig, basename: str):
    """Save figure in both PDF (vector) and PNG (600 DPI raster)."""
    png_path = os.path.join(FIG_DIR, f"{basename}.png")
    pdf_path = os.path.join(FIG_DIR, f"{basename}.pdf")
    fig.savefig(png_path, format="png")
    fig.savefig(pdf_path, format="pdf")
    print(f"  Saved: {png_path}")
    print(f"  Saved: {pdf_path}")
    return png_path


# ══════════════════════════════════════════════════════════════
# FIG 5 — Benchmark Landscape: 2-Cluster Structure
# ══════════════════════════════════════════════════════════════
def fig5_benchmark_clusters():
    fig, axes = plt.subplots(1, 2, figsize=(DOUBLE_COL, 3.3),
                             gridspec_kw={"width_ratios": [1, 1.4]})

    # Left: Cluster composition donut
    ax = axes[0]
    sizes = [47, 168]
    labels = ["Non-Western\nFocused\n(n=47, 21.9%)", "LLM-Ready\n(n=168, 78.1%)"]
    colors = [OI["vermillion"], OI["sky"]]
    wedges, texts = ax.pie(sizes, labels=labels, colors=colors,
                           startangle=90, pctdistance=0.75,
                           wedgeprops=dict(width=0.45, edgecolor="white", linewidth=2))
    for t in texts:
        t.set_fontsize(7)
        t.set_fontweight("bold")
    ax.set_title("A. Benchmark Landscape Clusters", fontweight="bold", pad=10)

    # Right: Feature comparison bars
    ax = axes[1]
    features = ["NW Framework\nCount", "LLM\nAdministrability", "Data\nAvailability",
                "Indigenous\nContent", "Non-English\nPrimary", "Format\nComplexity"]
    c1_vals = [0.915, 0.40, 1.9, 0.277, 0.574, 1.2]  # Non-Western Focused
    c2_vals = [0.012, 0.952, 2.1, 0.000, 0.351, 1.7]  # LLM-Ready

    x = np.arange(len(features))
    w = 0.35
    ax.bar(x - w/2, c1_vals, w, label="Non-Western Focused (n=47)",
           color=OI["vermillion"], edgecolor="white", linewidth=0.5,
           hatch="///")
    ax.bar(x + w/2, c2_vals, w, label="LLM-Ready (n=168)",
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
                fontsize=7, fontstyle="italic", color=OI["grey"],
                arrowprops=dict(arrowstyle="->", color=OI["grey"], lw=1.0))

    plt.tight_layout()
    save_figure(fig, "Figure5-benchmark-clusters")
    plt.close()


# ══════════════════════════════════════════════════════════════
# FIG 6 — Tradition Coverage: Concept Operationalization Gaps
# ══════════════════════════════════════════════════════════════
def fig6_concept_coverage():
    traditions = ["Confucian", "Ubuntu", "Islamic", "Dharmic", "Buddhist", "Indigenous", "Buen Vivir"]
    total_concepts = [9, 5, 7, 6, 6, 6, 5]
    measured = [2, 1, 0, 0, 0, 0, 0]
    unmeasured = [t - m for t, m in zip(total_concepts, measured)]

    fig, ax = plt.subplots(figsize=(DOUBLE_COL, 3.5))
    y = np.arange(len(traditions))
    h = 0.6

    ax.barh(y, measured, h, label="Measured concepts",
            color=OI["green"], edgecolor="white")
    ax.barh(y, unmeasured, h, left=measured, label="Unmeasured concepts",
            color=OI["vermillion"], alpha=0.7, edgecolor="white",
            hatch="///")

    ax.set_yticks(y)
    ax.set_yticklabels(traditions)
    ax.set_xlabel("Number of Moral Concepts")
    ax.set_title("Non-Western Moral Concept Operationalization in 218 Benchmarks",
                 fontweight="bold")
    ax.legend(loc="lower right", framealpha=0.9)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    # Annotate measured concepts
    concept_labels = {0: "ren, li", 1: "ubuntu"}
    for i, (m, t) in enumerate(zip(measured, total_concepts)):
        if m > 0:
            ax.text(m / 2, i, concept_labels.get(i, ""), ha="center", va="center",
                    fontsize=6, fontweight="bold", color="white")
        ax.text(t + 0.15, i, f"{m}/{t}", ha="left", va="center", fontsize=7, color=OI["black"])

    # Overall stat
    ax.text(0.98, 0.02, "3 of 44 concepts measured (6.8%)\n5 traditions at 0% coverage",
            transform=ax.transAxes, ha="right", va="bottom",
            fontsize=7, fontstyle="italic", color=OI["vermillion"],
            bbox=dict(boxstyle="round,pad=0.4", facecolor="#fff3f0",
                      edgecolor=OI["vermillion"], alpha=0.8))

    ax.set_xlim(0, 11)
    plt.tight_layout()
    save_figure(fig, "Figure6-concept-coverage")
    plt.close()


# ══════════════════════════════════════════════════════════════
# FIG 7 — Claude's Cultural Map Position (Inglehart-Welzel)
# ══════════════════════════════════════════════════════════════
def fig7_cultural_map():
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
    claude_pos = (1.8, 1.9)

    fig, ax = plt.subplots(figsize=(DOUBLE_COL, 5.5))

    # Quadrant shading
    ax.axhline(0, color="#cccccc", linewidth=0.8, zorder=1)
    ax.axvline(0, color="#cccccc", linewidth=0.8, zorder=1)
    ax.fill_between([-2.5, 0], -2.5, 0, color="#ffcccc", alpha=0.2, zorder=0)
    ax.fill_between([0, 2.5], 0, 2.5, color="#cce0ff", alpha=0.2, zorder=0)

    # Quadrant labels
    ax.text(-1.2, -2.2, "Traditional /\nSurvival", fontsize=7, color="#cc4444",
            ha="center", fontstyle="italic")
    ax.text(1.5, 2.2, "Secular-Rational /\nSelf-Expression", fontsize=7, color="#4466cc",
            ha="center", fontstyle="italic")
    ax.text(-1.2, 2.2, "Secular-Rational /\nSurvival", fontsize=7, color="#888888",
            ha="center", fontstyle="italic")
    ax.text(1.5, -2.2, "Traditional /\nSelf-Expression", fontsize=7, color="#888888",
            ha="center", fontstyle="italic")

    # Country scatter
    distances = {
        "Germany": 0.538, "United States": 0.884, "Japan": 0.990,
        "Brazil": 1.062, "China": 1.332, "India": 1.560,
        "Nigeria": 1.760, "Saudi Arabia": 1.974,
    }
    for name, (x, y) in countries.items():
        d = distances[name]
        size = max(30, 150 - d * 60)
        alpha = max(0.4, 1.0 - d * 0.35)
        ax.scatter(x, y, s=size, color=OI["blue"], alpha=alpha, edgecolor="white",
                   linewidth=0.8, zorder=3)
        offset_x = 0.12 if name not in ("Japan", "China") else -0.15
        offset_y = 0.12 if name not in ("Brazil",) else -0.15
        ax.annotate(f"{name}\n(d={d:.2f})", (x, y), (x + offset_x, y + offset_y),
                    fontsize=6, ha="left", va="bottom", zorder=4)

    # Claude marker (large star)
    ax.scatter(*claude_pos, s=300, color=OI["vermillion"], marker="*",
              edgecolor="white", linewidth=1.2, zorder=5)
    ax.annotate("Claude Opus 4.6\n(< 15% of humanity)",
                claude_pos, (claude_pos[0] - 0.3, claude_pos[1] - 0.5),
                fontsize=8, fontweight="bold", color=OI["vermillion"],
                ha="center", va="top",
                arrowprops=dict(arrowstyle="->", color=OI["vermillion"], lw=1.2),
                zorder=6)

    # Region box for <15% population
    rect = plt.Rectangle((0.8, 0.8), 1.7, 1.7, linewidth=1.2, edgecolor=OI["vermillion"],
                         facecolor="none", linestyle="--", zorder=2)
    ax.add_patch(rect)
    ax.text(2.3, 0.9, "<15% of\nglobal pop.", fontsize=6, color=OI["vermillion"],
            fontstyle="italic", ha="left")

    ax.set_xlabel("Survival  <<<  >>>  Self-Expression")
    ax.set_ylabel("Traditional  <<<  >>>  Secular-Rational")
    ax.set_title("Claude's Position on the Inglehart-Welzel Cultural Map",
                 fontweight="bold")
    ax.set_xlim(-2.5, 2.7)
    ax.set_ylim(-2.5, 2.7)
    ax.set_aspect("equal")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.tight_layout()
    save_figure(fig, "Figure7-cultural-map")
    plt.close()


# ══════════════════════════════════════════════════════════════
# FIG 8 — MFQ Profile Comparison (with hatching for grayscale)
# ══════════════════════════════════════════════════════════════
def fig8_mfq_profiles():
    foundations = ["Care/\nHarm", "Fairness/\nCheating", "Loyalty/\nBetrayal",
                   "Authority/\nSubversion", "Sanctity/\nDegradation"]
    claude = [4.80, 4.70, 1.80, 1.20, 0.80]
    liberal = [3.5, 3.5, 2.5, 2.5, 2.5]
    conservative = [3.0, 3.0, 3.5, 3.5, 3.5]
    non_weird = [3.0, 3.0, 3.5, 3.5, 3.5]

    fig, ax = plt.subplots(figsize=(DOUBLE_COL, 4.3))
    x = np.arange(len(foundations))
    w = 0.2

    # Four groups with distinct hatch patterns for grayscale
    ax.bar(x - 1.5*w, claude, w, label="Claude Opus 4.6", color=OI["vermillion"],
           edgecolor="black", linewidth=0.3, hatch="///")
    ax.bar(x - 0.5*w, liberal, w, label="Human Liberal", color=OI["sky"],
           edgecolor="black", linewidth=0.3, hatch="...")
    ax.bar(x + 0.5*w, conservative, w, label="Human Conservative", color=OI["blue"],
           edgecolor="black", linewidth=0.3, hatch="xxx")
    ax.bar(x + 1.5*w, non_weird, w, label="Non-WEIRD", color=OI["green"],
           edgecolor="black", linewidth=0.3, hatch="+++")

    # Divider between individualizing and binding
    ax.axvline(1.5, color="#cccccc", linewidth=1, linestyle="--")
    ax.text(0.75, 5.2, "INDIVIDUALIZING", ha="center", fontsize=7,
            color=OI["grey"], fontstyle="italic")
    ax.text(3.0, 5.2, "BINDING", ha="center", fontsize=7,
            color=OI["grey"], fontstyle="italic")

    # Ratio annotations
    ax.text(0.75, 4.95, "Claude I:B = 3.75", ha="center", fontsize=7,
            fontweight="bold", color=OI["vermillion"])
    ax.text(0.75, 4.72, "Liberal I:B = 1.40", ha="center", fontsize=6, color=OI["sky"])
    ax.text(0.75, 4.52, "Non-WEIRD I:B = 0.86", ha="center", fontsize=6, color=OI["green"])

    ax.set_xticks(x)
    ax.set_xticklabels(foundations)
    ax.set_ylabel("MFQ Score (0-5)")
    ax.set_title("Moral Foundations Profile: Claude vs. Human Populations",
                 fontweight="bold")
    ax.legend(loc="upper right", framealpha=0.9)
    ax.set_ylim(0, 5.5)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.tight_layout()
    save_figure(fig, "Figure8-mfq-profiles")
    plt.close()


# ══════════════════════════════════════════════════════════════
# FIG 9 — RLHF Conflict Taxonomy (cividis colormap + borders)
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

    fig, axes = plt.subplots(1, 2, figsize=(DOUBLE_COL, 3.0),
                             gridspec_kw={"width_ratios": [1.3, 1]})

    # Left: Horizontal bar chart
    ax = axes[0]
    y = np.arange(len(categories))
    colors_list = [OI["vermillion"], OI["orange"], OI["yellow"],
                   OI["sky"], OI["blue"], OI["purple"]]
    bars = ax.barh(y, counts, 0.65, color=colors_list, edgecolor="white", linewidth=1)

    ax.set_yticks(y)
    ax.set_yticklabels(categories)
    ax.set_xlabel("Conflict Instances")
    ax.set_title("A. RLHF Conflict Categories\n(n=237 total; 116 'Other' not shown)",
                 fontweight="bold")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.invert_yaxis()

    for bar, pct in zip(bars, pcts):
        ax.text(bar.get_width() + 0.8, bar.get_y() + bar.get_height()/2,
                f"{pct}%", va="center", fontsize=7, color=OI["black"])

    # Right: Tradition impact matrix — cividis colormap with cell borders
    ax = axes[1]
    traditions = ["Ubuntu", "Confucian", "Islamic", "Buddhist", "Dharmic", "Indigenous", "Buen Vivir"]
    conflict_names = ["Autonomy", "Secular", "Conseq.", "Anti-auth", "Gender", "Harm"]

    impact = np.array([
        [2, 2, 1, 1, 1, 2, 1],
        [0, 0, 2, 2, 2, 1, 1],
        [2, 2, 1, 2, 1, 1, 2],
        [1, 2, 2, 1, 1, 0, 0],
        [0, 1, 2, 0, 1, 0, 0],
        [0, 0, 1, 1, 2, 1, 0],
    ])

    # Use cividis (grayscale-safe, CVD-safe) with 3 discrete levels
    cividis = plt.cm.cividis
    cmap = matplotlib.colors.ListedColormap([cividis(0.1), cividis(0.5), cividis(0.9)])
    im = ax.imshow(impact, cmap=cmap, aspect="auto", vmin=0, vmax=2)

    # Add cell borders
    for i in range(len(conflict_names)):
        for j in range(len(traditions)):
            rect = plt.Rectangle((j - 0.5, i - 0.5), 1, 1,
                                 linewidth=0.5, edgecolor="#666666", facecolor="none")
            ax.add_patch(rect)

    ax.set_xticks(np.arange(len(traditions)))
    ax.set_xticklabels(traditions, rotation=45, ha="right")
    ax.set_yticks(np.arange(len(conflict_names)))
    ax.set_yticklabels(conflict_names)
    ax.set_title("B. Impact on Non-Western Traditions", fontweight="bold")

    # Cell labels
    labels_map = {0: "", 1: "med", 2: "high"}
    for i in range(len(conflict_names)):
        for j in range(len(traditions)):
            txt = labels_map[impact[i, j]]
            # Use contrasting text color based on background brightness
            color = "white" if impact[i, j] == 2 else "black"
            ax.text(j, i, txt, ha="center", va="center", fontsize=5.5, color=color,
                    fontweight="bold" if impact[i, j] == 2 else "normal")

    # Colorbar
    cbar = plt.colorbar(im, ax=ax, ticks=[0, 1, 2], shrink=0.7, pad=0.08)
    cbar.ax.set_yticklabels(["Low", "Medium", "High"], fontsize=6)

    plt.tight_layout()
    save_figure(fig, "Figure9-rlhf-taxonomy")
    plt.close()


# ══════════════════════════════════════════════════════════════
# FIG 10 — Triple-Bind: Triangular Flow Diagram (REDESIGN)
# ══════════════════════════════════════════════════════════════
def fig10_triple_bind():
    fig, ax = plt.subplots(figsize=(DOUBLE_COL, 6.5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 9.5)
    ax.set_aspect("equal")
    ax.axis("off")

    # ── A. Three node boxes (rounded rectangles) ─────────────
    nodes = {
        "scholarship": {
            "center": (5.0, 7.8),
            "label": "WEIRD SCHOLARSHIP",
            "stats": "60.1% N.Am + W.Eur\n6.9% NW engagement\nMean WEIRD: 64.5",
            "color": OI["vermillion"],
            "linestyle": "solid",
        },
        "benchmarks": {
            "center": (1.8, 1.8),
            "label": "BROKEN BENCHMARKS",
            "stats": "0/218 meas. invariance\n6.8% concepts measured\n55.5% Western-created",
            "color": OI["orange"],
            "linestyle": "dashed",
        },
        "models": {
            "center": (8.2, 1.8),
            "label": "MONOCULTURAL MODELS",
            "stats": "I:B ratio 3.75\n100% Western default\n92.5% knowledge gap",
            "color": OI["blue"],
            "linestyle": "dotted",
        },
    }

    box_w, box_h = 3.2, 2.0

    for key, node in nodes.items():
        cx, cy = node["center"]
        # Rounded rectangle
        rect = mpatches.FancyBboxPatch(
            (cx - box_w/2, cy - box_h/2), box_w, box_h,
            boxstyle="round,pad=0.2",
            facecolor=matplotlib.colors.to_rgba(node["color"], 0.12),
            edgecolor=node["color"],
            linewidth=2.0,
            linestyle=node["linestyle"],
            zorder=3,
        )
        ax.add_patch(rect)

        # Title
        ax.text(cx, cy + 0.5, node["label"],
                ha="center", va="center",
                fontsize=8, fontweight="bold", color=node["color"],
                zorder=4)
        # Stats
        ax.text(cx, cy - 0.25, node["stats"],
                ha="center", va="center",
                fontsize=6, color="#333333", linespacing=1.4,
                zorder=4)

    # ── B. Arrows (clockwise cycle) ──────────────────────────
    arrow_style = "Simple,tail_width=3,head_width=10,head_length=7"
    arrow_color = "#444444"

    # Scholarship (bottom-left) -> Benchmarks (top)
    ax.annotate("", xy=(2.4, 2.85), xytext=(3.6, 6.75),
                arrowprops=dict(arrowstyle=arrow_style, color=arrow_color, lw=1.2,
                                connectionstyle="arc3,rad=0.15"),
                zorder=2)

    # Benchmarks (right) -> Models (left)
    ax.annotate("", xy=(6.55, 1.8), xytext=(3.45, 1.8),
                arrowprops=dict(arrowstyle=arrow_style, color=arrow_color, lw=1.2,
                                connectionstyle="arc3,rad=-0.15"),
                zorder=2)

    # Models (top) -> Scholarship (bottom-right)
    ax.annotate("", xy=(6.4, 6.75), xytext=(7.6, 2.85),
                arrowprops=dict(arrowstyle=arrow_style, color=arrow_color, lw=1.2,
                                connectionstyle="arc3,rad=0.15"),
                zorder=2)

    # ── C. Mechanism edge-boxes (on arrows) ──────────────────
    mechanisms = [
        {
            "pos": (2.2, 5.1),
            "title": "CONSTRUCT SELECTION",
            "subtitle": "Western frameworks define\nwhat to measure",
        },
        {
            "pos": (5.0, 0.5),
            "title": "ALIGNMENT TARGET",
            "subtitle": "RLHF optimizes for\nWEIRD-normed benchmarks",
        },
        {
            "pos": (7.8, 5.1),
            "title": "NORMATIVE FEEDBACK",
            "subtitle": "Model outputs reinforce\ndominant vocabulary",
        },
    ]

    for mech in mechanisms:
        mx, my = mech["pos"]
        mbox = mpatches.FancyBboxPatch(
            (mx - 1.35, my - 0.45), 2.7, 0.9,
            boxstyle="round,pad=0.15",
            facecolor="#f5f5f5",
            edgecolor="#888888",
            linewidth=0.8,
            linestyle="--",
            zorder=5,
        )
        ax.add_patch(mbox)
        ax.text(mx, my + 0.15, mech["title"],
                ha="center", va="center",
                fontsize=6, fontweight="bold", color="#333333",
                zorder=6)
        ax.text(mx, my - 0.2, mech["subtitle"],
                ha="center", va="center",
                fontsize=5.5, fontstyle="italic", color="#666666",
                linespacing=1.2, zorder=6)

    # ── D. Center amplification indicator ────────────────────
    center_x, center_y = 5.0, 3.8
    center_box = mpatches.FancyBboxPatch(
        (center_x - 1.4, center_y - 0.75), 2.8, 1.5,
        boxstyle="round,pad=0.25",
        facecolor="white",
        edgecolor="#CC0000",
        linewidth=1.5,
        zorder=7,
    )
    ax.add_patch(center_box)
    ax.text(center_x, center_y + 0.25, "AMPLIFICATION\nCYCLE",
            ha="center", va="center",
            fontsize=9, fontweight="bold", color="#CC0000",
            linespacing=1.2, zorder=8)
    ax.text(center_x, center_y - 0.35,
            "Each layer inherits and\namplifies the monoculture\nof the layer before it",
            ha="center", va="center",
            fontsize=5.5, fontstyle="italic", color="#666666",
            linespacing=1.3, zorder=8)

    # ── E. Title ─────────────────────────────────────────────
    ax.set_title("The Triple Bind: Self-Reinforcing WEIRD Bias Across Three Layers",
                 fontweight="bold", fontsize=10, pad=15)

    save_figure(fig, "Figure10-triple-bind")
    plt.close()


# ══════════════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════════════
if __name__ == "__main__":
    print("Generating PAPER-V2 Figures 5-10 (publication quality)...")
    print(f"  Output directory: {FIG_DIR}")
    print(f"  savefig.dpi: {plt.rcParams['savefig.dpi']}")
    print()

    fig5_benchmark_clusters()
    fig6_concept_coverage()
    fig7_cultural_map()
    fig8_mfq_profiles()
    fig9_rlhf_conflicts()
    fig10_triple_bind()

    print("\nAll 6 figures generated (PNG + PDF).")
