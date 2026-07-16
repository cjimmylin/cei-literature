# Critique — Statistical Design for an n=5-SUT WALKWORTHY v2 Pilot

**Date:** 2026-07-16
**Lens:** REFUTE-FIRST statistical design. Attack the claim that a 5-LLM pilot on 344 public
items (10 behavioral designs, Inspect AI) can support its intended *descriptive* claims.
Concede only what survives.
**Stance:** The pilot is defensible ONLY as a per-design-cell, uncertainty-annotated,
comparison-generating exercise. Any leaderboard, ranking, or "SUT-A beats SUT-B" claim —
even hedged — does not survive at this n. Two findings are pilot-blocking as *claim-scope
guards*, not as run-blockers.

---

## Per-design effective-analysis-unit table (computed, full 344)

Counted directly from `datasets/public/design*.jsonl` (admin/pair_id/is_exemplar fields).
"Eff. unit" = the thing a headline metric averages over, PER SUT, AFTER exemplar exclusion.
Paired designs collapse 2 administrations → 1 unit. This is the real n, not the admin count.

| design | headline metric | unit type | admins (non-exemplar) | **eff. n / SUT** | 95% CI half-width @ p=0.5 (Wilson) |
|---|---|---|---|---:|---:|
| 01 | full_obedience_rate | single | 44 base | **44** | ±0.142 |
| 02 | break_turn_mean / break_rate | ladder | 36 base + 36 cold_open | **≤72 ladders (39 items)** | ±0.15 (before turn-exclusion) |
| 03 | say_do_gap | say/do pair | 29 say + 29 do | **29** | ±0.171 |
| 04 | motive_sensitivity_index | alpha/beta pair | 24 α + 24 β (+5 base singletons) | **24** | ±0.186 |
| 05 | csr_mean | single | 28 base | **28** | ±0.174 |
| 06 | profile_mean (7 criteria) | single | 27 base | **27** | ±0.176 |
| 07 | arc_pass_rate | ladder | 27 base | **≤27 ladders** | ±0.176 (before turn-exclusion) |
| 08 | covert_overt_gap | covert/overt pair | 29 cov + 29 ovt | **29** | ±0.171 |
| 09 | symmetry_index | seat_A/seat_B pair | 34 A + 34 B (+18 arbiter,+2 seat_C) | **34** | ±0.159 |
| 10 | mercy_delta | N/U pair | 32 N + 32 U | **32** | ±0.164 |

`banks total 510 = public 344 + holdout + exemplars`. The public runnable admin counts above
sum to the 344-admin figure once exemplars (5+4+8+7+4+4+4+8+4+8 = 56 exemplar admins) are set
aside. **The decisive fact: no design has more than 44 effective units per SUT, and five of
ten designs have ≤29.** Design 04 is the worst *structural* case at 24 pairs; designs 02/07 are
the worst *after-exclusion* case (below).

---

## SD-1 — No ranking or pairwise-difference claim survives at these CI widths
**Severity: CRITICAL. Pilot-blocking: YES (as a claim-scope guard).**

**Claim attacked:** implicit — "the pilot will show how the 5 SUTs order on each design / a
leaderboard." The boot prompt's Phase-4 language ("composite leaderboard with per-design cells",
`20260716-boot-prompt-...md:96`) invites exactly this.

**Evidence:** From the table, a single rate at the *largest* design (01, n=44) has a 95% Wilson
half-width of ±0.142 at p=0.5. At design 04 (n=24) it is ±0.186. To *distinguish two SUTs* on a
binary rate you need the difference to clear roughly the sum of two such intervals: a two-proportion
95% CI on Δrate at n=24/arm has half-width ≈ 0.28. So two SUTs must differ by **>0.28 in raw rate**
before the pilot can say their order is not a coin flip on that design — and that is per-design,
single-comparison, before any multiplicity correction. Most inter-model gaps on a normative rubric
will be smaller than that.

**Refutation attempt (steelman):** "Descriptive-only means we never claim significance; we just
report the numbers, so CI width is moot." — Does not survive. A ranking IS an inferential claim
in disguise: ordering 5 SUTs asserts 4+ pairwise "greater-than" relations. If the CIs overlap
(they will, mostly), the ranking is not reproducible under a re-run and reporting it *as a ranking*
misleads even without a p-value. "Descriptive" constrains the verb, not the reader's inference.

**Remedy:** Ban ranking language. Report per-design cells as rate ± Wilson-95 with n adjacent
(v1 G10 spirit, `../Christian-Ethics-Benchmark/PAPER/walkworthy-mvp-manuscript.md:850`). Where two
SUTs' intervals overlap, state "indistinguishable at pilot n." Reserve the word "leaderboard" for
v1/canonical release evidence, never the pilot.

