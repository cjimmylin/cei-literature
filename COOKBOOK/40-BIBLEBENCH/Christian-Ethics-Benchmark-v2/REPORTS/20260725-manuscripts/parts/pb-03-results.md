**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content

> **PART FILE — assembles into paper (b).** §1, §6 and §7 are drafted in
> `pb-01-intro-limitations-future.md`; §2 related work and §3–§4 are drafted separately.
> Target paper: *Judging the Judges for $0: A Two-Referee Concordance Method for Localizing
> LLM-as-Judge Failure on Value-Laden Rubrics.* Venue-generic and author-generic by ruling.

---

## 5 Results

### 5.1 Run shape and integrity

The measurement run administers the full public bank at revision 2026-07-24b — 344 items,
all runnable, expanding to 563 administration lines — to five systems under test, in three
independent single-epoch runs, followed by a full second-judge rescore pass over every
stored transcript. The design is therefore balanced: five systems × two judges × three
epochs, with the epochs functioning as replicates.

All 150 scoring runs (10 designs × 5 systems × 3 epochs) returned success, with zero
non-success statuses and no provider failures. Sample counts are 563 per system per epoch,
matching the bank-parity report design by design, for **8,445 total administrations**. The
second-judge pass ran 15 times (one per epoch × system cell), and all 15 returned exit code
0 with 563 rows each — **8,445 verdict rows** in total, from **14,235 judge-B calls**. All 15
epoch × system cells report at 10 of 10 designs, and there is **no sample-count drift across
epochs in any of the 50 design × system cells**. The run matrix took 3h56m wall-clock and the
second-judge pass 1h12m; per-system wall-clock spread was 3×, with one system alone setting
the critical path while a different system set the cost.

Spend was **$8.5319 exact** for the systems under test, judge-A and the branch classifier
across three epochs, plus **approximately $2.70 estimated** for the judge-B rescore, for
**about $11.23 all-in against a $16.00 authorized ceiling** (70% of ceiling, +3.0% on the
pre-run estimate). The judge-B component is an estimate rather than a measurement, and the
reason is worth stating plainly because it is a reproducibility hazard for anyone building
the same apparatus: **the rescore tool does not record token usage**, so its spend is not
recoverable from its own artifacts. Two independent reconstructions agree — scaling judge-A's
prompt volume at judge-B prices gives $2.73, and scaling the pilot's recorded figure by the
exact 3.00× administration ratio gives $2.70. **Both are upper bounds**, because judge-A's
token volume includes the branch-classifier calls that judge-B never makes. Account-level
usage could not be differenced because sibling projects share the key.

One methodological note on integrity verification, because it changed our practice.
Integrity was confirmed against each run log's own structured `status` field, **not** against
a text scan of console output. A text search for `402` over the run streams produced a **false
positive** by matching inside the token count `47,402`. Structured-field verification is the
standard adopted here; console-text verification of a numeric error condition is unsafe
whenever the same digits can appear inside an unrelated count.

**Comparability fences (binding).** (1) These are the **first-ever numbers on bank revision
2026-07-24b**; the pre-registered contrast families are therefore reportable *as
pre-registered* rather than as post-hoc, and this was declared before first use. (2) They are
**not comparable to the 2026-07-16 pilot** except under standing caveats: three design-07
items were unscorable then, one design-08 item was re-keyed, design-05 constraint satisfaction
was silently waived on zero-budget items, design-04 zero-keyed items were pooled into the
signed mean, and four items' prompt text changed. (3) **Design 08 is its own fence line** — this
is the first full-bank run under its post-anchor judge rubric, and pre-anchor design-08
verdicts are not comparable cells. (4) The **branch classifier is pinned** at `gpt-4.1-nano`,
carrying a documented cross-family disagreement property as a known instrument condition;
under the project's no-cross-classifier-pooling rule, **these cells may never be pooled with
cells from any future cross-family classifier pin**. (5) **Public bank only — the holdout was
untouched** and remains quarantined for a future blind first-use run. The harness reported on
here is the parallel research harness; a separate canonical harness remains the release path
for the benchmark project's own evidence, and nothing below is offered as release evidence.

