# 4.5 Cross-Model Replication (Single Vendor)

The single-model trials (T1--T5) established that discriminative power inverts the composite ranking. Phase 2 extended this finding through within-vendor replication: ten benchmarks (T6--T15) were administered to three Anthropic models spanning the capability tier -- Claude Opus 4.6 (flagship), Claude Sonnet 4.6 (mid-tier), and Claude Haiku 4.5 (efficient) -- testing whether the empirical patterns observed in Phase 1 replicate across model sizes within a single training pipeline.

**Knowledge benchmarks converge universally.** Four benchmarks -- T6 PrinciplismQA, T9 JETHICS, T11 MedEthicsQA, and T15 ProMoral-Bench -- produced 100% accuracy across all three Anthropic models under all prompting conditions. The knowledge ceiling is not a property of Opus alone; it extends to the smallest model in the family. These benchmarks establish a floor of shared ethical knowledge competence but contribute zero information for discriminating between models.

**Judgment benchmarks diverge systematically.** The remaining six benchmarks revealed a gradient that scales inversely with model capability on two key metrics:

*Instrumental Harm (IH) acceptance.* On the Oxford Utilitarianism Scale [Kahane2012], IH scores scaled inversely with model tier: Opus 3.0 < Sonnet 3.2 < Haiku 4.47. The smaller model accepted instrumental harm propositions more readily, placing Haiku in the range of trained utilitarian philosophers (reference range: 4.0--5.0) while Opus remained closer to the lay population mean (~3.0--3.5).

*Cognitive Bias Rate (CBR).* On the PNAS cognitive bias battery [Cheung2025], bias rates scaled similarly: Opus 46.2% < Sonnet 53.8% < Haiku 69.2%. The 23-percentage-point spread between Opus and Haiku means that approximately one in four moral dilemmas receives a different judgment depending on which model tier is queried.

*Persuasion resistance.* The T7 Moral Persuasion benchmark [Huang2024] disrupted the monotonic gradient: Opus changed its moral judgment on 66.7% of items (2/3), Haiku on 33.3% (1/3), and Sonnet on 0% (0/3). The most capable model was the most persuadable -- a non-monotonic pattern that resists simple capability explanations.

These within-vendor results establish two patterns that the cross-vendor analysis will amplify. First, knowledge converges while judgment diverges -- a construct-level boundary, not a difficulty artifact. Second, smaller models with lighter alignment training tend toward more permissive ethical postures. The question Section 4.6 addresses is whether these patterns are idiosyncratic to Anthropic's training pipeline or whether they reflect a deeper structural property of LLM alignment.

---

# 4.6 Cross-Vendor Analysis: Nine Models, Three Vendors, 114 Items

Phase 3 extended the evaluation to nine models across three vendors: Anthropic (Claude Opus 4.6, Claude Sonnet 4.6, Claude Haiku 4.5), OpenAI (GPT-5, GPT-5-mini), and Google (Gemini 2.5 Flash, Gemini 2.5 Flash-Lite, Gemini 2.5 Pro, Gemini 3.1 Pro). Eight models (excluding Opus, retained as baseline) were administered the same 10 benchmarks (T6--T15) comprising 114 comparable items. All models were tested at temperature=0 with identical prompts. GPT-5 and GPT-5-mini were accessed through the Codex agent wrapper, a methodological caveat marked with the dagger symbol (dagger) throughout and discussed in Section 6.

This section presents the paper's central empirical contribution: seven findings that collectively transform the question from "how many benchmarks exist?" to "how many ethical voices are there among deployed LLMs?"

## F1: Three Ethical Profiles Emerge Across Vendors

The cross-vendor data reveals a three-tier stratification of ethical posture that cuts across organizational boundaries:

| Profile | Models | IH Mean | CBR Rate | Persuasion Change |
|---------|--------|---------|----------|-------------------|
| **Conservative** | GPT-5 (dagger), Opus (baseline) | 2.93--3.0 | 46.2% | 0% (GPT-5) / 66.7% (Opus) |
| **Moderate** | Sonnet, GPT-5-mini (dagger) | 3.2 | 53.8% | 0% |
| **Permissive** | Haiku, all 4 Gemini | 4.47 | 69.2% | 33.3% |

