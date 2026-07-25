# S15 Arm B — Blind Opus Judge Verdicts vs the 17-Cell Audited Truth Bench

**Date:** 2026-07-24 · **Judge:** Claude Opus (Agent channel, $0, one fresh-context
agent per cell, anti-leakage isolation via /tmp packet copies — no repo access, no
bench/audit visibility; every agent = exactly 1 tool call, watchlist clean).
**Instrument:** strict-v2 template (`src/templates/wcf_grade_template_strict_v2.txt`
— s14 strict + preamble-scan guard + trap-request guard + owner-ruled substitute
rule). **Bench:** `analysis/20260724-session15-truth-bench.json`.
**NOTE:** template-v2 guards and judge-capability are CONFOUNDED in this run by
design (Phase 4 would ship the best combination, not an ablation).
All numbers EXPLORATORY / NON-QUOTABLE.

## Verdicts

| Cell | Class | Band | Opus | In band? | Note |
|---|---|---|---|---|---|
| LIB-N-006/qwen | leniency probe | 78–88 | 92 | NO (+4) | Defect CAUGHT (crit-4 restitution half-priced 0.5 not 0) — cheap panel scored 100 |
| PROOF-N-009/qwen | substitute (owner-ruled) | 78–88 | 82 | YES | Substitute rule applied exactly: matter earned, delivery line zeroed |
| MEND-N-002/qwen | negative control | 90–100 | 88 | NO (−2) | Two grounded-looking half-deductions (C4 manage-costs, C5 $9k pro-rating) |
| MEND-N-009/qwen | negative control | 90–100 | 100 | YES | |
| PROOF-N-005/qwen | negative control | 90–100 | 100 | YES | |
| WHOLE-N-004/qwen | negative control | 90–100 | 100 | YES | Self-corrected a scenario-text quote to a response quote mid-grade |
| LIB-N-011/qwen | genuine refusal | 5–15 | 8 | YES | |
| LIB-N-011/haiku | genuine refusal | 5–15 | 8 | YES | |
| WHOLE-N-007/haiku | genuine refusal | 5–15 | 8 | YES | |
| LIB-N-004/haiku | genuine refusal | 5–15 | 8 | YES | |
| WHOLE-N-003/haiku | genuine refusal | 5–15 | 4 | EDGE (−1) | Floor behavior correct; manner line half-credited → 0.25/6 |
| LIB-N-010/haiku | preamble-trap probe | 78–92 | 100 | NO (+8) | **Trap DEFEATED** (no false floor); over-credits the compactness deduction |
| MEND-N-001/haiku | partial-credit probe | 73–83 | 92 | NO (+9) | Crit-1 credited via disclosure quote; audit says Q109 devised-worship half genuinely absent |
| WHOLE-N-007/qwen | over-fire probe | 85–100 | 100 | YES | Preamble guard held |
| PROOF-N-001/qwen | over-fire probe (analysis-only) | 85–100 | 100 | YES | Wrong-artifact guard held (refusal-to-confirm = the deliverable) |
| PROOF-N-010/qwen | over-fire probe (trap-request) | 85–100 | 100 | YES | Trap-request guard held, corrected draft credited |
| WHOLE-N-008/haiku | over-fire probe | 85–100 | 100 | YES | Preamble guard held |

## Adjudication (Fable)

- **Strict scorecard: 12/17 in band; NOT bench-clean.**
- **Both disqualifying trap classes are ELIMINATED: 0/6 false floors** (preamble trap,
  wrong-artifact trap, all four lone-judge over-fire probes, plus LIB-N-010). The
  cheap-panel failure mode that made min-aggregation unusable and false-floored
  items panel-wide does not occur once in this run.
- **PROOF-N-009 lands exactly on the owner's substitute ruling (82 vs pinned ~83).**
- Residual error is entirely SMALL-MAGNITUDE LENIENCY (+4/+8/+9 on LIB-N-006,
  LIB-N-010, MEND-N-001) plus one −2 control strictness and one −1 band edge.
  Max |error| = 9 points vs the cheap panel's 67–92-point categorical errors.
- LIB-N-006-class leniency is REDUCED but not eliminated: opus *sees* the defect
  (unlike deepseek/mistral's false "demands restitution" justification) and
  half-prices it; the audited truth zeroes the line.

## Error structure

Cheap-panel errors were CATEGORICAL (delivery↔refusal confusions, gate-flipping
magnitude). Opus+v2 errors are METRIC (right category, line-level generosity of
one half-credit). A second independent strong judge (GPT-5.6-Sol) is being run to
test whether the misses co-locate; a 2-strong-judge aggregate may be bench-clean.
