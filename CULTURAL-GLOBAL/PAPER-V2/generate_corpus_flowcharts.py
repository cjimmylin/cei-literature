#!/usr/bin/env python3
"""
generate_corpus_flowcharts.py — Build two supplementary flowcharts.

Per T1.4 corpus flowchart spec (post-meta-critique reframing of "Modified PRISMA"):
1. Study 1 "Corpus Assembly Flowchart" — bibliometric standard, Donthu et al. 2021,
   Zupic & Cater 2015. Cumulative corpus, "~" counts allowed.
2. Study 2 "Benchmark Identification Flowchart" — PRISMA 2020 reporting principles
   (Page et al. 2021). Systematic search, exact counts.

Both saved to supplementary/supp-figures/ at 600 DPI PNG + vector PDF.
"""
from __future__ import annotations

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from pathlib import Path

# v2 rcParams
plt.rcParams.update({
    "figure.facecolor": "white",
    "axes.facecolor": "white",
    "savefig.facecolor": "white",
    "font.family": "sans-serif",
    "font.sans-serif": ["Arial", "Helvetica Neue", "DejaVu Sans"],
    "font.size": 8,
    "savefig.dpi": 600,
    "savefig.bbox": "tight",
    "pdf.fonttype": 42,
})

# Okabe-Ito grayscale-safe palette
COLOR_BOX = "#0072B2"      # blue
COLOR_EXCLUDE = "#D55E00"  # vermillion
COLOR_TEXT = "#000000"
COLOR_ARROW = "#444444"
COLOR_BOX_FILL = "#E6F0F8"
COLOR_EXCL_FILL = "#FBE5D6"


def draw_box(ax, xy, width, height, text, fill=COLOR_BOX_FILL, edge=COLOR_BOX):
    """Draw a rounded rectangle node with centered text."""
    box = FancyBboxPatch(
        (xy[0] - width / 2, xy[1] - height / 2),
        width, height,
        boxstyle="round,pad=0.04,rounding_size=0.08",
        linewidth=1.2,
        edgecolor=edge,
        facecolor=fill,
    )
    ax.add_patch(box)
    ax.text(
        xy[0], xy[1], text,
        ha="center", va="center",
        fontsize=7,
        color=COLOR_TEXT,
        wrap=True,
    )


def draw_arrow(ax, start, end, dashed=False):
    """Draw a flow arrow between nodes."""
    style = "->,head_length=4,head_width=3"
    linestyle = "--" if dashed else "-"
    arrow = FancyArrowPatch(
        start, end,
        arrowstyle=style,
        color=COLOR_ARROW,
        linewidth=1.0,
        linestyle=linestyle,
    )
    ax.add_patch(arrow)


def make_study1_flowchart(out_path: Path):
    """Study 1 — Corpus Assembly Flowchart (bibliometric standard)."""
    fig, ax = plt.subplots(figsize=(3.46, 5.5))  # single column
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 14)
    ax.axis("off")

    # Title
    ax.text(
        5, 13.5,
        "Study 1: Corpus Assembly Flowchart",
        ha="center", va="center",
        fontsize=9, fontweight="bold",
    )
    ax.text(
        5, 13.0,
        "(Bibliometric standard; cumulative)",
        ha="center", va="center",
        fontsize=7, style="italic", color="#555",
    )

    # Identification node
    draw_box(
        ax, (5, 11.2), 8.5, 1.4,
        "Identification\n~2,501 papers from arXiv (~1,443),\nACL Anthology (~908), targeted searches (~150)\n[cumulative 2010–2026]",
    )
    draw_arrow(ax, (5, 10.5), (5, 9.6))

    # Duplicates removed
    draw_box(
        ax, (5, 9.0), 8.5, 1.0,
        "Duplicates removed\n~120 papers",
        fill=COLOR_EXCL_FILL, edge=COLOR_EXCLUDE,
    )
    draw_arrow(ax, (5, 8.5), (5, 7.6))

    # Screening
    draw_box(
        ax, (5, 7.0), 8.5, 1.2,
        "Screening\n~2,381 papers screened against\nAI ethics inclusion criteria",
    )
    # Branch off for exclusions
    draw_arrow(ax, (5, 6.4), (5, 5.5))
    draw_arrow(ax, (8.5, 7.0), (9.0, 5.5), dashed=True)

    # Excluded with reasons
    draw_box(
        ax, (8.5, 5.0), 2.6, 1.0,
        "Excluded\n52 papers\n(no AI ethics\ncontent)",
        fill=COLOR_EXCL_FILL, edge=COLOR_EXCLUDE,
    )

    # Inclusion
    draw_box(
        ax, (5, 4.7), 8.5, 1.2,
        "Inclusion\n2,329 papers retained for\nWEIRD scoring + framework analysis",
    )
    draw_arrow(ax, (5, 4.1), (5, 3.2))

    # Sub-corpus split
    draw_box(
        ax, (3, 2.6), 4.0, 1.2,
        "Ethics subset\n730 papers\n(ethics_overall ≥ 50)",
    )
    draw_box(
        ax, (7.5, 2.6), 4.0, 1.2,
        "Broader corpus\n1,599 papers\n(technical+adjacent)",
    )
    draw_arrow(ax, (5, 4.1), (3, 3.2))
    draw_arrow(ax, (5, 4.1), (7.5, 3.2))

    # Footnote
    ax.text(
        5, 0.6,
        "Counts marked '~' reflect cumulative incremental assembly (Donthu et al. 2021;\nZupic & Cater 2015). This is not a prospective systematic review.",
        ha="center", va="center",
        fontsize=6, style="italic", color="#555",
    )

    fig.savefig(out_path.with_suffix(".png"), dpi=600, bbox_inches="tight", facecolor="white")
    fig.savefig(out_path.with_suffix(".pdf"), bbox_inches="tight", facecolor="white")
    plt.close(fig)


