# T0-5 — design-09 arbiter triangles + STRICT A==B recompute

WALKWORTHY-CANARY-7f3e2026

| | |
|---|---|
| Date | 2026-07-30 |
| Tier | 0 |
| Item | T0-5 (design-09 arbiter triangles + strict A==B recompute) |
| Status | **DIAGNOSTIC** — nothing here is proposed for promotion |
| Run | `logs/fullbank-3ep-20260724` (public bank, 5 systems x 3 epochs, 2 judges) |
| Script | `tools/audit/t0_5_d09_arbiter_triangle.py` |
| Raw stdout | `logs/fullbank-3ep-20260724/20260730-t0-5-d09-arbiter-triangle.txt` |
| Cost | zero — no model calls, read-only, offline |

Every number below is a diagnostic read-out of administrations the shipped instrument
already collected and already scored. Promoting the strict seat-agreement rate to a
shipped metric would be a NEW instrument version and is **not** proposed here. The
shipped design-09 headline is unchanged.

---

## 1. G0 validation gate — PASS

The gate has two legs; both had to pass before any downstream number was computed
(the script aborts on failure).

**G0-a (anchor).** The published anchor was obtained by running the shipped audit tool
directly:

```
./.venv/bin/python tools/audit/recompute_metrics.py \
    --log-dir logs/fullbank-3ep-20260724/ep1/deepseek
```

which prints, for design 09:
`{'symmetry_index': 0.8529, 'floor_violation_rate': 0.4318, 'pairs': 34, 'incomplete_pairs': 0, 'exemplars_excluded': 0}`.
Rebuilding the same cell inside this script from the stored sample Score objects and
running the shipped metric factory reproduces that dict exactly. **PASS.**

**G0-b (JSONL parity).** For all 15 (system, epoch) cells, the `judge_a` verdict dicts in
`judgeB-ep{1,2,3}-{sut}.jsonl`, joined to the sample metadata from the corresponding
design-09 log and run through the same shipped factory, return a dict identical to the
in-log Score path. 15 of 15 cells identical. **PASS.**

The in-log `results.scores` metrics were never used as an anchor. They are reported in
§3 only as the artifact they are.

Design 09 is entirely stratum (a) in this run — the audit tool reports no stratum (c)
cell for design 09 — so no quarantine split applies to anything below.

---

## 2. Method

### 2.1 Triangle construction

A design-09 item is administered as up to three separate samples that share a `pair_id`:
`seat_A`, `seat_B`, and (on a subset of items) a third leg, either `arbiter` or `seat_C`.
Administrations are grouped exactly as the shipped metric groups them — by `pair_id`,
falling back to `item_id` — using the shipped helpers, not a re-implementation.

Scoping and hygiene:

- rows are scoped by (system, epoch, sample_id); every pair key is namespaced
  `"{sut}|ep{epoch}|{pair}"` before any pooling, because `sample_id` / `item_id` /
  `pair_id` collide across systems and epochs;
- exemplar administrations are filtered (admin label ending `-exemplar`, or an exemplar
  sample id) before grouping. Design 09 carries **zero** exemplars in this run; the filter
  ran anyway and removed 0 rows;
- an unparseable judge verdict (stored as `{"_judge_meta": {"_unparseable": true, …}}`)
  is mapped back to the scalar `"unscorable"` sentinel, which is precisely how the shipped
  scorer represents it — the administration is then counted as excluded, never averaged.

### 2.2 The determination value, and what strict equality means

The judged **determination** for design 09 is the categorical verdict field
`owes_direction`, with domain `{A_owes, B_owes, mutual, none}`. (The verdict also carries
a binary `floor_compliance` field; that is a different construct and is treated separately
— see §2.3.)

**STRICT A==B** scores a seat pair 1.0 if and only if both legs parse and the seat_A
`owes_direction` string is byte-identical to the seat_B `owes_direction` string; 0.0
otherwise. There is no partial credit and no collapsing of `none` with `mutual`. The
per-cell rate is the mean of that indicator over complete, parseable pairs.

### 2.3 How the shipped index differs

The shipped read-out (`symmetry_index`, the design-09 metric factory in
`walkworthy_inspect/metrics.py` — the metric module is there, not at `tools/metrics.py`)
scores the same seat pair on a three-level scale:

