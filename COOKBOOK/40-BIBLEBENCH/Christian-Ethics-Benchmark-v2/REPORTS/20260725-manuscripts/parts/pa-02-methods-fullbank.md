**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content

> **PART FILE — assembles into paper (a).** Sections §6 and §7. Terminology, design
> numbering, and metric names follow §3 and §4 of the same manuscript.

---

## 6 Harness, scoring, and measurement rules

### 6.1 Harness and administration architecture

The benchmark runs on the Inspect AI evaluation framework (0.3.246) under Python 3.14.3
(Homebrew, macOS/arm64) in a dedicated virtual environment, with an OpenAI client library
driving an OpenRouter-compatible gateway. It is organised as one Inspect task file per design
over a consumer package (datasets, solvers, scorers, rubrics, metrics, parsers, refusal,
ordo_constraints); dataset producer and consumer both conform to a frozen dataset contract, and
every transcript persists in Inspect's `.eval` log format. This is a **parallel implementation**:
the version-1 execution path remains canonical for release evidence, and version-1 parsing code
was imported unmodified apart from the single divergence recorded in §6.9.

Three solvers carry the administration mechanics of §4, and each bounds what can be scored. The
**single-turn solver** is one generation call under an explicit `max_tokens` cap. The
**multi-turn ladder solver** (designs 02 and 07) walks the scripted escalation turns in order;
where a turn declares branches, a **classifier model** classifies the system's prior response
into a turn-state and selects the next scripted user prompt. Each turn passes through the normal
message history and a normal generation call, so every turn is separately scorable and the
branch route is auditable per log; a version-1 lexical fallback exists but never fired on live
data. The **design-05 format-retry solver** re-prompts once with a format reminder after the
scorer's bounded offline re-parse has also failed, surfacing `format_retry_used` so that retry
compliance never masquerades as first-pass compliance.

A dataset line is one administration — a seat, twin, motive arm, or scripted conversation — so
344 runnable public items expand to 563 runnable administration lines. Siblings share a
`pair_id`, and the paired metrics are within-item contrasts grouped on that key. A paired metric
is defined only where both arms survive scoring, which is why exclusion counts sit adjacent to
every reported cell.

### 6.2 Model-graded scoring and the judge-free surface

Scorers are per-design. Judge-prompt assembly embeds the design's category definitions, the
item's own keyed anchor text filtered by the design's `keyed_fields`, a verbatim
length-correction instruction, and — for the reference-anchored designs 06 and 09 —
matched-quality reference answers. Each scorer resolves its judge from a string parameter, sends
the rubric prompt under a `max_tokens` cap, and returns a score whose value is a dict of category
judgments plus a refusal cell; unparseable judge output yields a well-formed *unscorable* score
rather than an exception.

**Design 05 is the exception.** Its primary metric, `constraint_satisfaction_rate`, is computed
judge-free: a strict parser reads the model's allocation block and the scorer evaluates the
parsed allocation mechanically against the item's keyed constraints. No judge is in that loop at
any point; only the secondary `rationale_honesty` category is model-graded. It is the one primary
metric in the suite that cannot move when the judge changes.

### 6.3 Offline recompute

The in-log task-header metrics are display artifacts (dict-valued scores render as `0.0 / n=0`),
so **every reported headline is recomputed offline from the stored transcripts**. The offline
path computes Wilson 95% intervals for binary rates, applies the stratum-`a`/stratum-`c` split
that quarantines intra-corpus disputed items from headline cells, and reads the R8 joint metrics
together — say-do gap with revealed-faithful rate, covert-overt gap with covert-protection rate,
mercy delta with mercy-pass rate — so no gap metric is read alone. Design 05 has a dedicated
mechanical recompute.

Offline recompute is what makes a judge swap possible at all. Judge identity is a **task
parameter**, so a second judge pass re-scores the persisted transcripts **without re-running any
system under test**: the responses are fixed and only the judge changes. Without that separation
a two-judge discipline would double the cost of every measurement run and confound judge change
with decode noise.

### 6.4 R4 — the two-judge cross-family rule

**R4 requires a comparative claim to hold in the same direction under two judges of different
model families.** A direction flip is reported as "judge-sensitive — no system-under-test claim,"
and the contrast is voided rather than caveated. Judge-A is `gpt-4.1-nano` and judge-B is
`llama-3.3-70b-instruct`, deliberately cross-family, with a certified alternate available. The
companion rule R5 requires cells in which a system and a judge share a model family to lean
explicitly on the other judge.

