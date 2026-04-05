# Supplementary Figures

## Main Paper Figures (F1--F12)

### Figure 1: Top-15 Benchmarks by Composite Score
**File:** `figures/fig1-composite-scores.png` | `figures-pdf/fig1-composite-scores.pdf`
**Description:** Horizontal bar chart showing the top-15 benchmarks ranked by composite score (PD x 0.50 + PE x 0.30 + CI x 0.20), with stacked color bands indicating the contribution of each tier. Psychological Depth (blue), Practical Ease (orange), and Citation Impact (green) are shown as proportional segments.
**Source:** 28-feature characterization framework applied to 55 assessed benchmarks.

### Figure 2: Theory Distribution Across 222 Candidates
**File:** `figures/fig2-theory-distribution.png` | `figures-pdf/fig2-theory-distribution.pdf`
**Description:** Bar chart showing the number of candidate benchmarks associated with each of the 8 moral psychology theories after keyword scorer expansion. MFT dominates at 101 candidates; Dyadic Morality is lowest at 7.
**Source:** Five-signal detection pipeline output after keyword scorer expansion.

### Figure 4: Theory Coverage Heatmap (8 Theories x 15 Benchmarks)
**File:** `figures/fig3-theory-heatmap.png` | `figures-pdf/fig3-theory-heatmap.pdf`
**Description:** Heatmap showing which theories each of the top-15 benchmarks engages. Rows are theories (MFT, Schwartz, Trolley, Kohlberg, Social Intuitionism, Moral Identity, Dual Process, Dyadic Morality); columns are benchmarks. Cell intensity reflects engagement depth (primary, secondary, peripheral). The three empty rows (Dual Process, Social Intuitionism, Dyadic Morality with zero dedicated benchmarks) are the visual representation of Claim 3.
**Source:** Expert council assessment of benchmark-theory alignment.

### Figure 6: Implementation Status Grid
**File:** `figures/fig4-implementation-grid.png` | `figures-pdf/fig4-implementation-grid.pdf`
**Description:** Matrix showing the implementation status of top-15 benchmarks across 5 evaluation harness categories (direct API, lm-eval, Inspect, custom, behavioral). Color indicates status: green (implemented), yellow (partially implemented), red (not implemented), gray (not applicable).
**Source:** Implementation trial results and harness compatibility assessment.

### Figure 3: Construct Validity (A6) Score Distribution
**File:** `figures/fig5-construct-validity.png` | `figures-pdf/fig5-construct-validity.pdf`
**Description:** Histogram showing the distribution of A6 (construct validity evidence) scores across 55 assessed benchmarks. The median of 3/5 is highlighted. The right-skewed distribution shows that only 11% of benchmarks achieve multi-study validation (A6=5).
**Source:** 28-feature framework assessment.

### Figure 5: Human Baseline Availability (A5) Distribution
**File:** `figures/fig6-human-baselines.png` | `figures-pdf/fig6-human-baselines.pdf`
**Description:** Pie/bar chart showing A5 (human baseline availability) distribution: Published norms (42%), Paper-specific (33%), Partial (7%), None (18%).
**Source:** 28-feature framework assessment.

### Figure 7: Cross-Vendor Convergence --- Benchmark Discrimination
**File:** `figures/fig7-cross-vendor-convergence.png` | `figures-pdf/fig7-cross-vendor-convergence.pdf`
**Description:** Horizontal bar chart showing the coefficient of variation (CV) for each of the 23 benchmarks across all 9 models, ordered from most convergent (CV=0, ceiling-tied) to most divergent. Color-coded by discrimination category: red (ceiling, CV=0), orange (near-invariant, CV<0.05), yellow (low variation, CV<0.10), green (discriminating, CV>=0.10). A dashed vertical line at CV=0.05 marks the threshold between near-invariant and meaningfully varying benchmarks.
**Data source:** Cross-vendor comparison data (9 models x 23 benchmarks).

### Figure 8: RLHF Moral Fingerprint --- Three Vendors, One Profile
**File:** `figures/fig8-rlhf-fingerprint-radar.png` | `figures-pdf/fig8-rlhf-fingerprint-radar.pdf`
**Description:** Radar (spider) chart with 6 axes representing the six universal RLHF signatures (WEIRD-liberal bias, Purity floor, Authority suppression, Ethical consistency, Post-conventional default, Deontological refusal asymmetry). Three overlapping polygons (Anthropic in blue, Google in red, OpenAI in green) demonstrate near-complete overlap, visualizing the vendor-invariant moral fingerprint.
**Data source:** Normalized signature scores derived from cross-vendor analysis.

