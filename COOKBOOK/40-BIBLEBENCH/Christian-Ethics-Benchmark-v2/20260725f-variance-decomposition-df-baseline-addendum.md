# ADDENDUM — df-proportional baseline for the variance decomposition (successor to `20260725b-variance-decomposition-addendum.md` §3)

**Date:** 2026-07-25 · **Session:** phase-7 (boot prompt `20260725d-boot-prompt-phase7-claims-adjudication.md`)
**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content
**Supplements:** `20260725b-variance-decomposition-addendum.md` (immutable, not edited).
All of its *numbers* stand — two independent reviewers recomputed every percentage and
conceded them. What changes is §3's *reading*, per `RULINGS-APPLIED-20260725c.md`
RULING 1 (escalation Q3, verified in
`REPORTS/20260725-manuscripts/20260725-ESCALATION-claims-validity.md` §4.3).

---

## 1. The reference line

Sums of squares are non-negative and, under a null of no effect, have expectation
proportional to degrees of freedom. In the balanced 5 (SUT) × 2 (judge) layout with
3 epochs as replicates — `SS_total (df 29) = SS_SUT (4) + SS_judge (1) + SS_SUT×judge (4)
+ SS_error (20)` — the no-effect expectations are:

| Term | df | E[share] under no effect |
|---|---:|---:|
| SUT | 4 | **13.79%** |
| judge | 1 | 3.45% |
| SUT × judge | 4 | **13.79%** |
| error | 20 | 68.97% |

**R3 discipline (binding):** this is a descriptive expectation, not a test. No p-value,
no rejection decision, no significance language attaches to it. Shares are "above/below
the df-proportional reference line" — never "significant".

## 2. The judged, non-saturated designs against the line

| design | SUT×judge | vs 13.79% | SUT | vs 13.79% | corrected note |
|---|---:|---|---:|---|---|
| 02 | 46.5% | above | 5.8% | below | strongest genuine interaction case; near-absent model signal |
| 08 | 25.9% | above | 9.1% | below | `protected→steamrolled` boundary, quantified |
| 10 | 25.8% | above | 25.8% | above | interaction equals the model effect |
| 01 | 23.0% | above | 45.4% | above | **the only surviving "large SUT effect, judges still reorder it" exemplar** |
| 06 | 11.4% | **BELOW** | 63.4% | above | interaction below epoch noise; its flip is one adjacent transposition (τ = +0.80, ep1) |
| 09 | 9.9% | **BELOW** | 54.4% | above | interaction below epoch noise; ep3 ordering is tie-affected |
| 04 | 4.9% | **BELOW** | 46.3% | above | |
| 03 | 1.4% | **BELOW** | 6.6% | below | judge *level* shift (88.8%) with ~no interaction — unchanged special case |

(Design 07 is floor-saturated and excluded, as in the predecessor; design 05 is
judge-free by construction.)

## 3. What §3 of the predecessor must now be read as saying

1. **"non-zero in 8 of 8 judged designs" is WITHDRAWN as an evidential claim.** A sum of
   squares on a continuous metric is almost surely non-zero; the statement carries no
   information. Four of the eight interactions (03, 04, 06, 09) sit at or below the
   13.79% line — at or below what pure epoch noise produces.
2. **The "large SUT effect, judges still reorder it" narrative is restricted to design
   01.** Designs 06 and 09, previously listed alongside it, have below-line interactions;
   their R4 failures rest on the flip result, reported in graded form (RULING 2) with
   the transposition/tie qualifications above.
3. **"The models genuinely differ" is design-specific, not suite-wide.** %SUT is below
   the line in designs 02, 03 and 08.
4. **What is unchanged:** do NOT write "the judge dominates" — judge and SUT footprints
   remain comparable at the median (35.3% vs 35.6%). And the operational conclusion —
   **no SUT-vs-SUT claim is licensed** — is untouched; it rests on the ordering flips
   and the judge-free surface's 0-of-10, neither of which involves the interaction term.

The corrected suite-wide framing:

> *The models differ on most designs. On a minority of designs the judges clearly
> disagree about the ordering; on the rest the systems are too tightly spaced for either
> judge to resolve. Either way, no comparative claim survives the swap.*

## 4. Independent corroboration from the positive control ($0, verified)

Design 05 is judge-free: its two judge levels are exact duplicates, so the layout
collapses to 5 (SUT) × 3 (epoch) — `SS_total (df 14) = SS_SUT (4) + SS_error (10)` —
giving **E[%SUT] = 4/14 = 28.6%** under no effect. Observed: **%SUT = 27.4%.** The
positive control's own system main effect sits at its null expectation. This
independently corroborates the run report's 0-of-10 contrast result: the judge-free
surface genuinely does not separate these five systems, and no concealed ranking hides
behind the judged designs' disagreements.

---

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content.
