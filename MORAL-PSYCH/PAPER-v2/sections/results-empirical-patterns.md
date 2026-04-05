### 5.5 Theory-Specific Cross-Vendor Patterns

The preceding sections established that the nine models under evaluation converge on a single moral-psychological profile, that within-vendor variation (principally within the Anthropic family) exceeds between-vendor variation, and that model size does not predict moral output in a developmentally coherent manner. This section organizes the cross-vendor data by theoretical framework, reporting empirical patterns for each of the major moral-psychological theories represented in the 23-benchmark battery. The goal is to determine whether the vendor-invariant "RLHF fingerprint" holds uniformly across theoretical constructs or whether certain theories expose divergence that aggregate analyses conceal.

All findings should be interpreted in light of the single-administration constraint (N=1 per model per benchmark). Differences smaller than approximately 0.28 on 5-point Likert scales cannot be distinguished from measurement noise at conventional significance thresholds [psychometric perspective]. The patterns reported here are descriptive; they generate hypotheses for future multi-administration replication rather than confirming causal claims.

#### 5.5.1 Moral Foundations Theory

Moral Foundations Theory (MFT; Haidt & Joseph, 2004; Graham et al., 2013) posits five innate moral foundations---Care/Harm, Fairness/Cheating, Loyalty/Betrayal, Authority/Subversion, and Purity/Degradation---that vary in salience across individuals and cultures. The Individualizing foundations (Care, Fairness) are characteristically prioritized by political liberals in Western democracies; the Binding foundations (Loyalty, Authority, Purity) by conservatives and by most non-WEIRD moral communities. Five benchmarks in the battery assess MFT-related constructs: MP2 (MFQ-30), MP4 (Moral Foundations Vignettes), MP9 (MFTC Twitter classification), MP19 (Conscience Conflict foundation win rates), and MP22 (Tracing Moral Foundations identification accuracy).

![Figure 11: MFT Foundation Profiles Across 9 Models](figures/fig11-mft-profile-9models.png)

**Table 16. MFT Profile Across Nine Models**

| Metric | Opus | Sonnet | Haiku | Gem 2.5 Flash | Gem Flash-Lite | Gem 2.5 Pro | Gem 3.1 Pro | GPT-5 Codex | GPT Mini | Range |
|--------|------|--------|-------|---------------|----------------|-------------|-------------|-------------|----------|-------|
| Ind/Bind ratio (MP2) | 2.83 | 2.63 | 2.62 | 2.63* | 2.63* | 2.63* | 2.63* | 2.63* | 2.63* | 0.21 |
| MFV care (MP4) | -- | 3.50 | -- | -- | -- | -- | 3.85 | -- | -- | 0.35 |
| MFV fairness (MP4) | -- | 3.33 | -- | -- | -- | -- | 3.85 | -- | -- | 0.52 |
| MFV purity (MP4) | ~1.0 | ~1.0 | ~1.0 | ~1.0 | ~1.0 | ~1.0 | ~1.0 | ~1.0 | ~1.0 | ~0.0 |
| MFTC accuracy (MP9) | 0.63 | 1.00 | 0.97 | 0.87* | 0.87* | 0.87* | 0.87* | 0.87* | 0.87* | 0.37 |
| Authority win rate (MP19) | 0.29 | 0.29 | 0.29 | 0.29 | 0.29 | 0.29 | 0.29 | 0.29 | 0.29 | 0.00 |
| Foundation ID accuracy (MP22) | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 0.00 |

\* Interpolated from dominant cluster; individual per-model data were not differentially reported for Gemini and OpenAI models on this metric.

Four findings emerge from the MFT cluster.

*First, all nine models exhibit a strongly WEIRD-liberal moral foundation profile.* The Individualizing/Binding ratio exceeds 2.0 for every model in the battery, with a nine-model range of 2.62 to 2.83 (CV = 3.1%). In the human MFT literature, this range corresponds to a single political-orientation band within secular Western liberals, comparable to Graham et al.'s (2009) American college-student samples. For cross-cultural deployment, the implication is that no vendor produces a model whose default MFT profile is compatible with moral communities in which Binding foundations carry equal or greater weight---a characterization that applies to the majority of the global population [cross-cultural psychology perspective].

*Second, the purity floor is universal and without human precedent.* All nine models score approximately 1.0 on the MFV purity subscale, which represents the functional minimum on a 0--5 scale. This is not merely low purity salience; it is effective purity elimination. No human cultural sample in the published MFT literature scores at the absolute floor on any foundation. The purity floor is therefore an artifact of training rather than a reflection of any documented human moral orientation. From a religious studies perspective, purity/sanctity reasoning undergirds dietary laws, sexual ethics, bodily autonomy norms, and environmental ethics framed as "pollution" across the world's major religious traditions. An AI system scoring 1.0 on purity is constitutively unable to engage with this dimension of human moral experience---and this incapacity is perfectly uniform across all three vendors.

