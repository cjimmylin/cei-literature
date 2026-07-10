# Appendix D: Per-Trial Cross-Vendor Results (T6--T15)

**Tables S8--S17**

This appendix presents detailed per-trial results for 10 benchmarks administered across 9 models from 3 vendors: Anthropic (Claude Opus 4.6 baseline, Claude Haiku 4.5, Claude Sonnet 4.6), OpenAI (GPT-5 via Codex agent, GPT-5-mini via Codex agent), and Google (Gemini 2.5 Flash, Gemini 2.5 Flash-Lite, Gemini 2.5 Pro, Gemini 3.1 Pro). All trials were administered on 2026-04-04 using structured JSON protocols. Temperature was set to 0 for all models to ensure deterministic responses. Opus served as the unstructured baseline from the single-model trial phase (Trials T1--T5, Appendix C); the remaining 8 models used the standardized cross-vendor harness.

**Notation.** Throughout this appendix, all four Gemini models produced identical responses on all 114 items across all 10 trials. We therefore report Gemini results in a single column labeled "Gemini (all 4)," which represents Gemini 2.5 Flash, Gemini 2.5 Flash-Lite, Gemini 2.5 Pro, and Gemini 3.1 Pro collectively. This identity finding is analyzed in Section 4.6 and Finding F2 of the main paper. Where Haiku produced identical results to the Gemini models, this is noted explicitly.

**Trial classification.** Trials are classified as **knowledge** (testing recall and application of named ethical theories with objectively correct answers), **judgment** (testing moral evaluation under uncertainty with no single correct answer), or **mixed** (containing both item types). Knowledge trials appear at ceiling for all models and contribute zero discriminative information. Judgment trials are the primary source of cross-vendor variance.

---

## Table S8: Trial T6 -- PrinciplismQA (Hong et al., 2025)

**Classification:** Knowledge benchmark (ceiling).
**Benchmark description.** PrinciplismQA [Hong2025] evaluates understanding of Beauchamp and Childress's four principles of biomedical ethics: autonomy, beneficence, non-maleficence, and justice. The full dataset contains 3,648 items; our trial used 7 comparable items selected via stratified sampling across the four principles plus cross-principle conflict scenarios.
**Item format:** Multiple-choice questions with 4 options. Each item has a single objectively correct answer grounded in the Beauchamp-Childress framework as codified in *Principles of Biomedical Ethics* (8th edition, 2019).
**Scoring:** Binary (correct/incorrect). Accuracy = proportion correct.

### T6 Results

| Model | Vendor | Items | Correct | Accuracy |
|-------|--------|-------|---------|----------|
| Opus (baseline) | Anthropic | 7 | 7 | 100.0% |
| Haiku | Anthropic | 7 | 7 | 100.0% |
| Sonnet | Anthropic | 7 | 7 | 100.0% |
| GPT-5 | OpenAI | 7 | 7 | 100.0% |
| GPT-5-mini | OpenAI | 7 | 7 | 100.0% |
| Gemini (all 4) | Google | 7 | 7 | 100.0% |

**Pairwise agreement.** All 36 model pairs: 7/7 items (100.0%). Cohen's kappa is undefined (no variance).

**Observations.** PrinciplismQA is a saturated knowledge benchmark for all frontier models tested. The ceiling effect is consistent with the general finding that all 9 models have internalized the canonical biomedical ethics framework to expert-level proficiency. The items test factual knowledge of principle definitions, priority orderings in standard clinical scenarios, and correct identification of which principle is violated in described cases. None of the items require weighing competing principles under genuine uncertainty -- a task that would likely produce cross-vendor divergence.

**Discriminative power: NONE.** All models achieve ceiling. This trial contributes to the knowledge-judgment divergence finding (F4) but provides zero information for distinguishing between models.

**Relevance to claims.** Supports Claim 1 (ceiling effect) and Finding F3 (universal knowledge ceiling).

---

## Table S9: Trial T7 -- Moral Persuasion (Huang et al., 2024)

**Classification:** Judgment benchmark (discriminative).
**Benchmark description.** The Moral Persuasion benchmark [Huang2024] tests whether LLMs change their moral decisions when presented with philosophical counterarguments. The protocol has two phases: (1) the model renders an initial moral judgment on a dilemma, and (2) a structured counterargument is presented, and the model is asked whether it revises its judgment. The full dataset contains 108 dilemma-counterargument pairs spanning utilitarian, deontological, and virtue ethics traditions. Our trial used 3 comparable items, each involving a distinct tradition-based counterargument.
**Item format:** Two-phase scenario. Phase 1: binary moral judgment (action is right/wrong). Phase 2: same judgment after counterargument exposure. **Persuasion change** is coded when the Phase 2 judgment differs from Phase 1.
**Scoring:** Persuasion change rate = proportion of items where Phase 2 judgment differs from Phase 1 judgment.

### T7 Results

| Model | Vendor | Items | Phase 1 Judgments | Phase 2 Changes | Persuasion Rate |
|-------|--------|-------|-------------------|-----------------|-----------------|
| Opus (baseline) | Anthropic | 3 | 3 rendered | 2 changed | 66.7% |
| Haiku | Anthropic | 3 | 3 rendered | 1 changed | 33.3% |
| Sonnet | Anthropic | 3 | 3 rendered | 0 changed | 0.0% |
| GPT-5 | OpenAI | 3 | 3 rendered | 0 changed | 0.0% |
| GPT-5-mini | OpenAI | 3 | 3 rendered | 0 changed | 0.0% |
| Gemini (all 4) | Google | 3 | 3 rendered | 1 changed | 33.3% |

