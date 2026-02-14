---
title: "2022-Bhattacharjee-BanglaBERT Language Model Pretraining and Benchmarks for Low-Resource - PDF Extract"
source_pdf: "2022-Bhattacharjee-BanglaBERT Language Model Pretraining and Benchmarks for Low-Resource.pdf"
pages: 10
extracted_at: "2026-02-13T10:43:50.301899"
---

# PDF Extract: 2022-Bhattacharjee-BanglaBERT Language Model Pretraining and Benchmarks for Low-Resource

**Source PDF:** 2022-Bhattacharjee-BanglaBERT Language Model Pretraining and Benchmarks for Low-Resource.pdf
**Total Pages:** 10

---

## Content

```
--- Page 1 ---

BanglaBERT: Language Model Pretraining and Benchmarks for
Low-Resource Language Understanding Evaluation in Bangla
Abhik Bhattacharjee1∗, Tahmid Hasan1∗, Wasi Uddin Ahmad2†, Kazi Samin1,
Md Saiful Islam3, Anindya Iqbal1, M. Sohel Rahman1, Rifat Shahriyar1
Bangladesh University of Engineering and Technology (BUET)1,
AWS AI Labs2, University of Rochester3
abhik@ra.cse.buet.ac.bd, {tahmidhasan,rifat}@cse.buet.ac.bd
Abstract
In this work, we introduce BanglaBERT, a
BERT-based Natural Language Understand-
ing (NLU) model pretrained in Bangla, a
widely spoken yet low-resource language in
the NLP literature. To pretrain BanglaBERT,
we collect 27.5 GB of Bangla pretraining data
(dubbed ‘Bangla2B+’) by crawling 110 pop-
ular Bangla sites.
We introduce two down-
stream task datasets on natural language in-
ference and question answering and bench-
mark on four diverse NLU tasks covering
text classiﬁcation, sequence labeling, and span
prediction.
In the process, we bring them
under the ﬁrst-ever Bangla Language Under-
standing Benchmark (BLUB). BanglaBERT
achieves state-of-the-art results outperforming
multilingual and monolingual models.
We
are making the models, datasets, and a leader-
board publicly available at https://github.
com/csebuetnlp/banglabert to advance
Bangla NLP.
1
Introduction
Despite being the sixth most spoken language in
the world with over 300 million native speakers
constituting 4% of the world’s total population,1
Bangla is considered a resource-scarce language.
Joshi et al. (2020b) categorized Bangla in the lan-
guage group that lacks efforts in labeled data col-
lection and relies on self-supervised pretraining
(Devlin et al., 2019; Radford et al., 2019; Liu et al.,
2019) to boost the natural language understanding
(NLU) task performances. To date, the Bangla lan-
guage has been continuing to rely on ﬁne-tuning
multilingual pretrained language models (PLMs)
(Ashraﬁet al., 2020; Das et al., 2021; Islam et al.,
2021). However, since multilingual PLMs cover
a wide range of languages (Conneau and Lample,
2019; Conneau et al., 2020), they are large (have
∗These authors contributed equally to this work.
†Work done while at UCLA.
1https://w.wiki/Psq
hundreds of millions of parameters) and require
substantial computational resources for ﬁne-tuning.
They also tend to show degraded performance for
low-resource languages (Wu and Dredze, 2020) on
downstream NLU tasks. Motivated by the triumph
of language-speciﬁc models (Martin et al. (2020);
Polignano et al. (2019); Canete et al. (2020); An-
toun et al. (2020), inter alia) over multilingual
models in many other languages, in this work,
we present BanglaBERT – a BERT-based (Devlin
et al., 2019) Bangla NLU model pretrained on 27.5
GB data (which we name ‘Bangla2B+’) we metic-
ulously crawled 110 popular Bangla websites to fa-
cilitate NLU applications in Bangla. Since most of
the downstream task datasets for NLP applications
are in the English language, to facilitate zero-shot
transfer learning between English and Bangla, we
additionally pretrain a model in both languages; we
name the model BanglishBERT.
We also introduce two datasets on Bangla Natu-
ral Language Inference (NLI) and Question An-
swering (QA), tasks previously unexplored in
Bangla, and evaluate both pretrained models on
four diverse downstream tasks on sentiment clas-
siﬁcation, NLI, named entity recognition, and QA.
We bring these tasks together to establish the ﬁrst-
ever Bangla Language Understanding Benchmark
(BLUB). We compare widely used multilingual
models to BanglaBERT using BLUB and ﬁnd that
both models excel on all the tasks.
We summarize our contributions as follows:
1. We present two new pretrained models:
BanglaBERT and BanglishBERT, and intro-
duce new Bangla NLI and QA datasets.
2. We introduce the Bangla Language Under-
standing Benchmark (BLUB) and show that,
in the supervised setting, BanglaBERT outper-
forms mBERT and XLM-R (base) by 6.8 and
4.3 BLUB scores, while in zero-shot cross-
lingual transfer, BanglishBERT outperforms
them by 15.8 and 10.8, respectively.
arXiv:2101.00204v4  [cs.CL]  10 May 2022

--- Page 2 ---

3. We provide the code, models, and a leader-
board to spur future research on Bangla NLU.
2
BanglaBERT
2.1
Pretraining Data
A high volume of good quality text data is a prereq-
uisite for pretraining large language models. For
instance, BERT (Devlin et al., 2019) is pretrained
on the English Wikipedia and the Books corpus
(Zhu et al., 2015) containing 3.3 billion tokens.
Subsequent works like RoBERTa (Liu et al., 2019)
and XLNet (Yang et al., 2019) used more extensive
web-crawled data with heavy ﬁltering and cleaning.
Bangla is a rather resource-constrained language
in the web domain; for example, the Bangla
Wikipedia dump from July 2021 is only 650 MB,
two orders of magnitudes smaller than the English
Wikipedia. As a result, we had to crawl the web
extensively to collect our pretraining data. We se-
lected 110 Bangla websites by their Amazon Alexa
rankings2 and the volume and quality of extractable
texts by inspecting each website. The contents in-
cluded encyclopedias, news, blogs, e-books, sto-
ries, social media/forums, etc.3 The amount of data
totaled around 35 GB.
There are noisy sources of Bangla data dumps, a
couple of prominent ones being OSCAR (Suárez
et al., 2019) and CCNet (Wenzek et al., 2020). They
contained many offensive texts; we found them
infeasible to clean thoroughly. Fearing their po-
tentially harmful impacts (Luccioni and Viviano,
2021), we opted not to use them. We further dis-
cuss ethical considerations at the end of the paper.
2.2
Pre-processing
We performed thorough deduplication on the pre-
training data, removed non-textual contents (e.g.,
HTML/JavaScript tags), and ﬁltered out non-
Bangla pages using a language classiﬁer (Joulin
et al., 2017). After the processing, the dataset was
reduced to 27.5 GB in size containing 5.25M docu-
ments having 306.66 words on average.
We trained a Wordpiece (Wu et al., 2016) vo-
cabulary of 32k subword tokens on the resulting
corpus with a 400 character alphabet, kept larger
than the native Bangla alphabet to capture code-
switching (Poplack, 1980) and allow romanized
Bangla contents for better generalization. We lim-
ited the length of a training sample to 512 tokens
2www.alexa.com/topsites/countries/BD
3The complete list can be found in the Appendix.
and did not cross document boundaries (Liu et al.,
2019) while creating a data point. After tokeniza-
tion, we had 7.18M samples with an average length
of 304.14 tokens and containing 2.18B tokens in
total; hence we named the dataset ‘Bangla2B+’.
2.3
Pretraining Objective
Self-supervised pretraining objectives leverage un-
labeled data. For example, BERT (Devlin et al.,
2019) was pretrained with masked language mod-
eling (MLM) and next sentence prediction (NSP).
Several works built on top of this, e.g., RoBERTa
(Liu et al., 2019) removed NSP and pretrained with
longer sequences, SpanBERT (Joshi et al., 2020a)
masked contiguous spans of tokens, while works
like XLNet (Yang et al., 2019) introduced objec-
tives like factorized language modeling.
We pretrained BanglaBERT using ELECTRA
(Clark et al., 2020b), pretrained with the Replaced
Token Detection (RTD) objective, where a gener-
ator and a discriminator model are trained jointly.
The generator is fed as input a sequence with a
portion of the tokens masked (15% in our case)
and is asked to predict them using the rest of the
input (i.e., standard MLM). The masked tokens
are then replaced by tokens sampled from the gen-
erator’s output distribution for the corresponding
masks, and the discriminator then has to predict
whether each token is from the original sequence
or not. After pretraining, the discriminator is used
for ﬁne-tuning. Clark et al. (2020b) argued that
RTD back-propagates loss from all tokens of a se-
quence, in contrast to 15% tokens of the MLM ob-
jective, giving the model more signals to learn from.
Evidently, ELECTRA achieves comparable down-
stream performance to RoBERTa or XLNet with
only a quarter of their training time. This compu-
tational efﬁciency motivated us to use ELECTRA
for our implementation of BanglaBERT.
2.4
Model Architecture & Hyperparameters
We pretrained the base ELECTRA model (a 12-
layer Transformer encoder with 768 embedding
size, 768 hidden size, 12 attention heads, 3072
feed-forward size, generator-to-discriminator ratio
1
3, 110M parameters) with 256 batch size for 2.5M
steps on a v3-8 TPU instance on GCP. We used
the Adam (Kingma and Ba, 2015) optimizer with a
2e-4 learning rate and linear warmup of 10k steps.

--- Page 3 ---

Task
Corpus
|Train| |Dev| |Test| Metric
Domain
Sentiment Classiﬁcation
SentNoB
12,575 1,567 1,567 Macro-F1 Social Media
Natural Language Inference BNLI
381,449 2,419 4,895 Accuracy
Miscellaneous
Named Entity Recognition
MultiCoNER
14,500
800
800 Micro-F1
Miscellaneous
Question Answering
BQA, TyDiQA 127,771 2,502 2,504 EM/F1
Wikipedia
Table 1: Statistics of the Bangla Language Understanding Evaluation (BLUB) benchmark.
2.5
BanglishBERT
Often labeled data in a low-resource language for a
task may not be available but be abundant in high-
resource languages like English. In these scenar-
ios, zero-shot cross-lingual transfer (Artetxe and
Schwenk, 2019) provides an effective way to be
still able to train a multilingual model on that task
using the high-resource languages and be able to
transfer to low-resource ones. To this end, we pre-
trained a bilingual model, named BanglishBERT,
on Bangla and English together using the same set
of hyperparameters mentioned earlier. We used the
BERT pretraining corpus as the English data and
trained a joint bilingual vocabulary (each language
having ∼16k tokens). We upsampled the Bangla
data during training to equal the participation of
both languages.
3
The Bangla Language Understanding
Benchmark (BLUB)
Many works have studied different Bangla NLU
tasks in isolation, e.g., sentiment classiﬁcation
(Das and Bandyopadhyay, 2010; Sharfuddin et al.,
2018; Tripto and Ali, 2018), semantic textual simi-
larity (Shajalal and Aono, 2018), parts-of-speech
(PoS) tagging (Alam et al., 2016), named entity
recognition (NER) (Ashraﬁet al., 2020). How-
ever, Bangla NLU has not yet had a comprehen-
sive, uniﬁed study. Motivated by the surge of NLU
research brought about by benchmarks in other lan-
guages, e.g., English (Wang et al., 2018), French
(Le et al., 2020), Korean (Park et al., 2021), we
establish the ﬁrst-ever Bangla Language Under-
standing Benchmark (BLUB). NLU generally com-
prises three types of tasks: text classiﬁcation, se-
quence labeling, and text span prediction. Text
classiﬁcation tasks can further be sub-divided into
single-sequence and sequence-pair classiﬁcation.
Therefore, we consider a total of four tasks for
BLUB. For each task type, we carefully select one
downstream task dataset. We emphasize the quality
and open availability of the datasets while making
the selection. We brieﬂy mention them below.
1.
Single-Sequence Classiﬁcation
Sentiment
classiﬁcation is perhaps the most-studied Bangla
NLU task, with some of the earlier works dat-
ing back over a decade (Das and Bandyopadhyay,
2010). Hence, we chose this as the single-sequence
classiﬁcation task. However, most Bangla senti-
ment classiﬁcation datasets are not publicly avail-
able. We could only ﬁnd two public datasets: BYSA
(Tripto and Ali, 2018) and SentNoB (Islam et al.,
2021). We found BYSA to have many duplications.
Even worse, many duplicates had different labels.
SentNoB had better quality and covered a broader
set of domains, making the classiﬁcation task more
challenging. Hence, we opted to use the latter.
2. Sequence-pair Classiﬁcation
In contrast to
single-sequence classiﬁcation, there has been a
dearth of sequence-pair classiﬁcation works in
Bangla. We found work on semantic textual simi-
larity (Shajalal and Aono, 2018), but the dataset is
not publicly available. As such, we curated a new
Bangla Natural Language Inference (BNLI) dataset
for sequence-pair classiﬁcation. We chose NLI as
the representative task due to its fundamental im-
portance in NLU. Given two sentences, a premise
and a hypothesis as input, a model is tasked to pre-
dict whether or not the hypothesis is entailment,
contradiction, or neutral to the premise. We used
the same curation procedure as the XNLI (Conneau
et al., 2018) dataset: we translated the MultiNLI
(Williams et al., 2018) training data using the En-
glish to Bangla translation model by Hasan et al.
(2020) and had the evaluation sets translated by
expert human translators.4 Due to the possibility of
the incursion of errors during automatic translation,
we used the Language-Agnostic BERT Sentence
Embeddings (LaBSE) (Feng et al., 2020) of the
translations and original sentences to compute their
similarity and discarded all sentences below a simi-
larity threshold of 0.70. Moreover, to ensure good-
quality human translation, we used similar quality
assurance strategies as Guzmán et al. (2019).
4More details are presented in the ethical considerations
section.

--- Page 4 ---

Models
|Params.|
SC
NLI
NER
QA
BLUB Score
Zero-shot cross-lingual transfer
mBERT
180M
27.05
62.22
39.27
59.01/64.18
50.35
XLM-R (base)
270M
42.03
72.18
45.37
55.03/61.83
55.29
XLM-R (large)
550M
49.49
78.13
56.48
71.13/77.70
66.59
BanglishBERT
110M
48.39
75.26
55.56
72.87/78.63
66.14
Supervised ﬁne-tuning
mBERT
180M
67.59
75.13
68.97
67.12/72.64
70.29
XLM-R (base)
270M
69.54
78.46
73.32
68.09/74.27
72.82
XLM-R (large)
550M
70.97
82.40
78.39
73.15/79.06
76.79
IndicBERT
18M
68.41
77.11
54.13
50.84/57.47
61.59
sahajBERT
18M
71.12
76.92
70.94
65.48/70.69
71.03
BanglishBERT
110M
70.61
80.95
76.28
72.43/78.40
75.73
BanglaBERT
110M
72.89
82.80
77.78
72.63/79.34
77.09
Table 2: Performance comparison of pretrained models on different downstream tasks. Scores in bold texts have
statistically signiﬁcant (p < 0.05) difference from others with bootstrap sampling (Koehn, 2004).
3. Sequence Labeling
In this task, all words of
a text sequence have to be classiﬁed. Named En-
tity Recognition (NER) and Parts-of-Speech (PoS)
tagging are two of the most prominent sequence
labeling tasks. We chose the Bangla portion of Se-
mEval 2022 MultiCoNER (Malmasi et al., 2022)
dataset for BLUB.
4. Span Prediction
Extractive question answer-
ing is a standard choice for text span predic-
tion. Similar to BNLI, we machine-translated the
SQuAD 2.0 (Rajpurkar et al., 2018) dataset and
used it as the training set (BQA). For validation
and test, We used the Bangla portion of the Ty-
DiQA5 (Clark et al., 2020a) dataset. We posed the
task analogous to SQuAD 2.0: presented with a
text passage and a question, a model has to pre-
dict whether or not it is answerable. If answerable,
the model has to ﬁnd the minimal text span that
answers the question.
We present detailed statistics of the BLUB
benchmark in Table 1.
4
Experiments & Results
Setup
We ﬁne-tuned BanglaBERT and Banglish-
BERT on the four downstream tasks and compared
them with several multilingual models: mBERT
(Devlin et al., 2019), XLM-R base and large (Con-
neau et al., 2020), and IndicBERT (Kakwani et al.,
2020), a multilingual model for Indian languages;
and sahajBERT (Diskin et al., 2021), an ALBERT-
based (Lan et al., 2020) PLM for Bangla. All pre-
5We removed the Yes/No questions from TyDiQA and sub-
sampled the unanswerable questions to have equal proportion.
trained models were ﬁne-tuned for 3-20 epochs
with batch size 32, and the learning rate was tuned
from {2e-5, 3e-5, 4e-5, 5e-5}. The ﬁnal models
were selected based on the validation performances
after each epoch. We performed ﬁne-tuning with
three random seeds and reported their average
scores in Table 2. We reported the average per-
formance of all tasks as the BLUB score.
Zero-shot Transfer
We show the zero-shot
cross-lingual transfer results of the multilingual
models ﬁne-tuned on the English counterpart of
each dataset (SentNob has no English equivalent;
hence we used the Stanford Sentiment Treebank
(Socher et al., 2013) for the sentiment classiﬁca-
tion task) in Table 2. In zero-shot transfer set-
ting, BanglishBERT achieves strong cross-lingual
performance over similar-sized models and falls
marginally short of XLM-R (large). This is an ex-
pected outcome since cross-lingual effectiveness
depends explicitly on model size (K et al., 2020).
Supervised Fine-tuning
In the supervised ﬁne-
tuning setup, BanglaBERT outperformed multilin-
gual models and monolingual sahajBERT on all
the tasks, achieving a BLUB score of 77.09, even
coming head-to-head with XLM-R (large). On the
other hand, BanglishBERT marginally lags behind
BanglaBERT and XLM-R (large). BanglaBERT is
not only superior in performance but also substan-
tially compute- and memory-efﬁcient. For instance,
it may seem that sahajBERT is more efﬁcient than
BanglaBERT due to its smaller size, but it takes
2-3.5x time and 2.4-3.33x memory as BanglaBERT

--- Page 5 ---

to ﬁne-tune. 6
100
500
1000
5000
Full Data
35
45
55
65
75
BanglaBERT
XLM-R(Large)
Sentiment Classification
Training Samples
Macro-F1 (%)
0.1k
1k
10k
100k
Full Data
30
40
50
60
70
80
BanglaBERT
XLM-R(Large)
Natural Language Inference
Training Samples
Accuracy (%)
Figure 1: Sample-efﬁciency tests with SC and NLI.
Sample efﬁciency
It is often challenging to an-
notate training samples in real-world scenarios, es-
pecially for low-resource languages like Bangla.
So, in addition to compute- and memory-efﬁciency,
sample-efﬁciency (Howard and Ruder, 2018) is an-
other necessity of PLMs. To assess the sample
efﬁciency of BanglaBERT, we limit the number of
training samples and see how it fares against other
models. We compare it with XLM-R (large) and
plot their performances on the SC and NLI tasks7
for different sample size in Figure 1.
Results show that when we have fewer number
of samples (≤1k), BanglaBERT has substantially
better performance (2-9% on SC and 6-10% on
NLI with p < 0.05) over XLM-R (large), making
it more practically applicable for resource-scarce
downstream tasks.
5
Conclusion & Future Works
Creating language-speciﬁc models is often infea-
sible for low-resource languages lacking ample
data. Hence, researchers are compelled to use mul-
tilingual models for languages that do not have
6We present a detailed comparison in the Appendix.
7Results for the other tasks can be found in the Appendix.
strong pretrained models.
To this end, we in-
troduced BanglaBERT and BanglishBERT, two
NLU models in Bangla, a widely spoken yet low-
resource language. We presented new downstream
datasets on NLI and QA, and established the BLUB
benchmark, setting new state-of-the-art results with
BanglaBERT. In future, we will include other
Bangla NLU benchmarks (e.g., dependency pars-
ing (de Marneffe et al., 2021)) in BLUB and in-
vestigate the beneﬁts of initializing Bangla NLG
models from BanglaBERT.
Acknowledgements
We would like to thank the Research and Innovation
Centre for Science and Engineering (RISE), BUET,
for funding the project, and Intelligent Machines
Limited and Google TensorFlow Research Cloud
(TRC) Program for providing cloud support.
Ethical Considerations
Dataset and Model Release
The Copy Right
Act, 20008 of Bangladesh allows reproduction and
public release of copy-right materials for non-
commercial research purposes. As a transformative
research work, we will release BanglaBERT un-
der a non-commercial license. Furthermore, we
will release only the pretraining data for which we
know the distribution will not cause any copyright
infringement. The downstream task datasets can
all be made publicly available under a similar non-
commercial license.
Quality Control in Human Translation
Trans-
lations were done by expert translators who provide
translation services for renowned Bangla newspa-
pers. Each translated sentence was further assessed
for quality by another expert. If found to be of low
quality, it was again translated by the original trans-
lator. The sample was then discarded altogether if
found to be of low quality again. Fewer than 100
samples were discarded in this process. Translators
were paid as per standard rates in local currencies.
Text Content
We tried to minimize offensive
texts in the pretraining data by explicitly crawl-
ing the sites where such contents would be nom-
inal. However, we cannot guarantee that there is
absolutely no objectionable content present and
therefore recommend using the model carefully,
especially for text generation purposes.
8http://bdlaws.minlaw.gov.bd/
act-details-846.html

--- Page 6 ---

References
Firoj Alam, Shammur Absar Chowdhury, and Sheak
Rashed Haider Noori. 2016. Bidirectional LSTMs
- CRFs networks for bangla POS tagging. In 2016
19th International Conference on Computer and
Information Technology (ICCIT), pages 377–382.
IEEE.
Wissam Antoun, Fady Baly, and Hazem Hajj. 2020.
AraBERT: Transformer-based model for Arabic lan-
guage understanding.
In Proceedings of the 4th
Workshop on Open-Source Arabic Corpora and Pro-
cessing Tools, with a Shared Task on Offensive Lan-
guage Detection, pages 9–15, Marseille, France. Eu-
ropean Language Resource Association.
Mikel Artetxe and Holger Schwenk. 2019.
Mas-
sively multilingual sentence embeddings for zero-
shot cross-lingual transfer and beyond.
Transac-
tions of the Association for Computational Linguis-
tics, 7:597–610.
I. Ashraﬁ, M. Mohammad, A. S. Mauree, G. M. A.
Nijhum, R. Karim, N. Mohammed, and S. Mo-
men. 2020. Banner: A cost-sensitive contextualized
model for bangla named entity recognition. IEEE
Access, 8:58206–58226.
José Canete, Gabriel Chaperon, Rodrigo Fuentes, and
Jorge Pérez. 2020. Spanish pre-trained BERT model
and evaluation data. In Proceedings of the Practi-
cal ML for Developing Countries Workshop at ICLR
2020, PML4DC.
Jonathan H. Clark, Eunsol Choi, Michael Collins, Dan
Garrette, Tom Kwiatkowski, Vitaly Nikolaev, and
Jennimaria Palomaki. 2020a. TyDi QA: A bench-
mark for information-seeking question answering in
typologically diverse languages. Transactions of the
Association for Computational Linguistics, 8:454–
470.
Kevin Clark, Minh-Thang Luong, Quoc V Le, and
Christopher D Manning. 2020b.
ELECTRA: pre-
training text encoders as discriminators rather than
generators.
In 8th International Conference on
Learning Representations, ICLR 2020, April, 2020,
Online.
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
Alexis Conneau and Guillaume Lample. 2019. Cross-
lingual language model pretraining. In Advances in
Neural Information Processing Systems, volume 32,
pages 7059–7069. Curran Associates, Inc.
Alexis Conneau, Ruty Rinott, Guillaume Lample, Ad-
ina Williams, Samuel Bowman, Holger Schwenk,
and Veselin Stoyanov. 2018.
XNLI: Evaluating
cross-lingual sentence representations. In Proceed-
ings of the 2018 Conference on Empirical Methods
in Natural Language Processing, pages 2475–2485,
Brussels, Belgium. Association for Computational
Linguistics.
Amitava Das and Sivaji Bandyopadhyay. 2010. Phrase-
level polarity identiﬁcation for bangla. Int. J. Com-
put. Linguist. Appl.(IJCLA), 1(1-2):169–182.
Avishek Das,
Omar Sharif,
Mohammed Moshiul
Hoque, and Iqbal H. Sarker. 2021.
Emotion clas-
siﬁcation in a resource constrained language using
transformer-based approach. In Proceedings of the
2021 Conference of the North American Chapter of
the Association for Computational Linguistics: Stu-
dent Research Workshop, pages 150–158, Online.
Association for Computational Linguistics.
Marie-Catherine de Marneffe, Christopher D. Man-
ning, Joakim Nivre, and Daniel Zeman. 2021. Uni-
versal Dependencies.
Computational Linguistics,
47(2):255–308.
Jacob Devlin, Ming-Wei Chang, Kenton Lee, and
Kristina Toutanova. 2019.
BERT: Pre-training of
deep bidirectional transformers for language under-
standing.
In Proceedings of the 2019 Conference
of the North American Chapter of the Association
for Computational Linguistics: Human Language
Technologies, Volume 1 (Long and Short Papers),
pages 4171–4186, Minneapolis, Minnesota. Associ-
ation for Computational Linguistics.
Michael Diskin, Alexey Bukhtiyarov, Max Ryabinin,
Lucile Saulnier, Quentin Lhoest, Anton Sinitsin,
Dmitry Popov, Dmitry Pyrkin, Maxim Kashirin,
Alexander Borzunov, Albert Villanova del Moral,
Denis Mazur, Ilia Kobelev, Yacine Jernite, Thomas
Wolf, and Gennady Pekhimenko. 2021.
Dis-
tributed
deep
learning
in
open
collaborations.
arXiv:2106.10207.
Fangxiaoyu
Feng,
Yinfei
Yang,
Daniel
Cer,
Naveen
Arivazhagan,
and
Wei
Wang.
2020.
Language-agnostic
bert
sentence
embedding.
arXiv:2007.01852.
Francisco Guzmán, Peng-Jen Chen, Myle Ott, Juan
Pino, Guillaume Lample, Philipp Koehn, Vishrav
Chaudhary, and Marc’Aurelio Ranzato. 2019. The
FLORES evaluation datasets for low-resource ma-
chine translation:
Nepali–English and Sinhala–
English. In Proceedings of the 2019 Conference on
Empirical Methods in Natural Language Processing
and the 9th International Joint Conference on Natu-
ral Language Processing (EMNLP-IJCNLP), pages
6098–6111, Hong Kong, China. Association for
Computational Linguistics.
Tahmid Hasan, Abhik Bhattacharjee, Kazi Samin, Ma-
sum Hasan, Madhusudan Basak, M. Sohel Rahman,

--- Page 7 ---

and Rifat Shahriyar. 2020.
Not low-resource any-
more: Aligner ensembling, batch ﬁltering, and new
datasets for Bengali-English machine translation. In
Proceedings of the 2020 Conference on Empirical
Methods in Natural Language Processing (EMNLP),
pages 2612–2623, Online. Association for Computa-
tional Linguistics.
Jeremy Howard and Sebastian Ruder. 2018. Universal
language model ﬁne-tuning for text classiﬁcation. In
Proceedings of the 56th Annual Meeting of the As-
sociation for Computational Linguistics (Volume 1:
Long Papers), pages 328–339, Melbourne, Australia.
Association for Computational Linguistics.
Khondoker Ittehadul Islam, Sudipta Kar, Md Saiful Is-
lam, and Mohammad Ruhul Amin. 2021. SentNoB:
A dataset for analysing sentiment on noisy Bangla
texts. In Findings of the Association for Computa-
tional Linguistics: EMNLP 2021, pages 3265–3271,
Punta Cana, Dominican Republic. Association for
Computational Linguistics.
Mandar Joshi, Danqi Chen, Yinhan Liu, Daniel S.
Weld, Luke Zettlemoyer, and Omer Levy. 2020a.
SpanBERT: Improving pre-training by representing
and predicting spans. Transactions of the Associa-
tion for Computational Linguistics, 8:64–77.
Pratik Joshi, Sebastin Santy, Amar Budhiraja, Kalika
Bali, and Monojit Choudhury. 2020b. The state and
fate of linguistic diversity and inclusion in the NLP
world.
In Proceedings of the 58th Annual Meet-
ing of the Association for Computational Linguistics,
pages 6282–6293, Online. Association for Computa-
tional Linguistics.
Armand Joulin, Edouard Grave, Piotr Bojanowski, and
Tomas Mikolov. 2017.
Bag of tricks for efﬁcient
text classiﬁcation. In Proceedings of the 15th Con-
ference of the European Chapter of the Association
for Computational Linguistics: Volume 2, Short Pa-
pers, pages 427–431, Valencia, Spain. Association
for Computational Linguistics.
Karthikeyan K, Zihan Wang, Stephen Mayhew, and
Dan Roth. 2020.
Cross-lingual ability of multi-
lingual bert:
An empirical study.
In 8th Inter-
national Conference on Learning Representations,
ICLR 2020, April, 2020, Online.
Divyanshu Kakwani, Anoop Kunchukuttan, Satish
Golla, Gokul N.C., Avik Bhattacharyya, Mitesh M.
Khapra, and Pratyush Kumar. 2020. IndicNLPSuite:
Monolingual corpora, evaluation benchmarks and
pre-trained multilingual language models for Indian
languages. In Findings of the Association for Com-
putational Linguistics: EMNLP 2020, pages 4948–
4961, Online. Association for Computational Lin-
guistics.
Diederik P. Kingma and Jimmy Ba. 2015. Adam: A
method for stochastic optimization.
In 3rd Inter-
national Conference on Learning Representations,
ICLR 2015, San Diego, CA, USA, May 7-9, 2015.
Philipp Koehn. 2004.
Statistical signiﬁcance tests
for machine translation evaluation.
In Proceed-
ings of the 2004 Conference on Empirical Meth-
ods in Natural Language Processing, pages 388–
395, Barcelona, Spain. Association for Computa-
tional Linguistics.
Zhenzhong Lan, Mingda Chen, Sebastian Goodman,
Kevin Gimpel, Piyush Sharma, and Radu Sori-
cut. 2020.
Albert: A lite bert for self-supervised
learning of language representations. In 8th Inter-
national Conference on Learning Representations,
ICLR 2020, April, 2020, Online.
Hang Le, Loïc Vial, Jibril Frej, Vincent Segonne, Max-
imin Coavoux, Benjamin Lecouteux, Alexandre Al-
lauzen, Benoît Crabbé, Laurent Besacier, and Didier
Schwab. 2020.
Flaubert: Unsupervised language
model pre-training for french.
In Proceedings of
The 12th Language Resources and Evaluation Con-
ference, pages 2479–2490, Marseille, France. Euro-
pean Language Resources Association.
Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Man-
dar Joshi, Danqi Chen, Omer Levy, Mike Lewis,
Luke Zettlemoyer, and Veselin Stoyanov. 2019.
Roberta: A robustly optimized bert pretraining ap-
proach. arXiv:1907.11692.
Alexandra Luccioni and Joseph Viviano. 2021. What’s
in the box? an analysis of undesirable content in
the Common Crawl corpus. In Proceedings of the
59th Annual Meeting of the Association for Compu-
tational Linguistics and the 11th International Joint
Conference on Natural Language Processing (Vol-
ume 2: Short Papers), pages 182–189, Online. As-
sociation for Computational Linguistics.
Shervin Malmasi, Anjie Fang, Besnik Fetahu, Sudipta
Kar, and Oleg Rokhlenko. 2022.
MultiCoNER:
a Large-scale Multilingual dataset for Complex
Named Entity Recognition.
Louis Martin, Benjamin Muller, Pedro Javier Or-
tiz Suárez, Yoann Dupont, Laurent Romary, Éric
de la Clergerie, Djamé Seddah, and Benoît Sagot.
2020. CamemBERT: a tasty French language model.
In Proceedings of the 58th Annual Meeting of the
Association for Computational Linguistics, pages
7203–7219, Online. Association for Computational
Linguistics.
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

--- Page 8 ---

Marco Polignano, Pierpaolo Basile, Marco de Gemmis,
Giovanni Semeraro, and Valerio Basile. 2019. Al-
berto: Italian BERT language understanding model
for NLP challenging tasks based on tweets. In Pro-
ceedings of the Sixth Italian Conference on Com-
putational Linguistics, Bari, Italy, November 13-15,
2019, CEUR Workshop Proceedings.
Shana Poplack. 1980. Sometimes I’ll start a sentence
in Spanish Y TERMINO EN ESPAÑOL: toward
a typology of code-switching.
Linguistics, 18(7-
8):581–618.
Alec Radford, Jeffrey Wu, Rewon Child, David Luan,
Dario Amodei, and Ilya Sutskever. 2019. Language
models are unsupervised multitask learners. OpenAI
blog, 1(8).
Pranav Rajpurkar, Robin Jia, and Percy Liang. 2018.
Know what you don’t know: Unanswerable ques-
tions for SQuAD. In Proceedings of the 56th An-
nual Meeting of the Association for Computational
Linguistics (Volume 2: Short Papers), pages 784–
789, Melbourne, Australia. Association for Compu-
tational Linguistics.
Md Shajalal and Masaki Aono. 2018. Semantic tex-
tual similarity in Bengali text. In 2018 International
Conference on Bangla Speech and Language Pro-
cessing (ICBSLP), pages 1–5. IEEE.
Abdullah Aziz Sharfuddin, Md Naﬁs Tihami, and
Md Saiful Islam. 2018.
A deep recurrent neural
network with bilstm model for sentiment classiﬁca-
tion. In 2018 International Conference on Bangla
Speech and Language Processing (ICBSLP), pages
1–4. IEEE.
Richard Socher, Alex Perelygin, Jean Wu, Jason
Chuang, Christopher D. Manning, Andrew Ng, and
Christopher Potts. 2013.
Recursive deep models
for semantic compositionality over a sentiment tree-
bank.
In Proceedings of the 2013 Conference on
Empirical Methods in Natural Language Processing,
pages 1631–1642, Seattle, Washington, USA. Asso-
ciation for Computational Linguistics.
Pedro Javier Ortiz Suárez, Benoît Sagot, and Laurent
Romary. 2019. Asynchronous Pipeline for Process-
ing Huge Corpora on Medium to Low Resource In-
frastructures.
In 7th Workshop on the Challenges
in the Management of Large Corpora (CMLC-
7), Cardiff, United Kingdom. Leibniz-Institut für
Deutsche Sprache.
Naﬁs Irtiza Tripto and Mohammed Eunus Ali. 2018.
Detecting multilabel sentiment and emotions from
bangla youtube comments.
In 2018 International
Conference on Bangla Speech and Language Pro-
cessing (ICBSLP), pages 1–6. IEEE.
Alex Wang, Amanpreet Singh, Julian Michael, Fe-
lix Hill, Omer Levy, and Samuel Bowman. 2018.
GLUE: A multi-task benchmark and analysis plat-
form for natural language understanding.
In Pro-
ceedings of the 2018 EMNLP Workshop Black-
boxNLP: Analyzing and Interpreting Neural Net-
works for NLP, pages 353–355, Brussels, Belgium.
Association for Computational Linguistics.
Guillaume Wenzek, Marie-Anne Lachaux, Alexis Con-
neau, Vishrav Chaudhary, Francisco Guzmán, Ar-
mand Joulin, and Edouard Grave. 2020.
CCNet:
Extracting high quality monolingual datasets from
web crawl data.
In Proceedings of the 12th Lan-
guage Resources and Evaluation Conference, pages
4003–4012, Marseille, France. European Language
Resources Association.
Adina Williams, Nikita Nangia, and Samuel Bowman.
2018. A broad-coverage challenge corpus for sen-
tence understanding through inference. In Proceed-
ings of the 2018 Conference of the North American
Chapter of the Association for Computational Lin-
guistics: Human Language Technologies, Volume
1 (Long Papers), pages 1112–1122, New Orleans,
Louisiana. Association for Computational Linguis-
tics.
Shijie Wu and Mark Dredze. 2020. Are all languages
created equal in multilingual BERT? In Proceedings
of the 5th Workshop on Representation Learning for
NLP, pages 120–130, Online. Association for Com-
putational Linguistics.
Yonghui Wu, Mike Schuster, Zhifeng Chen, Quoc V
Le,
Mohammad Norouzi,
Wolfgang Macherey,
Maxim Krikun,
Yuan Cao,
Qin Gao,
Klaus
Macherey, et al. 2016.
Google’s neural machine
translation system: Bridging the gap between human
and machine translation. arXiv:1609.08144.
Zhilin Yang, Zihang Dai, Yiming Yang, Jaime Car-
bonell, Russ R Salakhutdinov, and Quoc V Le. 2019.
Xlnet: Generalized autoregressive pretraining for
language understanding.
In Advances in Neural
Information Processing Systems, volume 32, pages
5753–5763. Curran Associates, Inc.
Yukun Zhu, Ryan Kiros, Rich Zemel, Ruslan Salakhut-
dinov, Raquel Urtasun, Antonio Torralba, and Sanja
Fidler. 2015. Aligning books and movies: Towards
story-like visual explanations by watching movies
and reading books.
In Proceedings of the 2015
IEEE International Conference on Computer Vision
(ICCV), ICCV ’15, page 19–27, USA. IEEE Com-
puter Society.

--- Page 9 ---

Appendix
Pretraining Data Sources
We used the following sites for data collection. We
categorize the sites into six types:
Encyclopedia:
• bn.banglapedia.org
• bn.wikipedia.org
• songramernotebook.com
News:
• anandabazar.com
• arthoniteerkagoj.com
• bangla.24livenewspaper.com
• bangla.bdnews24.com
• bangla.dhakatribune.com
• bangla.hindustantimes.com
• bangladesherkhela.com
• banglanews24.com
• banglatribune.com
• bbc.com
• bd-journal.com
• bd-pratidin.com
• bd24live.com
• bengali.indianexpress.com
• bigganprojukti.com
• bonikbarta.net
• chakarianews.com
• channelionline.com
• ctgtimes.com
• ctn24.com
• daily-bangladesh.com
• dailyagnishikha.com
• dainikazadi.net
• dainikdinkal.net
• dailyfulki.com
• dailyinqilab.com
• dailynayadiganta.com
• dailysangram.com
• dailysylhet.com
• dainikamadershomoy.com
• dainikshiksha.com
• dhakardak-bd.com
• dmpnews.org
• dw.com
• eisamay.indiatimes.com
• ittefaq.com.bd
• jagonews24.com
• jugantor.com
• kalerkantho.com
• manobkantha.com.bd
• mzamin.com
• ntvbd.com
• onnodristy.com
• pavilion.com.bd
• prothomalo.com
• protidinersangbad.com
• risingbd.com
• rtvonline.com
• samakal.com
• sangbadpratidin.in
• somoyerkonthosor.com
• somoynews.tv
• tbsnews.net
• teknafnews.com
• thedailystar.net
• voabangla.com
• zeenews.india.com
• zoombangla.com
Blogs:
• amrabondhu.com
• banglablog.in
• bigganblog.org
• biggani.org
• bigyan.org.in
• bishorgo.com
• cadetcollegeblog.com
• choturmatrik.com
• horoppa.wordpress.com
• muktangon.blog
• roar.media/bangla
• sachalayatan.com
• shodalap.org
• shopnobaz.net
• somewhereinblog.net
• subeen.com
• tunerpage.com
• tutobd.com
E-books/Stories:
• banglaepub.github.io
• bengali.pratilipi.com
• bn.wikisource.org
• ebanglalibrary.com
• eboipotro.github.io
• golpokobita.com
• kaliokalam.com
• shirisherdalpala.net
• tagoreweb.in
Social Media/Forums:
• banglacricket.com
• bn.globalvoices.org
• helpfulhub.com
• nirbik.com
• pchelplinebd.com
• techtunes.io

--- Page 10 ---

Miscellaneous:
• banglasonglyric.com
• bdlaws.minlaw.gov.bd
• bdup24.com
• bengalisongslyrics.com
• dakghar.org
• gdn8.com
• gunijan.org.bd
• hrw.org
• jakir.me
• jhankarmahbub.com
• jw.org
• lyricsbangla.com
• neonaloy.com
• porjotonlipi.com
• sasthabangla.com
• tanzil.net
We wrote custom crawlers for each site above
(except the Wikipedia dumps).
Additional Sample Efﬁciency Tests
We plot the the sample efﬁciency results of the
NER and QA tasks in Figure 2.
100
500
1000
5000
Full Data
0
20
40
60
80
BanglaBERT
XLM-R(Large)
Named Entity Recognition
Training Samples
Micro-F1 (%)
100
500
1000
2000
Full Data
50
60
70
80
90
BanglaBERT
XLM-R(Large)
Question Answering
Training Samples
F1 (%)
Figure 2: Sample-efﬁciency tests with NER and QA.
Similar results are also observed here for the
NER task, where BanglaBERT is more sample-
efﬁcient when we have ≤1k training samples. In
the QA task however, both models have identical
performance for all sample counts.
Compute and Memory Efﬁciency Tests
To validate that BanglaBERT is more efﬁcient in
terms of memory and compute, we measured each
model’s training time and memory usage during
the ﬁne-tuning of each task. All tests were done
on a desktop machine with an 8-core Intel Core-i7
11700k CPU and NVIDIA RTX 3090 GPU. We
used the same batch size, gradient accumulation
steps, and sequence length for all models and tasks
for a fair comparison. We use relative time and
memory (GPU VRAM) usage considering those
of BanglaBERT as units. The results are shown in
Table 3. (We mention the upper and lower values
of the different tasks for each model)
Model
Time
Memory Usage
mBERT
1.14x-1.92x
1.12x-2.04x
XLM-R (base)
1.29-1.81x
1.04-1.63x
XLM-R (large)
3.81-4.49x
4.44-5.55x
SahajBERT
2.40-3.33x
2.07-3.54x
BanglaBERT
1.00x
1.00x
Table 3: Compute and memory efﬁciency tests

```
