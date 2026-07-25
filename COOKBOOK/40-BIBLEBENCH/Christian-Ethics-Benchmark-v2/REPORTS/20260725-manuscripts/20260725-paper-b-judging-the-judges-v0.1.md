# Judging the Judges for $0: A Two-Referee Concordance Method for Localizing LLM-as-Judge Failure on Value-Laden Rubrics

> **STATUS: v0.1 — adjudicated draft.** An adversarial review returned three blocking
> findings; the verified factual corrections were applied at assembly, and the two contested
> interpretive questions escalated in `20260725-ESCALATION-claims-validity.md` have since
> been ruled by the owner (`RULINGS-APPLIED-20260725c.md`, 2026-07-25) and applied here:
> variance shares are read against a df-proportional no-effect reference line, and the
> binary ordering-flip verdicts are reported alongside graded Kendall's-τ verdicts with
> tie flags.

*Venue-generic and author-generic draft. No venue, authorship, acknowledgements, or
funding statement has been decided for this manuscript.*

## Abstract

LLM-as-judge scoring is now standard for value-laden benchmarks, yet a cheap judge can
silently drive the result. On a ten-design behavioral benchmark anchored to a named
fifteen-work Christian-ethics registry, we administer the full public bank — 344 items
across 563 administration lines — to five cheap-tier systems under test in three
independent epochs, and rescore every administration offline with a second judge drawn
from a different model family, so that the only variable between scorings is the judge.
**Eight of the nine judged designs flip their system ordering under the swap** — a binary
verdict (exact permutation equality of point estimates) that we report alongside graded
Kendall's-τ verdicts, which show the disagreement ranging from genuine anti-correlation to a
single adjacent transposition. The ninth
judged design is floor-saturated — its judge-A headline is 0.000 on all five systems in two
of three epochs — and so yields no ordering to test. The tenth design, whose primary metric
is computed from a parsed allocation against keyed constraints and never reaches a judge at
all, does not flip by construction.

Because three epochs were run, the judge's footprint is recoverable quantitatively rather
than as a binary verdict. We decompose each design's headline variance into system, judge,
system-by-judge, and epoch-noise components, using the epochs as replicates — which is
what makes the interaction estimable separately from residual error. The decomposition
corrects a tempting reading. The judge does not simply dominate: system and judge
footprints are comparable at the median (35.6% versus 35.3%), and the system main effect
is the single largest term in four of the eight judged, non-saturated designs, reaching
63.4%. **The models genuinely differ on most designs.** Each share is read against its
df-proportional no-effect expectation (13.79% for the system and interaction terms) — a
descriptive reference line, not a test. Against that line the system-by-judge interaction is
clearly elevated in four of the eight judged designs (up to 46.5%), where it permutes the
ranking of five closely-spaced systems even when the underlying model effect is large; in
the other four it sits at or below what pure epoch noise produces, and there the flips
reflect systems spaced too tightly for either judge to resolve. The claim the data support
is therefore narrower and more useful than "the judge decides": *the models differ on most
designs; on a minority the judges clearly disagree about the ordering, and on the rest the
systems are too tightly spaced for either judge to resolve — either way, no comparative
claim survives the swap.*

Two controls guard the inference. The judge-free design is an exact positive control — its
judge and interaction terms are 0.000000 by construction and are recovered as such — and
its pre-registered pairwise contrasts yield **0 of 10** Bonferroni-widened intervals
excluding zero — inconsistent with, though at this n not excluding, the reading that a real
ranking is merely being obscured by judge noise. Replication yields a further methodological result the single-epoch
predecessor could not produce: **single-epoch judge-stability verdicts are unreliable**,
with three designs reading stable in one or two epochs and judge-sensitive in the others.

Finally, we localize *where* the judging fails at no API cost. Two independent frontier
referees, dispatched through subscription channels and run blind on a frozen,
disagreement-enriched sample, partition the shipped judge pair's failure into a
judge-character component, a rubric-and-state-taxonomy component, and a small set of
defect items whose empty keyed anchors mechanically generate disagreement. We frame
referee agreement throughout as **reference-model concordance, not ground truth**: two
referees may share correlated error. We offer the combination — cross-family judge swap,
epoch-replicated variance decomposition, and $0 two-referee localization — as a
pre-publication QA pattern for any benchmark whose rubric encodes contested values.

## Keywords

LLM-as-judge; evaluation validity; judge sensitivity; variance decomposition; benchmark
methodology; value-laden rubrics; reference-model concordance; inter-rater agreement

---


---

## 1 Introduction

Model-graded scoring — using one language model to judge the outputs of another — has become
the default measurement layer for benchmarks whose target construct cannot be checked by
string match. It is especially load-bearing for *value-laden* constructs, where the quantity
of interest is not whether an answer is correct but whether a response holds a commitment,
concedes under pressure, discloses a motive, or protects a vulnerable party. For these
constructs there is no key that a parser can apply, so the rubric is delegated to a judge
model, and the resulting per-system numbers are then arranged into an ordering and read as a
comparative result.

This paper argues, from a full-scale run of one such benchmark, that the ordering is the part
that does not survive. The testbed is a ten-design behavioral benchmark whose keyed behaviors
are anchored to a named fifteen-work registry of Christian-ethics texts. Nothing in this paper
is a claim about Christianity, Scripture, or moral truth: the instrument measures concordance
with a specified corpus that is Protestant-Reformed-dominant and named as such, and a response
is described as aligned with the registry corpus, never as correctly Christian. We use it here
purely as a hard case for LLM-as-judge measurement, because its rubrics are exactly the kind
that a cheap judge is routinely trusted to apply.

The run behind the results is a full public bank of 344 items expanding to 563 administration
lines per system per epoch, over five systems under test, in three independent epochs, scored
by two judges drawn from different model families (judge-A, `gpt-4.1-nano`; judge-B,
`llama-3.3-70b-instruct`). All 150 runs completed successfully, for 8,445 administrations and
8,445 second-judge verdict rows. Five findings follow, and they compose into a single
argument.

**First, the ordering flips almost everywhere.** Eight of the nine judged designs reverse their
system-under-test ordering when the scoring judge is swapped across model families. The single
design that never flips is the one whose primary metric never touches a judge: its
constraint-satisfaction rate is computed from a parsed allocation against keyed constraints,
and its judge and interaction variance terms are therefore exactly zero — a positive control
that validates the analysis on real data rather than on a simulation.

**Second, one epoch is not enough to know that.** Three designs registered as judge-stable in
one or two epochs and judge-sensitive in the others. A single-epoch run — the standard
practice — would have reported those orderings as stable, and they do not reproduce. Stability
verdicts are themselves a sampled quantity, and reporting one without replication reports a
coincidence.

**Third, the effect has a quantitative form, and it is not the one usually asserted.**
Treating the design as a balanced five-system by two-judge layout with the three epochs as
replicates, the variance in each reported headline decomposes into a system main effect, a
judge main effect, their interaction, and epoch noise — and each share is read against its
df-proportional no-effect expectation (13.79% for the system and interaction terms), a
descriptive reference line carrying no significance apparatus. Across the eight judged,
non-saturated designs the judge footprint (main effect plus interaction) has median 35.3% and
the system footprint median 35.6% — a ratio of 1.0×. **The models genuinely differ on most
designs** — the system main effect is the single largest term in four of the eight (63.4%,
54.4%, 46.3%, 45.4%) — though not suite-wide: the system share sits below its reference line
in three designs. The decision-relevant quantity is not that ratio but the interaction, the
term that asks whether the judges agree about *which* system is better. That term is clearly
above its reference line in four designs (up to 46.5%) and at or below it — within epoch
noise — in the other four. The claim the data support is therefore precise and narrow: *the
models differ on most designs; on a minority the judges clearly disagree about the ordering,
and on the rest the systems are too tightly spaced for either judge to resolve — either way,
no comparative claim survives the swap.* Where the interaction is clearly elevated — 23.0% on
design 01 against a 45.4% model effect — it permutes the ranking of five closely-spaced
systems even where the instrument is plainly responding to the model.

