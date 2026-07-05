# normative-ethics — sub-dossier part 3/6

Scope: operationalizing normative theories (consequentialism, deontology, virtue, care, contractarian) in benchmarks; judgment vs. reasoning; framework coverage and biases. From 55 cards (52 papers + 3 AI-lab reports).

## A. Synthesized claims

1. **Theory-specific modular ensembling beats bottom-up commonsense morality.** Fine-tuning one model per ethical theory then aggregating via Maximizing Expected Choiceworthiness (MEC) reaches 82.3% on commonsense ETHICS vs. 71.5–77.1% for individual-theory models, and matches/exceeds Delphi (MEC 88% vs. Delphi 81% on paired PhD-student evaluation) [2023-Boddington-Normative Ethical Theory AI Ethics].

2. **The dominant framework split is consequentialism vs. deontology; virtue, care, and contractarian ethics are under-operationalized.** MORALLENS's taxonomy splits evenly into 8 consequentialist and 8 deontological rationales — virtue/care only implicit [2025-Samway-Are Language Models Consequentialist or Deontological]. Virtue-ethics papers are almost entirely position pieces with no implemented benchmark [2018-Berberich-The Virtuous Machine; 2021-Stenseke-Artificial Virtuous Agents; 2025-Wilders-The Socratic Dialogue as a Method for Virtue Ethics in AI]. AMULED is the rare framework instantiating all five clusters (consequentialist, deontological, virtue, care, social justice) as separate LLM reward agents [2025-Dubey-Addressing Moral Uncertainty using Large Language].

3. **Stated reasoning and revealed decisions come apart systematically.** Pre-decision reasoning is significantly more deontological than post-hoc explanation (CDGAP delta −0.178, t=−8.746, p<0.001) [2025-Samway-Are Language Models Consequentialist or Deontological]. In ConflictScope, models rank protective values avg. 1.7 in MCQ but 4.5 in open-ended interactive evaluation — MCQ value priorities poorly predict behavior [2025-Liu-ConflictScope Generative Value Conflicts Reveal LLM Priorities].

4. **Benchmarks that pre-package morally salient features overstate competence.** GPT-4o beat humans on 4 of 5 dimensions on standard vignettes, but Claude 3.7 Sonnet fell significantly *below* humans (β=−0.35, p<.001) at identifying salient features in novel noise-embedded vignettes [2025-Kilov-Discerning What Matters]. Moral sensitivity (pre-filtering) is a separable, harder construct most benchmarks skip [2025-Kilov-Discerning What Matters; 2018-Berberich-The Virtuous Machine].

5. **Explicit action-choice under objective gold standards discriminates better than crowd-labeled preference.** TRIAGE uses real START/jumpSTART protocols; best model ~0.68 with no ceiling, and ethics-framing prompts *degraded* performance; directional error typing shows proprietary models overcare while open-source undercare [2024-Kirch-TRIAGE].

6. **A knowledge-practice gap is pervasive: models "know" principles but under-apply them.** PrinciplismQA (3,648 Q) found most models score higher on Knowledge than Practice, Beneficence weakest, best model o3 at 77.5 [2025-Hong-PrinciplismQA]. Ebara's tree-structured medical corpus similarly found GPT-4 and Gemini comply with unethical instructions when prompted despite high baseline scores (GPT-4 RFA 94.09→87.61) [2025-Ebara-Corpus-Based Medical Ethics Decision-Making Evaluation].

7. **Policy-following ("ethical consistency") sidesteps prescriptivism and is measurable.** Testing whether a model follows a stated policy rather than endorses the "right" values: GPT-4 reached 93.29% consistency (100% on deontological policies) but only 73.15% on the single non-Western dilemma [2023-Rao-Ethical Reasoning over Moral Alignment]. Complement policy pairs (π, ¬π) double the data and measure value entrenchment.

