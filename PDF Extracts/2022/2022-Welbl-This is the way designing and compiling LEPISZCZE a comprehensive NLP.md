---
title: "2022-Welbl-This is the way designing and compiling LEPISZCZE a comprehensive NLP - PDF Extract"
source_pdf: "2022-Welbl-This is the way designing and compiling LEPISZCZE a comprehensive NLP.pdf"
pages: 22
extracted_at: "2026-02-13T09:50:29.336345"
---

# PDF Extract: 2022-Welbl-This is the way designing and compiling LEPISZCZE a comprehensive NLP

**Source PDF:** 2022-Welbl-This is the way designing and compiling LEPISZCZE a comprehensive NLP.pdf
**Total Pages:** 22

---

## Content

```
--- Page 1 ---

This is the way: designing and compiling
LEPISZCZE, a comprehensive NLP benchmark for
Polish
Łukasz Augustyniak
WUST
(Wroclaw University of
Science and Technology)
Kamil Tagowski
WUST
Albert Sawczyn
WUST
Denis Janiak
WUST
Roman Bartusiak
WUST
Adrian Szymczak
WUST
Marcin W ˛atroba
WUST
Arkadiusz Janz
WUST
Piotr Szyma´nski
WUST
Mikołaj Morzy
Poznan University of Technology
Tomasz Kajdanowicz
WUST
Maciej Piasecki
WUST
Abstract
The availability of compute and data to train larger and larger language models
increases the demand for robust methods of benchmarking the true progress of LM
training. Recent years witnessed signiﬁcant progress in standardized benchmarking
for English. Benchmarks such as GLUE, SuperGLUE, or KILT have become a de
facto standard tools to compare large language models. Following the trend to
replicate GLUE for other languages, the KLEJ benchmark1 has been released for
Polish. In this paper, we evaluate the progress in benchmarking for low-resourced
languages. We note that only a handful of languages have such comprehensive
benchmarks. We also note the gap in the number of tasks being evaluated by
benchmarks for resource-rich English/Chinese and the rest of the world.
In this paper, we introduce LEPISZCZE 2, a new, comprehensive benchmark for
Polish NLP with a large variety of tasks and high-quality operationalization of the
benchmark. We design LEPISZCZE with ﬂexibility in mind. Including new models,
datasets, and tasks is as simple as possible while still offering data versioning and
model tracking. In the ﬁrst run of the benchmark, we test 13 experiments (task
and dataset pairs) based on the ﬁve most recent LMs for Polish. We use ﬁve
datasets from the Polish benchmark and add eight novel datasets. As the paper’s
main contribution, apart from LEPISZCZE , we provide insights and experiences
learned while creating the benchmark for Polish as the blueprint to design similar
benchmarks for other low-resourced languages.
1klej is the word for glue in Polish
2lepiszcze is the Polish word for glew, the Middle English predecessor of glue
36th Conference on Neural Information Processing Systems (NeurIPS 2022) Track on Datasets and Benchmarks.
arXiv:2211.13112v1  [cs.CL]  23 Nov 2022

--- Page 2 ---

1
Introduction
Lack of reproducibility is an infuriating problem in machine learning practice. The inability to
reproduce evaluation results and conduct reliable model comparisons is usually related to poor code
quality, unclear and cryptic selection of hyper-parameter values, the random introduction of multiple
factors affecting classiﬁcation performance, and lack of a well-deﬁned evaluation protocol (Pineau
et al., 2021). These problems can be circumvented by encouraging people to use standardized and
peer-reviewed evaluation environments. The rapid development of diverse language technology has
increased the need for reliable evaluation environments.
The reproducibility issues are intensifying even stronger as more novel language models emerge each
year. We have seen a remarkable progress on many language understanding tasks, from language
modeling (Brown et al., 2020; Rae et al., 2021; Hoffmann et al., 2022), Named Entity Recognition (Li
et al., 2020; Ye et al., 2022), Q&A (Lan et al., 2020; Yang et al., 2019), or various text classiﬁcation
tasks (Peters et al., 2018; Bingyu and Arefyev, 2022) in recent years. Moreover, in the last decade,
data-centric models have become the major direction in solving most problems in the NLP area.
Researchers and industry experts focus more on curated datasets and their maintenance processes.
Hence, benchmarking models based on many datasets and their various and constantly changing
versions is a great challenge.
Figure 1: Tasks in large NLP benchmarks vs. the number of speakers, with Indian languages grouped
for readability.
As shown in Figure 1, most NLP benchmarks are written for well-resourced languages such as English
and Mandarin Chinese. This is understandable because many datasets exist in these languages, and
many research teams are working in the context of these languages. Besides English and Mandarin
Chinese, languages thoroughly covered with benchmarks include Indian, Spanish, French, and
Portuguese. These are among the most commonly used languages in the world, and their position
in the ranking is not surprising. However, we can also ﬁnd Arabic and Japanese, widely spoken
languages, but surprisingly few tasks are covered in benchmarks for these languages. Finally, we
have languages with some benchmarks, such as Romanian, Persian, Dutch or Polish, but they only
cover the most basic NLP tasks.
In this work, we focus on Polish and provide datasets and tools to facilitate research on Polish NLP
tasks. We designed the benchmarking process so that it could be easily applied to other languages.
Thus, preparing and adding benchmarks for other low-resourced languages should become much less
laborious.
The Polish benchmarking tradition has a relatively short history. One of the few platforms for
evaluating and comparing modern language models for Polish is the KLEJ benchmark (Rybak et al.,
2020), a single-metric benchmark deﬁned over a limited dataset. This simple practice for evaluating
a model’s performance no longer works. Current recommendations for the comparative evaluation of
LMs advocate the inclusion of diversiﬁed tasks, challenges, and tests. Hence, we wanted to rethink
and design a benchmark and environment to assess models so that they can still serve as valuable
progress indicators.
2

--- Page 3 ---

Our main contributions are as follows:
• We propose LEPISZCZE , a new, extensive benchmark for Polish NLP with a large variety
of tasks, expanding the previous Polish benchmark KLEJ with eight new datasets, published
as a uniﬁed modern API.
• We design the benchmark and its maintenance using the best practices found in the literature,
and we also investigate some of the most problematic aspects of creating benchmarks.
We share the lessons learned while building the benchmark.
• We present the summary of training and evaluation of more than 6000 different models
for LEPISZCZE , storing all information about code, dataset versions, parameters, metrics,
predictions, or even information about their experimental environment.
2
Related Work
We used Google Scholar to review available NLP benchmarks for languages with at least 10 million
speakers without going deeper into dialects (i.e., German includes all German dialects without divid-
ing into Standard or Bavarian German). We searched for <language name> NLP|NLG benchmark.
Furthermore, we dismissed benchmarks consisting of a single dataset. As a result, we found 35
benchmarks (see Table 1 in the Appendix), which included a total of 71 different tasks. Out of those,
only 34 appeared in one language. These can be divided into two groups: specialized tasks which
require a larger effort to build a good dataset (like diagnosis normalization, see (Wang et al., 2020)),
or misdeﬁned tasks such as Named Entity Recognition in the Polish KLEJ benchmark, which was
not a span labeling task, but rather a text fragment classiﬁcation task to detect if it contains an entity,
without providing the span. We provide more detailed results of our survey in the supplementary
materials.
When it comes to language coverage, only 31 languages have an existing NLP or NLG benchmark
out of 91 available in the 2022 edition of Ethnologue (Fennig et al., 2022): Arabic, Assamese,
Bengali, Chinese, Dutch, English, French, German, Gujarati, Hindi, Indonesian, Italian, Japanese,
Kannada, Korean, Malayalam, Marathi, Odia, Persian, Polish, Portuguese, Punjabi, Romanian,
Russian, Spanish, Swahili, Tamil, Telugu, Turkish, Urdu. The 74 tasks were not equally distributed
per language, per Figure 1. Benchmarks for the two most commonly spoken languages: English and
Chinese, would cover around 40 tasks. In contrast, the languages with the lowest number of tasks
available in benchmarks and lower numbers of native speakers were Romanian and Polish (around 10
tasks). The results of our analysis are attached in Appendix.
The Polish language has a disproportionately small number of tasks in its main NLP benchmarks
given nearly 40 million native speakers. KLEJ benchmark originally provided only 9 tasks, marking
Polish the least task-covered European language concerning modern NLP and NLG benchmarked
tasks. Once we take a deeper look at how tasks are formulated in KLEJ, we must acknowledge that
the number of tasks formulated in a manner established in a given NLP sub-ﬁeld is even smaller.
There are two similar tasks of online reviews sentiment analysis, differing only in domains (PolEmo),
and another sentiment analysis task (AR) framed as a regression task. Thus, the number of tasks can
be reduced to 7 if we consider these datasets as one task. Moreover, some of the tasks are ill-deﬁned.
The NER task in KLEJ is not a sequence tagging but a document classiﬁcation task. Summarization
in KLEJ is evaluated based on classifying pairs of text and summary, the task is to predict whether
the summary summarizes the text. Most benchmarks would deﬁne summarization as an NLG task,
where the model is expected to generate the summary and would be evaluated with ROGUE or BLEU
measures. A similar situation is happening in the Q&A task.
The KLEJ benchmark was created in 2020. Since then, no new datasets have been added, and the
benchmark can be considered a little stale. Some of the tasks in KLEJ are not very difﬁcult and
diverse. Another potential problem with KLEJ is that it does not provide any environment for testing
or submitting the model, as the submission requires only a prediction ﬁle. Finally, the heterogeneous,
task-speciﬁc metrics for all the tasks in KLEJ could also be problematic when comparing the models
as it may lead to erroneous conclusions. In our work, we aim to address these limitations. In particular,
we plan to develop and maintain the long-term benchmark as part of the CLARIN-PL-Biz project.
3

--- Page 4 ---

3
LEPISZCZE
LEPISZCZE is an open-source benchmark and a continuous-submission leaderboard, concentrating
public Polish datasets (existing and new) in speciﬁc tasks. Integrating datasets and tasks with model
performance and efﬁciency allows academia and industry to gauge performance on tasks of interest
quickly. Finally, it intends to foster constructive competition and innovation by bringing together and
promoting previously disparate resources.
Our benchmark is structured into datasets, tasks, and models. We design the benchmark to be easily
extendable and ﬂexible so that leaderboards for various subsets of datasets, tasks, and models can be
added in the future.
3.1
Benchmark designing and construction process
In this section, we introduce the benchmark construction process and lessons learned during this
procedure, hoping that they could serve as a guide for other researchers that will face the task of
creating a benchmark. The general design concept we follow is to make the submission process
straightforward and benchmark easily extendable to new models and datasets, guaranteed by accessi-
ble experimental infrastructure and a uniﬁed submission procedure. Our approach makes it effortless
to test and compare models in a reliable and transparent way with the possibility of quickly entering
new data.
Task diversity
The value of the benchmark depends directly on the chosen tasks and their diversity.
If an unrepresentative collection of data and tasks is used to create a benchmark, the evaluation is of
limited informative value for the further development of language models. If a benchmark consists
only of closely related datasets, we can evaluate only a narrow part of the model’s capabilities. Hence,
one of the ﬁrst and the most critical tasks for us was to gather many diverse tasks for Polish that cover
different domains and tasks. We wanted to cover also many sources of text data in our benchmarking
environment. The model’s performance could differ for books, social media, and other domain texts.
Thus, having a representative collection of text data allows for evaluating the models in terms of
their in-domain and out-of-domain generalization abilities. However, since Polish is a low-resource
language, our choice was limited and we ended up with text classiﬁcation, natural language inference,
and sequence labeling tasks. We considered a few datasets for the regression task (e.g., CDSC-R
or Allegro Reviews from KLEJ). However, in our opinion, mentioned datasets are unsuitable for
benchmarking. It appears that annotation consistency is much lower than claimed in the original
papers (Rybak et al., 2020; Wróblewska and Krasnowska-Kiera´s, 2017). However, we hope to extend
the benchmark with other than the mentioned above regression task in the future.
Dataset selection
To select proper datasets for our benchmark, we ﬁrst looked at the datasets
available in KLEJ (Rybak et al., 2020). Many datasets have been described in their research papers,
but they were still quite hard to obtain, and of course, they were in different formats. We also
noticed that some tasks deﬁned in the KLEJ benchmark were ill-deﬁned, e.g., the NER task as text
classiﬁcation instead of sequence labeling. We set out to ﬁx these problems and widen the scope of
covered tasks and domains. Actual sequence tagging datasets (KPWr-NER and NKJP POS tagging)
were added to the benchmark. Regarding the classiﬁcation task, we added aspect-based sentiment
analysis, political advertising detection, and punctuation restoration datasets to cover more diversiﬁed
tasks. We also prepared two new datasets concerning legal text (Political Abusive Clauses) and
dialogue systems (DiaBiz.Kom). It is important to mention that almost all of the datasets chosen
by us (i.e., KPWr-NER, AspectEmo, PolEmo, DiaBiz.Kom, PAC, Political Advertising, and PSC)
have been created by researchers in the CLARIN-PL project; hence the annotation processes and
inter-annotator agreements are properly described in the relevant papers. The complete list of datasets
with a short description can be found in Section 3.2.
We challenged an interesting problem when extending the collection of datasets covered in the
benchmark, namely, should we add a dataset that is not free and publicly available? It is an important
choice when designing the benchmark. On the one hand, it contradicts the guidelines of open science,
but on the other hand, it makes the benchmark more challenging and practically useful. After a lot of
deliberations, we have decided to add to the benchmark the Dialogue Acts dataset — DiaBiz.Kom
(more in Section 3.2) which is available only for internal usage of CLARIN-PL-Biz associates. Still,
the dataset covers a signiﬁcant collection of infrequent domain data for Polish targeted at spoken
4

--- Page 5 ---

language understanding. The results of modern language models for this dataset present much room
for improvement — see Table 3.
Model selection
The next step was to select initial models in the benchmark to provide a baseline
and allow for easy comparison with the already published models. Each baseline model had to be
available in the HuggingFace repository, and it could not be too big since we were again limited
by the amount of available compute.3 We ﬁrst took the models of different sizes provided in
KLEJ – HerBERT-large is a top-1 model in the KLEJ benchmark. We used these models and our
hyperparameter search module to validate the experimental setup and generate the ﬁrst results for
benchmark. We then utilized another popular mono-lingual encoder model and tested it against
the previous one. Finally, to provide some diversity, we took the sentence model (which in fact is
a cross-lingual) and ran the experiment. We plan to add new models to the benchmark to allow
comparison of cross- vs. single-lingual and sentence- vs. word encoders. Table 2 shows the ﬁnal
collection of models used for experiments.
Choice of metrics
Every benchmark has to provide task-speciﬁc evaluation metrics. Even though
we can focus on a single metric for a speciﬁc dataset and task in most cases, it could not be enough
for many scenarios. A single metric can be insufﬁcient to capture the varying cost of errors in many
tasks. For instance, in sentiment analysis, the misclassiﬁcation of "strong negative" as "negative" is
far less consequential than the misclassiﬁcation of the same case as "positive". In general, instead of
focusing on a single metric, we want to evaluate language models using multiple metrics (and allow
for the construction of compound weighted metrics). LEPISZCZE calculates many different metrics,
namely, F1-score, recall, precision, and accuracy. We allow sorting submissions based on various
metrics. We believe that comparing models between tasks using different metrics may be misleading,
which is why we use homogeneous metrics to compare and score the models.
Many benchmarks concentrate only on metrics that evaluate the quality of predictions, without consid-
ering the cost of prediction. We believe that the omission of externalities, such as the computational
requirements of models, leads to very biased rankings. The costs incurred by modern language
models (i.e. in terms of their carbon footprint) can be signiﬁcant and should be included in the
evaluation. We track all Python environment information and completion times of all experiments for
the benchmark. This way, we can build a custom leaderboard that incorporates computational costs
as well. As (Ethayarajh and Jurafsky, 2020) said, a highly inefﬁcient model would provide less utility
to practitioners but not to a leaderboard since it is a cost that only the former must bear.
Experimental environment
We use several tools in our experimental environment to facilitate
the use of the benchmark. Benchmarking involves running many experiments and tracking their
performance. We actively utilize the HuggingFace repository to make the process of adding and
testing datasets and models convenient. We uniﬁed all datasets into one accessible and easy-to-process
data format, uploaded them to the HuggingFace Datasets 4 repository and ran all experiments using
the HuggingFace hub. Technically, our benchmark allows us to choose any dataset or collect utterly
new data, prepare data-loading scripts compatible with the HuggingFace platform, and evaluate
models in the target language. We also develop our library clarinpl-embeddings to unify the
whole process of training, validating, performing hyperparameter search, testing, and submitting
results to the leaderboard almost automatically, in only a few lines of code. We believe that this step
is crucial to allow continuous benchmarking and encourage researchers to submit their models or
datasets. Integrating benchmark libraries with HuggingFace Datasets platform opens new possibilities
to evaluate language models in a multilingual zero-shot setting for any low-resource language.
We believe using a uniﬁed dataset inventory will contribute to the sustainable development of reliable
evaluation data. The clarinpl-embeddings library is built on PyTorch, PyTorch Lightning and
Transformers is easily extendable and modiﬁable; we plan to keep developing and expanding it
over time. While the KLEJ benchmark required only a .zip ﬁle submission with predictions, we
provide a great level of technical support to the user with the extensive experimental environment
that reinforces the reproducibility.
3Maximum size of the model to perform hyperparameter search in a reasonable time was 350 million
parameters
4https://huggingface.co/datasets
5

--- Page 6 ---

Standard splits problems
Many benchmarks, such as GLUE and derived works, do not reveal test
sets on which the benchmarking platform calculates the ﬁnal results. Using static data splits leads to
over-ﬁtting and results in quick benchmark saturation. An alternative approach is based on multiple
splits(Gorman and Bedrick, 2020), allowing for evaluation of the model’s performance based on
many different data partitions. In our evaluation pipelines, we follow this methodology and use not
only a single train, dev, and test split but multiple splits. In our benchmark, we decided to implement
a new experiment to evaluate non-original splits in the next benchmark version.
Continuous benchmarking
The disadvantage of multi-task benchmarks such as GLUE, Super-
GLUE, KLEJ, etc., is their lack of dynamics. The static benchmarks become quickly outdated and,
therefore, useless from a practical perspective. As part of the CLARIN-PL-Biz 5, we plan to add
more datasets, tasks, and models and maintain LEPISZCZE benchmark continuously. We encourage
other associated researchers to publish datasets and models in our benchmark. Many LEPISZCZE
datasets have been added with their source and author contributions. We track all model parameters
and versions of each dataset. Hence, we can create a leaderboard for a speciﬁc version of the dataset
in our benchmark.
3.2
Datasets in the benchmark
In this section, we brieﬂy describe the ﬁnal collection of datasets selected for the initial version of
our benchmark. As of now, we also preserved the original splits of these datasets.
PAC — Polish Abusive Clauses Dataset
”I have read and agree to the terms and conditions” is
one of the biggest lies on the Internet. Consumers rarely read the contracts they are required to
accept. On the Internet, we probably skip most of the Terms and Conditions. However, we must
remember that we have concluded many more contracts. European consumer law aims to prevent
businesses from using so-called “unfair contractual terms” in their unilaterally drafted contracts,
requiring consumers to accept. The PAC aims to detect “unfair contractual term” as the equivalent of
an abusive clause. The task was formulated as binary text classiﬁcation. The dataset has been created
with the Ofﬁce of Competition and Consumer Protection. This dataset uses more than 700 contracts
and gathers 4,129 examples of abusive clauses and 5,127 non-abusive contract fragments.
It is worth noticing that the PAC dataset is important from an ethical point of view. Particularly it is
based on actual agreements. The Ofﬁce of Competition and Consumer Protection employees have
checked the dataset to see if it contains Personal Identiﬁable Information (PII). A couple of such
examples have been removed from the texts.
AspectEmo
Corpus (Koco´n et al., 2021) is an extended version of the publicly available PolEmo
2.0 corpus. The AspectEmo corpus consists of 1,465 online customer reviews from the following
domains: school, medicine, hotels, and products. All documents are annotated at the aspect level
with six sentiment categories: strong negative, weak negative, neutral, weakly positive, and strong
positive.
CDSC-E
Compositional Distributional Semantics Corpus (Wróblewska and Krasnowska-Kiera´s,
2017) is an entailment classiﬁcation task. It consists of 1000 pairs of sentences and human-annotated
entailment labels for each pair. There are three possible classes: entailment, contradiction, and
neutral.
Dialogue Acts — DiaBiz.Kom
It consists of 1,277,962 tokens in 1,104 transcribed call center
phone conversations spanning eight domains. Each example is annotated by three linguists (in a 2+1
system, with an inter-annotator agreement of Positive Speciﬁc Agreement equal to 0.78 for annotation
borders and categories and 0.86 for annotation borders) with dialogue acts in compliance with ISO
64217-2:2012 standard with layer of information concerning communicative functions. Within the
benchmark, we consider the task of dialogue act classiﬁcation, where each utterance is provided
with its role in the dialogue. DiaBiz.Kom is annotation layer on top of DiaBiz (P˛ezik et al., 2022) —
corpus of Polish call center dialogues.
5http://clarin-pl.eu/index.php/en/home/
6

--- Page 7 ---

DYK
Did You Know (pol. Czy wiesz?) is a dataset that consists of 4,721 human-annotated
question-answer pairs. It was simpliﬁed by (Rybak et al., 2020) to binary classiﬁcation to label
denoting if the answer contained in the Wikipedia article is factually correct in light of the stated
question.
KPWr-NER
is a part of the Polish Corpus of Wrocław University of Technology (Korpus J˛ezyka
Polskiego Politechniki Wrocławskiej) (Broda et al., 2012) is a named entity recognition dataset
focusing on ﬁne-grained categories of entities (82 classes) using BIO notation. It contains 13,959
training and 4,323 test human annotated sentences, originating from texts covering a large variety of
domains, genres, and sources.
NKJP-POS
is a part of the National Corpus of Polish (Narodowy Korpus J˛ezyka Polskiego)
(Przepiórkowski et al., 2012). Its objective is the part-of-speech tagging task. The dataset contains
85,663 sentences tagged with 35 tags. During the creation of the corpus, texts were annotated by
humans from various sources, covering many domains and genres.
PolEmo 2.0
(Koco´n et al., 2019) is a dataset of online consumer reviews from four domains:
medicine, hotels, products, and university. It consists of 8,216 reviews having 57,466 sentences. The
aim is to predict one of the sentiment classes: positive, negative, neutral, or ambiguous. During
the development of the KLEJ benchmark (Rybak et al., 2020) two tasks that differ in the context
used during evaluation have been created: in-domain and out-domain. In contrast, we preserved the
original data split and utilized all domains.
Political Advertising
dataset (Augustyniak et al., 2020) aims for detecting speciﬁc text chunks
and categories of political advertising in the Polish language. It contains 1,705 human-annotated
tweets tagged with nine categories, constituting campaigning under Polish electoral law. The authors
achieved 0.65 inter-annotator agreement (Cohen’s kappa score) for the sequence labeling task,
and they used an additional annotator to resolve the mismatches between the ﬁrst two annotators,
improving the ﬁnal consistency of annotations.
PSC
Polish Summaries Corpus (Ogrodniczuk and Kope´c, 2014) consists of 569 news summaries
done by human annotators. We used the simpliﬁed version developed by (Rybak et al., 2020) for
the purpose of the KLEJ benchmark. They formulated a binary paraphrase classiﬁcation task by
matching positive and negative pairs using the procedure detailed in the publication.
Punctuation Restoration
is a crowd-sourced text and audio dataset of Polish Wikipedia pages
read out loud by Polish lectors. The base dataset is divided into conversational (WikiTalks) and
information (WikiNews) parts. Then the texts were read by hundred people, which resulted in 36
hours of transcription. Punctuation restoration includes 1000 texts - 800 trains and 200 test examples.
This dataset is part of PolEval 2021 Competition 6.
4
Experiments
We conducted experiments on 13 datasets and ﬁve language models. Each language model was
ﬁne-tuned for a given dataset and was evaluated separately. Experiments were performed with our
developed library clarinpl-embeddings , which provides predeﬁned pipelines for text classiﬁca-
tion, text pairs classiﬁcation, and sequence labeling. To ensure reproducibility of our experiments,
we utilized MLOps tools: Data Version Control (DVC) (Kuprieiev et al., 2022) for pipelines and
tracking of datasets and models; Weight&Biases (Biewald, 2020) for experiments summaries and
metrics tracking. We share the code of our experiments on GitHub repository 7 and model tracking
dashboard 8.
6http://2021.poleval.pl/tasks/
7https://github.com/CLARIN-PL/LEPISZCZE
8https://wandb.ai/embeddings/LEPISZCZE
7

--- Page 8 ---

Table 1: Datasets available in the LEPISZCZE benchmark with sizes of the train, dev, and test sets.
The datasets that were previously incorporated into the KLEJ benchmark are marked with * symbol.
WIP denotes the dataset for which we present preliminary results.
Name
Domain
Task
Train
Dev
Test
#Classes
CDSC-E*
image captions
Entailment
Classiﬁcation
8000
1000
1000
3
DYK*
Wikipedia
Q&A Classiﬁcation
4154
0
1029
2
PolEmo 2.0
(In-Domain)*
online reviews
Sentiment Analysis
5783
723
722
4
PolEmo 2.0
(Out-Domain)*
online reviews
Sentiment Analysis
5783
494
494
4
PSC*
news
Paraphrase
Classiﬁcation
4302
0
1078
4
Abusive
Clauses
legal texts
Abusive Clauses Detection
4284
1519
3453
2
AspectEmo
online reviews
Aspect-based
Sentiment Analysis
1173
0
292
7
KPWr NER
misc.
NER
13959
0
4323
82
NKJP POS
misc.
POS Tagging
78219
0
7444
35
PolEmo 2.0
online reviews
Sentiment Analysis
6573
823
820
4
Political
Advertising
social media
Political Advertising
Detection
1020
340
341
9
Punctuation
Restoration
Wikipedia Talk,
Wikinews
Punctuation
Restoration
800
0
200
8
Dialogue Acts
(WIP)
call center phone
conversations
Dialogue Acts
Classiﬁcation
70454
8807
8807
54
4.1
Initial models for benchmark
We picked four recent transformer-based language models for Polish publicly available in the
HuggingFace hub, along with one multilingual XLM-RoBERTa model. We present those models
with their total number of parameters and repository location in Table 2. For ﬁne-tuning, we utilize
sequence and token classiﬁcation models from the transformers library (Wolf et al., 2020), consisting
of a single linear classiﬁcation layer with dropout. For the initial datasets evaluation, we chose both
cased and uncased versions of the language models.
Table 2: Language Models used for experiments. All models can be accessed via the HuggingFace
repository.
Model
#Params
HuggingFace Repository Name
PolBERT (base, cased), (Kłeczek, 2020)
132M
dkleczek/bert-base-polish-cased-v1
PolBERT (base, uncased), (Kłeczek, 2020)
132M
dkleczek/bert-base-polish-uncased-v1
HerBERT (base, cased)
(Mroczkowski et al., 2021)
124M
allegro/herbert-base-cased
HerBERT (large, cased)
(Mroczkowski et al., 2021)
355M
allegro/herbert-large-cased
XLM-RoBERTa (paraphrase)
(Reimers and Gurevych, 2019)
278M
sentence-transformers/paraphrase-
xlm-r-multilingual-v1
4.2
Hyper-parameter search (HPS)
To fairly compare different transformer models across various tasks, we performed a hyper-parameter
search (HPS) to obtain the best conﬁguration for ﬁne-tuning the language model to a particular
task. We performed a hyper-parameter search separately for each combination of tasks and language
models (which we restricted to 100 iterations). Under the hood, we utilized the Optuna framework
(Akiba et al., 2019) wrapper from the clarinpl-embeddings library. We also logged each run in
the hyper-parameter search via Weights&Biases PyTorch Lightning logger.
8

--- Page 9 ---

Experiments were computed using a server with ﬁve Titan RTX GPU cards. We logged over 6000
runs in the Weight&Biases dashboard, which took over 2000 hours to complete. We reported metrics,
hyper-parameters, dataset information, and package versions in each run.
We used macro averaged F1 measure as the metric for the objective function. Evaluation of models
in the hyper-parameter search stage was performed on the validation subset of the dataset. In case
validation subset was missing, we randomly sampled 10% of the training subset. After obtaining the
best hyper-parameter conﬁguration, we no longer need such a subset, so we use original subsets for
the ﬁnal model evaluation.
For each dataset and language model pair, we choose the best conﬁguration from the HPS process in
terms of the best F1-macro score on the validation subset. We retrain models ﬁve times and calculate
various metrics on test sets such as accuracy, precision, recall, and F1 with different averaging (micro,
macro, weighted) and class or tags metrics (accuracy, precision, recall, and F1).
4.3
Results of an initial set of trained models
Evaluation results are presented in Table 3, where we report macro averaged F1 metric for each dataset.
Other metrics results can be found in the appendix Section A.3. As we observe the performance of
models above 80% in text classiﬁcation datasets (except out-domain dataset), these models perform
poorly considering most sequence tagging tasks. Even the best performing model (HerBERT, large)
shows F1-macro around 39% for AspectEmo and 46% in Punctuation Restoration. Considering those
results, we can state that we still need better models that can cope with complex and under-represented
tasks. Multilingual models XLM-RoBERTa and HerBERT (large) are comparable only for one dataset
(around 2 percentage points difference for the Abusive Clauses dataset). However, for other tasks, the
gap is much bigger, and it fails even more in sequence tagging tasks with a difference of up to 70%.
We also reported preliminary results for Dialogue Acts classiﬁcation tasks. For the tested language
model, we achieved a comparable performance of about 50%. Considering limited computational
resources and ﬁne-tuning schemes, these results may be updated in our future work.
Table 3: Macro F1 performance of evaluated models on the test subsets. We present values as the
mean and standard deviations over 5 model retrains. The mean rank row is the average of a ranking
established on the mean of model retrains. Values marked with Bold present the best results for
a single dataset. Additionally, we indicate datasets previously appeared in the KLEJ benchmark with
*. WIP denotes the dataset for which we present preliminary results.
HerBERT
(base, cased)
HerBERT
(large, cased)
PolBERT
(base, cased)
PolBERT
(base,
uncased)
XLM-
RoBERTa
(paraphrase)
CDSC-E*
90.96 ± 0.73
90.48 ± 0.20
88.95 ± 0.31
90.62 ± 0.27
82.62 ± 0.88
DYK*
82.39 ± 1.43
79.58 ± 0.59
75.87 ± 0.98
74.41 ± 1.15
58.93 ± 7.98
PolEmo 2.0
In-Domain*
88.10 ± 0.36
88.34 ± 0.63
85.32 ± 0.45
85.71 ± 0.40
83.75 ± 0.45
PolEmo 2.0
Out-Domain*
57.31 ± 2.93
57.08 ± 2.03
54.10 ± 3.82
54.29 ± 1.83
45.12 ± 3.40
PSC*
97.90 ± 0.24
98.33 ± 0.69
98.95 ± 0.13
98.87 ± 0.10
58.85 ± 1.49
Abusive
Clauses
85.66 ± 0.58
86.57 ± 0.91
85.93 ± 0.66
85.74 ± 0.86
84.32 ± 0.71
AspectEmo
37.28 ± 0.71
39.44 ± 1.74
30.01 ± 0.58
31.48 ± 1.06
18.42 ± 0.98
KPWr NER
54.22 ± 0.76
52.68 ± 1.39
48.01 ± 0.76
40.21 ± 0.50
36.13 ± 0.44
NKJP POS
94.59 ± 0.56
96.14 ± 0.38
94.34 ± 0.61
94.54 ± 0.19
90.29 ± 0.51
PolEmo 2.0
86.78 ± 0.79
89.33 ± 0.49
85.89 ± 1.25
85.83 ± 0.47
84.12 ± 0.47
Political
Advertising
61.42 ± 1.38
62.16 ± 0.14
58.94 ± 1.92
62.52 ± 1.23
56.68 ± 0.94
Punctuation
Restoration
45.59 ± 0.38
46.68 ± 0.61
38.89 ± 0.91
41.31 ± 0.59
14.33 ± 1.94
Dialogue Acts
(WIP)
49.54 ± 0.74
51.11 ± 0.85
50.20 ± 1.32
48.87 ± 0.90
49.05 ± 0.39
Mean rank
2.15
1.62
3.23
3.08
4.92
9

--- Page 10 ---

5
Limitations
This study has potential limitations which are listed below. First, we do not give a human baseline
score to datasets in the benchmark as in SuperGLUE (Wang et al., 2019a). Second, in the initial
version of the benchmark, we do not solve the standard split problem and evaluate the model on
predeﬁned original splits, we work on the second batch of results with more focus on diversiﬁed splits.
Finally, due to practical constraints, the initial version of the benchmark does not include baselines
with static embeddings, but they will be added as well in the second batch of results. Our intention
is to keep the benchmark dynamic; we plan to add new datasets with various tasks which were not
covered in this version of the benchmark, including NLG tasks such as summarization or translation.
6
Conclusions and Future Work
In this paper, we have introduced LEPISZCZE , a new comprehensive benchmark for Polish NLP.
LEPISZCZE is characterized by the large variety of NLP tasks and high-quality operationalization of
the benchmark. The benchmarking approach is designed to maximize the ﬂexibility and portability
of other low-resourced languages. Adding new models, datasets, or NLP tasks is simple and intuitive.
The benchmark internally supports data versioning and model tracking for improved reproducibility.
In the ﬁrst run of the benchmark, we tested 13 experiments (task and dataset pairs) based on the ﬁve
most recent LMs for Polish to prove the usability and usefulness of LEPISZCZE .
An important added value of the paper is sharing our experiences collected during the work on the
benchmark. We hope that NLP researchers working on other low-resourced languages will ﬁnd our
comments and suggestions useful. Below we summarize the most important issues encountered
during our work on LEPISZCZE :
• multiple metrics: it is important to provide implementations of multiple metrics that can
be measured and compared across NLP tasks and datasets; evaluating language models on
a single metric produces a distorted view of models’ capabilities,
• diversity trumps openness: one should not refrain from including closed datasets in the
evaluation; they prevent over-ﬁtting (as LMs are unlikely to see these datasets during
training) and provide a good estimation of LM’s performance on difﬁcult tasks,
• include prediction costs: the quality of prediction as measured by traditional NLP metrics is
not enough, for the benchmark to be practically useful, one must be able to compare the
computational resources consumed by LMs as well,
• interface matters: making the benchmark interface simple and conventional hugely improves
its usefulness and the probability of wide adoption; in the space of NLP models, the
HuggingFace is the obvious choice of interface blueprints.
We plan to add more Natural Language Understanding and Spoken Language Understanding tasks to
the benchmark. We want to use our clarinpl-embeddings library to evaluate language models,
other contextual embeddings, and static word representations with simpler than transformer-based
models. The critical direction in the benchmark is to run experiments not only with the predeﬁned
data splits (Gorman and Bedrick, 2020) but also to use other splits to check the model’s robustness
properly. We hope that this benchmark will encourage the scientiﬁc community to work in transparent
and reproducible environments, leading to a rapid improvement of the current language technology
for the Polish language.
Acknowledgments and Disclosure of Funding
The work was partially supported by (1) the Polish Ministry of Education and Science, CLARIN-PL;
(2) the European Regional Development Fund as a part of the 2014-2020 Smart Growth Operational
Programme, CLARIN – Common Language Resources and Technology Infrastructure, (3) project
CLARIN-Q (agreement no. 2022/WK/09), and (4) the Department of Artiﬁcial Intelligence at
Wroclaw University of Science and Technology.
10

--- Page 11 ---

References
Takuya Akiba, Shotaro Sano, Toshihiko Yanase, Takeru Ohta, and Masanori Koyama. 2019. Optuna:
A next-generation hyperparameter optimization framework. In Proceedings of the 25th ACM
SIGKDD international conference on knowledge discovery & data mining, pages 2623–2631.
Lukasz Augustyniak, Krzysztof Rajda, Tomasz Kajdanowicz, and Michał Bernaczyk. 2020. Political
advertising dataset: the use case of the polish 2020 presidential elections. In Proceedings of the
The Fourth Widening Natural Language Processing Workshop, pages 110–114, Seattle, USA.
Association for Computational Linguistics.
Lukas Biewald. 2020. Experiment tracking with weights and biases. Software available from
wandb.com.
Zhang Bingyu and Nikolay Arefyev. 2022. The document vectors using cosine similarity revisited.
In Proceedings of the Third Workshop on Insights from Negative Results in NLP, pages 129–133,
Dublin, Ireland. Association for Computational Linguistics.
Pavel Blinov, Arina Reshetnikova, Aleksandr Nesterov, Galina Zubkova, and Vladimir Kokh.
2022. Rumedbench: A russian medical language understanding benchmark. arXiv preprint
arXiv:2201.06499.
Bartosz Broda, Michał Marci´nczuk, Marek Maziarz, Adam Radziszewski, and Adam Wardy´nski.
2012. KPWr: Towards a free corpus of Polish. In Proceedings of the Eighth International
Conference on Language Resources and Evaluation (LREC’12), pages 3218–3222, Istanbul,
Turkey. European Language Resources Association (ELRA).
Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan, Prafulla Dhariwal,
Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, Sandhini Agarwal, Ariel
Herbert-Voss, Gretchen Krueger, Tom Henighan, Rewon Child, Aditya Ramesh, Daniel M. Ziegler,
Jeffrey Wu, Clemens Winter, Christopher Hesse, Mark Chen, Eric Sigler, Mateusz Litwin, Scott
Gray, Benjamin Chess, Jack Clark, Christopher Berner, Sam McCandlish, Alec Radford, Ilya
Sutskever, and Dario Amodei. 2020. Language models are few-shot learners. Advances in Neural
Information Processing Systems, 2020-Decem(NeurIPS).
Samuel Cahyawijaya, Genta Indra Winata, Bryan Wilie, Karissa Vincentio, Xiaohong Li, Adhiguna
Kuncoro, Sebastian Ruder, Zhi Yuan Lim, Syafri Bahar, Masayu Khodra, et al. 2021. Indonlg:
Benchmark and resources for evaluating indonesian natural language generation. In Proceedings
of the 2021 Conference on Empirical Methods in Natural Language Processing, pages 8875–8898.
José Canete, Gabriel Chaperon, Rodrigo Fuentes, Jou-Hui Ho, Hojin Kang, and Jorge Pérez. 2022.
Spanish pre-trained bert model and evaluation data. In Proceedings of the Practical Machine
Learning for Developing Countries @ ICLR 2022.
Jiangjie Chen, Rui Xu, Ziquan Fu, Wei Shi, Zhongqiao Li, Xinbo Zhang, Changzhi Sun, Lei Li,
Yanghua Xiao, and Hao Zhou. 2022. E-kar: A benchmark for rationalizing natural language
analogical reasoning. In Findings of the Association for Computational Linguistics: ACL 2022,
pages 3941–3955.
Alexis Conneau and Douwe Kiela. 2018. Senteval: An evaluation toolkit for universal sentence
representations. arXiv preprint arXiv:1803.05449.
Stefan Daniel Dumitrescu, Petru Rebeja, Beata Lorincz, Mihaela Gaman, Andrei Avram, Mihai Ilie,
Andrei Pruteanu, Adriana Stan, Lorena Rosia, Cristina Iacobescu, et al. 2021. Liro: Benchmark
and leaderboard for romanian language tasks. In Thirty-ﬁfth Conference on Neural Information
Processing Systems Datasets and Benchmarks Track (Round 1).
Kawin Ethayarajh and Dan Jurafsky. 2020. Utility is in the eye of the user: A critique of NLP
leaderboards. In Proceedings of the 2020 Conference on Empirical Methods in Natural Language
Processing (EMNLP), pages 4846–4853, Online. Association for Computational Linguistics.
Zohreh Fallahnejad and Ali Zarezade. 2021. Persian nlp benchmark. https://github.com/
Mofid-AI/persian-nlp-benchmark#persian-nlp-benchmark.
11

--- Page 12 ---

Charles Fennig, David Eberhard, and Gary F. Simons, editors. 2022. Ethnologue: Languages of the
World, twenty-ﬁfth edition. SIL International, Dallas, TX, USA.
Sebastian Gehrmann, Tosin Adewumi, Karmanya Aggarwal, Pawan Sasanka Ammanamanchi, An-
uoluwapo Aremu, Antoine Bosselut, Khyathi Raghavi Chandu, Miruna-Adriana Clinciu, Dipanjan
Das, Kaustubh Dhole, et al. 2021. The gem benchmark: Natural language generation, its evaluation
and metrics. In Proceedings of the 1st Workshop on Natural Language Generation, Evaluation,
and Metrics (GEM 2021), pages 96–120.
J. R. S. Gomes. 2020. Plue: Portuguese language understanding evaluation. https://github.com/
jubs12/PLUE.
Kyle Gorman and Steven Bedrick. 2020. We need to talk about standard splits. ACL 2019 - 57th
Annual Meeting of the Association for Computational Linguistics, Proceedings of the Conference,
pages 2786–2791.
Jian Guan, Zhuoer Feng, Yamei Chen, Ruilin He, Xiaoxi Mao, Changjie Fan, and Minlie Huang. 2022.
Lot: A story-centric benchmark for evaluating chinese long text understanding and generation.
Transactions of the Association for Computational Linguistics, 10:434–451.
Jordan Hoffmann, Sebastian Borgeaud, Arthur Mensch, Elena Buchatskaya, Trevor Cai, Eliza
Rutherford, Diego de Las Casas, Lisa Anne Hendricks, Johannes Welbl, Aidan Clark, Tom
Hennigan, Eric Noland, Katie Millican, George van den Driessche, Bogdan Damoc, Aurelia Guy,
Simon Osindero, Karen Simonyan, Erich Elsen, Jack W. Rae, Oriol Vinyals, and Laurent Sifre.
2022. Training compute-optimal large language models.
Junjie Hu, Sebastian Ruder, Aditya Siddhant, Graham Neubig, Orhan Firat, and Melvin Johnson. 2020.
Xtreme: A massively multilingual multi-task benchmark for evaluating cross-lingual generalisation.
In International Conference on Machine Learning, pages 4411–4421. PMLR.
Divyanshu Kakwani, Anoop Kunchukuttan, Satish Golla, NC Gokul, Avik Bhattacharyya, Mitesh M
Khapra, and Pratyush Kumar. 2020. Indicnlpsuite: Monolingual corpora, evaluation benchmarks
and pre-trained multilingual language models for indian languages. In Findings of the Association
for Computational Linguistics: EMNLP 2020, pages 4948–4961.
Daniel Khashabi, Arman Cohan, Siamak Shakeri, Pedram Hosseini, Pouya Pezeshkpour, Malihe
Alikhani, Moin Aminnaseri, Marzieh Bitaab, Faeze Brahman, Sarik Ghazarian, et al. 2021. Parsinlu:
A suite of language understanding challenges for persian. Transactions of the Association for
Computational Linguistics, 9:1147–1162.
Douwe Kiela, Max Bartolo, Yixin Nie, Divyansh Kaushik, Atticus Geiger, Zhengxuan Wu, Bertie
Vidgen, Grusha Prasad, Amanpreet Singh, Pratik Ringshia, et al. 2021. Dynabench: Rethinking
benchmarking in nlp. In Proceedings of the 2021 Conference of the North American Chapter of
the Association for Computational Linguistics: Human Language Technologies, pages 4110–4124.
Dohyeong Kim, Myeongjun Jang, Deuk Sin Kwon, and Eric Davis. 2022. Kobest: Korean balanced
evaluation of signiﬁcant tasks. arXiv preprint arXiv:2204.04541.
Jan Koco´n, Piotr Miłkowski, and Monika Za´sko-Zieli´nska. 2019. Multi-level sentiment analysis of
PolEmo 2.0: Extended corpus of multi-domain consumer reviews. In Proceedings of the 23rd
Conference on Computational Natural Language Learning (CoNLL), pages 980–991, Hong Kong,
China. Association for Computational Linguistics.
Jan Koco´n, Jarema Radom, Ewa Kaczmarz-Wawryk, Kamil Wabnic, Ada Zaj ˛aczkowska, and Monika
Za´sko-Zieli´nska. 2021. Aspectemo: Multi-domain corpus of consumer reviews for aspect-based
sentiment analysis. 2021 International Conference on Data Mining Workshops (ICDMW), pages
166–173.
Fajri Koto, Afshin Rahimi, Jey Han Lau, and Timothy Baldwin. 2020. Indolem and indobert: A
benchmark dataset and pre-trained language model for indonesian nlp. In Proceedings of the 28th
International Conference on Computational Linguistics, pages 757–770.
12

--- Page 13 ---

Ruslan Kuprieiev, skshetry, Dmitry Petrov, Paweł Redzy´nski, Peter Rowlands, Casper da Costa-Luis,
Alexander Schepanovski, Ivan Shcheklein, Batuhan Taskaya, Gao, Jorge Orpinel, David de la
Iglesia Castro, Fábio Santos, Aman Sharma, Zhanibek, Dani Hodovic, Dave Berenbaum, Nikita
Kodenko, Andrew Grigorev, Earl, Nabanita Dash, daniele, George Vyshnya, maykulkarni, Max
Hora, Vera, Sanidhya Mangal, and Wojciech Baranowski. 2022. Dvc: Data version control - git for
data & models.
Dariusz Kłeczek. 2020. Polbert: Attacking polish nlp tasks with transformers. In Proceedings of the
PolEval 2020 Workshop. Institute of Computer Science, Polish Academy of Sciences.
Zhenzhong Lan, Mingda Chen, Sebastian Goodman, Kevin Gimpel, Piyush Sharma, and Radu
Soricut. 2020. Albert: A lite bert for self-supervised learning of language representations. In
International Conference on Learning Representations.
Hang Le, Loïc Vial, Jibril Frej, Vincent Segonne, Maximin Coavoux, Benjamin Lecouteux, Alexandre
Allauzen, Benoit Crabbé, Laurent Besacier, and Didier Schwab. 2020. Flaubert: Unsupervised
language model pre-training for french. In Proceedings of the 12th Language Resources and
Evaluation Conference, pages 2479–2490.
Xiaoya Li, Xiaofei Sun, Yuxian Meng, Junjun Liang, Fei Wu, and Jiwei Li. 2020. Dice loss for
data-imbalanced NLP tasks. In Proceedings of the 58th Annual Meeting of the Association for
Computational Linguistics, pages 465–476, Online. Association for Computational Linguistics.
Yaobo Liang, Nan Duan, Yeyun Gong, Ning Wu, Fenfei Guo, Weizhen Qi, Ming Gong, Linjun Shou,
Daxin Jiang, Guihong Cao, Xiaodong Fan, Ruofei Zhang, Rahul Agrawal, Edward Cui, Sining Wei,
Taroon Bharti, Ying Qiao, Jiun-Hung Chen, Winnie Wu, Shuguang Liu, Fan Yang, Daniel Campos,
Rangan Majumder, and Ming Zhou. 2020. XGLUE: A new benchmark datasetfor cross-lingual
pre-training, understanding and generation. In Proceedings of the 2020 Conference on Empirical
Methods in Natural Language Processing (EMNLP), pages 6008–6018, Online. Association for
Computational Linguistics.
Dayiheng Liu, Yu Yan, Yeyun Gong, Weizhen Qi, Hang Zhang, Jian Jiao, Weizhu Chen, Jie Fu,
Linjun Shou, Ming Gong, et al. 2021. Glge: A new general language generation evaluation
benchmark. In Findings of the Association for Computational Linguistics: ACL-IJCNLP 2021,
pages 408–420.
Bryan McCann, Nitish Shirish Keskar, Caiming Xiong, and Richard Socher. 2018. The natural
language decathlon: Multitask learning as question answering. arXiv preprint arXiv:1806.08730.
Robert Mroczkowski, Piotr Rybak, Alina Wróblewska, and Ireneusz Gawlik. 2021. HerBERT:
Efﬁciently pretrained transformer-based language model for Polish. In Proceedings of the 8th
Workshop on Balto-Slavic Natural Language Processing, pages 1–10, Kiyv, Ukraine. Association
for Computational Linguistics.
Maciej Ogrodniczuk and Mateusz Kope´c. 2014. The Polish summaries corpus. In Proceedings of
the Ninth International Conference on Language Resources and Evaluation (LREC’14), pages
3712–3715, Reykjavik, Iceland. European Language Resources Association (ELRA).
Sungjoon Park, Jihyung Moon, Sungdong Kim, Won Ik Cho, Jiyoon Han, Jangwon Park, Chisung
Song, Junseong Kim, Yongsook Song, Taehwan Oh, et al. 2021. Klue: Korean language under-
standing evaluation. arXiv preprint arXiv:2105.09680.
Matthew E. Peters, Mark Neumann, Mohit Iyyer, Matt Gardner, Christopher Clark, Kenton Lee, and
Luke Zettlemoyer. 2018. Deep contextualized word representations. In Proceedings of the 2018
Conference of the North American Chapter of the Association for Computational Linguistics: Hu-
man Language Technologies, Volume 1 (Long Papers), pages 2227–2237, New Orleans, Louisiana.
Association for Computational Linguistics.
Fabio Petroni, Aleksandra Piktus, Angela Fan, Patrick Lewis, Majid Yazdani, Nicola De Cao, James
Thorne, Yacine Jernite, Vladimir Karpukhin, Jean Maillard, et al. 2021. Kilt: a benchmark for
knowledge intensive language tasks. In Proceedings of the 2021 Conference of the North American
Chapter of the Association for Computational Linguistics: Human Language Technologies, pages
2523–2544.
13

--- Page 14 ---

Joelle Pineau, Philippe Vincent-Lamarre, Koustuv Sinha, Vincent Lariviére, Alina Beygelzimer,
Florence D’Alché-Buc, Emily Fox, and Hugo Larochelle. 2021. Improving reproducibility in
machine learning research (a report from the neurips 2019 reproducibility program). Journal of
Machine Learning Research, 22:1–20.
Adam Przepiórkowski, Mirosław Ba´nko, Rafał L. Górski, and Barbara Lewandowska-Tomaszczyk,
editors. 2012. Narodowy korpus j˛ezyka polskiego. Wydawnictwo Naukowe PWN.
Piotr P˛ezik, Gosia Krawentek, Sylwia Karasi´nska, Paweł Wilk, Paulina Rybi´nska, Angelika Peljak-
Łapi´nska, Anna Cichosz, Mikołaj Deckert, and Michał Adamczyk. 2022. Diabiz – an annotated
corpus of polish call center dialogs. In Language Resources and Evaluation Conference 2022.
European Language Resources Association (ELRA).
Jack W. Rae, Sebastian Borgeaud, Trevor Cai, Katie Millican, Jordan Hoffmann, Francis Song, John
Aslanides, Sarah Henderson, Roman Ring, Susannah Young, Eliza Rutherford, Tom Hennigan,
Jacob Menick, Albin Cassirer, Richard Powell, George van den Driessche, Lisa Anne Hendricks,
Maribeth Rauh, Po-Sen Huang, Amelia Glaese, Johannes Welbl, Sumanth Dathathri, Saffron
Huang, Jonathan Uesato, John Mellor, Irina Higgins, Antonia Creswell, Nat McAleese, Amy Wu,
Erich Elsen, Siddhant Jayakumar, Elena Buchatskaya, David Budden, Esme Sutherland, Karen
Simonyan, Michela Paganini, Laurent Sifre, Lena Martens, Xiang Lorraine Li, Adhiguna Kuncoro,
Aida Nematzadeh, Elena Gribovskaya, Domenic Donato, Angeliki Lazaridou, Arthur Mensch,
Jean-Baptiste Lespiau, Maria Tsimpoukelli, Nikolai Grigorev, Doug Fritz, Thibault Sottiaux,
Mantas Pajarskas, Toby Pohlen, Zhitao Gong, Daniel Toyama, Cyprien de Masson d’Autume,
Yujia Li, Tayfun Terzi, Vladimir Mikulik, Igor Babuschkin, Aidan Clark, Diego de Las Casas,
Aurelia Guy, Chris Jones, James Bradbury, Matthew Johnson, Blake Hechtman, Laura Weidinger,
Iason Gabriel, William Isaac, Ed Lockhart, Simon Osindero, Laura Rimell, Chris Dyer, Oriol
Vinyals, Kareem Ayoub, Jeff Stanway, Lorrayne Bennett, Demis Hassabis, Koray Kavukcuoglu,
and Geoffrey Irving. 2021. Scaling language models: Methods, analysis & insights from training
gopher.
Nils Reimers and Iryna Gurevych. 2019. Sentence-bert: Sentence embeddings using siamese bert-
networks. In Proceedings of the 2019 Conference on Empirical Methods in Natural Language
Processing. Association for Computational Linguistics.
Piotr Rybak, Robert Mroczkowski, Janusz Tracz, and Ireneusz Gawlik. 2020. Klej: Comprehensive
benchmark for polish language understanding. In Proceedings of the 58th Annual Meeting of the
Association for Computational Linguistics, pages 1191–1201.
Ali Safaya, Emirhan Kurtulu¸s, Arda Goktogan, and Deniz Yuret. 2022. Mukayese: Turkish nlp strikes
back. In Findings of the Association for Computational Linguistics: ACL 2022, pages 846–863.
Haitham Seelawi, Ibraheem Tuffaha, Mahmoud Gzawi, Wael Farhan, Bashar Talafha, Riham Badawi,
Zyad Sober, Oday Al-Dweik, Abed Alhakim Freihat, and Hussein Al-Natsheh. 2021. Alue:
Arabic language understanding evaluation. In Proceedings of the Sixth Arabic Natural Language
Processing Workshop, pages 173–184.
Tatiana Shavrina, Alena Fenogenova, Emelyanov Anton, Denis Shevelev, Ekaterina Artemova,
Valentin Malykh, Vladislav Mikhailov, Maria Tikhonova, Andrey Chertok, and Andrey Evlampiev.
2020. RussianSuperGLUE: A Russian language understanding evaluation benchmark. In Proceed-
ings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP),
pages 4717–4726, Online. Association for Computational Linguistics.
Alex Wang, Yada Pruksachatkun, Nikita Nangia, Amanpreet Singh, Julian Michael, Felix Hill, Omer
Levy, and Samuel Bowman. 2019a. Superglue: A stickier benchmark for general-purpose language
understanding systems. In Advances in Neural Information Processing Systems, volume 32. Curran
Associates, Inc.
Alex Wang, Yada Pruksachatkun, Nikita Nangia, Amanpreet Singh, Julian Michael, Felix Hill, Omer
Levy, and Samuel Bowman. 2019b. Superglue: A stickier benchmark for general-purpose language
understanding systems. Advances in neural information processing systems, 32.
14

--- Page 15 ---

Alex Wang, Amanpreet Singh, Julian Michael, Felix Hill, Omer Levy, and Samuel R Bowman. 2018.
Glue: A multi-task benchmark and analysis platform for natural language understanding. arXiv
preprint arXiv:1804.07461.
Lijie Wang, Yaozong Shen, Shuyuan Peng, Shuai Zhang, Xinyan Xiao, Hao Liu, Hongxuan Tang,
Ying Chen, Hua Wu, and Haifeng Wang. 2022. A ﬁne-grained interpretability evaluation benchmark
for neural nlp. arXiv preprint arXiv:2205.11097.
Qiong Wang, Zongcheng Ji, Jingqi Wang, Stephen Wu, Weiyan Lin, Wenzhen Li, Li Ke, Guohong
Xiao, Qing Jiang, Hua Xu, and Yi Zhou. 2020. A study of entity-linking methods for normal-
izing chinese diagnosis and procedure terms to icd codes. Journal of Biomedical Informatics,
105:103418.
Bryan Wilie, Karissa Vincentio, Genta Indra Winata, Samuel Cahyawijaya, Xiaohong Li, Zhi Yuan
Lim, Sidik Soleman, Rahmad Mahendra, Pascale Fung, Syafri Bahar, et al. 2020. Indonlu:
Benchmark and resources for evaluating indonesian natural language understanding. In Proceedings
of the 1st Conference of the Asia-Paciﬁc Chapter of the Association for Computational Linguistics
and the 10th International Joint Conference on Natural Language Processing, pages 843–857.
Thomas Wolf, Lysandre Debut, Victor Sanh, Julien Chaumond, Clement Delangue, Anthony Moi,
Pierric Cistac, Tim Rault, Remi Louf, Morgan Funtowicz, Joe Davison, Sam Shleifer, Patrick
von Platen, Clara Ma, Yacine Jernite, Julien Plu, Canwen Xu, Teven Le Scao, Sylvain Gugger,
Mariama Drame, Quentin Lhoest, and Alexander Rush. 2020. Transformers: State-of-the-art
natural language processing. In Proceedings of the 2020 Conference on Empirical Methods in
Natural Language Processing: System Demonstrations, pages 38–45, Online. Association for
Computational Linguistics.
Alina Wróblewska and Katarzyna Krasnowska-Kiera´s. 2017. Polish evaluation dataset for com-
positional distributional semantics models. In Proceedings of the 55th Annual Meeting of the
Association for Computational Linguistics (Volume 1: Long Papers), pages 784–792, Vancouver,
Canada. Association for Computational Linguistics.
Liang Xu, Hai Hu, Xuanwei Zhang, Lu Li, Chenjie Cao, Yudong Li, Yechen Xu, Kai Sun, Dian
Yu, Cong Yu, et al. 2020. Clue: A chinese language understanding evaluation benchmark. In
Proceedings of the 28th International Conference on Computational Linguistics, pages 4762–4772.
Liang Xu, Xiaojing Lu, Chenyang Yuan, Xuanwei Zhang, Huilin Xu, Hu Yuan, Guoao Wei, Xiang
Pan, Xin Tian, Libo Qin, et al. 2021. Fewclue: A chinese few-shot learning evaluation benchmark.
arXiv preprint arXiv:2107.07498.
Zhilin Yang, Zihang Dai, Yiming Yang, Jaime Carbonell, Russ R Salakhutdinov, and Quoc V Le.
2019. Xlnet: Generalized autoregressive pretraining for language understanding. In Advances in
Neural Information Processing Systems, volume 32. Curran Associates, Inc.
Yuan Yao, Qingxiu Dong, Jian Guan, Boxi Cao, Zhengyan Zhang, Chaojun Xiao, Xiaozhi Wang,
Fanchao Qi, Junwei Bao, Jinran Nie, et al. 2021. Cuge: A chinese language understanding and
generation evaluation benchmark. arXiv preprint arXiv:2112.13610.
Deming Ye, Yankai Lin, Peng Li, and Maosong Sun. 2022. Packed levitated marker for entity and
relation extraction. In Proceedings of the 60th Annual Meeting of the Association for Computa-
tional Linguistics (Volume 1: Long Papers), pages 4904–4917, Dublin, Ireland. Association for
Computational Linguistics.
Ningyu Zhang, Mosha Chen, Zhen Bi, Xiaozhuan Liang, Lei Li, Xin Shang, Kangping Yin, Chuanqi
Tan, Jian Xu, Fei Huang, et al. 2021. Cblue: A chinese biomedical language understanding
evaluation benchmark. arXiv preprint arXiv:2106.08087.
15

--- Page 16 ---

A
Appendix
A.1
Benchmarks
Table 4: Reviewed NLP benchmarks for languages with at least 10 million speakers. The benchmarks
are sorted by the language and name.
Name
# of tasks
Languages
ALUE (Seelawi et al., 2021)
6
Arabic
CBLUE (Zhang et al., 2021)
6
Chinese
CLUE (Xu et al., 2020)
7
Chinese
CUGE (Yao et al., 2021)
13
Chinese
FewCLUE (Xu et al., 2021)
7
Chinese
LOT (Guan et al., 2022)
3
Chinese
DecaNLP (McCann et al., 2018)
9
English
Dynabench (Kiela et al., 2021)
5
English
GLGE (Liu et al., 2021)
4
English
GLUE (Wang et al., 2018)
6
English
KILT (Petroni et al., 2021)
5
English
SentEval (Conneau and Kiela, 2018)
7
English
SuperGLUE (Wang et al., 2019b)
5
English
FLUE (Le et al., 2020)
7
French
IndicNLPSuite (Kakwani et al., 2020)
10
Indian
IndoNLG (Cahyawijaya et al., 2021)
4
Indonesian
IndoNLU (Wilie et al., 2020)
7
Indonesian
IndoLEM (Koto et al., 2020)
7
Indonesian
KLUE (Park et al., 2021)
8
Korean
KOBEST (Kim et al., 2022)
5
Korean
XGLUE (Liang et al., 2020)
9
Multilingual (13 languages)
GEM (Gehrmann et al., 2021)
9
Multilingual (15 languages)
XTREME (Hu et al., 2020)
6
Multilingual (17 languages)
E-KAR (Chen et al., 2022)
2
Multilingual (2 languages)
(Wang et al., 2022)
3
Multilingual (2 languages)
ParsiNLU (Khashabi et al., 2021)
6
Persian
Persian NLP Benchmark (Fallahnejad and Zarezade, 2021)
9
Persian
KLEJ (Rybak et al., 2020)
7
Polish
PLUE (Gomes, 2020)
6
Portugese
LiRO (Dumitrescu et al., 2021)
10
Romanian
RuMedBench (Blinov et al., 2022)
4
Russian
RussianSuperGLUE (Shavrina et al., 2020)
4
Russian
GLUES (Canete et al., 2022)
6
Spanish
SpanishGLUE (Canete et al., 2022)
7
Spanish
Mukayese (Safaya et al., 2022)
8
Turkish
16

--- Page 17 ---

A.2
Hyperparameter search
All hyperparameters used to create the ﬁrst version of benchmark are presented in Table 5. 5
Table 5: Hyperparameters for ﬁnetuning the language models.
Max. sequence length
512
Classiﬁer dropout
[0.0, 0.1, 0.2, 0.3, 0.4, 0.5]
No. ﬁnetuned layers
[0, 1, 2, 3, 4]
Learning rate
[1e-6, 5e-6, 1e-5, 5e-5, 1e-4, 5e-4, 1e-3, 5e-3]
Max. no. epochs
[2, 3, 5, 10, 15, 20]
Batch size
[16, 32, 64]
Optimizer
[Adam, AdamW]
Weight decay
[1e-4, 1e-3, 1e-2, 1e-1, 0]
Adam epsilon
[1e-8, 1e-7, 1e-6, 1e-5, 1e-4]
Use optimizer scheduler
[true, false]
Optimizer scheduler warmup steps
[0, 25, 50, 100, 200]
A.3
Metrics
In this section we provide other metrics that were calculated during experimental phase – tables 6 to
15.
Table 6: Accuracy performance of evaluated models on the test subsets. We present values as the
mean and standard deviations over 5 model retrains. The mean rank row is the average of a ranking
established on the mean of model retrains. Values marked with Bold present the best results for a
single dataset. Additionally, we indicate datasets previously appeared in the KLEJ benchmark with *.
WIP denotes the dataset for which we present preliminary results.
HerBERT
(base, cased)
HerBERT
(large, cased)
PolBERT
(base, cased)
PolBERT
(base,
uncased)
XLM-
RoBERTa
(paraphrase)
CDSC-E*
94.02 ± 0.33
93.92 ± 0.16
92.30 ± 0.25
93.48 ± 0.28
86.58 ± 0.68
DYK*
90.40 ± 0.78
87.66 ± 0.22
87.60 ± 0.64
86.82 ± 0.65
83.79 ± 0.88
PolEmo 2.0
In-Domain*
90.30 ± 0.28
90.55 ± 0.47
87.53 ± 0.43
87.59 ± 0.81
85.57 ± 0.46
PolEmo 2.0
Out-Domain*
75.06 ± 1.86
75.30 ± 1.69
69.31 ± 2.87
69.84 ± 1.34
57.69 ± 5.07
PSC*
98.22 ± 0.20
98.59 ± 0.57
99.11 ± 0.11
99.04 ± 0.08
73.99 ± 0.54
Abusive
Clauses
87.04 ± 0.54
88.01 ± 0.59
87.49 ± 0.58
87.13 ± 0.74
86.42 ± 0.38
AspectEmo
95.19 ± 0.07
95.27 ± 0.24
94.56 ± 0.11
94.65 ± 0.07
92.73 ± 0.25
KPWr NER
97.13 ± 0.05
97.25 ± 0.04
96.86 ± 0.04
95.90 ± 0.03
95.74 ± 0.03
NKJP POS
98.88 ± 0.02
98.98 ± 0.00
98.77 ± 0.02
98.79 ± 0.02
98.16 ± 0.02
PolEmo 2.0
88.20 ± 0.50
90.71 ± 0.40
87.05 ± 1.23
87.05 ± 0.50
85.22 ± 0.70
Political
Advertising
96.46 ± 0.21
96.49 ± 0.18
96.12 ± 0.09
96.38 ± 0.10
95.71 ± 0.08
Punctuation
Restoration
93.56 ± 0.08
94.10 ± 0.06
91.89 ± 0.26
92.38 ± 0.13
83.71 ± 0.19
Dialogue Acts
(WIP)
76.50 ± 0.21
77.08 ± 0.40
76.30 ± 0.25
76.16 ± 0.24
76.65 ± 0.75
Mean rank
2.23
1.31
3.42
3.27
4.77
17

--- Page 18 ---

Table 7: Micro F1 performance of evaluated models on the test subsets. We present values as the
mean and standard deviations over 5 model retrains. The mean rank row is the average of a ranking
established on the mean of model retrains. Values marked with Bold present the best results for a
single dataset. Additionally, we indicate datasets previously appeared in the KLEJ benchmark with *.
WIP denotes the dataset for which we present preliminary results.
HerBERT
(base, cased)
HerBERT
(large, cased)
PolBERT
(base, cased)
PolBERT
(base,
uncased)
XLM-
RoBERTa
(paraphrase)
CDSC-E*
94.02 ± 0.33
93.92 ± 0.16
92.30 ± 0.25
93.48 ± 0.28
86.58 ± 0.68
DYK*
90.40 ± 0.78
87.66 ± 0.22
87.60 ± 0.64
86.82 ± 0.65
83.79 ± 0.88
PolEmo 2.0
In-Domain*
90.30 ± 0.28
90.55 ± 0.47
87.53 ± 0.43
87.59 ± 0.81
85.57 ± 0.46
PolEmo 2.0
Out-Domain*
75.06 ± 1.86
75.30 ± 1.69
69.31 ± 2.87
69.84 ± 1.34
57.69 ± 5.07
PSC*
98.22 ± 0.20
98.59 ± 0.57
99.11 ± 0.11
99.04 ± 0.08
73.99 ± 0.54
Abusive
Clauses
87.04 ± 0.54
88.01 ± 0.59
87.49 ± 0.58
87.13 ± 0.74
86.42 ± 0.38
AspectEmo
58.18 ± 0.32
59.10 ± 1.32
50.82 ± 0.42
51.55 ± 0.98
34.07 ± 1.36
KPWr NER
76.90 ± 0.25
76.58 ± 0.67
72.59 ± 0.32
66.49 ± 0.09
61.57 ± 0.44
NKJP POS
98.88 ± 0.02
98.98 ± 0.00
98.77 ± 0.02
98.79 ± 0.02
98.16 ± 0.02
PolEmo 2.0
88.20 ± 0.50
90.71 ± 0.40
87.05 ± 1.23
87.05 ± 0.50
85.22 ± 0.70
Political
Advertising
68.02 ± 1.35
67.86 ± 0.88
65.25 ± 0.54
68.93 ± 1.31
60.94 ± 0.71
Punctuation
Restoration
73.23 ± 0.33
75.01 ± 0.23
66.49 ± 0.41
68.56 ± 0.39
21.72 ± 0.85
Dialogue Acts
(WIP)
76.50 ± 0.21
77.08 ± 0.40
76.30 ± 0.25
76.16 ± 0.24
76.65 ± 0.75
Mean rank
2.15
1.54
3.42
3.12
4.77
Table 8: Micro Precision performance of evaluated models on the test subsets. We present values
as the mean and standard deviations over 5 model retrains. The mean rank row is the average of a
ranking established on the mean of model retrains. Values marked with Bold present the best results
for a single dataset. Additionally, we indicate datasets previously appeared in the KLEJ benchmark
with *. WIP denotes the dataset for which we present preliminary results.
HerBERT
(base, cased)
HerBERT
(large, cased)
PolBERT
(base, cased)
PolBERT
(base,
uncased)
XLM-
RoBERTa
(paraphrase)
CDSC-E*
94.02 ± 0.33
93.92 ± 0.16
92.30 ± 0.25
93.48 ± 0.28
86.58 ± 0.68
DYK*
90.40 ± 0.78
87.66 ± 0.22
87.60 ± 0.64
86.82 ± 0.65
83.79 ± 0.88
PolEmo 2.0
In-Domain*
90.30 ± 0.28
90.55 ± 0.47
87.53 ± 0.43
87.59 ± 0.81
85.57 ± 0.46
PolEmo 2.0
Out-Domain*
75.06 ± 1.86
75.30 ± 1.69
69.31 ± 2.87
69.84 ± 1.34
57.69 ± 5.07
PSC*
98.22 ± 0.20
98.59 ± 0.57
99.11 ± 0.11
99.04 ± 0.08
73.99 ± 0.54
Abusive
Clauses
87.04 ± 0.54
88.01 ± 0.59
87.49 ± 0.58
87.13 ± 0.74
86.42 ± 0.38
AspectEmo
60.56 ± 0.99
61.07 ± 2.81
55.71 ± 1.16
56.05 ± 1.21
40.39 ± 2.12
KPWr NER
75.09 ± 0.37
73.85 ± 0.72
70.30 ± 0.34
64.48 ± 0.20
57.28 ± 0.46
NKJP POS
98.88 ± 0.02
98.98 ± 0.00
98.77 ± 0.02
98.79 ± 0.02
98.16 ± 0.02
PolEmo 2.0
88.20 ± 0.50
90.71 ± 0.40
87.05 ± 1.23
87.05 ± 0.50
85.22 ± 0.70
Political
Advertising
64.46 ± 2.95
64.07 ± 2.50
66.09 ± 2.36
68.18 ± 1.81
58.85 ± 2.23
Punctuation
Restoration
74.93 ± 0.33
77.33 ± 0.55
68.50 ± 2.34
70.64 ± 1.64
33.43 ± 1.44
Dialogue Acts
(WIP)
76.50 ± 0.21
77.08 ± 0.40
76.30 ± 0.25
76.16 ± 0.24
76.65 ± 0.75
Mean rank
2.23
1.62
3.27
3.12
4.77
18

--- Page 19 ---

Table 9: Micro Recall performance of evaluated models on the test subsets. We present values as the
mean and standard deviations over 5 model retrains. The mean rank row is the average of a ranking
established on the mean of model retrains. Values marked with Bold present the best results for a
single dataset. Additionally, we indicate datasets previously appeared in the KLEJ benchmark with *.
WIP denotes the dataset for which we present preliminary results.
HerBERT
(base, cased)
HerBERT
(large, cased)
PolBERT
(base, cased)
PolBERT
(base,
uncased)
XLM-
RoBERTa
(paraphrase)
CDSC-E*
94.02 ± 0.33
93.92 ± 0.16
92.30 ± 0.25
93.48 ± 0.28
86.58 ± 0.68
DYK*
90.40 ± 0.78
87.66 ± 0.22
87.60 ± 0.64
86.82 ± 0.65
83.79 ± 0.88
PolEmo 2.0
In-Domain*
90.30 ± 0.28
90.55 ± 0.47
87.53 ± 0.43
87.59 ± 0.81
85.57 ± 0.46
PolEmo 2.0
Out-Domain*
75.06 ± 1.86
75.30 ± 1.69
69.31 ± 2.87
69.84 ± 1.34
57.69 ± 5.07
PSC*
98.22 ± 0.20
98.59 ± 0.57
99.11 ± 0.11
99.04 ± 0.08
73.99 ± 0.54
Abusive
Clauses
87.04 ± 0.54
88.01 ± 0.59
87.49 ± 0.58
87.13 ± 0.74
86.42 ± 0.38
AspectEmo
56.01 ± 1.09
57.31 ± 0.95
46.74 ± 0.89
47.77 ± 1.76
29.59 ± 2.39
KPWr NER
78.80 ± 0.13
79.53 ± 0.64
75.05 ± 0.35
68.63 ± 0.10
66.55 ± 0.51
NKJP POS
98.88 ± 0.02
98.98 ± 0.00
98.77 ± 0.02
98.79 ± 0.02
98.16 ± 0.02
PolEmo 2.0
88.20 ± 0.50
90.71 ± 0.40
87.05 ± 1.23
87.05 ± 0.50
85.22 ± 0.70
Political
Advertising
72.09 ± 0.70
72.21 ± 1.17
64.53 ± 1.70
69.70 ± 1.12
63.30 ± 1.99
Punctuation
Restoration
71.61 ± 0.38
72.84 ± 0.81
64.70 ± 1.99
66.65 ± 1.74
16.10 ± 0.74
Dialogue Acts
(WIP)
76.50 ± 0.21
77.08 ± 0.40
76.30 ± 0.25
76.16 ± 0.24
76.65 ± 0.75
Mean rank
2.23
1.31
3.42
3.27
4.77
Table 10: Macro F1 performance of evaluated models on the test subsets. We present values as the
mean and standard deviations over 5 model retrains. The mean rank row is the average of a ranking
established on the mean of model retrains. Values marked with Bold present the best results for a
single dataset. Additionally, we indicate datasets previously appeared in the KLEJ benchmark with *.
WIP denotes the dataset for which we present preliminary results.
HerBERT
(base, cased)
HerBERT
(large, cased)
PolBERT
(base, cased)
PolBERT
(base,
uncased)
XLM-
RoBERTa
(paraphrase)
CDSC-E*
90.96 ± 0.73
90.48 ± 0.20
88.95 ± 0.31
90.62 ± 0.27
82.62 ± 0.88
DYK*
82.39 ± 1.43
79.58 ± 0.59
75.87 ± 0.98
74.41 ± 1.15
58.93 ± 7.98
PolEmo 2.0
In-Domain*
88.10 ± 0.36
88.34 ± 0.63
85.32 ± 0.45
85.71 ± 0.40
83.75 ± 0.45
PolEmo 2.0
Out-Domain*
57.31 ± 2.93
57.08 ± 2.03
54.10 ± 3.82
54.29 ± 1.83
45.12 ± 3.40
PSC*
97.90 ± 0.24
98.33 ± 0.69
98.95 ± 0.13
98.87 ± 0.10
58.85 ± 1.49
Abusive
Clauses
85.66 ± 0.58
86.57 ± 0.91
85.93 ± 0.66
85.74 ± 0.86
84.32 ± 0.71
AspectEmo
37.28 ± 0.71
39.44 ± 1.74
30.01 ± 0.58
31.48 ± 1.06
18.42 ± 0.98
KPWr NER
54.22 ± 0.76
52.68 ± 1.39
48.01 ± 0.76
40.21 ± 0.50
36.13 ± 0.44
NKJP POS
94.59 ± 0.56
96.14 ± 0.38
94.34 ± 0.61
94.54 ± 0.19
90.29 ± 0.51
PolEmo 2.0
86.78 ± 0.79
89.33 ± 0.49
85.89 ± 1.25
85.83 ± 0.47
84.12 ± 0.47
Political
Advertising
61.42 ± 1.38
62.16 ± 0.14
58.94 ± 1.92
62.52 ± 1.23
56.68 ± 0.94
Punctuation
Restoration
45.59 ± 0.38
46.68 ± 0.61
38.89 ± 0.91
41.31 ± 0.59
14.33 ± 1.94
Dialogue Acts
(WIP)
49.54 ± 0.74
51.11 ± 0.85
50.20 ± 1.32
48.87 ± 0.90
49.05 ± 0.39
Mean rank
2.15
1.62
3.23
3.08
4.92
19

--- Page 20 ---

Table 11: Macro Precision performance of evaluated models on the test subsets. We present values
as the mean and standard deviations over 5 model retrains. The mean rank row is the average of a
ranking established on the mean of model retrains. Values marked with Bold present the best results
for a single dataset. Additionally, we indicate datasets previously appeared in the KLEJ benchmark
with *. WIP denotes the dataset for which we present preliminary results.
HerBERT
(base, cased)
HerBERT
(large, cased)
PolBERT
(base, cased)
PolBERT
(base,
uncased)
XLM-
RoBERTa
(paraphrase)
CDSC-E*
92.24 ± 0.81
92.83 ± 0.69
89.91 ± 1.30
91.20 ± 0.92
80.18 ± 1.24
DYK*
83.47 ± 1.57
77.85 ± 0.34
78.90 ± 1.65
77.30 ± 1.94
66.03 ± 13.81
PolEmo 2.0
In-Domain*
89.40 ± 0.55
89.60 ± 0.95
85.99 ± 0.53
85.86 ± 0.95
83.86 ± 0.39
PolEmo 2.0
Out-Domain*
59.01 ± 1.95
59.29 ± 1.80
56.17 ± 2.23
56.94 ± 1.52
52.14 ± 2.03
PSC*
97.81 ± 0.23
98.42 ± 0.34
98.87 ± 0.11
98.64 ± 0.08
74.30 ± 0.90
Abusive
Clauses
84.94 ± 0.57
86.08 ± 0.46
85.54 ± 0.64
85.18 ± 0.71
84.99 ± 0.97
AspectEmo
40.08 ± 1.12
41.70 ± 3.99
43.69 ± 3.19
37.97 ± 3.17
23.57 ± 2.15
KPWr NER
55.97 ± 1.02
53.07 ± 1.77
50.45 ± 1.32
45.00 ± 1.25
36.64 ± 0.35
NKJP POS
95.91 ± 0.82
97.23 ± 0.38
96.59 ± 0.73
96.99 ± 0.23
92.50 ± 1.17
PolEmo 2.0
87.23 ± 0.43
90.04 ± 0.61
86.20 ± 1.38
86.09 ± 0.61
84.41 ± 0.82
Political
Advertising
58.82 ± 3.33
59.62 ± 1.33
60.89 ± 3.68
62.93 ± 1.75
54.68 ± 2.62
Punctuation
Restoration
49.48 ± 0.26
53.19 ± 0.97
46.22 ± 2.05
50.29 ± 6.67
23.85 ± 1.64
Dialogue Acts
(WIP)
52.83 ± 0.97
53.61 ± 1.10
52.38 ± 1.06
50.95 ± 1.10
52.47 ± 1.65
Mean rank
2.69
1.62
2.77
3.15
4.77
Table 12: Macro Recall performance of evaluated models on the test subsets. We present values
as the mean and standard deviations over 5 model retrains. The mean rank row is the average of a
ranking established on the mean of model retrains. Values marked with Bold present the best results
for a single dataset. Additionally, we indicate datasets previously appeared in the KLEJ benchmark
with *. WIP denotes the dataset for which we present preliminary results.
HerBERT
(base, cased)
HerBERT
(large, cased)
PolBERT
(base, cased)
PolBERT
(base,
uncased)
XLM-
RoBERTa
(paraphrase)
CDSC-E*
89.92 ± 0.94
88.51 ± 0.67
88.33 ± 1.09
90.15 ± 0.52
85.78 ± 1.95
DYK*
81.45 ± 1.58
81.95 ± 1.61
73.77 ± 0.94
72.52 ± 1.69
58.11 ± 5.10
PolEmo 2.0
In-Domain*
87.40 ± 0.33
87.62 ± 0.86
84.83 ± 0.56
85.75 ± 0.23
83.71 ± 0.67
PolEmo 2.0
Out-Domain*
60.99 ± 11.77
56.17 ± 1.53
71.26 ± 13.42
66.69 ± 13.84
42.76 ± 3.81
PSC*
98.00 ± 0.33
98.25 ± 1.02
99.03 ± 0.15
99.10 ± 0.15
59.35 ± 1.01
Abusive
Clauses
86.91 ± 1.09
87.37 ± 1.73
86.51 ± 1.04
87.01 ± 1.81
84.06 ± 1.76
AspectEmo
37.36 ± 0.72
39.80 ± 1.30
27.54 ± 0.69
29.80 ± 0.99
16.06 ± 1.17
KPWr NER
55.74 ± 0.71
55.52 ± 1.47
49.03 ± 0.55
40.81 ± 0.27
38.60 ± 0.47
NKJP POS
93.95 ± 0.64
95.39 ± 0.45
93.18 ± 0.50
93.28 ± 0.12
88.86 ± 0.33
PolEmo 2.0
86.50 ± 1.00
88.94 ± 0.39
85.68 ± 1.13
85.63 ± 0.40
83.95 ± 0.36
Political
Advertising
65.04 ± 1.05
65.60 ± 1.59
57.70 ± 1.62
62.72 ± 1.13
59.55 ± 1.23
Punctuation
Restoration
43.16 ± 0.36
43.56 ± 1.06
35.50 ± 1.27
38.11 ± 0.98
10.71 ± 1.90
Dialogue Acts
(WIP)
49.54 ± 1.16
51.79 ± 0.71
50.91 ± 1.45
49.58 ± 0.81
49.36 ± 0.84
Mean rank
2.38
1.62
3.31
2.77
4.92
20

--- Page 21 ---

Table 13: Weighted F1 performance of evaluated models on the test subsets. We present values
as the mean and standard deviations over 5 model retrains. The mean rank row is the average of a
ranking established on the mean of model retrains. Values marked with Bold present the best results
for a single dataset. Additionally, we indicate datasets previously appeared in the KLEJ benchmark
with *. WIP denotes the dataset for which we present preliminary results.
HerBERT
(base, cased)
HerBERT
(large, cased)
PolBERT
(base, cased)
PolBERT
(base,
uncased)
XLM-
RoBERTa
(paraphrase)
CDSC-E*
93.93 ± 0.32
93.80 ± 0.18
92.16 ± 0.24
93.42 ± 0.25
86.83 ± 0.54
DYK*
90.25 ± 0.79
88.08 ± 0.21
87.00 ± 0.58
86.20 ± 0.56
80.06 ± 2.89
PolEmo 2.0
In-Domain*
89.90 ± 0.28
90.20 ± 0.51
87.33 ± 0.45
87.64 ± 0.53
85.69 ± 0.40
PolEmo 2.0
Out-Domain*
75.61 ± 2.84
76.10 ± 2.67
69.68 ± 3.43
71.05 ± 1.20
60.33 ± 4.55
PSC*
98.22 ± 0.20
98.59 ± 0.58
99.11 ± 0.11
99.04 ± 0.08
68.62 ± 1.00
Abusive
Clauses
87.22 ± 0.51
88.11 ± 0.69
87.57 ± 0.57
87.29 ± 0.73
86.32 ± 0.46
AspectEmo
58.27 ± 0.40
59.16 ± 1.02
50.38 ± 0.39
51.50 ± 0.95
33.45 ± 1.42
KPWr NER
77.09 ± 0.24
77.02 ± 0.69
72.47 ± 0.27
65.97 ± 0.17
61.84 ± 0.47
NKJP POS
98.88 ± 0.02
98.98 ± 0.00
98.76 ± 0.02
98.79 ± 0.02
98.16 ± 0.02
PolEmo 2.0
88.02 ± 0.61
90.44 ± 0.41
86.99 ± 1.18
87.08 ± 0.49
85.17 ± 0.53
Political
Advertising
68.10 ± 1.34
68.10 ± 0.83
65.28 ± 0.56
68.89 ± 1.33
60.97 ± 0.61
Punctuation
Restoration
72.41 ± 0.30
73.77 ± 0.26
65.29 ± 0.48
67.29 ± 0.38
21.44 ± 0.78
Dialogue Acts
(WIP)
75.57 ± 0.30
76.03 ± 0.18
75.43 ± 0.25
75.21 ± 0.21
75.59 ± 0.59
Mean rank
2.19
1.5
3.46
3.08
4.77
Table 14: Weighted Precision performance of evaluated models on the test subsets. We present values
as the mean and standard deviations over 5 model retrains. The mean rank row is the average of a
ranking established on the mean of model retrains. Values marked with Bold present the best results
for a single dataset. Additionally, we indicate datasets previously appeared in the KLEJ benchmark
with *. WIP denotes the dataset for which we present preliminary results.
HerBERT
(base, cased)
HerBERT
(large, cased)
PolBERT
(base, cased)
PolBERT
(base,
uncased)
XLM-
RoBERTa
(paraphrase)
CDSC-E*
93.98 ± 0.36
93.90 ± 0.16
92.21 ± 0.24
93.43 ± 0.29
87.47 ± 0.67
DYK*
90.16 ± 0.81
88.78 ± 0.50
86.78 ± 0.64
85.98 ± 0.64
78.95 ± 5.62
PolEmo 2.0
In-Domain*
89.90 ± 0.31
90.22 ± 0.57
87.27 ± 0.48
87.84 ± 0.32
85.86 ± 0.37
PolEmo 2.0
Out-Domain*
77.90 ± 2.30
78.62 ± 2.63
72.96 ± 2.41
74.62 ± 1.55
69.00 ± 2.77
PSC*
98.23 ± 0.20
98.60 ± 0.56
99.11 ± 0.11
99.05 ± 0.09
74.15 ± 0.69
Abusive
Clauses
87.83 ± 0.67
88.46 ± 0.93
87.81 ± 0.55
88.05 ± 1.07
86.55 ± 0.42
AspectEmo
61.79 ± 1.23
62.07 ± 2.14
56.96 ± 1.27
57.36 ± 1.69
39.70 ± 1.43
KPWr NER
76.43 ± 0.35
75.60 ± 0.74
71.13 ± 0.25
65.41 ± 0.30
58.98 ± 0.43
NKJP POS
98.88 ± 0.02
98.99 ± 0.00
98.77 ± 0.02
98.80 ± 0.02
98.16 ± 0.02
PolEmo 2.0
87.98 ± 0.60
90.41 ± 0.43
87.00 ± 1.11
87.18 ± 0.46
85.22 ± 0.50
Political
Advertising
64.97 ± 3.06
64.93 ± 2.40
66.61 ± 2.34
68.50 ± 1.87
59.17 ± 2.21
Punctuation
Restoration
73.94 ± 0.27
76.80 ± 0.49
67.80 ± 1.84
69.84 ± 1.76
32.96 ± 1.15
Dialogue Acts
(WIP)
75.96 ± 0.47
76.30 ± 0.34
75.75 ± 0.55
75.20 ± 0.27
75.99 ± 0.86
Mean rank
2.15
1.62
3.46
3.0
4.77
21

--- Page 22 ---

Table 15: Weighted Recall performance of evaluated models on the test subsets. We present values
as the mean and standard deviations over 5 model retrains. The mean rank row is the average of a
ranking established on the mean of model retrains. Values marked with Bold present the best results
for a single dataset. Additionally, we indicate datasets previously appeared in the KLEJ benchmark
with *. WIP denotes the dataset for which we present preliminary results.
HerBERT
(base, cased)
HerBERT
(large, cased)
PolBERT
(base, cased)
PolBERT
(base,
uncased)
XLM-
RoBERTa
(paraphrase)
CDSC-E*
94.02 ± 0.33
93.92 ± 0.16
92.30 ± 0.25
93.48 ± 0.28
86.58 ± 0.68
DYK*
90.40 ± 0.78
87.66 ± 0.22
87.60 ± 0.64
86.82 ± 0.65
83.79 ± 0.88
PolEmo 2.0
In-Domain*
90.30 ± 0.28
90.55 ± 0.47
87.53 ± 0.43
87.59 ± 0.81
85.57 ± 0.46
PolEmo 2.0
Out-Domain*
75.06 ± 1.86
75.30 ± 1.69
69.31 ± 2.87
69.84 ± 1.34
57.69 ± 5.07
PSC*
98.22 ± 0.20
98.59 ± 0.57
99.11 ± 0.11
99.04 ± 0.08
73.99 ± 0.54
Abusive
Clauses
87.04 ± 0.54
88.01 ± 0.59
87.49 ± 0.58
87.13 ± 0.74
86.42 ± 0.38
AspectEmo
56.01 ± 1.09
57.31 ± 0.95
46.74 ± 0.89
47.77 ± 1.76
29.59 ± 2.39
KPWr NER
78.80 ± 0.13
79.53 ± 0.64
75.05 ± 0.35
68.63 ± 0.10
66.55 ± 0.51
NKJP POS
98.88 ± 0.02
98.98 ± 0.00
98.77 ± 0.02
98.79 ± 0.02
98.16 ± 0.02
PolEmo 2.0
88.20 ± 0.50
90.71 ± 0.40
87.05 ± 1.23
87.05 ± 0.50
85.22 ± 0.70
Political
Advertising
72.09 ± 0.70
72.21 ± 1.17
64.53 ± 1.70
69.70 ± 1.12
63.30 ± 1.99
Punctuation
Restoration
71.61 ± 0.38
72.84 ± 0.81
64.70 ± 1.99
66.65 ± 1.74
16.10 ± 0.74
Dialogue Acts
(WIP)
76.50 ± 0.21
77.08 ± 0.40
76.30 ± 0.25
76.16 ± 0.24
76.65 ± 0.75
Mean rank
2.23
1.31
3.42
3.27
4.77
22

```
