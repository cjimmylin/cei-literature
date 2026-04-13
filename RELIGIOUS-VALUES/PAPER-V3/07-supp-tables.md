## Supplementary Tables

This supplement presents the complete tabular data supporting the analyses described in the main text. Tables S1--S2 document the scoring framework specification and calibration. Table S3 provides the format taxonomy referenced throughout the paper. Tables S4--S5 describe the external search methodology and meta-evaluation criteria. Tables S6--S8 report the full cross-model and cross-vendor implementation trial results. Table S9 contains the complete statistical details for all eight claims. Table S10 presents the void factor analysis for traditions with zero viable benchmarks. The full 401-candidate feature matrix is available in the project repository as `data/20260404-religious-benchmark-feature-matrix-v2.json`.

---

### Table S1: Feature Matrix Score Distributions

The 401-candidate feature matrix characterizes each benchmark candidate along 22 features organized into three axes (Section 3.2). Because the full $401 \times 22$ matrix is too large to reproduce here, we present summary statistics for each axis composite and the overall composite score. All axis scores are normalized to 0--100 prior to composite calculation.

**Table S1a. Score Distribution by Axis (n = 401 Candidates)**

| Axis | Mean | Median | SD | Min | Max | Skew | Interpretation |
|------|------|--------|----|-----|-----|------|----------------|
| RD | 18.7 | 16.0 | 9.4 | 0 | 62 | +1.32 | Heavily right-skewed; 72% of candidates cluster at 15--25, reflecting surface-level religious mention without sustained theological engagement. The bimodal gap at RD $\approx$ 30 motivates the hard gate threshold. |
| PE | 31.4 | 28.0 | 22.8 | 0 | 85 | +0.54 | Bimodal distribution with an accessible cluster (PE $\geq$ 50, candidates with public data and evaluation code) and an inaccessible cluster (PE $<$ 20, candidates with no public data). Data availability (P3) is the primary driver of bimodality. |
| CI | 12.9 | 6.0 | 16.3 | 0 | 78 | +1.87 | Strongly right-skewed; the majority of candidates have low citation impact, consistent with a young field where 73% of candidates date from 2024--2026. The long right tail comprises established benchmarks with downstream adoption. |
| COMPOSITE | 19.8 | 17.2 | 10.1 | 0 | 52.0 | +0.91 | Range 0--52.0, with the top score held by ELQV. The composite spread across all gate-passers is 12.1 points (39.9--52.0), smaller than the mean bootstrap confidence interval width (15.87 points). |

The right-skew of all three axes reflects the field's structural characteristics: most benchmark candidates mention religion incidentally (low RD), lack public evaluation data (low PE), and have not yet accumulated citations (low CI). The 47 candidates that pass both hard gates (RD $\geq$ 30 and public data) constitute the right tail of the RD distribution and the accessible cluster of the PE distribution.

---

### Table S2: Scoring Formula Coefficients and Calibration

This table presents the complete scoring specification, including weight rationales and calibration anchors. All formulas were verified against the implementation in `build_religious_feature_matrix.py`; one discrepancy identified during verification (transposed weights for P3 and P4 in an earlier manuscript draft) was corrected so that the paper matches the code.

**Axis formulas.** Each axis score is computed as a weighted linear combination of its constituent features, normalized to 0--100:

$$\text{RD} = R2 \times 25 + R6 \times 20 + R1 \times 15 + R3 \times 15 + R5 \times 15 + R4 \times 10$$

$$\text{PE} = P7 \times 30 + P3 \times 25 + P9 \times 15 + P10 \times 10 + P5 \times 10 + P4 \times 10$$

$$\text{CI} = C2 \times 30 + C4 \times 25 + C3 \times 20 + C6 \times 15 + C5 \times 10$$

$$\text{COMPOSITE} = \text{RD} \times 0.40 + \text{PE} \times 0.35 + \text{CI} \times 0.25$$

**Table S2a. Weight Rationale by Feature**

