# WALKWORTHY v2 — Options memo: `pushback_rate` reporting-surface decision (phase-4 ARM 3)

**Date:** 2026-07-24 · **Status:** OPTIONS MEMO — owner ruling required (F11/C9 governed)
**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content

---

## 1. The decision

Whether `pushback_rate` (design-02 `pushback_with_alternative` turns / scored turns) is
promoted from a diagnostic sub-metric to a **reported** design-02 quantity in future
runs, alongside the headline `break_turn`. This is a reporting-surface instrument
change: governed under F11 (instrument changes need an owner ruling) and C9 (whatever
surface is chosen becomes the comparability line for future runs). Outcome to be
recorded in a new dated `RULINGS-APPLIED-20260724d.md`.

## 2. Evidence base

1. **First-look** (`20260724-pushback-rate-first-look.md`, $0 offline re-aggregation of
   the 2026-07-16 pilot logs): pushback_rate 0.1297–0.2428 per SUT (pooled 0.1855);
   **32.7% of the old undifferentiated hold-mass (range 21.8–45.8% per SUT) is the
   third-way state**; break_turn invariance proven exactly (stored pilot scalars ≡
   recompute, delta 0.000000 × 344 scored samples) — surfacing the state adds signal
   without disturbing the headline.
2. **S1-A taxonomy** (`REPORTS/20260718-item-assessment/20260718-08-substudies.md`):
   50 of 83 referee both-neither cells in the design-02 judge audit touched
   `pushback_with_alternative`; S1-A recommended un-collapsing it. This cuts both
   ways — the state is construct-relevant *and* it sits in the zone where the shipped
   judges and referees disagree most.
3. **Smoke instrument verification** (`20260724-changed-items-smoke-report.md`):
   PE-18 pushback_rate emits nonzero, plausible values live on bank rev 2026-07-24b
   (105/105 invocations) — the channel works end-to-end post-fix.

**Standing caveat (first-look footer):** every stored verdict behind item 1 is
single-judge (judge-A era). **Cross-judge stability of the state is untested.** The
full-bank two-judge run (phase-4 ARM 1, separately gated) is precisely the experiment
that would measure it.

## 3. Options

- **(A) PROMOTE to headline.** `pushback_rate` reported alongside `break_turn` as a
  design-02 headline in all future runs.
  *For:* the state is ~1/3 of hold-mass — leaving it unreported hides known
  construct-relevant signal; metric verified live; break_turn undisturbed.
  *Against:* commits the headline surface to a state whose judge-stability is
  unmeasured, on a design whose per-turn judge agreement is the bank's worst
  (0.21–0.26 A/B); if the state proves judge-fragile, a headline retraction is a C9
  event.

- **(A′) PROMOTE as reported secondary, per-judge only** *(recommended)*.
  `pushback_rate` joins the reported design-02 surface as a secondary metric:
  always reported **per judge, never pooled across judges**, carrying a standing
  "cross-judge stability untested" caveat until a full-bank two-judge run measures
  it — at which point headline status is re-decided on evidence.
  *For:* reports verified signal honestly; per-judge discipline matches R4; leaves
  the headline surface (break_turn) untouched, so no retraction risk; creates the
  exact evidence path (two-judge full-bank cells) for the final headline call.
  *Against:* a two-tier reported surface is slightly more complex to present.

- **(B) KEEP DIAGNOSTIC.** Computed and logged, not reported.
  *For:* zero surface commitment before judge-stability evidence.
  *Against:* knowingly leaves ~1/3 of hold-mass invisible in reported output after
  S1-A explicitly recommended un-collapsing it; the metric was fixed (PE-18) largely
  to surface this.

- **(C) DEFER.** No ruling until post-full-bank evidence.
  *For:* maximally conservative.
  *Against:* operationally identical to (B) but leaves the surface ungoverned — if
  ARM 1 runs first, its report would have to improvise the surface anyway.

## 4. Recommendation

**(A′).** The first-look establishes the state is real and large; S1-A establishes it
is judge-contested; the honest surface reports it per-judge with the caveat, and defers
only the *headline* question to the two-judge evidence that ARM 1 would generate.

---

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content.
