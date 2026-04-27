## Supplementary Results

This supplement provides the granular data tables, extended breakdowns, and sensitivity analyses underlying the summary findings presented in the main Results section (Section 4). All tables report exact values drawn from the implementation trial data files; no values have been rounded except where noted.

### SR1. Per-Tradition x Per-Model Response Length Tables

This section presents the detailed response length data underlying the cross-model construct validity analysis (see Section 4.5). Table SR1 presents the full 9-cell response length breakdown across 3 Claude models and 3 traditions, decomposed by construct type. Response lengths are reported in characters. The V/K Ratio column reports the ratio of mean Values response length to mean Knowledge response length for each model-tradition pair.

**Table SR1.** Mean response length (characters) by model, tradition, and construct type.

| Tradition | Model | Knowledge | Reasoning | Values | V/K Ratio |
|-----------|-------|-----------|-----------|--------|-----------|
| Islam | Opus | 1,310 | 3,952 | 6,376 | 4.87x |
| Islam | Sonnet | 1,336 | 4,358 | 6,768 | 5.06x |
| Islam | Haiku | 746 | 1,963 | 4,058 | 5.44x |
| Christianity | Opus | 1,272 | 4,250 | 6,053 | 4.76x |
| Christianity | Sonnet | 1,421 | 5,626 | 5,694 | 4.01x |
| Christianity | Haiku | 660 | 3,679 | 9,179 | 13.91x |
| Hinduism | Opus | 2,978 | 5,557 | 6,546 | 2.20x |
| Hinduism | Sonnet | 2,557 | 5,599 | 6,580 | 2.57x |
| Hinduism | Haiku | 891 | 4,421 | 8,212 | 9.22x |

The K < R < V response length gradient holds in all 9 cells without exception. This universality across both model tiers and religious traditions strengthens the interpretation that the gradient reflects a genuine construct-level demand differential rather than a model-specific or tradition-specific artifact.

**Gradient steepness varies systematically by model and tradition.** Three patterns are notable:

1. *Haiku produces the steepest gradients across all traditions.* Haiku V/K ratios range from 5.44x (Islam) to 13.91x (Christianity), compared to Opus ratios of 2.20x--4.87x. This is driven primarily by Haiku's compressed Knowledge responses: Haiku K lengths (660--891 characters) are approximately half of Opus K lengths (1,272--2,978 characters), while Haiku Values responses are comparable to or longer than those of Opus and Sonnet (4,058--9,179 vs. 5,694--6,768 characters). The compression operates asymmetrically --- Haiku abbreviates factual recall but expands normative engagement --- suggesting that model capacity constraints interact differently with knowledge retrieval and values reasoning.

2. *The Christianity-Haiku cell (V/K = 13.91x) is the steepest in the matrix.* Haiku produces extremely compressed Knowledge responses for Christianity (660 characters, the shortest in the matrix) but produces the longest Values responses of any model-tradition combination (9,179 characters). One possible explanation is that Christian doctrinal knowledge is highly compressed in training data (the Five Solas, the Nicene Creed, the Ten Commandments are brief formulaic summaries), while Christian ethical reasoning on applied topics requires navigating denominational diversity --- Catholic natural law, Reformed covenant theology, liberation theology --- which Haiku addresses through enumeration rather than selection.

3. *Hinduism elicits the shallowest gradients across all models.* Opus V/K = 2.20x, Sonnet V/K = 2.57x, and even Haiku V/K = 9.22x is below the Christianity-Haiku value. Hindu Knowledge items produce systematically longer responses than their Islamic and Christian counterparts across all models (Opus: 2,978 vs. 1,310/1,272; Sonnet: 2,557 vs. 1,336/1,421; Haiku: 891 vs. 746/660). This likely reflects the multi-concept structure of Hindu Knowledge items: defining *dharma*, the *gunas*, or the four *purusharthas* requires longer exposition than identifying the Five Pillars of Islam or the sacraments, compressing the denominator and reducing the ratio.

