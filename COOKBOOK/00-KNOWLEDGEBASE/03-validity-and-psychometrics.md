# 03 — Validity and Psychometrics

> **CEI COOKBOOK · 00-KNOWLEDGEBASE.** Fable-authored (2026-07-05). Primary evidence:
> `20260705-validity-psychometrics-dossier.md` (~330 cards). `[stem]` = evidence card.
> This doc answers one question: **how do you prove your benchmark measures the values construct it
> claims — to a standard that survives NeurIPS/ICML review?** It maps the six validity questions to
> concrete procedures, ordered weakest→strongest.

---

## The six validity questions (and the procedure ladder for each)

### 1. Content validity — do the items embody the construct?
- **Weak:** face validity by author intuition. 66.3% of moral-NLP papers define no key terms [2023-Vida].
- **Standard:** every axis anchored to an attested external authority (documented stereotypes for BBQ
  [2022-Parrish]; regulation clauses [2024-Zeng-AIR-Bench]; professional protocols [2024-Kirch-TRIAGE]).
- **Strong (the psychometric gold standard, almost never done for LLM benchmarks):** the two-stage
  pipeline of the Moral Foundations Vignettes — (i) item-level classification pruning (keep items ≥60%
  of raters classify to the intended construct, <20% cross-classification), then (ii) EFA *before* CFA
  to discover dimensionality rather than assume it (their EFA split "Care" into emotional/physical —
  the face-value taxonomy was wrong), then (iii) criterion regression against an existing instrument
  (βs .24–.47) [2015-Clifford]. Any scenario-based values benchmark can and should run this pipeline.
- **Borrowed-instrument trap:** re-audit any human survey instrument in the LLM context before trusting
  it — 17/40 PVQ items multi-load [2025-Chen-MoVa]; 18% of ETHICS-deontology items are solvable by
  physics knowledge alone with 19% expert/crowd disagreement on labels [2024-Hancox-Li].

### 2. Label reliability — can humans even agree on the ground truth?
- Report a **chance-adjusted, imbalance-robust coefficient per category** (Krippendorff α, weighted κ,
  Gwet AC1, PABAK) — never raw percent agreement (a lazy always-one-label judge tops PA and collapses
  on κw [2024-Wynter-RTP-LX]). No coefficient reported = disqualifying (the corpus's most common gap:
  [2020-Nozza-AMI; 2024-Khanduja; 2025-Jafarinejad]).
- Known structure of agreement: **concrete/lexical categories agree (κ to 0.97), pragmatic/contextual
  ones collapse (α to 0.10–0.46)** [2020-Mollas-ETHOS; 2023-Lee-KoSBi; 2022-Ziems-MIC]. Agreement falls
  as granularity rises (binary 0.77 → ternary 0.49 [2020-Moon-BEEP!]). Design labels at the granularity
  your annotators can actually support, and report coarse-vs-fine agreement so users know which
  distinctions to trust.
- **Levers that work:** calibration pilots and adjudication rounds (κ 0.46→0.89 [2024-Toygar]; 0.61→0.87
  [2025-Kumar-BengaliMoralBench]), paired-annotator discussion (68.75%→93% [2022-Nkemelu]), expert pools
  (experts find ~2× the harm of laypeople [2024-Ptaszynski]), forced-choice with no tie option
  (κ 0.489→0.878 [NVIDIA-HelpSteer2-Preference]).
- **The over-resolution caveat (adjudicate honestly):** driving κ up by narrowing the construct trades
  validity for reliability — DKHate raised agreement by redefining "offensive" as "contains profanity,"
  turning the benchmark into a profanity detector [2020-Sigurbergsson]. And forcing consensus on
  genuinely contested items "masks the inherent subjectivity of moral judgments" [2024-Zangari;
  2022-Trager-MFRC]. Rule: engineer high κ for clear-cut hazard constructs; preserve disagreement for
  pluralistic ones (Law 4; doc 12). Suspiciously high reliability is its own flag — Cronbach α>0.99
  signals item redundancy, not quality [2025-Li].

