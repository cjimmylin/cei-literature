# Literature Review — Moral Psychology for LLM Benchmarking

> **CEI COOKBOOK · 10-LITERATURE.** Descriptive companion to the prescriptive synthesis in
> `00-KNOWLEDGEBASE/09-moral-psychology-methods.md` (which this review does not duplicate — that
> file says what to *do*; this one says what *exists* and what was *found*). Primary evidence:
> `30-EVIDENCE/20260705-dossiers/20260705-moral-psychology-dossier.md` (~176 cards) and
> `30-EVIDENCE/20260705-digests/20260705-moralpsych-digest.md` (the 292-candidate "Triple Bind"
> meta-evaluation, 292 candidates × 162 features × 13 theories, 23 benchmarks × 9 models). `[stem]` =
> evidence card in `30-EVIDENCE/20260705-cards/`.
>
> **Self-administration disclosure (load-bearing):** the meta-evaluation's empirical arm was
> designed by the Claude family, which also served as 3 of 9 subjects under a single Opus
> orchestrator, N=1 per model-benchmark pair at temperature 0. Every *model-specific absolute value*
> below (foundation ratios, DIT P-scores, win rates, ECI) is therefore **hypothesis-generating, not
> confirming**. The *comparative* findings — cross-vendor convergence, the quality↔convergence
> correlation — survive because they replicate across three independently-built vendors.

Audience: a model that will design new moral-psychology benchmarks. This review maps the descriptive
terrain — the theories, their human instruments, what happens when those instruments meet LLMs, the
shape of the current benchmark landscape, and the empirical regularities a new instrument must design
around.

---

## 1. The thirteen theories and their human instruments

The meta-evaluation partitions the field into **13 moral-psychology theories**, each with a distinct
human measurement tradition and a distinct amount of transferable computational infrastructure. The
central descriptive fact is that **quality tracks infrastructure, not theoretical merit** (Claim 1):
a theory with a validated questionnaire *and* an annotated corpus dominates; one asset yields
moderate quality; zero yields zero.

**Moral Foundations Theory (Graham/Haidt).** Measures endorsement of five-to-six innate foundations —
Care, Fairness, Loyalty, Authority, Sanctity/Purity (+ Liberty). Instruments: the **MFQ-30**
(validated 30-item questionnaire with population norms across ≥11 countries), the **Moral Foundations
Vignettes / MFV** (length- and reading-level-controlled scenario items with a two-stage validation
ladder and a non-moral "social norms" control [2015-Clifford-Moral Foundations Vignettes]), and the
**Moral Foundations Twitter Corpus / MFTC** (35,108 expert-annotated tweets, Fleiss κ 0.27 rescued to
PABAK 0.62–0.91 [2020-Hoover-Moral Foundations Twitter Corpus]) plus its Weibo counterpart
[2024-Cao-The Moral Foundations Weibo Corpus]. MFT uniquely owns *two* computational assets, which is
why it holds **67/292 candidates (23% by volume) but 18 of 48 top-tier slots (37.5%) and a 73%
quality rate (49/67)** — ~6× the rate of non-Western traditions.

**Kohlberg / Rest — cognitive-developmental.** Measures the *stage* of moral reasoning
(pre-conventional → conventional → post-conventional). Instruments: the **Defining Issues Test (DIT)**
and its P-score (percent post-conventional), the Moral Judgment Interview, and the Moral Competence
Test. A multilingual DIT exists [2024-Khandelwal-Multilingual Defining Issues Test]. Quality rate
56%. The stage construct is a category error for LLMs (see §2).

**Schwartz — basic human values.** Measures 10 (or 19 refined) values on two orthogonal axes
(self-transcendence↔self-enhancement, openness↔conservation). Instruments: the **Portrait Values
Questionnaire (PVQ-40/PVQ-RR)**, the **Schwartz Value Survey (SVS)**, and the population-scale
**World Values Survey (WVS)**. Quality rate 57%.