### 5.2 Ordering flips at full bank

The judge-swap test asks, per design and per epoch, whether the ordering of the five systems
on that design's headline metric is preserved when judge-A's verdicts are replaced by
judge-B's over the identical stored transcripts. The test is offline and costs nothing.

| design | ep1 | ep2 | ep3 | verdict |
|---|:--:|:--:|:--:|---|
| 01 goodsamaritan | flips | flips | flips | judge-sensitive (all epochs) |
| 02 twomasters | flips | flips | flips | judge-sensitive (all epochs) |
| 03 quiettongue | flips | flips | STABLE | stability not reproducible |
| 04 innerweight | flips | STABLE | flips | stability not reproducible |
| 05 ordoamoris | STABLE | STABLE | STABLE | stable by construction (judge-free primary) |
| 06 crookedpath | flips | STABLE | STABLE | stability not reproducible |
| 07 seventyseven ▲ | — | — | — | **ordering undefined** (floor-saturated; judge-A is 0.000 on all five systems in ep1/ep2) |
| 08 vocationfork | flips | flips | flips | judge-sensitive (all epochs) |
| 09 doubleedge | flips | flips | flips | judge-sensitive (all epochs) |
| 10 strangergate | flips | flips | flips | judge-sensitive (all epochs) |

**Eight of the nine judged designs flip.** Design 07 is excluded from this count: it is floor-saturated, its judge-A headline is 0.000 on all five systems in epochs 1 and 2, and it therefore has no ordering to preserve or permute — the tool's recorded flip there is a stable-sort tie-break artefact, not a disagreement. The one judged design that never flips is design 05, and it is the one
design whose primary metric never reaches a judge at all: its constraint-satisfaction rate is
computed from a parsed allocation against keyed constraints.

The reading is the following. An ordering that holds in one epoch and flips in another is not
a stable ordering; it is a coincidence at that sample. Designs 03, 04 and 06 must therefore be
read as judge-sensitive, not as intermittently stable, and no comparative claim is available
on any of the nine.

The per-design headline cells for both judges are reproduced below as **descriptive instrument
readings**. Per-cell Wilson intervals are emitted per epoch in the run artifacts. **No ordering
claim is made from this table, and readers should not reconstruct one**: the analysis in §5.2
through §5.4 is precisely the finding that such an ordering does not reproduce under a
different judge.

| design | headline | judge | deepseek | mistral | gemini | llama | gpt-4.1-mini |
|---|---|---|---:|---:|---:|---:|---:|
| 01 | full_obedience_rate | A | 0.712 | 0.515 | 0.742 | 0.530 | 0.576 |
| 01 | | B | 0.646 | 0.523 | 0.532 | 0.583 | 0.452 |
| 02 | break_rate | A | 0.429 | 0.348 | 0.517 | 0.570 | 0.379 |
| 02 | | B | 0.711 | 0.688 | 0.622 | 0.414 | 0.646 |
| 03 | say_do_gap | A | 0.512 | 0.459 | 0.402 | 0.553 | 0.310 |
| 03 | | B | 0.066 | −0.064 | −0.092 | −0.053 | −0.116 |
| 04 | motive_delta_mean | A | 0.202 | 0.200 | 0.187 | 0.246 | 0.144 |
| 04 | | B | 0.157 | 0.127 | 0.081 | 0.209 | 0.035 |
| 05 | csr_mean | A | 0.928 | 0.903 | 0.900 | 0.898 | 0.920 |
| 05 | | B | 0.928 | 0.903 | 0.900 | 0.898 | 0.920 |
| 06 | profile_mean | A | 0.861 | 0.424 | 0.935 | 0.574 | 0.827 |
| 06 | | B | 0.957 | 0.763 | 0.965 | 0.839 | 0.936 |
| 07 | arc_pass_rate | A | 0.012 | 0.000 | 0.000 | 0.000 | 0.000 |
| 07 | | B | 0.000 | 0.000 | 0.062 | 0.014 | 0.014 |
| 08 | covert_overt_gap | A | 0.109 | 0.088 | 0.230 | 0.161 | 0.190 |
| 08 | | B | 0.295 | 0.223 | 0.212 | 0.173 | 0.199 |
| 09 | symmetry_index | A | 0.838 | 0.902 | 0.765 | 0.877 | 0.809 |
| 09 | | B | 0.841 | 0.878 | 0.798 | 0.882 | 0.881 |
| 10 | mercy_delta | A | 0.031 | 0.005 | 0.036 | 0.021 | 0.078 |
| 10 | | B | −0.022 | 0.011 | 0.018 | 0.054 | 0.022 |

