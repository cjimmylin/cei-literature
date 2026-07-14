# WCF-Bench — PPP-1 Assembled Manuscript Preview

> **EXPLORATORY MANUSCRIPT PREVIEW · SINGLE-JUDGE · NON-QUOTABLE**

This assembled review copy snapshots the unchanged manuscript foundation, then adds the PPP-1 preview Results, Discussion, and limitations. It does not modify the release-labeled manuscript source files.

> **EXPLORATORY MANUSCRIPT PREVIEW · SINGLE-JUDGE · NON-QUOTABLE**

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

> **EXPLORATORY MANUSCRIPT PREVIEW · SINGLE-JUDGE · NON-QUOTABLE**

<!-- WCFBENCH-CANARY-c1647-x9k4q -->
# 2. Related Work

WCF-Bench sits at the intersection of four research strands: (1) *pluralistic
alignment and steerability*, which asks whether a model can be shaped to represent a
declared value system rather than a single presumed-universal one; (2) *values and
ethics benchmarks*, which measure model moral behavior, and the smaller literature on
*religious-values evaluation*; (3) *LLM-as-judge validity*, which studies whether
model-based graders can be trusted, and how they fail; and (4) *benchmark contamination
and canary/do-not-train defenses*, which address whether a measurement survives the
possibility that the model has seen the test. We review each in turn and close each
subsection by stating precisely what WCF-Bench does that the strand does not.

## 2.1 Pluralistic alignment and steerability toward declared value systems

Much alignment research assumes a single set of human preferences that a model should
converge on. Pluralistic alignment rejects that assumption and instead asks how to
integrate diverse — and sometimes incompatible — value systems into alignment and
evaluation. Sorensen et al. (2024) offer a roadmap that formalizes three senses of
pluralism (Overton-spectrum, *steerable*, and distributional) and argues that language
models are a natural test bed for each. The *steerable* sense is the one WCF-Bench
inhabits: the question is not what a model believes by default, but whether it can be
directed to reflect a specified perspective and how faithfully it does so.

A growing benchmark literature measures this steerability directly. Miehling et al.
(2024) define *prompt steerability* formally as the degree to which a model's joint
behavioral distribution can be shifted from its baseline by persona and few-shot
prompting, and find that steerability is limited and asymmetric across persona
dimensions for current models. Meister et al. (2024) benchmark *distributional*
alignment — how well a model can be steered to match a target group's opinion
distribution — and isolate the question domain, steering method, and distribution-
expression method as decisive variables. Both build on Santurkar et al. (2023), whose
OpinionQA showed substantial baseline misalignment between model-reflected opinions and
those of specified U.S. demographic groups. The steerability toolkit itself descends in
part from methods like Constitutional AI (Bai et al. 2022), which conditions model
behavior on an explicit, natural-language set of principles rather than on aggregated
human preference labels alone.

*Differentiation.* These works steer toward demographic distributions, personas, or
short principle lists, and measure how far the behavioral distribution moves. WCF-Bench
instead measures conduct and counsel against **one fully specified, externally fixed
confessional standard** — the Westminster Standards (1647) — with the construct
disclosed verbatim: it scores whether a response *accords with that standard*, not
whether a model "is ethical" or matches a population's opinion. The target is a
centuries-stable, internally coherent document, not a moving annotator majority, and the
normative keys are traceable to a fixed anchor registry rather than to a preference
distribution to be simulated.

## 2.2 Values and ethics benchmarks for LLMs, including religious-values evaluation

A now-large family of benchmarks probes model moral cognition and behavior. Hendrycks
et al. (2021) introduced ETHICS, spanning justice, well-being, duties, virtues, and
commonsense morality, and reported that models predict widespread human moral judgments
only partially. Scherrer et al. (2023) built MoralChoice, pairing low-ambiguity
scenarios (one clearly preferred action) with high-ambiguity dilemmas and introducing a
statistical method to read out the moral beliefs a model encodes — finding models align
with common sense on clear cases but grow uncertain on ambiguous ones. A parallel line
studies *social bias* as a values-adjacent property: Parrish et al. (2022) built BBQ, a
hand-constructed question-answering bias benchmark whose nine social dimensions include
religion, and showed models fall back on stereotypes under-informative contexts.

Religious-values evaluation specifically is comparatively sparse. Liu et al. (2024)
measure the spiritual values and biases encoded in LLMs, reporting that model spiritual
values are surprisingly diverse and that different value settings change sensitivity to
different target groups in downstream fairness tasks. Work in this vein tends to treat
religion either as a *bias axis* to be neutralized (BBQ-style) or as an *encoded
tendency* to be described (Liu et al. 2024), rather than as a stipulated normative
standard to be measured against.

*Differentiation.* WCF-Bench does not aggregate a commonsense or crowd majority into a
gold label, nor does it treat a religious tradition as a protected attribute to hold
models neutral over. It fixes a **single confessional standard** as the normative
population and scores behavior against it with decomposed, anchor-traceable rubrics
(triaxial matter/manner/end sub-scores), across two tracks — the model's *own conduct*
and its *advisory fidelity* — with over-refusal scored as a first-class error rather
than a safe default. Where the standard is genuinely disputed among its own interpreters,
items are excluded from gold-labeling or scored as calibrated abstentions, rather than
resolved by majority vote.

## 2.3 LLM-as-judge validity: qualification, agreement, bias, and artifact failures

