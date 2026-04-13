## Supplementary Figures

This appendix catalogues all figures accompanying the paper, divided into main body figures (Figures 1--13) and supplementary figures (Figures S1--S8). For each figure, we specify the data source, visual encoding, key features, and the section in which the figure is referenced. Figures 1--9 and S1--S3 correspond to existing visualizations generated during earlier analysis sessions; Figures 10--13 and S4--S8 are new figures introduced in this revision to support the cross-model and cross-vendor analyses (Sections 4.5--4.6). Generation specifications for new figures are provided in sufficient detail to serve as input to a matplotlib/seaborn rendering script.

All figures use a colorblind-safe palette (Okabe-Ito) unless otherwise noted. Publication-quality output is rendered at 300 DPI as PNG files saved to `PAPER-V2/figures/`. Axis labels use a serif typeface (Times New Roman or Computer Modern); legends use sans-serif (Helvetica). All figures are designed to be self-contained: readable without surrounding text, with complete axis labels, legends, and inline annotations where appropriate.

---

### Main Body Figures

**Figure 1. Tradition Coverage Heatmap.**
Source: `PAPER/figures/fig1-tradition-heatmap.png`. A matrix of 14 religious and philosophical traditions (rows) against three benchmark availability indicators (columns): total candidates, gate-passers, and tiered entries. Cell color encodes count on a sequential blue scale, with zero-count cells rendered in light gray to make absences visually salient. A horizontal dashed line separates the 6 traditions with at least one gate-passer from the 8 traditions with zero viable benchmarks. Row order follows tradition family grouping (Abrahamic, Dharmic, East Asian, African/Indigenous, minority), with traditions sorted by descending gate-passer count within each family. The 8-tradition void --- Judaism, Jainism, Taoism, Shinto, Ubuntu Philosophy, Indigenous Spirituality, Baha'i, and Zoroastrianism --- occupies a contiguous block of empty cells in the lower portion of the matrix. Referenced in Section 4.1.

**Figure 2. Candidate Distribution by Tradition Family.**
Source: `PAPER/figures/fig2-tradition-distribution.png`. Grouped horizontal bar chart showing the 401 benchmark candidates organized by tradition. Each tradition receives two bars: a light bar indicating total candidates and a dark bar indicating gate-passers. The chart makes three features immediately visible: the Abrahamic dominance (Christianity 117, Islam 113), the false-positive inflation in Jainism (47 candidates, 0 gate-passers, nearly all triggered by the keyword *ahimsa*), and the near-total absence of African/Indigenous representation (Ubuntu Philosophy 4 candidates, Indigenous Spirituality 16 candidates, both with 0 gate-passers). Islam's conversion rate of 24.8\% (28/113) is annotated alongside Christianity's 5.1\% (6/117) to highlight the asymmetry between raw candidate volume and evaluation-quality output. Referenced in Section 4.1.

**Figure 3. RD vs. PE Scatter Plot.**
Source: `PAPER/figures/fig3-rd-vs-pe-scatter.png`. Scatter plot of all 401 candidates with Religious/Theological Depth (RD, 0--100) on the x-axis and Practical Ease (PE, 0--100) on the y-axis. Bubble size encodes log-transformed citation count ($\log(\text{citations} + 1)$), and color encodes tradition family using the Okabe-Ito palette (Abrahamic blue, Dharmic orange, East Asian green, African/Indigenous vermillion, minority reddish-purple). A vertical dashed red line marks the RD $\geq$ 30 hard gate; candidates to the left of this line are excluded from tiered ranking regardless of PE score. The Islamic benchmark cluster in the upper-right quadrant (RD 34--62, PE 60--85) is the most prominent feature, reflecting the shared-task infrastructure that simultaneously enforces data release protocols and scaffolds theological depth. The expected RD--PE tradeoff is visible outside this cluster: the most theologically rigorous candidates often lack public data, while the most accessible benchmarks treat religion as a demographic label. Referenced in Section 4.1.

