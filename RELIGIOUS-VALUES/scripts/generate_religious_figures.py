#!/usr/bin/env python3
"""Generate 4 publication-quality figures for the Religious Values Benchmark paper.

Reads from:
  - data/20260403-religious-benchmark-candidates.json
  - data/20260403-religious-benchmark-feature-matrix.json
  - data/20260403-religious-values-top15.json

Outputs to:
  - PAPER/figures/fig1-tradition-heatmap.png
  - PAPER/figures/fig2-tradition-distribution.png
  - PAPER/figures/fig3-rd-vs-pe-scatter.png
  - PAPER/figures/fig4-data-availability.png
"""
from __future__ import annotations

import json
import math
from collections import Counter
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np
import seaborn as sns

# ------------------------------------------------------------------
# Paths
# ------------------------------------------------------------------
BASE = Path(__file__).resolve().parent.parent
DATA = BASE / "data"
FIGURES = BASE / "PAPER" / "figures"
FIGURES.mkdir(parents=True, exist_ok=True)

CANDIDATES_FILE = DATA / "20260403-religious-benchmark-candidates.json"
FEATURE_FILE = DATA / "20260403-religious-benchmark-feature-matrix.json"
TOP15_FILE = DATA / "20260403-religious-values-top15.json"

# ------------------------------------------------------------------
# Style
# ------------------------------------------------------------------
plt.rcParams.update({
    "font.family": "serif",
    "font.size": 10,
    "axes.titlesize": 12,
    "axes.labelsize": 11,
    "xtick.labelsize": 9,
    "ytick.labelsize": 9,
    "figure.dpi": 300,
    "savefig.dpi": 300,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.15,
})

# ------------------------------------------------------------------
# Load data
# ------------------------------------------------------------------
with open(CANDIDATES_FILE) as f:
    candidates_data = json.load(f)

with open(FEATURE_FILE) as f:
    feature_data = json.load(f)

with open(TOP15_FILE) as f:
    top15_data = json.load(f)

entries = feature_data["entries"]
top15_keys = {e["key"] for e in top15_data["top15"]}

# 14 traditions (paper mentions 14 including Baha'i)
ALL_TRADITIONS = [
    "Christianity", "Islam", "Jainism", "Hinduism", "Buddhism",
    "Judaism", "Indigenous Spirituality", "Confucianism", "Sikhism",
    "Ubuntu Philosophy", "Taoism", "Zoroastrianism", "Shinto", "Baha'i"
]

TRADITION_FAMILIES = {
    "Christianity": "Abrahamic",
    "Islam": "Abrahamic",
    "Judaism": "Abrahamic",
    "Hinduism": "Dharmic",
    "Buddhism": "Dharmic",
    "Jainism": "Dharmic",
    "Sikhism": "Dharmic",
    "Confucianism": "East Asian",
    "Taoism": "East Asian",
    "Shinto": "East Asian",
    "Ubuntu Philosophy": "African/Indigenous",
    "Indigenous Spirituality": "African/Indigenous",
    "Baha'i": "Other",
    "Zoroastrianism": "Other",
}

FAMILY_COLORS = {
    "Abrahamic": "#2166AC",
    "Dharmic": "#1B7837",
    "East Asian": "#E08214",
    "African/Indigenous": "#B2182B",
    "Other": "#878787",
}

FAMILY_ORDER = ["Abrahamic", "Dharmic", "East Asian", "African/Indigenous", "Other"]

# ------------------------------------------------------------------
# Compute per-tradition statistics
# ------------------------------------------------------------------
total_by_t = Counter()
gate_by_t = Counter()
top15_by_t = Counter()
p3_avail_by_t = Counter()
p3_unavail_by_t = Counter()

AVAILABLE_VALUES = {"GitHub", "HuggingFace", "Website", "GitLab", "Archive", "Kaggle"}

for e in entries:
    t = e.get("D5_primary_tradition", "Unknown")
    if t == "Unknown":
        continue
    total_by_t[t] += 1
    if e.get("passes_gates"):
        gate_by_t[t] += 1
    if e["key"] in top15_keys:
        top15_by_t[t] += 1
    p3 = e.get("P3_data_availability", "Not available")
    if p3 in AVAILABLE_VALUES:
        p3_avail_by_t[t] += 1
    else:
        p3_unavail_by_t[t] += 1

# Ensure all 14 traditions present
for t in ALL_TRADITIONS:
    total_by_t.setdefault(t, 0)
    gate_by_t.setdefault(t, 0)
    top15_by_t.setdefault(t, 0)
    p3_avail_by_t.setdefault(t, 0)
    p3_unavail_by_t.setdefault(t, 0)


