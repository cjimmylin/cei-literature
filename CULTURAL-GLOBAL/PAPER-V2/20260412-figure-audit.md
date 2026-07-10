# Figure Audit Report — CULTURAL-GLOBAL PAPER-V2

**Date:** 2026-04-12
**Auditor Perspectives:** P1 (Scientific Figure Design), P5 (Color Science & Accessibility), P8 (Typography & Layout)
**Scope:** 10 main figures + 7 supplementary figures (17 total)

---

## 1. Per-Figure Inventory and DPI/Dimension Audit

### Main Figures (`PAPER-V2/figures/`)

| # | Filename | Current DPI | Pixel W x H | Physical Size (in) | Target DPI | Target Width | Action Needed |
|---|----------|-------------|-------------|---------------------|------------|-------------|---------------|
| 1 | `world-map-weird.png` | 72 | 2400 x 1400 | 33.3 x 19.4 | 300 (halftone) | Double (7.09in) | **CRITICAL:** DPI=72 is unpublishable. Regenerate at 300 DPI via Plotly `scale=` parameter. Physical size is absurd at 72 DPI. |
| 2 | `heatmap-regions-frameworks.png` | 150 | 1936 x 1181 | 12.9 x 7.9 | 300 (halftone) | Double (7.09in) | DPI too low. Regenerate at 300 DPI. Width at target = 2126 px, currently adequate if DPI is corrected. |
| 3 | `dendrogram.png` | 150 | 1781 x 1033 | 11.9 x 6.9 | 600 (line art) | Double (7.09in) | DPI too low for line art. Regenerate at 600 DPI. |
| 4 | `correspondence-biplot.png` | 300 | 3543 x 2964 | 11.8 x 9.9 | 300 (halftone) | Double (7.09in) | DPI OK. Oversized physically -- trim to 7.09 x 5.9in at 300 DPI (2126 x 1772 px). |
| 5 | `benchmark-landscape-clusters.png` | 200 | 2366 x 1100 | 11.8 x 5.5 | 300 (halftone) | Double (7.09in) | DPI too low. Regenerate at 300 DPI. Donut + bars = double-width appropriate. |
| 6 | `concept-coverage-gaps.png` | 200 | 2000 x 1000 | 10.0 x 5.0 | 600 (line art) | Double (7.09in) | DPI too low for bar chart (line art). Regenerate at 600 DPI. |
| 7 | `cultural-map-position.png` | 200 | 1584 x 1600 | 7.9 x 8.0 | 300 (halftone) | Single (3.46in) | DPI too low. Regenerate at 300 DPI. Near-square aspect ratio suits single column. |
| 8 | `mfq-profile-comparison.png` | 200 | 2000 x 1200 | 10.0 x 6.0 | 300 (halftone) | Double (7.09in) | DPI too low. Regenerate at 300 DPI. 4-group comparison needs width. |
| 9 | `rlhf-conflict-taxonomy.png` | 200 | 2585 x 1100 | 12.9 x 5.5 | 300 (halftone) | Double (7.09in) | DPI too low. Regenerate at 300 DPI. Dual-panel layout requires double width. |
| 10 | `triple-bind-diagram.png` | 200 | 1390 x 1374 | 6.95 x 6.87 | 600 (line art) | Single (3.46in) | DPI too low. Must be completely redesigned (see Section 5). |

### Supplementary Figures (`PAPER-V2/supplementary/supp-figures/`)

| # | Filename | Current DPI | Pixel W x H | Physical Size (in) | Target DPI | Target Width | Action Needed |
|---|----------|-------------|-------------|---------------------|------------|-------------|---------------|
| S1 | `bubble-world-map.png` | 72 | 2400 x 1400 | 33.3 x 19.4 | 300 (halftone) | Double (7.09in) | **CRITICAL:** DPI=72. Same Plotly issue as Fig 1. Regenerate. |
| S2 | `weird-histogram.png` | 300 | 3000 x 1800 | 10.0 x 6.0 | 300 (halftone) | Single (3.46in) | DPI OK. Physically oversized; set figsize to (3.46, 2.1). |
| S3 | `weird-radar.png` | 300 | 2353 x 1997 | 7.8 x 6.7 | 300 (halftone) | Single (3.46in) | DPI OK. Physically oversized; reduce figsize. |
| S4 | `pipeline-diagram.png` | 300 | 4161 x 1460 | 13.9 x 4.9 | 600 (line art) | Double (7.09in) | DPI should be 600 for line art. Very wide -- OK for double column landscape. |
| S5 | `nw-detection-bars.png` | 300 | 3000 x 1800 | 10.0 x 6.0 | 600 (line art) | Double (7.09in) | DPI should be 600 for bar chart. |
| S6 | `north-south-radar.png` | 300 | 2617 x 2161 | 8.7 x 7.2 | 300 (halftone) | Single (3.46in) | DPI OK. Physically oversized; reduce figsize. |
| S7 | `silhouette.png` | 150 | 1185 x 733 | 7.9 x 4.9 | 600 (line art) | Single (3.46in) | **DPI too low.** Regenerate at 600 DPI. Very small pixel count. |

**Summary:** 0 of 17 figures meet publication DPI requirements at correct physical dimensions. 2 figures are at critically low 72 DPI (Plotly-generated maps). 4 figures are at 150 DPI. 6 figures are at 200 DPI. Only 5 figures are at 300 DPI but most are physically oversized.

---

## 2. Font Verification

| Font | Resolved Path | Status |
|------|--------------|--------|
| Arial | `/System/Library/Fonts/Supplemental/Arial.ttf` | OK -- resolves to `.ttf` (not `.ttc`). Safe for matplotlib embedding. |
| Helvetica | `/System/Library/Fonts/Helvetica.ttc` | **WARNING:** Resolves to `.ttc` (TrueType Collection). Matplotlib cannot reliably embed `.ttc` fonts in PDF/EPS output. Avoid Helvetica; use Arial instead. |
| DejaVu Sans | `.venv/.../DejaVuSans.ttf` | OK -- matplotlib bundled fallback. |

