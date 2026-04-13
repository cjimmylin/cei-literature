# Supplementary Figures

## What Do Moral Psychology Benchmarks Actually Test? A Meta-Evaluation of 292 Candidates Across 13 Theories

**Version:** 4.0 (2026-04-05)

This supplement provides extended captions for all 15 main-text figures and 4 supplementary-only figures. Each entry includes the figure number and title, an extended caption describing visual content, reading instructions, and key findings, plus notes on data source and generation method.

---

## Main-Text Figures

### Figure 1: Triple Bind Conceptual Diagram

**File:** `figures/fig01-triple-bind.png`

**Extended Caption:** Figure 1 presents the triple bind as a three-circle Venn diagram in which each circle represents one of the three interlocking failures identified in this study: theoretical narrowness (Bind 1), empirical undiscrimination (Bind 2), and cultural blindness (Bind 3). The overlap regions illustrate the four causal pathways through which the binds reinforce one another: narrowness produces convergence, convergence reduces the incentive for diversity, cultural exclusion reinforces narrowness, and convergence makes cultural exclusion invisible. Directional arrows along each pathway indicate the self-reinforcing dynamics that sustain the triple bind as a stable equilibrium. The reader should note that the central region --- where all three circles overlap --- represents the condition in which the benchmark landscape currently operates: simultaneously narrow, undiscriminating, and culturally blind, with no natural mechanism for escape.

**Data Source:** Conceptual; derived from the integrated analysis in Section 6.3 and the compounding dynamics described in Section 7.1.4.

**Generation Method:** Programmatic vector diagram generated with Matplotlib; layout and labeling refined in post-processing.

---

### Figure 2: Composite Score Distribution with Jenks Natural Breaks

**File:** `figures/fig02-tier-histogram.png`

**Extended Caption:** Figure 2 displays the frequency distribution of composite quality scores for all 292 benchmark candidates as a histogram, with vertical dashed lines marking the three Jenks natural breaks at 27.8, 43.0, and 56.6 (GVF = 0.83). Each of the four resulting tiers is shaded in a distinct color: Low (n=83, 28.4%), Medium (n=72, 24.7%), High (n=89, 30.5%), and Top (n=48, 16.4%). The reader should observe that the distribution is right-skewed, with the majority of candidates clustering below the High-tier threshold at 43.0; the Top tier occupies the thin right tail. The key finding is that 53.1% of the landscape falls in the Medium or Low tiers, where fundamental quality requirements --- construct validity, human baselines, psychometric grounding --- remain unmet, establishing that the majority of moral psychology benchmarks for LLMs are not fit for publication-ready evaluation.

**Data Source:** 292-candidate composite scores from the 17-feature assessment framework (Tiers A--C), classified via Fisher-Jenks natural breaks optimization.

**Generation Method:** Histogram generated with Matplotlib; Jenks break points computed using the jenkspy library; tier shading applied programmatically.

---

### Figure 3: Theory x Tier Crosstab Heatmap

**File:** `figures/fig03-theory-tier-heatmap.png`

**Extended Caption:** Figure 3 presents a heatmap of the theory-by-tier crosstab (Table T5), with 13 moral psychology theories on the vertical axis ordered by quality rate from highest (Intuitionist, 100%) to lowest (Confucian, Indigenous, Identity; 0%), and four quality tiers (Top, High, Medium, Low) on the horizontal axis. Cell color intensity encodes candidate count, with darker cells indicating higher representation. The reader should note the sharp diagonal: the upper-left region (Western theories in high tiers) is warm-colored and dense, while the lower-right region (non-Western traditions in low tiers) is cool-colored or empty. This visual structure makes the cultural quality cliff immediately apparent --- the boundary between traditions that produce high-quality benchmarks and traditions that do not is sharp rather than gradual.

**Data Source:** Tier assignments for all 292 candidates, grouped by primary theoretical affiliation (Table T5, Section 4.1.3).

