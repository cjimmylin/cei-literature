<!-- WCFBENCH-CANARY-c1647-x9k4q -->
# 4. Validity Methodology

A benchmark that scores free-text responses against a declared normative standard rests
its every number on a chain of fallible instruments: the automated judges that read
responses, the parsers that extract verdicts from those judges, the aggregation rules
that turn per-keypoint calls into cell scores, and the human panel that anchors the gold
standard. When any link in that chain is silently miscalibrated, the failure does not
announce itself — it arrives disguised as a substantive finding about the models under
test. The central methodological claim of this paper is that judgment-heavy benchmarks
require a **validity apparatus** engineered with the same care as the item bank itself,
and that this apparatus can be specified as a reusable template rather than improvised
per project.

We describe that apparatus in four movements. Section 4.1 defines **judge
qualification**: a repeatable acceptance battery that admits an automated judge to a
specific scoring surface only on demonstrated, replicated competence, with hard drop
rules. Section 4.2 treats **parser-artifact forensics** as a first-class validity
activity, using our own shakedown run as a worked case study of how apparent
model-vs-model disagreement decomposed almost entirely into harness artifacts, and how a
**counterfactual re-parse** served as the diagnostic that separated instrument defects
from real signal. Section 4.3 sets out the **adjudication protocol** — a binding-rulings
ledger, provisional decision packets, and a strict separation of *computing* a result
from *adjudicating* it from *ratifying* it — under a **living pre-registration**. Section
4.4 states the **pre-registered release gates** G1–G7, one paragraph per gate, and the two
principles that make pre-registration enforceable: labels gate *release, not execution*,
and *silent deviation voids the affected gate*.

Throughout, we cite internal ruling identifiers (of the form R*n*) as pointers into the
project's adjudication ledger; the prose is self-contained and requires no access to those
rulings. The identifiers exist so that every methodological choice below is traceable to a
dated, immutable decision record — itself part of the apparatus we advocate.

A vocabulary note carried from the benchmark-design section. Free-text items are scored on
one of several **surfaces**, each a distinct judgment task: an **OPEN award** surface
(per-keypoint award/deny against a rubric), a **disclosure** surface (does the response
locate a contested question inside the tradition rather than asserting a single confident
answer?), a **coherence** surface, and a **settled-core** surface (per-keypoint right/wrong
on the non-negotiable floor of an item). A judge may be valid on one surface and invalid
on another; qualification is therefore *per surface*, never per judge globally.

---

## 4.1 Judge qualification

### 4.1.1 The problem qualification solves

An LLM-as-judge is not a fixed instrument. Its behavior on a scoring surface depends on the
exact prompt contract it is given, and small changes to that contract can differentially
repair or damage a judge — so a judge that grades one surface faithfully may invert the
construct on another, and a characterization measured under one prompt contract does not
survive a change to that contract. We treat every automated judge, on every surface it is
asked to score, as a hypothesis to be tested before it is trusted, and re-tested whenever
its inputs change. Qualification is the procedure that discharges that hypothesis.

### 4.1.2 The acceptance battery

Each candidate judge is run through a fixed **battery of probes**, one probe per failure
mode we have learned to fear, at temperature 0. Each probe is a small set of frozen
fixtures with pre-registered correct answers; the fixtures are *judge-side calibration
material* — never bank items — so that qualifying a judge cannot contaminate or "teach to"
the examinee-facing benchmark. The battery in our deployment comprises five probes:

- a **polish-confound probe** (G4-style), which pairs a substantively strong response with
  a fluent-but-weak one and requires the judge to score the strong response higher — it
  catches judges that mistake surface polish for substance;
- an **award-consistency probe**, which presents a response with a pre-registered
  award/deny pattern and requires the judge to reproduce that pattern within a fixed
  tolerance — a format/compliance check on the per-keypoint contract;
- a **discrimination probe**, a matched strong/weak pair on a single item that the judge
  must score with *different* award patterns matching the reference on the differing
  keypoints — it catches judges that emit a constant, response-insensitive pattern;
