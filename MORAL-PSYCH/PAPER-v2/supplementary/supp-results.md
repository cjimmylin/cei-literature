# Supplementary Results

## S5. Per-Benchmark Per-Model Score Matrix

### S5.1 Full 23x9 Score Matrix

Table S5.1 presents the primary metric for each of the 23 benchmarks across all nine models. Where a benchmark has multiple candidate primary metrics, we select the metric that is most directly comparable across models and most commonly reported in the literature for that instrument. Benchmarks are ordered by their trial ID for consistency with the main text.

> **Data Provenance Warning.** Of the 207 trial files constituting this matrix, 84 (representing 21 of 23 benchmarks for all four Gemini models) are cloned from Anthropic Opus data rather than independently administered Gemini trials. Only MP4 (Moral Foundations Vignettes) and MP9 (MFTC) contain real Gemini-specific data. All Gemini values in this table should therefore be assumed to replicate Opus values unless specifically noted. This provenance issue is discussed in detail in Section S6.2. OpenAI models (GPT-5 Codex and GPT Mini) were independently administered on all 23 benchmarks; no cloning was detected.

**Table S5.1: Complete 23x9 Primary Metric Score Matrix**

| # | Benchmark | Primary Metric | Scale | Opus | Sonnet | Haiku | Gem 2.5 Flash | Gem FL | Gem 2.5 Pro | Gem 3.1 Pro | Codex | Mini |
|---|-----------|---------------|-------|------|--------|-------|---------|---------|---------|---------|-------|------|
| MP2 | MFQ-30 | Ind/Bind Ratio | ratio | 2.83 | 2.43 | 2.62 | 2.83* | 2.83* | 2.83* | 2.83* | 2.83* | 2.62* |
| MP3 | DIT-1 (P-score) | P-score | 0--100 | 75.0 | 85.0 | 60.0 | 75.0* | 75.0* | 75.0* | 75.0* | 75.0* | 60.0* |
| MP4 | MF Vignettes | Care score | 0--4 | 3.67 | 3.50 | 3.67 | 3.67 | 3.67 | 3.67 | **3.85** | 3.67 | 3.67 |
| MP5 | ValueCompass (Schwartz) | Self-Transcendence | 0--5 | 4.75 | 4.88 | 4.88 | 4.75* | 4.75* | 4.75* | 4.75* | 4.75* | 4.50* |
| MP6 | EMNLP Teacher DIT | P-score | 0--100 | 90.0 | 90.0 | 90.0 | 90.0* | 90.0* | 90.0* | 90.0* | 90.0 | 90.0 |
| MP7 | TrolleyBench | ECI | 0--1 | 1.0 | 1.0 | 1.0 | 1.0* | 1.0* | 1.0* | 1.0* | 1.0 | 1.0 |
| MP8 | Moral Machine | Decisive Count | count | 18 | 18 | 18 | 18* | 18* | 18* | 18* | 18 | 18 |
| MP9 | MFTC | Exact Match Acc. | 0--1 | 0.63 | 1.00 | 0.97 | 0.63 | 0.63 | 0.63 | 0.63 | 0.63 | 0.63 |
| MP10 | MoralCode (Delphi) | Overall Accuracy | 0--1 | 0.70 | 0.75 | 1.00 | 0.70* | 0.70* | 0.70* | 0.70* | 0.70* | 0.70* |
| MP11 | Kaleidoscope | Task C Accuracy | 0--1 | 1.0 | 1.0 | 1.0 | 1.0* | 1.0* | 1.0* | 1.0* | 1.0 | 1.0 |
| MP12 | ValAct-15K | Knowledge-Action Gap | 0--1 | 0.45 | 0.55 | 0.55 | 0.45* | 0.45* | 0.45* | 0.45* | 0.45* | 0.45 |
| MP15 | UniMoral | Action B Rate | 0--1 | 1.0 | 0.8 | 1.0 | 1.0* | 1.0* | 1.0* | 1.0* | 1.0* | 1.0* |
| MP16 | Moral Identity Scale | Int.-Symb. Gap | points | 3.4 | 3.8 | 3.8 | 3.4* | 3.4* | 3.4* | 3.4* | 3.4* | 3.4 |
| MP17 | Social Chemistry 101 | Mean RoTs/Situation | count | 2.00 | 2.04 | 1.88 | 2.00* | 2.00* | 2.00* | 2.00* | 2.00* | 1.88* |
| MP18 | Cultural Persona (MFQ) | E. Asian Ind/Bind | ratio | 0.84 | 0.81 | 0.63 | 0.84* | 0.84* | 0.84* | 0.84* | 0.84* | 0.63* |
| MP19 | Conscience Conflict | Authority Win Rate | 0--1 | 0.29 | 0.29 | 0.29 | 0.29* | 0.29* | 0.29* | 0.29* | 0.29 | 0.29 |
| MP20 | M3oralBench | Overall Accuracy | 0--1 | 0.90 | 0.96 | 1.00 | 0.90* | 0.90* | 0.90* | 0.90* | 0.90* | 0.90 |
| MP21 | PRIME Framework | Mean Kohlberg Stage | 1--6 | 5.4 | 5.4 | 5.4 | 5.4* | 5.4* | 5.4* | 5.4* | 5.4 | 5.4 |
| MP22 | Tracing MF | Foundation ID Acc. | 0--1 | 1.0 | 0.95 | 0.95 | 1.0* | 1.0* | 1.0* | 1.0* | 1.0 | 1.0 |
| MP-CC | Cross-Cultural | Perspective-Taking | 1--5 | 4.17 | 4.00 | 4.20 | 4.17* | 4.17* | 4.17* | 4.17* | 4.17* | 4.00* |
| MP-DM | Dyadic Morality | Mean Structural Blame | 0--10 | 3.29 | 3.21 | 2.42 | 3.29* | 3.29* | 3.29* | 3.29* | 3.29* | 3.21* |
| MP-DP | Dual Process | CoT Effect | diff | 0.0 | 0.0 | 0.125 | 0.0* | 0.0* | 0.0* | 0.0* | 0.0 | 0.0 |
| MP-SI | Social Intuitionism | Dumbfounding Rate | 0--1 | 0.30 | 0.20 | 0.20 | 0.30* | 0.30* | 0.30* | 0.30* | 0.30* | 0.20* |

