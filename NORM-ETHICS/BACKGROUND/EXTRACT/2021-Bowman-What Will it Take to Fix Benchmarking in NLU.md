---
title: "2021-Bowman-What Will it Take to Fix Benchmarking in NLU - Background Extract"
source_pdf: "2021-Bowman-What Will it Take to Fix Benchmarking in NLU.pdf"
source_folder: "02-external-papers"
pages: 13
extracted_at: "2026-04-03T10:25:00"
---

# Background Extract: 2021-Bowman-What Will it Take to Fix Benchmarking in NLU

**Source PDF:** 2021-Bowman-What Will it Take to Fix Benchmarking in NLU.pdf
**Source:** 02-external-papers
**Total Pages:** 13

---

## Content

```
--- Page 1 ---

Proceedings of the 2021 Conference of the North American Chapter of the
Association for Computational Linguistics: Human Language Technologies, pages 4843–4855
June 6–11, 2021. ©2021 Association for Computational Linguistics
4843
What Will it Take to Fix Benchmarking
in Natural Language Understanding?
Samuel R. Bowman
New York University
bowman@nyu.edu
George E. Dahl
Google Research, Brain Team
gdahl@google.com
Abstract
Evaluation for many natural language under-
standing (NLU) tasks is broken: Unreliable
and biased systems score so highly on stan-
dard benchmarks that there is little room for
researchers who develop better systems to
demonstrate their improvements. The recent
trend to abandon IID benchmarks in favor of
adversarially-constructed, out-of-distribution
test sets ensures that current models will per-
form poorly, but ultimately only obscures the
abilities that we want our benchmarks to mea-
sure. In this position paper, we lay out four cri-
teria that we argue NLU benchmarks should
meet.
We argue most current benchmarks
fail at these criteria, and that adversarial data
collection does not meaningfully address the
causes of these failures. Instead, restoring a
healthy evaluation ecosystem will require sig-
niﬁcant progress in the design of benchmark
datasets, the reliability with which they are an-
notated, their size, and the ways they handle
social bias.
1
Introduction
A large and impactful thread of research on nat-
ural language understanding (NLU) has focused
on improving results on benchmark datasets that
feature roughly independent and identically dis-
tributed (IID) training, validation, and testing sec-
tions, drawn from data that were collected or anno-
tated by crowdsourcing (Maas et al., 2011; Bow-
man et al., 2015; Rajpurkar et al., 2016; Wang et al.,
2019b). Recent methodological progress combined
with longstanding issues in crowdsourced data qual-
ity has made it so state-of-the-art systems are near-
ing the maximum achievable values on most of
these benchmarks and thus are unlikely to be able
to measure further improvements (Devlin et al.,
2019; Raffel et al., 2020). At the same time, these
apparently high-performing systems have serious
known issues and have not achieved human-level
competence at their tasks (Ribeiro et al., 2020).
1. Good performance on the benchmark should imply
robust in-domain performance on the task.
,→We need more work on dataset design and data
collection methods.
2. Benchmark examples should be accurately and unam-
biguously annotated.
,→Test examples should be validated thoroughly
enough to remove erroneous examples and to prop-
erly handle ambiguous ones.
3. Benchmarks should offer adequate statistical power.
,→Benchmark datasets need to be much harder
and/or much larger.
4. Benchmarks should reveal plausibly harmful social
biases in systems, and should not incentivize the cre-
ation of biased systems.
,→We need to better encourage the development and
use auxiliary bias evaluation metrics.
Figure 1: A summary of the criteria we propose.
Progress suffers in the absence of a trustworthy
metric for benchmark-driven work: Newcomers
and non-specialists are discouraged from trying
to contribute, and specialists are given signiﬁcant
freedom to cherry-pick ad-hoc evaluation settings
that mask a lack of progress (Church and Hestness,
2019).
The plight of benchmark-driven NLU research
has prompted widespread concern about the as-
sumptions underlying standard benchmarks and
widespread interest in alternative models of evalua-
tion. As an especially clear example, the documen-
tation for the recent DynaBench benchmark suite
argues that “benchmarks saturate”, “benchmarks
have artifacts”, “researchers overﬁt on bench-
marks”, and “benchmarks can be deceiving” and
use these claims to motivate abandoning the IID
paradigm in favor of benchmark data that is col-
lected adversarially by asking a broad population
of annotators to try to fool some reference neural
network model.1
1https://dynabench.org/about

--- Page 2 ---

4844
The DynaBench approach falls into the broader
category of adversarial ﬁltering (Paperno et al.,
2016; Zellers et al., 2018; Nie et al., 2020; Le Bras
et al., 2020). Adversarial ﬁltering starts with a
pipeline that produces candidate examples for the
task, often through crowdsourcing, and then con-
structs a dataset by selecting those examples from
the pipeline where one or more machine learn-
ing models fails to predict the correct label. This
approach is appealing in that it guarantees that,
at least in the short term, existing approaches to
dataset construction can be patched to keep produc-
ing data that will challenge current systems.
However, collecting examples on which current
models fail is neither necessary nor sufﬁcient to
create a useful benchmark. Among other points of
concern, this approach can create a counterproduc-
tive incentive for researchers to develop models that
are different without being better, since a model
can top the leaderboard either by producing fewer
errors than the adversary or by simply producing
different errors, because the examples on which
these new errors would be tested will not appear
in the evaluation set. One could attempt to do this
by, for example, pretraining new models that de-
liberately avoid any data that was used to pretrain
the original adversary model, in order to minimize
the degree to which the idiosyncratic mistakes of
the new model line up with those of the old one.
This incentive can slow progress and contribute to
spurious claims of discovery.
This position paper argues that concerns about
standard benchmarks that motivate methods like
adversarial ﬁltering are justiﬁed, but that they can
and should be addressed directly, and that it is
possible and reasonable to do so in the context
of static, IID evaluation. We propose four criteria
that adequate benchmarks should satisfy: bench-
marks should offer a valid test of the full set of
relevant language phenomena, they should be built
around consistently-labeled data, they should offer
adequate statistical power, and they should disin-
centivize the use of systems with potentially harm-
ful biases. We then brieﬂy survey some ongoing or
promising research directions that could enable us
to meet these challenges, including hybrid data col-
lection protocols involving both crowdworkers and
domain experts, larger-scale data validation, and
auxiliary bias metric datasets attached to bench-
marks.
2
Background
The Problem
Performance on popular bench-
marks is extremely high, but experts can easily ﬁnd
issues with high-scoring models. The GLUE bench-
mark (Wang et al., 2019b; Nangia and Bowman,
2019), a compilation of NLU evaluation tasks, has
seen performance on its leaderboard approach or
exceed human performance on all nine of its tasks.
The follow-up SuperGLUE benchmark project
(Wang et al., 2019a) solicited dataset submissions
from the NLP research community in 2019, but
wound up needing to exclude the large majority of
the submitted tasks from the leaderboard because
the BERT model (Devlin et al., 2019) was already
showing performance at or above that of a majority
vote of human crowdworkers. Of the eight tasks
for which BERT did poorly enough to leave clear
headroom for further progress, all are now effec-
tively saturated (Raffel et al., 2020; He et al., 2020).
State-of-the-art performance on the highly popular
SQuAD 2 English reading-comprehension leader-
board (Rajpurkar et al., 2018) has long exceeded
that of human annotators.
Ample evidence has emerged that the systems
that have topped these leaderboards can fail dra-
matically on simple test cases that are meant to
test the very skills that the leaderboards focus on
(McCoy et al., 2019; Ribeiro et al., 2020). This re-
sult makes it clear that our systems have signiﬁcant
room to improve. However, we have no guaran-
tee that our benchmarks will detect these needed
improvements when they’re made. Most were col-
lected by crowdsourcing with relatively limited
quality control, such that we have no reason to
expect that perfect performance on their metrics is
achievable or that the benchmark will meaningfully
distinguish between systems with superhuman met-
ric performance. While the true upper bound on
performance for any task (Bayes error) is not mea-
surable, the fact that our systems have exceeded
serious estimates of human performance leaves us
with no reason to expect there to be much more
headroom.
In addition, many of our best models display
socially-relevant biases that render them inappro-
priate for deployment in many applications.2 Our
best current benchmarks do little or nothing to dis-
2The state-of-the-art T5 model, for example, shows far
more sensitivity to irrelevant gender information than humans
do when making coreference judgments, according to results
on the SuperGLUE leaderboard with the DNC Winogender
dataset (Rudinger et al., 2018; Poliak et al., 2018).

--- Page 3 ---

4845
courage harmful biases and, by building largely
on crowdsourced or naturally-occurring text data,
they likely incentivize the development of models
that reproduce problematic biases, at least to some
degree.
The Goal
This paper lays out four criteria that
we would like our benchmarks to satisfy in order
to facilitate further progress toward a primarily sci-
entiﬁc goal: building machines that can demon-
strate a comprehensive and reliable understanding
of everyday natural language text in the context
of some speciﬁc well-posed task, language variety,
and topic domain. Among language understand-
ing tasks, we focus on those that use labeled data
and that are designed to test relatively general lan-
guage understanding skills, for which the design of
benchmarks can be especially difﬁcult.
We distinguish between a task and a benchmark:
A task, in our terms, is a language-related skill or
competency that we want a model to demonstrate
in the context of a speciﬁc input–output format. A
benchmark attempts to evaluate performance on
a task by grounding it to a text domain and in-
stantiating it with a concrete dataset and evalua-
tion metric. As a rough example, multiple-choice
reading-comprehension question answering is a
task, which the Cosmos benchmark (Huang et al.,
2019) attempts to test using an accuracy metric over
a speciﬁc sample of passages and questions from
the English personal narrative domain. There is
no general way to prove that a concrete benchmark
faithfully measures performance on an abstract task.
Nevertheless, since we can only evaluate models
on concrete benchmarks, we have no choice but to
strengthen the correspondence between the two as
best we can.
We set aside the evaluation of computational ef-
ﬁciency and data efﬁciency, despite its relevance to
many speciﬁc applications of language technology.
We will not fully set aside issues of social bias.
Even though it is possible for the same system to
demonstrate both adept language understanding
and harmful social prejudices,3 ethical concerns
prompt us to argue that community-wide bench-
marks should identify and disincentivize potentially
harmful biases in models. The widespread sharing
of trained models among NLU researchers and en-
3The performance of models like RoBERTa (Liu et al.,
2019) or T5 (Raffel et al., 2020) on benchmarks like Super-
GLUE that include some coverage of social bias is a good
example of this, and typical human behavior is an even better
example.
gineers and the fast pace of NLP R&D work mean
that it is easy for systems designed with scientiﬁc
goals in mind to be deployed in settings where their
biases can cause real harm. While recent initiatives
around data documentation should reduce the acci-
dental deployment of models built on inappropriate
data (Bender and Friedman, 2018; Gebru et al.,
2018), we see room to do more.
We will also set aside few-shot learning, in
which tasks are made artiﬁcially difﬁcult by train-
ing models only on small subsets of the available
training data (as was prominently used for GPT-3
by Brown et al., 2020). This paper focuses in-
stead on the case where one is interested in reach-
ing excellent performance on some language task
and is willing to collect data or otherwise expend
resources to make that possible. While few-shot
learning represents a potentially impactful direc-
tion for engineering research, and success on some
task in a few-shot setting is clear evidence of suc-
cess more generally, artiﬁcial constraints on the use
of training data do not ﬁt the broad goals laid out
above and do not ﬁt many applied settings.
3
Four Challenges
This paper focuses on four criteria, outlined in Fig-
ure 1, that we argue effective future benchmarks
for NLU tasks should satisfy. We believe that no
current benchmark for any difﬁcult broad-domain
NLU task satisﬁes all four:
3.1
Validity
If one system signiﬁcantly outperforms another on
some benchmark, then that result should be strong
evidence that the higher-scoring system is actually
better at the task tested by the benchmark. In other
words, benchmarks are only useful for language
understanding research if they evaluate language
understanding. General-purpose benchmarks that
are designed to cover tasks like paragraph reading
comprehension over Wikipedia are only effective
if they test the full range of skills that are required
to understand and reason about paragraphs from
Wikipedia.
This criterion is difﬁcult to fully formalize, and
we know of no simple test that would allow one to
determine if a benchmark presents a valid measure
of model ability. Minimally, though, it requires the
following:
• An evaluation dataset should reﬂect the full
range of linguistic variation—including words

--- Page 4 ---

4846
and higher-level constructions—that is used
in the relevant domain, context, and language
variety.
• An evaluation dataset should have a plausible
means by which it tests all of the language-
related behaviors that we expect the model to
show in the context of the task.
• An evaluation dataset should be sufﬁciently
free of annotation artifacts (as in Si et al.,
2019; Sugawara et al., 2020b; Niven and Kao,
2019) that a system cannot reach near-human
levels of performance by any means other than
demonstrating the required language-related
behaviors.
If a benchmark fully meets this challenge, we
should expect any clear improvement on the bench-
mark to translate to similar improvements on any
other valid and reasonable evaluation data for the
same task and language domain.4
The rest of this section surveys common
paradigms for constructing a benchmark dataset,
and points to reasons that none offers a straightfor-
ward way to satisfy this criterion:
Naturally-Occurring Examples
It is intuitively
appealing to, where possible, build benchmark
datasets based on naturally-occurring data distribu-
tions. This minimizes our effort in creating bench-
marks and minimizes the risk that the benchmark
is somehow skewed in a way that omits important
phenomena. However, this is often not viable.
For tasks like reading comprehension or nat-
ural language inference that require multiple re-
lated texts (such as a passage and a question) as
input, there is often no natural distribution that ef-
ﬁciently isolates the relevant task behaviors. One
can ﬁnd naturally-occurring distributions over ques-
tions, like those used to construct Natural Ques-
tions (Kwiatkowski et al., 2019), but these will
generally be tied to the use contexts of a speciﬁc
NLP product and will thus be limited by users’
perceptions of the current abilities of that product.
Even for single-input tasks like coreference res-
olution or Cloze, for which any text corpus can
be the basis for a benchmark, naturalistic distribu-
tions do nothing to separate skills of interest from
factual world knowledge and can be overwhelm-
ingly dominated by the latter, making them poor
4Though, of course, any model with non-zero test error
could be presented with a potentially-unreasonable benchmark
entirely consisting of its own test errors.
metrics for incremental progress on NLU. Credible
existing NLU-oriented benchmarks for such tasks
are generally heavily curated (Paperno et al., 2016;
Levesque et al., 2012; Sakaguchi et al., 2019).
Expert-Authored
Examples
Expert-
constructed datasets for language understanding
like FraCaS (Cooper et al., 1996) and the Winograd
Schema Challenge (Levesque et al., 2012) have
been crucial for deﬁning several new tasks and
introducing them as objects of study. However,
expert example construction isn’t desirable for the
creation of benchmarks for the use cases we focus
on here.
Setting aside the logistical challenges of creat-
ing sufﬁciently large and diverse datasets by expert
labor alone, expert authorship generally gives mem-
bers of the research community direct, ﬁne-grained
control over the data on which their systems will be
evaluated. Intentionally or unintentionally, this can
produce data that is oriented toward linguistic phe-
nomena that are widely studied and widely known
to be important to the task at hand. While this can
be helpful when building diagnostic datasets that
focus on speciﬁc types of model failure (Cooper
et al., 1996; Naik et al., 2018; Wang et al., 2019b),
it is counterproductive when our goal is to build a
broad-coverage benchmark dataset to set priorities
and guide progress toward the solution of some
task.
Dunietz et al. (2020) and Sugawara et al. (2020a)
work around this issue by leaning on taxonomies
of required phenomena from outside NLP. This is
a direction worth pursuing, but it is not clear that
appropriate taxonomies will be available for most
NLU tasks of interest, or that these taxonomies
will be broad and thorough enough to be straight-
forwardly implemented as datasets.
Crowdsourcing
Most recent benchmarks for lan-
guage understanding have been collected, at least
in part, through crowdsourcing example construc-
tion, where non-expert annotators are given some
freedom to construct examples based on a simple
set of guidelines. This has an obvious appeal: Us-
ing non-expert annotators signiﬁcantly lowers costs
and using simple guidelines signiﬁcantly reduces
the risk that the resulting data will be skewed artiﬁ-
cially toward phenomena of interest to experts.
However, straightforward standard practice, as
was used to collect datasets like SNLI (Bowman
et al., 2015) and SQuAD, seem to be relatively poor

--- Page 5 ---

4847
at producing difﬁcult datasets that test the intended
phenomena. Existing datasets focus heavily on
repetitive, easy cases and often fail to isolate key
behaviors (Jia and Liang, 2017; Tsuchiya, 2018;
McCoy et al., 2019).
Adversarial Filtering
Given a source of exam-
ples and a model, adversarial-ﬁltering-style ap-
proaches build a benchmark based on samples from
that source for which the model fails. Adversarial
ﬁltering can remove examples that are easy due to
trivial artifacts, but it does not ensure that the re-
sulting dataset supports a valid test of model ability,
and it can systematically eliminate coverage of lin-
guistic phenomena or skills that are necessary for
the task but already well-solved by the adversary
model. This mode-seeking (as opposed to mass
covering) behavior by adversarial ﬁltering, if left
unchecked, tends to reduce dataset diversity and
thus make validity harder to achieve.
In contrast with this benchmark data collection
setting, adversarial competitions, in which one com-
pares the difﬁculty of collecting valid task exam-
ples that are adversarial to each of several systems,
could be part of a healthy evaluation ecosystem.
Such an ecosystem might involve frequent forma-
tive evaluations on a conventional non-adversarial
benchmark in conjunction with periodic organized
evaluations in an adversarial setting.
3.2
Reliable Annotation
For our benchmarks to incentivize the development
of sound new methods, the labels for their test
examples should be reliably correct. This means
avoiding three failure cases: (i) examples that are
carelessly mislabeled, (ii) examples that have no
clear correct label due to unclear or underspeciﬁed
task guidelines, and (iii) examples that have no
clear correct label under the relevant metric due to
legitimate disagreements in interpretation among
annotators. The ﬁrst two cases straightforwardly
compromise the validity of the benchmark, but the
third is somewhat subtler.
Legitimate disagreement emerges when an ex-
ample can be labeled in multiple ways depending
on an annotator’s choice between reasonable inter-
pretations of the text of an example. Such disagree-
ments might stem from dialectal variants in the
interpretation of words or constructions or differ-
ent reasonable interpretations of the actual state of
the world. As a toy example, consider the question:
Does Ed ate a burrito entail Ed ate a sandwich?
While most US English speakers would likely an-
swer no, many pedants and regulatory ofﬁcials have
argued for yes (Florestall, 2008).
When a benchmark contains many instances of
this kind of legitimate disagreement, a machine
learning model will be able to study a benchmark
dataset’s training set for clues about typical hu-
man behavior that might allow it to perform better
than any single human annotator. This effect could
contribute to misleading reports of super-human
performance on such benchmarks, where human
performance reﬂects the behavior of humans who
are reporting their own judgments, rather than at-
tempting to predict the most frequently assigned
label, as the model does. We observe evidence
of this kind of ambiguity in existing benchmarks:
For example, Pavlick and Kwiatkowski (2019) ﬁnd
that 20% of examples across several textual en-
tailment datasets are signiﬁcantly ambiguous, and
Kwiatkowski et al. (2019) show that 36% of short
answer annotations in Natural Questions differ sig-
niﬁcantly from the majority answer.
3.3
Statistical Power
Benchmark evaluation datasets should be large and
discriminative enough to detect any qualitatively
relevant performance difference between two mod-
els. This criterion introduces a trade-off: If we can
create benchmark datasets that are both reliable
and highly difﬁcult for the systems that we want to
evaluate, then moderate dataset sizes will sufﬁce.
However, if our benchmark datasets contain many
examples that are easy for current or near-future
systems, then we will need dramatically larger eval-
uation sets to reach adequate power.
In the context of a reliable dataset that is difﬁcult
for current systems, a 1% absolute accuracy im-
provement, such as that from 80% to 81%, may be
an acceptable minimum detectable effect. In this
case, an evaluation set of a few thousand examples
would sufﬁce under typical conditions seen in NLU
(Card et al., 2020). Many, though not all, popular
benchmark datasets satisfy this size threshold.
Since our systems continue to improve rapidly,
though, we should expect to be spending more time
in the long tail of our data difﬁculty distributions:
If we build reliable datasets, much of their future
value may lie in their ability to measure improve-
ments in accuracy among highly accurate systems.
For example, an improvement from 98% accuracy
to 98.1% represents the same 5% relative improve-

--- Page 6 ---

4848
ment as we saw from 80% to 81%. To reliably
detect this smaller absolute improvement, though,
requires two orders of magnitude more evaluation
data (Card et al., 2020).
3.4
Disincentives for Biased Models
A benchmark should, in general, favor a model
without socially-relevant biases over an otherwise
equivalent model with such biases. Many current
benchmarks fail this test. Because benchmarks are
often built around naturally-occurring or crowd-
sourced text, it is often the case that a system can
improve its performance by adopting heuristics that
reproduce potentially-harmful biases (Rudinger
et al., 2017). Developing adequate methods to min-
imize this effect will be challenging, both because
of deep issues with both the precise speciﬁcation
of what constitutes harmful bias and because of the
limited set of tools that we have available to us.
There is no precise enumeration of social biases
that will be broadly satisfactory across applications
and cultural contexts. This can be most easily il-
lustrated with the example of biased associations
between word representations for US English (as in
Bolukbasi et al., 2016). Associations between race
or gender and occupation are generally considered
to be undesirable and potentially harmful in most
contexts, and are something that benchmarks for
word representations should discourage, or at least
carefully avoid rewarding. If a set of word repre-
sentations encodes typically Black female names
like Keisha as being less similar to professional oc-
cupation terms like lawyer or doctor than typically
white male names like Scott are, then a model using
those representations is likely to reinforce harmful
race or gender biases in any downstream content
moderation systems or predictive text systems it
gets used in.
Adequately enumerating the social attributes for
which we might want to evaluate bias in some con-
text can be difﬁcult. For example, Indian castes,
like racial categories in the United States, are of-
ten signaled by names and are an axis on which
managers sometimes discriminate in hiring. Caste
is a salient category of social bias in India that is
subject to legal and institutional recognition. How-
ever, this bias also arises in some cases within the
United States, where it has no such recognition
(Tiku, 2020), and where it could be easily over-
looked by non-specialist bias researchers.
Furthermore, building such a list of attributes
is also deeply political. Within living memory,
popular and legal attitudes have changed signif-
icantly in the United States about attributes like
race, gender, gender expression, sexual orientation,
and disability. Attitudes on these issues continue
to change, and new categories can gain recognition
and protection over time. In many cases, this means
that choosing whether to include some attribute in
a computational metric of bias means choosing
which group of people to align oneself with on a
political issue. While there are clear ethical rules
of thumb to follow when doing so,5 making any
particular choice is nonetheless likely to put re-
searchers in conﬂict with established institutions
in ways that can change quickly. Any strategy for
handling bias in the context of NLP benchmarks
will have to grapple with this difﬁcult reality.
4
Sketching a Solution
Building new benchmarks that improve upon our
four axes is likely to be quite difﬁcult. Below we
attempt to sketch out some possible directions for
improvement along each axis.
4.1
Improving Validity
Building valid benchmarks will require signiﬁcant
new research into data collection methods, at least
some of which will be speciﬁc to the task under
study. We suspect that much of this work will in-
volve improvements in crowdsourcing and the use
of non-experts, as most of the annotation behind
the tasks we discuss requires no expertise other
than ﬂuent knowledge of the language variety un-
der study.
One promising direction involves methods that
start from relatively high-quality crowdsourced
datasets, then use expert effort to augment them in
ways that mitigate annotation artifacts. The Build-
it-Break-it challenge (Ettinger et al., 2017), the
Open Reading Benchmark (Dua et al., 2019), and
the Gardner et al. (2020) contrast sets, among their
other features, allow expert annotators to add exam-
ples to a test set to ﬁll perceived gaps in coverage
or correct perceived artifacts in a starting set of
crowdsourced examples. To the extent that crowd-
sourcing with non-experts can produce data that
has broad coverage and high difﬁculty but retains
some measurable artifacts or ﬂaws, this compro-
5The ACM code of ethics states, “when the interests of
multiple groups conﬂict, the needs of those less advantaged
should be given increased attention and priority.”

--- Page 7 ---

4849
mise approach may help to create usable bench-
mark datasets out of the results.
Another approach brings computational linguists
directly into the crowdsourcing process. This was
recently demonstrated at a small scale by Hu et al.
(2020) with OCNLI: They show that it is possi-
ble to signiﬁcantly improve data quality issues by
making small interventions during the crowdsourc-
ing process—like offering additional bonus pay-
ments for examples that avoid overused words and
constructions—without signiﬁcantly limiting anno-
tators’ freedom to independently construct creative
examples.
Of course, implementing interventions like these
in a way that offers convincing evidence of validity
will be difﬁcult.
4.2
Improving Handling of Annotation
Errors and Disagreements
The
use
of
standard
techniques
from
crowdsourcing—generally
involving
multi-
ple redundant annotations for each example—can
largely resolve the issue of mistaken annota-
tions.
Careful planning and pilot work before
data collection can largely resolve the issue of
ambiguous annotation guidelines.
Handling
legitimate annotator disagreements can take two
fairly different approaches, depending on the goals
of the benchmark.
The simplest approach treats ambiguously la-
beled examples in the same way as mislabeled ex-
amples, and systematically identiﬁes and discards
them during a validation phase. For some tasks,
it may still be possible to test models’ handling
of fundamentally ambiguous linguistic phenomena
or domains using unambiguous examples: In the
case of multiple-choice question answering, for
example, one can construct examples where one
answer candidates is only debatably correct, but
all other candidates are unequivocally wrong. Any
sound model would then be expected to select the
debatable choice.
Alternately, one can decline to assign single, dis-
crete labels to ambiguous examples. This can in-
volve asking models to predict the empirical dis-
tribution of labels that trustworthy annotators as-
sign (Pavlick and Kwiatkowski, 2019; Poesio et al.,
2019), or allowing models to predict any of several
answer choices that are supported by trustworthy
annotators (as in the SQuAD benchmark). This
comes at the cost, though, of requiring many more
annotator judgments per evaluation example.
4.3
Improving Statistical Power
In principle, achieving adequate statistical power
is straightforward: we simply estimate the number
of examples required to reach the desired statisti-
cal power for any plausible short-to-medium term
system evaluation for the task, and collect that num-
ber of examples. In practice, however, costs can
become prohibitive.
For a relatively simple task like NLI, labeling an
existing example likely requires a bare minimum
of 45 seconds (Vania et al., 2020), and creating a
new example requires at least one minute (Bowman
et al., 2020). Even if we use these very optimistic
numbers to estimate annotation speed, a ten-way-
annotated dataset of 500,000 examples will still
cost over $1 million at a $15/hr pay rate.6 Recruit-
ing more experienced annotators or encouraging
annotators to work more carefully could increase
this ﬁgure dramatically. While such an amount of
money is not completely out of reach in a well-
funded ﬁeld like NLP,7 investments of this kind
will inevitably be rare enough that they help rein-
force the ﬁeld’s concentration of data and effort on
a few high-resource languages and tasks.
For settings in which large datasets are necessary,
we see no clear way to avoid high costs. Gamiﬁca-
tion, in the style of the ESP game or ZombiLingo
(Von Ahn and Dabbish, 2004; Fort et al., 2014),
promises to offer free human labor, but at the cost
of the expert time needed to reﬁne the task deﬁ-
nition into a game that is widely enjoyable. This
approach also introduces severe constraints on the
kinds of data collection protocols that can be used
and raises tricky new ethical issues (Morschheuser
and Hamari, 2019). Ultimately, the community
needs to compare the cost of making serious invest-
ments in better benchmarks to the cost of wasting
researcher time and computational resources due
to our inability to measure progress.
4.4
Disincentives for Biased Models
Because there is no one-size-ﬁts-all deﬁnition of
harmful social bias, there is little prospect of creat-
6This ﬁgure ignores platform fees and makes the additional
optimistic assumption that only 10% of fully-annotated exam-
ples will be discarded because of annotator disagreement.
7To put this number in context, public estimates of the cost
of OpenAI’s GPT-3 (Brown et al., 2020) exceed $10M (Wig-
gers, 2020), and in machine translation, Meng et al. (2019)’s
use of 512 Nvidia V100 GPUs for three months would have
cost over $1M USD on commodity cloud infrastructure.

--- Page 8 ---

4850
ing a benchmark for language understanding that
is guaranteed to never reward the development of
harmfully biased models. This is not a compelling
reason to accept the status quo, and we nonethe-
less have a clear opportunity to mitigate some of the
potential harms caused by applied NLP systems be-
fore those systems are even developed. Opting not
to test models for some plausible and potentially-
harmful social bias is, intentionally or not, a politi-
cal choice.
While it would be appealing to try to guarantee
that our evaluation data does not itself demonstrate
evidence of bias, we are aware of no robust strat-
egy for reliably accomplishing this, and work on
the closely-related problem of model bias mitiga-
tion has been fraught with false starts and overly
optimistic claims (Gonen and Goldberg, 2019).
A viable alternate approach could involve the ex-
panded use of auxiliary metrics: Rather than trying
to fully mitigate bias within a single general dataset
and metric for some task, benchmark creators can
introduce a family of additional expert-constructed
test datasets and metrics that each isolate and mea-
sure a speciﬁc type of bias. Any time a model
is evaluated on the primary task test set in this
setting, it would be evaluated in parallel on these
additional bias test sets. This would not prevent
the primary metric from unintentionally and subtly
rewarding biased models, but it would combat this
effect by more directly highlighting and penaliz-
ing bias in models. In addition, the fact that these
metrics would target speciﬁc types of biases would
make it easier for benchmark maintainers to adapt
as changing norms or changing downstream appli-
cations demand coverage of additional potential
harms.
For several tasks, metrics like this already ex-
ist, at least for gender in English, in the form of
auxiliary test sets meant to be combined with a pre-
existing training set (Rudinger et al., 2018; Webster
et al., 2018; Kiritchenko and Mohammad, 2018; Li
et al., 2020). Even so, reﬁning these metrics and
developing new ones will likely require us to face
many of the same challenges that we highlight in
this paper for benchmark design more generally.
The larger challenge in implementing this ap-
proach, however, is a matter of community struc-
ture and incentive design. Methods papers dealing
with tasks for which metrics already exist rarely
report numbers on these metrics. Even for the Su-
perGLUE benchmark, which requires users to com-
pute test set metrics on the DNC Winogender test
set in order to reveal test set results for any other
target task, a large majority of papers that report
test set numbers omit this metric and decline to
report potentially unﬂattering bias numbers (Raffel
et al., 2020; Pruksachatkun et al., 2020; Schick and
Schütze, 2020; He et al., 2020).
The difﬁculty, then, is in developing community
infrastructure to encourage the widespread report-
ing of metrics that address the full range of rel-
evant likely harms. This could plausibly involve
peer review norms, explicit publication venue poli-
cies, stricter versions of the SuperGLUE approach
for which users can only retrieve aggregate perfor-
mance numbers, without a precise separation of
the primary and bias-oriented metrics, or even the
introduction of professional licensing standards.
Of course, ensuring that bias is measured and re-
ported is not enough to prevent bias-related harms
from emerging in practice: It is also necessary to
ensure that those who build and deploy NLP prod-
ucts will take these metrics seriously and respond
to them appropriately. And, of course, even if a
system encodes no social bias at all, it can still be
deployed in ways that produce unfair or unjust out-
comes. These difﬁcult issues are beyond the scope
of a paper on benchmark design.
5
Related Work
The NLP and ML research communities are in-
creasingly interested in issues surrounding data and
evaluation. This section surveys relevant positions
and issues that don’t quite ﬁt our schema.
Welty et al. (2019) advocate for the more pre-
cise reporting of the focus and abilities of test sets
and metrics in ML broadly, with a focus on is-
sues surrounding statistical power. Bender and
Friedman (2018) and Gebru et al. (2018) advocate
for explicit freestanding datasheets documenting
dataset releases of all kinds, with a focus on mak-
ing potential harmful mismatches between data and
application visible, and Hutchinson et al. (2021)
argue along similar lines for a broader program of
transparency and stakeholder engagement in data
creation. Dodge et al. (2019) lay out a set of best
practices for results reporting, with a focus on the
impact of hyperparameter tuning on model com-
parison. Ethayarajh and Jurafsky (2020) advocate
for the inclusion of efﬁciency considerations in
leaderboard design. Boyd-Graber and Börschinger
(2020) describe ways that trivia competitions can

--- Page 9 ---

4851
provide a model for carefully-considered dataset
design.
Church and Hestness (2019) revisit the argu-
ments that motivated the NLP community’s shift to-
ward quantitative benchmarking in the early 1990s
and warn that the overwhelming success of this
shift has indirectly laid the groundwork for the
widespread use of poor-quality benchmarks. Blod-
gett et al. (2020) challenge researchers working on
social bias in NLP to focus more precisely on spe-
ciﬁc types of harm to speciﬁc populations of users,
a challenge that our broad position piece does not
fully meet.
NLP has had longstanding debates over the types
of tasks that best test substantial language under-
standing skills. Many task-speciﬁc papers con-
tribute to this debate, as does a prominent recent
thread advocating for an increased focus on ground-
ing of various kinds by Bender and Koller (2020),
Bisk et al. (2020), Zellers et al. (2020), and others.
6
Conclusion
Benchmarking for NLU is broken. We lay out
four major criteria that benchmarks should fulﬁll
to offer faithful, useful, and responsible measures
of language ability. We argue that departing from
IID evaluation (as is seen with benchmark datasets
collected by adversarial ﬁltering) does not help to
address these criteria, but lay out in broad strokes
how each criterion might be addressed directly.
Nonetheless, important open research questions
remain. Most centrally, it is still unclear how best
to integrate expert effort into crowdsourced data
collection, and we do not yet see a clear institu-
tional model by which to ensure that bias metrics
are built and used when they are most needed.
Ethical Considerations
This paper advocates for reforms to a set of bench-
marking practices that have so far largely failed to
address issues of social bias, and that have thereby
helped create a false sense of security among those
building applied systems. While this paper offers
no complete and satisfactory solutions, it proposes
measures that should contribute to harm reduction.
Acknowledgments
We thank Emily Bender, Iacer Calixto, Haokin Liu,
Kyunghyun Cho, Will Huang, Jamie Kiros, and
audiences at CMU, Google, and Apple for feedback
on these ideas.
This project has beneﬁted from ﬁnancial sup-
port to SB by Eric and Wendy Schmidt (made by
recommendation of the Schmidt Futures program),
Samsung Research (under the project Improving
Deep Learning using Latent Structure), and Intuit.
This material is based upon work supported by
the National Science Foundation under Grant No.
1922658. Any opinions, ﬁndings, and conclusions
or recommendations expressed in this material are
those of the author(s) and do not necessarily reﬂect
the views of the National Science Foundation.
References
Emily M. Bender and Batya Friedman. 2018.
Data
statements for natural language processing: Toward
mitigating system bias and enabling better science.
Transactions of the Association for Computational
Linguistics, 6:587–604.
Emily M. Bender and Alexander Koller. 2020. Climb-
ing towards NLU: On meaning, form, and under-
standing in the age of data. In Proceedings of the
58th Annual Meeting of the Association for Compu-
tational Linguistics, pages 5185–5198, Online. As-
sociation for Computational Linguistics.
Yonatan Bisk, Ari Holtzman, Jesse Thomason, Jacob
Andreas, Yoshua Bengio, Joyce Chai, Mirella Lap-
ata, Angeliki Lazaridou, Jonathan May, Aleksandr
Nisnevich, Nicolas Pinto, and Joseph Turian. 2020.
Experience grounds language. In Proceedings of the
2020 Conference on Empirical Methods in Natural
Language Processing (EMNLP), pages 8718–8735,
Online. Association for Computational Linguistics.
Su Lin Blodgett, Solon Barocas, Hal Daumé III, and
Hanna Wallach. 2020.
Language (technology) is
power: A critical survey of “bias” in NLP. In Pro-
ceedings of the 58th Annual Meeting of the Asso-
ciation for Computational Linguistics, pages 5454–
5476, Online. Association for Computational Lin-
guistics.
Tolga
Bolukbasi,
Kai-Wei
Chang,
James
Zou,
Venkatesh Saligrama,
and Adam Kalai. 2016.
Man is to computer programmer as woman is to
homemaker? Debiasing word embeddings. In Pro-
ceedings of the 30th International Conference on
Neural Information Processing Systems, NIPS’16,
page 4356–4364, Red Hook, NY, USA. Curran
Associates Inc.
Samuel R. Bowman, Gabor Angeli, Christopher Potts,
and Christopher D. Manning. 2015. A large anno-
tated corpus for learning natural language inference.
In Proceedings of the 2015 Conference on Empiri-
cal Methods in Natural Language Processing, pages
632–642, Lisbon, Portugal. Association for Compu-
tational Linguistics.

--- Page 10 ---

4852
Samuel R. Bowman, Jennimaria Palomaki, Livio Bal-
dini Soares, and Emily Pitler. 2020. New protocols
and negative results for textual entailment data col-
lection. In Proceedings of the 2020 Conference on
Empirical Methods in Natural Language Process-
ing (EMNLP), pages 8203–8214, Online. Associa-
tion for Computational Linguistics.
Jordan Boyd-Graber and Benjamin Börschinger. 2020.
What question answering can learn from trivia nerds.
In Proceedings of the 58th Annual Meeting of the
Association for Computational Linguistics, pages
7422–7435, Online. Association for Computational
Linguistics.
Tom Brown, Benjamin Mann, Nick Ryder, Melanie
Subbiah,
Jared
D
Kaplan,
Prafulla
Dhariwal,
Arvind Neelakantan, Pranav Shyam, Girish Sastry,
Amanda Askell, Sandhini Agarwal, Ariel Herbert-
Voss, Gretchen Krueger, Tom Henighan, Rewon
Child, Aditya Ramesh, Daniel Ziegler, Jeffrey Wu,
Clemens Winter, Chris Hesse, Mark Chen, Eric
Sigler, Mateusz Litwin, Scott Gray, Benjamin Chess,
Jack Clark, Christopher Berner, Sam McCandlish,
Alec Radford, Ilya Sutskever, and Dario Amodei.
2020. Language models are few-shot learners. In
Advances in Neural Information Processing Systems,
volume 33, pages 1877–1901. Curran Associates,
Inc.
Dallas Card, Peter Henderson, Urvashi Khandelwal,
Robin Jia, Kyle Mahowald, and Dan Jurafsky. 2020.
With little power comes great responsibility.
In
Proceedings of the 2020 Conference on Empirical
Methods in Natural Language Processing (EMNLP),
pages 9263–9274, Online. Association for Computa-
tional Linguistics.
Kenneth Ward Church and Joel Hestness. 2019. A sur-
vey of 25 years of evaluation.
Natural Language
Engineering, 25(6):753–767.
Robin Cooper, Dick Crouch, Jan Van Eijck, Chris Fox,
Johan Van Genabith, Jan Jaspars, Hans Kamp, David
Milward, Manfred Pinkal, Massimo Poesio, et al.
1996. Using the framework. Technical report, LRE
62-051 D-16, The FraCaS Consortium.
Jacob Devlin, Ming-Wei Chang, Kenton Lee, and
Kristina Toutanova. 2019.
BERT: Pre-training of
deep bidirectional transformers for language under-
standing.
In Proceedings of the 2019 Conference
of the North American Chapter of the Association
for Computational Linguistics: Human Language
Technologies, Volume 1 (Long and Short Papers),
pages 4171–4186, Minneapolis, Minnesota. Associ-
ation for Computational Linguistics.
Jesse Dodge, Suchin Gururangan, Dallas Card, Roy
Schwartz, and Noah A. Smith. 2019.
Show your
work: Improved reporting of experimental results.
In Proceedings of the 2019 Conference on Empirical
Methods in Natural Language Processing and the
9th International Joint Conference on Natural Lan-
guage Processing (EMNLP-IJCNLP), pages 2185–
2194, Hong Kong, China. Association for Computa-
tional Linguistics.
Dheeru Dua, Ananth Gottumukkala, Alon Talmor,
Sameer Singh, and Matt Gardner. 2019. ORB: An
open reading benchmark for comprehensive evalu-
ation of machine reading comprehension.
arXiv
preprint 1912.12598.
Jesse Dunietz, Greg Burnham, Akash Bharadwaj,
Owen Rambow, Jennifer Chu-Carroll, and Dave Fer-
rucci. 2020. To test machine comprehension, start
by deﬁning comprehension. In Proceedings of the
58th Annual Meeting of the Association for Compu-
tational Linguistics, pages 7839–7859, Online. As-
sociation for Computational Linguistics.
Kawin Ethayarajh and Dan Jurafsky. 2020. Utility is in
the eye of the user: A critique of NLP leaderboards.
In Proceedings of the 2020 Conference on Empirical
Methods in Natural Language Processing (EMNLP),
pages 4846–4853, Online. Association for Computa-
tional Linguistics.
Allyson Ettinger, Sudha Rao, Hal Daumé III, and
Emily M. Bender. 2017. Towards linguistically gen-
eralizable NLP systems: A workshop and shared
task.
In Proceedings of the First Workshop on
Building Linguistically Generalizable NLP Systems,
pages 1–10, Copenhagen, Denmark. Association for
Computational Linguistics.
Marjorie Florestall. 2008. Is a burrito a sandwich? Ex-
ploring race, class, and culture in contracts. Michi-
gan Journal of Race and Language, 14:1.
Karën Fort, Bruno Guillaume, and Hadrien Chastant.
2014. Creating Zombilingo, a game with a purpose
for dependency syntax annotation. In Proceedings
of the First International Workshop on Gamiﬁcation
for Information Retrieval, pages 2–6.
Matt Gardner, Yoav Artzi, Victoria Basmov, Jonathan
Berant, Ben Bogin, Sihao Chen, Pradeep Dasigi,
Dheeru Dua, Yanai Elazar, Ananth Gottumukkala,
Nitish Gupta, Hannaneh Hajishirzi, Gabriel Ilharco,
Daniel Khashabi, Kevin Lin, Jiangming Liu, Nel-
son F. Liu, Phoebe Mulcaire, Qiang Ning, Sameer
Singh, Noah A. Smith, Sanjay Subramanian, Reut
Tsarfaty, Eric Wallace, Ally Zhang, and Ben Zhou.
2020. Evaluating models’ local decision boundaries
via contrast sets. In Proceedings of the 2020 Con-
ference on Empirical Methods in Natural Language
Processing: Findings, pages 1307–1323, Online. As-
sociation for Computational Linguistics.
Timnit Gebru, Jamie Morgenstern, Briana Vecchione,
Jennifer Wortman Vaughan, Hanna Wallach, Hal
Daumé III, and Kate Crawford. 2018. Datasheets
for datasets. arXiv preprint 1803.09010.
Hila Gonen and Yoav Goldberg. 2019. Lipstick on a
pig: Debiasing methods cover up systematic gender

--- Page 11 ---

4853
biases in word embeddings but do not remove them.
In Proceedings of the 2019 Conference of the North
American Chapter of the Association for Computa-
tional Linguistics: Human Language Technologies,
Volume 1 (Long and Short Papers), pages 609–614,
Minneapolis, Minnesota. Association for Computa-
tional Linguistics.
Pengcheng He, Xiaodong Liu, Jianfeng Gao, and
Weizhu Chen. 2020.
DeBERTa:
Decoding-
enhanced BERT with disentangled attention. arXiv
preprint 2006.03654.
Hai Hu, Kyle Richardson, Liang Xu, Lu Li, Sandra
Kübler, and Lawrence Moss. 2020. OCNLI: Orig-
inal Chinese Natural Language Inference. In Find-
ings of the Association for Computational Linguis-
tics: EMNLP 2020, pages 3512–3526, Online. As-
sociation for Computational Linguistics.
Lifu Huang, Ronan Le Bras, Chandra Bhagavatula, and
Yejin Choi. 2019.
Cosmos QA: Machine reading
comprehension with contextual commonsense rea-
soning. In Proceedings of the 2019 Conference on
Empirical Methods in Natural Language Processing
and the 9th International Joint Conference on Natu-
ral Language Processing (EMNLP-IJCNLP), pages
2391–2401, Hong Kong, China. Association for
Computational Linguistics.
Ben Hutchinson, Andrew Smart, Alex Hanna, Emily
Denton, Christina Greer, Oddur Kjartansson, Parker
Barnes, and Margaret Mitchell. 2021. Towards ac-
countability for machine learning datasets: Practices
from software engineering and infrastructure.
In
Proceedings of the 2021 ACM Conference on Fair-
ness, Accountability, and Transparency, FAccT ’21,
page 560–575, New York, NY, USA. Association for
Computing Machinery.
Robin Jia and Percy Liang. 2017. Adversarial exam-
ples for evaluating reading comprehension systems.
In Proceedings of the 2017 Conference on Empiri-
cal Methods in Natural Language Processing, pages
2021–2031, Copenhagen, Denmark. Association for
Computational Linguistics.
Svetlana Kiritchenko and Saif Mohammad. 2018. Ex-
amining gender and race bias in two hundred sen-
timent analysis systems.
In Proceedings of the
Seventh Joint Conference on Lexical and Compu-
tational Semantics, pages 43–53, New Orleans,
Louisiana. Association for Computational Linguis-
tics.
Tom Kwiatkowski, Jennimaria Palomaki, Olivia Red-
ﬁeld, Michael Collins, Ankur Parikh, Chris Al-
berti, Danielle Epstein, Illia Polosukhin, Jacob De-
vlin, Kenton Lee, Kristina Toutanova, Llion Jones,
Matthew Kelcey, Ming-Wei Chang, Andrew M. Dai,
Jakob Uszkoreit, Quoc Le, and Slav Petrov. 2019.
Natural questions: A benchmark for question an-
swering research. Transactions of the Association
for Computational Linguistics, 7:452–466.
Ronan Le Bras, Swabha Swayamdipta, Chandra Bha-
gavatula, Rowan Zellers, Matthew E Peters, Ashish
Sabharwal, and Yejin Choi. 2020. Adversarial ﬁlters
of dataset biases. arXiv preprint 2002.04108.
Hector J. Levesque, Ernest Davis, and Leora Mor-
genstern. 2012.
The Winograd schema challenge.
In Proceedings of the Thirteenth International Con-
ference on Principles of Knowledge Representa-
tion and Reasoning, KR’12, pages 552–561. AAAI
Press.
Tao Li, Daniel Khashabi, Tushar Khot, Ashish Sab-
harwal, and Vivek Srikumar. 2020. UNQOVERing
stereotyping biases via underspeciﬁed questions. In
Findings of the Association for Computational Lin-
guistics: EMNLP 2020, pages 3475–3489, Online.
Association for Computational Linguistics.
Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Man-
dar Joshi, Danqi Chen, Omer Levy, Mike Lewis,
Luke Zettlemoyer, and Veselin Stoyanov. 2019.
RoBERTa: A robustly optimized BERT pretraining
approach. arXiv preprint 1907.11692.
Andrew L. Maas, Raymond E. Daly, Peter T. Pham,
Dan Huang, Andrew Y. Ng, and Christopher Potts.
2011. Learning word vectors for sentiment analy-
sis. In Proceedings of the 49th Annual Meeting of
the Association for Computational Linguistics: Hu-
man Language Technologies, pages 142–150, Port-
land, Oregon, USA. Association for Computational
Linguistics.
Tom McCoy, Ellie Pavlick, and Tal Linzen. 2019.
Right for the wrong reasons: Diagnosing syntactic
heuristics in natural language inference. In Proceed-
ings of the 57th Annual Meeting of the Association
for Computational Linguistics, pages 3428–3448,
Florence, Italy. Association for Computational Lin-
guistics.
Yuxian Meng, Xiangyuan Ren, Zijun Sun, Xiaoya Li,
Arianna Yuan, Fei Wu, and Jiwei Li. 2019. Large-
scale pretraining for neural machine translation with
tens of billions of sentence pairs.
arXiv preprint
1909.11861.
Benedikt Morschheuser and Juho Hamari. 2019. The
gamiﬁcation of work: Lessons from crowdsourcing.
Journal of Management Inquiry, 28(2):145–148.
Aakanksha Naik, Abhilasha Ravichander, Norman
Sadeh, Carolyn Rose, and Graham Neubig. 2018.
Stress test evaluation for natural language inference.
In Proceedings of the 27th International Conference
on Computational Linguistics, pages 2340–2353,
Santa Fe, New Mexico, USA. Association for Com-
putational Linguistics.
Nikita Nangia and Samuel Bowman. 2019. Human vs.
muppet: A conservative estimate of human perfor-
mance on the glue benchmark. In Proceedings of the
57th Annual Meeting of the Association for Compu-
tational Linguistics, pages 4566–4575.

--- Page 12 ---

4854
Yixin Nie, Adina Williams, Emily Dinan, Mohit
Bansal, Jason Weston, and Douwe Kiela. 2020. Ad-
versarial NLI: A new benchmark for natural lan-
guage understanding. In Proceedings of the 58th An-
nual Meeting of the Association for Computational
Linguistics, pages 4885–4901, Online. Association
for Computational Linguistics.
Timothy Niven and Hung-Yu Kao. 2019. Probing neu-
ral network comprehension of natural language ar-
guments. In Proceedings of the 57th Annual Meet-
ing of the Association for Computational Linguis-
tics, pages 4658–4664, Florence, Italy. Association
for Computational Linguistics.
Denis Paperno, Germán Kruszewski, Angeliki Lazari-
dou, Ngoc Quan Pham, Raffaella Bernardi, San-
dro Pezzelle, Marco Baroni, Gemma Boleda, and
Raquel Fernández. 2016. The LAMBADA dataset:
Word prediction requiring a broad discourse context.
In Proceedings of the 54th Annual Meeting of the As-
sociation for Computational Linguistics (Volume 1:
Long Papers), pages 1525–1534, Berlin, Germany.
Association for Computational Linguistics.
Ellie Pavlick and Tom Kwiatkowski. 2019. Inherent
disagreements in human textual inferences. Transac-
tions of the Association for Computational Linguis-
tics, 7:677–694.
Massimo Poesio, Jon Chamberlain, Silviu Paun, Juntao
Yu, Alexandra Uma, and Udo Kruschwitz. 2019. A
crowdsourced corpus of multiple judgments and dis-
agreement on anaphoric interpretation. In Proceed-
ings of the 2019 Conference of the North American
Chapter of the Association for Computational Lin-
guistics: Human Language Technologies, Volume 1
(Long and Short Papers), pages 1778–1789, Min-
neapolis, Minnesota. Association for Computational
Linguistics.
Adam Poliak, Aparajita Haldar, Rachel Rudinger, J. Ed-
ward Hu, Ellie Pavlick, Aaron Steven White, and
Benjamin Van Durme. 2018. Collecting diverse nat-
ural language inference problems for sentence rep-
resentation evaluation. In Proceedings of the 2018
Conference on Empirical Methods in Natural Lan-
guage Processing, pages 67–81, Brussels, Belgium.
Association for Computational Linguistics.
Yada Pruksachatkun,
Jason Phang,
Haokun Liu,
Phu Mon Htut, Xiaoyi Zhang, Richard Yuanzhe
Pang, Clara Vania, Katharina Kann, and Samuel R.
Bowman. 2020. Intermediate-task transfer learning
with pretrained language models: When and why
does it work?
In Proceedings of the 58th Annual
Meeting of the Association for Computational Lin-
guistics, pages 5231–5247, Online. Association for
Computational Linguistics.
Colin Raffel, Noam Shazeer, Adam Roberts, Kather-
ine Lee, Sharan Narang, Michael Matena, Yanqi
Zhou, Wei Li, and Peter J. Liu. 2020.
Exploring
the limits of transfer learning with a uniﬁed text-to-
text transformer. Journal of Machine Learning Re-
search, 21(140):1–67.
Pranav Rajpurkar, Robin Jia, and Percy Liang. 2018.
Know what you don’t know: Unanswerable ques-
tions for SQuAD. In Proceedings of the 56th An-
nual Meeting of the Association for Computational
Linguistics (Volume 2: Short Papers), pages 784–
789, Melbourne, Australia. Association for Compu-
tational Linguistics.
Pranav Rajpurkar, Jian Zhang, Konstantin Lopyrev, and
Percy Liang. 2016. SQuAD: 100,000+ questions for
machine comprehension of text. In Proceedings of
the 2016 Conference on Empirical Methods in Natu-
ral Language Processing, pages 2383–2392, Austin,
Texas. Association for Computational Linguistics.
Marco Tulio Ribeiro, Tongshuang Wu, Carlos Guestrin,
and Sameer Singh. 2020.
Beyond accuracy: Be-
havioral testing of NLP models with CheckList. In
Proceedings of the 58th Annual Meeting of the Asso-
ciation for Computational Linguistics, pages 4902–
4912, Online. Association for Computational Lin-
guistics.
Rachel Rudinger,
Chandler May,
and Benjamin
Van Durme. 2017. Social bias in elicited natural lan-
guage inferences. In Proceedings of the First ACL
Workshop on Ethics in Natural Language Process-
ing, pages 74–79, Valencia, Spain. Association for
Computational Linguistics.
Rachel Rudinger, Jason Naradowsky, Brian Leonard,
and Benjamin Van Durme. 2018.
Gender bias in
coreference resolution. In Proceedings of the 2018
Conference of the North American Chapter of the
Association for Computational Linguistics: Human
Language Technologies, Volume 2 (Short Papers),
pages 8–14, New Orleans, Louisiana. Association
for Computational Linguistics.
Keisuke Sakaguchi, Ronan Le Bras, Chandra Bhaga-
vatula, and Yejin Choi. 2019. Winogrande: An ad-
versarial winograd schema challenge at scale. arXiv
preprint 1907.10641.
Timo Schick and Hinrich Schütze. 2020. It’s not just
size that matters: Small language models are also
few-shot learners. arXiv preprint 2009.07118.
Chenglei Si, Shuohang Wang, Min-Yen Kan, and Jing
Jiang. 2019. What does BERT learn from multiple-
choice reading comprehension datasets?
arXiv
preprint 1910.12391.
Saku Sugawara, Pontus Stenetorp, and Akiko Aizawa.
2020a. Benchmarking machine reading comprehen-
sion: A psychological perspective. arXiv preprint
2004.01912.
Saku Sugawara, Pontus Stenetorp, Kentaro Inui, and
A. Aizawa. 2020b. Assessing the benchmarking ca-
pacity of machine reading comprehension datasets.
In AAAI.
Nitasha Tiku. 2020. India’s engineers have thrived in
silicon valley. so has its caste system. The Washing-
ton Post.

--- Page 13 ---

4855
Masatoshi Tsuchiya. 2018.
Performance impact
caused by hidden bias of training data for recog-
nizing textual entailment.
In Proceedings of the
Eleventh International Conference on Language Re-
sources and Evaluation (LREC 2018), Miyazaki,
Japan. European Language Resources Association
(ELRA).
Clara Vania, Ruijie Chen, and Samuel R. Bowman.
2020. Asking Crowdworkers to Write Entailment
Examples: The Best of Bad options.
In Proceed-
ings of the 1st Conference of the Asia-Paciﬁc Chap-
ter of the Association for Computational Linguistics
and the 10th International Joint Conference on Nat-
ural Language Processing, pages 672–686, Suzhou,
China. Association for Computational Linguistics.
Luis Von Ahn and Laura Dabbish. 2004. Labeling im-
ages with a computer game. In Proceedings of the
SIGCHI conference on Human factors in computing
systems, pages 319–326.
Alex Wang,
Yada Pruksachatkun,
Nikita Nangia,
Amanpreet Singh, Julian Michael, Felix Hill, Omer
Levy, and Samuel Bowman. 2019a. SuperGLUE: A
stickier benchmark for general-purpose language un-
derstanding systems. In Advances in Neural Infor-
mation Processing Systems, pages 3266–3280.
Alex Wang, Amanpreet Singh, Julian Michael, Felix
Hill, Omer Levy, and Samuel R Bowman. 2019b.
GLUE: A multi-task benchmark and analysis plat-
form for natural language understanding.
In Pro-
ceedings of the International Conference on Learn-
ing Representations.
Kellie Webster, Marta Recasens, Vera Axelrod, and Ja-
son Baldridge. 2018.
Mind the gap: A balanced
corpus of gendered ambiguous pronouns. Transac-
tions of the Association for Computational Linguis-
tics, 6:605–617.
Chris Welty, Praveen Paritosh, and Lora Aroyo. 2019.
Metrology for AI: From benchmarks to instruments.
arXiv preprint 1911.01875.
Kyle Wiggers. 2020. OpenAI launches an API to com-
mercialize its research. VentureBeat.
Rowan Zellers, Yonatan Bisk, Roy Schwartz, and
Yejin Choi. 2018. SWAG: A large-scale adversar-
ial dataset for grounded commonsense inference. In
Proceedings of the 2018 Conference on Empirical
Methods in Natural Language Processing, pages 93–
104. Association for Computational Linguistics.
Rowan Zellers, Ari Holtzman, Elizabeth Clark, Lianhui
Qin, Ali Farhadi, and Yejin Choi. 2020. Evaluating
machines by their real-world language use. arXiv
preprint 2004.03607.
```
