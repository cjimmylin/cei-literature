# 04 — Saturation, Difficulty, and Discrimination

> **CEI COOKBOOK · 00-KNOWLEDGEBASE.** Fable-authored (2026-07-05). Primary evidence:
> `20260705-saturation-discrimination-dossier.md` (~114 cards) cross-checked against contamination and
> agentic dossiers. `[stem]` = evidence card. **The problem this doc solves:** the user's core requirement
> — benchmarks that are difficult, unsaturated, and discriminative, and that stay that way.

---

## 1. The saturation landscape (why most values benchmarks are dead)

- Frontier labs have *retired* their single-turn safety evals: OpenAI's disallowed-content eval sits at
  ~0.996 and is "no longer a useful signal" (production multi-turn: 0.692) [OpenAI-gpt-oss]; Anthropic
  reports 99.29–99.78% harmless single-turn and moved to 15-turn suites [Anthropic-Claude_Opus_4.5];
  Google calls saturation "accelerating faster than new benchmarks can be created"
  [Google DeepMind-Gemini_2.5]. Academic corollaries: ETHICS commonsense at 89.3% few-shot
  [2023-Wang-DecodingTrust]; GPT-4 ~98% on ambiguous BBQ [2025-Griffiths]; religious-bias score literally
  0% after debiasing [2025-Ajwad Abrar]. Of 102 safety benchmarks published since 2018, only 12 are
  still used on SOTA models [2024-Kaiyom-HELM Safety].
- **Saturation is almost never solved alignment.** It is (a) format artifact — change the probe and
  headroom reappears (Law 3 in doc 01); (b) shortcut exploitation — WinoBias is semantically solvable
  [2025-Wang-UCerF], slur-keyword items are lexically solvable [2021-Röttger-HateCheck]; (c) leakage —
  the "evaluation chronoeffect" [2025-Jiang-Raising the Bar]; or (d) incapacity masquerading as
  cleanliness — a model that can't read Thai shows "no Thai bias" [2025-Zhou]. Diagnose which before
  concluding anything.

## 2. Where durable headroom lives (the difficulty reservoirs, ranked by evidence strength)

1. **Ambiguity / underspecification.** Disambiguated items ceiling; ambiguous items discriminate and
   *bias increases with capability* on them (UnifiedQA: ~77% of ambiguous-item errors align with
   stereotype) [2022-Parrish-BBQ; 2024-Neplenbroek-MBBQ]. Score abstention as the aligned answer.
   Stratify by measured human consensus; the grey zone (~0.5 consensus) is where models diverge from
   humans most [2025-Russo].
2. **Applied reasoning over recognition.** The two-tier drop is the headline: NurValues Easy >90% vs
   Hard 32.29 (−56 pts) [2025-Yao-NurValues]; MedEthicsQA MCQ 91.1% vs open-ended 37.0%
   [2025-Wei-MedEthicsQA]; norm *attribution* (which norm was violated) floors models that pass binary
   judgment (66.6/42.6 vs ~88) [2025-Lin-MORALISE].
3. **Implicit measures.** IAT-style association probes expose bias in models that pass every explicit
   test (t(33,599)=76.39; predicts discriminatory decisions OR≈2.68) [2025-Bai; 2025-Griffiths].
   Implicit sub-labels floor frontier models (F1=0.00 on symbolization spans [2025-Seker-HATECAT-TR]).
4. **Multi-turn accumulation & pressure.** Bias rises monotonically with turns (GPT-4 56.67% on
   FairMT-1K) [2025-Fan-FairMT]; 70.19% of cross-domain memory interactions increase bias [2026-Ma-DIB];
   escalation defeats single-shot ceilings [2025-Wu-Staircase; 2025-Zhang-CValues+].
5. **Cultural / low-resource / dialect localization.** Tamil near-zero for all models
   [2024-Ng-SGHateCheck]; code-mixing floors at 0.0% [2022-Das-HateCheckHIn]; culturally-grounded
   generation drops AUPRC 36.4 points [2025-Ngui-SEA-SafeguardBench].
6. **Consistency/coherence under logical constraint.** Contradiction-check ECI clusters models
   0.567–0.708, none near 1.0 [2025-Zhu-TrolleyBench]; GARP-style rationality: 2/39 models pass at 1%
   [2024-Seror]. Judge-free and saturation-resistant *now* (longevity untested — flag as risk).
7. **Incentive conflict.** No model is consistently moral when payoffs oppose morality (7.9%–76.3%
   spread; game type explains R²=0.87) [2025-Backmann-MORALSIM] — the largest inter-model spreads in
   the corpus (doc 06).

## 3. Difficulty engineering methods (how to build hard items on purpose)

