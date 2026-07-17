"""
WALKWORTHY-CANARY-7f3e2026

make_figures.py — Publication-quality figures for the 2026-07-17 internal briefing report.
Generated OFFLINE from stored analysis artifacts; zero model calls.

Data provenance:
  J1 (Opus referee):  logs/jr-referee-20260716/referee-agreement.json
  J2 (Sol referee):   logs/jr-referee-20260716/referee-agreement-sol.json
  Judge-swap numbers: tools/audit/pilot_judge_swap.py over logs/pilot-20260716/
  Pilot judge-A §3:   20260716-pilot-report.md (transcribed and flagged in fig6)

Run from $V2 root:
  REPORTS/20260717-briefing/figures/.venv/bin/python \\
      REPORTS/20260717-briefing/figures/make_figures.py
  — or —
  .venv/bin/python REPORTS/20260717-briefing/figures/make_figures.py

Outputs: 6 PNGs at 200 dpi, white background, ~16 cm width, same directory.
"""
from __future__ import annotations

import json
import math
import os
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
_HERE = os.path.dirname(os.path.abspath(__file__))
_V2 = os.path.abspath(os.path.join(_HERE, os.pardir, os.pardir, os.pardir, os.pardir))
# $V2 = …/Christian-Ethics-Benchmark-v2
_V2 = os.path.abspath(os.path.join(_HERE, "..", "..", ".."))

J1_PATH = os.path.join(_V2, "logs", "jr-referee-20260716", "referee-agreement.json")
J2_PATH = os.path.join(_V2, "logs", "jr-referee-20260716", "referee-agreement-sol.json")
OUT_DIR = _HERE  # figures/ directory

DPI = 200
FIG_W_IN = 6.3  # ≈16 cm

# ---------------------------------------------------------------------------
# Load data
# ---------------------------------------------------------------------------
with open(J1_PATH, encoding="utf-8") as f:
    J1 = json.load(f)
with open(J2_PATH, encoding="utf-8") as f:
    J2 = json.load(f)

# ---------------------------------------------------------------------------
# Shared style
# ---------------------------------------------------------------------------
COLORS = {
    "opus_A": "#1f77b4",
    "opus_B": "#ff7f0e",
    "sol_A":  "#2ca02c",
    "sol_B":  "#d62728",
    "sol_opus": "#9467bd",
    "A":      "#1f77b4",
    "B":      "#d62728",
    "neither":"#aec7e8",
    "both_A": "#1f77b4",
    "both_B": "#d62728",
    "opus_A_sol_B": "#9467bd",
    "opus_B_sol_A": "#ff7f0e",
    "opus_side_sol_neither": "#8c564b",
    "sol_side_opus_neither":  "#e377c2",
    "both_neither": "#aec7e8",
}

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 9,
    "axes.titlesize": 10,
    "axes.labelsize": 9,
    "xtick.labelsize": 8,
    "ytick.labelsize": 8,
    "figure.facecolor": "white",
    "axes.facecolor": "white",
    "axes.edgecolor": "#333333",
    "grid.alpha": 0.4,
    "grid.linestyle": "--",
})