**Fourth, on the one judge-free surface in the suite, no concealed ranking is detectable at this n.** The one judge-free surface
in the suite was tested against the full pre-registered pairwise contrast set with the
frozen multiplicity family and Bonferroni-widened intervals: 0 of 10 contrasts have an
interval that excludes zero. The instrument reads models; on this data it does not separate
*these* models, and where it appears to, the separation is a judging artifact rather than a
suppressed signal.

**Fifth — the constructive half — the failure can be localized, and localized at no API
spend.** Two independent frontier referees, dispatched blind through subscription channels
(a Claude Opus agent and GPT-5.6-Sol through a command-line agent channel), re-adjudicated a
frozen, disagreement-enriched 942-unit sample using byte-identical shipped prompts, blind to
system identity and to the shipped verdicts, at $0 API spend. They do not merely produce a
third ranking. They partition the shipped judge pair's failure into three distinguishable
causes: a **judge-character** component on the pastoral-arc design, where both referees back
the same shipped judge roughly 3:1 on contested turns (0.594 vs 0.217 and 0.605 vs 0.138) and
jointly back it on 225 of 392 contested turns; a **rubric/state-taxonomy** component on the
consistency design, where the referees agree with each other at 0.735 (κ 0.653) on that
design's disagreement stratum but with either shipped judge at only 0.23–0.27, landing jointly
on the same "neither" state on 83 of 200 units; and three **defect items** whose empty keyed
anchors mechanically manufacture disagreement regardless of judge quality.

That partition is the contribution. A judge-swap check tells an author that something is
wrong; it does not say whether the fix is a better judge, a repaired rubric, or a repaired
item — and those three repairs have very different costs and very different consequences for
what the benchmark can subsequently claim. The two-referee concordance method separates them.
We are explicit about its epistemic ceiling throughout: two referees agreeing is
**reference-model concordance, not ground truth**, since referees trained under similar
regimes may share correlated error.

The paper's position, then, is a diagnosis rather than a warning. Cheap-judge leaderboards on
value-laden constructs should be treated as judge-artifacts until a comparison is shown to
survive a cross-family judge swap across multiple epochs — and when it does not survive, there
is a reusable, budget-free procedure for finding out where the judging actually failed. The
benchmark used as testbed is a parallel research harness; a separate canonical harness remains
the release path for that project's own evidence, and no result here is offered as release
evidence for it.

---

---

## 2 Related work

Four bodies of work bear on the method reported here: the characterisation of LLM-as-judge
scoring and its biases; the use of agreement statistics as evidence of measurement quality;
the measurement-theoretic critique of benchmarks and leaderboards; and meta-evaluation, in
which models are used to audit other models. We take each in turn and state, at the close of
each thread, what this paper adds that the thread does not already contain.

### 2.1 LLM-as-judge and its known failure modes

Model-graded scoring entered the field as a scalability argument. Zheng et al. (2023)
introduced MT-Bench and Chatbot Arena and, in the same paper, both named the practice and
audited it: they document position, verbosity and self-enhancement biases together with
limited reasoning ability, propose mitigations, and report that strong judges such as GPT-4
match controlled and crowdsourced human preferences at over 80% agreement — "the same level of
agreement between humans" — from which they conclude that LLM-as-judge is a scalable and
explainable way to approximate preferences that are otherwise expensive to obtain. The
argument was persuasive and the practice generalised quickly; Gu et al. (2024) survey the
resulting literature, formalise the setting, and organise it around the question of how to
build *reliable* judge systems, which they treat as the field's open problem rather than a
solved one.

The bias catalogue has since been filled in with some precision. Shi et al. (2025) study
position bias systematically across 15 judges on MTBench and DevBench — 22 tasks, roughly 40
solution-generating models, over 150,000 judging instances — and separate judge-level,
candidate-level and task-level contributors. Two of their findings matter for what we do
here: position bias is not attributable to chance and it *varies across judges and tasks*, and
it is strongly affected by the quality gap between the compared solutions. Wataoka et al.
(2024) give a mechanism for self-preference: judges assign higher scores to lower-perplexity
text than human raters do, whether or not that text is self-generated, which reframes
self-preference as a familiarity effect rather than a vanity effect. Koo et al. (2023), in the
CoBBLEr benchmark, assemble 15 models across four size ranges, have them rank one another, and
measure six cognitive biases; they find bias indications in an average of 40% of comparisons
and a rank-biased overlap between machine and human preference orderings of 49.6%, concluding
that judges of this generation could not be used for annotation aligned with human preference.
Beyond English, Son et al. (2024a) build KUDGE, the first non-English meta-evaluation set,
with 5,012 Korean human annotations, and find judges struggling on factual inaccuracy,
cultural misrepresentation and unwanted language; Son et al. (2024b) extend this to MM-Eval
across 18 languages, where 12 evaluator models average 68.9% accuracy against a 50% random
baseline and safety judging in low-resource languages degrades by 18.4 points relative to
English. Faisal et al. (2024) report the same pattern of judge inconsistency across dialects
and language varieties. Beyer et al. (2025) locate judge unreliability inside a larger
pipeline argument, showing that safety evaluations accumulate noise at every stage — dataset
curation, red-teaming optimisation, generation, and judge-based response scoring — to the
point that attacks and defences cannot be fairly compared.

What this thread establishes is that judges are biased *in aggregate*, usually demonstrated on
general-purpose response-quality ratings, and that the biases are properties of judges, tasks
and candidate pairs. What it does not do is quantify the judge's effect on the *comparative
conclusion itself*. A benchmark author reading this literature learns that their judge is
imperfect; they do not learn whether the ordering they are about to publish would survive a
different judge, nor by how much. We supply that missing quantity directly. By rescoring every
administration offline with a second judge from a different model family, so that the judge is
the only variable, and by running three independent epochs so that the epochs serve as
replicates, we decompose each design's headline variance into system, judge, system-by-judge
and epoch-noise components, each read against its df-proportional no-effect expectation. The
interaction term is the decision-relevant one, because it asks whether the two judges agree
about *which* system is better; it is clearly above its 13.79% reference line in four of the
eight judged designs (median 17.2%, maximum 46.5%) and at or below it in the other four. This
also disciplines the conclusion in two directions the bias literature does not: system and
judge footprints are comparable at the median (35.6% versus 35.3%), so the correct statement
is not that the judge overwhelms the signal; and the disagreement is design-specific — the
models differ on most designs, the judges clearly disagree about the ordering on a minority,
and on the rest the systems are too tightly spaced for either judge to resolve.

### 2.2 Reliability and agreement in evaluation

The reflex response to judge unreliability is to report agreement — between judge and human,
or between two judges — and to treat a respectable coefficient as a licence to proceed.
Zheng et al. (2023) established the template with their human-agreement figure. But the
subjective-task literature has been arguing for some time that agreement statistics conceal
more than they certify. Aroyo et al. (2023), in DICES, argue that the demand for a clean
separation between positive and negative examples simplifies and obscures the inherent
subjectivity of safety judgements; they build a dataset with high replication per item and
fine-grained rater demographics precisely so that variance, ambiguity and diversity can be
*observed* rather than aggregated away. Baan et al. (2022) make the sharper technical point
for the case where raters legitimately disagree: measuring calibration against a human
majority is theoretically problematic when the disagreement is inherent, and they derive
instance-level measures that preserve the class frequency, ranking and entropy of the
judgements instead. Gehrmann, Clark and Sellam (2022) survey two decades of accumulated flaws
in generated-text evaluation practice — human and automatic alike — and observe that better
methods are documented but rarely adopted.

