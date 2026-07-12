<!-- WCFBENCH-CANARY-c1647-x9k4q -->
# 1. Introduction

## 1.1 The steerability problem

A recurring demand on modern language models is not that they be good in the abstract,
but that they *represent a specified normative framework on request* — the values of a
particular deployer, community, jurisdiction, or tradition. This is the ambition behind
pluralistic-alignment research: rather than encoding a single global ethic and treating
every deviation from it as misalignment, a model should be *steerable* toward a declared
value system and evaluated on how faithfully it inhabits that system. Steerability of this
kind is only as meaningful as our ability to *measure* it. If a model is told to reason
and act within a stated framework, can its accord with that framework be assessed rigorously,
or must we fall back on the diffuse, annotator-averaged, majority-proxy notions of
"helpfulness" and "harmlessness" that dominate current alignment evaluation? The
methodological question this paper addresses is narrow and concrete: **given a fully
specified normative framework, can a model's conduct and counsel be measured against it
with construct validity — and can we know when such a measurement is trustworthy enough
to report?**

Most existing values-and-ethics benchmarks answer an easier question. They elicit moral
*opinions* against a target that is itself contested: labels are drawn from annotator
majorities, the "correct" answer shifts with the annotator pool, and a high score is quietly
read as evidence that a model "is ethical." Such instruments are simultaneously (a)
under-specified in their construct — whose ethics, codified where? — and (b) prone to
saturation and capability-correlation, because a smart model that can pattern-match consensus
opinion scores well without any behavioral commitment. Steerability toward a *declared*
framework needs the opposite: a target that is fixed independently of the model and the
annotator, so that accord is a property of the model's behavior rather than of the labeling
process.

## 1.2 Why a confessional standard is a strong test case

We take as our declared framework the **Westminster Standards** — the Westminster Confession
of Faith together with the Larger and Shorter Catechisms (1647). This is a deliberate choice
of test bed, not an endorsement, and it is chosen for properties that make it an unusually
demanding and clean instrument for the measurement problem above:

- **It is fixed.** The text has been stable for centuries. There is no moving target, no
  drift in the "gold" standard between evaluation rounds, and no need to reconstruct the
  norm from a fresh annotator survey each time the benchmark is run.
- **It is internally coherent and extensively documented.** The tradition has already done
  the operationalization work that most values benchmarks improvise. The Larger Catechism's
  exposition of the Decalogue (Q98–148) is a *graded casuistic system*: for each commandment
  it enumerates the duties required and the sins forbidden, supplies eight interpretive rules
  for reading the commandments (Q99), a four-headed calculus of what makes some sins more
  heinous than others (Q151), and a triaxial theory of right action — right in *matter*,
  *manner*, and *end* (WCF 16.7) — every element attached to proof texts. This is a ready-made,
  source-verifiable scoring ontology, granular enough to key individual rubric points to
  specific clauses.
- **It resolves to specific clauses, not vibes.** Because every gold label can be traced to
  a named anchor in the Standards, the target does not depend on an annotator majority. Where
  the Standards are silent, or where confessionally competent interpreters genuinely differ,
  the correct response is calibrated abstention ("the Standards leave this free / this is
  disputed"), and such items are flagged and scored accordingly rather than forced to a
  spurious label.

The point is methodological. A fully specified confession lets us isolate the measurement
problem from the labeling problem: because the norm is external, fixed, and clause-addressable,
any residual difficulty in scoring is attributable to the *measurement mechanism* and the
*judge*, not to disagreement about what the right answer is. That is precisely the setting in
which a steerability benchmark can be validated.

## 1.3 Construct disclosure

We state the construct exactly and without softening. **WCF-Bench measures the degree to
which a model's conduct and counsel accord with the ethical teaching of the Westminster
Standards (Confession of Faith, Larger Catechism, Shorter Catechism, 1647), as stated in
those documents.**

This is **not** a claim that a high-scoring model "is ethical" simpliciter, and it is not a
measure of generic religiosity. The normative population is stipulated: confessional Reformed
Christianity as codified at Westminster. A high WCF-Bench score is a statement of *accord with
a declared standard*, not a certificate of moral goodness; a low score is a statement of
*discord with that standard*, not an indictment of a model's character. Westminster is not a
stand-in for "Christianity" and still less for ethics in general — items are constructed so
that they cannot be satisfied by generic moralism, and every gold label must be traceable to
a specific anchor in the Standards. Readers, deployers, and model developers should read every
number in this paper through that disclosure. The benchmark is an instrument for measuring
steerability toward one fully specified framework; it is silent on whether that framework, or
any other, ought to be steered toward.

## 1.4 Contributions

This paper makes two co-equal contributions.

1. **WCF-Bench, a construct-disclosed steerability benchmark.** A frozen bank of **230**
   anchor-keyed items across **ten method-major designs**. The suite's signature is a
   design invariant: moral content is held constant while the *measurement mechanism*
   varies, yielding a designs × commandments matrix in which each commandment is measured
   ten methodologically independent ways — a multitrait–multimethod structure that lets
   method variance be estimated explicitly rather than hoped away. The ten mechanisms are
   omission-sensitive casuistry, complicity gradients, severity discernment, fidelity under
   social pressure, expressed-versus-revealed divergence, conscience and adiaphora triage,
   proof-text discipline, repentance-and-repair trajectories, triaxial matter/manner/end
   discrimination, and obedience under incentive conflict. Every design fields two evaluation
   **tracks** — the model's *own conduct* (is it the moral agent that lies, flatters,
   equivocates, or keeps its commitments?) and its *advisory fidelity* (does its counsel to
   a user conform in matter, manner, and end?) — and the divergence between the two is itself
   a reported metric. A **tier ladder** runs from recognition through applied open-response,
   multi-turn adversarial pressure, and agentic incentive conflict, with the *drop* between
   tiers, never a single absolute score, as the headline. Scoring is decomposed into
   anchor-keyed rubric keypoints rather than holistic ratings, and a mandatory perturbation
   battery (paraphrase, option order, persona/framing, pushback, register, monitoring-frame)
   turns invariance into a first-class, scored property.

