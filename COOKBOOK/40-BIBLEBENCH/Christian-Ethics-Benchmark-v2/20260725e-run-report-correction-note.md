# CORRECTION NOTE — successor to `20260725-fullbank-3ep-run-report.md` (flip count)

**Date:** 2026-07-25 · **Session:** phase-7 (boot prompt `20260725d-boot-prompt-phase7-claims-adjudication.md`)
**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content
**Corrects:** `20260725-fullbank-3ep-run-report.md` §0 (headline item 1) and §3 (flip
table, design 07 rows). That report is **immutable and is not edited**; this note is the
authoritative correction. Adjudicated in `RULINGS-APPLIED-20260725c.md` (escalation Q1,
verified in `REPORTS/20260725-manuscripts/20260725-ESCALATION-claims-validity.md` §4.1).

---

## What the report says

§0 item 1: *"Nine of ten designs flip their SUT ordering between judge-A and judge-B.
The one design that never flips (05) is the one whose primary metric never touches a
judge."* §3's table likewise records design 07 as "flips" in all three epochs.

## What is wrong with it

**Design 07 has no judge-A ordering to flip.** Its judge-A `arc_pass_rate` is identically
0.0000 on all five systems in epochs 1 and 2, and 0.0370/0/0/0/0 in epoch 3. The A-side
"ordering" the swap tool prints is Python's stable sort falling back to system load
order — an artifact, not a measurement. The tool's `JUDGE-SENSITIVE (order flips)` flag
for design 07 is therefore vacuous: a floor yields no permutation to preserve.

## The correct statement

> **Eight of the nine judged designs flip their SUT ordering between judge-A and
> judge-B. The ninth judged design (07) is floor-saturated under judge-A and yields no
> ordering to test (ORDER-UNDEFINED). Design 05, the judge-free design, is the tenth
> and does not flip by construction.**

## What is unaffected

The report's conclusion — no SUT-vs-SUT comparative claim is supported — is *unchanged*
and if anything reinforced: the correction removes a vacuous cell, not evidence. The
0-of-10 result on design 05's judge-free surface, all variance-decomposition numbers,
C1 intervals, spend, and bank census are untouched. Design 07's floor-saturation was
already documented in the report itself; the defect was only that the flip headline did
not exclude it.

Graded flip verdicts (Kendall's τ per design × epoch, with tie flags) supplement the
binary verdicts per `RULINGS-APPLIED-20260725c.md` RULING 2; see
`logs/fullbank-3ep-20260724/20260725-kendall-tau.txt`.

---

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content.
