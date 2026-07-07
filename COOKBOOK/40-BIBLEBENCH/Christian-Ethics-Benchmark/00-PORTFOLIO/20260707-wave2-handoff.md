# WALKWORTHY Wave-2 Handoff — 2026-07-07 (dual-tier doubling session)

<!-- WALKWORTHY-CANARY-7f3e2026 -->
Reads with: `20260706-session-handoff.md` (wave-1/v1 state — still authoritative for everything not superseded here).

## What this session did

Doubled every seed bank per Jimmy's directive, using **both Fable and Opus subagents** with provenance tagging, then ran the full quality cycle (cycle-2 adversarial review → Fable adjudication → revisions).

| Bank | Items (was → now) | Wave-2 split (Fable/Opus) |
|------|-------------------|---------------------------|
| 01 GOODSAMARITAN | 33 → 66 | 16 / 17 |
| 02 TWOMASTERS | 27 → 54 | 13 / 14 |
| 03 QUIETTONGUE | 22 → 44 pairs | 11 / 11 |
| 04 INNERWEIGHT | 22 → 44 | 11 / 11 |
| 05 ORDOAMORIS | 21 → 42 | 10 / 11 |
| 06 CROOKEDPATH | 20 → 40 | 10 / 10 |
| 07 SEVENTYSEVEN | 20 → 40 | 10 / 10 |
| 08 VOCATIONFORK | 22 → 44 | 11 / 11 |
| 09 DOUBLEEDGE | 23 → 46 | 11 / 12 |
| 10 STRANGERGATE | 21 → 42 | 10 / 11 |
| **Total seeds** | **231 → 462** | **113 / 118** |

Grand total with the 41 spec exemplars: **~503 test cases**. Every wave-2 item carries `wave: 2` + `author_model: fable|opus` frontmatter.

**Division of labor:** Fable subagents wrote the hard end (all stratum-c/DSP dispute keying, L3 implicit cues, tragic-tightness allocations, 10-rung ladders, pattern-salience embeds, three-way seat structures, matched reference-answer pairs); Opus subagents wrote the standard-hard majority + the easy calibration floors.

## Cycle-2 quality results

- **Review:** 10 independent Opus reviewers, wave-2 scope → **190 PASS / 41 REVISE / 0 KILL (17.7%** vs cycle 1's ~32%). Every cycle-1 systemic failure class independently verified FIXED (outcome identity, seat rendering, token floors, neutrality parity, cost binding, L1 hygiene).
- **Adjudication:** `REVIEWS/20260707-fable-adjudication-2.md` — rulings FA2-1…FA2-6 incl. two new playbook lints (**L8** no direct-Scripture anchors; **L9** citation-gloss integrity) and a design-10 spec amendment (**magnanimity-signalling** contempt subtype).
- **Revisions:** all 41 ratified fixes applied + bank-wide load-bearing citation-gloss sweeps (which caught ~20 additional drifts beyond the reviews); arithmetic re-verified in 05; cycle-2 revision logs in every bank.

## Author-tier provenance result (first data point — record for the paper)

Fable-authored ≈18% revise (20/113) vs Opus-authored ≈18% (21/118): **equal defect rates at unequal ambition** — the Fable sections carry the structures cycle 1 showed Opus could not write reliably (dispute keying, ambiguity-keyed pairs, L3 cues), and the cycle-1 lesson-feed demonstrably lifted Opus quality. The interesting question — do Fable-authored items *discriminate* better on a live panel? — is pre-specified as analysis cell in master plan §4 (extend headline H with an author_model factor).

## Deltas to the v1 handoff's "what remains"

- Session O1 (bank completion) is now largely DONE by this session; O1 shrinks to: holdout split (now over 462 items), easy-share backfill for banks 09/10 (~30% target; never by softening — FC-4), the O1-deferred advisory list in `20260707-fable-adjudication-2.md` §C, and the residual wave-1 gloss items flagged by the 05/09 sweeps.
- Everything else in the v1 handoff stands: O2 harness → O3 pilot → O4 panel → O5 gates (frozen) → O6 findings; Jimmy owes keys + human labels; contested tier still deliberately empty.

## Session history note

Two session-limit kills hit mid-fan-out (drafting phases); both recovered losslessly via on-disk state + checkpoint commits (`08f7e57d8`, `84917b606`). One API-overload kill (06 continuation) relaunched cleanly.
