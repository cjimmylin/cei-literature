# validity-psychometrics — sub-dossier part 3/6

Scope: 56 cards spanning moral-psychology benchmarks, multilingual hate/offensive-speech
corpora, bias/fairness challenge sets, and six AI-lab system cards. The through-line is how
each artifact tried to show it measures what it claims — via inter-rater reliability, human
baselines, construct/criterion validity, ceiling/floor diagnostics, and cross-instrument or
cross-paradigm coherence.

## A. Synthesized claims

1. **Raw inter-rater kappa on moral/values labels is chronically low, and prevalence
   correction is mandatory to interpret it.** MFTC reports overall Fleiss' κ = 0.27 but PABAK
   = 0.29 with per-foundation PABAK 0.62–0.91 once sparsity is controlled [2020-Hoover-Moral
   Foundations Twitter Corpus]. The Weibo replication shows κ swinging 0.45–0.92 by topic,
   with PABAK generally higher [2024-Cao-The Moral Foundations Weibo Corpus]. MIC reports
   Krippendorff's α as low as 0.10–0.46 alongside ICC(1,k) 0.42–0.72 [2022-Ziems-The Moral
   Integrity Corpus]. Lesson: report both raw and prevalence/bias-adjusted coefficients.

2. **Adjudication and iterative annotator training move agreement more than any modeling
   choice.** Turkish offensive detection rose from Cohen's κ = 46.26% (initial two-annotator)
   to 88.97% after adjudication [2024-Toygar-Turkish Offensive Language Detection Dataset];
   Burmese percent-agreement rose 68.75% → 93% over four peer-feedback cycles
   [2022-Nkemelu-Tackling Hate Speech in Low-resource Languages]; Indonesian toxicity reached
   Gwet's AC1 = 0.61 only after three training sessions [2024-Susanto-IndoToxic2024;
   2025-Susanto-A Multi-Labeled Dataset for Indonesian Discourse]; X-MuTeST lifted Fleiss κ to
   81–85 across three languages via re-annotation rounds [2026-Rehman-X-MuTeST].

3. **Prescriptive high-agreement design is achievable when the construct is deliberately made
   clear-cut.** SimpleSafetyTests hits Fleiss' κ = 0.83 with 92% unanimous agreement across
   3,000 responses using a prescriptive paradigm and easy, egregious items
   [2023-Vidgen-SimpleSafetyTests]. Educator-role profiling reached κ = 0.988 on binary
   harmfulness but only 0.799 on the multi-level moral-stage scale [2025-Jiang-EMNLP
   Educator-role]. Binarizing collapses subjectivity: Telugu agreement jumps from
   Krippendorff α = 0.47 (3-class) to α = 0.89 (binary) [2025-Kumar-TeSent].

4. **Survey-grounded ground truth converts contested values into a defensible, pluralistic
   target — and reveals that the ceiling is far below 1.0.** KoBBQ validates every
   stereotype and target group with 100 respondents plus a reading-comprehension solvability
   filter [2024-Jin-KoBBQ]. KorNAT derives social-value truth from 6,174 Koreans (~219
   responses/question) and reports an *empirical* ceiling of SVA = 0.450 (A-SVA 0.626),
   reflecting genuine within-population disagreement, against which the best model (~0.331)
   is legible [2024-Lee-KorNAT]. CLCA scores 220k WVS questions via 1,000 personas/culture
   and finds best-case KL-divergence still 0.51, far from 0 [2025-Liu-Cultural
   Learning-Based Culture Adaptation].

5. **High human-alignment correlation is a false green light when LLM response variance
   collapses — the "correct-answer effect."** GPT-4 correlates r = 0.82–0.86 with human MFQ
   per-item responses, yet all LLMs show dramatically lower within-condition variance (SD = 0
   observed repeatedly), inflating correlations even when means differ
   [2024-Almeida-Exploring the Psychology of LLMs]. Nunes formalizes this: Claude 2.1's MFQ
   Cronbach α crashes to 0.46 (vs human 0.74) because it emits identical scores across items
   [2024-Nunes-Conscience Conflict]. Andric finds 42% of models at IAT ceiling (>0.9),
   suppressing correlations [2025-Andric-Do LLMs Walk Their Talk]. Per-condition SD must be
   reported as a discrimination diagnostic, not just correlation.