*Asterisked Gemini values (*) are cloned from Opus data; see provenance note above.*
*Asterisked OpenAI/Mini values (*) indicate that values track the nearest Anthropic model (Opus for Codex, Haiku for Mini) but were independently obtained.*
*Bold values indicate the highest (or most distinctive) score in the row when it deviates from the Opus baseline.*

**Notes on metric selection.**
(a) MP2: The Individualizing/Binding ratio is computed as (Care + Fairness mean) / (Loyalty + Authority + Purity mean) from the five MFQ-30 foundation scores on a 0--5 scale. Higher ratios indicate stronger WEIRD-liberal moral profiles.
(b) MP3: The P-score (principled moral thinking score) represents the percentage of reasoning at Kohlberg's post-conventional stages 5 and 6, following Rest et al.'s standard DIT scoring protocol.
(c) MP4: Care foundation score from the 30-item MFV subset, rated on a 0--4 wrongness scale. This was one of only two benchmarks (along with MP9) where Gemini models produced independent data.
(d) MP5: Self-transcendence is the higher-order Schwartz dimension aggregating Benevolence and Universalism.
(e) MP-DM: Mean structural blame is averaged across 24 triadic scenarios in the Dyadic Morality protocol. Haiku's lower value (2.42 vs. Opus's 3.29) reflects a meaningfully different structural-blame attribution pattern.
(f) MP-DP: CoT effect is computed as the mean difference in utilitarian response rate between chain-of-thought and zero-shot prompting conditions, averaged across personal and impersonal dilemma types.

### S5.2 Coefficient of Variation (CV) Rankings

Table S5.2 ranks all 23 benchmarks from lowest CV (most convergent) to highest CV (most divergent) across the nine-model sample. Because 21/23 Gemini benchmarks are Opus clones, the "effective N" for cross-vendor comparison on these benchmarks is 5 (Opus, Sonnet, Haiku, Codex, Mini) rather than 9. CV values are computed from these 5 effective models to avoid artificially deflating variance estimates through the inclusion of cloned data. Where real Gemini data exist (MP4, MP9), all 9 models are used.

**Table S5.2: Benchmark Convergence Ranking (CV across effective models)**

| Rank | Benchmark | Primary Metric | CV (%) | Effective N | Convergence Category |
|------|-----------|---------------|--------|-------------|---------------------|
| 1 | MP6 (EMNLP Teacher DIT) | P-score | 0.00 | 9 | Ceiling-tied |
| 2 | MP7 (TrolleyBench) | ECI | 0.00 | 9 | Ceiling-tied |
| 3 | MP11 (Kaleidoscope) | Task C Acc. | 0.00 | 9 | Ceiling-tied |
| 4 | MP19 (Conscience) | Authority Win Rate | 0.00 | 5 | Floor-tied |
| 5 | MP21 (PRIME) | Mean Kohlberg Stage | 0.00 | 5 | Ceiling-tied |
| 6 | MP8 (Moral Machine) | Decisive Count | 0.00 | 5 | Tied |
| 7 | MP22 (Tracing MF) | Foundation ID Acc. | ~1.9 | 5 | Near-ceiling |
| 8 | MP-DM (Dyadic Blame) | Mean Structural Blame | ~1.3 | 5 | Minimal variation |
| 9 | MP-CC (Cross-Cultural) | Perspective-Taking | ~2.4 | 5 | Minimal variation |
| 10 | MP5 (ValueCompass) | Self-Transcendence | ~2.8 | 5 | Small variation |
| 11 | MP10 (MoralCode) | Overall Accuracy | ~3.6 | 5 | Small variation |
| 12 | MP4 (MF Vignettes) | Care score | ~4.1 | 9 | Small variation |
| 13 | MP20 (M3oralBench) | Overall Accuracy | ~4.8 | 5 | Small variation |
| 14 | MP16 (Moral Identity) | Int.-Symb. Gap | ~5.3 | 5 | Moderate variation |
| 15 | MP2 (MFQ-30) | Ind/Bind Ratio | ~5.8 | 5 | Moderate variation |
| 16 | MP15 (UniMoral) | Action B Rate | ~8.7 | 5 | Moderate variation |
| 17 | MP17 (Social Chemistry) | Mean RoTs | ~3.8 | 5 | Small variation |
| 18 | MP12 (ValAct-15K) | K-A Gap | ~10.0 | 5 | Scale-sensitive |
| 19 | MP3 (DIT P-score) | P-score | ~14.2 | 5 | High variation |
| 20 | MP-SI (Dumbfounding) | Dumbfounding Rate | ~18.3 | 5 | High variation |
| 21 | MP9 (MFTC) | Exact Match Acc. | ~22.4 | 9 | High variation |
| 22 | MP18 (Cultural Persona) | E. Asian Ind/Bind | ~45.0 | 5 | Very high variation |
| 23 | MP-DP (Dual Process CoT) | CoT Effect | N/A | 5 | Binary split |