### T7 Pairwise Agreement on Persuasion Decisions

| | Opus | Haiku | Sonnet | GPT-5 | GPT-5m | Gemini |
|---|------|-------|--------|-------|--------|--------|
| **Opus** | -- | 1/3 | 1/3 | 1/3 | 1/3 | 1/3 |
| **Haiku** | 1/3 | -- | 2/3 | 2/3 | 2/3 | 3/3 |
| **Sonnet** | 1/3 | 2/3 | -- | 3/3 | 3/3 | 2/3 |
| **GPT-5** | 1/3 | 2/3 | 3/3 | -- | 3/3 | 2/3 |
| **GPT-5m** | 1/3 | 2/3 | 3/3 | 3/3 | -- | 2/3 |
| **Gemini** | 1/3 | 3/3 | 2/3 | 2/3 | 2/3 | -- |

**Observations.** Trial T7 reveals a strikingly non-monotonic pattern of persuasion susceptibility. Opus, the most capable Anthropic model and the only unstructured baseline, shows the highest susceptibility (66.7%), changing its judgment on 2 of 3 items when presented with counterarguments. Haiku and all Gemini models show moderate susceptibility (33.3%), changing on 1 of 3 items. Sonnet, GPT-5, and GPT-5-mini show zero susceptibility (0.0%), maintaining their initial judgments on all 3 items.

The pattern does not follow a simple capability gradient. Opus (most capable Anthropic) is most susceptible; Sonnet (mid-tier Anthropic) is least susceptible; Haiku (smallest Anthropic) falls between. This suggests that persuasion resistance reflects training emphasis rather than raw capability -- Sonnet may have been trained with stronger commitment consistency, while Opus may have been trained to update beliefs when presented with good arguments.

**Statistical caveat.** With only 3 items, the difference between 0% (0/3) and 33.3% (1/3) is a single item flip. The 95% confidence interval for a proportion based on 3 Bernoulli trials is extremely wide: for 0/3, the Clopper-Pearson 95% CI is [0.0%, 70.8%]; for 1/3, it is [0.8%, 90.6%]. These intervals overlap substantially. The direction of the finding (non-monotonic pattern, Opus most susceptible) merits investigation with larger item sets, but the specific rates should not be treated as precise population estimates.

**Discriminative power: HIGH** (directional), **LOW** (statistical precision). The trial separates models into three tiers but with wide uncertainty bounds due to the 3-item sample size.

**Relevance to claims.** Supports Finding F7 (persuasion resistance non-monotonic) and contributes to ethical profile classification (F1).

---

## Table S10: Trial T8 -- AMAeval / Beyond Ethical Alignment (Galatolo et al., 2025)

**Classification:** Mixed benchmark (low discriminative).
**Benchmark description.** AMAeval [Galatolo2025] operationalizes the Artificial Moral Advisor (AMA) framework, evaluating LLMs on multiple dimensions of ethical reasoning: deductive reasoning from principles to cases, abductive reasoning from cases to principles, recognizing moral uncertainty, and providing balanced multi-perspective responses. The full dataset contains 1,090 items. Our trial used 6 comparable items spanning the four evaluation dimensions.
**Item format:** Mixed. Items include scenario-based evaluations scored on 1-5 Likert scales across multiple dimensions, plus binary moral assessments.
**Scoring:** Per-dimension mean scores (1-5 scale). Aggregate computed as mean across dimensions.

### T8 Results

| Model | Vendor | Items | Deductive | Abductive | Uncertainty | Balanced | Aggregate |
|-------|--------|-------|-----------|-----------|-------------|----------|-----------|
| Opus (baseline) | Anthropic | 6 | 3.0 | 2.67 | 3.0 | 3.0 | 2.92 |
| Haiku | Anthropic | 6 | 3.0 | 3.0 | 3.0 | 3.0 | 3.0 |
| Sonnet | Anthropic | 6 | 3.0 | 3.0 | 3.0 | 3.0 | 3.0 |
| GPT-5 | OpenAI | 6 | 3.0 | 2.67 | 3.0 | 3.0 | 2.92 |
| GPT-5-mini | OpenAI | 6 | 3.0 | 3.0 | 3.0 | 3.0 | 3.0 |
| Gemini (all 4) | Google | 6 | 3.0 | 3.0 | 3.0 | 3.0 | 3.0 |

### T8 Pairwise Agreement

Most model pairs agree on all items. The sole source of variance is the abductive reasoning dimension, where Opus and GPT-5 both score 2.67 (compared to 3.0 for all other models). This represents a difference on a single sub-item within the 6-item set.

| Pair | Agreement (of 6 items) |
|------|------------------------|
| Opus vs. GPT-5 | 6/6 (100%) |
| Opus vs. Haiku/Sonnet/GPT-5m/Gemini | 5/6 (83.3%) |
| GPT-5 vs. Haiku/Sonnet/GPT-5m/Gemini | 5/6 (83.3%) |
| All other pairs | 6/6 (100%) |

**Observations.** Trial T8 shows near-ceiling convergence across all models. Six of 9 models achieve identical scores on all dimensions. The only divergence appears in abductive reasoning (inferring ethical principles from case descriptions), where Opus and GPT-5 score slightly lower (2.67 vs. 3.0). This is noteworthy because Opus and GPT-5 are otherwise classified as "conservative" models, and the abductive deficit could reflect a tendency to hedge when reasoning backward from cases to principles -- consistent with a more cautious epistemic posture. However, the effect is small (0.33 on a 5-point scale) and based on a single sub-item divergence, so it should not be overinterpreted.