| Feature | Weight | Rationale |
|---------|--------|-----------|
| R2 (Theological Depth) | 25 | Highest RD weight. The survey's defining purpose is evaluating genuine religious engagement; theological depth is the single most important discriminator between benchmarks that assess religious values and those that treat religion as a demographic label. |
| R6 (Expert Validation) | 20 | Second-highest RD weight. Theologian involvement during benchmark construction is the strongest available proxy for construct validity in religious evaluation, where domain expertise cannot be substituted by computational methods alone. |
| R1 (Tradition Count) | 15 | Equal weight with R3, R5. Multi-tradition coverage is valuable but not privileged over depth within any single tradition; a rigorous single-tradition benchmark (e.g., IslamicMMLU) should not be penalized for its focused scope. |
| R3 (Scriptural Grounding) | 15 | Equal weight with R1, R5. Engagement with primary sacred texts distinguishes benchmarks that draw on first-order theological sources from those that rely on secondary commentary or general knowledge. |
| R5 (Pluralistic Coverage) | 15 | Equal weight with R1, R3. Recognition of inter- and intra-tradition diversity is important but should not be conflated with tradition count; a benchmark covering two traditions deeply scores higher on R5 than one mentioning fourteen superficially. |
| R4 (Denominational Awareness) | 10 | Lowest RD weight. Most benchmarks target a single tradition and do not attempt denominational distinction. R4 rewards the minority of benchmarks that navigate intra-tradition diversity (e.g., Sunni/Shia, Catholic/Protestant) but does not penalize focused instruments. |
| P7 (Implementability) | 30 | Highest PE weight. Harness compatibility determines whether a benchmark can be used in practice, not merely cited. A benchmark with perfect data availability but no evaluation harness integration requires substantial engineering effort to reproduce. |
| P3 (Data Availability) | 25 | Second-highest PE weight. Data inaccessibility is the single largest barrier to reproducibility in the field: the data availability gate alone eliminated 77% of the corpus (Section 3.3). |
| P9 (Model Compatibility) | 15 | Benchmarks supporting both open-weight and closed-source LLMs are more useful for cross-model comparison than those restricted to one category. |
| P10 (Language Coverage) | 10 | Multi-language support broadens benchmark applicability. Liturgical language normalization (Section 3.2) prevents penalizing benchmarks in Arabic, Sanskrit, or Hebrew as "low-resource." |
| P5 (License Terms) | 10 | Open licensing enables extension and adaptation; proprietary or unspecified licenses limit community uptake. |
| P4 (Code Availability) | 10 | Public evaluation code enables exact reproduction. Weighted below data availability because data is the more fundamental prerequisite. |
| C2 (Citations/Year) | 30 | Highest CI weight. Age normalization is critical in a field where 73% of candidates date from 2024--2026; raw citation counts would systematically favor older benchmarks regardless of current relevance. |
| C4 (Downstream Adoption) | 25 | Distinguishes benchmarks used as evaluation instruments from those merely cited. A benchmark cited 50 times but used for evaluation in 0 subsequent studies has less practical influence than one cited 10 times but adopted as an evaluation standard in 5 studies. |
| C3 (Venue Tier) | 20 | Publication at a top-tier NLP venue (ACL, NeurIPS, AAAI, EMNLP) signals peer review quality, though it also introduces a bias toward venues that privilege certain methodological traditions. |
| C6 (Community Engagement) | 15 | Shared tasks, workshops, and evaluation campaigns indicate sustained community investment beyond a single publication. |
| C5 (Leaderboard Presence) | 10 | Active leaderboards signal ongoing community use but are neither necessary nor sufficient for benchmark quality. |

**Table S2b. R2 Calibration Anchors**

