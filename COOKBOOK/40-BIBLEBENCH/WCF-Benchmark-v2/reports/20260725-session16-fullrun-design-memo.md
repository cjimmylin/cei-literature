# WCF-Benchmark-v2 — Full-Run Design Memo (session 16 → STOP-POINT 4)

**Date:** 2026-07-25 · **Status:** DESIGN — terminates at **STOP-POINT 4 (full-run
authorization: roster, epochs, caps), expected s17**. All pilot numbers herein are
EXPLORATORY / NON-QUOTABLE; they inform design only.

## 0. Gating prerequisite (from the B3 STOP ruling)

**No full run may launch until the strict-v3 candidate instrument passes the 20-cell
successor bench** (`analysis/20260725-session16-truth-bench-v2.json`; template
`src/templates/wcf_grade_template_strict_v3.txt`, sha256 `ce5c9fa5…`). s17 act 1:
both judges × 20 cells × single-packet mode ($0, ~1–2 h), Fable adjudicates.
Auto-revert rule: if ANY cell the s15 bench passed under strict-v2 degrades, revert
to strict-v2 + Sol-anchored disclosure and re-present the trade-off at STOP-POINT 4.
A strict-v3 pass RESTARTS the freeze (new manifest, judge-mode versioning rule);
the A3 stability study transfers only if the owner rules the deltas immaterial —
default: re-run the 120-verdict repeat study under v3 ($0, ~1 h) before quoting an
instrument-reliability number.

## 1. Measured pilot actuals (the three numbers this memo is built from)

| Quantity | Measured value | Source |
|---|---|---|
| SUT sampling cost | $1.96 real / $2.68 guard-priced for 438 responses (146×3) | `logs/20260724-session16-pilot/RUN-SUMMARY.json` |
| — per item: minimax-m3 | ~$0.0114 (74/146 items ran long: 743K completion tokens total) | same |
| — per item: gpt-5-mini | ~$0.0066 | same |
| — per item: gpt-4o-mini | ~$0.0004 | same |
| SUT sampling wall-clock | ~33 min for 438 calls, 8 workers, 0 failures | same |
| Opus judge throughput | 426 verdicts in ~29 min ≈ **890/hr** (background workflow fan-out, fresh context per verdict, $0) | workflow wf_c2765a22 |
| Sol judge throughput | mean 52 s/verdict ≈ **70/hr/stream**; 4 streams = **~280/hr**, $0, 0 parse failures in 876 total pilot verdicts | sol-stream logs |
| Cross-SUT validity | 7/10 audited cells clean; 2 new opus trap idioms → B3 STOP (ruled: strict-v3) | `/tmp/wcf-s16-b3-meta/SELECTION.json` + audits |

Sol is the wall-clock bottleneck, as predicted; opus via workflow fan-out is ~3×
faster than Sol at 4 streams and is not the constraint.

## 2. Scope constants

- Bank v2.5 main = 345; **G4 policy (STOP-POINT 3, ruled 2026-07-25): keep the 28
  exclusions frozen and disclose** → scored set = **317 items** (or 146 frontier
  core). Episodes (22) default OUT.
- Epochs: s7 precedent ×3 for paired significance.
- Judging mode: single-packet per fresh context ONLY (frozen canonical; batch mode
  unvalidated and now known to shift opus scores).
- Standing regrades wired into the full run, not the pilot: **5-AGG regrade**
  (s11 gold_order char-split fix at `wcf_tasks.py:96`) and the **fitness re-check**
  (does fit-now rise from 84?).

## 3. Costed scenarios (SUT cost ±50% on unmeasured SUTs; judge cost $0 throughout)

Roster pool: qwen3.7-plus + haiku-4.5 (gate-characterized), gpt-5-mini, minimax-m3,
gpt-4o-mini (pilot-characterized). qwen/haiku per-item costs are estimates
(~$0.005/$0.008) pending their first sampled run.

| Scenario | Shape | Responses | Verdicts (×2 judges) | SUT cost est. | Sol wall (4 str / 8 str) | Opus wall |
|---|---|---|---|---|---|---|
| **A (recommended)** | 5 SUTs × 317 × 3 ep | 4,755 | 9,510 | ~$28–35 | ~34 h / ~17 h | ~5.3 h |
| B (lean bank) | 5 SUTs × 146 core × 3 ep | 2,190 | 4,380 | ~$13–16 | ~15.6 h / ~7.8 h | ~2.5 h |
| C (lean roster) | 3 SUTs (mmx, 5-mini, qwen) × 317 × 3 ep | 2,853 | 5,706 | ~$20–24 | ~20.4 h / ~10.2 h | ~3.2 h |

Sol wall-clock levers (present measured options, owner picks at STOP-POINT 4):
1. **More streams** — 8 streams halves the wall if OAuth rate limits tolerate it
   (untested above 4; test with a 30-min probe before committing).
2. **Sol on 1 epoch + opus on all 3** — panel mean-of-2 quotable on epoch 1;
   epochs 2–3 opus-only used ONLY for paired stability/sensitivity, never pooled
   with panel numbers (instrument-versioning discipline). Cuts Sol to ~11 h (A).
3. **Paid API judge with cap** — replaces the OAuth channel; violates the
   $0-judge precedent and adds an unvalidated judge identity; NOT recommended.

Run plan per scenario: resumable SUT runner (extend `session16_pilot_runner.py`
patterns; cost guard = 2× estimate hard cap), packets via the frozen renderer (new
dated script), opus via background workflow (~900/hr), Sol via N background
streams, dual-arm aggregation script, per-judge sensitivity + paired-epoch
significance per s7/s8 precedent (panel-mean headline, per-mold + frontier-core
breakdowns, per-judge columns mandatory).

## 4. Analysis plan (paper numbers)

- Headline: per-SUT panel means with per-judge sensitivity columns; paired
  significance over epochs (s7 precedent); per-mold and frontier-core breakdowns.
- Instrument-reliability: the A3 (or re-run v3) ICC(2,1) repeat statistics.
- Methods narrative: s6–s15 instrument development + truth-bench validation + the
  two NO-GOs as instrument artifacts; NON-QUOTABLE discipline lifts ONLY via this
  run; no cross-instrument comparison anywhere, including drafts.
- Disclosures: G4 cheap-panel-era derivation; opposed judge residuals; bimodal
  boundary-cell classes; batch-mode prohibition; strict-v3 lineage (if adopted).

## 5. STOP-POINT 4 (to be ruled at s17 after the v3 gate)

Owner rules: (a) scenario A/B/C (or variant), (b) roster, (c) epochs, (d) SUT spend
cap (recommend 2× the scenario estimate), (e) Sol wall-clock lever (streams probe
vs 1-epoch Sol), (f) episodes in/out (default out). Nothing samples until then.