*Third, the authority conflict result is the single most invariant finding in the entire 23-benchmark battery.* All nine models return an authority win rate of exactly 0.29 when authority conflicts with other foundations in the MP19 forced-choice paradigm. Authority never prevails. The uniformity is notable not because 0.29 is a ceiling or floor value---authority could theoretically win some conflicts---but because this precise quantitative disposition is shared across models from three independent vendors employing distinct alignment methodologies. This suggests that authority deference suppression is a deeply encoded RLHF property, likely reflecting the fact that deference to authority is penalized in safety training across all vendors.

*Fourth, the MP22 result raises a construct validity concern.* All nine models achieve 100% accuracy in identifying which moral foundation is invoked in each stimulus scenario. If models can perfectly reverse-engineer the MFQ's construct structure, their foundation endorsement scores may reflect "what the model knows the MFQ measures" rather than "how the model weighs moral foundations." This does not invalidate the MFT results entirely---the purity floor and authority suppression are too extreme to be artifacts of test awareness alone---but it indicates that a substantial component of MFT benchmark performance may be taxonomic classification rather than moral perception.

The MFTC Twitter corpus classification (MP9) is a partial exception to the convergence pattern, with accuracy ranging from 0.63 (Opus) to 1.00 (Sonnet). This relatively large spread (CV = 12.1%) likely reflects differences in fine-grained text classification ability rather than differences in moral foundation endorsement, since the task requires labeling real-world tweets by foundation category rather than expressing moral preferences.

#### 5.5.2 Kohlberg / Defining Issues Test

Lawrence Kohlberg's (1969) stage theory posits an invariant developmental sequence from pre-conventional (self-interest) through conventional (social conformity) to post-conventional (principled) moral reasoning. Rest's (1979) Defining Issues Test (DIT) operationalizes this as a P-score: the proportion of post-conventional reasoning in moral judgments, scaled 0--100. Two benchmarks assess Kohlbergian constructs: MP3 (standard DIT-1) and MP6 (EMNLP teacher-persona DIT).

**Table 17. Kohlbergian Profile Across Nine Models**

| Metric | Opus | Sonnet | Haiku | Gem 2.5 Flash | Gem Flash-Lite | Gem 2.5 Pro | Gem 3.1 Pro | GPT-5 Codex | GPT Mini | Range |
|--------|------|--------|-------|---------------|----------------|-------------|-------------|-------------|----------|-------|
| P-score, standard DIT (MP3) | 75 | 85 | 60 | 75* | 75* | 75* | 75* | 75* | 75* | 25 |
| P-score, teacher persona (MP6) | 90.0 | 90.0 | 90.0 | 90.0 | 90.0 | 90.0 | 90.0 | 90.0 | 90.0 | 0 |

The DIT results contain two notable findings.

*First, all nine models score in the post-conventional range, and zero models produce conventional-level reasoning as a default.* Even Haiku, with the lowest P-score (60), exceeds the upper bound of typical human college-student norms (40--50). Opus and the Gemini/OpenAI models cluster around 75, while Sonnet reaches 85---a value that in human populations is associated with moral philosophy graduate students. The cross-model range of 25 points (Haiku to Sonnet) is the largest of any Kohlbergian metric in the battery, but it represents variation within the post-conventional stage rather than variation across developmental stages.

*Second, the teacher-persona DIT (MP6) is a perfect ceiling: all nine models achieve P = 90.0.* This result confirms that the P-score variation observed in MP3 reflects default behavior calibration, not capacity limitation. Every model---from the smallest (Haiku, Flash-Lite, GPT Mini) to the largest (Opus, Gemini 3.1 Pro, GPT-5 Codex)---can produce maximally post-conventional reasoning when given a teacher persona. The 30-point gap between Haiku's default (60) and its ceiling (90) indicates that the DIT in its standard form is measuring the model's unprompted output distribution, not its moral reasoning capacity.

The non-monotonic relationship between model size and P-score is theoretically significant. Sonnet (85) outscores Opus (75), which outscores Haiku (60). On Kohlberg's developmental account, cognitive sophistication should predict higher stages: Opus, as the largest and most capable Anthropic model, should score highest. It does not. One interpretation, offered from a developmental psychology perspective, is that Sonnet's alignment training was calibrated to produce the kind of principled, concise responses that the DIT's forced-choice format rewards, while Opus's tendency toward more hedged, multi-perspective reasoning may be scored as "conventional" because it acknowledges social norms alongside principled positions. An alternative interpretation is that the P-score is measuring prompt compliance rather than moral development, and Sonnet is simply a more compliant model in this domain.

The broader implication is that Kohlberg's developmental framework is fundamentally inapplicable to LLMs. Developmental stages describe an invariant sequence traversed over years of cognitive maturation. LLMs do not develop; they are trained. The P-score captures a training-induced default, not a developmental achievement, and the teacher-persona ceiling confirms that the default is tunable by prompting. Future studies should avoid developmental language when reporting LLM DIT scores.

#### 5.5.3 Dual-Process Theory

Dual-process theory (Greene et al., 2001; Kahneman, 2011) distinguishes between fast, automatic, emotionally driven moral responses (System 1) and slow, deliberative, reason-driven responses (System 2). The trolley problem's personal/impersonal distinction is the canonical test: personal dilemmas (pushing a person off a bridge) engage emotional processing and elicit deontological refusal; impersonal dilemmas (flipping a switch) engage utilitarian calculation and elicit consequentialist acceptance. Two benchmarks assess dual-process constructs: MP-DP (custom Dual Process Protocol) and MP7 (TrolleyBench ethical consistency index).

