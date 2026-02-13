---
title: "2024-retrieved-PeLLE Encoder-based Language Models for Brazilian Portuguese Based on - PDF Extract"
source_pdf: "2024-retrieved-PeLLE Encoder-based Language Models for Brazilian Portuguese Based on.pdf"
pages: 15
extracted_at: "2026-02-13T09:50:31.220708"
---

# PDF Extract: 2024-retrieved-PeLLE Encoder-based Language Models for Brazilian Portuguese Based on

**Source PDF:** 2024-retrieved-PeLLE Encoder-based Language Models for Brazilian Portuguese Based on.pdf
**Total Pages:** 15

---

## Content

```
--- Page 1 ---

PeLLE: Encoder-based language models for
Brazilian Portuguese based on open data
Guilherme Mello, Marcelo Finger, Felipe Serras, Miguel de Mello Carpi, Marcos Jose
University of São Paulo
Paulo Cavalin
Pedro Henrique Domingues
IBM Research
IBM Research, PUC-Rio
March 1, 2024
Abstract
In this paper we present PeLLE, a family of large language models based
on the RoBERTa architecture, for Brazilian Portuguese, trained on curated,
open data from the Carolina corpus. Aiming at reproducible results, we de-
scribe details of the pretraining of the models. We also evaluate PeLLE
models against a set of existing multilingual and PT-BR refined pretrained
Transformer-based LLM encoders, contrasting performance of large versus
smaller-but-curated pretrained models in several downstream tasks. We con-
clude that several tasks perform better with larger models, but some tasks
benefit from smaller-but-curated data in its pretraining.
1
Introduction
We introduce PeLLE, a family of Brazilian Portuguese Large Language Encoder,
and examine different ways of Large Language Model pretraining. We evaluate its
performance in downstream NLP tasks for Brazilian Portuguese (BP). The goal of
this work is to produce and evaluate BP-specific versions of a Transformer-encoded
language model (Vaswani et al., 2017) based on the RoBERTa architecture (Liu
et al., 2019), in a reproducible way. We investigate whether language-specific train-
ing is preferable to extending multilingual models, such as mBert (Devlin et al.,
2018) and XLM-R (Conneau et al., 2020) with training over the same open corpus.
The use of an open corpus ensures reproducible comparisons, and for that we
choose Carolina Corpus (Crespo et al., 2023), an open general corpus of Brazilian
1
arXiv:2402.19204v1  [cs.CL]  29 Feb 2024

--- Page 2 ---

Portuguese. Furthermore, Corpus Carolina is a highly curated corpus, as far as
very large corpora can be curated, which also allows us to contrast the employment
of quality data versus non-curated big data.
Model evaluation is performed over nontrivial NLP tasks for Portuguese which
still challenge existing technology, such as natural language inference, hate speech
identification and classification. We also add to the comparison several baseline
models derived from existing BP LLM-encoders, such as Bertimbau (Souza et al.,
2020) and Albertina-PTBR (Rodrigues et al., 2023), and generic multilingual ones,
such as mBERT (Devlin et al., 2018) and XLM-R (Conneau et al., 2020).
All our pretrained models will be made publicly available on Huggingface.
2
Related work
Large Language Models (LLMs) have emerged in the past few years as an effec-
tive way to improve Neural Network (NN)-based models for Natural Language
Processing (NLP)-based applications (Devlin et al., 2018; Brown et al., 2020).
The main idea consists of pretraining a NN on a large set of data relying on
self-supervised training objectives. That is, based on Auto-Regressive or Masked
Language Modeling (MLM) training objectives. A commonly-used approach in
current days is to first pretrain a Transformer NN on a large and generic set of un-
labeled data, and then finetune its parameters to a more specific and smaller dataset
with labeled data. We usually refer to those datasets as pretraining data and down-
stream data (Raffel et al., 2020). It is worth adding that LLMs can be based on
different types of Transformer-based architectures, such as those relying on a full
Encoder-Decoder architecture (Raffel et al., 2020), or those based on either En-
coder (Devlin et al., 2018) or Decoder (Brown et al., 2020) sides. In this work we
focus specifically on Encoder-based LLMs.
It is well known that English is the language with most abundant data in our
current day’s digital world, and one can easily scrape a lot of data from the web to
pretrain very large models (Joshi et al., 2020). For this reason, it is natural that most
recent efforts in LLMs were targeted at English at first, and other less-resourced
languages have a much smaller coverage of the LLM advances. Taking Portuguese
as an example, since is the target language of this work, we can observe that it is
included in some multilingual models (Devlin et al., 2018; Xue et al., 2021), and
there are some specific efforts in building Portuguese-only models (Souza et al.,
2020; Rodrigues et al., 2023).
Among the Portuguese specific models, the main difference is usually the pre-
training data. Besides the fact that the pretraining data can impact the performance
of the model on downstream data, it is also very important to understand the li-
2

--- Page 3 ---

censes of the documents that were used to compose that dataset. One corpus that is
commonly used is BrWaC (Wagner Filho et al., 2018), which contains web pages
crawled with the help of a web search engine. Although it is common belief that
publicly-available content can be freely used without asking for permission, that is
not true. Each web page has specific copyright licenses and it is key to understand
such licenses before using the data to pretrain an LLM. That said, we can find mod-
els such as Bertimbau and Albertina-PTBR that are pretrained on BrWaC, and that
makes these models unsuitable for commercial applications. That is the reason for
the release of an alternative version of Albertina-PTBR, namely Albertina-PTBR-
NoBrWaC, pretrained on data with more permissive licenses such as the OSCAR
dataset (Abadji et al., 2022).
Our work proposes a model that is pretrained only on complete open data in
Brazilian Portuguese, Carolina Corpus, which is described in section 3. This al-
lows us to present a model that can be reproduced by being totally transparent in
terms of data licensing. Although we present models pretrained on the full dataset,
future models could use only specific documents given licenses of choice. Ad-
ditionally, the taxonomies provided in the corpus, i.e. the classification of each
document according to a set of specific domains, allows for training models for
specific domains in the future.
3
Carolina Corpus
The Carolina Corpus1 is a general corpus of Brazilian Portuguese in continuous
development. The iteration employed for the training of our models corresponds
to version 1.2 Ada, which was the latest version available during the pretraining
phase. The corpus was constructed with the dual purpose of allowing investigations
in linguistics and in artificial intelligence, particularly in the pretraining of large
language models, as exemplified in the present study (Crespo et al., 2023).
Version 1.2 of the Carolina Corpus has been constructed through the extraction
of texts from the Web. Its primary distinguishing feature, in comparison to similar
corpora, is the systematic focus on both provenance and typological diversity of
included texts.
The Corpus has been constructed employing the WaC-WiPT methodology (Web-
as-Corpus With Provenance and Typology) (Sturzeneker et al., 2022), a variation
of the prevailing Web-as-Corpus (WaC) approach (Baroni et al., 2006, 2009). This
method encompasses a sequence of stages for systematically exploring and curat-
ing targeted web domains prior to their crawling and data extraction. Such proce-
dure ensures the incorporation of only open-licensed texts, as well as the recording
1https://sites.usp.br/corpuscarolina/corpus/
3

--- Page 4 ---

of diverse metadata, encapsulated within the header of each text. These encompass
the original license of the text, responsible organization and various typological
information.
The version 1.2 of Carolina Corpus has 823 million words, segmented across
more than 2 million texts. In terms of typological diversity, these tokens are mainly
distributed in five types: instructional, juridical, virtual (including social media
content), entertainment, and journalistic texts (R. Serras and Sturzeneker, 2023).
As highlighted in Table 1, Corpus Carolina stands out as being the more open
option when comparing to the datasets used to train other Portuguese encoders.
The methodology adopted in its development guarantees the addition of permissive
license texts and maintains information about the original license of each text. This
allows the corpus and the models derived from it to be more freely distributed and
used.
Table 1: Comparision of Datasets used to train Brazilian Portuguese models.
Model Family
Training Dataset
Size (tokens)
Openness
BERTimbau
Albertina-PTBR
BrWaC
2.68B
Crawled from the web, available for research
purposes only, download upon request
Albertina-PTPT
Oscar (mainly)
2.20B
Crawled from the web, shuffled at line level
to avoid copyright issues, available in public
domain, download upon request
PeLLE
Carolina v1.2
0.82B
Crawled by type from curated web-domains,
free download, licenses specified for each
text.
4
PeLLE models
In this section we present the details on how we created the PeLLE family of LLMs
introduced in this work. We present three new models, namely pPeLLE, xPeLLE,
and mPeLLE, based on RoBERTa (Liu et al., 2019), XML-R (Conneau et al., 2020),
and mBERT (Devlin et al., 2018), respectively. Notice that our three models were
trained on the same 1.2 version of the Carolina corpus.
The pPeLLE model is based on the RoBERTa base model and was trained from
scratch, using Masked Language Modeling (MLM) objective, with a new vocabu-
lary using the Carolina Corpus (v1.2) only. Even though DeBERTa is consistently
better than RoBERTa (He et al., 2020), as literature presents, model performance
can be mainly improved by model and data size rather than specific improvements
in model architecture or attention mechanism (Kaplan et al., 2020; Tay et al., 2022).
4

--- Page 5 ---

Thus, we used RoBERTa for it is a simple and robust method for transformer’s pre-
training and left DeBERTa as a future work. To develop the new vocabulary we
followed the RoBERTa tokenization and used a Byte-Level Byte-Pair Encoding
with 50k sub-word units. As Portuguese makes use of accents, we used NFKD
Unicode normalization as the only text preprocessing step.
To chose the pretraining hyperparamenters, we first conducted a brief search,
varying the learning rate: {1e-4, 1e-3}; and batch size {2k, 4k, 8k}. To keep the
training of each model similar in number of total tokens, the maximum training
steps were adjusted according to the batch size to reach 40 epochs of training, to
keep an approximate training time (wall clock). Similar to RoBERTa, and follow-
ing the literature, using bigger batches results in better performance (lower loss)
(Izsak et al., 2021). Using the best hyperparameters (lr: 1e-4; bsz: 8k) the PeLLE
model was trained for 100k steps.
To evaluate the impact of multilingual models, we used mBERT and XLM-R
weights to initialize mPeLLE and xPeLLE, respectively. We kept they original
multilingual vocabulary and used the same pretraining hyperparameters as PeLLE.
xPeLLE was trained for 45k steps while mPeLLE was trained for 20k steps, also
using the Carolina Corpus v1.2.
All three models are available on Huggingface (links not provided in this ver-
sion for anonymity reasons).
5
Evaluation
In this section we present the evaluation of models on downstream tasks. For that,
we rely on a varied set of benchmark datasets for Brazilian Portuguese. More
specifically, we apply our models and baselines on the ASSIN, ASSIN 2, HateBR,
and Acórdãos TCU datasets. We believe this evaluation protocol helps us under-
stand the capability of our models, not only on different types of data but also on
different types of tasks.
For the aforementioned datasets, we conduct a full finetuning of the models,
where the classification layer used for MLM prediction is replaced by a new layer
for the downstream task. Then, we train this new layer and adjust the remain-
ing parameters for the new task. For that we rely on the HuggingFace library,
transformers2, which provide us the base coding structure to train and evaluate the
models.
Notice that, in terms of implementation, the main modification for each task
lies in setting up a different top-most layer for the model, according to the number
of classes involved in the problem or the type of task itself. If it is a regression
2https://github.com/huggingface/transformers
5

--- Page 6 ---

task, we need a single-value layer for predicting the final output, and if it is a
classification problem, the neural network needs a layer with as many outputs as
the number of classes. In addition, we also need to use the appropriate training
loss function, which is the Cross Entropy loss for classification and Mean Squared
Error (MSE) for regression.
Next, we describe the baseline models, experiments and results on each down-
stream dataset.
5.1
Baseline models
To compare the performance of the proposed models, we consider a set LLMs
pretrained either on Brazilian Portuguese corpora or multilingual datasets. They
are presented as follows.
BERTimbau (Souza et al., 2020) is from the family of BERT models devel-
oped for Brazilian Portuguese. Pretrained with BrWaC dataset, the largest Brazil-
ian Portuguese corpus, comprising 2.68B tokens from documents of several do-
mains, BERTimbau achieved the state-of-the-art for Named Entity Recognition
(NER), Sentence Textual Similarity (STS) and Recognizing Textual Entailment
(RTE) tasks in Brazilian Portuguese at the time it was released. For this work, we
consider both BERTimbau-Base and BERTimbau-Large models.
Albertina3 (Rodrigues et al., 2023) is another family of LLMs designed for
Brazilian and European Portuguese. These models are based on DeBERTa (He
et al., 2020), which was able to surpass humans on the SuperGLUE benchmark.
In this paper, we consider only the Brazilian Portuguese models: Albertina-PTBR-
Base, Albertina-PTBR-Large, and Albertina-PTBR-NoBrWaC. While the pretrain-
ing data for Albertina-PTBR-base and Albertina-PTBR-Large were based on BrWaC,
Albertina-PTBR-NoBrWaC relied on a set of documents from the OSCAR dataset,
making it a model with less-restricted licenses in pretraining data.
mBERT4 is the multilingual version of BERT base (Devlin et al., 2018). It was
pretrained with data from 104 different languages, considering the languages with
largest Wikipedia representation.
XLM-RoBERTa (XLM-R) is built upon the RoBERTa model architecture and
is pretrained on a large corpus containing 100 different languages, which enables
it to perform well on a variety of cross-lingual tasks without the need for language-
specific training data (Conneau et al., 2020).
3We emphasize that Albertina-PTBR-Base was removed from their repository at the time of de-
velopment of this paper and may not be available for further analysis.
4https://huggingface.co/bert-base-multilingual-cased
6

--- Page 7 ---

5.2
ASSIN and ASSIN 2
ASSIN (Fonseca et al., 2016) and ASSIN 2 (Real et al., 2020) are datasets for the
tasks of Recognizing Textual Entailment (RTE) – also known as Natural Language
Inference – and Semantic Textual Similarity (STS). They contains up to 10,000 pair
of sentences annotated with gold standard. STS task is a regression problem with
a target score ranging from 1 to 5. RTE is a classification problem but ASSIN and
ASSIN 2 have different label sets. ASSIN RTE task is a multi-class classification
with sentences labeled as entailment, paraphrase or none. The ASSIN 2 RTE task
was simplified to a binary classification problem with target labels only stating if
the entailment holds or not (entailment or none).
Each dataset is divided into training, validation and test splits but their distri-
bution are different (see Table 2). While ASSIN contains sentences in Brazilian
and European Portuguese, equally distributed across each split, ASSIN 2 contains
only the Brazilian variation.
Table 2: ASSIN and ASSIN 2 dataset splits.
Train
Val.
Test
Total
ASSIN
5,000
1,000
4,000
10,000
ASSIN 2
6,500
500
2,448
9,448
To evaluate each model in this downstream tasks, we performed a hyper-parameter
search using a Population Based Training (PBT) (Jaderberg et al., 2017).
We
searched over the batch sizes of 16, 32 and 64 and learning rates 5e-6, 5e-5, 5e-4
and 5e-3, resulting in 12 initial models (agents) trained for 10 epochs with pertur-
bation between each epoch.
The results in Table 3 shows that larger models results in better performance,
which is in accordance with the literature (Kaplan et al., 2020), but we focus our
analysis on smaller (base) models as they represent a larger variability in its method
of construction. As BERTimbau performs better among base models, it is possi-
ble to assign its improved performance to its pretraining design. BERTimbau base
used mBERT weights as starting point. Also, they retrained the model tokenizer
from scratch, creating a new vocabulary, which is known to improve model perfor-
mance (Artetxe et al., 2020). pPeLLE performance is another evidence for that as
it performs close to multilingual models and was trained with a new vocabulary.
When comparing PeLLE family models with multilingual models, we can observe
that multilingual models is a good choice for weight initialization and XLM-R is
also a better choice for Portuguese as xPeLLE stands out among PeLLE family.
7

--- Page 8 ---

Table 3: ASSIN and ASSIN 2 results. RTE task are measured by F1 Score and
STS by Pearson Correlation.
ASSIN
ASSIN 2
Model
RTE
STS
RTE
STS
avg
Albertina PTBR Large
0.8959
0.8746
0.9152
0.8680
0.8884
Albertina PTBR NoBrWaC
0.8943
0.8693
0.9040
0.8543
0.8804
Bertimbau Large
0.8613
0.8532
0.8891
0.8495
0.8632
Albertina PTBR Base
0.8292
0.8237
0.8762
–
0.8430
Bertimbau Base
0.8486
0.8423
0.8883
0.8443
0.8558
mBERT
0.8052
0.7982
0.8373
0.8163
0.8142
XLM-R Base
0.8148
0.8192
0.8703
0.8026
0.8267
pPELLE
0.8113
0.8042
0.8489
0.8059
0.8175
mPELLE
0.7818
0.7981
0.8437
0.7942
0.8044
xPELLE
0.8184
0.8294
0.8551
0.8232
0.8315
5.3
HateBR
HateBR is an annotated dataset of offensive language on social media data (Vargas
et al., 2022). It is comprised of 7,000 Instagram5 comments annotated according
to three distinct layers: 1) binary classification in offensive versus non-offensive
content; 2) multi-class classification in nine hate speech groups, i.e. xenophobia,
racism, homophobia, sexism, religious intolerance, partyism, apology for the dic-
tatorship, antisemitism, and fatphobia; and 3) a regression problem to compute
offensiveness levels into highly, moderately, and slightly offensive messages. We
believe that this dataset not only allows us to evaluate the LLMs into a real-world
application with real-world data, but also provides an interesting range of applica-
tions for evaluating the models, i.e. binary classification, multiclass classification,
and regression.
We split the 7,000 samples of the dataset in 80% of the examples for training,
10% for validation, and 10% for test. The selection of samples was random and
stratified considering the distribution of labels for the binary classification task6,
and we relied on the same split for the regression. Notice that the binary problem
is almost balanced, with 3,500 samples of non-offensive texts and 3,477 with of-
fensive ones, so our data splitting aimed at keeping that balance. For the multiclass
problem, we also considered the stratification of the dataset considering the distri-
bution of the classes. Since the multiclass problem is also a multilabel problem,
5https://www.instagram.com
6The data splits will be available online
8

--- Page 9 ---

Table 4: HateBR class distribution.
Class
#samples
non-offensive
3500
offensive & non-hate speech
2798
apology for the dictatorship
28
fatphobia
20
homophobia
15
partyism
479
partyism AND sexism
11
religious intolerance
46
sexism
80
where a sample can be associated to more than one class at once, we simplified
the implementation by computing the set with all possible combinations of labels
and considered each combination as a separate class. Given that some classes pre-
sented too few example for a proper division into training, validation, and test sets,
classes with less that 10 samples were discarded. The list of classes and respective
number of samples is presented in Table 4.
It is also worth mentioning that, for these evaluations, we adopted a simplified
set of experiments. All models were trained with the same set of meta-parameters,
i.e. learning rate set to 5e-5, batch size set to 16, and number of epochs set to
5, and we consider only the baselines with comparable sizes. The main idea is
to understand how the models compare in a fast-deployment setting, for which
computation resources are not abundant and one needs to train smaller models with
limited optimizations. Thus, the models we considered as baselines are mBERT,
Bertimbau-Base and Albertina-PTBR-Base, where the latter two models are simply
referred to as Bertimbau and Albertina-PTBR in this section.
In Table 5 (see 2 Classes column), we present the F1 scores for the binary
classification task. We observe that all models perform quite close in this task.
pPeLLE and xPeLLE achieves the same values of Bertimbau, with 0.91, and these
three models are slightly better than mPeLLE and Albertina-PTBR, both with an
F1 score of 0.90. The multilingual mBERT model is slightly worse than the top
performers, with 0.87.
The results with the multi-class classification are presented in Table 5 (see 9
Classes column). Here we observe a slightly different scenario from the binary
classification. In this problem Bertimbau performed best with an F1 score of 0.50,
followed by mPeLLE, with 0.49, and by pPeLLE and Albertina-PTBR, both with
F1s of 0.47. Once again, mBERT performed the worst, with an F1 of only 0.39.
9

--- Page 10 ---

Table 5: Results for the HateBR and Acórdãos TCU tasks. The results of the
Acórdãos TCU datasets are presented in the "TCU dataset" column and are ex-
pressed in terms of F1 Score. For HateBR, the binary classification (2 Classes col-
umn) and multiclass classification (9 Classes column) are also expressed in terms
of F1 Score. The regression taks in HateBR dataset are expressed in terms of R2.
HateBR
Model
2 Classes
9 Classes
Regression
TCU Dataset
avg
pPeLLE
0.91
0.47
0.47
0.82
0.6675
xPeLLE
0.91
0.43
0.50
0.77
0.6525
mPeLLE
0.90
0.49
0.49
0.81
0.6725
mBERT
0.87
0.39
0.43
0.72
0.6025
Bertimbau
0.91
0.50
0.54
0.80
0.6875
Albertina-PTBR
0.90
0.47
0.45
0.82
0.6600
And xPeLLE presented modest results, with an F1 score of 0.43.
The results for the regression task are presented in Table 5 (see Regression
column). First, it is worth mentioning that the models present quite modest R2
scores, with the best result achieved by Bertimbau of only 0.54. The PeLLE mod-
els were closest competitors, with 0.50, 0.49, and 0.47 for xPeLLE, mPeLLE, and
pPeLLE, respectively. The Albertina-PTBR was slightly worse, with 0.45, fol-
lowed by mBERT with 0.43, which was the worst model once again.
From these results, the first main conclusion is that the use of open data seems
not to affect so much the performance of the models when finetuned to a down-
stream task. In the binary classification task, pPeLLE achieves the best result, and
at least one of our three models was a strong contender in the other two tasks. This
is encouraging since models pretrained on open data can be used with no restric-
tion in terms of data. Additionally, the not-so-stellar results of Albertina-PTBR
indicate that a smaller pretraining dataset can result in better models if the data
is well-curated, which is the case of the Caroline corpus. Finally, it seems clear
that Portuguese specific models compose a better choice for these tasks, given that
mBERT usually performs worse than the Portuguese-specific models.
5.4
Acórdãos TCU dataset
We complement the evaluation of the models on the case-law documents from
the Acórdãos TCU dataset7. This dataset is particularly interensting to evaluate
7https://www.kaggle.com/datasets/ferraz/acordaos-tcu
10

--- Page 11 ---

whether the legal documents included in Carolina help the model to better handle
legal-domain documents. In addition, this dataset is also useful to evaluate the
models on longer documents, since the average document length is 225.75 words,
with document lengths ranging from 8 to 4929 words. For comparison purposes,
the mean length of the texts in the HateBR dataset is of 11.56 words.
For this evaluation we focused on the classification of the type of the document,
consisting of 29 classes. This dataset contains 35,414 samples, with an average
number of examples per class of 1,221.55, with the number of examples per class
ranges from 20 to 12,659. Since there are classes that we consider with too few ex-
amples, such as single-digit number of examples, we removed such low-resourced
classes and considered only the remaining 24 classes to train our models.
For the experimental setup, we followed a similar training approach to that
with HateBR, described in Section 5.3. We considered the same meta-parameters
and the same baseline models, i.e. mBERT, Bertimbau-Base, and Albertina-PTBR-
Base.
The results in terms of macro F1 scores are presented in Table 5 (see TCU
Dataset column). We observe that pPeLLE achieves the highest F1 score with
0.82, tied with Albertinha-PTBR. The mPeLLE and Bertimbau models presented
values that were close to that, i.e. 0.81 and 0.80, respectively. In addition to that,
xPeLLE was slightly worse with 0.77. Again, mBERT lagged behind the other
models, with a modest score of only 0.72.
These results somehow confirm out previous outcomes. That is, the models
from the PeLLE family usually present competitive results compared with mod-
els trained on larger and non-curated datasets, such as Bertimbau and Albertina-
PTBR. Given that there is one PeLLE model, i.e. pPeLLE, that achieved the best
performance on this dataset, we may claim that the use of law-related documents
in the pretraining data can result in a model that excels on legal-domain down-
stream tasks. Off course, further experiments with other legal-domain datasets are
necessary to make such claim stronger.
6
Conclusions and Future Steps
The results of the evaluation above show that several tasks performs better with
larger models, but some benefits from smaller-but-curated data in its pretraining.
We do not have a clear distinction between those two sets of tasks, in general.
However, for tasks involving regression, as in Section 5.3, because all eval-
uated models are pretrained for classification only, larger models clearly have an
advantage. So size demonstrably dominates when all else is equalized.
It is also clear that pure Portuguese-only pretrained model, pPeLLe, for the
11

--- Page 12 ---

size of curated corpus used in this work, around 0.85B tokens, is sometimes a
competitive performer in Portuguese-only tasks against mPeLLE and xPeLLE.
Models of the PeLLE family that extend the weights of multi-language models
such as mBERT and XLM-R are often quite competitive, usually just a few percent-
age points below the best performing Large models. Neither xPeLLe nor mPeLLE
is a clear best performer, but the former has come up front more frequently.
The points above reinforce the advantage of continuing the enlargement of the
Carolina is a Corpus, which describes itself as in constant development. Its future
versions may serve the basis for larger models which may benefit both from the
size and quality of curated data. On top of allowing for reproducible experiments
due to the employment of open datasets, this new training will hopefully allow us to
better understand the impact of the amount of training data on model performance.
References
Abadji, J., Ortiz Suarez, P., Romary, L., and Sagot, B. (2022). Towards a cleaner
document-oriented multilingual crawled corpus.
In Proceedings of the Thir-
teenth Language Resources and Evaluation Conference, pages 4344–4355, Mar-
seille, France. European Language Resources Association.
Artetxe, M., Ruder, S., and Yogatama, D. (2020). On the cross-lingual transferabil-
ity of monolingual representations. In Proceedings of the 58th Annual Meeting
of the Association for Computational Linguistics, pages 4623–4637. Association
for Computational Linguistics.
Baroni, M., Bernardini, S., et al. (2006). WaCky! working papers on the web as
corpus. Gedit.
Baroni, M., Bernardini, S., Ferraresi, A., and Zanchetta, E. (2009). The wacky wide
web: a collection of very large linguistically processed web-crawled corpora.
Language resources and evaluation, 43:209–226.
Brown, T., Mann, B., Ryder, N., Subbiah, M., Kaplan, J. D., Dhariwal, P., Nee-
lakantan, A., Shyam, P., Sastry, G., Askell, A., Agarwal, S., Herbert-Voss, A.,
Krueger, G., Henighan, T., Child, R., Ramesh, A., Ziegler, D., Wu, J., Winter,
C., Hesse, C., Chen, M., Sigler, E., Litwin, M., Gray, S., Chess, B., Clark, J.,
Berner, C., McCandlish, S., Radford, A., Sutskever, I., and Amodei, D. (2020).
Language models are few-shot learners. In Larochelle, H., Ranzato, M., Hadsell,
R., Balcan, M., and Lin, H., editors, Advances in Neural Information Processing
Systems, volume 33, pages 1877–1901. Curran Associates, Inc.
12

--- Page 13 ---

Conneau, A., Khandelwal, K., Goyal, N., Chaudhary, V., Wenzek, G., Guzmán,
F., Grave, E., Ott, M., Zettlemoyer, L., and Stoyanov, V. (2020). Unsupervised
cross-lingual representation learning at scale. In Proceedings of the 58th Annual
Meeting of the Association for Computational Linguistics, pages 8440–8451,
Online. Association for Computational Linguistics.
Crespo, M. C. R. M., de Souza Jeannine Rocha, M. L., Lourenço Sturzeneker,
M., Ribas Serras, F., Lamartine de Mello, G., Silva Costa, A., Palma, M. F.,
Morais Mesquita, R., Guets, R. d. P., Marques da Silva, M., et al. (2023). Car-
olina: a general corpus of contemporary brazilian portuguese with provenance,
typology and versioning information. arXiv e-prints, pages arXiv–2303.
Devlin, J., Chang, M.-W., Lee, K., and Toutanova, K. (2018). Bert: Pre-training
of deep bidirectional transformers for language understanding. arXiv preprint
arXiv:1810.04805.
Fonseca, E., Santos, L., Criscuolo, M., and Aluisio, S. (2016). Assin: Avaliacao
de similaridade semantica e inferencia textual. In Computational Processing
of the Portuguese Language-12th International Conference, Tomar, Portugal,
pages 13–15.
He, P., Liu, X., Gao, J., and Chen, W. (2020). Deberta: Decoding-enhanced bert
with disentangled attention. arXiv preprint arXiv:2006.03654.
Izsak, P., Berchansky, M., and Levy, O. (2021). How to train BERT with an aca-
demic budget. In Proceedings of the 2021 Conference on Empirical Methods in
Natural Language Processing, pages 10644–10652. Association for Computa-
tional Linguistics.
Jaderberg, M., Dalibard, V., Osindero, S., Czarnecki, W. M., Donahue, J., Razavi,
A., Vinyals, O., Green, T., Dunning, I., Simonyan, K., Fernando, C., and
Kavukcuoglu, K. (2017). Population based training of neural networks. arXiv
preprint arXiv:1711.09846.
Joshi, P., Santy, S., Budhiraja, A., Bali, K., and Choudhury, M. (2020). The state
and fate of linguistic diversity and inclusion in the NLP world. In Proceedings
of the 58th Annual Meeting of the Association for Computational Linguistics,
pages 6282–6293, Online. Association for Computational Linguistics.
Kaplan, J., McCandlish, S., Henighan, T., Brown, T. B., Chess, B., Child, R., Gray,
S., Radford, A., Wu, J., and Amodei, D. (2020). Scaling laws for neural language
models. arXiv preprint arXiv:2001.08361.
13

--- Page 14 ---

Liu, Y., Ott, M., Goyal, N., Du, J., Joshi, M., Chen, D., Levy, O., Lewis, M.,
Zettlemoyer, L., and Stoyanov, V. (2019). Roberta: A robustly optimized bert
pretraining approach. arXiv preprint arXiv:1907.11692.
R. Serras, F. and Sturzeneker, M. (2023).
Carolina: um córpus geral do por-
tuguês brasileiro com proveniência, tipologia e versionamento. note = Accessed:
2023–09-18.
Raffel, C., Shazeer, N., Roberts, A., Lee, K., Narang, S., Matena, M., Zhou, Y., Li,
W., and Liu, P. J. (2020). Exploring the limits of transfer learning with a unified
text-to-text transformer. J. Mach. Learn. Res., 21(1).
Real, L., Fonseca, E., and Gonçalo Oliveira, H. (2020). The assin 2 shared task: a
quick overview. In Computational Processing of the Portuguese Language: 14th
International Conference, PROPOR 2020, Evora, Portugal, March 2–4, 2020,
Proceedings 14, pages 406–412. Springer.
Rodrigues, J., Gomes, L., Silva, J., Branco, A., Santos, R., Cardoso, H. L., and
Osório, T. (2023). Advancing neural encoding of portuguese with transformer
albertina pt. arXiv preprint arXiv:2305.06721.
Souza, F., Nogueira, R., and Lotufo, R. (2020). Bertimbau: pretrained bert mod-
els for brazilian portuguese. In Intelligent Systems: 9th Brazilian Conference,
BRACIS 2020, Rio Grande, Brazil, October 20–23, 2020, Proceedings, Part I 9,
pages 403–417. Springer.
Sturzeneker, M., Crespo, M. C., Rocha, M. L., Finger, M., de Sousa, M. C. P.,
do Monte, V. M., and Namiuti, C. (2022). Carolina’s methodology: building
a large corpus with provenance and typology information.
In DHandNLP@
PROPOR, pages 53–58.
Tay, Y., Dehghani, M., Rao, J., Fedus, W., Abnar, S., Chung, H. W., Narang, S.,
Yogatama, D., Vaswani, A., and Metzler, D. (2022). Scale efficiently: Insights
from pretraining and finetuning transformers. In International Conference on
Learning Representations.
Vargas, F., Carvalho, I., Rodrigues de Góes, F., Pardo, T., and Benevenuto, F.
(2022). HateBR: A large expert annotated corpus of Brazilian Instagram com-
ments for offensive language and hate speech detection. In Proceedings of the
Thirteenth Language Resources and Evaluation Conference, pages 7174–7183,
Marseille, France. European Language Resources Association.
14

--- Page 15 ---

Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N.,
Kaiser, Ł., and Polosukhin, I. (2017). Attention is all you need. Advances in
neural information processing systems, 30.
Wagner Filho, J. A., Wilkens, R., Idiart, M., and Villavicencio, A. (2018). The
brWaC corpus: A new open resource for Brazilian Portuguese. In Proceedings
of the Eleventh International Conference on Language Resources and Evalua-
tion (LREC 2018), Miyazaki, Japan. European Language Resources Association
(ELRA).
Xue, L., Constant, N., Roberts, A., Kale, M., Al-Rfou, R., Siddhant, A., Barua,
A., and Raffel, C. (2021). mT5: A massively multilingual pre-trained text-to-
text transformer. In Proceedings of the 2021 Conference of the North American
Chapter of the Association for Computational Linguistics: Human Language
Technologies, pages 483–498, Online. Association for Computational Linguis-
tics.
15

```
