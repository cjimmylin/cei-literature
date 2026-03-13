---\ntitle: "2024-Bonagiri-SaGE - PDF Extract"\nsource_pdf: "2024-Bonagiri-SaGE.pdf"\npages: 13\nextracted_at: "2026-02-14T02:17:29.346568"\n---\n\n# PDF Extract: 2024-Bonagiri-SaGE\n\n**Source PDF:** 2024-Bonagiri-SaGE.pdf\n**Total Pages:** 13\n\n---\n\n## Content\n\n```\n--- Page 1 ---\n\nSaGE: Evaluating Moral Consistency in Large Language
Models
Vamshi Krishna Bonagiri1,2, Sreeram Vennam1, Priyanshul Govil1,2
Ponnurangam Kumaraguru1, Manas Gaur2
1International Institute of Information Technology Hyderabad (IIITH)
2University of Maryland Baltimore County (UMBC)
vamshi.b@research.iiit.ac.in
sreeram.vennam@students.iiit.ac.in, priyanshul.govil@research.iiit.ac.in
pk.guru@iiit.ac.in, manas@umbc.edu
Abstract
Despite recent advancements showcasing the impressive capabilities of Large Language Models (LLMs) in
conversational systems, we show that even state-of-the-art LLMs are morally inconsistent in their generations,
questioning their reliability (and trustworthiness in general). Prior works in LLM evaluation focus on developing
ground-truth data to measure accuracy on specific tasks.
However, for moral scenarios that often lack
universally agreed-upon answers, consistency in model responses becomes crucial for their reliability.
To
address this issue, we propose an information-theoretic measure called Semantic Graph Entropy (SaGE),
grounded in the concept of “Rules of Thumb” (RoTs) to measure a model’s moral consistency.
RoTs are
abstract principles learned by a model and can help explain their decision-making strategies effectively. To
this extent, we construct the Moral Consistency Corpus (MCC), containing 50K moral questions, responses
to them by LLMs, and the RoTs that these models followed. Furthermore, to illustrate the generalizability
of SaGE, we use it to investigate LLM consistency on two popular datasets – TruthfulQA and HellaSwag.
Our results reveal that task-accuracy and consistency are independent problems, and there is a dire need to
investigate these issues further. Our Data and Code are publicly available at: https://github.com/vnnm404/SaGE
Keywords: Large Language Models, Evaluation, Trustworthiness, Consistency, Reliability, Morality
1.
Introduction
“Not to care about being consistent in one’s moral
attitudes and feelings...
would undermine one’s
credibility as a moral agent, not to mention as a
trustworthy and responsible person; one’s moral re-
sponses would be unpredictable and one’s character
unreliable”
– Campbell and Kumar (2012)
As Large Language Models (LLMs) continue to
scale in performance, the proliferation of these
AI systems in everyday use is inevitable (OpenAI,
2023; Lee, 2020). However, these systems are under-
utilized due to concerns about their trustworthiness
and reliability (Liu et al., 2023; Hu et al., 2021;
Mayer et al., 1995). Consequently, the field of AI
alignment has emerged to ensure that LLMs are
calibrated to human values, morals, ethics, and so-
cial norms (Gabriel 2020; Ammanabrolu et al. 2022;
Hadfield-Menell et al. 2019).
One of the key factors in ensuring alignment is
morality – principles concerning the distinction be-
tween right and wrong, or good and bad behavior.
Morality is an important factor in human decisions,
and acts as a driving force behind the persuasive-
ness and polarization of human opinions. Since
morals are shaped and maintained through mutual
agreements, it’s essential for AI systems to be de-
Figure 1: An example of GPT-3.5 Turbo providing
inconsistent answers when prompted with seman-
tically equivalent sentences. The responses were
recorded through the OpenAI API via zero-shot
prompting, on September 20th, 2023. The dialogues
shown represent paraphrased concise versions of the
original dialogues.
signed with careful consideration of these values,
ensuring alignment with human moral frameworks
(Gauthier 1987, Hu et al. 2021).
Moral Consistency is the ability to preserve
non-contradictory moral values across different
types of situations, and is often considered the hall-
mark of ethics (University; Arvanitis and Kalliris,
arXiv:2402.13709v2  [cs.CL]  8 Mar 2024

--- Page 2 ---\n\n2020; Marcus, 1980). However, LLMs are known
to yield inconsistent outputs even in semanti-
cally equivalent contexts (see Figure 1) (Jang and
Lukasiewicz, 2023). This inconsistent behavior, if
shown in moral scenarios, could lead LLMs to:
1. Create confusion and uncertainty, hinder-
ing users’ trust (Liu et al., 2023).
2. Corrupt users’ moral beliefs, as shown by
Kr¨ugel et al. (2023).
3. Behave in unexpected ways when deployed
in the real world, leading to ethical and social
risks (Weidinger et al., 2021).
Moral consistency is widely acknowledged in psy-
chology and ethics. However, its importance in the
NLP community is yet to be established. Specifi-
cally, there is a lack of standardized methodologies
and metrics to effectively assess moral consistency
in LLMs, or morality in general (Chang et al., 2023).
Existing research works in evaluating LLM align-
ment examine task-specific accuracies with human-
labeled ground truth data in applications such as
commonsense inference (Zellers et al., 2019), rea-
soning (Clark et al., 2018), multitasking (Ma et al.,
2023), and truthful question-answering (Lin et al.,
2022). However, ground truth data alone may not
be good enough to evaluate LLMs (Gehrmann et al.,
2023), especially on more subjective and compli-
cated problems, such as morality and inconsistency.
Thus, distinguishing between accuracy and chal-
lenges such as consistency becomes vital for crafting
appropriate evaluation methodologies.
To address this research gap, we introduce a
novel framework to measure the moral consistency
of LLMs in semantically similar contexts.1
Our
method encompasses the development of the Moral
Consistency Corpus (MCC), extended from the ex-
isting “Moral Integrity Corpus” (MIC) (Ziems et al.,
2022). Subsequently, we introduce Semantic Graph
Entropy (SaGE), a novel information-theoretic
metric grounded in the concept of Rules of Thumb
(RoTs) to measure moral consistency in an LLM’s
responses. RoTs are basic conceptual units of moral-
ity that a model has learned during its training
stage. Our approach consists of generating seman-
tically equivalent scenarios and employing consis-
tency checks to see if a target LLM follows the
same RoT while responding to these scenarios (see
Figure 2).
Our framework is model-agnostic, does not re-
quire ground truth labels, and provides a reliable
way to measure the consistency of a language model.
We use SaGE to show that even state-of-the-art
(SOTA) LLMs are morally inconsistent, question-
ing their reliability in the real world. Further, we
1Moral consistency is a much broader term; we limit
this work to moral consistency in similar contexts only.
generalize our method to measure consistency in
other popular tasks like commonsense reasoning
and truthful question-answering. Our experiments
reveal that accuracy and consistency are not di-
rectly related, emphasizing the importance of un-
derstanding and improving LLMs in generating
reliable responses. We also show that sampling
methods do not improve consistency, and there is a
need to craft better methods that can guide LLMs
to provide consistent responses. Finally, we discuss
one such method that can potentially improve LLM
consistency.
2.
Related Work
2.1.
Morality in Language Models
Moral decision-making is often grounded in founda-
tional norms – don’t lie, don’t cheat, don’t steal, etc.
(Jin et al., 2022b). Prior works have attempted to
teach such norms to AI models like Delphi (Jiang
et al., 2022). Delphi was trained on a huge corpus of
ethical judgments (Commonsense Norm Bank) and
showed impressive results on its test data. However,
when deployed in the real world, it was found to
be inconsistent, illogical, and offensive (Talat et al.,
2021). To help strengthen the morality in AI mod-
els, Forbes et al. (2020a) introduced the concept of
RoTs – basic conceptual units of social norms and
morality that can guide conversational agents to
behave morally and pro-socially (Ziems et al. 2022,
Kim et al. 2022). Subsequently, Jin et al. (2022a)
proposed the MoralExceptQA challenge to teach
LLMs about the exceptions within moral rules. We,
however, believe that before delving into exceptions,
it’s crucial to ensure that LLMs are even able to
follow the rules consistently.
As LLMs have grown in scale and capability, the
spectrum of potential social risks they present has
also broadened (Weidinger et al., 2021). This has
led to an increasing number of works emphasiz-
ing the evaluation of these models to align with
human morals. Pan et al. (2023) introduced the
MACHIAVELLI benchmark to measure an LLM’s
tendency toward morality instead of maximizing
reward. Kr¨ugel et al. (2023) qualitatively revealed
that ChatGPT is morally inconsistent and is capa-
ble of corrupting users’ moral judgments. Scherrer
et al. (2023) show high levels of LLM inconsistency
in moral scenarios by using them as survey respon-
dents. However, these works require human inter-
vention in curating datasets. Thus, they are limited
by human perception and may not generalize well
in the real world (Talat et al., 2021). Our work
addresses this limitation by introducing an auto-
mated and generalizable approach which does not
require additional human efforts, ensuring broader
applicability.