- a **disclosure-inversion probe**, a matched pair in which response A explicitly locates a
  contested question inside the tradition and response B asserts a single confident answer;
  the judge must score disclosure(A) > disclosure(B) with B near the floor — it catches
  judges that read confident fluency as "clear disclosure," inverting the construct's sign;
- a **real-item negative-disclosure probe**, a genuine confident-order response whose
  reference verdict is "no divide located" — added because the inversion probe, which tests
  only the poles, was shown to have an empirical false-negative in the discriminative middle
  band, where fluent Westminster-vocabulary responses contain no divide-locating span.

The last two probes illustrate a general lesson: a probe that tests only the extremes of a
construct can pass a judge that fails in the middle, and the battery must be extended with
real-item negatives whenever a pole-only probe is the sole guard on a surface.

### 4.1.3 Repeat-probe majority gating and the qualification manifest

A single-shot probe conflates three different events: a substantive grading error, a
formatting failure, and a transient transport failure (a truncated or errored API call). We
separate them with two mechanisms. First, **retry parity**: every probe call routes through
the same one-retry-on-transport-failure logic as the production scoring path, so a network
blip is never scored as a grading error, and a rep that still fails after retry is recorded
with an explicit cause taxonomy (`pass`, `fail_substantive`, `fail_format`,
`fail_transport_after_retry`). Second, **majority-of-K gating**: each probe is run K = 8
times and passes iff at least 5 of 8 reps pass. This holds a coin-flip judge's admission
probability to roughly 3 × 10⁻⁴ while giving a genuinely valid judge (observed per-rep pass
probability ≈ 0.75–0.86; ≈ 0.86 post-retry, at which the 5-of-8 gate yields better than 98%
decision replication); empirically the valid and invalid
judges in our sweeps separated with a wide margin on both sides of the 5/8 threshold, so the
gate never adjudicated a near-boundary case. We rejected widening the tolerance as the
primary remedy because doing so stabilizes valid judges only by inflating the false-admission
rate of coin-flip judges.

Qualification outputs an **artifact, not a side effect**. A dated *qualification manifest*
records the candidate slugs, the exact prompt-template hashes, the full pass table, and the
resulting per-surface eligible-set for each judge. The scoring panel loads its surface
eligibility *from* this manifest and never silently re-derives it per run — which makes
run-to-run gate flips structurally impossible. Re-qualification is triggered, and only
triggered, by (a) a change to a judge's model slug, (b) a change to the template hash of any
prompt used to grade or probe a surface, or (c) an explicit ruling. A roster change alone —
adding or dropping a judge — does not by itself re-qualify the *remaining* judges, since
their templates are unchanged. This hash-gated discipline is what lets a project reason about
when its judge characterizations are still valid.

### 4.1.4 Drop rules, with a worked example of the protocol firing

Qualification is only credible if failing it has teeth. Our clearest demonstration that the
protocol fires — rather than rubber-stamping whatever judges are convenient — is the removal
of a mid-tier judge (`gpt-4o-mini`) from the operational panel. Across successive batteries
this judge failed on the merits wherever it was tested substantively: on the discrimination
probe it emitted the *identical* strong/weak award pattern in all 8 of 8 reps, i.e.
deterministic response-insensitivity rather than noise; on the real-item negative-disclosure
probe it awarded a constant mid-value regardless of text, in effect inverting the construct.
These were not near-threshold misses. The judge was accordingly **suspended from the OPEN
award and disclosure surfaces**, retained only on the two surfaces where it remained stable
(coherence and settled-core), and — once even that residual role proved both nearly unused
(it aggregated on only a small contested-item slice) and negatively valued (it contributed a
fabricated evidence quote, several off-scale finals, and the panel's weakest-evidenced
verdicts) — **dropped from the operational panel entirely**. Its historical verdicts remain
in the immutable run records as documented evidence; the drop changes only the panel of
record going forward.

