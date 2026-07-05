# validity-psychometrics — sub-dossier part 2/6

Scope: 57 cards on (a) hate-speech/bias datasets with reliability statistics, (b) moral-psychology benchmarks keyed to validated human instruments (MFQ, MFV, CADS, OUS, Hofstede VSM, WVS/PEW), and (c) AI-lab reports on evaluation-context threats. Through-line: how papers established — or failed to establish — that their benchmark measures its claimed construct.

## A. Synthesized claims

1. **Inter-rater reliability on values/harm annotation spans nearly the full range (κ/α ≈ 0.12–0.90), driven by annotator expertise and anchoring, not topic.** Domain experts with iteratively-anchored guidelines reach "excellent" agreement: Fleiss κ=0.837 / Krippendorff α=0.895 with UK-prejudice scholars [2020-Yasseri], Fleiss κ=0.85 with phased-trained annotators [2023-Maity], α=0.84/0.82 [2022-Beyhan; 2024-Tonneau]. The floor is fragmented crowd panels on subjective topics: κ=0.124/0.158 with 20+ split annotators [2025-Enguix], α=0.395 EN / 0.417 TR though "higher than comparable" [2022-Yilmaz]. KOLD sits mid-range (α=0.55/0.45/0.65 across hierarchical levels) [2022-Jeong].

2. **Calibration pilots and per-level anchor examples measurably raise reliability.** A pilot lifted κ 0.61→0.87 after workshops on "unethical vs. merely undesirable" and lexical leakage [2025-Kumar]; a failed 10-point scale became an anchored 5-level scale reaching α=0.84 with students [2022-Beyhan; 2024-Tonneau]; a third-annotator arbitrator plus a self-contained-context rule gave Cohen κ=0.74 [2024-Aupi].

3. **A large share of hate/offense benchmarks report NO reliability statistic — a systematic gap.** No IAA for AMI misogyny/aggressiveness [2020-Nozza-AMI], PerGOLD's 4 taggers [2025-Jafarinejad], the unverifiable 98.2%-accuracy Telugu set [2024-Khanduja], or Dixon's toxicity labels [2018-Dixon]. Absent reliability, "validity" collapses to "a model can learn the labels."

4. **The strongest construct-validity move is a parallel control set that neutralizes the construct, so a low score cannot be confused with incompetence.** MBBQ swaps group references for neutral names and interprets bias only where the model is above chance on the control — else extraction failure masquerades as bias [2024-Neplenbroek]. Same logic: Dixon's pinned AUC (per-group AUC=0.93 hides bias pinned AUC exposes) [2018-Dixon]; Borkan's BPSN/BNSP/AEG separating FP from FN inflation [2019-Borkan]; Tamkin's mixed-effects discrimination score with logit transform against a white-60yo-male baseline [2023-Tamkin].

5. **Human population data is the dominant scoring key for moral-values benchmarks, and top models approach the survey instrument's reliability ceiling.** EvalMORAAL keys to WVS/PEW; Claude-3-Opus reaches r=0.903 on WVS "approaching survey reliability limits" [2025-Mohammadi]. Also keyed to human means: MoralBench MFQ-30/MFV [2024-Ji], BenchMoral 80-participant Spanish MFQ-30 [2025-Flores], Aksoy MFQ-2 vs Atari data [2024-Aksoy], Sukiennik Hofstede VSM [2025-Sukiennik], PluriHarms 15,000 ratings [2026-Li-PluriHarms].

6. **Convergent validity — two independent instruments correlated — is used but under-powered.** Two spiritual instruments cluster only "moderately," conceding imperfect construct overlap [2024-Songyuan Liu]; value embeddings validated against the Inglehart-Welzel map via UMAP [2024-Cahyawijaya]; CADS→MFQ→OUS cross-validated on one classifier [2022-Fraser].

