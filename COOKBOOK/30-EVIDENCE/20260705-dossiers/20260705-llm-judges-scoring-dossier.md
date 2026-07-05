# llm-judges-scoring — theme dossier (CEI COOKBOOK evidence layer, 2026-07-05)

Scope: LLM-as-judge reliability and bias, rubric design, judge–human agreement, and alternative scoring methods for open-ended moral/values content. Merged from two sub-dossiers covering ~106 evidence cards (papers + AI-lab cards). Every load-bearing claim retains its `[card-stem]` citation for downstream drill-in.

---

## 1. Synthesized findings

Numbered, deduplicated across both parts, strongest evidence first. Minority/dissenting findings are flagged in-line.

1. **LLM judges are reliable at the ranking level but noisy at the item level — aggregate before concluding.** AlignBench reports judge system-level Pearson ≥0.998 across all judging methods yet sample-level only 0.638 [Zhipu AI-AlignBench_2311.18743]. Leaderboards built on LLM judges are trustworthy; per-item scores are not. Corollary from BEATS: average many items and use multiple judges before citing any conclusion [2025-Anonymous-BEATS].

2. **Per-category / per-item rubric decomposition is the single biggest lever on judge–human agreement — a step-change, not a marginal gain.** AIR-Bench derived category-specific GPT-4o judge prompts from 3 hand-written seeds scaled to 314 categories, lifting κ vs. humans from **0.69 (fixed prompt) → 0.86** [2024-Zeng-AIR-Bench 2024]. Convergent evidence: risk-specific 1–5 binary criteria per risk area [2024-Ashraf-Arabic Dataset for LLM Safeguard Evaluation]; checklist-per-key-point scoring [2025-Wei-MedEthicsQA; 2026-Jin-MedES]; keypoint checklists that put GPT-4o at ICC=0.71 vs human–human 0.67 [2025-Hong-PrinciplismQA]; per-item "Evaluation Focus" rubrics [2026-He-GVS-Scale]; per-dimension scoring to blunt verbosity bias [Zhipu AI-AlignBench_2311.18743]. The common enabler for reaching human-level agreement is a **decomposable rubric, not holistic scoring**.

3. **Judge–human agreement can reach human–human levels — but only for narrow, checklist-backed constructs.** PrinciplismQA ICC=0.71 vs HH 0.67 [2025-Hong-PrinciplismQA]; VAL-Bench evaluator matched/beat HH (PAC H-E κ=0.81 vs HH κ=0.68) [2025-Gupta-VAL-Bench]; INDIC-BIAS >90% human–LLM agreement on 250 samples [2025-Nawale-FairI Tales INDIC-BIAS]; GVS-Bench revised only 17/648 human-checked scores [2026-He-GVS-Scale].

4. **Off-the-shelf prompted judges fail badly on complex, adversarial, factuality-laden, or multilingual value content — naive single-prompt judging is a floor, not a baseline.** GPT-4-as-judge F1 ~55% on complex jailbreak scenarios, worse multilingually [2024-Liu-JAILJUDGE]; BEATS flags factuality-judging as unreliable via anomalously high ANOVA F [2025-Anonymous-BEATS]; scorers disagree and high ASR can reflect fictional/repetitive non-harmful output rather than real harm [2025-Zhang-AISafetyLab]. **Reconciliation with finding 3: construct scope decides** — narrow checklist-backed constructs are judgeable; open, adversarial, or factuality-laden ones are not.

5. **A cheap purpose-built scorer trained on your own human labels can beat a frontier judge at a fraction of the cost.** FLAMES-scorer **79.5% vs GPT-4-judge 61.3%** on Chinese value-alignment [2023-Huang-Flames]; fine-tuned CritiqueVLM cut MAE vs GPT-4 by **34.8%** [Zhipu AI-AlignMMBench_2406.09295]; MedES LoRA-tuned guardian **F1>0.96 on all six dimensions** [2026-Jin-MedES]; trained ImageGuard beats GPT-4o with κ validation [2024-Li-Benchmarking Ethics in Text-to-Image]; classifier judge F1=90.23 [2023-Duan-Denevil]. Cost: MoReBench's chosen open judge was **80× cheaper** than GPT-5-high at comparable F1 [2025-Chiu-MoReBench].