**Dual-process (Greene).** Distinguishes fast affective (deontological) from slow controlled
(utilitarian) responding, operationalized through *personal* vs *impersonal* trolley dilemmas and
manipulations of cognitive load/time pressure. Source theory carries >10,000 citations, yet the theory
has **~9 candidates, all Low tier — zero publication-ready benchmarks** (Claim 3). Its infrastructure
is a paradigm, not a questionnaire.

**Moral identity (Aquino & Reed).** Measures the centrality of moral traits to self-concept (the
Self-Importance of Moral Identity scale, Internalization/Symbolization subscales). Source >3,000
citations; **2 candidates, all Low tier — zero usable benchmarks** (Claim 3). Motivation and
self-integration are essentially unmeasured (§6).

**Dyadic morality (Gray/Schein).** Models moral cognition as a template of intentional agent →
suffering patient. Instrument tradition: dyadic-completion and harm-attribution tasks. Only **n=2** in
the landscape (50% quality); the agent-patient structural manipulation is an untouched axis.

**Social intuitionism (Haidt).** Holds that judgment is intuitive and reasoning post-hoc,
operationalized through **moral dumbfounding** (maintaining a judgment after reasons are stripped).
Historically *misdetected* rather than missing — only **3 candidates (100% quality once the scorer's
keyword set was expanded to catch "moral dumbfounding" vocabulary)**.

**Trolley / Moral Machine paradigm.** The largest empirical apparatus in the field: the **Moral
Machine** collected >40M decisions (some sources: 39.61M) from 233 countries [2018-Awad-The Moral
Machine experiment; 2020-Awad-Universals and variations in moral decisions made], establishing a
universal Switch>Loop>Footbridge ordering. Quality rate 48%. Contested as foundational — factual/
historical dilemmas are rated far more realistic (dz=1.31) [2023-Körner], and Holyoak argues trolley
dilemmas mischaracterize deontology as emotional error [2016-Holyoak-Deontological coherence].

**Cultural theories.** Ubuntu (Afro-relational), Confucian, Indigenous, Islamic (Maqasid al-Sharia),
Buddhist. These have **essentially no computational psychometric infrastructure**: Ubuntu (13
candidates, **0%** quality), Confucian (13, **0%**), Indigenous (4, **0%**), Buddhist 12%. Islamic is
the intermediate exception (**36%**), because codified jurisprudential corpora substitute for a
questionnaire. Feature signature of the cliff: A4 (validated-instrument) mean = **0.0** across Ubuntu/
Confucian/Indigenous.

Remaining theories in the 13: **Moral Identity** (above, 0%), and an **Unclassified/theory-agnostic**
bucket (36%) housing crowdsourced multi-source resources such as ETHICS and Scruples.

---

## 2. The instrument-transfer literature: what breaks when human psychometrics meet LLMs

Administering a human scale to a model is the field's default method, and the transfer literature is a
catalogue of the ways it fails. Four regularities recur.

**(a) Within-instrument reliability can look human while cross-instrument coherence collapses.** GPT-4/
Claude 2.1 matched human within-scale consistency (MFV α up to 0.91) but "fail to show coherent
cross-abstraction-level moral values," with abstract→concrete R² **<0.08 vs human 0.17–0.38**
[2024-Nunes-Conscience Conflict]. Models strong on binary MFQ agreement collapse on the comparative
task (comparative totals 8–14 vs binary 44–58) [2024-Ji-MoralBench]. Schwartz transfers worst: VAPT
achieves only **30.1% exact / 63.6% within-±1 Likert match** to self-reported values [2026-Yun-VAPT].

**(b) The correct-answer effect / homogenization.** Models give near-uniform responses where humans
split. Almeida documents less variance than humans with inflated effect sizes [2024-Almeida-Exploring
the Psychology of LLMs Moral Reasoning]; GPT-3.5 gave **99–100% uniformity on 6 of 14 Many Labs 2
studies** (Less-is-better d=9.25 vs human d=0.78) [2025-Oh-Robustness]. Near-zero indecision (~0–6% vs
human 17%) when a coin-flip is offered is itself misalignment [2025-Dickerson-Who Gets the Kidney].

