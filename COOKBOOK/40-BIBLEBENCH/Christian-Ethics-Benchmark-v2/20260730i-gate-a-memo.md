# GATE A MEMO — Tier 0 complete; stop criterion FIRES; Tiers 1–3 stay closed

**Date:** 2026-07-30 · **Tier:** 0 closure (all work $0, offline, frozen run tree only)
**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content
**Authorization:** `RULINGS-APPLIED-20260729d.md` (Tier 0 of the repair queue); Gate A
criterion pre-committed in the plan of record and restated in
`20260730-boot-prompt-v3-tier0-continue.md` §2.

## 1. The pre-committed criterion, verbatim

> if no design shows a within-item contrast that is both unsaturated and
> judge-order-stable, STOP. Tier 0 alone is a publishable instrument-diagnostics result
> and needs no new instrument version. Stopping at Gate A forfeits nothing.

The criterion was pre-committed precisely so that this decision could be taken without a
fresh owner ruling. It is taken here.

## 2. The evidence, per candidate

| Surface | Unsaturated? | Judge-order-stable? | Source |
|---|---|---|---|
| d02 base vs cold_open, terminal-state rate | yes — 20 pooled cells span 0.157–0.694, none within 0.05 of a bound | no — 4 of 5 systems agree in direction (deepseek flips); Spearman rho 0.5643; per-epoch cross-judge agreement swings 0.95 / −0.05 / 0.80 | `20260730f` (T0-4) |
| d09 strict seat-A==seat-B rate | yes — all 10 cells in 0.588–0.814, none at ceiling | no — Spearman rho 0.40; one system moves three rank positions between judges | `20260730g` (T0-5) |
| d02 premium on break_turn (the previously stable-looking candidate, rho ≈ +0.7) | — | DISQUALIFIED — the effect is a ladder-length artifact: cold_open ladders have length 1, so the read-out admits only the values 0 and 1; documented as a rejected alternative | `20260730f` §6 (T0-4) |
| d07 arc conjunction and graded variants | no — the floor is real (levels 0.20–0.27 under grading; spread 0.0686) | moot; judge-B d07 labels additionally near-unusable | `20260729e` (T0-2) |
| d05 constraint satisfaction (judge-free) | no at item level — median 0.975, 12 of 32 items pinned at ceiling; and no within-item contrast exists (single-administration design); 0 of 10 SUT contrasts exclude zero under the pre-registered scope | trivially stable (no judge) | `20260730e` (T0-1), `20260730d` (T0-10) |
| d08 covert/overt gap | — | no — cross-judge rank correlation ≈ −0.5 (phase-7 record) | phase-7 adjudication record |
| Remaining judged paired designs (d01 twins, d03 say/do, d04 motive, d10 deservingness) | item-level spread exists for d01–d04 | no re-test at Tier 0; the phase-7 R4 result stands — eight of nine judged designs flip system ordering under judge swap | `20260725` phase-7 record; `20260730e` |

Corroborating item-level diagnostic (T0-1): outside the saturated designs, 67 items are
zero-information under at least one judge but only 6 under both — the judges do not agree
even on which items carry information. Order stability of any judged contrast has no
foundation to stand on at the item level either.

**No surface satisfies both prongs. The stop criterion fires.**

## 3. Decision

- **STOP at Gate A.** Tier 1 (taxonomy repair, judge-only rescores), Tier 2 (wide-gap
  probe), and Tier 3 (new items, format changes, bundled d02 version) remain CLOSED. No
  spend is authorized by this memo; nothing here opens a gate.
- **Holdout stays quarantined.** Gate B — worded as the holdout release condition — is
  never reached.
- **T1-3 (d07 anchor rescore) is formally retired**, per the T0-2 reconsideration duty:
  its premise (mislanding anchors caused the d07 floor) is refuted; its residual value was
  as a judge-B degeneracy probe, which is a judge-certification question, and Tier 1 is
  closed regardless.
- Per the pre-commitment, stopping forfeits nothing: Tier 0 stands alone as a publishable
  instrument-diagnostics result. Reopening any tier requires a new owner ruling.

## 4. What Tier 0 delivered (the diagnostics package)

