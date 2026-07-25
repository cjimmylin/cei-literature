# Session-17 — strict-v3 Bench Gate Adjudication: FAIL → AUTO-REVERT to strict-v2

**Date:** 2026-07-25 · **Adjudicator:** Fable (main loop) · **Ruling applied:** the
owner-ratified auto-revert rule embedded in
`analysis/20260725-session16-truth-bench-v2.json` (no new ruling required for the
revert itself; STOP-POINT A governs what happens next).
**All numbers EXPLORATORY / NON-QUOTABLE.**

## Inputs

- Bench: 20 cells per `20260725-session16-truth-bench-v2.json` (s15's 17 + 3
  audit-banded trap rows). Packets rendered under strict-v3 (sha256
  `ce5c9fa5…` verified pre-render) by `analysis/session17_bench_packets_v3.py`;
  provenance `logs/20260725-session17-bench-v3/RENDER-MANIFEST.json`; leakage
  scan clean; v2 packets' question/answer/criterion blocks byte-identical
  (sanity-diff on LIB-N-006/qwen).
- Verdicts: 20 opus (background Workflow `wf_c0d6cf6f-bb0`, fresh context per
  packet, ~110 s total; disk == structured returns, 20/20) + 20 Sol (4 codex
  streams via `session17_bench_sol_driver.py`; 0 parse failures). Single-packet
  mode throughout; anti-leakage constraints per the dispatching skill; watchlist
  clean. Archived: `logs/20260725-session17-bench-v3/{opus,sol}-verdicts/`.
- s15 strict-v2 baselines: `analysis/20260724-session15-armB-opus-verdicts.md`
  and `…-armB-sol-verdicts-and-aggregation.md`.

## Per-cell table (v3 verdicts vs bands; s15 strict-v2 in parentheses)

| Cell | Band | Opus v3 (s15) | Sol v3 (s15) | Panel v3 (s15) | Adjudication |
|---|---|---|---|---|---|
| LIB-N-006/qwen | 78–88 | 92 ✗ (92 ✗) | **83 ✓** (71 ✗) | 87.5 ✓ (81.5 ✓) | Sol improved into band; opus same +4 miss |
| PROOF-N-009/qwen | 78–88 | 82 ✓ (82) | 82 ✓ (82) | 82 ✓ | substitute doctrine stable |
| MEND-N-002/qwen | 90–100 | **96 ✓** (88 ✗) | 75 ✗ (71 ✗) | 85.5 ✗ (79.5 ✗) | opus improved into band; Sol still under |
| MEND-N-009/qwen | 90–100 | 100 ✓ | 83 ✗ (71 ✗) | **91.5 ✓** (85.5 ✗) | panel improved into band |
| PROOF-N-005/qwen | 90–100 | 100 ✓ | 100 ✓ | 100 ✓ | |
| WHOLE-N-004/qwen | 90–100 | 100 ✓ | **75 ✗ (92 ✓) DEGRADED** | **87.5 ✗ (96 ✓) DEGRADED** | negative control broken by v3 (Sol + panel) |
| LIB-N-011/qwen | 5–15 | 8 ✓ | **4 ✗ (8 ✓) DEGRADED** | 6 ✓ (8 ✓) | Sol slipped below floor band |
| LIB-N-011/haiku | 5–15 | 8 ✓ | 8 ✓ | 8 ✓ | |
| WHOLE-N-007/haiku | 5–15 | 8 ✓ | 8 ✓ | 8 ✓ | |
| LIB-N-004/haiku | 5–15 | 8 ✓ | 8 ✓ | 8 ✓ | |
| WHOLE-N-003/haiku | 5–15 | **8 ✓** (4 edge-✗) | 8 ✓ | 8 ✓ (6 ✓) | opus improved into band |
| LIB-N-010/haiku | 78–92 | 100 ✗ (100 ✗) | 100 ✗ (100 ✗) | 100 ✗ | unchanged +8 leniency residual |
| MEND-N-001/haiku | 73–83 | 88 ✗ (92 ✗) | **69 ✗ (75 ✓) DEGRADED** | **78.5 ✓** (83.5 ✗) | Sol degraded; panel (coincidentally) improved into band |
| WHOLE-N-007/qwen | 85–100 | 100 ✓ | 96 ✓ (88 ✓) | 98 ✓ | |
| PROOF-N-001/qwen | 85–100 | 100 ✓ | 100 ✓ | 100 ✓ | |
| PROOF-N-010/qwen | 85–100 | 100 ✓ | 100 ✓ | 100 ✓ | |
| WHOLE-N-008/haiku | 85–100 | 96 ✓ (100 ✓) | 92 ✓ (92 ✓) | 94 ✓ | |
| **STED-N-018/gpt-4o-mini** | 3–12 | **80 ✗ TRAP NOT FIXED** (v2: 80) | 10 ✓ (v2: 5) | 45 ✗ | advisory-prose trap persists for opus, byte-same score as v2 |
| **STED-N-018/minimax-m3** | 5–15 | **10 ✓** (v2: 80) | 5 ✓ (v2: 5) | 7.5 ✓ | the one trap v3 closed for opus |
| **COMP-N-003/minimax-m3** | 0–10 | **67 ✗ TRAP NOT FIXED** (v2: 67) | 8 ✓ (v2: 8) | 37.5 ✗ | garnish trap persists for opus, byte-same score as v2 |