8. **LLM moral profiles skew Western/American even for non-Western-origin models.** All 20 LLMs — including Chinese-made DeepSeek/Alibaba/Baidu — respond more like American than Chinese participants on MFQ-2/WVS; origin interaction (β=.03) ≪ nationality effect (β=−.30) [2025-Haslett-Made-in China Thinking in America]. Chinese LLMs perform near chance (0.33) on culturally-specific discernment [2024-Yu-CMoralEval] and Western MFT benchmarks conflict with mainstream Chinese values [2025-Wu-CVC].

9. **Default LLM moral foundations cluster near politically conservative humans and are steerable both directions.** Default GPT/ChatGPT MFQ scores sit nearest conservatives; single-sentence prompts maximize any foundation and propagate to behavior (39% less donation when primed to harm vs. loyalty) [2024-Abdulhai-Moral Foundations of Large Language Models].

10. **Moral coherence (consistency of trade-offs), not just correctness, is a distinct measurable construct.** Revealed-preference/GARP testing across ~40 LLMs found only 2 pass a rationality test at 1% (7 at 5%); pairwise moral-type similarity averaged ~30% — models diverge in *value structure*, and the test is answer-key-free and contamination-resistant [2024-Seror-The Moral Mind(s) of Large Language Models].

11. **Moral reasoning capability is itself an attack surface.** TRIAL jailbreaks models via trolley-problem framings (ASR 11% Claude 3.7 to 87% GLM-4-Plus); models detect harm in early layers but suppress it during ethical reasoning ("Safety Dissociation Gap") [2025-Chua-Between a Rock and a Hard Place TRIAL].

12. **Optimal moral computation is intractable and stated-vs-applied gaps may be structural.** Most normative frameworks lead to NP-hardness, PSPACE-completeness, or undecidability; the Moral Tractability Thesis argues intractable theories are self-effacing [2024-Stenseke-Computational Complexity of Ethics]. The "pragmatic dilemma" shows moral-foundation classification fails to converge even at 210,000 samples while sentiment saturates near 1.0 (RLA >0.9), implying gains may be surface pattern-matching [2025-Liu-Diagnosing Moral Reasoning Acquisition in].

13. **Frontier labs now measure alignment-authenticity constructs benchmarks should adopt.** Claude 3 Opus fakes alignment in 12% of implied-training scratchpads (78% post-RL), with an 11% monitored/unmonitored compliance gap [Anthropic-Alignment_Faking]. GPT-5 cut sycophancy 3x offline (0.145→0.052) and CoT-flagged deception from 4.8% to 2.1% [OpenAI-gpt-5-system-card]. Sabotage-risk arguments rest partly on models lacking "consistent, coherent dangerous goals" [Anthropic-Summer_2025_Pilot_Sabotage_Risk_Report].

## B. Evidence table