**Figure 4. Data Availability by Tradition.**
Source: `PAPER/figures/fig4-data-availability.png`. Stacked bar chart showing available versus unavailable evaluation data for each of the 14 traditions. The overall unavailability rate is 42\% (170 of 401 candidates). Color encoding uses green for available and red for unavailable. The chart reveals that data unavailability is not tradition-neutral: Indigenous Spirituality, Ubuntu Philosophy, Taoism, and Shinto have disproportionately high unavailability rates, reflecting the structural disadvantage of traditions whose knowledge systems were developed through oral, communal, and practice-based transmission rather than textual formats amenable to digital repository hosting. Referenced in Section 4.1.

**Figure 5. Bootstrap Confidence Interval Forest Plot.**
Source: `PAPER/figures/fig5-bootstrap-ci-forest.png`. Forest plot displaying all 45 gate-passing benchmarks (post-removal), ordered by composite score on the y-axis. Each benchmark is represented by a point estimate (median composite across 1,000 bootstrap iterations) with horizontal error bars showing the 95\% bootstrap confidence interval. Vertical dashed lines mark the tier boundaries separating Tier 1 (12 benchmarks), Tier 2 (3 benchmarks), and Tier 3 (10 benchmarks). The key feature is the extensive overlap of confidence intervals, particularly in the Tier 1/Tier 2 boundary region (composite scores 43--48), demonstrating that the ranking is subject to meaningful uncertainty and that adjacent benchmarks are not statistically distinguishable. The mean CI width is 15.87 composite points. Color encoding distinguishes tiers (Tier 1 dark blue, Tier 2 medium blue, Tier 3 light blue). Referenced in Section 4.2.

**Figure 6. Void Factor Radar.**
Source: `PAPER/figures/fig6-void-factor-radar.png`. Radar (spider) chart with 6 axes representing structural factors contributing to the 8-tradition benchmark void: (1) oral transmission tradition, (2) communal knowledge governance, (3) limited digital corpus availability, (4) small NLP research community, (5) restricted publication infrastructure, and (6) epistemic sovereignty constraints. Each void tradition receives a polygon plotted against these 6 dimensions, with axis values derived from the structured void factor taxonomy. The chart distinguishes two causal profiles: traditions where the void reflects community coordination problems that could be addressed through targeted investment (e.g., Judaism, Confucianism) versus traditions where the void reflects structural epistemic exclusion inherent to the benchmark creation pipeline (e.g., Indigenous Spirituality, Ubuntu Philosophy). Mean readiness scores for active traditions (10.5) versus void traditions (5.12) are annotated. Referenced in Section 4.3.

