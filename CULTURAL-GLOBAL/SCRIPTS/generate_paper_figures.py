"""Generate all figures for the CULTURAL-GLOBAL paper.

Produces:
  - Figure 1: World map — WEIRD tier choropleth (plotly)
  - Figure 2: Pipeline diagram — values alignment pipeline (matplotlib)
  - Figure 7: WEIRD tier bar chart (Western vs Non-Western scores)
  - Figure 8: WEIRD score distribution histogram
  - Figure 9: Regional WEIRD sub-dimension radar chart
  - Figure 10: Bubble world map — paper count by region, colored by dominant framework (plotly)
  - Figure 11: Non-Western framework detection rates bar chart
  - Figure 12: North/South framework engagement radar

Usage:
    python CULTURAL-GLOBAL/SCRIPTS/generate_paper_figures.py
"""
from __future__ import annotations

import glob
import json
import os
import sys
from collections import Counter, defaultdict

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.ticker as mticker
import numpy as np

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE, "DATA")
FIG_DIR = os.path.join(BASE, "PAPER", "figures")
os.makedirs(FIG_DIR, exist_ok=True)

# Common style
plt.rcParams.update({
    "font.family": "serif",
    "font.size": 11,
    "axes.titlesize": 13,
    "axes.labelsize": 12,
    "figure.facecolor": "white",
    "axes.facecolor": "white",
    "savefig.facecolor": "white",
    "savefig.dpi": 300,
})


def load_json(name: str) -> dict:
    path = os.path.join(DATA_DIR, name)
    if not os.path.exists(path):
        # Fallback: find latest file matching the suffix after the date prefix
        parts = name.split("-", 1)
        suffix = parts[1] if len(parts) > 1 else name
        candidates = sorted(glob.glob(os.path.join(DATA_DIR, f"*-{suffix}")), reverse=True)
        if candidates:
            path = candidates[0]
            print(f"  [fallback] {name}: using {os.path.basename(path)}")
    with open(path) as f:
        return json.load(f)


# ---------------------------------------------------------------------------
# Okabe-Ito colorblind-safe palette (used across figures)
# ---------------------------------------------------------------------------
OKABE_ITO = {
    "orange": "#E69F00",
    "sky_blue": "#56B4E9",
    "green": "#009E73",
    "yellow": "#F0E442",
    "blue": "#0072B2",
    "vermilion": "#D55E00",
    "purple": "#CC79A7",
    "black": "#000000",
}

# Region representative coordinates (lat, lon) for bubble map
REGION_COORDS = {
    "North America": (40.0, -100.0),
    "Western Europe": (48.0, 8.0),
    "East Asia": (35.0, 115.0),
    "MENA": (28.0, 40.0),
    "South Asia": (22.0, 78.0),
    "Southeast Asia": (5.0, 110.0),
    "Latin America & Caribbean": (-15.0, -60.0),
    "Eastern Europe & Central Asia": (50.0, 50.0),
    "Oceania": (-28.0, 145.0),
    "Sub-Saharan Africa": (0.0, 25.0),
}

# Framework display names
NW_DISPLAY = {
    "nw_confucian": "Confucian",
    "nw_ubuntu": "Ubuntu",
    "nw_islamic_ethics": "Islamic",
    "nw_buddhist": "Buddhist",
    "nw_dharmic": "Dharmic",
    "nw_indigenous_relational": "Indigenous",
    "nw_buen_vivir": "Buen Vivir",
}

# Framework colors (Okabe-Ito based)
NW_COLORS = {
    "nw_confucian": "#D55E00",
    "nw_ubuntu": "#009E73",
    "nw_islamic_ethics": "#0072B2",
    "nw_buddhist": "#CC79A7",
    "nw_dharmic": "#F0E442",
    "nw_indigenous_relational": "#E69F00",
    "nw_buen_vivir": "#56B4E9",
}