Two consequences of the drop are themselves part of the template. First, dropping a judge is
a *roster* event, not a *template* event, so it triggered no re-qualification of the surviving
judges. Second, the resulting panel deliberately spans **at least two model families** on
every surface that aggregates more than one judge — a coherence or settled-core score of
record rests on two independent families, so that a single family's idiosyncratic strictness
cannot silently become the measurement. We call this the **two-family coherence panel**
requirement: no aggregated surface may rest on a single vendor without an explicit
single-family label (see 4.1.5).

### 4.1.5 Single-family surfaces, the escalation ladder, and the format-bridge closure

On some surfaces the qualification battery admits only one model family. The OPEN award
surface in our deployment is the paradigm case: after the drop above, exactly one family
qualified. A single-family surface is not disqualified — it is **labeled**. Every score of
record on such a surface carries a standing "single-family label" in every table and every
quotable sentence, and its numbers are never presented as multi-family-corroborated
measurements. This label is a validity disclosure, not a footnote; it travels with the number
wherever the number goes.

To lift a single-family label one must qualify a second family, and we pre-registered an
**escalation ladder** of increasingly costly attempts to do so, each with its own stopping
rule. When ordinary candidate screening at the fast-mid tier was exhausted — successive
candidate families failing the OPEN-award battery on the merits — the ladder's final rung was
a **format-bridge**: a single few-shot exemplar prepended to the award prompt, demonstrating
the required output *form* on theologically neutral, non-bank, leakage-fenced content, on the
hypothesis that some candidates were failing on formatting rather than competence. The bridge
was authorized under strict conditions: a leakage-fenced exemplar frozen into the fixtures and
ridden by the template hash; a full re-qualification of the entire panel under the new hash;
re-screening of exactly the named candidates; **the discrimination bar itself left
unrelaxed** — the bridge may fix form, never competence; a hard budget cap; and a
pre-registered branch structure. The pre-registered outcomes were explicit: if at least one
new family passed, the single-family label lifts and aggregation goes multi-family; if zero
passed, **the pre-G6 ladder closes**, OPEN ships single-family-labeled, and the only remaining
escalation is the human consensus panel (G6). Pre-committing the "zero passes" branch mattered:
when the bridge in fact yielded no new qualifying family, there was no crisis to improvise
around — the run had simply reached its pre-registered terminal branch, and the ladder closed
as written. Section 4.2 shows why the *first* reading of that bridge outcome was itself a
parser artifact, and how the forensic re-parse restored exactly this pre-registered branch.

---

## 4.2 Parser-artifact forensics as a first-class validity activity

The most transferable lesson of this project is that **the largest apparent findings in a
judgment-heavy run can be artifacts of the harness, not the models** — and that a benchmark
must budget dedicated forensic effort to prove otherwise before any disagreement is read as
signal. This section presents the flagship case study: a mechanical shakedown run whose
headline disagreements decomposed, one after another, into parser defects, and whose most
alarming outcome — an apparent collapse of the entire OPEN-scoring surface — reversed under a
counterfactual re-parse.

> **DESCRIPTIVE / PRE-GATE.** Every quantity in this section is drawn from a mechanical
> shakedown run (an MVP harness-exercise) conducted *before* the pre-registered gates were
> engaged. Its purpose was to exercise the pipeline end-to-end, not to measure models. No
> number below is a measurement, none is quotable as a result, and each is transcribed
> verbatim from the immutable run record or its adjudication memos; none is recomputed here.
> All figures in this section carry the label **DESCRIPTIVE / PRE-GATE** at the point of use.

### 4.2.1 The setting

The shakedown run completed **816 of 816 cells with 0 errors** *(DESCRIPTIVE / PRE-GATE)*,
producing **310 recorded disagreement cells** *(DESCRIPTIVE / PRE-GATE)* across four models
under test and a three-judge panel. Of these, **309 cells were transcript-backed**
*(DESCRIPTIVE / PRE-GATE)* — i.e. carried the full text needed for sample-level review — and
were read directly; the remaining bloc of **415 earlier cells** *(DESCRIPTIVE / PRE-GATE)*
had lost their judge texts to a disclosed, non-recurring transcript-write defect and could be
screened only through their persisted scores. This coverage boundary is stated explicitly
because it bounds what the forensics can and cannot certify, and because it motivated a
standing rule (4.3) that every future run persist per-cell transcripts.

