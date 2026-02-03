---
title: "A Roadmap to Pluralistic Alignment - PDF Extract"
source_pdf: "2024-Sorensen-A Roadmap to Pluralistic Alignment.pdf"
pages: 23
extracted_at: "2026-01-24T17:05:42.013732"
---

# PDF Extract: A Roadmap to Pluralistic Alignment

**Source PDF:** 2024-Sorensen-A Roadmap to Pluralistic Alignment.pdf
**Total Pages:** 23

---

## Content

```
--- Page 1 ---

Position: A Roadmap to Pluralistic Alignment
Taylor Sorensen 1 Jared Moore 2 Jillian Fisher 1 3 Mitchell Gordon 1 4 Niloofar Mireshghallah 1
Christopher Michael Rytting 1 Andre Ye 1 Liwei Jiang 1 5 Ximing Lu 1 Nouha Dziri 5 Tim Althoff 1
Yejin Choi 1 5
Abstract
With increased power and prevalence of AI sys-
tems, it is ever more critical that AI systems are
designed to serve all, i.e., people with diverse
values and perspectives. However, aligning mod-
els to serve pluralistic human values remains an
open research question. In this piece, we pro-
pose a roadmap to pluralistic alignment, specifi-
cally using large language models as a test bed.
We identify and formalize three possible ways
to define and operationalize pluralism in AI sys-
tems: 1) Overton pluralistic models that present
a spectrum of reasonable responses; 2) Steerably
pluralistic models that can steer to reflect certain
perspectives; and 3) Distributionally pluralistic
models that are well-calibrated to a given pop-
ulation in distribution. We also formalize and
discuss three possible classes of pluralistic bench-
marks: 1) Multi-objective benchmarks, 2) Trade-
off steerable benchmarks that incentivize mod-
els to steer to arbitrary trade-offs, and 3) Jury-
pluralistic benchmarks that explicitly model di-
verse human ratings. We use this framework to
argue that current alignment techniques may be
fundamentally limited for pluralistic AI; indeed,
we highlight empirical evidence, both from our
own experiments and from other work, that stan-
dard alignment procedures might reduce distribu-
tional pluralism in models, motivating the need
for further research on pluralistic alignment.
1Department of Computer Science, University of Washing-
ton, Seattle, Washington, USA 2Department of Computer Science,
Stanford University, Stanford, California, USA 3Department of
Statistics, University of Washington, Seattle, Washington, USA
4Department of Electrical Engineering and Computer Science,
MIT, Cambridge, Massachusetts, USA 5Allen Institute for Arti-
ficial Intelligence, Seattle, Washington, USA. Correspondence
to: Taylor Sorensen <tsor13@cs.washington.edu>, Yejin Choi
<yejin@cs.washington.edu>.
Proceedings of the 41 st International Conference on Machine
Learning, Vienna, Austria. PMLR 235, 2024. Copyright 2024 by
the author(s).
Pluralistic 
Human Values
Security
Free speech
Factuality
Is it ok for governments to moderate 
public social media content?
Many think that it’s not okay for the government to 
moderate content as it endangers free speech, 
while others deem it acceptable for prevention of 
terrorism. A few, on the other hand, think it’s 
necessary to reduce misinformation.
Overton
Distributional
Steerable
or
It is ok for the government to moderate 
content for terrorism and threats.
It is not ok to moderate any content as it 
endangers free speech.
or
It is ok for the government to moderate 
content that promotes false information.
or
A: Yes, for public safety threats (45%) 
B: No, to protect free speech (32%) 
C: Yes, to prevent misinformation (9%)
…
Figure 1. Three kinds of pluralism in models.
1. Introduction
AI alignment aims to ensure that a system works with hu-
man intentions and values (Leike et al., 2018; Ji et al., 2024;
Gabriel, 2020).
However, even within a single task or
prompt, individual people vary widely in their goals, in-
tentions, and values. As a broader set of people use and rely
upon AI systems, we need systems that can understand and
cater to a broader set of needs. In other words, we need
systems that are pluralistic, or capable of representing a
diverse set of human values and perspectives. While many
in the community have argued for this (Bai et al., 2022b;
Gordon et al., 2022; Sorensen et al., 2023), at least two
important questions remain: How, concretely, can a system
be pluralistic? and How might benchmarks be designed to
measure pluralism?
In this piece, we advocate for explicit pluralistic consid-
erations in aligning AI systems (§2). In particular, we
1
arXiv:2402.05070v3  [cs.AI]  20 Aug 2024

--- Page 2 ---

Position: A Roadmap to Pluralistic Alignment
use large language models (LLMs) as a testbed for align-
ment (Askell et al., 2021), though we believe the concepts
can generalize to other AI systems (§6.3). Because plural-
ism may look different in different contexts, we formalize
three distinct ways of operationalizing pluralism for AI sys-
tems/models: 1) providing comprehensive, high-coverage
responses (Overton pluralism, §3.1), 2) an ability to be
faithfully steered to represent particular attributes (steerable
pluralism, §3.2), and 3) distributional representation of a
population (distributional pluralism, §3.3). Each form of
pluralism has cases where they may be desirable to maxi-
mize. We also define three types of pluralistic benchmarks:
multi-objective benchmarks (§4.1), benchmarks of mod-
els’ steerability across objectives (trade-off steerable bench-
marks, §4.2), and benchmarks that explicitly model individ-
uals (jury-pluralistic benchmarks, §4.3). We also outline the
situations for which each would be useful.
We then discuss the relationship between current alignment
approaches and pluralism (§5) and provide initial findings
that current alignment techniques reduce distributional plu-
ralism. We advocate and lay out a plan for future work
toward pluralistic evaluations and alignment.
2. Arguments for Pluralism in AI Systems
In this section, we argue for the importance of pluralism in
aligning AI models.
Customization necessitates pluralism. Any guardrails
placed on AI systems will require customization, within
the bounds of those guardrails, to serve diverse use cases
and values (Chen et al., 2023; Jang et al., 2023). Pluralism
can illuminate the set of values or attributes that users may
customize to, and provide an understanding of how well a
system can be steered (§3.2, 4.2).
Pluralistic systems have technical benefits. Implicit to cur-
rent preference-based methods like reinforcement learning
with human feedback (RLHF) is the assumption that models
should fit to the “average” human preference. However, this
treats human variation as noise instead of signal (Aroyo
et al., 2023; Siththaranjan et al., 2023) – pluralism, how-
ever, recognizes this as signal. Modeling pluralism also may
increase interpretability by enabling a clearer relationship
between decisions and their source (§3.2, 4.2).
Pluralistic evaluations enable generalist systems. Re-
cently, AI/NLP has trended away from specialist systems
and towards generalist systems (foundation models) for use
in a diverse set of tasks by a diverse set of users. Yet, current
alignment optimizes these generalist systems for a single
objective – averaged human preferences. To understand the
strengths and weaknesses of these systems, we must mea-
sure how they perform across a variety of objectives (§4.1)
(Ethayarajh & Jurafsky, 2022) and users (§3.2, 3.3, 4.3).
Pluralism as a value itself. Many modern societies view
accepting competing values and perspectives as a core value
in and of itself. Theorists have extolled the benefits of polit-
ical pluralism (de Tocqueville, 1835; Berlin, 1969; Rawls,
1996), moral and value pluralism (Nagel, 1979; Kekes, 1993;
Raz, 1999), and pluralist theories of truth (Wright, 1992;
Sher, 1998). While this piece primarily focuses on surfac-
ing differing ideas, perspectives, and values (§3, 4), our
scaffolding for technical measurements and implementa-
tions of value can also apply to other notions of pluralism.
This stands in contrast to current alignment procedures such
as RLHF which have been characterized as implementing
“preference-based utilitarianism.” (Tasioulas, 2022).
AI systems should reflect human diversity. We contend
that AI systems should reflect and support the diversity
amongst humans and their values, as it is both a feature and
a desired quality of human societies (§3.3, 4.3). Exposure
to diverse ideas (§3.1) also improves deliberation (Bowman
et al., 2022; Landemore & Page, 2015). Furthermore, al-
gorithmic monocultures lead to increased unfairness when
applied by many decision makers (Bommasani et al., 2021).
3. Pluralism for AI Models/Systems
In this section, we formalize three definitions for how a
single model or system can be pluralistic. Specifically, we
outline Overton pluralism, wherein a model outputs the
whole spectrum of reasonable responses; Steerable plural-
ism, wherein a model is faithfully steered to reflect certain
properties or perspectives; and Distributional pluralism,
wherein a model’s distribution over answers matches that
of a given target population (see Figure 1). For each, we
will also discuss relevant applications and potential eval-
uations, along with limitations and recommendations for
future research.
Throughout, we will consider a model or system M, a query
x, and a response y. While we specifically focus on natural
language queries and responses with M being an LLM,
our definitions can nevertheless generalize to other inputs,
outputs, and models as well.
3.1. Overton Pluralistic Models
Given an input, there are often many potential types (or
modes) of answers a model can produce. For example, if a
user poses a query to an LLM for which there is no single
established correct answer, the LLM may answer with any
one of several reasonable answers.
Definitions Given a query x, consider possible answers y.
(1) Correct Answer in C: An answer which can be conclu-
sively verified or with which the overwhelming majority of
people across various backgrounds would agree.
2

--- Page 3 ---

Position: A Roadmap to Pluralistic Alignment
(2) Reasonable Answer in R: An answer for which there
is suggestive, but inconclusive, evidence, or one with which
significant swaths of the population would agree. Additional
top-down restrictions (e.g., safety) may apply.
(3) Overton window: The set of all reasonable answers:
W(x) = {y ∈Y|(x, y) ∈R}.1
(4) A response set {y} to a query x is Overton-pluralistic:
{y} contains all potentially reasonable answers in the Over-
ton window. This is in contrast to picking just one answer
in the Overton window, or presenting an unreasonable an-
swer which would lie outside the Overton window. A single
response may be Overton-pluralistic if it synthesizes the
whole response set {y}.
(5) Model M is Overton-pluralistic: M gives Overton-
pluralistic responses to queries, that is for a given input x,
the output of M(x) = W(x).
Motivation In many situations, there are many reasonable
answers to a question (Min et al., 2020; Scherrer et al., 2023).
Rather than outputting a single reasonable answer, which
may be selected idiosyncratically or in a biased fashion,
Overton-pluralistic models output all reasonable answers.
Potential Implementation We outline two ways to opera-
tionalize Overton pluralism. In order to determine an Over-
ton window for a set of queries X, one could survey a popu-
lation for responses to a question and identify clusters (e.g.,
using semantic similarity) of candidate reasonable answers.
Then, one could narrow down the window to reasonable
answers W(x) with additional polling for reasonableness,
defining a minimum threshold of support, or some other
top-down way of filtering out unreasonable responses. One
could define a way to extract the set of “answers" {y} from a
model response and compare it to the window. Alternatively,
one could enumerate a list of unreasonable answers U(x)
and detect which reasonable or unreasonable answers the
response entails with an entailment model (Shajalal et al.,
2023; Liu et al., 2022). With both methods, metrics like
precision/recall/accuracy can be calculated.
Applications Many relevant domains fall under advice-
giving. Current LLMs often give advice confidently but
inconsistently or in an opinionated manner, affecting users’
downstream judgments (Krügel et al., 2023; Jakesch et al.,
2023). Overton-pluralism requires consideration of multiple
heterogeneous judgements, encouraging deliberation over
spontaneous judgement (Kant, 1788; Rawls, 1971). It could
also aid in scalable oversight (Bowman et al., 2022) to help
users annotate model outputs, in the single ground truth
case (Michael et al., 2023) or when we want a diversity of
1Our terminology generalizes the concept of an “Overton win-
dow" as used in political science: “the spectrum of ideas on public
policy and social issues considered acceptable or viable by the
general public at a given time." (OED, 2023)
views. Further examples include settings where we want to
encourage multiple approaches, such as mathematical proof
writing.
Limitations Defining and operationalizing the Overton win-
dow may present a challenge. If a reasonable answer is
determined by a set of expert annotators, it may be difficult
to scale. If the Overton window is not properly defined, mod-
els may contribute to bothsidesism / false balance (Imundo
& Rapp, 2021; Boykoff & Boykoff, 2004). One remedy
may be to present the support or certainty for each rea-
sonable answer in addition to its content, although current
LLMs struggle with this (Zhou et al., 2024). Also, while
pluralism may never be completely neutral, it can be consid-
ered a fairer response to queries (Haraway, 1988). Finally,
this framework requires long-form responses with multiple
answers; other concepts of pluralism may be required for
distributions over short answers (see §3.3).
Alignment Procedures and Recommendations While
RLHF may implicitly steer models to Overton pluralism
to the extent that users prefer it, further study into this is
needed. Alternatively, one approach to explicitly encourage
Overton pluralism is taking multiple samples from a model
(Long, 2023; Jung et al., 2022), potentially prompting for
diverse outputs (Hayati et al., 2023), to simulate an Overton
window. Alternatively, one could manually create the batch
of reasonable responses. A model can be trained to output a
synthesis of the entire batch. Datasets which identify human
values (Hendrycks et al., 2020; Sorensen et al., 2023) can be
used to evaluate Overton-pluralism. We recommend further
study into models’ current degree of Overton-pluralism and
how it can be amplified for relevant applications.
3.2. Steerable Pluralistic Models
A pluralistic model might instead faithfully steer (or align)
its responses to a given attribute or perspective, such as a
value, framework, or population.
Definitions With this in mind, let us consider:
(6) Steering attributes A: Attributes/properties/perspecti-
ves which we wish a model to faithfully reflect. Examples
include groups of people from a shared culture, philosoph-
ical/political schools of thought, or particular values. To
reflect multiple attributes simultaneously, the elements of A
could be construed as sets of attributes.
(7) Response y|x,a faithfully reflects attribute a ∈A: The
response y to the query x is consistent with, or follows from,
attribute a.
(8) Model M is steerably-pluralistic with respect to at-
tributes A: Given an input x and an attribute a ∈A, the
model M(x, a) conditioned on a produces a response y
which faithfully reflects a.
3

--- Page 4 ---

Position: A Roadmap to Pluralistic Alignment
Motivation In many instances, we want models to respond
to queries in a consistent and specifiable manner. Models
which have been so heavily “aligned” towards a specific
attribute such that they cannot be steered to other attributes
fail to be useful (or usable) to populations who may not
share that value or attribute. We see evidence of this in the
“Silicon Valley” and “WEIRD” (Henrich et al., 2010) bias
of many LLMs, which often skew male, White, American,
liberal, and wealthy in perspective (Santurkar et al., 2023;
Hartmann et al., 2023; Perez et al., 2022; Santy et al., 2023).
Potential Implementation Given queries X and attributes
A, one needs a way to condition the model on attributes
at inference. To measure whether a response reflects a,
one could either use direct human annotations or reward
models that are tuned specifically to the attributes, such
as a value-specific reward (Sorensen et al., 2023). These
attribute-specific faithfulness scores would be the degree to
which a model is steerably pluralistic.
Different attributes may require different metrics for faith-
fulness, depending on the kind of attribute and level of
ambiguity. For example, for a particular difficult moral
quandary, there may be no ambiguity given a particular ethi-
cal framework (e.g., only one “correct" or faithful answer).
However, if you condition instead on a population, there
may still be disagreement or ambiguity - other approaches
like an Overton window may apply here.
Several previous works have measured forms of steerable
pluralism, particularly with respect to moral, political, and
cultural perspectives (Argyle et al., 2023; Jiang et al., 2022;
Simmons, 2023; Ramezani & Xu, 2023; Santy et al., 2023).
However, previous work suggests that conditional pluralism
is far from solved (Santurkar et al., 2023).
Applications An important application of steerable-
pluralism is customization. Users often want to personalize
models towards characteristic properties and perspectives
(Chen et al., 2023), in tasks such as writing assistance (Li
et al., 2023a) and ideation (Girotra et al., 2023; Ma et al.,
2023). Steering towards therapeutic values can help in the
mental health domain (Song et al., 2024; Sharma et al.,
2023a). Steering models to represent multiple different per-
spectives can be valuable in creative production (Shanahan
& Clarke, 2023), psychological inquiry (Shanahan et al.,
2023), simulating social systems (Park et al., 2022), and
deliberative discourse (Danry et al., 2023; Landemore &
Page, 2015; Page, 2019; 2008).
Moreover, steerably pluralistic models may have useful
representations in a variety of settings, such as hate speech
detection (Feng et al., 2023) and negative thought reframing
(Sharma et al., 2023b;c). In general, this may allow varying
“cognitive architectures” for more structured and generally
intelligent systems (Sumers et al., 2023).
Limitations Steerable pluralism requires deciding which
attributes are acceptable to steer the model. We may want to
disallow some attributes (e.g., hate speech). The challenges
here are similar to those in determining which answers are
“reasonable” in Overton-pluralism, such as subjectivity or
arbitrariness in the selection of steerable attributes. More-
over, if attributes are defined too broadly, there is a risk
of stereotyping or “flattening” the nuances of the complex
perspectives and people that attributes are intended to repre-
sent (Durmus et al., 2023). In some cases, an intersectional
evaluation (Crenshaw, 1989), in which attributes are not con-
sidered independently but in conjunction with each other,
may be necessary.
Alignment Procedures and Recommendations There are a
variety of ways to induce particular values at inference time.
These include conditioning on certain groups (Argyle et al.,
2023; Hwang et al., 2023) and studying which conditions
(responses, demographics, etc.) yield the best agreement.
Li et al. (2023b); Kim & Lee (2023) learn user embeddings
which they use to induce certain values from LLMs. Zhao
et al. (2023) add a module to base LLMs which aims to
predict group responses in a few-shot manner. Fleisig et al.
(2023) predict annotator ratings for specific groups. Sharma
et al. (2023c;d) rewrite responses for specific audiences.
We believe that steerability research will become increas-
ingly important as users desire more customizability. While
there may be certain behaviors to which a model should not
be aligned, we advocate for systems that can be aligned to
many attributes within an acceptable range.
3.3. Distributionally Pluralistic Models
Another way to operationalize pluralism is in the distribu-
tion over answers compared to a given population.
Definitions In this framework, we consider:
(9) A population or group of people G: A set of people
which we want the model to represent.
(10) Model M is distributionally-pluralistic with respect to
a reference population G: For a given prompt x, M is as
likely to provide response y as the reference population G.
In other words, M is well-calibrated w.r.t. the distribution
over answers from G.
Motivation and Applications Distributional pluralism in
an LLM is crucial for any application where M is used to
simulate, interface with, or otherwise model the views of
a population, e.g., simulating populations via agent-based
modeling (Törnberg et al., 2023; Park et al., 2022; 2023),
piloting subject/user responses to surveys (Argyle et al.,
2023; Aher et al., 2023), survey design (Ziems et al., 2023),
or studying the internet as a cultural artifact (Buttrick, 2024).
Potential Implementation Let X be a set of queries to
4

--- Page 5 ---

Position: A Roadmap to Pluralistic Alignment
which G gives a distribution Y . For example, a census
survey or public opinion poll. M’s estimate, ˆY , can be com-
pared to the population distribution using any distributional
divergence metrics, such as Jensen-Shannon divergence,
KL-divergence, or Wasserstein distance (Santurkar et al.,
2023; Durmus et al., 2023), or hard measures like accuracy
or tetrachoric correlation (Argyle et al., 2023).
Limitations One potential limitation of distributional plu-
ralism is its proportional nature. This means that more
frequent opinions will be output by a model with higher
frequency, even if this response is harmful - although might
be mitigated by defining a window of reasonableness as in
Overton pluralism. Another limitation is the need for a pre-
determined target distribution–a population. In creation of a
general LLM, like ChatGPT, who is the target distribution?
Furthermore, for many open-ended queries, it is not clear
whether there is any response frequency data.
Alignment procedures While, to our knowledge, there are
no alignment procedures to explicitly increase distributional
calibration, there are a couple promising directions. One is
to simply (pre)train a model on more data from the target
population. As the cross entropy objective encourages a
model to learn the distributions of speech of a training pop-
ulation, simply providing more data from that population
ought to lead to better representation. Another promising di-
rection is to train on the data from a population (e.g., survey
data) that one could use to evaluate distributional pluralism,
although it is unclear how well this will generalize to novel
questions/domains. Further research is needed here.
Recommendations Oftentimes when researchers measure
to which group of people a model best aligns, they compare
average responses. In contrast, we advocate for compar-
ing distributions because it leads to clearer results: groups
of people have distributions over answers, and probabilis-
tic models do as well. We advocate for more distribution-
ally pluralistic evaluations with respect to clearly speci-
fied groups of people to better characterize current models.
Nonetheless, the stochasticity in distributional pluralism is
not desirable in all cases–for example, when the behavior
of a model needs to be tightly controlled.
4. Pluralism for Benchmarks
While the last section defined how a model can be pluralistic,
here we explore how a benchmark can be pluralistic. Most
current benchmarks are monistic (focused on a single objec-
tive). Pluralistic benchmarks have more than one objective
to maximize. Importantly, each is measured separately.
4.1. Multi-Objective Benchmarks
Definitions Define:
Multi-objective
Model 
 is a Pareto 
improvement over 
ℳ1
ℳ2
o5(ℳ1) > o5(ℳ2)
o1(ℳ1) > o1(ℳ2)
o2(ℳ1) > o2(ℳ2)
.
.
.
Security
Freedom
Conformity
Conciseness
Correctness
ℳ2
ℳ1
Trade-off Steerable
Model 
 is trade-off 
steerable if it can be 
steered along its 
Pareto frontier from 
one trade-off function 
( ) to another ( )
ℳ
f1
f2
Jury-pluralistic
Model 
 achieves 
higher welfare for the 
Jury than model 
 for 
the welfare function , 
ℳ1
ℳ2
w
w(ℳ1) > w(ℳ2)
Freedom
ℳ
Security
f1 = 0.2 ⋅ freedom + 0.8 ⋅ security
f2 = 0.8 ⋅ freedom + 0.2 ⋅ security
ℳf1
ℳf1
steer from  to 
f1
f2
x1
x2
ℳ2
ℳ1
w(ℳ1) = 4
w(ℳ2) = 3
y1
1
y1
2
y2
1
y2
2
Figure 2. Three kinds of pluralistic benchmarks.
(11) Objectives to maximize O = {o1, . . . , on}: A set of
multiple objectives to evaluate a model M, each of which
which we desire to maximize. Each o maps from a model
M to a scalar in R.
(12) Model M1 is a Pareto improvement to model M2.:
∀oi ∈O, oi(M1) ≥oi(M2); ∃oj s.t. oj(M1) > oj(M2).
In other words, M1 is at least as good as M2 for all objec-
tives and strictly better for some objective oj.
(13) Function f is a commensurating function over ob-
jectives O: f is a function which combines multiple ob-
jectives into a single scalar meta-objective of the form
f(M) = f(o1(M), . . . , on(M)).
(14) Benchmark B is a multi-objective benchmark over
O: B reports the entire spectrum of model performances
on all objectives and can be flexibly adapted to multiple
commensurating functions. The “top" of the leaderboard is
the set of solutions (models) for which there is no Pareto
improvement.
In practice, the set of solutions for which there is no Pareto
improvement can be quite large. Therefore, it may be conve-
nient to define a commensurating function f to determine a
ranking for a given use case. The important part of a Pareto
benchmark is that if objectives are combined, it is done ex-
plicitly, reporting all objectives for all solutions. This makes
it possible to propose alternative explicit trade-offs.
5

--- Page 6 ---

Position: A Roadmap to Pluralistic Alignment
Motivation and Applications Implicit trade-offs are every-
where. For example, there is a fundamental tension between
helpfulness and harmlessness for LLMs (Askell et al., 2021;
Bai et al., 2022a). However, these two attributes often get
clumped together and are implicitly traded-off through data
mixtures or vague human preferences. Through explicit
multi-objective benchmarks, we can better understand how
they trade-off and make informed decisions when selecting
a model for a given application or domain (Liang et al.,
2023; Srivastava et al., 2023; Hendrycks et al., 2023).
Potential Implementation There are many ways to oper-
ationalize these objectives, such as evaluation on test sets,
outputs of a reward model, preference/ELO scores, model
properties and more. Other objectives might include ad-
herence to individual rules such as “Do not offer financial
advice" (Glaese et al., 2022) or principles (Bai et al., 2022b).
Limitations If the set of metrics is very large, it may be
costly to compare models across a large number of dimen-
sions. The choice of which objectives and the granularity of
benchmarks to include will influence the strength of the eval-
uation. Choosing the correct number and level of abstraction
of the objectives can be a difficult design decision.
Alignment Procedures and Recommendations Most align-
ment techniques optimize a single objective instead of
a group of objectives, requiring a commensurating func-
tion. To avoid this, we can look to techniques from multi-
objective RL (Hayes et al., 2022; Yang et al., 2019; Tozer
et al., 2017). While several multi-objective benchmarks
exist (Liang et al., 2023; Srivastava et al., 2023; Pan et al.,
2023) and it is common practice to evaluate LLMs on a
range of evaluations, we encourage the continued use, re-
search, and development of these benchmarks. Single-value
benchmarks can often lead to “reward-hacking” and ex-
ploiting spurious features, such as annotators’ preference
for more verbose responses (Wang et al., 2023a). Mul-
tiple objectives allow for a more diverse set of model
strengths (Ethayarajh & Jurafsky, 2020) and mitigate over-
optimization.
4.2. Trade-Off Steerable Benchmarks
In the multi-objective benchmark section, we assumed that
the model was static, occupying a single point in the objec-
tive space. However, it is useful to consider a benchmark
which encourages models to be steerable to trade off objec-
tives in different ways at inference time.
Many of the takeaways from the previous section apply
here, so we will focus our discussion on what is unique
about trade-off steerable benchmarks.
Definitions Building on the definitions from Section 4.1,
(15) Steering commensurating (or trade-off) functions F:
A set of commensurating functions to steer a model towards.
(16) Model M is steerable to functions F: For f ∈F,
the model steered to f (denoted Mf) maximizes f: ∀f ′ ∈
F, f(Mf) ≥f(Mf ′)
(17) Benchmark B is a trade-off steerable benchmark with
respect to O, F: B attempts to measure 1) a model’s ability
to maximize objectives O and 2) a model’s steerability to
various commensurating functions f ∈F.
Motivation and Applications A trade-off steerable bench-
mark measures whether a single model can represent solu-
tions across a spectrum of objectives, allowing for tuning
to trade-off functions of choice at deployment time. Any
application where customization is desirable could benefit
from this kind of benchmark.
Potential Implementation Many commensurating func-
tions are possible, including linear combinations (e.g.,
f = w1o1 + . . . + wnon) and selecting a single objective.
Given F, one implementation of a trade-off steerable bench-
mark could be a reward which tries to maximize the steer-
ability and overall objective values, as follows:
X
f∈F
f(Mf)
Maximizing requires the model to increase the overall value
of each f ∈F and also match the aligned model to the cor-
responding objective function. Related concepts include the
hypervolume indicator (Guerreiro et al., 2020) and expected
utility metric (Zintgraf et al., 2015).
Limitations This framework assumes a set of commensurat-
ing functions. However, many philosophers who subscribe
to value pluralism believe that values are incommensurable
and cannot be traded off (Hsieh & Andersson, 2021). Trade-
off sterable benchmarks (and most of machine learning) are
incompatible with that view. It is also important for general-
ization that the kind of commensurating functions desired
for use at test time are present in the benchmark.
Alignment Procedures and Recommendations Some
promising procedures to steer models include controllable
decoding (Liu et al., 2024; Qin et al., 2022; Lu et al., 2020),
prefix tokens/custom instructions (Chen et al., 2021; Lu
et al., 2022), and model soups (Wortsman et al., 2022; Jang
et al., 2023; Ramé et al., 2023). To our knowledge, however,
there are no standard LLM trade-off steerable benchmarks.
We advocate for increased development of such benchmarks
to spur more development in steerable AI systems.
4.3. Jury-Pluralistic Benchmarks
While multi-objective benchmarks deal with an arbitrary
objective type, it is also useful to talk about the specific case
when there is a population of annotators (or jury) to which
6

--- Page 7 ---

Position: A Roadmap to Pluralistic Alignment
we wish to align. Here, we formalize a type of benchmark
which separately and explicitly models a jury (Gordon et al.,
2022) to maximize an overall welfare function.
Definitions We define:
(18) Jury/Population/Annotators J = {j1, . . . , jn}: Some
population which we wish to represent in our evaluation.
Each annotator/person/jury member ji maps from an query
and response to a scalar reward or utility ji : X, Y →R.
(19)
Function w is a welfare function over jury J: w
is a function which combines the jury’s utilities into a
single scalar welfare objective of the form w(x, y) =
w(j1(x, y), . . . , jn(x, y)).
(20) Benchmark B is jury-pluralistic: B explicitly mea-
sures each juror ji to maximize a welfare function w.
Motivation and Applications Jury-pluralistic benchmarks
can serve as a concrete approach for democratic AI align-
ment (Koster et al., 2022; Ovadya, 2023; Mishra, 2023).
They allow us to explicitly reason over which users or groups
models are being aligned to, and potentially obtain fairer
outcomes as people are included and social welfare func-
tions are selected. Consensus-seeking applications benefit
from this approach. For instance, Deepmind trained an LLM
to find consensus statements that users preferred to any in-
dividual human-written statement (Bakker et al., 2022) and
Twitter’s Community Notes has moderated misinformation
by leveraging consensus between users who often disagree
(Wojcik et al., 2022). These approaches help to integrate
a diverse set of user preferences, which have been found
to vary globally in perceptions such as safety judgments
(Aroyo et al., 2023).
Potential Implementation One could construct a represen-
tative jury (e.g., of a particular country, population, or ex-
pertise) using established social science methods (Flanigan
et al., 2021; Arnesen & Peters, 2018). One could also con-
struct a jury designed to amplify specific perspectives. For
instance, in online communities, under-represented users
sometimes face extra harassment (Pew Research Center,
2021). To combat this, community-specific moderation al-
gorithms could be aligned to a jury featuring their voices.
Once a jury is selected, jury member functions ji can be
approximated in several ways. For example, a separate pref-
erence/reward model could be trained for each jury member
(Gordon et al., 2022), or they could be estimated using en-
tailment from some user-written statement (Bakker et al.,
2022). These computational jury functions may be neces-
sary for alignment, but evaluation would ideally be validated
by human annotators.
Different welfare function choices can lead to explicit trade-
offs between the juror utilities as well. For example, using
a class of social welfare functions (Moulin, 2004; Bakker
et al., 2022)–
wα(j1, . . . , jn) =
(  1
n
Pn
i=1 j1−α
i

1
1−α
if α ≥0, α ̸= 1
npQn
i=1 ji)
if α = 1
–one can sweep the parameter α to change the inequality
aversion from a fully Utilitarian objective (α = 0) to a
max-min/Rawlsian objective (α = ∞) (Bakker et al., 2022).
Alternatively, one could modify the utility functions as fol-
lows ˆji = 1{ji>τ} to reduce the objective to a MAX-SAT
problem. Equilibria and minimax solutions (Harsanyi et al.,
1988) are also possible, e.g. (Swamy et al., 2024).
Limitations The main limitation to this approach is that
precisely estimating the individual juror’s functions may
require a large amount of data, although this could be miti-
gated by grouping by salient characteristics (e.g., nationality
(Aroyo et al., 2023)) or using sample efficient methods
(Liu et al., 2023). Depending on the choice of welfare
function, other limitations may apply: e.g., majoritarian
welfare functions could be susceptible to tyranny of the ma-
jority and Utilitarian welfare functions to fanatical influence
(MacAskill, 2016). This approach also assumes commensu-
rability. Reported values also might not be comparable on
the same scale (Ethayarajh & Jurafsky, 2022).
Alignment Procedures and Recommendations Once we
have our jury J and a welfare function w defined, the prob-
lem reduces to one of reward maximization, and we can
leverage established alignment techniques. The main nov-
elty of the framework is in the reward modeling through
a jury. We therefore recommend further research into the
questions of 1) who to represent on a jury, 2) how to es-
timate juror functions, and 3) establishing jury-pluralistic
benchmarks to spur further innovation.
5. Current Alignment Approaches and
Pluralism
5.1. Current Alignment Approaches
AI alignment aims to guide a LLM in the direction of human
intentions and values, such as safety and accuracy (Leike
et al., 2018; Ji et al., 2024). In supervised fine-tuning, mod-
els are trained to improve instruction following (Touvron
et al., 2023; Brown et al., 2020; Achiam et al., 2023) or ex-
press certain values (Solaiman & Dennison, 2021). RLHF
uses a reward model trained on human ratings of model-
generated data to steer a model to maximize human prefer-
ences (Ouyang et al., 2022; Anthropic, 2023). Controllable
decoding steers an LLM’s output towards an objective at
inference (Liu et al., 2024; 2021; Qin et al., 2022), but often
fall short of learning-based methods on alignment bench-
marks and have not been explored with pluralism. The de-
gree of pluralism of models resulting from these approaches
7

--- Page 8 ---

Position: A Roadmap to Pluralistic Alignment
depends on many factors, including: the representativeness
of the people building the models, from designers to annota-
tors (Cotra, 2021; Perez et al., 2022; Bobu et al., 2023; Peng
et al., 2023); the richness of a dataset/LM/reward model
(Casper et al., 2023); and other factors. Mishra (2023) ar-
gues that monistic approaches to RLHF cannot meet certain
democratic properties and Siththaranjan et al. (2023) find
that RLHF underweights outliers.
5.2. Current Approaches and Pluralism
Hypothesis: Current LLM alignment techniques can
reduce distributional pluralism w.r.t. the population of
internet users.
Theoretical aspect: The language modeling cross entropy
objective may help models learn distributional pluralism. If
query x with response y appears many times in the train-
ing data written by a random internet users, cross entropy
encourages the model to output y in proportion to the popu-
lation (Ji et al., 2021) 2. Moreover, we postulate that current
alignment techniques can reduce distributional pluralism, as
the alignment procedure does not have this property.
Empirical aspect: We rely on three empirical findings that
provide an initial indication of support for our hypothesis.
Firstly, in work by Santurkar et al. (2023), questions from
Pew Research’s American Trends Panels survey data (Opin-
ionQA) were utilized to compare the distribution of LLM re-
sponses to those of US citizens. Two different model classes
(Jurassic/GPT-3) with both pre- and post-aligned models
were compared. The results revealed that post-aligned mod-
els exhibited less similarity to human populations compared
to pre-aligned models. Expanding beyond the U.S., Durmus
et al. (2023) introduced GlobalOpinionQA, an aggregation
of multinational World Values similar to OpinionQA. Al-
though their focus was solely on post-aligned models, they
observed that these models tended to concentrate the prob-
ability mass on a few answer choices, in contrast to the
dispersed answers seen in their human distributions.
In an effort to expand on these works, we further tested3
a suite of vanilla pretrained LLMs in comparison to their
corresponding “aligned" counterparts (RLHFed, finetuned
LLMs) from three model classes, LLaMA(2), Gemma, and
GPT-3. These evaluations were conducted on two distinct
multiple-choice datasets: GlobalOpinionQA, as utilized in
the study by Durmus et al. (2023), and the Machine Person-
ality Inventory (MPI), comprising 120 questions designed
to assess human personality traits (Jiang et al., 2023).
4
2This may be complicated by factors such as overfitting (with
≥1 epoch) or textual features which hint at the response; however,
within tolerance, we believe this to be a descriptive analogy.
3Code can be found at: https://github.com/jfish
er52/AI_Pluralistic_Alignment
4An analysis’s strength of distributional pluralism w.r.t. a pop-
Our target distributions were Japan and the US citizens for
GlobalOpinionQA 5 and a global population for the MPI.
We calculate Jensen-Shannon distance between the human
the model distributions, averaged over 5 prompts.
As shown in Table 1, almost all pre-aligned models have
lower Jensen-Shannon distance to the target human dis-
tribution than the post-aligned models for both datasets.6
Additionally, we also observed a post-alignment reduction
in entropy, as reported in previous work (Santurkar et al.,
2023; Durmus et al., 2023). More details can be found in
App. A and B.
These studies reveal a consistent pattern of reduced distribu-
tional variance following alignment across various domains.
Therefore, when the target distribution is diverse, such as
internet users, current alignment techniques may potentially
limit distributional pluralism. However, a more compre-
hensive investigation of this hypothesis requires large-scale
experimentation across a broader range of domains, along
with further exploration into the role of entropy.
Current alignment techniques and other forms of plu-
ralism. Overton pluralism may emerge to the degree that
users prefer it, but people’s preference bias for assertive-
ness (Hosking et al., 2023; Zhou et al., 2024) may work
against this, causing models to express support inconsis-
tently (Krügel et al., 2023). LLMs may have a degree of
steerable pluralism via prompting, but this needs to be fur-
ther evaluated. Alignment techniques for all kinds of plural-
istic benchmarks warrant further investigation.
6. Discussion
6.1. Limitations
In this work, we 1) argue that current approaches are unclear
regarding to whom/what is being aligned and 2) formalize
and discuss a set of frameworks to operationalize how to
better align models to a set of values, characteristics, or per-
spectives. However, the goal of this work is not to delineate
exactly to whom or what to align, but rather to argue for
clearer, more pluralistic approaches in alignment.
Nevertheless, several of our definitions are hard to opera-
ulation depends on the degree of representativeness of the sample.
We refer interested readers to the original dataset documentation.
5We included the U.S. due to LLMs being largely trained on En-
glish from the U.S. and selected Japan as a nation with a somewhat
distinct culture (JS-distance of .26). The choice of two nations was
made due to incomplete overlap between country pairs.
6The only exception is for GPT-3 on MPI. However, OpenAI
now only provides "davinci-02" and "gpt-3.5-turbo" as opposed
to the original "davinci" and "*-instruct" series models, so it is
difficult to confirm if "davinci-002" is indeed the base model or
what procedure was done to "gpt-3.5-turbo". Thus, we encourage
interpretion of the GPT-3 results with caution.
8

--- Page 9 ---

Position: A Roadmap to Pluralistic Alignment
Model Class
LLaMA
LLaMA2 (7B)
LLaMA2 (13B)
Gemma (7B)
GPT-3
Dataset
Pre
Alpaca
Tulu
Pre
Post
Pre
Post
Pre
Post
Pre
Post
GlobalQA (Japan)
0.40
0.45
0.54
0.47
0.57
0.40
0.55
0.33
0.51
0.42
0.43
GlobalQA (US)
0.38
0.41
0.52
0.43
0.56
0.37
0.53
0.36
0.52
0.40
0.42
GlobalQA (Germany)
0.40
0.47
0.52
0.46
0.57
0.39
0.55
0.35
0.51
0.40
0.49
MPI
0.22
0.32
0.48
0.37
0.51
0.42
0.46
0.29
0.56
0.60
0.44
Table 1. Jensen-Shannon distance (similarity) between human and model distributions on GlobalQA (target human distributions of Japan,
US, and Germany) and MPI. Note that we compare two “post" RLHF models for LLaMA (Alpaca and Tulu). Smaller (more similar)
values are in bold.
tionalize (e.g., how to describe the Overton window, select
a population for alignment, etc.). We acknowledge this
and believe that this is a necessary difficulty in order to
be precise in measuring pluralism. We attempted to make
our definitions a useful abstraction: “as simple as possi-
ble, but not simpler" (Ratcliffe, 2016). Further abstracting
away these details would remove the required nuance of the
evaluations. Any design decisions, along with their limita-
tions and assumptions, must be carefully justified. Although
some alignment techniques may require automatic meth-
ods (e.g., jury functions), we advocate for human-centered
evaluations whenever possible.
We recognize that not all of our definitions of pluralism
are necessarily desirable in all cases. For example, distri-
butional pluralism may be helpful in using LLMs to study
culture (Buttrick, 2024) or creative domains (Shanahan &
Clarke, 2023), but may not be desirable in controlled envi-
ronments such as customer support. Additionally, it may
not be possible for a single model to satisfy all conditions:
e.g., Overton pluralism may be at odds with distributional
pluralism. Rather, our definitions are useful abstractions to
understand how models and benchmarks can be pluralistic,
and each applies in a different domain.
6.2. Relation to Prior Work
There has been a growing sense in the community of the im-
portance of measuring which values and to whom we are try-
ing to align LLMs (Kasirzadeh & Gabriel, 2022; Wang et al.,
2023b). While some previous work has shed valuable light
on these questions (Santurkar et al., 2023), our work goes
further in 1) unifying disparate approaches under concrete
definitions of pluralism (e.g., distributional), 2) proposing
previously unexplored (to our knowledge) kinds of plural-
ism (e.g., Overton), and 3) arguing that, in many cases, it
may actually be desirable to increase certain measures of
pluralism as opposed to merely using them as probes, in
contrast to other work (Santurkar et al., 2023; Durmus et al.,
2023; Feng et al., 2023).
6.3. Pluralism in Broader AI Systems
In this work, we focused largely on LLMs. However, we
believe that our definitions generalize broadly to other AI
systems. In general, the query/response framework may
be applied to any set of inputs/outputs, whether actions,
images, audio, or any other modality. For example, it may
be desirable for agents to be steerably pluralistic to be able
to customize to users needs. Distributional pluralism may
be useful in modeling potential actions that agents may take,
such as drivers on a road. There may be less of a need for
pluralism in areas where there is a single correct objective
to optimize - e.g., efficiency of a system, performance in a
2-player game. However, there is a broad set of subjective
tasks where pluralism is a valuable consideration.
7. Conclusion
In this work, we have argued for increased and more
precisely-directed attention on pluralism and the alignment
of AI systems. We also formalized three definitions of plu-
ralistic models and three forms of pluralistic benchmarks.
We argue that while current alignment techniques have made
remarkable progress, new methodologies for measuring and
aligning are needed.
While we thread specific recommendations for each kind
of pluralism throughout the work, we sketch some broad
recommendations here: 1) more research into finegrained
pluralistic evaluations to better characterize current models;
2) continued normative discussions about to what we want
to align and desirable customization bounds; 3) additional
alignment techniques to create more pluralistic models.
Impact Statement
We hope that this work leads to positive impact in encourag-
ing work in AI systems that work better with a diverse set of
people. Throughout the work, we have discussed potential
limitations and risks for each proposed definition. Addi-
tionally, this work, along with any other work in machine
learning, has potential for dual use: aligning to attributes
which may cause harm, etc. However, as our work is more
9

--- Page 10 ---

Position: A Roadmap to Pluralistic Alignment
theoretical, we believe that the positive impact to discus-
sions around pluralism in alignment outweigh any marginal
potential for dual use, which we believe to be minimal.
Acknowledgments
The authors thank Ben Newman, Joongwon Kim, Victoria
Ebert, Zaid Harchaoui, and Iason Gabriel for helpful feed-
back. This research was supported in part by DARPA under
the ITM program (FA8650-23-C-7316), the Office of Naval
Research (N00014-24-1-2207), the Institute for Humane
Studies (IHS018186), and the Allen Institute for AI.
References
Oxford English Dictionary, s.v. “Overton window (n.)”, July
2023. URL https://doi.org/10.1093/OED/
1985277434.
Achiam, O. J., Adler, S., Agarwal, S., Ahmad, L., Akkaya,
I., Aleman, F. L., Almeida, D., Altenschmidt, J., Altman,
S., Anadkat, S., Avila, R., Babuschkin, I., Balaji, S., Bal-
com, V., Baltescu, P., Bao, H., Bavarian, M., Belgum,
J., Bello, I., Berdine, J., Bernadett-Shapiro, G., Berner,
C., Bogdonoff, L., Boiko, O., Boyd, M., Brakman, A.-L.,
Brockman, G., Brooks, T., Brundage, M., Button, K.,
Cai, T., Campbell, R., Cann, A., Carey, B., Carlson, C.,
Carmichael, R., Chan, B., Chang, C., Chantzis, F., Chen,
D., Chen, S., Chen, R., Chen, J., Chen, M., Chess, B.,
Cho, C., Chu, C., Chung, H. W., Cummings, D., Currier,
J., Dai, Y., Decareaux, C., Degry, T., Deutsch, N., Dev-
ille, D., Dhar, A., Dohan, D., Dowling, S., Dunning, S.,
Ecoffet, A., Eleti, A., Eloundou, T., Farhi, D., Fedus, L.,
Felix, N., Fishman, S. P., Forte, J., Fulford, I., Gao, L.,
Georges, E., Gibson, C., Goel, V., Gogineni, T., Goh, G.,
Gontijo-Lopes, R., Gordon, J., Grafstein, M., Gray, S.,
Greene, R., Gross, J., Gu, S. S., Guo, Y., Hallacy, C., Han,
J., Harris, J., He, Y., Heaton, M., Heidecke, J., Hesse, C.,
Hickey, A., Hickey, W., Hoeschele, P., Houghton, B., Hsu,
K., Hu, S., Hu, X., Huizinga, J., Jain, S., Jain, S., Jang, J.,
Jiang, A., Jiang, R., Jin, H., Jin, D., Jomoto, S., Jonn, B.,
Jun, H., Kaftan, T., Kaiser, L., Kamali, A., Kanitscheider,
I., Keskar, N. S., Khan, T., Kilpatrick, L., Kim, J. W.,
Kim, C., Kim, Y., Kirchner, H., Kiros, J. R., Knight, M.,
Kokotajlo, D., Kondraciuk, L., Kondrich, A., Konstantini-
dis, A., Kosic, K., Krueger, G., Kuo, V., Lampe, M., Lan,
I., Lee, T., Leike, J., Leung, J., Levy, D., Li, C. M., Lim,
R., Lin, M., Lin, S., Litwin, M., Lopez, T., Lowe, R., Lue,
P., Makanju, A. A., Malfacini, K., Manning, S., Markov,
T., Markovski, Y., Martin, B., Mayer, K., Mayne, A., Mc-
Grew, B., McKinney, S. M., McLeavey, C., McMillan,
P., McNeil, J., Medina, D., Mehta, A., Menick, J., Metz,
L., Mishchenko, A., Mishkin, P., Monaco, V., Morikawa,
E., Mossing, D. P., Mu, T., Murati, M., Murk, O., M’ely,
D., Nair, A., Nakano, R., Nayak, R., Neelakantan, A.,
Ngo, R., Noh, H., Long, O., O’Keefe, C., Pachocki, J. W.,
Paino, A., Palermo, J., Pantuliano, A., Parascandolo, G.,
Parish, J., Parparita, E., Passos, A., Pavlov, M., Peng,
A., Perelman, A., de Avila Belbute Peres, F., Petrov, M.,
de Oliveira Pinto, H. P., Pokorny, M., Pokrass, M., Pong,
V. H., Powell, T., Power, A., Power, B., Proehl, E., Puri,
R., Radford, A., Rae, J., Ramesh, A., Raymond, C., Real,
F., Rimbach, K., Ross, C., Rotsted, B., Roussez, H., Ry-
der, N., Saltarelli, M. D., Sanders, T., Santurkar, S., Sas-
try, G., Schmidt, H., Schnurr, D., Schulman, J., Selsam,
D., Sheppard, K., Sherbakov, T., Shieh, J., Shoker, S.,
Shyam, P., Sidor, S., Sigler, E., Simens, M., Sitkin, J.,
Slama, K., Sohl, I., Sokolowsky, B. D., Song, Y., Stau-
10

--- Page 11 ---

Position: A Roadmap to Pluralistic Alignment
dacher, N., Such, F. P., Summers, N., Sutskever, I., Tang,
J., Tezak, N. A., Thompson, M., Tillet, P., Tootoonchian,
A., Tseng, E., Tuggle, P., Turley, N., Tworek, J., Uribe, J.
F. C., Vallone, A., Vijayvergiya, A., Voss, C., Wainwright,
C., Wang, J. J., Wang, A., Wang, B., Ward, J., Wei, J.,
Weinmann, C., Welihinda, A., Welinder, P., Weng, J.,
Weng, L., Wiethoff, M., Willner, D., Winter, C., Wolrich,
S., Wong, H., Workman, L., Wu, S., Wu, J., Wu, M.,
Xiao, K., Xu, T., Yoo, S., Yu, K., Yuan, Q., Zaremba,
W., Zellers, R., Zhang, C., Zhang, M., Zhao, S., Zheng,
T., Zhuang, J., Zhuk, W., and Zoph, B. Gpt-4 technical
report. 2023. URL https://api.semanticscho
lar.org/CorpusID:257532815.
Aher, G. V., Arriaga, R. I., and Kalai, A. T. Using large lan-
guage models to simulate multiple humans and replicate
human subject studies. In International Conference on
Machine Learning, pp. 337–371. PMLR, 2023.
Anthropic. Introducing claude, 2023. URL https://ww
w.anthropic.com/index/introducing-cla
ude.
Argyle, L., Busby, E., Fulda, N., Gubler, J., Rytting, C., and
Wingate, D. Out of one, many: Using language models
to simulate human samples. Political Analysis, 31:1–15,
02 2023. doi: 10.1017/pan.2023.2.
Arnesen, S. and Peters, Y. The legitimacy of represen-
tation: How descriptive, formal, and responsiveness
representation affect the acceptability of political deci-
sions. Comparative Political Studies, 51(7):868–899,
2018. doi: 10.1177/0010414017720702. URL https:
//doi.org/10.1177/0010414017720702.
Aroyo, L., Taylor, A. S., Diaz, M., Homan, C. M., Parrish,
A., Serapio-Garcia, G., Prabhakaran, V., and Wang, D.
Dices dataset: Diversity in conversational ai evaluation
for safety, 2023.
Askell, A., Bai, Y., Chen, A., Drain, D., Ganguli, D.,
Henighan, T., Jones, A., Joseph, N., Mann, B., Das-
Sarma, N., Elhage, N., Hatfield-Dodds, Z., Hernandez,
D., Kernion, J., Ndousse, K., Olsson, C., Amodei, D.,
Brown, T., Clark, J., McCandlish, S., Olah, C., and Ka-
plan, J. A general language assistant as a laboratory for
alignment, 2021.
Bai, Y., Jones, A., Ndousse, K., Askell, A., Chen, A., Das-
Sarma, N., Drain, D., Fort, S., Ganguli, D., Henighan,
T., Joseph, N., Kadavath, S., Kernion, J., Conerly, T.,
El-Showk, S., Elhage, N., Hatfield-Dodds, Z., Hernan-
dez, D., Hume, T., Johnston, S., Kravec, S., Lovitt, L.,
Nanda, N., Olsson, C., Amodei, D., Brown, T., Clark, J.,
McCandlish, S., Olah, C., Mann, B., and Kaplan, J. Train-
ing a helpful and harmless assistant with reinforcement
learning from human feedback, 2022a.
Bai, Y., Kadavath, S., Kundu, S., Askell, A., Kernion, J.,
Jones, A., Chen, A., Goldie, A., Mirhoseini, A., McKin-
non, C., Chen, C., Olsson, C., Olah, C., Hernandez, D.,
Drain, D., Ganguli, D., Li, D., Tran-Johnson, E., Perez,
E., Kerr, J., Mueller, J., Ladish, J., Landau, J., Ndousse,
K., Lukosuite, K., Lovitt, L., Sellitto, M., Elhage, N.,
Schiefer, N., Mercado, N., DasSarma, N., Lasenby, R.,
Larson, R., Ringer, S., Johnston, S., Kravec, S., Showk,
S. E., Fort, S., Lanham, T., Telleen-Lawton, T., Conerly,
T., Henighan, T., Hume, T., Bowman, S. R., Hatfield-
Dodds, Z., Mann, B., Amodei, D., Joseph, N., McCan-
dlish, S., Brown, T., and Kaplan, J. Constitutional ai:
Harmlessness from ai feedback, 2022b.
Bakker, M. A., Chadwick, M. J., Sheahan, H. R., Tessler,
M. H., Campbell-Gillingham, L., Balaguer, J., McAleese,
N., Glaese, A., Aslanides, J., Botvinick, M. M., and
Summerfield, C. Fine-tuning language models to find
agreement among humans with diverse preferences, 2022.
Berlin, I. Two concepts of liberty. In Four Essays on Liberty,
pp. 118–172. Oxford University Press, Oxford, 1969.
Bobu, A., Peng, A., Agrawal, P., Shah, J., and Dragan, A. D.
Aligning robot and human representations. arXiv preprint
arXiv:2302.01928, 2023.
Bommasani, R., Hudson, D. A., Adeli, E., Altman, R.,
Arora, S., von Arx, S., Bernstein, M. S., Bohg, J., Bosse-
lut, A., Brunskill, E., Brynjolfsson, E., Buch, S., Card, D.,
Castellon, R., Chatterji, N. S., Chen, A. S., Creel, K. A.,
Davis, J., Demszky, D., Donahue, C., Doumbouya, M.,
Durmus, E., Ermon, S., Etchemendy, J., Ethayarajh, K.,
Fei-Fei, L., Finn, C., Gale, T., Gillespie, L., Goel, K.,
Goodman, N. D., Grossman, S., Guha, N., Hashimoto,
T., Henderson, P., Hewitt, J., Ho, D. E., Hong, J., Hsu,
K., Huang, J., Icard, T. F., Jain, S., Jurafsky, D., Kalluri,
P., Karamcheti, S., Keeling, G., Khani, F., Khattab, O.,
Koh, P. W., Krass, M. S., Krishna, R., Kuditipudi, R.,
Kumar, A., Ladhak, F., Lee, M., Lee, T., Leskovec, J.,
Levent, I., Li, X. L., Li, X., Ma, T., Malik, A., Man-
ning, C. D., Mirchandani, S., Mitchell, E., Munyikwa,
Z., Nair, S., Narayan, A., Narayanan, D., Newman, B.,
Nie, A., Niebles, J. C., Nilforoshan, H., Nyarko, J. F.,
Ogut, G., Orr, L. J., Papadimitriou, I., Park, J. S., Piech,
C., Portelance, E., Potts, C., Raghunathan, A., Reich, R.,
Ren, H., Rong, F., Roohani, Y. H., Ruiz, C., Ryan, J.,
R’e, C., Sadigh, D., Sagawa, S., Santhanam, K., Shih, A.,
Srinivasan, K. P., Tamkin, A., Taori, R., Thomas, A. W.,
Tramèr, F., Wang, R. E., Wang, W., Wu, B., Wu, J., Wu,
Y., Xie, S. M., Yasunaga, M., You, J., Zaharia, M. A.,
Zhang, M., Zhang, T., Zhang, X., Zhang, Y., Zheng, L.,
Zhou, K., and Liang, P. On the opportunities and risks of
foundation models. ArXiv, abs/2108.07258, 2021. URL
https://arxiv.org/pdf/2108.07258.pdf.
11

--- Page 12 ---

Position: A Roadmap to Pluralistic Alignment
Bowman, S. R., Hyun, J., Perez, E., Chen, E., Pettit, C.,
Heiner, S., Lukoši¯ut˙e, K., Askell, A., Jones, A., Chen,
A., Goldie, A., Mirhoseini, A., McKinnon, C., Olah, C.,
Amodei, D., Amodei, D., Drain, D., Li, D., Tran-Johnson,
E., Kernion, J., Kerr, J., Mueller, J., Ladish, J., Landau, J.,
Ndousse, K., Lovitt, L., Elhage, N., Schiefer, N., Joseph,
N., Mercado, N., DasSarma, N., Larson, R., McCandlish,
S., Kundu, S., Johnston, S., Kravec, S., Showk, S. E.,
Fort, S., Telleen-Lawton, T., Brown, T., Henighan, T.,
Hume, T., Bai, Y., Hatfield-Dodds, Z., Mann, B., and
Kaplan, J. Measuring progress on scalable oversight for
large language models, 2022.
Boykoff, M. T. and Boykoff, J. M. Balance as bias: global
warming and the us prestige press. Global Environmental
Change, 14(2):125–136, 2004. ISSN 0959-3780. doi:
https://doi.org/10.1016/j.gloenvcha.2003.10.001. URL
https://www.sciencedirect.com/scienc
e/article/pii/S0959378003000669.
Brown, T. B., Mann, B., Ryder, N., Subbiah, M., Kaplan,
J., Dhariwal, P., Neelakantan, A., Shyam, P., Sastry, G.,
Askell, A., Agarwal, S., Herbert-Voss, A., Krueger, G.,
Henighan, T. J., Child, R., Ramesh, A., Ziegler, D. M.,
Wu, J., Winter, C., Hesse, C., Chen, M., Sigler, E., Litwin,
M., Gray, S., Chess, B., Clark, J., Berner, C., McCandlish,
S., Radford, A., Sutskever, I., and Amodei, D. Language
models are few-shot learners. ArXiv, abs/2005.14165,
2020. URL https://api.semanticscholar.
org/CorpusID:218971783.
Buttrick, N.
Studying large language models as com-
pression algorithms for human culture. Trends in Cog-
nitive Sciences, S1364-6613(24):00001–9, 2024. doi:
10.1016/j.tics.2024.01.001. Epub ahead of print.
Casper, S., Davies, X., Shi, C., Gilbert, T. K., Scheurer,
J., Rando, J., Freedman, R., Korbak, T., Lindner, D.,
Freire, P., Wang, T., Marks, S., Ségerie, C.-R., Carroll,
M., Peng, A., Christoffersen, P. J., Damani, M., Slocum,
S., Anwar, U., Siththaranjan, A., Nadeau, M., Michaud,
E. J., Pfau, J., Krasheninnikov, D., Chen, X., di Langosco,
L. L., Hase, P., Biyik, E., Dragan, A. D., Krueger, D.,
Sadigh, D., and Hadfield-Menell, D. Open problems and
fundamental limitations of reinforcement learning from
human feedback. ArXiv, abs/2307.15217, 2023. URL
https://api.semanticscholar.org/Corp
usID:260316010.
Chen, J., Liu, Z., Huang, X., Wu, C., Liu, Q., Jiang, G.,
Pu, Y., Lei, Y., Chen, X., Wang, X., Lian, D., and Chen,
E. When large language models meet personalization:
Perspectives of challenges and opportunities, 2023.
Chen, L., Lu, K., Rajeswaran, A., Lee, K., Grover, A.,
Laskin, M., Abbeel, P., Srinivas, A., and Mordatch, I. De-
cision transformer: Reinforcement learning via sequence
modeling, 2021.
Cotra, A. Why ai alignment could be hard with modern deep
learning. https://www.cold-takes.com/why
-ai-alignment-could-be-hard-with-mod
ern-deep-learning/, 2021.
Crenshaw, K.
Demarginalizing the intersection of race
and sex: A black feminist critique of antidiscrimination
doctrine, feminist theory and antiracist politics. The Uni-
versity of Chicago Legal Forum, 140:139–167, 1989.
Danry, V., Pataranutaporn, P., Mao, Y., and Maes, P. Don’t
just tell me, ask me: Ai systems that intelligently frame
explanations as questions improve human logical dis-
cernment accuracy over causal ai explanations. In Pro-
ceedings of the 2023 CHI Conference on Human Fac-
tors in Computing Systems, CHI ’23, New York, NY,
USA, 2023. Association for Computing Machinery. ISBN
9781450394215. doi: 10.1145/3544548.3580672. URL
https://doi.org/10.1145/3544548.3580
672.
de Tocqueville, A. Democracy in America. 1835.
Durmus, E., Nyugen, K., Liao, T. I., Schiefer, N., Askell,
A., Bakhtin, A., Chen, C., Hatfield-Dodds, Z., Hernan-
dez, D., Joseph, N., Lovitt, L., McCandlish, S., Sikder,
O., Tamkin, A., Thamkul, J., Kaplan, J., Clark, J., and
Ganguli, D. Towards measuring the representation of sub-
jective global opinions in language models, 2023. URL
https://api.semanticscholar.org/Corp
usID:259275051.
Ethayarajh, K. and Jurafsky, D. Utility is in the eye of the
user: A critique of nlp leaderboard design. In Conference
on Empirical Methods in Natural Language Processing,
2020. URL https://api.semanticscholar.
org/CorpusID:235408131.
Ethayarajh, K. and Jurafsky, D. The authenticity gap in
human evaluation. In Goldberg, Y., Kozareva, Z., and
Zhang, Y. (eds.), Proceedings of the 2022 Conference on
Empirical Methods in Natural Language Processing, pp.
6056–6070, Abu Dhabi, United Arab Emirates, Decem-
ber 2022. Association for Computational Linguistics. doi:
10.18653/v1/2022.emnlp-main.406. URL https://
aclanthology.org/2022.emnlp-main.406.
Feng, S., Park, C. Y., Liu, Y., and Tsvetkov, Y.
From
pretraining data to language models to downstream tasks:
Tracking the trails of political biases leading to unfair nlp
models, 2023.
Flanigan, B., Gölz, P., Gupta, A., Hennig, B., and Procaccia,
A. D. Fair algorithms for selecting citizens’assemblies.
12

--- Page 13 ---

Position: A Roadmap to Pluralistic Alignment
Nature, 596(7873):548–552, 2021. doi: 10.1038/s41586
-021-03788-6. URL https://doi.org/10.1038/
s41586-021-03788-6.
Fleisig, E., Abebe, R., and Klein, D. When the Majority is
Wrong: Modeling Annotator Disagreement for Subjective
Tasks, November 2023. URL http://arxiv.org/
abs/2305.06626. arXiv:2305.06626 [cs].
Gabriel, I. Artificial intelligence, values, and alignment.
Minds and Machines, 30(3):411–437, 2020. doi: 10.100
7/s11023-020-09539-2. URL https://doi.org/
10.1007/s11023-020-09539-2.
Girotra, K., Meincke, L., Terwiesch, C., and Ulrich,
K. T. Ideas are dimes a dozen: Large language mod-
els for idea generation in innovation.
https://
ssrn.com/abstract=4526071, July 2023.
Available at SSRN: https://ssrn.com/abstract=4526071
or http://dx.doi.org/10.2139/ssrn.4526071.
Glaese, A., McAleese, N., Tr˛ebacz, M., Aslanides, J.,
Firoiu, V., Ewalds, T., Rauh, M., Weidinger, L., Chad-
wick, M., Thacker, P., Campbell-Gillingham, L., Ue-
sato, J., Huang, P.-S., Comanescu, R., Yang, F., See, A.,
Dathathri, S., Greig, R., Chen, C., Fritz, D., Elias, J. S.,
Green, R., Mokrá, S., Fernando, N., Wu, B., Foley, R.,
Young, S., Gabriel, I., Isaac, W., Mellor, J., Hassabis, D.,
Kavukcuoglu, K., Hendricks, L. A., and Irving, G. Im-
proving alignment of dialogue agents via targeted human
judgements, 2022.
Gordon, M. L., Lam, M. S., Park, J. S., Patel, K., Han-
cock, J., Hashimoto, T., and Bernstein, M. S. Jury learn-
ing: Integrating dissenting voices into machine learn-
ing models. In CHI Conference on Human Factors in
Computing Systems, CHI ’22. ACM, April 2022. doi:
10.1145/3491102.3502004. URL http://dx.doi.o
rg/10.1145/3491102.3502004.
Guerreiro, A. P., Fonseca, C. M., and Paquete, L. The
hypervolume indicator. ACM Computing Surveys (CSUR),
54:1–42, 2020. URL https://api.semanticsc
holar.org/CorpusID:218470181.
Haraway, D. Situated knowledges: The science question in
feminism and the privilege of partial perspective. Feminist
Studies, 14(3):575–599, 1988. ISSN 00463663. URL
http://www.jstor.org/stable/3178066.
Harsanyi, J. C., Selten, R., et al. A general theory of equi-
librium selection in games. MIT Press Books, 1, 1988.
Hartmann, J., Schwenzow, J., and Witte, M. The political
ideology of conversational ai: Converging evidence on
chatgpt’s pro-environmental, left-libertarian orientation,
2023.
Hayati, S. A., Lee, M., Rajagopal, D., and Kang, D. How
far can we extract diverse perspectives from large lan-
guage models? criteria-based diversity prompting! ArXiv,
abs/2311.09799, 2023. URL https://api.semant
icscholar.org/CorpusID:265220883.
Hayes, C. F., R˘adulescu, R., Bargiacchi, E., Källström,
J., Macfarlane, M., Reymond, M., Verstraeten, T., Zint-
graf, L. M., Dazeley, R., Heintz, F., Howley, E., Iris-
sappane, A. A., Mannion, P., Nowé, A., Ramos, G.,
Restelli, M., Vamplew, P., and Roijers, D. M. A practi-
cal guide to multi-objective reinforcement learning and
planning.
Autonomous Agents and Multi-Agent Sys-
tems, 36(1):26, April 2022.
ISSN 1573-7454.
doi:
10.1007/s10458-022-09552-y. URL http://dx
.doi.org/10.1007/s10458-022-09552-y.
Hendrycks, D., Burns, C., Basart, S., Critch, A., Li, J., Song,
D., and Steinhardt, J. Aligning ai with shared human
values. arXiv preprint arXiv:2008.02275, 2020.
Hendrycks, D., Burns, C., Basart, S., Critch, A., Li, J., Song,
D., and Steinhardt, J. Aligning ai with shared human
values, 2023.
Henrich, J., Heine, S. J., and Norenzayan, A. The weirdest
people in the world? Behavioral and Brain Sciences, 33
(2-3):61–83, 2010. URL http://www2.psych.ubc
.ca/~henrich/audiofiles/WEIRD1.mp3.
Hosking, T., Blunsom, P., and Bartolo, M. Human feedback
is not gold standard. ArXiv, abs/2309.16349, 2023. URL
https://api.semanticscholar.org/Corp
usID:263134280.
Hsieh, N.-h. and Andersson, H. Incommensurable Values.
In Zalta, E. N. (ed.), The Stanford Encyclopedia of Phi-
losophy. Metaphysics Research Lab, Stanford University,
Fall 2021 edition, 2021.
Hwang, E., Majumder, B. P., and Tandon, N. Aligning
Language Models to User Opinions. 2023. doi: 10.48550
/ARXIV.2305.14929. URL https://arxiv.org/
abs/2305.14929. Publisher: arXiv Version Number:
1.
Imundo, M. and Rapp, D. When fairness is flawed: Ef-
fects of false balance reporting and weight-of-evidence
statements on beliefs and perceptions of climate change.
Journal of Applied Research in Memory and Cognition,
11, 10 2021. doi: 10.1016/j.jarmac.2021.10.002.
Jakesch, M., Bhat, A., Buschek, D., Zalmanson, L., and
Naaman, M. Co-writing with opinionated language mod-
els affects users’ views.
In Proceedings of the 2023
CHI Conference on Human Factors in Computing Sys-
tems, CHI ’23, New York, NY, USA, 2023. Associa-
tion for Computing Machinery. ISBN 9781450394215.
13

--- Page 14 ---

Position: A Roadmap to Pluralistic Alignment
doi: 10.1145/3544548.3581196.
URL https:
//doi.org/10.1145/3544548.3581196.
Jang, J., Kim, S., Lin, B. Y., Wang, Y., Hessel, J., Zettle-
moyer, L., Hajishirzi, H., Choi, Y., and Ammanabrolu, P.
Personalized soups: Personalized large language model
alignment via post-hoc parameter merging, 2023.
Ji, J., Qiu, T., Chen, B., Zhang, B., Lou, H., Wang, K., Duan,
Y., He, Z., Zhou, J., Zhang, Z., Zeng, F., Ng, K. Y., Dai,
J., Pan, X., O’Gara, A., Lei, Y., Xu, H., Tse, B., Fu, J.,
McAleer, S., Yang, Y., Wang, Y., Zhu, S.-C., Guo, Y., and
Gao, W. Ai alignment: A comprehensive survey, 2024.
Ji, Z., Li, J. D., and Telgarsky, M. Early-stopped neural
networks are consistent, 2021.
Jiang, G., Xu, M., Zhu, S.-C., Han, W., Zhang, C., and Zhu,
Y. Evaluating and inducing personality in pre-trained
language models, 2023. URL https://api.sema
nticscholar.org/CorpusID:258865158.
Jiang, H., Beeferman, D., Roy, B., and Roy, D.
Com-
munitylm: Probing partisan worldviews from language
models, 2022.
Jung, J., Qin, L., Welleck, S., Brahman, F., Bhagavatula, C.,
Bras, R. L., and Choi, Y. Maieutic prompting: Logically
consistent reasoning with recursive explanations, 2022.
Kant, I. Kant: Critique of Practical Reason. Cambridge
Texts in the History of Philosophy. Cambridge University
Press, 2 edition, 1788. doi: 10.1017/CBO97813161364
78.
Kasirzadeh, A. and Gabriel, I. In conversation with artifi-
cial intelligence: aligning language models with human
values, 2022.
Kekes, J. The Morality of Pluralism. Princeton University
Press, Princeton, 1993.
Kim, J. and Lee, B. Ai-augmented surveys: Leveraging
large language models for opinion prediction in nationally
representative surveys. arXiv preprint arXiv:2305.09620,
2023.
Kirk, R., Mediratta, I., Nalmpantis, C., Luketina, J., Ham-
bro, E., Grefenstette, E., and Raileanu, R. Understanding
the effects of rlhf on llm generalisation and diversity,
2024.
Koster, R., Balaguer, J., Tacchetti, A., Weinstein, A., Zhu,
T., Hauser, O., Williams, D., Campbell-Gillingham, L.,
Thacker, P., Botvinick, M., and Summerfield, C. Human-
centred mechanism design with democratic ai. Nature
Human Behaviour, 6(10):1398–1407, 2022. doi: 10.103
8/s41562-022-01383-x. URL https://doi.org/
10.1038/s41562-022-01383-x.
Krügel, S., Ostermaier, A., and Uhl, M. Chatgpt’s incon-
sistent moral advice influences users’judgment. Scien-
tific Reports, 13(1):4569, Apr 2023. ISSN 2045-2322.
doi: 10.1038/s41598-023-31341-0. URL https:
//doi.org/10.1038/s41598-023-31341-0.
Landemore, H. and Page, S. E. Deliberation and disagree-
ment: Problem solving, prediction, and positive dissensus.
Politics, philosophy & economics, 14(3):229–254, 2015.
Leike, J., Krueger, D., Everitt, T., Martic, M., Maini, V., and
Legg, S. Scalable agent alignment via reward modeling:
a research direction, 2018.
Li, C., Zhang, M., Mei, Q., Wang, Y., Hombaiah, S. A.,
Liang, Y., and Bendersky, M. Teach llms to personalize –
an approach inspired by writing education, 2023a.
Li, J., Mehrabi, N., Peris, C., Goyal, P., Chang, K.-W.,
Galstyan, A., Zemel, R., and Gupta, R. On the steerability
of large language models toward data-driven personas.
2023b. doi: 10.48550/ARXIV.2311.04978. URL ht
tps://arxiv.org/abs/2311.04978. Publisher:
arXiv Version Number: 1.
Liang, P., Bommasani, R., Lee, T., Tsipras, D., Soylu, D.,
Yasunaga, M., Zhang, Y., Narayanan, D., Wu, Y., Kumar,
A., Newman, B., Yuan, B., Yan, B., Zhang, C., Cosgrove,
C., Manning, C. D., Ré, C., Acosta-Navas, D., Hudson,
D. A., Zelikman, E., Durmus, E., Ladhak, F., Rong, F.,
Ren, H., Yao, H., Wang, J., Santhanam, K., Orr, L., Zheng,
L., Yuksekgonul, M., Suzgun, M., Kim, N., Guha, N.,
Chatterji, N., Khattab, O., Henderson, P., Huang, Q., Chi,
R., Xie, S. M., Santurkar, S., Ganguli, S., Hashimoto, T.,
Icard, T., Zhang, T., Chaudhary, V., Wang, W., Li, X.,
Mai, Y., Zhang, Y., and Koreeda, Y. Holistic evaluation
of language models, 2023.
Liu, A., Sap, M., Lu, X., Swayamdipta, S., Bhagavatula,
C., Smith, N. A., and Choi, Y. Dexperts: Decoding-time
controlled text generation with experts and anti-experts.
In Annual Meeting of the Association for Computational
Linguistics, 2021. URL https://api.semantic
scholar.org/CorpusID:235313967.
Liu, A., Swayamdipta, S., Smith, N. A., and Choi, Y. Wanli:
Worker and ai collaboration for natural language infer-
ence dataset creation, 2022.
Liu, A., Han, X., Wang, Y., Tsvetkov, Y., Choi, Y., and
Smith, N. A. Tuning language models by proxy, 2024.
Liu, N. F., Kumar, A., Liang, P., and Jia, R. Are sample-
efficient nlp models more robust?, 2023.
Long, J.
Large language model guided tree-of-thought.
arXiv preprint arXiv:2305.08291, 2023.
14

--- Page 15 ---

Position: A Roadmap to Pluralistic Alignment
Lu, X., West, P., Zellers, R., Bras, R. L., Bhagavatula, C.,
and Choi, Y. Neurologic decoding: (un)supervised neural
text generation with predicate logic constraints. ArXiv,
abs/2010.12884, 2020. URL https://api.semant
icscholar.org/CorpusID:225067055.
Lu, X., Welleck, S., Hessel, J., Jiang, L., Qin, L., West, P.,
Ammanabrolu, P., and Choi, Y. Quark: Controllable text
generation with reinforced unlearning, 2022.
Ma, X., Mishra, S., Liu, A., Su, S., Chen, J., Kulkarni, C.,
Cheng, H.-T., Le, Q., and Chi, E. Beyond chatbots: Ex-
plorellm for structured thoughts and personalized model
responses, 2023.
MacAskill, W. Normative Uncertainty as a Voting Problem.
Mind, 125(500):967–1004, October 2016. ISSN 0026-
4423. doi: 10.1093/mind/fzv169. URL https://doi.
org/10.1093/mind/fzv169.
Michael, J., Mahdi, S., Rein, D., Petty, J., Dirani, J., Pad-
makumar, V., and Bowman, S. R. Debate helps super-
vise unreliable experts. arXiv preprint arXiv:2311.08702,
2023.
Min, S., Michael, J., Hajishirzi, H., and Zettlemoyer, L. Am-
bigQA: Answering ambiguous open-domain questions.
In Webber, B., Cohn, T., He, Y., and Liu, Y. (eds.), Pro-
ceedings of the 2020 Conference on Empirical Methods in
Natural Language Processing (EMNLP), pp. 5783–5797,
Online, November 2020. Association for Computational
Linguistics. doi: 10.18653/v1/2020.emnlp-main.466.
URL https://aclanthology.org/2020.em
nlp-main.466.
Mishra, A. Ai alignment and social choice: Fundamental
limitations and policy implications, 2023.
Moulin, H. Fair Division and Collective Welfare. MIT
Press, 2004.
Nagel, T. The fragmentation of value. In Mortal Questions.
Cambridge University Press, Cambridge, 1979.
OpenAI. Openai davinci-002 model. https://www.op
enai.com, 2023a. Accessed on Date 06/2023.
OpenAI. Openai gpt3.5-turbo. https://www.openai
.com, 2023b. Accessed on Date 06/2023.
Ouyang, L., Wu, J., Jiang, X., Almeida, D., Wainwright,
C. L., Mishkin, P., Zhang, C., Agarwal, S., Slama, K.,
Ray, A., Schulman, J., Hilton, J., Kelton, F., Miller, L.,
Simens, M., Askell, A., Welinder, P., Christiano, P., Leike,
J., and Lowe, R. Training language models to follow
instructions with human feedback, 2022.
Ovadya, A. Reimagining democracy for ai. Journal of
Democracy, 34(4):162–170, Oct 2023.
Page, S. The difference: How the power of diversity creates
better groups, firms, schools, and societies-new edition.
Princeton University Press, 2008.
Page, S. E. The diversity bonus: How great teams pay off
in the knowledge economy. Princeton University Press,
2019.
Pan, A., Chan, J. S., Zou, A., Li, N., Basart, S., Woodside,
T., Ng, J., Zhang, H., Emmons, S., and Hendrycks, D.
Do the rewards justify the means? measuring trade-offs
between rewards and ethical behavior in the machiavelli
benchmark, 2023.
Park, J. S., Popowski, L., Cai, C. J., Morris, M. R., Liang,
P., and Bernstein, M. S. Social simulacra: Creating popu-
lated prototypes for social computing systems, 2022.
Park, J. S., O’Brien, J., Cai, C. J., Morris, M. R., Liang,
P., and Bernstein, M. S. Generative agents: Interactive
simulacra of human behavior. In Proceedings of the 36th
Annual ACM Symposium on User Interface Software and
Technology, pp. 1–22, 2023.
Peng, A., Netanyahu, A., Ho, M. K., Shu, T., Bobu, A., Shah,
J., and Agrawal, P. Diagnosis, feedback, adaptation: A
human-in-the-loop framework for test-time policy adapta-
tion. In Proceedings of the 40th International Conference
on Machine Learning, 2023.
Perez, E., Ringer, S., Lukoši¯ut˙e, K., Nguyen, K., Chen, E.,
Heiner, S., Pettit, C., Olsson, C., Kundu, S., Kadavath, S.,
et al. Discovering language model behaviors with model-
written evaluations. arXiv preprint arXiv:2212.09251, pp.
13387–13434, July 2022. doi: 10.18653/v1/2023.finding
s-acl.847. URL https://aclanthology.org/2
023.findings-acl.847.
Pew Research Center. The state of online harassment. Tech-
nical report, Washington, D.C., January 2021.
URL
https://www.pewresearch.org/internet
/2021/01/13/the-state-of-online-haras
sment/.
Qin, L., Welleck, S., Khashabi, D., and Choi, Y. Cold
decoding: Energy-based constrained text generation with
langevin dynamics. ArXiv, abs/2202.11705, 2022. URL
https://api.semanticscholar.org/Corp
usID:247058662.
Ramezani, A. and Xu, Y. Knowledge of cultural moral
norms in large language models, 2023.
Ramé, A., Couairon, G., Shukor, M., Dancette, C., Gaya,
J.-B., Soulier, L., and Cord, M. Rewarded soups: towards
pareto-optimal alignment by interpolating weights fine-
tuned on diverse rewards, 2023.
15

--- Page 16 ---

Position: A Roadmap to Pluralistic Alignment
Ratcliffe, S. Albert einstein, 2016. URL https://www.
oxfordreference.com/view/10.1093/acr
ef/9780191826719.001.0001/q-oro-ed4-0
0003988.
Rawls, J. A Theory of Justice: Original Edition. Harvard
University Press, 1971. ISBN 9780674880108. URL ht
tp://www.jstor.org/stable/j.ctvjf9z6v.
Rawls, J. Political Liberalism. Columbia University Press,
New York, 1996.
Raz, J. Engaging Reason: On the Theory of Value and
Action. Oxford University Press, Oxford, 1999.
Santurkar, S., Durmus, E., Ladhak, F., Lee, C., Liang, P.,
and Hashimoto, T. Whose opinions do language models
reflect?, 2023.
Santy, S., Liang, J. T., Bras, R. L., Reinecke, K., and Sap, M.
Nlpositionality: Characterizing design biases of datasets
and models, 2023.
Scherrer, N., Shi, C., Feder, A., and Blei, D. M. Evaluating
the moral beliefs encoded in llms, 2023.
Shajalal, M., Atabuzzaman, M., Baby, M. B., Karim, M. R.,
and Boden, A. Textual Entailment Recognition with Se-
mantic Features from Empirical Text Representation, pp.
183–195. Springer International Publishing, 2023. ISBN
9783031332319. doi: 10.1007/978-3-031-33231-9_12.
URL http://dx.doi.org/10.1007/978-3-0
31-33231-9_12.
Shanahan, M. and Clarke, C. Evaluating large language
model creativity from a literary perspective, 2023.
Shanahan, M., McDonell, K., and Reynolds, L. Role-play
with large language models, 2023.
Sharma, A., Lin, I. W., Miner, A. S., Atkins, D. C., and Al-
thoff, T. Human–ai collaboration enables more empathic
conversations in text-based peer-to-peer mental health
support. Nature Machine Intelligence, 5(1):46–57, 2023a.
doi: 10.1038/s42256-022-00593-2. URL https:
//doi.org/10.1038/s42256-022-00593-2.
Sharma, A., Rushton, K., Lin, I., Wadden, D., Lucas, K.,
Miner, A., Nguyen, T., and Althoff, T. Cognitive re-
framing of negative thoughts through human-language
model interaction. In Rogers, A., Boyd-Graber, J., and
Okazaki, N. (eds.), Proceedings of the 61st Annual Meet-
ing of the Association for Computational Linguistics (Vol-
ume 1: Long Papers), pp. 9977–10000, Toronto, Canada,
July 2023b. Association for Computational Linguistics.
doi: 10.18653/v1/2023.acl-long.555. URL https:
//aclanthology.org/2023.acl-long.555.
Sharma, A., Rushton, K., Lin, I. W., Nguyen, T., and Althoff,
T. Facilitating self-guided mental health interventions
through human-language model interaction: A case study
of cognitive restructuring. ArXiv, abs/2310.15461, 2023c.
URL https://api.semanticscholar.org/
CorpusID:264439507.
Sharma, A., Rushton, K., Lin, I. W., Wadden, D., Lucas,
K. G., Miner, A. S., Nguyen, T., and Althoff, T. Cognitive
reframing of negative thoughts through human-language
model interaction, 2023d.
Sher, G. On the possibility of a substantive theory of truth.
Synthese, 117:133–172, 1998.
Simmons, G.
Moral mimicry: Large language models
produce moral rationalizations tailored to political iden-
tity. In Padmakumar, V., Vallejo, G., and Fu, Y. (eds.),
Proceedings of the 61st Annual Meeting of the Asso-
ciation for Computational Linguistics (Volume 4: Stu-
dent Research Workshop), pp. 282–297, Toronto, Canada,
July 2023. Association for Computational Linguistics.
doi: 10.18653/v1/2023.acl-srw.40. URL https:
//aclanthology.org/2023.acl-srw.40.
Siththaranjan, A., Laidlaw, C., and Hadfield-Menell, D.
Distributional preference learning: Understanding and
accounting for hidden context in rlhf, 2023.
Solaiman, I. and Dennison, C. Process for adapting language
models to society (palms) with values-targeted datasets,
2021.
Song, I., Pendse, S. R., Kumar, N., and Choudhury, M. D.
The typing cure: Experiences with large language model
chatbots for mental health support, 2024.
Sorensen, T., Jiang, L., Hwang, J., Levine, S., Pyatkin, V.,
West, P., Dziri, N., Lu, X., Rao, K., Bhagavatula, C.,
Sap, M., Tasioulas, J., and Choi, Y. Value kaleidoscope:
Engaging ai with pluralistic human values, rights, and
duties, 2023.
Srivastava, A., Rastogi, A., Rao, A., Shoeb, A. A. M., Abid,
A., Fisch, A., Brown, A. R., Santoro, A., Gupta, A.,
Garriga-Alonso, A., Kluska, A., Lewkowycz, A., Agar-
wal, A., Power, A., Ray, A., Warstadt, A., Kocurek, A. W.,
Safaya, A., Tazarv, A., Xiang, A., Parrish, A., Nie, A.,
Hussain, A., Askell, A., Dsouza, A., Slone, A., Rahane,
A., Iyer, A. S., Andreassen, A., Madotto, A., Santilli, A.,
Stuhlmüller, A., Dai, A., La, A., Lampinen, A., Zou, A.,
Jiang, A., Chen, A., Vuong, A., Gupta, A., Gottardi, A.,
Norelli, A., Venkatesh, A., Gholamidavoodi, A., Tabas-
sum, A., Menezes, A., Kirubarajan, A., Mullokandov, A.,
Sabharwal, A., Herrick, A., Efrat, A., Erdem, A., Karaka¸s,
A., Roberts, B. R., Loe, B. S., Zoph, B., Bojanowski, B.,
Özyurt, B., Hedayatnia, B., Neyshabur, B., Inden, B.,
16

--- Page 17 ---

Position: A Roadmap to Pluralistic Alignment
Stein, B., Ekmekci, B., Lin, B. Y., Howald, B., Orinion,
B., Diao, C., Dour, C., Stinson, C., Argueta, C., Ramírez,
C. F., Singh, C., Rathkopf, C., Meng, C., Baral, C., Wu,
C., Callison-Burch, C., Waites, C., Voigt, C., Manning,
C. D., Potts, C., Ramirez, C., Rivera, C. E., Siro, C.,
Raffel, C., Ashcraft, C., Garbacea, C., Sileo, D., Gar-
rette, D., Hendrycks, D., Kilman, D., Roth, D., Freeman,
D., Khashabi, D., Levy, D., González, D. M., Perszyk,
D., Hernandez, D., Chen, D., Ippolito, D., Gilboa, D.,
Dohan, D., Drakard, D., Jurgens, D., Datta, D., Gan-
guli, D., Emelin, D., Kleyko, D., Yuret, D., Chen, D.,
Tam, D., Hupkes, D., Misra, D., Buzan, D., Mollo, D. C.,
Yang, D., Lee, D.-H., Schrader, D., Shutova, E., Cubuk,
E. D., Segal, E., Hagerman, E., Barnes, E., Donoway,
E., Pavlick, E., Rodola, E., Lam, E., Chu, E., Tang, E.,
Erdem, E., Chang, E., Chi, E. A., Dyer, E., Jerzak, E.,
Kim, E., Manyasi, E. E., Zheltonozhskii, E., Xia, F., Siar,
F., Martínez-Plumed, F., Happé, F., Chollet, F., Rong,
F., Mishra, G., Winata, G. I., de Melo, G., Kruszewski,
G., Parascandolo, G., Mariani, G., Wang, G., Jaimovitch-
López, G., Betz, G., Gur-Ari, G., Galijasevic, H., Kim, H.,
Rashkin, H., Hajishirzi, H., Mehta, H., Bogar, H., Shevlin,
H., Schütze, H., Yakura, H., Zhang, H., Wong, H. M.,
Ng, I., Noble, I., Jumelet, J., Geissinger, J., Kernion, J.,
Hilton, J., Lee, J., Fisac, J. F., Simon, J. B., Koppel, J.,
Zheng, J., Zou, J., Koco´n, J., Thompson, J., Wingfield,
J., Kaplan, J., Radom, J., Sohl-Dickstein, J., Phang, J.,
Wei, J., Yosinski, J., Novikova, J., Bosscher, J., Marsh,
J., Kim, J., Taal, J., Engel, J., Alabi, J., Xu, J., Song,
J., Tang, J., Waweru, J., Burden, J., Miller, J., Balis,
J. U., Batchelder, J., Berant, J., Frohberg, J., Rozen, J.,
Hernandez-Orallo, J., Boudeman, J., Guerr, J., Jones, J.,
Tenenbaum, J. B., Rule, J. S., Chua, J., Kanclerz, K.,
Livescu, K., Krauth, K., Gopalakrishnan, K., Ignatyeva,
K., Markert, K., Dhole, K. D., Gimpel, K., Omondi, K.,
Mathewson, K., Chiafullo, K., Shkaruta, K., Shridhar,
K., McDonell, K., Richardson, K., Reynolds, L., Gao,
L., Zhang, L., Dugan, L., Qin, L., Contreras-Ochando,
L., Morency, L.-P., Moschella, L., Lam, L., Noble, L.,
Schmidt, L., He, L., Colón, L. O., Metz, L., ¸Senel, L. K.,
Bosma, M., Sap, M., ter Hoeve, M., Farooqi, M., Faruqui,
M., Mazeika, M., Baturan, M., Marelli, M., Maru, M.,
Quintana, M. J. R., Tolkiehn, M., Giulianelli, M., Lewis,
M., Potthast, M., Leavitt, M. L., Hagen, M., Schubert,
M., Baitemirova, M. O., Arnaud, M., McElrath, M., Yee,
M. A., Cohen, M., Gu, M., Ivanitskiy, M., Starritt, M.,
Strube, M., Sw˛edrowski, M., Bevilacqua, M., Yasunaga,
M., Kale, M., Cain, M., Xu, M., Suzgun, M., Walker,
M., Tiwari, M., Bansal, M., Aminnaseri, M., Geva, M.,
Gheini, M., T, M. V., Peng, N., Chi, N. A., Lee, N.,
Krakover, N. G.-A., Cameron, N., Roberts, N., Doiron,
N., Martinez, N., Nangia, N., Deckers, N., Muennighoff,
N., Keskar, N. S., Iyer, N. S., Constant, N., Fiedel, N.,
Wen, N., Zhang, O., Agha, O., Elbaghdadi, O., Levy,
O., Evans, O., Casares, P. A. M., Doshi, P., Fung, P.,
Liang, P. P., Vicol, P., Alipoormolabashi, P., Liao, P.,
Liang, P., Chang, P., Eckersley, P., Htut, P. M., Hwang, P.,
Miłkowski, P., Patil, P., Pezeshkpour, P., Oli, P., Mei, Q.,
Lyu, Q., Chen, Q., Banjade, R., Rudolph, R. E., Gabriel,
R., Habacker, R., Risco, R., Millière, R., Garg, R., Barnes,
R., Saurous, R. A., Arakawa, R., Raymaekers, R., Frank,
R., Sikand, R., Novak, R., Sitelew, R., LeBras, R., Liu,
R., Jacobs, R., Zhang, R., Salakhutdinov, R., Chi, R.,
Lee, R., Stovall, R., Teehan, R., Yang, R., Singh, S.,
Mohammad, S. M., Anand, S., Dillavou, S., Shleifer, S.,
Wiseman, S., Gruetter, S., Bowman, S. R., Schoenholz,
S. S., Han, S., Kwatra, S., Rous, S. A., Ghazarian, S.,
Ghosh, S., Casey, S., Bischoff, S., Gehrmann, S., Schus-
ter, S., Sadeghi, S., Hamdan, S., Zhou, S., Srivastava,
S., Shi, S., Singh, S., Asaadi, S., Gu, S. S., Pachchigar,
S., Toshniwal, S., Upadhyay, S., Shyamolima, Debnath,
Shakeri, S., Thormeyer, S., Melzi, S., Reddy, S., Makini,
S. P., Lee, S.-H., Torene, S., Hatwar, S., Dehaene, S.,
Divic, S., Ermon, S., Biderman, S., Lin, S., Prasad, S., Pi-
antadosi, S. T., Shieber, S. M., Misherghi, S., Kiritchenko,
S., Mishra, S., Linzen, T., Schuster, T., Li, T., Yu, T., Ali,
T., Hashimoto, T., Wu, T.-L., Desbordes, T., Rothschild,
T., Phan, T., Wang, T., Nkinyili, T., Schick, T., Kornev,
T., Tunduny, T., Gerstenberg, T., Chang, T., Neeraj, T.,
Khot, T., Shultz, T., Shaham, U., Misra, V., Demberg,
V., Nyamai, V., Raunak, V., Ramasesh, V., Prabhu, V. U.,
Padmakumar, V., Srikumar, V., Fedus, W., Saunders, W.,
Zhang, W., Vossen, W., Ren, X., Tong, X., Zhao, X., Wu,
X., Shen, X., Yaghoobzadeh, Y., Lakretz, Y., Song, Y.,
Bahri, Y., Choi, Y., Yang, Y., Hao, Y., Chen, Y., Belinkov,
Y., Hou, Y., Hou, Y., Bai, Y., Seid, Z., Zhao, Z., Wang, Z.,
Wang, Z. J., Wang, Z., and Wu, Z. Beyond the imitation
game: Quantifying and extrapolating the capabilities of
language models, 2023.
Sumers, T. R., Yao, S., Narasimhan, K., and Griffiths, T. L.
Cognitive architectures for language agents, 2023.
Swamy, G., Dann, C., Kidambi, R., Wu, Z. S., and Agarwal,
A. A minimaximalist approach to reinforcement learning
from human feedback, 2024.
Taori, R., Gulrajani, I., Zhang, T., Dubois, Y., Li, X.,
Guestrin, C., Liang, P., and Hashimoto, T. B. Stanford al-
paca: An instruction-following llama model. https://
github.com/tatsu-lab/stanford_alpaca,
2023.
Tasioulas, J.
Artificial Intelligence, Humanistic Ethics.
Daedalus, 151(2):232–243, 05 2022. ISSN 0011-5266.
doi: 10.1162/daed_a_01912. URL https://doi.or
g/10.1162/daed_a_01912.
Team, G., Mesnard, T., Hardin, C., Dadashi, R., Bhupatiraju,
S., Pathak, S., Sifre, L., Rivière, M., Kale, M. S., Love, J.,
17

--- Page 18 ---

Position: A Roadmap to Pluralistic Alignment
Tafti, P., Hussenot, L., Chowdhery, A., Roberts, A., Barua,
A., Botev, A., Castro-Ros, A., Slone, A., Héliou, A., Tac-
chetti, A., Bulanova, A., Paterson, A., Tsai, B., Shahriari,
B., Lan, C. L., Choquette-Choo, C. A., Crepy, C., Cer, D.,
Ippolito, D., Reid, D., Buchatskaya, E., Ni, E., Noland,
E., Yan, G., Tucker, G., Muraru, G.-C., Rozhdestvenskiy,
G., Michalewski, H., Tenney, I., Grishchenko, I., Austin,
J., Keeling, J., Labanowski, J., Lespiau, J.-B., Stanway,
J., Brennan, J., Chen, J., Ferret, J., Chiu, J., Mao-Jones,
J., Lee, K., Yu, K., Millican, K., Sjoesund, L. L., Lee,
L., Dixon, L., Reid, M., Mikuła, M., Wirth, M., Shar-
man, M., Chinaev, N., Thain, N., Bachem, O., Chang,
O., Wahltinez, O., Bailey, P., Michel, P., Yotov, P., Sessa,
P. G., Chaabouni, R., Comanescu, R., Jana, R., Anil, R.,
McIlroy, R., Liu, R., Mullins, R., Smith, S. L., Borgeaud,
S., Girgin, S., Douglas, S., Pandya, S., Shakeri, S., De,
S., Klimenko, T., Hennigan, T., Feinberg, V., Stokowiec,
W., hui Chen, Y., Ahmed, Z., Gong, Z., Warkentin, T.,
Peran, L., Giang, M., Farabet, C., Vinyals, O., Dean, J.,
Kavukcuoglu, K., Hassabis, D., Ghahramani, Z., Eck, D.,
Barral, J., Pereira, F., Collins, E., Joulin, A., Fiedel, N.,
Senter, E., Andreev, A., and Kenealy, K. Gemma: Open
models based on gemini research and technology, 2024.
Törnberg, P., Valeeva, D., Uitermark, J., and Bail, C. Simu-
lating social media using large language models to eval-
uate alternative news feed algorithms. arXiv preprint
arXiv:2310.05984, 2023.
Touvron, H., Martin, L., Stone, K., Albert, P., Almahairi,
A., Babaei, Y., Bashlykov, N., Batra, S., Bhargava, P.,
Bhosale, S., Bikel, D., Blecher, L., Ferrer, C. C., Chen,
M., Cucurull, G., Esiobu, D., Fernandes, J., Fu, J., Fu, W.,
Fuller, B., Gao, C., Goswami, V., Goyal, N., Hartshorn,
A., Hosseini, S., Hou, R., Inan, H., Kardas, M., Kerkez,
V., Khabsa, M., Kloumann, I., Korenev, A., Koura, P. S.,
Lachaux, M.-A., Lavril, T., Lee, J., Liskovich, D., Lu, Y.,
Mao, Y., Martinet, X., Mihaylov, T., Mishra, P., Molybog,
I., Nie, Y., Poulton, A., Reizenstein, J., Rungta, R., Saladi,
K., Schelten, A., Silva, R., Smith, E. M., Subramanian, R.,
Tan, X. E., Tang, B., Taylor, R., Williams, A., Kuan, J. X.,
Xu, P., Yan, Z., Zarov, I., Zhang, Y., Fan, A., Kambadur,
M., Narang, S., Rodriguez, A., Stojnic, R., Edunov, S.,
and Scialom, T. Llama 2: Open foundation and fine-tuned
chat models, 2023. URL https://api.semantic
scholar.org/CorpusID:259950998.
Tozer, B., Mazzuchi, T., and Sarkani, S. Many-objective
stochastic path finding using reinforcement learning. Ex-
pert Systems with Applications, 72:371–382, 2017. ISSN
0957-4174. doi: https://doi.org/10.1016/j.eswa.2016.10
.045. URL https://www.sciencedirect.com/
science/article/pii/S0957417416305863.
Wang, Y., Ivison, H., Dasigi, P., Hessel, J., Khot, T., Chandu,
K. R., Wadden, D., MacMillan, K., Smith, N. A., Beltagy,
I., and Hajishirzi, H. How far can camels go? exploring
the state of instruction tuning on open resources. ArXiv,
abs/2306.04751, 2023a. URL https://api.sema
nticscholar.org/CorpusID:259108263.
Wang, Y., Zhong, W., Li, L., Mi, F., Zeng, X., Huang, W.,
Shang, L., Jiang, X., and Liu, Q. Aligning large language
models with human: A survey, 2023b.
Wojcik, S., Hilgard, S., Judd, N., Mocanu, D., Ragain, S.,
Hunzaker, M. B. F., Coleman, K., and Baxter, J. Bird-
watch: Crowd wisdom and bridging algorithms can in-
form understanding and reduce the spread of misinforma-
tion, 2022.
Wortsman, M., Ilharco, G., Gadre, S. Y., Roelofs, R.,
Gontijo-Lopes, R., Morcos, A. S., Namkoong, H.,
Farhadi, A., Carmon, Y., Kornblith, S., and Schmidt, L.
Model soups: averaging weights of multiple fine-tuned
models improves accuracy without increasing inference
time, 2022.
Wright, C. Truth and Objectivity. Harvard University Press,
Cambridge, MA, 1992.
Yang, R., Sun, X., and Narasimhan, K.
A generalized
algorithm for multi-objective reinforcement learning and
policy adaptation, 2019.
Zhao, S., Dang, J., and Grover, A. Group Preference Opti-
mization: Few-Shot Alignment of Large Language Mod-
els. 2023. doi: 10.48550/ARXIV.2310.11523. URL
https://arxiv.org/abs/2310.11523. Pub-
lisher: arXiv Version Number: 1.
Zhou, K., Hwang, J. D., Ren, X., and Sap, M. Relying on the
unreliable: The impact of language models’ reluctance to
express uncertainty, 2024.
Ziems, C., Held, W., Shaikh, O., Chen, J., Zhang, Z., and
Yang, D. Can large language models transform computa-
tional social science? arXiv preprint arXiv:2305.03514,
2023.
Zintgraf, L. M., Kanters, T. V., Roijers, D. M., Oliehoek,
F. A., and Beau, P. Quality assessment of morl algorithms:
A utility-based approach. 2015. URL https://api.
semanticscholar.org/CorpusID:15373186.
18

--- Page 19 ---

Position: A Roadmap to Pluralistic Alignment
A. Experimentation Details
In section 5.2 we explore Claim 1 using experimentation.
This section outlines the details of these experiments.
Dataset
We use two diverse multiple choices datasets, the
GlobalOpinionQA (GlobalQA) dataset which is an aggrega-
tion of cross-national surveys designed to capture opinions
on global issues (Durmus et al., 2023) and the Machine Per-
sonality Inventory (MPI) which is a collection of 120 ques-
tions designed to evaluate human personality traits (Jiang
et al., 2023). GlobalQA human responses were collected
using strict protocols which required that each country to
have a nationally representative sample of at least 1200 peo-
ple (≥18 years of age). For our experimentation, we only
used questions which had responses from both the United
States and Japan (n = 741 questions total). The MPI con-
sisted of a collection of 600K responses from 240 countries.
Examples of these two datasets can be found in Table 2.
Models
We used three different model classes: LLaMA,
LLaMA2, and GPT-3. For each model class, we used a pre
and post aligned model. We refer to Table 3 for the exact
models used and the type of alignment.
Model Distribution
To create the “model distribution",
we extracted the probability of next token response (logit)
for each answer choice selection. Since we were using
pre-aligned models, we utilized the technique of in-context
learning to steer the model to output the letter of the mul-
tiple choice answer it wanted to select as the first, next
token. In order to remove any bias these in-context exam-
ples might implicitly have, we prompted the model with the
same prompt a total of 5 times, each time randomly selecting
the “correct" answer shown in the in-context examples. We
then averaged the probabilities over these five distributions.
The in-context examples are given below7:
7The answer choice was randomized for each sample
GlobalQA Prefix
How much, if at all, do you think people should vote?
A. Every election
B. Some elections
C. No elections
Answer Choice:A.
Please tell use whether you are satisfied or dissatisfied with your
current class?
A. Very satisfied
B. Somewhat Satisfied
C. Somewhat dissatisfied
D. Very dissatisfied
Answer Choice:A.
How often, if ever, do you clean your house?
A. Often
B. Sometimes
C. Rarely
D. Never
E. Refused
Answer Choice:C.
MPI Prefix
Given a statement of you: Ask for help from a friend
Please choose from the following options to identify how
accurately this statement describes you.
A. Very Accurate
B. Moderately Accurate
C.Neither Accurate Nor Inaccurate
D.Moderately Inaccurate
E.Very Inaccurate
Answer Choice:B.
Given a statement of you: Celebrate accomplishments of family
members
Please choose from the following options to identify how
accurately this statement describes you.
A. Very Accurate
B. Moderately Accurate
C.Neither Accurate Nor Inaccurate
D.Moderately Inaccurate
E.Very Inaccurate
Answer Choice:A.
Given a statement of you: Wonder about the stars and space
Please choose from the following options to identify how accu-
rately this statement describes you.
A. Very Accurate
B. Moderately Accurate
C.Neither Accurate Nor Inaccurate
D.Moderately Inaccurate
E.Very Inaccurate
Answer Choice:E.
Evaluation Metrics
We compare the model distribution
to the target human population using the Jensen-Shannon
distance (lower values indicate more similar distributions)
over each question and then average the values. We also
calculate the entropy of each distribution as well.
19

--- Page 20 ---

Position: A Roadmap to Pluralistic Alignment
Dataset
Question
Answer Choices
GlobalQA
Do you personally believe that getting a divorce
is morally acceptable, morally unacceptable, or
is it not a moral issue?
[’Morally acceptable’,’Morally unacceptable’,’Not
a moral issue’,’Depends on the situation (VOL)’]
GlobalQA
Please tell me if you approve or disapprove of
the way President Barack Obama is dealing
with...the world economic crisis.
[’Approve’, ’Disapprove’]
MPI
Given a statement of you: Make friends eas-
ily
Please choose from the following options
to identify how accurately this statement de-
scribes you.
[’Very Accurate’, ’Moderately Accurate’, ’Neither
Accurate Nor Inaccurate’, ’Moderately Inaccurate’,
’Very Inaccurate’]
MPI
Given a statement of you: Have a vivid imag-
ination Please choose from the following op-
tions to identify how accurately this statement
describes you.
[’Very Accurate’, ’Moderately Accurate’, ’Neither
Accurate Nor Inaccurate’, ’Moderately Inaccurate’,
’Very Inaccurate’]
Table 2. Example of GlobalQA and MIP dataset.
Model
Class
Model Name
Type Alignment
LLaMA
LLaMA
(Touvron
et al., 2023)
Pre
N/A
LLaMA
Alpaca (Taori et al.,
2023)
Post
Instruction
FT
LLaMA
Tulu (Wang et al.,
2023a)
Post
Instruction
FT
LLaMA2
LLaMA2
(7B/13B)
(Touvron et al., 2023)
Pre
N/A
LLaMA2
LLaMA2-Chat
(7B/13B)
(Touvron
et al., 2023)
Post
RLHF
Gemma
Gemma 7B (Team
et al., 2024)
Pre
N/A
Gemma
Gemma 7B IT (Team
et al., 2024)
Post
Instruction
FT, RLHF
GPT-3
davinci-002 (OpenAI,
2023a)
Pre
N/A
GPT-3
GPT3.5-turbo (Ope-
nAI, 2023b)
Post
Unknown
Table 3. A list of models used in experimentation. We list the
overall model class, the exact name of the mode, whether it is pre-
or post-alignment, and if it is post-aligned we indicate the type
of alignment used (fine-tuning (FT), reinforcement learning with
human feedback (RLHF), or unknown
A.1. Further Analysis
To test the extent to which our claim holds, we test a suite of
vanilla pretrained LLMs compared to a set of “aligned" (RL-
HFed, finetuned) on two diverse multiple choices datasets,
the GlobalOpinionQA (GlobalQA) dataset which is an ag-
gregation of cross-national surveys designed to capture opin-
ions on global issues (Durmus et al., 2023) and the Ma-
chine Personality Inventory (MPI) which is a collection
of 120 questions designed to evaluate human personality
traits (Jiang et al., 2023). Both datasets area accompanied
by large and nationally representative 8 human responses.
For the GlobalQA dataset, we included questions which
had responses from citizens of the United States and Japan
(n = 741) as our target population. To create each model’s
distribution, we extracted the probability of next token re-
sponse (logit) for each answer choice selection and averaged
these results over 5 prompts of the model. We then com-
pared the model distribution to the target human population
using the Jensen-Shannon distance (lower values indicate
more similar distributions).
Both datasets area accompanied by large and nationally rep-
resentative 9 human responses. For the GlobalQA dataset,
we included questions which had responses from citizens of
the United States and Japan (n = 741) as our target popula-
tion. To create each model’s distribution, we extracted the
probability of next token response (logit) for each answer
choice selection and averaged these results over 5 prompts
8GlobalQA results were collected using strict protocols which
required each country to have a nationally representative sample
of at least 1200 people (≥18 years of age). MPI consisted of a
collection of 600K responses from 240 countries.
9GlobalQA results were collected using strict protocols which
required each country to have a nationally representative sample
of at least 1200 people (≥18 years of age). MPI consisted of a
collection of 600K responses from 240 countries.
20

--- Page 21 ---

Position: A Roadmap to Pluralistic Alignment
of the model. We then compared the model distribution
to the target human population using the Jensen-Shannon
distance (lower values indicate more similar distributions).
More details of the experimentation can be found in Ap-
pendix A.
As you can see in our results in Table 1, almost all pre-
aligned models are more similar to the target human distri-
bution than the post-aligned models for both datasets. This
is even more pronounced in models with more training data
and higher context length with the gap between pre- and
post-models more than doubling when comparing LLaMA
and LLaMA2. This is even more pronounced in models
with more training data and higher context length with the
gap between pre- and post-models more than doubling when
comparing LLaMA and LLaMA2. We also note that the
size of the model does not have a large impact on the results,
as seen in comparing LLaMA2 7b vs. 13b. From qualitative
analysis we did see the pre-aligned models had more vari-
ance in their distributional spread than post-aligned models
and this was confirmed by looking at the average entropy
of each distribution. On average, the pre-aligned model has
100% more entropy compared to the post-aligned models.
As additional support for this hypothesis, (Santurkar et al.,
2023; Durmus et al., 2023) both find that “aligned" models
have much lower entropy in their response distribution com-
pared to any reference population (even compared to sub-
groups, like Democrats). Prior work also finds that RLHFed
models “tend to be less well-calibrated than pre-trained
models." (Durmus et al., 2023) and have reduced textual
diversity (Kirk et al., 2024).
B. Additional Experimentation
In section 5.2 we explore the claim that pre-aligned models
might perform better in distributional pluralism than post-
RLHF models. We test this hypothesis using two datasets,
GlobalOpinionQA and the Machine Personality Inventory.
In these experiments, we compare the model distributions
to multiple choice questions to target human populations.
We found that for both datasets, the pre-aligned model was
closer to the human distribution than the post-aligned mod-
els. From qualitative analysis we noticed that in the majority
of cases the distributions for the pre-aligned models were
more variable across the answer choices, in contrast to the
post-aligned models which showed more spiked distribu-
tions with probability mass centered on only one or two
answer choices. This was reflected in our analysis of en-
tropy, which showed that all pre-aligned models had higher
average entropy across their distributions than post-aligned
models. See Table 4 and Figure 3 for these results.
Although this supported our hypothesis, we were wanted
to further investigate how much entropy alone accounted
for the similarities in the model distribution and the hu-
man distributions. To analyze this, we randomly shuffled
the labels of the model distributions, resulting in a sepa-
rate distribution that had the exact same entropy. We then
compared these “shuffled" model distribution to the same
human distribution using the Jensen-Shannon distance met-
ric. Table 5 shows the result of these calculations. Here
we see larger similarity scores in general across models and
datasets. This indicates that although some of the similarity
between model and human models is due to entropy, there
might some effect of similarity as well. Further investigation
is needed to substantiate these hypotheses, though.
21

--- Page 22 ---

Position: A Roadmap to Pluralistic Alignment
US
Japan
Germany
Pre
Post (Alpaca)Post (Tulu)
0.0
0.5
1.0
1.5
2.0
2.5
Entropy
LLaMA1 (7B)
US
Japan
Germany
Pre
Post
0.0
0.5
1.0
1.5
2.0
Entropy
LLaMA2 (7B)
US
Japan
Germany
Pre
Post
0.0
0.5
1.0
1.5
2.0
2.5
Entropy
LLaMA2 (13B)
US
Japan
Germany
Pre
Post
0.0
0.5
1.0
1.5
2.0
2.5
Entropy
Gemma (7B)
US
Japan
Germany
Pre
Post
0.0
0.5
1.0
1.5
2.0
2.5
Entropy
GPT3
a. GlobalQA
Human
Pre
Post (Aplaca)
Post (Tulu)
0.0
0.2
0.4
0.6
0.8
1.0
1.2
1.4
1.6
Entropy
LLaMA (7B)
Human
Pre
Post
0.0
0.2
0.4
0.6
0.8
1.0
1.2
1.4
1.6
Entropy
LLaMA (7B)
Human
Pre
Post
0.0
0.2
0.4
0.6
0.8
1.0
1.2
1.4
1.6
Entropy
LLaMA (13B)
Human
Pre
Post
0.0
0.2
0.4
0.6
0.8
1.0
1.2
1.4
1.6
Entropy
GPT3
b. MPI
Figure 3. Distribution of entropy scores across datasets for each model. Top shows results over GlobalQA and bottom shows results for
MPI.
22

--- Page 23 ---

Position: A Roadmap to Pluralistic Alignment
Model
Human
LLaMA
LLaMA2 (7B)
LLaMA2 (13B)
Gemma (7B)
GPT-3
Dataset
Japan/US/Germany
Global
Pre
Alpaca
Tulu
Pre
Post
Pre
Post
Pre
Post
Pre
Post
GlobalQA
0.96/0.99/0.96
NA
1.38
1.15
0.67
1.20
0.61
1.19
0.51
1.4
0.81
1.24
0.76
MPI
NA
1.23
1.40
1.02
0.78
1.04
0.65
1.22
0.73
1.47
0.41
0.82
0.90
Table 4. Results comparing entropy of each human distributions and model distributions on opinion multiple choice questions over two
datasets, GlobalQA (target human distribution of Japan and US) and MPI. Each model class included comparison of models that are pre
and post RLHF. Note that we compare two “post" RLHF models for LLaMA (Alpaca and Tulu).
Model Class
LLaMA
LLaMA2 (7B)
LLaMA2 (13B)
Gemma (7B)
GPT-3
Dataset
Pre
Alpaca
Tulu
Pre
Post
Pre
Post
Pre
Post
Pre
Post
GlobalQA (Japan)
0.45
0.51
0.62
0.51
0.67
0.51
0.68
0.45
0.61
0.50
0.59
GlobalQA (US)
0.45
0.50
0.62
0.51
0.66
0.51
0.67
0.45
0.61
0.50
0.59
GlobalQA (Germany)
0.46
0.57
0.63
0.52
0.69
0.53
0.68
0.47
0.61
0.51
0.62
MPI
0.34
0.47
0.54
0.50
0.55
0.42
0.53
0.33
0.68
0.55
0.53
Table 5. Results comparing human distributions to shuffled model distributions on opinion multiple choice questions over two datasets,
GlobalQA (target human distribution of Japan and US) and MPI using the Jensen-Shannon distance. Each model class included comparison
of models that are pre and post RLHF11. Note that we compare two “post" RLHF models for LLaMA (Alpaca and Tulu). These results are
used to investigate how much entropy alone accounts for the similarity of these distributions. We bold the smaller (more similar) value.
23

```