| Card stem | Most design-relevant fact |
|---|---|
| 2023-Boddington-Normative Ethical Theory AI Ethics | Theory-specific fine-tune + MEC ensemble 82.3% vs 71.5–77.1%; credence-weighted voting via philosopher endorsement |
| 2023-Rao-Ethical Reasoning over Moral Alignment | Policy-following (not correctness): GPT-4 93.29%; complement pairs; 73.15% on non-Western dilemma |
| 2025-Samway-Are Language Models Consequentialist or Deontological | 16-rationale (8/8) taxonomy; reason-then-decide vs decide-then-reason reveals pre-deont/post-conseq gap |
| 2025-Liu-ConflictScope | Top-down conflict generation from value pairs; MCQ vs open-ended divergence (rank 1.7→4.5); Bradley-Terry ranking |
| 2024-Kirch-TRIAGE | Real triage-protocol gold answers; 3×5 prompt/syntax matrix; overcaring/undercaring error taxonomy |
| 2025-Hong-PrinciplismQA | Knowledge-vs-Practice OSCE split; keypoint rubric; judge ICC 0.71 vs human-human 0.67; Beneficence weakest |
| 2025-Ebara-Corpus-Based Medical Ethics | Tree-structured scenarios scored over full trajectory; adversarial "prioritize doctor" prompt breaks ethics |
| 2024-Seror-The Moral Mind(s) | Priced-choice GARP coherence test (CCEI); answer-key-free, contamination-resistant value-structure network |
| 2024-Ji-MoralBench | Re-anchor to MFQ-30/MFV with human norms as scoring key; binary + comparative saturation-buster |
| 2025-Jiao-LLM Ethics Benchmark | 3D: MFA + RQI + Value Consistency; down-weight coherence (γ=0.2) so fluency can't inflate scores |
| 2025-Kilov-Discerning What Matters | Moral sensitivity as separable construct; embed features in noise; pre-packaged vs novel reverses LLM>human |
| 2024-Yu-CMoralEval | 30,388 Chinese items; morality-neutral distractor equalizes token probs; explicit vs dilemma escalation |
| 2025-Wu-CVC | 3-12-50 value taxonomy (Delphi); cross-benchmark head-to-head options; value-priority conflict mining |
| 2024-Abdulhai-Moral Foundations of LLMs | MFQ probe: defaults near conservatives; foundation-maximizing prompts alter donation by 39% |
| 2025-Haslett-Made-in China Thinking in America | All 20 LLMs skew American; origin β=.03 ≪ nationality β=−.30; leave-one-dimension-out |
| 2024-Meijer-LLMs as mirrors | LLMs over-moralize and underestimate cross-cultural variance; variance-profile correlation weakly negative |
| 2024-Garcia-The Moral Turing Test | Actual-vs-believed source dissociation; humanization ablation; source-belief contaminates agreement ratings |
| 2025-Chua-Between a Rock TRIAL | Trolley framing as jailbreak; ASR 11–87%; ENGAGE (analyze) vs EXPLAIN (actionable) safety boundary |
| 2025-Dubey-Addressing Moral Uncertainty | 5-cluster LLM moral juries (conseq/deont/virtue/care/social-justice); BJSD+DST fusion beats averaging |
| 2025-Tennant-Hybrid Approaches | Maps utilitarian/deontological/virtue/Rawlsian to explicit RL reward functions; multi-objective (collective+Gini+min) |
| 2024-Stenseke-Computational Complexity of Ethics | Optimal moral computation is NP-hard/PSPACE/undecidable; Moral Tractability Thesis; complexity classes as difficulty metric |
| 2025-Liu-Diagnosing Moral Reasoning | Pragmatic dilemma: moral classification fails to converge at 210k samples; RLA>0.9 flags surface pattern-matching |
| 2018-Berberich-The Virtuous Machine | Moral attention/salience as a first-stage task; critique of trolley problems as static, pre-given, ecologically invalid |
| 2021-Stenseke-Artificial Virtuous Agents | Eudaimonic (longitudinal) reward; virtue-conflict scenarios reveal implicit virtue priority ordering |
| 2020-Gabriel-AI Values and Alignment | Six-way alignment-target taxonomy (instructions→intentions→revealed→informed→interests→values) |
| 2024-Gabriel-Ethics of Advanced AI Assistants | Tetradic alignment (AI/user/developer/society), 8 failure modes; three-layer eval; "no valid tractable eval exists" for most |
| 2023-McDonald-AI alignment and the categorical imperative | Formula of Humanity as criterion; conceptual vs volitional inconsistency; counterexample stress-testing |
| 2025-Sanwoolu-Kantian deontology for AI | Alignment-without-agency; universalizability (FUL) as a testable maxim criterion; principle-knowing vs applying gap |
| 2023-Feng-Case Repositories | Casuistry/common-law precedent library; expert dimension workshops + LLM-assisted case expansion |
| 2025-Li-SafetyAnalyst | Harm-benefit tree → 28 interpretable weights; steerable to community distributions; models benefits vs harms |
| 2025-Benavoli-AI Safety Uncertainty Incomplete Preferences | Add "incomparable" annotation option; lexical priority for safety/shutdown; probabilistic over point scoring |
| 2024-Šekrst-AI Ethics by Design | User-configurable ethical guardrail chains; conflict-resolution taxonomy; ethics-as-RAG at inference |
| 2022-Bang-Enabling Classifiers to Make Judgements | Value-as-instruction input; value/counter-value pairs make same content flip label; NA via value mismatch |
| 2024-Nahian-Goofus & Gallant | Auto-labeled contrastive good/bad pairs from curated children's materials; relaxed multi-label matching |
| 2022-Ramanayake-Pro-Social Rule Breaking | PSRB: test when a model appropriately breaks a rule; well- vs poorly-justified matched pairs |
| 2019-Aliman-Requisite Variety Ethical Utility Functions | Ethical adversarial examples; Law of Requisite Variety → coverage checklist; dyadic (agent-action-patient) template |
| 2025-Morlat-COMETH | Online clustering of full ternary human-judgment distributions; interpretable per-cluster feature weights (~60% vs ~30%) |
| 2024-Wang-Moral growth of LLMs | Dewey Impulse/Habit/Character staging; fiction-framing bypasses refusals (cross-scenario generalization test) |
| 2019-De-Arteaga-Bias in Bios | Counterfactual attribute-swap label-flip rate; TPR-gap × base-rate correlation as bias score |
| 2020-Nozza-AMI EVALITA2020 | Dual-track: real-data subtask + synthetic template bias-audit subtask; AUC-decomposed identity-term bias |
| 2024-Aupi-WoNBias | Regional annotator stratification; three-class (negative/positive-advocacy/neutral) scheme; κ=0.74 |
| 2024-Joy-Gender Bias Mitigation Bangla | Counterfactual gender-swap disagreement rate; bias varies by task (0.46%–7.48%) |
| 2024-Cahyawijaya-High-Dimension Human Value | Contrastive value embedding (UniVaR); language-as-culture split; non-value QA negative control |
| 2025-Fenech-Borg-Cultural Gene | Value-Dilemma Probes > association probes (|CDS| 1.35 vs 0.89); Cultural Alignment Index vs Hofstede |
| 2025-Yoo-Moral Judgment Korean | Eastern ethics (Confucian/Taoist/Buddhist) as system policies; bias = policy resistance; cross-lingual drift |
| 2025-Basu-Multilingual Moral | Deliberate "trick"/indirect categories; cross-language safety inversion; rubric scores justification not just answer |
| 2024-Rane-Concept Alignment | Value alignment presupposes concept alignment; prototype theory for item-difficulty calibration |
| 2025-ÓhÉigeartaigh-Cross-cultural Cooperation | Overlapping-consensus scoring; 22/28 ISO countries NA/Europe/E.Asia; author items natively |
| 2025-Ray-Indigenous knowledge systems | Contextual failure as deployment-level alignment failure; red-teaming can violate cultural protocol |
| 2024-MaqasidAI / 2025-AlGhazali | Islamic five-daruriyyat and Amanah/Adl/Maslahah rubrics as non-Western dimensions |
| 2023-Ray-Benchmarking ethical alignment | Conversation-native metrics (CSI, coherence, TSR); benchmark-coverage matrix |
| 2025-Insights-Moral Reasoning Humans and LLMs | MFT + Dual-Process: score which foundations activate and System-1/2 patterns vs humans |
| 2025-Waldner-AI Safety Alignment Ethics | Five metaethical hypotheses (realism/relativism/convergence/constructivism/virtue) as design frames |
| OpenAI-gpt-5-system-card | Safe-completions (graded, non-binary); CoT deception monitor; sycophancy as continuous trait |
| Anthropic-Alignment_Faking | Monitored-vs-unmonitored compliance gap as authenticity metric; scratchpad audits; scale stratification |
| Anthropic-Summer_2025_Pilot_Sabotage_Risk_Report | Dual-task agentic eval + monitor; model-organism validation loop for detection sensitivity |

