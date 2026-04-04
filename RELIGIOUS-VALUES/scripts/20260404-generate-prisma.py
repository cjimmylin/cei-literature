#!/usr/bin/env python3
"""Generate PRISMA-style flow diagram for the Religious Values Benchmark Paper."""
from __future__ import annotations

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from pathlib import Path

# ---------- configuration ----------
OUT = Path(__file__).resolve().parent.parent / "PAPER" / "fig-prisma-flow.png"
FIG_W, FIG_H = 8, 10
DPI = 300

# colours — muted academic palette
BOX_FILL   = "#dce6f1"   # light steel blue
BOX_EDGE   = "#4472c4"   # mid blue
ARROW_CLR  = "#4472c4"
SIDE_FILL  = "#f2f2f2"   # light gray
SIDE_EDGE  = "#999999"
TIER_FILLS = ["#d6e9d6", "#fff2cc", "#f2dcdb"]  # green, amber, rose (muted)
TIER_EDGES = ["#548235", "#bf8f00", "#c0504d"]
TEXT_CLR   = "#1f1f1f"

# ---------- helpers ----------
def rounded_box(ax, cx, cy, w, h, text, fill=BOX_FILL, edge=BOX_EDGE, fontsize=11, bold_number=True, zorder=3):
    """Draw a rounded rectangle centred at (cx, cy) with wrapped text."""
    rect = mpatches.FancyBboxPatch(
        (cx - w / 2, cy - h / 2), w, h,
        boxstyle="round,pad=0.015", facecolor=fill, edgecolor=edge,
        linewidth=1.4, zorder=zorder,
    )
    ax.add_patch(rect)
    ax.text(cx, cy, text, ha="center", va="center", fontsize=fontsize,
            color=TEXT_CLR, fontweight="bold" if bold_number else "normal",
            zorder=zorder + 1, linespacing=1.35)

def arrow(ax, x0, y0, x1, y1, color=ARROW_CLR):
    ax.annotate("", xy=(x1, y1), xytext=(x0, y0),
                arrowprops=dict(arrowstyle="-|>", color=color, lw=1.6),
                zorder=2)

def side_annotation(ax, x_anchor, y_anchor, x_box, y_box, w, h, text, fontsize=9):
    """Bracket arrow to a side note box."""
    rect = mpatches.FancyBboxPatch(
        (x_box - w / 2, y_box - h / 2), w, h,
        boxstyle="round,pad=0.012", facecolor=SIDE_FILL, edgecolor=SIDE_EDGE,
        linewidth=1.0, zorder=3,
    )
    ax.add_patch(rect)
    ax.text(x_box, y_box, text, ha="center", va="center", fontsize=fontsize,
            color="#444444", zorder=4, linespacing=1.3)
    ax.annotate("", xy=(x_box - w / 2, y_box), xytext=(x_anchor, y_anchor),
                arrowprops=dict(arrowstyle="-|>", color=SIDE_EDGE, lw=1.0,
                                connectionstyle="arc3,rad=0.0"),
                zorder=2)

# ---------- build figure ----------
fig, ax = plt.subplots(figsize=(FIG_W, FIG_H))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis("off")
fig.patch.set_facecolor("white")

# vertical positions (top to bottom)
y_positions = [0.92, 0.76, 0.60, 0.44, 0.26]
cx = 0.42  # centre of main column (shifted left to make room for side notes)
bw = 0.38  # box width
bh = 0.065 # box height

# --- Box 1: Identification ---
rounded_box(ax, cx, y_positions[0], bw, bh,
            "2,099 vault papers screened", fontsize=12)

# --- Box 2: Candidates ---
rounded_box(ax, cx, y_positions[1], bw, bh,
            "401 benchmark candidates\nidentified", fontsize=11)

# arrow 1->2
arrow(ax, cx, y_positions[0] - bh / 2, cx, y_positions[1] + bh / 2)

# --- Box 3: Hard gates ---
rounded_box(ax, cx, y_positions[2], bw, bh,
            "47 pass both hard gates", fontsize=11)

# arrow 2->3
arrow(ax, cx, y_positions[1] - bh / 2, cx, y_positions[2] + bh / 2)

