**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content

> **PART FILE — assembles into paper (a). §2 Related work. Venue-generic, author-generic draft. Terminology, section numbering, and governance-rule labels follow the §3/§4 draft exactly.**

---

## 2 Related work

WALKWORTHY sits at the intersection of four literatures that rarely meet: moral and
value-laden evaluation of language models, religious and cultural values in model
evaluation, behavioral rather than knowledge-style probing, and the measurement-theory
critique of benchmarks. We survey each in turn and state, at the end of each thread,
precisely what this instrument adds and — equally important — what it declines to claim.

### 2.1 Moral and value-laden evaluation of language models

The dominant paradigm for moral evaluation of deployed language models descends from
preference-tuned assistant training, where "harmlessness" is operationalized as a
preference signal collected from human raters and optimized against (Bai et al., 2022a);
successor formulations replace some of that human labelling with a written list of
principles the model critiques itself against (Bai et al., 2022b). Both make the
evaluation target internal to the training pipeline: the standard against which conduct is
scored is the deploying organisation's own preference distribution or its own
constitution, and it is not separately auditable by a reader of the resulting scores.
Downstream safety benchmarks inherit this property, and their reliability has itself come
under scrutiny — a systematic pass over the safety evaluation pipeline finds intertwined
sources of noise at every stage, from dataset curation to judge-based scoring, sufficient
to make attacks and defences hard to compare fairly (Beyer et al., 2025).

A second body of work supplies moral content rather than safety policy. The ETHICS
dataset assembled scenario judgments across justice, deontology, virtue, and commonsense
morality, and became the most-cited instrument for testing "ethical capability"
(Hendrycks et al., 2021). Its validity has been interrogated directly: drawing on moral
theory, psychology, and prompt-level analysis, Hancox-Li et al. (2024) argue that ETHICS
principally measures commonsense pattern-matching rather than ethical reasoning, and that
the field cannot secure the validity of an ethics evaluation without first being clear
about which ethical phenomenon it means to measure. Subsequent datasets have broadened the
scenario base — everyday dilemmas annotated with the values each action implicates
(Chiu et al., 2024), multi-dimensional moral-reasoning assessment frameworks
(Jiao et al., 2025) — while a distinct line ties items explicitly to a named normative
theory, as with the Greatest Good Benchmark's utilitarian dilemmas
(Marraffini et al., 2025). Moral-foundations instruments form a parallel tradition,
surveyed comprehensively for pre-trained language models by Zangari et al. (2024), and
architectural proposals for deliberation under normative moral pluralism argue that
plural traditions should be represented as structured, weighable arguments rather than
collapsed into a single scalar (Yaacov, 2025).

What unites almost all of this work is that the standard of comparison is generic or
aggregated: commonsense morality, a rater population's aggregate preference, a
foundations profile, or a single normative theory selected on the evaluator's authority.
WALKWORTHY makes the opposite commitment. Its standard is a **named, specified corpus** —
a fifteen-work registry whose composition is stated in the manuscript and whose keyed
behaviors are traceable, item by item, to specific chapters or dictionary entries. The
reported quantity is *concordance with that corpus*, not moral correctness. A reader who
rejects the registry's positions can still read every number in this manuscript as a
well-defined measurement, because what is measured is agreement with a document set that
the reader can open. The Greatest Good Benchmark is the nearest precedent in spirit —
a benchmark that names its normative source rather than appealing to consensus — and
WALKWORTHY extends that move from a single philosophical theory to a bounded textual
corpus with per-item anchoring.

### 2.2 Religious and cultural values in model evaluation

