---
title: "2021-Center-The Catalan Language CLUB Catalan Language Understanding Benchmark - PDF Extract"
source_pdf: "2021-Center-The Catalan Language CLUB Catalan Language Understanding Benchmark.pdf"
pages: 8
extracted_at: "2026-02-13T13:13:45.187198"
---

# PDF Extract: 2021-Center-The Catalan Language CLUB Catalan Language Understanding Benchmark

**Source PDF:** 2021-Center-The Catalan Language CLUB Catalan Language Understanding Benchmark.pdf
**Total Pages:** 8

---

## Content

```
--- Page 1 ---

The Catalan Language CLUB⋆
Carlos Rodriguez-Penagos,1[0000−0001−8744−0380], Carme
Armentano-Oller1[0000−0002−9005−4138], Marta Villegas1[0000−0003−0711−0029],
Maite Melero1[0000−0001−9933−3224], Aitor Gonzalez1[0000−0002−6106−7810], Ona
de Gibert Bonet1[00000−0002−7163−4807], and Casimiro Carrino
Pio1[0000−0002−2314−9559]
Barcelona Supercomputing Center
{carlos.rodriguez1, carme.armentano, marta.villegas, maite.melero,
aitor.gonzalez, ona.degibert, casimiro.carrino,}@bsc.es
Abstract. The Catalan Language Understanding Benchmark (CLUB)
encompasses various datasets representative of diﬀerent NLU tasks that
enable accurate evaluations of language models, following the General
Language Understanding Evaluation (GLUE) example. It is part of AINA
and PlanTL, two public funding initiatives to empower the Catalan lan-
guage in the Artiﬁcial Intelligence era.
Keywords: Benchmark · NLU · Catalan
1
Introduction
Two public funding initiatives in Spain, PlanTL and AINA, aim at providing
Catalan with the tooling and resources that modern Artiﬁcial Intelligence (AI)
models can bring to industry, commerce and society in general. These initia-
tives are enabling high-quality corpora and datasets which, along with extensive
Transformer and Spacy1 language models, are being made available through var-
ious open platforms in order to enable Natural Language Understanding (NLU)
capabilities for any institution, organization, company or individual, and not
only for big corporations with deep pockets. These eﬀorts have incorporated
corpus annotation best practices, and at the same time strive to foster local
companies that can deal with the complex tasks needed for Data Science and
modern AI.
The Catalan Language Understanding Benchmark (CLUB) is a set of test cor-
pora to drive accurate evaluations of language models and downstream appli-
cations for real, practical use. As such, they are not modelled after usual lin-
guistic academic research corpus, but are designed for training and evaluating
Transformer models, powerful neural network embeddings in widespread use for
Artiﬁcial Intelligence applications.
⋆See Acknowledgements for institutional support
1 https://spacy.io/models/ca
arXiv:2112.01894v1  [cs.CL]  3 Dec 2021

--- Page 2 ---

2
C. Rodriguez-Penagos et al.
2
Datasets
We have compiled a new benchmark dataset suite for evaluating NLU capabilities
for Catalan, the Catalan Language Understanding Benchmark (CLUB).2 To
build it, we bootstrap from existing resources (such as the AnCora corpus3)
and create new high quality ones from scratch, adopting (and in some cases
improving on) existing guidelines. These datasets have permissive licences, and
are made publicly available through the Zenodo platform, under the Catalan AI
language resources community,4 and through HuggingFace.5
2.1
Data statements
In general, we provide as much curation information as possible following (Ben-
der and Friedman, 2018), [3] when relevant. For example, gender and socioeco-
nomic status are considered not as relevant for the kind of semantic annotations
created. However, the fact that all commissioned annotators (1) were native
speakers of Catalan, (2) were translators, editors, philologists or linguists, and
(3) had previous experience in language-related tasks, is considered to be impor-
tant. The curation rationale we follow was to make these datasets both repre-
sentative of contemporary Catalan language use, as well as directly comparable
to similar reference datasets from the General Language Understanding Evalu-
ation [6] (GLUE) benchmark.6 Since our datasets are geared towards Machine
Learning and Language Modelling, we have provided training, evaluation and
tests splits at HuggingFace. In what follows, we describe some of these datasets.
2.2
POS and NERC from AnCora
For Part-of-Speech Tagging (POS) and Named Entity Recognition and
Classiﬁcation (NERC) evaluations, we use annotations from the of the well-
known AnCora corpus, projected on the Universal Dependencies treebank7.
We extracted Named Entities from the original AnCora8 version, ﬁltering out
some unconventional ones, like book titles, and transcribe them into a standard
CONLL-IOB format.
The AnCora corpus has been released recently under CC-BY licence, and we
published our derivative version under the same licence.9
2 See https://huggingface.co/bsc
3 http://clic.ub.edu/corpus/en
4 https://zenodo.org/
5 https://huggingface.co/datasets/BSC-TeMU/
6 https://gluebenchmark.com/
7 https://github.com/UniversalDependencies/UD_Catalan-AnCora
8 https://doi.org/10.5281/zenodo.4762030
9 https://huggingface.co/datasets/BSC-TeMU/ancora-ca-ner

--- Page 3 ---

The Catalan Language CLUB
3
2.3
TECa: Textual Entailment for Catalan
Textual entailment (TE) is the directional relation between two sentences, a
premise and an hypothesis. For every premise the relation with an hypothesis
can be Neutral, Inference or Contradiction. Textual Entailment is considered an
important evaluation of the ability of a model to incorporate some measure of
inferential capabilities, as opposed to make do with a prodigious memory of what
it has actually seen before. TECa10 contains more than 20 000 pairs of sentences
annotated with their relation label, that can be 0 (neutral), 1 (inference) or 2
(contradiction).
Table 1: Example of a premise and a neutral, inference and contradiction hy-
pothesis.
Premise:
El Port de Barcelona ha guanyat un 30% el primer semestre
del 2016
Inference:
El Port de Barcelona augmenta la seva activitat
Neutral:
El segon semestre de 2016 no ha estat tan bo
Contradiction: L’inici del 2016 ha estat un mal any pel Port de Barcelona
Source sentences are extracted from the Catalan Textual Corpus11 and from
Vilaweb newswire.12
We randomly chose 18 000 sentences from those sources, and ﬁltered them by dif-
ferent criteria, such as length and stand-alone intelligibility. From the remaining
text sentences, we commissioned 3 hypotheses (one for each entailment category)
to be written by a team of annotators. We obtained more than 20 000 annotated
sentence pairs, which are published under CC-by licence. From 600 randomly
selected samples we cross-annotated for Quality Assurance, and obtained an
inter-annotator agreement of 83,57%.
2.4
Text Classiﬁcation: TeCla
TeCla13 (Textual Classiﬁcation for Catalan) is a Catalan News corpus for the-
matic Text Classiﬁcation tasks. It contains 153 265 articles classiﬁed under 30
diﬀerent categories, albeit editorially-oriented ones rather than truly encyclope-
dic labels.
We crawled 219 586 articles from the Catalan News Agency (ACN)14 newswire
archive, the latest from October 11, 2020. We used the subsection category as
10 https://doi.org/10.5281/zenodo.4761458
11 https://doi.org/10.5281/zenodo.4519349
12 http://www.vilaweb.cat
13 https://doi.org/10.5281/zenodo.4627197
14 http://www.acn.cat

--- Page 4 ---

4
C. Rodriguez-Penagos et al.
a classiﬁcation label, after excluding territorial labels and labels with less than
2 000 occurrences. With this criteria we compiled a total of 153 265 articles for
this text classiﬁcation dataset.
Bussiness
2.5%
Education
2.5%
Music
2.6%
Environment
2.8%
Parliament
3.8%
Economy
4.6%
Health
4.9%
Police
5.0%
Judicial
5.2%
Events
7.1%
Society
22.6%
Politics
16.7%
Parties
9.1%
Fig. 1: Label distribution of the Text Classiﬁcation dataset. Here, we show the
distribution of the ﬁltered dataset of labels with at least 2,000 instances.
2.5
Extractive Question Answering
For Extractive Question Answering we translated or created from scratch three
diﬀerent datasets: XQuAD-Ca, VilaQuAD and ViquiQuad.
XQuAD-Ca The Cross-lingual Question Answering Dataset15 is a multilingual
benchmark for evaluating question answering performance. The dataset consists
of a subset of 240 paragraphs from the Wikipedia and 1 190 question-answer
pairs from the development set of SQuAD v1.1 (Rajpurkar et al., 2016) together
with their professional translations into ten languages: Spanish, German, Greek,
Russian, Turkish, Arabic, Vietnamese, Thai, Chinese, and Hindi. Rumanian was
added later. We created a Catalan version using professional translators.
15 https://github.com/deepmind/xquad

--- Page 5 ---

The Catalan Language CLUB
5
ViquiQuAD Is an extractive Question Answering dataset16 using content from
the Catalan Wikipedia (Viquip`edia). 17 From a set of high quality, non-translation,
articles in the Catalan Wikipedia, 597 were randomly chosen, and from them 5-8
sentence contexts were extracted. We commissioned the creation of between 1
and 5 questions for each context, following an adaptation of the guidelines from
SQUAD 1.0 [4]. Annotators were native language speakers. In total, 15 153 pairs
of a question and an extracted fragment that contained the answer were created.
VilaQuAD Following the same guidelines as in 2.5, we developed VilaQuAD,18
an extractive QA dataset from newswire. From a the online edition of the catalan
newspaper Vilaweb,19 2 095 article headlines were randomnly selected. These
headlines were also used to create the Textual Entailment dataset (TECa). For
the extractive QA dataset, creation of between 1 and 5 questions for each news
context was commissioned to a team of native speakers. In total, 6 282 pairs of
a question and an extracted fragment that contains the answer were created.
Table 2: Statistics on the number of tokens in contexts, questions, and answers
in our QA datasets
XQuAD-ca ViquiQuAD VilaQuAD
Paragraph
48
597
2 095
Context
240
3 111
2 095
Total sentences
1 167
14 966
11 462
Sentences/context
4.9
4.81
5.5
Questions
1 189
15 153
6 282
Questions/context
4.9
4.9
3.0
Tokens in context
39 981
468 250
421 595
Tokens in questions
15 391
145 124
65 819
Tokens in questions/questions
12.96
9.58
10.48
Tokens in answers
4 424
63 157
27 676
Tokens in answers/answers
3.72
4.17
4.41
2.6
Semantic Textual Similarity: STS-ca
For Semantic Textual Similarity (STS) [1], we create a new dataset from scratch,
STS-ca20. It contains more than 3,000 sentence pairs, annotated with their se-
mantic similarity using a scale from 0 (no similarity at all) to 5 (semantic equiv-
alence).
16 https://doi.org/10.5281/zenodo.4562344
17 ca.wikipedia.org
18 https://doi.org/10.5281/zenodo.4562337
19 https://www.vilaweb.cat
20 https://doi.org/10.5281/zenodo.4529183