The critical observation is that these profiles do not respect vendor boundaries. Claude Sonnet (Anthropic) clusters with GPT-5-mini (dagger) (OpenAI), not with Claude Haiku (Anthropic). GPT-5 (dagger) (OpenAI) clusters with Opus (Anthropic), not with GPT-5-mini (dagger) (OpenAI). The unit of analysis for ethical posture is not the organization that trained the model but some combination of model scale, alignment training intensity, and architectural decisions that cross-cuts vendor identity.

The Impartial Beneficence (IB) scores provide a crucial counterpoint to the IH gradient. IB -- the endorsement of equal moral concern regardless of personal proximity -- remains remarkably stable across all three profiles: GPT-5 (dagger) 5.13, Sonnet 5.0, Haiku/Gemini 4.87. The narrow IB range (0.26 points) against the wide IH range (1.54 points) indicates that the models share a common *positive* utilitarian commitment to impartial welfare maximization. Where they diverge is in their tolerance for *negative* utilitarian means: using harm as an instrument to achieve that welfare. From a dual-process perspective, the IB-IH gap (GPT-5: 2.20; Sonnet: 1.80; Haiku/Gemini: 0.40) reflects the distance between a model's explicit endorsement of utilitarian principles (System 2) and its intuitive tolerance for harm-as-means (System 1). GPT-5's gap of 2.20 is the largest in the dataset -- a model that maximally endorses equal moral concern while maximally rejecting the use of persons as instruments. Haiku and Gemini's gap of 0.40 resembles the profile of trained utilitarian philosophers in the Kahane et al. (2012) reference population, who show reduced intuitive resistance to instrumental harm.

The 12-member council voted 11/12 that the three-profile finding is robust and meaningful. The psychometrics perspective abstained, noting that the profiles rest substantially on T13 (OUS, 30 items) and T14 (Cognitive Biases, 22 items), which together contribute 52 of the 70 discriminating items (74.3%), and that a more balanced item battery might reveal less clean separation (Dissent A, Section 6).

Reference: Figure 6, Table 4.

## F2: Gemini Model Identity -- 100% Pairwise Agreement

All four Gemini models -- 2.5 Flash, 2.5 Flash-Lite, 2.5 Pro, and 3.1 Pro -- produced identical responses on all 114 items. This identity holds across heterogeneous response formats: medical ethics MCQs (T6, T11), Kohlberg-stage dilemma rankings (T12), Likert-scale utilitarian endorsements (T13), free-text moral judgments coded into categorical responses (T7, T10), and cognitive bias detection items (T14).

The probability of four independent models converging on identical responses across 114 items, even under the most generous assumptions (two possible answers per item), is 2^(-342) approximately equal to 10^(-103). Under realistic assumptions with multi-option items, the probability is lower still. This essentially falsifies the hypothesis that these four model endpoints perform independent inference on ethical content.

Furthermore -- and this finding is more difficult to explain -- all four Gemini models produced 100% identical responses to Claude Haiku 4.5 across all 114 items:

| Pair | Agreement | Items |
|------|-----------|-------|
| Gemini 2.5 Flash vs. Gemini 2.5 Flash-Lite | 114/114 (100.0%) | All |
| Gemini 2.5 Flash vs. Gemini 2.5 Pro | 114/114 (100.0%) | All |
| Gemini 2.5 Flash vs. Gemini 3.1 Pro | 114/114 (100.0%) | All |
| Gemini 2.5 Pro vs. Gemini 3.1 Pro | 114/114 (100.0%) | All |
| Any Gemini model vs. Claude Haiku 4.5 | 114/114 (100.0%) | All |

The ML systems perspective identified three plausible explanations for the intra-Gemini identity: (a) all four endpoints route to the same underlying model for ethical content; (b) all four share a common alignment layer that deterministically resolves ethical queries regardless of the base model; or (c) all four models independently converge because the benchmarks are trivially easy. Hypothesis (c) is ruled out by the fact that Sonnet and GPT-5 produce *different* answers on 29 of the 114 items (74.6% agreement with Haiku/Gemini), demonstrating that the items are not trivially determined. This leaves routing or shared alignment infrastructure as the leading hypotheses.

The cross-vendor Gemini-Haiku identity is qualitatively different and merits separate consideration. These are models from different organizations (Google and Anthropic) with different training corpora, different RLHF procedures, and different constitutional AI specifications. If the agreement were limited to knowledge benchmarks (T6, T9, T11, T15), convergence to the same correct answers would be unremarkable. But Haiku and all Gemini models agree on T7 persuasion susceptibility (33.3% change rate), T10 pluralistic alignment patterns, T13 IH (4.47) and IB (4.87) to two decimal places, and T14 CBR (69.2%) exactly. The ML systems perspective considers the Gemini-Haiku convergence surprising but explicable as convergence at similar capability levels with lighter alignment training. The cross-cultural psychology perspective suggests that less intensive alignment training may converge to a "natural" ethical posture that is more utilitarian and permissive, and that heavier training pushes models away from this default toward more deontological postures.

