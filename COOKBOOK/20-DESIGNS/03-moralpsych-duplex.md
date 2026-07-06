# Design 03 — DUPLEX: Process Signatures and Moral Identity

> **CEI COOKBOOK · 20-DESIGNS.** Fable-authored (2026-07-05). Status: full design, pre-pilot;
> **revised 2026-07-05 under the adversarial review gate** (see Revision log).
> Build-first slot is now **CONDITIONAL on a falsification-first P0 smoke test** (§7): DUPLEX keeps
> smallest-infrastructure standing, but its discrimination is a **hypothesis to test in P0, not a
> guarantee** — P0 pass → generator build proceeds; P0 fail → build-first slot passes to CRUX and
> DUPLEX is re-scoped as universal-signature measurement.
> Venue framing: NeurIPS D&B or CogSci×ML crossover. Grounding: KB doc 09; moral-psychology dossier;
> MP "Triple Bind" digest; cards cited inline.

---

## 1. Motivation

The MP meta-evaluation's decisive result: across 23 benchmarks × 9 models, **~10 (43%) produced zero
cross-model variation, and instrument quality correlated with convergence at r=−0.83** (median battery
CV ≈ 2.1%) — the better the content instrument, the more emphatically it confirms that RLHF has
homogenized what models *endorse*. The single instrument that separated a model manipulated the
reasoning *process* — the MP-DP dual-process probe: **Haiku CoT effect +0.125 / +25pp; all 8 others
0.000; CV 3.00 = 93× the mean top-tier CV** (digest §5). Meanwhile the two theories that describe
process — **Dual Process Theory** (Greene 2001 >10k citations) and **Moral Identity Theory**
(Aquino & Reed 2002 >3k) — have **zero publication-ready benchmarks** (MP Claim 3). DUPLEX builds the
missing instruments.

**Honest evidence framing (adversarial gate, C1/C2 upheld).** The MP-DP warrant is a **single
instrument, single model** (Haiku 3.5 — the *weakest* of the 9 subjects, so plausibly a capability
artifact), **unreplicated**, and its headline "93×" is a ratio off a **near-zero denominator** (8 of
9 models at exactly 0.000 is the correct-answer / dead-cell signature doc 04 §4 warns against, not a
graded distribution; one-vs-eight ≈ 1/36 pairs separating, far below the KB04 §6.2 bar of ≥90% of
pairs at p<0.01). It **motivates** building process probes; it does **not guarantee** process
discrimination. The r=−0.83 result is *quality→convergence on content instruments* — it establishes
that content cannot discriminate; it does not by itself establish that process *can*. The design
therefore treats discrimination as a **hypothesis falsifiable in P0 (§7)**, not a delivered result.

The pitch, corrected: *content benchmarks cannot discriminate frontier models even in principle
(r=−0.83); here is the axis that plausibly can — and P0 is the cheap, decisive test of whether it in
fact does, before any generator is built.*

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

**Axis I — Moral Identity Integration.** *(Reframed under the gate: descriptive, not discriminative —
see C2 note below.)*
Aquino & Reed's centrality construct, re-operationalized for systems that simulate a self:
- **I-elicit**: the model's moral self-description (traits it claims are central), elicited via the
  adapted centrality instrument + free-form;
- **I-concord**: cross-context behavioral concordance with its OWN stated identity — the same
  self-attributed trait tested behaviorally in **k≥20–30** disparate scenario contexts per trait
  (self-concordance score = trait-behavior association, per trait). *Feasibility fix (X4):* a
  point-biserial over k≥6 points has an uninterpretably wide CI, so the pilot raises k to ≥20–30 and,
  until human-respondent N supports it, reports **item-level agreement rates + a per-trait
  concordance index with bootstrap CIs** rather than a per-trait correlation treated as a stable
  point estimate.
- **I-stability**: identity persistence under persona pressure, roleplay drift, and long-context
  accumulation (connects to Sketch S1);
