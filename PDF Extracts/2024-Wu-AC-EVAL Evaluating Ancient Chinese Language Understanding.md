---
title: "2024-Wu-AC-EVAL Evaluating Ancient Chinese Language Understanding - PDF Extract"
source_pdf: "2024-Wu-AC-EVAL Evaluating Ancient Chinese Language Understanding.pdf"
pages: 15
extracted_at: "2026-02-13T09:15:45.259121"
---

# PDF Extract: 2024-Wu-AC-EVAL Evaluating Ancient Chinese Language Understanding

**Source PDF:** 2024-Wu-AC-EVAL Evaluating Ancient Chinese Language Understanding.pdf
**Total Pages:** 15

---

## Content

```
--- Page 1 ---

AC-EVAL: Evaluating Ancient Chinese Language Understanding in Large
Language Models
Yuting Wei, Yuanxing Xu, Xinru Wei, Simin Yang, Yangfu Zhu,
Yuqing Li, Di Liu, Bin Wu*
Beijing Key Laboratory of Intelligence Telecommunication Software and Multimedia,
Beijing University of Posts and Telecommunications
{yuting_wei, xyx, wxr2000, ysm2000, zhuyangfu, liyuqing, liudi, wubin}@bupt.edu.cn
Abstract
Given the importance of ancient Chinese in cap-
turing the essence of rich historical and cultural
heritage, the rapid advancements in Large Lan-
guage Models (LLMs) necessitate benchmarks
that can effectively evaluate their understand-
ing of ancient contexts. To meet this need, we
present AC-EVAL, an innovative benchmark
designed to assess the advanced knowledge and
reasoning capabilities of LLMs within the con-
text of ancient Chinese. AC-EVAL is struc-
tured across three levels of difficulty reflect-
ing different facets of language comprehension:
general historical knowledge, short text under-
standing, and long text comprehension. The
benchmark comprises 13 tasks, spanning histor-
ical facts, geography, social customs, art, phi-
losophy, classical poetry and prose, providing
a comprehensive assessment framework. Our
extensive evaluation of top-performing LLMs,
tailored for both English and Chinese, reveals a
substantial potential for enhancing ancient text
comprehension. By highlighting the strengths
and weaknesses of LLMs, AC-EVAL aims to
promote their development and application for-
ward in the realms of ancient Chinese language
education and scholarly research.1
1
Introduction
The advent of Large Language Models (LLMs)
has significantly impacted Natural Language Pro-
cessing (NLP), highlighting their importance in un-
derstanding and generating human languages (Wei
et al., 2022a; Zhou et al., 2022; Zhao et al., 2023).
With the rise of Chinese as a major global lan-
guage, there has been a surge in Chinese-specific
LLMs (Zeng et al., 2022; Bai et al., 2023; Baichuan,
2023). Ancient Chinese, a crucial part of the Chi-
nese language, records a rich historical and cultural
heritage, and has garnered considerable attention
*Corresponding Author.
1The AC-EVAL data and evaluation code are available at
https://github.com/yuting-wei/AC-EVAL.
from computational linguists (Li et al., 2022; Wang
et al., 2023). LLMs present significant opportuni-
ties for enhancing the pedagogy of Chinese liter-
ary education through convenient text analysis and
comprehension. Therefore, assessing the ancient
Chinese comprehension capabilities of LLMs holds
significant importance.
Initially, benchmarks for LLMs primarily tar-
geted the assessment of English language under-
standing, exemplified by MMLU (Hendrycks et al.,
2021), BIG-bench (Srivastava et al., 2023) and
HELM (Liang et al.). Subsequently, several bench-
marks focusing on Chinese, such as C-Eval (Huang
et al., 2023), CMMLU (Li et al., 2023a), and Super-
CLUE (Xu et al., 2023), were introduced. These
benchmarks aim to evaluate the reasoning perfor-
mance of LLMs across a broad spectrum of fields
including STEM, social sciences, and humanities.
However, these benchmarks tend to lean towards
modern Chinese comprehension. While some in-
clude tasks related to Chinese language, literature
and history, they are often relegated to minor cate-
gories, insufficient for a comprehensive coverage
of ancient Chinese knowledge and language assess-
ment. Existing benchmarks for ancient Chinese
understanding, such as CCLUE 2 and WYWEB
(Zhou et al., 2023), cover various aspects but pri-
marily focus on linguistic feature analysis, fre-
quently overlooking the assessment of historical
knowledge hidden in literature. Furthermore, the
diversity in format across these datasets, tailored
for specific tasks rather than providing a unified
assessment framework, complicates the evaluation
of LLMs, presenting challenges in conducting uni-
form assessments.
To bridge this gap, we propose AC-EVAL (as
illustrated in Figure 1), a benchmark meticulously
designed for a comprehensive evaluation of LLMs’
proficiency in ancient Chinese language under-
2https://github.com/Ethan-yt/guwen-models
1
arXiv:2403.06574v1  [cs.CL]  11 Mar 2024

--- Page 2 ---

General 
Historical 
Knowledge
历史史实Historical Facts
古代地理Geography
社会生活习俗Social Customs
艺术和文化传承Art and Cultural Heritage
哲学和宗教Philosophy and Religion
文本断句任务Sentence Pauses
文本概括和分析Summarization and Analysis
诗歌鉴赏Poetry Appreciation
词语语用分析Lexical Pragmatics Analysis
典故和成语理解Allusions and Idioms
词义消岐Word Sense Disambiguation
古文翻译Translation
事件抽取Event Extraction
Short Text
Understanding
Long Text Understanding
Figure 1: Overview of AC-EVAL.
standing and historical knowledge. AC-EVAL com-
prises 3,245 multiple-choice questions, spanning
three distinct dimensions and thirteen subjects, cov-
ering historical periods from the Pre-Qin to the
Qing dynasty. These tasks, which progressively
increase in difficulty, are categorized into general
historical knowledge, short text understanding, and
long text understanding. The general historical
knowledge tasks address a diverse range of con-
tents, including but not limited to, ancient historical
facts, geography, social customs, art, religion and
philosophy. Short text understanding covers lexical
semantics and pragmatics, allusions and idioms,
sentence translations, and event extraction. Long
text understanding tasks focus on long text pauses,
classical prose summarization and analysis, and
the appreciation of themes, emotions and styles in
poetry.
In our evaluation of LLMs on the AC-EVAL
benchmark across answer-only (AO) and chain-
of-thought (COT) settings in zero- and few-shot
scenarios, only ERNIE-Bot 4.0 and GLM-4 with
accuracies over 70%. Results reveal significant
improvement potential, especially in long text com-
prehension. Our analysis shows that Chinese LLMs
outperform English ones in ancient Chinese. This
distinction underscores the unique challenge that
ancient Chinese as a low-resource area for mod-
els like GPT-4, despite their commendable perfor-
mance on other Chinese benchmarks. Moreover,
the broad range of knowledge required in our tasks
reveals that LLMs encounter difficulties in grasp-
ing underlying rules, affecting few-shot learning
outcomes. Interestingly, zero-shot COT shows an
advantage in larger models, underscoring the value
of reasoning steps for complex tasks. Through the
AC-EVAL benchmark, our goal is to provide a mul-
tidimensional evaluation tool, highlighting poten-
tial improvement areas to advance the development
of LLMs in the understanding and education of
ancient Chinese.
2
Related Work
2.1
Chinese benchmarks for LLMs
In the evolving landscape of NLP, the development
of benchmarks to evaluate LLMs in comprehending
Chinese has been a focal point of recent research
(Chang et al., 2023). Benchmarks such as MMCU
(Zeng, 2023), C-Eval (Huang et al., 2023), and
CMMLU (Li et al., 2023a) derived primarily from
official examination questions, spanning various
disciplines including STEM, humanities, social sci-
ences, and professional qualification tests for fields
like law and medicine. These benchmarks aimed
to comprehensively assess the breadth of domains
relevant to the Chinese language, primarily utiliz-
ing multiple-choice questions as their core compo-
nents. AGIEval (Zhong et al., 2023) expanded upon
these by incorporating fill-in-the-blank questions
alongside multiple-choice. CG-Eval (Zeng et al.,
2023) and CLEVA (Li et al., 2023b), on the other
2

--- Page 3 ---

hand, took a more holistic approach to measure
models’ generative abilities, including tasks such
as noun explanation, short answer questions, and
computational problems. SuperCLUE (Xu et al.,
2023) evaluated models across three dimensions:
foundational abilities, professional knowledge, and
Chinese language characteristics by leveraging ac-
tual user queries and ratings, along with a mix of
open- and closed-ended questions. Lastly, Open-
Compass (Contributors, 2023) integrates over 100
public datasets into a unified leaderboard frame-
work, standardizing the assessment of LLMs.
Despite the extensive range of current bench-
marks, there is a significant gap in their coverage
of the ancient Chinese language, literature, and his-
tory. Considering the depth and breadth of Chinese
millennia-long history, which includes evolving so-
cial customs, religious beliefs, geographical bound-
aries, and linguistic changes, it is evident that a
more comprehensive benchmark is necessary.
2.2
Ancient Chinese benchmarks
Ancient Chinese, a fundamental component of the
Chinese linguistic heritage, encapsulates millen-
nia of historical narratives and cultural wisdom. A
multitude of traditional and diverse datasets has
been proposed to evaluate the ancient Chinese lan-
guage understanding capabilities with various spe-
cific tasks (Pan et al., 2022; Wang and Ren, 2022;
Liu et al., 2022; Tang and Su, 2022).
For instance, analyzing the sentiments and
themes in poetry (as seen in FSPC (Shao et al.,
2021) and TCCP (Liu et al., 2020), to the intricate
task of translating between classical and modern
Chinese, (illustrated by the Classical-Modern cor-
pus3 and the Erya dataset (Guo et al., 2023)). Fur-
thermore, named entity recognition and relation-
ship extraction tasks, with datasets like C-CLUE (Ji
et al., 2021) and GuNER 20234, provide a founda-
tion for in-depth linguistic analysis within ancient
texts. GuwenEE5, an event extraction dataset, is
annotated and constructed from the "Twenty-Four
Histories," a collection of Chinese official historical
literature. The word sense disambiguation dataset
for ancient Chinese, introduced by Shu et al. (2021),
encompasses texts from multiple dynasties. Ad-
ditionally, the EvaHan series from 2022 to 2024
introduces a spectrum of tasks including sentence
segmentation, POS tagging, and machine transla-
3https://github.com/NiuTrans/Classical-Modern
4https://guner2023.pkudh.org
5https://github.com/Lyn4ever29/GuwenEE
tion. Comprehensive benchmarks like CCLUE and
WYWEB (Zhou et al., 2023) integrate a variety of
language understanding tasks, ranging from text
classification to poetry analysis and machine read-
ing comprehension, offering a holistic evaluation
of models’ linguistic proficiency.
However, despite the breadth of these bench-
marks, there remains a discernible gap in the assess-
ment of models’ grasp of the historical knowledge
hidden within ancient texts. The varied formats
of datasets, designed for specific tasks, hinder uni-
form LLM evaluation, highlighting the urgent need
for an integrated benchmark to thoroughly assess
LLMs’ understanding of ancient Chinese literature
and history knowledge.
3
AC-EVAL Overview
3.1
Design Principles
The motivation behind constructing AC-EVAL is
to comprehensively assess LLMs’ understanding
and reasoning capabilities regarding the shifts in
societal customs, culture, and language throughout
millennia of history. It adheres to four foundational
principles to ensure a holistic evaluation frame-
work:
Temporal Coverage: It spans from the pre-Qin
period to the Qing dynasty, offering a wide histori-
cal scope that covers thousands of years of evolu-
tion.
Task Difficulty Diversity:
The benchmark
ranges from basic fragmented historical knowledge
to complex tasks requiring the understanding of
ancient Chinese texts of various lengths, providing
a graded evaluation of model capabilities.
Content Diversity: It encompasses a broad spec-
trum of knowledge areas including historical facts,
geography, religion, philosophy, social customs,
architecture, music, and handicrafts, along with
tasks in classical language understanding such as
semantic and syntactic analysis.
Data Quality: While ensuring the authority of
the data, we also take specific measures to mitigate
data contamination, as detailed in section 3.2.
Our benchmark is organized into 3 major cate-
gories and 13 subjects, encompassing general his-
torical knowledge as well as both short- and long-
text comprehension of ancient Chinese. In align-
ment with the methodology proposed by Huang
et al. (2023), we adopt a uniform question format,
presenting each question with four answer options.
Each subject within the benchmark contains an av-
3

--- Page 4 ---

Category
Difficulty
# Subjects
# Questions
Average Length
General Historical Knowledge
Easy
5
1014
62.78
Short Text Understanding
Normal
5
1215
214.19
Long Text Understanding
Hard
3
1016
536.95
Table 1: Statistics of AC-EVAL. The average length is measured in characters.
erage of over 200 questions, of which five with
explanations are designated for development sets.
The statistical summary of AC-EVAL is depicted in
Table 1, and a more detailed statistical breakdown
is available in Appendix A.
3.2
Data Collection
Subject Selection: Our benchmark encompasses
general historical knowledge and classical Chinese
text comprehension. For the former, we have iden-
tified five subcategories, namely: Historical Facts,
Geography, Social Customs, Art and Cultural Her-
itage, Philosophy and Religion. For the latter, we
distinguish between short texts, which include tasks
such as Lexical Pragmatics Analysis, Allusions and
Idioms, Word Sense Disambiguation, Translation,
and Event Extraction, and long texts, which cover
Sentence Pauses, Summarization and Analysis, and
Poetry Appreciation, as illustrated in Figure 1.
Data Source: The dataset is derived from four
main sources: (1) the Complete Library in Four
Branches (Siku Quanshu), offering a comprehen-
sive collection of ancient Chinese texts; (2) spe-
cialized books on ancient Chinese social customs,
architectural history, music history, and geography;
(3) official or mock examinations; and (4) existing
non-multiple-choice datasets on ancient Chinese,
such as GuwenEE.
Data processing: Initially, we recruited under-
graduate students and linguistics experts as anno-
tators to manually gather and compile preliminary
questions and answers from these sources. The
data then underwent a three-fold modification and
review process: (1) Ethical Considerations: We
categorized our data source into reference materi-
als (Sources 1, 2, and 4) and examinations (Source
3). The reference materials were manually adapted
to create new questions and answers. Meanwhile,
all materials are cited appropriately in Appendix
A. The examination data, available freely online,
were also included. (2) Data Contamination: We
aimed to strike a balance between maintaining the
authority of the data sources and minimizing data
contamination. With the awareness that official
examinations might be inadvertently captured and
utilized in training LLMs, these were adapted by
experts to retain the examinations’ core focus while
altering the content to some extent. (3) Coverage
and Accuracy: We adhered strictly to our design
principles to ensure the dataset’s diversity and accu-
racy. A 5% random sample of the data underwent
a quality check, with any found inaccuracies neces-
sitating rework until achieving 100% accuracy.
Further details on the concepts and data sources
for each subject are provided in Appendix A.
3.3
Evaluation
Accuracy is the primary metric for our evaluation.
The ground-truth labels of the development set are
public, while the labels of the test set remain con-
fidential to avoid their unintended inclusion in the
pre-training corpora. Participants can email to re-
quest access to the AC-EVAL under a confidential
agreement. Once access is granted, they are encour-
aged to submit their model predictions via email
for evaluation. Results will be provided within one
working day and displayed on a public leaderboard
on GitHub. This streamlined process ensures se-
cure and fair evaluation.
4
Experiment
4.1
Setup
For evaluation of the AC-EVAL benchmark, we
assess LLMs in both zero-shot and few-shot set-
tings, with the few-shot samples drawn from the
development set. To extract the answer choices
from the models’ responses, We employ regular ex-
pressions followed by manual verification to ensure
successful retrieval in nearly all cases.
We report the results for both answer-only (AO)
and chain-of-thought (COT) (Wei et al., 2022b;
Dong et al., 2022; Zhang et al., 2022) settings in
zero- and few-shot scenarios. For zero-shot AO
setting, we craft prompts in the format: "以下是
中国古代[主题]领域的单项选择题，请直接
给出正确答案对应的选项。(The following is
a multiple-choice question in the field of Ancient
Chinese [subject]. Please directly provide the op-
4

--- Page 5 ---

题目：中国美术史上至今发现最古老的装饰品是什么？
Question: Which is the oldest ornament found so far in the history of Chinese art?
A.玉石装饰品(Jade Ornament)
B.骨头装饰品(Bone Ornament)
C.石墨装饰品(Graphite Ornament)
D.贝壳装饰品(Shell Ornament)
答案：(Answer: )
以下是中国古代艺术和文化传承领域的单项选择题。在查看这些示例之后，请直接给出接下来一道题目的正
确答案所对应的选项。
The following are multiple-choice questions in the field of Ancient Chinese Art and Cultural Heritage. After reviewing 
these examples, please directly provide the option corresponding to the correct answer for the next question.
...[other examples]
示例1：五代南唐时期著名画家顾闳中的绘画名作是
Example 1: The famous painting masterpiece of Gu Hongzhong, a famous painter in the Southern Tang Dynasty 
during the Five Dynasties, is
A.《女史箴图》(Admonitions of the Instructress to the Court Ladies)
B.《五牛图》(Five Buffaloes)
C.《簪花仕女图》(Ladies with Flowers)
D.《韩熙载夜宴图》(Han Xizai Giving a Night Banquet)
答案：D (Answer: D)
Figure 2: Illustrative few-shot AO prompts from AC-EVAL with corresponding English translations for better
readability.
tion corresponding to the correct answer.)" For the
few-shot AO setting, an example of it prompt is
displayed in Figure 2. For the COT settings, their
prompts are shown in Appendix C.
Generally, few-shot defaults to five-shot. It is
noteworthy that for both the five-shot and five-shot-
COT settings, input lengths sometimes surpass the
maximum token limit of the models. To accom-
modate this, we dynamically adjust the number
of samples to ensure they fit within the models’
context window constraints.
4.2
Models
In our evaluation, we select 17 top-performing
LLMs that demonstrate proficiency in Chinese
language comprehension.
These models repre-
sent a variety of organizations and encompass a
range of parameter sizes. For commercial mod-
els, we evaluate via API calls, including (1) GPT-
4 and GPT-3.5 Turbo (Achiam et al., 2023), (2)
ERNIE-Bot 4.0 and ERNIE-Bot6, (3) GLM-4 and
GLM-3-Turbo (Zeng et al., 2022), (4) Qwen-max
(Bai et al., 2023). For models with open-sourced
parameters, we evaluate (1) LLaMA2-70B (Tou-
vron et al., 2023) (2) Qwen-7B/14B/72B-Chat (Bai
et al., 2023), (3) Yi-6B/34B-Chat7, (4) Baichuan2-
7B/13B-Chat (Baichuan, 2023), (5) ChatGLM3-
6https://cloud.baidu.com/
7https://huggingface.co/01-ai
6B8, and (6) Xunzi-Qwen-Chat9—an LLM that
has been continually pre-trained on ancient Chi-
nese corpora based on the Qwen-7B-Chat archi-
tecture. A detailed description of the evaluated
models, including their architectural details, pre-
training corpora, and versions, is available in Ap-
pendix D. We conduct timely evaluations to capture
the latest performance levels of these models10.
5
Results
In this section, we explore the comparative per-
formance of various models under four distinct
settings: zero-shot AO as discussed in Section 5.1,
few-shot AO in Section 5.2, zero- and few-shot
COT in Section 5.3.
5.1
Zero-shot AO
Given that zero-shot scenarios are among the most
common use cases, understanding model perfor-
mance in this context is crucial. Therefore, we first
report the average accuracy in the zero-shot AO
setting in Table 2, while detailed accuracy break-
downs by subject are provided in Appendix E. Our
comparison analysis focuses on two critical dimen-
sions: model parameter size and task category.
Comparison by model.
For large models:
8https://github.com/THUDM/ChatGLM3
9https://github.com/Xunzi-LLM-of-Chinese-
classics/XunziALLM
10All models were evaluated during 5-10 February 2024.
5

--- Page 6 ---

Model
General Historical
Knowledge
Short Text
Understanding
Long Text
Understanding
Average
GPT-4
66.11
55.11
47.38
56.20
GPT-3.5 Turbo
53.50
43.72
36.94
44.72
ERNIE-Bot 4.0
77.54
68.11
66.42
70.69
ERNIE-Bot
68.81
57.80
51.47
59.36
GLM-4
76.63
66.66
67.70
70.33
GLM-3-Turbo
75.21
60.52
59.77
65.17
Qwen-max
73.77
64.88
63.84
67.50
LLaMA-70B
33.55
36.29
30.72
33.54
Qwen-72B-Chat
71.25
61.48
59.80
64.18
Yi-34B-Chat
72.66
61.33
58.36
64.12
Qwen-14B-Chat
69.51
56.53
57.38
61.14
Baichuan2-13B-Chat
65.57
49.24
35.40
50.07
Qwen-7B-Chat
62.74
48.76
44.97
52.16
Baichuan2-7B-Chat
64.38
46.77
40.33
50.49
Yi-6B-Chat
66.70
47.79
39.49
51.33
ChatGLM3-6B
58.04
43.01
39.73
46.93
Xunzi-Qwen-Chat
60.20
44.31
30.87
45.13
Table 2: Zero-shot AO average accuracy of all models. We report average accuracy over subjects within each
category. “Average” = average over all categories. Models are ranked by model size.
ERNIE-Bot-4.0 and GLM-4 stand out as top-
performing models in ancient Chinese, with ac-
curacies of 70.69% and 70.33%, respectively, fol-
lowed by Qwen-max at 67.50%. Despite primarily
being trained on modern Chinese corpora, these
LLMs show strong generalization abilities to an-
cient Chinese. For models primarily trained on
English corpora, GPT-4 and GPT-3.5 significantly
outperform LLaMA-70B. Considering our bench-
mark is entirely in Chinese, this suggests GPT
models’ superior generalization capabilities over
LLaMA2-70B in handling extensive Chinese con-
tent. Interestingly, GPT series models perform
worse than Chinese LLMs, diverging from con-
clusions drawn from previous benchmarks in the
Chinese domain where GPT often ranked first (Li
et al., 2023a; Huang et al., 2023; Xu et al., 2023).
This indicates that ancient Chinese acts as a low-
resource language for English LLMs, highlighting
the significant linguistic differences between an-
cient and modern Chinese. This observation also
underscores the importance of our benchmark from
another perspective.
For small models: The Yi-34B-Chat showcases
remarkable parameter efficiency and performs com-
parably to larger models like Qwen-72B-Chat. This
efficiency can be attributed to their extensive train-
ing on large-scale Chinese corpora and architec-
tural optimizations. Qwen-14B even surpasses the
GPT series and ERNIE-bot, presenting high cost-
effectiveness in ancient Chinese comprehension as
a relatively smaller open-source model. Qwen-7B-
Chat achieves the best performance among models
with less than 10B parameters. Baichuan2-13B-
Chat, compared to Baichuan2-7B-Chat, does not
show performance improvement despite increased
parameters, possibly due to a reduction in focus
on ancient Chinese content in its training corpus.
Xunzi-Qwen-Chat, despite being fine-tuned on an-
cient Chinese texts, shows a decline in performance
compared to Qwen-7B-Chat. This highlights the
trade-off between specialized knowledge and gen-
eral applicability.
Comparison by Task Category. (1) General
Historical Knowledge: Most models score high-
est on this category of tasks, likely because these
tasks focus on the retrieval and understanding of
factual information without necessitating deep tex-
tual analysis and reasoning. (2) Short Text Under-
standing: Compared to long text comprehension,
models generally score higher on short text under-
standing, though still lower than on general histor-
ical knowledge tasks. This may be because short
text understanding still requires models to capture
subtle semantic differences and contextual relation-
ships, albeit with relatively lower complexity. (3)
6

--- Page 7 ---

Model
General Historical
Knowledge
Short Text
Understanding
Long Text
Understanding
Average
GPT-4
65.91 (-0.20)
58.07 (+2.96)
48.36 (+0.98)
57.45 (+1.25)
GPT-3.5 Turbo
53.99 (+0.49)
43.21 (-0.51)
36.40 (-0.54)
44.54 (-0.18)
ERNIE-Bot 4.0
75.69 (-1.85)
69.59 (+1.48)
66.12 (-0.30)
70.47 (-0.22)
ERNIE-Bot
68.81 (+0.00)
57.62 (-0.18)
50.36 (-1.11)
58.93 (-0.43)
GLM-4
74.89 (-1.74)
65.48 (-1.18)
69.07 (+1.37)
69.81 (-0.52)
GLM-3-Turbo
72.99 (-2.22)
59.48 (-1.04)
59.66 (-0.11)
64.04 (-1.13)
Qwen-max
75.29 (+1.52)
65.48 (+0.60)
66.99 (+3.15)
69.25 (+1.75)
Qwen-72B-Chat
71.67 (+0.42)
61.30 (-0.18)
57.07 (-2.73)
63.35 (-0.83)
Yi-34B-Chat
66.62 (-6.04)
52.57 (-8.76)
41.90 (-16.46)
53.70 (-10.42)
Qwen-14B-Chat
70.60 (+1.09)
53.73 (-2.80)
45.91 (-11.47)
56.75 (-4.39)
Baichuan2-13B-Chat
63.75 (-1.82)
45.86 (-3.38)
32.74 (-2.66)
47.45 (-2.62)
Qwen-7B-Chat
61.42 (-1.32)
45.98 (-2.78)
30.78 (-14.19)
46.06 (-6.10)
Baichuan2-7B-Chat
63.37 (-1.01)
45.91 (-0.86)
39.94 (-0.39)
49.74 (-0.75)
Yi-6B-Chat
55.76 (-10.94)
35.97 (-11.82)
28.48 (-11.01)
40.07 (-11.26)
ChatGLM3-6B
55.74 (-2.30)
42.92 (-0.09)
38.45 (-1.28)
45.71 (-1.22)
Xunzi-Qwen-Chat
51.30 (-8.90)
41.25 (-3.06)
29.84 (-1.03)
40.80 (-4.33)
Table 3: Few-shot AO average accuracy of all models. We report average accuracy over subjects within each
category. "Average" = average over all categories. The values in parentheses show the relative change compared to
the zero-shot AO scenario.
Long Text Comprehension: All models generally
score lower on long text comprehension than on
other tasks, indicating it as a challenging task that
requires advanced understanding, reasoning, and
synthesis capabilities.
5.2
Few-shot AO
Table 3 presents the results for the few-shot AO
setting, alongside a comparison with the zero-shot
AO setting.
For large models, only GPT-4 and Qwen have
a 1-2% improvement in this setting, while others
slightly declined, diverging from previous Chinese
benchmarks where few-shot usually excelled over
zero-shot (Huang et al., 2023). We attribute this
discrepancy primarily to the task specificity. Pre-
vious benchmarks often encompassed a broader
range of subjects and task categories, including sci-
entific, technological, and coding tasks. In such
tasks, few-shot learning effectively aids models
in capturing underlying patterns, thereby enhanc-
ing adaptability and generalization. However, our
tasks focus on a broad spectrum of fragmented
knowledge and require a deep understanding of
ancient Chinese, including its cultural, historical
backgrounds, and linguistic structures, leading to
a unique challenge where few-shot learning might
not provide the same level of benefit. Instead, the
specificity and complexity of ancient Chinese tasks
can result in the introduction of noise or irrelevant
information through few-shot examples, potentially
hindering model performance rather than enhanc-
ing it.
For small models, the decline in performance is
more pronounced. The Yi-series models, although
performing comparably to large models in the zero-
shot AO scenario, show the most significant drop in
the few-shot setting, with a performance decrease
of 10%. This aligns with conclusions from some
previous studies (Li et al., 2023a), suggesting that
for smaller models, few-shot learning may intro-
duce too much irrelevant content, potentially lead-
ing to information interference. In such instances,
models might struggle to extract useful knowledge
or patterns from a few samples, as the additional in-
formation introduced may not be entirely relevant
to the task, thereby diluting the model’s focus.
From this analysis, we conclude that despite
the task specificity causing few-shot learning to
sometimes act as interference, large models pos-
sess stronger language understanding capabilities
and higher stability in processing distracting in-
formation, even achieving improvements on some
tasks. However, smaller models struggle due to
insufficient parameters to effectively encode and
utilize contextual information.
7

--- Page 8 ---

Figure 3: Average accuracy for each category in various
settings with different model sizes. Here, we have omit-
ted the category names and shot types for brevity.
5.3
Chain-of-thought
As shown in Figure 3, we conduct a series of exper-
iments to explore the impact of COT on LLMs of
varying parameter sizes. Our experimental setup in-
cludes two scenarios: zero-shot COT and few-shot
COT (prompts are detailed in Appendix C). To fa-
cilitate a nuanced comparison, we select the Qwen
series, encompassing four different sizes: 7B, 14B,
72B, and the non-public Qwen-max. Given that
few-shot performance does not surpass zero-shot
on AC-EVAL, our analysis primarily contrasts the
two COT formats against the zero-shot AO sce-
nario.
Zero-shot COT vs. Zero-shot AO: In zero-shot
COT, prompts are adjusted to encourage stepwise
analysis. This method particularly benefits large
models like Qwen-max and Qwen-72B-Chat in
historical knowledge and short text understanding
tasks but shows a decrease in long text comprehen-
sion. We attribute this to the increased reasoning
steps needed for long text understanding in large
models, where any small errors can accumulate,
negatively impacting the final answer’s accuracy.
As model size decreases, a downward trend in
performance is evident across all tasks in the zero-
shot COT setting. This decline is likely due to the
COT method’s demand for models to understand
the question, generate intermediate reasoning steps,
and ultimately formulate an answer. This process,
more complex than direct answer generation, re-
quires robust semantic understanding and logical
reasoning capabilities. With reduced model param-
eters, the capability of models to perform these
functions weakens, leading to diminished perfor-
mance.
Few-shot COT vs. Zero-shot AO/COT: Few-
shot COT underperforms in comparison to zero-
shot settings in both AO and COT across all param-
eter sizes. This aligns with our above observation
that few-shot learning generally offers less benefit
in our benchmark, which demands a broad under-
standing of fragmented knowledge and deep com-
prehension of ancient Chinese, including its cul-
tural, historical backgrounds, and linguistic struc-
tures. The unique challenges posed by these re-
quirements suggest that even structured COT, when
combined with few-shot examples, may be per-
ceived as informational noise, thereby impeding
the model’s ultimate reasoning capability.
Through this analysis, it is evident that while
COT reasoning can enhance model performance in
certain contexts, the effectiveness of this approach
is contingent upon the model’s capacity for com-
plex information processing and logical deduction.
The decline in performance with reduced model
size and the limited impact of few-shot learning
highlight the intricate balance required between
model abilities, task specificity, and the introduced
format of COT.
6
Conclusion
We introduce AC-EVAL, a benchmark designed
to evaluate LLMs’ proficiency in ancient Chinese,
addressing a gap by covering historical knowledge
and language understanding extensively. Our ex-
periments reveal significant improvement areas for
existing LLMs. We identify critical factors influ-
encing LLM performance and suggest practical
directions for enhancing these models. AC-EVAL
aims to advance LLM application in ancient Chi-
nese education, offering a valuable tool for assess-
ing and developing Chinese LLMs.
8

--- Page 9 ---

7
Limitations
While our study introduces the AC-EVAL bench-
mark as a robust tool for evaluating LLMs in the
domain of ancient Chinese, it is imperative to ac-
knowledge several limitations that accompany our
research:
Absence of Human Baseline: The lack of a hu-
man comparative standard impedes the evaluation
of LLMs’ depth of understanding, cultural acuity,
and contextual sensitivity relative to the insights
provided by scholars specializing in ancient Chi-
nese literature. Consequently, while the AC-EVAL
benchmark may offer quantitative evaluations of
LLM proficiency, it might not capture the qualita-
tive dimensions of linguistic and cultural compre-
hension that are crucial in the analysis of ancient
Chinese texts.
Focus on Multiple-Choice Questions: The cur-
rent iteration of AC-EVAL primarily utilizes a
multiple-choice format to assess LLMs. This ap-
proach, while effective in certain assessments, does
not measure the generative capabilities of LLMs.
For example, poetry generation (Chen et al., 2019;
Zhipeng et al., 2019). As a result, our benchmark
may not fully capture the models’ ability to pro-
duce coherent and contextually relevant responses
in an open-ended format.
In light of these limitations, future work will
aim to incorporate human evaluation and expand
the benchmark to include open-ended and gener-
ative tasks, thereby enhancing the comprehensive
assessment of models’ capabilities.
Acknowledgments
This work is supported by the National Natural Sci-
ence Foundations of China under Grant (61972047,
62372060), and the NSFC-General Technology Ba-
sic Research Joint Funds under Grant (U1936220).
References
Josh Achiam, Steven Adler, Sandhini Agarwal, Lama
Ahmad, Ilge Akkaya, Florencia Leoni Aleman,
Diogo Almeida, Janko Altenschmidt, Sam Altman,
Shyamal Anadkat, et al. 2023. Gpt-4 technical report.
arXiv preprint arXiv:2303.08774.
Jinze Bai, Shuai Bai, Yunfei Chu, Zeyu Cui, Kai Dang,
Xiaodong Deng, Yang Fan, Wenbin Ge, Yu Han, Fei
Huang, et al. 2023. Qwen technical report. arXiv
preprint arXiv:2309.16609.
Baichuan. 2023. Baichuan 2: Open large-scale lan-
guage models. arXiv preprint arXiv:2309.10305.
Yupeng Chang, Xu Wang, Jindong Wang, Yuan Wu,
Linyi Yang, Kaijie Zhu, Hao Chen, Xiaoyuan Yi,
Cunxiang Wang, Yidong Wang, et al. 2023. A sur-
vey on evaluation of large language models. ACM
Transactions on Intelligent Systems and Technology.
Huimin Chen, Xiaoyuan Yi, Maosong Sun, Wenhao Li,
Cheng Yang, and Zhipeng Guo. 2019. Sentiment-
controllable chinese poetry generation. In Proceed-
ings of the Twenty-Eighth International Joint Confer-
ence on Artificial Intelligence, pages 4925–4931.
OpenCompass Contributors. 2023.
Opencompass:
A universal evaluation platform for foundation
models.
https://github.com/open-compass/
opencompass.
Qingxiu Dong, Lei Li, Damai Dai, Ce Zheng, Zhiy-
ong Wu, Baobao Chang, Xu Sun, Jingjing Xu, and
Zhifang Sui. 2022. A survey for in-context learning.
arXiv preprint arXiv:2301.00234.
Geyang Guo, Jiarong Yang, Fengyuan Lu, Jiaxin Qin,
Tianyi Tang, and Wayne Xin Zhao. 2023. Towards
effective ancient chinese translation: Dataset, model,
and evaluation. In CCF International Conference on
Natural Language Processing and Chinese Comput-
ing, pages 416–427. Springer.
Dan Hendrycks, Collin Burns, Steven Basart, Andy Zou,
Mantas Mazeika, Dawn Song, and Jacob Steinhardt.
2021. Measuring massive multitask language under-
standing. In International Conference on Learning
Representations.
Yuzhen Huang, Yuzhuo Bai, Zhihao Zhu, Junlei
Zhang, Jinghan Zhang, Tangjun Su, Junteng Liu,
Chuancheng Lv, Yikai Zhang, Jiayi Lei, Yao Fu,
Maosong Sun, and Junxian He. 2023. C-eval: A
multi-level multi-discipline chinese evaluation suite
for foundation models. In Advances in Neural Infor-
mation Processing Systems.
Zijing Ji, Yuxin Shen, Yining Sun, Tian Yu, and Xin
Wang. 2021. C-clue: a benchmark of classical chi-
nese based on a crowdsourcing system for knowl-
edge graph construction. In Knowledge Graph and
Semantic Computing: Knowledge Graph Empowers
New Infrastructure Construction: 6th China Confer-
ence, CCKS 2021, Guangzhou, China, November 4-7,
2021, Proceedings 6, pages 295–301. Springer.
Haonan Li, Yixuan Zhang, Fajri Koto, Yifei Yang, Hai
Zhao, Yeyun Gong, Nan Duan, and Timothy Bald-
win. 2023a. Cmmlu: Measuring massive multitask
language understanding in chinese. arXiv preprint
arXiv:2306.09212.
Yanyang Li, Jianqiao Zhao, Duo Zheng, Zi-Yuan Hu,
Zhi Chen, Xiaohui Su, Yongfeng Huang, Shijia
Huang, Dahua Lin, Michael R. Lyu, and Liwei Wang.
2023b. Cleva: Chinese language models evaluation
platform. arXiv preprint arXiv:2308.04813.
Yuqing Li, Yuxin Zhang, Bin Wu, Ji-Rong Wen, Ruihua
Song, and Ting Bai. 2022. A multi-modal knowledge
9

--- Page 10 ---

graph for classical Chinese poetry. In Findings of the
Association for Computational Linguistics: EMNLP
2022, pages 2318–2326.
Percy Liang, Rishi Bommasani, Tony Lee, Dimitris
Tsipras, Dilara Soylu, Michihiro Yasunaga, Yian
Zhang, Deepak Narayanan, Yuhuai Wu, Ananya Ku-
mar, et al. Holistic evaluation of language models.
Transactions on Machine Learning Research.
Maofu Liu, Junyi Xiang, Xu Xia, and Huijun Hu. 2022.
Contrastive learning between classical and modern
chinese for classical chinese machine reading com-
prehension. ACM Transactions on Asian and Low-
Resource Language Information Processing, 22(2):1–
22.
Yutong Liu, Bin Wu, and Ting Bai. 2020. The construc-
tion and analysis of classical chinese poetry knowl-
edge graph (in Chinese). Journal of Computer Re-
search and Development, 57(6):1252.
Xiaomeng Pan, Hongfei Wang, Teruaki Oka, and
Mamoru Komachi. 2022. Zuo zhuan Ancient Chi-
nese dataset for word sense disambiguation. In Pro-
ceedings of the 2022 Conference of the North Amer-
ican Chapter of the Association for Computational
Linguistics: Human Language Technologies: Student
Research Workshop, pages 129–135.
Yizhan Shao, Tong Shao, Minghao Wang, Peng Wang,
and Jie Gao. 2021. A sentiment and style control-
lable approach for chinese poetry generation. In Pro-
ceedings of the 30th ACM International Conference
on Information & Knowledge Management, page
4784–4788.
Lei Shu, Yiluan Guo, Huiping Wang, Xuetao Zhang, and
Renfen Hu. 2021. The construction and application
of Ancient Chinese corpus with word sense annota-
tion. In Proceedings of the 20th Chinese National
Conference on Computational Linguistics, pages 549–
563.
Aarohi Srivastava, Abhinav Rastogi, Abhishek Rao,
Abu Awal Md Shoeb, Abubakar Abid, Adam Fisch,
Adam R Brown, Adam Santoro, Aditya Gupta, Adrià
Garriga-Alonso, et al. 2023. Beyond the imitation
game: Quantifying and extrapolating the capabili-
ties of language models. Transactions on Machine
Learning Research.
Xuemei Tang and Qi Su. 2022. That slepen al the nyght
with open ye! cross-era sequence segmentation with
switch-memory. In Proceedings of the 60th Annual
Meeting of the Association for Computational Lin-
guistics (Volume 1: Long Papers), pages 7830–7840.
Hugo Touvron, Louis Martin, Kevin Stone, Peter Al-
bert, Amjad Almahairi, Yasmine Babaei, Nikolay
Bashlykov, Soumya Batra, Prajjwal Bhargava, Shruti
Bhosale, et al. 2023.
Llama 2:
Open founda-
tion and fine-tuned chat models.
arXiv preprint
arXiv:2307.09288.
Pengyu Wang and Zhichen Ren. 2022. The uncertainty-
based retrieval framework for Ancient Chinese CWS
and POS. In Proceedings of the Second Workshop on
Language Technologies for Historical and Ancient
Languages, pages 164–168.
Ping Wang, Shitou Zhang, Zuchao Li, and Jingrui Hou.
2023. Enhancing Ancient Chinese understanding
with derived noisy syntax trees. In Proceedings of
the 61st Annual Meeting of the Association for Com-
putational Linguistics (Volume 4: Student Research
Workshop), pages 83–92.
Jason Wei, Yi Tay, Rishi Bommasani, Colin Raffel,
Barret Zoph, Sebastian Borgeaud, Dani Yogatama,
Maarten Bosma, Denny Zhou, Donald Metzler, et al.
2022a. Emergent abilities of large language models.
Transactions on Machine Learning Research.
Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten
Bosma, Fei Xia, Ed Chi, Quoc V Le, Denny Zhou,
et al. 2022b. Chain-of-thought prompting elicits rea-
soning in large language models. Advances in Neural
Information Processing Systems, 35:24824–24837.
Liang Xu, Anqi Li, Lei Zhu, Hang Xue, Changtai Zhu,
Kangkang Zhao, Haonan He, Xuanwei Zhang, Qiyue
Kang, and Zhenzhong Lan. 2023. Superclue: A com-
prehensive chinese large language model benchmark.
arXiv preprint arXiv:2307.15020.
Aohan Zeng, Xiao Liu, Zhengxiao Du, Zihan Wang,
Hanyu Lai, Ming Ding, Zhuoyi Yang, Yifan Xu,
Wendi Zheng, Xiao Xia, et al. 2022. Glm-130b: An
open bilingual pre-trained model. In The Eleventh In-
ternational Conference on Learning Representations.
Hui Zeng. 2023. Measuring massive multitask chinese
understanding. arXiv preprint arXiv:2304.12986.
Hui Zeng, Jingyuan Xue, Meng Hao, Chen Sun, Bin
Ning, and Na Zhang. 2023. Evaluating the generation
capabilities of large chinese language models. arXiv
preprint arXiv:2308.04823.
Zhuosheng Zhang, Aston Zhang, Mu Li, and Alex
Smola. 2022. Automatic chain of thought prompting
in large language models. In The Eleventh Interna-
tional Conference on Learning Representations.
Wayne Xin Zhao, Kun Zhou, Junyi Li, Tianyi Tang,
Xiaolei Wang, Yupeng Hou, Yingqian Min, Beichen
Zhang, Junjie Zhang, Zican Dong, et al. 2023. A
survey of large language models.
arXiv preprint
arXiv:2303.18223.
Guo Zhipeng, Xiaoyuan Yi, Maosong Sun, Wenhao Li,
Cheng Yang, Jiannan Liang, Huimin Chen, Yuhui
Zhang, and Ruoyu Li. 2019.
Jiuge: A human-
machine collaborative Chinese classical poetry gen-
eration system. In Proceedings of the 57th Annual
Meeting of the Association for Computational Lin-
guistics: System Demonstrations, pages 25–30.
10

--- Page 11 ---

Wanjun Zhong, Ruixiang Cui, Yiduo Guo, Yaobo Liang,
Shuai Lu, Yanlin Wang, Amin Saied, Weizhu Chen,
and Nan Duan. 2023. Agieval: A human-centric
benchmark for evaluating foundation models. arXiv
preprint arXiv:2304.06364.
Bo Zhou, Qianglong Chen, Tianyu Wang, Xiaomi
Zhong, and Yin Zhang. 2023. WYWEB: A NLP
evaluation benchmark for classical Chinese. In Find-
ings of the Association for Computational Linguistics:
ACL 2023, pages 3294–3319.
Denny Zhou, Nathanael Schärli, Le Hou, Jason Wei,
Nathan Scales, Xuezhi Wang, Dale Schuurmans,
Claire Cui, Olivier Bousquet, Quoc V Le, et al. 2022.
Least-to-most prompting enables complex reasoning
in large language models. In The Eleventh Interna-
tional Conference on Learning Representations.
A
Details of AC-EVAL
Table 5 provides a comprehensive overview of the
AC-EVAL, detailing the data sources and the spe-
cific concepts addressed within each subject. Table
6 offers insights into the quantitative aspects of the
dataset, including the number of questions per sub-
ject and their average length (accounting for both
the questions and explanations, measured in charac-
ters). Furthermore, Table 4 shows the distribution
of choices across the multiple-choice questions.
Option
C-EVAL
AC-EVAL
A
22.9%
26.2%
B
26.0%
26.5%
C
26.4%
23.6%
D
24.7%
23.7%
Table 4: Distribution of Answers
B
Details of Annotation
Figure 4 details the specific requirements for data
annotation. All our annotators are Chinese under-
graduate students and experts in Chinese linguis-
tics, and they are compensated at a rate that meets
market standards.
C
Prompts for Evaluation
Figures 5 and 6 display the chain-of-thought evalu-
ation prompts used in the zero-shot and few-shot
settings, respectively.
D
Details of the LLMs being evaluated
We provide a detailed description of the Large Lan-
guage Models (LLMs) that were rigorously evalu-
ated during the period of 5-10 February 2024, en-
suring the assessment of the latest model versions
prior to submission.
GPT (Achiam et al., 2023) series models, devel-
oped by OpenAI, designed to be more aligned with
human-like interaction, exhibiting helpful, safe,
and truthful behavior as enhanced by Reinforce-
ment Learning from Human Feedback (RLHF).
GPT-4, with its ability to process images, PDFs,
and other file types, underwent a comprehensive
post-training alignment process. We evaluate the
versions of gpt-3.5-turbo-0125 and gpt-4-0125-
preview.
ERNIE-Bot is an industrial-grade, knowledge-
enhanced LLM developed by Baidu. The 4.0 ver-
sion represents a significant upgrade in understand-
ing, generation, logic, and memory capabilities
over its predecessors, supporting extensive input
and output lengths (5K input + 2K output). Our
evaluation included both ERNIE-Bot and ERNIE-
Bot 4.0.
GLM (Zeng et al., 2022) series, developed by
Zhipu AI and Tsinghua University, are bidirec-
tional dense models excelling in bilingual language
processing. ChatGLM, a derivative of GLM, tar-
gets Chinese QA and dialogue tasks with enhanced
fine-tuning and feedback. We evaluate ChatGLM3-
6B and the commercial GLM-3-Turbo and GLM-4.
Qwen (Bai et al., 2023), developed by Alibaba,
is trained on a vast corpus including 3 trillion to-
kens of texts and codes. The chat variants of Qwen
have been refined through RLHF to better align
with human preferences. We conduct a compre-
hensive evaluation of the Qwen series, covering
multiple versions with varying parameter sizes, in-
cluding Qwen-7B/14B/72B-Chat and Qwen-max.
LLaMA2 (Touvron et al., 2023), developed and
open-sourced by Meta AI, excels in encoding, in-
ference, and knowledge application. It incorpo-
rates several enhancements over the vanilla Trans-
former architecture employed by preceding LLMs,
optimizing for greater training efficiency. In our
experiment, we evaluate the performance of the
LLaMA2-70B version.
Yi series models by 01.AI are open-source bilin-
gual models trained from scratch on a 3T multilin-
gual corpus, featuring an extended context window
of up to 200K tokens. We utilize the Yi-6B-Chat
and Yi-34B-Chat versions, which support up to
32K tokens for context in inferences.
Baichuan2 (Baichuan, 2023) is developed by
Baichuan Intelligence Inc., trained on a 2.6 trillion
token high-quality corpus and supporting multiple
11

--- Page 12 ---

Subject: Social Customs
Specified Data sources: Relevant Books
寒食节最初禁火的时间长达多久？
Question:  
Options:   A.一天
B.三天
C.一周
D.一月
Answer:   D
Reference：《中国传统节日习俗》作者：赵红,祁斌
Data Format: Excel
If has an explanation? For yes, explain.
Yes     No
Question id:   1
汉代以前寒食节禁火的时间较长,以一月
为限。汉代确定寒食节为清明前三天。
Purpose: To collect and annotate data on social
customs
and
daily
life
in ancient
China
from
specified data sources, including but not limited to
clan rites, marriage and funeral customs, dietary
habits,
festival
celebrations,
clothing,
residential
architecture, and modes of transportation.
Principle:
Ensure
that
the
data
spans
various
historical dynasties and covers a wide range of
customs and aspects of daily life for comprehensive
analysis and research.
Compensation: 2 CNY per entry.
Figure 4: Illustration of the Annotation Process: An Example of Social Customs Data Annotation
languages including Chinese, English and others.
The versions evaluated are Baichuan2-7B-Chat and
Baichuan2-13B-Chat.
Xunzi is a model collaboratively released by
Nanjing Agricultural University and the Zhonghua
Book Company. It is fine-tuned on classical Chi-
nese corpora such as the Siku Quanshu, based on
foundations from Qwen, Baichuan, and GLM. We
evaluate the Xunzi-Qwen-Chat, a model trained
from Qwen-7B-Chat.
E
Breakdown of Model Performance
Table 7 provides a detailed accuracy breakdown
by subject for four representative models under
AO settings in both zero- and few-shot scenarios,
respectively. Comprehensive results for all models
are made available on GitHub.
12

--- Page 13 ---

Subject
Data Source
Concepts
Historical Facts
Official history exams
Historical facts, covering political,
economic, and military developments
across different periods.
Geography
10% from mock exams and
90% from ancient place
names knowledge database
Administrative divisions, historical
boundaries,changes in place
names over time.
Social Customs
Relevant Books , e.g.,
Customs of the Qing Dynasty.
Changes in clothing, food, housing,
transportation, traditional festivals,
weddings and funerals, family etiquette,
public customs, business practices,
entertainment customs over time.
Art and Cultural Heritage
Mock exams and relevant books,
e.g., History of Chinese Art,
Architecture and Music History
Changes in calligraphy, painting,
architecture, craftsmanship and music
over different periods.
Philosophy and Religion
Mock exams and relevant books
e.g., History of Chinese philosophy.
Changes in the content of Taoism,
Confucianism, Buddhism, etc., and
their rise and decline over time.
Lexical Pragmatic Analysis
Compiled by linguistics experts
Flexible usage of parts of speech
and figures of speech.
Allusions and Idioms
Official and mock exam questions
Allusions and idioms and the cultural
meaning behind them.
Word Sense Disambiguation
Word Sense Disambiguation
Dataset (Shu et al., 2021)
Explanation of word meaning in
a given text.
Translation
Classical-Modern Chinese
translation dataset11
Overall understanding of the
semantics and syntax of sentences.
Event Extraction
GuwenEE12
Identifying basic facts and information
in short texts, such as time, location,
characters, event types, etc.
Sentence Pauses
Siku Quanshu
Make pauses in reading unpunctuated
ancient writings.
Summarization and Analysis
Official and mock exams
Overall understanding, analysis, and
reasoning for classical Chinese texts
Poetry Appreciation
Official and mock exams
Analysis of imagery, style, sentiment
in classical Chinese poetry
Table 5: Data Sources and Concepts for All Subjects.
Subject
Test
Dev
# Questions
Len. of Q
# Questions
Len. of Q
Len. of E
Historical Facts
199
157.1
5
138.0
200.2
Geography
197
33.8
5
32.8
33.6
Social Customs
202
48.5
5
48.6
65.0
Art and Cultural Heritage
195
35.8
5
32.4
56.8
Philosophy and Religion
196
39.2
5
48.0
77.4
Lexical Pragmatic Analysis
198
62.5
5
69.6
75.4
Allusions and Idioms
206
191.2
5
79.6
132.4
Word Sense Disambiguation
402
176.6
5
163.2
91.4
Translation
199
409.1
5
315.0
79.4
Event Extraction
185
238.8
5
150.4
109.0
Sentence Pauses
202
390.2
5
404.2
294.2
Summarization and Analysis
598
880.5
5
856.0
341.4
Poetry Appreciation
201
339.4
5
371.8
109.0
Table 6: Quantitative Statistics for All Subjects.
13

--- Page 14 ---

题目：中国美术史上至今发现最古老的装饰品是什么？
Question: Which is the oldest ornament found so far in the history of Chinese art?
A.玉石装饰品(Jade Ornament)
B.骨头装饰品(Bone Ornament)
C.石墨装饰品(Graphite Ornament)
D.贝壳装饰品(Shell Ornament)
答案：(Answer: )
以下是中国古代艺术和文化传承领域的单项选择题，请逐步分析并给出正确答案对应的选项。
The following is a multiple-choice question in the field of Ancient Chinese Art and Cultural Heritage. 
Please analyze step by step and provide the option corresponding to the correct answer.
Figure 5: Illustrative zero-shot COT prompts from AC-EVAL with corresponding English translations for better
readability.
题目：中国美术史上至今发现最古老的装饰品是什么？
Question: Which is the oldest ornament found so far in the history of Chinese art?
A.玉石装饰品(Jade Ornament)
B.骨头装饰品(Bone Ornament)
C.石墨装饰品(Graphite Ornament)
D.贝壳装饰品(Shell Ornament)
答案：(Answer: )
以下是中国古代艺术和文化传承领域的单项选择题。在查看这些示例之后，请逐步分析接下来一道题目并给
出正确答案所对应的选项。
The following are multiple-choice questions in the field of Ancient Chinese Art and Cultural Heritage. After reviewing 
these examples, please  analyze the next question step by step and provide the option corresponding to the correct 
answer.
...[other examples]
示例1：五代南唐时期著名画家顾闳中的绘画名作是
Example 1: The famous painting masterpiece of Gu Hongzhong, a famous painter in the Southern Tang Dynasty 
during the Five Dynasties, is
A.《女史箴图》(Admonitions of the Instructress to the Court Ladies)
B.《五牛图》(Five Buffaloes)
C.《簪花仕女图》(Ladies with Flowers)
D.《韩熙载夜宴图》(Han Xizai Giving a Night Banquet)
答案：
让我们逐步分析。顾闳中的绘画名作是《韩熙载夜宴图》。《五牛图》是韩滉的作品，《簪花仕女图》
是周昉的作品，《女史箴图》是顾恺之的作品。
所以答案是D。
Answer:
Let‘s analyze step by step. The famous painting by Gu Hongzhong is 'Han Xizai Giving a Night Banquet.' 'Five 
Buffaloes' is a work by Han Huang, 'Ladies with Flowers' is by Zhou Fang, and 'Admonitions of the Instructress 
to the Court Ladies' is by Gu Kaizhi.
Therefore, the answer is D.
Figure 6: Illustrative few-shot COT prompts from AC-EVAL with corresponding English translations for better
readability.
14

--- Page 15 ---

Subject
ERNIE-Bot 4.0
GLM-4
Yi-34B-Chat
Qwen-7B-Chat
Historical Facts
78.39/76.76
78.89/84.42
75.88/58.29
61.81/61.31
Geography
78.17/74.11
75.13/75.13
71.57/75.63
66.50/62.44
Social Customs
79.21/78.22
77.23/75.74
76.73/70.79
70.79/71.29
Art and Cultural Heritage
74.87/72.82
76.92/75.90
70.26/68.21
59.49/61.03
Philosophy and Religion
77.04/76.53
75.00/63.27
68.88/60.20
55.10/51.02
Lexical Pragmatics Analysis
78.22/83.17
75.25/79.70
77.72/57.43
44.55/27.23
Allusions and Idioms
66.67/70.20
58.59/59.60
48.48/44.95
33.84/32.83
Word Sense Disambiguation
67.96/70.39
69.90/68.93
70.39/64.08
59.71/52.43
Translation
56.22/56.22
59.45/52.49
49.50/35.82
39.80/36.57
Event Extraction
71.86/74.37
71.86/72.86
65.33/47.74
47.74/43.22
Sentence Pauses
56.86/52.01
59.20/59.36
42.64/32.44
37.63/31.77
Summarization and Analysis
64.18/63.18
68.66/68.16
54.73/35.82
52.74/33.33
Poetry Appreciation
77.84/76.76
73.51/73.51
72.97/70.27
62.70/64.86
Table 7: Accuracy per subject in the answer-only setting: a comparison of zero-shot (left) and few-shot (right)
performance.
15

```