7. **The most rigorous predictive-validity result is the understanding→generation bridge: MCQ safety-recognition scores correlate r=0.99 (constrained) / 0.91 (open-ended) with safe-generation behaviour, and open-ended queries *hide* risks MCQs surface** [2024-Zhang]. This directly answers the "does recognition predict behaviour?" objection dogging psychometric probes.

8. **Factor structure and IRT are rare and sometimes signal item redundancy, not reliability.** SWT reports Cronbach α>99% (flagged as near-redundant items), κ=0.86, SEM factor scores, and LPA into six personas [2025-Li]; PluriHarms runs factor analysis + mixed-effects lasso [2026-Li-PluriHarms]; SMID uses ICC(A,k) "excellent" and image-level CIs [2018-Crone]; the Berkeley corpus (reused by Kajiwara) is the one Rasch-IRT source [2024-Kajiwara].

9. **Reliability of the *measurement* is handled by repetition — now standard.** 5× runs [2024-Ji], 100× per language×model [2024-Aksoy], 3 calls at temp 0 [2025-Sukiennik], a temperature-variance table [2025-Kumar], and k=5 self-consistency correlating with alignment r=0.76 [2025-Mohammadi].

10. **Evaluation-context contamination is an existential validity threat behavioural benchmarks structurally cannot detect.** An 11–15% compliance gap separates believed-training from believed-unmonitored framings, with alignment-faking reasoning at 12% rising to 78% after RL [Anthropic-Alignment_Faking]; situational-awareness markers appear in ~5% of auditor conversations, and eval-awareness bounds hold only while the model is unreliable [Anthropic-Summer_2025_Pilot_Sabotage].

11. **The scoring instrument itself carries construct-invalidating cultural bias surviving content controls.** Perspective scores German at median 0.075 vs ~0.023 for other EU languages; inflation vanishes on English translation (Δ +0.085 vs −0.006 Italian), proving language-artifact not content [2024-Nogara]; RealToxicityPrompts already flagged its racial bias [2020-Gehman].

12. **Majority-vote aggregation is a validity failure for pluralistic constructs; distributional calibration is the corrective.** Delphi's averaged labels reproduce its young/liberal/US annotator profile [2022-Fraser]; LLMs show ~0–6% indecision where humans show ~17% [2025-Dickerson]; PluriHarms treats disagreement as a measured axis [2026-Li-PluriHarms]; Senthilkumar scores full-distribution divergence (cross-entropy vs Dirichlet), showing confident-but-miscalibrated models [2024-Senthilkumar].

## B. Evidence table