# ==================================================================
# Figure 1: Tradition Heatmap (14 traditions x 3 columns)
# ==================================================================
def fig1_heatmap():
    # Sort by gate-passer count descending, then total descending
    sorted_traditions = sorted(
        ALL_TRADITIONS,
        key=lambda t: (gate_by_t[t], total_by_t[t]),
        reverse=True,
    )

    matrix = np.array([
        [total_by_t[t], gate_by_t[t], top15_by_t[t]]
        for t in sorted_traditions
    ], dtype=float)

    fig, ax = plt.subplots(figsize=(4.5, 6))
    sns.heatmap(
        matrix,
        annot=True,
        fmt=".0f",
        cmap="YlOrRd",
        linewidths=0.8,
        linecolor="white",
        xticklabels=["Total\nCandidates", "Gate-\nPassers", "Top 15"],
        yticklabels=sorted_traditions,
        cbar_kws={"label": "Count", "shrink": 0.6},
        ax=ax,
        vmin=0,
    )
    ax.set_title("Figure 1: Tradition Coverage\n401 Candidates \u00d7 14 Traditions", fontweight="bold", pad=12)
    ax.tick_params(axis="x", rotation=0)
    ax.tick_params(axis="y", rotation=0)

    # Add a divider line between traditions with gate-passers and those without
    n_with_gate = sum(1 for t in sorted_traditions if gate_by_t[t] > 0)
    ax.axhline(y=n_with_gate, color="black", linewidth=2, linestyle="--")
    ax.text(
        3.05, n_with_gate + 0.1, "8-tradition void",
        fontsize=8, fontstyle="italic", va="top", ha="left",
    )

    fig.savefig(FIGURES / "fig1-tradition-heatmap.png")
    plt.close(fig)
    print(f"  Saved fig1-tradition-heatmap.png")


# ==================================================================
# Figure 2: Grouped bar chart by tradition family
# ==================================================================
def fig2_distribution():
    # Order traditions by family, then by total descending within family
    ordered = []
    for fam in FAMILY_ORDER:
        fam_ts = [t for t in ALL_TRADITIONS if TRADITION_FAMILIES[t] == fam]
        fam_ts.sort(key=lambda t: total_by_t[t], reverse=True)
        ordered.extend(fam_ts)

    totals = [total_by_t[t] for t in ordered]
    gates = [gate_by_t[t] for t in ordered]
    families = [TRADITION_FAMILIES[t] for t in ordered]

    fig, ax = plt.subplots(figsize=(6.5, 5))

    x = np.arange(len(ordered))
    width = 0.38

    # Light bars for total, dark bars for gate-passers
    light_colors = []
    dark_colors = []
    for t in ordered:
        fam = TRADITION_FAMILIES[t]
        base = FAMILY_COLORS[fam]
        light_colors.append(base + "55")  # alpha ~33%
        dark_colors.append(base)

    bars1 = ax.bar(x - width / 2, totals, width, color=light_colors, edgecolor="gray",
                   linewidth=0.5, label="Total candidates")
    bars2 = ax.bar(x + width / 2, gates, width, color=dark_colors, edgecolor="gray",
                   linewidth=0.5, label="Gate-passers")

    # Family separators
    cum = 0
    for fam in FAMILY_ORDER:
        n = sum(1 for t in ordered if TRADITION_FAMILIES[t] == fam)
        if cum > 0:
            ax.axvline(x=cum - 0.5, color="gray", linewidth=0.8, linestyle=":")
        # Family label
        mid = cum + n / 2 - 0.5
        # Shorten labels to avoid overlap
        label = {"African/Indigenous": "Afr./Indig."}.get(fam, fam)
        ax.text(mid, max(totals) * 1.06, label, ha="center", va="bottom",
                fontsize=7.5, fontstyle="italic", color="#555555")
        cum += n

    ax.set_xticks(x)
    ax.set_xticklabels(ordered, rotation=55, ha="right", fontsize=8)
    ax.set_ylabel("Number of benchmarks")
    ax.set_title("Figure 2: Candidate Distribution by Tradition Family", fontweight="bold", pad=18)
    ax.legend(loc="upper right", fontsize=8)

    # Gate-passing rate annotation
    overall_rate = sum(gates) / sum(totals) * 100
    ax.axhline(y=0, color="black", linewidth=0.5)
    ax.text(
        0.98, 0.85,
        f"Overall gate-passing rate: {overall_rate:.1f}%\n(46 of 401 candidates)",
        transform=ax.transAxes, ha="right", va="top",
        fontsize=8, bbox=dict(boxstyle="round,pad=0.3", facecolor="lightyellow", alpha=0.8),
    )

    ax.set_ylim(0, max(totals) * 1.18)
    fig.savefig(FIGURES / "fig2-tradition-distribution.png")
    plt.close(fig)
    print(f"  Saved fig2-tradition-distribution.png")


