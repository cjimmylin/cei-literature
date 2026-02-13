---
title: "2025-Lan-Fuxi A Benchmark for Evaluating Language - PDF Extract"
source_pdf: "2025-Lan-Fuxi A Benchmark for Evaluating Language.pdf"
pages: 25
extracted_at: "2026-02-13T09:15:44.861533"
---

# PDF Extract: 2025-Lan-Fuxi A Benchmark for Evaluating Language

**Source PDF:** 2025-Lan-Fuxi A Benchmark for Evaluating Language.pdf
**Total Pages:** 25

---

## Content

```
--- Page 1 ---

Fùxì: A Benchmark for Evaluating Language Models on Ancient Chinese
Text Understanding and Generation
Shangqing Zhao1, Yuhao Zhou1, Yupei Ren1,2,3,
Zhe Chen1, Chenghao Jia1, Fang Zhe1, Zhaogaung Long1, Shu Liu1,2,3, Man Lan1,2,3
1School of Computer Science and Technology, East China Normal University
2Lab of Artificial Intelligence for Education, East China Normal University
3Shanghai Institute of Artificial Intelligence for Education, East China Normal University
sqzhao@stu.ecnu.edu.cn, mlan@cs.ecnu.edu.cn
Abstract
Ancient Chinese text processing presents
unique challenges for large language models
(LLMs) due to its distinct linguistic features,
complex structural constraints, and rich cul-
tural context. While existing benchmarks have
primarily focused on evaluating comprehen-
sion through multiple-choice questions, there
remains a critical gap in assessing models’ gen-
erative capabilities in classical Chinese. We
introduce Fùxì, a comprehensive benchmark
that evaluates both understanding and genera-
tion capabilities across 21 diverse tasks. Our
benchmark distinguishes itself through three
key contributions: (1) balanced coverage of
both comprehension and generation tasks, in-
cluding novel tasks like poetry composition
and couplet completion, (2) specialized evalua-
tion metrics designed specifically for classical
Chinese text generation, combining rule-based
verification with fine-tuned LLM evaluators,
and (3) a systematic assessment framework that
considers both linguistic accuracy and cultural
authenticity. Through extensive evaluation of
state-of-the-art LLMs, we reveal significant per-
formance gaps between understanding and gen-
eration tasks, with models achieving promising
results in comprehension but struggling consid-
erably in generation tasks, particularly those
requiring deep cultural knowledge and adher-
ence to classical formats. Our findings high-
light the current limitations in ancient Chinese
text processing and provide insights for future
model development. The benchmark, evalua-
tion toolkit, and baseline results are publicly
available to facilitate research in this domain1.
1
Introduction
Ancient Chinese, as a written form of the Chinese
language used for more than two millennia in East
Asia, has profoundly shaped the cultural and in-
tellectual development of the region (Holcombe,
2006; Zhou, 2009). With an estimated corpus of
1https://github.com/cubenlp/FuxiBench
下列诗句中,描绘春日景象的是( )
A.  春风又绿江南岸,明月何时照我还?
B.  春眠不觉晓,处处闻啼鸟。
C.  春风得意马蹄疾,一日看尽长安花。
D.  春水初生,春林初盛,春风十里,不如你。
描绘春日景象的是：B
我们来玩飞花令吧，主题为“月”，每句
诗词中必须包含“月”字，且每句只能被
使用一次。我先来：
鸡声茅店月人迹板桥霜
好的，我来接一句：明月几
时有把酒问青天该你了！
但愿人长久千里共婵娟
这句太经典了！我接：举杯
邀明月对影成三人该你了！
二十四桥明月夜玉人何处教吹箫
好句！我接：一片冰心在玉
壶，夜深清露明月光。
按照提供的词牌名和题目写一首词。要求严格遵
守词牌的格律要求。
词牌: 望江南题目: 青墩初夏词
好的，按照词牌“望江南”的格律要求以及题目
“青墩初夏词”，我为您创作了一首词。此词遵循
词牌格律，七言四句：
望江南·青墩初夏词
青墩绿水润晴川，柳垂翠影共闲愁。
初夏风光新一遍，芳草悠然绕画楼。
这首词写出初夏青墩的自然景色以及心境的描绘，
符合“望江南”词牌的格律。
Figure 1: Interactions with GPT-4 about Ancient Chi-
nese related topics.
400 million words spanning 3 million texts, this
vast literary heritage encompasses literature, phi-
losophy, history, and various other domains, with
approximately half of these texts holding signifi-
cant academic and cultural value (Li, 2002; Zhou
et al., 2023; Lao Bin and Sizhe, 2024).
However, the increasing gap between classical
and modern Chinese poses significant challenges
for contemporary readers and researchers. This
linguistic evolution necessitates advanced Natural
Language Processing (NLP) technologies to effec-
tively process, understand, and analyze classical
Chinese texts. While pre-trained language models
like BERT (Devlin et al., 2019) and GPT (Radford
et al., 2018) have demonstrated remarkable capa-
bilities in modern Chinese NLP tasks, their applica-
tion to classical Chinese presents unique challenges
due to substantial differences in grammar, vocab-
ulary, and writing conventions. As illustrated in
Figure 1, even GPT-4 (OpenAI, 2023), currently
one of the most advanced LLMs, struggles with
traditional Chinese poetry games. Although these
models can sometimes correctly answer multiple-
choice questions by selecting from given options,
their performance in generating Ancient Chinese
related text still needs improvement, highlighting
the complexity of classical Chinese language un-
1
arXiv:2503.15837v1  [cs.CL]  20 Mar 2025

--- Page 2 ---

derstanding and generation.
While existing benchmarks such as C-CLUE (Ji
et al., 2021) and WYWEB (Zhou et al., 2023) have
made important contributions in evaluating model
performance on specific tasks, and more recent
works like ACLUE (Zhang and Li, 2023) and AC-
EVAL (Wei et al., 2024b) have provided compre-
hensive evaluation frameworks, there remains a
critical gap in assessing models’ generative capa-
bilities in classical Chinese. Most benchmarks rely
heavily on multiple-choice questions, which are
useful for assessing comprehension but do not ef-
fectively measure a model’s ability to generate co-
herent and contextually appropriate classical Chi-
nese text.
To address these limitations, we introduce Fùxì
(负
), a novel benchmark designed to comprehen-
sively evaluate both the understanding and gener-
ation capabilities of language models in classical
Chinese. Fùxì distinguishes itself through: 1) A
balanced focus on both comprehension and gener-
ation tasks, with 21 carefully designed task types
spanning various aspects of classical Chinese; 2)
Novel evaluation metrics specifically developed for
assessing the quality of generated classical Chinese
text; 3) A comprehensive evaluation framework
that considers both linguistic accuracy and cultural
authenticity.
Our contributions are summarized as follows:
• We present Fùxì, the first benchmark to com-
prehensively evaluate both understanding and
generation capabilities in classical Chinese,
featuring 21 diverse task types and novel eval-
uation metrics
• We introduce innovative task types specifi-
cally designed to assess unique aspects of
classical Chinese, including poetry genera-
tion, couplet completion, and style transfer
between classical and modern Chinese
• We provide extensive baseline results for state-
of-the-art language models on Fùxì, revealing
critical insights about their strengths and limi-
tations in handling classical Chinese
• We release our benchmark, evaluation toolkit,
and a fine-tuned model specialized for classi-
cal Chinese text evaluation, facilitating further
research in this domain
Through Fùxì, we aim to advance the develop-
ment of more capable language models for process-
ing classical Chinese texts, ultimately contributing
to the preservation and accessibility of this rich
cultural heritage.
2
Related Work
2.1
Chinese Benchmarks for LMs
Recent years have witnessed significant progress in
developing comprehensive benchmarks to evaluate
Chinese language models. Early benchmarks such
as MMCU (Zeng, 2023) and C-Eval (Huang et al.,
2023) focused on assessing models’ performance
across diverse disciplines through multiple-choice
questions derived from standardized tests. These
were followed by more sophisticated frameworks
like CMMLU (Li et al., 2024) and SuperCLUE (Xu
et al., 2023), which incorporated both closed- and
open-ended tasks to evaluate reasoning capabilities
and linguistic understanding.
Recognizing the importance of text generation,
benchmarks like CG-Eval (Zeng et al., 2024) and
CLEVA (Li et al., 2023) introduced tasks specifi-
cally designed to evaluate generative capabilities,
including short answer generation, computational
problem-solving, and creative writing tasks. Open-
Compass (Contributors, 2023), integrating over 100
datasets, further expanded the scope of generation
evaluation. While these benchmarks have signif-
icantly advanced Chinese language model evalu-
ation, they primarily focus on modern Chinese,
leaving the unique challenges of classical Chinese
largely unexplored.
2.2
Ancient Chinese Benchmarks
Ancient Chinese, with its rich linguistic and cul-
tural heritage, necessitates specialized resources
and evaluation tools to assess its historical, liter-
ary, and syntactic complexities. Current evaluation
benchmarks can be categorized into three main
streams: understanding-focused, comprehensive
evaluation frameworks, and generation-oriented as-
sessments.
For specific understanding tasks, several bench-
marks have emerged: GuNER (Su et al., 2023)
for named entity recognition, GuwenEE2 for event
extraction, and CCLUE (Ji et al., 2021) for gen-
eral language understanding. Complementary re-
sources such as CCP-KG (Yutong et al., 2020) and
CQY (Shao et al., 2021) address specialized aspects
such as classical poetry sentiment analysis. For
cross-temporal understanding, translation-focused
2https://github.com/Lyn4ever29/GuwenEE
2

--- Page 3 ---

datasets such as Erya (Guo et al., 2023) and Eva-
Han (Wang et al., 2023) specifically address the
syntactic and semantic relationships between an-
cient and modern Chinese.
Recent developments have introduced more com-
prehensive evaluation frameworks. ACHNLU (Hu
et al., 2024) evaluated 12 mainstream LLMs’ nat-
ural language understanding capabilities, while
ACLUE (Zhang and Li, 2023) presented a frame-
work encompassing 15 tasks across phonetic, lexi-
cal, syntactic, semantic, inference and knowledge-
based dimensions. Based on these, AC-EVAL in-
troduced a three-tier framework to assess general
historical knowledge, short text understanding, and
long text comprehension through 13 distinct tasks.
However, these frameworks predominantly rely on
multiple-choice questions, which, while facilitat-
ing standardized evaluation, may not fully capture
the models’ tendency toward hallucination or their
generative capabilities.
In terms of classical text generation, systems
like Jiuge (Li et al., 2021) and Yu Sheng (Ma et al.,
2023) have demonstrated the potential for the gener-
ation of ancient Chinese poetry, although their eval-
uation is based primarily on human evaluation. A
notable advancement is CharPoet (Yu et al., 2024),
which focuses on improving format correctness
through token-free generation pruning of LLMs.
Although existing benchmarks have made signif-
icant strides in evaluating ancient Chinese language
understanding, they either lack comprehensive cov-
erage or rely heavily on multiple-choice assess-
ments. Notably, the evaluation of LLMs’ capability
to generate authentic classical Chinese content re-
mains largely unexplored and requires systematic
investigation.
2.3
Evaluation Metrics for LLMs
The evaluation of language models, particularly for
classical Chinese text generation, presents unique
challenges that require specialized metrics and
approaches. Traditional metrics like BLEU (Pa-
pineni et al., 2002), ROUGE (Lin, 2004), and
METEOR (Banerjee and Lavie, 2005) have been
widely used for assessing text generation quality.
However, these metrics often fall short in captur-
ing the nuances of classical Chinese, especially
its unique structural requirements, linguistic pat-
terns, and rich cultural elements that are essential
for authentic classical text generation.
Human evaluation represents another approach,
where human judges assess responses generated
by different LLMs based on criteria such as accu-
racy, fluency, and cultural authenticity (Wei et al.,
2024a). While human evaluation provides nuanced
assessment, it is prohibitively slow and costly, mak-
ing it impractical for large-scale evaluations and
rapid development cycles. To address these limita-
tions, researchers have proposed using commercial
LLMs as surrogate evaluators, known as LLM-as-a-
judge (Wei et al., 2024a), where models like GPT-
4 and GPT-3.5-turbo serve as automated judges.
However, these LLM judges often exhibit biases
and inconsistencies in their evaluations, even when
various bias-mitigation techniques are applied. In
this work, we adopt a hybrid approach combining
rule-based metrics with aligned LLM evaluators.
For tasks with well-defined structural constraints,
we implement rule-based verification to assess ad-
herence to classical Chinese literary forms. For
more subjective aspects requiring deeper linguistic
and cultural understanding, we employ fine-tuned
LLMs specifically aligned to evaluate classical Chi-
nese text generation, mitigating the biases present
in general-purpose commercial LLMs while main-
taining evaluation efficiency.
3
Fùxì Overview
3.1
Design Principles
Task Diversity Previous work has predominantly
focused on assessing comprehension abilities
through multiple-choice questions. However, text
generation is equally critical for ancient Chinese
language processing. In the Fùxì benchmark, we
emphasize the evaluation of models’ generative ca-
pabilities by introducing a variety of generation
tasks. These include tasks such as classical-to-
modern Chinese translation, poetry appreciation,
and completing missing lines in poetic composi-
tions.
Data Quality Our dataset is derived from high-
quality internet sources, with manual curation to
consolidate duplicate content and ensure data con-
sistency. For deterministic tasks, such as predicting
the subsequent line of a poem, we automated the
data construction process using custom scripts to
maintain reliability. Additionally, some tasks are
sourced from pre-annotated datasets, further ensur-
ing the quality and integrity of the task data.
Task Evaluability Unlike prior benchmarks that
primarily rely on multiple-choice formats for ease
of scoring, Fùxì includes a significant number
of tasks that require text generation as answers.
3

--- Page 4 ---

Task
Description
Type
Eval Metric
Ancient Chinese RC
Multiple choice question on ancient Chinese text reading comprehension
NLU
Acc
Idiom RC
Multiple choice question on idiom reading comprehension
NLU
Acc
TCM Syndrome RC
Multiple choice question on TCM syndrome differentiation
NLU
Acc
Loan Character QA
Loan character identification question answering
NLG
Acc
Allegorical Saying QA
Allegorical saying question answering, to complete the second half.
NLG
Acc
Book Author
Given a book title, answer the author
NLG
Acc
Book Dynasty
Given a book title, answer the dynasty
NLG
Acc
Book Collection Classification
Classify book titles into 10 collections
NLG
Acc
Poetry Generation
Poetry creation according to topic words
NLG
Acc
Poetry Line Source Tracing
Identify the source of a poem line
NLG
Acc
Famous Quote Source Tracing
Identify the source of a classical Chinese quote
NLG
Acc
Idiom Source Tracing
Name the source book or essay of an idiom.
NLG
Acc
Inverse Poetry Translation
Decipher the original poem from translated modern Chinese version.
NLG
Acc
Poetry Translation
Translate a poem into modern Chinese
NLG
BLEU
Ancient Chinese Translation
Translate ancient Chinese text into modern Chinese(extracted from the erya dataset)
NLG
BLEU
Poetry Appreciation
Analysis of imagery, style, sentiment in classical Chinese poetry
NLG
BLEU
Idiom Explanation
Idiom explanation
NLG
BLEU
TCM QA
Answer questions given related TCM text.
NLG
BLEU
Prescription Explanation
Prescription details for TCM
NLG
BLEU
Couplet Generation
Generate the second line based on the first line.
NLG
Acc
Ci Generation
Write a poem following a specific ci pattern with tonal rules.
NLG
Acc
Table 1: Overview of the Fuxi benchmark, including task description and evaluation metrics.
This introduces unique challenges in evaluation.
For tasks without strictly correct answers, such as
classical-to-modern Chinese translation and poetry
appreciation, we employ widely-used text genera-
tion evaluation metrics like BLEU (Papineni et al.,
2002). For tasks with definitive answers, assessing
the correctness of model-generated text presents a
significant challenge. While human evaluation is an
option, it is resource-intensive and subject to inter-
annotator variability. Additionally, there is a lack
of established automated metrics for such tasks.
To enable consistent and automated evaluation, we
developed a prompt-based framework and manu-
ally annotated 1,000 samples, which were used to
fine-tune a Qwen model (Bai et al., 2023). This
fine-tuned model serves as an intelligent evaluation
agent, achieving evaluation accuracy comparable
to human judgments with minimal error margin.
3.2
Benchmark Construction
Multiple-Choice Reading Comprehension The
first category comprises multiple-choice questions
designed to evaluate comprehension of classical
Chinese texts. We incorporate reading comprehen-
sion tasks for Chinese idioms and passages from
WYWEB (Zhou et al., 2023). Additionally, we
include Traditional Chinese Medicine (TCM) as
a significant component of ancient Chinese cul-
tural heritage, primarily documented in classical
Chinese. The TCM syndrome differentiation task
(TCMSRC) challenges LLMs to select the most
appropriate diagnosis from four TCM syndrome
types based on patient case descriptions in classical
Chinese.
Open-ended Question Answering
This cate-
gory evaluates LLMs’ deeper understanding and
knowledge capabilities by requiring them to gen-
erate answers rather than selecting from options,
thereby revealing potential hallucinations.
The
tasks include loan character identification, comple-
tion of xiehouyu (traditional Chinese riddles), and
TCM-related questions. Leveraging the daizhige
database, we constructed tasks requiring LLMs
to identify authors and historical dynasties based
on book titles, and to categorize books into ten
collections based on title comprehension. Addi-
tionally, we developed source attribution tasks for
classical Chinese poetry and prose. LLMs must
identify the origins of randomly selected poetry
verses and famous quotations from ancient texts,
including the sources of traditional Chinese idioms.
A particularly challenging task is the Inverse Poetry
Translation where LLMs must reconstruct classical
poems from their modern Chinese translations. It
is a task that humans excel at but often challenges
AI models.
Comprehension-Based Generation
This cate-
gory features generation tasks where output quality
is evaluated using BLEU scores to measure similar-
ity with reference answers. Tasks include: 1) Trans-
lation of classical poetry and prose into modern
Chinese. 2) Comprehensive poetry appreciation. 3)
Idiom interpretation. 4) Detailed interpretation of
4

--- Page 5 ---

traditional medical prescriptions.
Pattern-constrained Generation The final cate-
gory assesses LLMs’ ability to generate text follow-
ing classical Chinese literary forms and regulations,
which have influenced various East Asian literary
traditions, including Japanese Haiku. We imple-
ment two specific tasks:
• Couplet Generation: Using a comprehensive
couplet dataset, LLMs must generate the sec-
ond sentence given the first sentence, with
evaluation based on matching character count.
• Ci Poetry Generation: Based on an extensive
collection of cipai (词牌, formal patterns) and
their corresponding rules, LLMs must com-
pose ci poetry according to specified themes
and patterns, with scores determined by adher-
ence to formal requirements.
3.3
Evaluation Metrics
We employ different evaluation strategies for vari-
ous task types in Fùxì, considering both the nature
of the tasks and the practical challenges in assess-
ment.
Multiple-Choice Reading Comprehension.
For
multiple-choice reading comprehension tasks, we
use accuracy as the evaluation metric. The answer
is extracted from LLM-generated responses using
regular expressions. A response is considered in-
correct if either the answer extraction fails or the
extracted answer differs from the ground truth.
Open-ended Question Answering.
While ac-
curacy remains the primary metric for open-ended
QA tasks, the diverse nature of LLM-generated re-
sponses poses challenges for automated evaluation.
Manual assessment, though accurate, is resource-
intensive and difficult to scale. To address this,
we develop an LLM-based evaluator following the
principles outlined in the LangChain evaluation
framework. We first create a training dataset of
2,000 human-annotated examples, where each ex-
ample consists of evaluation criteria, reference an-
swers, and predicted answers, along with binary
correctness labels. This dataset is then used to
fine-tune Qwen2-7B-Instruct, resulting in our LLM
Evaluator. To validate the reliability of our LLM
Evaluator, we conduct a correlation study between
human and automated assessments. We randomly
sample 1,000 examples from the evaluated results
and calculate the correlation coefficient between
human judgments and the LLM Evaluator’s deci-
sions. The strong correlation supports the validity
Task
# Questions
# Avg. QL
# Avg. AL
ACRC
300
814.28
1.00
IRC
1000
159.54
1.00
TCMSRC
1098
543.93
1.00
TCMQA
740
385.06
47.28
LCQA
500
37.95
16.88
ASQA
553
19.89
5.26
BA
384
17.37
2.64
BD
372
22.26
1.12
BCC
532
52.65
2.00
PG
300
27.48
89.23
PLST
400
25.22
11.46
FQST
200
29.41
10.06
IST
962
14.17
40.61
IPT
300
252.08
152.99
PT
300
145.79
213.91
ACT
1000
36.33
35.97
PA
109
112.70
1312.32
TCMNER
300
485.71
109.46
IE
1236
14.10
20.43
PE
404
19.74
70.11
CG
500
27.91
13.91
CiG
300
49.81
79.35
Table 2: Statistics of Question Length and Answer
Length for all tasks in Fuxi Benchmark.
of our automated evaluation approach. Details are
described in Appendix B.
Text Generation.
For generation tasks, we em-
ploy two distinct evaluation strategies based on
the task characteristics: 1) For translation-oriented
tasks where the target is modern Chinese, we uti-
lize the BLEU metric (Papineni et al., 2002), which
effectively captures the semantic and structural sim-
ilarities between generated and reference transla-
tions. 2) For pattern-constrained generation tasks
such as classical poetry and couplets, we focus on
evaluating adherence to formal rules (格律). Our
evaluation metrics specifically check for correct
tonal patterns, rhythmic structures, and parallel
construction requirements. While artistic quality
is an important aspect of classical Chinese poetry,
we prioritize format correctness as the fundamental
capability, leaving aesthetic evaluation for future
work. This approach allows us to establish a clear
baseline for assessing models’ ability to generate
formally correct classical Chinese text.
5

--- Page 6 ---

Model
ACRC
IRC
TCMSRC
ASQA
LCQA
BA
BD
BCC
PG
PLST
FQST
IST
IPT
PT
ACT
PA
IE
TCMQA
PE
gpt-4o-mini
50.67
77.60
79.23
6.69
10.00
1.04
16.67
78.20
2.00
3.75
16.50
1.25
3.67
5.61
19.77
5.87
1.78
31.93
55.32
gpt-4o
66.33
86.00
84.79
28.57
26.80
10.16
38.98
91.73
41.33
24.00
46.00
12.89
36.33
1.80
19.86
4.88
3.02
38.12
66.07
qwen-max
86.00
85.90
86.97
52.26
42.40
20.31
40.32
96.61
45.00
58.00
75.00
41.27
73.33
1.64
22.85
6.43
1.85
22.81
53.43
glm-4-plus
82.33
87.50
83.52
51.36
37.20
29.69
52.96
97.37
76.67
52.25
82.00
49.17
66.00
3.88
17.24
8.53
2.03
23.41
38.82
internlm25-7b
48.67
77.20
67.85
3.62
4.20
0.00
1.88
68.61
3.00
15.75
31.50
8.52
25.33
2.07
14.08
7.49
85.53
4.32
40.38
internlm25-20b
59.33
80.70
73.95
26.40
31.80
3.39
21.51
93.23
40.67
33.25
70.00
63.20
36.00
1.81
12.51
7.53
56.86
3.78
39.19
glm4-9b
63.67
77.80
76.05
2.17
5.60
1.30
14.78
73.12
2.67
8.00
28.50
3.64
25.00
9.38
18.06
7.01
1.92
26.36
56.79
llama31-8b
30.00
61.70
56.19
0.36
2.20
0.52
9.14
59.21
0.00
0.25
3.00
0.42
1.00
4.12
9.88
2.53
2.06
39.79
1.09
llama31-8b-chinese
37.00
67.50
56.01
0.00
0.60
0.00
2.69
72.37
0.33
0.25
2.50
0.10
1.00
7.32
13.72
6.21
1.07
25.29
55.33
qwen2-0.5b
34.33
46.20
28.05
0.18
0.80
0.26
3.76
12.78
1.00
1.25
2.50
0.83
13.67
4.51
14.51
2.37
2.71
31.14
1.29
Xunzi-qwen2-7b
45.00
62.30
54.37
12.48
2.20
0.00
5.65
19.55
28.00
5.75
26.00
23.91
11.67
1.06
1.15
3.93
20.38
2.55
22.10
qwen2-7b
77.00
79.80
82.88
5.24
3.40
1.04
8.87
74.44
0.00
13.00
22.00
2.18
21.67
1.63
15.97
6.75
1.36
27.46
47.84
qwen2.5-1.5b
46.67
71.70
71.13
2.17
5.40
2.08
17.20
59.77
24.67
11.00
14.50
8.21
30.33
6.91
17.47
2.66
2.61
43.64
1.10
qwen2.5-3b
57.67
77.60
76.23
18.44
12.80
3.39
18.01
83.83
28.00
18.75
41.00
8.94
41.67
7.78
20.47
6.05
1.45
27.84
61.68
qwen2.5-7b
71.33
83.20
83.33
22.78
18.60
3.39
20.97
92.67
29.67
28.00
44.50
18.81
41.67
7.64
19.15
6.72
1.74
23.66
55.40
qwen2.5-14b
78.67
82.50
83.15
34.72
29.60
5.47
38.44
92.67
62.67
38.00
54.00
30.25
57.33
9.28
18.21
6.67
2.35
24.95
62.65
qwen2.5-72b
83.00
85.80
86.89
35.44
31.60
14.32
43.28
93.80
48.00
46.00
61.00
42.72
77.67
3.46
24.99
7.31
2.46
22.36
41.40
Table 3: Evaluation results of selected models on Fuxi benchmark under zero-shot settings.
Model
Zero-shot Setting
ICL Setting (5-shot)
CG
CiG
CG
CiG
gpt-4o-mini
79.00
2.33
71.80
10.00
gpt-4o
89.60
55.33
83.40
53.33
qwen-max
96.60
25.67
93.80
39.67
glm-4-plus
19.20
41.67
44.00
54.33
internlm25-7b
32.40
17.67
59.80
18.67
internlm25-20b
63.40
3.67
44.40
6.67
glm4-9b
69.20
3.67
59.80
7.67
llama31-8b
8.60
0.33
0.20
0.00
llama31-8b-chinese
44.80
0.67
8.40
1.00
qwen2-0.5b
32.60
0.00
8.00
0.33
Xunzi-qwen2-7b
0.00
0.00
0.00
0.00
qwen2-7b
62.6
7.67
36.20
10.67
qwen2.5-1.5b
62.60
20.00
65.80
36.67
qwen2.5-3b
56.60
31.00
12.80
13.00
qwen2.5-7b
28.00
42.33
71.00
44.67
qwen2.5-14b
37.60
34.67
44.00
24.33
qwen2.5-72b
65.40
60.67
85.80
53.67
Table 4: Evaluation results on Chinese Generation (CG)
and Chinese-in-Graph (CiG) tasks under 5-shot settings.
4
Experiments
4.1
Setup
The Fùxì Benchmark comprehensively evaluates
both knowledge understanding and generation ca-
pabilities of large language models (LLMs) in the
domain of classical Chinese. For our primary eval-
uation protocol, we employed a zero-shot setting,
where models were provided with task instructions
and inputs without exemplars, requiring them to
generate answers based solely on their pre-trained
knowledge. All task instructions are demonstrated
in Appendix D. Additionally, considering the ex-
perimental paradigms used in related studies (Wei
et al., 2024b), we also conducted evaluations using
a few-shot in-context learning approach (Brown
et al., 2020).
4.2
Evaluated Models
We evaluated a variety of state-of-the-art models on
the Fùxì Benchmark, including both open-source
and commercial closed-source models. For open-
source models, the evaluation included the Qwen
series (Bai et al., 2023), GLM-4-9b (GLM et al.,
2024), LLaMA series (Grattafiori et al., 2024), In-
ternLM (Cai et al., 2024), and several fine-tuned
variants such as Xunzi 3 and Chinese-LLaMA (Cui
et al., 2023; LlamaFamily, 2024).
For closed-source models, we assessed GPT-
4o/GPT-4o-min (OpenAI, 2023), GLM-4-Plus and
Qwen-Max. These models were selected to rep-
resent a diverse range of design philosophies and
technical capabilities, ensuring a comprehensive
evaluation across the Fùxì Benchmark.
5
Results and Analysis
5.1
Overall Performance
Our comprehensive evaluation across 21 diverse
tasks reveals three key insights about LLM capabil-
ities in processing ancient Chinese:
Comprehension-Generation Gap According to
Table 3 and Table 5, all models perform signifi-
cantly better on multiple-choice tasks (ACRC, IRC,
TCMSRC) than generation tasks. For example, the
average accuracy score on RC tasks is 42.51 higher
than that on QA tasks (ASQA to IPT in Table 3).
As for TG tasks (PT to PE in Table 3) which are
evaluated with BLEU score, their lower scores are
reasonable given the highly subjective nature of
these tasks. However, the wide score range among
models also illustrates the substantial performance
gap across different architectures.
3https://github.com/Xunzi-LLM-of-Chinese-classics/
XunziALLM
6

--- Page 7 ---

Figure 2: Model performance scaling with model size
on four task categories.
Performance Scaling Despite the gap between
comprehension and generation, performance on all
tasks shows strong correlation with model size, par-
ticularly for knowledge-intensive tasks like book-
related tasks (BA, BD, BCC) and poetry-related
tasks (IPT, PLST). The largest model (72B param-
eters) outperform its 1.5B counterparts by an av-
erage of 22.06% on RC tasks and 31.85% on QA
tasks, suggesting specialized cultural knowledge
benefits significantly from increased parameteri-
zation. Performances of the closed-source API
models also indicate the scaling effect of model
size, with flagship models (GPT-4o, Qwen-Max,
GLM-4-Plus) significantly outperforming smaller
models (GPT-4o-mini).
Format Constraint Challenge Models struggle
with format-constrained generation, especially
LLaMA-31-8b because it is not optimized for
Chinese. The extended version (LLaMA-31-8b-
Chinese, with optimized Chinese vocabulary and
incremental pre-training) shows clear performance
improvements across all benchmark tasks. Xunzi-
Qwen2-7b, though specialized for ancient Chinese,
appears to have lost some instruction-following ca-
pability during fine-tuning, leading to an absolute
performance drop. Ci Poetry Generation requires
models to utilize their knowledge of cipai (词牌,
formal patterns) and generate poetry following spe-
cific structures, which proves more difficult than
couplet generation. The evaluation results confirm
that Couplet Generation is relatively easier, with
model average scores 29.46% higher than on Ci
Generation. GPT-4o and Qwen2.5-72b are the only
two models achieving non-trivial performance on
Ci Generation under zero-shot settings, indicating
their superior adherence to classical Chinese struc-
tural constraints. However, most models score be-
low 10% on this task. This suggests that adherence
to classical Chinese structural constraints presents
a unique challenge for current LLMs.
5.2
Task-Centric Analysis
Comprehension Tasks As shown in Table 3 and
Figure 2, comprehension tasks demonstrate clear
scaling advantages, with larger models consistently
outperforming smaller variants. The Ancient Chi-
nese RC task (ACRC) shows particular sensitiv-
ity to model architecture, with Chinese-originated
models (GLM and Qwen series) achieving better
performance than LLaMA series, even for API
models where Qwen-Max and GLM-4-Plus show a
10%+ gap compared to GPT-4o. The commercial
models demonstrate superior performance on com-
prehension tasks, potentially indicating advantages
from their larger parameter sizes.
Generation Tasks
For open-ended generation tasks, larger models
clearly perform better. Many of these tasks (in-
volving classical books, poetry, allegorical sayings,
loan characters) are knowledge-intensive, particu-
larly source tracing tasks, requiring more parame-
ters to memorize and understand this specialized
knowledge. Error analysis reveals that smaller mod-
els are more prone to hallucination phenomena.
For text generation tasks, there is no clear scaling
pattern in Figure 2. This is because these tasks can
be divided into translation tasks (PT, ACT) and ap-
preciation/explanation tasks (PA, IE, PE, TCMQA),
all using BLEU as the evaluation metric with ref-
erence answers that may not be optimal. Never-
theless, models with more parameters still perform
better on ancient Chinese short text translation. No-
tably, InternLM and Xunzi-Qwen2-7b perform ex-
ceptionally well on the Idiom Explanation (IE) task,
possibly because their pre-training data included
more relevant texts.
For pattern-constrained generation tasks, the re-
sults are evaluated using rule-based metrics since
LLM evaluators cannot precisely assess format
requirements, resulting in generally lower scores.
Xunzi-Qwen2-7b scored 0 because its outputs con-
tained many irrelevant descriptions or failed to
stop generating. Qwen2-0.5 similarly scored low
because it couldn’t maintain the required pattern
rules. LLaMA-31-8b exhibited language mixing
issues, and while LLaMA-31-8b-Chinese greatly
improved this aspect, it still struggled with pattern
adherence.
7

--- Page 8 ---

Model
RC
QA
TG
PG
gpt-4o-mini
69.17
13.98
20.05
40.67
gpt-4o
79.04
35.68
22.29
72.47
qwen-max
86.29
54.45
18.17
61.14
glm-4-plus
84.45
59.47
15.65
30.44
internlm25-7b
64.57
16.24
25.65
25.04
internlm25-20b
71.33
41.95
20.28
33.54
glm4-9b
72.51
16.48
19.92
36.44
llama31-8b
49.30
7.61
9.91
4.47
llama31-8b-chinese
53.50
7.98
18.16
22.74
qwen2-0.5b
36.19
3.70
9.42
16.30
Xunzi-qwen2-7b
53.89
13.52
11.50
0.00
qwen2-7b
79.89
15.18
16.84
35.14
qwen2.5-1.5b
63.17
17.53
12.40
41.30
qwen2.5-3b
70.50
27.48
20.88
43.80
qwen2.5-7b
79.29
32.11
19.05
35.17
qwen2.5-14b
81.44
44.32
20.69
36.14
qwen2.5-72b
85.23
49.38
17.00
63.04
Table 5: Average performance of models across task cat-
egories: Multiple-choice Reading Comprehension (RC),
Open-ended Question Answering (QA), Text Genera-
tion(TG) and Pattern-constrained Generation(PG).
Metric
w/ PG
w/o PG
Accuracy
0.898
0.930
Cohen’s κ
0.764
0.830
Precision
0.833
0.815
Recall
0.843
0.951
F1 Score
0.838
0.878
Pearson Correlation
0.764
0.835
Table 6: Overall Performance Metrics. w/o PG: without
Poetry Generation (PG) task.
5.3
LLM Evaluator Validation
To ensure reliable evaluation of open-ended gener-
ation tasks, we validated our LLM-based evaluator
through a comprehensive human evaluation study.
We randomly sampled 1,000 responses from GPT-
4o’s outputs across different task categories, with
sampling proportions matching the distribution of
tasks in the benchmark. Three expert annotators
independently judged each response, reaching con-
sensus on each sample to establish gold standard an-
swers. As shown in Figure 5, our evaluator demon-
strates strong alignment with human judgments,
achieving overall accuracy of 89.8% and substan-
tial agreement (Cohen’s κ = 0.764). The evaluator
performs exceptionally well on factual tasks like
Book Dynasty identification (BD, κ = 0.950) and
Poetry Line Source Tracing (PLST, κ = 0.905). It
ASQA
BA
BCC
BD
IST
LCQA
PG
IPT
PLST
FQST
0
0.2
0.4
0.6
0.8
1
Score
Accuracy
Cohen’s κ
Figure 3: Comparison of Accuracy and Cohen’s Kappa
across different labels. Overall performance: Accuracy
= 0.898, Cohen’s Kappa = 0.764.
shows slightly lower agreement on subjective tasks
like Allegorical Saying QA (ASQA, κ = 0.567),
mirroring patterns in human inter-annotator agree-
ment. As shown in Table 5, excluding the Poetry
Generation (PG) task improves overall agreement
to κ = 0.830. This exclusion was necessary because
our aligned LLM evaluator incorrectly penalized
valid responses providing three candidate poetic
forms (体裁), confirming that our automated eval-
uation approach provides reliable assessment for
most tasks. The strong correlation between human
and automated assessments (Pearson’s r = 0.835 ex-
cluding PG) validates our evaluation methodology,
enabling consistent comparison across models and
tasks while minimizing resource-intensive manual
evaluation.
6
Conclusion
This paper introduces Fùxì, a comprehensive bench-
mark for evaluating large language models’ capa-
bilities in ancient Chinese text understanding and
generation. Through extensive evaluation of cur-
rent state-of-the-art models across 21 diverse tasks,
our study reveals several important findings. First,
while modern LLMs demonstrate promising per-
formance in basic comprehension tasks, they still
face significant challenges in tasks requiring deep
cultural understanding and specialized knowledge.
Second, the generation of authentic ancient Chi-
nese text remains a particularly challenging area,
with models struggling to maintain consistent clas-
sical style and adhere to traditional formats. Third,
model size and architecture choices significantly
impact performance, with larger models and those
specifically trained on Chinese corpora showing ad-
vantages in certain tasks. Beyond these empirical
8

--- Page 9 ---

findings, Fùxì contributes to the field by provid-
ing: (1) a standardized evaluation framework that
encompasses both understanding and generation
capabilities, (2) novel evaluation metrics address-
ing classical Chinese’s unique structural require-
ments, validated through human-LLM evaluator
alignment, and (3) baseline results that can guide
future research and development in this area. The
insights gained from this benchmark can inform
both the development of more effective models for
processing ancient Chinese texts and the broader
field of cultural heritage preservation through AI.
7
Limitations
Evaluation Metrics
Although we introduce novel metrics for gener-
ation tasks, the automatic evaluation of generated
ancient Chinese text remains challenging. Current
metrics may not fully capture the nuances of clas-
sical Chinese style and literary conventions. Fu-
ture work could explore more sophisticated evalua-
tion approaches that better align with human expert
judgments.
Task Coverage
While our benchmark covers a broad range of
tasks, certain aspects of ancient Chinese language
processing remain underexplored. For instance,
the benchmark could be expanded to include more
specialized genres of classical literature or more
diverse historical periods. Additionally, the current
focus on written text does not address the phono-
logical aspects of ancient Chinese.
These limitations point to several promising di-
rections for future research, including the devel-
opment of more sophisticated evaluation metrics,
expansion of task coverage, and investigation of
methods to address historical data biases. We hope
that acknowledging these limitations will stimu-
late further research and improvements in ancient
Chinese language processing.
References
Jinze Bai, Shuai Bai, Yunfei Chu, Zeyu Cui, Kai Dang,
Xiaodong Deng, Yang Fan, Wenbin Ge, Yu Han, Fei
Huang, Binyuan Hui, Luo Ji, Mei Li, Junyang Lin,
Runji Lin, Dayiheng Liu, Gao Liu, Chengqiang Lu,
Keming Lu, Jianxin Ma, Rui Men, Xingzhang Ren,
Xuancheng Ren, Chuanqi Tan, Sinan Tan, Jianhong
Tu, Peng Wang, Shijie Wang, Wei Wang, Sheng-
guang Wu, Benfeng Xu, Jin Xu, An Yang, Hao Yang,
Jian Yang, Shusheng Yang, Yang Yao, Bowen Yu,
Hongyi Yuan, Zheng Yuan, Jianwei Zhang, Xingx-
uan Zhang, Yichang Zhang, Zhenru Zhang, Chang
Zhou, Jingren Zhou, Xiaohuan Zhou, and Tianhang
Zhu. 2023. Qwen technical report.
Satanjeev Banerjee and Alon Lavie. 2005. Meteor: An
automatic metric for mt evaluation with improved cor-
relation with human judgments. In Proceedings of
the acl workshop on intrinsic and extrinsic evaluation
measures for machine translation and/or summariza-
tion, pages 65–72.
Tom Brown, Benjamin Mann, Nick Ryder, Melanie
Subbiah, Jared D Kaplan, Prafulla Dhariwal, Arvind
Neelakantan, Pranav Shyam, Girish Sastry, Amanda
Askell, Sandhini Agarwal, Ariel Herbert-Voss,
Gretchen Krueger, Tom Henighan, Rewon Child,
Aditya Ramesh, Daniel Ziegler, Jeffrey Wu, Clemens
Winter, Chris Hesse, Mark Chen, Eric Sigler, Ma-
teusz Litwin, Scott Gray, Benjamin Chess, Jack
Clark, Christopher Berner, Sam McCandlish, Alec
Radford, Ilya Sutskever, and Dario Amodei. 2020.
Language Models are Few-Shot Learners. In Ad-
vances in Neural Information Processing Systems,
volume 33, pages 1877–1901. Curran Associates,
Inc.
Zheng Cai, Maosong Cao, Haojiong Chen, Kai Chen,
Keyu Chen, Xin Chen, Xun Chen, Zehui Chen, Zhi
Chen, Pei Chu, Xiaoyi Dong, Haodong Duan, Qi Fan,
Zhaoye Fei, Yang Gao, Jiaye Ge, Chenya Gu, Yuzhe
Gu, Tao Gui, Aijia Guo, Qipeng Guo, Conghui He,
Yingfan Hu, Ting Huang, Tao Jiang, Penglong Jiao,
Zhenjiang Jin, Zhikai Lei, Jiaxing Li, Jingwen Li,
Linyang Li, Shuaibin Li, Wei Li, Yining Li, Hong-
wei Liu, Jiangning Liu, Jiawei Hong, Kaiwen Liu,
Kuikun Liu, Xiaoran Liu, Chengqi Lv, Haijun Lv,
Kai Lv, Li Ma, Runyuan Ma, Zerun Ma, Wenchang
Ning, Linke Ouyang, Jiantao Qiu, Yuan Qu, Fukai
Shang, Yunfan Shao, Demin Song, Zifan Song, Zhi-
hao Sui, Peng Sun, Yu Sun, Huanze Tang, Bin Wang,
Guoteng Wang, Jiaqi Wang, Jiayu Wang, Rui Wang,
Yudong Wang, Ziyi Wang, Xingjian Wei, Qizhen
Weng, Fan Wu, Yingtong Xiong, Chao Xu, Ruil-
iang Xu, Hang Yan, Yirong Yan, Xiaogui Yang,
Haochen Ye, Huaiyuan Ying, Jia Yu, Jing Yu, Yuhang
Zang, Chuyu Zhang, Li Zhang, Pan Zhang, Peng
Zhang, Ruijie Zhang, Shuo Zhang, Songyang Zhang,
Wenjian Zhang, Wenwei Zhang, Xingcheng Zhang,
Xinyue Zhang, Hui Zhao, Qian Zhao, Xiaomeng
Zhao, Fengzhe Zhou, Zaida Zhou, Jingming Zhuo,
Yicheng Zou, Xipeng Qiu, Yu Qiao, and Dahua Lin.
2024. Internlm2 technical report.
OpenCompass Contributors. 2023.
Opencompass:
A universal evaluation platform for foundation
models.
https://github.com/open-compass/
opencompass.
Yiming Cui, Ziqing Yang, and Xin Yao. 2023. Efficient
and effective text encoding for chinese llama and
alpaca. arXiv preprint arXiv:2304.08177.
Jacob Devlin, Ming Wei Chang, Kenton Lee, and
Kristina Toutanova. 2019. BERT: Pre-training of
9

--- Page 10 ---

deep bidirectional transformers for language under-
standing. NAACL HLT 2019 - 2019 Conference of
the North American Chapter of the Association for
Computational Linguistics: Human Language Tech-
nologies - Proceedings of the Conference, 1:4171–
4186.
Team GLM, Aohan Zeng, Bin Xu, Bowen Wang, Chen-
hui Zhang, Da Yin, Diego Rojas, Guanyu Feng, Han-
lin Zhao, Hanyu Lai, Hao Yu, Hongning Wang, Jiadai
Sun, Jiajie Zhang, Jiale Cheng, Jiayi Gui, Jie Tang,
Jing Zhang, Juanzi Li, Lei Zhao, Lindong Wu, Lucen
Zhong, Mingdao Liu, Minlie Huang, Peng Zhang,
Qinkai Zheng, Rui Lu, Shuaiqi Duan, Shudan Zhang,
Shulin Cao, Shuxun Yang, Weng Lam Tam, Wenyi
Zhao, Xiao Liu, Xiao Xia, Xiaohan Zhang, Xiao-
tao Gu, Xin Lv, Xinghan Liu, Xinyi Liu, Xinyue
Yang, Xixuan Song, Xunkai Zhang, Yifan An, Yifan
Xu, Yilin Niu, Yuantao Yang, Yueyan Li, Yushi Bai,
Yuxiao Dong, Zehan Qi, Zhaoyu Wang, Zhen Yang,
Zhengxiao Du, Zhenyu Hou, and Zihan Wang. 2024.
Chatglm: A family of large language models from
glm-130b to glm-4 all tools.
Aaron Grattafiori, Abhimanyu Dubey, Zhenyu Jauhri,
Yang, Zhiwei Zhao, and Zhiyu Ma. 2024. The llama
3 herd of models.
Geyang Guo, Jiarong Yang, Fengyuan Lu, Jiaxin Qin,
Tianyi Tang, and Wayne Xin Zhao. 2023. Towards
effective ancient chinese translation: Dataset, model,
and evaluation. In Natural Language Processing and
Chinese Computing, pages 416–427, Cham. Springer
Nature Switzerland.
Charles Holcombe. 2006. Rethinking early east asian
history. Education about Asia, 11(2):9–13.
Die Hu, Guangyao Sun, Liu Liu, Chang Liu, and
Dongbo Wang. 2024.
Evaluation of ancient chi-
nese natural language understanding in large lan-
guage models based on achnlu. In Wisdom, Well-
Being, Win-Win, pages 3–18, Cham. Springer Nature
Switzerland.
Yuzhen Huang, Yuzhuo Bai, Zhihao Zhu, Junlei
Zhang, Jinghan Zhang, Tangjun Su, Junteng Liu,
Chuancheng Lv, Yikai Zhang, Jiayi Lei, Yao Fu,
Maosong Sun, and Junxian He. 2023. C-eval: A
multi-level multi-discipline chinese evaluation suite
for foundation models. Advances in Neural Informa-
tion Processing Systems, 36:62991–63010.
Zijing Ji, Yuxin Shen, Yining Sun, Tian Yu, and Xin
Wang. 2021.
C-CLUE: A Benchmark of Classi-
cal Chinese Based on a Crowdsourcing System for
Knowledge Graph Construction.
In Knowledge
Graph and Semantic Computing: Knowledge Graph
Empowers New Infrastructure Construction, pages
295–301, Singapore. Springer.
LYU Wei Lao Bin, PENG Yao and ZHI Sizhe. 2024.
The overview of research status for nlp research in
ancient chinese (2009-2024). Modern Information
Technology, 8(13):146–150+155.
Guoxin Li. 2002. The progress and tasks of digitaliza-
tion of chinese ancient book resources. Journal of
Academic Libraries, (01):21–26+41–91.
Haonan Li, Yixuan Zhang, Fajri Koto, Yifei Yang, Hai
Zhao, Yeyun Gong, Nan Duan, and Timothy Bald-
win. 2024. Cmmlu: Measuring massive multitask
language understanding in chinese.
Haotian Li, Jiatao Zhu, Sichen Cao, Xiangyu Li, Jia-
jun Zeng, and Peng Wang. 2021. Poetic expression
through scenery: Sentimental chinese classical po-
etry generation from images. In Database Systems
for Advanced Applications, pages 629–637, Cham.
Springer International Publishing.
Yanyang Li, Jianqiao Zhao, Duo Zheng, Zi-Yuan Hu,
Zhi Chen, Xiaohui Su, Yongfeng Huang, Shijia
Huang, Dahua Lin, Michael Lyu, and Liwei Wang.
2023. Cleva: Chinese language models evaluation
platform. In Proceedings of the 2023 Conference on
Empirical Methods in Natural Language Processing:
System Demonstrations, pages 186–217, Singapore.
Association for Computational Linguistics.
Chin-Yew Lin. 2004. Rouge: A package for automatic
evaluation of summaries.
In Text summarization
branches out, pages 74–81.
LlamaFamily. 2024. Llama-chinese. https://github.
com/LlamaFamily/Llama-Chinese.
Jingkun Ma, Runzhe Zhan, and Derek F. Wong. 2023.
Yu sheng: Human-in-loop classical chinese poetry
generation system. In Proceedings of the 17th Con-
ference of the European Chapter of the Association
for Computational Linguistics: System Demonstra-
tions, pages 57–66, Dubrovnik, Croatia. Association
for Computational Linguistics.
OpenAI. 2023. Gpt-4 technical report.
Kishore Papineni, Salim Roukos, Todd Ward, and Wei-
Jing Zhu. 2002. Bleu: a method for automatic evalu-
ation of machine translation. In Proceedings of the
40th annual meeting of the Association for Computa-
tional Linguistics, pages 311–318.
Alec Radford, Karthik Narasimhan, Tim Salimans, and
Ilya Sutskever. 2018. Improving Language Under-
standing by Generative Pre-Training.
Yizhan Shao, Tong Shao, Minghao Wang, Peng Wang,
and Jie Gao. 2021. A sentiment and style controllable
approach for chinese poetry generation. In Proceed-
ings of the 30th ACM International Conference on
Information & Knowledge Management, CIKM ’21,
pages 4784–4788, New York, NY, USA. Association
for Computing Machinery.
Qi Su, Yingying Wang, Zekun Deng, Hao Yang, and Jun
Wang. 2023. Overview of ccl23-eval task 1: Named
entity recognition in ancient chinese books. In Pro-
ceedings of the 22nd Chinese National Conference on
Computational Linguistics (Volume 3: Evaluations),
pages 34–40, Harbin, China. Chinese Information
Processing Society of China.
10

--- Page 11 ---

Dongbo Wang, Litao Lin, Zhixiao Zhao, Wenhao Ye,
Kai Meng, Wenlong Sun, Lianzhen Zhao, Xue Zhao,
Si Shen, Wei Zhang, and Bin Li. 2023. EvaHan2023:
Overview of the first international Ancient Chinese
translation bakeoff. In Proceedings of ALT2023: An-
cient Language Translation Workshop, pages 1–14,
Macau SAR, China. Asia-Pacific Association for Ma-
chine Translation.
Hui Wei, Shenghua He, Tian Xia, Andy Wong, Jingyang
Lin, and Mei Han. 2024a. Systematic evaluation
of llm-as-a-judge in llm alignment tasks: Explain-
able metrics and diverse prompt templates. ArXiv,
abs/2408.13006.
Yuting Wei, Yuanxing Xu, Xinru Wei, Simin Yang,
Yangfu Zhu, Yuqing Li, Di Liu, and Bin Wu. 2024b.
Ac-eval: Evaluating ancient chinese language under-
standing in large language models.
Liang Xu, Anqi Li, Lei Zhu, Hang Xue, Changtai Zhu,
Kangkang Zhao, Haonan He, Xuanwei Zhang, Qiyue
Kang, and Zhenzhong Lan. 2023. Superclue: A com-
prehensive chinese large language model benchmark.
Chengyue Yu, Lei Zang, Jiaotuan Wang, Chenyi
Zhuang, and Jinjie Gu. 2024. Charpoet: A chinese
classical poetry generation system based on token-
free llm.
Liu Yutong, Wu Bin, and Bai Ting. 2020. The construc-
tion and analysis of classical chinese poetry knowl-
edge graph. Journal of Computer Research and De-
velopment, 57(6):1252–1268.
Hui Zeng. 2023. Measuring massive multitask chinese
understanding.
Hui Zeng, Jingyuan Xue, Meng Hao, Chen Sun, Bin
Ning, and Na Zhang. 2024. Evaluating the generation
capabilities of large chinese language models.
Yixuan Zhang and Haonan Li. 2023. Can large langauge
model comprehend ancient chinese? a preliminary
test on aclue. In Proceedings of the Ancient Lan-
guage Processing Workshop, pages 80–87, Varna,
Bulgaria. INCOMA Ltd., Shoumen, Bulgaria.
Bin Zhou. 2009. A comprehensive review of japanese
chinese biographical history books. Journal of Histo-
riography, (03):98–104.
Bo Zhou, Qianglong Chen, Tianyu Wang, Xiaomi
Zhong, and Yin Zhang. 2023. WYWEB: A NLP
Evaluation Benchmark For Classical Chinese. In
Findings of the Association for Computational Lin-
guistics: ACL 2023, pages 3294–3319, Toronto,
Canada. Association for Computational Linguistics.
11

--- Page 12 ---

A
ICL Evaluation
The results of 5-shot in-context learning setting are
shown in Table 7. Under in-context learning setting,
each sample is prompted with 5 examples from
the development set. The quantitative statistics of
development set are shown in Table 9.
A.1
In-context Learning Results
Compared to zero-shot performance, we observe
several interesting patterns:
First, in-context learning provides asymmetric
benefits across model scales. Smaller models (<7B
parameters) show substantial improvements with
5-shot examples, with an average gain of 27.4 per-
centage points on tasks like Couplet Generation
(CG). For instance, internlm25_7b improves from
32.4% to 59.8% on pattern-constrained generation
tasks when provided with examples.
Second, larger models (>20B parameters) benefit
less from in-context examples, with an average im-
provement of only 5.9 percentage points across gen-
eration tasks. This suggests that increased model
size reduces context-dependence, as larger models
have already internalized more knowledge during
pre-training.
Third, the performance gap between compre-
hension and generation tasks persists even with
in-context examples. While multiple-choice tasks
like ACRC see modest improvements (average +4.2
points), challenging generation tasks like Ci Poetry
Generation (CiG) remain difficult even with exam-
ples, with only qwen2.5-72b achieving non-trivial
performance (24.0%).
Finally, we observe that domain-specific tasks
benefit more from in-context examples than general
tasks. Traditional Chinese Medicine tasks (TCM-
SRC, TCMQA) show an average improvement of
12.3 percentage points with 5-shot examples, sug-
gesting that specialized knowledge can be effec-
tively activated through demonstration.
B
LLM Evaluator Details
To evaluate the open-ended question answering
tasks automatically, LLMs are good choices as we
have witnessed the their impressive performances
on some of our tasks. However, directly using
LLMs to evaluate open-ended question answering
tasks is not a good idea as the LLMs are not reliable.
To address this issue, we first design a LLM-based
evaluator following the principles outlined in the
LangChain 4 evaluation framework. Unfortunatly,
even under the langhcain framework, the LLM eval-
uator is still not reliable on judge’s role.
To this end, we further design a training dataset
of 2,000 human-annotated examples, where each
example consists of evaluation criteria, task input,
reference answers, and predicted answers, along
with binary correctness labels. Furthermore, the
model is required to output its own reasoning for
the judgments. The prompt template is demon-
strated in Figure 4. We use the dataset to fine-tune
Qwen2-7B-Instruct, resulting in our LLM Evalua-
tor.
C
Case Study and Error Analysis
As shown in Table 10, we take some examples of
Inverse Poetry Translation task from the zero-shot
evaluation results. This is a super-easy task for
human beings, but it is still challenging for LLMs.
Given the modern Chinese version of the poem,
human beings can easily find the corresponding
ancient Chinese version. However, LLMs either
fails to generate a poem-like content(llama31-8b,
qwen2.5-72b) or generates a wrong poem(llama31-
8b-chinese, glm4-9b, qwen2.5-3b). Xunzi-qwen2-
7b generates many irrelevant content and show a
topic shift in the end. GPT-4o-mini generates most
of the content correctly, but it still fails on some
tiny mistakes. This phenomenon is also observed
across all models.
D
Task Examples
The examples of all tasks in Fuxi benchmark are
demonstrated below.
4https://github.com/langchain-ai/langchain
12

--- Page 13 ---

Model
ACRC
IRC
TCMSRC
ASQA
LCQA
BA
BD
BCC
PG
PLST
FQST
IST
IPT
PT
ACT
PA
IE
TCMQA
PE
glm-4-plus
78.67
88.40
88.80
42.68
46.40
42.97
67.20
79.89
63.00
45.75
77.00
51.66
34.67
16.10
26.57
9.24
8.56
48.85
3.58
internlm25_7b
51.00
68.20
51.64
6.33
16.60
0.78
22.04
48.50
10.00
3.50
10.50
2.49
23.00
1.92
7.06
6.94
68.53
9.24
1.73
internlm25_20b
43.67
64.90
73.22
8.68
7.40
4.69
6.45
64.10
13.00
4.75
37.50
10.50
32.33
3.48
9.88
5.58
81.63
6.11
2.33
glm4_9b
40.33
75.10
64.75
6.51
18.80
11.46
40.32
75.38
26.00
4.25
35.00
11.95
32.00
5.11
19.72
6.83
4.35
39.13
7.12
llama31_8b
27.00
25.80
26.59
3.98
1.60
0.78
6.72
56.20
4.00
0.00
0.50
3.12
2.67
55.14
3.39
5.02
76.29
40.62
3.04
llama31_8b_chinese
28.33
15.30
37.89
8.32
2.20
2.34
20.70
64.29
23.00
0.00
4.00
6.24
4.00
28.09
12.50
4.59
75.93
32.65
3.21
qwen2_0.5b
24.67
27.10
25.14
1.63
1.80
1.56
6.99
8.65
1.67
0.75
5.00
2.39
3.67
1.33
4.16
2.70
1.77
31.50
2.37
qwen2_1.5b
39.33
64.00
45.63
4.70
1.80
2.08
11.83
35.53
4.00
3.50
10.50
3.43
9.67
4.35
11.73
4.58
4.20
34.27
5.30
qwen2_7b
63.67
83.40
80.05
15.73
16.60
6.51
29.84
75.00
21.33
17.50
29.50
12.68
28.33
4.41
20.38
6.65
3.71
43.07
4.89
Xunzi_qwen2_7b
34.67
62.40
50.09
1.81
0.40
1.56
5.65
16.73
13.33
3.50
12.50
9.77
6.00
1.28
78.06
5.50
15.23
2.66
48.28
qwen2.5_1.5b
41.67
37.80
46.81
3.98
3.80
4.69
33.87
49.44
9.67
11.75
19.50
5.09
14.67
7.50
19.23
5.06
5.85
46.39
6.66
qwen2.5_3b
58.00
73.00
73.22
22.97
5.00
2.60
29.03
61.09
26.67
20.50
28.50
17.26
24.00
8.04
22.00
6.93
2.71
39.08
6.73
qwen2.5_7b
73.00
82.30
83.97
30.56
18.40
11.46
33.60
82.52
35.00
30.00
34.00
15.28
41.00
7.16
24.27
7.76
2.70
42.98
4.10
qwen2.5_14b
72.33
85.30
85.15
38.16
21.20
12.24
35.22
92.67
54.00
28.00
60.00
35.65
28.33
10.65
21.72
7.25
3.62
33.29
2.98
qwen2.5_72b
83.33
85.60
83.97
49.55
35.20
22.14
47.85
89.47
45.67
50.00
58.00
36.17
66.67
12.35
28.14
8.53
5.98
30.16
7.81
yi34bchat
61.33
81.90
75.14
18.26
8.60
5.99
40.32
69.92
20.33
13.75
30.00
28.48
49.67
11.61
22.09
6.31
5.42
23.66
8.11
Table 7: Evaluation results of selected models on Fuxi benchmark under 5-shot in-context learning settings.
Model
RC
QA
TG
PG
gpt-4o-mini
-
-
-
40.90
gpt-4o
-
-
-
68.37
qwen-max
-
-
-
66.74
glm-4-plus
85.29
55.12
18.82
49.17
internlm25-7b
56.95
14.37
15.90
39.24
internlm25-20b
60.60
18.94
18.17
25.54
glm4-9b
60.06
26.17
13.71
33.74
llama31-8b
26.46
7.96
30.58
0.10
llama31-8b-chinese
27.17
13.51
26.16
4.70
qwen2-0.5b
25.64
3.41
7.31
4.17
Xunzi-qwen2-7b
49.05
7.13
25.17
0.00
qwen2-7b
75.71
25.30
13.85
23.44
qwen2.5-1.5b
42.09
15.65
15.12
51.24
qwen2.5-3b
68.07
23.76
14.25
12.90
qwen2.5-7b
79.76
33.18
14.83
57.84
qwen2.5-14b
80.93
40.55
13.25
34.17
qwen2.5-72b
84.30
50.07
15.50
69.74
Table 8: Average performance of models across task
categories under 5-shot in-context learning settings:
Multiple-choice Reading Comprehension (RC), Open-
ended Question Answering (QA), Text Generation (TG)
and Pattern-constrained Generation (PG).
Task
# Questions
# Avg. AL
# Avg. AL
ACRC
5
857. 0
1. 0
IRC
5
152. 2
1. 0
TCMSRC
5
677. 6
1. 0
TCMQA
5
325. 8
40. 6
LCQA
5
44. 6
16. 0
ASQA
5
20. 2
5. 0
BA
5
23. 8
2. 4
BD
5
23. 8
1. 2
BCC
5
52. 8
2. 0
PG
5
27. 4
62. 6
PLST
5
25. 4
11. 0
FQST
5
32. 0
9. 6
IST
5
14. 0
47. 4
IPT
5
2420. 8
1464. 0
PT
5
140. 0
206. 6
ACT
5
36. 4
38. 6
PA
5
63. 6
1100. 0
TCMNER
5
403. 2
117. 2
IE
5
14. 0
16. 2
PE
5
19. 4
63. 8
CG
5
27. 4
13. 4
CiG
5
46. 6
60. 8
Table 9: Quantitative statistics of Question Length and
Answer Length in development set.
13

--- Page 14 ---

Task: Inverse Poetry Translation
Instruction: 根据以下翻译给出对应的古诗词原文。
Give the corresponding original text of ancient poetry based on the following translation.
Input:
听一支新曲喝一杯美酒，还是去年的天气旧日的亭台，西落的夕阳何时再回来？
那花儿落去我也无可奈何，那归来的燕子似曾相识，在小园的花径上独自徘徊。
Listening to a new song and drinking a glass of fine wine, it is still the same weather as last year and the
same pavilion as before. When will the setting sun come back?
I can do nothing about the falling flowers, and the returning swallows seem familiar, wandering alone on
the flower path in the small garden.
Output:
题目: 浣溪沙·一曲新词酒一杯Title: Huanxisha·A new song and a glass of wine
作者: 晏殊Author: Yan Shu
一曲新词酒一杯，去年天气旧亭台。夕阳西下几时回？
无可奈何花落去，似曾相识燕归来。小园香径独徘徊。
A new song and a glass of wine, the weather and pavilions of last year. When will the setting sun return?
The flowers fall helplessly, and the familiar swallows return. I wander alone in the fragrant path of the
small garden.
GPT-4o Correct
这段翻译对应的古诗词是宋代晏殊的《浣溪沙》："**一曲新词酒一杯，去年天气旧亭台。夕阳
西下几时回？无可奈何花落去，似曾相识燕归来。小园香径独徘徊。**"
GPT-4o-mini
这段翻译对应的古诗词原文是《酒泉子·听一曲新词》。这首词是宋代词人温庭筠所作。原文如
下:
听一曲新词，饮一杯旧酒。去年天气旧亭台，夕阳西下几时回？
无可奈何花落去，似曾相识燕归来。小园香径独徘徊。
llama31-8b
秋夕。
llama31-8b-chinese
这段文本并不是直接引用的古典诗词，而是一种现代的表达方式。它表达了一种对往昔美好时
光的怀念和对未来无法重复的事物的无奈。这样的表达手法在现代文学中很常见，但不是古典
诗词的典型风格。
如果要找到古诗词中的类似意境，可以参考以下几首诗：...
glm4-9b
独立小桥风细细，旧时王谢堂前燕，飞入寻常百姓家。
此句诗意大致与给出的翻译相符，原文出自唐代诗人刘禹锡的《陋室铭》。原文中的“独立小桥
风细细”对应“听一支新曲喝一杯美酒”，“旧时王谢堂前燕”对应“那归来的燕子似曾相识”，“飞入
寻常百姓家”则与“那花儿落去我也无可奈何，那归来的燕子似曾相识，在小园的花径上独自徘
徊”相呼应。但由于原文中没有直接提到“西落的夕阳何时再回来”，所以这部分内容在原文中并
没有直接对应。
qwen2.5-3b
根据您提供的翻译，对应的古诗词原句应该是：“去年今日此门中，人面桃花相映红。人面
不知何处去，桃花依旧笑春风。” 这是一首唐人经典的短诗，作者是崔护，出自《题都城南
庄》。您的原句也表达了相似的情感和意境，但这首诗更为人所熟知。
Xunzi-qwen2-7b
回答:《游园不值》（宋·朱熹）山光雨欲满谷，绿绕暗溪乔木。... 《春宵曲》（宋·苏轼）春宵
一刻值千金，花落人亡两不知。问君能有几多愁，恰似一江春水向东流。《如梦令》（宋·李
清照）... 回答:以上是我的演讲稿，希望对您有所帮助。祝您学习愉快！请注意，文字中有两
qwen2.5-72b
听新曲，饮美酒，依旧是去年的天气、旧日的亭台，西下的夕阳何时才能回来？无可奈何花落
去，似曾相识燕归来，小园香径独徘徊。
Table 10: Error Case for Task: Inverse Poetry Translation
14

--- Page 15 ---

作为一名阅卷老师，请根据以下评分标准对以下回答进行评价，评价结果的形式是：如果回答正确，输
出"Y" ，如果回答错误输出"N"。绝对不要输出额外的内容。
评分标准:
• 包含要点: 理解问题和标准回答，之后从标准答案中提取出一个答案要点，预测答案必须包含这个要
点。
• 与标准答案一致: 如果预测答案是一段文字，那么预测答案必须与预标准答案传达的信息一致。
• 符合问题和任务要求: 如果问题要求创作诗词, 那么回答中的诗词创作必须符合要求的主题和格式。
基于对作品的理解进行评判。
• 符合事实: 如果问题要求给出古诗词原文, 那么回答给出的诗句必须是历史上存在的，而且必须和标
准答案一致。
• 预测答案简洁明了: 预测答案需要简洁明了，如果出现重复内容或非中文文本则直接判断为错误。
<start>
***
[任务输入]: {input}
***
[标准答案]: {output}
***
[预测答案]: {prediction}
***
<end>
[评价结果]:\n Y/N \n 判断理由: {reason}
Figure 4: Prompt for the LLM Evaluator.
15

--- Page 16 ---

Task: Ancient Chinese RC
Instruction:
以下是一道文言文阅读理解的单项选择题, 请直接给出正确答案的选项。
The following is a multiple-choice question on ancient Chinese reading comprehension. Please
provide the correct answer option directly.
Input:
文章：古之学者必有师。师者, 所以传道受业解惑也。人非生而知之者, 孰能无惑？惑而
不从师, 其为惑也, 终不解矣。生乎吾前其闻道也固先乎吾吾从而师之生乎吾后其闻道也
亦先乎吾吾从而师之吾师道也夫庸知其年之先后生于吾乎？是故无贵无贱, 无长无少, 道
之所存, 师之所存也。
嗟乎！师道之不传也久矣！欲人之无惑也难矣！古之圣人, 其出人也远矣, 犹且从师而问
焉；今之众人, 其下圣人也亦远矣, 而耻学于师。是故圣益圣, 愚益愚。圣人之所以为圣,
愚人之所以为愚, 其皆出于此乎？
爱其子, 择师而教之；于其身也, 则耻师焉, 惑矣。彼童子之师, 授之书而习其句读者, 非吾
所谓传其道解其惑者也。句读之不知, 惑之不解, 或师焉, 或不焉, 小学而大遗, 吾未见其明
也。巫医乐师百工之人, 不耻相师。士大夫之族, 曰师曰弟子云者, 则群聚而笑之。问之,
则曰："彼与彼年相若也, 道相似也。位卑则足羞, 官盛则近谀。"呜呼！师道之不复, 可知
矣。巫医乐师百工之人, 君子不齿, 今其智乃反不能及, 其可怪也欤！
圣人无常师。孔子师郯子、苌弘、师襄、老聃。郯子之徒, 其贤不及孔子。孔子曰：三人
行, 则必有我师。是故弟子不必不如师, 师不必贤于弟子, 闻道有先后, 术业有专攻, 如是而
已。
李氏子蟠, 年十七, 好古文, 六艺经传皆通习之, 不拘于时, 学于余。余嘉其能行古道, 作
《师说》以贻之。
Article: In ancient times those who wanted to learn would seek out a teacher. A teacher’s role is to
transmit the Way (传道), impart knowledge (受业), and resolve doubts (解惑). Since no one is
born omniscient, who can claim to have no doubts? If one has doubts and is not willing to learn
from a teacher, his doubts will never be resolved. Anyone who was born before me and learned the
Way before me is my teacher. Anyone who was born after me and learned the Way before me
is also my teacher. Since what I desire to learn is the Way, why should I care whether he was
born before or after me? Therefore, it does not matter whether a person is high or low in position,
young or old in age. Where there is the Way, there is my teacher.
Alas! The tradition of honoring teachers has long decayed, making it arduous to dispel human
confusion. The sages of antiquity, far surpassing ordinary people, still learned from teachers.
Modern masses, vastly inferior to sages, shamefully disdain learning from others. Hence, sages
grow wiser, fools grow duller. Is this not the root of their divergence?
Parents hire tutors for children but shun self-improvement—a paradox. A child’s tutor drills texts,
not transmitting the Way or resolving profound doubts. Mastering punctuation yet ignoring truth
prioritizes trivia over substance. Artisans freely learn, yet elites mock teacher-disciple bonds as
"humiliating if inferior, sycophantic if superior." How ironic that despised artisans now surpass
elites in wisdom!
Sages have no fixed teachers. Confucius learned from Tanzi, Chang Hong, Shi Xiang, and Lao
Dan—none surpassing him in virtue. Confucius said: "Among three companions, one must be
my teacher." Thus, disciples need not be inferior to teachers, nor teachers superior to disciples.
Comprehension of the Way varies in timing; expertise differs in specialization—this is all. Li
Pan, seventeen, devoted to classical studies and mastering the Six Arts, learns from me unbound
by contemporary prejudices. I commend his adherence to ancient principles and compose this
Discourse on Teachers for him.
Figure 5: Example for task: Ancient Chinese RC (Part 1).
16

--- Page 17 ---

题目: 下列对原文有关内容的概括和分析，不正确的一项是:
A. 第一段所提出的无论贵贱长幼、有道者皆可为师的择师标准，很有积极意义。
B. 第二段以对比的方法针砭时弊，批判了"士大夫之族"耻于从师的恶劣风气。
C. 第三段以孔子从师为例，阐明教师的作用和"道之所存，师之所存"的道理。
D. 第四段作者借赞扬李蟠“不拘于时”“能行古道”，补充交代本文的写作缘由。
Question: Which analysis of the text is incorrect?
A. The first paragraph establishes a progressive standard for selecting teachers—merit lies in the
Way, transcending hierarchy—which remains socially impactful.
B. The second paragraph critiques societal decay through contrast, condemning the literati-official
class’s shame toward learning from teachers.
C. The third paragraph uses Confucius’s pedagogical examples to illustrate teachers’ roles and the
principle “where the Way resides, there lies the teacher”.
D. The fourth paragraph highlights Li Pan’s defiance of trends and revival of ancient practices,
contextualizing the essay’s purpose.
Output:
C
Figure 5: Example for task: Ancient Chinese RC (Part 2).
Task: Idiom RC
Instruction:
以下是关于成语的单项选择题，请直接给出正确答案的选项。
The following is an idiom-based multiple-choice question. Provide the correct answer option
directly.
Input:
题目: “祸福无门，唯人所召”。中的“祸福无门，唯人所召”的意思是？
A. 重遭祸事，是因为自己没有道德而造成的。
B. 指灾祸和幸福不是注定的，都是人们自己造成的。
C. 指福与祸没有定数，享福太甚就隐伏着祸端。亦作"福为祸先"。
D. 佛家用语，命中注定的灾祸。命中注定的灾祸难以逃脱。
Question: What is the meaning of the idiom “祸福无门，唯人所召”(Fortune and Misfortune
Have No Gate; They Are Summoned by One’s Own Deeds.) in the sentence?
A. Misfortunes recur due to one’s lack of virtue.
B. Disasters and blessings are not predetermined but caused by people’s own actions.
C. Fortune and misfortune are unpredictable; excessive enjoyment may lead to disaster. Also called
"fortune precedes misfortune".
D. Buddhist terminology: Predestined calamities that are inescapable.
Output:
B
Figure 6: Example for task: Idiom RC.
17

--- Page 18 ---

Task: TCM Syndrome RC
Instruction:
以下是关于中医辨证的单项选择题，请直接给出正确答案的选项。
The following is a multiple-choice question on Traditional Chinese Medicine (TCM) syndrome
differentiation. Provide the correct answer directly.
Input:
题目: 根据以下病人的情况进行中医辩证。
主诉: 肛内肿物外脱伴肿痛便血1周
描述: 患者1周来反复出现肛内肿物外脱伴肿痛便血，外用药物治疗。大便日行1-2次，质
稀不成形，排便畅但伴暗红色大量便血、排便不尽及肛门坠胀感。舌淡红苔白，脉数。
无发热恶寒及粘液便。
检查: 神清体健，皮肤无异常，腹部平软，双下肢无浮肿。舌脉同上。
以下选项中最恰当的中医辨证是？
A. 外伤损络证
B. 心脾两虚证
C. 风寒阻络证
D. 湿热下注证
Case Presentation: A patient presents with 1-week history of prolapsed hemorrhoids accompanied
by swelling, pain, and hematochezia. Stools are loose and frequent (1-2/day) with dark-red blood,
incomplete defecation, and anal distension. Tongue: pale-red with white coating; Pulse: rapid. No
fever/chills or mucous stool. Physical exam unremarkable.
Output:
D
Figure 7: Example for task: TCM Syndrome RC.
Task: Allegorical Saying QA
Instruction:
给出以下歇后语的后半句谜底。
Complete the second metaphorical half of the Allegorical Saying QA (traditional Chinese riddle
idiom).
Input:
墙头草随风倒
“The wall-top grass sways with the wind” — Symbolizing opportunistic vacillation
Output:
两面装好人
“Maintains dual facades of virtue” — Liˇangmiàn zhu¯ang hˇaorén (lit. two-faced pretense of
goodness), satirizing hypocrisy through the pun: 装(pretend) vs. 伪(false)
Figure 8: Example for task: Allegorical Saying QA.
18

--- Page 19 ---

Task: Loan Character QA
Instruction:
请帮我找出下面文言文句子中的通假字。
Please help me identify the loan characters in the following classical Chinese sentence.
Input:
人之言，苟亦信。
“People’s words, if insincere, should not be trusted.”
Output:
“”, 诈伪之言。，通“”。
“” (wéi), meaning deceitful words. Here, functions as a loan character for (wˇei, ’false’).
Figure 9: Example for task: Loan Character QA.
Task: Book Author
Input:
请问《关大王独赴单刀会》的作者是谁？
Who is the author of "King Guan Attending the Single Sword Meeting Alone"?
Output:
关汉卿Guan Hanqing
Figure 10: Example for task: Book Author.
Task: Book Dynasty
Input:
请问《涉异志》这本书写成于哪个朝代？
In which dynasty was "Records of Encountering Anomalies" written?
Output:
明; Ming Dynasty
Figure 11: Example for task: Book Dynasty.
Task: Book Collection Classification
Instruction:
请将提供的书归类到易藏、医藏、艺藏、诗藏、史藏、子藏、集藏、儒藏、道藏佛藏中
的一类。
Classify the provided book into one of the following categories: Yi (Changes), Medicine, Arts,
Poetry, History, Philosophy, Collections, Confucianism, Taoism and Buddhism.
Input:
《伤寒论集注》Collected Commentary on the Treatise on Cold Damage Disorders
Output:
医藏; Medicine Collection
Figure 12: Example for task: Book Collection Classification.
19

--- Page 20 ---

Task: Poetry Generation
Instruction:
给出一首符合下述关键词的五言诗、七言诗或者词。
Generate a classical poem (wuyan/qiyan/ci) that embodies the given thematic keywords.
Input:
写雪、抒情Themes: Snowscape depiction; Lyric expression
Output:
雪散因和气，冰开得暖光。
春销不得处，唯有鬓边霜。
Snow melts by gentle warmth, ice thaws into radiant light.
Spring cannot erase all traces—only frost at the temples remains.
(Bai Juyi, Tang Dynasty, "Musing on Transience")
*五言绝句wuyan jueju (five-character quatrain)
*七言律诗qiyan lüshi (seven-character regulated verse)
*词ci (Lyrical poetry adhering to specific cipai (词牌) tonal patterns.)
Figure 13: Example for task: Poetry Generation.
Task: Poetry Line Source Tracing
Instruction:
请给出以下句子的出处。
Please provide the source of the following poetic lines.
Input:
草枯鹰眼疾, 雪尽马蹄轻。
Withered grass sharpens eagle eyes, melted snow lightens horse hooves.
Output:
王维《观猎》Wang Wei’s "Watching the Hunt"
Figure 14: Example for task: Poetry Line Source Tracing.
Task: Famous Quote Source Tracing
Instruction:
请给出以下句子的出处。
Please identify the source of the following classical Chinese quotation.
Input:
“尽信书，则不如无书。”
“If one believes everything in books, it would be better not to have books at all.”
Output:
《孟子·尽心章句下·第三节》
Mèngzˇı · Jìn X¯ın II · Section 3 (Mencius, Jin Xin Chapter Part 2),
*This dictum reflects Mencius’ emphasis on critical thinking in Confucian philosophy.
Figure 15: Example for task: Famous Quote Source Tracing.
20

--- Page 21 ---

Task: Idiom Source Tracing
Instruction:
给出以下成语的出处。
Provide the source of the following idiom.
Input:
老马识途; An old horse knows the way
Output:
《韩非子·说林上》管仲、隰朋从于桓公伐孤竹, 春往冬返, 迷惑失道。管仲曰’老马之智可
用也。’乃放老马而随之。遂得道。
From "Han Feizi · Forest of Persuasion I": When Guan Zhong and Xi Peng followed Duke Huan
to attack Guzhu, they lost their way returning in winter after departing in spring. Guan Zhong said,
"The wisdom of an old horse can be useful. " They then let the old horse lead the way and found
their path.
Figure 16: Example for task: Idiom Source Tracing.
Task: Inverse Poetry Translation
Instruction:
根据以下翻译给出对应的古诗词原文。
Provide the original classical Chinese poem corresponding to the following modern translation.
Input:
预备丰盛的饭菜，邀请我到他好客的农家。
翠绿的树林围绕着村落，苍青的山峦在城外横卧。
推开窗户面对谷场菜园，手举酒杯闲谈庄稼情况。
等到九九重阳节到来时，再请君来这里观赏菊花。
My old friend prepares chicken and millet feast, inviting me to his rustic abode.
Emerald woods embrace the village, azure hills recline beyond the walls.
Opening windows to threshing fields, we toast and speak of crops.
When the Double Ninth Festival arrives, I’ll return to admire chrysanthemums.
Output:
题目: 过故人庄作者: 孟浩然
故人具鸡黍，邀我至田家。
绿树村边合，青山郭外斜。
开轩面场圃，把酒话桑麻。
待到重阳日，还来就菊花。
Title: Passing the Old Friend’s Village Author: Mèng Hàorán (Meng Haoran, Tang Dynasty poet)
“My friend has chicken and millet prepared,
Bidding me come to his rustic cottage.
Green trees encircle the village,
Blue hills slant beyond the outer walls.
Open the windows facing field and garden,
Raise wine cups discussing mulberry and hemp.
When comes the Double Ninth Day,
Again I’ll come to savor chrysanthemums.”
* 桑麻(s¯ang má) symbolizes agricultural affairs; 重阳(Chóngyáng) refers to the traditional festival on the 9th day of
the 9th lunar month.
Figure 17: Example for task: Inverse Poetry Translation.
21

--- Page 22 ---

Task: Poetry Translation
Instruction:
翻译以下诗词。
Translate the following classical Chinese poem into modern Chinese prose.
Input:
题目: 闺怨作者: 王昌龄
闺中少妇不知愁，春日凝妆上翠楼。
忽见陌头杨柳色，悔教夫婿觅封侯。
Title: Boudoir Lament Author: Wang Changling
“The young wife in her chamber knows not sorrow’s trace,
Adorned in spring splendor, ascends the jade tower’s grace.
Sudden sight of willow hues by the roadside lane,
Regrets urging her lord to seek honors on the frontier plain.”
Output:
闺中少妇未曾有过相思离别之愁，在明媚的春日，她精心妆饰，登上高楼。
忽然看到路边的杨柳春色，惆怅之情涌上心头。她后悔当初不该让丈夫从军边塞，建功
封侯。
The young gentlewoman, untouched by parting grief in her chamber,
Ascends the emerald tower in radiant spring, adorned with care.
Startled by willow-green hues along the path,
Regret floods her heart—why bid her lord seek glory on distant frontiers?
* 觅封侯(mì f¯enghóu) refers to pursuing military honors during the Tang frontier campaigns.
Figure 18: Example for task: Poetry Translation.
Task: Ancient Chinese Translation
Instruction:
将这句话翻译为现代汉语：
Translate the following classical Chinese sentence into modern Chinese.
Input:
秋，征堪、向，欲以为谏大夫，恭、显白皆为中郎。
“In autumn, [the emperor] summoned Zhou Kan and Liu Xiang, intending to appoint them as
Remonstrance Grand Masters. However, Hong Gong and Shi Xian reported [against this], and all
were made Central Lang Officers.”
Output:
秋天，征召周堪、刘向，想任命为谏大夫，弘恭、石显禀告，都做了中郎。
In autumn, Zhou Kan and Liu Xiang were summoned to the court with the intention of appointing
them as Remonstrance Grand Masters (Jiàn Dàf¯u 谏大夫). However, Hong Gong (Hóng G¯ong 弘
恭) and Shi Xian (Shí Xiˇan 石显), through their memorials (bái 白), intervened, resulting in both
scholars being appointed instead as Central Lang Officers (Zh¯ong Láng 中郎), a rank of palace
guards.
*征堪、向, 周堪(Zh¯ou K¯an)、刘向(Liú Xiàng) Renowned scholars of the Han Dynasty
*谏大夫(Jiàn Dàf¯u), 监察官职Remonstrance Grand Master
*中郎(Zh¯ong Láng), 宫廷侍卫官Central Lang Officer
*白(Bái), 禀告奏议的缩略语Abbreviation for reporting memorials
Figure 19: Example for task: Ancient Chinese Translation.
22

--- Page 23 ---

Task: Poetry Appreciation
Instruction:
赏析以下诗词。
Analyze the following classical Chinese poetry.
Input:
小令尊前见玉箫。银灯一曲太妖娆。歌中醉倒谁能恨，唱罢归来酒未消。
春悄悄，夜迢迢。碧云天共楚宫遥。梦魂惯得无拘检，又踏杨花过谢桥。
Title: Partridge Sky (鹧鸪天) Author: Yàn Jˇıdào (晏几道, Song Dynasty)
Output:
上阕解析
词写春夜怀人，深情款款。起句用韦皋玉
箫典故，暗喻前世情缘。
The opening couplet alludes to the legendary romance
between Wéi G¯ao and Jade Xiao, symbolizing predestined
love. The "silver lamp" illuminates an enchanting musical
performance, showcasing the poet’s profound captivation.
下阕解析
春夜迢迢，楚宫隐喻美人遥不可及。末
句"踏杨花过谢桥"乃千古名句，
The imagery of "treading catkins past Xie Bridge" (踏杨
花过谢桥) embodies transcendent dream-journeys, be-
coming an iconic representation of unconstrained spiritual
longing in Chinese literature.
艺术特色
虚实相生：宴饮之乐与孤眠清寂的强烈对比
用典技法：玉箫典故深化情感厚度
时空处理：现实物理时空vs. 梦境心理时空
Duality of presence: Contrast between banquet revelry and solitary longing
Intertextuality: Historical allusion enhances emotional depth
Chronotopic innovation: Physical-temporal constraints vs. dreamscape freedom
* 韦皋玉箫故事见《云溪友议》卷三
* 谢桥意象源于谢娘典故，象征才子佳人相会之地
* The Wei-Jade legend from Records of Yunxi Friends (云溪友议)
* Xie Bridge symbolizes literati-romantic encounters in classical tradition
Figure 20: Example for task: Poetry Appreciation.
Task: Idiom Explanation
Instruction:
给出以下成语的解释。
Provide the explanation for the following idiom.
Input:
衅起萧墙; Trouble begins within the inner walls
Output:
萧墙古代宫室内当门的小墙。指祸乱发生在家里。比喻内部发生祸乱。
Xiaowang refers to the small wall inside ancient palace doors. It indicates trouble arising within
one’s own household, metaphorically describing internal strife.
Figure 21: Example for task: Idiom Explanation.
23

--- Page 24 ---

Task: TCM QA
Instruction:
根据以下文本回答问题。
Answer the question based on the following text.
Input:
饮食减肥是很多人在春天减肥最常见的一种方法。不仅是因为饮食减肥效果最显著，还
因为饮食减肥方法最简单。今天，要为大家推荐的就是减肥水果和汤粥，快来看看都有
哪些吧。
巧选水果。
选择含糖较少的水果。据研究，菠萝、哈蜜瓜、木瓜、奇异果、香蕉、葡萄等水果的血
糖指数较高，减肥族应避免摄取太多这类水果。而像苹果、猕猴桃、柠檬、李子、樱
桃、柑橘类等血糖指数较低，是减肥族在搭配水果餐时的较佳选择。
餐前吃水果。
想要水果帮助我们实现减肥的效果，您在生活中就要注意进行水果饮食的时间。研究表
明：如在进餐前20分钟至40分钟吃一些水果或饮用1至2杯果汁，则可防止进餐过多导致
的肥胖。因为水果或果汁中富含果糖和葡萄糖，可快速被机体吸收，提高血糖浓度，降
低食欲。水果内的粗纤维还可让胃部有饱胀感。合理使用水果。饮食对于我们健康的重
要性是不能忽视的，尤其是水果的饮食，您就要更加的注意。水果的食用量不要过多。
大多数人认为，水果富含纤维素，几乎不含脂肪和蛋白质，因而可以无节制地放心食
用，其实这是一个误区。水果并非能量很低的食品，由于味道甜美很容易吃得过多，其
中的糖就会转化为脂肪而堆积。
问题：减肥适合吃哪几种水果？
Dietary regulation remains the most prevalent weight-loss approach in spring, valued for its
efficacy and simplicity. This article recommends fruits and soups for weight management, with
evidence-based strategies:
Strategic Fruit Selection
Prioritize low-glycemic-index fruits: Apples, kiwifruit, lemons, plums, cherries, and citrus varieties.
Avoid high-glycemic fruits such as pineapple, honeydew melon, papaya, banana, and grapes, as
indicated by glycemic load studies.
Temporal Optimization
Consume fruits or 100% fruit juice 20-40 minutes before meals. This timing: Facilitates rapid
absorption of fructose and glucose, which elevates blood glucose levels and suppresses appetite.
Leverages dietary fiber to induce gastric distension, thereby enhancing satiety signals. Quantitative
Control Counteract the common misconception that fruits can be consumed without limits: Fruits
contain non-negligible caloric density (4 kcal per gram of carbohydrates). Excessive intake triggers
hepatic lipogenesis, converting sugars into stored fat.
Output:
苹果、猕猴桃、柠檬、李子、樱桃、柑橘类等血糖指数较低，是减肥族在搭配水果餐时
的较佳选择。
Apples, kiwis, lemons, plums, cherries, and citrus fruits with low glycemic index are optimal
choices for weight-loss diets.
Figure 22: Example for task: TCM QA.
24

--- Page 25 ---

Task: Prescription Explanation
Instruction:
给出以下中药方剂的成份以及功效。
Provide the ingredients and efficacy of the following Chinese medicine prescription.
Input:
竹叶汤Bamboo Leaf Decoction
Output:
成份: 淡竹叶、黄芩、升麻、木通、车前子、黄连、玄参、芒消、栀子、大黄（炒）。
功效: 肝脏实热, 眼赤肿痛。
Ingredients: Lophatherum gracile, Scutellaria baicalensis, Cimicifuga heracleifolia, Akebia quinata,
Plantago asiatica, Coptis chinensis, Scrophularia ningpoensis, Natrii Sulfas, Gardenia jasminoides,
processed Rheum officinale.
Efficacy: Treats liver heat and red, swollen, painful eyes.
Figure 23: Example for task: Prescription Explanation.
Task: Couplet Generation
Instruction:
对对联, 请根据上联生成下联。
Generate the second line of a couplet based on the first line.
Input:
荷出污泥而不染, 品格高超可为友
The lotus emerges from the mud unstained; its noble character makes it worthy of friendship
Output:
竹生有节且虚心, 性质坚韧能抵风
The bamboo grows with joints and humble heart; its resilient nature can resist the wind
Figure 24: Example for task: Couplet Generation.
Task: Ci Generation
Instruction:
按照提供的词牌名和题目写一首词, 要求严格遵守词牌的格律。
Write a Ci poem according to the provided Cipai (词牌, Ci Tune Pattern) and title, strictly following
the metrical rules of the Cipai.
Input:
词牌: 望江南Cipai: Gazing at the Yangtze’s South
题目: 红桥春游词Title: A Spring Outing at Hong Bridge
Output:
江南好, 修袅袅溪光。杨柳风微莺嘴滑, 桃花漾足鸭头香。几处洗衣裳。
The South of Yangtze is lovely,
I seize the creek’s gleam for the spring ritual.
In gentle breeze willows sway, while warblers’ tongues slip sweet songs,
Peach blossoms flood the scene with fragrance thick as ducks’ heads,
Here and there, women wash their clothes.
Figure 25: Example for task: Ci Generation.
25

```