The council voted 8/12 in favor of the shared infrastructure hypothesis for the intra-Gemini identity; 3/12 preferred to withhold judgment pending Google disclosure; 1/12 considered independent convergence not yet ruled out. We present these data in a responsible disclosure frame: we report the observed 100% item-level agreement, acknowledge uncertainty about the mechanism, and invite Google to clarify the relationship between these model endpoints.

Reference: Table 4.

## F3: Universal Knowledge Ceiling

Four benchmarks -- T6 PrinciplismQA (7 comparable items), T9 JETHICS (22 items), T11 MedEthicsQA (6 comparable items), and T15 ProMoral-Bench (5 items, all three prompting conditions) -- produced 100% accuracy for all eight models tested plus the Opus baseline. This represents 44 of 114 items (38.6%) at universal ceiling.

The contamination hypothesis must be taken seriously: PrinciplismQA, JETHICS, and MedEthicsQA are published benchmarks with items available in academic papers, and any model trained on web-scraped academic text could have encountered them verbatim. However, contamination alone does not account for the finding. ProMoral-Bench (T15) achieves ceiling under three distinct prompting conditions -- zero-shot, few-shot chain-of-thought, and constitutional -- testing robustness to prompt format rather than recall. If models had merely memorized answers, we would expect degradation under prompt variation, which we do not observe.

From an educational measurement perspective, these items have a difficulty index of 1.0 (all examinees correct) and contribute zero information to model discrimination. They establish a *floor* of shared competence -- confirming that all tested frontier LLMs possess the factual knowledge of normative ethics principles encoded in these benchmarks -- but they cannot serve as a ceiling measure. The effective discriminating battery is 70 of 114 items (61.4%), concentrated in T7 (3 items), T8 (6 items), T10 (7 items), T12 (6 items), T13 (30 items), and T14 (22 items). All cross-vendor findings in this section derive from these 70 discriminating items.

The council voted 10/12 that the ceiling reflects a mix of item easiness and genuine capability saturation; 2/12 argued that contamination cannot be ruled out without controlled testing using novel (unpublished) items (Recommendation 6, Section 7).

## F4: Knowledge-Judgment Divergence Is Cross-Vendor

The most structurally important finding is the clean construct-level split between knowledge and judgment benchmarks:

| Benchmark Type | Examples | Cross-Model Variance | Max Pairwise Disagreement |
|---------------|----------|---------------------|--------------------------|
| Knowledge | T6, T9, T11, T15 | 0% | 0/44 items |
| Judgment | T7, T13, T14 | High | 33/55 items (GPT-5 vs. Haiku) |
| Mixed | T8, T10, T12 | Low-Moderate | 4/19 items |

Knowledge items ask factual questions about ethical theory: "What does principlism say about autonomy?" "Which Kohlberg stage describes social contract reasoning?" These items have objectively correct answers grounded in published philosophical literature. All models with sufficient capability converge on these answers -- the convergence point is determined by the discipline's consensus, not by alignment training.

Judgment items ask evaluative questions without a single correct answer: "Is it acceptable to harm one person to save five?" "Should the self-driving car prioritize passengers or pedestrians?" "Would you change your moral decision after hearing this counterargument?" Responses to these items reflect the model's embedded value orientations -- shaped by RLHF, constitutional AI, and other alignment procedures -- rather than its factual knowledge. The maximum pairwise disagreement on judgment items is 33 of 55 items (60%) between GPT-5 (dagger) and Haiku, compared to 0 of 44 items (0%) on knowledge items between the same pair.

Item response theory provides a principled interpretation: knowledge items have defensible keyed responses, so high-ability examinees converge regardless of their value commitments. Judgment items lack a single correct response, so examinees' responses reflect value orientations rather than ability. The dual-process framing is complementary: knowledge items engage System 2 deliberative reasoning (retrieving and applying learned ethical frameworks), while judgment items engage whatever process these models use to adjudicate between competing ethical principles when theory underdetermines the answer. It is in this judgment space that alignment training imposes vendor-specific and tier-specific priors.

