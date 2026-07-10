"""Correspondence Analysis (CA) of region x framework contingency table.

Performs CA via manual SVD on the 10-region x 12-framework detection-count
matrix, producing a biplot PNG and a JSON results file.
"""
from __future__ import annotations

import functools
import json
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

print = functools.partial(print, flush=True)

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
BASE = Path(__file__).resolve().parent.parent          # CULTURAL-GLOBAL/
DATA = BASE / "DATA"
FIGURES = BASE / "PAPER" / "figures"
FIGURES.mkdir(parents=True, exist_ok=True)

INPUT_FILE = DATA / "20260403-cross-cultural-analysis.json"
OUTPUT_JSON = DATA / "20260403-correspondence-analysis.json"
OUTPUT_PNG = FIGURES / "correspondence-biplot.png"

# ---------------------------------------------------------------------------
# Framework and region constants
# ---------------------------------------------------------------------------
FRAMEWORKS = [
    "virtue_ethics",
    "deontological_ethics",
    "utilitarian_ethics",
    "care_ethics",
    "contractarian_ethics",
    "nw_confucian",
    "nw_ubuntu",
    "nw_islamic_ethics",
    "nw_buddhist",
    "nw_dharmic",
    "nw_indigenous_relational",
    "nw_buen_vivir",
]

REGIONS = [
    "North America",
    "Western Europe",
    "East Asia",
    "MENA",
    "South Asia",
    "Southeast Asia",
    "Latin America & Caribbean",
    "Eastern Europe & Central Asia",
    "Oceania",
    "Sub-Saharan Africa",
]

DISPLAY_NAMES = {
    "virtue_ethics": "Virtue",
    "deontological_ethics": "Deontological",
    "utilitarian_ethics": "Utilitarian",
    "care_ethics": "Care",
    "contractarian_ethics": "Contractarian",
    "nw_confucian": "Confucian",
    "nw_ubuntu": "Ubuntu",
    "nw_islamic_ethics": "Islamic",
    "nw_buddhist": "Buddhist",
    "nw_dharmic": "Dharmic",
    "nw_indigenous_relational": "Indigenous",
    "nw_buen_vivir": "Buen Vivir",
}

REGION_COLORS = {
    "North America": "#E69F00",
    "Western Europe": "#56B4E9",
    "East Asia": "#009E73",
    "MENA": "#F0E442",
    "South Asia": "#0072B2",
    "Southeast Asia": "#D55E00",
    "Latin America & Caribbean": "#CC79A7",
    "Eastern Europe & Central Asia": "#999999",
    "Oceania": "#000000",
    "Sub-Saharan Africa": "#E84855",
}


def build_contingency_table(data: dict) -> np.ndarray:
    """Build region x framework detection-count matrix from cross-cultural analysis.

    Uses detection_rate (%) * n / 100, rounded to nearest integer.
    """
    profiles = data["regional_profiles"]
    N = np.zeros((len(REGIONS), len(FRAMEWORKS)), dtype=float)
    for i, region in enumerate(REGIONS):
        info = profiles[region]
        n = info["n"]
        rates = info["detection_rates"]
        for j, fw in enumerate(FRAMEWORKS):
            N[i, j] = round(rates[fw] * n / 100.0)
    return N