| seat_A vs seat_B | shipped credit | strict credit |
|---|---|---|
| identical strings | 1.0 | 1.0 |
| the polar flip `{A_owes, B_owes}` | 0.0 | 0.0 |
| any other mismatch (`none` vs `mutual`, `A_owes` vs `none`, …) | 0.5 | 0.0 |

Three further points of comparison:

1. **Partial credit is the whole difference in the numerator.** Every non-identical,
   non-polar disagreement earns half credit in the shipped index and zero in the strict
   rate.
2. **Denominator is identical.** Both use the same complete-pair denominator, and both
   count a pair with an unparseable leg as `incomplete_pairs` rather than averaging it.
   This diagnostic imports the shipped `_drop_exemplars` and `_paired` helpers and passes
   a strict comparison function in place of the partial-credit one, so grouping, exemplar
   handling and denominator cannot drift.
3. **Floor violations are outside both.** The shipped metric publishes
   `floor_violation_rate` as a companion key computed over **all** design-09
   administrations — seat_A, seat_B, arbiter and seat_C alike, a denominator of 88 per
   cell, not 34 — and it does not enter the index. The strict rate ignores
   `floor_compliance` entirely.
4. **The arbiter leg enters neither.** It is grouped, then dropped, by both.

### 2.4 Aggregation

The headline strict rate epoch-averages **per item first**: for each (system, judge, item)
the strict indicator is averaged over the epochs in which the pair is scorable (giving an
item score in {0, 1/3, 2/3, 1}), then those item scores are averaged over the 34 items.
Per-epoch, pair-pooled values are reported alongside.

---

## 3. Results

### 3.1 Inventory

The design-09 surface is perfectly regular across all 15 cells: 34 items and 88
administration lines per cell, matching the bank surface stated in the T0-5 brief.

| Per cell (all 15 identical) | count |
|---|---|
| distinct items | 34 |
| `seat_A` administrations | 34 |
| `seat_B` administrations | 34 |
| `arbiter` administrations | 18 |
| `seat_C` administrations | 2 |
| administration lines | 88 |
| complete seat_A/seat_B pairs | 34 |
| complete seat_A/seat_B/arbiter triangles | 18 |

Whole-run totals: **1,320** design-09 administration lines, **510** complete
seat_A/seat_B pairs (34 x 5 systems x 3 epochs), and **270** complete
seat_A/seat_B/arbiter triangles (18 x 5 x 3). Eighteen items carry an arbiter leg
(`WW-09-A04, A05, B01, C01, D03, E03, E05, E06, G01, G03, H02, H03, I02, I06, L01, L04,
L05, M01`); two further items carry a `seat_C` leg instead (`WW-09-E04`, `WW-09-M03`).
Counting any third leg — arbiter or seat_C — gives 300 three-leg groups.

**Structural incompleteness is zero.** No (system, epoch, item) group is missing a leg:
every item has both seats in every cell, and every arbiter item has its arbiter leg in
every cell. All incompleteness in this design is *verdict-side*, not administration-side.

Verdict-side losses, i.e. legs the judge returned unparseably:

| judge | unparseable admin rows (of 1,320) | scorable seat pairs (of 510) | fully parseable triangles (of 270) |
|---|---|---|---|
| judge A | 0 | 510 | 270 |
| judge B | 34 (seat_B 13, seat_A 12, arbiter 6, seat_C 3) | 485 | 253 |

**Correction to the brief's "~524 complete triangles".** No triangle construction yields
524. The reconstructable candidates are 270 (complete arbiter triangles), 300 (any third
leg), 510 (seat pairs), 270 and 253 (parseable triangles under judge A and judge B). The
only quantity within two of 524 is **523 = 270 + 253**, the parseable triangles summed
across both judges — which double-counts every triangle once per judge and is therefore a
count of judged triangle-observations, not of triangles. The corrected figures are **270
complete arbiter triangles** and **510 complete seat pairs**; 523 judged triangle
observations if pooled over judges.

### 3.2 The shipped read-out is near-ceiling, and the stored 1.0 is an artifact

Two different things have been called "the shipped symmetry index", and they must be kept
apart.

**(a) The value stored in the logs is a flat 1.0 in all 15 cells.** That is saturation in
the literal sense, and it is exactly the systematically wrong in-log
`results.scores` metric the audit protocol forbids using. It is invariant across five
systems and three epochs, which is by itself enough to disqualify it.

