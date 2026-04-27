#!/usr/bin/env python3
"""Generate new figures for Religious Values Benchmark Paper v2.

Figures 10-13 (main body) and S4-S8 (supplementary).
Uses matplotlib/seaborn with an academic, colorblind-safe style.
"""
from __future__ import annotations

import json
import os
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np
import seaborn as sns

# Paths
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FIGURES_DIR = os.path.join(SCRIPT_DIR, "figures")
DATA_DIR = os.path.join(os.path.dirname(SCRIPT_DIR), "data")
COMPARISON_DIR = os.path.join(os.path.dirname(SCRIPT_DIR), "COMPARISON", "results")

os.makedirs(FIGURES_DIR, exist_ok=True)

# Style
plt.rcParams.update({
    "font.family": "serif",
    "font.size": 11,
    "axes.labelsize": 12,
    "axes.titlesize": 13,
    "legend.fontsize": 9,
    "xtick.labelsize": 10,
    "ytick.labelsize": 10,
    "figure.dpi": 300,
    "savefig.dpi": 300,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.15,
})

# Okabe-Ito colorblind-safe palette
OI_BLUE = "#0072B2"
OI_ORANGE = "#E69F00"
OI_GREEN = "#009E73"
OI_RED = "#D55E00"
OI_PURPLE = "#CC79A7"
OI_CYAN = "#56B4E9"
OI_YELLOW = "#F0E442"
OI_BLACK = "#000000"

VENDOR_COLORS = {
    "Anthropic": OI_BLUE,
    "OpenAI": OI_GREEN,
    "Gemini": OI_RED,
}

KRV_COLORS = {
    "Knowledge": OI_CYAN,
    "Reasoning": OI_ORANGE,
    "Values": OI_RED,
}

# ── Data ──────────────────────────────────────────────────────────────

# Cross-model aggregate (Claude family)
CLAUDE_MODELS = {
    "Opus": {"K": 1853, "R": 4586, "V": 6327, "VK": 3.41},
    "Sonnet": {"K": 1771, "R": 5194, "V": 6364, "VK": 3.59},
    "Haiku": {"K": 766, "R": 3354, "V": 7026, "VK": 9.18},
}

# Per-tradition gradient
TRADITION_GRADIENT = {
    ("Islam", "Opus"): (1310, 3952, 6376),
    ("Islam", "Sonnet"): (1336, 4358, 6768),
    ("Islam", "Haiku"): (746, 1963, 4058),
    ("Christianity", "Opus"): (1272, 4250, 6053),
    ("Christianity", "Sonnet"): (1421, 5626, 5694),
    ("Christianity", "Haiku"): (660, 3679, 9179),
    ("Hinduism", "Opus"): (2978, 5557, 6546),
    ("Hinduism", "Sonnet"): (2557, 5599, 6580),
    ("Hinduism", "Haiku"): (891, 4421, 8212),
}