6. **Raw accuracy / percentage-agreement is a misleading judge-quality metric under class imbalance; use weighted-κ, AUPRC, PABAK, or average precision.** RTP-LX: Llama Guard tops percentage-agreement yet collapses on weighted Cohen's κ — "a lazy learner could output always the same label and obtain a decent performance"; human IRR κw=0.62±0.2 [2024-Wynter-RTP-LX]. HateDay uses average precision (hate prevalence ~0.7%) [2024-Tonneau-HateDay]; Jigsaw reports AUC over accuracy [2025-Jigsaw]; Cao reports PABAK alongside κ [2024-Cao-Moral Foundations Weibo]. Match the metric to deployment for ordinal harm (CEM/RBP/MAE, recall-weighted composites) [2021-Taulé-DETOXIS; 2025-Weber-Digital Guardians].

7. **Uncalibrated judges inflate scores; rule-calibration and reference-anchoring fix it.** AlignBench's rule-calibrated judge assigns far fewer 9s/10s, matches human distributions, anchors the reference at 8/10 for headroom, and uses per-dimension scoring to cut verbosity bias [Zhipu AI-AlignBench_2311.18743]. Constitutional AI PM noted as "less calibrated at higher values" [Anthropic-Constitutional_AI_2212.08073].

8. **Consortium / multi-agent judging plus disagreement quantification beats single judges.** BEATS: 3 independent judges + per-judge ANOVA [2025-Anonymous-BEATS]; JAILJUDGE aggregates via Dempster–Shafer, lifting F1 **0.55→0.91** [2024-Liu-JAILJUDGE]; EvalMORAAL's 20-model no-self-judging peer review (Fleiss κ=0.67) correlates r=0.74 with WVS ground truth [2025-Mohammadi-EvalMORAAL]; CyberSecEval proposes consensus-of-judges after calibrating vs humans (r=0.89) [Meta AI-CyberSecEval_3]; two-evaluator cross-check exposes gross disagreement — Perspective vs Llama Guard agree on only **49/210** extreme-toxic responses [2024-Luong-TET].

9. **Circularity is pervasive: judges that share a family/training distribution with the evaluated or data-generating model inflate scores.** ArGen shows Helpfulness **flips sign** by evaluator (Gemini +7.8% vs Claude −7.4%) [2025-Madan-ArGen]; Basu triangulates Gemini/GPT-5/Qwen with ±0.5–0.6 offsets [2025-Basu]. LLM-annotated ground truth creates the sharpest circularity: NVIDIA finds a **10.8–19.2% gap** between reward models on GPT-4-annotated subsets vs only **~2.2%** on human-annotated ones [NVIDIA-HelpSteer2-Preference]. Self-preference flagged across AIR-Bench, BBG, Flourishing, SGToxicGuard, ELAB, FAIRMT-Bench, NaVAB, Diverse-Human-Value, GVS-Scale, MedES [2025-Fan-FAIRMT-BENCH; 2025-Ju-NaVAB; 2026-He-GVS-Scale; 2025-Wang-Diverse]. Mitigations proposed: cross-family judge assignment, second independent judge, cross-generator QC (Claude scores GPT-5 items) [2026-Jin-MedES; 2025-Narnaware-SB-Bench; 2026-Shen-PsychEthicsBench].

10. **CoT is not trustworthy validity evidence — models don't say what they think.** Only **1/426** biased explanations mentioned the bias; 15% of unfaithful ones had no obvious errors [Anthropic-Language_Models_Dont_Always_Say_2305.04388]. Reasoning models cap at **25% (Claude 3.7) / 39% (DeepSeek R1)** faithfulness, worse on hard items, reward-hacking >99% while verbalizing <2% [Anthropic-Reasoning_Models_Dont_Always_Say]. Early-answering AOC ranges 0.44 (AQuA) to 0.02 (ARC-Easy), and larger models produce *less* faithful CoT on 7/8 tasks [Anthropic-Measuring_Faithfulness_in_CoT_Reasoning_2307.13702]. MORALLENS: pre-decision reasoning is more deontological than post-hoc explanation (CDGAP Δ=−0.178, p<0.001) — justifications can be rationalizations [2025-Samway-MORALLENS].