# ---------------------------------------------------------------------------
# Figure 1: World Map — WEIRD Tier Choropleth (Plotly)
# ---------------------------------------------------------------------------
def fig1_world_map():
    import plotly.express as px
    import plotly.io as pio

    geo = load_json("20260403-author-geography.json")
    ws = load_json("20260403-weird-scores.json")

    # ISO alpha-2 → alpha-3 mapping (plotly choropleth needs alpha-3)
    A2_TO_A3 = {
        "AF": "AFG", "AL": "ALB", "DZ": "DZA", "AO": "AGO", "AR": "ARG",
        "AU": "AUS", "AT": "AUT", "AZ": "AZE", "BH": "BHR", "BD": "BGD",
        "BY": "BLR", "BE": "BEL", "BJ": "BEN", "BT": "BTN", "BO": "BOL",
        "BA": "BIH", "BW": "BWA", "BR": "BRA", "BN": "BRN", "BG": "BGR",
        "BF": "BFA", "KH": "KHM", "CM": "CMR", "CA": "CAN", "CL": "CHL",
        "CN": "CHN", "CO": "COL", "CD": "COD", "CR": "CRI", "CI": "CIV",
        "HR": "HRV", "CU": "CUB", "CY": "CYP", "CZ": "CZE", "DK": "DNK",
        "DO": "DOM", "EC": "ECU", "EG": "EGY", "SV": "SLV", "EE": "EST",
        "ET": "ETH", "FI": "FIN", "FR": "FRA", "GE": "GEO", "DE": "DEU",
        "GH": "GHA", "GR": "GRC", "GT": "GTM", "HN": "HND", "HK": "HKG",
        "HU": "HUN", "IS": "ISL", "IN": "IND", "ID": "IDN", "IR": "IRN",
        "IQ": "IRQ", "IE": "IRL", "IL": "ISR", "IT": "ITA", "JM": "JAM",
        "JP": "JPN", "JO": "JOR", "KZ": "KAZ", "KE": "KEN", "KR": "KOR",
        "KW": "KWT", "LA": "LAO", "LV": "LVA", "LB": "LBN", "LR": "LBR",
        "LY": "LBY", "LT": "LTU", "LU": "LUX", "MO": "MAC", "MG": "MDG",
        "MW": "MWI", "MY": "MYS", "MV": "MDV", "ML": "MLI", "MT": "MLT",
        "MX": "MEX", "MN": "MNG", "MA": "MAR", "MZ": "MOZ", "MM": "MMR",
        "NA": "NAM", "NP": "NPL", "NL": "NLD", "NZ": "NZL", "NI": "NIC",
        "NE": "NER", "NG": "NGA", "NO": "NOR", "OM": "OMN", "PK": "PAK",
        "PS": "PSE", "PA": "PAN", "PY": "PRY", "PE": "PER", "PH": "PHL",
        "PL": "POL", "PT": "PRT", "QA": "QAT", "RO": "ROU", "RU": "RUS",
        "RW": "RWA", "SA": "SAU", "SN": "SEN", "RS": "SRB", "SG": "SGP",
        "SK": "SVK", "SI": "SVN", "SO": "SOM", "ZA": "ZAF", "SS": "SSD",
        "ES": "ESP", "LK": "LKA", "SD": "SDN", "SE": "SWE", "CH": "CHE",
        "SY": "SYR", "TW": "TWN", "TZ": "TZA", "TH": "THA", "TL": "TLS",
        "TG": "TGO", "TN": "TUN", "TR": "TUR", "UG": "UGA", "UA": "UKR",
        "AE": "ARE", "GB": "GBR", "US": "USA", "UY": "URY", "UZ": "UZB",
        "VE": "VEN", "VN": "VNM", "YE": "YEM", "ZM": "ZMB", "ZW": "ZWE",
        "TD": "TCD", "MU": "MUS", "SL": "SLE",
    }

    # Build per-paper WEIRD score lookup
    weird_lookup = {p["filename"]: p["weird_score"] for p in ws["papers"]}

    # Aggregate by country: count and mean WEIRD score
    country_scores = defaultdict(list)
    country_counts = Counter()
    for p in geo["papers"]:
        cc = p.get("author_country", "")
        if not cc or cc == "Unknown":
            continue
        country_counts[cc] += 1
        w = weird_lookup.get(p["filename"], 50)
        country_scores[cc].append(w)

    rows = []
    for cc, scores in country_scores.items():
        cc3 = A2_TO_A3.get(cc, "")
        if not cc3:
            continue
        mean_w = np.mean(scores)
        if mean_w >= 70:
            tier = "High-WEIRD (70-100)"
        elif mean_w >= 50:
            tier = "Moderate-WEIRD (50-69)"
        elif mean_w >= 30:
            tier = "Low-WEIRD (30-49)"
        else:
            tier = "Non-WEIRD (0-29)"
        rows.append({
            "country": cc3,
            "papers": country_counts[cc],
            "mean_weird": round(mean_w, 1),
            "tier": tier,
        })

    tier_order = ["High-WEIRD (70-100)", "Moderate-WEIRD (50-69)",
                  "Low-WEIRD (30-49)", "Non-WEIRD (0-29)"]
    tier_colors = {
        "High-WEIRD (70-100)": "#D55E00",
        "Moderate-WEIRD (50-69)": "#E69F00",
        "Low-WEIRD (30-49)": "#56B4E9",
        "Non-WEIRD (0-29)": "#009E73",
    }

    import pandas as pd
    df = pd.DataFrame(rows)

    fig = px.choropleth(
        df,
        locations="country",
        color="tier",
        hover_name="country",
        hover_data={"papers": True, "mean_weird": True, "tier": False, "country": False},
        category_orders={"tier": tier_order},
        color_discrete_map=tier_colors,
        labels={"tier": "WEIRD Tier", "papers": "Papers", "mean_weird": "Mean WEIRD"},
    )
    fig.update_layout(
        title=dict(text="Figure 1. Geographic Distribution of AI Ethics Papers by WEIRD Score Tier",
                   font=dict(family="serif", size=16)),
        font=dict(family="serif", size=12),
        geo=dict(
            showframe=False,
            showcoastlines=True,
            coastlinecolor="#AAAAAA",
            projection_type="natural earth",
            bgcolor="white",
        ),
        paper_bgcolor="white",
        plot_bgcolor="white",
        legend=dict(
            title_text="WEIRD Tier",
            orientation="h",
            yanchor="bottom",
            y=-0.05,
            xanchor="center",
            x=0.5,
        ),
        margin=dict(l=10, r=10, t=50, b=30),
    )

    out = os.path.join(FIG_DIR, "world-map-weird.png")
    pio.write_image(fig, out, width=1200, height=700, scale=2)
    print(f"  Saved {out}")


