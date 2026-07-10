#!/usr/bin/env python3
"""
generate_legacy_figures_v2.py — V2 wrapper for legacy figure generation.

Wraps SCRIPTS/generate_paper_figures.py to:
1. Override rcParams to v2 standards (sans-serif, 600 DPI, Arial, hatching)
2. Read data from parameterized --data-dir (not hardcoded)
3. Output to PAPER-V2/supplementary/supp-figures/ with dual PNG+PDF
4. Audit S-Fig source provenance and report defer-list

Per T1.2 figure spec sheet:
- Generates the 6 S-Figs with known matplotlib sources (S1, S2, S3, S4, S5, S6)
- Defers S-Fig 7 (silhouette, source unknown)
- Defers main Figs 2-4 (heatmap, dendrogram, biplot, sources unknown)
- For Plotly Fig 1 / S-Fig 1 (bubble map), uses cividis fallback rather than hatching

Usage:
    python generate_legacy_figures_v2.py [--data-dir ../DATA] [--out-dir supplementary/supp-figures]
"""
from __future__ import annotations

import argparse
import importlib.util
import os
import sys
from pathlib import Path

# v2 rcParams (must be set BEFORE legacy module import to override its globals)
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

V2_RCPARAMS = {
    "figure.facecolor": "white",
    "axes.facecolor": "white",
    "savefig.facecolor": "white",
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
    "hatch.linewidth": 0.5,
}


def import_legacy(legacy_path: Path):
    """Import the legacy figure module and override its globals."""
    spec = importlib.util.spec_from_file_location("legacy_figs", legacy_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def regenerate_with_v2(legacy_module, fn_name: str, out_path: Path, figsize=None):
    """Call a legacy fig function with v2 rcParams and save PNG+PDF dual output.

    Strategy: monkey-patch plt.close so the legacy function cannot close its figure,
    then grab the figure after the function returns and re-save with v2 settings.
    """
    plt.rcParams.update(V2_RCPARAMS)

    fn = getattr(legacy_module, fn_name, None)
    if fn is None:
        return False, f"function {fn_name} not found in legacy module"

    plt.close("all")

    # Monkey-patch plt.close to no-op so legacy function leaves figure in memory
    real_close = plt.close
    plt.close = lambda *a, **k: None
    # Also monkey-patch fig.savefig calls — let them happen but we'll re-save
    try:
        try:
            fn()
        finally:
            plt.close = real_close
    except Exception as e:
        return False, f"function {fn_name} failed: {type(e).__name__}: {e}"

    fig_nums = plt.get_fignums()
    if not fig_nums:
        return False, f"no figure left in memory after {fn_name}"

    fig = plt.figure(fig_nums[-1])
    if figsize:
        fig.set_size_inches(*figsize)
    fig.savefig(out_path.with_suffix(".png"), dpi=600, bbox_inches="tight", facecolor="white")
    fig.savefig(out_path.with_suffix(".pdf"), bbox_inches="tight", facecolor="white")
    real_close(fig)
    plt.close("all")
    return True, str(out_path.with_suffix(".png"))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-dir", default="../DATA", help="Directory with 20260403-*.json")
    parser.add_argument("--out-dir", default="supplementary/supp-figures", help="Output directory")
    parser.add_argument(
        "--legacy-script",
        default="../SCRIPTS/generate_paper_figures.py",
        help="Path to legacy generate_paper_figures.py",
    )
    args = parser.parse_args()

    legacy_path = Path(args.legacy_script).resolve()
    if not legacy_path.exists():
        print(f"ERROR: legacy script not found at {legacy_path}", file=sys.stderr)
        return 1

    # Resolve paths BEFORE any chdir
    out_dir = Path(args.out_dir).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)
    data_dir = Path(args.data_dir).resolve()
    if not data_dir.exists():
        print(f"ERROR: data dir not found at {data_dir}", file=sys.stderr)
        return 1

    # Apply rcParams BEFORE importing legacy (it sets its own at import time)
    plt.rcParams.update(V2_RCPARAMS)

    legacy = import_legacy(legacy_path)
    # Override legacy DATA_DIR
    if hasattr(legacy, "DATA_DIR"):
        legacy.DATA_DIR = str(data_dir)

    # Re-apply v2 rcParams (legacy module overwrote them)
    plt.rcParams.update(V2_RCPARAMS)

    # Function → output filename map per T1.2 spec
    figure_targets = [
        # (legacy_fn_name, output_filename, figsize_inches, S-Fig label)
        ("fig2_pipeline_diagram", "S-Fig4-pipeline-diagram", (7.09, 2.5), "S-Fig 4"),
        ("fig6_weird_histogram", "S-Fig2-weird-histogram", (3.46, 2.8), "S-Fig 2"),
        ("fig7_regional_radar", "S-Fig3-weird-radar", (3.46, 2.8), "S-Fig 3"),
        ("fig9_nw_detection_bars", "S-Fig5-nw-detection-bars", (7.09, 3.0), "S-Fig 5"),
        ("fig10_north_south_radar", "S-Fig6-north-south-radar", (3.46, 2.8), "S-Fig 6"),
    ]

    results = []
    for fn_name, out_name, figsize, label in figure_targets:
        out_path = out_dir / out_name
        ok, msg = regenerate_with_v2(legacy, fn_name, out_path, figsize=figsize)
        results.append((label, fn_name, ok, msg))
        status = "✓" if ok else "✗"
        print(f"  {status} {label} ({fn_name}) → {msg}")

    # Defer report
    print()
    print("Deferred figures (sources unknown or Plotly-only):")
    deferred = [
        ("Fig 1 world-map-weird", "Plotly choropleth — keep existing PNG, cividis fallback already documented"),
        ("Fig 2 heatmap-regions-frameworks", "source unknown (likely R or manual export)"),
        ("Fig 3 dendrogram", "source unknown"),
        ("Fig 4 correspondence-biplot", "source unknown"),
        ("S-Fig 1 bubble-world-map", "Plotly bubble map — keep existing PNG"),
        ("S-Fig 7 silhouette", "source unknown (likely clustering validation script)"),
    ]
    for name, reason in deferred:
        print(f"  ⏸ {name}: {reason}")

    # Summary
    n_ok = sum(1 for _, _, ok, _ in results if ok)
    n_fail = len(results) - n_ok
    print()
    print(f"Regenerated: {n_ok}/{len(results)} matplotlib S-figures at 600 DPI (PNG + PDF)")
    print(f"Deferred:    {len(deferred)} figures (source audit needed before regen)")

    return 0 if n_fail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
