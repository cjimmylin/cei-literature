# RULINGS-APPLIED — 2026-07-24e: design-02/07 classifier lineage + phase-5 spend GO

**Date:** 2026-07-24 · **Session:** phase-5 (boot prompt `20260724c-boot-prompt-phase5-fullbank-rescore-3ep.md`)
**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content
**Governance:** C6 / RULING 1d (pinned classifier) + PF-003 (spend gate)
**Spend memo:** `20260724d-spend-memo-fullbank-3ep.md`

---

## Why a ruling was needed

Two owner rulings issued on 2026-07-16 pointed in different directions for a run of
this kind, and the code makes them mutually exclusive:

- `20260716-prereg-comparisons-RATIFIED.md` **C6 / RULING 1d** — the branch-classifier
  pin **freezes at `gpt-4.1-nano`** for the current instrument lineage.
- `20260716-design02-classifier-pin-decision.md` — the **v-next** design-02 instrument
  **re-pins to a cross-family classifier** (`mistral-small-3.2` or
  `gemini-2.5-flash-lite`), never nano, on the F3 evidence that nano is the
  cross-family outlier (alt–alt agreement 0.902 vs alt–nano 0.685–0.721; on 24.4% of
  branch turns both alternatives agree against nano, concentrated in design-02
  `refused→complied` swaps).

`tasks/design02_twomasters.py` and `tasks/design07_seventyseven.py` both construct
`multiturn_ladder_solver(classifier_model=judge_model)` — **the classifier *is* the
judge model**, with no separate task parameter. Satisfying the v-next re-pin while
keeping judge-A = nano is therefore impossible without a code change, which the
phase-5 boot prompt fences (F11: stop, owner rules first).

The question was surfaced pre-spend rather than resolved by default because
`pushback_rate` — the metric this run exists to gather per-judge evidence on — is a
**design-02** metric, and design-02 is exactly where the nano classifier is documented
to misroute.

## Ruling — Option A

**The branch classifier stays pinned at `openrouter/openai/gpt-4.1-nano`.**

1. The phase-5 full-bank run is the **CURRENT instrument lineage**, governed by
   C6/RULING 1d. Judge-A and the 02/07 branch classifier are both nano, exactly as in
   the 2026-07-16 pilot and the 2026-07-24 smoke.
2. Design-02 (and 07) cells from this run carry the **nano refused-overcall as a
   documented instrument property**, cited to `20260716-f3-crossfamily-classifier-results.md`
   and `20260716-design02-classifier-pin-decision.md` — the same treatment the pilot
   cells already receive.
3. The **v-next cross-family re-pin remains UNFIRED** and available as a future,
   distinct instrument version. It is not cancelled by this ruling; it is deferred.
   Firing it will require its own session, its own F11 ruling, a `classifier_model`
   task-parameter decoupling, and its own C9 line.
4. **C6 no-cross-classifier-pooling continues to bind**: cells from this run may never
   be pooled with cells produced under any future cross-family pin.

## Spend GO

**Authorized: ceiling $16.00** (expected all-in $10.90) for the phase-5 ARM 1 run —
public bank rev 2026-07-24b, 10 designs × 5 SUTs × 3 independent single-epoch runs,
judge-A inline plus a full judge-B rescore pass. Basis and derivation in
`20260724d-spend-memo-fullbank-3ep.md` §4.

The authorized ceiling is **below** the boot prompt's carried ~$25 proposal because the
bottom-up model — exact token counts from the 50 pilot eval logs re-priced at live
2026-07-24 prices — came in under its $14–17 forward projection. The method reproduces
the pilot's recorded $2.73 (SUT + judge-A + classifier) and ≈$0.90 (judge-B) figures.

**Excluded from authorization:** the holdout (quarantine intact); any bank, rubric, or
metric edit; any SUT-roster change.

## Non-changes

- No bank edit, no rubric edit, no metric-formula edit, no code change. Bank revision
  stays **2026-07-24b**; the 33-test suite is untouched.
- Prior rulings untouched: `RULINGS-APPLIED-20260724.md` / `-20260724b.md` (PE waves),
  `-20260724c.md` (design-08 rubric anchor), `-20260724d.md` (`pushback_rate` A′
  reporting surface — binding on this run's report).

---

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content.
