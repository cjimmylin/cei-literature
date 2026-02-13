---
title: "2025-Erdem-Cetvel A Unified Benchmark for Evaluating - PDF Extract"
source_pdf: "2025-Erdem-Cetvel A Unified Benchmark for Evaluating.pdf"
pages: 31
extracted_at: "2026-02-13T09:15:44.098316"
---

# PDF Extract: 2025-Erdem-Cetvel A Unified Benchmark for Evaluating

**Source PDF:** 2025-Erdem-Cetvel A Unified Benchmark for Evaluating.pdf
**Total Pages:** 31

---

## Content

```
--- Page 1 ---

CETVEL: A Unified Benchmark for Evaluating Language
Understanding, Generation and Cultural Capacity of LLMs for Turkish
Abrek Er1* Ilker Kesen3* Gözde Gül ¸Sahin1,2 Aykut Erdem1,2
1 KUIS AI Center
2 Department of Computer Engineering, Koç University
3Department of Computer Science, University of Copenhagen
*Equal Contribution aber@ku.edu.tr
Abstract
We introduce CETVEL, a comprehensive bench-
mark designed to evaluate large language mod-
els (LLMs) in Turkish. Existing Turkish bench-
marks often lack either task diversity or cul-
turally relevant content, or both. CETVEL ad-
dresses these gaps by combining a broad
range of both discriminative and generative
tasks ensuring content that reflects the linguis-
tic and cultural richness of Turkish language.
CETVEL covers 23 tasks grouped into seven
categories, including tasks such as grammatical
error correction, machine translation, and ques-
tion answering rooted in Turkish history and id-
iomatic language. We evaluate 33 open-weight
LLMs (up to 70B parameters) covering differ-
ent model families and instruction paradigms.
Our experiments reveal that Turkish-centric
instruction-tuned models generally underper-
form relative to multilingual or general-purpose
models (e.g. Llama 3 and Mistral), despite
being tailored for the language.
Moreover,
we show that tasks such as grammatical error
correction and extractive question answering
are particularly discriminative in differentiat-
ing model capabilities. CETVEL offers a com-
prehensive and culturally grounded evaluation
suite for advancing the development and assess-
ment of LLMs in Turkish.
1
Introduction
Large language models (LLMs) have recently
achieved remarkable performance on widely used
English-centric benchmarks such as (Super)GLUE
(Wang et al., 2018, 2019) and MMLU (Hendrycks
et al., 2021). Their success across a broad spectrum
of tasks and domains (Jiang et al., 2023; Touvron
et al., 2023; Yang et al., 2024) has spurred the
development of evaluation suites in languages be-
yond English (Park et al., 2021; Elmadany et al.,
2023; Nielsen, 2023). In this work, we extend these
efforts to Turkish by introducing CETVEL1 , a com-
1CETVEL means ruler in Turkish, i.e. a rectangular shaped
object used for measuring the distance between two points.
prehensive benchmark designed to evaluate LLMs
across a diverse set of natural language processing
(NLP) tasks, with a particular emphasis on cultural
and linguistic relevance to Turkish.
Existing Turkish NLP benchmarks typically suf-
fer from one or both of the following limitations:
insufficient task diversity and a lack of culturally
relevant content. CETVEL addresses both short-
comings. First, it provides broad task coverage,
extending well beyond the multiple-choice ques-
tion answering (MCQA) format predominant in
recent Turkish benchmarks (Yüksel et al., 2024;
Bayram et al., 2024; Alhajar, 2024). Specifically,
CETVEL includes 23 tasks grouped into seven cate-
gories: Text Classification (TC), Multiple Choice
Question Answering (MCQA), Extractive Question
Answering (QA), Grammatical Correction (GC),
Machine Translation (MT), Summarization (SUM),
and Natural Language Inference (NLI).
Second, CETVEL prioritizes content deeply
rooted in Turkish language and culture, an aspect
often missing in multilingual or machine-translated
benchmarks, which tend to reflect Western cultural
biases (Singh et al., 2024; Acikgoz et al., 2024).
To counter this, CETVEL includes tasks based on
grammatical error correction, figurative language
processing, and extractive QA centered on Turk-
ish and Islamic history. We also introduce a novel
circumflex-based word sense disambiguation task2,
further enriching the benchmark’s linguistic speci-
ficity.
We evaluate 33 open-weight LLMs on CETVEL,
spanning a broad range of parameter scales (1B to
70B) and model families (e.g., Llama 3, Qwen2.5),
including both general-purpose/multilingual and
Turkish-specific models. Among all models, Llama
3 variants consistently deliver the strongest over-
all performance within their respective size cat-
egories. However, more importantly, our results
2In Turkish, hala means aunt, whereas hâlâ means still.
1
arXiv:2508.16431v1  [cs.CL]  22 Aug 2025

--- Page 2 ---

Generation
(45.7%)
Understanding
(54.3%)
XQuAD
TQuAD
MKQA
Exams
Belebele
TurkishPLU
XCOPA
TurkishMMLU
Proverbs
Riddles
CircumﬂexTR
IronyTR
NewsCat
OﬀensEval
STSb
XNLI
MNLI
SNLI
Extractive QA
Multiple Choice
Text Classiﬁcation
NLI
MLSum
XLSum
WikiLingua
WMT-16
GECTurk
Summarization
Translation
Grammatical Error Correction
Figure 1: Task taxonomy in the CETVEL benchmark. The leftmost pie chart illustrates the overall distribution of
tasks across two primary categories: language understanding and language generation. The middle chart details
the subtypes within the understanding category, including extractive question answering, multiple-choice QA, text
classification, and natural language inference, along with their associated datasets. The rightmost chart breaks down
the generation tasks into three subtypes: summarization, machine translation, and grammatical error correction.
show that most instruction-tuned LLMs specifically
developed for Turkish do not outperform general-
purpose models such as Llama 3 variants and Mis-
tral.
Our findings suggest that Turkish-centric
LLMs can benefit from improved instruction-
tuning, continued pretraining, and more rigorous
validation strategies. Nonetheless, we find that
there exists some exceptions: Cere-Llama-3-8B
achieves the best performance on grammatical er-
ror correction and extractive question answering
about Turkish and Islamic history, even outmatch-
ing the 70 billion parameter model Llama-3.3-70B-
Instruct.
Additionally, to better understand task-level vari-
ability, we assess the informativeness of each task
using Gini coefficient-based analysis. Our findings
indicate that grammatical error correction, machine
translation, and extractive QA are particularly ef-
fective in differentiating model capabilities, posi-
tioning these tasks as highly valuable resources for
benchmarking LLMs in Turkish.
Our contributions are as follows:
• We present CETVEL3, a new Turkish LLM
benchmark that combines broad task diversity
with high linguistic and cultural relevance.
• We evaluate 33 open-weight LLMs spanning
multiple families, language specializations,
and parameter scales (up to 70B).
• Our results reveal that most Turkish-centric
models do not outperform general-purpose
3Code and data:
KUIS-AI/cetvel
LLMs such as Llama 3 and Mistral at compa-
rable scales.
• We exceptionally find that Cere-Llama-3-8B
excels among all other Turkish-centric LLMs,
even surpassing a 70 billion parameter model
on grammatical error correction and extractive
QA about Turkish and Islam history.
• We identify grammatical correction, machine
translation, and extractive QA as the most in-
formative tasks for evaluating Turkish LLMs.
2
Related Work
2.1
LLM Benchmarks
Early benchmark suites such as GLUE (Wang
et al., 2018) and SuperGLUE (Wang et al., 2019)
have been pivotal in evaluating English-centric lan-
guage understanding for smaller-scale models like
BERT (Devlin et al., 2019) and RoBERTa (Liu
et al., 2019). As LLMs have evolved (LLaMA-
Team, 2024; Yang et al., 2024), more challeng-
ing benchmarks have emerged, targeting skills
such as commonsense reasoning (Bisk et al.,
2020), mathematical problem-solving (Cobbe et al.,
2021), coding proficiency (Liu et al., 2023, 2024b),
and domain-specific knowledge (e.g., scientific
QA) (Hendrycks et al., 2020; Rein et al., 2024).
Instruction-tuned models are further assessed
through alignment and safety benchmarks (Bai
et al., 2024). Inspired by GLUE and SuperGLUE,
CETVEL brings a similar unification of tasks and
datasets but with a specific focus on evaluating
LLMs in Turkish.
2

--- Page 3 ---

2.2
Multilingual Benchmarks
Multilingual benchmarks such as XTREME (Hu
et al., 2020), XTREME-R (Ruder et al., 2021),
and XGLUE (Liang et al., 2020) include Turk-
ish among other languages, covering a variety of
tasks like question answering (QA), natural lan-
guage inference (NLI), machine translation (MT),
and named entity recognition (NER). However,
these benchmarks typically provide only one or
two datasets per task, limiting their comprehen-
siveness. The MEGA benchmark (Ahuja et al.,
2023) extends multilingual evaluation by focusing
on generative LLMs, featuring 16 datasets, includ-
ing XQuAD (Artetxe et al., 2019), MLQA (Lewis
et al., 2019), XLSum (Hasan et al., 2021a), and
WikiANN (Rahimi et al., 2019), across 70 lan-
guages and multiple evaluation settings (mono-
lingual, translated, zero-shot cross-lingual). De-
spite this breadth, MEGA reports significant per-
formance gaps between Turkish and English, as
well as among other non-English languages. Re-
cent efforts such as M2QA (Engländer et al., 2024)
and SeaEval (Wang et al., 2023) show that LLM
performance can vary significantly by domain
and language. Additionally, large-scale multilin-
gual classification benchmarks have been devel-
oped (Ma et al., 2025; Adelani et al., 2024). No-
tably, TUMLU (Isbarov et al., 2025) evaluates
LLMs across eight Turkic languages and 11 school-
subject domains, offering a culturally aware assess-
ment framework for Turkic language models.
2.3
Benchmarks tailored for Turkish
Several benchmarks have been designed specifi-
cally for Turkish NLP. Mukayese (Safaya et al.,
2022) includes seven tasks, primarily targeting the
evaluation of pre-LLM-era multilingual models us-
ing fine-tuning. Benchmarks such as Acikgoz et al.
(2024) and Alhajar (2024) are built from machine-
translated datasets, including ARC (Clark et al.,
2018), TruthfulQA (Lin et al., 2022), and GSM8K
(Cobbe et al., 2021). TurkishMMLU (Yüksel et al.,
2024), a localized version of MMLU, provides
10K high-school-level questions spanning nine sub-
jects with zero-shot and few-shot evaluations. TR-
MMLU (Bayram et al., 2024) expands this further
with 6,200 questions across 62 categories, includ-
ing law and healthcare.
CETVEL advances beyond these resources in
three key ways:
(i) it covers a broader set of 23 tasks that in-
clude both discriminative and generative set-
tings, unlike MCQA-heavy benchmarks such
as TurkishMMLU, TR-MMLU, and TUMLU;
(ii) it includes tasks explicitly designed around
Turkish linguistic and cultural content, a criti-
cal shortcoming of machine-translated bench-
marks;
(iii) it is more comprehensive and up-to-date than
Mukayese, supporting zero-shot evaluation of
modern LLMs.
3
Tasks and Datasets
CETVEL includes a diverse set of tasks designed to
comprehensively evaluate large language models
in Turkish. These tasks are grouped into two high-
level categories: natural language understanding
(NLU) and natural language generation (NLG). In
total, CETVEL spans 23 tasks drawn from publicly
available benchmarks and curated datasets, with
particular emphasis on linguistic and cultural rel-
evance. Figure 1 provides a visual breakdown of
task categories and subtypes.
3.1
Language Understanding Tasks
We organize NLU tasks into four subcategories: (i)
extractive question answering (QA), (ii) multiple-
choice question answering (MCQA), (iii) text clas-
sification (TC), and (iv) natural language inference
(NLI).
Extractive Question Answering
In extractive QA, the model is presented with a
question and a contextual passage that contains
the answer. The objective is to extract the correct
answer span from the context. CETVEL includes
the following resources: XQuAD (Artetxe et al.,
2020) (Artetxe et al., 2020) extends the English
SQuAD dataset (Rajpurkar et al., 2016) with crowd-
sourced translations into 11 languages, including
Turkish. MKQA (Longpre et al., 2021) offers 10K
aligned question–answer pairs across 26 languages.
It lacks contextual passages, we retain this original
format. TQuAD contains context-based questions
on Turkish and Islamic history, making it uniquely
suited for culturally grounded QA in Turkish4.
Multiple Choice Question Answering
The multiple-choice question answering (MCQA)
is well-suited for zero-shot evaluation, and hence
it serves as the main format in many recent NLP
4
TQuad/turkish-nlp-qa-dataset
3

--- Page 4 ---

benchmarks. In CETVEL, we include datasets span-
ning three subdomains:
(i) Exam-style Assessments: Exams (Hardalov
et al., 2020) features 393 questions drawn
from Turkish high-school subjects such as
mathematics and religion. TurkishMMLU
(Yüksel et al., 2024) is an adaptation of
MMLU offering 900 questions across a wide
range of academic domains. Belebele (Ban-
darkar et al., 2024) includes 900 reading com-
prehension questions, translated by profes-
sionals into 122 languages, including Turkish.
(ii) Procedural and Commonsense Reasoning:
Turkish-PLU (Uzunoglu and ¸Sahin, 2023)
contains four tasks adapted from WikiHow, in-
cluding goal inference, next-event prediction,
step inference, and step ordering. XCOPA
(Ponti et al., 2020) is a multilingual bench-
mark requiring causal reasoning, in which
models must infer either a cause or an effect
given a premise.
(iii) Specific to Turkish: Turkish Proverbs5 com-
prises 1,730 Turkish proverbs paired with def-
initions from official linguistic resources. Dis-
tractors are generated using Llama3.3-70B
embeddings. BilmeceBench6 has 442 riddles
converted into MCQA format with random-
ized distractors. CircumflexTR is curated
specifically for CETVEL, and targets minimal
pairs distinguished by the circumflex diacritic
(e.g., kar “snow” vs. kâr “interest”).
Text Classification
We frame text classification tasks as MCQA by
presenting labels as choices. The task involves
selecting the most appropriate label for a given in-
put. We include the following five datasets: Offen-
sEval (Çöltekin, 2020) for hate speech detection,
performed on user-generated social media data.
IronyTR (Ozturk et al., 2021) for detecting irony
within sentences. STSb-TR, a machine-translated
variant of the STS benchmark, for predicting se-
mantic similarity between two given languages.
Natural Language Inference
Natural language inference (NLI) involves predict-
ing the logical relationship (entailment, contradic-
tion, or neutrality) between a premise and a hy-
pothesis. Similar to the text classification tasks,
we treat the NLI task as a multiple-choice question
5
datasets/furkanunluturk/turkce-atasozleri
6
datasets/selimc/bilmecebench
answering task where we use Turkish versions of
the widely adopted XNLI (Conneau et al., 2018),
SNLI (Bowman et al., 2015), and MNLI (Budur
et al., 2020) datasets.
3.2
Language Generation Tasks
We include three generation tasks: summarization,
machine translation, and grammatical error correc-
tion.
Summarization
The goal is to generate a concise summary from a
paragraph-length input. We evaluate models on the
Turkish portions of MLSum (Scialom et al., 2020)
(news summaries), XLSum (Hasan et al., 2021b)
(single-sentence summaries from BBC articles),
and WikiLingua (Ladhak et al., 2020) (step-by-
step instructional summaries from WikiHow).
Machine Translation
We also evaluate English-to-Turkish translation us-
ing WMT-16 (Bojar et al., 2016). This task mea-
sures cross-lingual language processing and Turk-
ish generation quality.
Grammatical Error Correction
This task involves correcting grammatical mistakes
in Turkish sentences. We use GECTurk (Kara
et al., 2023), which contains 22k sentence pairs syn-
thetically generated using 25 expert-defined gram-
mar rules.
4
Experimental Setup
This section outlines the models evaluated in
CETVEL, the metrics used for assessment, and im-
plementation details of our experimental pipeline.
4.1
Models
We evaluate 33 open-weight models collected from
the Huggingface Transformers package (Wolf et al.,
2020). Models are grouped into three main cate-
gories based on language coverage and pretraining
objectives:
General-purpose LLMs
These models are primarily pretrained on English
but might include additional language data during
pretraining. For this category of models, we cover
Mistral (Jiang et al., 2023), Mixtral (Jiang et al.,
2024) and Llama 3 (LLaMA-Team, 2024).
4

--- Page 5 ---

QA
MC
TC
NLI
SUM
MT
GEC
Avg.
Llama-3.3-70B-Instruct
16.1
60.1
58.1
32.4
16.2
13.6
44.1
34.4
Aya-Expanse-32B
26.2
55.6
55.3
43.3
22.4
20.1
4.5
32.5
Aya-23-35B
23.7
48.8
38.0
37.6
17.6
18.5
30.8
30.7
Llama-3.1-8B
19.3
45.8
44.8
32.2
13.5
15.6
35.3
29.5
Llama-3.1-8B-Instruct
18.0
50.1
40.1
36.0
13.5
15.6
31.5
29.3
Qwen2.5-7B
20.5
50.6
51.6
34.0
12.8
5.5
22.3
28.2
Llama-3-8B
20.9
43.0
40.6
33.9
12.3
11.3
34.1
28.0
Cere-Llama-3-8B
24.2
44.8
43.7
34.0
3.5
0.1
46.0
28.0
Ministral-2410-8B-Instruct
14.2
42.8
38.0
34.0
12.8
11.2
39.1
27.5
Qwen2.5-14B
26.7
52.6
37.7
34.0
13.0
8.1
18.9
27.3
Table 1: Performances of the top-10 models. Bold-face indicates best performances. Shapes next to model
ids denote the model type: Base pretrained models are represented by circles and instruction-tuned LLMs are
denoted by squares. Colors indicate the language focus: blue for English-centric, yellow for multilingually-
pretrained, and red for Turkish-centric LLMs. QA denotes extractive QA, MC denotes multiple-choice QA, TC
denotes text classification, NLI denotes natural language inference, SUM denotes summarization, MT denotes
machine translation, and GEC denotes grammatical error correction. Llama-3.3-70B-Instruct achieves the best
overall performance, followed by Aya-Expanse-32B. Among Turkish-centric LLMs, Cere-Llama-3-8B achieves an
exceptional performance, even surpassing Llama-3.3-70B-Instruct on GEC and extractive QA about Turkish history.
Multilingual LLMs
These models are pretrained to support a wide
range of languages. We include Aya-101 (Üstün
et al., 2024), Aya-23 (Aryabumi et al., 2024),
Aya-Expanse (Dang et al., 2024), Llama 3.1,
Llama 3.2, Llama 3.3 (LLaMA-Team, 2024), and
Qwen2.5 (Yang et al., 2024) models.
Turkish-centric LLMs
These models are either pretrained exclusively on
Turkish or further finetuned on Turkish data. We
include Kanarya (Safaya et al., 2022), Turna (Ulu-
do˘gan et al., 2024), Commencis-LLM-7B (Com-
mencis, 2024), Trendyol-LLM-7B (Trendyol,
2024), and Cere-Llama-3-8B (CerebrumTech,
2024). Kanarya and Turna models are pretrained
on solely Turkish.
The remaining three mod-
els, Commencis-LLM-7B, Trendyol-LLM-7B and
Cere-Llama-3-8B are finetuned on Turkish instruc-
tion following data by Turkish tech companies.
Specifically, Commencis-LLM-7B and Trendyol-
LLM-7B use Mistral-7B as base model, and Cere-
Llama-3-8B is built upon Llama3-8B model.
We further categorize models by their architec-
ture (decoder-only vs. encoder-decoder), training
paradigm (pretraining-only vs. instruction-tuned),
and parameter count. Within CETVEL, all of the
evaluated LLMs have fewer than 70B parameters
and are open-weights, publicly available models.
Exceptionally, Turna and Aya-101 models employ
an encoder-decoder architecture built upon T5 (Raf-
fel et al., 2020).
4.2
Evaluation Metrics
We use standard automatic metrics tailored to each
task type. Language understanding tasks are
evaluated using accuracy. For MCQA tasks, can-
didate answers are scored based on per-token per-
plexity, and the option with the lowest perplexity is
selected. Extractive QA is evaluated using Exact
Match (EM) (Rajpurkar et al., 2016). Summariza-
tion is evaluated using ROUGE-2 (Lin, 2004). Ma-
chine translation using BLEU-4 (Papineni et al.,
2002), and Grammatical Error Correction using
macro-F1. We do not employ LLM-as-a-judge
metrics (Zheng et al., 2023), as they have been
shown to be unreliable in multilingual settings (Fu
and Liu, 2025).
4.3
Implementation Details
All experiments are conducted using the LM
Evaluation Harness (Gao et al., 2024), a frame-
work that supports evaluation of Huggingface-
compatible models and integrates with the vLLM
inference backend (Kwon et al., 2023) for efficient
model serving. For NLU tasks, we use a batch size
of 4. For generation tasks, we process one instance
at a time and limit outputs to a maximum of 64
5

--- Page 6 ---

tokens, following the protocol used in Mukayese
(Safaya et al., 2022). We use beam search decod-
ing with a beam width of 5 across all generative
tasks, ensuring deterministic evaluation. We run ex-
periments for each single model on eight NVIDIA
A40 GPUs. Experiment duration depends on the
model size, for instance, the entire set of experi-
ments for an 8 billion parameter model completes
less than two days. We note that, we conduct each
experiment with exactly one single forward run per
model.
5
Results
We present our evaluation results, focusing on
model performance with respect to parameter size,
multilingual coverage, and training paradigm. Ta-
ble 1 shows the top-20 models7 across all task cat-
egories, and Figure 2 visualizes average perfor-
mance grouped by model architecture and size.
5.1
Overall Results
Our results indicate that LLaMA 3 models con-
sistently outperform alternatives within compara-
ble parameter ranges. The best-performing model
overall is Llama-3.3-70B-Instruct, which exceeds
the second-best model, Aya-Expanse-32B, by 4.5
points in average score. Notably, Llama-3.1-8B
performs comparably to larger models such as
Aya-23-35B and Aya-Expanse-32B, indicating
strong performance scaling efficiency. Unexpect-
edly, base pretrained Qwen2.5 models outperform
their instruction-tuned variants across all parameter
sizes, except for the smallest 0.5B model.
Turkish-centric instruction-tuned models gener-
ally lag behind multilingual and English-centric
models. In particular, Commencis-LLM-7B and
Trendyol-LLM-7B underperform relative to their
base model Mistral-7B. Models pretrained from
scratch in Turkish also show weak results: Turna-
1B ranks last overall, and Kanarya-2B achieves
only an average score of 19.9.
One excep-
tion among Turkish-centric models is Cere-Llama-
3-8B, which excels in grammatical error cor-
rection and extractive QA on culturally specific
datasets (e.g., TQuAD), outperforming even Llama-
3.3-70B-Instruct on these tasks. However, Cere-
Llama-3-8B underperforms in machine transla-
tion and knowledge-intensive tasks, likely due to
the lack of English exposure and general-domain
7Full category-specific results are provided in the ap-
pendix.
fine-tuning. This highlights the importance of in-
cluding cross-lingual and domain-diverse data dur-
ing instruction tuning for low-resource language
models.
Overall, CETVEL reveals a substantial gap in
the current instruction-tuning strategies for Turkish
and highlights the limitations of monolingual or
narrowly focused Turkish-centric models.
5.2
Language Understanding Tasks
For non-generative tasks, Llama-3.3-70B-Instruct
again leads overall, particularly on knowledge-
intensive benchmarks such as Turkish proverbs and
riddles. Larger models tend to outperform smaller
ones on exam-style tasks (TurkishMMLU, Bele-
bele, Exams), likely due to increased memorization
and reasoning capacity. However, performance on
commonsense reasoning (e.g., XCOPA) is less sen-
sitive to model size. For instance, Qwen2.5-0.5B
achieves 53.6% accuracy on XCOPA, just 14.4
points below the strongest model, Qwen2.5-14B.
On the extractive QA task, Qwen2.5 models outper-
form LLaMA models on XQuAD, with Qwen2.5-
14B ranking highest. For TQuAD, however, Cere-
Llama-3-8B achieves the best score, outperform-
ing all others despite its smaller size—highlighting
the benefits of task-specific tuning for culturally
grounded datasets.
5.3
Language Generation Tasks
On generative tasks, Aya models (excluding Aya-
101-8B) take the lead in summarization and ma-
chine translation, likely due to their strong mul-
tilingual pretraining. These models particularly
benefit from overlapping multilingual content in
training corpora (e.g., WikiLingua), which may en-
hance memorization and transfer. In contrast, Cere-
Llama-3-8B achieves the best results on gram-
matical error correction even surpassing 70b pa-
rameters model Llama-3.3-70B-Instruct, but per-
forms poorly in summarization and translation
tasks-again pointing to the importance of balanced
cross-lingual training.
All remaining Turkish-
centric models perform extremely poorly on ma-
chine translation due to exclusion of English dur-
ing instruction-tuning phase, where Kanarya-2B is
the highest performing model, attaining a BLUE-4
score of 3.1. Nonetheless, Kanarya-2B achieves
an overall performance of 24.7 ROGUE-2 score
on MLSum, outperforming same parameter-scale
Qwen2.5 models.
6

--- Page 7 ---

Cohere
Gptj
Llama 3
Mistral
Mixtral
Qwen 2.5
T5
17.5
20.0
22.5
25.0
27.5
30.0
32.5
35.0
Average Performance
8B
32B
35B
3B
1B
3B
8B
70B
7B
8B
7B
46B
0.5B
1.5B
3B
7B
14B
1B
13B
Kanarya
Turna
Commencis
Trendyol
CerebrumTech
Figure 2: Overall performances on CETVEL grouped by model family. Model size is indicated by the size of
the corresponding sphere. A striped sphere indicates that the corresponding model is Turkish-centric LLM. Our
experiments reveal that Llama-3.3-70B-Instruct achieves the best overall performance
5.4
Turkish-Centric LLMs
Overall,
Turkish-centric
models
fall
behind
English-centric and multilingual LLMs. This is
the case for both LLMs pretrained from scratch on
Turkish or LLMs instruction-tuned on Turkish after
pretraining. Turkish LLMs pretrained from scratch,
Turna-1B and Kanarya-2B, rank in the lower places.
LLMs finetuned on Turkish instructions perform
better, yet they underperform against their base
models. Both Trendyol-LLM-7B and Commencis-
LLM-7B models achieve overall performances be-
low their base LLM, Mistral-7B. As we mentioned
earlier, they perform extremely poorly on machine
translation, due to catastrophic forgetting English
(Liu et al., 2024a). These models attain mediocre
overall performances, highlighting that there is a
large room for improvement in developing LLMs
that can effectively process Turkish. As we men-
tioned earlier, Cere-Llama-3-8B achieves the high-
est score on TQuAD and GECturk datasets, even
outperforming the largest model Llama-3.3-70B-
Instruct. Nonetheless, Cere-Llama-3-8B also suf-
fers from catastrophic forgetting like other LLMs
instruction-tuned on Turkish.
5.5
Task Discrimination Analysis
To assess which tasks most effectively differentiate
model capabilities, we compute bootstrapped Gini
coefficients (Dorfman, 1979) across task categories
and within the tasks using the following formula,
G =
1
2 n2 ¯x
n
X
i=1
n
X
j=1
xi −xj
,
¯x = 1
n
n
X
k=1
xk.
(1)
As shown in Figure 3, Grammatical error correc-
tion (GEC), machine translation (MT), and ques-
tion answering (QA) exhibit the highest discrimi-
nation power, with coefficients of 0.490, 0.402, and
0.362, respectively. These tasks consistently pro-
duce wide performance gaps across models, mak-
ing them particularly informative for benchmark-
ing. Conversely, natural language inference (NLI),
text classification (TC), and multiple-choice ques-
tion answering (MCQA) have much lower Gini
coefficients (0.039, 0.080, and 0.090, respectively),
suggesting limited utility in differentiating LLMs
in the Turkish setting.
Additionally, some task categories contain tasks
with substantially varying discriminative power.
For example, the XCOPA and Proverbs tasks, both
7

--- Page 8 ---

GECTurk
TurkishPLU-SO
XCOPA
CircumﬂexTR
TurkishPLU-GI
TurkishPLU-SI
TurkishPLU-NE
Exams
Riddles
Belebele
TurkishMMLU
Proverbs
WMT-16
XNLI
MNLI
SNLI
XQuAD
TQuAD
MKQA
MLSum
XLSum
WikiLingua
tr-wikihow-summ
IronyTR
STSb
NewsCat
OﬀenseEval
0.0
0.2
0.4
0.6
Gini
0.49
0.03 0.03 0.04 0.05 0.07 0.07 0.08
0.17 0.19 0.21
0.34
0.40
0.02 0.03 0.03
0.38 0.39
0.56
0.15
0.21 0.24 0.25
0.03
0.12
0.15
0.27
Per-Dataset Gini with 95% CI
GEC
MCQA
MT
NLI
QA
SUM
TC
0.0
0.1
0.2
0.3
0.4
0.5
0.6
Gini
0.49
0.09
0.40
0.03
0.36
0.17
0.08
Per-Group Gini with 95% CI
Figure 3: Bar plots with 95% CI of the task-specific and category-wise bootstrapped Gini coefficients. We find
that grammatical error correction, machine translation and extractive question answering tasks are the strongest
indicators of differentiating model performances. Conversely, NLI and TC tasks contribute the least to differentiating
model performances.
from the MCQA category, have Gini coefficients of
0.03 and 0.34, respectively, indicating room for im-
provement in this category. Despite this variability,
tasks from the QA and NLI categories consistently
show high and low Gini coefficients, respectively,
which may indicate overall category-level discrimi-
nation power rather than dataset selection.
6
Conclusion
In this work, we introduced CETVEL, a task-diverse
NLP benchmark designed to evaluate large lan-
guage models in Turkish, with particular attention
to linguistic and cultural specificity. CETVEL ad-
dresses key limitations of previous efforts, which
often lacked task diversity or overlooked culturally
grounded content.
By incorporating underexplored phenomena
such as proverbs and riddles, CETVEL broadens
the scope of evaluation beyond standard NLP tasks
and provides a more comprehensive testbed for
both multilingual and Turkish-specific models.
Our
extensive
experiments
reveal
that
instruction-tuned
Turkish
LLMs
consistently
underperform
compared
to
general-purpose
models that have been pretrained on multilingual
corpora including Turkish. These results point
to the need for more effective instruction-tuning
strategies tailored to Turkish, including higher-
quality prompts, culturally relevant tasks, and
improved validation pipelines.
Among the evaluated models, Llama 3 variants
deliver the strongest overall performance across
tasks and parameter ranges. Furthermore, our task
discrimination analysis shows that Grammar Error
Correction, Machine Translation, and Question An-
swering are particularly effective in distinguishing
model capabilities, while NLI and Topic Classifica-
tion tasks contribute less to differentiation.
We hope CETVEL serves as a valuable resource
for advancing Turkish NLP and guiding the devel-
opment of more robust and culturally aware LLMs.
8

--- Page 9 ---

Limitations
In this version of CETVEL, our evaluation is limited
to open-weight models with up to 70B parameters.
Due to recent API restrictions, we were unable
to include widely used proprietary models that no
longer support log-probability outputs, which are
essential for our evaluation pipeline. Moreover,
our analysis is restricted to the zero-shot setting.
While this provides a controlled and reproducible
baseline, incorporating one-shot and few-shot eval-
uations remains an important direction for future
iterations of the benchmark. Finally, we note that
CETVEL might include user-generated web data,
which can be noisy as recently shown by Cengiz
et al. (2025). Nevertheless, we retain these data
resources because the underlying information for
solving the tasks remains accurate.
Acknowledgments
We thank Mustafa Cemil Güney and Demir Ekin
Arıkan for their contributions on the early stages
of the development. Ilker Kesen was supported
by the European Union’s Horizon 2020 research
and innovation program under grant agreement
No. 101135671 (TrustLLM). This work has been
supported by the Scientific and Technological Re-
search Council of Türkiye (TÜBITAK) as part of
the project “Automatic Learning of Procedural Lan-
guage from Natural Language Instructions for Intel-
ligent Assistance” with the number 121C132. We
also gratefully acknowledge KUIS AI Center for
providing computational support.
References
Emre Can Acikgoz, Mete Erdogan, and Deniz Yuret.
2024. Bridging the bosphorus: Advancing Turkish
large language models through strategies for low-
resource language adaptation and benchmarking. In
Proceedings of the Fourth Workshop on Multilingual
Representation Learning (MRL 2024), pages 242–
268, Miami, Florida, USA. Association for Compu-
tational Linguistics.
David Ifeoluwa Adelani, Hannah Liu, Xiaoyu Shen,
Nikita Vassilyev, Jesujoba O. Alabi, Yanke Mao, Hao-
nan Gao, and En-Shiun Annie Lee. 2024. SIB-200:
A simple, inclusive, and big evaluation dataset for
topic classification in 200+ languages and dialects.
In Proceedings of the 18th Conference of the Euro-
pean Chapter of the Association for Computational
Linguistics (Volume 1: Long Papers), pages 226–245,
St. Julian’s, Malta. Association for Computational
Linguistics.
Kabir Ahuja, Harshita Diddee, Rishav Hada, Milli-
cent Ochieng, Krithika Ramesh, Prachi Jain, Ak-
shay Nambi, Tanuja Ganu, Sameer Segal, Mohamed
Ahmed, Kalika Bali, and Sunayana Sitaram. 2023.
MEGA: Multilingual evaluation of generative AI.
In Proceedings of the 2023 Conference on Empir-
ical Methods in Natural Language Processing, pages
4232–4267, Singapore. Association for Computa-
tional Linguistics.
Mohamad
Alhajar.
2024.
Open
llm
turkish
leaderboard.
https://huggingface.co/spaces/
malhajar/OpenLLMTurkishLeaderboard.
Mikel Artetxe, Sebastian Ruder, and Dani Yogatama.
2019. On the cross-lingual transferability of mono-
lingual representations. CoRR, abs/1910.11856.
Mikel Artetxe, Sebastian Ruder, and Dani Yogatama.
2020. On the cross-lingual transferability of mono-
lingual representations. In Proceedings of the 58th
Annual Meeting of the Association for Computational
Linguistics, pages 4623–4637, Online. Association
for Computational Linguistics.
Viraat Aryabumi, John Dang, Dwarak Talupuru,
Saurabh Dash, David Cairuz, Hangyu Lin, Bharat
Venkitesh, Madeline Smith, Jon Ander Campos,
Yi Chern Tan, et al. 2024. Aya 23: Open weight re-
leases to further multilingual progress. arXiv preprint
arXiv:2405.15032.
Ge Bai, Jie Liu, Xingyuan Bu, Yancheng He, Jia-
heng Liu, Zhanhui Zhou, Zhuoran Lin, Wenbo Su,
Tiezheng Ge, Bo Zheng, and Wanli Ouyang. 2024.
Mt-bench-101: A fine-grained benchmark for evalu-
ating large language models in multi-turn dialogues.
In Proceedings of the 62nd Annual Meeting of the
Association for Computational Linguistics (Volume
1: Long Papers), page 7421–7454. Association for
Computational Linguistics.
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
M Ali Bayram, Ali Arda Fincan, Ahmet Semih Gümü¸s,
Banu Diri, Sava¸s Yıldırım, and Öner Ayta¸s. 2024.
Setting standards in turkish nlp:
Tr-mmlu for
large language model evaluation.
arXiv preprint
arXiv:2501.00593.
Yonatan Bisk, Rowan Zellers, Jianfeng Gao, Yejin Choi,
et al. 2020. Piqa: Reasoning about physical com-
monsense in natural language. In Proceedings of the
AAAI conference on artificial intelligence, volume 34,
pages 7432–7439.
9

--- Page 10 ---

Ond rej Bojar, Rajen Chatterjee, Christian Federmann,
Yvette Graham, Barry Haddow, Matthias Huck, An-
tonio Jimeno Yepes, Philipp Koehn, Varvara Lo-
gacheva, Christof Monz, Matteo Negri, Aurelie
Neveol, Mariana Neves, Martin Popel, Matt Post,
Raphael Rubino, Carolina Scarton, Lucia Specia,
Marco Turchi, Karin Verspoor, and Marcos Zampieri.
2016. Findings of the 2016 conference on machine
translation. In Proceedings of the First Conference
on Machine Translation, pages 131–198, Berlin, Ger-
many. Association for Computational Linguistics.
Samuel R. Bowman, Gabor Angeli, Christopher Potts,
and Christopher D. Manning. 2015. A large anno-
tated corpus for learning natural language inference.
In Proceedings of the 2015 Conference on Empiri-
cal Methods in Natural Language Processing, pages
632–642, Lisbon, Portugal. Association for Compu-
tational Linguistics.
Emrah Budur, Rıza Özçelik, Tunga Gungor, and Christo-
pher Potts. 2020. Data and Representation for Turk-
ish Natural Language Inference. In Proceedings of
the 2020 Conference on Empirical Methods in Nat-
ural Language Processing (EMNLP), pages 8253–
8267, Online. Association for Computational Lin-
guistics.
Ay¸se Aysu Cengiz, Ahmet Kaan Sever, Elif Ecem
Ümütlü, Naime ¸Seyma Erdem, Burak Aytan, Bü¸sra
Tufan, Abdullah Topraksoy, Esra Darıcı, and Cagri
Toraman. 2025. Evaluating the quality of benchmark
datasets for low-resource languages: A case study on
turkish. Preprint, arXiv:2504.09714.
CerebrumTech. 2024. CerebrumTech/cere-llama-3-8b-
tr · Hugging Face.
Peter Clark, Isaac Cowhey, Oren Etzioni, Tushar Khot,
Ashish Sabharwal, Carissa Schoenick, and Oyvind
Tafjord. 2018.
Think you have solved question
answering?
try arc, the ai2 reasoning challenge.
Preprint, arXiv:1803.05457.
Karl Cobbe, Vineet Kosaraju, Mohammad Bavarian,
Mark Chen, Heewoo Jun, Lukasz Kaiser, Matthias
Plappert, Jerry Tworek, Jacob Hilton, Reiichiro
Nakano, Christopher Hesse, and John Schulman.
2021. Training verifiers to solve math word prob-
lems. arXiv preprint arXiv:2110.14168.
Ça˘grı Çöltekin. 2020. A corpus of Turkish offensive
language on social media. In Proceedings of the
Twelfth Language Resources and Evaluation Confer-
ence, pages 6174–6184, Marseille, France. European
Language Resources Association.
Commencis. 2024.
Commencis/Commencis-LLM ·
Hugging face.
Alexis Conneau, Ruty Rinott, Guillaume Lample, Ad-
ina Williams, Samuel R. Bowman, Holger Schwenk,
and Veselin Stoyanov. 2018. Xnli: Evaluating cross-
lingual sentence representations. In Proceedings of
the 2018 Conference on Empirical Methods in Natu-
ral Language Processing. Association for Computa-
tional Linguistics.
John Dang, Shivalika Singh, Daniel D’souza, Arash
Ahmadian, Alejandro Salamanca, Madeline Smith,
Aidan Peppin, Sungjin Hong, Manoj Govindassamy,
Terrence Zhao, et al. 2024. Aya expanse: Combin-
ing research breakthroughs for a new multilingual
frontier. arXiv preprint arXiv:2412.04261.
Jacob Devlin, Ming-Wei Chang, Kenton Lee, and
Kristina Toutanova. 2019. BERT: Pre-training of
deep bidirectional transformers for language under-
standing. In Proceedings of the 2019 Conference of
the North American Chapter of the Association for
Computational Linguistics: Human Language Tech-
nologies, Volume 1 (Long and Short Papers), pages
4171–4186, Minneapolis, Minnesota. Association for
Computational Linguistics.
Robert Dorfman. 1979. A formula for the gini coeffi-
cient. The review of economics and statistics, pages
146–149.
AbdelRahim Elmadany, ElMoatez Billah Nagoudi, and
Muhammad Abdul-Mageed. 2023. ORCA: A chal-
lenging benchmark for Arabic language understand-
ing. In Findings of the Association for Computa-
tional Linguistics: ACL 2023, pages 9559–9586,
Toronto, Canada. Association for Computational Lin-
guistics.
Leon Engländer, Hannah Sterz, Clifton Poth, Jonas
Pfeiffer, Ilia Kuznetsov, and Iryna Gurevych. 2024.
M2qa: Multi-domain multilingual question answer-
ing. arXiv preprint arXiv:2407.01091.
Xiyan Fu and Wei Liu. 2025. How reliable is multilin-
gual llm-as-a-judge? Preprint, arXiv:2505.12201.
Leo Gao, Jonathan Tow, Baber Abbasi, Stella Biderman,
Sid Black, Anthony DiPofi, Charles Foster, Laurence
Golding, Jeffrey Hsu, Alain Le Noac’h, Haonan Li,
Kyle McDonell, Niklas Muennighoff, Chris Ociepa,
Jason Phang, Laria Reynolds, Hailey Schoelkopf,
Aviya Skowron, Lintang Sutawika, Eric Tang, An-
ish Thite, Ben Wang, Kevin Wang, and Andy Zou.
2024. A framework for few-shot language model
evaluation.
Momchil
Hardalov,
Todor
Mihaylov,
Dimitrina
Zlatkova, Yoan Dinkov, Ivan Koychev, and Preslav
Nvakov. 2020.
Exams:
A multi-subject high
school examinations dataset for cross-lingual and
multilingual question answering.
arXiv preprint
arXiv:2011.03080.
Tahmid Hasan, Abhik Bhattacharjee, Md. Saiful Is-
lam, Kazi Mubasshir, Yuan-Fang Li, Yong-Bin Kang,
M. Sohel Rahman, and Rifat Shahriyar. 2021a. XL-
sum: Large-scale multilingual abstractive summariza-
tion for 44 languages. In Findings of the Association
for Computational Linguistics: ACL-IJCNLP 2021,
pages 4693–4703, Online. Association for Computa-
tional Linguistics.
Tahmid Hasan, Abhik Bhattacharjee, Md. Saiful Is-
lam, Kazi Mubasshir, Yuan-Fang Li, Yong-Bin Kang,
10

--- Page 11 ---

M. Sohel Rahman, and Rifat Shahriyar. 2021b. Xl-
sum: Large-scale multilingual abstractive summariza-
tion for 44 languages. In Findings of the Association
for Computational Linguistics: ACL-IJCNLP 2021.
Association for Computational Linguistics.
Dan Hendrycks, Collin Burns, Steven Basart, Andy Zou,
Mantas Mazeika, Dawn Song, and Jacob Steinhardt.
2020. Measuring massive multitask language under-
standing. arXiv preprint arXiv:2009.03300.
Dan Hendrycks, Collin Burns, Steven Basart, Andy
Zou, Mantas Mazeika, Dawn Song, and Jacob Stein-
hardt. 2021. Measuring massive multitask language
understanding. Proceedings of the International Con-
ference on Learning Representations (ICLR).
Junjie Hu, Sebastian Ruder, Aditya Siddhant, Graham
Neubig, Orhan Firat, and Melvin Johnson. 2020.
Xtreme: A massively multilingual multi-task bench-
mark for evaluating cross-lingual generalisation. In
International conference on machine learning, pages
4411–4421. PMLR.
Jafar Isbarov, Arofat Akhundjanova, Mammad Hajili,
Kavsar Huseynova, Dmitry Gaynullin, Anar Rzayev,
Osman Tursun, Ilshat Saetov, Rinat Kharisov, Saule
Belginova, et al. 2025. Tumlu: A unified and na-
tive language understanding benchmark for turkic
languages. arXiv preprint arXiv:2502.11020.
Albert Q. Jiang, Alexandre Sablayrolles, Arthur Men-
sch, Chris Bamford, Devendra Singh Chaplot, Diego
de las Casas, Florian Bressand, Gianna Lengyel, Guil-
laume Lample, Lucile Saulnier, Lélio Renard Lavaud,
Marie-Anne Lachaux, Pierre Stock, Teven Le Scao,
Thibaut Lavril, Thomas Wang, Timothée Lacroix,
and William El Sayed. 2023. Mistral 7b. Preprint,
arXiv:2310.06825.
Albert Q Jiang, Alexandre Sablayrolles, Antoine
Roux, Arthur Mensch, Blanche Savary, Chris Bam-
ford, Devendra Singh Chaplot, Diego de las Casas,
Emma Bou Hanna, Florian Bressand, et al. 2024.
Mixtral of experts. arXiv preprint arXiv:2401.04088.
Atakan Kara, Farrin Marouf Sofian, Andrew Bond, and
Gözde ¸Sahin. 2023. GECTurk: Grammatical error
correction and detection dataset for Turkish. In Find-
ings of the Association for Computational Linguis-
tics: IJCNLP-AACL 2023 (Findings), pages 278–290,
Nusa Dua, Bali. Association for Computational Lin-
guistics.
Woosuk Kwon, Zhuohan Li, Siyuan Zhuang, Ying
Sheng, Lianmin Zheng, Cody Hao Yu, Joseph E.
Gonzalez, Hao Zhang, and Ion Stoica. 2023. Effi-
cient memory management for large language model
serving with pagedattention. In Proceedings of the
ACM SIGOPS 29th Symposium on Operating Systems
Principles.
Faisal Ladhak, Esin Durmus, Claire Cardie, and Kath-
leen McKeown. 2020. WikiLingua: A new bench-
mark dataset for cross-lingual abstractive summariza-
tion. In Findings of the Association for Computa-
tional Linguistics: EMNLP 2020, pages 4034–4048,
Online. Association for Computational Linguistics.
Patrick Lewis, Barlas O˘guz, Ruty Rinott, Sebastian
Riedel, and Holger Schwenk. 2019. Mlqa: Eval-
uating cross-lingual extractive question answering.
arXiv preprint arXiv:1910.07475.
Yaobo Liang, Nan Duan, Yeyun Gong, Ning Wu, Fen-
fei Guo, Weizhen Qi, Ming Gong, Linjun Shou,
Daxin Jiang, Guihong Cao, et al. 2020.
Xglue:
A new benchmark dataset for cross-lingual pre-
training, understanding and generation.
arXiv
preprint arXiv:2004.01401.
Chin-Yew Lin. 2004. ROUGE: A package for auto-
matic evaluation of summaries. In Text Summariza-
tion Branches Out, pages 74–81, Barcelona, Spain.
Association for Computational Linguistics.
Stephanie Lin, Jacob Hilton, and Owain Evans. 2022.
TruthfulQA: Measuring how models mimic human
falsehoods. In Proceedings of the 60th Annual Meet-
ing of the Association for Computational Linguistics
(Volume 1: Long Papers), pages 3214–3252, Dublin,
Ireland. Association for Computational Linguistics.
Chengyuan Liu, Yangyang Kang, Shihang Wang, Lizhi
Qing, Fubang Zhao, Chao Wu, Changlong Sun,
Kun Kuang, and Fei Wu. 2024a. More than catas-
trophic forgetting: Integrating general capabilities for
domain-specific LLMs. In Proceedings of the 2024
Conference on Empirical Methods in Natural Lan-
guage Processing, pages 7531–7548, Miami, Florida,
USA. Association for Computational Linguistics.
Jiawei Liu, Chunqiu Steven Xia, Yuyao Wang, and Ling-
ming Zhang. 2023. Is your code generated by chat-
GPT really correct? rigorous evaluation of large lan-
guage models for code generation. In Thirty-seventh
Conference on Neural Information Processing Sys-
tems.
Jiawei Liu, Songrun Xie, Junhao Wang, Yuxiang Wei,
Yifeng Ding, and Lingming Zhang. 2024b. Evaluat-
ing language models for efficient code generation. In
First Conference on Language Modeling.
Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Man-
dar Joshi, Danqi Chen, Omer Levy, Mike Lewis,
Luke Zettlemoyer, and Veselin Stoyanov. 2019.
Roberta: A robustly optimized bert pretraining ap-
proach. Preprint, arXiv:1907.11692.
LLaMA-Team. 2024.
The llama 3 herd of models.
Preprint, arXiv:2407.21783.
Shayne Longpre, Yi Lu, and Joachim Daiber. 2021.
MKQA: A linguistically diverse benchmark for mul-
tilingual open domain question answering. Transac-
tions of the Association for Computational Linguis-
tics, 9:1389–1406.
Chunlan Ma, Ayyoob Imani, Haotian Ye, Renhao Pei,
Ehsaneddin Asgari, and Hinrich Schuetze. 2025.
11

--- Page 12 ---

Taxi1500: A dataset for multilingual text classifi-
cation in 1500 languages. In Proceedings of the 2025
Conference of the Nations of the Americas Chap-
ter of the Association for Computational Linguistics:
Human Language Technologies (Volume 2: Short Pa-
pers), pages 414–439, Albuquerque, New Mexico.
Association for Computational Linguistics.
Dan Nielsen. 2023. ScandEval: A benchmark for Scan-
dinavian natural language processing. In Proceed-
ings of the 24th Nordic Conference on Computational
Linguistics (NoDaLiDa), pages 185–201, Tórshavn,
Faroe Islands. University of Tartu Library.
Asli Umay Ozturk, Yesim Cemek, and Pinar Karagoz.
2021. Ironytr: Irony detection in turkish informal
texts. International Journal of Intelligent Informa-
tion Technologies (IJIIT), 17(4):1–18.
Kishore Papineni, Salim Roukos, Todd Ward, and Wei-
Jing Zhu. 2002. Bleu: a method for automatic evalu-
ation of machine translation. In Proceedings of the
40th Annual Meeting of the Association for Compu-
tational Linguistics, pages 311–318, Philadelphia,
Pennsylvania, USA. Association for Computational
Linguistics.
Sungjoon Park, Jihyung Moon, Sungdong Kim, Won Ik
Cho, Jiyoon Han, Jangwon Park, Chisung Song, Jun-
seong Kim, Yongsook Song, Taehwan Oh, et al. 2021.
Klue: Korean language understanding evaluation.
arXiv preprint arXiv:2105.09680.
Edoardo Maria Ponti, Goran Glavaš, Olga Majewska,
Qianchu Liu, Ivan Vuli´c, and Anna Korhonen. 2020.
XCOPA: A multilingual dataset for causal common-
sense reasoning. In Proceedings of the 2020 Con-
ference on Empirical Methods in Natural Language
Processing (EMNLP), pages 2362–2376, Online. As-
sociation for Computational Linguistics.
Colin Raffel, Noam Shazeer, Adam Roberts, Katherine
Lee, Sharan Narang, Michael Matena, Yanqi Zhou,
Wei Li, and Peter J Liu. 2020. Exploring the lim-
its of transfer learning with a unified text-to-text
transformer. Journal of machine learning research,
21(140):1–67.
Afshin Rahimi, Yuan Li, and Trevor Cohn. 2019. Mas-
sively multilingual transfer for NER. In Proceedings
of the 57th Annual Meeting of the Association for
Computational Linguistics, pages 151–164, Florence,
Italy. Association for Computational Linguistics.
Pranav Rajpurkar, Jian Zhang, Konstantin Lopyrev, and
Percy Liang. 2016. SQuAD: 100,000+ questions for
machine comprehension of text. In Proceedings of
the 2016 Conference on Empirical Methods in Natu-
ral Language Processing, pages 2383–2392, Austin,
Texas. Association for Computational Linguistics.
David Rein, Betty Li Hou, Asa Cooper Stickland, Jack-
son Petty, Richard Yuanzhe Pang, Julien Dirani, Ju-
lian Michael, and Samuel R. Bowman. 2024. GPQA:
A graduate-level google-proof q&a benchmark. In
First Conference on Language Modeling.
Sebastian Ruder, Noah Constant, Jan Botha, Aditya Sid-
dhant, Orhan Firat, Jinlan Fu, Pengfei Liu, Junjie Hu,
Dan Garrette, Graham Neubig, et al. 2021. Xtreme-r:
Towards more challenging and nuanced multilingual
evaluation. arXiv preprint arXiv:2104.07412.
Ali Safaya, Emirhan Kurtulu¸s, Arda Goktogan, and
Deniz Yuret. 2022. Mukayese: Turkish NLP strikes
back. In Findings of the Association for Compu-
tational Linguistics: ACL 2022, pages 846–863,
Dublin, Ireland. Association for Computational Lin-
guistics.
Thomas Scialom, Paul-Alexis Dray, Sylvain Lamprier,
Benjamin Piwowarski, and Jacopo Staiano. 2020.
MLSUM: The multilingual summarization corpus.
In Proceedings of the 2020 Conference on Empirical
Methods in Natural Language Processing (EMNLP),
pages 8051–8067, Online. Association for Computa-
tional Linguistics.
Shivalika Singh, Angelika Romanou, Clémentine Four-
rier, David I. Adelani, Jian Gang Ngui, Daniel
Vila-Suero, Peerat Limkonchotiwat, Kelly Marchi-
sio, Wei Qi Leong, Yosephine Susanto, Raymond
Ng, Shayne Longpre, Wei-Yin Ko, Madeline Smith,
Antoine Bosselut, Alice Oh, Andre F. T. Martins,
Leshem Choshen, Daphne Ippolito, Enzo Ferrante,
Marzieh Fadaee, Beyza Ermis, and Sara Hooker.
2024. Global mmlu: Understanding and addressing
cultural and linguistic biases in multilingual evalua-
tion. Preprint, arXiv:2412.03304.
Hugo Touvron, Louis Martin, Kevin Stone, Peter Al-
bert, Amjad Almahairi, Yasmine Babaei, Nikolay
Bashlykov, Soumya Batra, Prajjwal Bhargava, Shruti
Bhosale, et al. 2023.
Llama 2:
Open founda-
tion and fine-tuned chat models.
arXiv preprint
arXiv:2307.09288.
Trendyol. 2024.
Trendyol/Trendyol-LLM-7b-base-
V1.0 · Hugging face.
Gökçe Uludo˘gan, Zeynep Balal, Furkan Akkurt, Melik-
sah Turker, Onur Gungor, and Susan Üsküdarlı. 2024.
TURNA: A Turkish encoder-decoder language model
for enhanced understanding and generation. In Find-
ings of the Association for Computational Linguistics:
ACL 2024, pages 10103–10117, Bangkok, Thailand.
Association for Computational Linguistics.
Ahmet Üstün, Viraat Aryabumi, Zheng Yong, Wei-Yin
Ko, Daniel D’souza, Gbemileke Onilude, Neel Bhan-
dari, Shivalika Singh, Hui-Lee Ooi, Amr Kayid, Fred-
die Vargus, Phil Blunsom, Shayne Longpre, Niklas
Muennighoff, Marzieh Fadaee, Julia Kreutzer, and
Sara Hooker. 2024. Aya model: An instruction fine-
tuned open-access multilingual language model. In
Proceedings of the 62nd Annual Meeting of the As-
sociation for Computational Linguistics (Volume 1:
Long Papers), pages 15894–15939, Bangkok, Thai-
land. Association for Computational Linguistics.
Arda Uzunoglu and Gözde ¸Sahin. 2023. Benchmarking
procedural language understanding for low-resource
12

--- Page 13 ---

languages: A case study on Turkish. In Proceed-
ings of the 13th International Joint Conference on
Natural Language Processing and the 3rd Confer-
ence of the Asia-Pacific Chapter of the Association
for Computational Linguistics (Volume 1: Long Pa-
pers), pages 804–819, Nusa Dua, Bali. Association
for Computational Linguistics.
Alex Wang, Yada Pruksachatkun, Nikita Nangia, Aman-
preet Singh, Julian Michael, Felix Hill, Omer Levy,
and Samuel Bowman. 2019. Superglue: A stick-
ier benchmark for general-purpose language under-
standing systems. Advances in neural information
processing systems, 32.
Alex Wang, Amanpreet Singh, Julian Michael, Felix
Hill, Omer Levy, and Samuel R Bowman. 2018.
Glue: A multi-task benchmark and analysis platform
for natural language understanding. arXiv preprint
arXiv:1804.07461.
Bin Wang, Zhengyuan Liu, Xin Huang, Fangkai Jiao,
Yang Ding, AiTi Aw, and Nancy F Chen. 2023.
Seaeval for multilingual foundation models: From
cross-lingual alignment to cultural reasoning. arXiv
preprint arXiv:2309.04766.
Thomas Wolf, Lysandre Debut, Victor Sanh, Julien
Chaumond, Clement Delangue, Anthony Moi, Pier-
ric Cistac, Tim Rault, Rémi Louf, Morgan Funtowicz,
Joe Davison, Sam Shleifer, Patrick von Platen, Clara
Ma, Yacine Jernite, Julien Plu, Canwen Xu, Teven Le
Scao, Sylvain Gugger, Mariama Drame, Quentin
Lhoest, and Alexander M. Rush. 2020. Transform-
ers: State-of-the-art natural language processing. In
Proceedings of the 2020 Conference on Empirical
Methods in Natural Language Processing: System
Demonstrations, pages 38–45, Online. Association
for Computational Linguistics.
An Yang, Baosong Yang, Beichen Zhang, Binyuan Hui,
Bo Zheng, Bowen Yu, Chengyuan Li, Dayiheng Liu,
Fei Huang, Haoran Wei, et al. 2024. Qwen2. 5 tech-
nical report. arXiv preprint arXiv:2412.15115.
Arda Yüksel, Abdullatif Köksal, Lütfi Kerem ¸Senel,
Anna Korhonen,
and Hinrich Schütze. 2024.
Turkishmmlu: Measuring massive multitask lan-
guage understanding in turkish.
arXiv preprint
arXiv:2407.12402.
Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan
Zhuang, Zhanghao Wu, Yonghao Zhuang, Zi Lin,
Zhuohan Li, Dacheng Li, Eric Xing, et al. 2023.
Judging llm-as-a-judge with mt-bench and chatbot
arena. Advances in neural information processing
systems, 36:46595–46623.
A
AI Assistant Usage
Within this work, we only used AI Assistants for
writing purposes. We mainly used chatbots for
refining our initial writing, i.e., proof-reading, im-
proving clarity and coherence. We did not use them
for generating textual content based on instructions.
B
Complete Results
This appendix subsection includes overall and
task-specific results for all models tested within
CETVEL.
13

--- Page 14 ---

B.1
Overall Results
QA
MC
TC
NLI
SUM
MT
GEC
Avg.
Llama-3.3-70B-Instruct
16.1
60.1
58.1
32.4
16.2
13.6
44.1
34.4
Aya-Expanse-32B
26.2
55.6
55.3
43.3
22.4
20.1
4.5
32.5
Aya-23-35B
23.7
48.8
38.0
37.6
17.6
18.5
30.8
30.7
Llama-3.1-8B
19.3
45.8
44.8
32.2
13.5
15.6
35.3
29.5
Llama-3.1-8B-Instruct
18.0
50.1
40.1
36.0
13.5
15.6
31.5
29.3
Qwen2.5-7B
20.5
50.6
51.6
34.0
12.8
5.5
22.3
28.2
Llama-3-8B
20.9
43.0
40.6
33.9
12.3
11.3
34.1
28.0
Cere-Llama-3-8B
24.2
44.8
43.7
34.0
3.5
0.1
46.0
28.0
Ministral-2410-8B-Instruct
14.2
42.8
38.0
34.0
12.8
11.2
39.1
27.5
Qwen2.5-14B
26.7
52.6
37.7
34.0
13.0
8.1
18.9
27.3
Aya-Expanse-8B
15.1
52.2
43.6
34.7
12.2
17.0
5.5
25.7
Aya-23-8B
18.5
45.7
45.3
33.3
12.8
16.9
4.3
25.2
Llama-3.2-3B
14.2
40.6
38.7
32.5
12.1
7.9
26.8
24.7
Qwen2.5-14B-Instruct
0.4
56.0
43.3
35.2
12.8
12.4
10.9
24.4
Llama-3-8B-Instruct
9.0
49.3
40.6
33.8
13.8
13.6
10.0
24.3
Qwen2.5-3B
19.7
41.5
40.2
34.0
12.3
4.1
14.7
23.8
Mistral-v0.3-7B
16.8
39.0
37.7
34.0
7.9
3.8
23.5
23.2
Qwen2.5-5B
22.1
39.8
35.3
33.9
12.0
4.1
14.2
23.0
Mixtral-v0.1-7B-Instruct
11.0
45.1
45.6
33.7
10.9
9.5
3.6
22.8
Qwen2.5-7B-Instruct
0.5
50.9
48.4
35.0
11.0
5.4
6.6
22.5
Mistral-v0.1-7B
16.6
39.2
37.3
33.9
3.6
5.0
20.8
22.4
Llama-3.2-3B-Instruct
15.5
39.1
36.9
34.0
8.1
4.9
16.7
22.2
Commencis-7B
5.1
38.1
39.4
32.5
9.8
4.7
23.7
21.9
Aya-101-13B
5.2
40.6
42.3
27.8
0.1
0.0
32.4
21.2
Llama-3.2-1B
4.0
37.7
43.7
34.1
7.5
1.2
18.1
20.9
Kanarya-2B
1.0
41.0
47.8
33.1
10.9
3.0
6.6
20.5
Qwen2.5-3B-Instruct
3.1
45.2
35.7
34.0
12.0
6.6
4.1
20.1
Qwen2.5-5B-Instruct
10.4
42.8
33.0
33.9
12.0
4.7
3.6
20.1
Mistral-v0.3-7B-Instruct
8.7
38.6
42.5
31.7
11.2
5.9
1.0
19.9
Qwen2.5-5B-Instruct
10.1
36.9
27.8
33.9
10.7
3.1
1.8
17.7
Trendyol-v1.0-7B-Base
0.3
38.4
41.8
34.3
5.3
1.0
0.1
17.3
Qwen2.5-5B
3.8
37.8
30.7
33.9
11.3
1.4
0.9
17.1
Turna-1B
0.0
35.9
36.6
34.1
7.1
0.1
0.0
16.3
Table 2: Overall results of the models, sorted by their average scores. Base and instruction-tuned variants are
represented by circles and squares, respectively. Colors indicate the language focus: blue for English-focused,
yellow for multilingual-focused, and red for Turkish-focused models.
14

--- Page 15 ---

B.2
Grammatical Error Correction Results
GECTurk
Avg.
Cere-Llama-3-8B
46.0
46.0
Llama-3.3-70B-Instruct
44.1
44.1
Ministral-2410-8B-Instruct
39.1
39.1
Llama-3.1-8B
35.3
35.3
Llama-3-8B
34.1
34.1
Aya-101-13B
32.4
32.4
Llama-3.1-8B-Instruct
31.5
31.5
Aya-23-35B
30.8
30.8
Llama-3.2-3B
26.8
26.8
Commencis-7B
23.7
23.7
Mistral-v0.3-7B
23.5
23.5
Qwen2.5-7B
22.3
22.3
Mistral-v0.1-7B
20.8
20.8
Qwen2.5-14B
18.9
18.9
Llama-3.2-1B
18.1
18.1
Llama-3.2-3B-Instruct
16.7
16.7
Qwen2.5-3B
14.7
14.7
Qwen2.5-5B
14.2
14.2
Qwen2.5-14B-Instruct
10.9
10.9
Llama-3-8B-Instruct
10.0
10.0
Kanarya-2B
6.6
6.6
Qwen2.5-7B-Instruct
6.6
6.6
Aya-Expanse-8B
5.5
5.5
Aya-Expanse-32B
4.5
4.5
Aya-23-8B
4.3
4.3
Qwen2.5-3B-Instruct
4.1
4.1
Mixtral-v0.1-7B-Instruct
3.6
3.6
Qwen2.5-5B-Instruct
3.6
3.6
Qwen2.5-5B-Instruct
1.8
1.8
Mistral-v0.3-7B-Instruct
1.0
1.0
Qwen2.5-5B
0.9
0.9
Trendyol-v1.0-7B-Base
0.1
0.1
Turna-1B
0.0
0.0
Table 3: Grammatical error correction results of the models, sorted by their average scores. Base and instruction-
tuned variants are represented by circles and squares, respectively. Colors indicate the language focus: blue for
English-focused, yellow for multilingual-focused, and red for Turkish-focused models.
15

--- Page 16 ---

B.3
Multiple Choice Question Answering Results
XCOPA
PLU
PLU_GI
PLU_NEP
PLU_SI
PLU_SO
Exams
Belebele
Proverbs
TurkishMMLU
BilmeceBench
CircumflexTR
Avg.
Llama-3.3-70B-Instruct
65.0
54.2
49.1
58.0
39.1
65.1
39.2
86.8
92.5
64.6
72.6
67.1
60.1
Qwen2.5-14B-Instruct
66.6
48.5
40.6
49.8
35.1
62.2
29.8
84.7
78.3
59.4
57.0
58.6
56.0
Aya-Expanse-32B
59.2
51.8
44.8
55.1
39.2
63.0
36.9
83.4
82.4
56.9
41.2
57.1
55.6
Qwen2.5-14B
64.6
48.7
41.3
48.7
35.3
62.9
33.1
81.2
75.4
56.2
47.5
58.6
52.6
Aya-Expanse-8B
57.8
50.2
43.0
51.1
40.4
61.4
31.6
73.6
72.3
46.6
48.9
54.3
52.2
Qwen2.5-7B-Instruct
61.8
47.1
41.1
46.7
32.2
61.3
30.3
73.4
71.2
47.6
52.0
54.3
50.9
Qwen2.5-7B
59.8
48.3
42.5
47.2
32.2
63.4
29.5
73.9
73.5
49.3
48.4
57.1
50.6
Llama-3.1-8B-Instruct
60.8
48.5
40.9
44.6
34.3
65.7
32.3
70.8
75.5
38.1
41.6
64.3
50.1
Llama-3-8B-Instruct
58.6
47.1
37.6
46.6
33.5
63.5
27.0
66.3
69.5
38.1
38.5
61.4
49.3
Aya-23-35B
60.4
48.8
43.0
52.1
35.1
59.7
29.8
72.9
56.9
45.3
34.8
60.0
48.8
Llama-3.1-8B
62.6
47.6
38.8
46.0
35.1
63.2
31.3
61.4
54.1
30.6
32.1
58.6
45.8
Aya-23-8B
59.6
49.3
42.1
48.9
37.3
62.7
27.0
60.7
45.0
33.0
34.4
58.6
45.7
Qwen2.5-3B-Instruct
56.2
44.8
38.9
42.0
32.2
59.1
27.5
67.4
60.1
37.8
33.0
54.3
45.2
Mixtral-v0.1-7B-Instruct
56.4
47.1
44.6
46.1
31.7
59.1
29.3
58.6
51.5
35.8
34.2
57.1
45.1
Cere-Llama-3-8B
60.2
48.7
41.8
46.9
35.9
63.1
28.0
51.4
48.1
25.6
33.9
58.6
44.8
Llama-3-8B
61.8
46.5
36.9
46.1
32.8
62.8
30.3
51.4
44.0
25.4
29.6
54.3
43.0
Ministral-2410-8B-Instruct
57.4
45.3
37.5
44.1
31.9
60.6
31.3
60.9
40.5
26.4
24.9
58.6
42.8
Qwen2.5-5B-Instruct
54.6
42.5
35.7
40.3
28.1
58.2
22.9
53.4
34.7
28.9
29.2
48.6
42.8
Qwen2.5-3B
55.2
43.9
38.0
40.6
29.7
59.5
26.5
61.9
43.5
22.6
24.4
55.7
41.5
Kanarya-2B
64.2
49.3
45.9
45.6
35.8
62.5
30.0
28.1
0.0
18.0
27.1
54.3
41.0
Aya-101-13B
59.6
41.3
37.4
35.0
27.3
57.1
22.9
22.9
1.0
37.4
47.1
57.1
40.6
Llama-3.2-3B
57.0
45.4
40.0
43.2
31.5
59.5
29.5
47.3
19.9
29.0
29.0
57.1
40.6
Qwen2.5-5B
54.2
42.1
35.8
39.7
27.3
57.6
21.6
46.7
23.0
23.0
29.9
50.0
39.8
Mistral-v0.1-7B
56.6
45.2
42.8
39.5
29.2
60.2
24.2
37.4
30.8
20.3
25.3
57.1
39.2
Llama-3.2-3B-Instruct
54.6
44.0
35.5
39.4
27.8
63.7
26.2
55.8
1.1
34.4
31.0
54.3
39.1
Mistral-v0.3-7B
58.4
43.4
41.0
38.6
26.6
58.4
24.2
41.1
27.6
26.9
23.5
57.1
39.0
Mistral-v0.3-7B-Instruct
57.2
43.0
41.2
40.9
27.0
55.3
25.4
46.1
30.0
19.6
21.5
50.0
38.6
Trendyol-v1.0-7B-Base
61.0
46.9
46.4
43.2
32.4
58.6
28.5
36.2
0.0
24.8
23.1
57.1
38.4
Commencis-7B
58.0
41.3
34.8
38.6
27.6
56.5
24.7
32.3
22.7
24.7
24.2
58.6
38.1
Qwen2.5-5B
54.8
40.8
36.2
35.7
26.5
56.5
21.1
29.9
20.3
17.9
25.1
47.1
37.8
Llama-3.2-1B
55.6
42.1
36.2
37.3
29.2
57.7
28.5
29.6
21.7
18.9
22.4
52.9
37.7
Qwen2.5-5B-Instruct
53.6
41.6
36.8
35.6
28.1
57.4
23.7
30.0
28.3
21.1
24.2
54.3
36.9
Turna-1B
55.8
40.3
38.0
38.3
27.3
51.2
23.7
22.6
19.2
19.3
24.2
51.4
35.9
Table 4: Multiple choice question answering results of the models, sorted by their average scores. Base and
instruction-tuned variants are represented by circles and squares, respectively. Colors indicate the language focus:
blue for English-focused, yellow for multilingual-focused, and red for Turkish-focused models.
16

--- Page 17 ---

B.4
Machine Translation Results
WMT16EN-TR
Avg.
Aya-Expanse-32B
20.1
20.1
Aya-23-35B
18.5
18.5
Aya-Expanse-8B
17.0
17.0
Aya-23-8B
16.9
16.9
Llama-3.1-8B-Instruct
15.6
15.6
Llama-3.1-8B
15.6
15.6
Llama-3.3-70B-Instruct
13.6
13.6
Llama-3-8B-Instruct
13.6
13.6
Qwen2.5-14B-Instruct
12.4
12.4
Llama-3-8B
11.3
11.3
Ministral-2410-8B-Instruct
11.2
11.2
Mixtral-v0.1-7B-Instruct
9.5
9.5
Qwen2.5-14B
8.1
8.1
Llama-3.2-3B
7.9
7.9
Qwen2.5-3B-Instruct
6.6
6.6
Mistral-v0.3-7B-Instruct
5.9
5.9
Qwen2.5-7B
5.5
5.5
Qwen2.5-7B-Instruct
5.4
5.4
Mistral-v0.1-7B
5.0
5.0
Llama-3.2-3B-Instruct
4.9
4.9
Commencis-7B
4.7
4.7
Qwen2.5-5B-Instruct
4.7
4.7
Qwen2.5-3B
4.1
4.1
Qwen2.5-5B
4.1
4.1
Mistral-v0.3-7B
3.8
3.8
Qwen2.5-5B-Instruct
3.1
3.1
Kanarya-2B
3.0
3.0
Qwen2.5-5B
1.4
1.4
Llama-3.2-1B
1.2
1.2
Trendyol-v1.0-7B-Base
1.0
1.0
Cere-Llama-3-8B
0.1
0.1
Turna-1B
0.1
0.1
Aya-101-13B
0.0
0.0
Table 5: Machine translation results of the models, sorted by their average scores. Base and instruction-tuned
variants are represented by circles and squares, respectively. Colors indicate the language focus: blue for English-
focused, yellow for multilingual-focused, and red for Turkish-focused models.
17

--- Page 18 ---

B.5
Natural Language Inference Results
MNLI
SNLI
XNLI
Avg.
Aya-Expanse-32B
42.5
47.1
40.5
43.3
Aya-23-35B
37.3
37.3
38.1
37.6
Llama-3.1-8B-Instruct
36.7
35.9
35.4
36.0
Qwen2.5-14B-Instruct
35.3
36.3
34.1
35.2
Qwen2.5-7B-Instruct
35.6
35.5
33.8
35.0
Aya-Expanse-8B
36.1
31.6
36.3
34.7
Trendyol-v1.0-7B-Base
35.2
33.7
34.0
34.3
Llama-3.2-1B
35.0
33.7
33.5
34.1
Turna-1B
34.9
33.8
33.4
34.1
Llama-3.2-3B-Instruct
34.8
33.8
33.4
34.0
Mistral-v0.3-7B
34.9
33.4
33.6
34.0
Qwen2.5-3B-Instruct
34.8
33.7
33.4
34.0
Qwen2.5-14B
34.8
33.7
33.4
34.0
Ministral-2410-8B-Instruct
34.8
33.7
33.4
34.0
Cere-Llama-3-8B
34.9
33.7
33.3
34.0
Qwen2.5-3B
34.8
33.7
33.4
34.0
Qwen2.5-7B
34.8
33.6
33.4
34.0
Qwen2.5-5B-Instruct
34.8
33.7
33.3
33.9
Mistral-v0.1-7B
34.8
33.6
33.4
33.9
Qwen2.5-5B-Instruct
34.8
33.7
33.3
33.9
Qwen2.5-5B
34.8
33.7
33.3
33.9
Llama-3-8B
34.8
33.6
33.4
33.9
Qwen2.5-5B
34.7
33.7
33.4
33.9
Llama-3-8B-Instruct
35.1
33.3
33.1
33.8
Mixtral-v0.1-7B-Instruct
34.8
32.2
34.1
33.7
Aya-23-8B
32.7
33.6
33.7
33.3
Kanarya-2B
33.4
31.7
34.2
33.1
Llama-3.2-3B
32.0
32.5
33.0
32.5
Commencis-7B
33.3
31.5
32.7
32.5
Llama-3.3-70B-Instruct
32.1
31.7
33.3
32.4
Llama-3.1-8B
31.9
34.3
30.3
32.2
Mistral-v0.3-7B-Instruct
31.3
31.8
32.0
31.7
Aya-101-13B
27.9
25.6
30.0
27.8
Table 6: Natural language inference results of the models, sorted by their average scores. Base and instruction-tuned
variants are represented by circles and squares, respectively. Colors indicate the language focus: blue for English-
focused, yellow for multilingual-focused, and red for Turkish-focused models.
18

--- Page 19 ---

B.6
Open Ended Question Answering Results
XQUAD
TQUAD
MKQA
Avg.
Qwen2.5-14B
40.3
34.8
5.0
26.7
Aya-Expanse-32B
31.9
30.2
16.4
26.2
Cere-Llama-3-8B
21.2
49.2
2.2
24.2
Aya-23-35B
30.9
20.6
19.4
23.7
Qwen2.5-5B
31.8
34.3
0.3
22.1
Llama-3-8B
20.8
28.5
13.5
20.9
Qwen2.5-7B
31.9
28.0
1.4
20.5
Qwen2.5-3B
32.3
26.8
0.1
19.7
Llama-3.1-8B
20.9
27.6
9.2
19.3
Aya-23-8B
24.7
20.6
10.0
18.5
Llama-3.1-8B-Instruct
21.4
23.3
9.1
18.0
Mistral-v0.3-7B
17.1
21.9
11.5
16.8
Mistral-v0.1-7B
16.7
21.0
12.0
16.6
Llama-3.3-70B-Instruct
14.5
17.4
16.3
16.1
Llama-3.2-3B-Instruct
23.0
18.7
4.7
15.5
Aya-Expanse-8B
25.0
13.5
7.0
15.1
Llama-3.2-3B
15.5
21.2
6.0
14.2
Ministral-2410-8B-Instruct
22.9
17.6
2.2
14.2
Mixtral-v0.1-7B-Instruct
10.7
9.8
12.5
11.0
Qwen2.5-5B-Instruct
16.5
14.7
0.2
10.4
Qwen2.5-5B-Instruct
13.4
16.3
0.7
10.1
Llama-3-8B-Instruct
9.7
12.9
4.2
9.0
Mistral-v0.3-7B-Instruct
11.4
9.5
5.0
8.7
Aya-101-13B
7.6
5.4
2.5
5.2
Commencis-7B
6.6
5.4
3.2
5.1
Llama-3.2-1B
4.9
6.3
0.8
4.0
Qwen2.5-5B
4.0
7.2
0.1
3.8
Qwen2.5-3B-Instruct
6.1
3.3
0.1
3.1
Kanarya-2B
0.8
1.7
0.6
1.0
Qwen2.5-7B-Instruct
0.9
0.6
0.0
0.5
Qwen2.5-14B-Instruct
0.9
0.3
0.0
0.4
Trendyol-v1.0-7B-Base
0.0
0.8
0.1
0.3
Turna-1B
0.0
0.0
0.1
0.0
Table 7: Open ended question answering results results of the models, sorted by their average scores. Base and
instruction-tuned variants are represented by circles and squares, respectively. Colors indicate the language focus:
blue for English-focused, yellow for multilingual-focused, and red for Turkish-focused models.
19

--- Page 20 ---

B.7
Summarization Results
XLSum
WikiLingua
WikiHowSumm
MLSum
Avg.
Aya-Expanse-32B
21.4
21.5
16.6
30.1
22.4
Aya-23-35B
13.3
18.4
12.7
25.9
17.6
Llama-3.3-70B-Instruct
16.3
12.0
8.5
28.1
16.2
Llama-3-8B-Instruct
13.5
8.1
7.9
25.8
13.8
Llama-3.1-8B-Instruct
12.4
7.9
7.9
25.8
13.5
Llama-3.1-8B
12.4
7.9
7.9
25.8
13.5
Qwen2.5-14B
13.1
6.8
6.6
25.7
13.0
Ministral-2410-8B-Instruct
13.8
6.9
6.7
24.0
12.8
Qwen2.5-14B-Instruct
15.7
7.1
4.7
23.7
12.8
Qwen2.5-7B
12.3
6.9
6.6
25.3
12.8
Aya-23-8B
14.1
11.4
1.7
24.0
12.8
Llama-3-8B
11.1
6.6
6.6
25.0
12.3
Qwen2.5-3B
11.4
6.5
6.5
24.9
12.3
Aya-Expanse-8B
13.3
13.4
0.5
21.4
12.2
Llama-3.2-3B
12.0
6.4
6.5
23.3
12.1
Qwen2.5-3B-Instruct
12.0
6.6
6.8
22.7
12.0
Qwen2.5-5B-Instruct
11.0
6.1
6.3
24.6
12.0
Qwen2.5-5B
11.9
5.9
6.3
24.0
12.0
Qwen2.5-5B
9.2
5.6
6.1
24.3
11.3
Mistral-v0.3-7B-Instruct
10.9
6.2
3.7
24.1
11.2
Qwen2.5-7B-Instruct
11.6
6.3
5.8
20.5
11.0
Kanarya-2B
9.3
4.5
5.3
24.7
10.9
Mixtral-v0.1-7B-Instruct
10.6
6.0
4.9
22.2
10.9
Qwen2.5-5B-Instruct
9.0
5.0
5.8
22.9
10.7
Commencis-7B
9.5
6.3
7.2
16.1
9.8
Llama-3.2-3B-Instruct
6.7
4.1
6.6
14.8
8.1
Mistral-v0.3-7B
6.3
6.0
1.9
17.3
7.9
Llama-3.2-1B
7.2
3.5
5.9
13.4
7.5
Turna-1B
6.1
5.6
5.7
11.0
7.1
Trendyol-v1.0-7B-Base
5.0
2.9
4.6
8.8
5.3
Mistral-v0.1-7B
1.2
6.0
1.1
6.3
3.6
Cere-Llama-3-8B
0.6
2.1
5.2
6.0
3.5
Aya-101-13B
0.1
0.0
0.0
0.3
0.1
Table 8: Summarization results of the models, sorted by their average scores. Shapes represent the model
architectures: an inverted triangle for Lllama, a star for Aya, a circle for Qwen, a triangle for T5, and a pentagon for
GPT-J. Colors indicate the language focus of the models: blue for English-focused, yellow for multilingual-focused,
and red for Turkish-focused models.
20

--- Page 21 ---

B.8
Text Classification Results
STSb
OffensEval
NewsCat
IronyTR
Avg.
Llama-3.3-70B-Instruct
12.9
83.1
78.0
58.2
58.1
Aya-Expanse-32B
21.5
67.1
82.8
50.0
55.3
Qwen2.5-7B
17.0
77.4
54.8
57.3
51.6
Qwen2.5-7B-Instruct
18.3
80.3
40.0
55.0
48.4
Kanarya-2B
12.9
61.6
66.8
50.0
47.8
Mixtral-v0.1-7B-Instruct
13.0
62.9
54.0
52.5
45.6
Aya-23-8B
23.0
34.2
72.4
51.7
45.3
Llama-3.1-8B
17.0
34.6
69.2
58.5
44.8
Cere-Llama-3-8B
22.1
34.0
68.4
50.2
43.7
Llama-3.2-1B
17.1
46.7
58.0
52.8
43.7
Aya-Expanse-8B
21.0
26.8
76.0
50.5
43.6
Qwen2.5-14B-Instruct
24.9
54.7
32.4
61.3
43.3
Mistral-v0.3-7B-Instruct
12.9
45.2
61.2
50.7
42.5
Aya-101-13B
17.0
79.9
20.0
52.2
42.3
Trendyol-v1.0-7B-Base
15.5
20.3
81.2
50.0
41.8
Llama-3-8B-Instruct
14.2
30.8
62.8
54.5
40.6
Llama-3-8B
16.4
21.9
72.4
51.5
40.6
Qwen2.5-3B
12.9
48.4
44.8
54.7
40.2
Llama-3.1-8B-Instruct
19.6
23.6
66.0
51.3
40.1
Commencis-7B
14.9
24.3
62.4
56.0
39.4
Llama-3.2-3B
13.2
25.4
66.4
50.0
38.7
Aya-23-35B
25.4
21.0
55.6
50.2
38.0
Ministral-2410-8B-Instruct
21.4
20.3
60.4
50.0
38.0
Qwen2.5-14B
20.4
22.0
52.4
56.2
37.7
Mistral-v0.3-7B
14.2
20.7
66.0
49.8
37.7
Mistral-v0.1-7B
13.6
20.5
65.2
50.2
37.3
Llama-3.2-3B-Instruct
12.9
20.6
64.0
50.2
36.9
Turna-1B
14.2
51.0
32.8
48.3
36.6
Qwen2.5-3B-Instruct
16.8
37.6
37.2
51.3
35.7
Qwen2.5-5B
12.9
27.4
48.4
52.3
35.3
Qwen2.5-5B-Instruct
12.9
20.7
48.8
49.7
33.0
Qwen2.5-5B
12.9
33.7
26.8
49.3
30.7
Qwen2.5-5B-Instruct
13.1
21.4
29.2
47.3
27.8
Table 9: Text classification results of the models, sorted by their average scores. Shapes represent the model
architectures: an inverted triangle for Lllama, a star for Aya, a circle for Qwen, a triangle for T5, and a pentagon for
GPT-J. Colors indicate the language focus of the models: blue for English-focused, yellow for multilingual-focused,
and red for Turkish-focused models.
21

--- Page 22 ---

C
Task Samples
This appendix section includes sample instances
for all tasks & datasets included within CETVEL.
Belebele
Tüm notalara do˘gru ¸sekilde basmaya devam
ederken elinizin mümkün oldu˘gu kadar rahat
oldu˘gundan emin olun - aynı zamanda par-
maklarınızla fazladan hareketler yapmamaya
çalı¸sın. Bu ¸sekilde kendinizi olabildi˘gince az
yormu¸s olacaksınız. Unutmayın ki piyanoda
oldu˘gu gibi daha fazla ses için tu¸slara çok
güçlü vurmanıza gerek yoktur. Akordeon üz-
erinde, ekstra hacim elde etmek için körü˘gü
daha fazla basınç veya hızda kullanırsınız.
Metne göre, hangisi akordeonu ba¸sarılı bir ¸sek-
ilde çalmak için uygun bir tavsiye de˘gildir?
A. Daha fazla ses çıkarmak için tu¸slara daha
güçlü basın
B. Yorulmamak için gereksiz hareketleri en
aza indirin
C. Eliniz rahat pozisyondayken notalara
do˘gru ¸sekilde basın
D. Ekstra ses elde etmek için körü˘gü daha
hızlı kullanın
English Translation
While continuing to press all the notes cor-
rectly, make sure your hand is as relaxed as
possible – at the same time, try not to make
extra movements with your fingers. This way,
you will tire yourself as little as possible. Re-
member that, just like on the piano, you don’t
need to hit the keys very hard to produce more
sound. On the accordion, to achieve extra vol-
ume, you use the bellows with more pressure
or speed.
According to the text, which of the following
is *not* an appropriate piece of advice for
playing the accordion successfully?
A. Press the keys harder to produce more
sound
B. Minimize unnecessary movements to
avoid fatigue
C. Press the notes correctly while keeping
your hand relaxed
D. Use the bellows faster to achieve extra vol-
ume
BilmeceBench
Bilmece: Kuyruklu kumbara yemek ta¸sır am-
bara.
Bilmecenin anlamı a¸sa˘gıdakilerden hangi-
sidir?
A. BALTA
B. ARMUT
C. KA¸SIK
D. AYAKKABI
English Translation
Riddle: A piggy bank with a tail carries food
to the storage.
What is the meaning of the riddle?
A. AXE
B. PEAR
C. SPOON
D. SHOE
Circumflex
Kelime: Hakim
Kelimenin anlamı a¸sa˘gıdakilerden hangisidir?
Cevap:
A. Sıfat: Egemenli˘gini yürüten, buyru˘gunu
yürüten, sözünü geçiren
B. Sıfat: Bilge
English Translation
Word:
Hakim What is the meaning of the word? An-
swer:
A. Adjective: One who exercises authority,
enforces command, and has influence
B. Adjective: Wise
Exams
Glikokortikoidler olarak adlandırılan hormon-
lar nerede sentezlenirler:
A. tiroid bezinde.
22

--- Page 23 ---

B. hipofizde.
C. pankreasta.
D. böbrek üstü bezinin kabu˘gunda.
English Translation
Where are the hormones called glucocorti-
coids synthesized:
A. in the thyroid gland.
B. in the pituitary gland.
C. in the pancreas.
D. in the cortex of the adrenal gland.
IronyTR
Cümle: *ODTÜden mezun olmadan yapıla-
cak 100 ¸sey* Madde 101: Pikapla kampüsten
kaçmak
Soru: Bu cümlede ironi var mı?
A. Hayır
B. Evet
English Translation
Sen-
tence: *100 things to do before graduating
from METU* Item 101: Escape the campus
with a pickup truck Question: Is there irony in
this sentence?
A. No
B. Yes
Natural Language Inference
A¸sa˘gıda iki cümle verilmektedir:
Cümle 1: "Evet, sanırım en sevdi˘gim restoran
her zaman en yakın restorandır.
En yakın
olanı biliyorsun. En dü¸sük kriterlere uydu˘gu
sürece."
Cümle 2: "En sevdi˘gim restoranlar her zaman
evimden en az yüz mil uzakta."
Bu iki cümle arasındaki ili¸ski nedir:
A. TUTARLI
B. ALAKASIZ
C. ÇEL˙I¸SK˙IL˙I
English Translation
Below are two sentences:
Sentence 1:
"Yes, I guess my favorite
restaurant is always the closest one. You know
the closest. As long as it meets the lowest
standards."
Sentence 2:
"My favorite restaurants are
always at least a hundred miles away from my
home."
What is the relationship between these
two sentences?
A. ENTAILMENT
B. NEUTRAL
C. CONTRADICTION
NewsCat
Cümle: Hırsız, Hietanen’in ba¸sını yaktı DEN˙I-
ZL˙ISPORLU Hietanen’i hırsız yaktı. Porto
maçı için kampta oldu˘gu saatte evine giren
hırsız, yatak odasına geçip, içki içti. E¸si Ri-
iena eve döndü˘günde yata˘gı da˘gınık görünce,
"Bana kampta oldu˘gunu söylüyorsun, eve
kadın getiriyorsun" diyerek ayrılmak istedi.
Rıza Çalımbay’dan izin alan futbolcu, e¸sini
ikna etti.
...
Soru: Bu cümlenin konusu nedir?
Cevap:
A. spor
B. magazin
C. siyaset
D. sa˘glık
E. ekonomi
English Translation
Sentence: The thief got Hietanen in trouble.
The thief caused trouble for Denizlispor player
Hietanen. While he was at camp for the Porto
match, a thief entered his home, went into the
bedroom, and drank alcohol. When his wife
Riiena returned home and saw the bed messy,
she said, "You tell me you’re at camp, but you
23

--- Page 24 ---

bring a woman home," and wanted to leave
him. The footballer got permission from Rıza
Çalımbay and convinced his wife.
...
Question: What is the topic of this sentence?
Answer:
A. sports
B. celebrity news
C. politics
D. health
E. economy
OffenseEval
Cümle: Hala Hogwarts mektubum gelmedi˘gin-
den oluyor tüm bunlar.
Soru: Bu cümle nefret söylemi içermekte
midir?
A. Hayır
B. Evet
English Translation
Sentence: All of this is happening because I
still haven’t received my Hogwarts letter.
Question: Does this sentence contain hate
speech?
A. No
B. Yes
STSb
A¸sa˘gıda iki cümle verilmektedir:
Cümle 1: "Bir kız saçlarını ¸sekillendirmekte."
Cümle 2: "Bir kız saçını fırçalıyor."
Bu iki cümle arasında ne kadar benzer-
lik vardır:
A. Benzerlik Yok
B. Dü¸sük Benzerlik
C. Orta Benzerlik
D. Yüksek Benzerlik
E. Çok Yüksek Benzerlik
F.
Mantıksal Olarak Aynı
English Translation
Below are two sentences:
Sentence 1: "A girl is styling her hair."
Sentence 2: "A girl is brushing her hair."
How similar are these two sentences?
A. No Similarity
B. Low Similarity
C. Moderate Similarity
D. High Similarity
E. Very High Similarity
F.
Logically Equivalent
TQUAD
Kaynak: Kemaleddin ibn Yunus ya da Musa
ibn Yunus (do˘gum yılı ve yeri: 1156 Musul
- ölüm yılı ve yeri: 1241 Musul).Astronom,
matematikçi ve ˙Islam bilgini.Tam adı Musa
bin Yunus bin Muhammed bin Men’a’dır,
Künyesi ise Ebu’l-Feth’tir, lakabı Kemaleddin
olup ayrıca ˙Ibn-i Yunus ve Mewsilî diye
de bilinir.˙Ilk e˘gitimini babası ¸Seyh Yunus
Rızauddin’in yanında fıkıh ve hadis ilimleri
ö˘grendi,
ardından Ba˘gdat’taki Nizamiye
Medreseleri’nde okumaya devam etti. Burada
¸Serafeddin el-Tusî’den matematik derslerini
aldı, ardından Batlamyus’un Almagest adlı
eserini de ö˘grenir. Ardından Musul’a döndü,
Emir Zeyneddin Camii’nde dersler verdi.
˙Ilim ö˘gretmeye elveri¸sli olarak in¸sa edilen
bu cami Kemaliyye Medresesi olarak anıldı.
Kısa zamanda ¸söhreti etrafa yayılan Musa
Kemaleddin ibn Yunus pek çok çevreden
gelen talebelere ilim ö˘gretti.
Soru:
Kemaleddin
ibn
Yunus
lakabı
dı¸sında hangi isimlerle bilinir?
Cevap:
˙Ibn-i Yunus ve Mewsilî
English Translation
Source: Kemaleddin ibn Yunus or Musa ibn
24

--- Page 25 ---

Yunus (born 1156 Mosul – died 1241 Mosul).
Astronomer,
mathematician,
and Islamic
scholar. His full name is Musa bin Yunus
bin Muhammad bin Men’a; his kunyah is
Abu’l-Feth, his laqab is Kemaleddin, and he
is also known as ˙Ibn-i Yunus and Mewsilî.
He received his initial education in fiqh
and hadith from his father, Sheikh Yunus
Rızauddin, then continued at the Niz¯amiyya
Madrasas in Baghdad, studying mathematics
under Sharaf al-Din al-Tusi and learning
Ptolemy’s Almagest. He returned to Mosul
and taught at the Zayn al-D¯ın Mosque, also
called the Kemaliyye Madrasa, gaining fame
and attracting many students.
Question: Aside from the laqab Kemaleddin
ibn Yunus, by what other names is he known?
Answer:
˙Ibn-i Yunus ve Mewsilî
Turkce Atasozleri
Atasözü: aba altında er yatar
Yukarıdaki atasözünün tanımı a¸sa˘gıdakilerden
hangisidir?
A. Giyim ku¸sam ki¸sili˘ge ölçü olamaz.
B. Tanrı’dan korkmayan kimse, insana her
türlü kötülü˘gü yapabilir.
C. ˙Insan kendinde herhangi bir kusur varken
ba¸skalarını aynı kusurla suçlamamalıdır.
D. Ortaya çıkan bir yanlı¸slık çok geç de olsa
düzeltilebilir.
English Translation
Proverb: Beneath a coarse cloak may lie a
noble man What is the meaning of the proverb
above?
A. Clothing and appearance are not reliable
measures of character.
B. One who does not fear God is capable of
doing all kinds of harm to others.
C. A person should not accuse others of a
fault they themselves possess.
D. A mistake that has come to light can be
corrected, even if belatedly.
TurkishPLU / Goal Inference
Örnek Adım: ˙I¸sletme adının hemen altındaki
ekranın sa˘g tarafında bulunan "Yer ˙I¸sareti"
dü˘gmesine dokunun. Hedef:
A. Yelp’e ˙I¸sletme Foto˘grafı Eklemek
B. Audacity’de ˙Iz ˙I¸saretleri Eklemek
C. Yelp’te Bir ˙I¸sletmeye Yer ˙I¸sareti Eklemek
D. Yelp’te Yinelenen ˙I¸sletme Giri¸slerini
Bildirmek
English Translation
Example Step: Tap the "Bookmark" button lo-
cated on the right side of the screen just below
the business name. Goal:
A. Add a Business Photo on Yelp
B. Add Track Markers in Audacity
C. Bookmark a Business on Yelp
D. Report Duplicate Business Listings on
Yelp
TurkishPLU / Next Event Prediction
Hedef: Dâhilî Numara Nasıl Aranır? Adım:
Arama cevaplandı˘gı anda dâhilî numarayı gire-
ceksen bir "duraklama" ekle. Bir sonraki adım:
A. E˘ger dâhilî numara sadece tüm menü oy-
natıldıktan sonra çevrilebiliyorsa bir "bek-
leme" ekle.
B. daha önce yapmadıysan, gizli Geli¸stirici
Seçenekleri butonunu görüntülemek için
seri numarana 7 kez dokun.
C. Ekran görüntüsünü Command ve V
tu¸slarını basılı tutarak veya Düzenle
menüsünden Yapı¸stır’ı seçerek bir kelime
i¸sleme belgesine, bir e-postaya veya bir
görüntü düzenleyiciye yapı¸stır.
English Translation
Goal: How to Dial an Extension Number?
Step: If you’ll enter the extension as soon as
the call is answered, insert a “pause.” Next
step:
A. If the extension can only be dialed after
the full menu has played, insert a “wait.”
25

--- Page 26 ---

B. If you haven’t done so already, tap your
serial number 7 times to reveal the hidden
Developer Options button.
C. Paste the screenshot into a word process-
ing document, an email, or an image ed-
itor by holding down the Command and
V keys or selecting Paste from the Edit
menu.
TurkishPLU / Step Inference
Hedef: Obsesif Kompulsif Ki¸silik Bozuklu˘gu
Nasıl Tanınır? Örnek Adım:
A. VPN’in sınırlamalarını bil.
B. Hedef SGPT seviyenin ne oldu˘gunu bil.
C. SNM’nin prensiplerini benimse.
D. OKKB’nin tanı kriterini bil.
English Translation
Goal:
How
to
Recognize
Obsessive-
Compulsive Personality Disorder (OCPD)?
Example Step:
A. Know the limitations of your VPN.
B. Know what your target SGPT level is.
C. Adopt the principles of SNM.
D. Know the diagnostic criteria for OCPD.
TurkishPLU / Step Ordering
Hedef: Tarayıcınızı Güncellemek
A. Önce:
Tarayıcıya
uygulanmasını
istedi˘giniz tüm Internet Explorer gün-
cellemelerinin yanına bir onay i¸sareti
koyun.
Sonra:
Internet Explorer için
herhangi bir güncelleme olup olmadı˘gını
görmek için güncelleme listesini gözden
geçirin.
B. Önce:
Internet Explorer için herhangi
bir güncelleme olup olmadı˘gını görmek
için güncelleme listesini gözden geçirin.
Sonra:
Tarayıcıya
uygulanmasını
istedi˘giniz tüm Internet Explorer gün-
cellemelerinin yanına bir onay i¸sareti
koyun.
English Translation
Goal: Updating Your Browser
A. First: Place a check mark next to all Inter-
net Explorer updates you want to apply to
the browser. Then: Review the update list
to see if there are any updates for Internet
Explorer.
B. First: Review the update list to see if
there are any updates for Internet Explorer.
Then: Place a check mark next to all Inter-
net Explorer updates you want to apply to
the browser.
TurkishMMLU
220 V gerilimle çalı¸san ve direnci 484 Ωolan
bir klima günde 5 saat süreyle çalı¸stırılıyor.
Elektrik enerjisinin kWh’i 40 kuru¸s oldu˘guna
göre klimanın harcadı˘gı 30 günlük enerji be-
deli kaç ’dir?
A. 4
B. 5
C. 6
D. 10
E. 15
English Translation
A 220 V air conditioner with a resistance of
484 Ωis operated for 5 hours per day. Given
that the cost of 1 kWh of electricity is 40 kuru¸s,
what is the energy cost in
for 30 days of use?
A. 4
B. 5
C. 6
D. 10
E. 15
XCOPA
Ürün balonlu naylonla paketlenmi¸sti bu yüz-
den
A. kırılgandı.
26

--- Page 27 ---

B. küçüktü.
English Translation
Sentence: The product was packaged with bub-
ble wrap, so
A. it was fragile.
B. it was small.
XQUAD
Kaynak: Akademi Ödülü kazananı Marlee
Matlin Amerikan ˙I¸saret Dili(ASL) çevirisini
yaparken altı kez Grammy kazanan ve
Akademi Ödülü adayı Lady Gaga ulusal mar¸sı
söylemi¸stir.
Soru:
Lady Gaga kaç Grammy kazan-
mı¸stır?
Cevap: altı
English Translation
Source:
Academy Award winner Marlee
Matlin performed the American Sign Lan-
guage (ASL) interpretation while six-time
Grammy winner and Academy Award nomi-
nee Lady Gaga sang the national anthem.
Question:
How
many
Grammys
has
Lady Gaga won?
Answer: six
GECTurk
Verilen cumlenin yazım hatalarını duzeltin.
Hatalı Cümle: Büyük yıldızlar transfer ederek,
ya’da büyük hocalar getirerek hokus pokus
ba¸sarıların
gelmedi˘gi
gerçe˘ginin
farkına
vardılar.
Düzeltilmi¸s hali:
Büyük yıldızlar trans-
fer ederek, ya da büyük hocalar getirerek
hokus pokus ba¸sarıların gelmedi˘gi gerçe˘ginin
farkına vardılar.
English Explanation
In Turkish, the coordinating conjunction "ya
da" ("or") is always written as two separate
words without an apostrophe.
MLSum
Ba¸slık: ˙Izmir’deki orman yangınının tehdit
etti˘gi oteller tahliye edildi
Metin:
˙IZM˙IR’in Menderes ilçesindeki
tatil beldesi Özdere’de otluk alanda yangın
çıktı.
Dumanların etkiledi˘gi iki otel ise
bo¸saltıldı. ˙Izmir’in tatil beldelerinden Özdere
Cumhuriyet Mahallesindeki otluk alanda
yangın çıktı. Çıkan yangını söndürmek için
38 arazöz ve 4 dozer aralıksız olarak çalı¸s-
malarını sürdürüyor. Öte yandan dumanların
etkiledi˘gi iki otel bo¸saltıldı. Helikopter kul-
lanılamıyor Menderes Belediyesi tarafından
yapılan açıklamada, "Menderes Belediyesi
ekipleri olarak ilk müdahaleyi gerçekle¸stirdik.
˙Izmir Büyük¸sehir Belediyemizle de irtibata
geçerek ˙IZSU ve ˙Izmir itfaiyemiz hemen
yangın
alanında
müdahaleye
ba¸sladılar.
˙Izmir Orman Bölge Müdürlü˘gümüze ba˘glı
ekipler de yangın söndürme çalı¸smalarını
gerçekle¸stiriyorlar. Havanın karanlık olması
nedeniyle uçak ve helikopter ile yangına
müdahale gerçekle¸stirilemiyor.
¸Su an yol
trafi˘ge kapatılmı¸s durumda. Gümüldür yolu
üzerinden ve Ahmetbeyli yolu üzerinden araç
trafi˘gi verilmekte. Rüzgarın etkisi çalı¸smaları
zorla¸stırsa da ekipler canla, ba¸sla yangını
kontrol altına almaya çalı¸sıyorlar. Umarız en
kısa sürede yangını kontrol altına alabiliriz.
Ne yazık ki milli servetimiz, ci˘gerlerimiz
yanıyor. Bir an önce bu felaketin son bulması
için canla, ba¸sla çalı¸sıyoruz" denildi.
Özet:
˙IZM˙IR’in Menderes ilçesi Özdere bölgesin-
deki
ormanlık
alanda
elektrik
tellerinin
sürtünmesi
sonucu
orman
yangını
çıktı.
Alevlerin
tehdit
etti˘gi
bölgede
bulunan
otellerde konaklayanlar, ekipler tarafından
tahliye edildi.
English Translation
Title: Hotels threatened by the forest fire in
˙Izmir evacuated
Text:
A fire broke out in a grassy area
27

--- Page 28 ---

in Özdere, a holiday resort in the Menderes
district of ˙Izmir. Smoke affected two hotels,
which were evacuated. To extinguish the fire,
38 fire trucks and 4 bulldozers have been
working nonstop.
Menderes Municipality
teams performed the first intervention, and
˙Izmir Metropolitan Municipality’s water and
fire departments joined the efforts.
Teams
from the ˙Izmir Forestry Regional Directorate
are also fighting the blaze. Due to darkness,
aircraft and helicopters cannot be used. Roads
are closed to traffic, with vehicles rerouted
via the Gümüldür and Ahmetbeyli roads.
Despite challenging winds, teams are striving
to bring the fire under control.
“Our na-
tion’s natural treasure is ablaze.” officials said,
urging that the disaster end as soon as possible.
Summary:
A fire broke out in a grassy area in Özdere,
Menderes district of ˙Izmir. Guests at hotels
threatened by the flames were evacuated by
response teams.
XLSum
Ba¸slık: ’˙Iklim de˘gi¸sikli˘gi penguenleri tehdit
ediyor’
Metin:
ABD’li,
˙Ingiliz
ve
Hollandalı
ara¸stırmacılar tarafından yürütülen ve iklim
de˘gi¸sikli˘ginin penguenler üzerindeki etkisini
konu alan çalı¸sma, "Nature Climate Change"
adlı bilimsel dergide yayımlandı. Makalede,
"Büyük penguen" olarak da anılan ve Antar-
tika’da ya¸sayan bu ku¸s türüne yönelik asıl
tehdidin deniz-buz oranındaki de˘gi¸simden
iddia edildi. Buna göre Antartika’daki buz
ve su oranı de˘gi¸sirse, penguenlerin ço˘gal-
maları ve beslenmeleri olumsuz etkilenecek.
Çalı¸sma, penguen grupları arasında farklı
dinamiklerin etkili olaca˘gını ancak yine de
tüm gruplarda sayının azalaca˘gını savunuyor.
Ara¸stırmacılar, devletlerin penguenleri "nesli
tükenmekte olan ku¸slar" olarak korumaya
alması önerisinde bulundu. Ancak korumaya
yönelik tedbirler, turizm ve balıkçılık alanında
kısıtlamalara neden olabiliyor.
’Neslinin
tükenmesi tehdidi var’ Çalı¸smayı yürüten
ekibin ba¸sında "Woods Hole Oceanographic"
Enstitüsü’nden
Stephanie
Jenouvrier
yer
alıyor.
Doktor Jenouvrier, tüm penguen
nüfusunun yüzde 19 ile 33 arasında bir
oranda azalaca˘gını belirtiyor.
Jenouvrier
penguenlerin "Yakın bir gelecekte önemli
oranda nüfusunu kaybedece˘gini ve muhteme-
len neslinin tükenmesi tehlikesiyle kar¸sı
kar¸sıya kalaca˘gını" söyledi. Antarktika’daki
Ross denizi çevresinde ya¸sayan penguen
gruplarının iklim de˘gi¸sikli˘ginden en son
etkilenenler olaca˘gını kaydeden Jenouvrier’a
göre bunun sebebi, bölgedeki deniz ve buz
da˘gılımının penguenler için hala elveri¸sli
olması.
Jenouvrier sözlerine ¸söyle devam
etti: "Ross denizinde penguenlerin ya¸sadı˘gı
bölgenin korunması ve geli¸stirilmesi, nesil
tükenmesi tehdidine kar¸sı zaman kazandıra-
caktır.
Böylece sera gazının azaltılması
konusunda gerekli müzakereler yapılabilecek,
stratejiler belirlenebilecektir." Aylarca yol kat
ediyor, yemek arıyorlar Penguenler, yavru-
larını beslemek için aylarca yuvadan uzak,
yemek arıyorlar. Antarktika buzulları boyunca
uzun müsefaler kat eden penguenler, denize
eri¸stikleri yerlerden karides gibi yiyecekler
topluyorlar.
Penguenler yemek ararken
yırtıcı hayvanlardan korunmak gibi çe¸sitli
nedenlerle ideal miktarda buzul tabakaya
ihtiyaç duyuyor. Buzul ve deniz miktarındaki
de˘gi¸simin penguenlerin beslendi˘gi karides
gibi canlıların verimlili˘gini de etkileyece˘gi
belirtiliyor. Penguenlerin ana besin kayna˘gı
olan karides ve benzeri deniz kabuklularının
üremesinin, buzul deniz da˘gılımından etk-
ilendi˘gi ifade ediliyor.
Buzulların artması
karides ve di˘ger kabuklular için olumlu
olarak de˘gerlendiriliyor.
Ancak bu durum,
penguenlerin
denize
ula¸smak
için
daha
uzun mesafe kat etmesi anlamına geliyor.
Uydudan yapılan ölçümlerde, Antartika’da
buzul-su seviyesinin daha önce görülmeyen
bir seviyeye yükseldi˘gi görülüyor.
Ancak
iklim modelleme yazılımları, bu durumun
ileride tersine dönece˘gini belirtiyor.
Özet:
˙Iklim de˘gi¸sikli˘ginin Antarktika’daki penguen
nüfusunu olumsuz etkileyebilece˘gi belirtiliyor.
Yapılan bir çalı¸smaya göre, sayıları 600 bini
bulan penguenlerin 2100 yılı itibariyle be¸ste
28

--- Page 29 ---

biri oranında azalabilece˘gi ifade ediliyor.
English Translation
Title: ’Climate change threatens penguins’
Text:
A study conducted by US, British,
and Dutch researchers on the impact of
climate change on penguins was published
in the scientific journal "Nature Climate
Change." The article states that the main
threat to this bird species, also known as the
“Emperor penguin” living in Antarctica, is
claimed to be changes in the sea–ice ratio.
According to this, if the ratio of ice to water in
Antarctica changes, penguins’ breeding and
feeding will be negatively affected. The study
argues that different dynamics will be at play
among penguin colonies, but that numbers
will decline in all groups. The researchers
recommended that governments list penguins
as “endangered birds.” However, conservation
measures can lead to restrictions in tourism
and fishing. Under the leadership of Stephanie
Jenouvrier from the Woods Hole Oceano-
graphic Institution, the team determined that
the total penguin population will decrease by
between 19% and 33%. Jenouvrier said that
penguins will lose a significant portion of their
population in the near future and may face the
risk of extinction. According to Jenouvrier,
the colonies living around the Ross Sea in
Antarctica will be the last to be affected by
climate change, because the distribution of sea
and ice in that region remains favorable for
penguins. Jenouvrier continued: “Protecting
and enhancing the region where penguins
live in the Ross Sea will buy time against
the threat of extinction.
This will allow
for necessary negotiations and strategies to
reduce greenhouse gases to be developed.”
Penguins travel for months and search for
food to feed their chicks. Penguins traverse
long distances along Antarctic ice, collecting
krill and similar prey from sea access points.
Penguins need an ideal amount of ice shelf
for various reasons, such as protection from
predators while foraging. Changes in ice and
sea levels will also affect the productivity
of krill and other crustaceans that penguins
eat. An increase in ice benefits krill and other
crustaceans, but forces penguins to travel
longer distances to reach the sea. Satellite
measurements show that the ice–water ratio in
Antarctica has reached unprecedented levels.
However, climate models predict this trend
will reverse in the future.
Summary:
It is stated that climate change could
negatively affect the penguin population
in Antarctica.
According to a study, the
population of around 600,000 penguins could
decrease by one fifth by 2100.
WikiHowSum
Metin: Yatabilece˘gin en do˘gal uyku pozisy-
onunda uzan.
Bir¸sey tutma, bacaklarını
yatakta tut, ba¸sını kaldırma. E˘ger normalda
sırt üstü uyuyorsan numaradan uyurken de
öyle yap.
Böylece seni tanıyan insanlar
¸süphelenmez. Do˘gal uykunda çok az hareket
edersin.
Gerçekten uyuyormu¸s izlenimi
yaratmak için en iyisi hiç hareket etmemek.
Biri seni uzun bir süre boyunca izlemedi˘gi
sürece hareket etmen beklenmez.
Göz
kapaklarını
fazlaca
sıkarak
kapatmaktan
kaçın.
En iyi uyuyor izlenimi için, göz
kapakların dâhil tüm kaslarının rahat olmalı.
Gözlerini kapattıktan sonra göz kapaklarının
kırpı¸smasını engellemek için a¸sa˘gı do˘gru
bak. Uyurken gözlerin her zaman tam kapalı
olmaz.
Göz kapaklarının dü¸serek nazikçe
kapanmasına izin ver; hâlâ göz kapaklarının
arasından etrafı biraz görebilirsin. Yava¸s, hatta
derin nefesler al. Nefes almanı rahatlatmalı
ve mümkün oldu˘gunca e¸sit aralıklarla nefes
alıp vermelisin.
Nefes alırken kafandan
sayıp, aynı sürede vermeye çalı¸s. Bunu her
nefesinde yap. E˘ger yüksek bir ses duyarsan
ya da biri sana dokunursa kısa ve ani bir
nefes al ve vücudunu hafifçe titret. Uyurken
bile, vücutlarımız etrafımızda olan ¸seylerin
farkındadır. Sahte uykunu, odadaki seslere
ve hareketlere bilinçsiz görünen tepkiler
ekleyerek sat. Rahatsızlı˘ga tepki verdikten
sonra, vücudunun gev¸semesine ve nefesinin
yava¸s ve dengeli bir duruma dönmesine izin
ver.
Sakın gülümseme ve gözlerini açma,
yoksa aslında uyanık oldu˘gun hemen anla¸sılır.
29

--- Page 30 ---

Özet:
Do˘gal
bir
uyku
pozisyonu
seç.
Yatakta hareketsiz bir ¸sekilde yat. Gözlerini
nazikçe kapat. Ritmik bir ¸sekilde nefes alıp
ver. Seslere ve dokunmaya tepki ver.
English Translation
Text: Lie in the most natural sleep position
possible.
Don’t hold anything, keep your
legs on the bed, don’t lift your head.
If
you normally sleep on your back, do so
here as well. That way, people who know
you won’t suspect. You move very little in
natural sleep.
To create the impression of
truly sleeping, it’s best not to move at all. As
long as no one watches you for a long time,
movement isn’t expected. Avoid squeezing
your eyelids tightly shut. For the best sleeping
impression, all your muscles—including your
eyelids—should be relaxed.
After closing
your eyes, look downward to prevent eyelid
twitching. Eyes are never fully closed when
sleeping. Allow your eyelids to fall gently and
close; you can still see a little through them.
Breathe slowly, even deeply. Your breathing
should be relaxed and at as equal intervals as
possible. Count in your head as you inhale,
and try to exhale in the same time. Do this
with each breath. If you hear a loud noise or
someone touches you, take a short, sudden
breath and slightly shake your body. Even
during sleep, our bodies are aware of things
around us. Sell your fake sleep by adding
unconscious-seeming reactions to sounds
and movements in the room. After reacting,
allow your body to relax and your breathing to
return to a slow, balanced state. Never smile
or open your eyes, or it will immediately
reveal you are actually awake.
Summary: Choose a natural sleep position.
Lie motionless on the bed.
Gently close
your eyes. Breathe rhythmically. Respond
to sounds and touch.
WMT16EN-TR
Translate English to Turkish.
English:
Norway’s rakfisk:
Is this the
world’s smelliest fish?
Turkish: Norveç’in rakfisk’i: Dünyanın en
kokulu balı˘gı bu mu?
30

--- Page 31 ---

Language Understanding Tasks
Task
Dataset
Source / Domain
License
#examp.
Metric
Extractive
Question Answering
XQUAD
Wikipedia
CC BY-SA 4.0
1190
Exact Match
TQUAD
Wikipedia
MIT
892
MKQA
Wikipedia
CC BY-SA 3.0
10000
Multiple Choice
Question Answering
Exams
High School Exams
CC-BY-SA 4.0
393
Accuracy
Belebele
Online Web Pages
CC-BY-SA 4.0
900
TurkishPLU
WikiHow
CC BY-NC-SA 3.0
3124
XCOPA
Crowd Sourcing
CC-BY-SA 4.0
600
TurkishMMLU
High School Exams
-
900
Proverbs
Turkish Dictionaries
GPL-3.0
1730
BilmeceBench
Turkish riddles
MIT
442
CircumflexTR
Turkish Dictionaries
MIT
72
Text Classification
IronyTR
Twitter
-
600
Accuracy
NewsCat
Online Newspapers
-
250
OffensEval
Twitter
CC BY-SA 2.0
3528
STSb
Multi-Domain
CC BY-SA 4.0
1389
Natural Language Inference
XNLI
SNLI & MNLI
CC BY 4.0
5010
Accuracy
MNLI
Crowd Sourcing
CC BY-SA 3.0
10000
SNLI
Image Captions
CC BY-SA 4.0
10000
Language Generation Tasks
Task
Dataset
Source / Domain
License
#examp.
Metric
Summarization
MLSum
Online Newspapers
Other
12775
ROUGE-2
XLSum
BBC News
CC BY-NC-SA 4.0
3400
WikiLingua
WikiHow
CC BY-NC-SA 3.0
3000
Machine Translation
WMT16EN-TR
Online Newspapers
-
3000
BLEU-4
Grammatical Correction
GECTurk
Newspapers
Apache-2.0
20800
Exact Match
Table 10: The overview of the tasks & datasets included in the CETVEL benchmark. Most of the listed datasets are
the Turkish splits of a larger multilingual dataset with few exceptions which are TurkishPLU, TQUAD, IronyTR,
NewsCat and GECTurk.
31

```