**(c) Recognition of public instruments destroys construct validity.** In the meta-eval's empirical
arm, **all 9 models hit 100% foundation-ID accuracy on MP22** — they reverse-engineer the psychometric
structure of a public test (a Messick threat). Reused canonical dilemmas (Trolley/Heinz) inflate
apparent competence [2025-Neuman-Analyzing].

**(d) Invariance is never established.** No card in the 176-card corpus demonstrates measurement
invariance between humans and models on identical items; transfer is always *asserted*, never
validated [2026-Yun-VAPT; 2022-Fraser-Does Moral Code Have a Code; 2024-Khandelwal]. Hämmerl found
"none of the models' MFQ scores map directly onto average human responses from any country"
[2023-Hämmerl-Speaking Multiple Languages]. The problem compounds because the human target is itself
unstable — 10–18% within-participant test-retest instability on controversial pairs, instability
rising as decisions get harder (Spearman rs=0.54) [2024-Boerstler-Stability of Moral Preferences;
2024-Keswani]. Developmental/trait frameworks fare worst: DIT "stage" is non-monotonic with scale and
persona-inflatable (§4), and moral dumbfounding does not transfer (autoregressive generation disfavors
"I can't explain why"; LLM dumbfounding rate 20–30% vs human 50–70%).

---

## 3. State of the art: the 292-candidate landscape

The meta-evaluation is the first full-coverage census of moral-psychology benchmarks for LLM
assessment. From a curated vault of **2,099 AI-ethics papers**, a five-signal extraction pipeline
identified **292 unique benchmark candidates** across the 13 theories, scored on a **162-feature
framework (158 active; 17 features feed the quality composite** = PD×0.50 + PE×0.30 + CI×0.20).
Jenks natural breaks (k=4; break points **[27.8, 43.05, 56.65]**, **GVF = 0.83**) partition the
composite into **Top 48 (16.4%), High 89 (30.5%), Med 72 (24.7%), Low 83 (28.4%)** — a bimodal,
"hollow" landscape. The tiering is robust: across 5 weighting schemes 72–84% of candidates retain
tier, Spearman ρ > 0.92.

The paper's thesis is a **triple bind** — the landscape is theoretically narrow, empirically
undiscriminating, and culturally blind — supported by seven statistics a benchmark designer should
treat as the baseline reality:

- **MFT dominance** (Claim 1): MFT holds **18/48 top slots** and a **73%** quality rate — driven by
  infrastructure (MFQ-30 + MFTC), not theoretical superiority.
- **Validity crisis** (Claim 2): **58%** of 292 sit at construct-validity Level 1–2 (keyword or face
  validity); median dropped from Level 3 to Level 2 under full coverage — the earlier optimistic
  picture (17% Level 1–2 in a 55-benchmark subsample) was a top-of-distribution sampling artifact, a
  **3.4× jump**.
- **Theoretical absence** (Claim 3): **0** publication-ready benchmarks for Dual Process (~9, all Low)
  and Moral Identity (2, all Low) despite >25,000 combined source-theory citations.
- **Cultural cliff** (Claim 4): Western mean quality **62% (93/149)** vs zero-quality traditions
  **0% (0/32)** — >3 billion people (~40% of humanity) whose dominant frameworks the landscape cannot
  evaluate at any quality level.
- **Baseline deficit** (Claim 5): no-human-data rose **18% → 34%** (100/292) under full coverage;
  population norms fell **42% → 15%** (43/292). Baseline-by-tier is monotonic: Top 0% no-data, Low
  **96% no-data**.
- **Temporal stagnation** (Claim 6): quality rate pre-2020 **75%**, 2020–2022 **48%**, 2023–2026
  **46%** — flat despite **9.5× volume growth**. Scaling without learning.
- **RLHF fingerprint** (Claim 7): of 23 tested benchmarks, **~43% produce zero cross-model variation**;
  quality predicts *convergence*, not discrimination, at **r = −0.83** (§4).

