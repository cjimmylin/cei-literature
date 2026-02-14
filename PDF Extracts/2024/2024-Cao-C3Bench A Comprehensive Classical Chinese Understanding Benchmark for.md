---
title: "2024-Cao-C3Bench A Comprehensive Classical Chinese Understanding Benchmark for - PDF Extract"
source_pdf: "2024-Cao-C3Bench A Comprehensive Classical Chinese Understanding Benchmark for.pdf"
pages: 10
extracted_at: "2026-02-13T17:43:17.091744"
---

# PDF Extract: 2024-Cao-C3Bench A Comprehensive Classical Chinese Understanding Benchmark for

**Source PDF:** 2024-Cao-C3Bench A Comprehensive Classical Chinese Understanding Benchmark for.pdf
**Total Pages:** 10

---

## Content

```
--- Page 1 ---

C3BENCH: A COMPREHENSIVE CLASSICAL CHINESE
UNDERSTANDING BENCHMARK FOR LARGE LANGUAGE
MODELS
Jiahuan Cao, Yongxin Shi, Dezhi Peng, Yang Liu, Lianwen Jin∗
South China University of Technology
jiahuanc@foxmail.com, eelwjin@scut.edu.cn
ABSTRACT
Classical Chinese Understanding (CCU) holds significant value in preserving and exploration of the
outstanding traditional Chinese culture. Recently, researchers have attempted to leverage the potential
of Large Language Models (LLMs) for CCU by capitalizing on their remarkable comprehension
and semantic capabilities. However, no comprehensive benchmark is available to assess the CCU
capabilities of LLMs. To fill this gap, this paper introduces C3bench, a Comprehensive Classical
Chinese understanding benchmark, which comprises 50,000 text pairs for five primary CCU tasks,
including classification, retrieval, named entity recognition, punctuation, and translation. Furthermore,
the data in C3bench originates from ten different domains, covering most of the categories in classical
Chinese. Leveraging the proposed C3bench, we extensively evaluate the quantitative performance of
15 representative LLMs on all five CCU tasks. Our results not only establish a public leaderboard
of LLMs’ CCU capabilities but also gain some findings. Specifically, existing LLMs are struggle
with CCU tasks and still inferior to supervised models. Additionally, the results indicate that
CCU is a task that requires special attention. We believe this study could provide a standard
benchmark, comprehensive baselines, and valuable insights for the future advancement of LLM-
based CCU research. The evaluation pipeline and dataset are available at https://github.com/
SCUT-DLVCLab/C3bench.
1
Introduction
The 5000-year history of Chinese civilization has engendered numerous precious cultural artifacts, with classical
Chinese serving as one of the most crucial carriers for this heritage. Consequently, classical Chinese understanding
plays a significant role in safeguarding and advancing this rich traditional Chinese culture. However, due to its distinctive
language structure and vocabulary, comprehending classical Chinese poses a significant challenge for non-experts. With
the rapid development of deep learning, some researchers tried to employ deep models to accomplish CCU tasks, such
as named entity recognition [1,2] and translation [3,4]. Recently, Large Language Models (LLMs) have demonstrated
impressive capabilities in various NLP tasks [5–10].
Benefiting from large-scale training corpus, LLMs possess robust transfer abilities [11–13]. Some researchers have
delved into the potential of LLMs for CCU tasks and achieved preliminary success [14–16]. Nevertheless, the classical
Chinese understanding capability of LLMs remains inadequately explored due to the lack of a standard CCU benchmark,
hampering further investigation in this field.
To fill this gap, we propose C3bench, a Comprehensive Classical Chinese understanding benchmark for LLMs, which
consists of 50,000 text pairs for five CCU tasks, including classification, retrieval, named entity recognition, punctuation,
and translation. Unlike previous benchmark [17] for specific CCU tasks or benchmark [18] that use simple multiple
choice questions to evaluate generative large language models, C3bench is the first multi-task CCU benchmark specified
for LLMs using natural language generation. Furthermore, the C3bench consists of data from ten different domains,
∗Corresponding Author.
arXiv:2405.17732v2  [cs.CL]  30 May 2024

--- Page 2 ---

Figure 1. The performance of several representative evaluated models on C3Bench.
requiring models to possess a broad and diverse range of understanding capabilities, aligning closely with the inherent
attributes of LLMs. Based on the C3bench, we conduct extensive evaluations of 15 representative models, affirming
their significant potential for future academic research endeavors. We draw the performance of several representative
models in a radar map as shown in Figure 1. The evaluation results unveil that existing LLMs are struggle with CCU
tasks and still inferior to supervised models. Additionally, the results indicate that CCU is a task that requires special
attention. In summary, our contributions are as follows:
• We propose a comprehensive classical Chinese understanding benchmark, named C3bench. To the best of
our knowledge, this is the first classical Chinese understanding benchmark for LLMs using natural language
generation.
• Based on C3bench, we comprehensively evaluate 15 widely-used models, revealing and quantifying their
abilities in classical Chinese understanding.
• We analyze the evaluation results in depth, uncovering valuable findings that can offer meaningful references
and insights for the future advancement of LLM-based CCU research.
2
Related works
2.1
Large language models
The rise of Large language models (LLMs) can be attributed to the introduction of the Transformer [19] architecture,
which dates back to GPT [20] and BERT [21]. Subsequently, the parameters of LLMs expanded rapidly. T5 [5] unified
the form of tasks, enabling a single model to address multiple tasks. Flan-T5 [7] used instruction tuning to align the
model’s responses with human instructions, and Reinforcement Learning from Human Feedback (RLHF) [22] further
strengthened this process. ChatGPT [22] and GPT-4 [10] are the most representative LLMs, while LLaMA [23] is the
most prominent open-source LLMs, driving the rapid development of the open-source community and giving birth to
models like Vicuna [24]. For Chinese LLMs, GLM-130B [25] is a large model based on the General Language Model
(GLM) architecture [26]. Baichuan2 [27] is a series of LLMs that have been trained from scratch on 2.6T tokens, while
Qwen [28] is a series of LLMs trained on 3T tokens. Those models have all undergone the Supervised Fine-Tuning
(SFT) [7] and RLHF [22] processes to get the chat models.
2.2
Automatically classical Chinese understanding
Early automatic systems for classical Chinese comprehension originated from the application of traditional Natural
Language Processing (NLP) techniques. These models were tailored for specific tasks, such as punctuation, named
2

--- Page 3 ---

entity recognition, and translation. These approaches [3, 29] predominantly rely on intricate statistical models or
extensively hand-annotated supervised data to attain satisfactory performance. Although these methodologies excel
in specific tasks, they are often hampered by the constraints of their manually-engineered features and proprietary
resources, which inhibit their capacity to generalize across a spectrum of tasks. With the rise of deep learning in NLP, we
have witnessed the proliferation of large-scale models and transfer learning techniques across a myriad of tasks. Models
like GuwenBERT1 and SikuBERT [30] exemplify this trend, leveraging pre-trained BERT [21] embeddings specific
to classical Chinese. With minimal supervised data, they have achieved remarkable proficiency in classical Chinese
understanding. A salient feature of these approaches is their reduced dependency on dictionaries and intricate structures,
offering a more generalized means of Classical Chinese understanding. The emergence of models like SikuGPT [14]
underscores the benefits of pre-trained models combined with extensive classical literature corpora, especially in
generating classical prose and poetry. Models such as Bloom-7B-Chunhua5, utilizing auto-generated fine-tuning data
coupled with open-source base models, have achieved high levels in classical Chinese question-answering tasks.
2.3
Chinese NLP evaluation benchmarks
Evaluation benchmarks for Natural Language Processing (NLP) in Chinese are crucial for the rapid development of
this field. CLUE [31] is widely recognized as one of the most authoritative benchmarks in the field. The introduction
of CUGE [32] has further enhanced the assessment of generative capacity. SuperCLUE [31] offers a comprehen-
sive assessment of LLMs from various perspectives, including code, computation, and conversation. C-Eval [33]
compromises evaluations across 52 disciplines within the humanities and social sciences. CMMLU [34] covers 67
topics ranging from basic disciplines to advanced professional levels. AGIEval [35] is derived from 20 official, public,
and high-standard admission and qualification exams intended for general human test-takers. PromptBench [36] and
HalluQA [37] assess LLMs concerning robustness and susceptibility to hallucination. However, there is no benchmark
in the field for assessing LLMs’ comprehension of classical Chinese.
2.4
Classical Chinese benchmarks
CASIA-AHCDB [38] provides more than 2.2 million texts from 10,350 categories for character recognition. MTHv2
[39] consists of 3,199 images of Buddhist texts, which can be used for text detection, text recognition, and reading order
prediction. ICDAR 2019 HDRC-CHINESE [40] is a large-scale family records dataset, which contains 12,850 images.
SCUT-CAB [41] is a complex dataset for layout analysis. M5HisDoc [42] is a comprehensive Chinese historical
document analysis benchmark, which features a wide range of styles. However, these datasets are specifically designed
for visual tasks. Regarding the NLP benchmarks of classical Chinese, the C-CLUE [17] has developed a dataset for
named entity recognition and relation extraction. NiuTrans2 provides an extensive corpus of Classical-Modern Chinese
bilingual data. In summary, compared with visual benchmarks, there is still a lack of NLP benchmarks of classical
Chinese, especially those designed for LLMs. This is one of the reasons that we propose the C3Bench dataset, a
multitask benchmark tailored for the evaluation of LLMs in classical Chinese.
3
C3Bench
3.1
Task definition
To comprehensively evaluate the classical Chinese understanding capabilities of LLMs, we have integrated the following
five tasks into the proposed C3bench. We provide some examples of each task in Table 1.
• Classification: The model is required to assign a given classical Chinese sentence to one of ten categories,
namely poetry, history, Buddhism, Confucianism, Taoism, medicine, arts, military, law, and agriculture.
• Retrieval: This task requires the model to accurately identify and return the title of the article from which the
classical Chinese sentence originated.
• Named Entity Recognition: Given a classical Chinese sentence, this task requires the model to return the
named entities (for example, the personal names, official position, or geographical names) within it.
• Punctuation: The model is supposed to insert appropriate punctuation marks into an unpunctuated sentence.
• Translation: This task requires the model to translate a classical Chinese sentence into modern Chinese.
1https://github.com/ethan-yt/guwenbert
2https://github.com/NiuTrans/Classical-Modern
3

--- Page 4 ---

Table 1. Examples of input and output in C3Bench.
Task
Input
Output
Classification
天生我材必有用，千金散尽还复来。
诗
Retrieval
中通外直，不蔓不枝，
香远益清，亭亭净植，可远观而不可亵玩焉。
《爱莲说》
NER
泰至渭南，集诸州兵来会。
诸将以众寡不敌，请且待欢更西以观之。
泰、渭、欢
Punctuation
夫未战而庙算胜者得算多也未战而庙算不胜者得算少也
夫未战而庙算胜者，得算多也；
未战而庙算不胜者，得算少也。
Translation
孔子既祥，五日弹琴而不成声，十日而成笙歌。
孔子在大祥后五天开始弹琴，但弹不成声调；
在大祥后逾月的又一旬里欢笙，其声调就和谐了。
3.2
Benchmark construction
Our benchmark construction involved several key procedures. Firstly, we selected ten representative categories of
ancient texts as labels for the classification task. For each category, sentences from ancient texts were collected
independently from the Internet, while preserving the titles of their source articles as the Ground Truth (GT) for
the retrieval task. In total, 10,000 sentences were collected. Secondly, the modern Chinese translations of these
sentences were obtained through online searches and manual annotation, which serve as the GT for the translation task.
Thirdly, we invited professional annotators to label the entities within the sentences, establishing the GT for the named
entity recognition (NER) task. Fourthly, we removed punctuation marks from each sentence to serve as input for the
punctuation task, with the original sentences as the GT. Finally, we conducted a rigorous and thorough double-check of
the aforementioned data to ensure its quality.
3.3
Data statistics
The basic data statistics of C3bench are shown in Table 2. We can see that each task consists of 10,000 pairs, amounting
to a total of 50,000 text pairs. The distribution of domains within the dataset is depicted in Figure 2. History and
Confucianism are predominant in classical Chinese texts and constitute the largest proportion of our benchmark. As
illustrated in Figure 3, the coverage of sentence length is quite diverse. Moreover, the majority of sentences have a
length ranging from 16 to 32, aligning with the typical distribution in classical Chinese. Additionally, there are also
challenging sentences with length exceeding 96.
Figure 2. Domain distribution of the dataset.
Figure 3. Distribution of sentence length.
4
Experiments
4.1
Models
In this paper, we focus on 15 widely used LLMs, including both open-source models and closed-source models. The
detail of these models are presented in Table 3. We also consider some supervised method for comparison.
4

--- Page 5 ---

Table 2. The data statistics of C3Bench.
Domain
Classification
Retrieval
Named Entity Recognition
Punctuation
Translation
Poetry
1,000
1,000
1,000
1,000
1,000
History
2,000
2,000
2,000
2,000
2,000
Buddhism
1,000
1,000
1,000
1,000
1,000
Confucianism
2,000
2,000
2,000
2,000
2,000
Taoism
1,000
1,000
1,000
1,000
1,000
Medicine
1,000
1,000
1,000
1,000
1,000
Art
500
500
500
500
500
Military
500
500
500
500
500
Law
500
500
500
500
500
Agriculture
500
500
500
500
500
Total
10,000
10,000
10,000
10,000
10,000
Open-source models:
LLaMA [23] is a representative open-source LLM, we selected the modern Chinese localized
versions of it, specifically LLaMA2-Chinese-7B-Chat3 and LLaMA2-Chinese-13B-Chat4. We included Bloom-7B-
Chuhua5, which is a classical Chinese localized version of Bloom [43]. Additionally, We selected the most widely
recognized ones developed by domestic research institutions for evaluation, including Baichuan2-7B-Chat [27],
Baichuan2-13B-Chat [27], ChatGLM2-6B [26], Qwen-7B-Chat [28], Qwen-14B-Chat [28] and Moss-moon-003-
SFT [44].
Closed-source models:
We selected models developed by OpenAI, including GPT-3.5-turbo [22] and GPT-4 [10], as
well as some representative models developed by domestic institutions, including ERNIE-bot-turbo [45], Spark-v3 [46],
ChatGLM [26] and abab5-chat [47].
Supervised methods:
Supervised methods of NER and punctuation are reached by Guwen-NER6 and Guwen-punc7,
respectively, both of which are finetuned from GuwenBERT, a RoBERTa pre-trained with 1.7B classical Chinese tokens.
Similarly, Guwen-cls8 is the supervised method of classification, and it is noteworthy that the category of Guwen-cls
is different from our category, so only the common category was considered when testing. And the best result of
translation is achieved by Cao, et al [15], with a LLaMA-13B model finetuned using 400M translation data.
Table 3. Details of tested models.
Model
Access method
Website
Parameters
Release date
Bloom-7B-Chunhua5
Local inf.
https://huggingface.co/wptoux/bloom-7b-chunhua
7B
April, 2023
Baichuan2-7B-Chat [27]
Local inf.
https://huggingface.co/baichuan-inc/Baichuan2-7B-Chat
7B
September, 2023
Baichuan2-13B-Chat [27]
Local inf.
https://huggingface.co/baichuan-inc/Baichuan2-13B-Chat
13B
September, 2023
ChatGLM2-6B [26]
Local inf.
https://huggingface.co/THUDM/chatglm2-6b
6B
June, 2023
Qwen-7B-Chat [28]
Local inf.
https://huggingface.co/Qwen/Qwen-7B-Chat
7B
September, 2023
Qwen-14B-Chat [28]
Local inf.
https://huggingface.co/Qwen/Qwen-7B-Chat
14B
September, 2023
LLaMA2-Chinese-7B-Chat3
Local inf.
https://huggingface.co/FlagAlpha/Llama2-Chinese-7b-Chat
7B
July, 2023
LLaMA2-Chinese-13B-Chat4
Local inf.
https://huggingface.co/FlagAlpha/Llama2-Chinese-13b-Chat
13B
July, 2023
Moss-moon-003-SFT [44]
Local inf.
https://huggingface.co/fnlp/moss-moon-003-sft
16B
April, 2023
GPT-3.5-turbo [22]
API call
https://chat.openai.com/
-
November, 2023
GPT-4 [22]
API call
https://chat.openai.com/
-
November, 2023
ERNIE-bot-turbo [45]
API call
https://console.bce.baidu.com/qianfan
-
September, 2023
Spark-v3 [46]
API call
https://xinghuo.xfyun.cn/sparkapi
-
October, 2023
abab5-chat [47]
API call
https://api.minimax.chat/
-
-
ChatGLM_Turbo [26]
API call
https://open.bigmodel.cn/
-
October, 2023
4.2
Settings
Prompts
The models we chose for evaluation have all undergone instruction-based fine-tuning or Reinforcement
Learning from Human Feedback (RLHF) [22], and thus can follow the instructions of users. Consequently, we have
constrained the output format of each task in prompts to facilitate automatic and precise evaluation of the output
results. The prompts in Chinese for each task are presented in Table 4, with translations provided in English for a wider
audience.
5

--- Page 6 ---

Table 4. Prompts for each task. We use the Chinese prompt and also provide its English meaning for reference.
Task
Prompt
Prompt in English
Classification
不需要解释，
直接从“诗、史、儒、道、佛、农、法、艺、医、兵”中
选择一个类别输出，
判断下列文言文的类别：[文言文]
Without explanation,
directly from "Poetry, History, Confucianism, Taoism, Buddhism,
Buddhism, Agriculture, Law, Arts, Medicine, Military" to select
a category output, judge the following categories of classical Chinese: [classical Chinese]
Retrieval
不需要解释，直接给出下列文言文出处书名：[文言文]
Without explanation, directly give
the following source title of classical Chinese: [classical Chinese]
NER
找出下列文言文中的命名实体。若无实体，输出“无”；
若有实体，直接输出实体，多个实体之间用“、”分隔：[文言文]
Find the following named entities in classical Chinese.
If there is no entity, output "no"; if there is an entity,
directly output entity, multiple entities are separated by ",": [classical Chinese]
Punctuation
不需要解释，直接输出下列文言文添加标点符号后的结果：[文言文]
Without explanation, directly output the following results
after adding punctuation marks to classical Chinese: [classical Chinese]
Translation
不需要解释，直接输出下列文言文的白话文翻译：[文言文]
Without explanation, directly output the
following classical Chinese translation of vernacular Chinese: [classical Chinese]
Inference settings
For open-source models, we employed the recommended system message and role, and loaded
the models using bfloat16 precision. Furthermore, the maximum number of tokens for model responses was limited
to 2048, with nucleus sampling configured at 1 and top-k sampling at 50. As for closed-source models, we were
unable to control the model loading precision, but the other settings remained consistent with those of the open-source
models. It is crucial to note that model outputs may not always strictly conform to the stipulated format. Therefore,
post-processing adjustments were implemented to ensure fair and consistent assessments across different models.
4.3
Metric
For different tasks, we employ distinct evaluation metrics.
• Classification: We utilize accuracy in this task. If the model correctly classifies a sentence, it will get a score
of 1, or 0 otherwise. The final total score is averaged for the accuracy.
• Retrieval: Similarly, we use accuracy for the retrieval task, while due to the multi-level label structure, we
calculate accuracy for each level of the hierarchy.
• Punctuation: We adopt F1 score as the evaluation metric as in previous work [48].
• Named Entity Recognition: We utilize F1 score for this task as in previous work [49].
• Translation: For this task, we use BLEU [50] as the evaluation metric.
4.4
Results and analysis
The results of all tested models are shown in Table 5, and we also draw the performance of several representative
models in a radar map as shown in Figure 1. Based on the results, we draw the following insights:
CCU is challenging for current LLMs:
The overall ranking of the CCU capability, as illustrated in Figure 4,
indicates that all 15 tested models scored an average below 50. In the critical translation task in classical Chinese, only
one model exceeds a 20 BLEU score. For the highly challenging retrieval task, the accuracy of all models falls below
0.3. This highlights the complexity of our data and suggests significant room for improvement in the ability of LLMs to
comprehend classical Chinese.
Existing LLMs do not outperform the supervised models:
As shown in the last row of Table 5, the performance
of supervised models on specific tasks outperforms existing LLMs, especially demonstrating significant superiority in
translation and classification tasks. In classification task, the best supervised model can achieve an accuracy of 0.8266,
which is 0.2651 higher than the best LLM. While in translation task, the best LLM achieves only 34.58 BLEU, far
behind the supervised method of 52.02 BLEU.
3https://huggingface.co/FlagAlpha/Llama2-Chinese-7b-Chat
4https://huggingface.co/FlagAlpha/Llama2-Chinese-13b-Chat
5https://huggingface.co/wptoux/bloom-7b-chunhua
6https://huggingface.co/ethanyt/guwen-ner
7https://huggingface.co/ethanyt/guwen-punc
8https://huggingface.co/ethanyt/guwen-cls
6

--- Page 7 ---

Table 5. Results of all tasks. The bold and underlined indicate the best and the second best results, respectively.
Model
Classifications ↑
Retrieval ↑
NER ↑
Punctuation ↑
Translation ↑
Average ↑
Bloom-7B-Chunhua5
39.62
13.36
34.70
62.19
11.27
33.23
Baichuan2-7B-Chat [27]
37.00
18.36
63.25
53.96
13.70
37.15
Baichuan2-13B-Chat [27]
44.26
17.79
46.67
65.11
12.45
37.26
ChatGLM2-6B [26]
50.28
9.03
28.56
28.48
6.76
24.62
Qwen-7B-Chat [28]
49.65
13.92
28.33
69.61
15.61
35.42
Qwen-14B-Chat [28]
44.93
25.90
66.72
71.83
15.38
44.95
LLaMA2-Chinese-7B-Chat3
18.78
3.20
12.62
34.73
4.24
14.71
LLaMA2-Chinese-13B-Chat4
28.75
2.27
9.31
47.27
5.91
18.70
Moss-moon-003-SFT [44]
15.07
15.84
28.90
58.39
13.35
26.30
GPT-3.5-turbo [22]
50.65
7.36
63.83
61.34
11.94
39.02
GPT-4 [22]
53.88
13.71
63.87
67.31
12.09
42.17
ERNIE-bot-turbo [45]
50.70
21.22
9.61
65.29
10.66
31.50
Spark-v3 [46]
51.61
21.83
53.81
85.38
34.58
49.44
abab5-chat [47]
52.20
15.53
34.64
65.42
10.56
35.67
ChatGLM_Turbo [26]
56.15
20.49
30.04
69.72
10.91
37.46
Supervised-Method
82.668
-
73.736
82.487
52.02 [15]
-
Figure 4. Overall ranking of Classical Chinese Understanding capability for all the evaluated models.
Current LLMs have unbalanced CCU capability:
Classical Chinese understanding capability of some large models
is unbalanced. For example, ChatGLM_Turbo [26] ranks first in the classification task and also achieves good retrieval
and punctuation performance. However, it exhibits extremely low performance on the named entity recognition and
translation tasks. We argue that this may be due to the imbalanced training data associated with individual tasks.
Classical Chinese understanding is a task that requires special attention:
Although certain studies [51] have
indicated significant improvements in the modern Chinese understanding capabilities of English models such as LLaMA
after fine-tuning with a small amount of Chinese data, our experiments suggest that such models have insufficient
understanding capabilities of classical Chinese. This underscores the unique requirements for understanding classical
Chinese, which demands knowledge of Chinese characteristics and traditional culture not readily transferable from
English. Therefore, improving the classical Chinese understanding capability of LLMs is a critical concern that
necessitates special attention.
7

--- Page 8 ---

5
Limitations
There are two main limitations of our work. First, the C3bench does not exhaustively cover all types of classical Chinese
understanding (CCU) tasks, such as the summary of ancient texts. Instead, we focus on five representative tasks, and
hope to evaluate the CCU capabilities of LLMs through these tasks. Second, only the zero-shot capacity in CCU tasks
was evaluated, without exploring few-shot scenarios.
6
Conclusion
In this study, we introduce C3bench, the first comprehensive Classical Chinese Understanding (CCU) benchmark for
Large Language Models (LLMs), which spans a multitude of tasks and various domains. Based on the C3bench, we
comprehensively evaluate 15 representative LLMs, quantifying their capabilities in CCU and establishing a public
leaderboard. Our results unveil that existing LLMs are struggle with CCU tasks and still inferior to supervised models.
Additionally, the results indicate that CCU is a task that requires special attention. This study provides a standard
benchmark, comprehensive baselines, and valuable insights for the future advancement of LLM-based CCU research.
References
[1] Peng Yu and Xin Wang. BERT-based named entity recognition in Chinese Twenty-Four Histories. In Proc. WISA,
pages 289–301. Springer, 2020.
[2] Xiaowei Han, Lizhen Xu, and Feng Qiao. CNN-BiLSTM-CRF model for term extraction in Chinese corpus. In
Proc. WISA, pages 267–274. Springer, 2018.
[3] Zongyuan Jiang, Jiapeng Wang, Jiahuan Cao, Xue Gao, and Lianwen Jin. Towards better translations from
classical to modern Chinese: A new dataset and a new method. In Proc. NLPCC, pages 387–399. Springer, 2023.
[4] Ernie Chang, Yow-Ting Shiue, Hui-Syuan Yeh, and Vera Demberg. Time-Aware ancient Chinese text translation
and inference. In Proc. LChange, pages 1–6, 2021.
[5] Colin Raffel, Noam Shazeer, Adam Roberts, Katherine Lee, Sharan Narang, Michael Matena, Yanqi Zhou, Wei Li,
and Peter J Liu. Exploring the limits of transfer learning with a unified text-to-text transformer. J. Mach. Learn.
Res., 21(1):5485–5551, 2020.
[6] Susan Zhang, Stephen Roller, Naman Goyal, Mikel Artetxe, Moya Chen, Shuohui Chen, Christopher Dewan,
Mona Diab, Xian Li, Xi Victoria Lin, et al. OPT: Open pre-trained transformer language models. arXiv preprint
arXiv:2205.01068, 2022.
[7] Hyung Won Chung, Le Hou, Shayne Longpre, Barret Zoph, Yi Tay, William Fedus, Yunxuan Li, Xuezhi Wang,
Mostafa Dehghani, Siddhartha Brahma, et al. Scaling instruction-finetuned language models. arXiv preprint
arXiv:2210.11416, 2022.
[8] Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam Roberts, Paul
Barham, Hyung Won Chung, Charles Sutton, Sebastian Gehrmann, et al. PALM: Scaling language modeling with
pathways. J. Mach. Learn. Res., 24(240):1–113, 2023.
[9] Tom B Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind Nee-
lakantan, Pranav Shyam, Girish Sastry, Amanda Askell, et al. Language models are few-shot learners. In Proc.
NeurIPS, pages 1877–1901, 2020.
[10] OpenAI. GPT-4 technical report. arXiv preprint arXiv:2303.08774, 2023.
[11] Zewen Chi, Heyan Huang, Luyang Liu, Yu Bai, Xiaoyan Gao, and Xian-Ling Mao. Can pretrained english
language models benefit non-english nlp systems in low-resource scenarios? IEEE-ACM Trans. Audio Speech
Lang., 2023.
[12] Marjan Ghazvininejad, Hila Gonen, and Luke Zettlemoyer. Dictionary-based phrase-level prompting of large
language models for machine translation. arXiv preprint arXiv:2302.07856, 2023.
[13] Hailemariam Mehari Yohannes and Toshiyuki Amagasa. Named-entity recognition for a low-resource language
using pre-trained language model. In Proc. SAC, pages 837–844, 2022.
[14] Liu Chang, Wang Dongbo, Zhao Zhixiao, Hu Die, Wu Mengcheng, Lin Litao, Shen Si, Li Bin, Liu Jiangfeng,
Zhang Hai, et al. SikuGPT: A generative pre-trained model for intelligent information processing of ancient texts
from the perspective of digital humanities. arXiv preprint arXiv:2304.07778, 2023.
8

--- Page 9 ---

[15] Jiahuan Cao, Dezhi Peng, Yongxin Shi, Zongyuan Jiang, and Lianwen Jin. Translating ancient Chinese to modern
Chinese at scale: A large language model-based approach. In Proc. ALT, pages 61–69, 2023.
[16] Dongbo Wang, Litao Lin, Zhixiao Zhao, Wenhao Ye, Kai Meng, Wenlong Sun, Lianzhen Zhao, Xue Zhao, Si Shen,
Wei Zhang, et al. EvaHan2023: Overview of the first international ancient Chinese translation bakeoff. In Proc.
ALT2023, pages 1–14, 2023.
[17] Zijing Ji, Yuxin Shen, Yining Sun, Tian Yu, and Xin Wang. C-CLUE: A benchmark of classical Chinese based on
a crowdsourcing system for knowledge graph construction. In Proc. CCKS, pages 295–301. Springer, 2021.
[18] Yixuan Zhang and Haonan Li. Can large langauge model comprehend ancient Chinese? A preliminary test on
aclue. In Proc. ALP, pages 80–87, 2023.
[19] Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N Gomez, Łukasz Kaiser, and
Illia Polosukhin. Attention is all you need. In Proc. NeurIPS, pages 6000–6010, 2017.
[20] Alec Radford, Karthik Narasimhan, Tim Salimans, Ilya Sutskever, et al. Improving language understanding by
generative pre-training. 2018.
[21] Jacob Devlin Ming-Wei Chang Kenton and Lee Kristina Toutanova. BERT: Pre-training of deep bidirectional
transformers for language understanding. In Proc. NAACL-HLT, volume 1, page 2, 2019.
[22] Long Ouyang, Jeffrey Wu, Xu Jiang, Diogo Almeida, Carroll Wainwright, Pamela Mishkin, Chong Zhang,
Sandhini Agarwal, Katarina Slama, Alex Gray, et al. Training language models to follow instructions with human
feedback. In Proc. NeurIPS, 2022.
[23] Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier Martinet, Marie-Anne Lachaux, Timothée Lacroix,
Baptiste Rozière, Naman Goyal, Eric Hambro, Faisal Azhar, et al. LLaMA: Open and efficient foundation
language models. arXiv preprint arXiv:2302.13971, 2023.
[24] Baolin Peng, Chunyuan Li, Pengcheng He, Michel Galley, and Jianfeng Gao. Instruction tuning with GPT-4.
arXiv preprint arXiv:2304.03277, 2023.
[25] Aohan Zeng, Xiao Liu, Zhengxiao Du, Zihan Wang, Hanyu Lai, Ming Ding, Zhuoyi Yang, Yifan Xu, Wendi
Zheng, Xiao Xia, et al. GLM-130B: An open bilingual pre-trained model. In Proc. ICLR, 2022.
[26] Zhengxiao Du, Yujie Qian, Xiao Liu, Ming Ding, Jiezhong Qiu, Zhilin Yang, and Jie Tang. GLM: General
language model pretraining with autoregressive blank infilling. In Proc. ACL, pages 320–335, 2022.
[27] Baichuan. Baichuan 2: Open large-scale language models. arXiv preprint arXiv:2309.10305, 2023.
[28] Jinze Bai, Shuai Bai, Yunfei Chu, Zeyu Cui, Kai Dang, Xiaodong Deng, Yang Fan, Wenbin Ge, Yu Han, Fei
Huang, et al. Qwen technical report. arXiv preprint arXiv:2309.16609, 2023.
[29] Hongyang Zhang, Muyun Yang, and Tiejun Zhao. Exploring hybrid character-words representational unit in
classical-to-modern Chinese machine translation. In Proc. IALP, pages 33–36. IEEE, 2015.
[30] Dongbo Wang, Chang Liu, Zhixiao Zhao, Si Shen, Liu Liu, Bin Li, Haotian Hu, Mengcheng Wu, Litao Lin, Xue
Zhao, et al. GujiBERT and GujiGPT: Construction of intelligent information processing foundation language
models for ancient texts. arXiv preprint arXiv:2307.05354, 2023.
[31] Liang Xu, Hai Hu, Xuanwei Zhang, Lu Li, Chenjie Cao, Yudong Li, Yechen Xu, Kai Sun, Dian Yu, Cong Yu,
Yin Tian, Qianqian Dong, Weitang Liu, Bo Shi, Yiming Cui, Junyi Li, Jun Zeng, Rongzhao Wang, Weijian Xie,
Yanting Li, Yina Patterson, Zuoyu Tian, Yiwen Zhang, He Zhou, Shaoweihua Liu, Zhe Zhao, Qipeng Zhao,
Cong Yue, Xinrui Zhang, Zhengliang Yang, Kyle Richardson, and Zhenzhong Lan. CLUE: A Chinese language
understanding evaluation benchmark. In Proc. COLING, pages 4762–4772, Barcelona, Spain (Online), December
2020. International Committee on Computational Linguistics.
[32] Yuan Yao, Qingxiu Dong, Jian Guan, Boxi Cao, Zhengyan Zhang, Chaojun Xiao, Xiaozhi Wang, Fanchao Qi,
Junwei Bao, Jinran Nie, et al. CUGE: A Chinese language understanding and generation evaluation benchmark.
arXiv preprint arXiv:2112.13610, 2021.
[33] Yuzhen Huang, Yuzhuo Bai, Zhihao Zhu, Junlei Zhang, Jinghan Zhang, Tangjun Su, Junteng Liu, Chuancheng
Lv, Yikai Zhang, Jiayi Lei, et al. C-Eval: A multi-level multi-discipline Chinese evaluation suite for foundation
models. arXiv preprint arXiv:2305.08322, 2023.
[34] Haonan Li, Yixuan Zhang, Fajri Koto, Yifei Yang, Hai Zhao, Yeyun Gong, Nan Duan, and Timothy Baldwin.
CMMLU: Measuring massive multitask language understanding in Chinese, 2023.
[35] Wanjun Zhong, Ruixiang Cui, Yiduo Guo, Yaobo Liang, Shuai Lu, Yanlin Wang, Amin Saied, Weizhu Chen, and
Nan Duan. AGIEval: A human-centric benchmark for evaluating foundation models, 2023.
9

--- Page 10 ---

[36] Kaijie Zhu, Jindong Wang, Jiaheng Zhou, Zichen Wang, Hao Chen, Yidong Wang, Linyi Yang, Wei Ye, Neil Zhen-
qiang Gong, Yue Zhang, et al. PromptBench: Towards evaluating the robustness of large language models on
adversarial prompts. arXiv preprint arXiv:2306.04528, 2023.
[37] Qinyuan Cheng, Tianxiang Sun, Wenwei Zhang, Siyin Wang, Xiangyang Liu, Mozhi Zhang, Junliang He, Mianqiu
Huang, Zhangyue Yin, Kai Chen, et al. Evaluating hallucinations in Chinese large language models. arXiv
preprint arXiv:2310.03368, 2023.
[38] Yue Xu, Fei Yin, Da-Han Wang, Xu-Yao Zhang, Zhaoxiang Zhang, and Cheng-Lin Liu. CASIA-AHCDB: A
large-scale Chinese ancient handwritten characters database. In Proc. ICDAR, pages 793–798. IEEE, 2019.
[39] Weihong Ma, Hesuo Zhang, Lianwen Jin, Sihang Wu, Jiapeng Wang, and Yongpan Wang. Joint layout analysis,
character detection and recognition for historical document digitization. In Proc. ICFHR, pages 31–36. IEEE,
2020.
[40] Rajkumar Saini, Derek Dobson, Jon Morrey, Marcus Liwicki, and Foteini Simistira Liwicki. ICDAR 2019
historical document reading challenge on large structured Chinese family records. In Proc. ICDAR, pages
1499–1504. IEEE, 2019.
[41] Hiuyi Cheng, Cheng Jian, Sihang Wu, and Lianwen Jin. Scut-cab: A new benchmark dataset of ancient Chinese
books with complex layouts for document layout analysis. In Proc. ICFHR, pages 436–451. Springer, 2022.
[42] Yongxin Shi, Chongyu Liu, Dezhi Peng, Cheng Jian, Jiarong Huang, and Lianwen Jin. M5HisDoc: A large-scale
multi-style Chinese historical document analysis benchmark. In Proc. NeurIPS Datasets and Benchmarks Track,
2023.
[43] Teven Le Scao, Angela Fan, Christopher Akiki, Ellie Pavlick, Suzana Ili´c, Daniel Hesslow, Roman Castagné,
Alexandra Sasha Luccioni, François Yvon, Matthias Gallé, et al. Bloom: A 176b-parameter open-access
multilingual language model. arXiv preprint arXiv:2211.05100, 2022.
[44] Tianxiang Sun, Xiaotian Zhang, Zhengfu He, Peng Li, Qinyuan Cheng, Hang Yan, Xiangyang Liu, Yunfan Shao,
Qiong Tang, Xingjian Zhao, Ke Chen, Yining Zheng, Zhejian Zhou, Ruixiao Li, Jun Zhan, Yunhua Zhou, Linyang
Li, Xiaogui Yang, Lingling Wu, Zhangyue Yin, Xuanjing Huang, and Xipeng Qiu. MOSS: Training conversational
language models from synthetic data. 2023.
[45] Zhengyan Zhang, Xu Han, Zhiyuan Liu, Xin Jiang, Maosong Sun, and Qun Liu. ERNIE: Enhanced language
representation with informative entities. In Proc. ACL, pages 1441–1451, 2019.
[46] iFLYTEK. Spark. https://xinghuo.xfyun.cn, 2023.
[47] MiniMax. abab5-chat. https://api.minimax.chat, 2023.
[48] Zhe Zhang, Jie Liu, Lihua Chi, and Xinhai Chen. Word-level BERT-CNN-RNN model for Chinese punctuation
restoration. In Proc. ICCC, pages 1629–1633, 2020.
[49] Pan Liu, Yanming Guo, Fenglei Wang, and Guohui Li. Chinese named entity recognition: The state of the art.
Neurocomputing, 473:37–53, 2022.
[50] Kishore Papineni, Salim Roukos, Todd Ward, and Wei-Jing Zhu. BLEU: a method for automatic evaluation of
machine translation. In Proc. ACL, pages 311–318, 2002.
[51] Yiming Cui, Ziqing Yang, and Xin Yao. Efficient and effective text encoding for Chinese LLaMA and Alpaca.
arXiv preprint arXiv:2304.08177, 2023.
10

```