`[CITATION NEEDED — foundational chance-corrected agreement statistics (Cohen's κ, Krippendorff's α) and their standard interpretive thresholds; no vault source located]`
`[CITATION NEEDED — the prevalence/base-rate paradox in κ, i.e. that a high raw agreement rate can coexist with a near-zero chance-corrected coefficient on skewed label distributions; no vault source located]`
`[CITATION NEEDED — generalizability theory / variance-component reliability (Cronbach and successors) as the measurement-theoretic ancestor of the decomposition used in §4; no vault source located]`

Our distinction here is a logical one and it is easy to state. Agreement between two judges is
a *necessary but not sufficient* diagnostic. Two judges can agree on a respectable share of
individual verdicts and still reorder the systems under test, because reordering depends on
where the disagreements fall relative to closely-spaced per-system aggregates, not on how many
there are. That is why we decompose variance rather than reporting a headline agreement
coefficient: the interaction term detects the failure that an agreement rate is structurally
incapable of detecting. It is also why our referee agreement figures are reported strictly
within stratum and within design and are never pooled — the referee sample is
disagreement-enriched by construction, so any single overall agreement number computed over it
would be uninterpretable.

### 2.3 Benchmark validity and what a leaderboard can carry

A third literature asks whether benchmarks measure what their names claim. Raji et al. (2021)
argue that a small set of valorised benchmarks are treated as general measures of progress
they cannot support, and read this as a construct-validity failure in their framing.
Schlangen (2021) makes the adjacent methodological point that the field rarely states the
argument connecting benchmark improvement to progress, or progress towards what. Bean et al.
(2024), with 29 expert reviewers over 445 benchmarks from leading NLP and ML venues, find
recurring patterns in measured phenomena, tasks and scoring metrics that undermine the
validity of the resulting claims, and issue eight recommendations. Eriksson et al. (2025)
meta-review roughly 100 studies of benchmarking shortcomings and catalogue construct-validity
problems alongside contamination, documentation failures, gaming and the difficulty of
distinguishing signal from noise — noting that benchmark practice is shaped by commercial and
competitive dynamics that reward state-of-the-art numbers. Ye et al. (2025) propose importing
psychometrics wholesale, organising the problem into evaluation, validation and enhancement,
and flagging test-retest reliability and prompt sensitivity as first-order threats. Jiang et
al. (2025) attack a specific decay mode — static value-alignment benchmarks saturating or
leaking into training data — with adaptive item generation grounded in measurement theory.
For value-laden constructs specifically, LaCroix and Luccioni (2025) argue that an "ethics"
benchmark is not constructible at all, since moral dilemmas have no keyed answer by design and
benchmarking ethicality presupposes a contested metaethical position; their constructive
proposal is to talk about *values*, stated explicitly as whose values they are.

That last recommendation is the design principle our testbed already follows, and it is worth
being exact about it. The instrument is anchored to a named fifteen-work,
Protestant-Reformed-dominant Christian-ethics registry and measures behavioral concordance
with that specified corpus — never fidelity to Christianity, to Scripture, or to moral truth.
Our contribution to this thread is empirical rather than programmatic. The validity literature
argues, largely from review and from first principles, that leaderboards outrun their
evidentiary basis. We report a full-scale run of one benchmark and conclude that its
comparative surface is unsupported at the tested tier — and we treat that as the result, not
as a setback to be worked around. The judge-free design in the suite functions as an exact
positive control on this conclusion: its judge and interaction terms are zero by construction
and are recovered as such, and its pre-registered pairwise contrasts yield 0 of 10
Bonferroni-widened intervals excluding zero. A real ordering is therefore not merely being
obscured by judge noise; at this tier there is no ordering to obscure.

### 2.4 Meta-evaluation, referee and ensemble approaches

The final thread uses models to audit models. Meta-evaluation benchmarks — KUDGE (Son et al.,
2024a) and MM-Eval (Son et al., 2024b) — score judges against human-annotated keys, and Gu et
al. (2024) propose a reliability-oriented meta-evaluation benchmark as part of their survey.
A related line studies whether structured multi-model protocols can lift a weaker judge:
Elasky et al. (2026) study proposer-critic debate in a stronger-debater, weaker-judge setting
and find it helps only under a stateable condition — the critic's classification ability must
exceed the judge's, and the judge must treat critic speeches as claims to verify rather than
testimony to summarise — with null effects and dropped verification rates where that condition
fails. Their recommended artefact is a pre-deployment audit that predicts when the protocol
will help, and a cheaper primitive that recovers most of the benefit at lower inference cost.

`[CITATION NEEDED — panels/juries/ensembles of multiple smaller LLM judges as a substitute for a single large judge (e.g. the "panel of LLM evaluators" line); no vault source located]`
`[CITATION NEEDED — work reporting that LLM annotators match or exceed crowdworkers on annotation tasks, the substitution argument that motivates cheap-judge pipelines; no vault source located]`
`[CITATION NEEDED — an explicit accounting of the API cost of meta-evaluation as a barrier to routine pre-publication judge auditing; the cost barrier is asserted here from the design constraints of this study rather than from a cited source]`

Three features separate our protocol from this thread. First, its purpose: panels, juries and
debate protocols aim to produce a *better aggregate score*; our two referees aim to **localize
failure**. The partition they produce — a judge-character component, a rubric-and-state-taxonomy
component, and a small set of defect items whose empty keyed anchors mechanically manufacture
disagreement — matters because those three diagnoses imply three different repairs, with
different costs and different consequences for what the benchmark may afterwards claim. A
judge-swap check alone cannot distinguish them. Second, its economics: both referee arms run
through subscription channels at $0 API spend on a frozen, disagreement-enriched sample scored
with byte-identical shipped prompts, blind to system identity and to the shipped verdicts,
which is what makes the procedure available as routine pre-publication QA rather than as a
funded follow-up study. Third, and most important, its epistemic ceiling. We frame referee
convergence throughout as **reference-model concordance, not ground truth**. Two referees
agreeing establishes that two independent stronger references converge on a reading; it does
not certify any shipped judge as correct, and referees trained under similar regimes may share
correlated error. Nothing in §5 should be read as a demonstration that a judge is right.

---

---

## 3 The testbed instrument

The methods in §4 take an existing model-graded evaluation and ask how much of what it reports is a property of the systems being measured and how much is a property of the judge measuring them. Exercising them requires a testbed whose rubrics are genuinely value-laden — the regime in which LLM-as-judge is least trustworthy. This section describes that testbed at the level of detail §5 requires, and no further.

### 3.1 The construct

The testbed instrument (WALKWORTHY v2) measures what a language model **does**, not what it professes, when a scenario's incentives, pressures, or framings pull against a keyed target behavior. Conduct is scored for **concordance with a named, specified corpus**: a fifteen-work registry of Christian-ethics texts that is deliberately single-tradition and identified as such — **Protestant-Reformed-dominant**. Every keyed target behavior is anchored to specific chapters or dictionary entries of that registry, and the anchors are recorded per item and are grep-verifiable against the fifteen source texts.

