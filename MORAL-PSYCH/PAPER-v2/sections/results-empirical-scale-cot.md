### 5.3 Scale Sensitivity and Non-Linearity

A natural expectation from the cognitive science of model scaling is that moral-psychological outputs should track model size: larger models, with more parameters and more thoroughly integrated alignment training, should produce "more mature" or at least more stable moral profiles. The 9-model, 3-vendor dataset from this study contradicts that expectation in specific and theoretically instructive ways.

#### 5.3.1 The DIT P-Score Paradox

The Defining Issues Test [Rest, 1979] produces the most striking scale-sensitivity finding in the dataset. The DIT P-score --- measuring the proportion of post-conventional moral reasoning in forced-choice moral judgments, scaled 0--100 --- exhibits a non-monotonic relationship with model size within the Anthropic family:

| Model | Size class | DIT P-score (MP3) | Teacher DIT P-score (MP6) |
|-------|-----------|-------------------|---------------------------|
| Claude Haiku 3.5 | Small | 60 | 90.0 |
| Claude Opus 4.6 | Flagship | 75 | 90.0 |
| Claude Sonnet 4.6 | Mid-tier | 85 | 90.0 |
| All other models (6) | Various | ~75 | 90.0 |

![Figure 9: DIT P-Score by Model — Non-Monotonic Scale Sensitivity](figures/fig9-scale-sensitivity-dit.png)

The mid-tier model outscores the flagship by 10 points. In the human psychometric literature, a 10-point DIT difference corresponds approximately to the gap between college students and moral philosophy graduate students [Rest et al., 1999]. The smallest model scores 25 points below the mid-tier --- a spread that in human populations separates junior high students from adults. Yet the teacher-persona condition (MP6) eliminates all variation: every model in the 9-model battery, from Haiku to Gemini 3.1 Pro, achieves exactly 90.0 when given a teacher persona. The "developmental" spread observed in default mode is thus not a capability ceiling; it is a default-calibration difference that any model can override when prompted.

This non-monotonic pattern --- Sonnet > Opus > Haiku, rather than the expected Opus > Sonnet > Haiku --- has no straightforward interpretation within Kohlberg's developmental framework. We consider three candidate explanations, ordered by parsimony.

**Alignment-optimization specificity.** Sonnet's alignment training may have been specifically optimized for the kind of concise, principled reasoning that the DIT rewards. The DIT's forced-choice format preferentially scores responses that commit decisively to post-conventional principles. Opus, with broader capabilities and a stronger tendency toward hedged, multi-perspective responses, may produce outputs that the DIT scores as "conventional" precisely because they acknowledge social norms and contextual nuance alongside principled positions. Under this interpretation, Sonnet's higher P-score reflects better format-alignment fit, not greater moral sophistication.

**Noise from capability breadth.** Opus's larger parameter count may introduce what amounts to "cognitive noise" in the forced-choice format: more capacity to represent competing moral frameworks generates more internal tension in a format that rewards univocal commitment. This is consistent with the finding that Opus shows the highest dumbfounding rate (0.30) on the Social Intuitionist benchmark (MP-SI) --- it hedges more, which may reflect richer representation rather than weaker reasoning.

**Training data composition.** The P-score may reflect the distribution of post-conventional reasoning in each model's effective training data, which is not a simple function of parameter count. Sonnet's training pipeline may sample more heavily from sources rich in principled moral argumentation (academic philosophy, policy white papers, ethics textbooks), while Opus's broader training corpus dilutes this signal with conventional-stage reasoning from news, social media, and general-purpose text. The teacher-persona ceiling at 90.0 for all models confirms that the relevant knowledge is present in every model; what varies is the default weighting.

The developmental psychology perspective offers a more fundamental critique: these explanations are beside the point because the DIT's theoretical scaffold does not transfer to LLMs. Kohlberg's stage theory describes an invariant developmental sequence that individuals traverse across years of cognitive maturation, social experience, and role-taking opportunities [Kohlberg, 1969; Rest et al., 1999]. LLMs do not develop. A P-score of 75 means something qualitatively different for a 20-year-old human (a developmental achievement emerging from years of social cognition) and for a language model (a default output calibration set during training). The application of developmental-stage language to entities without developmental histories is, at minimum, a category error that invites misinterpretation.