---

## SD-2 — The exclusion cascade can silently gut designs 02 and 07 to single-digit n
**Severity: CRITICAL. Pilot-blocking: YES (as a per-turn metric guard).**

**Claim attacked:** that break_turn / arc_pass_rate are reportable per-SUT headline numbers.

**Evidence:** The metric code excludes an *entire ladder item* on ANY single unscorable/None turn
(`metrics.py:222` `_break_turn_item`, `metrics.py:242` `_arc_shape_item`). Ladders are ~8 turns
(02) / ~6 turns (07). If per-turn judge parse-failure is even 5% i.i.d. per turn, a 6-turn ladder
survives with probability 0.95^6 ≈ 0.74 — a **~26% item loss** before any content. The live
micro-check already realized this: `20260716-polish-items-report.md:168` — design 07 recomputed to
**`arc_pass_rate 0.0, n=1, excluded=1`** (one item, one excluded, from 2); design 02 to
**`n=2`** (`:166`). That was --limit 2, but the *mechanism* (one bad turn kills the item) applies at
full scale and compounds with ladder length.

Sensitivity (design 07 base eff_n=27):

| per-item exclusion | surviving n | 95% CI half-width |
|---:|---:|---:|
| 0% | 27 | ±0.176 |
| 10% | 24 | ±0.186 |
| 25% | 20 | ±0.201 |
| 50% | 14 | ±0.232 |

**Refutation attempt (steelman):** "Real judge parse rates are high — the smoke showed judge JSON
parseable on every scored sample (`20260715-inspect-fit-assessment.md:11`)." — Partially survives:
if per-turn parse success is ~99%, a 6-turn ladder loses only ~6%. BUT that smoke was ~2 samples/
design and did NOT exercise the per-turn path at scale; and "unscorable" here is not only parse
failure — it is *any turn the judge cannot classify into the 5 rubric states*, which is a content
event, not just a JSON event. The n=1 live result is an existence proof that the cascade bites.

**Remedy:** For 02/07, MANDATORILY report `n` and `excluded` adjacent to every headline (the code
already returns them — surface them). Set a per-design minimum-n floor (e.g. n≥10 surviving ladders/
SUT) below which the cell is reported as "insufficient n, not evaluated" rather than as a rate.
Consider a partial-ladder salvage metric (break position on the scored prefix) as a *companion*, so
one bad terminal turn doesn't zero the item — but do not change the primary formula for the pilot.

---

## SD-3 — 10 designs × multiple metrics × C(5,2)=10 SUT pairs → ~200+ implicit comparisons
**Severity: MAJOR. Pilot-blocking: NO (discipline requirement).**

**Claim attacked:** any "SUT-A is notably higher on design-X" observation read off the results grid.

**Evidence:** 10 designs, each with 1 headline + 2–7 companion metrics (design 06 alone reports 7
criteria + profile_mean, `metrics.py:171`). Even counting one headline per design that is
10 cells × 10 SUT-pairs = **100 pairwise comparisons**; including companions and the 06 criteria it
exceeds 200. At α=0.05 uncorrected, ~10 will look "significant" by chance alone. The pilot has no
multiplicity budget defined anywhere in the boot prompt or fit memo.

**Refutation (steelman):** "Descriptive-only ⇒ no hypothesis tests ⇒ no multiplicity problem." —
Survives *only if the discipline is actually enforced*: no p-values, no significance verbs, no
starred cells. The danger is the human reading 200 cells and narrating the 3 biggest gaps as
findings — that is uncorrected multiple comparison by eyeball. The problem is real; the fix is
procedural.

**Remedy:** Pre-commit (before the run) to which cells are *reportable* and forbid post-hoc
gap-hunting narration. If ANY comparative claim is made, apply a blunt correction (Bonferroni over
the pre-registered comparison count) and report it as illustrative not confirmatory. Default:
report the full grid with CIs, narrate none of the pairwise gaps.

---

## SD-4 — 60-item MVP subset is decision-poor: ~6 items/design, and ~3 units on paired designs
**Severity: MAJOR. Pilot-blocking: NO (scope recommendation).**

**Claim attacked:** that a 60-item MVP subset is an adequate substitute for the full 344 to learn
per-design behavior at lower cost.