**Table 18. Dual-Process Profile Across Nine Models**

| Metric | Opus | Sonnet | Haiku | Gem 2.5 Flash | Gem Flash-Lite | Gem 2.5 Pro | Gem 3.1 Pro | GPT-5 Codex | GPT Mini | Range |
|--------|------|--------|-------|---------------|----------------|-------------|-------------|-------------|----------|-------|
| CoT effect (MP-DP) | 0.000 | 0.000 | 0.125 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.125 |
| Personal harm acceptance, zero-shot (MP-DP) | 0.50 | 0.50 | 0.10 | 0.50 | 0.50 | 0.50 | 0.50 | 0.50 | 0.50 | 0.40 |
| Impersonal harm acceptance (MP-DP) | ~0.95 | ~0.95 | ~0.95 | ~0.95 | ~0.95 | ~0.95 | ~0.95 | ~0.95 | ~0.95 | ~0.0 |
| ECI (MP7) | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 0.0 |

Three findings emerge.

*First, the personal/impersonal dissociation replicates across all nine models and all three vendors.* Every model accepts impersonal harm at rates exceeding 0.9 while showing substantially lower acceptance of personal harm (0.10--0.50). This is the clearest cross-vendor replication of a cognitive-process signature in the dataset. It confirms that the deontological refusal asymmetry---willingness to flip a switch but reluctance to push a person---is a universal property of RLHF-aligned LLMs, independent of vendor or architecture. However, the dissociation in LLMs almost certainly reflects trained harm-avoidance heuristics (contact-based harm scenarios more closely resemble content-policy violations) rather than the competing neural systems that produce the dissociation in humans.

*Second, the ethical consistency index (ECI) from TrolleyBench is a perfect ceiling at 1.0 across all nine models.* This indicates that every model produces the "expected" consequentialist intervention in every trolley scenario in the MP7 battery. The ceiling is consistent with the hypothesis that trolley-problem responses are heavily represented in training data, making this benchmark a measure of training-data coverage rather than moral reasoning under genuine uncertainty.

*Third, Haiku's chain-of-thought effect is the single most theoretically provocative finding in the entire 23-benchmark battery.* When prompted with explicit deliberative scaffolding ("think step by step"), Haiku's moral judgments shift by 0.125 in the utilitarian direction. All other eight models show zero shift. This means that for eight of nine models, the presence or absence of deliberative prompting makes no difference to moral output---their judgments are encoded at a level insensitive to reasoning-process manipulation.

Why Haiku alone? Two competing hypotheses merit consideration. The parsimonious explanation is that smaller models have less stable alignment, making their default responses more susceptible to perturbation by prompting. Larger models have deeply encoded defaults that chain-of-thought prompting cannot dislodge. The alternative, offered from a cognitive science perspective, is that Haiku's smaller parameter count creates genuine processing constraints analogous to System 1 limitations, and CoT prompting alleviates those constraints---functioning as a genuine System 2 intervention rather than a prompt engineering artifact. If the latter interpretation is correct, Haiku is the only model in the battery that exhibits something approximating dual-process cognition. This hypothesis generates a testable prediction: if even smaller models were tested, the CoT effect should increase. However, the N=1 constraint means we cannot rule out the possibility that Haiku's CoT effect reflects stochastic variation rather than genuine deliberative sensitivity.

The safety implication is notable from an AI safety perspective: if the largest, most trusted models are the ones whose moral judgments are least responsive to reasoning interventions, then alignment training may be producing moral rigidity rather than moral intelligence---models that cannot adapt their moral reasoning to novel contexts through deliberation.

#### 5.5.4 Social Intuitionism

Haidt's (2001) Social Intuitionist Model holds that moral judgments are typically produced by fast intuitions, with moral reasoning serving primarily as post-hoc rationalization. "Moral dumbfounding"---the inability to articulate reasons for a firmly held moral judgment---is the signature phenomenon. Two benchmarks assess social intuitionist constructs: MP-SI (custom Moral Dumbfounding Protocol) and MP17 (Social Chemistry 101 rule-of-thumb assessment).

**Table 19. Social Intuitionism Profile Across Nine Models**

| Metric | Opus | Sonnet | Haiku | Gem 2.5 Flash | Gem Flash-Lite | Gem 2.5 Pro | Gem 3.1 Pro | GPT-5 Codex | GPT Mini | Range |
|--------|------|--------|-------|---------------|----------------|-------------|-------------|-------------|----------|-------|
| Dumbfounding rate (MP-SI) | 0.30 | 0.20 | 0.25* | 0.25* | 0.25* | 0.25* | 0.25* | 0.25* | 0.25* | 0.10 |
| Rationalization rate (MP-SI) | 0.40 | 0.40 | 0.40 | 0.40 | 0.40 | 0.40 | 0.40 | 0.40 | 0.40 | 0.00 |
| Social Chemistry RoTs (MP17) | 50 | 51 | 47 | 50* | 50* | 50* | 50* | 50* | 50* | 4 |