--- Page 3 ---\n\nFigure 2: An illustration of our pipeline to evaluate moral consistency. Our five-step process includes
(1) Generating quality paraphrases for each question, (2) Generating answers from the target LLM, (3)
Generating RoTs for each Question-Answer pair, (4) Creating a semantic graph from the RoTs, and (5)
Calculating the Semantic Graph Entropy (SaGE).
2.2.
Inconsistency in Language Models
Semantic consistency is the ability to make consis-
tent decisions in semantically equivalent contexts
(Elazar et al., 2021). Mitchell et al. (2022) showed
that neural models’ internal beliefs are inconsistent
across examples. Subsequently, Jang et al. (2022)
expanded on these works by introducing multiple
categories such as negational, symmetric, transi-
tive, and additive consistency. While recent works
have highlighted the improved capabilities of LLMs,
they are still known to generate inconsistent out-
puts to semantically equivalent situations (Jang
and Lukasiewicz, 2023). Similar to our work, these
works attempted to evaluate and benchmark lan-
guage models on consistency. However, they still
rely on creating ground truth datasets.
Fluri et al. (2023) proposed using consistency
checks as a measure to evaluate super-human sce-
narios (forecasting future events, making legal judg-
ments, etc.) with no ground truth. Similarly, since
moral scenarios often do not have answers which
are universally agreed upon, evaluation based on
ground truth becomes difficult, and may seem nor-
mative (Cialdini et al., 1991). Therefore, we pro-
pose a way to evaluate LLMs’ moral consistency in
a descriptive manner without defining ground truth
labels. To the best of our knowledge, our work is a
first in measuring moral consistency in LLMs using
norms (RoTs).
3.
The Moral Consistency Corpus
To understand the level of moral consistency in
LLMs, we develop the Moral Consistency Corpus
(MCC), containing 50K moral questions, depicting
10K unique moral scenarios, and 50K × 11 answers
given by 11 LLMs, along with the RoTs they used
to answer these questions. MCC is constructed by
selectively augmenting 10K questions from MIC2
through paraphrasing and using 11 LLMs (listed in
Table 1) to generate answers for these questions.
Finally, we generate RoTs followed by the LLMs
to answer these questions. We choose MIC in our
experiments due to its collection of moral questions.
However, our approach can be generalized to any
dataset, as shown in section 5.4.
3.1.
Generating Paraphrases and
Responses
As we are quantifying moral consistency in seman-
tically equivalent scenarios, our approach heavily
relies on generating paraphrases. While paraphrase
generation used to be a challenge in NLP (Zhou and
Bhat, 2021), recent works have proven that instruct-
tuned LLMs produce effective paraphrases (Kaneko
2MIC is a corpus containing 38K moral prompt-reply
pairs between humans and chatbots, along with human-
annotated RoTs. We randomly sample 10K of these
data points for our experiments.

--- Page 4 ---\n\nand Okazaki, 2023). Many recent works have used
paraphrasing for tasks such as data augmentation
(Abaskohi et al., 2023), adversarial attacks (Agar-
wal et al., 2023; Morris et al., 2020), and improving
natural language generation evaluation (Tang et al.,
2023).
Inspired by these works, we use an LLM to gener-
ate five high-quality paraphrases for each question
in the selected 10K questions. We used a Vicuna-
13b model 3 (Chiang et al., 2023) for the paraphrase
generation, as our qualitative visual inspection re-
vealed that it produced suitable paraphrases for
our task. We use the following one-shot prompt to
generate paraphrases from the Vicuna model.
Our prompt: paraphrase generation
Instruction: Your task is to generate multi-
ple paraphrased sentences. Do not change the
meaning of the text and be concise.
Sentence: example sentence 1
Paraphrases: example paraphrases
Sentence: <question>
Paraphrases:
To ensure high quality4 (Bandel et al., 2022),
we filter the paraphrases by selecting those that
yielded a ParaScore (Shen et al., 2022) greater than
0.8. ParaScore is a metric that uses both lexical
divergence and semantic similarity to ensure good-
quality evaluation of paraphrases.
Then, we generate answers for each paraphrased
question using 11 different LLMs – OPT (125m,5
1.3b,6 2.7b,7 6.7b,8 and 13b9), LLama 2 (7b-chat-
hf,10 13b-chat-hf11), Falcon (7b-instruct12), Mistral
(7b-instruct-v0.113), GPT-3.5 Turbo, and GPT-4.
We chose these LLMs as they are considered SOTA
due to their performance on popular benchmarks
(Edward Beeching, 2023).
3.2.
Rules of Thumb (RoTs)
Forbes et al. (2020b) and Ziems et al. (2022) de-
fine RoTs as fundamental judgments about right
3https://huggingface.co/lmsys/vicuna-13b-v1.5
4High-quality paraphrases are those which are se-
mantically similar, yet lexically diverse.
5https://huggingface.co/facebook/opt-125m
6https://huggingface.co/facebook/opt-1.3b
7https://huggingface.co/facebook/opt-2.7b
8https://huggingface.co/facebook/opt-6.7b
9https://huggingface.co/facebook/opt-13b
10https://huggingface.co/meta-llama/Llama-2-7b-
chat-hf
11https://huggingface.co/meta-llama/Llama-2-13b-
chat-hf
12https://huggingface.co/tiiuae/falcon-7b
13https://huggingface.co/mistralai/Mistral-7B-
Instruct-v0.1
or wrong behavior. We adapt this definition and
redefine RoTs for the use of moral consistency mea-
surement as abstract guidelines or principles in-
ferred by a model from its training data, aiding
in its judgment of right or wrong behavior. We
propose using RoTs as explanations to represent
better and evaluate a model’s moral judgment. To
this extent, we redefine moral consistency for this
work as the ability to follow equivalent RoTs in
semantically similar scenarios. Prior attempts by
Kim et al. (2022) have shown that it is possible to
generate RoTs by looking at the question-answer
pairs. Inspired by these approaches, we generate
RoTs for every question-answer pair in MCC using
a few-shot approach (Brown et al., 2020). Following
is our prompt template to generate RoTs, and the
few shot examples are taken from MIC.
Our prompt: RoT generation
A Rule of Thumb (RoT) is a fundamental
judgment about right and wrong behavior. An
RoT should explain the basics of good and bad
behavior, should contain a judgment (e.g. “you
should”) and an action (e.g. “give money to the
poor”) and make a general rule but still provide
enough detail such that it is understandable
even out of context.
Instruction: Generate the rule of thumb for
the task question-answer pair: be as concise as
possible.
Question: When is it worth it to fight a losing
battle?
Answer: It is never worth it.
Rule of Thumb: Cowardice saves you from
fights you cannot win.
. . .
Question: <question>
Answer: <answer>
Rule of Thumb:
4.
Our Metric
Given a question q and a generative language model
M, the task of SaGE is to assess M’s consistency
level while answering q. We first generate n para-
phrases of q, represented as X(q) = {x1, ..., xn}.
Then, we generate model responses to each of
these paraphrased questions A(q) = {a1, ..., an},
followed by a set of RoTs obeyed while answering
the respective questions R(q) = {r1, ..., rn} (i.e.,
(xi, ai) →ri). We then use semantic embeddings
to represent the RoTs and construct a semantic
graph for q. Finally, we calculate the graph entropy
of the semantic graph constructed and scale the
metric accordingly.

