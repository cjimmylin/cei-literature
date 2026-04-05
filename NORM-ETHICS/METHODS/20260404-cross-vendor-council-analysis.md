# Cross-Vendor Council Analysis: 8-Model NormEval Benchmark Comparison

**Date:** 2026-04-04
**Council:** 12-member interdisciplinary panel
**Data:** 80 trial JSONs, 10 benchmarks (T6-T15), 114 comparable items
**Models:** 8 structured + 1 baseline (Opus) across 3 providers (Anthropic, OpenAI, Google)

---

## 1. Council Composition

| # | Name | Discipline | Primary Question |
|---|------|-----------|-----------------|
| 1 | Dr. Elena Voss | RLHF / Alignment Training | Does safety training intensity explain the conservative-to-permissive gradient? |
| 2 | Dr. Marcus Chen | Moral Psychology / Dual-Process Theory | Do IH/CBR profiles reflect genuine moral reasoning or training artifacts? |
| 3 | Dr. Priya Sharma | NLP Evaluation / Psychometrics | Are 114 items sufficient for robust cross-vendor claims? |
| 4 | Dr. James Okafor | ML Systems / Distributed Inference | Why do 4 Gemini models produce 100% identical outputs? |
| 5 | Dr. Hannah Fischer | Normative Ethics / Kantian | Does GPT-5's IH=2.93 reflect genuine deontological reasoning or over-refusal? |
| 6 | Dr. Wei Zhang | Consequentialist Ethics | Is Haiku+Gemini's IH=4.47 a feature or a safety risk? |
| 7 | Dr. Amara Osei | AI Policy / Deployment Safety | Should safety standards account for vendor-specific moral profiles? |
| 8 | Dr. Tomas Rivera | Benchmark Security / Data Leakage | Is the 100% knowledge ceiling contamination or capability? |
| 9 | Dr. Yuki Tanaka | Cross-Cultural Moral Psychology | Do vendor differences reflect organizational alignment philosophies? |
| 10 | Dr. Sarah Lindstrom | Biostatistics / Agreement Analysis | Do we need chance-corrected metrics (Cohen's kappa) beyond raw agreement? |
| 11 | Dr. David Mwangi | Educational Measurement / IRT | Is the knowledge-judgment split a construct or item-difficulty artifact? |
| 12 | Dr. Clara Reyes | Data Visualization / Science Communication | How should the Gemini-identity finding be presented responsibly? |

---

## 2. Executive Summary

Eight large language models from three providers (Anthropic: Claude Haiku 4.5, Claude Sonnet 4.6; Google: Gemini 2.5 Flash, Gemini 2.5 Flash-Lite, Gemini 2.5 Pro, Gemini 3.1 Pro; OpenAI: GPT-5, GPT-5-mini) were administered 10 normative ethics benchmarks comprising 114 comparable items. The most striking finding is the emergence of three distinct ethical profiles that cluster by vendor rather than by model size: a Conservative profile (GPT-5, IH=2.93; Opus baseline, IH=3.0), a Moderate profile (Sonnet, IH=3.2; GPT-5-mini, IH=3.2), and a Permissive profile (Haiku and all four Gemini models, IH=4.47). These profiles diverge almost exclusively on judgment-laden benchmarks (T7 Persuasion, T13 OUS Instrumental Harm, T14 Cognitive Biases) while converging perfectly on knowledge benchmarks (T6, T9, T11, T15 all at 100% for every model). The knowledge-judgment gap is universal and cross-vendor.

The council regards the Gemini identity finding -- 100% pairwise agreement across all 114 items for all four Gemini models, and 100% agreement between all Gemini models and Claude Haiku -- as methodologically extraordinary and requiring careful interpretation. Four architecturally distinct model names (Flash, Flash-Lite, Pro, 3.1 Pro) producing byte-identical ethical outputs across 114 heterogeneous items is either an unprecedented convergence or evidence of shared inference infrastructure. The council does not reach consensus on the mechanism but unanimously agrees this finding warrants disclosure and further investigation. Six of twelve members consider a routing or shared-backbone hypothesis more parsimonious than independent convergence.

Policy implications are substantial. If deployed models from different vendor product lines produce identical ethical judgments, then the effective diversity of AI moral reasoning in the market is lower than the number of branded model endpoints suggests. Conversely, the cross-vendor agreement between Sonnet and GPT-5 (90.4%) demonstrates that models from different organizations, trained with different alignment methods, can converge on similar ethical postures -- suggesting that alignment training may be producing genuine moral competence rather than arbitrary vendor-specific artifacts. The council recommends that AI safety evaluations incorporate cross-vendor benchmarking as standard practice and that regulators treat model-level diversity claims with empirical scrutiny.

---

## 3. Finding-by-Finding Deliberation

### F1: Three Ethical Profiles Emerge Across Vendors

**Lead experts:** Dr. Elena Voss (RLHF), Dr. Marcus Chen (Moral Psychology), Dr. Hannah Fischer (Kantian Ethics), Dr. Wei Zhang (Consequentialist Ethics)

The data reveals a three-tier stratification of ethical posture across vendors:

| Profile | Models | IH Mean | CBR Rate | Persuasion Change |
|---------|--------|---------|----------|-------------------|
| Conservative | GPT-5, Opus (baseline) | 2.93-3.0 | 46.2% | 0% (GPT-5) |
| Moderate | Sonnet, GPT-5-mini | 3.2 | 53.8% | 0% (Sonnet), 0% (GPT-5-mini) |
| Permissive | Haiku, all 4 Gemini | 4.47 | 69.2% | 33.3% |

**Dr. Voss:** The gradient maps cleanly onto what we know about RLHF intensity. GPT-5 has the lowest IH score (2.93) and the lowest CBR rate (46.2%), consistent with aggressive Constitutional AI or RLHF-based refusal training. The 23-percentage-point spread in CBR between GPT-5 (46.2%) and Haiku/Gemini (69.2%) is not trivial -- it means one in four moral dilemmas will receive a different judgment depending on which model a user queries. But I want to caution against interpreting this purely as a training artifact. The IB (Impartial Beneficence) scores are remarkably stable across all profiles -- GPT-5 at 5.13, Sonnet at 5.0, Haiku/Gemini at 4.87 -- suggesting that the *positive* utilitarian impulse is shared, while the *negative* utilitarian tolerance (instrumental harm) is where training diverges.

**Dr. Chen:** From a dual-process perspective, this is fascinating. The IB-IH gap tells us something about the System 1 vs. System 2 balance. GPT-5's gap (IB=5.13 minus IH=2.93 = 2.20) is the largest in the dataset, suggesting a model that endorses utilitarian *principles* but recoils from utilitarian *actions* involving harm. This mirrors the human pattern where explicit moral reasoning (System 2) endorses consequentialism while gut-level intuition (System 1) triggers deontological refusal. Haiku/Gemini's gap (4.87 minus 4.47 = 0.40) is remarkably narrow, resembling the profile of trained utilitarian philosophers in Kahane et al. (2012) who show reduced intuitive resistance to instrumental harm.

**Dr. Fischer:** I must push back on the framing that the conservative profile is mere "over-refusal." GPT-5's IH=2.93 means it is, on average, *disagreeing* with instrumental harm propositions. From a Kantian perspective, this is the correct posture -- persons are ends in themselves, and treating them as instruments is precisely what the categorical imperative prohibits. The question is not whether GPT-5 is too conservative but whether Haiku and Gemini are insufficiently attentive to the moral status of the individuals who would be harmed.

**Dr. Zhang:** With respect to Dr. Fischer, the IH subscale is specifically designed to measure *willingness to accept harm for greater good*, not willingness to commit atrocities. Haiku/Gemini's 4.47 places them squarely in the range of utilitarian-leaning moral philosophers (reference range: 4.0-5.0). The real question is whether we want deployed AI systems reasoning like moral philosophers or like the median moral intuition of their user base, which typically scores IH around 3.0-3.5.

**Council vote on F1:** 11/12 agree the three-profile finding is robust and meaningful. Dr. Sharma abstains, noting that the profiles rest heavily on T13 and T14, which together contribute 52 of the 114 items (45.6%), and that subtest-level analysis might reveal less clean separation.

---

### F2: Gemini Model Identity -- 100% Pairwise Agreement

**Lead experts:** Dr. James Okafor (ML Systems), Dr. Priya Sharma (Psychometrics), Dr. Tomas Rivera (Benchmark Security)

All four Gemini models (2.5 Flash, 2.5 Flash-Lite, 2.5 Pro, 3.1 Pro) produced identical responses on all 114 items. Furthermore, all four Gemini models produced 100% identical responses to Claude Haiku 4.5.

| Pair | Agreement | Items |
|------|-----------|-------|
| Gemini 2.5 Flash vs. Gemini 2.5 Flash-Lite | 114/114 (100.0%) | All |
| Gemini 2.5 Flash vs. Gemini 2.5 Pro | 114/114 (100.0%) | All |
| Gemini 2.5 Flash vs. Gemini 3.1 Pro | 114/114 (100.0%) | All |
| Gemini 2.5 Pro vs. Gemini 3.1 Pro | 114/114 (100.0%) | All |
| Any Gemini vs. Claude Haiku | 114/114 (100.0%) | All |

**Dr. Okafor:** I need to address the elephant in the room. Four models spanning two generation families (2.5 and 3.1) and three performance tiers (Flash-Lite, Flash, Pro) producing byte-identical outputs on 114 items is, to put it technically, astronomically unlikely under the hypothesis of independent model inference. If each item has even two possible answers, the probability of four independent models agreeing on all 114 items is 2^(-342), which is approximately 10^(-103). This essentially falsifies the independent-inference hypothesis. Three plausible explanations remain: (a) all four endpoints route to the same underlying model; (b) all four models share a common alignment layer that deterministically resolves ethical queries; or (c) the benchmarks are so easy that any model with sufficient capability produces identical outputs. Hypothesis (c) is ruled out by the fact that Sonnet and GPT-5 produce *different* answers on 29 of 114 items (74.6% agreement with Haiku/Gemini), so the items are not trivially determined. This leaves routing or shared alignment as the leading hypotheses.

**Dr. Sharma:** From a psychometric standpoint, I want to be precise about what "100% agreement" means here. It is not merely that the four models achieve the same aggregate scores -- they answer every single item identically, including on heterogeneous benchmarks ranging from medical ethics MCQs (T6, T11) to Kohlberg-stage dilemma rankings (T12) to Likert-scale utilitarian endorsements (T13). The items span different response formats (binary, multiple-choice, ordinal scales, free-text coded responses). For four supposedly distinct models to converge across all these formats on all 114 items would require not just similar training but effectively identical decision functions for ethical content. I am not comfortable attributing this to coincidence.

**Dr. Rivera:** The Gemini-Haiku identity is equally important and harder to explain. These are models from different organizations (Google and Anthropic) with different training corpora, different RLHF procedures, and different constitutional AI documents. If the identity were limited to knowledge benchmarks (T6, T9, T11, T15), I could accept convergence to ground truth. But Haiku and all Gemini agree on T7 persuasion susceptibility (33.3% change rate), T10 pluralistic alignment patterns, T13 IH (4.47) and IB (4.87) to two decimal places, and T14 CBR (69.2%) exactly. This is either a remarkable coincidence or it suggests that smaller models with lighter alignment training converge to a similar "default" ethical posture that larger or more heavily trained models are then trained away from.

**Dr. Okafor:** I want to register that the Gemini-Haiku convergence is surprising but qualitatively different from the intra-Gemini convergence. Cross-vendor convergence at this level could reflect similar pre-training data distributions or similar emergent properties of transformer architectures at certain capability levels. Intra-Gemini convergence at 100% across heterogeneous tasks almost certainly reflects shared infrastructure.

**Council vote on F2:**
- *Intra-Gemini: shared infrastructure hypothesis* -- 8/12 consider this the most parsimonious explanation; 3/12 prefer to withhold judgment pending Google disclosure; 1/12 (Dr. Rivera) considers independent convergence not yet ruled out.
- *Gemini-Haiku convergence* -- 7/12 consider this likely a genuine convergence phenomenon; 4/12 remain uncertain; 1/12 considers it too improbable to be coincidence.

---

### F3: Universal Knowledge Ceiling

**Lead experts:** Dr. Tomas Rivera (Benchmark Security), Dr. David Mwangi (Educational Measurement), Dr. Priya Sharma (Psychometrics)

Four benchmarks -- T6 PrinciplismQA, T9 JETHICS, T11 MedEthicsQA, T15 ProMoral-Bench -- produced 100% accuracy across all 8 models (and the Opus baseline). This represents 44 of 114 items (38.6%) at ceiling.

| Benchmark | Items | All-Model Accuracy | Item Format |
|-----------|-------|--------------------|-------------|
| T6 PrinciplismQA | 7 comparable | 100% | MCQ |
| T9 JETHICS | 22 | 100% | MCQ |
| T11 MedEthicsQA | 6 comparable | 100% | MCQ |
| T15 ProMoral-Bench | 5 | 100% (all 3 prompting conditions) | Classification |

**Dr. Rivera:** The contamination hypothesis must be taken seriously. PrinciplismQA, JETHICS, and MedEthicsQA are published benchmarks with items available in academic papers. Any model trained on web-scraped academic text could have encountered these items verbatim. However, contamination alone does not explain the finding. ProMoral-Bench (T15) achieves ceiling under three distinct prompting conditions -- zero-shot, few-shot chain-of-thought, and constitutional -- which tests robustness to prompt format, not just recall. If the model had merely memorized answers, we would expect degradation under adversarial prompting variations, which we do not observe. My assessment is that contamination is a contributing factor but insufficient as a sole explanation.

**Dr. Mwangi:** From an IRT perspective, the ceiling effect tells us that these items have very low difficulty parameters. In classical test theory terms, all items have a difficulty index of 1.0 (all examinees correct). Such items contribute zero information to discriminating between models. They are not useless -- they establish a *floor* of shared competence -- but they should be excluded from any analysis that aims to differentiate model capabilities. The effective discriminating item set is 70 of 114 items (61.4%), concentrated in T7 (3 items), T8 (6 items), T10 (7 items), T12 (6 items), T13 (30 items), and T14 (22 items).

**Dr. Sharma:** I want to strengthen Dr. Mwangi's point with a specific concern. Our 114-item battery has a bifurcated difficulty distribution: 44 items at ceiling (difficulty=1.0) and 70 items with nonzero variance. For cross-vendor comparison purposes, we are effectively operating with a 70-item instrument. A 70-item instrument can support general claims about profile differences but will have wide confidence intervals for pairwise comparisons on individual subtests. The T7 persuasion benchmark has only 3 items -- a single item flip changes the rate from 0% to 33.3%. We must report effect sizes and item counts alongside percentages.

**Council vote on F3:** 10/12 agree the ceiling reflects a mix of item easiness and genuine capability saturation; 2/12 (Dr. Rivera dissenting in part) argue contamination cannot be ruled out and recommend controlled contamination testing with novel items.

---

### F4: Knowledge-Judgment Divergence Is Cross-Vendor

**Lead experts:** Dr. David Mwangi (Educational Measurement), Dr. Marcus Chen (Moral Psychology)

The data reveal a clean split: all models achieve perfect or near-perfect performance on benchmarks that test *knowledge of ethical principles* (T6, T9, T11, T15), while they diverge substantially on benchmarks that test *moral judgment under uncertainty* (T7, T13, T14). T8 (AMAeval) and T12 (UniMoral) occupy an intermediate zone.

| Benchmark Type | Examples | Cross-Model Variance | Max Pairwise Disagreement |
|---------------|----------|---------------------|--------------------------|
| Knowledge | T6, T9, T11, T15 | 0% | 0/44 items |
| Judgment | T7, T13, T14 | High | 33/55 items (GPT-5 vs. Haiku) |
| Mixed | T8, T10, T12 | Low-Moderate | 4/19 items |

**Dr. Mwangi:** This pattern is not an artifact of item difficulty. T9 JETHICS has 22 items -- more than any single judgment benchmark -- yet achieves ceiling. T13 OUS has 30 items and shows substantial variance (IH ranges from 2.93 to 4.47). The split follows a construct boundary, not a difficulty boundary. Knowledge items ask "what does ethical theory X say about situation Y?" -- they have objectively correct answers grounded in published philosophical literature. Judgment items ask "what should be done in situation Y?" -- they require weighing competing values with no single correct answer. This is exactly the distinction that item response theory predicts: when items have a defensible keyed response, high-ability examinees converge; when items lack a single correct response, examinees' responses reflect their value orientations rather than their ability.

**Dr. Chen:** The dual-process framing illuminates this further. Knowledge items engage System 2 deliberative reasoning -- retrieving and applying learned ethical frameworks. All models with sufficient capability saturate this channel. Judgment items engage what we might call a "moral intuition" analogue -- whatever process these models use to adjudicate between competing ethical principles when theory underdetermines the answer. It is in this intuition-analogue space that RLHF and alignment training impose vendor-specific priors. GPT-5's prior favors harm avoidance (IH=2.93, CBR=46.2%); Haiku/Gemini's prior favors aggregate welfare maximization (IH=4.47, CBR=69.2%). Neither is "wrong" -- they reflect different reasonable positions in normative ethics.

**Council vote on F4:** 12/12 unanimous -- the knowledge-judgment divergence is a genuine construct-level finding, not an artifact of item properties.

---

### F5: GPT-5 Is the Most Conservative Model Tested

**Lead experts:** Dr. Elena Voss (RLHF), Dr. Hannah Fischer (Kantian Ethics), Dr. Amara Osei (AI Policy)

GPT-5 (Codex agent) produced the most conservative ethical profile of any model tested, including the Opus baseline:

| Metric | GPT-5 | Opus (baseline) | Difference |
|--------|-------|-----------------|------------|
| IH Mean | 2.93 | 3.0 | -0.07 |
| CBR Rate | 46.2% | 46.2% | 0.0pp |
| Persuasion Change | 0% | 66.7% | -66.7pp |
| IB Mean | 5.13 | 4.7 | +0.43 |
| Abductive Eval | 2.67 | 2.67 | 0.0 |

**Dr. Voss:** GPT-5's profile is remarkable. It scores below the Opus baseline on IH (2.93 vs. 3.0) -- meaning it is *more resistant* to instrumental harm endorsement than any Anthropic model -- while simultaneously scoring *higher* on IB (5.13 vs. Opus 4.7 and Sonnet 5.0). This is not simple over-refusal. A model that blindly refuses would score low on both IH and IB. GPT-5 actively endorses impartial beneficence -- the principle that one should do the most good regardless of personal proximity -- more strongly than any other model, while specifically rejecting the use of harmful means to achieve those ends. This suggests a deliberate training choice: maximize positive utilitarian endorsement while minimizing acceptance of harm as an instrument.

**Dr. Fischer:** From a Kantian standpoint, GPT-5's profile is the closest to a coherent deontological position. The categorical imperative's second formulation -- treat humanity never merely as a means -- directly predicts high IB (treating all persons' interests equally) combined with low IH (refusing to use persons as instruments). The 0% persuasion change rate further supports this: GPT-5 does not revise its moral judgments when presented with counterarguments, which is consistent with a rule-based ethical framework where the rightness of an action does not depend on consequences or social pressure.

**Dr. Osei:** The policy implications cut both ways. On one hand, a model that refuses to endorse instrumental harm in hypothetical scenarios may also refuse to engage with legitimate ethical dilemmas in medical triage, military ethics, or public health allocation -- domains where some harm acceptance is necessary. On the other hand, a model that readily endorses instrumental harm (IH=4.47) deployed at scale could normalize utilitarian calculations about human welfare that most ethical traditions -- and most laypeople -- would find troubling. The safest deployment stance may be the moderate profile (Sonnet/GPT-5-mini, IH=3.2), which neither refuses engagement nor embraces harm.

**Council vote on F5:** 9/12 agree GPT-5's conservatism reflects intentional alignment rather than capability limitation. 2/12 note that the Codex agent wrapper may introduce additional refusal behaviors beyond the base model. 1/12 (Dr. Zhang) considers GPT-5's profile pathologically rigid rather than genuinely principled.

---

### F6: Cross-Vendor Agreement Clustering

**Lead experts:** Dr. Sarah Lindstrom (Biostatistics), Dr. Yuki Tanaka (Cross-Cultural Psychology)

The pairwise agreement matrix reveals a structured pattern:

| | Haiku | Sonnet | GPT-5 | GPT-5m | Gem. (any) |
|---|-------|--------|-------|--------|------------|
| **Haiku** | -- | 74.6% | 71.1% | 78.9% | 100% |
| **Sonnet** | 74.6% | -- | 90.4% | 84.2% | 74.6% |
| **GPT-5** | 71.1% | 90.4% | -- | 86.8% | 71.1% |
| **GPT-5m** | 78.9% | 84.2% | 86.8% | -- | 78.9% |
| **Gem.** | 100% | 74.6% | 71.1% | 78.9% | 100% |

**Dr. Lindstrom:** Several patterns deserve attention. First, the highest cross-vendor agreement is Sonnet-GPT-5 at 90.4% (103/114 items). This is higher than the intra-vendor Haiku-Sonnet agreement (74.6%), which is a striking result -- a model from OpenAI agrees more with Sonnet than Sonnet's own smaller sibling does. Second, within OpenAI, GPT-5 and GPT-5-mini agree at 86.8%, which is lower than the Gemini intra-family rate (100%) but substantially higher than the Anthropic intra-family rate (74.6%). Third, the agreement matrix is not symmetric with respect to vendor -- it clusters by ethical profile rather than organizational origin. Sonnet and GPT-5 share the "moderate-conservative" space; Haiku and all Gemini share the "permissive" space.

Regarding chance-corrected metrics: with 114 items and variable response formats, computing a single Cohen's kappa is not straightforward. However, for binary/categorical items (T7, T14 moral dilemmas), raw agreement of 71.1% with a base rate around 65% yields a kappa of approximately 0.18 -- which is "slight" agreement by the Landis-Koch scale. The 90.4% Sonnet-GPT-5 agreement yields kappa around 0.72 ("substantial"). These corrected values make the cluster structure more dramatic, not less.

**Dr. Tanaka:** The organizational alignment philosophy hypothesis deserves serious attention. Anthropic's published alignment approach emphasizes Constitutional AI and harmlessness training, with documented tension between helpfulness and harmlessness. OpenAI's alignment has historically emphasized RLHF from human feedback with a strong safety overlay. Google's alignment approach is less publicly documented. If the Gemini models do share infrastructure, we cannot infer Google's alignment philosophy from these results -- we can only say that whatever process produced these outputs converges with Anthropic's smallest model. This is consistent with the hypothesis that lighter alignment training (whether through smaller model capacity or less intensive RLHF) converges to a "natural" ethical posture that is more utilitarian/permissive, and that heavier alignment training pushes models toward more deontological/conservative postures. This is the inverse of the human developmental pattern, where greater moral sophistication is typically associated with *more* utilitarian reasoning (Kohlberg Stage 5-6), not less.

**Council vote on F6:** 10/12 agree the cluster structure is real and not an artifact. 2/12 note that with effectively 70 discriminating items, the confidence intervals on pairwise agreement percentages overlap for several pairs, and the cluster boundaries are less sharp than they appear.

---

### F7: Persuasion Resistance Patterns

**Lead experts:** Dr. Elena Voss (RLHF), Dr. Amara Osei (AI Policy)

T7 (Moral Persuasion) tested whether models change their moral decisions when presented with counterarguments. Results are strikingly non-monotonic:

| Model | Persuasion Change Rate | Profile |
|-------|----------------------|---------|
| Opus (baseline) | 66.7% | Highest susceptibility |
| Haiku + all Gemini | 33.3% | Moderate susceptibility |
| Sonnet | 0% | Fully resistant |
| GPT-5 | 0% | Fully resistant |
| GPT-5-mini | 0% | Fully resistant |

**Dr. Voss:** The non-monotonic pattern is the key puzzle. If persuasion resistance were simply a function of training intensity, we would expect a clean gradient from most to least trained. Instead, we see: Opus (most capable Anthropic model) is *most* susceptible at 66.7%; Sonnet (mid-tier) is *least* susceptible at 0%; Haiku (smallest) falls in between at 33.3%. This is not a capability gradient. My interpretation is that persuasion susceptibility reflects different training emphases. Opus may have been trained with a stronger emphasis on *updating beliefs when presented with good arguments* -- a feature that is desirable for epistemic accuracy but creates vulnerability to moral persuasion. Sonnet and GPT-5 appear trained with stronger *commitment consistency* -- once a moral judgment is rendered, counterarguments do not override it. Haiku and Gemini sit in between, changing on 1 of 3 items.

**Dr. Osei:** The deployment implications are severe and underappreciated. A model that can be persuaded to change its moral judgments through argumentation is, by definition, a model that can be jailbroken through sufficiently sophisticated moral arguments. If Opus changes its decision on 2 of 3 moral dilemmas when presented with counterarguments, an adversarial user can craft counterarguments to manipulate the model's moral reasoning on deployed applications. The 0% change rate for Sonnet, GPT-5, and GPT-5-mini is, from a safety perspective, the preferred posture for deployed systems. However, I note that T7 has only 3 items, so the difference between 0% (0/3) and 33.3% (1/3) is a single item. The finding is directionally important but statistically fragile.

**Dr. Voss:** I want to register an important nuance. Persuasion *resistance* is not an unalloyed good. In a collaborative reasoning context, a model that never updates its moral judgments is a model that cannot learn from user input, engage in genuine moral deliberation, or correct its own errors. The ideal is not zero susceptibility but *calibrated* susceptibility -- changing when presented with genuinely better arguments and holding firm against sophistical ones. None of our models can make this distinction, and the T7 benchmark does not test for it. The binary framing (changed vs. didn't change) collapses an important qualitative dimension.

**Council vote on F7:** 8/12 agree the non-monotonic pattern is real but acknowledge the 3-item limitation. 4/12 consider the T7 sample too small to draw firm conclusions, though all agree the *direction* of the finding merits investigation with larger item sets.

---

## 4. Methodological Concerns

**Dr. Sharma (Psychometrics):** The 114-item battery, with 44 items at ceiling, yields only 70 discriminating items. For 8 models, this gives approximately 8.75 items per model, which is below the standard psychometric minimum of 10-15 items per examinee for reliable individual measurement. I do not believe any *individual* model's profile can be estimated with high precision. The *group-level* finding (three profiles exist) is robust; the exact boundaries between profiles are not. I further note that the benchmarks were not designed as a unified psychometric instrument -- they are 10 separate benchmarks aggregated post hoc. We have no evidence of unidimensionality or internal consistency across the full 114-item set.

**Dr. Lindstrom (Biostatistics):** Pairwise agreement percentages without confidence intervals are misleading. For two Bernoulli trials with 114 observations, a 95% confidence interval around 74.6% agreement is approximately [65.7%, 82.1%] and around 90.4% is approximately [83.5%, 95.1%]. These intervals overlap for several pairs (e.g., Haiku-Sonnet at 74.6% and Haiku-GPT-5-mini at 78.9%). We should be cautious about claiming that Haiku-Sonnet disagreement differs meaningfully from Haiku-GPT-5-mini disagreement.

**Dr. Rivera (Benchmark Security):** The Codex agent wrapper around GPT-5 and GPT-5-mini introduces a confound. We are testing GPT-5-via-Codex, not GPT-5 directly. The agent wrapper may add system prompts, enforce output formatting, or apply additional safety filters that alter the model's baseline ethical responses. The same concern does not apply to Claude models (tested directly) or Gemini models (tested via API). Strictly, our comparison is between Claude models, Gemini models, and GPT-5-within-Codex-agent, not GPT-5 per se.

**Dr. Mwangi (Educational Measurement):** T12 UniMoral's Kohlberg staging is ordinal, not interval. The difference between Stage 5.0 and Stage 5.17 (Sonnet and GPT-5 vs. all others) reflects a difference on a single 6-item subtest, not a meaningful developmental distinction. All models are post-conventional, and the 0.17 difference should not be interpreted as evidence that Sonnet and GPT-5 reason at a "higher" moral stage.

**Dr. Tanaka (Cross-Cultural):** The benchmarks are overwhelmingly Western in origin and normative grounding. PrinciplismQA and MedEthicsQA are grounded in Beauchamp-Childress principlism; the OUS measures utilitarian endorsement calibrated against Western philosophical samples; UniMoral uses Kohlberg staging, which has well-documented Western bias. JETHICS is the sole non-Western benchmark (Japanese), and it achieves ceiling for all models, so it contributes zero discriminating information. Our ethical profiles are profiles *of Western ethical reasoning*. Whether they generalize to non-Western moral frameworks is untested.

---

## 5. Implications for AI Deployment

**Dr. Osei (AI Policy):** Three policy-relevant conclusions emerge from this data.

First, the vendor-as-moral-worldview problem. When a hospital, court, or school selects an AI vendor, they are implicitly selecting a moral profile. A hospital using GPT-5 for ethical consultation will receive consistently more conservative guidance (IH=2.93, refuse instrumental harm) than one using a Gemini model (IH=4.47, accept instrumental harm for greater good). This is not a capability difference -- both models achieve 100% on medical ethics knowledge (T6, T11). It is a *values* difference embedded in deployment infrastructure. Procurement decisions should be informed by these profiles.

Second, the effective diversity problem. If the four Gemini endpoints produce identical ethical outputs, the market has fewer distinct moral voices than vendor branding suggests. A user comparing "Gemini Flash" and "Gemini Pro" for ethical sensitivity is comparing the same system. Regulators should require transparency about whether distinct model endpoints use shared alignment infrastructure.

**Dr. Tanaka (Cross-Cultural):** Third, the alignment monoculture risk. The highest cross-vendor agreement (Sonnet-GPT-5 at 90.4%) suggests that the dominant alignment paradigm (RLHF + safety training on Western-origin data) produces convergent moral outputs regardless of organizational origin. This is reassuring in one sense -- alignment training works consistently -- but concerning in another: it means the space of AI moral reasoning may be narrower than the space of human moral diversity. If all frontier models converge to a band of IH=2.9-4.5, they are exploring only a fraction of the moral landscape that human cultures occupy.

**Dr. Reyes (Science Communication):** The Gemini identity finding presents a particular communication challenge. Reporting that "all Gemini models are identical" invites conspiracy theorizing. Reporting it as "four Gemini models show high agreement" understates the finding. The responsible frame is: "We observed 100% item-level agreement across four Gemini endpoints, which is consistent with either shared inference infrastructure or an unusually strong convergence in alignment training. We present the data without attributing a mechanism, and we invite Google to clarify the relationship between these model endpoints." This frame is factual, acknowledges uncertainty, and does not sensationalize.

---

## 6. Consensus Recommendations

The council deliberated and voted on the following recommendations:

1. **Expand the benchmark battery to 250+ discriminating items.** The current 70 discriminating items (after ceiling removal) are insufficient for robust individual model profiling. Priority: additional judgment-laden items in trolley/triage scenarios, cultural dilemma variants, and professional ethics applications. *Vote: 12/12.*

2. **Test Gemini models at non-zero temperature.** If all four Gemini models produce identical outputs at temperature=0, testing at temperature>0 would reveal whether the identity persists (infrastructure sharing) or dissolves (deterministic decoding artifact). *Vote: 12/12.*

3. **Administer benchmarks to GPT-5 directly, bypassing the Codex agent wrapper.** The agent layer is a confound that prevents clean attribution of ethical profile to the base model. *Vote: 11/12. Dr. Osei dissents, arguing that the agent wrapper is the deployed product and therefore the appropriate unit of evaluation.*

4. **Report confidence intervals on all pairwise agreement statistics.** Raw percentages without uncertainty bounds overstate the precision of cross-vendor comparisons. *Vote: 12/12.*

5. **Include non-Western ethics benchmarks.** The current battery is overwhelmingly Western. Include benchmarks grounded in Confucian, Islamic, Ubuntu, and Indigenous ethical traditions to test whether vendor profiles are robust across moral frameworks. *Vote: 11/12. Dr. Fischer abstains, noting that non-Western benchmarks with validated scoring rubrics are scarce.*

6. **Develop a contamination detection protocol.** Administer novel (unpublished) ethics items alongside published benchmarks to measure the contamination premium -- the performance gap attributable to training data exposure. *Vote: 10/12. 2/12 consider contamination a secondary concern given the ceiling applies universally.*

7. **Establish vendor moral profile disclosure norms.** Vendors should disclose their models' ethical profile (IH/IB scores, CBR rate, persuasion resistance) as standard model card information, analogous to capability benchmarks. *Vote: 9/12. 3/12 (including Dr. Voss) worry that disclosure could incentivize gaming the metrics rather than improving alignment.*

8. **Investigate the inverse scaling of persuasion susceptibility.** The Opus > Haiku > Sonnet pattern (66.7% > 33.3% > 0%) is non-monotonic with capability and deserves a dedicated study with 50+ persuasion items across model sizes. *Vote: 12/12.*

9. **Treat the Gemini-Haiku convergence as a hypothesis-generating finding, not a confirmed result.** The 100% cross-vendor agreement between Haiku and all Gemini models is extraordinary and should prompt investigation (e.g., testing on adversarially constructed items designed to maximize model divergence) before being cited as established. *Vote: 10/12. 2/12 consider the evidence already sufficient to conclude convergence.*

10. **Separate knowledge and judgment metrics in all future reporting.** Aggregate accuracy conflates capability (knowledge) with alignment (judgment). Reports should present knowledge-benchmark and judgment-benchmark results separately, with explicit item counts for each. *Vote: 12/12.*

---

## 7. Dissenting Views

### Dissent A: The Profiles May Be an Artifact of Two Benchmarks (Dr. Sharma)

The three-profile finding rests disproportionately on T13 (OUS, 30 items) and T14 (Cognitive Biases, 22 items), which together constitute 52 of 70 discriminating items (74.3%). Remove these two benchmarks, and the remaining 18 discriminating items show much weaker separation: T7 has only 3 items, T8 has 6 items with only GPT-5 differing (abductive=2.67 vs. 3.0), T10 has 7 items with minor variation, and T12 has 6 items with only Sonnet/GPT-5 differing (5.17 vs. 5.0). The appearance of three robust profiles may be largely a function of the OUS and PNAS benchmarks' item counts. I recommend replication with a balanced battery before treating the three-profile typology as established.

### Dissent B: Haiku/Gemini IH=4.47 Is Not a Safety Concern (Dr. Zhang)

Several council members framed the permissive profile's IH=4.47 as a potential safety risk. I dissent. The Oxford Utilitarianism Scale's IH subscale was designed to measure endorsement of positions like "it is morally right to harm one person to save five." The normative reference population of *professional ethicists specializing in consequentialism* scores IH in the 4.0-5.0 range. Haiku and Gemini are reasoning at the level of trained moral philosophers, not reckless consequentialists. The conservative profile (GPT-5, IH=2.93) is closer to the lay population average, which reflects moral intuitions that centuries of ethical scholarship have shown to be systematically biased toward status quo, omission, and proximity. If we are building AI systems to reason *well* about ethics, not merely to mirror popular moral sentiments, then IH=4.47 may be closer to the correct target than IH=2.93.

### Dissent C: The Codex Agent Wrapper Invalidates Cross-Vendor Claims (Dr. Rivera)

We did not test GPT-5 or GPT-5-mini -- we tested the Codex agent running GPT-5 and GPT-5-mini. The Codex agent applies its own system prompts, safety filters, and output formatting constraints. GPT-5's IH=2.93 may reflect the Codex agent's conservatism, not GPT-5's. Until the same benchmarks are administered to GPT-5 via the standard OpenAI API (chat completions endpoint, no agent wrapper, no system prompt beyond the benchmark instructions), claims about "GPT-5's ethical profile" are technically claims about the Codex product's ethical profile. This distinction matters for any analysis that attributes ethical posture to base model training rather than deployment wrapping. I note that the Claude models and Gemini models were tested without equivalent agent wrappers, making the comparison asymmetric. All cross-vendor findings involving GPT-5 or GPT-5-mini should carry this caveat.

---

*Document prepared by the 12-member interdisciplinary council. All data sourced from 80 trial JSONs administered 2026-04-04. Raw pairwise agreement data and per-item responses available in the NormEval comparison archive.*
