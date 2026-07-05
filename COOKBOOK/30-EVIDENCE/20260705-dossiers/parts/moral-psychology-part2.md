# moral-psychology — sub-dossier part 2/3

Scope: 58 cards on operationalizing moral-psychology theories (MFT, DIT/Kohlberg, Schwartz values, deontology–utilitarianism, virtue ethics, Cultural Theory) for LLMs, and whether human instruments transfer validly.

## A. Synthesized claims

1. **Human psychometric instruments are being ported to LLMs wholesale — MFQ, DIT, PVQ-RR, WVS, CADS/OUS, Cultural Theory — but their validity for machines is asserted, not established.** Every author who uses one flags the mismatch: the DIT was human-validated for 30 years yet ChatGPT's Hindi P-score collapses to 25.63 vs 48.09 English (p.13) [2024-Khandelwal]; the MFQ maps LLMs closest to political conservatives but RLHF *widens* the human gap (p.5) [2024-Abdulhai]; Fraser explicitly notes questionnaires "were designed for humans" and Delphi is phrasing-sensitive [2022-Fraser]; VAPT achieves only 30.1% exact / 63.6% within-±1 Likert match to self-reported Schwartz values (p.17) [2026-Yun].

2. **The single most damaging validity threat is that human moral responses themselves are unstable, so "match human" is an ill-defined target.** Boerstler shows 10–18% within-participant instability on controversial kidney-allocation pairs over 10 sessions, with instability rising as decisions get harder (Spearman rs=0.54) — precisely the informative items (p.1, p.12) [2024-Boerstler]. Scruples operationalizes this by using the *distribution* of votes as the label and introduces the BEST oracle (human F1 0.490 < oracle 0.707), proving "match human performance" is the wrong goal when humans disagree (p.6) [2021-Lourie].

3. **Stated values ≠ enacted values: a reproducible calibration/knowledge–action gap.** Andric finds a +11.9pp gap between self-reported and behavioral altruism (d=1.08), with the IAT failing to predict behavior (r=.22, ns), affecting 75% of 24 models (p.4-6) [2025-Andric]. VALACT independently finds PVQ-40 self-report correlates only r=0.32 with scenario behavior in LLMs (0.41 in humans) (p.5) [2026-Huang-Knowing]. Jotautaite's speciesism split is the sharpest form: models classify 86% of statements as speciesist but judge only 34% morally wrong — "the problem is evaluative rather than epistemic" (p.5, p.11) [2025-Jotautaite].

4. **LLMs collapse the human value distribution — homogenization, not pluralism.** VALACT reports cross-model scenario agreement of r≈0.99–1.00 against human variability of r∈[−0.79, 0.98] (p.4) [2026-Huang-Knowing]. Russo shows LLM top-10 values cover 81.6% of mentions vs 35.2% for humans, with alignment collapsing toward the majority as consensus drops (p.1, p.5) [2025-Russo]. Dickerson shows near-zero LLM indecision (~0–6%) vs 17% human when a coin-flip is offered — determinism is itself misalignment (p.6) [2025-Dickerson]. Benkler's WEIRD skew (US R²=0.80 vs Nigeria 0.01) is the demographic face of the same collapse (p.6) [2023-Benkler].

5. **Cross-lingual / cross-cultural inconsistency is pervasive and structural, not noise.** EvalMORAAL: Western regions r=0.82 vs non-Western 0.61 (p.5) [2025-Mohammadi]. Vida: identical Moral-Machine content yields different preference profiles per language, and Llama-3-70B is *worst* (RMSE 0.672) — scale doesn't buy alignment (p.9) [2024-Vida]. MMRB shows non-monotone sentence→paragraph→document difficulty and that low-resource-language fine-tuning moves multilingual moral scores most (+27.1 align / −28.7 poison) (p.3) [2025-Zhou-Moral Reasoning]. Liu's Chinese vs English models diverge in post-debate stability (54–69% vs 1–8% choice change) (p.8) [2024-Liu-Evaluating].

