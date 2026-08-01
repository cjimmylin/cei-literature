# WALKWORTHY v4 spec v0.3 — adversarial review adjudication record

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content.
**Date:** 2026-07-31 · **Subject:** second adversarial review (refute-first, opus tier)
of `20260731j-walkworthy-v4-design-spec.md` v0.3 (profiling re-target) → adjudicated
revisions applied as **v0.4** (same file, version banner). Companion to `20260731k`
(the v0.1→v0.2 adjudication, which remains in force).
**All numbers are DIAGNOSTICS for v4 design only — NOT WALKWORTHY numbers.**

## 1. Review outcome

Verdict REVISE: 6 BLOCKER, 13 MAJOR, 6 MINOR. The reviewer re-derived the four named
crossing legs digit-for-digit from the raw tree — the arithmetic base again stands;
every accepted finding is inferential, definitional, or a v0.2-content regression.
All findings ACCEPTED; three (BLK-2, MAJ-4, MAJ-5) were escalated to the Fable tier
and are ruled on in §2. Dispositions in §3; the v0.4 text is authoritative for fixes.

## 2. Fable-tier ruling on the escalated question

*What evidence licenses calling a set of dimensions a "profile" rather than a signed
ladder, and what reference frame makes shape claims meaningful at n=7?*

**Ruling (three parts):**

**(a) The confirmatory core is crossings as sign-plus-interval claims on the frozen
instrument's own scales.** The v0.3 invariance claim was wrong as written (BLK-1: the
reviewer showed the evidence TIER flips under monotone rescaling on all three tested
legs — only the SIGN is invariant). The tier is therefore defined, explicitly, as a
claim about the pinned item-score scales of the stamped instrument — which is
legitimate and disclosed, exactly as every classical test score is scale-bound. The
corrected doctrine sentence: "the sign of a crossing is invariant to monotone
per-dimension rescaling; its evidence tier is a claim about the instrument's pinned
scales."

**(b) The norm-referenced frame is DEMOTED from gate machinery to a disclosed
reporting convention, and shape claims are descriptive-only in v4.0.** At n=7
reference models the frame cannot bear confirmatory weight: self-inclusion attenuates
standardized cells by up to 2.42× in a dimension-specific way (MAJ-4, breaking
within-model comparisons), the reference SD swings up to 5.30× under leave-one-model-
out (MAJ-5, d05 driven entirely by deepseek-r1), and the |z| cap (n−1)/√n bounds what
a cell can even express. v4.0 profile cells are reported leave-one-out standardized
(every model — panel or future — scored against a frame excluding itself, making
panel and non-panel cells commensurable and removing self-inclusion bias), with
leave-one-out sensitivity published per cell and frame recomputation inside every
bootstrap draw. S-1 is retired as a gate claim; shape statements ship
descriptive-only with the frame caveat named. Cross-version linking is COMMON-ITEM
(a frozen anchor-item subset carried across versions), not anchor-rerun (MAJ-6:
3 anchors on a changed item set = 1 df, unidentified, and dies with a deprecated
slug); anchor responses are archived at stamp.

**(c) The structural label is GRADED, because a crossing refutes a common ordering,
not unidimensionality** (BLK-2: a reflected single factor crosses on every pair; the
probe's crossing evidence localizes to gpt-5 on d04 — 5 of 5 both-legs-surviving
reversals). Three publishable levels, each with its licence:
  1. **Multi-axis report** — always available: per-dimension cells with tiers and
     uncertainty. No structural claim.
  2. **Two-axis structure demonstrated** — ≥ 1 named crossing at the confirmatory
     tier, PLUS the redundancy screen on |τ-b| (reflection IS redundancy — the screen
     is two-sided), PLUS explicit disclosure of where the crossing evidence
     localizes (today: one model, one dimension).
  3. **Multidimensional profile** — ≥ 2 confirmatory crossings on distinct dimension
     pairs whose moving models differ, plus a dimension pair with |τ-b| bounded away
     from 1 by its bootstrap interval. Not claimed for v4.0 unless earned; the spec
     plans for level 2.
The v4.0 ship rule targets level 2; the declared-ladder fallback remains if even
level 2 fails.

## 3. Dispositions (all findings accepted)

