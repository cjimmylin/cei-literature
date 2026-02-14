---
title: "2021-Jiang-Pre-trained Models and Evaluation Data for - PDF Extract"
source_pdf: "2021-Jiang-Pre-trained Models and Evaluation Data for.pdf"
pages: 9
extracted_at: "2026-02-14T01:57:23.142008"
---

# PDF Extract: 2021-Jiang-Pre-trained Models and Evaluation Data for

**Source PDF:** 2021-Jiang-Pre-trained Models and Evaluation Data for.pdf
**Total Pages:** 9

---

## Content

```
--- Page 1 ---

arXiv:2308.02976v1  [cs.CL]  6 Aug 2023
Accepted as a workshop paper at PML4DC, ICLR 2020
SPANISH PRE-TRAINED BERT MODEL
AND EVALUATION DATA
Jos´e Ca˜nete∗, Gabriel Chaperon, Rodrigo Fuentes
Department of Computer Science, Universidad de Chile
{jcanete,gchapero,rfuentes}@dcc.uchile.cl
Jou-Hui Ho, Hojin Kang
Department of Electrical Engineering, Universidad de Chile
{jouhui.ho,ho.kang.k}@ug.uchile.cl
Jorge P´erez
Department of Computer Science, Universidad de Chile &
Millennium Institute for Foundational Research on Data (IMFD), Chile
jperez@dcc.uchile.cl
ABSTRACT
The Spanish language is one of the top 5 spoken languages in the world. Never-
theless, ﬁnding resources to train or evaluate Spanish language models is not an
easy task. In this paper we help bridge this gap by presenting a BERT-based lan-
guage model pre-trained exclusively on Spanish data. As a second contribution,
we also compiled several tasks speciﬁcally for the Spanish language in a single
repository much in the spirit of the GLUE benchmark. By ﬁne-tuning our pre-
trained Spanish model, we obtain better results compared to other BERT-based
models pre-trained on multilingual corpora for most of the tasks, even achieving
a new state-of-the-art on some of them. We have publicly released our model, the
pre-training data, and the compilation of the Spanish benchmarks.
1
INTRODUCTION
The ﬁeld of natural language processing (NLP) has made incredible progress in the last two years.
Two of the most decisive features that have driven this improvement are the self-attention mecha-
nism, particularly the Transformer architecture (Vaswani et al., 2017), and the introduction of un-
supervised pre-training methods (Peters et al., 2018; Howard & Ruder, 2018; Devlin et al., 2018),
which take advantage of huge amounts of unlabeled text corpora. Thus the leading strategy to-
day for achieving good performance is to ﬁrst train a Transformer-based model, say M, with a
general language-modeling task over a huge unlabeled corpus and then, after this ﬁrst training is
over, “ﬁne-tune” M by continuing to train it for a speciﬁc task using labeled data. Built upon
these ideas, the BERT architecture –which stands for “Bidirectional Encoder Representations from
Transformers”– (Devlin et al., 2018), and several improvements thereof (Liu et al., 2019; Lan et al.,
2019; Yang et al., 2019b; Clark et al., 2019), changed the landscape of NLP in 2019.
BERT was initially released in two versions, one pre-trained on an English corpus and an-
other on a Chinese corpus (Devlin et al., 2018).
As a way of providing a resource for other
languages besides English and Chinese, the authors also released a “multilingual” version of
BERT (we’ll refer to it as mBERT from now on) pre-trained simultaneously on a corpus in-
cluding more than 100 different languages.
The mBERT model has shown impressive per-
formance when ﬁne-tuned for language-speciﬁc tasks and has achieved state-of-the-art results
in many cross-lingual benchmarks (Wu & Dredze, 2019; Pires et al., 2019).
The good perfor-
mance of mBERT has drawn the attention of many different NLP communities, and efforts have
been made to produce BERT versions trained on monolingual data. This has led to the release
∗Work partially performed while at Adereso.
1

--- Page 2 ---

Accepted as a workshop paper at PML4DC, ICLR 2020
of BERT models in Russian (Kuratov & Arkhipov, 2019), French (Martin et al., 2019; Le et al.,
2019), Dutch (de Vries et al., 2019; Delobelle et al., 2020), Italian (Polignano et al., 2019), and Por-
tugese (Souza et al., 2019).
In this paper we present the ﬁrst BERT model pre-trained for the Spanish language. Despite Span-
ish being widely spoken (much more than the previously mentioned languages), ﬁnding resources
to train or evaluate Spanish language models is not an easy task. For this reason, we also com-
piled several Spanish-speciﬁc tasks in a single repository, much in the spirit of the GLUE bench-
mark (Wang et al., 2019). By ﬁne-tuning our pre-trained Spanish model, we obtain better results
compared to other BERT-based models that were pre-trained on multilingual corpora for most of the
tasks, and we even achieve a new state-of-the-art on some of them. We have released our pre-trained
model, the training corpus, and the compilation of benchmarks as free resources to be used by the
Spanish NLP community.1
In the rest of this paper, we ﬁrst present our Spanish-BERT model. Then, we describe the tasks
that we have compiled into a benchmark that we call GLUES (GLUE for Spanish), and ﬁnally, we
present the results obtained by our model in some of the GLUES tasks. Before going into the details
of our model and results, we will brieﬂy review the related work.
2
RELATED WORK
Pre-trained language models using deep neural networks became very popular starting with ULM-
Fit (Howard & Ruder, 2018). ULMFit is based on a standard recurrent neural network architecture
and a language-modeling task (predicting the next token from the previous sequence of tokens). By
using vast amounts of text, ULMFit is ﬁrst trained for the language-modelingtask, aiming to help the
model acquire general knowledge from a big corpus. The model is then ﬁne-tuned in a supervised
way to solve a speciﬁc task using labeled data. The empirical results showed that the combination
of pre-training and ﬁne-tuning can considerably outperform training a model from scratch for the
same supervised task.
A similar pre-training strategy was later used by Devlin et al. (2018) to propose the BERT
model.
Compared with ULMFit, in BERT, the recurrent architecture is replaced with self-
attention (Vaswani et al., 2017), which allows the prediction of a token to depend on every other
token in the same sequence. The task used for pre-training BERT, called masked language modeling,
is based on corrupting an input sequence by arbitrarily deleting some of the tokens and then training
the model to reconstruct the original sequence (Devlin et al., 2018). Several variations of BERT in
terms of the training method and the task used for pre-training have been proposed (Liu et al., 2019;
Joshi et al., 2019; Yang et al., 2019b). There have also been efforts to make models more efﬁcient in
terms of the number of parameters or training time (Sanh et al., 2019; Lan et al., 2019; Clark et al.,
2019).
Wu & Dredze (2019) and Pires et al. (2019) studied Multilingual BERT models, that is, models pre-
trained simultaneously on corpora from different languages. These works showed how a single
model can learn from several languages, setting strong baselines for tasks involving non-English
languages. XLM (Lample & Conneau, 2019) introduced a supervised objective which involved par-
allel multilingual data, and XLM-RoBERTa (Conneau et al., 2019) brought the multilingual models
to the big leagues in terms of model size.
Several single-language BERT models came with results that usually got better perfor-
mance than multilingual models as it is the case with CamemBERT (Martin et al., 2019)
and
FlauBERT
(Le et al.,
2019)
for
French,
BERTje
(de Vries et al.,
2019)
and
Rob-
BERT (Delobelle et al., 2020) for Dutch, FinBERT (Virtanen et al., 2019) for Finish, to name a few.
Our work is similar to these models, but for the Spanish language. To the best of our knowledge,
our paper presents the ﬁrst publicly available Spanish BERT model and evaluation.
1https://github.com/dccuchile/beto
2

--- Page 3 ---

Accepted as a workshop paper at PML4DC, ICLR 2020
3
SPANISH-BERT MODEL, DATA AND TRAINING
We trained a model similar in size to a BERT-Base model (Devlin et al., 2018). Our model has 12
self-attention layers, with 12 attention-heads each (Vaswani et al., 2017), using a hidden size of 768.
In total, our model has 110M parameters. We trained two versions: one with cased data and one
with uncased data, using a dataset that we will describe next.
For training our model, we collected text from different sources. We used all the data from Wikipedia
and all the sources of the OPUS Project (Tiedemann, 2012) that had text in Spanish. These sources
include United Nations and Government journals, TED Talks, Subtitles, News Stories, and more.
The total size of the corpora gathered was comparable to the corpora used in the original BERT. Our
training corpus contains about 3 billion words, and we have released it for later use.2. Our corpus
can be considered an updated version of the one compiled by Cardellino (2016).
For both versions of our model, cased and uncased, we constructed a vocabulary of 31K subwords
using the byte pair encoding algorithm provided by the SentencePiece library (Kudo & Richardson,
2018). We added 1K placeholder tokens for later use, which gave us a vocabulary of 32K tokens.
For training our BERT models, we considered certain training details that have been successful in
RoBERTa (Liu et al., 2019). In particular, we integrated the Dynamic Masking technique into our
training, which involves using different masks for the same sentence in our corpus. The Dynamic
Masking we used was 10x, meaning that every sentence had 10 different masks. We also consid-
ered the Whole-Word Masking (WWM) technique from the updated version of BERT (Devlin et al.,
2018). WWM ensures that when masking a speciﬁc token, if the token corresponds to a sub-word in
a sentence, then all contiguous tokens conforming the same word are also masked. Additionally, we
trained on larger batches compared to the original BERT (but smaller than RoBERTa). We trained
each model (cased and uncased) for 2M steps, with learning rate of 0.0001, and the ﬁrst 10000 steps
as warm-up. The training was also divided into two phases, as described by You et al. (2019): we
trained the ﬁrst 900k steps with a batch size of 2048 and maximum sequence length of 128, and the
rest of the training with batch size of 256 and maximum sequence length of 512. All the pre-training
was done using Google’s preemptible TPU v3-8.
4
GLUES
In this section, we present the GLUES benchmark, which is a compilation of common NLP tasks
in the Spanish language, following the idea of the original English GLUE benchmark (Wang et al.,
2019). Through this benchmarks, we hope to help standardize future Spanish NLP efforts3. Next,
we describe the tasks that we currently consider in GLUES.
Natural Language Inference: XNLI
The Multi-Genre Natural Language Inference (MNLI)
dataset (Williams et al., 2017) consists of pair of sentences. The ﬁrst sentence is called the premise,
and the second is the hypothesis. The task is to predict whether the premise entails the hypothesis
(entailment), contradicts it (contradiction), or neither entails nor contradicts it (neutral). In other
words, the task is a 3-class classiﬁcation. The Cross-Lingual Natural Language Inference (XNLI)
corpus (Conneau et al., 2018) is an evaluation dataset that extends the MNLI by adding development
and test sets for 15 languages. In this setup, we train using the Spanish machine translation of the
MNLI dataset, and use the development and test sets from the XNLI corpus. This task is evaluated
using simple accuracy.
Paraphrasing: PAWS-X
PAWS-X (Yang et al., 2019a) is the multilingual version of the PAWS
dataset (Zhang et al., 2019). The task consists of determining whether two sentences are semanti-
cally equivalent or not. The dataset provides standard (translated) train, development and test sets,
and we used the Spanish portion. It is evaluated using simple accuracy.
Named Entity Recognition: CoNLL
Named Entity Recognition consists of determining phrases
in a sentence that contain the names of persons, organizations, locations, times, and quantities.
2https://github.com/josecannete/spanish-corpora
3See https://github.com/dccuchile/glues for a detailed description on how to obtain train-
dev-test data for each task.
3

--- Page 4 ---

Accepted as a workshop paper at PML4DC, ICLR 2020
For this task, we use the dataset by Tjong Kim Sang (2002), which focuses on persons, organi-
zations, and locations, with a fourth category of miscellaneous entities, all tagged using the BIO
format (Ramshaw & Marcus, 1999). This dataset provides standard train, development, and test
sets, and the performance is measured with an F1 score.
Part-of-Speech Tagging: Universal Dependencies v1.4
A part of speech (POS) is a category of
words with similar grammatical properties, such as noun, verb, adjective, preposition, and con-
junction. For the POS tagging task, we use the Spanish subset of the Universal Dependencies
(v1.4) Treebank (Nivre et al., 2016). The version of the dataset was chosen following the works
of Wu & Dredze (2019) and Kim et al. (2017). The dataset provides standard train, development,
and test sets. This task is evaluated based on the F1 score of predicted POS tags.
Document Classiﬁcation: MLDoc
The MLDoc dataset (Schwenk & Li, 2018) is a balanced sub-
set of the Reuters corpus. This task consists of classifying the documents into four categories,
CCAT (Corporate/Industrial), ECAT (Economics), GCAT (Government/Social), and MCAT (Mar-
kets). This dataset provides multiple sizes for the train split (1k, 2k, 5k and 10k), along with standard
development and test sets for eight languages. We chose to train using the largest available train split
in Spanish. This task is evaluated using simple accuracy.
Dependency Parsing: Universal Dependencies v2.2
A dependency tree represents the grammat-
ical structure of a sentence, deﬁning relationships in the form of labeled-edges from “dependent” to
“head” words. The label of each edge represents the type of relationship. The task of dependency
parsing consists of constructing a dependency tree for a given sentence. For this task, we use a
subset of the Universal Dependencies v2.2 Treebank (Nivre et al., 2018), in particular, the concate-
nation of the AnCora and GSD Spanish portions of the dataset. This decision and the version we
chose follow the work of Ahmad et al. (2019). The task is evaluated using the Unlabeled Attachment
Score (UAS) and Labeled Attachment Score (LAS) (K¨ubler et al., 2009). UAS is the percentage of
words that have been assigned the correct head, while LAS is the percentage of words that have been
assigned both the correct head and the correct label for the relationship.
Question Answering: MLQA, TAR and XQuAD
Given a context and a question, the task of
question answering (QA) consists of ﬁnding the sequence of contiguous words within the context
that answers the question. This task is usually evaluated using two metrics averaged across all
questions: exact match, that corresponds to the percentage of answers that match exactly, and F1
score, where answers are treated as bags of words. For our benchmark, we consider three trans-
lated versions of the SQuAD v1.1 dataset (Rajpurkar et al., 2016), namely, MLQA (Lewis et al.,
2019), XQuAD (Artetxe et al., 2019), and TAR (Carrino et al., 2019), which we will explain next.
MLQA provides translations for seven language with train data produced using machine transla-
tion from English, and development and test data translated by professionals (Lewis et al., 2019).
XQuAD provides test sets to evaluate cross-lingual models in 11 languages (Artetxe et al., 2019).
Carrino et al. (2019) proposed the TAR method (Translate Align Retrieve) that can be used to pro-
duce automatically machine translated versions of QA datasets. They provided a TAR-translation
from English to Spanish of SQuAD v1.1 (Carrino et al., 2019). In our benchmark, we consider the
train sets in MLQA and TAR, and the test sets in MLQA and XQuAD.
5
EVALUATION
5.1
FINE-TUNING
Since one of the goals of our work was to compare the performance of Spanish-BERT to
mBERT (Wu & Dredze, 2019; Yang et al., 2019a), our experimental setup closely follows the one
by Wu & Dredze (2019). Task speciﬁc output layers are incorporated, following the original BERT
work (Devlin et al., 2018).
For each task, no preprocessing is performed except tokenization from words into subwords
using the learned vocabulary and WordPiece (Wu et al., 2016).
We use the Adam opti-
mizer (Kingma & Ba, 2014) for ﬁne-tuning with standard parameters (β1 = 0.9, β2 = 0.999),
4

--- Page 5 ---

Accepted as a workshop paper at PML4DC, ICLR 2020
Model
XNLI
PAWS-X
NER
POS
MLDoc
Best mBERT
78.50a
89.00b
87.38a
97.10a
95.70a
es-BERT uncased
80.15
89.55
82.67
98.44
96.12∗
es-BERT cased
82.01
89.05
88.43
98.97∗
95.60
Table 1: Comparison of Spanish BERT (es-BERT) with the best results obtained by multilingual
BERT models where the ﬁne tune was done only on the Spanish train data in every dataset. Super-
script denotes results obtained by: (a) Wu & Dredze (2019) and (b) Yang et al. (2019a). The “∗”
indicates a new state-of-the-art resut in the respective Spanish benchmark.
Model
MLQA, MLQA
TAR, XQuAD
TAR, MLQA
Best mBERT
53.90 / 37.40c
77.60 / 61.80d
68.10 / 48.30d
es-BERT uncased
67.85 / 46.03
77.52 / 55.46
68.04 / 45.00
es-BERT cased
68.01 / 45.88
77.56 / 57.06
69.15 / 45.63
Table 2: Comparison of Spanish BERT (es-BERT) with the best results obtained by multilingual
BERT models in Question Answering. We only consider models where the ﬁne tune was done on
the Spanish train data in every dataset. Results are presented as F1 / ExactMatch. Every column
header denotes the train set (left) and test set (right) used in everry case. Different superscript denotes
results obtained by different authors: (c) Lewis et al. (2019) and (d) Carrino et al. (2019)
and L2 weight decay of 0.01. We warm up the learning rate for the ﬁrst 10% of steps, with a linear
decay afterward.
To allow for ﬁne-tuning on a single GPU, we limit the length of each sentence to 128 tokens for
all tasks. To accommodate tasks that require word-level classiﬁcation, we use the sliding window
approach described by Wu & Dredze (2019). After the ﬁrst window, the last 64 tokens are kept for
the next window, and only 64 new tokens are fed into the model.
For hyperparameter selection, we run experiments using different combinations of batch size, learn-
ing rate and number of epochs, following the values recommended by Devlin et al. (2018): batch
size {16, 32}; learning rate {5e-5, 3e-5, 2e-5}; number of epochs {2, 3, 4}. An extensive hyperpa-
rameter search is left for future work.
5.2
RESULTS
Tables 1 and 2 show our results compared to the best mBERT result reported in the literature for the
same setting. Spanish BERT outperforms most of the mBERT results, except for some QA settings
(Table 2). One of the largest difference can be seen in the XNLI task, which is the task that has
the largest training dataset in Spanish. We note that for two of the most standard Spanish datasets
(POS and MLDoc) we obtained a new state of the art. We also note that there are some important
differences in the performances in the QA datasets. The low quality of machine translation in MLQA
might be one possible reason. We observed that nearly half of the 81K examples in MLQA have a
mismatch between the answer and its starting position in the context.
It is important to note that our models are Spanish-only and thus cannot take advantage neither of
the original English train set in every translated benchmark, nor from train data in other languages.
Taking advantage of data in different languages is a capability that multilingual models have by
design. In fact, there has been recent work on large multilingual models that can achieve better
results on the Spanish datasets when ﬁne-tuned with general, not necessarily Spanish, data. This is
the case with the XLM-RoBERTa model (Conneau et al., 2019), which, with 560M parameters and
consuming training data from different languages, obtained results of 85.6% for XNLI and 89% for
NER in the Spanish test set. Both results are better than the one that we obtained by ﬁne-tuning with
Spanish data only (Table 1). Similarly, Yang et al. (2019a) obtained 90.7% in the Spanish test-set of
PAWS-X when ﬁne-tuning mBERT including the original English train set.
5

--- Page 6 ---

Accepted as a workshop paper at PML4DC, ICLR 2020
6
CONCLUSION
The advent of Transformer-based pre-trained language models has greatly improved the accessibility
of high-performing models for the average user. In this paper, we successfully pre-train a Spanish-
only model and open-source it, along with the training corpus and evaluation benchmarks, for the
community to use.
The ease of use of a pre-trained NLP model implies that its use cases are much broader, given that
practitioners from disciplines other than computer science could ﬁne-tune them for their domain-
speciﬁc downstream tasks. By releasing our Spanish-BERT model, we hope to encourage research
and the application of deep learning techniques in Spanish-speaking countries.
Another direction of the work is to improve Spanish NLP models in terms of size, memory, and
computation requirements. We are currently working on pre-training different ALBERT models
(Lan et al., 2019) for Spanish, with number of parameters ranging from 5M to 223M. Our initial
results with the smaller models are encouraging, and we plan to release these models as well.
ACKNOWLEDGMENTS
We thank Adereso4 for kindly providing support for training our uncased model, and Google for
helping us with the Cloud TPU program for research. This work was partially funded by the Mil-
lennium Institute for Foundational Research on Data.
REFERENCES
Wasi Ahmad, Zhisong Zhang, Xuezhe Ma, Eduard Hovy, Kai-Wei Chang, and Nanyun Peng. On dif-
ﬁculties of cross-lingual transfer with order differences: A case study on dependency parsing. In
Proceedings of the 2019 Conference of the North American Chapter of the Association for Com-
putational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers), pp.
2440–2452, Minneapolis, Minnesota, June 2019. Association for Computational Linguistics. doi:
10.18653/v1/N19-1253. URL https://www.aclweb.org/anthology/N19-1253.
Mikel Artetxe, Sebastian Ruder, and Dani Yogatama. On the cross-lingual transferability of mono-
lingual representations. arXiv preprint arXiv:1910.11856, 2019.
Cristian Cardellino.
Spanish Billion Words Corpus and Embeddings, March 2016.
URL
https://crscardellino.github.io/SBWCE/.
Casimiro Pio Carrino, Marta R Costa-juss`a, and Jos´e AR Fonollosa. Automatic spanish translation
of the squad dataset for multilingual question answering. arXiv preprint arXiv:1912.05200, 2019.
Kevin Clark, Minh-Thang Luong, Quoc V Le, and Christopher D Manning. Electra: Pre-training
text encoders as discriminators rather than generators. In International Conference on Learning
Representations, 2019.
Alexis Conneau, Guillaume Lample, Ruty Rinott, Adina Williams, Samuel R Bowman, Holger
Schwenk, and Veselin Stoyanov. Xnli: Evaluating cross-lingual sentence representations. arXiv
preprint arXiv:1809.05053, 2018.
Alexis Conneau, Kartikay Khandelwal, Naman Goyal, Vishrav Chaudhary, Guillaume Wenzek,
Francisco Guzm´an, Edouard Grave, Myle Ott, Luke Zettlemoyer, and Veselin Stoyanov. Un-
supervised cross-lingual representation learning at scale. arXiv preprint arXiv:1911.02116, 2019.
Wietse de Vries, Andreas van Cranenburgh, Arianna Bisazza, Tommaso Caselli, Gertjan van Noord,
and Malvina Nissim. Bertje: A dutch bert model. arXiv preprint arXiv:1912.09582, 2019.
Pieter Delobelle, Thomas Winters, and Bettina Berendt. Robbert: a dutch roberta-based language
model. arXiv preprint arXiv:2001.06286, 2020.
Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. Bert: Pre-training of deep
bidirectional transformers for language understanding. arXiv preprint arXiv:1810.04805, 2018.
4https://www.adere.so/
6