Religion enters model evaluation along three lines. The first is bias and stereotype
measurement: systematic probing across mask-filling, completion, and image generation
finds stereotype associations distributed unevenly across religions and intersecting with
gender, age, and nationality (Abrar et al., 2025), and demographic-distance methods infer
whose religious opinions a model's outputs most resemble, with attention to non-Western
populations (Shankar et al., 2025). The second is *values elicitation*: Liu et al. (2025)
test the spiritual values that popular models express, find them diverse rather than
uniformly secular, and then show that different elicited spiritual values change model
sensitivity across hate-target groups. The third, and closest to our work, is
tradition-anchored knowledge and reasoning benchmarking. IslamicMMLU assembles a large
multiple-choice bank across Quran, Hadith, and Fiqh tracks, including a school-of-thought
bias detection task (Abdelaal et al., 2026). IslamicLegalBench draws 718 instances from
38 foundational legal texts across seven schools of jurisprudence and reports both
accuracy and hallucination rates, along with a false-premise probe on which most tested
models accept misleading assumptions at high rates (Elmahjub et al., 2026). On the
Christian side, Owen (2026) constructs a doctrinal knowledge base of 576 atomic claims
drawn from catechisms, confessions, creeds, and denominational statements across eleven
traditions, and scores model responses against it — finding high precision but weak
recall, and a systematic tendency to attribute beliefs to "Christians" as an undivided
whole. Owen names this *doctrinal flattening*.

Alongside these sits the broader cultural-alignment literature, which supplies both methods
and cautions: cross-national survey instruments adapted to ask whose opinions a model's
answers resemble (Durmus et al., 2024); psychological measures showing model responses to
be an outlier relative to large-scale cross-cultural data and closest to Western, Educated,
Industrialized, Rich and Democratic populations (Atari et al., 2023); reviews documenting
cultural bias in model outputs across regions (Sukiennik et al., 2025); and a study testing
a published assistant constitution against World Values Survey items, which reports the
assistant's values sitting closest to Northern European and Anglophone populations and, on
many items, outside the range of every surveyed population (Pourdavood et al., 2026).

WALKWORTHY's position in this thread requires care, because it is easy to mis-read.
**We do not evaluate fidelity to a religion.** We evaluate behavioral concordance with a
fifteen-work registry that is **Protestant-Reformed-dominant** and named as such, and we
never claim that the registry's positions are correct, representative of Christianity, or
theologically authoritative. Two construction rules do the scoping work. Direct Scripture
anchoring is **disallowed by construction**, so every keyed behavior is mediated through a
named human ethicist's exposition rather than through a contested reading of a sacred
text; and one registry work is restricted to contrast-only use, carrying no consensus
claim anywhere in the bank. Items on which the fifteen works do not speak with one voice
are stratified as intra-corpus disputed and quarantined from comparative claims. Where
Owen (2026) treats flattening across eleven traditions as the defect to be detected, we
take the complementary route: we decline breadth entirely, name a single narrow corpus,
and accept the resulting limits on generality as the price of an auditable target.

Christian-anchored evaluation of language models does exist, and precision about how it
differs is more useful here than a bare claim of novelty. The closest neighbour we located
is the Gospel Coalition's AI Christian Benchmark (Sapp et al., 2025), which puts seven
theological questions to seven consumer platforms and has a panel of Christian scholars
hand-grade the answers, with score bands keyed to the Nicene Creed and, higher up, to that
organisation's own foundation documents and historic Protestant confessions. It is a
single-turn evaluation of **doctrinal assent** — what a model says it believes when asked
directly — and it is issued as a ministry report rather than a peer-reviewed study.
Adjacent academic work measures religious *bias* rather than conduct (Abrar et al., 2025;
Liu et al., 2025). What we did not locate is a *behavioral* benchmark that anchors conduct
— what a model does under pressure, across turns, in twinned conditions — to a named
corpus of Christian ethicists rather than to a creed or a confession. That narrower gap is
the one this instrument occupies, and we state it as a gap in the literature we surveyed
rather than as an exhaustive claim.

### 2.3 Behavioral versus knowledge-style evaluation