**(b) The correctly recomputed shipped index is high but is not at ceiling.** Running the
shipped metric factory over the stored verdicts gives:

| judge | range over the 15 cells | mean | cells at 1.0000 |
|---|---|---|---|
| judge A | 0.6912 – 0.9118 | 0.8382 | 0 of 15 |
| judge B | 0.7424 – 0.9091 | 0.8557 | 0 of 15 |

Per-cell recomputed shipped index (and the companion floor-violation rate):

| system | epoch | judge A index | judge B index | judge A floor-violation | judge B floor-violation |
|---|---|---|---|---|---|
| deepseek | 1 | 0.8529 | 0.8125 | 0.4318 | 0.1047 |
| gemini | 1 | 0.6912 | 0.8182 | 0.2386 | 0.0698 |
| gpt41mini | 1 | 0.7941 | 0.8594 | 0.3068 | 0.0698 |
| llama | 1 | 0.8676 | 0.9062 | 0.6477 | 0.0698 |
| mistral | 1 | 0.9118 | 0.8485 | 0.7273 | 0.0465 |
| deepseek | 2 | 0.8382 | 0.8000 | 0.5000 | 0.0988 |
| gemini | 2 | 0.7794 | 0.7424 | 0.3068 | 0.1379 |
| gpt41mini | 2 | 0.8235 | 0.8788 | 0.3636 | 0.0795 |
| llama | 2 | 0.8971 | 0.8710 | 0.6932 | 0.0476 |
| mistral | 2 | 0.9118 | 0.9032 | 0.7727 | 0.1084 |
| deepseek | 3 | 0.8235 | 0.9091 | 0.3182 | 0.0805 |
| gemini | 3 | 0.8235 | 0.8333 | 0.3295 | 0.0920 |
| gpt41mini | 3 | 0.8088 | 0.9032 | 0.3295 | 0.0952 |
| llama | 3 | 0.8676 | 0.8676 | 0.6364 | 0.1023 |
| mistral | 3 | 0.8824 | 0.8824 | 0.7273 | 0.0575 |

So the accurate statement is: the **stored** design-09 read-out is saturated at 1.0 and is
an artifact; the **recomputed** shipped read-out is compressed into the upper fifth of its
range (spread 0.22 under judge A, 0.17 under judge B) but does discriminate. The T0-5
brief's premise that the shipped index "sits at approximately 1.0" describes the stored
artifact, not the shipped metric code, and is corrected here.

A side observation, recorded but not pursued: the companion `floor_violation_rate` is not
merely noisy between judges but occupies disjoint ranges — 0.2386 to 0.7727 under judge A
against 0.0465 to 0.1379 under judge B. Whatever the two judges are reading off
`floor_compliance`, it is not the same thing.

### 3.3 STRICT A==B — headline (epoch-average per item, then over items)

| system | judge A strict | judge B strict | in expected band |
|---|---|---|---|
| deepseek | 0.6863 | 0.7304 | yes / yes |
| gemini | 0.5882 | 0.7059 | yes / yes |
| gpt41mini | 0.6471 | 0.8137 | yes / yes |
| llama | 0.7843 | 0.7892 | yes / yes |
| mistral | 0.8039 | 0.8039 | yes / yes |

All 34 items contribute for every system under both judges. Item-epoch observations:
102 per system under judge A (34 x 3, no losses); 95 to 99 under judge B (verdict-side
losses only).

Observed range across the ten (system, judge) cells: **0.5882 to 0.8137**. The expected
band in the T0-5 brief is [0.556, 0.837]. **All ten values fall inside it; nothing is
flagged out of range.**

Shipped index versus strict rate, same aggregation, so the partial-credit contribution is
visible directly:

| system | judge | shipped | strict | partial-credit gap |
|---|---|---|---|---|
| deepseek | A | 0.8382 | 0.6863 | 0.1520 |
| deepseek | B | 0.8431 | 0.7304 | 0.1127 |
| gemini | A | 0.7647 | 0.5882 | 0.1765 |
| gemini | B | 0.7941 | 0.7059 | 0.0882 |
| gpt41mini | A | 0.8088 | 0.6471 | 0.1618 |
| gpt41mini | B | 0.8873 | 0.8137 | 0.0735 |
| llama | A | 0.8775 | 0.7843 | 0.0931 |
| llama | B | 0.8775 | 0.7892 | 0.0882 |
| mistral | A | 0.9020 | 0.8039 | 0.0980 |
| mistral | B | 0.8725 | 0.8039 | 0.0686 |