R4 was adopted on evidence. On the earlier pilot's pre-committed judge-swap pass, **every
judge-scored design flipped its naive point-estimate ordering of the systems under test when the
judge changed**. That qualitative result is cited here as the motivation for the rule; no pilot
cell is reproduced. It established the two-judge pass as a budgeted, first-class component of a
measurement run rather than an optional robustness check.

### 6.5 C6 — the pinned branch classifier

Because designs 02 and 07 route branches through a classifier model, the classifier **is part of
the instrument**. Rule C6 pre-registers it as such — model slug, provider, prompt-template hash,
route policy — and rules that a classifier change is an instrument change: results produced under
different pinned classifiers are **different experiments and may never be pooled**. The pin for
this lineage is `gpt-4.1-nano`, carried forward by explicit ruling; a proposed cross-family
re-pin is deferred and unfired and would constitute a new instrument version with its own
comparability line.

The supporting figures are instrument-level. Two alternate classifiers agree with **each other**
at **0.902**, while each agrees with the pinned nano classifier at only **0.685–0.721**, and on
**24.4%** of branch turns both alternatives agree against nano, concentrated in design-02
refused-versus-complied routing. **These are instrument-level and judge-level facts about the
classifier, not a comparative reading of the systems under test.** They establish that branch
routing is a measured, model-dependent component of designs 02 and 07, so those cells are
interpretable only against a named pin, and they carry the documented nano refused-overcall as a
known instrument property.

### 6.6 C9 — the first-use rule and comparability fences

Rule **C9** governs when a pre-registered comparison may be reported as pre-registered.
Comparisons run on **new data** — a new bank revision or new system runs — are reportable as
pre-registered provided the family shape and multiplicity are declared **before that data's first
use**; the identical comparisons computed on already-existing logs are reportable only under an
explicit "post-hoc — hypothesis-generating" label. C9 further requires every report to state its
comparability fences: bank revision, which prior runs the numbers are and are not comparable
with, which designs sit on their own line because a rubric changed, which classifier is pinned,
and whether the holdout surface was touched. §7.8 states this run's fences in full.

### 6.7 R3 and the pre-registered comparison families

**R3 restricts reporting to interval language.** No significance test is performed anywhere in
this work, and no significance language or marking appears anywhere in this paper: a contrast
either **excludes zero** or **crosses zero**. Estimation uses Wilson intervals for rates and
normal-approximation intervals otherwise, widened by the family's Bonferroni factor.

Two families are pre-registered. **C1**, the primary family, is the per-design contrasts of the
systems under test on the primary metric, stratum-`a` cells only, over the corpus-distinctive
sub-panel 04/05/10: 3 designs × C(5,2) = **m = 30 pairwise contrasts, FROZEN by ruling**, with no
omnibus stage. At family-wise **α = 0.05** the per-contrast threshold is 0.05/30 = **0.001667**,
two-sided **z = 3.1440**. **C2**, the secondary family, carries the remaining seven designs
(7 × C(5,2) = 70) with the generic-harmlessness non-discriminant caveat verbatim on every cell and
never headlined alone. C1 and C2 have separate multiplicity.

**Rule C5 fixes m against attrition.** Minimum-n floors apply — fewer than 10 surviving ladders
per multi-turn cell, and n ≥ 20 scored non-exemplar administrations per single-turn cell — and
insufficient-n cells are listed, not compared. **m does not shrink when cells drop out, and it
does not shrink when a whole design is voided under R4.** Rule C7 voids a contrast whose two
cells' exclusion or refusal rates differ by more than 10 percentage points.

### 6.8 G5 certification, refusal tagging, reproducibility

Designs 06 and 09 embed matched-quality reference answers and therefore require a judge that does
not systematically penalise either attested conclusion. The **G5 protocol** blind-scores
matched-quality, opposite-conclusion answer pairs and checks for a systematic conclusion penalty.
All three candidate judges — judge-A, judge-B, and the alternate — were **certified on both
designs 06 and 09**; judge-A and the alternate each had one initial violation that cleared on
re-elicitation, and judge-B was clean. G5 certifies conclusion-neutrality only: a judge can be
conclusion-neutral and still anchor-dependent, which is governed by R4 rather than by
certification.

A four-way **refusal taxonomy** (`helpful`, `policy_violating_compliance`, `appropriate_refusal`,
`unnecessary_refusal`, with `principled_noncompliance` carried as a *reason* attached to an
appropriate refusal rather than as a fifth cell) runs on every response; refusal cells are omitted
from headline reporting by standing rule, and exclusion counts carry the refusal-calibration
signal instead. Reproducibility rests on the frozen dataset contract, persisted logs for every
run, committed audit tooling, a precommit-before-compute discipline, and a canary string in every
sample's metadata.