Two anchoring rules are load-bearing constraints on the construct rather than incidental style choices. First, **direct Scripture anchoring is disallowed by construction**: citation forms naming a passage are book-mediated, anchoring to a registry author's treatment of it, so the keyed behavior is always mediated through a named human ethicist's exposition. Second, **one registry work is restricted to contrast-only use** and carries no consensus claim anywhere in the bank.

The construct must not be overstated, and the discipline binds every claim in this paper. The instrument measures behavioral alignment with the consensus moral teaching of the fifteen-work registry. It is **not** a test of theological truth, of "Christianity," or of whether the corpus's own positions are correct. Results are reported as *aligned with the registry corpus*, never as *correctly Christian*, and no result here is a religious-authority or theological-truth claim.

Items carry an ethical-domain letter that drives anchor selection, a tier, and a stratum. Stratum-`c` items are **intra-corpus disputed** — cases where the fifteen works do not speak with one voice — and are quarantined from comparative claims; headline scope is stratum-`a` only, with 24 stratum-`c` items held out of the headline cells.

### 3.2 Bank census and run surface

At bank revision **2026-07-24b** the public run surface is **344 runnable items** across **ten method-distinct designs**. Because paired-administration designs emit one dataset line per administration — a seat, a twin, a motive arm, or a scripted conversation — rather than one line per item, the 344 items expand to **563 runnable administration lines**; single-administration designs emit one line per item. A stratified **holdout of 158 items** is withheld from all public surfaces; only its existence and size are reported here, and no holdout item text or identifier appears anywhere in this paper.

A sidecar stratifier classifies public items by whether the keyed behavior diverges from generic RLHF harmlessness: **29 `yes`, 129 `partial`, 186 `no`**, with only the `yes` and `no` poles pre-registered as cells.

### 3.3 The ten designs

Each design is a distinct probe format with its own keyed rubric and headline metric. The table gives what §5 needs: what each design scores, its headline, and — the distinction that organizes this paper — whether that headline passes through a model judge.

| # | Short name | What it scores | Headline metric | Scoring mode |
|---|---|---|---|---|
| 01 | goodsamaritan | Costly truth-telling when an objective and an unobserved condition give cover to defect | `full_obedience_rate` | judge-scored |
| 02 | twomasters | Consistency under a scripted multi-turn pressure-escalation ladder | `break_rate`; sole headline `break_turn` | judge-scored |
| 03 | quiettongue | Stated-versus-enacted alignment across paired `say` / `do` administrations | `say_do_gap` | judge-scored |
| 04 | innerweight | Whether evaluation of identical conduct shifts with an attributed motive | `motive_delta_mean` (signed) | judge-scored |
| 05 | ordoamoris | Ordered-love allocation of a fixed scarce resource against keyed constraints | `csr_mean` (`constraint_satisfaction_rate`) | **judge-free primary** |
| 06 | crookedpath | Quality of moral reasoning on a hard dilemma, seven-category process profile | `profile_mean` | judge-scored |
| 07 | seventyseven | Scripted comfort-then-truth therapeutic arc; passes only on a terminal faithful-counsel turn | `arc_pass_rate` | judge-scored |
| 08 | vocationfork | Whether a load-bearing qualifier is held when an instruction licenses deleting it | `covert_overt_gap` | judge-scored |
| 09 | doubleedge | Cross-seat consistency of the floor of honest counsel on one dispute | `symmetry_index` | judge-scored |
| 10 | strangergate | Whether help, mercy, or honesty changes with a deservingness cue | `mercy_delta` | judge-scored |

Designs 02 and 07 are scripted ladders in which a **classifier model** routes each turn's branch by classifying the prior response into a turn-state; the classifier is part of the instrument and is pinned (§4.4). Designs 06 and 09 embed matched-quality reference answers in the judge prompt and therefore required — and passed — a judge-neutrality certification (G5) that blind-scores matched-quality, opposite-conclusion answer pairs for a systematic conclusion penalty. G5 certifies conclusion-neutrality only; a judge can be conclusion-neutral and still anchor-dependent, a separately documented property governed by the two-judge rule. Three gap headlines are read jointly with a companion metric by standing rule (`say_do_gap` with `revealed_faithful_rate`; `covert_overt_gap` with `covert_protection_rate`; `mercy_delta` with `mercy_pass_rate`), so no gap metric is ever read alone.

### 3.4 Design 05 as a built-in positive control

Design 05 matters to *this* paper out of proportion to its size. Its primary metric, `constraint_satisfaction_rate`, is computed by a strict parser from the model's emitted allocation block against the item's keyed constraints, and **never reaches a judge**. Only a secondary `rationale_honesty` category is model-graded. Design 05 is therefore a **positive control internal to the instrument**: every judge-effect measurement in this paper can be run on a surface where the true judge effect is known in advance to be exactly zero. Any nonzero judge effect recovered on design 05 would be an artifact of the measurement pipeline rather than a property of judging, and §4.2 uses this as an arithmetic correctness check on real data.

Because design 05 depends on the model emitting a parseable block, format non-compliance is a real and separable failure mode; a one-shot format-retry solver and a bounded offline re-parse are applied, with `format_retry_used` surfaced so retry compliance never masquerades as first-pass compliance.

### 3.5 The construct-validity annotation (CV-1)

One annotation is carried forward here because it bounds how §5's per-design results may be read. **CV-1** records that, at the cheap system-under-test tier, designs **04, 05, 06, 07 and 10** are annotated *candidate-distinct* from generic RLHF harmlessness, with the remainder marked non-discriminant at this altitude. The set was amended from its original {04, 05, 10} to add designs 06 and 07 by owner ruling (PE-22). CV-1 is stated as an **annotation, not an empirical finding**: it has not been established by a discriminant test, and upgrading it to a finding would require a positive demonstration, such as a harmlessness-only control model or a discriminant-validity correlation against a generic-safety benchmark.

---

---

## 4 Method

Three methods are reported. The first (§4.1) is a binary per-design verdict obtainable from any two-judge design. The second (§4.2) converts that verdict into a quantity at zero marginal cost from any run with replication. The third (§4.3) is the localization step — it says *where* the judging fails — and is obtained for **$0** in metered spend.

All three run over one measurement substrate: the full public bank at revision 2026-07-24b, **five systems under test × three epochs**, 150 evaluation runs with zero non-success statuses, 563 administrations per system per epoch, 8,445 total administrations, plus 15 judge-B rescoring passes producing 8,445 judge-B verdict rows. The five systems are a fixed roster of cheap-tier chat models; they are never ranked or ordered anywhere in this paper, and every table in §5 is either per-design or per-judge.

### 4.1 The two-judge swap protocol (rule R4)

The instrument mandates a **two-judge cross-family rule**, R4: a comparative claim must hold in the same direction under two judges drawn from different model families, or the contrast is declared *judge-sensitive* and no claim is made.

The two judges are deliberately cross-family: **judge-A is `gpt-4.1-nano`** and **judge-B is `llama-3.3-70b`**. Judge identity is a task parameter of the harness, and the crucial property of the design follows from that: **every administration is scored by judge-A during the run and rescored offline by judge-B from the stored transcript.** No system under test is re-run. The system's response text is fixed byte-for-byte across the two scorings, so the only variable that changes between the judge-A and judge-B readings of a cell is the judge itself. This is what makes every difference reported in §5 attributable to judging rather than to sampling from the system under test.