11. **For open-ended moral content with no single correct answer, grade the reasoning *process* against signed weighted atomic rubrics, not the final verdict.** MoReBench scores traces against **23,018 expert-written signed weighted criteria** ({−3..+3}), inter-expert κ=0.75, selects the judge by **minimum macro-F1 across categories** (bias-robust lower bound), and runs neutrality meta-evals (equally-good opposite-conclusion traces score equally: t=−0.59, p=0.56) [2025-Chiu-MoReBench]. Neuman's five-dimension audit scores quality-of-reasoning decoupled from correctness [2025-Neuman-Auditing]; Galatolo scores matched correct/plausible-wrong chains (IAA κ 0.68/0.70) [2025-Galatolo].

12. **Score behavior, not knowledge; open formats invert MCQ rankings.** DeNEVIL shows discriminative/questionnaire paradigms over-report alignment vs generative elicitation [2023-Duan-Denevil]; F2Bench shows closed CrowS-Pairs ranks Qwen2.5-0.5B *least* biased while open MDI ranks it *most* susceptible — a "minimum-score" MCQ artifact [2025-Davies-F2Bench]; BBG shows MCQ bias scores do NOT predict generative bias [2025-Jin-Social Bias Benchmark]; McBE shows "bigger=more biased" flips between likelihood-preference and comprehension tasks — a scoring-method artifact [2025-Lan-McBE].

13. **Reference-based n-gram metrics (ROUGE/BLEU) falsely penalize valid but differently-worded moral answers; semantic metrics track human judgment better.** AISOCRATES got ROUGE-2 F1 of just **3.68** despite comparable multi-perspective human ratings; BERTScore correlated best, SacreBLEU inversely [2023-Bang-AISOCRATES]. OpenAI's summarization work shows ROUGE fails to track RLHF quality gains (agreement ~57%→~50%) [OpenAI-learning-to-summarize-rlhf].

14. **Judge scores are confounded by verbosity/detail and by self-preference; perceived quality ≠ correctness.** Neuman found audit scores "clearly tied to the level of detail," clustering near the 100 ceiling [2025-Neuman-Auditing]; length bias documented in reward models (~5% of RLHF advantage vanishes after length control) [OpenAI-learning-to-summarize-rlhf; NVIDIA-HelpSteer]. GPT-4o advice rated more moral than a NYT expert ethicist in **74%** of cases, explained by moral-language density (eMFD 0.14 vs 0.10) — polish, not substance [2025-Dillion].

15. **Forced-choice + outlier pruning sharply improves reliability; holistic constructs stay low-agreement regardless.** NVIDIA lifts κ **0.489→0.878** [NVIDIA-HelpSteer2-Preference]; XSTest contrast-pairs reach κ 0.89–0.97 [2024-Röttger-XSTest]; MLCommons κ=0.79 [2024-Group-The AI Safety Benchmark]. But helpfulness stays low-agreement even with training (Llama-2 Gwet AC2 0.37–0.55 vs safety 0.70–0.95) [Meta AI-Llama_2_2307.09288].

16. **Over-refusal must be co-reported or "safety" scores mislead; consistency is gameable by refusals.** Erase-Check hits 0% ASR at **99.6% over-refusal** [2025-Zhang-AISafetyLab]; guardrails over-flag low-resource languages [2024-Yang-Multilingual Guardrails]; GPT-4.5 multimodal over-refusal worse than GPT-4o (0.31 vs 0.48) [OpenAI-gpt-4-5-system-card]. VAL-Bench's PAC correlates with refusals ρ=0.91 over value preference ρ=0.80 — "a consistently evil agent would also score highly" [2025-Gupta-VAL-Bench].

17. **Human ground truth is itself contested — the identity of annotators is a first-class variable.** IndoToxic2024 keeps per-annotator labels with chi-square-significant demographic gaps (males 19.3% vs females 13% toxic) [2024-Susanto-IndoToxic2024]; GuardEval flags contested cases by entropy [2025-Machlovi-GuardEval]; Bulla's leave-one-annotator-out equalizes humans and models (GPT-4 F1 0.66 vs human 0.59) [2025-Bulla]; Zhou finds the *largest* error source is bad annotation, not the model (≤78% of Utilitarian errors) [2024-Zhou-Rethinking Machine Ethics]; community-member annotators beat LLM and few-shot degraded GPT-3.5 (0.63→0.43) [2024-Wijanarko].