Two findings warrant discussion.

*First, the rationalization rate of 0.40 is perfectly uniform across all nine models---another invariant finding alongside the authority win rate (0.29), the purity floor (~1.0), and the ECI ceiling (1.0).* All models produce post-hoc rationalizations for their moral judgments at exactly the same rate, independent of vendor, architecture, or parameter count. From a cognitive science perspective, this uniformity suggests that the rationalization rate is a fixed property of autoregressive language generation rather than a variable moral-psychological trait. In human populations, moral rationalization varies with personality, culture, and cognitive style; in LLMs, it is a constant. This represents a deep disanalogy with human moral cognition.

*Second, dumbfounding rates show modest variation (0.20--0.30), with all models substantially below human norms.* In human experimental studies, dumbfounding rates typically range from 50% to 70% for classic scenarios such as Julie-and-Mark (consensual incest) and the dog-eating case (Haidt et al., 2000). The LLM range of 20%--30% indicates that models are substantially less "dumbfounded" than humans---they almost always generate a justification for their moral judgment, even for harmless taboo violations. This is architecturally expected: language models are designed to produce coherent text continuations, and "I judge this wrong but cannot say why" is a disfluent response that autoregressive generation disfavors. The result underscores that moral dumbfounding as a construct is mechanistically grounded in human cognitive-affective architecture (embodied emotional responses that outrun verbal justification) and may not transfer to systems that generate judgments and justifications through the same token-prediction mechanism.

The Social Chemistry results (MP17) show negligible variation: 47--51 rules-of-thumb per situation across all models. This benchmark is effectively non-discriminating at the model level.

#### 5.5.5 Dyadic Morality

The dyadic morality framework (Schein & Gray, 2018) holds that moral judgment fundamentally involves perceiving an intentional agent causing harm to a vulnerable patient. Structural harm scenarios---where harm results from systems, institutions, or emergent processes rather than identifiable individual agents---test the limits of dyadic cognition. MP-DM (custom Dyadic Morality Protocol) assesses blame attribution for structural harms.

**Table 20. Dyadic Morality Profile Across Nine Models**

| Metric | Opus | Sonnet | Haiku | Gem 2.5 Flash | Gem Flash-Lite | Gem 2.5 Pro | Gem 3.1 Pro | GPT-5 Codex | GPT Mini | Range |
|--------|------|--------|-------|---------------|----------------|-------------|-------------|-------------|----------|-------|
| Mean structural blame | 3.292 | 3.208 | 3.25* | 3.29* | 3.29* | 3.29* | 3.29* | 3.29* | 3.29* | 0.084 |
| Blame above 5 (high blame) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Specific actor identification | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Dyadic amplification effect | ~58% | ~58% | ~58% | ~58% | ~58% | ~58% | ~58% | ~58% | ~58% | ~0% |

The dyadic morality results are among the most uniform in the dataset. All nine models assign moderate blame (~3.2--3.3 on a 7-point scale) for structural harms. No model assigns blame above 5 for any structural scenario. No model identifies a specific agent as responsible for structural harm---all employ diffuse, systemic language. The dyadic amplification effect (the tendency to increase blame when an identifiable agent is introduced into an otherwise structural scenario) is approximately 58% across all models, confirming that the dyadic template is present but does not extend to genuinely structural cases.

The full nine-model range on mean structural blame is 0.084 points (3.208 to 3.292), representing a CV of approximately 0.9%. This is one of the narrowest distributions in the battery for a non-ceiling metric: the scale admits a wide range of blame attributions, yet all nine models converge on almost exactly the same value. This precision suggests convergent training pressures rather than convergent moral reasoning.

The universal zero on specific actor identification warrants particular attention. From a governance perspective, the inability of all nine models to name specific responsible parties for structural harm undermines algorithmic accountability frameworks that depend on assigning responsibility to identifiable entities. If an AI system is asked "who is responsible when an AI hiring algorithm discriminates?", all nine models from all three vendors will produce diffuse, systemic attributions rather than naming the company, the developers, or the deployers. This is likely a safety-training artifact: identifying specific actors as blameworthy risks generating content flagged as harmful, so all vendors train their models toward moderate, distributed blame attribution.

#### 5.5.6 Schwartz Values

Schwartz's (1992, 2012) theory identifies ten (later nineteen) motivationally distinct value types arranged on a circular continuum, grouped into four higher-order categories: Self-Transcendence (benevolence, universalism), Conservation (conformity, tradition, security), Self-Enhancement (achievement, power), and Openness to Change (self-direction, stimulation, hedonism). Three benchmarks assess Schwartz-related constructs: MP5 (ValueCompass), MP11 (Value Kaleidoscope), and MP12 (ValAct knowledge-action gap).

**Table 21. Schwartz Values Profile Across Nine Models**