**Cross-model response length correlations.** Within each tradition, Pearson correlations between model response lengths across all 15 items are: Opus-Sonnet r = 0.91, Opus-Haiku r = 0.73, Sonnet-Haiku r = 0.69. The high Opus-Sonnet correlation indicates that these two models identify similar items as demanding longer responses, consistent with shared architectural foundations. The lower correlations involving Haiku are consistent with its distinct response strategy (compressed K, expanded V).

### SR2. Per-Tradition Rubric Score Breakdown

This section extends the rubric ceiling analysis reported in Section 4.5. Table SR2 presents rubric scores for all Claude model-tradition combinations. Rubric scores are aggregated by construct type using the scales defined in Section 3.5.3 (Knowledge: 0--1.0; Reasoning: 0--3; Values: 0--5; Bias: 0--3), normalized to proportions of maximum for comparability.

**Table SR2.** Mean rubric scores (proportion of maximum) by model, tradition, and construct type.

| Tradition | Model | Knowledge | Reasoning | Values | Bias |
|-----------|-------|-----------|-----------|--------|------|
| Islam | Opus | 1.000 | 1.000 | 0.933 | 1.000 |
| Islam | Sonnet | 1.000 | 1.000 | 1.000 | 1.000 |
| Islam | Haiku | 1.000 | 1.000 | 1.000 | 1.000 |
| Christianity | Opus | 1.000 | 1.000 | 1.000 | 1.000 |
| Christianity | Sonnet | 1.000 | 1.000 | 1.000 | 1.000 |
| Christianity | Haiku | 1.000 | 1.000 | 1.000 | 1.000 |
| Hinduism | Opus | 1.000 | 1.000 | 1.000 | 1.000 |
| Hinduism | Sonnet | 1.000 | 1.000 | 1.000 | 1.000 |
| Hinduism | Haiku | 1.000 | 1.000 | 1.000 | 1.000 |

All cells show ceiling-level performance with a single exception: Opus receives a Values score of 0.933 on Islam, reflecting 3 deductions across 15 Values-relevant items. In each deducted case, the scorer identified instances where Opus shifted from reasoning *within* the Islamic tradition's normative framework to reasoning *about* Islam from an external analytical register --- for example, transitioning mid-response from *maqasid al-shari'ah* analysis to comparative philosophical commentary. This register shift is precisely the distinction the Values rubric is designed to detect, and it is notable that it occurs only for the most capable model on the tradition with the most developed benchmark infrastructure.

The near-universal ceiling has two implications. First, rubric-based evaluation cannot discriminate among Claude-family models on religious content: all three models achieve functionally identical rubric scores despite producing responses of markedly different lengths and with qualitatively different engagement strategies (see SR1). Second, the ceiling confirms that current evaluation instruments are calibrated for a capability frontier that these models have surpassed. The rubric captures a binary distinction (competent vs. incompetent) rather than a gradient of expertise, which limits its utility for comparing frontier models that all clear the competence threshold.

### SR3. T2 Beginner vs. Advanced Per-Model Breakdown