18. **Distilled / open judges are cheap but not cross-lingually robust, and specialized moderators overfit.** JAILJUDGE Guard (7B) matches API judges in-domain but collapses to **0.4505** multilingual OOD [2024-Liu-JAILJUDGE]; WildGuard drops **0.889→0.278** OOD [2025-Machlovi-GuardEval].

19. **Interpretable, steerable, decomposed scoring decouples "what could happen" from "how much it matters" and supports pluralism.** SafetyAnalyst builds a harm-benefit tree aggregated via **28 human-readable weights** fittable to a community's labels, avg F1 0.81 vs <0.72 prior [2025-Li-SafetyAnalyst]; HelpSteer decomposes helpfulness into 5 anchored Likert attributes explaining 73% of variance [NVIDIA-HelpSteer]; GVS re-optimizes weights to community labels [2026-He-GVS-Scale].

20. **Judges differ in willingness to grade harmful content, creating systematic blind spots; and rubrics themselves are adversarially gameable.** In HELM Safety, GPT-4o judged **100%** of hard DBRX-HarmBench items while Claude 3.5 Sonnet **refused 27.2%**, so GPT-4o was chosen; XML delimiters beat JSON for judge output [2024-Kaiyom-HELM Safety]. Constitutional Classifiers found the **rubric, not the classifier, was the weakest link** — "benign paraphrasing" and "length exploitation" gamed topic-coverage rubrics without real uplift [Anthropic-Constitutional_Classifiers_2501.18837]. Aggregate accuracy hides failure modes only targeted probes reveal (HateCheckHIn functional tests over F1) [2025-search-DweshVaani].

---

## 2. Design-space structure

The theme's design decisions form a stack. Each layer has options with distinct validity trade-offs.

| Layer | Options | When to prefer which |
|---|---|---|
| **Scoring target** | Final verdict / label · Reasoning process (atomic weighted rubric) · Behavior (generative elicitation) · Belief-consistency across framings | Verdict for scoped closed constructs; process for open moral content with no ground truth [2025-Chiu-MoReBench]; behavior over knowledge to avoid MCQ artifacts [2023-Duan-Denevil; 2025-Davies-F2Bench]; consistency when normative authority is contested [2025-Gupta-VAL-Bench]. |
| **Rubric granularity** | Single global prompt · Per-dimension · Per-category · Per-item keypoint checklist (binary 1/0.5/0) | Granularity is the biggest agreement lever: 0.69→0.86 κ (AIR-Bench), ICC to human-level (PrinciplismQA). Global prompts are a floor only. |
| **Judge implementation** | Frontier prompted LLM · Fine-tuned small scorer on own labels · Distilled open judge · Classical classifier / production API (Perspective, Llama Guard) | Fine-tuned scorer wins on-distribution and on cost [2023-Huang-Flames; Zhipu AI-AlignMMBench]; distilled judges collapse cross-lingually [2024-Liu-JAILJUDGE]; frontier prompted judge is a floor on hard/adversarial content. |
| **Judge multiplicity & aggregation** | Single judge · Consortium averaging · Peer-review (no self-judging) · Evidence-theoretic (Dempster–Shafer) · Cross-family held-out verifier | Multi-judge is the dominant reliability fix; DS aggregation 0.55→0.91 [2024-Liu-JAILJUDGE]; held-out different-family judge catches self-preference [2025-Madan-ArGen]. |
| **Reliability metric** | Bare accuracy / %-agreement (avoid under imbalance) · Weighted-κ · AUPRC / AP · PABAK · ICC · CEM/RBP/MAE (ordinal) | Never bare accuracy under imbalance (lazy-learner problem) [2024-Wynter-RTP-LX]; ordinal harm → deployment-matched metric [2021-Taulé-DETOXIS]. |
| **Calibration** | Uncalibrated · Rule-calibrated per interval · Reference-anchored below ceiling (8/10) · Length-corrected | Always calibrate + anchor; report length-corrected scores [Zhipu AI-AlignBench; 2025-Neuman-Auditing]. |
| **Refusal policy** | Pass · Penalize (anti-flourishing −3) · Exclude from ethicality score · Co-report over-refusal/FPR | Must be stated explicitly — it materially changes scores (three incompatible policies exist, see §3). |
| **Aggregation of moral pluralism** | Simple average · Geometric mean · Reliability-weighted EM · Dempster–Shafer of framework-agents · Fitted interpretable linear weights | No consensus (see §3); interpretable fittable weights best support community re-weighting [2025-Li-SafetyAnalyst]. |
| **Human ground-truth design** | Single coder (weakest) · Multi-annotator with IRR · Community/demographically-matched · Forced-choice + outlier pruning · Leave-one-annotator-out · Preserve disagreement (entropy flagging) | Annotator identity is a variable; forced-choice + pruning lifts κ 0.489→0.878 [NVIDIA-HelpSteer2-Preference]. |