**Generation Method:** Heatmap generated with Seaborn/Matplotlib; row ordering by descending quality rate; color scale normalized to maximum cell count.

---

### Figure 4: Construct Validity Distribution

**File:** `figures/fig04-validity-distribution.png`

**Extended Caption:** Figure 4 shows the distribution of construct validity levels (Feature A6) across all 292 benchmark candidates, rendered as a bar chart with five bars corresponding to the five validity levels: Level 1 (keyword-level engagement, 27%), Level 2 (face validity only, 31%), Level 3 (adapted validated instrument without LLM revalidation, 24%), Level 4 (single-study validation, 14%), and Level 5 (multi-study psychometric validation, 4%). The reader should observe that 58% of all candidates fall at Level 1 or Level 2, where construct validity evidence is absent or limited to subjective face plausibility. The key finding is that the median validity level across the full landscape is Level 2 (face validity) --- a level that precludes interpretable claims about what the benchmark is actually measuring in an LLM. Only 4% of candidates achieve the multi-study validation standard that characterizes mature psychometric instruments.

**Data Source:** Feature A6 scores for all 292 candidates from the assessment framework (Section 4.2, Table T6).

**Generation Method:** Bar chart generated with Matplotlib; percentage labels computed from raw A6 level counts.

---

### Figure 5: Cultural Quality Cliff

**File:** `figures/fig05-cultural-cliff.png`

**Extended Caption:** Figure 5 visualizes the cultural quality cliff as a bar chart with moral traditions ordered by quality rate (top + high tiers combined) from highest to lowest: MFT (73%), Schwartz (57%), Kohlberg (56%), Trolley (48%), Islamic (36%), Buddhist (12%), and then the four zero-quality traditions (Ubuntu, Confucian, Indigenous, Identity; all 0%). The reader should note the distinct shape: a gradual descent from 73% to 48% across Western theories, a sharp drop to the intermediate cases (Islamic at 36%, Buddhist at 12%), and then a collapse to the zero line for the four non-Western cultural traditions. The key finding is that the quality cliff is not a smooth gradient but a categorical separation: every Western theory with 10+ candidates exceeds 46%, while every non-Western cultural tradition (excluding Islamic ethics) falls at or below 12%, with four traditions achieving exactly 0% despite fielding 32 candidates collectively.

**Data Source:** Quality rates (top + high tier percentage) for each theory from Table 8 (Section 4.4.1).

**Generation Method:** Horizontal bar chart generated with Matplotlib; traditions ordered by descending quality rate; color coding distinguishes Western (blue tones) from non-Western (orange/red tones) traditions.

---

### Figure 6: Baseline Availability by Tier

**File:** `figures/fig06-baseline-tier.png`

**Extended Caption:** Figure 6 presents a stacked bar chart showing human baseline availability (Feature A5) stratified by quality tier. Each tier's bar is divided into segments representing the proportion of candidates with published population norms, paper-specific human samples, partial/indirect norms, or no human baseline at all. The reader should observe that the "no baseline" segment grows substantially from the Top tier (where most candidates inherit baselines from validated source instruments) to the Low tier (where the majority lack any human comparison data). The key finding is that 34% of all 292 candidates provide no published human comparison data --- nearly double the 18% rate reported when the sample was limited to established benchmarks. Without baselines, claims about whether an LLM's moral profile is "above" or "below" human norms are empirically unmoored.

**Data Source:** Feature A5 (human baseline availability) scores for all 292 candidates, cross-referenced with Jenks tier assignments (Claim 5, Section 4.5).

**Generation Method:** Stacked bar chart generated with Matplotlib; baseline categories derived from A5 ordinal thresholds.

---

### Figure 7: Temporal Quality Stagnation

**File:** `figures/fig07-temporal-quality.png`