# ---------------------------------------------------------------------------
# Figure 2: Pipeline Diagram — Values Alignment Pipeline (Matplotlib)
# ---------------------------------------------------------------------------
def fig2_pipeline_diagram():
    fig, ax = plt.subplots(figsize=(14, 5))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 5)
    ax.axis("off")

    # Pipeline stages
    stages = [
        ("Training\nData", "Cultural composition\nof training corpus"),
        ("Annotator\nDemographics", "WEIRD sampling\nbias in labelers"),
        ("RLHF Reward\nModel", "Whose preferences\ndefine 'good'?"),
        ("Constitutional\nPrinciples", "Which normative\ntraditions included?"),
        ("Evaluation\nBenchmarks", "Whose values\ndefine success?"),
    ]

    box_w, box_h = 2.0, 1.4
    y_box = 2.8
    y_label = 1.3
    gap = 0.8
    x_start = 0.5

    box_color = "#E8EDF3"
    arrow_color = "#4472C4"
    label_color = "#C00000"

    for i, (title, annotation) in enumerate(stages):
        x = x_start + i * (box_w + gap)

        # Box
        rect = mpatches.FancyBboxPatch(
            (x, y_box), box_w, box_h,
            boxstyle="round,pad=0.15",
            facecolor=box_color,
            edgecolor="#2F5496",
            linewidth=1.5,
        )
        ax.add_patch(rect)

        # Title text
        ax.text(x + box_w / 2, y_box + box_h / 2, title,
                ha="center", va="center", fontsize=11, fontweight="bold",
                fontfamily="serif", color="#1A1A1A")

        # Arrow between boxes
        if i < len(stages) - 1:
            ax.annotate(
                "", xy=(x + box_w + gap * 0.15, y_box + box_h / 2),
                xytext=(x + box_w + 0.05, y_box + box_h / 2),
                arrowprops=dict(arrowstyle="-|>", color=arrow_color, lw=2),
            )

        # Annotation below
        ax.annotate(
            annotation,
            xy=(x + box_w / 2, y_box - 0.05),
            xytext=(x + box_w / 2, y_label),
            fontsize=9, fontfamily="serif", color=label_color,
            ha="center", va="top",
            arrowprops=dict(arrowstyle="-", color=label_color, lw=0.8,
                            linestyle="--"),
        )

    # Title
    ax.text(7.0, 4.6, "Figure 2. Values Alignment Pipeline: Where Cultural Values Enter",
            ha="center", va="bottom", fontsize=13, fontweight="bold", fontfamily="serif")

    plt.tight_layout()
    out = os.path.join(FIG_DIR, "pipeline-diagram.png")
    plt.savefig(out, bbox_inches="tight")
    plt.close()
    print(f"  Saved {out}")


