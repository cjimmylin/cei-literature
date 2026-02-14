---
title: "2025-Ghorbanpour-Data-Efficient Hate Speech Detection via Cross-Lingual ... - PDF Extract"
source_pdf: "2025-Ghorbanpour-Data-Efficient Hate Speech Detection via Cross-Lingual ....pdf"
pages: 16
extracted_at: "2026-02-13T13:57:14.578514"
---

# PDF Extract: 2025-Ghorbanpour-Data-Efficient Hate Speech Detection via Cross-Lingual ...

**Source PDF:** 2025-Ghorbanpour-Data-Efficient Hate Speech Detection via Cross-Lingual ....pdf
**Total Pages:** 16

---

## Content

```
--- Page 1 ---

arXiv:2505.14272v2  [cs.CL]  24 May 2025
Data-Efficient Hate Speech Detection via Cross-Lingual Nearest Neighbor
Retrieval with Limited Labeled Data
Faeze Ghorbanpour1,2
Daryna Dementieva1
Alexander Fraser1,2
1School of Computation, Information and Technology, TU Munich
2Munich Center for Machine Learning (MCML)
faeze.ghorbanpour@tum.de, daryna.dementieva@tum.de
Abstract
Considering the importance of detecting hateful
language, labeled hate speech data is expensive
and time-consuming to collect, particularly for
low-resource languages. Prior work has demon-
strated the effectiveness of cross-lingual trans-
fer learning and data augmentation in improv-
ing performance on tasks with limited labeled
data. To develop an efficient and scalable cross-
lingual transfer learning approach, we leverage
nearest-neighbor retrieval to augment minimal
labeled data in the target language, thereby en-
hancing detection performance. Specifically,
we assume access to a small set of labeled train-
ing instances in the target language and use
these to retrieve the most relevant labeled ex-
amples from a large multilingual hate speech
detection pool. We evaluate our approach on
eight languages and demonstrate that it con-
sistently outperforms models trained solely on
the target language data. Furthermore, in most
cases, our method surpasses the current state-
of-the-art. Notably, our approach is highly data-
efficient, retrieving as small as 200 instances in
some cases while maintaining superior perfor-
mance. Moreover, it is scalable, as the retrieval
pool can be easily expanded, and the method
can be readily adapted to new languages and
tasks. We also apply maximum marginal rel-
evance to mitigate redundancy and filter out
highly similar retrieved instances, resulting in
improvements in some languages.1,2
1
Introduction
Hate speech, abusive language targeting specific
groups (R¨ottger et al., 2021), is a global issue.
However, most detection advancements focus on
English due to the abundance of labeled datasets
(Poletto et al., 2021; Yin and Zubiaga, 2021). In
contrast, languages like Spanish, French, and Ital-
ian, though not low-resource for other tasks, lack
annotated hate speech datasets (Poletto et al., 2021),
1The pool and code will be made publicly available.
2This paper contains examples of hateful language.
limiting model effectiveness in detecting and ad-
dressing hate speech.
Collecting and annotating data for low-resource
languages is an effective solution, especially for
capturing linguistic and cultural nuances in hate
speech (Pelicon et al., 2021; Aluru et al., 2020a).
As R¨ottger et al. (2022) state, having some labeled
data in the target language is crucial for model ef-
fectiveness. However, while obtaining more data
can improve performance, this requires paying high
annotation costs (ElSherief et al., 2021) and ex-
poses annotators to harmful content (AlEmadi and
Zaghouani, 2024).
Transfer learning, especially from high-resource
languages like English, helps mitigate data scarcity
and improve detection performance (Bigoulaeva
et al., 2022; Firmino et al., 2024). However, the
choice of source tasks and languages remains cru-
cial. Some languages are useful for specific target
languages due to cultural similarities (Zhou et al.,
2023), and certain source tasks may be more use-
ful for particular target tasks (R¨ottger et al., 2022;
Antypas and Camacho-Collados, 2023).
Training on all available hate speech datasets
may seem beneficial, but is often inefficient, com-
putationally costly, and does not guarantee better
performance (Caselli et al., 2020). It can introduce
redundancy, dataset-specific biases, and annotation
inconsistencies, leading to overfitting (Wiegand
et al., 2019; Fortuna and Nunes, 2018). Moreover,
this approach lacks scalability, requiring frequent
retraining for new datasets (Vidgen et al., 2021a).
To address the mentioned problems, we propose
a novel method based on cross-lingual nearest-
neighbor retrieval. Our approach, pictured in Fig-
ure 1, retrieves a minimal yet relevant set of in-
stances and integrates them with the target lan-
guage training set for fine-tuning. Specifically, we
embed all available instances from fourteen tasks
using a multilingual sentence embedding model to
create a pool of hate speech detection samples. A

--- Page 2 ---

Figure 1: Overview of the proposed method. Given a small number of examples from a target language, we search
in a large pool of multilingual data for closely related instances. We then combine the retrieved instances with the
target language data and train a multilingual model on them for hate speech detection.
retrieval system selects the most relevant instances
from the multilingual pool based on their distance
to the target language training set. These retrieved
instances are then combined with the target training
data to fine-tune a language model (LM).
This solution addresses multiple challenges.
First, retrieving from a multilingual pool elimi-
nates the need to manually select source tasks or
languages. Second, it enhances efficiency by re-
trieving only a small number of relevant samples,
avoiding redundancy through distance-based re-
trieval. Third, it ensures scalability, as the multilin-
gual pool can be easily expanded with new datasets
and languages. Our method improves cross-lingual
transfer learning by considering linguistic and se-
mantic similarities in hate speech across languages.
We evaluate the proposed method on eight lan-
guages, including German, French, Spanish, Italian,
Portuguese, Hindi, Arabic, and Turkish, simulating
a scenario where only a limited number of training
examples (ranging from 10 to 2,000) are available.
Fine-tuning on a combination of retrieved data and
the target language training set significantly outper-
formed fine-tuning solely on the target training set
across all languages. Further, our method outper-
formed the state-of-the-art work in most languages
while fine-tuning with fewer samples. To refine the
retrieved data, we also experiment with applying
maximum marginal relevance (MMR) (Carbonell
and Goldstein, 1998) to remove highly similar in-
stances, leading to improved performance in some
languages. Our contributions are as follows:
• We propose a novel, efficient, and scalable
method for enhancing limited labeled hate
speech datasets by retrieving cross-lingual
samples using a retrieval system.
• We evaluate our method on eight languages,
demonstrating consistently higher perfor-
mance compared to training solely on the tar-
get language training set.
• Our approach is particularly effective in ex-
tremely low-resource settings, with fewer than
50 labeled instances, achieving up to 10% F1-
macro improvement in some cases.
2
Related Work
Hate Speech Detection with Limited Labeled
Data:
Hate speech violates human rights, dis-
rupts social peace, incites violence, and promotes
discrimination in all societies, regardless of lan-
guage. Detecting it is crucial to prevent conflict and
protect mental health and societal safety (Wilson,
2019; Narula and Chaudhary, 2024). Most datasets
and research efforts focus on English (Toraman
et al., 2022; Kennedy et al., 2020b; Vidgen et al.,
2021b), while languages like Spanish, Portuguese,
or Ukrainian have very limited resources. Accord-
ing to the Hate Speech Dataset Catalogue, these
languages each have only one available dataset with
fewer than 5,000 samples, which are also restricted
in context and domain (Basile et al., 2019; For-
tuna et al., 2019; Dementieva et al., 2024). Due

--- Page 3 ---

to limited resources, recent research increasingly
leverages other languages to improve hate speech
detection in low-resource settings.
Cross-lingual Transfer Learning for Hate
Speech Detection: Cross-lingual transfer learn-
ing has been widely studied in NLP, showing that
models trained on high-resource languages can
improve performance in low-resource languages
(Parovic et al., 2023; Muraoka et al., 2023; Pham
et al., 2024). This makes it a promising approach
for hate speech detection in low-resource settings.
Early methods used multilingual embeddings for
zero-shot and few-shot transfer from resource-rich
to resource-poor languages (Aluru et al., 2020b;
Pamungkas and Patti, 2019). Also, Bigoulaeva
et al. (2021) and Monnar et al. (2024) utilized
bilingual embeddings to transfer knowledge from
high-resource languages, showing promising re-
sults even without labeled data in target languages
but mainly benefiting closely related languages.
Data augmentation strategies, including cross-
lingual paraphrasing or translation-based methods,
have also been shown to alleviate data scarcity
(Pamungkas et al., 2021; Beddiar et al., 2021),
but these approaches are often constrained by the
availability and quality of translation resources.
Roychowdhury and Gupta (2023) employed data
augmentation with EasyMixup and reframed the
task as textual entailment, achieving improvements
but still relying on potentially noisy augmented
data. Hashmi et al. (2025), Gharoun et al. (2024),
and Mozafari et al. (2022) use meta-learning ap-
proaches specialized for bilingual contexts. While
effective, these methods require extensive labeled
bilingual data, are complex to implement and train,
and often demand substantial computational re-
sources, making them less scalable.
R¨ottger et al. (2022) showed that minimal target-
language data and initial English fine-tuning im-
prove performance. However, selecting an appro-
priate intermediate English task is challenging and
language-dependent. Building on this, Goldzy-
cher et al. (2023) uses an intermediate natural lan-
guage inference (NLI) task, which adds training
steps and requires more computation. Unlike prior
approaches, our method eliminates the need for
large-scale target-language annotation, intermedi-
ate tasks, or translation resources. Directly lever-
aging semantic similarity at the instance level en-
ables effective transfer with minimal target data
and avoids costly cross-lingual training pipelines.
Retrieval-based and Instance attribution Fine-
tuning methods: Prior work has shown that cross-
task retrieval-based data can improve generaliza-
tion in LMs (Guu et al., 2020; Khandelwal et al.,
2020). Shi et al. (2022) applied retrieval to classifi-
cation tasks via heuristic label mapping, whereas
we fine-tune directly on nearest neighbors. Das and
Khetan (2024) introduces data-efficient fine-tuning
through unsupervised core-set selection, showing
strong results in monolingual text-editing tasks.
However, this method is not designed for cross-
lingual transfer and depends on clustering quality.
Our approach is similar to Lin et al. (2022) and
Ivison et al. (2023) in using nearest neighbor re-
trieval and further fine-tuning, but is uniquely ap-
plied to multilingual datasets and leverages labeled
hate speech data. Our method uses instance attri-
bution, identifying relevant training examples for
a data point, unlike prior work (Pruthi et al., 2020;
Han and Tsvetkov, 2022), which used gradient-
based instance attribution to interpret neural net-
work predictions. Our neighbor identification ap-
proach is simpler as it avoids gradient computations
and reliance on labels, and is applied in a multilin-
gual, low-resource setting.
3
Methodology
Building on a large pool of labeled multilingual
hate speech data, our core hypothesis is that cer-
tain instances in this pool are more relevant to a
given target language than others. For each target
language, we assume access to a small amount of la-
beled data. The goal is to identify a relevant subset
of source data that, when used for training, yields
better performance. Initially, we employ an embed-
ding mode (Embedder) to encode instances from
multiple source languages. We then use a retrieval
module (Indexer) to index the resulting embedding
vectors and construct a pool of multilingual hate
speech detection instances.
When detecting hate speech in a low-resource
target language, the objective is to fine-tune an LM
for effective and efficient classification, as depicted
in Figure 1. We begin by embedding the target lan-
guage instances using the same embedding model.
The retrieval module (Retriever) then searches the
pool to find the nearest neighbors of the target in-
stances. We combine the retrieved data with the
target data and use the combined set to fine-tune
(Fine-tuner) an LM to classify them as Hate or
Non-Hate. Each module is described below.

--- Page 4 ---

3.1
Embedder and Indexer
Assume a source language3 A with a set of n text in-
stances Xs = {xs
1, xs
2, . . . , xs
n} and corresponding
labels Y s ∈{0, 1}, where 1 indicates hate speech
and 0 indicates non-hate speech. The objective of
this module is to project the input texts into a vector
space V s = {vs
1, vs
2, . . . , vs
n}, where each vector
vs
i is obtained by applying an embedding function:
vs
i = embedding(xs
i). These embeddings are then
passed to the retrieval module, which indexes the
vectors to enable efficient similarity search. This
indexed embedding space serves as the foundation
for retrieving relevant instances.
3.2
Retriever
Consider a target language B with a limited set of
labeled data Xt = {xt
1, xt
2, . . . , xt
m}, where m ≪
n (m and n denote the number of target and source
language instances, respectively.), and a label set
Y t ∈{0, 1}, where 1 denotes hate speech and 0
denotes non-hate speech (the same label set as the
source language). Similar to the source language,
we apply the embedding module to convert the
target language instances into a numerical vector
space V t = {vt
1, vt
2, . . . , vt
m}, where each vector
is computed as vt
i = embedding(xt
i).
The retrieval module is then employed to find rel-
evant samples from the pool using a nearest neigh-
bor search. Specifically, we want to retrieve a to-
tal of R instances from the source pool based on
Euclidean distance between the embedded target
vectors V t and the source vectors V s. The dis-
tance between an embedded target instance vt
i and
a source instance vs
j is calculated as:
dist(vt
i, vs
j) = ∥vt
i −vs
j∥2 =
v
u
u
t
d
X
k=1
(vt
i,k −vs
j,k)2
Where d is the dimensionality of the embedding
space. We then select the top k nearest neighbors
for each vt
i, and define the full retrieval set as:
R =
m
[
i=1
TopK(vt
i, V s, k)
where TopK(v′
i, V s, k) denotes the set of k
source vectors in V s with the lowest distance to vt
i.
3For clarity, we describe the approach using a single source
language. In practice, however, our methodology incorporates
multiple source languages—eight in total.
The set R contains up to m × k total retrieved in-
stances. We then map the vectors in R back to their
corresponding original texts using the retrieval in-
dex (Xs
r = {xs
r1, xs
r2, xs
r3, . . . , xs
rR}). Finally, we
apply deduplication to remove exact textual dupli-
cates. If the final count of unique instances falls
short of R, the retrieval process continues until the
desired number is reached.
3.3
Fine-tuner
In the fine-tuning module, we combine the retrieved
texts (Xs
r) with the training data from the target lan-
guage (Xt). The combined dataset is then used to
fine-tune a pre-trained LM (M) to perform binary
classification. Since the source and target tasks
share the same label space, i.e., Y s, Y t = {0, 1},
where 0 denotes non-hate and 1 denotes hate, joint
training of the fine-tuned model on the combined
source and target data is well-defined and coherent.
We define the final training set as D = Xs
r ∪Xt.
The model is fine-tuned by minimizing the binary
cross-entropy loss:
L = −1
|D|
X
(x,y)∈D
h
y log M(x)
+ (1 −y) log (1 −M(x))
i
4
Experimental Setup
4.1
Datasets
We use six large-scale English hate speech detec-
tion datasets as well as eight non-English ones.
These datasets were selected based on two crite-
ria: (a) the presence of explicit hate speech labels,
and (b) the use of annotation guidelines that align
with, or are closely related to, the definition of hate
speech adopted in this study. The English datasets
are: Dyn21 en (Vidgen et al., 2021b), Fou18 en
(Founta et al., 2018), Ken20 en (Kennedy et al.,
2020a), HateXplain (Mathew et al., 2021), Im-
plicit hate (ElSherief et al., 2021), and Xdomain en
(Toraman et al., 2022).
The non-English target tasks are: Bas19 es
(Basile et al., 2019), For19 pt (Fortuna et al.,
2019), Has21 hi (Mandl et al., 2021), Our19 ar
and Our19 fr (Ousidhoum et al., 2019), San20 it
(Sanguinetti et al., 2020), Xdomain tr (Toraman
et al., 2022), and Gahd24 de (Goldzycher et al.,
2024). The two-character language codes in dataset
names indicate the language of the task. More infor-
mation about datasets is provided in Appendix A.

--- Page 5 ---

Although all datasets are embedded and included
in the shared retrieval pool, we ensure that, for
each non-English target task, instances from the
same language are excluded from retrieval. This
guarantees that the target language data remains
unseen during its own retrieval process. Addition-
ally, we exclude Dyn21 en when the target task is
Gahd24 de because the latter includes translations
from the former. We also exclude Xdomain en
when the target task is Xdomain tr, as both orig-
inate from the same source. After constructing
the multilingual pool, we obtain approximately
265,671 instances, of which 37.15% are labeled as
hateful. The majority of data in the pool is English
(66.99%), Turkish (17.0%), and German (3.84%).
4.2
Models
For embedding the text instances, we utilized the
BAAI/bge-m3 multilingual encoder model (Chen
et al., 2024) using the Sentence Transformers li-
brary (Reimers and Gurevych, 2020). This model
generates 1024-dimensional vector representations
for each input text.
We use the FAISS library
(Douze et al., 2024; Johnson et al., 2021) to in-
dex dense vectors and perform a similarity search.
For retrieval, we adopt the Hierarchical Naviga-
ble Small World (HNSW) algorithm (Malkov and
Yashunin, 2020) as an efficient approximation of
the k-nearest neighbor search. Throughout all our
experiments for the classification model, we fine-
tune and evaluate XLM-T (Barbieri et al., 2022)
using the HuggingFace Transformers library (Wolf
et al., 2020). XLM-T is a variant of XLM-R (Con-
neau et al., 2020), further pre-trained on 198 mil-
lion multilingual Twitter posts to better capture
social media language patterns. Further details on
hyperparameters and experimental settings are pro-
vided in Appendix B.
4.3
Evaluation Details
We simulate low-resource conditions by using 12
different training subset sizes per each non-English
language: 10, 20, 30, 40, 50, 100, 200, 300, 400,
500, 1,000, and 2,000 examples. For each sub-
set size, we run experiments with 5 random seeds.
Across all experiments, we use a fixed validation
set of 500 examples and a test set of 2,000 exam-
ples for each target language4. We only use the
training split of the target language for retrieval
4For Arabic and French, smaller dataset sizes limited the
test sets to 1,000 and 1,500 samples, respectively.
and fine-tuning. The test set remains entirely un-
seen throughout the process to ensure evaluation
integrity and is kept fixed across all experiments.
The performance comparison is based on the
F1-macro metric. We compare our method to the
common practice of fine-tuning solely on the target
training set, referred to as Mono. We also compare
against the approach by R¨ottger et al. (2022), which
performs intermediate fine-tuning on three English
hate speech datasets (20,000 instances each) to
identify the most effective source task and then
fine-tunes on the target language training set. We
report the best result among the three as R¨ottger.
5
Results
Table 1 presents a subset of the main results, show-
ing five representative training sizes (20, 50, 200,
500, 2,000) out of the 12 evaluated across eight lan-
guages. The AVG column reflects the average per-
formance over all 12 training sizes. The Mono and
R¨ottger columns show the performance of those
methods on the target language’s test set. Columns
labeled 20, 200, 2,000, and 20,000 indicate the
number of retrieved instances used from the multi-
lingual pool. Further results are in Appendix D.
In all languages, retrieving as few as 20 in-
stances for fine-tuning already outperforms the
Mono setting, indicating the effectiveness of our
proposed method and the value of cross-lingual
data.
This is particularly promising for target
tasks with fewer than 50 instances, where perfor-
mance improvements exceed 10% in some lan-
guages such as San20 it, Ous19 ar, and Xdo-
main tr. While the performance gain decreases
as more target language training data becomes
available, the average results consistently show
that leveraging cross-lingual data outperforms re-
lying solely on the target language’s training set.
In most languages—except for Bas19 es and Xdo-
main tr—our proposed method outperforms the
R¨ottger on average, while using less training data
and without requiring manual selection of inter-
mediate tasks. Notably, retrieving around 200 in-
stances often yields comparable or even superior
performance to this work, which uses 20,000 train-
ing size for intermediate fine-tuning.
Another insight from Table 1 is how cross-
lingual retrieval can compensate for limited la-
beled data in the target language. For example,
in Hindi, retrieving just 20 instances for a training
size of 20 matches the performance of having 50

--- Page 6 ---

TRAIN
San20 it
Ous19 ar
Ous19 fr
SIZE
Mono 20
200
2,000
20,000 R¨ottger
Mono 20
200
2,000
20,000 R¨ottger
Mono 20
200
2,000
20,000 R¨ottger
20
54.25
63.20
66.76
67.06
60.06
64.96
51.67
57.63
63.23
61.73
59.47
60.52
47.26
47.21
52.68
53.93
55.05
52.93
50
65.71
67.20
68.42
71.65
69.44
69.10
52.13
59.36
66.65
66.31
64.51
65.76
47.87
48.29
52.19
52.97
55.60
54.15
200
72.81
72.46
72.83
72.41
72.50
71.56
67.97
67.98
69.18
67.35
65.47
66.61
51.93
51.54
54.06
55.80
53.63
53.76
500
74.18
75.39
75.29
74.53
66.09
73.69
66.54
68.95
69.47
69.28
65.54
67.60
51.91
53.30
52.84
55.51
55.31
53.39
2,000
76.40
69.27
78.36
77.57
76.95
77.07
66.91
69.52
69.77
70.15
68.27
67.07
51.84
53.51
53.13
53.30
54.74
52.89
AVG
66.53
67.68
71.00
71.06
68.55
70.47
59.82
63.94
66.82
66.41
65.20
65.41
49.72
50.56
53.12
54.05
54.84
53.88
Bas19 es
For19 pt
Xdomain tr
20
49.91
54.37
59.72
62.52
63.08
66.52
48.09
49.72
64.92
68.57
68.03
67.68
55.43
66.58
67.08
70.14
75.87
69.80
50
61.85
60.93
64.37
65.59
64.30
70.36
60.25
59.26
67.01
67.06
69.35
66.51
72.24
75.92
77.50
78.85
70.60
75.12
200
72.36
72.22
71.77
71.23
70.67
75.27
66.91
69.69
70.33
70.20
71.07
68.10
81.63
81.61
82.61
83.04
82.61
82.19
500
77.14
78.01
77.09
77.79
67.67
78.76
69.95
69.72
70.84
70.04
71.05
69.22
85.05
84.93
85.09
84.92
83.88
85.34
2,000
81.08
80.62
80.50
80.65
81.02
82.04
72.70
72.39
72.66
71.72
72.22
71.61
88.53
87.39
88.00
87.39
77.48
88.84
AVG
65.52
67.27
69.53
70.53
68.69
72.97
61.66
62.85
68.18
69.55
69.69
68.39
73.58
76.78
78.88
79.66
77.58
80.27
Gahd24 de
Has21 hi
20
44.99
50.52
58.15
59.08
57.48
59.82
46.87
47.34
51.03
53.68
55.37
54.92
50
57.85
54.53
60.30
60.47
61.02
62.57
46.87
48.39
53.36
52.26
55.78
54.77
200
65.80
66.95
66.15
66.24
65.97
64.25
52.20
55.83
54.65
56.80
56.02
57.47
500
66.56
69.78
69.68
70.45
61.80
67.02
56.20
56.94
57.66
57.88
59.55
57.96
2,000
73.77
79.19
78.79
77.82
77.90
72.42
57.14
58.19
60.22
60.50
59.65
58.01
AVG
60.06
62.98
64.77
65.36
64.18
64.23
50.96
52.44
55.10
56.25
57.05
56.70
Table 1: F1-macro scores across eight languages, comparing our method with the Mono and R¨ottger. Results
are reported for target training sizes of 20, 50, 200, 500, and 2,000. Columns represent the number of retrieved
instances. AVG denotes the mean over 12 training sizes. The best result for each language and training size is in
bold. Retrieved results that outperform the next larger Mono training size are underlined.
labeled examples, and retrieving 2,000 instances
approaches the performance of having 200 labeled
instances. This pattern is consistent across other
underlined values in the table. In languages where
Mono performance with 2,000 training samples fails
to exceed 70%—as in Ous19 ar, Ous19 fr, and
Has21 hi—retrieval proves especially valuable, of-
ten matching the next training size.
For languages where Mono’s highest perfor-
mance is less than 75% (Gahd24 de and For19 pt),
retrieval remains helpful, compensating for up to
500 labeled examples.
However, in languages
where Mono performance exceeds 75% with 2,000
samples, retrieval is less beneficial—except in the
extreme low-data case: with only 20 labeled data,
retrieval consistently outperforms the Mono model
trained on 50 examples across all languages.
Another observation from Table 1 is that, in
five languages—excluding Ous19 fr, For19 pt, and
Has21 hi—the highest average performance is
achieved by retrieving 2,000 instances, while re-
trieving 20,000 leads to a performance drop. For in-
stance, in Ous19 ar, retrieving 200 instances yields
the best result. This suggests that increasing the
number of retrieved data points for fine-tuning does
not necessarily lead to improved performance.
How Much Retrieved Data Is Sufficient?
To
address this question, we conducted an experiment
varying the number of retrieved instances across
21 settings, from 10 to 100,000 (More than a third
of the pool size), for four languages as shown in
Figure 2. The figure includes five different training
sizes, each represented by a distinct color. The
brown line labeled AVG denotes the average perfor-
mance over 12 training sizes.
As shown in the figure, especially in the average
trend line—where the effects of noise are dimin-
ished due to averaging— performance increases
as the number of retrieved instances grows—up to
around 2,000—after which it gradually declines.
This change is more pronounced for smaller train-
ing sizes (e.g., 20), while for larger sizes (e.g.,
2,000), the effect is minimal. These results suggest
that adding more retrieved data is not always ben-
eficial, and peak performance is typically reached
with around 2,000 retrieved instances.
5.1
Retrieved Languages Distribution
An interesting analysis is to examine which tasks
or languages the retrieved data come from for each
target language. This is illustrated in Figure 3,
which shows the average retrieval distribution when
retrieving 2,000 instances for a training size of
2,000, averaged over five random subsamples of
the original training set. In the Sankey diagram,
source tasks are shown on the left and target tasks
on the right, with edges representing the four most

--- Page 7 ---

10
20
30
4050
100
200
300
400
500
1000
2000
3000
4000
5000
10000
20000
30000
40000
50000
100000
Num Retrieved Data
55
60
65
70
75
Macro F1
68.84
71.65
74.02
75.39
78.36
71.66
San20_it
Train Size
20
50
200
500
2000
AVG
10
20
30
4050
100
200
300
400
500
1000
2000
3000
4000
5000
10000
20000
30000
40000
50000
100000
Num Retrieved Data
56
58
60
62
64
66
68
70
Macro F1
63.76
68.07
70.03
70.41
71.08
67.01
Ous19_ar
Train Size
20
50
200
500
2000
AVG
10
20
30
4050
100
200
300
400
500
1000
2000
3000
4000
5000
10000
20000
30000
40000
50000
100000
Num Retrieved Data
50
55
60
65
70
75
80
Macro F1
63.08
65.59
73.23
78.59
81.16
70.53
Bas19_es
Train Size
20
50
200
500
2000
AVG
10
20
30
4050
100
200
300
400
500
1000
2000
3000
4000
5000
10000
20000
30000
40000
50000
100000
Num Retrieved Data
45
50
55
60
65
70
75
80
Macro F1
59.96
61.54
67.98
70.75
79.19
65.61
Gahd24_de
Train Size
20
50
200
500
2000
AVG
Figure 2: Performance across different numbers of retrieved instances (10 to 100,000, log-scaled) for four languages.
Each curve corresponds to selected training sizes. The AVG line shows the average over 12 training sizes.
bas19_es
dyn21_en
for19_pt
fou18_en
implicit_en
ken20_en
ous19_ar
san20_it
xdomain_en
xdomain_tr
xplain_en
bas19_es
for19_pt
gahd24_de
has21_hi
ous19_ar
ous19_fr
san20_it
xdomain_tr
Source Tasks
Target Tasks
Figure 3: Sankey diagram of the distribution of the top
four retrieved source tasks per target task.
frequently retrieved source tasks for each target
task. Due to the dominance of English data in the
pool, a higher proportion of English instances is
expected, with Ken20 en and Fou18 en being the
most commonly retrieved source tasks.
However, we also observe non-negligible re-
trieval from smaller source tasks, such as Arabic,
highlighting semantic and contextual relevance be-
tween hate speech in source and target languages.
We can also see that linguistically or culturally
related languages tend to support each other: Por-
tuguese benefits French, Turkish supports Arabic,
and Italian aids Spanish. This highlights the effec-
tiveness of our approach in identifying culturally
proximate examples. This retrieval pattern can also
be due to shared annotation styles or content over-
lap. Further diagrams are in Appendix E.
5.2
English-only vs Multilingual Retrieval
This experiment examines the effect of multilin-
gual retrieval by comparing it to English-only re-
trieval, where data is retrieved exclusively from
English tasks. Table 2 presents the results: rows
are retrieval settings, and columns represent four
target languages (see Appendix F for other lan-
guages). Comparisons should be made vertically
within each language—for example, comparing
20 training samples with 20 retrieved instances
across the two row blocks. We observe only minor
differences in overall performance across the two
settings in the table, likely due to the high propor-
tion of English data in the pool. However, in spe-
cific cases—such as retrieving 2,000 instances for
Bas19 es and For19 pt, and 20 or 2,000 instances
for Has21 hi and Ous19 fr—multilingual retrieval
yields higher performance. This suggests that in-
corporating even a small amount of multilingual
data can be beneficial.

--- Page 8 ---

TRAIN
Bas19 es
For19 pt
Has21 hi
Ous19 fr
SIZE
20
200
2,000
20,000
20
200
2,000
20,000
20
200
2,000
20,000
20
200
2,000
20,000
English
Retrieval
20
55.83
61.15
61.92
63.03
52.00
65.73
68.11
67.55
46.92
52.72
56.01
55.71
47.26
51.17
53.58
55.10
50
61.67
65.19
64.13
62.91
57.58
66.86
67.71
68.52
48.90
52.67
55.62
55.46
48.64
51.56
54.38
53.35
200
71.53
71.08
71.01
68.24
69.13
70.04
68.73
70.19
54.22
56.24
58.62
56.44
50.70
56.15
54.11
53.56
500
77.13
76.28
76.67
74.55
69.60
70.67
70.77
70.02
55.23
57.54
59.83
58.02
51.75
53.22
52.46
53.48
2,000
80.67
80.68
80.68
80.54
72.07
72.32
71.12
64.82
57.40
59.00
60.63
60.74
50.47
53.11
52.31
53.82
AVG
67.27
69.98
69.61
68.62
62.86
68.53
69.02
68.32
52.04
55.22
57.19
56.24
50.00
52.40
53.38
54.07
Multilingual
Retrieval
20
54.37
59.72
62.52
63.08
49.72
64.92
68.57
68.03
47.34
51.03
53.68
55.37
47.21
52.68
53.93
55.05
50
60.93
64.37
65.59
64.30
59.26
67.01
67.06
69.35
48.39
53.36
52.26
55.78
48.29
52.19
52.97
55.60
200
72.22
71.77
71.23
70.67
69.69
70.33
70.20
71.07
55.83
54.65
56.80
56.02
51.54
54.06
55.80
53.63
500
78.01
77.09
77.79
67.67
69.72
70.84
70.04
71.05
56.94
57.66
57.88
59.55
53.30
52.84
55.51
55.31
2,000
80.62
80.50
80.65
81.02
72.39
72.66
71.72
72.22
58.19
60.22
60.50
59.65
53.51
53.13
53.30
54.74
AVG
67.27
69.53
70.53
68.69
62.85
68.18
69.55
69.69
52.44
55.10
56.25
57.05
50.56
53.12
54.05
54.84
Table 2: F1-macro scores across two strategies: English-only retrieval, and Multilingual retrieval.
6
Maximum Marginal Relevance
As an additional deduplication step, we apply
Maximum Marginal Relevance (MMR) in the re-
trieval module—before mapping the retrieved vec-
tors back to their original texts—to ensure both
relevance and diversity. Specifically, we retrieve
at least 2R candidate vectors and iteratively select
R vectors that balance similarity to the query and
dissimilarity to previously selected vectors. Given
a query vector q, a candidate set D, and a selected
set S, MMR selects the next vector v∗∈D \ S as:
MMR(v∗) = arg max
v∈D\S
h
λ · cos(v, q)
−(1 −λ) · max
s∈S cos(v, s)
i
Here, λ ∈[0, 1] controls the trade-off between
relevance to the query and diversity with respect to
the selected set. We set the λ = 0.5. This process
is repeated until exactly R vectors are selected.
Although removing highly similar instances us-
ing MMR increases the diversity of the retrieved
data, however, incorporating it does not affect per-
formance a lot, with results remaining largely simi-
lar across most languages—except for those listed
in Table 3 (See Appendix G). As shown in the
figure, for these three languages, applying MMR
particularly improves performance when retrieving
fewer than 2,000 instances. In contrast, for 20,000
retrieved instances, the performance without MMR
is higher. This suggests that when only a limited
number of instances is retrieved, MMR helps select
fewer but more diverse examples, which can lead
to improved performance. Interestingly, for the
Turkish dataset—where our method previously un-
derperformed without MMR—applying it allows
the model to surpass the performance of R¨ottger.
TRAIN
Without MMR
With MMR
SIZE
20
200
2,000
20,000
20
200
2,000
20,000
San20 it
20
63.20
66.76
67.06
60.06
60.28
66.89
61.69
62.38
50
67.20
68.42
71.65
69.44
69.71
68.30
70.11
63.30
200
72.46
72.83
72.41
72.50
72.51
72.66
73.07
72.08
500
75.39
75.29
74.53
66.09
74.93
75.41
75.00
75.69
2,000 69.27
78.36
77.57
76.95
77.66
77.06
76.67
68.88
AVG
67.68
71.00
71.06
68.55
69.24
71.64
71.38
68.33
Gahd24 de
20
50.52
58.15
59.08
57.48
51.47
58.14
58.63
59.14
50
54.53
60.30
60.47
61.02
54.83
60.07
61.13
60.50
200
66.95
66.15
66.24
65.97
68.09
66.20
67.13
65.41
500
69.78
69.68
70.45
61.80
70.36
70.11
70.06
62.77
2,000 79.19
78.79
77.82
77.90
78.55
79.08
77.53
68.84
AVG
62.98
64.78
65.36
64.18
62.71
65.13
65.83
63.62
Xdomain tr
20
66.58
67.08
70.14
75.87
65.19
72.00
77.16
67.48
50
75.92
77.50
78.85
70.60
75.98
76.08
79.84
64.58
200
81.61
82.61
83.04
82.61
81.43
80.92
83.06
82.76
500
84.93
85.09
84.92
83.88
84.77
84.60
84.01
83.41
2,000 87.39
88.00
87.39
77.48
88.14
87.73
86.91
66.70
AVG
76.78
78.88
79.66
77.58
77.59
79.75
80.80
76.01
Table 3: F1-macro scores without/with MMR for three
languages (rows).
7
Conclusion
This paper presents a cross-lingual nearest neighbor
retrieval approach to improve hate speech detection
in target languages with limited labeled data. Our
method retrieves the nearest neighbors from a mul-
tilingual pool of source tasks to augment the target
language data, consistently outperforming models
trained solely on the target language. Notably, even
with as few as 20 labeled instances in the target
language, our approach can achieve performance
improvements of up to 10% in some cases. Fur-
ther, we show that retrieving approximately 2,000
instances yields the highest average performance,
while retrieving more can lead to a performance
drop. Our method is scalable and adaptable to new
languages and tasks, allowing new source tasks to
be added to the pool with minimal effort.

--- Page 9 ---

Limitations
Despite the effectiveness of our approach, several
limitations remain. First, we assume access to a
small number of labeled hate speech instances in
the target language. While this assumption reduces
annotation cost, it may not hold in extremely low-
resource settings where even minimal labeled data
is unavailable or difficult to obtain due to linguistic,
political, or ethical constraints.
Second, the retrieval pool used in our experi-
ments is heavily imbalanced, with English account-
ing for the majority of instances. This dominance
can bias retrieval and limit performance improve-
ments for target languages that are typologically
distant or culturally distinct from English.
While we reviewed the definitions of hate speech
used in the datasets for our experiments, cultural
differences and annotation inconsistencies may still
be present. Although hate speech is undoubtedly
influenced by cultural context, many hateful ex-
pressions are universal across languages and cul-
tures. Our experiments demonstrate that leveraging
such cross-lingual data can effectively improve hate
speech detection in low-resource settings.
Our evaluation focuses on a subset of hate speech
detection tasks and languages and does not encom-
pass the full variety of online abuse domains or
contexts in which hate speech occurs. Expand-
ing the set of target labels and tasks, especially
in non-Western languages and underrepresented
communities, would help assess the robustness and
generalizability of the proposed method.
Finally, while our results confirm the effective-
ness of cross-lingual retrieval for hate speech de-
tection, a promising direction for future work is to
more deeply analyze the nature and influence of
the retrieved instances. Such analysis could offer
further insights into why retrieval is effective, en-
hance our understanding of cross-lingual transfer,
similarities, and differences of hate speech across
languages, and contribute to more interpretable and
adaptive retrieval strategies.
Ethical Consideration
Our approach relies on the availability of existing
labeled datasets for hate speech detection, many
of which are restricted to non-commercial research
use. This presents limitations for real-world deploy-
ment, particularly in industry settings where such
licensing terms may prohibit direct reuse. However,
the proposed method remains valuable in industrial
scenarios where systems are initially developed for
high-resource languages and later adapted to lower-
resource markets. Instead of incurring substan-
tial costs to collect large-scale labeled data from
scratch, companies could use this cross-lingual
transfer approach to quickly build minimum viable
products (MVPs) for new linguistic contexts.
Still, while our method provides an efficient path
for adapting models to low-resource languages us-
ing cross-lingual retrieval, its applicability is ulti-
mately constrained by legal access to source data.
Therefore, we emphasize that the responsible use of
our method and, further, data for the downstream
cases requires careful attention to data licensing
and ethical data sharing practices.
Acknowledgements
The work was supported by the European Research
Council (ERC) through the European Union’s Hori-
zon Europe research and innovation programme
(grant agreement No. 101113091) and the German
Research Foundation (DFG; grant FR 2829/7-1).
References
Maryam M. AlEmadi and Wajdi Zaghouani. 2024. Emo-
tional toll and coping strategies: Navigating the ef-
fects of annotating hate speech data. In Proceed-
ings of the Workshop on Legal and Ethical Issues in
Human Language Technologies @ LREC-COLING
2024, pages 66–72, Torino, Italia. ELRA and ICCL.
Sai Saketh Aluru, Binny Mathew, Punyajoy Saha, and
Animesh Mukherjee. 2020a. A deep dive into multi-
lingual hate speech classification. In Machine Learn-
ing and Knowledge Discovery in Databases. Applied
Data Science and Demo Track: European Confer-
ence, ECML PKDD 2020, Ghent, Belgium, Septem-
ber 14–18, 2020, Proceedings, Part V, page 423–439,
Cham. Springer International Publishing.
Sai Saketh Aluru, Binny Mathew, Punyajoy Saha, and
Animesh Mukherjee. 2020b. Deep learning models
for multilingual hate speech detection. In Machine
Learning and Knowledge Discovery in Databases.
ECML PKDD 2020, volume 12461 of Lecture Notes
in Computer Science, pages 528–544. Springer.
Dimosthenis Antypas and Jose Camacho-Collados.
2023. Robust hate speech detection in social me-
dia: A cross-dataset empirical evaluation. In The
7th Workshop on Online Abuse and Harms (WOAH),
pages 231–242, Toronto, Canada. ACL.
Francesco Barbieri, Luis Espinosa Anke, and Jose
Camacho-Collados. 2022. XLM-T: Multilingual lan-
guage models in Twitter for sentiment analysis and
beyond. In Proceedings of the Thirteenth Language

--- Page 10 ---

Resources and Evaluation Conference, pages 258–
266, Marseille, France. ELRA.
Valerio Basile, Cristina Bosco, Elisabetta Fersini,
Debora Nozza, Viviana Patti, Francisco Manuel
Rangel Pardo, Paolo Rosso, and Manuela Sanguinetti.
2019. SemEval-2019 task 5: Multilingual detection
of hate speech against immigrants and women in
Twitter. In Proceedings of the 13th International
Workshop on Semantic Evaluation, pages 54–63, Min-
neapolis, Minnesota, USA. ACL.
Djamila Romaissa Beddiar, Md Saroar Jahan, and
Mourad Oussalah. 2021. Data expansion using back
translation and paraphrasing for hate speech detec-
tion. Online Social Networks and Media, 24:100153.
Irina Bigoulaeva, Viktor Hangya, and Alexander Fraser.
2021. Cross-lingual transfer learning for hate speech
detection. In Proceedings of the First Workshop on
Language Technology for Equality, Diversity and
Inclusion, pages 15–25, Kyiv. ACL.
Irina Bigoulaeva, Viktor Hangya, Iryna Gurevych, and
Alexander Fraser. 2022. Addressing the challenges
of cross-lingual hate speech detection. arXiv preprint
arXiv:2201.05922.
Jaime Carbonell and Jade Goldstein. 1998. The use of
mmr, diversity-based reranking for reordering doc-
uments and producing summaries. In Proceedings
of the 21st Annual International ACM SIGIR Confer-
ence on Research and Development in Information
Retrieval, SIGIR ’98, page 335–336, New York, NY,
USA. ACM.
Tommaso Caselli, Valerio Basile, Jelena Mitrovi´c, Inga
Kartoziya, and Michael Granitzer. 2020. I feel of-
fended, don‘t be abusive! implicit/explicit messages
in offensive and abusive language. In Proceedings of
the Twelfth Language Resources and Evaluation Con-
ference, pages 6193–6202, Marseille, France. ELRA.
Jianlyu Chen, Shitao Xiao, Peitian Zhang, Kun
Luo, Defu Lian, and Zheng Liu. 2024.
M3-
embedding:
Multi-linguality, multi-functionality,
multi-granularity text embeddings through self-
knowledge distillation. In Findings of the Associa-
tion for Computational Linguistics: ACL 2024, pages
2318–2335, Bangkok, Thailand. ACL.
Alexis Conneau, Kartikay Khandelwal, Naman Goyal,
Vishrav Chaudhary, Guillaume Wenzek, Francisco
Guzm´an, Edouard Grave, Myle Ott, Luke Zettle-
moyer, and Veselin Stoyanov. 2020. Unsupervised
cross-lingual representation learning at scale. In Pro-
ceedings of the 58th Annual Meeting of the Asso-
ciation for Computational Linguistics, pages 8440–
8451, Online. ACL.
Devleena Das and Vivek Khetan. 2024. DEFT-UCS:
Data efficient fine-tuning for pre-trained language
models via unsupervised core-set selection for text-
editing. In Proceedings of the 2024 Conference on
Empirical Methods in Natural Language Processing,
pages 20296–20312, Miami, Florida, USA. ACL.
Daryna Dementieva,
Valeriia Khylenko,
Nikolay
Babakov, and Georg Groh. 2024. Toxicity classifica-
tion in Ukrainian. In Proceedings of the 8th Work-
shop on Online Abuse and Harms (WOAH 2024),
pages 244–255, Mexico City, Mexico. ACL.
Matthijs Douze, Alexandr Guzhva, Chengqi Deng,
Jeff Johnson, Gergely Szilvasy, Pierre-Emmanuel
Mazar´e, Maria Lomeli, Lucas Hosseini, and Herv´e
J´egou. 2024.
The faiss library.
arXiv preprint
arXiv:2401.08281.
Mai ElSherief, Caleb Ziems, David Muchlinski, Vaish-
navi Anupindi, Jordyn Seybolt, Munmun De Choud-
hury, and Diyi Yang. 2021. Latent hatred: A bench-
mark for understanding implicit hate speech. In Pro-
ceedings of the 2021 Conference on Empirical Meth-
ods in Natural Language Processing, pages 345–363,
Online and Punta Cana, Dominican Republic. ACL.
Anderson Almeida Firmino, Cl´audio de Souza Baptista,
and Anselmo Cardoso de Paiva. 2024. Improving
hate speech detection using cross-lingual learning.
Expert Syst. Appl., 235(C).
Paula Fortuna and S´ergio Nunes. 2018. A survey on
automatic detection of hate speech in text. ACM
Computing Surveys, 51(4).
Paula Fortuna, Jo˜ao Rocha da Silva, Juan Soler-
Company, Leo Wanner, and S´ergio Nunes. 2019. A
hierarchically-labeled Portuguese hate speech dataset.
In Proceedings of the Third Workshop on Abusive
Language Online, pages 94–104, Florence, Italy.
ACL.
Antigoni Founta, Constantinos Djouvas, Despoina
Chatzakou, Ilias Leontiadis, Jeremy Blackburn, Gi-
anluca Stringhini, Athena Vakali, Michael Sirivianos,
and Nicolas Kourtellis. 2018. Large scale crowd-
sourcing and characterization of twitter abusive be-
havior. Proceedings of the International AAAI Con-
ference on Web and Social Media, 12(1).
Hassan Gharoun, Fereshteh Momenifar, Fang Chen, and
Amir H. Gandomi. 2024. Meta-learning approaches
for few-shot learning: A survey of recent advances.
ACM Comput. Surv., 56(12).
Janis Goldzycher, Moritz Preisig, Chantal Amrhein, and
Gerold Schneider. 2023. Evaluating the effectiveness
of natural language inference for hate speech detec-
tion in languages with limited labeled data. In The
7th Workshop on Online Abuse and Harms (WOAH),
pages 187–201, Toronto, Canada. ACL.
Janis Goldzycher, Paul R¨ottger, and Gerold Schneider.
2024. Improving adversarial data collection by sup-
porting annotators: Lessons from GAHD, a German
hate speech dataset.
In Proceedings of the 2024
Conference of the North American Chapter of the
Association for Computational Linguistics: Human
Language Technologies (Volume 1: Long Papers),
pages 4405–4424, Mexico City, Mexico. ACL.

--- Page 11 ---

Kelvin Guu, Kenton Lee, Zora Tung, Panupong Pasu-
pat, and Ming-Wei Chang. 2020. Realm: retrieval-
augmented language model pre-training. In Proceed-
ings of the 37th International Conference on Machine
Learning, ICML’20. JMLR.org.
Xiaochuang Han and Yulia Tsvetkov. 2022. Orca: In-
terpreting prompted language models via locating
supporting data evidence in the ocean of pretraining
data. arXiv preprint arXiv:2205.12600.
Ehtesham Hashmi, Sule Yildirim Yayilgan, and Mo-
hamed Abomhara. 2025.
Metalinguist: Enhanc-
ing hate speech detection with cross-lingual meta-
learning. Complex & Intelligent Systems, 11(1):179.
Pengcheng He, Jianfeng Gao, and Weizhu Chen. 2021.
Debertav3: Improving deberta using electra-style pre-
training with gradient-disentangled embedding shar-
ing. arXiv preprint arXiv:2111.09543.
Hamish Ivison, Noah A. Smith, Hannaneh Hajishirzi,
and Pradeep Dasigi. 2023. Data-efficient finetuning
using cross-task nearest neighbors. In Findings of
the Association for Computational Linguistics: ACL
2023, pages 9036–9061, Toronto, Canada. ACL.
Jeff Johnson, Matthijs Douze, and Herv´e J´egou. 2021.
Billion-scale similarity search with gpus.
IEEE
Transactions on Big Data, 7(3):535–547.
Brendan Kennedy, Xisen Jin, Aida Mostafazadeh Da-
vani, Morteza Dehghani, and Xiang Ren. 2020a. Con-
textualizing hate speech classifiers with post-hoc ex-
planation. In Proceedings of the 58th Annual Meet-
ing of the Association for Computational Linguistics,
pages 5435–5442, Online. ACL.
Chris J. Kennedy, Geoff Bacon, Alexander Sahn, and
Claudia von Vacano. 2020b. Constructing interval
variables via faceted rasch measurement and multi-
task deep learning: a hate speech application. arXiv
preprint arXiv:2009.10277.
Urvashi Khandelwal, Omer Levy, Dan Jurafsky, Luke
Zettlemoyer, and Mike Lewis. 2020. Generalization
through memorization: Nearest neighbor language
models. In Proceedings of the 8th International Con-
ference on Learning Representations (ICLR).
Bill Yuchen Lin, Kangmin Tan, Chris Miller, Beiwen
Tian, and Xiang Ren. 2022. Unsupervised cross-
task generalization via retrieval augmentation. In
Advances in Neural Information Processing Systems,
volume 35.
Yu A. Malkov and D. A. Yashunin. 2020. Efficient
and robust approximate nearest neighbor search us-
ing hierarchical navigable small world graphs. IEEE
Transactions on Pattern Analysis and Machine Intel-
ligence, 42(4):824–836.
Thomas Mandl, Sandip Modha, Gautam Kishore Shahi,
Hiren Madhu, Shrey Satapara, Prasenjit Majumder,
Johannes Sch¨afer, Tharindu Ranasinghe, Marcos
Zampieri, Durgesh Nandini, and Amit Kumar Jaiswal.
2021. Overview of the hasoc subtrack at fire 2021:
Hate speech and offensive content identification in
english and indo-aryan languages. In Working Notes
of FIRE 2021 - Forum for Information Retrieval Eval-
uation, volume 3159, pages 1–19. CEUR Workshop
Proceedings.
Binny Mathew, Punyajoy Saha, Seid Muhie Yimam,
Chris Biemann, Pawan Goyal, and Animesh Mukher-
jee. 2021. Hatexplain: A benchmark dataset for ex-
plainable hate speech detection. In Proceedings of
the AAAI Conference on Artificial Intelligence, vol-
ume 35, pages 14867–14875.
Ayme Arango Monnar, Jorge P´erez Rojas, and Bar-
bara Poblete. 2024. Cross-lingual hate speech detec-
tion using domain-specific word embeddings. PLOS
ONE, 19(7):e0306521.
Marzieh Mozafari, Reza Farahbakhsh, and Noel Crespi.
2022. Cross-lingual few-shot hate speech and offen-
sive language detection using meta learning. IEEE
Access, 10:14880–14896.
Masayasu Muraoka,
Bishwaranjan Bhattacharjee,
Michele Merler, Graeme Blackwood, Yulong Li, and
Yang Zhao. 2023. Cross-lingual transfer of large lan-
guage model by visually-derived supervision toward
low-resource languages. In Proceedings of the 31st
ACM International Conference on Multimedia, MM
’23, page 3637–3646, New York, NY, USA. ACM.
Rachna Narula and Poonam Chaudhary. 2024. A com-
prehensive review on detection of hate speech for
multi-lingual data. Social Network Analysis and Min-
ing, 14(244).
Nedjma Ousidhoum, Zizheng Lin, Hongming Zhang,
Yangqiu Song, and Dit-Yan Yeung. 2019. Multi-
lingual and multi-aspect hate speech analysis. In
Proceedings of the 2019 Conference on Empirical
Methods in Natural Language Processing and the
9th International Joint Conference on Natural Lan-
guage Processing (EMNLP-IJCNLP), pages 4675–
4684, Hong Kong, China. ACL.
Endang Wahyu Pamungkas, Valerio Basile, and Viviana
Patti. 2021. A joint learning approach with knowl-
edge injection for zero-shot cross-lingual hate speech
detection. Information Processing and Management,
58(4).
Endang Wahyu Pamungkas and Viviana Patti. 2019.
Cross-domain and cross-lingual abusive language de-
tection: A hybrid approach with deep learning and
a multilingual lexicon. In Proceedings of the 57th
Annual Meeting of the Association for Computational
Linguistics: Student Research Workshop, pages 363–
370, Florence, Italy. ACL.
Marinela Parovic, Alan Ansell, Ivan Vuli´c, and Anna
Korhonen. 2023. Cross-lingual transfer with target
language-ready task adapters. In Findings of the As-
sociation for Computational Linguistics: ACL 2023,
pages 176–193, Toronto, Canada. Association for
Computational Linguistics.

--- Page 12 ---

Andraˇz Pelicon, Ravi Shekhar, Blaˇz ˇSkrlj, Matthew
Purver, and Senja Pollak. 2021. Investigating cross-
lingual training for offensive language detection.
PeerJ Computer Science, 7:e559.
Trinh Pham, Khoi Le, and Anh Tuan Luu. 2024. UniB-
ridge: A unified approach to cross-lingual transfer
learning for low-resource languages. In Proceedings
of the 62nd Annual Meeting of the Association for
Computational Linguistics (Volume 1: Long Papers),
pages 3168–3184, Bangkok, Thailand. ACL.
Fabio Poletto, Valerio Basile, Manuela Sanguinetti,
Cristina Bosco, and Viviana Patti. 2021. Resources
and benchmark corpora for hate speech detection: a
systematic review. Language Resources and Evalua-
tion, 55(2):477–523.
Garima Pruthi, Frederick Liu, Satyen Kale, and Mukund
Sundararajan. 2020. Estimating training data influ-
ence by tracing gradient descent. In Advances in
Neural Information Processing Systems, volume 33,
pages 19920–19930.
Nils Reimers and Iryna Gurevych. 2020.
Making
monolingual sentence embeddings multilingual us-
ing knowledge distillation. In Proceedings of the
2020 Conference on Empirical Methods in Natural
Language Processing (EMNLP), pages 4512–4525,
Online. ACL.
Paul R¨ottger, Debora Nozza, Federico Bianchi, and Dirk
Hovy. 2022. Data-efficient strategies for expanding
hate speech detection into under-resourced languages.
In Proceedings of the 2022 Conference on Empiri-
cal Methods in Natural Language Processing, pages
5674–5691, Abu Dhabi, United Arab Emirates. ACL.
Paul R¨ottger, Bertie Vidgen, Dong Nguyen, Zeerak
Waseem, Helen Margetts, and Janet Pierrehumbert.
2021. HateCheck: Functional tests for hate speech
detection models. In Proceedings of the 59th Annual
Meeting of the Association for Computational Lin-
guistics and the 11th International Joint Conference
on Natural Language Processing (Volume 1: Long
Papers), pages 41–58, Online. ACL.
Sumegh Roychowdhury and Vikram Gupta. 2023. Data-
efficient methods for improving hate speech detec-
tion.
In Findings of the Association for Compu-
tational Linguistics: EACL 2023, pages 125–132,
Dubrovnik, Croatia. ACL.
Manuela Sanguinetti, Gloria Comandini, Elisa Di
Nuovo, Simona Frenda, Marco Stranisci, Cristina
Bosco, Tommaso Caselli, Viviana Patti, and Irene
Russo. 2020. Haspeede 2 @ evalita2020: Overview
of the evalita 2020 hate speech detection task. In
Proceedings of the Seventh Evaluation Campaign of
Natural Language Processing and Speech Tools for
Italian. Final Workshop (EVALITA 2020), volume
2765. CEUR Workshop Proceedings.
Weijia Shi, Julian Michael, Suchin Gururangan, and
Luke Zettlemoyer. 2022. Nearest neighbor zero-shot
inference. In Proceedings of the 2022 Conference on
Empirical Methods in Natural Language Processing,
pages 3254–3265, Abu Dhabi, United Arab Emirates.
ACL.
Cagri Toraman, Furkan S¸ahinuc¸, and Eyup Yilmaz.
2022. Large-scale hate speech detection with cross-
domain transfer. In Proceedings of the Thirteenth
Language Resources and Evaluation Conference,
pages 2215–2225, Marseille, France. ELRA.
Bertie Vidgen, Dong Nguyen, Helen Margetts, Patricia
Rossini, and Rebekah Tromble. 2021a. Introducing
CAD: the contextual abuse dataset. In Proceedings
of the 2021 Conference of the North American Chap-
ter of the Association for Computational Linguistics:
Human Language Technologies, pages 2289–2303,
Online. ACL.
Bertie Vidgen, Tristan Thrush, Zeerak Waseem, and
Douwe Kiela. 2021b. Learning from the worst: Dy-
namically generated datasets to improve online hate
detection. In Proceedings of the 59th Annual Meet-
ing of the Association for Computational Linguistics
and the 11th International Joint Conference on Natu-
ral Language Processing (Volume 1: Long Papers),
pages 1667–1682, Online. ACL.
Michael Wiegand, Josef Ruppenhofer, and Thomas
Kleinbauer. 2019. Detection of Abusive Language:
the Problem of Biased Datasets. In Proceedings of
the 2019 Conference of the North American Chap-
ter of the Association for Computational Linguistics:
Human Language Technologies, Volume 1 (Long and
Short Papers), pages 602–608, Minneapolis, Min-
nesota. ACL.
Richard Ashby Wilson. 2019. The digital ethnogra-
phy of law: Studying online hate speech online and
offline. Journal of Legal Anthropology, 3(1):1–20.
Thomas Wolf, Lysandre Debut, Victor Sanh, Julien
Chaumond, Clement Delangue, Anthony Moi, Pier-
ric Cistac, Tim Rault, Remi Louf, Morgan Funtow-
icz, Joe Davison, Sam Shleifer, Patrick von Platen,
Clara Ma, Yacine Jernite, Julien Plu, Canwen Xu,
Teven Le Scao, Sylvain Gugger, Mariama Drame,
Quentin Lhoest, and Alexander Rush. 2020. Trans-
formers: State-of-the-art natural language processing.
In Proceedings of the 2020 Conference on Empirical
Methods in Natural Language Processing: System
Demonstrations, pages 38–45, Online. ACL.
Wenjie Yin and Arkaitz Zubiaga. 2021. Towards gener-
alisable hate speech detection: a review on obstacles
and solutions. PeerJ Computer Science, 7:e598.
Li Zhou, Laura Cabello, Yong Cao, and Daniel Her-
shcovich. 2023. Cross-cultural transfer learning for
Chinese offensive language detection. In Proceed-
ings of the First Workshop on Cross-Cultural Consid-
erations in NLP (C3NLP), pages 8–15, Dubrovnik,
Croatia. ACL.

--- Page 13 ---

A
Datasets Details
We used fourteen datasets in our study. Detailed information—including language, number of instances,
license type—is provided in Table 4. In total, we had 265,671 instances, of which 62.85% were Non-Hate
and 37.15% were Hate Speech.
Name
Language
Language
Code
Num
of
Instances
% of Total
Instances
Num
classes
% of Hate
Speech
Licence
Bas19 es (Basile et al., 2019)
Spanish
es
6600
2.48
2
41.50
CC BY 4.0
For19 pt (Fortuna et al., 2019)
Purtegues
pt
5670
2.13
2
31.53
CC BY 4.0
Has21 hi (Mandl et al., 2021)
Hindi
hi
4594
1.73
2
12.32
CC BY 4.0 (Only for research
purposes.)
Ous19 ar (Ousidhoum et al., 2019)
Arabic
ar
3353
1.26
2
22.52
MIT
Ous19 fr (Ousidhoum et al., 2019)
French
fr
4014
1.51
2
00.94
MIT
San20 it (Sanguinetti et al., 2020)
Italian
it
8100
3.05
2
41.83
CC BY-NC-SA 4.0
Gahd24 de (Goldzycher et al., 2024)
German
de
10996
3.84
2
42.37
CC BY 4.0
Xdomain tr (Toraman et al., 2022)
Turkish
tr
37933
17.0
2
42.67
CC BY-NC-SA 4.0
Ken20 en (Kennedy et al., 2020a)
English
en
23192
8.73
2
50.00
MIT
Fou18 en (Founta et al., 2018)
English
en
22565
8.49
2
22.00
CC BY 4.0
Xplain en (Mathew et al., 2021)
English
en
13749
5.08
2
43.22
MIT
Implicit en (ElSherief et al., 2021)
English
en
21480
8.09
2
38.12
MIT
Dyn21 en (Vidgen et al., 2021b)
English
en
41144
15.49
2
46.10
CC BY 4.0
Xdomain en (Toraman et al., 2022)
English
en
47124
21.12
2
19.41
CC BY-NC-SA 4.0
Table 4: Detailed information about the datasets used in this study.
B
Model and Training Details
B.1
Embedder
For the embedding model, we used BAAI/bge-m3,5,6 accessed via the Sentence Transformers library.7
This model supports over 100 languages, is effective for both short and long text retrieval, and produces
1024-dimensional embeddings. It is released under the MIT license, and the Sentence Transformers
library is licensed under Apache 2.0—both allowing use in academic research. We used the model in
inference mode without any fine-tuning, applying it to our text data to generate embedding vectors.
B.2
Retriever
For indexing and searching the embedding vectors in the retrieval pool, we used the Faiss, library8
which is licensed under MIT. We employed the HNSW (Hierarchical Navigable Small World) index with
Euclidean distance as the similarity metric, where smaller values indicate greater similarity to the query.
Since the size of the retrieval pool was moderate, we used the CPU version of the library. The index was
configured with 128 neighbors, a construction parameter of 200, and a search parameter of 128.
B.3
Fine-tuner
We used cardiffnlp/twitter-xlm-roberta-base9 (XLM-T), a multilingual transformer-based model
pre-trained on Twitter data, as our base model for fine-tuning on hate speech detection tasks. The model
is licensed under Apache 2.0, which permits use in academic research. Training and evaluation were
performed using the Hugging Face transformers library.10
To select the classification model, we also evaluated xlm-roberta-base11 (XLM-R) and
mdeberta-v3-base12 (He et al., 2021). XLM-T outperformed XLM-R, likely because hate speech
datasets are primarily sourced from social media, where XLM-T has been pre-trained. Although XLM-T
and mDeBERTa achieved similar performance, we chose to use XLM-T in our experiments, as it supports
a broader range of languages and aligns with our baseline setting.
5https://huggingface.co/BAAI/bge-m3
6https://github.com/FlagOpen/FlagEmbedding
7https://github.com/UKPLab/sentence-transformers
8https://github.com/facebookresearch/faiss
9https://huggingface.co/cardiffnlp/twitter-xlm-roberta-base
10https://github.com/huggingface/transformers
11https://huggingface.co/FacebookAI/xlm-roberta-base
12https://huggingface.co/microsoft/mdeberta-v3-base

--- Page 14 ---

Throughout all our experiments, for training sizes with fewer than 9,999 training instances, we trained
for 10 epochs; for larger training sizes, we used 5 epochs to reduce training time and avoid overfitting.
We set the batch size to 16 and used a learning rate of 5e-5. Inputs were truncated or padded to a
maximum sequence length of 128 tokens. We used binary cross-entropy loss, as our datasets involved
binary classification (Hate vs. Non-Hate). All other training hyperparameters were left at their default
values provided by the transformers.Trainer module.
C
Hardware, Tools, and Ethical Compliance
The experiments were conducted on NVIDIA GeForce GTX 1080 Ti servers. The embedding model
was used in inference mode without updating its parameters, while the classification model was fully
fine-tuned. As the classifier was based on xlm-roberta-base, it included approximately 279 million
parameters. We also acknowledge the use of an AI assistant during the writing process. ChatGPT13 was
used for paraphrasing and improving clarity throughout the formulation of the paper. All models and
datasets used in this study are licensed for academic research purposes and align with the intended use of
advancing NLP applications for social good.
D
Further Results
Table 5 presents the full results of cross-lingual nearest neighbor retrieval fine-tuning, covering training
sizes from 10 to 2,000. These results confirm the trend shown in the main table (Table 1): retrieving as few
as 20 instances already outperforms the Mono baseline in all languages. These performance improvements
are most notable when the target language has fewer than 50 training examples, with gains exceeding
10% compared to training solely on the target language data. In such low-resource settings, retrieving
cross-lingual nearest neighbors and using them for fine-tuning enables the model to match the performance
of much larger training sizes. In most cases, our method also outperforms the R¨ottger approach, while
using less data and without requiring manual selection of a source task.
Additionally, the underlined values—indicating the smallest amount of retrieved data that outperforms
the next larger training size—demonstrate that, in most cases and languages, retrieving cross-lingual data
can effectively compensate for having less labeled data. While in two tasks, Bas19 es and Xdomain tr,
training data appears to be of higher quality and retrieval cannot fully offset its absence, in all other tasks,
retrieval proves effective especially valuable when labeled data is scarce—less than 50-highlighting the
method’s strength in very low-resource hate speech detection settings.
E
Further Analysis
To further analyze what is retrieved and used for fine-tuning under a controlled setting (retrieving 2,000
instances for a training size of 2,000), see Figure 4. This figure shows the distribution of retrieved source
tasks, languages, and labels. As illustrated, English is retrieved the most, followed by Turkish and Spanish
in nearly equal amounts, then Italian and Portuguese. Excluding English, this pattern roughly reflects the
overall language distribution in the pool (see the ”% of Total Instances” column in Table 4). The second
to fifth most represented languages in the pool are Turkish, German, Italian, and Spanish. However, the
low retrieval of German—despite its high presence—and the higher retrieval of Spanish over Italian
are unexpected and may be attributed to task generality or cross-lingual similarity. The distribution of
retrieved labels also mirrors their proportions in the pool: approximately 40% of instances are labeled as
hate, and a similar pattern is observed in the retrieved hate instances across target tasks.
F
More about English-only vs. Multilingual Retrieval
Additional results comparing English-only retrieval and multilingual retrieval are presented in Table 6.
Comparisons in this table should be made vertically: for each language, the values for a specific training
size and number of retrieved instances should be compared between the upper (English-only) and lower
(multilingual) blocks. Similar to the datasets discussed in the main text, multilingual retrieval—with
13https://chatgpt.com/

--- Page 15 ---

San20 it
Ous19 ar
Ous19 fr
SIZE
Mono 20
200
2000
20000 R¨ottger
Mono 20
200
2000
20000 R¨ottger
Mono 20
200
2000
20000 R¨ottger
10
46.23
47.04
64.96
65.26
69.60
63.34
51.98
54.60
56.36
62.86
61.54
59.00
47.26
48.34
52.46
51.90
54.60
53.49
20
54.25
63.20
66.76
67.06
60.06
64.96
51.67
57.63
63.23
61.73
59.47
60.52
47.26
47.21
52.68
53.93
55.05
52.93
30
56.29
64.24
68.47
68.90
70.08
64.95
44.42
57.95
66.23
62.31
62.70
65.48
47.26
47.60
52.82
53.86
54.97
53.91
40
59.14
59.60
67.91
69.16
70.58
67.41
49.67
57.45
65.70
64.52
64.82
64.29
47.24
48.36
52.40
54.63
56.30
56.62
50
65.71
67.20
68.42
71.65
69.44
69.10
52.13
59.36
66.65
66.31
64.51
65.76
47.87
48.29
52.19
52.97
55.60
54.15
100
70.96
70.01
71.17
71.46
67.73
71.89
65.29
66.22
68.50
66.77
66.07
66.44
47.67
49.35
51.54
53.12
56.04
55.83
200
72.81
72.46
72.83
72.41
72.50
71.56
67.97
67.98
69.18
67.35
65.47
66.61
51.93
51.54
54.06
55.80
53.63
53.76
300
73.43
73.56
74.12
72.03
64.56
72.21
66.95
68.94
68.52
69.00
66.71
68.07
51.10
53.49
53.29
54.58
56.15
53.61
400
72.44
73.49
74.84
66.23
66.80
73.32
67.04
69.75
70.20
68.88
68.20
66.79
52.17
53.22
54.57
53.81
55.13
53.34
500
74.18
75.39
75.29
74.53
66.09
73.69
66.54
68.95
69.47
69.28
65.54
67.60
51.91
53.30
52.84
55.51
55.31
53.39
1000
76.56
76.65
68.84
76.41
68.21
76.14
67.29
68.98
68.08
67.77
69.07
67.26
53.14
52.49
55.48
55.15
50.51
52.59
2000
76.40
69.27
78.36
77.57
76.95
77.07
66.91
69.52
69.77
70.15
68.27
67.07
51.84
53.51
53.13
53.30
54.74
52.89
AVG
66.53
67.68
71.00
71.06
68.55
70.47
59.82
63.94
66.82
66.41
65.20
65.41
49.72
50.56
53.12
54.05
54.84
53.88
Bas19 es
For19 pt
Xdomain tr
10
36.51
46.06
58.18
62.23
61.97
59.71
43.18
48.03
61.67
67.53
67.79
66.38
46.92
56.19
73.20
77.11
72.50
72.50
20
49.91
54.37
59.72
62.52
63.08
66.52
48.09
49.72
64.92
68.57
68.03
67.68
55.43
66.58
67.08
70.14
75.87
69.80
30
54.38
60.75
62.56
64.62
63.52
69.02
51.73
54.34
64.61
69.70
67.80
67.78
58.90
73.13
73.64
78.37
75.58
75.58
40
57.63
57.69
62.77
63.10
61.87
66.98
53.83
52.63
65.59
69.68
67.57
67.04
69.97
74.20
75.43
61.71
78.70
75.98
50
61.85
60.93
64.37
65.59
64.30
70.36
60.25
59.26
67.01
67.06
69.35
66.51
72.24
75.92
77.50
78.85
70.60
75.12
100
65.03
65.36
66.04
67.71
65.93
71.94
64.38
67.81
68.26
69.41
68.99
68.95
71.43
79.84
78.77
80.79
80.48
81.41
200
72.36
72.22
71.77
71.23
70.67
75.27
66.91
69.69
70.33
70.20
71.07
68.10
81.63
81.61
82.61
83.04
82.61
82.19
300
74.40
76.04
76.18
75.31
71.92
76.43
68.86
69.37
69.97
69.86
70.14
68.63
81.34
81.80
83.74
83.27
83.39
84.36
400
76.58
75.77
76.06
76.30
73.84
77.57
69.10
69.74
70.19
69.96
70.80
67.92
84.54
83.08
84.53
84.27
63.18
85.24
500
77.14
78.01
77.09
77.79
67.67
78.76
69.95
69.72
70.84
70.04
71.05
69.22
85.05
84.93
85.09
84.92
83.88
85.34
1000
79.35
79.42
79.16
79.27
78.53
81.06
70.97
71.48
72.07
70.81
71.44
70.92
87.01
76.68
77.00
86.03
86.67
86.86
2000
81.08
80.62
80.50
80.65
81.02
82.04
72.70
72.39
72.66
71.72
72.22
71.61
88.53
87.39
88.00
87.39
77.48
88.84
AVG
65.52
67.27
69.53
70.53
68.69
72.97
61.66
62.85
68.18
69.55
69.69
68.39
73.58
76.78
78.88
79.66
77.58
80.27
Gahd24 de
Has21 hi
10
38.03
51.17
54.50
59.85
57.59
58.88
46.87
49.00
51.76
53.06
56.24
54.46
20
44.99
50.52
58.15
59.08
57.48
59.82
46.87
47.34
51.03
53.68
55.37
54.92
30
50.20
53.14
59.37
60.57
59.08
59.78
46.87
46.87
52.31
54.21
55.46
57.47
40
57.47
55.18
58.25
60.86
57.79
60.75
46.87
47.67
53.86
55.58
56.33
54.08
50
57.85
54.53
60.30
60.47
61.02
62.57
46.87
48.39
53.36
52.26
55.78
54.77
100
62.23
64.27
63.29
62.93
62.58
64.50
48.94
51.38
54.90
55.53
56.91
57.88
200
65.80
66.95
66.15
66.24
65.97
64.25
52.20
55.83
54.65
56.80
56.02
57.47
300
67.17
67.81
67.33
64.70
66.97
64.58
51.75
55.80
55.43
57.24
58.05
57.51
400
66.82
69.04
68.47
68.43
69.52
66.74
54.77
54.50
55.98
58.50
57.06
58.12
500
66.56
69.78
69.68
70.45
61.80
67.02
56.20
56.94
57.66
57.88
59.55
57.96
1000
69.81
74.17
73.02
72.92
72.50
69.45
56.18
57.40
60.06
59.76
58.14
57.74
2000
73.77
79.19
78.79
77.82
77.90
72.42
57.14
58.19
60.22
60.50
59.65
58.01
AVG
60.06
62.98
64.77
65.36
64.18
64.23
50.96
52.44
55.10
56.25
57.05
56.70
Table 5: F1-macro scores across eight languages, comparing our method with the Mono and R¨ottger baselines.
Results are reported for all of target training sizes from 10 to 2,000. Columns represent the number of retrieved
instances. AVG denotes the mean over 12 training sizes. The best result for each language and training size is in
bold. Retrieved results that outperform the next larger Mono training size are underlined.
bas19_es
dyn21_en
for19_pt
fou18_en
implicit_en
ken20_en
ous19_ar
san20_it
xdomain_en
xdomain_tr
xplain_en
bas19_es
for19_pt
gahd24_de
has21_hi
ous19_ar
ous19_fr
san20_it
xdomain_tr
Source Tasks
Target Tasks
ar
en
es
fr
it
pt
tr
bas19_es
for19_pt
gahd24_de
has21_hi
ous19_ar
ous19_fr
san20_it
xdomain_tr
Source Languages
Target Tasks
Hate
Non-Hate
bas19_es
for19_pt
gahd24_de
has21_hi
ous19_ar
ous19_fr
san20_it
xdomain_tr
Source Labels
Target Tasks
Figure 4: Sankey diagrams of the distribution of the top four retrieved source tasks (left), languages (middle), and
labels (right) for each target task.

--- Page 16 ---

even a small number of non-English source tasks—proves beneficial for three languages in this table:
Ous19 ar, San20 it, and Gahd24 de, in most cases. However, for Xdomain tr, the results differ slightly;
English-only retrieval performs marginally better, likely due to the generality of English tasks and their
semantic similarity to the Turkish dataset.
Ous19 ar
San20 it
Gahd24 de
Xdomain tr
SIZE
20
200
2000
20000
20
200
2000
20000
20
200
2000
20000
20
200
2000
20000
English
Retrieval
20
55.75
60.46
62.22
62.22
58.37
66.30
67.01
62.23
50.30
55.72
59.79
54.79
62.39
71.47
76.53
74.01
50
64.05
65.86
66.34
55.91
68.34
68.53
62.49
56.88
56.96
60.02
58.73
56.62
76.95
77.91
73.85
57.79
200
67.67
68.11
66.86
67.22
71.48
73.41
71.48
69.73
66.88
66.37
65.66
63.72
81.84
82.17
83.61
83.44
500
69.38
68.88
67.96
66.81
75.19
74.92
67.32
73.54
70.06
69.81
63.28
62.12
85.91
85.47
84.50
75.03
2000
70.95
71.32
69.26
70.21
77.05
77.75
68.58
77.69
78.93
78.74
77.93
77.58
87.81
87.67
87.55
87.26
AVG
64.27
66.46
66.15
65.06
67.74
71.14
67.91
66.37
62.81
64.45
64.79
62.93
77.46
80.27
80.90
76.36
Multilingual
Retrieval
20
57.63
63.23
61.73
59.47
63.20
66.76
67.06
60.06
50.52
58.15
59.08
57.48
66.58
67.08
70.14
75.87
50
59.36
66.65
66.31
64.51
67.20
68.42
71.65
69.44
54.53
60.30
60.47
61.02
75.92
77.50
78.85
70.60
200
67.98
69.18
67.35
65.47
72.46
72.83
72.41
72.50
66.95
66.15
66.24
65.97
81.61
82.61
83.04
82.61
500
68.95
69.47
69.28
65.54
75.39
75.29
74.53
66.09
69.78
69.68
70.45
61.80
84.93
85.09
84.92
83.88
2000
69.52
69.77
70.15
68.27
69.27
78.36
77.57
76.95
79.19
78.79
77.82
77.90
87.39
88.00
87.39
77.48
AVG
63.94
66.82
66.41
65.20
67.68
71.00
71.06
68.55
62.98
64.77
65.36
64.18
76.78
78.88
79.66
77.58
Table 6: F1-macro scores across two strategies: English-only retrieval, and Multilingual retrieval. Results are shown
for target training sizes of 20, 50, 200, 500, 2,000, and AVG (the average over 12 training sizes). Columns represent
target languages, and sub-columns are the number of retrieved instances.
G
More about Maximum Marginal Relevance
To compare the effect of using MMR versus not using it, refer to Table 7. In this table, since each
language is presented as a row block, comparisons should be made horizontally within the two sub-tables.
Specifically, for each language, values for the same training and retrieval size (e.g., 20 train, 20 retrieved)
should be compared between the settings without and with MMR. As shown, for the remaining languages
in this table, applying MMR does not lead to significant overall performance differences. This is likely
because, even without MMR, the retrieved cross-lingual data is already sufficiently diverse, so applying
MMR has minimal additional impact.
Without MMR
With MMR
Without MMR
With MMR
SIZE
20
200
2000
20000
20
200
2000
20000
20
200
2000
20000
20
200
2000
20000
Bas19 es
20
54.37
59.72
62.52
63.08
54.20
60.15
62.73
63.18
Ous19 fr
47.21
52.68
53.93
55.05
47.25
52.58
54.31
55.13
50
60.93
64.37
65.59
64.30
59.84
64.85
64.67
62.53
48.29
52.19
52.97
55.60
48.67
52.15
54.99
54.82
200
72.22
71.77
71.23
70.67
71.84
72.29
71.28
68.80
51.54
54.06
55.80
53.63
53.70
53.79
55.06
54.43
500
78.01
77.09
77.79
67.67
77.97
75.72
76.64
74.06
53.30
52.84
55.51
55.31
51.84
53.13
54.15
53.01
2000
80.62
80.50
80.65
81.02
80.31
81.23
81.12
80.58
53.51
53.13
53.30
54.74
52.07
51.44
52.79
53.19
AVG
67.27
69.53
70.53
68.69
67.26
69.70
70.01
68.28
50.56
53.12
54.05
54.84
50.43
52.99
54.22
54.54
Ous19 ar
20
57.63
63.23
61.73
59.47
57.75
59.96
60.50
62.33
For19 pt
49.72
64.92
68.57
68.03
54.31
65.48
68.95
67.63
50
59.36
66.65
66.31
64.51
59.66
66.19
64.98
64.46
59.26
67.01
67.06
69.35
61.81
67.52
67.81
67.38
200
67.98
69.18
67.35
65.47
67.61
69.52
66.35
64.55
69.69
70.33
70.20
71.07
68.29
69.83
69.48
69.74
500
68.95
69.47
69.28
65.54
68.70
70.39
69.59
67.17
69.72
70.84
70.04
71.05
69.46
70.21
69.91
71.83
2000
69.52
69.77
70.15
68.27
70.20
70.12
69.93
68.19
72.39
72.66
71.72
72.22
72.24
70.85
71.93
72.48
AVG
63.94
66.82
66.41
65.20
64.16
66.96
65.81
64.94
62.85
68.18
69.55
69.69
63.60
68.28
69.28
69.75
Has21 hi
20
47.34
51.03
53.68
55.37
47.42
52.96
53.17
56.03
50
48.39
53.36
52.26
55.78
47.34
54.19
53.55
56.29
200
55.83
54.65
56.80
56.02
55.57
56.11
56.67
57.67
500
56.94
57.66
57.88
59.55
56.78
58.43
59.28
57.55
2000
58.19
60.22
60.50
59.65
57.37
60.02
60.05
61.10
AVG
52.44
55.10
56.25
57.05
52.38
55.22
56.08
57.37
Table 7: F1-macro scores without/with MMR for five languages (rows), across five selected training sizes and an
average (AVG) computed over 12 training sizes.

```