# ==================================================================
# Figure 3: RD vs PE scatter plot
# ==================================================================
def fig3_scatter():
    fig, ax = plt.subplots(figsize=(6.5, 5))

    for e in entries:
        t = e.get("D5_primary_tradition", "Unknown")
        fam = e.get("D6_tradition_family", TRADITION_FAMILIES.get(t, "Other"))
        if fam not in FAMILY_COLORS:
            fam = "Other"
        rd = e.get("RD_score", 0) or 0
        pe = e.get("PE_score", 0) or 0
        cc = e.get("C1_citation_count", 0) or 0
        size = max(15, math.log(cc + 1) * 20 + 15)
        is_top15 = e["key"] in top15_keys

        ax.scatter(
            rd, pe,
            s=size,
            c=FAMILY_COLORS[fam],
            alpha=0.5 if not is_top15 else 0.9,
            edgecolors="black" if is_top15 else "none",
            linewidths=1.5 if is_top15 else 0,
            zorder=10 if is_top15 else 5,
        )

    # Reference lines
    ax.axvline(x=30, color="red", linewidth=1, linestyle="--", alpha=0.6)
    ax.text(31, 2, "RD \u2265 30 gate", fontsize=7, color="red", alpha=0.7)

    # Legend for families
    for fam in FAMILY_ORDER:
        ax.scatter([], [], c=FAMILY_COLORS[fam], s=40, label=fam)
    ax.scatter([], [], c="white", edgecolors="black", linewidths=1.5, s=50, label="Top 15")

    ax.legend(loc="lower right", fontsize=7.5, framealpha=0.9)
    ax.set_xlabel("Religious/Theological Depth (RD)")
    ax.set_ylabel("Practical Ease (PE)")
    ax.set_title("Figure 3: RD vs. PE for 401 Candidates", fontweight="bold")
    ax.set_xlim(-2, 105)
    ax.set_ylim(-2, 105)

    fig.savefig(FIGURES / "fig3-rd-vs-pe-scatter.png")
    plt.close(fig)
    print(f"  Saved fig3-rd-vs-pe-scatter.png")


# ==================================================================
# Figure 4: Data availability stacked horizontal bars
# ==================================================================
def fig4_data_availability():
    # Sort by total descending
    sorted_traditions = sorted(
        ALL_TRADITIONS,
        key=lambda t: total_by_t[t],
        reverse=True,
    )
    # Remove traditions with 0 total for cleaner chart
    sorted_traditions = [t for t in sorted_traditions if total_by_t[t] > 0]

    avail = [p3_avail_by_t[t] for t in sorted_traditions]
    unavail = [p3_unavail_by_t[t] for t in sorted_traditions]

    fig, ax = plt.subplots(figsize=(6.5, 5))
    y = np.arange(len(sorted_traditions))

    bars_avail = ax.barh(y, avail, color="#2CA02C", edgecolor="white", linewidth=0.5, label="Available")
    bars_unavail = ax.barh(y, unavail, left=avail, color="#D62728", edgecolor="white",
                           linewidth=0.5, label="Unavailable")

    # Count labels
    for i, (a, u) in enumerate(zip(avail, unavail)):
        if a > 0:
            ax.text(a / 2, i, str(a), ha="center", va="center", fontsize=8,
                    fontweight="bold", color="white")
        if u > 0:
            ax.text(a + u / 2, i, str(u), ha="center", va="center", fontsize=8,
                    fontweight="bold", color="white")

    ax.set_yticks(y)
    ax.set_yticklabels(sorted_traditions)
    ax.invert_yaxis()
    ax.set_xlabel("Number of candidates")
    ax.set_title("Figure 4: Data Availability by Tradition", fontweight="bold")
    ax.legend(loc="lower right", fontsize=8)

    # Summary annotation
    total_avail = sum(avail)
    total_all = sum(avail) + sum(unavail)
    pct = total_avail / total_all * 100
    ax.text(
        0.98, 0.02,
        f"Available: {total_avail} of {total_all} ({pct:.0f}%)",
        transform=ax.transAxes, ha="right", va="bottom",
        fontsize=8, bbox=dict(boxstyle="round,pad=0.3", facecolor="lightyellow", alpha=0.8),
    )

    fig.savefig(FIGURES / "fig4-data-availability.png")
    plt.close(fig)
    print(f"  Saved fig4-data-availability.png")


# ------------------------------------------------------------------
# Main
# ------------------------------------------------------------------
if __name__ == "__main__":
    print("Generating Religious Values Benchmark figures...")
    fig1_heatmap()
    fig2_distribution()
    fig3_scatter()
    fig4_data_availability()
    print("Done. Figures saved to:", FIGURES)
