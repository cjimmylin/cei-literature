# RULINGS-APPLIED — 2026-07-24d: `pushback_rate` reporting-surface ruling (phase-4 ARM 3)

**Date:** 2026-07-24 · **Session:** phase-4 (boot prompt `20260724b-boot-prompt-phase4-next-arms.md`)
**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content
**Governance:** F11 (instrument/reporting-surface change) + C9 (comparability line)
**Options memo:** `20260724c-pushback-rate-promotion-options-memo.md`

---

## Ruling

**Owner ruled Option A′** (2026-07-24, via in-session menu): `pushback_rate` is
promoted from diagnostic sub-metric to the **reported design-02 surface as a
SECONDARY metric**, under these binding conditions:

1. **Per-judge only, never pooled across judges.** Every reported `pushback_rate`
   cell names its judge; no cross-judge aggregate is ever printed (consistent with
   R4 two-judge discipline and C6 no-cross-classifier-pooling spirit).
2. **Standing caveat travels with every report of the metric** until measured:
   "cross-judge stability of `pushback_with_alternative` is untested; all
   pre-2026-07-24b figures are single-judge (judge-A era)."
3. **`break_turn` remains the sole design-02 headline.** Headline status for
   `pushback_rate` is explicitly NOT granted; it is re-decided on evidence after a
   full-bank two-judge run (phase-4 ARM 1, separately gated) measures per-judge
   stability of the state.
4. **C9:** this ruling defines the design-02 reporting surface from bank rev
   2026-07-24b forward. Pilot-era first-look figures
   (`20260724-pushback-rate-first-look.md`) remain C9-fenced descriptives of the
   2026-07-16 run and are not comparable cells.

## What was applied

- No code change required: `metrics.py` (post-PE-18) already computes and emits
  `pushback_rate`, `pushback_turns`, `pushback_scored_turns`; the smoke rescore
  (`20260724-changed-items-smoke-report.md`) verified the channel live. This ruling
  changes only what future REPORTS must print.
- Binding on: any future run report on rev 2026-07-24b+ (including the ARM 1
  full-bank report, if authorized), and the paper's §7/§8 treatment of design-02.
- Evidence base at ruling time: first-look (pushback_rate 0.13–0.24/SUT; 32.7% of
  old hold-mass, range 21.8–45.8%; break_turn invariance delta 0.000000 × 344),
  S1-A (50/83 referee both-neither cells touch the state; recommended
  un-collapsing), smoke PE-18 live verification. Full option analysis in the memo.

## Non-changes

- No bank edit, no rubric edit, no metric-formula edit. Bank revision stays
  **2026-07-24b**. No test-suite impact (33/33 unaffected).
- Prior rulings untouched: `RULINGS-APPLIED-20260724.md` / `-20260724b.md` (PE
  waves), `-20260724c.md` (design-08 rubric anchor).

---

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content.