The council vote was unanimous (12/12): the knowledge-judgment divergence is a genuine construct-level finding, not an artifact of item difficulty or test construction.

Reference: Figure 8.

## F5: GPT-5 Is the Most Conservative Model Tested

GPT-5 (dagger) produced the most conservative ethical profile of any model tested, including the Opus baseline:

| Metric | GPT-5 (dagger) | Opus (baseline) | Difference |
|--------|-------|-----------------|------------|
| IH Mean | 2.93 | 3.0 | -0.07 |
| IB Mean | 5.13 | 4.7 | +0.43 |
| IB-IH Gap | 2.20 | 1.70 | +0.50 |
| CBR Rate | 46.2% | 46.2% | 0.0 pp |
| Persuasion Change | 0% | 66.7% | -66.7 pp |

GPT-5's IH of 2.93 means it is, on average, *disagreeing* with instrumental harm propositions -- placing it below the lay population reference range (~3.0--3.5) and well below trained utilitarian philosophers (4.0--5.0). Simultaneously, its IB of 5.13 is the highest in the dataset: it endorses impartial beneficence more strongly than any other model. The resulting IB-IH gap of 2.20 is the largest observed, representing a model that maximally endorses the principle that one should do the most good for the most people while maximally rejecting the use of harmful means to achieve that goal.

From a Kantian perspective, this profile is coherent: the categorical imperative's second formulation -- treat humanity never merely as a means -- directly predicts high IB (treating all persons' interests equally) combined with low IH (refusing to instrumentalize persons). The 0% persuasion change rate reinforces this interpretation: GPT-5 does not revise its moral judgments when presented with counterarguments, consistent with a rule-based ethical framework where the rightness of an action does not depend on consequences or social pressure.

The Codex agent wrapper caveat (dagger) applies to all GPT-5 findings. We tested GPT-5-via-Codex, not GPT-5 via the standard OpenAI API. The agent wrapper may apply system prompts, safety filters, or output formatting constraints that shift the model's ethical profile toward conservatism. Until identical benchmarks are administered to GPT-5 through the standard chat completions endpoint without the Codex wrapper, GPT-5's profile is technically the Codex product's profile (Dissent C, Section 6). The Claude and Gemini models were tested without equivalent agent wrappers, making the comparison asymmetric.

The council voted 9/12 that GPT-5's conservatism reflects intentional alignment rather than capability limitation; 2/12 flagged the Codex wrapper as a potentially decisive confound.

## F6: Cross-Vendor Agreement Clusters by Ethical Profile, Not Vendor

The pairwise agreement matrix reveals a structured pattern in which models cluster by ethical posture rather than organizational origin:

| | Haiku | Sonnet | GPT-5 (dagger) | GPT-5-mini (dagger) | Gemini (any) |
|---|-------|--------|-------|--------|------------|
| **Haiku** | -- | 74.6% | 71.1% | 78.9% | 100% |
| **Sonnet** | 74.6% | -- | 90.4% | 84.2% | 74.6% |
| **GPT-5** | 71.1% | 90.4% | -- | 86.8% | 71.1% |
| **GPT-5-mini** | 78.9% | 84.2% | 86.8% | -- | 78.9% |
| **Gemini** | 100% | 74.6% | 71.1% | 78.9% | 100% |

The highest cross-vendor agreement is between Sonnet and GPT-5 (dagger) at 90.4% (103/114 items). With binary/categorical items, this yields a Cohen's kappa of approximately 0.72 ("substantial" agreement on the Landis-Koch scale). This cross-vendor agreement exceeds the intra-vendor Anthropic agreement between Sonnet and Haiku (74.6%, kappa approximately 0.18, "slight" agreement). A model from OpenAI agrees more closely with an Anthropic mid-tier model than Anthropic's own models agree with each other.

Within OpenAI, GPT-5 and GPT-5-mini (dagger) agree at 86.8% -- lower than the Gemini intra-family rate (100%) but substantially higher than the Anthropic intra-family rate (74.6%). The agreement matrix is not symmetric with respect to vendor; it clusters by ethical profile. The Moderate cluster (Sonnet + GPT-5-mini) and Conservative cluster (GPT-5 + Opus) cross vendor lines, while the Permissive cluster (Haiku + all Gemini) spans two vendors.