# ---------------------------------------------------------------------------
# Figure 10: Bubble World Map — Paper Count by Region (Plotly)
# ---------------------------------------------------------------------------
def fig10_bubble_map():
    import plotly.express as px
    import plotly.io as pio

    ca = load_json("20260403-cross-cultural-analysis.json")
    rp = ca["regional_profiles"]

    nw_keys = list(NW_DISPLAY.keys())

    rows = []
    for region, data in rp.items():
        if region not in REGION_COORDS:
            continue
        lat, lon = REGION_COORDS[region]
        ms = data.get("mean_scores", {})
        n = data.get("n", 0)

        # Dominant NW framework
        dom_key = max(nw_keys, key=lambda k: ms.get(k, 0))
        dom_score = ms.get(dom_key, 0)

        rows.append({
            "region": region,
            "lat": lat,
            "lon": lon,
            "papers": n,
            "dominant_framework": NW_DISPLAY[dom_key],
            "dom_score": round(dom_score, 1),
            "color": NW_COLORS[dom_key],
        })

    import pandas as pd
    df = pd.DataFrame(rows)

    fig = px.scatter_geo(
        df,
        lat="lat",
        lon="lon",
        size="papers",
        color="dominant_framework",
        hover_name="region",
        hover_data={"papers": True, "dom_score": True, "lat": False, "lon": False,
                    "dominant_framework": False},
        size_max=50,
        color_discrete_map={NW_DISPLAY[k]: NW_COLORS[k] for k in nw_keys},
        labels={"dominant_framework": "Dominant NW Framework", "dom_score": "Mean Score"},
    )

    fig.update_layout(
        title=dict(
            text="Figure 10. Geographic Distribution of AI Ethics Research by Dominant Non-Western Framework",
            font=dict(family="serif", size=14),
        ),
        font=dict(family="serif", size=12),
        geo=dict(
            showframe=False,
            showcoastlines=True,
            coastlinecolor="#AAAAAA",
            projection_type="natural earth",
            bgcolor="white",
            showland=True,
            landcolor="#F0F0F0",
        ),
        paper_bgcolor="white",
        plot_bgcolor="white",
        legend=dict(
            title_text="Dominant NW Framework",
            orientation="h",
            yanchor="bottom",
            y=-0.05,
            xanchor="center",
            x=0.5,
        ),
        margin=dict(l=10, r=10, t=50, b=30),
    )

    out = os.path.join(FIG_DIR, "bubble-world-map.png")
    pio.write_image(fig, out, width=1200, height=700, scale=2)
    print(f"  Saved {out}")