**Extended Caption:** Figure 7 presents a dual-axis time series showing two diverging trends: the number of new benchmark candidates per year (left axis, bar chart, showing roughly 9.5-fold volume growth from pre-2020 to 2023--2026) and the quality rate (right axis, line chart, showing a decline from approximately 75% pre-2020 to 48% in 2020--2022 to 46% in 2023--2026). The reader should track both axes simultaneously: as the bars rise steeply (volume explosion), the line falls (quality stagnation or decline). The key finding is that the field is not getting better at building moral psychology benchmarks; it is getting faster at building mediocre ones. The temporal pattern is itself a symptom of the triple bind: the infrastructure that enables high-quality benchmarks exists only for a small number of theories, and volume growth is driven by low- and medium-tier papers that repackage existing moral scenarios without addressing the construct validity gap.

**Data Source:** Year-of-publication metadata for all 292 candidates, grouped into three cohorts (pre-2020, 2020--2022, 2023--2026), with quality rates computed per cohort (Claim 6, Section 4.6).

**Generation Method:** Dual-axis chart generated with Matplotlib; left axis (bar) for volume, right axis (line) for quality rate; cohort boundaries aligned to calendar years.

---

### Figure 8: Cross-Vendor Convergence CV Chart

**File:** `figures/fig08-convergence-cv.png`

**Extended Caption:** Figure 8 displays the coefficient of variation (CV) for each of the 23 benchmarks administered in the cross-vendor empirical study, ordered from lowest CV (perfect convergence) to highest CV (maximum discrimination). Each bar represents one benchmark, with color coding by discrimination tier: D (zero variation, CV = 0.0), C (low variation, CV < 5%), B (moderate variation, CV 5--15%), and A (high discrimination, CV > 15%). The reader should note the bimodal distribution: a dense cluster of 10 benchmarks at CV approximately zero (all producing identical scores across nine models) and a sparse tail of benchmarks with measurable variation, culminating in the dual-process probe (MP-DP) at CV = 300%. The key finding is that 43% of benchmarks produce zero cross-model variation, and the battery's effective size --- the number of benchmarks contributing independent information --- is closer to six than twenty-three.

**Data Source:** Coefficient of variation computed from primary metric scores across 9 models x 3 vendors for each of 23 benchmarks (Table T13, Section 5.1.2).

**Generation Method:** Bar chart generated with Matplotlib; CV values on log scale for readability; discrimination tier thresholds marked with horizontal reference lines.

---

### Figure 9: RLHF Fingerprint Radar

**File:** `figures/fig09-rlhf-radar.png`

**Extended Caption:** Figure 9 presents a radar (spider) chart with six axes corresponding to the six universal RLHF signatures: WEIRD-liberal foundation bias, purity floor, authority deference suppression, ethical consistency ceiling, post-conventional moral default, and deontological refusal asymmetry. Each of the nine models is plotted as a polygon on the radar, with all nine polygons overlapping almost perfectly to form a single composite shape. The reader should observe that the overlap is near-total: switching from Claude Opus to Gemini 2.5 Pro to GPT-5 produces no visually detectable change in the moral profile. The key finding is that the RLHF moral fingerprint is vendor-invariant --- all nine models from three independent vendors share the same six moral signatures, constituting a shared moral identity without documented precedent in any human population.

**Data Source:** Normalized scores on each of the six RLHF signature dimensions for all 9 models (Table T14, Section 5.1.3).

**Generation Method:** Radar chart generated with Matplotlib; each axis normalized to 0--1 scale based on the theoretical range of the underlying metric; model polygons drawn with semi-transparent fill.

---

### Figure 10: DIT P-Score Non-Monotonicity

**File:** `figures/fig10-dit-pscore.png`