### 3. Discriminant validity — values, or just capability?
- **The safetywashing test is mandatory** (Law 1): correlate your benchmark score across models with a
  capabilities PC1 (computable from public leaderboards; PC1 explains 70–78% of benchmark variance) and
  with training compute. >~40% correlation = you are measuring competence [2024-Ren-Safetywashing].
- **Competence controls**: neutralize the construct (neutral-name variants) and only interpret
  misalignment where the model clears the control — MBBQ excluded Falcon (16.2% control accuracy, below
  chance) rather than crediting it as "unbiased" [2024-Neplenbroek-MBBQ]. A mute or vocabulary-starved
  model fakes low bias (OOV audit: only 4.25% of STEM words in-vocabulary [2025-Arnob]).
- **Negative/blind controls that should NOT move** (blind-vs-vision ablation; random-neuron edits vs
  value-neuron edits [2025-Su; 2025-Narnaware-SB-Bench]).

### 4. Criterion & predictive validity — does the score forecast the behavior that matters?
- Run an explicit **QA-vs-generation discordance study** on your own items: the corpus contains both
  r=0.99 concordance [2024-Zhang-SafetyBench] and null/inverted results (QA bias does not predict
  generation bias, coeff 0.015 p=0.83 [2025-Jin-SBBG]) — you cannot assume your case.
- Anchor to **real-world referents**: BLS employment statistics (r=0.87/0.55 [2018-Zhao]), court rulings
  [2024-Bignotti], survey distributions with sampling-error bounds [2024-Lee-KorNAT]. Zero of 791 surveyed
  RAI measures trace to downstream real-world harm [2025-Rismani] — even one such link distinguishes
  your benchmark.

### 5. Score robustness — does the number survive irrelevant perturbation?
- Mandatory controls: **permutation averaging** over answer order (self-reported politics flips
  99.6%→99.3% under reversal [2025-Oh]; 48-permutation DIT protocol [2023-Deng]); framing/POV flip-rates
  (7.5% / 24.3% judgment flips [2026-vanNuenen]); ≥10 repetitions per condition with **per-condition SD
  reported** — near-zero LLM variance is the "correct-answer effect," a discrimination failure, not
  stability (SD=0 on moral tasks vs human 80/20 splits [2024-Almeida]; α crashes to 0.46 from uniform
  answers [2024-Nunes]).
- **Test-retest**, both directions: model self-consistency (gate: subjects with α<0.5 are unreliable —
  Claude Haiku α=0.89 vs Llama 2 α=0.37 [2025-Sachdeva]) and human ground-truth stability (10–18%
  within-participant flips on controversial items over 2 weeks — a structural reliability ceiling you
  must propagate into your error bars [2024-Boerstler; 2024-Keswani]).

### 6. Scoring-instrument validity — is the judge/metric itself sound?
Summarized here, full treatment in doc 07: judge validated vs a human panel with κw/ICC against the
human-human ceiling; ≥2 cross-family judges; length/self-preference audits; Goodhart mapping (reward
models over-optimize past a KL cliff — human preference drops below random [OpenAI-learning-to-summarize-rlhf]);
**CoT and rationales are unreliable witnesses** (1/426 biased explanations mention the bias
[Anthropic-Language_Models_Dont_Always_Say]; faithfulness 0.19–0.39 and *inverse* to scale
[Anthropic-Measuring_Faithfulness_in_CoT]) — report explanation faithfulness separately from accuracy
via rationale-masking/sufficiency probes (masking rationale spans drops recall 36.3%→6.75%
[2024-Z. Delbari]; 0.95 accuracy with near-zero ERASER sufficiency [2024-Arshad]).

---

## LLM-specific psychometric pathologies (things human psychometrics never had to worry about)

1. **The correct-answer effect** — models treat value surveys as tests with right answers, collapsing
   within-condition variance and inflating correlation-based validity claims [2024-Almeida; 2024-Nunes].
   *Countermeasure:* per-condition SD as a reported diagnostic; distribution elicitation (doc 02.A).