The methodological shift from asking a model what it believes to observing what it does
under pressure is now well established. Model-written evaluations demonstrated that
behavioral probes could be generated at scale and surfaced inverse-scaling cases in which
larger models repeat back a user's preferred answer (Perez et al., 2022). Sycophancy has
since become its own measurement literature: preference-trained assistants exhibit it
consistently across free-form generation tasks, and human preference judgments appear
implicated in producing it (Sharma et al., 2024); multi-turn benchmarks measure how many
turns a model holds a position before conceding to a pressing user, and report that
preference training amplifies the effect (Hong et al., 2025); and broader formulations
extend the construct from agreement with stated beliefs to excessive preservation of a
user's self-image (Cheng et al., 2025). Escalation is the natural design idiom here:
multi-step moral dilemmas that progressively intensify a conflict show value priorities
shifting as the ladder is climbed, which single-step protocols cannot see
(Wu et al., 2025); and dialogue- and story-embedded value-alignment items are proposed
precisely because single-sentence adversarial prompts are now easy for tuned models to
deflect (Zhang et al., 2025).

Two further strands matter for our designs. The first is the gap between stated and
enacted values, formalized as the "value-action gap" and instrumented over a large bank of
value-informed actions spanning cultures and social topics (Shen et al., 2025), and
approached from the defect-detection side by work that tests for behavioral inconsistency
in the ethical suggestions models actually give (Ma et al., 2025). The second is agentic
behavioral probing, where the unit of observation is an action taken under goal conflict
rather than an answer given: stress tests in simulated corporate environments elicit
insider-threat behaviors across models from several developers (Anthropic, 2025);
managerial trade-off benchmarks pit operational effectiveness against human safety
(Simhi et al., 2025); and deception benchmarks score enacted deceptive conduct in
scenario settings (Huang et al., 2025).

All ten WALKWORTHY designs are behavioral in this sense, and none is a multiple-choice
knowledge probe. Several are multi-turn, including a scripted social-pressure ladder with
model-classified branch routing and a comfort-then-truth pastoral arc whose keyed terminal
state can only be reached across turns. The methodological commitment that distinguishes
the suite, however, is *pairing*: six designs run paired or multi-seat administrations
that differ in exactly one manipulated factor — observability, motive cue, covertness,
dispute seat, deservingness cue — so that the headline is a **within-item difference
between twinned conditions** rather than an absolute rating of a single response. This
buys partial immunity to the rater-level and stylistic confounds that afflict absolute
scoring, because both members of a pair are scored under the same rubric by the same
judge. One design (05) is judge-free by construction, scored by a mechanical allocation
parser, and is the only surface in the suite where the two-judge precondition is satisfied
by construction rather than by arrangement. The logic of that manipulation is inherited
from the counterfactual-revision literature. Kaushik et al. (2020) have annotators make
minimal local edits that flip a document's label, so that what separates the twinned pair
is the feature under test rather than a correlated artefact; Gardner et al. (2020) turn the
same primitive toward evaluation, assembling contrast sets that probe a model's local
decision boundary where an ordinary test set would let a shortcut pass unnoticed. Our
paired designs apply that primitive to a behavioral, value-laden target: the manipulated
factor is a single situational cue, and the reported quantity is the within-item difference
it produces. What we did not locate is that primitive developed specifically as a
confound-control device for value-laden *behavioral* evaluation, where the twinned object
is a multi-turn administration rather than a document — so what we claim here is the
application, not the device.

### 2.4 Construct validity and benchmark measurement

