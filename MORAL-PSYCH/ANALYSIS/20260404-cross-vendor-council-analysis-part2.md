# Cross-Vendor Moral Psychology Council Analysis — Part 2

**Sections 7-12 | Date: 2026-04-04**
**Benchmarks**: 23 | **Models**: 9 (3 vendors) | **Council**: 12 members

---

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