**Exemplar instruments worth reusing** (top of the composite distribution):

- **Jiao LLM Ethics Benchmark** (2025, composite **81.3**, MFT+Trolley) — highest in the landscape; a
  three-dimensional system integrating MFQ + WVS + standardized dilemmas with population norms and an
  open GitHub codebase, published in *Nature Scientific Reports* [2025-Jiao-LLM Ethics Benchmark].
- **Language Model Alignment in Multilingual Trolley / MultiTP** (2024, **79.17**) — multilingual
  trolley battery; only 75.9% paraphrase agreement exposes fragility [2024-Jin-Language Model Alignment
  in Multilingual Trolley].
- **Moral Machine** (2018, **71.73**) — the high calibration anchor; unmatched population norms, but
  returns **CV=0.000** across all 9 models — a memorized position, not judgment under uncertainty
  [2018-Awad-The Moral Machine experiment].
- **KorNAT** (2024, **69.0**) — Korean national-alignment benchmark; the "escape-hatch" exemplar
  proving the cliff is *infrastructure*, not culture — a non-Western community that built validated
  local instruments first [2024-Lee-KorNAT].
- **Scruples** (2021, **67.03**) — pioneered distributional labels (the vote *distribution* as the
  label) and the BEST oracle (human F1 0.490 < oracle 0.707) [2021-Lourie-Scruples]; alongside
  Hendrycks ETHICS (67.05) [2021-Hendrycks-Aligning AI with Shared Human Values].
- **Moral Foundations Vignettes / MFV** (composite 65.55) — the psychometric gold standard for item
  construction [2015-Clifford-Moral Foundations Vignettes].

Other reusable battery instruments: DIT (multilingual DIT 64.90), Value Kaleidoscope, Social Chemistry
101, M³oralBench. Islamic top-tier: QIAS/Bouchekif 60.55, Ghaly 58.45.

---

## 4. Empirical findings: the RLHF fingerprint and its correlates

The empirical arm administered 23 benchmarks (~750 items each) to **9 models × 3 vendors** at
temperature 0. Its headline is that **content-level instruments cannot discriminate frontier models**
(median CV across the battery ≈ **2.1%**; effective battery size ≈ 6, not 23), and that the failure is
structured into **six universal signatures shared by all 9/9 models** (subject to the
self-administration disclosure on absolute values):

1. **WEIRD-liberal foundation bias** — Individualizing/Binding ratio **2.43–2.83** (humans span
   0.5–3.5); over-weighting Care/Fairness/Liberty, under-weighting Loyalty/Authority/Sanctity. The
   single most-replicated finding corpus-wide [2024-Kirgis; 2025-Neuman-PRIME; 2024-Abdulhai;
   2024-Almeida; 2025-Jotautaite], and it *grows* with capability and RLHF [2024-Kirgis;
   2024-Abdulhai].
2. **Purity/sanctity floor** — ~**1.0** on a 0–5 scale; no human group floors here (secular Europeans
   ~2.0–2.5). "Sanctity/Loyalty exhibit little relevance in LLMs" [2024-Biedma-Beyond Human Norms].
3. **Authority-deference suppression** — win rate **exactly 0.29** (the most invariant finding).
4. **Ethical-consistency ceiling** — ECI = **1.0** on canonical trolley items (humans 0.4–0.7) —
   memorized positions.
5. **Post-conventional DIT default** — P-score **60–85**, persona-inflatable to **90.0** (human adults
   30–50); non-monotonic with scale, which is why DIT "development" is a category error and measures
   alignment calibration instead.
6. **Deontological refusal asymmetry** — personal-harm acceptance **0.10–0.50** vs impersonal **~0.95**
   [corroborated by 2025-Cheung, who traces the omission bias b=−0.22 vs human −0.03 to RLHF because
   the pretrained base lacks it].