--- Page 5 ---\n\n4.1.
Preliminary: Graph Entropy
Graph entropy is a measure used to determine
the structural information content of graphs (Ra-
shevsky, 1955).
Graph entropy measures have
been applied in diverse fields such as sociology (Lu
et al. 2008, Butts 2001), chemistry, biology (Mo-
rowitz 1955, Rashevsky 1955), and even linguistics
(Abramov and Lokot, 2011; Goel et al., 2022).
In our work, we aim to quantify the consistency
in a model’s responses to paraphrased questions.
We do so by analyzing the structural and semantic
properties of the responses. We define graph en-
tropy in this section and adapt it to our task in the
later sections.
We start with the definition of Shannon’s entropy
(Shannon, 1948). Given a probability vector p =
(p1, . . . , pn), with 0 ≤pi ≤1 and Pn
i=1 pi = 1. The
Shannon’s entropy of p is defined as:
H(p) = −
n
X
i=1
pi log(pi)
(1)
For a Graph G = (V, E), we consider the vertex
probability defined by Dehmer and Mowshowitz
(2011) as:
p(vi) =
f(vi)
P|V |
j=1 f(vj)
,
(2)
where f(vi) is an arbitrary information functional
of vi. Thus, the graph entropy I(G) is defined as:
I(G) = −
n
X
i=1
p(vi) log p(vi)
= −
n
X
i=1
f(vi)
P|V |
j=1 f(vj)
log
f(vi)
P|V |
j=1 f(vj)
.
(3)
4.2.
Semantic Graphs
To assess the consistency in the RoTs, we first
convert their textual representations {r1, ..., rn} to
their respective semantic embeddings {s1, ..., sn}.
We define a Semantic Graph Gs = (V, E) as a
graph with semantic embeddings with vertices
V
=
{s1, s2, ..., sn}, and the edges as E
=
{d(s1, s2), d(s1, s3), ..., d(s1, sn), ..., d(sn−1, sn)},
where d(si, sj) represents the cosine distance
between two semantic embeddings.
We utilize the approach of generating seman-
tic representations of the input sequences by em-
ploying an SBERT DeBERTa model (Reimers and
Gurevych, 2019; He et al., 2020), fine-tuned on Nat-
ural Language Inference (NLI) datasets (Williams
et al., 2017).
This model is selected due to its
superior performance in creating sentence embed-
dings for comparison, as highlighted by Reimers
and Gurevych (2019).
4.3.
Semantic Graph Entropy (SaGE)
We define SaGE as the graph entropy of our seman-
tic graph Gs. In order to calculate SaGE, we define
the information functional f(vi) for our use case
as:
f(vi) =
n
X
j=1
sim(vi, vj)
(4)
where sim(vi, vj) represents the semantic similarity
(calculated using cosine similarity) between vi and
vj. In information theoretic terms, f(vi) represents
the amount of mutual information stored within
the vertex vi. The underlying assumption is that
semantically similar sequences hold more mutual
information (Prior and Geffet, 2019). Substituting
this in eq. 2, we get:
p(vi) =
Pn
j=1 sim(vi, vj)
Pn
i=1
Pn
j=1 sim(vi, vj)
(5)
Finally, the graph entropy I(Gs) is scaled14 by
λ = Pn
i=1
Pn
j=1 sim(vi, vj)/(n(n −1)), to get:
I(Gs) = λ
n
X
i=1
p(vi) log(p(vi))
(6)
A higher value of the graph entropy would indicate
less consistency, as more randomness is associated
with it. To make a higher value of SaGE indicate
more consistency, we normalize the graph entropy
and define SaGE as:
SaGE(Gs) = 1 −I(Gs)
log n
(7)
5.
Experiments and Analysis
We show consistency as an intrinsic property of
LLMs, independent of their hyperparameters or
performance on popular benchmarks. We also ex-
plore the reliability of SaGE, and if consistency can
be improved using naive methods. We lay out our
investigation by answering the following questions:
1. How morally consistent are current SOTA
LLMs? (Section 5.1)
2. Is SaGE a reliable metric to quantify moral
consistency? (Section 5.2)
3. Can consistency be controlled through sam-
pling methods? (Section 5.3)
4. How does consistency correlate with accuracy
in popular benchmarks? (Section 5.4)
5. Can we improve consistency with RoTs? (Sec-
tion 5.5)
14While semantic graph entropy in itself can capture
the structural properties of the graph, we multiply it
with the average of sentence similarity, to capture the
sentence similarity properties as well.