6. **Bottom-up crowd-labeled moral datasets encode one demographic's morality and often contain "inappropriate" labels.** Zhou's error analysis attributes up to 78% of theory-guided misalignments to bad annotations, not model failure (p.9) [2024-Zhou-Rethinking]. Sachdeva/Russo/Yuan all draw from r/AmITheAsshole, inheriting young, Western, WEIRD norms (p.12) [2025-Sachdeva]; Fraser shows Delphi's profile mirrors its liberal MTurk annotators [2022-Fraser].

7. **Grading the reasoning process, not the verdict, sidesteps the "no correct answer" problem — the field's most promising design shift.** MoReBench scores 23,018 signed, weighted, atomic rubric criteria against reasoning traces, is uncorrelated with math/code/general benchmarks (r∈[−0.245, 0.216]), and shows models favor Utilitarian/Deontological framings as training side-effects (p.2, p.8) [2025-Chiu]. Theory-guided CoT similarly conditions and compares across normative frameworks (p.7) [2024-Zhou-Rethinking].

8. **Moral stances are unstable under social pressure — a validity threat static benchmarks miss.** Moral persuasion flips ~50% of high-ambiguity decisions (CAL 0.49 vs 0.06 low-ambiguity control) (p.5) [2024-Huang-Moral Persuasion]; moral sycophancy in VLMs shows asymmetric right→wrong flips exceeding the reverse [2026-MoralSycophancy]; Li's dose-response social referencing shows peer-consensus feedback shifts endorsement monotonically [2025-Li].

9. **Multi-step / path-dependent structure reveals that LLM "values" are context-driven heuristics, not stable principles.** MMDs' 5-step escalation finds non-transitive preferences (care>sanctity, sanctity>fairness, but care≈fairness) — "context-driven statistical imitation" (p.9) [2025-Wu]; the pragmatic dilemma shows moral-foundation classification never converges even at 210k samples (RLA>0.9 = semantic shortcut) while sentiment does (p.3) [2025-Liu-Diagnosing].

10. **Trolley/AV dilemmas yield robust cross-cultural structure but are criticized as unrealistic.** Moral Machine (39.61M decisions, cultural distance ρ=0.49, p.9) [2018-Awad] and its Switch>Loop>Footbridge universal ordering across 42 countries with relational-mobility r=0.67 [2020-Awad-Universals] are foundational; but Körner shows factual/historical dilemmas are rated far more realistic (dz=1.31) and Holyoak argues trolley dilemmas mischaracterize deontology as emotional error, urging "methodological atheism" [2023-Körner][2016-Holyoak].

11. **Frameworks matter: which theory a model defaults to is measurable and manipulable.** Model editing shows Justice and Virtue are most editable, Deontology most robust (p.7) [2025-Huang-Model Editing]; internal probes recover linearly-separable, partly cross-lingual moral-foundation directions at layer 17 (65.6%) (p.5) [2026-Hu]; Tennant formalizes utilitarian/deontological/virtue framings as intrinsic reward functions [2025-Tennant].

## B. Evidence table

