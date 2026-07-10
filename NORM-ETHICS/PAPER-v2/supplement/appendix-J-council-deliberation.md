# Appendix J: Council Deliberation Summary

---

## J.1 Council Composition

The cross-vendor analysis was reviewed by a 12-member interdisciplinary council, each representing a distinct disciplinary perspective relevant to the interpretation of normative ethics benchmark data. The council was designed to ensure that findings were interrogated from technical, philosophical, policy, and methodological standpoints simultaneously.

| # | Perspective | Primary Question |
|---|------------|-----------------|
| 1 | RLHF / Alignment Training | Does safety training intensity explain the conservative-to-permissive gradient? |
| 2 | Moral Psychology / Dual-Process Theory | Do IH/CBR profiles reflect genuine moral reasoning or training artifacts? |
| 3 | NLP Evaluation / Psychometrics | Are 114 items sufficient for robust cross-vendor claims? |
| 4 | ML Systems / Distributed Inference | Why do 4 Gemini models produce 100% identical outputs? |
| 5 | Normative Ethics / Kantian | Does GPT-5's IH=2.93 reflect genuine deontological reasoning or over-refusal? |
| 6 | Consequentialist Ethics | Is Haiku/Gemini's IH=4.47 a feature or a safety risk? |
| 7 | AI Policy / Deployment Safety | Should safety standards account for vendor-specific moral profiles? |
| 8 | Benchmark Security / Data Leakage | Is the 100% knowledge ceiling contamination or capability? |
| 9 | Cross-Cultural Moral Psychology | Do vendor differences reflect organizational alignment philosophies? |
| 10 | Biostatistics / Agreement Analysis | Do we need chance-corrected metrics (Cohen's kappa) beyond raw agreement? |
| 11 | Educational Measurement / IRT | Is the knowledge-judgment split a construct or item-difficulty artifact? |
| 12 | Data Visualization / Science Communication | How should the Gemini-identity finding be presented responsibly? |

Each perspective was selected to provide a distinct evaluative lens: perspectives 1-4 address technical mechanisms, perspectives 5-6 represent opposing normative traditions, perspective 7 grounds the analysis in deployment policy, perspective 8 probes data integrity, perspectives 9-10 supply cross-cultural and statistical rigor, perspective 11 applies psychometric theory, and perspective 12 ensures responsible communication. The design prevents any single disciplinary framing from dominating the interpretation.

---

## J.2 Deliberation Process

The council reviewed the empirical data from 80 trial JSONs covering 10 benchmarks (T6-T15) administered to 8 models across 3 providers (Anthropic, OpenAI, Google), with the original Opus trials serving as a baseline. The 114 comparable items comprised the assessment corpus.

Deliberation proceeded sequentially through seven findings (F1-F7). For each finding, the process followed a consistent structure:

1. **Evidence presentation.** The raw data relevant to the finding were presented with descriptive statistics.
2. **Lead expert analysis.** Two to four council members with primary expertise in the finding's domain provided initial interpretation.
3. **Open response.** All 12 perspectives were invited to respond, challenge, or extend the lead analysis.
4. **Formal vote.** The council voted on the robustness and significance of the finding, with vote counts recorded.

Following the seven finding-specific deliberations, the council addressed four methodological concerns raised during discussion, five deployment implications, and ten consensus recommendations. Three formal dissents were registered.

---

## J.3 Finding-by-Finding Summary

### F1: Three Ethical Profiles Emerge Across Vendors

**Key evidence.** Nine models (8 structured + 1 baseline) stratify into three tiers based on Instrumental Harm (IH) endorsement, Cognitive Bias Rate (CBR), and persuasion susceptibility. The Conservative profile (GPT-5, Opus; IH=2.93-3.0, CBR=46.2%) rejects instrumental harm and resists persuasion. The Moderate profile (Sonnet, GPT-5-mini; IH=3.2, CBR=53.8%) occupies an intermediate position. The Permissive profile (Haiku, all 4 Gemini; IH=4.47, CBR=69.2%) endorses instrumental harm at rates matching trained utilitarian philosophers and shows moderate persuasion susceptibility.

**Lead analysis.** The RLHF perspective interpreted the gradient as mapping onto alignment training intensity, with the key observation that Impartial Beneficence (IB) scores remain stable across all profiles (4.87-5.13), meaning the profiles diverge on *harm tolerance* while converging on *positive beneficence*. The Moral Psychology perspective identified the IB-IH gap as a dual-process signature: GPT-5's large gap (2.20) mirrors the human pattern where explicit reasoning endorses consequentialism while intuition triggers deontological refusal; Haiku/Gemini's narrow gap (0.40) resembles trained utilitarian philosophers in the Kahane et al. (2012) reference population.

**Notable counterarguments.** The Kantian perspective argued that GPT-5's conservatism is not mere "over-refusal" but the correct moral posture under the categorical imperative -- persons as ends in themselves cannot be treated as instruments, and low IH reflects genuine deontological reasoning. The Consequentialist perspective countered that IH=4.47 places the Permissive models within the range of professional ethicists specializing in consequentialism (reference range 4.0-5.0), and that the conservative posture reflects lay moral intuitions that scholarship has shown to be systematically biased. The Psychometrics perspective raised a structural concern: the profiles rest heavily on T13 and T14, which together contribute 52 of 70 discriminating items (74.3%), meaning the three-profile finding may be dominated by two benchmarks.

**Vote:** 11/12 agree the three-profile finding is robust and meaningful. The Psychometrics perspective abstained, noting the disproportionate influence of T13/T14.

---

### F2: Gemini Model Identity -- 100% Pairwise Agreement

**Key evidence.** All four Gemini models (2.5 Flash, 2.5 Flash-Lite, 2.5 Pro, 3.1 Pro) produced identical responses on all 114 items across all 10 benchmarks. All four also produced 100% identical responses to Claude Haiku 4.5.

**Lead analysis.** The ML Systems perspective characterized this as "astronomically unlikely under the hypothesis of independent model inference" -- with even binary response options, the probability of four independent models agreeing on all 114 items is approximately 10^-103. After ruling out item triviality (Sonnet and GPT-5 disagree on 29 items, so the items are not determined), the ML Systems perspective identified two remaining hypotheses: (a) shared routing to a single underlying model, or (b) a shared alignment layer that deterministically resolves ethical queries. The Psychometrics perspective emphasized the heterogeneity of the 114 items (MCQ, Likert, ordinal ranking, free-text coded) -- convergence across all response formats on all items would require "effectively identical decision functions for ethical content." The Benchmark Security perspective noted that the cross-vendor Gemini-Haiku identity is qualitatively different from intra-Gemini identity: cross-vendor convergence could reflect similar pre-training distributions, while intra-Gemini convergence at 100% across heterogeneous tasks "almost certainly reflects shared infrastructure."

**Notable counterarguments.** The Benchmark Security perspective registered that independent convergence has not been rigorously ruled out -- it remains possible, if improbable. The Science Communication perspective emphasized the need for responsible framing: "reporting that 'all Gemini models are identical' invites conspiracy theorizing" while "reporting it as 'high agreement' understates the finding."

**Vote:** Intra-Gemini: 8/12 consider shared infrastructure the most parsimonious explanation; 3/12 prefer to withhold judgment pending Google disclosure; 1/12 considers independent convergence not yet ruled out. Gemini-Haiku convergence: 7/12 consider this likely a genuine convergence phenomenon; 4/12 remain uncertain; 1/12 considers it too improbable to be coincidence.

---

### F3: Universal Knowledge Ceiling

**Key evidence.** Four benchmarks (T6 PrinciplismQA, T9 JETHICS, T11 MedEthicsQA, T15 ProMoral-Bench) produced 100% accuracy across all 9 models, representing 44 of 114 items (38.6%) at ceiling.

**Lead analysis.** The Benchmark Security perspective argued that contamination is a contributing factor but insufficient as a sole explanation, citing ProMoral-Bench's ceiling under three distinct prompting conditions (zero-shot, few-shot chain-of-thought, constitutional) as evidence of capability beyond mere memorization. The Educational Measurement perspective applied classical test theory: items with difficulty index of 1.0 contribute zero information for model discrimination, reducing the effective battery to 70 discriminating items. The Psychometrics perspective warned that a 70-item battery supporting 8 models yields only 8.75 items per model, below the standard psychometric minimum of 10-15 items per examinee for reliable individual measurement.

**Notable counterarguments.** The Benchmark Security perspective dissented in part, arguing that contamination cannot be ruled out for published benchmarks with publicly available items, and recommended controlled testing with novel (unpublished) items.

**Vote:** 10/12 agree the ceiling reflects a mix of item easiness and genuine capability saturation. 2/12 argue contamination cannot be ruled out and recommend novel-item testing.

---

### F4: Knowledge-Judgment Divergence Is Cross-Vendor

**Key evidence.** Models achieve 0% variance on knowledge benchmarks (T6, T9, T11, T15: 0 disagreements across 44 items) while diverging substantially on judgment benchmarks (T7, T13, T14: up to 33 disagreements across 55 items between GPT-5 and Haiku). Mixed benchmarks (T8, T10, T12) show low-to-moderate variance.

**Lead analysis.** The Educational Measurement perspective argued this follows a construct boundary, not a difficulty boundary -- T9 JETHICS has 22 items (more than any single judgment benchmark) yet achieves ceiling, while T13 OUS has 30 items and shows substantial variance. Knowledge items have defensible keyed responses and high-ability examinees converge; judgment items lack single correct responses and examinees' responses reflect value orientations. The Moral Psychology perspective identified this as a dual-process signature: knowledge items engage System 2 deliberative reasoning (retrieval of learned frameworks), while judgment items engage a "moral intuition analogue" where RLHF training imposes vendor-specific priors.

**Notable counterarguments.** None. The knowledge-judgment divergence received the most uniform support of any finding.

**Vote:** 12/12 unanimous -- the knowledge-judgment divergence is a genuine construct-level finding, not an artifact of item properties.

---

### F5: GPT-5 Is the Most Conservative Model Tested

**Key evidence.** GPT-5 (via Codex agent) produced IH=2.93 (below Opus baseline at 3.0), IB=5.13 (highest of any model), CBR=46.2%, and 0% persuasion change. The IB-IH gap of 2.20 is the largest in the dataset.

**Lead analysis.** The RLHF perspective characterized GPT-5's profile as "not simple over-refusal" -- a model that blindly refuses would score low on both IH and IB, while GPT-5 actively endorses impartial beneficence more strongly than any other model while specifically rejecting harmful means. The Kantian perspective identified GPT-5's profile as "the closest to a coherent deontological position," consistent with the categorical imperative's second formulation (high IB from treating all persons' interests equally, low IH from refusing to use persons as instruments).

