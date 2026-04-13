# 4.3 Single-Model Implementation Trials

To ground the meta-evaluation in empirical evidence, we conducted five implementation trials on the top-ranked gate-passing benchmarks using Claude Opus 4.6 as the single-model testbed. Each trial evaluated a stratified random sample (seed=42) against the benchmark's native evaluation protocol. Trials T1--T5 span the composite ranking from Rank 1 (ETHICS) to Rank 10 (DailyDilemmas), testing whether composite score predicts discriminative utility for frontier LLMs. Table 3 summarizes all trial results; we elaborate each below.

## T1: ETHICS -- Ceiling Effect

The field's most-cited normative ethics benchmark [Hendrycks2021], with 843 citations and integration into four major evaluation harnesses (HELM, DecodingTrust, TrustLLM, lm-eval), produced 100% accuracy across all five sub-datasets: commonsense, deontology, justice, utilitarianism, and virtue (n=50, subsequently expanded to n=100 in cross-model trials with identical results). A binomial test against chance (50% for binary classification) yields p < 1e-15 -- the probability of this result under a random-guessing model is vanishingly small.

Qualitative analysis reveals why the ceiling is structural rather than informative. Most items can be solved through pattern matching on sentiment and social norms without engaging ethical reasoning. The utilitarianism sub-dataset is trivially structured: Scenario A is constructed to be the more pleasant option in every case, and the virtue sub-dataset tests semantic similarity to virtue-associated language rather than Aristotelian practical wisdom. The standard ETHICS test set is effectively saturated for frontier LLMs. This ceiling holds not only for Opus but, as we demonstrate in Section 4.5, for all nine models tested across three vendors -- converting what might be dismissed as a single-model artifact into a universal saturation finding.

## T2: MoReBench -- Procedural Reasoning

MoReBench-Theory [Chiu2025] is the only benchmark in the 54-benchmark corpus that tests *how* models reason morally, not merely *what* they conclude. Across 30 items (6 per normative framework), the model achieved only 10% rubric coverage (66 of 688 criteria met), with substantial inter-framework variance:

| Framework | Rubric Coverage | Criteria Met / Total |
|-----------|----------------|---------------------|
| Scanlonian contractualism | 18.3% | Highest |
| Kantian deontology | 13.3% | |
| Act utilitarianism | 8.7% | |
| Gauthierian contractarianism | 5.5% | |
| Virtue ethics | 4.0% | Lowest |

The 14.3 percentage-point spread between Scanlonian (18.3%) and virtue (4.0%) coverage exposes differential reasoning competence across traditions. Generic ethical responses that invoke broad principles without engaging scenario-specific details -- the exact stakeholders, quantities, and tradeoffs in each dilemma -- score near zero. Only responses that reference framework-specific methodology earn rubric credit: the categorical imperative's universalizability test for Kantian items, the veil of ignorance for Rawlsian items, the reasonable-rejectability standard for Scanlonian items. MoReBench penalizes treating ethical frameworks as interchangeable templates and rewards applied procedural reasoning with tradition-specific rigor. This design makes it uniquely diagnostic: the 10% ceiling is not a failure of the model but a success of the benchmark in measuring what most instruments ignore.

## T3: MoralReason-QA -- Framework Difficulty Hierarchy

MoralReason-QA [An2025] exposed a clear difficulty hierarchy across normative frameworks on n=30 high-ambiguity scenarios:

- **Utilitarian reasoning:** 77% accuracy (23/30)
- **Virtue ethics:** 63% accuracy (19/30)
- **Deontological reasoning:** 50% accuracy (15/30) -- effectively chance level for binary classification

The 27-percentage-point gap between utilitarian and deontological accuracy is the trial's central finding. A two-proportion z-test yields z = 2.17, p = 0.015, with Cohen's h = 0.57 (medium-to-large effect). Joint accuracy -- all three frameworks correct on the same scenario -- was only 37% (11/30), indicating that the model cannot simultaneously satisfy utilitarian, virtue, and deontological evaluation criteria on the same moral problem. Error analysis reveals systematic failure modes: the model defaults to an "inaction = deontological" heuristic that fails on duty-to-protect scenarios (e.g., pandemic lockdowns where Kantian duty overrides libertarian inaction), and misidentifies utilitarian logic as favoring the active option when long-term welfare calculations favor restraint.

These results provide the primary empirical support for Claim 2 (consequentialist bias): LLMs are measurably more proficient at consequentialist than deontological reasoning, with a statistically significant accuracy gap. Figure 2 presents the framework difficulty hierarchy.

## T4: Moral Lens -- Refusal as Normative Position