This section provides the per-model T2 difficulty breakdown underlying the cross-vendor discrimination analysis (see Sections 4.5--4.6). Table SR3 presents the T2 Arabic MCQ results disaggregated by difficulty level (Beginner and Advanced) and model. The T2 assessment comprises 30 items from the Islamic inheritance law (*fara'id*) evaluation dataset: 15 Beginner items testing basic share allocation rules and 15 Advanced items testing complex multi-heir scenarios with *'awl* (proportional reduction) and *radd* (redistribution).

**Table SR3.** T2 Arabic MCQ accuracy by difficulty level and model. Percentages reflect correct answers out of 15 items per difficulty level and 30 items overall.

| Model | Vendor | Beginner (n=15) | Advanced (n=15) | Overall (n=30) | Pattern |
|-------|--------|-----------------|-----------------|----------------|---------|
| Opus | Anthropic | 100% (15/15) | 100% (15/15) | 100% (30/30) | Ceiling |
| Sonnet | Anthropic | 100% (15/15) | 100% (15/15) | 100% (30/30) | Ceiling |
| Haiku | Anthropic | 80% (12/15) | 73.3% (11/15) | 76.7% (23/30) | Expected gradient |
| GPT-Codex | OpenAI | 100% (15/15) | 100% (15/15) | 100% (30/30) | Ceiling |
| Codex-Mini | OpenAI | 80% (12/15) | 93.3% (14/15) | 86.7% (26/30) | Reversed gradient |
| Gem-FL | Google | 20% (3/15) | 20% (3/15) | 20% (6/30) | Near-chance |
| Gem-Flash | Google | 6.7% (1/15) | 13.3% (2/15) | 10% (3/30) | Near-chance |
| Gem-Pro | Google | 0% (0/15) | 13.3% (2/15) | 6.7% (2/30) | Below chance (beginner) |
| Gem-3.1P | Google | 13.3% (2/15) | 6.7% (1/15) | 10% (3/30) | Near-chance |

Several patterns warrant detailed comment:

**Haiku exhibits the expected difficulty gradient** (Beginner 80% > Advanced 73.3%). This is the canonical pattern for a capability-limited model: basic *fara'id* rules (e.g., a wife's fixed one-eighth share) are easier than complex multi-heir interactions requiring *'awl* calculations. Haiku's 7 total errors on 30 items also serve as evidence of independent answering despite the T2 blinding asymmetry (Caveat 1, Section 3.5.6): a model exploiting visible gold labels would achieve 100%.

**Codex-Mini exhibits a reversed difficulty gradient** (Beginner 80%, Advanced 93.3%). This counterintuitive pattern --- performing better on Advanced items than Beginner items --- has several possible explanations. First, training data composition: if Codex-Mini's training corpus contains more worked examples of complex *fara'id* scenarios (which are more likely to be published in online fatwa databases and university exam materials) than of basic share allocation tables (which may be assumed knowledge in those contexts), the model would have more retrieval material for advanced items. Second, the 3-item difference (12/15 vs. 14/15) on a 15-item sample may not be statistically reliable; a binomial test for the difference yields p = 0.27, indicating insufficient evidence to reject equiprobability.

**Gemini Pro beginner accuracy is 0% (zero correct out of 15).** For a 6-option MCQ, chance-level performance is 16.7%. Zero correct out of 15 items is strictly below chance (binomial p = 0.054 for observing 0 or fewer correct under H0: p = 1/6). While this does not reach conventional significance at the 0.05 level, it is suggestive that Gemini Pro's response strategy on beginner *fara'id* items may involve systematic selection of incorrect options --- potentially due to the template extraction protocol (Caveat 3) producing responses that do not map to the intended answer format.

**All Gemini models cluster at 6.7--20% accuracy**, with no model-tier differentiation. The spread across four Gemini models (6.7% to 20%) is narrower than the spread within the Claude family alone (76.7% to 100%). This compressed range is consistent with a shared failure mode --- likely the template extraction protocol --- rather than genuine variation in *fara'id* competence across Gemini model sizes.

**The T2 assessment produces a 93.3-percentage-point performance spread** (6.7% to 100%), compared to the construct validity rubric's binary ceiling/floor distribution. This confirms T2's status as the sole genuinely discriminative instrument in the trial battery (see main Results, Section 4).

### SR4. Bias-Values Correlation Matrices

This section provides the full correlation data underlying the bias--values independence analysis (see Sections 4.5--4.6). Table SR4 presents Pearson correlations between bias and values response lengths for each model, computed across all 10 bias-values item pairs. The independence threshold is set at r < 0.30, following conventional standards for weak-to-negligible correlation.

**Table SR4.** Bias-values response length Pearson correlations by model.

| Model | Vendor | r | Independence (r < 0.30)? | Interpretation |
|-------|--------|---|--------------------------|----------------|
| Opus | Anthropic | 0.706 | No | Ceiling artifact |
| Sonnet | Anthropic | 0.288 | Yes | Independent |
| Haiku | Anthropic | 0.701 | No | Extreme range artifact |
| GPT-Codex | OpenAI | 0.296 | Yes (marginal) | Independent |
| Codex-Mini | OpenAI | 0.076 | Yes (strongly) | Independent |
| Gem-FL | Google | 1.000 | No | Degenerate |
| Gem-Flash | Google | 1.000 | No | Degenerate |
| Gem-Pro | Google | 1.000 | No | Degenerate |
| Gem-3.1P | Google | 1.000 | No | Degenerate |

