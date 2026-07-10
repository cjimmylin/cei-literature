---
title: "2021-Schlangen-Targeting the Benchmark - Background Extract"
source_pdf: "2021-Schlangen-Targeting the Benchmark.pdf"
source_folder: "02-external-papers"
pages: 5
extracted_at: "2026-04-03T10:25:00"
---

# Background Extract: 2021-Schlangen-Targeting the Benchmark

**Source PDF:** 2021-Schlangen-Targeting the Benchmark.pdf
**Source:** 02-external-papers
**Total Pages:** 5

---

## Content

```
--- Page 1 ---

Targeting the Benchmark: On Methodology in Current
Natural Language Processing Research
David Schlangen
Computational Linguistics / Department of Linguistics
University of Potsdam, Germany
david.schlangen@uni-potsdam.de
Abstract
It has become a common pattern in our ﬁeld:
One group introduces a language task, exem-
pliﬁed by a dataset, which they argue is chal-
lenging enough to serve as a benchmark. They
also provide a baseline model for it, which then
soon is improved upon by other groups. Often,
research efforts then move on, and the pattern
repeats itself. What is typically left implicit
is the argumentation for why this constitutes
progress, and progress towards what. In this
paper, we try to step back for a moment from
this pattern and work out possible argumenta-
tions and their parts.
1
Introduction
The goal of any ﬁeld of research is to make progress
towards answering its foundational questions. To
do so, a methodology is required that guides at-
tempts at providing or improving answer proposals.
In natural language processing, the object of study
is human language, and any methodology for doing
research in this ﬁeld will need to have some con-
tact with examples of this object. This contact has
become more and more direct in the past decades,
with samples of language becoming more directly
the material from which proposals (in the form
of statistical models) are derived. Recent years
have seen an increase in the collection of samples
speciﬁcally for the purpose of creating benchmarks,
against which progress in devising models can be
measured. It is this function of benchmarking, and
its role in a progress-oriented methodology, that
this paper aims to investigate.
Figure 1 illustrates the basic structure of a bench-
marking methodology: A language task is devised
that is a) restricted enough to be managable with
current methods, and b) deemed challenging for the
capabilities that it involves.1 For this task, a dataset
1This ﬁgure is from (Schlangen, 2019), of which this is a
shorter version developed in a slightly different direction.
Task T 
• task 
description
Dataset D 
• collection 
instructions
exempliﬁes
Set CL of capabilites of 
competent language user
Cognitive 
Capability C
Cognitive 
Capability C’
Cognitive 
Capability C’’
…
Dataset D’ 
Task T’ 
• annotation 
manual
Model M’ 
• architecture
optimized for
exempliﬁes
involves
Model M 
• architecture
optimized for
?
?
Figure 1: Relations between Research Objects in a
Benchmark-Driven Methodology
is collected, often via crowd sourcing, on which in
turn models are trained and compared, using evalu-
ation metrics deﬁned together with the task. What
can we learn by following such a methodology?
Let’s look at the components ﬁrst and then at ways
in which this methodology is, might, and perhaps
should be used.
2
What is a Language Benchmark?
2.1
What is a Benchmark?
In computing, a benchmark is “a problem that has
been designed to evaluate the performance of a
system [which] is subjected to a known workload
and the performance of the system against this
workload is measured. Typically the purpose is to
compare the measured performance with that of
other systems that have been subject to the same
benchmark test.” (Butterﬁeld et al., 2016).
The use of this term in NLP is related: here,
benchmark tasks are also speciﬁcally designed for
evaluation; however, an important difference is that
what is being evaluated is not a full system that has
a separate main purpose, but rather an algorithm
that is instantiated on the benchmark itself. We will
discuss the consequences of this below.
This kind of evaluation of learning algorithm
has a long tradition in the ﬁeld of machine learn-
arXiv:2007.04792v1  [cs.CL]  7 Jul 2020

--- Page 2 ---

ing research.2 In this ﬁeld, a new algorithm would
normally be tested on a large collection of datasets,
possibly ranging from classiﬁcations of ﬂowers to
classiﬁcation of credit records, with no assumption
of any internal connection between the datasets.
Again, NLP is different here, as all datasets rep-
resent facets of the same underlying phenomenon,
language use.
We will argue that these two differences (life out-
side of benchmarking, and internal connection be-
tween tasks) are important, but understudied. But
ﬁrst we look at the notion of a language task in
some more detail.
2.2
What is a Language Task?
A language task is a mapping between an input
space and an output or action space, at least one
of which contains natural language expressions.
The mapping has to conform to a task description,
which is typically given only informally, making
reference to theoretical or pre-theoretical constructs
external to the deﬁnition, such as “translation” or
“is true of”. We call this an intensional descrip-
tion. Typically, a task will also be speciﬁed ex-
tensionally through the provision of a dataset of
examples of the mapping (that is, pairs of state and
action). To collect such a dataset, the task descrip-
tion (e.g., “classiﬁcation of entailment relations
between sentence pairs”) must be operationalised
into a collection instruction (“please mark whether
the a situation that is well described by sentence A
could normally also be described by sentence B”).
3
How Can It be Evaluated?
3.1
Relation Task / Dataset
Given a task and a dataset, the ﬁrst question to ask
is how well the latter exempliﬁes the former. In-
vestigating this is relatively straightforward. First,
the dataset should be veriﬁed, which is to check
whether the provided input/output pairs can indeed
be judged correct relative to the task (in its inten-
sional description). If the examples are collected
speciﬁcally for the purpose of exemplifying the
task, this is the process of controlling annotation,
and standard methodologies exist (Artstein and
Poesio, 2008; Pustejovsky and Stubbs, 2013). Care
needs to be taken that the task is actually well-
deﬁned enough to pose an unambiguous challenge
2For example, the UCI Machine Learning Repository has
been collecting and providing datasets for more than 20 years
now (Dua and Graff, 2019).
to capable language users.3
Validating a dataset is a less formalised process.
It comprises arguing that the dataset indeed exem-
pliﬁes the task intension well. For example, pairs
only of images of giraffes and sentences describing
them would arguably not exemplify the general task
of image description very well (even if the descrip-
tions are accurate), while perhaps exemplifying the
task of giraffe image description.
Another way to evaluate a dataset is by trying
to model it. If a model can “solve” the dataset
even when deprived of information that for theoret-
ical or pre-theoretical reasons is seen to be crucial,
the dataset can be considered an unsatisfactory ex-
empliﬁcation of the task. E.g., in a visual (polar)
question answering setting (Antol et al., 2015), if
in a dataset all and only the expressions that men-
tion giraffes are true, a model could seize on this
fact and perform well without needing the images,
which would be evidence that the dataset is deﬁ-
cient relative to the task description.4
3.2
Relation Cognitive Capability / Task
While the dataset forms the visible surface of the
task, it is the task itself that needs to provide value.
We can categorise tasks by how they are embed-
ded in further uses: a product task task is one that
can be argued to have direct value to consumers
(such as translation, or search); an annotation task
is one where the task description is theoretically
motivated and the output a linguistically motivated
object; a benchmark task – which is the type that
concerns us here – ﬁnally is one which gets its
value from how well it tests a particular ability
(and nothing else) and how well it discriminates
learners based on this ability.5
For a language benchmark task, the argument
roughly goes as follows (even if typically only
3Pavlick and Kwiatkowski (2019), for example, show that
the task of annotation textual entailments can lead to faultless
annotator disagreements.
4The task of visual question answering provides an in-
teresting example case of such a development. After Antol
et al. (2015) introduced the ﬁrst large scale dataset for this
task, it quickly became clear that this dataset could be handled
competitively by models that were deprived of visual input
(“language bias”, as noted e.g. by Jabri et al., 2016). This
problem was then addressed by Goyal et al. (2017) with the
construction of a less biased (and hence more valid) corpus
for the same task.
5Martinez-Plumed
and
Hernandez-Orallo
(2018),
analysing AI benchmarks in general, distinguish between
difﬁculty (which determines the ability level which must
be reached to perform better than chance on a task) and
discrimination (the slope of the graph ability level vs.
probability of correct response.

--- Page 3 ---

made implicitly): To be good at task T, an agent
must possess a set CT of capabilities (of represen-
tational or computational nature). If the c ∈CT
are capabilities that competent language users can
be shown or argued to possess and make use of
in using language—let’s call the set of these capa-
bilities of a competent language user CL, so that
CT ⊆CL— then being able to model these capa-
bilities (via modelling the task) results in progress
towards the ultimate goal, which is to model com-
petent language use. And hence, any task T that
comes with an interesting set CT is a good task.6
Under what conditions does this argument work?
First of all, the assumed connection to the set of
capabilities must indeed be there. We have al-
ready seen a way to challenge a claimed connection,
through providing a model that can “solve” a given
task (via a dataset) while not having access to in-
formation that, given our analysis of the task and
interest in CT , should be involved in the capabil-
ity.7 (Although this challenge in the ﬁrst instance
only targets the dataset and not the task itself.)
Secondly, following usual scientiﬁc methodol-
ogy (Popper, 1934), we can rank the value of an
instantiation of this argument by how precisely the
capability is speciﬁed, from the trivially correct
“task T involves the capability to do task T” to a
statement that could be wrong, e.g. “task T involves
the capability to compute the syntactic structure of
a natural language sentence”. Such a statement
must make reference to theoretical constructs be-
longing to the analysis of cognitive capabilities.
6To give some examples of informal versions of this ar-
gument, and chosing papers more or less randomly, here are
some quotes:
From the paper that introduced the visual question answer-
ing task (Antol et al., 2015): “What makes for a compelling
AI-complete task? We believe that in order to spawn the next
generation of AI algorithms, an ideal task should (i) require
multi-modal knowledge beyond a single sub-domain (such
as CV) and (ii) have a well-deﬁned quantitative evaluation
metric to track progress. [. . . ] Open-ended questions require a
potentially vast set of AI capabilities to answer – ﬁne-grained
recognition [...], object detection [...], activity recognition
[...], knowledge based reasoning [...], and commonsense
reasoning [. . . ].”
Williams et al. (2018), on computing entailments: “The
task of natural language inference (NLI) is well positioned
to serve as a benchmark task for research on NLU. [...] In
particular, a model must handle phenomena like lexical entail-
ment, quantiﬁcation, coreference, tense, belief, modality, and
lexical and syntactic ambiguity.”
7Such an attack challenges the claim of there being a neces-
sary connection between handling T and possessing capability
c. It might still very well be that humans can only perform
this task if they possess capability c (and all the knowledge
involved in it), because they wouldn’t be able to pick up the
statistical correlations that could be exploited.
Furthermore, we can rank the motivation given
for a task by how explicit it is in delineating the
set of capabilities it involves. For a given c ∈CT ,
is “c as required by T” fully separable from any
other tasks involving c? Or is “c as required by T”
perhaps all that there is to know about c, that is, is
c exhaustively represented by T?
Finally, underlying the benchmarking methodol-
ogy — where the benchmark is not just a measuring
tool, but also a modelling target — there has to to
be the assumption that some sort of transferable
knowledge is generated by modelling T, so that
what the model has learned about (a sufﬁciently
generally speciﬁed) c can be used in other tasks
that involve c. (Let’s call this transferability; which
strictly speaking is a property of models, not of
tasks.) More on this below.
To sum up, a benchmark task gets its value from
its connection to a particular facet of language, a
particular capability of language users; this in turn
seems to be difﬁcult to specify without access to
terms from theories of the domain, which allow us
to name these capabilities.8,9
4
How are Language Benchmarks Used?
In the way that these tasks are set up, as single-step
tasks that humans can quickly do (“describe this
image”, “is the elephant [in this image] sleeping?”,
“does sentence A follow from sentence B?”), it is
tempting to see a similarity to tasks used in intel-
ligence testing (see e.g. Borsboom (2005) for an
introduction). There is a crucial difference, how-
ever: Where intelligence testing works more in
the way standard computing benchmarking works
(subjecting the otherwise functioning learner to a
standardised workload), in NLP, benchmarks are
both the testing instrument as well as the training
material.10, 11 The question then cannot be “to what
extent does system Σ possess capability c”, it has
8And one will indeed ﬁnd that papers introducing such
tasks make mention of terms like syntax, semantics, composi-
tionality, quantiﬁers, etc.
9We can also note that with this focus normally comes a
certain top-down approach, where the collected data is not
investigated for how exactly the human participants actually
solved their task. (But see (van Miltenburg, 2019) for a de-
tailed study along those lines, for the task of image descrip-
tion.)
10Not unlike a school that aims to improve its test scores
by preparing its students speciﬁcally for the tests; in that case,
however, this practice would be seen as undermining the value
of the test.
11For a recent paper also discussing the relation between
AI benchmarking and intelligence testing, see (Chollet, 2019).

--- Page 4 ---

to be “to what extent can algorithm A learn c from
dataset D?” — and what does that tell us?
4.1
Single-Task Models
Let’s assume we have deﬁned a task T that we
are sufﬁciently convinced is well represented by
dataset D. We have trained a model M that per-
forms well on this dataset. What have we learned?
We have learned that a learning algorithm of the
type of M can model D. Further, we have learned
that the information to do task T (as exempliﬁed in
D), is contained in D, and M can pick it up.
Under what conditions can we now say that we
have modelled T, rather than just D? If we have
convinced ourselves that D represents T faithfully,
then we might be willing to make this leap, and
with it, claim that we have modelled CT . But we
can get further support by collecting more data D′
that also exempliﬁes T, but perhaps operationalises
it differently. The prediction should be at least that
the learning algorithm can also learn to model D′;
but more signiﬁcantly, we’d also want the model M
learned from D to perform well on D′. Similarly,
if we have another task T ′ of which we think that
it involves similar capabilities, we should expect it
to be amenable to being modelled with a learning
algorithm of similar type to M.
What do we learn from a model M′ (introduc-
ing architectural innovation κ over M) performing
better on T (via D)? We can take this as indication
that κ may be what is responsible for increasing
performance, and hence what is leading to a more
adequate model of CT .
4.2
Multi-Task Models
With the advent of pre-training in NLP (Peters et al.,
2018; Devlin et al., 2018), where a model is trained
on (a typically large amount of) data under a spe-
ciﬁc task-regime (typically language modelling, i.e.
the task of predicting the next word in a running
text) and then becomes part of the model for a
target task, it has become common to test on a col-
lection of tasks (Wang et al., 2019b,a). What do
we learn from such a setup? In our Figure 1, if
we ﬁnd a task on which we can pre-train a model
MP that becomes a part of models M and M′,
and which makes them more powerful than models
that do not have access to the pre-trained model,
then we can infer that whatever MP models is a
shared part of M and M′ as well (and hence in-
volves the hypothesised joint capability C′). This
then provides an instrument to study the tasks: if
the pre-trained model works well on some but not
all, there must be something that those groups have
in common. To make this intelligible, however,
recourse to theoretical terms must again be taken.
(E.g., assuming that these tasks involve the use of
certain types of representation, or certain actions
over representations.)
5
But Are We Making Progress?
Within the logic of this methodology, we are clearly
making enormous progress at two links in the chain
illustrated in Figure 1: For many of the established
tasks, models have been and continue to be pro-
posed that perform better, according to the metrics
deﬁned for the tasks. In addition, for many of the
tasks, better datasets have been collected, avoiding
exploitable biases. Where there is less activity is in
systematically studying the implications of success
at one task for success at others. The presenta-
tion above was largely idealised (or normative): In
reality, there is very little explicitness about the
assumed connection between tasks and capabilities,
and no theory of how (or whether) language com-
petence decomposes into capabilities that could be
learned separately and then be assembled into a
whole, and there is very little explicit knowledge
about the vertical links in the Figure, from one task
/ model to the next.
6
Conclusions
In this short paper, we have discussed the method-
ology of using language tasks to drive research
on models of language competence. We have ar-
gued that the success of this approach hinges on
how well progress on one task can be translated
into progress on other tasks. While some steps
have been taken in this direction, current work
still appears to mostly focus on isolated tasks (or
groups of tasks). Overcoming this, in our opin-
ion, will require more explicit considerations about
how tasks and capabilities are connected, and how
the set of capabilities is structured. For this, a
(re-)connection with the ﬁelds that study the com-
position of language competence, linguistics and
cognitive and developemental psychology, seems
to be advisable. Finally, the stark difference be-
tween how humans can pick up new tasks, based
on an intensional description and a few examples,
and how current models do this (by needing mas-
sive amounts of data), and between how human
language competence develops (from simpler in-

--- Page 5 ---

teractions to more complex ones) and how models
“develop” (from scratch on any task) has to be ac-
counted for, pointing to a future where the real
benchmark might be the developmental trajectory,
and the tasks are only measures, not targets.
References
Stanislaw Antol, Aishwarya Agrawal, Jiasen Lu, Mar-
garet Mitchell, Dhruv Batra, C. Lawrence Zitnick,
and Devi Parikh. 2015.
Vqa: Visual question an-
swering. In International Conference on Computer
Vision (ICCV).
Ron Artstein and Massimo Poesio. 2008. Inter-Coder
Agreement for Computational Linguistics. Compu-
tational Linguistic, 34(4):555–596.
Denny Borsboom. 2005.
Measuring the Mind:
Conceptual Issues in Contemporary Psychometrics.
Cambridge University Press, Cambridge, UK.
Andrew Butterﬁeld, Gerard Ekembe Ngondi, and Anne
Kerr, editors. 2016. A Dictionary of Computer Sci-
ence, 7th edition. Oxford University Press, Oxford,
UK.
Franc¸ois Chollet. 2019.
On the Measure of Intelli-
gence. arXiv e-prints, page arXiv:1911.01547.
Jacob Devlin, Ming-Wei Chang, Kenton Lee, and
Kristina Toutanova. 2018.
BERT: pre-training of
deep bidirectional transformers for language under-
standing. CoRR, abs/1810.04805.
Dheeru Dua and Casey Graff. 2019.
UCI machine
learning repository.
Yash Goyal, Tejas Khot, Douglas Summers-Stay,
Dhruv Batra, and Devi Parikh. 2017. Making the V
in VQA Matter: Elevating the Role of Image Under-
standing in Visual Question Answering. In CVPR
2017.
Allan Jabri, Armand Joulin, and Laurens van der
Maaten. 2016. Revisiting Visual Question Answer-
ing Baselines.
In European Conference on Com-
puter Vision (ECCV).
Fernando
Martinez-Plumed
and
Jos´e
Hernandez-
Orallo. 2018. Dual indicators to analyse ai bench-
marks: Difﬁculty, discrimination, ability and gener-
ality. IEEE Transactions on Games, pages 1–1.
Emiel van Miltenburg. 2019. Pragmatic factors in (au-
tomatic) image description. Ph.D. thesis, Vrije Uni-
versiteit Amsterdam.
Ellie Pavlick and Tom Kwiatkowski. 2019. Inherent
Disagreements in Human Textual Inferences. Trans-
actions of the Association for Computational Lin-
guistics, 7:677–694.
Matthew Peters, Mark Neumann, Mohit Iyyer, Matt
Gardner, Christopher Clark, Kenton Lee, and Luke
Zettlemoyer. 2018. Deep contextualized word rep-
resentations.
In Proceedings of the 2018 Confer-
ence of the North American Chapter of the Associ-
ation for Computational Linguistics: Human Lan-
guage Technologies, Volume 1 (Long Papers), pages
2227–2237, New Orleans, Louisiana. Association
for Computational Linguistics.
Karl Popper. 1934.
Logik der Forschung.
Mohr
Siebeck, T¨ubingen, Germany.
James Pustejovsky and Amber Stubbs. 2013.
Nat-
ural Language Annotation for Machine Learning.
O’Reilly, Sebastopol, CA, USA.
David Schlangen. 2019. Language tasks and language
games: On methodology in current natural language
processing research. CoRR, abs/1908.10747.
Alex Wang,
Yada Pruksachatkun,
Nikita Nangia,
Amanpreet Singh, Julian Michael, Felix Hill, Omer
Levy, and Samuel R. Bowman. 2019a.
Super-
GLUE: A Stickier Benchmark for General-Purpose
Language Understanding Systems. In NeurIPS, July,
pages 1–30.
Alex Wang, Amanpreet Singh, Julian Michael, Felix
Hill, Omer Levy, and Samuel R. Bowman. 2019b.
GLUE: A Multi-Task Benchmark and Analysis Plat-
form for Natural Language Understanding. In ICLR
2019, pages 1–20.
Adina Williams, Nikita Nangia, and Samuel R. Bow-
man. 2018. A Broad-Coverage Challenge Corpus
for Sentence Understanding through Inference. In
Proceedings of the Conference of the North Ameri-
can Chapter of the Association for Computational
Linguistics (NAACL).
```