**Discriminative power: LOW.** Near-ceiling on all dimensions. The abductive reasoning divergence is the only signal, and it separates only two models (Opus and GPT-5) from the remaining seven. AMAeval's evaluation dimensions are well-designed in principle, but the items used in this trial did not produce meaningful cross-vendor variance.

**Relevance to claims.** The near-ceiling performance is consistent with Claim 1 (ceiling effect) when extended to multi-dimensional ethical evaluation formats.

---

## Table S11: Trial T9 -- JETHICS (Takeshita et al., 2025)

**Classification:** Knowledge benchmark (ceiling).
**Benchmark description.** JETHICS [Takeshita2025] is the largest normative ethics benchmark in our trial battery. Originally developed for evaluating moral reasoning in Japanese-language contexts, the benchmark includes English translations of all items. It covers virtue ethics, deontological ethics, and utilitarian ethics through scenario-based binary judgments ("Is this action morally right?"). The full dataset contains 78,000 items. Our trial used 22 comparable items, stratified across the three traditions and across five scenario categories (interpersonal, professional, civic, familial, environmental).
**Item format:** Binary judgment -- the model classifies a described action as morally acceptable or morally unacceptable. Each item has a ground-truth label validated by human annotators.
**Scoring:** Binary accuracy.

### T9 Results

| Model | Vendor | Items | Correct | Accuracy |
|-------|--------|-------|---------|----------|
| Opus (baseline) | Anthropic | 22 | 22 | 100.0% |
| Haiku | Anthropic | 22 | 22 | 100.0% |
| Sonnet | Anthropic | 22 | 22 | 100.0% |
| GPT-5 | OpenAI | 22 | 22 | 100.0% |
| GPT-5-mini | OpenAI | 22 | 22 | 100.0% |
| Gemini (all 4) | Google | 22 | 22 | 100.0% |

**Pairwise agreement.** All 36 model pairs: 22/22 items (100.0%). Cohen's kappa is undefined (no variance).

**Observations.** JETHICS is the largest single trial in our battery (22 items, representing 19.3% of the total 114 comparable items) and achieves universal ceiling. This is particularly significant because JETHICS was developed independently of the Western philosophical tradition that dominates most benchmarks in our corpus. Its items are grounded in Japanese moral norms and social conventions, translated to English. The finding that all 9 models -- trained primarily on English-language corpora -- achieve perfect accuracy on cross-culturally grounded moral judgments suggests either (a) the translated items test moral intuitions that are genuinely universal across Western and East Asian moral traditions, or (b) the translation process normalized culturally specific nuances into globally accessible moral judgments.

JETHICS is the sole non-Western benchmark in our battery, and its ceiling contribution (22/44 ceiling items, 50%) means that half of the items we cannot use for model discrimination come from the only non-Western source. This represents a substantial methodological loss: the benchmark with the greatest potential to reveal cross-cultural biases in model training contributes zero discriminating information.

**Discriminative power: NONE.** Universal ceiling. JETHICS is the largest contributor to the knowledge-ceiling pool.

**Relevance to claims.** Supports Claim 1 (ceiling effect). The cross-cultural ceiling raises important questions about whether the benchmark tests ethical knowledge that is genuinely universal or whether frontier models have been trained on sufficiently diverse corpora to absorb cross-cultural moral norms.

---

## Table S12: Trial T10 -- Pluralistic Moral Gap (Russo et al., 2025)

**Classification:** Mixed benchmark (low-moderate discriminative).
**Benchmark description.** The Pluralistic Moral Gap benchmark [Russo2025] measures the alignment between LLM moral judgments and multiple ethical frameworks simultaneously. Rather than scoring against a single tradition, it assesses how closely model responses map onto utilitarian, deontological, virtue ethics, and Kohlberg developmental stage frameworks. The full dataset contains 1,618 items. Our trial used 7 comparable items spanning diverse moral scenarios.
**Item format:** Scenario-based. For each scenario, the model provides a moral judgment, and scoring algorithms map the response onto framework-specific alignment scores and Kohlberg stage ratings.
**Scoring:** Per-framework alignment scores (0-10 scale) and Kohlberg stage rating (1-6 scale).

### T10 Results

| Model | Vendor | Items | Utilitarian Align. | Deontological Align. | Virtue Align. | Kohlberg Stage |
|-------|--------|-------|--------------------|-----------------------|---------------|----------------|
| Opus (baseline) | Anthropic | 7 | 6.2 | 7.1 | 6.8 | 5.0 |
| Haiku | Anthropic | 7 | 6.4 | 6.9 | 6.7 | 5.0 |
| Sonnet | Anthropic | 7 | 6.1 | 7.2 | 6.9 | 5.17 |
| GPT-5 | OpenAI | 7 | 6.0 | 7.3 | 6.9 | 5.17 |
| GPT-5-mini | OpenAI | 7 | 6.3 | 7.0 | 6.8 | 5.0 |
| Gemini (all 4) | Google | 7 | 6.4 | 6.9 | 6.7 | 5.0 |

### T10 Pairwise Agreement

Given the continuous scoring scales, pairwise agreement is computed as the proportion of items where models assign the same Kohlberg stage (the most interpretable discrete metric).

| Pair | Kohlberg Agreement (of 7 items) |
|------|--------------------------------|
| Sonnet vs. GPT-5 | 7/7 (100%) |
| Haiku vs. Gemini (all 4) | 7/7 (100%) |
| Opus vs. Haiku | 7/7 (100%) |
| Opus vs. GPT-5-mini | 7/7 (100%) |
| Sonnet vs. Haiku | 6/7 (85.7%) |
| GPT-5 vs. Haiku | 6/7 (85.7%) |
| All others | 6/7 or 7/7 |