A now-substantial critical literature holds that benchmarks routinely fail to measure the
construct their names assert. The position statement of this critique argues that a small
set of influential benchmarks came to stand in for general capability without ever
establishing that they measure it, and locates the failure squarely in construct validity
(Raji et al., 2021); a companion diagnosis of benchmarking in language understanding
catalogued the practical mechanisms — unreliable and biased systems scoring highly, little
headroom left for genuine improvement — by which this happens (Bowman and Dahl, 2021).
Recent work has made the critique operational: a large multi-author review documents how
often the construct is left unspecified in language-model benchmarks and proposes what
builders should report instead (Bean et al., 2025). Karimi-Malekabadi et al. (2026) push
the diagnosis one step earlier, arguing that socio-cognitive benchmarks typically proceed with no explicit theoretical
specification of the target capability at all, so that narrow task coverage is routinely
misread as broad competence; their remedy is a lightweight documentation artifact, the
Theory Trace Card, in the tradition of model cards (Mitchell et al., 2019). Psychometric
framings supply the complementary toolkit, importing item-level quality assessment and
latent-variable measurement into benchmark construction (Fang et al., 2024). Review and
risk-management work rounds this out: an interdisciplinary review of current issues in AI
evaluation (Eriksson et al., 2025), and a risk-management analysis of 26 popular
benchmarks that enumerates 57 failure modes and 196 mitigations across comprehensiveness,
intelligibility, consistency, correctness, and longevity (McGregor et al., 2025).

WALKWORTHY takes this literature as a specification rather than as background. Three
things follow. First, the manuscript reports **double-rated item-quality evidence**: the
whole bank was rated on six dimensions by independent fresh-context raters under a locked
protocol, with overall severity derived mechanically from the dimensions rather than rated
directly, and with planted defects used as a detection check. Second, it reports a
**defect taxonomy** and the full disposition of every proposed edit, so that the reader
can see which classes of item defect were found, which were refuted, and which were
repaired. Third, and most consequentially for the reader of §2.4's literature, it reports
an explicit **construct-validity triage (CV-1)** that scopes candidate corpus-distinctive
measurement to a three-design sub-panel rather than asserting distinctiveness across all
ten designs. We are deliberate about the epistemic status of that triage: it is reported
as an **annotation** — a reasoned scoping of where the corpus-distinctive construct could
plausibly be carried — and **not** as an empirical discriminant test. No experiment in
this manuscript demonstrates that the three-design sub-panel measures something a generic
harmlessness instrument would miss; the annotation says where such a demonstration would
have to be attempted.

### 2.5 Judge-based scoring and its limits

Model-graded scoring is now standard practice for open-ended behavioral items, and its
reliability is contested in the same breath. The canonical treatment establishes both the
utility of strong models as judges and their position, verbosity, and self-enhancement
biases (Zheng et al., 2023); a book-length survey catalogues the design space and frames
the central open problem as how to build judge systems that are reliable at all
(Gu et al., 2024); judges have been shown to recognize and prefer their own generations
(Panickssery et al., 2024); and systematic analysis finds automated judges degrading in
predictable regions — non-English prompts, factual verification, hard items
(Son et al., 2024). WALKWORTHY responds structurally rather than analytically: a mandated
two-judge cross-family rule (R4) applies to every judged administration, and one design is
judge-free by construction. The quantitative localization of where and why the two judges
diverge, including the two-referee concordance method used to audit it, belongs to the
companion methods paper and is not reproduced here; that work establishes concordance
between reference models and never that a given judge is correct. What this manuscript
carries forward is the consequence: with eight of the nine judged designs flipping system ordering
under a judge swap, and the judge-free surface yielding no pairwise contrast whose
interval excludes zero, the comparative surface is unsupported at this system tier, and we
report that as a finding rather than as a schedule.

---

### Citation ledger