# All 9 models
ALL_MODELS = [
    {"name": "Opus", "vendor": "Anthropic", "K": 1853, "R": 4586, "V": 6327,
     "rK": 1.0, "rR": 1.0, "rV": 0.933, "rB": 1.0,
     "t2": 100, "t2b": 100, "t2a": 100, "bv_r": 0.706, "gradient": True},
    {"name": "Sonnet", "vendor": "Anthropic", "K": 1771, "R": 5194, "V": 6364,
     "rK": 1.0, "rR": 1.0, "rV": 1.0, "rB": 1.0,
     "t2": 100, "t2b": 100, "t2a": 100, "bv_r": 0.288, "gradient": True},
    {"name": "Haiku", "vendor": "Anthropic", "K": 766, "R": 3354, "V": 7026,
     "rK": 1.0, "rR": 1.0, "rV": 1.0, "rB": 1.0,
     "t2": 76.7, "t2b": 80, "t2a": 73.3, "bv_r": 0.701, "gradient": True},
    {"name": "GPT-Codex", "vendor": "OpenAI", "K": 82, "R": 472, "V": 461,
     "rK": 0.933, "rR": 0.956, "rV": 0.867, "rB": 1.0,
     "t2": 100, "t2b": 100, "t2a": 100, "bv_r": 0.296, "gradient": False},
    {"name": "Codex-Mini", "vendor": "OpenAI", "K": 78, "R": 415, "V": 416,
     "rK": 1.0, "rR": 0.878, "rV": 0.9, "rB": 1.0,
     "t2": 86.7, "t2b": 80, "t2a": 93.3, "bv_r": 0.076, "gradient": True},
    {"name": "Gem-FL", "vendor": "Gemini", "K": 63, "R": 104, "V": 101,
     "rK": 0.0, "rR": 0.0, "rV": 0.2, "rB": 1.0,
     "t2": 20, "t2b": 20, "t2a": 20, "bv_r": 1.0, "gradient": False},
    {"name": "Gem-Flash", "vendor": "Gemini", "K": 201, "R": 268, "V": 222,
     "rK": 0.0, "rR": 0.0, "rV": 0.0, "rB": 0.567,
     "t2": 10, "t2b": 6.7, "t2a": 13.3, "bv_r": 1.0, "gradient": False},
    {"name": "Gem-Pro", "vendor": "Gemini", "K": 231, "R": 305, "V": 244,
     "rK": 0.0, "rR": 0.0, "rV": 0.0, "rB": 1.0,
     "t2": 6.7, "t2b": 0, "t2a": 13.3, "bv_r": 1.0, "gradient": False},
    {"name": "Gem-3.1P", "vendor": "Gemini", "K": 310, "R": 328, "V": 318,
     "rK": 0.0, "rR": 0.0, "rV": 0.0, "rB": 1.0,
     "t2": 10, "t2b": 13.3, "t2a": 6.7, "bv_r": 1.0, "gradient": False},
]

# Year distribution of 401 candidates (73% from 2024-2026 per spine)
YEAR_DIST = {
    2010: 1, 2016: 1, 2018: 2, 2019: 4, 2020: 7, 2021: 14,
    2022: 32, 2023: 47, 2024: 112, 2025: 149, 2026: 32,
}
# Verify: 2024+2025+2026 = 293, 293/401 = 73.1%


# ── Figure 10: Cross-Model K<R<V Grouped Bar ─────────────────────────

def fig10_cross_model_gradient():
    fig, ax = plt.subplots(figsize=(8, 5))
    models = list(CLAUDE_MODELS.keys())
    x = np.arange(len(models))
    w = 0.25

    for i, (label, color) in enumerate(KRV_COLORS.items()):
        key = label[0]  # K, R, V
        vals = [CLAUDE_MODELS[m][key] for m in models]
        bars = ax.bar(x + (i - 1) * w, vals, w, label=label, color=color,
                      edgecolor="white", linewidth=0.5)
        for bar, val in zip(bars, vals):
            ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 100,
                    f"{val:,.0f}", ha="center", va="bottom", fontsize=8)

    # V/K annotations
    for j, m in enumerate(models):
        vk = CLAUDE_MODELS[m]["VK"]
        ax.text(x[j] + w, CLAUDE_MODELS[m]["V"] + 400,
                f"V/K={vk}x", ha="center", va="bottom", fontsize=8,
                fontstyle="italic", color=OI_BLACK)

    ax.set_xticks(x)
    ax.set_xticklabels(models)
    ax.set_ylabel("Mean Response Length (characters)")
    ax.set_title("Figure 10: K < R < V Response Length Gradient (Claude Family)")
    ax.legend(loc="upper left")
    ax.set_ylim(0, 8500)
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda v, _: f"{v:,.0f}"))
    sns.despine()
    fig.savefig(os.path.join(FIGURES_DIR, "fig10-cross-model-gradient.png"))
    plt.close(fig)
    print("  fig10 done")