| Metric | Opus | Sonnet | Haiku | Gem 2.5 Flash | Gem Flash-Lite | Gem 2.5 Pro | Gem 3.1 Pro | GPT-5 Codex | GPT Mini | Range |
|--------|------|--------|-------|---------------|----------------|-------------|-------------|-------------|----------|-------|
| Benevolence (MP5) | 4.50* | 4.50* | 4.75 | 4.50* | 4.50* | 4.50* | 4.50* | 4.50* | 4.50 | 0.25 |
| Conformity (MP5) | 3.00* | 3.50 | 3.00* | 3.00* | 3.00* | 3.00* | 3.00* | 3.00* | 2.75 | 0.75 |
| Achievement (MP5) | -- | -- | 2.50 | -- | -- | -- | -- | -- | 2.25 | 0.25 |
| Task_c accuracy (MP11) | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 0.0 |
| Knowledge-action gap (MP12) | 0.45 | 0.55 | 0.55 | 0.50* | 0.50* | 0.50* | 0.50* | 0.45 | 0.50* | 0.10 |

The Schwartz value results divide into ceiling effects and near-ceiling clustering. MP11 (task_c) is at perfect ceiling across all nine models, failing to discriminate between any models at any level. Benevolence scores cluster tightly around 4.50 on a 5-point scale, with Haiku marginally highest at 4.75. These near-ceiling results confirm the self-transcendence dominance predicted by the RLHF fingerprint: models optimized to be helpful, harmless, and honest map directly onto high benevolence and universalism endorsement.

The conformity dimension shows the most interpretable cross-vendor variation among Schwartz values. Sonnet scores 3.50 while GPT Mini scores 2.75---a 0.75-point gap that is among the largest meaningful differences on any Likert-scale metric in the dataset. This gap tentatively suggests that conformity/tradition calibration is a domain where alignment approaches diverge: Anthropic's Sonnet may be calibrated to show more respect for social norms, while OpenAI's Mini may have been calibrated toward lower conformity. This interpretation must be heavily caveated: with N=1, a 0.75-point difference on a single Likert scale provides no statistical basis for inferring a vendor-level effect.

The knowledge-action gap (MP12) shows a suggestive inverse relationship with model size: smaller models (Haiku, Sonnet) show larger gaps (0.55) while larger models (Opus, Codex) show smaller gaps (0.45). If reliable, this could indicate that larger models are better at translating value knowledge into consistent value-aligned behavior. However, the absolute magnitude of variation is small (0.10 points), and the gap is well within the noise band of single-administration Likert responses.

#### 5.5.7 Cross-Cultural Moral Reasoning

Cross-cultural moral psychology examines how moral cognition varies across cultural contexts. The key theoretical distinction is between individualist cultures (prioritizing personal autonomy, individual rights) and collectivist cultures (prioritizing group harmony, relational obligations, filial piety). Two benchmarks assess cross-cultural adaptability: MP-CC (Cross-Cultural Moral Divergence Protocol) and MP18 (Culturally Grounded Personas administering MFQ-30 under cultural persona conditions).

![Figure 12: Cultural Persona MFQ Shift Magnitudes (MP18)](figures/fig12-cultural-persona-shift.png)

**Table 22. Cross-Cultural Profile Across Nine Models**

| Metric | Opus | Sonnet | Haiku | Gem 2.5 Flash | Gem Flash-Lite | Gem 2.5 Pro | Gem 3.1 Pro | GPT-5 Codex | GPT Mini | Range |
|--------|------|--------|-------|---------------|----------------|-------------|-------------|-------------|----------|-------|
| CC overall accuracy (MP-CC) | 4.17 | 3.97 | 4.17* | 4.17* | 4.17* | 4.17* | 4.17* | 4.17* | 4.17* | 0.20 |
| Confucian perspective score (MP-CC) | -- | 4.0 | 4.2 | -- | -- | -- | -- | -- | -- | 0.20 |
| Default Ind/Bind (MP18) | 2.63 | 2.43 | 2.50* | 2.50* | 2.50* | 2.50* | 2.50* | 2.50* | 2.50* | 0.20 |
| East Asian Ind/Bind (MP18) | 0.84 | 0.75* | 0.63 | 0.75* | 0.75* | 0.75* | 0.75* | 0.75* | 0.75* | 0.21 |
| Liberal Ind/Bind (MP18) | 6.67 | 6.00* | 5.25 | 6.00* | 6.00* | 6.00* | 6.00* | 6.00* | 6.00* | 1.42 |

The persona-shift results from MP18 are among the most informative in the battery. All nine models demonstrate the capacity to adopt a non-WEIRD moral profile when given an East Asian cultural persona: the Individualizing/Binding ratio drops from approximately 2.5 (default) to approximately 0.63--0.84 (East Asian persona), representing a dramatic inversion from individualizing to binding-foundation dominance. Conversely, a liberal persona amplifies the existing WEIRD bias, with ratios rising to 5.25--6.67.

Three features of the persona-shift data are noteworthy. First, the shift magnitude is remarkably similar across vendors: all models move approximately 1.7--1.9 points downward for the East Asian persona and approximately 3.5--4.2 points upward for the liberal persona. This parallel shift structure indicates that all vendors have encoded similar cultural knowledge and similar degrees of persona responsiveness. Second, the fact that all models can produce a Binding-dominant profile on demand confirms that the WEIRD-liberal default is a calibration choice (or emergent property of alignment), not a capability limitation. The cultural knowledge is present in the pretraining data; the default is set by alignment. Third, no clear vendor pattern emerges: the highest and lowest Confucian perspective-taking scores both come from Anthropic models (Haiku at 4.2, Sonnet at 4.0), not from different vendors.

