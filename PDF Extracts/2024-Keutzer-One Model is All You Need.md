---
title: "2024-Keutzer-One Model is All You Need - PDF Extract"
source_pdf: "2024-Keutzer-One Model is All You Need.pdf"
pages: 10
extracted_at: "2026-02-13T09:15:43.023634"
---

# PDF Extract: 2024-Keutzer-One Model is All You Need

**Source PDF:** 2024-Keutzer-One Model is All You Need.pdf
**Total Pages:** 10

---

## Content

```
--- Page 1 ---

One Model is All You Need: ByT5-Sanskrit, a Unified Model for Sanskrit
NLP Tasks
Sebastian Nehrdich1,3, Oliver Hellwig2, and Kurt Keutzer3
1Heinrich Heine University D¨usseldorf,
2University of Z¨urich , Department of Comparative Language Science
3University of California, Berkeley , Berkeley Artificial Intelligence Research (BAIR)
Abstract
Morphologically rich languages are notoriously
challenging to process for downstream NLP
applications. This paper presents a new pre-
trained language model, ByT5-Sanskrit, de-
signed for NLP applications involving the mor-
phologically rich language Sanskrit. We evalu-
ate ByT5-Sanskrit on established Sanskrit word
segmentation tasks, where it outperforms previ-
ous data-driven approaches by a considerable
margin and matches the performance of the cur-
rent best lexicon-based model. It is easier to de-
ploy and more robust to data not covered by ex-
ternal linguistic resources. It also achieves new
state-of-the-art results in Vedic Sanskrit depen-
dency parsing and OCR post-correction tasks.
Additionally, based on the Digital Corpus of
Sanskrit, we introduce a novel multitask dataset
for the joint training of Sanskrit word segmen-
tation, lemmatization, and morphosyntactic tag-
ging tasks. We fine-tune ByT5-Sanskrit on this
dataset, creating a versatile multitask model
for various downstream Sanskrit applications.
We have used this model in Sanskrit linguis-
tic annotation projects, in information retrieval
setups, and as a preprocessing step in a San-
skrit machine translation pipeline. We also
show that our approach yields new best scores
for lemmatization and dependency parsing of
other morphologically rich languages. We thus
demonstrate that byte-level pretrained language
models can achieve excellent performance for
morphologically rich languages, outperforming
tokenizer-based models and presenting an im-
portant vector of exploration when constructing
NLP pipelines for such languages.
1
Introduction
It is generally acknowledged that morphologically
rich languages (MRL) are challenging for NLP
(Tsarfaty et al., 2020). While language modeling
has addressed this challenge, e.g. by integrating
subword information (see e.g. Bojanowski et al.,
2017), there is surprisingly little systematic re-
search on how efficient models for low-level tasks
such as tokenization, lemmatization, morphosyn-
tactic analysis, and dependency parsing can be de-
signed for MRLs. Access to this low-level infor-
mation is relevant for downstream tasks such as
information retrieval and question answering, as
well as for linguistic and literary studies.
In this paper, we introduce a unified model that
jointly performs these tasks for Sanskrit, an ancient
South-Asian MRL, which has been continuously
attested since 1,300 BCE. Vedic, its archaic level,
primarily focusses on the description of the Soma
and the fire sacrifice. Starting around 300 BCE,
the majority of Sanskrit literature was composed
in classical Sanskrit, encompassing a vast array
of domains from religious hymns to scientific and
narrative texts (see Table 2). Linguistic processing
of Sanskrit poses challenges due to its rich mor-
phology and vocabulary, free word order, heavy
compounding, and particularly due to the phonetic
merging of individual words into longer strings
(Sandhi; see e.g. Gupta et al. 2020), as can be
observed in this example:
yuvoh.
hi
m¯at¯a
aditih.
your
indeed
mother
Aditi
Aditi is indeed your mother.
With Sandhi: yuvorhi m¯at¯aditih.
Here, the words yuvoh. and hi as well as m¯at¯a
and aditih. are merged into longer strings, thereby
changing their contact phonemes (h. +h →rh, ¯a+a
→¯a). While the synthesis of Sandhi is determin-
istic, its analysis is not, as the new phoneme -¯a-
in m¯at¯aditih. could also arise from a+a, a+¯a or
¯a+¯a. As a consequence, Sanskrit word segmen-
tation (SWS) needs to be performed in order to
enable tasks such as lemmatization, morphosyntac-
tic tagging, and dependency parsing.
We propose a framework in which we pretrain
a character-level Sanskrit language model based
on ByT5 on a large body of Sanskrit data before
jointly fine-tuning it on a number of downstream
NLP tasks, which we reformulate as sequence-
arXiv:2409.13920v1  [cs.CL]  20 Sep 2024

--- Page 2 ---

generation tasks. This paradigm brings large per-
formance gains, leading to new SOTA results on
established Sanskrit NLP benchmarks. We empha-
size creating a system that is as simple as possible
to train and deploy, without depending on complex
pre- or postprocessing steps and retaining high per-
formance on data that shows challenges such as
OCR mistakes or the use of non-standard language
not sufficiently covered by available linguistic re-
sources.
In concrete terms, we achieve a gain of 8.8
points on perfect sentence matching score (PM)
for the Hackathon SWS benchmark compared
to the current state-of-the-art, while we come close
by 0.13 in performance on the SIGHUM dataset to
the currently best performing lexicon-driven model.
We achieve 4.88 points improvement on the SWS
DCS 2018 benchmark. On Vedic dependency
parsing, we achieve 2.18 points improvement on
UAS and 2.60 points on LAS compared to the
current state-of-the-art. On OCR post-correction,
we outperform the currently best approach by 0.29
lower CER and 3.16 lower WER. We also show
that our approach yields the best performance on
lemmatization and dependency parsing for three
other MLR languages.
We also present a novel dataset for the train-
ing and evaluation of three central Sanskrit NLP
tasks based on the Digital Corpus of Sanskrit
(DCS): Word segmentation, lemmatization, and
morphosyntactic tagging. We show that our pre-
trained model outperforms other baselines on these
new tasks. We also demonstrate that jointly train-
ing on the tasks of SWS, lemmatization, and mor-
phosyntactic tagging on top of the pretrained lan-
guage model leads to the best performance. This
enables the deployment of one single model with-
out dependence on external linguistic resources to
handle all relevant NLP tasks for annotated San-
skrit corpus building with the best performance.
We show that training and evaluating this model on
pseudo-paragraph-level, where multiple sentences
are predicted at once, gives a distinct performance
advantage due to the available contextual informa-
tion.
In Section 2, we give an overview of the relevant
research literature. In Section 3, we discuss the
pretraining and fine-tuning datasets used in this
paper. Section 4 introduces the layout of our pro-
posed multitask framework. In Section 5, we first
evaluate the model on established Sanskrit word
segmentation, Vedic Sanskrit dependency parsing,
OCR post-correction tasks, as well as on other
MLR languages, and then present the performance
of the unified model trained on the new dataset.
We also perform a detailed manual analysis of the
error patterns of the multitask model. We make
the code, all relevant datasets, the pretrained base
model as well as the fine-tuned multitask model
available under the Apache license 2.0 at https:
//github.com/sebastian-nehrdich/
byt5-sanskrit-analyzers.
2
Related Research
The pretrain-fine-tune paradigm, where a pre-
trained language model (PLM) trained on a large
corpus of unlabeled data is subsequently fine-tuned
on a smaller dataset of task-specific labeled data, is
the de-facto standard approach for NLP tasks such
as part-of-speech and morphosyntactic tagging,
sentence classification, and many more since the
publication of the encoder-only approaches BERT
(Devlin et al., 2019) and ELMo (Peters et al., 2018)
in 2018. When it comes to morphologically rich
languages, the good performance of this paradigm
is demonstrated for Turkish in ¨Ozc¸ift et al. (2021),
while Bamman and Burns (2020) and Nehrdich and
Hellwig (2022) show the superior performance of
BERT on linguistic annotation tasks for the mor-
phologically rich classical language Latin.
T5 (Raffel et al., 2019) introduced a new pre-
training paradigm where both encoder and decoder
are trained. This encoder-decoder architecture en-
ables the fine-tuning of the same base model on
diverse tasks such as translation, question answer-
ing, and text classification with the same hyper-
parameters and loss function. Sanh et al. (2022)
further show how the T5 paradigm can be used
efficiently in a multitask setup with large variation
between the different tasks. For morphologically
rich languages, language models that make use
of character-level information show superior per-
formance to those operating on word-level alone
(Gerz et al., 2018). While a number of openly avail-
able pretrained language models exist, only Xue
et al. (2021) followed a tokenizer-free byte-level
approach, resulting in strong performance on lin-
guistic tasks and achieving the best performance
on the morphological inflection task.
Most approaches to Sanskrit NLP tasks such as
Sanskrit word segmentation (SWS) can be broadly
separated into two groups: lexicon-based and data-

--- Page 3 ---

driven. For a recent, comprehensive overview of
the relevant literature, see Sandhan et al. (2022).
Lexicon-driven approaches rely on external linguis-
tic resources, while data-driven approaches learn
from data alone and are therefore less complex to
train and deploy. The main drawback of data-driven
approaches is that they cannot access latent knowl-
edge contained in lexical resources. Sandhan et al.
(2022) combine lexicon-based and data-driven as-
pects, formulating SWS as a character-level se-
quence labeling task that uses lexical information
whenever available. Krishna et al. (2020) presents
a lexicon-based multitask model that handles SWS,
morphological parsing, dependency parsing, syn-
tactic linearization, and prosodic linearization. To
our knowledge, this is the only other published
multitask approach to central Sanskrit NLP tasks.
Pretrained language models supporting Sanskrit
are available, but they are not yet widely used
for Sanskrit linguistic tasks. Conneau and Lam-
ple (2019) included Sanskrit data in its pretraining
setup. Hellwig et al. (2023) trained and evaluated
encoder-only PLMs for the task of Vedic Sanskrit
dependency parsing, coming to the conclusion that
they do not offer clear advantages in performance
yet due to the comparatively small amount of train-
ing data used.
3
Data
For pretraining, we use the Sanskrit data of the San-
graha dataset (Khan et al., 2024) as a basis, which
mostly consists of data gained by a comprehen-
sive OCR effort of the Sanskrit-related literature
available at the Internet Archive1. We only use
the language-verified split of this dataset and none
of the synthetic data. We decided to use this noisy
OCR-based dataset following the observation made
in Bamman and Burns (2020), where a PLM for
Latin trained on a noisy corpus consisting of largely
OCR’d data achieved new state of the art results
on Latin POS tagging tasks. We augment this data
with high-quality human input Sanskrit data from
the GRETIL collection 2 and the Digital Sanskrit
Buddhist Canon.3 The statistics of the dataset are
shown in Table 1.
We use IAST transliteration for pretraining as
well as all of the fine-tuning tasks, as this yields
1archive.org
2https://gretil.sub.uni-goettingen.de/
gretil.html
3https://www.dsbcproject.org/
Source
Number of Characters
IndicLLMSuite
5,173,251,798
GRETIL
253,712,457
DSBC
2,473,226
Table 1: Composition of the pretraining dataset. Num-
ber of characters is measured in character count in IAST
roman transliteration.
Category
Number of Characters
Epics
9,814,868
Vedic
7,211,586
Science
6,299,576
Pur¯an.a
4,682,010
Poetry
2,028,535
Buddhist
1,762,012
other
2,728,511
Table 2: Distribution of the fine-tuning data according to
different categories. Number of characters is measured
in character count in IAST roman transliteration.
clear efficiency advantages compared to Devana-
gari when training on the individual byte level, with
half the bytes needed. While other transliteration
schemes such as SLP1 offer further small gains in
efficiency, we decided against using them as the
human readability advantages of IAST lead to less
overhead during training and evaluation, as well as
less complex deployment pipelines.
3.1
Fine-tuning Dataset
The fine-tuning data utilized in this study for the
SWS, lemmatization, morphological tagging, and
dependency parsing tasks comes from the Digital
Corpus of Sanskrit (DCS; Hellwig 2010–2024), a
collection of classical and Vedic texts with manu-
ally validated lexical and morphosyntactic annota-
tions. For some Vedic texts, the DCS also provides
manually validated syntactic annotations (Hellwig
et al., 2023). The complete annotation is available
as text files in CoNLL-U format,4 serving as input
for the multitask and dependency parsing models
described in this paper. We use a snapshot of the
DCS dataset from April 2024. Table 2 gives an
overview of the DCS fine-tuning data, showing its
bias towards narrative (epics, Pur¯an.as), Vedic, and
scientific texts.
4https://github.com/OliverHellwig/
sanskrit/tree/master/dcs/data/conllu

--- Page 4 ---

4
Proposed Method
We propose the combination of the following
paradigms in order to generate an efficient, high-
performing end-to-end framework for various San-
skrit NLP tasks: We first pretrain a byte-level San-
skrit PLM based on the ByT5 architecture, which
is distributed under the Apache license 2.0, over-
coming the limitation of lack of access to latent
information for data-driven approaches. Then, we
reformulate the central Sanskrit NLP tasks of word
segmentation, lemmatization, and morphosyntac-
tic tagging as sequence generation tasks, using a
novel serialization strategy. In order to distinguish
between the different tasks, we use prefix letters at
the beginning of the input sequence to indicate the
task. “S” for segmentation, “L” for lemmatization,
and “M” for morphosyntactic tagging. Inspired by
T0 (Sanh et al., 2022), we combine these tasks into
a unified multitask setup, enabling the fine-tuning
of a single model to handle all of them simultane-
ously. The schema of this approach is demonstrated
in Figure 2.
The full morphosyntactic tags of the DCS con-
sume on average 46 characters, making their pre-
diction with a byte-level LM challenging. We there-
fore propose a serialization strategy by manually
mapping the morphosyntactic tags to unused letter
combinations of the IAST alphabet, reducing the
number of needed tokens per tag significantly. The
full tags can be restored based on this mapping
without information loss. Figure 1 demonstrates
this process. On average, the compression ratio of
this method is 0.14.
5
Experiments
Models were trained on GPU nodes of 8 NVIDIA
A6000 48GB GPUs. The time needed for pre-
training was one week, while the fine-tuning runs
varied between 2 and 8 hours.
The joint mul-
titask model took 32 hours to finetune.
We
leveraged the DeepSpeed library https://www.
deepspeed.ai/ for training in half precision
bf16, and for making efficient use of the multi-
GPU setup.
For the foundation model, we further pretrain a
ByT5 model (Xue et al., 2021) in the “base” config-
uration with 582M parameters on the entire dataset
for 100,000 steps with a batch size of 512 and
a sequence length of 512. The resulting model
is called ByT5-Sanskrit in this paper. According
to the scaling laws presented in Hoffmann et al.
(2022), the optimal number of parameters for our
training dataset size of 6.5B tokens is about 325M
parameters. This matches the ByT5 “small” config-
uration with 300M parameters. We decided to train
a model one category larger than that to ensure we
get optimal performance.
5.1
Evaluation on Previous Sanskrit Word
Segmentation Tasks
In order to examine how ByT5-Sanskrit performs
in comparison to other baselines, we fine-tune it
on a selection of different previously established
Sanskrit word segmentation tasks, each of which
used its own dataset.
The SIGHUM and Hackathon datasets are
adapted from Sandhan et al. (2022). DCS 2018
is the dataset presented in Hellwig and Nehrdich
(2018). rcNN-SS denotes a character-based seg-
mentation algorithm that performs joint compound
and Sandhi splitting using a combination of re-
current and convolutional operations (Hellwig and
Nehrdich, 2018). TransLIST is the model described
in Sandhan et al. (2022), which uses a combination
of character-level and lexicon-based word input
with a transformer model.
The results of our comparison are shown in Ta-
ble 3. Since TransLIST, due to its elaborate prepro-
cessing pipeline, is not compatible with the DCS
2018 dataset, we cannot evaluate it in that setting.
On DSC 2018 and Hackathon, ByT5-Sanskrit out-
performs the existing best baselines with a very
considerable margin, while it comes close to the
best-performing lexicon-based model, TransLIST,
on the SIGHUM dataset. The results show that
ByT5-Sanskrit successfully learns latent features
of the Sanskrit language and achieves very strong
performance without relying on lexical resources.
The performance gain on the Hackathon task is es-
pecially noteworthy, as this task has the smallest
train split of the three with 89k samples, indicat-
ing that fine-tuning ByT5-Sanskrit is very sample
efficient.
Compared to ByT5-Sanskrit, TransLIST shows
more variation in performance between SIGHUM
and Hackathon, indicating that the quality of data
preprocessing determines the quality of the out-
come for TransLIST to a significant degree. ByT5-
Sanskrit on the other hand shows consistent per-
formance improvements on all three tasks, mak-
ing elaborate lexical pre-processing unnecessary to
reach competitive performance.

--- Page 5 ---

Figure 1: Serialization for the morphosyntactic tagging task. The abbreviated tags are highlighted in red. We use
spaces as separation token between words.
Figure 2: Sanskrit Multitask Formulation: All tasks are converted into sequence-generation tasks. For each task, we
prepend prompt tokens (S, L, LM, here marked in red) in order to enable the model to distinguish between tasks.
For efficient training and inference, we use a novel serialization strategy to compress the morphosyntactic tags into
as few characters as possible, here marked in blue.
DCS 2018
SIGHUM
Hackathon
Model
(509k samples)
(99k samples)
(89k samples)
rcNN-SS
85.2
87.08
77.62
TransLIST
-
93.97
85.47
ByT5-Sanskrit
90.11
93.83
94.29
Table 3: Sentence level perfect matches on previous
Sanskrit word segmentation tasks. Results for rcNN-
SS and TransLIST are reported based on the respective
publications. Due to data incompatibility, we cannot
evaluate TransLIST on the DCS 2018 task. Size of
training dataset in parentheses.
5.2
Vedic Dependency Parsing
We also evaluate the performance of ByT5-Sanskrit
on the Vedic Sanskrit dependency parsing task. We
follow the serialization strategy of Lin et al. (2022)
and reformulate dependency parsing as a sequence
generation task. We compare our results against the
biaffine architecture (Dozat and Manning, 2016) in
its best performing configuration as presented in
Hellwig et al. (2023). Using the latest version of
the dependency annotated data of the DCS for our
experiments,we extract a total number of 24,807
sentences with gold dependency, part of speech,
and morphosyntactic annotation. We use 90% for
training, and 5% for each evaluation and testing.
Following the setup in Hellwig et al. (2023), we
exclude R. gvedic data from the test and evaluation
Biaffine
ByT5-Sanskrit
Setting
UAS
LAS
UAS
LAS
None
77.68
70.67
86.54
81.54
ALL
86.86
81.98
89.04
84.58
Table 4: UAS and LAS for the Vedic dependency pars-
ing. “None”: only surface forms used; “ALL”: all lin-
guistic gold information used
split and apply the augmentation strategy of ran-
domly concatenating up to four sentences from the
training set. Moreover, we replace the POS and
morphosyntactic information of old Vedic citations
(mantras) with a special tag. The biaffine model
and ByT5-Sanskrit are trained and evaluated on the
same data. We use 50 epochs for training. We eval-
uate both models in two settings: One without any
additional linguistic information, using only the
surface form of a word (None), and one where all
available linguistic features (POS tags, morphosyn-
tax, punctuation) are used (All).
The results in Table 4 show significant perfor-
mance improvements of 2.18 in UAS and 2.60 in
LAS over the biaffine baseline. Especially note-
worthy is the observation that the ByT5-Sanskrit-
based parser without any additional linguistic in-
formation comes close to the performance of the
biaffine parser with support of gold data. These

--- Page 6 ---

results are in line with the observations made in
Nehrdich and Hellwig (2022), where the addition
of a strong Latin PLM boosted dependency parsing
performance very significantly on three different
Latin treebanks, with configurations based on the
Latin PLM alone matching those that make use of
gold annotation without the PLM.
5.3
Sanskrit OCR Post-correction
We also evaluate our model on the task of Sanskrit
OCR post-correction as defined in Maheshwari
et al. (2022). Our results are presented in Table
6. We fine-tune ByT5-Sanskrit with a sequence
length of 512. The results show that ByT5-Sanskrit
also achieves the best performance on this task.
5.4
Lemmatization and Dependency Parsing
on other MLR Languages
In order to test whether our proposed framework
generalizes to other MLR languages, we conduct
experiments on lemmatization and dependency
parsing for three MLR languages: Bulgarian, Ro-
manian, and Turkish. The data is taken from the
Universal Dependency (Nivre et al., 2016) 2.2 re-
lease. As the base model for finetuning, we use
ByT5 in the ”base” configuration without further
pretraining. We show the results in Table 5. Since
our serialization strategy requires language exper-
tise, we cannot evaluate our framework on mor-
phosyntactic tagging for these languages. We com-
pare our approach against the current best base-
line UDPipe (Kondratyuk and Straka, 2019) for
lemmatization, for dependency parsing we also
compare against DPSG (Lin et al., 2022), since
their approach reaches the currently best results on
these languages and is structurally very similar to
our, with the main difference being that we use a
byte-level PLM, while they use the tokenizer-based
PLM mT5. The results show that our approach
outperforms the previous best baselines on lemma-
tization for two languages, while outperforming
the previous baselines on dependency parsing for
all languages. This shows that the performance
advantages of byte-level PLMs generalize to other
morphologically rich languages.
5.5
Joint Sanskrit Word Segmentation,
Lemmatization and Morpho-syntax
Tagging Task
We use a snapshot of the DCS from April 2024 as
the basis for our experiments with a total number of
601,403 sentences. We hold back 8,190 sentences
Lemma
Dep. Parsing
Language
Acc
LAS
Turkish IMST (UDPipe)
96.01
67.56
Turkish IMST (Ours, ByT5)
97.94
77.00
Romanian RRT (UDPipe)
98.41
86.74
Romanian RRT (DPSG, mT5)
-
88.76
Romanian RRT (Ours, ByT5)
98.15
91.16
Bulgarian BTB (UDPipe)
97.94
90.35
Bulgarian BTB (DPSG, mT5)
-
93.92
Bulgarian BTB (Ours, ByT5)
98.51
94.11
Table 5: Lemmatization and dependency parsing results
on three other MLR languages based on ByT5 base. The
UDPipe results are reported based on Kondratyuk and
Straka (2019), DPSG based on Lin et al. (2022).
Model
CER
WER
ByT5-Small
2.98
23.19
ByT5-Sanskrit
2.69
20.03
Table 6: CER and WER results for the Sanskrit OCR
post-correction task. ByT5-Small are the results as pre-
sented in Maheshwari et al. (2022).
for evaluation and 8,398 sentences for testing. We
keep the original order of the sentences, ensuring
that this data can also be used to train models on
longer sections of text. The DCS presents a chal-
lenge for our word segmentation model because
the forms without Sandhi were not consistently
recorded during the initial annotation of the DCS.
This incomplete annotation affects 65.8% of all
words in the DCS, primarily from classical San-
skrit, whereas unsandhied forms are recorded for
most Vedic and some Buddhist texts. When gener-
ating conllu files from the DCS, a heuristic that sup-
plements missing unsandhied forms is employed
to address this inconsistency. While this heuris-
tic can occasionally produce morphologically cor-
rect but unattested nominal forms (e.g., generating
hr.dayatah. instead of the attested hr.day¯at for the
ablative singular of hr.daya- ‘heart’), a cursory ex-
amination suggests such cases are infrequent (1-3%
of all words). Since we believe that the heuristi-
cally generated forms can nonetheless be useful for
the training, we include them in the training set and
prepend a special flag “R” at the beginning of each
line containing such forms. The test and validation
splits do not contain any reconstructed forms and
are therefore strongly biased towards Vedic texts.
This makes the annotation tasks more challenging
because Vedic texts are underrepresented in the
DCS (see Table 2).
Since the tasks can be combined arbitrarily, we

--- Page 7 ---

mT5
ByT5
ByT5-Sanskrit
Task
Sen
Sen
Par
Sen
Par
S
76.09
83.71
87.21
84.61
88.21
L
68.27
77.99
82.05
79.88
83.96
S+M
49.94
60.93
71.50
63.86
74.38
L+M
49.23
59.28
69.40
62.00
72.33
S+L+M
49.10
58.75
71.92
61.27
74.31
Table 7: Sentence level perfect match results for the
multitask experiment. ”S” denotes the task of Sanskrit
word segmentation, ”L” the task of lemmatization, and
”M” the task of morphosyntax tagging.
Figure 3: Results of the detailed error analysis
decided to limit the experiments to a number of
settings with real-world relevance. We provide
the data on sentence- and pseudo-paragraph level.
Pseudo-paragraphs are constructed by concatenat-
ing adjunct sentences with a length of up to 512
characters, giving the model the possibility to uti-
lize contextual information.
We show the results in Table 7. As the lexical re-
sources used for Sandhan et al. (2022) and Krishna
et al. (2020) are not compatible with our dataset,
we cannot evaluate their performance in this setting.
Due to resource constraints, we could not evaluate
mT5 on paragraph level. ByT-Sanskrit outperforms
all other models on these tasks. The visible gains
compared to ByT5 indicate that even in a multi-
task setup with a large fine-tuning dataset, the prior
knowledge from the pretraining stage brings dis-
tinct performance advantages. The weaker perfor-
mance of mT5 shows that tokenizer-based models
don’t perform as well in this setting. All models
perform better on pseudo-paragraph level, show-
ing that contextual information beyond sentence
boundaries is crucial for Sanskrit linguistic tasks
and should be used wherever possible. The visi-
ble performance drop that occurs when including
morphosyntactic tagging can be explained by the
fact that these tags are often ambiguous, as will be
discussed in the error analysis below.
5.6
Error analysis
For a detailed error analysis, one author of this
paper inspected 150 randomly drawn sentences in
which the model result differs from ground truth.
The differences were categorized into three classes:
(1) errors in the ground truth data which were cor-
rected by the model; (2) ambiguous cases where
both ground truth and model result are acceptable;
and (3) model errors. These three classes were fur-
ther subsetted with fine-grained error labels. Most
basically, the segmentation of a string may have
failed or parts of the analysis is missing or added.
Figure 3 shows that these cases constitute only a
small part of all errors. Notably, missegmentations
as well as missing words are also present in the
ground truth, e.g. when a meaningful linguistic
analysis of a string was impossible.
Most differences are observed at the lexical and
morphological levels. The pattern of model errors
aligns with the summary in Gupta et al. (2020),
primarily relating to nominal endings that denote
more than one case. For instance, an error is seen
in the phrase uttam¯ay¯a di´sah. ‘from the highest re-
gion’, where both the correctly reconstructed end-
ing -¯ay¯ah. in uttam¯ay¯ah. and -ah. in di´sah. can signify
a genitive or ablative singular. However, the senten-
tial context of this phrase unambiguously indicates
an ablative interpretation. Errors in the analysis of
verbal morphology are less common and typically
occur with unusual and rare forms. An example
is ¯avarvratatah. , the genitive singular of a partici-
ple derived from the intensive of the verb ¯a vart-
‘revolve’ (‘of someone who rotates intensively’).
The model misinterpreted this complex form as
the nominative singular of a newly coined noun
¯avarvrata-.
Both gold and silver exhibit a significant number
of ambiguities. Consider the following phrase:
aparen. a
´s¯al¯ay¯ah.
western-ADJ.INS.SG
hall-GEN/ABL.SG
to the west of-PREP
‘to the west of the hall’
Here, aparen. a is an example of a lexical ambi-
guity. While, at the level of morphosyntax, the
word is the instrumental singular of the adjective
apara- ‘western’, it can be argued that this word
became grammaticalized in Vedic, as was shown
for Vedic madhye ‘in the middle’ > Hindi mem. ‘in’
(Rein¨ohl, 2016). Although the grammaticalized
reading is preferred in the DCS, analyzing aparen. a
as an inflected adjective is perfectly valid, given our

--- Page 8 ---

limited knowledge about the temporal dynamics of
grammaticalization processes. Similarly, while the
genitive reading of ´s¯al¯ay¯ah. is the preferred analysis
in the DCS, the ablative cannot be ruled out here,
leading to a morphological ambiguity.
Beyond this, lexical ambiguities in the DCS pri-
marily arise from compound splitting. The DCS
follows major Sanskrit dictionaries in not split-
ting compounds deemed to have non-compositional
meanings. Given the lexical transparency of most
Sanskrit compounds, splitting them into their con-
stituent parts is often a justifiable approach. For
instance, the DCS keeps the compound ¯adikarah.
“creator” intact, but our model reasonably splits it
into ¯adi-karah. “beginning-maker”.
In about one third of all cases, our model corrects
a wrong analysis in the DCS. One case is dv¯ada´sa-
kap¯alam ‘(consisting of) twelve cups’ where the
first word is the compound form of the numeral
dv¯ada´san- ‘twelve’, but not, as recorded in the
DCS, of the adjective dv¯ada´sa- ‘twelfth’. Appar-
ently our model achieves a quality high enough to
be usable for error detection in the ground truth
data. While retraining ByT5-Sanskrit with cor-
rected data is not likely to improve its quality, such
error correction may nevertheless be useful for lin-
guistic studies.
Overall, more than half of the 150 sentences in-
spected (80 or 53.3%) revealed errors in the source
data or alternative valid readings. Together with
the bias in the test data (see Section 5.5), this result
indicates that the predictive quality of our model is
higher than indicated by the numbers in Table 7.
5.7
Ablation Study
To assess the impact of joint training on multiple
tasks, we conducted an ablation study where we
fine-tuned ByT5-Sanskrit on selected tasks individ-
ually. The results, presented in the upper half of
Table 8, clearly demonstrate that individual task
training diminishes performance for both segmen-
tation and lemmatization tasks. This confirms that
transfer learning across different tasks contributes
to enhanced overall performance.
A second experiment evaluated the effect of re-
moving samples containing reconstructed surface
forms (refer to Section 5.5). This condition re-
duced the training sample size to merely 26.22% of
the original data, effectively serving as an ablation
experiment probing the dataset size. Despite a no-
ticeable negative impact on performance (as seen
Task
Sentence PM
Segmentation only
83.52 (-1.09)
Lemmatization only
77.52 (-2.35)
Segmentation only w/o rec.
81.58 (-3.03)
Lemmatization only w/o rec.
76.85 (-3.03)
Table 8: Ablation Study where we fine-tune ByT-
Sanskrit on individual tasks seperately to show the per-
formance difference to the multitask setup. W/o rec.
indicates the setting where reconstructed forms (see
Section 5.5) are not used in the training dataset. Results
are given in sentence level perfect matches.
in the lower half of Table 8), the effect was less
pronounced than we anticipated. We hypothesize
that this behavior can primarily be attributed to the
strong priors of the ByT5-Sanskrit model. Con-
currently, removing sentences with reconstructed
forms from training rendered the distributions of
training and test data, which exclusively contain
such sentences, more similar. This suggests that
our approach is viable even for languages with a
limited amount of labeled training data.
6
Conclusion and Future Work
We have demonstrated that by pretraining a byte-
level language model on a large collection of
mostly noisy data, new state-of-the-art results for
Sanskrit word segmentation, Vedic dependency
parsing, and OCR post-correction are achieved,
closing the performance gap between lexicon-
based and data-driven Sanskrit NLP approaches.
We further demonstrated that this pretrained lan-
guage model can be used as a basis for a multitask
model that handles word segmentation, lemmati-
zation, and morphosyntactic tagging jointly with
high accuracy. We further demonstrated that this
multitask model benefits greatly from training and
inference on pseudo-paragraph-level. For the joint
fine-tuning on these tasks, we presented a novel
dataset. The resulting unified model, being inde-
pendent of external linguistic resources, is simple
to deploy and is already used for Sanskrit corpus
annotation projects as well as in information re-
trieval and machine translation setups. We also
showed that our approach generalizes to other mor-
phologically rich languages, where the application
of a byte-level PLM yields best results for two lan-
guages on lemmatization and for three languages
on dependency parsing. We thus establish that byte-
level PLMs are a crucial vector of exploration when
builiding NLP pipelines for MLR languages.

--- Page 9 ---

7
Limitations
Our model currently does not adequately address
the homonymy of words. In the DCS, 7.5% of
all lemmata, or tokenized words, have at least one
homonym. These homonyms account for a signifi-
cant 57.5% of all tokenized words. However, this
percentage is somewhat misleading. The primary
contributors to this high rate of homonymy are in-
declinable words such as ca ‘and’ and iti ‘thus’.
These words are used as nouns in grammatical liter-
ature, most notably in P¯an.ini’s As.t.¯adhy¯ay¯ı, where
their case endings indicate grammatical uses (e.g.,
at As.t.¯adhy¯ay¯ı 1.1.16: ...
itau an¯ars.e ‘in front
of (the particle) iti in non-Vedic texts’). In non-
grammatical texts, these words almost always have
their non-technical meaning. Similar considera-
tions apply to the use of nominalized verbal roots
in grammatical texts.
There are more problematic, but less frequent
cases. For instance, the word veda has four differ-
ent lemmata recorded in the DCS: (1) the famous
text collection of the same name, (2) ‘finding, ob-
taining’, (3) a small broom, and (4) the name of
a man. At least homonyms (1) and (3) are regu-
larly attested in Vedic and classical Sanskrit. Merg-
ing them into one lemma is lexicographically in-
adequate: while (1) and (2) may be etymologi-
cally related, (3) and probably also (4) are not (see
Mayrhofer, 1992, 579-581). However, the context
of their occurrence typically indicates very clearly
which of the lemmata is meant.
To address this issue, we plan to mark lemmata
with homonyms by numeric affixes in future ver-
sions of our model.
References
David Bamman and Patrick J. Burns. 2020. Latin bert:
A contextual language model for classical philology.
ArXiv, abs/2009.10053.
Piotr Bojanowski, Edouard Grave, Armand Joulin, and
Tomas Mikolov. 2017. Enriching word vectors with
subword information. Transactions of the Associa-
tion for Computational Linguistics, 5:135–146.
Alexis Conneau and Guillaume Lample. 2019. Cross-
lingual language model pretraining. Curran Asso-
ciates Inc., Red Hook, NY, USA.
Jacob Devlin, Ming-Wei Chang, Kenton Lee, and
Kristina Toutanova. 2019. Bert: Pre-training of deep
bidirectional transformers for language understand-
ing. In North American Chapter of the Association
for Computational Linguistics.
Timothy Dozat and Christopher D. Manning. 2016.
Deep biaffine attention for neural dependency pars-
ing. ArXiv, abs/1611.01734.
Daniela Gerz, Ivan Vuli´c, Edoardo Ponti, Jason Narad-
owsky, Roi Reichart, and Anna Korhonen. 2018.
Language Modeling for Morphologically Rich Lan-
guages: Character-Aware Modeling for Word-Level
Prediction. Transactions of the Association for Com-
putational Linguistics, 6:451–465.
Ashim Gupta, Amrith Krishna, Pawan Goyal, and Oliver
Hellwig. 2020. Evaluating neural morphological tag-
gers for Sanskrit. In Proceedings of the 17th SIG-
MORPHON Workshop on Computational Research
in Phonetics, Phonology, and Morphology, pages
198–203, Online. Association for Computational Lin-
guistics.
Oliver Hellwig. 2010–2024. DCS - The Digital Corpus
of Sanskrit.
Oliver Hellwig and Sebastian Nehrdich. 2018. San-
skrit word segmentation using character-level recur-
rent and convolutional neural networks. In Proceed-
ings of the 2018 Conference on Empirical Methods
in Natural Language Processing, pages 2754–2763,
Brussels, Belgium. Association for Computational
Linguistics.
Oliver Hellwig, Sebastian Nehrdich, and Sven Sellmer.
2023. Data-driven dependency parsing of Vedic San-
skrit. Language Resources and Evaluation, 57:1173–
1206.
Jordan Hoffmann, Sebastian Borgeaud, Arthur Mensch,
Elena Buchatskaya, Trevor Cai, Eliza Rutherford,
Diego de Las Casas, Lisa Anne Hendricks, Johannes
Welbl, Aidan Clark, Tom Hennigan, Eric Noland,
Katie Millican, George van den Driessche, Bogdan
Damoc, Aurelia Guy, Simon Osindero, Karen Si-
monyan, Erich Elsen, Jack W. Rae, Oriol Vinyals,
and L. Sifre. 2022. Training compute-optimal large
language models. ArXiv, abs/2203.15556.
Mohammed Safi Ur Rahman Khan, Priyam Mehta,
Ananth Sankar, Umashankar Kumaravelan, Sumanth
Doddapaneni, Suriyaprasaad G, Varun Balan G,
Sparsh Jain, Anoop Kunchukuttan, Pratyush Kumar,
Raj Dabre, and Mitesh M. Khapra. 2024. Indicllm-
suite: A blueprint for creating pre-training and fine-
tuning datasets for Indian languages.
D. Kondratyuk and M. Straka. 2019. 75 languages, 1
model: Parsing universal dependencies universally.
In Conference on Empirical Methods in Natural Lan-
guage Processing.
Amrith Krishna, Bishal Santra, Ashim Gupta, Pavanku-
mar Satuluri, and Pawan Goyal. 2020. A graph-based
framework for structured prediction tasks in Sanskrit.
Computational Linguistics, 46(4):785–845.
Boda Lin, Zijun Yao, Jiaxin Shi, Shulin Cao, Binghao
Tang, Si Li, Yong Luo, Juanzi Li, and Lei Hou. 2022.
Dependency parsing via sequence generation. In

--- Page 10 ---

Conference on Empirical Methods in Natural Lan-
guage Processing.
Ayush Maheshwari, Nikhil Singh, Amrith Krishna, and
Ganesh Ramakrishnan. 2022.
A benchmark and
dataset for post-OCR text correction in Sanskrit. In
Findings of the Association for Computational Lin-
guistics: EMNLP 2022, pages 6258–6265, Online.
Association for Computational Linguistics.
Manfred Mayrhofer. 1992. Etymologisches W¨orterbuch
des Altindoarischen. I. Band. Carl Winter, Heidel-
berg.
Sebastian Nehrdich and Oliver Hellwig. 2022. Accu-
rate dependency parsing and tagging of Latin. In
Proceedings of the Second Workshop on Language
Technologies for Historical and Ancient Languages,
pages 20–25, Marseille, France. European Language
Resources Association.
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
Matthew E. Peters, Mark Neumann, Mohit Iyyer, Matt
Gardner, Christopher Clark, Kenton Lee, and Luke
Zettlemoyer. 2018. Deep contextualized word repre-
sentations. ArXiv, abs/1802.05365.
Colin Raffel, Noam M. Shazeer, Adam Roberts, Kather-
ine Lee, Sharan Narang, Michael Matena, Yanqi
Zhou, Wei Li, and Peter J. Liu. 2019. Exploring the
limits of transfer learning with a unified text-to-text
transformer. J. Mach. Learn. Res., 21:140:1–140:67.
Uta Rein¨ohl. 2016. Grammaticalization and the Rise of
Configurationality in Indo-Aryan. Oxford University
Press, Oxford, UK.
Jivnesh Sandhan, Rathin Singha, N. Venkat Rao, Su-
vendu Samanta, Laxmidhar Behera, and Pawan
Goyal. 2022.
TransLIST: A transformer-based
linguistically informed Sanskrit tokenizer. ArXiv,
abs/2210.11753.
Victor Sanh, Albert Webson, Colin Raffel, Stephen
Bach, Lintang Sutawika, Zaid Alyafeai, Antoine
Chaffin, Arnaud Stiegler, Arun Raja, Manan Dey,
M Saiful Bari, Canwen Xu, Urmish Thakker,
Shanya Sharma Sharma, Eliza Szczechla, Taewoon
Kim, Gunjan Chhablani, Nihal Nayak, Debajyoti
Datta, Jonathan Chang, Mike Tian-Jian Jiang, Han
Wang, Matteo Manica, Sheng Shen, Zheng Xin Yong,
Harshit Pandey, Rachel Bawden, Thomas Wang, Tr-
ishala Neeraj, Jos Rozen, Abheesht Sharma, An-
drea Santilli, Thibault Fevry, Jason Alan Fries, Ryan
Teehan, Teven Le Scao, Stella Biderman, Leo Gao,
Thomas Wolf, and Alexander M Rush. 2022. Multi-
task prompted training enables zero-shot task gener-
alization. In International Conference on Learning
Representations.
Reut Tsarfaty, Dan Bareket, Stav Klein, and Amit Seker.
2020. From SPMRL to NMRL: What did we learn
(and unlearn) in a decade of parsing morphologically-
rich languages (MRLs)? In Proceedings of the 58th
Annual Meeting of the Association for Computational
Linguistics, pages 7396–7408, Online. Association
for Computational Linguistics.
Linting Xue, Aditya Barua, Noah Constant, Rami Al-
Rfou, Sharan Narang, Mihir Kale, Adam Roberts,
and Colin Raffel. 2021. ByT5: Towards a token-free
future with pre-trained byte-to-byte models. Transac-
tions of the Association for Computational Linguis-
tics, 10:291–306.
Akın ¨Ozc¸ift, Kamil Akarsu, Fatma Yumuk, and Cevh-
ernur S¨oylemez. 2021. Advancing natural language
processing (NLP) applications of morphologically
rich languages with bidirectional encoder representa-
tions from transformers (BERT): an empirical case
study for Turkish. Automatika, 62(2):226–238.

```
