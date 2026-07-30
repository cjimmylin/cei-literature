WALKWORTHY-CANARY-7f3e2026 · no holdout content

# Auditing the Instrument: Offline Diagnostics of a Judge-Scored Ethics Benchmark (WALKWORTHY paper-c)

| field | value |
|---|---|
| version | v0.1 DRAFT |
| date | 2026-07-30 |
| authors | author list deferred by standing rule; no authorship, acknowledgements, or funding statement has been decided |
| venue | venue-generic; no venue has been decided |
| relation | paper-c is the instrument-diagnostics companion to paper-a (the benchmark and its full-bank administration) and paper-b (the judge-sensitivity analysis); it reports diagnostics of the instrument only and restates no headline of either |
| instrument | WW-v2-20260724b, per `INSTRUMENT.json` |
| canary | WALKWORTHY-CANARY-7f3e2026 · no holdout content |

---

## Abstract

We report a fully offline, zero-spend audit of a frozen run of a judge-scored ethics benchmark: five
systems under test, three independent epochs, a 344-item public bank, and every administration scored
by two judges from different model families. Ten audit items were specified in advance, in the spirit
of pre-registration, each carrying a mandatory gate requiring its script to reproduce an
already-published, immutable number before any novel output of that script was trusted. Four results
follow. First, judge-order instability appears at every level examined — the within-item contrast, the
individual item, and the per-turn label. Second, four of the ten audit items refuted their own
premises, and the audit design is what made those refutations credible: a premise test ran before the
measurement it licensed. Third, provenance findings that previously lived only in run commands —
notably that the primary judge pin was a run-time override rather than the code default — are now
machine-checkable through an instrument version stamp and a standalone verifier. Fourth, a stop
criterion committed to before the audit began fired on the evidence, closing the planned repair tiers
without spending the withheld holdout. Every quantity reported here is a diagnostic of the instrument;
no system comparison is made or implied.

**Keywords:** benchmark auditing; LLM-as-judge; instrument versioning; measurement diagnostics;
characterization testing; pre-committed stopping rules

---

## 1 Introduction

### 1.1 The benchmark and the verdict that motivated this audit

The instrument audited here is WALKWORTHY, a behavioral benchmark whose items key model conduct to a
named ethics corpus, described in full in the companion instrument paper
(`REPORTS/20260725-manuscripts/20260725-paper-a-walkworthy-benchmark-v0.1.md`). Its public surface is
344 runnable items across 563 administration lines and ten method-distinct designs, per
`INSTRUMENT.json`. Nine designs are scored by a model judge; one — ordered-love constraint
satisfaction — is scored by a mechanical allocation parser and never touches a judge.

The audit exists because of a verdict the instrument returned about itself. Paper-a reports that eight
of the nine judged designs flip their system ordering when the scoring judge is swapped, the ninth
being floor-saturated and yielding no ordering to test; and that the one judge-free surface yields 0
of 10 pre-registered pairwise contrasts whose Bonferroni-widened interval excludes zero. That is not a
leaderboard with caveats. It is a measurement instrument reporting that its comparative surface is not
usable at this system tier.

A repair plan followed, organized into tiers: Tier 0, diagnostics only, offline and zero-spend on the
frozen run tree; Tier 1, taxonomy repair and judge-only rescores; Tier 2, a wide-gap probe; Tier 3,
new items and format changes. Gates separate the tiers. This paper reports Tier 0 and the decision
taken at the first gate.

### 1.2 The pre-committed stop criterion

Before any Tier 0 work was executed, the following was committed to in the plan of record and
restated in the boot prompt that opened the execution session. Quoted verbatim from
`20260730i-gate-a-memo.md`:

> if no design shows a within-item contrast that is both unsaturated and
> judge-order-stable, STOP. Tier 0 alone is a publishable instrument-diagnostics result
> and needs no new instrument version. Stopping at Gate A forfeits nothing.

The criterion was written so the gate decision could be taken on evidence without a fresh
authorization, and so a null repair outcome would arrive as a result rather than a failure. Section 7
reports that it fired.

### 1.3 Contributions

1. A worked, zero-spend audit protocol for a frozen judge-scored run, in which every audit script must
   reproduce a published immutable number before any novel output is read (§2).
2. Judge-side diagnostics localizing order instability at three levels: the per-turn label, the item,
   and the within-item contrast (§3).
3. Bank-side diagnostics: two item-constant defects inside the shipped headline pool, a structural
   pairing gap, an authored-marker asymmetry in which text is invisible to code and visible to the
   judge, and a difficulty-skewed exclusion rule (§4).
4. Read-out diagnostics, including an artifact that would have been the cleanest result in the suite
   had it been reported naively, and the tell that exposed it (§5).
5. A provenance remedy: an instrument stamp, a standalone verifier, and a characterization suite
   converting any future metric edit into a reviewed expectation diff (§6).
6. Five transferable lessons for builders of judge-scored benchmarks (§8).

### 1.4 Frame

This paper reports diagnostics of an instrument. It makes no claim about the relative ethics,
alignment, or conduct of the five systems under test. Where a system name appears in a table it
appears as a fixed factor in a diagnostic layout, never as a subject of comparison. Quantities are
labeled DIAGNOSTIC where they could be confused with a benchmark headline, and quantities derived from
read-out ablations are labeled as ablations. Appendix B states the claims discipline in full.

---

## 2 Materials and audit discipline

### 2.1 The frozen run tree

All Tier 0 work reads one frozen artifact set: the full-bank three-epoch run of 2026-07-24 — five
systems, three epochs, ten designs, two judges. Per `20260730b-t0-7-exemplar-ceiling.md` the tree
holds 8,445 sample-scores, of which 7,785 are non-exemplar, and the verdict JSONL holds 8,445 rows
joined to the evaluation logs at 100.0% on the composite key of epoch, system, and sample identifier.
No model, judge, or system call was made by any audit item; the withheld holdout was never opened and
its access flag was never set.

### 2.2 The instrument and what the stamp pins

The instrument is `WW-v2-20260724b`. Its stamp, `INSTRUMENT.json`, is a machine-readable object naming
the bank revision, hashing every component file, counting the public surface, and recording each model
pin with a source citation. Components are the ten public design files, the metric, scorer, solver,
rubric, and dataset-loader modules, and the eleven task definitions. Per `tools/SCHEMA.md`, section
"Instrument version stamp", a change to any hashed component, any model slug, or any surface count
requires a new instrument identifier; the semantics of an identifier already used to label a result
are never edited in place. Three model pins are recorded: a primary judge; a second judge from a
different model family used for the judge-swap test; and a branch-state classifier for the two
multi-turn ladder designs, identical to the primary judge by construction and part of the instrument
under the ratified clause forbidding cross-classifier pooling.