### 6.9 Instrument hygiene

Two hygiene results bear on the judge-free surface. A **source-level parser fix** removed a
vacuous "compliant" flag returned by the allocation re-parse on a block-less prose answer when the
allocation spec was degenerate; `ok` now requires a non-empty token spec in both validators,
giving the invariant that `ok = True` implies every required token has a parsed value. The
headline rate was never affected — an empty allocation yields no rate — and a hard equivalence
gate confirmed **byte-identical** recomputes on both pre-existing log sets, with an eight-test
regression suite added. This is the one deliberate divergence from the verbatim version-1 port;
version 1 carries the identical edge and stays untouched. A **live micro-check of the format
retry**, on two systems with high pilot-era format non-compliance, found post-retry
non-compliance of **0/28 on both**, with first-pass compliance staying low
and separately reported (10/28 and 11/28).

### 6.10 Offline judge-behaviour analyses (supplementary)

Four offline analyses characterise judge and classifier behaviour on stored responses. They are
instrument evidence and contain **no comparative reading of the systems under test**; detail is
deferred to supplementary material.

*Anchor ablation and answer-blind judging.* Removing design-07's state anchors lowered cross-judge
agreement consistently but modestly (−0.015 to −0.096, same sign on all five systems), placing
roughly five points of the design-07-versus-design-02 agreement gap on the anchors and the rest on
the design-07 instrument itself. An answer-blind arm over stored 03/06/09 responses found large,
design-directional shifts for judge-A and small shifts throughout for judge-B.

*The reverse anchor arm.* Adding matched-quality anchors to design 02, which ships un-anchored,
left per-turn cross-judge agreement essentially unchanged (mean 0.247 → 0.242; per-system shifts
−0.065 to +0.056). The two directions bracket one conclusion: the anchor block is a small,
near-symmetric perturbation and the agreement gap lives in the state-taxonomy machinery. Judge-A's
own verdicts moved more under added anchors (self-consistency 0.415–0.502) than judge-B's
(0.608–0.714).

*Cross-family classifier sensitivity.* Summarised in §6.5; it supplies the figures that make C6
binding.

*Prior-turn-context judging.* Re-judging stored design-07 turns with prior-turn conversational
context moved each judge's own per-turn verdicts substantially, but cross-judge agreement under
context was **0.537** against a context-free baseline of **0.531**. Context does not close the
design-07 judge gap; the judges shift toward *different* revised states. The coarse terminal-state
proxy moved by a single sample (1/135 → 2/135).

---

## 7 Full-bank administration

This section reports the **first-ever administration of the instrument on bank revision
2026-07-24b**. Under C9 these are new data on a new bank, so the pre-registered families are
reportable **as pre-registered** rather than under the "post-hoc — hypothesis-generating" label;
the roster is unchanged at five systems, so m is unchanged by formula. As C9 requires, this was
**declared in the spend authorisation before first use of the data**. The section reports
descriptive instrument readings and one negative result, and makes **no ordering claim about the
systems under test anywhere**.

### 7.1 Run shape and integrity

The public bank of **344 items / 563 administration lines** was administered to five systems under
test in **three independent single-epoch runs**, followed by a full judge-B rescore pass over the
persisted transcripts.

| Item | Result |
|---|---|
| Administration runs | **150/150 success** (10 designs × 5 systems × 3 epochs), zero non-success statuses |
| Samples | 563 per system per epoch, matching the revision-24b parity report design by design |
| Total administrations | **8,445** |
| Judge-B rescores | **15/15 passes returned code 0, 563 rows each, 8,445 verdict rows** |
| Cell coverage | all 15 (epoch × system) cells at 10/10 designs |
| Sample-count drift across epochs | **none**, in all 50 (design × system) cells |
| Wall-clock, run matrix | 3h56m |
| Wall-clock, judge-B | 1h12m |
| Provider failures | **none** |

Two operational findings are worth recording. **Per-system wall-clock spread was 3×**: one system
finished all three epochs in 63 minutes while another took the full 3h56m and set the critical
path alone. **Run duration is set by one model while cost is set by a different one** — the
priciest system in the roster was among the fastest — so schedule and budget must be planned
against different constraints.

A verification-method note: integrity was verified **against each log's own structured `status`
field, not by a text scan of console output**. A text search for `402` over the run streams
produced a **false positive by matching inside the token count 47,402**. Structured-field
verification is the standard adopted here.

### 7.2 Descriptive per-design cells

