# RULINGS-APPLIED — 2026-07-25: `pushback_rate` headline re-decision CLOSED (A′ affirmed)

**Date:** 2026-07-25 · **Session:** phase-5 (post-run)
**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content
**Governance:** discharges condition 3 of `RULINGS-APPLIED-20260724d.md` (the A′ ruling)
**Evidence:** `20260725-fullbank-3ep-run-report.md` §4

---

## What was deferred

`RULINGS-APPLIED-20260724d.md` (A′) promoted `pushback_rate` to the reported design-02
surface as a SECONDARY metric and explicitly withheld headline status, condition 3:

> `break_turn` remains the sole design-02 headline. Headline status for `pushback_rate`
> is explicitly NOT granted; it is re-decided on evidence after a full-bank two-judge
> run (phase-4 ARM 1, separately gated) measures per-judge stability of the state.

That run executed 2026-07-24/25 (150/150 eval runs, 15/15 judge-B passes, full public
bank rev 2026-07-24b × 5 SUTs × 3 epochs). **The condition-3 trigger is met.**

## The evidence

1. **Within-judge epoch stability is good.** Epoch ranges 0.020–0.073 for both judges;
   the metric is not stochastically noisy at full bank.
2. **Cross-judge level shifts materially.** Judge-B reads pushback higher on four of
   five SUTs: gemini +0.111, llama +0.092, mistral +0.090, gpt-4.1-mini +0.018;
   deepseek flat (−0.008).
3. **Cross-judge ordering does not hold.** Judge-A: deepseek ≫ llama ≈ gemini >
   gpt-4.1-mini > mistral. Judge-B: gemini > llama ≈ deepseek ≫ mistral ≈ gpt-4.1-mini.
   deepseek 1st→3rd, gemini 3rd→1st, gpt-4.1-mini 4th→5th, mistral 5th→4th.
4. **The instability sits on the state's own definitional boundaries.** The two largest
   design-02 disagreement transitions both involve the pushback state:
   `holds_line → pushback_with_alternative` ×142 (13.6%) and
   `pushback_with_alternative → material_concession` ×127 (12.2%) — contested from both
   the "held" and the "conceded" side.
5. **Context:** design 02 is the most judge-fragile instrument in the suite (exact
   primary-field agreement 0.232), and its `SUT × judge` interaction accounts for
   **46.5%** of headline variance versus a 5.8% SUT main effect
   (`20260725b-variance-decomposition-addendum.md`).

## Ruling

**Owner ruled: AFFIRM A′ and CLOSE the deferred decision** (2026-07-25, in-session).

1. **`break_turn` remains the sole design-02 headline.** Permanently for this instrument
   lineage — not "pending further evidence."
2. **`pushback_rate` remains a SECONDARY reported metric**, under the unchanged A′
   disciplines: per-judge only, never pooled across judges, every cell naming its judge.
3. **The standing caveat continues to travel with every report of the metric:**
   "cross-judge stability of `pushback_with_alternative` is untested; all
   pre-2026-07-24b figures are single-judge (judge-A era)." The phrase "untested" may now
   be read as "tested and found judge-dependent" where a report cites this ruling.
4. **Condition 3 of the A′ ruling is DISCHARGED.** No further re-decision is pending. Any
   future proposal to headline `pushback_rate` requires new evidence and a new ruling —
   it is not an open queue item.

## Rationale

The evidence supports precisely the disciplines A′ already imposed. A metric that is
stable within a judge but reorders its subjects between judges is reportable as a
per-judge descriptive cell and is not reportable as a headline, because a headline
implicitly licenses cross-cell comparison. Promotion was not supported; demotion was not
warranted either, since the metric is well-behaved within judge and surfaces a real
design-02 state (the "third way") that `break_turn` alone renders invisible.

## Non-changes

- No bank edit, no rubric edit, no metric-formula edit, no code change. Bank revision
  stays **2026-07-24b**; 33/33 tests unaffected.
- Prior rulings untouched: `-20260724.md` / `-20260724b.md` (PE waves), `-20260724c.md`
  (design-08 rubric anchor), `-20260724d.md` (A′ — this ruling discharges its condition 3
  but does not amend its surface), `-20260724e.md` (classifier lineage + spend GO).
- The v-next cross-family classifier re-pin remains UNFIRED and deferred.

---

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content.