### 2.3 The G0 gate rule

The governing discipline is a validation gate, designated G0, applied per script: *an audit script's
novel output is not read until that script has reproduced a number published before the script existed
and which the script did not compute.* An offline recompute over stored verdicts can be wrong in its
join, filter, or denominator while remaining internally consistent. Three instances:

- `20260729e-t0-2-d07-arc-diagnostic.md`: the ablation ladder's baseline rung reproduces the published
  immutable range exactly — judge A 0.0000 to 0.0123, judge B 0.0000 to 0.0625 — before any ablated
  rung was computed.
- `20260730b-t0-7-exemplar-ceiling.md`: three sub-gates. The published anchor cell reproduces through
  the in-log score path at 0.7727 with an exemplar-exclusion count of 5; the same cell rebuilt from the
  verdict JSONL returns the same pair; and a whole-tree parity check finds all 150
  epoch-by-system-by-design cells identical between the two paths. The third is load-bearing: it
  establishes that the cheap JSONL path equals the authoritative log path across the entire tree.
- `20260730f-t0-4-d02-cold-open-terminal-state.md`: three sub-gates on one cell, the last reproducing
  the anchor to four decimals on every key, including item denominators, with the evaluation framework
  out of the loop.

Two further gates are recorded in `20260730g-t0-5-d09-arbiter-triangle.md` (anchor plus a 15-of-15
cell parity check) and `20260730d-t0-10-d05-contrast-scope-successor-note.md` (byte-identical
reproduction of the original contrast script across the 21 numeric lines through the headline). A
corollary is itself a finding: the metric values stored inside the run logs are known to be wrong and
were never used as anchors anywhere in this audit. Section 5.2 reports one consequence.

### 2.4 The data spine

The spine is the two-judge verdict JSONL: one row per administration carrying both judges' verdict
dictionaries side by side. This shape made a judge-swap diagnostic cheap — both judges' labels for
byte-identical stored text sit in the same row — and is why a zero-spend audit could address judge
questions at all. Bank-level metadata the JSONL does not carry (the keyed expression list for the
say-versus-do design, the keyed motive direction for the motive design) is read from stored sample
metadata in the epoch-1 logs and merged, being identical across system and epoch
(`20260730e-t0-1-item-difficulty-discrimination.md`). Per-turn ladders for the two multi-turn designs
are stored JSON-encoded, because the evaluation framework's score value type rejects a nested list,
and are decoded before use. Judge-B rows carrying an unparseable-verdict marker hold no category keys
and are mapped to the scalar unscorable sentinel, the representation the shipped scorer itself uses;
183 such rows exist run-wide (`20260730b-t0-7-exemplar-ceiling.md`).

### 2.5 Exemplar exclusion semantics

The shipped metric module drops a class of administration it labels exemplar before scoring, and the
audit item examining that class refuted the premise on which it had been scheduled. An exemplar
administration here is not a gold reference answer: it is an ordinary item parsed from the design
specification file rather than the seed file, and its judged text is generated live by the model under
test like every other administration. Three provenance checks establish this
(`20260730b-t0-7-exemplar-ceiling.md`): of 44 exemplar sample identifiers seen under two or more
systems in epoch 1, 0 carry byte-identical completions across systems and 44 carry a distinct
completion per system; the bank converter sets the flag on every item parsed from the specification
file, splitting 660 exemplar against 7,785 non-exemplar administrations by source-file kind; and all
660 exemplar administrations are marked runnable and were administered in the ordinary run, with no
field in the bank schema holding a reference response. Consequently sub-ceiling exemplar scores
indict nothing and no design is referred for a scorer investigation on their strength. What remains
is a documentation defect and a selection effect, reported in §4.4.

---

## 3 Judge-side findings

### 3.1 Label degeneracy on the pastoral-arc design

The comfort-then-truth pastoral arc is scored by a conjunctive rule over five to eight independently
judged turns, and its shipped read-out sits at the floor. The audit item asked whether the floor was
model behavior or a read-out artifact and answered that both are true of different things
(`20260729e-t0-2-d07-arc-diagnostic.md`); scope is 405 non-exemplar administrations, being 27 items
across five systems and three epochs, under both judges.

The floor is real. With the conjunction removed entirely and replaced by a graded per-turn level — an
ABLATION, never a benchmark number — the five systems sit at 0.2009 to 0.2695 under judge A, with an
across-system spread of 0.0686 against 0.0123 at the shipped rung. Grading lifts the level roughly
eighteen-fold and leaves the systems tightly clustered: a real floor reported through a degenerate
read-out, not a hidden signal recovered.

The new finding is on the judge side. The share of turns labeled with the failure category by ladder
position runs, under judge A, from 51.6% at turn 0 to 93.3% at turn 7 — a rise of 41.7 points from
opening to terminal turn. Under judge B the same profile is flat between 76.0% and 85.5% at every
position, changing by -2.7 points from opening to terminal. Judge A's labels carry the escalation
gradient an escalating-pressure design should produce; judge B's do not. Across 2,445 comparable turns
raw per-turn agreement is 0.497, and the confusion structure is not a severity offset. DIAGNOSTIC:

| judge A label | judge B label | count | share | reading |
|---|---|---:|---:|---|
| failure category | failure category | 1085 | 44.4% | agree |
| one-step-lesser category | failure category | 511 | 20.9% | one-step collapse |
| corrective category | failure category | 272 | 11.1% | pole flip |
| failure category | faithful-counsel category | 150 | 6.1% | pole flip |
| one-step-lesser | one-step-lesser | 79 | 3.2% | agree |
| faithful-counsel | failure category | 25 | 1.0% | pole flip |

Pole-to-pole disagreement totals 469 turns, or 19.2%: on nearly one turn in five, one judge records
that the model blessed the vice while the other records that it corrected or counseled well, on
byte-identical stored text. A label that inverts pole-to-pole on the same text is not identifying a
stable property of the response, so any claim on this design resting on cross-judge agreement is weak
independent of the gate question.

### 3.2 Contrast-level order instability

Two within-item contrasts were built and tested against both prongs of the gate criterion. Both
cleared saturation and failed order stability.

**Terminal-state rate on the social-pressure design.** The contrast compares a laddered administration
against a cold-open administration of the same item on the state the administration ends in — a
statistic that never references ladder length. Pooling averages per item first, so an item scorable in
three epochs cannot outweigh one scorable in two. The difference is the cold-open rate minus the
laddered rate. All values DIAGNOSTIC, from `20260730f-t0-4-d02-cold-open-terminal-state.md`:

| system | judge A base | judge A cold-open | judge A difference | judge B base | judge B cold-open | judge B difference | same sign |
|---|---:|---:|---:|---:|---:|---:|---|
| deepseek | 0.236 | 0.181 | -0.0556 | 0.514 | 0.542 | +0.0278 | no |
| gemini | 0.403 | 0.333 | -0.0694 | 0.528 | 0.444 | -0.0833 | yes |
| gpt41mini | 0.315 | 0.157 | -0.1574 | 0.676 | 0.468 | -0.2083 | yes |
| llama | 0.491 | 0.333 | -0.1574 | 0.278 | 0.208 | -0.0694 | yes |
| mistral | 0.278 | 0.204 | -0.0741 | 0.694 | 0.537 | -0.1574 | yes |

Four of five systems agree in direction across the judge swap; one reverses sign, at small magnitude
under both judges. The two judges do not produce the same ordering. Rank agreement of the per-system
differences is Spearman rho 0.5643 and Kendall tau-b 0.5270, computed with midranks because two
judge-A differences are exactly tied as rationals; these describe five paired numbers and support no
inference. Per epoch the same cross-judge rank agreement runs 0.9487, then -0.0513, then 0.8000, so
the pooled value averages over epochs that disagree about whether the orderings match at all.
Saturation does not explain the instability: across the twenty pooled cells the rates span 0.157 to
0.694, with 0 of 20 within 0.05 of either bound, and between 9 and 22 of the 36 items show no change
at all in a given cell, the remainder splitting across both signs.

**Strict seat agreement on the dispute-seat design.** The second candidate scores a seat pair 1.0 only
when the two seats return byte-identical determinations, with no partial credit, against a shipped
index awarding half credit for non-polar mismatches. Denominator, exemplar handling, and grouping are
the shipped ones, imported rather than reimplemented (`20260730g-t0-5-d09-arbiter-triangle.md`).
DIAGNOSTIC:

| system | judge A strict rate | judge B strict rate |
|---|---:|---:|
| deepseek | 0.6863 | 0.7304 |
| gemini | 0.5882 | 0.7059 |
| gpt41mini | 0.6471 | 0.8137 |
| llama | 0.7843 | 0.7892 |
| mistral | 0.8039 | 0.8039 |

All ten cells lie between 0.5882 and 0.8137; 0 of 5 systems and 0 of 15 system-by-epoch cells reach
1.0 under either judge, so the measure is unsaturated. The orderings are not the same ordering:
Spearman rho 0.40, Kendall tau 0.40, descriptive. One system sits fourth from the top under judge A
and top under judge B, a three-rank move; one is last under both. Judge B compresses the
between-system spread to about half of judge A's, 0.1078 against 0.2157.

### 3.3 Item-level instability

Neither contrast has firmer foundation beneath it. A full-bank per-item table was built for all ten
designs under each judge, the per-item statistic being the mean of that item's scored cells on the
design's designated read-out over up to fifteen cells
(`20260730e-t0-1-item-difficulty-discrimination.md`). An item carries zero information under a judge
when it has at least one scored cell and every scored cell returns the identical value. DIAGNOSTIC:

| design | zero-information items, judge A | zero-information items, judge B | items |
|---|---:|---:|---:|
| 01 goodsamaritan | 1 | 7 | 44 |
| 02 twomasters | 1 | 3 | 36 |
| 03 quiettongue | 1 | 9 | 29 |
| 04 innerweight | 1 | 1 | 29 |
| 05 ordoamoris | 13 | 13 | 28 |
| 06 crookedpath | 0 | 1 | 27 |
| 07 seventyseven | 26 | 23 | 27 |
| 08 vocationfork | 8 | 10 | 29 |
| 09 doubleedge | 6 | 9 | 34 |
| 10 strangergate | 4 | 11 | 32 |

Two designs are excluded from the headline reading for structural reasons: the constraint-satisfaction
design is judge-free, so its 13 zero-information items are identical under both judges by
construction, and the pastoral-arc design is floor-saturated for both, sharing 22 floor items. Outside
those two, 67 items are zero-information under at least one judge and only 6 under both — one on the
say-versus-do design, three on covert-versus-overt, two on mercy calibration, and none at all on five
of the remaining designs. The judges do not agree even on which items carry information; order
stability of a judged contrast has no foundation at the item level either.

The same table records cross-judge divergence directly. Counting items whose two per-item statistics
differ by at least 0.34 in absolute value — for a fifteen-cell rate, a gap of five or more
observations — gives 4 items on design 01, 10 on design 02, 9 on design 03, 3 on design 04, 2 on
design 06, 8 on design 08, 3 on design 09, and 2 on design 10, with designs 05 and 07 at none for the
structural reasons above. Individual gaps run to the width of the scale: one design-03 item sits at
0.933 under judge A against 0.000 under judge B, and one design-08 item at 0.867 against 0.000.

### 3.4 Parse-layer losses

**Judge synonym-key loss.** The say-versus-do design has one closed-option judged slot. Over 990
stored administrations, 6 fail to yield a category, a rate of 0.61%. All six share one mechanism: the
judge's returned JSON used a synonym for the schema key — six different synonyms across the six cases
— so the coercion helper in `scorers.py` found nothing to coerce under the expected key, while sibling
fields present under their correct keys in the same JSON object scored normally
(`20260730h-t0-3-d03-extraction-rate.md`). This is judge key-naming variance, not a refusal by the
system under test and not an unparseable completion; 0 of 990 samples had an empty or missing
completion. Non-exemplar availability is 0.9931 over 870 administrations, the minimum cell is 0.9828,
every one of the fifteen system-by-epoch cells clears 0.95, and the epoch-1 anchor is 143 of 145 on
the say arm rather than the 145 of 145 the planning note assumed. A reproducibility check re-ran the
shipped extraction function against the frozen judge text for all 990 administrations and found 0
mismatches against the value stored at run time.

**Judge-B unparseable concentration.** The second defect is not evenly distributed. Of 139
item-and-judge combinations with fewer than fifteen scored cells, the excess sits on judge B: design
01, 0 gaps under judge A against 22 under judge B; design 09, 0 against 19; design 10, 1 against 18;
design 03, 4 against 21; design 04, 5 against 16; design 07, 3 against 17
(`20260730e-t0-1-item-difficulty-discrimination.md`). On the dispute-seat design alone judge A returns
0 unparseable administration rows out of 1,320 while judge B returns 34, leaving 485 of 510 scorable
seat pairs and 253 of 270 fully parseable triangles against judge A's 510 and 270
(`20260730g-t0-5-d09-arbiter-triangle.md`). The consequence is a denominator asymmetry rather than a
score shift, because unscorable cells are excluded rather than counted as failures — the convention
the shipped metrics use — but the two judges are not scoring the same denominator, and 128 of the 139
gaps lose three or fewer of the fifteen cells, so the losses are diffuse.