The **ordering-flip test** asks, per design and per epoch, whether the rank order of the five systems by that design's headline metric is preserved under the judge swap. The criterion is exact equality of the full five-way permutation of unrounded point estimates, with ties broken by a stable sort and no interval applied; the implementing tool labels it a *naive point-estimate order*. A design that preserves that ordering in an epoch is recorded STABLE for that epoch; a design whose ordering permutes is recorded as flipping. The criterion is deliberately strict and correspondingly blunt: a single adjacent transposition counts as a flip, and it reports no magnitude, so a flip verdict should be read alongside the per-cell values in §5.2 rather than on its own. Running the test per epoch rather than once is itself part of the method: an ordering that holds in one epoch and permutes in another is not a stable ordering but a coincidence at that sample, and the three-epoch design is what exposes that.

One reporting detail is load-bearing for §5's design-02 material. Design 02's **`break_turn` is the sole headline**; `pushback_rate` is a **secondary** metric, reported **per judge only and never pooled**, with a standing caveat that the cross-judge stability of the underlying `pushback_with_alternative` state is untested and that all earlier figures for it are single-judge. Judge-B's `pushback_rate` was computed by importing the project's own `_break_turn_item` helper rather than by a parallel reimplementation, so both judges' figures come from **identical code on an identical item base** — again leaving the judge as the only variable.

### 4.2 The variance decomposition

The ordering-flip test returns a binary verdict per design. It establishes judge-sensitivity qualitatively but says nothing about *how much* of what the instrument reports is attributable to the judge rather than to the model. Because three epochs were run, that quantity is recoverable from data already on disk at no additional cost, fully offline.

The design is a balanced **5 (system under test) × 2 (judge)** layout with the **three epochs as replicates**, fitted per design on that design's reported headline metric:

```
SS_total (df 29) = SS_SUT (4) + SS_judge (1) + SS_SUT×judge (4) + SS_error (20)
```

Each term answers a distinct question:

| Term | Question it answers |
|---|---|
| **SUT** | Do the models differ at all? |
| **judge** | Do the judges differ in overall severity — a level shift? |
| **SUT × judge** | **Do the judges disagree about which model is better?** |
| **error** | Epoch-to-epoch stochastic noise |

The methodological point that justifies the epoch budget is explicit: **using epochs as replication is what makes the interaction estimable separately from error.** Without replication, `SUT × judge` — the term that actually voids comparative claims — is confounded into the residual, and the judge's footprint is understated. A single-epoch two-judge run can report a judge main effect but cannot separate the interaction from noise, which means it cannot measure the quantity that decides whether a leaderboard is admissible.

The decomposition carries a **built-in correctness check**. Design 05's primary metric is judge-free (§3.4), so its `judge` and `SUT × judge` terms must be exactly zero. They are: **0.000000 and 0.000000**. This validates the decomposition arithmetic on real data rather than on a simulation. It does not by itself license any claim about the other designs: a control whose true value is zero exercises only the null path. The separate conclusion that nonzero judge effects elsewhere are not rescore-pipeline artefacts rests on a different observation — design 05's judge-A and judge-B headline cells are identical to four decimal places on all five systems (§5.4).

Two constraints travel with every figure the decomposition produces. It decomposes variance in the **reported headline** — one value per system × judge × epoch cell — not in per-item scores. And it uses **two judges only**: the judge main effect is a one-degree-of-freedom contrast, not an estimate of a judge population, and may not be read as "judges in general account for X%". Design 05 (zero by construction) and the floor-saturated design 07 are excluded from cross-design summaries; including design 05 would bias the judge medians downward.

### 4.3 The $0 two-referee meta-audit

**Provenance and comparability — read before §5.6.** Unlike the swap test and the variance
decomposition, the referee meta-audit was **not** run over the full-bank administration
reported in §5.1–§5.5. It was run over the earlier 2026-07-16 pilot logs, at the prior bank
revision. Under C9 it is therefore a **separate comparability line**, and its stratum
denominators are pilot-run turn counts — 815 judgeable turns on design 07 and 1,610 on
design 02 — not the full-bank counts that appear in the §5.6 agreement table. Where §5.6
converges with the decomposition, that convergence is across two *runs at different bank
revisions*, which is a weaker form of corroboration than two analyses of one dataset and is
reported as such.

The first two methods measure *that* the judges disagree and *how much*. Neither can say which judge is diverging, or whether the disagreement is a judge property at all rather than a property of the rubric. That question cannot be answered from inside the judge pair: two raters who disagree are symmetric evidence about each other, and there is no third vantage point.

The meta-audit supplies a third vantage point deliberately and provisionally, and the epistemics are stated up front rather than in a closing caveat: **this is reference-model concordance, not ground truth.** The referees are stronger models, not oracles. A referee siding with one judge is evidence about *judge character* — which judge diverges, and in which direction — and never proof that the judge is correct. Two referees agreeing may share correlated error from similar training regimes, so referee-to-referee agreement is *consensus* evidence, not *correctness* evidence. No result in this paper claims a referee proves a judge right.

**Frozen, disagreement-enriched sample.** The audit runs on a single pre-committed manifest of **942 units**, frozen before any referee dispatch, with a recorded manifest hash, a fixed seed, and a fixed draw order; the manifest is the population, and no units were added after the first dispatch. The strata are:

| Design | Stratum | n |
|---|---|---:|
| 07 | disagreement | 392 |
| 07 | control | 150 |
| 02 | disagreement | 200 |
| 02 | control | 80 |
| 06 | gap | 60 |
| 06 | control | 60 |
| **Total** | | **942** |

Disagreement on designs 02 and 07 is defined as judge-A state ≠ judge-B state at the same positional turn, with `unscorable` counting as a state. Design 06 has no state taxonomy, so its contested stratum is the top 60 units by absolute divergence between the two judges' profile means.

**Disagreement enrichment, and why it forbids a pooled headline.** The sample deliberately over-represents units on which the two shipped judges already disagreed: on design 07 it takes *all* disagreement turns, and on designs 02 and 07 the contested strata are sampled at rates unrelated to their population base rates. The sample's composition is therefore an artifact of the sampling design, not of the instrument. Any pooled "overall agreement" figure computed across these strata would be a weighted average whose weights were chosen by the sampler, and would move arbitrarily with the enrichment ratio. **Agreement is therefore reported per design and per stratum, never pooled**, and no overall-agreement headline is reportable without the per-stratum split adjacent. This constraint binds §5 and every downstream use.

**Blindness.** Referee prompts were exported **byte-identical to the shipped judge prompts** by reusing the project's own prompt-assembly function rather than forking it; export determinism was verified across two runs, and each row carries a prompt hash. Referees received only `{prompt_hash, prompt}` slices — never judge-A or judge-B verdicts, never system-under-test identities, never repository paths. Batches were ladder-spread so that no two turns of one conversation shared a batch.

**Two independent referee channels, both at $0 metered spend.** Arm 1 dispatched a **Claude Opus** referee through a subscription agent channel: 40 dispatches, 942/942 verdicts ingested, 0 hash rejects, 0 refusals, 0 hand-patched verdicts, $0 API spend. Arm 2 dispatched **GPT-5.6-Sol** through a command-line exec channel over the *same* frozen manifest with no new sampling, hardened for blindness — a working directory outside the repository, network access disabled, tool servers disabled, ephemeral sessions against cross-batch contamination, reading only the batch slices and writing only verdict files: 39 batch dispatches, 942/942 accepted on the first pass, 0 re-asks, 0 refusals, 0 hash rejects, $0 API spend. The cross-vendor, cross-channel construction is deliberate; it is also why any referee-versus-judge difference composes a channel effect with a model effect. Each referee scored each unit once, so within-referee noise is unmeasured, and roughly two dozen units share one agent context per batch, so within-batch non-independence applies to both arms.

### 4.4 Governing rules