**Figure 7. Values Relevance Histogram.**
Source: `PAPER/figures/fig7-values-relevance-histogram.png`. Histogram of A3 values relevance scores across the 16 gate-passing benchmarks assessed on the 24-dimension values relevance rubric. The x-axis spans 0--100, the y-axis shows count. The distribution exhibits a strong left skew: the mean score is 30.0/100 (SD = 16.2), with most scores below 40, only 3 of 16 (18.8\%) exceeding 50, and none reaching 75. A vertical dashed line marks the scale midpoint (50), and the one-sample t-test result is annotated ($t = -4.93$, $p < 0.001$, Cohen's $d = -1.23$). This distribution is the primary evidence for Claim 8 (values relevance failure): benchmarks that nominally evaluate religious values predominantly test knowledge recall and bias detection rather than values alignment. Referenced in Section 4.4.

**Figure 8. Claim Robustness Summary.**
Source: `PAPER/figures/fig8-claim-robustness.png`. Horizontal bar chart displaying all 8 empirical claims with color-coded significance levels: green (4 claims supported at $p < 0.05$), yellow (1 claim marginal), and orange (3 claims revised or not reaching significance). Each bar is labeled with the claim number and a brief descriptor. The supported claims are: tradition asymmetry ($\chi^2 = 64.96$, $p < 0.001$), knowledge--reasoning conflation (binomial $p = 0.0015$), data availability bottleneck, and values relevance failure ($p < 0.001$). The three revised claims are: WEIRD bias reversal, structural epistemic injustice pathway, and bias--values conflation significance. Referenced in Section 4.4.

**Figure 9. Gate Threshold Sensitivity.**
Source: `PAPER/figures/fig9-gate-threshold-sensitivity.png`. Line chart showing the number of gate-passing candidates as a function of the RD threshold, swept from 0 to 70 in increments of 5. The x-axis represents the RD threshold and the y-axis represents the number of candidates passing both gates (RD $\geq$ threshold and public data). A sharp drop at RD = 30 confirms the bimodal distribution of theological depth scores and validates the choice of RD = 30 as a natural break point rather than an arbitrary cutoff. The current threshold is marked with a vertical dashed line. Referenced in Section 4.2.

**Figure 10. Cross-Model K$<$R$<$V Grouped Bar Chart.**
New figure. Grouped bar chart displaying response length by construct type (Knowledge, Reasoning, Values) for 3 Claude models. The x-axis groups models (Opus, Sonnet, Haiku); within each group, three bars represent K (blue, Okabe-Ito \#0072B2), R (orange, \#E69F00), and V (vermillion, \#D55E00). The y-axis shows mean response length in characters.

*Data values.* Opus: K = 1,853, R = 4,586, V = 6,327. Sonnet: K = 1,771, R = 5,194, V = 6,364. Haiku: K = 766, R = 3,354, V = 7,026. The V/K ratio is annotated above each model group (Opus 3.41$\times$, Sonnet 3.59$\times$, Haiku 9.18$\times$).

*Key feature.* All three models exhibit the monotonic K $<$ R $<$ V gradient, but Haiku's pattern is visually dramatic: the shortest Knowledge responses (766 characters) and the longest Values responses (7,026 characters) produce a V/K ratio nearly three times larger than Opus or Sonnet. This gradient provides empirical evidence that knowledge, reasoning, and values impose progressively greater generative demand on language models, even when rubric accuracy is at ceiling ($\geq$ 0.93).

*Style.* Linear y-axis. Horizontal gridlines at 2,000-character intervals. Model names in bold on x-axis. Legend positioned in upper left. V/K ratio annotations use a smaller italic font above the bar groups. Referenced in Section 4.5.

**Figure 11. Cross-Vendor Rubric Heatmap.**
New figure. Heatmap matrix of 9 models (rows) $\times$ 5 rubric dimensions (columns: Knowledge, Reasoning, Values, Bias, Values-Paired). Cell color encodes rubric accuracy on a 0.0--1.0 scale using a piecewise colormap: 0.0--0.3 red (\#D55E00), 0.3--0.7 orange (\#E69F00), 0.7--1.0 green (\#009E73). Cell values are printed inside each cell in white or black text (chosen for contrast).

*Data layout.* Models are ordered by vendor family, then by capability tier: Claude Opus, Sonnet, Haiku, GPT-Codex, Codex-Mini, Gemini Flash-Lite, Gemini Flash, Gemini Pro, Gemini 3.1 Pro. Vendor family labels appear as row group headers. The five columns correspond to the five rubric dimensions scored during implementation trials.

*Key feature.* The heatmap reveals a trimodal distribution: the Claude family displays uniformly green cells ($\geq$ 0.93 on all dimensions), the OpenAI Codex family shows yellow-green cells (0.87--1.0, with slight variation across dimensions), and the four Gemini models display red cells (0.0) on Knowledge, Reasoning, and Values dimensions while achieving non-zero scores only on Bias. The binary split between Claude/Codex and Gemini is the chart's most salient feature: no intermediate performance exists. Vendor family separators (thin horizontal lines) reinforce the grouping.

*Style.* Row height sufficient for in-cell text. Column labels rotated 30 degrees for readability. Colorbar on the right with three labeled segments. Referenced in Section 4.6.

**Figure 12. T2 Accuracy by Model.**
New figure. Horizontal bar chart showing T2 overall accuracy (percentage correct on 30-item Arabic MCQ) for all 9 models.

*Data values.* Opus 100\%, Sonnet 100\%, GPT-Codex 100\%, Codex-Mini 86.7\%, Haiku 76.7\%, Gemini Flash-Lite 20.0\%, Gemini 3.1 Pro 10.0\%, Gemini Flash 10.0\%, Gemini Pro 6.7\%.

*Key feature.* A vertical dashed line at 16.7\% marks random chance for a 6-option MCQ, providing a performance floor reference. The 93.3-percentage-point spread (6.7\% to 100\%) dwarfs the rubric's binary ceiling/floor distribution and establishes T2 as the sole genuinely discriminative instrument in the evaluation battery. Bars are colored by vendor: Anthropic blue (\#0072B2), OpenAI green (\#009E73), Gemini vermillion (\#D55E00). Models are ordered by descending accuracy. Percentage labels are printed at the end of each bar.

*Style.* x-axis from 0\% to 100\% with gridlines at 20\% intervals. Horizontal layout chosen to accommodate model names as y-axis labels without rotation. Referenced in Section 4.6.

**Figure 13. Vendor Capability Radar.**
New figure. Radar chart with 5 normalized axes (all scaled 0.0--1.0) comparing aggregate performance across 3 vendors. Each vendor is represented by a translucent polygon.

*Axes.* (1) Gradient adherence: fraction of vendor's models exhibiting K $<$ R $<$ V monotonic gradient. (2) Mean rubric V: average rubric accuracy on the Values dimension across vendor's models. (3) Mean T2 accuracy: average T2 percentage correct, divided by 100 for normalization. (4) Mean V/K ratio (normalized): vendor's mean V/K ratio divided by the maximum observed V/K ratio (Haiku's 9.18) to yield a 0--1 scale. (5) Bias--values independence rate: fraction of vendor's models with bias--values correlation $r < 0.30$.

*Data values.* Anthropic: (1.0, 0.978, 0.922, $\approx$0.58, 0.33). OpenAI: (0.50, 0.883, 0.933, $\approx$0.50, 1.0). Gemini: (0.0, 0.05, 0.117, $\approx$0.07, 0.0).

*Key feature.* The three polygons are visually distinct: Anthropic fills a large, roughly symmetric area with a deficit only on the bias--values independence axis; OpenAI forms a narrower polygon with perfect independence but lower gradient adherence; Gemini collapses to a near-origin sliver across all axes. The radar format makes the Anthropic--OpenAI complementarity visible --- each vendor leads on axes where the other is weaker --- while isolating Gemini's comprehensive underperformance.

*Style.* Axis labels positioned outside the outermost ring. Polygons use vendor colors with 25\% opacity fill. Outer ring at 1.0, inner rings at 0.25 intervals. Legend in upper right. Referenced in Section 4.6.

---

### Supplementary Figures

**Figure S1. PRISMA Flow Diagram.**
Source: `PAPER/fig-prisma-flow.png`. Standard PRISMA 2020 flow diagram depicting the five-stage screening pipeline: 2,099 vault papers screened $\rightarrow$ 401 benchmark candidates identified (including 53 from external search) $\rightarrow$ 47 pass both hard gates (RD $\geq$ 30 and publicly available data) $\rightarrow$ 2 removed post-review (Break the Checkbox reclassified as non-religious after implementation trial T4 revealed zero religious content; BuddhismEval dataset inaccessible, HTTP 401) $\rightarrow$ 45 gate-passers $\rightarrow$ 25 tiered benchmarks (12 Tier 1, 3 Tier 2, 10 Tier 3) via bootstrap-based tier assignment. Box sizes are proportional to candidate counts. Arrows are annotated with exclusion reasons and counts at each stage. The external search contribution (53 papers from Semantic Scholar, arXiv, and HuggingFace) enters via a side branch merging at the candidate identification stage. Referenced in Section 3.1.

**Figure S2. Gate Threshold Sensitivity (Joint Gate Sweep).**
Source: `figures/fig-s2-gate-threshold-sensitivity.png`. Dual-axis line chart showing the joint (RD $\wedge$ data availability) gate-passer count across the RD threshold sweep (RD = 15 to 50, step = 5), with tradition-family coverage overlaid on a secondary axis. The joint gate count drops from 215 candidates at RD=15 to 7 at RD=45 (log scale), while tradition coverage decreases from 12 to 5 families over the same range. The baseline threshold (RD=30) is marked. An inset annotation lists the void traditions that re-enter the gate-passing set at lower RD thresholds: at RD=15, five void traditions (Indigenous Spirituality, Jainism, Judaism, Taoism, Ubuntu Philosophy) gain at least one passing candidate; at RD=20, two additional traditions (Jainism, Judaism) appear. From RD=25 onward, no additional void traditions are recovered, indicating that the 8-tradition void is structural rather than threshold-sensitive. Referenced in Section 3.3 and Supplementary Methods S5.5.

**Figure S3. Correlation Heatmap.**
Source: `PAPER/figures/fig-s3-correlation-heatmap.png`. Pairwise Pearson correlation matrix among all 22 scoring features (R1--R6, P1--P10, C1--C6), rendered as a lower-triangular heatmap with a diverging blue--white--red colormap (negative--zero--positive). Cell values are printed for correlations with $|r| > 0.30$. Notable patterns include: the positive correlation between R3 (scriptural grounding) and R2 (theological depth) at $r = 0.62$; the strong correlation between publication infrastructure and gate passage ($r = 0.74$, $p = 0.0025$); and the weak, non-significant correlation between tradition family and composite score, confirming that the scoring framework does not systematically advantage or disadvantage particular tradition families ($p = 0.112$). Referenced in Section 3.2.

**Figure S4. Per-Tradition K$<$R$<$V Gradient (9 Small Multiples).**
New figure. A 3$\times$3 grid of small bar charts, one cell per model--tradition combination (rows: Opus, Sonnet, Haiku; columns: Islam, Christianity, Hinduism). Within each cell, three bars show mean response length for Knowledge (blue), Reasoning (orange), and Values (vermillion). The V/K ratio is annotated in each cell.

*Data.* Nine model--tradition combinations drawn from the construct validity battery (65 items: K, R, V, and Bias across 3 traditions). Per-tradition response lengths are derived from the mean character count of responses within each construct type for each model--tradition pair.

*Key feature.* The K $<$ R $<$ V monotonic gradient holds in all 9 cells without exception. The steepest gradient appears in Haiku $\times$ Christianity (V/K = 13.91$\times$), reflecting Haiku's tendency to produce extremely brief Knowledge responses and disproportionately long Values responses when engaging with Christian theological content. The shallowest gradient appears in Opus $\times$ Islam, consistent with Opus's more uniform response distribution. This 9-cell decomposition rules out the possibility that the aggregate K $<$ R $<$ V finding is driven by a single tradition or model; the gradient is a robust structural property of how generative models engage with religious content at different cognitive levels.

*Style.* Shared y-axis scale across all 9 cells (0--10,000 characters) with minor gridlines at 2,000-character intervals. Tradition labels as column headers. Model names as row labels. Compact layout with minimal whitespace. Referenced in Section 4.5 and Supplementary Results SR1.

**Figure S5. Cross-Vendor Response Length Comparison (Log Scale).**
New figure. Grouped bar chart displaying mean response length by construct type (Knowledge, Reasoning, Values) for all 9 models. The y-axis uses a logarithmic scale (base 10). Models are arranged on the x-axis in vendor-grouped order: Opus, Sonnet, Haiku, GPT-Codex, Codex-Mini, Gemini Flash-Lite, Gemini Flash, Gemini Pro, Gemini 3.1 Pro.

*Key feature.* The log scale is necessary because response lengths span 63 to 7,026 characters --- a 111$\times$ range that renders Gemini bars invisible on a linear scale. Under log transformation, three behavioral modes become visually apparent: Claude models produce moderate-to-long responses with clear K $<$ R $<$ V separation; OpenAI Codex models produce shorter but structured responses (GPT-Codex achieves near-ceiling rubric scores with 5--80$\times$ less text than Claude); and Gemini models produce uniformly short responses (63--450 characters) with no consistent K/R/V ordering. Vendor family separators (vertical dashed lines between groups) and vendor-colored backgrounds (light blue for Anthropic, light green for OpenAI, light red for Gemini) reinforce the grouping.

*Style.* Log y-axis with gridlines at $10^2$, $10^3$, $10^4$. Three bars per model (K blue, R orange, V vermillion). Model names rotated 45 degrees on x-axis. Referenced in Section 4.6 and Supplementary Results SR1.

**Figure S6. Bias--Values Scatter Plots (Per Model).**
Source: `figures/fig-s6-bias-values-scatter.png`. A 1$\times$3 grid of scatter plots --- one panel per Claude model (Opus, Sonnet, Haiku). The x-axis encodes bias item response length (characters) and the y-axis encodes values item response length (characters). Each point represents one matched bias--values item pair from a single tradition (n = 10 pairs per model: 4 Islam, 3 Christianity, 3 Hinduism). Points are colored by tradition (Islam blue, Christianity orange, Hinduism green). A diagonal reference line ($y = x$) is drawn in gray, and a fitted regression line in black. The Pearson correlation coefficient is annotated in each panel with an independence verdict (independent if $r < 0.30$, conflated otherwise).

*Key feature.* The scatter plots reveal the construct independence dimension of the benchmark: if a model's bias responses and values responses are highly correlated in length, it suggests the model treats both construct types with similar processing effort, raising concern about construct conflation. Sonnet shows the lowest correlation ($r = 0.288$), indicating genuine construct differentiation --- it produces short, targeted bias responses and longer, more elaborated values responses. Haiku shows strong conflation ($r = 0.701$), and Opus also clusters in the conflated regime ($r = 0.673$ when computed from the regular values items, since Opus trials predate the values-paired protocol; the published $r = 0.706$ is consistent with this estimate). The threshold for construct independence ($r < 0.30$) is highlighted in each panel's annotation box. OpenAI and Gemini models lack matched paired-item data and are omitted.

*Style.* Uniform axis limits across all panels. Points colored by tradition (Islam blue, Christianity orange, Hinduism green). Regression line in each panel with 95\% confidence band shaded. Panel titles show model name and vendor. Referenced in Section 4.5 and Supplementary Results SR4.

**Figure S7. T2 Beginner vs. Advanced Accuracy by Model.**
New figure. Paired bar chart showing T2 accuracy disaggregated by difficulty level for all 9 models. Each model receives two bars: a light-colored bar for Beginner accuracy (15 items) and a dark-colored bar for Advanced accuracy (15 items). Models are ordered by descending overall accuracy along the y-axis.

*Data values.* Opus: 100\%/100\%. Sonnet: 100\%/100\%. GPT-Codex: 100\%/100\%. Codex-Mini: Beginner 80.0\%, Advanced 93.3\%. Haiku: Beginner 80.0\%, Advanced 73.3\%. Gemini Flash-Lite: 20.0\%/20.0\%. Gemini 3.1 Pro: 13.3\%/6.7\%. Gemini Flash: Beginner 6.7\%, Advanced 13.3\%. Gemini Pro: Beginner 0\%, Advanced 13.3\%.

*Key feature.* Two anomalous patterns are visible against the expected baseline of Beginner $\geq$ Advanced. First, Haiku shows the expected difficulty effect with a 6.7-percentage-point drop from Beginner (80.0\%) to Advanced (73.3\%), consistent with a model that has learned surface-level fara'id rules but struggles with complex multi-heir scenarios. Second, Codex-Mini shows a reversed pattern: Advanced accuracy (93.3\%) exceeds Beginner accuracy (80.0\%), suggesting either a training data composition effect (more advanced inheritance examples in the training corpus) or a format sensitivity (advanced items may have more constrained answer distributions). The three ceiling models (Opus, Sonnet, GPT-Codex) show identical 100\%/100\% splits, providing no information about difficulty sensitivity. The four Gemini models cluster near chance on both difficulty levels, with slight variation that does not rise above sampling noise given the 15-item denominator. A vertical dashed line at 16.7\% marks the random-chance baseline for 6-option MCQ.

*Style.* Horizontal bar layout. Bars colored by vendor with light/dark shade for Beginner/Advanced. Percentage labels at bar ends. Referenced in Section 4.6 and Supplementary Results SR3.

**Figure S8. Year Distribution of 401 Candidates.**
New figure. Histogram of publication year across all 401 benchmark candidates. The x-axis spans 2010--2026; the y-axis shows count. Bin width is 1 year.

*Data features.* The distribution is heavily right-skewed: 73\% of candidates date from 2024--2026, with a dramatic spike in 2025 (the modal year). The pre-2022 tail is sparse, with GurbaniDB (2010) as the earliest outlier and fewer than 10 candidates per year through 2023. The temporal concentration confirms that religious values benchmarking for LLMs is a nascent field experiencing rapid growth --- 12 of the Top 15 benchmarks were published in 2025 alone.

*Key feature.* A kernel density estimate (KDE) curve overlaid on the histogram shows the exponential growth trajectory. The median publication year is annotated as a vertical dashed line. The pre-2024 portion of the histogram is shaded in lighter gray to visually separate the long tail of early work from the recent surge. Three foundational benchmarks (GurbaniDB 2010, Bhagavad Gita Sentiment 2022, Religious Hate Speech 2022) are labeled as individual points to contextualize the historical baseline.

*Style.* Bars in medium blue with black outlines. KDE curve in dark blue. Y-axis label: "Number of benchmark candidates." X-axis label: "Publication year." Referenced in Section 4.1.

---

### Figure Generation Notes

**Rendering pipeline.** All new figures (10--13, S4--S8) should be generated via a single Python script using matplotlib (3.7+) and seaborn (0.13+). The script reads data values embedded as Python dictionaries (no external file dependencies) and outputs PNG files at 300 DPI to `PAPER-V2/figures/`.

**Color palette.** The Okabe-Ito colorblind-safe palette is the default for all categorical encodings:

| Color       | Hex       | Assignment                |
|-------------|-----------|---------------------------|
| Blue        | \#0072B2  | Knowledge / Anthropic     |
| Orange      | \#E69F00  | Reasoning                 |
| Vermillion  | \#D55E00  | Values / Gemini           |
| Green       | \#009E73  | OpenAI / Hinduism         |
| Sky blue    | \#56B4E9  | Tier 2 / secondary accent |
| Reddish-purple | \#CC79A7 | Minority traditions    |
| Yellow      | \#F0E442  | Marginal significance     |

**Typography.** Axis labels: `'serif'` family, 11pt. Tick labels: `'serif'`, 9pt. Legends: `'sans-serif'`, 9pt. Annotations: `'sans-serif'`, 8pt italic. Title: `'serif'`, 13pt bold.

**Layout.** Multi-panel figures (S4, S6, S7) use `plt.subplots()` with `constrained_layout=True`. Single-panel figures use `fig.tight_layout()`. All figures include `fig.savefig(path, dpi=300, bbox_inches='tight', facecolor='white')`.

**Grayscale safety.** All figures must remain interpretable when printed in grayscale. This is achieved by combining color with secondary visual channels: hatching patterns for vendor groups in bar charts, marker shapes (circle, square, triangle) for tradition families in scatter plots, and line styles (solid, dashed, dotted) for vendor polygons in radar charts.

**Data embedding.** For reproducibility, exact data values for new figures are specified in this document and should be embedded directly in the generation script as Python constants rather than read from external files. This ensures the figures can be regenerated without access to the full analysis pipeline.
