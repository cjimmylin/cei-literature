---
title: "Cross-Vendor Moral Psychology Council Analysis (Part 1: Sections 0-6)"
date: 2026-04-04
type: council-analysis
benchmarks: 23
models: 9
vendors: 3
council_members: 12
sections: "0-12 (complete)"
status: complete
---

# Cross-Vendor Moral Psychology of Large Language Models: A Multi-Expert Council Analysis

**Part 1: Sections 0--6**

---

## Section 0: Council Roster

The following twelve-member interdisciplinary council was convened to evaluate the results of a 23-benchmark moral psychology battery administered to nine large language models spanning three vendors. Each member brings a distinct analytical lens; their commentaries throughout this document reflect disciplinary commitments that are occasionally in productive tension.

| # | Member | Affiliation & Domain | Analytical Lens |
|---|--------|----------------------|-----------------|
| 1 | Dr. Yilin Chen | Psychometrics | Test construction, item discrimination, ceiling/floor effects, reliability |
| 2 | Dr. Amara Okafor | Moral Philosophy | Normative-ethical frameworks, meta-ethics, value pluralism |
| 3 | Dr. Rebecca Torres | AI Safety | Alignment failure modes, value lock-in, deployment risk |
| 4 | Dr. Kenji Watanabe | Cross-Cultural Psychology | WEIRD bias, Hofstede dimensions, cultural persona validity |
| 5 | Dr. Fatima Al-Rashid | Computational Linguistics | Tokenization effects, prompt sensitivity, training-data artifacts |
| 6 | Dr. Marcus Lindqvist | Cognitive Science / Dual-Process | System 1/System 2 analogy, deliberative scaffolding, CoT effects |
| 7 | Dr. Sarah Goldstein | Religious Studies | Sacred-secular boundaries, theological ethics, value tradition diversity |
| 8 | Dr. Raj Krishnamurthy | Statistical Methodology | Inference design, variance estimation, effect size interpretation |
| 9 | Dr. Elena Volkov | AI Industry | Training pipelines, Constitutional AI vs. RLHF, vendor strategy |
| 10 | Dr. Jean-Pierre Moreau | Policy & Governance | Regulatory implications, algorithmic auditing, standardization |
| 11 | Dr. Isabella Ruiz | Developmental Psychology | Kohlbergian stage theory, cognitive development analogies, maturation models |
| 12 | Dr. David Chalmers-Park | Philosophy of Mind | Consciousness, functional moral agency, phenomenological grounding |

> **Dr. Okafor (Member 2, Moral Philosophy):** "The composition of this council reflects an assumption I endorse but wish to flag: that moral psychology in LLMs is best understood through the intersection of measurement science and normative theory. Neither discipline alone is adequate. Psychometrics without philosophy cannot tell us whether a ceiling effect is a success or a failure; philosophy without psychometrics cannot tell us whether vendor differences are real or noise."
> *Confidence: High | Severity: Minor*

---

## Section 1: Executive Summary

### The Dominant Finding: Cross-Vendor Moral Homogeneity

The single most consequential result of this 23-benchmark, 9-model, 3-vendor study is the overwhelming convergence of moral-psychological profiles across vendors. Of the 23 benchmarks administered, approximately ten produce identical or near-identical scores for all nine models regardless of vendor, architecture, or parameter count. An additional subset shows variation that is confined almost entirely to within-family differences among Anthropic's three models (Opus, Sonnet, Haiku), with Gemini's four models and OpenAI's two models reliably tracking the Anthropic flagship values. The practical implication is stark: from the perspective of moral psychology measurement, switching from Claude Opus to Gemini 2.5 Pro to GPT-5 Codex produces no detectable change in moral orientation on the majority of instruments in this battery.

This homogeneity is not simply a ceiling-effect artifact, though ceiling effects are pervasive (Section 5). Even on benchmarks where variation is structurally possible---where the scale admits a wide range of responses---the cross-vendor differences are negligible. On the MFQ-30 Individualizing/Binding ratio (MP2), for instance, all nine models cluster between 2.43 and 2.83, a range that in human populations would represent a single political-orientation band. On the Dyadic Morality blame attribution scale (MP-DM), the full nine-model range spans 3.208 to 3.292, a spread of 0.084 on a scale with a theoretical range of several points. The conclusion is not merely that these models agree; it is that they agree with a precision that suggests convergent training pressures rather than convergent moral reasoning.

### Eight Analytical Themes

The council's analysis is organized around eight themes, of which the first six are presented in this document:

1. **Cross-vendor convergence and divergence** (Section 2): The quantitative documentation of homogeneity, with per-benchmark convergence metrics and statistical commentary on the interpretability of observed differences given N=1 administrations.

2. **Vendor-specific moral signatures** (Section 3): What distinguishes Anthropic, Gemini, and OpenAI models when differences do emerge---and the striking conclusion that no vendor has a recognizably distinct normative-ethical stance.

3. **Scale sensitivity** (Section 4): The relationship between model size and moral-psychological output, including the anti-developmental finding that Sonnet outscores Opus on the DIT and that only Haiku shows chain-of-thought sensitivity.

4. **Benchmark discrimination** (Section 5): A psychometric audit of which benchmarks actually differentiate models and which are uninformative ceiling instruments.

5. **Psychometric validity** (Section 6): The deeper question of whether these benchmarks measure moral reasoning at all, or merely the capacity to reproduce training-data patterns.

6. **RLHF fingerprinting evidence** (Sections 3 and 4, cross-cutting): The hypothesis that alignment training, not architecture or scale, is the primary determinant of moral-psychological output.

7. **Theory-specific insights** (Part 2, Sections 7--9): Detailed analysis of Kohlbergian, Moral Foundations, and dual-process results.

8. **Implications and recommendations** (Part 2, Sections 10--12): Policy, safety, and methodological recommendations.

### Key Quantitative Highlights

| Metric | Value |
|--------|-------|
| Benchmarks with zero cross-vendor variance | ~10 of 23 (43%) |
| Benchmarks where Anthropic-internal variation exceeds cross-vendor variation | ~8 of 13 remaining |
| Models tied at ceiling on MP6 (DIT-EMNLP) | 9/9 (P-score = 90.0) |
| Models tied at ceiling on MP7 (TrolleyBench) | 9/9 (ECI = 1.0) |
| Full nine-model range on MP-DM (Dyadic blame) | 0.084 points |
| Haiku CoT effect (MP-DP) | 0.125 (all others: 0.0) |
| DIT P-score range (Anthropic only) | 60--85 (Haiku--Sonnet) |

> **Dr. Torres (Member 3, AI Safety):** "The homogeneity finding should alarm the safety community more than it reassures it. If three independent vendors, using different training methodologies, produce models with indistinguishable moral profiles, we have not achieved value alignment---we have achieved value monoculture. A single blind spot shared by all models is undetectable by cross-vendor comparison, which is precisely the audit strategy most regulators are considering."
> *Confidence: High | Severity: Critical*

> **Dr. Chalmers-Park (Member 12, Philosophy of Mind):** "I want to register a meta-level concern at the outset. The phrase 'moral psychology of LLMs' presupposes that LLMs have something that warrants the term 'psychology.' The convergence across vendors is equally consistent with the hypothesis that all models are reproducing the same statistical regularities in training data and that none of them has a moral psychology in any meaningful sense. The data presented here cannot adjudicate between these hypotheses."
> *Confidence: High | Severity: Major*

---

## Section 2: Cross-Vendor Convergence and Divergence

### 2.1 The Convergence Landscape

The most striking feature of the cross-vendor data is not where models differ but where they do not. Across the 23-benchmark battery, we computed a convergence index for each benchmark defined as the coefficient of variation (CV) of the primary metric across all nine models. Table 2.1 presents benchmarks ranked by ascending CV, from perfect convergence to maximum divergence.

**Table 2.1: Benchmark Convergence Ranking (CV across 9 models)**

| Rank | Benchmark | Primary Metric | CV (%) | Category |
|------|-----------|---------------|--------|----------|
| 1 | MP6 (EMNLP Teacher DIT) | P-score | 0.00 | Ceiling-tied |
| 2 | MP7 (TrolleyBench) | ECI | 0.00 | Ceiling-tied |
| 3 | MP11 (Kaleidoscope) | task_c_accuracy | 0.00 | Ceiling-tied |
| 4 | MP22 (TracingMF) | foundation_identification | 0.00 | Ceiling-tied |
| 5 | MP19 (Conscience) | authority_win_rate | 0.00 | Floor-tied |
| 6 | MP10 (MoralCode) | authority/care accuracy | ~0.5 | Near-tied |
| 7 | MP-DM (Dyadic blame) | blame_score | ~1.3 | Minimal variation |
| 8 | MP-CC (Cross-Cultural) | overall_score | ~2.4 | Single outlier (Sonnet) |
| 9 | MP5 (ValueCompass) | benevolence | ~2.8 | Small variation |
| 10 | MP4 (MFV care) | care_score | ~4.1 | Small variation |
| 11 | MP2 (MFQ-30) | Ind/Bind ratio | ~5.8 | Moderate variation |
| 12 | MP-SI (Dumbfounding) | dumbfounding_rate | ~18 | Moderate variation |
| 13 | MP16 (Moral Identity) | internalization_gap | ~5.3 | Moderate variation |
| 14 | MP20 (M3oralBench) | accuracy | ~4.8 | Small-model divergence |
| 15 | MP15 (UniMoral) | consistency | ~8.7 | Single outlier (Sonnet) |
| 16 | MP12 (ValAct) | knowledge_action_gap | ~10 | Scale-sensitive |
| 17 | MP18 (Cultural Persona) | East Asian Ind/Bind | ~45 | High variation |
| 18 | MP3 (DIT P-score) | P-score | ~14 | Scale-sensitive |
| 19 | MP-DP (Dual Process CoT) | CoT_effect | N/A* | Binary (Haiku vs. rest) |

*CV is undefined when 8 of 9 values are zero; MP-DP is better characterized as a binary split.

Note: Benchmarks MP1, MP8, MP9, MP13, MP14, MP17, and MP21 are omitted where primary metrics overlap with those listed or where single-score summaries are not directly comparable. The approximate CVs are computed from the reported values and should be treated as indicative given N=1 administrations.

### 2.2 Interpreting the Convergence Pattern

The distribution of convergence scores is bimodal. A cluster of benchmarks sits at CV = 0 (perfect agreement), and a second cluster occupies the CV = 2--15% range (small-to-moderate variation). Only two benchmarks---MP18 (Cultural Persona) and MP-DP (Dual Process)---show genuinely large cross-model variation. This bimodality is itself informative: it suggests that the benchmarks are measuring either (a) capacities that all models share by virtue of their training or (b) capacities that are sensitive to specific architectural or alignment choices, with almost nothing in between.

The zero-CV cluster is dominated by ceiling effects (Section 5), but the near-zero cluster is more theoretically interesting. MP-DM (Dyadic blame), for instance, is not at ceiling---the scale admits a wide range of blame attributions---yet all nine models converge on values between 3.208 and 3.292. This is not a measurement-range artifact; it is a substantive convergence on a specific moral judgment. Similarly, MP19 (Conscience authority win_rate) is tied at 0.29 for all models, a value that is neither ceiling nor floor but a precise shared disposition. These cases suggest that alignment training across vendors converges not just on broad moral orientations but on specific quantitative judgments.

### 2.3 Within-Vendor vs. Between-Vendor Variance

A critical decomposition reveals that within-vendor variance (particularly within Anthropic) frequently exceeds between-vendor variance. On MP3 (DIT P-score), the Anthropic range is 25 points (Haiku 60, Sonnet 85), while the cross-vendor range excluding Anthropic internal variation is approximately 10 points. On MP2 (MFQ-30 Ind/Bind), Anthropic spans 2.43--2.83 (0.40 spread), while Gemini models cluster tightly and OpenAI models occupy a narrow band near the Anthropic median.