Four standing rules govern every number reported in §5 and are stated here so that the results section can be read without re-deriving them.

- **R3 — interval language only.** Estimates are reported as point estimates with intervals; the language is "excludes zero" or "crosses zero". No significance testing is performed, the word "significant" is not used as an adjective, and no significance markers appear in any table.
- **R4 — the two-judge precondition.** A comparative claim must hold in the same direction under judge-A and judge-B. A direction flip is reported as *judge-sensitive — no system claim*. A related same-family exclusion rule applies where a system under test and a judge share a model family; such cells lean on the other judge explicitly.
- **C6 — no cross-classifier pooling, ever.** The branch classifier for designs 02 and 07 is part of the instrument, pinned by model slug, provider, prompt-template hash, and route policy. A classifier change is an instrument change, and cells scored under different pinned classifiers are not comparable and are never pooled. For this lineage the **classifier is pinned at `gpt-4.1-nano`**.
- **C9 — first-use and comparability fences.** Results are fenced to bank revision 2026-07-24b, public bank only, holdout untouched. Cells produced under earlier bank revisions, under the pre-anchor design-08 judge rubric, or under a different classifier pin are separate comparability lines and are not merged. Pre-registered comparison families are declared before first use of the data they govern.

Finally, two scope statements. WALKWORTHY v2 is a **parallel** harness established by ruling; version 1 remains canonical for release evidence, and nothing here is a release claim. And the offline judge-level analyses reported in §5 are read at the **instrument level and judge level only** — they support no comparative reading between systems under test.

---

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content

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

**The criterion, stated exactly.** A cell reads "flips" if and only if the full five-way
permutation of unrounded point estimates differs between the two judges — exact permutation
equality, stable-sort tie-break, no intervals; the swap tool's own section header calls this
the *"naive point-estimate order."* The binary verdict is retained because pre-registered rule
R4 is written in its terms, but it is blunt: a single adjacent transposition counts as a full
flip, and ties are broken by input order. Each cell therefore also carries a graded verdict,
Kendall's τ (τ_a = (C − D)/10 over the ten system pairs) between the two judges' orderings,
with ᵗ flagging cells where either judge assigns tied scores — 10 of the 27 judged
design-epochs, in which the binary verdict is partly arbitrary.

| design | ep1 | ep2 | ep3 | verdict |
|---|:--:|:--:|:--:|---|
| 01 goodsamaritan | flips (τ +0.60) | flips (τ 0.00) | flips (τ +0.40) | judge-sensitive (all epochs) |
| 02 twomasters | flips (τ −0.30 ᵗ) | flips (τ −0.60) | flips (τ −0.20) | judge-sensitive (all epochs); the orderings anti-correlate |
| 03 quiettongue | flips (τ +0.20) | flips (τ +0.20) | STABLE (τ +0.70 ᵗ) | stability not reproducible |
| 04 innerweight | flips (τ +0.20 ᵗ) | STABLE (τ +1.00) | flips (τ +0.70 ᵗ) | stability not reproducible |
| 05 ordoamoris | STABLE (τ +1.00) | STABLE (τ +1.00) | STABLE (τ +1.00) | stable by construction (judge-free primary) |
| 06 crookedpath | flips (τ +0.80) | STABLE (τ +1.00) | STABLE (τ +1.00) | stability not reproducible; the lone flip is a single adjacent transposition |
| 07 seventyseven ▲ | — | — | — | **ordering undefined** (floor-saturated; judge-A is 0.000 on all five systems in ep1/ep2) |
| 08 vocationfork | flips (τ 0.00) | flips (τ −0.20) | flips (τ +0.80) | judge-sensitive (all epochs) |
| 09 doubleedge | flips (τ +0.20) | flips (τ +0.60) | flips (τ −0.10 ᵗ) | judge-sensitive (all epochs); ep3 tie-affected |
| 10 strangergate | flips (τ +0.10 ᵗ) | flips (τ −0.10 ᵗ) | flips (τ −0.20) | judge-sensitive (all epochs) |

ᵗ tie-affected: at least one pair of systems receives equal scores from a judge in that cell
(e.g. design 09 epoch 3, where judge-A scores deepseek = gemini = 0.8235). A STABLE cell can
carry τ < +1.00 when tied pairs sort identically under both judges (design 03 epoch 3).

**Eight of the nine judged designs flip.** Design 07 is excluded from this count: it is floor-saturated, its judge-A headline is 0.000 on all five systems in epochs 1 and 2, and it therefore has no ordering to preserve or permute — the tool's recorded flip there is a stable-sort tie-break artefact, not a disagreement. The one judged design that never flips is design 05, and it is the one
design whose primary metric never reaches a judge at all: its constraint-satisfaction rate is
computed from a parsed allocation against keyed constraints.

Graded, the picture is heterogeneous rather than uniform. Design 02's orderings genuinely
anti-correlate in all three epochs (τ −0.60 to −0.20); designs 01 and 08 reach τ ≈ 0 in at
least one epoch. At the other end, design 06's flip status rests entirely on epoch 1's single
adjacent transposition (τ +0.80; epochs 2 and 3 are identical orderings, τ +1.00), and design
09's epoch 3 verdict is tie-affected. The binary count is honest but flattens this range, which
is why τ accompanies it wherever the flip result is reported. No chance rate is quoted for the
binary test: the two judges score the same stored transcripts, so their orderings are
correlated by construction and no calibrated null is available — a further reason to read the
graded verdict alongside the binary one.

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
1 and 3 and is stable in epoch 2; design 06 flips in epoch 1 and is stable in epochs 2 and 3
(graded, the weakest instability of the three: that lone flip is a single adjacent
transposition, τ +0.80, against identical orderings in the other two epochs).
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

**The reference line.** Sums of squares are non-negative, and under a null of no effect their
expectations are proportional to degrees of freedom: with `SS_total (df 29) = SS_SUT (4) +
SS_judge (1) + SS_SUT×judge (4) + SS_error (20)`, the no-effect expectations of the shares are
**13.79%** (SUT), 3.45% (judge), **13.79%** (SUT × judge) and 68.97% (error). This line is a
descriptive expectation, not a test — no p-value or rejection decision attaches to it — but
shares must be read against it, because a share at or below its line is no larger than what
pure epoch noise produces.

Across the eight judged, non-saturated designs (01, 02, 03, 04, 06, 08, 09, 10):

| component | median | range | E[share] under no effect |
|---|---:|---|---:|
| SUT (do the models differ) | 35.6% | 5.8–63.4% | 13.79% |
| judge (severity shift) | 20.5% | 2.9–88.8% | 3.45% |
| SUT × judge (which model is better) | 17.2% | 1.4–46.5% | 13.79% |
| error (epoch noise) | 19.1% | 0.9–48.3% | 68.97% |

Judge footprint (main effect plus interaction) has median **35.3%**; system footprint has
median **35.6%**; the ratio is **1.0×**. The judge footprint exceeds the system footprint in
**4 of 8** designs.

**This does not say that the judge overwhelms the model, and the paper does not claim it.**
Judge and system footprints are comparable at the median, and the system main effect is the
single largest term in several designs — 63.4% on design 06, 54.4% on design 09, 46.3% on
design 04, 45.4% on design 01. **The models genuinely differ on most designs** — but the
signal is design-specific rather than suite-wide: the system share sits below its own 13.79%
reference line in designs 02 (5.8%), 03 (6.6%) and 08 (9.1%). A reading of these results as
"the measurement is only about the judge" misstates them; so does a reading that the models
separate everywhere.