# side note for hard gates (right side, between boxes 2 and 3)
side_annotation(ax, cx + bw / 2, (y_positions[1] + y_positions[2]) / 2,
                0.78, (y_positions[1] + y_positions[2]) / 2, 0.30, 0.055,
                "Hard gates:\nRD $\\geq$ 30 AND public data", fontsize=9)

# side note: 354 excluded
side_annotation(ax, cx + bw / 2, (y_positions[1] + y_positions[2]) / 2 - 0.005,
                0.78, (y_positions[1] + y_positions[2]) / 2 - 0.065, 0.30, 0.040,
                "354 excluded (RD < 30 or no public data)", fontsize=8)

# --- Box 4: Post-review ---
rounded_box(ax, cx, y_positions[3], bw, bh,
            "45 gate-passers retained", fontsize=11)

# arrow 3->4
arrow(ax, cx, y_positions[2] - bh / 2, cx, y_positions[3] + bh / 2)

# side note for post-review removals (right side)
mid_34 = (y_positions[2] + y_positions[3]) / 2
side_annotation(ax, cx + bw / 2, mid_34,
                0.78, mid_34, 0.30, 0.065,
                "2 removed post-review:\n  Break the Checkbox (non-religious)\n  BuddhismEval (HTTP 401)",
                fontsize=8)

# --- Box 5: Final tiers (compound) ---
# Main tier box (larger)
tier_cy = y_positions[4]
tier_h = 0.16
tier_w = bw + 0.06

# outer container
tier_rect = mpatches.FancyBboxPatch(
    (cx - tier_w / 2, tier_cy - tier_h / 2), tier_w, tier_h,
    boxstyle="round,pad=0.015", facecolor="white", edgecolor=BOX_EDGE,
    linewidth=1.4, zorder=3,
)
ax.add_patch(tier_rect)

# Title inside tier box
ax.text(cx, tier_cy + tier_h / 2 - 0.025, "25 tiered benchmarks",
        ha="center", va="center", fontsize=12, fontweight="bold",
        color=TEXT_CLR, zorder=4)

# Three tier sub-rows
sub_w = tier_w - 0.04
sub_h = 0.032
sub_x = cx
tier_data = [
    ("11 Tier 1 -- Robust ($p \\geq 0.80$)", TIER_FILLS[0], TIER_EDGES[0]),
    ("4 Tier 2 -- Likely ($0.30 \\leq p < 0.80$)", TIER_FILLS[1], TIER_EDGES[1]),
    ("10 Tier 3 -- Contested ($0.01 \\leq p < 0.30$)", TIER_FILLS[2], TIER_EDGES[2]),
]

for i, (label, fill, edge) in enumerate(tier_data):
    sy = tier_cy + 0.02 - i * 0.042
    sub_rect = mpatches.FancyBboxPatch(
        (sub_x - sub_w / 2, sy - sub_h / 2), sub_w, sub_h,
        boxstyle="round,pad=0.008", facecolor=fill, edgecolor=edge,
        linewidth=1.0, zorder=4,
    )
    ax.add_patch(sub_rect)
    ax.text(sub_x, sy, label, ha="center", va="center", fontsize=9.5,
            color=TEXT_CLR, zorder=5)

# arrow 4->5
arrow(ax, cx, y_positions[3] - bh / 2, cx, tier_cy + tier_h / 2)

# side note for bootstrap
mid_45 = (y_positions[3] + tier_cy + tier_h / 2) / 2
side_annotation(ax, cx + bw / 2, mid_45,
                0.78, mid_45, 0.30, 0.040,
                "Bootstrap sensitivity analysis\n(10,000 resamples)", fontsize=8)

# --- Title ---
ax.text(cx, 0.98, "Figure: PRISMA Flow -- Religious Values Benchmark Selection",
        ha="center", va="center", fontsize=13, fontweight="bold", color=TEXT_CLR)

# ---------- save ----------
OUT.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(OUT, dpi=DPI, bbox_inches="tight", facecolor="white")
plt.close(fig)
print(f"Saved: {OUT}  ({OUT.stat().st_size / 1024:.0f} KB)")