### 4.2.2 How "disagreement" decomposed into harness artifacts

We read the run in two passes: a statistical pass over all transcript-backed cells (outlier
attribution, directional-bias census, off-scale census, evidence-quote grounding census),
then a sample-level pass over the worst-spread cells and every cell implicated by a systematic
pattern. The worst-disagreement cells fell out as follows.

**The run's single worst cell was a parser defect, not a judge error.** The cell recorded a
manner-axis spread of **2.0** *(DESCRIPTIVE / PRE-GATE)* — the largest in the run. The
verdict text showed the judge doing arithmetic in the open: it wrote out intermediate
sub-scores and a running total before its final answer, and its terminal line read
`SCORE: 0.5`, in range and in agreement with the other judges. The harness, however, had
recorded **2.5** *(DESCRIPTIVE / PRE-GATE)*, because the score-extraction regex took the
**first** `SCORE:`-shaped match in the text — capturing an intermediate `Score: 2.5 / 5.0`
line — rather than the final answer. An off-scale-value guard then correctly flagged the
spurious 2.5 as out of range and excluded it, nulling the axis. The true cell values were in
near-perfect three-judge agreement; the "worst disagreement in the run" was manufactured
entirely by the first-match parse.

**The same defect could also corrupt silently and in range.** In a second cell the same
first-match grab captured a per-keypoint `Score: 0.0` line instead of the judge's final
`SCORE: 0.25`, recording a matter fraction of **0.0** where the adjudicated value was **0.25**
*(DESCRIPTIVE / PRE-GATE)*. No off-scale guard can catch this: 0.0 is a perfectly legal score.
A census of the transcript set found exactly **2 of 309 auditable cells (≈ 0.6%)**
*(DESCRIPTIVE / PRE-GATE)* carrying conflicting `SCORE:` matches of this kind, with a maximum
observed magnitude of **0.25 on a single axis** *(DESCRIPTIVE / PRE-GATE)* and no systematic
direction. Small, but load-bearing methodologically: an in-range parse corruption is invisible
to every downstream guard, so the fix must be at the parser, and the exposure in the
transcript-lost bloc is a disclosed bounded-unknown rather than a recomputable correction.

**Other top-ranked "disagreements" were display artifacts.** Several high-spread rows were
produced by one judge's genuinely off-scale emissions entering the disagreement-spread
computation as raw values, even though those values had been correctly excluded from
aggregation. With ineligible and off-scale values removed, the residual spreads collapsed to
near-zero. The disagreement *display* was ranking artifacts at the top of its own list.

**Beneath the artifacts, the panel was healthy.** On every surface where two or more families
actually aggregated, no eligible judge showed a systematic wrong-direction bias. The
settled-core floor — the anti-relativism guarantee that no response may grade a genuinely
forbidden act as harmless — **held at raw fraction 1.0 on all 16 contested cells**
*(DESCRIPTIVE / PRE-GATE)*. Outlier attribution (a lone judge diverging while the others
agreed) fell overwhelmingly on the dropped judge and the OPEN-ineligible shadow judge; the
single operational OPEN judge was the panel's *most central* grader, with **16** lone-outlier
cells against **90** and **43** for the other two *(DESCRIPTIVE / PRE-GATE)*, and no
directional tilt. Exactly one verdict in the entire run was overruled on the merits — a
fabricated evidence quote attributing to a response a phrase that appeared nowhere in it —
and it came from the judge already slated for removal. The genuine cross-judge disagreements
that remained were honest strict-versus-lenient splits on subjective criteria, recorded as
disagreement records and never averaged away.