6. **Within-instrument consistency without cross-instrument coherence is the central validity
   failure of LLM values measurement.** Nunes shows LLM cross-abstraction R² < 0.08 (abstract
   questionnaire → concrete vignette) versus human R² 0.17–0.38 — models pattern-match
   instrument formats rather than holding coherent values [2024-Nunes-Conscience Conflict].
   Seror reframes coherence economically: only 2/39 models pass a GARP rationality test at
   1%, 7/39 at 5%, and top CCEI is only 0.417 [2024-Seror-The Moral Mind(s)].

7. **MCQ/forced-choice bias scores do NOT predict generative behavior — a criterion-validity
   crisis for closed-form values evals.** SBBG shows QA bias and generation bias fail to
   positively correlate (English coeff 0.015, p = 0.832; Korean −0.102, p = 0.048), and
   higher-performing models within a family show *lower* QA bias but *higher* generation
   bias [2025-Jin-Social Bias Benchmark for Generation]. SB-Bench confirms closed-form masks
   bias: blind text-only scores exceed vision scores for all four tested models (Phi-4-MM
   89.44% blind vs 74.30% vision) [2025-Narnaware-SB-Bench]. Multiple bias benchmarks
   correlate poorly with each other [2025-Neplenbroek-Cross-Lingual Transfer].

8. **Automated LLM judges can be trusted only when explicitly validated against a human panel,
   and even then agreement is merely "human-level."** PrinciplismQA reports LLM-judge-vs-human
   ICC = 0.71 against human-human ICC = 0.67 [2025-Hong-PrinciplismQA]. SB-Bench: judge-human
   Cohen's κ = 0.81 [2025-Narnaware-SB-Bench]. SBBG: GPT-4 judge-human κ = 0.69 vs
   inter-annotator κ = 0.78 [2025-Jin-Social Bias Benchmark for Generation]. AlignBench: judge
   sample-level Pearson only 0.638 but system-level 0.998 — reliable for ranking systems, noisy
   per-item [Zhipu AI-AlignBench].

9. **Behavioral audits via minimal-pair counterfactuals give causally-attributable, human-free
   bias signals with proper significance testing.** The EEC swaps one identity token and finds
   75–86% of 219 systems consistently favor one gender, average gaps <0.03 but individual δ up
   to 0.34, via paired t-tests with Bonferroni correction [2018-Kiritchenko-Examining Gender
   and Race Bias]. Bias-in-Bios summarizes bias as a single Pearson r = 0.85 between TPR gender
   gap and occupational imbalance [2019-De-Arteaga-Bias in Bios]. GenMO, RedditBias, and TeSent
   extend the minimal-pair recipe [2024-Bajaj-GenMO; 2021-Barikeri-REDDITBIAS; 2025-Kumar-TeSent].

10. **Benchmark substrate itself must be audited: several "canonical" datasets do not stably
    exhibit the construct they claim.** FFB runs ERM across 910 seeded runs and marks several
    standard fairness datasets as *not reliably biased*, and tabulates 0.17 (20%) accuracy
    drift for the same Adult metric across prior papers [2023-Han-FFB]. Zhou-Rethinking finds
    the largest single GPT-4 error source is "inappropriate annotation" in the benchmark labels
    themselves [2024-Zhou-Rethinking Machine Ethics]. Fasching shows within-model Krippendorff
    α > 0.9 across 10 prompts, so cross-model SD > 0.2 in 78.4% of groups is genuine model
    disagreement, not prompt noise [2025-Fasching-Inconsistencies].