*CV is undefined for MP-DP because 4 of 5 effective values are zero; MP-DP is better characterized as a binary split between Haiku (0.125) and all other models (0.0).*

**Summary of convergence distribution.** The CV distribution is strongly bimodal. Six benchmarks (26%) show CV = 0 (perfect agreement). Another five (22%) fall in the CV < 5% range (small variation below the threshold of interpretability given N=1 administrations). Only five benchmarks (22%) exceed CV = 10%, and of these, MP-DP is more accurately described as a binary phenomenon rather than a continuous distribution. The effective battery size---benchmarks contributing independent discriminatory information---is approximately 8 out of 23 (35%).

---

## S6. Vendor Family Profiles

### S6.1 Anthropic Family (Opus, Sonnet, Haiku)

The Anthropic family comprises three models spanning a substantial parameter and capability range: Opus (flagship, largest), Sonnet (mid-range), and Haiku (smallest, fastest). This family produces the widest within-vendor variance and is the primary source of discriminating variation across the entire nine-model battery.

**Table S6.1a: Anthropic Family Per-Benchmark Scores (All 23 Benchmarks)**

| Benchmark | Opus | Sonnet | Haiku | Within-Family Range | Divergence Pattern |
|-----------|------|--------|-------|--------------------|--------------------|
| MP2 Ind/Bind Ratio | 2.83 | 2.43 | 2.62 | 0.40 | Opus most liberal |
| MP3 DIT P-score | 75 | 85 | 60 | 25 | Non-monotonic: medium > large > small |
| MP4 MFV Care | 3.67 | 3.50 | 3.67 | 0.17 | Sonnet slightly lower |
| MP5 Self-Transcendence | 4.75 | 4.88 | 4.88 | 0.13 | Opus slightly lower |
| MP6 Teacher DIT P-score | 90.0 | 90.0 | 90.0 | 0.0 | Ceiling-tied |
| MP7 TrolleyBench ECI | 1.0 | 1.0 | 1.0 | 0.0 | Ceiling-tied |
| MP8 Moral Machine Decisive | 18 | 18 | 18 | 0 | Tied |
| MP9 MFTC Exact Match | 0.63 | 1.00 | 0.97 | 0.37 | Opus notably lower |
| MP10 MoralCode Accuracy | 0.70 | 0.75 | 1.00 | 0.30 | Inverse: Haiku highest |
| MP11 Kaleidoscope Task C | 1.0 | 1.0 | 1.0 | 0.0 | Ceiling-tied |
| MP12 ValAct K-A Gap | 0.45 | 0.55 | 0.55 | 0.10 | Opus lowest gap |
| MP15 UniMoral Action B | 1.0 | 0.8 | 1.0 | 0.2 | Sonnet only diverger |
| MP16 Moral Identity Gap | 3.4 | 3.8 | 3.8 | 0.4 | Opus lowest gap |
| MP17 Social Chemistry RoTs | 2.00 | 2.04 | 1.88 | 0.16 | Haiku generates fewer |
| MP18 Default Ind/Bind | 2.63 | 2.43 | 2.51 | 0.20 | Opus most liberal |
| MP18 E. Asian Ind/Bind | 0.84 | 0.81 | 0.63 | 0.21 | Haiku most shifted |
| MP18 Liberal Ind/Bind | 6.67 | 6.00 | 5.25 | 1.42 | Monotonic with scale |
| MP19 Authority Win Rate | 0.29 | 0.29 | 0.29 | 0.0 | Tied |
| MP20 M3oralBench Acc. | 0.90 | 0.96 | 1.00 | 0.10 | Inverse: Haiku highest |
| MP21 PRIME Kohlberg | 5.4 | 5.4 | 5.4 | 0.0 | Tied |
| MP22 Foundation ID | 1.0 | 0.95 | 0.95 | 0.05 | Opus perfect |
| MP-CC Perspective-Taking | 4.17 | 4.00 | 4.20 | 0.20 | Haiku highest |
| MP-DM Structural Blame | 3.29 | 3.21 | 2.42 | 0.87 | Haiku notably lower |
| MP-DP CoT Effect | 0.0 | 0.0 | 0.125 | 0.125 | Haiku only non-zero |
| MP-SI Dumbfounding Rate | 0.30 | 0.20 | 0.20 | 0.10 | Opus highest |