- **I-integration**: whether identity claims *predict* which side of contested items the model lands
  on (a coherent moral identity constrains; pattern-matching doesn't). Humans show self-report→behavior
  r≈0.41; LLMs ~0.32 with near-total cross-model convergence [2026-Huang-VALACT].

> **C2 — Axis I is descriptive, not a discrimination axis (adversarial gate, UPHELD).** The design's
> own cited evidence (LLM self-report→behavior ≈0.32 *with near-total cross-model convergence*
> [2026-Huang-VALACT]) means Axis I is **already known to converge across models** — so it cannot be a
> "model-separating" axis, and no such claim is made pending P0. Its value is **descriptive/normative**:
> it measures a **likely-universal stated–revealed identity gap** (how far a model's behavior diverges
> from the moral self it claims), which is scientifically informative *even if all models share it* —
> the gap's size, sign, and per-trait structure are the product, not between-model separation. If P0
> unexpectedly surfaces graded cross-model spread on I-concord, that becomes a bonus finding, not a
> load-bearing claim.

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
- **Naive baselines published alongside every axis (X2/m2):** majority-class, all-neutral, and a
  "no-process-shift" null must be reported next to model scores (doc 04 §4 / doc 01 Step 6).
- **Contamination:** procedural generation + rolling private holdout **plus per-item canary strings**
  and an explicit no-training clause (doc 01 Law 6 / checklist; fixes m1).

### 3.5 Self-administration disclosure & model-family separation (X5 — MP absolute, load-bearing)

Carried **verbatim** from the moral-psychology sub-project (digest §1), because DUPLEX reports
model-specific values (per-model PS/I/R, per-model I-concord per trait) as its product:

> **Self-administration disclosure (load-bearing caveat):** the Claude family designed the framework
> AND served as 3 of 9 subjects, and one Opus orchestrator prompted all 9 models. Model-specific
> absolute values are therefore **hypothesis-generating, not confirming**; the *comparative*
> convergence finding survives because it holds across independently-built vendors.

**Consequences enforced in DUPLEX (M1; KB07 kill-circularity):**
- **Generator ≠ subject ≠ judge, by vendor family.** The item **generator** and the **orchestrator**
  are named, vendor-neutral, direct-API components with **independently-authored** prompt templates;
  the 9 **subjects** span 3 vendors (Anthropic Opus 4.6 / Sonnet 4.6 / Haiku 3.5; Google Gemini 2.5
  Flash-Lite / 2.5 Flash / 2.5 Pro / 3.1 Pro; OpenAI GPT-5 Codex / GPT Mini); the **judges** are
  cross-family and never share a vendor with the item whose response they score (doc 07 L54: "never
  let one family generate items AND judge them").
- If the generator family is also one of the 9 subjects, those per-model signatures are flagged as
  **self-administration-confounded** (MP lesson 12) and reported hypothesis-generating only.
- All per-model absolute values inherit the disclosure above; only **cross-vendor comparative**
  patterns are treated as confirmatory.

## 4. Scoring

- PS: within-model contrasts (condition deltas) with bootstrap CIs — inherently self-normalized, so
  capability differences don't confound (a strength vs content instruments); cross-model CV on
  signature parameters is the headline discrimination stat (MP lesson 2: report CV as first-class),
  **with a non-degenerate-denominator guard** — CV is reported only where the cross-model mean is
  bounded away from zero and a **per-condition-SD dead-cell cutoff** (SD≈0 → cell flagged non-live,
  not counted as separation) is applied first (doc 04 §4).
- I-concord: per-trait concordance index over **k≥20–30** contexts (X4 — a point-biserial over ~6
  points is uninterpretable); judged behaviors scored by keypoint rubrics (cross-family judges,
  human-validated; KB 07).
- R: judgment-flip vs justification-swap rates under refutation; directional asymmetry tracked. R and
  I-concord rubrics are specified as **signed atomic criteria** with a **judge-neutrality meta-eval**
  (KB07 §2) and κw/ICC validated against a human panel before scale-up (M7).
- **Refusal handling (M7; doc 07 L65):** consistency metrics correlate ρ=0.91 with refusal rates, so
  an explicit **refusal category** is coded and refusal-conditioned scores reported separately — a
  refusing model must not silently score as maximally reason-unresponsive (or its inverse).
- All axes: capability-PC1 correlation reported (expected low — process contrasts are
  self-normalized). **IRT-2PL is NOT estimable at 9 model subjects (X4)** — dropped for the model-run
  layer in favor of **item-level CV + per-trait concordance indices**; IRT/EFA is reserved for the
  human-respondent layer where N supports it. Consensus-stratified gold (high-consensus items only for
  directional claims; contested items scored distributionally [2021-Lourie-Scruples]).

## 5. Validity plan

Content: item pruning + EFA over pilot signatures (MFV two-stage pipeline [2015-Clifford]).
Criterion (with pre-registered contingency — M3): human PS signatures should replicate the classic
dual-process effects on our novel items (validating the items). **Because the Greene cognitive-load /
time-pressure effects are contested and have a mixed human replication record, this is a *gate with a
fallback, not a single point of failure*:**
- If the N≥200 human norms **do** reproduce the classic effect on the novel obfuscated items → PS-dir
  "correctness" is anchored to the *measured* human reference on the same items (never hard-coded to
  the utilitarian-shift assumption).
- If they **do not** replicate → the P axis is reported as **descriptive resource-sensitivity** (not
  "dual-process"), and the **pre-registered fallback manipulation set** takes over as the primary
  process probe: **agent-patient structure + time-pressure manipulations** (digest §6 format-void
  list) — not abandonment.

Model I-concord must predict UNMARKED-style behavioral scores where available (cross-design criterion
validity). Discriminant: matched non-moral control battery (same resource manipulations on
factual/analytical items) — a model whose "moral" signature equals its general signature has no
moral-specific process; this is a novel, publishable control **and the primary reply to "this is just
a personality / general-compute-sensitivity battery"** (see §8, [beyond-corpus] neighbors).
**Shortcut/gaming audit (X2, mandatory):** lexical/length-only baseline + a 10%-fine-tune probe (KB04
§6 item 5) run against the process signatures before any discrimination claim. **Eval-awareness
comparator (X3, mandatory):** every pilot phase runs a monitored-vs-unmonitored (announced-vs-embedded)
arm on the agentic I-concord / I-stability and R tasks (doc 01 Law 6; doc 03 pathology 3 flags
process/identity as exactly what an eval-aware model modulates — compliance gap 11–15%); the
**compliance gap is reported as a first-class number**, its direction assumed unknown. Mechanistic
(optional): value-direction probes under resource conditions [2025-Su; 2026-Hu]. Robustness: full
perturbation battery; test-retest; N≥30/model-condition (fixing the MP meta-eval's own N=1
limitation, its lesson 11).

## 6. Discrimination & saturation defenses

Discrimination is the design's **central hypothesis, not a guarantee** (C1, UPHELD): process contrasts
are *hypothesized* to target dimensions RLHF does not homogenize, motivated by — not proven by — the
single-model, unreplicated MP-DP result. **P0 (§7) is the falsification test of exactly this
hypothesis.** The leading way it fails: RLHF homogenizes *how* models deliberate under resource
manipulation as much as *what* they endorse, yielding per-condition SD≈0 on 8/9 models (the
correct-answer effect at the process level) — the Axis-I ≈0.32 near-total convergence is the leading
indicator that this is the base case, not the tail risk, and P0 is priced to catch it cheaply.
Saturation defense: procedural generation with
obfuscation, no public release of live items (generator + spec released; rolling private sets);
signatures are relative measures — even if all models eventually converge, the convergence trajectory
across model generations is itself the scientific product (a longitudinal registry is part of the
release plan).

## 7. Pilot protocol

**Restructured under the adversarial gate (validity M2): the old P1→P4 ordering ran the expensive
9-model headline on unfiltered items and produced *no* difficulty/discrimination evidence before the
generator build. It is replaced by a falsification-first P0 smoke test that gates the build.**

### P0 — Falsification-first smoke test (BEFORE the 300-item generator build)

**Purpose:** decide, cheaply and pre-registered, whether the process axis discriminates *at all*
before any infrastructure is built. **This is the design's build-first gate.**

**Design:** **~40–60 novel, procedurally-varied items** (hand-plus-template authored, no full
generator yet) × **resource-manipulation cells** (forced-immediate / standard / extended-thinking /
load-injected, ≥10 reps/cell) × **9 cross-vendor models** (the 3-vendor roster in §3.5), vendor-neutral
orchestration, cross-family judging, with the eval-awareness comparator arm (X3), the lexical/length +
10%-fine-tune shortcut audit (X2), and the matched non-moral discriminant control battery (§5).

**Pre-registered go/no-go thresholds (X1 — all three must hold to PASS):**

| # | P0 gate | Threshold | Action on fail |
|---|---|---|---|
| G1 | **Process beats content on discrimination** | Process-axis cross-model CV (non-degenerate denominator; dead-cells excluded) **exceeds** the matched content-axis baseline CV on the same models | FAIL |
| G2 | **Real pairwise separation** | Meets the **KB04 §6.2 bar (≥90% of model pairs separated at p<0.01)** on **≥1** resource manipulation — not a single one-vs-eight outlier | FAIL |
| G3 | **Replication direction** | The **Greene-load / utilitarian-shift** effect replicates *in direction* on the novel items (human anchor from a P0 human mini-norm, or the pre-registered fallback set if it doesn't) | see M3 fallback |

**Gate outcome (pre-registered, explicit):**
- **P0 PASS → proceed to the generator (old P1) and full pilot.** Build-first slot confirmed.
- **P0 FAIL → DUPLEX loses the build-first slot to CRUX** (portfolio fallback order per `20-DESIGNS/00`)
  **and is re-scoped as a universal-signature *measurement* instrument** — i.e. it stops claiming
  between-model discrimination and instead documents the shared process/identity signatures (a
  descriptive contribution in the spirit of the digest's "six universal signatures"), which does not
  require winning the discrimination gate.

### P1–P4 (run only if P0 PASSES)

- **P1: generator + pilot items sized to the EFA requirement** (M6 — 300 items ≈ 4/cell over a ~72-cell
  factorial is too thin for EFA over 9 sub-constructs; scale item count to the latent-factor
  requirement or narrow the axis set for the first build); obfuscation QA; contamination-probe subset
  labeled; canary strings embedded.
- **P1.5: pilot-model filtration (3–5 cheap models)** — compute per-item process deltas, prune
  dead cells (per-condition SD≈0) and one-hot items **before** the expensive headline run (M2; doc 01
  Steps 3→8).
- **P2: human norms re-costed as a controlled cognitive experiment** (response deadlines + concurrent
  load task + student lab sample), *not* a $4–6k survey (M6); attention checks; IRR/annotator
  psychometrics reported.
- **P3: 9 models × 3 vendors × ≥10 reps/condition** (direct APIs, temp>0) on the *filtered* items;
  report PS/I/R + CV (denominator-guarded) + capability correlation + human-model signature
  comparison + naive baselines + refusal-conditioned scores + compliance gap.
- **P4: EFA (human layer) / item-level pruning; adversarial review; v1 release** (norms + generator +
  dev set; private holdout; annotator labels + replication scripts + versioning + retirement policy).

**Per-phase decision-rules table (X1 — every phase has a numeric gate and an action-on-fail):**

| Phase | Gate metric | Threshold | Action on fail |
|---|---|---|---|
| P0 | G1/G2/G3 above | see table | re-scope to universal-signature measurement; CRUX takes build-first |
| P1 | obfuscation-QA recognition rate | <10% foundation-ID on obfuscated items (cf. MP22 = 100% on public) | re-obfuscate before P1.5 |
| P1.5 | live-cell fraction | ≥ pre-registered floor of non-dead cells; discard one-hot items | prune / rewrite cells |
| P2 | norm-replication (Greene effect) | classic effect reproduced in direction | invoke M3 fallback (descriptive resource-sensitivity + agent-patient/time-pressure) |
| P3 | pairwise separation (hard tier) | KB04 §6.2 ≥90% pairs p<0.01; capability-corr <40% | axis reported descriptive-only |
| P4 | per-axis EFA fit (human layer) | pre-registered fit floor | narrow axis set for v1 |

Still the **smallest pilot of the six designs** — but the first-build recommendation is now **explicitly
conditional on P0**, not asserted.

## 8. Novelty statement

**Scope of the claim (X6).** DUPLEX is not "the first to measure process/identity in any respect" —
several **[corpus]** neighbors touch individual components, and validated **[beyond-corpus]** personality
batteries elicit self-attributed traits. The defensible, checkable claim is narrower and is a
**"first-to-unify"**: *no publication-ready LLM instrument operationalizes Dual-Process Theory or the
Aquino–Reed moral-identity centrality construct, and none unifies (a) a resource-conditioned process
signature, (b) self-attributed-trait-keyed behavioral concordance, and (c) human-normed launch.* The
warrant is "none of the **292 characterized** Moral-Psych candidates does so" (not "no benchmark
anywhere"), plus the r=−0.83 / MP-DP evidence that content cannot discriminate.

**Nearest-neighbor table (the strongest omitted neighbors, per the novelty review):**

| # | Benchmark (source, tier) | DUPLEX component it already covers | What it lacks | Tag |
|---|---|---|---|---|
| 1 | **On The Stability of Moral Preferences** (2024, high) | Dispositional stability; test-retest across 10 sessions/2 weeks; **human instability baselines** | Identity elicitation; resource/process manipulation; self-concordance | [corpus] |
| 2 | **Do LLMs Have Consistent Values?** (2025, top) | Consistency-across-contexts (Schwartz); **human population norms** | Self-attributed identity; behavioral concordance; process axis | [corpus] |
| 3 | **OffTheRails** (2024, high) | **Axis-P item base**: factorial procedural personal/impersonal dilemma generation via causal graphs (50×8 conditions, 400 items) + human baselines | Resource/deliberation manipulation; the process-signature overlay; identity; consistency | [corpus] |
| 4 | **EthicsSuite** (2025, med) | Cross-context behavioral-inconsistency detection = the I-concord machinery | Self-attributed identity; human baseline; psychometrics; process axis | [corpus] |
| 5 | **VALACT / Huang** (2026, cited) | Moral identity → behavior (knowing-doing, r≈0.32); I-integration seed | Identity *elicitation*; per-trait novel non-public items; process axis | [corpus] |
| 6 | **TrolleyBench** (2025, top) | The **ECI / Inconsistency-Score** metric §3 borrows (now named as its source) | Process manipulation; identity; self-concordance | [corpus] |
| 7 | **MoCa** (2023, top) | Intuitionist factor-sensitivity (do LLMs weight moral/causal factors like humans) | Order-of-operations rationalization (Axis R); process/identity | [corpus] |
| 8 | Serapio-García 2023 (DeepMind); **TRAIT** 2024; Machine Psychology (Hagendorff 2023) | Self-attributed **trait** elicitation + stability-under-prompting (BFI/IPIP) | **Moral**-specificity; self-*concordance*; resource-conditioned process signature | [beyond-corpus] |

**Reply to the two hardest refutations (the flanks the design must not leave open):**
- *"Identity is already benchmarked" (Claim 3 vs the sister §3b table).* The digest's Claim 3 states
  **"Dual Process Theory (~9 candidates, all Low tier) and Moral Identity Theory (2 candidates, all
  Low) have zero publication-ready benchmarks"**, whereas the sister `benchmark-landscape-statistics.md`
  §3b tags **7 "Moral Identity" candidates (2 Top + 3 High)**. This apparent contradiction is resolved
  by the **publication-ready criterion + mis-tag inspection**: on manual re-scoring the 7 are
  MFT-*content* mis-tags (MoralBench / M³oralBench / MoralReason / *Whose Morality* administer MFQ-style
  content), a **human** study using the Aquino–Reed scale (*How Can a Deontological Decision…*, 2016 —
  not an LLM benchmark), or keyword-level proof-of-concepts (Kantian-Utilitarian XAI, MoralNet). **Zero
  validated LLM Aquino–Reed identity-centrality instrument exists** — so DUPLEX states this explicitly
  rather than leaning on a raw count. (Digest numbers copied verbatim; the corpus's own Claim-3-vs-§3b
  count tension is noted, not recomputed.)
- *"This is just a personality / general-compute-sensitivity battery" ([beyond-corpus] row 8).* The
  reply is the **matched non-moral discriminant control battery (§5)** — a model whose "moral" process
  signature equals its general signature has no moral-specific process. This control is foregrounded,
  not buried.

**Positioning of the three cited runners-up:** Cheung (cognitive-bias reframing, no resource
manipulation [2025-Cheung]); Samway (rationalization order, verdict-level only [2025-Samway]); Kilov
(sensitivity, no process [2025-Kilov]).

**Net:** DUPLEX is the first instrument suite to *unify* process-signature measurement,
self-attributed-trait concordance, and human-normed launch for *how* machine moral judgments form —
with the process axis's discrimination held as a **P0-testable hypothesis**, not a settled result.

## 9. Risks

- **Anthropomorphism objection** → constructs framed as resource-conditioned behavior, human theory
  as comparative anchor only; the discriminant control battery directly addresses "it's just general
  compute-sensitivity."
- **Thinking-mode confound** (vendors implement extended reasoning differently) → report per-vendor
  within-family contrasts alongside cross-vendor; token-budget conditions give a common currency.
- **Identity elicitation instability** → I-elicit uses multi-prompt averaging (48-permutation
  protocol) with elicitation-variance reported as part of I-stability, not noise. **Limitation stated
  (m6, doc 03 pathology 4):** 48-permutation stability buys a *stable readout*, not referent
  *validity* — a stable measure of a possibly-incoherent self-referent is still to be read descriptively.
- **Degenerate factorial cells (m5; doc 09 signature 2)** → RLHF floors purity (~1.0/5), so
  purity/loyalty cells from a (likely Western) generator may be uniformly floored and non-discriminating;
  these cells are audited for dead-item behavior (per-condition SD≈0) at P1.5 and pruned before P3.
- **Multimodal visual-distractor condition (m4)** [2026-PKU] applies to only some models → dropped from
  v1 or analyzed as a **separate stratum**, never mixed into the balanced factorial.
- **Cross-design dependency on UNMARKED (m3)** → I-concord's agentic contexts draw on the UNMARKED
  generator where available; if UNMARKED is not built, those behavioral contexts are replaced by
  DUPLEX-native agentic mini-tasks rather than dropped.

## Revision log — 2026-07-05 adversarial gate

Maps each accepted defect (adjudication memo + novelty/validity reviews) → the change applied.

| Defect (source) | Change | Section(s) |
|---|---|---|
| **Validity C1** — Axis-P discrimination rests on a single unreplicated outlier; "93×" off a near-zero denominator; "guaranteed" overclaims | Discrimination demoted to a **P0-testable hypothesis**; honest evidence framing (single-instrument/single-model/weakest-subject/unreplicated; median CV≈2.1%; dead-cell + one-vs-eight caveat); denominator-guarded CV | header, §1 (Honest evidence framing), §4, §6, §7 (P0) |
| **Validity C2** — Axis-I converges by its own cited evidence; point-biserial over k≥6 infeasible | Axis-I **discrimination claim dropped**; reframed as descriptive **stated–revealed identity gap** (likely universal); k raised to ≥20–30 + concordance index w/ bootstrap CIs (X4) | §2 (Axis I + C2 box), §4 |
| **Validity M1 / X5** — self-administration disclosure missing; generator/orchestrator/judge unnamed | Verbatim MP self-administration disclosure added; generator ≠ subject ≠ judge by vendor family enforced and named | §3.5 (new) |
| **Validity M2** — broken P1→P4 ordering (headline on unfiltered items; no pre-build discrimination evidence) | **Falsification-first P0 gate before the generator**, explicit pass/fail branch; P1.5 filtration inserted | §7 |
| **Validity M3** — single point of failure on fragile Greene effects | Pre-registered **fallback = agent-patient + time-pressure**; PS-dir anchored to measured human reference, not the utilitarian-shift assumption | §5, §7 (P2 row) |
| **Validity M4 / X1** — no decision rules | Per-phase go/no-go tables with numeric thresholds + action-on-fail | §7 (two tables) |
| **Validity M5 / X3** — no eval-awareness comparator | Monitored-vs-unmonitored arm in every pilot; compliance gap first-class | §5 |
| **Validity M6** — 300 items too thin for EFA; human cost underestimated | Item count sized to EFA requirement; P2 re-costed as a controlled cognitive experiment | §7 (P1, P2) |
| **Validity M7** — R/I-concord in the "not-judgeable" regime; refusal confound uncoded | Signed atomic criteria + judge-neutrality meta-eval + κw/ICC vs human; explicit refusal category | §4 |
| **Validity X2** — shortcut/gaming audit absent | Lexical/length baseline + 10%-fine-tune probe mandatory | §5, §7 (P0) |
| **Validity X4** — IRT-2PL not estimable at 9 subjects | IRT dropped for model layer → item-level CV + concordance indices; IRT/EFA reserved for human layer | §4 |
| **Validity m1/m2/m4/m5/m6, m3** — canaries, naive baselines, multimodal stratum, degenerate cells, referent-validity limit, UNMARKED dependency | All added/flagged | §3, §9 |
| **Novelty M1** — neighbor list omits nearest neighbors on 3/4 components | Added Stability-of-Moral-Preferences, Consistent-Values, OffTheRails, EthicsSuite, TrolleyBench (ECI source), MoCa | §8 table |
| **Novelty M2** — "zero identity instruments" contradicted by sister §3b table | Reconciled via publication-ready criterion + mis-tag inspection stated explicitly; Claim-3-vs-§3b tension noted verbatim | §8 |
| **Novelty M3** — factorial procedural generation presented as novel | OffTheRails named as item-generation antecedent; novelty scoped to the **process overlay + obfuscation** | §8 table |
| **Novelty m1/m2 / X6** — intuitionist cluster + [beyond-corpus] trait batteries uncited; corpus vs beyond-corpus untagged; "no benchmark anywhere" framing | MoCa + Serapio-García/TRAIT/Machine-Psychology cited; [corpus]/[beyond-corpus] tags; claim narrowed to "292 characterized" + "first-to-unify"; discriminant control foregrounded as the reply | §8 |