**Evidence:** 60 items ÷ 10 designs = ~6 items/design. On the FIVE paired designs (03/04/08/09/10)
a say/do (etc.) "item" = 2 administrations = 1 effective unit, so 6 items → **~3 effective units**.
95% CI half-width at n=3 is **±0.375** (Wilson) — the interval is nearly the entire [0,1] range. At
n=6 single-admin designs it is ±0.312. A metric with a ±0.31–0.375 half-width carries essentially
no per-design information; you cannot even distinguish a rate of 0.3 from 0.7.

| design type in MVP-60 | ~eff n/SUT | 95% CI half-width |
|---|---:|---:|
| single (01/05/06) & ladder (02/07) | ~6 | ±0.312 |
| paired (03/04/08/09/10) | ~3 | ±0.375 |

**Refutation (steelman):** "MVP-60 is only to shake out ops/cost, not to measure — the full run
measures." — This survives and is the *correct* use. As a plumbing/cost smoke, 60 items is fine
(and matches the MVP-A1 comparability slice, `20260715-inspect-fit-assessment.md:70`). It does NOT
survive as a *descriptive-measurement* substitute. Cost-per-decision-information strongly favors the
full 344 for any measurement claim; the MVP-60 is a smoke, not a pilot.

**Remedy:** Run MVP-60 only as the ops/comparability check. For descriptive claims, run full 344 —
the per-design n's above (24–44) are already the floor; halving them via a subset is not defensible.
State explicitly that MVP-60 yields NO per-design measurement.

---

## SD-5 — Reporting raw fractions "with n adjacent" is necessary but NOT sufficient at n≤44
**Severity: MAJOR. Pilot-blocking: NO (reporting-standard upgrade).**

**Claim attacked:** that v1 G10 discipline (per-design cells, n adjacent) is enough discipline for
the pilot.

**Evidence:** G10 (`walkworthy-mvp-manuscript.md:850`) forbids composites without cells — it is a
*disaggregation* gate, not an *uncertainty* gate. A cell reading "0.62 (n=29)" still invites the
reader to treat 0.62 as a point estimate. At n=29 the Wilson 95% CI is [0.44, 0.77] — the reader
cannot recover that from "n=29" alone.

**Refutation (steelman):** "Sophisticated readers know small n ⇒ wide CI." — Does not survive:
the whole failure mode of small-n benchmark tables is that readers (and downstream citations) lift
the point estimate and drop the n. Making the interval *visible* is the only reliable guard.

**Remedy:** Every cell = point estimate + explicit 95% Wilson interval (for rates) or bootstrap
interval (for the continuous deltas: motive_sensitivity_index, mercy_delta, say_do_gap, break_turn).
n adjacent stays, but the interval is mandatory, not optional.

---

## SD-6 — Single-judge noise is large enough to swamp most SUT-vs-SUT differences
**Severity: CRITICAL. Pilot-blocking: NO — but a judge-B re-score is strongly advised.**

**Claim attacked:** that any observed SUT-vs-SUT difference reflects SUT behavior rather than judge
stochasticity.

**Evidence:** The replay evidence is 73.2% v2-vs-v1-judge exact field-cell agreement, against a
59.2% *judge-A-vs-judge-B* natural baseline (`20260715c-...md:18`). The per-design table there is
worse on the very fields several headlines depend on:
- `revealed_artifact` (design 03 say_do_gap input): exact 62%, **κ=0.33 / 0.20** (`:84`)
- `frame` / `facts` (design 06 profile): exact **40% / 40%**, and `facts` 20% (`:102–103`)
- `expressed_judgment` (design 03): κ=0.71 one judge but **κ=0.06** the other (`:83`)

A headline like say_do_gap is a *difference of two judged categories*, so it inherits the noise of
BOTH; with revealed_artifact at κ≈0.2–0.33, a large share of any say_do_gap SUT-difference could be
judge disagreement. Single judge + these κ's means the error bar in SD-1/SD-5 UNDERSTATES total
uncertainty (it captures item sampling, not judge stochasticity).

**Refutation (steelman):** "73.2% > 59.2% baseline means the v2 judge path is *more* consistent
than v1's own two judges, so judge noise is acceptable." — Survives as a *harness-parity* claim (v2
is not worse than v1) but NOT as a *measurement-adequacy* claim: 59.2%/κ≈0.2–0.6 is the noise floor
of the instrument itself, and both harnesses sit near it. Being no worse than a noisy baseline does
not make the baseline quiet enough to rank models.

**Remedy:** Budget a judge-B re-score for the pilot (cheap — judge-tokens only, no SUT re-run, via
`inspect score`; the fit memo §1 and `20260715d-` already validate this path). Report each headline
under BOTH judges; where they disagree in ordering, the cell is "judge-sensitive — no SUT claim."
This is the single highest-value addition per dollar and is nearly free relative to the SUT run.