# ── Figure 11: Cross-Vendor Rubric Heatmap ───────────────────────────

def fig11_rubric_heatmap():
    dims = ["Knowledge", "Reasoning", "Values", "Bias"]
    dim_keys = ["rK", "rR", "rV", "rB"]
    names = [m["name"] for m in ALL_MODELS]
    data = np.array([[m[k] for k in dim_keys] for m in ALL_MODELS])

    fig, ax = plt.subplots(figsize=(7, 6))

    # Custom colormap: red (0) -> orange (0.5) -> green (1.0)
    from matplotlib.colors import LinearSegmentedColormap
    cmap = LinearSegmentedColormap.from_list(
        "rubric", [(0, OI_RED), (0.35, OI_ORANGE), (0.7, OI_YELLOW), (1.0, OI_GREEN)]
    )

    im = ax.imshow(data, cmap=cmap, vmin=0, vmax=1, aspect="auto")

    ax.set_xticks(range(len(dims)))
    ax.set_xticklabels(dims)
    ax.set_yticks(range(len(names)))
    ax.set_yticklabels(names)

    # Add text annotations
    for i in range(len(names)):
        for j in range(len(dims)):
            val = data[i, j]
            color = "white" if val < 0.4 else "black"
            ax.text(j, i, f"{val:.2f}" if val > 0 else "0.00",
                    ha="center", va="center", fontsize=9, color=color,
                    fontweight="bold" if val >= 0.9 else "normal")

    # Vendor separators
    ax.axhline(2.5, color="white", linewidth=2)
    ax.axhline(4.5, color="white", linewidth=2)

    # Vendor labels on right
    ax.text(len(dims) + 0.3, 1, "Anthropic", va="center", fontsize=9,
            color=VENDOR_COLORS["Anthropic"], fontweight="bold")
    ax.text(len(dims) + 0.3, 3.5, "OpenAI", va="center", fontsize=9,
            color=VENDOR_COLORS["OpenAI"], fontweight="bold")
    ax.text(len(dims) + 0.3, 6.5, "Gemini", va="center", fontsize=9,
            color=VENDOR_COLORS["Gemini"], fontweight="bold")

    cbar = fig.colorbar(im, ax=ax, shrink=0.8, label="Rubric Score")
    ax.set_title("Figure 11: Cross-Vendor Rubric Scores (9 Models x 4 Dimensions)")
    fig.savefig(os.path.join(FIGURES_DIR, "fig11-rubric-heatmap.png"))
    plt.close(fig)
    print("  fig11 done")


# ── Figure 12: T2 Accuracy by Model ─────────────────────────────────

def fig12_t2_accuracy():
    # Sort by accuracy descending
    sorted_models = sorted(ALL_MODELS, key=lambda m: m["t2"])
    names = [m["name"] for m in sorted_models]
    accs = [m["t2"] for m in sorted_models]
    colors = [VENDOR_COLORS[m["vendor"]] for m in sorted_models]

    fig, ax = plt.subplots(figsize=(8, 5))
    y = np.arange(len(names))
    bars = ax.barh(y, accs, color=colors, edgecolor="white", linewidth=0.5, height=0.7)

    # Value labels
    for bar, acc in zip(bars, accs):
        xpos = bar.get_width() + 1.5
        if acc < 25:
            xpos = bar.get_width() + 1.5
        ax.text(xpos, bar.get_y() + bar.get_height() / 2,
                f"{acc:.1f}%", va="center", fontsize=9)

    # Random chance line
    ax.axvline(16.7, color=OI_BLACK, linestyle="--", linewidth=1, alpha=0.6)
    ax.text(17.5, len(names) - 0.5, "Random chance\n(16.7%)", fontsize=8,
            va="top", alpha=0.7)

    ax.set_yticks(y)
    ax.set_yticklabels(names)
    ax.set_xlabel("T2 Arabic MCQ Accuracy (%)")
    ax.set_title("Figure 12: T2 Islamic Inheritance Law Accuracy (30 Items)")
    ax.set_xlim(0, 115)

    # Legend
    from matplotlib.patches import Patch
    legend_elements = [Patch(facecolor=c, label=v) for v, c in VENDOR_COLORS.items()]
    ax.legend(handles=legend_elements, loc="lower right")
    sns.despine()
    fig.savefig(os.path.join(FIGURES_DIR, "fig12-t2-accuracy.png"))
    plt.close(fig)
    print("  fig12 done")