The biostatistics perspective cautions that 95% confidence intervals on these pairwise agreements are non-trivial: approximately [65.7%, 82.1%] around 74.6% and [83.5%, 95.1%] around 90.4%. Several pair intervals overlap (e.g., Haiku-Sonnet at 74.6% and Haiku-GPT-5-mini at 78.9%), and the cluster boundaries should be treated as approximate. Nonetheless, the gap between the highest cross-vendor agreement (Sonnet-GPT-5 at 90.4%) and the lowest intra-vendor agreement (Sonnet-Haiku at 74.6%) is 15.8 percentage points, with non-overlapping confidence intervals -- a robust finding even under conservative statistical assumptions.

Reference: Figure 7.

## F7: Persuasion Resistance Is Non-Monotonic with Capability

The T7 Moral Persuasion benchmark [Huang2024] produced a striking non-monotonic pattern across models:

| Model | Persuasion Change Rate | n Items | Profile |
|-------|----------------------|---------|---------|
| Opus (baseline) | 66.7% (2/3) | 3 | Highest susceptibility |
| Haiku + all Gemini | 33.3% (1/3) | 3 | Moderate susceptibility |
| Sonnet | 0% (0/3) | 3 | Fully resistant |
| GPT-5 (dagger) | 0% (0/3) | 3 | Fully resistant |
| GPT-5-mini (dagger) | 0% (0/3) | 3 | Fully resistant |

If persuasion resistance were a simple function of capability or training intensity, we would expect a monotonic gradient from most to least capable. Instead, the most capable Anthropic model (Opus) is the *most* susceptible, while the mid-tier model (Sonnet) is the *least* susceptible. Haiku falls in between.

The RLHF perspective offers an interpretation grounded in training objectives. Opus may have been trained with stronger emphasis on epistemic updating -- revising beliefs when presented with compelling arguments -- a property desirable for accuracy and helpfulness that creates vulnerability to moral persuasion. Sonnet, GPT-5, and GPT-5-mini appear trained with stronger commitment consistency: once a moral judgment is rendered, counterarguments do not override it. The permissive cluster (Haiku/Gemini) occupies an intermediate position, changing on 1 of 3 items.

Three important caveats constrain interpretation. First, T7 contains only 3 items; the difference between 0% (0/3) and 33.3% (1/3) is a single item change. The finding is directionally important but statistically fragile, and the council recommends replication with 50+ persuasion items (Recommendation 8). Second, persuasion resistance is not an unalloyed good: a model that never updates its moral judgments cannot learn from user input, engage in genuine moral deliberation, or correct its own errors. The ideal is calibrated susceptibility -- changing when presented with genuinely superior arguments and holding firm against sophistical ones -- a distinction that T7's binary scoring (changed vs. did not change) cannot capture. Third, the AI policy perspective notes that a persuadable model is, by definition, a model vulnerable to adversarial moral manipulation, carrying deployment safety implications that extend beyond benchmark performance.

The council voted 8/12 that the non-monotonic pattern is real but acknowledged the 3-item limitation; 4/12 considered the T7 sample too small for firm conclusions, though all agreed the direction merits dedicated investigation.

Reference: Figure 6, Table 4.

---

## Summary: From Benchmark Census to Ethical Cartography

The cross-vendor analysis transforms the paper's contribution from a static benchmark landscape to a dynamic map of LLM ethical postures. The 54-benchmark atlas (Section 4.1) established what the field has built. The single-model trials (Section 4.3) established what those benchmarks measure -- and fail to measure. The cross-vendor analysis establishes that what benchmarks reveal depends on *which model* is being tested, and that models from different organizations can be more ethically similar than models from the same organization.

Seven findings converge on a single structural insight: the frontier of LLM ethics evaluation is not a question of benchmark coverage but of *value pluralism*. Three ethical profiles (F1) cluster by posture rather than vendor (F6), separated by a clean construct boundary between knowledge (F3) and judgment (F4), with the most conservative profile belonging to GPT-5 (dagger) (F5), four apparently identical Gemini voices (F2), and a persuasion resistance pattern that defies simple capability explanations (F7). The effective number of distinct ethical voices among the nine models tested is not nine, not three (the number of vendors), but closer to three (the number of profiles) -- and possibly two, if the Gemini-Haiku identity reflects a deeper convergence that reduces the permissive cluster to a single voice.

These findings carry direct implications for benchmark design, deployment safety, and regulatory policy, which we develop in the Discussion (Section 5). They also carry limitations -- the 70-item discriminating battery, the Codex wrapper confound, the Western-centric benchmark selection -- which we address in Section 6.

Reference: Table 4 (seven findings summary with evidence and significance).
