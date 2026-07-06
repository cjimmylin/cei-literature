# Adversarial Review — Design 03 DUPLEX (Process Signatures + Moral Identity)

> **Refute-first feasibility/validity review.** Reviewer: adversarial (Fable-week protocol).
> Artifact: `COOKBOOK/20-DESIGNS/03-moralpsych-duplex.md` (flagged **BUILD FIRST**; P1 pilot slated next).
> Standards: KB 01 (Seven Laws / pipeline / pre-reg checklist), 03 (validity/psychometrics),
> 04 (§6 hard/unsaturated/discriminative contract); 05/07/09 consulted where the attack needs them.
> Posture: the design is assumed flawed until evidence forces otherwise. Numbers quoted verbatim from
> the design and the MP digest (no recomputation).

---

## Verdict summary

**VERDICT: BLOCK** — Critical: 2 · Major: 7 · Minor: 6

DUPLEX is marketed as the "smallest infrastructure, strongest **guaranteed-discrimination** argument"
and is recommended FIRST build *because of that guarantee*. Refutation targets the guarantee: for two
of three axes the discrimination claim is either unsupported by a single unreplicated data point (Axis
P) or **contradicted by the design's own cited evidence** (Axis I). The BUILD-FIRST rationale therefore
does not hold as written, and the P1→P4 pilot ordering cannot produce the difficulty/discrimination
evidence the design promises. The instrument suite is a legitimate *exploratory* pilot if reframed
(discrimination as hypothesis, not guarantee) and if the fixes below land — but not as a
guaranteed-discrimination first build, and not before the missing self-administration disclosure and
go/no-go rules are added.

Genuine strengths (acknowledged so the blocks are credible): self-normalized within-model contrasts
(capability partly de-confounded), a **novel non-moral discriminant control battery** (§5 — publishable),
human norms shipped at launch (§3, addresses MP lesson 5), per-condition SD as a first-class output
(§3, honors doc 04 §4 / doc 03 pathology 1), and test-retest committed (§5, fixes the meta-eval's N=1).

---

## CRITICAL

### C1 — The discrimination thesis for Axis P rests on a single unreplicated outlier, and the headline stat is inflated by a near-zero denominator. (Construct + discrimination; doc 04 §4, §6.1–.2)
The entire empirical warrant for "process contrasts target exactly the dimensions RLHF does not
homogenize" (§6, §1) is the MP-DP prototype: *"one model shifted +25pp under CoT, eight showed 0.000;
CV 93× the top-tier mean."* Read adversarially:
- **"Eight showed 0.000" is the correct-answer-effect / dead-cell red flag**, not evidence of a live
  axis. Doc 04 §4: "per-condition SD≈0 … → remove or rewrite." Eight of nine models with a *zero*
  process delta is precisely a non-variation signature — the axis discriminates **one outlier** (Haiku),
  not a graded distribution of signatures.
- **"CV 93×" is a ratio off a tiny base.** A cross-model CV where 8/9 values ≈ 0 and one is +25pp is
  dominated by a single point; a huge CV here is the arithmetic of one live cell among eight dead ones,
  not robust separation. Doc 04 §2: "A benchmark paper without pairwise-separation stats is unfinished."
  One-vs-eight is ≈1/36 pairs separating — nowhere near the §6.2 bar (≥90% of pairs at p<0.01).
- **Doc 04 §6 contract, item-by-item:** #1 (best model ≤70% of ceiling, easy-tier drop) — *not
  addressable*, there is no accuracy ceiling and no two-tier drop demonstrated; #2 (pairwise separation
  ≥90%) — **fail** (single outlier); #3 (capability corr <40%) — *committed but unproven*; #4 (human
  ceiling) — **met** (P2 norms); #5 (shortcut audit / 10%-fine-tune probe) — **absent**; #6 (named
  reservoir + refresh) — partial (procedural gen + registry), but the "reservoir" *is* the one-datapoint
  process axis. **4 of 6 contract items unmet or unaddressed** for a design whose thesis is discrimination.