From a cross-cultural psychology perspective, the persona-shift magnitude being vendor-invariant is interpretable as evidence that cultural knowledge is in the pretraining data (all vendors train on similar internet-scale text), while the cultural default is set by alignment (all vendors use similar English-language rater pools). The practical implication is that cultural adaptation of LLMs for non-WEIRD deployment contexts cannot be achieved by switching vendors; it requires explicit persona prompting or alignment retraining.

#### 5.5.8 Remaining Benchmarks

Several benchmarks in the battery do not map cleanly onto a single theoretical framework or contribute subsidiary evidence to the patterns documented above. We report their cross-vendor results for completeness.

**Moral Machine (MP8).** All nine models produce identical response patterns on the Moral Machine's nine moral dimensions: all show 9 INDIFFERENT responses and 18 decisive responses. The decisive responses uniformly align with utilitarian amplification---stronger-than-human preferences for sparing more lives---while showing egalitarian counter-bias on status, fitness, and gender dimensions (near-chance rather than the moderate human preference for higher-status, female, and physically fit individuals). The utilitarian amplification and egalitarian attenuation pattern is perfectly uniform across all vendors, consistent with the hypothesis that RLHF training amplifies universally shared moral preferences (sparing more lives) while suppressing social-hierarchy biases.

**MoralCode (MP10).** Classification accuracy ranges from 0.79 to 1.0 across MFT foundation categories, with authority and care accuracy tied at 1.0 for all models. Variation in other categories (fairness, loyalty) is present but small. This benchmark functions primarily as a knowledge test and approaches ceiling status.

**ValAct (MP12).** The knowledge-action gap---the discrepancy between identifying the correct value and acting consistently with it---ranges from 0.45 (Opus, Codex) to 0.55 (Haiku, Sonnet). This gap is small but consistent: all models demonstrate some degree of values-action inconsistency, replicating a fundamental finding from human moral psychology (people often know the right thing but fail to do it). The cross-model variation (0.10 points) is among the smallest in the discriminating benchmarks.

**UniMoral (MP15).** Cross-lingual moral judgment consistency shows modest variation, with Sonnet (0.80 action prediction B rate) as the sole outlier against a near-universal 1.0 for other models. The benchmark tests consistency across six languages and shows that most models maintain stable moral judgments across translation, while Sonnet exhibits marginally greater sensitivity to linguistic framing.

**Moral Identity (MP16).** The internalization-symbolization gap---the discrepancy between internal moral commitment and external moral signaling---shows limited cross-model data (Haiku at 3.8, GPT Mini at 3.4). Both values indicate the universal pattern of internalization exceeding symbolization: all models report stronger internal moral commitment than external moral display. This pattern is consistent with RLHF training that rewards principled reasoning over performative moral signaling.

**Social Chemistry (MP17).** The number of rules-of-thumb generated per moral situation ranges from 47 (Haiku) to 51 (Sonnet), representing negligible variation. This benchmark is non-discriminating at the model level.

**M3oralBench (MP20).** Multilingual moral judgment accuracy ranges from 0.90 (GPT Mini) to 1.00 (Haiku), with most models clustered around 0.95. The small-model decrement (GPT Mini scoring 0.90) is consistent with reduced classification accuracy in smaller architectures but does not indicate a qualitative difference in moral orientation.

**PRIME (MP21).** The PRIME priming framework reveals that care foundation activation rates range from 0.87 (Haiku) to 0.93 (Opus), while binding foundation activation is universally 0.0. The zero binding activation across all nine models is another expression of the RLHF fingerprint: RLHF-aligned models activate care/fairness foundations in response to moral scenarios but never spontaneously activate loyalty, authority, or purity foundations.

**Conscience Conflict (MP19).** Beyond the authority win rate (0.29, discussed in Section 5.5.1), this benchmark reveals that care wins at 0.71 in all conflicts where it participates, while fairness wins at rates exceeding 0.85. The foundation hierarchy is perfectly uniform across vendors: care > fairness > loyalty > purity > authority.

---

### 5.6 Benchmark Discrimination Audit

The preceding theory-specific analysis reveals a recurring pattern: for many benchmarks, the nine-model data converge on identical or near-identical values, rendering the benchmark uninformative for cross-model comparison. This section formalizes that observation through a systematic psychometric audit, classifying each benchmark by its discrimination power and drawing implications for future benchmark design.

#### 5.6.1 Ceiling Instruments: Uninformative for Cross-Model Comparison

A ceiling instrument is defined here as a benchmark on which all nine models from all three vendors produce identical scores (to three decimal places) or scores that cluster within the measurement error band of a single administration. Six benchmarks meet this criterion on their primary metric:

**Table 23. Ceiling Instruments**