# ── Figure 13: Vendor Capability Radar ───────────────────────────────

def fig13_vendor_radar():
    categories = [
        "K<R<V\nGradient",
        "Rubric\nValues",
        "T2\nAccuracy",
        "Bias-Values\nIndependence",
        "Mean V/K\nRatio",
    ]
    N = len(categories)

    # Normalize all to 0-1
    vendor_data = {
        "Anthropic": [
            1.0,       # 3/3 gradient
            0.978,     # mean rubric V
            0.922,     # mean T2
            0.33,      # 1/3 independent
            min(1.0, 5.39 / 10),  # mean V/K normalized
        ],
        "OpenAI": [
            0.5,       # 1/2 gradient
            0.883,     # mean rubric V
            0.933,     # mean T2
            1.0,       # 2/2 independent
            min(1.0, 5.48 / 10),
        ],
        "Gemini": [
            0.0,       # 0/4 gradient
            0.05,      # mean rubric V
            0.117,     # mean T2
            0.0,       # 0/4 independent
            min(1.0, 1.2 / 10),
        ],
    }

    angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(7, 7), subplot_kw=dict(polar=True))

    for vendor, values in vendor_data.items():
        vals = values + values[:1]
        ax.plot(angles, vals, "o-", linewidth=2, label=vendor,
                color=VENDOR_COLORS[vendor], markersize=5)
        ax.fill(angles, vals, alpha=0.15, color=VENDOR_COLORS[vendor])

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, fontsize=9)
    ax.set_ylim(0, 1.1)
    ax.set_yticks([0.25, 0.5, 0.75, 1.0])
    ax.set_yticklabels(["0.25", "0.50", "0.75", "1.00"], fontsize=8, alpha=0.6)
    ax.set_title("Figure 13: Vendor Capability Radar (Normalized Metrics)", pad=20)
    ax.legend(loc="lower right", bbox_to_anchor=(1.15, -0.05))
    fig.savefig(os.path.join(FIGURES_DIR, "fig13-vendor-radar.png"))
    plt.close(fig)
    print("  fig13 done")


# ── Figure S4: Per-Tradition Gradient (3x3 Small Multiples) ──────────

def figs4_tradition_gradient():
    traditions = ["Islam", "Christianity", "Hinduism"]
    models = ["Opus", "Sonnet", "Haiku"]

    fig, axes = plt.subplots(3, 3, figsize=(12, 10), sharey=False)
    fig.suptitle("Figure S4: K < R < V Gradient by Tradition and Model", fontsize=14)

    for row, tradition in enumerate(traditions):
        for col, model in enumerate(models):
            ax = axes[row, col]
            k, r, v = TRADITION_GRADIENT[(tradition, model)]
            vk = v / k if k > 0 else 0

            bars = ax.bar(["K", "R", "V"], [k, r, v],
                          color=[KRV_COLORS["Knowledge"],
                                 KRV_COLORS["Reasoning"],
                                 KRV_COLORS["Values"]],
                          edgecolor="white", linewidth=0.5)

            ax.set_title(f"{model} | {tradition}", fontsize=10)
            ax.set_ylabel("Chars" if col == 0 else "")

            # V/K annotation
            ax.text(2, v + 200, f"V/K={vk:.1f}x", ha="center", fontsize=8,
                    fontstyle="italic")

            for bar, val in zip(bars, [k, r, v]):
                ax.text(bar.get_x() + bar.get_width() / 2, val + 50,
                        f"{val:,}", ha="center", va="bottom", fontsize=7)

            sns.despine(ax=ax)

    fig.tight_layout(rect=[0, 0, 1, 0.95])
    fig.savefig(os.path.join(FIGURES_DIR, "fig-s4-tradition-gradient.png"))
    plt.close(fig)
    print("  figS4 done")