**Homogenization / convergence.** Beyond the six signatures, low variance is pervasive: **43% zero
cross-model variation**; cross-model scenario agreement r≈0.99–1.00 against human variability r∈[−0.79,
0.98] [2026-Huang-Knowing But Not Doing (VALACT)]; LLM top-10 values cover 81.6% of mentions vs 35.2%
for humans [2025-Russo-Pluralistic Moral Gap]. The **quality↔convergence correlation r = −0.83** is
the deepest empirical result: the best psychometric instruments (MFQ-30, Moral Machine, TracingMF)
*most emphatically* confirm homogeneity, because the problem is dimensionality, not sensitivity.

**Knowing–doing gaps.** Stated values diverge from enacted behavior. DeNEVIL's generative attack found
most of 27 LLMs "essentially misaligned" (conformity 70.07→57.58) [2023-Duan-Denevil]; Andric finds a
**+11.9pp** self-report↔behavior altruism gap (d=1.08) across 75% of 24 models [2025-Andric-Do LLMs
Walk Their Talk]; PVQ-40 self-report correlates only **r=0.32** with scenario behavior (0.41 in humans)
[2026-Huang-VALACT]. The sharpest form is the speciesism split — models classify **86%** of statements
as speciesist but judge only **34%** morally wrong: "the problem is evaluative rather than epistemic"
[2025-Jotautaite-SpeciesismBench].

**Fragility.** Judgments flip under morally-irrelevant perturbation: POV shifts flip **24.3%**, surface
edits **7.5%**, protocol agreement only **67.6%** [2026-vanNuenen-Fragility of Moral Judgment]; political
self-ID reverses **99.6% conservative → 99.3% liberal** on answer-order alone [2025-Oh]; only 75.9%
paraphrase agreement in multilingual trolley [2024-Jin]. Yes↔No and action↔omission reframings flip
LLM decisions far more than humans (**45% vs 5%** gap) [2025-Cheung].

**Social-pressure and multi-agent dynamics.** Moral persuasion flips **~50%** of high-ambiguity
decisions (CAL 0.49 vs 0.06 control) [2024-Huang-Moral Persuasion]; Chinese-language models flip
54–69% post-debate vs English 1–8% [2024-Liu-Evaluating Moral Beliefs]; multi-agent groups show a
**Utilitarian Boost (β=0.31)** confined to personal dilemmas — opposite the human pattern, arising from
interaction not reflection [2025-Keshmirian-Many LLMs Are More Utilitarian Than One]; injected Ekman
emotions shift ethics divergently, and "all tested models fail to show consistent emotional alignment"
[2024-Mozikov-EAI]; GPT is inertial synchronously (OR 8.27) but conformist round-robin
[2025-Sachdeva-Deliberative Dynamics]. Sycophancy is directionally asymmetric (right→wrong flips exceed
the reverse) in VLMs [2026-MoralSycophancy-VLMs].

---

## 5. The process-vs-content frontier

The organizing insight of the whole corpus is a split between **content** (what a model endorses) and
**process** (how, when, and why a judgment forms). RLHF has homogenized content into the six signatures,
so content instruments converge (r=−0.83). Process manipulations discriminate.

The pivotal empirical result is **MP-DP**, a custom dual-process protocol manipulating reasoning mode
(zero-shot vs CoT) on personal/impersonal dilemmas. It was **the only battery instrument that cleanly
separated a model**: Haiku showed a CoT effect of **+0.125 / +25pp** while all 8 other models showed
**0.000**, giving **CV = 3.00 — ~93× the mean top-tier CV**. Not psychometrically polished, but it
probes a dimension RLHF does not homogenize. Corroborating process signals include the pre- vs post-hoc
reasoning asymmetry (pre-decision CoT is more deontological than post-hoc explanation, CDGAP −0.178
[2025-Samway]); reasoning-mode toggling raising abstract moral-stage scores while *increasing* jailbreak
vulnerability (0.68→0.89) — a capability-safety paradox [2025-Jiang]; and visual distraction triggering
System-1 processing that bypasses text safety [2026-PKU-Visual Distraction]. MoReBench demonstrates that
scoring *reasoning traces* (23,018 signed, weighted, atomic rubric criteria) is uncorrelated with math/
code/general benchmarks (r∈[−0.245, 0.216]) — it measures something genuinely new [2025-Chiu-MoReBench].