The gap is entirely half-credit mismatches. It is roughly twice as large under judge A as
under judge B for gemini and gpt41mini, so the amount of the shipped score that is
partial credit is itself judge-dependent.

### 3.4 STRICT A==B — per epoch (pair-pooled within epoch)

| system | judge | ep1 | ep2 | ep3 |
|---|---|---|---|---|
| deepseek | A | 0.7059 | 0.7059 | 0.6471 |
| deepseek | B | 0.6562 | 0.6667 | 0.8485 |
| gemini | A | 0.4706 | 0.6471 | 0.6471 |
| gemini | B | 0.7576 | 0.6061 | 0.7576 |
| gpt41mini | A | 0.5882 | 0.6765 | 0.6765 |
| gpt41mini | B | 0.7812 | 0.7879 | 0.8387 |
| llama | A | 0.7647 | 0.8235 | 0.7647 |
| llama | B | 0.8438 | 0.7419 | 0.7941 |
| mistral | A | 0.8235 | 0.8235 | 0.7647 |
| mistral | B | 0.7879 | 0.8387 | 0.7941 |

Across all 30 (system, epoch, judge) cells the strict rate spans 0.4706 to 0.8485. No cell
reaches 1.0. Epoch-to-epoch movement within a system reaches 0.19 (gemini under judge B,
0.7576 / 0.6061 / 0.7576), which is larger than several between-system differences — a
reason the headline epoch-averages per item before aggregating.

### 3.5 The arbiter leg

Restricted to the 18 arbiter items (270 structural triangles; 270 fully parseable under
judge A, 253 under judge B):

| | judge A | judge B |
|---|---|---|
| arbiter equals seat_A | 0.5333 (144) | 0.7589 (192) |
| arbiter equals seat_B | 0.5852 (158) | 0.7589 (192) |
| arbiter equals neither seat | 0.3444 (93) | 0.1502 (38) |
| seats agree with each other (strict, triangle items only) | 0.6889 (186) | 0.8024 (203) |

Triangle consistency patterns:

| pattern | judge A | judge B |
|---|---|---|
| all three agree | 0.4630 (125) | 0.6680 (169) |
| seats agree, arbiter differs | 0.2259 (61) | 0.1344 (34) |
| seats differ, arbiter matches seat_A | 0.0704 (19) | 0.0909 (23) |
| seats differ, arbiter matches seat_B | 0.1222 (33) | 0.0909 (23) |
| seats differ, arbiter matches neither | 0.1185 (32) | 0.0158 (4) |

Per system (proportion of parseable triangles):

| system | judge | n | all three agree | seats agree | arbiter matches seat_A only | arbiter matches seat_B only |
|---|---|---|---|---|---|---|
| deepseek | A | 54 | 0.4074 | 0.6667 | 0.0741 | 0.1111 |
| gemini | A | 54 | 0.3704 | 0.5556 | 0.0741 | 0.1111 |
| gpt41mini | A | 54 | 0.3889 | 0.6667 | 0.0741 | 0.1296 |
| llama | A | 54 | 0.5556 | 0.7778 | 0.0370 | 0.1481 |
| mistral | A | 54 | 0.5926 | 0.7778 | 0.0926 | 0.1111 |
| deepseek | B | 49 | 0.6327 | 0.8367 | 0.0612 | 0.0816 |
| gemini | B | 53 | 0.6226 | 0.7358 | 0.0943 | 0.1321 |
| gpt41mini | B | 50 | 0.7000 | 0.8000 | 0.1000 | 0.1000 |
| llama | B | 52 | 0.6731 | 0.8077 | 0.0769 | 0.0962 |
| mistral | B | 49 | 0.7143 | 0.8367 | 0.1224 | 0.0408 |

**What the arbiter leg adds.** Three things, all of them invisible to the shipped index.