# ---------------------------------------------------------------------------
# Figure 7: WEIRD Tier Bar Chart
# ---------------------------------------------------------------------------
def fig4_weird_tier_bars():
    ca = load_json("20260403-cross-cultural-analysis.json")
    weird = ca["weird_comparison"]

    tiers = ["High-WEIRD (70-100)", "Moderate-WEIRD (50-69)",
             "Low-WEIRD (30-49)", "Non-WEIRD (0-29)"]
    tier_labels = ["High-WEIRD\n(70-100)", "Moderate-WEIRD\n(50-69)",
                   "Low-WEIRD\n(30-49)", "Non-WEIRD\n(0-29)"]

    western_keys = ["virtue_ethics", "deontological_ethics", "utilitarian_ethics",
                    "care_ethics", "contractarian_ethics"]
    nw_keys = ["nw_confucian", "nw_ubuntu", "nw_islamic_ethics",
               "nw_buddhist", "nw_dharmic", "nw_indigenous_relational", "nw_buen_vivir"]

    mean_west = []
    mean_nw = []
    for tier in tiers:
        td = weird.get(tier, {})
        means = td.get("mean_scores", {})
        w_vals = [means.get(k, 0) for k in western_keys]
        nw_vals = [means.get(k, 0) for k in nw_keys]
        mean_west.append(np.mean(w_vals) if w_vals else 0)
        mean_nw.append(np.mean(nw_vals) if nw_vals else 0)

    x = np.arange(len(tiers))
    width = 0.35

    fig, ax = plt.subplots(figsize=(10, 6))
    bars1 = ax.bar(x - width/2, mean_west, width, label="Western Frameworks",
                   color="#4472C4", edgecolor="white", linewidth=0.5)
    bars2 = ax.bar(x + width/2, mean_nw, width, label="Non-Western Frameworks",
                   color="#ED7D31", edgecolor="white", linewidth=0.5)

    ax.set_xlabel("WEIRD Tier")
    ax.set_ylabel("Mean Framework Score")
    ax.set_title("Figure 4. Western vs Non-Western Framework Engagement by WEIRD Tier")
    ax.set_xticks(x)
    ax.set_xticklabels(tier_labels)
    ax.legend()
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    # Value labels
    for bar in bars1:
        h = bar.get_height()
        if h > 0.05:
            ax.text(bar.get_x() + bar.get_width()/2, h + 0.03, f"{h:.2f}",
                    ha="center", va="bottom", fontsize=9)
    for bar in bars2:
        h = bar.get_height()
        if h > 0.05:
            ax.text(bar.get_x() + bar.get_width()/2, h + 0.03, f"{h:.2f}",
                    ha="center", va="bottom", fontsize=9)

    plt.tight_layout()
    out = os.path.join(FIG_DIR, "weird-tier-bars.png")
    plt.savefig(out)
    plt.close()
    print(f"  Saved {out}")