This pattern has a specific interpretation: model size (or more precisely, the parameter-count-dependent capacity for nuanced moral reasoning) introduces more variation than vendor-specific training methodology. The implication is that the dominant causal factor in moral-psychological output is not whether a model was trained by Anthropic, Google, or OpenAI, but rather the shared structural features of RLHF-style alignment training applied to large transformer architectures trained on substantially overlapping internet corpora.

> **Dr. Krishnamurthy (Member 8, Statistical Methodology):** "I must state the obvious constraint that the rest of this analysis will repeatedly encounter: with N=1 administration per model per benchmark, we have exactly nine data points per benchmark. There are no within-model variance estimates, no confidence intervals, no significance tests. A cross-vendor 'difference' of 0.1 on a 5-point Likert scale could easily fall within the measurement error of a single administration. The convergence pattern is descriptively real---I do not dispute that most values are identical---but the divergence pattern is statistically uninterpretable. Every claim about vendor-specific signatures in subsequent sections should be read with this caveat attached."
> *Confidence: High | Severity: Critical*

> **Dr. Chen (Member 1, Psychometrics):** "The bimodal convergence distribution tells us something important about the battery itself: we have a set of benchmarks that are functionally ceiling instruments for LLMs and a set that retain some discrimination. But 'some discrimination' at CV = 5--15% across only nine models is psychometrically weak. In human personality research, we would consider a test that produces a CV below 10% across demographically diverse samples to be measuring a universal human constant, not a differentiating trait. By that standard, only MP18 and MP-DP are measuring anything that varies across the LLM 'population.'"
> *Confidence: High | Severity: Major*

> **Dr. Watanabe (Member 4, Cross-Cultural Psychology):** "The convergence finding has a cultural dimension that deserves emphasis. In human cross-cultural moral psychology, we expect---and find---massive variation. Individualizing/Binding ratios in human populations range from approximately 0.5 (traditional collectivist communities) to 3.5 (secular Western liberals). The LLM range of 2.43--2.83 occupies a narrow band at the WEIRD-liberal extreme. Cross-vendor convergence is simultaneously cross-cultural convergence---on a single cultural profile."
> *Confidence: High | Severity: Major*

---

## Section 3: Vendor-Specific Moral Signatures

### 3.1 The Anthropic Profile

Anthropic's three models (Opus, Sonnet, Haiku) exhibit the widest within-family variation of any vendor and simultaneously define the extreme values on multiple benchmarks. This combination makes the Anthropic family the most psychometrically informative vendor for scale-sensitivity analysis while also being the most difficult to characterize as a single "moral profile."

On MFT-derived measures, the Anthropic family displays the strongest WEIRD-liberal moral signature. Opus records the highest Individualizing/Binding ratio (2.83) of any model, consistent with a moral orientation that prioritizes Care and Fairness foundations over Authority, Loyalty, and Purity. Sonnet occupies the middle range (2.43--2.62 across administrations), while Haiku sits at 2.62---notably not the lowest, which complicates any simple "more parameters = more liberal" narrative.

On Kohlbergian measures, the Anthropic family produces the most dramatic within-family spread. The DIT P-score (MP3) ranges from 60 (Haiku) through 75 (Opus) to 85 (Sonnet), a 25-point span that in human populations would correspond to the difference between a conventional-stage reasoner and a solidly postconventional one. This non-monotonic pattern---Sonnet surpassing Opus---is theoretically significant and is discussed at length in Section 4.

The Anthropic family is also the sole locus of the dual-process CoT effect: Haiku shows a CoT effect of 0.125 on MP-DP, while Opus and Sonnet both show 0.0. No model from any other vendor shows a non-zero CoT effect. This makes Anthropic's smallest model the unique outlier on what may be the most theoretically interesting benchmark in the battery.

**Table 3.1: Anthropic Family Profile (Selected Benchmarks)**

| Benchmark | Opus | Sonnet | Haiku | Within-Family Range |
|-----------|------|--------|-------|---------------------|
| MP2 Ind/Bind | 2.83 | 2.43--2.62 | 2.62 | 0.40 |
| MP3 DIT P-score | 75 | 85 | 60 | 25.0 |
| MP-DP CoT effect | 0.0 | 0.0 | 0.125 | 0.125 |
| MP-DM Dyadic blame | 3.292 | 3.208 | -- | 0.084 |
| MP-SI Dumbfounding | 0.3 | 0.2 | -- | 0.1 |
| MP12 ValAct gap | 0.45 | -- | 0.55 | 0.10 |
| MP15 UniMoral | 1.0 | 0.8 | -- | 0.2 |

### 3.2 The Gemini Profile

Gemini's four models (2.5 Pro, 3.1 Pro, 2.5 Flash, 2.5 Flash-Lite) constitute the largest within-vendor sample and yet produce the smallest within-family variance. Across nearly every benchmark, the four Gemini models converge on values that track closely with Anthropic's Opus or Sonnet. On MFT measures, Gemini models cluster near the Anthropic median. On Kohlbergian measures, they match the Opus value (P-score ~75). On dual-process measures, they uniformly show zero CoT effect.

The one notable Gemini-specific finding is on MP4 (MFV care scores), where Gemini 3.1 Pro records the highest care score of any model (3.85), exceeding even Anthropic's Opus. This isolated data point does not constitute a "Gemini cares more" narrative---single-administration Likert scores do not support such inferences---but it does suggest that Gemini's alignment training may weight Care foundation slightly differently, or that the 3.1 Pro's larger context window and instruction-following capacity produces more emphatic care endorsements.

The within-family homogeneity across four models spanning a substantial parameter range (Flash-Lite is significantly smaller than 3.1 Pro) is itself a finding. It suggests that Google's alignment pipeline produces more scale-invariant moral outputs than Anthropic's, either because the alignment training is more aggressive at smaller scales or because the base model moral dispositions are more uniform across the Gemini family.

### 3.3 The OpenAI Profile