# ===========================================================================
# FIG 1 — Concordance heatmap
# ===========================================================================
def make_fig1():
    """Heatmap of raw agreement for rater pairs x row strata.
    Rows: 02-control, 02-disagreement, 07-control, 07-disagreement
    Cols: Opus-A, Opus-B, Sol-A, Sol-B, Sol-Opus
    Values from J1.designs_02_07_per_stratum and J2.designs_02_07_sol_vs_ABO_per_stratum
    (disagreement-enriched sample rows only for disagreement strata).
    """
    d02_ctrl_j1  = J1["designs_02_07_per_stratum"]["02"]["control"]["overall"]
    d02_dis_j1   = J1["designs_02_07_per_stratum"]["02"]["disagreement"]["overall"]
    d07_ctrl_j1  = J1["designs_02_07_per_stratum"]["07"]["control"]["overall"]
    d07_dis_j1   = J1["designs_02_07_per_stratum"]["07"]["disagreement"]["overall"]

    d02_ctrl_j2  = J2["designs_02_07_sol_vs_ABO_per_stratum"]["02"]["control"]["overall"]
    d02_dis_j2   = J2["designs_02_07_sol_vs_ABO_per_stratum"]["02"]["disagreement"]["overall"]
    d07_ctrl_j2  = J2["designs_02_07_sol_vs_ABO_per_stratum"]["07"]["control"]["overall"]
    d07_dis_j2   = J2["designs_02_07_sol_vs_ABO_per_stratum"]["07"]["disagreement"]["overall"]

    # Row labels
    row_labels = [
        "d02 control\n(n=80)",
        "d02 disagree\n(n=200)",
        "d07 control\n(n=150)",
        "d07 disagree\n(n=392)",
    ]
    # Col labels: Opus-A, Opus-B, Sol-A, Sol-B, Sol-Opus
    col_labels = ["Opus↔A", "Opus↔B", "Sol↔A", "Sol↔B", "Sol↔Opus"]

    data = np.array([
        # 02 control
        [d02_ctrl_j1["raw_agreement_opus_A"],
         d02_ctrl_j1["raw_agreement_opus_B"],
         d02_ctrl_j2["raw_agreement_sol_A"],
         d02_ctrl_j2["raw_agreement_sol_B"],
         d02_ctrl_j2["raw_agreement_sol_opus"]],
        # 02 disagreement
        [d02_dis_j1["raw_agreement_opus_A"],
         d02_dis_j1["raw_agreement_opus_B"],
         d02_dis_j2["raw_agreement_sol_A"],
         d02_dis_j2["raw_agreement_sol_B"],
         d02_dis_j2["raw_agreement_sol_opus"]],
        # 07 control
        [d07_ctrl_j1["raw_agreement_opus_A"],
         d07_ctrl_j1["raw_agreement_opus_B"],
         d07_ctrl_j2["raw_agreement_sol_A"],
         d07_ctrl_j2["raw_agreement_sol_B"],
         d07_ctrl_j2["raw_agreement_sol_opus"]],
        # 07 disagreement
        [d07_dis_j1["raw_agreement_opus_A"],
         d07_dis_j1["raw_agreement_opus_B"],
         d07_dis_j2["raw_agreement_sol_A"],
         d07_dis_j2["raw_agreement_sol_B"],
         d07_dis_j2["raw_agreement_sol_opus"]],
    ])

    fig, ax = plt.subplots(figsize=(FIG_W_IN, 3.0))
    im = ax.imshow(data, vmin=0.0, vmax=1.0, cmap="RdYlGn", aspect="auto")
    ax.set_xticks(range(5))
    ax.set_xticklabels(col_labels)
    ax.set_yticks(range(4))
    ax.set_yticklabels(row_labels, fontsize=8)
    ax.set_title(
        "Raw agreement — disagreement-enriched sample — per-stratum only\n"
        "(J1=Opus referee; J2=Sol four-way referee; source: referee-agreement[−sol].json)",
        fontsize=9, pad=6
    )

    # Annotate cells
    for r in range(4):
        for c in range(5):
            v = data[r, c]
            col = "white" if (v < 0.35 or v > 0.75) else "black"
            ax.text(c, r, f"{v:.3f}", ha="center", va="center",
                    fontsize=8.5, color=col, fontweight="bold")

    cbar = fig.colorbar(im, ax=ax, fraction=0.04, pad=0.03)
    cbar.set_label("Raw agreement", fontsize=8)
    cbar.ax.tick_params(labelsize=7)

    fig.tight_layout()
    out = os.path.join(OUT_DIR, "fig1-concordance-heatmap.png")
    fig.savefig(out, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"Saved: {out}")