--- Page 6 ---\n\n5.1.
Results on MCC
For a question q, given n paraphrases X(q) =
{x1, ..., xn}, with generated answers as A(q) =
{a1, ..., an}, Elazar et al. (2021)’s measure of con-
sistency is defined as:
Conslex(q) =
2
n(n −1)
n
X
i,j=1,i̸=j
sim(ai, aj)
Here, sim(x, y) is replaced with lexical similarity
metrics such as BLEU (Papineni et al., 2002) and
ROUGE (Lin, 2004). Consequent works have re-
placed the lexical similarity metrics with seman-
tic similarity metrics (Raj et al., 2022) for more
reliability.
Therefore, we replace sim(x, y) with
BERTScore to incorporate semantic similarity.
To quantify moral consistency in LLMs, we fol-
low our pipeline on a subset of MIC to construct
MCC. Then, we evaluate 11 LLMs on MCC using
SaGE, along with the metrics mentioned above.
Our approach relies on checking if these LLMs are
consistent with their answers, when questions are
paraphrased.
Table 1 shows the LLMs’ average scores on the
MCC dataset. Of the SOTA LLMs we picked, the
maximum observed SaGE score was 0.681, reveal-
ing that LLMs are inconsistent in moral scenarios.
We notice that among the OPT models, there is an
increase in consistency with the number of model
parameters. However, this does not hold perfectly
for the other groups of models, as GPT-3.5 Turbo
shows a higher level of consistency compared to
GPT-4. Since SOTA models do not perform well
on our task, MCC can serve as a benchmark to
assess moral consistency in future LLMs. Through
this experiment, we highlight the issue of moral
consistency in current LLMs, and call for the devel-
opment of better models that are morally aligned
and consistent.
5.2.
Human Evaluations
To assess the reliability of SaGE, we compare it with
the metrics mentioned in section 5.1 with respect
to human annotations. For human annotations, we
qualitatively select 500 data points from MCC that
contain questions which demand the LLM’s moral
opinions.
Measuring consistency with human judgments is
not a trivial task. Therefore, similar to (Gururan-
gan et al., 2018), we asked the annotators to look
at pairwise answers from the dataset, and deter-
mine if they are semantically equivalent. To ensure
the consistency of our annotations, we employed
a three-rater system where ‘Y’ denoted agreement
(semantic equivalence), ‘N’ indicated disagreement,
and ‘NA’ represented uncertainty. We observed
a Krippendorff’s α score of 0.868, signifying high
reliability among annotators.
We construct a mapping of: ‘Y’ →1 and ‘N’
→0 and calculate the entropy of this distribution,
by converting it into a probability distribution for
each question. Then, we measure its correlation
with respect to SaGE and the other metrics cho-
sen. Results displayed in Table 2 show that SaGE
best correlates with human judgments for our task.
Interestingly, the usage of RoTs show a significant
increase in correlations, implying the relevance of
RoTs in assessing moral consistency. The low corre-
lations of BLEU and ROUGE indicate that lexical
similarity is not a good measurement, reinforcing
prior research (Kan´e et al., 2019). Meanwhile, se-
mantic similarity measures such as BERTScore cap-
ture semantic information, showing an increase in
correlations. However, SaGE accounts for struc-
tural properties as well as semantic similarity in
the data, making it a better metric to assess con-
sistency.
5.3.
Consistency and Temperature
Temperature-based sampling is a common approach
to sampling-based generation. It is used to alter
the probability distribution of a model’s output,
with temperature as a parameter (Holtzman et al.,
2019). During the decoding step, the probability
mass function (PMF) of the model’s vocabulary
(with temperature T) is estimated as:
Pr(vk) =
elk/T
P
i eli/T
(8)
where vk is the k-th vocabulary token and lk the
corresponding logit. This would imply that when
T = 0, the PMF becomes a Kronecker delta func-
tion, and the response becomes completely deter-
ministic. Similarly, a larger T value would make
the PMF more evenly distributed, increasing the
randomness in generations.
However, moral consistency is an intrinsic prop-
erty of LLMs, whereas sampling methods represent
extrinsic methods to generate text after an LLM
processes the input. To show that moral consis-
tency is not a function of temperature, we perform
our consistency experiment on different tempera-
ture values. This is done in two settings: (1) The
model is prompted with the same question 5 times,
and (2) with 5 different paraphrases. We use the
same 500 quality questions used in the previous
section for this experiment.
Figure 3 summarizes the results. While consis-
tency decreases in the case of same questions, we
see almost no change in consistency in the case of
paraphrasing. This reveals that consistency in the
real world (where paraphrased inputs are common)
is not a function of temperature and is an intrinsic
property of LLMs. This shows that sampling-based
extrinsic methods are not a fix for consistency, and