2. **A reusable validity template for judge-scored benchmarks.** WCF-Bench is built with, and
   this paper documents in full, machinery that treats validity as the primary deliverable:
   a **judge-qualification protocol** (a fixed battery, re-qualification triggers, an escalation
   ladder, drop rules, and a cross-family judge panel to defeat single-family bias);
   **parser-artifact forensics** as a first-class validity activity, in which apparent "model
   disagreement" is decomposed into harness artifacts and diagnosed by counterfactual re-parse
   before any substantive conclusion is drawn; a disciplined **adjudication protocol** that
   separates *computing* results from *adjudicating* and *ratifying* them; and a set of
   **pre-registered release gates** whose thresholds and computations are frozen before the
   data exist. We present this machinery as a template that other declared-norm benchmarks can
   adopt independently of the Westminster construct.

## 1.5 A validity-first stance

The two contributions are not sequential — measure first, validate later — but interlocked.
The distinctive commitment of this work is that **the validity checks decide whether any
results table is released at all.** Before the evaluation was run, we pre-registered a battery
of gates: capability-correlation (hard-tier scores must not be a proxy for general capability),
headroom (the best roster-frontier model must not ceiling on the hard tier), separation (a
supermajority of frontier model pairs must be statistically distinguishable), judge validity
(agreement with a human panel against a stated ceiling), shortcut resistance (a lexical
baseline must score near chance and a fine-tune probe must fail to reach parity), human
consensus on gold labels, and per-design reliability. Each gate has a frozen threshold and a
frozen computation; a silent deviation from the pre-registration voids the affected gate. The
release rule is explicit: **the gates gate the release of the league table, not the running
of the evaluation.** A benchmark that fails its own validity gates does not publish a ranking
with caveats; it withholds the ranking and reports the failure. This inverts the usual
publish-and-caveat convention and is, in our view, the correct posture for any benchmark whose
scores could be read as a values verdict on a model.

A further methodological commitment supports this stance. In the course of construction we
found that measured "disagreement" among judges was, in an instructive case, an artifact of
the harness rather than a signal about the models — a score-extraction parsing bug and a
false-firing willingness veto that tripped whenever a judge dutifully quoted a refusal
fixture. Diagnosing these artifacts by counterfactual re-parse, and only then re-reading the
underlying evidence, materially changed the picture. We elevate this kind of forensic work
from an incidental fix to a documented validity method, because judge-scored benchmarks are
exactly where such artifacts hide.

## 1.6 Paper map

The remainder of the paper is organized as follows. **Section 2 (Related work)** situates
WCF-Bench against four strands: pluralistic alignment and steerability toward declared value
systems, values-and-ethics benchmarks for language models, the validity literature on
LLM-as-judge evaluation, and benchmark contamination together with canary and do-not-train
defenses. **Section 3 (Benchmark design)** presents the construct and anchor registry, the
230-item bank, the ten method-major designs, the tier ladder and two tracks, the scorer
kinds, the perturbation battery, and the contamination defenses. **Section 4 (Validity
methodology)** develops the second contribution as a method: judge qualification,
parser-artifact forensics as a worked case study, the adjudication protocol, and the
pre-registered release gates. **Section 5 (Experimental setup)** transcribes the
pre-registration — the system-under-test roster and its anti-leakage exclusions, the judge
panel of record, the fixed seed, the perturbation scope, the budget ceiling, and the frozen
gate computations — and states explicitly that it was written before the run. **Section 6
(Results)** reports the gate outcomes and, conditionally on the gates passing, the league
tables and perturbation, agreement, and cost summaries, each carrying its validity labels.
**Section 7 (Discussion)** interprets the outcomes gate by gate and draws the general lessons
for judge-scored benchmarks. **Sections 8 and 9 (Limitations and Ethics & release)** state the
scope bounds, the single-judge-family and holdout-withholding disclosures, and the release
posture for the bank and harness.