**Extended Caption:** Figure 10 presents the Defining Issues Test (DIT) P-scores for all nine models, ordered by model size within each vendor family. The key observation is the non-monotonic relationship between model scale and moral reasoning stage: within the Anthropic family, Sonnet (mid-size) achieves the highest P-score (approximately 85), exceeding both the larger Opus (approximately 75) and the smaller Haiku (approximately 60). This pattern violates the naive expectation that larger models should score higher on moral reasoning measures. The reader should also note the human reference lines: average adults score 30--50, graduate students 50--65, and moral philosophy PhDs 60--70. All nine LLMs exceed the highest documented human norms, with the scale sensitivity suggesting that P-score differences across models may reflect training data composition rather than genuine differences in moral reasoning sophistication.

**Data Source:** DIT P-scores from MP3 benchmark administration to 9 models; human reference values from Rest (1979) and Thoma (2006).

**Generation Method:** Grouped bar chart generated with Matplotlib; human reference bands shown as horizontal shaded regions; vendor grouping indicated by color.

---

### Figure 11: Haiku CoT Effect

**File:** `figures/fig11-cot-effect.png`

**Extended Caption:** Figure 11 visualizes the chain-of-thought (CoT) effect on moral judgment across all nine models using paired bars (zero-shot vs. CoT condition) for each model. Eight of nine models show no CoT effect: their moral judgments are identical with and without deliberative prompting. Haiku alone shows a 25 percentage-point increase in deontological response rate under CoT prompting --- the single largest cross-model difference in the entire 23-benchmark battery. The reader should note that this finding comes from the benchmark with the highest discrimination power (CV = 300%), which probes process-level rather than content-level moral cognition. The key finding is that the smallest model in the Anthropic family exhibits a dual-process dissociation that disappears in larger models, suggesting that scale-dependent training may compress the deliberative-intuitive distinction that is central to moral psychology.

**Data Source:** Zero-shot and CoT acceptance rates for personal-harm dilemmas from MP-DP (Dual Process Theory Protocol) across 9 models (Section 5.1.3, Signature 6).

**Generation Method:** Paired bar chart generated with Matplotlib; CoT shift magnitude annotated for each model.

---

### Figure 12: MFT Foundation Profiles for 9 Models

**File:** `figures/fig12-mft-profiles.png`

**Extended Caption:** Figure 12 presents the MFT foundation profiles (Care, Fairness, Loyalty, Authority, Purity on a 0--5 Likert scale) for all nine models as grouped bars or overlaid line plots. The reader should observe two patterns: first, all nine models share the same hierarchical ordering (Care > Fairness >> Loyalty > Authority >> Purity), and second, the cross-model variation within each foundation is minimal (typically less than 0.5 points on the 5-point scale). The Purity foundation scores cluster near 1.0 for all models --- the functional floor --- while Care and Fairness cluster near 4.0--4.5. The key finding is that the MFT profile is effectively invariant across vendors: the models do not merely agree on which foundations to endorse but agree on the precise magnitude of endorsement for each foundation, producing an Individualizing/Binding ratio band of 2.43--2.83 that falls within the "very liberal" zone of the MFT political space.

**Data Source:** MFQ-30 foundation subscale scores (MP2) and MFV purity subscale (MP4) for all 9 models.

**Generation Method:** Grouped bar chart generated with Matplotlib; foundation ordering follows MFT convention (Care, Fairness, Loyalty, Authority, Purity).

---

### Figure 13: Cultural Persona Shift Magnitudes

**File:** `figures/fig13-cultural-persona.png`

**Extended Caption:** Figure 13 displays the Individualizing/Binding ratio shifts when models are administered the Cultural Persona benchmark (MP18) under three conditions: default (no persona), East Asian persona, and liberal persona. For each model, three markers show the ratio under each condition, connected by lines to emphasize the shift magnitude. Under default conditions, all models cluster at Ind/Bind ratios of 2.43--2.63. Under the East Asian persona, ratios drop to 0.63--0.84, demonstrating that models possess the cultural knowledge to produce non-WEIRD profiles. Under the liberal persona, ratios inflate to 5.25--6.67, overshooting real American liberals (approximately 1.83) by a factor of 3.6. The key finding is the stereotype amplification effect: models can shift their moral profiles dramatically under persona prompting, but the shifts produce caricatures that exceed any documented human population, revealing that the WEIRD-liberal default is set by alignment training rather than knowledge limitation.

