---
title: "2023-Vries-DUMB A Benchmark for Smart Evaluation of Dutch Models - PDF Extract"
source_pdf: "2023-Vries-DUMB A Benchmark for Smart Evaluation of Dutch Models.pdf"
pages: 21
extracted_at: "2026-02-13T13:13:45.548766"
---

# PDF Extract: 2023-Vries-DUMB A Benchmark for Smart Evaluation of Dutch Models

**Source PDF:** 2023-Vries-DUMB A Benchmark for Smart Evaluation of Dutch Models.pdf
**Total Pages:** 21

---

## Content

```
--- Page 1 ---

arXiv:2305.13026v2  [cs.CL]  13 Oct 2023
DUMB: A Benchmark for Smart Evaluation of Dutch Models
Wietse de Vries
University of Groningen
The Netherlands
wietse.de.vries@rug.nl
Martijn Wieling
University of Groningen
The Netherlands
m.b.wieling@rug.nl
Malvina Nissim
University of Groningen
The Netherlands
m.nissim@rug.nl
Abstract
We introduce the Dutch Model Benchmark:
DUMB. The benchmark includes a diverse
set of datasets for low-, medium- and high-
resource tasks.
The total set of nine tasks
includes four tasks that were previously not
available in Dutch.
Instead of relying on a
mean score across tasks, we propose Rela-
tive Error Reduction (RER), which compares
the DUMB performance of language models
to a strong baseline which can be referred to
in the future even when assessing different
sets of language models. Through a compari-
son of 14 pre-trained language models (mono-
and multi-lingual, of varying sizes), we as-
sess the internal consistency of the bench-
mark tasks, as well as the factors that likely
enable high performance.
Our results in-
dicate that current Dutch monolingual mod-
els under-perform and suggest training larger
Dutch models with other architectures and pre-
training objectives.
At present, the highest
performance is achieved by DeBERTaV3large,
XLM-Rlarge and mDeBERTaV3base. In addi-
tion to highlighting best strategies for training
larger Dutch models, DUMB will foster fur-
ther research on Dutch. A public leaderboard
is available at dumbench.nl.
1
Introduction
To evaluate and compare new and existing lan-
guage models, a reliable method of comparing
model quality is essential. For this reason, several
benchmark suites have been proposed, such as En-
glish GLUE (Wang et al., 2018) and SuperGLUE
(Wang et al., 2019). However, at present, there is
no standard benchmark for Dutch.
The currently available Dutch language mod-
els are BERTje (de Vries et al., 2019), which
is a Dutch version of BERTbase (Devlin et al.,
2019a), and three versions of RobBERT (Delo-
belle et al., 2020, 2022b) which are Dutch versions
of RoBERTabase (Liu et al., 2019). Direct com-
parisons between these models have focused on
several tasks: sentiment analysis, natural language
inference, coarse-grained part-of-speech tagging
and three-class named entity recognition, where
RobBERT often outperforms BERTje (Delobelle
et al., 2022b).
Results are not completely con-
sistent, however. Some studies found that Rob-
BERT performs better than BERTje at speciﬁc
tasks (Ruitenbeek et al., 2022; Delobelle et al.,
2022b; De Bruyne et al., 2021), whereas other
studies ﬁnd the opposite (Wijnholds and Moortgat,
2021; De Langhe et al., 2022). Other works as-
sume higher performance for speciﬁc models and
either exclusively experiment with BERTje (Alam
et al., 2021; Ghaddar et al., 2021; Brandsen et al.,
2022), or exclusively experiment with RobBERT
(Spruit et al., 2022; Delobelle et al., 2022a).
By developing a new benchmark, we aim to re-
duce the present unclarity of current evaluations
and obtain insights into potential performance im-
provements for future development of new Dutch
models. We also hope that this work will foster
further research on Dutch, including the develop-
ment of decoder-based models. Indeed, we see the
establishment of such a benchmark, together with
the evaluation of existing encoder-based models,
as a necessary step towards making it possible to
also devise a solid evaluation framework for gen-
erative models, which is complicated by the high
degree of variability related to prompts and out-
puts.
Contributions
• We
create
a
balanced
Dutch
benchmark
(DUMB) of nine tasks, including four which
were previously unavailable.
• We propose using a Relative Error Reduction
(RER) metric to compare relative model perfor-
mance across tasks.
• We assess the current state of Dutch language
modeling, also through comparison against mul-
tilingual and English models.

--- Page 2 ---

• We identify and quantify limitations of current
Dutch models and propose directions for poten-
tial developments.
Other Benchmarks
Various monolingual and multilingual bench-
marks exist. For English, the two standard bench-
marks are GLUE (Wang et al., 2018) and Super-
GLUE (Wang et al., 2019). Four of the nine tasks
in GLUE are comparable Natural Language Infer-
ence (NLI) tasks, and three of the remaining tasks
are semantic similarity tasks. SuperGLUE has a
focus on Question Answering (QA), with 4 of the
8 tasks being QA tasks.
Multiple efforts exist to make GLUE-like
benchmarks for other languages, such as (Chi-
nese) CLUE (Xu et al., 2020), BasqueGLUE (Ur-
bizu et al., 2022), RussianSuperGLUE (Shavrina
et al., 2020), (Korean) KLUE (Park et al., 2021),
(French) FLUE (Le et al., 2020), (Japanese)
JGLUE (Kurihara et al., 2022), (Indonesian) In-
doNLU (Wilie et al., 2020) and (Arabic) ORCA
(Elmadany et al., 2022). These benchmarks con-
tain varying numbers of tasks relating to, for
instance, NLI, QA, Semantic Textual Similarity
(STS), Word Sense Disambiguation (WSD). All
monolingual benchmarks use the mean task score
as an aggregate measure.
We discuss in Sec-
tion 3.3 why this might not be optimal, and sug-
gest an alternative approach for comparative eval-
uation. Reported baseline experiments sometimes
include only monolingual models of the target lan-
guage (Park et al., 2021; Urbizu et al., 2022; El-
madany et al., 2022). For other benchmarks, base-
sized multilingual models (Shavrina et al., 2020)
or base- and large-sized multilingual models are
included as well (Kurihara et al., 2022; Wilie et al.,
2020). For the latter two studies, the large multi-
lingual models outperform the (base-sized) mono-
lingual models.
Multilingual benchmarks have also been pro-
posed. XGLUE (Liang et al., 2020), XTREME
(Hu et al., 2020) and XTREME-R (Ruder et al.,
2021) cover 19, 40 and 50 languages, respectively.
Dutch is included in these benchmarks, but only
for coarse-grained Universal Dependencies Part-
Of-Speech (POS) tagging (Zeman et al., 2022) and
automatically generated WikiANN Named Entity
Recognition (Pan et al., 2017). These multilingual
benchmarks only contain English training data,
and are therefore tailored to evaluate cross-lingual
transfer rather than monolingual performance.
Task
Dataset
M.
C.
|Train|
|Dev|
|Test|
POS
Lassy
acc.
218
59,167
1,814
4,184
NER
SoNaR-1
F1
7
54,472
1,392
4,080
WSD
WiC-NL
acc.
2
7,184
1,330
1,330
PR
DPR
acc.
2
786
142
1,216
CR
COPA-NL
acc.
2
400
100
500
NLI
SICK-NL
acc.
3
4,439
495
4,906
SA
DBRD
acc.
2
19,528
500
2,224
ALD
DALC
F1
3
6,817
1,205
3,270
QA
SQuAD-NL
F1
-
130,319
10,174
1,699
Table 1:
The nine DUMB tasks and their evaluation
Metrics, number of Classes, and split sizes. Underlined
datasets (WSD, PR, CR, QA) and splits (POS, NER,
WSD, SA, QA) are newly introduced in this paper.
2
DUMB Tasks
A general language model should be able to per-
form well at different types of tasks.
There-
fore, we balance our benchmark to contain word-
level, word-pair-level, sentence-pair level and
document-level tasks. Moreover, we include tasks
having different orders of magnitude of training
items.
We call these low-resource (102), mid-
resource (103), and high-resource (>104) tasks.
All included datasets are freely available and
most source datasets use permissive licenses that
allow (modiﬁed) redistribution. We do however
not currently share the pre-processed benchmark
directly because of licensing restrictions of some
datasets. Simple instructions to download these
datasets and a single pre-processing script are
available on our Github so that the entire bench-
mark can be obtained.
The included tasks are
listed in Table 1 and described below. Appendix A
contains example items for each task.
2.1
Word Tasks
Word tasks involve classifying or tagging individ-
ual words. The surrounding sentence can be used
to determine lexicosemantic classes for individual
(compound) words.
Part-Of-Speech Tagging (POS)
We use the
ﬁne-grained POS annotations from the Lassy
Small v6.0 corpus (van Noord et al., 2013). The
corpus permits non-commercial use (custom li-
cense). This data was annotated using the Corpus
Gesproken Nederlands (CGN) guidelines that de-
ﬁne 316 distinct morphosyntactic tags (van Eynde,
2004), of which 218 tags are used in the Lassy cor-
pus.

--- Page 3 ---

The source corpus contains documents from
magazines, newsletters, web pages, Wikipedia,
press releases, novels, brochures, manuals, legal
texts and reports. Only the Wikipedia section of
this corpus is included in Universal Dependencies
(Zeman et al., 2022). For our benchmark, we in-
troduce document-level random cross validation
splits. We reserve 2% of documents as develop-
ment data, 5% as test data and the remaining 93%
as training data. We selected the random seed such
that all 218 classes appear in the training data.
Named Entity Recognition (NER)
For NER,
we use the SoNaR-1 v1.2.2 corpus (Oostdijk et al.,
2013). The corpus permits non-commercial use
(custom license). In addition to the person, organi-
zation, location and miscellaneous entity types of
CoNLL-2002 (Tjong Kim Sang, 2002), SoNaR-1
contains separate classes for products and events,
resulting in 6 entity classes and a negative class.
The SoNaR-1 source data largely overlaps with
the POS source data described in the previous sec-
tion and contains the same domains. Cross valida-
tion splits were made in identical fashion. To facil-
itate transfer or multi-task learning, we ensure that
documents that have annotations for both tasks are
in the same splits for both tasks.
2.2
Word Pair Tasks
Word pair tasks involve comparison of words or
small clusters of words. These tasks are speciﬁ-
cally designed to test disambiguation.
Word Sense Disambiguation (WSD)
As our
Word Sense Disambiguation (WSD) task, we
replicate the English Words in Context (WiC; Pile-
hvar and Camacho-Collados, 2019) task.
WiC
items contain two sentences from different con-
texts that contain the same target word. The task
is a binary classiﬁcation task to determine whether
the words share the same sense in both sentences.
For English WiC, the word senses of WordNet
(Miller, 1994) are used to determine sense equiv-
alence (Pilehvar and Camacho-Collados, 2019).
The used sentences were extracted from WordNet,
VerbNet (Kipper Schuler et al., 2009) and Wik-
tionary. This English task is included in the Super-
GLUE benchmark (Wang et al., 2019). A multi-
lingual version of WiC, XL-WiC (Raganato et al.,
2020), has been constructed based on WordNet
and Wiktionary in other languages. This dataset
contains Dutch test data that has been extracted
from Open Dutch WordNet (Postma et al., 2016),
but it is lacking Dutch training data.
To replicate WiC and XL-WiC for Dutch (WiC-
NL), we use the sense-tagged data from Dutch-
SemCor (Vossen et al., 2012). The source dataset
allows modiﬁcation and redistribution (CC-BY
3.0).
DutchSemCor provides Cornetto (Vossen
et al., 2008) word sense annotations for docu-
ments from the SoNaR-500 corpus (Oostdijk et al.,
2013). We extract and group sentences by POS tag
(adjectives, nouns and verbs), lemmas and word
senses. For each lemma, we randomly select an
equal number of positive and negative pairs of sen-
tences, where the word sense is either the same
or different. Note that we do this by lemma, so
the target word may have different morphology in
the two sentences. For cross validation, we split
our dataset by lemma, so none of the words in the
test data have been seen during training. The same
lemma appears at most six times in training and
four times in development and test data. The de-
velopment and test data each contain 15% of the
total set of lemmas.
The ﬁnal dataset contains
1.3K development and test items and 7.2K train
items. This size is similar to English WiC (5.4K
train, 0.6K development and 1.4K test).
As positive and negative classes are balanced,
majority and random performance is 50%. State-
of-the-art English WiC accuracy is 77.9% (T5 +
UDG; Wang et al., 2021) and the highest cross-
lingual Dutch XL-WiC accuracy is 72.8 (XLM-
Rlarge; Raganato et al., 2020). We expect WiC-NL
performance at a similar order of magnitude.
Pronoun Resolution (PR)
Similar to the Wino-
grad Schema Challenge (Levesque et al., 2012)
that is included in SuperGLUE, we include a pro-
noun resolution task in our benchmark. We use
coreference annotations from SemEval2010 Task
1 (Recasens et al., 2010) as source data to con-
struct a Dutch Pronoun Resolution (DPR) dataset.
The dataset permits non-commercial use (custom
license). We do not directly redistribute the data,
but do automate pre-processing. We cast this task
as a balanced binary classiﬁcation with one or two
sentences as input. In the input, a pronoun and a
non-pronoun entity are marked and the task is to
determine whether the pronoun refers to the en-
tity. Entities in negative samples always refer to a
different entity or pronoun.
Cross validation splits are taken from the source
SemEval data. The ﬁnal dataset contains only 768

--- Page 4 ---

training items, which makes this task relatively
low-resource. Positive and negative cases are bal-
anced, so majority and random accuracy is 50%.
2.3
Sentence Pair Tasks
Sentence pair tasks test whether models recognize
semantic relationships between sentences. Specif-
ically, we test temporal causal relationships and
entailment relationships.
Causal Reasoning (CR)
We have translated the
Choice of Plausible Alternatives (COPA; Gordon
et al., 2012) dataset to Dutch (COPA-NL). COPA
is distributed under the 2-Clause BSD License
and permits modiﬁed redistribution. In this causal
reasoning task, one of two causally related sen-
tences has to be selected based on a premise. We
used Google Translate (Nov. 2022) to translate all
items, and manually corrected translation errors
for the entire dataset in two passes: (i) we checked
that individual sentences were correct translations,
and (ii) we assessed the coherence of sentence
pairs and corresponding labels.
The train, dev and test splits are 400, 100 and
500 items, respectively. Due to the limited training
data size, English models typically use auxiliary
training data such as the Social IQa dataset (Sap
et al., 2019). With auxiliary data, English COPA
accuracy can reach 98.4% (He et al., 2021). In our
experiments, we will not use any auxiliary data, so
performance is expected to be lower. XCOPA, a
translation of COPA in 11 other languages (Ponti
et al., 2020), can reach 55.6% average accuracy
over all languages and 69.1% when using auxiliary
training data (XLM-R; Conneau et al., 2020).
Natural Language Inference (NLI)
We use
SICK-NL (Wijnholds and Moortgat, 2021) for
NLI, a Dutch translation of SICK (Marelli et al.,
2014), distributed under the permissive MIT li-
cense. This is a three-class NLI sentence pair clas-
siﬁcation task (entailment, contradiction, neutral).
SICK also includes human judgements of seman-
tic textual similarity (STS), but this task is not part
of DUMB in order to preserve task type balance.
For SICK-NL, accuracies up to 84.9% have been
reported (RobBERT2022; Delobelle et al., 2022b).
2.4
Document Tasks
Document tasks involve classiﬁcation of a multi-
sentence text and extractive question answering.
Sentiment Analysis (SA)
We use the Dutch
Book Reviews Dataset v3.0 (DBRD; Van der
Burgh and Verberne, 2019), which is distributed
with the permissive MIT license.
This task in-
volves classifying a book review as positive or
negative. We remove 500 reviews from the train-
ing set to use for development, since the original
data is missing a dev set. The highest previously
reported accuracy on this task (with original splits)
is 95.1% (RobBERT2022; Delobelle et al., 2022b).
Abusive Language Detection (ALD)
We in-
clude an abusive language detection task based
on DALC v2.0 (Ruitenbeek et al., 2022), which
is distributed with the permissive GPLv3 license.
This dataset contains annotations for anonymized
abusive and offensive Twitter messages. The spe-
ciﬁc task we include is a three-way classiﬁcation
of abusive, offensive or neutral tweets. The high-
est previously achieved macro F1 score of this task
is 63.7% (RobBERTV2; Ruitenbeek et al., 2022).
Question
Answering
(QA)
We
translated
SQuAD2.0 (Rajpurkar et al., 2016, 2018) to
Dutch using Google Translate (Feb. 2023) with
post-editing.
SQuAD-NL consists of Wikipedia
paragraphs and questions for which the answer
can be found in the context paragraph.
Unan-
swerable questions are also included.
As the
original SQuAD test-data is not public, we use
the same 240 paragraphs that were selected in
XQuAD (Artetxe et al., 2020) as test data, and
the remaining 1,827 paragraphs are used as our
development data.
The test data was manually
corrected by eight BSc students as part of their
thesis work.
For SQuAD-NL we use the same
license of the original dataset (CC-BY-SA 4.0).
We also distribute SQuAD-NL version 1.1, which
does not contain unanswerable questions.
3
Evaluation
We conduct an analysis of several pre-trained lan-
guage models (PLMs) with DUMB. The goal of
this analysis is to identify strengths and limitations
of current Dutch language models, as well as to
determine the overall effectiveness of the proposed
benchmark. We evaluate the inﬂuence of model
variants, model sizes and pre-training languages.
3.1
Pre-trained Language Models
The model types we include in our evaluation in-
clude three Transformer-encoder (Vaswani et al.,

--- Page 5 ---

2017) variants, namely BERT (Devlin et al.,
2019a), RoBERTa (Liu et al., 2019) and DeBER-
TaV3 (He et al., 2023). For each model, we ﬁne-
tune the base model size and the large model size,
if available. Models with the base and large model
sizes have 85M and 302M trainable parameters
in their Transformer-encoder layers, respectively.
Due to varying vocabulary sizes, the total word
embedding layers vary in size.
All currently available Dutch monolingual lan-
guage models are included in our experiments, as
well as their multilingual equivalents. Dutch is in-
cluded in the set of pre-training languages of each
multilingual model. We also include the mono-
lingual English model variants since they have
been shown to transfer well to non-English lan-
guages (Artetxe et al., 2020; Blevins and Zettle-
moyer, 2022).
Language models can in gen-
eral transfer well to other languages through ei-
ther cross-lingual ﬁne-tuning a multilingual model
(de Vries et al., 2022), or through various con-
tinual pre-training approaches (Gogoulou et al.,
2022; de Vries and Nissim, 2021; Li et al., 2021).
However, monolingual English models can also
perform well on non-English languages by merely
ﬁne-tuning in the target language (Blevins and
Zettlemoyer, 2022). Monolingual transfer effec-
tiveness is facilitated by language contamination
during pre-training, which is higher for RoBERTa
than for BERT (Blevins and Zettlemoyer, 2022).
As BERT-type models, we take English BERT
(Devlin et al., 2019a), cased multilingual BERT
(mBERT; Devlin et al., 2019b) and Dutch BERTje
(de Vries et al., 2019). These are all pre-trained
on curated data with Masked Language Modeling
(MLM) and the Next Sentence Prediction (NSP)
or Sentence Order Prediction (SOP) objectives.
These models are the ﬁrst published English, mul-
tilingual and Dutch language models, respectively.
A large variant is only available for English.
As RoBERTa-type models, we include English
RoBERTa (Liu et al., 2019), multilingual XLM-
RoBERTa (XLM-R; Conneau et al., 2020) and
three versions of RobBERT (Delobelle et al.,
2020, 2022b). These models are pre-trained with
only the MLM objective, and their pre-training
datasets have larger sizes and lower curation due
to the inclusion of web scraped data. The Dutch
RobBERTV1 and RobBERTV2 models are trained
with the OSCAR 2019 corpus (Ortiz Suárez et al.,
2020); the ﬁrst version used the original English
byte-pair-encoding vocabulary, while the second
used a new Dutch vocabulary. The RobBERT2022
update is trained with the same procedure as V2,
but with the larger OSCAR 22.01 corpus (Abadji
et al., 2022). Large model variants are only avail-
able for English and multilingual RoBERTa.
As DeBERTaV3-type models, we include En-
glish DeBERTaV3 (He et al., 2023) and multilin-
gual mDeBERTaV3 (He et al., 2023). DeBER-
TaV3 primarily differs from BERT and RoBERTa
by disentangling content and position embed-
dings (He et al., 2021).
Moreover, DeBER-
TaV3 and mDeBERTaV3 are pre-trained with an
ELECTRA-style (Clark et al., 2020) generator-
discriminator training with gradient-disentangled
word embeddings (He et al., 2023).
DeBER-
TaV3 and mDeBERTaV3 outperform RoBERTa
and XLM-RoBERTa on GLUE (Wang et al., 2018)
and XNLI (Conneau et al., 2018), respectively, de-
spite being pre-trained with the same data. A large
model variant is only available for English.
3.2
Fine-tuning Procedure
Our benchmark contains several types of tasks re-
quiring different implementations. Reference im-
plementations in the Hugging Face Transformers
library for each task can be found in our reposi-
tory.1 Speciﬁcally, we provide an implementation
for token classiﬁcation (POS, NER), span clas-
siﬁcation (WSD, PR), multiple choice (CR), se-
quence classiﬁcation (NLI, SA, ALD), and extrac-
tive question answering (QA).
We ﬁne-tune each of the pre-trained models on
the tasks with individual hyper-parameter grid-
searches for each model and task. Optimal hyper-
parameters are chosen based on validation data,
and differ between models and tasks.
We opti-
mize numbers of epochs, warm-up steps, learn-
ing rate and dropout. After the hyper-parameter
search, we rerun ﬁne-tuning with 5 different ran-
dom seeds. Reported scores are average test data
performance of those 5 runs. Grid search ranges,
optimal hyper-parameters, and training durations
are in Appendix B. In our baseline experiments,
we ﬁne-tune the pre-trained models on the bench-
mark task training data without exploring transfer
from similar tasks or special sampling techniques.
1github.com/wietsedv/dumb/tree/main/trainers

--- Page 6 ---

Word
Word Pair
Sentence Pair
Document
Avg
POS
NER
WSD
PR
CR
NLI
SA
ALD
QA
Model
RER
RER
Acc.
RER
F1
RER
Acc.
RER
Acc.
RER
Acc.
RER
Acc.
RER
Acc.
RER
F1
RER
F1
BERTje
0
0
97.8
0
86.1
0
65.9
0
65.8
0
62.0
0
85.2
0
93.3
0
58.8
0
70.3
RobBERTV1
-16.3
12.5
98.1
-19.4
83.5
-15.3
60.6
-24.0
57.6
-14.7
56.4
-12.7
83.3
-58.2
89.4
4.8
60.8
-19.4
64.6
RobBERTV2
1.6
16.2
98.2
4.1
86.7
-5.3
64.1
0.1
65.8
-10.2
58.1
-3.8
84.6
-0.5
93.2
12.0
63.7
2.2
71.0
RobBERT2022
3.6
17.3
98.2
7.6
87.2
-6.4
63.7
-1.8
65.2
-10.1
58.2
3.1
85.6
4.0
93.5
18.9
66.6
-0.2
70.3
mBERTcased
-5.8
6.2
97.9
9.2
87.4
7.7
68.5
-11.0
62.0
-18.4
55.0
-6.2
84.3
-41.7
90.5
-4.5
56.9
6.9
72.4
XLM-Rbase
-0.3
13.9
98.1
10.8
87.6
1.9
66.5
-16.2
60.2
-26.8
51.8
2.0
85.5
-3.6
93.0
3.4
60.2
12.3
74.0
mDeBERTaV3base
12.8
18.2
98.2
17.2
88.5
10.8
69.6
-20.8
58.7
19.7
69.5
25.2
88.9
3.3
93.5
12.4
63.9
29.2
79.0
XLM-Rlarge
14.4
26.5
98.4
29.7
90.3
21.3
73.1
-15.8
60.4
-25.8
52.2
24.4
88.8
13.2
94.2
19.0
66.6
37.2
81.4
BERTbase
-42.8
-19.8
97.4
-30.8
81.9
-22.4
58.2
-18.7
59.4
-28.0
51.4
-19.2
82.3
-203.9
79.6
-16.1
52.2
-26.2
62.5
RoBERTabase
-25.6
-6.5
97.7
-27.3
82.3
-14.0
61.1
-20.4
58.8
-24.1
52.8
-19.7
82.3
-99.9
86.6
-16.0
52.2
-2.1
69.7
DeBERTaV3base
-1.6
6.5
97.9
1.7
86.4
-4.2
64.4
-25.3
57.1
-20.5
54.2
8.6
86.5
-14.6
92.3
3.5
60.2
29.7
79.1
BERTlarge
-35.1
-12.0
97.5
-25.9
82.5
-25.4
57.2
-29.3
55.8
-31.2
50.2
-15.4
82.9
-158.7
82.6
-7.8
55.6
-10.4
67.2
RoBERTalarge
-14.1
6.4
97.9
-12.3
84.4
-19.8
59.1
-23.3
57.8
-26.1
52.1
-8.5
83.9
-63.8
89.0
1.2
59.3
19.7
76.2
DeBERTaV3large
15.7
17.9
98.2
10.9
87.6
12.7
70.2
-14.4
60.9
35.4
75.4
24.1
88.7
-6.4
92.8
12.5
64.0
48.4
84.7
Table 2:
Task scores and Relative Error Reduction (RER) scores per model. Models are grouped by pre-train
language and model size. Bold values indicate highest (or not signiﬁcantly different, p ≥0.05) scores per task.
Gray values are signiﬁcantly (p < 0.05) below baseline. Signiﬁcance testing is described in Section 3.3. Updated
results with newer models can be found on dumbench.nl.
3.3
Evaluation Method
We provide a single aggregate score based on
all tasks. In existing benchmarks, the arithmetic
mean score of the different tasks is used, despite
varying metrics and task difﬁculties within the
benchmark (Wang et al., 2018, 2019; Hu et al.,
2020).
This assumes that absolute score differ-
ences are equally meaningful across tasks, which
could be the case if the set of tasks is relatively ho-
mogeneous. However, our set has a high variation
in expected scores with around 95% accuracy on
POS and only 70% on CR. We assume that a single
point improvement for POS (effectively reducing
the error by 20%) would then be more meaning-
ful than a single point improvement on CR (effec-
tively reducing the error by about 3%).
As a solution, we propose to not use the mean
score per model, but the average Relative Error
Reduction (RER) compared to a strong baseline.
For instance if the baseline task performance is
80% and a target model achieves 85%, RER score
is 5%/20% = 25%.
For our baseline model,
we choose the Dutch BERTje model. This is the
ﬁrst Dutch pre-trained language model and is only
available in base size. We argue that any newer
and larger models should outperform this baseline
to be considered useful for practical applications.
To evaluate whether language models do not
signiﬁcantly differ from the best performing
model per task, or perform signiﬁcantly lower than
the baseline model per task, we ﬁt two binomial
mixed effects regression models per task. Correct-
ness of the each item is used as dependent variable
in all cases, and by-item random intercepts are in-
cluded to account for the item-based variability.
The predictor of interest is the model (i.e. a 14-
level nominal variable). The two regression mod-
els per task use the baseline model or the best per-
forming model as reference levels. Consequently,
for each item 70 predictions are included (14 mod-
els times ﬁve runs per model) in all 18 regression
models (two regression models for each task). We
use a signiﬁcance threshold α of 0.05 in evaluat-
ing the p-values distinguishing the performance of
each model from that of the chosen reference level.
POS
NER
WSD
PR
CR
NLI
SA
ALD
QA
POS
-
0.85
0.75
0.31
0.43
0.77
0.89
0.93
0.66
NER
0.85
-
0.92
0.41
0.42
0.88
0.87
0.81
0.75
WSD
0.75
0.92
-
0.35
0.52
0.86
0.77
0.64
0.75
PR
0.31
0.41
0.35
-
0.29
0.15
0.50
0.38
-0.03
CR
0.43
0.42
0.52
0.29
-
0.64
0.48
0.47
0.51
NLI
0.77
0.88
0.86
0.15
0.64
-
0.74
0.79
0.87
SA
0.89
0.87
0.77
0.50
0.48
0.74
-
0.82
0.66
ALD
0.93
0.81
0.64
0.38
0.47
0.79
0.82
-
0.59
QA
0.66
0.75
0.75
-0.03
0.51
0.87
0.66
0.59
-
0.70
0.74
0.70
0.30
0.47
0.71
0.72
0.68
0.59
Table 3:
Correlations between tasks (RER) for the
models in Table 2. Highest correlations per column are
shown in bold and correlations that are not signiﬁcant
(based on 14 values) are shown in gray (p < 0.05).
3.4
Results
Results for each model and task, grouped by pre-
training language and model size, are in Table 2.
For model comparison we consider RER per task
and average RER across tasks as the most im-
portant metrics, but we also report the conven-

--- Page 7 ---

tional metrics for each task. Highest overall per-
formance is achieved by DeBERTaV3large, an En-
glish model. In the following sections we com-
pare performance across tasks and per model, and
discuss patterns regarding model types, sizes and
pre-training languages.
4
Analysis of Tasks
Table 2 shows great variation across tasks, with
baseline scores between 58.8% (ALD) and 97.8%
(POS). Since absolute scores are not comparable
across tasks and metrics, we run a Pearson corre-
lation between RER scores of each pair of tasks
(Table 3) to analyse how tasks relate to each other.
We use cross-task correlations as a sanity check
for our benchmark. Positive correlations are ex-
pected between all tasks and strong correlations
between similar tasks, because all tasks should
achieve higher performance if the Dutch language
is better represented by a model.
The word-
level tasks (POS and NER) and the document-
level tasks (SA and ALD) have strong pairwise
correlations of 0.84 and 0.82, respectively. Corre-
lations above 0.9 are observed between POS and
ALD (0.93), NER and WSD (0.92).
For NER
and WSD this makes sense since both tasks in-
volve analysis of syntactic and semantic informa-
tion of content words. For POS and ALD the re-
sults are less intuitive.
Given the low absolute
scores of ALD (maximum F1 is 66.6), we hy-
pothesize that the language models converge to a
non-optimal solution that relies more on individ-
ual words than on broader context. Moreover, the
correlation between tasks seems more closely re-
lated to the training set sizes than task similarity.
4.1
High- and Low-resource Tasks
The two low-resource tasks (PR, CR) show the
weakest average correlations of 0.30 and 0.47,
which suggests that training sizes might contribute
to model performance differences.
Three high-
resource tasks (POS, NER, SA) strongly corre-
late with each other, with correlations ranging be-
tween 0.85 and 0.89, but these tasks correlate less
strongly with QA, the highest-resource task. Mid-
and high-resource tasks show average correlations
of 0.59 (QA) to 0.74 (NER) and ﬁve of these seven
tasks have correlations of are at least 0.70.
The two low-resource tasks PR and CR do not
correlate with other tasks except for a single sig-
niﬁcant correlation between CR and NLI. This
correlation makes sense, since both tasks involve
evaluating causality between two sentences. CR
is the lowest resource task, and only multilin-
gual mDeBERTaV3 and English DeBERTaV3large
manage to outperform the BERTje baseline. These
two models also perform especially well on the
closely related NLI task, for which they achieve
best performance across models.
Large variants of English BERT and RoBERTa
reach lower PR and CR performance than base
variants (Table 2). Moreover, these two tasks have
the lower RER scores across tasks for multilingual
models (except mBERT SA). This suggests that
non-Dutch PLMs, and especially larger variants
have a disadvantage at low-resource tasks. How-
ever, English and multilingual CR performance is
still high for DeBERTaV3-based models. Rela-
tively stable Dutch monolingual and high DeBER-
TaV3 performances indicate that it is not impossi-
ble to achieve good performance on small datasets.
Since any model could in theory achieve high per-
formance given enough data, we consider it impor-
tant that models generalize well with little data.
High DeBERTaV3 performance can be related
to its pre-training procedure with the ELECTRA-
style objective and Gradient Disentangled Embed-
ding Sharing (GDES). To verify this, we tested
the English DeBERTalarge model, which is not in-
cluded in Table 2 due to lack of a multilingual
variant. This model was pre-trained using Masked
Language Modeling, but is architecturally iden-
tical to DeBERTaV3large. English DeBERTalarge
achieves -33.7 average RER, and -31.6 and 0.0
RER on CR and NLI, as opposed to 35.4 and 24.1
with DeBERTaV3large, suggesting that high cross-
lingual DeBERTaV3 performance is primarily due
to ELECTRA-style pre-training and GDES.
Dutch
Multi
English
base
large
base
large
base
large
BERT
0
4.3 9.6
-5.8
2.8 8.1
-42.8
-35.1
RoBERTa
3.6
13.4 7.8
-0.3
14.4
-25.6
-14.1
DeBERTaV3
24.1 8.1
38.0 10.8
12.8
36.4 8.6
-1.6
15.7
Table 4: Mean RER scores for different model types,
sizes, and pre-training languages. The Dutch RoBERTa
variant is RobBERT2022. Black scores correspond to
the average RER scores in Table 2. Estimated scores
from a linear regression model are shown in gray, with
standard errors as superscripts. Note that standard er-
rors are high, since the estimates are based on only 12
observations.

--- Page 8 ---

5
Analysis of Models
Table 2 shows the results of models of varying
types, sizes, and pre-training languages. Surpris-
ingly, the monolingual English DeBERTaV3large
model
achieves
highest
overall
performance,
mostly thanks to outstanding performance on the
CR and QA tasks. The other two high-performing
models are the multilingual mDeBERTaV3 and
XLM-Rlarge models.
In this section we discuss
how model types, sizes and pre-training languages
compare and why Dutch models are outperformed
by non-Dutch models.
To estimate the effects of pre-train languages,
model types and model sizes, we ﬁt a linear re-
gression model with those variables as predictors
(see Appendix C). A model with all three predic-
tors ﬁts the data signiﬁcantly better than using sin-
gle predictors (model comparison: p < 0.05) and
explains 83.6% of variance (adjusted R2: 73.3%).
All three predictors signiﬁcantly contribute to this
model (p < 0.05); we discuss them in the follow-
ing subsections. Interactions between predictors
did not signiﬁcantly improve the model ﬁt.
The average RER scores are shown in Table 4,
where missing values are estimated by the regres-
sion model. According to this analysis, a Dutch
DeBERTaV3large model could potentially achieve
an error reduction which is more than two times
higher than the current best model (38.0 vs. 15.7).
5.1
Pre-training Language
Dutch monolingual models seem to outperform
equivalent multilingual models and multilingual
models outperform equivalent English models.
According to the regression model, language ac-
counts for a 1.6 point (non-signiﬁcant, p = 0.83)
decrease for multilingual pre-training compared
to Dutch monolingual pre-training and a 28.9
point decrease for English pre-training compared
to Dutch monolingual pre-training. On the basis
of these results, we cannot conclusively claim that
current monolingual Dutch models are preferable
over multilingual models. Table 2 does however
clarify that Dutch models outperform equivalent
multilingual models for all tasks except POS, NER
and QA. Multilingual and English models perform
particularly well on QA.
5.2
Model Type
RoBERTa consistently outperforms BERT, and
DeBERTaV3 consistently outperforms RoBERTa
for every language and model size (Table 4).
The regression model estimates an 9.1 point im-
provement for RoBERTa over BERT. DeBER-
TaV3 shows an additional 24.6 point improve-
ment on RoBERTa, which is nearly double that of
RoBERTa on BERT. Due to the absence of Dutch
DeBERTaV3 models, we cannot be sure whether
monolingual Dutch models would yield this large
improvement. It might be that DeBERTaV3 learns
a particularly good language-independent repre-
sentation, which could boost cross-lingual per-
formance more than monolingual performance.
English experiments on the GLUE benchmark
show the same model performance order, with
GLUE scores of 84.1, 88.8 and 91.4 for BERTlarge,
RoBERTalarge and DeBERTaV3large, respectively
(He et al., 2023). Regardless of the exact improve-
ment, our ﬁndings, and similar results for English
(He et al., 2023), suggest that a Dutch DeBER-
TaV3 would outperform RoBERTa models.
5.3
Model Size
The Dutch monolingual language models are only
available in base model sizes.
However, larger
models perform better, with an estimated 13.9
point improvement for larger models compared to
base-sized models. For XLM-R, the difference is
14.7 points and for the three English model types
the differences are 7.7, 14.5 and 17.3 points. This
shows that larger models perform better for Dutch
regardless of pre-training language.
6
Conclusion
We have introduced DUMB, a benchmark with
nine Dutch language tasks, including four new
tasks and Relative Error Reduction (RER) as a
comparative model evaluation metric. The tasks
are internally consistent with positive correlations
between tasks across models. Some randomness
in low-resource task performance might be due to
model failure of non-Dutch models.
RobBERT models achieve up to 3.6 RER,
but multilingual and even English models can
achieve
up
to
14.4
(XLM-Rlarge)
and
15.7
(DeBERTaV3large) RER, respectively.
Model
comparisons across pre-training languages, model
types and model sizes reveal that high multilin-
gual and English performance on Dutch tasks can
be partially attributed to model size, but to an
even larger extent this can be attributed to the De-
BERTaV3 model type. A Dutch DeBERTaV3large

--- Page 9 ---

model could achieve a substantially higher esti-
mated RER of 38.0. This estimation shows that
there is much room for improving benchmark
scores with better future models. Additionally, we
encourage evaluating large generative models with
DUMB. Our results are based on a robust standard
approach and set a strong baseline that can also be
useful to evaluate effective prompt engineering.
A
public
leaderboard
is
available
at
dumbench.nl and the benchmark and ref-
erence
model
source
code
are
available
at
github.com/wietsedv/dumb. The leader-
board will contain all models discussed in this
paper, and will be kept up-to-date with newer
models and updated versions of the benchmark.
7
Limitations
We claim to create a balanced set of tasks, but we
do not include each and every NLP task type. Our
criterion of balance is about not over-representing
speciﬁc tasks and task categories, not about com-
pleteness. We exclude tasks like parsing and we
simplify tasks to be classiﬁcation tasks, such as
WiC for WSD and PR instead of coreference reso-
lution. This standardises model implementations
and lets us focus on the PLM instead of task-
speciﬁc architectures on top of the PLMs.
Secondly, the proposed comparative evaluation
metric, Relative Error Reduction, can be consid-
ered to not be comparable to aggregate scores of
other benchmarks. However, we argue that aggre-
gate scores can never be compared across bench-
marks with different tasks and datasets.
More-
over, some NLP evaluation metrics such as BLEU
are not directly translatable to Relative Error Re-
duction. This is not a limitation for our bench-
mark, however, since we only include tasks that
have ﬁxed gold labels and therefore use error-
based metrics.
Thirdly, our model comparison only contains
Transformer-encoder models and no generative
language models. Like GLUE, our set of tasks is
suitable for ﬁne-tuning encoder models, whereas
generative models require prompt design. For this
paper and the initial benchmark entries, we aimed
to get robust baseline results with a standard ﬁne-
tuning approach, a hyper-parameter grid-search
and multiple runs.
We believe that such robust
baseline results are necessary to be able to contex-
tualize highly variable prompt-engineering based
approaches.
And ﬁnally, our model comparison contains
more English than Dutch models. We try to show
the effects of several modeling decisions in order
to propose a way forward for Dutch modeling, but
availability of comparable multilingual and Dutch
PLMs is limited. Size and architecture factors may
differ for monolingual Dutch models, but we do
not currently have the models to make that eval-
uation. We speciﬁcally create this benchmark to
motivate further development of Dutch PLMs.
8
Ethics Statement
Our proposed benchmark consists of existing
datasets and derivatives of existing datasets. These
source datasets have been published under various
licenses, as is discussed in Section 2. Moreover,
we list all dataset sources and applicable licenses
in the README of our source code, as well as
the leaderboard website. We made sure that all
datasets are freely available and permit academic
use, though not all permit (modiﬁed) redistribu-
tion. Therefore, we provide a combination of auto-
mated and manual methods for downloading these
datasets from ofﬁcial sources. A single script can
be used to pre-process the data in a deterministic
way to recreate our benchmark.

--- Page 10 ---

References
Julien Abadji, Pedro Ortiz Suarez, Laurent Romary,
and Benoît Sagot. 2022. Towards a cleaner docu-
ment-oriented multilingual crawled corpus.
arXiv
preprint arXiv:2201.06642.
Firoj Alam, Shaden Shaar, Fahim Dalvi, Hassan Saj-
jad, Alex Nikolov, Hamdy Mubarak, Giovanni
Da San Martino, Ahmed Abdelali, Nadir Durrani,
Kareem Darwish, Abdulaziz Al-Homaid, Wajdi Za-
ghouani, Tommaso Caselli, Gijs Danoe, Friso Stolk,
Britt Bruntink, and Preslav Nakov. 2021. Fighting
the COVID-19 infodemic: Modeling the perspective
of journalists, fact-checkers, social media platforms,
policy makers, and the society. In Findings of the
Association for Computational Linguistics: EMNLP
2021, pages 611–649, Punta Cana, Dominican Re-
public. Association for Computational Linguistics.
Mikel Artetxe, Sebastian Ruder, and Dani Yogatama.
2020. On the cross-lingual transferability of mono-
lingual representations. In Proceedings of the 58th
Annual Meeting of the Association for Computa-
tional Linguistics, pages 4623–4637, Online. Asso-
ciation for Computational Linguistics.
Terra Blevins and Luke Zettlemoyer. 2022. Language
contamination helps explains the cross-lingual capa-
bilities of English pretrained models. In Proceed-
ings of the 2022 Conference on Empirical Methods
in Natural Language Processing, pages 3563–3574,
Abu Dhabi, United Arab Emirates. Association for
Computational Linguistics.
Alex Brandsen, Suzan Verberne, Karsten Lambers, and
Milco Wansleeben. 2022. Can BERT dig it? Named
Entity Recognition for information retrieval in the
archaeology domain. J. Comput. Cult. Herit., 15(3).
Kevin Clark, Minh-Thang Luong, Quoc V. Le, and
Christopher D. Manning. 2020. ELECTRA: Pre–
training text encoders as discriminators rather than
generators. In International Conference on Learn-
ing Representations.
Alexis Conneau, Kartikay Khandelwal, Naman Goyal,
Vishrav Chaudhary, Guillaume Wenzek, Francisco
Guzmán, Edouard Grave, Myle Ott, Luke Zettle-
moyer, and Veselin Stoyanov. 2020. Unsupervised
cross-lingual representation learning at scale.
In
Proceedings of the 58th Annual Meeting of the Asso-
ciation for Computational Linguistics, pages 8440–
8451, Online. Association for Computational Lin-
guistics.
Alexis Conneau, Ruty Rinott, Guillaume Lample, Ad-
ina Williams, Samuel Bowman, Holger Schwenk,
and Veselin Stoyanov. 2018.
XNLI: Evaluating
cross-lingual sentence representations. In Proceed-
ings of the 2018 Conference on Empirical Methods
in Natural Language Processing, pages 2475–2485,
Brussels, Belgium. Association for Computational
Linguistics.
Luna De Bruyne, Orphée De Clercq, and Veronique
Hoste. 2021. Emotional RobBERT and insensitive
BERTje : combining transformers and affect lexica
for Dutch emotion detection. In Proceedings of the
Eleventh Workshop on Computational Approaches
to Subjectivity, Sentiment and Social Media Anal-
ysis (EACL 2021), pages 257–263. Association for
Computational Linguistics.
Loic De Langhe, Orphee De Clercq, and Veronique
Hoste. 2022.
Investigating cross-document event
coreference for Dutch. In Proceedings of the Fifth
Workshop on Computational Models of Reference,
Anaphora and Coreference, pages 88–98, Gyeongju,
Republic of Korea. Association for Computational
Linguistics.
Wietse de Vries and Malvina Nissim. 2021. As good
as new. how to successfully recycle English GPT-2
to make models for other languages. In Findings
of the Association for Computational Linguistics:
ACL-IJCNLP 2021, pages 836–846, Online. Asso-
ciation for Computational Linguistics.
Wietse de Vries, Andreas van Cranenburgh, Arianna
Bisazza, Tommaso Caselli, Gertjan van Noord, and
Malvina Nissim. 2019. BERTje: A Dutch BERT
Model. arXiv preprint arXiv:1912.09582.
Wietse de Vries, Martijn Wieling, and Malvina Nissim.
2022. Make the best of cross-lingual transfer: Evi-
dence from POS tagging with over 100 languages.
In Proceedings of the 60th Annual Meeting of the
Association for Computational Linguistics (Volume
1: Long Papers), pages 7676–7685, Dublin, Ireland.
Association for Computational Linguistics.
Pieter Delobelle, Ewoenam Tokpo, Toon Calders, and
Bettina Berendt. 2022a. Measuring fairness with bi-
ased rulers: A comparative study on bias metrics
for pre-trained language models. In Proceedings of
the 2022 Conference of the North American Chap-
ter of the Association for Computational Linguis-
tics: Human Language Technologies, pages 1693–
1706, Seattle, United States. Association for Com-
putational Linguistics.
Pieter
Delobelle,
Thomas
Winters,
and
Bettina
Berendt. 2020. RobBERT: a Dutch RoBERTa-based
Language Model.
In Findings of the Association
for Computational Linguistics: EMNLP 2020, pages
3255–3265, Online. Association for Computational
Linguistics.
Pieter
Delobelle,
Thomas
Winters,
and
Bettina
Berendt. 2022b. RobBERT-2022: Updating a dutch
language model to account for evolving language
use. arXiv preprint arXiv:2211.08192.
Jacob Devlin, Ming-Wei Chang, Kenton Lee, and
Kristina Toutanova. 2019a. BERT: Pre-training of
deep bidirectional transformers for language under-
standing.
In Proceedings of the 2019 Conference
of the North American Chapter of the Association
for Computational Linguistics: Human Language

--- Page 11 ---

Technologies, Volume 1 (Long and Short Papers),
pages 4171–4186, Minneapolis, Minnesota. Associ-
ation for Computational Linguistics.
Jacob Devlin, Ming-Wei Chang, Kenton Lee, and
Kristina Toutanova. 2019b.
Multilingual BERT.
https://github.com/google-research/bert/blob/master/multilingual.md.
AbdelRahim Elmadany, El Moatez Billah Nagoudi,
and Muhammad Abdul-Mageed. 2022. ORCA: A
challenging benchmark for Arabic language under-
standing. arXiv preprint arXiv:2212.10758.
Abbas Ghaddar, Philippe Langlais, Ahmad Rashid,
and Mehdi Rezagholizadeh. 2021.
Context-aware
Adversarial Training for Name Regularity Bias in
Named Entity Recognition. Transactions of the As-
sociation for Computational Linguistics, 9:586–604.
Evangelia Gogoulou, Ariel Ekgren, Tim Isbister, and
Magnus Sahlgren. 2022. Cross-lingual transfer of
monolingual models.
In Proceedings of the Thir-
teenth Language Resources and Evaluation Confer-
ence, pages 948–955, Marseille, France. European
Language Resources Association.
Andrew Gordon, Zornitsa Kozareva, and Melissa
Roemmele. 2012.
SemEval-2012 task 7: Choice
of plausible alternatives: An evaluation of common-
sense causal reasoning. In *SEM 2012: The First
Joint Conference on Lexical and Computational Se-
mantics – Volume 1: Proceedings of the main con-
ference and the shared task, and Volume 2: Pro-
ceedings of the Sixth International Workshop on Se-
mantic Evaluation (SemEval 2012), pages 394–398,
Montréal, Canada. Association for Computational
Linguistics.
Pengcheng He, Xiaodong Liu, Jianfeng Gao, and
Weizhu Chen. 2021.
DeBERTa:
Decoding-en-
hanced bert with disentangled attention. In Inter-
national Conference on Learning Representations.
Pengcheng He, Xiaodong Liu, Jianfeng Gao, and
Weizhu Chen. 2023. DeBERTaV3: Improving de-
BERTa using ELECTRA-style pre-training with gra-
dient-disentangled embedding sharing. In Submitted
to The Eleventh International Conference on Learn-
ing Representations. Under review.
Junjie Hu, Sebastian Ruder, Aditya Siddhant, Gra-
ham Neubig, Orhan Firat, and Melvin Johnson.
2020. XTREME: A massively multilingual multi-
-task benchmark for evaluating cross-lingual gener-
alisation. In Proceedings of the 37th International
Conference on Machine Learning, volume 119 of
Proceedings of Machine Learning Research, pages
4411–4421. PMLR.
Karin Kipper Schuler, Anna Korhonen, and Susan
Brown. 2009. VerbNet overview, extensions, map-
pings and applications. In Proceedings of Human
Language Technologies: The 2009 Annual Confer-
ence of the North American Chapter of the Associa-
tion for Computational Linguistics, Companion Vol-
ume: Tutorial Abstracts, pages 13–14, Boulder, Col-
orado. Association for Computational Linguistics.
Kentaro Kurihara, Daisuke Kawahara, and Tomohide
Shibata. 2022.
JGLUE: Japanese general lan-
guage understanding evaluation. In Proceedings of
the Thirteenth Language Resources and Evaluation
Conference, pages 2957–2966, Marseille, France.
European Language Resources Association.
Hang Le, Loïc Vial, Jibril Frej, Vincent Segonne, Max-
imin Coavoux, Benjamin Lecouteux, Alexandre Al-
lauzen, Benoit Crabbé, Laurent Besacier, and Didier
Schwab. 2020. FlauBERT: Unsupervised language
model pre-training for French. In Proceedings of the
Twelfth Language Resources and Evaluation Con-
ference, pages 2479–2490, Marseille, France. Euro-
pean Language Resources Association.
Hector J. Levesque, Ernest Davis, and Leora Morgen-
stern. 2012. The Winograd Schema Challenge. In
Proceedings of the Thirteenth International Con-
ference on Principles of Knowledge Representation
and Reasoning, KR’12, page 552–561. AAAI Press.
Zuchao Li, Kevin Parnow, Hai Zhao, Zhuosheng
Zhang, Rui Wang, Masao Utiyama, and Eiichiro
Sumita. 2021.
Cross-lingual transferring of pre–
trained contextualized language models.
arXiv
preprint arXiv:2107.12627.
Yaobo Liang, Nan Duan, Yeyun Gong, Ning Wu, Fen-
fei Guo, Weizhen Qi, Ming Gong, Linjun Shou,
Daxin Jiang, Guihong Cao, Xiaodong Fan, Ruofei
Zhang, Rahul Agrawal, Edward Cui, Sining Wei,
Taroon Bharti, Ying Qiao, Jiun-Hung Chen, Win-
nie Wu, Shuguang Liu, Fan Yang, Daniel Campos,
Rangan Majumder, and Ming Zhou. 2020. XGLUE:
A new benchmark datasetfor cross-lingual pre-train-
ing, understanding and generation.
In Proceed-
ings of the 2020 Conference on Empirical Methods
in Natural Language Processing (EMNLP), pages
6008–6018, Online. Association for Computational
Linguistics.
Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Man-
dar Joshi, Danqi Chen, Omer Levy, Mike Lewis,
Luke Zettlemoyer, and Veselin Stoyanov. 2019.
RoBERTa: A robustly optimized BERT pretraining
approach. arXiv preprint arXiv:1907.11692.
Marco Marelli, Stefano Menini, Marco Baroni, Luisa
Bentivogli, Raffaella Bernardi, and Roberto Zam-
parelli. 2014.
A SICK cure for the evaluation of
compositional distributional semantic models.
In
Proceedings of the Ninth International Conference
on Language Resources and Evaluation (LREC’14),
pages 216–223, Reykjavik, Iceland. European Lan-
guage Resources Association (ELRA).
George A. Miller. 1994. WordNet: A lexical database
for English. In Human Language Technology: Pro-
ceedings of a Workshop held at Plainsboro, New Jer-
sey, March 8-11, 1994.
Nelleke Oostdijk, Martin Reynaert, Véronique Hoste,
and Ineke Schuurman. 2013. The Construction of a
500-Million-Word Reference Corpus of Contempo-
rary Written Dutch. In Peter Spyns and Jan Odijk,

--- Page 12 ---

editors, Essential Speech and Language Technology
for Dutch: Results by the STEVIN programme, The-
ory and Applications of Natural Language Process-
ing, pages 219–247. Springer, Berlin, Heidelberg.
Pedro Javier Ortiz Suárez, Laurent Romary, and Benoît
Sagot. 2020. A monolingualapproach to contextual-
ized word embeddings for mid-resource languages.
In Proceedings of the 58th Annual Meeting of the
Association for Computational Linguistics, pages
1703–1714, Online. Association for Computational
Linguistics.
Xiaoman Pan, Boliang Zhang, Jonathan May, Joel
Nothman,
Kevin Knight,
and Heng Ji. 2017.
Cross-lingual name tagging and linking for 282 lan-
guages. In Proceedings of the 55th Annual Meet-
ing of the Association for Computational Linguistics
(Volume 1: Long Papers), pages 1946–1958, Van-
couver, Canada. Association for Computational Lin-
guistics.
Sungjoon Park,
Jihyung Moon,
Sungdong Kim,
Won Ik Cho, Ji Yoon Han, Jangwon Park, Chisung
Song, Junseong Kim, Youngsook Song, Taehwan
Oh, Joohong Lee, Juhyun Oh, Sungwon Lyu,
Younghoon Jeong, Inkwon Lee, Sangwoo Seo,
Dongjun Lee, Hyunwoo Kim, Myeonghwa Lee,
Seongbo Jang, Seungwon Do, Sunkyoung Kim,
Kyungtae Lim, Jongwon Lee, Kyumin Park, Jamin
Shin, Seonghyun Kim, Lucy Park, Alice Oh, Jung-
Woo Ha, and Kyunghyun Cho. 2021. KLUE: Ko-
rean language understanding evaluation. In Thirty-
ﬁfth Conference on Neural Information Processing
Systems Datasets and Benchmarks Track (Round 2).
Mohammad
Taher
Pilehvar
and
Jose
Camacho-
Collados. 2019. WiC: the word-in-context dataset
for evaluating context-sensitive meaning represen-
tations.
In Proceedings of the 2019 Conference
of the North American Chapter of the Association
for Computational Linguistics: Human Language
Technologies, Volume 1 (Long and Short Papers),
pages 1267–1273, Minneapolis, Minnesota. Associ-
ation for Computational Linguistics.
Edoardo Maria Ponti, Goran Glavaš, Olga Majewska,
Qianchu Liu, Ivan Vuli´c, and Anna Korhonen. 2020.
XCOPA: A multilingual dataset for causal com-
monsense reasoning.
In Proceedings of the 2020
Conference on Empirical Methods in Natural Lan-
guage Processing (EMNLP), pages 2362–2376, On-
line. Association for Computational Linguistics.
Marten Postma, Emiel van Miltenburg, Roxane Segers,
Anneleen Schoen, and Piek Vossen. 2016.
Open
Dutch WordNet.
In Proceedings of the 8th
Global WordNet Conference (GWC), pages 302–
310, Bucharest, Romania. Global Wordnet Associ-
ation.
Alessandro
Raganato,
Tommaso
Pasini,
Jose
Camacho-Collados, and Mohammad Taher Pilehvar.
2020. XL-WiC: A multilingual benchmark for eval-
uating semantic contextualization. In Proceedings
of the 2020 Conference on Empirical Methods in
Natural Language Processing (EMNLP), pages
7193–7206, Online. Association for Computational
Linguistics.
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
Marta Recasens, Lluís Màrquez, Emili Sapena, M. An-
tònia Martí, Mariona Taulé, Véronique Hoste, Mas-
simo Poesio, and Yannick Versley. 2010.
Se-
mEval-2010 task 1: Coreference resolution in mul-
tiple languages. In Proceedings of the 5th Interna-
tional Workshop on Semantic Evaluation, pages 1–
8, Uppsala, Sweden. Association for Computational
Linguistics.
Sebastian Ruder, Noah Constant, Jan Botha, Aditya
Siddhant, Orhan Firat, Jinlan Fu, Pengfei Liu, Jun-
jie Hu, Dan Garrette, Graham Neubig, and Melvin
Johnson. 2021. XTREME-R: Towards more chal-
lenging and nuanced multilingual evaluation.
In
Proceedings of the 2021 Conference on Empirical
Methods in Natural Language Processing, pages
10215–10245, Online and Punta Cana, Dominican
Republic. Association for Computational Linguis-
tics.
Ward Ruitenbeek, Victor Zwart, Robin Van Der No-
ord, Zhenja Gnezdilov, and Tommaso Caselli. 2022.
“zo grof !”: A comprehensive corpus for offensive
and abusive language in Dutch. In Proceedings of
the Sixth Workshop on Online Abuse and Harms
(WOAH), pages 40–56, Seattle, Washington (Hy-
brid). Association for Computational Linguistics.
Maarten Sap, Hannah Rashkin, Derek Chen, Ronan
Le Bras, and Yejin Choi. 2019. Social IQa: Com-
monsense reasoning about social interactions.
In
Proceedings of the 2019 Conference on Empirical
Methods in Natural Language Processing and the
9th International Joint Conference on Natural Lan-
guage Processing (EMNLP-IJCNLP), pages 4463–
4473, Hong Kong, China. Association for Computa-
tional Linguistics.
Tatiana Shavrina, Alena Fenogenova, Emelyanov An-
ton, Denis Shevelev, Ekaterina Artemova, Valentin
Malykh, Vladislav Mikhailov, Maria Tikhonova,
Andrey Chertok, and Andrey Evlampiev. 2020.
RussianSuperGLUE: A Russian language under-
standing evaluation benchmark. In Proceedings of

--- Page 13 ---

the 2020 Conference on Empirical Methods in Nat-
ural Language Processing (EMNLP), pages 4717–
4726, Online. Association for Computational Lin-
guistics.
Marco Spruit, Stephanie Verkleij, Kees de Schepper,
and Floortje Scheepers. 2022. Exploring language
markers of mental health in psychiatric stories. Ap-
plied Sciences, 12(4).
Erik F. Tjong Kim Sang. 2002.
Introduction to the
CoNLL-2002 Shared Task: Language-Independent
Named Entity Recognition.
In COLING-02: The
6th Conference on Natural Language Learning 2002
(CoNLL-2002).
Gorka Urbizu, Iñaki San Vicente, Xabier Saralegi, Ro-
drigo Agerri, and Aitor Soroa. 2022. BasqueGLUE:
A natural language understanding benchmark for
Basque. In Proceedings of the Thirteenth Language
Resources and Evaluation Conference, pages 1603–
1612, Marseille, France. European Language Re-
sources Association.
Benjamin Van der Burgh and Suzan Verberne. 2019.
The merits of universal language model ﬁne-tuning
for small datasets–a case with dutch book reviews.
arXiv preprint arXiv:1910.00896.
Frank van Eynde. 2004. Part of speech tagging en lem-
matisering van het Corpus Gesproken Nederlands.
KU Leuven.
Gertjan van Noord, Gosse Bouma, Frank Van Eynde,
Daniël de Kok, Jelmer van der Linde, Ineke Schuur-
man, Erik Tjong Kim Sang, and Vincent Vandegh-
inste. 2013.
Large Scale Syntactic Annotation of
Written Dutch: Lassy. In Peter Spyns and Jan Odijk,
editors, Essential Speech and Language Technology
for Dutch: Results by the STEVIN programme, The-
ory and Applications of Natural Language Process-
ing, pages 147–164. Springer, Berlin, Heidelberg.
Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob
Uszkoreit, Llion Jones, Aidan N Gomez, Łukasz
Kaiser, and Illia Polosukhin. 2017. Attention is all
you need. In Advances in Neural Information Pro-
cessing Systems, volume 30. Curran Associates, Inc.
Piek Vossen, Attila Görög, Rubén Izquierdo, and An-
tal van den Bosch. 2012. DutchSemCor: Targeting
the ideal sense-tagged corpus. In Proceedings of the
Eighth International Conference on Language Re-
sources and Evaluation (LREC’12), pages 584–589,
Istanbul, Turkey. European Language Resources As-
sociation (ELRA).
Piek Vossen, Isa Maks, Roxane Segers, and Hennie
VanderVliet. 2008. Integrating lexical units, synsets
and ontology in the cornetto database. In Proceed-
ings of the Sixth International Conference on Lan-
guage Resources and Evaluation (LREC’08), Mar-
rakech, Morocco. European Language Resources
Association (ELRA).
Alex Wang, Yada Pruksachatkun, Nikita Nangia,
Amanpreet Singh, Julian Michael, Felix Hill, Omer
Levy, and Samuel Bowman. 2019. Superglue: A
stickier benchmark for general-purpose language
understanding systems. In Advances in Neural In-
formation Processing Systems, volume 32. Curran
Associates, Inc.
Alex Wang, Amanpreet Singh, Julian Michael, Fe-
lix Hill, Omer Levy, and Samuel Bowman. 2018.
GLUE: A multi-task benchmark and analysis plat-
form for natural language understanding. In Pro-
ceedings of the 2018 EMNLP Workshop Black-
boxNLP: Analyzing and Interpreting Neural Net-
works for NLP, pages 353–355, Brussels, Belgium.
Association for Computational Linguistics.
Zirui Wang, Adams Wei Yu, Orhan Firat, and Yuan
Cao. 2021. Towards zero-label language learning.
arXiv preprint arXiv:2109.09193.
Gijs Wijnholds and Michael Moortgat. 2021. SICK-
-NL: A dataset for Dutch natural language inference.
In Proceedings of the 16th Conference of the Euro-
pean Chapter of the Association for Computational
Linguistics: Main Volume, pages 1474–1479, On-
line. Association for Computational Linguistics.
Bryan Wilie, Karissa Vincentio, Genta Indra Winata,
Samuel Cahyawijaya, Xiaohong Li, Zhi Yuan Lim,
Sidik Soleman, Rahmad Mahendra, Pascale Fung,
Syafri Bahar, and Ayu Purwarianti. 2020. IndoNLU:
Benchmark and resources for evaluating Indonesian
natural language understanding. In Proceedings of
the 1st Conference of the Asia-Paciﬁc Chapter of the
Association for Computational Linguistics and the
10th International Joint Conference on Natural Lan-
guage Processing, pages 843–857, Suzhou, China.
Association for Computational Linguistics.
Liang Xu, Hai Hu, Xuanwei Zhang, Lu Li, Chen-
jie Cao, Yudong Li, Yechen Xu, Kai Sun, Dian
Yu, Cong Yu, Yin Tian, Qianqian Dong, Weitang
Liu, Bo Shi, Yiming Cui, Junyi Li, Jun Zeng,
Rongzhao Wang, Weijian Xie, Yanting Li, Yina
Patterson, Zuoyu Tian, Yiwen Zhang, He Zhou,
Shaoweihua Liu, Zhe Zhao, Qipeng Zhao, Cong
Yue, Xinrui Zhang, Zhengliang Yang, Kyle Richard-
son, and Zhenzhong Lan. 2020. CLUE: A Chinese
language understanding evaluation benchmark. In
Proceedings of the 28th International Conference
on Computational Linguistics, pages 4762–4772,
Barcelona, Spain (Online). International Committee
on Computational Linguistics.
Daniel Zeman, Joakim Nivre, et al. 2022. Universal de-
pendencies 2.11. LINDAT/CLARIAH-CZ digital li-
brary at the Institute of Formal and Applied Linguis-
tics (ÚFAL), Faculty of Mathematics and Physics,
Charles University.

--- Page 14 ---

A
Task examples
This appendix contains example items for each DUMB task, selected from training data.
POS: Part-of-Speech Tagging (Lassy)
Provide POS tags for every word in the sentence.
Sentence
Tagged Sentence
Scoubidou-touwtjes zijn veilig in de hand, maar
niet in de mond.
[N|soort|mv|dim
Scoubidou-
touwtjes]
[WW|pv|tgw|mv
zijn]
[ADJ|vrij|basis|zonder
veilig]
[VZ|init
in]
[LID|bep|stan|rest
de]
[N|soort|ev|basis|zijd|stan
hand] [LET ,] [VG|neven maar] [BW niet]
[VZ|init in] [LID|bep|stan|rest de]
[N|soort|ev|basis|zijd|stan
mond]
[LET .]
NER: Named Entity Recognition (SoNaR)
Mark all named entities in the sentence.
Sentence
Tagged Sentence
Topman Jack Welch van het Amerikaanse indus-
triële concern General Electric (GE) verwerpt het
aanbod van zijn collega van Honeywell om de
beoogde fusie van de twee ondernemingen te red-
den.
Topman
[PERSON
Jack
Welch]
van
het
[LOCATION
Amerikaanse]
industriële
con-
cern
[ORGANIZATION
General
Electric]
([ORGANIZATION GE])
verwerpt
het
aan-
bod van zijn collega van [ORGANIZATION
Honeywell] om de beoogde fusie van de twee
ondernemingen te redden.
De radar wordt dit weekend gepresenteerd op het
Vogelfestival in het natuurgebied de Oostvaarder-
splassen in Lelystad.
De radar wordt dit weekend gepresenteerd op
het [EVENT Vogelfestival] in het natuurge-
bied de [LOCATION Oostvaardersplassen] in
[LOCATION Lelystad].
WSD: Word Sense Disambiguation (WiC-NL)
Determine whether the marked words in each sentence have the same sense.
Sentence 1
Sentence 2
Label
In bijna elk mechanisch apparaat zijn wel
assen te vinden. (mechanical device)
Mannen daarentegen zijn meer geboeid
door mechaniek en willen nagenoeg al-
tijd een mechanisch uurwerk. (mechanical
clock)
same
Het merendeel lijkt een ijzige kalmte over
zich heen te hebben. (icy calm)
De schaatsgrootheden uit de tijd van de
wollen muts en de ijzig koude buitenba-
nen met storm en sneeuw kunnen worden
vergelijken met de schaatsgrootheden uit de
tijd van gestoomlijnde pakken, klapschaats
en en geconditioneerde binnenbanen. (icy
temperature)
different

--- Page 15 ---

PR: Pronoun Resolution (DPR)
Determine whether the marked pronoun refers to the marked expression.
Text
Label
Toen kwam de aanslag op New York en de generaal, intussen president, werd voor de
keuze gesteld. Hij nam het binnenlandse risico: confrontatie met zijn islamitische militan-
ten, in plaats van met de Verenigde Staten. (the general, He)
same
Di Rupo weet waarom hij zich verzet tegen het privatiseringsbeginsel. (he, the privati-
zation principle)
different
CR: Causal Reasoning (COPA-NL)
Choose the most plausible cause or effect, given a premise.
Premise
Choice 1
Choice 2
Label
De
vrouw
bungelde
het
koekje boven de hond. (The
woman dangled the biscuit
above the dog.)
De hond sprong op.(The
dog jumped up.)
De hond krabde aan zijn
vacht.
(The dog scratched
its fur.)
Choice 1
De vrouw voelde zich een-
zaam.
(The woman felt
lonely.)
Ze renoveerde haar keuken.
(She renovated her kitchen.)
Ze adopteerde een kat. (She
adopted a cat.)
Choice 2
NLI: Natural Language Inference (SICK-NL)
Classify whether the ﬁrst sentence entails or contradicts the second sentence.
Sentence 1
Sentence 2
Label
Een man springt in een leeg bad (A man
is jumping into an empty pool)
Een man springt in een vol zwembad (A
man is jumping into a full pool)
contradiction
Een man met een trui is de bal aan
het dunken bij een basketbalwedstrijd (A
man with a jersey is dunking the ball at a
basketball game)
De bal wordt gedunkt door een man met
een trui bij een basketbalwedstrijd (The
ball is being dunked by a man with a jer-
sey at a basketball game)
entailment
Drie kinderen zitten in de bladeren Three
kids are sitting in the leaves
Drie kinderen springen in de bladeren
(Three kids are jumping in the leaves)
neutral
ALD: Abusive Language Detection (DALC)
Classify whether the tweet is abusive or offensive.
Text
Label
Ach @USER wie neemt die nog serieus. Het gezellige dikkertje dat propogandeerde dat
dik zijn, wat extra vet niet erg is en dat we gewoon lekker ongezond moeten eten wanneer
we dat willen. En nu klagen over de kwetsbaren wat juist diegene zijn met teveel vetcellen.
(fat shaming)
abusive
@USER OMDAT VROUWEN MOEILIJKE WEZENS ZIJN (misogynistic)
offensive

--- Page 16 ---

SA: Sentiment Analysis (DBRD)
Classify whether the review is positive or negative.
Text
Label
Het verhaal speelt zich af aan het einde van de 19e eeuw. Boeiend van begin tot eind, geeft
het een inkijkje in het leven van arbeiders en wetenschappers in Barcelona. De industriële
revolutie is net begonnen en de effecten daarvan tekenen zich af. Grote veranderingen
op het gebied van de medische wetenschap spelen op de achtergrond van liefde, vriend-
schap, betrokkenheid en verraad. Fictie wordt vermengd met historische feiten op een
meeslepende manier, pakkend begin, verrassend einde. Aanrader! (explicit recommenda-
tion)
positive
Eerlijk gezegd vindt ik dat dit boek vreemd is geschreven. De verhaallijnen gaan door
elkaar heen en dat maakt het heel onduidelijk. Het onderwerp is wel goed bedacht (odd
writing style and entangled story lines)
negative
QA: Question Answering (SQuAD-NL)
Locate the answer to a question in a given paragraph, or classify the question as unanswerable.
Question
Context and Answer
Wat is Saksische tuin in het Pools?
Vlakbij,
in Ogród Saski (de Saksische Tuin),
was het
Zomertheater in gebruik van 1870 tot 1939, en in het inter-
bellum omvatte het theatercomplex ook Momus, het eerste lit-
eraire cabaret van Warschau, en Melodram, het muziekthe-
ater van Leon Schiller.
Het Wojciech Bogusławski Theater
(1922-26) was het beste voorbeeld van "Pools monumentaal the-
ater". Vanaf het midden van de jaren dertig huisvestte het Great
Theatre-gebouw het Upati Institute of Dramatic Arts - de eerste
door de staat gerunde academie voor dramatische kunst, met een
acteerafdeling en een regie-afdeling.

--- Page 17 ---

B
Training setup and hyper-parameters
Our main results are based on 14 pre-trained language models, 9 tasks and 5 test runs per model and
task, totalling 630 runs. However, the total number of runs is much larger due to experimentation and
hyper-parameter search. The total amount of runs within the hyper-parameter grids (can be found on
the next two pages) is 7,504. The hyper-parameter search ranges can be found on the next two pages.
Training durations per vary from seconds to hours, depending on task, model size and training epochs.
All
models
were
trained
on
single
A100
(40GB)
GPUs
with
the
implementations
on
github.com/wietsedv/dumb/tree/main/trainers and the following hyper-parameters:
• Batch Size: 32
• Weight Decay: 0
• Learning Rate Decay: Linear
• Optimizer: Adam
• Adam β1: 0.9
• Adam β2: 0.999
• Adam ǫ: 1e-8
• Gradient Clipping: 1.0
• Epochs: see table
• Dropout: see table
• Learning Rate: see table
• Warmup: see table
Roughly estimated training durations across models and hyper-parameters are:
• POS: 30 minutes
• NER: 30 minutes
• WSD: 8 minutes
• PR: 2 minutes
• CR: 2 minutes
• NLI: 8 minutes
• SA: 45 minutes
• ALD: 10 minutes
• QA: 4 hours
Combined grid search and test run times add up to 105 GPU hours per pre-trained model and 61 days
for the 14 models combined. Additional experiments that did not end up in the paper may add about
50% extra GPU hours. When evaluating new models, we advice experimenting with smaller grids based
on our optimal parameters.

--- Page 18 ---

C
Model Performance Regression Model
This table shows the linear regression model discussed in Section 5.
OLS Regression
R e s u l t s
==============================================================================
Dep .
V a r i a b l e :
RER
R−squared :
0.836
Model :
OLS
Adj . R−squared :
0.733
Method :
Least
Squares
F−s t a t i s t i c :
8.127
Date :
Tue ,
13 Jun
2023
Prob
(F−s t a t i s t i c ) :
0.00535
Time :
18:34:39
Log−Likelihood :
−47.201
No.
Observations :
14
AIC :
106.4
Df
R e s i d u a l s :
8
BIC :
110.2
Df Model :
5
Covariance Type :
nonrobust
============================================================================================
coef
s t d
e r r
t
P >| t |
[0.025
0.975]
−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−
I n t e r c e p t
−9.5663
6.507
−1.470
0.180
−24.571
5.438
Language [T . e n g l i s h ]
−28.8601
7.480
−3.858
0.005
−46.109
−11.611
Language [T . m u l t i l i n g u a l ]
−1.5577
7.072
−0.220
0.831
−17.865
14.750
Model [T . debertav3 ]
33.6502
7.279
4.623
0.002
16.865
50.435
Model [T . r o b e r t a ]
9.0766
6.053
1.499
0.172
−4.882
23.035
Size [T . l a r g e ]
13.8761
6.333
2.191
0.060
−0.728
28.480
==============================================================================
Omnibus :
3.330
Durbin −Watson :
2.501
Prob ( Omnibus ) :
0.189
Jarque −Bera
( JB ) :
2.099
Skew :
−0.941
Prob ( JB ) :
0.350
K u r t o s i s :
2.768
Cond . No .
5.86
==============================================================================

--- Page 19 ---

Task
Model
Epochs
Warmup
LR
Dropout
Dev
Test
POS
BERTje
{1, 3, 5}
{0.0, 0.3}
{3e-05, 5e-05, 0.0001}
{0.0, 0.1}
98.4
97.8
POS
RobBERTV1
{1, 3, 5}
{0.0, 0.3}
{3e-05, 5e-05, 0.0001}
{0.0, 0.1}
98.6
98.1
POS
RobBERTV2
{1, 3, 5}
{0.0, 0.3}
{3e-05, 5e-05, 0.0001}
{0.0, 0.1}
98.7
98.2
POS
RobBERT2022
{1, 3, 5}
{0.0, 0.3}
{3e-05, 5e-05, 0.0001}
{0.0, 0.1}
98.6
98.2
POS
mBERTcased
{1, 3, 5}
{0.0, 0.3}
{3e-05, 5e-05, 0.0001}
{0.0, 0.1}
98.6
97.9
POS
XLM-Rbase
{1, 3, 5}
{0.0, 0.3}
{3e-05, 5e-05, 0.0001}
{0.0, 0.1}
98.7
98.1
POS
mDeBERTaV3base
{1, 3, 5}
{0.0, 0.3}
{3e-05, 5e-05, 0.0001}
{0.0, 0.1}
98.7
98.2
POS
XLM-Rlarge
{1, 3, 5}
{0.0, 0.3}
{3e-05, 5e-05, 0.0001}
{0.0, 0.1}
98.8
98.4
POS
BERTbase
{1, 3, 5}
{0.0, 0.3}
{3e-05, 5e-05, 0.0001}
{0.0, 0.1}
97.9
97.3
POS
RoBERTabase
{1, 3, 5}
{0.0, 0.3}
{3e-05, 5e-05, 0.0001}
{0.0, 0.1}
98.2
97.6
POS
DeBERTaV3base
{1, 3, 5}
{0.0, 0.3}
{3e-05, 5e-05, 0.0001}
{0.0, 0.1}
98.4
97.9
POS
BERTlarge
{1, 3, 5}
{0.0, 0.3}
{3e-05, 5e-05, 0.0001}
{0.0, 0.1}
98.2
97.5
POS
RoBERTalarge
{1, 3, 5}
{0.0, 0.3}
{3e-05, 5e-05, 0.0001}
{0.0, 0.1}
98.5
97.9
POS
DeBERTaV3large
{1, 3, 5}
{0.0, 0.3}
{3e-05, 5e-05, 0.0001}
{0.0, 0.1}
98.6
98.2
NER
BERTje
{1, 3, 5}
{0.0, 0.3}
{1e-05, 3e-05, 5e-05}
{0.0, 0.1}
85.1
86.1
NER
RobBERTV1
{1, 3, 5}
{0.0, 0.3}
{1e-05, 3e-05, 5e-05}
{0.0, 0.1}
84.2
83.5
NER
RobBERTV2
{1, 3, 5}
{0.0, 0.3}
{1e-05, 3e-05, 5e-05}
{0.0, 0.1}
85.5
86.7
NER
RobBERT2022
{1, 3, 5}
{0.0, 0.3}
{1e-05, 3e-05, 5e-05}
{0.0, 0.1}
85.7
87.2
NER
mBERTcased
{1, 3, 5}
{0.0, 0.3}
{1e-05, 3e-05, 5e-05}
{0.0, 0.1}
86.6
87.4
NER
XLM-Rbase
{1, 3, 5}
{0.0, 0.3}
{1e-05, 3e-05, 5e-05}
{0.0, 0.1}
85.9
87.6
NER
mDeBERTaV3base
{1, 3, 5}
{0.0, 0.3}
{1e-05, 3e-05, 5e-05}
{0.0, 0.1}
85.1
88.5
NER
XLM-Rlarge
{1, 3, 5}
{0.0, 0.3}
{1e-05, 3e-05, 5e-05}
{0.0, 0.1}
87.5
90.3
NER
BERTbase
{1, 3, 5}
{0.0, 0.3}
{1e-05, 3e-05, 5e-05}
{0.0, 0.1}
81.7
81.9
NER
RoBERTabase
{1, 3, 5}
{0.0, 0.3}
{1e-05, 3e-05, 5e-05}
{0.0, 0.1}
83.7
82.3
NER
DeBERTaV3base
{1, 3, 5}
{0.0, 0.3}
{1e-05, 3e-05, 5e-05}
{0.0, 0.1}
83.6
86.4
NER
BERTlarge
{1, 3, 5}
{0.0, 0.3}
{1e-05, 3e-05, 5e-05}
{0.0, 0.1}
83.3
82.5
NER
RoBERTalarge
{1, 3, 5}
{0.0, 0.3}
{1e-05, 3e-05, 5e-05}
{0.0, 0.1}
83.8
84.4
NER
DeBERTaV3large
{1, 3, 5}
{0.0, 0.3}
{1e-05, 3e-05, 5e-05}
{0.0, 0.1}
88.2
87.6
WSD
BERTje
{1, 3, 5, 10}
{0.0, 0.3}
{1e-05, 3e-05, 5e-05, 0.0001}
{0.0, 0.1}
67.9
65.9
WSD
RobBERTV1
{1, 3, 5, 10}
{0.0, 0.3}
{1e-05, 3e-05, 5e-05, 0.0001}
{0.0, 0.1}
61.3
60.6
WSD
RobBERTV2
{1, 3, 5, 10}
{0.0, 0.3}
{1e-05, 3e-05, 5e-05, 0.0001}
{0.0, 0.1}
66.3
64.1
WSD
RobBERT2022
{1, 3, 5, 10}
{0.0, 0.3}
{1e-05, 3e-05, 5e-05, 0.0001}
{0.0, 0.1}
67.0
63.7
WSD
mBERTcased
{1, 3, 5, 10}
{0.0, 0.3}
{1e-05, 3e-05, 5e-05, 0.0001}
{0.0, 0.1}
68.2
68.5
WSD
XLM-Rbase
{1, 3, 5, 10}
{0.0, 0.3}
{1e-05, 3e-05, 5e-05, 0.0001}
{0.0, 0.1}
66.7
66.5
WSD
mDeBERTaV3base
{1, 3, 5, 10}
{0.0, 0.3}
{1e-05, 3e-05, 5e-05, 0.0001}
{0.0, 0.1}
69.8
69.6
WSD
XLM-Rlarge
{1, 3, 5, 10}
{0.0, 0.3}
{1e-05, 3e-05, 5e-05, 0.0001}
{0.0, 0.1}
73.0
73.1
WSD
BERTbase
{1, 3, 5, 10}
{0.0, 0.3}
{1e-05, 3e-05, 5e-05, 0.0001}
{0.0, 0.1}
60.0
58.2
WSD
RoBERTabase
{1, 3, 5, 10}
{0.0, 0.3}
{1e-05, 3e-05, 5e-05, 0.0001}
{0.0, 0.1}
62.6
61.1
WSD
DeBERTaV3base
{1, 3, 5, 10}
{0.0, 0.3}
{1e-05, 3e-05, 5e-05, 0.0001}
{0.0, 0.1}
66.4
64.4
WSD
BERTlarge
{1, 3, 5, 10}
{0.0, 0.3}
{1e-05, 3e-05, 5e-05, 0.0001}
{0.0, 0.1}
60.2
57.2
WSD
RoBERTalarge
{1, 3, 5, 10}
{0.0, 0.3}
{1e-05, 3e-05, 5e-05, 0.0001}
{0.0, 0.1}
64.3
59.1
WSD
DeBERTaV3large
{1, 3, 5, 10}
{0.0, 0.3}
{1e-05, 3e-05, 5e-05, 0.0001}
{0.0, 0.1}
71.3
70.2
PR
BERTje
{1, 3, 5, 10, 20}
{0.0, 0.3}
{1e-05, 3e-05, 5e-05, 0.0001}
{0.0, 0.1}
69.7
65.8
PR
RobBERTV1
{1, 3, 5, 10, 20}
{0.0, 0.3}
{1e-05, 3e-05, 5e-05, 0.0001}
{0.0, 0.1}
66.9
57.3
PR
RobBERTV2
{1, 3, 5, 10, 20}
{0.0, 0.3}
{1e-05, 3e-05, 5e-05, 0.0001}
{0.0, 0.1}
69.0
65.8
PR
RobBERT2022
{1, 3, 5, 10, 20}
{0.0, 0.3}
{1e-05, 3e-05, 5e-05, 0.0001}
{0.0, 0.1}
71.1
65.2
PR
mBERTcased
{1, 3, 5, 10, 20}
{0.0, 0.3}
{1e-05, 3e-05, 5e-05, 0.0001}
{0.0, 0.1}
70.4
62.0
PR
XLM-Rbase
{1, 3, 5, 10, 20}
{0.0, 0.3}
{1e-05, 3e-05, 5e-05, 0.0001}
{0.0, 0.1}
64.1
57.4
PR
mDeBERTaV3base
{1, 3, 5, 10, 20}
{0.0, 0.3}
{1e-05, 3e-05, 5e-05, 0.0001}
{0.0, 0.1}
69.7
58.7
PR
XLM-Rlarge
{1, 3, 5, 10, 20}
{0.0, 0.3}
{1e-05, 3e-05, 5e-05, 0.0001}
{0.0, 0.1}
64.8
60.4
PR
BERTbase
{1, 3, 5, 10, 20}
{0.0, 0.3}
{1e-05, 3e-05, 5e-05, 0.0001}
{0.0, 0.1}
65.5
57.6
PR
RoBERTabase
{1, 3, 5, 10, 20}
{0.0, 0.3}
{1e-05, 3e-05, 5e-05, 0.0001}
{0.0, 0.1}
68.3
60.4
PR
DeBERTaV3base
{1, 3, 5, 10, 20}
{0.0, 0.3}
{1e-05, 3e-05, 5e-05, 0.0001}
{0.0, 0.1}
69.0
57.1
PR
BERTlarge
{1, 3, 5, 10, 20}
{0.0, 0.3}
{1e-05, 3e-05, 5e-05, 0.0001}
{0.0, 0.1}
64.1
55.8
PR
RoBERTalarge
{1, 3, 5, 10, 20}
{0.0, 0.3}
{1e-05, 3e-05, 5e-05, 0.0001}
{0.0, 0.1}
61.3
56.6
PR
DeBERTaV3large
{1, 3, 5, 10, 20}
{0.0, 0.3}
{1e-05, 3e-05, 5e-05, 0.0001}
{0.0, 0.1}
71.8
60.9

--- Page 20 ---

Task
Model
Epochs
Warmup
LR
Dropout
Dev
Test
CR
BERTje
{1, 3, 5, 10, 20}
{0.0, 0.3}
{1e-05, 3e-05, 5e-05, 0.0001}
{0.0, 0.1}
71.0
62.0
CR
RobBERTV1
{1, 3, 5, 10, 20}
{0.0, 0.3}
{1e-05, 3e-05, 5e-05, 0.0001}
{0.0, 0.1}
69.0
56.4
CR
RobBERTV2
{1, 3, 5, 10, 20}
{0.0, 0.3}
{1e-05, 3e-05, 5e-05, 0.0001}
{0.0, 0.1}
68.0
56.2
CR
RobBERT2022
{1, 3, 5, 10, 20}
{0.0, 0.3}
{1e-05, 3e-05, 5e-05, 0.0001}
{0.0, 0.1}
71.0
55.4
CR
mBERTcased
{1, 3, 5, 10, 20}
{0.0, 0.3}
{1e-05, 3e-05, 5e-05, 0.0001}
{0.0, 0.1}
61.0
55.0
CR
XLM-Rbase
{1, 3, 5, 10, 20}
{0.0, 0.3}
{1e-05, 3e-05, 5e-05, 0.0001}
{0.0, 0.1}
70.0
51.8
CR
mDeBERTaV3base
{1, 3, 5, 10, 20}
{0.0, 0.3}
{1e-05, 3e-05, 5e-05, 0.0001}
{0.0, 0.1}
81.0
69.5
CR
XLM-Rlarge
{1, 3, 5, 10, 20}
{0.0, 0.3}
{1e-05, 3e-05, 5e-05, 0.0001}
{0.0, 0.1}
66.0
52.2
CR
BERTbase
{1, 3, 5, 10, 20}
{0.0, 0.3}
{1e-05, 3e-05, 5e-05, 0.0001}
{0.0, 0.1}
65.0
51.2
CR
RoBERTabase
{1, 3, 5, 10, 20}
{0.0, 0.3}
{1e-05, 3e-05, 5e-05, 0.0001}
{0.0, 0.1}
70.0
52.8
CR
DeBERTaV3base
{1, 3, 5, 10, 20}
{0.0, 0.3}
{1e-05, 3e-05, 5e-05, 0.0001}
{0.0, 0.1}
61.0
51.4
CR
BERTlarge
{1, 3, 5, 10, 20}
{0.0, 0.3}
{1e-05, 3e-05, 5e-05, 0.0001}
{0.0, 0.1}
64.0
50.2
CR
RoBERTalarge
{1, 3, 5, 10, 20}
{0.0, 0.3}
{1e-05, 3e-05, 5e-05, 0.0001}
{0.0, 0.1}
66.0
52.1
CR
DeBERTaV3large
{1, 3, 5, 10, 20}
{0.0, 0.3}
{1e-05, 3e-05, 5e-05, 0.0001}
{0.0, 0.1}
82.0
75.4
NLI
BERTje
{1, 3, 5, 10}
{0.0, 0.3}
{1e-05, 3e-05, 5e-05, 0.0001}
{0.0, 0.1}
84.2
85.2
NLI
RobBERTV1
{1, 3, 5, 10}
{0.0, 0.3}
{1e-05, 3e-05, 5e-05, 0.0001}
{0.0, 0.1}
83.2
83.3
NLI
RobBERTV2
{1, 3, 5, 10}
{0.0, 0.3}
{1e-05, 3e-05, 5e-05, 0.0001}
{0.0, 0.1}
85.5
84.6
NLI
RobBERT2022
{1, 3, 5, 10}
{0.0, 0.3}
{1e-05, 3e-05, 5e-05, 0.0001}
{0.0, 0.1}
85.1
85.6
NLI
mBERTcased
{1, 3, 5, 10}
{0.0, 0.3}
{1e-05, 3e-05, 5e-05, 0.0001}
{0.0, 0.1}
83.8
84.3
NLI
XLM-Rbase
{1, 3, 5, 10}
{0.0, 0.3}
{1e-05, 3e-05, 5e-05, 0.0001}
{0.0, 0.1}
85.9
85.5
NLI
mDeBERTaV3base
{1, 3, 5, 10}
{0.0, 0.3}
{1e-05, 3e-05, 5e-05, 0.0001}
{0.0, 0.1}
89.1
88.9
NLI
XLM-Rlarge
{1, 3, 5, 10}
{0.0, 0.3}
{1e-05, 3e-05, 5e-05, 0.0001}
{0.0, 0.1}
89.1
88.8
NLI
BERTbase
{1, 3, 5, 10}
{0.0, 0.3}
{1e-05, 3e-05, 5e-05, 0.0001}
{0.0, 0.1}
81.4
82.3
NLI
RoBERTabase
{1, 3, 5, 10}
{0.0, 0.3}
{1e-05, 3e-05, 5e-05, 0.0001}
{0.0, 0.1}
83.2
82.3
NLI
DeBERTaV3base
{1, 3, 5, 10}
{0.0, 0.3}
{1e-05, 3e-05, 5e-05, 0.0001}
{0.0, 0.1}
87.1
86.5
NLI
BERTlarge
{1, 3, 5, 10}
{0.0, 0.3}
{1e-05, 3e-05, 5e-05, 0.0001}
{0.0, 0.1}
83.4
82.9
NLI
RoBERTalarge
{1, 3, 5, 10}
{0.0, 0.3}
{1e-05, 3e-05, 5e-05, 0.0001}
{0.0, 0.1}
84.2
83.9
NLI
DeBERTaV3large
{1, 3, 5, 10}
{0.0, 0.3}
{1e-05, 3e-05, 5e-05, 0.0001}
{0.0, 0.1}
88.9
89.1
SA
BERTje
{1, 2, 3}
{0.0, 0.3}
{3e-05, 5e-05, 0.0001}
{0.0, 0.1}
94.8
93.3
SA
RobBERTV1
{1, 2, 3}
{0.0, 0.3}
{3e-05, 5e-05, 0.0001}
{0.0, 0.1}
91.2
89.4
SA
RobBERTV2
{1, 2, 3}
{0.0, 0.3}
{3e-05, 5e-05, 0.0001}
{0.0, 0.1}
95.4
93.2
SA
RobBERT2022
{1, 2, 3}
{0.0, 0.3}
{3e-05, 5e-05, 0.0001}
{0.0, 0.1}
95.2
93.5
SA
mBERTcased
{1, 2, 3}
{0.0, 0.3}
{3e-05, 5e-05, 0.0001}
{0.0, 0.1}
92.8
90.5
SA
XLM-Rbase
{1, 2, 3}
{0.0, 0.3}
{3e-05, 5e-05, 0.0001}
{0.0, 0.1}
95.6
93.0
SA
mDeBERTaV3base
{1, 2, 3}
{0.0, 0.3}
{3e-05, 5e-05, 0.0001}
{0.0, 0.1}
94.2
93.5
SA
XLM-Rlarge
{1, 2, 3}
{0.0, 0.3}
{3e-05, 5e-05, 0.0001}
{0.0, 0.1}
96.4
94.2
SA
BERTbase
{1, 2, 3}
{0.0, 0.3}
{3e-05, 5e-05, 0.0001}
{0.0, 0.1}
81.0
79.6
SA
RoBERTabase
{1, 2, 3}
{0.0, 0.3}
{3e-05, 5e-05, 0.0001}
{0.0, 0.1}
86.8
86.6
SA
DeBERTaV3base
{1, 2, 3}
{0.0, 0.3}
{3e-05, 5e-05, 0.0001}
{0.0, 0.1}
92.4
92.3
SA
BERTlarge
{1, 2, 3}
{0.0, 0.3}
{3e-05, 5e-05, 0.0001}
{0.0, 0.1}
82.4
82.6
SA
RoBERTalarge
{1, 2, 3}
{0.0, 0.3}
{3e-05, 5e-05, 0.0001}
{0.0, 0.1}
87.4
89.0
SA
DeBERTaV3large
{1, 2, 3}
{0.0, 0.3}
{3e-05, 5e-05, 0.0001}
{0.0, 0.1}
93.6
92.8
ALD
BERTje
{1, 3, 5, 10}
{0.0, 0.3}
{3e-05, 5e-05, 0.0001}
{0.0, 0.1}
67.4
58.8
ALD
RobBERTV1
{1, 3, 5, 10}
{0.0, 0.3}
{3e-05, 5e-05, 0.0001}
{0.0, 0.1}
66.3
60.8
ALD
RobBERTV2
{1, 3, 5, 10}
{0.0, 0.3}
{3e-05, 5e-05, 0.0001}
{0.0, 0.1}
70.1
63.7
ALD
RobBERT2022
{1, 3, 5, 10}
{0.0, 0.3}
{3e-05, 5e-05, 0.0001}
{0.0, 0.1}
67.9
66.6
ALD
mBERTcased
{1, 3, 5, 10}
{0.0, 0.3}
{3e-05, 5e-05, 0.0001}
{0.0, 0.1}
64.0
56.9
ALD
XLM-Rbase
{1, 3, 5, 10}
{0.0, 0.3}
{3e-05, 5e-05, 0.0001}
{0.0, 0.1}
65.8
60.2
ALD
mDeBERTaV3base
{1, 3, 5, 10}
{0.0, 0.3}
{3e-05, 5e-05, 0.0001}
{0.0, 0.1}
68.0
63.9
ALD
XLM-Rlarge
{1, 3, 5, 10}
{0.0, 0.3}
{3e-05, 5e-05, 0.0001}
{0.0, 0.1}
70.3
66.6
ALD
BERTbase
{1, 3, 5, 10}
{0.0, 0.3}
{3e-05, 5e-05, 0.0001}
{0.0, 0.1}
60.1
52.2
ALD
RoBERTabase
{1, 3, 5, 10}
{0.0, 0.3}
{3e-05, 5e-05, 0.0001}
{0.0, 0.1}
63.3
52.2
ALD
DeBERTaV3base
{1, 3, 5, 10}
{0.0, 0.3}
{3e-05, 5e-05, 0.0001}
{0.0, 0.1}
64.9
60.2
ALD
BERTlarge
{1, 3, 5, 10}
{0.0, 0.3}
{3e-05, 5e-05, 0.0001}
{0.0, 0.1}
62.3
55.6
ALD
RoBERTalarge
{1, 3, 5, 10}
{0.0, 0.3}
{3e-05, 5e-05, 0.0001}
{0.0, 0.1}
64.0
59.3
ALD
DeBERTaV3large
{1, 3, 5, 10}
{0.0, 0.3}
{3e-05, 5e-05, 0.0001}
{0.0, 0.1}
68.1
64.0

--- Page 21 ---

Task
Model
Epochs
Warmup
LR
Dropout
Dev
Test
QA
BERTje
{2}
{0.0, 0.3}
{3e-05, 5e-05, 0.0001}
{0.0, 0.1}
70.3
70.3
QA
RobBERTV1
{2}
{0.0, 0.3}
{3e-05, 5e-05, 0.0001}
{0.0, 0.1}
64.2
64.6
QA
RobBERTV2
{2}
{0.0, 0.3}
{3e-05, 5e-05, 0.0001}
{0.0, 0.1}
68.8
71.0
QA
RobBERT2022
{2}
{0.0, 0.3}
{3e-05, 5e-05, 0.0001}
{0.0, 0.1}
69.0
70.3
QA
mBERTcased
{2}
{0.0, 0.3}
{3e-05, 5e-05, 0.0001}
{0.0, 0.1}
71.7
72.4
QA
XLM-Rbase
{2}
{0.0, 0.3}
{3e-05, 5e-05, 0.0001}
{0.0, 0.1}
73.8
74.0
QA
mDeBERTaV3base
{2}
{0.0, 0.3}
{3e-05, 5e-05, 0.0001}
{0.0, 0.1}
79.9
79.0
QA
XLM-Rlarge
{2}
{0.0, 0.3}
{3e-05, 5e-05, 0.0001}
{0.0, 0.1}
82.6
81.4
QA
BERTbase
{2}
{0.0, 0.3}
{3e-05, 5e-05, 0.0001}
{0.0, 0.1}
61.8
62.5
QA
RoBERTabase
{2}
{0.0, 0.3}
{3e-05, 5e-05, 0.0001}
{0.0, 0.1}
68.4
69.7
QA
DeBERTaV3base
{2}
{0.0, 0.3}
{3e-05, 5e-05, 0.0001}
{0.0, 0.1}
77.7
79.1
QA
BERTlarge
{2}
{0.0, 0.3}
{3e-05, 5e-05, 0.0001}
{0.0, 0.1}
67.0
67.2
QA
RoBERTalarge
{2}
{0.0, 0.3}
{3e-05, 5e-05, 0.0001}
{0.0, 0.1}
75.0
76.2
QA
DeBERTaV3large
{2}
{0.0, 0.3}
{3e-05, 5e-05, 0.0001}
{0.0, 0.1}
84.2
84.7

```