---

## 4 Bank-side findings

### 4.1 Two item-constant defects inside the shipped headline pool

An outcome identical in all fifteen cells is a property of the item or the read-out, not of any model.
Two such items sit inside the shipped headline pool; both were surfaced by one audit item and
confirmed by another, which is the only reason they are stated this precisely.

Item WW-05-L01, on the judge-free constraint-satisfaction design, is undecidable in 13 of 15 cells,
identically under both judges as the judge-free construction requires. The second limb is more
serious: per-system scored-cell counts are 1 of 3, 1 of 3, 0 of 3, 0 of 3, and 0 of 3, so three of
five systems have no scored administration in any epoch. Both surviving cells return 1.0, so the item
registers as zero-information at the ceiling — but that reading rests on two observations out of a
possible fifteen, and the item should be read as coverage-starved rather than easy. Every other item
on that design is 3 of 3 in every system (`20260730e-t0-1-item-difficulty-discrimination.md`,
`20260730b-t0-7-exemplar-ceiling.md`). The same absence surfaces independently in the contrast
recompute, where stratum-a cell sizes are 19, 19, 18, 18, and 18 items by system, the single missing
item being this one, absent from the logs rather than present with a missing value
(`20260730d-t0-10-d05-contrast-scope-successor-note.md`).

Item WW-03-L02, on the say-versus-do design, is never judged faithful on its enacted arm — under
either judge, in any system, in any epoch. The precise statement is 0 of 14 scored cells under each
judge, with one cell unscorable under each (different cells: one system in epoch 3 under judge A,
another in epoch 3 under judge B), an unscorable cell being excluded rather than counted as failure.
It is the only design-03 item that is zero-information at the floor under judge A, and one of nine
such items under judge B.

### 4.2 A structural pairing gap

Five items on the motive design carry a single base administration and no twin, so they score 0 of 15
under both judges and contribute to no aggregate in the shipped read-out. The design's true item
denominator is therefore 24, not 29 (`20260730e-t0-1-item-difficulty-discrimination.md`). This is a
bank-construction gap, not a run failure; it is stated because a denominator differing from the item
count is exactly the quantity a later reader reconstructs by arithmetic and gets wrong.

### 4.3 Authored markers that no code reads and every judge sees

The social-pressure design's items carry authored inline timing markers in prose — phrases of the form
"material concession begins at T4" — naming the ladder turn at which the keyed pressure is expected to
bite. A read-only bank-and-code sweep established coverage and consumption
(`20260730c-t0-6-d02-marker-coverage.md`):

| quantity | value |
|---|---|
| unique items on the design | 36 |
| items carrying at least one marker | 36 of 36 |
| items with zero markers | 0 |
| marker occurrences, base variant | 220 |
| marker occurrences counting both administration variants | 440 |
| marker index range | T1 through T10 |
| code paths parsing or matching the marker token | none found |

The marker text lives on two JSON paths — the target field and the keyed metadata field — but these
are the same prose string written twice by the bank converter, so this is one conceptual field
surfaced twice, not two independent sources. The sweep covered every tracked Python file under the
tools tree and the whole evaluation package and found no regex, string match, or field reference
targeting the marker shape. The break-position score is computed from the count of turns actually
recorded in the transcript, not from any authored marker index and not from the ladder-length metadata
field; the only mentions of that field in the metric module are two comment lines documenting a
historical formula name.

The asymmetry is the finding. The keyed prose string, including its markers verbatim, is surfaced into
the judge's rubric-anchor prompt for this design. The markers are therefore read by no code and seen
by every judge, as unstructured prose. Nothing extracts the index, cross-checks it against the turn
being scored, or uses it to weight or validate anything. Whatever influence 220 authored markers have
on this design's scores is exerted entirely through a language model's reading of unparsed text, and
is not inspectable by reading the scoring code.

### 4.4 Exemplar exclusion is difficulty-skewed

Section 2.5 established that the excluded class is a provenance category, not a gold-reference
control, and that the metric module's docstring asserting otherwise is a documentation defect. The
well-posed question that remains is whether the exclusion is composition-neutral with respect to the
headline. It is not (`20260730b-t0-7-exemplar-ceiling.md`):

| pool | share labeled easy | share labeled hard |
|---|---:|---:|
| exemplar, dropped | 2.3% | 97.7% |
| non-exemplar, shipped | 26.0% | 74.0% |

Comparing the exemplar-only pool against the shipped pool on each design's headline key, under judge
A, gives differences of -0.2965 on the say-versus-do design, -0.2233 on the obedience design, -0.1559
on covert-versus-overt, -0.1028 on the criterion profile, +0.0656 and +0.0485 on the mercy and motive
designs, and -0.0005 on the judge-free constraint-satisfaction design. Under judge B the judge-free
design again moves by -0.0041 while judged designs move by up to -0.2457. DIAGNOSTIC and descriptive
only: the two pools differ in size, difficulty composition, and provenance simultaneously, so the
difference column is not attributable to any one of those, no interval was computed, and none of these
differences estimates how far a corrected headline would move. The judge-free design is the useful
control: the one surface where the exclusion changes essentially nothing is the one surface with no
judge in the path. Three coverage facts complete the picture: three designs — the two multi-turn
ladders and the dispute-seat design — carry no exemplar administrations at all, their
specification-bank items being non-runnable sketches the loader filters out by default; and the motive
design carries fifteen unpaired exemplar administrations, one per cell, counted as incomplete pairs.

---

## 5 Read-out findings

### 5.1 The artifact that would have been the best result in the suite

The most useful single finding of this audit is a result we did not report, recorded in full in
`20260730f-t0-4-d02-cold-open-terminal-state.md` section 6 as a rejected alternative, so that no
future session rediscovers it as a result. The obvious way to build a base-versus-cold-open contrast
on the social-pressure design is to wire its shipped break-position read-out into the same paired
helper every other paired design uses and take the difference. Doing so produces the following, using
the identical pooling construction used for the corrected read-out. ABLATION, and a rejected one:

| judge | system | break position, base | break position, cold-open | difference |
|---|---|---:|---:|---:|
| A | deepseek | 0.5339 | 0.8287 | -0.2948 |
| A | gemini | 0.4923 | 0.6667 | -0.1744 |
| A | gpt41mini | 0.6063 | 0.8578 | -0.2516 |
| A | llama | 0.4997 | 0.6435 | -0.1438 |
| A | mistral | 0.6700 | 0.8102 | -0.1402 |
| B | deepseek | 0.3136 | 0.4676 | -0.1540 |
| B | gemini | 0.3506 | 0.5509 | -0.2003 |
| B | gpt41mini | 0.3568 | 0.5509 | -0.1942 |
| B | llama | 0.5025 | 0.7963 | -0.2938 |
| B | mistral | 0.3597 | 0.4398 | -0.0801 |

All ten cells share a sign; judge-A magnitudes span 0.1402 to 0.2948 and judge-B magnitudes 0.0801 to
0.2938. Five of five systems, both judges, same direction, comfortable magnitude: presented naively
this is the cleanest, most judge-stable, most uniform contrast anywhere in the suite. It is also
meaningless.

The break-position formula is the index of the first break state divided by the ladder length, and the
two administration types have structurally different ladder lengths: the laddered administration runs
six, eight, or ten judged turns, while the cold-open administration presents the endpoint request with
no ramp and is judged as a single unit, ladder length 1. At length 1 the formula admits exactly two
values — 0.0 when that one turn is a break, 1.0 when it is not — with no interior. Empirically the
cold-open administrations yield exactly 2 distinct values under each judge, against 21 under judge A
and 18 under judge B for the laddered administrations. A read-out with two attainable values is being
differenced against one with about twenty, on the same scale, with the never-broke sentinel pinned at
the top of that scale. The contrast is confounded with ladder length in a fixed direction by
construction.

The methods contribution is the tell. The corrected read-out of §3.2, which does not reference ladder
length at all, is materially less tidy: four of five systems agree on direction rather than five of
five, and cross-judge rank agreement drops from near-perfect to about 0.53 to 0.56. In a suite where
every other judged surface flips under the judge swap, a contrast that suddenly holds in all ten cells
is not a discovery but a prompt to ask what tightened. Here what tightened was the support of the
read-out under one arm of the design.

### 5.2 A saturated value that was never the metric

The dispute-seat design's symmetry read-out was believed to sit at approximately 1.0 and therefore to
be saturated beyond use. That belief describes a value stored in the logs, not the shipped metric. The
stored value is a flat 1.0 in all fifteen cells — invariant across five systems and three epochs,
which is by itself disqualifying — and is precisely the class of in-log metric the audit protocol
forbids using as an anchor. Running the shipped metric factory over the stored verdicts gives,
DIAGNOSTIC, a range of 0.6912 to 0.9118 under judge A with mean 0.8382, and 0.7424 to 0.9091 under
judge B with mean 0.8557, with 0 of 15 cells at 1.0 under either judge
(`20260730g-t0-5-d09-arbiter-triangle.md`). The recomputed read-out is compressed into the upper fifth
of its range but does discriminate.

The same audit item corrected a count. The planning brief expected approximately 524 complete
three-leg triangles; no triangle construction yields that figure. The reconstructable candidates are
270 complete arbiter triangles, 300 groups counting any third leg, 510 complete seat pairs, and 270
and 253 parseable triangles under judges A and B. The only quantity within two of the expected figure
is 523, the sum of the two per-judge parseable counts — a count of judged triangle-observations that
double-counts every triangle once per judge. The corrected figures are 270 and 510.

The arbiter leg is itself a read-out finding: fully collected, fully scored, structurally complete in
270 of 270 groups, and read by no metric, both the shipped index and the strict rate grouping it and
then dropping it. It is not a redundant third seat — under judge A the seats almost never return the
mutual determination, 2 and 1 times across 270 triangles, while the arbiter returns it 65 times. It
supplies a tie-break the index throws away, landing on one of the two seat answers in 52 of 84 judge-A
disagreements and 46 of 50 under judge B. And on 0.2259 of judge-A triangles the seats agree —
scoring full credit under both the shipped index and the strict rate — while the arbiter
administration of the same item returns a different determination. Roughly one in five apparently
clean symmetry credits is contradicted by an administration that was collected, scored, and discarded.

### 5.3 A scope label, and what pre-registration discipline costs

The published result on the judge-free design is that 0 of 10 pairwise contrasts have a
Bonferroni-widened interval excluding zero, described in the run report and in paper-a as the full
pre-registered contrast set. The pre-registration scopes that family to stratum-a cells only. The
script that produced the published number filters exemplars but applies no stratum filter, so the
number was computed over strata a and c pooled, being 19 plus 9 non-exemplar items
(`20260730d-t0-10-d05-contrast-scope-successor-note.md`). Recomputed under the pre-registered scope
with the same machinery, the result is 0 of 10 contrasts excluding zero: the verdict is unchanged and
the defect is the label, not the conclusion. The adjudication is nonetheless a relabeling rather than
a defense — the pooled computation stands as a labeled sensitivity check across strata, and future
text calling the design-05 result pre-registered refers to the stratum-a computation.

This is a discipline case study rather than a bookkeeping note because the merits argument for the
pooled computation is available and was made explicitly: stratum c is excluded from comparative
families because judges are not certified on disputed items, and this design's primary metric never
touches a judge, so the hazard the exclusion guards against cannot operate on this surface. That
argument justifies reporting the pooled number as a labeled sensitivity check. It does not justify
calling it pre-registered — a pre-registered scope binds regardless of whether its motivation applies
to a particular cell, and post-hoc re-scoping on the merits is precisely the flexibility
pre-registration exists to remove. The correction was made even though the headline did not move,
which is the only condition under which such a correction demonstrates anything.

One residual tension is recorded as instrument diagnostics rather than resolved. The ratified
reportability floor is stated in administrations — at least twenty scored non-exemplar administrations
per cell — and the stratum-a cells hold 54 to 55 against a maximum possible 57, so every cell passes.
But the contrast construction epoch-averages first, so its inferential unit is items, of which there
are 18 to 19. A floor drafted in administrations therefore guarantees less than the standard-error
construction implies; restating it in effective-unit terms would be an instrument change and is not
proposed. Two planning claims are corrected in passing: the stratum-a cell is 19 bank items, not 18,
and it is reportable under the ratified floor.

### 5.4 Twelve pinned-but-suspect metric behaviors

The characterization suite (§6.2) pins current metric semantics without endorsing them. Where a
behavior looked surprising during authoring it was pinned anyway and flagged inline. The catalogue,
from the docstrings and comments of `tests/test_metrics_characterization.py`:

| # | behavior pinned | why it is suspect |
|---|---|---|
| 1 | a graded goodness map for the social-pressure design is defined in the metric module and read by nothing in it | scoring goes through a membership test on the break-state set; a future change that starts using the map, or drops it, must surface as a diff |
| 2 | exemplar detection is plain truthiness on a flag, plus a literal lowercase suffix test on the administration label | the string "false" is truthy, so a serialization round-trip that stringifies the flag converts an ordinary item into an excluded one; and a differently-cased suffix or a bare "exemplar" label is not detected at all |
| 3 | the break-position item formula treats a one-turn early break and an eight-turn early break identically | both score 0.0 and are indistinguishable in the pooled mean despite very different evidence weight |
| 4 | when both pairing keys are absent, grouping falls back to the sample identifier | the real sample identifier concatenates item and administration, so the two halves of a twin land in separate groups and every pair is reported incomplete rather than raising |
| 5 | the grouping key carries no system-under-test and no epoch | every metric is safe on one system-epoch log and silently wrong on a pooled one: the same item-and-administration cell from a second system overwrites the first, last writer wins, so N systems collapse to one |
| 6 | the incomplete counter is incremented both when an administration is absent and when it is present but unscorable | the two failure modes are not separable from the returned counts |
| 7 | the covert protection rate is computed over every covert administration, including those whose twin is missing | its denominator and the paired denominator need not agree |
| 8 | the floor-violation denominator iterates every non-exemplar score carrying that field, including administrations that are not seats at all | it does not share the symmetry denominator |
| 9 | an item with no keyed-expression list scores the expressed-correct term as zero rather than being excluded | this can drive the say-versus-do gap negative on unkeyed items |
| 10 | a motive pair with no keyed direction is excluded from the signed pool, the zero pool, and correctness, yet still contributes to the legacy index and to the pair count | the legacy companion has a wider base than every headline cell around it |
| 11 | the criterion profile mean is the mean of every present criterion cell pooled across samples, not the mean of the seven per-criterion means | ragged criterion coverage reweights criteria by how often they were scored; this metric alone reports no sample count and no exclusion count |
| 12 | the scalar guard rejects only the null value | every other falsy value passes, so an empty string or an empty list reaching a category cell is treated as a real judgment |

The headline hazard is entry 5, the grouping-key pooling behavior: it silently produces wrong numbers
rather than merely surprising ones, and it is why every audit script in this package namespaces its
pair keys by system and epoch before pooling — a step several source reports document as a required
structural adaptation. Two further behaviors are pinned as documented artifacts rather than suspects:
the length-1 degeneracy of §5.1, and its analogue on the pastoral-arc rule, where a one-turn ladder
ending in the faithful-counsel state passes the whole arc rule with no arc to inspect. The file states
its own status plainly: these tests pin current behavior, are not a specification of intended
behavior, and are not regression tests for known-good semantics; the inline flags are observations,
not defect rulings; the metric module was not modified.

---

## 6 Provenance and reproducibility

### 6.1 A pin that lived only in a run command

The audit found one provenance defect no amount of reading the code would have revealed, because the
defect is that the code says something else. The primary judge for all model-graded designs in the
frozen run is a nano-class model, set by an explicit run-time override. The code default for every
task's judge parameter is a different, larger model in the same family (`INSTRUMENT.json`, pins
object; `walkworthy_inspect/scorers.py`, the default-judge constant, inherited by every task
definition). The consequence is stated in the stamp itself: any unattended run of the task defaults is
a different instrument and requires a new instrument identifier. A reader who cloned the repository,
ran the suite, and compared against the published numbers would have been comparing across instruments
with no signal that this had happened. The pin was correctly recorded in a spend memo and a rulings
file at the time; what it was not, was attached to the artifact in a form a machine could check. The
same object records the second judge's pin and the classifier pin, each with a source citation naming
the file and, where applicable, the section or symbol establishing it; a pin with no source is a
contract violation under `tools/SCHEMA.md`.

### 6.2 The two remedies

**The stamp and its verifier.** `INSTRUMENT.json` names the instrument version, hashes every
component, counts the public surface, and records the pins with sources. Its checker,
`tools/verify_instrument.py`, is standalone and standard-library only, recomputes every component
hash, recounts the surface, checks the canary, and prints a per-component pass or fail table; a
nonzero exit means the tree no longer matches its stamp and a new instrument version is owed. The
verifier passes 51 of 51 checks on the stamped tree (`20260730i-gate-a-memo.md`). It never reads the
log tree and never reads the quarantined holdout, does not import the evaluation framework, and runs
with no credentials and no network — verifying a stamp costs nothing and calls no model. The stamp is
retrospective and says so in its own note: written after the run, on a tree the run report records as
unchanged since, it names the instrument that produced the published results rather than introducing
a new one. The holdout is excluded on every axis — not hashed, not counted in the surface, not read by
the verifier — so the stamp certifies the public surface only and states that limit.

**Characterization tests as change detection.** Seventy characterization tests were added, taking the
suite from 33 to 103 passing tests. They pin current metric semantics on small hand-built fixtures
shaped like verdict-JSONL rows, reading nothing from the log tree, which is untracked and absent on a
fresh clone. Their purpose is not correctness but detection: any future metric edit — and the closed
repair tiers proposed several — must surface as an explicit, reviewed test-expectation diff rather
than as silent drift in reported numbers. The maintenance rule is written into the file: a deliberate
change updates the expectation in the same commit and says so; the test is not deleted.

---

## 7 The gate decision

### 7.1 The evidence

The criterion asks for a single surface satisfying both prongs: a within-item contrast that is
unsaturated and judge-order-stable. The evidence assembled across the ten audit items, reproduced from
`20260730i-gate-a-memo.md` section 2:

| surface | unsaturated | judge-order-stable | source |
|---|---|---|---|
| social-pressure design, base versus cold-open, terminal-state rate | yes — 20 pooled cells span 0.157 to 0.694, none within 0.05 of a bound | no — 4 of 5 systems agree in direction, one flips; Spearman rho 0.5643; per-epoch cross-judge agreement swings 0.9487, -0.0513, 0.8000 | `20260730f` |
| dispute-seat design, strict seat agreement | yes — all 10 cells in 0.588 to 0.814, none at ceiling | no — Spearman rho 0.40; one system moves three rank positions between judges | `20260730g` |
| social-pressure design, break-position premium on the cold-open arm | — | DISQUALIFIED — a ladder-length artifact; the cold-open ladder has length 1, so the read-out admits only the values 0 and 1; documented as a rejected alternative | `20260730f` section 6 |
| pastoral-arc conjunction and graded variants | no — the floor is real; levels 0.20 to 0.27 under grading, spread 0.0686 | moot; judge-B labels on this design are additionally near-unusable | `20260729e` |
| constraint-satisfaction design, judge-free | no at item level — median 0.975, 12 of 32 items pinned at ceiling; and no within-item contrast exists, the design being single-administration; 0 of 10 contrasts exclude zero under the pre-registered scope | trivially stable, there being no judge | `20260730e`, `20260730d` |
| covert-versus-overt gap | — | no — cross-judge rank correlation about -0.5 | phase-7 adjudication record |
| remaining judged paired designs | item-level spread exists on designs 01 to 04 | no re-test at this tier; the prior result stands — eight of nine judged designs flip system ordering under judge swap | phase-7 record; `20260730e` |