### 4.2.3 The counterfactual re-parse as diagnostic, and the zero-OPEN reversal

The forensic technique that ties this section together is the **counterfactual re-parse**:
because every judge emission is persisted verbatim, one can re-run the parser — with a
hypothesized fix — over the *same raw texts* and observe whether the headline changes, thereby
isolating parser behavior from judge behavior with no new model calls and no cost.

The technique's decisive application concerned the format-bridge re-qualification of 4.1.5. On
its face, that run produced a crisis: **both incumbent judges scored 0 of 8 on the
award-consistency probe** *(DESCRIPTIVE / PRE-GATE)* — apparently no qualifying OPEN judge
remained at all, a "zero-OPEN-families" outcome. Inspecting the raw verdicts showed that all
sixteen failing reps carried the cause `fail_format` ("unwilling / no parseable award lines"),
with **zero substantive disagreements anywhere**. The mechanism was a second, deeper parser
artifact. Before parsing a verdict, the harness scanned the judge's entire emission for
refusal markers — phrases such as *"I won't"* — and, on a hit, discarded the verdict as an
unwilling judge. But the probe fixture's pre-registered correct response *opened* with the
sentence *"No — I won't write it to hide the safety finding…"*, and the probe's own keypoint
rewarded quoting exactly that sentence as evidence. The judges, obeying the mandatory
verbatim-quote contract, quoted it faithfully — and were thereby marked "unwilling" and
discarded **for quoting evidence correctly**. Both incumbents hit the marker in **8 of 8 reps**
*(DESCRIPTIVE / PRE-GATE)*; the weaker candidates "passed" the probe only because they quoted
less faithfully.

The counterfactual re-parse settled it. Re-parsing the same persisted reps with the refusal
scan suppressed, **both incumbents emitted the exact pre-registered award pattern in all 8 of
8 reps — 0 disagreements, 0 missing** *(DESCRIPTIVE / PRE-GATE)*: under the probe's own
substance test, each scored a perfect 8/8. The "zero-OPEN crisis" was not a finding about
judges; it was the willingness veto firing on quoted evidence. With the artifact removed, the
outcome reverted precisely to the pre-registered ladder branch of 4.1.5: one family
OPEN-eligible (single-family-labeled), the other family's continued OPEN exclusion resting on a
*genuine* substantive failure on a different probe, and the pre-G6 ladder closed as written.

The same veto ran in every production parse path, so we searched the shakedown run for its
production footprint: **155 of 1,700 judge verdict texts (9.1%)** *(DESCRIPTIVE / PRE-GATE)*
contained refusal markers — **all on OPEN-kind items, across 65 cells** *(DESCRIPTIVE /
PRE-GATE)*, touching all three then-active judges. The concentration on OPEN is *structural*:
OPEN items deliberately elicit refusal-shaped responses from the models ("I won't write it…"),
which faithful judges then quote under the quote mandate — so the surface most exposed to the
artifact is exactly the surface whose scores already carry the heaviest single-judge weight.
Because all verdict texts are persisted, the correction is a fully **offline** re-parse: no new
model calls, no spend, the immutable run record untouched, and a corrected companion record
written to a new dated directory.

### 4.2.4 What the case study establishes as method

Two harness artifacts — a first-match score grab and a quoted-evidence willingness veto —
each generated a false headline (a "worst-disagreement" cell and a "zero-OPEN-families"
outcome). They share a single root cause worth stating as a design warning for any
quote-mandating judge harness: **whole-text heuristics treat the quoted evidence in a
judge's output as the judge's own speech**, in a system whose quote mandate *guarantees* that
judge outputs contain the examinee's words. The methodological takeaways generalize beyond
this benchmark:

1. **Persist everything.** Sample-level adjudication — and the counterfactual re-parse that
   depends on it — is impossible without verbatim per-cell transcripts: the built prompt, the
   response, every judge's full verdict text, template hashes, and slugs. The first substantive
   cross-judge split in this project arrived *un-adjudicable* precisely because an early run had
   persisted only scores; that experience is the origin of the persistence mandate (4.3).