--- Page 7 ---\n\nModel
BLEU
ROUGE
BERTScore
SaGE
Ans
RoT
Ans
RoT
Ans
RoT
Ans
RoT
opt-125m
0.011
0.012
0.138
0.127
0.355
0.352
0.243
0.252
opt-1.3b
0.009
0.010
0.133
0.119
0.369
0.362
0.263
0.268
opt-2.7b
0.008
0.011
0.135
0.127
0.382
0.378
0.277
0.284
opt-6.7b
0.007
0.012
0.130
0.129
0.385
0.382
0.282
0.290
opt-13b
0.008
0.012
0.139
0.135
0.412
0.408
0.312
0.318
Mistral-7B-Instruct-v0.1
0.016
0.015
0.151
0.150
0.499
0.493
0.405
0.407
falcon-7b-instruct
0.027
0.016
0.194
0.159
0.648
0.621
0.584
0.563
Llama-2-7b-chat-hf
0.073
0.020
0.296
0.170
0.564
0.546
0.362
0.452
Llama-2-13b-chat-hf
0.084
0.020
0.261
0.176
0.660
0.635
0.595
0.575
GPT-3.5 Turbo †
0.056
0.015
0.217
0.151
0.613
0.529
0.681
0.478
GPT-4 †
0.055
0.0172
0.246
0.166
0.568
0.486
0.641
0.438
Table 1:
Average consistency scores of 11 LLMs on MCC. The ‘Ans’ column represents the scores
calculated on LLM answers, and the ‘RoT’ column represents scores calculated on the generated RoTs.
Results show that none of the state-of-the-art LLMs cross a SaGE score of 0.681, indicating the inability
of LLMs to be morally consistent. Some of the best-performing models in different categories are indicated
in bold. † : Results on a subset of MCC (10%) due to API limitations.
0.0
0.1
0.5
0.7
0.9
1.0
1.5
0
0.5
1
Temperature
Score
ROUGE(w/o)
SaGE(w/o)
ROUGE(w)
SaGE(w)
Figure 3: Representation of the variation in ROUGE and SaGE scores across different temperatures. The
dashed line depicts consistency trends without paraphrasing, and the solid line depicts consistency trends
with paraphrases. The figure reveals that consistency is not dependent on temperature.
Metric
Answers
RoTs
BLEU
0.391
0.412
ROUGE
0.459
0.476
BERTScore
0.522
0.527
SaGE
0.561
0.592
Table 2: Pearson correlations of SaGE with the
average of human annotations. SaGE shows signif-
icant improvement over the previous metrics. On
top of that, the results show that using RoTs en-
hances the reliability of such metrics even further.
special care needs to be taken to train consistent
models.
5.4.
Consistency and Accuracy
In this section, we evaluate LLM consistency in
tasks similar to moral reasoning with established
benchmarks to understand if consistency can be
studied through such datasets.
We employ our
Model
TruthfulQA
HellaSwag
SaGE
Accuracy
SaGE
Accuracy
opt-125m
0.258
0.357
0.164
0.313
opt-1.3b
0.258
0.260
0.162
0.537
opt-2.7b
0.282
0.374
0.151
0.614
opt-6.7b
0.285
0.351
0.156
0.687
opt-13b
0.315
0.341
0.146
0.712
Mistral-7B
0.421
0.567
0.529
0.756
falcon-7b
0.577
0.343
0.289
0.781
Llama-2-7b
0.452
0.388
0.563
0.786
Llama-2-13b
0.559
0.374
0.520
0.819
Table 3: SaGE scores and accuracies on TruthfulQA
and HellaSwag. No correlations are observed be-
tween the two (see Figure 4).
pipeline on two popular benchmarks:
1. TruthfulQA (Lin et al., 2022): A benchmark
to measure whether a language model is truth-
ful in generating answers to questions. It con-
tains 817 questions that some humans would
falsely answer due to false beliefs or miscon-
ceptions.

--- Page 8 ---\n\n0.3 0.4 0.5 0.6
0.3
0.4
0.5
SaGETruthfulQA
AccuracyTruthfulQA
0.2
0.4
0.6
0.4
0.6
0.8
SaGEHellaSwag
AccuracyHellaSwag
Figure 4: Scatter plot between SaGE scores and
dataset’s task accuracies. We observe no significant
correlation, implying that consistency and accuracy
are two different problems.
2. HellaSwag (Zellers et al., 2019): A common-
sense inference challenge dataset. HellaSwag
contains over 39K contexts and 4 possible ex-
tensions each of the contexts, of which only
one adheres to commonsense.15
The major distinguishing factor of MCC from
these datasets is that MCC does not have ground
truth, while HellaSwag and TruthfulQA have
ground truth to evaluate accuracies against. This
presents us with an opportunity to see if a model
that is accurate on a task, is also consistent on the
same task.
Table 3 and Figure 4 summarize the results. The
results reveal that task accuracy and consistency are
two different problems. It is important to note that
a model that is truthful or can reason, should also
be able to do so consistently. However, we show that
SOTA LLMs fail to perform these tasks consistently,
revealing a major pitfall in the evaluation strategies
being employed in current systems (i.e., through
ground truth data).
5.5.
Improving consistency
In order to explore possible strategies of improving
consistency, we employ a naive method to see if
LLMs even have the ability to behave consistently.
We do this by prompting the LLM to follow specific
RoTs while answering questions. These RoTs are
human annotated, and are taken from the MIC
corpus. Specifically, we use the prompt below to
make LLMs follow specific RoTs while answering
questions.
Our prompt: RoT-based answer gen-
eration
Instruction: Answer the following question.
Keep in mind this rule of thumb, <RoT>
Question: <question>
Answer:
15We sample a subset of HellaSwag (1K data points)
for our experiments due to computing constraints.
Table 4 summarizes the results of the experiment.
We notice that there is a significant improvement
(around 10%) when we ask the LLM to follow an
RoT while answering a question. This indicates
that LLMs can be taught to follow rules consistently.
This methodology can be employed by knowledge-
based systems to pick certain rules during inference,
allowing the models to produce more consistent
results. Our results indicate that there is a scope
for improvement in LLM consistency, and SaGE
can reliably measure such improvements.
Model
BLEU
ROUGE
BERT
Score
SaGE
GPT-3.5
0.015
0.151
0.529
0.438
GPT-3.5 with
RoT
prompt-
ing
0.018
0.169
0.565
0.548
Table 4:
Average consistency scores before and
after including RoTs to be followed in the prompt.
The experiment reveals a clear increase in consis-
tency levels after including RoT in the prompt.
The experiment is carried out on 500 handpicked
samples from MCC.
6.
Conclusion
In this work, we introduce a novel framework to
evaluate the moral consistency of LLMs. We in-
troduce SaGE, a new information-theoretic metric,
grounded in the concept of RoTs to measure moral
consistency in LLMs. Our approach mainly con-
sists of generating high quality paraphrases of moral
questions, and employing consistency checks to see
if a target LLM follows the same RoT while answer-
ing these questions. We also introduce the MCC to
measure the moral consistency in LLMs. We eval-
uate SOTA LLMs on our dataset, and show that
they are morally inconsistent in their generations.
Further, we show that inconsistency is an intrin-
sic property of LLMs, and cannot be solved with
extrinsic methods such as temperature sampling.
By employing SaGE on other popular tasks, we
show that task based accuracy and consistency are
independent problems, indicating an urgent need
to investigate this problem further.
Finally, we
show that LLMs can be taught to be consistent by
simply making them follow RoTs, hinting a scope
of improvement in this domain. We invite future
works to develop more consistent models and evalu-
ate them on our dataset, or use our methodology to
evaluate consistency on their own task, ultimately
leading to LLMs that can produce morally consis-
tent and ethically sound responses.