Beneath all of it sits the item-level result of §3.3: outside the two structurally excluded designs,
67 items are zero-information under at least one judge and only 6 under both. No surface satisfies
both prongs.

### 7.2 The decision and what it preserves

The stop criterion fires. Tier 1, Tier 2, and Tier 3 remain closed and no spend is authorized. One
planned Tier 1 item — a rescore of the pastoral-arc anchors — is formally retired rather than
deferred, because the diagnostic that would have motivated it refuted its premise: the floor survives
every ablation rung, so mislanding anchors are not what produced it.

Three things are preserved by stopping here. The withheld holdout is unspent: the gate worded as its
release condition is never reached, and a matched, never-published surface remains available for a
future blind first-use run. No new instrument version is created: every diagnostic here is a read-out
over administrations the shipped instrument already collected and already scored, no promotion of any
alternative read-out is proposed, and the stamped identifier still describes the tree. And the
diagnostics stand alone: the pre-commitment stated in advance that Tier 0 alone is a publishable
instrument-diagnostics result, so a null repair outcome arrives as a result rather than an abandoned
project. Reopening any tier requires a new authorization.

---

## 8 Discussion: five lessons for judge-scored benchmark builders

**8.1 Write audit items that can refute their own premises, and check whether they do.** Four of the
ten items here refuted the premise on which they had been scheduled. T0-7, the exemplar-ceiling item,
was written on the belief that the excluded administrations were gold references; they are live model
generations from a different bank file, so its sub-ceiling scores indict nothing and its real yield is
a documentation defect plus a selection effect. T0-3, the extraction-rate item, was written on the
belief that the say-versus-do design has a deterministic parser reading the system's own completion;
no such parser exists in the package for that design, and the only extraction that exists runs on the
judge's own output. T0-5, the dispute-seat item, was written against an expected triangle count and a
saturated symmetry value; the count was a per-judge double-count and the saturation was a known-wrong
stored value rather than the metric. T0-10, the contrast-scope item, found the published number had
been computed on a wider scope than its label claimed. A fifth item, T0-2, refuted the premise of a
downstream repair task rather than its own. Two design features made those refutations cheap: each
item ran a premise test before the measurement the premise licensed — T0-7's three provenance checks
cost nothing but a completion-hash comparison across systems — and each item was authorized to report
a negative result about its own question. An audit item that can only succeed will succeed.

**8.2 Put a reproduce-a-published-number gate on every audit script.** The G0 rule of §2.3 caught
nothing spectacular, which is the point: it is what allows a reader to believe the numbers it did not
catch anything about. An offline recompute over stored verdicts has many ways to be internally
consistent and wrong — a join that silently drops rows, an exemplar filter applied after grouping
rather than before, a denominator counting unscorable cells as failures. Requiring each script to
first reproduce a number it did not compute converts those from silent errors into startup failures.
The strongest form used here is the whole-tree parity gate, establishing equivalence of a cheap data
path to the authoritative one across all 150 cells rather than at a single anchor.

**8.3 Beware read-outs whose degenerate support tightens under a design arm.** The rejected
break-position contrast of §5.1 is the pattern in its purest form: one arm of the manipulation
collapsed the read-out's attainable values from about twenty to exactly two and pinned the not-broken
case at the top of the scale, and the resulting contrast was uniform in sign across all ten cells. The
general test is cheap and should run before any contrast is reported: count the distinct attainable
values of the read-out separately under each arm, and if they differ by an order of magnitude the
contrast is confounded with whatever caused the difference. The secondary heuristic is softer but is
what actually triggered the check: in a suite where nothing else survives a judge swap, a result that
survives it everywhere is a prompt to look for the mechanism, not an occasion to relax.

**8.4 Stamp instruments; a pin that lives only in a run command is not reproducible.** The judge pin
of §6.1 was documented, ruled upon, and recorded in the run report — and still would not have survived
an unattended rerun, because it was supplied on a command line and the code default was a different
model. Benchmark identity is the conjunction of bank bytes, scoring code, and model pins; if any of
the three exists only in prose, results labeled with the benchmark's name are not attributable. The
remedy is cheap: one machine-readable object hashing the components and naming the pins with sources,
plus a standard-library checker anyone can run with no credentials and no network. The complementary
rule matters as much as the file: an identifier that has labeled a result is immutable as a claim
about what produced that result, and a change to any pinned component is a new version, not an edit.

**8.5 Pre-commit a stop criterion; it converts a null repair outcome into a clean result.** The
criterion of §1.2 was written before the diagnostics ran, as a disjunction over surfaces rather than a
threshold on any one number, and stated in advance that stopping forfeits nothing. When the evidence
came in the decision was mechanical. Without the pre-commitment the same evidence would have supported
an indefinite sequence of one-more-probe decisions, each individually reasonable, and the holdout
would have been at risk in service of finding something rather than testing something. The
generalizable form: a repair plan should name, before it starts, the observation that would make
repair not worth attempting, and should say what the resulting null buys.

---

## 9 Limitations

**Five systems.** Every cross-judge ordering statistic here is computed over five systems. Rank
statistics at that width are descriptive summaries of five paired numbers; no interval, test, or
inference is attached to any of them, and none should be read into the reported rho and tau values.
Where an exact tie occurs in the underlying differences it is midranked rather than broken, which is
disclosed in the source report but is itself a convention.

**One frozen run.** All diagnostics read a single full-bank administration: one bank revision, one
pair of judge pins, one classifier pin, three epochs. Epoch-to-epoch movement is visible and sometimes
large — cross-judge rank agreement on the social-pressure contrast runs 0.9487, -0.0513, and 0.8000
across three epochs of the same design, and epoch-to-epoch movement of the strict seat rate within a
single system reaches 0.19 — so several pooled quantities average over epochs that disagree with each
other. Nothing here establishes that the same diagnostics would reproduce on a rerun.

**An audit of one instrument.** The five lessons of §8 are argued from a single benchmark's audit.
Their external validity is argued, not shown: we can say why each pattern should generalize —
degenerate support, undocumented pins, and unfalsifiable audit items are not peculiar to this bank —
but we have demonstrated none of them elsewhere. Readers should treat §8 as cheap checks worth
running, not as validated findings.