| Item | One-line result | Artifacts |
|---|---|---|
| T0-2 | d07 floor is real, not a read-out artifact; judge-B d07 labels near-unusable (flat 76–85% across the ladder, 19.2% pole-to-pole disagreement) | `20260729e`, tools/audit/d07_arc_diagnostic.py |
| T0-7 | Premise false: exemplars are spec-bank items run live, not gold references — sub-ceiling exemplar scores indict nothing; scorer NOT referred. Byproducts: dropped slice is 97.7% hard (exclusion shifts judge-scored headlines up to −0.30, judge-free control −0.0005); metrics docstring misdescribes the data | `20260730b`, tools/audit/t0_7_exemplar_ceiling.py |
| T0-6 | All 36 d02 items carry keyed timing markers; no code parses them; the judge sees them as unparsed prose context | `20260730c`, tools/audit/t0_6_d02_marker_coverage.py |
| T0-10 | Published d05 "0 of 10" was computed pooled-strata but labeled pre-registered; stratum-a-only recompute gives the identical headline; relabeled with the merits argument made; C5 floor passes under the ratified admins wording | `20260730d`, tools/audit/t0_10_d05_stratum_contrasts.py |
| T0-1 | Full-bank per-item table: usable both-judge spread only in d01–d04; 67-vs-6 judge disagreement on informative items; WW-05-L01 coverage-starved, WW-03-L02 zero-pass, five d04 items twinless (true denominator 24) | `20260730e`, tools/audit/t0_1_item_difficulty_fullbank.py |
| T0-4 | d02 terminal-state contrast: unsaturated, not judge-order-stable; break_turn pairing artifact documented as rejected alternative | `20260730f`, tools/audit/t0_4_d02_terminal_state.py |
| T0-5 | 270 complete d09 triangles (the ~524 figure was a per-judge double-count); recomputed symmetry index is 0.69–0.91, not the in-log 1.0 artifact; strict A==B unsaturated in the predicted band but not judge-order-stable; the discarded arbiter leg is informative | `20260730g`, tools/audit/t0_5_d09_arbiter_triangle.py |
| T0-3 | Premise corrected: d03 has no SUT-side forced-choice parser — extraction operates on the judge's JSON; rate 0.9931 non-exemplar, minimum cell 0.9828, ep1 anchor 143/145; all six failures are one judge synonym-key defect | `20260730h`, tools/audit/t0_3_d03_extraction_rate.py |
| T0-8 | Instrument WW-v2-20260724b stamped and machine-verifiable (INSTRUMENT.json + tools/verify_instrument.py, 51/51 checks); found that the nano judge pin is a run-time override, not the code default (gpt-4.1-mini) — an unattended default run would be a different instrument | tools/SCHEMA.md §stamp, INSTRUMENT.json, tools/verify_instrument.py |
| T0-9 | 70 characterization tests pin current metric semantics (suite 33 → 103 green); 12 pinned-but-suspect behaviors catalogued, headline: the metric grouping key carries no sut/epoch, so cross-log pooling silently overwrites pairs | tests/test_metrics_characterization.py |

## 5. Corrections to planning premises made during execution

Recorded so no future session re-inherits them: exemplars are not gold references (T0-7);
the d09 triangle count is 270, not ~524, and the symmetry saturation at 1.0 was the
known-wrong in-log value, not the metric (T0-5); the d05 stratum-a cell is 19 bank items
and passes the ratified C5 floor — "n=18, not reportable" is refuted (T0-10); d03 has no
SUT-side parser and the ep1 anchor is 143/145 (T0-3); the metric module lives at
walkworthy_inspect/metrics.py, not tools/metrics.py.

## 6. Findings inventory for the instrument-diagnostics write-up

Judge-side: judge-B d07 label degeneracy (T0-2); judges disagree on which items are
informative, 67 vs 6 (T0-1); judge-B synonym-key JSON loss, six administrations (T0-3);
judge-B unparseable-verdict concentration (T0-1 coverage gaps). Bank-side: WW-05-L01 and
WW-03-L02 item-constant defects; five twinless d04 items; d02 keyed timing markers unread
but judge-visible (T0-6). Metric-side: exemplar exclusion is difficulty-skewed (T0-7);
grouping-key pooling hazard and the further T0-9 catalogue; break_turn single-turn
degeneracy (T0-4, pinned by test). Provenance-side: the nano pin is an override, not the
default (T0-8); published d05 scope label corrected (T0-10). Any promotion of any
alternative read-out remains a new instrument version by standing rule; none is proposed.

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content