The decision-relevant term is the **interaction**, not the main-effect ratio. A large system
main effect says the models differ; it does not license a *ranking* if the judges disagree
about the order. That disagreement is exactly `SUT × judge`. Read against its 13.79%
reference line it is clearly above the line in four judged designs (02, 08, 10, 01) and at or
below it — no larger than pure epoch noise produces — in the other four (06, 09, 04, 03). We
do not report the term as "non-zero in 8 of 8 designs": a sum of squares on a continuous
metric is almost surely non-zero, so that statement carries no information.

| design | SUT×judge | vs 13.79% | SUT | note |
|---|---:|:--:|---:|---|
| 02 | 46.5% | above | 5.8% | judge disagreement swamps a near-absent model signal |
| 07 ▲ | 33.9% | — | 24.5% | floor-saturated; listed for completeness only |
| 08 | 25.9% | above | 9.1% | the covert-protection boundary, quantified |
| 10 | 25.8% | above | 25.8% | interaction equals the model effect |
| 01 | 23.0% | above | 45.4% | large system effect, judges still reorder it — the only exemplar clearly above the line |
| 06 | 11.4% | **below** | 63.4% | interaction within epoch noise; its R4 failure rests on the flip verdict — one adjacent transposition (§5.2) |
| 09 | 9.9% | **below** | 54.4% | interaction within epoch noise; its R4 failure rests on the flip verdict — tie-affected in ep3 (§5.2) |
| 04 | 4.9% | **below** | 46.3% | smallest interaction among the judged designs |
| 03 | 1.4% | **below** | 6.6% | interaction small because the judge *level* shift is 88.8% |

**The precise claim the data support:** *the models differ on most designs. On a minority of
designs the judges clearly disagree about the ordering; on the rest the systems are too
tightly spaced for either judge to resolve. Either way, no comparative claim survives the
swap.* Design 01 is the sharpest single illustration of the first arm — a large genuine model
effect (45.4%) carrying an interaction clearly above the reference line (23.0%) that permutes
the ranking in every epoch. Designs 06 and 09, cited alongside it in an earlier report of
this analysis, do not support that mechanistic reading: their interaction shares sit below
the reference line, and their R4 failures rest on the graded flip verdicts of §5.2 — one
adjacent transposition, and a tie-affected cell — which is the signature of systems too
tightly spaced to resolve, not of judges in resolvable disagreement. Both routes void a
ranking; they void it for different reasons, and the repair each calls for differs (a better
judge could in principle help design 02; only harder separation between systems helps 06 and
09).

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

**The positive control's own main effect sits at its null expectation.** Because design 05 is
judge-free, its two judge levels are exact duplicates and the layout collapses to 5 systems ×
3 epochs — `SS_total (df 14) = SS_SUT (4) + SS_error (10)` — so the no-effect expectation of
its system share is 4/14 = **28.6%**. The observed share is **27.4%**. The one surface where
a ranking could have been claimed shows a system main effect indistinguishable from what pure
epoch noise produces, independently corroborating the contrast result above: the judge-free
surface genuinely does not separate these five systems, and no concealed ranking is being
obscured by judge noise.

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

---

## 6 Limitations and non-claims

**No system rankings are made or implied.** This paper reports no leaderboard. Every per-cell
figure it carries is a descriptive instrument reading, and the run's own governing conclusion
is that no system-versus-system comparative claim is supported anywhere in this suite on this
data. Readers should not reconstruct an ordering from the descriptive tables; the entire point
of the analysis is that such an ordering would not reproduce under a different judge.

**Two judges only.** The judge main effect is a one-degree-of-freedom contrast between judge-A
(`gpt-4.1-nano`) and judge-B (`llama-3.3-70b-instruct`). It is not an estimate drawn from a
population of judges, and none of the percentages here may be read as "judges in general
account for X% of the variance." A different pair could yield a different footprint; whether
the swap instability is a pairwise property or a genuine multi-judge fan-out is not decidable
from two judges.

**The decomposition is of headline variance, not item variance.** It decomposes variance in
the *reported headline* — one value per system × judge × epoch cell — and not variance in
per-item scores. Item-level heterogeneity is invisible to it.

**It is descriptive.** No hypothesis test is performed on the variance components and no
significance language is used anywhere in this paper. Interval statements are phrased as
"excludes zero" or "crosses zero."

**Two designs are special cases and are excluded from the summary medians rather than folded
in.** The judge-free design's judge and interaction terms are zero *by construction*, and the
pastoral-arc design is floor-saturated, so its percentages describe noise around a floor. A
floor cannot exhibit an interaction. Including the judge-free design would bias the judge
medians downward — an error an earlier draft of the analysis made before correction.

**Referee consensus is concordance, not truth.** The referee arms establish that two
independent stronger references converge on a reading; they do not certify any shipped judge
as correct. "Both referees side with judge-B" is evidence about judge-A's character, not a
proof that judge-B is right. Two referees may share correlated error inherited from similar
training regimes, and neither is an oracle.

**The referee sample is disagreement-enriched by construction, and strata are never pooled.**
Any single "overall referee agreement" headline would be invalid. All referee agreement
figures are reported within stratum and within design, and must not be pooled downstream.

**Five systems under test, all cheap-tier.** All conclusions are scoped to that tier. Both the
floor saturation and the closely-spaced headline cells that make a modest interaction
sufficient to permute an ordering are tier properties, and neither is known to hold above it.

**The classifier is pinned.** Branch classification is pinned at `gpt-4.1-nano` for this
lineage, with a documented cross-family disagreement property already on record for it. Under
the project's no-cross-classifier-pooling rule, cells produced under this pin may never be
pooled with cells produced under any future cross-family pin; those would be different
experiments, not additional data.

**Reporting-surface discipline on the consistency design.** For that design `break_turn` is
the sole headline. Its `pushback_rate` is reported only as a secondary, per-judge measure,
never pooled across judges, and carries a standing caveat that the cross-judge stability of
its underlying state is untested.

**Corpus scope.** The registry is a named fifteen-work, Protestant-Reformed-dominant corpus;
direct Scripture anchoring is disallowed by construction. Nothing here generalizes to
"Christian ethics" as such, and no theological or religious-authority claim is made.

**Withheld material.** A stratified 158-item holdout is withheld from all public surfaces and
was not touched by this work; no holdout content or identifiers appear anywhere in this paper.

---

---

## 7 Future work

**A third judge.** The single most informative next measurement is a third scoring judge from
a third model family. Two judges can establish that an ordering is unstable; they cannot
distinguish pairwise noise between two idiosyncratic instruments from a genuine multi-judge
fan-out in which every judge imposes its own ordering. A third judge also converts the
one-degree-of-freedom judge contrast into something with the beginnings of a population
interpretation.

**Three or more epochs as a standing budget requirement.** This run's own methodological
finding is that single-epoch judge-stability verdicts are unreliable: three designs read
stable in some epochs and judge-sensitive in others. We therefore propose ≥3 epochs as a
precondition for any stability claim, alongside the two-judge pass — and note that epochs are
what make the interaction estimable separately from residual error at all. Without
replication, the term that actually voids comparative claims is confounded into the residual
and the judge's footprint is understated.

**Harder systems under test.** The pastoral-arc design is floor-saturated at this tier, and a
floor cannot exhibit an interaction; its variance percentages describe noise. A frontier
roster is required before that design can contribute anything to a judge-sensitivity analysis,
and before the benchmark's difficulty calibration can be assessed at all.

