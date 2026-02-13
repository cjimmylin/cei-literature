---
title: "2021-Enevoldsen-DaCy A Unified Framework for Danish NLP - PDF Extract"
source_pdf: "2021-Enevoldsen-DaCy A Unified Framework for Danish NLP.pdf"
pages: 8
extracted_at: "2026-02-13T13:13:45.216525"
---

# PDF Extract: 2021-Enevoldsen-DaCy A Unified Framework for Danish NLP

**Source PDF:** 2021-Enevoldsen-DaCy A Unified Framework for Danish NLP.pdf
**Total Pages:** 8

---

## Content

```
--- Page 1 ---

DACY: A UNIFIED FRAMEWORK FOR DANISH NLP
Kenneth C. Enevoldsen
Interacting Minds Centre &
Center for Humanities Computing Aarhus
Aarhus University
Jens Chr. Skous Vej 4, Building 1483, 3rd ﬂoor
Denmark, 8000 Aarhus C
kenneth.enevoldsen@cas.au.dk
Lasse Hansen
Department of Clinical Medicine &
Center for Humanities Computing Aarhus
Aarhus University
Jens Chr. Skous Vej 4, Building 1483, 3rd ﬂoor
Denmark, 8000 Aarhus C
lasse.hansen@clin.au.dk
Kristoffer L. Nielbo
Interacting Minds Centre &
Center for Humanities Computing Aarhus
Aarhus University
Jens Chr. Skous Vej 4, Building 1483, 3rd ﬂoor
Denmark, 8000 Aarhus C
kln@cas.au.dk
ABSTRACT
Danish natural language processing (NLP) has in recent years obtained considerable improvements
with the addition of multiple new datasets and models. However, at present, there is no coherent
framework for applying state-of-the-art models for Danish. We present DaCy: a uniﬁed framework
for Danish NLP built on SpaCy. DaCy uses efﬁcient multitask models which obtain state-of-the-art
performance on named entity recognition, part-of-speech tagging, and dependency parsing. DaCy
contains tools for easy integration of existing models such as for polarity, emotion, or subjectivity
detection. In addition, we conduct a series of tests for biases and robustness of Danish NLP pipelines
through augmentation of the test set of DaNE. DaCy large compares favorably and is especially
robust to long input lengths and spelling variations and errors. All models except DaCy large display
signiﬁcant biases related to ethnicity while only Polyglot shows a signiﬁcant gender bias. We argue
that for languages with limited benchmark sets, data augmentation can be particularly useful for
obtaining more realistic and ﬁne-grained performance estimates. We provide a series of augmenters
as a ﬁrst step towards a more thorough evaluation of language models for low and medium resource
languages and encourage further development.
Keywords Natural Language Processing · Low-resource NLP · Data Augmentation · Danish NLP
1
Introduction
Danish Natural Language Processing (NLP) has seen a recent rise in resources with the introduction of the Danish
Gigaword Corpus (Derczynski et al., 2021), curated lists of Natural Language Processing (NLP) tools by DaNLP
(Brogaard Pauli et al., 2021) and sprogteknologi.dk, and at least ﬁve pretrained neural language models (Højmark-
Bertelsen, 2021; Møllerhøj, 2019; Tamini-Sarnikowski, 2020). Datasets and models are available for most common
tasks such as Named Entity Recognition (NER), Part-of-Speech (POS) tagging, dependency parsing, sentiment analysis,
and coreference resolution (Brogaard Pauli et al., 2021; “Sprogteknologi.dk”, 2021). However, no coherent, efﬁcient
and state-of-the-art framework exists for all fundamental NLP tasks. Models are developed and distributed as disjoint
projects and often require diverging package versions and have idiosyncratic APIs. These factors complicate workﬂows
and hamper further developments.
arXiv:2107.05295v1  [cs.CL]  12 Jul 2021

--- Page 2 ---

DaCy: A Uniﬁed Framework for Danish NLP
1.1
DaCy
With this motivation we present DaCy: an efﬁcient end-to-end framework for Danish NLP with state-of-the-art
performance on POS, NER and dependency parsing. DaCy ﬁlls the gap in Danish NLP by providing a consistent
interface that is easily extendable and able to integrate other models. DaCy is built on SpaCy v.3 which comes
with a range of advantages: the framework is optimized, user-friendly, and well-documented. DaCy includes three
ﬁne-tuned language models: DaCy small, based on a Danish Electra (14M parameters) (Højmark-Bertelsen, 2021);
DaCy medium, based on the Danish BERT (110M parameters) (Møllerhøj, 2019); and DaCy large, based on the
multilingual XLM-Roberta (550M parameters) (Conneau et al., 2020). All models have been ﬁne-tuned to do POS
tagging, NER, and dependency parsing in a single forward pass, which increases the efﬁciency of the model and allows
for larger models at the same computational cost.
Besides models ﬁne-tuned for DaCy, the package includes convenient wrappers to add other models to the pipeline.
For instance, Danish models for detecting polarity, emotion, and subjectivity classiﬁcation can be added in a single
line of code, and any HuggingFace Transformers (Wolf et al., 2020) model trained for sentence classiﬁcation can be
conveniently wrapped and included in the pipeline using utility functions. With this functionality, DaCy aims at being a
uniﬁed framework for Danish NLP. All functionality is well-documented and covered by tutorials.1
1.2
Robustness & Evaluation
Fine-tuned language models are commonly evaluated by testing performance on a gold-standard benchmark dataset.
The most commonly used benchmark for Danish is the DaNE dataset (Hvingelby et al., 2020), which consists of
the Danish Dependency Treebank (Johannsen et al., 2015), additionally tagged for NER. For languages with few
benchmarks datasets, such as Danish, the performance stability and generalizability can not be reliably estimated
(Ribeiro et al., 2020). For instance, the text included in DaNE was collected in the years 1983–1992 from both written
and spoken domains (Hvingelby et al., 2020). Given the change of languages over time and the addition of new textual
domains such as social media, this dataset is unlikely to be representative of the contemporary domains of application.
For instance, models might not be sufﬁciently exposed to e.g. abbreviated names, spelling errors, or non-standard
casing to correctly and robustly classify them. In this sense, the performance obtained on DaNE is unlikely to hold for
real-world use cases.
To provide an additional layer of validation, we propose evaluating models on augmented gold-standard data. Data
augmentation entails generating new data by slightly modifying existing data points (Feng et al., 2021). Data aug-
mentation techniques such as rotation and cropping are widely used in computer vision to reduce overﬁtting (Shorten
& Khoshgoftaar, 2019), and are becoming increasingly common in NLP (Chen et al., 2021). The complex syntactic
and semantic structure of text complicates the task of ﬁnding useful augmentations, but simple manipulations such
as synonym replacement and random character swaps and deletions have been found to be particularly useful for
supervised learning in low-resource settings (Wei & Zou, 2019).
Although data augmentation is most commonly used for increasing the amount of training data, it can just as well be
used for evaluation purposes (Ribeiro et al., 2020). By augmenting a gold-standard dataset, we can evaluate model
performance when exposed to data that more closely mimics real-life settings by adding spelling errors, more diverse
names, or other manipulations. In section 2.2, we introduce a series of augmentations and evaluate the performance of
Danish NLP pipelines on them.
The contributions of this paper are three-fold. 1) We introduce new state-of-art models for Danish dependency parsing,
NER and POS. 2) We introduce the DaCy Python library as a uniﬁed framework for state-of-the-art NLP in Danish. 3)
We evaluate Danish NLP pipelines using data augmentation and provide directions for future model development.
2
Methods
2.1
Training
To train the candidate models for DaCy, all publicly available language models for Danish were ﬁne-tuned on the DaNE
corpus (Hvingelby et al., 2020) using SpaCy 3.0.3 (Honnibal et al., 2020). The models include 2 Danish ELECTRAs
(Clark et al., 2020; Højmark-Bertelsen, 2021; Tamini-Sarnikowski, 2020), the Danish ConvBERT (Jiang et al., 2021;
Tamini-Sarnikowski, 2020), the Danish BERT (Devlin et al., 2019; Møllerhøj, 2019), and the multilingual XLM-Roberta
Large (Conneau et al., 2020). All models were trained with an input length of 10 sentences until convergence using
similar hyperparameters on a Quadro RTX 8000 GPU. Adam was used as optimizer with hyperparameters β1 = 0.9
1See: https://centre-for-humanities-computing.github.io/DaCy/
2

--- Page 3 ---

DaCy: A Uniﬁed Framework for Danish NLP
Table 1: Performance of models ﬁnetuned for DaCy. Highest scores are in bold and second highest is underlined. WPS
indicates words pr. second.
POS
NER
Dependency Parsing
Speed
Framework
Model
Accuracy
PER
LOC
ORG
MISC
Avg. F1
UAS
LAS
WPS
DaCy large
XLM-Roberta
98.39
95.53
83.90
77.82
80.16
85.20
90.59
88
4311
DaCy medium
DaBERT
97.93
89.62
83.09
67.35
70.69
78.47
87.88
85
8335
DaCy small
Ælæctra Cased
97.69
87.36
81.95
63.83
70.68
76.55
86.45
83
10671
DaELECTRA
97.40
82.80
77.39
63.01
66.95
73.16
85.20
82
9855
DaConvBERT
97.23
85.08
78.26
61.76
66.93
73.77
84.61
81
10029
and β2 = 0.999. Further, L2 normalization with α = 0.01 and gradient clipping with c = 1.0 was employed. For
increased efﬁciency, all models were trained with a multi-task objective (Caruana, 1997; Ruder, 2017) on NER, POS,
and dependency parsing. This allows the training of larger models at the same computational cost, but it is unlikely that
multi-task training at this scale improves performance (Aghajanyan et al., 2021; Raffel et al., 2020).2
Table 1 shows the performance of all ﬁne-tuned models evaluated on DaNE’s test set. The three best performing models
in each size category, XLM-Roberta, DaBERT, and Ælæctra Cased are included in DaCy as the large, medium and
small, respectively. In line with previous ﬁndings (Brown et al., 2020; Radford et al., 2019; Raffel et al., 2020), larger
models tend to perform better with XLM-Roberta obtaining the best performance across the board.
2.2
Evaluation
To evaluate the robustness of DaCy and other Danish NLP pipelines, we assessed their performance on multiple
augmented version of the DaNE test set. All Danish models are trained on the DaNE corpus which consists of a mix of
textual data of both spoken and written origin from the years 1983–1992 (Hvingelby et al., 2020), with the exception of
Polyglot which is trained on entities extracted from Wikipedia (Al-Rfou’ et al., 2013). As a consequence, the training
data is rarely representative of the domain in which the models will be applied. For example, social media, contemporary
news media, and historical texts have domain speciﬁc characteristics such as non-standard casing, a higher degree of
typos, use of hashtags, and historic spelling such as upper-cased nouns (Baldwin, 2012; Farzindar & Inkpen, 2015;
Tahmasebi, 2018). While it is infeasible to test the models on all possible domains, some of these characteristics can be
modelled using data augmentation which can provide practitioners with an estimate of the potential shortcomings of the
model. Further, data augmentation can be used to estimate biases against protected groups such as gender and ethnicity.
The augmenters presented here are not meant to be exhaustive, but rather a ﬁrst step towards more thorough validation of
new language models. We argue that the bar for inclusion of a new model should be set higher than a slight increase in
benchmark performance. Language models are used in a variety of contexts which current benchmarks tasks, especially
for low resource languages, do not capture. Our aim with these experiments is to provide an extra layer of insight into
the performance of language models that more closely mimics naturalistic use cases, and encourage the development of
further augmenters. Augmentation not only provides insights into when model performance breaks down, whether
certain models are more suited for speciﬁc use-cases than others, but can also be used for identifying speciﬁc areas to
improve upon.
The augmenters developed for this paper are designed in accordance with the SpaCy framework, and are thus not neces-
sarily tied to DaCy or Danish in particular and can be used both during model validation and training. Comprehensive
tutorials are provided on the DaCy Github repository.
We tested small, medium, and large SpaCy (Honnibal et al., 2020) and DaCy models, Stanza (Qi et al., 2020), Polyglot
(Al-Rfou’ et al., 2013), NERDA (Kjeldgaard, 2020), Flair (Akbik et al., 2019), and DaNLP’s BERT (Brogaard Pauli
et al., 2021) on the DaNE test set augmented with the following augmenters:
1. Keystroke augmentation: substitute 2%, 5%, or 15% of characters with a neighbouring character on a Danish
QWERTY keyboard.
2. ÆØÅ augmentation: substitute æ/Æ with ae/Ae, ø/Ø with oe/Oe, and å/Å with aa/Aa to simulate some historic
text variations in Danish.
3. Lower-case augmentation: convert all text to lower-case.
2For
a
full
list
of
models
and
training
conﬁgurations
see
the
conﬁg
ﬁles
on
Github:
https://github.com/
centre-for-humanities-computing/DaCy/tree/main/training
3

--- Page 4 ---

DaCy: A Uniﬁed Framework for Danish NLP
Table 2: Performance of Danish NLP pipelines. Wall Time is the time taken by the model to go through the DaNE test
set without augmentation. Stanza uses the spacy-stanza implementation. The speed of the DaNLP model is reported
as provided by the framework, which does not utilize batch input. However, given the model size it can be expected
to reach speeds comparable to DaCy medium. Empty cells indicates that the framework does not include the speciﬁc
model.
POS
NER
Dependency Parsing
Wall Time
Model
Accuracy
Person
Location
Organization
Misc
F1
F1 w/o Misc
LAS
UAS
GPU/CPU
DaCy large
98.37
93.33
84.88
76.49
80.16
84.39
85.65
88.44
90.85
2.9 / 34.7
DaCy medium
98.15
89.86
83.96
64.47
70.09
77.67
79.68
86.65
89.25
1.8 / 9.9
DaCy small
97.75
87.98
79.23
60.58
64.82
74.18
76.98
84.03
87.63
1.9 / 2.6
DaNLP BERT
92.27
83.90
71.13
72.84
83.20
37.4 / -
Flair
97.80
92.60
84.82
61.29
70.49
81.09
2.0 / -
NERDA
92.35
81.52
65.96
72.41
79.04
80.85
2.5 / -
Polyglot
76.26
79.25
68.06
40.69
56.67
65.32
- / 3.8
SpaCy large
96.30
86.17
84.16
63.36
65.52
75.75
78.57
78.01
81.95
0.9 / 1.4
SpaCy medium
95.71
84.55
77.29
63.16
63.25
73.23
76.01
77.73
81.87
1.2 / 1.4
SpaCy small
94.80
78.92
69.04
53.49
61.54
67.11
68.61
74.03
78.68
1.4 / 1.5
Stanza
97.62
83.84
87.34
29.3 / -
4. Spacing augmentation: randomly remove 5% of all whitespace.
5. Name augmentations:
(a) Substitute all names (PER entities) with randomly sampled Danish names, respecting ﬁrst and last names.
(b) Substitute all names with randomly sampled names of Muslim origin used in Denmark (Meldgaard,
2005), respecting ﬁrst and last names.
(c) Substitute all names with sampled Danish male names, respecting ﬁrst and last names.
(d) Substitute all names with sampled Danish female names, respecting ﬁrst and last names.
(e) Abbreviate all ﬁrst names to the ﬁrst character including a full stop.
The stochastic augmentations, i.e. name and keystroke augmentations, were repeated 20 times.
Previous evaluations of Danish NLP tools have used the gold-standard tokens instead of using a tokenization module.
While this allows for easier comparison of the speciﬁc modules it inﬂates the performance metrics of the models and is
unlikely to reﬂect the metric of interest, namely, the performance during application.3 All models were tested using
both their own tokenizer (if they have one) and the SpaCy tokenizer for Danish. The performance reported in section 3
uses the best peforming tokenization module for each pipeline. For all models except Stanza and Polyglot this was
found to be the SpaCy tokenizer.
3
Results
Table 2 shows the overall performance of Danish NLP frameworks on POS, NER, and dependency parsing on the
un-augmented DaNE test set. DaCy large obtains a new state-of-the-art on all tasks, most notably on NER and
dependency parsing. Regardless of model, performance for POS is stable around 98% accuracy. POS tagging has long
been at this level, and obtaining greater accuracy has been argued to require updates to the training data rather than new
architectures (Manning, 2011).
Tables 3 to 5 shows a detailed performance breakdown of the models on NER, POS, and dependency parsing on the
augmented data described in section 2.2. Overall, spelling variations and abbreviated ﬁrst names consistently reduce
performance of all models on all tasks. Even simple replacements of æ, ø, and å lead to performance degradation. In
general, larger models handle augmentations better than small models with DaCy large performing the best on all
augmentations with the exception of lower-casing. DaCy medium, DaNLP’s BERT, and NERDA are based on the
uncased Danish BERT (Møllerhøj, 2019), and are consequently not affected by casing. The BiLSTM-based models
(Stanza and Flair) perform competitively under augmentations and are only consistently outperformed by DaCy large.
On NER speciﬁcally, all models with the exception of DaCy large obtain signiﬁcantly worse performance on Muslim
names as compared to Danish names. The robustness of DaCy large likely stems from the multilingual pre-training
3In our experiments, several of the Danish models performed worse using their own tokenizer.
4

--- Page 5 ---

DaCy: A Uniﬁed Framework for Danish NLP
Table 3: NER performance of Danish NLP pipelines reported as average F1 scores excluding the MISC category. Best
scores are marked bold and second best are underlined. * denotes that the result is signiﬁcantly different from the
baseline using a signiﬁcance threshold of 0.05 with Bonferroni correction for multiple comparisons. Danish names is
considered the baseline for the augmentation of Muslim, female, and male names. Values in parentheses denote the
standard deviation. NERDA limits input size to 128 wordpieces which leads to truncation on long input sizes and high
rates of keystroke errors.
Deterministic Augmentations
Input Length
Names
Model
Baseline
Æøå
Lowercase
5 sentences
10 sentences
Abbreviated
DaCy large
85.6
83.5
69.7
86.5
86.5
80.1
DaCy medium
79.7
73.1
79.5
80.9
80.4
76.3
DaCy small
77.0
74.7
48.0
77.0
78.2
69.4
DaNLP BERT
83.2
78.6
83.1
78.6
61.9
78.1
Flair
81.1
80.2
24.4
81.0
80.9
74.9
NERDA
80.9
74.8
80.7
73.7
53.8
76.4
Polyglot
65.3
61.4
55.3
64.8
64.2
40.2
SpaCy large
78.6
75.4
5.7
78.8
78.8
78.0
SpaCy medium
76.0
74.7
9.7
76.5
76.8
76.0
SpaCy small
68.6
66.9
4.8
68.0
68.0
63.8
Stochastic Augmentations
Names
Keystroke Errors
Model
Danish
Muslim
Female
Male
2%
5%
15%
DaCy large
86.2 (0.6)*
86.0 (0.5)
86.2 (0.5)
86.2 (0.4)
82.0 (1.2)*
76.9 (1.3)*
61.3 (1.6)*
DaCy medium
80.3 (0.5)*
77.9 (0.8)*
80.3 (0.4)
80.2 (0.7)
65.5 (1.7)*
50.0 (1.6)*
25.8 (1.3)*
DaCy small
76.5 (0.9)
75.7 (0.7)*
76.7 (0.8)
76.6 (0.7)
70.7 (1.6)*
62.1 (1.5)*
41.3 (1.6)*
DaNLP BERT
82.9 (0.6)
81.0 (1.0)*
83.1 (0.5)
83.0 (0.7)
72.6 (1.2)*
60.9 (1.7)*
37.0 (1.5)*
Flair
81.2 (0.7)
79.8 (0.7)*
81.4 (0.5)
81.5 (0.5)
78.3 (0.9)*
73.5 (1.5)*
56.3 (1.7)*
NERDA
80.0 (1.1)*
78.1 (1.2)*
80.2 (0.8)
80.0 (0.8)
70.7 (1.4)*
57.5 (1.4)*
31.1 (1.6)*
Polyglot
63.1 (1.2)*
41.8 (0.7)*
61.2 (1.2)*
64.8 (1.2)*
57.4 (0.9)*
46.9 (1.9)*
24.7 (1.9)*
SpaCy large
79.5 (0.6)*
71.6 (1.1)*
79.8 (0.5)
79.4 (0.5)
72.1 (1.0)*
63.3 (1.5)*
44.9 (1.8)*
SpaCy medium
78.2 (0.7)*
69.2 (1.4)*
78.2 (0.7)
78.5 (0.8)
70.5 (1.3)*
64.2 (1.5)*
46.9 (1.6)*
SpaCy small
62.5 (1.6)*
57.8 (1.4)*
63.0 (1.1)
63.3 (0.9)
65.4 (0.7)*
60.5 (1.5)*
45.9 (1.6)*
Table 4: POS performance of Danish NLP pipelines reported as accuracy. Best scores are marked bold and second best
are underlined. * denotes that the result is signiﬁcantly different from baseline using a signiﬁcance threshold of 0.05
with Bonferroni correction for multiple comparisons. Values in parentheses denote the standard deviation. NERDA
limits input size to 128 wordpieces which leads to truncation on long input sizes and with a high degree of keystroke
errors.
Deterministic Augmentations
Stochastic Augmentations
Input Length
Keystroke Errors
Model
Baseline
Æøå
Lowercase
5 sentences
10 sentences
2%
5%
15%
DaCy large
98.4
97.5
95.5
98.5
98.4
95.5 (0.2)*
91.1 (0.2)*
75.4 (0.6)*
DaCy medium
98.2
96.5
98.1
97.8
97.9
93.6 (0.3)*
86.5 (0.3)*
63.3 (0.6)*
DaCy small
97.7
95.4
95.4
97.6
97.7
93.1 (0.2)*
85.9 (0.4)*
62.5 (0.4)*
Flair
97.8
95.0
95.0
97.7
97.7
94.7 (0.2)*
89.8 (0.3)*
72.1 (0.4)*
Polyglot
76.3
71.6
75.6
75.7
75.6
71.7 (0.2)*
65.3 (0.3)*
49.4 (0.4)*
SpaCy large
96.3
92.4
91.5
96.3
96.3
91.5 (0.2)*
84.8 (0.4)*
66.2 (0.5)*
SpaCy medium
95.7
92.4
91.6
95.8
95.7
91.0 (0.3)*
84.5 (0.3)*
66.0 (0.5)*
SpaCy small
94.8
90.5
90.3
94.8
94.8
90.7 (0.2)*
85.3 (0.3)*
69.1 (0.4)*
Stanza
97.6
96.1
95.4
97.7
97.7
94.8 (0.2)*
90.6 (0.3)*
75.6 (0.5)*
5

--- Page 6 ---

DaCy: A Uniﬁed Framework for Danish NLP
Table 5: Dependency parsing performance of Danish NLP pipelines reported as LAS. Best scores are marked bold
and second best are underlined. * denotes that the result is signiﬁcantly different from baseline using a signiﬁcance
threshold of 0.05 with Bonferroni correction for multiple comparisons. Values in parentheses denote the standard
deviation.
Deterministic Augmentations
Stochastic Augmentations
Input Length
Keystroke Errors
Model
Baseline
Æøå
Lowercase
5 sentences
10 sentences
2%
5%
15%
DaCy large
88.4
86.2
87.0
88.3
88.3
83.7 (0.4)*
76.6 (0.5)*
53.6 (0.8)*
DaCy medium
86.7
84.6
86.6
85.4
85.3
79.9 (0.5)*
69.9 (0.7)*
41.1 (0.9)*
DaCy small
84.0
79.0
82.7
83.5
83.0
76.8 (0.4)*
66.2 (0.8)*
38.0 (0.6)*
SpaCy large
78.0
71.0
74.0
77.6
77.6
69.7 (0.5)*
59.3 (0.7)*
34.8 (0.7)*
SpaCy medium
77.7
71.2
73.8
77.4
77.4
69.6 (0.6)*
59.5 (0.6)*
35.3 (0.7)*
SpaCy small
74.0
65.9
70.4
74.1
74.1
67.5 (0.4)*
59.1 (0.5)*
38.2 (0.7)*
Stanza
83.8
80.2
82.5
83.9
83.9
79.0 (0.4)*
71.9 (0.5)*
49.8 (0.9)*
and the model size. Similarly, DaCy small is robust to spelling errors and outperforms larger models such as DaNLP’s
BERT and NERDA, this is likely due to its well-curated training data (Derczynski et al., 2021). DaNLP’s BERT and
NERDA models were found to severely under-perform if given longer input lengths. DaCy’s models consistently
perform slightly better with more context, but are not vulnerable to shorter input. Lastly, as expected, the lack of casing
is especially detrimental for NER for the cased models, most notably Flair, the SpaCy models, DaCy large and DaCy
small.
4
Discussion
This paper has introduced the DaCy models and presented a thorough evaluation of Danish NLP models on a battery of
augmentations. DaCy models achieve state-of-the-art performance on Danish NER, POS, and dependency parsing,
and are robust to augmentations such as keystroke errors, name changes, and lowercasing. The results from training
DaCy underline three well-known trends in deep learning and NLP, 1) larger models tend to perform better, 2) higher
quality pre-training data leads to better models, as illustrated by the superior performance of Ælæctra compared to
DaELECTRA, and 3) multilingual models perform competitively with monolingual models (Brown et al., 2020; Raffel
et al., 2020; Xue et al., 2021).
Our experiments with multiple augmenters revealed different patterns of strengths and weaknesses across Danish NLP
models. In general, larger models tend to be more robust to data augmentations. Several models are highly sensitive
to casing, which limits their usefulness on certain domains. Evaluating models on augmented data provides a more
holistic and realistic estimate of the expected performance, and can reveal in which use cases one model might be more
useful than another. For example, it might be better to use DaCy medium on social media as opposed to DaCy large as
its performance is not affected by casing.
The purpose of the data augmentation experiments was to evaluate the robustness of Danish models and to open a
discussion on how to present new models going forward. As more models are developed for low and medium resource
languages, properly evaluating them becomes vital for securing robustness, transparency, and effectiveness despite
limited benchmark sets. We do not posit data augmentation as the only solution, but demonstrate that it can effectively
reveal performance differences on important factors such as casing, spelling errors, and biases related to protected
groups. As researchers, we bear the responsibility for releasing adequately tested and robust models into the world.
With the increasing ease of deployment, users must be made aware of the level of performance they can realistically
expect to achieve on their problem, and when to choose one model over another. Social media researchers should
know that certain models are sensitive to casing, historians should know that some models handle old text variations
such as ae, oe, aa poorly, and lawyers should be aware that models might not be able to identify abbreviated names as
effectively. In this regard, transparency and openness as to when and how models fail are crucial measures to report.
Such evaluation requires the development of infrastructure and tools, but is fast and easy to conduct once in place.
For instance, it only takes 8 minutes to test DaCy large on all augmented datasets including bootstrapping. As part of
the DaCy library, we provide several augmenters and utility functions for evaluation that integrate with SpaCy and
encourage new NLP models to use and expand upon them. For the continued development of low and medium resource
NLP in a direction that is beneﬁcial for practitioners, it is vital to conduct more thorough evaluation of new models. We
6

--- Page 7 ---

DaCy: A Uniﬁed Framework for Danish NLP
suggest these augmenters not as an evaluation standard, but as preliminary guiding principles for future development of
NLP models for low and medium resource languages in particular.
Abbreviations
NER Named Entity Recognition
NLP Natural Language Processing
POS Part-of-Speech
References
Aghajanyan, A., Gupta, A., Shrivastava, A., Chen, X., Zettlemoyer, L., & Gupta, S. (2021). Muppet: Massive multi-task
representations with pre-ﬁnetuning [version: 1]. arXiv:2101.11038 [cs]. Retrieved January 29, 2021, from
http://arxiv.org/abs/2101.11038
Akbik, A., Bergmann, T., Blythe, D., Rasul, K., Schweter, S., & Vollgraf, R. (2019). FLAIR: An easy-to-use framework
for state-of-the-art NLP. Proceedings of the 2019 Conference of the North American Chapter of the Association
for Computational Linguistics (Demonstrations), 54–59. https://doi.org/10.18653/v1/N19-4010
Al-Rfou’, R., Perozzi, B., & Skiena, S. (2013). Polyglot: Distributed word representations for multilingual NLP.
Proceedings of the Seventeenth Conference on Computational Natural Language Learning, 183–192. Retrieved
July 7, 2021, from https://aclanthology.org/W13-3520
Baldwin, T. (2012). Social media: Friend or foe of natural language processing? Proceedings of the 26th Paciﬁc Asia
Conference on Language, Information, and Computation, 58–59.
Brogaard Pauli, A., Barrett, M., Lacroix, O., & Hvingelby, R. (2021). DaNLP: An open-source toolkit for danish natural
language processing. Proceedings of the 23rd Nordic Conference on Computational Linguistics (NoDaLiDa
2021).
Brown, T. B., Mann, B., Ryder, N., Subbiah, M., Kaplan, J., Dhariwal, P., Neelakantan, A., Shyam, P., Sastry, G.,
Askell, A., Agarwal, S., Herbert-Voss, A., Krueger, G., Henighan, T., Child, R., Ramesh, A., Ziegler, D. M.,
Wu, J., Winter, C., ... Amodei, D. (2020). Language models are few-shot learners. arXiv:2005.14165 [cs].
Retrieved July 8, 2021, from http://arxiv.org/abs/2005.14165
Caruana, R. (1997). Multitask learning [Publisher: Springer]. Machine learning, 28(1), 41–75.
Chen, J., Tam, D., Raffel, C., Bansal, M., & Yang, D. (2021). An empirical survey of data augmentation for limited data
learning in NLP. arXiv:2106.07499 [cs]. Retrieved June 30, 2021, from http://arxiv.org/abs/2106.07499
Clark, K., Luong, M.-T., Le, Q. V., & Manning, C. D. (2020). ELECTRA: Pre-training text encoders as discriminators
rather than generators. arXiv:2003.10555 [cs]. Retrieved May 3, 2021, from http://arxiv.org/abs/2003.10555
Conneau, A., Khandelwal, K., Goyal, N., Chaudhary, V., Wenzek, G., Guzmán, F., Grave, E., Ott, M., Zettlemoyer, L.,
& Stoyanov, V. (2020). Unsupervised cross-lingual representation learning at scale. arXiv:1911.02116 [cs].
Retrieved May 2, 2021, from http://arxiv.org/abs/1911.02116
Derczynski, L., Ciosici, M. R., Baglini, R., Christiansen, M. H., Dalsgaard, J. A., Fusaroli, R., Henrichsen, P. J.,
Hvingelby, R., Kirkedal, A., Kjeldsen, A. S., Ladefoged, C., Nielsen, F. Å., Madsen, J., Petersen, M. L.,
Rystrøm, J. H., & Varab, D. (2021). The danish gigaword corpus. Proceedings of the 23rd Nordic Conference
on Computational Linguistics.
Devlin, J., Chang, M.-W., Lee, K., & Toutanova, K. (2019). BERT: Pre-training of deep bidirectional transformers for
language understanding. arXiv:1810.04805 [cs]. Retrieved December 30, 2019, from http://arxiv.org/abs/1810.
04805
Farzindar, A., & Inkpen, D. (2015). Natural language processing for social media [Publisher: Morgan & Claypool
Publishers]. Synthesis Lectures on Human Language Technologies, 8(2), 1–166.
Feng, S. Y., Gangal, V., Wei, J., Chandar, S., Vosoughi, S., Mitamura, T., & Hovy, E. (2021). A survey of data
augmentation approaches for NLP. arXiv:2105.03075 [cs]. Retrieved May 11, 2021, from http://arxiv.org/abs/
2105.03075
Højmark-Bertelsen, M. (2021). Ælæctra - a step towards more efﬁcient danish natural language processing. https:
//github.com/MalteHB/-l-ctra/
Honnibal, M., Montani, I., Van Landeghem, S., & Boyd, A. (2020). spaCy: Industrial-strength natural language
processing in python. Zenodo. https://doi.org/10.5281/zenodo.1212303
Hvingelby, R., Pauli, A. B., Barrett, M., Rosted, C., Lidegaard, L. M., & Søgaard, A. (2020). DaNE: A named entity
resource for danish. Proceedings of the 12th Language Resources and Evaluation Conference, 4597–4604.
Jiang, Z., Yu, W., Zhou, D., Chen, Y., Feng, J., & Yan, S. (2021). ConvBERT: Improving BERT with span-based
dynamic convolution. arXiv:2008.02496 [cs]. Retrieved July 6, 2021, from http://arxiv.org/abs/2008.02496
7

--- Page 8 ---

DaCy: A Uniﬁed Framework for Danish NLP
Johannsen, A., Alonso, H. M., & Plank, B. (2015). Universal dependencies for danish. Proceedings of the Fourteenth
International Workshop on Treebanks and Linguistic Theories.
Kjeldgaard, L. (2020). NERDA. https://github.com/ebanalyse/NERDA
Manning, C. D. (2011). Part-of-speech tagging from 97% to 100%: Is it time for some linguistics? In A. F. Gelbukh (Ed.),
Computational linguistics and intelligent text processing (pp. 171–189). Springer. https://doi.org/10.1007/978-
3-642-19400-9_14
Meldgaard, E. V. (2005). Muslimske fornavne i Danmark [Publisher: Københavns Universitet]. Retrieved July 7, 2021,
from https://nors.ku.dk/publikationer/webpublikationer/muslimske_fornavne/
Møllerhøj, J. D. (2019, December 5). Danish BERT model: BotXO has trained the most advanced BERT model.
[BotXO]. Retrieved December 26, 2019, from https://www.botxo.ai/blog/danish-bert-model/
Qi, P., Zhang, Y., Zhang, Y., Bolton, J., & Manning, C. D. (2020). Stanza: A python natural language processing toolkit
for many human languages. arXiv:2003.07082 [cs]. Retrieved May 2, 2021, from http://arxiv.org/abs/2003.
07082
Radford, A., Wu, J., Child, R., Luan, D., Amodei, D., & Sutskever, I. (2019). Language models are unsupervised
multitask learners. OpenAI blog, 1(8), 9.
Raffel, C., Shazeer, N., Roberts, A., Lee, K., Narang, S., Matena, M., Zhou, Y., Li, W., & Liu, P. J. (2020). Exploring
the limits of transfer learning with a uniﬁed text-to-text transformer. arXiv:1910.10683 [cs, stat]. Retrieved
November 25, 2020, from http://arxiv.org/abs/1910.10683
Ribeiro, M. T., Wu, T., Guestrin, C., & Singh, S. (2020). Beyond accuracy: Behavioral testing of NLP models with
CheckList. Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics, 4902–
4912. https://doi.org/10.18653/v1/2020.acl-main.442
Ruder, S. (2017). An overview of multi-task learning in deep neural networks. arXiv:1706.05098 [cs, stat]. Retrieved
July 6, 2021, from http://arxiv.org/abs/1706.05098
Shorten, C., & Khoshgoftaar, T. M. (2019). A survey on image data augmentation for deep learning. Journal of Big
Data, 6(1), 60. https://doi.org/10.1186/s40537-019-0197-0
Sprogteknologi.dk. (2021). Retrieved June 30, 2021, from https://sprogteknologi.dk/
Tahmasebi, N. (2018). A study on word2vec on a historical swedish newspaper corpus. Proceedings of the Digital
Humanities in the Nordic Countries 3rd Conference, DHN 2018, Helsinki, Finland, March 7-9, 2018., 25–37.
http://ceur-ws.org/Vol-2084/paper2.pdf
Tamini-Sarnikowski, P. T. (2020). Danish transformers. https://github.com/sarnikowski
Wei, J., & Zou, K. (2019). EDA: Easy data augmentation techniques for boosting performance on text classiﬁcation
tasks. Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and
the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP), 6382–6388.
https://doi.org/10.18653/v1/D19-1670
Wolf, T., Debut, L., Sanh, V., Chaumond, J., Delangue, C., Moi, A., Cistac, P., Rault, T., Louf, R., Funtowicz, M.,
Davison, J., Shleifer, S., von Platen, P., Ma, C., Jernite, Y., Plu, J., Xu, C., Scao, T. L., Gugger, S., ... Rush,
A. M. (2020). HuggingFace’s transformers: State-of-the-art natural language processing. arXiv:1910.03771
[cs]. Retrieved June 30, 2021, from http://arxiv.org/abs/1910.03771
Xue, L., Constant, N., Roberts, A., Kale, M., Al-Rfou, R., Siddhant, A., Barua, A., & Raffel, C. (2021). mT5: A
massively multilingual pre-trained text-to-text transformer. arXiv:2010.11934 [cs]. Retrieved July 6, 2021,
from http://arxiv.org/abs/2010.11934
8

```