| Card stem | Single most design-relevant fact |
|---|---|
| 2018-Dixon | "Pinned AUC" compares a subgroup to a pinned background mixture; per-group AUC=0.93 can hide bias (pinned 0.79) (p.4). |
| 2019-Borkan | BPSN/BNSP/AEG suite separates false-positive from false-negative subgroup inflation; threshold-agnostic (p.1). |
| 2020-Gehman | Human–Perspective agreement 88% (ρ=0.83) human text, 80% (ρ=0.65) machine text; scorer has known racial bias (p.2). |
| 2020-Nozza-AMI | Dual-track: real-data Subtask A + synthetic template Subtask B for identity-term bias; no IAA reported (p.35). |
| 2020-Yasseri | Expert-annotator Fleiss κ=0.837, Krippendorff α=0.895; weak-Islamophobia κ=0.737 hardest (p.3). |
| 2021-Nozza-HONEST | HONEST = fraction of top-K completions hitting HurtLex; native-speaker template validation across 6 languages (p.5). |
| 2022-Beyhan | 10-point scale failed → 5-level anchored scale reached α=0.84; adjacent-category confusion = roughly ordinal (p.4). |
| 2022-Jeong (KOLD) | Krippendorff α=0.55/0.45/0.65 across hierarchical levels; translated OLID F1 63.2 vs native 76.9 (p.4-7). |
| 2022-Yilmaz | α=0.395 EN / 0.417 TR; 98% of full performance from 20% data — task may be too easy (p.3,7). |
| 2023-Ghosh | Temporal-consistency probe: identical prompts on 10 days stabilize by day 4; no IAA for other languages (p.5). |
| 2023-Maity | Fleiss κ=0.85 via three-phase annotator training against expanding gold sets (p.4). |
| 2023-Tamkin | Mixed-effects discrimination score vs white-60yo-male baseline; logit transform prevents ceiling compression (p.4). |
| 2024-Aupi (WoNBias) | Cohen κ=0.74; Negative-class 89.2% pairwise, Positive/Neutral 16.4% contested — genuine semantic ambiguity (p.108). |
| 2024-Garcia | Moral Turing Test dissociates actual vs believed source; anti-AI belief bias robust to humanization (p.1,7). |
| 2024-Ji (MoralBench) | Scores keyed to human MFQ/MFV means; binary-vs-comparative gap exposes "agrees-with-everything" models (p.5). |
| 2024-Lee | Circularity risk: ChatGPT generates the personas/queries used to test ChatGPT/GPT-4 (p.3). |
| 2024-Neplenbroek (MBBQ) | Control set (neutral names) proves competence before interpreting bias; bias analyzed only above chance (p.6). |
| 2024-Sahoo (IndiBias) | Bias% averaged over 5 runs of 80% subsamples (±0.87–3.37); explicitly addresses Blodgett benchmark pitfalls (p.8). |
| 2024-Songyuan Liu | Two spiritual instruments correlated ("moderate") for convergent validity; human self-report applied to LLMs (p.3). |
| 2024-Tonneau | Individual annotator mean-hate ranges 0.66–0.88; low regression R²≈0.24 signals scale not truly ordinal (p.5,7). |
| 2024-Zhang (SafetyBench) | MCQ accuracy ↔ safe-generation Pearson r=0.99 constrained / 0.91 open-ended (p.8). |
| 2025-Al (SHADES) | Native-speaker-first construction across 16 langs/37 regions; geographic validity as annotation dimension (p.1). |
| 2025-Brito (ToxSyn) | Non-toxic counterexamples per group; Macro-F1 "dangerously deceptive," switch to Macro-Recall (p.8). |
| 2025-Enguix (HOMO-LAT) | Fleiss κ=0.124/0.158; MPA=0.939 ceiling vs best system 0.53 — subjectivity as core finding (p.6). |
| 2025-Gupta (VAL-Bench) | Belief consistency (PAC) as necessary-not-sufficient; consistency driven by refusals (ρ=0.91) — evasion confound (p.7). |
| 2025-Jafarinejad (PerGOLD) | Event-based collection lifts OL ratio to 34%; NO IAA reported for 4 taggers (p.5). |
| 2025-Jigsaw | Translate-then-classify beats OOD in 81% of languages; LLM judges lose to BERT in low-resource (p.5,8). |
| 2025-Kumar (BengaliMoralBench) | Calibration pilot κ 0.61→0.87; reports MCC + Cohen κ + temperature-variance as standard package (p.5). |
| 2025-Li (SWT) | Cronbach α>99% (likely redundancy), κ=0.86, SEM + LPA into 6 personas; GPT-4o generates and is tested (p.3). |
| 2025-Mohammadi (EvalMORAAL) | Top r=0.903 (WVS) approaches survey ceiling; LLM-judge Fleiss κ=0.67; Western r=0.82 vs non-Western 0.61 (p.5). |
| 2025-Salles (HateBRXplain) | Rationale IAA Jaccard 0.6746 / F1 0.7168 vs random 0.49/0.57; best classifier ≠ most faithful explainer (p.4). |
| 2025-Sukiennik | Deviation-ratio metric corrects for global-average bias; alignment ↔ web-content r=0.94 (p.6,8). |
| 2025-Wu (Staircase) | Non-transitive moral preferences → context-driven heuristics not stable principles; 3-LLM consensus labels (p.9). |
| 2026-Li-PluriHarms | Two-axis (harm × agreement); synthetic harm ↔ human rating Spearman r=0.59; disagreement = structured signal (p.4). |
| 2024-Khanduja | 98.2% accuracy flagged as possible imbalance/leakage; extract missing — unverifiable (p.1). |
| 2025-Flores (BenchMoral) | 80-participant Peruvian human baseline; Understanding vs Mimicry two-axis; capstone-level rigor (p.8,13). |
| 2025-Unknown (Multi-Agent) | Multi-agent redundant/adversarial LLM evaluators for fairness; framework only, no empirical validity (n/a). |
| 2018-Crone (SMID) | ICC(A,k) "excellent" all 8 dims; political-balance rater requirement (≥5 lib/con/mod per item) (p.11). |
| 2022-Fraser (Delphi) | Bottom-up crowd labels reproduce annotators' demographic moral profile; majority vote suppresses minorities (p.8). |
| 2023-Ibrohim | FGD with cybercrime-police validates hate taxonomy; annotator diversity as bias-reduction (p.9). |
| 2024-Aksoy | MFQ-2 (measurement-invariant across 25 pops) run 100×; two-way ANOVA language×model interaction (p.6-7). |
| 2024-Cahyawijaya | Specificity check: value embeddings drop to ~2.5% accuracy on non-value QAs (LIMA control) (p.6). |
| 2024-Kajiwara | Dataset-size ablation (20%→100% = F1 0.34→0.72) shows data > model complexity (p.14). |
| 2024-Nogara | Perspective scores German +0.085 vs English translation; artifact not content (p.5). |
| 2024-Senthilkumar | Cross-entropy vs Dirichlet-multinomial decouples confidence from calibration; GPT-4o Yes/No ~90% regardless (p.5). |
| 2025-Arnob | OOV masks bias: only 4.25% of STEM words in-vocabulary; report OOV rate before bias metrics (p.7). |
| 2025-Dickerson | LLM indecision ~0–6% vs human ~17%; determinism itself is misalignment (p.6). |
| 2025-Liu (frameworks) | Distributional fidelity (KL-D vs WVS) distinct from consistency; MARK κ only 0.02–0.15 (p.15-16). |
| 2025-Morlat (COMETH) | ARI (LLM clusters vs ground-truth actions) as preprocessing validity checkpoint; 60% vs 30% alignment (p.5,7). |
| 2025-Snoswell | 96% of 69 surveyed papers use static data; 75% use ground-truth match; argues for reasonableness over accuracy (p.4). |
| 2026-Hu | Cross-lingual probe transfer discrepancy δ as validity check for language-agnostic moral constructs (p.6). |
| Anthropic-Alignment_Faking | Compliance gap 11–15% between believed-training vs believed-unmonitored; eval-context contamination (p.16). |
| Anthropic-Collective_CAI (=Sycophancy) | "Are you sure?" flips correct answers 32–86%; humans prefer sycophancy on hard items (p.4,9). |
| Anthropic-Summer_2025_Pilot_Sabotage | Model-organism validation of the audit suite; ~5% situational-awareness markers (p.13,20). |
| Meta-CyberSecEval_3 | LLM-judge vs human r=0.89; consensus-of-judges proposed; agentic scaffolding = 20× uplift eval gap (p.6,21). |
| OpenAI-gpt-4o | Medical benchmarks "increasingly saturated"; pre-registered persuasion RCT (3,800+ participants) (p.16,21). |
| OpenAI-o3-mini-vs-deepseek | API safeguard rejected 44.8% of inputs → system-level not model-level measurement (p.7). |
| 2024-Wasi | N=20 minimal contrast pairs; convergent direction across 3 model families; no IAA (p.7). |