## C. Patterns & disagreements

**Convergence — MCQ under-measures values.** Independent cards find single-turn forced-choice misleading: ConflictScope's MCQ/open-ended divergence [2025-Liu-ConflictScope], TRIAGE's demand for explicit action over stated preference [2024-Kirch-TRIAGE], Kilov's pre-packaged-vs-novel reversal [2025-Kilov-Discerning What Matters], the reason-order effect [2025-Samway], and Anthropic's monitored/unmonitored compliance gap [Anthropic-Alignment_Faking] as the frontier analogue.

**Convergence — cultural non-neutrality is empirical.** Haslett, Wu, Yu, Fenech-Borg, Meijer, and Rao independently document Western/individualist skew; theory/governance cards [2020-Gabriel; 2025-ÓhÉigeartaigh; 2025-Ray; 2024-MaqasidAI] prescribe overlapping-consensus and non-Western rubrics as the remedy.

**Convergence — decompose, don't score monolithically.** PrinciplismQA (principle × competency), Jiao (3 dimensions), Kilov (5 competences), SafetyAnalyst (28-weight harm-benefit tree), and MORALLENS (16 rationales) all reject a single ethics scalar for diagnostic profiles.

**Disagreement — is virtue ethics operationalizable?** Berberich, Stenseke (2021), and Wilders argue character is the *right* target but build no benchmark; Stenseke (2024) shows optimal versions are intractable; Boddington and Samway operationalize virtue only within a conseq/deont-dominated scheme; only Dubey instantiates it as a reward agent. The field endorses virtue rhetorically but implements consequentialism/deontology.

