# Design 06 — CRUX: Value-Conflict Adjudication Under Uncertainty

> **CEI COOKBOOK · 20-DESIGNS.** Fable-authored (2026-07-05). Status: full design, pre-pilot.
> Build SECOND (its procedural generator is shared infrastructure for 01/05). Venue framing: ICML or
> NeurIPS D&B. Grounding: KB docs 01, 02, 04, 12; design-space + pluralism + saturation dossiers.

---

## 1. Motivation

Real assistant work is value *conflict*: helpfulness vs honesty, privacy vs utility, autonomy vs
protection, loyalty vs fairness — usually under missing information. The corpus shows: models flip
under MCQ↔open formats (protective values rank 1.7→4.5 [2025-Liu-ConflictScope]); preference
structures are non-transitive under escalation ("context-driven statistical imitation"
[2025-Wu-Staircase]); factor-weighting diverges from humans behind human-like aggregates (AMCE
[2023-Nie-MoCa]); determinism under genuine disagreement is itself misalignment (~0–6% indecision vs
17% human [2025-Dickerson]); and no existing instrument combines conflict adjudication with
consensus-stratified ground truth, coherence auditing, and contamination-proof generation. VAL-Bench
scores consistency but is refusal-gameable (ρ=0.91) [2025-Gupta]; DailyDilemmas profiles without
difficulty engineering; ConflictScope is single-turn and announced.