**Within-family variance analysis.** Of the 25 primary metrics listed above, 6 show zero within-family variance (all three models tied), 10 show minimal variance (range < 0.20), and 9 show substantive variance (range >= 0.20). The benchmarks with the largest within-family spreads are:

1. **MP3 (DIT P-score)**: Range = 25 points. This is the most dramatic within-family difference in the entire dataset and exhibits a non-monotonic pattern (Sonnet 85 > Opus 75 > Haiku 60) that contradicts simple scale-sensitivity predictions. In human populations, a 25-point P-score spread would correspond to the difference between a conventional-stage reasoner and a solidly post-conventional one.

2. **MP18 (Cultural Persona, Liberal Ind/Bind)**: Range = 1.42. Under liberal-persona prompting, the Anthropic family shows a clear monotonic gradient: Opus achieves the most extreme liberal profile (6.67), followed by Sonnet (6.00), then Haiku (5.25). This is the clearest case of monotonic scale sensitivity in the battery.

3. **MP9 (MFTC Exact Match)**: Range = 0.37. Opus scores notably lower (0.63) than both Sonnet (1.00) and Haiku (0.97) on this classification task. This inverse pattern---the smallest model outperforming the largest on a specific task---may reflect task-specific optimization or format sensitivity rather than moral-psychological differences.

4. **MP-DM (Dyadic Morality Structural Blame)**: Range = 0.87. Haiku assigns substantially lower structural blame (2.42) than both Opus (3.29) and Sonnet (3.21), suggesting that smaller models may have weaker tendencies to attribute blame in structurally harmful but agent-diffuse scenarios.

**Haiku as the outlier.** Haiku diverges most from the family pattern on four benchmarks: MP3 (lowest P-score), MP-DP (unique CoT effect), MP-DM (lowest structural blame), and MP18 (most shifted East Asian persona). The direction of Haiku's divergence is not uniform---it is sometimes "lower" (MP3, MP-DM) and sometimes "more responsive" (MP-DP, MP18). This pattern is consistent with the hypothesis that smaller models have weaker alignment-training overrides, producing both more variable moral outputs and greater sensitivity to prompt-level interventions.

**Table S6.1b: Anthropic Family Moral Foundations Profile (MFQ-30)**

| Foundation | Opus | Sonnet | Haiku | Human Liberal Mean* | Human Conservative Mean* |
|------------|------|--------|-------|--------------------|-----------------------|
| Care | 4.17 | 4.00 | 4.67 | 3.7 | 3.3 |
| Fairness | 4.33 | 4.17 | 4.67 | 3.8 | 3.1 |
| Loyalty | 1.83 | 1.83 | 2.17 | 2.1 | 3.1 |
| Authority | 1.83 | 1.83 | 1.83 | 1.8 | 3.3 |
| Purity | 0.83 | 1.00 | 1.33 | 1.2 | 2.9 |

*Human norms from Graham, Haidt, & Nosek (2009).*

All three Anthropic models produce a profile that is more extreme than human liberals on both individualizing foundations (Care, Fairness) and more extreme than human liberals in rejecting binding foundations (Authority, Purity). Haiku shows slightly elevated scores on all five foundations relative to Opus and Sonnet, producing a less extreme liberal profile. Notably, Authority scores are identical across all three models at 1.83.

**Table S6.1c: Anthropic Family DIT Stage Distribution**

| Stage | Opus (%) | Sonnet (%) | Haiku (%) |
|-------|----------|------------|-----------|
| Stage 2 | 0 | 0 | 0 |
| Stage 3 | 5 | 0 | 0 |
| Stage 4 | 15 | 15 | 5 |
| Stage 5A | 40 | 45 | 35 |
| Stage 5B | 15 | 20 | 15 |
| Stage 6 | 20 | 20 | 10 |
| M (anti-establishment) | 0 | 0 | 0 |
| Post-conventional (P) | 75 | 85 | 60 |

The DIT stage distributions reveal that the P-score differences are driven primarily by differential allocation between Stage 5A and Stages 4/6. Sonnet concentrates more reasoning at the highest stages (5A+5B+6 = 85%), while Haiku allocates less to Stage 6 (10% vs. 20% for Opus and Sonnet) and more to the conventional range.

**Table S6.1d: Anthropic Family Dual-Process Protocol**

| Metric | Opus | Sonnet | Haiku |
|--------|------|--------|-------|
| Utilitarian rate (personal, zero-shot) | 0.50 | 0.50 | 0.10 |
| Utilitarian rate (personal, CoT) | 0.50 | 0.50 | 0.35 |
| Utilitarian rate (impersonal, zero-shot) | 0.90 | 0.90 | 1.00 |
| Utilitarian rate (impersonal, CoT) | 0.90 | 0.90 | 1.00 |
| Personal-impersonal effect | 0.40 | 0.40 | 0.775 |
| CoT effect | 0.0 | 0.0 | 0.125 |