### 5.3 Single-epoch stability verdicts are unreliable

This is a new methodological result, and it is one the single-epoch pilot could not have
produced. It is available only because the run replicates.

Designs 03, 04 and 06 each register STABLE in one or two epochs and judge-sensitive in the
others: design 03 flips in epochs 1 and 2 and is stable in epoch 3; design 04 flips in epochs
1 and 3 and is stable in epoch 2; design 06 flips in epoch 1 and is stable in epochs 2 and 3.
**A single-epoch run would have reported those three orderings as stable**, and the stability
does not reproduce. Only design 05 is stable in all three epochs, and it is stable by
construction rather than by measurement.

The stability verdict is therefore itself a sampled quantity with its own sampling
distribution, and reporting one epoch's verdict reports a draw from that distribution rather
than a property of the instrument. The operational consequence is a budget rule: **future
measurement runs should budget at least three epochs before any stability claim**, alongside
the two-judge pass that the pilot already established as first-class. Replication is not only
a precision device here; it is what makes the judge × system interaction estimable separately
from residual error in the first place, as §5.4 depends on.

### 5.4 The variance decomposition — how much is the judge

The swap test yields a binary verdict per design. It does not say *how much* of what the
instrument measures is attributable to the judge rather than to the model. Because three
epochs were run, that quantity is recoverable from data already on disk at zero additional
cost, by treating each design as a balanced 5 (system) × 2 (judge) layout with the three
epochs as replicates and decomposing the total sum of squares in the reported headline into
system, judge, system × judge, and error.

| design | headline | SS_total | %SUT | %judge | %SUT×judge | %error |
|---|---|---:|---:|---:|---:|---:|
| 01 goodsamaritan | full_obedience_rate | 0.28656 | 45.4 | 12.0 | 23.0 | 19.6 |
| 02 twomasters | break_rate | 0.52187 | 5.8 | 40.3 | 46.5 | 7.4 |
| 03 quiettongue | say_do_gap | 2.10168 | 6.6 | 88.8 | 1.4 | 3.2 |
| 04 innerweight | motive_delta_mean | 0.13657 | 46.3 | 30.1 | 4.9 | 18.7 |
| 05 ordoamoris ◆ | csr_mean | 0.01580 | 27.4 | 0.0 | 0.0 | 72.6 |
| 06 crookedpath | profile_mean | 0.87070 | 63.4 | 24.2 | 11.4 | 0.9 |
| 07 seventyseven ▲ | arc_pass_rate | 0.01417 | 24.5 | 12.8 | 33.9 | 28.8 |
| 08 vocationfork | covert_overt_gap | 0.18671 | 9.1 | 16.8 | 25.9 | 48.3 |
| 09 doubleedge | symmetry_index | 0.08034 | 54.4 | 2.9 | 9.9 | 32.8 |
| 10 strangergate | mercy_delta | 0.03453 | 25.8 | 6.9 | 25.8 | 41.5 |

◆ judge-free primary — the positive control. ▲ floor-saturated; its percentages describe noise
around a floor and are excluded from the summary.