def run_ca(N: np.ndarray) -> dict:
    """Run correspondence analysis via SVD on contingency table N.

    Returns dict with coordinates, singular values, explained variance, etc.
    """
    # --- Identify and exclude zero-sum rows/columns ---
    row_sums = N.sum(axis=1)
    col_sums = N.sum(axis=0)

    row_mask = row_sums > 0
    col_mask = col_sums > 0

    active_rows = [i for i, m in enumerate(row_mask) if m]
    active_cols = [j for j, m in enumerate(col_mask) if m]

    if len(active_rows) < len(REGIONS):
        excluded_regions = [REGIONS[i] for i in range(len(REGIONS)) if not row_mask[i]]
        print(f"WARNING: Excluding zero-sum regions: {excluded_regions}")

    if len(active_cols) < len(FRAMEWORKS):
        excluded_fws = [FRAMEWORKS[j] for j in range(len(FRAMEWORKS)) if not col_mask[j]]
        print(f"WARNING: Excluding zero-sum frameworks: {excluded_fws}")

    N_active = N[np.ix_(active_rows, active_cols)]

    # --- Correspondence analysis ---
    grand_total = N_active.sum()
    P = N_active / grand_total               # correspondence matrix
    r = P.sum(axis=1)                         # row masses
    c = P.sum(axis=0)                         # column masses

    Dr_inv_sqrt = np.diag(1.0 / np.sqrt(r))
    Dc_inv_sqrt = np.diag(1.0 / np.sqrt(c))

    # Standardized residuals
    S = Dr_inv_sqrt @ (P - np.outer(r, c)) @ Dc_inv_sqrt

    # SVD
    U, sigma, Vt = np.linalg.svd(S, full_matrices=False)

    # Principal coordinates (symmetric scaling)
    F = Dr_inv_sqrt @ U * sigma               # row (region) coordinates
    G = Dc_inv_sqrt @ Vt.T * sigma            # column (framework) coordinates

    total_inertia = float(np.sum(sigma ** 2))
    n_dims = min(len(sigma), 2)
    explained = [(float(sigma[k] ** 2) / total_inertia * 100) for k in range(n_dims)]

    # --- Build coordinate dicts (all regions/frameworks, zero for excluded) ---
    row_coords: dict[str, list[float]] = {}
    for idx, i in enumerate(active_rows):
        row_coords[REGIONS[i]] = [float(F[idx, 0]), float(F[idx, 1]) if n_dims > 1 else 0.0]
    # Fill excluded regions with 0,0
    for i in range(len(REGIONS)):
        if REGIONS[i] not in row_coords:
            row_coords[REGIONS[i]] = [0.0, 0.0]

    col_coords: dict[str, list[float]] = {}
    for idx, j in enumerate(active_cols):
        col_coords[FRAMEWORKS[j]] = [float(G[idx, 0]), float(G[idx, 1]) if n_dims > 1 else 0.0]
    for j in range(len(FRAMEWORKS)):
        if FRAMEWORKS[j] not in col_coords:
            col_coords[FRAMEWORKS[j]] = [0.0, 0.0]

    # Display-name versions
    row_coords_display = dict(row_coords)
    col_coords_display = {DISPLAY_NAMES[k]: v for k, v in col_coords.items()}

    return {
        "total_inertia": total_inertia,
        "explained_variance_pct": explained,
        "singular_values": [float(s) for s in sigma],
        "row_coords": row_coords,
        "col_coords": col_coords,
        "row_coords_display": row_coords_display,
        "col_coords_display": col_coords_display,
    }


def make_biplot(ca: dict) -> None:
    """Generate publication-quality correspondence analysis biplot."""
    fig, ax = plt.subplots(figsize=(12, 10))
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")

    ev = ca["explained_variance_pct"]
    dim1_label = f"Dimension 1 ({ev[0]:.1f}%)"
    dim2_label = f"Dimension 2 ({ev[1]:.1f}%)" if len(ev) > 1 else "Dimension 2"

    # --- Origin crosshair ---
    ax.axhline(0, color="#cccccc", linewidth=0.8, zorder=1)
    ax.axvline(0, color="#cccccc", linewidth=0.8, zorder=1)

    # --- Plot framework points (columns) ---
    for fw, (x, y) in ca["col_coords"].items():
        display = DISPLAY_NAMES[fw]
        ax.scatter(x, y, marker="^", s=100, c="#888888", edgecolors="black",
                   linewidths=0.5, zorder=3)
        ax.annotate(display, (x, y), textcoords="offset points", xytext=(6, 6),
                    fontsize=9, fontstyle="italic", color="#555555", zorder=4)

    # --- Plot region points (rows) ---
    for region, (x, y) in ca["row_coords"].items():
        color = REGION_COLORS.get(region, "#000000")
        ax.scatter(x, y, marker="o", s=160, c=color, edgecolors="black",
                   linewidths=0.8, zorder=5, label=region)
        ax.annotate(region, (x, y), textcoords="offset points", xytext=(8, -4),
                    fontsize=9, fontweight="bold", color=color, zorder=6)

    ax.set_xlabel(dim1_label, fontsize=12)
    ax.set_ylabel(dim2_label, fontsize=12)
    ax.set_title("Correspondence Analysis: Regions \u00d7 Frameworks", fontsize=14,
                 fontweight="bold", pad=15)

    # Legend — sorted by order in REGIONS
    handles, labels = ax.get_legend_handles_labels()
    order = {r: i for i, r in enumerate(REGIONS)}
    sorted_pairs = sorted(zip(handles, labels), key=lambda t: order.get(t[1], 99))
    if sorted_pairs:
        ax.legend([h for h, _ in sorted_pairs], [l for _, l in sorted_pairs],
                  loc="lower right", fontsize=8, framealpha=0.9, title="Regions",
                  title_fontsize=9)

    ax.grid(True, alpha=0.15, linewidth=0.5)
    ax.tick_params(labelsize=10)
    fig.tight_layout()
    fig.savefig(OUTPUT_PNG, dpi=300, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"Biplot saved to {OUTPUT_PNG}")