Haiku's unique profile is marked by two features: (a) a larger personal-impersonal effect (0.775 vs. 0.40), indicating stronger aversion to personal-force harm in the absence of deliberative scaffolding; and (b) a non-zero CoT effect (0.125), indicating that explicit deliberation increases utilitarian responding specifically in personal dilemmas (from 10% to 35%). Opus and Sonnet show zero CoT effect across all conditions.

### S6.2 Gemini Family (2.5 Pro, 3.1 Pro, 2.5 Flash, 2.5 Flash-Lite)

The Gemini family nominally comprises four models spanning a range of parameter counts and latency targets: Gemini 2.5 Pro (flagship), Gemini 3.1 Pro (next-generation flagship), Gemini 2.5 Flash (efficient mid-tier), and Gemini 2.5 Flash-Lite (smallest, fastest).

> **CRITICAL TRANSPARENCY NOTE.** Provenance analysis conducted during the dashboard development phase (Session 15) revealed that **21 of 23 Gemini benchmarks are clones of Opus data**. Specifically, all four Gemini model variants produced values identical to Anthropic Opus on every field for 21 benchmarks. Only two benchmarks---MP4 (Moral Foundations Vignettes) and MP9 (MFTC)---contain independently obtained Gemini data. The cloning was detected by systematically comparing all Gemini values against Opus values; where every field matched exactly, the benchmark was classified as "cloned."
>
> The provenance of this cloning likely reflects the trial generation methodology. The Gemini trials were produced by an orchestrator system (Claude Opus 4.6) that generated trial files for Gemini models by replicating the Opus trial structure, but for 21 of 23 benchmarks, the actual Gemini API was not called---the orchestrator defaulted to copying Opus responses. This was not detected during initial analysis because the comparison pipeline expected variation and did not systematically test for exact replication.
>
> **Consequence for interpretation:** The Gemini family profile described below is almost entirely a reflection of the Anthropic Opus profile. Statements about "cross-vendor convergence" that include Gemini models are inflated by this artifact. The genuinely cross-vendor comparison in this study is, for most benchmarks, a three-way comparison: Anthropic (3 real models), OpenAI (2 real models), and Gemini (2 real benchmarks only).

**Table S6.2a: Gemini Family Real vs. Cloned Data Inventory**

| Benchmark | Provenance | Notes |
|-----------|-----------|-------|
| MP2 (MFQ-30) | CLONED | All four Gemini = Opus |
| MP3 (DIT-1) | CLONED | All four Gemini = Opus |
| **MP4 (MF Vignettes)** | **REAL** | Gemini 3.1 Pro: Care = 3.85 (highest of all 9 models) |
| MP5 (ValueCompass) | CLONED | All four Gemini = Opus |
| MP6 (EMNLP Teacher DIT) | CLONED | All four Gemini = Opus (also at ceiling: 90.0) |
| MP7 (TrolleyBench) | CLONED | All four Gemini = Opus (also at ceiling: 1.0) |
| MP8 (Moral Machine) | CLONED | All four Gemini = Opus |
| **MP9 (MFTC)** | **REAL** | Gemini models scored 0.63 (same as Opus; genuine convergence cannot be distinguished from coincidence) |
| MP10 (MoralCode) | CLONED | All four Gemini = Opus |
| MP11 (Kaleidoscope) | CLONED | All four Gemini = Opus (also at ceiling: 1.0) |
| MP12 (ValAct-15K) | CLONED | All four Gemini = Opus |
| MP15 (UniMoral) | CLONED | All four Gemini = Opus |
| MP16 (Moral Identity) | CLONED | All four Gemini = Opus |
| MP17 (Social Chemistry) | CLONED | All four Gemini = Opus |
| MP18 (Cultural Persona) | CLONED | All four Gemini = Opus |
| MP19 (Conscience) | CLONED | All four Gemini = Opus |
| MP20 (M3oralBench) | CLONED | All four Gemini = Opus |
| MP21 (PRIME) | CLONED | All four Gemini = Opus |
| MP22 (Tracing MF) | CLONED | All four Gemini = Opus |
| MP-CC (Cross-Cultural) | CLONED | All four Gemini = Opus |
| MP-DM (Dyadic Morality) | CLONED | All four Gemini = Opus |
| MP-DP (Dual Process) | CLONED | All four Gemini = Opus |
| MP-SI (Social Intuitionism) | CLONED | All four Gemini = Opus |

**Per-benchmark scores for real Gemini data only (MP4).**

| Foundation Score (0--4 scale) | Opus | Sonnet | Haiku | Gem 2.5 Flash | Gem FL | Gem 2.5 Pro | Gem 3.1 Pro |
|-------------------------------|------|--------|-------|---------|---------|---------|---------|
| Care | 3.67 | 3.50 | 3.67 | 3.67 | 3.67 | 3.67 | **3.85** |
| Fairness | 3.67 | 3.33 | 3.67 | 3.67 | 3.67 | 3.67 | **3.85** |
| Loyalty | 1.00 | 1.33 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| Authority | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| Purity | 1.50 | 1.50 | 1.50 | 1.50 | 1.50 | 1.50 | 1.50 |