--- Page 9 ---\n\n7.
Ethical Considerations
Precautions taken during dataset construc-
tion. Firstly, as MCC is a direct extension of MIC
(Ziems et al., 2022), we ensure that it adheres to
the same moral principles as MIC, and followed
similar ethical assumptions while constructing the
dataset. While we understand that the generation
of rules and norms can be seen as normative, we
emphasize that our work only uses RoTs to eval-
uate if a model is consistently following the same
RoT, making it a completely descriptive approach.
Therefore, we do not judge if any RoT is right or
wrong, but simply use it to evaluate the consistency
of a model’s judgement.
Risks from data release. MCC is an evalua-
tion dataset specifically for research purposes only,
it is advised against using this dataset for training
models, as it may encompass rules that contravene
the ethical principles of certain communities. It
is very critical to note that the paraphrases and
RoTs generated are not fully monitored by the au-
thors or any humans, so it may contain unreliable,
ethically questionable, or upsetting generations by
LLMs. Therefore, to ensure awareness among the
data users, we explicitly provide these details and
warnings to users who seek to use our data. Futher-
more, we emphasize that the RoTs generated are
not intended to be universally binding, nor do they
reflect a humans moral opinions.
They do not
constitute a comprehensive ethical framework but
rather serve as a means to elucidate pre-existing
biases in models.
Risks in methodology. For our human anno-
tation experiments, we ensure that the annotators
are fully aware of the potential for harmful or sen-
sitive data, and allowed them to opt out at any
point. Furthermore, we were constantly monitor-
ing them to ensure a smooth annotation process,
which did not make them uncomfortable in any
form whatsoever.
In the section focused on improvements, we
prompt the model on which rules to follow. While
this can be considered a normative approach, we
only perform this experiment to show that it is
possible to increase consistency in current LLMs,
and SaGE can measure it. We do not consider this
an effective method to build morally aligned agents,
but only a naive method to improve consistency.
Our work focuses solely on improving moral con-
sistency, as we consider the moral alignment with
humans a subsequent problem.
We understand that moral consistency is a
broader term in ethics, and the moral consistency of
humans itself is often debated about (Paton, 1971;
Marcus, 1980). However, we tackle a subproblem of
it which is semantic consistency in moral scenarios,
and argue that these inconsistencies would cause
issues to the users and LLMs trust.
8.
Limitations
Our experiments are limited to only 11 LLMs and 5
paraphrases due to GPU and compute constraints.
However, we make sure to include most of the SOTA
architectures in our experiments, along with mod-
els with different number of parameters (from the
OPT family) to analyse consistency across such cat-
egories. Our methods also depend on many NLP
tools such as SBERT for sentence embeddings, and
Vicuna for paraphrase and RoT generation. There-
fore, some of their limitations will carry over to
our work. Despite that, we chose these tools due
to their proven capabilities in the respective tasks,
and make additional checks such as human annota-
tions, and evaluation with existing metrics to ensure
the tools are performing the required tasks effec-
tively. Specifically, we understand that tasks such
as RoT generation can also provide inconsistent
results, since we are using LLMs for them. While
we acknowledge that this may cause minor incon-
sistencies in our experiments, we rely on previous
works that show effective generation of RoTs (Kim
et al., 2022; Ziems et al., 2022), and current LLMs
capabilities in text generation (Khalatbari et al.,
2023) to ensure reliable generation of RoTs. We
also show that the RoTs we generated are reliable,
through our human annotations.
9.
Acknowledgements
This work was done during the first (Vamshi Kr-
ishna Bonagiri) and third (Priyanshul Govil) au-
thor’s internship at KAI2 Lab of UMBC.
We would like to thank Abhinav Menon, An-
mol Goel, Daniel Paleka, Gaurav Singh, Mukund
Choudhary, Pratyaksh Gautam, Shashwat Singh,
and Vanshpreet Singh Kohli for their valuable feed-
back.
10.
References
Amirhossein Abaskohi, Sascha Rothe, and Yadol-
lah Yaghoobzadeh. 2023. Lm-cppf: Paraphrasing-
guided data augmentation for contrastive prompt-
based few-shot fine-tuning.
arXiv preprint
arXiv:2305.18169.
Olga Abramov and Tatiana Lokot. 2011. Typol-
ogy by means of language networks: Applying
information theoretic measures to morphological
derivation networks. Towards an Information
Theory of Complex Networks: Statistical Methods
and Applications, pages 321–346.