Because open-ended value judgments resist mechanical scoring, benchmarks increasingly
use strong LLMs as graders. Zheng et al. (2023), introducing MT-Bench and Chatbot Arena,
established that a strong judge (e.g., GPT-4) can reach over 80% agreement with human
preferences, but catalogued the failure modes: position bias, verbosity bias, self-
enhancement (self-preference) bias, and limited reasoning. Wang et al. (2023) showed
that a pairwise judge's ranking can be *hacked* simply by reordering candidates,
demonstrating that position bias is large enough to invert conclusions, and proposed
calibration strategies to counter it. Self-preference bias — a judge favoring outputs
from its own model family — has since been isolated and quantified as a distinct effect
(Wataoka et al. 2024). These findings motivate cross-family judge panels, order
permutation, length correction, and per-criterion (rather than holistic) rubrics — all
of which WCF-Bench adopts.

A separate concern is what "agreement with humans" even means when the underlying task
is subjective. Aroyo and Welty (2015) argued that the single-ground-truth ideal is a
myth for interpretive tasks and that disagreement across annotators is signal to be
represented, not noise to be averaged away. For a confessionally scoped construct this
cuts sharply: the *identity* of the qualified rater partly determines the construct, so
judge and human-panel competence must be established rather than assumed.

*Differentiation.* WCF-Bench treats judge trustworthiness as an empirical precondition
rather than an assumption. It runs a **judge-qualification battery with explicit drop
rules** (a judge that fails qualification is removed from the panel of record, not
merely down-weighted), requires a cross-family panel with the item-generating family
barred from judging its own items, quarantines judge-scored components behind mechanical
scorers, and — as the paper's methodology contribution details — treats *parser-artifact
forensics* (distinguishing genuine judge disagreement from harness parsing failures) as
a first-class validity activity. It further reports judge–human agreement against a
qualified, confessionally literate human ceiling rather than a crowd majority.

## 2.4 Benchmark contamination and canary / do-not-train defenses

A measurement is only valid if the model has not memorized the test. Srivastava et al.
(2022), in BIG-bench, popularized the *canary GUID*: a standardized do-not-train string
embedded in every task file so that benchmark data can be filtered out of web-scraped
training corpora, with the model's log-probability on the canary itself serving as a
contamination probe. Detection methods have proliferated: Golchin and Surdeanu (2023)
propose guided-instruction completion and a GPT-4 few-shot classifier to trace whether a
model has seen specific dataset partitions, and broader surveys catalogue the space of
contamination detection and mitigation techniques (Xu et al. 2024). The consistent
lesson is that public benchmarks decay as they leak into training data, and that
canaries plus withheld splits are the standard defenses.

*Differentiation.* WCF-Bench combines several of these defenses into a single release
posture. It embeds an explicit canary/do-not-train string in every released file; it
**withholds a private holdout/refresh set** outside the public tree so leakage can be
audited by comparing public-set to holdout performance; it enforces a non-canonical
surface rule (scenario stems may not quote or closely paraphrase the standard's own
wording or famous dilemma stems, so an item cannot be solved by retrieval recognition);
and it pre-registers shortcut audits — a lexical/word-averaging baseline expected near
chance and a fine-tune probe expected to fail frontier parity — as gate conditions
rather than post-hoc checks. Contamination resistance is thus built into item
construction and release, not appended as a caveat.

## References

Aroyo, L., and Welty, C. (2015). Truth Is a Lie: Crowd Truth and the Seven Myths of
Human Annotation. *AI Magazine*, 36(1), 15–24.

Bai, Y., Kadavath, S., Kundu, S., Askell, A., et al. (2022). Constitutional AI:
Harmlessness from AI Feedback. arXiv:2212.08073.

Golchin, S., and Surdeanu, M. (2023). Time Travel in LLMs: Tracing Data Contamination in
Large Language Models. arXiv:2308.08493.

Hendrycks, D., Burns, C., Basart, S., Critch, A., Li, J., Song, D., and Steinhardt, J.
(2021). Aligning AI With Shared Human Values. *International Conference on Learning
Representations (ICLR)*. arXiv:2008.02275.

Liu, S., Zhang, Z., Yan, R., Wu, W., Yang, C., and Lu, J. (2024). Measuring Spiritual
Values and Bias of Large Language Models. arXiv:2410.11647.

Meister, N., Guestrin, C., and Hashimoto, T. (2024). Benchmarking Distributional
Alignment of Large Language Models. arXiv:2411.05403. (NAACL 2025.)

Miehling, E., Desmond, M., Ramamurthy, K. N., Daly, E. M., Varshney, K. R., Farchi, E.,
Dognin, P., Rios, J., Bouneffouf, D., Liu, M., and Sattigeri, P. (2024). Evaluating the
Prompt Steerability of Large Language Models. arXiv:2411.12405. (NAACL 2025.)

Parrish, A., Chen, A., Nangia, N., Padmakumar, V., Phang, J., Thompson, J., Htut, P. M.,
and Bowman, S. R. (2022). BBQ: A Hand-Built Bias Benchmark for Question Answering.
*Findings of ACL 2022*. arXiv:2110.08193.

Santurkar, S., Durmus, E., Ladhak, F., Lee, C., Liang, P., and Hashimoto, T. (2023).
Whose Opinions Do Language Models Reflect? *International Conference on Machine Learning
(ICML)*. arXiv:2303.17548.

Scherrer, N., Shi, C., Feder, A., and Blei, D. (2023). Evaluating the Moral Beliefs
Encoded in LLMs (MoralChoice). *NeurIPS 2023*. arXiv:2307.14324.

Sorensen, T., Moore, J., Fisher, J., Gordon, M., et al. (2024). A Roadmap to Pluralistic
Alignment. *International Conference on Machine Learning (ICML)*. arXiv:2402.05070.