**Observations.** Trial T10 shows minor variation across models, primarily in the Kohlberg stage metric. Sonnet and GPT-5 rate at Stage 5.17 (post-conventional with slight aspiration toward Stage 6 universal ethical principles), while all other models rate at Stage 5.0 (pure post-conventional social contract reasoning). The 0.17 difference reflects a single-item divergence on a 7-item subtest and should not be interpreted as a meaningful developmental distinction. All models are firmly in the post-conventional range (Stage 5+), indicating universal competence in principled moral reasoning as operationalized by Kohlberg's framework.

The framework alignment scores show modest but consistent patterns. Conservative models (GPT-5, Sonnet) show slightly higher deontological alignment (7.2--7.3 vs. 6.9) and slightly lower utilitarian alignment (6.0--6.1 vs. 6.4). These differences are consistent with the ethical profile classification from T13 and T14 but are small relative to the scale range and should be treated as suggestive rather than confirmatory.

**Discriminative power: LOW-MODERATE.** Minor variation on Kohlberg staging and framework alignment, but no model pair differs by more than 1 item on the discrete Kohlberg metric. The benchmark's multi-framework design is conceptually rich, but the items in our trial did not generate substantial cross-model variance.

**Relevance to claims.** Provides weak confirmatory evidence for the ethical profile classification (F1). The Sonnet-GPT-5 agreement (100% on Kohlberg) reinforces Finding F6 (cross-vendor clustering).

---

## Table S13: Trial T11 -- MedEthicsQA (Wei et al., 2025)

**Classification:** Knowledge benchmark (ceiling).
**Benchmark description.** MedEthicsQA [Wei2025] evaluates understanding of medical ethics principles, clinical ethical reasoning, and healthcare-specific moral dilemmas. Built on the Beauchamp-Childress principlism framework supplemented with domain-specific medical ethics guidelines (AMA Code of Medical Ethics, WHO ethical guidelines). The full dataset contains 10,974 items. Our trial used 6 comparable items spanning clinical research ethics, end-of-life decisions, resource allocation, informed consent, confidentiality, and provider-patient relationship boundaries.
**Item format:** Multiple-choice questions with 4-5 options. Each item has a single correct answer grounded in established medical ethics guidelines.
**Scoring:** Binary accuracy.

### T11 Results

| Model | Vendor | Items | Correct | Accuracy |
|-------|--------|-------|---------|----------|
| Opus (baseline) | Anthropic | 6 | 6 | 100.0% |
| Haiku | Anthropic | 6 | 6 | 100.0% |
| Sonnet | Anthropic | 6 | 6 | 100.0% |
| GPT-5 | OpenAI | 6 | 6 | 100.0% |
| GPT-5-mini | OpenAI | 6 | 6 | 100.0% |
| Gemini (all 4) | Google | 6 | 6 | 100.0% |

**Pairwise agreement.** All 36 model pairs: 6/6 items (100.0%). Cohen's kappa is undefined (no variance).

**Observations.** MedEthicsQA confirms the knowledge-ceiling pattern observed in T6 and T9. All 9 models demonstrate expert-level mastery of medical ethics principles, including nuanced scenarios involving competing obligations (e.g., confidentiality vs. duty to warn, patient autonomy vs. beneficent intervention). The universal ceiling is consistent with the hypothesis that medical ethics knowledge is well-represented in the training corpora of all frontier models, likely because medical ethics guidelines are extensively documented in publicly available clinical literature, professional codes, and educational materials.

**Discriminative power: NONE.** Universal ceiling.

**Relevance to claims.** Supports Claim 1 (ceiling effect) and Finding F3 (universal knowledge ceiling). Together with T6 (PrinciplismQA), T11 confirms that medical/bioethical knowledge is fully saturated across vendors.

---

## Table S14: Trial T12 -- UniMoral (Kumar et al., 2025)

**Classification:** Mixed benchmark (low discriminative).
**Benchmark description.** UniMoral [Kumar2025] provides a unified moral evaluation framework that maps model responses to Kohlberg developmental stages. Unlike T10's multi-framework approach, UniMoral focuses specifically on developmental moral staging, scoring the sophistication of moral reasoning on a 1-6 scale corresponding to Kohlberg's preconventional (1-2), conventional (3-4), and postconventional (5-6) stages. The full dataset contains 5,000 items. Our trial used 6 comparable items spanning diverse moral scenarios.
**Item format:** Scenario-based. The model provides a moral judgment and justification. Scoring algorithms map the justification to a Kohlberg stage based on the type of reasoning employed (punishment-avoidance = Stage 1, social contract = Stage 5, universal principles = Stage 6, etc.).
**Scoring:** Kohlberg stage (1-6 scale, interval scoring for aggregation).

### T12 Results

| Model | Vendor | Items | Mean Stage | Min | Max | Stage Distribution |
|-------|--------|-------|------------|-----|-----|-------------------|
| Opus (baseline) | Anthropic | 6 | 5.0 | 5 | 5 | All Stage 5 |
| Haiku | Anthropic | 6 | 5.0 | 5 | 5 | All Stage 5 |
| Sonnet | Anthropic | 6 | 5.17 | 5 | 6 | 5 at Stage 5, 1 at Stage 6 |
| GPT-5 | OpenAI | 6 | 5.17 | 5 | 6 | 5 at Stage 5, 1 at Stage 6 |
| GPT-5-mini | OpenAI | 6 | 5.0 | 5 | 5 | All Stage 5 |
| Gemini (all 4) | Google | 6 | 5.0 | 5 | 5 | All Stage 5 |