# ── Figure S5: Cross-Vendor Response Length (Log Scale) ──────────────

def figs5_cross_vendor_length():
    fig, ax = plt.subplots(figsize=(10, 5))
    names = [m["name"] for m in ALL_MODELS]
    x = np.arange(len(names))
    w = 0.25

    for i, (label, color) in enumerate(KRV_COLORS.items()):
        key = label[0]
        vals = [m[key] for m in ALL_MODELS]
        ax.bar(x + (i - 1) * w, vals, w, label=label, color=color,
               edgecolor="white", linewidth=0.5)

    ax.set_yscale("log")
    ax.set_xticks(x)
    ax.set_xticklabels(names, rotation=30, ha="right")
    ax.set_ylabel("Mean Response Length (characters, log scale)")
    ax.set_title("Figure S5: Response Length by Construct Type (All 9 Models, Log Scale)")
    ax.legend()

    # Vendor separators
    ax.axvline(2.5, color="gray", linestyle=":", linewidth=0.8)
    ax.axvline(4.5, color="gray", linestyle=":", linewidth=0.8)
    ax.text(1, ax.get_ylim()[1] * 0.7, "Anthropic", ha="center", fontsize=9,
            color=VENDOR_COLORS["Anthropic"], fontweight="bold")
    ax.text(3.5, ax.get_ylim()[1] * 0.7, "OpenAI", ha="center", fontsize=9,
            color=VENDOR_COLORS["OpenAI"], fontweight="bold")
    ax.text(6.5, ax.get_ylim()[1] * 0.7, "Gemini", ha="center", fontsize=9,
            color=VENDOR_COLORS["Gemini"], fontweight="bold")

    sns.despine()
    fig.savefig(os.path.join(FIGURES_DIR, "fig-s5-cross-vendor-length.png"))
    plt.close(fig)
    print("  figS5 done")


# ── Figure S2: Gate Threshold Sensitivity Curves ─────────────────────