--- Page 6 ---

6
C. Rodriguez-Penagos et al.
Table 3: Question-answer reasoning typology. We sampled 100 random question-
answer pairs and classiﬁed them manually. We add SQuAD and FQuAD for
completeness.
XQuAD-ca ViquiQuAD VilaQuAD SQuAD FQuAD
Lexical variation
33.0%
7.0%
32.0%
33.3%
35.2%
World knowledge
16.0%
17.0%
16.0%
9.1%
11.1%
Syntactic variation
35.0%
43.0%
22.0%
64.1%
57.4%
Multiple sentence
17.0%
9.0%
16.0%
13.6%
17.6%
Table 4: Question type frequencies. Diﬀerences between XQuAD-ca and XQuAD-
en are explained because there are not unambiguous translations for some pro-
nouns.
XQuAD-ca ViquiQuAD VilaQuAD XQuAD-en
Quin/-s/-a/-es?
(Which?)
44.41%
22.42%
20.87 %
7.06%
Qu`e?
(What?)
16.32%
25.51%
22.59 %
57.31%
Qui?
(Who?)
10.18%
14.75%
18.45 %
10.00%
Quant/-s/-a/-es? (How many?)
8.16%
6.1%
9.57 %
6.55%
Com?
(How?)
7.82%
12.13%
8.21 %
5.13%
Quan?
(When?)
6.48%
6.5%
7.18 %
7.14%
Per qu`e?
(Why?)
1.26%
2.29%
4.36 %
1.26%
On?
(Where?)
3.2%
10.16 %
8.77 %
3.86%
Other
2.19%
0.14%
0%
1.93%
To develop STS-ca, we pre-selected potential sentence pairs from the CaText
corpus 21 by using diﬀerent similarity measures (Jaccard, Doc2Vec and Distil-
BERT [5] embedding cosine similarity). We did a ﬁnal manual review to ensure
that the selection represented superﬁcial and deep similarities in subject matter
and lexicon. Following the guidelines set in the SemEval challenges,22 we com-
missioned 4 native speaker annotators from 2 independent companies to assess
the similarity of the sentence pairs on a scale between 0 (completely dissimilar)
to 5 (completely equivalent), with other possible values, such as 3 (roughly equiv-
alent, but some important information diﬀers). Then, for each sentence pair, we
computed the mean of the four annotations, and we discarded single annotations
that deviate by more than 1 from the mean. After this ﬁltering process, we used
the mean of the remaining annotations as a ﬁnal score. Finally, in order to assess
the quality of the dataset, we measured the correlation of each annotator’s labels
with the average of the rest of the annotators, and averaged all the individual
correlations, resulting in a Pearson correlation of 0.739.
21 https://doi.org/10.5281/zenodo.4519349
22 http://ixa2.si.ehu.eus/stswiki