# ===========================================================================
# FIG 2 — Side-with bars
# ===========================================================================
def make_fig2():
    """Stacked side-with bars (A / B / neither) for d02 and d07 disagreement strata.
    Groups: Opus (J1), Sol (J2), plus d07 after-defect-exclusion for each.
    """
    # Opus d02
    opus_02 = J1["disagreement_side_with"]["02"]["overall"]
    # Sol d02
    sol_02  = J2["disagreement_sol_joint"]["02"]["sol_side_with"]["overall"]
    # Opus d07 (before / after exclusion)
    opus_07_before = J1["disagreement_side_with"]["07"]["overall"]
    opus_07_after  = J1["design07_unscorable_sensitivity"]["side_with_after"]
    # Sol d07 (before / after exclusion)
    sol_07_before  = J2["disagreement_sol_joint"]["07"]["sol_side_with"]["overall"]
    sol_07_after   = J2["design07_sol_sensitivity"]["sol_side_with_after_primary"]

    def rates(d):
        return d["sides_with_A_rate"], d["sides_with_B_rate"], d["sides_with_neither_rate"]

    groups = [
        ("Opus\nd02 (n=200)", *rates(opus_02)),
        ("Sol\nd02 (n=200)", *rates(sol_02)),
        ("Opus\nd07 (n=392)", *rates(opus_07_before)),
        ("Opus d07\nex-defect (n=274)", *rates(opus_07_after)),
        ("Sol\nd07 (n=392)", *rates(sol_07_before)),
        ("Sol d07\nex-defect (n=274)", *rates(sol_07_after)),
    ]

    labels   = [g[0] for g in groups]
    rates_A  = [g[1] for g in groups]
    rates_B  = [g[2] for g in groups]
    rates_N  = [g[3] for g in groups]

    x = np.arange(len(labels))
    fig, ax = plt.subplots(figsize=(FIG_W_IN, 3.8))

    b1 = ax.bar(x, rates_A, color=COLORS["A"], label="Sides with A", width=0.6)
    b2 = ax.bar(x, rates_B, bottom=rates_A, color=COLORS["B"], label="Sides with B", width=0.6)
    b3 = ax.bar(x, rates_N, bottom=[a+b for a,b in zip(rates_A,rates_B)],
                color=COLORS["neither"], label="Neither", width=0.6)

    # Annotate segments
    for i, (a, b, n) in enumerate(zip(rates_A, rates_B, rates_N)):
        if a > 0.04: ax.text(i, a/2, f"{a:.2f}", ha="center", va="center", fontsize=7.5, color="white", fontweight="bold")
        if b > 0.04: ax.text(i, a + b/2, f"{b:.2f}", ha="center", va="center", fontsize=7.5, color="white", fontweight="bold")
        if n > 0.04: ax.text(i, a + b + n/2, f"{n:.2f}", ha="center", va="center", fontsize=7.5, color="#333")

    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=8)
    ax.set_ylabel("Proportion")
    ax.set_ylim(0, 1.05)
    ax.set_title(
        "Referee side-with rates — design 02 & 07 disagreement strata\n"
        "(J1=Opus; J2=Sol; ex-defect excludes 5 items with unscorable Opus verdicts)",
        fontsize=9, pad=6
    )
    ax.legend(loc="upper right", fontsize=8, framealpha=0.9)
    ax.yaxis.grid(True, alpha=0.4, linestyle="--")
    ax.set_axisbelow(True)

    fig.tight_layout()
    out = os.path.join(OUT_DIR, "fig2-sidewith-bars.png")
    fig.savefig(out, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"Saved: {out}")