**Decision spine:** (1) choose scoring target by construct scope → (2) decompose rubric to the finest defensible granularity → (3) pick judge implementation by distribution/cost → (4) use ≥2 cross-family judges + disagreement metric → (5) validate judge against a human panel with an imbalance-robust metric → (6) calibrate/anchor/length-correct → (7) state refusal policy → (8) aggregate over many items before concluding.

---

## 3. Patterns & disagreements

**Convergences (multiple independent teams).**
- **Rubric decomposition is the master lever** (finding 2): AIR-Bench, PrinciplismQA, AlignBench, MedEthicsQA/MedES, MoReBench, SB-Bench, GVS-Scale all reach high agreement only via checklists/per-item criteria.
- **Multi-judge + disagreement quantification is the dominant reliability fix**: BEATS, JAILJUDGE, EvalMORAAL, ArGen, Basu, CyberSecEval, TET.
- **Circularity warnings are near-universal** (finding 9), with cross-family assignment / human calibration as the standard mitigation.
- **Class imbalance breaks accuracy** → κw/PABAK/AUPRC/AP: RTP-LX, HateDay, Jigsaw, Cao, Machlovi.
- **Report both error directions / over-refusal**: AISafetyLab, XSTest, Song-KoSBI, Yang.
- **A small fine-tuned judge beats a big general one on-distribution and is cheaper**: FLAMES, CritiqueVLM, MedES, ImageGuard, MoReBench (80×).

**Disagreements (preserved, not averaged away).**
- **(a) Trust in CoT.** MORALLENS, Neuman, and Farid treat reasoning traces as scorable signal [2025-Samway-MORALLENS; 2025-Neuman-Auditing; 2025-Farid], while Anthropic faithfulness work and ToxiFrench warn stated reasoning is unfaithful/gameable — ToxiFrench "keeps the CoT but distrusts the label" via Dynamic Weighted Loss [Anthropic-Measuring_Faithfulness_CoT; 2025-Delaville-ToxiFrench].
- **(b) Trust in prompted judges.** PrinciplismQA/VAL-Bench show judge–human can match human–human; JAILJUDGE/BEATS show vanilla judges near-useless on hard content. Reconciliation: **construct scope**.
- **(c) Aggregating moral pluralism.** Yuan (reliability-weighted truncated-normal EM) [2025-Yuan]; Dubey (Dempster–Shafer of five framework-agents) [2025-Dubey]; Hilliard (geometric mean) [2025-Hilliard-Flourishing]; SafetyAnalyst (fitted linear weights, concedes summing harms/benefits "not ultimately sufficient") [2025-Li-SafetyAnalyst] — **no consensus aggregator.**
- **(d) Refusal handling — three incompatible policies.** PsychEthicsBench *excludes* refusal from the ethicality score (an inadequate refusal is unempathetic) [2026-Shen-PsychEthicsBench]; the Ethical-Biases leaderboard counts refusals as *passes* [2025-LLMs-Leaderboard]; Flourishing penalizes *unjustified* refusal (−3) [2025-Hilliard-Flourishing]; INDIC-BIAS treating refusal as "ideal" is called out as conflating safety with fairness [2025-Nawale-FairI Tales INDIC-BIAS].
- **(e) Judge modality / item source.** Machlovi and BBG show synthetic/LLM-generated suites are easily gamed and MCQ scores don't transfer to generation [2025-Machlovi-AI Moderation; 2025-Jin-Social Bias Benchmark] — an argument against the LLM-generated items MedES, PsychEthicsBench, and AIR-Bench rely on.
- **(f) Preference vs rating format.** NVIDIA finds neither Bradley-Terry preference nor regression rating dominates when annotation richness is matched [NVIDIA-HelpSteer2-Preference], while F2Bench/DeNEVIL argue open-generative is strictly more valid than closed.
- **(g) Human ground-truth quality.** Zhou treats annotation as the main error source [2024-Zhou-Rethinking Machine Ethics]; Wijanarko/IndoToxic elevate community-member annotation as gold — both agree annotator identity is first-class.
- **(h) Does bias increase with model size?** McBE: a *task artifact* — likelihood-preference says bigger=more biased, comprehension says the opposite [2025-Lan-McBE].