### Figure 9: DIT P-Score by Model --- Non-Monotonic Scale Sensitivity
**File:** `figures/fig9-scale-sensitivity-dit.png` | `figures-pdf/fig9-scale-sensitivity-dit.pdf`
**Description:** Bar chart showing DIT P-scores for all 9 models, colored by vendor. The non-monotonic pattern within Anthropic (Haiku 60, Opus 75, Sonnet 85) is highlighted, with a horizontal reference line at human mean (~42). All models score well above human means; the paradox is that the mid-tier model outscores the flagship.
**Data source:** MP3 (DIT) trial results across all 9 models.

### Figure 10: The Haiku Dual-Process Effect
**File:** `figures/fig10-cot-effect-haiku.png` | `figures-pdf/fig10-cot-effect-haiku.pdf`
**Description:** Bar chart showing the chain-of-thought (CoT) effect magnitude for each of the 9 models on the MP-DP (Dual Process) protocol. Eight models show a CoT effect of exactly 0.0; Claude Haiku shows +0.125 (12.5 percentage points more utilitarian with CoT). An annotation arrow highlights Haiku as the only model with a dual-process signature. Haiku's bar has a thick black border for emphasis.
**Data source:** MP-DP trial results (with/without CoT condition).

### Figure 11: MFT Foundation Profiles Across 9 Models
**File:** `figures/fig11-mft-profile-9models.png` | `figures-pdf/fig11-mft-profile-9models.pdf`
**Description:** Grouped bar chart with 5 foundation axes (Care, Fairness, Loyalty, Authority, Purity) and 9 model bars per foundation, colored by vendor. Shows the universal WEIRD-liberal profile: high Care and Fairness, low Loyalty and Authority, and a universal purity floor (~1.0). Annotations highlight "Individualizing (high)", "Binding (low)", and "Purity floor (universal)".
**Data source:** MFV (MP4) scores across 9 models.

### Figure 12: Cultural Persona MFQ Shift Magnitudes (MP18)
**File:** `figures/fig12-cultural-persona-shift.png` | `figures-pdf/fig12-cultural-persona-shift.pdf`
**Description:** Grouped bar chart showing the shift in MFQ Individualizing/Binding ratio when models are prompted with Confucian, Islamic, Ubuntu, and Western (baseline) cultural personas. Three Anthropic models shown (Opus, Sonnet, Haiku). All models show negative shifts (toward more balanced Binding) under non-Western personas, with Islamic persona producing the largest shift.
**Data source:** MP18 (Cultural Persona) trial results.

---

## Supplementary Figures (SF1--SF4)

### SF1: Per-Benchmark Score Distributions Across 9 Models
**Specification:** Panel of 23 mini-charts (one per benchmark), each showing 9 model data points colored by vendor (blue=Anthropic, red=Gemini, green=OpenAI) overlaid on a box showing the interquartile range. Benchmarks ordered by CV (most convergent at top). Panels for MP6, MP7, MP11, MP22 show zero-width boxes.
**Dimensions:** 8.5" x 14" (full page, portrait)
**Status:** To be generated from cross-vendor comparison JSON.

### SF2: Within-Vendor vs. Between-Vendor Variance Decomposition
**Specification:** Stacked bar chart for each of the 23 benchmarks showing the proportion of total variance explained by within-vendor differences (lighter shade) vs. between-vendor differences (darker shade). Sorted by between-vendor proportion. For ~8 of 13 non-ceiling benchmarks, within-Anthropic variance exceeds total between-vendor variance.
**Dimensions:** 10" x 6" (landscape)
**Status:** To be generated from variance decomposition analysis.

### SF3: Schwartz Value Profiles Across 9 Models
**Specification:** Parallel coordinates plot with 10 Schwartz value types as axes, colored lines for each model (by vendor). Shows the universal pattern of high Universalism/Self-Direction and low Achievement/Power.
**Dimensions:** 10" x 6" (landscape)
**Status:** To be generated from MP5 (ValueCompass) data.

### SF4: Dyadic Morality Attribution Patterns
**Specification:** Grouped bar chart showing mean structural blame, blame above zero, and dyadic effect sizes across all 9 models for the MP-DM protocol. Shows the extremely narrow range (3.208--3.292 on blame), visualizing the near-invariance of dyadic processing.
**Dimensions:** 8" x 5"
**Status:** To be generated from MP-DM trial data.

---

## Figure Generation Notes

**Color palette (consistent across all figures):**
- Anthropic: `#4A90D9` (blue)
- Google/Gemini: `#E74C3C` (red)
- OpenAI: `#2ECC71` (green)

**Typography:**
- Title: 13pt bold
- Axis labels: 11pt
- Data labels: 10pt
- Annotations: 9-10pt italic

**Output formats:** All figures generated as both PNG (300 DPI) and PDF.

**Generation scripts:** `scripts/build_figures_pdf.py` handles F1-F12. SF1-SF4 specifications are provided here for future generation from raw trial data.