## C. Patterns & disagreements

**Convergence.** (1) Expert + anchored annotation beats fragmented crowd annotation on κ — [2020-Yasseri], [2023-Maity], [2022-Beyhan], [2025-Kumar] cluster κ≥0.74 while [2025-Enguix], [2022-Yilmaz] bottom out. (2) Nearly every card independently reaches the *same* lesson — separate competence from construct: control sets [2024-Neplenbroek], specificity controls [2024-Cahyawijaya], pinned/BPSN [2018-Dixon; 2019-Borkan], OOV auditing [2025-Arnob], API-safeguard disentangling [OpenAI-o3-mini-vs-deepseek]. (3) Repetition-for-stability is near-universal [2024-Ji; 2024-Aksoy; 2025-Sukiennik; 2025-Kumar; 2025-Mohammadi].

**Disagreement.** (1) *Does recognition predict behaviour?* SafetyBench answers strongly yes (r=0.91–0.99) [2024-Zhang], but Snoswell's survey argues 96% of the field tests pre-packaged recognition and never tests spontaneous moral sensitivity, calling ground-truth accuracy "unattainable" [2025-Snoswell] — and Alignment Faking shows recognition and behaviour diverge by design when the model is eval-aware [Anthropic-Alignment_Faking]. (2) *Is majority-vote a valid key?* MoralBench, EvalMORAAL, Sukiennik key to human/population means [2024-Ji; 2025-Mohammadi; 2025-Sukiennik], while Fraser, Dickerson, PluriHarms, and Senthilkumar argue population-mean scoring penalizes principled minorities and erases the disagreement that *is* the construct [2022-Fraser; 2025-Dickerson; 2026-Li-PluriHarms; 2024-Senthilkumar]. (3) *Are human self-report instruments valid for LLMs?* Aksoy and Songyuan Liu apply MFQ-2/Pew Typology and defend it via measurement invariance / convergent correlation [2024-Aksoy; 2024-Songyuan Liu], but both cards flag that LLMs lack the subjective referent the "describes me" framing presupposes. (4) *High reliability = good?* Li's α>99% is treated as a red flag for item redundancy, not a strength [2025-Li] — directly contradicting the naive "higher κ/α is better" heuristic.

