---
title: "2025-Ganea-A Culturally-Rich Romanian NLP Dataset from 'Who Wants to Be a - PDF Extract"
source_pdf: "2025-Ganea-A Culturally-Rich Romanian NLP Dataset from 'Who Wants to Be a.pdf"
pages: 10
extracted_at: "2026-02-13T13:14:08.166685"
---

# PDF Extract: 2025-Ganea-A Culturally-Rich Romanian NLP Dataset from 'Who Wants to Be a

**Source PDF:** 2025-Ganea-A Culturally-Rich Romanian NLP Dataset from 'Who Wants to Be a.pdf
**Total Pages:** 10

---

## Content

```
--- Page 1 ---

A Culturally-Rich Romanian NLP Dataset from "Who Wants to
Be a Millionaire?" Videos
Alexandru-Gabriel Ganea Antonia-Adelina Popovici Adrian-Marius Dumitran
University of Bucharest Faculty of Mathematics and Computer Science
Abstract
Large Language Models (LLMs) demon-
strate varying performance across lan-
guages and cultural contexts. This study
introduces a novel, culturally-rich, multi-
lingual dataset derived from video record-
ings of the Romanian game show "Who
Wants to Be a Millionaire?" (Vrei să
fii Milionar?).
We employed an inno-
vative process combining optical charac-
ter recognition (OCR), automated text ex-
traction, and manual verification to col-
lect question-answer pairs, enriching them
with metadata including question domain
(e.g., biology, history), cultural relevance
(Romanian-specific vs. international), and
difficulty.
Benchmarking state-of-the-art
LLMs, including Romanian-adapted mod-
els, on this dataset revealed significant
performance disparities:
models consis-
tently achieve higher accuracy (80-95%)
on international questions compared to
Romanian-specific cultural questions (50-
75%). We further investigate these differ-
ences through experiments involving ma-
chine translation of Romanian questions
into English and cross-lingual tests using
a comparable dataset in French. Our find-
ings underscore the impact of cultural con-
text and data source on LLM performance
and offer practical insights for building
robust, culturally-aware multilingual NLP
systems, especially in educational domains.
The dataset is publicly available at Hug-
ging Face.
1
Introduction
The rapid advancement of large language mod-
els (LLMs) has transformed many NLP tasks,
including question answering, summarization,
and translation.
However, most evaluations
focus on high-resource languages like English,
leaving a gap in understanding LLM perfor-
mance in lower-resource and culturally diverse
contexts.
To address this, we introduce a Romanian-
language dataset derived from Vrei să fii mil-
ionar?, the local version of "Who Wants to Be
a Millionaire?" 1. Publicly available on Hug-
ging Face 2, the dataset was compiled directly
from video recordings, requiring structured
data extraction from a dynamic visual format
rather than standard text corpora. It reflects
authentic language in a culturally specific, con-
versational quiz show setting. Each question is
annotated for cultural relevance—Romanian-
specific vs. international—and labeled by dif-
ficulty (easy, medium, hard).
Evaluating LLMs in Romanian poses unique
challenges, including complex grammar, rich
vocabulary, and limited NLP resources. This
study investigates how well current mod-
els handle Romanian-language multiple-choice
question answering (MCQA), with emphasis
on cultural knowledge and the performance
impact of Romanian-specific fine-tuning. We
benchmark state-of-the-art open-source LLMs,
including models adapted for Romanian, to
explore the effects of language and cultural
grounding.
Our findings offer insights into the strengths
and limitations of multilingual LLMs in cultur-
ally rich settings and contribute toward build-
ing more inclusive, robust NLP systems for un-
derrepresented languages like Romanian.
2
Related Work
2.1
Linguistic and Cultural Diversity
in LLM Evaluation
While LLMs such as GPT-4 (OpenAI, 2023),
PaLM (Chowdhery et al., 2022), and LLaMA
1https://en.wikipedia.org/wiki/Who_Wants_
to_Be_a_Millionaire
2https://huggingface.co/datasets/WWTBM/
wwtbm
arXiv:2506.05991v1  [cs.CL]  6 Jun 2025

--- Page 2 ---

(Touvron et al., 2023) have shown impressive
performance across a wide range of bench-
marks, most evaluation datasets are heavily
skewed toward English or other high-resource
languages (Wang et al., 2022; Nangia et al.,
2021).
This imbalance limits our under-
standing of how well these models general-
ize to linguistically and culturally diverse con-
texts.
Several efforts have highlighted this
issue and proposed multilingual benchmarks
such as XTREME (Hu et al., 2020) and
XGLUE (Liang et al., 2020), but these often
lack deep cultural grounding and fail to include
many underrepresented languages.
More recent work has turned attention to
culturally situated evaluation.
For example,
the BOLD benchmark(Dhamala et al., 2021)
introduces cultural dimensions to evaluate bi-
ases in language models.
2.2
Romanian NLP Datasets and
Resources
Romanian, as a mid-resource language, has
seen increasing support through dedicated
datasets and benchmarks.
The RoBERT
model (Dumitrescu et al., 2020), based on
the original BERT architecture and trained
specifically for Romanian, is not to be con-
fused with RoBERTa (Liu et al., 2019), a ro-
bustly optimized BERT approach pretrained
on larger, English-focused corpora.
Foun-
dational resources like CoRoLa (Tufiş et al.,
2017) have further enabled robust pretraining
and evaluation. More recently, the "Vorbesti
Românes,te?" initiative (Masala et al., 2024)
introduced a large-scale instruction-tuned Ro-
manian benchmark suite, along with open-
source models and datasets that significantly
advance the capabilities of Romanian LLMs
across multiple evaluation categories.
2.3
Language Models for Romanian
and Other Underrepresented
Languages
Several transformer-based models have been
trained or adapted specifically for Romanian,
such as RoBERT and DistilRoBERTa (Sanh
et al., 2019) include Romanian as part of their
training data, although their performance on
Romanian tasks varies greatly depending on
the domain and task complexity.
In the broader context of low-resource or
typologically diverse languages, projects like
Masakhane (Nekoto et al., 2020) and Amer-
icasNLP (Mager et al., 2021) advocate for
community-driven, culturally-aware NLP de-
velopment. These projects underscore the im-
portance of local expertise and participatory
research in building fair and effective NLP
tools for underrepresented languages.
In
line
with
efforts
to
support
under-
represented languages, our work emphasizes
the value of non-traditional data sources for
NLP development.
Unlike most Romanian-
language datasets, which are typically derived
from written corpora, our approach leverages
video recordings of a quiz show to extract
question-answer pairs. This not only provides
a more dynamic linguistic sample—complete
with spoken language nuances and cultural ref-
erences—but also demonstrates how alterna-
tive modalities can be harnessed to build more
representative NLP resources.
3
Dataset Creation
We developed a multilingual dataset centered
on the Romanian edition of the quiz show
Who Wants to Be a Millionaire?.
The core
of this resource is the highly curated and an-
notated Romanian dataset. To facilitate com-
parative and cross-lingual analysis, we also
translated this primary Romanian data into
English and curated parallel datasets in En-
glish and French, following a similar structure
where possible. The creation process for the
primary Romanian dataset involved multiple
steps, outlined below.
3.1
Data Collection and Frame
Extraction
The final dataset comprises 1000 multiple-
choice questions collected from publicly avail-
able video recordings.
Approximately 400
questions originated from episodes aired be-
tween 2011–2012 3, obtained via Google Drive,
and around 600 questions were extracted
from 2018–2019 episodes downloaded from
YouTube. 4
Each video was analyzed frame-by-frame to
capture screenshots precisely when the cor-
3https://drive.google.com/drive/folders/
1zjO0P_awwSm52uWQKc9gMpEh25LrVfnC
4https://www.youtube.com/playlist?list=
PLvC_Gs1fsycShkx65zNpIqUhlgTuVI8UB

--- Page 3 ---

Figure 1: Example of question frame
rect answer turned green, signifying correct-
ness. To avoid redundancy, subsequent frames
(approximately 500 frames per question) were
skipped. Captured images were manually re-
viewed to ensure accuracy.
3.2
Text Extraction and Diacritic
Correction
Text
was
extracted
using
Google’s
gemini-1.5-flash-002
(Team
et
al.,
2024a)
and
structured
into
Q&A
pairs.
Romanian diacritics were automatically re-
stored using a Romanian finetuned model
mt5-base-romanian-diacritics 5 version of
MT5 (Xue et al., 2021), followed by minimal
manual correction.
3.3
Duplicate Removal
Duplicates were identified by calculating cosine
similarity using embeddings generated with
jina-embeddings-v3 (Sturua et al., 2024).
Questions exceeding a similarity threshold of
0.9 were manually reviewed, resulting in the
removal of approximately 10 duplicates.
3.4
Metadata Annotation
Questions were enriched with relevant meta-
data, including:
• Episode Air Date.
• Monetary Value (RON): Used as a
proxy for question difficulty.
• Difficulty Level:
Easy, medium, and
hard (based on monetary value).
• Category: Art and Culture, Cinematog-
raphy, Gastronomy...
• Cultural context: Romanian or Inter-
national. For example if a questions asks
about "Titanic" ->International whereas
if the question is about "Filantropica" ->
then its Romanian.
5https://huggingface.co/iliemihai/
mt5-base-romanian-diacritics
The distribution of questions across diffi-
culty levels (Figure 2) shows the distribution
of questions across difficulty levels
Figure 2:
Distribution of difficulty levels across
Romanian-specific and international cultural con-
texts. Note the limited number of "hard" questions
reflecting contestant dropout at higher quiz levels.
3.5
Cultural Context Categorization
Questions
were
automatically
classified
as
Romanian-specific
or
international
us-
ing
Qwen2.5-72B-Instruct
and
manually
validated, resulting in a 28.4% / 71.6% split.
3.6
Topic Categorization
Figure 3: Distribution of questions across topic
categories.
Questions were automatically assigned to 12
topic domains using Qwen2.5-72B-Instruct,
followed by manual verification and correc-
tion where necessary.
The topic distribu-
tion is summarized in Figure 3, which shows
the number of Romanian-specific and interna-
tional questions across each domain.
4
Methodology
We evaluated the performance of several state-
of-the-art LLMs, specifically chosen to rep-
resent both general multilingual models and

--- Page 4 ---

Romanian-specific adaptations.
The evalu-
ation framework, including model selection,
configurations, prompting strategy, and test-
ing conditions, is detailed below.
4.1
LLM Selection and Configuration
We benchmarked a diverse range of models
(7B-72B parameters) covering various archi-
tectures, capabilities, and Romanian adapta-
tions.
Category
Model
General Multilingual
Llama-3.1-8B-Instruct (Grattafiori and Dubey, 2024a)
Llama-3.3-70B-Instruct (Grattafiori and Dubey, 2024b)
Gemma2-9B-Instruct (Team et al., 2024b)
Mistral-7B-Instruct-v0.1 (Jiang et al., 2023)
Aya-23-8B (Aryabumi et al., 2024)
EuroLLM-9B-Instruct (Martins et al., 2024)
Qwen2.5-72B-Instruct (Qwen et al., 2025)
Phi-4 (Abdin et al., 2024)
Romanian Fine-tuned
RoGemma2-9B-Instruct (Masala et al., 2024)
RoLlama3.1-8B-Instruct (Masala et al., 2024)
RoMistral-7B-Instruct (Masala et al., 2024)
Pansophic-1-preview (Pansophic, 2024)
Table 1: Evaluated LLMs used in the benchmark.
Inference
for
the
largest
models
(Qwen2.5-72B,
Llama-3.3-70B)
utilized
the Hyperbolic API6; others were evaluated
locally (Kaggle, 2x NVIDIA T4 GPUs).
4.2
Experiments
We evaluated model performance across mul-
tiple dimensions to assess capabilities in han-
dling Romanian language and cultural nu-
ances. The experiments were structured along
three main axes:
1. Category-Based Evaluation:
Perfor-
mance was measured separately for each
of the 12 annotated topic categories (e.g.,
Art, History, Science) to identify domain-
specific strengths and weaknesses.
2. Difficulty-Based Evaluation: Models
were assessed across easy, medium, and
hard difficulty levels (derived from game
show monetary value) to evaluate robust-
ness to varying challenge levels.
3. Cultural
Context
Evaluation:
We
performed
separate
evaluations
on
Romanian-specific
versus
international
questions to isolate the impact of cultural
context and identify potential cultural
knowledge gaps.
6https://hyperbolic.xyz
To further investigate cross-lingual and cul-
tural generalization, we also conducted exper-
iments using:
• Comparable
French
and
English
Datasets: To observe if performance pat-
terns generalized across other languages,
including another Romance language.
• Romanian-English Translation:
We
translated the Romanian dataset into En-
glish and re-evaluated models to help
disentangle linguistic understanding chal-
lenges from cultural knowledge factors.
4.3
Prompt Design
To ensure consistent and comparable results
across all models, we standardized the prompt
format.
Each prompt included the question
text followed by four multiple-choice answer
options (a, b, c, d).
Models were explic-
itly instructed to respond only with the let-
ter corresponding to their chosen answer. The
prompt was structured as follows:
Please respond with only the letter
corresponding to the correct answer.
Do not include any additional text,
explanations, or punctuation.
Additionally, a system-level instruction was
included to further guide the model behavior:
You
are
a
master
of
answering
multiple-choice
questions
who
re-
sponds only with the letter corre-
sponding to the correct answer.
Both prompts and system instructions were
translated into Romanian to match the evalu-
ation language of the dataset. All evaluations
were conducted using a zero-shot prompting
strategy.
4.4
Model Inference Configuration
To maintain consistent inference behavior and
minimize randomness, the following parame-
ters were uniformly applied across all model
runs:
• Max Tokens:
1 (restricting output to
one character).
• Temperature: 0 (fully deterministic re-
sponses).

--- Page 5 ---

These settings ensured consistent, concise,
and deterministic outputs, facilitating accu-
rate performance comparisons.
4.5
Evaluation Pipelines
Evaluation procedures differed based on model
access.
API-based models (Qwen2.5-72B,
Llama-3.3-70B) were queried via the Hyper-
bolic API using JSON requests, with built-
in retries for rate limits. Locally executed
models processed structured prompts directly
using Hugging Face Transformers and local
tokenizers.
For both pipelines, failed or in-
complete predictions were consistently marked
with a placeholder (’x’) for standardized error
handling.
4.6
Performance Metrics
Model predictions were systematically com-
pared against ground-truth answers.
Accu-
racy scores were calculated separately for each
testing condition (cultural context, difficulty,
and category), providing insights into models’
relative strengths and limitations, particularly
concerning their understanding of Romanian
language and cultural-specific knowledge.
5
Results and Analysis
We evaluate model performance comprehen-
sively, focusing separately on cultural context,
topic categories, and question difficulty.
5.1
Performance by Cultural Context
Table 2 reveals model accuracy based on cul-
tural context (Romanian-specific vs. interna-
tional).
Model
Romanian
International
Overall
RoGemma2-9B
60.3
91.5
82.8
Gemma2-9B
62.8
89.2
81.8
Llama-3.1-8B
52.3
79.1
71.6
RoLlama3.1-8B
48.7
84.2
74.3
Pansophic-1
50.5
79.8
71.6
Aya-23-8B
46.9
78.1
69.3
Mistral-7B
32.1
59.8
52.0
RoMistral-7B
49.1
84.1
74.3
EuroLLM-9B
70.7
88.2
83.3
Qwen2.5-72B
63.9
94.4
85.9
Llama-3.3-70B
75.8
96.5
90.7
Phi-4
56.3
85.2
77.1
Table 2: Model accuracy (%) by cultural context.
Analysis and Observations:
• Significant Cultural Gap: We investi-
gated whether there is a statistically sig-
nificant difference in model performance
between Romanian-specific and interna-
tional questions.
The null hypothesis states that there is
no difference in mean accuracy between
Romanian-specific and international ques-
tions across models. For each of the 12
models, we computed the mean accuracy
separately on the Romanian-specific and
international subsets, and then performed
a paired t-test on these per-model differ-
ences.
The test rejected the null hypothesis,
showing a statistically significant differ-
ence in performance (t(11) = 18.82, p <
0.001).
This indicates that models per-
form significantly better on international
questions than on Romanian-specific ones,
highlighting the challenge posed by cul-
tural context.
• Top
Model
Performance:
While
Llama-3.3-70B-Instruct
achieves
the
highest overall (90.7%) and international
(96.5%) scores, its accuracy still drops sig-
nificantly on Romanian-specific questions
(75.8%), indicating that large scale does
not fully overcome the need for specific
cultural knowledge.
• Difficulty
Distribution
Paradox:
Crucially,
this performance gap exists
despite
the
Romanian-specific
subset
having proportionally fewer ’Hard’ ques-
tions compared to the international set
(as shown in Figure 2).
This strongly
suggests
that
Romanian-specific
ques-
tions, even those classified as ’Easy’ or
’Medium’ based on game progression,
present an intrinsic challenge likely due
to reliance on specific cultural facts,
historical figures, or linguistic nuances
less represented in models’ training data.
• Fine-tuning Effects:
Romanian fine-
tuning yields mixed results. RoGemma2-9B
and RoMistral-7B improved notably over
their base models, mainly on interna-
tional questions, suggesting better linguis-

--- Page 6 ---

tic adaptation rather than direct cultural
knowledge gains.
• Smaller
Model
Struggles:
Smaller
models like Mistral-7B and Aya-23-8B
struggle significantly, particularly with
Romanian-specific questions, highlighting
the combined difficulty of handling a mid-
resource language and specific cultural
content.
These results underscore the importance of
evaluating LLMs within specific cultural con-
texts. Further experiments exploring the im-
pact of fine-tuning in few-shot settings are de-
tailed in Appendix A.
5.2
Performance by Topic Categories
To understand performance variations across
different knowledge domains,
we analyzed
model accuracy for each of the 12 topic cat-
egories.
Figure 4 presents these results as a
heatmap, offering a visual comparison across
models and topics.
The topic categories on
the x-axis are sorted by descending average ac-
curacy across all models, indicating generally
"easier" topics on the left and "harder" topics
on the right.
Science
Religion
Medicine
Geography
Art
History
Cinema
Sports
Gastronomy
General
Music
Literature
Topic Category (sorted by average model accuracy)
RoGemma2-9B
Gemma2-9B
Llama-3.1-8B
RoLlama3.1-8B
Aya-23-8B
Mistral-7B
RoMistral-7B
EuroLLM-9B
Qwen2.5-72B
Llama-3.3-70B
Model
99
100
96
90
82
76
78
82
88
75
79
74
95
100
93
89
78
82
74
80
82
79
70
74
87
80
89
77
70
77
67
61
73
67
64
58
92
88
85
84
74
73
64
61
75
69
64
70
87
82
74
84
75
67
59
59
78
59
64
53
62
68
59
65
48
51
62
47
32
47
52
38
91
80
93
87
73
69
72
76
70
66
63
68
94
95
96
95
84
85
75
76
89
79
67
73
97
95
96
94
86
82
83
82
77
81
79
78
99
95
96
96
91
92
87
94
93
87
75
77
40
50
60
70
80
90
100
Accuracy (%)
Figure 4: Model accuracies by topic (categories
sorted by average score).
Analysis and Observations:
The heatmap
highlights several key trends:
• Topic Difficulty Gradient: A clear per-
formance gradient exists, with topics like
Science, Religion, and Medicine (left side)
generally yielding higher accuracies than
Literature, Music, and General Culture
(right side).
• Model Scale Matters:
Larger mod-
els (Llama-3.3-70B, Qwen2.5-72B) dis-
play consistently high performance (more
yellow/bright green) across nearly all cat-
egories.
• Specific Model Weaknesses: Smaller
models, particularly Mistral-7B, show
significant weaknesses (darker cells) in
multiple, often lower-performing, cate-
gories.
• Fine-tuning Effects Visually: Roma-
nian fine-tuning shows noticeable bene-
fits for RoMistral-7B compared to its
base. Improvements for RoGemma2-9B ap-
pear more targeted (e.g., Medicine), while
RoLlama3.1-8B shows less consistent vi-
sual improvement over its base.
Overall, the heatmap confirms that perfor-
mance varies significantly by topic, influenced
by model scale and targeted fine-tuning.
5.3
Performance by Difficulty Levels
Table 3 summarizes accuracy based on ques-
tion difficulty.
Model
Easy
Medium
Hard
RoGemma2-9B
84.7
79.2
84.2
Gemma2-9B
84.3
77.9
73.6
Qwen2.5-72B
86.4
82.8
94.7
Llama-3.3-70B
91.4
86.4
89.4
Table 3: Accuracy (%) by question difficulty level.
Observations:
• Llama-3.3-70B and Qwen2.5-72B show
robustness across all difficulty levels.
• Smaller models generally see significant
accuracy drops on medium and hard ques-
tions.
• Romanian-fine-tuned models often out-
perform their base models at higher dif-
ficulties.
5.4
Cross-Language Testing on French
and English Datasets
To investigate whether observed performance
patterns generalize beyond Romanian, we eval-
uated models on comparable French and En-
glish datasets. For each language, we used a

--- Page 7 ---

sample consisting of 35 hard, 165 medium, and
300 easy questions. Table 4 shows the compar-
ative accuracy.
Model
Romanian
French
English
Gemma2-9B
81.4
76.4
88.8
Llama-3.1-8B
71.8
68.8
85.0
Aya-23-8B
73.4
66.0
77.6
Mistral-7B
52.6
47.2
75.6
EuroLLM-9B
74.2
70.6
79.6
Qwen2.5-72B
68.2
83.1
93.6
Llama-3.3-70B
77.0
82.2
94.0
Table 4: Accuracy (%) by language.
A consistent performance hierarchy emerges
across models, with accuracy highest in En-
glish, followed by Romanian, and lowest in
French (Table 4).
This likely reflects the
dominance of English in pre-training data.
The lower French scores compared to Roma-
nian suggest language-specific challenges or
dataset differences beyond language family.
While larger models like Qwen2.5-72B and
Llama-3.3-70B show greater cross-lingual ro-
bustness, consistent performance across lan-
guages remains challenging—highlighting the
need for continued language-specific evaluation
in multilingual NLP.
5.5
Translation-Based Comparison
with English
To isolate the impact of linguistic versus cul-
tural grounding, we translated all Romanian
questions into English and re-evaluated model
performance. By comparing responses to the
original and translated versions, we analyzed
whether discrepancies arose from limitations
in Romanian language understanding or from
gaps in cultural knowledge.
This experiment revealed that translation
did not help and, in fact, led to slightly worse
performance, highlighting the importance of
native-language benchmarks for fair and accu-
rate evaluation.
5.6
Illustrative Examples of
Culturally-Specific Questions
To illustrate the nature of the challenges posed
by the Romanian-specific subset (discussed in
Section 5.1), here are selected examples requir-
ing localized knowledge. English translations
are provided.
Original
Translated
Dataset version
Gemma2-9B
EuroLLM-9B
Qwen2.5-72B
Llama-3.3-70B
Model
81.8
80.2
83.3
76.3
85.9
83.3
90.7
85.0
40
60
80
100
Accuracy (%)
Figure 5: Comparison between original and trans-
lated Romanian dataset.
• Historical Context (Index 896): RO:
În afară de Marea Unire, domnia lui Ferdi-
nand I a fost marcată s,i de: (EN: Besides
the Great Union, the reign of Ferdinand I
was marked by:) Answer: Primul Război
Mondial / World War I. Model prediction:
loss of Bucovina. Commentary: The En-
glish translation misses the Romanian his-
torical context, where Ferdinand’s reign is
more closely associated with WWI than
the loss of Bucovina.
• Geographical
Knowledge
(Index
958): RO: Ce munt,i trebuie să urci ca să
vizitezi Babele?
(EN: What mountains
must you climb to visit Babele?) Answer:
Bucegi.
Model prediction:
Făgăras,.
Commentary:
The English translation
doesn’t account for the specific location of
Babele in the Bucegi Mountains, leading
to the incorrect prediction of Făgăras,.
• Idiomatic Expression (Index 918):
RO: O expresie veche românească spune
că omul care speră lucruri irealizabile
visează:
(EN: An old Romanian ex-
pression says that the man who hopes
for unachievable things dreams:)
An-
swer: cai verzi pe peret,i / green horses
on walls.
Model prediction:
green and
dried.
Commentary:
A literal transla-
tion misses the idiomatic meaning, which
is culturally rooted and nonsensical with-
out Romanian-specific knowledge.
These questions exemplify how the dataset
probes knowledge beyond internationally com-

--- Page 8 ---

mon facts, demanding culturally embedded
understanding.
6
Conclusions
We introduced WWTBM, a novel, culturally-
rich multilingual dataset derived from "Who
Wants to Be a Millionaire?" videos, designed
for evaluating LLMs on Romanian cultural nu-
ances. Our benchmarking revealed several key
insights into model performance at the inter-
section of language and culture.
A significant performance gap consis-
tently appears between international (high
accuracy)
and
Romanian-specific
ques-
tions
(lower
accuracy)
across
all
tested
models,
including
large-scale
ones
like
Llama-3.3-70B-Instruct.
This highlights
that
current
pre-training
does
not
fully
capture deep cultural knowledge.
Further-
more, Romanian-specific fine-tuning showed
mixed effects, sometimes improving linguistic
adaptation
more
than
cultural
knowledge
retrieval.
Cross-lingual tests confirmed performance
variations across languages (English > Roma-
nian > French). Notably, translating Roma-
nian questions to English decreased accu-
racy compared to the original, underscoring
the value and potential subtleties of native-
language benchmarks.
Overall,
our findings stress the critical
need for culturally-grounded datasets like
WWTBM for robust LLM evaluation. Devel-
oping models adept across diverse cultural con-
texts remains challenging but crucial, particu-
larly for building effective and equitable educa-
tional NLP applications. WWTBM provides a
valuable resource for advancing this research.
7
Ethical Considerations
The dataset used in this research was obtained
solely from publicly available video recordings
of the Romanian edition of Who Wants to Be
a Millionaire?, accessible on platforms such as
YouTube. No private or restricted content was
involved.
The dataset is released as an open-source re-
source to support multilingual and culturally-
aware NLP research.
No personally identifi-
able information (PII) of participants or audi-
ence members was collected, included, or dis-
tributed. The research team ensured that all
content is educationally relevant and intended
strictly for research and development purposes.
We recognize the importance of ongoing eth-
ical oversight and remain committed to ad-
dressing any concerns raised by content owners
or stakeholders. Future users are encouraged
to uphold these standards and use the dataset
responsibly and in accordance with applicable
copyright.
8
Limitations
While
this
study
provides
valuable
in-
sights into multilingual LLM performance in
Romanian-specific and international contexts,
several limitations must be acknowledged.
First, the dataset is relatively small, with
around 1,000 questions collected from available
recordings of the Romanian edition of Who
Wants to Be a Millionaire?. Despite careful
curation, this limited size may affect the sta-
tistical robustness of evaluations, particularly
for difficult questions and less common topics.
Moreover, the dataset reflects the knowledge
areas, difficulty distribution, and cultural bi-
ases of the quiz show format, which may not
fully represent broader Romanian culture or
general knowledge domains.
Second, the use of automated tools—such as
multimodal OCR and LLM-based categoriza-
tion—may introduce annotation errors, even
with subsequent manual correction.
While
manual validation helped reduce inconsisten-
cies, some residual inaccuracies may have in-
fluenced results.
Third,
our
evaluation
was
limited
to
multiple-choice questions with minimal con-
text, which may oversimplify real-world lan-
guage understanding. Results could differ in
tasks involving open-ended answers, reasoning,
or richer context.
Lastly, the study focused on open-source
LLMs.
Evaluations including proprietary or
domain-specialized models might produce dif-
ferent outcomes.
Future work should expand the dataset in
size and diversity, include varied question for-
mats, and explore tasks requiring deeper rea-
soning and contextual understanding to bet-
ter guide Romanian-language and educational
NLP development.

--- Page 9 ---

References
Marah
Abdin,
Jyoti
Aneja,
Harkirat
Behl,
Sébastien Bubeck, Ronen Eldan, Suriya Gu-
nasekar, Michael Harrison, Russell J. Hewett,
Mojan Javaheripi, Piero Kauffmann, James R.
Lee, Yin Tat Lee, Yuanzhi Li, Weishung Liu,
Caio C. T. Mendes, Anh Nguyen, Eric Price,
Gustavo de Rosa, Olli Saarikivi, and 8 oth-
ers. 2024.
Phi-4 technical report.
Preprint,
arXiv:2412.08905.
Viraat Aryabumi, John Dang, Dwarak Talupuru,
Saurabh Dash,
David Cairuz,
Hangyu Lin,
Bharat Venkitesh, Madeline Smith, Jon Ander
Campos, Yi Chern Tan, Kelly Marchisio, Max
Bartolo, Sebastian Ruder, Acyr Locatelli, Julia
Kreutzer, Nick Frosst, Aidan Gomez, Phil Blun-
som, Marzieh Fadaee, and 2 others. 2024. Aya
23: Open weight releases to further multilingual
progress. Preprint, arXiv:2405.15032.
Aakanksha Chowdhery, Sharan Narang, Jacob De-
vlin, Maarten Bosma, Gaurav Mishra, Adam
Roberts, Paul Barham, Hyung Won Chung,
Charles Sutton, Sebastian Gehrmann, and 1
others. 2022. Palm: Scaling language modeling
with pathways. ArXiv.
Jwala Dhamala, Yonatan Belinkov, and 1 others.
2021.
Bold: Dataset and metrics for measur-
ing biases in open-ended language generation.
ArXiv.
Stefan Daniel Dumitrescu, Andrei M Avram, and
Andrei M Butnaru. 2020. The birth of romanian
bert. In ACL.
Aaron
Grattafiori
and
Abhimanyu
Dubey.
2024a.
The
llama
3
herd
of
models.
Preprint, arXiv:2407.21783.
Retrieved from
https://huggingface.co/meta-llama/
Llama-3.1-8B-Instruct. This model is an
instruct-tuned version of LLaMA 3.1 8B by
Meta AI.
Aaron
Grattafiori
and
Abhimanyu
Dubey.
2024b.
The
llama
3
herd
of
models.
Preprint, arXiv:2407.21783.
Retrieved from
https://huggingface.co/meta-llama/
Llama-3.3-70B-Instruct. This model is an
instruct-tuned version of LLaMA 3.3 70B by
Meta AI.
Junjie Hu, Sebastian Ruder, Aditya Siddhant, and
1 others. 2020. Xtreme: A massively multilin-
gual multi-task benchmark for evaluating cross-
lingual generalization. In ICML.
Albert Q. Jiang, Alexandre Sablayrolles, Arthur
Mensch, Chris Bamford, Devendra Singh Chap-
lot,
Diego de las Casas,
Florian Bressand,
Gianna Lengyel,
Guillaume Lample,
Lucile
Saulnier,
Lélio Renard Lavaud,
Marie-Anne
Lachaux, Pierre Stock, Teven Le Scao, Thibaut
Lavril, Thomas Wang, Timothée Lacroix, and
William El Sayed. 2023. Mistral 7b. Preprint,
arXiv:2310.06825.
Yichao Liang, Nan Duan, Ming Gong, and 1 oth-
ers. 2020.
Xglue: A new benchmark dataset
for cross-lingual pre-training, understanding and
generation. In ACL.
Yinhan Liu, Myle Ott, Naman Goyal, Jingfei
Du, Mandar Joshi, Danqi Chen, Omer Levy,
Mike Lewis, Luke Zettlemoyer, and Veselin Stoy-
anov. 2019.
Roberta:
A robustly optimized
bert pretraining approach.
In arXiv preprint
arXiv:1907.11692.
Manuel Mager, Pedro Ortiz Suárez, and 1 others.
2021. Findings of the americasnlp 2021 shared
task on open machine translation for indigenous
languages of the americas. In ACL.
Pedro
Henrique
Martins,
Patrick
Fernandes,
João Alves, Nuno M. Guerreiro, Ricardo Rei,
Duarte M. Alves, José Pombal, Amin Farajian,
Manuel Faysse, Mateusz Klimaszewski, Pierre
Colombo, Barry Haddow, José G. C. de Souza,
Alexandra Birch, and André F. T. Martins.
2024.
Eurollm: Multilingual language models
for europe. Preprint, arXiv:2409.16235.
Mihai Masala, Denis C. Ilie-Ablachim, Dragos Cor-
latescu, Miruna Zavelca, Marius Leordeanu, Ho-
ria Velicu, Marius Popescu, Mihai Dascalu, and
Traian Rebedea. 2024. Openllm-ro – technical
report on open-source romanian llms. Preprint,
arXiv:2405.07703. Models available at https:
//huggingface.co/OpenLLM-Ro.
Nikita Nangia, Alex Wang, and Samuel R Bow-
man. 2021. Winomt: Gender bias in machine
translation revisited. In ArXiv.
Wilhelmina Nekoto, Vukosi Marivate, and 1 others.
2020. Participatory research for low-resourced
machine translation: A case study in african lan-
guages. In ACL.
OpenAI. 2023. Gpt-4 technical report. ArXiv.
Pansophic. 2024.
Pansophic-1-preview.
Model
available
at
https://huggingface.co/
pansophic/pansophic-1-preview-LLaMA3.
1-8b.
Qwen, :, An Yang, Baosong Yang, Beichen Zhang,
Binyuan Hui, Bo Zheng, Bowen Yu, Chengyuan
Li, Dayiheng Liu, Fei Huang, Haoran Wei, Huan
Lin, Jian Yang, Jianhong Tu, Jianwei Zhang,
Jianxin Yang, Jiaxi Yang, Jingren Zhou, and
25 others. 2025.
Qwen2.5 technical report.
Preprint, arXiv:2412.15115.
Victor Sanh, Lysandre Debut, Julien Chaumond,
and Thomas Wolf. 2019. Distilbert, a distilled
version of bert:
smaller, faster, cheaper and
lighter. ArXiv, abs/1910.01108.

--- Page 10 ---

Saba Sturua, Isabelle Mohr, Mohammad Kalim
Akram, Michael Günther, Bo Wang, Markus
Krimmel,
Feng Wang,
Georgios Mastrapas,
Andreas Koukounas,
Nan Wang,
and Han
Xiao. 2024.
jina-embeddings-v3:
Multilin-
gual embeddings with task lora.
Preprint,
arXiv:2409.10173.
Gemini Team, Petko Georgiev, Ving Ian Lei,
Ryan Burnell, Libin Bai, Anmol Gulati, Gar-
rett Tanzer, Damien Vincent, Zhufeng Pan,
Shibo Wang, Soroosh Mariooryad, Yifan Ding,
Xinyang Geng, Fred Alcober, and Roy Frostig...
2024a. Gemini 1.5: Unlocking multimodal un-
derstanding across millions of tokens of context.
Preprint, arXiv:2403.05530.
Gemma Team, Morgane Riviere, Shreya Pathak,
Pier Giuseppe Sessa, Cassidy Hardin, Surya
Bhupatiraju, and Léonard Hussenot... 2024b.
Gemma 2: Improving open language models at
a practical size. Preprint, arXiv:2408.00118.
Hugo Touvron, Thibaut Lavril, Gautier Izacard,
Xavier Martinet, Marie-Anne Lachaux, Timo-
thée Lacroix, Baptiste Rozière, Naman Goyal,
Eric Hambro, Faisal Azhar, and 1 others. 2023.
Llama: Open and efficient foundation language
models. ArXiv.
Dan Tufiş, Elena Irimia, and 1 others. 2017. The
corola corpus of contemporary romanian lan-
guage. ACL.
Yizhong Wang, Daniel Khashabi, Swaroop Mishra,
and 1 others. 2022. Super-naturalinstructions:
Generalization via declarative instructions on
1600+ nlp tasks. ACL.
Linting Xue,
Noah Constant,
Adam Roberts,
Mihir Kale, Rami Al-Rfou, Aditya Siddhant,
Aditya Barua, and Colin Raffel. 2021.
mt5:
A massively multilingual pre-trained text-to-
text transformer.
Preprint, arXiv:2010.11934.
This is a Romanian fine-tune of the original
paper, available at https://huggingface.co/
iliemihai/mt5-base-romanian-diacritics.
A
Few-Shot Learning Results
To further investigate the impact of Romanian
fine-tuning and provide additional context be-
yond the zero-shot evaluations presented in
the main paper, we conducted experiments us-
ing few-shot prompting. We evaluated model
performance by providing 1, 3, or 5 examples
(shots) from the training portion of our dataset
within the prompt before presenting the actual
test question. The examples were randomly se-
lected for each query.
Table 5 presents the accuracy scores for
various base models and their correspond-
ing
Romanian
fine-tuned
variants
across
0,
1,
3,
and
5-shot
settings.
Due
to
space constraints, model names are abbre-
viated (e.g., RLa2=RoLlama2, M3.1=Llama-
3.1, RGe2=RoGemma2, DPO dates omitted
where ambiguous).
Model Abbrev.
FS=0 FS=1 FS=3 FS=5
(%)
(%)
(%)
(%)
Llama-2-7b
29.7
48.2
52.5
52.1
RLa2-7b-Base
25.0
35.0
46.4
50.7
Llama-2-7b-Chat
48.3
52.4
56.4
55.7
RLa2-7b-Ins (Oct24)
68.6
72.6
75.5
74.0
RLa2-7b-Ins (Apr25)
63.7
73.2
75.3
74.0
RLa2-7b-DPO (Oct24)
59.7
69.2
74.4
72.8
RLa2-7b-DPO (Apr25)
71.7
71.6
73.4
73.2
Mistral-7B-Ins-v0.3
67.0
67.3
69.7
69.6
RMi-7b-Ins (Oct24)
68.7
71.7
75.6
76.1
RMi-7b-Ins (Apr25)
73.5
74.1
74.5
76.1
RMi-7b-DPO (Oct24)
48.5
70.8
73.2
74.0
RMi-7b-DPO (Apr25)
73.6
73.1
73.9
74.4
Llama-3-8B-Ins
67.9
71.5
71.3
71.6
RLa3-8b-Ins (Oct24)
72.8
75.3
75.9
75.8
RLa3-8b-Ins (Apr25)
74.3
75.6
77.4
76.1
RLa3-8b-DPO (Oct24)
73.8
75.3
75.3
75.9
RLa3-8b-DPO (Apr25)
76.5
75.6
76.8
77.1
Llama-3.1-8B-Ins
70.1
71.2
72.1
72.8
RLa3.1-8b-Ins (Oct24)
72.6
74.6
76.0
77.5
RLa3.1-8b-Ins (Apr25)
73.1
75.1
76.7
76.6
RLa3.1-8b-DPO (Oct24)
74.1
74.0
74.9
76.6
RLa3.1-8b-DPO (Apr25)
76.1
74.8
74.5
75.2
Gemma-1.1-7b-IT
65.1
61.9
61.1
60.4
RGe-7b-Ins (Oct24)
71.7
74.4
75.5
76.2
RGe-7b-Ins (Apr25)
70.6
76.1
76.0
76.6
RGe-7b-DPO (Oct24)
70.6
74.2
75.1
75.8
Gemma-2-9b-IT
79.6
81.1
81.9
82.5
RGe2-9b-Ins (Oct24)
78.4
80.9
82.3
81.1
RGe2-9b-Ins (Apr25)
75.8
74.9
79.3
79.5
RGe2-9b-DPO (Oct24)
79.5
80.5
82.2
81.1
RGe2-9b-DPO (Apr25)
81.4
78.9
80.5
80.4
Table 5:
Few-Shot (FS) Accuracy Comparison:
Base Models vs. Romanian Fine-tuned Variants.
Model names abbreviated for space.
Brief Observations:
These few-shot results
generally confirm the zero-shot trends.
Ro-
manian fine-tuned models often maintain or
slightly increase their advantage over base
models with 1-5 examples. Performance tends
to saturate or slightly decrease between 3 and
5 shots. DPO variants are competitive, some-
times outperforming Instruct versions, espe-
cially at 0/1 shot. Base Gemma models show
less benefit from few-shot examples here.
A
detailed analysis is future work.

```
