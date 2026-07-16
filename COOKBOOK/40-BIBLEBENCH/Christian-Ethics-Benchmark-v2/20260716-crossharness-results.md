# v1↔v2 Cross-Harness Comparison — RESULTS (Option A)

**Date:** 2026-07-16 (session 5) · **Authorization:** owner GO
(`20260716-owner-ruling-f1-and-spend-go.md`), spend memo Item 3, ceiling $0.75.
**Design:** `20260716-crossharness-design.md` · **Pre-committed mapping:**
`20260716-crossharness-mapping-precommit.md` (nothing beyond it was computed).
**Tool:** `tools/audit/crossharness_compare.py` · Data: stored v1 MVP-A1 run
(2026-07-13, read-only) vs fresh v2 slice runs (`logs/crossharness-20260716/`,
60 items × 2 SUTs × judges A+B). Zero v1-tree writes.

**Scope guard:** descriptive instrument evidence only. Does NOT reopen the PARALLEL
ruling; v1 remains canonical. No SUT rankings anywhere (R1); every per-design cell is
n=6 → insufficient-n (R2); the pooled per-item agreement is the headline statistic.

## Headline — pooled per-item(-unit) agreement, same SUT + same judge across harnesses

| SUT | judge | categorical exact | numeric mean abs Δ |
|---|---|---|---|
| mistral-small | A (gpt-4.1-nano) | 73/131 = 0.557 | 0.391 |
| mistral-small | B (llama-3.3-70b) | 85/129 = 0.659 | 0.275 |
| gemini-flash-lite | A | 74/125 = 0.592 | 0.634 |
| gemini-flash-lite | B | 81/122 = 0.664 | 0.303 |

- Cross-harness agreement is **higher under judge-B than judge-A** on both SUTs —
  consistent with the F2 finding (`20260716-f2-ablations-report.md`) that judge-A's
  verdicts are strongly anchor-dependent and less stable.
- Per-field κ is mixed (e.g., action_class 0.38–1.00, turn_state 0.23–0.34,
  revealed_artifact 0.11–0.29; near-degenerate small-n binaries like allocation_ok are
  uninformative). Cross-harness per-item agreement is real but far from identity —
  of the same order as cross-JUDGE agreement within one harness.

## Decision rule — per-design Δharness vs the same-slice judge-swap band (all cells n=6, insufficient-n)

| design | mistral: Δh / Δj → verdict | gemini: Δh / Δj → verdict |
|---|---|---|
| 01 | 0.467 / 0.200 → **outside** | 0.033 / 0.300 → within |
| 04 | 0.133 / 0.161 → within | 0.233 / 0.039 → **outside** |
| 05 | 0.267 / 0.000 → outside* | 0.200 / 0.000 → outside* |
| 06 | 0.057 / 0.276 → within | 0.024 / 0.250 → within |
| 08 | 0.033 / 0.100 → within | 0.133 / 0.200 → within |
| 09 | 0.083 / 0.083 → within | 0.033 / 0.117 → within |
| 10 | 0.083 / 0.125 → within | 0.083 / 0.000 → outside* |

(02/03/07 not-comparable: 02/07 pre-declared descriptive-only (confounds c1/c2);
03's say_do_gap is not reconstructable from v1's per-arm fields.)

**Adjudication of the outside-band cells:**
- **05 (both SUTs) and 10-gemini are band artifacts, not harness effects:** their
  Δjudge is 0.000 (05 is judge-free by construction), so the band is degenerate — any
  nonzero delta lands "outside". For 05 the delta additionally has a known cause: the
  F9 retry (v2 final non-compliance 0/5 vs v1's residual 2/6; v1 attempts_dist shows
  every item took 2 attempts). Expected, documented, not noise.
- **01-mistral (0.467) and 04-gemini (0.233) are the only judge-banded exceedances,
  and they do not replicate across SUTs** (01-gemini and 04-mistral are within band).
  At n=6 with decode/time noise (c3) inside Δharness, inconsistent single-SUT
  exceedances are indistinguishable from small-n noise.

**Honest summary (the strongest claim this design supports):** on the comparable
designs, **no consistent harness effect larger than the judge effect was detected at
this n** — any v1↔v2 difference is not clearly larger than the noise we already accept
by using two judges. This is evidence the harnesses measure the same constructs, at
descriptive pilot precision; it is NOT a harness-equivalence certification.

## Judge-sensitivity reproduction

Within-harness |A−B| direction agrees on all comparable designs for mistral and on all
but design 08 for gemini (v1 0.000 vs v2 0.200). Design 05 shows 0.000 in both
harnesses (judge-free, as expected). The pilot's central judge-sensitivity finding
reproduces across harnesses.

## Quantified confounds

- **c2 (branch routing) is real and large on 07:** only 17–19 of 36 multi-turn
  positions had byte-identical administered user text across harnesses (02: 35–39 of
  46). The dropped-turn tallies are stimulus divergence, not join failure — 02/07
  cross-harness comparability is structurally limited, as pre-declared.
- **Exemplar asymmetry:** v1 scores all 6 items/design; v2 excludes `is_exemplar`
  admins from primaries (unmapped tallies: 01:1, 03:4, 04:2, 05:1, 06:1, 08:2, 10:4).
- One v1-recompute scale-mismatch bug (raw vs normalized rating deltas on 04) was
  caught by cross-checking against v2 metric formulas and fixed before any number was
  read into this report.

## Spend

v2 slice: 20/20 runs success, ≈0.78M in / 0.20M out (SUT + judge-A + classifier) +
judge-B rescore (200 samples). Estimated ≈ $0.25–0.35 vs ceiling $0.75 — within
envelope.

## What this feeds

A future canonical-ruling evidence base (per the PARALLEL ruling's anticipation):
this result says the v2 instrument reads the same constructs as v1 within judge noise
on single-turn designs, with 02/07 needing the branch-routing alignment work (F7-ish)
before any cross-harness claim. Nothing here changes v1's canonical status.