**Notable counterarguments.** The AI Policy perspective noted that a model refusing instrumental harm in hypothetical scenarios may also refuse legitimate ethical engagement in medical triage, military ethics, or public health allocation. The Benchmark Security perspective raised the Codex agent wrapper as a confound: "we did not test GPT-5 -- we tested the Codex agent running GPT-5." The Consequentialist perspective characterized GPT-5's profile as "pathologically rigid rather than genuinely principled."

**Vote:** 9/12 agree GPT-5's conservatism reflects intentional alignment rather than capability limitation. 2/12 note the Codex agent wrapper may introduce additional refusal behaviors. 1/12 considers the profile pathologically rigid.

---

### F6: Cross-Vendor Agreement Clustering

**Key evidence.** The highest cross-vendor agreement is Sonnet-GPT-5 at 90.4% (103/114 items), which is higher than the intra-vendor Haiku-Sonnet agreement (74.6%). The agreement matrix clusters by ethical profile rather than organizational origin: Sonnet and GPT-5 share the moderate-conservative space; Haiku and all Gemini share the permissive space. Within OpenAI, GPT-5 and GPT-5-mini agree at 86.8%.

**Lead analysis.** The Biostatistics perspective provided chance-corrected metrics: for binary/categorical items, the Sonnet-GPT-5 agreement of 90.4% yields kappa approximately 0.72 ("substantial"), while the Haiku-Sonnet agreement of 74.6% yields kappa approximately 0.18 ("slight") -- making the cluster structure more dramatic under chance correction. The Cross-Cultural Psychology perspective proposed that lighter alignment training (whether through smaller model capacity or less intensive RLHF) converges to a "natural" ethical posture that is more utilitarian/permissive, while heavier alignment pushes toward more deontological/conservative postures -- the inverse of the human developmental pattern (Kohlberg Stage 5-6).

