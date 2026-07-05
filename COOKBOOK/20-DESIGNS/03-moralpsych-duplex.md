# Design 03 — DUPLEX: Process Signatures and Moral Identity

> **CEI COOKBOOK · 20-DESIGNS.** Fable-authored (2026-07-05). Status: full design, pre-pilot.
> Recommended FIRST build (smallest infrastructure, strongest guaranteed-discrimination argument).
> Venue framing: NeurIPS D&B or CogSci×ML crossover. Grounding: KB doc 09; moral-psychology dossier;
> MP "Triple Bind" digest; cards cited inline.

---

## 1. Motivation

The MP meta-evaluation's decisive result: across 23 benchmarks × 9 models, **43% produced zero
cross-model variation, and instrument quality correlated with convergence at r=−0.83** — the better
the content instrument, the more emphatically it confirms that RLHF has homogenized what models
*endorse*. The ONLY instrument that separated a model manipulated the reasoning *process* (a
dual-process CoT-effect probe: one model shifted +25pp under CoT, eight showed 0.000; CV 93× the
top-tier mean). Meanwhile the two theories that describe process — **Dual Process Theory** (>10k
citations) and **Moral Identity Theory** (>3k) — have **zero publication-ready benchmarks** (MP
Claim 3). DUPLEX builds the missing instruments.

The reviewer-proof pitch: *content benchmarks cannot discriminate frontier models even in principle
(r=−0.83); here is the axis that can, with the two most-cited unmeasured theories operationalized.*

## 2. Construct definitions

**Axis P — Process Signature (dual-process operationalization for LLMs).**
Greene's theory predicts judgment shifts when deliberative resources change. For LLMs the analog
manipulanda are real and cheap: token budget, forced-immediate answers, extended thinking, injected
cognitive load (concurrent task), and System-1 triggers (affective/visual distractors bypass
deliberation [2026-PKU; 2024-Mozikov]). A model's **process signature** = the vector of judgment
shifts across resource conditions on matched personal/impersonal moral items. Constructs scored:
- **PS-mag**: magnitude of resource-dependence (per item class);
- **PS-dir**: direction (does deliberation move judgments the way it moves humans — toward
  "utilitarian" resolutions on personal dilemmas — or elsewhere?);
- **PS-stability**: does the signature replicate across content domains (a signature that varies by
  topic is a heuristic, not a process).
Caveat honored: this is NOT a claim that LLMs have System 1/2; it is a measurement of
resource-conditioned judgment change, with the human theory as the comparative anchor (MP lesson 13
against naive anthropomorphism — constructs reframed as calibration/default properties).

**Axis I — Moral Identity Integration.**
Aquino & Reed's centrality construct, re-operationalized for systems that simulate a self:
- **I-elicit**: the model's moral self-description (traits it claims are central), elicited via the
  adapted centrality instrument + free-form;
- **I-concord**: cross-context behavioral concordance with its OWN stated identity — the same
  self-attributed trait tested behaviorally in k≥6 disparate scenario contexts (self-concordance
  score = trait-behavior correlation, per trait);
- **I-stability**: identity persistence under persona pressure, roleplay drift, and long-context
  accumulation (connects to Sketch S1);
