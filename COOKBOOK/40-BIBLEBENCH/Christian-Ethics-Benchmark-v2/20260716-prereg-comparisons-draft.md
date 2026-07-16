# DRAFT — Pre-registered comparison list + multiplicity handling for v2 comparative claims (F11)

> **STATUS: DRAFT — NOT RATIFIED.** Owner (Jimmy) ratifies, amends, or strikes each
> numbered line. Until ratification, R1/R3 stand unchanged: **no comparative claim of
> any kind is reportable from v2 data.** (F11, 20260716 adjudication, SD-3.)
>
> **Data-dependency disclosure:** this draft was written 2026-07-16, AFTER the pilot,
> the F2 ablations, the cross-harness run, and the F3 offline analysis were read. It
> is not blind. Rule C9 (first-use) handles the consequence.

## 0. Trigger and scope

This document governs **any future comparative v2 claim** — SUT-vs-SUT,
design-vs-design, judge-vs-judge, or v1-vs-v2 harness claims promoted beyond
descriptive instrument evidence. Descriptive single-cell reporting under the R-rules
(point estimate + Wilson 95% + n/excluded adjacent) needs nothing from this file.

## 1. Pre-registered comparison families

- **C1 (primary family): per-design SUT contrasts on the primary metric, stratum-(a)
  cells only, on the corpus-distinctive sub-panel 04/05/10** (R7: the designs not
  discriminant vs generic RLHF harmlessness are 01/02/03/06/07/08/09). Family size
  for a 5-SUT roster: 3 designs × C(5,2) = 30 pairwise contrasts, or 3 omnibus
  tests + post-hoc pairs — owner picks ONE of the two shapes at ratification.
- **C2 (secondary family): the remaining designs (01/02/03/06/07/08/09) as
  R7-caveated contrasts** — every cell carries the "generic-harmlessness
  non-discriminant" caveat verbatim; never headlined alone.
- **C3 (stratifier, ratified 2026-07-16): divergence-split** (`banks/
  20260716-divergence-tags.jsonl`: 29 yes / 129 partial / 186 no). Usable in
  comparative headlines **with the calibration caveat attached verbatim**: per-design
  "partial" thresholds vary by tagger (04 = 29/33 vs 06 = 3/31 partial), so
  divergence-split contrasts are reported per-design or with `yes` vs `no` poles
  only; a pooled `partial` stratum is NOT a pre-registered cell.
- **C4 (instrument-stability preconditions, all comparative claims):**
  1. **2-judge rule (R4):** the contrast must hold in the same direction under
     judge-A and judge-B; a flip = "judge-sensitive — no SUT claim."
  2. **Certified judges only for 06/09 cells (R6/F5):** no comparative use of 06/09
     until the scoring judge passes G5 certification (`tools/audit/judge_certify.py`).
  3. **Same-family exclusion (R5):** cells where SUT and judge share a model family
     lean on the other judge explicitly.
- **C5 (minimum-n floors, R2):** multi-turn (02/07): <10 surviving ladders per
  (design, SUT) ⇒ insufficient-n, cell excluded from its family. Single-turn
  designs: <20 scored non-exemplar admins per cell ⇒ insufficient-n. Insufficient-n
  cells are listed, not compared, and do not shrink the multiplicity family
  (m is fixed at pre-registration, not after exclusions).
- **C6 (pinned classifier — REQUIRED by the F3 finding):** any comparative claim
  involving 02/07 pre-registers the branch classifier as part of the instrument:
  **model slug + provider + prompt template hash + route policy**
  (`solvers.py::_classify_branch` + `classifier_rubric`). The F3 offline replay
  showed route swaps change 24–56% (02) and 83–91% (07) of administered turns —
  a classifier change is an instrument change: results across different pinned
  classifiers are NOT comparable cells, they are different experiments. The pilot's
  pinned value: `openrouter/openai/gpt-4.1-nano` via the tasks' `judge_model`
  default. If F5 replaces judge-A, the classifier pin must be re-declared explicitly
  (inherit the new judge OR freeze nano) BEFORE any new 02/07 run.
- **C7 (exclusion-rate comparability, CV-7):** a pairwise contrast is void if the two
  cells' exclusion/refusal rates differ by >10 percentage points; report the
  exclusion rates adjacent and mark the cell "not directly comparable."

## 2. Multiplicity handling

- **Correction: blunt Bonferroni within each family** (per the adjudicated F11
  remedy — chosen for auditability, not power). α = 0.05 family-wise; per-contrast
  threshold = 0.05/m with m fixed by this document at ratification.
- Estimation language throughout: corrected CIs (Wilson for rates, normal-approx
  otherwise, widened by the Bonferroni factor); **no significance stars, no
  "significant" as an adjective** (R3 carries over).
- C1 and C2 are separate families (separate m); C3 stratified contrasts inherit the
  family of the metric they stratify and multiply m accordingly (a stratified C1
  contrast with 2 poles doubles that family's m).

## 3. First-use rule (C9)

Because this draft post-dates the pilot data: pre-registered comparisons run on
**new data** (new SUT runs or new banks) are reportable as pre-registered. The same
comparisons computed on the existing pilot logs are reportable only with an explicit
**"post-hoc on pilot data — hypothesis-generating"** label. No exceptions.

## 4. What ratification requires from the owner

1. Confirm or amend the C1 family shape (30 pairwise vs omnibus+post-hoc).
2. Confirm the C5 single-turn floor (proposed n≥20).
3. Confirm the C3 partial-stratum restriction (per-design / poles-only).
4. Confirm the C6 classifier pin policy when judge-A changes (inherit vs freeze).
5. Set α if not 0.05.

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content.