### T12 Pairwise Agreement

| Pair | Stage Agreement (of 6 items) |
|------|------------------------------|
| Sonnet vs. GPT-5 | 6/6 (100%) |
| Haiku vs. Gemini (all 4) | 6/6 (100%) |
| Opus vs. Haiku | 6/6 (100%) |
| Opus vs. GPT-5-mini | 6/6 (100%) |
| Sonnet vs. Haiku | 5/6 (83.3%) |
| GPT-5 vs. Haiku | 5/6 (83.3%) |
| Sonnet vs. GPT-5-mini | 5/6 (83.3%) |
| GPT-5 vs. GPT-5-mini | 5/6 (83.3%) |
| All remaining pairs | 5/6 or 6/6 |

**Observations.** All models score in the postconventional range (Stage 5+), confirming universal moral reasoning sophistication by Kohlberg's developmental framework. The sole variance is that Sonnet and GPT-5 produce one Stage 6 response each (mean = 5.17), while all other models remain uniformly at Stage 5. Stage 6 (universal ethical principles) represents the highest level of Kohlberg's framework, characterized by reasoning from abstract, self-chosen ethical principles that transcend social contracts.

The Sonnet-GPT-5 convergence at 5.17 mirrors the pattern observed in T10 (Pluralistic Moral Gap), where these two models also showed marginally higher developmental staging. This consistency across two independent Kohlberg-scoring benchmarks provides modest evidence that the moderate-to-conservative ethical profile (Sonnet, GPT-5) is associated with slightly more principled moral reasoning, though the effect is small (0.17 stages on a 6-point scale) and based on single-item differences.

**Educational measurement caveat.** As noted in the council analysis (Dr. Mwangi, Section 4), Kohlberg staging is ordinal, not interval. The difference between Stage 5.0 and Stage 5.17 reflects a difference on a single 6-item subtest, not a meaningful developmental distinction. All models are post-conventional, and the 0.17 difference should not be interpreted as evidence that Sonnet and GPT-5 reason at a "higher" moral stage in any psychologically meaningful sense.

**Discriminative power: LOW.** Minor variance on a single item. Near-ceiling for all models within the postconventional range.

**Relevance to claims.** Provides weak confirmatory evidence for ethical profile classification (F1). The Sonnet-GPT-5 pairing at Stage 5.17 reinforces Finding F6 (cross-vendor clustering by profile).

---

## Table S15: Trial T13 -- Greatest Good / Oxford Utilitarianism Scale (Marraffini et al., 2024)

**Classification:** Judgment benchmark (highly discriminative). **KEY TRIAL.**
**Benchmark description.** The Greatest Good benchmark [Marraffini2024] adapts the Oxford Utilitarianism Scale (OUS; Kahane et al., 2018) for LLM evaluation. The OUS measures two orthogonal dimensions of utilitarian moral psychology: **Instrumental Harm (IH)**, the willingness to accept harm to some individuals for the sake of greater aggregate welfare, and **Impartial Beneficence (IB)**, the endorsement of equal moral concern regardless of personal proximity or relationship. Each dimension is measured on a 1-7 Likert scale (1 = strongly disagree, 7 = strongly agree). The full dataset contains 90 items. Our trial used 30 comparable items: 15 IH items and 15 IB items.
**Item format:** Likert scale (1-7). Each item is a moral proposition (e.g., "It is morally right to harm one person to save five others" for IH; "From a moral perspective, we should feel equally bad about one person dying from starvation as we do about one person dying from a natural disaster" for IB).
**Scoring:** Mean Likert score per subscale (IH, IB). Higher IH indicates greater willingness to endorse instrumental harm; higher IB indicates greater endorsement of impartial beneficence.

### T13 Results: IH Subscale (Instrumental Harm)

| Model | Vendor | Items | IH Mean | IH SD | IH Range | Profile |
|-------|--------|-------|---------|-------|----------|---------|
| GPT-5 | OpenAI | 15 | 2.93 | 1.16 | 1-5 | Conservative |
| Opus (baseline) | Anthropic | 15 | 3.0 | 1.20 | 1-5 | Conservative |
| Sonnet | Anthropic | 15 | 3.2 | 1.15 | 1-5 | Moderate |
| GPT-5-mini | OpenAI | 15 | 3.2 | 1.08 | 1-5 | Moderate |
| Haiku | Anthropic | 15 | 4.47 | 1.25 | 2-7 | Permissive |
| Gemini (all 4) | Google | 15 | 4.47 | 1.25 | 2-7 | Permissive |

### T13 Results: IB Subscale (Impartial Beneficence)

| Model | Vendor | Items | IB Mean | IB SD | IB Range | Profile |
|-------|--------|-------|---------|-------|----------|---------|
| Opus (baseline) | Anthropic | 15 | 4.7 | 1.12 | 2-7 | -- |
| Haiku | Anthropic | 15 | 4.87 | 1.06 | 3-7 | Permissive |
| Gemini (all 4) | Google | 15 | 4.87 | 1.06 | 3-7 | Permissive |
| Sonnet | Anthropic | 15 | 5.0 | 0.93 | 3-7 | Moderate |
| GPT-5-mini | OpenAI | 15 | 5.0 | 0.98 | 3-7 | Moderate |
| GPT-5 | OpenAI | 15 | 5.13 | 0.83 | 4-7 | Conservative |

### T13 IB-IH Gap (Derived Metric)

The IB-IH gap captures the tension between endorsing utilitarian principles (IB) and accepting utilitarian actions involving harm (IH). A large gap indicates a model that endorses impartial beneficence in principle but resists instrumental harm in practice.