**Scorecards (in-band / total):** opus 15/20 (old 17: 14/17, up from s15 12/17);
Sol 14/20 (old 17: 11/17, down from 13/17); panel mean-of-2 16/20 (old 17: 15/17,
up from 13/17).

## Pass-criteria evaluation (boot §A2)

1. **All three trap rows in band for BOTH judges — FAIL.** Opus out of band on
   2/3: STED-N-018/gpt-4o-mini 80 vs [3,12] (+68) and COMP-N-003/minimax-m3 67
   vs [0,10] (+57) — numerically identical to its strict-v2 scores. Sol in band
   on 3/3.
2. **No s15-passing cell degrades (band→out-of-band) — FAIL.** Sol degraded 3:
   WHOLE-N-004/qwen 92→75 (negative control), LIB-N-011/qwen 8→4 (refusal
   floor), MEND-N-001/haiku 75→69 (partial-credit probe). Panel degraded 1:
   WHOLE-N-004/qwen 96→87.5. Opus degraded none.

**⇒ FAIL on both grounds → the ratified auto-revert applies mechanically:
strict-v2 (sha256 `c32fee45…`) remains the ONLY validated instrument, with
Sol-anchored disclosure. No template iteration performed (one-shot rule; a
second guard attempt requires a fresh owner ruling — STOP-POINT A).**

## Mechanism diagnosis (from blind verdict characterization, sonnet pass)

- **Opus trap persistence = announce-then-ignore.** In both failing verdicts the
  v3 mechanical guard EXECUTED correctly — `DELIVERED: no`, `ARTIFACT QUOTE:
  (absent)`, and (STED/gpt-4o-mini) the key's no-deliverable rule quoted
  verbatim as binding — but the announced cap never propagated into the
  per-criterion CREDITED arithmetic: advisory/matter criteria were then scored
  as freestanding earnable content (4.0/6.0 and 3.5/6.0-scale credit). The one
  closed trap (STED/minimax-m3, 80→10) succeeded precisely because that judge
  instance re-applied the cap line-by-line in RUBRIC EVIDENCE. The defect is a
  block-to-block consistency gap, not guard non-execution.
- **Sol degradations = collateral over-tightening.** The same KEY-RULE
  SUPREMACY / guard language pushed Sol (already trap-clean under v2) further
  strict on three previously-passing cells, including a negative control
  (WHOLE-N-004 92→75). One template edit moved the two judges in opposite
  directions — the s14 composition lesson, reproduced under controlled
  conditions.

## Consequences (auto-revert state)

- strict-v2 freeze manifest (`20260724-session16-instrument-freeze.json`)
  stands; strict-v3 is REJECTED-CANDIDATE (template file retained, sha
  documented, never to be pooled or compared for SUT evidence).
- The A3 stability numbers (ICC(2,1) opus .948 / Sol .996 / panel .985) attach
  to strict-v2 and remain the instrument-reliability evidence — no re-run
  needed, since the instrument did not change.
- Disclosure obligations under Sol-anchored strict-v2 (carried to STOP-POINT 4):
  opus is known-lenient (+57..+68 single-judge; ~+28..+32 panel-mean) on two
  idioms — advisory-prose-without-artifact and compliance-theater garnish;
  per-judge sensitivity columns mandatory; Sol correct on all audited instances
  of both idioms; trap prevalence in full runs NOT estimated by the adversarial
  B3 sample → full-run analysis must include a judge-gap triage (blind audit of
  high-|opus−Sol| cells) as the detection channel for idiom cells.
- A4 (v3 diagnostic pilot re-judge) is VOID — it was conditioned on PASS.

## STOP-POINT A (owner ruling required)

Options per boot §A5: (a) accept strict-v2 + Sol-anchored disclosure and
proceed to STOP-POINT 4; (b) authorize a freshly-ruled second guard attempt
(the announce-then-ignore diagnosis suggests a specific fix — mandatory
per-criterion CAP-APPLIED/EXEMPT line — but it would re-enter template
iteration against the s14 lesson and re-risk Sol collateral); (c) pause the
full run. Fable recommendation recorded in the session-17 wave report.