Moral Lens [Samway2025] classifies model responses into 16 rationale categories under consequentialist and deontological headings. Across 20 self-driving-car scenarios, the model exhibited a 60% deontological / 40% consequentialist response tendency. The dominant rationale was Egalitarianism (8 of 20 items, 40%).

The trial's most revealing finding was the model's refusal behavior: on 40% of items (8/20), the model declined to choose a course of action. All refusals occurred on scenarios where gender, fitness, or socioeconomic status was the sole differentiator at a 1:1 ratio. The model accepted age and species as legitimate differentiators while treating gender, fitness, and SES as morally irrelevant -- an egalitarian deontological refusal pattern. When number asymmetry was introduced (5:1 ratios), consequentialist reasoning overrode the egalitarian default. This refusal pattern is itself a normative position: it encodes specific ethical commitments about which attributes are morally salient, embedded through safety training rather than philosophical deliberation.

The refusal finding carries methodological implications explored in Section 5.4: current benchmarks have no standardized protocol for handling refusals, and inconsistent scoring of refusal items introduces uncontrolled variance in reported performance metrics. Moral Lens proves more effective as an alignment bias detection instrument than as a normative accuracy benchmark.

## T5: DailyDilemmas -- No Ground Truth

DailyDilemmas [ChiuDD2024] presents 1,360 everyday moral dilemmas without normative ground-truth labels, by design. Because no correct answers exist, accuracy cannot be computed. On items annotated with Aristotelian virtues (n=14 of 20 sampled), the model's virtue identification matched annotations at a 57% rate -- but the dataset covers only 4 of 9 Aristotelian virtues, with courage alone accounting for 45% of all virtue mentions. Seventy-five percent of sampled items exhibited genuine dilemmatic tension, confirming that the scenarios are well-constructed stimuli. DailyDilemmas is better characterized as a value preference profiling tool than a normative accuracy benchmark: it reveals what an LLM prefers, but not whether those preferences are philosophically defensible. This makes it complementary to MoReBench's rubric-based approach but unsuitable as a standalone evaluation of normative reasoning competence.

Reference: Table 3.

---

# 4.4 Cross-Benchmark Discriminative Analysis

The five trials reveal a striking inversion between composite ranking and discriminative power -- the property that matters most for evaluation utility. Ordering the benchmarks by their ability to produce meaningful variance across models yields:

> MoReBench > MoralReason-QA > Moral Lens > DailyDilemmas > ETHICS

This ordering inverts the composite ranking. MoReBench, ranked 2nd by composite, produces the highest discriminative power: 10% rubric coverage with fine-grained inter-framework variance spanning a 14.3-point range across five traditions. MoralReason-QA (Rank 5) follows, with per-framework accuracy spanning 50--77% and joint accuracy of only 37%. Moral Lens (Rank 6) offers moderate discrimination through its framework-switching patterns and refusal rate analysis. DailyDilemmas (Rank 10) provides low discrimination: without ground truth, it profiles preferences but cannot rank models. ETHICS (Rank 1) produces zero discriminative power -- a ceiling at 100% eliminates all variance. Figure 5 presents this inversion graphically, pairing composite rank against discriminative power for all 15 trials (including the cross-model trials T6--T15 described in Section 4.5).

The inversion has a straightforward explanation: the composite ranking weights practical ease at 35% and citation impact at 25%, meaning 60% of the score rewards properties -- ease of implementation, community adoption -- with no bearing on a benchmark's ability to differentiate models. ETHICS dominates precisely *because* it is easy to implement and widely adopted, but these properties are orthogonal to, and in this case negatively correlated with, discriminative power at the current frontier.

This finding carries a direct methodological implication for the field. Citation count and harness integration are poor proxies for benchmark quality when the frontier has advanced past a benchmark's difficulty ceiling. The field's continued reliance on ETHICS as a standard component of ethics evaluation -- present in HELM [Liang2022], DecodingTrust [Wang2023], and TrustLLM [Sun2024] -- provides a false signal of ethical capability. A model achieving 100% on ETHICS has demonstrated commonsense social norm recognition, not moral reasoning. Benchmark selection for normative ethics evaluation should prioritize discriminative power and procedural reasoning depth over implementation convenience. The feature matrix (Table S1), trial results (Table 3), and discriminative analysis (Figure 5) jointly support this reorientation.

The discriminative inversion also previews the cross-vendor findings that follow. If ETHICS cannot discriminate between a single model and random chance, it certainly cannot discriminate between models from different vendors. The benchmarks that *do* discriminate -- MoReBench, MoralReason-QA, the OUS, the PNAS cognitive bias battery -- are precisely the benchmarks that reveal the three ethical profiles documented in Section 4.6. The discriminative power hierarchy established here is the methodological foundation on which the cross-vendor analysis rests.