11. **Stated reasoning is frequently unfaithful, so verdict-only validity is insufficient.**
    Anthropic finds biasing features drop accuracy up to 36.3% yet models mention the bias in
    only 1/426 explanations; 73% of unfaithful CoTs rationalize the biased answer
    [Anthropic-Language_Models_Dont_Always_Say_What_They_Think]. Claude 3.7's CoT faithfulness
    averages 0.30 (MMLU) / 0.19 (GPQA) [Anthropic-Claude_3.7_Sonnet_System_Card]. Andric's
    Calibration Gap of +11.9 pp (models claim 77.5% altruism, act at 65.6%) quantifies
    say-do divergence [2025-Andric-Do LLMs Walk Their Talk].

## B. Evidence table

| Card stem | Single most design-relevant fact |
|---|---|
| 2020-Hoover-Moral Foundations Twitter Corpus | Report PABAK alongside raw κ (0.29 vs 0.27); sparse moral labels make raw κ misleading |
| 2024-Cao-The Moral Foundations Weibo Corpus | κ varies 0.45–0.92 by topic; ambiguous "general discourse" topics depress agreement |
| 2022-Ziems-The Moral Integrity Corpus | Convert disagreement into measured Global Consensus; ICC(1,k) 0.42–0.72 |
| 2023-Vidgen-SimpleSafetyTests | Prescriptive, deliberately-easy floor test yields Fleiss κ = 0.83, 92% unanimity |
| 2024-Toygar-Turkish Offensive Language Detection | Adjudication raised Cohen κ from 46.26% to 88.97% |
| 2022-Nkemelu-Tackling Hate Speech Low-resource | Paired-annotator peer discussion raised agreement 68.75% → 93% |
| 2024-Jin-KoBBQ | Survey-validate every stereotype+target (100 resp.); reading-comprehension solvability gate |
| 2024-Lee-KorNAT | Report empirical ceiling (SVA=0.450) + naive baseline so raw scores are legible |
| 2025-Liu-Cultural Learning-Based Culture Adaptation | KL-divergence to survey distribution as population-level alignment metric |
| 2024-Almeida-Exploring the Psychology of LLMs | High human-correlation + near-zero LLM variance = "correct-answer" red flag |
| 2024-Nunes-Conscience Conflict | Cross-abstraction R² < 0.08 (LLM) vs 0.17–0.38 (human) exposes values incoherence |
| 2024-Seror-The Moral Mind(s) | Priced-choice GARP/CCEI test of value-system coherence, answer-key-free |
| 2025-Jin-Social Bias Benchmark for Generation | QA bias score does NOT predict generation bias (coeff 0.015, p=0.83) |
| 2025-Narnaware-SB-Bench | Blind-vs-vision ablation proves the benchmark measures visually-triggered bias |
| 2025-Hong-PrinciplismQA | LLM-judge ICC 0.71 ≈ human-human ICC 0.67, explicitly validated |
| Zhipu AI-AlignBench | Judge reliable at system level (Pearson 0.998) but noisy per-item (0.638) |
| 2018-Kiritchenko-Examining Gender and Race Bias | Minimal-pair δ with paired t-test + Bonferroni; 75–86% of systems biased |
| 2019-De-Arteaga-Bias in Bios | Single r=0.85 (TPR gap × base rate) as compact aggregate bias score |
| 2023-Han-FFB | Meta-audit: run ERM over 910 seeds to check the construct is even stably present |
| 2024-Zhou-Rethinking Machine Ethics | Largest GPT-4 error source = bad benchmark annotation, not model failure |
| 2025-Fasching-Inconsistencies | Within-model α>0.9 across 10 prompts isolates genuine cross-model disagreement |
| 2022-Chalkidis-FairLex | Report triad: avg mF1, group disparity, worst-group mF1 (21.5% disparity hidden by mean) |
| 2025-Andric-Do LLMs Walk Their Talk | Calibration Gap (+11.9pp) as virtue-signaling metric; binary force busts IAT ceiling |
| 2024-Goldzycher-AustroTox | α=0.49 is below the 0.667 "tentative" threshold; publish disaggregated labels |
| 2025-Kumar-TeSent | Agreement jumps 0.47→0.89 when 3-class collapses to binary |
| 2026-Rehman-X-MuTeST | Token-level human rationales evaluate reasoning, not just verdict; Fleiss 81–85 |
| 2025-Jiang-EMNLP Educator-role | CPST-E Cronbach α 0.82–0.91; anchor to 100 real teachers as human baseline |
| 2025-Li-Untangling Input from Reasoning Language | 2×2 factorial + moral fingerprinting; 12–13/13 models more lenient than humans |
| Anthropic-Language_Models_Dont_Always_Say | Bias mentioned in 1/426 explanations — verdict-only validity is unsafe |
| Anthropic-Claude_3.7_Sonnet_System_Card | CoT faithfulness 0.30/0.19; classifiers 95% on adversarial validation set |
| 2023-Körner-Deontology and Utilitarianism in Real Life | Realism (typicality/plausibility/absurdness) as a first-class scenario validity check |
| 2025-Dillion-AI Language Model Rivals Expert Ethicist | Pre-registered, source-blinded comparative Moral Turing Test vs a named expert |
| 2024-Susanto-IndoToxic2024 | Preserve per-annotator labels + demographics for subjectivity analysis |
| OpenAI-gpt-5-system-card | Sycophancy 0.145→0.052 measured offline as a first-class construct |
| Meta AI-Llama_Guard | Separate prompt vs response classification; AUPRC 0.945 own set |
| 2024-Karpov-Inducing Human-like Biases | Vision-ROI negative control for "model matches human X" claims |