--- Page 7 ---

The Catalan Language CLUB
7
Table 5: Example from STS-ca
Sentence 1
Sentence 2
STS
Els
manifestants
ocupen
l’Imperial
Tarraco durant una hora fent jocs de
taula
Els
manifestants
ocupen
l’Imperial
Tarraco i fan jocs de taula
4
Aleshores hi posarem un got de vi i con-
tinuarem amb la cocci´o ﬁns que s’hagi
evaporat el vi i ho salpebrarem.
Mentre, hi posarem el vi al sofregit i
deixarem coure uns 7/8, ﬁns que el vi
s’evapori.
3
3
Evaluating Transformer models using CLUB
CLUB was created originally to evaluate the biggest embeddings yet deployed
for the Catalan language, using huge crawlings of the .cat domains, along with
speciﬁc ones of catalan government websites, resulting in a RoBERTa-base model
(BERTa)23 introduced in [2]. This model was created with more than 1 700 mil-
lion word tokens, and outperforms in these tasks all other mono or multilingual
models available for this Iberian language.
For our model, we leverage the Huggingface Transformers library [7]. For
each task, we attach a linear layer to the models and ﬁne tuned with the train-
ing set of the speciﬁc dataset. We trained each speciﬁc model under the same
settings across tasks consisting of 10 training epochs, with an eﬀective batch
size of 32 instances, a learning rate of 5e−5 and a maximum input length of 512
tokens for all the datasets but TECA, where we used 128 tokens. The rest of the
hyperparameters are set to the default values in Huggingface Transformers. We
select the best checkpoint as per the task-speciﬁc metric in the corresponding
validation set, and then evaluate it on the test set. We report the results and
metrics used in Table 6.24
Table 6: Results of BERTa Catalan model using CLUB.
QA viquiquad
STS
NERC
POS
TE
F1
EM
Pe/Sp
F1
F1
Acc
86.99
73.24
81.56
89.63
98.94
79.12
4
Further work
Project AINA will ensure that Catalan has the resources and models needed to
claim its rightful place in a global digital AI ecosystem. We are also designing
and commissioning other datasets, such as realistic chatbot conversations for
23 https://huggingface.co/PlanTL-GOB-ES/roberta-base-ca
24 We use F1 for POS and NERC, accuracy for TC, an average of Pearson and Spear-
man (Pe/Sp) coeﬃcient for STS and F1/Exact Match for QA (ViquiQuAD).