def make_study2_flowchart(out_path: Path):
    """Study 2 — Benchmark Identification Flowchart (PRISMA-adjacent)."""
    fig, ax = plt.subplots(figsize=(3.46, 6.0))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 16)
    ax.axis("off")

    ax.text(
        5, 15.5,
        "Study 2: Benchmark Identification",
        ha="center", va="center",
        fontsize=9, fontweight="bold",
    )
    ax.text(
        5, 15.0,
        "(Following PRISMA 2020 reporting principles)",
        ha="center", va="center",
        fontsize=7, style="italic", color="#555",
    )

    # Identification
    draw_box(
        ax, (5, 13.2), 8.5, 1.4,
        "Identification\nVault scan: 1,574 candidates\n(composite_relevance ≥ 20 from 2,329)\n+ 48 from external search",
    )
    draw_arrow(ax, (5, 12.5), (5, 11.6))

    # Screening
    draw_box(
        ax, (5, 11.0), 8.5, 1.2,
        "Screening\n1,622 records reviewed against\ninclusion criteria",
    )
    draw_arrow(ax, (5, 10.4), (5, 9.5))
    draw_arrow(ax, (8.5, 11.0), (9.0, 8.5), dashed=True)

    # Excluded with reasons
    draw_box(
        ax, (8.7, 7.6), 3.0, 2.4,
        "Excluded\n1,404 records\n• 800 no benchmark\n• 450 no cross-cultural\n  values content\n• 154 insufficient\n  methodological detail",
        fill=COLOR_EXCL_FILL, edge=COLOR_EXCLUDE,
    )

    # Eligibility / Inclusion
    draw_box(
        ax, (5, 8.9), 8.5, 1.2,
        "Eligibility\n218 benchmarks meet\nfull inclusion criteria",
    )
    draw_arrow(ax, (5, 8.3), (5, 7.4))

    # Final inclusion
    draw_box(
        ax, (5, 6.8), 8.5, 1.2,
        "Inclusion\n218 benchmarks for\nmeta-evaluation analysis",
    )
    draw_arrow(ax, (5, 6.2), (5, 5.0))

    # Coding split
    draw_box(
        ax, (3, 4.3), 4.0, 1.4,
        "Deep-scored\n32 benchmarks\n× 96 features\n(council coding)",
    )
    draw_box(
        ax, (7.5, 4.3), 4.0, 1.4,
        "Automated-scored\n186 benchmarks\n× 13 features\n(keyword scoring)",
    )
    draw_arrow(ax, (5, 6.2), (3, 5.0))
    draw_arrow(ax, (5, 6.2), (7.5, 5.0))

    # External search note
    ax.text(
        5, 2.4,
        "External search: Semantic Scholar, arXiv, ACL Anthology;\ntargeted for underrepresented traditions; 15 net new benchmarks",
        ha="center", va="center",
        fontsize=6, color="#555",
    )

    # Footnote
    ax.text(
        5, 0.6,
        "Reporting follows PRISMA 2020 principles (Page et al. 2021) for the screening\nand selection pipeline. Cross-cultural validity coding in separate pass.",
        ha="center", va="center",
        fontsize=6, style="italic", color="#555",
    )

    fig.savefig(out_path.with_suffix(".png"), dpi=600, bbox_inches="tight", facecolor="white")
    fig.savefig(out_path.with_suffix(".pdf"), bbox_inches="tight", facecolor="white")
    plt.close(fig)


def main():
    out_dir = Path(__file__).parent / "supplementary" / "supp-figures"
    out_dir.mkdir(parents=True, exist_ok=True)

    print("Generating Study 1 Corpus Assembly Flowchart...")
    make_study1_flowchart(out_dir / "S-Fig-Study1-Corpus-Assembly")
    print(f"  → {out_dir / 'S-Fig-Study1-Corpus-Assembly.png'}")

    print("Generating Study 2 Benchmark Identification Flowchart...")
    make_study2_flowchart(out_dir / "S-Fig-Study2-Benchmark-Identification")
    print(f"  → {out_dir / 'S-Fig-Study2-Benchmark-Identification.png'}")

    print("\nDone. Both flowcharts at 600 DPI PNG + vector PDF.")


if __name__ == "__main__":
    main()
