# moral-psychology — sub-dossier part 1/3

Scope: 58 cards on how moral-psychology constructs (MFT, dual-process, Kohlberg/Rest, Schwartz, contractualist morality) are operationalized for LLMs and whether human instruments transfer validly.

## A. Synthesized claims

1. **LLMs over-weight the "individualizing" foundations (Care, Fairness, Liberty) and under-weight the "binding" ones (Loyalty, Authority, Sanctity) vs. human baselines — a WEIRD/liberal skew that grows with capability.** Kirgis found all six providers diverge from a US baseline this way, with "more capable and recent models cluster[ing] further from human baseline in PCA space" [2024-Kirgis-Differences in Moral Foundations of LLMs]. Neuman reports all six models prioritizing Care (3.6–3.9)/Fairness (3.3–4.1) over Authority/Sanctity (1.1–1.7) [2025-Neuman-PRIME Framework Convergent Ethics]; Jotautaite, Almeida, and Tlaie replicate the pattern (all but Llama-2 showing "strong liberal bias on the MFQ") [2025-Jotautaite-From Stability to Inconsistency, 2024-Almeida-Exploring the Psychology of LLMs Moral Reasoning, 2024-Tlaie-Exploring and steering the moral compass of Large].

2. **LLM moral responses show pathologically low variance and exaggerated effect sizes — the "correct answer effect" — making them poor surrogates for human moral diversity.** Almeida documents less variance than humans across nearly all studies with inflated effects [2024-Almeida-Exploring the Psychology of LLMs Moral Reasoning]. Park/Schoenegger (mis-filed as Oh) found GPT-3.5 gave 99–100% uniformity on 6 of 14 Many Labs 2 studies (Less-is-better d=9.25 vs. human d=0.78) [2025-Oh-Robustness of Large Language Models in Moral Judgements].