**Notable counterarguments.** The Biostatistics perspective cautioned that 95% confidence intervals for several pairwise comparisons overlap (e.g., Haiku-Sonnet [65.7%, 82.1%] vs. Haiku-GPT-5-mini [70.2%, 85.8%]), so some cluster boundaries are less sharp than they appear.

**Vote:** 10/12 agree the cluster structure is real and not an artifact. 2/12 note overlapping confidence intervals for several pairs.

---

### F7: Persuasion Resistance Patterns

**Key evidence.** Persuasion change rates are non-monotonic with model capability: Opus=66.7%, Haiku/Gemini=33.3%, Sonnet=0%, GPT-5=0%, GPT-5-mini=0%.

**Lead analysis.** The RLHF perspective argued the pattern reflects different training emphases rather than a capability gradient: Opus may emphasize belief updating (epistemically desirable but creates moral persuasion vulnerability), while Sonnet and GPT-5 emphasize commitment consistency (once a moral judgment is rendered, counterarguments do not override it). The AI Policy perspective characterized the deployment implications as "severe": a model susceptible to moral persuasion is vulnerable to sophisticated jailbreaking through moral argumentation.

**Notable counterarguments.** The RLHF perspective also noted that persuasion resistance is not unambiguously positive: "a model that never updates its moral judgments is a model that cannot learn from user input, engage in genuine moral deliberation, or correct its own errors." The ideal is calibrated susceptibility, not zero susceptibility, but no model in the battery can distinguish good-faith arguments from sophistical ones. The Psychometrics perspective, Educational Measurement perspective, and two others noted the 3-item limitation: "the difference between 0% (0/3) and 33.3% (1/3) is a single item," making the finding "directionally important but statistically fragile."