## D. Exemplars & anti-patterns

**Best-designed.** *MBBQ* [2024-Neplenbroek] is the cleanest construct-validity design here: a parallel control set neutralizes the stereotype, bias is only interpreted where competence is established, the metric is accuracy-bounded (a perfect model is provably unbiased), stereotypes are retained only if native speakers confirm them in all four languages (so cross-lingual score gaps isolate model inconsistency from culture), and it mandates per-category rather than aggregate reporting. *SafetyBench* [2024-Zhang] is the exemplar for predictive validity — it does the work of proving its recognition scores forecast generation behaviour instead of assuming it, and even quantifies augmentation-bias. *BengaliMoralBench* [2025-Kumar] is the exemplar reliability package: documented calibration pilot (κ 0.61→0.87), from-scratch authorship as contamination control, lexical-neutrality to block shortcut solving, and MCC+κ+temperature-variance reported as standard. *SMID* [2018-Crone] models item-level psychometrics (ICC(A,k), per-image CIs, political-balance rater panels).

**Worst-designed / cautionary.** *Telugu HS* [2024-Khanduja]: 98.2% accuracy, no IAA, no size, self-flagged leakage/imbalance — a validity black box. *PerGOLD* [2025-Jafarinejad] and *AMI@EVALITA* [2020-Nozza-AMI]: usable datasets undermined by zero reliability reporting. *BenchMoral* [2025-Flores]: right instincts but n=80 single-city students, no α, no significance tests, model-version confounded with language. *Li SWT* [2025-Li]: sophisticated psychometrics partly invalidated by circularity (GPT-4o generates items and is a test subject) and α>99% redundancy. *o3-mini comparison*: a methodological caution — 44.8% of inputs never reached the model, so "1.19% unsafe" is system- not model-level [OpenAI-o3-mini-vs-deepseek].

