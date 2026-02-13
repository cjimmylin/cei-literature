---
title: "2025-Abdul-Mageed-Where Are We Evaluating LLM Performance - PDF Extract"
source_pdf: "2025-Abdul-Mageed-Where Are We Evaluating LLM Performance.pdf"
pages: 28
extracted_at: "2026-02-13T09:15:42.746431"
---

# PDF Extract: 2025-Abdul-Mageed-Where Are We Evaluating LLM Performance

**Source PDF:** 2025-Abdul-Mageed-Where Are We Evaluating LLM Performance.pdf
**Total Pages:** 28

---

## Content

```
--- Page 1 ---

arXiv:2502.19582v2  [cs.CL]  3 Jun 2025
Where Are We?
Evaluating LLM Performance on African Languages
Ife Adebaraξ
Hawau Olamide ToyinΩNahom Tesfu GhebremichaelΩ
AbdelRahim Elmadanyξ
Muhammad Abdul-Mageedξ,Ω,λ
ξThe University of British Columbia
ΩMBZUAI
λ Invertible AI
{ife.adebara,a.elmadany,muhammad.mageed}@ubc.ca
(a) Language policies for education across Africa.
(b) Official national language policies across Africa.
(c) Official regional language policies across Africa. None means no
additional policy is available on a regional level.
(d) We collect SAHARA to empirically evaluate LLM
performance on African languages, allowing us to
demonstrate with evidence how current language poli-
cies directly impact progress in the field.
Figure 1: Maps of Africa showing the languages covered in this work and the language policies across the continent.
The term Indigenous language is broadly defined here as one that is ‘native’ to the area (Walsh, 2005). The term
Both in maps (a), (b), and (c) refers to Indigenous and foreign languages combined. Knowledge of what is an
Indigenous language is based exclusively on Ethnologue (https://www.ethnologue.com).
Abstract
Africa’s rich linguistic heritage remains under-
represented in NLP, largely due to historical
policies that favor foreign languages and create
significant data inequities. In this paper, we
integrate theoretical insights on Africa’s lan-
guage landscape with an empirical evaluation
using SAHARA— a comprehensive benchmark
we curate from large-scale, publicly accessi-
ble datasets capturing the continent’s linguis-
tic diversity. By systematically assessing the
performance of leading large language mod-

--- Page 2 ---

els (LLMs) on SAHARA, we demonstrate how
policy-induced data variations directly impact
model effectiveness across African languages.1
Our findings reveal that while models perform
reasonably well on few languages, many In-
digenous languages remain marginalized due
to sparse data. Leveraging these insights, we
offer actionable recommendations for policy re-
forms and inclusive data practices. Overall, our
work underscores the urgent need for a dual ap-
proach—combining theoretical understanding
with empirical evaluation—to foster linguistic
diversity in AI for African communities.
1
Introduction
The digital landscape of Africa is as diverse as its
cultures and languages, yet the continent’s rich lin-
guistic heritage remains largely underrepresented
in NLP research. Despite significant transforma-
tions over the past decade driven by advances
in large language models (LLMs) and a growing
interest in linguistic diversity, most efforts have
concentrated on a handful of widely spoken lan-
guages such as Swahili, Afrikaans, and Hausa,
while many Indigenous languages continue to be
sidelined due to the paucity of accessible, high-
quality datasets. This oversight, deeply rooted in
historical language policies that have neglected
robust data collection and accessibility, has far-
reaching implications for the development of lan-
guage technology across Africa (Eberhard et al.,
2021). Recent initiatives, including the work of
Masakhane (Dione et al., 2023b; Adelani et al.,
2021c, 2023, 2024b; Bandarkar et al., 2024a) and
the efforts of platforms like HuggingFace, have
begun to address these challenges by curating
language-specific datasets and adapting transfer
learning techniques for low-resource African lan-
guages. Models such as Cheetah (Adebara et al.,
2024a), Serengeti (Adebara et al., 2023), Toucan
(Elmadany et al., 2024), Afri-XLMR (Alabi et al.,
2022), AfriTeVa (Oladipo et al., 2023; Jude Ogun-
depo et al., 2022), mBERT (Devlin et al., 2018),
XLM-R (Conneau et al., 2020), and LLaMA (Tou-
vron et al., 2023) have leveraged multilingual data
to enhance performance on these languages, yet
progress remains uneven—highlighting that the ad-
vancements achieved are primarily concentrated on
a select few.
In this study, we undertake a comprehensive em-
pirical evaluation of leading LLMs on an extensive
1SAHARA is publicly available at https://github.com/UBC-
NLP/sahara.
benchmark that we collect using mostly existing
datasets to unravel how current African language
policies, by dictating data availability and accessi-
bility, directly shape model performance across
the continent’s diverse linguistic spectrum. By
systematically analyzing the distribution of exist-
ing datasets across languages and performance pat-
terns among various LLMs, we not only pinpoint
which languages benefit from ample data resources
but also illuminate the underlying factors that con-
tribute to their relative success. Our investigation
reveals that the disparities in NLP outcomes are
closely tied to policy-driven data inequities, offer-
ing concrete evidence of the need for more inclu-
sive, forward-thinking language policies. These
insights provide actionable recommendations for
enhancing dataset creation and model training, ul-
timately aiming to bridge the digital divide and
foster linguistic diversity in artificial intelligence
for African communities.
Overall, we make the following contributions:
(1) Benchmark with wide, diverse coverage. We
introduce Sahara, a comprehensive benchmark as-
sembled from large-scale, publicly accessible, and
inclusive datasets that capture the rich linguistic
diversity of Africa. This benchmark enables a sys-
tematic evaluation of data availability and model
performance across a broad range of African lan-
guages. (2) Dynamic leaderboard. We develop a
dynamic leaderboard built on best design practices,
providing a transparent and continually updated
platform to track progress and benchmark innova-
tions in African NLP. (3) Empirical evaluation.
We perform an extensive empirical assessment of
a wide spectrum of models thereby establishing
robust baselines and revealing performance dispar-
ities linked to data resource availability. (4) Policy-
driven and actionable insights. We uncover clear
links between current language policies, data avail-
ability, and model performance, demonstrating how
policy-induced data inequities shape the effective-
ness of language models across Africa. Our analy-
sis provides recommendations for future research
and development by informing policy reforms that
foster more inclusive language technologies tai-
lored to the needs of African communities. We
now discuss language polices in Africa.
2
Language Policies in Africa
Across Africa, the predominant response to the
continent’s multilingual landscape has been the

--- Page 3 ---

adoption of a foreign language for official func-
tions. However, in some instances, select Indige-
nous African languages receive official recognition
at regional or national levels or within educational
contexts (Petzell, 2012; Foster, 2021; Ouane and
Glanz, 2010). 2 For instance in Nigeria, English is
the official language, with only three out of 512 In-
digenous languages recognized at the regional level.
Similarly, Ghana designates English as its official
language while also recognizing ten of its 73 In-
digenous languages for institutional use. In Tanza-
nia, Swahili is the sole Indigenous official language
among 118 languages, alongside English. Kenya
grants official status to 12 of its 61 languages, while
South Africa recognizes 12 out of 20 Indigenous
languages as institutional languages (Adebara and
Abdul-Mageed, 2022). Figures 1(a), 1(b), 1(c),
and 1(d) illustrate the distribution of language poli-
cies across the continent.
Even when Indigenous languages are granted of-
ficial status alongside foreign languages, they often
serve a symbolic rather than functional role. For
instance, although Kiswahili is recognized as an
official language by the African Union, its website
and official document releases remain in English
and French. A similar pattern emerges in educa-
tion systems: where Indigenous languages are used,
their role is typically confined to early childhood
education and is usually paired with a foreign lan-
guage rather than serving as the sole medium of
instruction (Petzell, 2012; Foster, 2021; Ouane and
Glanz, 2010). These language policies significantly
shape language use across various domains, includ-
ing newspapers, radio, television, and social media.
Due to the dominance of foreign languages in of-
ficial contexts, major newspapers and government
publications are predominantly produced in lan-
guages such as English, French, and Portuguese,
thereby limiting access for speakers of Indigenous
languages (ResCue and Agbozo, 2021). Although
some Indigenous languages are used on television
and radio, foreign languages tend to dominate na-
tional broadcasts, especially in political discourse
2An Indigenous language is defined here as one that is
native to a particular region, rather than introduced from else-
where, in contrast to a foreign language, which may nonethe-
less serve as the mother tongue for certain local populations
(Walsh, 2005). A national language refers to a language spo-
ken broadly across an entire country. A regional language is
spoken by a significant number of people within a specific area
but does not have widespread national usage. An educational
language is officially designated as a medium of instruction
within the educational system.
and formal news reporting (Cheo et al., 2023; My-
ers and Harford, 2020; National Communications
Authority, 2016).
Social media presents a more flexible environ-
ment where users can communicate in Indigenous
languages; however, platform support remains un-
even (Sunday et al., 2018; Molale and Mpofu,
2023; ResCue and Agbozo, 2021). Many African
languages are underrepresented in digital spaces,
lacking features such as text input options, spell
checkers, or automated translation services. Con-
sequently, users often resort to code-switching be-
tween Indigenous and dominant foreign languages,
reinforcing existing linguistic divides. These trends
underscore how official language policies shape
broader language use, ultimately contributing to the
marginalization of Indigenous languages in both
public and digital communication spheres.
The analysis of language policies in Africa re-
veals how historical choices have led to signif-
icant data imbalances for Indigenous languages.
Motivated by this, we built our benchmark, SA-
HARA to evaluate how these policies directly im-
pact data availability, coverage, and the perfor-
mance of LLMs on African languages. In the fol-
lowing section, we detail the construction of SA-
HARA and demonstrate its role in linking language
policy to empirical outcomes in NLP.
3
Related Work
The development of NLP for African languages
is hindered by data scarcity, policy-induced dis-
parities, and suboptimal model performance. Re-
cent initiatives have sought to mitigate these chal-
lenges by curating diverse datasets, rigorously eval-
uating multilingual models, and advocating for
more inclusive language policies. For example,
several initiatives have contributed to expanding
datasets for African (Yimam et al., 2020; Muham-
mad et al., 2022; Aliyu et al., 2022; Muhammad
et al., 2023b,a; Ilevbare et al., 2024; Elmadany
et al., 2024).
Some notable ones like Adelani
et al. (2021c, 2022b) introduced MasakhaNER, a
named entity recognition dataset for 10 African
languages, highlighting the limitations in existing
resources. Similarly, IROKOBench (Adelani et al.,
2024b) evaluated LLMs on African languages, re-
vealing stark performance gaps between high- and
low-resource languages. Adebara et al. (2022) de-
veloped AfroLID, a neural language identification
model covering 517 African languages, showing

--- Page 4 ---

that most languages lack NLP datasets beyond lan-
guage identification.
Language policies play a crucial role in deter-
mining resource availability. Adebara and Abdul-
Mageed (2022); Hershcovich et al. (2022) empha-
sized the sociolinguistic factors affecting NLP de-
velopment, noting that languages with official sta-
tus receive more institutional support, fostering
greater digital representation. Bird (2020) further
critiqued the Western-centric approach in speech
and language technologies, calling for AI mod-
els that align with Indigenous linguistic contexts.
Model performance in African languages remains
uneven, largely due to the dominance of high-
resource languages in multilingual training. Con-
neau et al. (2018) introduced XLM-R, demonstrat-
ing the limitations of cross-lingual transfer learn-
ing for underrepresented languages. Meta AI’s
No Language Left Behind (NLLB) project (Costa-
jussà et al., 2022) attempted to improve multilin-
gual models for low-resource languages, but perfor-
mance remained inconsistent, particularly in gener-
ation tasks. Despite these advances, African NLP
still requires increased investment in dataset cura-
tion, inclusive policy frameworks, and model de-
velopment tailored to the linguistic diversity of the
continent. We now introduce SAHARA.
4
Sahara Benchmark
Our objective is to create a comprehensive bench-
mark for African NLP that enables (i) analysis of
existing language resources and (ii) the assessment
of language models and tracking of the progress
of African NLP. To achieve this goal, we develop
SAHARA, adhering to several key design princi-
ples that we will now elucidate. SAHARA estab-
lishes a comprehensive and adaptable benchmark
for African NLP using publicly available datasets.
Figure shows coverage of SAHARA.
Wide and Diverse Coverage.
SAHARA is the
most comprehensive benchmark for African NLP,
covering a vast range of languages. We achieve
this by collecting high-quality, publicly available
datasets from as many African languages as pos-
sible, ensuring easy accessibility for researchers
evaluating their models. As a result, SAHARA sup-
ports 517 languages across various tasks, making
it the most extensive and representative benchmark
for African NLP. It encompasses languages from
50 out of 54 African countries and includes data
written in five different scripts: Arabic, Coptic,
Ethiopic, Latin, and Vai, spanning five language
families across the continent.
Tasks and Task Clusters.
SAHARA is designed
to support a broad spectrum of NLP tasks, which
we systematically organize into coherent task clus-
ters. The inclusion of well-defined, challenging
clusters enables a more meaningful assessment of a
model’s capabilities and allows researchers to eval-
uate performance on specific clusters. As shown in
Table 1, SAHARA comprises four clusters: text clas-
sification, text generation, multiple-choice, compre-
hensive and reasoning (MCCR), and token-level
classification. For further details on the datasets
used for each task, please refer to Appendix A.
Modular Public Leaderboard.
We implement
a user-friendly leaderboard for model evaluation
on SAHARA, hosted on Hugging Face (HF) Spaces.
Evaluated models must be publicly available in HF
repositories to ensure seamless integration. When
submitting a model, users are required to provide
detailed metadata—including whether the model
is pretrained, further pretrained, or instructed—and
then submit an evaluation request. The submission
enters a processing queue, and once evaluation is
complete, the results are automatically displayed
on the leaderboard. Our team will actively main-
tain the leaderboard by continuously integrating
new publicly available tasks and datasets to keep it
up-to-date. SAHARA thus serves as a valuable tool
for assessing model performance in African NLP,
accelerating the development of high-performance
models, and contributing to the field’s growth. In
addition to evaluating models on the entire bench-
mark, users have the flexibility to assess perfor-
mance on specific task clusters, encouraging the
development of specialized models tailored to ad-
dress the unique challenges of African NLP.
5
Experiments and Results
5.1
Experimental Setup
To comprehensively assess the progress of African
NLP, we systematically evaluate a range of widely
used instruction-based LLMs in a few-shot set-
ting on the SAHARA benchmark.
We include
both open and closed LLMs, such as Phi-3.5 and
Phi-4 (Abdin et al., 2024), Gemma family (Team
et al., 2024) models including Gemma-2 (2, 9, 27B)
and Gemma-3 (4, 12, 27B), Llama family mod-
els (Dubey et al., 2024) including Llama-3.1 (8,

--- Page 5 ---

Cluster
Task
Identifier
#AL
#DS
Classification
Cross-Lingual Natural Language Inference (Adelani et al., 2024b)
xnli
16
1
Language Identification (Adebara et al., 2022)
langid
517
1
News Classification (Azime and Mohammed, 2021; Niyongabo et al., 2020; David, 2020a)
news
4
3
Sentiment Analysis (Diallo et al., 2021; Oyewusi et al., 2020; Shode et al., 2022a)
sentiment
3
3
Topic Classification (Hedderich et al., 2020)
topic
2
1
Generation
Machine Translation (Adelani et al., 2022a; Reid et al., 2021a; Ogueji and Ahia, 2019; Akera et al., 2022)
mt
29
5
Paraphrase (Scherrer, 2020)
paraphrase
4
1
Summarization (Hasan et al., 2021; Adebara et al., 2024b)
summary
10
2
Title Generation (Hasan et al., 2021; Adebara et al., 2024b)
title-gen
10
2
MCCR
General Knowledge (Adelani et al., 2024b)
mmlu
16
1
Mathematical Word Problems (Adelani et al., 2024b)
mgsm
16
1
Reading Comprehension (Bandarkar et al., 2024a)
reading-comp
25
1
Context-based Question Answering (Clark et al., 2020)
squad-qa
1
1
Tokens
NER (Adelani et al., 2021a, 2022c; Eiselen, 2016; Alabi et al., 2020a; Pan et al., 2017)
ner
27
5
Phrase Chunking (Eiselen, 2016)
chunking
8
1
POS Tagging (Onyenwe et al., 2018a, 2019)
pos
1
1
Total
16
517
30
Table 1: Descriptive statistics of languages and dataset diversity in SAHARA across different tasks and task-clusters.
#AL: African Languages, #DS: datasets, MCCR: multiple-choice, comprehensive and reasoning task-cluster.
70B), Llama-3.2 (1, 3B), and Llama-3.3 (70B),
Aya models (8, 23B) (Aryabumi et al., 2024), and
Command family models (Cohere et al., 2025) in-
cluding Command-R-Plus-R7B, Command-R-Plus
(104B) and Command-A (111B), as well as pro-
prietary models such as GPT-4.13 (Achiam et al.,
2023) and Claude-4-Sonnet4 (Anthropic, 2024).
We further analyze performance by categorizing
models according to size: small language models
(SLM, <8B parameters) and large language models
(LLM, ≥8B parameters), allowing investigation of
the relationship between scale and effectiveness.
For robust comparison, we aggregate evaluation
datasets according to task clusters described in Ap-
pendix A. From each task, we randomly sample
1, 000 data points for few-shot testing, employing
well-curated, concise prompts—examples of which
appear in Appendix C1.
5.2
Results and Discussion
We evaluate 24 LMs across four task clusters, main-
taining a consistent assessment approach while
varying evaluation metrics.
Depending on the
task, we employ Exact Match, F1, Accuracy,
spBLEU1K (Elmadany et al., 2024), and RougeL
scores.
As shown in Table 2, in the classification
tasks, the closed models Claude-4-Sonnet and
GPT-4.1 consistently lead in performance, fol-
lowed by larger LLMs such as Gemma3 (27B) and
CommandR-Plus-104B. In the language identifica-
tion task, most models struggle to grasp the task
effectively, with only the larger LLMs demonstrat-
3GPT-41.1 version: gpt-4.1-2025-04-14.
4Claude-4-Sonnet version: claude-4-sonnet-20250514
ing some understanding, suggesting that model size
is crucial for achieving higher accuracy across vari-
ous multilingual tasks. In the generation task clus-
ter, larger models perform as expected, with GPT-
4.1 and Llama-3.1 (70B) achieving the best results.
There is a noticeable performance increase across
all models in the paraphrase task, while the summa-
rization task exhibits a more balanced performance
among all models. Considering their size, Phi-3.5
and Gemma3 (4B) perform well within this task
cluster. In the MCCR tasks, Command-A (111B)
performs competitively against the closed Claude-
4-Sonnet model. In the MGSM task, which in-
volves solving mathematical word problems, most
open-source models perform poorly, while Claude-
4-Sonnet excels, achieving an exact match score
of 22.34%.
In token-level tasks, GPT-4.1 and
Command-A (111B) consistently deliver strong
performances, whereas the Aya model family strug-
gle to grasp the tasks.
Results demonstrate a nuanced landscape of per-
formance across multilingual and African LLMs,
with notable variations depending on parameter
size and task type.
In few-shot settings, the
closed model Claude-4-Sonnet achieves the high-
est overall average score (40.82), outperforming
all open models across most task clusters. Among
open models, Command-A (111B) and Gemma-
3 (27B) also exhibit strong performance, particu-
larly in downstream tasks such as reasoning tasks,
where Gemma2 (27B) reaches top score of 82.49
on Squad-QA and Command-A achieves 61.91
on MMLU task. For smaller parameter regimes,
Gemma-2 (2B) and Phi-4 (3.8B) demonstrate the
best performance on their model size. Furthermore,

--- Page 6 ---

SLM
LLM
Closed LLM
Cluster
Identifier
Metric
Shots
S1
S2
S3
S4
S5
S6
L1
L2
L3
L4
L5
L6
L7
L8
L9
L10
L11
L12
L13
L14
L15
L16
CL1
CL2
Classification
xlni
Acc.
5
33.6
33.7
36.7
41.18
40.4
46.68
48.08
55.06
34.3
40.69
37.09
61.09
57.86
65.58
44.2
38.19
51.89
48.38
52.09
35.87
46.77
59.67
69
69.6
lid
F1
10
0
0
0.87
0.26
0.85
0.77
2.82
3.6
0
1.49
2.27
1.95
4.61
4
1.81
3.34
3.26
3.07
3.3
3.05
3.32
4.57
3.73
4.48
news
F1
3
0.86
0.35
0.15
17.54
0
6.64
21.94
0
2.06
24.06
0.12
25.83
7.83
35.56
28.03
0.61
35.26
33.31
34.81
3.45
30.46
28.66
40.09
32.19
sentiment
F1
5
38.51
24.75
30.45
11.05
28.77
1.99
36.09
42.47
38.4
28.36
36.07
34.56
20.55
46.35
35.86
25.94
24.51
45.82
35.89
19.98
37.07
47.14
55.67
57.52
topic
F1
3
8.73
31.62
20.3
19.79
12.46
17.15
48.11
39.35
34.95
28.55
42.12
44.3
31.8
70.73
36.47
43.74
64.89
56.48
48.73
52.09
50.96
53.16
67.93
76.57
Avg.
16.34
18.08
17.69
17.96
16.50
14.65
31.41
28.10
21.94
24.63
23.53
33.55
24.53
44.44
29.27
22.36
35.96
37.41
34.96
22.89
33.72
38.64
47.28
48.07
Generation
mt_eng2xx
spBleu1K
5
1.79
3.63
3.45
3.25
2.12
3.4
7.07
7.61
1.72
4.37
2.79
6.24
6.91
4.56
3.73
3.29
8.84
8.7
9.36
1.4
6.06
8.22
12.18
12.36
mt_fra2xx
spBleu1K
5
0.79
0.36
0.74
1.05
1.25
1.32
0.73
0.95
0.7
1.19
0.66
2.03
1.67
2.05
1.15
0.82
1.93
1.87
1.77
1.05
1.04
2.3
3.41
3.42
mt_xx2xx
spBleu1K
5
0.4
0.45
0.42
0.42
0.36
0.18
0.43
0.63
0.72
0.55
0.46
0.71
0.9
1.39
0.55
0.17
1.28
1.05
1.37
0.67
0.38
0.85
5.15
4.44
paraphrase
spBleu1K
5
23.2
28.88
31.15
19.12
25.93
17.85
28.73
25.83
31.68
31.33
23.66
17.26
21.34
15.37
32.13
30.68
26.86
19.64
27.79
19.23
36.06
26.06
23.2
20.35
summary
rougeL
2
10.03
3.24
4.37
10.07
0.91
13.34
15.1
10.43
1.45
12.74
5.92
16.16
15.73
17.13
13.27
4.19
16.92
17.19
16.4
15.46
14.88
16.09
5.99
16.3
title
spBleu1K
2
2.14
2.81
0.25
2.3
0.03
5.78
7.48
5.78
3
5.94
1.58
7.75
7.51
8.65
6.83
3.2
11.07
10.34
8.78
7.32
6.69
8.65
13.62
9.48
Avg.
6.39
6.56
6.73
6.04
5.10
6.98
9.92
8.54
6.55
9.35
5.85
8.36
9.01
8.19
9.61
7.06
11.15
9.80
10.91
7.52
10.85
10.36
10.59
11.06
MCCR
mmlu
Acc.
5
24.09
28.5
28.68
27.29
28.9
30.99
31.88
40.9
26.4
44.51
22.1
42.09
44.9
60.71
51.5
24
56.51
59.3
50.42
59.81
29.8
61.91
81.6
58.6
mgsm
ExactM
5
2.6
3.21
0
1.2
3.39
0.7
2.9
2.8
3.3
2.7
1.5
2.3
5.3
0.6
4.4
3
10.1
7.51
7.6
4.5
4.39
11.1
45.9
29.5
belebele
Acc.
5
27.71
14.71
25.2
29.31
31.31
24.69
22.7
26.93
25.09
28.24
26.33
25.63
31.04
32.34
33.64
26.61
30.4
35.92
33.72
30.83
20.99
29.12
36.6
39.7
squad_qa
F1
5
57.45
70.89
67.32
43.13
71.31
74.97
78.04
80.91
52.66
59.48
63.41
73.78
82.49
79.16
69.25
64.64
77.65
76.35
66.25
53.92
74.64
80.05
78.02
76.11
Avg.
27.96
29.33
30.30
25.23
33.73
32.84
33.88
37.89
26.86
33.73
28.34
35.95
40.93
43.20
39.70
29.56
43.67
44.77
39.50
37.27
32.46
45.55
60.53
50.98
Tokens
ner
F1
5
0
0.78
1.76
2.99
0.13
3.65
2.26
7.49
2.35
3.96
0.2
6.03
13.14
11.4
8.51
1.52
6.86
10.54
8.64
6.04
4.3
16.88
35.06
27.04
phrase
F1
5
14.79
28.5
29.44
11.52
24.91
27.73
15.95
29.35
29.42
16.55
30.87
13.59
30.01
23.97
26.34
23.09
25.55
23.13
16.78
25.13
29.44
31.05
36.69
36.45
pos
F1
5
8.83
6.73
10.56
8.04
10.3
10.46
9.13
13.2
9.81
11.68
12.52
13.86
19
13.99
18.36
11.4
14.13
15.04
11.52
20.76
13.71
27.54
62.84
38.67
Avg.
7.87
12.00
13.92
7.52
11.78
13.95
9.11
16.68
13.86
10.73
14.53
11.16
20.72
16.45
17.74
12.00
15.51
16.24
12.31
17.31
15.82
25.16
44.86
34.05
Overall
14.64
16.49
17.16
14.19
16.78
17.10
21.08
22.80
17.30
19.61
18.06
22.25
23.80
28.07
24.08
17.75
26.57
27.05
24.42
21.25
23.21
29.93
40.82
36.04
Table 2: Few-shot evaluation across different task clusters/tasks. The highest score for each individual task is
in bold green , while the best average score across each task cluster (and overall score, calculated as average
of task cluster averages) is in bold orange . Underline: refers to the best score across the open source/weights
LLMs. Shots: number of shots. SLMs: S1 Llama3.2 (1B), S2 Llama3.2 (3B), S3 Gemma2 (2B), S4 Phi-3.5
(3.8B), S5 Phi-4 (3.8B), and S6 Gemma3 (4B). LLMs: L1 Llama3.1 (8B), L2 Gemma2 (9B), L3 Aya
(8B), L4 Babel (9B), L5 Command-R-Plus-R7B (8B), L6 Gemma3 (12B), L7 Gemma2 (27B), L8 Gemma3
(27B), L9 DeepSeek-R1-Distill-Qwen (32B), L10 Aya (35B), L11 Llama3.1 (70B), L12 Llama3.3 (70B),
L13 DeepSeek-R1-Distill-Qwen (70B), L14 Babel (83B), L15 Command-R-Plus (104B), L16 Command-A
(111B). CLosed LLMs: CL1 Claude-4-Sonnet, CL2 GPT-4.1. Table E4 is a full-page version of this table.
Gemma2 (9B, 12B) show consistent mid-to-high
performance across various clusters, but do not sur-
pass the larger models in aggregate. Importantly,
translating into English is consistently easier for
the models than translating from French, likely re-
flecting disparities in training data distribution and
language representation on the target side. These
findings highlight not only the dominance of closed
LLMs and very large open models in multilingual
tasks, but also the critical influence of resource
availability and model scale on task-specific out-
comes.
Which LM should I use for reasoning tasks?
In a limited resource setting, for mathematical QA
tasks that fall in the MCCR cluster, Phi-4 ranks top
among SLMs for 16 African Languages. In the
LLMs category, Command-A (111B) has better
performance on a higher number of African lan-
guages. For reading comprehension tasks (bele-
bele), Phi-4 is most suitable in constrained com-
pute resource settings while in scenarios without
limits in compute resources, Llama 3.3-70B gives
better performance.
Which African language(s) do LMs perform
best on?
The models achieve their highest per-
formance on a small set of well-resourced African
languages—chiefly Hausa, Swahili, Yorùbá, and
Afrikaans—across diverse NLP tasks. Both open-
source models like Command-A (111B) and Aya-
35B and proprietary models such as Claude-4-
Sonnet consistently excel on these languages, re-
flecting their ample labeled and parallel data. This
trend spans simple classification and NER tasks
to complex reasoning benchmarks (e.g., MMLU,
XLNI) and machine translation, underscoring that
data availability, rather than linguistic typology, is
the primary driver of model effectiveness.
Models explicitly designed with African linguis-
tic diversity, such as Aya-35B, also achieve strong
results on Southern Sotho and Lingala—languages
that have benefited from recent, community-led
data initiatives. Swahili, in particular, ranks among
the top languages for Llama3 models, likely due
to its standardized orthography, regular morphol-
ogy, and extensive bilingual corpora. Afrikaans and
Swahili similarly perform well within Gemma2 and
Command-R-Plus (104B), supported by their inclu-
sion in massive multilingual datasets (e.g., mC4,
OSCAR, WMT) and, in Afrikaans’s case, estab-
lished government-supported digital media.
Overall, our findings reveal that LM perfor-
mance correlates strongly with the volume and di-
versity of available data. Underperformance on

--- Page 7 ---

low-resource African languages is not a function
of inherent complexity but of underrepresentation
in training data. Bridging this gap will require
concerted efforts to collect, annotate, and standard-
ize datasets that capture the dialectal, sociolinguis-
tic, and orthographic richness of all African lan-
guages—an essential step toward improved model
equity and real-world utility across the continent’s
full linguistic spectrum.
6
Data-Performance-Policy Analysis
To understand the relationship between policy, data
availability, and performance, we carry out a num-
ber of analyses inspired by SAHARA
data and
empirical results on it.
Data Availability and Diversity.
As shown in
Figure E3, among the 517 languages in our bench-
mark, only 45 have more than one dataset, while
the majority are represented solely by language
identification data. Amharic leads with 11 unique
datasets across all clusters, followed by Yorùbá
with ten and Hausa with nine. A total of six lan-
guages have only one dataset beyond language iden-
tification, while the remaining 36 have between two
and eight datasets each. It is important to note that
the disparity in dataset availability is closely linked
to language policy. The 45 languages with multiple
datasets generally hold official status or are spoken
by a significant majority in their respective coun-
tries. Government policies that designate certain
languages as official often yield greater institutional
support, driving increased documentation, educa-
tion, and media presence. For example, Amharic’s
official status in Ethiopia contributes to its rela-
tively rich dataset availability, while Yorùbá and
Hausa, both widely used in Nigeria for regional
governance and media, similarly benefit from en-
hanced linguistic resources. Conversely, languages
lacking official recognition or widespread institu-
tional support receive minimal investment in digital
and linguistic infrastructure. The dominance of a
few languages within policy frameworks perpet-
uates data scarcity for many Indigenous African
languages, thereby limiting their inclusion in NLP
advancements and reinforcing digital inequalities.
It is noteworthy that availability of NLP data
is not necessarily determined by the number of
speakers and that other variables including lan-
guage prestige, literacy rates, and economic in-
centives can be involved. This becomes evident
when comparing speaker populations with actual
data availability.
For example, Hausa (73 mil-
lion speakers), Swahili (80 million), and Zulu (28
million) are categorized as hopefuls—languages
with some available labeled datasets. In contrast,
Naija (Nigerian Pidgin)—despite having approxi-
mately 153 million speakers—is classified as a left-
behind language (Joshi et al., 2020), largely due to
decades of stigmatization and negative public atti-
tudes (Oyebola and Ugwuanyi, 2023), which have
significantly contributed to the scarcity of acces-
sible and annotated linguistic resources. Notably,
several non-African languages with significantly
smaller speaker populations—such as Catalan (5
million), Finnish (10 million), and Swedish (10.5
million)—are regarded as high-resource, primarily
as a result of sustained efforts in documentation,
digitization, and technological integration. This
discrepancy underscores a broader systemic issue
in language representation: it is not just linguistic
demographics that shape digital inclusion, but also
factors such as historical language prestige, policy
decisions, digital infrastructure, and the extent of
prior documentation.
These intersecting factors ultimately determine
whether a language is integrated into AI systems or
remains marginalized. Addressing this imbalance
requires a shift in policy and practice to prioritize
equitable digital representation. This includes tar-
geted investments in multilingual data collection,
increased funding for research on historically ex-
cluded and low-resource languages, and the inten-
tional integration of these languages into education
systems, media platforms, and digital technologies.
Such efforts must also consider the sociopolitical
and infrastructural barriers that shape language in-
clusion in AI, ensuring that underrepresented lan-
guages are not only documented but actively sup-
ported within the broader digital ecosystem.
Data Quality.
Most of the downstream task
datasets are limited to simple tasks that require
merely an atomic class label at the word, sen-
tence, or document level (e.g., sentiment analy-
sis, named entity recognition, topic classification).
Furthermore, many of these datasets are transla-
tions of existing resources or content from high-
resource languages like English and French, and
they do not always reflect authentic language usage
within the respective communities. For instance,
AfriXLNI, AfriMMLU, and AfriMGSM (Adelani
et al., 2024b) were created by translating XLNI,
MMLU, and MGSM into African languages. In

--- Page 8 ---

these datasets, the frequent use of borrowed words
and phonologized variants of foreign terms (Ade-
bara and Abdul-Mageed, 2022) highlights the chal-
lenges posed by cross-lingual concept gaps. When
translations are applied to classification tasks, mis-
alignments in the attached labels can occur because
labels are not always equivalent across languages.
Some labels may not exist in the target language
or may have restricted usage. For example, while
English possesses a productive set of adjectives,
languages like Yorùbá have a more limited adjec-
tive inventory that is context-dependent, meaning
that an English adjective may be translated as a
noun or verb in Yorùbá rather than as an adjective.
Model Performance
Here, we analyze perfor-
mance of our best model, Claude-4-Sonnet. As
shown in Figure 2, the model faces varying degrees
of difficulty when handling African languages. Fig-
ure 2(a) demonstrates that for generation tasks,
even the strongest models struggle to produce high-
quality text in African languages, with most scores
falling below 15 BLEU/ROUGE. In contrast, Fig-
ure 2(b) shows that while many languages achieve
relatively strong classification performance (over
80% accuracy), a substantial portion still falls into
the 60%–80% range, underscoring a clear perfor-
mance gap. Finally, Figures 2(c) and 2(d) reveal
that translation into English is notably easier than
translation out of English or French into African
languages, where BLEU scores drop from an av-
erage of around 19 down to nine or 11, respec-
tively. This finding suggests that even the best
model struggles more with producing fluent, faith-
ful output in African languages than with under-
standing them—underscoring the urgent need for
better data and model development tailored to these
languages.
Apart from our empirical analyses, the limited
availability and diversity of datasets for African
languages in NLP benchmarks has significant im-
plications for developing robust language technolo-
gies. Limited Model Performance and General-
ization – Models trained on a single dataset per
language risk overfitting to specific domains or
styles, reducing their ability to generalize across
different contexts, which is especially problematic
for African languages with high dialectal variation.
Bias Toward Well-Resourced Languages – Lan-
guages with more datasets naturally perform better
in multilingual models, reinforcing disparities and
leading to poor performance for underrepresented
African languages. Restricted Downstream Appli-
cations – Many NLP applications, such as machine
translation and question answering, require diverse
datasets; if a language is represented only by lan-
guage identification data, it cannot support the de-
velopment of more complex language technolo-
gies. Challenges in Transfer Learning – Transfer
learning techniques, like multilingual fine-tuning,
rely on cross-lingual similarities and sufficient data;
when African languages suffer from sparse training
data, they are unable to effectively leverage knowl-
edge transfer from resource-rich languages. We
also analyze the performance of Command-A in
Figure E2.
7
Recommendations
Policy determines how languages are used across
various domains, influencing their visibility and
viability in digital spaces. Currently, the limited
online presence of many Indigenous African lan-
guages restricts the availability of training data,
which is crucial for building effective NLP models.
We provide the following recommendations:
Policy matters. Governments and policymakers
should enact national language policies that man-
date the inclusion of Indigenous and underrepre-
sented languages across digital infrastructure, ed-
ucation, and media. Countries with multilingual
populations should adopt policies that support the
systematic documentation, transcription, and digi-
tization of African languages to enhance their pres-
ence in AI applications. Such efforts will enrich the
diversity of available data, paving the way for the
development of more robust and inclusive models.
Expand data collection and annotation. Given
that only 45 of the 517 languages in the benchmark
have more than one dataset based on our collec-
tion, it is essential to increase the availability of
high-quality data for underrepresented African lan-
guages across a broad range of downstream tasks.
Moreover, prioritizing community-driven data an-
notation efforts will be crucial in ensuring both
linguistic diversity and accuracy, especially for lan-
guages that lack institutional support.
Develop contextually relevant and culturally
accurate datasets. Many existing African lan-
guage datasets are derived from translations of
high-resource languages, which can introduce mis-
alignments and fail to capture authentic linguis-
tic expressions. To improve NLP performance,
datasets should be created using native speakers

--- Page 9 ---

(a) Generation tasks.
(b) Classification tasks.
(c) MCCR tasks.
(d) MT tasks grouped.
Figure 2: Distribution of best model performance (Claude-4-Sonnet) on different task clusters across African
languages in downstream data.
and sourced from real-world interactions, litera-
ture, and media in African languages. This will
help preserve linguistic authenticity and avoid the
overreliance on loanwords or structures that do not
naturally occur in the language. Specialized cor-
pora should also be developed to capture dialectal
variations and culturally specific language use.
8
Conclusion
In this work, we set out to unravel how current
African language policies, by dictating data avail-
ability and accessibility, directly influence model
performance across the continent’s diverse linguis-
tic spectrum. To achieve this, we conducted a com-
prehensive empirical evaluation of leading large
language models (LLMs) on SAHARA, an exten-
sive benchmark assembled primarily from existing
datasets. SAHARA consists of 30 publicly accessi-
ble datasets, covering 16 classification, generation,
MCCR, and token level tasks. We also introduced
the first publicly available leaderboard for African
languages. Our evaluations revealed critical gaps
in task performance and language coverage, un-
derscoring pronounced disparities rooted in policy-
induced data inequities. Moreover, our findings
highlight the importance of integrating theoretical
insights on language policies with empirical evalu-
ations to inform forward-thinking policy reforms
and promote inclusive data practices. We believe
that SAHARA will serve as essential benchmarking
standards, catalyzing future research and develop-
ment efforts aimed at bridging the digital divide
and fostering linguistic diversity in artificial intelli-
gence for African communities.

--- Page 10 ---

9
Limitations
We identify the following limitations for our work:
1. Data and Data Availability Bias. Our bench-
mark relies on publicly available datasets,
which inherently reflect existing biases in lan-
guage documentation and institutional sup-
port. Many Indigenous African languages re-
main severely underrepresented due to histori-
cal policies that prioritize dominant languages.
As a result, our findings may not fully capture
the linguistic diversity of the continent.
2. Task Scope.
The evaluation primarily fo-
cuses on tasks where data is available, such as
language identification and text classification.
However, the scarcity of datasets for complex
NLP tasks (e.g., machine translation, question
answering) limits our ability to assess model
performance in broader applications. Future
efforts should address this gap by developing
more comprehensive datasets across a wider
range of tasks.
3. Model Performance Constraints. While we
analyze the impact of data scarcity on model
effectiveness, our study does not explore ar-
chitectural modifications or fine-tuning strate-
gies that could improve performance for
low-resource languages. Further research is
needed to examine whether adaptive tech-
niques, such as multilingual pretraining with
targeted data augmentation, could mitigate
these challenges.
4. Policy Implementation Challenges. Our rec-
ommendations for policy reforms and inclu-
sive data practices require significant insti-
tutional commitment and resources. While
we outline actionable steps, their adoption de-
pends on the willingness of governments, re-
search institutions, and technology develop-
ers to prioritize African language inclusion in
NLP.
Despite these limitations, our work underscores
the urgency of addressing data inequities and ad-
vocating for policies that foster greater linguistic
diversity in AI development.
10
Ethical Considerations
We make the following ethics-related statements
about our work:
1. Our research aims to investigate the progress
of NLP for African languages, addressing his-
torical language policies that have contributed
to data inequities. By improving representa-
tion in NLP, we align with broader efforts to
foster linguistic diversity in AI, ensuring that
African languages are not sidelined in techno-
logical advancements.
2. The datasets used in our benchmark are de-
rived from publicly available sources, yet their
existence is shaped by historical and con-
temporary policies that prioritize certain lan-
guages over others. We acknowledge that the
digital presence of African languages is not
merely a technical issue but a policy-driven re-
ality that influences which languages receive
institutional support and investment.
3. Although we do not develop models in this
work, our findings highlight the impact of
policy-induced data disparities on model per-
formance. Addressing these challenges re-
quires policy interventions that support multi-
lingual data collection, equitable resource al-
location, and ethical considerations in dataset
creation.
4. Proper attribution to dataset authors is not
just an academic necessity but a policy im-
perative for transparency and recognition. To
mitigate concerns about data ownership and
ethical usage, we provide a publicly accessi-
ble reference file citing all datasets included
in our benchmark. We strongly encourage re-
searchers and policymakers to acknowledge
these sources, reinforcing the importance of
ethical and inclusive data practices.
Acknowledgments
We acknowledge support from Canada Research
Chairs (CRC), CLEAR Global funding from the
Gates Foundation, the Natural Sciences and En-
gineering Research Council of Canada (NSERC;
RGPIN-2018-04267), the Social Sciences and Hu-
manities Research Council of Canada (SSHRC;
895-2020-1004; 895-2021-1008), Canadian Foun-
dation for Innovation (CFI; 37771), Digital Re-
search Alliance of Canada,5 and UBC ARC-
Sockeye.6 We also thank Clémentine Fourrier and
5https://alliancecan.ca
6https://arc.ubc.ca/ubc-arc-sockeye

--- Page 11 ---

Nouamane Tazi from HuggingFace for providing
feedback on this work. The findings and conclu-
sions contained within this work those of the au-
thors and do not necessarily reflect positions or
policies of any supporters.
References
Marah Abdin, Jyoti Aneja, Hany Awadalla, Ahmed
Awadallah, Ammar Ahmad Awan, Nguyen Bach,
Amit Bahree, Arash Bakhtiari, Jianmin Bao, Harkirat
Behl, Alon Benhaim, Misha Bilenko, Johan Bjorck,
Sébastien Bubeck, Martin Cai, Qin Cai, Vishrav
Chaudhary, Dong Chen, Dongdong Chen, Weizhu
Chen, Yen-Chun Chen, Yi-Ling Chen, Hao Cheng,
Parul Chopra, Xiyang Dai, Matthew Dixon, Ro-
nen Eldan, Victor Fragoso, Jianfeng Gao, Mei Gao,
Min Gao, Amit Garg, Allie Del Giorno, Abhishek
Goswami, Suriya Gunasekar, Emman Haider, Jun-
heng Hao, Russell J. Hewett, Wenxiang Hu, Jamie
Huynh, Dan Iter, Sam Ade Jacobs, Mojan Javaheripi,
Xin Jin, Nikos Karampatziakis, Piero Kauffmann,
Mahoud Khademi, Dongwoo Kim, Young Jin Kim,
Lev Kurilenko, James R. Lee, Yin Tat Lee, Yuanzhi
Li, Yunsheng Li, Chen Liang, Lars Liden, Xihui
Lin, Zeqi Lin, Ce Liu, Liyuan Liu, Mengchen Liu,
Weishung Liu, Xiaodong Liu, Chong Luo, Piyush
Madan, Ali Mahmoudzadeh, David Majercak, Matt
Mazzola, Caio César Teodoro Mendes, Arindam Mi-
tra, Hardik Modi, Anh Nguyen, Brandon Norick,
Barun Patra, Daniel Perez-Becker, Thomas Portet,
Reid Pryzant, Heyang Qin, Marko Radmilac, Liliang
Ren, Gustavo de Rosa, Corby Rosset, Sambudha Roy,
Olatunji Ruwase, Olli Saarikivi, Amin Saied, Adil
Salim, Michael Santacroce, Shital Shah, Ning Shang,
Hiteshi Sharma, Yelong Shen, Swadheen Shukla, Xia
Song, Masahiro Tanaka, Andrea Tupini, Praneetha
Vaddamanu, Chunyu Wang, Guanhua Wang, Lijuan
Wang, Shuohang Wang, Xin Wang, Yu Wang, Rachel
Ward, Wen Wen, Philipp Witte, Haiping Wu, Xiaoxia
Wu, Michael Wyatt, Bin Xiao, Can Xu, Jiahang Xu,
Weijian Xu, Jilong Xue, Sonali Yadav, Fan Yang,
Jianwei Yang, Yifan Yang, Ziyi Yang, Donghan Yu,
Lu Yuan, Chenruidong Zhang, Cyril Zhang, Jianwen
Zhang, Li Lyna Zhang, Yi Zhang, Yue Zhang, Yunan
Zhang, and Xiren Zhou. 2024. Phi-3 technical report:
A highly capable language model locally on your
phone.
Josh Achiam, Steven Adler, Sandhini Agarwal, Lama
Ahmad, Ilge Akkaya, Florencia Leoni Aleman,
Diogo Almeida, Janko Altenschmidt, Sam Altman,
Shyamal Anadkat, et al. 2023. Gpt-4 technical report.
arXiv preprint arXiv:2303.08774.
Ife Adebara and Muhammad Abdul-Mageed. 2022. To-
wards afrocentric NLP for African languages: Where
we are and where we can go. In Proceedings of the
60th Annual Meeting of the Association for Compu-
tational Linguistics (Volume 1: Long Papers), pages
3814–3841, Dublin, Ireland. Association for Compu-
tational Linguistics.
Ife Adebara, AbdelRahim Elmadany, and Muhammad
Abdul-Mageed. 2024a. Cheetah: Natural language
generation for 517 African languages. In Proceed-
ings of the 62nd Annual Meeting of the Association
for Computational Linguistics (Volume 1: Long Pa-
pers), pages 12798–12823, Bangkok, Thailand and
virtual meeting. Association for Computational Lin-
guistics.
Ife Adebara, AbdelRahim Elmadany, and Muhammad
Abdul-Mageed. 2024b. Cheetah: Natural language
generation for 517 african languages.
Ife Adebara, AbdelRahim Elmadany, Muhammad
Abdul-Mageed, and Alcides Alcoba Inciarte. 2023.
SERENGETI: Massively multilingual language mod-
els for Africa. In Findings of the Association for
Computational Linguistics: ACL 2023, pages 1498–
1537, Toronto, Canada. Association for Computa-
tional Linguistics.
Ife Adebara, AbdelRahim Elmadany, Muhammad
Abdul-Mageed, and Alcides Alcoba Inciarte. 2022.
Afrolid: A neural language identification tool for
african languages.
D. Adelani, Jade Abbott, Graham Neubig, Daniel
D’Souza, Julia Kreutzer, Constantine Lignos, Chester
Palen-Michel, Happy Buzaaba, Shruti Rijhwani,
Sebastian Ruder, Stephen Mayhew, Israel Abebe
Azime, S. Muhammad, Chris C. Emezue, Joyce
Nakatumba-Nabende, Perez Ogayo, Anuoluwapo
Aremu, Catherine Gitau, Derguene Mbaye, J. Alabi,
Seid Muhie Yimam, Tajuddeen R. Gwadabe, Ignatius
Ezeani, Rubungo Andre Niyongabo, Jonathan Muki-
ibi, V. Otiende, Iroro Orife, Davis David, Samba
Ngom, Tosin P. Adewumi, Paul Rayson, Mofe-
toluwa Adeyemi, Gerald Muriuki, Emmanuel Anebi,
C. Chukwuneke, N. Odu, Eric Peter Wairagala,
S. Oyerinde, Clemencia Siro, Tobius Saul Bateesa,
Temilola Oloyede, Yvonne Wambui, Victor Akin-
ode, Deborah Nabagereka, Maurice Katusiime, Ay-
odele Awokoya, Mouhamadane Mboup, D. Gebrey-
ohannes, Henok Tilaye, Kelechi Nwaike, Degaga
Wolde, Abdoulaye Faye, Blessing Sibanda, Ore-
vaoghene Ahia, Bonaventure F. P. Dossou, Kelechi
Ogueji, Thierno Ibrahima Diop, A. Diallo, Adewale
Akinfaderin, T. Marengereke, and Salomey Osei.
2021a. Masakhaner: Named entity recognition for
african languages. ArXiv, abs/2103.11811.
David Adelani, Jesujoba Alabi, Angela Fan, Julia
Kreutzer, Xiaoyu Shen, Machel Reid, Dana Ruiter,
Dietrich Klakow, Peter Nabende, Ernie Chang, Tajud-
deen Gwadabe, Freshia Sackey, Bonaventure F. P.
Dossou, Chris Emezue, Colin Leong, Michael Beuk-
man, Shamsuddeen Muhammad, Guyo Jarso, Oreen
Yousuf, Andre Niyongabo Rubungo, Gilles Hacheme,
Eric Peter Wairagala, Muhammad Umair Nasir, Ben-
jamin Ajibade, Tunde Ajayi, Yvonne Gitau, Jade
Abbott, Mohamed Ahmed, Millicent Ochieng, An-
uoluwapo Aremu, Perez Ogayo, Jonathan Mukiibi,
Fatoumata Ouoba Kabore, Godson Kalipe, Derguene

--- Page 12 ---

Mbaye, Allahsera Auguste Tapo, Victoire Memd-
jokam Koagne, Edwin Munkoh-Buabeng, Valen-
cia Wagner, Idris Abdulmumin, Ayodele Awokoya,
Happy Buzaaba, Blessing Sibanda, Andiswa Bukula,
and Sam Manthalu. 2022a. A few thousand trans-
lations go a long way! leveraging pre-trained mod-
els for African news translation. In Proceedings of
the 2022 Conference of the North American Chap-
ter of the Association for Computational Linguistics:
Human Language Technologies, pages 3053–3070,
Seattle, United States. Association for Computational
Linguistics.
David Adelani, Hannah Liu, Xiaoyu Shen, Nikita Vassi-
lyev, Jesujoba Alabi, Yanke Mao, Haonan Gao, and
En-Shiun Lee. 2024a. SIB-200: A simple, inclusive,
and big evaluation dataset for topic classification in
200+ languages and dialects. In Proceedings of the
18th Conference of the European Chapter of the As-
sociation for Computational Linguistics (Volume 1:
Long Papers), pages 226–245, St. Julian’s, Malta.
Association for Computational Linguistics.
David Adelani, Graham Neubig, Sebastian Ruder,
Shruti Rijhwani, Michael Beukman, Chester Palen-
Michel, Constantine Lignos, Jesujoba Alabi, Sham-
suddeen Muhammad,
Peter Nabende,
Cheikh
M. Bamba Dione, Andiswa Bukula, Rooweither
Mabuya, Bonaventure F. P. Dossou, Blessing Sibanda,
Happy Buzaaba, Jonathan Mukiibi, Godson Kalipe,
Derguene Mbaye, Amelia Taylor, Fatoumata Kabore,
Chris Chinenye Emezue, Anuoluwapo Aremu, Perez
Ogayo, Catherine Gitau, Edwin Munkoh-Buabeng,
Victoire Memdjokam Koagne, Allahsera Auguste
Tapo, Tebogo Macucwa, Vukosi Marivate, Mbon-
ing Tchiaze Elvis, Tajuddeen Gwadabe, Tosin
Adewumi, Orevaoghene Ahia, and Joyce Nakatumba-
Nabende. 2022b. MasakhaNER 2.0: Africa-centric
transfer learning for named entity recognition. In Pro-
ceedings of the 2022 Conference on Empirical Meth-
ods in Natural Language Processing, pages 4488–
4508, Abu Dhabi, United Arab Emirates. Association
for Computational Linguistics.
David Adelani, Dana Ruiter, Jesujoba Alabi, Damilola
Adebonojo, Adesina Ayeni, Mofe Adeyemi, Ayo-
dele Esther Awokoya, and Cristina España-Bonet.
2021b. The effect of domain and diacritics in Yoruba–
English neural machine translation.
In Proceed-
ings of Machine Translation Summit XVIII: Research
Track, pages 61–75, Virtual. Association for Machine
Translation in the Americas.
David Ifeoluwa Adelani, Jade Abbott, Graham Neu-
big, Daniel D’souza, Julia Kreutzer, Constantine Lig-
nos, Chester Palen-Michel, Happy Buzaaba, Shruti
Rijhwani, Sebastian Ruder, Stephen Mayhew, Is-
rael Abebe Azime, Shamsuddeen H. Muhammad,
Chris Chinenye Emezue, Joyce Nakatumba-Nabende,
Perez Ogayo, Aremu Anuoluwapo, Catherine Gitau,
Derguene Mbaye, Jesujoba Alabi, Seid Muhie Yi-
mam, Tajuddeen Rabiu Gwadabe, Ignatius Ezeani,
Rubungo Andre Niyongabo, Jonathan Mukiibi, Ver-
rah Otiende, Iroro Orife, Davis David, Samba Ngom,
Tosin Adewumi, Paul Rayson, Mofetoluwa Adeyemi,
Gerald Muriuki, Emmanuel Anebi, Chiamaka Chuk-
wuneke, Nkiruka Odu, Eric Peter Wairagala, Samuel
Oyerinde, Clemencia Siro, Tobius Saul Bateesa,
Temilola Oloyede, Yvonne Wambui, Victor Akin-
ode, Deborah Nabagereka, Maurice Katusiime, Ayo-
dele Awokoya, Mouhamadane MBOUP, Dibora Ge-
breyohannes, Henok Tilaye, Kelechi Nwaike, De-
gaga Wolde, Abdoulaye Faye, Blessing Sibanda, Ore-
vaoghene Ahia, Bonaventure F. P. Dossou, Kelechi
Ogueji, Thierno Ibrahima DIOP, Abdoulaye Diallo,
Adewale Akinfaderin, Tendai Marengereke, and Sa-
lomey Osei. 2021c. MasakhaNER: Named entity
recognition for African languages.
Transactions
of the Association for Computational Linguistics,
9:1116–1131.
David Ifeoluwa Adelani, Marek Masiak, Israel Abebe
Azime, Jesujoba Alabi, Atnafu Lambebo Tonja,
Christine Mwase, Odunayo Ogundepo, Bonaventure
F. P. Dossou, Akintunde Oladipo, Doreen Nixdorf,
Chris Chinenye Emezue, Sana Al-azzawi, Blessing
Sibanda, Davis David, Lolwethu Ndolela, Jonathan
Mukiibi, Tunde Ajayi, Tatiana Moteu, Brian Odhi-
ambo, Abraham Owodunni, Nnaemeka Obiefuna,
Muhidin Mohamed, Shamsuddeen Hassan Muham-
mad, Teshome Mulugeta Ababu, Saheed Abdul-
lahi Salahudeen, Mesay Gemeda Yigezu, Tajud-
deen Gwadabe, Idris Abdulmumin, Mahlet Taye,
Oluwabusayo Awoyomi, Iyanuoluwa Shode, Tolu-
lope Adelani, Habiba Abdulganiyu, Abdul-Hakeem
Omotayo, Adetola Adeeko, Abeeb Afolabi, An-
uoluwapo Aremu, Olanrewaju Samuel, Clemencia
Siro, Wangari Kimotho, Onyekachi Ogbu, Chinedu
Mbonu, Chiamaka Chukwuneke, Samuel Fanijo, Jes-
sica Ojo, Oyinkansola Awosan, Tadesse Kebede,
Toadoum Sari Sakayo, Pamela Nyatsine, Freed-
more Sidume, Oreen Yousuf, Mardiyyah Odu-
wole, Kanda Tshinu, Ussen Kimanuka, Thina
Diko, Siyanda Nxakama, Sinodos Nigusse, Ab-
dulmejid Johar, Shafie Mohamed, Fuad Mire Has-
san, Moges Ahmed Mehamed, Evrard Ngabire,
Jules Jules, Ivan Ssenkungu, and Pontus Stenetorp.
2023. MasakhaNEWS: News topic classification for
African languages. In Proceedings of the 13th In-
ternational Joint Conference on Natural Language
Processing and the 3rd Conference of the Asia-Pacific
Chapter of the Association for Computational Lin-
guistics (Volume 1: Long Papers), pages 144–159,
Nusa Dua, Bali. Association for Computational Lin-
guistics.
David Ifeoluwa Adelani, Graham Neubig, Sebas-
tian Ruder, Shruti Rijhwani, Michael Beukman,
Chester Palen-Michel, Constantine Lignos, Je-
sujoba Oluwadara Alabi, Shamsuddeen Hassan
Muhammad, Peter Nabende, Cheikh M. Bamba
Dione,
Andiswa Bukula,
Rooweither Mabuya,
Bonaventure F. P. Dossou, Blessing K. Sibanda,
Happy Buzaaba, Jonathan Mukiibi, Godson Kalipe,
Derguene Mbaye, Amelia Taylor, Fatoumata Kabore,
Chris C. Emezue, Anuoluwapo Aremu, Perez Ogayo,
Catherine W. Gitau, Edwin Munkoh-Buabeng, Vic-
toire Memdjokam Koagne, Allahsera Auguste Tapo,

--- Page 13 ---

Tebogo Macucwa, Vukosi Marivate, Elvis Mbon-
ing, Tajuddeen R. Gwadabe, Tosin P. Adewumi, Ore-
vaoghene Ahia, Joyce Nakatumba-Nabende, Neo L.
Mokono, Ignatius M Ezeani, Chiamaka Ijeoma Chuk-
wuneke, Mofetoluwa Adeyemi, Gilles Hacheme,
Idris Abdulmumin, Odunayo Ogundepo, Oreen
Yousuf, Tatiana Moteu Ngoli, and Dietrich Klakow.
2022c.
Masakhaner 2.0:
Africa-centric trans-
fer learning for named entity recognition. ArXiv,
abs/2210.12391.
David Ifeoluwa Adelani, Jessica Ojo, Israel Abebe Az-
ime, Jian Yun Zhuang, Jesujoba O. Alabi, Xuanli He,
Millicent Ochieng, Sara Hooker, Andiswa Bukula,
En-Shiun Annie Lee, Chiamaka Chukwuneke, Happy
Buzaaba, Blessing Sibanda, Godson Kalipe, Jonathan
Mukiibi, Salomon Kabongo, Foutse Yuehgoh, Mma-
sibidi Setaka, Lolwethu Ndolela, Nkiruka Odu,
Rooweither Mabuya, Shamsuddeen Hassan Muham-
mad, Salomey Osei, Sokhar Samb, Tadesse Kebede
Guge, and Pontus Stenetorp. 2024b. Irokobench: A
new benchmark for african languages in the age of
large language models.
Benjamin Akera, Jonathan Mukiibi, Lydia Sanyu Nag-
gayi, Claire Babirye, Isaac Owomugisha, Solomon
Nsumba, Joyce Nakatumba-Nabende, Engineer Bain-
omugisha, Ernest Mwebaze, and John Quinn. 2022.
Machine translation for african languages: Commu-
nity creation of datasets and models in uganda. In 3rd
Workshop on African Natural Language Processing.
Jesujoba Alabi, Kwabena Amponsah-Kaakyire, David
Adelani, and Cristina España-Bonet. 2020a. Massive
vs. curated embeddings for low-resourced languages:
the case of Yorùbá and Twi. In Proceedings of the
Twelfth Language Resources and Evaluation Confer-
ence, pages 2754–2762, Marseille, France. European
Language Resources Association.
Jesujoba Alabi, Kwabena Amponsah-Kaakyire, David
Adelani, and Cristina Espana-Bonet. 2020b. Massive
vs. curated embeddings for low-resourced languages:
The case of Yorùbá and Twi. In Proceedings of The
12th Language Resources and Evaluation Confer-
ence, pages 2754–2762.
Jesujoba O. Alabi, David Ifeoluwa Adelani, Marius
Mosbach, and Dietrich Klakow. 2022. Adapting pre-
trained language models to African languages via
multilingual adaptive fine-tuning. In Proceedings of
the 29th International Conference on Computational
Linguistics, pages 4336–4349, Gyeongju, Republic
of Korea. International Committee on Computational
Linguistics.
Saminu Mohammad Aliyu, Gregory Maksha Wajiga,
Muhammad Murtala, Shamsuddeen Hassan Muham-
mad, Idris Abdulmumin, and Ibrahim Said Ahmad.
2022. Herdphobia: A dataset for hate speech against
fulani in nigeria.
Anthropic. 2024. The claude 3 model family: Opus,
sonnet, haiku anthropic. Technical report, Anthropic.
Viraat Aryabumi, John Dang, Dwarak Talupuru,
Saurabh Dash, David Cairuz, Hangyu Lin, Bharat
Venkitesh, Madeline Smith, Jon Ander Campos,
Yi Chern Tan, Kelly Marchisio, Max Bartolo, Se-
bastian Ruder, Acyr Locatelli, Julia Kreutzer, Nick
Frosst, Aidan Gomez, Phil Blunsom, Marzieh Fadaee,
Ahmet Üstün, and Sara Hooker. 2024. Aya 23: Open
weight releases to further multilingual progress.
Israel Abebe Azime and Nebil Mohammed. 2021. An
amharic news text classification dataset.
Lucas Bandarkar, Davis Liang, Benjamin Muller, Mikel
Artetxe, Satya Narayan Shukla, Donald Husa, Naman
Goyal, Abhinandan Krishnan, Luke Zettlemoyer, and
Madian Khabsa. 2024a. The belebele benchmark: a
parallel reading comprehension dataset in 122 lan-
guage variants. In Proceedings of the 62nd Annual
Meeting of the Association for Computational Lin-
guistics (Volume 1: Long Papers), pages 749–775,
Bangkok, Thailand and virtual meeting. Association
for Computational Linguistics.
Lucas Bandarkar, Davis Liang, Benjamin Muller, Mikel
Artetxe, Satya Narayan Shukla, Donald Husa, Naman
Goyal, Abhinandan Krishnan, Luke Zettlemoyer, and
Madian Khabsa. 2024b. The belebele benchmark: a
parallel reading comprehension dataset in 122 lan-
guage variants. In Proceedings of the 62nd Annual
Meeting of the Association for Computational Lin-
guistics (Volume 1: Long Papers), page 749–775.
Association for Computational Linguistics.
Abhik Bhattacharjee, Tahmid Hasan, Wasi Uddin Ah-
mad, and Rifat Shahriyar. 2023. BanglaNLG and
BanglaT5: Benchmarks and resources for evaluating
low-resource natural language generation in Bangla.
In Findings of the Association for Computational
Linguistics: EACL 2023, pages 726–735, Dubrovnik,
Croatia. Association for Computational Linguistics.
Steven Bird. 2020. Decolonising speech and language
technology. In Proceedings of the 28th International
Conference on Computational Linguistics, pages
3504–3519, Barcelona, Spain (Online). International
Committee on Computational Linguistics.
Jiaao Chen, Derek Tam, Colin Raffel, Mohit Bansal,
and Diyi Yang. 2023. An Empirical Survey of Data
Augmentation for Limited Data Learning in NLP.
Transactions of the Association for Computational
Linguistics, 11:191–211.
Wei-Rui Chen, Ife Adebara, Khai Doan, Qisheng Liao,
and Muhammad Abdul-Mageed. 2024. Fumbling
in babel: An investigation into ChatGPT’s language
identification ability. In Findings of the Association
for Computational Linguistics: NAACL 2024, pages
4387–4413, Mexico City, Mexico. Association for
Computational Linguistics.
Victor Ngu Cheo, Esther Phubon Chie, and Yollande
Menguie. 2023. An evaluation of media use of in-
digenous languages in cameroon. The International
Journal of African Language and Media Studies
(IJALMS), 30:1–20.

--- Page 14 ---

Jonathan H. Clark, Eunsol Choi, Michael Collins, Dan
Garrette, Tom Kwiatkowski, Vitaly Nikolaev, and
Jennimaria Palomaki. 2020. TyDi QA: A benchmark
for information-seeking question answering in typo-
logically diverse languages. Transactions of the As-
sociation for Computational Linguistics, 8:454–470.
Team Cohere, Arash Ahmadian, Marwan Ahmed,
Jay Alammar, Milad Alizadeh, Yazeed Alnumay,
Sophia Althammer, Arkady Arkhangorodsky, Viraat
Aryabumi, Dennis Aumiller, et al. 2025. Command
a: An enterprise-ready large language model. arXiv
preprint arXiv:2504.00698.
Alexis Conneau, Kartikay Khandelwal, Naman Goyal,
Vishrav Chaudhary, Guillaume Wenzek, Francisco
Guzmán, Edouard Grave, Myle Ott, Luke Zettle-
moyer, and Veselin Stoyanov. 2020. Unsupervised
cross-lingual representation learning at scale. In Pro-
ceedings of the 58th Annual Meeting of the Asso-
ciation for Computational Linguistics, pages 8440–
8451, Online. Association for Computational Lin-
guistics.
Alexis Conneau, Ruty Rinott, Guillaume Lample, Ad-
ina Williams, Samuel R. Bowman, Holger Schwenk,
and Veselin Stoyanov. 2018. Xnli: Evaluating cross-
lingual sentence representations. In Proceedings of
the 2018 Conference on Empirical Methods in Natu-
ral Language Processing. Association for Computa-
tional Linguistics.
Marta R Costa-jussà, James Cross, Onur Çelebi, Maha
Elbayad, Kenneth Heafield, Kevin Heffernan, Elahe
Kalbassi, Janice Lam, Daniel Licht, Jean Maillard,
et al. 2022.
No language left behind: Scaling
human-centered machine translation. arXiv preprint
arXiv:2207.04672.
Davis David. 2020a.
Swahili : News classification
dataset.
Davis David. 2020b.
Swahili : News classification
dataset. The news version contains both train and
test sets.
Jacob Devlin, Ming-Wei Chang, Kenton Lee, and
Kristina Toutanova. 2018. BERT: pre-training of
deep bidirectional transformers for language under-
standing. CoRR, abs/1810.04805.
Mountaga Diallo, Chayma Fourati, and Hatem Had-
dad. 2021. Bambara language dataset for sentiment
analysis.
Cheikh M. Bamba Dione,
David Adelani,
Pe-
ter Nabende, Jesujoba Alabi, Thapelo Sindane,
Happy Buzaaba, Shamsuddeen Hassan Muhammad,
Chris Chinenye Emezue, Perez Ogayo, Anuoluwapo
Aremu, Catherine Gitau, Derguene Mbaye, Jonathan
Mukiibi, Blessing Sibanda, Bonaventure F. P. Dos-
sou, Andiswa Bukula, Rooweither Mabuya, Al-
lahsera Auguste Tapo, Edwin Munkoh-Buabeng,
victoire Memdjokam Koagne, Fatoumata Ouoba
Kabore, Amelia Taylor, Godson Kalipe, Tebogo
Macucwa, Vukosi Marivate, Tajuddeen Gwadabe,
Mboning Tchiaze Elvis, Ikechukwu Onyenwe, Gra-
tien Atindogbe, Tolulope Adelani, Idris Akinade,
Olanrewaju Samuel, Marien Nahimana, Th’eogene
Musabeyezu, Emile Niyomutabazi, Ester Chimhenga,
Kudzai Gotosa, Patrick Mizha, Apelete Agbolo, Sey-
dou Traore, Chinedu Uchechukwu, Aliyu Yusuf,
Muhammad Abdullahi, and Dietrich Klakow. 2023a.
Masakhapos: Part-of-speech tagging for typologi-
cally diverse african languages.
Cheikh M. Bamba Dione, David Ifeoluwa Adelani,
Peter Nabende, Jesujoba Alabi, Thapelo Sindane,
Happy Buzaaba, Shamsuddeen Hassan Muhammad,
Chris Chinenye Emezue, Perez Ogayo, Anuoluwapo
Aremu, Catherine Gitau, Derguene Mbaye, Jonathan
Mukiibi, Blessing Sibanda, Bonaventure F. P. Dos-
sou, Andiswa Bukula, Rooweither Mabuya, Allah-
sera Auguste Tapo, Edwin Munkoh-Buabeng, Vic-
toire Memdjokam Koagne, Fatoumata Ouoba Ka-
bore, Amelia Taylor, Godson Kalipe, Tebogo
Macucwa, Vukosi Marivate, Tajuddeen Gwadabe,
Mboning Tchiaze Elvis, Ikechukwu Onyenwe, Gra-
tien Atindogbe, Tolulope Adelani, Idris Akinade,
Olanrewaju Samuel, Marien Nahimana, Théogène
Musabeyezu, Emile Niyomutabazi, Ester Chimhenga,
Kudzai Gotosa, Patrick Mizha, Apelete Agbolo, Sey-
dou Traore, Chinedu Uchechukwu, Aliyu Yusuf,
Muhammad Abdullahi, and Dietrich Klakow. 2023b.
MasakhaPOS: Part-of-speech tagging for typolog-
ically diverse African languages. In Proceedings
of the 61st Annual Meeting of the Association for
Computational Linguistics (Volume 1: Long Papers),
pages 10883–10900, Toronto, Canada. Association
for Computational Linguistics.
Long Doan, Linh The Nguyen, Nguyen Luong Tran,
Thai Hoang, and Dat Quoc Nguyen. 2021. PhoMT:
A high-quality and large-scale benchmark dataset for
Vietnamese-English machine translation. In Proceed-
ings of the 2021 Conference on Empirical Methods
in Natural Language Processing, pages 4495–4503,
Online and Punta Cana, Dominican Republic. Asso-
ciation for Computational Linguistics.
Abhimanyu Dubey, Abhinav Jauhri, Abhinav Pandey,
Abhishek Kadian, Ahmad Al-Dahle, Aiesha Letman,
Akhil Mathur, Alan Schelten, Amy Yang, Angela
Fan, Anirudh Goyal, Anthony Hartshorn, Aobo Yang,
Archi Mitra, Archie Sravankumar, Artem Korenev,
Arthur Hinsvark, Arun Rao, Aston Zhang, Aurelien
Rodriguez, Austen Gregerson, Ava Spataru, Bap-
tiste Roziere, Bethany Biron, Binh Tang, Bobbie
Chern, Charlotte Caucheteux, Chaya Nayak, Chloe
Bi, Chris Marra, Chris McConnell, Christian Keller,
Christophe Touret, Chunyang Wu, Corinne Wong,
Cristian Canton Ferrer, Cyrus Nikolaidis, Damien Al-
lonsius, Daniel Song, Danielle Pintz, Danny Livshits,
David Esiobu, Dhruv Choudhary, Dhruv Mahajan,
Diego Garcia-Olano, Diego Perino, Dieuwke Hupkes,
Egor Lakomkin, Ehab AlBadawy, Elina Lobanova,
Emily Dinan, Eric Michael Smith, Filip Radenovic,
Frank Zhang, Gabriel Synnaeve, Gabrielle Lee, Geor-
gia Lewis Anderson, Graeme Nail, Gregoire Mi-

--- Page 15 ---

alon, Guan Pang, Guillem Cucurell, Hailey Nguyen,
Hannah Korevaar, Hu Xu, Hugo Touvron, Iliyan
Zarov, Imanol Arrieta Ibarra, Isabel Kloumann, Ishan
Misra, Ivan Evtimov, Jade Copet, Jaewon Lee, Jan
Geffert, Jana Vranes, Jason Park, Jay Mahadeokar,
Jeet Shah, Jelmer van der Linde, Jennifer Billock,
Jenny Hong, Jenya Lee, Jeremy Fu, Jianfeng Chi,
Jianyu Huang, Jiawen Liu, Jie Wang, Jiecao Yu,
Joanna Bitton, Joe Spisak, Jongsoo Park, Joseph
Rocca, Joshua Johnstun, Joshua Saxe, Junteng Jia,
Kalyan Vasuden Alwala, Kartikeya Upasani, Kate
Plawiak, Ke Li, Kenneth Heafield, Kevin Stone,
Khalid El-Arini, Krithika Iyer, Kshitiz Malik, Kuen-
ley Chiu, Kunal Bhalla, Lauren Rantala-Yeary, Lau-
rens van der Maaten, Lawrence Chen, Liang Tan, Liz
Jenkins, Louis Martin, Lovish Madaan, Lubo Malo,
Lukas Blecher, Lukas Landzaat, Luke de Oliveira,
Madeline Muzzi, Mahesh Pasupuleti, Mannat Singh,
Manohar Paluri, Marcin Kardas, Mathew Oldham,
Mathieu Rita, Maya Pavlova, Melanie Kambadur,
Mike Lewis, Min Si, Mitesh Kumar Singh, Mona
Hassan, Naman Goyal, Narjes Torabi, Nikolay Bash-
lykov, Nikolay Bogoychev, Niladri Chatterji, Olivier
Duchenne, Onur Çelebi, Patrick Alrassy, Pengchuan
Zhang, Pengwei Li, Petar Vasic, Peter Weng, Pra-
jjwal Bhargava, Pratik Dubal, Praveen Krishnan,
Punit Singh Koura, Puxin Xu, Qing He, Qingxiao
Dong, Ragavan Srinivasan, Raj Ganapathy, Ramon
Calderer, Ricardo Silveira Cabral, Robert Stojnic,
Roberta Raileanu, Rohit Girdhar, Rohit Patel, Ro-
main Sauvestre, Ronnie Polidoro, Roshan Sumbaly,
Ross Taylor, Ruan Silva, Rui Hou, Rui Wang, Saghar
Hosseini, Sahana Chennabasappa, Sanjay Singh,
Sean Bell, Seohyun Sonia Kim, Sergey Edunov,
Shaoliang Nie, Sharan Narang, Sharath Raparthy,
Sheng Shen, Shengye Wan, Shruti Bhosale, Shun
Zhang, Simon Vandenhende, Soumya Batra, Spencer
Whitman, Sten Sootla, Stephane Collot, Suchin Gu-
rurangan, Sydney Borodinsky, Tamar Herman, Tara
Fowler, Tarek Sheasha, Thomas Georgiou, Thomas
Scialom, Tobias Speckbacher, Todor Mihaylov, Tong
Xiao, Ujjwal Karn, Vedanuj Goswami, Vibhor
Gupta, Vignesh Ramanathan, Viktor Kerkez, Vincent
Gonguet, Virginie Do, Vish Vogeti, Vladan Petro-
vic, Weiwei Chu, Wenhan Xiong, Wenyin Fu, Whit-
ney Meers, Xavier Martinet, Xiaodong Wang, Xiao-
qing Ellen Tan, Xinfeng Xie, Xuchao Jia, Xuewei
Wang, Yaelle Goldschlag, Yashesh Gaur, Yasmine
Babaei, Yi Wen, Yiwen Song, Yuchen Zhang, Yue
Li, Yuning Mao, Zacharie Delpierre Coudert, Zheng
Yan, Zhengxing Chen, Zoe Papakipos, Aaditya Singh,
Aaron Grattafiori, Abha Jain, Adam Kelsey, Adam
Shajnfeld, Adithya Gangidi, Adolfo Victoria, Ahuva
Goldstand, Ajay Menon, Ajay Sharma, Alex Boesen-
berg, Alex Vaughan, Alexei Baevski, Allie Feinstein,
Amanda Kallet, Amit Sangani, Anam Yunus, An-
drei Lupu, Andres Alvarado, Andrew Caples, An-
drew Gu, Andrew Ho, Andrew Poulton, Andrew
Ryan, Ankit Ramchandani, Annie Franco, Apara-
jita Saraf, Arkabandhu Chowdhury, Ashley Gabriel,
Ashwin Bharambe, Assaf Eisenman, Azadeh Yaz-
dan, Beau James, Ben Maurer, Benjamin Leonhardi,
Bernie Huang, Beth Loyd, Beto De Paola, Bhargavi
Paranjape, Bing Liu, Bo Wu, Boyu Ni, Braden Han-
cock, Bram Wasti, Brandon Spence, Brani Stojkovic,
Brian Gamido, Britt Montalvo, Carl Parker, Carly
Burton, Catalina Mejia, Changhan Wang, Changkyu
Kim, Chao Zhou, Chester Hu, Ching-Hsiang Chu,
Chris Cai, Chris Tindal, Christoph Feichtenhofer, Da-
mon Civin, Dana Beaty, Daniel Kreymer, Daniel Li,
Danny Wyatt, David Adkins, David Xu, Davide Tes-
tuggine, Delia David, Devi Parikh, Diana Liskovich,
Didem Foss, Dingkang Wang, Duc Le, Dustin Hol-
land, Edward Dowling, Eissa Jamil, Elaine Mont-
gomery, Eleonora Presani, Emily Hahn, Emily Wood,
Erik Brinkman, Esteban Arcaute, Evan Dunbar, Evan
Smothers, Fei Sun, Felix Kreuk, Feng Tian, Firat
Ozgenel, Francesco Caggioni, Francisco Guzmán,
Frank Kanayet, Frank Seide, Gabriela Medina Flo-
rez, Gabriella Schwarz, Gada Badeer, Georgia Swee,
Gil Halpern, Govind Thattai, Grant Herman, Grigory
Sizov, Guangyi, Zhang, Guna Lakshminarayanan,
Hamid Shojanazeri, Han Zou, Hannah Wang, Han-
wen Zha, Haroun Habeeb, Harrison Rudolph, He-
len Suk, Henry Aspegren, Hunter Goldman, Ibrahim
Damlaj, Igor Molybog, Igor Tufanov, Irina-Elena
Veliche, Itai Gat, Jake Weissman, James Geboski,
James Kohli, Japhet Asher, Jean-Baptiste Gaya,
Jeff Marcus, Jeff Tang, Jennifer Chan, Jenny Zhen,
Jeremy Reizenstein, Jeremy Teboul, Jessica Zhong,
Jian Jin, Jingyi Yang, Joe Cummings, Jon Carvill,
Jon Shepard, Jonathan McPhie, Jonathan Torres,
Josh Ginsburg, Junjie Wang, Kai Wu, Kam Hou
U, Karan Saxena, Karthik Prasad, Kartikay Khan-
delwal, Katayoun Zand, Kathy Matosich, Kaushik
Veeraraghavan, Kelly Michelena, Keqian Li, Kun
Huang, Kunal Chawla, Kushal Lakhotia, Kyle Huang,
Lailin Chen, Lakshya Garg, Lavender A, Leandro
Silva, Lee Bell, Lei Zhang, Liangpeng Guo, Licheng
Yu, Liron Moshkovich, Luca Wehrstedt, Madian
Khabsa, Manav Avalani, Manish Bhatt, Maria Tsim-
poukelli, Martynas Mankus, Matan Hasson, Matthew
Lennie, Matthias Reso, Maxim Groshev, Maxim
Naumov, Maya Lathi, Meghan Keneally, Michael L.
Seltzer, Michal Valko, Michelle Restrepo, Mihir
Patel, Mik Vyatskov, Mikayel Samvelyan, Mike
Clark, Mike Macey, Mike Wang, Miquel Jubert Her-
moso, Mo Metanat, Mohammad Rastegari, Mun-
ish Bansal, Nandhini Santhanam, Natascha Parks,
Natasha White, Navyata Bawa, Nayan Singhal, Nick
Egebo, Nicolas Usunier, Nikolay Pavlovich Laptev,
Ning Dong, Ning Zhang, Norman Cheng, Oleg
Chernoguz, Olivia Hart, Omkar Salpekar, Ozlem
Kalinli, Parkin Kent, Parth Parekh, Paul Saab, Pa-
van Balaji, Pedro Rittner, Philip Bontrager, Pierre
Roux, Piotr Dollar, Polina Zvyagina, Prashant Ratan-
chandani, Pritish Yuvraj, Qian Liang, Rachad Alao,
Rachel Rodriguez, Rafi Ayub, Raghotham Murthy,
Raghu Nayani, Rahul Mitra, Raymond Li, Rebekkah
Hogan, Robin Battey, Rocky Wang, Rohan Mah-
eswari, Russ Howes, Ruty Rinott, Sai Jayesh Bondu,
Samyak Datta, Sara Chugh, Sara Hunt, Sargun
Dhillon, Sasha Sidorov, Satadru Pan, Saurabh Verma,
Seiji Yamamoto, Sharadh Ramaswamy, Shaun Lind-
say, Shaun Lindsay, Sheng Feng, Shenghao Lin,
Shengxin Cindy Zha, Shiva Shankar, Shuqiang

--- Page 16 ---

Zhang, Shuqiang Zhang, Sinong Wang, Sneha Agar-
wal, Soji Sajuyigbe, Soumith Chintala, Stephanie
Max, Stephen Chen, Steve Kehoe, Steve Satterfield,
Sudarshan Govindaprasad, Sumit Gupta, Sungmin
Cho, Sunny Virk, Suraj Subramanian, Sy Choudhury,
Sydney Goldman, Tal Remez, Tamar Glaser, Tamara
Best, Thilo Kohler, Thomas Robinson, Tianhe Li,
Tianjun Zhang, Tim Matthews, Timothy Chou, Tzook
Shaked, Varun Vontimitta, Victoria Ajayi, Victoria
Montanez, Vijai Mohan, Vinay Satish Kumar, Vishal
Mangla, Vítor Albiero, Vlad Ionescu, Vlad Poenaru,
Vlad Tiberiu Mihailescu, Vladimir Ivanov, Wei Li,
Wenchen Wang, Wenwen Jiang, Wes Bouaziz, Will
Constable, Xiaocheng Tang, Xiaofang Wang, Xiao-
jian Wu, Xiaolan Wang, Xide Xia, Xilun Wu, Xinbo
Gao, Yanjun Chen, Ye Hu, Ye Jia, Ye Qi, Yenda Li,
Yilin Zhang, Ying Zhang, Yossi Adi, Youngjin Nam,
Yu, Wang, Yuchen Hao, Yundi Qian, Yuzi He, Zach
Rait, Zachary DeVito, Zef Rosnbrick, Zhaoduo Wen,
Zhenyu Yang, and Zhiwei Zhao. 2024. The llama 3
herd of models.
David M Eberhard, F Simons Gary, and Charles D Fen-
nig (eds). 2021. Ethnologue: Languages of the world.
Twenty-fourth edition, Dallas, Texas: SIL Interna-
tional.
Roald Eiselen. 2016. Government domain named entity
recognition for South African languages. In Proceed-
ings of the Tenth International Conference on Lan-
guage Resources and Evaluation (LREC’16), pages
3344–3348, Portorož, Slovenia. European Language
Resources Association (ELRA).
AbdelRahim Elmadany, Ife Adebara, and Muhammad
Abdul-Mageed. 2024. Toucan: Many-to-many trans-
lation for 150 African language pairs. In Findings of
the Association for Computational Linguistics ACL
2024, pages 13189–13206, Bangkok, Thailand and
virtual meeting. Association for Computational Lin-
guistics.
AbdelRahim Elmadany, ElMoatez Billah Nagoudi, and
Muhammad Abdul-Mageed. 2023. ORCA: A chal-
lenging benchmark for Arabic language understand-
ing. In Findings of the Association for Computa-
tional Linguistics: ACL 2023, pages 9559–9586,
Toronto, Canada. Association for Computational Lin-
guistics.
Danny S Foster. 2021. Language of Instruction in Rural
Tanzania: A Critical Analysis of Parents’ Discursive
Practices and Valued Linguistic Capabilities. Ph.D.
thesis, University of Bristol.
Sebastian Gehrmann, Tosin Adewumi, Karmanya
Aggarwal,
Pawan
Sasanka
Ammanamanchi,
Anuoluwapo
Aremu,
Antoine
Bosselut,
Khy-
athi Raghavi Chandu, Miruna-Adriana Clinciu,
Dipanjan Das, Kaustubh Dhole, Wanyu Du, Esin
Durmus, Ondˇrej Dušek, Chris Chinenye Emezue,
Varun
Gangal,
Cristina
Garbacea,
Tatsunori
Hashimoto, Yufang Hou, Yacine Jernite, Harsh Jham-
tani, Yangfeng Ji, Shailza Jolly, Mihir Kale, Dhruv
Kumar, Faisal Ladhak, Aman Madaan, Mounica
Maddela, Khyati Mahajan, Saad Mahamood, Bod-
hisattwa Prasad Majumder, Pedro Henrique Martins,
Angelina McMillan-Major, Simon Mille, Emiel van
Miltenburg, Moin Nadeem, Shashi Narayan, Vitaly
Nikolaev, Andre Niyongabo Rubungo, Salomey
Osei,
Ankur
Parikh,
Laura
Perez-Beltrachini,
Niranjan Ramesh Rao, Vikas Raunak, Juan Diego
Rodriguez,
Sashank
Santhanam,
João
Sedoc,
Thibault Sellam, Samira Shaikh, Anastasia Shimo-
rina, Marco Antonio Sobrevilla Cabezudo, Hendrik
Strobelt, Nishant Subramani, Wei Xu, Diyi Yang,
Akhila Yerukola, and Jiawei Zhou. 2021.
The
GEM benchmark:
Natural language generation,
its evaluation and metrics. In Proceedings of the
1st Workshop on Natural Language Generation,
Evaluation, and Metrics (GEM 2021), pages 96–120,
Online. Association for Computational Linguistics.
Jian Guan, Zhuoer Feng, Yamei Chen, Ruilin He, Xiaoxi
Mao, Changjie Fan, and Minlie Huang. 2022. LOT:
A Story-Centric Benchmark for Evaluating Chinese
Long Text Understanding and Generation. Transac-
tions of the Association for Computational Linguis-
tics, 10:434–451.
Tri Wahyu Guntara, Alham Fikri Aji, and Radityo Eko
Prasojo. 2020. Benchmarking multidomain English-
Indonesian machine translation. In Proceedings of
the 13th Workshop on Building and Using Compara-
ble Corpora, pages 35–43, Marseille, France. Euro-
pean Language Resources Association.
Jiyeon Ham, Yo Joong Choe, Kyubyong Park, Ilji Choi,
and Hyungjoon Soh. 2020. KorNLI and KorSTS:
New Benchmark Datasets for Korean Natural Lan-
guage Understanding. In Findings of the Association
for Computational Linguistics: EMNLP 2020, pages
422–430.
Tahmid Hasan, Abhik Bhattacharjee, Md. Saiful Is-
lam, Kazi Mubasshir, Yuan-Fang Li, Yong-Bin Kang,
M. Sohel Rahman, and Rifat Shahriyar. 2021. XL-
sum: Large-scale multilingual abstractive summariza-
tion for 44 languages. In Findings of the Association
for Computational Linguistics: ACL-IJCNLP 2021,
pages 4693–4703, Online. Association for Computa-
tional Linguistics.
Michael A. Hedderich, David Adelani, Dawei Zhu, Je-
sujoba Alabi, Udia Markus, and Dietrich Klakow.
2020. Transfer learning and distant supervision for
multilingual transformer models: A study on African
languages. In Proceedings of the 2020 Conference on
Empirical Methods in Natural Language Processing
(EMNLP), pages 2580–2591, Online. Association for
Computational Linguistics.
Daniel Hershcovich, Stella Frank, Heather Lent,
Miryam de Lhoneux, Mostafa Abdou, Stephanie
Brandl, Emanuele Bugliarello, Laura Cabello Pi-
queras, Ilias Chalkidis, Ruixiang Cui, Constanza
Fierro, Katerina Margatina, Phillip Rust, and Anders
Søgaard. 2022. Challenges and strategies in cross-
cultural NLP. In Proceedings of the 60th Annual

--- Page 17 ---

Meeting of the Association for Computational Lin-
guistics (Volume 1: Long Papers), pages 6997–7013,
Dublin, Ireland. Association for Computational Lin-
guistics.
Junjie Hu, Sebastian Ruder, Aditya Siddhant, Graham
Neubig, Orhan Firat, and Melvin Johnson. 2020.
Xtreme: A massively multilingual multi-task bench-
mark for evaluating cross-lingual generalization.
Comfort Eseohen Ilevbare, Jesujoba O. Alabi, David Ife-
oluwa Adelani, Firdous Damilola Bakare, Oluwa-
toyin Bunmi Abiola,
and Oluwaseyi Adesina
Adeyemo. 2024. Ekohate: Abusive language and
hate speech detection for code-switched political dis-
cussions on nigerian twitter.
Pratik Joshi, Sebastin Santy, Amar Budhiraja, Kalika
Bali, and Monojit Choudhury. 2020. The state and
fate of linguistic diversity and inclusion in the NLP
world. In Proceedings of the 58th Annual Meeting of
the Association for Computational Linguistics, pages
6282–6293, Online. Association for Computational
Linguistics.
Odunayo Jude Ogundepo, Akintunde Oladipo, Mofe-
toluwa Adeyemi, Kelechi Ogueji, and Jimmy Lin.
2022. AfriTeVA: Extending ?small data? pretrain-
ing approaches to sequence-to-sequence models. In
Proceedings of the Third Workshop on Deep Learn-
ing for Low-Resource Natural Language Processing,
pages 126–135, Hybrid. Association for Computa-
tional Linguistics.
Kentaro Kurihara, Daisuke Kawahara, and Tomohide
Shibata. 2022. Jglue: Japanese general language
understanding evaluation. In Proceedings of the Thir-
teenth Language Resources and Evaluation Confer-
ence, pages 2957–2966.
Hang Le, Loïc Vial, Jibril Frej, Vincent Segonne, Max-
imin Coavoux, Benjamin Lecouteux, Alexandre Al-
lauzen, Benoit Crabbé, Laurent Besacier, and Didier
Schwab. 2020. FlauBERT: Unsupervised Language
Model Pre-training for French. In Proceedings of
The 12th Language Resources and Evaluation Con-
ference, pages 2479–2490.
Yaobo Liang, Nan Duan, Yeyun Gong, Ning Wu, Fenfei
Guo, Weizhen Qi, Ming Gong, Linjun Shou, Daxin
Jiang, Guihong Cao, Xiaodong Fan, Ruofei Zhang,
Rahul Agrawal, Edward Cui, Sining Wei, Taroon
Bharti, Ying Qiao, Jiun-Hung Chen, Winnie Wu,
Shuguang Liu, Fan Yang, Daniel Campos, Rangan
Majumder, and Ming Zhou. 2020. XGLUE: A new
benchmark dataset for cross-lingual pre-training, un-
derstanding and generation. In Proceedings of the
2020 Conference on Empirical Methods in Natural
Language Processing (EMNLP), pages 6008–6018,
Online. Association for Computational Linguistics.
Tshepang
Molale
and
Phillip
Mpofu.
2023.
(Dis)continuities of african language radio on
social media: The case of south africa’s motsweding
fm and radio zimbabwe. In African Language Media,
1 edition, page 14. Routledge.
Shamsuddeen Muhammad, Idris Abdulmumin, Abinew
Ayele, Nedjma Ousidhoum, David Adelani, Seid Yi-
mam, Ibrahim Ahmad, Meriem Beloucif, Saif Mo-
hammad, Sebastian Ruder, Oumaima Hourrane, Ali-
pio Jorge, Pavel Brazdil, Felermino Ali, Davis David,
Salomey Osei, Bello Shehu-Bello, Falalu Lawan,
Tajuddeen Gwadabe, Samuel Rutunda, Tadesse Be-
lay, Wendimu Messelle, Hailu Balcha, Sisay Chala,
Hagos Gebremichael, Bernard Opoku, and Stephen
Arthur. 2023a. AfriSenti: A Twitter sentiment anal-
ysis benchmark for African languages. In Proceed-
ings of the 2023 Conference on Empirical Methods in
Natural Language Processing, pages 13968–13981,
Singapore. Association for Computational Linguis-
tics.
Shamsuddeen Hassan Muhammad, Idris Abdulmu-
min, Seid Muhie Yimam, David Ifeoluwa Ade-
lani, Ibrahim Sa’id Ahmad, Nedjma Ousidhoum,
Abinew Ali Ayele, Saif M. Mohammad, Meriem
Beloucif, and Sebastian Ruder. 2023b. SemEval-
2023 Task 12: Sentiment Analysis for African Lan-
guages (AfriSenti-SemEval). In Proceedings of the
17th International Workshop on Semantic Evalua-
tion (SemEval-2023). Association for Computational
Linguistics.
Shamsuddeen Hassan Muhammad, David Ifeoluwa Ade-
lani, Sebastian Ruder, Ibrahim Sa’id Ahmad, Idris
Abdulmumin, Bello Shehu Bello, Monojit Choud-
hury, Chris Chinenye Emezue, Saheed Salahudeen
Abdullahi, Anuoluwapo Aremu, Alípio orge, and
Pavel Brazdil. 2022. NaijaSenti: A Nigerian Twitter
sentiment corpus for multilingual sentiment analy-
sis. In Proceedings of the Thirteenth Language Re-
sources and Evaluation Conference, pages 590–602,
Marseille, France. European Language Resources
Association.
Mary Myers and Nicola Harford. 2020. Local radio sta-
tions in africa: Sustainability or pragmatic viability?
El Moatez Billah Nagoudi, AbdelRahim Elmadany,
Ahmed El-Shangiti, and Muhammad Abdul-Mageed.
2023. Dolphin: A challenging and diverse bench-
mark for Arabic NLG. In Findings of the Associa-
tion for Computational Linguistics: EMNLP 2023,
pages 1404–1422, Singapore. Association for Com-
putational Linguistics.
Ramesh Nallapati, Bowen Zhou, Cicero dos Santos,
Ça˘glar Gu˙lçehre, and Bing Xiang. 2016. Abstrac-
tive text summarization using sequence-to-sequence
RNNs and beyond.
In Proceedings of the 20th
SIGNLL Conference on Computational Natural Lan-
guage Learning, pages 280–290, Berlin, Germany.
Association for Computational Linguistics.
National Communications Authority. 2016. List of au-
thorised vhf-fm radio stations in ghana. Third Quar-
ter.
Rubungo Andre Niyongabo, Qu Hong, Julia Kreutzer,
and Li Huang. 2020. KINNEWS and KIRNEWS:
Benchmarking cross-lingual text classification for

--- Page 18 ---

Kinyarwanda and Kirundi. In Proceedings of the
28th International Conference on Computational Lin-
guistics, pages 5507–5521, Barcelona, Spain (On-
line). International Committee on Computational Lin-
guistics.
Kelechi Ogueji and Orevaoghene Ahia. 2019. Pidgin-
unmt: Unsupervised neural machine translation from
west african pidgin to english.
Kelechi Ogueji, Yuxin Zhu, and Jimmy Lin. 2021.
Small data? no problem! exploring the viability
of pretrained multilingual language models for low-
resourced languages. In Proceedings of the 1st Work-
shop on Multilingual Representation Learning, pages
116–126, Punta Cana, Dominican Republic. Associa-
tion for Computational Linguistics.
Akintunde Oladipo,
Mofetoluwa Adeyemi,
Ore-
vaoghene Ahia, Abraham Owodunni, Odunayo Ogun-
depo, David Adelani, and Jimmy Lin. 2023. Better
quality pre-training data and t5 models for African
languages. In Proceedings of the 2023 Conference on
Empirical Methods in Natural Language Processing,
pages 158–168, Singapore. Association for Compu-
tational Linguistics.
Ikechukwu E Onyenwe, Mark Hepple, Uchechukwu
Chinedu, and Ignatius Ezeani. 2018a. A basic lan-
guage resource kit implementation for the IgboNLP
project. ACM Trans. Asian Low-Resour. Lang. Inf.
Process., 17(2).
Ikechukwu E Onyenwe, Mark Hepple, Uchechukwu
Chinedu, and Ignatius Ezeani. 2018b. A basic lan-
guage resource kit implementation for the igbonlp
project. ACM Trans. Asian Low-Resour. Lang. Inf.
Process., 17(2).
Ikechukwu E. Onyenwe, Mark Hepple, Uchechukwu
Chinedu, and Ignatius Ezeani. 2019. Toward an effec-
tive Igbo part-of-speech tagger. ACM Trans. Asian
Low-Resour. Lang. Inf. Process., 18(4).
Sylvester Olubolu Orimaye, Saadat M. Alhashmi, and
Siew Eu-gene. 2012. Sentiment analysis amidst am-
biguities in youtube comments on yoruba language
(nollywood) movies. In Proceedings of the 21st In-
ternational Conference on World Wide Web, WWW
’12 Companion, page 583–584, New York, NY, USA.
Association for Computing Machinery.
Adama Ouane and Christine Glanz. 2010. How and
why Africa should invest in African languages and
multilingual education: An evidence-and practice-
based policy advocacy brief. UNESCO Institute for
Lifelong Learning.
Folajimi Oyebola and Kingsley Ugwuanyi. 2023. Atti-
tudes of nigerians towards bbc pidgin: A preliminary
study. Language Matters, 54(1):78–101.
Wuraola Fisayo Oyewusi, Olubayo Adekanmbi, and
Olalekan Akinsande. 2020. Semantic enrichment
of nigerian pidgin english for contextual sentiment
classification.
Xiaoman Pan, Boliang Zhang, Jonathan May, Joel Noth-
man, Kevin Knight, and Heng Ji. 2017. Cross-lingual
name tagging and linking for 282 languages. In Pro-
ceedings of the 55th Annual Meeting of the Associa-
tion for Computational Linguistics (Volume 1: Long
Papers), pages 1946–1958, Vancouver, Canada. As-
sociation for Computational Linguistics.
Malin Petzell. 2012. The linguistic situation in Tanzania.
Moderna språk, 106(1):136–144.
Afshin Rahimi, Yuan Li, and Trevor Cohn. 2019. Mas-
sively multilingual transfer for NER. In Proceedings
of the 57th Annual Meeting of the Association for
Computational Linguistics, pages 151–164, Florence,
Italy. Association for Computational Linguistics.
Machel Reid, Junjie Hu, Graham Neubig, and Yutaka
Matsuo. 2021a. AfroMT: Pretraining strategies and
reproducible benchmarks for translation of 8 African
languages. In Proceedings of the 2021 Conference
on Empirical Methods in Natural Language Process-
ing, pages 1306–1320, Online and Punta Cana, Do-
minican Republic. Association for Computational
Linguistics.
Machel Reid, Junjie Hu, Graham Neubig, and Yutaka
Matsuo. 2021b. AfroMT: Pretraining strategies and
reproducible benchmarks for translation of 8 african
languages. In Conference on Empirical Methods in
Natural Language Processing (EMNLP), Punta Cana,
Dominican Republic.
E. ResCue and G. E. Agbozo. 2021. Creating trans-
lated interfaces: The representations of african lan-
guages and cultures in digital media. In Rethinking
Language Use in Digital Africa: Technology and
Communication in Sub-Saharan Africa, pages 51–72.
Multilingual Matters & Channel View Publications.
Yves Scherrer. 2020. TaPaCo: A corpus of sentential
paraphrases for 73 languages. In Proceedings of the
Twelfth Language Resources and Evaluation Confer-
ence, pages 6868–6873, Marseille, France. European
Language Resources Association.
Iyanuoluwa Shode, David Ifeoluwa Adelani, and Anna
Feldman. 2022a. yosm: A new yoruba sentiment
corpus for movie reviews.
Iyanuoluwa Shode, David Ifeoluwa Adelani, and Anna
Feldman. 2022b.
YOSM: A new Yorùbá Senti-
ment Corpus for Movie Reviews. AfricaNLP 2022
@ICLR.
Oloruntola Sunday, Ayo Yusuff, Simon Godwin Ire-
tomiwa, Vincent Adakole Obia, and Samuel Eji-
wunmi. 2018. Use of indigenous languages for social
media communication: The nigerian experience. In
African Language Digital Media and Communica-
tion, 1 edition, page 15. Routledge.
Gemma Team, Morgane Riviere, Shreya Pathak,
Pier Giuseppe Sessa, Cassidy Hardin, Surya Bhupati-
raju, Léonard Hussenot, Thomas Mesnard, Bobak
Shahriari, Alexandre Ramé, Johan Ferret, Peter

--- Page 19 ---

Liu, Pouya Tafti, Abe Friesen, Michelle Casbon,
Sabela Ramos, Ravin Kumar, Charline Le Lan,
Sammy Jerome, Anton Tsitsulin, Nino Vieillard,
Piotr Stanczyk, Sertan Girgin, Nikola Momchev,
Matt Hoffman, Shantanu Thakoor, Jean-Bastien Grill,
Behnam Neyshabur, Olivier Bachem, Alanna Wal-
ton, Aliaksei Severyn, Alicia Parrish, Aliya Ah-
mad, Allen Hutchison, Alvin Abdagic, Amanda
Carl, Amy Shen, Andy Brock, Andy Coenen, An-
thony Laforge, Antonia Paterson, Ben Bastian, Bilal
Piot, Bo Wu, Brandon Royal, Charlie Chen, Chintu
Kumar, Chris Perry, Chris Welty, Christopher A.
Choquette-Choo, Danila Sinopalnikov, David Wein-
berger, Dimple Vijaykumar, Dominika Rogozi´nska,
Dustin Herbison, Elisa Bandy, Emma Wang, Eric
Noland, Erica Moreira, Evan Senter, Evgenii Elty-
shev, Francesco Visin, Gabriel Rasskin, Gary Wei,
Glenn Cameron, Gus Martins, Hadi Hashemi, Hanna
Klimczak-Pluci´nska, Harleen Batra, Harsh Dhand,
Ivan Nardini, Jacinda Mein, Jack Zhou, James Svens-
son, Jeff Stanway, Jetha Chan, Jin Peng Zhou, Joana
Carrasqueira, Joana Iljazi, Jocelyn Becker, Joe Fer-
nandez, Joost van Amersfoort, Josh Gordon, Josh
Lipschultz, Josh Newlan, Ju yeong Ji, Kareem Mo-
hamed, Kartikeya Badola, Kat Black, Katie Mil-
lican, Keelin McDonell, Kelvin Nguyen, Kiranbir
Sodhia, Kish Greene, Lars Lowe Sjoesund, Lau-
ren Usui, Laurent Sifre, Lena Heuermann, Leti-
cia Lago, Lilly McNealus, Livio Baldini Soares,
Logan Kilpatrick, Lucas Dixon, Luciano Martins,
Machel Reid, Manvinder Singh, Mark Iverson, Mar-
tin Görner, Mat Velloso, Mateo Wirth, Matt Davi-
dow, Matt Miller, Matthew Rahtz, Matthew Watson,
Meg Risdal, Mehran Kazemi, Michael Moynihan,
Ming Zhang, Minsuk Kahng, Minwoo Park, Mofi
Rahman, Mohit Khatwani, Natalie Dao, Nenshad
Bardoliwalla, Nesh Devanathan, Neta Dumai, Nilay
Chauhan, Oscar Wahltinez, Pankil Botarda, Parker
Barnes, Paul Barham, Paul Michel, Pengchong
Jin, Petko Georgiev, Phil Culliton, Pradeep Kup-
pala, Ramona Comanescu, Ramona Merhej, Reena
Jana, Reza Ardeshir Rokni, Rishabh Agarwal, Ryan
Mullins, Samaneh Saadat, Sara Mc Carthy, Sarah
Cogan, Sarah Perrin, Sébastien M. R. Arnold, Se-
bastian Krause, Shengyang Dai, Shruti Garg, Shruti
Sheth, Sue Ronstrom, Susan Chan, Timothy Jordan,
Ting Yu, Tom Eccles, Tom Hennigan, Tomas Ko-
cisky, Tulsee Doshi, Vihan Jain, Vikas Yadav, Vilobh
Meshram, Vishal Dharmadhikari, Warren Barkley,
Wei Wei, Wenming Ye, Woohyun Han, Woosuk
Kwon, Xiang Xu, Zhe Shen, Zhitao Gong, Zichuan
Wei, Victor Cotruta, Phoebe Kirk, Anand Rao, Minh
Giang, Ludovic Peran, Tris Warkentin, Eli Collins,
Joelle Barral, Zoubin Ghahramani, Raia Hadsell,
D. Sculley, Jeanine Banks, Anca Dragan, Slav Petrov,
Oriol Vinyals, Jeff Dean, Demis Hassabis, Koray
Kavukcuoglu, Clement Farabet, Elena Buchatskaya,
Sebastian Borgeaud, Noah Fiedel, Armand Joulin,
Kathleen Kenealy, Robert Dadashi, and Alek An-
dreev. 2024. Gemma 2: Improving open language
models at a practical size.
Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier
Martinet, Marie-Anne Lachaux, Timothée Lacroix,
Baptiste Rozière, Naman Goyal, Eric Hambro, Faisal
Azhar, Aurelien Rodriguez, Armand Joulin, Edouard
Grave, and Guillaume Lample. 2023. Llama: Open
and efficient foundation language models.
Michael Walsh. 2005. Will indigenous languages sur-
vive? Annu. Rev. Anthropol., 34(1):293–315.
Bryan Wilie, Karissa Vincentio, Genta Indra Winata,
Samuel Cahyawijaya, Xiaohong Li, Zhi Yuan Lim,
Sidik Soleman, Rahmad Mahendra, Pascale Fung,
Syafri Bahar, et al. 2020. Indonlu: Benchmark and
resources for evaluating indonesian natural language
understanding. arXiv preprint arXiv:2009.05387.
Liang Xu, Hai Hu, Xuanwei Zhang, Lu Li, Chenjie
Cao, Yudong Li, Yechen Xu, Kai Sun, Dian Yu,
Cong Yu, et al. 2020. Clue: A chinese language
understanding evaluation benchmark. arXiv preprint
arXiv:2004.05986.
Yuan Yao, Qingxiu Dong, Jian Guan, Boxi Cao,
Zhengyan Zhang, Chaojun Xiao, Xiaozhi Wang, Fan-
chao Qi, Junwei Bao, Jinran Nie, et al. 2021. CUGE:
A Chinese Language Understanding and Generation
Evaluation Benchmark. arXiv e-prints, pages arXiv–
2112.
Seid Muhie Yimam, Hizkiel Mitiku Alemayehu,
Abinew Ayele, and Chris Biemann. 2020. Exploring
Amharic sentiment analysis from social media texts:
Building annotation tools and classification mod-
els. In Proceedings of the 28th International Con-
ference on Computational Linguistics, pages 1048–
1060, Barcelona, Spain (Online).

--- Page 20 ---

Appendices
A
Sahara Task Clusters
A.1
Text Classification
Cross-Lingual Natural Language Inference.
This task involves the classification of 2 given sen-
tences—a premise and a hypothesis into entailment,
neutral, or contradiction semantic relation (Adelani
et al., 2024b). Adelani et al. (2024b) introduced
AfriXNLI, a benchmark for evaluating 15 African
Languages on Natural Language Inference (NLI).
The languages were translated from the English
portion of XNLI (Conneau et al., 2018).
Language Identification.
We include language
identification datasets across 518 African lan-
guages (Adebara et al., 2022). The dataset includes
data from multiple domains including education,
government, health care, news, and religion. Addi-
tional statistics of the data is available in Table D3.
We include language identification tasks to inves-
tigate (1.)
the capabilities of language models
in correctly generating the appropriate language
names of an input text and (2.) Correctly generate
an additional sentence in a specific language. We
include these two approaches because many lan-
guages have multiple names (Chen et al., 2024) and
a LM’s inability to appropriately name a language
does not implicate a lack of information about the
language.
News Classification.
This task involves automat-
ically categorizing news articles into predefined cat-
egories or topics based on their content. The goal is
to leverage machine learning and NLP techniques
to understand and organize large volumes of news
data, making it easier for users to access relevant in-
formation. News classification plays a crucial role
in information retrieval, content recommendation,
and other applications that involve organizing and
categorizing textual data. The news classification
cluster consists of data from four languages includ-
ing Amharic (Azime and Mohammed, 2021), Kin-
yarwanda (Niyongabo et al., 2020), Kirundi (Niy-
ongabo et al., 2020), and Swahili (David, 2020a,b).
Table D3 provides additional details of the data in
this cluster.
Sentiment Analysis.
Sentiment analysis is cru-
cial in gaining insights into public opinion, cus-
tomer feedback, and user sentiments across various
platforms. The sentiment analysis cluster consists
of the Bambara Sentiment dataset (Diallo et al.,
2021), YOSM–a Sentiment Corpus for Movie Re-
views in Yorùbá (Shode et al., 2022b), and the
Nigerian Pidgin sentiment dataset (Oyewusi et al.,
2020), respectively. Further details about the sta-
tistical composition of this data is available in Ta-
ble D3.
Topic Classification.
The primary goal for this
task is to automatically categorize the content of
the text based on its theme. Topic classification is
widely used in various applications, such as docu-
ment organization, content recommendation, and
information retrieval. We include topic classifi-
cation datasets for Yorùbá and Hausa (Hedderich
et al., 2020).
A.2
Text Generation
Machine Translation.
A robust benchmark for
MT tasks is essential. SAHARA, in its quest to
effectively assess machine translation for African
languages, selectively incorporates datasets con-
taining diverse African languages into its bench-
mark. Specifically, SAHARA includes datasets such
as Pidgin-UNMT7 (Ogueji and Ahia, 2019), Afro-
MT8 (Reid et al., 2021a), Lafand-MT (Adelani
et al., 2022a), SALT9 (Akera et al., 2022), and
HornMT, thus encompassing a total of 45 language
pairs.
Paraphrase.
Paraphrasing is a core task in NLG
that revolves around the comprehension and gener-
ation of text that conveys the same meaning while
possibly exhibiting differences in structure, phras-
ing, or style (Chen et al., 2023). SAHARA incorpo-
rates the TaPaCo dataset (Scherrer, 2020), which
is publicly accessible and covers a total of 73 lan-
guages, including four of African origin. These
African languages consist of Kirundi, Amazigh, a
macro-language Berber, and Afrikaans.
Summarization.
Summarization is the task of
creating a condensed version of a text that retains
its core ideas and essential information (Nallap-
ati et al., 2016). In the context of SAHARA, our
focus primarily centers on a subset of the abstrac-
tive summarization dataset, XL-SUM (Hasan et al.,
2021), which includes several African languages:
Amharic, Hausa, Igbo, Kirundi, Oromo, Pidgin,
7PidginUNMT GitHub Link
8AfroMT GitHub Link
9SALT GitHub Link

--- Page 21 ---

Somali, Swahili, Tigrinya, and Yoruba. Addition-
ally, we have extended our dataset collection ef-
forts by scraping non-overlapping summarization
datasets from BBC and Voice of Africa (VoE) web-
sites, specifically targeting three African languages:
Hausa, Ndebele, and Swahili.
Title Generation.
The task of title generation in
NLG involves generating a concise and meaningful
title or headline for a given article.
This task
shares its dataset source with summarization,
drawing from XL-SUM, and also includes dataset
extensions from BBC and VoE with focus on
enabling zero-shot title generation.
A.3
Multiple-Choice, Comprehensive and
Reasoning
This task cluster majorly addresses Question An-
swering type questions. The QA tasks in this clus-
ter are more mathematical-reasoning and reading-
comprehension-oriented.
Mathematical Word Problems.
(Adelani et al.,
2024b) introduced AfriMGSM, a QA dataset that
contains human-written grade school mathematical
word problems. Their dataset covers 15 African
Languages, and the translation of each question to
English for each language for in-language evalua-
tion of LLMs. In this task, given a word problem,
the LLM is expected to return a numerical value as
output.
General Knowledge QA.
(Adelani et al., 2024b)
introduced AfriMMLU, a multi-choice QA dataset
covering 5 areas of knowledge in 15 African Lan-
guages. The knowledge areas are high-school ge-
ography, high-school microeconomics, elementary
mathematics, international law), and global facts.
In this task given a question in any of the aforemen-
tioned areas, and 4 options, the LLM is expected
to choose the right option.
Reading Comprehension QA.
In this task, the
LLMs are evaluated based on their ability to un-
derstand information in a given article. (Bandarkar
et al., 2024b) introduced a parallel reading com-
prehension dataset covering 122 languages, 23 of
which are native to Africa. The dataset comprises
of short paragraphs accompanied by multi-choice
Questions, whose answers can be inferred from
accompanying paragraphs.
Context-based Question-Answering.
QA rep-
resents another vital facet of NLG, focusing on a
model’s capability to provide answers based on in-
tegrated knowledge. SAHARA relies on the gold
passage dataset from the multilingual TYDIA10 QA
resource (Clark et al., 2020). This dataset offers
concise questions with precisely one correspond-
ing answer, enabling rigorous evaluation of QA
performance.
A.4
Tokens-level Classification
Named Entity Recognition.
We incorporate
NER datasets across 30 languages. We use Dis-
tance Supervision NER (DS NER) Data (Hed-
derich et al., 2020), MasakhaNER (Adelani et al.,
2022b), WikiAnn (Rahimi et al., 2019), Yoruba-
Twi NER (Alabi et al., 2020b), and multiple NER
data from SADiLaR. Additional details about the
datasets are available in Table D3.
Phrase Chunking.
This task involves identify-
ing and grouping together consecutive words or
tokens into meaningful syntactic units, known as
phrases. These phrases can include noun phrases,
verb phrases, prepositional phrases, and other gram-
matical structures. The goal of phrase chunking is
to analyze the grammatical structure of a sentence
and extract higher-level syntactic units for better
understanding. The phrase chunking cluster con-
sists of data for ten Indigenous languages of South
Africa (see Table D3). The data has annotations
for noun, verb, adjective, adverbial, and preposi-
tional phrase chunks. Words not belonging to these
phrase types are labelled with the tag O.
Part of Speech Tagging.
This classification task
involves assigning grammatical categories or labels
(such as noun, verb, adjective) to each word in a
sentence. The primary goal of POS tagging is to
analyze the syntactic structure of a sentence and
understand the role of each word within it. POS
tagging is crucial for various NLP applications, as it
provides a foundation for more advanced linguistic
analysis. We include datasets for Igbo taken from
IgboNLP (Onyenwe et al., 2019).
B
Benchmark
Table B1 shows the comparison between SA-
HARA with other benchmarks.
10TyDiQA GitHub Link

--- Page 22 ---

Category
Benchmark
Reference
Lang/Total
Tasks
Multilingual
FLoRES200
(Costa-jussà et al., 2022)
52/200
1
GEMv1
(Gehrmann et al., 2021)
10/52
5
GEMv2
(Gehrmann et al., 2021)
10/52
9
NLLB M.D.
(Costa-jussà et al., 2022)
2/8
1
NLLB S.D.
(Costa-jussà et al., 2022)
2/8
1
SIB-200
(Adelani et al., 2024a)
46/200
1
Toxicity200
(Costa-jussà et al., 2022)
50/200
1
XGLUE
(Liang et al., 2020)
1/19
3
XTremE
(Hu et al., 2020)
2/40
4
Language-specific
BanglaNLPv1
(Bhattacharjee et al., 2023)
1
6
CLUE
(Xu et al., 2020)
1
6
CUGE
(Yao et al., 2021)
1
8
Dolphin
(Nagoudi et al., 2023)
1
13
FLUE
(Le et al., 2020)
1
5
IndoNLU
(Wilie et al., 2020)
1
5
IndoNLG
(Guntara et al., 2020)
1
6
JGLUE
(Kurihara et al., 2022)
1
3
KorNLU
(Ham et al., 2020)
1
2
LOT
(Guan et al., 2022)
1
4
ORCA
(Elmadany et al., 2023)
1
7
PhoMT
(Doan et al., 2021)
1
1
African
AfriSenti
(Muhammad et al., 2023a)
14
1
AfroMT
(Reid et al., 2021b)
8/8
1
AfroNLG
(Adebara et al., 2024b)
517/517
6
AfroNLU
(Adebara et al., 2023)
28/28
7
Horn-MT
−
3/3
1
Iroko-Bench
(Adelani et al., 2024b)
16/16
3
Mafand-MT
(Adelani et al., 2022a)
17/17
1
Menyo-20k
(Adelani et al., 2021b)
1/1
1
Naija-senti
(Muhammad et al., 2022)
4/4
1
SAHARA
ours
517/517
16
Table B1: A Comparison of SAHARA with other Benchmarks. M.D: Multilingual domain, S.D: Seed Data.
C
Few-shot prompt example
Figure C1 shows an example for MT task.
D
Dataset Description
Table D2 describes all datasets included in SA-
HARA.
E
Data-Performance-Policy Analysis

--- Page 23 ---

Figure C1: Few-shot prompting example for the machine translation task. The prompt provides five examples of the
specific task for context and alignment.

--- Page 24 ---

Dataset
Brief Description
African Language(s)
MasakhaNER (Adelani et al., 2021a),
(Adelani et al., 2022c)
Curated for Named Entity Recognition
for several African Languages
amh, bam, bbj, ewe, fon, hau, ibo, kin,
lug, luo, mos, nya, pcm, sna, swa, tsn,
twi, wol, xho, yor, zul
MasakhaPOS (Dione et al., 2023a)
Curated from News sources and pub-
licly available datasets for Part-Of-
Speech Tagging
bam, bbj, ewe, fon, hau, ibo, kin, lug,
luo, mos, nya, pcm, sna, swa, tsn, twi,
wol, xho, yor, zul
MAFAND-MT (Adelani et al., 2022a)
African news corpus for Machine Trans-
lation
bam, bbj, ewe, fon, hau, ibo, lug, luo,
mos, swa, tsn, twi, wol, xho, yor, zul
XL-Sum Hasan et al. (2021)
Curated for Summarization and Title
Generation
amh, ibo, orm, run, swa, yor, hau, pcm,
som, tir
YorubaSenti (Orimaye et al., 2012)
Curated from comments on movies on
YouTube
yor
TaPaCo (Scherrer, 2020)
Developed to provide example sen-
tences and translations for particular lin-
guistic constructions and words
afr, ber, run , zgh
TyDi QA (Clark et al., 2020)
Curated for Information-Seeking QA
tasks
swa
HornMT
Parallel MT dataset curated for lan-
guages in Horn of Africa
aaf, amh, orm, som, tir
yoruba-twi-ner (Alabi et al., 2020a)
Curated for evaluating embeddings for
low-resource languages
yor, twi
KINNEWS
and
KIRNEWS
(Niy-
ongabo et al., 2020)
Curated for multi-class classification of
news articles
kin, run
AmharicNews (Azime and Mohammed,
2021)
Curated for text classification from
news articles
amh
SwahiliNews v0.2 (David, 2020a)
Curated for text classification from
news articles
swa
Bambara (Diallo et al., 2021)
Curated for Sentiment Analysis through
web crawling
bam
IgboNLP(Onyenwe et al., 2018b)
Contains text corpus, POS tagset and
POS-tagged subcorpus
ibo
yosm (Shode et al., 2022a)
Curated from movie reviews for Senti-
ment Analysis
yor
pidgin-tweet (Oyewusi et al., 2020)
Curated for SA from tweets
pcm
WikiAnn (Pan et al., 2017), (Rahimi
et al., 2019)
afr, amh, ibo, mlg, kin, som, swa, yor
HausaTopic,YorubaTobic (Hedderich
et al., 2020)
Curated for Topic Classification
hau, yor
SaDiLAR (Eiselen, 2016)
Curated for NER of 10 South African
Languages
afr, nbl, nso, sot, ssw, tsn, tso, ven, xho,
zul
AfriSenti (Muhammad et al., 2023a)
Curated for African tweet sentiment
analysis
amh, ALG-ara, hau, kin, ibo, MOR-
ara, MOZ-por, pcm,form, swa, tir,
twi,tso,yor
Afro-MT (Reid et al., 2021a)
Benchmark for MT of 8 African Lan-
guages
afr, bem, lin, run, sot, swa, xho, zul
PidginUNMT (Ogueji et al., 2021)
pcm
SALT (Akera et al., 2022)
Curated for Parallel MT of 5 Ugandan
Languages
ach, lgg, lug, nyn, teo
Cheetah (Adebara et al., 2024b)
Summarization test set
hau, nde, swa
Cheetah (Adebara et al., 2024b)
Title generation test set
amh, gag (zero-shot), hau, ibo, pcm,
som, swa, tir, yor, kin (zero-shot), afr,
mlg (zero-shot), orm, nde (zero-shot),
sna(zero-shot)
NCHLT-NER (Eiselen, 2016)
Named Entity Recognition
afr, nbl, nso, sot, ssw, tsn, tso, ven, xho,
zul
BeleBele (Bandarkar et al., 2024b)
Reading Comprehension MCQA
afr amh, bam, fuv, gaz, hau, ibo,kea,kin,
lin, lug, luo,nso, nya, sna ,som, sot, ssw,
swh, tir, tsn, tso, wol, xho, yor,zul
IrokoBench (Adelani et al., 2024b)
MGSM,MMLU,XNLI
amh, ewe, hau, ibo,kin, lin, lug, orm,
sna ,sot, swa, tir, wol, xho, yor,zul
Table D2: A description of all datasets included in Sahara. ALG: Algerian, MOR: Moroccan, MOZ: Mozambican.

--- Page 25 ---

Task
Source
Language
Train/ Dev/ Test
MT
(Adelani et al., 2022a)
eng-hau
5.9K/ 1.3K/ 1.5K
eng-ibo
6.9K/ 1.5K/ 1.4K
eng-lug
4.1K/ 1.5K/ 1.5K
eng-pcm
4.8K/ 1.5K/ 1.6K
eng-swa
30.8K/ 1.8K/ 1.8K
eng-tsn
2.1K/ 1.3K/ 1.5K
eng-twi
3.3K/ 1.3K/ 1.5K
eng-yor
6.6K/ 1.5K/ 1.6K
eng-zul
3.5K/ 1.5K/ 1.0K
fra-bam
3.0K/ 1.5K/ 1.5K
fra-bbj
2.2K/ 1.1K/ 1.4K
fra-ewe
2.0K/ 1.4K/ 1.6K
fra-fon
2.6K/ 1.2K/ 1.6K
fra-mos
2.5K/ 1.5K/ 1.6K
fra-wol
3.4K/ 1.5K/ 1.5K
(Reid et al., 2021a)
eng-afr
25.8K/ 3.2K/ 3.2K
eng-bem
12.0K/ 1.5K/ 1.5K
eng-lin
17.7K/ 2.2K/ 2.2K
eng-run
12.5K/ 1.6K/ 1.6K
eng-sot
28.8K/ 3.6K/ 3.6K
eng-swa
28.1K/ 3.5K/ 3.5K
eng-xho
26.1K/ 3.3K/ 3.3K
eng-zul
29.1K/ 3.6K/ 3.6K
(Ogueji and Ahia, 2019)
eng-pcm
1.7K/ 0.2K/ 0.2K
(Akera et al., 2022)
All-pairs1
20.0K/ 2.5K/ 2.5K
HornMT
All-pairs2
1.7K/ 0.2K/ 0.2K
NER
(Adelani et al., 2021a)
See Table D2
41.2K/ 5.1K/ 5.1K
(Adelani et al., 2022c)
See Table D2
41.2K/ 5.1K/ 5.1K
(Eiselen, 2016)
See Table D2
1.7M/ 219.7K/ 215.6K
(Alabi et al., 2020a)
See Table D2
20.2K/ 2.8K/ 5.5K
(Pan et al., 2017)
See Table D2
9.2K/ 9.2K/ 9.4K
News
(Azime and Mohammed, 2021)
amh
41.2K/ 5.1K/ 5.1K
(Niyongabo et al., 2020)
kin
15.3K/ 1.7K/ 4.3K
run
3.3K/ 0.4K/ 0.9K
(David, 2020a)
swa
4.4K/ 0.6K/ 0.6K
Paraphrase
(Scherrer, 2020)
amh, ber, kab, run
22.4K/ 2.8K/ 2.8K
ber
17.6K/ 2.2K/ 2.2K
kab
4.4K/ 0.6K/ 0.6K
Phrase Chunking
(Eiselen, 2016)
See Table D2
107.5K/ 13.0K/ 13.4K
POS Tagging
(Onyenwe et al., 2018a, 2019)
ibo
756.8K/ 94.7K/ 95.0K
Question Answering
(Clark et al., 2020)
swa
49.9K/ 0.5K/ n/a
Sentiment Analysis
(Diallo et al., 2021)
bam
2.4K/ 0.3K/0.3K
(Oyewusi et al., 2020)
pcm
11.2K/ 1.4K/ 1.4K
(Shode et al., 2022a)
yor
0.8K/ 0.2K/ 0.5K
Summarization
(Hasan et al., 2021)
amh
5.8K/ 0.7K/ 0.7K
ibo
4.2K/ 0.5K/ 0.5K
orm
6.1K/ 0.8K/ 0.8K
Rundi
5.7K/ 0.7K/ 0.7K
swa
7.9K/ 1.0K/ 1.0K
yor
6.4K/ 0.8K/ 0.8K
hau
6.4K/ 0.8K/ 0.8K
pcm
9.2K/ 1.2K/ 1.2K
som
6.0K/ 0.7K/ 0.7K
Tigrinya
5.5K/ 0.7K/ 0.7K
(Adebara et al., 2024b)
⋆†
-/ -/ 0.4K
Title Generation
(Hasan et al., 2021)
amh
5.8K/ 0.7K/ 0.7K
ibo
4.2K/ 0.5K/ 0.5K
orm
6.1K/ 0.8K/ 0.8K
run
5.7K/ 0.7K/ 0.7K
swa
7.9K/ 1.0K/ 1.0K
yor
6.4K/ 0.8K/ 0.8K
hau
6.4K/ 0.8K/ 0.8K
pcm
9.2K/ 1.2K/ 1.2K
som
6.0K/ 0.7K/ 0.7K
Tigrinya
5.5K/ 0.7K/ 0.7K
(Adebara et al., 2024b)
⋆
-/ -/ 5.9K
Topic Classification
(Hedderich et al., 2020)
hau
2.0K/ 0.3K/0.6K
yor
1.3K/ 0.2K/ 0.4K
Table D3: Statistics of the data in our benchmark. All −pairs1 each have the same size of data. They include
ach-eng, ach-lgg, ach-lug, ach-nyn, ach-teo, ach-teo, eng-lgg, eng-lug, eng-nyn, eng-teo, lgg-teo, lug-lgg, lug-teo,
nyn-lgg, nyn-lug, and nyn-teo. All −pairs2 are all possible language combinations of aaf, amh, orm, som, tir, eng.
⋆† is a summarization test set including ‘hau’, ‘nde’ (zero-shot), and ‘swa’. ⋆is a title generation test set across
15 languages: ‘amh’, ‘gag’ (zero-shot), ‘hau’, ‘ibo’, ‘pcm’, ‘som’, ‘swa’, ‘tir’, ‘yor’, ‘kin’ (zero-shot), ‘afr’, ‘mlg’
(zero-shot), ‘orm’, ‘nde’ (zero-shot), ‘sna’(zero-shot).

--- Page 26 ---

(a) Generation tasks.
(b) Classification tasks.
(c) MCCR tasks.
(d) MT tasks grouped.
Figure E2: Distribution of best open weight model performance (Command-A) on different task clusters across
African languages in downstream data.
Figure E3: Distribution of languages across different clusters. Each bar represents the number of datasets a language
appears in, categorized into the clusters, with some languages appearing in all four clusters while others are only
present in one or two.

--- Page 27 ---

(a) Command-A performers.
(b) Claude-4-Sonnet performance.
Figure E4: Performance of Command-A and Claude-4-Sonnet on token-level task cluster across African
languages in downstream data.

--- Page 28 ---

SLM
LLM
Closed LLM
Cluster
Identifier
Metric
Shots
S1
S2
S3
S4
S5
S6
L1
L2
L3
L4
L5
L6
L7
L8
L9
L10
L11
L12
L13
L14
L15
L16
CL1
CL2
Classification
xlni
Acc.
5
33.6
33.7
36.7
41.18
40.4
46.68
48.08
55.06
34.3
40.69
37.09
61.09
57.86
65.58
44.2
38.19
51.89
48.38
52.09
35.87
46.77
59.67
69
69.6
lid
F1
10
0
0
0.87
0.26
0.85
0.77
2.82
3.6
0
1.49
2.27
1.95
4.61
4
1.81
3.34
3.26
3.07
3.3
3.05
3.32
4.57
3.73
4.48
news
F1
3
0.86
0.35
0.15
17.54
0
6.64
21.94
0
2.06
24.06
0.12
25.83
7.83
35.56
28.03
0.61
35.26
33.31
34.81
3.45
30.46
28.66
40.09
32.19
sentiment
F1
5
38.51
24.75
30.45
11.05
28.77
1.99
36.09
42.47
38.4
28.36
36.07
34.56
20.55
46.35
35.86
25.94
24.51
45.82
35.89
19.98
37.07
47.14
55.67
57.52
topic
F1
3
8.73
31.62
20.3
19.79
12.46
17.15
48.11
39.35
34.95
28.55
42.12
44.3
31.8
70.73
36.47
43.74
64.89
56.48
48.73
52.09
50.96
53.16
67.93
76.57
Avg.
16.34
18.08
17.69
17.96
16.50
14.65
31.41
28.10
21.94
24.63
23.53
33.55
24.53
44.44
29.27
22.36
35.96
37.41
34.96
22.89
33.72
38.64
47.28
48.07
Generation
mt_eng2xx
spBleu1K
5
1.79
3.63
3.45
3.25
2.12
3.4
7.07
7.61
1.72
4.37
2.79
6.24
6.91
4.56
3.73
3.29
8.84
8.7
9.36
1.4
6.06
8.22
12.18
12.36
mt_fra2xx
spBleu1K
5
0.79
0.36
0.74
1.05
1.25
1.32
0.73
0.95
0.7
1.19
0.66
2.03
1.67
2.05
1.15
0.82
1.93
1.87
1.77
1.05
1.04
2.3
3.41
3.42
mt_xx2xx
spBleu1K
5
0.4
0.45
0.42
0.42
0.36
0.18
0.43
0.63
0.72
0.55
0.46
0.71
0.9
1.39
0.55
0.17
1.28
1.05
1.37
0.67
0.38
0.85
5.15
4.44
paraphrase
spBleu1K
5
23.2
28.88
31.15
19.12
25.93
17.85
28.73
25.83
31.68
31.33
23.66
17.26
21.34
15.37
32.13
30.68
26.86
19.64
27.79
19.23
36.06
26.06
23.2
20.35
summary
rougeL
2
10.03
3.24
4.37
10.07
0.91
13.34
15.1
10.43
1.45
12.74
5.92
16.16
15.73
17.13
13.27
4.19
16.92
17.19
16.4
15.46
14.88
16.09
5.99
16.3
title
spBleu1K
2
2.14
2.81
0.25
2.3
0.03
5.78
7.48
5.78
3
5.94
1.58
7.75
7.51
8.65
6.83
3.2
11.07
10.34
8.78
7.32
6.69
8.65
13.62
9.48
Avg.
6.39
6.56
6.73
6.04
5.10
6.98
9.92
8.54
6.55
9.35
5.85
8.36
9.01
8.19
9.61
7.06
11.15
9.80
10.91
7.52
10.85
10.36
10.59
11.06
MCCR
mmlu
Acc.
5
24.09
28.5
28.68
27.29
28.9
30.99
31.88
40.9
26.4
44.51
22.1
42.09
44.9
60.71
51.5
24
56.51
59.3
50.42
59.81
29.8
61.91
81.6
58.6
mgsm
ExactM
5
2.6
3.21
0
1.2
3.39
0.7
2.9
2.8
3.3
2.7
1.5
2.3
5.3
0.6
4.4
3
10.1
7.51
7.6
4.5
4.39
11.1
45.9
29.5
belebele
Acc.
5
27.71
14.71
25.2
29.31
31.31
24.69
22.7
26.93
25.09
28.24
26.33
25.63
31.04
32.34
33.64
26.61
30.4
35.92
33.72
30.83
20.99
29.12
36.6
39.7
squad_qa
F1
5
57.45
70.89
67.32
43.13
71.31
74.97
78.04
80.91
52.66
59.48
63.41
73.78
82.49
79.16
69.25
64.64
77.65
76.35
66.25
53.92
74.64
80.05
78.02
76.11
Avg.
27.96
29.33
30.30
25.23
33.73
32.84
33.88
37.89
26.86
33.73
28.34
35.95
40.93
43.20
39.70
29.56
43.67
44.77
39.50
37.27
32.46
45.55
60.53
50.98
Tokens
ner
F1
5
0
0.78
1.76
2.99
0.13
3.65
2.26
7.49
2.35
3.96
0.2
6.03
13.14
11.4
8.51
1.52
6.86
10.54
8.64
6.04
4.3
16.88
35.06
27.04
phrase
F1
5
14.79
28.5
29.44
11.52
24.91
27.73
15.95
29.35
29.42
16.55
30.87
13.59
30.01
23.97
26.34
23.09
25.55
23.13
16.78
25.13
29.44
31.05
36.69
36.45
pos
F1
5
8.83
6.73
10.56
8.04
10.3
10.46
9.13
13.2
9.81
11.68
12.52
13.86
19
13.99
18.36
11.4
14.13
15.04
11.52
20.76
13.71
27.54
62.84
38.67
Avg.
7.87
12.00
13.92
7.52
11.78
13.95
9.11
16.68
13.86
10.73
14.53
11.16
20.72
16.45
17.74
12.00
15.51
16.24
12.31
17.31
15.82
25.16
44.86
34.05
Overall
14.64
16.49
17.16
14.19
16.78
17.10
21.08
22.80
17.30
19.61
18.06
22.25
23.80
28.07
24.08
17.75
26.57
27.05
24.42
21.25
23.21
29.93
40.82
36.04
Table E4: Few-shot evaluation across different task clusters/tasks. The highest score for each individual task is in bold green , while the best average score across each
task cluster (and overall score, calculated as average of task cluster averages) is in bold orange . Underline: refers to the best score across the open source/weights LLMs.
Shots: number of shots. SLMs: S1 Llama3.2 (1B), S2 Llama3.2 (3B), S3 Gemma2 (2B), S4 Phi-3.5 (3.8B), S5 Phi-4 (3.8B), and S6 Gemma3 (4B). LLMs: L1
Llama3.1 (8B), L2 Gemma2 (9B), L3 Aya (8B), L4 Babel (9B), L5 Command-R-Plus-R7B (8B), L6 Gemma3 (12B), L7 Gemma2 (27B), L8 Gemma3 (27B),
L9 DeepSeek-R1-Distill-Qwen (32B), L10 Aya (35B), L11 Llama3.1 (70B), L12 Llama3.3 (70B), L13 DeepSeek-R1-Distill-Qwen (70B), L14 Babel (83B), L15
Command-R-Plus (104B), L16 Command-A (111B). CLosed LLMs: CL1 Claude-4-Sonnet, CL2 GPT-4.1.

```