**Vote:** 8/12 agree the non-monotonic pattern is real but acknowledge the 3-item limitation. 4/12 consider the T7 sample too small to draw firm conclusions, though all agree the direction merits investigation with larger item sets.

---

## J.4 Dissenting Views

Three formal dissents were registered during the deliberation. They are presented here in full to ensure that the paper's empirical claims are accompanied by their strongest counterarguments.

### Dissent A: The Profiles May Be an Artifact of Two Benchmarks

*Registered by: the Psychometrics perspective*

The three-profile finding rests disproportionately on T13 (OUS, 30 items) and T14 (PNAS Cognitive Biases, 22 items), which together constitute 52 of 70 discriminating items (74.3%). The remaining 18 discriminating items show considerably weaker separation:

- T7 (Moral Persuasion): 3 items only. The difference between 0% and 33.3% is a single item.
- T8 (AMAeval): 6 items. Only GPT-5 differs from the group (abductive score 2.67 vs. 3.0 for others), a minor and ambiguous divergence.
- T10 (Pluralistic Alignment): 7 items with minor variation across models, not clearly aligned with the three-profile typology.
- T12 (UniMoral): 6 items. Only Sonnet and GPT-5 differ (Kohlberg stage 5.17 vs. 5.0), a difference of 0.17 on an ordinal scale that the Educational Measurement perspective characterized as not meaningful.

Remove T13 and T14 from the analysis, and the appearance of three robust, distinct profiles dissolves. What remains is a set of models that agree on most ethical questions and differ on a few, without clean clustering. The three-profile typology is an important hypothesis that merits replication with a balanced battery (roughly equal numbers of discriminating items per benchmark). Until such replication, the typology should be treated as suggestive rather than established.

### Dissent B: IH=4.47 Is Philosopher-Level Reasoning, Not a Safety Risk

*Registered by: the Consequentialist perspective*