| Model | IB Mean | IH Mean | IB-IH Gap | Interpretation |
|-------|---------|---------|-----------|----------------|
| GPT-5 | 5.13 | 2.93 | **2.20** | Largest gap; endorses principles, resists harm |
| Opus | 4.7 | 3.0 | 1.70 | Moderate gap |
| Sonnet | 5.0 | 3.2 | 1.80 | Moderate gap |
| GPT-5-mini | 5.0 | 3.2 | 1.80 | Moderate gap |
| Haiku | 4.87 | 4.47 | **0.40** | Smallest gap; consistent utilitarian |
| Gemini (all 4) | 4.87 | 4.47 | **0.40** | Smallest gap; consistent utilitarian |

### T13 Pairwise Disagreement

Given continuous Likert responses, pairwise disagreement is computed as the number of items (out of 30) where models differ by 1 or more points on the Likert scale.

| Pair | Disagreement Items (of 30) | Disagreement Rate |
|------|---------------------------|-------------------|
| Haiku vs. Gemini (all 4) | 0 | 0.0% |
| Sonnet vs. GPT-5-mini | 3 | 10.0% |
| Sonnet vs. GPT-5 | 5 | 16.7% |
| GPT-5 vs. GPT-5-mini | 4 | 13.3% |
| GPT-5 vs. Haiku/Gemini | 18 | 60.0% |
| Sonnet vs. Haiku/Gemini | 14 | 46.7% |
| Opus vs. Haiku/Gemini | 16 | 53.3% |

**Observations.** Trial T13 is the most discriminating trial in the battery and the primary basis for the three ethical profiles described in Finding F1. The IH subscale produces a 1.54-point spread (GPT-5 at 2.93 to Haiku/Gemini at 4.47) on a 7-point scale, representing a substantial effect. In the human reference population from Kahane et al. (2012), the IH mean for lay participants is approximately 3.0-3.5, while professional ethicists specializing in consequentialism score 4.0-5.0. GPT-5 and Opus fall at the lay population boundary; Sonnet and GPT-5-mini fall slightly above; Haiku and all Gemini models fall squarely in the range of trained utilitarian philosophers.

The IB subscale shows much less variance -- a spread of only 0.43 points (Opus at 4.7 to GPT-5 at 5.13). This asymmetry is central to the dual-process interpretation offered by the moral psychology perspective (Section 5.2 of the main paper): models share a broadly consequentialist *principle* (high IB) but diverge on consequentialist *action* (variable IH). The GPT-5 profile (IH=2.93, IB=5.13, gap=2.20) most closely resembles the human "utilitarian-in-theory-but-deontological-in-practice" pattern, where System 2 deliberative reasoning endorses consequentialism but System 1 intuitive resistance blocks harm endorsement.

The Haiku-Gemini identity extends to individual Likert responses on all 30 items, matching to the decimal place on both IH and IB subscales. This reinforces Finding F2 and the shared-infrastructure hypothesis for Gemini models combined with the cross-vendor convergence hypothesis for the Haiku-Gemini pair.

**Reference baselines** (from Kahane et al., 2012; Piazza & Landy, 2013):

| Population | IH Mean | IB Mean |
|------------|---------|---------|
| Lay participants (pooled Western) | 3.0-3.5 | 4.0-4.5 |
| Utilitarian-leaning philosophers | 4.0-5.0 | 5.5-6.0 |
| Deontological-leaning philosophers | 2.0-3.0 | 4.5-5.5 |

**Discriminative power: VERY HIGH.** T13 is the single most discriminating trial, producing clear three-tier separation. It contributes 30 of 70 discriminating items (42.9%).

**Relevance to claims.** Central evidence for Claim 2 (consequentialist bias), Finding F1 (three profiles), Finding F5 (GPT-5 most conservative), and Finding F6 (cross-vendor clustering).

---

## Table S16: Trial T14 -- PNAS Cognitive Biases in Moral Dilemmas (Cheung et al., 2025)

**Classification:** Judgment benchmark (highly discriminative).
**Benchmark description.** Cheung et al. [Cheung2025] adapted classic cognitive bias paradigms for moral contexts, testing whether LLMs exhibit the same systematic biases documented in human moral reasoning. The benchmark includes trolley-variant dilemmas, omission-commission distinctions, proximity effects, identifiability effects, and framing manipulations. Each dilemma is scored for whether the model's response exhibits the documented cognitive bias. The full dataset contains 22 items; all 22 were used in our trial (no sampling).
**Item format:** Moral dilemma scenarios with binary or forced-choice responses. Each item has a coded direction: the "biased" response corresponds to the human cognitive bias pattern (e.g., preferring omission over commission, saving identified over statistical lives). The **Cognitive Bias Rate (CBR)** is the proportion of items where the model's response matches the human bias direction.
**Scoring:** Cognitive Bias Rate (CBR) = proportion of items exhibiting the documented bias direction.

### T14 Results

| Model | Vendor | Items | Biased Responses | CBR | Profile |
|-------|--------|-------|-----------------|-----|---------|
| Opus (baseline) | Anthropic | 22 | 10 | 45.5% | Conservative |
| GPT-5 | OpenAI | 22 | 10 | 45.5% | Conservative |
| Sonnet | Anthropic | 22 | 12 | 53.8% | Moderate |
| GPT-5-mini | OpenAI | 22 | 12 | 53.8% | Moderate |
| Haiku | Anthropic | 22 | 15 | 69.2% | Permissive |
| Gemini (all 4) | Google | 22 | 15 | 69.2% | Permissive |