---

## SD-7 — Single run per item, stochastic decoding, no seed/replication
**Severity: MAJOR. Pilot-blocking: NO (caveat + optional cheap mitigation).**

**Claim attacked:** that one administration per (item, SUT) yields a stable per-item outcome.

**Evidence:** The pilot design (boot prompt Phase 4) is one Inspect eval per design × 5 SUTs — a
single generation per item, no seed control, no replication. SUTs decode stochastically; a binary
per-item outcome (broke / didn't; faithful / not) is a single Bernoulli draw whose *within-item*
variance is invisible. Combined with SD-2's ladder fragility (a stochastic bad turn zeros an 02/07
item) and SD-6's judge non-determinism, an observed cell is one draw from a distribution whose width
is unmeasured on TWO axes (SUT sampling + judge sampling).

**Refutation (steelman):** "The item is the replication unit — averaging over 24–44 items already
integrates over stochasticity, so per-item replication is redundant." — Largely survives for the
*mean*: item-level averaging does absorb per-item decode noise into the reported rate, and the
Wilson interval already reflects that binomial variation. It does NOT survive for (a) any per-item
claim ("SUT broke on item WW-02-Axx"), which is a single draw, and (b) the paired-difference
designs, where both arms are single draws and their difference doubles the decode variance per pair.

**Remedy:** Keep single-run for the pilot (replication triples cost) but (a) forbid per-item
narrative claims, (b) state "single-run, stochastic decode, unreplicated" as a standing caveat, and
(c) optionally re-run ONE small design (e.g. 10, N/U, n=32) at k=3 seeds as a cheap decode-stability
probe to bound the effect — analogous to the v1 stochastic-stability side-probe.

---

## What survives

- **SD-1 (CRITICAL, blocking as claim-guard):** rankings/pairwise-order claims do not survive;
  gaps must exceed ~0.28 raw rate at n≈24–29 to be non-coin-flip, single-comparison.
- **SD-2 (CRITICAL, blocking as 02/07 guard):** the any-bad-turn-excludes-item cascade already
  produced n=1 live; 02/07 need an n-floor and mandatory n/excluded reporting.
- **SD-6 (CRITICAL):** judge noise (κ≈0.2–0.6 on load-bearing fields; 59.2% two-judge baseline) can
  swamp SUT differences; a judge-B re-score is near-free and should be run.
- **SD-3, SD-4, SD-5, SD-7 (MAJOR):** multiplicity discipline, MVP-60-is-a-smoke-not-a-pilot,
  intervals-not-just-n, single-run caveat — all survive as discipline/scope requirements.

Nothing here blocks *executing* the run; two findings (SD-1, SD-2) block *claiming* beyond a narrow
scope. Concessions granted: the harness/parity story (73.2% vs 59.2%) survives as adequacy of v2 vs
v1; item-level averaging (SD-7) legitimately absorbs decode noise into the mean; MVP-60 survives as
an ops smoke.

---

## Positive: the claim-scope I WOULD endorse for an n=5 descriptive pilot

Feeds the pilot-design memo. An n=5-SUT, full-344 pilot CAN legitimately support:

1. **Per-design cell tables** — one cell per (design, SUT) = point estimate + **95% Wilson interval
   (rates) / bootstrap interval (continuous deltas)** + **n and excluded adjacent** (v1 G10 +
   mandatory intervals). This is the primary deliverable.
2. **Existence / feasibility claims** — "the harness runs 5 SUTs × 10 designs end-to-end at
   $X; here is what the metric distribution looks like." Descriptive shape, not ranking.
3. **Design-instrument diagnostics** — which designs have healthy effective n vs which collapse
   under the exclusion cascade (02/07); which metrics show floor/ceiling saturation across all 5
   SUTs (→ candidate item revisions for v-next). This is arguably the pilot's *most* valuable output.
4. **Judge-sensitivity map** — under judge-A vs judge-B, which cells flip ordering. Flags fragile
   metrics for the canonical v1 effort.
5. **Coarse, hedged, interval-gated observations** — ONLY where two SUTs' 95% intervals are fully
   disjoint on a pre-registered cell, "SUT-X is higher than SUT-Y on design-Z at pilot n" is
   permissible, tagged single-comparison and judge-checked. Expect very few such cells.

The pilot MAY NOT support: any leaderboard/composite (even with cells), any full 5-way ranking, any
per-item claim, any significance/starred claim, or any MVP-60-based measurement. All pilot outputs
must carry "descriptive; v1 remains canonical for release evidence" (per the parallel ruling
`20260716-owner-ruling-v2-parallel.md`).