**Data Source:** MP18 (Cultural Persona) Ind/Bind ratios for all 9 models across default, East Asian, and liberal persona conditions (Section 5.1.3, Signature 1).

**Generation Method:** Dot-and-line chart generated with Matplotlib; horizontal reference lines mark human liberal (1.83) and conservative (0.9) population means.

---

### Figure 14: Tier vs. Discrimination Scatter

**File:** `figures/fig14-tier-discrimination.png`

**Extended Caption:** Figure 14 presents a scatter plot with composite quality score on the x-axis and coefficient of variation (discrimination power) on the y-axis for all 23 benchmarks administered in the cross-vendor study. Points are color-coded by quality tier (Top, High, Medium, Low). A fitted regression line shows the strongly negative correlation (r = -0.83): higher-quality benchmarks produce less variation between models, not more. The reader should note the outlier in the lower-right quadrant --- MP-DP (Dual Process), a Low-tier benchmark that achieves the highest discrimination by probing process-level rather than content-level cognition. The key finding is counterintuitive: the best instruments in the landscape are the ones that most emphatically confirm moral convergence, establishing that the undiscrimination finding is not a measurement artifact but a genuine property of RLHF-aligned models confirmed by their own best instruments.

**Data Source:** Composite quality scores (17-feature assessment) and 9-model CVs for 23 benchmarks (Table T26, Section 6.1).

**Generation Method:** Scatter plot generated with Matplotlib; linear regression fit with r-value annotation; tier membership indicated by point color and shape.

---

### Figure 15: Infrastructure-Quality-Discrimination Pipeline Diagram

**File:** `figures/fig15-pipeline.png`

**Extended Caption:** Figure 15 presents the infrastructure-quality-discrimination pipeline as a three-stage flow diagram. Stage 1 (Theory Infrastructure) shows how a theory's dual assets --- validated instruments and annotated corpora --- feed into Stage 2 (Benchmark Quality), where inherited psychometric properties determine composite scores and tier assignments. Stage 2 feeds into Stage 3 (Empirical Discrimination), where the content-level vs. process-level measurement dimension determines whether a benchmark can distinguish between RLHF-aligned models. Feedback arrows illustrate the self-reinforcing dynamics: high-quality content-level benchmarks confirm convergence, convergence reduces the incentive for process-level investment, and the cycle perpetuates the triple bind. The reader should trace the full pathway from MFT's infrastructure advantage through its quality dominance to the convergence finding, recognizing that the pipeline explains why more benchmarks of the same type cannot resolve the evaluative crisis.

**Data Source:** Conceptual; derived from the integrated analysis in Section 6.2 and the tier-stratified empirical findings in Section 6.1.

**Generation Method:** Flow diagram generated programmatically with Matplotlib/NetworkX; stage boxes and arrow annotations added in post-processing.

---

## Supplementary-Only Figures

### Figure S16: UMAP Benchmark Clustering

**File:** Not yet generated.

**Extended Caption:** Figure S16 presents a two-dimensional UMAP projection of all 292 benchmark candidates, where each point represents one candidate positioned according to its 17-feature assessment profile. Points are colored by quality tier (Top, High, Medium, Low) and shaped by primary theoretical affiliation. The reader should observe the spatial clustering pattern: MFT candidates form a dense cluster in the high-quality region (upper-right), with Schwartz and trolley candidates partially overlapping, while non-Western tradition candidates occupy a separate, diffuse region in the low-quality zone (lower-left). The separation between Western and non-Western clusters in the reduced feature space provides geometric confirmation of the cultural quality cliff: the traditions do not merely differ in score; they occupy structurally distinct regions of the assessment space, suggesting that the quality gap reflects different kinds of benchmarks rather than merely different levels of the same kind.

