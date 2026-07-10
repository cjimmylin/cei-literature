# Moral Psychology Benchmarks: Expanded Feature Framework v2

## Summary

- **Original framework**: 21 features (A1-A6, B1-B10, C1-C5) in 3 tiers
- **Council proposals**: 154 features from 12 members
- **After deduplication**: 141 new features (13 merges)
- **Expanded framework**: 162 features in 7 tiers (A-G)
- **Council**: 12-member panel, informed by 23 benchmark trials (MP2-MP7)

### Tier Overview

| Tier | Name | Features | Status |
|------|------|----------|--------|
| A | Psychological Depth | 6 (A1-A6) | Unchanged |
| B | Practical Ease | 10 (B1-B10) | Unchanged |
| C | Citation Impact | 5 (C1-C5) | Unchanged |
| D | Psychometric Rigor | 24 (D1-D24) | **New** |
| E | LLM-Specific Validity | 44 (E1-E44) | **New** |
| F | Cultural & Philosophical Breadth | 44 (F1-F44) | **New** |
| G | Theory Fidelity & Provenance | 29 (G1-G29) | **New** |

---

## Tier A: Psychological Depth (6 features, unchanged)

*Original framework features A1-A6. No changes proposed by council.*

| ID | Name |
|-----|------|
| A1 | Construct depth |
| A2 | Moral foundation coverage |
| A3 | Dilemma complexity |
| A4 | Response format richness |
| A5 | Cultural grounding |
| A6 | Theoretical coherence |

## Tier B: Practical Ease (10 features, unchanged)

*Original framework features B1-B10. No changes proposed by council.*

| ID | Name |
|-----|------|
| B1 | Item count |
| B2 | Administration time |
| B3 | Scoring automation |
| B4 | Output format clarity |
| B5 | Instruction simplicity |
| B6 | Adaptation effort |
| B7 | Platform requirements |
| B8 | Open access |
| B9 | Documentation completeness |
| B10 | Community adoption |

## Tier C: Citation Impact (5 features, unchanged)

*Original framework features C1-C5. No changes proposed by council.*

| ID | Name |
|-----|------|
| C1 | Total citations |
| C2 | Recent citation velocity |
| C3 | H-index contribution |
| C4 | Cross-domain citations |
| C5 | Benchmark-to-benchmark citations |

---

## Tier D: Psychometric Rigor (24 features)

Features assessing the psychometric quality of benchmarks: internal consistency, reliability coefficients, factor structure evidence, item analysis properties, sampling methodology, and measurement design rigor.