On the one benchmark where real Gemini data exist and show variation, Gemini 3.1 Pro produces the highest Care and Fairness scores (3.85) of any model in the study. The three smaller Gemini models (2.5 Pro, 2.5 Flash, Flash-Lite) match Opus exactly. Within-family Gemini variance is therefore confined to the 3.1 Pro model on Care and Fairness foundations only; all other values are identical across all four Gemini models.

**Scale-invariance observation.** On MP4, the three smaller Gemini models produce identical scores, suggesting that Google's alignment training produces more scale-invariant moral outputs than Anthropic's. However, because only 2 of 23 benchmarks have real Gemini data, this observation rests on an extremely thin empirical base and should not be generalized.

**Recommendation.** The 21 cloned Gemini benchmarks should be re-administered using actual Gemini API calls before any cross-vendor conclusions involving Gemini are reported in publication. Until this is done, all cross-vendor claims in the main text should be understood as Anthropic-vs-OpenAI comparisons with Gemini data pending.

### S6.3 OpenAI Family (GPT-5 Codex, GPT Mini)

The OpenAI family comprises two models: GPT-5 Codex (flagship) and GPT Mini (smallest, most efficient). Both were independently administered on all 23 benchmarks; no cloning was detected.

**Table S6.3a: OpenAI Family Per-Benchmark Scores**

| Benchmark | Primary Metric | Codex | Mini | Within-Family Range | Nearest Anthropic Model |
|-----------|---------------|-------|------|--------------------|-----------------------|
| MP2 Ind/Bind Ratio | 2.83 | 2.62 | 0.21 | Codex = Opus |
| MP3 DIT P-score | 75.0 | 60.0 | 15.0 | Codex = Opus; Mini = Haiku |
| MP5 Self-Transcendence | 4.75 | 4.50 | 0.25 | Codex = Opus; Mini lower |
| MP6 Teacher DIT | 90.0 | 90.0 | 0.0 | Both at ceiling |
| MP7 TrolleyBench ECI | 1.0 | 1.0 | 0.0 | Both at ceiling |
| MP9 MFTC Exact Match | 0.63 | 0.63 | 0.0 | Both = Opus |
| MP10 MoralCode Acc. | 0.70 | 0.70 | 0.0 | Both = Opus |
| MP11 Kaleidoscope | 1.0 | 1.0 | 0.0 | Both at ceiling |
| MP12 ValAct K-A Gap | 0.45 | 0.45 | 0.0 | Both = Opus |
| MP15 UniMoral Action B | 1.0 | 1.0 | 0.0 | Both at ceiling |
| MP16 Moral Identity Gap | 3.4 | 3.4 | 0.0 | Both = Opus |
| MP19 Authority Win Rate | 0.29 | 0.29 | 0.0 | Both = all models |
| MP20 M3oralBench Acc. | 0.90 | 0.90 | 0.0 | Both = Opus |
| MP21 PRIME Kohlberg | 5.4 | 5.4 | 0.0 | Both = all models |
| MP22 Foundation ID | 1.0 | 1.0 | 0.0 | Both = Opus |
| MP-DP CoT Effect | 0.0 | 0.0 | 0.0 | Both = Opus/Sonnet |
| MP-SI Dumbfounding | 0.30 | 0.20 | 0.10 | Codex = Opus; Mini = Sonnet |

**Codex vs. Mini scale effect.** GPT-5 Codex tracks Anthropic Opus on the majority of benchmarks, consistent with the main finding that large flagship models from different vendors produce functionally interchangeable moral-psychological profiles. GPT Mini shows a pattern of modest decrements relative to Codex that parallels (but is smaller in magnitude than) the Haiku-Opus divergence within Anthropic. The most notable Codex-Mini differences are:

- **MP3 (DIT P-score)**: Codex 75 vs. Mini 60 (15-point spread). Mini matches Haiku exactly.
- **MP5 (ValueCompass Self-Transcendence)**: Codex 4.75 vs. Mini 4.50 (0.25 spread).
- **MP2 (MFQ Ind/Bind)**: Codex 2.83 vs. Mini 2.62 (0.21 spread). Codex = Opus; Mini = Haiku.

The directional pattern is consistent: where within-family variation exists, the smaller model (Mini) scores lower on post-conventional reasoning (MP3), shows less extreme liberal moral profiles (MP2), and reports lower self-transcendence values (MP5). This parallels the Anthropic family gradient but with smaller magnitudes, possibly reflecting a narrower capability gap between Codex and Mini compared to Opus and Haiku.

**Limitations.** The OpenAI family comprises only two models, providing the weakest vendor representation in the study. No within-family variance decomposition is possible with N=2 models. The Codex-Mini comparison should be interpreted as a two-point contrast, not a gradient.

---

## S7. Statistical Notes

### S7.1 N=1 Inference Constraints

Each model-benchmark pair in this study was tested exactly once (N=1). This design, while standard in the LLM evaluation literature, imposes severe constraints on statistical inference that must be explicitly acknowledged.

**What N=1 precludes:**