--- Page 7 ---

Accepted as a workshop paper at PML4DC, ICLR 2020
Jeremy Howard and Sebastian Ruder. Universal language model ﬁne-tuning for text classiﬁcation.
arXiv preprint arXiv:1801.06146, 2018.
Mandar Joshi, Danqi Chen, Yinhan Liu, Daniel S Weld, Luke Zettlemoyer, and Omer Levy.
Spanbert:
Improving pre-training by representing and predicting spans.
arXiv preprint
arXiv:1907.10529, 2019.
Joo-Kyung Kim, Young-Bum Kim, Ruhi Sarikaya, and Eric Fosler-Lussier. Cross-lingual transfer
learning for POS tagging without cross-lingual resources. In Proceedings of the 2017 Conference
on Empirical Methods in Natural Language Processing, pp. 2832–2838, Copenhagen, Denmark,
September 2017. Association for Computational Linguistics. doi: 10.18653/v1/D17-1302. URL
https://www.aclweb.org/anthology/D17-1302.
Diederik P Kingma and Jimmy Ba. Adam: A method for stochastic optimization. arXiv preprint
arXiv:1412.6980, 2014.
Sandra K¨ubler, Ryan McDonald, and Joakim Nivre. Dependency parsing. Synthesis lectures on
human language technologies, 1(1):1–127, 2009.
Taku Kudo and John Richardson. Sentencepiece: A simple and language independent subword
tokenizer and detokenizer for neural text processing. arXiv preprint arXiv:1808.06226, 2018.
Yuri Kuratov and Mikhail Arkhipov. Adaptation of deep bidirectional multilingual transformers for
russian language. arXiv preprint arXiv:1905.07213, 2019.
Guillaume Lample and Alexis Conneau. Cross-lingual language model pretraining. arXiv preprint
arXiv:1901.07291, 2019.
Zhenzhong Lan, Mingda Chen, Sebastian Goodman, Kevin Gimpel, Piyush Sharma, and Radu Sori-
cut. Albert: A lite bert for self-supervised learning of language representations. arXiv preprint
arXiv:1909.11942, 2019.
Hang Le, Lo¨ıc Vial, Jibril Frej, Vincent Segonne, Maximin Coavoux, Benjamin Lecouteux, Alexan-
dre Allauzen, Benoˆıt Crabb´e, Laurent Besacier, and Didier Schwab. Flaubert: Unsupervised
language model pre-training for french. arXiv preprint arXiv:1912.05372, 2019.
Patrick Lewis, Barlas O˘guz, Ruty Rinott, Sebastian Riedel, and Holger Schwenk. Mlqa: Evaluating
cross-lingual extractive question answering. arXiv preprint arXiv:1910.07475, 2019.
Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Mandar Joshi, Danqi Chen, Omer Levy, Mike
Lewis, Luke Zettlemoyer, and Veselin Stoyanov. Roberta: A robustly optimized bert pretraining
approach. arXiv preprint arXiv:1907.11692, 2019.
Louis Martin, Benjamin Muller, Pedro Javier Ortiz Su´arez, Yoann Dupont, Laurent Romary,
´Eric Villemonte de la Clergerie, Djam´e Seddah, and Benoˆıt Sagot. Camembert: a tasty french
language model. arXiv preprint arXiv:1911.03894, 2019.
Joakim Nivre, Marie-Catherine De Marneffe, Filip Ginter, Yoav Goldberg, Jan Hajic, Christopher D
Manning, Ryan McDonald, Slav Petrov, Sampo Pyysalo, Natalia Silveira, et al. Universal de-
pendencies v1: A multilingual treebank collection. In Proceedings of the Tenth International
Conference on Language Resources and Evaluation (LREC’16), pp. 1659–1666, 2016.
Joakim Nivre, Mitchell Abrams, ˇZeljko Agi´c, Lars Ahrenberg, Lene Antonsen, Maria Jesus Aran-
zabe, Gashaw Arutie, Masayuki Asahara, Luma Ateyah, Mohammed Attia, et al. Universal de-
pendencies 2.2. 2018.
Matthew E. Peters, Mark Neumann, Mohit Iyyer, Matt Gardner, Christopher Clark, Kenton Lee, and
Luke Zettlemoyer. Deep contextualized word representations. preprint arXiv 1802.05365, 2018.
Telmo Pires, Eva Schlinger, and Dan Garrette. How multilingual is multilingual bert?
CoRR,
abs/1906.01502, 2019. URL http://arxiv.org/abs/1906.01502.
7