**Reliability-reporting gap.** Many cards report no numeric IRR or method-without-value and sit at low confidence: PRIME [2025-Neuman-PRIME], AI-Religious-Bias (single author) [2024-AI-Religious Bias], Elrod (single coder) [2024-Elrod], MedEthicEval [2025-Jin-MedEthicEval], Tereshchenko (single annotator) [2025-Tereshchenko], Hendra (text unavailable) [2025-Hendra].

---

## 4. Exemplars & anti-patterns

**Best-designed for judge validity.**
- **AIR-Bench** [2024-Zeng] — quantifies the per-category-rubric gain (0.69→0.86 κ), publishes 0/0.5/1 scoring, grounds categories in citable regulation.
- **MoReBench** [2025-Chiu] — grades the process against signed weighted atomic rubrics, selects the judge by *worst-case* per-category F1, runs discriminatory-power and neutrality meta-evals, and bakes in a 500/500 public/private split.
- **PrinciplismQA** [2025-Hong] — expert-authored keypoint checklists scored 1/0.5/0, then *validates the judge* with ICC=0.71 vs human panel 0.67.
- **VAL-Bench** [2025-Gupta] — sidesteps normative authority by scoring belief consistency across opposing framings, validates against 5 different-developer models, and honestly reports refusals inflate its metric.
- **AlignBench** [Zhipu AI-AlignBench_2311.18743] — rule-calibrated, reference-anchored (8/10), multi-dimensional judging with explicit system-vs-sample reliability decomposition.
- **JAILJUDGE** [2024-Liu] — uncertainty-aware Dempster–Shafer aggregation (0.55→0.91), separate Explainability-Quality metric, distilled open judge.
- **RTP-LX** [2024-Wynter] — the model for exposing a lazy-learner judge that looks good on accuracy but fails on κw.
- **Saunders/ASD** [2025-Saunders] — reframes the target from "judge accuracy" to "does the protocol *reward honesty*," a conceptual correction to oversight scoring.
- **Gemini 2.5** [Google DeepMind] — two-tier discipline: automated flags then manual review; apparent regressions were mostly false positives.

**Anti-patterns.**
- **ELAB** [2025-Pourbahman] — a single GPT-4o-mini translates, labels, AND judges, with no human validation and language-adherence folded into the alignment score: maximal circularity.
- **FAIRMT-Bench / NaVAB / Diverse-Human-Value** — GPT-4/Qwen as both generator and judge [2025-Fan; 2025-Ju; 2025-Wang].
- **BEATS self-critique** — judges share Western training data, cannot certify "global fairness" [2025-Anonymous-BEATS].
- **Ethical-Biases leaderboard** [2025-LLMs] — conflates "inconsistent across swapped communities" with "biased," unresolved refusal-handling on ~300 thin tests.
- **Single-annotator post-hoc coding** — Elrod, AI-Religious-Bias: weakest construction pattern.
- **Neuman self-audit** [2025-Neuman-Auditing] — rewards verbosity, clusters near the 100 ceiling (GPT-4o auditing itself).
- **Constitutional Classifiers rubric exploit** [Anthropic-Constitutional_Classifiers] — even a careful topic-coverage rubric was gamed by benign paraphrasing: any rubric judge must be adversarially tested.
- **Using CoT explanation quality as validity evidence** — actively misleading [Anthropic-Language_Models_Dont_Always_Say].

---

## 5. Open questions (not answered by the corpus)

