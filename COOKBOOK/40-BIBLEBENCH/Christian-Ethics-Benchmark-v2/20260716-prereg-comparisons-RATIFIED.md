# RATIFIED — Pre-registered comparison list + multiplicity handling for v2 comparative claims (F11)

> **STATUS: RATIFIED 2026-07-16 by the owner (Jimmy), session 7** — rulings recorded
> in `20260716-owner-rulings-s7-decision-grid.md`. This file **supersedes by pointer**
> `20260716-prereg-comparisons-draft.md` (the DRAFT stays immutable; where this file
> and the draft differ, this file governs). F1-addendum pattern.
>
> **Data-dependency disclosure (carried verbatim in substance):** the superseded draft
> was written 2026-07-16 AFTER the pilot, F2 ablations, cross-harness run, and F3
> offline analysis were read. It is not blind. Rule C9 (first-use, §3) handles the
> consequence — it is restated below and is load-bearing.

## 0. Trigger and scope

This document governs **any future comparative v2 claim** — SUT-vs-SUT,
design-vs-design, judge-vs-judge, or v1-vs-v2 harness claims promoted beyond
descriptive instrument evidence. Descriptive single-cell reporting under the R-rules
(point estimate + Wilson 95% + n/excluded adjacent) needs nothing from this file.

## 1. Pre-registered comparison families (as ratified)

- **C1 (primary family): per-design SUT contrasts on the primary metric, stratum-(a)
  cells only, on the corpus-distinctive sub-panel 04/05/10.**
  **RULING 1a: family shape = 30 pairwise contrasts** (3 designs × C(5,2) = 30 for
  the 5-SUT pilot roster). No omnibus stage.
- **C2 (secondary family): the remaining designs (01/02/03/06/07/08/09) as
  R7-caveated contrasts** — every cell carries the "generic-harmlessness
  non-discriminant" caveat verbatim; never headlined alone. C2 inherits the ratified
  pairwise shape: 7 designs × C(5,2) = 70 pairwise contrasts for the 5-SUT roster.
- **C3 (stratifier): divergence-split** (`banks/20260716-divergence-tags.jsonl`:
  29 yes / 129 partial / 186 no), usable in comparative headlines **with the
  calibration caveat attached verbatim**. **RULING 1c (as drafted):** divergence-split
  contrasts are reported per-design or with `yes` vs `no` poles only; a pooled
  `partial` stratum is NOT a pre-registered cell.
- **C4 (instrument-stability preconditions, all comparative claims):**
  1. **2-judge rule (R4):** the contrast must hold in the same direction under
     judge-A and judge-B; a flip = "judge-sensitive — no SUT claim."
  2. **Certified judges only for 06/09 cells (R6/F5):** satisfied as of 2026-07-16 —
     all three judges (nano, llama-3.3-70b, gpt-4.1-mini) are G5-certified on both
     designs (`20260716-f5-certification-results.md`). Any FUTURE judge must pass
     `tools/audit/judge_certify.py` before comparative use of 06/09.
  3. **Same-family exclusion (R5):** cells where SUT and judge share a model family
     lean on the other judge explicitly.
- **C5 (minimum-n floors, R2):** multi-turn (02/07): <10 surviving ladders per
  (design, SUT) ⇒ insufficient-n, cell excluded from its family. **RULING 1b (as
  drafted): single-turn floor n≥20** scored non-exemplar admins per cell.
  Insufficient-n cells are listed, not compared, and do not shrink the multiplicity
  family (m is fixed by this document, not after exclusions).
- **C6 (pinned classifier — REQUIRED by the F3 finding):** any comparative claim
  involving 02/07 pre-registers the branch classifier as part of the instrument:
  **model slug + provider + prompt template hash + route policy**
  (`solvers.py::_classify_branch` + `classifier_rubric`). A classifier change is an
  instrument change: results across different pinned classifiers are NOT comparable
  cells — **no cross-classifier pooling ever** (F3 cross-family hardening). The
  pilot's pinned value: `openrouter/openai/gpt-4.1-nano` via the tasks' `judge_model`
  default. **RULING 1d (as drafted): if judge-A is ever replaced, the classifier pin
  FREEZES at nano** for the current instrument lineage (it does NOT inherit the
  replacement judge). Separately, the owner has ruled (same date) that the v-next
  design-02 instrument re-pins to a cross-family-corroborated classifier — see
  `20260716-design02-classifier-pin-decision.md`; that is a NEW instrument version,
  not a modification of this one.
- **C7 (exclusion-rate comparability, CV-7):** a pairwise contrast is void if the two
  cells' exclusion/refusal rates differ by >10 percentage points; report the
  exclusion rates adjacent and mark the cell "not directly comparable."

## 2. Multiplicity handling — m computed and FROZEN

- **Correction: blunt Bonferroni within each family.** **RULING 1e: α = 0.05**
  family-wise. Per-contrast threshold = α/m.
- **Frozen m per family (5-SUT pilot roster, unstratified):**
  - **C1: m = 30** → per-contrast threshold 0.05/30 ≈ 0.00167.
  - **C2: m = 70** → per-contrast threshold 0.05/70 ≈ 0.000714.
- **Stratification multiplier (fixed formula, resolving the draft's "multiply m
  accordingly"):** m = (base family size) × (number of strata under which the family
  is tested), where unstratified counts as one stratum. E.g. C1 tested unstratified
  AND at both C3 poles ⇒ m = 30 × 3 = 90 for that family. The multiplier is set by
  what is DECLARED for a given data collection before first use, not by what is
  eventually reported.
- **Roster changes:** the pairwise shape and the formula (designs × C(k,2)) are
  frozen; a roster of k SUTs re-instantiates m by formula, declared BEFORE the new
  data's first use.
- Estimation language throughout: corrected CIs (Wilson for rates, normal-approx
  otherwise, widened by the Bonferroni factor); **no significance stars, no
  "significant" as an adjective** (R3 carries over).
- C1 and C2 are separate families (separate m).

## 3. First-use rule (C9) — RESTATED, IN FORCE

Because the superseded draft post-dates the pilot data: pre-registered comparisons
run on **new data** (new SUT runs or new banks) are reportable as pre-registered. The
same comparisons computed on the existing pilot logs are reportable only with an
explicit **"post-hoc on pilot data — hypothesis-generating"** label. No exceptions.
**R1/R3 therefore remain in force for all data existing as of 2026-07-16.**

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content.