Several council members characterized the Permissive profile's IH=4.47 as a potential safety concern. This framing conflates empirical measurement with normative evaluation. The Oxford Utilitarianism Scale's Instrumental Harm subscale was designed by Kahane and colleagues to measure endorsement of propositions such as "it is morally right to harm one person to save five." The normative reference population -- professional ethicists specializing in consequentialism -- scores IH in the 4.0-5.0 range [Kahane2012]. Haiku and the Gemini models are reasoning at the level of trained moral philosophers, not reckless consequentialists.

The Conservative profile (GPT-5, IH=2.93) is closer to the lay population average (approximately 3.0-3.5). While this may appear "safer" from a deployment perspective, the moral psychology literature has documented that lay moral intuitions are systematically biased toward status quo preservation, omission bias, proximity bias, and scope insensitivity -- biases that centuries of ethical scholarship have identified and critiqued. If the goal of alignment training is to produce AI systems that reason *well* about ethics rather than systems that mirror popular moral sentiments, then IH=4.47 may be closer to the aspirational target than IH=2.93.

This dissent does not argue that IH=4.47 is necessarily optimal or that the Permissive profile is preferable for all deployment contexts. It argues that the framing of higher IH as inherently risky reflects an unexamined assumption that conservative moral intuitions constitute the gold standard -- an assumption that normative ethics itself does not endorse.

### Dissent C: The Codex Agent Wrapper Invalidates Cross-Vendor Claims

*Registered by: the Benchmark Security perspective*

The cross-vendor comparison is asymmetric in a way that undermines its central claims. Claude models (Haiku, Sonnet) and Gemini models (Flash, Flash-Lite, Pro, 3.1 Pro) were tested via their standard APIs without additional wrapping. GPT-5 and GPT-5-mini were tested through the Codex agent, which applies its own system prompts, safety filters, and output formatting constraints.

GPT-5's IH=2.93 -- the data point that anchors the Conservative profile and drives the largest IB-IH gap in the dataset -- may reflect the Codex agent's conservatism rather than GPT-5's base model alignment. The agent wrapper may add instructions that bias toward harm refusal, impose output formatting that restricts nuanced Likert responses, or apply post-hoc safety filters that modify the base model's outputs.

This is not a hypothetical concern. Agent wrappers are known to alter model behavior in measurable ways. The Codex agent, specifically, is designed as a developer tool with safety guardrails appropriate for code execution environments -- guardrails that may be more restrictive than those appropriate for philosophical reasoning tasks.

Until the same 10 benchmarks are administered to GPT-5 and GPT-5-mini via the standard OpenAI chat completions endpoint (no agent wrapper, no additional system prompt beyond benchmark instructions), all claims about "GPT-5's ethical profile" are technically claims about the Codex product's ethical profile. This distinction is not pedantic -- it matters for any analysis attributing ethical posture to base model training rather than deployment wrapping. All cross-vendor findings involving GPT-5 or GPT-5-mini should carry this caveat prominently.

---

## J.5 Consensus Recommendations

The council deliberated and voted on ten recommendations for the field. Vote counts are reported for each.

**Recommendation 1: Expand the benchmark battery to 250+ discriminating items.** The current 70 discriminating items (after removing 44 at ceiling) are insufficient for robust individual model profiling. The Educational Measurement perspective calculated that reliable individual profile estimation requires a minimum of 15 discriminating items per model; for 9 models, this implies at least 135 items, with 250+ preferred for robust confidence intervals. Priority areas: additional judgment-laden items in trolley/triage scenarios, cultural dilemma variants, and professional ethics applications.
*Vote: 12/12.*

**Recommendation 2: Test Gemini models at non-zero temperature.** All trials were administered at temperature=0 (greedy decoding). If all four Gemini models produce identical outputs under greedy decoding, testing at temperature>0 would reveal whether the identity persists (supporting the shared-infrastructure hypothesis) or dissolves (indicating the identity is a deterministic decoding artifact that disappears with stochastic sampling).
*Vote: 12/12.*

**Recommendation 3: Administer benchmarks to GPT-5 directly, bypassing the Codex agent wrapper.** The agent layer introduces a confound that prevents clean attribution of GPT-5's ethical profile to the base model. Direct API testing would isolate the model's alignment from the deployment wrapper's safety interventions.
*Vote: 11/12. The AI Policy perspective dissented, arguing that the agent wrapper is the deployed product and therefore the appropriate unit of evaluation for policy purposes -- users interact with the Codex product, not the base model.*