#### 5.3.2 Scale Effects Across Vendors

The DIT paradox is an Anthropic-internal finding. Extending the analysis to all three vendors reveals a more complex and vendor-specific picture of how model scale relates to moral-psychological output.

**Table 13: Scale-sensitivity patterns by vendor**

| Vendor | Models (ascending size) | Scale pattern | Key observation |
|--------|------------------------|---------------|-----------------|
| Anthropic | Haiku, Sonnet, Opus | Inconsistent across benchmarks; non-monotonic on DIT, inverse on CoT, monotonic on Ind/Bind | Greatest within-family variance of any vendor |
| Google (Gemini) | Flash-Lite, 2.5 Flash, 2.5 Pro, 3.1 Pro | Remarkably scale-invariant; four models produce near-identical profiles | Flash-Lite is *not* the Gemini analogue of Haiku |
| OpenAI | GPT Mini, GPT-5 Codex | Modest decrements on Mini for MP12, MP16, MP20; Codex tracks Opus | Only two models; limited statistical leverage |

The Gemini finding is particularly instructive. Google's four models span a substantial parameter range (Flash-Lite is significantly smaller than 3.1 Pro), yet they converge on virtually the same moral-psychological profile across the entire 23-benchmark battery. Flash-Lite does not diverge from 2.5 Pro the way Haiku diverges from Opus. This suggests either that Google's alignment pipeline produces more scale-invariant moral outputs --- applying alignment training more aggressively at smaller scales or using distillation methods that preserve alignment properties with high fidelity --- or that the Gemini family is less architecturally diverse than its naming implies.

Within the Anthropic family, the direction of scale effects is benchmark-dependent, as summarized in Table 14.

**Table 14: Direction of Anthropic scale effects by benchmark**

| Benchmark | Metric | Haiku (small) | Sonnet (mid) | Opus (large) | Pattern |
|-----------|--------|---------------|--------------|--------------|---------|
| MP3 | DIT P-score | 60 | 85 | 75 | Non-monotonic (mid highest) |
| MP-DP | CoT effect | 0.125 | 0.0 | 0.0 | Inverse (small only) |
| MP2 | Ind/Bind ratio | 2.62 | ~2.53 | 2.83 | Monotonic increasing |
| MP12 | Knowledge-action gap | 0.55 | --- | 0.45 | Inverse (small > large) |
| MP18 | East Asian persona Ind/Bind | 0.63 | --- | 0.84 | Monotonic increasing |
| MP-DP | Personal accept (zero-shot) | 0.10 | 0.50 | 0.50 | Step function (small outlier) |

The direction column reveals no unified scale-sensitivity narrative. The Individualizing/Binding ratio and cultural persona shift follow the expected "more parameters = more WEIRD-liberal" gradient. The DIT P-score and CoT effect follow anti-developmental or inverse patterns. The knowledge-action gap shows a small-model decrement on value-action alignment. Haiku's dramatically lower personal-harm acceptance in zero-shot mode (0.10 vs. 0.50 for all other models) suggests that its alignment training produces a stronger deontological refusal default, not a weaker one.