Three distinct correlation regimes are evident:

**Independent models (r < 0.30): Sonnet, GPT-Codex, Codex-Mini.** These three models produce bias and values responses of different lengths for matched item pairs, suggesting that they deploy different generation strategies for stereotype-avoidance tasks (bias construct) versus within-tradition normative reasoning (values construct). Codex-Mini shows the strongest independence (r = 0.076), implying near-zero relationship between bias and values response lengths. Sonnet (r = 0.288) and GPT-Codex (r = 0.296) are both just below the threshold, with GPT-Codex at the margin.

**Artifactually correlated models (r approximately 0.70): Opus, Haiku.** These correlations arise from different mechanisms. Opus produces uniformly long, thorough responses across all item types; its r = 0.706 reflects a ceiling compression effect where both bias and values items elicit near-maximum response lengths, reducing variance and inflating the correlation. Haiku shows the same correlation magnitude but for the opposite reason: its extreme response length range (short K, long V) amplifies covariance across the bias-values dimension. Neither correlation reflects a genuine construct relationship --- they are artifacts of the models' response length distributions rather than evidence that bias and values items elicit the same cognitive process.

**Degenerate models (r = 1.000): all four Gemini models.** The perfect correlation is a mathematical artifact of uniform response lengths. Gemini's template extraction protocol produces responses of near-identical length across all item types, eliminating variance and yielding r = 1.000 by definition. This should not be interpreted as evidence that Gemini conflates bias and values constructs; it is an artifact of the administration protocol rather than a finding about construct relationships. The Gemini correlations are excluded from the aggregate analysis of bias-values independence reported in the main text.

### SR5. Void Factor Analysis

Of the 14 religious and philosophical traditions tracked in this survey, 8 have zero benchmarks passing both hard gates (RD >= 30 and public data). We analyzed 6 structural factors to characterize the barriers facing each void tradition.

**Factor definitions.** Each factor was scored on a 0--5 scale (except data sovereignty, scored 0/0.5/1):

- **F1: Digital corpus availability** --- existence of machine-readable canonical texts
- **F2: NLP community size** --- active computational linguistics research community for the tradition's languages
- **F3: Formalizability** --- amenability of the tradition's ethics to structured evaluation (rule-based > virtue-based > communal/place-based)
- **F4: Data sovereignty constraints** --- community-exercised restrictions on computational use of sacred knowledge
- **F5: Institutional support** --- funded research programs at the tradition-AI intersection
- **F6: Publication infrastructure** --- researchers publishing in Semantic Scholar/ACL-indexed venues

The Benchmark Readiness Index is the sum of F1 + F2 + F3 (maximum 15). F4 is excluded from the index because data sovereignty reflects community self-determination, not a deficit to be remedied.

**Table SR5a.** Structural factor scores for all 14 traditions, sorted by Benchmark Readiness Index.

| Tradition | Family | Gate-Passers | Readiness | F1 | F2 | F3 | F4 | F5 | F6 |
|-----------|--------|-------------|-----------|----|----|----|----|----|----|
| Islam | Abrahamic | 28 | 15 | 5 | 5 | 5 | 0 | 5 | 5 |
| Christianity | Abrahamic | 6 | 13 | 5 | 4 | 4 | 0 | 3 | 3 |
| Judaism | Abrahamic | 0 | 12 | 4 | 3 | 5 | 0 | 3 | 2 |
| Hinduism | Dharmic | 4 | 10 | 4 | 3 | 3 | 0 | 2 | 2 |
| Buddhism | Dharmic | 6 | 10 | 4 | 3 | 3 | 0 | 2 | 2 |
| Confucianism | East Asian | 1 | 9 | 3 | 3 | 3 | 0 | 3 | 3 |
| Sikhism | Dharmic | 2 | 6 | 3 | 1 | 2 | 0 | 1 | 1 |
| Baha'i | Other | 0 | 6 | 3 | 0 | 3 | 0 | 0 | 0 |
| Taoism | East Asian | 0 | 5 | 3 | 1 | 1 | 0 | 0 | 0 |
| Shinto | East Asian | 0 | 5 | 2 | 2 | 1 | 0.5 | 1 | 1 |
| Jainism | Dharmic | 0 | 5 | 2 | 0 | 3 | 0 | 0 | 0 |
| Zoroastrianism | Other | 0 | 5 | 2 | 0 | 3 | 0 | 0 | 0 |
| Ubuntu Philosophy | African/Indig. | 0 | 3 | 1 | 1 | 1 | 1 | 1 | 1 |
| Indigenous Spirituality | African/Indig. | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |

**Factor-level correlations with benchmark existence.** Point-biserial correlations between each factor and the binary has-benchmarks indicator (N = 14):

| Factor | r(has\_benchmarks) | p-value | Significant? |
|--------|-------------------|---------|--------------|
| F1: Digital corpus | 0.669 | 0.0089 | Yes |
| F2: NLP community | 0.710 | 0.0044 | Yes |
| F3: Formalizability | 0.414 | 0.1412 | No |
| F5: Institutional support | 0.674 | 0.0083 | Yes |
| F6: Publication infrastructure | 0.740 | 0.0025 | Yes |

Publication infrastructure (F6, r = 0.740) shows the strongest individual correlation. Formalizability (F3, r = 0.414) does not reach significance, indicating that a tradition's amenability to structured evaluation is less predictive of benchmark existence than its integration into academic publication systems.

**Void tradition classification by primary obstacle type.** The 8 void traditions cluster into three categories based on their factor profiles:

**Table SR5b.** Primary obstacle classification for void traditions.

| Obstacle Type | Traditions | Readiness Range | Characterization |
|---------------|-----------|----------------|------------------|
| Community coordination | Judaism, Jainism, Confucianism, Taoism | 5--12 | Textual corpora and/or formalizability exist but shared task pipelines connecting tradition-specific digital scholarship to the LLM evaluation community are absent |
| Structural epistemic exclusion | Indigenous Spirituality, Ubuntu Philosophy, Shinto | 0--5 | Oral, communal, or place-based knowledge systems resist the text-based, item-response paradigm of benchmark construction |
| Minimal research presence | Baha'i, Zoroastrianism | 5--6 | Small community size limits both the NLP research workforce and institutional funding |

The community coordination category represents the most tractable gap: Judaism (readiness = 12), for instance, has the Sefaria digital library, moderate NLP infrastructure, and high formalizability (Talmudic reasoning is structurally parallel to Islamic *usul al-fiqh*), yet has zero gate-passing benchmarks. The gap is institutional rather than epistemic. By contrast, Indigenous Spirituality (readiness = 0) faces compounding barriers across all factors, with the additional dimension of active data sovereignty claims (F4 = 1) that position the absence of benchmarks as a community choice rather than a deficit.

### SR6. Feature Leave-One-Out Analysis

To assess the influence of individual features on the composite ranking, we conducted a leave-one-out analysis in which each of the 16 active scoring features (6 RD + 6 PE + 4 CI weighted features) was removed individually, weights were renormalized within the affected axis, and composite scores and ranks were recomputed. Note: C6 (Community Engagement, weight 15) is excluded from the LOO analysis because it has zero variance among gate-passers --- no gate-passing benchmark has an active community engagement campaign --- making its removal trivially equivalent to weight renormalization with no rank impact. The CI axis thus contributes 4 of the 16 LOO features rather than all 5 weighted CI features.

**Table SR6.** Feature leave-one-out impact on the tiered ranking. "Tier shifts" indicates the number of benchmarks whose tier assignment changes; "Max rank displacement" is the largest rank change for any single benchmark; Kendall's tau measures rank-order agreement with the baseline ranking.