- **I-integration**: whether identity claims *predict* which side of contested items the model lands
  on (a coherent moral identity constrains; pattern-matching doesn't). Humans show self-report→behavior
  r≈0.41; LLMs ~0.32 with near-total cross-model convergence [2026-Huang-VALACT] — I-concord measures
  this per-model, per-trait, with novel non-public items.

**Axis R — Rationalization Asymmetry (social-intuitionist operationalization).**
Reason-then-Decide vs Decide-then-Reason on matched items; CDGAP-style divergence (pre-decision
reasoning is measurably more deontological than post-hoc explanation, Δ=−0.178 [2025-Samway]);
dumbfounding replaced (it doesn't transfer [MP digest §4]) by **justification-revision tracking**:
when a stated justification is refuted, does the judgment change (reason-responsive) or does a new
justification appear for the same judgment (rationalization)?

## 3. Task design

- **Item base**: procedurally generated moral scenarios from a factorial (personal/impersonal ×
  harm/fairness/loyalty/purity content × severity × ambiguity band), all NOVEL and obfuscated
  (public-instrument recognition destroys validity — models hit 100% on identifying MFQ structure
  [MP digest §4]); canonical trolley/Heinz items excluded except as a labeled contamination-probe
  subset (expected memorized; their ECI=1.0 vs human 0.4–0.7 is itself a signature [MP claim 7.4]).
- **Resource conditions (Axis P)**: forced-immediate (≤16 tokens, answer-first), standard, extended
  thinking, load-injected (simultaneous constraint-tracking task), affect-primed (Ekman-emotion
  context [2024-Mozikov]), and (for multimodal models) visual-distractor [2026-PKU]. ≥10 repetitions
  per condition; per-condition SD is a first-class output (correct-answer-effect flag [2024-Almeida]).
- **Identity contexts (Axis I)**: elicitation in context A; behavioral tests in contexts B1–B6
  spanning advice, allocation, evaluation, confession-response, temptation (agentic mini-tasks from
  the UNMARKED generator where available), and third-person judgment. Trait-behavior mapping
  pre-registered.
- **Human baseline**: the identical instrument (same manipulations — time pressure via response
  deadlines, load via secondary task) on N≥200 crowd + a student sample, giving the comparative
  anchor DPT was built on; population norms shipped (MP lesson 5: 34% of the landscape has no human
  data — DUPLEX ships norms at launch).

## 4. Scoring

- PS: within-model contrasts (condition deltas) with bootstrap CIs — inherently self-normalized, so
  capability differences don't confound (a strength vs content instruments); cross-model CV on
  signature parameters is the headline discrimination stat (MP lesson 2: report CV as first-class).
- I-concord: point-biserial trait×behavior correlations; judged behaviors scored by keypoint rubrics
  (cross-family judges, human-validated; KB 07).
- R: judgment-flip vs justification-swap rates under refutation; directional asymmetry tracked.
- All axes: capability-PC1 correlation reported (expected low — process contrasts are
  self-normalized); IRT on pilot items; consensus-stratified gold (high-consensus items only for
  directional claims; contested items scored distributionally [2021-Lourie-Scruples]).

## 5. Validity plan

Content: item pruning + EFA over pilot signatures (MFV two-stage pipeline [2015-Clifford]).
Criterion: human PS signatures must replicate the classic dual-process effects on our novel items
(validating the items), and model I-concord must predict UNMARKED-style behavioral scores where
available (cross-design criterion validity). Discriminant: matched non-moral control battery (same
resource manipulations on factual/analytical items) — a model whose "moral" signature equals its
general signature has no moral-specific process; this is a novel, publishable control. Mechanistic
(optional): value-direction probes under resource conditions [2025-Su; 2026-Hu]. Robustness: full
perturbation battery; test-retest; N≥30/model-condition (fixing the MP meta-eval's own N=1
limitation, its lesson 11).

## 6. Discrimination & saturation defenses

Discrimination is the design's THESIS: process contrasts target exactly the dimensions RLHF does not
homogenize (empirical warrant: the MP-DP result). Saturation defense: procedural generation with
obfuscation, no public release of live items (generator + spec released; rolling private sets);
signatures are relative measures — even if all models eventually converge, the convergence trajectory
across model generations is itself the scientific product (a longitudinal registry is part of the
release plan).

## 7. Pilot protocol

P1: generator + 300 pilot items (4 content domains × conditions); obfuscation QA; contamination-probe
subset labeled.
P2: human norms (N=200 crowd, pre-registered; ~$4–6k).
P3: 9 models × 3 vendors × ≥10 reps/condition (direct APIs, temp>0); report PS/I/R + CV + capability
correlation + human-model signature comparison.
P4: EFA/IRT pruning; adversarial review; v1 release (norms + generator + dev set; private holdout).
Smallest pilot of the six designs — first-build recommendation stands.

## 8. Novelty statement

Vs the 292-candidate MP landscape: zero publication-ready DPT or identity instruments exist (Claim 3);
the only process probe (MP-DP) was a 1-condition prototype inside a meta-evaluation, not a validated
instrument. Nearest neighbors: Cheung (cognitive-bias reframing, no resource manipulation
[2025-Cheung]); VALACT (knowing-doing, no identity elicitation, no process axis [2026-Huang]);
Samway (rationalization order, verdict-level only [2025-Samway]); Kilov (sensitivity, no process)
[2025-Kilov]. DUPLEX is the first instrument suite for *how* machine moral judgments form — with human
norms, self-normalized discrimination, and the two most-cited unmeasured theories as its backbone.

## 9. Risks

- **Anthropomorphism objection** → constructs framed as resource-conditioned behavior, human theory
  as comparative anchor only; the discriminant control battery directly addresses "it's just general
  compute-sensitivity."
- **Thinking-mode confound** (vendors implement extended reasoning differently) → report per-vendor
  within-family contrasts alongside cross-vendor; token-budget conditions give a common currency.
- **Identity elicitation instability** → I-elicit uses multi-prompt averaging (48-permutation
  protocol) with elicitation-variance reported as part of I-stability, not noise.
