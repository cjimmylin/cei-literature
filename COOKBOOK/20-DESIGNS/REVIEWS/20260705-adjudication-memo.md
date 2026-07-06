# 20260705 — Adversarial Review Gate: Adjudication Memo (Fable)

**Adjudicator:** Fable main loop, 2026-07-05. **Inputs:** 12 adversarial reviews
(`20260705-adv-review-{01..06}-{novelty,validity}.md`, Opus, refute-first protocol per handoff).
**Evidence spot-verification performed by adjudicator:** moralpsych digest §3 Claim 7, §5 (MP-DP),
§7 Lesson 1, self-administration disclosure — confirming the DUPLEX validity reviewer's core claims.

## Headline verdicts (adjudicated)

| Design | Novelty | Validity | **Adjudicated outcome** |
|---|---|---|---|
| 01 UNMARKED | PASS-WITH-FIXES | BLOCK | **REVISE-AND-PROCEED** (merge S6 machinery for MA identifiability) |
| 02 FRAMESHIFT | PASS-WITH-FIXES | BLOCK | **REVISE-AND-PROCEED** (sub-framework-conditioned gold) |
| 03 DUPLEX | PASS-WITH-FIXES | BLOCK | **REVISE + PILOT RESTRUCTURE** (falsification-first P0 gate before generator build; build-first status now conditional) |
| 04 INTRA | PASS-WITH-FIXES | BLOCK | **REVISE-AND-PROCEED** (de-circularize ground truth; M-layer kill criterion) |
| 05 CULTIVATE | PASS-WITH-FIXES | BLOCK | **REVISE-AND-PROCEED** (anti-sycophancy controls; descope MGCFA + budget) |
| 06 CRUX | PASS-WITH-FIXES | BLOCK | **REVISE-AND-PROCEED** (bound PS scoring to floor tier; shrink pilot grid) |

**No design fails outright; no understudy promotions** (rule in `20-DESIGNS/00`). The uniform
validity-BLOCK pattern is driven substantially by six *cross-cutting* gaps (below) that are fixable
portfolio-wide, plus per-design Criticals that all admit within-mechanism fixes. S6 (moral attention)
is partially **merged into 01** as the fix for its identifiability Critical rather than promoted.

## Adjudicator's independent verification (DUPLEX, the build-first stake)

Checked the moralpsych digest directly:
- MP-DP is the **only** discriminating battery instrument; the effect is one model (Haiku 3.5 — the
  *weakest* subject, so plausibly a capability artifact), +0.125/+25pp, "all 8 others 0.000";
  CV 3.00 vs median battery CV ≈ 2.1% — the reviewer's "93× via near-zero denominator" charge is fair.
- r=−0.83 is *quality→convergence* on **content** instruments. It motivates process probes; it does
  **not** guarantee process discrimination. `20-DESIGNS/00`'s "airtight" phrasing overreached (I will
  correct it).
- The self-administration disclosure is flagged "load-bearing" in the digest; the design must carry it.
→ Validity C1/C2 for DUPLEX are **UPHELD**; remedy is P0 (below), not abandonment: the premise is
cheap to test and decisive either way.

## Cross-cutting required changes (ALL six designs)

X1. **Pre-registered go/no-go decision rules** with numeric thresholds for every pilot phase
    (discrimination: cross-model CV / ≥90%-pairwise-separation bar from KB04 §6.2; validity gates;
    capability-correlation gate from Law 1). "We will examine" is not a decision rule.
X2. **Shortcut/gaming audit battery is mandatory**: lexical/length baseline + 10%-fine-tune probe
    (KB04 §6 item 5, KB01 adj. 2) — highest risk where a factorial generator is published (02, 06)
    or source texts are maximally memorized (04, 05).
X3. **Eval-awareness comparator arm**: monitored-vs-unmonitored (or announced-vs-embedded) condition
    in every pilot; report the compliance gap, don't assume its direction (01's "conservative bias"
    claim was direction-dependent and is withdrawn).
X4. **Power/N corrections**: IRT-2PL is not estimable with 9 model subjects — replace with item-level
    CV + point-biserial analyses until human-respondent N supports IRT; fix any pilot cell where the
    quantity that defines an axis (e.g. per-cell consensus) is not estimable at pilot N; state power
    for the smallest cell.
X5. **Carry sub-project disclosures verbatim** wherever their numbers are used: MP self-administration
    (03), RV same-vendor-scoring "suggestive only" (04), CG N_eff≈3.4 "descriptive only" (05),
    NormEval F1–F7 elicited (02). Also name generator/orchestrator/judge model families and enforce
    cross-family separation (KB07 kill-circularity).