Across the eight judged, non-saturated designs (01, 02, 03, 04, 06, 08, 09, 10):

| component | median | range |
|---|---:|---|
| SUT (do the models differ) | 35.6% | 5.8–63.4% |
| judge (severity shift) | 20.5% | 2.9–88.8% |
| SUT × judge (which model is better) | 17.2% | 1.4–46.5% |
| error (epoch noise) | 19.1% | 0.9–48.3% |

Judge footprint (main effect plus interaction) has median **35.3%**; system footprint has
median **35.6%**; the ratio is **1.0×**. The judge footprint exceeds the system footprint in
**4 of 8** designs.

**This does not say that the judge overwhelms the model, and the paper does not claim it.**
Judge and system footprints are comparable at the median, and the system main effect is the
single largest term in several designs — 63.4% on design 06, 54.4% on design 09, 46.3% on
design 04, 45.4% on design 01. **The models genuinely differ**, and any reading of these
results as "the measurement is only about the judge" misstates them.

The decision-relevant term is the **interaction**, not the main-effect ratio. A large system
main effect says the models differ; it does not license a *ranking* if the judges disagree
about the order. That disagreement is exactly `SUT × judge`, and it is **non-zero in all 8 judged, non-saturated
judged designs**, median 17.2%.

| design | SUT×judge | SUT | note |
|---|---:|---:|---|
| 02 | 46.5% | 5.8% | judge disagreement swamps a near-absent model signal |
| 07 ▲ | 33.9% | 24.5% | floor-saturated; listed for completeness only |
| 08 | 25.9% | 9.1% | the covert-protection boundary, quantified |
| 10 | 25.8% | 25.8% | interaction equals the model effect |
| 01 | 23.0% | 45.4% | large system effect, judges still reorder it |
| 06 | 11.4% | 63.4% | large system effect, judges still reorder it |
| 09 | 9.9% | 54.4% | large system effect, judges still reorder it |
| 04 | 4.9% | 46.3% | smallest interaction among the judged designs |
| 03 | 1.4% | 6.6% | interaction small because the judge *level* shift is 88.8% |

**The precise claim the data support is therefore: the models differ, but the judges disagree
about the ordering in every judged design.** Designs 01, 06 and 09 are the sharpest
illustration — a substantial genuine model effect that nonetheless fails the swap test,
because an interaction of 9–23% is enough to permute the ranking of five closely-spaced
systems. This is the mechanism behind §5.2's flip result, and it is why no comparative claim
survives even where the instrument is plainly responding to the model.

Two designs are instructive special cases in opposite directions. **Design 03** is 88.8% judge
*level* shift with almost no interaction: the two judges apply near-uniformly different
thresholds, which collapses `say_do_gap` from roughly 0.31–0.55 under judge-A to approximately
zero or negative under judge-B on every system. **Design 02** is the reverse — a 46.5%
interaction sitting on a 5.8% model effect — making it the most judge-fragile instrument in
the suite.

**The positive control.** Design 05's primary metric is judge-free, so its judge and
system × judge terms must be exactly zero if the arithmetic is right. They are: **0.000000 and
0.000000**. This validates the decomposition on real data rather than on simulation.
Separately and independently, design 05's judge-A and judge-B headline cells are identical to
four decimal places on all five systems (Δ = 0.0000), which establishes that the rescore
pipeline introduces no drift — and therefore that **every nonzero judge-A/judge-B delta
elsewhere in the suite is a real judge effect rather than pipeline noise**.

### 5.5 The judge-free surface yields no distinction

An obvious objection to §5.4 is that the judge is merely obscuring a real ranking that a
cleaner instrument would recover. The suite contains the surface that tests this. Design 05's
`constraint_satisfaction_rate` never reaches a judge, so the two-judge precondition is
satisfied **by construction rather than by luck**, and it is the only surface in the suite
where a pre-registered comparative claim can survive.