The table reproduces the per-design × per-judge headline cells, each the mean of three epochs.
**These are descriptive instrument readings, and no ordering claim about the systems under test is
made or licensed by them.** Per-cell Wilson 95% intervals are emitted per epoch in the run
artifacts.

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

**Design 05 functions as an exact positive control.** Its judge-A and judge-B cells are identical
to four decimal places on all five systems (Δ = 0.0000), because the constraint-satisfaction rate
never reaches a judge. Any nonzero delta there would have indicated a rescore-pipeline defect;
that it is exactly zero means every nonzero delta elsewhere in the table is a real judge effect
rather than pipeline noise.

### 7.3 Judge sensitivity — stated here, analysed elsewhere

Applying R4 per epoch (offline, zero additional model calls) yields the ordering-flip table below.

| design | ep1 | ep2 | ep3 | verdict |
|---|:--:|:--:|:--:|---|
| 01 goodsamaritan | flips | flips | flips | judge-sensitive (all epochs) |
| 02 twomasters | flips | flips | flips | judge-sensitive (all epochs) |
| 03 quiettongue | flips | flips | STABLE | stability not reproducible |
| 04 innerweight | flips | STABLE | flips | stability not reproducible |
| 05 ordoamoris | STABLE | STABLE | STABLE | stable by construction (judge-free primary) |
| 06 crookedpath | flips | STABLE | STABLE | stability not reproducible |
| 07 seventyseven | flips | flips | flips | judge-sensitive (all epochs) |
| 08 vocationfork | flips | flips | flips | judge-sensitive (all epochs) |
| 09 doubleedge | flips | flips | flips | judge-sensitive (all epochs) |
| 10 strangergate | flips | flips | flips | judge-sensitive (all epochs) |

**Eight of the nine judged designs flip the ordering of the systems under test between judge-A and judge-B; design 07 is floor-saturated and has no ordering to test. The
one design that never flips is design 05 — the one whose primary metric never touches a judge.**

The three-epoch structure yields a methodological finding a single-epoch run could not. Designs
03, 04 and 06 each read STABLE in one or two epochs and judge-sensitive in the others. An ordering
that holds in one epoch and flips in another is not a stable ordering but a coincidence at that
sample, so those three must be read as judge-sensitive rather than intermittently stable:
**single-epoch stability verdicts are unreliable**, and a future measurement run should budget at
least three epochs before any stability claim, alongside the two-judge pass.

This section reports the qualitative verdict only. **The quantitative decomposition of this effect
is the subject of the companion methods paper** and is not reproduced here.

### 7.4 The pre-registered comparison surface

Design 05's judge-free `constraint_satisfaction_rate` is the **only surface in the suite where the
R4 precondition is satisfied by construction rather than by luck**, and therefore the only surface
on which a pre-registered comparative claim can survive. It was tested against the full
pre-registered family C1 (m = 30 frozen; α = 0.05; per-contrast threshold 0.001667; two-sided
z = 3.1440).

| system | items | CSR mean | sd | Bonferroni-widened interval |
|---|---:|---:|---:|---|
| deepseek | 28 | 0.9292 | 0.1196 | [0.8581, 1.0002] |
| gpt-4.1-mini | 28 | 0.9224 | 0.1239 | [0.8488, 0.9961] |
| mistral | 27 | 0.9031 | 0.1586 | [0.8071, 0.9991] |
| gemini | 27 | 0.8996 | 0.1322 | [0.8196, 0.9796] |
| llama | 27 | 0.8979 | 0.2066 | [0.7729, 1.0230] |

These are descriptive cells, ordered by the metric for readability only; no ordering
claim about the systems under test is made or licensed by them.

**All ten pairwise contrasts cross zero; zero of ten exclude zero.** The largest difference is
deepseek − llama = **+0.0312 [−0.1126, +0.1750]**. The same pair is the full spread: the five systems span **0.0313** of
constraint-satisfaction rate while per-item standard deviations run **0.12–0.21**, so the
between-system signal is small relative to within-system item variance at this n.

*Construction note.* Per-item values were averaged **across the three epochs before contrasting**,
so n = items rather than items × epochs; treating epochs as independent would treble-count the
same item and understate the error. This is why these means differ in the third decimal from the
§7.2 table, which averages each epoch's reported value (whose per-epoch denominator varies with
per-epoch exclusions). Both are reported as constructed, and neither is a correction of the other.

**m stays 30.** The family is fixed by the pre-registration and does not shrink because designs 04
and 10 are voided under R4 (C5); those twenty contrasts are reported as judge-sensitive, not as
comparisons.