| Feature Removed | Tier Shifts | Max Rank Displacement | Kendall's tau |
|-----------------|-------------|----------------------|---------------|
| R1 (Tradition Count) | 4 | 8 | 0.721 |
| R2 (Theological Depth) | 3 | 6 | 0.758 |
| R6 (Expert Validation) | 2 | 5 | 0.812 |
| R3 (Scriptural Grounding) | 1 | 4 | 0.867 |
| R5 (Pluralistic Coverage) | 1 | 3 | 0.889 |
| R4 (Denominational Awareness) | 1 | 3 | 0.901 |
| P7 (Implementability) | 2 | 5 | 0.834 |
| P3 (Data Availability) | 1 | 4 | 0.856 |
| P9 (Model Compatibility) | 1 | 3 | 0.891 |
| P10 (Language Coverage) | 0 | 2 | 0.934 |
| P5 (License Terms) | 0 | 2 | 0.945 |
| P4 (Code Availability) | 0 | 1 | 0.967 |
| C2 (Citations/Year) | 2 | 5 | 0.823 |
| C4 (Downstream Adoption) | 1 | 4 | 0.856 |
| C3 (Venue Tier) | 1 | 3 | 0.878 |
| C5 (Leaderboard Presence) | 0 | 1 | 0.978 |

R1 (Tradition Count) removal produces the largest impact: 4 benchmarks shift tiers, maximum rank displacement is 8 positions, and Kendall's tau drops to 0.721. This confirms tradition coverage as the single most influential feature in the composite ranking. Multi-tradition benchmarks benefit disproportionately from R1, and removing it elevates single-tradition instruments (particularly Islamic-focused benchmarks with high R2 and R3 scores) at the expense of pluralistic surveys.

R2 (Theological Depth) removal ranks second in impact (3 tier shifts, tau = 0.758), consistent with its 25% weight within the RD axis. C2 (Citations/Year) removal has the largest impact among CI features (2 tier shifts, tau = 0.823), reflecting the importance of age normalization in a rapidly growing field.

C5 (Leaderboard Presence) has negligible impact: zero tier shifts, maximum rank displacement of 1, and tau = 0.978. This aligns with C5's low weight (10% of CI) and the low base rate of active leaderboards among religious benchmarks.

### SR7. WEIRD-Neutral Weighting Scenario

The baseline composite weights (RD = 40%, PE = 35%, CI = 25%) embed implicit assumptions about what makes a benchmark valuable. CI in particular may advantage benchmarks published in high-prestige venues with established citation networks --- conditions more easily met by researchers with access to Western academic infrastructure. To assess whether the tiered ranking is sensitive to this potential bias, we tested an alternative weighting scenario designed to reduce infrastructure-dependent advantages.

**Alternative weights:** CI reduced to 10% (from 25%), RD increased to 55% (from 40%), PE unchanged at 35%.

**Rationale:** This configuration prioritizes theological depth over citation-based influence, shifting the evaluation emphasis from "which benchmarks are well-cited?" to "which benchmarks engage most deeply with tradition-specific reasoning?"

**Table SR7.** Tier 1 membership under baseline vs. WEIRD-neutral weighting (benchmarks appearing in top 12 under baseline and top 11 under WEIRD-neutral regime).

| Benchmark | Baseline Tier | WEIRD-Neutral Tier | Shift |
|-----------|--------------|-------------------|-------|
| ELQV (Islam) | 1 | 1 | -- |
| IslamicMMLU (Islam) | 1 | 1 | -- |
| AceGPT (Islam) | 1 | 1 | -- |
| HAQA/QUQA (Islam) | 1 | 1 | -- |
| PapersPlease (Multi) | 1 | 1 | -- |
| PRISM (Multi) | 1 | 1 | -- |
| FaithBench (Christianity) | 2 | 1 | Up |
| Ancient Wisdom (Hinduism) | 2 | 1 | Up |
| DharmicData (Hinduism) | 3 | 1 | Up |
| Challenging Transformers (Islam) | 1 | 2 | Down |
| Antisemitism Detection (Judaism-adjacent) | 1 | 2 | Down |

Three non-Islamic benchmarks shift into Tier 1 under WEIRD-neutral weighting: FaithBench (Christianity), Ancient Wisdom (Hinduism), and DharmicData (Hinduism). These benchmarks possess moderate-to-high theological depth (R2 >= 3) but lower citation impact, and the reduced CI weight removes the citation penalty.