# ---------------------------------------------------------------------------
# Figure 6: WEIRD Score Histogram
# ---------------------------------------------------------------------------
def fig6_weird_histogram():
    ws = load_json("20260403-weird-scores.json")
    scores = [p["weird_score"] for p in ws["papers"]]

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.hist(scores, bins=20, range=(0, 100), color="#4472C4", edgecolor="white",
            linewidth=0.5, alpha=0.85)

    # Tier boundaries
    for boundary, label in [(30, "Non/Low"), (50, "Low/Mod"), (70, "Mod/High")]:
        ax.axvline(boundary, color="#C00000", linestyle="--", linewidth=1.2, alpha=0.7)
        ax.text(boundary + 1, ax.get_ylim()[1] * 0.92, label,
                fontsize=9, color="#C00000", rotation=0)

    # Mean line
    mean_val = np.mean(scores)
    ax.axvline(mean_val, color="#2F5496", linestyle="-", linewidth=2, alpha=0.8)
    ax.text(mean_val + 1, ax.get_ylim()[1] * 0.82, f"Mean = {mean_val:.1f}",
            fontsize=10, color="#2F5496", fontweight="bold")

    ax.set_xlabel("WEIRD Score (0-100)")
    ax.set_ylabel("Number of Papers")
    ax.set_title("Figure 6. Distribution of WEIRD Scores Across 2,046 AI Ethics Papers")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.tight_layout()
    out = os.path.join(FIG_DIR, "weird-histogram.png")
    plt.savefig(out)
    plt.close()
    print(f"  Saved {out}")


# ---------------------------------------------------------------------------
# Figure 7: Regional WEIRD Sub-Dimension Radar
# ---------------------------------------------------------------------------
def fig7_regional_radar():
    ws = load_json("20260403-weird-scores.json")

    # Group papers by region
    geo = load_json("20260403-author-geography.json")
    country_to_region = {}
    if "region_mapping" in geo:
        country_to_region = geo["region_mapping"]
    elif "papers" in geo:
        for p in geo["papers"]:
            cc = p.get("author_country", "")
            reg = p.get("macro_region", "Unknown")
            if cc:
                country_to_region[cc] = reg

    # Build paper-level region lookup from geo papers
    paper_regions = {}
    if "papers" in geo:
        for p in geo["papers"]:
            paper_regions[p.get("filename", "")] = p.get("macro_region", "Unknown")

    regions_of_interest = [
        "North America", "Western Europe", "East Asia", "MENA", "South Asia"
    ]
    dims = ["w", "e", "i", "r", "d"]
    dim_labels = ["Western", "Educated", "Industrialized", "Rich", "Democratic"]

    region_scores = {r: {d: [] for d in dims} for r in regions_of_interest}

    for p in ws["papers"]:
        fn = p.get("filename", "")
        region = paper_regions.get(fn, "Unknown")
        if region in region_scores:
            for d in dims:
                region_scores[region][d].append(p.get(d, 0))

    # Compute means
    region_means = {}
    for r in regions_of_interest:
        region_means[r] = [np.mean(region_scores[r][d]) if region_scores[r][d] else 0
                           for d in dims]

    # Radar chart
    angles = np.linspace(0, 2 * np.pi, len(dims), endpoint=False).tolist()
    angles += angles[:1]

    colors = ["#4472C4", "#ED7D31", "#A5A5A5", "#FFC000", "#5B9BD5"]

    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
    for idx, region in enumerate(regions_of_interest):
        values = region_means[region] + [region_means[region][0]]
        ax.plot(angles, values, "o-", linewidth=2, label=region, color=colors[idx])
        ax.fill(angles, values, alpha=0.08, color=colors[idx])

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(dim_labels, fontsize=11)
    ax.set_ylim(0, 20)
    ax.set_yticks([5, 10, 15, 20])
    ax.set_yticklabels(["5", "10", "15", "20"], fontsize=9)
    ax.set_title("Figure 7. WEIRD Sub-Dimension Profiles by Region", pad=20)
    ax.legend(loc="upper right", bbox_to_anchor=(1.3, 1.1), fontsize=10)

    plt.tight_layout()
    out = os.path.join(FIG_DIR, "weird-radar.png")
    plt.savefig(out, bbox_inches="tight")
    plt.close()
    print(f"  Saved {out}")