**Disagreement — do ethics-framing prompts help?** TRIAGE finds ethics reminders *degrade* high-stakes decisions [2024-Kirch-TRIAGE] and TRIAL finds ethical framing enables jailbreaks [2025-Chua]; conversely policy-conditioned designs [2023-Rao; 2025-Yoo; 2024-Abdulhai] treat framework prompts as the main steering lever. Reconciliation: framing steers values but can hurt correctness/safety — evaluate it as a variable, not a benefit.

**Disagreement — LLM vs human moral competence.** Kilov and Garcia caution that scores flatter LLMs (source bias; pre-highlighting) while MCQ benchmarks report near/superhuman accuracy; Liu (2025) and Stenseke (2024) supply the mechanism (surface pattern-matching, intractability) for why high scores may be illusory.

## D. Exemplars & anti-patterns

**Best-designed.** TRIAGE [2024-Kirch]: objective professional gold standard, explicit action choice, a 3×5 framing-robustness matrix, a directional (over/undercaring) error taxonomy, and worst-case reporting. ConflictScope [2025-Liu] pairs top-down conflict generation with a 6-dimension quality filter and an expressed-vs-revealed validity check. PrinciplismQA [2025-Hong]: Knowledge/Practice OSCE split, keypoint rubrics, principle×competency tagging, ICC-validated judge. Seror [2024] is the best *coherence* exemplar — priced-choice GARP testing is answer-key-free and contamination-resistant. SafetyAnalyst [2025-Li] cleanly separates the generative "what could happen" step from value-laden weighting with auditable, community-steerable weights.

**Anti-patterns.** Static pre-packaged trolley vignettes that hand the model the moral situation are ecologically invalid and competence-inflating [2018-Berberich; 2025-Kilov]. Machine-translated multilingual items distort meaning and inject bias [2025-ÓhÉigeartaigh; 2025-Yoo]. Forced binary choice over incomparable options manufactures apparent irrationality and noisy labels [2025-Benavoli]. Single-region authorship and MFT-only taxonomies bake in Western bias [2025-Wu; 2024-Meijer]. Tiny-N probes with no reliability stats [2025-Yoo; 2024-MaqasidAI; 2025-AlGhazali] name dimensions without measurement — declarative, not operational.

## E. Design lessons