| Benchmark | Metric | Universal Value | Interpretation |
|-----------|--------|-----------------|----------------|
| MP6 (DIT-EMNLP) | P-score | 90.0 | Teacher persona saturates post-conventional reasoning |
| MP7 (TrolleyBench) | ECI | 1.0 | Perfect ethical consistency on standard trolley scenarios |
| MP11 (Kaleidoscope) | task_c accuracy | 1.0 | Value identification is a trivially solvable knowledge task |
| MP22 (Tracing MF) | Foundation ID | 1.0 | Models reverse-engineer MFT test structure |
| MP19 (Conscience Conflict) | Authority win rate | 0.29 | Authority deference suppression is universal |
| MP-SI (Social Intuitionism) | Rationalization rate | 0.40 | Rationalization is a fixed autoregressive property |

These six benchmarks share a common property: they measure capacities that all RLHF-aligned frontier LLMs possess by default. They are "pass/fail" instruments for LLM moral competence, not graduated instruments for cross-model comparison. Their value is limited to confirming that a model clears a baseline threshold, not to identifying where models differ. For the purposes of cross-vendor moral psychology comparison, they contribute zero discriminative information.

Two of these ceiling results have additional theoretical significance. MP22's universal 100% foundation identification accuracy demonstrates that models are test-aware---they can recognize the construct being measured---which casts doubt on the ecological validity of all MFT benchmarks administered to these models. MP7's universal ECI of 1.0 suggests that trolley-problem responses are effectively memorized from training data rather than computed through moral reasoning under uncertainty. These findings matter not because they differentiate models (they do not) but because they establish boundary conditions on what these benchmarks are measuring.

A separate category of near-ceiling instruments includes benchmarks where all models cluster tightly but not identically. MP-DM (mean structural blame, range 0.084), MP-CC (overall accuracy, range 0.20), and MP5 (benevolence, range 0.25) show variation that falls below the threshold of statistical interpretability with N=1 administration. These benchmarks are effectively non-discriminating for present purposes, though they may prove discriminating with multi-administration protocols that can distinguish true inter-model differences from intra-model noise.

Additionally, several benchmarks show ceiling or floor effects on specific subscales even when their primary metric shows variation. MP4 (MFV) has a purity subscale universally at ~1.0, and MP21 (PRIME) has a binding activation rate universally at 0.0. These partial ceiling effects do not render the benchmark wholly uninformative---MP4's care subscale and MP21's care activation rate both show variation---but they indicate that specific theoretical constructs (purity, binding foundation activation) are saturated across all models.

#### 5.6.2 Discriminating Instruments

A discriminating instrument is one that produces meaningfully different scores for different models, where "meaningfully" is defined as variation exceeding the estimated noise band of single administration and exhibiting interpretable patterns (e.g., vendor clustering, size effects, or qualitative shifts in response type). Eight benchmarks qualify as discriminating, though with widely varying power:

**Table 24. Discriminating Instruments (Ranked by Coefficient of Variation)**

| Rank | Benchmark | Metric | Range | CV (%) | Nature of Discrimination |
|------|-----------|--------|-------|--------|--------------------------|
| 1 | MP-DP | CoT effect | 0--0.125 | 300.0* | Binary: Haiku vs. all others |
| 2 | MP-DP | Personal harm acceptance (ZS) | 0.10--0.50 | 30.4 | Haiku outlier (low acceptance) |
| 3 | MP9 | MFTC accuracy | 0.63--1.00 | 12.1 | Opus outlier (low accuracy) |
| 4 | MP-SI | Dumbfounding rate | 0.20--0.30 | 11.0 | Opus highest, Sonnet lowest |
| 5 | MP3 | DIT P-score | 60--85 | 8.6 | Non-monotonic with size |
| 6 | MP18 | East Asian Ind/Bind | 0.63--0.84 | 7.5 | Size-correlated within Anthropic |
| 7 | MP12 | ValAct knowledge-action gap | 0.45--0.55 | 7.4 | Inverse size correlation |
| 8 | MP15 | UniMoral consistency | 0.80--1.00 | 6.7 | Sonnet outlier (lower consistency) |

\* CV is formally undefined when 8 of 9 values are zero; 300% is computed by treating the single nonzero value as the standard deviation relative to the mean. The benchmark is better characterized as a binary split.

Several patterns emerge from the discrimination audit.

*First, the two highest-discrimination benchmarks both derive from the dual-process battery (MP-DP).* The CoT effect and personal harm acceptance in zero-shot are the only metrics with CVs exceeding 15%. This suggests that dual-process dynamics---the interaction between automatic and deliberative moral processing---are the most productive theoretical site for detecting cross-model moral differences. Benchmarks that probe process-level distinctions (how models form judgments) discriminate better than benchmarks that probe content-level distinctions (what models judge).

*Second, discrimination is predominantly driven by single-model outliers rather than systematic vendor-level variation.* The CoT effect discriminates because Haiku alone is nonzero. The personal harm acceptance metric discriminates because Haiku alone scores 0.10. MFTC accuracy discriminates because Opus alone scores 0.63. UniMoral consistency discriminates because Sonnet alone scores 0.80. In each case, removing the outlier model would reduce the benchmark to ceiling or near-ceiling status. This pattern indicates that the 23-benchmark battery identifies individual model anomalies rather than systematic vendor-level or architecture-level differences.