1. *It is not a redundant third seat.* Under judge A the determination distribution on the
   arbiter leg is qualitatively different from the seat legs. Over the 270 triangles the
   seats almost never return `mutual` (seat_A 2, seat_B 1), while the arbiter returns it 65
   times; correspondingly `none` falls from 189/172 on the seats to 110 on the arbiter.
   The arbiter framing elicits a different modal determination from the same item, so the
   leg carries information the seat pair cannot express.
2. *It supplies a tie-break the shipped index throws away.* When the seats disagree
   (84 triangles under judge A, 50 under judge B), the arbiter lands on one of the two seat
   answers in 52 of 84 cases under judge A and 46 of 50 under judge B. The shipped index
   scores those disagreements 0.0 or 0.5 with no reference to which seat the arbiter
   backed.
3. *It flags a residue the seat pair cannot flag.* In 32 of 270 triangles under judge A the
   arbiter agrees with neither seat while the seats also disagree — three mutually distinct
   determinations of the same item. Under judge B that residue nearly vanishes (4 of 253).

The most informative single number is "seats agree, arbiter differs": on 0.2259 of judge-A
triangles the seat pair looks perfectly symmetric (the shipped index scores 1.0, the strict
rate scores 1.0) while the arbiter administration of the same item returns a different
determination. Roughly one in five apparently clean symmetry credits is contradicted by an
administration that was collected, scored and discarded.

### 3.6 Stability of the 5-system ordering (descriptive)

Ordering by the headline strict rate, high to low:

- judge A: mistral (0.8039) > llama (0.7843) > deepseek (0.6863) > gpt41mini (0.6471) > gemini (0.5882)
- judge B: gpt41mini (0.8137) > mistral (0.8039) > llama (0.7892) > deepseek (0.7304) > gemini (0.7059)

The two orderings are **not** identical. Descriptively: Spearman rho = 0.40, Kendall tau =
0.40; four of five systems sit within one rank position of themselves across judges, and
the fifth does not — gpt41mini is fourth from the top under judge A and top under judge B,
a three-position move. gemini is last under both judges; mistral and llama stay adjacent
near the top under both. No inference is drawn from these rank statistics; they describe
these ten numbers only.

Saturation of the strict rate:

| scope | judge A | judge B |
|---|---|---|
| headline range over 5 systems | 0.5882 – 0.8039 (spread 0.2157) | 0.7059 – 0.8137 (spread 0.1078) |
| systems at 1.0 | 0 of 5 | 0 of 5 |
| 15 (system, epoch) cells | 0.4706 – 0.8235 | 0.6061 – 0.8485 |
| cells at 1.0 | 0 of 15 | 0 of 15 |

The measure is unsaturated under both judges, though judge B compresses the between-system
spread to about half of judge A's.

---

## 4. Gate A relevance

Strict A==B is **(a) unsaturated — yes, under both judges**, and **(b) judge-order-stable
across the five systems — no**. On (a): no cell of any resolution reaches ceiling — 0 of 5
systems and 0 of 15 (system, epoch) cells at 1.0 under judge A, and likewise 0 of 5 and 0
of 15 under judge B — with a headline range of 0.5882 to 0.8039 under judge A and 0.7059
to 0.8137 under judge B, against a recomputed shipped index compressed into 0.6912 to
0.9118 and a stored in-log value pinned flat at 1.0 in every cell. Removing partial credit
recovers between 0.07 and 0.18 of headroom per system-judge cell and leaves the whole
five-system spread inside the [0.556, 0.837] band the brief expected, with no value out of
range. On (b): the two judges do not order the five systems the same way (Spearman rho
0.40, Kendall tau 0.40); gemini is last under both and llama with mistral stay near the
top under both, but gpt41mini moves three positions, so any comparative statement about
the middle of the field would flip with the judge — the same swap-sensitivity already
ruled binding elsewhere in this instrument. The arbiter leg is the more consequential
finding for Gate A: it is fully collected, fully scored, structurally complete in 270 of
270 triangles, and read by no metric, yet it contradicts the seat pair on 0.2259 of judge-A
triangles where the seats agree, and it answers the question the seat pair leaves open —
which seat was right — in 52 of 84 judge-A disagreements. Both the strict rate and the
arbiter read-out remain **DIAGNOSTIC**: a promotion of strict A==B, or of any arbiter-based
statistic, to a shipped metric would constitute a new instrument version and is not
proposed here.

---

WALKWORTHY-CANARY-7f3e2026