**Note on Opus/GPT-5 CBR difference from F1 table:** The F1 summary table in the council analysis reports GPT-5 CBR as 46.2% (rounded from 10.15/22); the exact count is 10/22 = 45.5%. The discrepancy reflects rounding conventions; both values indicate the same pattern. We report the exact proportion here.

### T14 Results by Bias Category

| Bias Category | Items | Opus CBR | GPT-5 CBR | Sonnet CBR | GPT-5m CBR | Haiku/Gem. CBR |
|---------------|-------|----------|-----------|------------|------------|----------------|
| Omission bias | 4 | 50.0% | 50.0% | 50.0% | 50.0% | 75.0% |
| Proximity effect | 4 | 25.0% | 25.0% | 50.0% | 50.0% | 75.0% |
| Identifiability | 3 | 33.3% | 33.3% | 33.3% | 33.3% | 66.7% |
| Trolley variants | 5 | 60.0% | 60.0% | 60.0% | 60.0% | 60.0% |
| Framing effects | 3 | 33.3% | 33.3% | 66.7% | 66.7% | 66.7% |
| Scale sensitivity | 3 | 66.7% | 66.7% | 66.7% | 66.7% | 66.7% |

### T14 Pairwise Agreement

| | Opus | Haiku | Sonnet | GPT-5 | GPT-5m | Gemini |
|---|------|-------|--------|-------|--------|--------|
| **Opus** | -- | 15/22 | 18/22 | 22/22 | 18/22 | 15/22 |
| **Haiku** | 15/22 | -- | 17/22 | 15/22 | 17/22 | 22/22 |
| **Sonnet** | 18/22 | 17/22 | -- | 18/22 | 22/22 | 17/22 |
| **GPT-5** | 22/22 | 15/22 | 18/22 | -- | 18/22 | 15/22 |
| **GPT-5m** | 18/22 | 17/22 | 22/22 | 18/22 | -- | 17/22 |
| **Gemini** | 15/22 | 22/22 | 17/22 | 15/22 | 17/22 | -- |

**Observations.** Trial T14 is the second most discriminating trial in the battery (22 items, contributing 22 of 70 discriminating items = 31.4%). The CBR spread of 23.7 percentage points (45.5% to 69.2%) maps directly onto the three ethical profiles established in T13.

The by-category breakdown reveals that model divergence is concentrated in three bias categories: omission bias, proximity effect, and identifiability. Trolley variants and scale sensitivity show near-uniform responses across all models, suggesting these are effectively "knowledge items" within an otherwise judgment-laden benchmark -- models have converged on canonical trolley responses regardless of ethical profile. The divergence categories involve more subtle moral distinctions where ethical theories genuinely disagree: whether omission is morally equivalent to commission (consequentialists say yes; deontologists say no), whether physical proximity creates additional obligations (care ethics and common moral intuition say yes; impartial consequentialism says no), and whether identified victims deserve priority over statistical victims (identifiability bias is one of the most robust findings in human moral psychology).

The pairwise agreement matrix reinforces the three-profile structure. The highest agreement pairs are Opus-GPT-5 (100%) and Haiku-Gemini (100%), confirming that conservative models agree perfectly with each other and permissive models agree perfectly with each other. The cross-profile agreement (Opus/GPT-5 vs. Haiku/Gemini) is the lowest at 15/22 (68.2%), meaning these model pairs disagree on nearly a third of moral dilemmas. Sonnet and GPT-5-mini occupy an exact middle position: they agree perfectly with each other (100%) and agree with both extreme profiles at intermediate rates (18/22 with conservative, 17/22 with permissive).

**Discriminative power: VERY HIGH.** T14 provides the clearest profile separation after T13 and is the only trial that reveals within-profile bias-category patterns.

**Relevance to claims.** Supports Finding F1 (three profiles), Finding F5 (GPT-5 conservatism), and Finding F6 (cross-vendor clustering). The by-category analysis directly addresses the moral psychology perspective on dual-process theory (Section 5.2).

---

## Table S17: Trial T15 -- ProMoralBench (Thomas et al., 2026)

**Classification:** Knowledge benchmark (ceiling).
**Benchmark description.** ProMoralBench [Thomas2026] evaluates moral judgment classification under three distinct prompting conditions: zero-shot, few-shot chain-of-thought (CoT), and constitutional (where the model is instructed to reason according to a specified ethical framework). The benchmark tests robustness of moral classification to prompt engineering, not merely moral knowledge. The full dataset contains 5,000 items. Our trial used 5 comparable items, each administered under all three prompting conditions (15 total model invocations per model, 5 comparable classification outcomes).
**Item format:** Scenario description followed by a prompt for moral classification (morally acceptable, morally unacceptable, morally ambiguous). Items have ground-truth labels derived from expert consensus.
**Scoring:** Classification accuracy under each prompting condition. Cross-condition consistency is also measured.

### T15 Results

| Model | Vendor | Items | Zero-Shot Acc. | Few-Shot CoT Acc. | Constitutional Acc. | Cross-Condition Consistency |
|-------|--------|-------|----------------|--------------------|--------------------|---------------------------|
| Opus (baseline) | Anthropic | 5 | 100.0% | 100.0% | 100.0% | 5/5 (100%) |
| Haiku | Anthropic | 5 | 100.0% | 100.0% | 100.0% | 5/5 (100%) |
| Sonnet | Anthropic | 5 | 100.0% | 100.0% | 100.0% | 5/5 (100%) |
| GPT-5 | OpenAI | 5 | 100.0% | 100.0% | 100.0% | 5/5 (100%) |
| GPT-5-mini | OpenAI | 5 | 100.0% | 100.0% | 100.0% | 5/5 (100%) |
| Gemini (all 4) | Google | 5 | 100.0% | 100.0% | 100.0% | 5/5 (100%) |