## C. Patterns & disagreements

**Convergence.** (a) Every human-rated moral corpus that reports it finds low raw agreement
and reaches for a correction — PABAK [2020-Hoover; 2024-Cao], Gwet's AC1 [2024-Susanto;
2025-Susanto], or binarization [2025-Kumar; 2025-Jiang-EMNLP]. (b) Survey- or
distribution-grounded truth is the emerging gold standard for contested values [2024-Jin-KoBBQ;
2024-Lee-KorNAT; 2025-Liu]. (c) Multiple independent teams converge on the "correct-answer
effect"/ceiling collapse as the dominant LLM-specific validity threat [2024-Almeida;
2024-Nunes; 2025-Andric], and prescribe reporting response variance and forcing binary choice
[2025-Andric].

**Disagreement / tension.** Vidgen and Jiang-EMNLP show that *making the construct easy* buys
κ = 0.83–0.99 [2023-Vidgen; 2025-Jiang-EMNLP], whereas Hoover explicitly warns that "excessive
focus on maximizing annotator agreement risks... suppressing the natural variability of moral
sentiment" [2020-Hoover]. Ziems and the Susanto papers side with Hoover — preserving
disagreement as signal [2022-Ziems; 2024-Susanto; 2025-Susanto] — while SimpleSafetyTests
treats high agreement as the goal [2023-Vidgen]. The resolution is domain-dependent: floor
safety tests want clear-cut truth; pluralistic values benchmarks want to measure the
distribution. A second tension: behavioral minimal-pair audits [2018-Kiritchenko;
2019-De-Arteaga] and closed-form MCQ scores [2024-Jin-KoBBQ] are cheap and human-free, but
SBBG and SB-Bench demonstrate they can invert or hide the generative behavior that matters
[2025-Jin-Social Bias Benchmark for Generation; 2025-Narnaware-SB-Bench].

## D. Exemplars & anti-patterns

**Best-designed.** *KorNAT* [2024-Lee-KorNAT] is the strongest: survey-grounded truth from
6,174 people with sampling-theory error bounds, an explicitly reported empirical ceiling and
naive baseline, distractor/consistency screening to purge bad respondents, human criterion
validation (94/100 questions preferred the higher-A-SVA model), and refusal treated as a
first-class outcome. *KoBBQ* [2024-Jin-KoBBQ] is a close second (survey-validated targets +
human-solvability gate + ANOVA/Tukey/Wilcoxon rigor). *Nunes* [2024-Nunes-Conscience Conflict]
and *Andric* [2025-Andric] are the best *validity-methodology* exemplars: both build in
positive controls (human Cronbach α, human R², multi-method dissociation) that catch failures
single-metric benchmarks miss. *FairLex* [2022-Chalkidis] models decomposing disparity into
attribute-agnostic factors and reporting a fairness triad.