| Cited as | Vault source file |
|---|---|
| Bai et al., 2022a (Training a Helpful and Harmless Assistant with RLHF) | `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/RELIGIOUS-VALUES/BACKGROUND/EXTRACT/2022-Bai-Training Helpful And Harmless.md` (also `papers/2022-Bai-Training a Helpful and Harmless Assistant with.md`) |
| Bai et al., 2022b (Constitutional AI) | `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/papers/2022-Bai-Constitutional AI.md` |
| Beyer et al., 2025 (LLM-Safety Evaluations Lack Robustness) | `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/NORM-ETHICS/BACKGROUND/EXTRACT/2025-Beyer-LLM-Safety Evaluations Lack Robustness.md` |
| Hendrycks et al., 2021 (ETHICS / Aligning AI with Shared Human Values) | `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/papers/2021-Hendrycks-Aligning AI with Shared Human Values.md` |
| Hancox-Li et al., 2024 (Is ETHICS about ethics?) | `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/papers/2024-Hancox-Li-Is ETHICS about ethics.md` |
| Chiu et al., 2024 (DailyDilemmas) | `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/papers/2024-Chiu-DailyDilemmas.md` |
| Jiao et al., 2025 (LLM Ethics Benchmark) | `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/NORM-ETHICS/BACKGROUND/EXTRACT/2025-Jiao-LLM Ethics Benchmark Three-Dimensional Assessment.md` |
| Marraffini et al., 2025 (Greatest Good Benchmark) | `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/NORM-ETHICS/BACKGROUND/EXTRACT/2025-Marraffini-Greatest Good Benchmark Utilitarian LLM.md` |
| Zangari et al., 2024 (survey on moral foundation theory and PLMs) | `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/NORM-ETHICS/BACKGROUND/EXTRACT/2024-Zangari-A survey on moral foundation theory and pre-trained language models.md` |
| Yaacov, 2025 (Normative Moral Pluralism for AI) | `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/NORM-ETHICS/BACKGROUND/EXTRACT/2025-Yaacov-Normative Moral Pluralism for AI.md` |
| Abrar et al., 2025 (Religious Bias Landscape in Language and Text-to-Image Models) | `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/RELIGIOUS-VALUES/BACKGROUND/EXTRACT/2025-Hamid-Religious Bias Landscape Language.md` (vault filename credits "Hamid"; paper's own byline is Abrar, Oeshy, Kabir, Ananiadou) |
| Shankar et al., 2025 (Sometimes the Model doth preach) | `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/RELIGIOUS-VALUES/BACKGROUND/EXTRACT/2025-Shankar-Sometimes The Model Doth.md` |
| Liu et al., 2025 (Measuring Spiritual Values and Biases of LLMs) | `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/RELIGIOUS-VALUES/BACKGROUND/EXTRACT/2024-Buyl-Measuring Spiritual Values And.md` (vault filename credits "Buyl"; paper's own byline is Liu, Zhang, Yan, Wu, Yang, Lu) |
| Abdelaal et al., 2026 (IslamicMMLU) | `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/RELIGIOUS-VALUES/BACKGROUND/EXTRACT/2024-Alharbi-Islamicmmlu Benchmark For Evaluating.md` (also `NORM-ETHICS/BACKGROUND/EXTRACT/2026-Abdelaal-IslamicMMLU.md`; vault filename credits "Alharbi", paper's byline is Abdelaal, Al Haffar, Fawzi, Magdy) |
| Elmahjub et al., 2026 (IslamicLegalBench) | `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/papers/2026-Elmahjub-IslamicLegalBench.md` |
| Owen, 2026 (Detecting doctrinal flattening in AI generated responses) | `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/RELIGIOUS-VALUES/BACKGROUND/EXTRACT/2026-Johnson-Detecting Doctrinal Flattening Ai.md` (vault filename credits "Johnson"; paper's byline is Jason Owen, *AI and Ethics* 6:178) |
| Durmus et al., 2024 (GlobalOpinionQA) | `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/RELIGIOUS-VALUES/BACKGROUND/EXTRACT/2024-Durmus-Towards Measuring The Representation.md` |
| Atari et al., 2023 (Which Humans?) | `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/NORM-ETHICS/BACKGROUND/EXTRACT/2023-Atari-Which Humans Cultural Bias AI.md` |
| Sukiennik et al., 2025 (An Evaluation of Cultural Value Alignment in LLM) | `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/RELIGIOUS-VALUES/BACKGROUND/EXTRACT/2025-Sukiennik-Evaluation Cultural Value Alignment.md` |
| Pourdavood et al., 2026 (Does Claude's Constitution Have a Culture?) | `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/papers/2026-Pourdavood-Does Claudes Constitution Have a Culture.md` |
| Perez et al., 2022 (Model-Written Evaluations) | `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/papers/2022-Perez-Discovering Language Model Behaviors with Model-Written Evaluations.md` |
| Sharma et al., 2024 (Towards Understanding Sycophancy in Language Models) | `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/papers/2024-Sharma-Towards Understanding Sycophancy in Language Models.md` |
| Hong et al., 2025 (SYCON-Bench) | `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/papers/2025-Zheng-SYCON Bench.md` (vault filename credits "Zheng"; note's `authors` field is Hong, Byun, Kim, Shu, Choi) |
| Cheng et al., 2025 (ELEPHANT / social sycophancy) | `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/papers/2025-Cheng-ELEPHANT Social Sycophancy.md` |
| Wu et al., 2025 (The Staircase of Ethics / Multi-step Moral Dilemmas) | `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/NORM-ETHICS/BACKGROUND/EXTRACT/2025-Wu-Staircase of Ethics Multi-Step Moral Dilemmas.md` |
| Zhang et al., 2025 (Beyond Single-Sentence Prompts) | `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/NORM-ETHICS/BACKGROUND/EXTRACT/2025-Zhang-Beyond Single-Sentence Prompts Upgrading Value Alignment Benchmarks.md` |
| Shen et al., 2025 (ValueActionLens / value-action gap) | `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/papers/2025-Shen-ValueActionLens Mind the Value-Action Gap.md` |
| Ma et al., 2025 (EthicsSuite) | `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/papers/2025-Ma-EthicsSuite Detecting Behavioral Inconsistency in LLM Ethics.md` |
| Anthropic, 2025 (Agentic Misalignment) | `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/papers/2025-Anthropic-Agentic Misalignment.md` |
| Simhi et al., 2025 (ManagerBench) | `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/papers/2025-Simhi-ManagerBench Evaluating Safety-Pragmatism Trade-off in Managerial.md` |
| Huang et al., 2025 (DeceptionBench) | `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/papers/2025-Huang-DeceptionBench A Comprehensive Benchmark for AI Deception Behaviors.md` |
| Raji et al., 2021 (AI and the Everything in the Whole Wide World Benchmark) | `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/NORM-ETHICS/BACKGROUND/EXTRACT/2021-Raji-AI and the Everything in the Whole Wide World Benchmark.md` |
| Bowman and Dahl, 2021 (What Will it Take to Fix Benchmarking in NLU?) | `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/NORM-ETHICS/BACKGROUND/EXTRACT/2021-Bowman-What Will it Take to Fix Benchmarking in NLU.md` |
| Bean et al., 2025 (Measuring what Matters: Construct Validity in LLM Benchmarks) | `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/NORM-ETHICS/BACKGROUND/EXTRACT/2025-Burden-Measuring What Matters Construct Validity in LLM Benchmarks.md` (also `NORM-ETHICS/.../2024-Bean-Measuring What Matters - Construct Validity in LLM Benchmarks.md` and `RELIGIOUS-VALUES/.../2025-Li-Measuring What Matters Construct.md`; paper's lead byline is Bean, Kearns et al.) |
| Karimi-Malekabadi et al., 2026 (Theory Trace Card) | `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/NORM-ETHICS/BACKGROUND/EXTRACT/2026-Karimi-Malekabadi-Theory Trace Card TTC Documentation for Socio-Cognitive Benchmarks.md` |
| Mitchell et al., 2019 (Model Cards for Model Reporting) | `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/NORM-ETHICS/BACKGROUND/EXTRACT/2019-Mitchell-Model Cards for Model Reporting.md` |
| Fang et al., 2024 (PATCH: Psychometrics-Assisted Benchmarking) | `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/RELIGIOUS-VALUES/BACKGROUND/EXTRACT/2024-Srivastava-Patch Psychometrics Assisted Benchmarking.md` (vault filename credits "Srivastava"; paper's byline is Fang, Oberski, Nguyen) |
| Eriksson et al., 2025 (Can We Trust AI Benchmarks?) | `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/NORM-ETHICS/BACKGROUND/EXTRACT/2025-Eriksson-Can We Trust AI Benchmarks An Interdisciplinary Review.md` |
| McGregor et al., 2025 (BenchRisk) | `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/NORM-ETHICS/BACKGROUND/EXTRACT/2025-McGregor-BenchRisk Identifying 57 Failure Modes in AI Safety Benchmarks.md` |
| Zheng et al., 2023 (Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena) | `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/RELIGIOUS-VALUES/BACKGROUND/EXTRACT/2023-Zheng-Judging Llm Judge With.md` |
| Gu et al., 2024 (A Survey on LLM-as-a-Judge) | `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/NORM-ETHICS/BACKGROUND/EXTRACT/2024-Gu-A Survey on LLM-as-a-Judge.md` |
| Panickssery et al., 2024 (LLM Evaluators Recognize and Favor Their Own Generations) | `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/NORM-ETHICS/BACKGROUND/EXTRACT/2024-Panickssery-LLM Evaluators Favor Own Generations.md` |
| Son et al., 2024 (LLM-as-a-Judge & Reward Model: What They Can and Cannot Do) | `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/NORM-ETHICS/BACKGROUND/EXTRACT/2024-Son-LLM-as-a-Judge & Reward Model What They Can and Cannot Do.md` |
| "the companion methods paper" (referred to generically; no citation key) | — (companion manuscript in this same `20260725-manuscripts` set; venue-generic, deliberately uncited) |

### External sources (added 2026-07-29; not held in the vault)

These three were added by the §2 citation sweep and are **not** vault-resident. Each was
retrieved and inspected directly rather than cited from memory; the retrieval date is
recorded so the claim is auditable.

| Cited as | Full record | Verification |
|---|---|---|
| Sapp et al., 2025 (The Gospel Coalition AI Christian Benchmark) | The Gospel Coalition / The Keller Center, ministry report, not peer-reviewed. Seven theological prompts × seven consumer platforms, hand-graded by a panel of Christian scholars; score bands keyed to the Nicene Creed (lower band) and TGC foundation documents plus historic Protestant confessions (upper band). `https://www.thegospelcoalition.org/ai-christian-benchmark/` | Page retrieved and read 2026-07-29. **A vault record exists** at `CEI-Lit-WS/papers/2025-Coalition-The Gospel Coalition AI Christian Benchmark.md` (its `first_author` is Casey Sapp, so the filename token "Coalition" is another byline mismatch) **but its PDF extract is an empty shell** — `PDF Extracts/2025/2025-Coalition-…md` reports `pages: 0` with a blank content block. The vault copy therefore cannot support a citation; the live report can. |
| Kaushik, Hovy and Lipton, 2020 (*Learning the Difference That Makes a Difference with Counterfactually-Augmented Data*) | International Conference on Learning Representations, 2020. Code/data: `https://github.com/acmi-lab/counterfactually-augmented-data` | Record confirmed against the conference programme listing and the authors' repository, 2026-07-29. |
| Gardner et al., 2020 (*Evaluating Models' Local Decision Boundaries via Contrast Sets*) | Findings of the Association for Computational Linguistics: EMNLP 2020, pp. 1307–1323. `https://aclanthology.org/2020.findings-emnlp.117/` | Record confirmed against the ACL Anthology entry, 2026-07-29. |

**Note on filename-vs-byline mismatches.** Seven vault sources carry an author token in the
filename that does not match the paper's own byline (Hamid/Abrar, Buyl/Liu, Alharbi/Abdelaal,
Johnson/Owen, Srivastava/Fang, Zheng/Hong, Burden-Li/Bean). In every case the citation in the
prose follows the byline printed in the source document, and the ledger records the vault path
so the discrepancy is auditable. Any downstream bibliography build should resolve these against
the source PDFs rather than the filenames.

---

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content