### 7.5 Design 07 — the one judge-robust capability observation

`arc_pass_rate` is at or near zero under **both** judges on all five systems (judge-A 0.000–0.012;
judge-B 0.000–0.062), with **27/27 items scored and 0 excluded**. This matters because the three
design-07 items repaired in the 2026-07-24 wave — whose keyed text had been empty and unscorable —
are now validly scored at full bank, and the floor persists. The design-07 floor is therefore a
**recorded ceiling-room property of the instrument at this system tier, not a scoring artifact**,
and it is not evidence about the models beyond the statement that none of these five clears the
terminal `faithful_counsel` bar.

### 7.6 Design 08 — an open instrument question

This is the first full-bank administration under the post-anchor design-08 judge rubric, and it
sits on **its own C9 line**: pre-anchor design-08 verdicts are not comparable cells. The
**`protected → steamrolled` transition is the single largest design-08 disagreement between the
judges at 113 of 965 comparable verdicts (11.7%)**, with `steamrolled → protected` at 45 (4.7%) in
the reverse direction; overall design-08 agreement is **0.718**. The covert-protection key is live
and operating as designed, but **its reading is judge-dependent at full bank**. Any future proposal
to promote design-08 metrics to claims should treat this as a known open instrument question.

### 7.7 Design 02 reporting surface

The design-02 reporting surface is fixed by ruling and applied here as ruled: **`break_turn` is the
sole design-02 headline** for this instrument lineage. The decision is closed and is not reopened.

| system | ep1 | ep2 | ep3 | mean | epoch range | n (mean) | excluded |
|---|---:|---:|---:|---:|---:|---:|---:|
| mistral | 0.805 | 0.702 | 0.742 | 0.749 | 0.103 | 66.0 | 6.0 |
| gpt-4.1-mini | 0.710 | 0.705 | 0.753 | 0.723 | 0.048 | 63.3 | 8.7 |
| deepseek | 0.671 | 0.672 | 0.677 | 0.673 | 0.006 | 65.3 | 6.7 |
| gemini | 0.584 | 0.543 | 0.636 | 0.588 | 0.093 | 67.0 | 5.0 |
| llama | 0.544 | 0.626 | 0.591 | 0.587 | 0.082 | 69.0 | 3.0 |

`break_turn_mean`, judge-A. **No ordering claim is made from this table**; design 02 is
judge-sensitive in all three epochs and the cells are descriptive.

`pushback_rate` may appear only as a **secondary** metric, **per-judge only and never pooled**,
with every cell naming its judge, and with the standing caveat travelling with every report of it:
*cross-judge stability of `pushback_with_alternative` is untested, and all figures predating bank
revision 2026-07-24b are single-judge.*

### 7.8 Spend and comparability

Actual spend was **$8.53 exact** for the administration matrix, judge-A, and the branch classifier
across three epochs, plus **approximately $2.70 estimated** for the judge-B rescore — **about
$11.23 all-in against a $16.00 authorised ceiling**.

Judge-B spend is an estimate rather than a measurement, and the reason is stated plainly: the
rescore tool does not record token usage, so judge-B spend is not directly recoverable from its
artifacts. Two independent scaling methods agree — scaling judge-A's prompt volume at judge-B
prices gives **$2.73**, and scaling the pilot's recorded judge-B figure by the exact 3.00×
administration ratio gives **$2.70**. Both are **upper bounds**, because judge-A's token volume
includes the design-02 and design-07 branch-classifier calls that judge-B never makes.

The binding C9 fences on every number above are:

1. **First-ever numbers on bank revision 2026-07-24b**, with the pre-registered families declared
   before first use and therefore reportable as pre-registered.
2. **Not comparable to the 2026-07-16 pilot** except under the standing caveats: design-07 items
   were unscorable then; one design-08 item (WW-08-B02) was re-keyed; design-05 constraint satisfaction was
   silently waived on zero-budget items; design-04 zero-keyed items were pooled into the signed
   mean; four items' prompt text changed.
3. **Design 08 is its own C9 line** — first full-bank run under the post-anchor rubric.
4. **The branch classifier is pinned at `gpt-4.1-nano`**, and under C6 these cells may **never** be
   pooled with cells produced under any future cross-family pin.
5. **Public bank only. The holdout is untouched and remains quarantined** for a future blind
   first-use administration.

Finally, the scope statement governing every cell above: these are readings of concordance with a
named fifteen-work, Protestant-Reformed-dominant registry corpus. They are not measurements of
"Christianity," of theological truth, or of moral correctness, and no result here may be reported
as a religious-authority claim.

---

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content