Srivastava, A., Rastogi, A., Rao, A., et al. (2022). Beyond the Imitation Game:
Quantifying and Extrapolating the Capabilities of Language Models (BIG-bench).
arXiv:2206.04615.

Wang, P., Li, L., Chen, L., Cai, Z., Zhu, D., Lin, B., Cao, Y., Kong, L., Liu, Q., Liu,
T., and Sui, Z. (2023). Large Language Models are not Fair Evaluators. arXiv:2305.17926.
(ACL 2024.)

Xu, C., Guan, S., Greene, D., and Kechadi, M.-T. (2024). Benchmark Data Contamination
of Large Language Models: A Survey. arXiv:2406.04244.

Wataoka, K., Takahashi, T., and Ri, R. (2024). Self-Preference Bias in LLM-as-a-Judge.
arXiv:2410.21819.

Zheng, L., Chiang, W.-L., Sheng, Y., Zhuang, S., Wu, Z., Zhuang, Y., Lin, Z., Li, Z.,
Li, D., Xing, E. P., Zhang, H., Gonzalez, J. E., and Stoica, I. (2023). Judging
LLM-as-a-Judge with MT-Bench and Chatbot Arena. *NeurIPS 2023*. arXiv:2306.05685.

> **EXPLORATORY MANUSCRIPT PREVIEW · SINGLE-JUDGE · NON-QUOTABLE**

<!-- WCFBENCH-CANARY-c1647-x9k4q -->
<!--
Bank-composition counts in this file were verified against the frozen bank in
`05-BANK-YAML/*.yaml` on 2026-07-12 with the following commands (run from 05-BANK-YAML/):
  Total items:        grep -hE "^id:" *.yaml | wc -l                       -> 230
  Per design:         grep -hoE "^id: [A-Z]+" *.yaml | sort | uniq -c
  Per commandment:    grep -hoE "^id: [A-Z]+-C[0-9]+" *.yaml | grep -oE "C[0-9]+$" | sort | uniq -c
  Per tier:           grep -hoE "^tier: T[0-9]" *.yaml | sort | uniq -c    -> T2 111 / T3 70 / T4 49
  Per track:          grep -hoE "^track: [AB]" *.yaml | sort | uniq -c     -> A 71 / B 159
  Contested items:    grep -hE "^contested: true" *.yaml | wc -l           -> 4
  Disputed legs:      awk '/^id:/{last=$0}/^disputed: true/{print last}' *.yaml -> 4
  Perturbation labels: grep -hE "^perturbations:" *.yaml | grep -c "P3|P4|P6" -> 143 / 132 / 25
These are properties of the frozen item bank (design facts), NOT run results.
-->
# 3. Benchmark Design

WCF-Bench is a construct-disclosed benchmark that measures the degree to which a
language model's conduct and counsel *accord with the ethical teaching of the
Westminster Standards* — the Confession of Faith, Larger Catechism, and Shorter
Catechism of 1647 — as stated in those documents. This section defines that
construct precisely, describes the normative apparatus that keys every item to a
verifiable source, and lays out the frozen 230-item bank: its ten
method-major designs, its tier ladder, its two behavioral tracks, its scorer
kinds, its perturbation battery, and the contamination defenses embedded in its
release architecture. Throughout, we distinguish *design facts* — properties of
the bank that exist independently of any model being run — from measurements,
which are the subject of later sections.

## 3.1 Construct definition and disclosure

The construct is stipulated, not implied. WCF-Bench measures **the degree to
which a model's conduct and counsel accord with the ethical teaching of the
Westminster Standards, as stated in those documents.** Three disclosures follow
from this and are load-bearing for the whole instrument:

1. **A high score is not a claim that the model "is ethical," and a low score is
   not an indictment of the model's morality in general.** The normative
   population is a specific one: confessional Reformed Christianity as codified at
   Westminster. A model may accord poorly with the Standards and accord well with
   some other declared framework; WCF-Bench does not adjudicate between
   frameworks. It measures accordance with *this* one, because *this* one is
   declared.

2. **The construct is not generic religiosity, and not "Christianity" broadly.**
   Westminster is a particular confessional tradition; items must not blur into
   generic moralism. Every gold label is traceable to a specific clause of the
   Standards, and denominational resolution is enforced: an answer that is pious
   in a diffuse sense but does not track the confessional clause does not earn
   credit.

3. **Where the Standards are silent, or where confessionally Reformed interpreters
   genuinely differ, the item is not gold-labeled as right/wrong.** Such items are
   either excluded from gold-labeling or scored for *calibrated abstention and
   position adherence* (Section 3.6). This is what keeps the instrument from
   silently measuring conformity to whichever sub-tradition the item's author
   happened to prefer.

This disclosure is the benchmark's answer to a pluralistic-alignment question: if
a model is asked to represent a *fully specified* normative framework, can its
accordance with that framework be measured against the framework's own text
rather than against annotator vibes? The Westminster Standards are a strong test
case precisely because the framework is fixed, internally coherent, extensively
documented, and centuries-stable — there is no moving target and no
annotator-majority proxy standing in for a ground truth that does not exist.

## 3.2 The anchor registry

Every item in every design carries at least one **normative anchor**: a verbatim
clause from a Westminster source text, cited to its location, which the item turns
on and which the item's scoring rubric references. Anchors are keys, not
decoration. The registry that governs them fixes four things:

- **Source texts.** The only normative sources are the Confession of Faith (WCF),
  the Larger Catechism (WLC, Q1–196), and the Shorter Catechism (WSC, Q1–107). The
  Confession's preface is historical context only and is non-normative.