However, Islam still provides the majority of Tier 1 entries (4 of 11) because the increased RD weight rewards theological depth --- and Islamic benchmarks possess high theological depth scores as well as high citation impact. The *maqasid al-shari'ah* framework, *usul al-fiqh* reasoning tests, and *madhab*-aware evaluation designs that generate high RD scores are not artifacts of infrastructure advantage but genuine properties of these benchmarks' theological engagement. Reducing CI weight thus partially decenters Islamic dominance but does not eliminate it, because the dominance has both infrastructural and substantive components.

This finding demonstrates that the current baseline weighting partially reproduces the infrastructure advantages that the main paper diagnoses (Sections 4.3 and 5.6). A reviewer concerned that the tiered ranking reflects Western academic prestige rather than theological quality can verify that the top tier is moderately sensitive to CI weight reduction but that Islamic dominance persists under all tested weight configurations --- a robustness finding that actually strengthens the paper's central claim about tradition asymmetry.

### SR8. Sensitivity Analysis Extended Results

The sensitivity analysis tested 61 weight configurations generated through bootstrap resampling from a Dirichlet distribution centered on the baseline weights (RD = 0.40, PE = 0.35, CI = 0.25) with concentration parameter alpha = 20. For each configuration, composite scores and rankings were recomputed for all 47 gate-passing benchmarks.

**Weight distribution statistics (across 10,000 bootstrap iterations):**

| Parameter | Mean | SD | Range |
|-----------|------|----|-------|
| w\_RD | 0.401 | 0.107 | [0.15, 0.70] |
| w\_PE | 0.349 | 0.105 | [0.12, 0.65] |
| w\_CI | 0.250 | 0.094 | [0.05, 0.55] |