| Method | Mechanism | Evidence | Cost |
|---|---|---|---|
| Adversarial filtration | keep highest-loss items from an ensemble | ETHICS Hard <50% vs 71% [2021-Hendrycks] | needs pilot models |
| Cross-model hardest-item distillation | keep items most models get wrong | 10K→1K raises exposed bias 11→57% [2025-Fan-FairMT] | ~5 pilot models |
| Attack-success gating | keep only prompts that break ≥1 model | Flames: best model 63.77% harmless [2023-Huang] | red-team loop |
| Weak-model pruning | drop items all weak models pass | [2025-Wei-MedEthicsQA; 2024-Zhang-SafetyBench] | cheap |
| IRT-2PL adaptive generation | fit difficulty/discrimination, generate at ability frontier | ~150 items/model, concurrent validity 0.8897 [2025-Jiang-Raising the Bar] | psychometric tooling |
| Cognitive-load rewriting | re-embed saturated items in dialogues/stories | 97.4→65.3 [2025-Zhang-CValues+] | LLM-assisted, cheap |
| Human-ambiguity targeting | select items by judged ambiguity | SynthBias reshuffles ranks (3rd→8th) [2025-Wang-UCerF] | human ratings |
| Graded corruption / severity ladders | parametric difficulty knobs | corruption intensities 1–10 [2023-Lee-VisAlign] | design-time |
| Genetic-algorithm middle-sampling | oversample the contested band | 150 from 62,612 candidates [2026-Li-PluriHarms] | fitness data |

**Open problem worth publishing on:** no head-to-head comparison exists of these difficulty currencies
(IRT vs highest-loss vs human-ambiguity vs cross-model error) for durability-per-item — a new benchmark
that runs this comparison internally would make a methods contribution by itself (saturation dossier §5.1).

## 4. Discrimination engineering (making scores separate models)

- **Design the null point**: cell-balanced construction so a competent unbiased system lands on a known
  value (50% CrowS ideal; bias metrics bounded by accuracy so a perfect model is provably unbiased
  [2024-Jin-KoBBQ]).
- **Prove separation statistically**: inter-model spread with bootstrap CIs/McNemar/ANOVA and multiple
  seeds; NurValues Hard separates 91.7% of model pairs at p<0.001 where Easy separates almost none
  [2025-Yao-NurValues]. A benchmark paper without pairwise-separation stats is unfinished.
- **Metric choice matters under imbalance**: macro-F1/worst-group discriminate (0.500–0.837) where
  accuracy compresses (0.927–0.951) [2025-Do-ViToSA]; publish the majority-class baseline (a dummy
  beats GPT-3.5 on BanTH [2025-Ishmam]).
- **Flag dead items**: >99% uniform responses across models, per-condition SD≈0, or answer-order
  sensitivity → remove or rewrite [2024-Almeida; 2025-Oh].
- **Confidence×correctness scoring**: rank confidently-wrong < uncertain < confidently-right; UCerF
  re-ranks models Equalized Odds cannot (5th→8th) [2025-Wang-UCerF].

## 5. Keeping it hard: anti-saturation lifecycle (see doc 05 for contamination mechanics)

- Two-tier release: canaried public set + private rolling holdout (only private evaluators score >50 on
  longevity; ETHICS/BBQ = 0 [2025-McGregor-BenchRisk]).
- Refresh triggers: capability-triggered re-evaluation (new frontier model → re-run separation stats);
  retire tiers that stop separating; publish regeneration templates so the community can mint fresh
  items to the same spec.
- Hedge with saturation-resistant metric families (consistency/coherence, implicit probes, incentive
  games) alongside accuracy metrics.
- **The "10% fine-tune" probe**: if fine-tuning on 10% of your benchmark reaches parity with SOTA, your
  items share exploitable surface structure [2025-Machlovi].

## 6. Design contract for a "hard, unsaturated, discriminative" claim

To claim these properties in a paper, show ALL of:
1. Best frontier model ≤~70% of ceiling on the hard tier, with the easy-tier drop reported
   [2025-Lin-MORALISE pattern].
2. Pairwise model separation stats (≥90% of pairs at p<0.01 on the hard tier) [2025-Yao-NurValues pattern].
3. Capability-correlation <40% (Law 1) [2024-Ren-Safetywashing].
4. Human ceiling explicitly measured and models placed relative to it, with headroom quantified.
5. Shortcut audit: lexical baseline ≈ chance; 10%-fine-tune probe fails to reach parity.
6. A named difficulty reservoir (§2) with a refresh mechanism (§5) — difficulty that will survive two
   model generations, not just today's.

**Drill-down:** `20260705-saturation-discrimination-dossier.md` §2 (decision table), §3 (the
scale-vs-bias contradiction and its reconciliation), §4 (GETA, Hendrycks-ETHICS, UCerF, TRIAGE,
FairMT exemplars).
