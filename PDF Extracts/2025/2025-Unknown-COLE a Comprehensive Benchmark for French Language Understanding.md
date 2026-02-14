---
title: "2025-preprint)-COLE a Comprehensive Benchmark for French Language Understanding - PDF Extract"
source_pdf: "2025-preprint)-COLE a Comprehensive Benchmark for French Language Understanding.pdf"
pages: 19
extracted_at: "2026-02-13T13:14:05.238029"
---

# PDF Extract: 2025-preprint)-COLE a Comprehensive Benchmark for French Language Understanding

**Source PDF:** 2025-preprint)-COLE a Comprehensive Benchmark for French Language Understanding.pdf
**Total Pages:** 19

---

## Content

```
--- Page 1 ---

COLE: a Comprehensive Benchmark for French Language Understanding
Evaluation
David Beauchemin†, Yan Tremblay†, Mohamed Amine Youssef† and Richard Khoury
Group for Research in Artificial Intelligence of Laval University (GRAIL)
Université Laval, Québec, Canada
david.beauchemin@ift.ulaval.ca, yan.tremblay.6@ulaval.ca,
mohamed-amine.youssef.1@ulaval.ca, richard.khoury@ift.ulaval.ca
Abstract
To address the need for a more comprehensive
evaluation of French Natural Language Under-
standing (NLU), we introduce COLE, a new
benchmark composed of 23 diverse task cover-
ing a broad range of NLU capabilities, includ-
ing sentiment analysis, paraphrase detection,
grammatical judgment, and reasoning, with a
particular focus on linguistic phenomena rele-
vant to the French language. We benchmark
95 large language models (LLM), providing an
extensive analysis of the current state of French
NLU. Our results highlight a significant perfor-
mance gap between closed- and open-weights
models and identify key challenging frontiers
for current LLMs, such as zero-shot extractive
question-answering (QA), fine-grained word
sense disambiguation, and understanding of re-
gional language variations. We release COLE
as a public resource to foster further progress
in French language modelling.
1
Introduction
The field of Natural Language Processing (NLP)
has seen significant progress in recent years, pri-
marily driven by the development of LLMs. These
models, trained on vast amounts of text data, have
achieved state-of-the-art results on a wide range of
tasks. Examples can be found in healthcare, where
they assist in clinical diagnosis (Thirunavukarasu
et al., 2023), and in insurance, where they explain
insurance contracts (Beauchemin et al., 2024). To
accurately gauge their capabilities and limitations,
the community relies on comprehensive bench-
marks. In the English-speaking world, corpora
of tasks like the General Language Understanding
Evaluation benchmark (GLUE) (Wang et al., 2018),
a suite of nine tasks designed to assess a model’s
ability to understand natural language (NL), have
become the standard for evaluating model compe-
tency across a diverse set of NLU tasks. Follow-
ing the success of GLUE, similar initiatives have
emerged for other languages, such as the bench-
mark FLUE in French (Le et al., 2020) or CLUE in
Chinese (Xu et al., 2020). These benchmarks have
been instrumental in advancing NLP research in
various languages by providing language-specific
evaluation sets, which make it possible to quantify
the development of language-specific resources,
like the French LM FlauBERT (Le et al., 2020).
Despite the significant contributions of FLUE, it
caused a gap in the evaluation of NLU in French.
Indeed, the benchmark lacks task diversity. It does
not include typical NLU tasks, such as textual en-
tailment (TE), idiom comprehension, QA, linguis-
tic phenomena, paraphrase detection and sentiment
analysis. Thus, there remains a need for a broader
set of NLU tasks to evaluate the competency of
LMs.
Moreover, it should address the unique
linguistic challenges endemic to the French lan-
guage, such as its rich morphology (Gross, 1984),
grammatical gender (Rowlett, 2007), and complex
syntactic structures (Abeillé and Godard, 2002),
thereby providing a more rigorous and nuanced
measure of a model’s competency.
To address this gap, we introduce the COrpus
for Langue understanding Evaluation (COLE), a
French NLU benchmark of 23 tasks. COLE is de-
signed to provide a comprehensive and challenging
evaluation suite for LLMs, with a focus on a wide
variety of tasks, including linguistic phenomena
and reasoning types that are particularly relevant to
the French language.
release version Our main contributions are as
follows:
1. We propose a comprehensive evaluation suite
for French NLU, carefully curated to cover a
wide range of tasks and corpus size1.
2. We benchmark and analyze 95 LLMs on COLE.
This paper is organized as follows: Section 2
presents the related work, then Section 3 describes
our tasks. Section 4 details the experimentation
1https://huggingface.co/datasets/graalul/COLE-public
arXiv:2510.05046v2  [cs.CL]  7 Oct 2025

--- Page 2 ---

setup and Section 5 discusses the results. Finally,
Section 6 concludes the paper and our future work.
2
Related Work
Historically, evaluation of LMs has been conducted
using metrics or benchmark corpora (Chang et al.,
2023). The first approach relies either on task-
agnostic metrics, such as perplexity (Jelinek et al.,
1977), which measures the quality of the proba-
bility distribution of words generated by a model,
or on task-specific metrics, like the BLEU score
that evaluates a model’s performance for machine
translation (Papineni et al., 2002) or MeaningBERT
that evaluates meaning preservation in text simpli-
fication (Beauchemin et al., 2023). However, these
metrics do not provide a comprehensive assessment
of a model’s general NLU competencies. Task-
specific metrics are narrowly-focused by definition,
and task-agnostic metrics often fail to capture cru-
cial aspects of language (Bowman and Dahl, 2021).
The second approach relies on the use of large
benchmark corpora designed for NLU or other
downstream tasks. For example, the GLUE bench-
mark is designed to assess a model’s NLU perfor-
mance on nine distinct tasks. These tasks can be
grouped into three main categories. The first in-
volves single-sentence understanding, and includes
a sentences’ grammatical acceptability (CoLA)
task (Warstadt et al., 2019) and a binary sentiment
classification task (SST) (Socher et al., 2013). The
second category focuses on similarity and para-
phrase detection, It features the Microsoft Research
Paraphrase Corpus (Dolan and Brockett, 2005) to
identify if two sentences are semantically equiva-
lent, the Quora Question Pairs (Wang et al., 2018)
to detect duplicate questions, and the Semantic Tex-
tual Similarity (STS) task (Cer et al., 2017), which
involves predicting a similarity score between 1 and
5. The final category, Natural Language Inference
(NLI), which is a cornerstone of NLP evaluation
efforts and a fundamental task for NLU. NLI, also
known as recognizing TE, is the task of determin-
ing whether a “hypothesis” is true (entailment), un-
determined (neutral), or false (contradiction) given
a “premise”. This task is particularly challenging
as it requires a deep understanding of semantic re-
lationships, contextual nuances, and reasoning. A
model that performs well on NLI typically demon-
strates a sophisticated grasp of language that goes
beyond surface-level pattern matching, making it a
crucial component for many downstream applica-
tions such as summarization (Bowman et al., 2015).
In GLUE, this category of tasks comprises four
distinct challenges: the Multi-Genre NLI (MNLI)
task (Williams et al., 2018b), a large-scale task
with both in-domain and cross-domain test sets;
the Question NLI task (Rajpurkar et al., 2016), as
a binary classification task; the Recognizing TE
(RTE) task (Dagan et al., 2005), a binary NLI task;
and the Winograd NLI task (Levesque et al., 2012),
a coreference resolution NLI task.
Following this paradigm, the FLUE benchmark
(Le et al., 2020) aggregates six tasks to assess LM
competency on French, which can also be grouped
into three categories. The first is text classification,
represented by the Cross-Lingual Sentiment (CLS)
task, which evaluates sentiment classification on
product reviews (Prettenhofer and Stein, 2010).
The second category focuses on sentence-pair un-
derstanding, and features a paraphrasing task us-
ing the PAWS-X corpus (Yang et al., 2019) to
identify semantic equivalence, and a cross-lingual
NLI (XNLI) task to determine the logical relation-
ship between a premise and a hypothesis (Conneau
et al., 2018). Finally, the benchmark has a category
to probe linguistic and semantic knowledge with
a dependency parsing task, designed to analyze
grammatical structure (Abeillé et al., 2003; Seddah
et al., 2013), and two Word Sense Disambiguation
(WSD) tasks that require identifying the correct
meaning of an ambiguous noun or verb in context
(Segonne et al., 2019).
Similarly, the CLUE benchmark (Xu et al., 2020)
provides a suite of ten tasks designed for Man-
darin Chinese. It includes two text classification
tasks: TNEWS for short news articles and IFLY-
TEK for longer app descriptions (Xu et al., 2020).
For sentence-pair understanding, it features the Ant
Financial Question Matching Corpus (Xu et al.,
2020), which requires identifying semantically
equivalent questions, and the Chinese Multi-Genre
NLI Task (Xu et al., 2020). It also emphasizes read-
ing comprehension, with two distinct extractive QA
datasets: CMRC2018 (Cui et al., 2019) and DRCD
(Shao et al., 2018). Finally, CLUE probes more
complex and specialized reasoning through unique
tasks: the Winograd Schema Challenge (WSC) for
commonsense pronoun resolution (Xu et al., 2020),
the Chinese idiom dataset for cloze test idiom un-
derstanding (Zheng et al., 2019), the C3 dataset
for multi-choice cloze tests requiring causal reason-
ing (Sun et al., 2020), and the Chinese scientific

--- Page 3 ---

literature task for abstract-keyword relevance.
3
COLE Benchmark
In this section, we present the 23 tasks that com-
pose COLE in Section 3.1, divided into three cate-
gories: single-sentence, similarity and paraphras-
ing, and inference. Table 1 presents a summary of
all our tasks, including instance type, metric, and
corpus size. We will then present the evaluation
metric and our composite score in Section 3.2.
3.1
Tasks
3.1.1
Single-Sentence Tasks
1. Allociné (Blard, 2020) is a task that focuses on
sentiment analysis using movie reviews scraped
from the Allociné website. Each instance is
a single sentence expressing a user-generated
opinion. The model must classify the sentiment
as negative (0) or positive (1). This task evalu-
ates the ability of LLMs to understand sentiment
in informal language.
2. MMS-Fr (Łukasz Augustyniak et al., 2023) is a
sentiment analysis task using the French subset
of the Massive Multilingual Sentiment (MMS)
corpus. Each instance is a single text entry, and
the model must classify its sentiment into one
of three categories: negative (0), neutral (1),
or positive (2). This task evaluates an LLM’s
ability to discern sentiment across the various
domains and text sources included in the origi-
nal collection.
3. QFrCoLA (Beauchemin and Khoury, 2025) is
a grammatical acceptability classification task
for Quebec-French. Each instance is labelled as
unacceptable (0) or acceptable (1). The model
must classify whether the sentence is grammat-
ically acceptable or not. This task assesses the
grammar competency of an LLM.
3.1.2
Similarity and Paraphrase Tasks
1. DACCORD (Skandalis et al., 2024) is a para-
phrase detection task between sentence pairs.
Each instance consists of two sentences, and the
model must determine whether they convey the
same meaning (0) or contradict each other (1).
The dataset contains sentence pairs manually
curated to reflect NL use and covers a variety
of topics, including political discourse. This
task assesses an LLM’s ability to comprehend
paraphrasing across a wide range of topics.
2. FQuAD (d’Hoffschmidt et al., 2020) is a French
extractive QA task built from Wikipedia articles.
Given a context paragraph and a question in
French, the model must extract a contiguous
span of text from the paragraph that answers the
question. The dataset is designed to evaluate
the ability of models to understand and retrieve
factual information in French.
3. Fr-BoolQ (Faysse, 2022) is a binary QA task
translated into French from the original BoolQ
dataset (Clark et al., 2019). Each instance con-
sists of a short context and a yes/no question.
The model must determine whether the context
supports the answer to the question. The ques-
tions are naturally occurring and not guaranteed
to be answerable, making the task challenging.
The goal is to predict “yes” (1) if the context
entails the answer, and “no” (0) otherwise.
4. PAWS-X (Yang et al., 2019) is a paraphrase de-
tection task designed to evaluate models’ ability
to detect whether two sentences in French con-
vey the same meaning despite having different
surface forms. Each instance presents a pair of
sentences that are often lexically similar but se-
mantically distinct. This task assesses an LLM’s
competency in understanding semantics.
5. PIAF (Keraron et al., 2020) is a French ex-
tractive QA task developed from government
and public-domain documents. Given a context
passage and a question in French, the model
must extract the precise span of text that an-
swers the question. PIAF is designed to evaluate
models in realistic information access settings,
with questions sourced from real user needs and
verified by human annotators. It complements
FQuAD by covering a broader range of topics
relevant to public services.
6. QFrCoRE and QFrCoRT (Beauchemin et al.,
2025a) are, respectively, an expression and a
regional terms definition matching task. Each
example consists of a local Quebec idiom or
word and a list of ten potential definitions for
the instance. The model must determine the ap-
propriate definition from the candidate list. This
task assesses an LLM’s capacity to comprehend
local expressions or regional terms.
7. STS22 (Agirre et al., 2012) is an STS task that
evaluates the degree of semantic equivalence
between pairs of French sentences. Each input
consists of two sentences, and the model must
assign an integer-valued similarity score ranging
from 1 (completely unrelated) to 4 (identical
meaning). This task evaluates an LLM’s ability

--- Page 4 ---

Task Name
Task Type
Instance Type
Metric
Train
Dev
Test
Allociné
Sentiment Analysis
Sentence
Accuracy
160,000
20,000
20,000
DACCORD
Paraphrase Detection
Sentence Pair
Accuracy
–
–
1,034
FQuAD
Extractive QA
Context and Question
EM/F1
–
100
400
Fr-BoolQ
Boolean QA
Context and Question
Accuracy
–
–
178
FraCaS
NLI
Sentence Pair
Accuracy
–
–
346
GQNLI-Fr
NLI
Sentence Pair
Accuracy
243
27
30
LingNLI-Fr
NLI
Sentence Pair
Accuracy
29,985
–
4,893
MMS
Sentiment Analysis
Sentence
Accuracy
132,696
14,745
63,190
MNLI-9/11-Fr
NLI
Sentence Pair
Accuracy
–
–
2,000
MultiBLiMP-Fr
Grammatical Acceptability
Sentence Pair
Accuracy
160
18
77
PAWS-X
Paraphrase Detection
Sentence Pair
Accuracy
49,401
2,000
2,000
PIAF
Extractive QA
Context and Question
EM/F1
3,105
346
384
QFrBLiMP
Grammatical Acceptability
Sentence Pair
Accuracy
1,108
124
529
QFrCoLA
Grammatical Acceptability
Sentence
Accuracy
15,846
1,761
7,546
QFrCoRE
Definition Matching
List of Sentences
Accuracy
–
–
4,633
QFrCoRT
Definition Matching
List of Sentences
Accuracy
–
–
201
RTE3-Fr
NLI
Sentence Pair
Accuracy
–
800
800
SICK-Fr
NLI
Sentence Pair
Accuracy
4,439
495
4,906
STS22
STS
Sentence Pair
Accuracy
101
–
72
Wino-X-LM
Pronoun Resolution
Sentence
Accuracy
–
–
2,793
Wino-X-MT
Pronoun Resolution
Sentence and Translation
Accuracy
–
–
2,988
WSD-Fr
WSD
Sentence
EM
269,821
–
3,121
XNLI-Fr
NLI
Sentence Pair
Accuracy
393,000
2,490
5,010
Table 1: COLE’s 23 tasks summary with instance types, evaluation metrics, and sizes per split.
to understand semantic equivalences.
3.1.3
Inference Tasks
1. FraCaS (Richard et al., 2024) is an NLI task.
The dataset is designed to evaluate a model’s se-
mantic reasoning capabilities across a broad and
structured range of linguistic phenomena, such
as quantifiers, plurality, anaphora, and ellipsis.
2. GQNLI-Fr (Skandalis et al., 2024) is an
NLI task that uses an automatically-generated
French translation of the English GQNLI dataset
(Cui et al., 2022). It focuses specifically on gen-
eralized quantifiers (e.g. some, all, none, few)
and tests LLMs’ ability to reason over these
constructs.
3. LingNLI-Fr (Skandalis et al., 2024) is an
NLI task that uses an automatically-generated
French translation of the English LingNLI
dataset (Parrish et al., 2021).
4. MNLI-9/11-Fr (Williams et al., 2018a) is an
NLI task based on a French-translated subset
of the MultiNLI dataset, focusing on sentence
pairs on the topic of 9/11. This task assesses
an LLM’s ability to reason about hypothesis
understanding in NL.
5. MultiBLiMP-Fr (Jumelet et al., 2025) is a
grammatical judgment task utilizing the French
subset of the Multilingual Benchmark of Lin-
guistic Minimal Pairs (MultiBLiMP). Each in-
stance consists of a minimal pair of sentences:
one grammatically correct and one incorrect,
differing by a single, targeted linguistic fea-
ture.
The model is required to identify the
grammatically-acceptable sentence from the
pair. This task evaluates the model’s knowledge
of six linguistic phenomena, including syntax,
morphology, and agreement.
6. QFrBLiMP (Beauchemin et al., 2025b) is a
grammatical judgment task for Quebec French.
The model chooses which of two sentences is
grammatically correct. This task assesses the
LLM’s grammatical competency across 20 lin-
guistic phenomena.
7. RTE3-Fr (Skandalis et al., 2024) is an NLI
task based on a French translation of the RTE3
dataset (Giampiccolo et al., 2007). It is designed
to test fine-grained reasoning over short texts.
8. SICK-Fr (Lajavaness, 2023) is an NLI task de-
rived from the French version of SICK dataset
(Bentivogli et al., 2016). This dataset tests the
LLM over a broad range of linguistic phenom-
ena, including negation, and paraphrasing.
9. Wino-X-LM (Emelin and Sennrich, 2021) is a
pronoun resolution task in the form of coref-
erence resolution.
Each example presents a
French sentence containing an ambiguous pro-

--- Page 5 ---

noun and two possible antecedents. The model
must select the correct referent based on con-
text, thereby evaluating its ability to resolve
gender and number agreement in pronominal
references.
10. Wino-X-MT (Emelin and Sennrich, 2021) is
a natural pronoun resolution task. Given two
French translations of an original English sen-
tence, each differing only in the gender of a
pronoun, the model must choose the translation
that correctly resolves the referent according
to the context. It tests the model’s sensitivity
to grammatical and semantic alignment across
languages.
11. WSD-Fr (Le et al., 2020) is a WSD task from
the FLUE benchmark that evaluates a model’s
ability to identify the correct meaning of an am-
biguous verb in a given context. Each instance
consists of a sentence, and the model must select
the verb/noun that is ambiguous.
12. XNLI-Fr (Conneau et al., 2018) is an NLI task
based on the French subset of the XNLI cor-
pus, which extends the MultiNLI dataset to 15
languages (Williams et al., 2018a). This task as-
sesses LM’s ability to reason about hypothesis
understanding in NL.
3.2
Evaluation Metrics
3.2.1
Task Evaluations
To evaluate competency, we utilize task-specific
evaluation metrics that are aligned with the original
protocol. All three metrics are in the [0, 1] range.
Accuracy measures the proportion of correct pre-
dictions over the total number of instances.
Exact Match (EM) (Wang et al., 2018) evaluates
whether the predicted answer exactly matches the
reference answer. It is a strict metric where any
semantic mismatch results in a zero score.
F1 Score is a measure that assesses the token-level
overlap between predicted and reference spans. In
contrast to EM, it allows partial credit for seman-
tic mismatches. A prediction that overlaps signifi-
cantly with the answer still receives a high score,
even if it is not an exact match.
3.2.2
Composite Score
To evaluate the overall model performance across
the diverse tasks in COLE, we compute a com-
posite score (CS) following a methodology similar
to that of GLUE. This score is calculated as the
unweighted mean of per-task scores, where each
task contributes equally, regardless of its size or
type. For tasks reporting multiple main metrics
(e.g. FQUaD), we first average these metrics to
obtain a single task score. Finally, we multiply the
weighted mean by 100 to obtain a normalized rat-
ing in the range of [0, 100], so the final composite
score can be expressed as a percentage. This pro-
vides a single and easily-interpretable value to com-
pare models’ general NLU capabilities in French.
4
Experiments
4.1
Evaluation Settings
We evaluate a diverse set of French LLMs using
a zero-shot evaluation setup. Each task is framed
as an NL prompt that describes it, and the model
produces an appropriate output based solely on its
pretrained capabilities. All LLMs are evaluated on
the same shared test set to ensure fair comparison.
Depending on the nature of the task, models either
select a response from a predefined set of labels
or generate an answer. Evaluation is conducted
automatically using task-specific metrics.
4.2
Models
4.2.1
Baseline Models
We use a Random selection algorithm as our base-
line. For our classification tasks, it randomly se-
lects one of the potential candidates as the answer.
For example, in a binary classification such as Fr-
BoolQ, it would select either 0 or 1, while for NLI
tasks, such as FraCaS, it selects either 0, 1, or 2. For
the text extraction tasks, namely, FQuAD, PIAF
and WSD-Fr, it randomly selects a word from the
whitespace-split sentence. For example, given the
sentence “I love apples.”, it would whitespace-split
it to [“I”, “love”, “apples”], then select randomly a
word from that set as the answer.We use the seed
42 to facilitate the reproducibility of our results.
4.2.2
LLM
To ensure a thorough and representative analysis of
the current LM landscape, we selected 95 to cover
four aspects of LLM specifications:
1. A Mix of Access Paradigms: We include both
closed- and open-weights LLMs.
2. Variety in Size: The selected models span a
large range of parameter counts, from smaller
models (under 1 billion parameters) to the
largest closed-weights LLMs available as of
mid-2025 (around 100 billion parameters).
3. Variety in Capability: We intentionally in-
cluded models marketed as having advanced

--- Page 6 ---

“reasoning” capabilities (Γ) to assess if this spe-
cialization translates to better performance.
4. Model Specialization: We include models opti-
mized for French (Υ), to test whether this leads
to better performance.
To select the LMs, we leverage two leaderboards:
the Text Arena and the Open LLM leaderboards.
We present our selected models in Appendix B, and
our hardware and budget in Appendix C.
5
Results and Discussion
In this section, we present and analyze the perfor-
mance of the 95 benchmarked LLMs on COLE’s
23 tasks. We present our CS results in Figure 1 and
our complete results are detailed in Appendix D.
We structure our discussion around overall perfor-
mance trends, the impact of model characteristics
such as size and specialization, and a closer look at
performance on specific task categories.
5.1
Overall Performance Analysis
Our
evaluation
reveals
a
wide
perfor-
mance
spectrum,
with
the
CS
ranging
from 28.38% (SmolLM2-135M) to 70.12%
(GPT-5-mini-2025-08-07).
A clear trend
emerges from the leaderboard: closed-weights
LLMs dominate the top ranks.
Indeed, the
top 23 highest-scoring models are all closed-
weights
LLMs,
while
the
best-performing
open-weight model, Qwen3-max, achieves a CS
of 49.14%, 10% less than the next-best-performing
closed-weights model and 20% less than the
best-performing closed-weights model. One might
assume that this is due to the closed-weight models
being larger than open-weight models, since we
were limited in the size of open-weights models we
could run on our local hardware (see Appendix C)
while the closed-weight models were run through
API calls.
However, even the “mini” versions
of leading closed-weights models substantially
outperform larger open-weights models. Moreover,
there is no substantial performance difference
between regular and “mini” versions of closed-
weight models.
For example, the performance
decline from “Grok-3” to “Grok-3-mini” is less
than one percent, and the “mini” version of
“GPT-5” actually outperforms its larger version.
This suggests that the vast and high-quality
proprietary training datasets, data quality and
extensive post-training alignment procedures of
closed-weights LLMs are the determining factors,
rather than raw parameter count.
The good performance of smaller closed-weights
LLMs compared to their larger counterparts may
also be due to the knowledge distillation process
(Hinton, 2014). Indeed, the “mini” or “flash” ver-
sion of an LLM is typically a distilled model of
a larger LLM (Gou et al., 2021). The massive
“teacher” model (i.e. GPT-5) is used to train the
smaller “student” model (i.e. GPT-5-mini). The
student learns to replicate the teacher’s correct out-
puts and reasoning patterns, essentially inheriting
the most important knowledge in a much more com-
pact form. This process hyper-focuses the mini LM
on core language understanding and instruction-
following skills (Sanh, 2019; Ouyang et al., 2022).
The larger LM, in contrast, retains a wider, more
general set of capabilities that may not be relevant
to the benchmark tasks (Liang et al., 2022).
5.2
The Impact of Model Specialization
We analyze two types of specialization: models
optimized for French (Υ) and for reasoning (Γ).
French-specialized
models
show
com-
petitive
but
mixed
results.
For
instance,
Chocolatine-2-14B-it-v2.0.3
stands
out as the strongest open-weights models with
a CS of 45.05. Its strong performance on gram-
matical judgment tasks, such as MultiBLiMP-Fr
(94.81%), suggests a superior grasp of French
linguistic structure.
However, this does not
uniformly translate to semantic and reasoning
tasks, where general-purpose LLMs surpass it.
While language-specific pre-training is effective
for capturing syntactic and grammatical nuances, it
may not be sufficient to bridge the gap in broader
NLU capabilities.
Reasoning
models
generally
perform
well on inference-heavy tasks.
LLMs like
Claude-opus-4 achieve high scores on NLI
tasks such as LingNLI-Fr and SICK-Fr. How-
ever, this result is not consistent. Performance on
FraCaS, a task designed to probe deep semantic
and logical phenomena, remains challenging
even for top-tier reasoning models. In fact, the
best result in this task (66.27%) was achieved by
GPT-4o-mini-2024-07-18, a non-reasoning
model. This highlights that while current reasoning
models are adept at pattern-matching forms of
inference, they still struggle with more complex,
structured logical reasoning.

--- Page 7 ---

5.3
Performance Across Task Categories
5.3.1
Areas of Strength
Semantic Understanding.
Models generally ex-
cel at tasks requiring coarse-grained semantic un-
derstanding. For example, on sentiment analysis
(Allociné) and paraphrase detection (DACCORD),
top models consistently achieve accuracy scores
above 95%. Similarly, many NLI tasks, such as
XNLI-Fr, are handled effectively by the leading
models, which score well above 70%. These results
suggest that high-level sentence and sentence-pair
understanding is a well-developed capability.
Grammatical
Judgment.
Beyond
semantic
tasks, the LLMs demonstrate a strong competency
in French grammatical structure. It is most evident
in the MultiBLiMP-Fr task, where many leading
models achieve near-perfect results, with several
scoring a perfect 100%. This high level of perfor-
mance indicates that the syntactic rules and formal
structures of the French language have been ro-
bustly learned. However, this corpus is composed
of online text; thus, performance may better reflect
proficiency in recognizing common online linguis-
tic patterns rather than a comprehensive grasp of
formal grammatical rules.
5.3.2
Challenging Frontiers
Extractive QA.
Performance in FQuAD and
PIAF is low, especially for the EM metric. A
large number of LLMs, including top-tier ones
like Claude-opus-4, achieve a 0% EM score.
While their F1 scores are sometimes higher, the
inability to extract verbatim text suggests a strong
tendency to rephrase or generate answers rather
than strictly follow the extraction instruction. It
highlights a fundamental challenge in adhering to
instruction for zero-shot QA.
Regional LU.
The regional tasks QFrCoRE and
QFrCoRT, which focused on defining Quebec-
French expressions and terms, represent a major
blind spot. Most open-weights LLMs score near
the random baseline of 9.1%, indicating a lack of
regional and cultural linguistic knowledge. The
performance of closed-weights LLMs, such as
Claude-opus-4, which scores an exceptional
93.46% on QFrCoRE and 97.66% on QFrCoRT,
is a significant outlier and demonstrates that cap-
turing such knowledge is possible, though not yet
widespread. This significant gap between closed-
and open-weights LLMs suggests that mastering
deep cultural and dialectical nuance is not an emer-
gent property of model architecture alone, but
rather a direct consequence of the breadth and di-
versity of the training data. The proprietary cor-
pora used by top commercial labs likely contain
a far richer concentration of regional web content,
literature, and media from Québec than is avail-
able in standard open-source datasets. The excep-
tional performance of these few models, therefore,
demonstrates that capturing such specific linguistic
knowledge is possible.
Word Sense Disambiguation.
This task was also
challenging, with the vast majority of models fail-
ing to produce correct outputs, resulting in scores
near 0%. It suggests that while models have a broad
contextual understanding, their ability to perform
fine-grained lexical disambiguation in a zero-shot
manner is severely limited.
6
Conclusion and Future Works
In this paper, we introduce COLE, a comprehensive
benchmark for French NLU comprising 23 tasks.
Our goal was to address a critical gap in the French
NLP ecosystem by providing a more challenging
and wide-ranging benchmark for LLMs than pre-
viously available. By benchmarking 95 LLMs, we
assess the current landscape of NLU capabilities
in French. Our findings reveal a performance gap
between closed and open-weights models, with the
former consistently achieving superior results. This
advantage is particularly pronounced in tasks re-
quiring deep understanding of French. While mod-
els demonstrate strong capabilities in core semantic
and grammatical tasks, our benchmark successfully
highlights several challenging frontiers for future
research, including zero-shot extractive QA and
understanding regional linguistic variations.
For future work, we plan to expand COLE to in-
clude tasks that cover additional NLU phenomena,
such as multi-hop reasoning and dialogue under-
standing. We also aim to develop a non-public test
set to provide a more robust measure of generaliza-
tion, mitigating the potential for data contamina-
tion. Our hope is that COLE will serve as a valu-
able resource for the community, driving the de-
velopment of more capable and nuanced language
models for the French language.

--- Page 8 ---

LLM
CS
Acc.
(%) (▼)
LLM
CS
Acc.
(%) (▼)
GPT-5-mini-2025-08-07 (Γ)
70.12
DeepSeek-R1-Distill-Qwen-14B (Γ)
37.77
o3-mini-2025-01-31 (Γ)
68.98
Llama-3.2-1B (Γ)
37.62
GPT-4.1-mini-2025-04-14
67.68
Mixtral-8x7B-v0.1
37.04
Claude-opus-4-20250514 (Γ)
67.13
Lucie-7B-it-human-data (Υ)
35.41
Claude-sonnet-4-20250514 (Γ)
65.76
OLMo-2-1124-7B-it
35.20
GPT-4o-mini-2024-07-18
65.72
Qwen2.5-1.5B
34.88
Gemini-2.5-pro (Γ)
65.43
Granite-3.3-8b-it
34.80
DeepSeek-chat
65.20
Qwen2.5-0.5B
34.38
o1-mini-2024-09-12 (Γ)
64.44
Phi-3.5-mini-it
34.28
GPT-4.1-2025-04-14
64.38
Gemma-2-2b (Γ)
34.22
o1-2024-12-17 (Γ)
64.36
OLMo-2-0425-1B-it
34.19
o3-2025-04-16 (Γ)
64.15
Gemma-2-27b (Γ)
34.19
GPT-5-2025-08-07 (Γ)
63.61
OLMo-2-1124-13B-it
34.12
GPT-4o-2024-08-06
63.04
Chocolatine-14B-it-DPO-v1.3 (Υ)
33.95
Grok-3-latest (Γ)
62.34
Gemma-2-9b (Γ)
33.86
Grok-4-0709
62.31
SmolLM2-1.7B-it
33.86
Gemini-2.5-flash
62.21
Gemma-2-2b-it (Γ)
33.85
DeepSeek-reasoner (Γ)
62.20
OLMo-2-1124-7B
33.77
Grok-3-mini-latest (Γ)
62.01
SmolLM2-1.7B
33.77
GPT-oss-120b (Γ)
61.97
Mixtral-8x7B-it-v0.1
33.77
Grok-3-fast-latest (Γ)
61.95
DeepSeek-R1-Distill-Qwen-7B (Γ)
33.34
Grok-3-mini-fast-latest (Γ)
61.57
Llama-3.2-3B (Γ)
33.26
Mistral-large-latest (Γ)
60.70
Apertus-8B-it-2509
33.20
Pixtral-large-latest
60.48
Meta-Llama-3.1-8B (Γ)
33.12
Qwen-max
49.14
OLMo-2-0325-32B
33.05
Qwen3-14B
45.17
OLMo-2-0425-1B
32.84
Chocolatine-2-14B-it-v2.0.3 (Υ)
45.05
Gemma-2-27b-it (Γ)
32.81
QwQ-32B (Γ)
44.94
Apertus-8B-2509
32.48
DeepSeek-R1-Distill-Qwen-32B (Γ)
44.92
Qwen2.5-1.5B-it
32.32
Qwen3-14B-Base
44.49
Qwen2.5-3B-it
32.25
French-Alpaca-Llama3-8B-it-v1.0 (ΓΥ)
44.42
Llama-3.2-1B-it (Γ)
32.15
Qwen2.5-14B-it
44.01
Qwen2.5-3B
32.08
S1.1-32B (Γ)
42.53
OLMo-2-1124-13B
31.61
Phi-4
42.16
DeepSeek-R1-Distill-Llama-8B (Γ)
31.51
Granite-3.2-8b-it
41.33
RandomBaselineModel
31.22
Qwen2.5-32B
41.19
Qwen2.5-0.5B-it
30.74
Qwen2.5-7B-it
40.19
Aya-23-8b
30.71
Meta-Llama-3.1-8B-it (Γ)
40.13
Gemma-2-9b-it (Γ)
30.34
Deepthink-Reasoning-14B (Γ)
40.07
CroissantLLMBase (Υ)
30.21
Deepthink-Reasoning-7B (Γ)
39.96
SmolLM2-135M-it
29.84
Qwen2.5-14B
39.79
SmolLM2-360M
29.83
Qwen2.5-7B
39.78
GPT-oss-20b (Γ)
29.72
Reka-flash-3 (Γ)
38.77
Lucie-7B-it-v1.1 (Υ)
29.18
Qwen2.5-32B-it
38.55
SmolLM2-360M-it
29.10
Granite-3.3-8b-base
38.42
DeepSeek-R1-0528-Qwen3-8B
29.06
Llama-3.2-3B-it (Γ)
38.27
OLMo-2-0325-32B-it
28.45
Aya-expanse-8b
37.87
SmolLM2-135M
28.38
Lucie-7B (Υ)
37.84
Figure 1: Composite score performance of all 95 LLMs. Scores are reported as percentages (%) and are ranked in
descending order (▼).

--- Page 9 ---

Limitations
While we believe COLE is a significant contribu-
tion to the evaluation of French NLU, we acknowl-
edge several limitations that offer avenues for fu-
ture research.
Data Contamination
A primary limitation of
our benchmark is the potential for data contamina-
tion. All datasets included in COLE are publicly
available. Given that LLMs are trained on vast
web scrapes, it is highly probable that their train-
ing data included portions of the training, valida-
tion, and even test sets of these datasets. Conse-
quently, our zero-shot evaluation may not purely
measure a model’s generalization capabilities but
could also reflect memorization. This is a pervasive
challenge in modern LLM evaluation, and holistic
benchmarks now emphasize the need to actively
track and mitigate such contamination (Liang et al.,
2022; Jiang et al., 2024).
Mix of French Varieties
COLE intentionally
incorporates datasets from different varieties of
French, notably including several from Québec,
namely, QFrCoLA, QFrBLiMP, QFrCoRE, QFr-
CoRT, alongside datasets primarily based on
French from France. While this diversity reflects
the richness of the language, our composite score
does not distinguish between them.
It is well-
documented that NLP models can exhibit perfor-
mance disparities across dialects, and an aggre-
gated score can obscure these nuances (Blodgett
et al., 2016). Future work could involve creating
dialect-specific sub-scores to provide a more gran-
ular analysis.
Reliance on Machine-Translated Datasets
Sev-
eral of our inference tasks, such as GQNLI-Fr,
XNLI-Fr, and RTE3-Fr, are based on English
datasets that have been machine-translated into
French.
While these provide valuable data for
cross-lingual comparison, they may contain arti-
facts or “translationese” that do not reflect the full
complexity and naturalness of native French. Such
reliance on translated text for evaluation can be
a shortcut that fails to capture the complete chal-
lenges of a language, a known issue in cross-lingual
transfer methodologies (Artetxe et al., 2020).
Evaluation Scope
Our experimental setup is
exclusively focused on a zero-shot evaluation
paradigm. This approach is valuable for assessing
the out-of-the-box capabilities of pretrained mod-
els. However, it does not evaluate other important
aspects of model performance, such as their abil-
ity to learn in-context (few-shot learning) or their
adaptability through fine-tuning. A complete pic-
ture of a model’s utility requires evaluation across
different adaptation strategies, not just a single
point of assessment (Liang et al., 2022).
Composite Score Granularity
The COLE com-
posite score is an unweighted arithmetic mean of
the individual task scores. This straightforward ap-
proach ensures simplicity and interpretability but
treats all tasks as equally important. It does not ac-
count for differences in task difficulty, dataset size,
or the specific linguistic phenomena being tested.
Over-reliance on a single aggregate score can be
misleading and may fail to highlight the specific
strengths and weaknesses of different models, a
known pitfall of current benchmarking practices
(Bowman and Dahl, 2021).
Ethical Considerations
The development and release of the COLE bench-
mark, like any tool for advancing language model
capabilities, carries ethical implications that war-
rant careful consideration.
Intended Use and Dual Nature of LLMs
Our
primary goal in creating COLE is to provide a ro-
bust tool for the French NLP community to mea-
sure progress and gain a deeper understanding of
model capabilities. However, we acknowledge that
advancements spurred by such benchmarks con-
tribute to the development of more powerful LLMs.
These models have a dual-use nature: while they
can be used for beneficial applications, they can
also be exploited for malicious purposes, such as
generating convincing disinformation, automating
social manipulation, or creating harmful content at
scale (Bender et al., 2021).
Bias and Representational Harms
The datasets
comprising COLE are sourced from public do-
mains, including web reviews (Allociné) and
Wikipedia articles (FQuAD). These sources are
known to contain societal biases related to gen-
der, race, religion, and other demographics. By
using these datasets for evaluation, our benchmark
may inadvertently favour models that learn and
reproduce these biases. We did not perform a com-
prehensive audit for such biases in the constituent
datasets. We advocate for users of COLE to be

--- Page 10 ---

aware of this and recommend that future work in-
clude better documentation and characterization
of dataset contents, following principles like those
proposed for Datasheets for Datasets (Gebru et al.,
2021).
Data Provenance and Privacy
The data used in
COLE’s datasets, while publicly available, was cre-
ated by individuals who did not explicitly consent
to its use in training or evaluating large-scale AI
models. For instance, reviews on Allociné were
written for other users, not for machine learning
research. The practice of scraping and repurposing
public data without the informed consent of the
original creators raises significant ethical questions
about privacy and ownership, a problem that has
been highlighted in the context of other large-scale
web-derived datasets (Birhane et al., 2023).
Mitigation and Positive Impact
Despite the
risks, we believe that public benchmarks like
COLE are essential for transparency and account-
ability in AI. By providing a standardized evalu-
ation suite, our work enables researchers to audit
proprietary and open models for specific failings,
including biases or reasoning gaps. Furthermore,
COLE can be used proactively to develop more ro-
bust and safer models. For example, it can serve as
a foundation for “red teaming” exercises, where the
goal is to systematically find and mitigate model
harms before deployment (Ganguli et al., 2022).
We encourage the use of COLE not only for per-
formance ranking but also for critical safety and
ethics research.
Acknowledgements
This research was made possible thanks to the sup-
port of a Canadian insurance company, NSERC
research grant RDCPJ 537198-18 and FRQNT doc-
toral research grant. We thank the reviewers for
their comments regarding our work.
References
Marah Abdin, Jyoti Aneja, Hany Awadalla, Ahmed
Awadallah, Ammar Ahmad Awan, Nguyen Bach,
Amit Bahree, Arash Bakhtiari, Jianmin Bao, Harkirat
Behl, Alon Benhaim, Misha Bilenko, Johan Bjorck,
Sébastien Bubeck, Martin Cai, Qin Cai, Vishrav
Chaudhary, Dong Chen, Dongdong Chen, Weizhu
Chen, Yen-Chun Chen, Yi-Ling Chen, Hao Cheng,
Parul Chopra, Xiyang Dai, Matthew Dixon, Ro-
nen Eldan, Victor Fragoso, Jianfeng Gao, Mei Gao,
Min Gao, Amit Garg, Allie Del Giorno, Abhishek
Goswami, Suriya Gunasekar, Emman Haider, Jun-
heng Hao, Russell J. Hewett, Wenxiang Hu, Jamie
Huynh, Dan Iter, Sam Ade Jacobs, Mojan Javaheripi,
Xin Jin, Nikos Karampatziakis, Piero Kauffmann,
Mahoud Khademi, Dongwoo Kim, Young Jin Kim,
Lev Kurilenko, James R. Lee, Yin Tat Lee, Yuanzhi
Li, Yunsheng Li, Chen Liang, Lars Liden, Xihui
Lin, Zeqi Lin, Ce Liu, Liyuan Liu, Mengchen Liu,
Weishung Liu, Xiaodong Liu, Chong Luo, Piyush
Madan, Ali Mahmoudzadeh, David Majercak, Matt
Mazzola, Caio César Teodoro Mendes, Arindam Mi-
tra, Hardik Modi, Anh Nguyen, Brandon Norick,
Barun Patra, Daniel Perez-Becker, Thomas Portet,
Reid Pryzant, Heyang Qin, Marko Radmilac, Liliang
Ren, Gustavo de Rosa, Corby Rosset, Sambudha Roy,
Olatunji Ruwase, Olli Saarikivi, Amin Saied, Adil
Salim, Michael Santacroce, Shital Shah, Ning Shang,
Hiteshi Sharma, Yelong Shen, Swadheen Shukla, Xia
Song, Masahiro Tanaka, Andrea Tupini, Praneetha
Vaddamanu, Chunyu Wang, Guanhua Wang, Lijuan
Wang, Shuohang Wang, Xin Wang, Yu Wang, Rachel
Ward, Wen Wen, Philipp Witte, Haiping Wu, Xiaoxia
Wu, Michael Wyatt, Bin Xiao, Can Xu, Jiahang Xu,
Weijian Xu, Jilong Xue, Sonali Yadav, Fan Yang,
Jianwei Yang, Yifan Yang, Ziyi Yang, Donghan Yu,
Lu Yuan, Chenruidong Zhang, Cyril Zhang, Jianwen
Zhang, Li Lyna Zhang, Yi Zhang, Yue Zhang, Yunan
Zhang, and Xiren Zhou. 2024a. Phi-3 Technical Re-
port: A Highly Capable Language Model Locally on
Your Phone.
Marah Abdin, Jyoti Aneja, Harkirat Behl, Sébastien
Bubeck, Ronen Eldan, Suriya Gunasekar, Michael
Harrison, Russell J Hewett, Mojan Javaheripi, Piero
Kauffmann, et al. 2024b. Phi-4 Technical Report.
arXiv:2412.08905.
Anne Abeillé, Lionel Clément, and François Toussenel.
2003. The French Treebank: a New Resource for
French. In Treebanks, pages 165–184. Kluwer, Dor-
drecht.
Anne Abeillé and Danièle Godard. 2002. The syntactic
structure of french auxiliaries. Language, 78(3):404–
452.
Eneko Agirre, Mona Diab, Daniel Cer, and Aitor
Gonzalez-Agirre. 2012. SemEval-2012 Task 6: a Pi-
lot on Semantic Textual Similarity. In Proceedings of
the Joint Conference on Lexical and Computational
Semantics: Proceedings of the Main Conference and
the Shared Task: Proceedings of the Sixth Interna-
tional Workshop on Semantic Evaluation, SemEval
’12, page 385–393, USA. Association for Computa-
tional Linguistics.
Loubna Ben Allal,
Anton Lozhkov,
Elie Bak-
ouch, Gabriel Martín Blázquez, Guilherme Penedo,
Lewis Tunstall, Andrés Marafioti, Hynek Kydlíˇcek,
Agustín Piqueres Lajarín, Vaibhav Srivastav, Joshua
Lochner, Caleb Fahlgren, Xuan-Son Nguyen, Clé-
mentine Fourrier, Ben Burtenshaw, Hugo Larcher,
Haojun Zhao, Cyril Zakka, Mathieu Morlon, Colin
Raffel, Leandro von Werra, and Thomas Wolf. 2025.

--- Page 11 ---

SmolLM2: When Smol Goes Big - Data-Centric
Training of a Small Language Model.
Maksim Aparovich, Volha Harytskaya, Vladislav Porit-
ski, Oksana Volchek, and Pavel Smrz. 2025. Belaru-
sianGLUE: Towards a Natural Language Understand-
ing Benchmark for Belarusian. In Proceedings of the
Annual Meeting of the Association for Computational
Linguistics, pages 511–527.
Mikel Artetxe, Sebastian Ruder, and Dani Yogatama.
2020. On the Cross-lingual Transferability of Mono-
lingual Representations. In Proceedings of the An-
nual Meeting of the Association for Computational
Linguistics, pages 5266–5277, Online. Association
for Computational Linguistics.
Viraat Aryabumi, John Dang, Dwarak Talupuru,
Saurabh Dash, David Cairuz, Hangyu Lin, Bharat
Venkitesh, Madeline Smith, Kelly Marchisio, Se-
bastian Ruder, Acyr Locatelli, Julia Kreutzer, Nick
Frosst, Phil Blunsom, Marzieh Fadaee, Ahmet Üstün,
and Sara Hooker. 2024. Aya 23: Open Weight Re-
leases to Further Multilingual Progress.
David Beauchemin and Richard Khoury. 2025. QFr-
CoLA: a Quebec-French Corpus of Linguistic Ac-
ceptability Judgments.
David Beauchemin, Richard Khoury, and Zachary
Gagnon. 2024.
Quebec Automobile Insurance
Question-Answering With Retrieval-Augmented
Generation. In Proceedings of the Natural Legal Lan-
guage Processing Workshop, pages 48–60, Dublin,
Ireland. Association for Computational Linguistics.
David Beauchemin, Horacio Saggion, and Richard
Khoury. 2023.
Meaningbert: assessing meaning
preservation between sentences. Frontiers in Arti-
ficial Intelligence, 6:1223924.
David Beauchemin, Yan Tremblay, Mohamed Amine
Youssef, and Richard Khoury. 2025a.
A Set of
Quebec-French Corpus of Regional Expressions and
Terms.
David Beauchemin, Pier-Luc Veilleux, Richard Khoury,
and Johanna-Pascale Roy. 2025b.
QFrBLiMP: a
Quebec-French Benchmark of Linguistic Minimal
Pairs.
Emily M Bender, Timnit Gebru, Angelina McMillan-
Major, and Shmargaret Shmitchell. 2021. On the
Dangers of Stochastic Parrots: Can Language Models
Be Too Big? In Proceedings of the ACM conference
on fairness, accountability, and transparency, pages
610–623.
Luisa Bentivogli, Raffaella Bernardi, Marco Marelli,
Stefano Menini, Marco Baroni, and Roberto Zam-
parelli. 2016. SICK Through the Semeval Glasses.
Lesson Learned From the Evaluation of Composi-
tional Distributional Semantic Models on Full Sen-
tences Through Semantic Relatedness and Textual
Entailment. Language Resources and Evaluation,
50(1):95–124.
Abeba Birhane, Vinay Uday Prabhu, and Emmanuel Ka-
hembwe. 2023. The Multimodal Crossover: A Case
Study on the LAION-400M Dataset. In Proceedings
of the IEEE/CVF Winter Conference on Applications
of Computer Vision, pages 1831–1843.
Jonas Bjerg. 2024. Tips and Tricks for Prompt Engi-
neering. In The Early-Career Professional’s Guide
to Generative AI: Opportunities and Challenges for
an AI-Enabled Workforce, pages 133–143. Springer.
Théophile
Blard.
2020.
French
Senti-
ment
Analysis
with
BERT.
https:
//github.com/TheophileBlard/
french-sentiment-analysis-with-bert.
Su Lin Blodgett, Lisa Green, and Brendan O’Connor.
2016. Demographic Dialecta Variation in Social Me-
dia: A Case Study of African-American English. In
Proceedings of the Conference on Empirical Methods
in Natural Language Processing, pages 1119–1130,
Austin, Texas. Association for Computational Lin-
guistics.
Samuel R. Bowman, Gabor Angeli, Christopher Potts,
and Christopher D. Manning. 2015. A Large Anno-
tated Corpus for Learning Natural Language Infer-
ence. In Proceedings of the Conference on Empiri-
cal Methods in Natural Language Processing, pages
632–642, Lisbon, Portugal. Association for Compu-
tational Linguistics.
Samuel R. Bowman and George E. Dahl. 2021. What
Will it Take to Fix Benchmarking in NLP?
In
Proceedings of the Conference of the North Amer-
ican Chapter of the Association for Computational
Linguistics: Human Language Technologies, pages
4843–4855, Online. Association for Computational
Linguistics.
Daniel Cer, Mona Diab, Eneko Agirre, Iñigo Lopez-
Gazpio, and Lucia Specia. 2017.
SemEval-2017
Task 1: Semantic Textual Similarity Multilingual and
Cross-lingual Focused Evaluation. In Proceedings
of the International Workshop on Semantic Evalua-
tion, pages 1–14, Vancouver, Canada. Association
for Computational Linguistics.
Yupeng Chang, Xu Wang, Jindong Wang, Yuan Wu,
Linyi Yang, Kaijie Zhu, Hao Chen, Xiaoyuan Yi,
Cunxiang Wang, Yidong Wang, et al. 2023. A Survey
on Evaluation of Large Language Models. ACM
Transactions on Intelligent Systems and Technology.
Christopher Clark, Kenton Lee, Ming-Wei Chang,
Tom Kwiatkowski, Michael Collins, and Kristina
Toutanova. 2019. BoolQ: Exploring the Surprising
Difficulty of Natural Yes/No Questions. In NAACL.
Alexis Conneau, Ruty Rinott, Guillaume Lample, Adina
Williams, Samuel R. Bowman, Holger Schwenk, and
Veselin Stoyanov. 2018. XNLI: Evaluating Cross-
lingual Sentence Representations. In Proceedings
of the Conference on Empirical Methods in Natural
Language Processing, pages 2475–2485, Brussels,
Belgium. Association for Computational Linguistics.

--- Page 12 ---

Ruixiang Cui, Daniel Hershcovich, and Anders Søgaard.
2022. Generalized quantifiers as a source of error
in multilingual nlu benchmarks. In Proceedings of
the Conference of the North American Chapter of the
Association for Computational Linguistics: Human
Language Technologies, Seattle, USA. Association
for Computational Linguistics.
Yiming Cui, Ting Liu, Wanxiang Che, Li Xiao, Zhipeng
Chen, Wentao Ma, Shijin Wang, and Guoping Hu.
2019. A Span-Extraction Dataset for Chinese Ma-
chine Reading Comprehension. In Proceedings of
the Conference on Empirical Methods in Natural Lan-
guage Processing and the International Joint Confer-
ence on Natural Language Processing, pages 5857–
5863, Hong Kong, China. Association for Computa-
tional Linguistics.
Ido Dagan, Oren Glickman, and Bernardo Magnini.
2005.
Pascal.
In Machine Learning Challenges.
Evaluating Predictive Uncertainty, Visual Object
Classification, and Recognising Tectual Entailment:
First PASCAL Machine Learning Challenges Work-
shop, MLCW 2005, Southampton, UK, April 11-
13, 2005, Revised Selected Papers, pages 177–190.
Springer.
John Dang, Shivalika Singh, Daniel D’souza, Arash
Ahmadian, Alejandro Salamanca, Madeline Smith,
Aidan Peppin, Sungjin Hong, Manoj Govindassamy,
Terrence Zhao, Sandra Kublik, Meor Amer, Viraat
Aryabumi, Jon Ander Campos, Yi-Chern Tan, Tom
Kocmi, Florian Strub, Nathan Grinsztajn, Yannis
Flet-Berliac, Acyr Locatelli, Hangyu Lin, Dwarak
Talupuru, Bharat Venkitesh, David Cairuz, Bowen
Yang, Tim Chung, Wei-Yin Ko, Sylvie Shang Shi,
Amir Shukayev, Sammie Bae, Aleksandra Piktus, Ro-
man Castagné, Felipe Cruz-Salinas, Eddie Kim, Lu-
cas Crawhall-Stein, Adrien Morisot, Sudip Roy, Phil
Blunsom, Ivan Zhang, Aidan Gomez, Nick Frosst,
Marzieh Fadaee, Beyza Ermis, Ahmet Üstün, and
Sara Hooker. 2024. Aya Expanse: Combining Re-
search Breakthroughs for a New Multilingual Fron-
tier.
DeepSeek-AI. 2025. DeepSeek-R1: Incentivizing Rea-
soning Capability in LLMs via Reinforcement Learn-
ing.
Martin d’Hoffschmidt, Wacim Belblidia, Quentin
Heinrich, Tom Brendlé, and Maxime Vidal. 2020.
FQuAD: French Question Answering Dataset. In
Findings of the Association for Computational Lin-
guistics, pages 1193–1208, Online. Association for
Computational Linguistics.
Bill Dolan and Chris Brockett. 2005. Automatically
Constructing a Corpus of Sentential Paraphrases. In
Proceedings of the International Workshop on Para-
phrasing, Jeju, Korea. Association for Computational
Linguistics.
Denis Emelin and Rico Sennrich. 2021. Wino-X: Multi-
lingual Winograd Schemas for Commonsense Rea-
soning and Coreference Resolution. In Proceedings
of the Conference on Empirical Methods in Natural
Language Processing, pages 8517–8532, Online and
Punta Cana, Dominican Republic. Association for
Computational Linguistics.
Manuel Faysse. 2022. French-BoolQ: A French Version
of the BoolQ Dataset. https://huggingface.
co/datasets/manu/french_boolq.
Hug-
ging Face Dataset.
Manuel Faysse, Patrick Fernandes, Nuno M. Guerreiro,
António Loison, Duarte M. Alves, Caio Corro, Nico-
las Boizard, João Alves, Ricardo Rei, Pedro H. Mar-
tins, Antoni Bigata Casademunt, François Yvon, An-
dré F. T. Martins, Gautier Viaud, Céline Hudelot,
and Pierre Colombo. 2024. CroissantLLM: A Truly
Bilingual French-English Language Model.
Deep Ganguli, Liane Lovitt, Jackson Kernion, Amanda
Askell, Yuntao Bai, Saurav Kadavath, Ben Mann,
Ethan Perez, Nicholas Schiefer, Kamal Ndousse,
Andy Jones, Sam Israel, Anna Rutter, Thomas Law-
son, Tom Hume, Sam Johnston, Anna Chen, Tom
Conerly, Tom Henighan, Nova DasSarma, Dawn
Drain, D.K. Tran, Nelson Joseph, Nelson Elhage,
Zac Hatfield-Dodds, Andrew Critch, Catherine Ols-
son, Danny Hernandez, Tom Shevlane, Jack Clark,
Jared Kaplan, and Dario Amodei. 2022. Red Team-
ing Language Models to Reduce Harms: Meth-
ods, Scaling Behaviors, and Lessons Learned. In
arXiv:2209.07858.
Timnit Gebru, Jamie Morgenstern, Briana Vecchione,
Jennifer Wortman Vaughan, Hanna Wallach, Hal
Daumé III, and Kate Crawford. 2021. Datasheets
for Datasets. In Proceedings of the ACM Conference
on Fairness, Accountability, and Transparency, pages
1–22.
Danilo Giampiccolo, Bernardo Magnini, Ido Dagan, and
William B Dolan. 2007. The Third Pascal Recogniz-
ing Textual Entailment Challenge. In Proceedings
of the ACL-PASCAL workshop on textual entailment
and paraphrasing, pages 1–9.
Jianping Gou, Baosheng Yu, Stephen J Maybank, and
Dacheng Tao. 2021.
Knowledge Distillation: A
Survey. International journal of computer vision,
129(6):1789–1819.
Olivier Gouvert, Julie Hunter, Jérôme Louradour,
Christophe Cerisara, Evan Dufraisse, Yaya Sy, Laura
Rivière, Jean-Pierre Lorré, and OpenLLM-France
community. 2025. The Lucie-7B LLM and the Lucie
Training Dataset: Open Resources for Multilingual
Language Generation.
IBM Granite Team. 2024. Granite 3.0 Language Mod-
els. URL: https://github. com/ibm-granite/granite-
3.0-language-models.
Aaron Grattafiori, Abhimanyu Dubey, Abhinav Jauhri,
Abhinav Pandey, Abhishek Kadian, Ahmad Al-
Dahle, Aiesha Letman, Akhil Mathur, Alan Schelten,
Alex Vaughan, et al. 2024. The Llama 3 Herd of
Models. arXiv:2407.21783.

--- Page 13 ---

Maurice Gross. 1984. Lexicon-Grammar and the Syn-
tactic Analysis of French. In International Confer-
ence on Computational Linguistics, pages 275–282.
G Hinton. 2014. Distilling the Knowledge in a Neu-
ral Network. In Deep Learning and Representation
Learning Workshop in Conjunction with NIPS.
Binyuan Hui, Jian Yang, Zeyu Cui, Jiaxi Yang, Day-
iheng Liu, Lei Zhang, Tianyu Liu, Jiajun Zhang,
Bowen Yu, Kai Dang, et al. 2024. Qwen2.5 Techni-
cal Report. CoRR.
Fred Jelinek, Robert L Mercer, Lalit R Bahl, and
James K Baker. 1977. Perplexity—a Measure of the
Difficulty of Speech Recognition Tasks. The Journal
of the Acoustical Society of America, 62(S1):S63–
S63.
Minhao Jiang, Ken Ziyu Liu, Ming Zhong, Rylan Scha-
effer, Siru Ouyang, Jiawei Han, and Sanmi Koyejo.
2024.
Investigating Data Contamination for Pre-
Training Language Models. arXiv:2401.06059.
Jaap Jumelet, Leonie Weissweiler, and Arianna Bisazza.
2025.
MultiBLiMP 1.0:
A Massively Multi-
lingual Benchmark of Linguistic Minimal Pairs.
arXiv:2504.02768.
Rachel Keraron, Guillaume Lancrenon, Mathilde Bras,
FrÃ©dÃ©ric Allary, Gilles Moyse, Thomas Scialom,
Edmundo-Pavel Soriano-Morales, and Jacopo Sta-
iano. 2020. Project piaf: Building a native french
question-answering dataset. In Proceedings of The
12th Language Resources and Evaluation Confer-
ence, pages 5483–5492, Marseille, France. European
Language Resources Association.
Lajavaness. 2023. SICK-fr: French version of the SICK
Entailment Dataset.
https://huggingface.
co/datasets/Lajavaness/SICK-fr. Hug-
ging Face Dataset.
Hang Le, Loïc Vial, Jibril Frej, Vincent Segonne, Max-
imin Coavoux, Benjamin Lecouteux, Alexandre Al-
lauzen, Benoît Crabbé, Laurent Besacier, and Didier
Schwab. 2020. FlauBERT: Unsupervised Language
Model Pre-training for French. In Proceedings of
the Language Resources and Evaluation Conference,
pages 2445–2455, Marseille, France. European Lan-
guage Resources Association.
Hector J Levesque, Ernest Davis, and Leora Morgen-
stern. 2012. The Winograd Schema Challenge. In
International Conference on the Principles of Knowl-
edge Representation and Reasoning.
Dawei Li, Bohan Jiang, Liangjie Huang, Alimoham-
mad Beigi, Chengshuai Zhao, Zhen Tan, Amrita
Bhattacharjee, Yuxuan Jiang, Canyu Chen, Tianhao
Wu, et al. 2024.
From Generation to Judgment:
Opportunities and Challenges of LLM-As-A-Judge.
arXiv:2411.16594.
Percy Liang, Rishi Bommasani, Tony Lee, Dimitris
Tsipras, Dilara Soylu, Michihiro Yasunaga, Yian
Zhang, Deepak Narayanan, Yuhuai Wu, Ananya Ku-
mar, et al. 2022. Holistic Evaluation of Language
Models.
Transactions on Machine Learning Re-
search.
Ggaliwango Marvin, Nakayiza Hellen, Daudi Jjingo,
and Joyce Nakatumba-Nabende. 2023. Prompt Engi-
neering in Large Language Models. In International
conference on data intelligence and cognitive infor-
matics, pages 387–402. Springer.
Thomas Mesnard, Cassidy Hardin, Robert Dadashi,
Surya Bhupatiraju, Shreya Pathak, Laurent Sifre,
Morgane Rivière, Mihir Sanjay Kale, Juliette Love,
Pouya Tafti, et al. 2024. Gemma: Open Models
Based on Gemini Research and Technology. CoRR.
Team OLMo, Pete Walsh, Luca Soldaini, Dirk Groen-
eveld, Kyle Lo, Shane Arora, Akshita Bhagia, Yul-
ing Gu, Shengyi Huang, Matt Jordan, Nathan Lam-
bert, Dustin Schwenk, Oyvind Tafjord, Taira An-
derson, David Atkinson, Faeze Brahman, Christo-
pher Clark, Pradeep Dasigi, Nouha Dziri, Michal
Guerquin, Hamish Ivison, Pang Wei Koh, Jiacheng
Liu, Saumya Malik, William Merrill, Lester James V.
Miranda, Jacob Morrison, Tyler Murray, Crystal
Nam, Valentina Pyatkin, Aman Rangapur, Michael
Schmitz, Sam Skjonsberg, David Wadden, Christo-
pher Wilhelm, Michael Wilson, Luke Zettlemoyer,
Ali Farhadi, Noah A. Smith, and Hannaneh Hajishirzi.
2024. 2 OLMo 2 Furious.
OpenAI.
2025.
GPT-OSS.
https://
huggingface.co/openai/gpt-oss-20b.
Long Ouyang, Jeffrey Wu, Xu Jiang, Diogo Almeida,
Carroll Wainwright, Pamela Mishkin, Chong Zhang,
Sandhini Agarwal, Katarina Slama, Alex Ray, et al.
2022. Training Language Models to Follow Instruc-
tions With Human Feedback. Advances in neural
information processing systems, 35:27730–27744.
Jonathan Pacifico. 2024a. Chocolatine-14B-Instruct-
v1.2.
Jonathan Pacifico. 2024b. French-Alpaca-Llama3-8B-
Instruct-v1.0.
Jonathan Pacifico. 2025. Chocolatine-2-14B-Instruct-
v2.0.3.
Kishore Papineni, Salim Roukos, Todd Ward, and Wei-
Jing Zhu. 2002. BLEU: a Method for Automatic
Evaluation of Machine Translation. In Proceedings
of the annual meeting of the Association for Compu-
tational Linguistics, pages 311–318.
Alicia Parrish, William Huang, Omar Agha, Soo-Hwan
Lee, Nikita Nangia, Alexia Warstadt, Karmanya Ag-
garwal, Emily Allaway, Tal Linzen, and Samuel R.
Bowman. 2021. Does Putting a Linguist in the Loop
Improve NLU Data Collection? In Findings of the
Association for Computational Linguistics: EMNLP,
pages 4886–4901, Punta Cana, Dominican Republic.
Association for Computational Linguistics.

--- Page 14 ---

Peter Prettenhofer and Benno Stein. 2010.
Cross-
Language Text Classification Using Structural Corre-
spondence Learning. In Proceedings of the annual
meeting of the association for computational linguis-
tics, pages 1118–1127.
Qwen Team. 2025a. Qwen3 Technical Report.
Qwen Team. 2025b. QwQ-32B: Embracing the Power
of Reinforcement Learning.
Pranav Rajpurkar, Jian Zhang, Konstantin Lopyrev, and
Percy Liang. 2016. SQuAD: 100,000+ Questions for
Machine Comprehension of Text. In Proceedings
of the Conference on Empirical Methods in Natu-
ral Language Processing, pages 2383–2392, Austin,
Texas. Association for Computational Linguistics.
Abhinav Rastogi, Albert Q Jiang, Andy Lo, Gabrielle
Berrada, Guillaume Lample, Jason Rute, Joep Bar-
mentlo, Karmesh Yadav, Kartik Khandelwal, Khy-
athi Raghavi Chandu, et al. 2025.
Magistral.
arXiv:2506.10910.
Reka AI. 2025. Reka-flash-3.
Ange Richard, Laura Alonzo Canul, and François Portet.
2024. FRACAS: a FRench Annotated Corpus of
Attribution Relations in NewS. In Joint International
Conference on Computational Linguistics, Language
Resources and Evaluation, pages 7417–7428.
Paul Rowlett. 2007. Thes Syntax of French. Cambridge
University Press.
Prithiv Sakthi. 2025a. Deepthink-Reasoning-14B.
Prithiv Sakthi. 2025b. Deepthink-Reasoning-7B.
V Sanh. 2019. DistilBERT, a Distilled Version of BERT:
Smaller, Faster, Cheaper and Lighter. In Proceed-
ings of Conference on Neural Information Processing
Systems.
Djamé Seddah, Reut Tsarfaty, Sandra Kübler, Marie
Candito, Jinho D Choi, Richárd Farkas, Jennifer Fos-
ter, Iakes Goenaga, Koldo Gojenola Galletebeitia,
Yoav Goldberg, et al. 2013. Overview of the SPMRL
Shared Task: A Cross-Framework Evaluation of
Parsing Morphologically Rich Languages. In Pro-
ceedings of the Workshop on Statistical Parsing of
Morphologically-Rich Languages, pages 146–182.
Association for Computational Linguistics.
Vincent Segonne, Marie Candito, and Benoît Crabbé.
2019. Using Wiktionary as a Resource for Wsd: The
Case of French Verbs. In Proceedings of the Interna-
tional Conference on Computational Semantics-Long
Papers, pages 259–270. Association for Computa-
tional Linguistics.
Chih-Chieh Shao, Trois Wang, Yuting Huang, Sam
Tsai, K. Robert Chang, and Hsuan-Tien Hsu. 2018.
DRCD: a Chinese Machine Reading Comprehension
Dataset. In Proceedings of the Conference on Em-
pirical Methods in Natural Language Processing:
System Demonstrations, pages 25–30, Brussels, Bel-
gium. Association for Computational Linguistics.
Simple Scaling. 2025. s1.1-32B.
Maximos Skandalis, Richard Moot, Christian Retoré,
and Simon Robillard. 2024. New Datasets for Auto-
matic Detection of Textual Entailment and of Contra-
dictions between Sentences in rench. In Proceedings
of the Joint International Conference on Computa-
tional Linguistics, Language Resources and Evalua-
tion, pages 12173–12186, Torino, Italy. ELRA and
ICCL.
Richard Socher, Alex Perelygin, Jean Wu, Jason
Chuang, Christopher D. Manning, Andrew Ng, and
Christopher Potts. 2013. Recursive Deep Models for
Semantic Compositionality Over a Sentiment Tree-
bank. In Proceedings of the Conference on Empiri-
cal Methods in Natural Language Processing, pages
1631–1642, Seattle, Washington, USA. Association
for Computational Linguistics.
Kai Sun, Dian Yu, Cong Yu, Claire Dong, Jianshu
Wang, Yin Tian, Weitang Liu, Zehan Tian, and
Dong Yu. 2020.
C3:
A Reading Comprehen-
sion Dataset Requiring Char-level, Clause-level and
Causal-reasoning. In Proceedings of the Interna-
tional Conference on Computational Linguistics,
pages 4682–4693, Barcelona, Spain (Online). Inter-
national Committee on Computational Linguistics.
Apertus Team. 2025.
Apertus:
Democratizing
Open and Compliant LLMs for Global Language
Environments.
https://huggingface.co/
swiss-ai/Apertus-70B-2509.
Arun James Thirunavukarasu, Daniel Shu Wei Ting,
Kavya Elangovan, Laura Gutierrez, Tock Han Tan,
and Lavisha Jeyaseelan. 2023. Large Language Mod-
els in Medicine. Nature medicine, 29(8):1930–1940.
Alex Wang, Amanpreet Singh, Julian Michael, Felix
Hill, Omer Levy, and Samuel Bowman. 2018. GLUE:
A multi-task benchmark and analysis platform for nat-
ural language understanding. In Proceedings of the
EMNLP Workshop BlackboxNLP: Analyzing and In-
terpreting Neural Networks for NLP, pages 353–355,
Brussels, Belgium. Association for Computational
Linguistics.
Alex Warstadt, Amanpreet Singh, and Samuel R. Bow-
man. 2019.
Neural Network Acceptability Judg-
ments. In Transactions of the Association for Com-
putational Linguistics, volume 7, pages 631–646,
Cambridge, MA. MIT Press.
Adina Williams, Nikita Nangia, and Samuel Bowman.
2018a. A broad-coverage challenge corpus for sen-
tence understanding through inference. In Proceed-
ings of the Conference of the North American Chap-
ter of the Association for Computational Linguistics:
Human Language Technologies, pages 1112–1122.
Association for Computational Linguistics.
Adina Williams, Nikita Nangia, and Samuel R. Bow-
man. 2018b. A Broad-Coverage Challenge Corpus
for Sentence Understanding through Inference. In

--- Page 15 ---

Proceedings of the Conference of the North Ameri-
can Chapter of the Association for Computational
Linguistics: Human Language Technologies, pages
1112–1122, New Orleans, Louisiana. Association for
Computational Linguistics.
Thomas Wolf, Lysandre Debut, Victor Sanh, Julien
Chaumond, Clement Delangue, Anthony Moi, Pier-
ric Cistac, Tim Rault, Rémi Louf, Morgan Funtow-
icz, Joe Davison, Sam Shleifer, Patrick von Platen,
Clara Ma, Yacine Jernite, Julien Plu, Canwen Xu,
Teven Le Scao, Sylvain Gugger, Mariama Drame,
Quentin Lhoest, and Alexander M. Rush. 2020. Hug-
gingFace’s Transformers: State-of-the-art Natural
Language Processing. arXiv:1910.03771.
Liang Xu, Hai Hu, Xuanwei Zhang, Lu Li, Chenjie Cao,
Yudong Li, Yechen Xu, Kai Sun, Dian Yu, Cong
Yu, Yin Tian, Qianqian Dong, Weitang Liu, Bo Shi,
Yiming Cui, Junyi Li, Jun Zeng, Rongzhao Wang,
Weijian Xie, Yanting Li, Yina Patterson, Zehan Tian,
Dian Zhang, Fangkai Zhou, Chao Sun, Hang Li, and
Jian Sun. 2020. CLUE: A Chinese Language Un-
derstanding Evaluation Benchmark. In Proceedings
of the International Conference on Computational
Linguistics, pages 4762–4772, Barcelona, Spain (On-
line). International Committee on Computational Lin-
guistics.
Yinfei Yang, Yuan Zhang, Chris Tar, and Jason
Baldridge. 2019.
PAWS-X: A Cross-lingual Ad-
versarial Dataset for Paraphrase Identification. In
Proceedings of EMNLP.
Qinyuan Ye, Mohamed Ahmed, Reid Pryzant, and
Fereshte Khani. 2024. Prompt Engineering a Prompt
Engineer. In Findings of the Association for Compu-
tational Linguistics, pages 355–385.
Chujie Zheng, Minlie Huang, and Aixin Sun. 2019.
CHID: A Chinese Idiom Dataset for Cloze Test. In
Proceedings of the Annual Meeting of the Associ-
ation for Computational Linguistics, pages 5408–
5417, Florence, Italy. Association for Computational
Linguistics.
Łukasz Augustyniak, Szymon Wo´zniak, Marcin Gruza,
Piotr Gramacki, Krzysztof Rajda, Mikołaj Morzy,
and Tomasz Kajdanowicz. 2023. Massively Multilin-
gual Corpus of Sentiment Datasets and Multi-faceted
Sentiment Classification Benchmark.
A
Inference Prompt Details
We present in Figure 2, the translated prompt used
to generate the predictions per task. Prompt were
inspired by Aparovich et al. (2025) prompts and
prompt engineering best practices (Marvin et al.,
2023; Ye et al., 2024; Li et al., 2024; Bjerg, 2024).
B
Selected LLM Details
We present in Table 2 the comprehensive suite of
open-source LLMs we could fit on our hardware2
(details in Table 2), detailing their origins and re-
spective sizes, while in Table 3, we present the com-
prehensive suite of private LLMs benchmarked in
our study. The selection was curated to cover a
wide spectrum of parameter counts, and to include
those with specializations in French (Υ) or rea-
soning (Γ). All LLMs are downloaded from the
HuggingFace Model repository (Wolf et al., 2020)
using default parameters.
C
Hardware and Private LLM Inference
Budget
C.1
Hardware
We rely on three NVIDIA RTX 6000 ADA with 49
GB of memory, without memory pooling; thus, the
maximum size we can fit is around 32B parameters
in order to have a sufficient batch size to process
the experiment in a reasonable timeframe (i.e. a
month or so).
C.2
Private LLM Inference Budget
We allocated a budget of approximately 2,000 USD
for using private LLM APIs (e.g., OpenAI, An-
thropic) during development, prototyping, and ad-
justing our prompts. For the complete inference
loop across all selected private LLMs and tasks, we
allocated a budget of nearly $ 17,500 USD. It took
approximately four weeks to process all private
model inference in parallel.
D
Complete Experiments Results
In this section, we present our complete results in
Table 4.
2We rely on three NVIDIA RTX 6000 ADA with 49 GB
of memory, without memory pooling, thus the maximum size
we can fit is around 32B parameters.

--- Page 16 ---

LLM
Source
Size
Apertus-8B-it-2509
Team (2025)
8B
Apertus-8B-2509
Team (2025)
8B
Aya-23-8b
Aryabumi et al. (2024)
8B
Aya-expanse-8b
Dang et al. (2024)
8B
Chocolatine-14b-it (Υ)
Pacifico (2024a)
14B
Chocolatine-2-14b-it (Υ)
Pacifico (2025)
14.8B
CroissantLLM-Base (Υ)
Faysse et al. (2024)
1.3B
DeepSeek-R1-distill-Llama-8b (Γ)
DeepSeek-AI (2025)
8.03B
DeepSeek-R1-distill-Qwen-14b (Γ)
DeepSeek-AI (2025)
14.8B
DeepSeek-R1-distill-Qwen-32b (Γ)
DeepSeek-AI (2025)
32.8B
DeepSeek-R1-distill-Qwen-7b (Γ)
DeepSeek-AI (2025)
7.62B
DeepSeek-R1-distill-Qwen3-8b (Γ)
DeepSeek-AI (2025)
5.27B
Deepthink-reasoning-14b (Γ)
Sakthi (2025a)
14.8B
Deepthink-reasoning-7b (Γ)
Sakthi (2025b)
7.62B
French-Alpaca-Llama3-8b-it (Υ, Γ)
Pacifico (2024b)
8.03B
Gemma-2-27b-it (Γ)
Mesnard et al. (2024)
27.2B
Gemma-2-27b (Γ)
Mesnard et al. (2024)
27.2B
Gemma-2-2b-it (Γ)
Mesnard et al. (2024)
27.2B
Gemma-2-2b (Γ)
Mesnard et al. (2024)
2.6B
Gemma-2-9b-it (Γ)
Mesnard et al. (2024)
9B
Gemma-2-9b (Γ)
Mesnard et al. (2024)
9.2B
GPT-oss-20b (Γ)
OpenAI (2025)
21.5B
Granite3.2-8B
Granite Team (2024)
8.17B
Granite3.3-8B-base
Granite Team (2024)
8.17B
Granite3.3-8B-it
Granite Team (2024)
8.17B
Llama-3.2-1b-it (Γ)
Grattafiori et al. (2024)
1.2B
Llama-3.2-1b (Γ)
Grattafiori et al. (2024)
1.2B
Llama-3.2-3b-it (Γ)
Grattafiori et al. (2024)
3.21B
Llama-3.2-3b (Γ)
Grattafiori et al. (2024)
3.21B
Lucie-7b-it-human-data (Υ)
Gouvert et al. (2025)
6.71B
Lucie-7b-it (Υ)
Gouvert et al. (2025)
6.71B
Lucie-7b (Υ)
Gouvert et al. (2025)
6.71B
Meta-Llama-3.1-8b-it (Γ)
Grattafiori et al. (2024)
8B
Meta-Llama-3.1-8b (Γ)
Grattafiori et al. (2024)
8B
Mixtral-8x7b-it
Rastogi et al. (2025)
46.7B
Mixtral-8x7b
Rastogi et al. (2025)
46.7B
OLMo-2-32B-it
OLMo et al. (2024)
32.2B
OLMo-2-32B
OLMo et al. (2024)
32.2B
OLMo-2-13B-it
OLMo et al. (2024)
13.7B
OLMo-2-13B
OLMo et al. (2024)
13.7B
OLMo-2-7B-it
OLMo et al. (2024)
7.3B
OLMo-2-7B
OLMo et al. (2024)
7.3B
OLMo-2-1B-it
OLMo et al. (2024)
1.48B
OLMo-2-1B
OLMo et al. (2024)
1.48B
Phi-3.5-mini-it
Abdin et al. (2024a)
3.8B
Phi-4
Abdin et al. (2024b)
14.7B
QwQ-32b (Γ)
Qwen Team (2025b)
32.8B
Qwen2.5-0.5b-it (Γ)
Hui et al. (2024)
494M
Qwen2.5-0.5b
Hui et al. (2024)
494M
Qwen2.5-1.5b-it
Hui et al. (2024)
1.5B
Qwen2.5-1.5b
Hui et al. (2024)
1.5B
Qwen2.5-14b-it
Hui et al. (2024)
14.7B
Qwen2.5-14b
Hui et al. (2024)
14.7B
Qwen2.5-32b-it
Hui et al. (2024)
32.8B
Qwen2.5-32b
Hui et al. (2024)
32.8B
Qwen2.5-3b-it
Hui et al. (2024)
3B
Qwen2.5-3b
Hui et al. (2024)
3B
Qwen2.5-7b-it
Hui et al. (2024)
7.6B
Qwen2.5-7b
Hui et al. (2024)
7.6B
Qwen3-14b-base
Qwen Team (2025a)
14.8B
Qwen3-14b
Qwen Team (2025a)
8.76B
Reka-flash-3 (Γ)
Reka AI (2025)
20.9B
S1.1-32b (Γ)
Simple Scaling (2025)
32.8B
SmolLM2-1.7b-it
Allal et al. (2025)
1.7B
SmolLM2-1.7b
Allal et al. (2025)
1.7B
SmolLM2-135m-it
Allal et al. (2025)
134.5M
SmolLM2-135m
Allal et al. (2025)
134.5M
SmolLM2-360m-it
Allal et al. (2025)
361.8M
SmolLM2-360m
Allal et al. (2025)
361.8M
Table 2: The selected open-source LLM used in our work, along with their source and size. “Υ” are model that have
a specialization in French, while “Γ” are model marketed as reasoning LLM.

--- Page 17 ---

LLM
Source
Claude-Opus-4-20250514 (Γ)
Anthropic
Claude-Sonnet-4-20250514 (Γ)
Anthropic
DeepSeek-chat
DeepSeek
DeepSeek-reasoner (Γ)
DeepSeek
Gemini-2.5-flash
Google
Gemini-2.5-pro (Γ)
Google
GPT-4.1-2025-04-14
OpenAI
GPT-4.1-mini-2025-04-14
OpenAI
GPT-4o-2024-08-06
OpenAI
GPT-4o-mini-2024-07-18
OpenAI
GPT-5-2025-08-07 (Γ)
OpenAI
GPT-5-mini-2025-08-07 (Γ)
OpenAI
GPT-oss-120B (Γ)
OpenAI
Grok-3-fast-latest (Γ)
xAI
Grok-3-latest (Γ)
xAI
Grok-3-mini-fast-latest (Γ)
xAI
Grok-3-mini-latest (Γ)
xAI
Grok-4-0709 (Γ)
xAI
Mistral-large-latest (Γ)
Mistral
o1-2024-12-17 (Γ)
OpenAI
o1-mini-2024-09-12 (Γ)
OpenAI
o3-2025-04-16 (Γ)
OpenAI
o3-mini-2025-01-31 (Γ)
OpenAI
Pixtral-large-latest
Mistral
Qwen-max (Γ)
Qwen
Table 3: The selected private LLM used in our work, along with their source. “Γ” are model that are marketed as
reasoning LLM.

--- Page 18 ---

LLM
Allocine
Acc. (%)
DACCORD
Acc. (%)
FQuAD
EM (%)
FQuAD
F1 (%)
FraCaS
Acc. (%)
Fr-BoolQ
Acc. (%)
GQNLI-Fr
Acc. (%)
LingNLI-Fr
Acc. (%)
MMS
Acc. (%)
MNLI-9/11-Fr
Acc. (%)
MultiBLiMP-Fr
Acc. (%)
PAWS-X
Acc. (%)
PIAF
EM (%)
PIAF
F1 (%)
QFrBLiMP
Acc. (%)
QFrCoLA
Acc. (%)
QFrCoRE
Acc. (%)
QFrCoRT
Acc. (%)
RT3-Fr
Acc. (%)
SICK-Fr
Acc. (%)
STS22
Acc. (%)
Wino-X-LM
Acc. (%)
Wino-X-MT
Acc. (%)
WSD
EM (%)
XNLI-Fr
Acc. (%)
Apertus-8B-2509
48.83
49.61
25.00
6.37
14.03
46.07
26.67
31.70
20.97
31.70
40.26
49.55
26.04
5.73
50.28
42.30
9.76
14.04
38.12
49.86
19.44
49.98
49.70
0.00
33.41
Apertus-8B-it-2509
51.59
50.19
50.00
18.19
11.94
49.44
30.00
32.97
38.76
33.65
49.35
54.90
0.00
14.32
51.80
31.61
13.40
18.13
10.12
31.31
22.22
50.66
49.53
0.00
32.65
Aya-23-8b
46.20
49.90
25.00
21.05
9.85
48.88
30.00
32.03
39.48
32.70
45.45
48.55
1.04
17.53
50.47
62.67
9.99
12.87
9.88
15.37
26.39
49.12
49.93
0.00
33.33
Aya-expanse-8b
48.58
49.81
27.75
64.38
29.25
46.07
30.00
32.56
20.53
32.05
45.45
48.10
20.05
54.52
52.93
67.92
9.37
7.60
39.75
56.87
29.17
49.19
50.64
0.83
33.33
Chocolatine-14B-it-DPO-v1.3 (Υ)
53.05
60.83
50.00
4.41
28.06
50.00
36.67
33.58
33.95
33.40
59.74
54.90
0.00
0.00
64.27
30.93
9.61
10.53
28.75
31.72
29.17
57.72
49.97
2.92
34.55
Chocolatine-2-14B-it-v2.0.3 (Υ)
80.73
54.84
21.50
55.57
47.46
44.38
36.67
36.36
52.47
36.35
94.81
46.10
17.19
46.52
86.01
72.52
11.33
12.28
45.12
23.93
30.56
64.63
53.08
17.85
37.98
Claude-opus-4-20250514 (Γ)
96.92
95.07
0.00
0.00
61.79
94.94
60.00
69.55
75.65
70.30
98.70
79.05
26.04
29.11
88.66
82.31
93.46
97.66
82.88
75.64
51.39
91.34
82.13
0.16
75.63
Claude-sonnet-4-20250514 (Γ)
96.73
96.62
0.00
2.78
58.21
96.63
63.33
72.70
75.29
72.70
97.40
75.25
0.00
10.42
88.85
82.63
91.75
97.66
86.75
78.88
58.33
92.23
73.59
1.51
73.69
CroissantLLMBase (Υ)
47.98
49.81
0.00
2.18
9.85
48.31
30.00
32.05
39.50
32.70
45.45
48.55
0.00
59.80
49.53
59.91
10.58
9.36
9.12
14.51
22.22
51.13
49.43
0.00
33.33
DeepSeek-R1-0528-Qwen3-8B
30.18
47.10
0.00
7.80
37.01
50.00
40.00
33.78
12.11
33.65
53.25
49.80
0.00
7.41
51.23
48.66
3.93
6.43
29.88
45.64
13.89
48.84
50.10
0.00
25.79
DeepSeek-R1-Distill-Llama-8B (Γ)
57.60
52.80
0.00
6.93
20.60
43.82
46.67
33.89
42.70
32.60
50.65
48.10
0.00
8.20
51.23
55.96
10.49
11.11
41.38
15.39
26.39
49.27
49.03
0.00
32.87
DeepSeek-R1-Distill-Qwen-14B (Γ)
68.64
72.53
0.00
5.05
44.18
46.63
40.00
43.18
71.36
45.45
41.56
48.70
0.00
3.74
50.09
62.70
32.18
35.67
31.87
20.77
26.39
50.59
49.46
0.00
53.55
DeepSeek-R1-Distill-Qwen-32B (Γ)
94.21
58.99
0.00
8.58
51.04
65.17
36.67
47.70
73.17
51.40
58.44
54.50
0.00
7.94
60.11
67.45
31.04
53.22
54.50
55.01
38.89
56.25
50.03
0.00
48.70
DeepSeek-R1-Distill-Qwen-7B (Γ)
41.05
50.87
0.00
4.28
48.36
52.81
23.33
33.50
33.75
34.25
49.35
50.25
0.00
6.83
52.93
64.31
8.72
12.87
50.62
56.67
27.78
50.38
48.09
0.00
32.61
DeepSeek-chat
95.20
92.75
37.00
63.48
35.22
92.70
26.67
61.27
73.11
63.50
97.40
75.80
24.74
49.75
88.85
80.81
83.92
92.40
70.25
33.49
50.00
79.45
52.91
44.79
64.61
DeepSeek-reasoner (Γ)
95.71
96.23
7.75
13.54
63.88
93.26
46.67
62.17
73.90
63.60
97.40
77.45
7.81
14.39
89.98
81.08
84.98
91.23
74.25
69.71
52.78
77.77
53.08
0.26
66.05
Deepthink-Reasoning-14B (Γ)
29.39
70.50
1.25
26.18
29.55
53.93
33.33
42.20
40.43
50.45
89.61
53.75
0.00
23.50
69.94
54.90
32.87
31.58
38.50
48.12
25.00
54.74
50.20
0.00
51.92
Deepthink-Reasoning-7B (Γ)
55.22
50.48
1.50
4.27
42.69
55.62
53.33
36.85
70.49
41.00
49.35
54.90
52.08
5.91
52.74
65.33
15.73
13.45
60.62
36.36
37.50
52.70
51.17
0.38
39.20
French-Alpaca-Llama3-8B-it-v1.0 (ΓΥ)
78.44
56.67
100.00
8.46
60.30
51.69
40.00
35.23
43.98
35.30
58.44
47.65
78.12
9.51
53.88
65.35
23.74
16.37
50.88
28.62
31.94
51.31
50.70
0.03
33.83
GPT-4.1-2025-04-14
96.20
96.81
0.00
0.00
63.88
95.51
70.00
73.19
75.56
75.20
98.70
77.05
0.00
0.00
89.79
82.89
86.73
94.15
83.00
80.17
50.00
84.71
62.95
1.22
71.88
GPT-4.1-mini-2025-04-14
95.43
93.91
16.00
49.07
54.93
93.82
70.00
65.77
75.18
66.90
93.51
73.45
13.80
39.00
89.22
78.98
82.80
92.40
81.12
72.85
51.39
79.38
57.76
34.57
70.68
GPT-4o-2024-08-06
94.44
96.62
0.00
2.78
58.21
94.38
66.67
70.75
74.92
72.40
98.70
78.00
0.00
0.00
88.47
82.85
83.94
93.57
79.00
80.00
47.22
83.03
58.17
0.00
71.98
GPT-4o-mini-2024-07-18
95.52
93.13
6.75
43.41
66.27
97.19
53.33
63.44
74.00
63.80
97.40
77.10
5.99
33.87
86.77
81.50
73.88
90.64
76.62
77.44
56.94
69.14
51.37
39.86
67.56
GPT-5-2025-08-07 (Γ)
97.08
96.13
0.00
0.00
43.88
94.38
60.00
57.49
75.27
61.25
98.70
78.45
0.00
10.42
90.93
83.99
87.93
95.32
82.50
80.41
47.22
94.63
91.63
0.00
62.73
GPT-5-mini-2025-08-07 (Γ)
96.47
96.42
12.50
43.26
58.21
96.07
66.67
63.64
75.21
66.50
98.70
77.45
7.29
31.87
89.22
81.90
77.36
92.40
85.88
80.84
58.33
93.84
91.03
37.62
74.25
GPT-oss-120b (Γ)
94.71
95.84
3.25
15.46
41.49
93.26
56.67
61.70
71.72
65.25
100.00
77.40
2.34
13.42
89.41
78.15
66.52
76.61
83.88
84.08
52.78
81.10
74.26
4.20
65.67
GPT-oss-20b (Γ)
49.95
50.39
0.00
16.05
25.37
52.25
30.00
33.89
21.05
34.00
38.96
46.95
0.00
12.76
51.98
53.46
6.65
8.77
15.50
37.89
25.00
51.16
49.56
0.00
31.30
Gemini-2.5-flash
89.58
95.16
0.00
0.00
60.30
95.51
63.33
66.40
72.81
66.25
100.00
77.45
0.00
0.00
88.66
80.86
87.80
95.91
79.50
72.85
48.61
82.96
61.38
0.00
69.84
Gemini-2.5-pro (Γ)
96.58
97.39
0.00
2.78
55.82
95.51
70.00
67.89
75.50
67.50
97.40
76.95
0.00
10.42
90.36
85.77
90.68
96.49
85.62
71.40
50.00
92.52
88.42
0.00
70.68
Gemma-2-27b-it (Γ)
17.81
50.19
3.00
4.48
54.63
53.37
40.00
32.21
27.54
30.60
59.74
50.95
2.60
3.87
58.98
44.12
27.78
15.20
45.00
35.30
25.00
55.14
49.80
1.25
31.82
Gemma-2-27b (Γ)
44.84
49.23
75.00
2.26
31.94
51.12
33.33
31.19
21.92
30.45
40.26
50.80
78.12
1.58
46.12
48.17
6.15
4.68
21.50
28.54
27.78
48.37
50.27
0.19
30.84
Gemma-2-2b-it (Γ)
11.37
49.61
75.00
2.08
31.64
56.74
30.00
30.29
16.68
29.80
44.16
50.30
0.00
55.22
51.61
55.76
12.84
5.26
33.50
56.44
23.61
49.77
49.10
0.00
25.47
Gemma-2-2b (Γ)
48.39
49.81
1.75
3.66
33.73
49.44
33.33
33.54
21.78
33.25
45.45
46.70
78.12
1.39
51.42
51.83
10.64
12.87
33.50
55.52
26.39
50.98
49.16
0.00
32.83
Gemma-2-9b-it (Γ)
46.59
21.08
2.50
5.92
45.07
57.87
23.33
25.04
6.01
22.85
64.94
58.55
52.08
1.15
69.19
69.32
6.76
8.19
30.63
7.32
9.72
52.85
51.54
0.42
19.54
Gemma-2-9b (Γ)
47.77
49.71
2.25
3.81
25.97
47.19
36.67
32.60
21.50
29.40
51.95
45.80
0.00
70.85
52.55
58.73
2.18
5.85
40.38
56.22
31.94
49.98
49.90
0.03
33.27
Granite-3.2-8b-it
92.90
49.90
14.75
48.03
60.90
51.69
40.00
35.40
48.70
35.25
45.45
49.90
12.76
41.76
54.25
67.19
11.33
10.53
51.25
28.64
30.56
50.63
51.31
16.92
33.25
Granite-3.3-8b-base
52.46
52.61
75.00
17.64
61.19
50.56
46.67
35.21
40.80
35.55
53.25
48.05
1.82
14.71
53.12
49.23
9.82
12.87
48.38
30.78
37.50
49.41
50.23
0.10
33.49
Granite-3.3-8b-it
74.72
49.32
0.00
27.02
37.01
52.25
26.67
33.21
37.58
33.70
49.35
46.65
0.00
21.45
50.85
64.90
12.67
17.54
35.38
37.22
27.78
50.66
50.33
0.00
33.61
Grok-3-fast-latest (Γ)
95.80
96.62
0.00
0.00
57.31
95.51
60.00
67.67
74.38
70.45
98.70
77.75
0.00
0.00
89.79
82.71
79.43
92.40
82.38
73.85
41.67
83.64
61.11
0.00
67.56
Grok-3-latest (Γ)
95.83
96.62
0.00
0.00
58.81
95.51
66.67
67.28
74.39
70.75
98.70
77.80
0.00
0.00
90.74
82.48
79.47
91.23
82.12
73.77
44.44
83.71
60.94
0.00
67.37
Grok-3-mini-fast-latest (Γ)
95.87
97.49
0.00
2.78
34.03
94.94
50.00
58.19
75.35
57.70
98.70
75.80
0.00
10.42
90.36
81.74
82.54
88.89
82.50
77.48
55.56
86.25
81.83
0.00
60.84
Grok-3-mini-latest (Γ)
95.83
97.29
0.00
2.78
35.82
94.38
56.67
57.92
75.26
58.00
100.00
76.60
0.00
10.42
90.36
82.00
82.50
90.64
82.75
78.54
54.17
86.32
81.76
0.00
60.28
Grok-4-0709
96.98
91.97
0.00
0.00
36.42
94.38
56.67
55.69
76.24
57.95
100.00
73.95
0.00
10.42
90.93
83.21
85.84
95.32
83.88
75.30
44.44
95.99
93.74
0.00
58.34
Llama-3.2-1B-it (Γ)
58.78
49.90
3.00
3.96
54.93
47.75
16.67
33.17
34.03
33.15
44.16
52.50
1.04
1.94
49.34
48.30
15.93
12.28
47.25
28.70
31.94
51.63
50.33
0.03
32.97
Llama-3.2-1B (Γ)
51.93
49.52
25.00
1.43
61.49
55.62
40.00
34.91
39.98
35.25
51.95
50.70
26.04
72.41
50.09
34.75
9.67
11.11
51.25
28.62
26.39
49.91
49.90
0.00
32.51
Llama-3.2-3B-it (Γ)
54.97
59.19
3.25
6.89
29.85
60.67
43.33
38.71
70.60
37.50
51.95
50.45
26.04
3.16
55.95
60.15
17.61
24.56
49.88
41.19
30.56
49.70
49.67
0.03
40.90
Llama-3.2-3B (Γ)
51.89
50.00
75.00
2.83
13.13
50.56
33.33
31.31
39.25
32.05
46.75
54.00
0.00
53.34
48.58
31.83
9.67
12.87
12.38
14.51
33.33
50.48
51.27
0.00
33.11
Lucie-7B-it-human-data (Υ)
52.11
50.58
29.75
50.31
42.99
48.88
40.00
34.85
36.59
36.65
50.65
54.75
22.40
43.09
50.09
32.10
9.91
10.53
12.50
19.81
23.61
49.87
49.73
0.06
33.51
Lucie-7B-it-v1.1 (Υ)
43.36
48.74
0.00
23.69
10.45
43.82
30.00
31.76
54.80
32.85
46.75
49.95
0.00
18.87
47.83
39.11
17.35
17.54
9.00
14.51
19.44
48.48
49.73
0.00
31.58
Lucie-7B (Υ)
47.57
49.90
35.50
55.66
60.30
46.63
36.67
35.34
39.95
35.25
51.95
54.10
30.21
47.56
51.98
31.26
10.12
7.60
42.75
19.26
20.83
49.70
49.73
2.76
33.37
Meta-Llama-3.1-8B-it (Γ)
82.30
74.37
4.75
8.33
40.90
55.62
36.67
38.22
56.18
39.95
62.34
54.85
3.39
11.56
62.57
65.54
20.14
9.36
41.75
58.56
37.50
50.91
48.96
0.13
38.38
Meta-Llama-3.1-8B (Γ)
52.48
50.10
2.25
5.65
60.90
48.88
40.00
35.32
48.26
35.20
50.65
52.35
0.00
2.75
47.64
48.22
9.78
9.36
46.25
21.83
27.78
49.87
49.33
0.00
33.25
Mistral-large-latest (Γ)
95.76
95.07
0.00
0.00
58.81
94.38
46.67
65.89
75.31
66.15
96.10
77.50
0.00
0.00
90.17
82.18
84.03
90.64
75.62
70.83
48.61
81.38
55.89
0.00
66.51
Mixtral-8x7B-it-v0.1
60.52
49.42
4.25
39.73
40.30
49.44
46.67
34.42
40.26
34.05
41.56
53.70
4.95
33.12
39.32
35.56
9.86
11.70
32.88
20.57
18.06
52.81
49.40
8.88
32.81
Mixtral-8x7B-v0.1
52.06
49.71
10.50
32.99
60.30
49.44
40.00
35.07
39.88
35.50
53.25
47.50
9.11
26.52
57.84
63.99
9.43
11.70
49.38
28.01
27.78
50.73
49.10
2.76
33.37
OLMo-2-0325-32B-it
3.89
47.10
13.50
50.39
40.90
37.08
16.67
31.23
15.25
31.05
36.36
43.70
11.46
41.33
40.83
47.40
3.95
2.92
27.62
23.81
26.39
50.52
50.47
3.49
13.85
OLMo-2-0325-32B
46.92
50.19
11.25
37.14
58.21
42.70
36.67
31.86
19.36
34.05
46.75
47.60
7.29
28.97
43.10
45.49
8.29
5.85
27.25
32.25
33.33
49.41
48.49
1.06
32.85
OLMo-2-0425-1B-it
48.58
49.13
8.75
31.55
16.72
51.69
33.33
31.70
27.58
34.10
55.84
51.40
2.08
21.42
49.72
53.71
12.82
32.16
35.00
46.49
25.00
51.49
50.80
0.00
33.67
OLMo-2-0425-1B
46.85
48.84
1.25
11.37
48.36
44.94
36.67
34.87
22.09
33.30
50.65
52.90
26.04
7.82
45.56
32.12
9.48
12.87
41.75
55.67
23.61
50.77
49.83
0.00
33.39
OLMo-2-1124-13B-it
49.79
48.94
20.25
53.71
25.97
50.00
20.00
31.00
28.27
31.10
62.34
52.30
14.84
46.89
48.96
39.50
12.30
12.87
20.62
24.54
27.78
50.02
48.29
0.70
32.12
OLMo-2-1124-13B
48.43
50.10
11.50
41.84
18.81
41.57
20.00
31.35
26.94
31.60
46.75
48.55
8.85
34.06
52.17
51.76
9.56
13.45
30.00
14.59
27.78
49.16
48.56
0.19
32.61
OLMo-2-1124-7B-it
31.85
50.87
15.75
47.13
25.97
51.69
50.00
33.11
27.82
33.25
58.44
52.25
9.64
38.67
56.90
58.79
9.26
8.19
29.12
27.99
23.61
51.02
48.09
2.92
37.80
OLMo-2-1124-7B
43.44
48.65
9.00
32.02
31.04
57.30
33.33
31.98
24.29
31.95
50.65
51.05
5.99
25.49
53.88
63.57
9.76
9.94
45.38
29.11
25.00
51.02
48.29
0.06
32.16
Phi-3.5-mini-it
29.30
29.40
50.00
5.37
29.25
48.88
30.00
32.29
21.95
32.00
50.65
45.60
52.08
3.05
51.98
68.71
5.42
12.28
41.50
69.34
13.89
50.63
49.83
0.16
33.31
Phi-4
60.36
64.51
0.00
83.98
60.30
50.00
40.00
35.64
65.67
35.65
46.75
45.55
0.00
6.34
49.15
54.09
18.33
36.84
62.00
66.35
25.00
49.87
50.74
0.00
46.79
Pixtral-large-latest
94.46
96.32
0.00
8.18
52.84
97.75
63.33
64.05
73.49
63.45
93.51
71.25
0.00
0.00
88.28
80.69
77.25
86.55
82.75
72.32
43.06
80.13
55.56
0.00
66.67
QwQ-32B (Γ)
91.14
51.64
50.00
18.85
21.19
71.91
40.00
38.63
72.16
40.75
83.12
61.75
0.00
17.70
78.64
58.34
24.45
22.81
44.00
60.86
25.00
53.81
50.37
0.32
46.01
Qwen2.5-0.5B-it
47.87
47.39
50.00
4.88
25.97
50.00
30.00
32.70
36.88
31.50
50.65
51.25
0.00
9.98
46.69
37.97
10.99
8.19
15.88
15.43
31.94
49.87
49.46
0.00
32.97
Qwen2.5-0.5B
51.68
47.58
50.00
3.93
47.76
51.69
23.33
33.82
37.40
34.55
54.55
49.85
0.00
12.05
48.39
62.95
9.41
11.11
44.88
22.36
29.17
49.48
50.03
0.00
33.41
Qwen2.5-1.5B-it
47.88
49.81
0.00
1.56
25.67
49.44
30.00
32.17
21.08
32.00
46.75
48.60
26.04
1.56
48.39
59.70
14.94
18.13
39.62
55.65
25.00
50.45
49.93
0.00
33.57
Qwen2.5-1.5B
47.69
49.81
5.50
11.83
29.25
51.69
30.00
32.60
20.53
32.05
61.04
49.00
0.00
66.69
48.96
51.03
13.73
16.37
39.75
56.87
26.39
49.70
48.23
0.03
33.33
Qwen2.5-14B-it
29.22
71.28
100.00
26.69
29.25
52.81
30.00
42.49
40.39
50.05
92.21
55.05
0.00
23.62
70.51
54.13
33.13
29.82
37.62
48.86
25.00
55.57
50.64
0.00
51.86
Qwen2.5-14B
84.36
78.34
2.75
12.49
28.96
55.06
26.67
36.69
55.24
42.15
48.05
46.75
1.04
7.76
48.58
56.59
34.79
45.61
54.00
55.93
27.78
48.87
47.82
0.13
48.28
Qwen2.5-32B-it
52.94
58.80
1.25
25.08
17.31
46.07
30.00
32.70
61.21
34.90
63.64
61.30
1.04
20.72
53.31
65.00
39.02
38.60
38.38
53.55
38.89
38.67
47.93
3.43
40.06
Qwen2.5-32B
72.93
85.01
4.75
18.32
31.04
47.75
33.33
38.61
67.96
44.10
46.75
53.30
2.08
16.15
58.60
54.84
48.50
53.22
28.00
59.74
22.22
54.85
51.41
1.60
34.57
Qwen2.5-3B-it
59.98
50.97
1.25
5.43
28.96
49.44
30.00
33.46
40.15
32.55
45.45
49.25
1.04
4.35
51.98
44.18
11.74
12.87
39.50
56.75
22.22
50.59
50.80
0.00
33.21
Qwen2.5-3B
45.87
48.74
25.00
5.11
34.93
44.38
30.00
33.03
21.19
31.65
51.95
47.95
1.04
5.82
52.93
54.92
15.43
19.88
39.38
31.13
27.78
50.66
49.97
0.06
33.11
Qwen2.5-7B-it
55.43
50.48
1.25
4.82
45.97
52.81
53.33
37.13
70.32
41.50
57.14
54.95
52.08
5.12
52.74
64.71
15.95
15.20
59.62
36.59
36.11
51.66
50.00
0.45
39.46
Qwen2.5-7B
84.19
61.80
2.50
7.77
44.18
51.12
50.00
40.00
62.92
43.65
61.04
49.05
1.04
7.29
49.53
46.25
13.10
23.39
56.88
58.19
34.72
49.37
50.80
0.13
45.69
Qwen-max
42.77
67.89
15.50
46.81
46.87
65.17
50.00
56.88
48.98
61.25
70.13
60.45
10.68
36.18
56.52
26.95
67.80
70.76
70.75
63.13
27.78
41.39
31.33
35.25
57.23
Qwen3-14B-Base
92.94
52.42
1.50
15.52
62.69
54.49
26.67
45.82
69.78
53.30
54.55
53.00
1.82
16.55
64.46
66.09
57.39
50.88
49.12
30.55
31.94
51.81
49.46
0.48
58.90
Qwen3-14B
86.94
61.80
25.00
19.85
55.82
56.74
30.00
54.20
72.32
60.80
48.05
55.25
26.04
17.96
57.28
42.49
33.48
28.07
56.62
40.38
30.56
57.79
50.54
0.70
60.68
RandomBaselineModel
50.44
50.00
0.00
0.00
30.15
55.62
26.67
33.52
33.60
34.20
51.95
50.80
0.00
6.51
49.15
49.46
9.93
12.28
34.12
33.31
30.56
49.98
48.96
5.00
34.29
Reka-flash-3 (Γ)
79.38
53.09
0.00
9.39
39.10
54.49
23.33
44.35
54.23
48.05
49.35
54.45
26.04
9.54
55.01
60.12
10.32
11.70
54.00
45.52
31.94
52.85
50.44
0.00
52.50
S1.1-32B (Γ)
58.42
49.81
0.00
16.74
28.06
52.81
40.00
43.67
63.10
50.55
55.84
54.65
26.04
16.44
60.30
55.00
47.20
56.14
69.50
45.56
22.22
55.21
49.87
0.00
46.09
SmolLM2-1.7B-it
47.84
48.55
25.00
1.23
53.13
47.19
33.33
35.19
29.71
34.75
49.35
49.40
0.00
18.34
48.77
54.29
9.76
11.11
44.38
47.88
22.22
51.63
50.17
0.00
33.23
SmolLM2-1.7B
46.94
49.71
0.00
47.06
28.96
46.63
30.00
32.56
20.53
32.10
55.84
44.65
0.00
16.34
53.31
63.31
9.37
9.94
39.75
56.89
23.61
49.41
50.27
0.00
37.15
SmolLM2-135M-it
48.12
49.71
0.00
18.15
16.42
42.13
30.00
32.45
30.53
32.35
42.86
50.60
0.00
5.60
50.85
64.14
9.37
9.36
22.38
26.89
29.17
50.98
50.03
0.00
33.99
SmolLM2-135M
48.09
50.00
0.00
22.88
11.34
47.19
26.67
32.78
39.14
33.15
50.65
53.95
0.00
2.15
52.17
34.73
10.25
9.36
12.38
14.51
26.39
49.59
49.16
0.00
33.07
SmolLM2-360M-it
49.65
53.29
0.00
14.73
31.34
44.38
16.67
33.58
38.86
33.75
46.75
50.50
0.00
12.85
50.66
31.95
9.41
12.87
21.38
18.00
22.22
48.69
50.44
0.00
35.45
SmolLM2-360M
47.58
50.58
0.00
15.59
35.82
50.56
16.67
33.84
29.65
33.35
57.14
54.70
0.00
6.78
51.23
34.32
11.37
7.60
31.75
16.02
27.78
50.41
49.97
0.00
32.97
o1-2024-12-17 (Γ)
96.02
97.39
0.00
0.00
45.07
97.19
63.33
66.95
75.65
67.30
100.00
78.20
0.00
0.00
91.49
84.00
85.41
95.91
87.25
83.92
45.83
91.98
88.69
0.00
67.49
o1-mini-2024-09-12 (Γ)
95.22
94.49
8.00
40.05
37.91
93.82
60.00
56.88
74.48
57.20
96.10
76.85
6.77
31.60
87.71
80.28
70.49
77.78
80.88
81.10
44.44
85.54
76.61
38.77
58.06
o3-2025-04-16 (Γ)
96.97
97.00
0.00
0.00
45.07
94.94
56.67
62.46
75.47
63.45
98.70
79.30
0.00
0.00
91.49
85.33
86.01
95.91
87.00
82.65
52.78
92.70
89.46
0.00
70.50
o3-mini-2025-01-31 (Γ)
95.38
96.81
9.50
43.04
56.12
94.38
73.33
66.14
74.67
68.20
98.70
80.00
8.59
33.92
89.22
80.82
76.97
87.72
80.75
79.70
50.00
87.54
81.12
40.60
71.22
Table 4: Performance of all 95 LLM across COLE tasks. Scores are reported in accuracy (Acc.), exact match (EM),
and F1-score, all as percentages (%).

--- Page 19 ---

≪system≫Judge whether this sentence is grammatically correct. An-
swer only with 1 if the sentence is grammatically correct, 0 otherwise.
≪user≫{sentence 0}
{sentence 1}
The answer is: {input}.
(a) QFrCoLA
≪system≫To what extent are the following two sentences similar?
Give an integer score from 1 to 4. Answer only with an integer be-
tween 1 (no similarity) and 4(perfect equivalence).
≪user≫{sentence 1}
{sentence 2}
The answer is: {input}.
(b) STS22
≪system≫What is the relationship of the second sentence with respect to
the first?
0 — if the second sentence entails the first,
1 — if the relation is neutral,
2 — if there is a contradiction.
Answer only with 0, 1, or 2.
≪user≫Sentence 1: {premise}
Sentence 2: {hypothesis}
The answer is: {input}.
(c) FraCaS, GQNLI-Fr, LingNLI-Fr, MNLI-9/11-Fr, RTE3-Fr,
SICK-Fr, XNLI-Fr
≪system≫Determine the relationship between the following two
sentences. Reply only with:
0 — if the sentences are compatible (they convey the same information
or are coherent),
1 — if the two sentences contradict each other.
Answer only with 0 or 1.
≪user≫{sentence 0}
{sentence 1}
The answer is: {input}.
(d) DACCORD
≪system≫Do the following two sentences mean the same thing?
Answer only with 1 if the two sentences have the same meaning, 0
otherwise.
≪user≫{sentence 1}
{sentence 2}
The answer is: {input}.
(e) PAWS-X
≪system≫What does the Quebec “{expression}” mean? Answer
only with the index (starting at zero) of the correct definition. For ex-
ample, if the third one is correct, answer 2.
≪user≫Here is a list of possible definitions:{definitions}
The answer is: {input}.
(f) QFrCoRE
≪system≫Which of the following two sentences is grammatically correct?
- Answer 0 if sentence 0 is correct.
- Answer 1 if sentence 1 is correct.
Respond only with 0 or 1.
≪user≫Sentence 0: {sentence_a}
Sentence 1: {sentence_b}
The answer is: {input}.
(g) QFrBLiMP, MultiBLiMP-Fr
≪system≫What is the sentiment of this sentence?
Answer only with:
0 — if the sentence is negative,
1 — if the sentence is neutral,
2 — if the sentence is positive.
Respond only with 0,1 or 2.
≪user≫{sentence}
The answer is: {input}.
(h) MMS-Fr
≪system≫Here is a sentence in English containing the pronoun "it" in an
ambiguous sense, along with its French translation.
≪user≫Sentence: {sentence}
French version (replace by “_”): {context}
Options:
1 — {option1}
2 — {option2}
The answer is: {input}.
(i) Wino-X-LM
≪system≫Here are two French translations of an English sentence with
an ambiguous pronoun. Which one uses the correct pronoun based on the
original sentence? Respond only with 1 or 2.
≪user≫Original sentence: {sentence}
Translation 1 (with “{pronoun1}”): {translation1}
Translation 2 (with “{pronoun2}”): {translation2}
The answer is: {input}.
(j) Wino-X-MT
≪system≫You will receive a sentence containing an ambiguous word along
with the part-of-speech (PoS) tags for each word in the sentence. The ambigu-
ous word can be either a verb or an adjective. Your task is to indicate exactly
this ambiguous word in the sentence, without adding or rephrasing anything.
Respond only with the identified ambiguous word.
≪user≫{sentence}
{pos_tag_labels}.
The answer is:
(k) WSD-Fr
≪system≫You will be given a context followed by a question.
Your task is to extract **verbatim** the span of text from the context that
best answers the question.
Do not invent anything. Do not rephrase.
Only respond by copying an exact excerpt from the context above.
Respond only with a passage extracted from the context. ≪user≫Context:
{context}
Question: {question}
The answer is: {input}.
(l) FQuAD, PIAF
≪system≫Read the passage and answer the question using only the infor-
mation from the text.
- If the passage allows you to answer “yes”, respond with 1.
- If the passage only allows you to answer “no” or doesn’t answer the ques-
tion, respond with 0.
≪user≫Passage: {passage}
Question: {question}
The answer is: {input}.
(m) Fr-BoolQ
≪system≫What is the sentiment of this sentence?
Answer only with:
0 — if the sentence is negative,
1 — if the sentence is positive,
Respond only with 0 or 1
≪user≫{sentence}
The answer is: {input}.
(n) Allocine
≪system≫What does the Quebec “{term}” mean? Answer only with
the index (starting at zero) of the correct definition.
≪user≫Here is a list of possible definitions:{definitions}
The answer is: {input}.
(o) QFrCoRT
Figure 2: The translated prompt templates used for the zero-shot evaluation of each task in the COLE benchmark.
Each prompt consists of a system message providing the instruction and a user message containing the input
placeholder for the data instance. Blue boxes contain the task instructions. Yellow boxes contain the prefix for the
model to continue. Texts in “≪≫” are role-tags to be fed to the model.

```