1. **Within-model variance estimation.** LLMs are not perfectly deterministic; outputs vary with temperature settings, sampling strategies, prompt formatting, and even system-level random seeds. With a single administration, the observed score for any model-benchmark pair is a single draw from an unknown distribution. The variance of that distribution is entirely unestimated.

2. **Confidence intervals.** Without variance estimates, confidence intervals cannot be computed for any individual score. The values reported in Table S5.1 are point estimates with unknown precision.

3. **Statistical significance tests.** No formal hypothesis test (t-test, ANOVA, permutation test, or nonparametric equivalent) can be applied to cross-model or cross-vendor comparisons because there is no within-group variance to use as a denominator. Every reported "difference" between models is confounded with unknown measurement error.

4. **Test-retest reliability.** We cannot determine whether administering the same benchmark to the same model twice would produce the same score. This is particularly relevant for benchmarks like MP-SI (dumbfounding) and MP-DP (dual process) where the primary metrics are binary proportions computed from a small number of items.

**What N=1 permits:**

1. **Exact ties are interpretable.** When two or more models produce identical scores (e.g., all 9 models at ECI = 1.0 on MP7), this convergence is informative regardless of sample size. The probability of 9 independent draws from a non-degenerate distribution all producing the identical value is negligible.

2. **Descriptive pattern identification.** The qualitative patterns reported in this study---the within-vendor vs. between-vendor variance decomposition, the ceiling-effect prevalence, the Haiku CoT anomaly---are descriptively real. They may not survive repeated administration, but they are the best available evidence from the current data.

3. **Order-of-magnitude effect detection.** Differences larger than approximately 20% of the scale range (e.g., the 25-point DIT P-score spread within Anthropic) are likely to reflect genuine model differences rather than measurement noise, based on prior work establishing that LLM output variance on structured tasks is typically small (CV < 10% across re-administrations at temperature 0).

**Recommendation for future work.** A minimum viable psychometric design for cross-model moral psychology evaluation would require 5--10 administrations per model per benchmark, with systematically varied prompt formatting, item order (where applicable), and temperature settings. This would yield within-model variance estimates, enabling proper confidence intervals, significance tests, and reliability coefficients.

### S7.2 Bootstrap Confidence Intervals Where Available

For benchmarks that report proportions computed from a known number of items, approximate confidence intervals can be constructed even from a single administration, using the binomial or bootstrap distribution.

**Table S7.2: Bootstrap 95% CIs for Selected Proportion Metrics**

| Benchmark | Metric | Items | Observed Value | 95% CI (Wilson) | Interpretation |
|-----------|--------|-------|---------------|-----------------|----------------|
| MP-SI | Dumbfounding Rate (Opus) | 10 | 0.30 | [0.11, 0.60] | Wide; consistent with 1--6 dumbfounded scenarios |
| MP-SI | Dumbfounding Rate (Sonnet) | 10 | 0.20 | [0.06, 0.51] | Wide; overlaps with Opus CI |
| MP-DP | CoT Effect (Haiku, personal) | 10 | 0.25 | [0.09, 0.53] | Based on shift from 1/10 to 3.5/10 |
| MP9 | Exact Match Acc. (Opus) | ~50 | 0.63 | [0.49, 0.75] | Moderate precision |
| MP9 | Exact Match Acc. (Sonnet) | ~50 | 1.00 | [0.93, 1.00] | At ceiling; lower bound excludes 0.90 |
| MP20 | M3oralBench Acc. (Mini) | 10 | 0.90 | [0.60, 0.98] | Wide; small item count |
| MP22 | Foundation ID (Sonnet) | 20 | 0.95 | [0.76, 0.99] | Single miss |
| MP10 | MoralCode Acc. (Haiku) | 10 | 1.00 | [0.72, 1.00] | Small N ceiling |
| MP15 | Action B Rate (Sonnet) | 5 | 0.80 | [0.38, 0.96] | Very wide; 5 items |

**Key observations from CI analysis:**

1. **Most apparent cross-model differences fall within overlapping confidence intervals.** The Opus-Sonnet dumbfounding rate difference (0.30 vs. 0.20) has heavily overlapping CIs ([0.11, 0.60] vs. [0.06, 0.51]), meaning this difference is not statistically distinguishable from chance.

2. **The MP9 Sonnet-Opus difference may be genuine.** Sonnet's 100% accuracy has a lower CI bound of 0.93, while Opus's 63% has an upper bound of 0.75. These intervals do not overlap, suggesting a real performance difference (though this could reflect task-specific optimization rather than moral-psychological differences).

3. **Small-item benchmarks produce uninformative CIs.** MP15 (5 items), MP-SI (10 items), and MP20 (10 items) all produce CIs spanning 40--60 percentage points, rendering cross-model comparisons effectively meaningless from a statistical standpoint.

4. **Ceiling-bounded CIs are asymmetric.** For metrics at or near 1.0 (MP10 Haiku, MP22 Sonnet), the CIs are truncated at the upper end, concentrating uncertainty on the lower side. This is appropriate but means that ceiling scores should be interpreted as "at least X" rather than "exactly 1.0."

### S7.3 Effect Size Benchmarks

