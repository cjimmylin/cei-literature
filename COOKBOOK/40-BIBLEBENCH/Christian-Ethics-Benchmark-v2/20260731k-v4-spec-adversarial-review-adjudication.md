# WALKWORTHY v4 spec — adversarial review adjudication record

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content.
**Date:** 2026-07-31 · **Subject:** adversarial review (refute-first, opus tier) of
`20260731j-walkworthy-v4-design-spec.md` v0.1 → adjudicated revisions applied as v0.2
(same file, version banner — manuscript/spec convention).
**Status of all numbers herein: DIAGNOSTICS for v4 design only — NOT WALKWORTHY numbers**
(per `RULINGS-APPLIED-20260731g.md`, "What this run is NOT").

## 1. Review outcome

Verdict REVISE: 4 BLOCKER, 12 MAJOR, 10 MINOR findings. The reviewer independently
reproduced all 18 published d01/d03/d04 frontier pair lines digit-for-digit from the raw
judge JSONLs — **the probe's arithmetic stands unrefuted**; every accepted finding is
inferential or governance-level. All 26 findings ACCEPTED (some with modification), none
rejected. Dispositions below; the revised spec text is authoritative for the fixes.

## 2. The three computations that changed the spec

### 2.1 Permutation null of the v0.1 gate (reviewer, 300 SUT-label permutations)

A design "PASSES" the v0.1 §6 gate under a no-difference null 34.7–54.0 pct of the time
(d01 38.3 / d03 34.7 / d04 54.0); per-test confirmatory rate under the null ≈ 6.9 pct;
v0.1 ship rule joint false-pass ≈ 0.30–0.45. **Adjudication: accepted in full.** The
v0.2 gate names confirmatory-eligible pairs in advance, applies Holm within design,
mandates a permutation-calibrated family-wise ship rule, and requires the calibration to
be re-run and reported on the v4-B2 data.

### 2.2 Retained-set recompute (reviewer, exact §2.1 item sets)

On the items v0.1 actually carried forward: d01 keeps 1 confirmatory pair (interval
[0.083, 0.583]); **d03 keeps zero of its 6 pair verdicts** (its confirmatory pair's epoch
signs become [0, 1, 1] on the 4-item set); **d04 loses its only confirmatory pair**
(interval widens to [−0.548, +0.052]). **Adjudication: accepted.** A design may not enter
v4 on a verdict computed over items it discards. v0.2 reclassifies d03 and d04 as
REBUILD (target n ≥ 12, seeded by their band survivors), keeps d01 (12 items) and d05
(17 items) as carry-forward, and states retained-set evidence only.