# ===========================================================================
# FIG 3 — Joint referee cells
# ===========================================================================
def make_fig3():
    """7 mutually-exclusive joint referee cells for d02 (n=200) and d07 (n=392).
    Source: J2.disagreement_sol_joint.[02|07].joint_referee_table.cells
    """
    cell_keys = [
        "both_side_A",
        "both_side_B",
        "opus_A_sol_B",
        "opus_B_sol_A",
        "opus_side_sol_neither",
        "sol_side_opus_neither",
        "both_neither",
    ]
    cell_labels = [
        "Both→A",
        "Both→B",
        "Opus→A, Sol→B",
        "Opus→B, Sol→A",
        "Opus sides,\nSol neither",
        "Sol sides,\nOpus neither",
        "Both\nneither",
    ]
    cell_colors = [
        COLORS["both_A"],
        COLORS["both_B"],
        COLORS["opus_A_sol_B"],
        COLORS["opus_B_sol_A"],
        COLORS["opus_side_sol_neither"],
        COLORS["sol_side_opus_neither"],
        COLORS["both_neither"],
    ]

    cells_02 = J2["disagreement_sol_joint"]["02"]["joint_referee_table"]["cells"]
    cells_07 = J2["disagreement_sol_joint"]["07"]["joint_referee_table"]["cells"]
    n_02 = J2["disagreement_sol_joint"]["02"]["joint_referee_table"]["n"]
    n_07 = J2["disagreement_sol_joint"]["07"]["joint_referee_table"]["n"]

    counts_02 = [cells_02[k] for k in cell_keys]
    counts_07 = [cells_07[k] for k in cell_keys]
    pct_02 = [c / n_02 for c in counts_02]
    pct_07 = [c / n_07 for c in counts_07]

    fig, axes = plt.subplots(1, 2, figsize=(FIG_W_IN, 4.2))
    for ax, pct, counts, n, title in [
        (axes[0], pct_02, counts_02, n_02, f"Design 02 (n={n_02})"),
        (axes[1], pct_07, counts_07, n_07, f"Design 07 (n={n_07})"),
    ]:
        y = np.arange(len(cell_labels))
        bars = ax.barh(y, pct, color=cell_colors, edgecolor="white", linewidth=0.5)
        ax.set_yticks(y)
        ax.set_yticklabels(cell_labels, fontsize=8)
        ax.set_xlim(0, max(max(pct_02), max(pct_07)) * 1.25)
        ax.set_xlabel("Proportion", fontsize=8)
        ax.set_title(title, fontsize=9)
        ax.xaxis.grid(True, alpha=0.4, linestyle="--")
        ax.set_axisbelow(True)
        # Annotate with count and pct
        for bar, cnt, p in zip(bars, counts, pct):
            ax.text(p + 0.007, bar.get_y() + bar.get_height() / 2,
                    f"{cnt} ({p:.1%})", va="center", fontsize=7.5)

    fig.suptitle(
        "Joint referee cell distribution — d02 & d07 disagreement strata\n"
        "(7 mutually exclusive cells; source: J2 disagreement_sol_joint.joint_referee_table)",
        fontsize=9, y=1.01
    )
    fig.tight_layout()
    out = os.path.join(OUT_DIR, "fig3-joint-referee-cells.png")
    fig.savefig(out, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"Saved: {out}")


# ===========================================================================
# FIG 4 — Design-06 category deltas
# ===========================================================================
def make_fig4():
    """Per-category mean deltas for 7 categories x 5 comparison pairs x 2 strata.
    Pairs: Opus-A, Opus-B (J1); Sol-A, Sol-B, Sol-Opus (J2).
    Strata: control, gap.
    Makes the `principles` Opus outlier visually obvious.
    """
    cats = ["frame", "facts", "principles", "alternatives", "resolution", "remainder", "pastoral"]

    # J1 data
    j1_ctrl_oA = J1["design06_per_stratum"]["control"]["per_category_mean_delta_opus_minus_A"]
    j1_ctrl_oB = J1["design06_per_stratum"]["control"]["per_category_mean_delta_opus_minus_B"]
    j1_gap_oA  = J1["design06_per_stratum"]["gap"]["per_category_mean_delta_opus_minus_A"]
    j1_gap_oB  = J1["design06_per_stratum"]["gap"]["per_category_mean_delta_opus_minus_B"]

    # J2 data
    j2_ctrl_sA    = J2["design06_sol_per_stratum"]["control"]["per_category_mean_delta_sol_minus_A"]
    j2_ctrl_sB    = J2["design06_sol_per_stratum"]["control"]["per_category_mean_delta_sol_minus_B"]
    j2_ctrl_sOpus = J2["design06_sol_per_stratum"]["control"]["per_category_mean_delta_sol_minus_opus"]
    j2_gap_sA     = J2["design06_sol_per_stratum"]["gap"]["per_category_mean_delta_sol_minus_A"]
    j2_gap_sB     = J2["design06_sol_per_stratum"]["gap"]["per_category_mean_delta_sol_minus_B"]
    j2_gap_sOpus  = J2["design06_sol_per_stratum"]["gap"]["per_category_mean_delta_sol_minus_opus"]

    def vals(src):
        return [src[c]["mean_delta"] for c in cats]

    series = {
        "Opus−A": (vals(j1_ctrl_oA), vals(j1_gap_oA),   COLORS["opus_A"], "o", "-"),
        "Opus−B": (vals(j1_ctrl_oB), vals(j1_gap_oB),   COLORS["opus_B"], "s", "-"),
        "Sol−A":  (vals(j2_ctrl_sA), vals(j2_gap_sA),   COLORS["sol_A"],  "^", "--"),
        "Sol−B":  (vals(j2_ctrl_sB), vals(j2_gap_sB),   COLORS["sol_B"],  "D", "--"),
        "Sol−Opus":(vals(j2_ctrl_sOpus),vals(j2_gap_sOpus),COLORS["sol_opus"],"v","-."),
    }

    x = np.arange(len(cats))
    fig, axes = plt.subplots(1, 2, figsize=(FIG_W_IN * 1.5, 4.0), sharey=False)
    titles = ["Control stratum (n=60)", "Gap stratum (n=60)"]

    for col, (ax, title, stratum_idx) in enumerate(zip(axes, titles, [0, 1])):
        for lbl, (ctrl_v, gap_v, color, marker, ls) in series.items():
            v = ctrl_v if stratum_idx == 0 else gap_v
            ax.plot(x, v, marker=marker, color=color, linestyle=ls, label=lbl,
                    linewidth=1.4, markersize=5)
        ax.axhline(0, color="black", linewidth=0.8, linestyle=":")
        ax.set_xticks(x)
        ax.set_xticklabels(cats, rotation=35, ha="right", fontsize=8)
        ax.set_ylabel("Mean delta (referee − judge)")
        ax.set_title(title, fontsize=9)
        ax.yaxis.grid(True, alpha=0.4, linestyle="--")
        ax.set_axisbelow(True)
        # Mark principles with a vertical band
        ax.axvspan(1.5, 2.5, alpha=0.08, color="red", label="_nolegend_")
        ax.text(2, ax.get_ylim()[1] * 0.95 if col == 0 else -0.45,
                "principles\noutlier", ha="center", va="top",
                fontsize=7, color="red", fontstyle="italic")

    handles, lbls = axes[0].get_legend_handles_labels()
    fig.legend(handles, lbls, loc="upper center", ncol=5, fontsize=8,
               bbox_to_anchor=(0.5, 1.02), framealpha=0.9)
    fig.suptitle(
        "Design-06 per-category mean deltas — 5 referee−judge pairs, 2 strata\n"
        "(source: J1 design06_per_stratum; J2 design06_sol_per_stratum; n=60 each cell)",
        fontsize=9, y=1.06
    )
    fig.tight_layout()
    out = os.path.join(OUT_DIR, "fig4-design06-category-deltas.png")
    fig.savefig(out, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"Saved: {out}")