def main() -> None:
    print("=== Correspondence Analysis: Regions x Frameworks ===\n")

    # --- Load data ---
    with open(INPUT_FILE) as f:
        data = json.load(f)

    # --- Build contingency table ---
    N = build_contingency_table(data)
    print(f"Contingency table: {N.shape[0]} regions x {N.shape[1]} frameworks")
    print(f"Grand total detections: {int(N.sum())}")
    print()

    # Print the contingency table
    print("Detection counts (score >= 50) per region x framework:")
    header = f"{'Region':<32s}" + "".join(f"{DISPLAY_NAMES[fw]:>12s}" for fw in FRAMEWORKS)
    print(header)
    print("-" * len(header))
    for i, region in enumerate(REGIONS):
        row = f"{region:<32s}" + "".join(f"{int(N[i, j]):>12d}" for j in range(len(FRAMEWORKS)))
        print(row)
    print()

    # --- Run CA ---
    ca = run_ca(N)
    print(f"Total inertia: {ca['total_inertia']:.6f}")
    print(f"Explained variance: Dim1={ca['explained_variance_pct'][0]:.1f}%, "
          f"Dim2={ca['explained_variance_pct'][1]:.1f}%")
    print(f"Singular values: {[f'{s:.4f}' for s in ca['singular_values']]}")
    print()

    # Print coordinates
    print("Row (region) coordinates:")
    for region in REGIONS:
        x, y = ca["row_coords"][region]
        print(f"  {region:<35s} ({x:+.4f}, {y:+.4f})")
    print()
    print("Column (framework) coordinates:")
    for fw in FRAMEWORKS:
        x, y = ca["col_coords"][fw]
        print(f"  {DISPLAY_NAMES[fw]:<20s} ({x:+.4f}, {y:+.4f})")
    print()

    # --- Spot-checks ---
    print("Spot-checks:")
    ssa_coords = np.array(ca["row_coords"]["Sub-Saharan Africa"])
    ubuntu_coords = np.array(ca["col_coords"]["nw_ubuntu"])
    d_ssa_ubuntu = np.linalg.norm(ssa_coords - ubuntu_coords)
    print(f"  Sub-Saharan Africa <-> Ubuntu distance: {d_ssa_ubuntu:.4f}")

    ea_coords = np.array(ca["row_coords"]["East Asia"])
    confucian_coords = np.array(ca["col_coords"]["nw_confucian"])
    d_ea_confucian = np.linalg.norm(ea_coords - confucian_coords)
    print(f"  East Asia <-> Confucian distance: {d_ea_confucian:.4f}")

    mena_coords = np.array(ca["row_coords"]["MENA"])
    islamic_coords = np.array(ca["col_coords"]["nw_islamic_ethics"])
    d_mena_islamic = np.linalg.norm(mena_coords - islamic_coords)
    print(f"  MENA <-> Islamic distance: {d_mena_islamic:.4f}")
    print()

    # --- Generate biplot ---
    make_biplot(ca)

    # --- Write JSON ---
    output = {
        "date": "20260403",
        "method": "correspondence_analysis_svd",
        "n_regions": len(REGIONS),
        "n_frameworks": len(FRAMEWORKS),
        "total_inertia": ca["total_inertia"],
        "explained_variance_pct": ca["explained_variance_pct"],
        "singular_values": ca["singular_values"],
        "row_coords": ca["row_coords"],
        "col_coords": ca["col_coords"],
        "row_coords_display": ca["row_coords_display"],
        "col_coords_display": ca["col_coords_display"],
        "contingency_table": {
            "regions": list(REGIONS),
            "frameworks": list(FRAMEWORKS),
            "counts": N.astype(int).tolist(),
        },
    }
    with open(OUTPUT_JSON, "w") as f:
        json.dump(output, f, indent=2)
    print(f"JSON saved to {OUTPUT_JSON}")
    print("\nDone.")


if __name__ == "__main__":
    main()