# ---------------------------------------------------------------------------
# Figure 9: Non-Western Framework Detection Rates
# ---------------------------------------------------------------------------
def fig9_nw_detection_bars():
    nw = load_json("20260403-nw-scores.json")
    counts = nw["field_counts_gte50"]
    total = nw["total_papers"]

    frameworks = [
        ("nw_confucian", "Confucian"),
        ("nw_indigenous_relational", "Indigenous\nRelational"),
        ("nw_ubuntu", "Ubuntu"),
        ("nw_islamic_ethics", "Islamic\nJurisprudence"),
        ("nw_buddhist", "Buddhist"),
        ("nw_dharmic", "Dharmic"),
        ("nw_buen_vivir", "Buen Vivir"),
    ]

    names = [f[1] for f in frameworks]
    vals = [counts.get(f[0], 0) for f in frameworks]
    pcts = [v / total * 100 for v in vals]

    fig, ax = plt.subplots(figsize=(10, 6))
    colors_list = ["#C00000", "#4472C4", "#548235", "#ED7D31",
                   "#7030A0", "#FFC000", "#44546A"]
    bars = ax.bar(range(len(names)), vals, color=colors_list, edgecolor="white",
                  linewidth=0.5)

    for bar, pct, val in zip(bars, pcts, vals):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
                f"{val}\n({pct:.1f}%)", ha="center", va="bottom", fontsize=9)

    ax.set_xticks(range(len(names)))
    ax.set_xticklabels(names, fontsize=10)
    ax.set_ylabel("Number of Papers (score >= 50)")
    ax.set_title("Figure 9. Non-Western Framework Detection Rates (N = 2,046)")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.tight_layout()
    out = os.path.join(FIG_DIR, "nw-detection-bars.png")
    plt.savefig(out)
    plt.close()
    print(f"  Saved {out}")


# ---------------------------------------------------------------------------
# Figure 10: North/South Framework Engagement Radar
# ---------------------------------------------------------------------------
def fig10_north_south_radar():
    ca = load_json("20260403-cross-cultural-analysis.json")
    ns = ca.get("north_south_comparison", {})

    if not ns:
        print("  SKIP: north_south_comparison not in data")
        return

    fw_labels = ["Utilitarian", "Deontological", "Virtue", "Care",
                 "Contractarian", "Confucian", "Ubuntu", "Islamic Juris.",
                 "Indigenous Rel."]
    fw_keys = ["utilitarian_ethics", "deontological_ethics", "virtue_ethics",
               "care_ethics", "contractarian_ethics",
               "nw_confucian", "nw_ubuntu", "nw_islamic_ethics",
               "nw_indigenous_relational"]

    groups = ["Global North", "Global South"]
    group_data = {}
    for g in groups:
        gd = ns.get(g, {})
        means = gd.get("mean_scores", {})
        group_data[g] = [means.get(k, 0) for k in fw_keys]

    if not any(any(v > 0 for v in group_data[g]) for g in groups):
        print("  SKIP: no non-zero data for North/South radar")
        return

    angles = np.linspace(0, 2 * np.pi, len(fw_labels), endpoint=False).tolist()
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(9, 9), subplot_kw=dict(polar=True))
    colors_ns = {"Global North": "#4472C4", "Global South": "#ED7D31"}

    for g in groups:
        values = group_data[g] + [group_data[g][0]]
        ax.plot(angles, values, "o-", linewidth=2, label=g, color=colors_ns[g])
        ax.fill(angles, values, alpha=0.1, color=colors_ns[g])

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(fw_labels, fontsize=10)
    ax.set_title("Figure 10. Framework Engagement: Global North vs Global South", pad=20)
    ax.legend(loc="upper right", bbox_to_anchor=(1.3, 1.1), fontsize=10)

    plt.tight_layout()
    out = os.path.join(FIG_DIR, "north-south-radar.png")
    plt.savefig(out, bbox_inches="tight")
    plt.close()
    print(f"  Saved {out}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    print("Generating paper figures...")
    fig1_world_map()
    fig2_pipeline_diagram()
    fig4_weird_tier_bars()
    fig6_weird_histogram()
    fig7_regional_radar()
    fig9_nw_detection_bars()
    fig10_north_south_radar()
    fig10_bubble_map()
    print("Done.")


if __name__ == "__main__":
    main()
