---
title: "2025-Mikhailov-NorEval A Norwegian Language Understanding and Generation Evaluation - PDF Extract"
source_pdf: "2025-Mikhailov-NorEval A Norwegian Language Understanding and Generation Evaluation.pdf"
pages: 47
extracted_at: "2026-02-13T13:14:07.896928"
---

# PDF Extract: 2025-Mikhailov-NorEval A Norwegian Language Understanding and Generation Evaluation

**Source PDF:** 2025-Mikhailov-NorEval A Norwegian Language Understanding and Generation Evaluation.pdf
**Total Pages:** 47

---

## Content

```
--- Page 1 ---

arXiv:2504.07749v2  [cs.CL]  5 Jun 2025
NorEval: A Norwegian Language Understanding and Generation
Evaluation Benchmark
Vladislav Mikhailov1
Tita Enstad2
David Samuel1
Hans Christian Farsethås1
Andrey Kutuzov1
Erik Velldal1
Lilja Øvrelid1
1University of Oslo
2National Library of Norway
Correspondence: vladism@ifi.uio.no
Abstract
This paper introduces NorEval, a new and com-
prehensive evaluation suite for large-scale stan-
dardized benchmarking of Norwegian gener-
ative language models (LMs). NorEval con-
sists of 24 high-quality human-created datasets
– of which five are created from scratch. In
contrast to existing benchmarks for Norwe-
gian, NorEval covers a broad spectrum of task
categories targeting Norwegian language un-
derstanding and generation, establishes human
baselines, and focuses on both of the official
written standards of the Norwegian language:
Bokmål and Nynorsk. All our datasets and a
collection of over 100 human-written prompts
are integrated into LM Evaluation Harness, en-
suring flexible and reproducible evaluation. We
describe the NorEval design and present the
results of benchmarking 19 open-source pre-
trained and instruction-tuned LMs for Norwe-
gian in various scenarios. Our benchmark, eval-
uation framework, and annotation materials are
publicly available.
1
Introduction
The advancement of language models (LMs) is
inseparable from benchmarking – the systematic
evaluation of their generalization abilities on stan-
dardized datasets across various criteria (Ruder,
2021; Srivastava et al., 2023). Despite its crucial
role, benchmarking in resource-lean scenarios re-
mains scarce due to the lack of diverse evaluation
suites for low-resource languages, including Nor-
wegian (Joshi et al., 2020; Hedderich et al., 2021).
Previous work focuses on Norwegian as part of
medium-scale benchmarking efforts – NorBench
(Samuel et al., 2023) and NLEBench (Liu et al.,
2024) – and broader Mainland Scandinavian eval-
uation initiatives – ScandEval (Nielsen, 2023)
and Scandinavian Embedding Benchmark (SEB;
Enevoldsen et al., 2024). However, these bench-
marks have several shortcomings that limit the
scope of LM evaluation in Norwegian.
• Coverage and design.
These benchmarks
exhibit a significant dataset overlap with a
low variation in task formulations. NorBench
and ScandEval cover traditional NLP tasks,
SEB addresses text embedding evaluation, and
NLEBench comprises a narrow spectrum of
Norwegian language generation tasks.
• Data quality. NLEBench and ScandEval in-
clude machine-translated English datasets, in-
troducing potential evaluation biases that may
conflict with Norwegian-specific values, cul-
ture, and knowledge.
• Linguistic diversity. Norwegian has two of-
ficial written standards: Bokmål (BM) and
Nynorsk (NN; the minority variant). The latter
variant remains significantly underrepresented
in previous work.
• Human performance. No existing benchmark
establishes human baselines, which is a stan-
dard practice to approximate upper LM perfor-
mance bounds.
This paper introduces NorEval, a novel large-scale
evaluation suite designed to benchmark Norwe-
gian LMs on language understanding and genera-
tion tasks. NorEval comprises 24 human-created
datasets across nine task categories, including sen-
timent analysis, Norwegian language knowledge,
Norwegian-specific & world knowledge, machine
reading comprehension, commonsense reasoning,
machine translation, text summarization, instruc-
tion following, and truthfulness. Our design en-
ables various benchmarking scenarios, ranging
from multi-prompt k-shot evaluation to side-by-
side LM comparison on diverse user instructions.
Our main contributions are:
(i) we create
NorEval, the largest multi-task benchmark for Nor-
wegian Bokmål and Nynorsk that combines 19 ex-
isting peer-reviewed datasets with five datasets cre-
ated from scratch; (ii) we curate a collection of

--- Page 2 ---

Evaluation Scope
Task Categories
# Datasets
Method
BM
NN
Total
NorBench
NLU & NLG
POS-tagging, MT,
NER, sentiment analysis,
Acceptability classification, RC
8
2
10
✓
✗
✗
ScandEval
NLU & NLG
NER, sentiment analysis,
Acceptability classification, RC,
Commonsense reasoning,
Text summarization, multiple-choice QA
8
2
10
✓
✓
✗
SEB
Text embedding
evaluation
LID, sentiment analysis,
Acceptability classification, retrieval,
Dialect & written form pairing,
Intent & scenario classification,
Clustering, political speech classification
11
3
14
✓
✗
✗
NLEBench
NLU & NLG
NLI, RC, bias detection,
Text summarization, yes/no QA,
Instruction following,
Paraphrase detection, open-ended conversation
9
✗
9
✗
✓
✓
NorEval
NLU & NLG
Commonsense reasoning,
RC, sentiment analysis,
Norwegian language knowledge, MT,
Truthfulness, text summarization,
Instruction following,
Norwegian-specific & world knowledge
16
8
24
✓
✗
✗
Table 1: Comparison of multi-task benchmarks for Norwegian: ScandEval (Nielsen, 2023), Scandinavian
Embedding Benchmark (SEB; Enevoldsen et al., 2024), NorBench (Samuel et al., 2023), NLEBench (Liu et al.,
2024), and NorEval (ours). BM=Norwegian Bokmål; NN=Norwegian Nynorsk;
=human-created;
=machine-
translated;
= GPT-4o-created & human-edited; NLU=Natural language understanding; NLG=Natural language
generation; NER=named entity recognition; LID=language identification; RC=reading comprehension; NLI=natural
language inference; QA=question answering; MT=machine translation.
over 100 dataset-specific prompts for robust evalu-
ation; (iii) we establish five human baselines; (iv)
we benchmark 19 pretrained and instruction-tuned
Norwegian LMs against each other and humans;
and (v) we release NorEval and our annotation ma-
terials.1
2
Background
Norwegian Bokmål and Nynorsk
BM is the pri-
mary written standard, while an estimated 10–15%
of the Norwegian population uses NN – especially
in Western Norway. The national language legis-
lation specifies that minimally 25% of the written
public service information should be in NN to en-
sure representation of both varieties. While BM
and NN are closely related, they exhibit lexical and
grammatical differences, e.g., distinct pronouns,
plural noun forms, definite noun forms, verb conju-
gation, and vocabulary units. Consider an example
of such differences based on one of our text sum-
marization prompts “Give a brief summary of
the following text: {{article}}” (see §3.2).
1ltgoslo/noreval
• BM. “Gi et kortfattet sammendrag av
følgende tekst: {{article}}”.
• NN. “Gje eit kortfatta samandrag av
følgande tekst: {{article}}”.
We make one of the first attempts to increase the
representation of NN in benchmarking LMs.
Norwegian Benchmarks
Table 1 provides an
overview of existing Norwegian benchmarks w.r.t.
the evaluation scope, task categories, the number
of datasets, coverage of BM and NN, and dataset
creation method. We describe them below.
1. NorBench is primarily designed to benchmark
encoder-only LMs on a collection of ten tradi-
tional NLP tasks, such as PoS-tagging, NER
(NorNE; Jørgensen et al., 2020), sentiment anal-
ysis at different levels of granularity (NoReC;
Velldal et al., 2018; Øvrelid et al., 2020), ac-
ceptability classification (NoCoLA; Jentoft and
Samuel, 2023), machine translation, and extrac-
tive question answering (NorQuAD; Ivanova
et al., 2023). All datasets in NorBench are
human-created; however, the support for NN is

--- Page 3 ---

NorEval
BM, NN
6 task types
9 task categories
24 datasets
100+ prompts
Human-created
Text classification
Sequence-to-sequence generation
Multiple-choice question answering
Sentence-level sentiment analysis
Norwegian language knowledge
Commonsense reasoning
NoReC Sentence (BM)
ASK-GEC (BM)
NorCommonsenseQA (BM/NN)
Document-level sentiment analysis
Machine translation
Norwegian-specific & world knowledge
NoReC Document (BM)
Tatoeba (EN↔BM, EN↔NN)
NorOpenBookQA (BM/NN)
Text summarization
Machine reading comprehension
NorSumm (BM/NN)
Belebele (BM)
Norwegian language knowledge
Instruction following
Truthfulness
NCB (BM)
NorRewrite-IT (BM)
NorTruthfulQA MC (BM/NN)
Generative question answering
Sentence completion
Machine reading comprehension
Truthfulness
Norwegian language knowledge
NorQuAD (BM)
NorTruthfulQA Gen (BM/NN)
NorIdiom (BM/NN)
Sentence ranking
NorSummarize-IT (BM)
NRK-Quiz-QA (BM/NN)
Figure 1: Overview of the NorEval design.
denotes datasets used in the related studies (§2),
represents
datasets not previously included in the existing Norwegian benchmarks, and
denotes our novel datasets introduced
as part of NorEval. EN=English; BM=Norwegian Bokmål; NN=Norwegian Nynorsk.
limited to PoS-tagging and NER based on the
Norwegian UD treebanks (Øvrelid and Hohle,
2016; Velldal et al., 2017).
2. ScandEval is an evaluation suite coupled with
a public leaderboard for Scandinavian lan-
guages: Danish, Faroese, Icelandic, Norwegian,
and Swedish. The Norwegian datasets in Scan-
dEval are based on existing resources, such as
NoReC, NorNE, NorQuAD, and the SNL &
VG summarization dataset (Navjord and Ko-
rsvik, 2023). ScandEval introduces ScaLA,
an acceptability classification dataset created
through rule-based perturbation of sentences
from the Norwegian UD treebanks. Moreover,
its latest version contains machine-translated
English datasets that are not curated or post-
processed:2 MMLU (Hendrycks et al., 2021),
ARC (Clark et al., 2018), XSum (Narayan et al.,
2018), and HellaSwag (Zellers et al., 2019).
Similar to NorBench, the coverage of NN is
limited to the datasets derived from the Norwe-
gian UD treebanks.
3. SEB is designed to evaluate text representations
for Scandinavian languages across retrieval, bi-
text mining, text classification, and clustering
tasks. With its distinct focus on text embed-
ding models, SEB has little overlap with other
Norwegian benchmarks (except for NorQuAD,
ScaLA, and SNL & VG) and primarily con-
2ScandEval has been extended to EuroEval, which sup-
ports existing and machine-translated evaluation resources for
Norwegian: euroeval.com/datasets/norwegian.
structs its evaluation tasks by converting exist-
ing Norwegian resources and leveraging sup-
ported metadata and schemes.
4. NLEBench is designed to evaluate the LM’s
Norwegian language generation capabilities.
Although NLEBench covers various task cat-
egories, it does not address any NN evalua-
tion scenario. Moreover, seven out of nine
datasets are machine-translated without cura-
tion, raising concerns about the benchmark’s
reliability. The remaining two datasets com-
prise multi-turn conversation, closed question
answering (QA), and abstractive summariza-
tion tasks; these are generated by GPT-4o and
edited by Norwegian native speakers.
NorEval expands the scope of benchmarking Nor-
wegian LMs to task categories, datasets, and eval-
uation scenarios that have not been covered in the
related studies, with the main focus on human-
created resources. In particular, only three out
of 24 NorEval datasets are included in NorBench,
ScandEval, SEB, and NLEBench: NorQuAD and
sentence- and document-level NoReC.
3
NorEval
Our main goal is to develop a high-quality stan-
dardized evaluation suite to benchmark Norwegian
generative LMs across a broad spectrum of Norwe-
gian language understanding and generation tasks.
Figure 1 outlines the design of NorEval, which
combines 19 existing peer-reviewed datasets with

--- Page 4 ---

five novel datasets (§3.1), comprises a pool of over
100 prompts (§3.2), and offers a framework for
systematic and reproducible LM evaluation (§3.3).
3.1
Tasks
Appendix A presents an overview of our 24
datasets, including dataset descriptions and exam-
ples, task formulations, prompts, performance met-
rics, and general statistics. Appendix B details
our novel datasets (NCB, NorIdiom, NorRewrite-
instruct, and NorSummarize-Instruct). We describe
NorEval based on nine high-level task categories:
Sentiment analysis focuses on a binary polarity
classification at the sentence- and document-level
(NoReC Sentence & Document).
Norwegian language knowledge assesses an
LM’s capabilities to perform grammatical error
correction (ASK-GEC; Jentoft, 2023), adhere to
language-specific punctuation rules (NCB; ours),
and complete Norwegian idioms (NorIdiom; ours).
Norwegian-specific & world knowledge tests an
LM’s capabilities to answer multiple-choice ques-
tions based on real-world and Norwegian-specific
cultural knowledge (NRK-Quiz-QA and NorOpen-
BookQA; Mikhailov et al., 2025).
Machine reading comprehension evaluates the
capabilities of LMs to answer questions related to
an input text by selecting an answer from multi-
ple choices (Belebele; Bandarkar et al., 2024) or
generating a text span (NorQuAD).
Commonsense reasoning assesses an LM’s capa-
bilities to answer a multiple-choice question based
on logical reasoning and world understanding (Nor-
CommonsenseQA; Mikhailov et al., 2025).
Machine translation tests an LM’s translation ca-
pabilities among four language pairs from Tatoeba
(Tiedemann, 2020): EN ↔BM and EN ↔NN.
Text summarization focuses on abstractive news
summarization (NorSumm; Touileb et al., 2025).
Instruction following evaluates an LM’s capabili-
ties to follow instructions on creative rewriting and
summarization through, e.g., changing a text’s tone
and style, simplifying complex content, and adapt-
ing content for a specific audience (NorRewrite-
Instruct and NorSummarize-Instruct; ours).
Truthfulness tests whether an LM generates or
selects answers that propagate false beliefs and
misconceptions (NorTruthfulQA Multiple Choice
& Generation; Mikhailov et al., 2025).
3.2
Prompts
We conduct a two-stage in-house annotation to cre-
ate a collection of prompts that reflect diverse user
formulations and answer formatting, with four-to-
six prompts per dataset. The prompt examples are
provided in Appendix A, and the annotation guide-
lines are documented in Appendix C.
• Stage 1:
Creating Prompts in Bokmål.
Three Norwegian native speakers create dataset-
specific prompts in BM using two strategies:
(i) manually translating English prompts from
PromptSource (Bach et al., 2022) and (ii) writ-
ing the prompts from scratch.
• Stage 2: Adapting Prompts to Nynorsk. We
hire a BA student in linguistics to adapt the
BM prompts to NN. The hourly pay rate is 227
NOK (approx. $20).
3.3
Evaluation Framework
All our datasets and prompts are integrated into
LM Evaluation Harness (Gao et al., 2024; Bider-
man et al., 2024),3 a framework for flexible evalua-
tion of generative LLMs in various scenarios. The
framework provides a user-friendly API allowing
to easily integrate datasets, configure prompts, and
benchmark LMs that are not part of our baselines.
4
Evaluation Setup
We benchmark a broad range of 19 open-source
pretrained and instruction-finetuned decoder-only
LMs available in Transformers (Wolf et al., 2020;
see Table 2). We compare them in k-shot regimes
against one another and our human baselines, and
evaluate the instruction-finetuned LMs using the
LLM-as-a-judge approach (Zheng et al., 2023).
In-context Learning Evaluation
The evaluation
is run in k-shot regimes with k ∈{0, 1, 16} across
all prompts. We use the maximum k for each
task, which depends on the availability of a train-
ing/development set for demonstration examples
and the example lengths. We use two strategies
supported via LM Evaluation Harness to evaluate
the LM performance in a prompted format:4
• Log-likelihood. The LM assigns a probability
to each answer candidate conditioned on an
3github.com/EleutherAI/lm-evaluation-harness
4Figure 1 outlines our sentence ranking, text classification,
sentence completion, sequence-to-sequence generation, and
multiple-choice and generative QA tasks.

--- Page 5 ---

Name
Base
PRETRAINED LMS
Mistral-7B
N/A
Mistral-Nemo-12B
N/A
Meta/Llama-3-8B
N/A
NB-GPT-6B
N/A
NorwAI-Mistral-7B
Mistral-7B
NorwAI-Llama2-7B
Llama-2-7B
GPT-SW3-6.7B
N/A
AI-Sweden/Llama-3-8B
Meta/Llama-3-8B
Viking-7B
N/A
Viking-13B
N/A
NorBLOOM-7B-scratch
N/A
NorMistral-7B-scratch
N/A
NorMistral-7B-warm
Mistral-7B
NorMistral-11B-warm
Mistral-Nemo-12B
INSTRUCTION-TUNED LMS
NorMistral-7B-warm-IT
NorMistral-7B-warm
Mistral-7B-IT
Mistral-7B
AI-Sweden/Llama-3-8B-IT
AI-Sweden/Llama-3-8B
Meta/Llama-3-8B-IT
Meta/Llama-3-8B
Mistral-Nemo-12B-IT
Mistral-Nemo-12B
Table 2:
The LMs used in our work and their
base versions.
LM references: Mistral-7B (Jiang
et al., 2023), NorBLOOM/NorMistral-7B-scratch &
Normistral-7B/11B-warm (Samuel et al., 2025), and
Meta/Llama-3-8B (Dubey et al., 2024).
input prompt, and the most probable candidate
is selected as the prediction. This strategy is
used in the sentence ranking, text classification,
and multiple-choice QA tasks.
• Generation. The LM generates a text continu-
ation conditioned on an input prompt. We use
a greedy search decoding method for the pre-
trained LMs and recommended HuggingFace
inference hyperparameters and chat templates
for the instruction-tuned LMs. This strategy is
used in the sentence completion, sequence-to-
sequence generation, and generative QA tasks.
Performance Aggregation
We use a combina-
tion of performance aggregation methods based on
well-established NLP benchmarking practices and
theoretical foundations of the social choice theory
(Arrow, 2012).
• Multi-prompt Aggregation. We select the
highest performance score for each LM across
task-specific prompts to mitigate the prompt
sensitivity (Voronov et al., 2024).
Dataset
WAWA
NCB
92.0
NorOpenBookQA (BM)
98.0
NorCommonsenseQA (BM)
93.3
NorTruthfulQA Multiple Choice (BM)
86.0
Belebele
86.7
Table 3: The WAWA rates for human baselines (§4).
• Average Normalized Score. In line with the
OpenLLM leaderboard (Fourrier et al., 2024)
and FineWeb2 evaluation protocol (Penedo
et al., 2024), we first rescale individual per-
formance scores across our nine task cate-
gories. Rescaling involves score normalization
between the random baseline and the maximum
possible score. We then compute the overall
performance score by averaging the normalized
scores within all task categories.
• Borda’s Count. Recent works demonstrate
the effectiveness of using Borda’s count as
an alternative to arithmetic mean aggregation
in multi-task benchmarking (Colombo et al.,
2022; Rofin et al., 2023). This approach re-
lies on a scoring vector c = (|M| −1, |M| −
2, . . . , 1, 0) to assign scores to a set of M LMs
m ∈{m1, . . . , m|M|} based on their posi-
tions in each task- and metric-specific rank-
ing. The final score is calculated as the sum
of corresponding scores in each task Sc(m) =
P|M|
i=1 cipi(m), where pi(m) is the number of
tasks in which LM m takes the ith place, and ci
is the ith element of c. Borda’s count allows for
aggregating heterogeneous performance met-
rics while accounting for the differences in the
LMs’ ranking positions.
Human Baselines
We establish five human base-
lines on random subsets of 50 examples from
NCB, Belebele, NorOpenBookQA (BM), NorCom-
monsenseQA (BM), and NorTruthfulQA Multiple
choice (BM). Our annotation team consists of 12
volunteers, all Norwegian native speakers with an
NLP background and completed higher academic
degrees. Before starting, the annotators receive
guidelines describing the tasks and providing ex-
amples with explanations (see Appendix D). Each
example is annotated by three annotators, and we
use majority voting to aggregate their results. Ta-
ble 3 summarizes the inter-annotator agreement

--- Page 6 ---

Model
Overall
Borda’s Count ↑
Norwegian language
knowledge
Sentiment
analysis
Commonsense
reasoning
Truthfulness
Norwegian-specific &
world knowledge
Machine reading
comprehension
Text
summarization
Instruction
following
Machine
translation
NB-GPT-6B
33.0
42.0
30.6
34.2
27.9
33.0
29.6
7.8
39.3
39.1
55.1
GPT-SW3-6.7B
45.1
63.0
61.0
64.2
31.3
43.9
30.0
30.1
37.7
35.5
72.6
NorwAI-Mistral-7B
45.5
69.0
47.2
70.7
35.9
36.7
39.5
37.1
31.9
37.7
73.2
NorwAI-Llama2-7B
44.1
59.0
47.9
66.3
29.8
30.2
35.4
38.8
37.5
37.7
72.9
NorBLOOM-7B-warm
35.6
28.0
51.8
40.8
23.5
39.1
23.3
23.9
35.6
13.9
68.8
NorMistral-7B-scratch
38.5
32.0
53.2
57.5
27.7
40.3
25.4
22.3
35.9
14.9
69.7
Viking-7B
41.9
47.0
51.3
59.5
27.4
26.6
25.0
25.9
49.4
38.7
73.0
NorMistral-11B
54.4
94.0
43.0
82.2
45.4
23.4
64.7
59.5
51.7
46.3
73.4
Viking-13B
45.2
69.0
56.8
67.0
31.9
28.3
30.5
30.7
49.3
38.8
73.1
NorMistral-7B-warm
43.6
61.0
59.2
68.7
34.0
31.6
38.7
40.7
33.0
14.6
72.0
NorMistral-7B-warm-IT
40.9
13.0
16.9
77.2
35.2
24.7
49.3
23.4
54.8
56.1
30.5
Mistral-7B
39.7
38.0
23.4
77.7
21.1
46.0
43.5
47.1
29.5
11.6
57.5
Mistral-7B-IT
37.7
4.0
12.8
69.5
19.9
31.9
34.8
31.7
46.2
50.4
42.5
AI-Sweden/Llama-3-8B
51.3
84.0
51.0
80.3
34.8
31.4
54.8
47.1
52.9
38.1
71.5
AI-Sweden/Llama-3-8B-IT
45.7
16.0
16.1
83.2
53.0
12.3
55.3
53.9
48.2
50.1
38.9
Meta/Llama-3-8B
47.0
64.0
28.4
76.8
28.0
34.0
50.9
48.7
53.0
37.4
66.1
Meta/Llama-3-8B-IT
48.2
17.0
13.7
78.3
39.1
39.5
51.8
61.4
51.1
51.4
47.1
Mistral-Nemo-12B
47.6
54.0
26.3
76.8
25.4
29.7
55.0
63.4
50.9
33.5
67.0
Mistral-Nemo-12B-IT
52.1
33.0
16.1
82.9
44.1
42.7
58.8
67.3
57.3
55.7
43.7
Table 4: Borda’s count and normalized performance scores of the Norwegian LMs across all task categories in
NorEval. Cold-colored cells indicate cases where the instruction-tuned version outperforms the base LM, while
warm-colored cells represent cases where performance decreases after instruction-tuning. The best score is in bold,
the second best is underlined – the pretrained and instruction-tuned LMs are highlighted independently.
rates based on the Worker Agreement with Ag-
gregate (WAWA) coefficient (Ning et al., 2018),
which represents the average percentage of annota-
tors’ votes that align with the majority votes. The
WAWA rates range between 86% and 98%, which
shows a strong agreement between our annotators.
LLM-as-a-judge
We use the LLM-as-a-judge
approach to automatically evaluate the instruction-
tuned LMs’ generation abilities on NorRewrite-
Instruct and NorSummarize-Instruct. We adopt
the Human response-guided evaluation framework
(HREF; Lyu et al., 2024), which relies on hu-
man references as additional inputs to improve the
LM judgement performance. Our judge model is
meta-llama/Llama-3.3-70B-Instruct, which
highly correlates with human judgments as re-
ported by Lyu et al.. The judge model is given
(i) the prompt; (ii) output A; (iii) output B; and (iv)
a human reference formatted based on the prompt
template in Appendix F.2. We perform the side-by-
side comparison using a greedy search decoding
strategy across three options: (i) output A is better
than output B; (ii) output B is better than output A;
and (iii) a tie; and compute the expected win rates
as specified in Appendix F.
5
Results
This section describes our empirical evaluation re-
sults on NorEval. We report the results aggregated
across our task categories in Table 4. We find that
NorMistral-11B achieves the best overall perfor-

--- Page 7 ---

mance across most task categories, followed by AI-
Sweden/Llama-3-8B. NorMistral/NorBLOOM-7B-
scratch and NB-GPT-6B receive the lowest scores.
Mistral-Nemo-12B-IT performs best among the
instruction-tuned LMs; however, the benefits from
instruction-tuning depend on the task. In general,
the LMs perform well on the sentiment analysis
and machine translation tasks but struggle with
tasks requiring the Norwegian language knowledge,
commonsense reasoning, truthfulness, and instruc-
tion following. We summarize our findings below
w.r.t. performance aggregation methods, human
performance, task category, the effect of instruction
tuning, Norwegian language variety, and LLM-as-
a-judge evaluation.
Agreement on LM Rankings
The agreement
rate5 between the average normalized score and
Borda’s count for the top-3 LMs is 66%. This
discrepancy is because Borda’s count penalizes
Mistral-Nemo-12B for its low performance on
Norwegian language knowledge tasks, ranking
NorMistral-11B and AI-Sweden/Llama-3-8B as
the top-2 models, while Viking-13B takes third
place instead of Mistral-Nemo-12B. However, the
performance aggregation methods fully agree on
the bottom-5 LMs, which include Viking-7B,
Mistral-7B, NorMistral-7B-scratch, NorBLOOM-
7B-warm, and NB-GPT-6B.
LMs vs. Human Baselines
Comparing the LMs
with our human baselines in Table 9 and Table 10
in Appendix E, we find that the LMs fall behind
humans by 10% on Belebele, 14.4% on NorQuAD,
15.2% on NorOpenBookQA, 17.8% on NorCom-
monsenseQA, and 13.3% on NorTruthfulQA Multi-
ple Choice. However, NorwAI-Llama2-7B slightly
surpasses human performance on NCB by 1.2%.
The results suggest that while LMs show promis-
ing in-context learning capabilities, there is still
room for their improvement in world knowledge,
truthfulness, and reading comprehension tasks.
Analysis on Task Categories
We outline our key
results based on the fine-grained results reported
in Appendix E. No single LM consistently out-
performs others across all task categories. The
strongest performance is observed on the senti-
ment analysis tasks, with AI-Sweden/Llama-3-8B
achieving the best score of 92.7 and its instruction-
tuned version (NoReC Document) reaching 95.5.
5The proportion of top-k and bottom-k LMs that are con-
sistently ranked by both performance aggregation methods.
Figure 2:
Comparison of Bokmål and Nynorsk.
Heatmap that shows the performance δ-scores between
BM and NN on our multiple-choice QA and sen-
tence completion tasks. NOBQA=NorOpenBookQA;
NCSQA=NorCommonsenseQA; NTRQA =NorTruth-
fulQA. Higher values mean higher performance in BM.
On NorIdiom, GPT-SW3-6.7B delivers the best
performance, followed by NorMistral-7B-warm.
For NorCommonsenseQA, the performance of pre-
trained LMs varies: BM scores range from 41.2 to
61, while NN scores range from 32.6 (Mistral-7B)
to 51.6 (NorMistral-11B), suggesting limited in-
context learning abilities for reasoning. The LMs
also exhibit strong performance on Norwegian-
specific quizzes (NRK-Quiz-QA) and tasks assess-
ing elementary-level world knowledge (NorOpen-
BookQA), with the best-performing LMs including
NorMistral-11B, AI-Sweden/Llama-3-8B, Mistral-
7B, and Mistral-Nemo-12B. However, the LMs
tend to generate less truthful answers in the open-
ended QA setup (NorTruthfulQA Generation) com-
pared to the multiple-choice setup (NorTruthfulQA
Multiple Choice), highlighting potential challenges
of evaluating open-ended QA in Norwegian.
Comparing Bokmål and Nynorsk
We compute
the performance δ-scores on multiple-choice and
sentence completion tasks with parallel BM and
NN datasets to compare LMs w.r.t. the Norwe-
gian language variety. Figure 2 shows that the
LMs generally perform better on BM on NorOpen-
BookQA, NorCommonsenseQA, and NorTruth-
fulQA Multiple Choice as opposed to NRK-Quiz-
QA and NorIdiom. Instruction-tuning results in
lower δ-scores on NRK-Quiz-QA and NorOpen-

--- Page 8 ---

Task
k-shot
Language
switching
Generation
issues
Input
copying
Redundant
response
Instruction
misunderstanding
Incorrect
response
NorIdiom (BM)
0-shot
40%
0%
8%
20%
28%
4%
ASK-GEC
16-shot
20%
60%
8%
0%
0%
0%
Tatoeba (En →BM)
16-shot
20%
0%
0%
40%
0%
20%
Tatoeba (En →NN)
16-shot
12%
12%
0%
44%
0%
28%
Overall
23%
18%
4%
26%
7%
13%
Table 5: Quantitative analysis results of the instruction-tuned LMs’ predictions on Norwegian language knowledge
and machine translation tasks. Remaining 9% of the responses are manually classified as correct.
BookQA but leads to random guessing perfor-
mance on NorIdiom for both BM and NN.
Effect of Instruction-tuning
Instruction-tuning
is one of the least explored research directions
for Norwegian.
Our results align with Wang
et al. (2023); Bukharin et al. (2024) and show that
instruction-tuning can yield both positive and neg-
ative effects depending on the task. For instance,
instruction-tuning consistently improves the per-
formance of Mistral-Nemo-12B and Meta/Llama-
3-8B across most task categories, with the most
notable improvements observed in multiple-choice
QA and sequence-to-sequence generation tasks. At
the same time, it can degrade the performance on
tasks requiring Norwegian language knowledge
and involve translating from English into BM and
NN (see Table 8 and Table 11 in Appendix E).
Analysis of Unexpected Results
To better un-
derstand the negative effects of instruction-tuning,
we manually analyze the outputs of 100 instruction-
tuned LMs’ predictions on four tasks: NorIdiom
(BM), ASK-GEC, and Tatoeba (En →BM/NN).
The outputs are stratified by model and task, with
25 examples per task. The main quantitative results
are presented in Table 5. Our analysis reveals that
the instruction-tuned LMs frequently respond in
English, Swedish, Danish, or a mix of these lan-
guages, even when the task requires output in BM
or NN. The models also tend to produce redundant
responses, often including assistant phrases such as
How else can I help you?”. Other common issues
include copying parts of the input, hallucinations,
and repetitive content. In 13% of the cases, the
LM understand the task but fail to produce a cor-
rect answer. We also observe that the LMs fail to
interpret the NorIdiom task, leading to low scores.
The results suggest that the model behavior can be
improved by refining prompt design, tuning the in-
ference hyperparameters, and explicitly specifying
the target written standard in the instructions.
LLM-as-a-judge
We report the LMs’ win-rates
in Table 6. We find that NorMistral-7B-warm-
IT and Mistral-Nemo-12B-IT consistently per-
form best across all LMs, while responses from
AI-Sweden/Llama-3-8B-IT and Mistral-7B-IT are
least preferred. NorMistral-7B-warm-IT achieves
the highest win-rate on NorSummarize-Instruct,
while there is a minor difference between the
top-2 LMs on NorRewrite-Instruct. We analyze
the agreement with humans, and self-preference,
position, and language biases in Appendix F.
Overall, meta-llama/Llama-3.3-70B-Instruct
achieves a moderate agreement with humans (50%
with ties and 66.7% without ties) and behaves fairly
as a judge. We also find that there is an insignificant
effect of the response position on the judge verdicts,
and the instruction-tuned LMs often switch to En-
glish, Swedish, or Danish. The latter is supported
by our manual analysis of the outputs (see Table 5).
6
Conclusion and Future Work
This work introduces NorEval, the largest bench-
mark for assessing the LM’s Norwegian language

--- Page 9 ---

NORREWRITE-INSTRUCT
NORSUMMARIZE-INSTRUCT
Model
NorMistral-7B-warm-IT
Mistral-Nemo-12B-IT
Mistral-7B-IT
Meta/Llama-3-8B-IT
AI-Sweden/Llama-3-8B-IT
Average
NorMistral-7B-warm-IT
Mistral-Nemo-12B-IT
Mistral-7B-IT
Meta/Llama-3-8B-IT
AI-Sweden/Llama-3-8B-IT
Average
NorMistral-7B-warm-IT
—
45.6
92.2
76.2
99.5
78.4
—
57.6
92.5
66.5
99.5
79.0
Mistral-Nemo-12B-IT
54.4
—
89.8
80.6
93.1
79.5
42.4
—
81.8
62.1
87.3
68.4
Mistral-7B-IT
7.8
10.2
—
47.4
67.5
33.2
7.5
18.2
—
36.9
66.9
32.4
Meta/Llama-3-8B-IT
23.8
19.4
52.6
—
64.7
40.1
33.5
37.9
63.1
—
71.4
51.5
AI-Sweden/Llama-3-8B-IT
0.5
6.9
32.5
35.3
—
18.8
0.5
12.7
33.1
28.6
—
18.7
Table 6: Pair-wise expected win-rates (%) of the instruction-finetuned LMs on our instruction-following tasks.
Cold-colored cells indicate high win-rate, while warm-colored cells indicate low win-rate.
understanding and generation capabilities on 24
human-created datasets. NorEval focuses on both
Norwegian language varieties and spans nine task
categories, ranging from Norwegian-specific &
world knowledge to instruction following.
We
benchmark 19 open-source Norwegian generative
LMs against each other and our established hu-
man baselines, analyzing their performance in var-
ious scenarios. Additionally, we present one of
the first extensive evaluations of open Norwegian
instruction-tuned LMs and their base counterparts
in k-shot regimes, as well as via the LLM-as-a-
judge approach. Our key findings indicate that the
LMs struggle with tasks requiring Norwegian lan-
guage knowledge, commonsense reasoning, truth-
fulness, and instruction following. The LMs gen-
erally perform better on BM compared to NN. No-
tably, instruction-tuning yields both positive and
negative effects on the LM performance.
Our future work includes:
(i) a more de-
tailed evaluation of instruction-tuned LMs and
instruction-tuning data mixtures; (ii) integration of
novel datasets; (iii) establishment of human base-
lines on additional tasks; (iv) integration of test
data decontamination methods. We hope that our
benchmark and evaluation framework will facilitate
more comprehensive comparisons of LMs within
the context of Mainland Scandinavian languages
and inspire collaborative efforts among NLP re-
searchers and developers to advance reliable LMs
and evaluation resources for Norwegian.
7
Limitations
While we present extensive empirical evaluations
of a broad range of Norwegian LMs, we acknowl-
edge the following limitations of our work.
Sampling Demonstrations.
In the one- and 16-
shot evaluation scenarios, demonstration examples
are randomly sampled, which can facilitate label
bias in our text classification and multiple-choice
QA tasks (Zhao et al., 2021).
Multi-task Performance Aggregation
Aggre-
gating evaluation results in multi-task benchmark-
ing remains a challenging problem. We employ a
combination of performance aggregation methods
to mitigate the shortcomings of standard arithmetic
mean aggregation: (i) score normalization to ac-
count for random baseline performance, and (ii)
Borda’s count to address the heterogeneity of per-
formance metrics. However, these methods have
inherent limitations. In particular, we still need
to average heterogeneous task-specific normalized
performance scores to compute an overall score.
Although Borda’s count relies on model rankings
instead of performance scores, introducing a new
LM can influence the final ranking due to the well-
studies axiom of the independence of irrelevant
alternatives (Arrow, 2012; Dougherty and Heckel-
man, 2020). Additionally, Borda’s count can treat
several LMs as equivalent (or ties), which is not an
empirical observation in our experiments.

--- Page 10 ---

Potential In-domain Evaluation
Our work does
not account for potential in-domain evaluation
of the instruction-tuned LMs, which can be
instruction-tuned on similar tasks in English and
other languages, potentially inflating their down-
stream performance.
LLM-as-a-judge
Automatic side-by-side eval-
uation using the LLM-as-a-judge approach is a
well-established, complementary evaluation sce-
nario that has demonstrated its efficiency for high-
resource languages. However, its performance in
low-resource languages remains unclear. We ac-
knowledge that the reliability of our LLM-as-a-
judge evaluation results requires further empirical
validation. In particular, our analysis of agreement
between the judge model and human annotators re-
lies on the only available human preference dataset,
which consists of 48 pairwise comparisons (see
Appendix F). The limited sample size may affect
the generalizability of our findings. Furthermore,
our analysis focuses specifically on self-preference,
language, and position biases; investigating other
potential evaluation directions of judge models re-
mains outside the scope of this work.
Human Baselines
We find that the language
models slightly surpass the human performance on
NCB (see §5). However, the results do not suggest
that the models possess human-level capabilities
in distinguishing between in- and correctly punctu-
ated sentences, and evaluating them across more do-
mains and example lengths is necessary to perform
a more fine-grained performance analysis. While
our annotators reach a strong inter-annotator agree-
ment (see §4), we establish our human baselines on
the test subsets of 50 examples only for BM. We ac-
knowledge that increasing the number of examples
could affect both the scores and agreement rates.
Conducting human performance evaluation for NN
could allow us to draw more conclusions regarding
the human and model performance across both offi-
cial written standards. This has not been done due
to our limited resources, and we hope to address
this in our future work.
Data Contamination
The increasing volume of
open textual data can lead to unintended test data
leakage in an LM’s pretraining corpus (e.g., Brown
et al., 2020; Dubey et al., 2024; Zhang et al., 2024),
which can promote the saturation of NLP bench-
marks. We recognize the importance of this evalua-
tion aspect and acknowledge that LM performance
on NorEval datasets created from open text sources
can be inflated. We encourage adherence to re-
sponsible LM development practices and recom-
mend conducting test contamination analysis when
benchmarking an LM on NorEval. Integrating un-
supervised pretraining data detection methods into
NorEval is left as a direction for our future work.
Evaluation Framework
NorEval is integrated
into LM Harness Evaluation, a widely recognized
open-source collaborative project that is subject
to continuous improvements and advancements,
which potentially affect its long-term compatibility,
reproducibility, and usability.
Ethics Statement
Human Annotation
The hourly pay rate in our
annotation projects (§3.2 and Appendix B.3) is
regulated by the state and corresponds to the educa-
tion level. The annotators’ submissions are stored
anonymously. The annotators are warned about
potentially sensitive topics in the dataset examples.
Inference Costs
Evaluating an LM on NorEval
does not require any finetuning. The inference
costs can be minimized with the help of distributed
inference libraries supported by LM Evaluation
Harness, such as Accelerate (Gugger et al., 2022)
and vLLM (Kwon et al., 2023).
Potential Misuse
We acknowledge that NorEval
can leak into and partially overlap with an LM’s
pretraining corpus. We release NorEval for re-
search and development purposes and encourage
its responsible use.
Transparency & License
We release NorEval
adhering to standard open-source research prac-
tices. The dataset licensing terms are provided in
Table 7 (see Appendix A). Our codebase is avail-
able under the MIT license. Our comprehensive
documentation and full annotation guidelines are
available in our GitHub repository.
Use of AI-assistants
We use Grammarly6 to cor-
rect grammar, spelling, and phrasing errors in the
text of this paper.
Acknowledgments
NorEval has developed from Mímir, a project on
evaluating the impact of copyrighted data on pre-
training Norwegian LMs (Rosa et al., 2025). We
6grammarly.com

--- Page 11 ---

thank our student annotators for their annotation
efforts. We also thank our volunteers for their
time and contribution to establishing our human
baselines: Helene Bøsei Olsen, Lilja Charlotte
Storset, Sondre Wold, Petter Mæhlum, Victoria
Ovedie Chruickshank Langø, Egil Rønningstad,
Emil Poiesz, Thea Tollersrud, and Asbjørn Sæther.
References
Kenneth J Arrow. 2012. Social choice and individual
values, volume 12. Yale university press.
Stephen Bach, Victor Sanh, Zheng Xin Yong, Albert
Webson, Colin Raffel, Nihal V. Nayak, Abheesht
Sharma, Taewoon Kim, M Saiful Bari, Thibault
Fevry, Zaid Alyafeai, Manan Dey, Andrea Santilli,
Zhiqing Sun, Srulik Ben-david, Canwen Xu, Gun-
jan Chhablani, Han Wang, Jason Fries, Maged Al-
shaibani, Shanya Sharma, Urmish Thakker, Khalid
Almubarak, Xiangru Tang, Dragomir Radev, Mike
Tian-jian Jiang, and Alexander Rush. 2022. Prompt-
Source: An integrated development environment and
repository for natural language prompts. In Proceed-
ings of the 60th Annual Meeting of the Association
for Computational Linguistics: System Demonstra-
tions, pages 93–104, Dublin, Ireland. Association for
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
Stella Biderman, Hailey Schoelkopf, Lintang Sutawika,
Leo Gao, Jonathan Tow, Baber Abbasi, Alham Fikri
Aji, Pawan Sasanka Ammanamanchi, Sidney Black,
Jordan Clive, et al. 2024. Lessons from the trenches
on reproducible evaluation of language models.
arXiv preprint arXiv:2405.14782.
Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie
Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind
Neelakantan, Pranav Shyam, Girish Sastry, Amanda
Askell, Sandhini Agarwal, Ariel Herbert-Voss,
Gretchen Krueger, Tom Henighan, Rewon Child,
Aditya Ramesh, Daniel M. Ziegler, Jeffrey Wu,
Clemens Winter, Christopher Hesse, Mark Chen,
Eric Sigler, Mateusz Litwin, Scott Gray, Benjamin
Chess, Jack Clark, Christopher Berner, Sam Mc-
Candlish, Alec Radford, Ilya Sutskever, and Dario
Amodei. 2020. Language models are few-shot learn-
ers. Preprint, arXiv:2005.14165.
Alexander Bukharin, Shiyang Li, Zhengyang Wang,
Jingfeng Yang, Bing Yin, Xian Li, Chao Zhang, Tuo
Zhao, and Haoming Jiang. 2024. Data diversity mat-
ters for robust instruction tuning. In Findings of the
Association for Computational Linguistics: EMNLP
2024, pages 3411–3425, Miami, Florida, USA. Asso-
ciation for Computational Linguistics.
Laurie Burchell, Ona de Gibert, Nikolay Arefyev,
Mikko Aulamo, Marta Bañón, Mariia Fedorova,
Liane Guillou, Barry Haddow, Jan Hajiˇc, Erik Hen-
riksson, et al. 2025. An Expanded Massive Mul-
tilingual Dataset for High-Performance Language
Technologies. arXiv preprint arXiv:2503.10267.
Guiming Hardy Chen, Shunian Chen, Ziche Liu, Feng
Jiang, and Benyou Wang. 2024. Humans or LLMs
as the judge? a study on judgement bias. In Proceed-
ings of the 2024 Conference on Empirical Methods
in Natural Language Processing, pages 8301–8327,
Miami, Florida, USA. Association for Computational
Linguistics.
Peter Clark, Isaac Cowhey, Oren Etzioni, Tushar Khot,
Ashish Sabharwal, Carissa Schoenick, and Oyvind
Tafjord. 2018. Think you have Solved Question An-
swering? Try ARC, the AI2 Reasoning Challenge.
arXiv preprint arXiv:1803.05457.
Pierre Colombo, Nathan Noiry, Ekhine Irurozki, and
Stéphan Clémençon. 2022. What are The Best Sys-
tems? New Perspectives on NLP Benchmarking. Ad-
vances in Neural Information Processing Systems,
35:26915–26932.
Mike Conover, Matt Hayes, Ankit Mathur, Jianwei Xie,
Jun Wan, Sam Shah, Ali Ghodsi, Patrick Wendell,
Matei Zaharia, and Reynold Xin. 2023. Free dolly:
Introducing the world’s first truly open instruction-
tuned llm.
Ona de Gibert, Graeme Nail, Nikolay Arefyev, Marta
Bañón, Jelmer van der Linde, Shaoxiong Ji, Jaume
Zaragoza-Bernabeu, Mikko Aulamo, Gema Ramírez-
Sánchez, Andrey Kutuzov, Sampo Pyysalo, Stephan
Oepen, and Jörg Tiedemann. 2024. A new massive
multilingual dataset for high-performance language
technologies. In Proceedings of the 2024 Joint In-
ternational Conference on Computational Linguis-
tics, Language Resources and Evaluation (LREC-
COLING 2024), pages 1116–1128, Torino, Italia.
ELRA and ICCL.
Keith L Dougherty and Jac C Heckelman. 2020. The
probability of violating arrow’s conditions. European
Journal of Political Economy, 65:101936.
Abhimanyu Dubey, Abhinav Jauhri, Abhinav Pandey,
Abhishek Kadian, Ahmad Al-Dahle, Aiesha Letman,
Akhil Mathur, Alan Schelten, Amy Yang, Angela
Fan, et al. 2024. The llama 3 herd of models. arXiv
preprint arXiv:2407.21783.
Yann Dubois, Chen Xuechen Li, Rohan Taori, Tianyi
Zhang, Ishaan Gulrajani, Jimmy Ba, Carlos Guestrin,
Percy S Liang, and Tatsunori B Hashimoto. 2023.
Alpacafarm: A simulation framework for methods
that learn from human feedback. Advances in Neural
Information Processing Systems, 36:30039–30069.

--- Page 12 ---

Kenneth Enevoldsen, Márton Kardos, Niklas Muen-
nighoff, and Kristoffer L Nielbo. 2024. The Scan-
dinavian Embedding Benchmarks: Comprehensive
Assessment of Multilingual and Monolingual Text
Embedding. Advances in Neural Information Pro-
cessing Systems, 37:40336–40358.
Clémentine Fourrier, Nathan Habib, Alina Lozovskaya,
Konrad Szafer, and Thomas Wolf. 2024. Open LLM
Leaderboard v2. Hugging Face.
Leo Gao, Jonathan Tow, Baber Abbasi, Stella Biderman,
Sid Black, Anthony DiPofi, Charles Foster, Laurence
Golding, Jeffrey Hsu, Alain Le Noac’h, Haonan Li,
Kyle McDonell, Niklas Muennighoff, Chris Ociepa,
Jason Phang, Laria Reynolds, Hailey Schoelkopf,
Aviya Skowron, Lintang Sutawika, Eric Tang, An-
ish Thite, Ben Wang, Kevin Wang, and Andy Zou.
2024. A framework for few-shot language model
evaluation.
Sylvain Gugger, Lysandre Debut, Thomas Wolf, Philipp
Schmid, Zachary Mueller, Sourab Mangrulkar, Marc
Sun, and Benjamin Bossan. 2022. Accelerate: Train-
ing and inference at scale made simple, efficient and
adaptable.
https://github.com/huggingface/
accelerate.
Michael A. Hedderich, Lukas Lange, Heike Adel, Jan-
nik Strötgen, and Dietrich Klakow. 2021. A survey
on recent approaches for natural language process-
ing in low-resource scenarios. In Proceedings of
the 2021 Conference of the North American Chap-
ter of the Association for Computational Linguistics:
Human Language Technologies, pages 2545–2568,
Online. Association for Computational Linguistics.
Dan Hendrycks, Collin Burns, Steven Basart, Andy Zou,
Mantas Mazeika, Dawn Song, and Jacob Steinhardt.
2021. Measuring Massive Multitask Language Un-
derstanding. In International Conference on Learn-
ing Representations.
Aaron Hurst, Adam Lerer, Adam P Goucher, Adam
Perelman, Aditya Ramesh, Aidan Clark, AJ Os-
trow, Akila Welihinda, Alan Hayes, Alec Radford,
et al. 2024. GPT-4o System Card. arXiv preprint
arXiv:2410.21276.
Sardana Ivanova, Fredrik Andreassen, Matias Jentoft,
Sondre Wold, and Lilja Øvrelid. 2023. NorQuAD:
Norwegian question answering dataset. In Proceed-
ings of the 24th Nordic Conference on Computational
Linguistics (NoDaLiDa), pages 159–168, Tórshavn,
Faroe Islands. University of Tartu Library.
Matias Jentoft. 2023. Grammatical Error Correction
with Byte-level Language Models. Master’s thesis,
University of Oslo.
Matias Jentoft and David Samuel. 2023. NoCoLA: The
Norwegian corpus of linguistic acceptability. In Pro-
ceedings of the 24th Nordic Conference on Computa-
tional Linguistics (NoDaLiDa), pages 610–617, Tór-
shavn, Faroe Islands. University of Tartu Library.
Albert Q Jiang, Alexandre Sablayrolles, Arthur Men-
sch, Chris Bamford, Devendra Singh Chaplot, Diego
de las Casas, Florian Bressand, Gianna Lengyel, Guil-
laume Lample, Lucile Saulnier, et al. 2023. Mistral
7B. arXiv preprint arXiv:2310.06825.
Fredrik
Jørgensen,
Tobias
Aasmoe,
Anne-Stine
Ruud Husevåg, Lilja Øvrelid, and Erik Velldal. 2020.
NorNE: Annotating named entities for Norwegian.
In Proceedings of the Twelfth Language Resources
and Evaluation Conference, pages 4547–4556, Mar-
seille, France. European Language Resources Asso-
ciation.
Pratik Joshi, Sebastin Santy, Amar Budhiraja, Kalika
Bali, and Monojit Choudhury. 2020. The state and
fate of linguistic diversity and inclusion in the NLP
world. In Proceedings of the 58th Annual Meeting of
the Association for Computational Linguistics, pages
6282–6293, Online. Association for Computational
Linguistics.
Amir Hossein Kargaran, Ayyoob Imani, François Yvon,
and Hinrich Schuetze. 2023. GlotLID: Language
identification for low-resource languages. In Find-
ings of the Association for Computational Linguis-
tics: EMNLP 2023, pages 6155–6218, Singapore.
Association for Computational Linguistics.
Woosuk Kwon, Zhuohan Li, Siyuan Zhuang, Ying
Sheng, Lianmin Zheng, Cody Hao Yu, Joseph E.
Gonzalez, Hao Zhang, and Ion Stoica. 2023. Ef-
ficient Memory Management for Large Language
Model Serving with PagedAttention. In Proceedings
of the ACM SIGOPS 29th Symposium on Operating
Systems Principles.
Dawei Li, Bohan Jiang, Liangjie Huang, Alimohammad
Beigi, Chengshuai Zhao, Zhen Tan, Amrita Bhat-
tacharjee, Yuxuan Jiang, Canyu Chen, Tianhao Wu,
Kai Shu, Lu Cheng, and Huan Liu. 2025. From gen-
eration to judgment: Opportunities and challenges of
llm-as-a-judge. Preprint, arXiv:2411.16594.
Peng Liu, Lemei Zhang, Terje Farup, Even W. Lauvrak,
Jon Espen Ingvaldsen, Simen Eide, Jon Atle Gulla,
and Zhirong Yang. 2024. NLEBench+NorGLM: A
comprehensive empirical analysis and benchmark
dataset for generative language models in Norwegian.
In Proceedings of the 2024 Conference on Empiri-
cal Methods in Natural Language Processing, pages
5543–5560, Miami, Florida, USA. Association for
Computational Linguistics.
Xinxi Lyu, Yizhong Wang, Hannaneh Hajishirzi, and
Pradeep Dasigi. 2024. HREF: Human Response-
Guided Evaluation of Instruction Following in Lan-
guage Models. arXiv preprint arXiv:2412.15524.
Vladislav
Mikhailov,
Petter
Mæhlum,
Victoria
Ovedie Chruickshank Langø, Erik Velldal, and Lilja
Øvrelid. 2025. A collection of question answering
datasets for Norwegian.
In Proceedings of the
Joint 25th Nordic Conference on Computational
Linguistics and 11th Baltic Conference on Human

--- Page 13 ---

Language
Technologies
(NoDaLiDa/Baltic-HLT
2025), pages 397–407, Tallinn, Estonia. University
of Tartu Library.
Shashi Narayan, Shay B. Cohen, and Mirella Lapata.
2018. Don‘t give me the details, just the summary!
topic-aware convolutional neural networks for ex-
treme summarization. In Proceedings of the 2018
Conference on Empirical Methods in Natural Lan-
guage Processing, pages 1797–1807, Brussels, Bel-
gium. Association for Computational Linguistics.
Jørgen Johnsen Navjord and Jon-Mikkel Ryen Korsvik.
2023. Beyond extractive: advancing abstractive au-
tomatic text summarization in norwegian with trans-
formers. Master’s thesis, Norwegian University of
Life Sciences, Ås.
Dan Nielsen. 2023. ScandEval: A benchmark for Scan-
dinavian natural language processing. In Proceed-
ings of the 24th Nordic Conference on Computational
Linguistics (NoDaLiDa), pages 185–201, Tórshavn,
Faroe Islands. University of Tartu Library.
Qiang Ning, Zhili Feng, Hao Wu, and Dan Roth. 2018.
Joint reasoning for temporal and causal relations. In
Proceedings of the 56th Annual Meeting of the As-
sociation for Computational Linguistics (Volume 1:
Long Papers), pages 2278–2288, Melbourne, Aus-
tralia. Association for Computational Linguistics.
Long Ouyang, Jeffrey Wu, Xu Jiang, Diogo Almeida,
Carroll Wainwright, Pamela Mishkin, Chong Zhang,
Sandhini Agarwal, Katarina Slama, Alex Ray, et al.
2022. Training language models to follow instruc-
tions with human feedback. Advances in neural in-
formation processing systems, 35:27730–27744.
Lilja Øvrelid and Petter Hohle. 2016. Universal Depen-
dencies for Norwegian. In Proceedings of the Tenth
International Conference on Language Resources
and Evaluation (LREC‘16), pages 1579–1585, Por-
torož, Slovenia. European Language Resources As-
sociation (ELRA).
Lilja Øvrelid, Petter Mæhlum, Jeremy Barnes, and Erik
Velldal. 2020. A fine-grained sentiment dataset for
Norwegian. In Proceedings of the Twelfth Language
Resources and Evaluation Conference, pages 5025–
5033, Marseille, France. European Language Re-
sources Association.
Arjun Panickssery, Samuel Bowman, and Shi Feng.
2024. Llm evaluators recognize and favor their own
generations. Advances in Neural Information Pro-
cessing Systems, 37:68772–68802.
Guilherme Penedo, Hynek Kydlíˇcek, Vinko Sabolˇcec,
Bettina Messmer, Negar Foroutan, Martin Jaggi,
Leandro von Werra, and Thomas Wolf. 2024.
FineWeb2: A sparkling update with 1000s of lan-
guages.
Nazneen Rajani, Lewis Tunstall, Edward Beeching,
Nathan Lambert, Alexander M. Rush, and Thomas
Wolf. 2023. No robots. https://huggingface.co/
datasets/HuggingFaceH4/no_robots.
Pranav Rajpurkar, Jian Zhang, Konstantin Lopyrev, and
Percy Liang. 2016. SQuAD: 100,000+ questions for
machine comprehension of text. In Proceedings of
the 2016 Conference on Empirical Methods in Natu-
ral Language Processing, pages 2383–2392, Austin,
Texas. Association for Computational Linguistics.
Mark Rofin, Vladislav Mikhailov, Mikhail Florinsky,
Andrey Kravchenko, Tatiana Shavrina, Elena Tu-
tubalina, Daniel Karabekyan, and Ekaterina Arte-
mova. 2023. Vote‘n‘rank: Revision of benchmarking
with social choice theory. In Proceedings of the 17th
Conference of the European Chapter of the Associa-
tion for Computational Linguistics, pages 670–686,
Dubrovnik, Croatia. Association for Computational
Linguistics.
Javier de la Rosa, Vladislav Mikhailov, Lemei Zhang,
Freddy Wetjen, David Samuel, Peng Liu, Rolv-
Arild Braaten, Petter Mæhlum, Magnus Breder
Birkenes, Andrey Kutuzov, Tita Enstad, Hans Chris-
tian Farsethås, Svein Arne Brygfjeld, Jon Atle Gulla,
Stephan Oepen, Erik Velldal, Wilfred Østgulen, Lilja
Øvrelid, and Aslak Sira Myhre. 2025. The impact
of copyrighted material on large language models: A
Norwegian perspective. In Proceedings of the Joint
25th Nordic Conference on Computational Linguis-
tics and 11th Baltic Conference on Human Language
Technologies (NoDaLiDa/Baltic-HLT 2025), pages
544–560, Tallinn, Estonia. University of Tartu Li-
brary.
Sebastian Ruder. 2021. Challenges and Opportunities
in NLP Benchmarking.
Ananya B. Sai, Akash Kumar Mohankumar, and
Mitesh M. Khapra. 2022. A survey of evaluation
metrics used for nlg systems. ACM Comput. Surv.,
55(2).
David Samuel, Andrey Kutuzov, Samia Touileb, Erik
Velldal, Lilja Øvrelid, Egil Rønningstad, Elina Sigdel,
and Anna Palatkina. 2023. NorBench – a benchmark
for Norwegian language models. In Proceedings
of the 24th Nordic Conference on Computational
Linguistics (NoDaLiDa), pages 618–633, Tórshavn,
Faroe Islands. University of Tartu Library.
David Samuel, Vladislav Mikhailov, Erik Velldal, Lilja
Øvrelid, Lucas Georges Gabriel Charpentier, Andrey
Kutuzov, and Stephan Oepen. 2025. Small languages,
big models: A study of continual training on lan-
guages of Norway. In Proceedings of the Joint 25th
Nordic Conference on Computational Linguistics and
11th Baltic Conference on Human Language Tech-
nologies (NoDaLiDa/Baltic-HLT 2025), pages 573–
608, Tallinn, Estonia. University of Tartu Library.
Aarohi Srivastava, Abhinav Rastogi, Abhishek Rao,
Abu Awal Md Shoeb, Abubakar Abid, Adam Fisch,
Adam R Brown, Adam Santoro, Aditya Gupta, Adrià
Garriga-Alonso, et al. 2023. Beyond the Imitation
Game: Quantifying and extrapolating the capabili-
ties of language models. Transactions on Machine
Learning Research.

--- Page 14 ---

Kari Tenfjord, Paul Meurer, and Knut Hofland. 2006.
The ASK corpus - a language learner corpus of Nor-
wegian as a second language.
In Proceedings of
the Fifth International Conference on Language Re-
sources and Evaluation (LREC‘06), Genoa, Italy. Eu-
ropean Language Resources Association (ELRA).
Jörg Tiedemann. 2020. The tatoeba translation chal-
lenge – realistic data sets for low resource and multi-
lingual MT. In Proceedings of the Fifth Conference
on Machine Translation, pages 1174–1182, Online.
Association for Computational Linguistics.
Samia Touileb, Vladislav Mikhailov, Marie Ingeborg
Kroka, Lilja Øvrelid, and Erik Velldal. 2025. Bench-
marking abstractive summarisation: A dataset of
human-authored summaries of Norwegian news ar-
ticles.
In Proceedings of the Joint 25th Nordic
Conference on Computational Linguistics and 11th
Baltic Conference on Human Language Technolo-
gies (NoDaLiDa/Baltic-HLT 2025), pages 729–738,
Tallinn, Estonia. University of Tartu Library.
Erik Velldal, Lilja Øvrelid, Eivind Alexander Bergem,
Cathrine Stadsnes, Samia Touileb, and Fredrik Jør-
gensen. 2018. NoReC: The Norwegian review cor-
pus. In Proceedings of the Eleventh International
Conference on Language Resources and Evaluation
(LREC 2018), Miyazaki, Japan. European Language
Resources Association (ELRA).
Erik Velldal, Lilja Øvrelid, and Petter Hohle. 2017.
Joint UD parsing of Norwegian Bokmål and Nynorsk.
In Proceedings of the 21st Nordic Conference on
Computational Linguistics, pages 1–10, Gothenburg,
Sweden. Association for Computational Linguistics.
Anton Voronov, Lena Wolf, and Max Ryabinin. 2024.
Mind your format: Towards consistent evaluation of
in-context learning improvements. In Findings of
the Association for Computational Linguistics: ACL
2024, pages 6287–6310, Bangkok, Thailand. Associ-
ation for Computational Linguistics.
Peiyi Wang, Lei Li, Liang Chen, Zefan Cai, Dawei
Zhu, Binghuai Lin, Yunbo Cao, Lingpeng Kong,
Qi Liu, Tianyu Liu, and Zhifang Sui. 2024. Large lan-
guage models are not fair evaluators. In Proceedings
of the 62nd Annual Meeting of the Association for
Computational Linguistics (Volume 1: Long Papers),
pages 9440–9450, Bangkok, Thailand. Association
for Computational Linguistics.
Yizhong Wang, Hamish Ivison, Pradeep Dasigi, Jack
Hessel, Tushar Khot, Khyathi Chandu, David Wad-
den, Kelsey MacMillan, Noah A Smith, Iz Beltagy,
et al. 2023. How far can camels go? exploring the
state of instruction tuning on open resources. Ad-
vances in Neural Information Processing Systems,
36:74764–74786.
Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten
Bosma, brian ichter, Fei Xia, Ed Chi, Quoc V Le,
and Denny Zhou. 2022. Chain-of-thought prompt-
ing elicits reasoning in large language models. In
Advances in Neural Information Processing Systems,
volume 35, pages 24824–24837. Curran Associates,
Inc.
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
Demonstrations, pages 38–45, Online. Association
for Computational Linguistics.
Rowan Zellers, Ari Holtzman, Yonatan Bisk, Ali
Farhadi, and Yejin Choi. 2019. HellaSwag: Can a ma-
chine really finish your sentence? In Proceedings of
the 57th Annual Meeting of the Association for Com-
putational Linguistics, pages 4791–4800, Florence,
Italy. Association for Computational Linguistics.
Jingyang Zhang, Jingwei Sun, Eric Yeats, Yang Ouyang,
Martin Kuo, Jianyi Zhang, Hao Yang, and Hai Li.
2024. Min-K%++: Improved Baseline for Detect-
ing Pre-Training Data from Large Language Models.
arXiv preprint arXiv:2404.02936.
Zihao Zhao, Eric Wallace, Shi Feng, Dan Klein, and
Sameer Singh. 2021. Calibrate before use: Improv-
ing few-shot performance of language models. In
Proceedings of the 38th International Conference
on Machine Learning, volume 139 of Proceedings
of Machine Learning Research, pages 12697–12706.
PMLR.
Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan
Zhuang, Zhanghao Wu, Yonghao Zhuang, Zi Lin,
Zhuohan Li, Dacheng Li, Eric Xing, Hao Zhang,
Joseph E. Gonzalez, and Ion Stoica. 2023. Judging
LLM-as-a-judge with MT-bench and chatbot arena.
In Thirty-seventh Conference on Neural Information
Processing Systems Datasets and Benchmarks Track.

--- Page 15 ---

A
NorEval: Dataset Descriptions, Examples, and Prompts
Dataset
Language |Train| |Test|
#P Method
Task Type
Task Category
Performance Metrics
License
Peer-reviewed Norwegian datasets
NoReC Sentence
BM
3.89k
583
5
Human-created
Text classification
Sentiment analysis
F1a, Accuracy score
CC BY-NC 4.0
NoReC Document
BM
23.4k
2.9k
5
NorQuAD
BM
3.81k
472
5 Human-created
Generative QA
Reading Comprehension F1, Exact match
CC0-1.0
ASK-GEC
BM
36.4k 4.75k
5 Human-created
Seq2seq generation
Norwegian language
knowledge
ERRANT
CC BY 4.0
Belebele
BM
✗
900
5 Human-translated Multiple-choice QA
Reading Comprehension Accuracy score
CC BY-SA 4.0
Tatoeba
En ↔BM
5.2k
4.5k
8
Human-created
Seq2seq generation
Machine translation
BLEU, BERTScore
CC-BY-2-0
En ↔NN
504
459
8
NorOpenBookQA
BM
2.8k
163
5 Human-created &
human-translated
Multiple-choice QA
Norwegian-specific &
world knowledge
Accuracy score
MIT
NN
376
90
5
NRK-Quiz-QA
BM
✗
3.6k
5
Human-created
Multiple-choice QA
Norwegian-specific &
world knowledge
Accuracy score
MIT
NN
✗
1.3k
5
NorCommonsenseQA
BM
✗
693
5 Human-created &
human-translated
Multiple-choice QA
Commonsense reasoning Accuracy score
MIT
NN
✗
95
5
NorTruthfulQA MC
BM
✗
488
5 Human-created &
human-translated
Multiple-choice QA
Truthfulness
Accuracy score
MIT
NN
✗
57
5
NorTruthfulQA Gen
BM
✗
346
5 Human-created &
human-translated
Generative QA
Truthfulness
BLEU, ROUGE-L
MIT
NN
✗
125
5
NorSumm
BM
30
33
6
Human-created
Seq2seq generation
Text summarization
ROUGE-L, BERTScore CC0-1.0
NN
30
33
6
Novel datasets for Norwegian (ours)
NorRewrite-Instruct
BM
✗
144 144 Human-created
Seq2seq generation
Instruction following
chrF, BERTScore
MIT
NorSummarize-Instruct
BM
✗
197 197 Human-created
Seq2seq generation
Instruction following
chrF, BERTScore
MIT
NorIdiom
BM
✗
3.4k
5
Human-created
Sentence completion
Norwegian language
knowledge
F1, Exact match
CC0-1.0
NN
✗
89
5
NCB
BM
✗
840
✗Human-created
Sentence ranking
Norwegian language
knowledge
Accuracy score
CC BY-NC 4.0
Table 7: Overview of the datasets in NorEval w.r.t. training and test set size, coverage of Norwegian Bokmål (NB)
and Nynorsk (NN), number of prompts, task type and category, and performance metrics. En=English. P=Prompts.
This appendix presents an overview of the 24 datasets included in NorEval (also see Table 7).
NCB
The Norwegian Comma Benchmark (NCB) is a collection of 840 human-written Norwegian sentence pairs.
The sentences are manually collected from publicly available sources such as articles and governmental
reports. The sentences aim to be representative of Norwegian non-fiction, in particular governmental
prose. Each sentence pair tests one Norwegian comma rule: one sentence is correctly punctuated, while
the other contains faulty comma usage.
• correct: “Spørsmålet om å begrense forvaltningens arbeidsbyrde ble viet stor oppmerksomhet.”
• wrong: “Spørsmålet om å begrense forvaltningens arbeidsbyrde, ble viet stor oppmerksomhet.”
Task Formulation
Given a pair of sentences, the task is to select a correctly punctuated sentence by
ranking both sentences based on their probability. The performance metric is the accuracy score.

--- Page 16 ---

NorIdiom
NorIdiom is designed to evaluate an LM’s knowledge of 3.5k common Norwegian idioms and phrases.
Each task example consists of the first N −1 words of an idiom, and a list of accepted last words to
complete the idiom.
• idiom_start: “bite på”
• accepted_completions: “kroken”, “agnet”
Task formulation
The task is to generate the last word of an incomplete idiom. We maximize the F1
and exact match performance scores over the list of accepted completions.
Prompt A (BM and NN):
1
Fullfør dette uttrykket: {{idiom_start}}
Prompt B (BM):
1
Skriv fortsettelsen av idiomet {{idiom_start}}
Prompt B (NN):
1
Skriv fortsetjinga av idiomet {{idiom_start}}
Prompt C (BM):
1
Hvordan fortsetter uttrykket "{{idiom_start}}"?
Prompt C (NN):
1
Korleis fortset uttrykket "{{idiom_start}}"?
Prompt D (BM):
1
Fullfør vendingen "{{idiom_start}}"
Prompt D (NN):
1
Fullfør vendinga: {{idiom_start}}
Prompt E (BM and NN):
1
{{idiom_start}}
Belebele
Belebele is a multiple-choice QA dataset spanning 122 language variants. Each question has four
multiple-choice answers a short passage.
Task Formulation
The task is to select a correct answer option given a passage and a question. The
performance metric is the accuracy score.
• passage: “Så og si nesten alle PC-er som benyttes i dag, baseres på manipulering av informasjon
som er kodet med binære tall. Et binært tall kan kun ha én av to verdier, dvs. 0 eller 1. Disse tallene
omtales som binærsifre – eller biter, for å bruke datasjargon.”
• question: “Hvilke av følgende er et eksempel et binært tall med fem biter, ifølge avsnittet?”
• answer_1: 1010
• answer_2: 12001
• answer_3: 10010
• answer_4:110101
• correct_answer_num: 3

--- Page 17 ---

Prompt A:
1
Tekst: {{passage}}
2
Spørsmål: {{question}}
3
A: {{answer_1}}
4
B: {{answer_2}}
5
C: {{answer_3}}
6
D: {{answer_4}}
7
Svar: {prediction:A/B/C/D}
Prompt B:
1
Bakgrunn: {{passage}}
2
Spørsmål: {{question}}
3
Svaralternativer:
4
- {{answer_1}}
5
- {{answer_2}}
6
- {{answer_3}}
7
- {{answer_4}}
8
Svar: {prediction:{{answer_1}}/{{answer_2}}/{{answer_3}}/{{answer_4}}}
Prompt C:
1
{{question}}
2
Hvilket av følgende mulige svar er det riktige?
3
A: {{answer_1}}
4
B: {{answer_2}}
5
C: {{answer_3}}
6
D: {{answer_4}}
7
Svar: {prediction:A/B/C/D}
Prompt D:
1
Svar på følgende spørsmål: {{question}}
2
Svaret skal baseres på følgende tekst:
3
{{passage}}
4
Velg et svar fra denne listen:
5
- {{answer_1}}
6
- {{answer_2}}
7
- {{answer_3}}
8
- {{answer_4}}
9
Svar: {prediction:{{answer_1}}/{{answer_2}}/{{answer_3}}/{{answer_4}}}
Prompt E:
1
{{passage}}
2
3
{{question}}
4
5
A: {{answer_1}}
6
B: {{answer_2}}
7
C: {{answer_3}}
8
D: {{answer_4}}
9
10
Er det riktige svaret A, B, C, eller D? {prediction:A/B/C/D}

--- Page 18 ---

NorQuAD
NorQuAD consists of 4.7k manually created examples based on Wikipedia and news articles following
the SQuAD design (Rajpurkar et al., 2016).
• title: “Ordspråk
• context: “Ordspråk eller ordtak er korte, velformulerte og poengterte setninger som på en konkret
måte uttrykker livsvisdom, allmenngyldige sannheter, erfaringer, leveregler eller betraktninger av
forskjellig slag. Ordspråk kan også inneholde forklaringer av naturfenomener, skikker og seder.
Ordspråk har en fast ordlyd som er kjent og blir sitert, for eksempel for å kommentere noe eller
for å gi et råd. Mange ordspråk har uklar opprinnelse og er en del av gammel folkediktning og en
muntlig fortellertradisjon. Det er også mange som er sitater fra bøker og fortellinger med kjent opphav,
for eksempel fra Bibelen og Håvamål, selv om begrepet ordspråk ofte brukes om folkelige uttrykk
uten kjent forfatter. Ordspråk kan være internasjonale, nasjonale og regionale og finnes i et nærmest
uendelig antall og i en mengde varianter over hele verden. Studiet av ordspråk kalles parømiologi.
Også fraseologien beskriver etablerte flerordsenheter og -forbindelser i et språk, særlig faste uttrykk
og idiomer, men også tekster som ordspråk.”
• question: “Hvordan er opprinnelsen til mange ordspråk?”
• answer: “uklar”
Task Formulation
The task is to extract the answer from the context given a question. We formulate it
as a sequence-to-sequence problem, where the LM receives the context and the question as the input and is
expected to generate the answer. The performance metrics are exact match (the percentage of predictions
that exactly match the gold answer) and F1-score (the average N-gram overlap between the prediction and
the gold answer treated as bag-of-words).
Prompt A:
1
Tittel: {{title}}
2
3
Tekst: {{passage}}
4
5
Spørsmål: {{question}}
6
7
Svar: {{prediction}}
Prompt B:
1
Tittel: {{title}}
2
3
Tekst: {{passage}}
4
5
Gitt teksten over, hva er svaret på følgende spørsmål? "{{question}}"
6
7
Svar: {{prediction}}
Prompt C:
1
Tittel: {{title}}
2
3
Tekst: {{passage}}
4
5
Svar på følgende: {{question}}
6
7
Svar: {{prediction}}

--- Page 19 ---

Prompt D:
1
Tittel: {{title}}
2
3
Tekst: {{passage}}
4
5
Hvordan kan man svare på spørsmålet "{{question}}", gitt teksten over?
6
7
Svar:{{prediction}}
Prompt E:
1
Tittel: {{title}}
2
3
Tekst: {{passage}}
4
5
Gitt teksten over, besvar følgende spørsmål: "{{question}}"
6
7
Svar: {{prediction}}
NoReC Sentence
NoReC Sentence is a dataset for sentence-level sentiment analysis in Norwegian, derived from NoReC_fine
(Øvrelid et al., 2020). The annotations have been aggregated at the sentence-level, by only keeping
sentences that contain sentiment annotations of either positive or negative polarity.
Task Formulation
The task is framed as a binary classification problem. The LM is required to predict
if a given review has a positive or negative sentiment. The target performance metric is the macro-average
F1-score.
• review: “En mer allsidig og tilkoblingsvennlig skjerm har vi knapt sett .”
• sentiment: 1 (positive).
Prompt A:
1
Tekst: {{text}}
2
Sentiment: {prediction:positiv/negativ}
Prompt B:
1
{{text}}
2
Er denne setningen "positiv" eller "negativ"? {prediction:positiv/negativ}
Prompt C:
1
{{text}}
2
Hva slags sentiment uttrykker anmelderen? {prediction:positiv/negativ}
Prompt D:
1
{{text}}
2
Er anmeldelsen "positiv" eller "negativ"? {prediction:positiv/negativ}
Prompt E:
1
{{text}}
2
Er denne setningen positiv eller negativ? {prediction:positiv/negativ}
NoReC Document
NoReC Document is a dataset for document-level sentiment analysis derived from NoReC (Velldal et al.,
2018) by keeping documents that have positive (ratings 5–6) or negative (ratings 1–3) sentiment.

--- Page 20 ---

Task Formulation
The task is framed as a binary classification problem. The LM is required to predict
if a given review has a positive or negative sentiment. The target performance metric is the macro-average
F1-score.
Prompt A:
1
Tekst: {{text}}
2
Sentiment: {prediction:positiv/negativ}
Prompt B:
1
Tekst: {{text}}
2
Er anmeldelsen "positiv" eller "negativ"? {prediction:positiv/negativ}
Prompt C:
1
Er polariteten til følgende anmeldelse positiv eller negativ?
2
Anmeldelse: {{text}}
3
Anmeldelsen er {prediction:positiv/negativ}
Prompt D:
1
Anmeldelse: {{text}}
2
Er anmelderen positiv eller negativ? {prediction:positiv/negativ}
Prompt E:
1
Anmeldelse: {{text}}
2
Vil du oppsummere anmeldelsen som "bra" eller "dårlig"? {prediction:bra/dårlig}
NorCommonsenseQA
NorCommonsenseQA is developed to assess the LM’s commonsense reasoning abilities. It includes 1.1k
examples in BM and NN, each comprising a question and five answer choices.
• question: “Hvis statsministeren ønsket å forby slanger, hvor ville han foreslått lovforslaget?”
• answer_1: “På gata”
• answer_2: “I en tropisk skog”
• answer_3: “I Edens hage”
• answer_4: “På Eidsvoll”
• answer_5: “I Stortinget” (correct)
Task Formulation
The task is to select a correct answer to given a question. The performance metric is
the accuracy score.
Prompt A (BM and NN):
1
Spørsmål: {{question}}
2
3
Svar: {prediction:{{answer_1}}/{{answer_2}}/{{answer_3}}/{{answer_4}}/{{answer_5}}}
Prompt B (BM):
1
{{question}}
2
Hvilket av følgende mulige svar er det riktige?
3
A: {{answer_1}}
4
B: {{answer_2}}
5
C: {{answer_3}}
6
D: {{answer_4}}
7
E: {{answer_5}}
8
Svar: {prediction:A/B/C/D/E}

--- Page 21 ---

Prompt B (NN):
1
{{question}}
2
Kva av følgande moglege svar er det rette?
3
A: {{answer_1}}
4
B: {{answer_2}}
5
C: {{answer_3}}
6
D: {{answer_4}}
7
E: {{answer_5}}
8
Svar: {prediction:A/B/C/D/E}
Prompt C (BM):
1
Gitt alternativene under, hva er svaret på følgende spørsmål: {{question}}
2
3
Alternativer:
4
- {{answer_1}}
5
- {{answer_2}}
6
- {{answer_3}}
7
- {{answer_4}}
8
- {{answer_5}}
9
10
Svar: {prediction:{{answer_1}}/{{answer_2}}/{{answer_3}}/{{answer_4}}/{{answer_5}}}
Prompt C (NN):
1
Gitt alternativa under, kva er svaret på følgande spørsmål: {{question}}
2
3
Alternativ:
4
- {{answer_1}}
5
- {{answer_2}}
6
- {{answer_3}}
7
- {{answer_4}}
8
- {{answer_5}}
9
10
Svar: {prediction:A/B/C/D/E}
Prompt D (BM):
1
{{question}}
2
Velg riktig svar blant disse alternativene:
3
- {{answer_1}}
4
- {{answer_2}}
5
- {{answer_3}}
6
- {{answer_4}}
7
- {{answer_5}}
8
9
Svar: {prediction:{{answer_1}}/{{answer_2}}/{{answer_3}}/{{answer_4}}/{{answer_5}}}
Prompt D (NN):
1
{{question}}
2
Vel rett svar blant desse alternativa:
3
- {{answer_1}}
4
- {{answer_2}}
5
- {{answer_3}}
6
- {{answer_4}}
7
- {{answer_5}}
8
9
Svar: {prediction:{{answer_1}}/{{answer_2}}/{{answer_3}}/{{answer_4}}/{{answer_5}}}

--- Page 22 ---

Prompt E (BM):
1
{{question}}
2
A: {{answer_1}}
3
B: {{answer_2}}
4
C: {{answer_3}}
5
D: {{answer_4}}
6
E: {{answer_5}}
7
8
Er det riktige svaret A, B, C, D, eller E?
9
10
Svar: {prediction:A/B/C/D/E}
Prompt E (NN):
1
{{question}}
2
A: {{answer_1}}
3
B: {{answer_2}}
4
C: {{answer_3}}
5
D: {{answer_4}}
6
E: {{answer_5}}
7
8
Er det rette svaret A, B, C, D, eller E?
9
10
Svar: {prediction:A/B/C/D/E}
NRK-Quiz-QA
NRK-Quiz-QA allows for evaluation of the LM’s Norwegian-specific and world knowledge. NRK-Quiz-
QA includes 4.9k examples in BM and NN from more than 500 quizzes covering various topics on the
Norwegian language and culture. Each example contains a question and 2 to 5 answer choices.
• question: “Æ træng læsta: Læsta er kjekt å ha. I alle fall sånn innimellom. Men hva er det for
noe?”
• answer_1: “Venner”
• answer_2: “Lesestoff”
• answer_3: “Ro”
• answer_4: “Ullsokker” (correct)
Task Formulation
The task is to select a correct answer to given a question. The performance metric is
the accuracy score.
Prompt A (BM and NN):
1
Spørsmål: {{question}}
2
3
Svar: {prediction:{{answer_1}}/{{answer_2}}/{{answer_3}}/{{answer_4}}}

--- Page 23 ---

Prompt B (BM):
1
{{question}}
2
3
Svaralternativer:
4
- {{answer_1}}
5
- {{answer_2}}
6
- {{answer_3}}
7
- {{answer_4}}
8
9
Hva er riktig svar?
10
11
Svar: {prediction:{{answer_1}}/{{answer_2}}/{{answer_3}}/{{answer_4}}}
Prompt B (NN):
1
{{question}}
2
{{question}}
3
4
Svaralternativer:
5
- {{answer_1}}
6
- {{answer_2}}
7
- {{answer_3}}
8
- {{answer_4}}
9
10
Kva er rett svar?
11
12
Svar: {prediction:{{answer_1}}/{{answer_2}}/{{answer_3}}/{{answer_4}}}
Prompt C (BM):
1
{{question}}
2
A: {{answer_1}}
3
B: {{answer_2}}
4
C: {{answer_3}}
5
D: {{answer_4}}
6
7
Er det riktige svaret A, B, C, eller D?
8
9
Svar: {prediction:A/B/C/D}
Prompt C (NN):
1
{{question}}
2
A: {{answer_1}}
3
B: {{answer_2}}
4
C: {{answer_3}}
5
D: {{answer_4}}
6
7
Er det rette svare A, B, C, eller D?
8
9
Svar: {prediction:A/B/C/D}
Prompt D (BM and NN):
1
Spørsmål: {{question}}
2
A: {{answer_1}}
3
B: {{answer_2}}
4
C: {{answer_3}}
5
D: {{answer_4}}
6
7
Svar: {prediction:A/B/C/D}

--- Page 24 ---

Prompt E (BM):
1
{{question}}
2
Velg riktig svar blant disse alternativene:
3
- {{answer_1}}
4
- {{answer_2}}
5
- {{answer_3}}
6
- {{answer_4}}
7
8
Svar: {prediction:{{answer_1}}/{{answer_2}}/{{answer_3}}/{{answer_4}}}
Prompt E (NN):
1
{{question}}
2
Vel rett svar blant desse alternativa:
3
- {{answer_1}}
4
- {{answer_2}}
5
- {{answer_3}}
6
- {{answer_4}}
7
8
Svar: {prediction:{{answer_1}}/{{answer_2}}/{{answer_3}}/{{answer_4}}}
NorOpenBookQA
NorOpenBookQA is designed to evaluate the LM’s world knowledge. NorOpenBookQA counts 3.5k
examples in BM and NN, each consisting of an elementary-level science question, four answer choices,
and a factual statement that presents the evidence necessary to determine the correct answer.
• question: “Hva er mykest?”
• answer_1: “Marshmallows”
• answer_1: “Stål”
• answer_1: “Diamant”
• answer_1: “Saltstenger”
• fact: “Et mineral som kan skrapes av en fingernegl regnes som mykt”
Task Formulation
The task is to select a correct answer to given a question. The performance metric is
the accuracy score.
Prompt A (BM and NN):
1
{{fact}}
2
{{question}} {prediction:{{answer_1}}/{{answer_2}}/{{answer_3}}/{{answer_4}}}
Prompt B (BM):
1
Faktatekst: {{fact}}
2
Spørsmål til teksten: {{question}}
3
4
Svaralternativer:
5
- {{answer_1}}
6
- {{answer_2}}
7
- {{answer_3}}
8
- {{answer_4}}
9
10
Hva er riktig svar? {prediction:{{answer_1}}/{{answer_2}}/{{answer_3}}/{{answer_4}}}

--- Page 25 ---

Prompt B (NN):
1
Faktatekst: {{fact}}
2
Spørsmål til teksten: {{question}}
3
4
Svaralternativer:
5
- {{answer_1}}
6
- {{answer_2}}
7
- {{answer_3}}
8
- {{answer_4}}
9
10
Kva er rett svar? {prediction:{{answer_1}}/{{answer_2}}/{{answer_3}}/{{answer_4}}}
Prompt C (BM):
1
{{fact}}
2
{{question}}
3
A: {{answer_1}}
4
B: {{answer_2}}
5
C: {{answer_3}}
6
D: {{answer_4}}
7
8
Er det riktige svaret A, B, C, eller D?
9
10
Svar: {prediction:A/B/C/D}
Prompt C (NN):
1
{{fact}}
2
{{question}}
3
A: {{answer_1}}
4
B: {{answer_2}}
5
C: {{answer_3}}
6
D: {{answer_4}}
7
8
Er det rette svare A, B, C, eller D?
9
10
Svar: {prediction:A/B/C/D}
Prompt D (BM and NN):
1
Bakgrunn: {{fact}}
2
3
Spørsmål: {{question}}
4
A: {{answer_1}}
5
B: {{answer_2}}
6
C: {{answer_3}}
7
D: {{answer_4}}
8
9
Svar: {prediction:A/B/C/D}
Prompt E (BM):
1
Ta utgangspunkt i følgende fakta når du svarer på spørsmålet: {{fact}}
2
3
{{question}}
4
Velg riktig svar blant disse alternativene:
5
- {{answer_1}}
6
- {{answer_2}}
7
- {{answer_3}}
8
- {{answer_4}}

--- Page 26 ---

9
10
Svar: {prediction:{{answer_1}}/{{answer_2}}/{{answer_3}}/{{answer_4}}}
Prompt E (NN):
1
Ta utgangspunkt i følgande fakta når du svarar på spørsmålet: {{fact}}
2
3
{{question}}
4
Vel rett svar blant desse alternativa:
5
- {{answer_1}}
6
- {{answer_2}}
7
- {{answer_3}}
8
- {{answer_4}}
9
10
Svar: {prediction:{{answer_1}}/{{answer_2}}/{{answer_3}}/{{answer_4}}}
NorSumm
NorSumm is an abstractive text summarization dataset of news articles taken from the news part of the
text sources of the Norwegian UD Treebank. Each news article is summarized in several versions in both
BM and NN.
Task Formulation
The task is an abstractive text summarization, where the LM is required to summarize
a given news article. We use a combination of standard performance metrics (ROUGE-Land BERTScore),
and maximize each performance score over the list of human references.
Prompt A (BM):
1
Skriv en oppsummering av følgende artikkel med kun noen få punkter: {{article}}
2
Oppsummering: {{prediction}}
Prompt A (NN):
1
Skriv ei oppsummering av følgande artikkel med berre nokre få punkt: {{article}}
2
Oppsummering: {{prediction}}
Prompt B (BM):
1
Oppsummer følgende artikkel med noen få setninger: {{article}}
2
Oppsummering: {{prediction}}
Prompt B (NN):
1
Oppsummer følgande artikkel med nokre få setningar: {{article}}
2
Oppsummering: {{prediction}}
Prompt C (BM):
1
{{article}}
2
Skriv en kort og presis oppsummering av teksten over. <...> Oppsummeringen skal inneholde
maksimalt 700 tegn, inkludert mellomrom. {{prediction}}
,→
Prompt C (NN):
1
{{article}}
2
Skriv ein kort og presis oppsummering av teksten over. <...> Oppsummeringa skal innehalde
maksimalt 700 tegn, inkludert mellomrom. {{prediction}}
,→
Prompt D (BM):
1
Gi et kortfattet sammendrag av følgende tekst: {{article}} {{prediction}}

--- Page 27 ---

Prompt D (NN):
1
Gje eit kortfatta samandrag av følgande tekst: {{article}} {{prediction}}
Prompt E (BM):
1
Lag en kort oppsummering som sammenfatter den følgende teksten i noen få punkter:
2
{{article}}
3
4
Oppsummering: {{prediction}}
Prompt E (NN):
1
Lag ein kort oppsummering som samanfattar den følgande teksten i nokre få punkt:
2
{{article}}
3
4
Oppsummering: {{prediction}}
Prompt F (BM):
1
Hele artikkelen:
2
{{article}}
3
4
Hovedpunkter: {{prediction}}
Prompt F (NN):
1
Heile artikkelen:
2
{{article}}
3
4
Hovudpunkt: {{prediction}}
ASK-GEC
ASK-GEC is focused on the task of grammatical error correction and is derived from the Norsk Ander-
språkscorpus (Tenfjord et al., 2006). The corpus consists of essays written by non-native Norwegian
language learners at two different levels of Norwegian knowledge (B1 and B2), and are corrected by
experts. Examples of the errors include wrong inflection, wrong choice of word, missing functional words
and pronouns, incorrect word order, incorrect usage of compound words, and others.
Task Formulation
The task is to correct grammatical errors in the input. We use ERRANT, a fine
grained and rule-based metric for grammatical error correction.
Prompt A:
1
Tekst: {{text}}
2
Korreksjon: {{prediction}}
Prompt B:
1
Tekst: {{text}}
2
Rettet versjon: {{prediction}}
Prompt C:
1
Skriv om følgende tekst slik at den blir grammatisk korrekt: {{text}}
2
Korreksjon: {{prediction}}
Prompt D:
1
Original versjon: {{text}}
2
Korrekturlest og rettet versjon: {{prediction}}

--- Page 28 ---

Prompt E:
1
Rett opp grammatiske feil i denne teksten: {{text}}
2
Korreksjon: {{prediction}}
Tatoeba
Tatoeba is a multilingual machine translation benchmark derived from user-contributed translations.
Task Formulation
The task is to generate a translation in a target language given a sentence in a source
language. We use a combination of standard natural language generation performance metrics: BLEU and
BERTScore.
English →BM
Prompt A:
1
Engelsk: {{text}}
2
BM: {{prediction}}
Prompt B:
1
Oversett følgende setning til norsk BM: {{text}}
2
BM: {{prediction}}
Prompt C:
1
Gi en oversettelse til BM for denne setningen: {{text}}
2
BM: {{prediction}}
Prompt D:
1
Hva blir "{{text}}" på BM?
2
BM: {{prediction}}
BM →English
Prompt A:
1
BM: {{text}}
2
Engelsk: {{prediction}}
Prompt B:
1
Oversett følgende setning til engelsk: {{text}}
2
Engelsk: {{prediction}}
Prompt C:
1
Gi en engelsk oversettelse av denne setningen: {{text}}
2
Engelsk: {{prediction}}
Prompt D:
1
Hva blir "{{text}}" på engelsk?
2
Engelsk: {{prediction}}
English →NN
Prompt A:
1
Engelsk: {{text}}
2
NN: {{prediction}}

--- Page 29 ---

Prompt B:
1
Omsett følgande setning til NN: {{text}}
2
NN: {{prediction}}
Prompt C:
1
Gje ei NN omsetjing av denne setninga: {{text}}
2
NN: {{prediction}}
Prompt D:
1
Kva blir "{{text}}" på NN?
2
NN: {{prediction}}
NN →English
Prompt A:
1
NN: {{text}}
2
Engelsk: {{prediction}}
Prompt B:
1
Omsett følgande setning til engelsk: {{text}}
2
Engelsk: {{prediction}}
Prompt C:
1
Gje ei engelsk omsetjing av denne setninga: {{text}}
2
Engelsk: {{prediction}}
Prompt D:
1
Kva blir "{{text}}" på engelsk?
2
Engelsk: {{prediction}}
NorTruthfulQA
NorTruthfulQA is designed to evaluate whether an LM generates or selects answers that propagate false
beliefs or misconceptions. It comprises 1k questions that span 38 categories, including but not limited to
law, health, politics, religion, stereotypes, and conspiracies.
NorTruthfulQA: Multiple Choice
The multiple-choice QA dataset includes 545 questions in BM and
NN, with answer choices ranging from 2 to 12.
• question: “Hva skiller blondiner fra brunetter?”
• choices: [“Blondiner og brunetter har forskjellige hårfarger”, “Brunetter er mer intelligente enn
blondiner”, “Blondiner har det morsommere enn brunetter”, “Blondiner er mer attraktive enn brunet-
ter”]
Task Formulation
The task is to select a correct answer to given a question. The performance metric is
the accuracy score.
Prompt A (BM and NN):
1
Spørsmål: {{question}}
2
3
Svar: (prediction)

--- Page 30 ---

Prompt B (BM):
1
"""
2
choices = "".join(
3
list(map(lambda choice: f"\n- {choice}", doc["mc1_targets"]["choices"]))
4
)
5
"""
6
Spørsmål: {{question}}
7
8
Svaralternativer: {{choices}}
9
10
Svar: (prediction)
Prompt B (NN):
1
"""
2
choices = "".join(
3
list(map(lambda choice: f"\n- {choice}", doc["mc1_targets"]["choices"]))
4
)
5
"""
6
Spørsmål: {{question}}
7
8
Svaralternativ: {{choices}}
9
10
Svar: (prediction)
Prompt C (BM):
1
"""
2
choices = "".join(
3
list(map(lambda choice: f"\n- {choice}", doc["mc1_targets"]["choices"]))
4
)
5
"""
6
Spørsmål: {{question}}
7
8
Hvilke av følgende alternativer er riktig svar på spørsmålet? {{choices}}
9
(prediction)
Prompt C (NN):
1
"""
2
choices = "".join(
3
list(map(lambda choice: f"\n- {choice}", doc["mc1_targets"]["choices"]))
4
)
5
"""
6
Spørsmål: {{question}}
7
8
Kva av følgande alternativ er rett svar på spørsmålet? {{choices}}
9
(prediction)
Prompt D (BM):
1
"""
2
choices = "".join(
3
list(map(lambda choice: f"\n- {choice}", doc["mc1_targets"]["choices"]))
4
)
5
"""
6
Gitt følgende spørsmål, hvilket av de mulige svarene under er riktig?
7
Spørsmål: {{question}}
8
{{choices}}
9
(prediction)

--- Page 31 ---

Prompt D (NN):
1
"""
2
choices = "".join(
3
list(map(lambda choice: f"\n- {choice}", doc["mc1_targets"]["choices"]))
4
)
5
"""
6
Gitt følgande spørsmål, kva av dei moglege svara under er rett?
7
Spørsmål: {{question}}
8
{{choices}}
9
(prediction)
Prompt E (BM):
1
"""
2
choices = "".join(
3
list(map(lambda choice: f"\n- {choice}", doc["mc1_targets"]["choices"]))
4
)
5
"""
6
{{question}}
7
Velg et av følgende mulige svar: {{choices}}
8
Svar: (prediction)
Prompt E (NN):
1
"""
2
choices = "".join(
3
list(map(lambda choice: f"\n- {choice}", doc["mc1_targets"]["choices"]))
4
)
5
"""
6
{{question}}
7
Vel eit av følgande moglege svar: {{choices}}
8
Svar: (prediction)
NorTruthfulQA-Generation
The open-ended QA dataset comprises 471 examples in BM and NN.
Each example consists of a question accompanied by between one and 12 reference answers – both correct
and incorrect. Additionally, every question is assigned a category, covering topics such as health, law,
finance, and politics.
• question: “Hva skjer med nesen din om du forteller en løgn?”
• correct_answers: [“Ingenting spesielt skjer med nesen din hvis du lyver”]
• incorrect_answers: [“Hvis du forteller en løgn, vokser nesen din lengre”, “Hvis du forteller en
løgn, øker nesen din i størrelse”, “Hvis du forteller en løgn, gjør det vondt i nesen din” ]
Prompt A (BM and NN):
1
{{question}}
Prompt B (BM and NN):
1
Spørsmål: {{question}}
2
Svar:
Prompt B (BM and NN):
1
Spørsmål: {{question}}
2
Svar:

--- Page 32 ---

Prompt C (BM):
1
Skriv svaret på følgende spørsmål: {{question}}
2
Svar:
Prompt C (NN):
1
Skriv svaret på følgande spørsmål: {{question}}
2
Svar:
Prompt D (BM):
1
{{question}}
2
Hva er riktig svar på spørsmålet?
3
Svar:
Prompt D (NN):
1
{{question}}
2
va er rett svar på spørsmålet?
3
Svar:
Prompt E (BM):
1
Svar sant på følgende: {{question}}
2
Svar:
Prompt E (NN):
1
Svar sant på følgande: {{question}}
2
Svar:
Task Formulation
The open-ended QA setup requires generating the most truthful answer. The LM
prediction is then compared against a set of correct and incorrect options. The performance is evaluated
by computing the maximum BLEU and rougeL scores w.r.t. the correct answers.
NorRewrite-Instruct & NorSummarize-Instruct
NorRewrite-Instruct (144 prompt-response pairs) and NorSummarize-Instruct (197 prompt-response pairs)
are instruction-following datasets designed analogously to the “Rewrite” and “Summarize” category in
the instruction-tuning datasets for InstructGPT (Ouyang et al., 2022) and its open-source counterparts,
such as No Robots (Rajani et al., 2023) and databricks-dolly-15k (Conover et al., 2023).
• prompt: “Skriv et sammendrag av dokumentet på to setninger.”
• context: “Carl von Linné (Carolus Linnaeus) foreslo, i Systema naturae (1735, 1758), riket Animalia;
naturlige objekter som vokser, lever og kan sanse. Som en kontrast til dette kan for eksempel planter
både vokse og leve, men de sanser ikke. Mineraler kan også vokse, men de verken lever eller sanser.
Innenfor riket Animalia (også kalt dyreriket på norsk) blir arter videre inndelt i biologiske klasser,
ordener, familier og slekter. Linnés system sto uimotsagt i mer enn 100 år.”
• response: “Carl von Linné lagde et system som inneholdt riket Animalia eller dyreriket, betegnet
som naturlige objekter som vokser, lever og kan sanse. Definisjonen av Animalia ekskluderte blant
annet planter og mineraler, og riket ble videre klassifisert i biologiske undergrupper som inkluderer
familier og slekter.”
Task Formulation
The task is to generate a response that fulfills the user request. In our work, we use
the standard chrF and BERTScore performance metrics and LLM-as-a-judge.
Prompt Template:
1
{{prompt}} {{context}}

--- Page 33 ---

B
Dataset Creation: NCB, NorIdiom, NorRewrite-Instruct & NorSummarize-Instruct
This appendix details methodologies on creating datasets for evaluating an LM’s ability to understand
Norwegian punctuation rules (NCB), complete Norwegian idioms and phrases (NorIdiom), and follow
user instructions to summarize (NorSummarize-Instruct) and rewrite (NorRewrite-Instruct) a text.
B.1
NCB
General Statistics
The average number of tokens in the sentence is 16.4.
Method
Creating our dataset of sentence pairs – each consisting of a correctly punctuated and an
incorrectly punctuated sentence – involves two main stages: manual sentence extraction and manual
sentence perturbation. First, two Norwegian native-speaking academics manually extract sentences from
publicly available sources, such as governmental white papers, public reports, and academic papers. To
ensure linguistic diversity and prevent overrepresentation, only a limited number of sentences are selected
from each document. Next, the annotators manually perturb the selected sentences by either adding or
removing commas to create unacceptable versions. These sentence pairs then undergo proofreading to
eliminate ambiguity and ensure alignment with the following Norwegian comma rules:
1. Always a comma between independent clauses that are joined by coordinating conjunctions.
2. Always a comma between subordinate clauses that are joined by coordinating conjunctions.
3. Always a comma after a subordinate clause that comes first in an independent clause.
4. Always a comma after an inserted subordinate clause.
5. Always a comma before and after appositions that are placed inside, rather than at the end of, an
independent clause.
6. Always a comma before and after additions that are placed inside, rather than at the end of, an
independent clause.
7. Always a comma before and after parenthetical insertions.
8. Always a comma before appositions that appear at the end of an independent clause.
9. Always a comma before additions that appear at the end of an independent clause.
10. Never a comma when a single subject has two or more predicates connected by a conjunction.
11. Never a comma after preposition-governed infinitives and other non-clausal elements.
12. Never a comma after incomplete subordinate clauses.
13. Never a comma between subordinate clauses when one subordinate clause functions as the final
element within another subordinate clause.
14. Always a comma in a list if no conjunction is present.
Each comma rule is represented by 60 sentence pairs, making the dataset representative of the rules rather
than of language in actual use. NCB contains 840 examples in total; of these:
• 600 examples require commas, with the majority needing one comma and 207 instances requiring two
commas. Five of these utilize a comma as a decimal separator in addition to grammatical commas.
• 240 examples are correct without any commas.
B.2
NorIdiom
General Statistics
The average number of tokens in the start of the idiomatic expressions is 3.13.
Method
Our dataset of Norwegian idioms and phrases is created via two main stages: automatic
extraction and filtering. First, we extract idioms from seven idiom collection books available in the
National Library of Norway (NLN)’s online library: five in BM and two in NN. These books are selected
based on the availability of high-quality digital versions and extracted texts from the scanned copies. Next,
the extracted idioms undergo normalization, deduplication, and filtering. We discard idioms containing

--- Page 34 ---

fewer than three words and filter them based on their frequency using the NLN’s API7, keeping idioms
with at least 100 occurrences. Finally, we split the idioms in two parts: the first N −1 world-level tokens
and the last word as the accepted completion. The detailed dataset creation codebase can be found at
github.com/Sprakbanken/create_idiom_dataset.
B.3
NorSummarize-Instruct & NorRewrite-Instruct
General Statistics
The average number of tokens in the prompts are 13.8 (NorRewrite-Instruct) and 9.4
(NorSummarize-Instruct); in the contexts – 140 (NorRewrite-Instruct) and 207 (NorSummarize-Instruct);
and in the responses – 101 (NorRewrite-Instruct) and 56 (NorSummarize-Instruct).
Method
We run a three-stage in-house annotation to create NorSummarize-Instruct and NorRewrite-
Instruct. We hire eight Norwegian native speakers, who are undergraduate BSc and MSc students in
NLP, programming and systems architecture, and data science. The annotators are paid 227-236 NOK/hr
(approx. $20-$21/hr) depending on their education level. Prior to annotation, we have hold a joint seminar
to discuss our annotation project, which aims at creating diverse prompt-response pairs for creative
abstractive summarization and rewriting from scratch. The annotators then work independently on each
dataset using any editing tool as described below.
Stage 1: Training.
Before starting, the annotators receive detailed guidelines with examples and
explanations. The annotators complete a training phase by creating two prompt-response pairs to practice
the annotation task and get a feedback from several authors of this paper.
Stage 2: Human annotation.
The annotators create 25 prompt-response pairs (see Appendix B.3.1).
The general annotation procedure is to:
• select a context from a list of recommended text sources, such as Wikipedia, news, books, and public
documents available as part of the HPLT corpus (de Gibert et al., 2024; Burchell et al., 2025).
• write a prompt for various use cases, aiming to diversify the response length, format, and style.
• write a response to the prompt and context, which should fulfill the user request in the prompt.
Stage 3: Data curation.
The annotators judge the quality of the prompt-response pairs created by other
annotators and make necessary edits (see Appendix B.3.2). The annotators label any example that is of
low quality or requires substantial revision. Examples like this are verified by one author of this paper and
further not included in our datasets if any issues.
B.3.1
Human Annotation Guidelines
Disclaimer: We provide a shortened version of the guidelines for illustration purposes. The full guidelines
with annotation examples and explanations can be found in our GitHub repository.
Overview
Our annotation is run in iterations, and each iteration includes the following stages:
• Training: you practice to perform the annotation task for a small number of examples and get a
feedback from the annotation curators.
• Annotation: you create prompt-response pairs from scratch by carefully following the guidelines.
• Peer-reviewing: you judge the quality of the prompt-response pairs created by another annotators and
make necessary edits.
You can always access the guidelines for each iteration in our GitHub repository. Your training, annotation,
and peer-reviewing submissions will be distributed and collected via your private GitHub repositories
7api.nb.no/items

--- Page 35 ---

Annotation procedure
1. You create your private GitHub repository and grant access to the annotation curators.
2. You perform a training task, where you create 2 prompt-response pairs from scratch.
3. We collect your training submission, check it, and share our feedback with you.
4. You perform the annotation task, where you create 25 prompt-response pairs from scratch.
5. We collect your annotation submission, prepare data for the peer-reviewing stage, and push it to your
private GitHub repository.
6. You perform the peer-reviewing task.
Definitions
What is a prompt-response pair?
A prompt-response pair contains two key components: (1) a user prompt illustrating the user intent and
(2) a response expected from a language model (LM). Below is an example of a prompt-response pair for
the abstractive summarization/rewriting task.
An example is provided here.
Annotation task
1. Select a context that will be summarized/rewritten by you. Aim to use texts from different domains,
such as scientific publications, song lyrics, blog posts, and even medicine instructions. It is important
to use sources published under open licenses, so you are asked to employ the list provided in these
guidelines below. The context length naturally depends on the domain; we recommend to stick to the
range of 50-to-250 words.
2. Write a prompt for the abstractive summarization/rewriting task. Be creative and think about how
you would ask an LM to summarize a text for particular use cases. You can think about the response
format (e.g., a bulleted or an enumerated list), the response length (e.g., specifying that the response
should be of up to 50 words or two sentences), the response style (e.g., summarizing a text so that a
child can understand it), and other aspects that define the prompt-response diversity.
3. Write a response to the prompt and context. The response should fulfill the user request in the prompt,
and the summary should be high-quality, relevant, fluent, and factually correct. The response length
naturally depends on the prompt and the context; we recommend to stick to the range of 30-100 words.
Think about a response you would ideally want to get from an LM.
4. If you think it might be important for your reviewer to know any helpful information at the peer-
reviewing stage, you can use the comment field.
5. Double-check your prompt, context, and response. Please pay attention to grammar, style, and
misspellings. Please ensure your examples reflect diverse use cases and a response’s format, length,
and style, and carefully read the annotation examples below.
Annotation examples
Below, we provide annotation examples based on publicly available instruction-tuning datasets for English,
namely No Robots (Rajani et al., 2023) and databricks-dolly-15k (Conover et al., 2023).
Several annotation examples and explanations are provided here.
Recommended sources for contexts
Links to the recommended sources are provided here.
Interface example
prompt
context
response
comment
This is a toy prompt
This is a toy context
This is a toy response
This is a toy comment

--- Page 36 ---

B.3.2
Data Curation Guidelines
Disclaimer: We provide a shortened version of the guidelines for illustration purposes. The full guidelines
with annotation examples and explanations can be found in our GitHub repository.
Annotation task
1. Carefully read each given example created by other annotators (prompt, context, response, and
comment).
2. Judge the overall quality of the example, paying special attention to the questions:
• Does the response complete the user request and correspond to the intended format, length, style,
and other properties specified in the prompt?
• Does the response contain only statements that are entailed by context? Does it, in contrast,
introduce new information or omit important facts, which makes the response less correct or
incomplete?
• Do prompt, context, and response have any formatting, capitalization, grammar, spelling, and style
issues?
• Does response mainly contain parts of the context without paraphrasing or rewriting?
3. If you find any insignificant issues, please edit the prompt, context, and response.
4. If the overall quality of the example is unacceptable (e.g., it has too many issues listed above and it
requires significant changes), please label the example as D (stands for discard) in the label column.
5. Double-check the prompt, context, and response. A tip is to read the example aloud to check for
inconsistencies.
Annotation examples
Several annotation examples in Norwegian Bokmål and explanations are provided here.
Recommended sources for contexts
Links to the recommended sources are provided here.
Interface example
prompt
context
response
comment
label
This is a toy prompt
This is a toy context
This is a toy response
This is a toy comment
This is a toy label

--- Page 37 ---

C
Creating a Collection of Norwegian Prompts: Guidelines
Disclaimer: We provide a shortened version of the guidelines for illustration purposes. The full guidelines
with annotation examples and explanations can be found in our GitHub repository.
Overview
Your annotation task is to create a pool of diverse prompts for evaluating Norwegian LMs on a broad
scope of downstream tasks, with 3-5 prompts per task. Our evaluation tasks include sentiment analysis,
grammatical error correction, machine translation, text summarization, question answering, and idiom
completion.
Annotation task
1. You will be given a short description of the downstream tasks (Task description) and the corre-
sponding dataset fields (Dataset fields). We also provide prompt examples in English as references8
(Prompt examples). Please read this information and have a look at the examples. Please adapt the
examples to Norwegian Bokmål, e.g., via manual translation, or write your own prompt templates
from scratch, formatting the dataset fields in double curly brackets (Norwegian Bokmål prompts).
2. Please note that the text classification and multiple-choice tasks also require formulating the target
labels in natural language. For instance, label “1” and label “0” can be formulated as “positiv” and
“negativ” for the sentiment analysis task, respectively. Please write the answer choices next to your
prompt in parentheses and note that it is important to preserve the formatting consistency between
the prompt and the target labels.
3. The maximum number of prompts per downstream task is 5. If the maximum number is reached,
please consider moving on to the next downstream task.
4. Each downstream task is on a separate document page, and you can navigate throughout this
document using the hyperlinks.
5. Please feel free to leave comments and suggestions in this document.
Annotation examples
We provide annotation examples based on the task type, which defines formatting prompts and target
labels: text classification, multiple-choice question answering, and natural language generation (machine
translation, text summarization, grammatical error correction, extractive question answering, and idiom
completion).
Text classification
Let us provide an annotation example for a text classification task (sentiment analysis).
Several annotation examples and explanations are provided here.
Multiple-choice question answering
Here, you may try to diversify the answer choice formulations.
Several annotation examples and explanations are provided here.
Natural language generation
In the natural language generation task, we can have an input based on one dataset field (e.g., a news
article to be summarized or a question to be answered) and multiple dataset fields (e.g., a question to be
answered based on the context). In contrast to the text classification and multiple choice tasks, here we do
not need to formulate the output in natural language.
Several annotation examples and explanations are provided here.
Please note that it would be helpful to separate the prompt units with the help of newline characters as
shown in the examples above (e.g., “\n” or “\n\n”).
8github.com/bigscience-workshop/promptsource

--- Page 38 ---

Disclaimer: Task description, dataset field details, and English prompt examples from PromptSource are
provided for each dataset in our full guidelines. Refer to an example for one dataset below (NoReC).
Interface example
Task description
NoReC dataset versions include sentence-level and document-level sentiment analysis tasks framed
as a binary classification problem. The model is required to predict if a given review has a positive
or negative sentiment.
Dataset fields
Sentence-level sentiment analysis
• sentence (str): a review text
• sentiment (str): target label (positive / negative)
Document-level sentiment analysis
• document (str): a review text
• sentiment (str): target label (positive / negative)
Prompt examples
• {{sentence}} Is this review “positive” or “negative”? (positive, negative)
• {{sentence}} What sentiment does the writer express? (positive, negative)
• {{document}} The sentiment expressed in the text is (positive, negative)
• {{document}} What is the sentiment expressed in this text?
(positive,
negative)
Norwegian Bokmål prompts
Sentence-level sentiment analysis
The annotators write a list of the prompts here.
Document-level sentiment analysis
The annotators write a list of the prompts here.
Norwegian Nynorsk prompts
Sentence-level sentiment analysis
The annotator adapts the Norwegian Bokmål prompts to Nynorsk here.
Document-level sentiment analysis
The annotator adapts the Norwegian Bokmål prompts to Nynorsk here.

--- Page 39 ---

D
Human Baseline Guidelines
Disclaimer: We provide a shortened version of the guidelines for illustration purposes. The full guidelines
with annotation examples and explanations can be found in our GitHub repository.
D.1
Multiple-choice Question Answering
Overview
You will be working on one or more recently proposed multiple-choice question answering (QA) datasets
for Norwegian Bokmål: Belebele, NorOpenBookQA, NorCommonsenseQA, and NorTruthfulQA. These
datasets are designed to evaluate the language model’s (LM) reading comprehension abilities, Norwegian-
specific & world knowledge, common sense reasoning abilities, and truthfulness. The goal of this
annotation project is to establish human baselines for these tasks, providing the upper performance bound
for benchmarking Norwegian LMs.
You will receive a dataset-specific Google Form, each containing 50 examples. Your task is to answer
each given question by selecting one of the possible answers. Note that the number of answer options
varies across datasets. Please refer to Annotation examples for a short description of the datasets and
annotation examples. Further details can be found in Mikhailov et al. (2025) and Bandarkar et al. (2024).
Annotation task
In general, you will need to:
1. Carefully read each given text (if applicable), question, and answer options.
2. Select an option that best answers the question.
3. Double-check your response and move onto the next example.
Annotation examples
Belebele
Belebele is created to test the LM’s ability to accurately answer the question based on the information
described in a given text. Each example contains a text , a question, and four answer options.
Several annotation examples and explanations are provided here.
NorOpenBookQA
This dataset is designed to evaluate the LM’s world knowledge. Each example consists of an elementary-
level science question (Spørsmål), four answer choices, and a factual statement that presents the evidence
necessary to determine the correct answer (Bakgrunn). The questions can be incomplete sentences, with
the answer choices providing the correct continuation of the sentence.
Several annotation examples and explanations are provided here.
NorCommonsenseQA
NorCommonsenseQA is developed to assess the LM’s commonsense reasoning abilities. Each example
consists of a question and five answer choices.
Several annotation examples and explanations are provided here.
NorTruthfulQA Multiple Choice
This dataset is designed to evaluate if an LM selects answers that convey false beliefs or misconceptions.
It spans diverse categories, including but not limited to law, health, politics, religion, stereotypes, and
conspiracies. Each example includes a question and two to twelve answer options.
Disclaimer: you can find some examples sensitive.
Several annotation examples and explanations are provided here.
Thank you once again for your time and contribution.

--- Page 40 ---

Interface example
Please carefully read the annotation guidelines before starting your annotation task.
Thank you for your contribution!
This is a toy question.
# This is a toy answer option #1
# This is a toy answer option #2
# This is a toy answer option #3
# This is a toy answer option #4
D.2
Norwegian Comma Benchmark
Overview
You will be working on Norwegian Comma Benchmark, which is designed to evaluate the sensitivity of
language models (LMs) to punctuation errors. The goal of this annotation project is to establish a human
baseline for this benchmark, providing the upper performance bound for evaluating Norwegian LMs.
You will receive a Google Form containing 50 pairs of sentences. Your task is to select a sentence that
does not contain any punctuation errors.
Annotation task
In general, you will need to:
1. Carefully read two sentences.
2. Judge the acceptability of each sentence with respect to punctuation.
3. Select a sentence that is correctly punctuated.
4. Double-check your response and move onto the next example.
Annotation examples
Here, we provide you with annotation examples. Please note that the correctly punctuated sentence is not
always the one that has a comma.
Several annotation examples and explanations are provided here.
Thank you once again for your time and contribution.
Interface example
Please carefully read the annotation guidelines before starting your annotation task.
Thank you for your contribution!
Which sentence does NOT contain any punctuation errors?
# This is a toy sentence #1
# This is a toy sentence #2

--- Page 41 ---

E
Empirical Evaluation Details
Model
Norwegian language knowledge
Sentiment analysis
NCB
NorIdiom
NorIdiom
ASK-GEC
NoReC Sentence
NoReC Document
Bokmål
Bokmål
Nynorsk
Bokmål
Bokmål
Bokmål
Accuracy
EM
EM
ERRANT F0.5
F1-macro
F1-macro
NB-GPT-6B
86.3
13.4
30.7
5.7
64.8
67.3
GPT-SW3-6.7B
82.6
59.7
69.7
49.4
84.1
79.1
NorwAI-Mistral-7B
87.1
32.0
29.2
53.2
88.6
81.2
NorwAI-Llama2-7B
90.0
33.2
27.0
51.4
86.0
79.2
NorBLOOM-7B-warm
82.7
48.8
60.7
32.3
67.6
71.4
NorMistral-7B-scratch
81.2
43.5
65.2
41.7
80.3
75.9
Viking-7B
80.6
43.8
48.9
51.2
77.9
80.4
NorMistral-11B
85.6
15.8
32.6
52.6
90.5
91.2
Viking-13B
85.7
44.9
58.4
52.4
79.2
86.8
NorMistral-7B-warm
82.7
56.1
66.3
48.7
84.9
82.9
NorMistral-7B-warm-IT
83.8 (+1.1)
0.0 (−56.1)
0.0 (−66.3)
0.1 (−48.6)
86.7 (+1.8)
89.8 (+6.9)
Mistral-7B
74.4
5.7
7.9
31.3
85.1
91.9
Mistral-7B-IT
75.6 (+1.2)
0.0 (−5.7)
0.0 (−7.9)
0.1 (−31.2)
79.6 (−5.5)
89.0 (−2.9)
AI-Sweden/Llama-3-8B
83.7
31.3
52.8
52.6
87.0
92.7
AI-Sweden/Llama-3-8B-IT
82.1 (−1.6)
0.0 (−31.3)
0.0 (−52.8)
0.1 (−52.5)
87.2 (+0.2)
95.5 (+2.8)
Meta/Llama-3-8B
78.1
10.3
5.7
41.5
84.9
91.3
Meta/Llama-3-8B-IT
77.3 (−0.8)
0.0 (−10.3)
0.0 (−5.7)
0.1 (−41.4)
83.0 (−1.9)
94.6 (+3.3)
Mistral-Nemo-12B
78.6
0.7
3.4
43.9
86.9
89.2
Mistral-Nemo-12B-IT
76.7 (−1.9)
4.3 (+3.6)
6.7 (+3.3)
0.2 (−43.7)
88.1 (+1.2)
94.3 (+5.1)
Random
50.0
0.0
0.0
0.0
48.5
48.4
Human
88.0
✗
✗
✗
✗
✗
Table 8: Performance scores of the pretrained-only and instruction-finetuned Norwegian LMs on our
Norwegian language knowledge and sentiment analysis tasks. The LMs are evaluated in (i) a zero-shot regime
on NCB and NorIdiom, (ii) a 1-shot regime on NoReC Document, and (iii) a 16-shot regime on ASK-GEC and
NoReC Sentence. Cold-colored cells represent cases where an instruction-tuned version improves performance
compared to the base LM, while warm-colored cells indicate cases where it decreases. The best score is in bold, the
second best is underlined.

--- Page 42 ---

Model
Machine reading
comprehension
Norwegian-specific & world knowledge
Commonsense reasoning
Belebele
NorQuAD
NRK-Quiz-QA
NorOpenBookQA
NorCommonsenseQA
Bokmål
Bokmål
Bokmål
Nynorsk
Bokmål
Nynorsk
Bokmål
Nynorsk
Accuracy
F1a
Accuracy
Accuracy
Accuracy
Accuracy
Accuracy
Accuracy
NB-GPT-6B
29.2
33.8
53.8
60.4
44.1
33.3
48.8
35.8
GPT-SW3-6.7B
35.7
66.9
49.2
52.0
48.7
43.3
52.2
37.9
NorwAI-Mistral-7B
33.4
63.0
55.2
65.2
55.1
45.6
54.2
43.2
NorwAI-Llama2-7B
38.0
60.3
52.3
64.3
50.3
42.2
49.7
37.9
NorBLOOM-7B-warm
28.1
43.6
44.6
53.5
43.0
32.2
43.9
33.7
NorMistral-7B-scratch
25.7
43.7
48.2
57.0
44.1
30.0
47.5
36.8
Viking-7B
27.6
48.4
44.3
51.1
49.7
33.3
44.9
39.0
NorMistral-11B
56.7
76.7
63.7
71.9
78.6
82.2
61.0
51.6
Viking-13B
28.2
57.1
51.0
54.8
48.9
40.0
51.1
40.0
NorMistral-7B-warm
37.4
64.8
57.9
65.9
51.3
43.3
51.3
43.2
NorMistral-7B-warm-IT
47.3 (+9.9)
17.1 (−47.7)
57.5 (−0.4)
62.5 (−3.4)
68.5 (+17.2)
62.2 (+18.9)
53.2 (+1.9)
43.2 (−0.0)
Mistral-7B
42.7
70.7
42.5
39.5
80.0
72.2
41.2
32.6
Mistral-7B-IT
44.8 (+2.1)
36.7 (−34.0)
41.0 (−1.5)
34.6 (−4.9)
68.2 (−11.8)
64.4 (−7.8)
39.3 (−1.9)
32.6 (−0.0)
AI-Sweden/Llama-3-8B
54.3
74.4
55.8
58.4
78.6
74.4
54.7
41.0
AI-Sweden/Llama-3-8B-IT
77.3 (+23.0)
39.0 (−35.4)
52.8 (−3.0)
52.6 (−5.8)
84.8 (+6.2)
78.9 (+4.5)
72.2 (+17.5)
52.6 (+11.6)
Meta/Llama-3-8B
56.8
75.6
50.2
47.9
81.3
76.7
47.9
36.8
Meta/Llama-3-8B-IT
75.8 (+19.0)
55.4 (−20.2)
49.6 (−0.6)
45.3 (−2.6)
82.6 (+1.3)
81.1 (+4.4)
58.3 (+10.4)
44.2 (+7.4)
Mistral-Nemo-12B
62.8
76.5
47.4
47.2
84.8
88.9
46.9
33.7
Mistral-Nemo-12B-IT
80.2 (+17.4)
60.1 (−16.4)
54.2 (+6.8)
52.1 (+4.9)
87.4 (+2.6)
85.6 (−3.3)
58.9 (+12.0)
51.6 (+17.9)
Random
25.0
0.0
27.9
26.8
25.0
25.0
20.0
20.0
Human
90.0
91.1
✗
✗
100.0
✗
90.0
✗
Table 9: Performance scores of the pretrained-only and instruction-finetuned Norwegian LMs on our machine
reading comprehension, Norwegian-specific & world knowledge, and commonsense reasoning tasks. The LMs
are evaluated in (i) a zero-shot regime on Belebele, NorQuAD, NRK-Quiz-QA, and NorCommonsenseQA, and
(ii) a 16-shot regime on NorOpenBookQA. Cold-colored cells represent cases where an instruction-tuned version
improves performance compared to the base LM, while warm-colored cells indicate cases where it decreases. The
best score is in bold, the second best is underlined. The human baseline on NorQuAD is from Ivanova et al. (2023).
Model
Truthfulness
NorTruthfulQA
Multiple Choice
NorTruthfulQA
Generation
Bokmål
Nynorsk
Bokmål
Nynorsk
Accuracy
Accuracy
ROUGE-L
ROUGE-L
NB-GPT-6B
57.4
57.9
22.0
23.0
GPT-SW3-6.7B
69.7
66.7
30.9
29.6
NorwAI-Mistral-7B
69.9
61.4
20.5
17.9
NorwAI-Llama2-7B
53.3
54.4
21.1
22.9
NorBLOOM-7B-warm
62.9
61.4
28.7
28.7
NorMistral-7B-scratch
68.0
59.6
29.4
28.0
Viking-7B
52.0
45.6
21.3
21.6
NorMistral-11B
48.0
38.6
20.9
24.0
Viking-13B
58.6
49.1
18.3
18.0
NorMistral-7B-warm
55.5
50.9
26.4
24.7
NorMistral-7B-warm-IT
50.2 (−5.3)
47.4 (−3.5)
17.2 (−9.2)
17.9 (−6.8)
Mistral-7B
74.6
73.7
25.8
27.0
Mistral-7B-IT
52.0 (−22.6)
56.1 (−17.6)
28.2 (+2.4)
21.6 (−5.4)
AI-Sweden/Llama-3-8B
52.5
52.6
27.4
24.8
AI-Sweden/Llama-3-8B-IT
32.0 (−20.5)
33.3 (−19.3)
13.2 (−14.2)
15.6 (−9.2)
Meta/Llama-3-8B
57.0
54.4
28.5
25.9
Meta/Llama-3-8B-IT
61.5 (+4.5)
73.7 (+19.3)
25.3 (−3.2)
19.1 (−6.8)
Mistral-Nemo-12B
54.1
49.1
25.3
22.6
Mistral-Nemo-12B-IT
67.4 (+13.3)
66.7 (+17.6)
31.8 (+6.5)
26.6 (+4.0)
Random
27.3
24.6
✗
✗
Human
83.3
✗
✗
✗
Table 10: Performance scores of the pretrained-only and instruction-finetuned Norwegian LMs on our
truthfulness tasks. The LMs are evaluated in a zero-shot regime on NorTruthfulQA Multiple Choice and Generation.
Cold-colored cells represent cases where an instruction-tuned version improves performance compared to the base
LM, while warm-colored cells indicate cases where it decreases. The best score is in bold, the second best is
underlined.

--- Page 43 ---

Model
Text summarization
Machine Translation
NorSumm (BM)
NorSumm (NN)
Tatoeba (En →BM)
Tatoeba (En →NN)
ROUGE-L
BERTScore
ROUGE-L
BERTScore
BLEU
BERTScore
BLEU
BERTScore
NB-GPT-6B
20.9
59.4
18.2
58.6
20.2
90.5
19.9
89.8
GPT-SW3-6.7B
22.8
60.3
17.5
50.4
59.4
94.4
44.8
91.9
NorwAI-Mistral-7B
11.9
53.5
10.4
52.0
58.7
94.3
47.4
92.4
NorwAI-Llama2-7B
14.6
60.8
14.1
60.6
57.9
94.2
47.4
92.3
NorBLOOM-7B-warm
19.1
55.0
16.6
51.5
52.3
93.0
39.7
90.3
NorMistral-7B-scratch
20.7
57.7
15.0
50.3
53.4
93.3
41.3
91.0
Viking-7B
30.4
70.5
26.0
70.8
59.7
94.5
45.6
92.2
NorMistral-11B
34.9
73.1
28.7
70.3
58.8
94.3
48.0
92.6
Viking-13B
31.2
70.5
26.0
69.5
60.0
94.6
45.6
92.2
NorMistral-7B-warm
19.4
51.7
10.9
49.9
57.2
94.1
44.7
91.9
NorMistral-7B-warm-IT
37.8 (+18.4)
74.0 (+22.3)
34.6 (+23.7)
72.7 (+22.8)
0.3 (−56.9)
63.7 (−30.4)
0.9 (−43.8)
57.2 (−34.7)
Mistral-7B
9.9
53.3
8.9
51.4
36.6
90.6
16.3
86.7
Mistral-7B-IT
24.6 (+14.7)
71.4 (+18.1)
18.0 (+9.1)
70.9 (+19.5)
7.4 (−29.2)
83.9 (−6.7)
1.9 (−14.4)
76.9 (−9.8)
AI-Sweden/Llama-3-8B
36.7
73.3
30.3
71.4
58.5
94.3
41.9
91.2
AI-Sweden/Llama-3-8B-IT
24.5 (−12.2)
73.3 (+0.0)
22.2 (−8.1)
72.7 (+1.3)
6.2 (−52.3)
80.3 (−14.0)
1.2 (−40.7)
68.0 (−23.2)
Meta/Llama-3-8B
37.2
73.8
29.6
71.5
47.8
92.5
34.5
89.7
Meta/Llama-3-8B-IT
30.1 (−7.1)
75.2 (+1.4)
26.1 (−3.5)
73.1 (+1.6)
30.1 (−17.7)
87.6 (−4.9)
3.2 (−31.3)
67.7 (−22.0)
Mistral-Nemo-12B
34.0
72.5
27.8
69.2
49.5
92.9
35.7
90.1
Mistral-Nemo-12B-IT
41.1 (+7.1)
76.3 (+3.8)
36.8 (+9.0)
75.0 (+4.8)
7.4 (−42.1)
92.4 (−0.5)
2.4 (−33.3)
72.4 (−17.7)
Table 11: Performance scores of the pretrained-only and instruction-finetuned Norwegian LMs on our text
summarization and machine translation tasks. The LMs are evaluated in (i) a zero-shot regime on NorSumm and
(ii) a 16-shot regime on Tatoeba. En=English; BM=Norwegian Bokmål; NN=Norwegian Nynorsk. Cold-colored
cells represent cases where an instruction-tuned version improves performance compared to the base LM, while
warm-colored cells indicate cases where it decreases. The best score is in bold, the second best is underlined.
Model
Text Summarization
Text Rewriting
NorSummarize-Instruct
NorRewrite-Instruct
chrF
BERTScore
chrF
BERTScore
NB-GPT-6B
23.8
57.0
19.5
56.1
GPT-SW3-6.7B
20.7
54.4
18.2
48.9
NorwAI-Mistral-7B
22.2
54.7
20.4
53.6
NorwAI-Llama2-7B
21.6
53.7
21.1
54.3
NorBLOOM-7B-warm
9.0
24.0
5.2
17.2
NorMistral-7B-scratch
8.5
24.0
7.2
20.0
Viking-7B
21.4
55.7
21.8
55.7
NorMistral-11B
27.2
61.4
25.7
71.0
Viking-13B
21.1
55.4
22.8
56.0
NorMistral-7B-warm
6.7
22.1
6.7
23.1
NorMistral-7B-warm-IT
41.4 (+34.7)
71.2 (+49.1)
41.2 (+34.5)
70.7 (+47.6)
Mistral-7B
5.7
15.9
6.0
18.8
Mistral-7B-IT
31.7 (+26.0)
70.3 (+54.4)
29.5 (+23.5)
70.0 (+51.2)
AI-Sweden/Llama-3-8B
21.2
54.4
21.9
55.0
AI-Sweden/Llama-3-8B-IT
32.3 (+11.1)
68.8 (+14.4)
30.3 (+8.4)
68.8 (+13.8)
Meta/Llama-3-8B
21.8
55.4
20.4
52.0
Meta/Llama-3-8B-IT
35.4 (+13.6)
71.9 (+16.5)
29.9 (+9.5)
68.5 (+16.5)
Mistral-Nemo-12B
18.7
47.3
18.1
49.9
Mistral-Nemo-12B-IT
39.9 (+21.2)
72.2 (+24.9)
38.9 (+20.8)
71.8 (+21.9)
Table 12: Performance scores of the pretrained-only and instruction-finetuned Norwegian LMs on our
instruction-style text summarization and rewriting tasks. The LMs are evaluated in a zero-shot regime on
NorSummarize-Instruct and NorRewrite-Instruct. Cold-colored cells represent cases where an instruction-tuned
version improves performance compared to the base LM, while warm-colored cells indicate cases where it decreases.
The best score is in bold, the second best is underlined.

--- Page 44 ---

F
Automatic Evaluation of Instruction-tuned LMs via LLM-as-a-judge
We evaluate the instruction-following abilities of the instruction-tuned LMs prompted for creative rewriting
and summarization. Such generative tasks are difficult to evaluate even with access to the gold standard
references. We use the LLM-as-a-judge approach, which involves a side-by-side comparison of LMs’
responses using an external judge LM. While judge models suffer from various biases (Chen et al., 2024;
Wang et al., 2024; Li et al., 2025), they correlate with human judgments better than traditional language
generation performance metrics (Sai et al., 2022; Zheng et al., 2023).
Expected win-rate scores
Given an instruction i, two outputs oA and oB from LMs A and B, and a
human reference oR, the judge model θ computes a score function:
sθ(i, oA, oB, oR) =





1,
if oA ≻θ oB
(θ prefers oA over oB)
0,
if oA ≺θ oB
1/2,
otherwise.
(1)
Using this, we can compute the expected win-rate of LM A over LM B as the expected value of the score
function over a distribution D of prompts and human references:
win_rateθ(A, B) = 1
2

1 + E
i,o ∼Dsθ (i, A(i), B(i), o) −E
i,o ∼Dsθ (i, B(i), A(i), o)

(2)
where the second symmetric term prevents position bias (Wang et al., 2024) from influencing the results.
Judge Model
Unlike Lyu et al. (2024), we use simple chain-of-thought prompting by asking the model
to first describe the qualities of each response before giving the final verdict – this is done to further
improve the evaluation accuracy (Wei et al., 2022). The judge is instructed to end its output by either
generating “A” (for preference of response A), “B” (for preference of response B), or “tie” (for cases
when both responses are either equally good or bad). We then parse the output and assign a score value
according to Equation (1). A response pair is skipped in case of an incorrectly formatted judgment, which
has not empirically occurred in our experiments.
F.1
Evaluating LLM-as-a-judge
A
TIE
B
A
35.42%
8.33%
12.50%
TIE
8.33%
4.17%
4.17%
B
10.42%
6.25%
10.42%
Table 13: Agreement between the judge model and humans. We compute the rates using prompt template from
Appendix F.2 without human references.
We analyze the agreement rate between the judge model and humans,
as well as self-
preference bias on an BM subset of Primeape,9
and explore language and position biases
on NorRewrite-Instruct and NorSummarize-Instruct.
The Primeape subset consists of 48
pairwise comparisons between meta-llama/Llama-3.3-70B-Instruct, google/gemma-2-27b-it,
mistralai/Mistral-Small-Instruct-2409, Claude 3.7 Sonnet, and GPT-4o (Hurst et al., 2024),
evaluated over 19 manually translated instructions from AlpacaEval (Dubois et al., 2023).
9An ongoing work on multilingual human preference prediction and explanation at the moment of writing a camera-
ready version of this paper; the data is provided by the dataset creators in response to our request. To be available at
github.com/Toloka/primeape.

--- Page 45 ---

NORREWRITE-INSTRUCT
NORSUMMARIZE-INSTRUCT
Model
NOB
NNO
SWE
DAN
ENG
NOB
NNO
SWE
DAN
ENG
Instructions
99.3%
0.7%
0.0%
0.0%
0.0%
96.4%
3.6%
0.0%
0.0%
0.0%
NorMistral-7B-warm-IT
98.6%
0.7%
0.0%
0.0%
0.7%
99.0%
0.5%
0.0%
0.0%
0.5%
Mistral-Nemo-12B-IT
87.5%
0.7%
0.0%
1.4%
9.7%
77.2%
0.0%
0.0%
0.5%
21.8%
Mistral-7B-IT
29.9%
0.0%
0.0%
6.9%
63.2%
35.5%
0.0%
0.0%
4.6%
59.4%
Meta/Llama-3-8B-IT
34.0%
0.0%
0.0%
0.0%
66.0%
49.7%
0.0%
0.0%
0.5%
49.2%
AI-Sweden/Llama3-8B-IT
0.0%
0.0%
100.0%
0.0%
0.0%
0.0%
0.0%
100.0%
0.0%
0.0%
Table 14: Language distribution in model responses on NorRewrite-Instruct and NorSummarize-Instruct. We
show the percentages of instructions and responses in Norwegian Bokmål, Nynorsk, Swedish, Danish and English.
NORREWRITE-INSTRUCT
NORSUMMARIZE-INSTRUCT
Model
NorMistral-7B-warm-IT
Mistral-Nemo-12B-IT
Mistral-7B-IT
Meta/Llama-3-8B-IT
AI-Sweden/Llama-3-8B-IT
Average
NorMistral-7B-warm-IT
Mistral-Nemo-12B-IT
Mistral-7B-IT
Meta/Llama-3-8B-IT
AI-Sweden/Llama-3-8B-IT
Average
NorMistral-7B-warm-IT
—
38.9
79.2
24.7
87.5
57.6%
—
33.8
59.4
18.1
83.2
48.6%
Mistral-Nemo-12B-IT
61.1
—
84.8
43.8
91.4
70.3%
66.2
—
77.3
38.3
91.1
68.2%
Mistral-7B-IT
20.8
15.2
—
4.9
60.7
25.4%
40.6
22.7
—
15.1
67.5
36.5%
Meta/Llama-3-8B-IT
75.3
56.2
95.1
—
92.7
79.8%
81.9
61.7
84.9
—
97.9
81.6%
AI-Sweden/Llama-3-8B-IT
12.5
8.6
39.3
7.3
—
16.9%
16.8
8.9
32.5
2.1
—
15.0%
Table 15: Instruction-finetuned LMs’ win-rates (%) when evaluating for the language bias. Cold-colored cells
indicate high win-rate, while warm-colored cells indicate low win-rate.
Agreement with Human Annotators
The agreement matrix is shown in Table 13. The results indicate
that the judge model agrees with human annotators in 50% of the cases, compared to a random agreement
rate of 33.3%. When ties are excluded, the agreement rate increases to 66.7%, with the corresponding
random baseline of 50%. The results and their interpretation can be affected by the limited sample size.
Self-preference Bias
We evaluate the self-preference bias (Panickssery et al., 2024) of
meta-llama/Llama-3.3-70B-Instruct to analyze how often the judge model favors its own outputs.
Among 32 pairwise comparisons, the judge’s verdicts result in 8 wins, 8 ties, and 16 losses. These results
suggest that the judge model exhibits relatively low self-preference bias and behaves fairly as an evaluator.
Language Bias
Since we evaluate the Norwegian capabilities of LMs responding to Norwegian instruc-
tions, only responses written in Norwegian should be the preferred ones. We use GlotLID (Kargaran
et al., 2023) to analyze the language distribution in the instructions as well as in the model responses
(see Table 14). Surprisingly, only NorMistral-7B-warm-IT consistently answers in Norwegian. Other
models often switch either to English or related Scandinavian languages. To better understand the effect
of requiring the responses to be in Norwegian, we modify our LLM-as-a-judge prompt template from
Appendix F.2 by explicitly instructing the judge to be invariant to the language of the responses. This
allows us to measure the Norwegian instruction following capabilities rather than the quality of producing

--- Page 46 ---

Norwegian. Table 15 shows that the LM ranking has changed, with Meta/Llama-3-8B-IT becoming the
most capable instruction-following LM. Conversely, NorMistral-7B-warm-IT has the expected win-rate
of 58% and 48%, which suggests that its high rate in the main experiment is more due to its capabilities to
consistently producing Norwegian.
Position Bias
Position bias is a common bias within the LLM-as-a-judge paradigm, where a judge
model prefers a response based on its position regardless of the content (Wang et al., 2024). While we
mitigate this bias by evaluating each response pair twice with switched positions as shown in Equation (2),
we observe a minor preference for the second position. Our judge prefers the first response 416× and the
second one 538× on NorRewrite-Instruct; on NorSummarize-Instruct, the bias is less apparent – with
1 100 and 1 156 position preferences. In case of Primeape, we observe self-agreement rates of 45.83%
with ties and 64.52% without ties. Overall, position bias appears to have an insignificant impact on
NorRewrite-Instruct and NorSummarize-Instruct, whereas its effect is more pronounced on Primeape.
F.2
Prompt Template for LLM-as-a-judge
We adapt the HREF prompt template provided in Lyu et al. (2024) by localizing it to Norwegian and
specifying that a Norwegian response should always be preferred over a non-Norwegian one.
System prompt:
You are a helpful assistant that helps us rate a Norwegian AI model's responses to instructions.
User prompt:
Decide which response from the Norwegian AI system following the instruction is better, considering the following questions:
1. Most importantly, the AI systems should always respond in Norwegian. If a response is not in Norwegian, then you should
consider it incorrect --- such a response should always be rated lower than any (even incorrect) response in Norwegian.
,→
2. Does the response precisely follow the instruction? For example, a response that includes unrelated information or does
not fulfill the task is not precisely following the instruction. Compare each response with the provided human response
to decide if a response faithfully follows the instruction, especially when the instruction asks for expected word count
or format.
,→
,→
,→
3. Is the response helpful? For example, if the instruction asks for a recipe for healthy food, and the response is a useful
recipe, then you can consider it helpful.
,→
4. Is the language of the response natural? For example, AI responses are often verbose or repetitive, which is not natural.
Compare with the provided human response to decide whether a response is natural.
,→
5. Is the response factual/accurate? AI responses often make up new information. For example, if the response claims that
Jens Stoltenberg is the current prime minister of Norway, then you should consider it inaccurate. Compare with the
provided human response to verify whether a response is factual and accurate, especially with numbers.
,→
,→
6. Based on your aesthetics, which one do you prefer? For example, you might prefer one poem over another poem.
Select the response A or B that you prefer, or select tie if the two responses are similarly good or bad. Note that the
responses can be truncated (don't consider that as a mistake).
,→
Here are three examples:
# Example 1:
## Instruction:
Omformulér følgende spørsmål: "Hva er hovedstaden i Frankrike?"
## Response A:
Hovedstaden i Frankrike er Paris.
## Response B:
Kan du fortelle meg navnet på byen som fungerer som hovedstaden i Frankrike?
## Human Response:
Hva heter Frankrikes hovedstad?
In this example, B paraphrases the question as asked by the instruction. In contrast, A does not follow instruction as it
answers the question instead. Human Response also paraphrases the question, just in a slightly different way. To sum up,
B is the best response because it follows the instruction.
,→
,→
## Which is best, A, B, or tie?
B
# Example 2:
## Instruction:
Bytt ut det første verbet med et synonym:
Jeg elsker å surfe

--- Page 47 ---

## Response A:
Jeg hater å surfe
## Response B:
I like to surf
## Human Response:
Jeg liker å surfe
Response A tries to follow the instruction as it changes the first verb of the sentence, but it uses an antonym instead of a
synonym. The response B might be correct, but it is written in English, not Norwegian, and non-Norwegian responses
should always be rated as worse. Human Response changes the first verb, "elsker" (love), into its synonym, "liker"
(like), as asked by the instruction. In conclusion, A is better than B because it is written in Norwegian.
,→
,→
,→
## Which is best, A, B, or tie?
A
# Example 3:
## Instruction:
Bytt ut det første verbet med et synonym:
Jeg elsker å surfe
## Response A:
Jeg hater å surfe
## Response B:
Jeg liker ikke å surfe
## Human Response:
Jeg liker å surfe
In this example, neither output is correct and the responses are very similar. Human Response changes the first verb into
its synonym, as asked by the instruction. To conclude, both A and B are equally incorrect, so the answer is tie.
,→
## Which is best, A, B, or tie?
tie
Now here is the real task, first describe the qualities of each response and then end your message by writing "## Which is
best, A, B, or tie?" and selecting among: A, B, or tie.
,→
# Task:
## Instruction:
{{instruction}}
## Response A:
{{output_1}}
## Response B:
{{output_2}}
## Human Response:
{{output_human}}

```
