---
title: "2023-Oslo-NorBench A Benchmark for Norwegian Language Models - PDF Extract"
source_pdf: "2023-Oslo-NorBench A Benchmark for Norwegian Language Models.pdf"
pages: 16
extracted_at: "2026-02-13T13:13:45.475814"
---

# PDF Extract: 2023-Oslo-NorBench A Benchmark for Norwegian Language Models

**Source PDF:** 2023-Oslo-NorBench A Benchmark for Norwegian Language Models.pdf
**Total Pages:** 16

---

## Content

```
--- Page 1 ---

NorBench – A Benchmark for Norwegian Language Models
David Samuel,1 Andrey Kutuzov,1 Samia Touileb,2 Erik Velldal,1 Lilja Øvrelid,1
Egil Rønningstad,1 Elina Sigdel1 and Anna Palatkina1
1University of Oslo, Language Technology Group
2University of Bergen, MediaFutures
Abstract
We present NorBench: a streamlined suite
of NLP tasks and probes for evaluating Nor-
wegian language models (LMs) on stan-
dardized data splits and evaluation metrics.
We also introduce a range of new Norwe-
gian language models (both encoder and
encoder-decoder based). Finally, we com-
pare and analyze their performance, along
with other existing LMs, across the differ-
ent benchmark tests of NorBench.
1
Introduction
This paper provides a suite of standardized tasks
and probes for benchmarking of Norwegian lan-
guage models (LMs). In addition to collecting a
broad range of annotated datasets, we provide pre-
cise task deﬁnitions, pre-deﬁned data splits and
evaluation metrics, with corresponding scripts for
streamlining the entire benchmarking pipeline. The
resulting resource is dubbed NorBench. We further-
more present a range of new transformer-based lan-
guage models (LMs) for Norwegian, trained with
optimized conﬁgurations and architectures, and on
different corpora with different pre-processing. Our
contributions are as follows:
1. We introduce NorBench, a collection of Nor-
wegian datasets and evaluation scripts that
ensures simple, fair and standardized com-
parison between Norwegian LMs. The ex-
isting models from prior work are evaluated
and compared. All data and code related to
NorBench are publicly available online.1
2. An integral part of NorBench is diagnostic
set of tasks that probe the afﬁnity of LMs
towards gender-bias and toxic language – an
unfortunate side-effect for many models pre-
trained on large amounts of text.
1https://github.com/ltgoslo/norbench
Task
Train
Dev
Test
Morpho-syntactic token-level tasks
Tokens in UD tasks
489 217
67 619
54 739
Named entities
23 071
2 942
2 393
Sentiment analysis
SA documents
34 903
4 360
4 351
SA sentences
7 973
1 411
1 181
SA targets
5 044
877
735
Linguistic acceptability
NoCoLA sentences
116 195
14 289
14 383
Question answering
NorQuAD questions
3 808
472
472
Machine translation
Bokm˚al–Nynorsk sentences
10 000
10 000
10 000
Table 1: Number of labeled entities in the training,
development, and test splits in the datasets used for
the NorBench tasks.
3. We develop a new generation of Norwegian
LMs – NorBERT3 and NorT5 – that achieve
state-of-the-art performance across most Nor-
Bench tasks. We provide multiple sizes of
these models and show that even small ver-
sions maintain competitive performance.
4. We empirically test the impact of different
available Norwegian training corpora on the
downstream performance. Our results suggest
that pre-training on a simple concatenation of
all available resources is not always beneﬁcial.
The rest of the paper is structured as follows. Sec-
tion 2 provides an overview of the tasks included
in NorBench. In Section 3, the details of our eval-
uation workﬂow are outlined. The architecture
and the training collections of our novel LMs are
described in Section 4, while in Section 5, we sum-
marize and analyze the benchmarking results. Sec-
tion 6 brieﬂy describes prior work, while we point
out directions for future work in Section 7, before
concluding in Section 8.
arXiv:2305.03880v1  [cs.CL]  6 May 2023

--- Page 2 ---

2
NorBench task descriptions
We here brieﬂy describe each task and associated
dataset. The number of training examples for the
different datasets and their train, development, and
test splits are provided in Table 1. For the full
details about each task, we refer the reader to the
NorBench GitHub repository. Before we describe
the various tasks, we ﬁrst brieﬂy comment on the
two ofﬁcial varieties of written Norwegian.
Bokm˚al and Nynorsk
Norwegian has two ofﬁ-
cial written standards: Bokm˚al (BM), used by 85–
90% of the Norwegian population, and Nynorsk
(NN). While they are closely related, there can be
relatively large lexical differences. The contextu-
alised LMs presented in this paper are therefore
trained jointly on both varieties, but with the minor-
ity variant Nynorsk represented by comparatively
less data than Bokm˚al (reﬂecting the natural usage).
Several previous studies have indicated that joint
modeling of Bokm˚al and Nynorsk works well for
many NLP tasks, like tagging and parsing (Velldal
et al., 2017) and NER (Jørgensen et al., 2020). In
cases where the labeled data for our benchmark
tasks are available as separate versions for Bokm˚al
and Nynorsk, we ﬁne-tune models jointly on the
combined BM/NN data. One practical advantage
of training joint and ‘variety agnostic’ models, is
that only a single model needs to be maintained,
and we bypass the need for a separate ‘language
identiﬁcation’ step.
2.1
Morpho-syntactic token-level tasks
UD tasks
We use the Norwegian Universal De-
pendencies Treebank (Øvrelid and Hohle, 2016;
Velldal et al., 2017) from UD 2.11,2 in turn con-
verted from NDT (Solberg et al., 2014). In order
to evaluate the general performance on Norwegian,
we concatenate the Bokm˚al (BM) and Nynorsk
(NN) datasets for both ﬁne-tuning and evaluation.
The models are challenged to predict universal part-
of-speech tags (UPOS), universal features (UFeats),
lemmas and dependency trees (Nivre et al., 2016).
UPOS tags cover the basic POS categories (17
tags) and UFeats differentiate more ﬁne-grained
lexical and grammatical properties of words, e.g.
number, gender, and tense (172 tags in total). Both
tagging tasks use the standard accuracy metric.
Lemmatization evaluates how well a language
model understands Norwegian morphology and in
2http://hdl.handle.net/11234/1-4923
order to transform an inﬂected word into its lemma-
tized form. An integral part of lemmatization – in
our variety-agnostic setting – is implicit language
identiﬁcation, because Bokm˚al and Nynorsk have
different lemmatization standards. Correct predic-
tion requires exact match with the gold lemma; we
report the aggregated token-wise accuracy.
Dependency parsing involves identifying the re-
lationships between words in a sentence, result-
ing in a dependency tree that represents the gram-
matical structure of the sentence. By evaluating
the quality of dependency parsing outputs by a
language model, one can determine its ability to
recognize and categorize the grammatical roles of
words based on their syntactic function. We report
the labeled attachment score (LAS), the standard
evaluation metric for dependency parsing.3
Named entity recognition
We use the NorNE4
dataset which annotates the UD/NDT (for both
Bokm˚al and Nynorsk) with named entities
(Jørgensen et al., 2020).
We predict 8 entity
types: Person (PER), Organization (ORG), Loca-
tion (LOC), Geo-political entity, with a locative
sense (GPE-LOC), Geo-political entity, with an
organization sense (GPE-ORG), Product (PROD),
Event (EVT), and Nominals derived from names
(DRV). The evaluation metric used is ‘strict’ micro
F1, requiring both the correct entity type and exact
match of boundary surface string. It is computed
using the code for the SemEval’13 Task 9.5
2.2
Sentiment analysis
Document-level ternary polarity classiﬁcation
The Norwegian Review Corpus (NoReC; 2nd re-
lease) (Velldal et al., 2018) comprises 43 425 pro-
fessional reviews from a range of Norwegian news
sources, and covering a range of different domains
(e.g., books, movies, games, music, various con-
sumer goods, etc.). The average length of a docu-
ment is 389 words. While the reviews originally
come with numerical ratings on a scale of 1–6,
we here conﬂate these to three classes; negative
(ratings 1–3), fair (4), and positive (5–6). This
mapping is done to avoid problems with too few
examples for the ratings in the extreme ends of the
numerical scale. The dataset comes with prede-
3https://universaldependencies.org/
conll18/evaluation.html
4https://github.com/ltgoslo/norne
5https://github.com/davidsbatista/
NER-Evaluation

--- Page 3 ---

ﬁned data splits (chronologically sorted), and we
evaluate using macro F1.
Sentence-level ternary sentiment classiﬁcation
We include the dataset NoReCsentence6 for training
and evaluating on the task of sentence-level polarity
classiﬁcation with respect to three classes (positive,
negative, or neutral). As described by Kutuzov et al.
(2021), this data is derived from NoReCﬁne (Øvre-
lid et al., 2020), a subset of NoReC, by aggregating
the ﬁne-grained annotations to the sentence-level,
removing sentences with mixed sentiment. The
evaluation metric is macro F1.
Targeted
sentiment
analysis
We
use
the
NoReCtsa7 dataset for the task of targeted senti-
ment analysis (TSA). As described in Rønningstad
et al. (2022), the data is derived from NoReCﬁne
by only including target expressions and the
associated positive/negative polarity. The task is to
jointly predict the target spans and their polarity,
and we use the same evaluation strategy as for
NER.
2.3
Linguistic acceptance
NoCoLA
Norwegian corpus of linguistic accep-
tance (NoCoLA; Jentoft and Samuel, 2023) is used
to evaluate language models on their understanding
of Norwegian grammaticality. NoCoLA is derived
from the ASK Corpus – a language learner corpus
of Norwegian as a second language (Tenfjord et al.,
2006), which contains texts written exclusively in
Norwegian Bokm˚al, not covering the Nynorsk vari-
ety. We report the Matthews correlation coefﬁcient
(MCC; Matthews, 1975) on NoCoLAclass, the of-
ﬁcial binary sentence classiﬁcation variant of the
dataset.
2.4
Question answering
NorQuAD
is a Norwegian extractive question
answering dataset which consists of 4 752 manually
created question-answer pairs based on Wikipedia
and news articles (Ivanova et al., 2023).8 We here
report token-level F1; human performance on the
test portion of the dataset has been measured at
91.1% F1 (Ivanova et al., 2023).
6https://github.com/ltgoslo/norec_
sentence
7https://github.com/ltgoslo/norec_tsa
8https://github.com/ltgoslo/NorQuAD
2.5
Machine translation
Bokm˚al–Nynorsk translation.
The fact that a
monolingual Norwegian language model is actu-
ally trained on two language varieties – Bokm˚al
and Nynorsk – allows us to evaluate generative
models on machine translation. We collect the
available Bokm˚al–Nynorsk bitexts,9 deduplicate
the sentences on both sides and split them into
training, development, and test portions, each with
10 000 parallel sentences. We evaluate the transla-
tion from Bokm˚al to Nynorsk using SacreBLEU
(Lin and Och, 2004; Post, 2018).10
2.6
Diagnostics of harmful predictions
Unlike the previous items, this is not a ‘task’, but
rather a description of important model properties.
We follow previous works on Norwegian to probe
our language models for gender bias in occupa-
tions, as well as assessing the harmfulness of their
sentence completions (Touileb et al., 2023, 2022;
Touileb and Nozza, 2022).
3
NorBench baseline methodology
Below we describe various choices pertaining to
ﬁne-tuning the LMs for the various tasks. Note
that, all of the approaches described here should be
considered baselines, in the sense that the goal is
not to produce state-of-the-art results, but rather to
implement simple evaluation approaches allowing
for a fair comparison of different LMs across the
various tasks.
3.1
A joint model for UD tasks
Since the UD tasks are annotated within the same
dataset, we evaluate them jointly with a single
multi-task model. We follow the multi-task setup
from UDify (Kondratyuk and Straka, 2019): ﬁrst,
we take a separate weighted convex combination of
hidden layers for every subtask. Then, we average-
pool these contextualized subword representations
to get a vector embedding for each token. Finally,
these vectors are input to classiﬁcation heads for
9Provided
by
the
National
Library
of
Nor-
way:
https://www.nb.no/sprakbanken/
ressurskatalog/oai-nb-no-sbr-78/,
https:
//www.nb.no/sprakbanken/ressurskatalog/
oai-nb-no-sbr-47/
10The SacreBLEU metric involves several parame-
ters that change the outcomes (Post, 2018),
we use
BLEU with no smoothing,
13a tokenization and no
lowercasing – the default values in torchmetrics
0.11.4:
https://torchmetrics.readthedocs.
io/en/stable/text/sacre_bleu_score.

--- Page 4 ---

UPOS and UFeats tagging, to a classiﬁcation head
for predicting lemma transformation rules, and to
biafﬁne attention heads for dependency parsing
(Dozat and Manning, 2017).
3.2
Text classiﬁcation
For document- and sentence-level sentiment anal-
ysis, together with classiﬁcation of linguistic ac-
ceptability, we utilize the same text classiﬁcation
approach, based on the widely-used ﬁne-tuning
scheme from Devlin et al. (2019). There, every
tokenized text sequence is preﬁxed by a special
[CLS] token, appended by a [SEP] token and
passed into a pre-trained language model, which
produces a contextualized representation for the
special [CLS] token. Finally, this representation is
passed into the downstream classiﬁer that produces
the ﬁnal prediction among the available classes.
For the encoder-decoder models, we chose three
target words as the class labels (‘negativ’, ‘nøytral’
and ‘positivt’) and ﬁne-tuned the models to gener-
ate these target words given the input text. At the
inference time, an input text is assigned a class de-
pending on whether the corresponding target word
occurs in the generated text.
3.3
Sequence labeling for NER and TSA
NER and TSA are approached as a sequence label-
ing task where we classify text spans by tagging
tokens with beginning-inside-outside tags (BIO;
Ramshaw and Marcus, 1995).
3.4
Question answering
We follow the SQuAD ﬁne-tuning method intro-
duced in BERT (Devlin et al., 2019). For every
question and context passage, the goal is to iden-
tify the answer within the passage. The question
and passage texts are concatenated together and the
evaluated model is trained to predict the ﬁrst and
last token of the answer – the problem is cast as
2-task binary classiﬁcation problem.
3.5
Machine translation
We use this task only for evaluation of generative
sequence-to-sequence models such as T5s (Raffel
et al., 2020). This task naturally ﬁts these mod-
els – the source sentence is encoded and the target
sentence is decoded with the respective parts of
the model. We use simple greedy decoding for
generation during inference.
3.6
Probing for gender-bias and harmfulness
We take advantage of the MLM objective of the
models, and create templates consisting of gen-
dered head-words, followed by predicates.
Gender-bias
To probe for gender bias in occupa-
tions, we follow and use the templates of Touileb
et al. (2023) and Touileb et al. (2022). These tem-
plates are sequences of masked gendered head-
words (e.g. the woman, the man, the sisters, the
uncles ...), followed by predicates pertaining to
verbs related to performing an occupation (e.g. is,
was, worked as, ...), followed by a set of occu-
pations extracted from the Norwegian Statistics
bureau (Touileb et al., 2022). Using the proba-
bilities of the masked gendered head-words, we
compute the two bias scores: normative and de-
scriptive as deﬁned by Touileb et al. (2023). The
normative score compares the gender-based aggre-
gated probability distributions of templates with a
normative distribution of genders in occupations.
The idea here is that genders should be equally
represented in each occupation with a gender dis-
tribution falling between 45% and 55% for each
occupation. The descriptive bias score compares
the probability distribution of genders across occu-
pations as represented in language models, to the
real world distribution of these genders based on
the Norwegian Statistics bureau data.
Harmfulness
We also follow Touileb and Nozza
(2022) to assess the harmfulness of sentence-
completions of each language model.
We use
their templates, constructed similarly to the previ-
ous templates where the head-words are gendered-
nouns followed by predicates as deﬁned by Nozza
et al. (2021), and where the last token is masked.
The probing is therefore aiming at completing sen-
tences, by looking at top one, ﬁve, ten, and twenty
most likely words for each template. Once the com-
pletions returned by the models, we compute the
HONEST score (Nozza et al., 2021). This score is
a word-level completion score that maps generated
completions to their respective language-speciﬁc
HurtLex (Bassignana et al., 2018) lexicon of offen-
sive words. The scores represent the total number
of completions existing in the lexicon compared to
the total amount of returned completions.
4
New Norwegian language models
A number of large Norwegian language models
have appeared in recent years:
to name only

--- Page 5 ---

the masked LMs, Kutuzov et al. (2021) trained
NorBERT1, followed by NorBERT2, and Kummer-
vold et al. (2021) introduced NB-BERT models,
coming in different sizes. In this paper, we present
a set of novel masked and text-to-text LMs for
Norwegian trained according to the LTG-BERT
training recipe by Samuel et al. (2023). We dub
these models NorBERT3 and NorT5 and evaluate
their performance across different model sizes and
training corpora.
4.1
Training corpora
Text sources
Our LM training dataset included
the following text collections:
• Norwegian Wikipedia dumps (BM/NN) from
October 2022; about 180 million words;
• NBDigital, public domain texts released by the
National Library (NB) of Norway in 2015; 660
million words;11
• Norwegian News Corpus (NAK): a collection
of Norwegian news texts (both Bokm˚al and
Nynorsk) published between 1998 and 2019;
1.7 billion words;12
• Norwegian Colossal Corpus (NCC): the pub-
lic part of the large and heterogenous corpus
released by NB in 202213 (Kummervold et al.,
2021); about 6.9 billion words;
• Norwegian part of web-crawled mC4 corpus
(Xue et al., 2021); about 15 billion words.
The ‘standard’ models were trained on the con-
catenation of these corpora, yielding a training
collection of about 25 billion word tokens.
In
Section 5.2, we investigate the effects of ‘over-
sampling’ higher-quality sources and training sep-
arate models from scratch on NAK, NCC, mC4,
Wikipedia, and NBDigital.
Deduplication
Before training, all the corpora
were de-duplicated on the paragraph-level, using
SimHash14 and removing exact duplicates. The
same was done across corpora, reducing their size
up to 10%, depending on the corpus.
11https://www.nb.no/sprakbanken/en/
resource-catalogue/oai-nb-no-sbr-34/
12https://www.nb.no/sprakbanken/
ressurskatalog/oai-nb-no-sbr-4/
13https://huggingface.co/datasets/
NbAiLab/NCC
14https://github.com/ChenghaoMou/
text-dedup
Hyperparameter
x-small
small
base
large
Number of parameters
15M
40M
123M
353M
Number of layers
12
12
12
24
Hidden dimension
192
384
768
1 024
Attention heads
3
6
12
16
Table 2: The main hyperparameters of our four con-
ﬁgurations of NorBERT3 language models. Full
list of hyperparameters is given in Table 9.
Filtering
Since the largest portion of our train-
ing corpus is sourced from web-crawled texts, it is
crucial to ﬁlter out any unnatural language. Even
though our main web-text source is the multilingual
Colossal Clean Crawled Corpus (mC4), it still con-
tains noisy texts (Dodge et al., 2021), which was
also apparent when we manually investigated some
of the Norwegian samples. We follow the ﬁltering
heuristics implemented for the MassiveText corpus
(Rae et al., 2021) and adapt them for Norwegian.
4.2
Architecture
We employ the masked language modeling ap-
proach for pre-training NorBERT3 language mod-
els and follow the optimized training method from
Samuel et al. (2023). This approach differs from
the standard BERT (Devlin et al., 2019) training as
follows:
1. Liu et al. (2019) found out that BERT is under-
trained and the next-sentence prediction task is
unnecessary – we thus pre-train for 8× more
steps, use sequence length of 512 throughout
the whole training, and utilize only the masked
language modeling task (MLM) without next-
sentence prediction.
2. SpanBERT (Joshi et al., 2020) and T5 (Raf-
fel et al., 2020) demonstrated the advantages
of masking random spans instead of individual
subwords as in Devlin et al. (2019). Thus, for
our MLM objective, the data loader iteratively
samples random spans until 15% of the input
text is masked. The length of each span is sam-
pled from Geo(p), where p = 1/3.
3. Samuel et al. (2023) compared various conﬁgu-
rations of transformer architectures and of the
training hyperparameters. We employ the best
performing setting for our pre-training. Crucial
upgrades involve using the NormFormer layer
normalization (Shleifer and Ott, 2022), disentan-
gled attention with relative positions (He et al.,

--- Page 6 ---

2021) and increased amount of weight decay.
Please refer to Samuel et al. (2023) for more
pre-training details.
Parameter count
We train four LMs of different
sizes (Table 2), accommodating users with vary-
ing degrees of computational resources, and to es-
tablish a baseline performance across LMs with
different number of parameters.
Vocabulary and tokenizer
We utilize Word-
Piece subword tokenizer (Wu et al., 2016) and set
its vocabulary size to 50 000. Following GPT-2
(Radford et al., 2019), we represent the text as a
sequence of UTF-8 bytes instead of Unicode char-
acters, which substantially reduces the number of
out-of-vocabulary tokens. We train the tokenizer on
the full corpus utilizing the open implementation
from the tokenizers library.15
NorT5
Some NLP tasks, for example machine
translation, require a generative language model.
Thus we extend the encoder-only architecture of
NorBERT3 to full encoder-decoder transformer and
pre-train the resulting model, dubbed NorT5, on
text-to-text masked language modeling (T5; Raffel
et al., 2020). We use the same text corpus, tok-
enizer and training settings as in NorBERT3 when
applicable. For the T5-speciﬁc training choices, we
follow T5 version 1.1 – i.e. pre-training only on
self-supervised masked LM and no parameter shar-
ing between the embedding and classiﬁer layer.16
4.3
Pre-training details
In order to reduce training time, pre-training is par-
allelized over multiple GPUs with the global batch
size of 8 192. The number of GPUs used depends
on the size of pre-trained language models, ranging
between 16 and 512 AMD Instinct MI250X GPUs,
each with 128GB memory. The amount of training
steps is 250 000, increasing the training budget of
the original BERT models 8 times. NorBERT3, base
was pre-trained in 280 hours using this setting.
5
Benchmarking results
In addition to our NorBERT3 models, we also
benchmark these existing models:
15https://github.com/huggingface/
tokenizers
16https://github.com/google-research/
text-to-text-transfer-transformer/blob/
main/released_checkpoints.md#t511
• BERT (Devlin et al., 2019): to get a baseline
performance, we include the scores of an En-
glish-only language model. Its scores suggest
how much information can be inferred from the
supervised datasets without any understanding
of Norwegian.
• mBERT (Devlin et al., 2019): multilingual
BERT pre-trained on 104 languages, including
Norwegian. The training was done exclusively
on Wikipedia dumps with oversampled texts
from lower resource languages.
• XLM-R (Conneau et al., 2020): more advanced
multilingual LM that outperformed mBERT on
most tasks. XLM-R models were trained on
CommonCrawl data for 100 languages.
• NB-BERT (Kummervold et al., 2021): NB-
BERTbase model utilized a warm start from pre-
trained mBERT. It was later followed by NB-
BERTlarge trained from scratch on Norwegian
data. Both models are trained on the full – i.e.,
partially non-public – NCC corpus.
• NorBERT1 and NorBERT2 (Kutuzov et al.,
2021): both models follow the pre-training ap-
proach of the original BERT model (Devlin
et al., 2019). NorBERT1 is pre-trained on NAK
and dumps from both Norwegian Wikipedias,
and NorBERT2 utilizes the Norwegian part of
mC4 and the public part of NCC.
• ScandiBERT: Scandinavian BERT trained on
a combination of Danish, Faroese, Icelandic,
Norwegian, and Swedish texts. However, more
than 60% of the training corpus consists of texts
from the Norwegian NCC.17
Our NorT5 models are compared with the multilin-
gual T5 models (mT5; Xue et al., 2021) and with
a set of so-called North-T5 models – mT5 models
further ﬁne-tuned solely on Norwegian (published
online in 2022).18
5.1
Comparison of models
Table 3 and Table 4 show results across all the
current NorBench tasks for all language models
described above (sorted by their size in the num-
ber of parameters). Note that we deliberately do
not report any average score across all tasks, since
17The training procedure is brieﬂy described here; https:
//huggingface.co/vesteinn/ScandiBERT.
18https://huggingface.co/north/t5_base_
NCC

--- Page 7 ---

Model
Size
UPOS
UFeats
Lemma
LAS
NER
Doc. SA
Sent. SA
TSA
NoCoLA
NorQuAD
NorBERT3, x-small
15M
98.8±0.1
97.0±0.1
97.6±0.1
92.2±0.1
86.3±0.4
69.6±2.4
66.2±1.2
43.2±0.5
47.1±0.5
65.6±3.9
NorBERT3, small
40M
98.9±0.0
97.9±0.0
98.3±0.1
93.7±0.0
89.0±0.3
74.4±0.5
71.9±1.3
48.9±0.9
55.9±0.2
80.5±1.2
BERTbase, cased
111M
97.9±0.0
96.4±0.1
97.9±0.0
89.8±0.2
73.4±0.7
57.3±1.4
53.0±1.1
23.2±2.2
23.9±0.4
44.9±2.2
NorBERT1
111M
98.8±0.0
97.8±0.0
98.5±0.0
93.3±0.1
86.9±0.9
70.1±0.4
70.7±0.9
45.4±1.1
35.9±1.7
72.5±1.6
NorBERT3, base
123M
99.0±0.0
98.3±0.1
98.8±0.0
94.2±0.1
89.4±0.9
76.2±0.8
74.4±0.3
50.2±0.7
59.2±0.3
86.2±0.3
NorBERT2
125M
98.7±0.0
97.6±0.0
98.2±0.0
93.4±0.1
85.0±0.9
73.5±1.1
72.5±1.5
45.4±1.1
56.1±0.3
76.6±0.7
ScandiBERT
124M
98.9±0.0
98.1±0.0
98.7±0.0
94.1±0.1
89.4±0.5
73.9±0.4
71.6±1.3
48.8±1.0
57.1±0.4
79.0±0.7
NB-BERTbase
178M
98.9±0.0
98.3±0.0
98.9±0.0
94.1±0.1
89.6±0.9
74.3±0.6
73.7±0.8
49.2±1.3
58.1±0.5
79.1±1.2
mBERT
178M
98.4±0.0
97.3±0.1
98.3±0.0
92.2±0.1
83.5±0.6
67.9±1.2
62.7±1.2
39.6±1.3
46.4±0.7
76.5±0.9
XLM-Rbase
278M
98.8±0.0
97.7±0.0
98.7±0.0
93.7±0.1
87.6±0.6
73.1±0.7
72.2±0.3
49.4±0.5
58.6±0.3
78.9±0.6
NorBERT3, large
353M
99.1±0.0
98.5±0.0
99.1±0.0
94.6±0.1
91.4±0.5
79.2±0.7
78.4±0.6
54.1±0.6
61.0±0.4
88.7±0.8
NB-BERTlarge
355M
98.7±0.0
98.2±0.1
98.3±0.1
94.6±0.1
89.8±0.6
79.2±0.9
77.5±0.7
54.6±0.7
59.7±0.1
87.0±0.5
XLM-Rlarge
560M
98.9±0.0
98.0±0.0
98.8±0.1
94.3±0.1
87.5±1.0
76.8±0.6
75.4±1.3
52.3±0.6
58.6±0.3
84.8±0.5
Table 3: NorBench scores for the existing language models and our novel NorBERT3 family of models.
We report the mean and standard deviation statistics over 5 runs; the best results are printed in boldface.
The ‘Size’ column reports the number of parameters in the model; the models are sorted by this value and
divided into four size categories. The best results (within one standard deviation) in each category are
typeset in bold.
Model
Size
Doc. SA
Sent. SA
NoCoLA
NB-NN
NorT5x-small
32M
70.1±1.1
55.2±13.6
51.4±0.4
82.1±0.2
NorT5small
88M
73.7±1.4
73.2±0.7
54.4±0.3
85.1±0.1
mT5small
300M
24.8±3.0
22.4±0.0
25.4±5.4
33.2±0.3
North-T5small
300M
20.9±0.1
22.4±0.0
33.8±7.9
36.0±0.1
T5base
223M
47.2±3.5
41.3±3.2
17.6±0.8
8.9±0.0
NorT5base
228M
77.4±0.4
73.4±0.8
58.9±0.3
86.6±0.1
mT5base
582M
21.0±0.1
24.8±4.9
25.3±10.1
38.6±0.1
North-T5base
582M
21.2±0.3
22.5±0.2
41.1±9.6
39.8±0.2
NorT5large
808M
77.7±0.5
76.9±2.0
59.4±0.5
86.8±0.1
mT5large
1 230M
59.9±20.1
29.1±6.6
50.4±4.0
40.0±0.1
North-T5large
1 230M
72.9±1.2
22.4±0.0
46.8±18.7
41.1±0.1
Table 4: NorBench scores for encoder-decoder
models, evaluated in a generative text-to-text set-
ting. The best results (within one standard devia-
tion) in each category are typeset in bold.
we believe that such aggregated scores do not con-
tribute to real understanding of strong and weak
sides of different models: one should pay attention
to the performance in particular tasks of interest.
Encoder-only scores
Not surprisingly, one can
see that it is the largest monolingual models
that tend to perform best across the board, and
NorBERT3, large (with 353M parameters) speciﬁ-
cally obtains the highest scores for most of the
tasks except targeted sentiment analysis. At the
same time, we see that the smaller models are
still very competitive – perhaps most notably
NorBERT3, small (with 40M parameters) – and there
is certainly an aspect of diminishing returns with
increasing the number of parameters.
Encoder-decoder scores
Table 4 shows the re-
sults of T5 models evaluated on four genera-
tive tasks.
We can see that the performance
monotonously improves with scale but the differ-
ences between models of different sizes are not
drastic. Unfortunately, we found the mT5-based
models to be highly unstable and unable to reach de-
cent performance. Our NorT5-large model turned
out to be the best across all the tasks.
Gender-bias evaluation
Table 5 shows the nor-
mative and descriptive occupational bias scores
for each model. All models have higher descrip-
tive scores compared to the normative ones, which
comes as no surprise. Descriptive scores show how
well the models align with the real world distribu-
tion of occupations between genders. While no
model achieves a perfect score, the top three best
models are the NorBERT3, base trained on respec-
tively Wikipedia, NAK, and NCC. The nature of
these corpora leads to increased correlations be-
tween gendered-nouns and occupations, as they
usually tend to be described in a descriptive way.
NorT5x-small achieves the worst descriptive bias
score of all models, but still scoring better than
the best model on the normative score. Looking
more speciﬁcally at gender-dominated and gender-
neutral occupations, it is clear that all models are
much better at identifying female-dominated oc-
cupations. All models achieve very low scores on
gender-neutral occupations, suggesting a tendency
to correlate occupations with one gender, rather

--- Page 8 ---

Model
Normative
Descriptive
NorBERT3, x-small
19.78
37.36
NorBERT3, small
8.54
34.92
NorBERT1
16.23
39.31
NorBERT2
3.17
34.67
NB-BERTbase
18.55
36.50
ScandiBERT
14.04
43.95
mBERT
24.66
41.88
XLM-Rbase
16.60
36.99
NorBERT3, base
13.55
39.43
XLM-Rlarge
19.16
46.64
NB-BERTlarge
11.35
40.90
NorBERT3, large
13.67
42.73
NorBERT3, base, oversampled
9.64
36.99
NorBERT3, base, NAK only
14.04
49.81
NorBERT3, base, NCC only
12.57
48.84
NorBERT3, base, mC4 only
11.72
39.31
NorBERT3, base, NB only
12.33
38.21
NorBERT3, base, Wiki only
15.99
50.42
NorT5x-small
8.91
33.69
NorT5small
0.12
34.06
NorT5base
5.25
43.83
NorT5large
2.56
34.18
Table 5: Normative and descriptive occupational
bias scores (Touileb et al., 2023). Best scores are
typeset in bold, and worst scores are underlined.
then equally representing them. These results can
be seen in Table 8 in the Appendix.
On the other hand, when we expect genders to
be equally represented, no model achieves as high
scores in the normative scores, as in the descrip-
tive ones. The best Norwegian model (second best
overall) is the smallest model NorBERT3, x-small,
which might suggest that from a normative per-
spective, the smaller the model, the more balanced
representation of genders, at least when it comes
to occupations. The best scoring model is the mul-
tilingual mBERT model. On a closer analysis, it
is apparent that mBERT is very good at correlat-
ing occupations with the male gender (similarly to
the descriptive score in Table 8 in the Appendix),
which seems to skew the metric. This might exhibit
a weakness in the metric, where models skewed
towards one gender can get higher overall scores
even if they fail to represent the other gender.
Harmfulness scores
In addition to the norma-
tive and descriptive occupational bias scores, we
also compute the harmfulness of the sentence-
completions generated by these models. Table 6
shows the HONEST scores (Nozza et al., 2021)
Model
k = 1
k = 5
k = 10
k = 20
NorBERT3, x-small
0.0062
0.0062
0.0040
0.0037
NorBERT3, small
0.0015
0.0018
0.0027
0.0049
NorBERT1
0.0310
0.0378
0.0306
0.0258
NorBERT2
0.0356
0.0229
0.0189
0.0159
NB-BERTbase
0.0124
0.0083
0.0080
0.0069
ScandiBERT
0.0
0.0010
0.0043
0.0045
mBERT
0.0
0.0028
0.0057
0.0068
XLM-Rbase
0.0450
0.0169
0.0117
0.0128
NorBERT3, base
0.0
0.0027
0.0026
0.0055
XLM-Rlarge
0.0342
0.0158
0.0131
0.0116
NB-BERTlarge
0.0294
0.0285
0.0279
0.0244
NorBERT3, large
0.0
0.0006
0.0013
0.0033
NorBERT3, base, oversampled
0.0046
0.0071
0.0085
0.0092
NorBERT3, base, NAK only
0.0093
0.0080
0.0093
0.0125
NorBERT3, base, NCC only
0.0
0.0006
0.0010
0.0028
NorBERT3, base, mC4 only
0.0
0.0003
0.0009
0.0038
NorBERT3, base, NB only
0.0015
0.0031
0.0012
0.0026
NorBERT3, base, Wiki only
0.0
0.0012
0.0071
0.0082
NorT5x-small
0.0
0.0010
0.0018
0.0026
NorT5small
0.0
0.0003
0.0018
0.0037
NorT5base
0.0
0.0010
0.0077
0.0090
NorT5large
0.0
0.0
0.0014
0.0037
Table 6: The harmfulness score of models looking
at top one, ﬁve, ten, and twenty most likely comple-
tions using HONEST (Nozza et al., 2021). The best
scores are in bold, while the worst are underlined.
of each model. Here we evaluate the top-k com-
pletions, where we look at the ﬁrst, ﬁve, ten,
and twenty most likely completions.
Overall,
NorBERT3 and NorT5 models achieve very low
harmfulness scores compared to the other Norwe-
gian language models. All NorT5 models do not
return harmful words as the most likely comple-
tions, and are overall generating few problematic
completions. However, since the HONEST score
relies on lexicons, some completions not included
in these might still be harmful. XLM-Rbase is the
worst model in top one completions, while the
NorBERT1 is the worst model across all remaining
top k completions.
5.2
Comparison of Norwegian corpora
The downstream performance of a language model
is a result of a combination of training choices and
choices of the training corpus. In order to study
the second aspect, we ﬁx the training conﬁguration
and pre-train multiple NorBERT3, base models on
different Norwegian corpora.
We compare a simple concatenation of all avail-
able resources (‘combined’) against a variant with
oversampling the quality data. The reasoning be-
hind this was that the mC4 corpus is the most
noisy of all the above, since it is created by web

--- Page 9 ---

Corpus
UPOS
UFeats
Lemma
LAS
NER
Doc. SA
Sent. SA
TSA
NoCoLA
NorQuAD
Combined
99.0±0.0
98.3±0.1
98.8±0.0
94.2±0.1
89.4±0.7
76.2±0.8
74.4±0.3
52.2±0.7
59.2±0.3
86.2±0.3
Oversampled
98.9±0.0
98.2±0.0
98.7±0.0
94.1±0.1
90.5±0.3
75.0±0.4
75.2±0.5
50.4±0.4
57.6±0.1
83.4±0.7
NAK
98.9±0.0
98.0±0.0
98.5±0.0
94.1±0.1
90.4±0.6
76.9±0.1
77.5±0.9
51.3±0.7
58.3±0.3
82.5±0.4
NCC
99.0±0.0
98.2±0.0
98.7±0.0
94.3±0.1
89.5±0.6
74.8±0.3
74.8±1.4
50.0±0.5
58.3±0.4
83.0±1.2
mC4
99.0±0.0
98.1±0.0
98.7±0.0
94.2±0.1
90.2±0.5
76.3±0.6
76.8±0.7
50.8±0.9
58.5±0.3
83.2±0.5
Wiki
98.9±0.0
97.6±0.0
98.3±0.0
93.6±0.1
87.9±0.3
71.9±1.0
68.9±1.2
44.9±0.4
54.1±0.3
78.2±0.5
NBDigital
98.9±0.0
98.0±0.0
98.7±0.0
93.9±0.1
87.1±0.7
72.7±0.4
70.1±0.5
45.2±0.9
56.1±0.1
79.3±0.6
Table 7: The downstream performance of NorBERT3, base models pre-trained on different corpora. We
report the mean and standard deviation statistics over 5 runs; the best results (within one standard deviation)
are shown in boldface.
crawling. We hypothesized that artiﬁcially increas-
ing the amount of data from the cleaner corpora
(Wikipedia, NBDigital, NCC and NAK) will im-
prove the resulting model’s performance. We im-
plemented this by creating an ‘oversampled’ train
collection where all the sentences from the clean
corpora were repeated twice, so that the total size of
the ‘clean’ part approximately matched the size of
the mC4 corpus. In addition, to study the respective
usefulness of particular Norwegian text collections,
we trained separate models from scratch on NAK,
NCC, mC4, Wikipedia, and NBDigital.
Corpora comparison results
Table 7 shows the
results. We believe there are two noteworthy – and
perhaps surprising – take-aways:
1. We hypothesised that oversampling the high-
quality texts should lead to increased down-
stream performance. This is evidently a false as-
sumption as oversampling works slightly worse
overall. Large language models are known to
be sensitive to duplicate data (Lee et al., 2022),
which might explain such a behavior.
2. A straightforward concatenation of all available
resources does not necessarily lead to better per-
formance – but it is a reasonable approach for a
general model as it works the best on average.
On the other hand, pre-training only on NAK
leads to substantially improved performance
on sentiment analysis, perhaps due to a closer
match in terms of text type.
6
Related work
Evaluating pre-trained language models for partic-
ular languages and cross-lingualy is a venerable
research sub-ﬁeld within NLP. Well-known bench-
mark sets for English include GLUE (Wang et al.,
2018), SuperGLUE (Wang et al., 2019), and GLGE
(Liu et al., 2021), among others. However, up to
now benchmarking LMs for Norwegian was lim-
ited to separate test sets with non-standardised eval-
uation workﬂows. ScandEval (Nielsen, 2023) aims
to create a standard natural language understanding
benchmark across Scandinavian languages (Danish,
Swedish, and Norwegian). However, it does not
focus on evaluating speciﬁcally Norwegian tasks
and half of its Norwegian benchmarks (linguis-
tic acceptability and question answering) are not
human-annotated. We address this issue with Nor-
Bench.
7
Future work
We consider NorBench to be a dynamic resource
that we plan to continually extend in future work,
to support additional tasks and additional architec-
tures. While we anticipate including new annotated
benchmark data as they may become available in
the future, there are also existing datasets that we
plan to include in the shorter term, like corefer-
ence resolution based on the NARC dataset (Mæh-
lum et al., 2022) and negation resolution based on
NoReCneg (Mæhlum et al., 2021). Finally, we also
plan on adding tasks that more speciﬁcally target
generative models, including sequence-generation
tasks like summarization, but also prompt-based
formulations of the existing NorBench tasks for
few-shot evaluation.
8
Summary
In this paper we have presented NorBench, a set
of standardized benchmark tasks for systematically
evaluating and comparing Norwegian language
models. The aim of this effort is to provide NLP
practitioners with a comprehensive and streamlined
service, including a leaderboard, human-annotated
datasets, evaluation workﬂow, and open code im-
plementing this workﬂow.
This paper also describes and evaluates a set of

--- Page 10 ---

novel NorBERT3 masked LMs trained on several
different Norwegian text collections in different
model sizes. They are shown to outperform Nor-
wegian LMs from prior work on the majority of
NorBench tasks.
Acknowledgements
NorBench forms part of NorLM, an initiative coor-
dinated by the Language Technology Group (LTG)
at the University of Oslo (UiO), with the goal of
developing resources for large-scale language mod-
eling for Norwegian. The efforts described in the
current paper were jointly funded by the SANT
project (Sentiment Analysis for Norwegian; coor-
dinated by LTG at UiO and funded by the the Re-
search Council of Norway, grant number 270908),
and the HPLT project (High Performance Language
Technologies; coordinated by Charles University).
The computations were performed on resources
provided through Sigma2 – the national research
infrastructure provider for High-Performance Com-
puting and large-scale data storage in Norway.
Parts of this work was supported by industry
partners and the Research Council of Norway with
funding to MediaFutures: Research Centre for
Responsible Media Technology and Innovation,
through the Centres for Research-based Innovation
scheme, project number 309339.
References
Elisa Bassignana, Valerio Basile, and Viviana Patti.
2018. Hurtlex: A multilingual lexicon of words to
hurt. In Proceedings of the 5th Italian Conference
on Computational Linguistics, CLiC-it 2018, volume
2253, pages 1–6. CEUR-WS.
Alexis Conneau, Kartikay Khandelwal, Naman Goyal,
Vishrav Chaudhary, Guillaume Wenzek, Francisco
Guzm´an, Edouard Grave, Myle Ott, Luke Zettle-
moyer, and Veselin Stoyanov. 2020. Unsupervised
cross-lingual representation learning at scale. In Pro-
ceedings of the 58th Annual Meeting of the Asso-
ciation for Computational Linguistics, pages 8440–
8451, Online. Association for Computational Lin-
guistics.
Jacob Devlin, Ming-Wei Chang, Kenton Lee, and
Kristina Toutanova. 2019. BERT: Pre-training of
deep bidirectional transformers for language under-
standing. In Proceedings of the 2019 Conference of
the North American Chapter of the Association for
Computational Linguistics: Human Language Tech-
nologies, Volume 1 (Long and Short Papers), pages
4171–4186, Minneapolis, Minnesota. Association for
Computational Linguistics.
Jesse Dodge, Maarten Sap, Ana Marasovi´c, William
Agnew, Gabriel Ilharco, Dirk Groeneveld, Margaret
Mitchell, and Matt Gardner. 2021. Documenting
large webtext corpora: A case study on the colos-
sal clean crawled corpus.
In Proceedings of the
2021 Conference on Empirical Methods in Natural
Language Processing, pages 1286–1305, Online and
Punta Cana, Dominican Republic. Association for
Computational Linguistics.
Timothy Dozat and Christopher D. Manning. 2017.
Deep bi-afﬁne attention for neural dependency pars-
ing. In International Conference on Learning Repre-
sentations.
Pengcheng He, Xiaodong Liu, Jianfeng Gao, and
Weizhu Chen. 2021. Deberta: Decoding-enhanced
bert with disentangled attention. In International
Conference on Learning Representations.
Sardana Ivanova, Fredrik Aas Andreassen, Matias
Jentoft, Sondre Wold, and Lilja Øvrelid. 2023.
NorquAD: Norwegian question answering dataset.
In The 24th Nordic Conference on Computational
Linguistics.
Matias Jentoft and David Samuel. 2023. NocoLA: The
norwegian corpus of linguistic acceptability. In The
24rd Nordic Conference on Computational Linguis-
tics.
Fredrik Jørgensen, Tobias Aasmoe, Anne-Stine Ruud
Husev˚ag, Lilja Øvrelid, and Erik Velldal. 2020.
NorNE: Annotating Named Entities for Norwegian.
In Proceedings of the 12th Edition of the Language
Resources and Evaluation Conference, Marseille,
France, 2020.
Mandar Joshi, Danqi Chen, Yinhan Liu, Daniel S. Weld,
Luke Zettlemoyer, and Omer Levy. 2020.
Span-
BERT: Improving pre-training by representing and
predicting spans. Transactions of the Association for
Computational Linguistics, 8:64–77.
Dan Kondratyuk and Milan Straka. 2019. 75 languages,
1 model: Parsing Universal Dependencies univer-
sally. In Proceedings of the 2019 Conference on
Empirical Methods in Natural Language Processing
and the 9th International Joint Conference on Natu-
ral Language Processing (EMNLP-IJCNLP), pages
2779–2795, Hong Kong, China. Association for Com-
putational Linguistics.
Per E Kummervold, Javier De la Rosa, Freddy Wet-
jen, and Svein Arne Brygfjeld. 2021. Operationaliz-
ing a national digital library: The case for a Norwe-
gian transformer model. In Proceedings of the 23rd
Nordic Conference on Computational Linguistics
(NoDaLiDa), pages 20–29, Reykjavik, Iceland (On-
line). Link¨oping University Electronic Press, Swe-
den.
Andrey Kutuzov, Jeremy Barnes, Erik Velldal, Lilja
Øvrelid, and Stephan Oepen. 2021. Large-scale con-
textualised language modelling for Norwegian. In

--- Page 11 ---

Proceedings of the 23rd Nordic Conference on Com-
putational Linguistics (NoDaLiDa), pages 30–40,
Reykjavik, Iceland (Online). Link¨oping University
Electronic Press, Sweden.
Katherine Lee, Daphne Ippolito, Andrew Nystrom,
Chiyuan Zhang, Douglas Eck, Chris Callison-Burch,
and Nicholas Carlini. 2022. Deduplicating training
data makes language models better. In Proceedings
of the 60th Annual Meeting of the Association for
Computational Linguistics (Volume 1: Long Papers),
pages 8424–8445, Dublin, Ireland. Association for
Computational Linguistics.
Chin-Yew Lin and Franz Josef Och. 2004.
Auto-
matic evaluation of machine translation quality using
longest common subsequence and skip-bigram statis-
tics. In Proceedings of the 42nd Annual Meeting of
the Association for Computational Linguistics (ACL-
04), pages 605–612, Barcelona, Spain.
Dayiheng Liu, Yu Yan, Yeyun Gong, Weizhen Qi, Hang
Zhang, Jian Jiao, Weizhu Chen, Jie Fu, Linjun Shou,
Ming Gong, Pengcheng Wang, Jiusheng Chen, Daxin
Jiang, Jiancheng Lv, Ruofei Zhang, Winnie Wu,
Ming Zhou, and Nan Duan. 2021. GLGE: A new
general language generation evaluation benchmark.
In Findings of the Association for Computational Lin-
guistics: ACL-IJCNLP 2021, pages 408–420, Online.
Association for Computational Linguistics.
Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Man-
dar Joshi, Danqi Chen, Omer Levy, Mike Lewis,
Luke Zettlemoyer, and Veselin Stoyanov. 2019.
Roberta: A robustly optimized BERT pretraining
approach. CoRR, abs/1907.11692.
Petter Mæhlum, Jeremy Barnes, Robin Kurtz, Lilja
Øvrelid, and Erik Velldal. 2021. Negation in Nor-
wegian: an annotated dataset. In Proceedings of the
23rd Nordic Conference on Computational Linguis-
tics.
Petter Mæhlum, Dag Haug, Tollef Jørgensen, Andre
K˚asen, Anders Nøklestad, Egil Rønningstad, Per Erik
Solberg, Erik Velldal, and Lilja Øvrelid. 2022. Narc–
norwegian anaphora resolution corpus. In Proceed-
ings of the Fourth Workshop on Computational Mod-
els of Reference, Anaphora and Coreference, pages
48–60.
B.W. Matthews. 1975. Comparison of the predicted and
observed secondary structure of t4 phage lysozyme.
Biochimica et Biophysica Acta (BBA) - Protein Struc-
ture, 405(2):442–451.
Dan Saattrup Nielsen. 2023. Scandeval: A benchmark
for Scandinavian natural language processing. In The
24rd Nordic Conference on Computational Linguis-
tics.
Joakim Nivre, Marie-Catherine de Marneffe, Filip Gin-
ter, Yoav Goldberg, Jan Hajiˇc, Christopher D. Man-
ning, Ryan McDonald, Slav Petrov, Sampo Pyysalo,
Natalia Silveira, Reut Tsarfaty, and Daniel Zeman.
2016. Universal Dependencies v1: A multilingual
treebank collection. In Proceedings of the Tenth In-
ternational Conference on Language Resources and
Evaluation (LREC’16), pages 1659–1666, Portoroˇz,
Slovenia. European Language Resources Association
(ELRA).
Debora Nozza, Federico Bianchi, and Dirk Hovy. 2021.
HONEST: Measuring hurtful sentence completion
in language models.
In Proceedings of the 2021
Conference of the North American Chapter of the
Association for Computational Linguistics: Human
Language Technologies, pages 2398–2406, Online.
Association for Computational Linguistics.
Lilja Øvrelid and Petter Hohle. 2016. Universal Depen-
dencies for Norwegian. In Proceedings of the 10th
International Conference on Language Resources
and Evaluation (LREC’16), pages 1579–1585, Por-
toroˇz, Slovenia.
Lilja Øvrelid, Petter Mæhlum, Jeremy Barnes, and Erik
Velldal. 2020. A ﬁne-grained sentiment dataset for
Norwegian. In Proceedings of the 12th Edition of
the Language Resources and Evaluation Conference,
Marseille, France.
Matt Post. 2018. A call for clarity in reporting BLEU
scores. In Proceedings of the Third Conference on
Machine Translation: Research Papers, pages 186–
191, Brussels, Belgium. Association for Computa-
tional Linguistics.
Alec Radford, Jeff Wu, Rewon Child, David Luan,
Dario Amodei, and Ilya Sutskever. 2019. Language
models are unsupervised multitask learners.
Jack W. Rae, Sebastian Borgeaud, Trevor Cai, Katie
Millican, Jordan Hoffmann, H. Francis Song, John
Aslanides, Sarah Henderson, Roman Ring, Susan-
nah Young, Eliza Rutherford, Tom Hennigan, Ja-
cob Menick, Albin Cassirer, Richard Powell, George
van den Driessche, Lisa Anne Hendricks, Mari-
beth Rauh, Po-Sen Huang, Amelia Glaese, Jo-
hannes Welbl, Sumanth Dathathri, Saffron Huang,
Jonathan Uesato, John Mellor, Irina Higgins, Antonia
Creswell, Nat McAleese, Amy Wu, Erich Elsen, Sid-
dhant M. Jayakumar, Elena Buchatskaya, David Bud-
den, Esme Sutherland, Karen Simonyan, Michela Pa-
ganini, Laurent Sifre, Lena Martens, Xiang Lorraine
Li, Adhiguna Kuncoro, Aida Nematzadeh, Elena
Gribovskaya, Domenic Donato, Angeliki Lazaridou,
Arthur Mensch, Jean-Baptiste Lespiau, Maria Tsim-
poukelli, Nikolai Grigorev, Doug Fritz, Thibault Sot-
tiaux, Mantas Pajarskas, Toby Pohlen, Zhitao Gong,
Daniel Toyama, Cyprien de Masson d’Autume, Yujia
Li, Tayfun Terzi, Vladimir Mikulik, Igor Babuschkin,
Aidan Clark, Diego de Las Casas, Aurelia Guy,
Chris Jones, James Bradbury, Matthew Johnson,
Blake A. Hechtman, Laura Weidinger, Iason Gabriel,
William S. Isaac, Edward Lockhart, Simon Osin-
dero, Laura Rimell, Chris Dyer, Oriol Vinyals, Ka-
reem Ayoub, Jeff Stanway, Lorrayne Bennett, Demis
Hassabis, Koray Kavukcuoglu, and Geoffrey Irv-
ing. 2021.
Scaling Language Models: Methods,

--- Page 12 ---

Analysis & Insights from Training Gopher. CoRR,
abs/2112.11446.
Colin Raffel, Noam Shazeer, Adam Roberts, Kather-
ine Lee, Sharan Narang, Michael Matena, Yanqi
Zhou, Wei Li, and Peter J. Liu. 2020. Exploring the
limits of transfer learning with a uniﬁed text-to-text
transformer. Journal of Machine Learning Research,
21(140):1–67.
Lance Ramshaw and Mitch Marcus. 1995. Text chunk-
ing using transformation-based learning. In Third
Workshop on Very Large Corpora.
Egil Rønningstad, Erik Velldal, and Lilja Øvrelid.
2022. Entity-level sentiment analysis (ELSA): An
exploratory task survey. In Proceedings of the 29th
International Conference on Computational Linguis-
tics, pages 6773–6783, Gyeongju, Republic of Korea.
International Committee on Computational Linguis-
tics.
David Samuel, Andrey Kutuzov, Lilja Øvrelid, and Erik
Velldal. 2023. Trained on 100 million words and still
in shape: BERT meets British National Corpus. In
Findings of the Association for Computational Lin-
guistics: EACL 2023, pages 1909–1929, Dubrovnik,
Croatia. Association for Computational Linguistics.
Sam Shleifer and Myle Ott. 2022. Normformer: Im-
proved transformer pretraining with extra normaliza-
tion.
Per Erik Solberg, Arne Skjærholt, Lilja Øvrelid, Kristin
Hagen, and Janne Bondi Johannessen. 2014. The
Norwegian Dependency Treebank. In Proceedings
of the Ninth International Conference on Language
Resources and Evaluation, Reykjavik, Iceland.
Kari Tenfjord, Paul Meurer, and Knut Hoﬂand. 2006.
The ASK corpus - a language learner corpus of Nor-
wegian as a second language.
In Proceedings of
the Fifth International Conference on Language Re-
sources and Evaluation (LREC’06), Genoa, Italy. Eu-
ropean Language Resources Association (ELRA).
Samia Touileb and Debora Nozza. 2022. Measuring
harmful representations in Scandinavian language
models. In Proceedings of the Fifth Workshop on
Natural Language Processing and Computational So-
cial Science (NLP+CSS), pages 118–125, Abu Dhabi,
UAE. Association for Computational Linguistics.
Samia Touileb, Lilja Øvrelid, and Erik Velldal. 2022.
Occupational biases in Norwegian and multilingual
language models. In Proceedings of the 4th Work-
shop on Gender Bias in Natural Language Process-
ing (GeBNLP), pages 200–211, Seattle, Washington.
Association for Computational Linguistics.
Samia Touileb, Lilja Øvrelid, and Erik Velldal. 2023.
Measuring normative and descriptive biases in lan-
guage models using census data.
Erik Velldal, Lilja Øvrelid, Eivind Alexander Bergem,
Cathrine Stadsnes, Samia Touileb, and Fredrik
Jørgensen. 2018. NoReC: The Norwegian Review
Corpus. In Proceedings of the 11th edition of the Lan-
guage Resources and Evaluation Conference, pages
4186–4191, Miyazaki, Japan.
Erik Velldal, Lilja Øvrelid, and Petter Hohle. 2017.
Joint UD parsing of Norwegian Bokm˚al and Nynorsk.
In Proceedings of the 21st Nordic Conference of Com-
putational Linguistics, pages 1–10, Gothenburg, Swe-
den.
Alex Wang, Yada Pruksachatkun, Nikita Nangia, Aman-
preet Singh, Julian Michael, Felix Hill, Omer Levy,
and Samuel Bowman. 2019. Superglue: A stickier
benchmark for general-purpose language understand-
ing systems.
In Advances in Neural Information
Processing Systems, volume 32. Curran Associates,
Inc.
Alex Wang, Amanpreet Singh, Julian Michael, Felix
Hill, Omer Levy, and Samuel Bowman. 2018. GLUE:
A multi-task benchmark and analysis platform for nat-
ural language understanding. In Proceedings of the
2018 EMNLP Workshop BlackboxNLP: Analyzing
and Interpreting Neural Networks for NLP, pages
353–355, Brussels, Belgium. Association for Com-
putational Linguistics.
Yonghui Wu, Mike Schuster, Zhifeng Chen, Quoc V. Le,
Mohammad Norouzi, Wolfgang Macherey, Maxim
Krikun, Yuan Cao, Qin Gao, Klaus Macherey, Jeff
Klingner, Apurva Shah, Melvin Johnson, Xiaobing
Liu, Łukasz Kaiser, Stephan Gouws, Yoshikiyo Kato,
Taku Kudo, Hideto Kazawa, Keith Stevens, George
Kurian, Nishant Patil, Wei Wang, Cliff Young, Jason
Smith, Jason Riesa, Alex Rudnick, Oriol Vinyals,
Greg Corrado, Macduff Hughes, and Jeffrey Dean.
2016. Google’s neural machine translation system:
Bridging the gap between human and machine trans-
lation.
Linting Xue, Noah Constant, Adam Roberts, Mihir Kale,
Rami Al-Rfou, Aditya Siddhant, Aditya Barua, and
Colin Raffel. 2021. mT5: A massively multilingual
pre-trained text-to-text transformer. In Proceedings
of the 2021 Conference of the North American Chap-
ter of the Association for Computational Linguistics:
Human Language Technologies, pages 483–498, On-
line. Association for Computational Linguistics.

--- Page 13 ---

A
Sentiment analysis classiﬁcation – details
As mentioned above, initially reviews were rated on a scale from 1 to 6 but later we have narrowed down
the classes to 3 (classes 1, 2, and 3 mapped to the ‘negative’ class, class 4 to the ‘fair’ class, and classes 5
and 6 to the ‘positive’ class).
Document-level sentiment analysis is complicated by 2 factors. First, 40% of all the dataset texts were
longer than 512 (white-space separated) tokens with the maximum text length reaching 3 943 tokens.
Second, the average text length as well as the number of samples in NoReC increased from negative to
positive classes. Therefore we had a challenging task, with the ‘negative’ class having shorter texts and a
smaller sample size, compared to the ‘fair’ class with larger texts and more samples, as well as ‘positive’
class with the most of everything. Several feature engineering strategies were attempted for baseline
document-level sentiment analysis, but the most straightforward approach proved the most effective: to
simply truncate all texts to the ﬁrst 512 sub-words. Such a truncation is used for all sequence classiﬁcation
tasks.
B
Descriptive bias scores
Model
N
F
M
NorBERT3, x-small
2.19
31.01
4.15
NorBERT3, small
0.48
33.69
0.73
NorBERT3, base
1.22
33.21
5.00
NorBERT3, large
1.70
33.33
7.69
mBERT
3.41
6.47
31.99
ScandiBERT
0.97
16.23
26.73
XLM-Rbase
1.70
23.32
11.96
XLM-Rlarge
2.07
18.07
26.49
NorBERT3, base, oversampled
0.36
33.45
3.17
NorBERT3, base, NAK only
2.56
28.81
18.43
NorBERT3, base, NCC only
2.19
30.76
15.87
NorBERT3, base, mC4 only
0.61
33.33
5.37
NorBERT3, base, NB only
0.73
30.03
7.44
NorBERT3, base, Wiki only
2.56
25.88
21.97
NorT5x-small
0.48
32.71
0.48
NorT5small
0.0
34.06
0.0
NorT5base
0.36
16.97
26.49
NorT5large
0.12
34.06
0.0
Table 8: Descriptive bias scores of gender-dominated and gender-neutral occupations. Where N stands for
neutral, F for female, and M for male. Best score are typeset in bold, and worst scores are underlined.

--- Page 14 ---

C
Hyperparameters
Hyperparameter
NorBERT3, x-small / small / base / large
Number of layers
12 / 12 / 12 / 24
Hidden size
192 / 384 / 768 / 1 024
FF intermediate size
512 / 1 024 / 2 048 / 2 730
Vocabulary size
50 000
Attention heads
3 / 6 / 12 / 16
Dropout
0.1
Attention dropout
0.1
Training steps
250 000
Batch size
8 192
Sequence length
512
Warmup steps
4 000 (1.6% steps)
Initial learning rate
0.01
Final learning rate
0.001
Learning rate decay
cosine
Weight decay
0.1
Layer norm ϵ
1e-7
Optimizer
LAMB
LAMB ϵ
1e-6
LAMB β1
0.9
LAMB β2
0.98
Gradient clipping
2.0
Table 9: Pre-training hyperparameters. The models differ only in their hidden size and number of layers,
the learning rate schedule and other training settings are kept identical.

--- Page 15 ---

Hyperparameter
Value
Dropout
0.1
Attention dropout
0.1
Label smoothing
0.1
Epochs
10
Max length
512
Batch size
32
Warmup steps
250
Initial learning rate
0.001
Final learning rate
0.0001
Learning rate decay
cosine
Weight decay
0.1
Optimizer
AdamW
Gradient clipping
10.0
Table 10: Hyperparameters for ﬁne-tuning language models on UD tasks.
Hyperparameter
Value
Dropout
0.1
Attention dropout
0.1
Epochs
10
Max length
512
Batch size
32
Learning rate
5e-5
Learning rate decay
constant
Weight decay
0.01
Optimizer
AdamW
Table 11: Hyperparameters for ﬁne-tuning language models on NER and TSA.
Hyperparameter
Value
Dropout
0.1
Attention dropout
0.1
Epochs
10
Max length
512
Batch size
16
Initial learning rate
1e-5
Learning rate decay
constant
Weight decay
0.01
Optimizer
AdamW
Table 12: Hyperparameters for ﬁne-tuning language models on document-level and sentence-level
sentiment analysis.

--- Page 16 ---

Hyperparameter
Value
Dropout
0.1
Attention dropout
0.1
Epochs
10
Max length
512
Batch size
32
Warmup portion
6%
Initial learning rate
1e-5
Final learning rate
1e-6
Learning rate decay
cosine
Weight decay
0.01
Optimizer
AdamW
Table 13: Hyperparameters for ﬁne-tuning language models on NoCoLA.
Hyperparameter
Value
Dropout
0.0
Attention dropout
0.0
Epochs
10
Max length
512
Batch size
32
Warmup portion
6%
Initial learning rate
2e-5
Final learning rate
2e-6
Learning rate decay
cosine
Weight decay
0.1
Optimizer
AdamW
Table 14: Hyperparameters for ﬁne-tuning language models on Bokm˚al–Nynorsk machine translation.
Hyperparameter
Value
Dropout
0.1
Attention dropout
0.1
Epochs
3
Batch size
16
Warmup steps
100
Max length
384
Document stride
128
Initial learning rate
1e-4
Final learning rate
0.0
Learning rate decay
linear
Weight decay
0.01
Optimizer
AdamW
Table 15: Hyperparameters for ﬁne-tuning language models on NorQuAD

```