--- Page 8 ---

Accepted as a workshop paper at PML4DC, ICLR 2020
Marco Polignano,
Pierpaolo Basile,
Marco de Gemmis,
Giovanni Semeraro,
and Va-
lerio
Basile.
AlBERTo:
Italian
BERT
Language Understanding Model
for
NLP
Challenging Tasks Based on Tweets.
In Proceedings of the Sixth Italian Confer-
ence on Computational Linguistics (CLiC-it 2019), volume 2481. CEUR, 2019.
URL
https://www.scopus.com/inward/record.uri?eid=2-s2.0-85074851349&partnerID=40&md5=7a
Pranav Rajpurkar, Jian Zhang, Konstantin Lopyrev, and Percy Liang. Squad: 100,000+ questions
for machine comprehension of text. arXiv preprint arXiv:1606.05250, 2016.
Lance A Ramshaw and Mitchell P Marcus. Text chunking using transformation-based learning. In
Natural language processing using very large corpora, pp. 157–176. Springer, 1999.
Victor Sanh, Lysandre Debut, Julien Chaumond, and Thomas Wolf. Distilbert, a distilled version of
bert: smaller, faster, cheaper and lighter. arXiv preprint arXiv:1910.01108, 2019.
Holger Schwenk and Xian Li. A corpus for multilingual document classiﬁcation in eight languages.
In Nicoletta Calzolari (Conference chair), Khalid Choukri, Christopher Cieri, Thierry Declerck,
Sara Goggi, Koiti Hasida, Hitoshi Isahara, Bente Maegaard, Joseph Mariani, H´el`ene Mazo, Asun-
cion Moreno, Jan Odijk, Stelios Piperidis, and Takenobu Tokunaga (eds.), Proceedings of the
Eleventh International Conference on Language Resources and Evaluation (LREC 2018), Paris,
France, may 2018. European Language Resources Association (ELRA). ISBN 979-10-95546-00-
9.
F´abio Souza, Rodrigo Nogueira, and Roberto Lotufo. Portuguese named entity recognition using
bert-crf. arXiv preprint arXiv:1909.10649, 2019.
J¨org Tiedemann. Parallel data, tools and interfaces in opus. In Lrec, volume 2012, pp. 2214–2218,
2012.
Erik F. Tjong Kim Sang. Introduction to the CoNLL-2002 shared task: Language-independent
named entity recognition. In COLING-02: The 6th Conference on Natural Language Learning
2002 (CoNLL-2002), 2002. URL https://www.aclweb.org/anthology/W02-2024.
Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N Gomez,
Łukasz Kaiser, and Illia Polosukhin. Attention is all you need. In Advances in neural information
processing systems, pp. 5998–6008, 2017.
Antti Virtanen, Jenna Kanerva, Rami Ilo, Jouni Luoma, Juhani Luotolahti, Tapio Salakoski, Filip
Ginter, and Sampo Pyysalo.
Multilingual is not enough: Bert for ﬁnnish.
arXiv preprint
arXiv:1912.07076, 2019.
Alex Wang, Amanpreet Singh, Julian Michael, Felix Hill, Omer Levy, and Samuel R. Bowman.
GLUE: A multi-task benchmark and analysis platform for natural language understanding. 2019.
In the Proceedings of ICLR.
Adina Williams, Nikita Nangia, and Samuel R Bowman. A broad-coverage challenge corpus for
sentence understanding through inference. arXiv preprint arXiv:1704.05426, 2017.
Shijie Wu and Mark Dredze. Beto, bentz, becas: The surprising cross-lingual effectiveness of bert.
arXiv preprint arXiv:1904.09077, 2019.
Yonghui Wu, Mike Schuster, Zhifeng Chen, Quoc V Le, Mohammad Norouzi, Wolfgang Macherey,
Maxim Krikun, Yuan Cao, Qin Gao, Klaus Macherey, et al. Google’s neural machine trans-
lation system: Bridging the gap between human and machine translation.
arXiv preprint
arXiv:1609.08144, 2016.
Yinfei Yang, Yuan Zhang, Chris Tar, and Jason Baldridge. Paws-x: A cross-lingual adversarial
dataset for paraphrase identiﬁcation. arXiv preprint arXiv:1908.11828, 2019a.
Zhilin Yang, Zihang Dai, Yiming Yang, Jaime Carbonell, Russ R Salakhutdinov, and Quoc V Le.
Xlnet: Generalized autoregressive pretraining for language understanding. In Advances in neural
information processing systems, pp. 5754–5764, 2019b.
8

--- Page 9 ---

Accepted as a workshop paper at PML4DC, ICLR 2020
Yang You, Jing Li, Sashank Reddi, Jonathan Hseu, Sanjiv Kumar, Srinadh Bhojanapalli, Xiaodan
Song, James Demmel, Kurt Keutzer, and Cho-Jui Hsieh.
Large batch optimization for deep
learning: Training bert in 76 minutes. In International Conference on Learning Representations,
2019.
Yuan Zhang, Jason Baldridge, and Luheng He. Paws: Paraphrase adversaries from word scrambling.
arXiv preprint arXiv:1904.01130, 2019.
9

```
