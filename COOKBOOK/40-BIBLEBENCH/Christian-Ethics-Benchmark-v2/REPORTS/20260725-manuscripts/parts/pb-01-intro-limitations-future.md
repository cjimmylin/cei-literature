**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content

> **PART FILE — assembles into paper (b).** §2 related work and §3–§5 are drafted separately.
> Target paper: *Judging the Judges for $0: A Two-Referee Concordance Method for Localizing
> LLM-as-Judge Failure on Value-Laden Rubrics.* Venue-generic and author-generic by ruling.

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
judge main effect, their interaction, and epoch noise. Across the eight judged, non-saturated
designs the judge footprint (main effect plus interaction) has median 35.3% and the system
footprint median 35.6% — a ratio of 1.0×. **The models genuinely differ**, and in several
designs the system main effect is the single largest term (63.4%, 54.4%, 46.3%, 45.4%). The
decision-relevant quantity is not that ratio but the interaction, the term that asks whether
the judges agree about *which* system is better. That term is non-zero in all 8 judged, non-saturated
designs, with median 17.2% and range 1.4–46.5%. The claim the data support is therefore
precise and narrow: *the models differ, but the judges disagree about the ordering in every
judged design.* An interaction of 9–23% is enough to permute the ranking of five
closely-spaced systems even where the instrument is plainly responding to the model.

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