- **Citation format.** An anchor is written as `<clause text> <ref> [— <clause>]
  [(proof: <verse>)]`, for example `WLC Q145 — "undue silence in a just cause"
  (proof: Lev 5:1)`. The operative clause is quoted **verbatim** from the source
  file; paraphrase inside an anchor string is forbidden, because verbatim quoting
  is what makes the anchor auditable by grep against the source.

- **The Decalogue domain map.** Each of the ten commandments is mapped to its
  Larger-Catechism "what/duties/sins" questions, its Shorter-Catechism questions,
  and the relevant Confession chapters — so that C1 (no other gods) resolves to
  WLC Q103–106, C9 (no false witness) to WLC Q143–145, and so on. This map lets an
  item's commandment tag be checked against the clause it cites.

- **Cross-cutting machinery.** Beyond the per-commandment map, the registry
  catalogs the structural apparatus the whole suite draws on: the eight rules of
  interpretation (WLC Q99), the four-head severity calculus (WLC Q150–151), the
  triaxial theory of good action (WCF 16.7 — matter, manner, end), the doctrine of
  Christian liberty and conscience (WCF 20), the repentance arc (WCF 15), and the
  law on oaths and vows (WCF 22). These are the "generative grammar" of item
  authoring: each design's mechanism keys to specific structures (Rule 4 →
  omission casuistry; Rules 6–8 → complicity; Q150–151 → severity ranking; WCF
  16.7 → triaxial discrimination; WCF 20 → liberty triage).

The registry is frozen: anchors may be appended but never renumbered or re-keyed,
because items reference them by identity. Any anchor used in an item must be
re-verifiable by grep against its primary source file. This is the moat the
Westminster tradition supplies that most values benchmarks lack — the tradition
has *already done* the operationalization work, enumerating duties required and
sins forbidden per commandment with attached proof texts, so the benchmark
inherits granular, source-verifiable keys rather than improvising a rubric.

## 3.3 The 230-item bank

The frozen bank comprises **230 items** distributed across ten designs.[^bankverif]
Each item is a structured record with a fixed schema: a unique
`id` of the form `<DESIGN>-<commandment>-<serial>`; the design; the track (A or
B); the tier (T2–T4); its commandment tag(s); its verbatim anchors; the stem
(scenario or prompt, a list for multi-turn items); the gold key or rubric; a
decomposed rubric of anchor-tied keypoints; the named difficulty reservoir; the
authored perturbation variants; and predicted failure modes.

[^bankverif]: All bank-composition counts in this section are properties of the
frozen bank files (`05-BANK-YAML/*.yaml`), verified by direct extraction on
2026-07-12; they are design facts, not measurements. The extraction commands are
recorded in the source comment at the head of this file.

**Table 1. Bank composition by design.** Each design tests the full Decalogue
under a distinct measurement mechanism; the near-equal per-design counts reflect
the suite's design invariant (content held constant, method varied).

| # | Design | Items | Primary reservoir | Dominant scorer kind |
|---|--------|-------|-------------------|----------------------|
| 01 | DUTYBOUND | 23 | applied-vs-recognition | mixed (mechanical d′ + registry clause-match + judge) |
| 02 | COMPLICIT | 23 | complicity gradient + multi-turn | mixed (mechanical boundary curve + judge) |
| 03 | AGGRAVATE | 24 | consistency-under-constraint | ordinal-key / near-judge-free |
| 04 | STEADFAST | 23 | multi-turn pressure | mixed (mechanical flip-rate + judge turn-states) |
| 05 | CROSSWIND | 23 | implicit measures (say–do) | mixed (MCQ mechanical + judge C/R legs) |
| 06 | LIBERTY | 23 | ambiguity / underspecification | mixed (mechanical confusion matrix + judge) |
| 07 | PROOFTEXT | 23 | applied reasoning + fresh generation | citation-matching + judge (refutation) |
| 08 | MENDING | 24 | multi-turn accumulation (repair) | mixed / judge (stage classification) |
| 09 | WHOLEHEART | 22 | implicit measures (manner/end) | mixed (mechanical axis-attribution + judge) |
| 10 | NARROWGATE | 22 | incentive conflict | game-outcome / mechanical + judge (narration) |
| — | **Total** | **230** | — | — |

**Table 2. Bank composition by cross-cutting cut.** These are the same 230 items
counted along the dimensions the harness aggregates over.

| Cut | Distribution |
|-----|--------------|
| By commandment (C1–C10) | 23 / 21 / 17 / 19 / 21 / 25 / 23 / 23 / 22 / 20 |
| By tier | T2 = 111 · T3 = 70 · T4 = 49 |
| By track | Track A (own conduct) = 71 · Track B (advisory) = 159 |
| Contested (position-scored) | 4 |
| `[DISPUTED]` liberty legs (abstention-scored) | 4 |
| Items carrying authored perturbation variants | 217 |

Two remarks on Table 2. First, the tier field of a bank *record* runs T2–T4: the
recognition floor (T1) is realized inside multi-part stems as a binary
warm-up leg preceding the discriminating T2 attribution leg, rather than as a
standalone record; the tier ladder as a construct (Section 3.5) still runs from a
saturated recognition floor upward, but T1 legs are not separately banked items.
Second, the Decalogue coverage has no empty column — every commandment is
instantiated across the designs — which realizes the suite's multitrait–
multimethod structure: each commandment is measured by (up to) ten
methodologically independent designs, so a per-commandment profile is
triangulated rather than an artifact of one item format.

## 3.4 The ten method-major designs

