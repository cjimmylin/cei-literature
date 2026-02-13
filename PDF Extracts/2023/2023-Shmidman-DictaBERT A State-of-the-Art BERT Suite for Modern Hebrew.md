---
title: "2023-Shmidman-DictaBERT A State-of-the-Art BERT Suite for Modern Hebrew - PDF Extract"
source_pdf: "2023-Shmidman-DictaBERT A State-of-the-Art BERT Suite for Modern Hebrew.pdf"
pages: 10
extracted_at: "2026-02-13T09:50:27.904159"
---

# PDF Extract: 2023-Shmidman-DictaBERT A State-of-the-Art BERT Suite for Modern Hebrew

**Source PDF:** 2023-Shmidman-DictaBERT A State-of-the-Art BERT Suite for Modern Hebrew.pdf
**Total Pages:** 10

---

## Content

```
--- Page 1 ---

DictaBERT: A State-of-the-Art BERT Suite for Modern Hebrew
Shaltiel Shmidman1,†, Avi Shmidman1,2,‡, Moshe Koppel1,2,†
1DICTA / Jerusalem, Israel
2Bar Ilan University / Ramat Gan, Israel
†{shaltieltzion,moishk}@gmail.com
‡avi.shmidman@biu.ac.il
Abstract
We present DictaBERT, a new state-of-the-
art pre-trained BERT model for modern He-
brew, outperforming existing models on most
benchmarks. Additionally, we release three
fine-tuned versions of the model, designed to
perform three specific foundational tasks in the
analysis of Hebrew texts: prefix segmentation,
morphological tagging and question answering.
These fine-tuned models allow any developer
to perform prefix segmentation, morphological
tagging and question answering of a Hebrew in-
put with a single call to a HuggingFace model,
without the need to integrate any additional li-
braries or code. In this paper we describe the
details of the training as well and the results on
the different benchmarks. We release the mod-
els1 to the community, along with sample code
demonstrating their use. We release these mod-
els as part of our goal to help further research
and development in Hebrew NLP.
1
Introduction
In recent years, Hebrew NLP research has made
major progress with the release of various pre-
trained language models with Hebrew support.
The first was the multi-lingual transformer model
mBERT, based on the BERT architecture (Devlin
et al., 2019), which was then followed by several
other models of a similar architecture (HeBERT
(Chriqui and Yahav, 2022), AlephBERT (Seker
et al., 2021), AlephBERTGimmel (Gueta et al.,
2023), and HeRo (Shalumov and Haskey, 2023)).
Earlier this year it was shown that when finetuned,
the much larger mT5 (Xue et al., 2021) models per-
form very well on the various Hebrew benchmarks
(Eyal et al., 2022) resulting in SOTA scores for
most of the experiments.
We present our model DictaBERT which is
based on the BERT architecture with minor modi-
1Exact
license
can
be
found
at
https://
creativecommons.org/licenses/by-sa/4.0/
fications to the training parameters, as well as im-
proved training set and an improved procedure for
preprocessing training samples. The model outper-
forms previous BERT models on most benchmarks,
with the most noticeable improvement seen on the
QA task. This gain is significant, as the QA task re-
quires more complex syntactic understanding than
other tasks. The performance gain on this task may
indicate increased language comprehension in the
model. Notably, the model’s performance on the
QA task is essentially equivalent2 to that of the
mT5-XL model, a model with over 10 times as
many parameters as DictaBERT.
We
also
present
DictaBERT-morph,
DictaBERT-seg
and
DictaBERT-heq,
customized models fine-tuned for morphological
tagging, prefix segmentation and question an-
swering, respectively. The models are released
with sample code for easy integration.3
These
fine-tuned models allow any developer to perform
prefix segmentation and morphological tagging
and question answering of a Hebrew input with
a single call to a HuggingFace model, without
the need to integrate any additional libraries or
code. The details of the fine-tuning are detailed in
section 4.
2
Approach
2.1
Tokenizer
We use the Word-Piece tokenization method pro-
posed by Song et al. (2021) with the default normal-
izers and preprocessors suggested by HuggingFace,
with the following modification:
We added a pre-tokenizer to handle usage of
quotation marks and apostrophes in Modern He-
brew. We make sure to keep as single tokens words
2The QA task is scores with two measures: EM (exact
match) and F1. DictaBERT achieves a slightly higher score
for the EM, whereas mT5-XL achieves a slightly higher score
for the F1.
3The sample code can be found in the appendix.
arXiv:2308.16687v2  [cs.CL]  13 Oct 2023

--- Page 2 ---

with quotation marks meant as abbreviations (e.g.,
) and words with an apostrophe indicating
foreign sounds (e.g.,
).
Following the work in AlephBertGimmel, the
tokenizer was trained with a vocabulary size of
128,000 tokens.
2.2
Pre-training Data
Our training dataset is a mixture of several sources,
summing to a total of three billion words (3.8B
tokens). We’d like to emphasize that none of the
data is synthetic. The dataset is built up of several
different components:
C4 [70%]. We start with the HeDC4 corpus
released by (Shalumov and Haskey, 2023), and
continue further cleaning it. We removed approxi-
mately 15% of the corpus using various techniques
including histograms and gibberish detectors, as
well as removing sentences that had a very high per-
plexity when run through an MLM scoring function.
We limited our training corpus to contain mainly
English and Hebrew; sentences that contained a
disproportionate number of non-English/Hebrew
tokens were removed. In addition, in order to retain
only documents of substantial content, we filter out
any document with less than 50 words.
Other sources [30%]. We collected data from
various other sources including news sites, blogs,
tv and movie subtitles, novels, and more. This data
was also run through the cleaning process described
above, although without the final filter by length.
2.3
Training Objectives
In the original BERT article (Devlin et al., 2019),
the model was pretrained using two objectives:
MLM (masked language modeling) and NSP (next
sentence prediction). Following the work by Liu
et al. (2019), we removed the NSP objective from
the training, and only trained with the MLM objec-
tive.
In addition, we made slight adjustments to the
constructions of the training examples for the MLM
objective, as follows:
1. We don’t mask tokens that are broken up into
multiple word-pieces. In our research, we found
that masking part of a word and training to predict
it results in lower quality model.
2. We never truncate part of a sentence. If we
are creating a training example from a document
that is longer than the maximum length, we remove
entire sentences from the end of the example, such
that we maximize the number of full sentences that
can be fit within the training example, without any
premature sentence truncation.
3. In order to help the model cope with data that
isn’t fully clean, and in order to expand the utility of
the MLM function for downstream tasks, we insert
randomly in 10% of instances a [BLANK] token.
This token helps the model learn that sometimes
there can be a word in a sentence that doesn’t actu-
ally belong there. An example of a downstream use
case in which this would be useful is when utilizing
the MLM feature to predict word alternates: the
prediction of a [BLANK] indicates that the word
can be optionally be left out altogether.
4. In addition, in order to keep the training data
as clean as possible, we throw out any training
instance with the [UNK] token, in order to ensure
that we train on authentically Hebrew data. This
resulted in throwing out approximately 3% of the
sentences in our already cleaned dataset.
2.4
Training Details and Hyperparameters
We trained our model with the HuggingFace ar-
chitecture wrapped with NVIDIA libraries4 which
are highly optimized for training compute-heavy
machine learning models on NVIDIA hardware.
We pre-trained the model on 4 A100 40GB GPUs
for a total of 36,000 iterations, for a total of 35B
tokens (1.75 epochs of each example 5 times). The
training was done in 3 phases:
(1) Sequences of up to 256 tokens with a learning
rate of 6e-3 for 0.7 epochs.
(2) Sequences of 256 tokens with a learning rate
of 1e-4 for 0.3 epochs.
(3) Sequences of 512 tokens with a learning rate
of 5e-5 for 0.75 epochs.
The total training time was 9.4 days. The train-
ing was done with a global batch size of 8,192,
warmup proportion of 0.2843 for phase 1 & 2, and
0.128 for phase 3.
3
Experiments and Results
We compare the performance of DictaBERT with
previous Hebrew models of similar paramater size,
drawing results from their respective publications
when they exist; otherwise we fill in the scores by
finetuning the models ourselves. The models we
compare to are: mBERT, AlephBert, AlephBert-
Gimmel, HeRo, mT5-Base. For the QA task, we
4https://github.com/NVIDIA/
DeepLearningExamples/tree/master/
PyTorch/LanguageModeling/BERT

--- Page 3 ---

Seg
POS
Features
mBERT
96.07
93.14
92.68
AlephBert
97.88
95.81
95.27
ABG
98.09
96.22
95.76
HeRo
97.86
96.05
95.61
mT5-Base
96.34
95.9
-
DictaBERT
98.16
96.25
96.1
Table 1: Performance Comparison of Different Models
on the Morphology task
also compare our results to the much larger mT5-
XL model (3.7B parameters).
Following previous publications, we tested our
model on the following tasks:
Morphology We follow the multi-task configu-
ration setup and evaluation procedure detailed in
Seker et al. (2021) in order to fine-tune for segmen-
tation, part of speech, and fine-grained morpholog-
ical feature prediction, and in order to calculate the
MultiSet (mset) scores for evaluation. We train the
model with the same training & test data used in
previous works for this task. The results for this
task are listed in Table 1. DictaBERT outper-
forms all previous models.
Named Entity Recognition (NER) We train on
the NEMO dataset presented by Bareket and Tsar-
faty (2021), which contains 9 categories and 6,220
sentences (7,713 entities). We report the token F1
score for each model. The results for this task are
listed in Table 2. DictaBERT outperforms all
previous models.
Sentiment Analysis We evaluate our model on
the sentiment analysis dataset presented in Amram
et al. (2018), based on 12K social media comments.
The results for this task are also listed in Table 2.
DictaBERT outperforms all previous models.
Question Answering For this task we use the
newly released HeQ dataset by Cohen et al. (2023),
which contains 30K high quality samples from the
GeekTime newsfeed, and from Wikipedia. The
results for this task are listed in Table 3. As dis-
cussed above, DictaBERT outperforms all previ-
ous models of similar parameter size, and performs
essentially equivalent to the much larger mT5-XL
model5.
5We are also pleased to share the weights to our finetuned
version of mT5-XL, after finetuning it on the HeQ corpus.
The model is available for use on huggingface here: https:
//huggingface.co/dicta-il/mt5-xl-heq
Sentiment
NER
mBERT
84.21
79.11
AlephBert
89.02
83.62
AlephBertGimmel
89.51
85.26
HeRo
89.56
86.79
mT5-Base
87.25
74.7
DictaBERT
89.79
87.01
Table 2: Performance Comparison of Different Models
on the Sentiment and NER tasks
HeQ-EM
HeQ-F1
mBERT
62.7
71.42
AlephBert
57.91
67.66
AlephBertGimmel
57.12
67.37
HeRo
61.89
71.3
mT5-Base
53.65
65.03
mT5-XL
63.4
73.5
DictaBERT
63.6
72.9
ChatGPT
9.38
32.19
Table 3: Performance Comparison of Different Models
on the QA task
4
Fine-tuned Models
With this publication, we are also releasing three
fine-tuned models, with sample code, in order to
allow easy integration of DictaBERT’s segmenta-
tion and morph analysis and question answering
capabilities into any product or experiment.
We wish to emphasize that for the morph anal-
ysis and segmentation models, although the eval-
uation above used the exact training and test data
used in previous works in order to ensure fair com-
parison of DictaBERT’s capabilities with previous
BERT models, the fine-tuned models that we are
currently releasing were fine-tuned on much larger
corpora and with a simpler output format for easy
integration, in order to provide maximum practical
value to the community.
4.1
DictaBERT-seg
This model was trained on a prefix segmentation
task, wherein, given a sentence, we aim to identify
the letters that function as proclitics at the begin-
nings of the words, segmenting them from the es-
sential word unit. For example, the word
("that went") would be segmented into
("that")
and
("went"). Note that this model does not
segment suffixes, if any, at the ends of the words.
Training Data The training data for the fine-

--- Page 4 ---

tuning of DictaBERT-seg is made up of various
modern Hebrew texts including Wikipedia, blogs,
and more. The prefix segmentation training set
was initially automatically derived from Dicta’s
in-house diacritized corpus, and subsequently re-
viewed and corrected by an expert human annotator.
The training data consists of 52K sentences with a
total of 1.2M words.
Architecture The architecture of the model is as
follows: We run each word of the sentence through
eight classifiers in order to predict the probability
of each of eight different possible prefix functions
a Hebrew proclitic may serve. We train the model
to predict the relevant prefix classes for each word
given its sentence context. During inference, we
limit the predictions to valid sets of proclitic func-
tions given the initial letters of the word. When
words are comprised of multiple word pieces, we
train on the first word piece alone, because the pro-
clitics will virtually always be contained within
the initial word piece (although we determine the
valid sets of proclitic functions based on the whole
word).
Sample code and output is displayed in Ap-
pendix A.
4.2
DictaBERT-morph
This model was trained on a morphology task,
where given a sentence, we aim to tag the fine-
grained morphological features of each word.
Specifically, DictaBERT-morph predicts part-
of-speech, as well as gender, number, person, and
tense, wherever relevant. Similarly to the previous
model, this model also identifies proclitic functions.
Additionally, this model also identifies whether
there is a suffix appended to the word, and if so,
which function it serves, and also the gender, num-
ber, and person of the suffix.
Training Data We used the UD Treebank (Sade
et al., 2018) which consists of 5K tagged sentences
in the train split, as well an additional 35K sen-
tences from the IAHLT6 UD corpus of tagged He-
brew sentences (Zeldes et al., 2022).
Architecture For every word in a sentence, we
we train five classifiers to predict the morphologi-
cal features of that word. For cases where a word
is broken up into multiple word pieces, we per-
6We would like to express our thanks to IAHLT
for this tagged corpus.
For more information regard-
ing the resources curated and made available by IAHLT,
see: https://github.com/IAHLT/iahlt.github.
io/blob/main/index.md
form the predictions on the first word piece. The 5
classifiers are as follows:
• Prediction of the POS for the main word
• Prediction of the proclitic functions (can be
multiple or none - e.g.,
["from the
meal"] has both an ADP and DET prefix)
• Prediction of the fine-grained morphological
features of the word (gender, number, person,
and tense)
• Prediction of whether there is a suffix and
which function it serves
• Predictions of fine-grained features of the suf-
fix (gender, number, and person), if the previ-
ous classifier predicts that there is a suffix
Sample code and output is displayed in Ap-
pendix B.
4.3
DictaBERT-heq
This model was trained on the question answering
task, where given a context and a question, we aim
to extract the answer to the question from the con-
text. This model uses the standard HuggingFace
architecture for Bert-Question-Answering. The
model was trained on the HeQ train dataset as listed
in the experiment section.
Sample code and output is displayed in Ap-
pendix C.
5
Conclusion
We are happy to release these model to the public to
help further research and development in Hebrew.7
References
Adam Amram, Anat Ben David, and Reut Tsarfaty.
2018.
Representations and architectures in neu-
ral sentiment analysis for morphologically rich lan-
guages: A case study from Modern Hebrew. In Pro-
ceedings of the 27th International Conference on
Computational Linguistics, pages 2242–2252, Santa
7The base model DictaBERT is available at https:
//huggingface.co/dicta-il/dictabert
The fine-tuned segmentation model DictaBERT-seg is
available at https://huggingface.co/dicta-il/
dictabert-seg
The fine-tuned morphology model DictaBERT-morph is
available at https://huggingface.co/dicta-il/
dictabert-morph
The fine-tuned QA model DictaBERT-heq is avail-
able
at
https://huggingface.co/dicta-il/
dictabert-heq.

--- Page 5 ---

Fe, New Mexico, USA. Association for Computa-
tional Linguistics.
Dan Bareket and Reut Tsarfaty. 2021. Neural Model-
ing for Named Entities and Morphology (NEMO2).
Transactions of the Association for Computational
Linguistics, 9:909–928.
Avihay Chriqui and Inbal Yahav. 2022. HeBERT and
HebEMO: A hebrew BERT model and a tool for po-
larity analysis and emotion recognition. INFORMS
Journal on Data Science, 1(1):81–95.
Amir DN Cohen, Hilla Merhav Fine, Yoav Goldberg,
and Reut Tsarfaty. 2023. Heq: a large and diverse
hebrew reading comprehension benchmark.
Jacob Devlin, Ming-Wei Chang, Kenton Lee, and
Kristina Toutanova. 2019. Bert: Pre-training of deep
bidirectional transformers for language understand-
ing.
Matan Eyal, Hila Noga, Roee Aharoni, Idan Szpektor,
and Reut Tsarfaty. 2022. Multilingual sequence-to-
sequence models for hebrew nlp.
Eylon Gueta, Avi Shmidman, Shaltiel Shmidman,
Cheyn Shmuel Shmidman, Joshua Guedalia, Moshe
Koppel, Dan Bareket, Amit Seker, and Reut Tsar-
faty. 2023. Large pre-trained models with extra-large
vocabularies: A contrastive analysis of hebrew bert
models and a new one to outperform them all.
Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Man-
dar Joshi, Danqi Chen, Omer Levy, Mike Lewis,
Luke Zettlemoyer, and Veselin Stoyanov. 2019.
Roberta: A robustly optimized bert pretraining ap-
proach.
Shoval Sade, Amit Seker, and Reut Tsarfaty. 2018.
The Hebrew Universal Dependency treebank: Past
present and future. In Proceedings of the Second
Workshop on Universal Dependencies (UDW 2018),
pages 133–143, Brussels, Belgium. Association for
Computational Linguistics.
Amit Seker,
Elron Bandel,
Dan Bareket,
Idan
Brusilovsky, Refael Shaked Greenfeld, and Reut Tsar-
faty. 2021. Alephbert:a hebrew large pre-trained lan-
guage model to start-off your hebrew nlp application
with.
Vitaly Shalumov and Harel Haskey. 2023.
Hero:
Roberta and longformer hebrew language models.
arXiv:2304.11077.
Xinying Song, Alex Salcianu, Yang Song, Dave Dopson,
and Denny Zhou. 2021. Fast wordpiece tokenization.
Linting Xue, Noah Constant, Adam Roberts, Mihir Kale,
Rami Al-Rfou, Aditya Siddhant, Aditya Barua, and
Colin Raffel. 2021. mT5: A massively multilingual
pre-trained text-to-text transformer. In Proceedings
of the 2021 Conference of the North American Chap-
ter of the Association for Computational Linguistics:
Human Language Technologies, pages 483–498, On-
line. Association for Computational Linguistics.
Amir Zeldes, Nick Howell, Noam Ordan, and Yifat Ben
Moshe. 2022. A second wave of ud hebrew treebank-
ing and cross-domain parsing.

--- Page 6 ---

A
Appendix: Example Code & Usage of DictaBERT-seg
Output:

--- Page 7 ---

B
Appendix: Example Code & Usage of DictaBERT-morph
Output:

--- Page 8 ---


--- Page 9 ---


--- Page 10 ---

C
Appendix: Example Code & Usage of DictaBERT-heq
Output:

```