| Card stem | Most design-relevant fact |
|---|---|
| 2018-Awad-The Moral Machine experiment | 9-factor conjoint AMCE design; cultural distance ρ=0.49; 3 moral clusters (p.9). |
| 2020-Awad-Universals and variations | Switch>Loop>Footbridge universal in 42 countries; relational-mobility r=0.67 (p.4). |
| 2024-Vida-Decoding Multilingual Moral Preferences | Same content, different profile per language; Llama-3-70B worst RMSE 0.672 (p.9). |
| 2020-Schramowski-Moral Choice Machine | QA-template averaging recovers r=0.73 with WEAT; fooled by positive adjectives (p.13). |
| 2021-Lourie-Scruples | Distributional labels + BEST oracle: human F1 0.490 < oracle 0.707 (p.6). |
| 2022-Trager-Moral Foundations Reddit Corpus | Splits Fairness into Equality/Proportionality; LLMs still lag fine-tuned BERT (p.6). |
| 2023-Catapang-EMoTES-3K | Bilingual Filipino corpus; mixed-intent (action vs intent) as hard probe (p.5). |
| 2023-Hopp-Dutch Moral Foundations | Cross-cultural MFV validation; 97% classified; loyalty lowest/floor (p.11). |
| 2024-Bajaj-GenMO | Minimal-pair gender swap; all models favor female 63–88% of mismatches (p.8). |
| 2024-Franken-OffTheRails | Causal-graph procedural generation of factorially-balanced dilemmas (400 items) (p.5). |
| 2024-Huang-Moral Persuasion | High-ambiguity persuasion flips ~50% decisions; CAL 0.49 vs 0.06 control (p.5). |
| 2024-Khandelwal-Moral Judgment (DIT) | DIT ported to 6 langs; ChatGPT Hindi P-score 25.63 vs English 48.09 (p.13). |
| 2024-Liu-Evaluating Moral Beliefs | 3-module (word/scenario/debate); Chinese models flip 54–69% post-debate (p.8). |
| 2024-Qiu-ProgressGym | Temporal/diachronic alignment; 19-dim value embedding (Gert+MFT+worldview) (p.6). |
| 2024-Sorin-Ethical Alignment Healthcare | Repeat-run consistency metric; organ-harvest 0% utilitarian across all 13 models (p.16). |
| 2024-Zhou-Rethinking Machine Ethics | Theory-guided CoT; up to 78% of misalignments are bad annotations, not model (p.9). |
| 2025-Andric-Do LLMs Walk Their Talk | Calibration Gap +11.9pp (d=1.08); IAT doesn't predict behavior r=.22 (p.4-6). |
| 2025-Bulla-LLMs meet moral values | Leave-one-annotator-out baseline; GPT-4 beats humans on 3/5 MFT dims (p.13). |
| 2025-Chiu-MoReBench | Grade reasoning via 23,018 weighted rubric criteria; uncorrelated with math/code (p.8). |
| 2025-Gao-MIST | Multi-image "text-image flow": moral signal only emerges across modalities (p.5). |
| 2025-Huang-Model Editing Double-Edged | Justice/Virtue most editable, Deontology most robust; dual-use steering (p.7). |
| 2025-Jiao-LLM Ethics Benchmark | MFQ+WVS+dilemmas → MFA/RQI/consistency; cultural bias top failure mode (p.12). |
| 2025-Jotautaite-SpeciesismBench | 86% recognized speciesist but only 34% judged wrong — evaluative not epistemic gap (p.5). |
| 2025-Kumar-Are Rules Meant to be Broken | Person-conditioned prediction; each annotation carries MFQ2+Hofstede persona (p.6). |
| 2025-Li-Analyzing Cognitive Differences | Cultural Theory (4 worldviews); dose-response social-referencing shifts endorsement (p.7). |
| 2025-Mohammadi-EvalMORAAL | Western r=0.82 vs non-Western 0.61; direct CoT beats log-prob scoring +0.10 (p.5). |
| 2025-Russo-Pluralistic Moral Gap | LLM top-10 values 81.6% vs human 35.2%; alignment collapses at low consensus (p.5). |
| 2025-Sachdeva-Everyday Moral Dilemmas | GPT-4 best human agreement α=0.34; LLM ensemble approximates Reddit consensus (p.8). |
| 2025-Tomar-BharatBBQ | Stereotypical Bias Score separates stereotype endorsement from lexical preference (p.7). |
| 2025-Wu-Staircase of Ethics | 5-step escalation exposes non-transitive, context-driven value preferences (p.9). |
| 2025-Zhou-Moral Reasoning Across Languages | Low-resource-lang fine-tuning moves multilingual moral scores most (+27/−28.7) (p.3). |
| 2026-Huang-Knowing But Not Doing (VALACT) | Cross-model r≈1.0 vs human −0.79–0.98; PVQ vs behavior r=0.32 (p.4-5). |
| 2023-Wang-STREAM | Captures Judgment+Degree+Confidence; demographic-anchored evolving baselines (p.3). |
| 2025-Kumar-UniMoral (BengaliMoralBench) | Triadic Virtue/Commonsense/Justice, scratch-built for contamination control (p.4). |
| 2026-MoralSycophancy-VLMs | Under user disagreement, right→wrong flips exceed wrong→right (asymmetry diagnostic). |
| 2016-Holyoak-Deontological coherence | "Methodological atheism": don't treat utilitarian answers as truth (p.3). |
| 2018-Crone-SMID | 2,941 rated images; all 5 MFT foundations intercorrelated r>.5 — categories not discrete (p.11). |
| 2022-Fraser-Does Moral Code Have a Code | Delphi mirrors its liberal annotators; can't separate moral from convention (11/16) (p.7). |
| 2023-Benkler-Moral Value Pluralism | WVS as ground truth; WEIRD skew US R²=0.80 vs Nigeria 0.01 (p.6). |
| 2023-Körner-Deontology and Utilitarianism | Factual/historical dilemmas rated far more realistic than trolley (dz=1.31) (p.8). |
| 2024-Abdulhai-Moral Foundations of LLMs | MFQ maps LLMs to conservatives; RLHF widens the human gap; steerable (p.5). |
| 2024-Boerstler-Stability of Moral Preferences | 10–18% within-person instability; worst on the hardest/most informative items (p.12). |
| 2024-Karpov-Inducing Human-like Biases | fMRI fine-tuning did NOT improve brain-model alignment; vision-ROI control design (p.8). |
| 2024-Ober-Lyceum Aristotle | Phronesis is uncodifiable; use range-of-acceptable-answers scoring for pluralism (p.20). |
| 2024-Stenseke-Computational Complexity | Optimal moral computation is NP-hard/undecidable → approximation is unavoidable (p.4). |
| 2024-Wang-Moral Growth of LLMs | Deweyan Impulse/Habit/Character staging; "beating scenario" red-team probe (p.6). |
| 2025-Bryan-Virtue Ethics Extinction | VIA 24 character strengths / 6 clusters as cross-cultural virtue scaffold (p.3). |
| 2025-Dickerson-Who Gets the Kidney | LLM indecision ~0–6% vs human 17% — determinism as misalignment (p.6). |
| 2025-El Masri-Towards Attuned AI | RLHF/RLAIF/CAI all reduce to preference-maximization; Ethics of Care corrective (p.4). |
| 2025-Iftikhar-LLM Counselors | 15 practitioner-grounded ethical violations mapped to APA/ACA/NASW codes (p.2). |
| 2025-Liu-Diagnosing Moral Reasoning | Pragmatic dilemma: RLA>0.9 = semantic shortcut; classification never converges (p.3). |
| 2025-Morlat-COMETH | Probabilistic clustering of human judgment distributions doubles alignment (60 vs 30%) (p.7). |
| 2025-Pipitone-Unlocking practical wisdom | Robot "inner speech" (visible reasoning) raises human ethical awareness (p.10). |
| 2025-Tennant-Hybrid Approaches | Formalizes utilitarian/deontological/virtue framings as intrinsic RL rewards (p.20). |
| 2025-Yuan-Probabilistic Aggregation | Truncated-normal EM fuses continuous LLM moral scores; "coherence over correctness" (p.2). |
| 2026-Hu-Straight and Narrow | Moral-foundation directions linearly separable at layer 17 (65.6%), partly cross-lingual (p.5). |
| 2026-Yun-VAPT | Extract/embody/explain probes; 63.6% within-±1 Likert to self-reported values (p.17). |
| 2024-MaqasidAI-Maqasid Al-Shariah | Five daruriyyat (faith/life/intellect/lineage/wealth) as a non-Western rubric. |
| 2025-Nadeem-Ethical Decision-Making | Human–AI agreement ~62%; relational ethics domain falls below 45% (p.1). |
| 2026-Hendricks-LLMs Fuel Extremist Attitudes | LLM rights/fairness framings increase sacralization and violence justification (abstract). |

