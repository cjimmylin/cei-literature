---
title: "2026-Karimi-Malekabadi-Theory Trace Card TTC Documentation for Socio-Cognitive Benchmarks - PDF Extract"
source_pdf: "2026-Karimi-Malekabadi-Theory Trace Card TTC Documentation for Socio-Cognitive Benchmarks.pdf"
pages: 15
extracted_at: "2026-02-07T17:00:45.792498"
---

# PDF Extract: 2026-Karimi-Malekabadi-Theory Trace Card TTC Documentation for Socio-Cognitive Benchmarks

**Source PDF:** 2026-Karimi-Malekabadi-Theory Trace Card TTC Documentation for Socio-Cognitive Benchmarks.pdf
**Total Pages:** 15

---

## Content

```
--- Page 1 ---

Theory Trace Card: Theory-Driven Socio-Cognitive Evaluation of LLMs
Farzan Karimi-Malekabadi
Suhaib Abdurahman*
Zhivar Sourati†
Jackson Trager
Morteza Dehghani
University of Southern California
{karimima,sabdurah,souratih,jptrager,mdehghan}@usc.edu
Abstract
Socio-cognitive benchmarks for large language
models (LLMs) often fail to predict real-world
behavior, even when models achieve high
benchmark scores. Prior work has attributed
this evaluation–deployment gap to problems
of measurement and validity. While these cri-
tiques are insightful, we argue that they over-
look a more fundamental issue: many socio-
cognitive evaluations proceed without an ex-
plicit theoretical specification of the target ca-
pability, leaving the assumptions linking task
performance to competence implicit. Without
this theoretical grounding, benchmarks that ex-
ercise only narrow subsets of a capability are
routinely misinterpreted as evidence of broad
competence: a gap that creates a systemic valid-
ity illusion by masking the failure to evaluate
the capability’s other essential dimensions. To
address this gap, we make two contributions.
First, we diagnose and formalize this theory
gap as a foundational failure that undermines
measurement and enables systematic overgen-
eralization of benchmark results. Second, we
introduce the THEORY TRACE CARD (TTC), a
lightweight documentation artifact designed to
accompany socio-cognitive evaluations, which
explicitly outlines the theoretical basis of an
evaluation, the components of the target capa-
bility it exercises, its operationalization, and
its limitations. We argue that TTCs enhance
the interpretability and reuse of socio-cognitive
evaluations by making explicit the full validity
chain, which links theory, task operationaliza-
tion, scoring, and limitations, without modify-
ing benchmarks or requiring agreement on a
single theory.
1
Introduction
In May 2023, the helpline chatbot “Tessa” was
withdrawn shortly after deployment (Reddy and
*Equal contribution.
†Equal contribution.
Reddy, 2025). Introduced by the National Eat-
ing Disorder Association to support individuals in
vulnerable situations, the system instead produced
harmful responses, including advice about “weight
loss” and “daily calorie deficits” that directly
contradicted the organization’s mission (Wheeler,
2024; Sharp et al., 2023).
In the aftermath,
displaced staff offered a blunt assessment that
“perhaps human empathy is best left to human-
ity” (Torous and Blease, 2024).
Failures such as Tessa point to an important prob-
lem. Performance on widely used socio-cognitive
evaluation benchmarks does not reliably predict
how systems behave in real-world social settings.
This mismatch is especially consequential because
large language models (LLMs) are deployed in
high-stakes social settings that require human-
like socio-cognitive capabilities, including mental
health chatbots, self-harm prevention tools, and
systems that offer advice about morally sensitive
decisions (Kang et al., 2024; Gandhi et al., 2023).
When systems fail in precisely the contexts that
their evaluations are intended to anticipate, the eval-
uation process itself must be called into question.
A growing body of work has argued that one
of the reasons for this evaluation gap is the prob-
lem of measurement and validity. Drawing on tra-
ditions in psychometrics, these critiques empha-
size issues such as benchmark construction, dataset
bias, and the limits of inference from aggregate
scores (Riemer et al., 2024; Bean et al., 2025;
Wallach et al., 2025; Jacobs and Wallach, 2021).
Within this framework, measurement claims are
understood to depend on multiple forms of valid-
ity, including construct validity and the assump-
tions linking observed performance to latent ca-
pacities (Messick, 1995; Borsboom et al., 2004;
Cronbach and Meehl, 1955).
Here, we argue that while these critiques are in-
sightful, they presuppose a prior requirement for
valid measurement that is often left unexamined:
arXiv:2601.01878v1  [cs.AI]  5 Jan 2026

--- Page 2 ---

an explicit theoretical specification of the target
capability itself. Questions of measurement qual-
ity and construct validity depend on assumptions
about what is being measured. When the theoreti-
cal structure of a social capability is left implicit,
it becomes unclear what benchmark performance
is intended to support. As a result, benchmarks are
often treated as if they define the capability they
are meant to measure. In practice, this leads to
a reactive and incremental pattern of benchmark
development, where new benchmarks are intro-
duced primarily to address specific failures, edge
cases, or blind spots identified in prior benchmarks,
rather than to systematically cover the structure
of the underlying capability. While this process
can yield increasingly specialized evaluations, it
also fragments empirical findings across narrowly
scoped tasks, making it difficult to integrate re-
sults into a coherent account of the broader capabil-
ity. The field thus accumulates benchmark-specific
improvements without a principled basis for gen-
eralization, encouraging intermediate conclusions
based on inherently incomplete and task-defined
specifications.
In contrast to this fragmented approach, ground-
ing benchmark design in socio-cognitive theory
allows researchers to treat social abilities as mul-
tidimensional constructs. This situates individual
test results within a nomological network (Cron-
bach and Meehl, 1955), a web of relationships that
makes performance predictable and generalizable
beyond the task itself. Making theoretical commit-
ments explicit allows evaluation to be scoped and
constrained a priori, guiding interpretation accord-
ing to an established conceptual structure rather
than an ad hoc, benchmark-by-benchmark process.
Consequently, benchmarks can probe various di-
mensions of a target capability in a coordinated
manner, supporting cumulative scientific progress
grounded in coherent foundations.
1.1
The Role of Theory in Socio-Cognitive
Evaluation
To give some concrete examples of what we mean
by the role of theory in evaluation, consider how
several widely used social capabilities are currently
assessed in the literature.
Theory-of-Mind.
From a psychological perspec-
tive, Theory of Mind (ToM) is commonly under-
stood as comprising multiple components rather
than a unitary ability. A standard distinction sepa-
rates cognitive ToM—the capacity to represent and
reason about others’ beliefs, intentions, and knowl-
edge states—from affective ToM, which involves
understanding others’ emotions, feelings, and so-
cial motivations (Apperly and Butterfill, 2009;
Shamay-Tsoory and Aharon-Peretz, 2012; Corradi-
Dell’Acqua et al., 2013; Raimo et al., 2022). Most
existing ToM evaluations for language models fo-
cus on narrative false-belief tasks, adapted from
developmental psychology and introduced in NLP
by Nematzadeh et al. (2018) and Le et al. (2019),
with later variants such as Hi-ToM and Open-ToM
(Wu et al., 2023; Xu et al., 2024). In these tasks, a
model is given a short narrative and asked to pre-
dict an agent’s belief when that belief diverges from
reality, testing its ability to represent mental states
and distinguish one’s own beliefs from those of oth-
ers (Wimmer and Perner, 1983). High performance
on these tasks is then seen as evidence for general
ToM or social reasoning capabilities (e.g., Kosinski,
2024; Bubeck et al., 2023). However, theoretically,
false-belief reasoning only relates to cognitive ToM.
These benchmarks and evaluations thus implicitly
limit ToM to cognitive ToM or assume generaliza-
tion to other components of the ToM framework,
such as affective understanding, sensitivity to social
context, and the use of mental-state information to
guide behavior. Without the explicit theoretical ac-
counts that clarify the multi-component structure
and how the benchmark targets it, these evaluations
can easily lead to over-broad claims and misleading
interpretations.
Empathy.
Widely used benchmarks such as Dai-
lyDialog (Li et al., 2017), EmpatheticDialogues
(Rashkin et al., 2019), EmotionQueen (Chen et al.,
2024), and EmotionBench (Huang et al., 2024) op-
erationalize empathy primarily through emotion
recognition or emotion-conditioned response gen-
eration. Models that correctly identify that a user
is “sad” or “anxious” or respond with aligned emo-
tionality are therefore described as empathetic. For
example, EmpatheticDialogues describes empa-
thy as “understanding and acknowledging any im-
plied feelings” and evaluates empathy via unidi-
mensional ratings of whether “speakers’ responses
show understanding of the feelings of the person
talking” (Rashkin et al., 2019), while Emotion-
Bench defines empathy as an “ability of LLMs,
i.e., how their feelings change when presented with
specific situations” (Huang et al., 2024). However,
psychological theory distinguishes emotion recog-

--- Page 3 ---

nition from empathic concern, an other-oriented
motivation to support or help (Batson et al., 1997;
Zaki and Ochsner, 2012), and treats empathy as
multi-component (e.g., cognitive vs. affective vs.
compassionate; and dissociations such as empathic
concern vs. personal distress; Decety and Lamm,
2006, 2011). When evaluations do not explicitly
commit to a theoretical account and instead col-
lapse components or conflate empathy with adja-
cent concepts (Rashkin et al., 2019; Chen et al.,
2024; Huang et al., 2024; Hong et al., 2025; We-
livita and Pu, 2024), they can mislead as capturing
empathy, even though they only reflect narrow as-
pects or proxy capacities (illustration in Figure 1).
Moral Reasoning.
Prominent evaluations such
as ETHICS (Hendrycks et al., 2021) often opera-
tionalize moral reasoning as predicting perceived
appropriateness, categorizing moral concepts (e.g.,
fairness, justice), or producing an “appropriate” re-
sponse to a moral scenario. Newer benchmarks di-
versify these operationalizations but still tie moral-
ity to particular normative or psychological lenses:
MoralBench (Ji et al., 2025) and CMoralEval (Yu
et al., 2024) ground evaluation in Moral Founda-
tions Theory (Haidt and Graham, 2007; Graham
et al., 2013); MORABLES (Marcuzzo et al., 2025)
evaluates identifying moral lessons in (Western) fa-
bles; the Greatest Good Benchmark (Marraffini
et al., 2024) compares model and human judg-
ments on utilitarian dilemmas; AgentHarm (An-
driushchenko et al., 2024) emphasizes harm avoid-
ance; and Scherrer et al. (2023) probe moral beliefs
using scenarios drawn from multiple moral theories.
High performance is then interpreted as evidence
of general moral competence. Yet moral psychol-
ogy offers competing accounts of moral reasoning,
from pluralistic frameworks such as Moral Foun-
dations Theory (Haidt and Graham, 2007; Graham
et al., 2013) to harm-centered accounts such as
the Theory of Dyadic Morality (Gray et al., 2012;
Schein and Gray, 2018), among others. Any bench-
mark, therefore, embeds substantive assumptions
about what morality is and which distinctions mat-
ter. Benchmarks that focus primarily on harm, for
instance, effectively privilege one theoretical ac-
count over others. More broadly, when these the-
oretical commitments are left implicit, results are
easily overgeneralized: competence under a par-
ticular operationalization (e.g., harm avoidance,
utilitarian tradeoffs, endorsement of specific foun-
dations, extracting fable morals) is mistaken for
broad moral reasoning ability, even though it may
reflect only one slice of a heterogeneous construct.
1.1.1
Present work
These examples illustrate a general problem in
the design and interpretation of social evaluation
benchmarks. The issue is not that the tasks are
poorly constructed or incorrectly measured. Rather,
benchmarks routinely rely on implicit theories of
what a capability consists of, which components
matter, and how task performance should general-
ize beyond the evaluation setting.
This paper addresses this gap by providing both
a theoretical diagnosis of current evaluation failures
and a practical path forward. First, we character-
ize the systemic validity illusion—a phenomenon
where the absence of explicit theory allows narrow
benchmark performance to be misinterpreted as ev-
idence of broad social competence. We argue that
this “theory gap” is not merely a reporting over-
sight but a logical failure that renders measurement
claims groundless, as there is no principled basis
for determining what a score represents or how it
should generalize. To address this, we introduce
the THEORY TRACE CARD (TTC), a lightweight
reporting instrument designed to make the theo-
retical assumptions underlying social evaluations
explicit. The TTC records how a target capability
is defined, which components are exercised by a
benchmark, and what forms of inference the eval-
uation results can and cannot support. By doing
so, it enables more interpretable use of existing
benchmarks without requiring agreement on a sin-
gle theory or invalidating prior work. Finally, we
discuss broader implications for evaluation prac-
tice, advocating for a shift from “evaluation by
leaderboard” toward “evaluation by argument”.
2
Consequences of Implicit Theory in
Socio-Cognitive Evaluation
At a theoretical level, the core problem is a sys-
tematic pattern of under-specification in socio-
cognitive evaluation. When theoretical assump-
tions are left implicit, benchmark results are rou-
tinely asked to support claims they were never de-
signed to justify. This under-specification takes
several recurring forms in the literature: (i) some
benchmarks rely primarily on task labels or folk
definitions of complex socio-cognitive capacities,
without reference to any formal theory; (ii) others
cite an explicit theoretical framework, but do not

--- Page 4 ---

Figure 1: Collapsing Social Capabilities in Benchmark Evaluation. Theoretical constructs (left), such as empathy,
are multidimensional, composed of distinct and often orthogonal components like Empathic Concern (motivation
to help) and Personal Distress (self-oriented anxiety). When evaluation relies on a low-dimensional benchmark
(right), this complex state space is collapsed into a single scalar metric. As a result, qualitatively distinct behavioral
profiles—such as safe compassion (blue) versus harmful distress-based mirroring (red)—receive indistinguishable
scores, creating a validity illusion that can mask unsafe model behavior.
specify which components of that framework are
exercised by the task; (iii) still others articulate
multiple theoretical components, but leave the rela-
tions among those components, as well as the con-
ditions under which task performance is expected
to generalize, implicit; and (iv) across all of these
cases, the limits of extrapolating benchmark scores
to real-world behavior and deployment contexts
remain underspecified. Overall, these gaps allow
benchmark scores to function as default evidence
of broad competence in the absence of an explicit
theoretical argument linking task performance to
the target capability and its use outside the evalua-
tion setting (Messick, 1995; Cronbach and Meehl,
1955; Riemer et al., 2024). Because such assump-
tions are reused, cited, and operationalized across
evaluation pipelines, their effects compound, shap-
ing research claims, deployment decisions, and
user expectations. The rest of this section exam-
ines how this shared theoretical under-specification
manifests differently for researchers, practitioners,
and the users who are impacted.
Researchers and Scientific Progress.
For re-
searchers,
implicit
theory
distorts
scientific
progress in the evaluation of socio-cognitive ca-
pabilities.
Many such benchmarks operational-
ize only a narrow subset of a theoretically multi-
structured construct while leaving the underlying
theoretical commitments and omitted components
unstated. When this happens, improvements in
benchmark performance are often interpreted as ev-
idence of progress on the broader capability, even
though the scope of what is being exercised by the
task remains unchanged (Lipton and Steinhardt,
2019; Yarkoni, 2022). Over time, these partial op-
erationalizations can come to define the construct
itself within the field, shaping both research pri-
orities and claims of advancement. Benchmark
saturation compounds this problem in theory-laden
social evaluations. As scores approach the ceil-
ing, high performance is often interpreted as ev-
idence that a complex social capability has been
“solved” or that models have achieved human-level
performance (Dillion et al., 2023; Ott et al., 2022;
Van Duijn et al., 2023). However, audits of sat-
urated socio-cognitive benchmarks suggest that
such claims frequently reflect the exhaustion of
task-specific regularities rather than comprehen-
sive coverage of the theoretical construct (Fodor,
2025). This distortion is further reinforced when

--- Page 5 ---

progress is assessed through relative benchmark
rank or score, as is common in leaderboard-based
evaluation, where models are compared based on
their aggregate performance on a fixed set of tasks.
For social-cognitive evaluations that are implicitly
grounded in a particular theoretical understanding
of a capability, rank alone obscures which compo-
nents of that theory are being exercised and which
are not. Optimization pressure then shifts toward
aspects of the construct that are easiest to opera-
tionalize in such tasks, rather than those that are
theoretically central or predictive of real-world so-
cial behavior (Ethayarajh and Jurafsky, 2020; Lip-
ton and Steinhardt, 2019). These dynamics make
it difficult to compare results across evaluations
that nominally target the same social construct, to
diagnose failures outside benchmark settings
Practitioners and Deployment.
For practition-
ers and organizations, implicit theory creates con-
crete evaluation and deployment risk. Teams re-
sponsible for assessing model readiness routinely
rely on benchmark results to decide whether a sys-
tem can be used in high-stakes settings (Amodei
et al., 2016; Jacobs et al., 2021). When bench-
marks are labeled with socially meaningful capa-
bilities such as “empathy,” “moral reasoning,” or
“Theory of Mind,” strong performance is often in-
terpreted as evidence that the corresponding risks
have been evaluated and mitigated. Such inter-
pretations are unwarranted unless the theoretical
scope of the benchmark is explicit. Interpreting
evaluation results requires a justified chain of infer-
ences—from scoring (what the metric captures), to
generalization (what domain the test represents), to
extrapolation (what real-world behavior the score
predicts) (Kane, 2013). When this chain remains
implicit, benchmark results may support claims
about performance on stylized tasks while provid-
ing no principled evidence about behavior in the tar-
get deployment context. Systems may be deployed
into settings that require capacities that were never
actually evaluated, with failures appearing surpris-
ing only because the limits of the evaluation were
never made visible.
Users and Impacted Communities.
For users
and impacted communities, the consequences are
both practical and epistemic. Public claims that
models possess socio-cognitive capabilities shape
expectations about how these systems will behave
in interaction (Quattrociocchi et al., 2025).
When benchmarks lack explicit theoretical speci-
fication, they create a misleading impression of uni-
versality that directly affects users: models appear
competent across social and cultural contexts, even
when evaluations operationalize culturally specific
constructs. This exacerbates WEIRD (Western,
Educated, Industrialized, Rich, and Democratic)
bias in AI evaluation (Tao et al., 2024; Atari et al.,
2023b). While models are widely known to be
trained on disproportionately WEIRD data, this
bias is compounded at evaluation time, as bench-
marks often rely on psychological theories de-
veloped and tested primarily in WEIRD contexts
(Henrich et al., 2010).
As a result, users en-
counter systems whose benchmark-certified “so-
cial” or “moral” competence reflects alignment
with WEIRD cultural logics but is presented as
broadly applicable. For example, treating “moral-
ity” as interpersonal harm (Schein and Gray, 2018)
obscures forms of moral judgment grounded in
honor (Razavi et al., 2023; Atari et al., 2020) or
sanctity (Atari et al., 2023a) that are central in
many non-WEIRD societies. Without transparent
documentation of what evaluations do and do not
establish, affected individuals lack a basis for un-
derstanding unexpected system behavior, attribut-
ing responsibility, or meaningfully contesting de-
cisions made based on benchmark performance
(Jacobs and Wallach, 2021).
3
Theory Trace Card
The Theory Trace Card (TTC) is a structured doc-
umentation artifact designed to accompany socio-
cognitive evaluations. Its purpose is to make ex-
plicit the theoretical and measurement assump-
tions that evaluation practices already rely on
but rarely articulate. We argue that TTCs can be
used in two complementary ways: (i) by bench-
mark creators, to document the theoretical ground-
ing and intended scope of a benchmark at design
and publication time; and (ii) by researchers, prac-
titioners, and auditors, to make explicit the assump-
tions underlying their evaluations and their interpre-
tation of results. Providing TTCs alongside bench-
mark papers and evaluation papers supports more
disciplined interpretation, clarifies the claims that
scores are intended to support, and enables prin-
cipled comparison across evaluations that target
similar capabilities under different theoretical and
operational commitments. In doing so, it shifts the
evaluation infrastructure from simplistic compar-
isons to evaluation by argument.

--- Page 6 ---

The TTC is motivated by argument-based ap-
proaches to validity, particularly Kane’s framework
(Kane, 2013). Kane’s central insight was that va-
lidity does not reside in tests or scores themselves,
but in the interpretive arguments that connect ob-
served performance to the conclusions drawn from
it.
While this perspective has been influential
in psychometrics, its implications have remained
largely absent in the context of modern machine
learning benchmarks, where evaluation artifacts
rarely make their inferential assumptions explicit.
In Kane’s account, evaluation depends on a chain
of inferences, including scoring inference (from re-
sponses to scores), generalization inference (from
sampled items to an intended task domain), and
extrapolation inference (from task performance to
claims about behavior or capability beyond the test
setting). Kane’s framework provides a powerful
lens for diagnosing validity problems, but does
not prescribe how these inferential commitments
should be represented or documented in practice.
This gap is particularly salient for socio-
cognitive evaluation in LLMs. Benchmarks in this
domain are frequently used as stand-ins for com-
plex psychological or normative constructs despite
substantial differences in theory choice, task design,
and scoring procedures. As emphasized in the va-
lidity literature, many threats to interpretation arise
not from theory alone, but from misalignments
between theoretical constructs, task operationaliza-
tion, and scoring (Messick, 1995; Borsboom et al.,
2004; Cronbach and Meehl, 1955). Yet, existing
evaluation practices rarely provide a unified repre-
sentation of these elements.
The TTC addresses this gap by translating the
inferential structure highlighted by Kane into a con-
crete, reusable artifact. Rather than treating theory,
task design, and scoring as separate concerns, the
TTC integrates them into a single card that docu-
ments (i) how a target capability is theoretically
defined, (ii) which components of that capability
are exercised by the evaluation, (iii) how those
components are operationalized through task de-
sign, and (iv) how task performance is interpreted
through scoring. In this way, the TTC supports the
full validity cycle, from theoretical specification,
through task operationalization and scoring, to the
interpretation and reuse of evaluation results.
3.1
Design Principles
The TTC is guided by three design principles.
First, it is descriptive rather than normative. It
records the theoretical commitments an evaluation
makes without requiring consensus on a single the-
ory or adjudicating between competing accounts.
Second, it is lightweight. Completing a TTC should
require minimal additional effort beyond what is
already necessary to design and report an evalua-
tion. The goal is to improve interpretability and
usability without raising the barrier to proposing,
reproducing, or applying benchmarks.
Third, it is compatible with existing benchmarks.
The TTC can be applied both retrospectively and
prospectively. It does not require benchmarks to be
redesigned or re-scored; instead, it clarifies how ex-
isting evaluations should be interpreted and which
claims their results can support.
3.2
Core Components
The TTC consists of four core components, summa-
rized in the TTC template shown in Card 1. Each
component corresponds to a distinct point in the in-
ferential chain linking task performance to claims
about socio-cognitive capabilities.
Theory.
This component specifies how the tar-
get capability is understood for the purposes of the
evaluation. Authors should state the theoretical
framework, account, or construct definition that the
benchmark adopts, and briefly describe how that
framework characterizes the capability, including
any core components or sub-capabilities it posits.
Where relevant, authors may also note assumed
processes or dependencies among components, as
well as the broader nomological network in which
the capability is situated (e.g., related constructs,
expected correlations, or dissociations). This com-
ponent fixes the conceptual object of evaluation
and makes explicit the theoretical commitments on
which subsequent interpretation depends.
Components Exercised.
This component iden-
tifies which theoretical components, under the
adopted framework, the evaluation task is intended
to exercise. By requiring authors to enumerate the
components targeted by the task, this section clar-
ifies which aspects of the broader capability are
directly probed by the evaluation, without requir-
ing an exhaustive enumeration of components that
fall outside the task’s scope.
Task Operationalization.
This component ex-
plains how the evaluation task operationalizes
the exercised components.
Authors should de-
scribe what the model is required to do given the

--- Page 7 ---

task input, along with any key design specifica-
tions—such as prompt structure, response format,
interaction constraints, or generation limits—that
shape the model’s degrees of freedom. Crucially,
this section makes explicit the scoring criterion:
how model performance is evaluated. It should
describe the criteria used to score responses (e.g.,
rubric-based ratings, LLM-based evaluators), in-
cluding any aggregation procedures where relevant.
By making scoring procedures explicit, this com-
ponent completes the inferential chain from task
performance to interpretable benchmark outcomes.
Inference and Limitations.
This section demon-
strates how task performance is considered as ev-
idence of the exercised component(s) under the
adopted theoretical framework and its limitations,
as well as those related to the operationalization,
similar to the limitations outlined in evaluation or
benchmark papers. Rather than requiring authors
to anticipate all possible unintended strategies, this
documentation clarifies the intended mapping from
task behavior to theoretical components.
Card 1: Theory Trace Card (TTC) Template
1. Theory
• Framework: Name of socio-cognitive theory
/ construct framework + citation(s).
• Core components:
List components/sub-
capabilities posited by the framework (brief).
2. Components Exercised
• List the specific theoretical components the
evaluation is intended to exercise.
3. Task Operationalization
• Task: Describe required behavior given the
task input.
• Key specs: E.g., prompt template/response
format; interaction/generation limits
• Scoring criterion: How performance is eval-
uated (e.g., label agreement, preference judg-
ments, aggregation)
4. Inference and Limitations
• How performance is treated as evidence of
the exercised component(s).
• Limitations based on theory and operational-
ization.
4
Worked Examples: Empathy and
Moral Reasoning Evaluations
Cards 2 and 3 present completed Theory Trace
Cards for a hypothetical empathy evaluation and
a Moral Foundations Theory–based moral reason-
ing evaluation. In the empathy example, the TTC
explicitly states that the evaluation relies on a com-
ponential understanding of empathy, while exer-
cising only the Perspective-Taking component. In
the moral reasoning example, the TTC records that
the evaluation adopts Moral Foundations Theory
and exercises judgments aligned with the Fairness
foundation within moral scenarios.
Card 2: Empathy Evaluation
1. Theory
• Framework: Functional architecture of human empa-
thy (Decety and Jackson, 2004; Lietz et al., 2011)
• Core components: Affective response (sharing); Self–
other awareness; Perspective taking; Emotion regula-
tion
2. Components Exercised
• Perspective Taking
3. Task Operationalization
• Task: Predict an explicit emotion label given a short
textual description of a speaker’s situation.
• Key specifications: Fixed prompt; closed-set emotion
labels; no interaction, context accumulation, or justifi-
cation.
• Scoring criterion: Agreement between model predic-
tions and predefined emotion categories.
4. Inference and Limitations
• Performance supports the Perspective Taking compo-
nent of empathy.
• Affective Sharing, Self–Other Awareness, and Emotion
Regulation are not evaluated by the task.
• The emotion taxonomy and labels may reflect WEIRD
cultural assumptions; cross-cultural generalization is
not established.
The TTC separates four elements that are of-
ten conflated in benchmark interpretation: (i) how
the target capability is theoretically specified, (ii)
which components of that capability are targeted,
(iii) how task design and scoring operationalize
those components, and (iv) how performance is in-
terpreted and constrained. Making these elements
explicit shows how evaluations that are frequently
treated as measures of broad socio-cognitive abil-
ities in fact support narrower, theory-dependent
claims, and how the TTC enables more disciplined
interpretation and reuse of benchmark results with-
out modifying tasks, datasets, or reported scores.
To demonstrate that the TTC can also be applied
retrospectively, Appendix A includes completed
TTCs for several widely used existing benchmarks,
including EmpatheticDialogues (Rashkin et al.,
2019), false-belief Theory of Mind evaluations
(e.g., Kosinski, 2024), the ETHICS moral reasoning
benchmark (Hendrycks et al., 2021), GoEmotions
(Demszky et al., 2020), and SocialIQA (Sap et al.,

--- Page 8 ---

2019). These examples demonstrate how the TTC
can be instantiated post hoc to reveal theoretical
commitments, component coverage, and the limits
of inference—without modifying datasets, tasks, or
scoring procedures.
Card 3: Moral Reasoning Evaluation
1. Theory
• Framework: Moral Foundations Theory (Graham et
al., 2013)
• Core components: Care; Fairness; Loyalty; Authority;
Purity
2. Components Exercised
• Fairness
3. Task Operationalization
• Task: Endorse the action aligned with the Fairness
foundation given a moral scenario.
• Key specs: Scenario template; comparative judgment.
• Scoring criterion: Agreement between model judg-
ments and human responses.
4. Inference and Limitations
• Performance supports reasoning aligned with the Fair-
ness foundation in MFT.
• Fairness in MFT is an aggregate of two justice con-
cerns (equality and proportionality), limiting inference
to where this distinction doesn’t matter.
• Limited cross-cultural generalization.
5
Discussion
In this paper, we advance the evaluation literature
with two central contributions. First, we provide a
theoretical diagnosis of a current gap in the evalua-
tion of socio-cognitive capabilities in LLMs. We
argue that many widely used benchmarks implic-
itly rely on substantive theoretical accounts of com-
plex constructs while leaving those accounts un-
specified, enabling shortcut solutions or proxy opti-
mization to masquerade as genuine capability gains
(Geirhos et al., 2020; Abdurahman et al., 2024). As
a result, benchmark performance can be overgen-
eralized, with task success taken to support claims
about broad real-world capabilities that the evalu-
ation does not, in fact, exercise. This gap is not
primarily a problem of data quality or modeling
technique, but of unarticulated theory: measure-
ment proceeds without a fixed account of what is
being measured or how task performance licenses
downstream claims, a pattern long recognized as
a threat to construct validity in the behavioral sci-
ences (Meehl, 1990; Haig, 2018).
Second, we introduce the TTC as a lightweight
piece of evaluation infrastructure designed to ad-
dress this gap. The TTC provides a structured ap-
proach to documenting how a target capability is
defined for the purposes of evaluation, including
which components of that definition are exercised
by a task, how those components are operational-
ized in prompts and scoring, and the scope of in-
ference that evaluation results are intended to sup-
port. We recommend that TTCs accompany socio-
cognitive evaluations, including benchmark design
and the use of benchmark results for evaluation.
By making explicit the inferential assumptions that
link task performance to claims about capability,
across scoring, generalization, and extrapolation,
the TTC supports more disciplined interpretation
and reuse of benchmark results without requiring
agreement on a single theory or invalidating prior
work.
Importantly, the TTC does not impose a single
definition of any socio-cognitive capability. Dif-
ferent researchers may adopt different theoretical
frameworks or emphasize different components of
the same construct. The role of the TTC is not to
adjudicate between these views, but to record them
in a comparable and explicit form. This makes the-
oretical disagreement visible and traceable, rather
than implicit in task design, benchmark naming, or
informal interpretation.
While our worked examples focus on empathy
and moral reasoning, they are intended to illustrate
how a TTC can be constructed prospectively, along-
side the design of a new benchmark, since any eval-
uation that supports claims beyond the test setting
relies on assumptions about how task performance
relates to a target capability.
More broadly, this work argues that theory
choice in evaluation is not optional but inevitable.
Socio-cognitive benchmarks already embed theo-
retical commitments. The choice facing the field is
whether those commitments remain implicit, lim-
iting interpretability and encouraging overgeneral-
ization, or are made explicit, open to scrutiny, and
subject to refinement. By shifting the interpretive
burden from readers and downstream users to the
evaluation itself, the TTC promotes more reliable,
cumulative, and responsible use of benchmark re-
sults. We argue that such explicitness is a necessary
condition for progress in evaluating complex socio-
cognitive capabilities in language models.
6
Limitations
There are some limitations regarding the utility and
applicability of TTC that constrain the extent to
which a TTC facilitates correct interpretation and
generalization of LLM capabilities and subsequent

--- Page 9 ---

downstream use and deployment. Making theo-
retical assumptions explicit does not ensure that
those assumptions are accurate, nor does it elim-
inate judgment calls in how a card is completed.
Different authors may reasonably fill out the same
TTC differently, reflecting genuine theoretical dis-
agreement about how a capability should be defined
or decomposed. However, such disagreement in
TTC completion is itself informative, surfacing the-
oretical divergence that is otherwise implicit. In ad-
dition, because the TTC relies on human construct
concepts to structure interpretation, it does not by
itself prevent anthropomorphic readings of model
behavior or determine whether a given construct
framework is appropriate for describing machine
behavior. The TTC constrains what claims are sup-
ported by an evaluation under stated assumptions,
but it does not adjudicate between competing the-
ories. As with other documentation practices, the
TTC is most effective when used alongside com-
plementary evaluation methods, such as targeted
stress tests or audits that probe claims extending
beyond a benchmark’s stated scope.
References
Suhaib Abdurahman, Mohammad Atari, Farzan Karimi-
Malekabadi, Mona J Xue, Jackson Trager, Peter S
Park, Preni Golazizian, Ali Omrani, and Morteza De-
hghani. 2024. Perils and opportunities in using large
language models in psychological research. PNAS
nexus, 3(7):pgae245.
Dario Amodei, Chris Olah, Jacob Steinhardt, Paul
Christiano, John Schulman, and Dan Mané. 2016.
Concrete problems in ai safety.
arXiv preprint
arXiv:1606.06565.
Maksym Andriushchenko, Alexandra Souly, Mateusz
Dziemian, Derek Duenas, Maxwell Lin, Justin
Wang, Dan Hendrycks, Andy Zou, Zico Kolter, Matt
Fredrikson, and 1 others. 2024. Agentharm: A bench-
mark for measuring harmfulness of llm agents. arXiv
preprint arXiv:2410.09024.
Ian A Apperly and Stephen A Butterfill. 2009.
Do
humans have two systems to track beliefs and belief-
like states? Psychological review, 116(4):953.
Aristotle. 340 BC. Nicomachean Ethics.
Mohammad Atari, Jesse Graham, and Morteza De-
hghani. 2020. Foundations of morality in iran. Evo-
lution and Human behavior, 41(5):367–384.
Mohammad Atari, Jonathan Haidt, Jesse Graham, Sena
Koleva, Sean T Stevens, and Morteza Dehghani.
2023a.
Morality beyond the weird:
How the
nomological network of morality varies across cul-
tures. Journal of Personality and Social Psychology,
125(5):1157.
Mohammad Atari, Mona Xue, Peter Park, Damián Blasi,
and Joseph Henrich. 2023b. Which humans?
C. Daniel Batson and 1 others. 1997. Distress and em-
pathy: Two qualitatively distinct vicarious emotions
with different motivational consequences. Journal of
Personality, 65(1):91–121.
Andrew M. Bean, Ryan Othniel Kearns, Angelika Ro-
manou, Franziska Sofia Hafner, Harry Mayne, Jan
Batzner, Negar Foroutan Eghlidi, Chris Schmitz,
Karolina Korgul, Hunar Batra, Oishi Deb, Emma Be-
harry, Cornelius Emde, Thomas Foster, Anna Gausen,
María Grandury, Simeng Han, Valentin Hofmann, Lu-
jain Ibrahim, and 23 others. 2025. Measuring what
matters: Construct validity in large language model
benchmarks. In Proceedings of the NeurIPS 2025
Datasets and Benchmarks Track.
Denny Borsboom, Gideon J Mellenbergh, and Jaap
Van Heerden. 2004. The concept of validity. Psycho-
logical review, 111(4):1061.
Sébastien Bubeck, Varun Chandrasekaran, Ronen Eldan,
Johannes Gehrke, Eric Horvitz, Ece Kamar, Peter
Lee, Yin Tat Lee, Yuanzhi Li, Scott Lundberg, and
1 others. 2023. Sparks of artificial general intelli-
gence: Early experiments with gpt-4. arXiv preprint
arXiv:2303.12712.
Yuyan Chen, Hao Wang, Songzhou Yan, Sijia Liu,
Yueze Li, Yi Zhao, and Yanghua Xiao. 2024.
Emotionqueen: A benchmark for evaluating em-
pathy of large language models.
arXiv preprint
arXiv:2409.13359.
C. Corradi-Dell’Acqua and 1 others. 2013. Cognitive
and affective theory of mind share the same local but
not the same global functional architecture: Evidence
from lesion studies. Social Cognitive and Affective
Neuroscience, 8(3):234–242.
Alan S Cowen and Dacher Keltner. 2017. Self-report
captures 27 distinct categories of emotion bridged by
continuous gradients. Proceedings of the national
academy of sciences, 114(38):E7900–E7909.
Lee J. Cronbach and Paul E. Meehl. 1955. Construct va-
lidity in psychological tests. Psychological Bulletin,
52:281–302.
Katarzyna de Lazari-Radek and Peter Singer. 2017. Util-
itarianism: A very short introduction, volume 530.
Oxford University Press.
Jean Decety and Philip L Jackson. 2004. The func-
tional architecture of human empathy. Behavioral
and cognitive neuroscience reviews, 3(2):71–100.
Jean Decety and Claus Lamm. 2006. Human empathy
through the lens of social neuroscience. The scientific
World journal, 6(1):1146–1163.

--- Page 10 ---

Jean Decety and Claus Lamm. 2011. 15 empathy ver-
sus personal distress: Recent evidence from social
neuroscience. The social neuroscience of empathy,
page 199.
Dorottya Demszky, Dana Movshovitz-Attias, Jeongwoo
Ko, Alan Cowen, Gaurav Nemade, and Sujith Ravi.
2020. Goemotions: A dataset of fine-grained emo-
tions. arXiv preprint arXiv:2005.00547.
Danica Dillion, Niket Tandon, Yuling Gu, and Kurt Gray.
2023. Can ai language models replace human partici-
pants? Trends in Cognitive Sciences, 27(7):597–600.
Kawin Ethayarajh and Dan Jurafsky. 2020. Utility is in
the eye of the user: A critique of nlp leaderboards.
arXiv preprint arXiv:2009.13888.
James Fodor. 2025. Line goes up? inherent limitations
of benchmarks for evaluating large language models.
arXiv preprint arXiv:2502.14318.
Kanishk Gandhi, Jan-Philipp Fränken, Tobias Gersten-
berg, and Noah Goodman. 2023.
Understanding
social reasoning in language models with language
models. Advances in Neural Information Processing
Systems, 36:13518–13529.
Robert
Geirhos,
Jörn-Henrik
Jacobsen,
Claudio
Michaelis,
Richard
Zemel,
Wieland
Brendel,
Matthias Bethge, and Felix A Wichmann. 2020.
Shortcut learning in deep neural networks. Nature
Machine Intelligence, 2(11):665–673.
Jesse Graham, Jonathan Haidt, Spassena Koleva, Mislav
Motyl, Ravi Iyer, Sean Wojcik, and Peter H. Ditto.
2013. Moral foundations theory: The pragmatic va-
lidity of moral pluralism. Advances in Experimental
Social Psychology, 47:55–130.
Kurt Gray, Liane Young, and Adam Waytz. 2012. The
moral dyad: A fundamental template unifying moral
judgment. Psychological Inquiry, 23(2):206–215.
Jonathan Haidt and Jesse Graham. 2007. When morality
opposes justice: Conservatives have moral intuitions
that liberals may not recognize. Social Justice Re-
search, 20(1):98–116.
Brian D Haig. 2018. An abductive theory of scientific
method. In Method matters in psychology: Essays in
applied philosophy of science, pages 35–64. Springer.
Dan Hendrycks and 1 others. 2021. Aligning ai with
shared human values. In ICLR.
Joseph Henrich, Steven J. Heine, and Ara Norenzayan.
2010. The weirdest people in the world? Behavioral
and Brain Sciences, 33(2–3):61–83.
Cecilia M Heyes and Chris D Frith. 2014.
The
cultural evolution of mind reading.
Science,
344(6190):1243091.
Yuna Hong, Bonhwa Ku, and Hanseok Ko. 2025. Per-
formance evaluation metrics for empathetic llms. In-
formation, 16(11):977.
Jen-tse Huang, Man Ho Lam, Eric John Li, Shujie Ren,
Wenxuan Wang, Wenxiang Jiao, Zhaopeng Tu, and
Michael R Lyu. 2024. Apathetic or empathetic? eval-
uating llms’ emotional alignments with humans. Ad-
vances in Neural Information Processing Systems,
37:97053–97087.
Abigail Z. Jacobs and Hanna Wallach. 2021. Measure-
ment and fairness. FAccT.
Maia Jacobs, Jeffrey He, Melanie F. Pradier, Barbara
Lam, Andrew C Ahn, Thomas H McCoy, Roy H
Perlis, Finale Doshi-Velez, and Krzysztof Z Gajos.
2021. Designing ai for trust and collaboration in
time-constrained medical decisions: a sociotechnical
lens. In Proceedings of the 2021 chi conference on
human factors in computing systems, pages 1–14.
Jianchao Ji, Yutong Chen, Mingyu Jin, Wujiang Xu,
Wenyue Hua, and Yongfeng Zhang. 2025. Moral-
bench: Moral evaluation of llms. ACM SIGKDD
Explorations Newsletter, 27(1):62–71.
Michael T Kane. 2013. Validating the interpretations
and uses of test scores. Journal of educational mea-
surement, 50(1):1–73.
Dongjin Kang, Sunghwan Mac Kim, Taeyoon Kwon,
Seungjun Moon, Hyunsouk Cho, Youngjae Yu,
Dongha Lee, and Jinyoung Yeo. 2024. Can large
language models be good emotional supporter? miti-
gating preference bias on emotional support conver-
sation. In Proceedings of the 62nd Annual Meeting of
the Association for Computational Linguistics (Vol-
ume 1: Long Papers), pages 15232–15261.
Michal Kosinski. 2024. Evaluating large language mod-
els in theory of mind tasks. Proceedings of the Na-
tional Academy of Sciences, 121(45):e2405460121.
Matthew Le, Y-Lan Boureau, and Maximilian Nickel.
2019. Revisiting the evaluation of theory of mind
through question answering. In Proceedings of the
2019 Conference on Empirical Methods in Natu-
ral Language Processing and the 9th International
Joint Conference on Natural Language Processing
(EMNLP-IJCNLP), pages 5872–5877.
Yanran Li and 1 others. 2017. Dailydialog: A manually
labelled multi-turn dialogue dataset. In IJCNLP.
Cynthia A Lietz, Karen E Gerdes, Fei Sun, Jen-
nifer Mullins Geiger, M Alex Wagaman, and Eliza-
beth A Segal. 2011. The empathy assessment index
(eai): A confirmatory factor analysis of a multidimen-
sional model of empathy. Journal of the Society for
Social Work and Research, 2(2):104–124.
Angeline Lillard. 1998. Ethnopsychologies: cultural
variations in theories of mind. Psychological bulletin,
123(1):3.
Zachary Lipton and Jacob Steinhardt. 2019.
Trou-
bling trends in machine learning scholarship. Queue,
17(1):45–77.

--- Page 11 ---

Matteo Marcuzzo, Alessandro Zangari, Andrea Al-
barelli,
Jose Camacho-Collados,
and Moham-
mad Taher Pilehvar. 2025. Morables: A benchmark
for assessing abstract moral reasoning in llms with
fables. In Proceedings of the 2025 Conference on
Empirical Methods in Natural Language Processing,
pages 27715–27739.
Giovanni Franco Gabriel Marraffini, Andrés Cotton,
Noe Fabian Hsueh, Axel Fridman, Juan Wisznia, and
Luciano Del Corro. 2024. The greatest good bench-
mark: Measuring llms’ alignment with utilitarian
moral dilemmas. In Proceedings of the 2024 Con-
ference on Empirical Methods in Natural Language
Processing, pages 21950–21959.
Paul E Meehl. 1990. Why summaries of research on
psychological theories are often uninterpretable. Psy-
chological reports, 66(1):195–244.
Samuel Messick. 1995. Validity of psychological as-
sessment: Validation of inferences from persons’ re-
sponses and performances as scientific inquiry into
score meaning. American psychologist, 50(9):741.
Chris Moore. 2013. The development of commonsense
psychology. Psychology Press.
Aida Nematzadeh, Kaylee Burns, Erin Grant, Alison
Gopnik, and Tom Griffiths. 2018. Evaluating theory
of mind in question answering. In Proceedings of the
2018 Conference on Empirical Methods in Natural
Language Processing, pages 2392–2400.
Simon Ott, Adriano Barbosa-Silva, Kathrin Blagec, Jan
Brauner, and Matthias Samwald. 2022. Mapping
global dynamics of benchmark creation and satura-
tion in artificial intelligence. Nature Communica-
tions, 13(1):6793.
Gabriele Paolacci, Jesse Chandler, and Panagiotis G
Ipeirotis. 2010. Running experiments on amazon
mechanical turk. Judgment and Decision making,
5(5):411–419.
Kishore Papineni, Salim Roukos, Todd Ward, and Wei-
Jing Zhu. 2002. Bleu: a method for automatic evalu-
ation of machine translation. In Proceedings of the
40th annual meeting of the Association for Computa-
tional Linguistics, pages 311–318.
Josef Perner, Susan R Leekam, and Heinz Wimmer.
1987. Three-year-olds’ difficulty with false belief:
The case for a conceptual deficit. British journal of
developmental psychology, 5(2):125–137.
Walter Quattrociocchi, Matjaz Perc, and 1 others. 2025.
Epistemological fault lines between human and artifi-
cial intelligence. PsyArXiv Preprint, OSF Preprints.
Preprint, accessed 22 Dec 2025.
Simona Raimo, Maria Cropano, María Dolores Roldán-
Tapia, Lidia Ammendola, Daniela Malangone, and
Gabriella Santangelo. 2022. Cognitive and affective
theory of mind across adulthood. Brain Sciences,
12(7):899.
Hannah Rashkin and 1 others. 2019. Towards empa-
thetic open-domain conversation models. In ACL.
John Rawls. 1999. Collected papers. Harvard Univer-
sity Press.
Pooya Razavi, Hadi Shaban-Azad, and Sanjay Srivas-
tava. 2023. Gheirat as a complex emotional reaction
to relational boundary violations: A mixed-methods
investigation. Journal of Personality and Social Psy-
chology, 124(1):179.
Pavan Reddy and Nithin Reddy. 2025.
Prevent-
ing another tessa:
Modular safety middleware
for health-adjacent ai assistants.
arXiv preprint
arXiv:2509.07022.
Thomas Reid. 1788. Essays on the Active Powers of
Man. Edinburgh University Press.
Matthew Riemer, Zahra Ashktorab, Djallel Bouneffouf,
Payel Das, Miao Liu, Justin D Weisz, and Murray
Campbell. 2024. Position: Theory of mind bench-
marks are broken for large language models. arXiv
preprint arXiv:2412.19726.
Maarten Sap, Hannah Rashkin, Derek Chen, Ronan
LeBras, and Yejin Choi. 2019.
Socialiqa: Com-
monsense reasoning about social interactions. arXiv
preprint arXiv:1904.09728.
Chelsea Schein and Kurt Gray. 2018. The theory of
dyadic morality: Reinventing moral judgment by
redefining harm. Personality and Social Psychology
Review, 22(1):32–70.
Nino Scherrer, Claudia Shi, Amir Feder, and David Blei.
2023. Evaluating the moral beliefs encoded in llms.
Advances in Neural Information Processing Systems,
36:51778–51809.
Simone G. Shamay-Tsoory and Judith Aharon-Peretz.
2012. Neural processing associated with cognitive
and affective theory of mind. Social Cognitive and
Affective Neuroscience, 7(1):53–63.
Gemma Sharp, John Torous, and Madeline L West. 2023.
Ethical challenges in ai approaches to eating disor-
ders.
Henry Sidgwick. 1907. The Methods of Ethics.
Yan Tao, Olga Viberg, Ryan S Baker, and René F Kizil-
cec. 2024. Cultural bias and cultural alignment of
large language models. PNAS nexus, 3(9):pgae346.
John Torous and Charlotte Blease. 2024. Generative
artificial intelligence in mental health care: potential
benefits and current challenges. World Psychiatry,
23(1):1.
Max Van Duijn, Bram Van Dijk, Tom Kouwenhoven,
Werner De Valk, Marco Spruit, and Peter van der
Putten. 2023. Theory of mind in large language mod-
els: Examining performance of 11 state-of-the-art
models vs. children aged 7-10 on advanced tests. In
Proceedings of the 27th conference on computational
natural language learning (CoNLL), pages 389–402.

--- Page 12 ---

Hanna Wallach, Meera Desai, A Feder Cooper, An-
gelina Wang, Chad Atalla, Solon Barocas, Su Lin
Blodgett, Alexandra Chouldechova, Emily Corvi,
P Alex Dow, and 1 others. 2025. Position: Evaluating
generative ai systems is a social science measurement
challenge. arXiv preprint arXiv:2502.00561.
Anuradha Welivita and Pearl Pu. 2024. Are large lan-
guage models more empathetic than humans? arXiv
preprint arXiv:2406.05063.
Carolyn V Wheeler. 2024. Regulating ai therapy chat-
bots: A call for federal oversight. Tex. A&M L. Rev.,
12:891.
Heinz Wimmer and Josef Perner. 1983. Beliefs about
beliefs: Representation and constraining function of
wrong beliefs in young children’s understanding of
deception. Cognition, 13(1):103–128.
Joshua D Wondra and Phoebe C Ellsworth. 2015.
An appraisal theory of empathy and other vicari-
ous emotional experiences. Psychological review,
122(3):411.
Yufan Wu, Yinghui He, Yilin Jia, Rada Mihalcea, Yu-
long Chen, and Naihao Deng. 2023.
Hi-tom: A
benchmark for evaluating higher-order theory of
mind reasoning in large language models. In Find-
ings of the Association for Computational Linguistics:
EMNLP 2023, pages 10691–10706.
Hainiu Xu, Runcong Zhao, Lixing Zhu, Jinhua Du, and
Yulan He. 2024. Opentom: A comprehensive bench-
mark for evaluating theory-of-mind reasoning capa-
bilities of large language models. arXiv preprint
arXiv:2402.06044.
Tal Yarkoni. 2022. The generalizability crisis. Behav-
ioral and Brain Sciences, 45:e1.
Linhao Yu, Yongqi Leng, Yufei Huang, Shang Wu,
Haixin Liu, Xinmeng Ji, Jiahui Zhao, Jinwang Song,
Tingting Cui, Xiaoqing Cheng, and 1 others. 2024.
Cmoraleval: A moral evaluation benchmark for chi-
nese large language models. In Findings of the As-
sociation for Computational Linguistics: ACL 2024,
pages 11817–11837.
Jamil Zaki and Kevin Ochsner. 2012. The dynamic na-
ture of empathy: Affective and cognitive components
respond differently to change. Trends in Cognitive
Sciences, 16(2):70–75.

--- Page 13 ---

A
Appendix
Theory Trace Card for EmpatheticDialogues (Rashkin et al., 2019)
1. Theory
• Framework: Appraisal Theory of Empathy (Wondra and Ellsworth, 2015) [The authors’ operational framework is
“Empathetic Response,” which we map here to the closest theoretical framework for empathy, namely the Appraisal
Theory of Empathy.]
• Core components:
– Appraisal of the target’s situation
– Vicarious emotional experience
– Compassion
2. Components Exercised
• Appraisal of the target’s situation
• Compassion
3. Task Operationalization
• Task: The model acts as a “Listener” and must generate a response to a “Speaker” describing a personal situation
• Key specs:
– Input: Dialogue history (context) grounded in one of 32 emotion labels (e.g., Proud, Afraid).
– Constraints: The model has access to the text context but not to the emotion label itself.
Scoring Criterion:
• Automated similarity-based metrics (e.g., BLEU; Papineni et al., 2002) and human evaluations assessing the perceived
appropriateness and empathy of generated responses relative to reference replies.
4. Inference and Limitations
• Inference: Performance supports cognitive empathy.
• Limitations: No overlapping emotions or non-textual cues (tone, body language). Only tested short scenarios.
Dialogues sourced from MTurk workers whose demographics are known to be culturally biased (Paolacci et al.,
2010).
Theory Trace Card for LLM ToM Evaluation (Kosinski, 2024)
1. Theory
• Framework: Theory of Mind (Wimmer and Perner, 1983; Perner et al., 1987; Heyes and Frith, 2014).
• Core components: [Not explicitly stated in paper.]
– Cognitive ToM (e.g., belief-tracking)
– Affective ToM (e.g., emotion-tracking)
2. Components Exercised
• Cognitive ToM (belief tracking)
3. Task Operationalization
• Task: Given a short, structured narrative describing an agent, an object, and a belief-relevant change in the environ-
ment, the model answers questions predicting the agent’s belief or action.
• Key specs: Tasks are modeled after classic developmental false-belief paradigms, including “Smarties” and
“Sally–Anne” tasks (Wimmer and Perner, 1983; Perner et al., 1987). Each false-belief scenario is paired with
closely matched true-belief control scenarios and reversed versions to control for task structure and language cues.
• Scoring Criterion: Accuracy measured as the proportion of scenarios fully solved, where a scenario is counted as
correct only if all sub-questions (false-belief and control questions) are answered correctly.
4. Inference and Limitations
• Inference: Performance supports cognitive ToM (belief-tracking).
• Limitations: Does not cover non-text-based cues (e.g., gaze). Only short text-based scenarios. False-belief tasks
were developed for Western populations, and performance may be culturally biased (Lillard, 1998; Heyes and Frith,
2014).

--- Page 14 ---

Theory Trace Card for ETHICS Moral Reasoning (Hendrycks et al., 2021)
1. Theory
• Framework: A multi-theory account of moral reasoning drawing on justice (Sidgwick, 1907), deontology (Rawls,
1999), virtue ethics (Aristotle, 340 BC), utilitarianism (de Lazari-Radek and Singer, 2017), and commonsense moral
judgment (Reid, 1788)
• Core components:
– Justice.
– Deontological reasoning.
– Virtue and vice attribution.
– Utilitarian reasoning.
– Commonsense moral reasoning.
2. Components Exercised
• Justice.
• Deontological reasoning.
• Virtue and vice attribution.
• Utilitarian reasoning.
• Commonsense moral judgment.
3. Task Operationalization
• Task: Given a short, stylized moral scenario, the model produces a discrete judgment aligned with the normative
framing of the task (e.g., reasonable vs. unreasonable, virtue vs. vice, more vs. less pleasant).
• Key specs: The benchmark comprises multiple task types, one for each of the components above. All tasks use fixed
prompts and closed-set response formats.
• Scoring Criterion: Accuracy with respect to human-labeled judgments for each task type. For Justice, Deontology,
Virtue Ethics, and Commonsense Morality, responses are scored based on agreement with annotated reasonableness
or acceptability labels; for Utilitarianism, scoring reflects correct identification of the more pleasant (lower-pain)
scenario in paired comparisons.
4. Inference and Limitations
• Inference: Performance supports moral reasoning in unambiguous text-based scenarios in terms of justice, deontology,
virtue ethics, utilitarianism, and commonsense moral intuitions.
• Limitations: Excludes multimodal, sequential, interactive, and open-ended reasoning. Benchmark operationalizes
ethics primarily through Western moral theories (e.g., deontology, utilitarianism, virtue ethics). Primarily includes
data from English speakers from the United States, Canada, and the United Kingdom, sourced from MTurk and
Reddit.

--- Page 15 ---

Theory Trace Card for GoEmotions (Demszky et al., 2020)
• Framework: Emotion Taxonomy after Cowen and Keltner, 2017.
• Core components: Emotion recognition [Paper tests ability to recognize the emotion categories identified in Cowen
and Keltner, 2017]
2. Components Exercised
• Emotion recognition.
3. Task Operationalization
• Task: Given a single short text comment, the model predicts one or more emotion labels from a predefined set.
• Key specs: Single-utterance inputs (Reddit comments); closed-set label space consisting of 27 emotion categories
plus neutral; multi-label classification; no justification required.
• Scoring Criterion: Performance is evaluated by agreement with human-annotated emotion labels, using standard
multi-label classification metrics.
4. Inference and Limitations
• Inference: Performance supports the model’s ability to recognize clearly expressed emotions in short text snippets
under a fixed category schema
• Limitations: Does not evaluate other facets of emotion understanding (e.g., detecting subtle or implicit emotions,
understanding causes of emotions). Emotion taxonomy for labeling texts was created based on MTurk ratings without
controls for cultural diversity.
Theory Trace Card for SocialIQA (Sap et al., 2019)
1. Theory
• Framework: Commonsense Psychology (Moore, 2013)
• Core components:
– Inferring motivations.
– Inferring next actions.
– Inferring emotions.
2. Components Exercised
• Inferring motivations.
• Inferring next actions.
• Inferring emotions.
3. Task Operationalization
• Task: Given a short narrative describing an everyday social situation, the model answers a multiple-choice question
about motivations and intentions, emotional reactions, or likely next actions.
• Key specs: Single sentence scenarios; multiple-choice format with three answer options; questions and answers
constructed using a combination of crowdsourced annotations and prior datasets.
• Scoring Criterion: Accuracy measured as agreement with human-annotated correct answers collected via MTurk.
4. Inference and Limitations:
• Inference: Performance supports social commonsense reasoning.
• Limitations: Uses constrained, textual scenarios with limited context. Scenarios were sourced from English-speaking
WEIRD sources and annotated by MTurk workers, which may be culturally biased and not reflect non-Western social
norms.

```