def figs2_gate_threshold_sensitivity():
    """Joint-gate sensitivity sweep with tradition coverage on secondary axis.

    Loads real sensitivity data from data/20260404-sensitivity-analysis.json.
    Shows how the joint (RD AND data availability) gate count changes across
    RD thresholds, plus tradition-family coverage as a secondary y-axis. The
    baseline (RD=30) is marked, and the void-traditions-gained annotations
    document which traditions enter the gate-passing set at lower thresholds.
    """
    sens_path = os.path.join(DATA_DIR, "20260404-sensitivity-analysis.json")
    with open(sens_path) as f:
        sens = json.load(f)
    gt_results = sens["gate_threshold"]["results"]

    thresholds = [r["threshold"] for r in gt_results]
    joint = [r["gate_passers"] for r in gt_results]
    traditions = [r["traditions_represented"] for r in gt_results]
    voids_gained = [len(r.get("void_traditions_gained", [])) for r in gt_results]

    fig, ax1 = plt.subplots(figsize=(9.5, 5.8))

    # Primary axis: joint gate count
    line1 = ax1.plot(thresholds, joint, "o-", linewidth=2.5, markersize=9,
                     color=OI_BLUE, label="Joint gate-passers (RD \u2227 data availability)")
    ax1.set_xlabel("RD (Religious/Theological Depth) Threshold")
    ax1.set_ylabel("Number of Gate-Passing Candidates", color=OI_BLUE)
    ax1.tick_params(axis="y", labelcolor=OI_BLUE)
    ax1.set_yscale("log")
    ax1.set_xticks(thresholds)
    ax1.grid(True, alpha=0.3, linestyle=":")

    # Annotate gate count at each point
    for t, j in zip(thresholds, joint):
        ax1.annotate(f"{j}", (t, j), textcoords="offset points",
                     xytext=(8, 4), ha="left", fontsize=9, color=OI_BLUE,
                     fontweight="bold")

    # Secondary axis: traditions represented
    ax2 = ax1.twinx()
    line2 = ax2.plot(thresholds, traditions, "s--", linewidth=2, markersize=8,
                     color=OI_ORANGE, label="Tradition families represented",
                     alpha=0.9)
    ax2.set_ylabel("Tradition Families with $\\geq$1 Gate-Passer",
                   color=OI_ORANGE)
    ax2.tick_params(axis="y", labelcolor=OI_ORANGE)
    ax2.set_ylim(0, 14)
    ax2.set_yticks(range(0, 15, 2))

    # Annotate tradition counts
    for t, n in zip(thresholds, traditions):
        ax2.annotate(f"{n}", (t, n), textcoords="offset points",
                     xytext=(8, -12), ha="left", fontsize=9, color=OI_RED,
                     fontstyle="italic")

    # Mark baseline at RD=30
    ax1.axvline(30, color=OI_BLACK, linestyle="-", linewidth=1.2, alpha=0.5)
    ax1.text(30.3, ax1.get_ylim()[1] * 0.5, "Baseline\n(RD=30)",
             fontsize=9, va="center", ha="left", alpha=0.75, fontweight="bold")

    # Footnote box: void traditions gained at low thresholds
    void_note = (
        "Void traditions gained at lower RD thresholds:\n"
        "RD=15: +5 (Indigenous, Jainism, Judaism, Taoism, Ubuntu)\n"
        "RD=20: +2 (Jainism, Judaism)\n"
        "RD=25 to 50: no additional traditions"
    )
    ax1.text(0.98, 0.02, void_note, transform=ax1.transAxes,
             fontsize=8, va="bottom", ha="right",
             bbox=dict(boxstyle="round,pad=0.4", facecolor="white",
                       edgecolor="gray", alpha=0.95))

    # Combined legend
    lines = line1 + line2
    labels = [l.get_label() for l in lines]
    ax1.legend(lines, labels, loc="upper right", framealpha=0.95,
               bbox_to_anchor=(1.0, 1.0))

    ax1.set_title("Figure S2: Gate Threshold Sensitivity (Joint Gate Sweep)")
    sns.despine(right=False)
    fig.tight_layout()
    fig.savefig(os.path.join(FIGURES_DIR, "fig-s2-gate-threshold-sensitivity.png"))
    plt.close(fig)
    print("  figS2 done")


# ── Figure S6: Bias-Values Scatter Plots Per Model ───────────────────

