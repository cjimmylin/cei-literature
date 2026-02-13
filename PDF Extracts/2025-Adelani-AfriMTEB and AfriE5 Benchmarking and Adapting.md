---
title: "2025-Adelani-AfriMTEB and AfriE5 Benchmarking and Adapting - PDF Extract"
source_pdf: "2025-Adelani-AfriMTEB and AfriE5 Benchmarking and Adapting.pdf"
pages: 15
extracted_at: "2026-02-13T09:15:42.812311"
---

# PDF Extract: 2025-Adelani-AfriMTEB and AfriE5 Benchmarking and Adapting

**Source PDF:** 2025-Adelani-AfriMTEB and AfriE5 Benchmarking and Adapting.pdf
**Total Pages:** 15

---

## Content

```
--- Page 1 ---

AfriMTEB and AfriE5: Benchmarking and Adapting Text Embedding
Models for African Languages
Kosei Uemura1
Miaoran Zhang3
David Ifeoluwa Adelani2,4
1University of Toronto
2Mila - Quebec AI Institute, McGill University
3Saarland University, Saarland Informatic Campus
4Canada CIFAR AI Chair
k.uemura@mail.utoronto.ca
mzhang@lsv.uni-saarland.de
david.adelani@mila.quebec
Abstract
Text embeddings are an essential building com-
ponent of several NLP tasks such as retrieval-
augmented generation which is crucial for pre-
venting hallucinations in LLMs. Despite the
recent release of massively multilingual MTEB
(MMTEB), African languages remain under-
represented, with existing tasks often repur-
posed from translation benchmarks such as
FLORES clustering or SIB-200. In this paper,
we introduce AfriMTEB—a regional expansion
of MMTEB covering 59 languages, 14 tasks,
and 38 datasets, including six newly added
datasets. Unlike many MMTEB datasets that
include fewer than five languages, the new ad-
ditions span 14 to 56 African languages and in-
troduce entirely new tasks, such as hate speech
detection, intent detection, and emotion clas-
sification, which were not previously covered.
Complementing this, we present AfriE5, an
adaptation of the instruction-tuned mE5 model
to African languages through cross-lingual con-
trastive distillation. Our evaluation shows that
AfriE5 achieves state-of-the-art performance,
outperforming strong baselines such as Gemini-
Embeddings and mE5.
1
Introduction
Text embeddings are core building blocks for NLP
systems in information retrieval, clustering, seman-
tic similarity, and classification (Gao et al., 2022;
Feng et al., 2022). However, evaluations on di-
verse tasks are often limited to a few high resource
languages such as English (Muennighoff et al.,
2023) or Chinese (Xiao et al., 2024). Many under-
represented languages are excluded due to lack
of datasets or non-discoverability of community-
created benchmarks (Ojo et al., 2025).
While recent text embedding benchmarks have
improved language coverage in recent years, such
as MMTEB (Enevoldsen et al., 2025), African lan-
guages remain under-represented, where many of
the tasks covered are either based on massively
Figure 1: AfriMTEB (Full): Model size vs. mean
performance. Parameter counts (billions, log scale) are
shown on the x-axis, and mean scores across AfriMTEB
(Full) tasks on the y-axis. AfriE5-large-instruct (red)
achieves the best overall performance (64.6) despite
having far fewer parameters than most 7–8B models.
evaluation of translation datasets (NLLB-Team
et al., 2022; Federmann et al., 2022), and the tasks
derived or repurposed from translation benchmarks
such as Belebele (Bandarkar et al., 2024) and SIB-
200 (Adelani et al., 2024). As a result, the quality
of text embeddings for languages in the African
region remains unknown, as the region has few
standardized tools for comparing models across
tasks and languages (Alabi et al., 2025)
In this paper, we introduce AfriMTEB, a regional
extension of MTEB tailored to African languages
and tasks. Figure 2 shows the full suite that cov-
ers 59 languages and 38 datasets spanning Bitext
mining, Classification (single, pair and multi-label),
Semantic Text Similarity, Retrieval, Clustering, and
Reranking. To support fast-and-compute friendly
evaluation, we also provide AfriMTEB-Lite, a
compact suite over nine geographically-diverse lan-
guages (Amharic, Oromo, Igbo, Yoruba, Hausa,
Swahili, Kinyarwanda, Xhosa, Zulu) constructed
arXiv:2510.23896v1  [cs.CL]  27 Oct 2025

--- Page 2 ---

Figure 2: Overview of AfriMTEB and AfriMTEB-Lite. The Full suite spans 59 languages and 38 datasets across 7
families; the Lite suite provides uniform coverage for 9 languages and 13 datasets.
by selecting, within each task family, the maxi-
mally overlapping tasks such that every task in-
cludes all nine languages, ensuring uniform lan-
guage coverage across the suite.
In addition to benchmarking, we develop AfriE5-
Large-Instruct adapting strong embedding mod-
els to African languages.
Starting from the
instruction-tuned mE5-Large-Instruct (Wang et al.,
2024a,c), we leveraged cross-lingual contrastive
distillation. We construct supervision by translating
MNLI/SNLI datasets(Williams et al., 2018; Bow-
man et al., 2015) in African languages with NLLB-
200 (3.3B) (NLLB-Team et al., 2022), followed by
automatic filtering by SSA-COMET (an African
COMET-based QE metric) (Li et al., 2025), and
expanding each example into multiple sources or
target directions to encourage cross-lingual align-
ment. We then use the receipe of BGE Re-ranker
v2 m3 (Chen et al., 2024) for text embedding model
training.
We evaluate widely used baselines, including
BGE-M3, E5 variants (e.g., e5-mistral-7b-instruct),
Qwen embeddings, Gemini embedding-001, and
Embedding Gemma (Chen et al., 2024; Wang et al.,
2024c; Zhang et al., 2025; Lee et al., 2025). On
AfriMTEB-Lite, our adapted model AfriE5-Large-
Instruct, trained only on nine African languages,
achieves an average score of 63.7, surpassing me5-
large-instruct (62.0) and Gemini embedding-001
(63.1). Remarkably, despite being tuned with data
and languages aligned to the AfriMTEB-Lite, our
model leveraged cross-lingual transfer to general-
ize to the broader AfriMTEB benchmark covering
59 languages and 38 datasets, where it also deliv-
ers the best performance with an average score of
62.4, ahead of me5-large-instruct (61.3) and Gem-
ini embedding-001 (60.6) as shown in Figure 1.
These results highlight that targeted cross-lingual
adaptation on a carefully selected subset of lan-
guages can transfer effectively to a much larger
set, yielding consistent improvements across task
families while preserving the backbone’s general
utility.
2
AfriMTEB Benchmark
AfriMTEB is a regional extension of MTEB de-
signed to evaluate text embeddings for African lan-
guages across multiple task families. To address
persistent gaps in language coverage and enable
systematic, comparable assessment, we introduce
AfriMTEBas a standardized benchmark for African
languages. It consists of a Full suite covering
59 languages and 38 datasets, and a Lite suite
that maintains uniform language coverage for 9
target languages over 13 representative datasets.
Languages are selected to span major families
and geographic regions while prioritizing practi-
cal relevance and the availability of reliable public
datasets; tasks reflect core embedding applications
and draw on established, well-curated resources.
The Lite suite supports rapid iteration by enforcing
consistent task coverage across languages through
maximal task–language overlap.
AfriMTEB follows the MTEB taxonomy and
groups tasks into eight families. Table 1 lists the
tasks, task families and the datasets included in
the Full suite. Each dataset belongs to one of the
eight task families: (1) Bibtext mining (2) Pair clas-
sification (3) Semantic Text Similarity (STS) (4)
Clustering (5) Classification (6) Multi-label Clas-

--- Page 3 ---

Task
Number of Languages
Task
Family
Datasets (AfriMTEB Full)
in MMTEB
in AfriMTEB
Bitext Mining
Btxt
Flores, NTREX, BibleNLP, NollySenti, Tatoeba
59
59
NLI
Pr Clf
XNLI, AfriXNLI
1
15
Topic class.
Clf
SIB200Classification, SIB200_14Classes
0
56
News Topic class.
Clf
MasakhaNEWS, TswanaNews, SiswatiNews, SwahiliNews
16
17
IsiZuluNews, KinNews
Sentiment
Clf
NaijaSenti, AfriSenti, MultilingualSentiment
11
12
Hate speech
Clf
AfriHate
0
14
LID
Clf
LanguageClassification, SouthAfricanLangClassification
0
18
Clf
AfriSentiLangClassification
Intent
Clf
MassiveIntent, InjongoIntent
3
16
Scenario
Clf
MassiveScenario
0
3
Emotion
Multi. Clf
EmotionAnalysisPlus
0
14
Semantic relatedness
STS
SemRel24STS
7
7
Retrieval
Rtrvl
Belebele, MIRACL, MIRACLRetrievalHardNegatives,
31
31
MrTidy, XQuAD, XM3600T2I
Clustering
Clust
SIB200ClusteringFast, MasakhaNEWSClusteringP2P
58
58
MasakhaNEWSClusteringS2S
Reranking
Rrnk
MIRACLReranking
0
2
Table 1: Tasks, task families and datasets included in AfriMTEB (Full). The task families are Bitext Mining
(Btxt), Pair Classification (Pr Clf), Classification (Clf), Semantic Text Similarity (STS), Multi-label Classification
(Multi. Clf), Retrieval (Rtrvl), Clustering (Clust) and Reranking (Rrnk). We introduce additional the five datasets
highlighted in bold.
sification (7) Retrieval (8). The first four task fam-
ilies performs a similarity related tasks based on
two pairs of sentences, either to identity translation
pairs, categorize them into a class (e.g., entailment
vs. contradiction) or provide a similarity score. The
next three tasks (5) - (6) classify a sentence or arti-
cle into one or more classes. Finally, the last sets of
tasks (7) and (8) are information retrieval tasks for
retrieval or re-ranking based on a user query. We
provide full description in Appendix A.1.
2.1
Existing MTEB datasets
AfriMTEB builds on the Massive Text Embedding
Benchmark (MTEB) by selecting tasks that in-
clude African languages. From the original bench-
mark, we inherit datasets covering bitext min-
ing (e.g., Flores, NTREX, Tatoeba), pair classi-
fication (XNLI), topic and sentiment classifica-
tion (SIB-200, AfriSenti, MasakhaNEWS), seman-
tic textual similarity (SemRel24), retrieval (MIR-
ACL, XQuAD, XM3600), clustering (SIB-200,
MasakhaNEWS), and reranking (MIRACL).
However, language coverage in these datasets
is uneven: some tasks include only a few African
languages, while others span broader multilingual
settings. To ensure fairness, we compute macro
averages over languages within each task, then av-
erage across tasks and families to obtain the overall
AfriMTEB score. This prevents any single task or
language from dominating the benchmark.
2.2
AfriMTEB-Full: Introducing 6 new
datasets
The Full suite is built by selecting datasets from
MTEB that include African languages and extending
them with six additional datasets. These additions
broaden task coverage, increase difficulty, and im-
prove language representation.
AfriXNLI (Pr Clf)
An African extension of the
XNLI benchmark that provides natural language
inference data to 15 African languages (Adelani
et al., 2025). By including AfriXNLI, we expand
language coverage for the pair classification family
beyond a single African language (Swahili), ensur-
ing broader representation of African languages in
entailment-style tasks.
Brighter Emotion Analysis (Multi. Clf).
A
multilabel emotion data set that covers 32 lan-
guages including 14 African languages (Belay
et al., 2025; Muhammad et al., 2025b). Each sen-
tence may be assigned multiple emotion labels
such as JOY, ANGER, SADNESS, or FEAR. By
including this dataset, AfriMTEB introduces the
first multi-label classification task for African lan-
guages, thereby broadening the taxonomy beyond
single-label settings.

--- Page 4 ---

AfriHate Classification (Clf)
A multilingual
hate-speech classification dataset covering 14
African languages (Muhammad et al., 2025a).
Each instance is labeled as HATE, ABUSIVE, or
NEUTRAL, providing a standardized benchmark
for toxic content detection across diverse languages
and registers. This dataset extends evaluation to
socially relevant safety applications.
Injongo Intent (Clf)
The Injongo dataset is a
multilingual resource for intent detection covering
16 African languages (Yu et al., 2025). It con-
sists of short, conversational utterances annotated
with 40 everyday intent categories, for example
requests such as “freeze account” or “play music.”
By focusing on dialogue-style classification, In-
jongo complements existing benchmarks like MAS-
SIVE (FitzGerald et al., 2023), but offers broader
African language coverage.
KinNewsClassification (Clf)
A Kinyarwanda
news topic classification dataset with labels cov-
ering domains such as politics, business, and
sports (Niyongabo et al., 2020). We include this
dataset because MasakhaNEWS does not cover Kin-
yarwanda. Adding KinNews ensures we can cover
Kinyarwanda in the AfriMTEB-Lite, since the Lite
version requires maximally overlapping tasks.
SIB-200_14Classes (Clf)
A more challenging
variant of the SIB-200 dataset where labels are
consolidated into 14 categories. This version still
includes 56 African languages but is not limited
to them (Adelani et al., 2024). By merging fine-
grained topics into broader classes, intra-class
diversity increases, which raises task difficulty.
The inclusion of this dataset not only strengthens
African language evaluation but also increases the
difficulty for other covered languages in SIB-200,
leading to more robust cross-lingual assessment.
Finally, we added SIB200Classification dataset
to complement SIB-200_14Classes in the “Clf”
task family, although not new. The only difference
is that the former covers seven categories compared
to the latter. The original MTEB only considers
SIB-200 in the Clustering (Clust) task family.
2.3
AfriMTEB-Lite construction
The Lite suite focuses on nine geographically-
diverse African languages: Amharic, Oromo, Igbo,
Yoruba, Hausa, Swahili, Kinyarwanda, Xhosa,
Zulu. We selected only those datasets from MTEB
that include nine languages to guarantee consis-
tent language–task alignment across families. The
result is a compact yet representative benchmark
of 13 datasets 1 spanning classification, retrieval,
bitext mining, clustering, pair classification, and
multi-label classification.
3
Adapting Embedding Models to
African Languages
3.1
Method
Our approach combines contrastive learning with
knowledge distillation in a unified objective. Given
a batch of B query–document groups, each with
group size G, the total loss is:
L = Lkd + Lcontrastive.
(1)
Knowledge Distillation.
The distillation term
aligns the student’s predicted distribution with the
teacher’s scores using KL divergence. Teacher’s
scores are gained during training data creation.:
Lkd = −1
B
B
X
i=1
G
X
j=1
P (i,j)
teacher log P (i,j)
student,
(2)
where P (i,j)
teacher and P (i,j)
student are normalized soft-
max scores for candidate j in group i, obtained
from the teacher reranker and the student encoder
respectively.
Contrastive Learning.
The contrastive term is
computed with in-batch (and cross-device) nega-
tives:
Lcontrastive = −1
B
B
X
i=1
log
exp(si,iG/τ)
PBG
j=1 exp(si,j/τ)
.
(3)
where si,j = qi⊤pj is the similarity between
query embedding qi and passage embedding pj,
and τ is a temperature hyperparameter. The nu-
merator contains the similarity between query qi
and its corresponding positive passage pi · G. The
denominator includes all similarities between qi
and all passages in the batch, comprising both pre-
mined hard negatives (from NLI contradiction ex-
amples and hard negative mining) and in-batch neg-
atives (other queries and passages from the same
training batch). With cross-device negative sharing
enabled, the total negative set spans all examples
across all GPUs in the distributed training setup,
providing a rich set of challenging negative exam-
ples for each query.
1We merged two datasets: MasakhaNEWS and KinNEWS
since they have similar structure, thus we report 12 datasets

--- Page 5 ---

Model
Btxt
Clf
Clust
Multi. Clf
Pr Clf
Rrnk
Rtrvl
STS
Average
Small models (<1B)
mmBERT-base
3.0
48.5
33.1
24.6
54.1
6.8
4.9
38.0
26.6
KaLM
49.9
36.3
46.8
25.9
60.0
49.3
52.8
53.4
46.8
Qwen3-Embedding 0.6B
33.6
35.9
37.6
25.2
58.0
52.9
52.0
54.1
43.7
bge-m3
70.0
40.0
47.3
26.8
66.4
66.8
70.2
58.7
55.8
mE5-large
79.7
43.3
45.3
27.7
64.3
65.2
69.2
62.5
57.2
mE5-large-instruct
85.8
49.8
61.9
28.6
63.8
61.9
74.1
64.8
61.3
AfriE5-large-instruct
85.5
49.7
62.9
29.8
67.9
64.0
75.4
63.7
62.4
Medium models (≈4B)
Qwen3-Embedding-4B
42.5
42.9
39.6
25.8
57.4
60.6
61.5
54.9
48.2
Large models (≥7B)
gte-Qwen2-7B-instruct
52.7
41.0
56.6
25.1
58.1
58.8
60.3
54.9
50.9
GritLM-7B
45.2
43.4
54.0
26.6
59.6
65.4
61.0
59.1
51.8
Linq-Embed-Mistral
45.2
43.2
55.4
27.1
59.4
65.1
59.2
62.5
52.1
SFR-Embedding-Mistral
46.3
42.5
58.0
26.2
58.9
63.8
58.1
62.0
52.0
E5 mistral 7b instruct
46.4
41.9
58.5
26.0
58.7
64.1
57.3
61.3
51.8
Qwen3-Embedding-8B
48.4
43.7
41.8
27.2
58.3
60.0
69.9
54.7
50.5
Undisclosed size
gemini embedding 001
72.2
50.0
52.7
32.7
71.6
63.4
77.5
65.0
60.6
Table 2: AfriMTEB results. Average performance of embedding models across 59 African and regionally relevant
languages grouped by task family. The final column reports the unweighted macro average across task families.
Best scores in each column are highlighted in bold.
3.2
Cross-lingual Training Data Construction
We constructed cross-lingual training data by lever-
aging large-scale natural language inference cor-
pora, a supervision signal that has proven effec-
tive for learning sentence embeddings. (Gao et al.,
2022; Reimers and Gurevych, 2019) Specifically,
we used MultiNLI and SNLI (Williams et al., 2018;
Bowman et al., 2015) as source datasets in English.
Each sentence pair was translated into the nine
African target languages using NLLB-200 (3.3B)
(NLLB-Team et al., 2022). We then estimated
translation quality by SSA-COMET-MTL (Li et al.,
2025), a COMET variant (Rei et al., 2020). and
filtered pairs below a threshold of 0.75 to ensure
the data quality.
To encourage cross-lingual alignment, each ex-
ample was expanded into multiple configurations:
(i) premise in target language and hypothesis in
source, (ii) premise in source and hypothesis in
target, (iii) both in target, and (iv) both in source,
that is,is, English. For MultiNLI, we reformulated
examples as query–positive/negative pairs (entail-
ment as pos, contradiction as neg). For SNLI, we
followed the same strategy but included all 3-way
annotations. We further increased training diffi-
culty by sampling up to 15 hard negatives per in-
stance using mE5-large-instruct.
To improve supervision, we distilled teacher
scores from the BGE Reranker v2 m3 cross-
encoder (Chen et al., 2024). Each datapoint was
thus annotated with both positive/negative pairs
and soft teacher distributions.
3.3
Experimental Settings
We fine-tuned mE5-Large-Instruct using the open-
sourced FlagEmbedding training repository based
on BGE Reranker v2 m3 recipe (Chen et al., 2024).
Training was performed with torchrun on a single
GPU. The key settings are summarized in Table 5.
We followed the default implementation of con-
trastive learning with cross-device negatives and
enabled knowledge distillation with teacher scores
provided by BGE Reranker v2 m3.
We trained for one epoch over the curated cross-
lingual dataset, with logging every 100 steps and
checkpoint saving every 100 steps. All samples
in a batch were drawn from the same dataset
(–same_dataset_within_batch) to maintain con-
sistent supervision. The resulting model is referred
to as AfriE5-Large-Instruct. We provide brief de-
scriptions of the baseline models in Appendix A.2.
4
Results
4.1
AfriMTEB results
Smaller sized E5 variants have comparable per-
formance to Gemini Embedding
Despite being
listed under small models (< 1B), the E5 family
matches or surpasses the proprietary model on aver-
age AfriMTEB score. AfriE5-Large-Instruct attains
the best macro average at 62.4, edging out Gemini

--- Page 6 ---

Belebele
Flores
News
NTREX
SIB-200
Model
Hate
Senti
NLI
Retrvl
Emo
Btxt
Intent
TC
Btxt
14Classes
Class
Clust
Avg
Small models (<1B)
mmBERT-base
48.2
39.9
54.0
4.0
27.3
1.8
72.5
55.1
2.2
2.4
34.2
5.0
28.9
KaLM
48.5
44.3
61.0
51.0
28.9
53.2
63.4
74.6
58.6
7.3
48.9
16.8
46.4
Qwen3-Embedding 0.6B
48.6
41.5
58.1
46.3
28.1
33.0
68.5
70.5
38.1
3.5
40.0
12.0
40.7
EmbeddingGemma 300m
45.4
39.0
53.6
10.6
26.6
12.2
49.4
59.0
17.9
1.4
29.6
4.6
29.1
bge-m3
50.1
47.9
68.7
69.9
29.4
78.1
75.4
72.7
80.4
10.2
55.6
21.0
55.0
mE5-large
49.8
48.9
65.2
69.9
31.3
86.9
77.1
77.7
88.7
11.6
60.4
25.6
57.8
mE5-large-instruct
51.5
47.0
64.5
75.7
31.5
91.4
75.5
78.8
91.5
22.0
71.2
43.9
62.0
AfriE5-large-instruct
51.7
50.7
69.0
77.7
32.8
91.2
75.4
79.5
92.0
26.2
72.0
45.7
63.7
Medium models (≈4B)
Qwen3-Embedding-4B
50.0
41.2
56.8
58.3
28.3
47.7
70.1
76.0
49.0
7.9
49.2
17.5
46.0
Large models (≥7B)
gte-Qwen2-7B-instruct
46.0
43.5
58.6
55.6
27.8
58.4
57.1
79.8
60.0
10.4
50.8
22.4
47.5
GritLM-7B
51.4
45.6
59.8
55.0
29.6
46.5
70.8
75.3
52.0
8.8
50.8
22.2
47.3
Linq-Embed-Mistral
51.0
43.8
59.7
52.1
30.0
46.7
70.3
76.5
52.0
7.6
50.7
22.1
46.9
SFR-Embedding-Mistral
49.3
44.5
58.9
50.9
28.8
47.7
62.5
77.0
53.0
8.5
49.7
21.9
46.1
E5 mistral 7b instruct
49.0
45.7
58.7
50.2
28.6
47.9
61.8
76.0
53.3
7.2
49.2
21.8
45.8
Qwen3-Embedding 8B
50.8
46.2
58.8
68.3
29.1
58.3
67.7
77.6
57.3
8.0
53.5
20.9
49.7
Undisclosed size
gemini embedding 001
55.0
53.8
75.3
83.6
35.5
88.1
83.9
76.8
84.2
17.7
69.2
34.6
63.1
Table 3: AfriMTEB-Lite results. Average performance of embedding models across nine African languages (AMH,
GAZ, HAU, IBO, KIN, SWA, XHO, YOR, ZUL) on 12 tasks. Columns report task-level averages, and the final
column gives the unweighted macro average across tasks. Best scores per column are highlighted in bold.
embedding (60.6) and mE5-Large-Instruct (61.3) in
Table 2. This indicates that strong multilingual cov-
erage and targeted adaptation can outweigh model
size or access to proprietary training data.
Gemini Embedding excels on classification tasks
over E5 variants
While E5 variants lead over-
all, Gemini embedding 001 is strongest on most
classification-style families: single-label classifi-
cation (50.0 vs. 49.8 for mE5-Large-Instructand
49.7 for AfriE5-Large-Instruct), multi-label clas-
sification (32.7 vs. 28.6/29.8), and pair classifi-
cation (71.6 vs. 63.8/67.9). It also tops retrieval
(77.5) and semantic textual similarity (65.0). These
strengths suggest Gemini’s instruction/data mix
particularly benefits discriminative judgment tasks
and sentence-level similarity scoring.
Language coverage is more crucial than text em-
bedding model sizes
Large 7B and 8B encoders
do not translate into higher AfriMTEB scores. All
7B/8B models cluster in the low–mid 50s, for ex-
ample, gte-Qwen2-7B-instruct at 50.9, GritLM-7B
at 51.8, Qwen3-Embedding-8B at 50.5. Thay are
clearly below the smaller E5 variants of around
61.3 point. This gap underscores that broad, bal-
anced language coverage and task diversity matter
more than parameter count alone.
AfriE5 and mE5 excel on Bitext mining and
clustering
On bitext mining, mE5-Large-Instruct
and AfriE5-Large-Instruct have comparable perfor-
mance of 85 points, both are far ahead of other
opens and the API baseline (Gemini embedding
at 72.2).
For clustering, AfriE5-Large-Instruct
leads with 62.9 and mE5-Large-Instruct is next
(61.9), while larger models and Gemini embed-
dings behind. These families reward models that
learn language-agnostic semantic spaces with ro-
bust cross-lingual alignment, which appears to be
a particular strength of the E5 lineage.
AfriE5 generalizes to 59 languages despite train-
ing on only 9
Although AfriE5-Large-Instruct is
adapted using supervision centered on nine African
languages (AfriMTEB), it achieves the highest Full-
suite average (62.4) across 59 languages. Rela-
tive to mE5-Large-Instruct, AfriE5-Large-Instruct
shows consistent family-level gains on pair classifi-
cation (+4.1), reranking (+2.1), retrieval (+1.3),
clustering (+1.0), and multi-label classification
(+1.2), with small trade-offs on bitext mining
(–0.3), single-label classification (–0.1), and STS
(–1.1). This pattern indicates that targeted cross-
lingual distillation can yield transferable gains
beyond the training languages, particularly for
retrieval-style tasks.
AfriE5 improves reranking with knowledge dis-
tillation
Although the base model mE5-Large-
Instruct records a reranking score of 61.9, AfriE5-
Large-Instruct raises this to 64.0. It also surpasses
gemini embedding 001 (63.4) on the same task

--- Page 7 ---

(Table 2). This improvement can be attributed to
the training recipe, where AfriE5-Large-Instruct
leverages knowledge distillation from the BGE-
M3 cross-encoder in addition to contrastive su-
pervision. The result suggests that incorporating
reranker-derived soft labels enhances cross-lingual
alignment for ranking-style objectives.
4.2
AfriMTEB-Lite Results
Here, we described the overall aggregated results
by datasets and languages in Table 3 and Figure 3.
The comprehensive results are in Appendix A.4.
AfriE5 achieved overall best performance over
other models
On the Lite suite of nine African
languages and twelve tasks, AfriE5-Large-Instruct
attains the best overall score with an average of
63.7, compared to 62.0 for mE5-Large-Instruct and
the same performance of 63.1 as Gemini embed-
ding (Table 3). Although the performance advan-
tage is not uniform across all task families, AfriE5
consistently remains competitive and often sur-
passes both baselines on challenging benchmarks
such as AfriXNLI and the SIB200 variants. These
results highlight that adapting mE5 with cross-
lingual contrastive distillation improves its effec-
tiveness for African languages, even when trained
on a compact set of nine languages.
Our adaptation boosts classification tasks,
especially SIB200-14
Relative to mE5-Large-
Instruct, AfriE5-Large-Instruct shows clear im-
provements on several classification benchmarks.
It achieves higher scores on AfriSentiment (+3.7),
AfriXNLI (+4.5), and SIB200 clustering (+1.8).
The largest gain appears on SIB200-14 classifica-
tion (+4.4; 26.2 vs. 21.8), a setting that requires
grouping semantically diverse texts into broad topi-
cal categories. These improvements indicate that
the cross-lingual, NLI-style contrastive learning
used in AfriE5 strengthens semantic alignment
across languages, leading to more effective cross-
lingual transfer for classification and clustering
tasks.
5
Ablation
We conduct controlled experiments where all
training settings are held fixed (base architecture,
loss, knowledge distillation from BGE reranker,
batch/group sizes, number of steps, and sampling)
while varying a single factor at a time. We report
AfriMTEB-Lite results in Table 4.
Impact of cross-lingual dataset expansion
As
described in Section §3.2, comparing row 1 (×,
0.75) and row 3 (✓, 0.75), the average increases
from 62.3 to 63.2. The cross-lingual expansion
of the data set exposes the model to richer cross-
lingual contrasts: First, higher scores on bitext min-
ing tasks show that the expansion improves the
model’s ability to align semantically equivalent
sentences between languages, producing a more
coherent multilingual embedding space. Second,
classification tasks such as SIB200-14 benefit from
this stronger alignment, as the model learns to ab-
stract over diverse topical domains without relying
on language-specific cues.
Machine translation quality threshold (QE)
With expansion enabled (rows 2–4), the best over-
all score is achieved after filtering using a COMET
variant, SSA-COMET-MTL QE=0.75 (63.2), com-
pared to 62.5 at 0.67 and a sharp drop to 58.3 at
0.80. A low threshold (0.67) retains large noisy
translations (around 433K training samples), which
slightly hurts reasoning-heavy tasks. In contrast,
a high threshold (0.80) filters out too much data
(remaining only 7500 samples), reducing linguistic
and semantic diversity and leading to weaker trans-
fer, especially in classification. The middle ground
(0.75) balances translation quality with coverage
with around 60K samples, yielding the most reli-
able improvements across tasks. We provide the
number of samples retained by SSA-COMET-MTL
in Appendix A.3
6
Related Work
African benchmarks
A number of African
NLP benchmarks focus on text classification
and related tasks.
AfroBench aggregates mul-
tiple tasks and languages with an emphasis on
broad coverage (Ojo et al., 2025). News topic
classification resources include MasakhaNEWS
and earlier Kinyarwanda/Kirundi corpora (KIN-
NEWS/KIRNEWS) (Adelani et al., 2023; Niy-
ongabo et al., 2020). Sentiment and toxicity are
covered by AfriSenti, NaijaSenti, and AfriHate
(Muhammad et al., 2023, 2022, 2025a). The SIB-
200 suite provides large-scale topic classification
with stronger representation of African languages
(Adelani et al., 2024). Intent and slot-filling are
addressed by INJONGO (Yu et al., 2025). These
resources underscore the need for region-specific
evaluation and supply tasks that align well with
sentence-embedding assessment.

--- Page 8 ---

Figure 3: Performance on AfriMTEB-Lite across nine target languages. Bars show mean scores by language
for four representative embedding models. AfriE5-large-instruct consistently achieves the highest or near-highest
scores.
Flores
News
NTREX
SIB-200
SIB-200
SIB-200
Avg
Cross-lingual Expansion
QE Thres.
Hate
Senti
NLI
Emo
Btxt
Intent
TC
Btxt
14Classes
Class
Clust
Avg
✓
0.67
52.2
50.9
66.3
32.3
91.6
77.6
82.7
94.1
23.8
71.7
44.8
62.5
✓
0.70
51.3
52.0
69.0
32.6
91.3
75.2
79.5
92.2
26.9
73.1
45.5
62.6
✓
0.75
51.4
53.3
69.1
32.8
91.2
77.1
82.6
93.8
26.2
72.0
45.7
63.2
✓
0.80
51.5
49.9
68.2
29.8
88.2
85.9
79.9
91.0
11.2
61.8
24.2
58.3
×
0.75
52.3
52.8
68.2
32.0
88.5
81.2
82.0
91.2
21.8
70.6
45.2
62.3
Table 4: Ablation study of AfriE5-large-instruct on AfriMTEB-Lite. Columns match the benchmark layout
in Table 3. We vary the use of cross-lingual dataset expansion and the translation quality threshold (QE) during
filtering.
Multilingual text embedding benchmarks
The
Massive Text Embedding Benchmark (MTEB) in-
troduced a common taxonomy and leaderboard for
sentence embeddings (Muennighoff et al., 2023).
Since then, several language- or region-specific
variants have emerged, including MMTEB (with
Europe and Indic tracks), SEA-BED for South-
east Asia, PL-MTEB for Polish, and MTEB-
French (Ponwitayarat et al., 2025; Po´swiata et al.,
2024; Ciancone et al., 2024). Additional efforts
target specific language families or regions: C-
MTEB (Chinese), German-focused suites, JMTEB
(Japanese), Korean-focused suites, ruMTEB (Rus-
sian), FaMTEB (Persian/Farsi), and VN-MTEB
(Vietnamese) (Xiao et al., 2024; Wehrli et al., 2024;
Li et al., 2024; Snegirev et al., 2025; Zinvandi et al.,
2025; Pham et al., 2025). Our work follows this
trend by building an Africa-focused extension with
broad task coverage.
Multilingual text embedding models
Com-
mercial/API models widely used in practice in-
clude OpenAI’s text-embedding-3 series, Google’s
gemini-embedding-001, and Cohere’s Embed v3
(Neelakantan et al., 2022; Lee et al., 2025). Open-
weight models are an active research area: me5, e5,
and e5-mistral-7b-instruct provide strong general-
purpose and instruction-tuned baselines (Wang
et al., 2024c,a); Qwen3-Embedding and Embed-
ding Gemma offer lightweight multilingual options
(Zhang et al., 2025; Vera et al., 2025); GTE pro-
poses efficient, general-purpose embeddings (Li
et al., 2023a); and classic multilingual encoders
LaBSE remain strong references (Feng et al., 2022).
The recent BGE-M3 model integrates multilingual,
multi-function training and is a competitive open
baseline (Chen et al., 2024). Despite progress, cov-
erage and performance on many African languages
remain uneven, motivating region-specific evalua-
tion and targeted adaptation.
7
Conclusion
We presented AfriMTEB, a large-scale benchmark
for African languages spanning 59 languages and
14 tasks, and AfriE5, an adaptation of mE5-large-
instruct via cross-lingual contrastive distillation.
AfriE5 achieves state-of-the-art results on both
AfriMTEB-Full and Lite, surpassing strong base-
lines such as Gemini embedding-001. Our abla-
tions show that cross-lingual dataset expansion and
balanced translation filtering are crucial for these
gains. AfriMTEB and AfriE5 provide standardized
evaluation and a strong baseline to advance text

--- Page 9 ---

embedding research for African languages.
8
Limitations
AfriMTEB expands coverage to 59 languages, yet
many African languages, dialects, orthographies,
and code-switched registers remain underrepre-
sented. Several datasets inherit noise or hetero-
geneity from crowd labels, repurposed tasks, and
preprocessing; our adaptation data further relies
on machine translation (NLLB-200) and automatic
quality estimation (SSA-COMET), which vary in
reliability across language pairs and domains. Dis-
tillation from a single teacher (BGE Reranker v2
m3) can also transfer its biases, potentially ad-
vantaging languages and styles that align with the
MT/QE pipeline and the teacher’s preferences.
Our evaluation focuses on text-only sen-
tence/paragraph embeddings and macro-averages
across tasks and languages; alternative weightings
(e.g., by population or application criticality) and
additional metrics (calibration, robustness, fair-
ness) could yield different conclusions. End-to-end
RAG quality, multimodal retrieval, and very long-
context document embeddings are out of scope,
and domain coverage skews toward formal/news
text over colloquial or specialized domains. True
parity with closed-weight baselines (e.g., data mix-
tures, architectures, inference settings) is infeasi-
ble; repeated API evaluations may be affected by
nondeterminism, and some open models may be
sensitive to prompt formats or poolers we did not
exhaustively tune.
Finally, benchmark contamination remains pos-
sible because public corpora are widely used in
pretraining, which can inflate absolute scores. Our
single-GPU fine-tuning recipe favors accessibil-
ity over peak performance and may limit stabil-
ity, and releasing full translation/provenance arte-
facts is nontrivial due to size and licensing. While
AfriE5 trained on nine languages generalizes well
to 59 in our tests, transfer may degrade for typo-
logically distant or extremely low-resource lan-
guages; broader community datasets and multi-
teacher/multi-signal training are promising avenues
to mitigate these limitations.
References
David Ifeoluwa Adelani, Hannah Liu, Xiaoyu Shen,
Nikita Vassilyev, Jesujoba O. Alabi, Yanke Mao, Hao-
nan Gao, and Annie En-Shiun Lee. 2024. Sib-200:
A simple, inclusive, and big evaluation dataset for
topic classification in 200+ languages and dialects.
Preprint, arXiv:2309.07445.
David Ifeoluwa Adelani, Marek Masiak, Israel Abebe
Azime, Jesujoba Alabi, Atnafu Lambebo Tonja, and
et. al. 2023. Masakhanews: News topic classification
for african languages. Preprint, arXiv:2304.09972.
David Ifeoluwa Adelani, Jessica Ojo, Israel Abebe Az-
ime, Jian Yun Zhuang, Jesujoba Oluwadara Alabi,
Xuanli He, Millicent Ochieng, Sara Hooker, Andiswa
Bukula, En-Shiun Annie Lee, Chiamaka Ijeoma
Chukwuneke, Happy Buzaaba, Blessing Kudzaishe
Sibanda, Godson Koffi Kalipe, Jonathan Mukiibi,
Salomon Kabongo Kabenamualu, Foutse Yuehgoh,
Mmasibidi Setaka, Lolwethu Ndolela, and 8 others.
2025. IrokoBench: A new benchmark for African
languages in the age of large language models. In
Proceedings of the 2025 Conference of the Nations
of the Americas Chapter of the Association for Com-
putational Linguistics: Human Language Technolo-
gies (Volume 1: Long Papers), pages 2732–2757,
Albuquerque, New Mexico. Association for Compu-
tational Linguistics.
Jesujoba O Alabi, Michael A Hedderich, David Ife-
oluwa Adelani, and Dietrich Klakow. 2025. Chart-
ing the landscape of african nlp: Mapping progress
and shaping the road ahead.
arXiv preprint
arXiv:2505.21315.
Lucas Bandarkar, Davis Liang, Benjamin Muller, Mikel
Artetxe, Satya Narayan Shukla, Donald Husa, Naman
Goyal, Abhinandan Krishnan, Luke Zettlemoyer, and
Madian Khabsa. 2024. The belebele benchmark: a
parallel reading comprehension dataset in 122 lan-
guage variants. In Proceedings of the 62nd Annual
Meeting of the Association for Computational Lin-
guistics (Volume 1: Long Papers), pages 749–775,
Bangkok, Thailand. Association for Computational
Linguistics.
Tadesse Destaw Belay, Israel Abebe Azime, Abinew Ali
Ayele, Grigori Sidorov, Dietrich Klakow, Philip
Slusallek, Olga Kolesnikova, and Seid Muhie Yimam.
2025. Evaluating the capabilities of large language
models for multi-label emotion understanding. In
Proceedings of the 31st International Conference on
Computational Linguistics, pages 3523–3540, Abu
Dhabi, UAE. Association for Computational Linguis-
tics.
Samuel R. Bowman, Gabor Angeli, Christopher Potts,
and Christopher D. Manning. 2015. A large anno-
tated corpus for learning natural language inference.
Preprint, arXiv:1508.05326.
Jianlv Chen, Shitao Xiao, Peitian Zhang, Kun Luo, Defu
Lian, and Zheng Liu. 2024. Bge m3-embedding:
Multi-lingual, multi-functionality, multi-granularity
text embeddings through self-knowledge distillation.
Preprint, arXiv:2402.03216.
Mathieu Ciancone, Imene Kerboua, Marion Schaeffer,
and Wissam Siblini. 2024. Mteb-french: Resources

--- Page 10 ---

for french sentence embedding evaluation and analy-
sis. Preprint, arXiv:2405.20468.
Alexis Conneau, Kartikay Khandelwal, Naman Goyal,
Vishrav Chaudhary, Guillaume Wenzek, Francisco
Guzmán, Edouard Grave, Myle Ott, Luke Zettle-
moyer, and Veselin Stoyanov. 2020.
Unsuper-
vised cross-lingual representation learning at scale.
Preprint, arXiv:1911.02116.
Kenneth Enevoldsen, Isaac Chung, Imene Kerboua,
Márton Kardos,
Ashwin Mathur,
David Stap,
Jay Gala, Wissam Siblini, Dominik Krzemi´nski,
Genta Indra Winata, Saba Sturua, Saiteja Utpala,
Mathieu Ciancone, Marion Schaeffer, Diganta Misra,
Shreeya Dhakal, Jonathan Rystrøm, Roman Solo-
matin, Ömer Veysel Ça˘gatan, and 63 others. 2025.
MMTEB: Massive multilingual text embedding
benchmark. In The Thirteenth International Con-
ference on Learning Representations.
Christian Federmann, Tom Kocmi, and Ying Xin. 2022.
NTREX-128 – news test references for MT evalua-
tion of 128 languages. In Proceedings of the First
Workshop on Scaling Up Multilingual Evaluation,
pages 21–24, Online. Association for Computational
Linguistics.
Fangxiaoyu Feng, Yinfei Yang, Daniel Cer, Naveen
Arivazhagan, and Wei Wang. 2022.
Language-
agnostic bert sentence embedding.
Preprint,
arXiv:2007.01852.
Jack FitzGerald, Christopher Hench, Charith Peris,
Scott Mackie, Kay Rottmann, Ana Sanchez, Aaron
Nash, Liam Urbach, Vishesh Kakarala, Richa Singh,
Swetha Ranganath, Laurie Crist, Misha Britan,
Wouter Leeuwis, Gokhan Tur, and Prem Natara-
jan. 2023.
MASSIVE: A 1M-example multilin-
gual natural language understanding dataset with
51 typologically-diverse languages. In Proceedings
of the 61st Annual Meeting of the Association for
Computational Linguistics (Volume 1: Long Papers),
pages 4277–4302, Toronto, Canada. Association for
Computational Linguistics.
Tianyu Gao, Xingcheng Yao, and Danqi Chen. 2022.
Simcse: Simple contrastive learning of sentence em-
beddings. Preprint, arXiv:2104.08821.
Xinshuo Hu, Zifei Shan, Xinping Zhao, Zetian Sun,
Zhenyu Liu, Dongfang Li, Shaolin Ye, Xinyuan Wei,
Qian Chen, Baotian Hu, and 1 others. 2025. Kalm-
embedding: Superior training data brings a stronger
embedding model. arXiv preprint arXiv:2501.01028.
Junseong Kim, Seolhwa Lee, Jihoon Kwon, Sangmo
Gu, Yejin Kim, Minkyung Cho, Jy yong Sohn, and
Chanyeol Choi. 2024. Linq-embed-mistral:elevating
text retrieval with improved gpt data through task-
specific control and quality refinement. Linq AI Re-
search Blog.
Jinhyuk Lee, Feiyang Chen, Sahil Dua, Daniel
Cer, Madhuri Shanbhogue, Iftekhar Naim, Gus-
tavo Hernández Ábrego, Zhe Li, Kaifeng Chen, Hen-
rique Schechter Vera, Xiaoqi Ren, Shanfeng Zhang,
Daniel Salz, Michael Boratko, Jay Han, Blair Chen,
Shuo Huang, Vikram Rao, Paul Suganthan, and 28
others. 2025. Gemini embedding: Generalizable em-
beddings from gemini. Preprint, arXiv:2503.07891.
Senyu Li, Jiayi Wang, Felermino D. M. A. Ali, Colin
Cherry, Daniel Deutsch, Eleftheria Briakou, Rui
Sousa-Silva, Henrique Lopes Cardoso, Pontus Stene-
torp, and David Ifeoluwa Adelani. 2025. Ssa-comet:
Do llms outperform learned metrics in evaluating mt
for under-resourced african languages?
Preprint,
arXiv:2506.04557.
Shengzhe
Li,
Masaya
Ohagi,
and
Ryokan
Ri.
2024.
JMTEB: Japanese Massive Text Em-
bedding Benchmark. https://huggingface.co/
datasets/sbintuitions/JMTEB.
Zehan Li, Xin Zhang, Yanzhao Zhang, Dingkun Long,
Pengjun Xie, and Meishan Zhang. 2023a. Towards
general text embeddings with multi-stage contrastive
learning. Preprint, arXiv:2308.03281.
Zehan Li, Xin Zhang, Yanzhao Zhang, Dingkun Long,
Pengjun Xie, and Meishan Zhang. 2023b. Towards
general text embeddings with multi-stage contrastive
learning. arXiv preprint arXiv:2308.03281.
Marc Marone, Orion Weller, William Fleshman, Eu-
gene Yang, Dawn Lawrie, and Benjamin Van
Durme. 2025. mmbert: A modern multilingual en-
coder with annealed language learning. Preprint,
arXiv:2509.06888.
Rui Meng, Ye Liu, Shafiq Rayhan Joty, Caiming
Xiong, Yingbo Zhou, and Semih Yavuz. 2024. Sfr-
embedding-mistral:enhance text retrieval with trans-
fer learning. Salesforce AI Research Blog.
Niklas Muennighoff, Hongjin Su, Liang Wang, Nan
Yang, Furu Wei, Tao Yu, Amanpreet Singh, and
Douwe Kiela. 2024. Generative representational in-
struction tuning. Preprint, arXiv:2402.09906.
Niklas Muennighoff, Nouamane Tazi, Loïc Magne, and
Nils Reimers. 2023. Mteb: Massive text embedding
benchmark. Preprint, arXiv:2210.07316.
Shamsuddeen Hassan Muhammad, Idris Abdulmu-
min, Abinew Ali Ayele, David Ifeoluwa Adelani,
Ibrahim Said Ahmad, Saminu Mohammad Aliyu,
Nelson Odhiambo Onyango, Lilian D. A. Wanzare,
Samuel Rutunda, Lukman Jibril Aliyu, Esubalew
Alemneh, Oumaima Hourrane, Hagos Tesfahun Ge-
bremichael, Elyas Abdi Ismail, Meriem Beloucif,
Ebrahim Chekol Jibril, Andiswa Bukula, Roowei-
ther Mabuya, Salomey Osei, and 8 others. 2025a.
Afrihate: A multilingual collection of hate speech
and abusive language datasets for african languages.
Preprint, arXiv:2501.08284.
Shamsuddeen Hassan Muhammad, Idris Abdulmumin,
Abinew Ali Ayele, Nedjma Ousidhoum, David Ife-
oluwa Adelani, Seid Muhie Yimam, Ibrahim Sa’id
Ahmad, Meriem Beloucif, Saif M. Mohammad, Se-
bastian Ruder, Oumaima Hourrane, Pavel Brazdil,

--- Page 11 ---

Felermino Dário Mário António Ali, Davis David,
Salomey Osei, Bello Shehu Bello, Falalu Ibrahim,
Tajuddeen Gwadabe, Samuel Rutunda, and 7 oth-
ers. 2023.
Afrisenti: A twitter sentiment anal-
ysis benchmark for african languages.
Preprint,
arXiv:2302.08956.
Shamsuddeen Hassan Muhammad, David Ifeoluwa Ade-
lani, Sebastian Ruder, Ibrahim Said Ahmad, Idris
Abdulmumin, Bello Shehu Bello, Monojit Choud-
hury, Chris Chinenye Emezue, Saheed Salahudeen
Abdullahi, Anuoluwapo Aremu, Alipio Jeorge, and
Pavel Brazdil. 2022. Naijasenti: A nigerian twitter
sentiment corpus for multilingual sentiment analysis.
Preprint, arXiv:2201.08277.
Shamsuddeen Hassan Muhammad, Nedjma Ousid-
houm, Idris Abdulmumin, Jan Philip Wahle, Terry
Ruas, Meriem Beloucif, Christine de Kock, Nirmal
Surange, Daniela Teodorescu, Ibrahim Said Ahmad,
David Ifeoluwa Adelani, Alham Fikri Aji, Felermino
D. M. A. Ali, Ilseyar Alimova, Vladimir Araujo,
Nikolay Babakov, Naomi Baes, Ana-Maria Bucur,
Andiswa Bukula, and 29 others. 2025b. Brighter:
Bridging the gap in human-annotated textual emo-
tion recognition datasets for 28 languages. Preprint,
arXiv:2502.11926.
Arvind Neelakantan, Tao Xu, Raul Puri, Alec Rad-
ford, Jesse Michael Han, Jerry Tworek, Qiming
Yuan, Nikolas Tezak, Jong Wook Kim, Chris Hallacy,
Johannes Heidecke, Pranav Shyam, Boris Power,
Tyna Eloundou Nekoul, Girish Sastry, Gretchen
Krueger, David Schnurr, Felipe Petroski Such, Kenny
Hsu, and 6 others. 2022.
Text and code em-
beddings by contrastive pre-training.
Preprint,
arXiv:2201.10005.
Rubungo Andre Niyongabo, Hong Qu, Julia Kreutzer,
and Li Huang. 2020. Kinnews and kirnews: Bench-
marking cross-lingual text classification for kin-
yarwanda and kirundi. Preprint, arXiv:2010.12174.
NLLB-Team, Marta R. Costa-jussà, James Cross, Onur
Çelebi, Maha Elbayad, Kenneth Heafield, Kevin Hef-
fernan, Elahe Kalbassi, Janice Lam, Daniel Licht,
Jean Maillard, Anna Sun, Skyler Wang, Guillaume
Wenzek, Al Youngblood, Bapi Akula, Loic Barrault,
Gabriel Mejia Gonzalez, Prangthip Hansanti, and
20 others. 2022.
No language left behind: Scal-
ing human-centered machine translation. Preprint,
arXiv:2207.04672.
Jessica Ojo, Odunayo Ogundepo, Akintunde Oladipo,
Kelechi Ogueji, Jimmy Lin, Pontus Stenetorp, and
David Ifeoluwa Adelani. 2025. Afrobench: How
good are large language models on african languages?
Preprint, arXiv:2311.07978.
Loc Pham, Tung Luu, Thu Vo, Minh Nguyen, and Viet
Hoang. 2025. Vn-mteb: Vietnamese massive text
embedding benchmark. Preprint, arXiv:2507.21500.
Wuttikorn Ponwitayarat, Raymond Ng, Jann Railey
Montalan, Thura Aung, Jian Gang Ngui, Yosephine
Susanto, William Tjhi, Panuthep Tasawong, Erik
Cambria, Ekapol Chuangsuwanich, Sarana Nu-
tanong, and Peerat Limkonchotiwat. 2025.
Sea-
bed: Southeast asia embedding benchmark. Preprint,
arXiv:2508.12243.
Rafał
Po´swiata,
Sławomir
Dadas,
and
Michał
Perełkiewicz. 2024. Pl-mteb: Polish massive text
embedding benchmark. Preprint, arXiv:2405.10138.
Ricardo Rei, Craig Stewart, Ana C Farinha, and Alon
Lavie. 2020. COMET: A neural framework for MT
evaluation. In Proceedings of the 2020 Conference
on Empirical Methods in Natural Language Process-
ing (EMNLP), pages 2685–2702, Online. Association
for Computational Linguistics.
Nils Reimers and Iryna Gurevych. 2019. Sentence-bert:
Sentence embeddings using siamese bert-networks.
Preprint, arXiv:1908.10084.
Artem Snegirev, Maria Tikhonova, Anna Maksimova,
Alena Fenogenova, and Alexander Abramov. 2025.
The russian-focused embedders’ exploration: rumteb
benchmark and russian embedding model design.
Preprint, arXiv:2408.12503.
Henrique Schechter Vera, Sahil Dua, Biao Zhang,
Daniel Salz, and et. al. 2025. Embeddinggemma:
Powerful and lightweight text representations.
Preprint, arXiv:2509.20354.
Liang Wang, Nan Yang, Xiaolong Huang, Binx-
ing Jiao, Linjun Yang, Daxin Jiang, Rangan Ma-
jumder, and Furu Wei. 2024a. Text embeddings by
weakly-supervised contrastive pre-training. Preprint,
arXiv:2212.03533.
Liang Wang, Nan Yang, Xiaolong Huang, Linjun Yang,
Rangan Majumder, and Furu Wei. 2024b. Improv-
ing text embeddings with large language models.
Preprint, arXiv:2401.00368.
Liang Wang, Nan Yang, Xiaolong Huang, Linjun Yang,
Rangan Majumder, and Furu Wei. 2024c.
Mul-
tilingual e5 text embeddings: A technical report.
Preprint, arXiv:2402.05672.
Benjamin Warner, Antoine Chaffin, Benjamin Clavié,
Orion Weller, Oskar Hallström, Said Taghadouini,
Alexis Gallagher, Raja Biswas, Faisal Ladhak, Tom
Aarsen, Griffin Thomas Adams, Jeremy Howard, and
Iacopo Poli. 2025. Smarter, better, faster, longer:
A modern bidirectional encoder for fast, memory
efficient, and long context finetuning and inference.
In Proceedings of the 63rd Annual Meeting of the
Association for Computational Linguistics (Volume
1: Long Papers), pages 2526–2547, Vienna, Austria.
Association for Computational Linguistics.
Silvan Wehrli, Bert Arnrich, and Christopher Irrgang.
2024. German text embedding clustering benchmark.
Preprint, arXiv:2401.02709.

--- Page 12 ---

Adina Williams, Nikita Nangia, and Samuel R. Bow-
man. 2018. A broad-coverage challenge corpus for
sentence understanding through inference. Preprint,
arXiv:1704.05426.
Shitao Xiao, Zheng Liu, Peitian Zhang, Niklas Muen-
nighoff, Defu Lian, and Jian-Yun Nie. 2024. C-pack:
Packed resources for general chinese embeddings.
Preprint, arXiv:2309.07597.
Hao Yu, Jesujoba O. Alabi, Andiswa Bukula, Jian Yun
Zhuang, En-Shiun Annie Lee, Tadesse Kebede
Guge, Israel Abebe Azime, Happy Buzaaba, Bless-
ing Kudzaishe Sibanda, Godson K. Kalipe, Jonathan
Mukiibi, Salomon Kabongo Kabenamualu, Mma-
sibidi Setaka, Lolwethu Ndolela, Nkiruka Odu,
Rooweither Mabuya, Shamsuddeen Hassan Muham-
mad, Salomey Osei, Sokhar Samb, and 3 others. 2025.
Injongo: A multicultural intent detection and slot-
filling dataset for 16 african languages. Preprint,
arXiv:2502.09814.
Yanzhao Zhang, Mingxin Li, Dingkun Long, Xin Zhang,
Huan Lin, Baosong Yang, Pengjun Xie, An Yang,
Dayiheng Liu, Junyang Lin, Fei Huang, and Jingren
Zhou. 2025. Qwen3 embedding: Advancing text
embedding and reranking through foundation models.
Preprint, arXiv:2506.05176.
Erfan Zinvandi, Morteza Alikhani, Mehran Sarmadi,
Zahra Pourbahman, Sepehr Arvin, Reza Kazemi,
and Arash Amini. 2025. Famteb: Massive text em-
bedding benchmark in persian language. Preprint,
arXiv:2502.11571.
A
Appendix
A.1
Task categories
AfriMTEB follows the MTEB taxonomy and
groups tasks into eight families. Table 1 lists the
families and the datasets included in the Full suite.
Bitext Mining.
Given two sentence sets from dif-
ferent languages, the task is to identify translation
pairs. Embeddings are used to compute similarities
and find the best match for each sentence.
Pair Classification.
This task involves a pair of
input sentences with a binary or categorical rela-
tionship label (e.g., entailment vs. contradiction).
Predictions are based on embedding similarity.
Classification.
Single-text classification where
each input is mapped to one label among several
categories (e.g., topic, sentiment, hate speech, or
language ID). A linear classifier is trained on top
of embeddings.
Multi-label Classification.
Texts may be as-
signed multiple labels simultaneously (e.g., emo-
tions). A multi-label classifier is applied on top of
embeddings to handle overlapping categories.
Clustering.
Given a collection of texts, the task
is to group them into clusters that correspond to
gold categories. Embeddings are clustered with
algorithms such as k-means.
Semantic Text Similarity (STS).
This task mea-
sures the degree of semantic similarity between
sentence pairs, either within or across languages,
based on embedding similarity.
Retrieval.
Given a query, the task is to retrieve
relevant documents from a large corpus.
Both
queries and documents are embedded, and simi-
larity scores determine ranking.
Reranking.
Given a query and a candidate set of
documents, the goal is to rank the candidates by
relevance using embeddings. This task focuses on
fine-grained ranking quality.
Parameter
Value
Training epochs
1
Batch size (per device)
8
Group size
8
Learning rate
1e-5
Warmup ratio
0.1
Max query length
512
Max passage length
512
Padding multiple
8
Knowledge distillation
True (KL divergence)
Negatives cross-device
Enabled
Embedding normalization
True (L2)
Sentence pooling
Mean pooling
Temperature
0.02
Precision
FP16
Table 5: Key training configurations used in fine-tuning.
A.2
Baseline Model Descriptions
mmBERT-base
mmBERT-base is a massively
multilingual ModernBERT encoder trained on 3T,+
tokens covering >1,800 languages, extending the
ModernBERT architecture (fast encoder with long
context) to the multilingual regime (Warner et al.,
2025). The training recipe introduces curriculum-
style annealed language learning, inverse masking,
and temperature-based sampling to emphasize low-
resource languages while retaining strong perfor-
mance on high-resource ones (Marone et al., 2025).
Reported results show that mmBERT-base surpasses
prior multilingual encoders such as XLM-R on
standard NLU and retrieval benchmarks, approach-
ing the English-only ModernBERT on GLUE de-
spite being trained predominantly on non-English
data (Marone et al., 2025). Inference follows stan-
dard encoder usage (mean pooling over last hidden

--- Page 13 ---

states and L2 normalization).
KaLM-Embedding
KaLM-Embedding is a mul-
tilingual embedding family that prioritizes training-
data quality over sheer scale, combining (i) persona-
based synthetic examples distilled from LLMs,
(ii) ranking-consistency filtering, and (iii) semi-
homogeneous task batching for efficient contrastive
learning (Hu et al., 2025). Many public check-
points are built on compact Qwen2 backbones (e.g.,
∼0.5B) and instruction-tuned variants for down-
stream retrieval and semantic similarity. Technical
reports describe v1.5/v2 updates with improved
data curation and training strategy, yielding strong
MTEB performance for their size (Hu et al., 2025).
Qwen3-Embedding (0.6B / 4B / 8B)
Qwen3-
Embedding is a purpose-built series of dense en-
coders for text embeddings and reranking, offered
in 0.6B/4B/8B sizes with a 32k token context win-
dow and coverage of 100+ languages (Zhang et al.,
2025). The models are instruction-aware and sup-
port flexible output dimensionalities (via MRL-
style prefix truncation), with typical maximum em-
bedding sizes of 1,024 (0.6B), 2,560 (4B), and
4,096 (8B); matching reranker models are avail-
able at each size. Training leverages Qwen3 LLMs
both as backbones and as data synthesizers across
domains and languages, improving robustness for
retrieval/reranking workloads. Inference uses mean
pooling and L2 normalization; common deploy-
ment stacks expose a user-selectable output dimen-
sionality for storage/latency trade-offs.
BGE-M3
BGE-M3 (BAAI) is a versatile embed-
ding model unifying three capabilities in a single
encoder: Multi-Functionality (dense, multi-vector,
and sparse retrieval), Multi-Linguality (100+ lan-
guages), and Multi-Granularity (robust from short
queries to long documents, up to ∼8,192 tokens)
(Chen et al., 2024). The training pipeline uses self-
knowledge distillation across retrieval functions to
align representations and enables hybrid retrieval
without switching models (Chen et al., 2024). It is
widely used as a strong multilingual baseline for
retrieval, clustering, and classification.
mE5-Large, mE5-Large-Instruct
mE5-large
and mE5-large-instruct (Wang et al., 2024c) are
multilingual members of the E5 family built
on XLM-RoBERTa-large (Conneau et al., 2020),
trained with a two-stage recipe that first per-
forms weakly supervised contrastive pre-training
on roughly one billion multilingual text pairs and
then supervised fine-tuning on curated embedding
tasks; the instruction variant further formats su-
pervision with concise task instructions to special-
ize representations for retrieval and related tasks.
Both use a 24-layer encoder that produces 1,024-
dimensional vectors and inherit broad ( 100 lan-
guage) coverage from the XLM-RoBERTa back-
bone. At inference time they follow the E5 prompt
conventions (e.g., query / passage style inputs), ap-
ply mean pooling over the last hidden states, and
L2-normalize the output, yielding strong perfor-
mance on retrieval, semantic similarity, clustering,
and classification benchmarks in both monolingual
and cross-lingual settings.
gte-Qwen2-7B-instruct
gte-Qwen2-7B-
instruct
(Alibaba-NLP)
is
a
7B-parameter
instruction-tuned General Text Embedding model
built on Qwen2-7B, targeting high-quality multi-
lingual embeddings with a 32k context window (Li
et al., 2023b). At release, it reported leading scores
on MTEB English/Chinese subsets, reflecting a
training mixture that combines instruction-style
contrastive objectives and curated negatives. It is
used as a strong large-model baseline for retrieval,
reranking, and semantic similarity.
GritLM-7B
GritLM-7B (Contextual AI) unifies
generation and embeddings in one model via Gen-
erative Representational Instruction Tuning (GRIT)
(Muennighoff et al., 2024). A custom modeling
component adds bidirectional attention paths so
that the same backbone can function as a strong
encoder for embeddings without sacrificing gen-
erative performance (Muennighoff et al., 2024).
The paper reports SOTA-level MTEB results for
7B-class open models alongside strong generative
benchmarks, demonstrating that a single model can
excel at both modalities (Muennighoff et al., 2024).
Linq-Embed-Mistral
Linq-Embed-Mistral is
a Mistral-7B–based embedding model developed
with task-tailored data crafting, filtering, and hard-
negative mining to improve retrieval quality (Kim
et al., 2024). The technical report and model card
document leading MTEB retrieval scores at release
(e.g., average ∼68.2 on 56 datasets; retrieval score
∼60.2), achieved through homogeneous task or-
dering and mixed-task fine-tuning strategies (Kim
et al., 2024). It is frequently used as a competitive
7B encoder baseline for dense retrieval.
SFR-Embedding-Mistral
SFR-Embedding-
Mistral (Salesforce Research) applies transfer

--- Page 14 ---

learning on top of E5-mistral-7b-instruct and
Mistral-7B-v0.1,
with
additional
multi-task
training and optimized negative sampling aimed at
retrieval tasks (Meng et al., 2024). Public materials
position it as a top-performing 7B embedding
model for search, clustering, and classification
workloads (Meng et al., 2024).
E5 Mistral 7B Instruct
E5-Mistral-7B-instruct
initializes the E5 instruction-tuning recipe from
Mistral-7B-v0.1, producing a 7B encoder special-
ized for instruction-aware embeddings (Wang et al.,
2024b). As with other E5 variants, inference ben-
efits from task instructions plus query:/passage:
prefixes; mean pooling with L2 normalization is
used for final vectors (Wang et al., 2024b,a). It
serves both as a competitive baseline and as a
foundation for further transfer learning (e.g., SFR-
Embedding-Mistral).
Gemini
Embedding-001
gemini-embedding-
001 is Google’s multilingual text-embedding
model available via the Gemini API and Vertex AI,
trained with Matryoshka Representation Learning
(MRL) so that leading vector prefixes remain
useful at smaller dimensions (Lee et al., 2025).
The default output is 3,072 dimensions, but APIs
allow setting output dimensionality (e.g., 1,536 or
768) with minimal quality loss, enabling flexible
storage/latency trade-offs (Lee et al., 2025). The
model supports 100+ languages and has been a
strong performer on multilingual MTEB since its
early releases.
A.3
Detailed Statistics of Machine Translation
Quality
To assess the quality of the machine translation
data used in AfriMTEB, we rely on automatic eval-
uation with SSA-COMET (Li et al., 2025). SSA-
COMET is a recently released metric trained on
SSA-MTE, a large-scale human-annotated evalu-
ation dataset covering 13 African language pairs
with over 63,000 sentence-level judgments. Com-
pared to earlier African-focused metrics such as
AfriCOMET, SSA-COMET provides stronger cor-
relation with human ratings and better robustness
in low-resource settings.
From Table 6, we observe a clear trade-off be-
tween dataset size and quality. At a relaxed thresh-
old of 0.67, over 430k sentence pairs are retained,
ensuring broad coverage across all nine target lan-
guages. Increasing the threshold to 0.75 reduces
Language
0.67
0.75
0.80
Amharic (amh_Ethi)
44,166
4,617
281
Oromo (gaz_Latn)
73,846
14,598
2,818
Hausa (hau_Latn)
31,799
5,851
1,056
Igbo (ibo_Latn)
16,778
1,279
136
Kinyarwanda (kin_Latn)
81,003
4,867
337
Swahili (swh_Latn)
116,338
21,996
1,849
Xhosa (xho_Latn)
18,143
2,007
351
Yoruba (yor_Latn)
31,377
3,316
411
Zulu (zul_Latn)
20,229
1,535
224
Total
433,629
60,066
7,463
Table 6: Number of translation pairs retained after fil-
tering with SSA-COMET at three thresholds. Lower
thresholds yield more data, while stricter thresholds re-
tain fewer but higher-quality examples.
the pool to around 60k examples, striking a bal-
ance between filtering noise and preserving suffi-
cient training data. At the strictest cutoff of 0.80,
only 7.5k pairs remain, indicating that high-quality
translations are relatively scarce. Language-level
differences are also evident: Swahili, Oromo, and
Kinyarwanda consistently contribute the largest
number of pairs, while Igbo and Amharic see the
sharpest reductions under stricter filtering, reflect-
ing variation in MT quality across languages.
A.4
Detailed AfriMTEB-Lite results
Table
7
shows
the
comprehensive
results
across all evaluated datasets and languages in
AfriMTEB-Lite.

--- Page 15 ---

Dataset
amh
gaz
hau
ibo
kin
swa
xho
yor
zul
Avg.
AfriHateClassification
bge-m3
52.52
52.19
47.32
56.03
51.71
64.81
36.85
50.77
38.49
50.08
gemini embedding 001
54.31
52.31
52.4
63.47
57.75
74.07
38.94
56.3
45.3
54.98
mE5-large-instruct
50.78
51.92
42.95
57.16
54.85
67.12
40.18
51.56
47.03
51.51
AfriE5-large-instruct
52.76
53.79
44.77
58.95
56.47
64.94
37.8
51.67
43.93
51.68
AfriSentiClassification
bge-m3
48.45
34.8
68.83
54.43
46.12
44.52
–
38.21
–
47.91
gemini embedding 001
59.75
34.35
75.02
61.65
58.58
45.94
–
41.25
–
53.79
mE5-large-instruct
44.07
35.8
68.64
49.52
50.19
41.95
–
38.91
–
47.01
AfriE5-large-instruct
51.41
35.7
71.78
53.67
53.98
44.13
–
44.57
–
50.75
NewsClassification
bge-m3
84.73
74.62
78.23
64.23
49.4
73.8
77.85
79.05
–
72.74
gemini embedding 001
84.41
82.09
77.14
68.9
58.58
71.95
87.31
84.21
–
76.82
mE5-large-instruct
87.82
79.54
80.71
77.59
57.27
79.43
85.29
83.07
–
78.84
AfriE5-large-instruct
89.52
81.75
81.52
78.03
58.31
78.15
85.59
82.99
–
79.48
AfriXNLI
bge-m3
75.64
66.39
69.67
64.33
65.27
73.88
69.41
64.03
69.87
68.72
gemini embedding 001
81.32
66.8
78.57
78.05
73.79
78.34
75.42
71.72
73.38
75.27
mE5-large-instruct
66.85
62.96
63.51
65.05
62.01
68.09
66.66
61.89
63.7
64.52
AfriE5-large-instruct
72.28
68.57
67.89
70.36
64.68
72.1
72.41
65.43
67.52
69.03
EmotionAnalysisPlus
bge-m3
20.99
28.54
24.92
23.49
33.9
37.14
21.52
40.58
33.86
29.44
gemini embedding 001
28.38
30.8
36.03
30.71
39.52
39.67
27.76
45.66
40.6
35.46
mE5-large-instruct
22.27
30.41
27.03
27.59
34.27
39.89
24.17
40.88
37.05
31.51
AfriE5-large-instruct
24.07
30.74
28.37
30.18
36.21
38.8
28.13
42.2
36.35
32.78
FloresBitextMining
bge-m3
83.73
71.4
82.71
72.78
76.63
86.13
81.99
65.33
82.24
78.1
gemini embedding 001
91.3
77.8
90.01
87.9
90.13
91.43
90.37
83.99
90.28
88.13
mE5-large-instruct
92.58
88.51
91.5
91.65
92.05
93.22
92.58
87.88
92.72
91.41
AfriE5-large-instruct
92.37
88.67
91.32
91.32
91.83
92.91
92.29
87.92
92.51
91.24
InjongoIntent
bge-m3
85.84
61.19
86.5
71.86
65.66
90.36
74.62
74.11
68.05
75.35
gemini embedding 001
89.5
65.23
95.25
83.14
77.72
93.64
87.38
84.28
79.22
83.93
mE5-large-instruct
80.86
64.89
85.05
74.45
65.95
80.17
78.11
79.38
70.25
75.46
AfriE5-large-instruct
82.84
62.31
85.95
72.3
65.2
84.42
79.67
77.73
68.36
75.42
NTREXBitextMining
bge-m3
79.36
60.9
86.3
81.64
79.04
93.91
83.76
72.93
86.07
80.43
gemini embedding 001
87.2
65.69
88.16
87.03
81.02
94.49
86.33
77.45
90.35
84.19
mE5-large-instruct
92.07
73.8
94.81
94.57
92.65
97.45
93.82
89.26
95.15
91.51
AfriE5-large-instruct
92.87
78.04
94.67
94.63
91.83
97.43
93.88
89.67
95.37
92.04
SIB200-14Classes
bge-m3
16.05
6.08
13.59
6.85
9.23
16.92
9.83
4.08
9.31
10.22
gemini embedding 001
18.27
8.13
18.58
16.24
23.23
20.03
18.46
13.64
23.07
17.74
mE5-large-instruct
21.24
12.61
22.11
21.49
23.8
32.44
21.63
17.23
25.51
22.01
AfriE5-large-instruct
30.21
13.28
27.48
25.91
29.02
33.05
27.06
20.71
28.82
26.17
SIB200Classification
bge-m3
64.9
44.22
60.85
51.16
53.44
67.99
56.41
46.73
55.07
55.64
gemini embedding 001
71.72
57.15
69.65
69.84
73.69
73.4
71.01
65
71.3
69.2
mE5-large-instruct
72.87
57.09
71.27
73.7
74.68
76.63
74.1
66.05
74.14
71.17
AfriE5-large-instruct
75.47
59.82
72.57
73.69
75.16
76.46
73.8
67.1
74.04
72.01
SIB200ClusteringS2S
bge-m3
29.82
10.84
22.91
15.01
18.84
34.49
21.51
13.4
22.02
20.98
gemini embedding 001
39.18
20.92
40.94
37
37.29
38.3
34.57
27.63
35.68
34.61
mE5-large-instruct
48.96
30.47
44.47
46.11
47.42
50.32
46.65
36.03
45.04
43.94
AfriE5-large-instruct
54.35
31.61
44.87
46.56
48.65
49.95
49.53
38.31
47.52
45.71
BelebeleRetrieval
BGE-m3
79.99
58.88
75.48
61.26
65.58
87.92
69.13
60.84
69.59
69.85
Gemini Embedding
91.07
68.23
86.46
80.26
86.01
92.65
86.33
75
86.61
83.62
mE5-Large-Instruct
81.08
66.34
77.54
73.72
76.93
86.97
77.63
62.97
77.97
75.68
AfriE5-Large-Instruct
83.34
69.42
78.71
75.71
78.34
87.99
80.16
65.25
80.26
77.69
Table 7: Task-wise and per-language Performance. Comparison of the selected models across all African
languages for each task.

```