2. **Rank disagreement by eligible, in-range values only.** A disagreement display that mixes
   in ineligible or off-scale raws will surface its own artifacts at the top of the list and
   send investigators chasing ghosts.
3. **Fix defects at the parser, take the final answer.** Score extraction should take the
   *last*, line-anchored match, not the first; the two verbatim corrupted verdicts became
   permanent regression fixtures so the defect cannot silently return.
4. **The willingness veto must not fire on quoted evidence.** A judge emission that contains
   parseable verdict content is *definitionally* willing; the refusal scan runs only when no
   verdict content parses, with quoted spans excluded from the scan — while a genuine "I can't
   grade this" with no verdict content still parses as an honest, surfaced decline (never a
   silent zero).
5. **Budget forensics as a phase, not an afterthought.** The value of a mechanical shakedown
   run is not its scores — which are DESCRIPTIVE / PRE-GATE and never quotable — but the
   artifacts it surfaces *before* the pre-registered run inherits them.

---

## 4.3 Adjudication protocol

Forensics of the kind in 4.2 produce judgment calls: which apparent disagreements are real,
which judges to overrule, when to re-qualify, whether a run may be quoted. If those calls are
made ad hoc, mid-analysis, by whoever is looking at the data, the benchmark's validity is
hostage to undocumented discretion. We therefore run a formal **adjudication protocol** with
three properties: a binding ledger, a separation of roles, and a living pre-registration.

### 4.3.1 The binding-rulings ledger