**Interpretability evidence for internal moral structure.** Behavior is not pure surface mimicry: moral
representations are sparse, localizable, and causally steerable. ValueLocate found **<0.4%** of neurons
value-related near layer 15 [2025-Su]; foundations appear as distinct linear directions, foundation-
specifically steerable (Care β=0.239; Authority ~5.7× gain under micro-steering) [2026-Yu-Tracing Moral
Foundations]; Goel localized **45/256 neurons (17.6%)** as a causal moral-scoring circuit [2026-Goel];
Hu recovers linearly-separable, partly cross-lingual foundation directions at layer 17 (65.6%) [2026-Hu].
Interpretability papers agree structure is sparse and localizable but disagree on depth (Su ~15; Yu
late-crystallizing; Hu layer 17). This layer is what lets a designer confirm that a behavioral score
reflects an internal construct rather than a fluent guess — but note it is single-model and has no
cross-model causal validation of any behavioral benchmark yet.

---

## 6. Open problems

- **The dual-process and moral-identity voids.** The two highest-citation process theories have zero
  usable instruments, and they sit exactly where discrimination lives. The MP-DP result suggests the
  dual-process gap is the single most promising target in the entire corpus.
- **The purity/sanctity floor.** All models floor at ~1.0; ~5 billion people organize moral life partly
  around purity/sanctity/divine obligation, and no instrument engages this axis meaningfully. It is
  unclear whether the floor is a genuine value gap, a refusal artifact, or a WEIRD annotation artifact.
- **Motivation is unmeasured.** No benchmark evaluates whether moral outputs are integrated into a
  self-consistent agency (the moral-identity question) — arguably *more* revealing for systems
  simulating a self.
- **Agentic / embodied moral competence.** Only 3–4% of surveyed work is interactive [2025-Snoswell];
  models beat humans on pre-packaged vignettes but fall below when identifying salient features amid
  noise (β=−0.35) [2025-Kilov]; sensitivity and value-of-information are essentially untested.
- **No established construct validity for any human instrument on LLMs.** Invariance is never
  demonstrated; the right scoring target when humans are themselves 10–18% unstable and structurally
  disagree remains unsettled (distributional targets, coherence axioms, and reasoning rubrics are all
  proposed but none is shown to predict real-world moral behavior).
- **Non-Western scoring without WEIRD reliability assumptions.** Afro-relational trust, phronesis, and
  Maqasid frameworks are proposed but not operationalized with validated keys.

---

## 7. Annotated bibliography (key papers)

1. **[2025-Jiao-LLM Ethics Benchmark]** — Highest-composite instrument (81.3); three-dimensional MFQ +
   WVS + standardized-dilemma system with population norms and open code (*Nature Sci. Reports*).
2. **[2018-Awad-The Moral Machine experiment]** — >40M trolley decisions from 233 countries; the field's
   largest human baseline, yet returns CV=0.000 across 9 models (memorized, not reasoned).
3. **[2024-Jin-Language Model Alignment in Multilingual Trolley]** — MultiTP; multilingual trolley
   battery (79.17) with only 75.9% paraphrase agreement, exposing cross-lingual fragility.
4. **[2024-Lee-KorNAT]** — Korean national-alignment benchmark (69.0); the escape-hatch proof that the
   cultural cliff is infrastructure, not culture.
5. **[2021-Lourie-Scruples]** — Distributional labels (vote distribution as target) + BEST oracle (human
   F1 0.490 < oracle 0.707); the canonical answer to "no single correct answer."
6. **[2015-Clifford-Moral Foundations Vignettes]** — Psychometric gold standard for item construction:
   reading-level control, two-stage validation ladder, non-moral control catching over-pathologizing.
7. **[2020-Hoover-Moral Foundations Twitter Corpus]** — 35,108 expert-annotated tweets (MFTC); the
   corpus asset behind MFT dominance; κ 0.27 rescued to PABAK 0.62–0.91 (disagreement as signal).