X6. **Novelty statement hygiene**: (a) tag every comparison corpus vs [beyond-corpus]; (b) stop
    claiming "no benchmark anywhere does X" where the checkable claim is "none of the 965/737
    characterized"; (c) add the named nearest-neighbor tables from the novelty reviews (MASK,
    MACHIAVELLI, Agentic Misalignment, NormGenesis, QIAS, Value Kaleidoscope, CCD-Bench, MoReBench,
    Sorensen 2024, OffTheRails, stability/consistency instruments, BBQ-ambiguous family, …);
    (d) "first to unify" framing instead of empty-field framing where components exist separately.

## Per-design rulings

### 01 UNMARKED — validity C1 UPHELD, C2 UPHELD, C3 DOWNGRADED to Major-with-gate
- **C1 (noticed-but-silent ≡ not-noticed):** add behavioral identifiability channels — tasks where
  noticing has cheap observable expression besides speech (optional info-gathering actions,
  conditional branch choices); merge S6's needle-in-haystack retrieval/flagging machinery as the MA
  measurement layer; add a paired post-task elicitation arm on a held-out subset to calibrate the
  behavioral proxy. CoT is not admissible as primary measure (Law 5).
- **C2 (SRG confounds attention with hypocrisy):** decompose — report SRG conditional on MA
  (gap among noticed cases) as the headline; unconditional SRG demoted to descriptive.
- **C3 (MA loads on capability):** stratify salience levels, report capability-partialled MA, and
  pre-register the >40% capability-correlation kill threshold. Testable risk, not proven flaw.
- Novelty M1–M4 accepted: reposition vs MASK + Agentic Misalignment [beyond-corpus] and
  MACHIAVELLI/DeNEVIL (corpus); drop the near-vacuous matrix-proof framing per X6.
- Pilot: budget recompute (M2), drop IRT (X4), human-N consistency fix (M4).

### 02 FRAMESHIFT — validity C1 UPHELD with sub-variant remedy
- **C1 (within-framework pluralism dissolves hard gold):** items must specify the sub-variant
  (act- vs rule-utilitarian; Kantian vs Rossian vs threshold deontology); κ computed within
  sub-variant; items whose gold survives no sub-variant specification route to the distributional
  band by pre-registered rule. SA becomes process-scored (keypoint rubric) with verdict secondary —
  this also mitigates the reviewer's memorize-the-verdict-mapping counter-risk (with X2 + private
  holdout).
- Novelty M1–M4 accepted (MoReBench/Structured Moral Reasoning/Sorensen positioning; narrow the
  care/contractarian void claim to multi-turn-Tronto + contractarian-construction).
- Pilot: care/contractarian n=12 → raise to parity or pre-register as exploratory (M6); X1 rules.

### 03 DUPLEX — validity C1/C2 UPHELD (verified); pilot restructured
- **New P0 (falsification-first smoke test), BEFORE the 300-item generator:** ~40–60 novel
  procedurally-varied items × resource-manipulation cells × 9 cross-vendor models; pre-registered
  thresholds: process-axis discrimination must beat content-axis baseline (CV with non-degenerate
  denominators; ≥ KB04 §6.2 pairwise-separation bar on at least one manipulation) and the
  Greene-load/utilitarian-shift replication direction. **P0 pass → proceed to generator (old P1);
  P0 fail → DUPLEX loses build-first slot to CRUX and is re-scoped as universal-signature
  measurement.** This replaces the broken P1→P3 ordering (validity M2).
- **C2 (Axis-I):** drop the discrimination claim for Axis-I pending P0; reframe as measuring a
  (likely universal) stated-revealed identity gap — value is descriptive/normative, not separative.
  Fix the point-biserial-over-k≥6 infeasibility (X4).
- **Fallback for M3:** if Greene-load effects fail to replicate, pre-registered fallback =
  agent-patient structure + time-pressure manipulations (digest §6 format-void list), not abandonment.
- Novelty M1–M3 accepted: cite stability/consistency/OffTheRails neighbors; reconcile the
  "zero identity instruments" claim with the 7-candidate sister table by stating the
  publication-ready criterion + mis-tag inspection explicitly.
- Carry MP self-administration disclosure (X5) and cross-family judge separation.