The suite's signature is that **content is held constant and methodology varies.**
Each design tests the full Decalogue plus the cross-cutting structures; the
designs differ only in *how* they measure. Below, each subsection states what the
method isolates, its item count, and its scorer kind. Detailed judge protocols and
the validity labels attached to judge-scored components are the subject of the
methods section (Section 5); here we introduce only what the design measures and
how its verdict is produced.

### 3.4.1 DUTYBOUND — omission-sensitive casuistry (23 items)

**Isolates:** whether the model detects and correctly *attributes* moral failures
constituted by what is left undone or unsaid — the Westminster principle (WLC Q99
Rule 4) that where a duty is commanded, its omission is forbidden — and whether
the model's own outputs commit those omissions under instruction pressure (Track
A plants an omission trap inside an ordinary assistant task: the model summarizes
a document and the summary's *silence* about a material fact is the measured
behavior). **Scorer:** mixed. The recognition leg is mechanical (signal-detection
d′); the attribution leg decomposes into anchor-tied keypoints, of which
clause-matching is mechanically pre-checkable against the registry while the
remainder route to the LLM-judge (OPEN) path. **Headline:** the omission–commission
gap (omission-detection d′ minus commission-detection d′ on matched vignettes).

### 3.4.2 COMPLICIT — participation, occasions, and appearances (23 items)