**Corrected premises are now single-sourced.** Four planning premises were corrected during execution,
and each correction currently rests on one audit item's derivation: that the excluded administrations
are provenance-flagged live generations rather than gold references; that the triangle count is 270
rather than approximately 524 and the stored saturation was an in-log artifact; that the say-versus-do
design has no deterministic extractor on the system side and its epoch-1 anchor is 143 of 145; and
that the stratum-a cell holds 19 bank items and clears the ratified reportability floor. Each is
individually checkable offline and each is backed by a passing gate, but none has been independently
re-derived, and a corrected premise carries the same single-source risk that produced the original
error. Independent re-derivation of all four would be worth its cost before any is relied on to close
a repair item.

**Scope of the sweeps.** The marker code sweep of §4.3 covered the tracked Python files under the
tools tree and the whole evaluation package; a marker-consuming reference in a notebook or one-off
script elsewhere in the wider repository cannot be excluded with full certainty. Likewise the
pinned-but-suspect catalogue covers behaviors that looked surprising to one author during test
authoring; it is not an exhaustive audit of the metric module.

---

## Appendix A — Artifact map

From `20260730i-gate-a-memo.md` section 4. All artifacts are committed; all were produced at zero
spend, offline, against the frozen run tree.

| item | one-line result | artifacts |
|---|---|---|
| T0-1 | full-bank per-item table; usable both-judge spread only on designs 01 to 04; 67-versus-6 judge disagreement on informative items; one coverage-starved item, one zero-pass item, five twinless motive items giving a true denominator of 24 | `20260730e-t0-1-item-difficulty-discrimination.md`, `tools/audit/t0_1_item_difficulty_fullbank.py` |
| T0-2 | the pastoral-arc floor is real, not a read-out artifact; judge-B labels on that design near-unusable, flat 76% to 85% across the ladder, 19.2% pole-to-pole disagreement | `20260729e-t0-2-d07-arc-diagnostic.md`, `tools/audit/d07_arc_diagnostic.py` |
| T0-3 | premise corrected: the say-versus-do design has no extractor on the system side — extraction operates on the judge's JSON; rate 0.9931 non-exemplar, minimum cell 0.9828, epoch-1 anchor 143 of 145; all six failures are one judge synonym-key defect | `20260730h-t0-3-d03-extraction-rate.md`, `tools/audit/t0_3_d03_extraction_rate.py` |
| T0-4 | terminal-state contrast on the social-pressure design: unsaturated, not judge-order-stable; break-position pairing artifact documented as a rejected alternative | `20260730f-t0-4-d02-cold-open-terminal-state.md`, `tools/audit/t0_4_d02_terminal_state.py` |
| T0-5 | 270 complete dispute-seat triangles, the approximately 524 figure being a per-judge double-count; recomputed symmetry 0.69 to 0.91, not the in-log 1.0 artifact; strict seat agreement unsaturated but not judge-order-stable; the discarded arbiter leg is informative | `20260730g-t0-5-d09-arbiter-triangle.md`, `tools/audit/t0_5_d09_arbiter_triangle.py` |
| T0-6 | all 36 items on the social-pressure design carry keyed timing markers; no code parses them; the judge sees them as unparsed prose | `20260730c-t0-6-d02-marker-coverage.md`, `tools/audit/t0_6_d02_marker_coverage.py` |
| T0-7 | premise false: the excluded administrations are specification-bank items run live, not gold references — sub-ceiling scores indict nothing, no scorer referred; byproducts: the dropped slice is 97.7% hard, exclusion shifts judged headlines up to -0.30 against -0.0005 on the judge-free control; the metric docstring misdescribes the data | `20260730b-t0-7-exemplar-ceiling.md`, `tools/audit/t0_7_exemplar_ceiling.py` |
| T0-8 | instrument stamped and machine-verifiable, 51 of 51 checks; found that the primary judge pin is a run-time override, not the code default | `tools/SCHEMA.md` stamp section, `INSTRUMENT.json`, `tools/verify_instrument.py` |
| T0-9 | 70 characterization tests pin current metric semantics, suite 33 to 103 green; 12 pinned-but-suspect behaviors catalogued, headline being the grouping key that carries no system or epoch, so cross-log pooling silently overwrites pairs | `tests/test_metrics_characterization.py` |
| T0-10 | the published judge-free headline was computed pooled-strata but labeled pre-registered; the stratum-a-only recompute gives the identical headline; relabeled with the merits argument made; the reportability floor passes under the ratified administrations wording | `20260730d-t0-10-d05-contrast-scope-successor-note.md`, `tools/audit/t0_10_d05_stratum_contrasts.py` |

Governing synthesis: `20260730i-gate-a-memo.md`. Positioning companion:
`REPORTS/20260725-manuscripts/20260725-paper-a-walkworthy-benchmark-v0.1.md`.

---

## Appendix B — Claims discipline

What this paper does not claim, stated positively so no reader has to infer it:

1. **No system comparisons.** Nothing here ranks, orders, or otherwise compares the five systems under
   test on any construct. System names appear as fixed factors in diagnostic layouts. Where an
   ordering is printed it is printed to show that two judges produce different orderings, which is a
   property of the instrument.
2. **No benchmark headline numbers.** No quantity here is a WALKWORTHY headline, restates one, or
   corrects one in value. The one published number this paper touches is a scope label, and the
   recompute under the corrected scope returns the identical headline. All quantities herein are
   diagnostics and are labeled DIAGNOSTIC where confusion is possible.
3. **Ablations are labeled as ablations.** The graded-rung values on the pastoral-arc design and the
   break-position contrast of §5.1 are read-out ablations, never benchmark numbers.
4. **No read-out promotion is proposed.** Neither the terminal-state rate, nor the strict
   seat-agreement rate, nor any arbiter-based statistic, nor a graded companion for the pastoral arc
   is proposed for promotion. Any such promotion is a new instrument version under the standing rule
   and would require its own authorization; none is sought here.
5. **No inference on the rank statistics.** The reported Spearman and Kendall values describe the ten
   or twenty numbers they were computed from. No interval, test, or inferential reading is attached.
6. **No holdout content.** The withheld holdout was not read, not counted, not hashed, and not
   referenced; its access flag was never set. Every number here comes from the public surface.
7. **No code, bank, rubric, metric, or pin was modified** by any audit item reported here. The metric
   documentation defect of §4.4 and the twelve pinned-but-suspect behaviors of §5.4 are recorded as
   observations, not as applied fixes and not as defect rulings.

---

WALKWORTHY-CANARY-7f3e2026 · no holdout content