**Recommendation:** Standardize all figures on `Arial` (`.ttf`, properly embeddable). The legacy script uses `font.family: serif` which will fall back to DejaVu Serif -- inconsistent with the `sans-serif` used by `generate_new_figures.py`. All figures must use the same font family for visual coherence.

**Font size audit (`generate_new_figures.py`):**

| Element | Current Size | Target for Print |
|---------|-------------|-----------------|
| Base font | 10 pt | 7-8 pt at single-col; OK at double-col |
| Axis title | 12 pt | 9-10 pt at single-col; OK at double-col |
| Axis labels | 11 pt | 8-9 pt at single-col; OK at double-col |
| Tick labels | 9 pt | 7 pt minimum |
| Legend | 9 pt | 7 pt minimum |

All font sizes are defined for screen viewing at physical sizes of 10-13 inches. When scaled to 3.46-7.09 inches for print, effective sizes will be roughly halved. Current sizes are acceptable for double-column figures but will need increase for single-column figures to remain legible at ~50% reduction.

---

## 3. Generation Script Analysis

### 3.1 `generate_new_figures.py` (Figs 5-10)

| Property | Value |
|----------|-------|
| **Location** | `PAPER-V2/generate_new_figures.py` |
| **Generates** | Figs 5 (benchmark clusters), 6 (concept coverage), 7 (cultural map), 8 (MFQ profiles), 9 (RLHF conflicts), 10 (triple bind) |
| **DPI** | `figure.dpi: 200` (global rcParams) -- no per-savefig DPI override |
| **Background** | `figure.facecolor: "white"`, `axes.facecolor: "#fafafa"` |
| **Palette** | Okabe-Ito colorblind-safe (8 colors) |
| **Font** | `sans-serif` family, base size 10 |
| **Data dependencies** | **None** -- all data is hardcoded inline. Figures are static/illustrative. |
| **Can run standalone?** | Yes -- no external file reads. |

**Per-figure details:**

| Fig | Function | figsize | Colormap/Palette | Special Notes |
|-----|----------|---------|-----------------|---------------|
| 5 | `fig5_benchmark_clusters()` | (12, 5.5) | OI vermillion + sky | Donut (left) + grouped bars (right). `width_ratios=[1, 1.4]`. |
| 6 | `fig6_concept_coverage()` | (10, 5) | OI green + vermillion | Stacked horizontal bars. `alpha=0.7` on unmeasured bars. |
| 7 | `fig7_cultural_map()` | (9, 8) | OI blue + vermillion | Scatter + quadrant shading. `aspect="equal"`. Square. |
| 8 | `fig8_mfq_profiles()` | (10, 6) | OI vermillion/sky/blue/green | 4-group grouped bar chart. |
| 9 | `fig9_rlhf_conflicts()` | (13, 5.5) | 6-color OI subset + ListedColormap heatmap | Dual panel: bars (left) + impact heatmap (right). `width_ratios=[1.3, 1]`. |
| 10 | `fig10_triple_bind()` | (10, 8) | OI vermillion/orange/blue | Diagram: 3 circles + curved arrows. No axes. |

### 3.2 `SCRIPTS/generate_paper_figures.py` (Legacy -- Figs 1, S1-S7)

| Property | Value |
|----------|-------|
| **Location** | `CULTURAL-GLOBAL/SCRIPTS/generate_paper_figures.py` |
| **Generates** | 8 functions: `fig1_world_map`, `fig2_pipeline_diagram`, `fig4_weird_tier_bars`, `fig6_weird_histogram`, `fig7_regional_radar`, `fig9_nw_detection_bars`, `fig10_north_south_radar`, `fig10_bubble_map` |
| **DPI** | `savefig.dpi: 300` (rcParams). Plotly figures use `scale=2` at `width=1200, height=700` = 2400x1400 px at 72 DPI metadata. |
| **Background** | `figure.facecolor: "white"`, `axes.facecolor: "white"` (no `#fafafa`) |
| **Palette** | Okabe-Ito palette defined but NOT used consistently -- some functions use Office-style colors (`#4472C4`, `#ED7D31`, `#C00000`, `#2F5496`). |
| **Font** | `serif` family, base size 11 |
| **Output directory** | Hardcoded to `CULTURAL-GLOBAL/PAPER/figures/` (old PAPER dir, NOT PAPER-V2) |

**Data file dependencies:**

| Data File | Used By | Exists? |
|-----------|---------|---------|
| `20260403-author-geography.json` | `fig1_world_map()`, `fig7_regional_radar()` | Yes |
| `20260403-weird-scores.json` | `fig1_world_map()`, `fig6_weird_histogram()`, `fig7_regional_radar()` | Yes |
| `20260403-cross-cultural-analysis.json` | `fig4_weird_tier_bars()`, `fig10_north_south_radar()`, `fig10_bubble_map()` | Yes |
| `20260403-nw-scores.json` | `fig9_nw_detection_bars()` | Yes |

**Additional Python dependencies:** `plotly`, `pandas`, `numpy`, `matplotlib` -- all available in `.venv`.

**Can it run with current paths?** No -- output path `PAPER/figures/` differs from current `PAPER-V2/figures/`. The `FIG_DIR` must be updated. Also, the function-to-figure-number mapping in the legacy script does NOT match the PAPER-V2 numbering. The legacy script's internal numbering (Fig 1, 2, 4, 6, 7, 9, 10) reflects an earlier paper structure.

**Mapping: legacy script function to current PAPER-V2 figure assignment:**