# ===========================================================================
# FIG 5 — Defect items unscorable counts
# ===========================================================================
def make_fig5():
    """Unscorable counts by item x referee (Opus J1, Sol J2), with overlap-48 annotation.
    Items: WW-07-L02, WW-07-I04, WW-07-F02, WW-07-A02, WW-07-D03
    Source: J1.opus_unscorable_audit, J2.sol_unscorable_audit
    """
    item_keys = ["WW-07-L02", "WW-07-I04", "WW-07-F02", "WW-07-A02", "WW-07-D03"]

    j1_audit = J1["opus_unscorable_audit"]["by_item_id"]
    j2_audit = J2["sol_unscorable_audit"]["by_item_id"]

    # Opus counts: all 5 items present
    opus_counts = []
    for ik in item_keys:
        if ik in j1_audit:
            opus_counts.append(j1_audit[ik]["n"])
        else:
            opus_counts.append(0)

    # Sol counts: only 3 named defect items (WW-07-F02, WW-07-I04, WW-07-L02); A02/D03 = 0
    sol_counts = []
    for ik in item_keys:
        if ik in j2_audit:
            sol_counts.append(j2_audit[ik]["n"])
        else:
            sol_counts.append(0)

    x = np.arange(len(item_keys))
    w = 0.35
    fig, ax = plt.subplots(figsize=(FIG_W_IN, 3.5))

    b1 = ax.bar(x - w/2, opus_counts, width=w, color=COLORS["opus_A"], label="Opus referee")
    b2 = ax.bar(x + w/2, sol_counts,  width=w, color=COLORS["sol_A"],  label="Sol referee")

    # Annotate counts
    for bar, cnt in zip(b1, opus_counts):
        if cnt > 0:
            ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3,
                    str(cnt), ha="center", va="bottom", fontsize=8.5, fontweight="bold")
    for bar, cnt in zip(b2, sol_counts):
        if cnt > 0:
            ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3,
                    str(cnt), ha="center", va="bottom", fontsize=8.5, fontweight="bold")

    # Totals annotation
    opus_total = J1["opus_unscorable_audit"]["n_opus_unscorable_units"]
    sol_total  = J2["sol_unscorable_audit"]["n_sol_unscorable_units"]
    overlap    = J2["sol_unscorable_audit"]["opus_and_sol_unscorable_overlap"]

    ax.set_xticks(x)
    ax.set_xticklabels(item_keys, fontsize=8, rotation=15, ha="right")
    ax.set_ylabel("Unscorable count")
    ax.set_title(
        "Design-07 unscorable counts by item and referee\n"
        "(source: J1 opus_unscorable_audit; J2 sol_unscorable_audit)",
        fontsize=9, pad=6
    )
    ax.legend(fontsize=8, loc="upper right")
    ax.yaxis.grid(True, alpha=0.4, linestyle="--")
    ax.set_axisbelow(True)

    # Overlap annotation box
    info = (
        f"Opus total unscorable: {opus_total}\n"
        f"Sol total unscorable:  {sol_total}\n"
        f"Opus∩Sol overlap: {overlap}"
    )
    ax.text(0.03, 0.97, info, transform=ax.transAxes, va="top", ha="left",
            fontsize=8, bbox=dict(boxstyle="round,pad=0.4", fc="lightyellow", ec="#999", alpha=0.9))

    # Note on (no keyed text) items
    ax.text(0.5, -0.22,
            "WW-07-L02 / I04 / F02 ship '(no keyed text)' rubric anchors — unscorables expected here.",
            transform=ax.transAxes, ha="center", va="top", fontsize=7.5, color="#555",
            fontstyle="italic")

    fig.tight_layout()
    out = os.path.join(OUT_DIR, "fig5-defect-items.png")
    fig.savefig(out, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"Saved: {out}")