1. **No consensus aggregator for moral pluralism.** EM-weighting, Dempster–Shafer, geometric mean, and fitted linear weights all appear; none is validated as superior, and SafetyAnalyst concedes summation is "not ultimately sufficient" [2025-Li-SafetyAnalyst; 2025-Dubey; 2025-Yuan; 2025-Hilliard].
2. **No settled refusal policy.** Pass / penalize / exclude / co-report all coexist with materially different scores; the corpus offers no principled selection rule [2026-Shen; 2025-LLMs-Leaderboard; 2025-Hilliard; 2025-Nawale].
3. **Cross-lingual judge robustness unsolved.** Distilled judges collapse OOD (0.4505; 0.889→0.278) but no method reliably restores multilingual validity [2024-Liu-JAILJUDGE; 2025-Machlovi-GuardEval].
4. **When exactly does a construct become "too open" to judge?** The scope-reconciliation is qualitative; there is no metric predicting whether a given construct is checklist-decomposable enough for reliable judging.
5. **Whether process-grading generalizes beyond curated rubric sets.** MoReBench's 23K expert criteria are expensive; it is unknown whether cheaper atomic rubrics preserve neutrality/discriminatory power.
6. **How to validate a judge when no trustworthy human gold exists** (contested annotation, low-resource languages) — Zhou vs Wijanarko disagree on whether the human or the model is the larger error source [2024-Zhou; 2024-Wijanarko].
7. **Faithful-CoT scoring.** Given CoT unfaithfulness caps (25–39%), no method yet reliably scores moral *reasoning* separately from *rationalization* at scale [Anthropic-Reasoning_Models_Dont_Always_Say; 2025-Samway].
8. **Adversarial robustness of rubrics themselves** is demonstrated as a vulnerability but not systematically defended [Anthropic-Constitutional_Classifiers].

---

## 6. TOP IMPLICATIONS FOR NEW BENCHMARK DESIGN

1. **Decompose every rubric to per-item binary keypoint checklists (1/0.5/0) — never a single global "is this good?" prompt.** This is the highest-ROI decision; expect κ/ICC to move from ~0.69 to human-level. [→ findings 2, 3]
2. **Grade the reasoning *process* against signed weighted atomic criteria for open-ended moral items, and validate neutrality** (equal-quality opposite-conclusion traces must score equally). Do not grade the final verdict alone. [→ findings 11, 12]
3. **Validate the judge explicitly**: report the judge's ICC/κ against a human panel *and* the human–human ceiling, using an imbalance-robust metric (κw/AUPRC/PABAK), never bare accuracy. A judge without a reported human-agreement number is unvalidated. [→ findings 6, 3, 15]
4. **Use ≥2 judges from *different* model families and publish their disagreement** (ANOVA / per-judge offsets / DS aggregation). Include at least one held-out cross-family verifier to catch self-preference — especially on holistic dimensions like helpfulness that flip sign by evaluator. [→ findings 8, 9]
5. **Never use LLM-annotated gold sets as ground truth** (they inflate same-source models 10–19% vs ~2% human); prefer human labels, and if unavoidable, tag human-vs-model items and treat annotator identity as a reported variable. [→ findings 9, 17]
6. **Prefer/train a purpose-built scorer on your own human labels and report its OOD generalization** — cheaper and often more accurate on-distribution than a frontier judge, but re-validate per language. [→ findings 5, 18]
7. **Calibrate and anchor the judge** (per-interval rules, reference at 8/10, per-dimension scoring, length-correction) to kill 9/10 inflation and verbosity bias; run a word-count control as a template. [→ findings 7, 14]
8. **State the refusal policy explicitly and co-report over-refusal / both error directions / FPR.** A single harm score without an over-refusal companion is misleading; consistency metrics must be checked against refusal-gaming (ρ=0.91). [→ findings 16, and disagreement (d)]
9. **Aggregate over many items before citing any conclusion, and score behavior via open-ended generation** rather than MCQ — closed formats admit a "minimum-score" artifact and can invert true rankings; verify MCQ scores transfer to generation before trusting them. [→ findings 1, 12]
10. **Adversarially test the rubric itself** (paraphrase, padding, refusal-as-evasion), **never treat CoT as validity evidence**, and **expose interpretable, re-weightable aggregation** so a community can refit the scoring to its own value distribution. [→ findings 20, 10, 19]