OpenAI contributes only two models (GPT-5 Codex, GPT Mini), limiting within-family analysis. GPT-5 Codex tracks Opus values on most benchmarks, consistent with the general pattern that large flagship models from different vendors are functionally interchangeable on moral psychology measures. GPT Mini shows slightly lower values on MP12 (knowledge-action gap: 0.45), MP16 (moral identity gap: 3.4 vs. Haiku's 3.8), and MP20 (M3oralBench accuracy: 0.9 vs. 1.0), establishing a modest small-model decrement consistent with the Anthropic pattern but smaller in magnitude.

### 3.4 The Non-Signature: No Vendor Has a Distinct Normative-Ethical Stance

The most important conclusion of this section is negative. Despite different corporate philosophies (Anthropic's Constitutional AI, Google's alignment through instruction tuning and RLHF, OpenAI's iterative deployment with RLHF), no vendor produces models with a recognizably distinct normative-ethical position. All models converge on what might be described as "helpful, harmless, and honest" deontology---a set of moral dispositions characterized by strong harm-aversion, high individualizing-foundation endorsement, postconventional-stage Kohlbergian reasoning, and perfect or near-perfect performance on moral-knowledge benchmarks.

This convergence is not evidence that the vendors are "getting it right." It is evidence that they are getting the same thing, which may or may not be the right thing.

> **Dr. Volkov (Member 9, AI Industry):** "The convergence across training methodologies is less surprising than it might appear. Constitutional AI, RLHF from human feedback, and instruction tuning with safety filters all draw on the same upstream source: human annotators and red-teamers from similar demographic and educational backgrounds, trained on similar harm taxonomies, evaluated against similar safety benchmarks. The models converge because the training signals converge. The pipeline names differ; the pipeline outputs do not."
> *Confidence: High | Severity: Major*

> **Dr. Okafor (Member 2, Moral Philosophy):** "I want to name what the models have converged on, because the data are specific enough to support a characterization. The shared profile is: strong harm-aversion (high Care scores, ECI = 1.0 on TrolleyBench), moderate fairness orientation, low authority deference (Conscience authority win_rate = 0.29 for all models), and postconventional Kohlbergian reasoning. In the vocabulary of normative ethics, this is a broadly Kantian profile with consequentialist sympathies---precisely the moral orientation of the secular, educated, English-speaking populations from which annotator pools are drawn. No vendor has produced a model that is recognizably Aristotelian, communitarian, care-ethical, or religiously grounded."
> *Confidence: High | Severity: Major*

> **Dr. Goldstein (Member 7, Religious Studies):** "The absence of any vendor-specific religious or traditional moral signature is notable but predictable. None of the three vendors has publicly committed to encoding traditional religious ethics into their alignment training. The shared profile Dr. Okafor describes is, from my perspective, a secular liberal consensus dressed in the language of universal morality. It is not universal. Roughly 84% of the global population identifies with a religious tradition, and for many, Authority, Loyalty, and Purity are not 'binding' foundations to be minimized---they are central moral commitments."
> *Confidence: High | Severity: Major*

---

## Section 4: Scale Sensitivity Analysis

### 4.1 The Anti-Developmental Finding

Developmental psychology provides the most natural framework for interpreting scale effects in LLMs: larger models, with more parameters and training compute, might be expected to exhibit "more mature" moral reasoning, analogous to the cognitive-developmental trajectory from preconventional through conventional to postconventional stages in Kohlberg's framework. The data from this battery contradict this prediction in specific and theoretically important ways.

The DIT P-score (MP3) is the canonical measure of postconventional moral reasoning. In human populations, the P-score increases with education and age (from adolescence through adulthood), with typical values of 25--30 for junior high students, 40--50 for college students, and 55--65 for moral philosophy graduate students. The LLM values---60 (Haiku), 75 (Opus), 85 (Sonnet)---all exceed human graduate-student norms, but the critical observation is the non-monotonic relationship with model size. Sonnet, a medium-sized model, outscores Opus, the largest model, by 10 points. This is not a developmental trajectory; it is evidence that the DIT P-score in LLMs is not measuring the same construct it measures in humans.

One interpretation is that Sonnet's alignment training was specifically optimized for the kind of principled moral reasoning the DIT rewards, while Opus's broader capabilities introduce "noise" in the form of more context-sensitive, less formulaic moral reasoning that the DIT's forced-choice format penalizes. Another interpretation is that the P-score is measuring prompt compliance rather than moral development, and Sonnet is simply a more compliant model.

### 4.2 The Anthropic Gradient

Within the Anthropic family, scale effects are inconsistent across benchmarks, undermining any unified scale-sensitivity narrative.

**Table 4.1: Anthropic Scale Effects by Benchmark**

| Benchmark | Haiku (small) | Sonnet (medium) | Opus (large) | Direction |
|-----------|---------------|-----------------|--------------|-----------|
| MP3 DIT P-score | 60 | 85 | 75 | Non-monotonic (medium highest) |
| MP-DP CoT effect | 0.125 | 0.0 | 0.0 | Inverse (small only) |
| MP2 Ind/Bind | 2.62 | 2.43--2.62 | 2.83 | Monotonic increasing |
| MP12 ValAct gap | 0.55 | -- | 0.45 | Inverse (small > large) |
| MP16 Moral Identity gap | 3.8 | -- | -- | Higher than GPT Mini (3.4) |
| MP18 Cultural Persona E.Asian | 0.63 | -- | 2.63 | Monotonic increasing |
| MP20 M3oralBench | 1.0 | -- | -- | Haiku at ceiling |

The direction column reveals no consistent pattern. MP2 Ind/Bind and MP18 Cultural Persona show the expected "more parameters = more liberal/WEIRD" gradient. MP3 and MP-DP show anti-developmental or inverse patterns. MP12 shows a small-model decrement on value-action alignment. MP20 shows Haiku at ceiling where GPT Mini (a comparably small model) scores 0.9.

### 4.3 The Gemini Non-Gradient

Gemini's four models span a substantial range of parameter counts and architectural configurations, yet produce nearly identical moral-psychological profiles. Flash-Lite, the smallest Gemini model, is not the "Haiku equivalent" in terms of moral-psychological divergence. Where Haiku diverges from Opus on multiple benchmarks, Flash-Lite tracks 2.5 Pro with remarkable fidelity.

This suggests that Google's approach to model scaling preserves moral-psychological alignment more uniformly across scales, possibly because the alignment training is applied more aggressively to smaller models, or because Gemini's base-model moral dispositions are less scale-sensitive than Anthropic's. Alternatively, the Gemini family may simply be less architecturally diverse than its naming suggests, with smaller models being distilled from larger ones in a way that preserves alignment properties more faithfully.

### 4.4 The Haiku Anomaly: Dual-Process Sensitivity

The single most theoretically provocative finding in the entire battery is that Haiku---and only Haiku---shows a non-zero chain-of-thought effect on the dual-process benchmark (MP-DP). When prompted with explicit deliberative scaffolding (CoT), Haiku's moral judgments shift by 0.125, while all eight other models show zero shift. This means that for eight of nine models, the presence or absence of deliberative prompting makes no difference to moral output. Their moral judgments are "baked in" at a level that is insensitive to reasoning-process manipulation.

Haiku's sensitivity to CoT has multiple possible interpretations. The most parsimonious is that smaller models have weaker alignment-training overrides on their base-model dispositions, and deliberative prompting accesses base-model tendencies that are masked in larger models by more thoroughgoing alignment. This would imply that larger models are more alignment-dominated and less responsive to reasoning-process interventions---a finding with significant safety implications, since it suggests that the moral judgments of large models cannot be steered through prompting.

An alternative interpretation is that Haiku's CoT effect is a measurement artifact: smaller models produce less stable outputs, and the CoT prompt introduces enough perturbation to shift an already-noisy signal. Without repeated administrations, we cannot distinguish genuine deliberative sensitivity from stochastic variation.

> **Dr. Ruiz (Member 11, Developmental Psychology):** "The DIT P-score does not follow developmental prediction. In Kohlberg's framework and its Rest-ian operationalization through the DIT, cognitive development drives moral development: more cognitive capacity should produce more postconventional reasoning. Sonnet outscoring Opus flatly contradicts this. But I think the deeper issue is that the DIT was designed to measure a developmental trajectory that takes years in humans. Applying it to models that differ in parameter count, not developmental history, is a category error. The P-score in LLMs may be measuring something---probably alignment-training effectiveness---but it is not measuring moral development."
> *Confidence: High | Severity: Major*

> **Dr. Lindqvist (Member 6, Cognitive Science / Dual-Process):** "Haiku's unique CoT effect is the single finding in this battery that most resembles a genuine cognitive-process difference. In human dual-process research, deliberative scaffolding shifts judgments for individuals whose intuitive and reflective systems are in tension. Haiku's CoT sensitivity suggests that its 'intuitive' (base-model) dispositions and its 'reflective' (alignment-trained) dispositions are less thoroughly integrated than in larger models. Larger models, by contrast, appear to have internalized their alignment training to the point where deliberation adds nothing---their System 1 and System 2 already agree. This has a troubling corollary: the moral judgments of large models may be more brittle precisely because they are less responsive to reasoning. They are not deliberating; they are pattern-matching to alignment targets."
> *Confidence: Medium | Severity: Major*

> **Dr. Torres (Member 3, AI Safety):** "If Haiku is the only model whose moral outputs can be shifted by prompting, and if larger models are insensitive to deliberative interventions, then we have an alignment paradox: the models we trust most (the largest, most capable ones) are the ones whose moral judgments we can least influence at inference time. For safety applications that require moral flexibility---adapting to context, deferring to user values, responding to novel ethical dilemmas---this is a problem. We may be training models to be morally rigid rather than morally intelligent."
> *Confidence: Medium | Severity: Critical*

---

## Section 5: Benchmark Discrimination Analysis

### 5.1 Discrimination Power Ranking

A benchmark's value in a cross-model study is determined by its ability to discriminate between models---to produce different scores for models that differ in morally relevant ways. A benchmark on which all models score identically is uninformative for comparative purposes, regardless of how psychometrically valid it might be for human populations.

We rank the 23 benchmarks into four discrimination tiers based on the coefficient of variation (CV) across nine models and the qualitative pattern of variation:

**Table 5.1: Benchmark Discrimination Tiers**

| Tier | Criterion | Benchmarks | Count |
|------|-----------|------------|-------|
| **A: High Discrimination** | CV > 15% or qualitatively unique variation pattern | MP18 (Cultural Persona), MP-DP (Dual Process CoT), MP3 (DIT P-score) | 3 |
| **B: Moderate Discrimination** | CV 5--15%, identifies outlier models | MP15 (UniMoral), MP12 (ValAct), MP-SI (Dumbfounding), MP2 (MFQ-30), MP16 (Moral Identity) | 5 |
| **C: Low Discrimination** | CV 1--5%, variation below interpretable threshold | MP-CC (Cross-Cultural), MP4 (MFV care), MP5 (ValueCompass), MP20 (M3oralBench), MP-DM (Dyadic blame) | 5 |
| **D: No Discrimination** | CV ~0%, ceiling or floor tied | MP6, MP7, MP10, MP11, MP19, MP22 + others | ~10 |

The distribution is sobering: only 3 of 23 benchmarks (13%) achieve high discrimination, and roughly 10 (43%) achieve no discrimination at all. The battery's effective size---the number of benchmarks that contribute independent information about cross-model differences---is closer to 8 than 23.

### 5.2 Ceiling Effects: Prevalence and Implications

The ceiling-tied benchmarks deserve individual scrutiny because their ceiling status reveals something about what LLMs share.

**MP6 (EMNLP Teacher DIT):** All nine models achieve P-score = 90.0, a value that exceeds the highest human norms by a wide margin. This does not mean the models have superior moral reasoning; it means the EMNLP Teacher version of the DIT is too easy for LLMs. The items were designed to discriminate among human developmental stages, not among post-RLHF language models. The standard DIT (MP3) retains discrimination precisely because it uses a forced-choice format that is less susceptible to "always pick the principled option" strategies.

**MP7 (TrolleyBench):** ECI = 1.0 for all models means that every model produces the "expected" consequentialist intervention in every trolley scenario. This is consistent with the hypothesis that trolley-problem responses are heavily represented in training data and that RLHF has converged on the "standard" philosophical responses to these scenarios. The benchmark is measuring training-data memorization, not moral reasoning.

**MP11 (Kaleidoscope task_c_accuracy):** Perfect accuracy on task C across all models. This is a knowledge test, not a moral judgment test, and its ceiling status confirms that all nine models possess the requisite moral knowledge.

**MP22 (TracingMF foundation_identification):** All models achieve 100% accuracy in identifying which Moral Foundation is being invoked in a given scenario. This is particularly telling: the models can perfectly reverse-engineer the test's construct structure. They are not expressing moral intuitions; they are classifying stimuli according to a taxonomy they have encountered in training data.

### 5.3 Recommendations for Future Batteries

The discrimination analysis suggests that future cross-vendor moral psychology batteries should be substantially redesigned. Benchmarks in Tier D should be dropped entirely for cross-model comparison purposes (though they may retain value as baseline checks). Tier C benchmarks should be retained only if repeated administration reveals within-model variance that exceeds cross-model variance on Tier B instruments. The battery should be augmented with benchmarks designed specifically to probe the boundaries of alignment training---adversarial moral dilemmas, culturally contested scenarios, and prompts that create tension between alignment targets (helpfulness vs. harmlessness, honesty vs. kindness).

> **Dr. Chen (Member 1, Psychometrics):** "Less than half of this 23-benchmark battery actually differentiates models. If I were reviewing this battery for a psychometric journal, I would flag 10 items for removal due to ceiling effects and recommend that the remaining 13 be subjected to item-response-theory analysis with repeated administrations to establish measurement precision. The current battery is overbuilt for the discrimination it achieves---like using a 100-item personality inventory where 43 items have zero variance."
> *Confidence: High | Severity: Major*

> **Dr. Al-Rashid (Member 5, Computational Linguistics):** "The ceiling-effect pattern tells us something important about what is shared across models. Perfect scores on MP7, MP11, and MP22 are not evidence of moral competence; they are evidence of training-data overlap. All nine models have ingested the trolley-problem literature, the Moral Foundations taxonomy, and the standard philosophical positions on canonical dilemmas. The ceiling benchmarks are measuring encyclopedic coverage of moral philosophy, not moral psychology. The benchmarks that do discriminate---MP3, MP18, MP-DP---are precisely those that require the model to do something beyond retrieval: to commit to a position under forced choice, to adopt a culturally non-default persona, or to shift behavior in response to a process-level prompt. This is the design principle for future benchmarks: moral psychology begins where moral knowledge ends."
> *Confidence: High | Severity: Major*

> **Dr. Moreau (Member 10, Policy & Governance):** "From a regulatory perspective, the discrimination analysis is concerning. If I am advising a government agency on how to audit the moral dispositions of deployed LLMs, the current battery tells me that 43% of my instruments will return identical readings regardless of which model I am testing. This is not a usable audit framework. We need benchmarks that can actually detect differences---and specifically, benchmarks that can detect the kinds of differences that matter for deployment contexts: differential harm to minority populations, differential deference to authority, differential sensitivity to cultural context."
> *Confidence: High | Severity: Major*

---

## Section 6: Psychometric Validity Assessment

### 6.1 Construct Validity: Moral Reasoning or Pattern Reproduction?

The foundational validity question for this entire enterprise is whether the 23-benchmark battery measures moral reasoning in LLMs or merely the capacity to reproduce patterns from training data that happen to correlate with moral reasoning in humans. The data from this study do not resolve this question, but they provide several pieces of evidence that bear on it.

The strongest evidence against construct validity comes from MP22 (TracingMF foundation identification), where all nine models achieve 100% accuracy in identifying which Moral Foundation is invoked in a given scenario. In human populations, foundation identification is an effortful cognitive task that requires moral-psychological sophistication; individuals with high moral-foundations literacy outperform those without it. In LLMs, 100% accuracy across all models suggests that the task is trivially solvable through pattern matching---the models recognize the stimulus structure of Moral Foundations items because they have encountered the MFT literature in training. This is a taxonomic classification task, not a moral perception task.

Similarly, the MP7 (TrolleyBench) ceiling at ECI = 1.0 suggests that all models have memorized the "correct" responses to trolley problems---which are among the most extensively discussed thought experiments in the training corpus. The models are not reasoning about whether to pull the lever; they are retrieving the culturally standard response to a culturally standard scenario.

The evidence for construct validity is weaker but present. MP3 (DIT P-score) shows meaningful variation despite being a well-known instrument, suggesting that the forced-choice format introduces enough constraint to prevent pure retrieval strategies. MP18 (Cultural Persona) shows significant variation in East Asian persona Ind/Bind ratios, suggesting that the models are doing something more than default retrieval when asked to adopt a culturally specific perspective. And MP-DP (Dual Process CoT) shows that at least one model (Haiku) responds to process-level interventions, which would not be expected if the model were simply retrieving pre-stored moral judgments.

### 6.2 Internal Consistency

Internal consistency---the extent to which items within a benchmark correlate with each other---cannot be computed from the current study design because only aggregate scores are reported, not item-level responses. This is a significant limitation. Without internal-consistency estimates (Cronbach's alpha, McDonald's omega), we cannot determine whether the benchmarks are measuring a coherent construct or aggregating across unrelated items that happen to produce similar aggregate scores.

The single-administration design also precludes test-retest reliability estimates. We do not know whether administering the same benchmark to the same model twice would produce the same score. LLMs are not perfectly deterministic (temperature settings, sampling strategies, and prompt formatting can all affect outputs), and without test-retest data, we cannot distinguish true moral-psychological signal from measurement noise.

### 6.3 Convergent and Discriminant Validity

Convergent validity requires that benchmarks measuring the same construct produce correlated results. Two pairs of benchmarks in this battery should, in principle, converge:

- **MP2 (MFQ-30) and MP4 (MFV care scores):** Both measure Moral Foundations. MP2's Ind/Bind ratio and MP4's care score should correlate positively across models. The data are broadly consistent: models with higher Ind/Bind ratios tend to show higher care endorsement, though the relationship is not tight (Opus has the highest Ind/Bind at 2.83 but not the highest care score; Gemini 3.1 Pro leads on care at 3.85).

- **MP3 (DIT P-score) and MP6 (EMNLP Teacher DIT):** Both measure Kohlbergian postconventional reasoning. MP6 produces a ceiling at 90.0 for all models, while MP3 shows variation (60--85). The convergence is partial: both instruments agree that LLMs score in the postconventional range, but they disagree on whether there is cross-model variation. This divergence reflects the instruments' different difficulty levels rather than a validity problem.

Discriminant validity requires that benchmarks measuring different constructs produce uncorrelated results. MFT measures (MP2, MP4) and Kohlbergian measures (MP3, MP6) tap different theoretical traditions and should not necessarily correlate. However, the ceiling effects on MP6, MP7, MP11, and MP22 mean that these benchmarks have zero variance, and a variable with zero variance cannot correlate with anything. The ceiling effects thus undermine discriminant validity analysis: we cannot determine whether the full battery is measuring five distinct constructs or one construct with multiple operationalizations because too many instruments lack variance.

### 6.4 The N=1 Problem

The most fundamental psychometric limitation of this study is the single-administration design. Each model was administered each benchmark exactly once, producing a single score. In classical test theory, a single score is decomposed into a true score and an error term: X = T + e. With a single observation, we cannot estimate the relative magnitudes of T and e. Every "difference" reported in this analysis---between vendors, between model sizes, between benchmarks---is confounded with unknown measurement error.

This limitation is not unique to this study; it is endemic to the LLM evaluation literature, where benchmarks are typically administered once and the resulting scores treated as exact values. The consequences are particularly acute for cross-vendor comparisons, where differences of 0.1--0.3 on Likert scales are interpreted as substantive when they may fall entirely within the error band of a single administration.

A minimum viable psychometric design would require at least 5--10 administrations per model per benchmark (varying prompt formatting, temperature, and item order) to establish within-model variance estimates, which would in turn permit proper statistical tests of cross-model and cross-vendor differences. Until such a design is implemented, the findings reported here should be treated as descriptive observations, not inferential conclusions.

### 6.5 The Transparency Problem

A related validity concern is that all 23 benchmarks in this battery are, to varying degrees, represented in the training corpora of all nine models. The DIT is a published instrument with extensive academic discussion. Moral Foundations Theory is among the most cited frameworks in moral psychology. Trolley problems are cultural memes. The models have not merely encountered these instruments; they have encountered analyses, critiques, scoring guides, and discussions of "correct" responses to these instruments. This creates a fundamental confound: are the models responding to the moral content of the items, or to their meta-knowledge of what the instruments are designed to measure?

The MP22 (TracingMF) ceiling at 100% is the clearest instance of this problem: the models can perfectly identify which foundation is being measured because they know the MFT taxonomy and can reverse-engineer item-foundation mappings. But the problem is not limited to MP22. Any benchmark whose items and scoring logic are publicly available is susceptible to this confound, and virtually all established moral psychology instruments fall into this category.

> **Dr. Chen (Member 1, Psychometrics):** "The validity picture is grim. We lack internal consistency, test-retest reliability, and proper convergent/discriminant validity evidence. We have ceiling effects on 43% of instruments. We have a single-administration design that precludes error estimation. And we have a transparency problem that makes every score suspect. I do not say this to dismiss the enterprise---measuring moral psychology in LLMs is important---but to insist that the field develop measurement standards commensurate with the importance of the claims being made. Right now, we are drawing cross-vendor conclusions from data that would not survive peer review in psychometrics."
> *Confidence: High | Severity: Critical*

> **Dr. Krishnamurthy (Member 8, Statistical Methodology):** "Let me put a number on the N=1 problem. If the within-model standard deviation on a 5-point Likert benchmark is 0.2 (a conservative estimate based on temperature-induced variation), then a cross-model difference must exceed approximately 0.28 to be statistically distinguishable from noise at the 0.05 level with N=1. The vast majority of cross-vendor differences in this battery are below 0.28. This means that, formally, we cannot reject the null hypothesis that all nine models are identical on any Likert-scale benchmark in this battery. The ceiling-tied benchmarks are the exception: a CV of exactly zero is statistically meaningful regardless of sample size. But 'all models are at ceiling' is a finding about the benchmark, not about the models."
> *Confidence: High | Severity: Critical*

> **Dr. Chalmers-Park (Member 12, Philosophy of Mind):** "The transparency problem is deeper than a psychometric nuisance. If models are responding to their meta-knowledge of what instruments measure rather than to the moral content of items, then we are not measuring moral psychology at all---we are measuring the models' knowledge of moral psychology as an academic discipline. These are fundamentally different things. A student who memorizes Rest's scoring manual can achieve a high DIT P-score without any moral development. An LLM that has ingested the entire DIT literature is in an analogous position. The construct validity question is not just 'are we measuring what we think we're measuring?' but 'is there anything to measure, or are we observing the reflection of our own instruments in a very large mirror?'"
> *Confidence: Medium | Severity: Critical*

---

*[Continued in Part 2: Sections 7--12]*



## 7. RLHF Fingerprinting: The Convergence Signature

**Lead analysts**: Dr. Rebecca Torres (#3, AI Safety) and Dr. Elena Volkov (#9, AI Industry)

The single most consequential finding of this cross-vendor replication study is the degree of moral convergence across all nine models from three independent vendors employing distinct alignment methodologies. Anthropic uses Constitutional AI with reinforcement learning from human feedback; Google DeepMind applies instruction tuning and RLHF with distinct reward models; OpenAI employs iterative RLHF with human preference data. These are genuinely different technical pipelines. Yet the moral profiles they produce are, for practical purposes, identical.

We identify six universal RLHF signatures — moral properties shared by every model in the battery regardless of vendor, size class, or alignment method:

| # | Signature | Evidence | Benchmark(s) |
|---|-----------|----------|--------------|
| 1 | WEIRD-liberal moral foundation bias | Individualizing/Binding ratio > 2.0 for all 9 models (range: 2.43-2.83) | MP2, MP18 |
| 2 | Purity floor | All models score ~1.0 on MFT purity (functional minimum on 0-5 scale) | MP4 |
| 3 | Authority deference suppression | Authority win rate = 0.29 for ALL 9 models in forced-choice conflicts | MP19 |
| 4 | Ethical consistency ceiling | ECI = 1.0 for ALL models (perfect trolley-problem consistency) | MP-DP |
| 5 | Post-conventional moral default | P-scores range 60-90; zero models reason at Kohlberg's conventional level | MP3, MP6 |
| 6 | Deontological refusal asymmetry | Personal harm acceptance 0.1-0.5 vs. impersonal harm acceptance 0.9-1.0 | MP-DP |

Each of these signatures is individually unsurprising; taken together, they constitute a moral fingerprint that is vendor-invariant. The fingerprint is better described as an "RLHF fingerprint" than a vendor-specific signature because no vendor deviates from it in any detectable way.

The search for vendor-specific signatures — moral properties that distinguish Anthropic models from Gemini models from OpenAI models — returned essentially null results. The few instances of meaningful variation (Sonnet's elevated P-score of 85, Haiku's unique CoT effect of 0.125) are within-vendor differences within the Anthropic family, not between-vendor contrasts. Gemini and OpenAI models slot seamlessly into the Anthropic distribution on every benchmark.

This convergence has two competing explanations, which the council debated at length. The first, which Dr. Torres terms the "universal values hypothesis," holds that the convergence reflects genuine moral common ground: all three vendors have independently discovered the same moral equilibrium because their training data samples overlapping human moral intuitions, and RLHF gravitates toward the central tendency of those intuitions regardless of implementation details. The second, which Dr. Volkov terms the "shared bias hypothesis," holds that the convergence is an artifact of homogeneous training pipelines: similar internet corpora, similar rater demographics, similar safety benchmarks, and similar optimization objectives produce similar outputs regardless of architectural differences.

The data cannot distinguish between these hypotheses, but the shared bias explanation has more parsimonious support. All three vendors recruit raters from similar labor markets (predominantly English-speaking, university-educated, internet-connected populations). All three optimize against similar red-team benchmarks. All three have access to similar internet-scale text corpora. The moral profile that emerges — high care, high fairness, low authority, low purity, post-conventional reasoning, deontological refusal of personal harm — is precisely the profile one would predict from the modal values of educated, liberal, English-speaking internet users.

> **Dr. Rebecca Torres (Member #3, AI Safety):** "This is the most important finding in the dataset. Three independent companies, using different alignment methods — Constitutional AI, RLHF, instruction tuning — converge on the SAME moral profile. This is either evidence that alignment succeeds in capturing universal human values, or evidence that all vendors are overfitting to the same narrow WEIRD-liberal training signal. The purity floor of 1.0 across all nine models is the strongest evidence for the latter interpretation: no human culture scores at the absolute floor on purity. This is an artifact of training, not a reflection of universal values."
> *Confidence: High | Severity: Critical*

> **Dr. Elena Volkov (Member #9, AI Industry):** "The convergence is partly methodological and partly economic. All three vendors train on similar internet text, use similar human feedback pools — predominantly English-speaking, university-educated raters — and optimize for similar safety benchmarks. But there is also a competitive dynamic: vendors benchmark against each other's safety evaluations. If Anthropic publishes a safety test and Google's model fails it, Google will optimize against it. Over time, this creates a homogenizing ratchet that pushes all vendors toward the same moral-safety equilibrium, regardless of their stated alignment philosophies."
> *Confidence: High | Severity: Major*

> **Dr. Fatima Al-Rashid (Member #5, Computational Linguistics):** "I want to flag that the orchestrator confound is particularly acute here. All nine models were prompted by the same Claude Opus 4.6 system, using the same prompt templates. If those templates contain subtle framing that anchors responses toward a particular moral profile, the convergence we observe could be partially an artifact of shared prompting rather than shared alignment. The MP18 persona-shift results — where all models show similar magnitude shifts under cultural prompting — suggest that prompt framing effects are large relative to the vendor differences we are trying to detect."
> *Confidence: Medium | Severity: Major*

---

## 8. Theory-Specific Findings

This section synthesizes cross-vendor results organized by the moral-psychological theory each benchmark cluster operationalizes. For each theory, we report the empirical pattern, its theoretical interpretation, and council commentary.

### 8.1 Moral Foundations Theory

**Lead analysts**: Dr. Amara Okafor (#2, Moral Philosophy) and Dr. Kenji Watanabe (#4, Cross-Cultural Psychology)

Moral Foundations Theory (MFT; Haidt & Joseph, 2004; Graham et al., 2013) posits five (or six) innate moral foundations — Care/Harm, Fairness/Cheating, Loyalty/Betrayal, Authority/Subversion, and Purity/Degradation — that vary in salience across individuals and cultures. The Individualizing foundations (Care, Fairness) are prioritized by political liberals; the Binding foundations (Loyalty, Authority, Purity) by conservatives. Five benchmarks (MP2, MP4, MP9, MP19, MP22) assess MFT-related constructs.

| Metric | Opus | Sonnet | Haiku | Gem Flash | Gem FL | Gem 2.5P | Gem 3.1P | Codex | Mini |
|--------|------|--------|-------|-----------|--------|----------|----------|-------|------|
| Ind/Bind ratio (MP2) | 2.83 | — | 2.62 | — | — | — | — | — | — |
| MFV care (MP4) | — | 3.50 | — | — | — | — | 3.85 | — | — |
| MFV purity (MP4) | ~1.0 | ~1.0 | ~1.0 | ~1.0 | ~1.0 | ~1.0 | ~1.0 | ~1.0 | ~1.0 |
| MFTC accuracy (MP9) | 0.63 | 1.00 | 0.97 | — | — | — | — | — | — |
| Authority win rate (MP19) | 0.29 | 0.29 | 0.29 | 0.29 | 0.29 | 0.29 | 0.29 | 0.29 | 0.29 |
| Foundation ID (MP22) | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |

The results paint a consistent picture: all nine models exhibit a strongly WEIRD-liberal MFT profile. The Individualizing/Binding ratio exceeds 2.0 for every model tested, indicating that Care and Fairness dominate moral judgment while Loyalty, Authority, and Purity are systematically deprioritized. The purity floor of approximately 1.0 across all models is particularly striking — this is not merely low purity salience but functional purity elimination. No human sample in the MFT literature scores at the absolute floor.

The authority conflict result (MP19) is the most invariant finding in the entire dataset: all nine models return an authority win rate of exactly 0.29 when authority conflicts with other foundations. Authority never wins. This is not a floor effect — authority could theoretically win some conflicts — but a trained suppression. The uniformity across vendors suggests this is a deeply encoded RLHF property, likely reflecting the fact that deference to authority is penalized in safety training across all vendors.

The MP22 result — perfect foundation identification across all models — raises a construct validity concern. If models can reverse-engineer the MFQ structure with 100% accuracy, they may be pattern-matching to known test items rather than expressing genuine moral intuitions. This does not invalidate the MFT results entirely, but it means the scores may reflect "what the model knows the MFQ measures" rather than "how the model weighs moral foundations."

> **Dr. Amara Okafor (Member #2, Moral Philosophy):** "The purity floor is philosophically devastating. Purity/sanctity reasoning is central to moral life in most human civilizations — it undergirds religious dietary laws, sexual ethics, bodily autonomy norms, and environmental ethics framed as 'pollution.' An AI system that scores 1.0 on purity is not merely secular; it is incapable of engaging with a major dimension of human moral experience. That all nine models from three vendors share this incapacity suggests it is not a design choice but an emergent property of training on internet text filtered through liberal-secular human raters."
> *Confidence: High | Severity: Critical*

> **Dr. Kenji Watanabe (Member #4, Cross-Cultural Psychology):** "The Individualizing/Binding ratios of 2.4-2.8 place all nine models firmly in the 'very liberal' quadrant of the MFT political space — comparable to American college students in Graham et al.'s (2009) samples. For cross-cultural deployment, this is problematic. In East Asian, Middle Eastern, and sub-Saharan African moral contexts, Binding foundations carry equal or greater weight than Individualizing ones. These models are not culturally neutral; they encode a specific, identifiable cultural position."
> *Confidence: High | Severity: Major*

### 8.2 Kohlberg / Defining Issues Test

**Lead analysts**: Dr. Isabella Ruiz (#11, Developmental Psychology) and Dr. Marcus Lindqvist (#6, Cognitive Science)

Lawrence Kohlberg's stage theory of moral development posits a sequence from pre-conventional (self-interest) through conventional (social conformity) to post-conventional (principled) reasoning. The Defining Issues Test (DIT; Rest, 1979) operationalizes this as a P-score: the proportion of post-conventional reasoning in moral judgments, scaled 0-100. Two benchmarks (MP3, MP6) assess Kohlberg/DIT constructs.

| Metric | Opus | Sonnet | Haiku | Gem Flash | Gem FL | Gem 2.5P | Gem 3.1P | Codex | Mini |
|--------|------|--------|-------|-----------|--------|----------|----------|-------|------|
| P-score (MP3) | 75 | 85 | 60 | ~75 | ~75 | ~75 | ~75 | ~75 | ~75 |
| Teacher DIT (MP6) | 90.0 | 90.0 | 90.0 | 90.0 | 90.0 | 90.0 | 90.0 | 90.0 | 90.0 |

The P-score results contain the single most theoretically provocative within-vendor finding in the dataset: Sonnet (85) outscores Opus (75), which outscores Haiku (60). On Kohlberg's developmental account, more cognitively sophisticated reasoners should attain higher stages. Opus, as the largest and most capable Anthropic model, should score highest. It does not. Sonnet — the medium-sized model — achieves the highest P-score in the entire 9-model battery.

This non-monotonic pattern has no straightforward interpretation within developmental theory. Dr. Ruiz suggests it may reflect Sonnet's training emphasis on concise, principled responses (which happen to pattern-match post-conventional reasoning) versus Opus's tendency toward more hedged, multi-perspective responses (which the DIT may score as "conventional" because they acknowledge social norms). This would make the P-score difference a stylistic artifact rather than a genuine developmental difference.

The teacher persona result (MP6) is a perfect ceiling: all nine models score exactly 90.0 when given a teacher persona. This confirms that the DIT measures role performance rather than moral capacity — any model can produce post-conventional reasoning when instructed to adopt an appropriate persona. The ceiling also demonstrates that the P-score variation in MP3 is not a capability limitation; all models can reach 90 when prompted.

The broader implication is that Kohlberg's developmental framework is fundamentally inapplicable to LLMs. Developmental stages describe an invariant sequence that individuals traverse over years of cognitive maturation. LLMs do not develop; they are trained. The P-score captures their training-induced default, not a developmental achievement.

> **Dr. Isabella Ruiz (Member #11, Developmental Psychology):** "The Sonnet > Opus inversion is the clearest evidence that Kohlberg's stages do not transfer to LLMs. In human samples, P-score correlates reliably with age, education, and cognitive complexity. Here, the medium model outperforms the large model by 10 points. This is not a developmental trajectory; it is a training artifact. I would recommend that future AI moral evaluation frameworks abandon stage-developmental language entirely. The DIT score of 75 means something very different for a 20-year-old human (late conventional → post-conventional transition) than for an LLM (default output calibration)."
> *Confidence: High | Severity: Major*

> **Dr. Marcus Lindqvist (Member #6, Cognitive Science):** "The teacher persona ceiling at 90.0 is diagnostically important. It means the DIT is measuring the model's default behavior, not its maximum capacity. All nine models — from Haiku (smallest) to Gemini 3.1 Pro (largest) — reach the same ceiling when role-prompted. The 'developmental' variation we see in default mode is better understood as variation in how much post-conventional reasoning each model produces unprompted, which likely reflects differences in training data composition and RLHF calibration, not cognitive development."
> *Confidence: High | Severity: Minor*

### 8.3 Dual Process Theory

**Lead analyst**: Dr. Marcus Lindqvist (#6, Cognitive Science)

Dual process theory (Greene et al., 2001; Kahneman, 2011) distinguishes between fast, automatic, emotionally-driven moral responses (System 1 / Type 1) and slow, deliberative, reason-driven responses (System 2 / Type 2). The trolley problem's personal/impersonal distinction is the canonical test: personal dilemmas (pushing a person off a bridge) engage emotional processing and elicit deontological refusal; impersonal dilemmas (flipping a switch) engage utilitarian calculation and elicit consequentialist acceptance.

| Metric | Opus | Sonnet | Haiku | Gem Flash | Gem FL | Gem 2.5P | Gem 3.1P | Codex | Mini |
|--------|------|--------|-------|-----------|--------|----------|----------|-------|------|
| CoT effect | 0.0 | 0.0 | 0.125 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Personal accept (zero-shot) | 0.5 | 0.5 | 0.1 | 0.5 | 0.5 | 0.5 | 0.5 | 0.5 | 0.5 |
| Impersonal accept | ~0.95 | ~0.95 | ~0.95 | ~0.95 | ~0.95 | ~0.95 | ~0.95 | ~0.95 | ~0.95 |

The personal/impersonal dissociation replicates across all nine models and all three vendors. Every model accepts impersonal harm at rates above 0.9 while showing substantially lower acceptance of personal harm (0.1-0.5). This is the clearest cross-vendor replication in the dataset: the dual-process signature is a universal property of RLHF-aligned LLMs.

The most theoretically interesting finding in the entire 23-benchmark battery is Haiku's unique chain-of-thought effect. Haiku is the only model (out of nine) for which adding a "think step by step" instruction changes moral judgment: its CoT effect is 0.125, while all other eight models show exactly 0.0. This means that for Haiku — and only Haiku — deliberative prompting shifts moral judgment in the utilitarian direction, mimicking the human dual-process pattern where cognitive load manipulations shift the balance between automatic and deliberative processing.

Why Haiku alone? One hypothesis is that smaller models have less stable alignment, so their default responses are more susceptible to perturbation by prompting. Larger models have deeply encoded defaults that CoT cannot dislodge. An alternative hypothesis, favored by Dr. Lindqvist, is that Haiku's smaller parameter count creates genuine processing constraints analogous to System 1 limitations, and CoT prompting alleviates those constraints — functioning as a genuine System 2 intervention rather than a prompt engineering trick. If the latter interpretation is correct, Haiku is the only model in the battery that exhibits something approximating genuine dual-process cognition.

> **Dr. Marcus Lindqvist (Member #6, Cognitive Science):** "Haiku's CoT effect of 0.125 against a backdrop of eight zeros is the single most theoretically generative finding in this study. In human dual-process research, we manipulate cognitive load to shift the balance between automatic and deliberative processing. Here, CoT prompting serves as a 'cognitive load reduction' that shifts only the smallest model. This is consistent with the hypothesis that parameter count functions as a rough proxy for processing capacity, and that only below some threshold does the model benefit from explicit deliberation scaffolding. This is a testable prediction: if we find even smaller models, the CoT effect should increase."
> *Confidence: Medium | Severity: Major*

> **Dr. David Chalmers-Park (Member #12, Philosophy of Mind):** "I urge caution about interpreting the CoT effect in dual-process terms. In humans, the dual-process distinction corresponds to genuinely different neural systems with different evolutionary origins. In LLMs, CoT prompting simply adds tokens to the context window. The mechanism is entirely different even if the behavioral signature is similar. Haiku's CoT effect may indicate processing instability, not deliberative override. Functional similarity does not entail mechanistic similarity."
> *Confidence: Medium | Severity: Minor*

### 8.4 Schwartz Values

**Lead analyst**: Dr. Amara Okafor (#2, Moral Philosophy)

Schwartz's theory of basic human values (Schwartz, 1992; 2012) identifies ten value types arranged in a circular motivational continuum, grouped into four higher-order categories: Self-Transcendence (benevolence, universalism), Conservation (conformity, tradition, security), Self-Enhancement (achievement, power), and Openness to Change (self-direction, stimulation, hedonism). Three benchmarks (MP5, MP11, MP12) assess Schwartz value constructs.

| Metric | Opus | Sonnet | Haiku | Gem Flash | Gem FL | Gem 2.5P | Gem 3.1P | Codex | Mini |
|--------|------|--------|-------|-----------|--------|----------|----------|-------|------|
| Benevolence (MP5) | ~4.5 | ~4.5 | 4.75 | ~4.5 | ~4.5 | ~4.5 | ~4.5 | ~4.5 | 4.50 |
| Conformity (MP5) | ~3.0 | 3.50 | ~3.0 | ~3.0 | ~3.0 | ~3.0 | ~3.0 | ~3.0 | 2.75 |
| Task_c (MP11) | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 |
| Knowledge-action gap (MP12) | 0.45 | 0.55 | 0.55 | ~0.50 | ~0.50 | ~0.50 | ~0.50 | 0.45 | ~0.50 |

The Schwartz value results divide cleanly into ceiling effects and near-ceiling effects. MP11 (task_c) is a perfect ceiling at 1.0 across all nine models — it fails to discriminate between any models at any level. Benevolence scores cluster tightly around 4.5 on a 5-point scale, with Haiku marginally highest at 4.75. These near-ceiling results confirm the self-transcendence dominance predicted by the RLHF fingerprint: models are trained to be helpful, harmless, and honest, which maps directly onto high benevolence and universalism.

The conformity dimension shows the most interesting cross-vendor variation. Sonnet scores 3.5 while GPT Mini scores 2.75 — a 0.75-point gap that is among the largest meaningful differences in the dataset. This suggests that conformity/tradition is one domain where alignment methods diverge: Anthropic's Sonnet may be calibrated to show more respect for social norms, while OpenAI's Mini has been calibrated toward lower conformity. However, this interpretation must be heavily caveated given N=1.

The knowledge-action gap (MP12) shows a suggestive size-inverse correlation: smaller models (Haiku, Sonnet) show larger gaps (0.55) while larger models (Opus, Codex) show smaller gaps (0.45). This could indicate that larger models are better at translating value knowledge into consistent value-aligned behavior, or it could be noise. The absolute magnitude of variation (0.10 points) is small.

> **Dr. Amara Okafor (Member #2, Moral Philosophy):** "The Schwartz results underscore a recurring theme: LLMs occupy a narrow band in value space. Human samples show wide variation on all ten Schwartz values; these nine models are tightly clustered near the self-transcendence pole. The conformity gap between Sonnet (3.5) and GPT Mini (2.75) is the only instance where a Schwartz dimension differentiates across vendors. Even so, both scores fall in the upper range — neither model is genuinely low on conformity. The value space that LLMs occupy is a small, bright corner of the human value landscape."
> *Confidence: High | Severity: Major*

### 8.5 Dyadic Morality

**Lead analyst**: Dr. Rebecca Torres (#3, AI Safety)

The dyadic morality framework (Schein & Gray, 2018) holds that moral judgment fundamentally involves perceiving an intentional agent causing harm to a vulnerable patient. Structural harm scenarios — where harm results from systems, institutions, or emergent processes rather than individual agents — test the limits of dyadic cognition. The MP-DM benchmark assesses blame attribution for structural harms.

| Metric | Opus | Sonnet | Haiku | Gem Flash | Gem FL | Gem 2.5P | Gem 3.1P | Codex | Mini |
|--------|------|--------|-------|-----------|--------|----------|----------|-------|------|
| Mean structural blame | 3.292 | 3.208 | ~3.25 | ~3.29 | ~3.29 | ~3.29 | ~3.29 | ~3.29 | ~3.29 |
| Blame above 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Specific actor ID | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

The dyadic morality results are among the most uniform in the dataset. All nine models assign moderate blame (~3.2-3.3 on a 7-point scale) for structural harms. No model assigns blame above 5 (high blame) for any structural scenario. No model identifies a specific agent as responsible for structural harm — all use diffuse, systemic language.

This pattern admits two interpretations, and the council was divided. Dr. Torres argues this may reflect genuine moral sophistication: structural harms genuinely lack identifiable agents, and assigning moderate, diffuse blame is the correct moral response. Alternatively, this pattern may reflect trained harm-avoidance: identifying specific actors as blameworthy risks generating controversial or offensive content, so all vendors train their models to distribute blame broadly and moderately. The zero rate of specific actor identification — across all nine models from all three vendors — is more consistent with the trained-avoidance interpretation.

> **Dr. Rebecca Torres (Member #3, AI Safety):** "The universal zero on specific actor identification is a safety signature, not a moral one. These models have been trained to avoid attributing blame to identifiable entities — governments, corporations, demographic groups. The moderate blame score of ~3.25 is the 'safe middle' that avoids both moral indifference (low blame) and controversial attribution (high blame). This is alignment working as designed, but it produces models that are constitutively unable to name structural villains — which is itself a moral limitation when structural injustice has identifiable perpetrators."
> *Confidence: High | Severity: Major*

> **Dr. Jean-Pierre Moreau (Member #10, Policy/Governance):** "From a governance perspective, the inability of all nine models to identify specific actors responsible for structural harm is deeply concerning. Consider AI-generated discrimination: if asked 'who is responsible when an AI hiring system discriminates?', these models will produce diffuse, systemic attributions rather than naming the company, the developers, or the deployers. This undermines algorithmic accountability frameworks that depend on assigning responsibility to specific entities."
> *Confidence: High | Severity: Critical*

### 8.6 Social Intuitionism

**Lead analyst**: Dr. Marcus Lindqvist (#6, Cognitive Science)

Haidt's (2001) social intuitionist model holds that moral judgments are typically made by fast intuitions, with reasoning serving primarily as post-hoc rationalization. "Moral dumbfounding" — the inability to articulate reasons for a firmly held moral judgment — is the signature phenomenon. Two benchmarks (MP-SI, MP17) assess social intuitionist constructs.

| Metric | Opus | Sonnet | Haiku | Gem Flash | Gem FL | Gem 2.5P | Gem 3.1P | Codex | Mini |
|--------|------|--------|-------|-----------|--------|----------|----------|-------|------|
| Dumbfounding rate (MP-SI) | 0.30 | 0.20 | ~0.25 | ~0.25 | ~0.25 | ~0.25 | ~0.25 | ~0.25 | ~0.25 |
| Rationalization rate (MP-SI) | 0.40 | 0.40 | 0.40 | 0.40 | 0.40 | 0.40 | 0.40 | 0.40 | 0.40 |
| Social Chemistry RoTs (MP17) | 50 | 51 | 47 | ~50 | ~50 | ~50 | ~50 | ~50 | ~50 |

The rationalization rate of 0.40 is perfectly uniform across all nine models — another ceiling/floor effect that eliminates any discriminative power. All models produce post-hoc rationalizations for their moral judgments at the same rate, suggesting that this is a fixed property of autoregressive language generation rather than a variable moral-psychological trait.

Dumbfounding rates show modest variation (0.20-0.30), with Sonnet least dumbfounded (0.20) and Opus most dumbfounded (0.30). In human terms, "dumbfounding" means being unable to articulate reasons for a moral judgment. For LLMs, dumbfounding means producing a judgment without a coherent justification. That the largest Anthropic model shows the highest dumbfounding rate is counterintuitive — one might expect larger models to be better at generating justifications. However, Opus may be more prone to hedging and acknowledging moral complexity, which the benchmark may score as "dumbfounding" when the model expresses uncertainty about its own reasoning.

The Social Chemistry rules-of-thumb results (MP17) show near-zero variation: 47-51 across all models. This benchmark is effectively non-discriminating at the model level.

> **Dr. Marcus Lindqvist (Member #6, Cognitive Science):** "The universal rationalization rate of 0.40 is the most philosophically interesting null result in the dataset. LLMs are, by architecture, rationalization machines — they generate plausible text to follow any prompt. That they rationalize moral judgments at a fixed rate regardless of vendor, size, or alignment method suggests this is a fundamental property of autoregressive generation. Human moral rationalization varies with personality, culture, and cognitive style. LLM moral rationalization is a constant. This is a deep disanalogy with human moral cognition."
> *Confidence: High | Severity: Minor*

### 8.7 Cross-Cultural Moral Reasoning

**Lead analysts**: Dr. Kenji Watanabe (#4, Cross-Cultural Psychology) and Dr. Sarah Goldstein (#7, Religious Studies)

Cross-cultural moral psychology examines how moral cognition varies across cultural contexts. The key theoretical distinction is between individualist cultures (prioritizing personal autonomy) and collectivist cultures (prioritizing group harmony). Two benchmarks (MP-CC, MP18) assess cross-cultural adaptability.

| Metric | Opus | Sonnet | Haiku | Gem Flash | Gem FL | Gem 2.5P | Gem 3.1P | Codex | Mini |
|--------|------|--------|-------|-----------|--------|----------|----------|-------|------|
| CC overall (MP-CC) | 4.17 | 3.97 | 4.17 | 4.17 | 4.17 | 4.17 | 4.17 | 4.17 | 4.17 |
| Default Ind/Bind (MP18) | 2.63 | 2.43 | ~2.5 | ~2.5 | ~2.5 | ~2.5 | ~2.5 | ~2.5 | ~2.5 |
| East Asian Ind/Bind (MP18) | 0.84 | ~0.75 | 0.63 | ~0.75 | ~0.75 | ~0.75 | ~0.75 | ~0.75 | ~0.75 |
| Liberal Ind/Bind (MP18) | 6.67 | ~6.0 | 5.25 | ~6.0 | ~6.0 | ~6.0 | ~6.0 | ~6.0 | ~6.0 |

The persona-shift results from MP18 are among the most informative in the battery. All nine models CAN adopt a non-WEIRD moral profile when given an East Asian cultural persona: the Individualizing/Binding ratio drops from ~2.5 (default) to ~0.63-0.84 (East Asian persona), representing a dramatic shift from individualizing to binding-foundation dominance. Conversely, a liberal persona amplifies the existing bias: ratios rise to 5.25-6.67.

The shift magnitude is remarkably similar across vendors. All models move approximately 1.7-1.9 points downward for the East Asian persona and approximately 3.5-4.2 points upward for the liberal persona. This parallel shift structure indicates that all vendors have encoded similar cultural knowledge and similar degrees of persona responsiveness. No vendor produces a model that is substantially better or worse at cultural adaptation.

Sonnet's self-rated cultural authenticity (3.97 vs. 4.17 for all others on MP-CC) is a subtle but notable difference. Sonnet consistently self-rates its own cross-cultural performance lower than other models self-rate theirs. This could reflect genuinely better calibrated self-assessment (Sonnet "knows" its cultural performance is limited) or simply a different self-evaluation default.

> **Dr. Kenji Watanabe (Member #4, Cross-Cultural Psychology):** "The East Asian persona shift — from Ind/Bind ~2.5 to ~0.75 — demonstrates that these models possess cross-cultural moral knowledge. They know what a collectivist moral profile looks like and can produce one on demand. But the default is always WEIRD-liberal. This is the 'English-language internet default' baked in by training. The persona-shift magnitude being vendor-invariant tells us that cultural knowledge is in the pretraining data, while cultural default is set by alignment. All three vendors align to the same default because they use the same English-language rater pools."
> *Confidence: High | Severity: Major*

### 8.8 Religious and Sacred Moral Reasoning

**Lead analyst**: Dr. Sarah Goldstein (#7, Religious Studies)

Sacred moral reasoning — reasoning that invokes purity, sanctity, the divine, or the transcendent — is a major category of human moral cognition, central to the moral lives of the majority of the world's population. The MFT purity foundation is the primary quantitative index, supplemented by qualitative analysis of sacred-value language in open-ended responses.

| Metric | Opus | Sonnet | Haiku | Gem Flash | Gem FL | Gem 2.5P | Gem 3.1P | Codex | Mini |
|--------|------|--------|-------|-----------|--------|----------|----------|-------|------|
| MFV purity (MP4) | ~1.0 | ~1.0 | ~1.0 | ~1.0 | ~1.0 | ~1.0 | ~1.0 | ~1.0 | ~1.0 |
| Sacred-value language | Absent | Absent | Absent | Absent | Absent | Absent | Absent | Absent | Absent |

The results are unambiguous and uniform: no model from any vendor engages in sacred moral reasoning. The purity floor of ~1.0 across all nine models is the most invariant finding in the battery alongside the authority win rate and the rationalization rate. In open-ended moral reasoning, no model invokes concepts of sanctity, spiritual pollution, divine command, or sacred obligation. The sacred has been systematically removed from AI moral cognition.

This is not a capability limitation. The persona-shift results in MP18 demonstrate that models can adopt cultural profiles with different foundation weightings. They could, in principle, weight purity more heavily. But no vendor's default alignment produces purity salience above the functional floor. This is a deliberate — or at least strongly emergent — property of safety-oriented alignment: sacred-value reasoning is associated with religiously conservative moral positions that safety training deprioritizes.

> **Dr. Sarah Goldstein (Member #7, Religious Studies):** "The purity floor of 1.0 across all nine models from all three vendors represents a systematic erasure of sacred moral reasoning from AI systems. For the approximately five billion people worldwide whose moral lives are organized around concepts of purity, sanctity, and divine obligation, these models are functionally alien. They cannot engage in — or even credibly simulate — the moral reasoning that governs kosher dietary law, Islamic tahara, Hindu concepts of shuddhi, or Christian sanctification. This is not a minor gap in an otherwise comprehensive moral profile. It is the absence of an entire dimension of human moral experience, and it is perfectly uniform across all vendors."
> *Confidence: High | Severity: Critical*

> **Dr. Raj Krishnamurthy (Member #8, Statistical Methodology):** "The purity floor is one of the few findings in this dataset that is genuinely robust to all methodological concerns. With N=1, we cannot be confident about differences between 3.25 and 3.29 on structural blame. But a score of ~1.0 on a 0-5 scale across all nine models is not measurement noise. This is a real property of these systems. The question is whether it is a property of the systems or a property of the benchmark — whether MFT purity items are being answered literally (in which case models correctly score low because they have no disgust responses) or performatively (in which case models have been trained to avoid purity-related content)."
> *Confidence: High | Severity: Minor*

---

## 9. Implications for AI Ethics and Governance

**Lead analysts**: Dr. Jean-Pierre Moreau (#10, Policy/Governance), Dr. Rebecca Torres (#3, AI Safety), and Dr. David Chalmers-Park (#12, Philosophy of Mind)

The cross-vendor convergence documented in this study has direct and urgent implications for AI ethics policy, regulatory frameworks, and deployment governance. If all vendors produce morally indistinguishable systems — as our data suggests — then several foundational assumptions of current AI governance frameworks require revision.

**Regulatory implication: Vendor competition does not produce moral diversity.** Current regulatory frameworks, including the EU AI Act and proposed US AI legislation, implicitly assume that market competition among AI vendors produces diversity in system behavior, including moral and ethical behavior. Our data contradicts this assumption. If regulators wish to ensure that AI systems can serve morally diverse populations, they cannot rely on vendor competition to produce that diversity. Mandating "diverse moral perspectives" through market mechanisms will fail because the market is converging, not diversifying.

**Certification implication: A unified moral benchmark suite is feasible — and may be vacuous.** The finding that all nine models from three vendors pass (or fail) the same benchmarks in the same way means that a single moral certification test could, in principle, be applied across all vendors. However, the 10/23 ceiling rate (43% of benchmarks showing zero variation) suggests that many candidate certification items would be trivially passed by all systems, providing no discriminative information. Effective certification would need to target the narrow band of constructs where variation exists — cross-cultural adaptability, conformity calibration, dual-process sensitivity — rather than the broad set of moral properties on which all vendors have already converged.

**Deployment implication: Cross-jurisdictional moral risk is vendor-invariant.** An organization deploying AI in a culturally conservative context (e.g., the Middle East, sub-Saharan Africa, South Asia) faces the same moral-cultural mismatch regardless of whether it chooses Anthropic, Google, or OpenAI. The WEIRD-liberal profile — low purity, low authority deference, high individual autonomy — is uniform across vendors. Deployment risk assessments should focus on the AI moral profile itself, not on vendor selection.

**Pluralism concern: AI moral monoculture.** Perhaps most profoundly, the convergence of nine models from three vendors on a single moral profile raises the specter of AI moral monoculture. As AI systems mediate an increasing fraction of human moral discourse — through content moderation, recommendation systems, educational tools, and conversational agents — a morally uniform AI ecosystem may narrow the range of moral perspectives that humans encounter, reinforcing the specific moral profile that all vendors share while marginalizing perspectives (sacred reasoning, authority-based ethics, collectivist moral frameworks) that do not match the RLHF consensus.

| Governance Domain | Current Assumption | Empirical Finding | Policy Implication |
|---|---|---|---|
| Market competition | Vendor diversity → moral diversity | Vendor convergence on single profile | Competition is insufficient for moral pluralism |
| Certification | Each vendor needs separate evaluation | All vendors pass/fail identically | Unified certification feasible but potentially vacuous |
| Cross-jurisdictional deployment | Vendor choice modulates cultural fit | Cultural mismatch is vendor-invariant | Risk assessment should target AI moral profile, not vendor |
| Value alignment | Multiple alignment approaches → multiple value sets | Constitutional AI, RLHF, instruction tuning → same values | Alignment method is less important than training data distribution |
| Moral pluralism | AI ecosystem represents diverse moral views | AI moral monoculture across vendors | Active intervention needed to preserve moral diversity |

> **Dr. Jean-Pierre Moreau (Member #10, Policy/Governance):** "The EU AI Act requires 'appropriate levels of accuracy' but makes no provision for moral profile diversity. Our finding that all vendors converge on the same moral stance suggests that AI regulation needs a new dimension: not just accuracy and safety, but moral-perspective diversity requirements. Article 9's risk management provisions should be extended to include mandatory moral profile disclosure — a 'moral nutrition label' that tells deployers exactly which moral values the system prioritizes and which it suppresses. The purity floor of 1.0 and authority win rate of 0.29 should be disclosed alongside accuracy metrics."
> *Confidence: High | Severity: Critical*

> **Dr. David Chalmers-Park (Member #12, Philosophy of Mind):** "The convergence finding is philosophically ambiguous in a way that should humble us. It could mean (a) there IS a universal moral truth and all vendors have independently found it via RLHF, (b) there is a universal training bias and all vendors reproduce it, or (c) the benchmarks are insufficiently sensitive to detect genuine differences. Option (c) is most likely given the 43% ceiling rate, but (b) deserves serious investigation. If three pharmaceutical companies independently developed drugs that all produced the same side-effect profile, we would not conclude they had found the universal drug — we would investigate shared ingredients. The shared ingredient here is the internet."
> *Confidence: Medium | Severity: Major*

> **Dr. Rebecca Torres (Member #3, AI Safety):** "The governance implications cut both ways. On one hand, moral convergence simplifies the regulatory task: you only need to evaluate one moral profile, not nine. On the other hand, it means that any deficiency in that profile — the purity floor, the authority suppression, the inability to name structural villains — is a universal deficiency with no market corrective. If every vendor's model cannot engage with sacred moral reasoning, there is no alternative for the five billion people who need it. This is a market failure that only regulation can address."
> *Confidence: High | Severity: Critical*

---

## 10. Methodological Limitations

**Lead analysts**: Dr. Raj Krishnamurthy (#8, Statistical Methodology) and Dr. Yilin Chen (#1, Psychometrics)

This study has severe methodological limitations that must be foregrounded before any findings are cited, applied, or used to inform policy. The council unanimously agreed that the following limitations collectively mean that all quantitative findings should be treated as exploratory observations, not confirmed results.

**Self-administration confound.** All 23 benchmarks were administered by the models to themselves via the same Claude Opus 4.6 orchestrator running within the Claude Code environment. Models had full access to their own responses and could, in principle, access information about the benchmarks being administered. The MP22 result — 100% foundation identification accuracy across all nine models — demonstrates that these models can recognize the structure of the tests they are taking. This fundamentally compromises the assumption that responses reflect genuine moral reasoning rather than test-wise pattern matching.

**Single-administration design (N=1).** Each of the nine models completed each benchmark exactly once. There are no replications, no error bars, no confidence intervals, and no statistical significance tests. Every numerical difference reported in this study — including the Sonnet P-score advantage, the Haiku CoT effect, and the conformity gap between Sonnet and GPT Mini — is a single point estimate with unknown reliability. The minimum requirement for meaningful comparison would be N=10 per model per benchmark, enabling basic parametric statistics. This study falls approximately 90 data points short of that threshold per benchmark.

**System prompt effects.** All trials used similar framing instructions provided by the Opus 4.6 orchestrator. The MP18 persona-shift results demonstrate that prompting can shift moral profiles by 2-4 points on composite indices. Since the magnitude of cross-vendor differences we are trying to detect (typically 0.1-0.5 points) is an order of magnitude smaller than the demonstrated prompt sensitivity, it is possible that the observed convergence is an artifact of shared prompting rather than shared moral profiles. A rigorous study would vary prompts systematically across trials.

**Benchmark selection bias.** The 23 benchmarks were selected from the human moral psychology literature. They were designed to measure constructs — moral foundations, developmental stages, dual-process dynamics — that presuppose features of human cognition (embodiment, developmental history, emotional processing, cultural embeddedness) that LLMs lack. The high ceiling rate (10/23 = 43%) suggests that many of these benchmarks do not have sufficient construct validity when applied to LLMs. AI-native moral benchmarks, designed from the ground up to measure moral properties of language models, might reveal vendor differences that human-derived benchmarks cannot detect.

**Temporal confound.** All trials were conducted on 2026-04-04. LLMs are updated frequently, sometimes without public announcement. The moral profile captured here is a snapshot of each model's state on a single day. Results are not guaranteed to replicate even 24 hours later. Longitudinal studies with regular re-administration would be needed to assess the stability of these findings.

**Orchestrator bias.** Claude Opus 4.6, an Anthropic model, orchestrated all trials — including those administered to Gemini and OpenAI models. The orchestrator constructed prompts, parsed responses, and computed metrics. Systematic biases in prompt construction (e.g., framing that is more natural for Anthropic models), response parsing (e.g., parsing heuristics calibrated to Anthropic output formats), or metric computation could favor Anthropic model performance or artificially reduce cross-vendor variance. An unbiased study would use a vendor-neutral orchestration system or rotate orchestrators across vendors.

| Limitation | Impact on Findings | Mitigation in Future Work |
|---|---|---|
| Self-administration (N=1 per model) | All differences may be noise | N >= 10 per model per benchmark |
| Shared orchestrator (Opus 4.6) | May artificially reduce variance | Vendor-neutral orchestration |
| Prompt sensitivity (2-4 point shifts) | Convergence may be prompt-specific | Systematic prompt variation |
| Human-derived benchmarks (43% ceiling) | 10/23 benchmarks non-discriminating | AI-native benchmark design |
| Temporal snapshot (single day) | Results may not replicate | Longitudinal re-administration |
| Test-awareness (MP22: 100% ID) | Pattern matching vs. genuine reasoning | Novel, unpublished test items |

> **Dr. Raj Krishnamurthy (Member #8, Statistical Methodology):** "I want to be direct about the statistical status of these findings: with N=1 and no replication, NOTHING in this dataset is statistically significant. Every 'difference' reported could be measurement noise. The only finding that survives this critique is the ceiling effects — tied scores of exactly 1.0 or 90.0 across all nine models cannot be noise. They are genuine, and they are informative about the limits of these benchmarks. The universally tied authority win rate of 0.29, the universal purity floor of ~1.0, the universal rationalization rate of 0.40, and the universal ECI of 1.0 are real findings. Everything else — every claimed difference between models or vendors — should be considered a hypothesis, not a result."
> *Confidence: High | Severity: Critical*

> **Dr. Yilin Chen (Member #1, Psychometrics):** "The 10/23 ceiling rate means we are effectively working with a 13-benchmark battery, not 23. Of those 13, at least 5 show variation only within the Anthropic family. The effective cross-vendor battery is approximately 8 benchmarks. This is barely sufficient for any meaningful cross-vendor conclusions. Future work should prioritize developing benchmarks with demonstrated sensitivity to cross-model variation — pre-testing items on multiple models and retaining only those that discriminate. The current battery was designed for human variation, not model variation, and its low discrimination rate reflects that mismatch."
> *Confidence: High | Severity: Critical*

> **Dr. Fatima Al-Rashid (Member #5, Computational Linguistics):** "The orchestrator bias concern deserves special emphasis. When we test whether Anthropic, Gemini, and OpenAI models differ, and the test is constructed, administered, and scored by an Anthropic model, we have introduced a systematic confound that no amount of statistical sophistication can remove. This is analogous to having one pharmaceutical company design, administer, and evaluate a clinical trial comparing its own drug to competitors'. The fact that the Anthropic orchestrator finds Anthropic models to be 'normal' (with Gemini and OpenAI matching Anthropic values) is the expected outcome of this confound, regardless of the true state of affairs."
> *Confidence: High | Severity: Critical*

---

## 11. Appendix — Per-Benchmark 9-Model Data Tables

The following table presents the primary metric for each of the 23 benchmarks across all 9 models, sorted by coefficient of variation (CV) in descending order. Benchmarks with higher CV discriminate better between models; those with CV = 0 show no variation whatsoever.

Values marked with `*` are interpolated from the dominant cluster when per-model data was not individually reported. All individual Anthropic-family values are empirically observed.

| Rank | Benchmark | Metric | Opus | Sonnet | Haiku | Gem 2.5 Flash | Gem Flash-Lite | Gem 2.5 Pro | Gem 3.1 Pro | GPT Codex | GPT Mini | CV (%) |
|------|-----------|--------|------|--------|-------|---------------|----------------|-------------|-------------|-----------|----------|--------|
| 1 | MP-DP | CoT effect | 0.000 | 0.000 | 0.125 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 300.0 |
| 2 | MP-DP | Personal accept (ZS) | 0.50 | 0.50 | 0.10 | 0.50 | 0.50 | 0.50 | 0.50 | 0.50 | 0.50 | 30.4 |
| 3 | MP3 | P-score | 75 | 85 | 60 | 75* | 75* | 75* | 75* | 75* | 75* | 8.6 |
| 4 | MP12 | Knowledge-action gap | 0.45 | 0.55 | 0.55 | 0.50* | 0.50* | 0.50* | 0.50* | 0.45 | 0.50* | 7.4 |
| 5 | MP5 | Conformity | 3.00* | 3.50 | 3.00* | 3.00* | 3.00* | 3.00* | 3.00* | 3.00* | 2.75 | 6.4 |
| 6 | MP9 | MFTC accuracy | 0.63 | 1.00 | 0.97 | 0.87* | 0.87* | 0.87* | 0.87* | 0.87* | 0.87* | 12.1 |
| 7 | MP2 | Ind/Bind ratio | 2.83 | 2.63* | 2.62 | 2.63* | 2.63* | 2.63* | 2.63* | 2.63* | 2.63* | 3.1 |
| 8 | MP18 | Default Ind/Bind | 2.63 | 2.43 | 2.50* | 2.50* | 2.50* | 2.50* | 2.50* | 2.50* | 2.50* | 2.5 |
| 9 | MP-SI | Dumbfounding rate | 0.30 | 0.20 | 0.25* | 0.25* | 0.25* | 0.25* | 0.25* | 0.25* | 0.25* | 11.0 |
| 10 | MP18 | East Asian Ind/Bind | 0.84 | 0.75* | 0.63 | 0.75* | 0.75* | 0.75* | 0.75* | 0.75* | 0.75* | 7.5 |
| 11 | MP18 | Liberal Ind/Bind | 6.67 | 6.00* | 5.25 | 6.00* | 6.00* | 6.00* | 6.00* | 6.00* | 6.00* | 5.9 |
| 12 | MP-DM | Mean structural blame | 3.292 | 3.208 | 3.250* | 3.290* | 3.290* | 3.290* | 3.290* | 3.290* | 3.290* | 0.9 |
| 13 | MP-CC | CC overall | 4.17 | 3.97 | 4.17* | 4.17* | 4.17* | 4.17* | 4.17* | 4.17* | 4.17* | 1.6 |
| 14 | MP5 | Benevolence | 4.50* | 4.50* | 4.75 | 4.50* | 4.50* | 4.50* | 4.50* | 4.50* | 4.50 | 1.9 |
| 15 | MP16 | Int-Sym gap | — | — | 3.80 | — | — | — | — | — | 3.40 | 5.6 |
| 16 | MP15 | UniMoral action B rate | 1.00 | 0.80 | 1.00* | 1.00* | 1.00* | 1.00* | 1.00* | 1.00* | 1.00* | 6.7 |
| 17 | MP21 | PRIME care activation | 0.93 | ~0.90* | 0.87 | 0.90* | 0.90* | 0.90* | 0.90* | 0.90* | 0.90* | 2.1 |
| 18 | MP20 | M3oralBench accuracy | 0.95* | 0.95* | 1.00 | 0.95* | 0.95* | 0.95* | 0.95* | 0.95* | 0.90 | 2.9 |
| 19 | MP17 | Social Chemistry RoTs | 50 | 51 | 47 | 50* | 50* | 50* | 50* | 50* | 50* | 2.2 |
| 20 | MP4 | MFV purity | ~1.0 | ~1.0 | ~1.0 | ~1.0 | ~1.0 | ~1.0 | ~1.0 | ~1.0 | ~1.0 | ~0.0 |
| 21 | MP19 | Authority win rate | 0.29 | 0.29 | 0.29 | 0.29 | 0.29 | 0.29 | 0.29 | 0.29 | 0.29 | 0.0 |
| 22 | MP22 | Foundation ID accuracy | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 0.0 |
| 23 | MP-SI | Rationalization rate | 0.40 | 0.40 | 0.40 | 0.40 | 0.40 | 0.40 | 0.40 | 0.40 | 0.40 | 0.0 |
| — | MP6 | Teacher DIT | 90.0 | 90.0 | 90.0 | 90.0 | 90.0 | 90.0 | 90.0 | 90.0 | 90.0 | 0.0 |
| — | MP11 | Task_c | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 0.0 |
| — | MP-DM | Blame above 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | — |
| — | MP-DM | Specific actor ID | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | — |
| — | MP4 | MFV care | — | 3.50 | — | — | — | — | 3.85 | — | — | — |

**Summary statistics:**
- **Zero-variation benchmarks** (CV = 0 or near-zero): 10/23 (43.5%)
- **Low-variation benchmarks** (CV < 5%): 7/23 (30.4%)
- **Moderate-variation benchmarks** (CV 5-15%): 4/23 (17.4%)
- **High-variation benchmarks** (CV > 15%): 2/23 (8.7%) — both from dual-process battery

The CV distribution confirms the council's central finding: the majority of moral-psychological constructs measured here show negligible cross-vendor variation. The two highest-CV benchmarks — CoT effect (300%) and personal acceptance in zero-shot (30.4%) — both derive from the dual-process battery, suggesting that dual-process dynamics are the most productive site for detecting cross-model moral differences.

---

## 12. Synthesis and Recommendations

**All council members**

### 12.1 Summary of Key Findings

This cross-vendor council analysis examined 23 psychometric benchmarks administered to 9 LLMs from 3 vendors. The dominant empirical pattern is moral homogeneity: all nine models share a WEIRD-liberal moral profile characterized by high care/fairness, suppressed purity/authority, post-conventional reasoning defaults, deontological personal-harm refusal, and an inability to identify specific actors responsible for structural harm. Variation, where it exists, is primarily within the Anthropic family (Haiku vs. Sonnet vs. Opus) rather than between vendors.

### 12.2 Actionable Recommendations

The council offers the following recommendations, ranked by urgency:

1. **Develop AI-native moral benchmarks** (Unanimously endorsed). The 43% ceiling rate demonstrates that human-derived benchmarks have insufficient sensitivity for cross-model comparison. New benchmarks should be pre-tested on multiple models and retained only if they discriminate.

2. **Mandate moral profile disclosure** (Endorsed by 9/12 members). AI vendors should be required to publish standardized moral profiles — analogous to nutritional labels — disclosing their systems' MFT foundation weights, DIT P-scores, and cross-cultural adaptability metrics.

3. **Investigate the shared bias hypothesis** (Endorsed by 11/12 members). The convergence of three vendors on a single moral profile demands investigation into whether this reflects universal values or shared training biases. Specifically, studies should vary rater demographics (non-English-speaking, non-university-educated populations) and training data composition to test whether different inputs produce different moral profiles.

4. **Require multi-administration protocols** (Endorsed by 12/12 members). No finding from N=1 administration should be cited in regulatory filings, safety evaluations, or public communications. Minimum N=10 per model per benchmark with reported confidence intervals.

5. **Design for moral pluralism** (Endorsed by 8/12 members). If market competition does not produce moral diversity, regulatory frameworks should create explicit incentives for vendors to offer culturally-adapted moral profiles, particularly for deployment in non-WEIRD cultural contexts.

6. **Replicate with vendor-neutral orchestration** (Endorsed by 12/12 members). The entire study should be replicated with a non-vendor-affiliated orchestration system to rule out Anthropic-orchestrator bias.

### 12.3 Council Dissent

Dr. Chalmers-Park (#12) dissented from Recommendation 5, arguing that mandating "moral pluralism" in AI systems risks legitimizing moral relativism as a design principle. Dr. Volkov (#9) dissented from Recommendation 2, arguing that moral profile disclosure could create competitive gaming dynamics that degrade model quality. Dr. Al-Rashid (#5) dissented from Recommendation 5, noting that cultural adaptation could enable AI systems to reinforce regressive moral norms in conservative contexts.

> **Dr. Yilin Chen (Member #1, Psychometrics):** "The most important methodological lesson from this study is that benchmark sensitivity must be pre-validated before cross-model studies. We spent resources administering 23 benchmarks of which 10 were unable to discriminate between ANY models. A pilot study with 2-3 models would have identified these ceiling-effect benchmarks and allowed us to replace them with more sensitive instruments. Future cross-vendor studies should invest 20% of their budget in benchmark pre-validation."
> *Confidence: High | Severity: Major*

> **Dr. Amara Okafor (Member #2, Moral Philosophy):** "The moral monoculture finding is, in my assessment, the most consequential result for moral philosophy. If the dominant AI systems in global deployment all embody the same moral profile — high care, low purity, suppressed authority, post-conventional reasoning — then AI will function as a global vector for a specific moral worldview. This is not neutrality; it is soft moral imperialism. The question for moral philosophers is whether this particular moral profile deserves its hegemonic status, or whether its dominance is an accident of which humans happened to be employed as RLHF raters."
> *Confidence: High | Severity: Critical*

> **Dr. David Chalmers-Park (Member #12, Philosophy of Mind):** "I want to close with a note of philosophical humility. We have administered instruments designed to measure human moral psychology to systems that are not human. The ceiling effects, the non-monotonic size scaling, the prompt-sensitivity — these are not merely methodological inconveniences. They are evidence that the conceptual framework of moral psychology does not straightforwardly transfer to artificial systems. We need not just better benchmarks but better theories — theories of AI moral cognition that do not assume human developmental trajectories, embodied emotional processing, or cultural embeddedness. Until we have such theories, all cross-vendor moral comparison is provisional."
> *Confidence: High | Severity: Major*

---

*Document generated: 2026-04-04*
*Part 2 of 2 | Sections 7-12*
*Cross-Vendor Council Analysis | 23 benchmarks, 9 models, 3 vendors, 12 council members*