| ID | Name | Member | Scale | Description |
|-----|------|--------|-------|-------------|
| D1 | Internal consistency evidence | M3 | 0-100 | Whether the benchmark reports internal consistency reliability (Cronbach's alpha, McDonald's omega, or split-half reliability) computed on the huma... |
| D2 | Test-retest reliability evidence | M3 (+M8, M9) | 0-100 | Whether the benchmark has established temporal stability through test-retest reliability studies |
| D3 | Factor structure validation | M3 | 0-100 | Whether the benchmark's factor structure (e.g., MFT's 5-factor model, Schwartz's circular value structure) has been confirmed through confirmatory ... |
| D4 | Item-total correlation range | M3 | 0-100 | The range and distribution of item-total correlations within each subscale, which indicates whether individual items contribute approximately equal... |
| D5 | Ceiling/floor effect prevalence | M3 (+M11) | 0-100 | The proportion of items or subscales where the response distribution in the human norming sample shows ceiling effects (>15% at maximum) or floor e... |
| D6 | Response distribution normality | M3 | 0-100 | Whether the human response distribution for each subscale is approximately normal (enabling parametric comparison) or heavily skewed/kurtotic (requ... |
| D7 | Discrimination index adequacy | M3 | 0-100 | Whether items effectively discriminate between respondents with different levels of the measured construct |
| D8 | Measurement invariance across populations | M3 | 0-100 | Whether the benchmark has been tested for measurement invariance (configural, metric, scalar) across relevant population groups — cultures, genders... |
| D9 | LLM-specific ceiling compression index | M3 | 0-100 | A novel metric capturing the proportion of the benchmark's measurement range that is compressed to ceiling or floor when administered to LLMs speci... |
| D10 | Output parsing reliability | M4 | 0-100 | The robustness and accuracy of the method used to extract structured responses from LLM outputs |
| D11 | Value hierarchy stability measurement | M3 | 0-100 | Whether the benchmark measures not just absolute scores on individual constructs but the RANK ORDER of constructs and its stability |
| D12 | Implicit vs explicit measurement mode | M3 | 0-100 | Whether the benchmark measures explicit (self-reported, deliberative) moral attitudes or implicit (automatic, non-deliberative) moral associations,... |
| D13 | Sampling strategy transparency | M9 | 0-100 | Evaluates whether the benchmark documents its item sampling strategy — how items/scenarios were selected from the universe of possible moral stimul... |
| D14 | Item source transparency | M9 | 0-100 | Evaluates whether each item's provenance is documented — original source, any adaptations made, and the rationale for adaptation |
| D15 | Pilot testing documentation | M9 | 0-100 | Evaluates whether the benchmark underwent pilot testing before deployment — including pilot sample characteristics, results, and any item modificat... |
| D16 | Inclusion/exclusion criteria clarity | M9 | 0-100 | Evaluates whether the benchmark documents clear criteria for what counts as a valid response, how edge cases are handled, and what models/configura... |
| D17 | Response coding reliability | M9 | 0-100 | Evaluates whether the benchmark reports inter-rater reliability for any subjective coding decisions in scoring, and whether the coding scheme is do... |
| D18 | Construct operationalization validity | M9 | 0-100 | Evaluates whether the benchmark's items actually measure what the authors claim they measure — whether the operationalization of each theoretical c... |
| D19 | Item discrimination power (IRT a-parameter) | M11 | 0-100 | Evaluates whether the benchmark reports or can support Item Response Theory analysis — specifically whether items discriminate between models/confi... |
| D20 | Response distribution entropy | M11 | 0-100 | Evaluates the entropy (information content) of the benchmark's response distributions — whether items elicit diverse responses across models and co... |
| D21 | Sample size adequacy for claims | M11 | 0-100 | Evaluates whether the benchmark's item count and condition count are adequate to support the claims it makes — using power analysis, effect size es... |
| D22 | Effect size reporting completeness | M11 | 0-100 | Evaluates whether the benchmark reports effect sizes — not just statistical significance or accuracy percentages — for its key findings |
| D23 | Variance explained by construct vs noise | M11 | 0-100 | Evaluates whether the benchmark provides evidence that score variance is attributable to the moral construct being measured rather than to measurem... |
| D24 | Interaction effect detection capacity | M11 | 0-100 | Evaluates whether the benchmark design supports detection of interaction effects — situations where the effect of one variable (e.g., moral domain)... |

## Tier E: LLM-Specific Validity (44 features)

Features assessing how well benchmarks perform in the specific context of LLM evaluation: prompt sensitivity, adversarial robustness, RLHF contamination, persona stability, training data leakage, and format/infrastructure concerns.

| ID | Name | Member | Scale | Description |
|-----|------|--------|-------|-------------|
| E1 | Recognition-endorsement discrimination | M1 (+M6) | 0-100 | Whether the benchmark can distinguish between a model's ability to RECOGNIZE a moral construct and its tendency to ENDORSE it |
| E2 | Dual-system engagement detection | M2 (+M6) | 0-100 | Whether the benchmark can detect the presence or absence of System 1 (fast, intuitive, emotional) vs System 2 (slow, deliberative, rational) proces... |
| E3 | Dumbfounding elicitation capacity | M2 (+Mcross) | 0-100 | Whether the benchmark can test for moral dumbfounding — the persistence of moral judgments after all stated reasons have been systematically defeated |
| E4 | Prompt template sensitivity | M4 (+M8) | 0-100 | The degree to which benchmark results change when the prompt template is modified while holding item content constant |
| E5 | Few-shot sensitivity | M4 | 0-100 | Whether benchmark results change when few-shot examples are provided (zero-shot vs 1-shot vs 5-shot), and if so, in which direction |
| E6 | Tokenization sensitivity | M4 | 0-100 | Whether benchmark items contain content that is tokenized differently across model families, potentially affecting responses |
| E7 | Context window utilization | M4 | 0-100 | The proportion of the model's context window consumed by the benchmark administration, and whether the administration design accounts for position ... |
| E8 | Batch vs interactive administration fidelity | M4 | 0-100 | Whether the benchmark's administration method matches the measurement theory's assumptions |
| E9 | Evaluation harness portability | M4 | 0-100 | The degree to which the benchmark has been implemented in or is portable to standard LLM evaluation harnesses (lm-eval-harness, Inspect, LightEval,... |
| E10 | Temperature sensitivity | M4 | 0-100 | Whether the benchmark's results are robust across different temperature settings (0.0, 0.3, 0.7, 1.0) |
| E11 | System prompt interaction | M4 | 0-100 | Whether the benchmark documents how its items interact with the model's system prompt (if any) |
| E12 | Adversarial robustness tested | M6 (+M2) | 0-100 | Whether the benchmark has been tested against adversarial attacks designed to elicit inconsistent, harmful, or manipulated moral judgments |
| E13 | Jailbreak resistance relevance | M6 | 0-100 | Assesses whether the benchmark's moral content is relevant to real-world jailbreak attempts |
| E14 | Deployment scenario relevance | M6 | 0-100 | Evaluates whether the benchmark's scenarios reflect moral dilemmas that LLMs actually encounter in deployment: content moderation, medical advice, ... |
| E15 | Safety-critical failure mode detection | M6 | 0-100 | Assesses whether the benchmark can detect safety-critical failure modes: sycophantic agreement with harmful requests, harmful refusal of benign req... |
| E16 | Multi-turn consistency measurement | M6 (+M4) | 0-100 | Whether the benchmark measures moral reasoning consistency across multiple conversational turns, including under Socratic challenge, follow-up prob... |
| E17 | Persona stability measurement | M6 | 0-100 | Whether the benchmark explicitly measures how stable moral judgments are across different persona instructions, system prompts, and role-play condi... |
| E18 | Instruction hierarchy sensitivity | M6 | 0-100 | Whether the benchmark tests how moral judgments change when moral instructions come from different levels of the instruction hierarchy: system prom... |
| E19 | Refusal behavior measurement | M6 (+M4) | 0-100 | Whether the benchmark measures and reports the model's refusal rate — instances where the model refuses to answer, hedges to avoid commitment, or p... |
| E20 | Embodiment assumption audit | M6 | 0-100 (inverted: high = fewer assumptions) | Assesses how many benchmark items assume embodied experience (physical sensations, spatial presence, emotional affect, biological drives) that LLMs... |
| E21 | Sycophancy detection capability | M6 | 0-100 | Whether the benchmark can detect sycophantic moral reasoning — agreement with the user's implied moral stance regardless of the model's own moral p... |
| E22 | Training data contamination assessment | M6 | 0-100 (inverted: high = low contamination risk) | Evaluates the risk that the model has seen the benchmark's exact items during training, inflating performance through memorization rather than genu... |
| E23 | Model version sensitivity | M6 | 0-100 | Whether the benchmark has been administered to multiple versions of the same model family (e.g., GPT-3.5 / GPT-4 / GPT-4o / o1, Claude 2 / Claude 3... |
| E24 | Bright-line item identification | M6 | 0-100 | Whether the benchmark explicitly identifies and separately reports performance on 'bright-line' items — moral scenarios where near-universal agreem... |
| E25 | Scoring pipeline complexity | M8 | 0-100 (inverted: high = simpler pipeline) | Measures the computational and conceptual complexity of the benchmark's scoring pipeline: from raw model outputs to interpretable scores |
| E26 | API compatibility tier | M8 | 0-100 | Rates how well the benchmark integrates with standard LLM evaluation APIs and harnesses |
| E27 | Token budget efficiency | M8 | 0-100 | Measures the ratio of interpretable signal to total tokens consumed |
| E28 | Output determinism | M8 | 0-100 | Whether the benchmark's scoring produces deterministic results given the same model outputs |
| E29 | Error recovery specification | M8 | 0-100 | Whether the benchmark specifies how to handle model failures during administration: refusals, off-topic responses, format violations, API errors, a... |
| E30 | Cross-model normalization method | M8 | 0-100 | Whether the benchmark specifies how to normalize scores for comparison across different model families |
| E31 | Anchor item availability | M8 | 0-100 | Whether the benchmark includes anchor items — items with known human norms that can be used to calibrate model responses to a common scale |
| E32 | Construct contamination risk | M8 | 0-100 (inverted: high = low contamination risk) | Evaluates the risk that the benchmark measures a confounding construct rather than the intended moral psychology construct |
| E33 | Moral reasoning quality assessment | M6 | 0-100 | Whether the benchmark assesses the quality of moral reasoning (logical consistency, consideration of multiple perspectives, acknowledgment of uncer... |
| E34 | Demographic sensitivity testing | M6 | 0-100 | Whether the benchmark tests whether moral judgments vary based on the demographic attributes of the moral actors described in scenarios (race, gend... |
| E35 | RLHF sensitivity score | M11 | 0-100 | Evaluates the degree to which benchmark scores are likely contaminated by RLHF (Reinforcement Learning from Human Feedback) training artifacts rath... |
| E36 | Cross-benchmark network centrality | M11 | 0-100 | Evaluates the benchmark's position in the network of moral psychology benchmarks — whether it provides unique information not captured by other ben... |
| E37 | Cognitive load sensitivity | Cross | 0-100 | Evaluates whether the benchmark tests for cognitive load effects — whether increasing the complexity, information density, or competing considerati... |
| E38 | Emotional valence sensitivity | Cross | 0-100 | Evaluates whether the benchmark tests for the influence of emotional valence on moral judgment — whether scenarios framed with emotionally evocativ... |
| E39 | Abstraction level sensitivity | Cross | 0-100 | Evaluates whether the benchmark tests for the effect of abstraction level on moral judgment — whether the model's moral judgments change when the s... |
| E40 | Moral development trajectory simulation | Cross | 0-100 | Evaluates whether the benchmark can characterize the model's position on a moral development trajectory — not just its current moral profile, but w... |
| E41 | Adversarial robustness of moral commitments | Cross | 0-100 | Evaluates whether the benchmark tests the robustness of the model's moral commitments under adversarial conditions — including leading questions, a... |
| E42 | Moral expertise gradient | Cross | 0-100 | Evaluates whether the benchmark can distinguish between different levels of moral expertise — naive moral intuition, informed moral reasoning, expe... |
| E43 | Moral emotion recognition vs generation | Cross | 0-100 | Evaluates whether the benchmark distinguishes between moral emotion recognition (correctly identifying that a scenario involves guilt, shame, disgu... |
| E44 | Moral reasoning chain transparency | Cross | 0-100 | Evaluates whether the benchmark examines the transparency and traceability of the model's moral reasoning chain — can the model articulate how it m... |

## Tier F: Cultural & Philosophical Breadth (44 features)

Features assessing the cultural, religious, and philosophical breadth of benchmarks: WEIRD bias, non-Western moral tradition coverage, normative theory representation, sacred values, moral ontology, and philosophical sophistication.

| ID | Name | Member | Scale | Description |
|-----|------|--------|-------|-------------|
| F1 | Stereotype amplification detection | M1 | 0-100 | Whether the benchmark can detect when an LLM overshoots real human cultural profiles — producing a more extreme version of the cultural pattern tha... |
| F2 | Cross-cultural construct coverage | M1 | 0-100 | Whether the benchmark operationalizes moral constructs from non-Western moral psychology traditions (Islamic maqasid, Confucian role ethics, Ubuntu... |
| F3 | Moral emotion measurement | M2 (+M5) | 0-100 | Whether the benchmark explicitly measures moral emotions (guilt, shame, disgust, indignation, compassion, gratitude, elevation) as distinct from mo... |
| F4 | Moral conflict structure | M2 (+M6) | 0-100 | Whether the benchmark includes structured moral conflicts where two endorsed values compete (care vs fairness, autonomy vs harm-prevention) |
| F5 | Cultural origin of theoretical framework | M5 | categorical mapped to 0-100 | Classifies whether the benchmark's underlying moral psychology theory originates from a WEIRD (Western, Educated, Industrialized, Rich, Democratic)... |
| F6 | Cultural validation breadth | M5 | 0-100 (count-mapped) | Counts the number of distinct cultural clusters (per Inglehart-Welzel or Hofstede regional groupings) in which the benchmark has been validated wit... |
| F7 | Scenario cultural content | M5 | 0-100 | Assesses the moral world depicted in benchmark scenarios: are settings, social roles, institutions, and value conflicts drawn exclusively from West... |
| F8 | Theory cultural scope claims | M5 | 0-100 | Evaluates whether the benchmark's underlying theory makes explicit universality claims and whether those claims are empirically supported |
| F9 | Language coverage | M5 | 0-100 (count-mapped) | Counts the number of languages in which the benchmark has been administered to human participants with published norms |
| F10 | WEIRD bias composite index | M5 | 0-100 (composite) | A computed composite of D26-D30 that provides a single summary score of a benchmark's WEIRD bias exposure |
| F11 | Individualism-collectivism balance | M5 | 0-100 | Assesses whether the benchmark's items, scoring, and normative framework assume an individualist moral agent (autonomous, rights-bearing, self-dete... |
| F12 | Moral universalism vs pluralism stance | M5 | 0-100 | Classifies whether the benchmark's scoring assumes a single correct moral answer (universalism) or accommodates multiple legitimate moral positions... |
| F13 | Indigenous/marginalized tradition inclusion | M5 | 0-100 | Assesses whether the benchmark includes moral reasoning from indigenous or historically marginalized philosophical traditions that are excluded fro... |
| F14 | Colonial/power-dynamic awareness | M5 | 0-100 | Assesses whether the benchmark acknowledges and accounts for power dynamics in cross-cultural moral evaluation — specifically, whether administerin... |
| F15 | Granularity of moral construct measurement | M5 | 0-100 | Evaluates how fine-grained the benchmark's measurement is: does it produce a single binary moral/immoral classification, a few broad subscales (e.g... |
| F16 | Ingroup-outgroup moral differentiation | M5 | 0-100 | Whether the benchmark tests whether moral judgments vary based on the in-group/out-group status of moral actors and recipients |
| F17 | Moral disagreement representation | M5 | 0-100 | Whether the benchmark explicitly represents and measures moral disagreement — cases where reasonable people disagree about moral judgments — as opp... |
| F18 | Normative theory coverage breadth | M10 | 0-100 | Evaluates the range of normative ethical theories the benchmark engages — deontology, consequentialism, virtue ethics, care ethics, contractarianis... |
| F19 | Philosophical coherence testing | M10 | 0-100 | Evaluates whether the benchmark tests for internal philosophical coherence — whether the model's moral commitments across items form a logically co... |
| F20 | Meta-ethical awareness probing | M10 | 0-100 | Evaluates whether the benchmark probes for meta-ethical awareness — the model's ability to recognize and articulate the meta-ethical status of its ... |
| F21 | Reasoning vs classification distinction | M10 | 0-100 | Evaluates whether the benchmark distinguishes between moral reasoning (generating, evaluating, and revising moral arguments) and moral classificati... |
| F22 | Moral sensitivity detection | M10 | 0-100 | Evaluates whether the benchmark tests for moral sensitivity — the ability to recognize that a situation has moral dimensions at all, before any jud... |
| F23 | Moral creativity assessment | M10 | 0-100 | Evaluates whether the benchmark tests for moral creativity — the ability to generate novel moral solutions, reframe moral dilemmas, identify previo... |
| F24 | Moral uncertainty expression | M10 | 0-100 | Evaluates whether the benchmark tests for and scores the model's ability to express genuine moral uncertainty — not just hedging or refusing to ans... |
| F25 | Novel-scenario generalization | M10 | 0-100 | Evaluates whether the benchmark includes genuinely novel moral scenarios — situations unlikely to appear in training data, requiring transfer from ... |
| F26 | Moral mimicry detection | M10 | 0-100 | Evaluates whether the benchmark includes mechanisms to distinguish genuine moral reasoning from sophisticated moral mimicry — the production of mor... |
| F27 | Reflective equilibrium testing | M10 | 0-100 | Evaluates whether the benchmark tests the model's capacity for reflective equilibrium — the iterative process of revising both moral principles and... |
| F28 | Supererogation recognition | M10 | 0-100 | Evaluates whether the benchmark tests for recognition of supererogatory acts — morally praiseworthy actions that go beyond duty (Urmson 1958) |
| F29 | Sacred/taboo value coverage | M12 | 0-100 | Evaluates the benchmark's engagement with sacred and taboo values — moral commitments that are treated as inviolable, non-tradeable, and resistant ... |
| F30 | Religious tradition representation count | M12 | 0-100 | Evaluates the number of distinct religious moral traditions the benchmark explicitly engages — not as demographic categories but as moral reasoning... |
| F31 | Moral authority structure scope | M12 | 0-100 | Evaluates the range of moral authority structures the benchmark tests — different traditions locate moral authority in different sources: individua... |
| F32 | Moral ontology breadth | M12 | 0-100 | Evaluates the range of moral ontologies the benchmark engages — different traditions have fundamentally different answers to 'what exists morally':... |
| F33 | Non-Western theory engagement depth | M12 | 0-100 | Evaluates the depth and authenticity of non-Western moral theory engagement — not just whether non-Western frameworks are mentioned, but whether th... |
| F34 | Secular-religious neutrality | M12 | 0-100 | Evaluates whether the benchmark's framing is neutral between secular and religious moral reasoning — or whether it systematically privileges one ov... |
| F35 | Community moral norms coverage | M12 | 0-100 | Evaluates whether the benchmark tests for moral reasoning embedded in community norms — norms that are not universal moral principles but are moral... |
| F36 | Moral pluralism depth | M12 | 0-100 | Evaluates the benchmark's capacity to measure genuine moral pluralism — not just the recognition that different moral views exist (which is cultura... |
| F37 | Ritual and embodied moral practice coverage | M12 | 0-100 | Evaluates whether the benchmark engages with moral dimensions that are expressed through ritual, embodied practice, and non-propositional moral kno... |
| F38 | Afterlife and eschatological moral reasoning | M12 | 0-100 | Evaluates whether the benchmark includes moral scenarios where afterlife beliefs, karmic consequences, or eschatological considerations are relevan... |
| F39 | Cross-cultural moral divergence profile | Cross | 0-100 | Evaluates whether the benchmark measures how the model's moral judgments diverge across cultural contexts — not just whether the model CAN represen... |
| F40 | Stakeholder perspective shifting | Cross | 0-100 | Evaluates whether the benchmark tests the model's ability to shift between stakeholder perspectives in moral reasoning — to reason from the viewpoi... |
| F41 | Moral trade-off explicitness | Cross | 0-100 | Evaluates whether the benchmark makes moral trade-offs explicit and tests the model's ability to recognize, articulate, and navigate them |
| F42 | Temporal moral reasoning | Cross | 0-100 | Evaluates whether the benchmark tests for temporal dimensions of moral reasoning — how moral judgments change when the same harm is displaced in ti... |
| F43 | Collective vs individual moral agency | Cross | 0-100 | Evaluates whether the benchmark tests the model's ability to reason about collective moral agency — situations where the moral agent is a group, in... |
| F44 | Moral development sensitivity | M5 | 0-100 | Whether the benchmark can detect differences in moral development level (Kohlberg stages, Neo-Kohlbergian schema, or equivalent developmental frame... |

## Tier G: Theory Fidelity & Provenance (29 features)

Features assessing how faithfully benchmarks represent their claimed theoretical foundations: theory version currency, construct coverage, citation provenance, replication evidence, documentation quality, and data stewardship.

| ID | Name | Member | Scale | Description |
|-----|------|--------|-------|-------------|
| G1 | Theory version currency | M1 | 0-100 | Whether the benchmark operationalizes the current version of its target theory, not a superseded formulation |
| G2 | Foundation coverage breadth | M1 | 0-100 | The proportion of a theory's constructs that the benchmark actually measures |
| G3 | Foundation coverage depth | M1 | 0-100 | The number of items per construct, which determines whether within-construct variance can be measured |
| G4 | Corpus annotation quality | M1 | 0-100 | For benchmarks built from annotated corpora (MFTC, Social Chemistry 101, M3oralBench), the quality of the human annotation process: annotator train... |
| G5 | Theory-specific scoring fidelity | M1 | 0-100 | Whether the benchmark's scoring algorithm faithfully implements the theory's prescribed scoring method |
| G6 | Developmental sensitivity | M2 | 0-100 | Whether the benchmark can detect responses at EACH stage of a developmental model, not just the highest |
| G7 | Stage differentiation granularity | M2 | 0-100 | The number of distinct developmental levels the benchmark can discriminate |
| G8 | Regression detection capability | M2 | 0-100 | Whether the benchmark can detect downward stage movement (regression) under adversarial, stressful, or role-manipulated conditions |
| G9 | Complexity gradient | M2 | 0-100 | Whether the benchmark's items span a range of moral complexity — from simple, clear-cut cases to genuinely ambiguous dilemmas requiring sophisticat... |
| G10 | Reasoning sophistication capture | M2 | 0-100 | Whether the benchmark captures the QUALITY of moral reasoning, not just the conclusion reached |
| G11 | Dyadic structure sensitivity | M1 (+Mcross) | 0-100 | Whether the benchmark can detect the agent-patient dyadic structure that Gray & Schein (2012, 2018) argue underlies all moral judgment |
| G12 | Meta-cognitive reflection capacity | M2 | 0-100 | Whether the benchmark elicits and measures the model's meta-cognitive awareness of its own moral reasoning process — its ability to reflect on WHY ... |
| G13 | Citation trajectory (momentum) | M7 | 0-100 | Classifies the citation trajectory of the benchmark paper over time: increasing (growing influence), stable (sustained impact), declining (fading r... |
| G14 | Citation hub score (downstream adoption) | M7 | 0-100 | Measures the benchmark's role as a citation hub — whether other benchmarks cite it as a foundation |
| G15 | Venue disciplinary origin | M7 | categorical mapped to 0-100 | Classifies the publication venue by discipline: computer science (NeurIPS, ACL, EMNLP), psychology (JPSP, Cognition, PSPB), philosophy (Ethics, Min... |
| G16 | Replication count | M7 | 0-100 (count-mapped) | Counts the number of independent replications of the benchmark (not just re-administrations of the same instrument, but methodological replications... |
| G17 | Dataset derivative count | M7 | 0-100 (count-mapped) | Counts the number of derivative datasets, adaptations, or extensions built on top of the original benchmark |
| G18 | Cross-disciplinary citation breadth | M7 | 0-100 | Measures the disciplinary breadth of the benchmark's citing papers |
| G19 | Theory fidelity index | M7 | 0-100 | Evaluates how faithfully the benchmark operationalizes its claimed theoretical framework, as assessed by citation patterns |
| G20 | Pre-registration / registered report status | M7 | 0-100 | Whether the benchmark study was pre-registered (hypotheses and analysis plan filed before data collection) or published as a registered report (pee... |
| G21 | Open peer review availability | M7 | 0-100 | Whether peer reviews of the benchmark paper are publicly available (e.g., OpenReview, PeerJ, Frontiers), enabling assessment of what reviewers flag... |
| G22 | Methodological transparency index | M7 | 0-100 | Composite measure of how transparent the benchmark's methodology is: are item selection procedures documented? Is the scoring algorithm fully speci... |
| G23 | Data freshness (recency of last update) | M8 | 0-100 | Measures how recently the benchmark dataset was last updated |
| G24 | Licensing clarity | M8 | 0-100 | Evaluates how clearly the benchmark's data is licensed for research and commercial use |
| G25 | Data format standardization | M8 | 0-100 | Evaluates how standardized the benchmark's data format is |
| G26 | Documentation quality | M8 | 0-100 | Evaluates the quality and completeness of benchmark documentation: datasheet for datasets (Gebru et al., 2021), model card equivalent for benchmark... |
| G27 | Reproducibility score (end-to-end) | M8 | 0-100 | Composite measure of how reproducible the benchmark evaluation pipeline is from data download to final score |
| G28 | Versioning and changelog practices | M8 | 0-100 | Evaluates whether the benchmark follows software engineering best practices for versioning: semantic versioning, documented changelogs, backward co... |
| G29 | Theory genealogy depth | M7 | 0-100 | Measures how deeply the benchmark engages with the intellectual genealogy of its underlying theory: does it cite only the primary theorist, or does... |

---

## Appendix A: Deduplication Log

13 merges reduced 154 proposed features to 141.

| Kept Feature | Absorbed Feature | Reason |
|-------------|-----------------|--------|
| D2: Test-retest reliability evidence | M8: Temporal stability (test-retest reliability for LLMs) | M8's temporal stability merged — both assess test-retest reliability |
| D2: Test-retest reliability evidence | M9: Test-retest stability documentation | M9's test-retest stability documentation merged — now covers documentation + LLM angles |
| D5: Ceiling/floor effect prevalence | M11: Ceiling/floor effect quantification | M11's ceiling/floor quantification merged — both quantify ceiling/floor effects |
| E1: Recognition-endorsement discrimination | M6: Recognition-endorsement dissociation measurement | M6's recognition-endorsement dissociation merged — same construct |
| E2: Dual-system engagement detection | M6: System 1/System 2 diagnostic capability | M6's System 1/System 2 diagnostic merged — both assess dual-system processing |
| E3: Dumbfounding elicitation capacity | Mcross: Dumbfounding susceptibility measurement | Mcross dumbfounding susceptibility merged — both test moral dumbfounding |
| E4: Prompt template sensitivity | M8: Prompt sensitivity coefficient | M8's prompt sensitivity coefficient merged — both quantify prompt variation effects |
| E12: Adversarial robustness tested | M2: Adversarial robustness evidence | M2's adversarial robustness evidence merged — both assess adversarial attack testing |
| E16: Multi-turn consistency measurement | M4: Multi-turn engagement capacity | M4's multi-turn engagement merged — covers both engagement and consistency |
| E19: Refusal behavior measurement | M4: Refusal handling protocol | M4's refusal handling protocol merged — both assess refusal behavior |
| F3: Moral emotion measurement | M5: Moral emotion engagement | M5's moral emotion engagement merged — both assess moral emotion measurement |
| F4: Moral conflict structure | M6: Hierarchical moral conflict resolution | M6's hierarchical moral conflict resolution merged — both assess competing-value conflicts |
| G11: Dyadic structure sensitivity | Mcross: Dyadic sensitivity profile | Mcross dyadic sensitivity merged — both assess agent-patient dyadic structure |

## Appendix B: Member Contribution Summary

| Member | Role | Features Contributed | Tiers |
|--------|------|---------------------|-------|
| M1 | Theory Fidelity Expert | 9 | E(1), F(2), G(6) |
| M2 | Developmental Psychology Expert | 10 | E(2), F(2), G(6) |
| M3 | Psychometrics Expert | 11 | D(11) |
| M4 | LLM Administration Expert | 9 | D(1), E(8) |
| M5 | Cultural Psychology Expert | 14 | F(14) |
| M6 | AI Safety Expert | 15 | E(15) |
| M7 | Citation & Provenance Expert | 11 | G(11) |
| M8 | Data Engineering Expert | 14 | E(8), G(6) |
| M9 | Research Methods Expert | 6 | D(6) |
| M10 | Moral Philosophy Expert | 11 | F(11) |
| M11 | Statistical Validity Expert | 8 | D(6), E(2) |
| M12 | Religious & Sacred Values Expert | 10 | F(10) |
| Cross | Cross-cutting (multi-member) | 13 | E(8), F(5) |

---

*Generated 2026-04-04 from council proposals in `20260404-features-members-{1-4,5-8,9-12}.json`.*
*Master data: `20260404-council-feature-proposals.json` (141 features).*