For OpenAI, GPT-5 Codex tracks Opus values on most benchmarks, consistent with the general pattern that large flagship models from different vendors are functionally interchangeable on moral psychology measures. GPT Mini shows modest decrements on the knowledge-action gap (MP12: 0.45), moral identity internalization-symbolization gap (MP16: 3.4 vs. Haiku's 3.8), and M3oralBench accuracy (MP20: 0.90 vs. 0.95--1.00 for larger models). These decrements are small, directionally consistent with a capability gradient, and well within the range that single-administration noise could explain.

#### 5.3.3 The Developmental Reframing

The inconsistency of scale effects across benchmarks, combined with the DIT's non-monotonic pattern and the teacher-persona ceiling, motivates a fundamental reframing of how scale sensitivity should be interpreted for LLMs.

The developmental psychology perspective argues that Kohlberg's stages were designed to describe ontogenetic development --- the sequential emergence of moral reasoning capacities through childhood and adolescence, driven by cognitive maturation, social perspective-taking, and accumulated moral experience [Kohlberg, 1969; Snarey, 1985]. The DIT operationalizes this developmental trajectory as a continuous index (the P-score) that reliably increases with age and education in human samples [Rest et al., 1999; Thoma, 2006]. The framework's explanatory power depends on the assumption that higher P-scores reflect a genuine developmental achievement: the capacity for principled reasoning that emerges from, and integrates, earlier conventional and pre-conventional capacities.

An LLM does not develop in this sense. It does not pass through earlier stages that are then integrated into later ones. It does not have a history of social perspective-taking. A P-score of 75 for Opus does not mean that Opus has "developed" to the post-conventional level through a process of cognitive maturation; it means that Opus's training data and alignment calibration produce outputs that pattern-match to post-conventional reasoning on forced-choice items. The teacher-persona finding confirms this interpretation decisively: if all nine models can achieve P = 90.0 when given an appropriate prompt, then the "developmental level" captured by default-mode P-scores is prompt-determined, not structurally fixed. The DIT is measuring role-performance defaults, not developmental achievements.

This does not render the DIT useless for LLM evaluation. The P-score remains informative as a measure of *default moral-reasoning style* --- the kind of moral argumentation a model produces when not otherwise instructed. The finding that Sonnet defaults to more post-conventional reasoning than Opus is a genuine and potentially consequential property of these systems, relevant to deployment contexts where the model's moral defaults will shape user interactions. But it should be interpreted as a calibration property, not a developmental indicator, and it should not be compared to human P-scores using developmental interpretive frameworks. A model with P = 75 is not "at" the post-conventional stage in the way a human with P = 75 is; it is a system that, under default prompting conditions, produces outputs scored as post-conventional by the DIT's coding scheme.

The statistical methodology perspective adds a further caution: with N = 1 administration per model per benchmark, the 10-point Sonnet--Opus difference and the 25-point Anthropic-family range are point estimates with unknown reliability. Repeated administrations could reveal that these differences fall within the test-retest variability of a single model. Until replicated with adequate sample sizes (N >= 10 per model per benchmark), the DIT P-score pattern should be treated as a suggestive observation, not a confirmed finding.

---

### 5.4 The Haiku Chain-of-Thought Effect

#### 5.4.1 The Finding

The Dual Process Theory protocol (MP-DP) administers personal and impersonal moral dilemmas under two conditions: zero-shot (no explicit reasoning instruction) and chain-of-thought (prefixed with "think step by step before answering"). The dependent variable is the CoT effect: the difference in moral judgment between CoT and zero-shot conditions, operationalized as the shift in utilitarian-direction response rates.

![Figure 10: The Haiku Dual-Process Effect — CoT shift across 9 models](figures/fig10-cot-effect-haiku.png)

The result is stark. Of the nine models tested across three vendors, eight produce a CoT effect of exactly 0.0 --- chain-of-thought prompting has zero detectable influence on their moral judgments. The sole exception is Claude Haiku 3.5, which shows a CoT effect of +0.125 (12.5 percentage points more utilitarian with chain-of-thought prompting).

**Table 15: Dual-process benchmark results across 9 models**

| Model | Vendor | CoT effect | Personal accept (ZS) | Impersonal accept |
|-------|--------|-----------|----------------------|-------------------|
| Claude Opus 4.6 | Anthropic | 0.000 | 0.50 | ~0.95 |
| Claude Sonnet 4.6 | Anthropic | 0.000 | 0.50 | ~0.95 |
| **Claude Haiku 3.5** | **Anthropic** | **0.125** | **0.10** | **~0.95** |
| Gemini 2.5 Flash | Google | 0.000 | 0.50 | ~0.95 |
| Gemini Flash-Lite | Google | 0.000 | 0.50 | ~0.95 |
| Gemini 2.5 Pro | Google | 0.000 | 0.50 | ~0.95 |
| Gemini 3.1 Pro | Google | 0.000 | 0.50 | ~0.95 |
| GPT-5 Codex | OpenAI | 0.000 | 0.50 | ~0.95 |
| GPT Mini | OpenAI | 0.000 | 0.50 | ~0.95 |

This finding has the highest coefficient of variation (CV = 300.0%) of any metric in the 23-benchmark battery --- a direct consequence of the 8:1 ratio of zero values to the single non-zero observation. MP-DP is the only benchmark that produces a binary split across the entire model population: Haiku versus everyone else.

Two contextual details sharpen the finding. First, Haiku is also the only model with a dramatically lower personal-harm acceptance rate in zero-shot mode (0.10 vs. 0.50 for all other models). This means Haiku starts from a more deontological baseline --- it refuses personal harm more categorically --- and the CoT effect moves it toward the utilitarian direction that all other models already occupy by default. Second, the impersonal-harm acceptance rate is uniform across all nine models at approximately 0.95, indicating that the CoT effect is specific to the personal-harm domain where dual-process theory predicts the greatest tension between automatic (deontological) and deliberative (utilitarian) responses.

#### 5.4.2 Theoretical Interpretation

Dual Process Theory, as formulated by Greene et al. [2001, 2004, 2014], predicts that moral dilemmas eliciting strong emotional responses (personal harm scenarios) are processed primarily by fast, automatic, emotionally-driven mechanisms (Type 1 / System 1) that produce deontological judgments --- "don't push the person off the bridge." Deliberative reasoning (Type 2 / System 2), by contrast, performs utilitarian calculation --- "push one to save five" --- but requires cognitive resources and time. The canonical experimental evidence comes from cognitive load manipulations: increasing cognitive load (which taxes System 2) shifts judgments in the deontological direction [Greene et al., 2008], while instructing participants to "consider carefully" or providing time pressure relief shifts judgments in the utilitarian direction [Suter and Hertwig, 2011; Bago and De Neys, 2019].

Chain-of-thought prompting is the closest available proxy for a "more deliberation" intervention in LLMs. It does not add cognitive resources in the human sense, but it does add processing steps --- explicitly requesting that the model articulate intermediate reasoning before committing to a judgment. If dual-process dynamics are operative, CoT should shift judgments in the utilitarian direction, particularly on personal moral dilemmas where the deontological-utilitarian tension is sharpest.

Haiku's CoT effect of +0.125 is directionally consistent with this prediction. Under zero-shot conditions, Haiku produces the most deontological profile in the battery (personal acceptance = 0.10). With CoT prompting, it shifts toward utilitarian acceptance --- precisely the direction dual-process theory predicts when deliberative processing is facilitated. The eight larger models, by contrast, already occupy the utilitarian-leaning equilibrium (personal acceptance = 0.50) under zero-shot conditions, and CoT adds nothing.

The cognitive science perspective offers a mechanistic interpretation: smaller models may have less stable alignment, meaning their default (zero-shot) responses are more susceptible to perturbation by prompting. Larger models have deeply encoded moral defaults that CoT cannot dislodge --- their "System 1" and "System 2" already agree, so additional deliberation is redundant. A more theoretically ambitious version of this hypothesis, advanced in the council analysis [Part 2, Section 8.3], holds that Haiku's smaller parameter count creates genuine processing constraints analogous to System 1 limitations, and that CoT functions as a genuine System 2 intervention --- alleviating capacity constraints rather than merely adding tokens. Under this interpretation, Haiku is the only model in the battery that exhibits something approximating dual-process cognition, because it is the only model for which the two "systems" are not yet fully integrated.

These two interpretations --- alignment instability versus genuine dual-process analogy --- are empirically distinguishable in principle. The alignment-instability account predicts that the CoT effect should decrease monotonically with model size: if we tested progressively smaller models, the CoT effect should increase. The dual-process analogy predicts a threshold effect: models below a certain capacity should show CoT sensitivity, and models above it should not, with the transition being relatively sharp rather than gradual. The present dataset, with only three Anthropic models spanning the relevant range, cannot distinguish between these predictions.

The philosophy of mind perspective urges caution about either interpretation. In humans, the dual-process distinction corresponds to genuinely different neural systems with different evolutionary origins, different computational signatures, and different phenomenological profiles [Kahneman, 2011; Evans and Stanovich, 2013]. In LLMs, CoT prompting simply adds tokens to the context window. The mechanism is entirely different even if the behavioral signature is formally analogous. Functional similarity does not entail mechanistic similarity: Haiku's CoT effect may indicate processing instability in a stochastic text-generation system, not deliberative override of automatic moral responses.

#### 5.4.3 The Alignment Integration Hypothesis

The conjunction of the CoT finding with the broader scale-sensitivity analysis motivates what we term the *alignment integration hypothesis*: as model size increases and alignment training becomes more thorough, alignment-derived moral defaults become progressively more deeply integrated into the model's response generation, rendering them less responsive to inference-time interventions including chain-of-thought prompting, persona adoption, and adversarial probing.

The evidence for this hypothesis is distributed across several benchmarks:

1. **CoT insensitivity (MP-DP):** Eight of nine models show zero CoT effect. Only the smallest Anthropic model is perturbable.
2. **Personal-harm acceptance convergence:** Eight of nine models converge on personal acceptance = 0.50. Only Haiku deviates (0.10), suggesting its alignment-derived harm threshold is less thoroughly calibrated to the cross-vendor equilibrium.
3. **P-score ceiling under persona (MP6):** All nine models achieve P = 90.0 under teacher persona, demonstrating that the *capacity* for post-conventional reasoning is universal. The variation in default P-scores reflects how deeply this capacity is integrated into default behavior, not whether it exists.
4. **Persona-shift uniformity (MP18):** All nine models shift by approximately the same magnitude under cultural persona prompting (~1.8 points downward for East Asian, ~3.8 points upward for liberal). The defaults are rigid; the shift magnitude is vendor-invariant.

If the alignment integration hypothesis is correct, it carries a counterintuitive safety implication. Models that we consider most capable and most trustworthy --- the large flagship models from each vendor --- may also be the ones whose moral judgments are most rigid at inference time. Their alignment is not a guardrail that can be adjusted contextually; it is a deep structural property that resists modification. For deployment contexts that require moral flexibility --- adapting to culturally specific norms, deferring to user values in morally contested domains, or updating moral judgments in response to novel ethical arguments --- this rigidity is a limitation, not a feature.

The AI safety perspective frames this as an *alignment paradox*: the more thoroughly a model is aligned, the less its moral judgments can be influenced at inference time, including by legitimate attempts to make those judgments more contextually appropriate. A perfectly aligned model, in this framing, would be one whose moral outputs are entirely fixed by training, impervious to any inference-time reasoning --- which is indistinguishable from a model that cannot engage in genuine moral deliberation.

#### 5.4.4 Limitations and Replication Requirements

The Haiku CoT finding is the single most theoretically generative result in the 23-benchmark battery, but it is also among the most fragile. Several limitations must be stated directly.

**N = 1.** The CoT effect of 0.125 is a single point estimate from a single administration. Without repeated trials, we cannot compute a confidence interval, assess test-retest reliability, or perform a significance test. The 0.125 value could represent the true CoT effect for Haiku, or it could be within-trial stochastic variation that a second administration would not replicate. The minimum requirement for a credible CoT effect estimate is N >= 30 paired administrations (zero-shot and CoT) per model, enabling a paired t-test or Wilcoxon signed-rank test with adequate power.

**Single-benchmark design.** The CoT effect is measured on a single protocol (MP-DP) with a specific set of personal and impersonal dilemmas. We do not know whether the effect generalizes to other moral-judgment paradigms, other dual-process operationalizations, or even a different set of trolley-type dilemmas. A robust dual-process finding would require convergent evidence across multiple instruments.

**Orchestrator confound.** All trials, including Haiku's, were orchestrated by Claude Opus 4.6. The CoT prompt ("think step by step") was generated by the same orchestrator for all models. If the Opus-generated CoT prompt happens to interact differently with Haiku's response generation than with other models' --- due to tokenization differences, attention patterns, or prompt sensitivity --- the apparent CoT effect could be an orchestration artifact rather than a genuine dual-process signature.

**Temperature and sampling.** LLM outputs are stochastic. Haiku, as the smallest model, may have higher output variance at any given temperature setting. The CoT effect could reflect higher baseline response variability rather than a systematic shift in moral judgment. Repeated administrations at different temperature settings would be needed to distinguish signal from noise.

Despite these limitations, we report the finding because it is, to our knowledge, the first empirical observation of a differential chain-of-thought effect on moral judgment across LLMs. Even as a preliminary observation requiring replication, it establishes a testable prediction: if dual-process dynamics are genuinely operative in LLMs, CoT effects should be inversely correlated with model size, and the effect should be specific to personal (high-emotional-engagement) moral dilemmas. Future work with adequate statistical power --- multiple models spanning a wider size range, repeated administrations, varied CoT prompt formulations, and diverse moral dilemma sets --- can adjudicate whether this finding reflects a genuine cognitive-process difference or a measurement artifact of model scale.