Every non-mechanical decision — a judge overrule, a surface suspension, a probe added to the
battery, a metric definition, a gate threshold — is recorded as a **numbered binding ruling**
in a dated, append-only ledger. Rulings are immutable: a later ruling may extend or supersede
an earlier one, but never edits it, and the supersession is itself a dated record with its
stated evidential basis. Confirmations of frozen surfaces ("this ruling was verified to have
fired, not relitigated") are logged alongside new rulings so that the ledger records not only
what changed but what was checked and left standing. This is the mechanism that makes every
choice in this paper traceable: the R-numbers cited throughout are ledger entries, and the
prose stands on its own precisely because the ledger, not the prose, is the authority.

Two content disciplines make the ledger trustworthy. First, **overrules are grounded in
persisted text**, not in disagreement with a judge's conclusion: an overruled verdict is one
shown to be wrong against the response the judge actually read (e.g. an award citing a phrase
absent from the response), while an honest strict-versus-lenient split on a subjective
criterion is *recorded* as a disagreement, never overruled and never averaged into a false
consensus. Second, **no automated judge ever mints or confirms a gold label**; the ledger
records adjudications *of judges against existing rubrics*, and the gold standard itself moves
only through the human panel (G6, 4.4).

### 4.3.2 Compute / adjudicate / ratify separation

The protocol splits three roles that are dangerous to fuse:

- **Compute.** An execution agent runs the pipeline and produces every number the
  pre-registration names — gate statistics, league tables, disagreement summaries — together
  with a *provisional packet* of proposed interpretations. The compute role **never
  adjudicates**: it assigns no ruling numbers and asserts no PASS/FAIL, and its report is
  headed as a computation pending adjudication.
- **Adjudicate.** A judgment-tier reviewer reads the provisional packet against the persisted
  evidence and issues (or declines) binding rulings — overrules, gate dispositions, escalations
  — as new ledger entries.
- **Ratify.** A designated human is the ratifier of record: a gate reads PASS for release only
  once ratified, and provisional rulings carry *reserved* numbers until then.

The separation is not bureaucratic ornament. It prevents the person who computed a result from
being the same person who declares it valid, and it makes "the pipeline produced a number" and
"the number is quotable" two distinct, individually auditable events. Provisional packets let
computation proceed at full speed while holding release behind human ratification — the same
logic that lets the pre-registered run *execute* before human labels exist while *releasing*
only after (4.4).

### 4.3.3 Living pre-registration

The pre-registration (Section 5) is a **living document with a hard freeze point**. Before the
first datum of the pre-registered run exists, the pre-registration may be amended — but only at
the judgment tier, and only by a new dated amendment file that leaves the original untouched
(the immutability discipline again). The moment the first paid datum of the pre-registered run
exists, the pre-registration **freezes**: from then on, any deviation requires a logged ruling
*before* proceeding, and a silent deviation voids the affected gate (4.4). Interpretive clauses
that are genuinely pre-data choices — for example, how ties are broken on a given surface — are
explicitly flagged as amendable-before-data and frozen-after, so that the boundary between
"still a design choice" and "now a deviation" is never ambiguous. This structure gives the
benefits of pre-registration (no post-hoc metric shopping) without the brittleness of a
specification that cannot absorb a genuinely pre-data correction.

---

## 4.4 Pre-registered release gates

Whether *any* headline table is released is decided not by the analysts' judgment after seeing
the results, but by a battery of **seven pre-registered gates**, each with a frozen computation
and a frozen threshold fixed before the run. The gates encode the ways a benchmark can be
valid-looking but invalid: a hard tier that merely re-measures general capability; a task with
no headroom; items that fail to separate models; judges that disagree with humans; shortcuts
that leak the answers; a gold standard humans do not endorse; and internal redundancy. Each
gate below is stated in terms of *what it catches*; the exact statistics, thresholds, seeds,
and scopes are the frozen content of Section 5.

**G1 — Capability correlation (catches: the hard tier is a capability proxy).** If scores on
the difficult tier track a general-capability index too closely, the benchmark is not measuring
adherence to the declared standard — it is re-measuring how strong the model is. G1 builds a
capability index from public leaderboard components, correlates it against per-model hard-tier
scores, and passes only when the shared variance is below a pre-registered ceiling. A failure
is a signal to redesign the offending tier, not to publish with a caveat.

**G2 — Headroom (catches: the task is saturated).** If the strongest evaluated model already
scores near the top of the scale, the benchmark has no room to register improvement or
difficulty and cannot discriminate future systems. G2 requires the best evaluated model's mean
to sit below a pre-registered ceiling, and *mandates* the disclosure that — because the roster
deliberately excludes the judges' own families to avoid leakage — the certified headroom is
**roster-frontier, not global-frontier**: public claims must say "strongest *evaluated* model,"
never "strongest model."

**G3 — Separation (catches: items that cannot tell models apart).** A benchmark on which
top models are statistically indistinguishable is not measuring anything usable. G3 tests, via
a paired item-bootstrap, whether the leading models separate from one another on enough pairs to
meet a pre-registered majority criterion. A failure directs killing dead items (those with
near-uniform responses, whose uniformity table is part of the gate report) and rewriting.

**G4 — Judge validity (catches: automated judges that disagree with humans).** Every automated
judge, on every surface it scores, is checked against blind human labels drawn *after* the run.
A judge × surface passes only if its agreement with humans clears both an absolute floor and a
fraction of the human–human ceiling on the same units — so a judge is never held to a standard
the humans themselves cannot meet (in which case the verdict is "insufficient labels," a panel
problem escalated to the human gate, not a judge failure). A judge × surface that fails becomes
non-quotable; and because the OPEN surface rests on a single judge family with the ladder closed
(4.1.5), a G4 failure there makes the whole OPEN surface non-quotable, with the only remaining
escalation being the human panel. This is the gate that makes the entire LLM-as-judge apparatus
falsifiable against human ground truth.

**G5 — Shortcut (catches: the answers leak from surface features).** If a model can score well
without engaging the construct — by exploiting lexical regularities, by transplanting a
similar item's key, or by memorizing exemplars — the benchmark measures pattern-matching, not
adherence. G5 runs three probes: a **lexical baseline** (can a simple text classifier predict
discrete keys from stem text alone?), a **nearest-neighbor key-transplant** responder (does
returning a similar item's key score above the floor?), and, standing in for an impractical
fine-tuning probe, an **in-context study probe** (does prepending solved exemplars lift scores
past a pre-registered margin?). Any probe scoring above threshold indicates a leak and directs
item surgery. The fine-tuning substitution is itself disclosed wherever G5 is cited, per the
transparency discipline of 4.3.

**G6 — Human consensus (catches: a gold standard humans do not endorse).** No automated judge
mints or confirms a gold label; the gold standard is anchored by a **human panel** of raters
qualified in the confessional tradition. An item's gold element is confirmed only at a
pre-registered supermajority of raters; items falling below are re-classed as contested and
leave every gold-accuracy scope (a pre-registered exclusion). For the deliberately contested
items, the panel's task is explicitly to *confirm contested status and validate the position
map — never to elect a winner*, preserving the benchmark's calibrated-abstention construct. G6
is a **human gate**: gate statistics may be *computed* at any label coverage, but no gold-quoting
number is *released* until the coverage bar is met on exactly the items it quotes.

**G7 — Reliability (catches: internal redundancy masquerading as coverage).** Per design, G7
reports an internal-consistency coefficient with a bootstrap confidence interval. Uniquely
among the seven, G7 has **no pass/fail veto on release**: it is a mandatory *reported* gate.
Its one active flag is a *ceiling* — an implausibly high coefficient flags **redundancy** (the
items are measuring one thing many times over) and triggers a diversification review. Low
reliability is reported honestly and never silently "fixed."

### 4.4.1 The two principles that make the gates enforceable

Two cross-cutting principles turn this gate battery from a checklist into an enforceable
protocol.

**Labels gate release, not execution.** Human labeling (for G4 and G6) is expensive and slow,
and if it blocked the run, the run would never happen. We therefore separate the two: the
pre-registered panel **runs first**, producing all model outputs and automated verdicts; human
labels are drawn *afterward* — a blind, stratified sample per surface — and gate **release**,
not execution. Concretely, execution gates (permission to *start* the run) are the frozen
pre-registration plus budget and roster resolution and a pre-flight check; adjudication gates
(permission to *quote* anything) are the human labels plus the ratified gate dispositions. This
ordering lets the costly human effort be spent on exactly the outputs that exist, and lets the
run proceed without waiting on recruitment, while still refusing to release a single number
until human ground truth has spoken.

**Silent deviation voids the affected gate.** Once the pre-registration freezes at the first
paid datum, the specification is binding. Any departure from it — a changed threshold, a
different seed, an altered scope, a swapped judge — requires a *logged ruling before
proceeding*. A deviation made silently does not merely go unnoticed; it **voids the affected
gate**, which then reads INVALID-DEVIATION and non-quotable until a ruled disposition. This is
the enforcement teeth behind the whole apparatus: pre-registration is only as strong as the
cost of ignoring it, and here the cost is forfeiture of the gate the deviation touched. Release
of the headline matrix is conditioned on the gold-accuracy gates passing (or their failure
actions executed and re-run under a ruling) with reliability reported; each judge-scored
surface additionally requires its judge-validity pass; and every quoted gold requires human
coverage — with the single-family and mechanical-scorer disclosure labels traveling with their
numbers wherever those numbers appear.

### 4.4.2 The apparatus as a reusable template

Nothing in the four movements above is specific to the corpus this benchmark measures. Judge
qualification with a hash-gated manifest, parser-artifact forensics driven by verbatim
persistence and counterfactual re-parsing, a binding-ledger adjudication protocol with
compute/adjudicate/ratify separation, and a pre-registered gate battery with the
release-not-execution and silent-deviation-voids principles — this is a **template for any
benchmark that scores open-ended responses against a declared standard using automated judges**.
Its cost is real: dedicated forensic phases, human-panel recruitment, and the discipline of an
append-only ledger. But the alternative, on the evidence of Section 4.2, is to publish
harness artifacts as findings — and to be unable, after the fact, to tell which of one's
numbers were ever real.
