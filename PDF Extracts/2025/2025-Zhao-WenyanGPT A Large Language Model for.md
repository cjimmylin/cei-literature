---
title: "2025-Zhao-WenyanGPT A Large Language Model for - PDF Extract"
source_pdf: "2025-Zhao-WenyanGPT A Large Language Model for.pdf"
pages: 12
extracted_at: "2026-02-13T09:15:44.182940"
---

# PDF Extract: 2025-Zhao-WenyanGPT A Large Language Model for

**Source PDF:** 2025-Zhao-WenyanGPT A Large Language Model for.pdf
**Total Pages:** 12

---

## Content

```
--- Page 1 ---

WenyanGPT: A Large Language Model for Classical Chinese Tasks
Xinyu Yao1, Mengdi Wang1, Bo Chen1,2, Xiaobing Zhao1,2
1Minzu University of China,
2National Language Resources Monitoring & Research Center of Languages
chenbomuc@muc.edu.cn
Abstract
Classical Chinese, as the core carrier of Chi-
nese culture, plays a crucial role in the inher-
itance and study of ancient literature. How-
ever, existing natural language processing mod-
els primarily optimize for Modern Chinese,
resulting in inadequate performance on Clas-
sical Chinese.
This paper presents a com-
prehensive solution for Classical Chinese lan-
guage processing. By continuing pre-training
and instruction fine-tuning on the LLaMA3-
8B-Chinese model, we construct a large lan-
guage model, WenyanGPT1, which is specifi-
cally designed for Classical Chinese tasks. Ad-
ditionally, we develop an evaluation bench-
mark dataset, WenyanBENCH2. Experimental
results on WenyanBENCH demonstrate that
WenyanGPT significantly outperforms current
advanced LLMs in various Classical Chinese
tasks.
We make the model’s training data,
instruction fine-tuning data3, and evaluation
benchmark dataset publicly available to pro-
mote further research and development in the
field of Classical Chinese processing.
1
Introduction
Classical Chinese is an important component of
Chinese culture, with a long history and profound
cultural heritage. It is essential for understanding
traditional Chinese culture. With the rapid devel-
opment of artificial intelligence technology, intel-
ligent processing of ancient Chinese texts offers a
new solution for the preservation and inheritance of
Classical Chinese. Modern technologies, such as
digitalization and natural language processing, can
efficiently preserve and spread traditional culture
while fostering deeper and more innovative aca-
demic research. Maximizing the potential of AI in
processing Classical Chinese texts has become an
1https://huggingface.co/Wenyanmuc/WenyanGPT
2https://github.com/Wenyanmuc/WenyanBENCH
3https://github.com/Wenyanmuc/WenyanGPT
Translation
问：将这段古汉语文本翻译成现代汉语：古之学者必有师。
答：古代求学的人必定有老师。
Question: Translating this ancient Chinese text into modern Chinese:  古之学者必有
师。
Answer: 古代求学的人必定有老师。
Punctuation
问：请给这段古汉语文本添加标点符号：汝忆否四五年前某夕吾尝语曰与使吾
先死也无宁汝先吾而死
答：汝忆否？四五年前某夕，吾尝语曰：“与使吾先死也，无宁汝先吾而死。”
Question: Please add punctuation marks to this ancient Chinese text: 汝忆否四五年
前某夕吾尝语曰与使吾先死也无宁汝先吾而死
Answer: 汝忆否？四五年前某夕，吾尝语曰：“与使吾先死也，无宁汝先吾而
死。”
NER
问：识别古汉语文本中的人物、地名、时间、官职名等实体：二十三年，罢宣
慰司，立辽阳行省，以亦力撒合为参知政事。
答：'人物'： ['亦力撒合']， '地点'： []， '时间'： ['二十三年']， '官职'： ['宣慰司
'， '参知政事']
Question: Identify entities such as characters, place, time, and official positions in 
ancient Chinese texts: 二十三年，罢宣慰司，立辽阳行省，以亦力撒合为参知政
事。
Answer: 'characters'： ['亦力撒合']，  'place'： []， 'time'： ['二十三年']， 'official 
positions'： ['宣慰司'， '参知政事']
Figure 1: Examples of tasks from WenyanGPT. The
model demonstrates advanced knowledge in Classical
Chinese and shows strong performance in both Classical
Chinese understanding and generation tasks.
urgent need for cultural inheritance and academic
development.
Early research in Classical Chinese language
processing focused on tasks such as punctuation,
word segmentation, part-of-speech tagging, named
entity recognition and translation. These tasks ini-
tially relied on traditional machine learning meth-
ods, such as Hidden Markov Models (HMMs) for
part-of-speech tagging (Huang et al., 2002), Con-
ditional Random Fields (CRFs) for punctuation
(Huang et al., 2010) and named entity recogni-
tion (Yuan et al., 2019; Li, 2018). In deep learn-
ing, RNNs, LSTMs, GRUs, and Attention mecha-
nisms have been applied to various tasks, including
couplet generation and classical poetry generation
(Yan et al., 2016; Yi et al., 2017), punctuation and
part-of-speech tagging using BiLSTM-CRF mod-
els (Wang et al., 2019; Cheng et al., 2020; Zhang
et al., 2023b; Chang et al., 2024). As Transformer
architectures emerged (Vaswani et al., 2017), stud-
ies began using large-scale parallel corpora to train
models for translating Classical Chinese into Mod-
ern Chinese (Liu et al., 2018) and for generating
1
arXiv:2504.20609v1  [cs.CL]  29 Apr 2025

--- Page 2 ---

classical poetry (Huang et al., 2020). The introduc-
tion of pre-trained models including BERT (Ken-
ton and Toutanova, 2019) and GPT (Radford and
Narasimhan, 2018) provided new opportunities for
intelligent Classical Chinese processing. Some re-
search integrated ancient Chinese texts into the
training data of general pre-trained models, improv-
ing the processing performance of Classical Chi-
nese compared to typical pre-trained models (Tian
et al., 2020; Wang et al., 2022, 2023a; Liu et al.,
2023a). Other studies used Classical Chinese cor-
pus to continue pre-training and fine-tuning large
language models, aiming to build conversational
models for Classical Chinese (Zhang et al., 2024;
Yang et al., 2024b; Cao et al., 2023, 2024).
However, challenges remain in Classical Chi-
nese processing.
Different tasks require train-
ing specialized models, and no effective univer-
sal model exists. Additionally, there is a lack of
standardized evaluation benchmarks in this field,
with existing evaluation tasks, datasets, and metrics
being inconsistent, making it difficult to perform
cross-task comparisons and systematic assessments
of model performance.
To
address
these
issues,
we
propose
WenyanGPT,
a
large
language
model
for
Classical Chinese. Some examples of WenyanGPT
are shown in Figure 1.
We also construct the
largest available pre-training corpus for continued
pre-training, enhancing the model’s domain adapt-
ability.
Additionally, we propose a framework
for generating domain-specific instruction data
for supervised fine-tuning in the development of
WenyanGPT. To promote research in the intelligent
processing of Classical Chinese, we build the
WenyanBENCH evaluation dataset and conduct
extensive experiments for detailed analysis. The
main contributions are as follows:
• We propose WenyanGPT, a large language
model focused on Classical Chinese.
It
demonstrates superior performance and wide
applicability in tasks such as punctuation, part-
of-speech tagging, translation, etc.
• We release pre-training and instruction fine-
tuning datasets, along with a novel method
for constructing domain-specific fine-tuning
data, providing valuable resources for future
research.
• We introduce WenyanBENCH, an eval-
uation benchmark for Classical Chinese
tasks, with extensive experiments verifying
WenyanGPT’s leading performance across
multiple tasks.
2
Related Work
2.1
PLMs
In 2017, Google introduced a new neural network
architecture, Transformer. It utilizes self-attention
mechanisms to better handle long-distance depen-
dencies and significantly improves training effi-
ciency through parallel computation. Based on
Transformer, various LLMs have been proposed.
BERT employs an encoder-only Transformer archi-
tecture and is pre-trained using masked language
modeling and next sentence prediction tasks. The
GPT series, on the other hand, uses a decoder-only
Transformer architecture and an autoregressive lan-
guage model (ALM). Over the course of the GPT
series, the model size has steadily increased, from
the original GPT to subsequent iterations, includ-
ing GPT-2 (Radford et al., 2019), GPT-3 (Brown
et al., 2020), and GPT-4 (Achiam et al., 2023), with
continuous improvements in performance. PaLM
(Chowdhery et al., 2023) uses the standard Trans-
former architecture in a decoder-only model with a
modified SwiGLU activation function. This model,
with 540 billion parameters, achieved human-level
performance in 1-shot learning on the BIG-bench
(Srivastava et al., 2023) dataset. In 2023, Meta
AI released the LLaMA model (Touvron et al.,
2023). This model also follows a decoder-only
Transformer architecture and excels in various nat-
ural language processing tasks after large-scale
training. In 2024, LLaMA 3 (Dubey et al., 2024)
was released, including a pre-trained version with
405 billion parameters and a post-training version,
alongside the LLaMA Guard 3 model for input-
output safety. Pre-trained language models have
seen rapid development, with Transformer-based
models becoming the mainstream technology in
natural language processing (NLP).
2.2
Classical Chinese PLMs
Pre-trained
language
models
have
achieved
widespread success in the field of natural language
processing. However, studies show that general-
domain models often lack specialized knowledge
for tasks in specific domains. Models pre-trained
with domain-specific data tend to perform better
for specialized tasks (Ke et al., 2023; Gupta et al.,
2023; Ibrahim et al., 2024; Taylor et al., 2022;
2

--- Page 3 ---

Classical Chinese Corpus
Domain Instruction 
Data Generation
Instruction fine-
tuning data
Base Model
Pre-trained Model 
Classical Chinese 
LLM
WenyanGPT
Classical Chinese 
Benchmark
WenyanBENCH
Pre-training corpus
continued 
pretraining
fine-tuning
Figure 2: Overall Training Framework of WenyanGPT.
Lehman et al., 2023; Liu et al., 2020).
In the
field of Classical Chinese, several studies have
extended models such as BERT, RoBERTa, and
GPT by incorporating Classical Chinese corpora
for pre-training, resulting in specialized models
like AnchiBERT (Tian et al., 2020), SikuBERT and
SikuRoBERTa (Wang et al., 2022), GujiBERT and
GujiGPT series (Wang et al., 2023a), and SikuGPT
(Liu et al., 2023a). These models show improved
performance over general pre-trained models in
Classical Chinese tasks. Instruction fine-tuning
is another effective strategy. Using Supervised
Fine-Tuning (SFT) can activate LLMs’ ability to
understand and answer questions in a specific do-
main (Liu et al., 2023b; Xiong et al., 2023; Wang
et al., 2023b; Yue et al., 2023; Huang et al., 2023;
Cui et al., 2023; Yang et al., 2023b; Zhang et al.,
2023a; Dan et al., 2023). Classical Chinese LLMs
(Zhang et al., 2024; Yang et al., 2024b; Cao et al.,
2023, 2024) are in the early stages of development.
For example, the "Xunzi4" Classical Chinese large
language model was trained on Classical Chinese-
related corpora based on general models such as
Qwen2.5 (Yang et al., 2024a), Baichuan2 (Yang
et al., 2023a), and GLM-4 (Zeng et al., 2024). It has
shown excellent performance in intelligent tagging,
information extraction, and other tasks. TongGu
(Cao et al., 2024), through two-stage instruction
fine-tuning, is capable of Classical Chinese punc-
tuation, translation, and appreciation tasks. In this
paper, WenyanGPT is fine-tuned on higher-quality
pre-training data and a larger, more diverse instruc-
tion dataset, showing superior and more compre-
hensive task handling capabilities.
3
WenyanGPT
In order to obtain the WenyanGPT Classical Chi-
nese model, we first construct a Classical Chinese
4https://github.com/Xunzi-LLM-of-Chinese-classics/
XunziALLM.
Source
Scale
Source
Scale
Daizhige
5.2G
Poetry-master 323M
wenyanguji.com
1.6G
PoetrySplider
16M
network resource
1.1G
poems-db
660M
TCM-Ancient-Books 322M
core-texts
232M
chinese-novel
294M
sidamingzhi
6.7M
chinese-gushiwen
23M
chtxt-main
88M
Classical-Chinese
208M chinese-poetry 115M
Classical-Modern
853M
guner2023
63M
core-books-main
752M kangxi-master
37M
GuWen-master
2.5M
scripta-sinica
3.7G
Table 1: Sources and Scale of Classical Chinese Pre-
training Corpus.
pre-training corpus and continue pre-training based
on LLaMA3-8B-Chinese (Section 3.1). Then, we
propose a method to construct domain instruction
data (Section 3.2).
In our framework, instruc-
tion generation is manually constructed, guided
by LLMs, and tested to ensure the high quality of
the fine-tuning data. The complete training process
is shown in Figure 2.
3.1
Pre-training
Hyper parameter
Value
per device train batch size
16
gradient accumulation steps
1
learning rate
1.0e-4
num train epochs
1
lr scheduler type
cosine
warmup ratio
0.1
Table 2: Hyper-parameter Settings in Continue Pre-
training.
The corpus used in the pre-training phase
is sourced from authoritative websites such as
Daizhige, Wenyanguji, and various Classical
Chinese-related data collected and organized from
GitHub. The detailed data sources and scale are
shown in Table 1.
We uniformly format and
store data from these different sources, remov-
ing redundant information, errors, special sym-
bols, and invalid characters. As a result, we ob-
tain a clean, large-scale, high-quality Classical Chi-
nese corpus of approximately 16GB. This corpus
covers the Four Books and Five Classics, includ-
ing Confucian classics, historical records, works
of various philosophers, poetry, essays, drama,
novels, miscellanies, and other literary genres.
It also encompasses diverse fields such as local
3

--- Page 4 ---

gazetteers, genealogies, religious texts, agricultural,
law, medicine, astronomy, geography, craft books,
and military texts. The corpus integrates both sim-
plified and traditional Chinese characters, span-
ning from the Pre-Qin period to the Republic of
China, providing rich materials for deep learning
and research on ancient Chinese texts. We select
LLaMA3-8B-Chinese as the base model and use
the bfloat16 data format during training to improve
efficiency. The hyper-parameter settings in pre-
training are shown in Table 2.
3.2
Supervised Fine-Tuning
Based on continued pre-training, we perform super-
vised fine-tuning to better adapt the model to spe-
cific tasks and instructions. We use a high-quality
set of instruction fine-tuning data, which we have
previously collected and organized, to trigger the
knowledge the model acquires during pre-training.
The detailed process for constructing the instruc-
tion fine-tuning data is shown in Figure 3.
Data Selection and Initial Organization.
We
select relevant data from the Classical Chinese cor-
pus, including three major categories: question-
answer pairs, parallel corpora, and tagged corpora.
Parallel corpora are used for translation and in-
terpretation tasks, while tagged corpora support
fine-grained tasks such as punctuation and part-of-
speech tagging. In cases where the corpus lacks
clear question-answer pairs, we generate supple-
mentary data. During the selection phase, we pri-
oritize high-quality data with clear content, stan-
dardized semantics, and task relevance to build the
initial high-quality input-output pairs.
Manual Design of Task Instructions and Model
Expansion.
We design initial task instruction
templates manually based on high-quality input
and output, covering tasks such as Classical Chi-
nese punctuation, and translating Classical Chinese
into Modern Chinese. Then, we use LLMs, such
as GPT and Qwen series to expand the task in-
structions. On the one hand, we generate diverse
instructions from existing ones; on the other hand,
we allow LLMs to perform reverse reasoning from
the existing high-quality input-output pairs to gen-
erate new instructions, ensuring diversity in the
instructions. After the expansion, we conduct an
initial screening of the generated instructions, re-
moving those with unclear or unreasonable seman-
tics, resulting in a seed instruction set.
Task
Data Source
Num
Punctuation
Daizhige
107,3017
Part-of-speech tagging
evahan
9,952
NER
Self-built
29923
Translation
classical-modern
222,700
wenyanguji.com
302,724
Word explanation
gushiwen.com
31,088
Reverse dictionary
chinese-dictionary
39,708
chinese-xinhua
138,810
Total
1,847,922
Table 3: Sources and Scale of Instruction Fine-Tuning
Data.
Hyper parameter
Value
per device train batch size
8
gradient accumulation steps
2
learning rate
1.0e-4
num train epochs
1
lr scheduler type
cosine
warmup ratio
0.1
Table 4: Hyper-parameter Settings in Fine-Tuning.
Testing the Instruction Set and Optimizing Fine-
Tuning Data.
We randomly select high-quality
input-output pairs and combine them with the seed
instruction set to evaluate the model’s adherence
to instructions across different task scenarios. We
analyze the test results to refine the instructional
design and identify the task instructions that pro-
duce higher-quality outputs. Then, we combine the
optimized instruction set with high-quality input-
output pairs to construct fine-tuning data for spe-
cific instructions, providing reliable data support
for subsequent model training.
Generation and Supplementation of Specific
Task Data.
Due to the lack of specific task in-
struction data in the corpus, we manually design
diverse initial instructions and inputs. Then we
use LLMs including Qwen2.5-14B and Qwen2.5-
72B to generate high-quality answers. We remove
low-quality or irrelevant content through manual
selection and automatic quality checks, forming
another portion of the instruction data.
Data Integration and Output Validation.
We
integrate the data generated from the corpus and
the supplementary data from the LLMs to form a
complete instruction dataset. During integration,
we ensure consistency between instructions and
outputs, covering multiple Classical Chinese task
4

--- Page 5 ---

Question-Answer 
Pairs
Classical Chinese Corpus
Parallel corpora
古之学者必有师。
古代求学的人必定有老师。
Tagged Corpus
十三年，
十三年/t ，/w 
high quality pairs
(input, output)
(input, output)
Parts of high quality pairs
Larger models
Artificial design
(instruction,input)
extract
reverse reasoning
expand 
Initial instructions
test instructions
Seed instructions
Seed instruction data
instructions
High quality  instruction
Parts of high quality sft 
data
(instruction, input, output)
outputs
Generated output
filter
filter
filter
merge
Parts of high quality sft 
data
(instruction, input, output)
Final high quality sft 
data
(instruction, input, output)
filter
filter
Figure 3: Instruction Fine-Tuning Data Construction Process.
Task
Num
Punctuation
7,559
Part-of-speech tagging
1,247
NER
3,741
Translation
5,013
Word Explanation
3,931
Reverse Dictionary
4,462
Total
25,953
Table 5: Data Sources and Detailed Statistics of Wenyan-
Bench.
scenarios. Finally, through comprehensive data val-
idation and optimization, we create a high-quality
instruction dataset. In the end, we obtain about
1.85 million instruction fine-tuning data. The de-
tailed data sources and counts are shown in Table
3. We use these data to fine-tune the pre-trained
model. The hyper-parameter settings in fine-tuning
are shown in Table 4.
4
Benchmarking Classical Chinese Tasks
WenyanBench.
In order to evaluate the model’s
performance on Classical Chinese tasks, we devise
a benchmark known as WenyanBench. Wenyan-
Bench shares the same data sources as the instruc-
tion fine-tuning data and has undergone duplicate
data removal, as well as validation by both manual
and LLMs. For quality control, we sample a subset
of the data. The distribution and detailed statistics
of WenyanBench are shown in Table 5.
Tasks.
Our benchmark includes six tasks related
to Classical Chinese. Among them, we subdivide
14 types of punctuation marks in the punctuation
task, divide ancient Chinese word classes into 17
categories in the part-of-speech tagging task, and
define 4 categories for the named entity recognition
task.
Metrics.
For the WenyanBench benchmark, dif-
ferent evaluation metrics are used for different
types of tasks (understanding tasks and generation
tasks). For understanding tasks, evaluation primar-
ily relies on Precision, Recall, and F1-Score. For
generation tasks, BLEU and BERT-Score are used
as evaluation metrics. BLEU measures the N-gram
overlap between generated content and reference
answers, while BERT-Score better captures the se-
mantic similarity between the generated content
and reference answers.
Evaluation Method.
To efficiently assess model
performance, we design a set of scripted tools to
automatically compute BLEU, BERT-Score, and
other metrics. These tools quickly and accurately
quantify model outputs, providing clear feedback
for model optimization. This automated evalua-
tion approach improves evaluation efficiency and
ensures the consistency and comparability of the
results.
5
Experiments
The experiments evaluate WenyanGPT’s perfor-
mance on understanding and generation tasks in
Classical Chinese.
5

--- Page 6 ---

Model
Punctuation
Part-of-speech tagging
NER
P(%) R(%) F1(%) P(%) R(%)
F1(%)
P(%) R(%) F1(%)
Qwen2.5-7B-Instruct
54.34
53.31
53.82
51.25
48.16
49.65
66.05
46.55
54.61
Baichuan2-7B-Chat
51.05
21.03
29.79
47.11
30.97
37.37
35.10
10.58
16.26
GLM-4-9B-Chat
52.39
55.00
53.66
49.90
54.98
52.32
52.19
45.42
48.57
Meta-Llama-3-8B-Instruct 55.05
22.41
31.85
25.73
17.06
20.52
47.50
57.48
52.01
Llama3-8B-Chinese-Chat
45.76
38.07
41.56
21.34
19.34
20.29
46.85
66.69
55.04
Xunzi-Qwen-1.5-7B-Chat
52.08
47.19
49.51
77.54
78.07
77.81
49.79
51.21
50.49
GPT-4o
52.00
50.70
51.34
82.41
81.11
81.75
61.58
76.97
68.42
Deepseek-V3
56.33
61.94
59.01
79.12
79.18
79.15
56.83
79.75
66.36
WenyanGPT
76.84
74.52
75.66
89.66
88.54
89.1
92.14
90.19
91.16
Table 6: Results for understanding tasks (Punctuation, Part-of-speech tagging, Named Entity Recognition) on
WenyanBench. The results underlined represent the second-best model’s F1 score.
0
0.2
0.4
0.6
0.8
1
p
c nr n
r
v w d ns t
y u m a
f
j
q
Part-of-speech tagging
0
0.2
0.4
0.6
0.8
1
，。；：“ 《》）（！＜＞？”
Punctuation
0
0.2
0.4
0.6
0.8
1
characte
rs
place
time
official 
positions
NER
Figure 4: The F1 scores of WenYanGPT for the subcategories of understanding tasks (including Punctuation,
Part-of-speech tagging, and Named Entity Recognition) on WenyanBench.
5.1
Experimental Setup
Baselines.
The baselines include general-domain
and Classical Chinese domain LLMs.
The
general-domainLLMs are Qwen2.5-7B-Instruct,
Baichuan2-7B-Chat,
GLM-4-9B-Chat,
Meta-
Llama-3-8B-Instruct, Llama3-8B-Chinese-Chat,
GPT-4o, and Deepseek-V3 (DeepSeek-AI et al.,
2025).
The Classical Chinese domain LLM is
Xunzi-Qwen1.5-7B-Chat.
Data and Evaluation.
We use the WenyanBench
benchmark for testing. The understanding tasks,
including punctuation, part-of-speech tagging, and
named entity recognition, are evaluated by Preci-
sion, Recall, and F1-Score. The generation tasks
include word explanation, translation, and reverse
dictionary, where BLEU is used for word explana-
tion and translation, and BERT-Score is used for
reverse dictionary.
5.2
Experimental Analysis
WenyanGPT demonstrates a significant lead in
language understanding tasks.
The experimen-
tal results for understanding tasks are presented
in Table 6. In the named entity recognition task,
0.00 
0.20 
0.40 
0.60 
0.80 
1.00 
Punctuation
Part-of-speech 
tagging
NER
Translation
Word explanation
Reverse dictionary
Qwen2.5-7B-Instruct
Baichuan2-7B-Chat
GLM-4-9B-Chat
Meta-Llama-3-8B-Instruct
Llama3-8B-Chinese-Chat
Xunzi-Qwen1.5-7B_chat
gpt-4o
Deepseek-V3
WenyanGPT
Figure 5: Radar plot showing model performance on
WenyanBench, with values normalized to a 0-1 scale.
WenyanGPT’s precision, recall, and F1 score all
exceed 90%, while the second-best model, GPT-
4o, fails to surpass 80% in any of these metrics.
In the punctuation task, WenyanGPT’s F1 score is
16.65% higher than that of the second-best model,
Deepseek-V3, reaching 75.66%. Additionally, in
the part-of-speech tagging task, WenyanGPT’s F1
score is 7.35% higher than that of the second-
best model, GPT-4o.
These results highlight
6

--- Page 7 ---

Model
Translation
Word explanation
Reverse dictionary
Bleu1 Bleu2 Bleu3 Bleu4 Bleu1 Bleu2 Bleu3 Bleu4 P(%) R(%) F1(%)
Qwen2.5-7B-Instruct
0.37
0.23
0.17
0.14
0.16
0.09
0.07
0.05 68.43 68.99 68.66
Baichuan2-7B-Chat
0.33
0.20
0.14
0.11
0.14
0.08
0.05
0.04 64.81 66.21 65.42
GLM-4-9B-Chat
0.34
0.21
0.15
0.12
0.15
0.09
0.06
0.05 65.58 68.04 66.69
Meta-Llama-3-8B-Instruct 0.16
0.09
0.06
0.05
0.11
0.06
0.05
0.04 59.41 64.13 61.48
Llama3-8B-Chinese-Chat
0.26
0.15
0.10
0.08
0.11
0.06
0.04
0.03
61.8 65.18 63.28
Xunzi-Qwen1.5-7B-Chat
0.22
0.15
0.11
0.09
0.11
0.08
0.06
0.05 66.47 68.45 67.35
GPT-4o
0.41
0.27
0.19
0.14
0.19
0.13
0.09
0.07 64.96 66.76 65.81
Deepseek-V3
0.30
0.19
0.13
0.10
0.20
0.14
0.11
0.08 71.93 71.84 71.88
WenyanGPT
0.47
0.33
0.24
0.19
0.35
0.31
0.27
0.23 75.51 75.31 75.39
Table 7: Results for generation tasks (Translation, Word explanation, Reverse dictionary) on WenyanBench. The
results underlined represent the second-best model’s BLEU1 score and BERT-Score-F1 score.
WenyanGPT’s overwhelming superiority in under-
standing tasks, particularly in NER and punctua-
tion. This performance is attributed to the model’s
extensive pre-training on Classical Chinese data,
enabling it to handle complex linguistic phenom-
ena and ensuring higher accuracy and stability in
fundamental language understanding tasks, such as
part-of-speech tagging and NER.
WenyanGPT demonstrates excellent capabilities
and high efficiency in subcategories of Classi-
cal Chinese comprehension tasks.
As shown
in Figure 4, the F1 scores of our model in the
three task’s subcategories are generally stable and
high. Specifically, in the named entity recognition
task, WenyanGPT’s F1 score remains above 80%,
demonstrating its strong ability to correctly iden-
tify entities such as historical figures, place, and
proper nouns in ancient Chinese texts. This per-
formance shows that it has strong accuracy and
robustness when processing ancient Chinese texts,
and can effectively capture complex contextual re-
lationships and word meaning changes. Overall,
WenyanGPT’s high F1 score in ancient Chinese
comprehension tasks not only reflects its high ef-
ficiency in basic tasks, but also demonstrates its
advantages and potential in processing fine-grained
tasks in ancient Chinese.
WenyanGPT can significantly enhance the qual-
ity of generated content in generation tasks.
The experimental results for generation tasks are
displayed in Table 7. WenyanGPT exhibits strong
semantic preservation and contextual consistency,
demonstrates superior and more stable performance
in translation and word explanation tasks, with con-
sistently high BLEU scores (BLEU1-BLEU4). In
classical Chinese translation, the model’s BLEU1
score of 0.47 exceeds that of the second-best model
by 0.06. Furthermore, WenyanGPT’s F1 score in
the reverse dictionary task is 3.47% higher than
the second best model. Through meticulous pre-
training and multitask training, WenyanGPT de-
velops robust contextual consistency, enabling it
to generate content that accurately reflects the in-
tended meaning and context. This capability en-
sures high-quality semantic transmission and con-
tent coherence in both long-text generation and
complex tasks, such as word explanation.
WenyanGPT can achieve better performance
than the previous open source LLMs in Classi-
cal Chinese tasks.
WenyanGPT, through large-
scale pre-training and multitask joint optimization,
demonstrates substantial capabilities in Classical
Chinese processing tasks, establishing a clear lead
over existing mainstream LLMs. This validates
the effectiveness of the proposed approach. The
performance of various LLMs on WenyanBench is
shown in Figure 5. It is evident that WenyanGPT
has achieved the highest score in six Classical Chi-
nese tasks. WenyanGPT’s multitask training strat-
egy, which integrates various Classical Chinese
processing tasks, enhances the model’s ability to
learn across tasks. The mutual reinforcement of
shared linguistic features and semantic information
between tasks notably boosts the model’s gener-
alization capabilities. This inter-task synergy not
only improves performance on individual tasks but
also enables WenyanGPT to effectively handle mul-
tiple tasks simultaneously, maintaining stable per-
formance, especially in complex tasks, and demon-
strating superior adaptability across tasks.
7

--- Page 8 ---

Case 1
Please segment the following
Classical Chinese content and
accurately tag the parts of
speech: 四年春，州吁弑桓
公而立。
Ground Truth
四年/t 春/n ，/w 州吁/nr 弑/v
桓公/nr 而/c 立/v 。/w
WenyanGPT
四年/t 春/n ，/w 州吁/nr 弑/v
桓公/nr 而/c 立/v 。/w
Deepseek-V3
四/m 年/t 春/t，/w /ns 州
吁/nr 弑/v 桓公/nr 而/c 立/v
。/w
GPT-4o
四年/n 春/n ，/w 州/n 吁/v
弑/v 桓公/n 而/c 立/v 。/w
Qwen2.5-7B-
Instruct
四年/t 春/w ，/w 卫州吁/nr
射/v 桓公/nr 而/c 立/v 。/w
Xunzi-
Qwen1.5-
7B-Chat
四年春/t ，/w 州吁/nr 杀/v
桓公/nr 而/c 立/v 。/w
Table 8: Response examples for the part-of-speech tag-
ging task from different LLMs. Errors in part-of-speech
tagging are marked in red, while text errors are high-
lighted in blue.
5.3
Case Study
We provide response examples for part-of-speech
tagging from five LLMs: WenyanGPT, Deepseek-
V3, GPT-4o (Hurst et al., 2024), Qwen2.5-7B-
Instruct, and Xunzi-Qwen1.5-7B-Chat, as shown
in Table 8. By analyzing these examples, we can
see the performance differences of different LLMs
in ccessing tasks, especially in the understanding
tasks of classical Chinese.
Table 8 illustrates some typical errors in the
part-of-speech tagging task. Specifically, GPT-4o
makes mistakes in tagging time words and proper
nouns. For instance, it incorrectly tags the time
expression "四年" (the forth year) as a common
noun, and it also struggles with recognizing the
proper noun "州吁" (Wei Zhou Xu). Qwen2.5-
7B-Instruct errors in tagging the part of speech for
"春" (spring) and sometimes replaces characters
in the original text with inappropriate alternatives.
Xunzi-Qwen1.5-7B-Chat primarily fails in distin-
guishing between time words and nouns, mistak-
enly using the simplified character "杀" instead of
the correct "弑". These errors highlight the model’s
difficulty in making precise distinctions between
similar words.
WenyanGPT demonstrates strong semantic un-
derstanding and retention capabilities in handling
Classical Chinese tasks. Its ability to accurately tag
parts of speech and generate concise, poetic word
explanations demonstrates a deep grasp of the nu-
ances of Classical Chinese. In contrast, other LLMs
struggle with both understanding the subtle distinc-
tions of Classical Chinese and producing responses
that remain faithful to the content and meaning of
the original text. This positions WenyanGPT as a
powerful tool for handling complex tasks in the do-
main of Classical Chinese, far surpassing the other
LLMs in terms of both accuracy and literariness.
6
Conclusion
We propose a comprehensive solution for Classical
Chinese language processing challenges, including
the development of WenyanGPT, a large language
model focused on the Classical Chinese domain,
and WenyanBENCH, an evaluation benchmark
dataset for Classical Chinese tasks. We release pre-
training and instruction fine-tuning datasets and
describe the method for constructing the instruc-
tion fine-tuning dataset. Through systematic exper-
iments and analysis, we demonstrate the significant
impact of domain-specific pre-training and multi-
task instruction fine-tuning on improving Classical
Chinese processing capabilities. Our model out-
permforms existing mainstream LLMs in various
downstream tasks. In future, we attend to explore
the potential of multimodal models by combining
Classical Chinese texts with image data (such as in-
scriptions and manuscripts) to enhance processing
capabilities.
Limitations
Although WenyanGPT has made progress in Clas-
sical Chinese tasks, there are still some limitations.
Firstly, due to space limitations and the subjectiv-
ity of evaluation (manual assessment), tasks such
as poetry generation are not included in the paper.
Secondly, the model mainly relies on large-scale,
high-quality instruction datasets. Finally, there is
still room for improvement when handling long
Classical Chinese texts and complex syntax.
References
Josh Achiam, Steven Adler, Sandhini Agarwal, Lama
Ahmad, Ilge Akkaya, Florencia Leoni Aleman,
Diogo Almeida, and 1 others. 2023. Gpt-4 technical
report. arXiv preprint arXiv:2303.08774.
8

--- Page 9 ---

Tom Brown, Benjamin Mann, Nick Ryder, Melanie
Subbiah, and 1 others. 2020. Language models are
few-shot learners. Advances in neural information
processing systems, 33:1877–1901.
Jiahuan Cao, Dezhi Peng, Yongxin Shi, Zongyuan Jiang,
and Lianwen Jin. 2023. Translating ancient chinese
to modern chinese at scale: A large language model-
based approach. In International Conference on Al-
gorithmic Learning Theory.
Jiahuan Cao, Dezhi Peng, Peirong Zhang, Yongxin Shi,
and 1 others. 2024. Tonggu: Mastering classical chi-
nese understanding with knowledge-grounded large
language models. In Conference on Empirical Meth-
ods in Natural Language Processing.
Bolin Chang, Yiguo Yuan, Bin Li, Zhixing Xu, and
1 others. 2024. Automatic word segmentation and
part-of-speech tagging for classical chinese based on
radicals. Data Analysis and Knowledge Discovery,
8(11):102–113.
Ning Cheng, Bin Li, Liming Xiao, Changwei Xu, and
1 others. 2020. Integration of automatic sentence
segmentation and lexical analysis of ancient chi-
nese based on bilstm-crf model. In Proceedings of
LT4HALA 2020-1st Workshop on Language Tech-
nologies for Historical and Ancient Languages, pages
52–58.
Aakanksha Chowdhery, Sharan Narang, Jacob Devlin,
Maarten Bosma, and 1 others. 2023. Palm: Scal-
ing language modeling with pathways. Journal of
Machine Learning Research, 24(240):1–113.
Jiaxi Cui, Zongjian Li, Yang Yan, Bohua Chen, and
Li Yuan. 2023. Chatlaw: Open-source legal large
language model with integrated external knowledge
bases. CoRR.
Yuhao Dan, Zhikai Lei, Yiyang Gu, Yong Li, and
1 others. 2023. Educhat: A large-scale language
model-based chatbot system for intelligent education.
Preprint, arXiv:2308.02773.
DeepSeek-AI, Aixin Liu, Bei Feng, Bing Xue, Bingx-
uan Wang, Bochao Wu, Chengda Lu, Chenggang
Zhao, Chengqi Deng, Chenyu Zhang, Chong Ruan,
Damai Dai, Daya Guo, Dejian Yang, Deli Chen,
Dongjie Ji, Erhang Li, Fangyun Lin, Fucong Dai,
and 181 others. 2025. Deepseek-v3 technical report.
Preprint, arXiv:2412.19437.
Abhimanyu Dubey, Abhinav Jauhri, Abhinav Pandey,
and 1 others. 2024. The llama 3 herd of models.
arXiv preprint arXiv:2407.21783.
Kshitij Gupta, Benjamin Th’erien, Adam Ibrahim,
Mats L. Richter, Quentin G. Anthony, Eugene
Belilovsky, Irina Rish, and Timothée Lesort. 2023.
Continual pre-training of large language mod-
els:
How to (re)warm your model?
ArXiv,
abs/2308.04014.
Chuen-Min Huang, Kuo-Lin Lu, Yi-Ying Cheng, and
Yu-Chen Peng. 2020. Generating chinese classical
poetry with quatrain generation model (qgm) using
encoder-decoder lstm. In 2020 IEEE International
Conference on Big Data (Big Data), pages 5700–
5702. IEEE.
Hen-Hsen Huang, Chuen-Tsai Sun, and Hsin-Hsi Chen.
2010. Classical chinese sentence segmentation. In
CIPS-SIGHAN Joint Conference on Chinese Lan-
guage Processing, Beijing, China, August 28-29,
2010.
Liang Huang, Yinan Peng, Huan Wang, and Zhenyu
Wu. 2002. Statistical part-of-speech tagging for clas-
sical chinese. In Proceedings of the 5th International
Conference on Text, Speech and Dialogue, TSD ’02,
page 115–122, Berlin, Heidelberg. Springer-Verlag.
Quzhe Huang, Mingxu Tao, Zhenwei An, Chen Zhang,
Cong Jiang, Zhibin Chen, Zirui Wu, and Yansong
Feng. 2023. Lawyer llama technical report.
Aaron Hurst, Adam Lerer, Adam P Goucher, Adam
Perelman, and 1 others. 2024. Gpt-4o system card.
arXiv preprint arXiv:2410.21276.
Adam Ibrahim, Benjamin Th’erien, Kshitij Gupta,
Mats L. Richter, Quentin Anthony, Timothée Lesort,
Eugene Belilovsky, and Irina Rish. 2024. Simple
and scalable strategies to continually pre-train large
language models. ArXiv, abs/2403.08763.
Zixuan Ke, Yijia Shao, Haowei Lin, Tatsuya Konishi,
Gyuhak Kim, and Bin Liu. 2023. Continual pre-
training of language models. In International Con-
ference on Learning Representations.
Jacob Devlin Ming-Wei Chang Kenton and Lee Kristina
Toutanova. 2019. Bert: Pre-training of deep bidirec-
tional transformers for language understanding. In
Proceedings of naacL-HLT, volume 1, page 2. Min-
neapolis, Minnesota.
Eric Lehman, Evan Hernandez, Diwakar Mahajan,
Jonas Wulff, Micah J Smith, Zachary Ziegler, Daniel
Nadler, Peter Szolovits, Alistair Johnson, and Emily
Alsentzer. 2023. Do we still need clinical language
models? ArXiv, abs/2302.08091.
N Li. 2018. Automatic extraction of alias in ancient
local chronicles based on conditional random fields.
J. Chin. Inf. Process, 32:41.
Chang Liu, Dongbo Wang, Zhixiao Zhao, Die Hu,
Mengcheng Wu, Litao Lin, Si Shen, Bin Li,
Jiangfeng Liu, Hai Zhang, and Lianzheng Zhao.
2023a.
Sikugpt: A generative pre-trained model
for intelligent information processing of ancient texts
from the perspective of digital humanities. ArXiv,
abs/2304.07778.
Dayiheng Liu, Jiancheng Lv, Kexin Yang, and Qian
Qu. 2018. Ancient–modern chinese translation with
a new large training dataset. ACM Transactions on
Asian and Low-Resource Language Information Pro-
cessing (TALLIP), 19:1 – 13.
9

--- Page 10 ---

June M. Liu, Donghao Li, He Cao, Tianhe Ren, Zeyi
Liao, and Jiamin Wu. 2023b. Chatcounselor: A large
language models for mental health support. ArXiv,
abs/2309.15461.
Zhuang Liu, Degen Huang, Kaiyu Huang, Zhuang Li,
and Jun Zhao. 2020. Finbert: A pre-trained financial
language representation model for financial text min-
ing. In International Joint Conference on Artificial
Intelligence.
Alec Radford and Karthik Narasimhan. 2018.
Im-
proving language understanding by generative pre-
training.
Alec Radford, Jeff Wu, Rewon Child, David Luan, and
1 others. 2019. Language models are unsupervised
multitask learners.
Aarohi Srivastava, Abhinav Rastogi, Abhishek Rao,
Abu Awal Md Shoeb, and 1 others. 2023. Beyond the
imitation game: Quantifying and extrapolating the
capabilities of language models. Trans. Mach. Learn.
Res., 2023.
Ross Taylor, Marcin Kardas, Guillem Cucurull, Thomas
Scialom, and 1 others. 2022. Galactica: A large
language model for science. ArXiv, abs/2211.09085.
Huishuang Tian, Kexin Yang, Dayiheng Liu, and
Jiancheng Lv. 2020. Anchibert: A pre-trained model
for ancient chinese language understanding and gen-
eration. 2021 International Joint Conference on Neu-
ral Networks (IJCNN), pages 1–8.
Hugo Touvron, Thibaut Lavril, Gautier Izacard, and 1
others. 2023. Llama: Open and efficient foundation
language models. ArXiv, abs/2302.13971.
Ashish Vaswani, Noam M. Shazeer, Niki Parmar, Jakob
Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz
Kaiser, and Illia Polosukhin. 2017. Attention is all
you need. In Neural Information Processing Systems.
Dongbo Wang, Chang Liu, Zhixiao Zhao, Si Shen, and
1 others. 2023a.
Gujibert and gujigpt: Construc-
tion of intelligent information processing foundation
language models for ancient texts. arXiv preprint
arXiv:2307.05354.
Dongbo Wang, Chang Liu, Zihe Zhu, Jiangfeng Liu,
and 1 others. 2022. Sikubert and sikuroberta: Con-
struction and application of pre-trained models for
the siku quanshu in the field of digital humanities.
Library Tribune, 42(06):31–43.
Hao Wang, Chi-Liang Liu, Nuwa Xi, Zewen Qiang,
Sendong Zhao, Bing Qin, and Ting Liu. 2023b. Hu-
atuo: Tuning llama model with chinese medical
knowledge. ArXiv, abs/2304.06975.
Hongbin Wang, Haibing Wei, Jianyi Guo, and Liang
Cheng. 2019. Ancient chinese sentence segmentation
based on bidirectional lstm+ crf model. Journal of
advanced computational intelligence and intelligent
informatics, 23(4):719–725.
Honglin Xiong, Sheng Wang, Yitao Zhu, Zihao Zhao,
Yuxiao Liu, Linlin Huang, Qian Wang, and Ding-
gang Shen. 2023.
Doctorglm: Fine-tuning your
chinese doctor is not a herculean task.
ArXiv,
abs/2304.01097.
Rui Yan, Cheng-Te Li, Xiaohua Hu, and Ming Zhang.
2016. Chinese couplet generation with neural net-
work structures. In Proceedings of the 54th Annual
Meeting of the Association for Computational Lin-
guistics (Volume 1: Long Papers), pages 2347–2357.
Aiyuan Yang, Bin Xiao, Bingning Wang, Borong Zhang,
and 1 others. 2023a. Baichuan 2: Open large-scale
language models. arXiv preprint arXiv:2309.10305.
An Yang, Baosong Yang, Beichen Zhang, and 1 others.
2024a. Qwen2. 5 technical report. arXiv preprint
arXiv:2412.15115.
Songhua Yang, Hanjie Zhao, Senbin Zhu, Guangyu
Zhou, and 1 others. 2024b. Zhongjing: Enhancing
the chinese medical capabilities of large language
model through expert feedback and real-world multi-
turn dialogue.
In Proceedings of the AAAI Con-
ference on Artificial Intelligence, volume 38, pages
19368–19376.
Yi Yang, Yixuan Tang, and Kar Yan Tam. 2023b. In-
vestlm: A large language model for investment us-
ing financial domain instruction tuning. Preprint,
arXiv:2309.13064.
Xiaoyuan Yi, Ruoyu Li, and Maosong Sun. 2017. Gen-
erating chinese classical poems with rnn encoder-
decoder. In Chinese Computational Linguistics and
Natural Language Processing Based on Naturally
Annotated Big Data: 16th China National Confer-
ence, CCL 2017, and 5th International Symposium,
NLP-NABD 2017, Nanjing, China, October 13-15,
2017, Proceedings 16, pages 211–223. Springer.
Y Yuan, D Wang, S Huang, and B Li. 2019. The com-
parative study of different tagging sets on entity ex-
traction of classical books. Data Analysis and Knowl-
edge Discovery, 3(03):57–65.
Shengbin Yue, Wei Chen, Siyuan Wang, Bingxuan Li,
and 1 others. 2023. Disc-lawllm: Fine-tuning large
language models for intelligent legal services. ArXiv,
abs/2309.11325.
Team Glm Aohan Zeng, Bin Xu, Bowen Wang, Chenhui
Zhang, Da Yin, Diego Rojas, and 1 others. 2024.
Chatglm: A family of large language models from
glm-130b to glm-4 all tools. ArXiv, abs/2406.12793.
Jundong Zhang, Songhua Yang, Jiangfeng Liu, and
Qi Huang. 2024.
Aigc empowering the revital-
ization of ancient books on traditional chinese
medicine:building the huang-di large language model.
Library Tribune, 44(10):103–112.
Xuanyu Zhang, Qing Yang, and Dongliang Xu. 2023a.
Xuanyuan 2.0: A large chinese financial chat model
with hundreds of billions parameters. Proceedings of
10

--- Page 11 ---

the 32nd ACM International Conference on Informa-
tion and Knowledge Management.
Yiqin Zhang, Sanhong Deng, Qi Zhang, Dongbo Wang,
and Hongcun Gong. 2023b. Comparative analysis of
language models for linguistic examination of ancient
chinese classics: A case study of zuozhuan corpus.
In 2023 International Conference on Asian Language
Processing (IALP), pages 154–161. IEEE.
A
Categories of part-of-speech tagging
The part-of-speech tagging includes the following
17 categories: nr – Proper Noun (Person), v – Verb,
n – Noun, r – Pronoun, w – Punctuation, c – Con-
junction, p – Preposition, d – Adverb, t – Time
word, y – Modal Particle, u – Auxiliary word, m
– Numeral, a – Adjective, f – Locality Word, ns –
Proper Noun (Place), j – Abbreviation, q – Quanti-
fier.
B
Example of instruction construction
(1) Initialization instruction template:
instruction = "Extract entities from the following
Classical Chinese paragraph, and list characters,
place, time, and official titles. Return the result in
the following format: ’characters’: [...] , ’place’:
[...] , ’time’: [...] , ’official positions’: [...]."
(2) Instruction for task expansion:
prompt = "Based on the following example in-
struction, generate additional instructions for the
Named Entity Recognition (NER) task. These in-
structions should ask the model to extract four
types of entities include characters, place, time,
and official positions from a given Classical Chi-
nese paragraph, and return the results in structured
format. The generated instructions should be di-
verse, natural, consistent with Chinese linguistic
habits, and should clearly specify the task goal and
output format. Example instruction: {instruction}"
(3) Reverse reasoning:
prompt = "Based on the given input content
and the corresponding output, generate some clear
and reasonable task instructions. The instructions
should effectively guide the model to extract four
categories of named entities include characters,
place, time, and official positions from Classical
Chinese text and return them in a structured format
consistent with the provided output. Please ensure
linguistic diversity while maintaining semantic ac-
curacy.
Reference example:
Input: Extract characters, place, time, and offi-
cial positions from the following ancient texts: 侍
御史赵承庆见之，叹曰：御史言及此，天下福
也。
Output: ’characters’: [’赵承庆’], ’place’: [],
’time’: [], ’official positions’: [’御史’]"
Answer:
1. Please conduct entity analysis of the following
classical Chinese to identify the full names, geo-
graphical names, historical time nodes and official
information of all characters, and classify them in
JSON format. If there is no corresponding entity
for a category, leave the list empty.
2. You need to find out four types of information
from the following ancient materials: the name
of the person, the specific place, the dynasty/year,
and the official position. Please according to the
sample format arrangement results: ’ characters’ :
[], ’place’: [], ’time’: [], ’official positions’: []"
...
(4)Filtering generated instructions:
Accept Example :
Input: Perform named entity recognition on the
given Classical Chinese text. Extract characters,
place, time, and official positions, and return them
in the following format: ’characters’: [...], ’place’:
[...], ’time’: [...], ’official positions’: [...]. Classical
Chinese text: 天成初，移镇许州，加同平章
事。
Output:’characters’: [], ’place’: [’许州’], ’time’:
[’天成初’], ’official positions’: [’同平章事’]
Reject Example:
Input: Perform named entity recognition on the
given Classical Chinese text: 天成初，移镇许
州，加同平章事。
Output: 天成初：时间，许州：地点，同平
章事：官职。
C
Case of word explanation task
For the word explanation task, WenyanGPT’s re-
sponse is the closest to the Ground Truth. Although
WenyanGPT adds some modifiers, it maintains
simplicity and refinement in describing the color,
which matches the tone of the poem. Deepseek-
V3, GPT-4o, Qwen2.5-7B-Instruct, and Xunzi-
Qwen1.5-7B-Chat do not specify the subject as "海
棠花" (begonia flowers) and instead over-explained
the moistness of the petals and the process of
spreading color, deviating from the standard, con-
cise description of "晕红" (blushing red). Specifi-
cally, the responses from Qwen2.5-7B-Instruct and
Xunzi-Qwen1.5-7B-Chat extend the impact of the
external environment, which do not fully align with
11

--- Page 12 ---

Case 2
Explain the meaning of "晕
红" in the line "一片晕红
才著雨，几丝柔绿乍和烟"
from "浣溪沙·谁道飘零不可
怜".
Ground Truth
形容海棠花的色泽。De-
scribes the color of begonia
flowers.
WenyanGPT
形容海棠花色泽鲜艳而
浓丽。Describes the bright
and rich color of the begonia
flower.
Deepseek-V3
指雨后花朵泛起的朦胧红
晕。It refers to the hazy red
glow that appears on flowers
after the rain.
GPT-4o
指花瓣在雨水滋润下呈现
出的一种柔和而略带湿
润光泽的红色。Refers to
the soft and slightly moist red
color that the petals appear to
have when nourished by rain.
Qwen2.5-7B-
Instruct
指花瓣上晕染开的淡红
色，适合颜色柔和、渐
变，类似于涂抹或被雨水
滋润后散开的红晕。Refers
to the light red color that
spreads across the petals. It
is suitable for soft and gradual
colors, similar to the blush that
spreads after being smeared or
moistened by rain.
Xunzi-
Qwen1.5-
7B-Chat
指花瓣上的红色晕染，因
为花瓣在雨中被淋湿，
所以红色晕染更加明显。
Refers to the red smudge on
the flower petals. Because the
petals got wet in the rain, the
red smudge is more obvious.
Table 9: Response examples for the word explanation
task from different LLMs.
the original text’s expression. This over-expansion
shows that these LLMs fail to capture the intended
simplicity and depth of the original description.
12

```