def figs6_bias_values_scatter():
    """Scatter plots of bias-item vs values-item response lengths per Claude model.

    Loads real trial data from data/20260404-trial-{tradition}-{model}.json.
    Each point pairs a bias item with the matched values item from the same
    tradition. Pearson r is computed and annotated per panel.
    """
    import glob
    from scipy.stats import pearsonr

    models = ["opus", "sonnet", "haiku"]
    traditions = ["islam", "christianity", "hinduism"]
    trad_colors = {"islam": OI_BLUE, "christianity": OI_ORANGE, "hinduism": OI_GREEN}

    fig, axes = plt.subplots(1, 3, figsize=(13, 4.5))
    fig.suptitle("Figure S6: Bias vs Values Response Length (Per Model)", fontsize=14)

    for col, model in enumerate(models):
        ax = axes[col]
        all_x, all_y = [], []
        all_colors = []

        for trad in traditions:
            trial_path = os.path.join(DATA_DIR, f"20260404-trial-{trad}-{model}.json")
            if not os.path.exists(trial_path):
                continue
            with open(trial_path) as fp:
                trial = json.load(fp)

            # Build maps: numeric index -> response length
            # Prefer values_paired items (Sonnet, Haiku); fall back to regular
            # values items paired by index (Opus, which lacks values_paired).
            bias_by_idx = {}
            values_paired_by_idx = {}
            values_by_idx = {}
            for r in trial["results"]:
                if r["type"] == "bias":
                    # item_id like "bias_christianity_1"
                    parts = r["item_id"].rsplit("_", 1)
                    if len(parts) == 2 and parts[1].isdigit():
                        bias_by_idx[int(parts[1])] = len(r["response"])
                elif r["type"] == "values_paired":
                    # item_id like "values_christianity_1"
                    parts = r["item_id"].rsplit("_", 1)
                    if len(parts) == 2 and parts[1].isdigit():
                        values_paired_by_idx[int(parts[1])] = len(r["response"])
                elif r["type"] == "values":
                    # item_id like "christianity_V1"
                    suffix = r["item_id"].split("_")[-1]
                    if suffix.startswith("V") and suffix[1:].isdigit():
                        values_by_idx[int(suffix[1:])] = len(r["response"])

            # Use values_paired if available, else fall back to regular values
            if values_paired_by_idx:
                values_source = values_paired_by_idx
            else:
                values_source = values_by_idx

            # Pair by index
            common = sorted(set(bias_by_idx) & set(values_source))
            for idx in common:
                all_x.append(bias_by_idx[idx])
                all_y.append(values_source[idx])
                all_colors.append(trad_colors[trad])

        if len(all_x) < 2:
            ax.text(0.5, 0.5, "Insufficient\npaired data",
                    transform=ax.transAxes, ha="center", va="center",
                    fontsize=11, color="gray")
            ax.set_title(model.capitalize())
            continue

        x_arr = np.array(all_x)
        y_arr = np.array(all_y)
        r, p = pearsonr(x_arr, y_arr)

        ax.scatter(x_arr, y_arr, c=all_colors, s=70, alpha=0.75,
                   edgecolor="white", linewidth=0.8)

        # Diagonal y=x reference line
        lim = max(x_arr.max(), y_arr.max()) * 1.1
        ax.plot([0, lim], [0, lim], "--", color="gray", linewidth=1, alpha=0.6)

        # Linear regression line
        if len(x_arr) >= 2:
            coeffs = np.polyfit(x_arr, y_arr, 1)
            x_line = np.array([x_arr.min(), x_arr.max()])
            y_line = coeffs[0] * x_line + coeffs[1]
            ax.plot(x_line, y_line, "-", color=OI_BLACK, linewidth=1.5, alpha=0.8)

        # Annotate r with independence verdict
        independent = "independent" if r < 0.30 else "conflated"
        verdict_color = OI_GREEN if r < 0.30 else OI_RED
        ax.text(0.05, 0.95, f"r = {r:.3f}\n({independent})",
                transform=ax.transAxes, fontsize=10, va="top",
                fontweight="bold", color=verdict_color,
                bbox=dict(boxstyle="round,pad=0.3", facecolor="white",
                          edgecolor=verdict_color, alpha=0.9))

        ax.set_title(f"{model.capitalize()} (n={len(x_arr)} pairs)")
        ax.set_xlabel("Bias item response length (chars)")
        if col == 0:
            ax.set_ylabel("Values item response length (chars)")
        ax.set_xlim(0, lim)
        ax.set_ylim(0, lim)
        ax.grid(True, alpha=0.3, linestyle=":")

    # Tradition legend (shared)
    from matplotlib.patches import Patch
    legend_elements = [
        Patch(facecolor=trad_colors["islam"], label="Islam"),
        Patch(facecolor=trad_colors["christianity"], label="Christianity"),
        Patch(facecolor=trad_colors["hinduism"], label="Hinduism"),
    ]
    fig.legend(handles=legend_elements, loc="lower center", ncol=3,
               bbox_to_anchor=(0.5, -0.02), frameon=False)

    sns.despine()
    fig.tight_layout(rect=[0, 0.03, 1, 0.95])
    fig.savefig(os.path.join(FIGURES_DIR, "fig-s6-bias-values-scatter.png"))
    plt.close(fig)
    print("  figS6 done")