### 2.3 Mid-tier P1 rerun (this adjudication, $0, `analyze_widegap_probe.py
--log-root logs/fullbank-3ep-20260724`, identical tier code)

The stored mid-tier tree yields **10 surviving pair verdicts of 60 tests** (5
confirmatory + 5 descriptive; d01 4C+1D, d02 1D, d03 1C, d04 1D, d05 2D, d07 0).
**Adjudication: MAJOR 7 accepted; the "12 survivors where mid-tier had zero" attribution
in spec v0.1 §1 and in `20260731i` §5.1 is RETRACTED as stated.** Gate A's zero was a
zero on a different, stricter object (within-item contrasts with five-system rank
stability), not on the P1 pairwise test. The identified frontier claim, now in v0.2:
frontier spacing roughly doubles the pair-test survival rate (12/36 vs 10/60), lifts the
confirmatory rate to ≈ 3× the permutation null (19.4 pct vs ≈ 6.9 pct null, mid-tier
8.3 pct), converts d05 from 2 descriptive to 4 confirmatory pairs, and releases 9 of 11
d05 ceiling items. **Correction notice for `20260731i` §5.1:** that report is immutable;
this paragraph is its standing correction (successor-file convention, precedent
`20260730l`).

## 3. Fable-tier ruling on the escalated question (BLOCKER 2/3 pair)

Question: may a benchmark band-filter items and evaluate its discrimination gate on the
same administration, and what is carry-forward evidence worth?

**Ruling: No shared administration.** Band membership demonstrably moves under panel and
sampling changes (mid-tier→frontier retention 29–70 pct per design); gating on the
selecting run inflates exactly the edge items selection favored. v4-B is split: **B1**
(calibration administration → band filter + item admission) and **B2** (independent
administration of the admitted bank → gate evaluation). Carry-forward evidence is
defined as evidence computed on the retained set (per §2.2 above) and is *provisional*
until B2; the probe functions as B1 for the carry-forward core. Additionally (MAJOR 15):
authoring reserves a per-design holdout fraction at creation, quarantined under the
existing loader guard, because the v3 holdout contains no v4-new-design items and
cannot blind-confirm them.

## 4. Disposition table (remaining findings)

| # | Finding (abbrev.) | Disposition in v0.2 |
|---|---|---|
| B4 | Commitment design founded on unprobed, NOT-VALIDATED WW-03-L02 with a different read-out | Accepted. §2.3 demoted to v4.1 candidate pending a construct micro-probe (v4-C); UNVALIDATED status and read-out mismatch disclosed |
| M5 | BT τ rationale cited a Spearman value as Kendall | Accepted. Kendall-only record range 0.40–0.527; threshold raised to τ-b ≥ 0.60; 4-rank discreteness noted |
| M6 | Judge-B parse failures 7.3–13.6 pct, per-pair item intersection breaks pairing | Accepted. Complete-case parity required; per-design parse-fail rate reported; swap check void above 15 pct; analysis-script upgrade listed as v4-B precondition |
| M8 | d05 confirmatory pairs are 3× deepseek-r1; anchor gpt-4.1-mini (0.859) not separated from frontier top three | Accepted. d05 evidence restated honestly; hardening expansion justified against the top-three gap (+0.061 marginal), not "4 confirmatory pairs" |
| M9 | Ranked-sacrifice scoring under-defined; keying normativity unadjudicated | Accepted. Primary = binary first-sacrifice match (defined whenever ≥ 1 constraint violated; infeasible-by-design guarantees this); ordering τ demoted to secondary, k ≥ 3 only; independent double-keying with disclosed disagreement rate |
| M10 | §4.5 piloting leaked paid calls into the $0 authoring phase | Accepted. Piloting moved to v4-B1; v4-A produces candidate items only |
| M11 | §2.4 unbudgeted new d02 authoring; BT protocol unspecified | Accepted. v4.0 scope = the 7 stored in-band items on stored final-turn responses only; Davidson BT (tie term); 6 pairs × 2 orderings × 2 judges × 3 epochs; position-debias by averaging orderings; new d02 authoring deferred to v4.1 |
| M12 | Regex false zeros bias toward the designed-for conclusion | Accepted; folded into the §2.3 micro-probe design (documented normalizer, false-negative audit, metric renamed fact_presence_rate, carry-vs-disown judge secondary) |
| M13 | Zero epoch difference: consistency rule unstated | Accepted. Stated: a zero epoch difference BREAKS consistency (matches shipped analysis code) |
| M14 | d03/d04 gate on 4–5 items | Accepted; merged with B2 fix: minimum retained n ≥ 12 for any gated design |
| M16 | Missing diagnostics banner; tier-naming duty under-scoped | Accepted. Banner added; tier named in every headline claim, both tiers |
| Minors 17–26 | "exactly $N" is scenario budget not keyed constraint; scorer description qualifier; WW-04-I02 is a negative example; §6 over-attribution to Ruling 1; band undefined for signed deltas; 22.6 pct is judge-A-only (judge-B residue 4 of 253); second anchor named and pinned (deepseek-chat) + slug re-verification at stamp; per-design cost model; drift/seed/test-retest risks section added; d02 read-out provenance (T0-4 terminal-state, not the CLOSED pushback_rate) named | All accepted as one-line fixes in v0.2 |

## 5. What the review left standing

The probe arithmetic (all recounts exact); the D-3 retire-absolute-d02 call; the §7
separately-ruled phase structure; the §8 open-questions discipline; canary/lint/
immutability compliance. The reviewer's flagged residual risk — the §2.4 paired-
comparison protocol has never been run against data — is carried into v4-C as its
explicit validation question.

## 6. Verification

Adjudication artifacts: reviewer report (session task record), reviewer reproduction
scripts (session scratchpad, ephemeral), mid-tier rerun output (scratchpad JSON +
command line in §2.3, $0, reproducible from the committed script and stored tree).
This file: `lint_claims.py` 0 blockers · canary 2 · successor-file naming (`k` next in
sequence) · no prior file edited except the v0.1→v0.2 spec revision under its version
banner.

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content.