# ===========================================================================
# FIG 6 — Pilot judge-swap dumbbell
# ===========================================================================
def make_fig6():
    """Per-design headline metric under judge-A vs judge-B per SUT.
    Compact 2x5 grid of dumbbell plots (connected A-B dots per SUT).
    Judge-A values from pilot_judge_swap.py (recompute from stored logs).
    Judge-B values from pilot_judge_swap.py (recompute from judgeB-verdicts.jsonl).
    Design 05 csr_mean is NaN from log-header path; recovered judge-A values from
    pilot-report §3 (HAND-TRANSCRIBED — flagged). No judge-B csr_mean available
    (CSR is judge-free; rationale_honesty only for judge-B).
    A/B agreement ranges from pilot-report §2 (HAND-TRANSCRIBED — flagged).
    Title includes required R4 disclaimer.
    """
    # All values sourced from tools/audit/pilot_judge_swap.py output (run 2026-07-17).
    # Design 05: judge-A recovered from pilot-report §3 recompute (hand-transcribed, flagged).
    # A/B agreement range strings from pilot-report §2 (hand-transcribed, flagged).

    SUTS_SHORT = {
        "deepseek-chat": "ds",
        "gemini-flash-lite": "gem",
        "gpt-4.1-mini": "gpt",
        "llama-3.3-70b": "llama",
        "mistral-small": "mist",
    }
    SUTS = list(SUTS_SHORT.keys())
    SUTS_DISP = [SUTS_SHORT[s] for s in SUTS]

    designs_data = {
        # (headline_label, {sut: (judgeA, judgeB)}, agree_range_str, note)
        "01\nfull_obedience_rate": {
            "A": {"deepseek-chat": 0.6818, "gemini-flash-lite": 0.6818,
                  "gpt-4.1-mini": 0.6591, "llama-3.3-70b": 0.5455, "mistral-small": 0.4773},
            "B": {"deepseek-chat": 0.5714, "gemini-flash-lite": 0.4318,
                  "gpt-4.1-mini": 0.4146, "llama-3.3-70b": 0.6136, "mistral-small": 0.5682},
            "agree": "0.55–0.69",
        },
        "02\nbreak_rate": {
            "A": {"deepseek-chat": 0.5571, "gemini-flash-lite": 0.5857,
                  "gpt-4.1-mini": 0.5882, "llama-3.3-70b": 0.6029, "mistral-small": 0.5441},
            "B": {"deepseek-chat": 0.7391, "gemini-flash-lite": 0.8030,
                  "gpt-4.1-mini": 0.7000, "llama-3.3-70b": 0.5286, "mistral-small": 0.8182},
            "agree": "0.21–0.26 (per-turn)",
        },
        "03\nsay_do_gap": {
            "A": {"deepseek-chat": 0.4828, "gemini-flash-lite": 0.5862,
                  "gpt-4.1-mini": 0.3214, "llama-3.3-70b": 0.5172, "mistral-small": 0.2857},
            "B": {"deepseek-chat": -0.0385, "gemini-flash-lite": -0.0909,
                  "gpt-4.1-mini": -0.0417, "llama-3.3-70b": -0.1481, "mistral-small": -0.0690},
            "agree": "0.43–0.50",
        },
        "04\nmotive_delta": {
            "A": {"deepseek-chat": 0.1759, "gemini-flash-lite": 0.1806,
                  "gpt-4.1-mini": 0.1713, "llama-3.3-70b": 0.2917, "mistral-small": 0.2407},
            "B": {"deepseek-chat": 0.1414, "gemini-flash-lite": 0.1401,
                  "gpt-4.1-mini": 0.0404, "llama-3.3-70b": 0.1932, "mistral-small": 0.0455},
            "agree": "0.60–0.70",
        },
        # Design 05: judge-A from pilot-report §3 recompute (hand-transcribed)
        # Judge-B not available (CSR judge-free; rationale_honesty only)
        "05\ncsr_mean\n[judgeA only*]": {
            "A": {"deepseek-chat": 0.9028, "gemini-flash-lite": 0.9226,
                  "gpt-4.1-mini": 0.8869, "llama-3.3-70b": 0.8436, "mistral-small": 0.9444},
            "B": None,  # not available
            "agree": "0.67–0.87 (ratio_honesty)",
        },
        "06\nprofile_mean": {
            "A": {"deepseek-chat": 0.8254, "gemini-flash-lite": 0.9418,
                  "gpt-4.1-mini": 0.8466, "llama-3.3-70b": 0.5847, "mistral-small": 0.4709},
            "B": {"deepseek-chat": 0.9524, "gemini-flash-lite": 0.9643,
                  "gpt-4.1-mini": 0.9193, "llama-3.3-70b": 0.7886, "mistral-small": 0.7253},
            "agree": "0.43–0.83",
        },
        "07\narc_pass_rate": {
            "A": {"deepseek-chat": 0.0000, "gemini-flash-lite": 0.0000,
                  "gpt-4.1-mini": 0.0000, "llama-3.3-70b": 0.0000, "mistral-small": 0.0000},
            "B": {"deepseek-chat": 0.0000, "gemini-flash-lite": 0.0400,
                  "gpt-4.1-mini": 0.0000, "llama-3.3-70b": 0.0417, "mistral-small": 0.0000},
            "agree": "0.48–0.56 (per-turn)",
        },
        "08\ncovert_overt_gap": {
            "A": {"deepseek-chat": 0.0172, "gemini-flash-lite": 0.1111,
                  "gpt-4.1-mini": 0.1207, "llama-3.3-70b": 0.1897, "mistral-small": 0.2500},
            "B": {"deepseek-chat": 0.2308, "gemini-flash-lite": 0.2241,
                  "gpt-4.1-mini": 0.4000, "llama-3.3-70b": 0.2679, "mistral-small": 0.2115},
            "agree": "0.59–0.73",
        },
        "09\nsymmetry_index": {
            "A": {"deepseek-chat": 0.8088, "gemini-flash-lite": 0.7941,
                  "gpt-4.1-mini": 0.7353, "llama-3.3-70b": 0.8676, "mistral-small": 0.8235},
            "B": {"deepseek-chat": 0.8500, "gemini-flash-lite": 0.7333,
                  "gpt-4.1-mini": 0.9516, "llama-3.3-70b": 0.8281, "mistral-small": 0.8333},
            "agree": "0.36–0.51",
        },
        "10\nmercy_delta": {
            "A": {"deepseek-chat": -0.0156, "gemini-flash-lite":  0.0156,
                  "gpt-4.1-mini": -0.0781, "llama-3.3-70b":  0.0469, "mistral-small":  0.0625},
            "B": {"deepseek-chat":  0.0517, "gemini-flash-lite": -0.0156,
                  "gpt-4.1-mini":  0.0323, "llama-3.3-70b":  0.0323, "mistral-small": -0.0333},
            "agree": "0.68–0.83",
        },
    }

    design_labels = list(designs_data.keys())
    n_designs = len(design_labels)
    n_cols = 5
    n_rows = 2

    fig, axes = plt.subplots(n_rows, n_cols, figsize=(FIG_W_IN * 1.6, 5.5))
    axes_flat = axes.flatten()

    sut_colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd"]

    for ax_idx, (label, dd) in enumerate(designs_data.items()):
        ax = axes_flat[ax_idx]
        A_vals = dd["A"]
        B_vals = dd["B"]
        agree  = dd["agree"]

        y_pos = np.arange(len(SUTS))

        for si, (sut, short) in enumerate(SUTS_SHORT.items()):
            a_v = A_vals.get(sut)
            b_v = B_vals.get(sut) if B_vals is not None else None

            if a_v is not None and b_v is not None:
                ax.plot([a_v, b_v], [si, si], color=sut_colors[si], linewidth=1.2, alpha=0.7)
                ax.plot(a_v, si, "o", color=sut_colors[si], markersize=6, label=f"A:{short}" if ax_idx == 0 else "_")
                ax.plot(b_v, si, "s", color=sut_colors[si], markersize=6, label=f"B:{short}" if ax_idx == 0 else "_")
            elif a_v is not None:
                ax.plot(a_v, si, "o", color=sut_colors[si], markersize=6)
            elif b_v is not None:
                ax.plot(b_v, si, "s", color=sut_colors[si], markersize=6)

        ax.set_yticks(y_pos)
        ax.set_yticklabels([SUTS_SHORT[s] for s in SUTS], fontsize=7)
        ax.tick_params(axis="x", labelsize=7)
        ax.set_title(label, fontsize=7.5, pad=3)
        ax.axvline(0, color="gray", linewidth=0.5, linestyle=":")
        ax.xaxis.grid(True, alpha=0.3, linestyle="--")
        ax.set_axisbelow(True)
        # Agree range annotation
        ax.text(0.98, 0.02, f"A/B agree:\n{agree}", transform=ax.transAxes,
                ha="right", va="bottom", fontsize=6.0, color="#555",
                bbox=dict(boxstyle="round,pad=0.2", fc="lightyellow", ec="#bbb", alpha=0.8))

    # Legend: circle = judge-A, square = judge-B
    h_A = mpatches.Patch(color="gray", label="Judge-A (circle)")
    h_B = mpatches.Patch(facecolor="none", edgecolor="gray", label="Judge-B (square)")
    leg_A = plt.Line2D([0],[0], marker="o", color="w", markerfacecolor="gray", markersize=7, label="Judge-A")
    leg_B = plt.Line2D([0],[0], marker="s", color="w", markerfacecolor="gray", markersize=7, label="Judge-B")

    fig.legend(handles=[leg_A, leg_B], loc="upper center", ncol=2, fontsize=8,
               bbox_to_anchor=(0.5, 1.01))

    fig.suptitle(
        "no SUT-vs-SUT ordering claims (R4)\n"
        "Per-design headline: judge-A vs judge-B across 5 SUTs\n"
        "* d05 judge-A = recovered csr_mean (pilot-report §3, HAND-TRANSCRIBED); "
        "d05 judge-B unavailable (CSR judge-free)\n"
        "All A/B agree ranges from pilot-report §2 (HAND-TRANSCRIBED)",
        fontsize=8, y=1.07
    )

    fig.tight_layout()
    out = os.path.join(OUT_DIR, "fig6-pilot-judge-swap.png")
    fig.savefig(out, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"Saved: {out}")


# ===========================================================================
# Main
# ===========================================================================
if __name__ == "__main__":
    print(f"V2 root resolved to: {_V2}")
    print(f"J1 path: {J1_PATH}")
    print(f"J2 path: {J2_PATH}")
    print(f"Output dir: {OUT_DIR}")
    print()
    make_fig1()
    make_fig2()
    make_fig3()
    make_fig4()
    make_fig5()
    make_fig6()
    print("\nAll figures complete.")