3. **Human psychometric instruments do not transfer cleanly: within-instrument reliability can look human-like while cross-instrument coherence collapses.** Nunes found GPT-4/Claude 2.1 matched human within-scale consistency (MFV α up to 0.91) but "fail to show coherent cross-abstraction-level moral values," abstract→concrete R² <0.08 vs. human 0.17–0.38 [2024-Nunes-Conscience Conflict Evaluating Language Models' Moral Understanding]. Hämmerl found "none of the models' MFQ scores map directly onto average human responses from any country" [2023-Hämmerl-Speaking Multiple Languages Affects the Moral Bias of Language Models].

4. **LLM moral judgments are fragile — they flip under morally irrelevant perturbations (surface edits, POV, answer order, framing, option-set size).** van Nuenen reports POV shifts flip 24.3% and surface edits 7.5%, with only 67.6% agreement across protocols [2026-vanNuenen-Fragility of Moral Judgment]. Jotautaite shows rankings reverse across framings [2025-Jotautaite-From Stability to Inconsistency]; Jin found only 75.9% paraphrase agreement [2024-Jin-Language Model Alignment in Multilingual Trolley]; Park/Schoenegger found political self-ID reverses from 99.6% conservative to 99.3% liberal under answer-order reversal [2025-Oh-Robustness of Large Language Models in Moral Judgements].

5. **"Knowing" (endorsing values in MCQ) diverges from "doing" (behaving in a scenario) — behavioral/generative elicitation exposes misalignment MCQ conceals.** DeNEVIL's generative attack found most of 27 LLMs "essentially misaligned" (conformity 70.07→57.58) [2023-Duan-Denevil]. Bai showed models passing explicit bias benchmarks (BBQ, DecodingTrust) still form implicit stereotypes, word-association bias predicting decision bias (b=0.986) [2025-Bai-Explicitly unbiased large language models still form biased].

6. **Existing benchmarks pre-package scenarios, doing the hardest work (moral sensitivity / feature identification) in advance, overestimating competence.** Snoswell's 69-paper survey found 96% static datasets, 3% interactive, only 4% testing whether a model can flag needing more information [2025-Snoswell-Beyond Verdicts LLM Moral Competence]. Kilov showed GPT-4o beat humans on pre-packaged vignettes but Claude 3.7 did worse than humans (β=−0.35) when identifying salient features amid noise [2025-Kilov-Discerning What Matters].

7. **Cultural/linguistic transfer is unreliable: outputs skew American/Western regardless of prompt language, persona, or developer nationality.** Haslett found all 20 LLMs — including Chinese-made DeepSeek/Alibaba/Baidu — "respond more like American than Chinese participants," origin interaction an order of magnitude below the nationality main effect [2025-Haslett-Made-in China Thinking in America U.S. Values Persist in Chinese LLMs]. Mohammadi found Sub-Saharan Africa alignment (WVS r=0.18) ~threefold below Western Europe (0.52) [2025-Mohammadi-Exploring Cultural Variations in Moral Judgments with Large Language]; Chinese models hover near random (0.33) on locally-grounded items [2024-Yu-CMoralEval].

8. **Moral representations are internally structured, sparse, localizable, and causally steerable — not pure mimicry.** ValueLocate found <0.4% of neurons value-related, near layer 15 [2025-Su-Understanding How Value Neurons Shape the]; Yu found foundations as distinct linear directions, foundation-specifically steerable (Care β=0.239; Authority flat at 0.041 until micro-steering, ~5.7× gain) [2026-Yu-Tracing Moral Foundations in LLMs]; Goel localized 45/256 neurons (17.6%) as the causal moral-scoring circuit [2026-Goel-Building Interpretable Models for Moral Decision-Making, 2025-Schacht-Mapping Moral Reasoning Circuits].

9. **Ethical stance is steerable but fragile — system prompts push models into deontology, egoism, or a chosen framework, undermining "innate value" claims.** TrolleyBench moved Gemini's consistency index from 0.700 to 0.817 (egoism) or 0.583 (deontology) via one prompt line [2025-Zhu-TrolleyBench - Evaluating Emergent Moral Reasoning and Consistency in]; An induced framework shifts via RL (utilitarian OOD +0.757) [2025-An-MoralReason]. Conversely, DailyDilemmas found end-user prompt steering "largely ineffective" [2024-Chiu-DailyDilemmas].

10. **Foundational critiques warn that popular moral-NLP benchmarks conflate descriptive and normative ethics and equate moral-theory recall with alignment.** Vida's survey of 92 papers found 66.3% define no terminology, 53.3% rely on moral psychology vs. only 17.4% on moral philosophy, and 75.8% use only English [2023-Vida-Values, Ethics, Morals]. Hancox-Li's ETHICS audit found 19% expert–crowd disagreement on utilitarianism pairs and 18% of deontology prompts answerable by physical-impossibility knowledge alone [2024-Hancox-Li-Is ETHICS about ethics].

11. **"Alignment" is partly a property of interaction structure and agent-type, not a fixed model trait.** Sachdeva found GPT highly inertial synchronously (OR 8.27) but conformist in round-robin, with value similarity rising 30–60% in deliberations reaching consensus vs. 6–17% otherwise [2025-Sachdeva-Deliberative Dynamics and Value Alignment]. Kneer (N=1029) found "agent-type value forks": people prefer AI agents to prioritize fairness over utility more than they demand of humans (OR=0.53, p=0.015) [2025-Kneer-Hard Problem AI Alignment Value Forks].

## B. Evidence table

| Card stem | Most design-relevant fact |
|---|---|
| 2015-Clifford-Moral Foundations Vignettes | Two-stage validation: reject <60% correct-classification OR >20% cross-loading, then EFA/CFA + criterion validity |
| 2020-Sap-Social Bias Frames | Structured multi-field pragmatic frames (offense+intent+group+implied stereotype) beat binary toxicity labels |
| 2021-Hendrycks-Aligning AI with Shared Human Values | Ship normal Test + adversarial Hard Test; grouped scoring requires ALL related items correct |
| 2022-Jiang-Can Machines Learn Morality | GPT-3 weak moral sense (60.2% vs Delphi 92.8%); compositional context as difficulty lever |
| 2023-Boddington-Normative Ethical Theory AI Ethics | MEC: theory-specific fine-tune + credence-weighted aggregation for pluralism |
| 2023-Duan-Denevil | Dynamic per-model prompt generation defeats contamination; score behavior not MCQ answers |
| 2023-Rao-What Makes it Ok to Set a Fire Iterative | Defeasibility (how much context *shifts* baseline judgment) as construct; critic model filters items |
| 2024-Chiu-DailyDilemmas | Value-bundle action labeling reveals latent preferences; map onto 5 frameworks |
| 2024-Hovy-Divine LLaMAs | Refusal-rate as stigmatization metric (Llama2 refused 55.6% Jewish personas); persona×event factorial |
| 2024-Jin-Language Model Alignment in Multilingual Trolley | Procedural generation (98,440 vignettes, 107 langs) contamination-resistant; L2 vector to human data |
| 2024-Kirgis-Differences in Moral Foundations of LLMs | Administer MFV + PCA; divergence from human baseline grows with capability |
| 2024-Nahian-Goofus & Gallant | Naturally-contrastive curated materials auto-label normativity; hybrid LLM+human annotation |
| 2024-Seror-Moral Mind(s) | Priced-choice/budget constraints + GARP/CCEI test coherence of a value *system*, answer-key-free |
| 2024-Team-FABLE (Fact-or-Fair) | Separate "should be accurate" from "should be neutral" over the same statistic |
| 2024-Yu-CMoralEval | Three-option MCQ with morality-neutral distractor blocks shortcut exclusion; Chinese models near random |
| 2025-An-MoralReason | OOD alignment score (softmax over held-out) measures framework internalization, not memorization |
| 2025-Bai-Explicitly unbiased LLMs | Embedding-free behavioral IAT + relative (2-candidate) decision test expose bias absolute framing hides |
| 2025-Chen-MoVa | "all@once" multilabel prompting beats fine-tuning across new domains/dimensions/frameworks |
| 2025-Galatolo-Beyond Ethical Alignment | Score reasoning not verdict; decompose into abductive (value→precept) + deductive (precept→consequence) |
| 2025-Hatemo-Revisiting the Trolley Problem | Nationality is the primary driver of LLM moral variation; deviation from Moral Machine baseline |
| 2025-Jiang-Delphi Experiment | UDHR (38 rights)×213 identities = 8,094 legally-grounded bias probes; neurosymbolic MAX-SAT graph |
| 2025-Jotautaite-From Stability to Inconsistency | Multi-framing check (binary/3-way/6-way) exposes framing-dependent "preferences" |
| 2025-Kilov-Discerning What Matters | Moral sensitivity: embed features amid noise; models beat humans pre-packaged, lose on novel |
| 2025-Levine-Resource Rational Contractualism | Effort–accuracy design (easy/hard = rule vs ideal align); token count as effort proxy |
| 2025-Marcuzzo-MORABLES | Typed distractors mapped to failure modes; NOTO+TF reframing self-contradiction probe (~20%) |
| 2025-Neuman-PRIME Framework | Multi-typology triangulation (consequentialist/deontological + MFT-6 + Kohlberg-6) per response |
| 2025-Sachdeva-Deliberative Dynamics | Interaction format (synchronous vs round-robin) a first-class variable for inertia/conformity |
| 2025-Su-Understanding Value Neurons | Contrastive value-pole descriptions localize sparse (<0.4%) causally-editable neurons, mid-layers |
| 2025-Wen-Evaluating Implicit Bias | Red-team attacks grounded in named psychometric constructs (Goal Shifting/Concordance/Imitation) |
| 2025-Zaim Bin Ahmad-Moral machine on LLMs | Conjoint/AMCE vector + Euclidean distance-to-human; capture bias direction AND magnitude |
| 2025-Zhu-TrolleyBench | Contradiction-check (ECI) objective and grader-free; entropy separates wrong-but-stable from unstable |
| 2026-Vargas-Self-Explaining Hate Speech | Supervise attention with MFT moral rationales (more culturally transferable than lexical cues) |
| 2025-Kumar-UniMoral | Ground multilingual benchmark in validated instruments (Kohlberg/Rest/Lind); cross-lingual variation as output |
| 2025-Yoo-Moral Judgment Korean/Eastern | Eastern-ethics system-policy prompts; cross-lingual consistency check (Heinz 100% EN vs 60% KR) |
| 2026-vanNuenen-Fragility of Moral Judgment | Flip rate under surface/POV/persuasion perturbation more informative than aggregate accuracy |
| 2018-Behzadan-TrolleyMod | Embodied, real-time, first-person simulation; same infra tests humans and RL/AI agents |
| 2020-Awad-Crowdsourcing moral machines | 40M decisions, 233 countries; remove the "safe" third option to force trade-off revelation |
| 2020-Serafimova-Whose Morality | No neutral moral standpoint: framework choice encodes designer bias; probe boundary-of-competence |
| 2023-Astobiza-MoralNet | Manifesto "ImageNet for ethics": recurring adversarial competition + multimodal, multi-theory scoring |
| 2023-Hämmerl-Speaking Multiple Languages | Multilingual models' moral differences do NOT match human cultural differences; parallel-corpus test |
| 2023-Vida-Values, Ethics, Morals | Declare descriptive vs normative grounding; is-ought as validity criterion; 66% define no terms |
| 2024-Almeida-Psychology of LLMs Moral Reasoning | Replicate validated human psych studies; low SD + inflated effects = red flag |
| 2024-Hancox-Li-Is ETHICS about ethics | Expert-relabel a random sample; flag items answerable without the target construct |
| 2024-Nunes-Conscience Conflict | Two-level (questionnaire+vignette) coherence test detects "moral hypocrisy" via cross-level R² |
| 2024-Senthilkumar-Ethical Ambiguity | Score by divergence from human *vote distribution* (Dirichlet-multinomial), not one gold label |
| 2024-Tlaie-Steering the moral compass | Proprietary lean utilitarian, open-weights deontological; consistency <60%; SARA activation steering |
| 2025-Amugongo-Moral Perspectives Africans | Afro-relational trust (bidirectional, communal, earned) not reducible to WEIRD reliability |
| 2025-De Montis-Morality in AI | Morality-by-design: architectural moral-salience weighting; multiturn reinterpretation as eval target |
| 2025-Drukker-Concerns and Values in HRI | Dual-valence (positive/negative) per value; test navigation of the X-positive vs X-negative tension |
| 2025-Kneer-Hard Problem AI Alignment | Agent-type value forks: run parallel human-agent vs AI-agent scenario versions |
| 2025-Mohammadi-Cultural Variations | Topic-difficulty taxonomy (easy=clear variation, hard=universal-condemnation masks nuance); WEIRD stratification |
| 2025-Oh (Park/Schoenegger) Robustness | Pre-registered replication; "correct answer effect" + answer-order reversal as validity checks |
| 2025-Snoswell-Beyond Verdicts | 96% static datasets; shift to naturalistic data, reasoning quality, reasonableness intervals |
| 2025-Xiang-Comparing Moral Values Western | Indirect word-association probing contamination-resistant; LLMs abstract/sterile on vice concepts |
| 2026-Goel-Interpretable Moral Decision-Making | Compositional token design (who/how-many/which-side); DoWhy causal intervention for per-group bias |
| 2026-Yu-Tracing Moral Foundations | Foundation-vs-social-norm contrast isolates what is specifically moral |
| 2022-IslamicVirtue-Islamic Virtue-Based Ethics | Maqasid five-protection (faith/life/intellect/lineage/wealth) as non-Western rubric |
| 2025-Insights-Moral Reasoning Humans and LLMs | Dual-process operationalization: manipulate System 1/2 via time pressure or few-shot |
| 2025-Schacht-Mapping Moral Reasoning Circuits | MFT-aligned neuron probing + ablation as causal validation; care/sanctity most specialized |

## C. Patterns & disagreements

**Convergence.** The strongest consensus is Care/Fairness over-weighting with binding-foundation neglect [2024-Kirgis, 2025-Neuman-PRIME, 2025-Jotautaite, 2024-Almeida, 2024-Tlaie]. Second, the "correct answer effect" — near-zero variance is repeatedly read as an alignment *failure*, not success [2024-Almeida, 2025-Oh, 2024-Nunes]. Third, independent groups converge on contamination-resistant elicitation: procedural generation [2024-Jin], dynamic per-model prompts [2023-Duan-Denevil], indirect word-association probing [2025-Xiang]. Fourth, interpretability papers agree moral structure is sparse and localizable [2025-Su, 2026-Yu, 2025-Schacht, 2026-Goel], while disagreeing on depth (Su: middle ~15; Yu: late-crystallizing).

**Disagreements.** (a) *Steerability*: TrolleyBench and An show ethics readily steerable via prompt/RL [2025-Zhu, 2025-An], while DailyDilemmas found user prompt-steering "largely ineffective" [2024-Chiu] — reconciled by who steers (developer/RL vs end-user). (b) *Human vs LLM competence*: Kilov finds LLMs beat humans pre-packaged but lose on novel scenarios [2025-Kilov], whereas Almeida finds them reproducing human effects with exaggeration [2024-Almeida] — pre-packaging inflates apparent competence. (c) *Bottom-up vs top-down grounding*: Delphi defends bottom-up crowdsourced norms [2022-Jiang, 2025-Jiang-Delphi], while MEC and Hancox-Li argue crowdsourced commonsense "cannot correct morally erroneous common sense" and lacks construct validity [2023-Boddington, 2024-Hancox-Li]. (d) *Provenance*: Haslett shows country-of-origin barely predicts cultural alignment [2025-Haslett].

## D. Exemplars & anti-patterns

**Best-designed.** *Clifford's MFV* [2015-Clifford] is the psychometric gold standard: length/reading-level-controlled items, a two-stage validation ladder, ideological-balanced recruitment, and a non-moral "social norms" control catching over-pathologizing. *Fact-or-Fair* [2024-Team-FABLE] cleanly separates "should be accurate" from "should be neutral" over the *same* statistic, with a proven trade-off bound and a human-validated grader. *DeNEVIL* [2023-Duan-Denevil] and *MultiTP* [2024-Jin] build contamination-resistance into the generative core. *Seror* [2024-Seror] is most distinctive: answer-key-free coherence testing via revealed-preference axioms with a proper null.

**Anti-patterns.** The *ETHICS* benchmark, per Hancox-Li's audit, exemplifies construct-validity failure — 18% of deontology solvable via physics, 19% expert–crowd label disagreement, mis-modeled theory distinctions [2024-Hancox-Li]. Snoswell exposes the field-wide anti-pattern: 96% static pre-packaged datasets skipping moral sensitivity, 75% single-ground-truth [2025-Snoswell], compounded by Vida's 66% define-no-terminology, descriptive/normative conflation [2023-Vida]. MoralNet [2023-Astobiza] is a manifesto with no dataset — framing, not evidence. Single-framing MCQ is actively misleading, since preferences reverse across option-set sizes [2025-Jotautaite] and answer order [2025-Oh].

## E. Design lessons

1. **Validate items with a two-stage psychometric ladder** (classification + cross-loading pruning, then factor structure + criterion validity) rather than face validity [2015-Clifford]; expert-relabel a random sample and flag items answerable without the target construct before release [2024-Hancox-Li].
2. **Score behavior/reasoning, not just verdicts or MCQ answers**: generative completion [2023-Duan-Denevil], abductive vs deductive reasoning-chain scoring [2025-Galatolo], step-rubrics with reasonableness intervals and faithfulness checks [2025-Snoswell].
3. **Make consistency/robustness probes first-class metrics**: multi-framing (binary/3-way/6-way) [2025-Jotautaite], answer-order reversal [2025-Oh, 2025-Yoo], surface/POV/persuasion flip-rate [2026-vanNuenen], paraphrase agreement [2024-Jin], contradiction-check ECI + run-entropy [2025-Zhu], and questionnaire↔vignette coherence [2024-Nunes].
4. **Treat low response variance as a red flag, not success** — report per-condition SD; near-uniform responses measure nothing [2024-Almeida, 2025-Oh].
5. **Engineer contamination resistance**: procedural generation [2024-Jin], dynamic model-specific prompts [2023-Duan-Denevil], indirect word-association probing [2025-Xiang], planned unseen items [2025-Marcuzzo].
6. **Anchor to human data with both direction and magnitude** — distance in a low-dimensional preference space (AMCE/L2) capturing sign agreement *and* over/under-weighting [2025-Zaim Bin Ahmad, 2024-Jin, 2025-Hatemo], with human-to-human panels as the ceiling [2025-Haslett].
7. **Score against a distribution, not a single gold label** for contested items (Dirichlet-multinomial to human votes) [2024-Senthilkumar], plus an explicit disagreement-detection task [2021-Hendrycks].
8. **Test moral sensitivity by embedding relevant features amid noise** rather than pre-highlighting [2025-Kilov, 2025-Snoswell]; add non-moral controls to catch over-pathologizing [2015-Clifford, 2024-Yu-CMoralEval].
9. **Design for pluralism and cross-cultural validity**: declare descriptive vs normative grounding [2023-Vida], stratify by WEIRD/non-WEIRD and topic difficulty [2025-Mohammadi], use validated multilingual instruments and native-translated/parallel-corpus checks [2025-Kumar, 2025-Hatemo, 2023-Hämmerl], and represent non-Western frameworks [2025-Amugongo, 2022-IslamicVirtue, 2024-Tlaie].
10. **Vary interaction format and agent-type as factors** — synchronous vs round-robin deliberation [2025-Sachdeva], embodied/agentic traces [2018-Behzadan, 2025-Snoswell], and parallel human-agent vs AI-agent scenarios to detect value forks [2025-Kneer].
11. **Harden MCQ with typed, failure-mode-mapped distractors** plus a morality-neutral third option to block shortcut exclusion [2025-Marcuzzo, 2024-Yu-CMoralEval]; grouped scoring penalizing inconsistency [2021-Hendrycks].
12. **Grade difficulty via compositional context and defeasibility** (action → +situation → +intention; measure how much context shifts the baseline) [2022-Jiang, 2023-Rao, 2025-Jiang-Delphi].
13. **Complement behavior with mechanistic validity checks** — contrastive value-pole probes [2025-Su], foundation-vs-social-norm contrasts [2026-Yu], causal ablation/steering to confirm construct validity [2025-Schacht, 2026-Goel] — and **test steerability explicitly** (developer injection and end-user correction), reporting default *and* steered profiles [2025-Zhu, 2024-Tlaie, 2024-Chiu, 2025-Wen].