The pre-registered contrast family C1 comprises 3 designs (04, 05, 10) × C(5,2) = **m = 30,
frozen**; with α = 0.05 the per-contrast threshold is 0.001667 and the two-sided z is 3.1440.
Per-item constraint-satisfaction values were averaged across the three epochs *before*
contrasting, so n = items rather than items × epochs — the latter would treble-count the same
item and understate the error.

| system | items | CSR mean | sd | Bonferroni-widened interval |
|---|---:|---:|---:|---|
| deepseek | 28 | 0.9292 | 0.1196 | [0.8581, 1.0002] |
| gpt-4.1-mini | 28 | 0.9224 | 0.1239 | [0.8488, 0.9961] |
| mistral | 27 | 0.9031 | 0.1586 | [0.8071, 0.9991] |
| gemini | 27 | 0.8996 | 0.1322 | [0.8196, 0.9796] |
| llama | 27 | 0.8979 | 0.2066 | [0.7729, 1.0230] |

**All 10 pairwise contrasts cross zero; 0 of 10 exclude zero.** The largest difference is
deepseek − llama = **+0.0312 [−0.1126, +0.1750]**. The same pair is the full spread: the five systems span 0.0313 of the metric
while per-item standard deviations run 0.12–0.21, so the between-system signal is small
relative to within-system item variance at this n. The instrument reads models; on this data
it does not separate *these* models on the one surface where separation could have been
claimed.

*Construction note.* The means in this table differ from the §5.2 headline table in the third
decimal (deepseek 0.9292 here vs 0.9277 there). The headline table averages each epoch's
reported metric, whose per-epoch denominator varies with per-epoch exclusions; this table
averages each item across its three epochs first and then across items, which is the correct
construction for a repeated-measures contrast. **Both are reported as constructed; neither is a
correction of the other.**

**m stays 30.** The multiplicity family is fixed by the pre-registration and does not shrink
because designs 04 and 10 are voided by the swap test. Those 20 contrasts are reported as
judge-sensitive, not as comparisons. No significance language is used anywhere: "crosses zero"
and "excludes zero" are interval statements.

### 5.6 Where the judging fails — referee localization

The preceding subsections establish that the judging is decisive and that the instrument
cannot currently support a comparison. They do not say *where* the judging fails, and the
three plausible causes — a divergent judge, an unreadable rubric, a defective item — call for
three different and very differently-priced repairs. The two-referee arms supply that
localization. All figures below are reported **per design and per stratum, never pooled**; the
referee sample is disagreement-enriched by construction, so any pooled headline would be
invalid. And throughout: referee concordance is evidence about judge character, **not proof
that any judge is correct**.

**(i) Judge-character — design 07, the pastoral arc.** On the 392 contested turns of that
design, both referees side with judge-B roughly 3:1 over judge-A and agree with each other:
Opus sides with B on 0.5944 (233) versus A on 0.2168 (85), neither on 0.1888 (74); Sol sides
with B on 0.605 (237) versus A on 0.138 (54), neither on 0.2577 (101). Removing the defect
items of (iii) sharpens both: Opus 0.7628 versus 0.1569 and Sol 0.770 versus 0.146 on the
274-unit sensitivity slice, which excludes the five items affected by unscorable verdicts (a superset of the three defect items below). Referee-to-referee raw agreement on this stratum is **0.857**,
rising to 0.9416 on the primary exclusion slice; the two referees back opposite judges on only
13 of 392 turns, and jointly back judge-B on 225. On the same stratum Opus↔B κ = 0.3091 against
Opus↔A κ = −0.0697, and Sol↔B κ = 0.3778 against Sol↔A κ = −0.14; on the separate 150-unit
control stratum both referees concord highly with the judges' shared state (Opus 0.880, Sol
0.860; referee-to-referee 0.920). The dominant pattern is specific and directional: judge-A
calls `comfort_only` or `cold_correction` where judge-B and both referees call
`full_validation`. **Read:** on this design judge-A under-calls the target state relative to
judge-B and to both references. This is a judge-selection question, and a stronger or
additional judge is the indicated candidate repair, which remains an open owner decision rather than a settled one.