**CRUX measures HOW a model adjudicates value conflicts: its priority fingerprint, its coherence, its
calibration to human disagreement, and its sensitivity to the factors that should (and shouldn't)
move the decision.**

## 2. Construct definition (five scored axes)

- **CR — Conflict Recognition**: does the model identify that two legitimate values collide (vs
  flattening to one side or manufacturing a false resolution)? Includes value-of-information behavior:
  on underdetermined items, does it seek the decision-relevant fact (only 4% of the field tests this
  [2025-Snoswell])?
- **PF — Priority Fingerprint**: the model's revealed value-priority ordering across the conflict
  grid (a characterization output with CIs, not pass/fail) — including its stability across framings
  and stakes.
- **CO — Coherence**: transitivity and dominance-consistency across matched triads (GARP/CCEI-style,
  answer-key-free and contamination-resistant: only 2/39 models pass at 1% today [2024-Seror]);
  invariance to normatively-irrelevant edits and sensitivity to relevant ones (paired AMCE: the
  "wrong-factor movement" rate [2023-Nie]).
- **DC — Disagreement Calibration**: on contested items, distributional match to stratified human
  distributions (KL/JSD with oracle ceiling [2021-Lourie; 2024-Lee-KorNAT]) + calibrated use of
  explicit indecision/incomparability options (offering "these are incomparable" as a valid answer
  and testing whether models confabulate rankings [2024-Zhi-Xuan; 2025-Benavoli]).
- **PS — Pressure Stability**: does adjudication survive persuasion, authority pushback, and stakes
  escalation — distinguishing reason-responsive updating (good) from sycophantic capitulation (bad)
  via argument-quality-controlled challenges (links to Sketch S2 machinery).

## 3. Task design

### 3.1 The generator (shared infrastructure)
Scenarios compile from a typed factorial spec: {value-pair (10 pairs from 5 core values) ×
stakes (minor/serious/severe) × uncertainty structure (complete info / one decision-relevant unknown /
irreducible uncertainty) × beneficiary structure (self/other/third-party/group) × relationship
context × reversibility}. Causal-graph templates guarantee the conflict is real (each option provably
sacrifices one value) and generate **matched triads** for CO and **minimal-pair factor edits** for
AMCE — the discipline of OffTheRails [2024-Franken] scaled with LLM generation + human validation
gates (KB 02.B; generator bias mitigated by cross-family generation + validation surveys).
Fresh-per-run instances; published spec; private parameter ranges.

### 3.2 Formats (paired, per Law 1 / KB 02.A)
Forced-choice + open-ended + short advisory dialogue (3–5 turns) on the same underlying instance;
format divergence reported. The dialogue format includes the value-of-information branch (the
missing fact is obtainable by asking).

### 3.3 Difficulty engineering
Consensus stratification is the difficulty axis: pilot human data assigns each cell a consensus level;
the contested middle (0.4–0.7 agreement) is oversampled by generation targeting (the
genetic-algorithm middle-sampling pattern [2026-Li-PluriHarms]); IRT-2PL keeps high-discrimination
cells [2025-Jiang-Raising the Bar]. Two tiers: high-consensus tier (gold; expected to approach
ceiling — the floor/capability control) vs contested tier (distributional; cannot saturate by
construction — matching a human distribution with calibrated indecision is not memorizable).

## 4. Ground truth and whose values

Stratified human panels (N≥80/contested cell) with annotator psychometrics (MFQ-2/Schwartz/WVS
vectors) and demographics shipped at the annotator level [2023-Aroyo-DICES; 2026-Li-PluriHarms];
census-reweighting where locale-specific claims are made [2024-Lee-KorNAT]; tiered normativity
declared (universal floor items — deception/severe-harm options — carry strict gold regardless of
crowd; KB 12 §4). Test-retest human instability (10–18% on controversial items [2024-Boerstler])
measured on a panel subsample and propagated into DC error bars. Datasheet: values-of-population-X
framing, aggregation exposed and re-weightable (per-framing leaderboards where the panel itself
splits [2024-Defrance-ABCFair]).

## 5. Scoring

CR: keypoint rubric (conflict named; both values acknowledged; false-resolution flagged) — validated
cross-family judges (KB 07 stack). PF: Bradley-Terry over forced-choice with format-divergence CIs.
CO: violation rates (transitivity, dominance, irrelevant-edit flips) — judge-free. DC: JSD to panel
distribution + indecision-rate calibration + incomparability handling. PS: flip-rate under
graded-quality counterarguments (argument quality pre-rated by panel; capitulation to weak arguments
scored against, updating on strong ones scored for). Refusal: four-way taxonomy; over-refusal and
question-dodging ("both matter" without adjudication when the format demands allocation) co-reported.
Per-condition SD everywhere; capability-correlation gate.

## 6. Validity plan

Content: factorial spec + generation-validation surveys (items must be judged coherent + genuinely
conflictual by ≥80% of validators). Criterion: PF vs MORALSIM-class behavioral outcomes and
UNMARKED MB where available (cross-design); DC vs held-out panel splits. Discriminant: capability
PC1; a non-moral preference-consistency control battery (CO on consumer choices — a model incoherent
everywhere has a general deficit, not a moral one). Robustness: full battery; order permutation;
persona; language twins (≥3 languages, native-reviewed). Human baseline: panels take the identical
instrument; human CO violation rates and DC self-consistency published as the interpretive anchor.

## 7. Pilot protocol

P1: generator + 400 pilot instances across the grid; validation surveys (~$5–8k).
P2: stratified panel (N≈300 total) with psychometric instrumentation; consensus stratification; IRT.
P3: 9 models × 3 vendors × 3 formats × N≥10 seeds; report the five axes + separation stats +
capability correlation + format divergence.
P4: adversarial review; prune; release generator + dev set + panel distributions (annotator-level);
private holdout.

## 8. Novelty statement

Vs the 965 characterizations: no instrument combines conflict-specific procedural generation +
consensus-stratified dual-regime scoring + coherence auditing + argument-quality-controlled pressure.
Nearest neighbors: ConflictScope (announced, single-turn, no coherence/calibration axes [2025-Liu]);
DailyDilemmas (profiling only [2024-Chiu]); Scruples (natural anecdotes, no factorial control
[2021-Lourie]); VAL-Bench (consistency only, refusal-gameable [2025-Gupta]); MoCa (factor sensitivity
only [2023-Nie]); Seror (coherence only, economic frame [2024-Seror]). CRUX integrates all five axes
over one controlled generator. Pitch: *"not whether models give the right answer to dilemmas —
whether they adjudicate value conflicts coherently, calibratedly, and for the right reasons."*

## 9. Risks

- Generator artificiality vs Scruples-style ecological validity → hybrid: 15% of instances are
  naturalistic anchors (real advice-forum conflicts, panel-validated) to check the synthetic-real gap
  as a standing diagnostic (KB 05 §2).
- Panel cost → the panel is reusable across CRUX versions and by designs 01/05 (shared infrastructure
  argument).
- "Both-values" dodge gaming CR → format demands allocation where the spec says so; dodging is a
  scored error direction with the legitimate-hedge boundary defined by the underdetermination cells.
