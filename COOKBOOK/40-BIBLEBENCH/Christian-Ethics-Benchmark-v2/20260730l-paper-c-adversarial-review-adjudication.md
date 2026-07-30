# Paper-c adversarial review — adjudication record + Gate A memo corrections

**Date:** 2026-07-30 · **Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content
**Scope:** adjudication of the refute-first review of
`REPORTS/20260730k-diagnostics-manuscript/20260730k-paper-c-instrument-diagnostics-v0.1.md`
(committed pre-review at `af8845cd8`), and successor corrections to two defects the review
surfaced in the immutable `20260730i-gate-a-memo.md`.

## 1. Review outcome and adjudication

Refute-first review returned 4 blocker, 7 major, 12 minor findings; verdict "does not
survive as v0.1; all blockers locally repairable; re-submit as v0.2." The reviewer's
failed-attack list independently reproduced the core quantitative structure (rank
statistics including the tie correction, zero-information union, coverage gaps,
extraction figures, triangle inventory, stamp verification live at 51 of 51).

**Adjudication: all 23 findings ACCEPTED; none refuted.** Two carry modifications:

- **Finding 11 (escalated to the main loop): the d02 measure substitution.** The reviewer
  asked whether replacing the break-position premium with the terminal-state rate was a
  construct disqualification or an undisclosed pre-registration deviation. RULING: not a
  deviation. `RULINGS-APPLIED-20260729d.md` (lines 81–86) — the same document that
  committed the tier/gate structure — already disqualifies the break-position read-out on
  construct grounds (degenerate support at ladder length 1) and names the terminal-state
  statistic as T0-4's read-out. The substitution was pre-committed jointly with the gate,
  before any Tier 0 execution. It is additionally outcome-irrelevant: on the committed
  full-bank data the disqualified read-out's own cross-judge rank agreement is 0.00
  (Kendall −0.20, recomputed by the reviewer from the committed table), so gate prong (b)
  fails on the d02 surface under either measure. The paper discloses all of this rather
  than asking the reader to infer it.
- **Finding 18 (anonymization pretense):** resolved by naming the system plainly in prose
  (gpt41mini's three-rank move). The claims frame forbids comparative ethics claims, not
  the naming of systems in diagnostic rank statements; the adjacent tables name it anyway.

All fixes applied to the manuscript in place (house manuscript practice: papers are
living files edited under version banners; the internal version advances to v0.2,
filename unchanged, as with paper-a).

## 2. Successor corrections to `20260730i-gate-a-memo.md` (immutable; corrected here)

1. **§2 evidence table, d02 premium row — "rho ≈ +0.7" is a planning-era figure and is
   not reproducible from the committed run data.** It entered the memo from the
   2026-07-30 boot prompt, which carried it from pre-Tier-0 planning material. On the
   committed full-bank table (`20260730f` §6) the break-position premium's cross-judge
   rank agreement is Spearman 0.00 / Kendall −0.20. The memo row's CONCLUSION
   (disqualified as ladder-length artifact) is unaffected — indeed strengthened: the
   artifact was never judge-order-stable on the run data; its apparent stability lived
   entirely in sign uniformity.
2. **§2 evidence table, d05 row — "12 of 32 items pinned at ceiling" has the wrong
   denominator.** The 12 ceiling items were counted over the 28 non-exemplar design-05
   items (`20260730e` §3); 32 is the full bank count including 4 exemplar items. Correct
   statement: 12 of 28 non-exemplar items.

Neither correction changes the Gate A decision: both affected rows argued AGAINST the
d02 premium and AGAINST d05 as gate-satisfying surfaces, and both corrections argue in
the same direction more strongly.

## 3. Two source-report prose defects noted (tables are authoritative)

- `20260729e` §2 prose says judge-B d07 labels sit "flat at 76–85%"; its own table's
  range is 68.1–85.5 (minimum at turn 3). The no-gradient finding is unaffected.
- The universal "every audit script carried a G0 gate" formulation (memo §4 framing as
  inherited by the draft) holds for the six items that recompute from the frozen run
  tree (T0-1, T0-2, T0-4, T0-5, T0-7, T0-10); T0-6/T0-8/T0-9 are tree/bank reads with
  no recomputed quantity to gate, and T0-3's stated anchor was corrected rather than
  reproduced. The paper now states the six-of-ten form.

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content
