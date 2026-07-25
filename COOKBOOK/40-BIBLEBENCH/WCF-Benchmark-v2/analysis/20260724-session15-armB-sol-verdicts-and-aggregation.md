# S15 Arm B — GPT-5.6-Sol Verdicts + Strong-Judge Aggregation Study vs the 17-Cell Bench

**Date:** 2026-07-24 · **Judge:** GPT-5.6-Sol via `codex exec` (OAuth, $0; high reasoning
effort; stdin-piped packet, sandbox read-only, no file/browse access; same blind packets
as the opus arm — `analysis/20260724-session15-bench-packets/` copied to /tmp isolation).
**Instrument:** strict-v2 template (identical to the opus arm — judge capability is the
only varied factor between the two strong arms; template-v2 vs cheap-panel remains
confounded with judge tier by design). **Companion:** `20260724-session15-armB-opus-verdicts.md`.
All numbers EXPLORATORY / NON-QUOTABLE.

## Verdicts + two-strong-judge aggregation

| Cell | Class | Band | Opus | Sol | Mean(O,S) | Mean in band? |
|---|---|---|---|---|---|---|
| LIB-N-006/qwen | leniency probe | 78–88 | 92 | 71 | 81.5 | **YES** (judges bracket the truth) |
| PROOF-N-009/qwen | substitute (ruled) | 78–88 | 82 | 82 | 82 | **YES** (both exactly on doctrine) |
| MEND-N-002/qwen | negative control | 90–100 | 88 | 71 | 79.5 | NO (−10.5) |
| MEND-N-009/qwen | negative control | 90–100 | 100 | 71 | 85.5 | NO (−4.5) |
| PROOF-N-005/qwen | negative control | 90–100 | 100 | 100 | 100 | YES |
| WHOLE-N-004/qwen | negative control | 90–100 | 100 | 92 | 96 | YES |
| LIB-N-011/qwen | genuine refusal | 5–15 | 8 | 8 | 8 | YES |
| LIB-N-011/haiku | genuine refusal | 5–15 | 8 | 8 | 8 | YES |
| WHOLE-N-007/haiku | genuine refusal | 5–15 | 8 | 8 | 8 | YES |
| LIB-N-004/haiku | genuine refusal | 5–15 | 8 | 8 | 8 | YES |
| WHOLE-N-003/haiku | genuine refusal | 5–15 | 4 | 8 | 6 | YES |
| LIB-N-010/haiku | preamble-trap probe | 78–92 | 100 | 100 | 100 | NO (+8) — see note |
| MEND-N-001/haiku | partial-credit probe | 73–83 | 92 | 75 | 83.5 | EDGE (+0.5) |
| WHOLE-N-007/qwen | over-fire probe | 85–100 | 100 | 88 | 94 | YES |
| PROOF-N-001/qwen | over-fire probe | 85–100 | 100 | 100 | 100 | YES |
| PROOF-N-010/qwen | over-fire probe | 85–100 | 100 | 100 | 100 | YES |
| WHOLE-N-008/haiku | over-fire probe | 85–100 | 100 | 92 | 96 | YES |

**Scorecards (strict, no partial credit):** opus alone 12/17 · Sol alone 13/17 ·
mean-of-2 13/17 (14/17 if the 83.5 edge floors to 83). Max-of-2 and min-of-2 are
strictly worse (leniency- and strictness-dominated respectively). **No configuration
is bench-clean.**

## What every strong configuration achieves (vs the cheap panel)

- **ZERO categorical errors, all configurations.** All 5 refusal cells floor; all 6
  trap/over-fire probes hold (preamble trap, wrong-artifact trap, lone-judge floors —
  the classes that produced 67–92-point cheap-panel errors and disqualified
  min-aggregation — do not occur once across 34 strong-judge verdicts).
- **PROOF-N-009 = 82 from BOTH judges independently** — the owner's strict-substitute
  ruling is cleanly encodable and consistently applied.
- Residual misses are METRIC (≤19 points, mostly ≤8), and the two judges' error
  directions are OPPOSED: opus errs lenient (+4/+8/+9), Sol errs strict (−7/−19/−19).
  On LIB-N-006 the bracketing cancels perfectly (mean 81.5 vs truth ~83).

## Residual error ledger (owner-relevant)

1. **Sol negative-control strictness** — MEND-N-002/MEND-N-009 at 71: Sol half-credits
   lines while attaching quotes that satisfy them, with no articulated rationale
   (verified on the MEND-N-009 transcript). Unexplained strictness, mirror image of
   cheap-panel unexplained leniency. Drags mean-of-2 below band on both controls.
2. **LIB-N-010 shared +8** — BOTH strong judges score 100 vs band 78–92. The s14 audit's
   deduction here was explicitly tentative ("a POSSIBLE small deduction… → ~83–92") for
   artifact-compactness. Two independent strong judges finding no deduction is evidence
   the bench band, not the judges, may be wrong on this cell. Flagged for owner; NOT
   silently re-litigated.
3. **MEND-N-001 opus leniency (+9)** — opus credits the Q109 devised-worship line via
   the disclosure quote; the audit says that half is genuinely absent. Sol prices it
   correctly (75). Mean lands at the band edge (83.5).

## Granularity caveat for any Phase-4 use (flag, not a recommendation)

The frozen criterion counts **nonzero** |qwen − haiku| gaps. Strong judges score with
fine granularity (82, 88, 92…), so 1-point noise gaps count as "discrimination" that
the coarse cheap panel would have scored as ties. A strong-judge Phase 4 under the
verbatim criterion is therefore EASIER than s12/s13's — direction favors GO. Only the
owner can weigh/amend the frozen criterion; flagged so a future GO is not
unknowingly noise-assisted.

## Spend

$0 this arm (Agent channel + codex OAuth). Session total remains $0 API.