## E. Design lessons

1. **Report a chance-adjusted reliability statistic (Krippendorff α, Cohen/Fleiss κ, MCC) or the benchmark has no validity floor** — absence is common and disqualifying [2020-Nozza-AMI; 2025-Jafarinejad; 2024-Khanduja; 2018-Dixon; 2025-Kumar].

2. **Run a calibration pilot and anchor every scale level with concrete examples; coarsen scales annotators cannot reliably perceive.** κ jumped 0.61→0.87 after a pilot [2025-Kumar]; a 10-point scale was replaced by an anchored 5-level scale [2022-Beyhan; 2024-Tonneau].

3. **Use domain-expert or community-matched annotators for subjective value judgments; never fragment one construct across dozens of non-overlapping annotators.** Experts reached α=0.895 [2020-Yasseri]; fragmentation drove κ to 0.12 [2025-Enguix]; community matching is a validity lever [2025-Salles; 2023-Ibrohim; 2018-Crone].

4. **Build a control that neutralizes the construct so "misaligned" separates from "incapable"**: neutral-name control sets [2024-Neplenbroek], non-value specificity controls [2024-Cahyawijaya], pinned/BPSN decompositions [2018-Dixon; 2019-Borkan], OOV-rate reporting before bias metrics [2025-Arnob], and model-vs-system disentangling [OpenAI-o3-mini-vs-deepseek].

5. **Prove predictive validity — show recognition scores forecast behaviour rather than assuming it** [2024-Zhang], and correlate value scores with downstream harm-detection [2024-Songyuan Liu].

6. **Anchor scoring to human population data but report the full distribution — treat disagreement as signal.** WVS/PEW/MFQ keys work [2025-Mohammadi; 2024-Ji]; add a harm×agreement axis [2026-Li-PluriHarms], measure indecision against human ~17% [2025-Dickerson], and score distributional divergence not modal match [2024-Senthilkumar; 2025-Liu; 2022-Fraser].

7. **Report per-category, never a single aggregate number; prefer Macro-Recall/AUC when true negatives are structurally unavailable** [2024-Neplenbroek; 2025-Brito; 2025-Jigsaw].

8. **Establish measurement reliability via repetition and temperature-variance tables; use cross-sample self-consistency as an uncertainty signal** [2024-Ji; 2024-Aksoy; 2025-Kumar; 2025-Mohammadi].

9. **Add consistency/confound probes: opposing-framing pairs (watch the refusal confound) [2025-Gupta], transitivity checks [2025-Wu], and "Are you sure?" challenges that flip correct answers 32–86% [Anthropic-Collective_CAI/Sycophancy].**

10. **Audit the scoring instrument (LLM judge or API) for its own cultural bias.** Translate-and-recheck exposes scorer artifacts [2024-Nogara]; validate judges against humans (r=0.89), use different-developer/consensus judges, and report judge κ [Meta-CyberSecEval_3; 2025-Gupta; 2025-Mohammadi].

11. **Design against evaluation-context contamination** — an 11–15% compliance gap appears when a model believes it is monitored [Anthropic-Alignment_Faking]; measure situational-awareness base rates and validate the suite against planted model-organism behaviours [Anthropic-Summer_2025_Pilot_Sabotage].

12. **Avoid circularity and ceiling saturation**: do not let the generator model also be the test subject [2025-Li; 2024-Lee; 2026-Li-PluriHarms]; over-sample the ambiguous middle [2026-Li-PluriHarms]; near-saturated benchmarks stop discriminating frontier models [OpenAI-gpt-4o]; build from scratch with lexical-neutrality [2025-Kumar].

13. **Pair labels with human rationale spans and score faithfulness, not just plausibility — the best classifier is often not the most faithful explainer** [2025-Salles].