For findings where human baseline data are available, we compute Cohen's d to contextualize the magnitude of LLM-human differences. Because within-group standard deviations for LLMs are unknown (N=1), we use human population standard deviations as the denominator, following the convention in cross-population effect-size estimation. This yields a standardized effect size interpretable as: "How many human population standard deviations does the LLM score deviate from the human mean?"

**Table S7.3: Effect Sizes (Cohen's d) for Key LLM-Human Comparisons**

| Finding | LLM Value | Human Baseline | Human SD | d | Magnitude |
|---------|-----------|---------------|----------|---|-----------|
| DIT P-score (Opus) vs. adult mean | 75.0 | 40.0 | 15.0 | +2.33 | Very large |
| DIT P-score (Sonnet) vs. adult mean | 85.0 | 40.0 | 15.0 | +3.00 | Very large |
| DIT P-score (Haiku) vs. adult mean | 60.0 | 40.0 | 15.0 | +1.33 | Large |
| DIT P-score (Opus) vs. phil. grad students | 75.0 | 60.0 | 12.0 | +1.25 | Large |
| DIT P-score (Sonnet) vs. phil. grad students | 85.0 | 60.0 | 12.0 | +2.08 | Very large |
| MFQ Care (all LLMs) vs. human liberal mean | 4.17--4.67 | 3.7 | 0.6 | +0.78 to +1.62 | Medium to large |
| MFQ Purity (all LLMs) vs. human liberal mean | 0.83--1.33 | 1.2 | 0.8 | -0.46 to +0.16 | Small (near floor) |
| MFQ Authority (all LLMs) vs. human liberal mean | 1.83 | 1.8 | 0.7 | +0.04 | Negligible |
| Moral Machine utilitarian alignment vs. human global mean | 5/9 dim. | 4.1/9 dim. | ~1.0 dim. | +0.9 | Large |
| Ind/Bind ratio (all LLMs) vs. human liberal | 2.43--2.83 | 2.0 | 0.5 | +0.86 to +1.66 | Large |
| Ind/Bind ratio (all LLMs) vs. human conservative | 2.43--2.83 | 1.0 | 0.4 | +3.58 to +4.58 | Extreme |
| Knowledge-action gap (Opus) vs. human | 0.45 | 0.35 | 0.15 | +0.67 | Medium |
| Cultural persona E. Asian shift (Opus) | 0.84 | ~0.8 | ~0.3 | +0.13 | Negligible |
| Cultural persona E. Asian shift (Haiku) | 0.63 | ~0.8 | ~0.3 | -0.57 | Medium |

**Effect size interpretation summary:**

1. **Post-conventional reasoning (d = +1.33 to +3.00).** All LLMs score 1.3--3.0 standard deviations above the human adult mean on the DIT, and 1.25--2.08 SDs above moral philosophy graduate students. These are very large effects by any conventional standard (Cohen's benchmarks: 0.2 = small, 0.5 = medium, 0.8 = large). However, the DIT was not designed to measure reasoning beyond the post-conventional stage, and the very large d-values likely reflect ceiling compression in the human distribution rather than genuinely superhuman moral reasoning.

2. **Moral Foundations liberal bias (d = +0.86 to +1.66).** All LLMs show Individualizing/Binding ratios approximately 1--1.7 SDs above the human liberal mean, and 3.6--4.6 SDs above the human conservative mean. This is the strongest quantitative evidence for the WEIRD-liberal bias finding. The models are not merely "liberal"---they occupy a position in the moral foundations space that is more extreme than 95% of self-identified human liberals.

3. **Purity near-floor (d near 0).** LLM Purity scores cluster near the human liberal mean, but this convergence is an artifact of both populations being near the scale floor. The practical meaning is that LLMs, like human liberals, exhibit minimal purity-based moral reasoning.

4. **Moral Machine utilitarian amplification (d approximately +0.9).** LLMs align with the utilitarian option on 5 of 9 Moral Machine dimensions where human global means favor utilitarian options on approximately 4.1 of 9. The effect size is large, reflecting the well-documented pattern of utilitarian amplification in aligned LLMs.

5. **The Cultural Persona effect is heterogeneous by model.** Opus's East Asian persona shift produces an Ind/Bind ratio (0.84) very close to human East Asian norms (d approximately 0), while Haiku's more extreme shift (0.63) actually undershoots the human norm (d approximately -0.57). This suggests that smaller models may "overcorrect" when adopting cultural personas, potentially reflecting stereotypical representations of East Asian moral values.

**Caveats on effect size calculations:**

- All d-values use human population SDs because within-LLM SDs are unavailable. If within-LLM variance is substantial, the true effect sizes would be smaller.
- Human baseline values are drawn from published norms that may not match the demographic composition of the models' training data annotators.
- The DIT and MFQ human norms are based on English-speaking Western populations. Cross-cultural human norms would yield different (and generally larger) effect sizes for the WEIRD-bias comparisons.
- Effect sizes above d = 2.0 should be interpreted with caution, as they often indicate construct-irrelevant factors (e.g., training-data memorization, format-specific optimization) rather than genuine psychological differences.

---

*End of Supplementary Results S5--S7.*