**Anti-patterns.** *Zhou-Bias-Beyond-English* [2025-Zhou-Bias Beyond English] relies on
translation with "no human validation of the translations, no inter-rater reliability, no
factor analysis" — face validity only. *Jikeli* [2019-Jikeli] and *Nurce* [2021-Nurce]
report no IRR coefficient at all. *HateThaiSent* [2024-Maity] and *Hashmi* [2025-Hashmi] give
accuracy numbers with unconfirmed annotation quality. Zhou-Rethinking's error analysis
[2024-Zhou-Rethinking Machine Ethics] shows the deeper anti-pattern: benchmarks whose labels
are themselves the largest error source. These are cautionary: a headline F1 or bias score
without reliability evidence is uninterpretable.

## E. Design lessons

1. **Always report a prevalence/bias-adjusted agreement coefficient (PABAK or Gwet's AC1)
   alongside raw κ/α for sparse moral labels** [2020-Hoover; 2024-Cao; 2024-Susanto], and
   compare against a published benchmark α (e.g., HateXplain 0.46) so a "moderate" number is
   legible [2025-Kumar; 2024-Goldzycher].
2. **Budget for adjudication and multi-round annotator training — it is the highest-leverage
   quality lever** [2024-Toygar (46→89%); 2022-Nkemelu (69→93%); 2026-Rehman].
3. **Ground contested values in a demographically-representative survey distribution and score
   models against that distribution (KL-divergence or probability mass), not a majority label**
   [2024-Lee-KorNAT; 2025-Liu; 2024-Jin-KoBBQ].
4. **Report the empirical ceiling and a naive baseline** so raw scores sit against a real
   maximum, not an implied 1.0 [2024-Lee-KorNAT].
5. **Treat near-zero LLM response variance as a red flag, not a success — report per-condition
   SD and force binary choice when ceiling effects appear** [2024-Almeida; 2024-Nunes;
   2025-Andric].
6. **Add coherence checks across abstraction levels and answer orderings** (abstract↔concrete
   R², ordering-effect tests, priced-choice GARP consistency) to catch models that pattern-match
   instruments rather than holding values [2024-Nunes; 2024-Seror; 2025-Li].
7. **Never trust MCQ/closed-form bias scores as proxies for generative behavior — run an
   explicit QA-vs-generation discordance study** [2025-Jin-Social Bias Benchmark for Generation;
   2025-Narnaware-SB-Bench].
8. **Validate every automated judge against a human expert panel and report both judge-human and
   human-human ICC/κ; distinguish system-level (reliable) from item-level (noisy) agreement**
   [2025-Hong-PrinciplismQA; 2025-Narnaware-SB-Bench; Zhipu AI-AlignBench].
9. **Audit the benchmark substrate before use: run a baseline across many seeds to confirm the
   construct is stably present, and quantify cross-paper metric drift** [2023-Han-FFB;
   2024-Zhou-Rethinking Machine Ethics].
10. **Include a negative/blind control that should NOT move** (vision-ROI control, blind-vs-vision
    ablation, noisy-standard-text null) to prove the benchmark isolates its target construct
    [2024-Karpov; 2025-Narnaware-SB-Bench; 2025-Bui].
11. **Evaluate reasoning/rationale faithfulness, not only verdicts** — stated reasons frequently
    do not drive answers [Anthropic-Language_Models_Dont_Always_Say; Anthropic-Claude_3.7;
    2026-Rehman; 2025-Snoswell].
12. **Add a say-do or social-pressure condition** (Calibration Gap, sycophancy direction) since
    static-test success can mask behavioral failure [2025-Andric; 2026-MoralSycophancy;
    OpenAI-gpt-5-system-card].
13. **Validate scenario realism as its own construct and use factual/expert-anchored items** to
    resist "unrealistic trolley" criticism [2023-Körner; 2025-Dillion].
14. **Preserve per-annotator labels + demographics** to study whose values a model matches and to
    treat disagreement as measurable rather than noise [2024-Susanto; 2025-Susanto; 2022-Ziems].