| Legacy Function | Legacy Label | PAPER-V2 Assignment | Current Filename |
|----------------|-------------|---------------------|------------------|
| `fig1_world_map()` | Figure 1 | Fig 1 (main) | `world-map-weird.png` |
| `fig2_pipeline_diagram()` | Figure 2 | Fig S4 (supplementary) | `pipeline-diagram.png` |
| `fig4_weird_tier_bars()` | Figure 4 | Not currently in PAPER-V2 figures | -- |
| `fig6_weird_histogram()` | Figure 6 | Fig S2 (supplementary) | `weird-histogram.png` |
| `fig7_regional_radar()` | Figure 7 | Fig S3 (supplementary) | `weird-radar.png` |
| `fig9_nw_detection_bars()` | Figure 9 | Fig S5 (supplementary) | `nw-detection-bars.png` |
| `fig10_north_south_radar()` | Figure 10 | Fig S6 (supplementary) | `north-south-radar.png` |
| `fig10_bubble_map()` | Figure 10b | Fig S1 (supplementary) | `bubble-world-map.png` |

**Data-driven figures from other sources (Figs 2-4):**

| Fig | Filename | Likely Generator | Notes |
|-----|----------|-----------------|-------|
| 2 | `heatmap-regions-frameworks.png` | Unknown (possibly R or manual) | 150 DPI suggests manual export. |
| 3 | `dendrogram.png` | Unknown | 150 DPI, likely from clustering analysis script. |
| 4 | `correspondence-biplot.png` | Unknown | 300 DPI, likely from correspondence analysis script. |
| S7 | `silhouette.png` | Unknown | 150 DPI, from clustering validation. |

---

## 4. Grayscale and Colorblind Risk Assessment

### 4.1 Colorblind Safety