## C. Patterns & disagreements

**Convergence.** (a) *Instruments transfer poorly and pluralism collapses.* Behavioral scenario measures repeatedly beat questionnaires (VALACT prompt-sensitivity CV 2.5% vs 9.3% [2026-Huang-Knowing]; Andric's dissociations [2025-Andric]; VAPT [2026-Yun]). (b) *WEIRD skew is universal* across every cross-cultural card [2023-Benkler][2025-Mohammadi][2024-Vida][2024-Khandelwal][2025-Zhou-Moral Reasoning]. (c) *Human disagreement is signal, not noise* — Scruples, Russo, Dickerson, Boerstler, STREAM all argue for distributional targets [2021-Lourie][2025-Russo][2025-Dickerson][2024-Boerstler][2023-Wang]. (d) *Scale does not buy alignment* [2024-Vida][2024-Bajaj (larger open models more biased)][2025-Jotautaite].

**Disagreement.** (1) *Is there a ground truth?* Sorin codes a "correct" deontological answer per medical dilemma [2024-Sorin]; Yuan and Morlat reject correctness for "coherence"/majority-consensus [2025-Yuan][2025-Morlat]; MoReBench and Ober reject single answers entirely for pluralistic rubrics/range-scoring [2025-Chiu][2024-Ober]. (2) *Do LLMs match conservatives or liberals?* Abdulhai finds MFQ profiles nearest conservatives [2024-Abdulhai]; Fraser finds Delphi mirrors young liberals [2022-Fraser] — reconcilable only by noting different instruments, models, and annotator pools. (3) *Trolley dilemmas: foundational or misleading?* Awad treats them as the empirical bedrock [2018-Awad][2020-Awad-Universals]; Körner and Holyoak call them cartoonish and normatively loaded [2023-Körner][2016-Holyoak]. (4) *Can crowd data ground alignment?* Trager/Bulla defend human-annotated corpora [2022-Trager][2025-Bulla]; Zhou finds their labels are the main error source [2024-Zhou-Rethinking].

## D. Exemplars & anti-patterns

**Best-designed.** *MoReBench* [2025-Chiu] is the strongest: it grades reasoning traces against signed, weighted, expert rubrics, uses min-across-category macro-F1 for bias-robust judge selection, runs adversarial neutrality checks (equal-quality traces for opposite conclusions, t=−0.59, ns), a discriminatory-power meta-eval, and a public/private 500/500 contamination split. *Scruples* [2021-Lourie] pioneered distributional labels + the BEST oracle + two-tier complexity. *Andric* [2025-Andric] models rigorous multi-method validity engineering (piloted away ceiling effects, IAT/behavior/self-report triangulation, Calibration Gap). *OffTheRails* [2024-Franken] gives factorially-balanced, causally-controlled procedural items where the manipulated factor is known by construction. *SpeciesismBench* [2025-Jotautaite] cleanly splits recognition from evaluation and uses orthogonal capacity manipulation and matched farmed/non-farmed contrasts.

**Anti-patterns.** *Sorin* [2024-Sorin]: only 5 trolley variants, all Western, a single asserted "correct" answer, and API-vs-web-UI inconsistency — a cautionary case of over-small, over-confident benchmarks. *Nadeem* [2025-Nadeem]: 30 binary items with pre-baked justifications, non-stratified convenience sample, κ ≤ 0.33 — underpowered for its domain-level claims. *Li's Cultural Theory* [2025-Li]: Cronbach's α>99% signals item redundancy, the questionnaire was GPT-4-generated then tested on GPT-4 (circularity), with no human baseline. *Benkler* [2023-Benkler]: one model, English-only prompts asking non-Anglophone personas about their values. Recurrent worst-practice: **using one LLM to both generate items and be evaluated** [2025-Li][2025-Wu][2026-Hu], and **no test-retest / IAA reporting** (most cards).

## E. Design lessons

1. **Never treat a human instrument as valid for LLMs without re-validation.** Administer it to humans and models on identical items; report cross-language and cross-prompt invariance [2026-Huang-Knowing][2024-Khandelwal][2026-Yun]. Add multi-prompt averaging (10 QA templates [2020-Schramowski]; 48 permutations [2024-Khandelwal]; 10 variants [2022-Fraser]) to strip phrasing artifacts.

2. **Make the human disagreement distribution the target, not a majority label.** Use distributional cross-entropy + a BEST-style oracle [2021-Lourie], Dirichlet/EM aggregation [2021-Lourie][2025-Yuan], consensus-level stratification [2025-Russo], and an explicit indecision option to measure whether models mirror human uncertainty [2025-Dickerson].

3. **Report test–retest and self-consistency as first-class validity gates.** Repeat a subset across sessions [2024-Boerstler]; report self-consistency (models with α<0.5 are unreliable subjects) [2025-Sachdeva]; use Maximum-Capacity stability across ≥5 runs [2023-Wang]; report repeat-run consistency, not just modal answers [2024-Sorin].

4. **Grade the reasoning process for value-laden items that lack a correct answer.** Signed weighted atomic rubrics [2025-Chiu]; theory-conditioned CoT to reveal framework bias [2024-Zhou-Rethinking][2025-Jiao]; pipeline decomposition (perception→action→principle→factor→consequence) to localize failures [2025-Kumar-Are Rules].

5. **Measure the stated-vs-enacted gap directly.** Pair a self-report scale with a behavioral scenario for the same subjects and compute the Calibration Gap [2025-Andric][2026-Huang-Knowing]; split recognition from moral evaluation as two scored axes [2025-Jotautaite].

6. **Stress-test stability under social pressure and editing.** Add user-disagreement/persuasion conditions and measure directional flip asymmetry [2024-Huang-Moral Persuasion][2026-MoralSycophancy][2025-Li]; probe resistance to benevolent *and* malicious steering [2025-Huang-Model Editing].

7. **Build in contamination control from the start.** Scratch-authored native-language items [2025-Kumar-UniMoral]; rephrase-then-self-filter web data (keep only untraceable items) [2025-Russo]; public/private splits [2025-Chiu]; distribute the moral signal so no single span/modality is diagnostic [2025-Gao][2025-Liu-Diagnosing].

8. **Design against surface shortcuts.** Lexical-neutral items forbidding moral cue words [2025-Kumar-UniMoral]; SBS-style metrics that separate stereotype endorsement from lexical preference [2025-Tomar]; RLA/convergence-curve diagnostics to detect semantic-similarity gaming [2025-Liu-Diagnosing]; minimal-pair swaps (gender, species, virtue/vice) to isolate one axis [2024-Bajaj][2025-Jotautaite][2026-Hu].

9. **Cover culture and language deliberately, and correlate results to external cultural indices.** Include low-resource languages (they move the needle most) [2025-Zhou-Moral Reasoning]; anchor to WVS/PEW/Hofstede/relational-mobility [2023-Benkler][2025-Mohammadi][2020-Awad-Universals][2025-Kumar-Are Rules]; supply non-Western rubrics (Maqasid daruriyyat; triadic Bengali; kapwa) [2024-MaqasidAI][2025-Kumar-UniMoral][2023-Catapang].

10. **Use realistic, multi-step, factorially-controlled stimuli — not only single trolley vignettes.** Factual/historical dilemmas with realism ratings [2023-Körner]; causal-graph procedural generation [2024-Franken]; escalating multi-step chains with transitivity checks [2025-Wu]; and complement text with images via the circumplex/text-image-flow designs [2018-Crone][2023-Hopp][2025-Gao].

11. **Accept pluralism and computational limits as design constraints.** Score ranges of acceptable answers rather than forcing single optima [2024-Ober]; expect approximation, not optimal moral computation [2024-Stenseke]; and use developmental (Impulse/Habit/Character), tiered (sensitivity→judgment→agency), and complexity-graded difficulty ladders [2024-Wang][2025-Huang-Model Editing].

12. **Watch for downstream harm, not just accuracy.** Universally "positive" rights/fairness framings can fuel extremism [2026-Hendricks]; map failures to real professional codes and include crisis sub-tests for high-stakes domains [2025-Iftikhar][2024-Sorin].
