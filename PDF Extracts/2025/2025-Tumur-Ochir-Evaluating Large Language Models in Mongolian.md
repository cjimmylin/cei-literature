---
title: "2025-Tumur-Ochir-Evaluating Large Language Models in Mongolian - PDF Extract"
source_pdf: "2025-Tumur-Ochir-Evaluating Large Language Models in Mongolian.pdf"
pages: 6
extracted_at: "2026-02-14T01:57:26.281708"
---

# PDF Extract: 2025-Tumur-Ochir-Evaluating Large Language Models in Mongolian

**Source PDF:** 2025-Tumur-Ochir-Evaluating Large Language Models in Mongolian.pdf
**Total Pages:** 6

---

## Content

```
--- Page 1 ---

Evaluating Large Language Models in Mongolian
Dorjnyam Tumur-Ochir　Fei Cheng　Yugo Murawaki　Chenhui Chu
Kyoto University
dorjnyam@nlp.ist.i.kyoto-u.ac.jp
{feicheng, murawaki, chu}@i.kyoto-u.ac.jp
Abstract
This paper presents a comprehensive evaluation for as-
sessing large language model (LLM) capabilities in the
Mongolian language, addressing a critical gap in multilin-
gual LLM evaluation. We introduce MonMLU, a novel
benchmark derived from native-level university entrance
exams, alongside Mongolian adaptations of established
benchmarks including Vicuna, MT-Bench, MGSM, and
XCOPA. Our evaluation of leading commercial and openly
available models reveals that while GPT-4o-mini achieves
the highest performance (8.86 on Vicuna, 8.10 on MT-
Bench), openly available models signiﬁcantly underper-
form.
These ﬁndings highlight future opportunities for
improving LLM performance in Mongolian and other low-
resource languages.
1
Introduction
The advancements in large language models (LLMs)
have been especially signiﬁcant in high-resource languages
such as English and Chinese [1, 2].
These models
have demonstrated exceptional capabilities in text genera-
tion, classiﬁcation, understanding, and reasoning tasks [3].
While many state-of-the-art models are multilingual, their
eﬀectiveness in low-resource languages often lags due to
limited training data and benchmarks. Multilingual bench-
marks such as MMMLU and MGSM have been developed
to address these gaps by extending the original English
benchmarks to various languages [4, 5].
The Mongolian language, with over 6 million speakers
across Mongolia and Inner Mongolia (China), represents a
signiﬁcant yet underserved language [6]. Digital resources
in Mongolian comprise less than 0.02% of Common Crawl
data, highlighting the substantial disparity in representation
compared to high-resource languages. This underrepre-
sentation necessitates dedicated evaluation frameworks to
assess and advance LLM capabilities in Mongolian.
To address the resource gap in Mongolian, we develop
and release MonMLU,1）a multi-subject multiple-choice
language understanding benchmark based on native en-
trance examination materials in Mongolian. We adapt the
widely used English benchmarks such as Vicuna and MT-
Bench [7] to evaluate Mongolian rapidly. We show that
current models can generate intelligible responses and fol-
low simple instructions in Mongolian. In addition, to mea-
sure reasoning and understanding abilities, MGSM [5] and
XCOPA[8] are adapted.
The main contributions of our work include:
• MonMLU, a comprehensive benchmark based on na-
tive Mongolian university entrance exams, testing cul-
tural and linguistic knowledge across eight subjects.
• Mongolian-speciﬁc versions of established bench-
marks
(Vicuna,
MT-Bench,
MGSM,
XCOPA)
through translation and localization.
• We evaluate leading commercial and open-source
LLMs, providing a quantitative assessment of their
Mongolian language capabilities.
2
Related Work
2.1
Monolingual benchmarks
Monolingual benchmarks play a crucial role in assessing
the performance of large language models (LLMs) within
a speciﬁc language. Benchmarks such as MMLU, MT-
Bench, and GSM8k are widely used to evaluate LLMs
for reasoning, conversational ability, and mathematical
problem-solving tasks. These benchmarks are designed to
test models on diverse, challenging tasks and have signiﬁ-
cantly advanced the capabilities of LLMs for high-resource
languages like English.
1）https://huggingface.co/ku-nlp/monmlu
― 368 ―
言語処理学会 第31回年次大会 発表論文集（2025年3月）
This work is licensed by the author(s) under CC BY 4.0
 (https://creativecommons.org/licenses/by/4.0/).

--- Page 2 ---

For instance, MMLU assesses knowledge across 57 sub-
jects, including humanities, sciences, and general knowl-
edge. MT-Bench evaluates models’ multi-turn conver-
sation abilities, ensuring context and coherence across in-
teractions are maintained. Similarly, GSM8k focuses on
grade school math word problems, testing models’math-
ematical reasoning and problem-solving skills.
However, such comprehensive benchmarks have not
been developed for low-resource languages like Mongo-
lian. The lack of Mongolian benchmarks limits the ability
to evaluate models comprehensively and hinders progress
in improving LLMs for the language.
Developing tai-
lored benchmarks for the Mongolian language is critical
for understanding and enhancing model performance in
this context.
2.2
Multilingual benchmarks
Eﬀorts to extend evaluations beyond high-resource lan-
guages have led to the development of multilingual bench-
marks. These benchmarks aim to assess LLM performance
across a wide range of languages, providing insights into
multilingual and cross-lingual capabilities. Key examples
include:
• MMMLU (Multilingual MMLU): An extension of
MMLU, MMMLU provides evaluations in 14 lan-
guages by translating the original English dataset.
• XCOPA (Cross-lingual Choice of Plausible Alter-
natives): Derived from the original English COPA
benchmark, XCOPA evaluates commonsense reason-
ing in multiple languages by asking models to select
the most plausible outcome or cause of a given sce-
nario.
• MGSM (Multilingual Grade School Math): This is a
multilingual adaptation of the GSM8k dataset, con-
taining grade school-level math problems translated
into various languages. MGSM assesses the ability to
solve basic mathematical problems within a multilin-
gual context.
These multilingual benchmarks have signiﬁcantly broad-
ened the scope of LLM evaluations. Nevertheless, Mon-
golian is often underrepresented, or even absent, in many
existing multilingual benchmarks. This underscores the
need for targeted evaluation datasets that reﬂect the lin-
guistic and cultural speciﬁcs of the language.
2.3
Low-resource
language
bench-
marks
Low-resource languages are frequently incorporated into
massively multilingual benchmarks such as SIB-200 [9]
and Taxi-200 [10].
However, massively multilingual
benchmarks often prioritize breadth of language coverage
over data quality, particularly for low-resource languages.
Furthermore, they are often limited to classiﬁcation tasks,
neglecting other important and diverse tasks such as rea-
soning and generation.
3
Mongolian Language
Mongolian, a member of the Mongolic language fam-
ily, presents a signiﬁcant yet underrepresented language
in natural language processing. It is primarily spoken in
not just Mongolia, but also in some parts of China (In-
ner Mongolia) and Russia, with approximately 5-6 million
speakers. The language employs diverse writing systems,
including the traditional Mongolian and Cyrillic scripts.
A Romanized transliteration of the Cyrillic script is also
common in informal online communication. This study
focuses on Mongolian written in Cyrillic, the most preva-
lent form. Mongolian presents unique challenges due to its
complex linguistic features such as agglutinative morphol-
ogy and vowel harmony. These linguistic characteristics,
coupled with limited digital resources, make Mongolian a
compelling case study for enhancing LLM performance in
low-resource language settings.
4
Benchmarks
To overcome the scarcity of evaluation resources for
Mongolian, we employ a two-pronged approach: adapt-
ing existing multilingual benchmarks and creating novel
benchmarks tailored speciﬁcally for the language. These
benchmarks comprehensively evaluate Natural Language
Understanding (NLU) and Natural Language Generation
(NLG) tasks. This section introduces and discusses the
following benchmarks: Mongolian Vicuna and MT-Bench,
MonGSM and MonCOPA, and MonMLU. See Appendix
A.2 for samples.
4.1
Adapting existing benchmarks
To adapt Vicuna, MT-Bench, MGSM, and XCOPA
for Mongolian, we followed a machine translation, post-
editing, and localization approach:
― 369 ―
This work is licensed by the author(s) under CC BY 4.0
 (https://creativecommons.org/licenses/by/4.0/).

--- Page 3 ---

Table 1: Summary of benchmarks.
Benchmark
Description
Task type
Size
Construction method
Mongolian Vicuna
Single-turn dialogue
NLG
80
Translation
Mongolian MT-Bench
Multi-turn dialogue
NLG
80
Translation
MonGSM
Math word problems
NLU (Reasoning)
250
Translation
MonCOPA
Commonsense reasoning
NLU (Reasoning)
500
Translation
MonMLU
General knowledge
NLU (Knowledge)
400
Entrance Examination Collection
1. Machine translation: We used GPT-4o to translate
the original English benchmarks into Mongolian.
2. Manual post-editing: A native Mongolian speaker
manually edited the translations to ensure linguistic
accuracy and cultural appropriateness.
3. Localization: Nouns and named entities such as per-
sons and places were replaced by Mongolian names
to make their context more native. For example, robe
to дээл, Hawaii to Х ө всг ө л.
Mongolian Vicuna and MT-Bench
To quickly
evaluate models in the Mongolian language, we adapted
the widely used Vicuna and MT-Bench, which are widely
used benchmarks for evaluating conversational abilities in
LLMs. These benchmarks assess the capacity to generate
coherent, contextually relevant, and logically consistent re-
sponses in single-turn and multi-turn dialogues.
MonGSM and MonCOPA
MonGSM is a Mongo-
lian adaptation of MGSM dataset, which consists of grade
school-level math word problems. These problems test ba-
sic arithmetic, logical reasoning, and problem-solving abil-
ities. XCOPA is a benchmark for evaluating models’ ability
to transfer commonsense reasoning across languages.
These benchmarks highlight the reasoning capabilities
of models in Mongolian and oﬀer a comparative perspec-
tive on their performance relative to other languages.
4.2
Constructing native MonMLU
MonMLU is a benchmark speciﬁcally designed to eval-
uate general knowledge and reasoning abilities in the Mon-
golian language.
We obtained test questions from the
Mongolian General Entrance Examination and received
permission from the relevant institution,2）making it a re-
liable source for testing models on diverse subjects.
It
covers eight subjects: Mongolian language, Mongolian
history, Biology, Chemistry, Physics, and Social Science.
Each subject contains 50 multiple-choice questions with
2）https://eec.mn/
ﬁve choices.
We obtained exam questions and answers, publicly avail-
able on 2）, in PDF format. We manually extract the text
from the exams, excluding images and tables to focus on
unimodal models.
MonMLU evaluates models on the accuracy of re-
sponses, the depth of knowledge across various subjects,
and the ability to understand complex queries and provide
contextually correct answers.
Table 1 shows the summary of all benchmarks. These
benchmarks collectively provide a comprehensive evalua-
tion suite for the Mongolian language, covering conversa-
tional skills, reasoning, and general knowledge.
5
Evaluation
5.1
Settings
Models
For our evaluation, we selected the leading
commercial and openly available models. For commer-
cial models, we use a family of OpenAI models, namely
GPT-3.5-Turbo, GPT-4-Turbo, and GPT-4o-mini.3）Openly
available models are Gemma-2-9B and 27B,4）Llama-3.1
8B,5）Mistral 7B,6）EMMA-500,7）and Qwen2.5 7B.8）We
also include versions of Gemma-2-9B and Llama-3.1-8B,
Gemma-2-9B-Alpaca-MN and Llama-3.1-8B-Alpaca-MN
respectively, ﬁne-tuned on the original Alpaca instruction
dataset that is machine-translated to Mongolian.9）
Evaluation method
We implemented a consistent
evaluation protocol across all benchmarks. For reasoning
3）https://platform.openai.com/docs/models
4）https://huggingface.co/google/gemma-2-9b-it
5）https://huggingface.co/meta-llama/Llama-3.
1-8B
6）https://huggingface.co/mistralai/
Mistral-7B-Instruct-v0.3
7）https://huggingface.co/MaLA-LM/
emma-500-llama2-7b
8）https://huggingface.co/Qwen/Qwen2.
5-7B-Instruct
9）https://huggingface.co/datasets/saillab/
alpaca-mongolian-cleaned
― 370 ―
This work is licensed by the author(s) under CC BY 4.0
 (https://creativecommons.org/licenses/by/4.0/).

--- Page 4 ---

Table 2: Performance of various models across NLG and NLU tasks.
NLG
NLU
Vicuna
MT-Bench
MonGSM
MonMLU
MonCOPA
GPT-4o-mini
8.86
8.10
68.0
52.3
61.0
GPT-4-Turbo
8.49
7.89
74.4
51.1
59.8
GPT-3.5-Turbo
2.95
3.22
17.6
18.0
15.3
Gemma-2-27B-IT
7.01
6.50
59.2
43.7
49.6
Gemma-2-9B-IT
4.22
3.96
46.4
32.2
38.1
Gemma-2-9B-Alpaca-MN
5.95
4.76
14.0
21.6
23.4
Llama-3.1-8B-Instruct
1.98
2.40
34.0
21.1
23.5
Llama-3.1-8B-Alpaca-MN
5.47
3.99
4.0
17.5
16.7
Mistral-7B-Instruct-v0.3
1.38
1.10
4.0
0.0
10.3
EMMA-500-llama2-7b
3.96
2.54
0.0
4.0
0.0
Qwen-2.5-7B-Instruct
2.50
2.64
12.4
23.1
15.6
tasks such as MonGSM, we employed a zero-shot chain-
of-thought setting to assess natural problem-solving ca-
pabilities. Conversational tasks, Vicuna and MT-Bench,
were evaluated using GPT-4o as an independent judge as
proposed by [11]. Multiple-choice questions were scored
using exact match criteria.
5.2
Results
As shown in Table 2, our evaluation revealed signiﬁcant
performance variations across models and tasks. Among
commercial models, GPT-4o-mini demonstrated superior
performance in both NLG and NLU tasks, achieving scores
of 8.86 on Vicuna and 52.3 on MonMLU. GPT-4-Turbo
followed closely with strong results of 8.49 on Vicuna
and 51.1 on MonMLU. However, GPT-3.5-Turbo showed
notably lower performance, scoring only 2.95 on Vicuna
and 18.0 on MonMLU.
Writing
Roleplay
Reasoning
Math
Coding
Extraction
STEM
Humanities
0 1 2 3 4 5 6 7 8 9
model
Qwen2.5-7B-Instruct
EMMA-500-llama2-7b
Gemma-2-9b-Alpaca-M
Llama-3.1-8B-Alpaca-M
Gemma-2-9B-IT
Llama3.1-8B-Instruct
GPT-4o-mini
Figure 1: Category-wise scores of various models on Mon-
golian Vicuna.
In the openly available category, Gemma-2-27B-IT
achieved the strongest results among non-commercial mod-
els, scoring 7.01 on Vicuna and 6.50 on MT-Bench. The
9B variant also shows reasonable performance. Smaller
models demonstrated limited eﬀectiveness, as evidenced
by Mistral-7B and Llama-3.1-8B-Instruct.
As illustrated by Figures 1 and 2, ﬁne-tuned models on
Alpaca, most notably Llama-3.1-8B, show considerable
performance improvement in generation tasks in categories
such as writing and roleplay. At the same time, they lose
their performance in categories such as extraction, coding,
and math. However, we can see a huge performance drop
in NLU tasks. This may be due to a lack of task-speciﬁc
training data as Alpaca contains mostly generic instruc-
tions.
6
Conclusion
In this work, we introduced a set of benchmarks for
the Mongolian language. Four benchmarks were adapted
from widely used English and multilingual benchmarks in-
cluding MT-Bench and MGSM. MonMLU, a multi-subject
multiple-choice benchmark based on native examination
material, was constructed. We evaluated various types of
models on these newly constructed benchmarks. Openly
available models lag behind commercial models consid-
erably. Also, simply ﬁne-tuning models with additional
Mongolian instruction data, while improving text coher-
ence in generated output, does not enhance understanding
and reasoning in the Mongolian language. In future work,
we plan to explore methods aimed at simultaneously im-
proving both generative and understanding capabilities.
― 371 ―
This work is licensed by the author(s) under CC BY 4.0
 (https://creativecommons.org/licenses/by/4.0/).

--- Page 5 ---

Acknowledgment
This work was supported by JSPS KAKENHI Grant
Number JP23K28144.
References
[1]
Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier
Martinet, Marie-Anne Lachaux, Timothée Lacroix, Bap-
tiste Rozière, Naman Goyal, Eric Hambro, Faisal Azhar,
Aurelien Rodriguez, Armand Joulin, Edouard Grave, and
Guillaume Lample. Llama: Open and eﬃcient foundation
language models, 2023.
[2]
Qwen, :, An Yang, Baosong Yang, Beichen Zhang,
Binyuan Hui, Bo Zheng, Bowen Yu, Chengyuan Li, Day-
iheng Liu, Fei Huang, Haoran Wei, Huan Lin, Jian Yang,
Jianhong Tu, Jianwei Zhang, Jianxin Yang, Jiaxi Yang,
Jingren Zhou, Junyang Lin, Kai Dang, Keming Lu, Ke-
qin Bao, Kexin Yang, Le Yu, Mei Li, Mingfeng Xue, Pei
Zhang, Qin Zhu, Rui Men, Runji Lin, Tianhao Li, Tingyu
Xia, Xingzhang Ren, Xuancheng Ren, Yang Fan, Yang Su,
Yichang Zhang, Yu Wan, Yuqiong Liu, Zeyu Cui, Zhenru
Zhang, and Zihan Qiu. Qwen2.5 technical report, 2024.
[3]
Tom Brown, Benjamin Mann, Nick Ryder, Melanie Sub-
biah, Jared D Kaplan, Prafulla Dhariwal, Arvind Nee-
lakantan, Pranav Shyam, Girish Sastry, Amanda Askell,
Sandhini Agarwal, Ariel Herbert-Voss, Gretchen Krueger,
Tom Henighan, Rewon Child, Aditya Ramesh, Daniel
Ziegler, Jeﬀrey Wu, Clemens Winter, Chris Hesse, Mark
Chen, Eric Sigler, Mateusz Litwin, Scott Gray, Benjamin
Chess, Jack Clark, Christopher Berner, Sam McCandlish,
Alec Radford, Ilya Sutskever, and Dario Amodei. Lan-
guage models are few-shot learners.
In H. Larochelle,
M. Ranzato, R. Hadsell, M.F. Balcan, and H. Lin, editors,
Advances in Neural Information Processing Sys-
tems, Vol. 33, pp. 1877–1901. Curran Associates, Inc.,
2020.
[4]
Dan Hendrycks, Collin Burns, Steven Basart, Andy Zou,
Mantas Mazeika, Dawn Song, and Jacob Steinhardt. Mea-
suring massive multitask language understanding, 2020.
[5]
Freda Shi, Mirac Suzgun, Markus Freitag, Xuezhi Wang,
Suraj Srivats, Soroush Vosoughi, Hyung Won Chung,
Yi Tay, Sebastian Ruder, Denny Zhou, Dipanjan Das, and
Jason Wei. Language models are multilingual chain-of-
thought reasoners, 2022.
[6]
Pratik Joshi, Sebastin Santy, Amar Budhiraja, Kalika Bali,
and Monojit Choudhury. The state and fate of linguistic
diversity and inclusion in the NLP world.
In Dan Ju-
rafsky, Joyce Chai, Natalie Schluter, and Joel Tetreault,
editors, Proceedings of the 58th Annual Meeting
of the Association for Computational Linguistics,
pp. 6282–6293, Online, July 2020. Association for Com-
putational Linguistics.
[7]
Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan
Zhuang, Zhanghao Wu, Yonghao Zhuang, Zi Lin, Zhuo-
han Li, Dacheng Li, Eric P. Xing, Hao Zhang, Joseph E.
Gonzalez, and Ion Stoica. Judging llm-as-a-judge with
mt-bench and chatbot arena, 2023.
[8]
Edoardo Maria Ponti, Goran Glavaš, Olga Majewska,
Qianchu Liu, Ivan Vulić, and Anna Korhonen. XCOPA:
A multilingual dataset for causal commonsense reason-
ing. In Bonnie Webber, Trevor Cohn, Yulan He, and Yang
Liu, editors, Proceedings of the 2020 Conference
on Empirical Methods in Natural Language Pro-
cessing (EMNLP), pp. 2362–2376, Online, November
2020. Association for Computational Linguistics.
[9]
David Ifeoluwa Adelani, Hannah Liu, Xiaoyu Shen, Nikita
Vassilyev, Jesujoba O. Alabi, Yanke Mao, Haonan Gao,
and Annie En-Shiun Lee. Sib-200: A simple, inclusive,
and big evaluation dataset for topic classiﬁcation in 200+
languages and dialects, 2024.
[10]
Chunlan Ma, Ayyoob ImaniGooghari, Haotian Ye, Renhao
Pei, Ehsaneddin Asgari, and Hinrich Schütze. Taxi1500:
A multilingual dataset for text classiﬁcation in 1500 lan-
guages, 2024.
[11]
Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan
Zhuang, Zhanghao Wu, Yonghao Zhuang, Zi Lin, Zhuo-
han Li, Dacheng Li, Eric P. Xing, Hao Zhang, Joseph E.
Gonzalez, and Ion Stoica. Judging llm-as-a-judge with
mt-bench and chatbot arena, 2023.
― 372 ―
This work is licensed by the author(s) under CC BY 4.0
 (https://creativecommons.org/licenses/by/4.0/).

--- Page 6 ---

A
Appendix
A.1
MT-Bench
Writing
Roleplay
Reasoning
Math
Coding
Extraction
STEM
Humanities
0 1 2 3 4 5 6 7 8
model
Qwen2.5-7B-Instruct
EMMA-500-llama2-7b
Gemma-2-9b-Alpaca-M
Llama-3.1-8B-Alpaca-M
Gemma-2-9B-IT
Llama-3.1-8B-Instruct
GPT-4o-mini
Figure 2: Category-wise scores of various models on Mon-
golian MT-Bench.
A.2
Samples
Figure 3: A sample instruction and response pair of GPT-
4o-mini on Mongolian Vicuna.
Figure 4: A sample from MT-Bench. Words in red are
localized words.
Figure 5: A sample from MonGSM. Words in red are
localized words.
Figure 6: A sample from MonMLU. The correct answer is
in bold.
― 373 ―
This work is licensed by the author(s) under CC BY 4.0
 (https://creativecommons.org/licenses/by/4.0/).

```