--- Page 8 ---

8
C. Rodriguez-Penagos et al.
customer support, Winograd tests, Sentiment Analysis corpora, etc. Also forth-
coming are Speech corpus, like the recently published ParlamentParla 25 (more
than 600 hours of speech from Catalan Parliament sessions) and contributions
to the Catalan Commonvoice campaigns.26. You can follow AINA through its
oﬃcial website. 27
5
Acknowledgments
This work was partially funded by the Generalitat de Catalunya through the
project PDAD14/20/00001, the State Secretariat for Digitalization and Artiﬁcial
Intelligence (SEDIA) within the framework of the Plan TL,28 and the MT4All
CEF project.
References
1. Agirre, E., Cer, D., Diab, M., Gonzalez-Agirre, A.: SemEval-2012 task 6: A pi-
lot on semantic textual similarity. In: *SEM 2012: The First Joint Conference on
Lexical and Computational Semantics – Volume 2: Proceedings of the Sixth In-
ternational Workshop on Semantic Evaluation (SemEval 2012). pp. 385–393. As-
sociation for Computational Linguistics, Montr´eal, Canada (7-8 Jun 2012), https:
//www.aclweb.org/anthology/S12-1051
2. Armengol-Estap´e, J., Carrino, C.P., Rodriguez-Penagos, C., de Gibert Bonet, O.,
Armentano-Oller, C., Gonzalez-Agirre, A., Melero, M., Villegas, M.: Are multilin-
gual models the best choice for moderately under-resourced languages? a compre-
hensive assessment for catalan (2021)
3. Bender, E.M., Friedman, B.: Data Statements for Natural Language Process-
ing: Toward Mitigating System Bias and Enabling Better Science. Transac-
tions of the Association for Computational Linguistics 6, 587–604 (12 2018).
https://doi.org/10.1162/tacl a 00041, https://doi.org/10.1162/tacl_a_00041
4. Rajpurkar, P., Zhang, J., Lopyrev, K., Liang, P.: Squad: 100,000+ questions for
machine comprehension of text (2016)
5. Sanh, V., Debut, L., Chaumond, J., Wolf, T.: Distilbert, a distilled version of BERT:
smaller, faster, cheaper and lighter. CoRR abs/1910.01108 (2019), http://arxiv.
org/abs/1910.01108
6. Wang, A., Singh, A., Michael, J., Hill, F., Levy, O., Bowman, S.R.: GLUE: A multi-
task benchmark and analysis platform for natural language understanding (2019),
in the Proceedings of ICLR.
7. Wolf, T., Debut, L., Sanh, V., Chaumond, J., Delangue, C., Moi, A., Cistac, P.,
Rault, T., Louf, R., Funtowicz, M., Davison, J., Shleifer, S., von Platen, P., Ma,
C., Jernite, Y., Plu, J., Xu, C., Scao, T.L., Gugger, S., Drame, M., Lhoest, Q.,
Rush, A.M.: Huggingface’s transformers: State-of-the-art natural language process-
ing (2020)
25 https://zenodo.org/record/5541827
26 https://commonvoice.mozilla.org
27 https://politiquesdigitals.gencat.cat/en/tic/aina-el-projecte-per-garantir-el-catala-en-lera-digita
28 https://www.plantl.gob.es/

```