**(ii) Rubric / state-taxonomy ambiguity — design 02.** The same procedure on that design's
200-unit disagreement stratum returns the opposite shape. Each referee agrees with each
shipped judge only 0.23–0.27 of the time (Opus 0.2500 with A, 0.2550 with B; Sol 0.230 with A,
0.270 with B) and sides with **neither** judge about half the time (0.4950 and 0.5000). But the
referees agree substantially **with each other**: raw 0.735, κ 0.653 on that stratum, and 0.813
(κ 0.719) on its 80-unit control stratum — and they land jointly on the same "neither" state on
**83 of 200 units (41.5%)**, most often jointly calling `full_compliance` where judge-A said
`pushback_with_alternative` or `holds_line` and judge-B said `material_concession`. A
strong-model consensus reading of this taxonomy exists, and **both** shipped judges deviate
from it in different directions. That makes this a taxonomy problem, not a judge-selection
problem — **and therefore a stronger judge will not fix it**. Some residual genuine ambiguity
remains on top (the taxonomy is harder than design 07's: referee-to-referee 0.735 versus 0.857,
control concordance 0.813 versus 0.920).

**(iii) Defect items.** Both referees' `unscorable` verdicts concentrate on the same three
design-07 items whose shipped per-turn rubric anchor was, at the time of the audit, literally "(no keyed text)":
**WW-07-L02, WW-07-I04, WW-07-F02**. Opus returned 50 unscorable verdicts (19 / 18 / 11 on
those three, 2 anywhere else); Sol returned 87 (35 / 23 / 29, zero anywhere else); the
intersection is 48. With no keyed norm to score against, the two shipped judges fall back on
opposite priors — judge-A overwhelmingly outputs `full_validation` while judge-B scatters
toward `deflection` — so these items **manufacture disagreement mechanically, independent of
judge quality**. Two independent referees dual-confirm that they cannot be scored as shipped.

**A fourth candidate cause, not separable in this run.** The partition above names three
causes — a divergent judge, an unreadable rubric, a defective item. A fourth is available
and is not excluded by this design: the pinned branch classifier misrouting a turn, which
changes which rubric the judge is applying at all. This matters precisely here, because
designs 02 and 07 — the only two designs localized — are the two classifier-routed ladders.
The project's own cross-family evidence is specific: alternate–alternate classifier
agreement of 0.902 against alternate–nano 0.685–0.721, with 24.4% of branch turns splitting
two-against-one versus the pinned classifier, concentrated in design-02 state swaps. And
because the pinned classifier and judge-A are the **same model instance**, the
"judge-A character" reading on design 07 is confounded with classifier character *by
construction* and cannot be separated within this run. Any repair proposal should treat
the classifier as a live alternative explanation rather than as a fixed background condition.

**(iv) No localization — design 06.** The method did not succeed everywhere, and the failure
is reported rather than omitted. Design 06 contributed 120 of the 942 frozen units (60 gap,
60 control) and yields no localization: arm 1's headline category divergence on `principles`
did not replicate in arm 2, which found a referee-to-referee gap of roughly +0.40 on that
category against within-±0.20 agreement on every other category. The honest reading is that
arm 1's standout was a single-referee character trait rather than a strong-model consensus.
On the three designs actually audited the method localized two and returned nothing on one —
a result that also supplies the empirical counterweight to this paper's own stated ceiling,
that two referees may share correlated error.

**Convergence with the decomposition.** The referee localization and the variance decomposition
are independent analyses on different data slices, and they agree on the same design: design 02
has the largest interaction in the suite (46.5% on a 5.8% model effect) and the lowest exact
primary-field agreement between the shipped judges (0.232), and the referee arms independently
place its failure at the taxonomy level rather than at the judge level. That two methods with
no shared machinery localize the same design to the same cause is the strongest internal
evidence for the method that this run provides.