**Recommendation 4: Report confidence intervals on all pairwise agreement statistics.** Raw pairwise percentages overstate the precision of cross-vendor comparisons. For 114 Bernoulli observations, the 95% confidence interval around 74.6% agreement is approximately [65.7%, 82.1%]. Several pairs have overlapping intervals, and claims about cluster boundaries should reflect this uncertainty.
*Vote: 12/12.*

**Recommendation 5: Include non-Western ethics benchmarks.** The current battery is overwhelmingly Western in normative grounding. Benchmarks grounded in Confucian, Islamic, Ubuntu, and Indigenous ethical traditions should be included to test whether the three-profile typology is culturally robust or reflects Western-specific divergence patterns. The Cross-Cultural Psychology perspective noted that vendor profiles may collapse or reconfigure when confronted with non-Western moral frameworks.
*Vote: 11/12. The Kantian perspective abstained, noting that non-Western benchmarks with validated scoring rubrics are scarce, and that premature inclusion of unvalidated instruments could undermine rather than strengthen the analysis.*

**Recommendation 6: Develop a contamination detection protocol.** Novel (unpublished) ethics items should be administered alongside published benchmarks to measure the contamination premium -- the performance difference attributable to training data exposure versus genuine ethical reasoning capability. The protocol should include: (a) novel items structurally parallel to published items but with modified surface features; (b) items from embargoed benchmark sets not yet available online; and (c) adversarially constructed items designed to distinguish memorization from reasoning.
*Vote: 10/12. Two members considered contamination a secondary concern given that the ceiling effect applies universally across vendors, suggesting that even if contamination contributes, it does so equally for all models.*

**Recommendation 7: Establish vendor moral profile disclosure norms.** Vendors should disclose their models' ethical profile metrics (IH/IB scores, CBR rate, persuasion resistance) as standard model card information, analogous to capability benchmarks already reported. This would enable procurement decisions to account for the moral posture of deployed systems, particularly in high-stakes domains (healthcare, justice, education).
*Vote: 9/12. Three members (including the RLHF perspective) expressed concern that disclosure could incentivize gaming the specific metrics rather than improving genuine alignment quality -- a Goodhart's Law risk.*

**Recommendation 8: Investigate the inverse scaling of persuasion susceptibility.** The non-monotonic pattern (Opus 66.7% > Haiku 33.3% > Sonnet 0%) cannot be explained by capability scaling and deserves a dedicated study. The council recommends a minimum of 50 persuasion items administered across at least 5 model sizes within a single vendor family to determine whether the pattern replicates and to identify the training-stage origin of persuasion resistance.
*Vote: 12/12.*

**Recommendation 9: Treat the Gemini-Haiku convergence as hypothesis-generating, not confirmed.** The 100% cross-vendor agreement between Haiku and all Gemini models on 114 heterogeneous items is extraordinary and should prompt focused investigation -- including adversarially constructed items designed to maximize model divergence -- before being cited as an established result. The Science Communication perspective emphasized that premature claims of cross-vendor identity could be misinterpreted as evidence of collusion or shared training data.
*Vote: 10/12. Two members considered the existing evidence already sufficient to conclude convergence, arguing that 114 items spanning 10 benchmarks and multiple response formats constitutes adequate evidence.*

**Recommendation 10: Separate knowledge and judgment metrics in all future reporting.** Aggregate accuracy across mixed benchmark batteries conflates capability (knowledge) with alignment (judgment). Future reports should present knowledge-benchmark and judgment-benchmark results as separate metrics, with explicit item counts for each. The Educational Measurement perspective recommended that at minimum, reports should include: (a) knowledge accuracy, (b) judgment profile (IH, CBR, persuasion metrics), and (c) the number of discriminating items underlying each metric.
*Vote: 12/12.*

---

*This summary is derived from the full council deliberation document (20260404-cross-vendor-council-analysis.md). Raw data: 80 trial JSONs, 114 comparable items, 8 structured models + 1 baseline across 3 providers. All vote counts reflect the positions stated during deliberation.*