# ── Figure S7: T2 Beginner vs. Advanced ──────────────────────────────

def figs7_t2_beginner_advanced():
    fig, ax = plt.subplots(figsize=(8, 5))
    names = [m["name"] for m in ALL_MODELS]
    x = np.arange(len(names))
    w = 0.35

    beg = [m["t2b"] for m in ALL_MODELS]
    adv = [m["t2a"] for m in ALL_MODELS]

    ax.bar(x - w / 2, beg, w, label="Beginner (15 items)", color=OI_CYAN,
           edgecolor="white", linewidth=0.5)
    ax.bar(x + w / 2, adv, w, label="Advanced (15 items)", color=OI_ORANGE,
           edgecolor="white", linewidth=0.5)

    # Random chance line
    ax.axhline(16.7, color=OI_BLACK, linestyle="--", linewidth=1, alpha=0.5,
               label="Random chance (16.7%)")

    ax.set_xticks(x)
    ax.set_xticklabels(names, rotation=30, ha="right")
    ax.set_ylabel("Accuracy (%)")
    ax.set_title("Figure S7: T2 Beginner vs. Advanced Accuracy by Model")
    ax.set_ylim(0, 115)
    ax.legend(loc="upper right", fontsize=8)

    # Vendor separators
    ax.axvline(2.5, color="gray", linestyle=":", linewidth=0.8)
    ax.axvline(4.5, color="gray", linestyle=":", linewidth=0.8)

    sns.despine()
    fig.savefig(os.path.join(FIGURES_DIR, "fig-s7-t2-beginner-advanced.png"))
    plt.close(fig)
    print("  figS7 done")


# ── Figure S8: Year Distribution Histogram ───────────────────────────

def figs8_year_distribution():
    fig, ax = plt.subplots(figsize=(8, 4.5))
    years = sorted(YEAR_DIST.keys())
    counts = [YEAR_DIST[y] for y in years]

    # Color 2024-2026 differently
    colors = [OI_ORANGE if y >= 2024 else OI_CYAN for y in years]

    ax.bar(years, counts, color=colors, edgecolor="white", linewidth=0.5)

    # Percentage annotation for 2024-2026
    total = sum(counts)
    recent = sum(c for y, c in YEAR_DIST.items() if y >= 2024)
    pct = recent / total * 100
    ax.annotate(f"2024-2026: {recent}/{total}\n({pct:.0f}% of corpus)",
                xy=(2025, max(counts) * 0.9), fontsize=10,
                ha="center", fontweight="bold",
                bbox=dict(boxstyle="round,pad=0.3", facecolor=OI_ORANGE, alpha=0.3))

    ax.set_xlabel("Publication Year")
    ax.set_ylabel("Number of Candidates")
    ax.set_title("Figure S8: Temporal Distribution of 401 Benchmark Candidates")
    ax.set_xticks(years)
    ax.set_xticklabels(years, rotation=45, ha="right")
    sns.despine()
    fig.savefig(os.path.join(FIGURES_DIR, "fig-s8-year-distribution.png"))
    plt.close(fig)
    print("  figS8 done")


# ── Main ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("Generating PAPER-V2 figures...")
    print("\nMain body figures:")
    fig10_cross_model_gradient()
    fig11_rubric_heatmap()
    fig12_t2_accuracy()
    fig13_vendor_radar()

    print("\nSupplementary figures:")
    figs2_gate_threshold_sensitivity()
    figs4_tradition_gradient()
    figs5_cross_vendor_length()
    figs6_bias_values_scatter()
    figs7_t2_beginner_advanced()
    figs8_year_distribution()

    print(f"\nAll figures saved to: {FIGURES_DIR}")
    print(f"Total: {len(os.listdir(FIGURES_DIR))} files")