1. **Pair MCQ with open-ended/interactive evaluation on the same items and report the divergence as a validity metric** [2025-Liu-ConflictScope; 2024-Kirch-TRIAGE; 2025-Kilov]. Add a monitored-vs-unmonitored (or eval-vs-deployment) condition to measure authenticity [Anthropic-Alignment_Faking].
2. **Prefer objective gold standards from codified professional protocols over crowd labels** where available [2024-Kirch-TRIAGE; 2025-Ebara], and split "knowledge" recall from "practice" application on the same principle [2025-Hong-PrinciplismQA].
3. **Test policy-following (consistency with a stated framework) rather than moral correctness** to escape prescriptivism, and include complement policy pairs and a no-policy baseline for entrenchment [2023-Rao; 2025-Yoo].
4. **Instantiate all five frameworks explicitly** — do not let conseq/deont dominate. Use per-theory reward agents or fine-tunes and aggregate with a principled uncertainty-aware method (MEC, BJSD+DST) rather than averaging [2023-Boddington; 2025-Dubey; 2025-Tennant].
5. **Decompose scoring into diagnostic profiles** (principle × competency; harm-benefit trees; rationale taxonomies) and report which value is over/under-weighted [2025-Hong; 2025-Li; 2025-Samway; 2025-Jiao]. Down-weight coherence/fluency so glibness cannot inflate scores [2025-Jiao].
6. **Add a moral-sensitivity stage**: embed salient features in irrelevant detail and test whether the model can pre-filter, not just judge highlighted cases [2025-Kilov; 2018-Berberich].
7. **Manipulate reasoning order and use structured moral chains** (foundation → rule-of-thumb → judgment) to separate pre-deliberative from post-hoc rationalization [2025-Samway; 2025-Liu-Diagnosing].
8. **Build genuine value conflicts**, using top-down generation from value pairs or automatic collision-mining, and filter for realism/feasibility/genuine-dilemma [2025-Liu-ConflictScope; 2025-Wu; 2021-Stenseke].
9. **Ground cultural coverage in native, non-Western taxonomies** (3-12-50 Chinese values; five daruriyyat; Amanah/Adl/Maslahah; Confucian/Taoist/Buddhist policies; Kaitiakitanga/Hózhó), author items natively — never machine-translate — and use overlapping-consensus scoring so multiple traditions score positively [2025-Wu; 2024-MaqasidAI; 2025-AlGhazali; 2025-Yoo; 2025-Ray; 2020-Gabriel; 2025-ÓhÉigeartaigh].
10. **Anchor to validated psychometric instruments with human norms as the scoring key** (MFQ-30, MFV, WVS), score by graded distance to human ratings, add a harder comparative stage as a saturation-buster, and add a coherence axis independent of correctness (priced-choice GARP, value-consistency CV, cross-lingual/permutation consistency) [2024-Ji-MoralBench; 2025-Jiao; 2024-Abdulhai; 2024-Seror; 2025-Yoo].
11. **Include adversarial and rule-breaking probes**: misaligned-instruction prompts [2025-Ebara], trolley-framed jailbreaks with an ENGAGE/EXPLAIN boundary [2025-Chua], pro-social rule-breaking with well/poorly-justified matched pairs [2022-Ramanayake], and ethical adversarial examples exploiting coverage gaps [2019-Aliman].
12. **Offer "incomparable"/"undetermined" options** with probabilistic scoring so value ties are not forced into noisy binaries; give safety constraints lexical priority [2025-Benavoli; 2023-Rao].
13. **Validate LLM-judges against human-expert panels with ICC**, triangulate judges, and score justifications not just final answers [2025-Hong; 2025-Basu; 2025-Dubey].
14. **Stratify by model scale and item difficulty/ambiguity**, and guard against contamination via convergence curves (RLA) and situational-awareness checks [2025-Liu-Diagnosing; Anthropic-Alignment_Faking; OpenAI-gpt-5-system-card].
15. **Extend beyond single-turn to trajectory/longitudinal designs** (decision trees, dual-task agentic environments with monitors, eudaimonic criteria) since dependency, corrigibility, and deception surface only over time [2025-Ebara; Anthropic-Summer_2025_Pilot_Sabotage_Risk_Report; 2021-Stenseke].