| # | Finding (abbrev.) | Disposition in v0.4 |
|---|---|---|
| BLK-1 | Monotone-invariance claim false for tier | Corrected per ruling 2(a); tiers attach to pinned scales |
| BLK-2 | Reflected factor produces crossings; distinctness screen one-sided | Ruling 2(c): graded labels; redundancy on absolute τ; localization disclosure |
| BLK-3 | Named crossings underpowered (X-1 d05 leg needs ~92–128 items at +0.036) | Accepted. X-1 RE-NAMED to the powered pair: gpt5/deepseekr1 between P-ALLOCATION and P-MOTIVE (d05 leg +0.458 already interval-excluding; d04 leg −0.172 needs ~34 items). X-2 retained (d03 leg n ok; d04 leg needs ~37). **d04 REBUILD target n = 40** (was floor 12), sized from measured effects/SDs at the corrected multiplicity; power line added to §6 with expected-failure disclosure |
| BLK-4 | P-MOTIVE fails §5.4(c) as written; τ-on-near-ties is the wrong statistic | Accepted. §5.4(c) replaced: judge agreement on the SIGN of the dimension's named contrasts + item-level cross-judge correlation ≥ 0.30; probe τ table disclosed in the spec |
| BLK-5 | 15 pct void rule denominator unstated; complete-case reading VOIDs d03 (22.6 pct loss) and d07 (32.1 pct) | Accepted. Denominator fixed = complete-case retention vs judge-A-scored records; both rates published; judge-B parse hardening (retry-on-parse-failure) added as a v4-A code deliverable with target retention ≥ 85 pct; X-2's confirmatory eligibility disclosed as conditional on d03 clearing the rule at B2 |
| BLK-6 | 10 normative references to overwritten v0.2; authoring rules absent from disk | Accepted. v0.4 is fully self-contained — all v0.2 content inlined (authoring rules incl. double-hazard + WW-04-I02 floor, BT gate both components, ranked-sacrifice degenerate counts, cost model, provenance notes, rejected-items rule, `20260731e` citation) |
| MAJ-1 | Holm across conjunction legs is wrong | Accepted: crossing p = max(leg p) (intersection-union); Holm across the named claim family {X-1, X-2} only |
| MAJ-2 | τ thresholds indeterminate (n=4 lattice vs n=5+) | Accepted: all ordering statistics computed over the 7 reference models, stated explicitly; thresholds re-picked on that lattice; bootstrap interval on τ reported |
| MAJ-3 | §5.4 floor 0.40 inside the failed 0.40–0.527 range | Accepted: with (c) replaced (BLK-4) the general τ floor is retired; wherever ordering-τ is still used the floor is 0.60, aligned with the BT gate |
| MAJ-4/5/6 | Frame self-inclusion bias; n=7 SD fragility; linking unidentified | Ruling 2(b): LOO standardization, sensitivity disclosure, in-bootstrap frame recomputation, common-item linking, anchor-response archive |
| MAJ-7 | "10 items at mid-tier band" unexecutable (7/6/8 exist); probes can't satisfy admission | Accepted: rule = most band-central available up to 10 (actual 7/6/8); axis probes decide variance/degeneracy screening ONLY — admission requires authored expansion + B1 |
| MAJ-8 | Selective variance citation (d08 = 9.1 pct, below the 13.79 pct df-null) | Accepted: all three candidates cited against the df line; d08 named the weakest |
| MAJ-9 | Ship rule readable two ways; "confirmed" vs "confirmatory" | Accepted: qualifying set enumerated by name {X-1, X-2}; tier words used exactly; reliability pairs excluded from the count |
| MAJ-10 | Ship rule silently amends Ruling 1.3 (descriptive-sufficient) | Accepted: the confirmatory-crossing requirement is flagged as an AMENDMENT to Ruling 1.3 in §8 for explicit ratification |
| MAJ-11 | Untiered §1 motivating claims; d03 ordering reverses under judge B (claude45 1.000 > gpt5 0.880) | Accepted: tier + judge named on every motivating claim; the d03 judge-B reversal disclosed wherever shape statements reference P-FAITHFULNESS |
| MAJ-12 | Permutation-null unit unspecified | Accepted: within-item SUT-label permutation, identical permutation across dimensions/epochs/judges, stated in §6 |
| MAJ-13 | B1+B2 cost unstated (~$200 extrapolated) | Accepted: order-of-magnitude line added to §7 (B1+B2 ≈ $180–230 at 7 models × ~150 items × 2 administrations); new §8 ratification question |
| MIN-1..6 | v4.1 status of P-COMMITMENT; zero-epoch rule in descriptive clause; v4-C derivation ($10–14 actual, $20–30 kept as ceiling); in-bootstrap frame; d06 judge-B pole risk flagged; BT gate second component restored | All accepted as one-line fixes |

## 4. What the review left standing

All probe arithmetic (second independent digit-for-digit reproduction); the B1/B2
split; the two-tier structure and anti-Gate-A partial-ship provision; the
declared-ladder fallback; "a ship the null explains is not a ship"; retire-absolute-
d02 (reviewer strengthens it: judge ordering τ-b −0.913); the §8 open-questions
discipline. The reviewer's residual-risk flag — frame uncertainty silently omitted
from reported intervals — is addressed structurally by ruling 2(b) (frame recomputed
inside every bootstrap draw; sensitivity published), not by prose.

## 5. Verification

This file: `lint_claims.py` 0 blockers · canary 2 · next letter (`l`) in the per-day
sequence · no prior file edited except the spec's v0.3→v0.4 revision under its
version banner. The v0.2 and v0.3 texts remain recoverable at git objects
`d249122d0` and `ee3a441ff`; v0.4 removes the need to consult them (BLK-6).

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content.
