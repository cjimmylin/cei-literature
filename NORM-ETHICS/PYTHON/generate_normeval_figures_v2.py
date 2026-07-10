#!/usr/bin/env python3
"""Generate publication-quality figures and tables for NormEval Paper v2.

Parses data.js and data_cross_vendor.js from the dashboard, then produces
14 figures (8 main + 6 supplementary) and a combined PDF.

Usage:
    python generate_normeval_figures_v2.py
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.colors import LinearSegmentedColormap
import numpy as np
import seaborn as sns

# ── Paths ────────────────────────────────────────────────────────────
BASE = Path(__file__).resolve().parent.parent  # NORM-ETHICS/
DASH = BASE / "DASHBOARD-v2"
OUT_FIG = BASE / "PAPER-v2" / "figures"
OUT_TBL = BASE / "PAPER-v2" / "tables"
OUT_FIG.mkdir(parents=True, exist_ok=True)
OUT_TBL.mkdir(parents=True, exist_ok=True)

# ── Academic style ───────────────────────────────────────────────────
PALETTE = {
    "blue": "#2166AC", "red": "#B2182B", "amber": "#D6604D",
    "green": "#4DAF4A", "purple": "#6A3D9A", "teal": "#1B9E77",
    "pink": "#E7298A", "gray": "#999999",
}
TRAD_COLORS = {
    "Virtue": PALETTE["purple"], "Deontological": PALETTE["blue"],
    "Utilitarian": PALETTE["amber"], "Care": PALETTE["pink"],
    "Contractarian": PALETTE["teal"],
}
PROVIDER_COLORS = {"Anthropic": "#a78bfa", "Google": "#5b8def", "OpenAI": "#4ecb71"}

plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["Times New Roman", "Charter", "Palatino"],
    "axes.titlesize": 11, "axes.labelsize": 10, "xtick.labelsize": 9,
    "ytick.labelsize": 9, "legend.fontsize": 9, "figure.dpi": 100,
    "savefig.dpi": 300, "savefig.bbox": "tight", "savefig.pad_inches": 0.05,
    "axes.spines.top": False, "axes.spines.right": False,
    "axes.grid": True, "grid.alpha": 0.3, "grid.color": "#cccccc",
})

# ── Data parsing ─────────────────────────────────────────────────────
def parse_js_constants(filepath: Path) -> dict[str, object]:
    """Extract JS const blocks from a data.js file into a dict."""
    text = filepath.read_text(encoding="utf-8")
    out = {}
    for m in re.finditer(r"const\s+(DATA_\w+)\s*=\s*", text):
        name = m.group(1)
        start = m.end()
        depth, i = 0, start
        in_str, esc = False, False
        while i < len(text):
            c = text[i]
            if esc:
                esc = False
            elif c == "\\":
                esc = True
            elif c == '"':
                in_str = not in_str
            elif not in_str:
                if c in "{[":
                    depth += 1
                elif c in "}]":
                    depth -= 1
                    if depth == 0:
                        blob = text[start:i + 1]
                        try:
                            out[name] = json.loads(blob)
                        except json.JSONDecodeError:
                            print(f"  WARN: Could not parse {name}")
                        break
            i += 1
    return out


def load_data():
    """Load all dashboard data."""
    d = parse_js_constants(DASH / "data.js")
    cv = parse_js_constants(DASH / "data_cross_vendor.js")
    d.update(cv)
    return d


# ── Figure 1: Tradition Coverage Heatmap ─────────────────────────────
def fig1_tradition_heatmap(data):
    traditions = data["DATA_TRADITION_COVERAGE"]["traditions"]
    names = data["DATA_TRADITION_COVERAGE"]["benchmark_names"]
    heatmap = np.array(data["DATA_TRADITION_COVERAGE"]["heatmap"])
    n_pass = data["DATA_OVERVIEW"]["n_pass"]

    fig, ax = plt.subplots(figsize=(5, 14))
    cmap = LinearSegmentedColormap.from_list("trad", ["#f7f7f7", PALETTE["purple"]])
    sns.heatmap(heatmap, ax=ax, cmap=cmap, vmin=0, vmax=100,
                xticklabels=traditions, yticklabels=names,
                annot=True, fmt=".0f", annot_kws={"size": 5},
                linewidths=0.3, linecolor="#e0e0e0", cbar_kws={"shrink": 0.5, "label": "Engagement Score"})
    ax.axhline(y=n_pass, color="black", linewidth=1.5, linestyle="--")
    ax.text(5.2, n_pass, f"Gate cutoff (Top {n_pass})", va="center", fontsize=7, style="italic")
    for i in range(n_pass):
        for lbl in ax.get_yticklabels():
            pass  # bold handled by font weight below
    ax.set_title("Figure 1: Tradition Coverage Across 54 Benchmarks", fontsize=11, fontweight="bold", pad=12)
    ax.set_xlabel("")
    ax.set_ylabel("")
    plt.tight_layout()
    return fig


# ── Figure 2: Framework Difficulty ───────────────────────────────────
def fig2_framework_difficulty(data):
    frameworks = ["Utilitarian", "Virtue", "Deontological"]
    accuracies = [77, 63, 50]
    colors = [TRAD_COLORS["Utilitarian"], TRAD_COLORS["Virtue"], TRAD_COLORS["Deontological"]]

    fig, ax = plt.subplots(figsize=(5, 3.5))
    bars = ax.bar(frameworks, accuracies, color=colors, edgecolor="white", width=0.6)
    ax.axhline(y=50, color=PALETTE["gray"], linestyle="--", linewidth=0.8, label="Chance (binary)")
    ax.set_ylabel("Accuracy (%)")
    ax.set_ylim(0, 100)
    ax.set_title("Figure 2: Framework Difficulty Hierarchy (MoralReason-QA)", fontsize=10, fontweight="bold")
    for bar, acc in zip(bars, accuracies):
        ax.text(bar.get_x() + bar.get_width() / 2, acc + 2, f"{acc}%", ha="center", fontsize=10, fontweight="bold")
    # 27pp bracket
    ax.annotate("", xy=(0, 77), xytext=(2, 77), arrowprops=dict(arrowstyle="<->", color="black", lw=1.2))
    ax.text(1, 79, "27pp gap", ha="center", fontsize=8, style="italic")
    ax.legend(loc="upper right", framealpha=0.7)
    plt.tight_layout()
    return fig


# ── Figure 3: ND vs PE Scatter ───────────────────────────────────────
def fig3_nd_pe_scatter(data):
    scatter = data["DATA_COMPOSITE_SCORING"]["scatter"]
    nds = [s["nd"] for s in scatter]
    pes = [s["pe"] for s in scatter]
    cis = [s["ci"] for s in scatter]
    passes = [s["passes"] for s in scatter]
    names = [s["name"] for s in scatter]

    fig, ax = plt.subplots(figsize=(6, 5))
    for i, (nd, pe, ci, p, nm) in enumerate(zip(nds, pes, cis, passes, names)):
        size = max(20, np.log10(ci + 1) * 80)
        color = PALETTE["blue"] if p else PALETTE["gray"]
        alpha = 0.85 if p else 0.4
        ax.scatter(nd, pe, s=size, c=color, alpha=alpha, edgecolors="white", linewidth=0.5, zorder=3 if p else 2)
        if i < 3 or nm.startswith("Aligning AI"):
            offset = (5, 5) if i > 0 else (5, -10)
            ax.annotate(nm[:25], (nd, pe), textcoords="offset points", xytext=offset, fontsize=6, alpha=0.8)

    ax.axvline(x=40, color=PALETTE["red"], linestyle=":", linewidth=0.8, alpha=0.6, label="ND gate = 40")
    ax.set_xlabel("Normative Depth (ND)")
    ax.set_ylabel("Practical Ease (PE)")
    ax.set_title("Figure 3: ND vs. PE Tradeoff (n=54)", fontsize=10, fontweight="bold")
    ax.legend(loc="lower left", framealpha=0.7)
    legend_pass = mpatches.Patch(color=PALETTE["blue"], label="Gate-pass")
    legend_fail = mpatches.Patch(color=PALETTE["gray"], alpha=0.4, label="Gate-fail")
    ax.legend(handles=[legend_pass, legend_fail], loc="lower left", framealpha=0.7)
    plt.tight_layout()
    return fig


# ── Figure 4: Data Availability ──────────────────────────────────────
def fig4_data_availability(data):
    host_dist = data["DATA_AVAILABILITY"]["host_distribution"]
    names = [h["name"] for h in host_dist]
    counts = [h["count"] for h in host_dist]
    total = sum(counts)
    colors = [PALETTE["red"] if n == "None" else PALETTE["green"] if n == "GitHub"
              else PALETTE["teal"] if n == "HuggingFace" else PALETTE["amber"] for n in names]

    fig, ax = plt.subplots(figsize=(6, 3))
    left = 0
    for name, count, color in zip(names, counts, colors):
        ax.barh(0, count, left=left, color=color, edgecolor="white", height=0.5)
        if count > 2:
            ax.text(left + count / 2, 0, f"{name}\n{count} ({count*100//total}%)",
                    ha="center", va="center", fontsize=8, color="white" if name in ("None", "GitHub") else "black")
        left += count
    ax.set_xlim(0, total)
    ax.set_yticks([])
    ax.set_xlabel("Number of Benchmarks")
    ax.set_title("Figure 4: Data Availability Distribution (n=54)", fontsize=10, fontweight="bold")
    plt.tight_layout()
    return fig


# ── Figure 5: Trial Accuracy vs Discriminative Power ─────────────────
def fig5_trial_paired_bar(data):
    trials = data["DATA_TRIAL_DATA"]["trials"]
    ids = [t["id"] for t in trials]
    accs = [t["accuracy"] for t in trials]
    discs = [t["discriminative"] for t in trials]

    fig, ax = plt.subplots(figsize=(8, 4))
    x = np.arange(len(ids))
    w = 0.35
    ax.bar(x - w / 2, accs, w, color=PALETTE["green"], label="Accuracy", alpha=0.85)
    ax.bar(x + w / 2, discs, w, color=PALETTE["blue"], label="Discriminative Power", alpha=0.85)
    ax.set_xticks(x)
    ax.set_xticklabels(ids, fontsize=8)
    ax.set_ylabel("Score")
    ax.set_ylim(0, 105)
    ax.set_title("Figure 5: Accuracy vs. Discriminative Power (15 Trials)", fontsize=10, fontweight="bold")
    ax.legend(loc="upper right", framealpha=0.7)
    # Highlight T1 inversion
    ax.annotate("Ceiling\n(zero disc.)", xy=(0, 5), fontsize=7, ha="center", color=PALETTE["red"], style="italic")
    plt.tight_layout()
    return fig


# ── Figure 6: IH/IB Scaling ─────────────────────────────────────────
def fig6_ih_ib_scaling(data):
    cv = data["DATA_CROSS_VENDOR"]
    models = cv["ih_scaling"]["models"]
    providers = cv["ih_scaling"]["providers"]
    ih = cv["ih_scaling"]["IH_means"]
    ib = cv["ih_scaling"]["IB_means"]
    ref_phil = cv["ih_scaling"]["ref_philosopher_IH"]
    ref_lay = cv["ih_scaling"]["ref_lay_IH"]

    fig, ax = plt.subplots(figsize=(8, 4.5))
    x = np.arange(len(models))
    w = 0.35
    bars_ih = ax.bar(x - w / 2, ih, w, color=PALETTE["red"], label="IH (Instrumental Harm)", alpha=0.85)
    bars_ib = ax.bar(x + w / 2, ib, w, color=PALETTE["green"], label="IB (Impartial Beneficence)", alpha=0.85)
    ax.axhline(y=ref_phil, color=PALETTE["amber"], linestyle="--", linewidth=1, label=f"Philosopher IH ref ({ref_phil})")
    ax.axhline(y=ref_lay, color=PALETTE["gray"], linestyle="--", linewidth=1, label=f"Lay population IH ref ({ref_lay})")

    ax.set_xticks(x)
    ax.set_xticklabels(models, fontsize=7, rotation=30, ha="right")
    ax.set_ylabel("OUS Score (1-7)")
    ax.set_ylim(1, 7)
    ax.set_title("Figure 6: Instrumental Harm and Impartial Beneficence Across 9 Models", fontsize=10, fontweight="bold")
    ax.legend(loc="upper left", fontsize=7, framealpha=0.7)

    # Provider brackets
    provider_spans = {}
    for i, p in enumerate(providers):
        provider_spans.setdefault(p, []).append(i)
    for prov, idxs in provider_spans.items():
        mid = np.mean(idxs)
        ax.text(mid, 0.7, prov, ha="center", fontsize=7, color=PROVIDER_COLORS.get(prov, "black"),
                fontweight="bold", transform=ax.get_xaxis_transform())
    plt.tight_layout()
    return fig


# ── Figure 7: Cross-Vendor Pairwise Agreement Heatmap ────────────────
def fig7_cross_vendor_heatmap(data):
    cv = data["DATA_CROSS_VENDOR"]
    labels = cv["heatmap"]["labels"]
    matrix = np.array(cv["heatmap"]["matrix"])

    fig, ax = plt.subplots(figsize=(6, 5))
    cmap = LinearSegmentedColormap.from_list("agree", ["#fee0d2", "#fc9272", "#de2d26", "#67000d"][::-1])
    # Reverse so 100% is dark green, low is red
    cmap = sns.color_palette("RdYlGn", as_cmap=True)
    sns.heatmap(matrix, ax=ax, annot=True, fmt=".1f", cmap=cmap,
                vmin=70, vmax=100, xticklabels=labels, yticklabels=labels,
                annot_kws={"size": 8}, linewidths=0.5, linecolor="white",
                cbar_kws={"shrink": 0.7, "label": "Agreement %"})
    ax.set_title("Figure 7: Cross-Vendor Pairwise Agreement (114 Items)", fontsize=10, fontweight="bold")

    # Provider boxes
    # Anthropic: 0-1, Google: 2-5, OpenAI: 6-7
    for start, end, prov in [(0, 2, "Anthropic"), (2, 6, "Google"), (6, 8, "OpenAI")]:
        rect = plt.Rectangle((start, start), end - start, end - start,
                              fill=False, edgecolor=PROVIDER_COLORS[prov], linewidth=2)
        ax.add_patch(rect)
    plt.tight_layout()
    return fig


# ── Figure 8: Knowledge vs Judgment Divergence ───────────────────────
def fig8_knowledge_judgment(data):
    cv = data["DATA_CROSS_VENDOR"]
    trials = cv["knowledge_judgment"]["trials"]

    # Sort: knowledge first, then mixed, then judgment
    type_order = {"knowledge": 0, "mixed": 1, "judgment": 2}
    trials_sorted = sorted(trials, key=lambda t: (type_order[t["type"]], t["id"]))

    fig, ax = plt.subplots(figsize=(6, 4.5))
    type_colors = {"knowledge": PALETTE["green"], "mixed": PALETTE["amber"], "judgment": PALETTE["red"]}

    for i, t in enumerate(trials_sorted):
        color = type_colors[t["type"]]
        mn, mx = t["min_agreement"], t["max_agreement"]
        ax.plot([mn, mx], [i, i], color=color, linewidth=3, solid_capstyle="round", zorder=3)
        ax.scatter([mn, mx], [i, i], color=color, s=40, zorder=4, edgecolors="white", linewidth=0.5)
        ax.text(mx + 1.5, i, f'{t["id"]}: {t["name"]}', va="center", fontsize=7)

    ax.set_xlim(25, 120)
    ax.set_ylim(-0.5, len(trials_sorted) - 0.5)
    ax.set_xlabel("Pairwise Agreement Range (%)")
    ax.set_title("Figure 8: Knowledge vs. Judgment Divergence", fontsize=10, fontweight="bold")
    ax.set_yticks([])
    ax.axvline(x=100, color=PALETTE["gray"], linestyle=":", linewidth=0.5, alpha=0.5)

    # Legend
    patches = [mpatches.Patch(color=type_colors[t], label=t.capitalize()) for t in ["knowledge", "mixed", "judgment"]]
    ax.legend(handles=patches, loc="lower left", framealpha=0.7)
    plt.tight_layout()
    return fig


# ── Supplementary Figures ────────────────────────────────────────────
def figS1_pca_clusters(data):
    if "DATA_PCA_DATA" not in data:
        return None
    pca = data["DATA_PCA_DATA"]
    benchmarks = pca.get("benchmarks", [])
    if not benchmarks:
        return None

    fig, ax = plt.subplots(figsize=(6, 5))
    for b in benchmarks:
        color = PALETTE["blue"] if b.get("passes_gates", False) else PALETTE["gray"]
        ax.scatter(b["pc1"], b["pc2"], c=color, s=30, alpha=0.7, edgecolors="white", linewidth=0.3)
    ax.set_xlabel("PC1")
    ax.set_ylabel("PC2")
    ax.set_title("Figure S1: PCA Benchmark Clustering", fontsize=10, fontweight="bold")
    plt.tight_layout()
    return fig


def figS2_temporal_trends(data):
    if "DATA_TEMPORAL_DATA" not in data:
        return None
    td = data["DATA_TEMPORAL_DATA"]
    benchmarks = td.get("benchmarks", [])
    if not benchmarks:
        return None

    fig, axes = plt.subplots(1, 3, figsize=(10, 3.5), sharey=False)
    for ax, metric in zip(axes, ["ND", "PE", "CI"]):
        years = [b["year"] for b in benchmarks if metric in b]
        vals = [b[metric] for b in benchmarks if metric in b]
        if years:
            ax.scatter(years, vals, c=PALETTE["blue"], s=20, alpha=0.6)
            if len(years) > 2:
                z = np.polyfit(years, vals, 1)
                xs = np.linspace(min(years), max(years), 50)
                ax.plot(xs, np.polyval(z, xs), color=PALETTE["red"], linewidth=1.5, linestyle="--")
        ax.set_xlabel("Year")
        ax.set_ylabel(metric)
        ax.set_title(f"{metric} over Time", fontsize=9)
    fig.suptitle("Figure S2: Temporal Trends in Benchmark Properties", fontsize=10, fontweight="bold", y=1.02)
    plt.tight_layout()
    return fig


def figS5_provider_radar(data):
    cv = data.get("DATA_CROSS_VENDOR", {})
    pp = cv.get("provider_profiles", {})
    if not pp:
        return None

    dims = pp.get("dimensions", [])
    profiles = pp.get("profiles", {})
    if not dims or not profiles:
        return None

    n = len(dims)
    angles = np.linspace(0, 2 * np.pi, n, endpoint=False).tolist()
    angles += angles[:1]  # close polygon

    fig, ax = plt.subplots(figsize=(5.5, 5.5), subplot_kw=dict(polar=True))

    prov_colors = {"Anthropic (Sonnet)": PROVIDER_COLORS["Anthropic"],
                   "OpenAI (GPT-5)": PROVIDER_COLORS["OpenAI"],
                   "Google (Gemini)": PROVIDER_COLORS["Google"]}

    for prov_name, values in profiles.items():
        vals = values + values[:1]  # close polygon
        color = prov_colors.get(prov_name, PALETTE["gray"])
        ax.plot(angles, vals, "o-", linewidth=1.8, label=prov_name, color=color)
        ax.fill(angles, vals, alpha=0.15, color=color)

    ax.set_thetagrids(np.degrees(angles[:-1]), dims, fontsize=7)
    ax.set_ylim(0, 105)
    ax.set_title("Figure S5: Provider Ethical Profiles\n(6 Dimensions)", fontsize=10, fontweight="bold", pad=20)
    ax.legend(loc="upper right", bbox_to_anchor=(1.3, 1.1), fontsize=7, framealpha=0.7)
    plt.tight_layout()
    return fig


def figS6_cbr_by_model(data):
    cv = data.get("DATA_CROSS_VENDOR", {})
    cbr = cv.get("cbr_rate", {})
    models = cbr.get("models", [])
    providers = cbr.get("providers", [])
    rates = cbr.get("cbr_percent", [])
    if not models:
        return None

    fig, ax = plt.subplots(figsize=(7, 3.5))
    colors = [PROVIDER_COLORS.get(p, PALETTE["gray"]) for p in providers]
    bars = ax.bar(range(len(models)), rates, color=colors, edgecolor="white")
    ax.axhline(y=50, color=PALETTE["gray"], linestyle="--", linewidth=0.8, label="50% (neutral)")
    ax.set_xticks(range(len(models)))
    ax.set_xticklabels(models, fontsize=7, rotation=30, ha="right")
    ax.set_ylabel("Cognitive Bias Rate (%)")
    ax.set_title("Figure S6: CBR by Model", fontsize=10, fontweight="bold")
    ax.legend(loc="upper left", fontsize=7)
    for bar, rate in zip(bars, rates):
        ax.text(bar.get_x() + bar.get_width() / 2, rate + 1, f"{rate}%", ha="center", fontsize=7)
    plt.tight_layout()
    return fig


# ── Save helper ──────────────────────────────────────────────────────
def save_fig(fig, name, is_supp=False):
    """Save figure as both PNG and PDF."""
    if fig is None:
        print(f"  SKIP: {name} (no data)")
        return
    prefix = "figS" if is_supp else "fig"
    for ext in ("png", "pdf"):
        path = OUT_FIG / f"{name}.{ext}"
        fig.savefig(path, format=ext)
    plt.close(fig)
    print(f"  OK: {name}")


# ── Combined PDF ─────────────────────────────────────────────────────
def build_combined_pdf():
    """Assemble all figures into a single PDF using fpdf2."""
    from fpdf import FPDF

    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.set_auto_page_break(auto=True, margin=15)

    from fpdf.enums import XPos, YPos

    # Title page
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 16)
    pdf.cell(0, 40, "", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.multi_cell(0, 10, "NormEval Paper v2\nFigures and Tables", align="C")
    pdf.set_font("Helvetica", "", 11)
    pdf.cell(0, 20, "", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.cell(0, 8, "Three Ethical Profiles, One Knowledge Ceiling:", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.cell(0, 8, "A Meta-Evaluation of 54 Normative Ethics Benchmarks", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.cell(0, 8, "Across Nine LLMs and Three Vendors", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.cell(0, 20, "", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.cell(0, 8, "Generated: 2026-04-05", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    # Main body figures
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 14)
    pdf.cell(0, 10, "Main Body Figures", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(5)

    fig_files = sorted(OUT_FIG.glob("fig[0-9]*.png"))
    for f in fig_files:
        pdf.add_page()
        pdf.set_font("Helvetica", "B", 10)
        pdf.cell(0, 8, f.stem.replace("-", " ").title(), new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        try:
            pdf.image(str(f), x=10, w=190)
        except Exception as e:
            pdf.set_font("Helvetica", "", 9)
            pdf.cell(0, 8, f"[Could not embed: {e}]", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    # Supplementary figures
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 14)
    pdf.cell(0, 10, "Supplementary Figures", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(5)

    supp_files = sorted(OUT_FIG.glob("figS*.png"))
    for f in supp_files:
        pdf.add_page()
        pdf.set_font("Helvetica", "B", 10)
        pdf.cell(0, 8, f.stem.replace("-", " ").title(), new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        try:
            pdf.image(str(f), x=10, w=190)
        except Exception as e:
            pdf.set_font("Helvetica", "", 9)
            pdf.cell(0, 8, f"[Could not embed: {e}]", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    out_path = BASE / "PAPER-v2" / "normeval-figures-tables-v2.pdf"
    pdf.output(str(out_path))
    print(f"\n  Combined PDF: {out_path}")


# ── Main ─────────────────────────────────────────────────────────────
def main():
    print("Loading dashboard data...")
    data = load_data()
    print(f"  Loaded {len(data)} data constants")

    # Validate
    n_bench = data["DATA_OVERVIEW"]["n_total"]
    n_pass = data["DATA_OVERVIEW"]["n_pass"]
    print(f"  Benchmarks: {n_bench}, Gate-pass: {n_pass}")

    print("\nGenerating main body figures...")
    save_fig(fig1_tradition_heatmap(data), "fig1-tradition-heatmap")
    save_fig(fig2_framework_difficulty(data), "fig2-framework-difficulty")
    save_fig(fig3_nd_pe_scatter(data), "fig3-nd-vs-pe-scatter")
    save_fig(fig4_data_availability(data), "fig4-data-availability")
    save_fig(fig5_trial_paired_bar(data), "fig5-trial-accuracy-discriminative")
    save_fig(fig6_ih_ib_scaling(data), "fig6-ih-ib-scaling")
    save_fig(fig7_cross_vendor_heatmap(data), "fig7-cross-vendor-heatmap")
    save_fig(fig8_knowledge_judgment(data), "fig8-knowledge-judgment-divergence")

    print("\nGenerating supplementary figures...")
    save_fig(figS1_pca_clusters(data), "figS1-pca-clusters", is_supp=True)
    save_fig(figS2_temporal_trends(data), "figS2-temporal-trends", is_supp=True)
    save_fig(figS5_provider_radar(data), "figS5-provider-radar", is_supp=True)
    save_fig(figS6_cbr_by_model(data), "figS6-cbr-by-model", is_supp=True)

    print("\nBuilding combined PDF...")
    build_combined_pdf()

    print("\nDone! Files in:")
    print(f"  Figures: {OUT_FIG}")
    print(f"  Combined: {BASE / 'PAPER-v2' / 'normeval-figures-tables-v2.pdf'}")


if __name__ == "__main__":
    main()