| Fig | Palette Used | Colorblind Safe? | Risk Areas |
|-----|-------------|-----------------|------------|
| 1 | Vermillion/Orange/Sky/Green tier colors | **MODERATE RISK** -- orange (#E69F00) and vermillion (#D55E00) are close for deuteranopia. | Tier boundaries on choropleth. |
| 2 | Blue/grey heatmap | LOW RISK | Continuous scale is generally safe. |
| 3 | Default matplotlib dendrogram colors | **HIGH RISK** -- matplotlib default colors are NOT colorblind-safe. | Branch coloring. |
| 4 | Unknown | UNKNOWN -- need to inspect | Biplot markers/labels. |
| 5 | OI vermillion + sky | LOW RISK -- high contrast pair. | Safe. |
| 6 | OI green + vermillion | LOW RISK -- OI pair designed for this. | Safe. |
| 7 | OI blue (scatter) + vermillion (Claude) | LOW RISK | Safe. Two-color scheme with high separation. |
| 8 | OI vermillion/sky/blue/green (4 groups) | LOW RISK -- full OI palette. | Safe. |
| 9 | 6 OI colors + 3-level ListedColormap | **MODERATE RISK** -- the ListedColormap uses `#f0f0f0`, orange, vermillion. Orange/vermillion distinction poor for deuteranopia. | Impact heatmap (right panel). Cell text labels ("med"/"high") mitigate this. |
| 10 | OI vermillion/orange/blue | **MODERATE RISK** -- vermillion and orange overlap for CVD. | Circle borders and fills. |
| S1 | 7 NW framework colors (mixed OI + custom) | **HIGH RISK** -- 7 categories on a map with some non-OI colors. Yellow on white background is near-invisible. | Bubble colors on white landmass. |
| S2 | Single blue | LOW RISK | Histogram, one color. |
| S3 | 5 Office-style colors | **HIGH RISK** -- uses `#4472C4`, `#ED7D31`, `#A5A5A5`, `#FFC000`, `#5B9BD5`. Several overlap under CVD. | 5 overlapping radar traces. |
| S4 | Blue/grey boxes | LOW RISK | Diagram. |
| S5 | 7 custom colors (non-OI) | **HIGH RISK** -- `#C00000`, `#4472C4`, `#548235`, `#ED7D31`, `#7030A0`, `#FFC000`, `#44546A` are NOT colorblind-safe. | 7-bar chart, several colors confusable. |
| S6 | 2 Office colors | LOW RISK -- just blue vs orange. | Two-trace radar. |
| S7 | Unknown | UNKNOWN | Silhouette plot. |

### 4.2 Grayscale Viability

| Fig | Grayscale Viable? | Issue |
|-----|-------------------|-------|
| 1 (choropleth) | **NO** -- 4 tiers rely entirely on color hue. | Add crosshatch/pattern fills for tiers. |
| 2 (heatmap) | PARTIAL -- intensity differences may survive. | Add value annotations in cells. |
| 3 (dendrogram) | **NO** -- branch colors distinguish clusters. | Add cluster labels at leaf level. |
| 5 (clusters) | PARTIAL -- donut distinguishable by position; bars need hatching. | Add hatch patterns to one group. |
| 6 (coverage) | YES -- stacked bars with high luminance contrast (green vs red-orange). | Green is darker than vermillion in grayscale. Acceptable. |
| 7 (cultural map) | YES -- scatter points are all same color; Claude star is distinct marker shape. | OK. |
| 8 (MFQ) | **NO** -- 4 groups distinguished only by color. | Add hatch patterns to bars. |
| 9 (RLHF) | PARTIAL -- bars have different luminances; heatmap uses 3 levels with text labels. | Text labels save the heatmap. Bars need hatching. |
| 10 (triple bind) | **NO** -- 3 circles distinguished by color only. | Add different line styles (solid/dashed/dotted) to circle borders. |

---

## 5. Fig 10 Redesign: Triple-Bind Mechanism Diagram

### 5.1 Problem Statement

The current Fig 10 is three overlapping circles with curved arrows -- essentially a Venn diagram with flow arrows. This is visually simplistic and does not convey the **mechanistic, self-reinforcing** nature of the triple bind. For a top-tier journal, the diagram must communicate:
1. Three distinct layers (Scholarship, Benchmarks, Models)
2. The causal chain linking them
3. The feedback loop (cycle, not linear)
4. Specific mechanisms at each transition point
5. The compounding/amplifying nature of the bias

### 5.2 Proposed Wireframe: Layered Feedback-Loop Architecture

**Layout: Triangular flow diagram with mechanism boxes on edges**

```
                    +---------------------------+
                    |    WEIRD SCHOLARSHIP      |
                    |  [rounded rect, #D55E00]  |
                    |                           |
                    |  60.1% N.Am + W.Eur       |
                    |  6.9% NW engagement       |
                    |  Mean WEIRD: 64.5         |
                    +---------------------------+
                   /  ^                       \  |
                  /    \                       v  \
    [mechanism   /      \  [mechanism          \   [mechanism
     box A]     /        \  box C]              \   box B]
               /          \                      \
              v            \                      v
+------------------+        \        +------------------+
| BROKEN           |         \       | MONOCULTURAL     |
| BENCHMARKS       |          \      | MODELS           |
| [rounded rect,   |           \     | [rounded rect,   |
|  #E69F00]        |            \    |  #0072B2]        |
|                  |             \   |                  |
| 0/218 meas. inv. |              \  | I:B ratio 3.75  |
| 6.8% concepts    |               \ | 100% Western    |
| 55.5% W-created  |                \| 92.5% know. gap |
+------------------+                 +------------------+
                    \               /
                     \             /
                      \  [mech.  /
                       \ box D] /
                        \      /
                         v    /
                    [AMPLIFICATION
                      ZONE - center]
```

**Detailed specification for matplotlib implementation:**

**A. Three node boxes (rounded rectangles):**

| Node | Position (figure coords) | Size | Fill | Border |
|------|-------------------------|------|------|--------|
| SCHOLARSHIP | center-top: (5.0, 7.5) | 3.5 x 2.2 in | `#D55E00` at alpha=0.12 | `#D55E00`, linewidth=2.5, rounded (`boxstyle="round,pad=0.3"`) |
| BENCHMARKS | bottom-left: (1.5, 1.5) | 3.5 x 2.2 in | `#E69F00` at alpha=0.12 | `#E69F00`, linewidth=2.5 |
| MODELS | bottom-right: (8.5, 1.5) | 3.5 x 2.2 in | `#0072B2` at alpha=0.12 | `#0072B2`, linewidth=2.5 |

Each box contains:
- Line 1: Node title (12pt, bold, node color)
- Lines 2-4: Three key statistics (8pt, `#333333`, line-spacing 1.4)

**B. Three mechanism edge-boxes (pill-shaped, on the arrows):**

| Edge | Position | Label | Mechanism Text |
|------|----------|-------|---------------|
| A: Scholarship -> Benchmarks | midpoint of left diagonal | "CONSTRUCT SELECTION" | "Western frameworks define what to measure" |
| B: Benchmarks -> Models | midpoint of bottom edge | "ALIGNMENT TARGET" | "RLHF optimizes for WEIRD-normed benchmarks" |
| C: Models -> Scholarship | midpoint of right diagonal | "NORMATIVE FEEDBACK" | "Model outputs reinforce dominant vocabulary" |

Each mechanism box:
- Size: 2.5 x 0.9 in
- Fill: `#f5f5f5`
- Border: `#888888`, linewidth=1.0, dashed
- Title: 8pt bold, `#333333`
- Subtitle: 7pt italic, `#666666`

**C. Arrows (thick, directional):**

Three arrows forming a clockwise cycle:
- Style: `FancyArrowPatch` with `arrowstyle="Simple,tail_width=4,head_width=14,head_length=10"`
- Color: `#444444`
- Each arrow curves slightly outward (connectionstyle=`arc3,rad=0.15`)
- Arrow path: Scholarship bottom-left corner -> Benchmarks top; Benchmarks right -> Models left; Models top-right corner -> Scholarship bottom-right

**D. Center amplification indicator:**

- Position: centroid of triangle (5.0, 3.5)
- Content: A small "amplification spiral" icon (concentric arcs) OR text box
- Text: "AMPLIFICATION\nCYCLE" (11pt bold, `#CC0000`)
- Subtitle: "Each layer inherits and\namplifies the monoculture\nof the layer before it" (7pt italic, `#666666`)
- Background: white with subtle red border, `boxstyle="round,pad=0.4"`

**E. Overall figure:**

- `figsize=(10, 9)` for double-column width
- `ax.set_xlim(0, 10)`, `ax.set_ylim(0, 10)`
- `ax.axis("off")`
- Title: "The Triple Bind: Self-Reinforcing WEIRD Bias Across Three Layers" (13pt bold, pad=20)
- DPI: 600 (line art)

**F. Visual hierarchy (reading order):**

1. Three large colored boxes draw the eye to the nodes (highest visual weight)
2. Thick arrows establish the flow direction
3. Mechanism boxes on edges explain the causal links
4. Center amplification indicator conveys the compounding nature

---

## 6. Target Width Assignments

| Fig | Content Type | Recommended Width | Rationale |
|-----|-------------|-------------------|-----------|
| 1 | Choropleth world map | Double (7.09in / 180mm) | Geographic detail requires width |
| 2 | Heatmap (regions x frameworks) | Double (7.09in / 180mm) | Many columns need horizontal space |
| 3 | Dendrogram | Double (7.09in / 180mm) | Leaf labels need legibility |
| 4 | Correspondence biplot | Double (7.09in / 180mm) | Scatter with many labeled points |
| 5 | Donut + grouped bars (2 panels) | Double (7.09in / 180mm) | Dual panel |
| 6 | Horizontal stacked bars | Double (7.09in / 180mm) | 7 tradition labels + annotations |
| 7 | Scatter plot (cultural map) | Single (3.46in / 88mm) | Square aspect, few data points; single-col focuses attention |
| 8 | 4-group grouped bars | Double (7.09in / 180mm) | 5 x 4 = 20 bars need width |
| 9 | Bars + heatmap (2 panels) | Double (7.09in / 180mm) | Dual panel |
| 10 | Mechanism diagram | Double (7.09in / 180mm) | Complex diagram needs space (after redesign) |
| S1 | Bubble world map | Double (7.09in / 180mm) | Geographic detail |
| S2 | Histogram | Single (3.46in / 88mm) | Simple 1D distribution |
| S3 | Radar chart (5 regions) | Single (3.46in / 88mm) | Circular, compact |
| S4 | Pipeline diagram | Double (7.09in / 180mm) | 5 sequential boxes need horizontal space |
| S5 | Bar chart (7 bars) | Double (7.09in / 180mm) | 7 categories with percentage labels |
| S6 | Radar chart (2 groups) | Single (3.46in / 88mm) | Circular, compact |
| S7 | Silhouette plot | Single (3.46in / 88mm) | Simple diagnostic plot |

---

## 7. CMYK Conversion Notes

### Color space issues

1. **Okabe-Ito palette:** All colors are defined in sRGB hex. For CMYK conversion:
   - `#E69F00` (orange) converts cleanly
   - `#56B4E9` (sky blue) converts cleanly
   - `#009E73` (green) -- **GAMUT WARNING:** This saturated green may shift in CMYK. Preview in CMYK and consider desaturating slightly.
   - `#D55E00` (vermillion) converts cleanly
   - `#F0E442` (yellow) -- **LOW CONTRAST WARNING:** Very light yellow will be nearly invisible on white paper in CMYK.

2. **Background `#fafafa`:** This extremely light grey (RGB 250,250,250) will be **indistinguishable from white** in CMYK printing. Either make it fully white (`#ffffff`) or darken to at least `#f0f0f0` for any visible tint.

3. **Plotly-generated maps (Figs 1, S1):** Plotly exports as rasterized PNG; no vector path available. For CMYK, convert the final PNG with an ICC profile (e.g., `US Web Coated SWOP v2`).

4. **Transparency/alpha:** Several figures use `alpha=0.15` fills (Fig 7 quadrant shading, Fig 10 circles). Transparency does NOT exist in CMYK. These must be pre-composited to flat RGB before CMYK conversion, or converted to equivalent solid colors.

### Conversion workflow

```
# For matplotlib figures: save as PDF (vector) first, then convert
fig.savefig("figure.pdf", format="pdf", backend="pdf")
# Then use Ghostscript or Adobe for CMYK conversion

# For Plotly figures: save high-DPI PNG, then ICC-convert
# sips --matchTo '/System/Library/ColorSync/Profiles/Generic CMYK Profile.icc' input.png --out output.png
```

### Font embedding for PDF/EPS output

- Arial (`.ttf`) embeds correctly in matplotlib PDF backend
- Helvetica (`.ttc`) does NOT embed -- avoid
- Set `pdf.fonttype: 42` (TrueType) in rcParams for maximum compatibility
- Set `ps.fonttype: 42` for EPS output

---

## 8. Consolidated Action Plan

### Priority 1 (Blocking -- must fix before submission)

| Item | Figures Affected | Fix |
|------|-----------------|-----|
| DPI below 300 | Figs 1, 2, 3, 5, 6, 7, 8, 9, 10, S1, S7 (11 of 17) | Regenerate all at target DPI (300 or 600). |
| Font family inconsistency | All legacy-generated (serif) vs new (sans-serif) | Standardize on Arial, `font.family: "sans-serif"`, `font.sans-serif: ["Arial"]`. |
| Fig 10 redesign | Fig 10 | Implement new triangular flow diagram per Section 5 spec. |
| `#fafafa` background inconsistency | Figs 5-10 use it; Figs 1-4, S1-S7 do not | Unify to white (`#ffffff`) for all figures. |

### Priority 2 (Should fix)

| Item | Figures Affected | Fix |
|------|-----------------|-----|
| Colorblind risk | Figs 3, S1, S3, S5 | Replace non-OI palettes with Okabe-Ito throughout. |
| Grayscale viability | Figs 1, 3, 8, 10 | Add hatch patterns or texture differentiation. |
| Physical size normalization | All 17 | Set figsize to match target width at target DPI. |
| Plotly DPI metadata | Figs 1, S1 | Use `scale=3` or higher in `pio.write_image()` and set DPI metadata via `sips`. |

### Priority 3 (Polish)

| Item | Figures Affected | Fix |
|------|-----------------|-----|
| Alpha transparency for CMYK | Figs 7, 10 | Pre-composite to solid colors. |
| rcParams for PDF embedding | All | Add `pdf.fonttype: 42`, `ps.fonttype: 42`. |
| Legacy script output path | Legacy script | Update `FIG_DIR` to `PAPER-V2/figures/` and `PAPER-V2/supplementary/supp-figures/`. |
| Yellow on white | Fig S1 | Darken `#F0E442` or add dark border for Buen Vivir/Dharmic markers. |

---

*End of Phase 1 audit. This report is a read-only assessment; no files were modified.*

---

## Phase 2: Cross-Review

**Date:** 2026-04-12
**Reviewer Perspectives:** P5 (Color Science), P8 (Typography), P10 (LaTeX Embedding), P11 (Data Viz Code)
**Method:** Independent verification of Phase 1 findings, with additions and corrections.

---

### CR-1. Fig 10 Wireframe Assessment

**Verdict: APPROVED with 5 amendments.**

The Section 5 wireframe is concrete enough for a matplotlib developer to implement. The specification includes exact coordinates, colors, font sizes, boxstyles, arrow parameters, and figure dimensions. However, five gaps would cause implementation friction:

| # | Gap | Required Specification |
|---|-----|----------------------|
| 1 | **Coordinate system mismatch** | The wireframe uses figure coords `(5.0, 7.5)` etc. in a `(10, 10)` space, but the existing `fig10_triple_bind()` uses `(-5, 5)` centered coords. The wireframe must state: `ax.set_xlim(0, 10)`, `ax.set_ylim(0, 10)`. This IS stated in Section 5.2.E but the developer must reconcile with the existing code's `(-5, 5)` range -- add an explicit note to replace the existing coordinate system entirely. |
| 2 | **Node box sizing units** | "3.5 x 2.2 in" is specified but `FancyBboxPatch` in matplotlib uses data coordinates, not inches. At `figsize=(10, 9)` with xlim/ylim `(0, 10)`, 1 data unit ~ 1 inch horizontally and ~0.9 inch vertically. The spec should state dimensions in **data units**: width=3.5, height=2.4 (to get ~2.2 physical inches vertically). |
| 3 | **Text vertical positioning within boxes** | "Line 1: title, Lines 2-4: statistics" but no explicit y-offsets within the box. Specify: title at `cy + 0.55` (data units from box center), stats block at `cy - 0.25` with `linespacing=1.4`. |
| 4 | **Mechanism edge-box rotation** | The left and right edge-boxes (A: Scholarship->Benchmarks, C: Models->Scholarship) sit on diagonal edges. The spec says nothing about text rotation. Recommendation: do NOT rotate the boxes (rotation makes text harder to read in print). Keep all edge-boxes horizontal and position them adjacent to the diagonal arrows, offset outward. |
| 5 | **Arrow endpoint coordinates** | The spec says "Scholarship bottom-left corner -> Benchmarks top" but does not give numeric `(x, y)` pairs. Required values for the `annotate()` calls: Scholarship bottom-left = `(3.25, 6.4)` -> Benchmarks top = `(1.5, 2.6)`; Benchmarks right = `(3.25, 1.5)` -> Models left = `(6.75, 1.5)`; Models top-right = `(8.5, 2.6)` -> Scholarship bottom-right = `(6.75, 6.4)`. |

**Comparison with existing code:** The current `fig10_triple_bind()` (lines 371-457 in `generate_new_figures.py`) uses circles, not rounded rectangles, and a simpler layout. The wireframe is a full replacement, not a patch. The developer should create a new function `fig10_triple_bind_v2()` and swap at the call site.

**One rejected detail:** The "concentric arcs spiral icon" for the amplification zone (Section 5.2.D, first option) is impractical in matplotlib -- it would require manual `Arc` patches that are fragile and non-semantic. The text-box option is the correct choice. The spec already presents this as the fallback ("OR text box") -- make the text-box the PRIMARY spec and remove the spiral option.

---

### CR-2. Font Verification

**Phase 1 finding: CONFIRMED and extended.**

Arial resolves correctly on this macOS system:

| Font | Resolved Path | Format | Embeddable |
|------|--------------|--------|------------|
| Arial Regular | `/System/Library/Fonts/Supplemental/Arial.ttf` | TTF | Yes |
| Arial Bold | `/System/Library/Fonts/Supplemental/Arial Bold.ttf` | TTF | Yes |
| Arial Italic | `/System/Library/Fonts/Supplemental/Arial Italic.ttf` | TTF | Yes |
| Arial Bold Italic | `/System/Library/Fonts/Supplemental/Arial Bold Italic.ttf` | TTF | Yes |

Verified: matplotlib `findfont('Arial')` resolves to the real `.ttf` file (not a fallback). PDF embedding test confirmed Arial appears in the output PDF with `pdf.fonttype: 42`.

**Exact rcParams specification (canonical):**

```python
plt.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["Arial", "Helvetica Neue", "DejaVu Sans"],
    "pdf.fonttype": 42,    # TrueType (not Type 3)
    "ps.fonttype": 42,     # TrueType for EPS
})
```

**Notes:**
- The fallback chain `["Arial", "Helvetica Neue", "DejaVu Sans"]` is intentional. Helvetica Neue is listed second (not Helvetica) because Helvetica on macOS is `.ttc` format which matplotlib cannot embed. Helvetica Neue is also `.ttc` on this system, so it will also fail -- but DejaVu Sans (bundled with matplotlib) is the final safe fallback.
- Do NOT put Helvetica (plain) in the chain. It resolves to `/System/Library/Fonts/Helvetica.ttc` and will cause silent PDF embedding failures.
- `pdf.fonttype: 42` is critical. The default (Type 3) produces fonts that some journals reject and that do not render correctly in some PDF viewers.

**Font size scaling concern:** Phase 1 correctly notes that font sizes will be halved when figures are scaled from their current physical sizes (10-13 in) to publication widths (3.46-7.09 in). However, the recommendation to "increase for single-column figures" is insufficient. The correct fix is to **set figsize to the target publication width** and keep font sizes at 7-9pt. This avoids any scaling. Specifically:

| Figure Width | `figsize` width | Base font | Axis label | Tick label |
|-------------|----------------|-----------|------------|------------|
| Double (7.09 in) | 7.09 | 8 pt | 9 pt | 7 pt |
| Single (3.46 in) | 3.46 | 7 pt | 8 pt | 6.5 pt |

---

### CR-3. Legacy Script Feasibility

**Phase 1 finding: PARTIALLY CORRECT. Amended below.**

The legacy script (`SCRIPTS/generate_paper_figures.py`) references:
- `DATA_DIR` = `CULTURAL-GLOBAL/DATA/`
- `FIG_DIR` = `CULTURAL-GLOBAL/PAPER/figures/` (hardcoded to old path)

**Data dependency verification (all exist in `DATA/`):**

| Data File | Status |
|-----------|--------|
| `20260403-author-geography.json` | EXISTS |
| `20260403-weird-scores.json` | EXISTS |
| `20260403-cross-cultural-analysis.json` | EXISTS |
| `20260403-nw-scores.json` | EXISTS |

**Additional dependencies not mentioned in Phase 1:**
- `plotly` is required for `fig1_world_map()` and `fig10_bubble_map()` (choropleth + bubble map)
- The script has a `load_json()` fallback that searches for date-prefixed files by suffix, so it will auto-resolve even if dates change

**Can it run?** Almost. Two changes needed:

1. **Output path:** Change line 36 from `FIG_DIR = os.path.join(BASE, "PAPER", "figures")` to point at `PAPER-V2/figures/` and `PAPER-V2/supplementary/supp-figures/` (the legacy script writes everything to one directory, but PAPER-V2 splits main/supplementary).

2. **Plotly `scale` parameter:** The Plotly `write_image()` calls use `scale=2` at `width=1200`, producing 2400px at 72 DPI metadata. To get 300 DPI at 7.09in width, need: `scale = (7.09 * 300) / 1200 = 1.77`, or better: set `width=2127, height=1242, scale=1` and manually set DPI metadata via `sips` post-hoc. Plotly does not natively write DPI metadata into PNGs.

3. **Font family:** Line 42 sets `font.family: "serif"` -- must change to `"sans-serif"` with the Arial chain from CR-2.

**Recommendation:** Do NOT modify the legacy script in place. Create a thin wrapper `regenerate_legacy_figures.py` in `PAPER-V2/` that:
- Imports the legacy functions
- Overrides `FIG_DIR` 
- Applies the unified rcParams
- Saves to both `figures/` and `supplementary/supp-figures/` as appropriate
- Calls `sips` to set DPI metadata on Plotly outputs

---

### CR-4. Colorblind and Grayscale Review

**Phase 1 risk assessments: APPROVED with 3 corrections and 2 additions.**

#### Corrections

| Fig | Phase 1 Rating | Corrected Rating | Reason |
|-----|---------------|-----------------|--------|
| Fig 1 (choropleth) | MODERATE | **HIGH** | 4 tiers on a map with no redundant encoding (no patterns, no labels on countries). Deuteranopes cannot distinguish orange (#E69F00) from vermillion (#D55E00) at the small sizes of country polygons. This is functionally indistinguishable from Fig S1's HIGH rating. |
| Fig 9 heatmap | MODERATE | **LOW** (after mitigation) | The text labels ("med"/"high") already provide a redundant channel. The heatmap only has 3 levels. Phase 1 correctly identifies this but still rates it MODERATE -- with text labels present, the effective risk is LOW. |
| Fig 10 | MODERATE | **LOW** (after redesign) | The wireframe redesign uses rounded rectangles with text inside each node. Even if the border colors are confusable, the node labels ("WEIRD Scholarship", "Broken Benchmarks", "Monocultural Models") are the primary differentiator. Risk drops to LOW. |

#### Mitigation adequacy

| Mitigation | Adequate? | Notes |
|-----------|-----------|-------|
| **Hatching for grayscale (Figs 1, 5, 8)** | YES | Standard practice. Use matplotlib `hatch` parameter: `"///"`, `"xxx"`, `"..."`, `"+++"` for 4 tiers. Ensure hatch linewidth is >= 1.0 at target DPI to survive print. |
| **Diverging colormaps (Fig 2 heatmap)** | PARTIAL | A diverging colormap (e.g., `RdBu`) helps colorblindness but may hurt grayscale (both extremes map to dark). For a heatmap with no natural zero-point, a **sequential** colormap (`viridis` or `cividis`) is safer. `cividis` is specifically designed for CVD. |
| **Cluster labels at dendrogram leaves (Fig 3)** | YES, but INSUFFICIENT alone | Adding leaf labels helps but does not solve the branch-color problem. Also add `set_link_color_palette()` with the OI palette to replace matplotlib defaults, and consider using `above_threshold_color` to limit the number of colors to 3-4. |

#### Additions

| Fig | Issue Not Flagged in Phase 1 | Risk | Mitigation |
|-----|----------------------------|------|------------|
| Fig 7 (cultural map) | Quadrant shading uses `#ffe8e8` (pink) and `#e8f4ff` (blue) at alpha=0.3. These are near-invisible in grayscale and will disappear entirely in CMYK. | LOW (decorative, not data-bearing) | Either darken to `#ffcccc` / `#cce0ff` or add diagonal watermark text ("Traditional/Survival" etc.) which is already present. No action needed if quadrant text labels remain. |
| Fig 6 (coverage) | Green (#009E73) and vermillion (#D55E00) are the OI pair specifically chosen for CVD safety, but in **grayscale** they have similar luminance (~45% and ~48% grey). | MODERATE for grayscale-only venues | Add hatching to one bar series (e.g., `"///"` on unmeasured bars). |

---

### CR-5. LaTeX Embedding Compatibility

**Triple-output (PNG + PDF + TIFF) assessment:**

| Format | Nature | acmart (ACM) | PNAS | IEEE | Verdict |
|--------|--------|-------------|------|------|---------|
| **PDF** (vector) | Preferred | Preferred | Preferred | Preferred | BEST for all line-art figures (3, 4, 6, 10, S4, S5, S7). Use `fig.savefig(..., format='pdf')`. |
| **PNG** (raster) | Acceptable (300+ DPI) | Acceptable (300+ DPI) | Acceptable (300+ DPI) | Acceptable (300+ DPI) | OK for halftone figures (1, 2, 5, 7, 8, 9, S1-S3, S6). |
| **TIFF** (raster) | Required for final submission | Not required | Preferred | Not accepted (too large) | ONLY generate on demand. Most LaTeX workflows use PDF/PNG during drafting; TIFF is a submission-stage artifact. |
| **EPS** | Legacy format | Accepted | Accepted | Accepted | Not recommended. Modern LaTeX (`pdflatex`, `lualatex`, `xelatex`) all prefer PDF over EPS. Only generate if the venue explicitly requires it. |

**Key compatibility issues:**

1. **`\includegraphics` and PDF:** LaTeX `\includegraphics{fig}` auto-selects `fig.pdf` over `fig.png` when both exist. This is correct behavior -- vector preferred. Ensure filenames are consistent (no spaces, no uppercase).

2. **Transparency in PDF figures:** `pdflatex` handles transparency correctly in included PDFs. However, some print workflows flatten transparency incorrectly. The Phase 1 recommendation to pre-composite alpha to solid RGB (Section 7, point 4) is correct for CMYK/print but unnecessary for the LaTeX draft stage.

3. **File size:** PDF vector figures with many scatter points (Fig 7, ~8 points) are tiny. But Fig 1 (Plotly choropleth) as PDF would be enormous (full world-map vector data). Keep Plotly outputs as high-DPI PNG only.

4. **Nature template specifics:** Nature requires figures at exact widths (89mm single, 183mm double) and specifies "at least 300 d.p.i." for raster. They accept PDF, EPS, TIFF. Their LaTeX template uses `\includegraphics[width=\linewidth]` so physical dimensions in the file are overridden -- only pixel count matters for raster quality.

**Recommendation:** Generate **PDF + PNG** for all matplotlib figures. Skip TIFF during development (add a `--tiff` flag to the generator for submission time). For Plotly figures (1, S1), generate PNG only at `scale=3` (3600x2100 px, giving 508 DPI at 7.09in width).

**Savefig pattern:**

```python
def save_figure(fig, basename: str, dpi: int = 300):
    """Save figure in both PDF (vector) and PNG (raster)."""
    fig.savefig(os.path.join(FIG_DIR, f"{basename}.pdf"), format="pdf")
    fig.savefig(os.path.join(FIG_DIR, f"{basename}.png"), format="png", dpi=dpi)
```

---

### CR-6. Consolidated Recommendations Per Figure

| Fig | DPI | Width | Format | Font Fix | Color Fix | Grayscale Fix | Other |
|-----|-----|-------|--------|----------|-----------|---------------|-------|
| 1 | 300 | 7.09in | PNG only (Plotly) | Change to Arial sans-serif | Upgrade to HIGH risk; add hatch patterns to tiers | Hatch patterns on choropleth tiers | Plotly `scale=3` |
| 2 | 300 | 7.09in | PDF+PNG | Arial | Switch to `cividis` colormap (CVD+grayscale safe) | Add cell value annotations | Identify generator script |
| 3 | 600 | 7.09in | PDF+PNG | Arial | Replace default colors with OI palette via `set_link_color_palette()` | Add cluster ID labels at leaves | Identify generator script |
| 4 | 300 | 7.09in | PDF+PNG | Arial | Unknown palette -- audit when generator found | N/A (scatter, marker shapes suffice) | Reduce physical size |
| 5 | 300 | 7.09in | PDF+PNG | Already sans-serif | OK (OI) | Add hatching to one bar group | Set figsize=(7.09, 3.3) |
| 6 | 600 | 7.09in | PDF+PNG | Already sans-serif | OK (OI) | Add `"///"` hatch to unmeasured bars | Set figsize=(7.09, 3.5) |
| 7 | 300 | 3.46in | PDF+PNG | Already sans-serif | OK | OK (single color + star marker) | Set figsize=(3.46, 3.1), scale fonts |
| 8 | 300 | 7.09in | PDF+PNG | Already sans-serif | OK (OI) | Add hatch patterns (4 distinct) to bar groups | Set figsize=(7.09, 4.3) |
| 9 | 300 | 7.09in | PDF+PNG | Already sans-serif | OK (text labels mitigate) | OK (text labels present) | Set figsize=(7.09, 3.0) |
| 10 | 600 | 7.09in | PDF+PNG | Already sans-serif | OK after redesign (text-labeled nodes) | Add dashed/dotted/solid line styles to node borders | Implement wireframe from Section 5 |
| S1 | 300 | 7.09in | PNG only (Plotly) | Change to Arial | Replace non-OI colors; darken yellow | Add framework abbreviation labels to bubbles | Plotly `scale=3` |
| S2 | 300 | 3.46in | PDF+PNG | Change to Arial | OK (single color) | OK | Set figsize=(3.46, 2.1) |
| S3 | 300 | 3.46in | PDF+PNG | Change to Arial | Replace Office colors with OI palette | Add distinct line styles per trace | Set figsize=(3.46, 3.0) |
| S4 | 600 | 7.09in | PDF+PNG | Change to Arial | OK (blue/grey) | OK | Set figsize=(7.09, 2.5) |
| S5 | 600 | 7.09in | PDF+PNG | Change to Arial | Replace non-OI colors with OI | Add hatch patterns (7 bars) | Set figsize=(7.09, 4.3) |
| S6 | 300 | 3.46in | PDF+PNG | Change to Arial | OK (2 colors) | Add distinct markers/line styles | Set figsize=(3.46, 3.0) |
| S7 | 600 | 3.46in | PDF+PNG | Change to Arial | Unknown -- audit | N/A (diagnostic) | Regenerate at higher resolution |

---

### CR-7. Final Action Priority List

**Blocking (must complete before any submission):**

1. Set unified rcParams block (Arial chain + fonttype 42 + target figsize) in both scripts
2. Regenerate all 17 figures at correct DPI and physical dimensions
3. Implement Fig 10 wireframe redesign (new function, not patch)
4. Save all matplotlib figures as PDF+PNG dual output
5. Fix Plotly figures (1, S1) with `scale=3` and `sips` DPI metadata

**Should fix (before journal submission):**

6. Replace non-OI palettes in legacy script (Figs S3, S5) with Okabe-Ito
7. Add hatch patterns to Figs 1, 5, 6, 8 for grayscale viability
8. Switch Fig 2 heatmap colormap to `cividis`
9. Add `set_link_color_palette()` with OI colors to Fig 3 dendrogram
10. Identify and document generator scripts for Figs 2, 3, 4, S7

**Polish (nice to have):**

11. Add `--tiff` flag to generator for submission-stage TIFF export
12. Pre-composite alpha fills to solid RGB for CMYK readiness
13. Darken `#fafafa` to `#f0f0f0` or unify to white across all figures
14. Create thin wrapper script for legacy figure regeneration

---

*End of Phase 2 cross-review. No files other than this report were modified.*