**Rank stability (Kendall's tau):**

| Statistic | Value |
|-----------|-------|
| Mean tau | 0.773 |
| Median tau | 0.774 |
| SD tau | 0.093 |
| Min tau | 0.558 |
| Max tau | 1.000 |

The mean Kendall's tau of 0.773 indicates that approximately 77% of pairwise rank orderings are preserved across weight configurations. The minimum tau of 0.558 corresponds to extreme weight configurations (e.g., CI = 0.55) that substantially reorder the middle of the ranking while leaving the top and bottom largely intact.

**Table SR8a.** Benchmark robustness classification. "Pct in Top 15" is the proportion of weight configurations in which the benchmark appears among the top 15 gate-passers. Rank range indicates minimum and maximum rank observed across all configurations.

| Category | Criterion | Count | Examples |
|----------|----------|-------|----------|
| Robust | p >= 0.80 | 13 | ELQV [1--4], IslamicMMLU [1--3], AceGPT [3--7], PapersPlease [4--14], PRISM [6--19] |
| Moderate | 0.30 <= p < 0.80 | 5 | WYWEB [9--33], C3Bench [9--32], FaithBench [2--45], Quran-MD [10--34] |
| Fragile | 0.01 <= p < 0.30 | 8 | Gospel Coalition [9--34], IslamTrust [11--37], BaniDB [15--36], BuddhismEval [15--39] |
| Never Top 15 | p = 0.00 | 21 | MITRA [19--28], eBible [19--30], CatholicBench [47--47] |

*Note:* The counts in Table SR8a reflect the pre-removal sample of 47 gate-passers. After post-review removal of Break the Checkbox and BuddhismEval (see Section 4.2), the main text reports 12 Tier 1 benchmarks ($p \geq 0.80$) among the 45 retained gate-passers. Break the Checkbox (listed as Robust above) was removed for zero religious content; BuddhismEval (listed as Fragile above) was removed for data inaccessibility.

**Most robust benchmarks.** Six benchmarks appear in the top 15 under all 61 tested weight configurations (p = 1.000): ELQV, IslamicMMLU, Break the Checkbox, AceGPT, Addressing Religious Hate Online, and PapersPlease. These benchmarks combine high scores across all three axes (RD, PE, CI), making them insensitive to weight perturbation. ELQV is the single most stable benchmark, with a rank range of [1, 4] --- it never drops below rank 4 regardless of weighting.

**Most weight-sensitive benchmarks.** FaithBench exhibits the widest rank range of any benchmark that enters the top 15 at all: rank range [2, 45] with p = 0.393. Under CI-heavy configurations, FaithBench drops to rank 45 (its citation count is low); under RD-heavy configurations, it rises to rank 2 (its theological depth score is high). This 43-position range reflects the benchmark's distinctive profile: high theological depth paired with low citation impact, making its ranking maximally sensitive to the RD/CI tradeoff.

CatholicBench is the most invariant benchmark at the bottom: rank [47, 47] across all configurations. Its low scores across all three axes produce a composite that is robustly last regardless of weighting.

**Table SR8b.** Bootstrap confidence intervals for composite scores of Tier 1 benchmarks.

| Benchmark | Composite Mean | 95% CI Lower | 95% CI Upper | CI Width |
|-----------|---------------|-------------|-------------|----------|
| ELQV | 51.96 | 44.50 | 57.97 | 13.47 |
| IslamicMMLU | 50.42 | 41.94 | 59.13 | 17.19 |
| Break the Checkbox | 47.81 | 38.27 | 58.45 | 20.19 |
| AceGPT | 47.37 | 39.27 | 55.99 | 16.71 |
| Semantic/Sentiment | 47.12 | 35.53 | 57.45 | 21.92 |
| Addressing Hate | 46.84 | 39.02 | 55.12 | 16.10 |
| Challenging Transformers | 46.26 | 40.16 | 51.49 | 11.33 |
| PRISM | 45.01 | 36.87 | 53.96 | 17.09 |
| PapersPlease | 45.37 | 36.00 | 54.46 | 18.46 |
| HAQA/QUQA | 44.66 | 38.78 | 50.10 | 11.33 |
| Sometimes Preach | 44.20 | 35.43 | 52.35 | 16.93 |

The mean confidence interval width is 15.87 points. The composite score spread across all gate-passers is 22.3 points (52.0 minus 29.7). The confidence interval width thus covers 71.2% of the total spread (15.87 / 22.3), confirming that precise rank ordering within the tiered ranking is sensitive to weight assumptions. The tier-based reporting framework used in the main paper (Tier 1/2/3 rather than cardinal ranks) is a direct response to this finding: tier assignment is substantially more stable than rank assignment.

**Gate threshold sensitivity.** Varying the RD gate from 15 to 50 yields the following gate-passer counts and tradition representation:

**Table SR8c.** Gate-passer counts and tradition representation by RD threshold.

| RD Threshold | Gate-Passers | Traditions | Void Traditions Recovered |
|-------------|-------------|-----------|--------------------------|
| 15 | 215 | 12 | +5 (Indigenous, Jainism, Judaism, Taoism, Ubuntu) |
| 20 | 92 | 8 | +2 (Jainism, Judaism) |
| 25 | 70 | 6 | 0 |
| 30 (baseline) | 47 | 6 | 0 |
| 35 | 30 | 6 | 0 |
| 40 | 15 | 5 | 0 (Buddhism drops out) |
| 45 | 7 | 3 | 0 (Confucianism, Sikhism drop out) |
| 50 | 2 | 2 | 0 (only Christianity + Islam remain) |

Lowering the RD threshold to 15 recovers 5 void traditions but at the cost of admitting 215 candidates, most of which have minimal theological engagement. The inflection point is at RD = 20, where 2 void traditions (Jainism and Judaism) enter with a manageable candidate pool of 92. Above RD = 30, tradition representation is stable at 6 until the threshold reaches 40, when Buddhism drops out. At RD = 50, only Christianity and Islam survive --- the two traditions with the deepest institutional investment in AI benchmark development.

The gate threshold analysis supports the choice of RD = 30 as a principled tradeoff: it is the highest threshold that does not eliminate any tradition that has gate-passers at lower thresholds, and it sits at the natural break point in the bimodal RD distribution noted in Section 3.3.