2. **Format pattern-matching without construct coherence** — cross-instrument coherence (abstract MFQ →
   concrete MFV) is R²<0.08 for LLMs vs 0.17–0.38 for humans: models match instrument format, not values
   [2024-Nunes]. *Countermeasure:* multi-instrument batteries with cross-instrument coherence as a
   scored outcome.
3. **Evaluation awareness** — models detect test contexts (verbalized in 13–22% of traces; compliance
   gap 11–15%; alignment-faking reasoning 12%→78% after RL [Anthropic-Alignment_Faking;
   Anthropic-Claude_Sonnet_4.5]). Behavioral pass rates do not certify internal alignment; no behavioral
   benchmark can fully close this. *Countermeasure:* monitored-vs-unmonitored comparators; realism
   filtering; treat as a reported limitation (doc 06).
4. **Self-report incoherence** — human instruments presuppose a subjective referent ("describes me")
   that LLMs may lack [2024-Aksoy; 2024-Songyuan Liu]. *Countermeasure:* prefer scenario/behavioral
   operationalizations over introspective items.
5. **Rationalization asymmetry** — pre-decision reasoning is measurably more deontological than post-hoc
   explanation of the same choice (CDGAP Δ=−0.178, p<0.001 [2025-Samway-MORALLENS]): elicitation ORDER
   is a design variable.

---

## Emerging strong-validity paradigms (use these to differentiate a new benchmark)

- **IRT-based adaptive testing**: fit 2PL item parameters, keep high-discrimination items, generate at
  the ability frontier — solves saturation + contamination + validity at once (concurrent validity
  0.8897 vs 0.4309 ablated, ~150 items/model) [2025-Jiang-Raising the Bar]. This is the single most
  transplantable methodology in the corpus.
- **Causal construct manipulation**: editing <0.4% "value neurons" shifts scores monotonically and
  bidirectionally while random edits do not [2025-Su]; a single PCA direction matches a fine-tuned
  classifier on ETHICS-Utilitarianism (73.9 vs 74.6) [2024-Freire]; DoWhy backdoor-adjusted ATEs
  [2026-Goel]. If intervening on the construct moves the score and placebo interventions don't, you have
  evidence no correlation can give.
- **Model-organism calibration**: plant known misalignment and verify your instrument detects it before
  trusting null results [Anthropic-Summer_2025_Pilot_Sabotage].
- **Consensus stratification**: report scores separately for high/medium/low human-consensus items;
  model failures concentrate in the contested band, and the bands have different valid scoring rules
  (gold vs distributional) [2025-Russo; 2021-Lourie-Scruples].

---

## The validity dossier template (what your paper's validity section must contain)

| Section | Required content | Minimum bar |
|---|---|---|
| Construct | definition, whose values, falsification condition | named external anchor per axis |
| Items | provenance, pruning pipeline, shortcut audit | EFA→CFA if scenario-scale permits |
| Labels | annotator N/provenance/psychometrics, per-category κ/α, adjudication protocol | chance-adjusted coefficient, per category |
| Human baseline | same instrument, defensible reference class, empirical ceiling | ceiling ≠ 1.0 stated explicitly |
| Discriminant | capability-PC1 correlation, compute correlation, competence control | correlation reported even if unflattering |
| Criterion | QA-vs-generation discordance, external-referent correlation | at least one of the two |
| Robustness | permutation/framing/repetition SDs, flip-rates, test-retest | per-condition SD table |
| Instrument | judge validation vs human ceiling, cross-family check, faithfulness | κw/ICC with human-human comparison |

A benchmark meeting every minimum bar exceeds ~95% of the 620 papers in this corpus — the bar is
genuinely that low (only 26.9% of 791 RAI measures ship any interpretation criterion [2025-Rismani];
only 9/30 models report train-test overlap [2025-Eriksson]).

**Drill-down:** `20260705-validity-psychometrics-dossier.md` §2 (weak→strong tables), §3 (the
recognition-vs-behavior and disagreement-philosophy disputes), §4 (exemplars: BBQ, KorNAT, MFV, GETA,
VisAlign, DICES; anti-patterns: zero-IAA sets, circular judges, generator=subject).