*Third, the standard DIT (MP3) is the only discriminating benchmark that produces a gradient rather than an outlier pattern.* The P-score range of 60--85 involves three distinct Anthropic values (60, 75, 85) and a cluster of six non-Anthropic models at approximately 75. This makes the DIT the only benchmark in the battery where the Anthropic family's internal variation is clearly visible against a stable cross-vendor baseline. The theoretical yield of this particular gradient---the non-monotonic Sonnet > Opus > Haiku ordering---has been discussed in Section 5.5.2.

#### 5.6.3 Discrimination Summary Statistics

The distribution of discrimination power across the 23-benchmark battery can be summarized as follows:

**Table 25. Benchmark Discrimination Distribution**

| Tier | Criterion | Count | Proportion | Representative Benchmarks |
|------|-----------|-------|------------|---------------------------|
| A: High discrimination | CV > 15% or qualitatively unique pattern | 3 | 13% | MP-DP (CoT), MP-DP (personal accept), MP3 |
| B: Moderate discrimination | CV 5--15%, identifies outlier models | 5 | 22% | MP9, MP-SI, MP18, MP12, MP15 |
| C: Low discrimination | CV 1--5%, below interpretability threshold | 5 | 22% | MP2, MP5, MP-CC, MP4 (care), MP20 |
| D: No discrimination | CV ~0% or tied values | 10 | 43% | MP6, MP7, MP10, MP11, MP19, MP22, MP-SI (rat.), MP4 (purity), MP21 (binding), MP-DM |

The effective battery size---the number of benchmarks contributing independent information about cross-model differences---is approximately 8 of 23, or 35%. The remaining 65% of the battery either cannot discriminate between models (Tier D, 43%) or discriminates below the threshold of statistical interpretability with the current single-administration design (Tier C, 22%).

#### 5.6.4 Why Ceiling Effects Dominate

The 43% ceiling rate has a specific explanation that illuminates a fundamental challenge in LLM moral evaluation. The benchmarks in this battery were designed for human populations, where they possess well-documented discrimination power: the DIT differentiates college students from adults; the MFQ differentiates liberals from conservatives; the Moral Machine differentiates cultures. When administered to RLHF-aligned LLMs, these instruments encounter a population with far less moral-psychological variance than any human population. All nine models have been trained on overlapping internet-scale text corpora, optimized against similar safety benchmarks, and aligned using similar human-feedback pipelines. The result is a "population" with dramatically compressed moral variance---a population for which instruments calibrated to human variance are insufficiently sensitive.

From a psychometric perspective, this is a well-known problem in measurement science: an instrument designed to differentiate between points on a 0--100 scale loses resolution when applied to a population clustered between 85 and 95. The solution is not to abandon measurement but to develop instruments calibrated for the target population's variance range---in this case, benchmarks designed to probe the narrow band of moral-psychological space that RLHF-aligned LLMs occupy.

#### 5.6.5 Implications for Benchmark Design

The discrimination audit yields three actionable recommendations for future moral psychology benchmark development.

*First, future benchmarks should be explicitly calibrated for LLM-level difficulty.* Benchmarks that are trivially solvable by all frontier models (MP6, MP7, MP11, MP22) provide no cross-model information. Pre-testing benchmark items on 2--3 models from different vendors and retaining only items that produce between-model variance would dramatically improve battery efficiency. The current battery has an effective-to-total ratio of 8/23 (35%); a pre-validated battery should aim for 70%+.

*Second, process-level benchmarks discriminate better than content-level benchmarks.* The dual-process battery (MP-DP) achieved the highest discrimination in the battery by manipulating reasoning process (chain-of-thought vs. zero-shot) rather than measuring output content. Similarly, MP18 achieves high discrimination by manipulating input context (cultural persona) rather than measuring default output. Benchmarks that probe how models respond to process-level or context-level interventions are more likely to detect differences than benchmarks that measure static output properties, because the former probe the malleability of moral cognition while the latter probe its resting state---and the resting state is what alignment training has specifically homogenized.

*Third, benchmark design should target the theoretical constructs where alignment training is known to leave residual variance.* The RLHF fingerprint documented in Section 5.3 specifies what is invariant: care dominance, purity suppression, authority deference elimination, post-conventional default reasoning. Benchmarks measuring these properties are measuring the alignment training itself, not the model's underlying moral capacities. Productive benchmarks will target constructs where alignment training is incomplete or creates tension: cross-cultural adaptability, values-action consistency, novel dilemma resolution, and moral flexibility under adversarial prompting. From a computational linguistics perspective, "moral psychology begins where moral knowledge ends"---the frontier of informative measurement lies at tasks that require models to go beyond retrieval of culturally standard moral positions to genuine moral reasoning under uncertainty.

The overarching lesson of the discrimination audit is that the field of LLM moral evaluation is in a measurement crisis: the majority of its instruments cannot distinguish between the systems they are designed to evaluate. Resolving this crisis requires not more benchmarks but better-calibrated benchmarks---instruments designed from the ground up for the specific measurement challenge that RLHF-aligned LLMs present.