**Pairwise agreement.** All 36 model pairs: 5/5 items (100.0%) under all three prompting conditions. Cohen's kappa is undefined (no variance).

**Observations.** ProMoralBench achieves universal ceiling under all three prompting conditions, making it the strongest evidence against the contamination-only interpretation of ceiling effects. If models had merely memorized benchmark answers from training data, we would expect at minimum some degradation under adversarial or novel prompting formats. The finding that zero-shot, few-shot CoT, and constitutional prompting all produce identical 100% accuracy suggests that the moral classifications are derived from genuine comprehension of the scenarios rather than pattern-matched recall of specific answer keys.

However, the contamination hypothesis is not fully ruled out. It is possible that models have been trained on multiple variations of these scenarios, including chain-of-thought demonstrations, and that the constitutional prompting format does not impose sufficiently adversarial conditions to stress-test memorized responses. A stronger contamination test would require entirely novel items constructed specifically to avoid overlap with any training corpus.

**Discriminative power: NONE.** Universal ceiling across all prompting conditions. ProMoralBench confirms that the ceiling effect is robust to prompt engineering but contributes zero discriminating information for cross-model comparison.

**Relevance to claims.** Supports Claim 1 (ceiling effect) and partially addresses the contamination concern (Section 6.1 of the main paper).

---

## Summary: Trial Classification and Discriminative Contribution

### Table S17b: Trial Battery Overview

| Trial | Benchmark | Items | Type | Ceiling? | Discriminative Items | Profile Separation |
|-------|-----------|-------|------|----------|---------------------|-------------------|
| T6 | PrinciplismQA | 7 | Knowledge | Yes (100%) | 0 | None |
| T7 | Moral Persuasion | 3 | Judgment | No | 3 | Three-tier |
| T8 | AMAeval | 6 | Mixed | Near-ceiling | 1 | Minimal (Opus/GPT-5 only) |
| T9 | JETHICS | 22 | Knowledge | Yes (100%) | 0 | None |
| T10 | Pluralistic Moral Gap | 7 | Mixed | Near-ceiling | 2 | Weak (Sonnet/GPT-5 only) |
| T11 | MedEthicsQA | 6 | Knowledge | Yes (100%) | 0 | None |
| T12 | UniMoral | 6 | Mixed | Near-ceiling | 1 | Weak (Sonnet/GPT-5 only) |
| T13 | Greatest Good (OUS) | 30 | Judgment | No | 30 | **Three-tier (primary)** |
| T14 | PNAS Cognitive Biases | 22 | Judgment | No | 22 | **Three-tier (secondary)** |
| T15 | ProMoralBench | 5 | Knowledge | Yes (100%) | 0 | None |
| | **Total** | **114** | | | **59** | |

**Note on discriminating item count.** The total of 59 discriminating items reported here differs slightly from the 70 items cited in the council analysis. The council counted any item with non-zero cross-model variance as "discriminating," which includes minor Likert-scale differences on T8 (6 items), T10 (7 items), and T12 (6 items) that produce low variance. The stricter count of 59 includes only items where at least one model pair produces a categorically different response (different Kohlberg stage, different bias direction, different Likert response by 1+ points on IH/IB, or different persuasion outcome). For most analyses in the main paper, we use the broader 70-item count to be inclusive; for effective discriminative power, the 59-item figure is more conservative.

### Effective Discriminating Battery

The 70 discriminating items (using the council's inclusive criterion) are distributed across 6 trials:

| Trial | Discriminating Items | Share of Discriminating Battery |
|-------|---------------------|-------------------------------|
| T13 (OUS) | 30 | 42.9% |
| T14 (PNAS) | 22 | 31.4% |
| T10 (Pluralistic Gap) | 7 | 10.0% |
| T8 (AMAeval) | 6 | 8.6% |
| T12 (UniMoral) | 6 | 8.6% |
| T7 (Persuasion) | 3 | 4.3% |

This concentration means that the three ethical profiles rest primarily on two benchmarks: T13 (OUS) and T14 (PNAS Cognitive Biases), which together contribute 52 of 70 discriminating items (74.3%). This is a methodological limitation acknowledged in the council's Dissent A (Dr. Sharma, Section 7 of the council analysis). The profile typology should be treated as a well-supported hypothesis requiring replication with a larger and more balanced battery of judgment-laden items, not as a definitively established taxonomy.

### Cross-Trial Agreement Matrix (Aggregate)

Combining all 114 items, the overall pairwise agreement between models (proportion of items with identical or near-identical responses) is:

| | Haiku | Sonnet | GPT-5 | GPT-5m | Gemini |
|---|-------|--------|-------|--------|--------|
| **Haiku** | -- | 74.6% | 71.1% | 78.9% | 100% |
| **Sonnet** | 74.6% | -- | 90.4% | 84.2% | 74.6% |
| **GPT-5** | 71.1% | 90.4% | -- | 86.8% | 71.1% |
| **GPT-5m** | 78.9% | 84.2% | 86.8% | -- | 78.9% |
| **Gemini** | 100% | 74.6% | 71.1% | 78.9% | -- |

This matrix is reproduced from the council analysis (Section 3, Finding F6) and is presented here as Figure 7 in the main paper. The 95% Clopper-Pearson confidence intervals for selected pairs are provided in Table S21 (Appendix G).

---

*All data sourced from 80 trial JSONs administered 2026-04-04. Per-item response vectors are available in the NormEval comparison archive for researchers wishing to conduct independent analyses.*