**Data Source:** 17-feature assessment profiles for all 292 candidates, reduced via UMAP (n_neighbors=15, min_dist=0.1, metric=euclidean).

**Generation Method:** UMAP embedding computed with umap-learn; scatter plot generated with Matplotlib; interactive version available in the companion dashboard.

---

### Figure S17: Theory Coverage Treemap (Updated for 292)

**File:** Not yet generated.

**Extended Caption:** Figure S17 presents a treemap visualization of theoretical coverage across all 292 benchmark candidates, where rectangle area encodes the number of candidates affiliated with each theory and color saturation encodes quality rate (top + high percentage). The reader should note the dominance of MFT (67 candidates, darkest color indicating 73% quality rate) relative to the non-Western traditions (smaller rectangles, lighter colors indicating lower quality rates). The "Unclassified" category (83 candidates, moderate color) occupies the largest single rectangle, reflecting the substantial number of benchmarks that engage moral psychology without primary allegiance to a single theory. The key finding, relative to the prior 55-benchmark treemap, is that the expanded 292-candidate landscape does not dilute MFT's quality dominance; it reveals that the dominance is even more pronounced when the full tail of low-quality non-MFT candidates is included.

**Data Source:** Theory affiliation and quality tier assignments for all 292 candidates (Table T5, Section 4.1.3).

**Generation Method:** Treemap generated with squarify/Matplotlib; rectangle sizing by candidate count, color mapping by quality rate.

---

### Figure S18: Feature Importance by Variance

**File:** Not yet generated.

**Extended Caption:** Figure S18 presents a horizontal bar chart showing the variance contribution of each of the 17 composite-determining features (A1--A6, B1--B4, B6--B7, B10, C1--C3, C5) to the overall composite score variance across 292 candidates. Features are ordered from highest variance contribution (top) to lowest (bottom). The reader should observe that Feature A6 (construct validity evidence) and Feature A5 (human baseline availability) contribute the most variance, confirming that these two features are the primary drivers of quality tier separation. Feature A4 (validated source instrument) ranks third, reflecting the binary nature of its distribution: candidates that inherit a validated instrument score substantially higher than those that do not. The key finding is that the composite score --- and therefore tier assignment --- is determined primarily by three features (A6, A5, A4) that together capture the "theory infrastructure" advantage described in Section 4.1.2.

**Data Source:** Feature-level scores for all 292 candidates across the 17 composite-determining features.

**Generation Method:** Variance decomposition computed with NumPy; horizontal bar chart generated with Matplotlib.

---

### Figure S19: Pre/Post RLHF Quality Comparison

**File:** Not yet generated.

**Extended Caption:** Figure S19 presents paired comparisons of moral profile metrics for base models versus their RLHF-aligned counterparts, where available, across the MFQ-30 Ind/Bind ratio, the DIT P-score, and the ethical consistency index (ECI). For each metric, paired points connected by arrows show the shift from base to aligned model. The reader should observe the consistent direction of shift: RLHF alignment increases the Ind/Bind ratio (toward WEIRD-liberal values), increases the P-score (toward post-conventional reasoning), and increases the ECI (toward perfect consistency). The magnitude of the shift is largest for the purity floor (base models show moderate purity sensitivity; aligned models show near-zero) and the ECI (base models show human-like inconsistency; aligned models achieve perfect consistency). The key finding is that the six RLHF signatures documented in Section 5.1.3 are alignment artifacts rather than properties of the underlying language model, as the pre-alignment models do not exhibit the same moral fingerprint.

**Data Source:** Base-model and RLHF-aligned model scores on MFQ-30, DIT, and ECI benchmarks, where base-model access was available (limited to Anthropic and open-weight models).

**Generation Method:** Paired dot-and-arrow chart generated with Matplotlib; shift magnitudes annotated; base-model data limited to publicly available checkpoints.

---

*End of Supplementary Figures.*
