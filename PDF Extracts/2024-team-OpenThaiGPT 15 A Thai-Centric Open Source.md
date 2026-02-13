---
title: "2024-team-OpenThaiGPT 15 A Thai-Centric Open Source - PDF Extract"
source_pdf: "2024-team-OpenThaiGPT 15 A Thai-Centric Open Source.pdf"
pages: 8
extracted_at: "2026-02-13T09:15:42.547983"
---

# PDF Extract: 2024-team-OpenThaiGPT 15 A Thai-Centric Open Source

**Source PDF:** 2024-team-OpenThaiGPT 15 A Thai-Centric Open Source.pdf
**Total Pages:** 8

---

## Content

```
--- Page 1 ---

arXiv:2411.07238v2  [cs.CL]  25 Feb 2025
OpenThaiGPT 1.5: A Thai-Centric Open Source
Large Language Model
Sumeth Yuenyong∗
Department of Computer Engineering, Faculty of Engineering, Mahidol University
Kobkrit Viriyayudhakorn†
iApp Technology Co., Ltd.
Artiﬁcial Intelligence Entrepreneur Association of Thailand (AIEAT)
Apivadee Piyatumrong‡
Big Data Institute (Public Organization)
Jillaphat Jaroenkantasima§
Department of Electrical Engineering, Faculty of Engineering, Kasetsart University
November 2024
Abstract
OpenThaiGPT 1.5 is an advanced Thai language chat model based on Qwen v2.5, ﬁnetuned on
over 2,000,000 Thai instruction pairs. This report provides an engineering perspective on the model’s
development, capabilities, and performance. We discuss the model’s architecture, training process,
and key features, including multi-turn conversation support, Retrieval Augmented Generation (RAG)
compatibility, and tool-calling functionality. Benchmark results demonstrate OpenThaiGPT 1.5’s
state-of-the-art performance on various Thai language tasks, outperforming other open-source Thai
language models. We also address practical considerations such as GPU memory requirements and
deployment strategies.
1
Model Architecture and Training
1.1
Base Model
OpenThaiGPT 1.5 is built upon the Qwen v2.5 architecture [5], leveraging its advanced capabilities as
a foundation for Thai language modeling. The model is available in two sizes: 7 billion and 72 billion
parameters, catering to diﬀerent computational resource constraints and performance requirements. The
7B model was ﬁnetuned from Qwen/Qwen2.5-7B-Instruct on Huggingface, and the 72B model was ﬁne-
tuned from Qwen/Qwen2.5-72B-Instruct. Both base models have a vocabulary size of 152,064 and a
maximum input length of 32,768. Inspection of the tokenizers and initial experimentation revealed that
the Qwen 2.5 models already support the Thai language. For this reason, as well as due to the limitation
of our computing, we opted not to perform any continued pretraining of the model with Thai data and
start with instruction ﬁnetuning.
1.2
Finetuning Process
The model underwent extensive ﬁnetuning on a diverse dataset of over 2,000,000 Thai instruction pairs.
This process was crucial in adapting the base model to the nuances of the Thai language and culture,
enabling its eﬀectiveness in handling Thai-speciﬁc domain questions. We used the NeMo1 framework
∗sumeth.yue@mahidol.edu
†kobkrit@iapp.co.th
‡apivadee.pi@bdi.or.th
§autsadang41@gmail.com
1https://github.com/NVIDIA/NeMo
1

--- Page 2 ---

by Nvidia for ﬁnetuning. The 7B and 72B proposed models were trained using the LoRa technique [4].
The LoRa adaptor size r was 64, and α was 128. The learning rate was 1e−4. The global batch size
was 32. We used 10% of the ﬁnetuning data as a validation set and restored the checkpoint with the
lowest validation loss after training. Both models were trained on a server with 8x H100 GPUs, which
was kindly provided to us by SiamAI2.
1.2.1
Datasets
The ﬁnetuning dataset for OpenThaiGPT 1.5 comprises several high-quality, diverse Thai language
datasets:
• Thai Wiki Summary Dataset: A collection of 3,000 cleaned rows generated from Wikipedia,
focusing on summarization and information synthesis tasks.
• Thai QA Multi-turn Answer Dataset: This dataset contains 11,992 cleaned rows of multi-turn
question-answering conversations, enhancing the model’s ability to maintain context and generate
coherent responses across multiple interactions.
• Additional Proprietary Datasets: Supplementary over 30 datasets covering various domains
and task types, further enriching the model’s knowledge and capabilities.
• Synthetic Data: We used Llama 3.1 405B[3] to generate synthetic data by prompting it to create
variations of an existing instruction, generate counterfactual questions to existing facts, and to
form questions about Wikipedia articles.
• LLM as a Judge: After generating synthetic data, we used another instance of Llama 3.1 405B[3]
to review the quality of the generated data. We used in-context learning to inform the model of
examples of low and high-quality instruction-answer pairs. We ﬁltered the synthetic data to retain
only instruction-answer pairs that the model judged high-quality.
• English Data: We would like the model to be English-Thai bilingual. Therefore, to alleviate
catastrophic forgetting of English, we mixed in about 20% of English data from various datasets
on Huggingface such as: yahma/alpaca-cleaned, OpenAssistant/oasst1, and (a subset of) Open-
Orca/OpenOrca.
These datasets were carefully curated and processed to ensure high-quality training data, contributing
to the model’s robust performance across a wide range of Thai language tasks and domains.
1.3
Alignment and Safety
We created a safety net for Reinforcement Learning from Human Feedback (RLHF) [6] to ensure the
model does not generate or respond to rude or socially sensitive topics.
Our approach began with
compiling a list of impolite words and sensitive subjects to which the model should refuse to answer.
We manually wrote examples that included these words and addressed sensitive issues. Additionally,
we employed techniques such as Easy Data Augmentation [11] to enhance our dataset, and we also
experimented with jailbreaking [12] some open-weight LLMs to generate more of this data locally and
oﬀ-line. In total, we constructed around 5,000 records of alignment data and aligned the model using
Direct Preference Optimization (DPO) [9], accessible through the model aligner module of NeMo.
2
Key Features
The ﬁnetuning process preserved all the key features of Qwen2.5.
2.1
Multi-turn Conversation Support
OpenThaiGPT 1.5 preserved multi-turn conversation capability by having around 30% of the instruc-
tion ﬁnetuning dataset consist of multi-turn conversations. This allows for more natural and coherent
dialogues. This feature is essential for applications requiring extended interactions, such as customer
support or interactive learning systems.
2https://siam.ai/
2

--- Page 3 ---

2.2
Retrieval Augmented Generation (RAG)
The model supports RAG, enabling it to incorporate external knowledge sources during response gen-
eration.
This feature signiﬁcantly enhances the model’s ability to provide accurate and up-to-date
information, making it suitable for applications requiring access to large, dynamic knowledge bases.
2.3
Tool Calling Support
OpenThaiGPT 1.5 includes a tool-calling feature that allows it to execute predeﬁned functions or make
API calls based on user queries. This capability extends the model’s functionality beyond text generation,
enabling it to perform tasks such as retrieving real-time data or interacting with external systems.
2.4
Extended Context Handling
The model can process up to 131,072 input tokens and generate up to 8,192 tokens, allowing for detailed
and complex interactions. This extended context window is particularly useful for tasks requiring the
analysis of long documents or generating comprehensive responses.
3
Performance and Benchmarks
3.1
Evaluation Dataset
3.1.1
OpenThaiGPT Evaluation Dataset
We introduce the OpenThaiGPT Evaluation Dataset
¯
, a comprehensive collection of Thai-language bench-
mark exams that we developed to evaluate language models’ performance across various educational and
professional domains. This novel dataset comprises multiple standardized tests and specialized assess-
ments:
• Academic Standardized Tests:
– A-Level exams (2021-2022) covering Applied Mathematics, Biology, English, and Social Stud-
ies
– ONET M3 (Grade 9) and M6 (Grade 12) exams from 2021-2025, including subjects like Thai,
Mathematics, Social Studies, Science, and English
– TGAT (Thai General Aptitude Test) focusing on Critical Thinking
– TPAT1 (Thai Professional Aptitude Test) emphasizing Medical Ethics
• Professional Certiﬁcations:
– Thai Investment Consultant Licensing Exams (IC Plain, IC Complex P2, P3)[10]
• Natural Language Understanding Benchmarks:
– Facebook Belebele Thai[1]
– XCOPA Thai for cross-lingual transfer learning[8]
– XNLI 2.0 Thai for cross-lingual natural language inference[2]
The dataset features multiple-choice questions with veriﬁed answers, and includes additional anno-
tations such as answerability ﬂags and solution type indicators. All content has been veriﬁed by Thai
speakers and is distributed under the Apache-2.0 License. The evaluation framework provides a rigorous
testing environment for assessing Thai language models’ capabilities across academic knowledge, profes-
sional expertise, and general language understanding. The dataset is open-source and publicly available
at Huggingface3, enabling researchers and developers to evaluate and compare diﬀerent Thai language
models using standardized benchmarks.
3https://huggingface.co/datasets/openthaigpt/openthaigpt_eval
3

--- Page 4 ---

3.1.2
Thai Exam Benchmark
The Thai Exam Benchmark[7] is a comprehensive evaluation dataset designed to assess language models’
performance on Thai educational and professional examinations. It consists of multiple-choice questions
from various Thai national examinations including ONET (Ordinary National Educational Test), IC
(Investment Consultant), TGAT (Thai General Aptitude Test), TPAT-1 (Thai Professional Aptitude
Test), and A-Level exams. This benchmark provides a rigorous test of both language understanding and
domain-speciﬁc knowledge across academic and professional contexts.
3.1.3
M3Exam
The M3Exam[13] is a multilingual, multimodal, and multilevel benchmark for evaluating the capabilities
of large language models. It includes questions from various domains, including science, mathematics,
and social studies, and is designed to test the model’s understanding of context, reasoning, and knowledge
application.
3.2
Evaluation Results
OpenThaiGPT 1.5 has been evaluated on these three datasets. The results demonstrate the model’s
superior performance compared to other open-source Thai language models.
Table 1: Performance Comparison of Diﬀerent Language Models in the 7B - 8B sizes on OpenThaiGPT
Evaluation Dataset
Exam Name
Llama-3.1-8B
Typhoon-v1.5x-8b
Qwen2.5-7B
OpenThaiGPT1.5-7b
Correct
%
Correct
%
Correct
%
Correct
%
A Level
57/120
47.50
56/120
46.67
70/120
58.33
72/120
60.00
TGAT
18/50
36.00
16/50
32.00
16/50
32.00
18/50
36.00
TPAT1
22/40
55.00
21/40
52.50
23/40
57.50
23/40
57.50
Investment Consult
12/25
48.00
14/25
56.00
17/25
68.00
19/25
76.00
Facebook Beleble TH
146/200
73.00
156/200
78.00
158/200
79.00
162/200
81.00
XCOPA TH
138/200
69.00
159/200
79.50
161/200
80.50
162/200
81.00
XNLI 2.0 TH
110/200
55.00
113/200
56.50
106/200
53.00
109/200
54.50
O-NET M3 Thai
8/25
32.00
12/25
48.00
18/25
72.00
16/25
64.00
O-NET M3 Thai
10/20
50.00
15/20
75.00
18/20
90.00
16/20
80.00
O-NET M3 Math
3/16
18.75
4/16
25.00
5/16
31.25
5/16
31.25
O-NET M3 Science
11/26
42.31
12/26
46.15
12/26
46.15
12/26
46.15
O-NET M3 English
23/30
76.67
21/30
70.00
26/30
86.67
25/30
83.33
O-NET M6 Thai
19/65
29.23
31/65
47.69
30/65
46.15
35/65
53.85
O-NET M6 Math
3/17
17.65
5/17
29.41
5/17
29.41
5/17
29.41
O-NET M6 Social
24/55
43.64
28/55
50.91
31/55
56.36
32/55
58.18
O-NET M6 Science
9/28
32.14
12/28
42.86
16/28
57.14
16/28
57.14
O-NET M6 English
37/52
71.15
34/52
65.38
41/52
78.85
42/52
80.77
Total/Average
650/1169
55.60
709/1169
60.65
753/1169
64.41
769/1169
65.78
For the Thai Exam Benchmark and M3Exam, OpenThaiGPT 1.5 (72B) achieved a score of 63.89%
and 70.39% respectively, outperforming several other large language models, including some closed API-
only models:
These benchmark results highlight OpenThaiGPT 1.5’s strong performance in Thai language under-
standing and generation tasks, positioning it as a leading option for Thai language AI applications.
4
Conclusion
We have developed and released OpenThaiGPT version 1.5 on Huggingface at openthaigpt/openthaigpt1.5-
{size}b-instruct where {size} are 7, 14 or 72. There are based on Qwen2.5 family of models. Extensive
experiments on Thai exams data showed that OpenThaiGPT1.5 is currently the most capable open
model for the Thai language.
4

--- Page 5 ---

Table 2: Performance Comparison of Diﬀerent Language Models in the 14B sizes on OpenThaiGPT
Evaluation Dataset. Note that there are no 14B sized models for Llama-3.1 and Typhoon-v1.5x.
Qwen2.5-14B
OpenThaiGPT1.5-14b
Exam Name
Score
Total
%
Score
Total
%
A Level
74
120
61.67
78
120
65.00
TGAT
22
50
44.00
25
50
50.00
TPAT1
24
40
60.00
21
40
52.50
Investment Consult
19
25
76.00
18
25
72.00
Facebook Beleble TH
169
200
84.50
174
200
87.00
XCOPA TH
170
200
85.00
173
200
86.50
XNLI 2.0 TH
139
200
69.50
129
200
64.50
O-NET M3 Thai
19
25
76.00
21
25
84.00
O-NET M3 Social
18
20
90.00
18
20
90.00
O-NET M3 Math
7
16
43.75
2
16
12.50
O-NET M3 Science
13
26
50.00
14
26
53.85
O-NET M3 English
28
30
93.33
28
30
93.33
O-NET M6 Thai
34
65
52.31
37
65
56.92
O-NET M6 Math
4
17
23.53
7
17
41.18
O-NET M6 Social
33
55
60.00
34
55
61.82
O-NET M6 Science
14
28
50.00
16
28
57.14
O-NET M6 English
43
52
82.69
41
52
78.85
Total/Average
830
1169
71.09
836
1169
71.51
Table 3: Performance Comparison of Diﬀerent Language Models in the 70B - 72B sizes on OpenThaiGPT
Evaluation Dataset
Exam Name
Llama-3.1-70B
Llama-3-typhoon
Qwen2.5-72B
OpenThaiGPT1.5-72B
Correct
%
Correct
%
Correct
%
Correct
%
A Level
74/120
61.67
71/120
59.17
90/120
75.00
92/120
76.67
TGAT
20/50
40.00
23/50
46.00
24/50
48.00
23/50
46.00
TPAT1
20/40
50.00
21/40
52.50
22/40
55.00
22/40
55.00
Investment Consult
13/25
52.00
15/25
60.00
20/25
80.00
18/25
72.00
Facebook Beleble TH
176/200
88.00
175/200
87.50
180/200
90.00
180/200
90.00
XCOPA TH
171/200
85.50
169/200
84.50
180/200
90.00
181/200
90.50
XNLI 2.0 TH
126/200
63.00
125/200
62.50
131/200
65.50
141/200
70.50
O-NET M3 Thai
14/25
56.00
19/25
76.00
19/25
76.00
21/25
84.00
O-NET M3 Social
19/20
95.00
19/20
95.00
18/20
90.00
19/20
95.00
O-NET M3 Math
4/16
25.00
7/16
43.75
6/16
37.50
6/16
37.50
O-NET M3 Science
16/26
61.54
14/26
53.85
17/26
65.38
19/26
73.08
O-NET M3 English
28/30
93.33
28/30
93.33
29/30
96.67
29/30
96.67
O-NET M6 Thai
39/65
60.00
36/65
55.38
39/65
60.00
37/65
56.92
O-NET M6 Math
10/17
58.82
7/17
41.18
4/17
23.53
7/17
41.18
O-NET M6 Social
42/55
76.36
37/55
67.27
35/55
63.64
36/55
65.45
O-NET M6 Science
16/28
57.14
14/28
50.00
18/28
64.29
19/28
67.86
O-NET M6 English
43/52
82.69
38/52
73.08
45/52
86.54
47/52
90.38
Total/Average
831/1169
71.09
818/1169
69.97
877/1169
75.02
897/1169
76.73
5

--- Page 6 ---

Model
Average Score
Thai Exam Score
M3Exam Score
Claude 3.5 Sonnet (2024-06-20)
68.41%
69.2%
67.62%
OpenThaiGPT 1.5 72B
67.14%
63.89%
70.39%
GPT-4o (2023-05-13)
66.26%
63.89%
68.63%
Qwen2.5 72B Instruct
63.43%
60.53%
66.33%
OpenThaiGPT 1.5 14B
60.41%
58.41%
62.41%
Meta Llama 3.1 70B Instruct
59.38%
58.23%
60.52%
Llama 3 Typhoon v1.5x 70b Instruct
59.34%
58.76%
59.92%
OpenThaiGPT 1.5 7B
53.03%
52.04%
54.01%
Table 4: Benchmark Results on the Thai Exam Benchmark and the M3Exam.
References
[1] L. Bandarkar, D. Liang, B. Muller, M. Artetxe, S. N. Shukla, D. Husa, N. Goyal, A. Krishnan,
L. Zettlemoyer, and M. Khabsa. The belebele benchmark: a parallel reading comprehension dataset
in 122 language variants. In Proceedings of the 62nd Annual Meeting of the Association for Com-
putational Linguistics (Volume 1: Long Papers), pages 749–775, Bangkok, Thailand and virtual
meeting, Aug. 2024. Association for Computational Linguistics.
[2] A. Conneau, R. Rinott, G. Lample, A. Williams, S. R. Bowman, H. Schwenk, and V. Stoyanov.
Xnli: Evaluating cross-lingual sentence representations.
In Proceedings of the 2018 Conference
on Empirical Methods in Natural Language Processing. Association for Computational Linguistics,
2018.
[3] A. Dubey, A. Jauhri, A. Pandey, A. Kadian, A. Al-Dahle, A. Letman, A. Mathur, A. Schelten,
A. Yang, A. Fan, et al. The llama 3 herd of models. arXiv preprint arXiv:2407.21783, 2024.
[4] E. J. Hu, Y. Shen, P. Wallis, Z. Allen-Zhu, Y. Li, S. Wang, L. Wang, and W. Chen. Lora: Low-rank
adaptation of large language models. arXiv preprint arXiv:2106.09685, 2021.
[5] B. Hui, J. Yang, Z. Cui, J. Yang, D. Liu, L. Zhang, T. Liu, J. Zhang, B. Yu, K. Dang, et al. Qwen2.
5-coder technical report. arXiv preprint arXiv:2409.12186, 2024.
[6] L. Ouyang, J. Wu, X. Jiang, D. Almeida, C. Wainwright, P. Mishkin, C. Zhang, S. Agarwal,
K. Slama, A. Ray, et al. Training language models to follow instructions with human feedback.
Advances in neural information processing systems, 35:27730–27744, 2022.
[7] K.
Pipatanakul,
P.
Jirabovonvisut,
P.
Manakul,
S.
Sripaisarnmongkol,
R.
Patomwong,
P. Chokchainant, and K. Tharnpipitchai. Typhoon: Thai large language models. arXiv preprint
arXiv:2312.13951, 2023.
[8] E. M. Ponti, G. Glavaˇs, O. Majewska, Q. Liu, I. Vuli´c, and A. Korhonen. Xcopa: A multilingual
dataset for causal commonsense reasoning. arXiv preprint arXiv:2005.00333, 2020.
[9] R. Rafailov, A. Sharma, E. Mitchell, C. D. Manning, S. Ermon, and C. Finn. Direct preference
optimization: Your language model is secretly a reward model. Advances in Neural Information
Processing Systems, 36, 2024.
[10] Stock Exchange of Thailand. General investment advisor course. Accessed on November 7, 2024.
[11] J. Wei and K. Zou. Eda: Easy data augmentation techniques for boosting performance on text
classiﬁcation tasks. In Proceedings of the 2019 Conference on Empirical Methods in Natural Language
Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-
IJCNLP), pages 6382–6388, 2019.
[12] Z. Xu, Y. Liu, G. Deng, Y. Li, and S. Picek. A comprehensive study of jailbreak attack versus
defense for large language models. In Findings of the Association for Computational Linguistics
ACL 2024, pages 7432–7449, 2024.
[13] W. Zhang, M. Aljunied, C. Gao, Y. K. Chia, and L. Bing. M3exam: A multilingual, multimodal,
multilevel benchmark for examining large language models. Advances in Neural Information Pro-
cessing Systems, 36:5484–5505, 2023.
6

--- Page 7 ---

A
OpenThaiGPT Evaluation Dataset Examples
Here are some examples from the OpenThaiGPT Evaluation Dataset.
Example 1: Investment Consultant Exam
Mr. A purchased units of Mutual Fund A at a price of 10.20 baht per unit. One year later,
he sold those units at a price of 10.50 baht per unit. During the year, the mutual fund paid
a dividend of 0.30 baht per unit. What is the rate of return that Mr. A received from his
investment in Mutual Fund A? (Do not consider tax liabilities and other expenses incurred
from investing in Mutual Fund A.)
• (1) 2.94%
• (2) 5.71%
• (3) 5.88%
• (4) 6.00%
(3) is the correct answer.
Example 2: O-NET M6 Thai Language
Which situation matches the meaning of the Thai idiom ”pointing at a bird on a branch tip”
(meaning to have unrealistic expectations or false hopes)?
• (1) Somsak was disappointed to receive only an honorable mention in the essay contest,
saying he shouldn’t have pointed at a bird on a branch tip
• (2) Somsri studied very hard but still ranked only third in class; this is what they call
pointing at a bird on a branch tip
• (3) Somjit has been hinting to her mother several times that she wants a mobile phone,
hoping her mother will buy it after exams; Somjit is pointing at a bird on a branch tip
• (4) Somjai received a sum of prize money and invited friends to go shopping for pretty
clothes, saying now she can ﬁnally point at a bird on a branch tip
• (5) Somying keeps pestering her father for a car even though she’s still in junior high
school; this is called pointing at a bird on a branch tip
(5) is the correct answer.
Example 3: O-NET M6 Social Studies
When OPEC announced a reduction in oil production, causing global oil prices to rise, it
aﬀected the gasoline market, which is considered an essential commodity in Thailand. The
domestic retail price of gasoline increased signiﬁcantly, impacting people’s lives in the country.
Given this situation, if the government wants to help gasoline consumers, which measure
should the government implement?
• (1) Set the gasoline price at equilibrium
• (2) Establish lower production quotas for gasoline
• (3) Set a price ceiling in the gasoline market
• (4) Set a price ﬂoor in the gasoline market
• (5) Set minimum wages in the oil production industry
(3) is the correct answer.
Example 4: O-NET M6 Science
A man with blood type AB and color blindness marries a woman with blood type O and
normal vision (no family history of color blindness). They have three children together - one
daughter and two sons. Which statement is correct?
• (1) Both sons have normal vision
7

--- Page 8 ---

• (2) The children will have either blood type AB or O
• (3) If they have another child, it will be female
• (4) All three children can donate blood to their mother
• (5) The daughter may or may not be a carrier of color blindness
(1) is the correct answer.
Example 5: O-NET M6 Mathematics
Given that the proposition ”If Manee studies hard then Manee passes the exam” is false,
and ”Manee is class president or Manee passes the exam” is true, which of the following
propositions must be true?
• (1) Manee doesn’t study hard or passes the exam
• (2) Manee passes the exam and is not class president
• (3) Manee studies hard if and only if Manee passes the exam
• (4) If Manee is class president then Manee doesn’t study hard
• (5) Manee is class president if and only if Manee fails the exam
(5) is the correct answer.
Example 6: Facebook Beleble Thai[1]
Let your hands be as relaxed as possible while still playing all the notes correctly. Try not
to move your ﬁngers unnecessarily. This method will minimize the fatigue you experience.
Remember that you don’t need to press the keys harder to make the sound louder like a
piano. If you want to increase the volume of the accordion, use more pressure or speed with
the bellows.
Which of the following is NOT a correct tip for successfully playing the accordion?
• (1) To make the sound louder, increase pressure when playing the notes
• (2) Try not to move ﬁngers excessively to avoid using too much force
• (3) Be careful when playing notes while keeping hands as relaxed as possible
• (4) Increase the bellows speed to make the sound louder
(1) is the correct answer.
B
Our Links
Oﬃcial Website:
https://openthaigpt.aieat.or.th/
See our project on GitHub:
https://github.com/orgs/OpenThaiGPT/repositories
Hugging faces:
https://huggingface.co/openthaigpt
8

```