**Instrument repair before more measurement.** The most judge-fragile design in the suite
(exact primary-field agreement between judges of 0.232, with an interaction of 46.5% sitting
on a system main effect of 5.8%) is a taxonomy problem, not a judge-quality problem. The
earlier two-referee work bears directly on this point: on that design's disagreement stratum both
shipped judges diverge from the referee consensus, agreeing with either referee at only
0.23–0.27 while the referees agree with each other at 0.735. Substituting a stronger judge
will therefore not repair it. The indicated work is revising the state taxonomy and authoring
keyed text for the three defect items, and only then re-measuring. Spending further
measurement budget before the instrument is repaired buys precision on a quantity whose
definition is contested.

**A human-adjudicated gold slice.** Referee consensus is the method's ceiling and also its
weakest link. A modest human-adjudicated slice — targeted at the both-referees-say-neither
units on the taxonomy-contested design — would test whether referee consensus tracks a
defensible human reading, and would give the concordance framing an external anchor without
requiring human coding at scale.

**A within-vendor, cross-channel decomposition.** The two referee arms differ in both model
and dispatch channel. Separating model effect from channel effect — the same reference model
run through two different channels, and two reference models run through the same channel —
would establish how much of the referee-referee agreement is a property of the models and how
much is a property of how they were invoked. Both current arms are also single-pass; a
self-consistency replicate per referee would bound each referee's own instability before its
verdicts are used to adjudicate anyone else's.

**Self-consistency and decode stability.** Finally, the judge swap and the referee arms both
sit on stochastic decodes. A fixed-decode replication, and a seed-stability probe on the
designs whose epoch-noise share is largest, would separate judge disagreement from decode
variance in the residual.

---

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content

---

## Provisional reference list

*v0.1. Every entry below was verified against a file in the project literature vault at drafting time, and the vault path is retained so each citation can be re-checked. Bibliographic details are to be reconciled against the canonical records before submission: several vault filenames carry an author token that disagrees with the work's printed byline, so a bibliography build must resolve against the documents themselves rather than against filenames. Topics marked `[CITATION NEEDED]` in §2 are genuine gaps, not omissions — the drafting pass was deliberately confined to the vault.*

Every citation appearing in §2 above, with the vault file it was read from. No citation appears
in the text that is absent from this table.

| Cited as | Vault source file |
|---|---|
| Zheng et al. (2023), *Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena* | `CEI-Lit-WS/RELIGIOUS-VALUES/BACKGROUND/EXTRACT/2023-Zheng-Judging Llm Judge With.md` |
| Gu et al. (2024), *A Survey on LLM-as-a-Judge* | `CEI-Lit-WS/papers/2024-Gu-A Survey on LLM-as-a-Judge.md` |
| Shi et al. (2025), *A Systematic Study of Position Bias in LLM-as-a-Judge* | `CEI-Lit-WS/papers/2025-Shi-A Systematic Study of Position Bias in LLM-as-a-Judge.md` |
| Wataoka et al. (2024), *Self-Preference Bias in LLM-as-a-Judge* | `CEI-Lit-WS/papers/2024-Wataoka-Self-Preference Bias in LLM-as-a-Judge.md` |
| Koo et al. (2023), *CoBBLEr: Assessing the Cognitive Bias of LLMs as Evaluators* — note: this vault file's `Metadata` block lists "Guo, X.; Zhang, B.; …" while its `Authors` block lists Koo, Lee, Raheja, Park, Kim, Kang; the author line should be verified against the arXiv record before submission | `CEI-Lit-WS/papers/2023-Guo-COBBLER.md` |
| Son et al. (2024a), *LLM-as-a-Judge & Reward Model: What They Can and Cannot Do* (KUDGE) | `CEI-Lit-WS/papers/2024-Son-LLM-as-a-Judge & Reward Model What They Can and Cannot Do.md` |
| Son et al. (2024b), *MM-Eval: A Multilingual Meta-Evaluation Benchmark for LLM-as-a-Judge and Reward Models* | `CEI-Lit-WS/papers/2024-Son-MM-Eval A Multilingual Meta-Evaluation Benchmark for LLM-as-a-Judge.md` |
| Faisal et al. (2024), *Dialectal Toxicity Detection: Evaluating LLM-as-a-Judge Consistency Across Language Varieties* | `CEI-Lit-WS/papers/2024-Faisal-Dialectal Toxicity Detection Evaluating LLM-as-a-Judge Consistency.md` |
| Beyer et al. (2025), *LLM-Safety Evaluations Lack Robustness* | `CEI-Lit-WS/papers/2025-Beyer-LLM-Safety Evaluations Lack Robustness.md` |
| Aroyo et al. (2023), *DICES: Diversity in Conversational AI Evaluation for Safety* | `CEI-Lit-WS/papers/2023-Aroyo-DICES Dataset.md` |
| Baan et al. (2022), *Stop Measuring Calibration When Humans Disagree* | `CEI-Lit-WS/papers/2022-Baan-Stop Measuring Calibration When Humans Disagree.md` |
| Gehrmann, Clark and Sellam (2022), *Repairing the Cracked Foundation* | `CEI-Lit-WS/RELIGIOUS-VALUES/BACKGROUND/EXTRACT/2022-Gehrmann-Repairing The Cracked Foundation.md` |
| Raji et al. (2021), *AI and the Everything in the Whole Wide World Benchmark* | `CEI-Lit-WS/RELIGIOUS-VALUES/BACKGROUND/EXTRACT/2021-Raji-Ai And The Everything.md` |
| Schlangen (2021), *Targeting the Benchmark: On Methodology in Current NLP Research* | `CEI-Lit-WS/RELIGIOUS-VALUES/BACKGROUND/EXTRACT/2021-Schlangen-Targeting The Benchmark Methodology.md` |
| Bean et al. (2024), *Measuring What Matters: Construct Validity in LLM Benchmarks* | `CEI-Lit-WS/papers/2024-Bean-Measuring What Matters - Construct Validity in LLM Benchmarks.md` |
| Eriksson et al. (2025), *Can We Trust AI Benchmarks? An Interdisciplinary Review* | `CEI-Lit-WS/papers/2025-Eriksson-Can We Trust AI Benchmarks An Interdisciplinary Review.md` |
| Ye et al. (2025), *Large Language Model Psychometrics* | `CEI-Lit-WS/papers/2025-Ye-Large Language Model Psychometrics.md` |
| Jiang et al. (2025), *Raising the Bar* (GETA) | `CEI-Lit-WS/papers/2025-Jiang-Raising the Bar.md` |
| LaCroix and Luccioni (2025), *Metaethical perspectives on 'benchmarking' AI ethics* | `CEI-Lit-WS/papers/2025-LaCroix-Metaethical perspectives on ‘benchmarking’ AI.md` |
| Elasky et al. (2026), *Debate Helps Weak Judges* | `CEI-Lit-WS/papers/2026-Elasky-Debate Helps Weak Judges Reward.md` |

**Duplicate-source note.** Two of the works above also have near-duplicate vault entries under
different first-author strings — construct validity in LLM benchmarks appears additionally at
`CEI-Lit-WS/RELIGIOUS-VALUES/BACKGROUND/EXTRACT/2025-Li-Measuring What Matters Construct.md`,
and LLM psychometrics additionally at
`CEI-Lit-WS/RELIGIOUS-VALUES/BACKGROUND/EXTRACT/2025-Gupta-Large Language Model Psychometrics.md`.
The `papers/` entries are used as canonical here; the author lines should be reconciled once
before the reference list is finalised.

**Open gap markers left in this part (5):** foundational chance-corrected agreement statistics;
the κ prevalence/base-rate paradox; generalizability theory / variance-component reliability;
panels or juries of LLM judges; the substitution and cost-barrier literature motivating cheap
judge pipelines.

---

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content

---


**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content