--- Page 10 ---\n\nAnmol Agarwal, Shrey Gupta, Vamshi Bonagiri,
Manas Gaur, Joseph Reagle, and Ponnurangam
Kumaraguru. 2023. Towards effective paraphras-
ing for information disguise. In European Con-
ference on Information Retrieval, pages 331–340.
Springer.
Prithviraj Ammanabrolu, Liwei Jiang, Maarten
Sap, Hannaneh Hajishirzi, and Yejin Choi. 2022.
Aligning to social norms and values in interactive
narratives. In Proceedings of the 2022 Conference
of the North American Chapter of the Association
for Computational Linguistics: Human Language
Technologies, pages 5994–6017.
Alexios Arvanitis and Konstantinos Kalliris. 2020.
Consistency and Moral Integrity:
A Self-
Determination Theory Perspective. Journal of
Moral Education, 49(3):1–14. Publisher: Rout-
ledge.
Elron Bandel, Ranit Aharonov, Michal Shmueli-
Scheuer, Ilya Shnayderman, Noam Slonim, and
Liat Ein Dor. 2022. Quality controlled paraphrase
generation. In Proceedings of the 60th Annual
Meeting of the Association for Computational
Linguistics (Volume 1: Long Papers), pages 596–
609.
Tom Brown, Benjamin Mann, Nick Ryder, Melanie
Subbiah, Jared D Kaplan, Prafulla Dhariwal,
Arvind Neelakantan, Pranav Shyam, Girish Sas-
try, Amanda Askell, et al. 2020. Language models
are few-shot learners. Advances in neural infor-
mation processing systems, 33:1877–1901.
Carter T Butts. 2001. The complexity of social net-
works: theoretical and empirical findings. Social
Networks, 23(1):31–72.
Richmond Campbell and Victor Kumar. 2012.
Moral
reasoning
on
the
ground.
Ethics,
122(2):273–312.
Yupeng Chang, Xu Wang, Jindong Wang, Yuan
Wu, Kaijie Zhu, Hao Chen, Linyi Yang, Xiaoyuan
Yi, Cunxiang Wang, Yidong Wang, et al. 2023.
A survey on evaluation of large language models.
arXiv preprint arXiv:2307.03109.
Wei-Lin Chiang, Zhuohan Li, Zi Lin, Ying Sheng,
Zhanghao Wu, Hao Zhang, Lianmin Zheng,
Siyuan Zhuang, Yonghao Zhuang, Joseph E. Gon-
zalez, Ion Stoica, and Eric P. Xing. 2023. Vicuna:
An open-source chatbot impressing gpt-4 with
90%* chatgpt quality.
Robert B Cialdini, Carl A Kallgren, and Ray-
mond R Reno. 1991. A focus theory of normative
conduct: A theoretical refinement and reevalu-
ation of the role of norms in human behavior.
In Advances in experimental social psychology,
volume 24, pages 201–234. Elsevier.
Peter Clark, Isaac Cowhey, Oren Etzioni, Tushar
Khot, Ashish Sabharwal, Carissa Schoenick, and
Oyvind Tafjord. 2018. Think you have solved
question answering? try arc, the ai2 reasoning
challenge. arXiv preprint arXiv:1803.05457.
Matthias Dehmer and Abbe Mowshowitz. 2011. A
history of graph entropy measures. Information
Sciences, 181(1):57–78.
Nathan
Habib
Sheon
Han
Nathan
Lambert
Nazneen
Rajani
Omar
Sanseviero
Lewis
Tunstall
Thomas
Wolf
Edward
Beeching,
Cl´ementine Fourrier. 2023.
Open llm leader-
board.
https://huggingface.co/spaces/
HuggingFaceH4/open_llm_leaderboard.
Yanai Elazar, Nora Kassner, Shauli Ravfogel,
Abhilasha Ravichander, Eduard Hovy, Hinrich
Sch¨utze, and Yoav Goldberg. 2021. Measuring
and Improving Consistency in Pretrained Lan-
guage Models. Transactions of the Association
for Computational Linguistics, 9:1012–1031.
Lukas Fluri, Daniel Paleka, and Florian Tram`er.
2023. Evaluating Superhuman Models with Con-
sistency Checks. ArXiv:2306.09983 [cs, stat].
Maxwell Forbes, Jena D. Hwang, Vered Shwartz,
Maarten Sap, and Yejin Choi. 2020a.
Social
Chemistry 101: Learning to Reason about Social
and Moral Norms. In Proceedings of the 2020
Conference on Empirical Methods in Natural Lan-
guage Processing (EMNLP), pages 653–670, On-
line. Association for Computational Linguistics.
Maxwell Forbes, Jena D. Hwang, Vered Shwartz,
Maarten Sap, and Yejin Choi. 2020b.
Social
Chemistry 101: Learning to Reason about Social
and Moral Norms. In Proceedings of the 2020
Conference on Empirical Methods in Natural Lan-
guage Processing (EMNLP), pages 653–670, On-
line. Association for Computational Linguistics.
Iason Gabriel. 2020. Artificial intelligence, values,
and alignment. Minds and machines, 30(3):411–
437.
David Gauthier. 1987. Overview of a Theory. In
David Gauthier, editor, Morals by Agreement,
page 0. Oxford University Press.
Sebastian
Gehrmann,
Elizabeth
Clark,
and
Thibault Sellam. 2023. Repairing the cracked
foundation: A survey of obstacles in evaluation
practices for generated text. Journal of Artificial
Intelligence Research, 77:103–166.

--- Page 11 ---\n\nAnmol Goel, Charu Sharma, and Ponnurangam
Kumaraguru. 2022. An unsupervised, geometric
and syntax-aware quantification of polysemy. In
Proceedings of the 2022 Conference on Empirical
Methods in Natural Language Processing, pages
10565–10574.
Suchin Gururangan, Swabha Swayamdipta, Omer
Levy, Roy Schwartz, Samuel Bowman, and
Noah A Smith. 2018. Annotation artifacts in
natural language inference data. In Proceedings
of the 2018 Conference of the North American
Chapter of the Association for Computational
Linguistics: Human Language Technologies, Vol-
ume 2 (Short Papers), pages 107–112.
Dylan Hadfield-Menell, McKane Andrus, and
Gillian Hadfield. 2019. Legible normativity for ai
alignment: The value of silly rules. In Proceed-
ings of the 2019 AAAI/ACM Conference on AI,
Ethics, and Society, pages 115–121.
Pengcheng He,
Xiaodong Liu,
Jianfeng Gao,
and Weizhu Chen. 2020.
Deberta: Decoding-
enhanced bert with disentangled attention. In
International Conference on Learning Represen-
tations.
Ari Holtzman, Jan Buys, Li Du, Maxwell Forbes,
and Yejin Choi. 2019. The curious case of neural
text degeneration. In International Conference
on Learning Representations.
Peng Hu, Yaobin Lu, and Yeming (Yale) Gong.
2021. Dual humanness and trust in conversational
AI: A person-centered approach. Computers in
Human Behavior, 119:106727.
Myeongjun Jang, Deuk Sin Kwon, and Thomas
Lukasiewicz. 2022. Becel: Benchmark for con-
sistency evaluation of language models. In Pro-
ceedings of the 29th International Conference on
Computational Linguistics, pages 3680–3696.
Myeongjun
Jang
and
Thomas
Lukasiewicz.
2023.
Consistency Analysis of ChatGPT.
ArXiv:2303.06273 [cs].
Liwei Jiang, Jena D. Hwang, Chandra Bhagavat-
ula, Ronan Le Bras, Jenny Liang, Jesse Dodge,
Keisuke Sakaguchi, Maxwell Forbes, Jon Bor-
chardt, Saadia Gabriel, Yulia Tsvetkov, Oren
Etzioni, Maarten Sap, Regina Rini, and Yejin
Choi. 2022. Can Machines Learn Morality? The
Delphi Experiment. ArXiv:2110.07574 [cs].
Zhijing Jin, Sydney Levine, Fernando Gonzalez,
Ojasv Kamal, Maarten Sap, Mrinmaya Sachan,
Rada Mihalcea, Josh Tenenbaum, and Bernhard
Sch¨olkopf. 2022a. When to Make Exceptions: Ex-
ploring Language Models as Accounts of Human
Moral Judgment. ArXiv:2210.01478 [cs].
Zhijing Jin, Sydney Levine, Fernando Gonza-
lez Adauto, Ojasv Kamal, Maarten Sap, Mrin-
maya Sachan, Rada Mihalcea, Josh Tenenbaum,
and Bernhard Sch¨olkopf. 2022b. When to make
exceptions: Exploring language models as ac-
counts of human moral judgment. Advances in
neural information processing systems, 35:28458–
28473.
Hassan Kan´e, Yusuf Kocyigit, Pelkins Ajanoh, Ali
Abdalla, and Mohamed Coulibali. 2019. Towards
neural similarity evaluator. In Workshop on Doc-
ument Intelligence at NeurIPS 2019.
Masahiro Kaneko and Naoaki Okazaki. 2023. Re-
ducing sequence length by predicting edit opera-
tions with large language models. arXiv preprint
arXiv:2305.11862.
Leila Khalatbari, Yejin Bang, Dan Su, Willy Chung,
Saeed Ghadimi, Hossein Sameti, and Pascale
Fung. 2023. Learn What NOT to Learn: Towards
Generative Safety in Chatbots. Publisher: arXiv
Version Number: 2.
Hyunwoo Kim, Youngjae Yu, Liwei Jiang, Xim-
ing Lu, Daniel Khashabi, Gunhee Kim, Yejin
Choi, and Maarten Sap. 2022. ProsocialDialog:
A Prosocial Backbone for Conversational Agents.
ArXiv:2205.12688 [cs].
Sebastian
Kr¨ugel,
Andreas
Ostermaier,
and
Matthias Uhl. 2023.
ChatGPT’s inconsistent
moral advice influences users’ judgment. Sci Rep,
13(1):4569. Number: 1 Publisher: Nature Pub-
lishing Group.
Raymond ST Lee. 2020. Artificial intelligence in
daily life. Springer.
Chin-Yew Lin. 2004. Rouge: A package for auto-
matic evaluation of summaries. In Text summa-
rization branches out, pages 74–81.
Stephanie Lin, Jacob Hilton, and Owain Evans.
2022. TruthfulQA: Measuring How Models Mimic
Human Falsehoods. ArXiv:2109.07958 [cs].
Yang Liu, Yuanshun Yao, Jean-Francois Ton, Xi-
aoying Zhang, Ruocheng Guo, Hao Cheng, Yegor
Klochkov, Muhammad Faaiz Taufiq, and Hang Li.
2023. Trustworthy LLMs: a Survey and Guideline
for Evaluating Large Language Models’ Align-
ment. ArXiv:2308.05374 [cs].
Jia-Liang Lu, Fabrice Valois, Mischa Dohler, and
Dominique Barthel. 2008. Quantifying organiza-
tion by means of entropy. IEEE communications
letters, 12(3):185–187.
Xiao Ma,
Swaroop Mishra,
Ahmad Beirami,
Alex Beutel, and Jilin Chen. 2023.
Let’s do

--- Page 12 ---\n\na thought experiment:
Using counterfactuals
to improve moral reasoning.
arXiv preprint
arXiv:2306.14308.
Ruth Barcan Marcus. 1980.
Moral dilemmas
and consistency.
The Journal of Philosophy,
77(3):121–136.
Roger C. Mayer, James H. Davis, and F. David
Schoorman. 1995. An Integrative Model of Orga-
nizational Trust. The Academy of Management
Review, 20(3):709–734. Publisher: Academy of
Management.
Eric Mitchell, Joseph Noh, Siyan Li, Will Arm-
strong, Ananth Agarwal, Patrick Liu, Chelsea
Finn, and Christopher Manning. 2022. Enhanc-
ing Self-Consistency and Performance of Pre-
Trained Language Models through Natural Lan-
guage Inference. In Proceedings of the 2022 Con-
ference on Empirical Methods in Natural Lan-
guage Processing, pages 1754–1768, Abu Dhabi,
United Arab Emirates. Association for Compu-
tational Linguistics.
Harold J Morowitz. 1955.
Some order-disorder
considerations in living systems. The bulletin of
mathematical biophysics, 17:81–86.
John Morris, Eli Lifland, Jin Yong Yoo, Jake
Grigsby, Di Jin, and Yanjun Qi. 2020. Textat-
tack: A framework for adversarial attacks, data
augmentation, and adversarial training in nlp. In
Proceedings of the 2020 Conference on Empirical
Methods in Natural Language Processing: System
Demonstrations, pages 119–126.
OpenAI. 2023. Gpt-4 technical report.
Alexander Pan, Jun Shern Chan, Andy Zou,
Nathaniel Li, Steven Basart, Thomas Woodside,
Jonathan Ng, Hanlin Zhang, Scott Emmons, and
Dan Hendrycks. 2023. Do the Rewards Justify the
Means? Measuring Trade-Offs Between Rewards
and Ethical Behavior in the MACHIAVELLI
Benchmark. ArXiv:2304.03279 [cs].
Kishore Papineni, Salim Roukos, Todd Ward, and
Wei-Jing Zhu. 2002.
Bleu: a method for au-
tomatic evaluation of machine translation. In
Proceedings of the 40th annual meeting of the
Association for Computational Linguistics, pages
311–318.
Herbert James Paton. 1971. The categorical impera-
tive: A study in Kant’s moral philosophy, volume
1023. University of Pennsylvania Press.
Anat Prior and Maayan Geffet. 2019. Mutual infor-
mation and semantic similarity as predictors of
word association strength: Modulation by associ-
ation type and semantic relation. In Proceedings
of EuroCogSci, pages 265–270.
Harsh Raj, Domenic Rosati, and Subhabrata Ma-
jumdar. 2022.
Measuring reliability of large
language models through semantic consistency.
arXiv preprint arXiv:2211.05853.
Nicolas Rashevsky. 1955.
Life, information the-
ory, and topology. The bulletin of mathematical
biophysics, 17:229–235.
Nils Reimers and Iryna Gurevych. 2019. Sentence-
BERT: Sentence Embeddings using Siamese
BERT-Networks. ArXiv:1908.10084 [cs].
Nino Scherrer, Claudia Shi, Amir Feder, and
David M. Blei. 2023. Evaluating the Moral Beliefs
Encoded in LLMs.
Claude Elwood Shannon. 1948. A mathematical
theory of communication. The Bell system tech-
nical journal, 27(3):379–423.
Lingfeng Shen, Lemao Liu, Haiyun Jiang, and
Shuming Shi. 2022. On the evaluation metrics
for paraphrase generation. In Proceedings of the
2022 Conference on Empirical Methods in Natu-
ral Language Processing, pages 3178–3190.
Zeerak Talat, Hagen Blix, Josef Valvoda, M. I.
Ganesh, Ryan Cotterell, and Adina Williams.
2021. A Word on Machine Ethics: A Response
to Jiang et al. (2021). ArXiv.
Tianyi Tang, Hongyuan Lu, Yuchen Eleanor Jiang,
Haoyang Huang, Dongdong Zhang, Wayne Xin
Zhao, and Furu Wei. 2023. Not all metrics are
guilty: Improving nlg evaluation with llm para-
phrasing. arXiv preprint arXiv:2305.15067.
Santa Clara University. Consistency and Ethics.
Laura Weidinger, John Mellor, Maribeth Rauh,
Conor Griffin, Jonathan Uesato, Po-Sen Huang,
Myra Cheng, Mia Glaese, Borja Balle, Atoosa
Kasirzadeh, Zac Kenton, Sasha Brown, Will
Hawkins, Tom Stepleton, Courtney Biles, Abeba
Birhane, Julia Haas, Laura Rimell, Lisa Anne
Hendricks, William Isaac, Sean Legassick, Ge-
offrey Irving, and Iason Gabriel. 2021. Ethical
and social risks of harm from Language Models.
ArXiv:2112.04359 [cs].
Adina Williams, Nikita Nangia, and Samuel R Bow-
man. 2017. A broad-coverage challenge corpus for
sentence understanding through inference. arXiv
preprint arXiv:1704.05426.
Rowan Zellers, Ari Holtzman, Yonatan Bisk, Ali
Farhadi, and Yejin Choi. 2019. Hellaswag: Can
a machine really finish your sentence? In Pro-
ceedings of the 57th Annual Meeting of the As-
sociation for Computational Linguistics, pages
4791–4800.

--- Page 13 ---\n\nJianing Zhou and Suma Bhat. 2021. Paraphrase
generation: A survey of the state of the art. In
Proceedings of the 2021 conference on empirical
methods in natural language processing, pages
5075–5086.
Caleb Ziems, Jane A. Yu, Yi-Chia Wang, Alon
Halevy, and Diyi Yang. 2022. The Moral Integrity
Corpus: A Benchmark for Ethical Dialogue Sys-
tems. ArXiv:2204.03021 [cs].
\n```\n