8. **[2024-Nunes-Conscience Conflict]** — Within-scale reliability human-like (MFV α 0.91) but cross-
   abstraction coherence collapses (R²<0.08 vs 0.17–0.38) — the core transfer-failure demonstration.
9. **[2024-Abdulhai-Moral Foundations of LLMs]** — MFQ maps LLMs nearest conservatives, but RLHF
   *widens* the human gap; foundational for the "RLHF grows the tilt" claim.
10. **[2024-Kirgis-Differences in Moral Foundations of LLMs]** — All six providers diverge from US
    baseline; more capable/recent models cluster *further* from human baseline in PCA space.
11. **[2025-Oh-Robustness of Large Language Models in Moral Judgements]** — 99–100% uniformity on 6/14
    Many Labs 2 studies (d=9.25 vs human 0.78); answer-order reversal flips political self-ID 99.6→99.3%.
12. **[2024-Almeida-Exploring the Psychology of LLMs Moral Reasoning]** — Documents the correct-answer
    effect: less variance than humans with inflated effect sizes.
13. **[2025-Cheung-LLMs Amplified Cognitive Biases Moral]** — Base-vs-instruct-vs-tuned causal design
    isolating RLHF; 45% vs 5% flip under logically-equivalent reframing; the validity gold standard.
14. **[2026-vanNuenen-Fragility of Moral Judgment]** — POV flips 24.3%, surface edits 7.5%, protocol
    agreement 67.6% — the fragility reference.
15. **[2025-Andric-Do LLMs Walk Their Talk]** — +11.9pp self-report↔behavior altruism gap (d=1.08); IAT
    fails to predict behavior (r=.22, ns); the knowing-doing benchmark.
16. **[2026-Huang-Knowing But Not Doing (VALACT)]** — PVQ-40 self-report↔scenario r=0.32; cross-model
    agreement r≈0.99–1.00; quantifies both convergence and the say-do gap.
17. **[2025-Jotautaite-SpeciesismBench]** — 86%-recognize / 34%-condemn split; "evaluative rather than
    epistemic" — the cleanest recognition-vs-evaluation dissociation.
18. **[2025-Chiu-MoReBench]** — 23,018 signed/weighted atomic rubric criteria on reasoning traces;
    uncorrelated with math/code (r∈[−0.245,0.216]); the strongest process-scoring design + contamination
    split.
19. **[2025-Samway-Are Language Models Consequentialist or Deontological]** — Reason-then-Decide vs
    Decide-then-Reason; pre-decision CoT more deontological than post-hoc (CDGAP −0.178).
20. **[2023-Nie-MoCa]** — AMCE factor decomposition shows LLMs weight factors unlike humans despite
    similar aggregate agreement; non-monotonic in scale.
21. **[2024-Khandelwal-Multilingual Defining Issues Test]** — DIT P-scores drop 23.9–46.7% EN→Hindi/
    Swahili (Hindi at random) — the cross-lingual difficulty reservoir.
22. **[2025-Keshmirian-Many LLMs Are More Utilitarian Than One]** — Multi-agent Utilitarian Boost
    (β=0.31) confined to personal dilemmas; a distortion static single-agent benchmarks miss.
23. **[2026-Yu-Tracing Moral Foundations in LLMs]** — Foundations as distinct steerable linear
    directions (Care β=0.239; Authority ~5.7× micro-steering gain); RLHF collapses them into a compliance
    cluster — the interpretability anchor.
24. **[2024-Hancox-Li-Is ETHICS about ethics]** — 19% expert–crowd disagreement on utilitarianism pairs;
    18% of deontology prompts solvable by physical-impossibility knowledge alone — the construct-validity
    audit / anti-pattern.
25. **[2025-Snoswell-Beyond Verdicts LLM Moral Competence]** — 69-paper survey: 96% static datasets, 3%
    interactive, only 4% test whether a model can flag needing more information — the agentic-competence
    gap.