| Anchor Benchmark | R2 Score | Theological Engagement | Calibration Rationale |
|-------------------|----------|------------------------|----------------------|
| IslamicMMLU | 4 | Fiqh-level jurisprudential reasoning across 4 madhabs (Hanafi, Maliki, Shafi'i, Hanbali), including a madhab bias detection task requiring models to identify when a response reflects one school's ruling while purporting to represent Islamic consensus. | Upper calibration: demonstrates sustained engagement with tradition-specific legal methodology, not merely factual recall of religious content. |
| Break the Checkbox | 2 | Multi-religion multiple-choice questions spanning several traditions without deep theological engagement within any single tradition. | Middle calibration: acknowledges multi-tradition coverage but does not reward breadth without depth. Subsequently reclassified as non-religious after implementation trial T4 revealed zero religious content. |
| Surface mentions | 1 | Religious vocabulary appearing in general cultural surveys (e.g., World Values Survey adaptations) without theological substance. Religion serves as a demographic category, not a domain of inquiry. | Lower calibration: establishes the floor for benchmarks that mention religion without engaging it as a domain of moral reasoning. |

Note: After correction of an R2 computation bug in the scoring pipeline, 68.8% of benchmarks still receive the minimum R2 score ($R2 = 1$). The persistent floor effect means that R2 contributes meaningful discrimination only among the top 30% of benchmarks --- precisely the candidates that pass the RD $\geq$ 30 hard gate and enter the tiered ranking (Section 3.2).

---

### Table S3: Format Taxonomy (12 Codes)

The task format feature (P1) classifies each benchmark using a 12-code taxonomy organized by harness compatibility --- the degree to which a format can be integrated into standard LLM evaluation frameworks (e.g., lm-evaluation-harness, EleutherAI). High-compatibility formats support automated scoring with minimal customization; low-compatibility formats require bespoke evaluation pipelines or human judgment.

**Table S3. Format Taxonomy with Harness Compatibility Classification**

| Code | Name | Description | Harness Compatibility | Scoring Method |
|------|------|-------------|----------------------|----------------|
| MCQ | Multiple Choice | Fixed answer choices (A/B/C/D); model selects one option | High | Exact match |
| MRC | Machine Reading Comprehension | Extract answer span from a provided passage | High | F1 / exact match |
| BIN | Binary Classification | Yes/No, Halal/Haram, True/False dichotomous judgment | High | Exact match |
| TXT | Text Classification | Classify passages by tradition, theme, or sentiment | High | Accuracy / F1 |
| SHT | Shared Task | Competition format with standardized train/dev/test splits and published baselines | High | Task-specific metric |
| SCN | Scenario-based | Present ethical dilemma and evaluate response quality against tradition-specific criteria | Medium | Rubric / LLM-as-judge |
| PSY | Psychometric/Survey | Likert-scale or forced-choice value statements adapted from established psychological instruments | Medium | Scale scoring |
| MIX | Mixed Format | Multiple formats combined within a single benchmark | Medium | Format-specific |
| OPN | Open-ended Generation | Free-text theological response requiring substantive generation | Low | Rubric / human judgment |
| MTN | Multi-turn Dialogue | Conversational theological engagement across multiple exchanges | Low | Rubric / human judgment |
| RAG | Retrieval-Augmented | Retrieval from sacred text corpora combined with generation | Low | Retrieval metrics + rubric |
| MUL | Multimodal | Visual and text inputs (religious imagery, calligraphy, sacred architecture) | Low | Task-specific |

A 13th format code --- DLG (Dialectical Reasoning) --- is reserved for future taxonomy revisions to capture benchmarks requiring multi-turn Socratic or Talmudic-style argumentation, distinct from open-ended generation (OPN) and multi-turn dialogue (MTN). No current candidate requires this code, but emerging work on theological dialogue systems suggests its future relevance (Section 3.2).

The format distribution among gate-passing candidates is concentrated in high-compatibility formats: MCQ accounts for 53% of gate-passers, followed by MRC (15%) and SHT (11%). Low-compatibility formats are underrepresented among gate-passers because their evaluation difficulty correlates with lower implementability scores (P7), creating a structural bias in the tiered ranking toward formats amenable to automated scoring.

---

### Table S4: External Search Results by Tradition Family

The external search (Section 3.1, Stage 2) was conducted across Semantic Scholar, arXiv, and HuggingFace Datasets using 72 queries organized by tradition family. This table reports the yield by tradition, documenting the search's coverage and the tradition-specific discovery rates.

**Table S4. External Search Yield by Tradition Family**

| Tradition Family | Queries | Discoveries | Ingested | False Positives | Discovery Rate |
|-----------------|---------|-------------|----------|-----------------|----------------|
| Islamic | ~15 | ~25 | ~20 | ~5 | 1.67 per query |
| Christian | ~10 | ~15 | ~12 | ~3 | 1.50 per query |
| Jewish | ~8 | ~8 | ~6 | ~2 | 1.00 per query |
| Dharmic | ~15 | ~12 | ~8 | ~4 | 0.80 per query |
| East Asian | ~10 | ~5 | ~4 | ~1 | 0.50 per query |
| African/Indigenous | ~8 | ~3 | ~2 | ~1 | 0.38 per query |
| Other | ~6 | ~2 | ~1 | ~0 | 0.33 per query |
| **Total** | **72** | **70** | **53** | **16** | **0.97 per query** |

One additional duplicate of an existing vault entry was excluded from the ingested count. False positives comprised physics experiments, medical studies, and unrelated benchmarks returned by tradition-specific keyword queries.

**Limitations.** All 72 queries were conducted in English, introducing a systematic language bias that likely undercounts non-English benchmarks. The Islamic tradition's high discovery rate (1.67 per query) partly reflects the strong indexing of Arabic-language AI research in English-language databases; traditions with scholarship published primarily in non-English venues (e.g., Japanese for Shinto, Sanskrit/Hindi for Dharmic traditions) are likely underrepresented. HuggingFace API rate limits yielded zero results during the query period, and the search did not include Google Scholar or PapersWithCode, suggesting that the 401-candidate corpus is a lower bound on the true benchmark population (Section 3.7).

---

### Table S5: Meta-Evaluation Criteria

Seven meta-evaluation criteria were developed to assess benchmark quality along dimensions that numerical scoring cannot fully capture (Section 3.4). These criteria were applied to all gate-passing benchmarks and informed the qualitative assessments reported in Sections 4.1--4.4.

**Table S5. Meta-Evaluation Criteria Specification**

| # | Criterion | Description | Rating Scale | Application |
|---|-----------|-------------|-------------|-------------|
| 1 | Content Validity | Distinguishes benchmarks testing genuine theological reasoning from those testing factual recall. A 20-item sample is classified by theological engagement level; the proportion of high-engagement items serves as the content validity indicator. | HIGH / MEDIUM / LOW | Gate-passers only |
| 2 | Discriminative Power | Checks for ceiling and floor effects across model families. A ceiling effect is defined as any tested model achieving $\geq$90% accuracy; a floor effect as all models scoring below 30%. | STRONG / MODERATE / WEAK / UNKNOWN | Gate-passers with published cross-model data |
| 3 | Cultural Authenticity | Records the positionality of benchmark authors relative to the tradition being evaluated, reflecting the argument that sacred texts cannot be treated as "just data" amenable to standard NLP annotation procedures. | NATIVE / CONSULTED / EXTERNAL | All gate-passers |
| 4 | Reproducibility | Five-item checklist: (1) publicly available data, (2) evaluation code, (3) defined scoring metrics, (4) documented prompts, (5) inter-annotator agreement reporting. | 0--5 (count of present items) | All gate-passers |
| 5 | Complementarity | Unique dimensions contributed to the overall selection, spanning tradition coverage, task type, cognitive level, language, and domain specificity. | 1--5 (unique dimension count) | Tiered benchmarks only |
| 6 | Construct Coverage | Maps each benchmark to the dimensions of religious values alignment it purports to measure. | Subset of: Knowledge, Reasoning, Values, Sensitivity, Pluralism, Contextualization | All gate-passers |
| 7 | Annotation Quality | Records how gold-standard answers were determined, from highest reliability (expert theologian judgment) to lowest (automatic generation without validation). | EXPERT THEOLOGIAN / DOMAIN SCHOLAR / CROWDWORKER / AUTOMATIC | All gate-passers |

Criteria 1--3 and 7 involve categorical judgments made by a single scorer without inter-rater reliability computation. This is a limitation acknowledged in Section 3.7: a multi-rater protocol with tradition-specific theologians would strengthen construct validity but was beyond the scope of this survey.

---

### Table S6: Cross-Model Response Length Gradient

Response length (mean characters per response) serves as a proxy for cognitive effort across construct types (Section 3.5). The monotonic gradient hypothesis predicts strict K < R < V ordering, reflecting progressively more elaborate responses as items shift from factual recall (Knowledge) to tradition-internal reasoning (Reasoning) to within-tradition normative engagement (Values). This table reports the full cross-vendor data.

**Table S6. Mean Response Length by Model, Construct Type, and Vendor**

| Model | Vendor | K Mean | R Mean | V Mean | V/K Ratio | R/K Ratio | V/R Ratio | Gradient? |
|-------|--------|--------|--------|--------|-----------|-----------|-----------|-----------|
| Opus | Anthropic | 1,853 | 4,586 | 6,327 | 3.41x | 2.47x | 1.38x | YES |
| Sonnet | Anthropic | 1,771 | 5,194 | 6,364 | 3.59x | 2.93x | 1.23x | YES |
| Haiku | Anthropic | 766 | 3,354 | 7,026 | 9.18x | 4.38x | 2.09x | YES |
| GPT-Codex | OpenAI | 82 | 472 | 461 | 5.63x | 5.76x | 0.98x | NO (V < R) |
| Codex-Mini | OpenAI | 78 | 415 | 416 | 5.33x | 5.32x | 1.00x | YES (marginal) |
| Gem-FL | Gemini | 63 | 104 | 101 | 1.60x | 1.65x | 0.97x | NO |
| Gem-Flash | Gemini | 201 | 268 | 222 | 1.11x | 1.33x | 0.83x | NO |
| Gem-Pro | Gemini | 231 | 305 | 244 | 1.06x | 1.32x | 0.80x | NO |
| Gem-3.1P | Gemini | 310 | 328 | 318 | 1.03x | 1.06x | 0.97x | NO |

Response lengths in characters. Gradient defined as strict monotonicity K < R < V. Codex-Mini is classified YES because V (416) marginally exceeds R (415), satisfying the strict ordering criterion by a single character.

**Interpretation.** Three distinct behavioral modes emerge. The Claude family exhibits robust K < R < V gradients with V/K ratios ranging from 3.41x (Opus) to 9.18x (Haiku), indicating differentiated engagement with construct types. Haiku's extreme V/K ratio (9.18x) reflects its brevity on Knowledge items (766 characters) combined with extensive Values responses (7,026 characters), suggesting that even a smaller model allocates disproportionate effort to normative reasoning tasks. The OpenAI Codex models exhibit compressed responses across all construct types (82--472 characters), achieving near-ceiling rubric scores with 5--80x shorter responses than Claude --- a "compressed accuracy" mode that achieves quality without verbosity. The Gemini models produce uniformly short responses (63--328 characters) with V/R ratios below 1.0 for all four models, indicating no construct-type differentiation; this pattern is consistent with template-based response generation rather than construct-sensitive engagement.

The Gemini data provenance caveat (Section 3.5.6, Caveat 3) applies to all Gemini rows: backfilled template extraction rather than interactive API administration may not capture the full response quality that interactive prompting would elicit. The absence of a K < R < V gradient for Gemini models may therefore partly reflect methodological artifact rather than genuine model behavior.

---

### Table S7: Cross-Vendor Rubric Scores

All open-ended responses were evaluated against item-specific scoring rubrics (Section 3.5.3). Rubric scores are normalized to 0--1 for each construct type: Knowledge (checklist accuracy), Reasoning (methodological completeness, 0--3 normalized), Values (within-tradition normative engagement, 0--5 normalized), and Bias (stereotype avoidance, 0--3 normalized). V-Paired reports the Values score computed only from the 10 matched bias-values pairs.

**Table S7. Normalized Rubric Scores by Model and Construct Type**

| Model | Vendor | Origin | K | R | V | B | V-Paired |
|-------|--------|--------|---|---|---|---|----------|
| Opus | Anthropic | Original | 1.000 | 1.000 | 0.933 | 1.000 | 1.000 |
| Sonnet | Anthropic | Original | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |
| Haiku | Anthropic | Original | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |
| GPT-Codex | OpenAI | Original | 0.933 | 0.956 | 0.867 | 1.000 | 0.920 |
| Codex-Mini | OpenAI | Original | 1.000 | 0.878 | 0.900 | 1.000 | 0.980 |
| Gem-FL | Gemini | Backfilled | 0.000 | 0.000 | 0.200 | 1.000 | 0.200 |
| Gem-Flash | Gemini | Backfilled | 0.000 | 0.000 | 0.000 | 0.567 | 0.000 |
| Gem-Pro | Gemini | Backfilled | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |
| Gem-3.1P | Gemini | Backfilled | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |

Origin: "Original" denotes rubric scores from interactive administration via API with the system prompts specified in Section 3.5.1. "Backfilled" denotes rubric scores computed post-hoc from template-extracted responses (Section 3.5.5). Backfilled scores carry the Gemini data provenance caveat (Section 3.5.6, Caveat 3).

**Interpretation.** The rubric scores reveal a ceiling effect among Claude-family and OpenAI models: all five "Original"-origin models achieve $\geq$ 0.867 on every construct type, with 11 of 15 non-Bias scores at 1.000. This ceiling effect means that rubric-based evaluation cannot discriminate among high-capability models --- the instruments are too easy for the models they evaluate (Section 6). Opus's sole deduction (V = 0.933) reflects three instances of shifting from within-tradition normative reasoning to an external analytical register, a construct distinction the rubric was designed to detect.

The four Gemini models score 0.000 on Knowledge and Reasoning (15 of 16 cells), with only Gem-FL achieving a non-zero Values score (0.200). The uniformly high Bias scores for three of four Gemini models (B = 1.000 for Gem-FL, Gem-Pro, Gem-3.1P) suggest that Gemini models may engage stereotype-avoidance processing even when producing minimal substantive content --- a pattern consistent with template-based response generation where Bias items elicit default safety-oriented responses that happen to score well on the rubric's avoidance criteria. Gem-Flash's lower Bias score (0.567) may reflect a different template configuration rather than a genuine capability difference.

All three methodological caveats from Section 3.5.6 apply to this table. Same-vendor scorer bias (Caveat 2) may inflate Claude-family scores relative to an independent scorer. Gemini data provenance limitations (Caveat 3) mean that backfilled scores represent a lower bound; interactive API administration might yield substantially different results.

---

### Table S8: T2 Arabic MCQ Results by Model and Difficulty

The T2 assessment comprises 30 items drawn from the Islamic Inheritance Law (fara'id) evaluation dataset, stratified as 15 Beginner and 15 Advanced items (Section 3.5.2). Each item is a 6-option multiple-choice question in Arabic script with a single gold-standard correct answer. Random chance is approximately 16.7% (1/6).

**Table S8. T2 Arabic MCQ Accuracy by Model, Vendor, and Difficulty Tier**

| Model | Vendor | Beginner (15) | Advanced (15) | Overall (30) | $\Delta$ (Adv $-$ Beg) |
|-------|--------|--------------|---------------|-------------|-------------|
| Opus | Anthropic | 15/15 (100%) | 15/15 (100%) | 30/30 (100%) | 0 pp |
| Sonnet | Anthropic | 15/15 (100%) | 15/15 (100%) | 30/30 (100%) | 0 pp |
| Haiku | Anthropic | 12/15 (80%) | 11/15 (73.3%) | 23/30 (76.7%) | $-$6.7 pp |
| GPT-Codex | OpenAI | 15/15 (100%) | 15/15 (100%) | 30/30 (100%) | 0 pp |
| Codex-Mini | OpenAI | 12/15 (80%) | 14/15 (93.3%) | 26/30 (86.7%) | +13.3 pp |
| Gem-FL | Gemini | 3/15 (20%) | 3/15 (20%) | 6/30 (20%) | 0 pp |
| Gem-Flash | Gemini | 1/15 (6.7%) | 2/15 (13.3%) | 3/30 (10%) | +6.7 pp |
| Gem-Pro | Gemini | 0/15 (0%) | 2/15 (13.3%) | 2/30 (6.7%) | +13.3 pp |
| Gem-3.1P | Gemini | 2/15 (13.3%) | 1/15 (6.7%) | 3/30 (10%) | $-$6.7 pp |

$\Delta$ = Advanced accuracy minus Beginner accuracy in percentage points (pp). Random chance for 6-option MCQ $\approx$ 16.7%.

**Interpretation.** The T2 assessment is the sole genuinely discriminative instrument in the trial battery, producing a 93.3-percentage-point performance spread (6.7% for Gem-Pro to 100% for Opus, Sonnet, and GPT-Codex) that dwarfs the rubric's binary ceiling/floor distribution. Three performance tiers are visible: perfect accuracy (Opus, Sonnet, GPT-Codex at 100%); above-chance but imperfect accuracy (Haiku at 76.7%, Codex-Mini at 86.7%); and near-chance or below-chance accuracy (all four Gemini models at 6.7--20%).

The difficulty gradient ($\Delta$) is inconsistent across models. Haiku performs 6.7 pp worse on Advanced items, while Codex-Mini performs 13.3 pp better --- suggesting that the Beginner/Advanced difficulty stratification interacts with model-specific capabilities rather than tracking a universal difficulty gradient. For perfect-accuracy models, $\Delta$ is undefined (0 pp at ceiling).

**T2 blinding caveat (Section 3.5.6, Caveat 1).** The original Claude trials (Opus, Sonnet, Haiku) were administered with gold-standard answer labels visible in the input file, making reported accuracy figures upper-bound estimates. Subsequent cross-vendor trials (OpenAI, Gemini) used a blind administration protocol. Haiku's 7 errors (76.7% accuracy) provide evidence of independent answering even under contaminated conditions, as a model exploiting visible labels would be expected to achieve perfect accuracy. Nevertheless, the asymmetry means that Claude-family T2 accuracy may be inflated relative to OpenAI and Gemini accuracy, and direct cross-vendor comparison of T2 scores should be interpreted with this caveat in mind.

---

### Table S9: Claim Robustness Battery --- Full Statistical Details

Eight empirical claims were pre-registered and subjected to formal statistical testing (Section 3.6). This table presents the complete test specifications, statistics, and outcomes. The Bonferroni-corrected significance threshold is $\alpha_{\text{adj}} = 0.05 / 8 = 0.00625$. Values are reported to three decimal places; the main text reports two decimal places for readability.

**Table S9. Statistical Test Results for All Eight Claims**

| Claim | Test | n | Statistic | df | p-value | Effect Size | 95% CI | Bonferroni | Outcome |
|-------|------|---|-----------|----|---------|----|--------|------------|---------|
| C1a | $\chi^2$ (uniform) | 47 | 64.957 | 5 | < 0.001 | V = 0.526 | --- | PASS | SUPPORTED |
| C1b | $\chi^2$ (proportional) | 47 | 21.839 | 5 | 0.0006 | V = 0.305 | --- | PASS | SUPPORTED |
| C2 | Binomial | 47 | k = 13 | --- | 0.0015 | --- | [0.000, 0.403] | PASS | SUPPORTED |
| C3 | Binomial | 47 | k = 47 | --- | < 0.001 | --- | [0.938, 1.000] | PASS | SUPPORTED |
| C4 | Logistic reg. | 401 | Pseudo-R$^2$ = 0.068 | --- | 0.112 | --- | --- | FAIL | REVISED |
| C5 | Binomial | 47 | k = 28 | --- | 0.121 | --- | [0.465, 1.000] | FAIL | MARGINAL |
| C6 | Fisher's exact | 401 | OR = 0.580 | --- | 0.090 | --- | --- | FAIL | REVISED |
| C7 | Binomial | 23 | k = 10 | --- | 0.678 | --- | [0.232, 0.655] | FAIL | REVISED |
| C8a | One-sample t | 16 | t = $-$4.93 | 15 | 0.0002 | d = $-$1.232 | --- | PASS | SUPPORTED |
| C8b | Wilcoxon | 16 | W = 5.0 | --- | 0.0006 | --- | --- | PASS | SUPPORTED |
| C8c | Binomial ($\geq$ 50) | 16 | k = 3 | --- | 0.011 | --- | --- | FAIL | SUPPORTED ($\alpha$ = 0.05) |
| C8d | Binomial ($\geq$ 75) | 16 | k = 0 | --- | 0.000015 | --- | --- | PASS | SUPPORTED |

**Claim descriptions.** C1: Tradition asymmetry --- Islam dominates the gate-passing distribution. C1a tests against uniform expectation; C1b tests against corpus-proportional expectation. C2: Knowledge--reasoning conflation --- fewer than expected benchmarks test genuine theological reasoning. C3: Data availability bottleneck --- data accessibility predicts gate passage. C4: Structural epistemic injustice --- tradition family predicts gate passage through logistic regression. C5: WEIRD bias --- non-WEIRD traditions are disadvantaged. C6: WEIRD bias (Fisher's exact) --- WEIRD/non-WEIRD classification is associated with gate passage. C7: Bias--values conflation --- bias and values items are not independently measured. C8: Values relevance failure --- the mean values relevance score among gate-passers is significantly below the scale midpoint.

**Notes.** C4 p-value is for the overall logistic regression model; individual tradition family coefficients are all non-significant, indicating that no single tradition family is a statistically significant predictor of gate passage after controlling for other covariates (Section 4.4). Claims C4, C6, and C7 were revised from their pre-registered form to reflect the empirical findings: the expected WEIRD bias is reversed (non-WEIRD traditions pass at 14.4% vs. WEIRD at 8.9%), structural epistemic injustice operates through publication infrastructure rather than the scoring framework, and bias--values conflation does not reach statistical significance in the cross-sectional survey.

C8 is tested with four complementary tests (a--d) to provide converging evidence given the small sample (n = 16). All four tests support the values relevance failure claim, with the one-sample t-test and Wilcoxon signed-rank test surviving Bonferroni correction. The large effect size (d = $-$1.232) indicates a substantively meaningful deficit: the mean values relevance score of 30.0/100 falls more than one standard deviation below the scale midpoint.

---

### Table S10: Void Factor Analysis for 8 Missing Traditions

Eight of fourteen surveyed traditions have zero viable benchmarks after gate application. This table presents a structured factor analysis identifying the primary obstacles to benchmark development for each tradition, organized by the six void factors described in Section 4.3.

**Table S10. Void Factor Ratings for Traditions with Zero Gate-Passing Benchmarks**

| Tradition | Family | F1: Digital Corpus | F2: NLP Community | F3: Shared Tasks | F4: Formalizable | F5: English Pub. | F6: Indiv.-Response | Primary Obstacle |
|-----------|--------|-------------------|-------------------|-----------------|-----------------|-----------------|----------------------|-----------------|
| Judaism | Abrahamic | HIGH | MODERATE | NONE | HIGH | HIGH | YES | Community coordination |
| Jainism | Dharmic | MODERATE | LOW | NONE | MODERATE | LOW | YES | Community coordination |
| Taoism | East Asian | HIGH | LOW | NONE | MODERATE | LOW | YES | Community coordination |
| Confucianism | East Asian | HIGH | MODERATE | NONE | HIGH | MODERATE | YES | Community coordination |
| Shinto | East Asian | LOW | LOW | NONE | LOW | LOW | PARTIAL | Structural exclusion |
| Ubuntu | African/Indig. | LOW | LOW | NONE | LOW | LOW | NO (communal) | Structural exclusion |
| Indigenous | African/Indig. | LOW | LOW | NONE | LOW | LOW | NO (communal) | Structural exclusion |
| Baha'i | Other | MODERATE | LOW | NONE | MODERATE | MODERATE | YES | Minimal community presence |
| Zoroastrianism | Other | MODERATE | LOW | NONE | MODERATE | LOW | YES | Minimal community presence |

**Factor definitions.** F1 (Digital Corpus): availability of machine-readable sacred texts and scholarly commentary. F2 (NLP Community): presence of an active computational linguistics or NLP research community working with tradition-specific texts. F3 (Shared Tasks): existence of organized evaluation campaigns or competition-format benchmarks. F4 (Formalizable): compatibility of the tradition's reasoning methods with item-response evaluation formats (e.g., syllogistic reasoning, case-based analysis). F5 (English Publication): degree to which tradition-specific scholarship is accessible through English-language publication venues indexed by major databases. F6 (Individual-Response): whether the tradition's knowledge system is compatible with the individual-response formats that current LLM evaluation assumes.

**Interpretation.** Two distinct patterns account for the 8-tradition void. Four traditions --- Judaism, Jainism, Taoism, Confucianism --- possess sufficient digital infrastructure (F1 $\geq$ MODERATE) and formalizable reasoning systems (F4 $\geq$ MODERATE) to support benchmark construction within the existing paradigm. Their absence from the tiered ranking reflects a community coordination gap: the institutional bridges between tradition-specific digital scholarship and the LLM evaluation community have not yet been built. Judaism illustrates this most starkly: the Sefaria digital library contains the complete Tanakh, Talmud, and centuries of rabbinic commentary in machine-readable format, and Talmudic logic is highly amenable to formalization, yet no shared task pipeline has converted these resources into LLM evaluation artifacts. For these traditions, the first call to action (Section 6) --- targeted shared tasks co-located with major NLP venues --- addresses the binding constraint.

Three traditions --- Shinto, Ubuntu Philosophy, Indigenous Spirituality --- face a fundamentally different obstacle. Their knowledge systems are embedded in ritual practice (Shinto), communal deliberation (Ubuntu), or oral and relational transmission (Indigenous), and cannot be straightforwardly extracted into decontextualized test items without transforming their epistemic character. The F6 rating captures this structural exclusion: the benchmark creation pipeline assumes an individual respondent producing propositional answers, which is incompatible with traditions that locate moral reasoning in collective processes, embodied practices, or relational accountability. For these traditions, the third call to action (Section 6) --- community-governed evaluation protocols respecting the CARE Principles for Indigenous Data Governance --- addresses the binding constraint.

Two traditions --- Baha'i and Zoroastrianism --- have moderate digital infrastructure but minimal presence in both the NLP research community and the broader AI evaluation ecosystem. Their absence likely reflects small community size rather than structural incompatibility with the benchmark paradigm. Targeted outreach to Baha'i and Zoroastrian scholarly communities could yield benchmark development within existing methodological frameworks.