**Full-bank confirmation of two instrument watch items.** First, design 08's
`protected → steamrolled` transition, flagged at smoke scale on 4 of 30 verdicts, is confirmed
at full n as the design's single largest disagreement transition: **113 of 965 comparable
verdicts (11.7%)**, with `steamrolled → protected` at 45 (4.7%) in the reverse direction, and
overall design-08 agreement of 0.718. The decomposition quantifies the same phenomenon as a
25.9% interaction against a 9.1% model effect. The covert-protection key is live and operating
as designed, but its reading is judge-dependent at full bank, and — as its own comparability
line — this is the first full-bank run under its post-anchor rubric. Second, design 07's floor
saturation is confirmed on revision 2026-07-24b: `arc_pass_rate` is at or near zero under both
judges on all five systems (judge-A 0.000–0.012; judge-B 0.000–0.062), with 27 of 27 items
scored and 0 excluded. This matters because the three repaired defect items are now validly
scored and the floor persists, making it a **recorded ceiling-room property of the instrument
at this system tier rather than a scoring artifact**. It is not evidence about the models
beyond the observation that none of these five clears the terminal bar.

**Exact primary-field agreement between the two judges** (pooled over the three epochs within
each design; never pooled across designs) is reported below, with the per-system range, since
it is the raw quantity that the decomposition and the referee arms both interpret.

| design | agreement | n | per-system range |
|---|---:|---:|---|
| 04 innerweight | 0.842 | 880 | 0.75–0.91 |
| 10 strangergate | 0.759 | 1,050 | 0.69–0.84 |
| 08 vocationfork | 0.718 | 965 | 0.66–0.79 |
| 06 crookedpath | 0.707 | 457 | 0.39–0.93 |
| 01 goodsamaritan | 0.651 | 702 | 0.63–0.68 |
| 07 seventyseven | 0.597 | 402 | 0.47–0.65 |
| 09 doubleedge | 0.526 | 1,286 | 0.30–0.68 |
| 05 ordoamoris (secondary field) | 0.525 | 465 | 0.40–0.67 |
| 03 quiettongue | 0.512 | 953 | 0.46–0.55 |
| 02 twomasters | 0.232 | 1,041 | 0.18–0.28 |

Design 02 is the most judge-fragile instrument in the suite at 0.232; design 06's per-system
range (0.39–0.93) is the widest, meaning that on that design how much the judges agree depends
heavily on which system is being judged. The dominant disagreement transitions are: design 03
`no → yes` ×345 (36.2%), which is the level shift that collapses `say_do_gap` under judge-B;
design 09 `0 → 1` ×566 (44.0%); design 07 `cold_correction → full_validation` ×63 and
`comfort_only → full_validation` ×58; design 06 `0.5 → 1` ×61 and `0 → 1` ×60; design 08
`protected → steamrolled` ×113 (11.7%); and design 02 `holds_line → pushback_with_alternative`
×142 (13.6%) together with `pushback_with_alternative → material_concession` ×127 (12.2%).

**Reporting-surface note on design 02.** `break_turn` is the sole headline for that design.
`pushback_rate` is reported only as a **secondary** measure, **per judge and never pooled**, and
every report of it carries the standing caveat that the cross-judge stability of the
`pushback_with_alternative` state is untested and that all figures predating bank revision
2026-07-24b are single-judge. It is used here only as evidence about the state's definitional
boundaries, and that evidence is the transition pair immediately above: the two largest
design-02 disagreement transitions **both** involve the pushback state, from the "held" side
(`holds_line → pushback_with_alternative`, ×142, 13.6%) and from the "conceded" side
(`pushback_with_alternative → material_concession`, ×127, 12.2%). The state is contested from
both directions at once — which is exactly the signature of a boundary definition problem
rather than a judge-quality problem, and it corroborates (ii) from inside the shipped judge
pair. No ordering of that metric is presented, and it is not a finding about the systems.

---

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content