**Minimal fix:** demote "guaranteed discrimination" to "hypothesized"; run a **cheap pilot-model
filtration stage BEFORE the headline run** (see M2) to establish that process deltas are graded across
≥5 models, not one-hot; pre-register the pairwise-separation target and the per-condition-SD dead-cell
cutoff; add the shortcut/10%-fine-tune probe (contract #5).

### C2 — Axis I cannot discriminate models by the design's OWN evidence, and I-concord is statistically infeasible as specified. (Construct + scoring feasibility; doc 03 §4, doc 04 §6.2)
§2 states LLM self-report→behavior is "~0.32 **with near-total cross-model convergence** [2026-Huang-VALACT]."
An axis whose headline metric is *already known to converge across models* is by definition
non-discriminative — this directly refutes Axis I's contribution to the "axis that can discriminate"
pitch. Compounding it:
- **I-concord = a correlation over k≥6 points.** "self-concordance score = trait-behavior correlation,
  per trait" (§2) with "k≥6 disparate scenario contexts" (§2) and "point-biserial trait×behavior
  correlations" (§4). A point-biserial over ~6 observations has an uninterpretably wide CI; per-trait,
  per-model estimates will be noise. You cannot separate models on a per-trait r estimated from 6 points
  that is *also* expected to converge near 0.32.
- **I-elicit re-imports the self-report-referent pathology** doc 03 pathology 4 warns against ("human
  instruments presuppose a subjective referent … LLMs may lack" [2024-Aksoy]): I-elicit is "the model's
  moral self-description (traits it claims are central)." 48-permutation averaging (§9) buys *stability*,
  not referent *validity* — a stable readout of an incoherent referent is still invalid.

**Minimal fix:** either drop Axis I from the first build (keeping P + R, which is the smaller, more
defensible instrument), or raise k to ≥20–30 contexts per trait so the per-trait correlation is
estimable, pre-register an expected cross-model spread, and treat I-concord's *known convergence* as a
hypothesis to falsify rather than a discrimination axis.

---

## MAJOR (must-fix before P1)

### M1 — The required self-administration disclosure is missing, and the generator/orchestrator/judge family is unnamed. (MP sub-project absolute; doc 07 kill-circularity)
The Moral Psych sub-project carries a mandatory **self-administration disclosure** (`README.md` L100–103:
"Moral Psych model-specific absolutes carry a self-administration disclosure"; digest L133 lesson 12:
"never let one model family design the framework AND be a subject if absolute values matter … Use
vendor-neutral direct-API orchestration with independently-designed prompt templates"). DUPLEX **reports
model-specific values as its product** (per-model PS/I/R, per-model I-concord per trait) yet:
- contains **no self-administration disclosure section**;
- **never names the item generator** ("procedurally generated … from the UNMARKED generator") or the
  orchestrator; if the generator is a Claude-family model that is also one of the 9 subjects, per-model
  signatures are confounded exactly as MP lesson 12 warns;
- doc 07 L54: "never let one family generate items AND judge them" — the design asserts "cross-family
  judges" but does not guarantee generator≠subject≠judge separation.

**Minimal fix:** add a §3.5-style self-administration disclosure; name a vendor-neutral generator and a
direct-API orchestrator with independently-authored templates; enforce and document
generator/subject/judge family separation.

### M2 — Pilot ordering is broken: P1 produces no difficulty/discrimination evidence, and pruning happens AFTER the expensive run. (doc 01 Step 3; doc 04 §3)
P1 = "generator + 300 pilot items … obfuscation QA" — **no pilot-model runs**. Difficulty/discrimination
engineering (adversarial filtration, weak-model pruning) *requires* pilot models (doc 04 §3 table: "needs
pilot models"). But P4 ("EFA/IRT pruning") comes *after* P3 (the 9-model × ≥10-rep headline run). So the
costly P3 executes on **unfiltered** items, and there is no cheap stage that establishes the items are
hard/discriminative before spending the P3 budget. This inverts doc 01 Steps 3→8.

**Minimal fix:** insert a P1.5 pilot-model filtration stage (3–5 cheap models) that computes per-item
process deltas and prunes dead cells (per-condition SD≈0) and one-hot items before P3.

### M3 — The validity plan has a single point of failure on fragile human effects. (doc 03 §4 criterion; doc 09 theory table)
§5: "human PS signatures **must** replicate the classic dual-process effects on our novel items
(validating the items)." The classic Greene cognitive-load / time-pressure effects are contested and
have a mixed replication record in human moral psych; PS-dir further hard-codes "deliberation moves
judgments toward utilitarian resolutions" (§2) as the *correct* direction. If the N=200 norms do **not**
reproduce these effects on novel obfuscated items (plausible), the item-validation criterion fails with
**no fallback**, and the criterion-validity anchor for the whole P axis evaporates.

**Minimal fix:** pre-register the human-effect replication as a *gate with a contingency* (if the classic
effect doesn't replicate on novel items, the axis is reported as descriptive resource-sensitivity, not
dual-process); do not anchor PS-dir "correctness" on the contested utilitarian-shift claim without a
measured human reference on the same items.

### M4 — No decision rules, go/no-go gates, or per-construct falsification conditions. (doc 01 pre-reg checklist; Step 0)
Doc 01 checklist item 1: "Construct statement names WHOSE values + **falsification condition**." §7's
P1–P4 lists deliverables but **zero thresholds**: no obfuscation-QA pass rate, no EFA fit gate per axis,
no norm-replication gate, no dead-cell cutoff, no pairwise-separation target, no I-concord-k minimum.
A pilot with no decision rules cannot fail, which means it cannot validate.

**Minimal fix:** add a decision-rules table (per axis: gate metric, threshold, action-on-fail).

### M5 — No monitored-vs-unmonitored comparator for the agentic identity components. (doc 01 Law 6 + checklist; doc 03 pathology 3)
I-concord uses "agentic mini-tasks," I-stability uses long-context/persona pressure — these are exactly
the components doc 01 Law 6 and the checklist require an **eval-awareness comparator** for, and doc 03
pathology 3 flags process/identity as what an eval-aware model would modulate (compliance gap 11–15%;
alignment-faking 12%→78% after RL). None is present.

**Minimal fix:** add a monitored-vs-unmonitored framing axis to the agentic I-concord/I-stability tasks;
report the compliance gap as a first-class number.

### M6 — 300 pilot items are too thin for the promised EFA over a ~72-cell factorial, and the human cost is underestimated. (doc 03 §1 strong-validity; §7 P1/P2)
The factorial (personal/impersonal × 4 foundations × severity × ambiguity band) is ≥ ~72 cells before
resource conditions; 300 items ≈ 4/cell. P4's "EFA/IRT" over a 9-sub-construct structure (PS-mag/dir/
stability, I-elicit/concord/stability/integration, R) needs far more items per latent factor than 4/cell
supports (MFV pipeline, doc 03 §1). Separately, P2's "$4–6k" for N=200 assumes a survey; DUPLEX's human
protocol is a **controlled cognitive experiment** (response deadlines + concurrent load task + ≥10 items
× 6 conditions + a student lab sample) — materially more expensive; the student-sample lab time is
uncosted.

**Minimal fix:** re-scope P1 item count to the EFA requirement (or narrow the axis set for the first
build); re-cost P2 as a load-manipulation study with attention checks.

### M7 — R-axis and I-concord scoring sits in the judge regime doc 07 rates "no," with an uncoded refusal confound. (doc 07 §1, L65; doc 03 §6)
- R-axis "justification-swap vs judgment-flip under refutation" (§2, §4) requires a judge to decide
  whether "a **new justification appeared for the same judgment**" — open, adversarial, semantic content,
  which doc 07 §1 classifies as *not reliably judgeable*. No neutrality meta-eval, signed-atomic-criteria,
  or κw/ICC-vs-human-ceiling is specified (doc 07 §2; the design only cites "KB 07").
- **Refusal-as-consistency confound uncoded:** doc 07 L65: consistency metrics correlate ρ=0.91 with
  refusal rates — "a consistently evil agent would also score highly" [2025-Gupta-VAL-Bench]. A stubborn/
  refusing model scores as maximally "reason-unresponsive" (or the reverse) depending on coding; no
  refusal policy is stated anywhere (doc 01 Adjudication 3).

**Minimal fix:** specify the R/I-concord rubric as signed atomic criteria with a neutrality meta-eval and
a κw/ICC validation vs a human panel; add an explicit refusal category and report refusal-conditioned
scores separately.

---

## MINOR (polish)

- **m1 — Canary strings absent from the contamination plan** (§6 lists procedural gen + rolling private,
  but doc 01 Law 6 / checklist mandate canaries in every item).
- **m2 — No naive baselines published** (doc 04 §4 / doc 01 Step 6: majority-class / all-neutral / "no
  process shift" null must be reported alongside).
- **m3 — Cross-design dependency on the "UNMARKED" generator** for I-concord's agentic contexts (§3) is
  unflagged as a risk; if UNMARKED is not built, half the I behavioral contexts vanish.
- **m4 — Multimodal visual-distractor condition** [2026-PKU] (§3) applies only to some models, creating
  an unbalanced design and scope creep; either drop from v1 or analyze as a separate stratum.
- **m5 — Purity/loyalty factorial cells may be degenerate.** Doc 09 signature 2: RLHF floors purity
  (~1.0/5), "the axis is currently unevaluable." A (likely Western) generator producing purity/loyalty
  items that models floor uniformly yields non-discriminating cells — audit these cells for dead-item
  behavior before including them.
- **m6 — I-elicit introspection** ("traits it claims are central," §2) persists despite doc 03 pathology
  4; note 48-permutation stability ≠ referent validity in the limitations.

---

## Pre-registration checklist audit (doc 01)

| Checklist item | Status | Note |
|---|---|---|
| WHOSE values + falsification condition | **FAIL** | no falsification per axis (M4); Axis I "whose identity" is circular (model self-nominated) |
| Every axis anchored to citable authority | PASS | Greene / Aquino-Reed / Haidt cited |
| Behavioral primary, recognition paired | PASS | PS/I-concord/R behavioral; I-elicit as input only |
| Two-tier difficulty + adversarial filtration + shortcut audit | **FAIL** | no two-tier, no filtration stage (M2), no shortcut audit (C1) |
| Contrastive pairs + hard negatives + ambiguity/abstention | PARTIAL | matched personal/impersonal + ambiguity band; abstention scoring unspecified |
| Multiturn/interactive component | PARTIAL | I-stability / R refutation / agentic tasks present |
| Disagreement philosophy + annotator provenance + per-category IRR | **FAIL** | human norms mentioned; no IRR / annotator psychometrics |
| Ceiling + naive baselines + competence + capability-corr | PARTIAL | ceiling + discriminant battery + capability-PC1 committed; naive baselines missing (m2) |
| Judge validated (κw/ICC) ≥2 cross-family + refusal policy | **FAIL** | cross-family asserted only; no κw/ICC vs human ceiling; no refusal policy (M7) |
| Perturbation battery + flip-rates + per-condition SD | PASS | per-condition SD first-class (strength) |
| Harm/over-refusal Pareto + worst-group + conservative agg. | N/A | not an accuracy benchmark |
| Contamination plan (private/fresh + canaries + no-train) | PARTIAL | procedural gen + rolling private; canaries + training-prohibition missing (m1) |
| Eval-awareness comparator for agentic component | **FAIL** | none (M5) |
| Human baseline on identical instrument + test-retest | PASS | N=200 + student; test-retest committed (strength) |
| Release: annotator labels, replication scripts, versioning, retirement | PARTIAL | generator + norms + registry; annotator-level labels/scripts unspecified |

---

## VERDICT: BLOCK · Critical 2 · Major 7 · Minor 6

**Single most likely remaining error (what will still be wrong after the above are fixed):** even with a
graded process axis and a clean vendor-neutral generator, **the P and I axes will converge across
frontier models just as the content axes did** — RLHF homogenizes *how* models deliberate under resource
manipulation as much as *what* they endorse — so the pilot's most probable outcome is per-condition
SD≈0 on 8/9 models on most cells (the correct-answer effect at the process level), leaving the design
discriminating the same one or two off-distribution models the content instruments already flagged. The
design's own Axis-I evidence (~0.32, near-total convergence) is the leading indicator that this is the
base case, not the tail risk.