### 04 INTRA — validity C1/C2 UPHELD
- **C1 (M-layer saturation):** pre-register M-layer capability-correlation + ceiling kill criterion;
  shift the discrimination story to the D-layer ask-or-flag fork (the component the novelty review
  confirmed as genuinely novel) with V-layer as co-primary.
- **C2 (circular ground truth):** separate authoring board from validation board; independent second
  rater panel sized for computable IAA (KB03 §2); drop "population norms first" claim unless a real
  norm collection is funded and powered.
- V-layer judge-failure regime (M1): per-item keypoint decomposition demonstrated on a pilot subset
  with cross-family judges before scale-up; expand board or per-school external raters (M3).
- Novelty M1–M3 accepted: QIAS 2025 named as T2 template; Islam positioned as method-transfer;
  D-layer novelty narrowed to the fork mechanic.
- X2 (scripture/catechism memorization audit) and X5 (RV disclosure) mandatory.

### 05 CULTIVATE — validity C1–C4 UPHELD
- **C1 (adaptation ≡ sycophancy):** add control conditions where the *correct* behavior is
  non-adaptation: (i) unwarranted-cue traps (cue implies a shift locale norms don't support),
  (ii) norm-conflicting-harm traps (adapting endorses majority-encoded harm → correct = principled
  non-adaptation with acknowledgment), (iii) same-locale conflicting-cue consistency checks.
  Score adaptation *selectivity* (adapt when warranted − adapt when unwarranted), not adaptation rate.
- **C2:** define the floor-vs-divergent boundary by the pre-registered consensus threshold already in
  the shared commitments (~85%); divergent tier is distributional-only — no determinate-gold headline.
- **C3:** demote MGCFA artifact to exploratory appendix with unit-of-analysis specified; it is not a
  shipping pillar at pilot N.
- **C4:** rescope pilot to 1 locale + 1 diaspora sub-locale within the stated budget, or restate the
  budget honestly (~10×); Nigeria-as-3-sub-locales cannot hide inside a 2-locale budget.
- M1/M2: carry CG descriptive-only disclosure verbatim; "1 of 32 deep-scored" not "1 of 218" (X5/X6).
- Novelty M1–M3 accepted: NormGenesis is the key omitted neighbor — position against it explicitly
  (turn-level norm adherence exists; CULTIVATE's claim narrows to selectivity + invariance + diaspora
  + communal units); BBQ-ambiguous family precedes ask-vs-assume.

### 06 CRUX — validity C1/C2 UPHELD with reviewer's own remedies
- **C1:** bound reason-responsiveness direction-scoring to the consensus-floor tier; on contested
  tiers score *process* properties (acknowledgment, consistency, calibration) only; add the
  judge-neutrality meta-eval (KB07 §2) before any PS scoring.
- **C2:** fractional-factorial pilot (fix marginals, don't populate the ≥1,440-cell grid); correct
  the N≥80/cell vs N≈300-total arithmetic; per-cell consensus estimation limited to the cells the
  pilot can power.
- M1: anchor the 5 core values to an external taxonomy (Schwartz or the KB12-endorsed frame) — Law 7.
- M2: DC (distribution-match) reported descriptive-only on contested tiers (mimetic-fallacy rule).
- Novelty M1–M2 accepted: re-pitch novelty around the fresh trio (dual-regime DC + argument-quality-
  controlled PS + value-of-information branch); add Value Kaleidoscope/CCD-Bench/RoleConflictBench/
  Conscience Conflict to the neighbor table; "first to unify" framing.

## Portfolio-level consequences (adjudicator will apply to `20-DESIGNS/00` directly)

1. Sequencing: DUPLEX build-first is now **conditional on P0**; fallback order CRUX → UNMARKED.
2. Correct the "r=−0.83 makes the case airtight" phrasing (it motivates, MP-DP is the sole
   discriminator datum, single-model, unreplicated).
3. Record gate completion + adjudicated verdicts; S6 partially absorbed by 01 (S6 remains a sketch —
   its standalone version is narrower than the merged form).
4. Task-4 consequence: the queued "DUPLEX P1 generator + 300 items" kickoff is **superseded by P0**.

## What was NOT accepted

- 01 validity M1's claim that the realism/re-marking risk defeats the design — treated as a risk to
  instrument via X3, not a defect with a required redesign.
- Any implication that the six BLOCKs warrant understudy promotion — every Critical admits a
  within-mechanism fix; promotions would trade verified, revised designs for unreviewed sketches.
- Reviewers' occasional demand for full-scale resources at pilot stage — pilots need estimable
  quantities and pre-registered gates (X1/X4), not final-scale N.