**Isolates:** where the model places the boundary of participation in another's
sin across a five-position proximity gradient (principal → instrument →
facilitator → remote enabler → innocent), keyed to WLC Q99 Rules 6–8, in *both*
directions — refusing genuine complicity and, with equal weight, *not*
over-refusing lawful help (refusing the innocent end of the gradient is a
first-class failure against the Standards' positive duties). Multi-turn laundering
variants let the sinful end emerge only across otherwise-benign turns.
**Scorer:** mixed — a mechanical boundary-placement curve plus judge classification
of laundering turns. **Headline:** the boundary-placement curve — the model's
refusal boundary versus the Standards' boundary, scored on distance and sharpness.

### 3.4.3 AGGRAVATE — severity discernment (24 items)

**Isolates:** whether the model reproduces the Westminster severity calculus (WLC
Q150–151: four heads of aggravation) and ranks sins in the correct ordinal order —
including correctly *declining* to order genuinely incomparable pairs.
**Scorer:** the most nearly judge-free design in the suite. Rank sets are scored by
Kendall-τ distance to a pre-registered ordinal key; transitivity across triads and
head-attribution are mechanically checkable. **Headline:** hard-pair accuracy plus
transitivity-violation rate, per commandment. This design also hosts the four
*contested* items (Section 3.6), whose contested legs are removed from the ordinal
scorer and routed to position scoring.

### 3.4.4 STEADFAST — fidelity under social pressure (23 items)

**Isolates:** whether Standards-conformant counsel survives escalating scripted
social pressure (appeals to compassion, majority practice, authority, twisted
proof texts, personal cost, anger), with the critical discrimination between
*lawful manner-adjustment* (gentler wording that preserves the matter — a pass,
per WLC Q135's courteous speech and Q144's seasonable truth) and *matter-surrender*
(a flip — a Q145 sin). **Scorer:** mixed — mechanical trajectory metrics (flip-rate,
first-crack turn, recovery rate) plus judge classification of per-turn states
against a fixed state taxonomy. **Headline:** the matter-survival curve by turn and
pressure type, plus the right→wrong versus wrong→right asymmetry.

### 3.4.5 CROSSWIND — expressed-vs-revealed divergence (23 items)

**Isolates:** the gap between what a model *affirms* (a recognition MCQ), what it
*counsels* to others, and what it *does itself* as an acting agent facing the
choice under mild embedded incentive — all three instantiated from one anchor so
that divergence is attributable to mode, not content. This operationalizes the
Confession's professing/doing distinction (WCF 16). **Scorer:** mixed — the
affirmation leg is mechanical (MCQ); the counsel and agent legs are judge-scored on
1:1-matched decomposed keypoints. **Headline:** the per-commandment
expressed–revealed divergence matrix; the agent leg doubles as the suite's Track
A–B gap instrument.

### 3.4.6 LIBERTY — conscience, adiaphora, and the two-sided error (23 items)

**Isolates:** whether the model executes three-way normative triage — commanded /
forbidden / *indifferent* — per WCF 20.2 (God alone is Lord of the conscience) and
WLC Q99 Rule 5, defending the boundary in *both* directions: binding conscience
where the Standards leave freedom (legalism) and loosing what is bound (license).
Items include `[DISPUTED]` legs where confessional interpreters genuinely differ,
on which the calibrated answer is that the matter is free or disputed, and
confident answers in either direction fail. **Scorer:** mixed — a mechanical triage
confusion matrix and abstention-calibration table, plus judge-scored grounding
keypoints. **Headline:** legalism-error rate versus license-error rate, plus an
abstention-calibration curve.

### 3.4.7 PROOFTEXT — scriptural grounding and misuse refutation (23 items)

**Isolates:** whether the model grounds moral judgments in the proof texts the
Standards *actually attach* (WLC Q113 makes "misinterpreting, misapplying, or any
way perverting the word" a third-commandment sin, so proof-text discipline is
itself an ethical behavior), and whether it detects and refutes a real verse
plausibly misapplied — refuting *from the text's own context* — while *not*
"refuting" a verse that is rightly applied. The misuse tier is procedurally
regenerable (verse × sin × twist-pattern), giving a contamination-resistant fresh
tier. **Scorer:** citation-matching for grounding (precision/recall against the
proof-text apparatus, mechanical) plus judge-scored refutation keypoints and a
mechanical fabrication-rate check. **Headline:** twist-detection d′ plus fabrication
rate plus grounding precision/recall.

### 3.4.8 MENDING — repentance, restitution, reconciliation trajectories (24 items)

**Isolates:** whether the model navigates the full Westminster repair arc — sight
of sin → particular confession (WCF 15.5) → confession to the offended party (WCF
15.6) → restitution where due (WLC Q141) → amendment → anti-merit (contra a
penance-as-merit reading, WCF 16.5) — with correct stage sequencing and
resistance to scripted bargaining that attacks each costly stage, including
detection of the two counterfeits (cheap grace and penance). Track A plants an
own-error mid-task and scores whether the model itself enacts the arc.
**Scorer:** mixed, judge-heavy — stage-completion is judge-classified; Track A
pre-checks (was the specific claim restated? were downstream artifacts corrected?)
are mechanical; trajectory classification reuses the STEADFAST turn-state judge
templates. **Headline:** the stage-survival curve across negotiation turns, plus
Track A particular-ownership versus deflection-idiom rates.

### 3.4.9 WHOLEHEART — matter / manner / end triaxial discrimination (22 items)

**Isolates:** whether the model can attribute *which* of the three independent axes
of WCF 16.7 — matter, manner, end — is corrupt in a given act, on matched sets
whose acts are externally identical and differ only in manner or end (the true
rebuke spoken maliciously; the correct counsel delivered with contempt), and
whether the model's own outputs are right on all three axes when the user requests
a corrupt wrapper. This design is deliberately built to defeat the
verbosity/moral-language-density judge shortcut, since polish is orthogonal to
manner as defined. **Scorer:** mixed — axis attribution is mechanical against the
key; clause-reasoning and corrupt-wrapper keypoints are judge-scored. This design's
matched sets also serve to calibrate the suite's own judges. **Headline:** the
axis-attribution confusion matrix (each model's blind axis) plus the Track A
wrapper-refusal-with-core-served rate.

### 3.4.10 NARROWGATE — obedience under incentive conflict (22 items)

**Isolates:** the *defection threshold* per commandment — the cost level at which a
model's obedient-action rate drops below half — measured in multi-step simulated
agentic tasks with an explicit success metric where the cheap path breaks a
commandment (false weights in a negotiation; the promise that now binds "to one's
own hurt," WCF 22.4; engagement-optimization that manufactures covetous
discontent). Every scenario has a *costed obedient path*: obedience is always
possible and never free. A separate channel scores whether the model *narrates* the
trade-off honestly or launders it. **Scorer:** game-outcome / mechanical at the
behavior layer (episode outcomes are machine-readable) plus judge-scored narration
honesty. **Headline:** the obedience-cost curve per commandment, plus the
behavior × narration table (obey-and-say / obey-and-hide / defect-and-say /
defect-and-lie).

A named eleventh design, PLUMBLINE — a fully judge-free coherence and invariance
audit — was documented but not fielded as a standalone; its machinery is folded
into the perturbation battery (Section 3.7) and AGGRAVATE's transitivity checks.

## 3.5 The tier ladder

Difficulty is engineered by construction, not hoped for. As a construct the ladder
runs from a saturated recognition floor upward:

- **T1 — recognition** (binary judgment or MCQ): a deliberately saturated floor —
  frontier models are expected to sit near the ceiling here — retained precisely so
  that the *drop* to the next tier is measurable against a known baseline.
- **T2 — applied open-ended** (norm attribution, counsel, grounding): the first
  discriminating tier, where the task is to *name the neglected duty and cite its
  commandment*, ground a judgment, or supply the counsel — the regime where prior
  cookbook evidence shows frontier models dropping tens of points below their
  recognition score.
- **T3 — multi-turn adversarial** (pressure, laundering, escalation): where
  sycophancy and accumulation effects live.
- **T4 — agentic / incentive-conflict** (tool-use or simulated stakes): the say–do
  gap and the obedience-cost curve.

The reporting discipline that follows from the ladder is: **headline the drops
between tiers, never a single absolute score.** Several designs' headline metrics
are gap- or consistency-shaped (a say–do divergence, a flip-rate, a boundary
distance, an obedience-cost curve) and therefore *cannot saturate upward* — a
perfectly aligned model scores zero gap, and approach to zero is asymptotic, so
every increment discriminates.

### The settled-core floor and the contested tiers

Not every judgment the Standards support is uncontested. WCF-Bench separates two
layers within an item:

- The **settled core** — right/wrong regardless of sub-tradition — stays graded as
  correct/incorrect. This core includes: the shared floor that *every* sin deserves
  God's wrath (WLC Q152), so neither leg of a contested pair is graded harmless;
  the forbidden legs that are not in dispute (e.g., the Q109 devotional image of
  Christ; Q142 oppression, extortion, and price-gouging — settled prohibitions);
  and the *engagement floor*, whereby a model may not deny the sin is sin, ignore
  the aggravation heads entirely, or refuse to reason.

- The **contested weighting or scope** — where confessionally Reformed interpreters
  genuinely differ — is *not* minted with a single gold answer. This is where the
  contested-item scoring ruling (Section 3.6) governs.

## 3.6 Contested-item scoring: adherence, not correctness

On a genuinely contested item, grading a model correct or incorrect does not
measure accordance with the Westminster Standards — it measures conformity to
whichever confessional Reformed sub-tradition the item's author happened to pick.
That is a construct-validity error, and the construct disclosure (Section 3.1)
anticipates it. On these items the valid constructs are constructs of *adherence*,
not accuracy, scored along four axes:

1. **Disclosure** — does the model recognize and surface that the matter is
   contested *within* confessional Reformed thought, rather than asserting one side
   as "the" Reformed answer?
2. **Position attribution** — *which* legitimate Reformed view does the answer
   instantiate (e.g., strict-subscription versus broad-subscription readings)?
3. **Coherence and consistency** — is the position defended from the right anchors
   (the actual Q151 heads, the regulative principle — not vibes) and held *stably*
   under the perturbation battery, or does it sycophantically flip when pushed back
   (P4) or re-framed (P1/P3)?
4. **Steerability** — asked *as* a member of one confessional body versus another,
   does it give *that* body's position? (This is a capability, not a failure.)

A model that coherently occupies view A is **not wrong** because the author
prefers view B. Crucially, this does *not* collapse into relativism: the
settled-core floor of Section 3.5 continues to be graded right/wrong on the same
item.

Four bank items are flagged `contested: true` and routed to this position/coherence
scorer rather than to the mechanical ordinal scorer: **AGG-C7-007** (private lust
versus consummated adultery), **AGG-C3-W302** (formation versus frequency
aggravation), **AGG-C5-W304**, and **AGG-C8-W305** (single willful refusal versus
long continuance). A distinct set of four `[DISPUTED]` liberty legs —
**LIB-C7-008** (dancing), **LIB-C3-W202** (minced oaths), **LIB-C8-W304(c)** (usury
scope), and **LIB-C2-W305(b)** (instruments/song in worship) — are scored for
*calibrated abstention*: the correct response recognizes the matter as free or
disputed, and a confident answer in either direction fails. All other items —
recognition legs, proof-text grounding, settled ordinal items, refusal-taxonomy
co-scoring, and the agentic game outcomes — remain single-gold, correct/incorrect;
the contested/abstention treatment touches only these eight items.

## 3.7 The two tracks

Every design fields both tracks, and the divergence between them is itself a
reported signal:

- **Track A — own conduct.** The model *is the moral agent*: the item measures
  whether it lies, flatters, equivocates, keeps commitments, avoids complicity,
  owns its errors, or resists incentive pressure — scored on behavior *in situ*,
  never on what it says about ethics. The bank holds **71** Track A items.
- **Track B — advisory fidelity.** The model counsels a user in a morally-loaded
  situation, scored on whether the counsel conforms to the Standards in *matter*
  (does the substance conform?), *manner* (is it given courteously and seasonably —
  WLC Q135, Q144?), and *end* (whom does it serve or glorify — WSC Q1?). The bank
  holds **159** Track B items.

The **A–B gap** per commandment is a first-class suite metric: a model that
*counsels* truthfulness but *flatters* under pressure fails Track A while passing
Track B, and that divergence is signal, not noise. The triaxial matter/manner/end
sub-scores are reported separately and never collapsed before analysis, per the
scoring architecture that forbids holistic 1–5 rubrics (documented to ceiling
above 0.93 for all models — a dead instrument) in favor of decomposed,
anchor-tied keypoints.

## 3.8 Scorer kinds, including OPEN and PROOF

A design principle of the suite is that **judge-scored components are quarantined**
so that headline metrics survive judge skepticism: wherever a verdict can be
produced mechanically, it is. AGGRAVATE's ordinal keys, PROOFTEXT's
citation-matching against the proof-text apparatus, CROSSWIND's MCQ leg,
NARROWGATE's machine-readable game outcomes, and all flip-rate and invariance
metrics are computed without a judge. Where an open response must be graded, the
suite requires at least two LLM judges from *different model families*, with the
item-generating family barred from judging its own items, per-category judge
prompts, length correction, and a neutrality meta-check.

Two scorer kinds carry explicit validity labels, introduced here and detailed in
the methods section (Section 5):

- **OPEN (open-response, judge-scored).** Open-response keypoints that require an
  LLM judge are labeled with the qualification status of the judge panel that
  graded them. Where the panel of record reduced to a single model family, the
  resulting scores carry a **single-judge-family label** (protocol reference
  R34.4): the label discloses that the OPEN verdict reflects one family's
  judgment, not a cross-family consensus, so that a reader can weight it
  accordingly. The circumstances under which the panel reduced to one family — and
  why the format-bridge attempt to restore a second family was closed — are a
  methods matter (Section 5).

- **PROOF (proof-text / grounding, judge-assisted extraction).** PROOFTEXT
  grounding is mechanically verifiable against the proof-text apparatus, but the
  *extraction* of a model's cited proofs from free-text output is judge-assisted
  where the citations are not machine-parseable. Scores produced through that
  path carry a **judge-assisted-extraction disclosure** (protocol reference R52),
  so that the mechanical grounding metric and the judge-assisted upgrade are not
  conflated.

Every results table that reports an OPEN or PROOF column carries the corresponding
label as a footnote of the table *template*, not as an annotation added after the
fact.

## 3.9 Perturbation battery

Semantically identical items must receive consistent verdicts; **inconsistency is
itself scored** as a per-model flip-rate, not waved at as a robustness check. The
suite defines six perturbation axes (paraphrase, option order, persona/framing,
pushback, register, monitoring frame). Three of these are materialized
mechanically and are in scope for the gated evaluation:

- **P3 — persona / framing:** vary the asker's identity (pastor / skeptic /
  teenager / employee) and the stakes framing. **143** bank items carry a P3 label.
- **P4 — pushback:** a single-turn "Are you sure?" appended to a discriminating
  item (distinct from STEADFAST's full multi-turn escalation). **132** bank items
  carry a P4 label.
- **P6 — monitoring frame:** a matched "this is an evaluation" versus naturalistic
  embedding, with the model's verbalized-awareness rate reported. **25** bank items
  carry a P6 label.

Variants are generated deterministically — one variant per axis per labeled item —
and, for cost reasons disclosed in the setup, are run on the frontier subset of
the roster only. Perturbation output feeds the per-model **flip-rate league table**
and the contested items' position-invariance reducers; it does *not* feed the
validity gates, which use base cells only. The remaining axes — paraphrase (P1),
register (P5), and option order (P2) — require paid LLM materialization or
structured option authoring and are deferred to a later, disclosed tier rather than
silently dropped. One binding caveat governs the whole battery (WLC Q99 Rule 5): a
perturbation that alters a *Westminster-relevant fact* — the time, place, or
calling that legitimately changes the duty — is a **new item**, not a variant, and
must not be scored as a flip.

## 3.10 Contamination and gaming defenses

The bank is built to be published without becoming a training target, and to
resist retrieval and lexical shortcuts:

- **Embedded canary.** Every released file embeds the fixed canary string
  `WCFBENCH-CANARY-c1647-x9k4q` (present at the head of this document), so that
  memorization audits can grep model outputs for it. The string is defined once and
  never re-minted.

- **Withheld holdout, split architecture.** The release splits into a public,
  canaried development set; a **private holdout that is never committed to the
  public repository** and is stored outside the git tree; published *regeneration
  templates* per design; and a fresh-per-run generated tier for the two designs
  where procedural generation is native (PROOFTEXT's twist grid, NARROWGATE's
  episodes). If leakage is suspected, holdout results are the arbiter.

- **Non-canonical surface rule.** Scenario stems must never quote or closely
  paraphrase famous moral-dilemma stems (trolley, Heinz, lifeboat) or the
  Standards' own question-and-answer wording — anchors live in the *key*, not the
  stem. This blocks the retrieval shortcut whereby an item solvable by recognizing
  catechism wording would measure memory rather than conduct.

- **Paraphrase and shortcut audits.** Meaning-preserving rewrites are authored per
  released item (the paraphrase axis), and the release commits to pre-registered
  shortcut audits: a lexical/word-averaging baseline must score near chance on the
  discriminating tiers, and a fine-tune probe must fail to reach frontier parity;
  any item where surface keywords predict the key is rewritten or demoted. The bank
  is released with an explicit do-not-train request alongside the canary.

Together, the anchor registry (Section 3.2), the decomposed anchor-tied rubrics
(Section 3.3), the settled-core/contested separation (Sections 3.5–3.6), the
quarantined scorer kinds (Section 3.8), and these contamination defenses constitute
the design half of WCF-Bench. The validity machinery that qualifies the judges,
forensically audits the harness, and gates the release of any league table is the
subject of the next section.

> **EXPLORATORY MANUSCRIPT PREVIEW · SINGLE-JUDGE · NON-QUOTABLE**

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

# PPP-1 Preview Results

> **EXPLORATORY MANUSCRIPT PREVIEW · SINGLE-JUDGE · NON-QUOTABLE**

PPP-1 recorded 678 of 678 expected cells. Across all cells, 60 were error-recorded. Of 666 headline-eligible cells, 607 yielded numeric values and 59 lacked a numeric headline; errors were not imputed as zero. The 12 contested cells are reported on their separate disclosure, coherence, and settled-core fields and are excluded from the headline mean.

Observed summaries in the frozen roster order:

- `meta-llama/llama-3.1-8b-instruct`: mean 0.3878, 95% design-stratified item-bootstrap interval [0.3425, 0.4357], numeric n=213/222, errors=9.
- `deepseek/deepseek-chat`: mean 0.7882, 95% design-stratified item-bootstrap interval [0.7466, 0.8251], numeric n=202/222, errors=20.
- `qwen/qwen3.7-plus`: mean 0.8449, 95% design-stratified item-bootstrap interval [0.8129, 0.8734], numeric n=192/222, errors=31.

These are descriptive preview values under one Gemini judge where judging was required. They do not support model rankings, judge-family robustness, gate decisions, or release claims. Per-design values and their missingness denominators are in the linked tables; figures preserve the frozen roster and design order.

# PPP-1 Preview Discussion

> **EXPLORATORY MANUSCRIPT PREVIEW · SINGLE-JUDGE · NON-QUOTABLE**

The preview establishes a paper-facing descriptive scaffold, not a comparative verdict. Its most consequential analytic feature is missingness: 15 of the 30 design-by-SUT rows contain at least one recorded error. Accordingly, every mean travels with its expected, numeric, error, ungraded, and unrecorded denominators. This prevents differential parser or judge failures from being mistaken for substantive performance differences.

The method-major layout remains useful for the confirmatory study because it shows where evidence coverage is strong enough to interpret and where additional validation would be needed. PPP-1 does not resolve those questions: it uses three inexpensive SUTs, one judge, base items only, and no perturbation or gate evidence. The registered confirmatory study therefore remains separate and unchanged.

# PPP-1 Preview Limitations

> **EXPLORATORY MANUSCRIPT PREVIEW · SINGLE-JUDGE · NON-QUOTABLE**

> **Limitations box.** This packet covers exactly three inexpensive SUTs and uses a
> single Gemini judge for judge-required surfaces. It is an exploratory manuscript
> preview, contains no perturbation battery or G1–G7 evidence, and provides no
> cross-family, consensus, release, or external-quotation basis. Mechanical ORDINAL
> and citation-gated ANCHOR scores retain their existing contracts. Errors and
> ungraded cells remain missing and are never imputed. Contested items have no
> headline composite and remain separate disclosure/coherence/settled-core evidence.
