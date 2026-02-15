---
title: "2025-Cao-Measuring Hong Kong Massive Multi-Task Language Understanding HKMMLU - PDF Extract"
source_pdf: "2025-Cao-Measuring Hong Kong Massive Multi-Task Language Understanding HKMMLU.pdf"
pages: 30
extracted_at: "2026-02-15T17:51:59.122222"
---

# PDF Extract: 2025-Cao-Measuring Hong Kong Massive Multi-Task Language Understanding HKMMLU

**Source PDF:** 2025-Cao-Measuring Hong Kong Massive Multi-Task Language Understanding HKMMLU.pdf
**Total Pages:** 30

---

## Content

```
--- Page 1 ---

Preprint. Under review.
Measuring Hong Kong Massive Multi-Task
Language Understanding
Chuxue Cao1∗, Zhenghao Zhu1∗, Junqi Zhu1, Guoying Lu1, Siyu Peng1,
Juntao Dai2, Weijie Shi1, Sirui Han1†, Yike Guo1†
1Hong Kong University of Science and Technology, 2Peking University,
ccaoai@connect.ust.hk
Abstract
Multilingual understanding is crucial for the cross-cultural applicability
of Large Language Models (LLMs). However, evaluation benchmarks
designed for Hong Kong’s unique linguistic landscape, which combines
Traditional Chinese script with Cantonese as the spoken form and its cul-
tural context, remain underdeveloped. To address this gap, we introduce
HKMMLU, a multi-task language understanding benchmark that evalu-
ates Hong Kong’s linguistic competence and socio-cultural knowledge.
The HKMMLU includes 26,698 multi-choice questions across 66 subjects,
organized into four categories: Science, Technology, Engineering, and Math-
ematics (STEM), Social Sciences, Humanities, and Other. To evaluate the
multilingual understanding ability of LLMs, 90,550 Mandarin-Cantonese
translation tasks were additionally included. We conduct comprehensive
experiments on GPT-4o, Claude 3.7 Sonnet, and 18 open-source LLMs of
varying sizes on HKMMLU. The results show that the best-performing
model, DeepSeek-V3, struggles to achieve an accuracy of 75%, significantly
lower than that of MMLU and CMMLU. This performance gap highlights
the need to improve LLMs’ capabilities in Hong Kong-specific language
and knowledge domains. Furthermore, we investigate how question lan-
guage, model size, prompting strategies, and question and reasoning token
lengths affect model performance. We anticipate that HKMMLU will signifi-
cantly advance the development of LLMs in multilingual and cross-cultural
contexts, thereby enabling broader and more impactful applications. 1
1
Introduction
Large Language Models (LLMs) such as GPT-4o, Claude 3.7 Sonnet, and Qwen-2.5 have
garnered significant attention across various industries for their remarkable capability in
various disciplines (OpenAI, 2024; Anthropic, 2025; Yang et al., 2025). Benchmarks have been
developed to evaluate their performance and analyze their limitations (Hendrycks et al.,
2021a; Huang et al., 2023; Chen et al., 2024). Massive Multitask Language Understanding
(MMLU) (Hendrycks et al., 2021a) is a widely used English benchmark that evaluates LLMs
across various subjects through multi-choice questions. Subsequently, similar studies have
tried to extend MMLU to additional languages and regions, including Chinese (Li et al.,
2024; Tam et al., 2024; Chen et al., 2024; Hsu et al., 2023), Korean (Son et al., 2024), Indonesian
and Spanish (Wang et al., 2024).
While benchmarks have been developed to evaluate models in the context of Chinese
across various subjects, they are present in Simplified Chinese or Traditional Chinese (Tai-
wan) (Li et al., 2024; Huang et al., 2023; Hsu et al., 2023; Tam et al., 2024; Chen et al., 2024).
Consequently, challenges exist in evaluating knowledge and language specific to Hong
Kong: (1) Hong Kong’s socio-cultural uniqueness stems from its “One Country, Two Sys-
tems” policy and multicultural identity, blending local traditions and Western influences.
*Equal contribution. †Corresponding authors.
1The data are available at https://huggingface.co/datasets/chuxuecao/HKMMLU
1
arXiv:2505.02177v1  [cs.CL]  4 May 2025

--- Page 2 ---

Preprint. Under review.
HKMMLU
STEM
23%
6158
DSE 
Mathematics
DSE Physics
DSE 
Chemistry
DSE Biology
Organic 
Chemistry
Basic Medical 
Science
Statistics and 
Machine 
Learning
...
Optometry
Pharmacy
HK Law
HK History
HK Literature
HK Party 
Politics
HK Education
HK Politicians 
& Events
HK Celebrity
HK 
Government & 
Political System
Human 
Behavior
HK Cultural 
Art
HK Party 
Politics
DSE Geography
DSE Economics
DSE Tourism
DSE Intro to 
Accounting
 & Finance
HK Physical 
Geography
HK Urban and 
Regional 
Development
...
...
...
HK Film and 
Televison
HK Life 
Knowledge
HK Events and 
Festivals
HK 
Entertainment  
Management
HK
Transportation
Science and 
Technology 
Commonsense
HK Livelihood
Social 
Commonsense
Culture 
Commonsense
HK Human 
Geography
Chinese History
HK Society
HK Current 
Affairs
Other
25.5%
6802
Social 
Sciences
18.1%
4834
Humanities
33.4%
8904
作爲一個精通香港繁體字和香港時事的專家，請完成以下繁體中文單選題。
勞工處公佈於6月3日公佈新修訂《颱風及暴雨警告下工作守則》，內容包括除必要人員
外，僱員在八號颱風警告取消後兩小時，應留在原來地點，而非立即啓程上班。有關指引
是以下哪一項？
(A) 危險情況 (
) 
(B) 極端情況 (
) 
(C) 突發情況 (
) 
(D) 意外情況 (
)
(As an expert proficient in Hong Kong traditional Chinese characters 
and current affairs, please complete the following multi-choice question in 
traditional Chinese.)
(The Labour Department announced on June 3 the newly revised "Code of 
Practice for Working in Typhoon and Rainstorm Warnings," which states that, 
except for essential personnel, employees should remain at their original 
location for two hours after the cancellation of the No. 8 typhoon warning, 
rather than immediately heading to work. Which of the following guidelines 
does this relate to?)
Dangerous situations
Extreme situations
Emergency situations
Accidental situations
Example Question on HK Current Affairs
Figure 1: Overview of HKMMLU subject (partial) with an illustrative task example and
bilingual English translations for clarity.
However, CMMLU and C-Eval (Li et al., 2024; Huang et al., 2023) focus on generalized
Chinese contexts, neglecting Hong Kong’s distinct legal systems, historical narratives, and
socio-linguistic practices. Consequently, these frameworks fail to evaluate LLMs’ abil-
ity to understand region-specific knowledge and reasoning in multicultural scenarios; (2)
Hong Kong Cantonese, as a spoken language, diverges markedly from the Mandarin-based
written standard in Traditional Chinese script, preserving archaic grammar and regional
vocabulary (Cheng & Tang, 2014), and cannot be directly translated word-for-word from
Mandarin Chinese text. While TMMLU+ and TMLU (Tam et al., 2024; Chen et al., 2024)
evaluate the Traditional Chinese understanding capabilities of LLMs, the proficiency of
language models in capturing Cantonese literary expression remains uncertain.
To address these challenges, we introduce the Hong Kong Massive Multi-Task Language
Understanding (HKMMLU) benchmark (Figure 1), specifically designed to evaluate LLMs
in the unique linguistic and cultural context of Hong Kong. The benchmark consists of two
parts: (1) a comprehensive knowledge base for Hong Kong consisting of 26,698 questions,
divided into four categories: Science, Technology, Engineering, and Mathematics (STEM),
Humanities, Social Sciences, and Other; (2) translation tasks for Cantonese, including 90,550
instances, with half of the translations from Mandarin to Cantonese and the other half in
the opposite direction.
We evaluated GPT-4o, Claude 3.7 Sonnet, and 18 open-source LLMs across various model
sizes using the HKMMLU benchmark. The results indicate that all models lack adequate
knowledge about Hong Kong and Traditional Chinese, especially Cantonese, failing to
achieve an accuracy of 75%. For a deeper insight into the proficiency of the models in
Cantonese literacy expression, we conducted experiments on translation tasks. The ex-
perimental results show that models performed better in Cantonese-to-Mandarin than in
Mandarin-to-Cantonese, with Llama-3-Taiwan-70B-Instruct having the smallest gap. These
findings underscore the importance of ongoing enhancement of Traditional Chinese and
Hong Kong knowledge understanding abilities.
Furthermore, our extensive experiments reveal that: (1) After translating HKMMLU to
Simplified Chinese, the models exhibit a slight decrease in accuracy, with the average
accuracy of all models dropping from 57% to 56.7%. (2) Chain-of-thought (CoT) prompting
improves model performance in STEM. Providing reasoning examples in the prompts
further enhances model performance significantly in STEM and slightly in Social Sciences.
(3) Few-shot prompting does not always enhance model performance. (4) Models with
larger parameters within the same series tend to achieve higher accuracy. (5) When the
question token length exceeds 600, the accuracy of most open-source models begins to
2

--- Page 3 ---

Preprint. Under review.
decline, whereas the accuracy of closed-source models tends to improve. Additionally,
the length of reasoning tokens is negatively correlated with model performance. (6) We
also conducted a human testing experiment involving 100 Hong Kong-specific questions.
Even the top-performing model, DeepSeek-V3, failed to surpass human test-takers with a
post-secondary degree, particularly on questions written in Cantonese.
2
Related Work
Benchmarks are crucial for evaluating LLM capabilities, with many emerging to assess
performance across various skills and subjects. For example, MATH (Hendrycks et al.,
2021b) and GSM8K (Cobbe et al., 2021) evaluated the mathematical ability of language mod-
els. Benchmarks like AI2 (Clark et al., 2018), CommonsenseQA (Talmor et al., 2019), and
Winogrande (Sakaguchi et al., 2021) introduced the evaluation of commonsense reasoning.
There are also benchmarks specifically designed to evaluate the reading comprehension (Ra-
jpurkar et al., 2018; Kwiatkowski et al., 2019; Li et al., 2022) and code generation capabilities
of LLMs (Chen et al., 2021; Austin et al., 2021).
Besides evaluating the basic skills of LLMs, researchers have focused on different languages.
In the early stages, benchmarks like GLUE (Wang et al., 2018) and SuperGLUE (Wang
et al., 2019) have emerged for evaluating English natural language understanding. Ad-
ditionally, numerous evaluation benchmarks for Chinese languages have been proposed,
including SuperCLUE (Xu et al., 2023) for natural language understanding, CMATH (Wei
et al., 2023) for elementary school math, and MMCU (Zeng, 2023) for medicine and educa-
tion. Notably, ACLUE (Zhang & Li, 2023) evaluates ancient Chinese language ability, and
AGIEVAL (Zhong et al., 2024) offers evaluation in both Chinese and English for various
standardized competitions and exams. In addition, several Traditional Chinese Bench-
marks, such as DRCD (Shao et al., 2019) and TTQA (Ennen et al., 2023), assess reading
comprehension and local commonsense knowledge in Taiwan.
Large-scale multitask evaluation benchmarks were introduced to provide a more compre-
hensive evaluation of LLMs. One prominent example is MMLU (Hendrycks et al., 2021a),
an English-only, multi-domain evaluation benchmark. After that, Simplified-Chinese bench-
marks, such as CMMLU (Li et al., 2024) and C-EVAL (Huang et al., 2023), were developed
for Chinese-specific subjects, while M3KE (Liu et al., 2023) mainly focuses on the Chinese
education sector. In addition, TMMLU (Hsu et al., 2023) and TMMLU+ (Tam et al., 2024)
evaluate model performance in a Traditional Chinese context. Furthermore, benchmarks
like KMMLU (Son et al., 2024) address the Korean language and local knowledge, while
Cross-MMLU (Wang et al., 2024) integrates multiple languages and cultural perspectives.
While these Chinese benchmarks generally evaluate models across various subjects in hu-
man society, they primarily focus on Simplified Chinese or Traditional Chinese (Taiwan),
which differs from the language system used in Hong Kong, particularly Cantonese. Al-
though HKCanto-Eval (Cheng et al., 2025) has developed a Cantonese Benchmark, 78.4% of
its multi-choice tasks are translated from MMLU, with few tasks focusing on Hong Kong
socio-culture. In contrast, most HKMMLU data is sourced from materials specific to Hong
Kong, covering 23 subjects (14,912 data points), including topics such as Hong Kong Party
Politics and Hong Kong Law.
3
HKMMLU
Task Overview We introduce HKMMLU, a benchmark for evaluating the Traditional Chi-
nese understanding and reasoning capabilities of LLMs. The benchmark covers diverse
areas of knowledge, including the STEM, Social Sciences, Humanities, and Other domains.
Except for non-region-specific subjects like mathematics, biology, and physics, the HK-
MMLU includes a wide range of Hong Kong-specific questions, such as physical geography,
history, and law of Hong Kong. These questions evaluate Hong Kong-related knowledge of
LLMs. Additionally, it features a Cantonese-Mandarin translation task.
Data Collection We collected multi-choice questions from primary and secondary school
exams, Hong Kong Diploma of Secondary Education Examination (HKDSE), Hong Kong
3

--- Page 4 ---

Preprint. Under review.
Knowledge Challenge questions, civic quiz competition questions, and so on, all of which
have undergone rigorous manual annotation and selection. We also included some non-
Taiwan-related questions from the TMMLU+, which constitutes 30.6% of HKMMLU. Taiwan
Traditional Chinese characters are converted to Hong Kong Traditional Chinese characters
using OpenCC (Kuo, 2024). Additionally, we created the translation task manually.
Data Processing Each question is presented in a multi-choice format with two to three
answer options. An example of our multi-choice question is shown in Figure 1. For questions
without a subject during collection, we used three LLMs for labeling, including DeepSeek-
V3 (DeepSeek-AI et al., 2025), GPT-4o (OpenAI, 2024) and Qwen-2.5-72B-Instruct (Yang
et al., 2025), and applied a majority voting approach. For each subject, one data sample was
annotated using o3-mini (OpenAI, 2025) to generate a reasoning process.
Quality Control To ensure the accuracy of labeling, we have manually checked 200 labels,
and the accuracy rate is 96%. For multi-choice questions that are converted from question-
answer pairs, we have leveraged three processing models, including GPT-4o, DeepSeek-V3,
and Claude 3.7 Sonnet, with a processing ratio of 1:1:1 for fairness. To secure the quality, we
have manually checked 100 questions processed by each LLM; the accuracy rate is 97.7%.
Data Statistics The HKMMLU dataset consists of four main categories: STEM, Humanities,
Social Sciences, and Other, with a total of 66 sub-tasks and 26,698 data points. Figure 2
illustrates that the token length of most multi-choice questions ranges from 30 to 200, with
the STEM category featuring relatively longer questions. Figure 3 displays the distribution
of sentence token lengths, indicating that Cantonese expressions tend to have slightly longer
tokens due to the characteristics of the language. Refer to Table 6 and Table 5 for detailed
statistical results and subject information for HKMMLU.
0
100
200
300
400
Tokens Length
0
200
400
600
800
1000
1200
1400
1600
Frequency
STEM
Soc. Sci
Humanities
Other
Figure 2: Question (include choices) token
length distribution of multi-choice questions
in HKMMLU.
0
20
40
60
80
100
120
Tokens Length
0
2000
4000
6000
8000
Frequency
Cantonese
Mandarin
Figure 3: Token length distribution of Can-
tonese and Mandarin sentences of transla-
tion tasks in HKMMLU.
4
Experiments
Setup For multi-choice tasks, we evaluate the model in the following methods: 1) Direct
Answer Evaluation: Models are prompted with questions directly; 2) CoT Evaluation:
Models are asked to provide a reasoning process before giving their final answer; 3) Few-
shot Evaluation: Models are provided with several question answering examples before
the question; 4) 1-shot CoT Evaluation: A reasoning process for the example question is
presented prior to the question. We use regular expressions to extract the answers and
calculate the percentage of correct answers. For translation tasks, we directly prompt the
LLM to translate the sentences and utilize BLEU (Papineni et al., 2002), METEOR (Lavie &
Agarwal, 2007), and ROUGE-L (Lin, 2004) for evaluation.
Models We evaluated 20 models selected from 10 model families, including various
model sizes. For closed-source models, we assessed GPT-4o (OpenAI, 2024) and Claude
3.7 Sonnet (Anthropic, 2025).
For the open-source models, we evaluated models in-
cluding DeepSeek-V3 (DeepSeek-AI et al., 2025), Gemma-2-it-2b/27b (Team et al., 2024),
GLM-4-9b-chat (GLM et al., 2024), Llama-3.1-Instruct-8B/70B (AI@Meta, 2024a), Llama-
3-Taiwan-Instruct-8B/70B (Lin & Chen, 2023), Meta-Llama-3-Instruct-8B/70B (AI@Meta,
4

--- Page 5 ---

Preprint. Under review.
Model
Avg.
STEM
Soc. Sci.
Humanities
Other
tc
sc
tc
sc
tc
sc
tc
sc
tc
sc
DeepSeek-V3
74.8
74.0
74.5
74.1
73.4
70.8
76.0
75.9
74.7
74.1
GPT-4o
70.3
69.9
75.0
74.2
70.4
67.8
68.7
70.1
67.9
67.1
Claude 3.7 Sonnet
66.7
66.9
74.3
74.0
69.4
64.7
63.1
65.9
62.1
63.2
Gemma-2-2B-IT
42.0
41.5
30.6
31.4
39.9
38.6
47.8
46.7
47.1
46.9
Gemma-2-27B-IT
57.4
56.5
55.6
55.4
55.3
54.3
59.9
59.0
57.4
56.1
GLM-4-9B-Chat
49.0
50.9
42.7
45.8
47.3
49.7
53.6
54.8
49.9
51.4
Llama-3.1-8B-Instruct
40.0
41.8
32.6
34.4
38.1
38.1
44.5
47.4
42.7
44.5
Llama-3.1-70B-Instruct
58.7
56.9
60.5
60.1
59.4
56.7
59.1
56.8
55.9
53.9
Llama-3-Taiwan-8B-Instruct
51.9
48.4
47.2
45.9
48.9
45.4
56.7
52.1
52.4
48.2
Llama-3-Taiwan-70B-Instruct
67.4
65.1
73.5
71.8
67.2
63.2
66.5
64.5
62.7
60.8
Llama-3-8B-Instruct
45.1
44.7
33.3
35.6
41.2
41.0
53.3
51.0
48.7
48.1
Llama-3-70B-Instruct
59.2
59.3
59.6
60.7
57.6
56.3
61.2
61.7
57.3
57.0
Mistral-Small-Instruct
45.2
45.0
38.9
40.1
42.0
41.9
49.6
49.3
47.9
46.5
Mistral-Large-Instruct
60.0
58.9
63.8
62.3
58.2
56.8
59.6
59.5
58.4
56.3
Qwen2.5-3B-Instruct
50.3
51.4
42.5
46.0
47.8
49.4
54.4
53.5
54.7
55.4
Qwen2.5-7B-Instruct
57.2
57.5
55.9
57.3
54.0
54.7
60.1
59.3
57.4
57.8
Qwen2.5-14B-Instruct
62.3
64.1
63.8
65.2
61.5
61.4
62.9
65.7
60.5
63.1
Qwen2.5-72B-Instruct
69.1
68.6
71.9
71.2
67.9
67.4
70.2
69.8
65.9
65.5
Yi-1.5-9B-Chat
52.6
52.7
45.5
48.8
51.6
50.2
57.0
55.4
54.3
55.0
Yi-1.5-34B-Chat
60.6
59.7
56.2
55.4
58.7
56.3
64.7
64.5
60.7
60.3
Avg.
57.0
56.7
54.9
55.5
55.5
54.2
59.4
59.1
56.9
56.6
Table 1: Zero-shot performance of models on HKMMLU in Traditional Chinese (TC) and
Simplified Chinese (SC). “Soc. Sci” stands for Social Sciences. “Avg.” indicates the micro-
average accuracy. The highest score in each column is in bold, while the second highest
score is underlined.
2024b), Mistral-Instruct-Large-2411/Small-2409 (Jiang et al., 2023), Qwen2.5-Instruct-
3B/7B/14B/72B (Yang et al., 2025), and Yi-1.5-Chat-9B/34B (01.AI, 2025).
4.1
Main Results
Results by model The evaluation results of 0-shot prompting is shown in Table 1. We have
observed the following: (1) DeepSeek-V3 achieves an average accuracy of 74.8%, ranking
first and surpassing both the two closed-source models. (2) Llama-3-Taiwan-Instruct series,
fine-tuned on Traditional Chinese data, achieves the highest average accuracy among Llama
models. Notably, the 70B variant of Llama-3-Taiwan-Instruct reaches an average accuracy
of 67.4%, outperforming Claude 3.7 Sonnet. (3) Among the remaining tested models, those
fine-tuned on simplified Chinese data (e.g., models from the GLM, Qwen, and Yi families)
generally outperform other model families of comparable sizes, such as the Llama series
(excluding the Llama-3-Taiwan-Instruct-8B / 70B models), Gemma and Mistral models. The
Qwen2.5-72B-Instruct model achieves an accuracy of 69.1%, which is notably higher than
the Mistral-Large-Instruct model, even though the latter has almost 123 billion parameters.
(4) In contrast, most of the other models exhibit relatively low average accuracies, with
many failing to exceed 60%. Among all the tested models, the Llama-3.1-8B-Instruct from
the Llama family shows the lowest performance, with an average accuracy of only 40%.
Additionally, in all series, larger parameter-sized LLMs tend to achieve higher average
scores and perform better across all domains.
Result by subject We compare the performance of the two best-performing models, includ-
ing DeepSeek-V3 and GPT-4o, under 0-shot conditions. Results in Table 1 reveal that except
for a slightly lower score in the STEM category, DeepSeek-V3 significantly outperforms
GPT-4o in Other categories. Notably, in the Humanities category, DeepSeek-V3 exceeds
GPT-4o by 7.3 points. As detailed in Figure 4, DeepSeek-V3 demonstrates superior per-
5

--- Page 6 ---

Preprint. Under review.
formance over GPT-4o in most subjects. Specifically, DeepSeek-V3 surpasses GPT-4o in
Mathematics, Physics, and Chemistry, whereas GPT-4o shows higher accuracy in Biology,
Medicine, and Pharmacy. This difference suggests that DeepSeek-V3 may have advantages
in solving calculation-related questions. Furthermore, DeepSeek-V3 tends to perform better
in subjects such as Hong Kong Current Affairs, Hong Kong Law, Hong Kong Politicians,
and Events, which require a strong local knowledge base. In contrast, GPT-4o performs
slightly better in subjects related to finance and economics.
Basic Medical Science
Business Management
Chinese History
Chinese National Conditions
Chinese and World Culture
Chinese and World Geography
Clinical Psychology
College Math
Cultural Commonsense
Dentistry
Economics
Educational Psychology
Financial Analysis
Fire Science
HKDSE Biology
HKDSE Business, Accounting and Financial Studies
HKDSE Chemistry
HKDSE Economics
HKDSE Geography
HKDSE Information and Communication Technology
HKDSE Mathematics
HKDSE Physics
HKDSE Tourism and Hospitality
Human Behavior
Insurance Studies
Logic Reasoning
Management Accounting
Marketing Management
Mechanical
Nautical Science
Optometry
Organic Chemistry
Pharmacology
Pharmacy
Physics
Science and Technology Commonsense
Social Commonsense
Statistics and Machine Learning
Technical Skills
Traditional Chinese Medicine Clinical Medicine
Veterinary Pathology
Veterinary Pharmacology
World Entertainment
Hong Kong Celebrity
Hong Kong Cultural Art
Hong Kong Current Affairs
Hong Kong Education
Hong Kong Entertainment Industry and Management
Hong Kong Events and Festivals
Hong Kong Film and Television
Hong Kong Government and Political System
Hong Kong Historical Geography and Development
Hong Kong History
Hong Kong Human Geography
Hong Kong Law
Hong Kong Life Knowledge
Hong Kong Literature
Hong Kong Livelihood
Hong Kong Music
Hong Kong Party Politics
Hong Kong Physical Geography
Hong Kong Physical Transport and Infrastructure
Hong Kong Politicians and Events
Hong Kong Society
Hong Kong Transportation
Hong Kong Urban and Regional Development
Subject
0
20
40
60
80
100
Accuracy
Non-HK-specific
HK-specific
70% Accuracy Line
DeepSeek-V3
GPT-4o
Figure 4: Comparing the two top-performing models.
Metric
BLEU
METEOR
ROUGE-L
Avg.
Task
C to M M to C
C to M M to C
C to M
M to C
C to M M to C
DeepSeek-V3
57.4
41.9
79.0
67.1
80.2
69.4
72.2
59.5
GPT-4o
55.9
20.9
78.0
49.0
79.3
53.5
71.1
41.1
Claude 3.7 Sonnet
46.8
29.1
70.6
57.0
71.2
58.7
62.9
48.3
Gemma-2-2B-IT
31.4
8.7
61.2
29.1
66.4
37.9
53.0
25.2
Gemma-2-27B-IT
46.0
20.5
72.6
47.9
75.2
53.7
64.6
40.7
GLM-4-9B-Chat
45.8
9.6
72.5
34.3
74.7
40.3
64.3
28.1
Llama-3.1-8B-Instruct
25.1
8.2
52.2
26.8
55.3
30.5
44.2
21.8
Llama-3.1-70B-Instruct
38.4
13.4
65.1
36.8
67.4
42.7
57.0
31.0
Llama-3-Taiwan-8B-Instruct
30.6
25.8
58.9
51.0
61.7
55.6
50.4
44.1
Llama-3-Taiwan-70B-Instruct
48.2
45.1
72.6
69.8
74.0
71.4
64.9
62.1
Llama-3-8B-Instruct
42.4
19.2
68.8
43.2
70.9
49.1
60.7
37.2
Llama-3-70B-Instruct
50.1
13.7
74.0
38.0
75.6
43.6
66.6
31.8
Mistral-Large-Instruct
49.2
20.8
74.5
47.7
76.1
51.9
66.6
40.1
Mistral-Small-Instruct
45.4
24.4
71.3
50.7
73.7
55.6
63.5
43.6
Qwen2.5-3B-Instruct
38.6
5.3
65.5
24.8
68.3
31.3
57.5
20.5
Qwen2.5-7B-Instruct
46.6
9.1
72.0
31.6
73.7
37.3
64.1
26.0
Qwen2.5-14B-Instruct
49.3
21.1
73.7
47.4
74.9
51.6
66.0
40.0
Qwen2.5-72B-Instruct
53.1
25.7
76.1
52.6
77.3
56.1
68.8
44.8
Yi-1.5-9B-Chat
42.1
7.6
69.7
29.3
71.4
36.3
61.1
24.4
Yi-1.5-34B-Chat
33.0
12.2
50.4
37.5
51.2
43.2
44.9
31.0
Avg.
43.6
18.6
68.8
42.9
70.9
47.9
61.1
36.5
Table 2:
Model performance on translation tasks. Models generally perform better in
translating from Cantonese to Mandarin than from Mandarin to Cantonese. “C” stands for
Cantonese, “M” stands for Mandarin. The highest score in each column is in bold, while the
second highest score is underlined.
Performance on Translation Tasks We evaluated various models for translating between
Mandarin and Cantonese, as shown in Table 2. DeepSeek-V3 achieves the best performance
6

--- Page 7 ---

Preprint. Under review.
in the Cantonese-to-Mandarin translation task across all evaluation metrics. However, it
ranks second in the Mandarin-to-Cantonese translation task, with Llama-3-Taiwan-70B-
Instruct ranking first. GPT-4o ranks second in the Cantonese-to-Mandarin translation
task but performs poorly in the Mandarin-to-Cantonese task. This imbalanced perfor-
mance, where models generally perform better in Cantonese-to-Mandarin translation than
in Mandarin-to-Cantonese, is also observed in other models, with the Llama-3-Taiwan series
exhibiting the smallest gap. This discrepancy may be attributed to the fact that Mandarin
is more widely used in China and has more training materials available, leading to better
performance in translating from Cantonese to Mandarin. These results emphasize the
benefits of fine-tuning with traditional Chinese materials. However, it is noteworthy that
the performance of fine-tuned models in the Cantonese-to-Mandarin translation task has
decreased, suggesting that while fine-tuning can improve overall translation capabilities, it
may not uniformly enhance performance across all translation directions.
4.2
Analysis
4.2.1
Performance on Traditional Chinese and Simplified Chinese
To evaluate the performance of LLMs in Simplified Chinese, we translated the HK-
MMLU into Simplified Chinese using GPT-4o. Contrary to the conclusions drawn from
TMMLU+ (Tam et al., 2024), which suggest that non-Traditional Chinese LLMs perform
better in Simplified Chinese, the results from HKMMLU indicate that most LLMs achieve
higher average scores in Traditional Chinese. Specifically, most models excel in Traditional
Chinese in Social Sciences, Humanities, and Other categories, while their performance in
STEM is comparatively weaker. This discrepancy may stem from the fact that the first
three categories include more Hong Kong-specific knowledge, which is more frequently
represented in Traditional Chinese within the training materials of LLMs, reflecting the
unique cultural context of Hong Kong. In contrast, STEM topics such as Mathematics and
Biology are more general and often use standardized terminologies.
We also compare the performance of different models on different MMLU benchmarks. As
shown in Figure 5, non-Traditional Chinese models, such as DeepSeek-V3 and Qwen2.5-72B-
Instruct, perform worse on TMMLU+ and HKMMLU compared to CMMLU, indicating their
deficiency on Traditional Chinese understanding. Llama-3-Taiwan-70B-Instruct, fine-tuned
with Traditional Chinese materials related to Taiwan, performs best on TMMLU+. However,
although Hong Kong and Taiwan Traditional Chinese share most characters, Llama-3-
Taiwan-70B-Instruct performs poorly on HKMMLU, indicating a lack of knowledge of Hong
Kong and Cantonese.
CMMLU
TMMLU+
HKMMLU
30 40 50 60 70 80
DeepSeek-V3
GPT-4o
Claude 3.7 Sonnet
Gemma-2-27B-IT
GLM-4-9B-Chat
Llama-3.1-70B-Instruct
Llama-3-Taiwan-70B-Instruct
Qwen2.5-72B-Instruct
Figure 5:
Comparison of model perfor-
mance among HKMMLU, TMMLU+, and
CMMLU, with most models achieving their
best results on CMMLU.
0
1
2
3
4
5
Number of Shots
40
45
50
55
60
65
70
75
80
Accuracy (%)
DeepSeek-V3
GPT-4o
Gemma-2-2B-IT
Gemma-2-27B-IT
GLM-4-9B-Chat
Llama-3.1-8B-Instruct
Llama-3.1-70B-Instruct
Llama-3-Taiwan-8B-Instruct
Llama-3-Taiwan-70B-Instruct
Llama-3-8B-Instruct
Llama-3-70B-Instruct
Mistral-Small-Instruct
Qwen2.5-3B-Instruct
Qwen2.5-14B-Instruct
Qwen2.5-72B-Instruct
Yi-1.5-9B-Chat
Yi-1.5-34B-Chat
Figure 6: A comparison of zero-shot and
few-shot prompts on accuracy on HK-
MMLU.
7

--- Page 8 ---

Preprint. Under review.
Model
Avg.
STEM
Soc. Sci.
Humanities
Other
DA
0-CoT
1-CoT
DA
0-CoT
1-CoT
DA
0-CoT
1-CoT
DA
0-CoT
1-CoT
DA
0-CoT
1-CoT
DeepSeek-V3
74.9
74.1
75.8
74.5
78.1
81.0
73.5
74.3
75.6
76.0
72.9
74.3
74.8
71.8
72.9
GPT-4o
70.3
72.4
72.2
75.0
79.7
82.1
70.4
74.1
74.1
68.6
69.1
66.6
67.9
68.3
68.8
Claude 3.7 Sonnet
66.7
72.3
66.8
74.3
81.7
78.6
69.4
76.2
74.8
63.0
67.3
58.7
62.1
66.6
59.5
Gemma-2-2B-IT
42.0
36.6
36.8
30.6
31.6
30.2
40.1
35.9
34.4
47.7
38.4
40.3
47.0
39.8
40.4
Gemma-2-27B-IT
57.4
55.8
56.9
55.7
59.2
60.6
55.4
55.0
57.7
59.7
55.8
56.3
57.5
53.3
53.4
GLM-4-9B-Chat
48.9
49.7
51.0
42.8
51.0
51.2
47.3
48.6
50.6
53.4
50.1
52.3
49.9
49.0
49.3
Llama-3.1-8B-Instruct
40.0
34.0
29.8
32.6
32.9
29.0
38.1
34.8
30.8
44.4
34.9
30.2
42.7
33.4
29.0
Llama-3.1-70B-Instruct
58.7
49.8
39.6
60.5
51.9
43.2
59.5
50.7
41.4
58.8
49.5
36.9
55.9
47.4
38.3
Llama-3-Taiwan-8B-Instruct
51.9
49.6
51.2
47.4
45.5
48.3
48.9
47.7
49.3
56.6
53.1
53.8
52.4
50.2
51.9
Llama-3-Taiwan-70B-Instruct
67.4
64.9
66.5
73.6
72.8
74.4
67.3
65.5
67.2
66.3
62.5
64.0
62.6
60.0
61.5
Llama-3-8B-Instruct
45.1
40.6
45.8
33.3
35.5
37.6
41.3
39.4
42.5
53.2
43.6
52.1
48.6
42.7
47.9
Llama-3-70B-Instruct
59.2
58.2
60.5
59.7
60.3
62.4
57.8
57.9
61.3
61.0
57.6
60.0
57.2
57.4
58.6
Mistral-Small-Instruct
45.1
42.3
40.2
38.9
43.0
40.2
42.1
39.6
37.9
49.4
43.0
41.9
47.8
43.2
39.9
Mistral-Large-Instruct
60.0
58.7
49.3
63.8
59.2
51.7
58.2
56.3
50.8
59.5
59.9
48.1
58.4
58.6
47.2
Qwen2.5-3B-Instruct
50.3
42.1
44.0
42.5
41.5
41.8
48.0
40.5
42.4
54.1
41.9
44.8
54.7
44.5
46.6
Qwen2.5-7B-Instruct
57.2
53.1
53.9
56.0
56.0
56.3
54.1
51.8
52.7
60.0
52.6
54.0
57.4
51.9
52.4
Qwen2.5-14B-Instruct
62.3
61.2
61.7
63.9
65.2
64.7
61.5
61.3
61.8
62.8
60.5
61.5
60.4
58.1
58.8
Qwen2.5-72B-Instruct
69.1
66.9
66.6
72.0
71.4
71.1
67.9
67.6
67.3
70.1
65.8
65.6
65.8
63.6
62.7
Yi-1.5-9B-Chat
52.5
49.7
50.5
45.4
45.9
45.4
51.6
49.1
49.0
56.9
51.3
54.2
54.3
51.9
51.5
Yi-1.5-34B-Chat
60.5
56.1
58.1
56.2
54.4
55.5
58.7
56.5
57.1
64.6
56.7
60.1
60.5
56.6
58.7
Avg.
57.0
54.4
53.9
54.9
55.8
55.3
55.6
54.1
53.9
59.3
54.3
53.8
56.9
53.4
52.5
Table 3: Model performance on HKMMLU using direct answering (DA), 0-shot CoT (0-CoT),
and 1-shot CoT prompting (1-CoT). “Soc. Sci” stands for Social Sciences. “Avg.” represents
the micro-average accuracy. The highest score within each model and category across the
three methods is underlined.
4.2.2
Efficiency of Chain-of-Thought (CoT) Prompting
To evaluate the effectiveness of CoT prompting, we first applied a 0-shot CoT prompt
as detailed in Appendix J.1, which requires the LLM to think step-by-step to generate
an answer. Similar to the conclusions drawn from CMMLU (Li et al., 2024), the average
scores of all models drop significantly. However, models such as DeepSeek-V3, Gemma 2
series, Llama-3 series, and Yi-1.5 series show improved performance in the STEM category.
This improvement is because the STEM category includes subjects such as mathematics and
physics, which may require certain reasoning steps to generate the correct answer.
We further investigate whether an example reasoning step would encourage the LLMs to
generate more convincing answers. As shown in Table 3, several have shown significant
improvement despite the decreased average accuracy for most models, such as DeepSeek-V3
and GLM-4-9B-Chat. Notably, DeepSeek-V3, GPT-4o, and GLM-4-9B-Chat increased by
more than five percentage points in the STEM category. The significant improvement in
performance of these models in 1-shot CoT compared to 0-shot CoT can be attributed to
the high-quality reasoning example provided. This finding further proves the necessity of
reliable reasoning steps for tasks in STEM. These models also show slight enhancement in
Social Sciences. However, only GPT-4o and Llama-3-70B-Instruct show an increase in scores
in the Other subject, while no model shows improvement in Humanities. This limitation is
because these two categories include more Hong Kong-specific knowledge, which cannot
be learned through reasoning if the models lack relevant knowledge.
4.2.3
Efficiency of Few-shot Prompting
Contrary to previous studies suggesting that an increase in the number of shots leads to
improved performance (Brown et al., 2020), our findings indicate that the performance of
most models tends to stabilize (Figure 6). However, some models, such as Llama-3-8B-
Instruct and GLM-4-9B-Chat, experience a sharp decline between 0-shot and 1-shot. In
contrast, models like Yi-1.5-9B-Chat and Mistral-Small-Instruct show a relatively significant
improvement from 0-shot to 1-shot. DeepSeek-V3 shows a slight increase in performance
from 2-shot to 3-shot, maintaining its rank one position. The results indicate that the number
of shots affects model performance differently across models and does not always lead to
improved performance.
4.2.4
Impact of Question Token Length and Reasoning Token Length
We explore the impact of the token length of questions on model performance. As shown in
Figure 7, most models show a decrease in accuracy as the token length increases beyond 400,
except the two closed-source models and Qwen-2.5-72B-Instruct. Even the top-performing
model, DeepSeek-V3, shows a sharp decline after 600 token length. This trend highlights
8

--- Page 9 ---

Preprint. Under review.
0-200
200-400
400-600
600-800
Token Range
0.2
0.3
0.4
0.5
0.6
0.7
Average Score
0-200
200-400
400-600
600-800
800-1000
1000-1200
1200-1400
1400-1600
1600-1800
1800-2000
Token Range
0.2
0.3
0.4
0.5
0.6
0.7
0.8
Average Score
DeepSeek-V3
DeepSeek-V3
GPT-4o
GPT-4o
Claude-3.7-Sonnet
Qwen2.5-3B-Instruct
Qwen2.5-3B-Instruct
Qwen2.5-72B-Instruct
Qwen2.5-72B-Instruct
Gemma 2 IT 2B
Gemma 2 IT 2B
Mistral-Small-Instruct
Mistral-Small-Instruct
Mistral-Large-Instruct
Mistral-Large-Instruct
Llama-3-Taiwan-8B-Instruct
Llama-3-Taiwan-8B-Instruct
Llama-3-Taiwan-70B-Instruct
Llama-3-Taiwan-70B-Instruct
Llama-3-8B-Instruct
Llama-3-8B-Instruct
Llama-3-70B-Instruct
Llama-3-70B-Instruct
Yi-1.5-34B-Chat
Yi-1.5-34B-Chat
Figure 7: Impact of question token length on model performance (left) and impact of
reasoning token length on model performance (right).
the deficiency of most open-source LLMs in understanding long texts in Traditional Chinese.
Specifically, the two Traditional Chinese-fine-tuned models, Llama-3-Taiwan-70B-Instruct
and Llama-3-Taiwan-8B-Instruct, do not show advantages in long text understanding. The
70B model declines after 600 tokens, while the 8B model declines after 400 tokens. To
examine the relationship between the token length of reasoning and model performance,
we record the accuracy of models at various reasoning token lengths when utilizing 1-
shot CoT. Figure 7 illustrates that models tend to underperform when the reasoning token
length exceeds 400 tokens. This observation suggests that longer reasoning tokens do not
necessarily enhance model accuracy without adequate knowledge.
4.2.5
Comparative Analysis of Human and LLM Performance
Tester
Avg.
Cantonese
TC
DeepSeek-V3
57.0
59.2
56.2
Human
57.9
63.4
55.9
Table 4: Performance comparison between humans and the top LLM, DeepSeek-V3, on 100
selected Hong Kong-specific questions. “TC” denotes Traditional Chinese.
To reduce over-reliance on LLM-driven analysis in the benchmark (Yeadon et al., 2024)
and to assess their actual understanding of Traditional Chinese and Cantonese, we have
implemented a human-machine comparison test. We selected 100 questions from Hong
Kong-specific subjects and tested them on 24 local testers with a post-secondary degree or
above. Humans achieved an average accuracy of 57.9% (SD = 5.9%, SE = 1.2%) with a 95%
confidence interval of [55.5%, 60.2%]. In comparison, the top-performing LLM, DeepSeek-
V3, achieved an accuracy of 57% (Table 4), slightly below the average accuracy of human
test takers. These results reveal the limitations of LLMs in matching the knowledge and
language skills of local individuals while also highlighting the challenges of our benchmark.
Furthermore, we also find that the gap between human and LLM is greater for questions
in Cantonese than for those in Traditional Chinese, indicating DeepSeek-V3’s deficiency in
understanding Cantonese linguistic and cultural nuances.
5
Conclusion
We introduce HKMMLU, a benchmark designed to evaluate the proficiency of LLMs in
Hong Kong knowledge and its languages through multi-choice questions and Mandarin-
Cantonese translation tasks. Experimental results highlight significant performance gaps in
LLMs when addressing region-specific linguistic nuances and socio-cultural context. Our
analysis further identifies key factors influencing model performance, including question
language, model size, prompting strategies, and the lengths of questions and reasoning
tokens. A comparison test between humans and the top-performing LLM, DeepSeek-V3,
on 100 Hong Kong-specific questions further demonstrates the deficiencies of LLMs in
9

--- Page 10 ---

Preprint. Under review.
knowledge of Hong Kong and its languages, particularly Cantonese. Focusing on Hong
Kong’s unique sociolinguistic landscape, this work aims to drive advancements in LLMs’
multilingual and cross-cultural capabilities, fostering AI systems that are both technically
robust and culturally attuned to global and local needs.
Ethics Statement
All data in HKMMLU are sourced from publicly available materials, ensuring transparency
and accessibility. Humans have carefully reviewed each instance to ensure no harmful or
offensive questions are included. Additionally, when applying the LLMs for labeling or
inference, we did not use any damaging or intentionally provocative prompts that could
lead to safety or unethical outputs.
References
01.AI. Yi: Open foundation models by 01.ai, 2025. URL https://arxiv.org/abs/2403.
04652.
AI@Meta.
Llama-3.1-70b-instruct model card.
2024a.
URL https://github.com/
meta-llama/llama-models/blob/main/models/llama3_1/MODEL_CARD.md.
AI@Meta. Llama 3 model card. 2024b. URL https://github.com/meta-llama/llama3/
blob/main/MODEL_CARD.md.
AI Anthropic. Claude 3.7 sonnet and claude code. 2025. URL https://www.anthropic.com/
news/claude-3-7-sonnet.
Jacob Austin, Augustus Odena, Maxwell Nye, Maarten Bosma, Henryk Michalewski, David
Dohan, Ellen Jiang, Carrie Cai, Michael Terry, Quoc Le, and Charles Sutton. Program
synthesis with large language models, 2021. URL https://arxiv.org/abs/2108.07732.
Tom Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared D Kaplan, Prafulla
Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, et al.
Language models are few-shot learners. In H. Larochelle, M. Ranzato, R. Hadsell, M.F.
Balcan, and H. Lin (eds.), Advances in Neural Information Processing Systems, volume 33, pp.
1877–1901. Curran Associates, Inc., 2020. URL https://proceedings.neurips.cc/paper_
files/paper/2020/file/1457c0d6bfcb4967418bfb8ac142f64a-Paper.pdf.
Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Ponde de Oliveira Pinto,
Jared Kaplan, Harri Edwards, Yuri Burda, Nicholas Joseph, Greg Brockman, Alex Ray,
Raul Puri, Gretchen Krueger, Michael Petrov, Heidy Khlaaf, Girish Sastry, Pamela Mishkin,
Brooke Chan, Scott Gray, Nick Ryder, Mikhail Pavlov, Alethea Power, et al. Evaluating
large language models trained on code, 2021. URL https://arxiv.org/abs/2107.03374.
Po-Heng Chen, Sijia Cheng, Wei-Lin Chen, Yen-Ting Lin, and Yun-Nung Chen. Measuring
taiwanese mandarin language understanding. In First Conference on Language Modeling,
2024. URL https://openreview.net/forum?id=7jSMMvXLri.
Siu-Pong Cheng and Sze-Wing Tang. Languagehood of cantonese: A renewed front in an
old debate. Open Journal of Modern Linguistics, 4(3):389–398, 2014.
Tsz Chung Cheng, Chung Shing Cheng, Chaak Ming Lau, Eugene Tin-Ho Lam, Chun Yat
Wong, Hoi On Yu, and Cheuk Hei Chong. Hkcanto-eval: A benchmark for evaluating
cantonese language understanding and cultural comprehension in llms, 2025. URL
https://arxiv.org/abs/2503.12440.
Peter Clark, Isaac Cowhey, Oren Etzioni, Tushar Khot, Ashish Sabharwal, Carissa Schoenick,
and Oyvind Tafjord. Think you have solved question answering? try arc, the ai2 reasoning
challenge, 2018. URL https://arxiv.org/abs/1803.05457.
10

--- Page 11 ---

Preprint. Under review.
Karl Cobbe, Vineet Kosaraju, Mohammad Bavarian, Mark Chen, Heewoo Jun, Lukasz
Kaiser, Matthias Plappert, Jerry Tworek, Jacob Hilton, Reiichiro Nakano, Christopher
Hesse, and John Schulman. Training verifiers to solve math word problems, 2021. URL
https://arxiv.org/abs/2110.14168.
DeepSeek-AI, Aixin Liu, Bei Feng, Bing Xue, Bingxuan Wang, Bochao Wu, Chengda Lu,
Chenggang Zhao, Chengqi Deng, Chenyu Zhang, Chong Ruan, Damai Dai, Daya Guo,
Dejian Yang, Deli Chen, Dongjie Ji, et al. Deepseek-v3 technical report, 2025. URL
https://arxiv.org/abs/2412.19437.
Philipp Ennen, Po-Chun Hsu, Chan-Jan Hsu, Chang-Le Liu, Yen-Chen Wu, Yin-Hsiang Liao,
Chin-Tung Lin, Da-Shan Shiu, and Wei-Yun Ma. Extending the pre-training of bloom
for improved support of traditional chinese: Models, methods and results, 2023. URL
https://arxiv.org/abs/2303.04715.
Team GLM, :, Aohan Zeng, Bin Xu, Bowen Wang, Chenhui Zhang, Da Yin, Dan Zhang,
Diego Rojas, Guanyu Feng, Hanlin Zhao, Hanyu Lai, Hao Yu, Hongning Wang, Jiadai
Sun, Jiajie Zhang, Jiale Cheng, Jiayi Gui, Jie Tang, Jing Zhang, Jingyu Sun, et al. Chatglm:
A family of large language models from glm-130b to glm-4 all tools, 2024. URL https:
//arxiv.org/abs/2406.12793.
Dan Hendrycks, Collin Burns, Steven Basart, Andy Zou, Mantas Mazeika, Dawn Song, and
Jacob Steinhardt. Measuring massive multitask language understanding. In International
Conference on Learning Representations, 2021a. URL https://openreview.net/forum?id=
d7KBjmI3GmQ.
Dan Hendrycks, Collin Burns, Saurav Kadavath, Akul Arora, Steven Basart, Eric Tang, Dawn
Song, and Jacob Steinhardt. Measuring mathematical problem solving with the MATH
dataset. In Thirty-fifth Conference on Neural Information Processing Systems Datasets and
Benchmarks Track (Round 2), 2021b. URL https://openreview.net/forum?id=7Bywt2mQsCe.
Chan-Jan Hsu, Chang-Le Liu, Feng-Ting Liao, Po-Chun Hsu, Yi-Chang Chen, and Da shan
Shiu. Advancing the evaluation of traditional chinese language models: Towards a
comprehensive benchmark suite, 2023. URL https://arxiv.org/abs/2309.08448.
Yuzhen Huang, Yuzhuo Bai, Zhihao Zhu, Junlei Zhang, Jinghan Zhang, Tangjun Su, Junteng
Liu, Chuancheng Lv, Yikai Zhang, jiayi lei, Yao Fu, Maosong Sun, and Junxian He. C-eval:
A multi-level multi-discipline chinese evaluation suite for foundation models. In Thirty-
seventh Conference on Neural Information Processing Systems Datasets and Benchmarks Track,
2023. URL https://openreview.net/forum?id=fOrm2rGX2r.
Albert Q. Jiang, Alexandre Sablayrolles, Arthur Mensch, Chris Bamford, Devendra Singh
Chaplot, Diego de las Casas, Florian Bressand, Gianna Lengyel, Guillaume Lample, Lucile
Saulnier, Lélio Renard Lavaud, Marie-Anne Lachaux, Pierre Stock, Teven Le Scao, Thibaut
Lavril, Thomas Wang, Timothée Lacroix, and William El Sayed. Mistral 7b, 2023. URL
https://arxiv.org/abs/2310.06825.
Carbo Kuo. Opencc. GitHub, 2024. URL https://github.com/BYVoid/OpenCC.
Tom Kwiatkowski, Jennimaria Palomaki, Olivia Redfield, Michael Collins, Ankur Parikh,
Chris Alberti, Danielle Epstein, Illia Polosukhin, Jacob Devlin, Kenton Lee, Kristina
Toutanova, Llion Jones, Matthew Kelcey, Ming-Wei Chang, Andrew M. Dai, Jakob Uszko-
reit, Quoc Le, and Slav Petrov. Natural questions: A benchmark for question answering
research. Transactions of the Association for Computational Linguistics, 7:452–466, 2019. doi:
10.1162/tacl_a_00276. URL https://aclanthology.org/Q19-1026/.
Alon Lavie and Abhaya Agarwal. METEOR: An automatic metric for MT evaluation with
high levels of correlation with human judgments. In Chris Callison-Burch, Philipp Koehn,
Cameron Shaw Fordyce, and Christof Monz (eds.), Proceedings of the Second Workshop on
Statistical Machine Translation, pp. 228–231, Prague, Czech Republic, June 2007. Association
for Computational Linguistics. URL https://aclanthology.org/W07-0734/.
11

--- Page 12 ---

Preprint. Under review.
Haonan Li, Martin Tomko, Maria Vasardani, and Timothy Baldwin. MultiSpanQA: A
dataset for multi-span question answering. In Marine Carpuat, Marie-Catherine de Marn-
effe, and Ivan Vladimir Meza Ruiz (eds.), Proceedings of the 2022 Conference of the North
American Chapter of the Association for Computational Linguistics: Human Language Tech-
nologies, pp. 1250–1260, Seattle, United States, July 2022. Association for Computational
Linguistics. doi: 10.18653/v1/2022.naacl-main.90. URL https://aclanthology.org/
2022.naacl-main.90/.
Haonan Li, Yixuan Zhang, Fajri Koto, Yifei Yang, hai zhao, Yeyun Gong, Nan Duan, and
Timothy Baldwin. CMMLU: Measuring massive multitask language understanding in
chinese, 2024. URL https://openreview.net/forum?id=ck4SG9lnrQ.
Chin-Yew Lin. ROUGE: A package for automatic evaluation of summaries. In Text Summa-
rization Branches Out, pp. 74–81, Barcelona, Spain, July 2004. Association for Computa-
tional Linguistics. URL https://aclanthology.org/W04-1013/.
Yen-Ting Lin and Yun-Nung Chen. Taiwan llm: Bridging the linguistic divide with a
culturally aligned language model, 2023. URL https://arxiv.org/abs/2311.17487.
Chuang Liu, Renren Jin, Yuqi Ren, Linhao Yu, Tianyu Dong, Xiaohan Peng, Shuting Zhang,
Jianxiang Peng, Peiyi Zhang, Qingqing Lyu, Xiaowen Su, Qun Liu, and Deyi Xiong. M3ke:
A massive multi-level multi-subject knowledge evaluation benchmark for chinese large
language models, 2023. URL https://arxiv.org/abs/2305.10263.
OpenAI. Gpt-4o system card, 2024. URL https://arxiv.org/abs/2410.21276.
OpenAI.
Openai o3-mini system card.
2025.
URL https://cdn.openai.com/
o3-mini-system-card-feb10.pdf.
Kishore Papineni, Salim Roukos, Todd Ward, and Wei-Jing Zhu.
Bleu: a method for
automatic evaluation of machine translation. In Pierre Isabelle, Eugene Charniak, and
Dekang Lin (eds.), Proceedings of the 40th Annual Meeting of the Association for Computational
Linguistics, pp. 311–318, Philadelphia, Pennsylvania, USA, July 2002. Association for
Computational Linguistics. doi: 10.3115/1073083.1073135. URL https://aclanthology.
org/P02-1040/.
Pranav Rajpurkar, Robin Jia, and Percy Liang. Know what you don‘t know: Unanswerable
questions for SQuAD. In Iryna Gurevych and Yusuke Miyao (eds.), Proceedings of the 56th
Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers), pp.
784–789, Melbourne, Australia, July 2018. Association for Computational Linguistics. doi:
10.18653/v1/P18-2124. URL https://aclanthology.org/P18-2124/.
Keisuke Sakaguchi, Ronan Le Bras, Chandra Bhagavatula, and Yejin Choi. Winogrande: an
adversarial winograd schema challenge at scale. Commun. ACM, 64(9):99–106, August
2021. ISSN 0001-0782. doi: 10.1145/3474381. URL https://doi.org/10.1145/3474381.
Chih Chieh Shao, Trois Liu, Yuting Lai, Yiying Tseng, and Sam Tsai. Drcd: a chinese machine
reading comprehension dataset, 2019. URL https://arxiv.org/abs/1806.00920.
Guijin Son, Hanwool Lee, Sungdong Kim, Seungone Kim, Niklas Muennighoff, Taekyoon
Choi, Cheonbok Park, Kang Min Yoo, and Stella Biderman. Kmmlu: Measuring massive
multitask language understanding in korean, 2024. URL https://arxiv.org/abs/2402.
11548.
Alon Talmor, Jonathan Herzig, Nicholas Lourie, and Jonathan Berant. CommonsenseQA: A
question answering challenge targeting commonsense knowledge. In Jill Burstein, Christy
Doran, and Thamar Solorio (eds.), Proceedings of the 2019 Conference of the North American
Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume
1 (Long and Short Papers), pp. 4149–4158, Minneapolis, Minnesota, June 2019. Association
for Computational Linguistics. doi: 10.18653/v1/N19-1421. URL https://aclanthology.
org/N19-1421/.
12

--- Page 13 ---

Preprint. Under review.
Zhi-Rui Tam, Ya-Ting Pai, Yen-Wei Lee, Jun-Da Chen, Wei-Min Chu, Sega Cheng, and
Hong-Han Shuai. An improved traditional chinese evaluation suite for foundation model,
2024. URL https://arxiv.org/abs/2403.01858.
Gemma Team, Morgane Riviere, Shreya Pathak, Pier Giuseppe Sessa, Cassidy Hardin, Surya
Bhupatiraju, Léonard Hussenot, Thomas Mesnard, Bobak Shahriari, Alexandre Ramé,
Johan Ferret, Peter Liu, Pouya Tafti, Abe Friesen, Michelle Casbon, Sabela Ramos, Ravin
Kumar, Charline Le Lan, Sammy Jerome, Anton Tsitsulin, Nino Vieillard, et al. Gemma 2:
Improving open language models at a practical size, 2024. URL https://arxiv.org/abs/
2408.00118.
Alex Wang, Amanpreet Singh, Julian Michael, Felix Hill, Omer Levy, and Samuel Bowman.
GLUE: A multi-task benchmark and analysis platform for natural language understanding.
In Tal Linzen, Grzegorz Chrupała, and Afra Alishahi (eds.), Proceedings of the 2018 EMNLP
Workshop BlackboxNLP: Analyzing and Interpreting Neural Networks for NLP, pp. 353–355,
Brussels, Belgium, November 2018. Association for Computational Linguistics. doi:
10.18653/v1/W18-5446. URL https://aclanthology.org/W18-5446/.
Alex Wang, Yada Pruksachatkun, Nikita Nangia, Amanpreet Singh, Julian Michael, Felix
Hill, Omer Levy, and Samuel R. Bowman. SuperGLUE: a stickier benchmark for general-
purpose language understanding systems. Curran Associates Inc., Red Hook, NY, USA,
2019.
Bin Wang, Zhengyuan Liu, Xin Huang, Fangkai Jiao, Yang Ding, AiTi Aw, and Nancy Chen.
SeaEval for multilingual foundation models: From cross-lingual alignment to cultural
reasoning. In Kevin Duh, Helena Gomez, and Steven Bethard (eds.), Proceedings of the
2024 Conference of the North American Chapter of the Association for Computational Linguistics:
Human Language Technologies (Volume 1: Long Papers), pp. 370–390, Mexico City, Mexico,
June 2024. Association for Computational Linguistics. doi: 10.18653/v1/2024.naacl-long.
22. URL https://aclanthology.org/2024.naacl-long.22/.
Tianwen Wei, Jian Luan, Wei Liu, Shuang Dong, and Bin Wang. Cmath: Can your language
model pass chinese elementary school math test?, 2023. URL https://arxiv.org/abs/
2306.16636.
Liang Xu, Anqi Li, Lei Zhu, Hang Xue, Changtai Zhu, Kangkang Zhao, Haonan He, Xuanwei
Zhang, Qiyue Kang, and Zhenzhong Lan. Superclue: A comprehensive chinese large
language model benchmark, 2023. URL https://arxiv.org/abs/2307.15020.
An Yang, Baosong Yang, Beichen Zhang, Binyuan Hui, Bo Zheng, Bowen Yu, Chengyuan
Li, Dayiheng Liu, Fei Huang, Haoran Wei, Huan Lin, Jian Yang, et al. Qwen2.5 technical
report, 2025. URL https://arxiv.org/abs/2412.15115.
Will Yeadon, Alex Peach, and Craig Testrow. A comparison of human, gpt-3.5, and gpt-4
performance in a university-level coding course. Scientific Reports, 14(1), October 2024.
ISSN 2045-2322. doi: 10.1038/s41598-024-73634-y. URL http://dx.doi.org/10.1038/
s41598-024-73634-y.
Hui Zeng. Measuring massive multitask chinese understanding, 2023. URL https://arxiv.
org/abs/2304.12986.
Yixuan Zhang and Haonan Li. Can large language model comprehend Ancient Chinese?
a preliminary test on ACLUE. In Adam Anderson, Shai Gordin, Bin Li, Yudong Liu,
and Marco C. Passarotti (eds.), Proceedings of the Ancient Language Processing Workshop,
pp. 80–87, Varna, Bulgaria, September 2023. INCOMA Ltd., Shoumen, Bulgaria. URL
https://aclanthology.org/2023.alp-1.9/.
Wanjun Zhong, Ruixiang Cui, Yiduo Guo, Yaobo Liang, Shuai Lu, Yanlin Wang, Amin Saied,
Weizhu Chen, and Nan Duan. AGIEval: A human-centric benchmark for evaluating
foundation models. In Kevin Duh, Helena Gomez, and Steven Bethard (eds.), Findings
of the Association for Computational Linguistics: NAACL 2024, pp. 2299–2314, Mexico City,
Mexico, June 2024. Association for Computational Linguistics. doi: 10.18653/v1/2024.
findings-naacl.149. URL https://aclanthology.org/2024.findings-naacl.149/.
13

--- Page 14 ---

Preprint. Under review.
Contents
1
Introduction
1
2
Related Work
3
3
HKMMLU
3
4
Experiments
4
4.1
Main Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5
4.2
Analysis
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7
4.2.1
Performance on Traditional Chinese and Simplified Chinese . . . . .
7
4.2.2
Efficiency of Chain-of-Thought (CoT) Prompting
. . . . . . . . . . .
8
4.2.3
Efficiency of Few-shot Prompting
. . . . . . . . . . . . . . . . . . . .
8
4.2.4
Impact of Question Token Length and Reasoning Token Length . . .
8
4.2.5
Comparative Analysis of Human and LLM Performance . . . . . . .
9
5
Conclusion
9
A HKMMLU Subjects
15
B
Models Evaluated in this Paper
16
C Detailed Results of Few-shot Prompting
16
D Efficiency of Reasoning Examples for STEM and non-STEM Tasks
18
E
Simplified Chinese vs. Languages of Hong Kong
19
F
Model Performance Comparison: CMMLU, TMMLU+, and HKMMLU
19
G Model Performance on Hong Kong-specific Tasks
20
H Model Performance by Subject
20
I
Details of Human Review
23
J
Prompts
23
J.1
Inference Prompts . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
23
J.2
Translation Prompts . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
24
J.3
Subject Category Prompts . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
24
K Data Examples in HKMMLU
24
L
Compute and Resources Used for Evaluation
24
M Fair and Ethical Labor
25
14

--- Page 15 ---

Preprint. Under review.
A
HKMMLU Subjects
Category
Subject Name
Traditional Chinese Name
Questions Number
STEM
Basic Medical Science
Dentistry
College Math
HKDSE Biology
HKDSE Chemistry
HKDSE Information and Communication technology
HKDSE Mathematics
HKDSE Physics
Mechanical
Optometry
Organic Chemistry
Pharmacology
Pharmacy
Physics
Traditional Chinese Medicine Clinical Medicine
Veterinary Pathology
Veterinary Pharmacology
Statistics and Machine Learning
基礎醫學
牙醫學
大學數學
香港中學文憑考試生物
香港中學文憑考試化學
香港中學文憑考試資訊與通訊科技
香港中學文憑考試數學
香港中學文憑考試物理
機械與機電概論
視光學
有機化學
藥理學
藥劑學
物理
中醫臨床醫學
獸醫病理學
獸醫藥理學
統計與機器學習
1020
296
176
140
254
360
184
103
109
891
131
620
350
115
278
310
577
244
Social Science
Business Management
Chinese and World Geography
Clinical Psychology
Economics
Educational Psychology
Financial Analysis
HKDSE Business, Accounting and Financial Studies
HKDSE Geography
HKDSE Tourism and Hospitality
HKDSE Economics
Hong Kong Physical Geography #
Hong Kong Transport and Infrastructure #
Hong Kong Urban and Regional Development #
Insurance Studies
Management Accounting
Marketing Management
企業管理
中國與世界地理
臨床心理學
經濟學
教育心理學
財務分析
香港中學文憑考試企業、會計與財務概論
香港中學文憑考試地理
香港中學文憑考試旅遊與款待
香港中學文憑考試經濟
香港自然地理
香港交通與基礎設施
香港城市與區域規劃
保險學
管理會計
行銷管理
155
164
129
399
173
229
226
148
238
227
714
463
1148
118
197
106
Humanities
Chinese National Conditions
Chinese and World Culture
Chinese History
Hong Kong Education #
Hong Kong Historical Geography and Development #
Hong Kong History #
Hong Kong Cultural Art #
Hong Kong Current Affairs #
Hong Kong Celebrity #
Hong Kong Government and Political System #
Hong Kong Literature #
Hong Kong Politicians and Events #
Hong Kong Society #
Hong Kong Human Geography #
Hong Kong Law #
Hong Kong Party Politics #
Human Behavior
World Entertainment
中國國情
中國與世界文化
中國歷史
香港教育
香港歷史地理與發展
香港歷史
香港文娛
香港時事
香港名人文化
香港政府機構與政治制度
香港文學
香港政治人物與事件
香港社會
香港人文地理
香港法律
香港政黨政治
人類行為與社會學
世界文娛
117
154
110
730
143
556
162
278
1267
281
203
268
515
1251
412
1440
297
720
Other
Commonsense of Science and Technology
Cultural Commonsense
Fire Science
Hong Kong Events and Festivals #
Hong Kong Entertainment Industry and Management #
Hong Kong Film and Television #
Hong Kong Life Knowledge #
Hong Kong Livelihood #
Hong Kong Music #
Hong Kong Transportation #
Logic Reasoning
Nautical Science
Social Commonsense
Technical Skills
科學技術常識
文化常識
火災學
香港活動與節慶
香港文娛產業與經營
香港影視
香港生活常識
香港民生
香港音樂
香港交通
邏輯思維
航海
社會常識
技術工學
124
164
135
108
155
2201
330
895
1035
357
159
606
187
346
Table 5: Overview of subjects in HKMMLU. “#” indicated the HK-Specific subjects.
Table 5 lists all 66 subjects across the four categories, their names in Traditional Chinese,
and the number of questions. In particular, HKMMLU includes 23 Hong Kong-specific
subjects that cover local geography, history, politics, and culture unique to Hong Kong.
Meanwhile, Basic Medical Sciences, Hong Kong Urban and Regional Planning, Hong Kong
Party Politics, and Hong Kong Film and Television are the subjects with the most questions
in their respective disciplines. Furthermore, Hong Kong Film and Television has the most
significant data volume among all subjects in HKMMLU, which has 2,201 questions.
15

--- Page 16 ---

Preprint. Under review.
Category
Subject
Q
Avg. Q
Max. Q
Min. Q
Avg. Q Tokens
Avg. C Tokens
STEM
18
6158
342.1
1020
103
34.8
36.6
Humanities
16
4834
302.1
1148
106
27.3
28.2
Social Science
18
8904
494.6
1440
110
17.9
24.2
Other
14
6802
485.9
2201
108
22.0
23.7
All
66
26698
404.5
2201
103
24.5
27.7
Table 6: The statistics of the HKMMLU, where Q represents the question and C indicates
the answer choices.
Table 6 displays a detailed statistical breakdown of the HKMMLU by category, including the
number of subjects, total questions, average number of questions per category, maximum
and minimum counts, and the average token length of both questions and choices.
B
Models Evaluated in this Paper
Model
Version
Model Size
Access
Creator
DeepSeek-V3
-
685B
API
deepseek
GPT-4o
20240806
undisclosed
API
OpenAI
Claude 3.7 Sonnet
20250219
undisclosed
API
Anthropic
Gemma-2-2B-IT
-
2.61B
weights
Google
Gemma-2-27B-IT
-
27.2B
weights
Google
GLM-4-9B-Chat
-
9.4B
weights
Tsinghua & Zhipu
Llama-3.1-8B-Instruct
20240723
8.03B
weights
Meta AI
Llama-3.1-70B-Instruct
20240723
70.6B
weights
Meta AI
Llama-3-Taiwan-8B-Instruct
-
8.03B
weights
Yen-Ting Lin
Llama-3-Taiwan-70B-Instruct
-
70.6B
weights
Yen-Ting Lin
Llama-3-8B-Instruct
20240418
8.03B
weights
Meta AI
Llama-3-70B-Instruct
20240418
70.6B
weights
Meta AI
Mistral-Small-Instruct
2409
22.2B
weights
Mistral AI
Mistral-Large-Instruct
2411
123B
weights
Mistral AI
Qwen2.5-3B-Instruct
-
3.09B
weights
Alibaba
Qwen2.5-7B-Instruct
-
7.61B
weights
Alibaba
Qwen2.5-14B-Instruct
-
14.7B
weights
Alibaba
Qwen2.5-72B-Instruct
-
72.7B
weights
Alibaba
Yi-1.5-9B-Chat
-
8.83B
weights
01.AI
Yi-1.5-34B-Chat
-
34.4B
weights
01.AI
Table 7: Models evaluated in this paper.
Table 7 outlines the models evaluated in this paper, including their versions, sizes, access
methods, and creators.
C
Detailed Results of Few-shot Prompting
Models
Shot Num
STEM
Soc. Sci.
Humanities
Other
Avg.
DeepSeek-V3
0
74.5
73.5
76.0
74.8
74.9
1
74.0
73.5
77.4
74.6
75.2
2
74.0
73.2
77.3
74.8
75.1
3
75.0
73.8
77.6
76.2
75.9
4
74.7
73.9
77.5
75.5
75.7
5
74.9
73.9
77.3
75.5
75.6
GPT-4o
0
75.0
70.4
68.6
67.9
70.3
1
74.7
68.7
68.4
66.6
69.5
2
74.3
69.1
69.4
67.9
70.1
3
74.0
69.2
68.8
67.2
69.7
4
74.2
68.9
69.1
68.0
70.0
16

--- Page 17 ---

Preprint. Under review.
5
75.0
68.9
69.2
67.3
70.0
Claude 3.7 Sonnet
0
74.3
69.4
63.0
62.1
66.7
1
74.1
69.8
68.3
62.8
68.7
2
74.3
69.2
66.7
62.8
68.1
3
74.2
68.4
63.8
62.1
66.8
4
57.7
67.3
68.8
59.1
63.7
5
46.3
49.6
48.4
45.2
47.4
Gemma-2-2B-IT
0
30.6
40.1
47.7
47.0
42.0
1
30.3
37.6
48.0
47.1
41.5
2
30.0
38.5
48.3
48.1
42.0
3
30.3
39.4
50.0
48.0
42.8
4
30.5
37.5
48.6
48.3
42.1
5
30.3
39.6
49.9
47.7
42.8
Gemma-2-27B-IT
0
55.7
55.4
59.7
57.5
57.4
1
55.0
55.8
59.4
58.0
57.3
2
55.3
56.0
60.0
57.8
57.6
3
54.4
55.7
59.5
58.6
57.3
4
54.7
55.8
59.8
58.2
57.5
5
55.2
56.0
60.3
57.9
57.7
GLM-4-9B-Chat
0
42.8
47.3
53.4
49.9
48.9
1
38.8
43.8
50.9
47.5
45.9
2
40.2
46.1
50.8
48.9
46.9
3
39.1
45.9
51.1
49.9
47.0
4
39.9
46.2
51.9
49.3
47.4
5
39.2
46.1
51.3
48.7
46.9
Llama-3.1-8B-Instruct
0
32.6
38.1
44.4
42.7
40.0
1
35.2
38.1
42.9
42.8
40.1
2
34.1
39.2
44.3
41.3
40.2
3
33.9
38.6
44.5
43.6
40.6
4
33.0
38.0
45.4
43.5
40.6
5
32.6
37.7
44.1
43.0
39.9
Llama-3.1-70B-Instruct
0
60.5
59.5
58.8
55.9
58.7
1
59.7
57.3
58.5
56.7
58.1
2
59.8
58.1
58.5
55.9
58.1
3
59.6
58.2
57.7
56.9
58.1
4
59.6
57.9
58.6
56.1
58.1
5
59.8
56.9
58.3
57.1
58.1
Llama-3-Taiwan-8B-Instruct
0
47.4
48.9
56.6
52.4
51.9
1
46.2
48.1
54.8
51.6
50.7
2
45.9
48.1
54.8
52.1
50.7
3
46.4
47.9
56.5
52.5
51.5
4
46.1
49.6
55.6
53.1
51.6
5
45.5
49.0
56.3
53.4
51.6
Llama-3-Taiwan-70B-Instruct
0
73.6
67.3
66.3
62.6
67.4
1
72.4
67.9
65.1
63.0
66.9
2
72.9
67.8
65.6
63.7
67.3
3
71.8
67.0
64.5
65.0
66.8
4
72.3
66.6
64.8
63.2
66.6
5
73.1
68.0
64.9
64.0
67.2
Llama-3-8B-Instruct
0
33.3
41.3
53.2
48.6
45.1
1
32.9
35.7
46.1
43.8
40.4
2
33.3
41.0
52.8
50.0
45.2
3
32.2
41.2
53.2
49.8
45.1
4
32.4
42.0
53.3
50.1
45.4
5
29.9
40.5
49.1
45.6
42.1
Llama-3-70B-Instruct
0
59.7
57.8
61.0
57.2
59.2
1
58.2
56.8
61.2
59.2
59.1
2
57.6
57.7
61.7
59.1
59.4
3
57.6
57.6
62.2
60.5
59.8
4
57.6
57.0
62.1
60.5
59.6
5
58.1
58.2
61.9
60.1
59.9
Mistral-Small-Instruct
0
38.9
42.1
49.4
47.8
45.1
1
41.3
43.6
51.1
50.2
47.1
2
40.7
43.5
51.9
49.4
47.0
3
41.8
42.4
52.8
48.6
47.2
4
41.3
43.3
52.5
48.6
47.1
17

--- Page 18 ---

Preprint. Under review.
5
41.7
43.4
53.3
49.0
47.6
Mistral-Large-Instruct
0
63.8
58.2
59.5
58.4
60.0
1
64.0
58.1
59.3
58.8
60.0
2
63.5
58.6
60.0
58.3
60.1
3
63.6
58.1
59.4
58.6
59.9
4
64.6
58.5
59.6
58.1
60.2
5
63.9
57.8
59.0
58.1
59.6
Qwen2.5-3B-Instruct
0
42.5
48.0
54.1
54.7
50.3
1
42.3
47.3
53.2
54.5
49.8
2
42.5
48.0
54.2
54.8
50.3
3
42.0
47.7
55.6
56.4
51.0
4
42.0
48.1
55.3
55.4
50.7
5
42.1
47.5
54.7
54.3
50.2
Qwen2.5-7B-Instruct
0
56.0
54.1
60.0
57.4
57.2
1
55.9
54.1
59.6
57.1
57.0
2
56.0
54.2
59.3
56.9
56.9
3
56.6
55.0
60.2
57.3
57.6
4
56.2
55.3
61.3
57.9
58.1
5
56.1
55.7
60.6
57.1
57.7
Qwen2.5-14B-Instruct
0
63.9
61.5
62.8
60.4
62.3
1
63.0
61.6
63.8
62.6
62.9
2
63.5
61.7
63.1
62.3
62.7
3
63.5
61.9
64.2
61.7
63.0
4
63.7
61.5
65.0
61.5
63.2
5
64.1
61.8
65.1
61.8
63.4
Qwen2.5-72B-Instruct
0
72.0
67.9
70.1
65.8
69.1
1
71.2
66.2
68.4
64.7
67.7
2
72.5
66.8
68.9
64.6
68.3
3
72.3
66.7
68.4
65.1
68.2
4
72.1
66.5
68.9
65.3
68.3
5
71.9
67.2
68.7
64.8
68.3
Yi-1.5-9B-Chat
0
45.4
51.6
56.9
54.3
52.5
1
44.9
53.0
58.3
56.0
53.6
2
46.1
53.3
59.4
58.6
54.9
3
46.8
54.2
60.9
57.9
55.6
4
46.5
54.0
59.9
58.1
55.2
5
47.0
54.6
60.8
58.8
55.9
Yi-1.5-34B-Chat
0
56.2
58.7
64.6
60.5
60.5
1
54.6
59.7
65.3
61.2
60.7
2
56.6
59.1
66.3
61.2
61.4
3
56.8
59.5
66.3
61.8
61.7
4
56.1
59.8
66.8
61.8
61.8
5
56.6
59.5
65.9
60.8
61.3
Table 8: Accuracy (%) in multi-choice tasks with different models, showing 0-shot to 5-shot
performance for each model.
We compared the detailed results of few-shot prompting on HKMMLU across four categories
in Table 8. We found that increasing the number of shots for a single model does not
necessarily improve its performance, underscoring the importance of knowledge acquisition
during the pre-training process. Specifically, Claude 3.7 Sonnet exhibits a sharp decline in
performance from 4-shot to 5-shot, with many responses being, “Sorry, I didn’t understand
your query. Can you provide more details?” This decline indicates that adding more
examples does not enhance performance but may lead to confusion.
D
Efficiency of Reasoning Examples for STEM and non-STEM Tasks
As shown in Table 9, in the STEM category, models such as DeepSeek-V3, GPT-4o, Gemma-
2-27B-IT, GLM-4-9B-Chat, the Llama-3 Taiwan series, the Llama-3 series, Qwen-2.5-3B/14B-
Instruct, and the Yi-1.5 series demonstrated a decline in performance after applying a
1-shot example. However, their performance significantly improved after incorporating the
18

--- Page 19 ---

Preprint. Under review.
Models
STEM
Non-STEM
DA
1s
1s-cot
DA
1s
1s-cot
DeepSeek-V3
74.5
74.0
81.0
75.0
75.5
74.2
GPT-4o
75.0
74.7
82.1
68.9
68.0
69.3
Claude 3.7 Sonnet
74.3
74.1
78.6
64.5
67.1
63.3
Gemma-2-2B-IT
30.6
30.3
30.2
45.4
44.9
38.8
Gemma-2-27B-IT
55.7
55.0
60.6
57.9
58.0
55.8
GLM-4-9B-Chat
42.8
38.8
51.2
50.7
48.0
51.0
Llama-3.1-8B-Instruct
32.6
35.2
29.0
42.2
41.6
30.0
Llama-3.1-70B-Instruct
60.5
59.7
43.2
58.1
57.7
38.5
Llama-3-Taiwan-8B-Instruct
47.4
46.2
48.3
53.3
52.0
52.0
Llama-3-Taiwan-70B-Instruct
73.6
72.4
74.4
65.5
65.2
64.1
Llama-3-8B-Instruct
33.3
32.9
37.6
48.6
42.6
48.2
Llama-3-70B-Instruct
59.7
58.2
62.4
59.0
59.4
59.9
Mistral-Small-Instruct
38.9
41.3
40.2
47.0
48.8
40.2
Mistral-Large-Instruct
63.8
64.0
51.7
58.8
58.8
48.6
Qwen2.5-3B-Instruct
42.5
42.3
41.8
52.6
52.0
44.7
Qwen2.5-7B-Instruct
56.0
55.9
56.3
57.6
57.4
53.2
Qwen2.5-14B-Instruct
63.9
63.0
64.7
61.8
62.9
60.8
Qwen2.5-72B-Instruct
72.0
71.2
71.1
68.3
66.7
65.2
Yi-1.5-9B-Chat
45.4
44.9
45.4
54.7
56.2
52.0
Yi-1.5-34B-Chat
56.2
54.6
55.5
61.8
62.6
58.9
Avg.
54.9
54.4
55.3
57.6
57.3
53.4
Table 9: Comparison results on DA, 1-shot and 1-shot-CoT.
reasoning process, surpassing the results of 0-shot. In contrast, this enhancement is rare in
non-STEM tasks, with only GPT-4o and GLM-4-9B-Chat exhibiting slight improvements
from the 1-shot CoT approach.
This trend may be because the STEM category primarily includes subjects such as Mathemat-
ics and Physics, which require a reasoning process. However, instructing the LLM to think
step-by-step does not guarantee a high-quality reasoning chain. Providing high-quality
reasoning examples enables the LLM to organize its thought process more effectively, lead-
ing to improved performance. This finding suggests that high-quality reasoning examples
significantly contribute to the accuracy of tasks that require systematic reasoning steps.
E
Simplified Chinese vs. Languages of Hong Kong
Simplified Chinese and Hong Kong languages share fundamental grammar, professional
terminology, and basic vocabulary but differ significantly in character forms, vocabulary
choices, grammatical habits, and cultural context. For example, simplified Chinese uses
streamlined characters (e.g., “体” vs. Traditional “體”), while Hong Kong has specific terms
like “MTR” (港鐵) that differ from mainland equivalents. Furthermore, Cantonese often
omits subjects and employs colloquial particles, requiring flexible grammatical parsing.
Therefore, cultural references and social issues unique to Hong Kong necessitate cultural
knowledge for accurate interpretation. To perform well on Hong Kong-related tasks in
the Hong Kong language, LLMs should incorporate region-specific vocabularies, flexible
grammatical parsing, and cultural knowledge bases to enhance understanding across
linguistic and cultural divides.
F
Model Performance Comparison: CMMLU, TMMLU+, and HKMMLU
Table 10 compares model performance on HKMMLU, CMMLU, and TMMLU+. These
results indicate that most models perform the best on CMMLU in STEM, Social Sciences, and
Humanities, while their performance is weaker on HKMMLU in STEM and Social Sciences.
This discrepancy indicates a deficiency in LLMs’ Traditional Chinese understanding abilities
and highlights the challenges presented in our benchmark.
19

--- Page 20 ---

Preprint. Under review.
Model
HKMMLU
CMMLU
TMMLU+
STEM
Soc.Sci
Humanities
Other
STEM
Soc.Sci
Humanities
Other
STEM
Soc.Sci
Humanities
Other
DeepSeek-V3
74.5
73.5
76.0
74.8
81.6
83.0
85.1
85.5
79.9
81.5
68.5
71.7
GPT-4o
75.0
70.4
68.6
67.9
73.4
77.0
78.0
81.3
76.1
80.7
62.5
70.7
Claude 3.7 Sonnet
74.3
69.4
63.0
62.1
72.7
67.9
74.4
76.6
74.7
81.3
69.2
70.3
Gemma-2-2B-IT
30.6
40.1
47.7
47.0
37.3
43.5
40.4
48.7
32.3
36.1
29.5
33.4
Gemma-2-27B-IT
55.7
55.4
59.7
57.5
58.7
63.0
62.0
68.9
57.3
63.1
45.6
53.0
GLM-4-9B-Chat
42.8
47.3
53.4
49.9
59.3
69.6
71.2
68.8
47.3
52.9
39.9
44.7
Llama-3.1-8B-Instruct
32.6
38.1
44.4
42.7
39.4
45.6
45.8
54.0
35.0
37.3
29.4
35.0
Llama-3.1-70B-Instruct
60.5
59.5
58.8
55.9
64.3
66.6
66.2
73.1
62.5
65.2
47.9
54.4
Llama-3-Taiwan-8B-Instruct
47.4
48.9
56.6
52.4
42.4
49.4
49.7
57.4
50.3
59.1
48.8
50.6
Llama-3-Taiwan-70B-Instruct
73.6
67.3
66.3
62.6
61.1
66.2
67.8
72.3
75.4
83.9
73.8
74.1
Llama-3-8B-Instruct
33.3
41.3
53.2
48.6
41.8
47.4
47.6
54.4
34.8
37.9
30.7
35.8
Llama-3-70B-Instruct
59.7
57.8
61.0
57.2
63.0
65.0
64.5
73.0
61.7
63.0
49.0
55.0
Mistral-Small-Instruct
38.9
42.1
49.4
47.8
43.4
50.6
48.8
56.1
39.3
43.1
31.5
37.9
Mistral-Large-Instruct
63.8
58.2
59.5
58.4
64.6
69.5
70.8
72.0
65.4
68.2
50.6
57.6
Qwen2.5-3B-Instruct
42.5
48.0
54.1
54.7
61.6
68.5
70.1
74.8
45.1
49.1
37.3
42.7
Qwen2.5-7B-Instruct
56.0
54.1
60.0
57.4
75.0
77.8
80.9
80.6
58.5
62.0
48.8
55.2
Qwen2.5-14B-Instruct
63.9
61.5
62.8
60.4
78.6
81.2
84.0
82.8
67.5
71.1
53.8
61.0
Qwen2.5-72B-Instruct
72.0
67.9
70.1
65.8
82.0
82.7
85.8
85.7
74.4
78.1
60.8
67.8
Yi-1.5-9B-Chat
45.4
51.6
56.9
54.3
64.9
72.4
73.7
75.8
49.3
56.6
43.7
47.5
Yi-1.5-34B-Chat
56.2
58.7
64.6
60.5
70.3
74.5
77.4
77.3
55.7
62.3
46.2
52.4
Avg.
54.9
55.6
59.3
56.9
61.8
66.1
67.2
71.0
57.1
61.6
48.4
53.5
Table 10: Model performance comparison on different MMLU Benchmark.
Model
HK-Specific
tc
sc
DeepSeek-V3
75.1
74.6
GPT-4o
67.8
68.1
Claude 3.7 Sonnet
61.9
64.1
Gemma-2-2B-IT
48.0
46.8
Gemma-2-27B-IT
57.7
57.1
GLM-4-9B-Chat
51.4
53.0
Llama-3.1-8B-Instruct
43.9
46.0
Llama-3.1-70B-Instruct
57.5
54.9
Llama-3-Taiwan-8B-Instruct
54.2
49.9
Llama-3-Taiwan-70B-Instruct
63.7
61.7
Llama-3-8B-Instruct
51.4
49.8
Llama-3-70B-Instruct
59.3
59.4
Mistral-Small-Instruct
48.4
47.6
Mistral-Large-Instruct
57.8
56.9
Qwen2.5-3B-Instruct
53.6
53.6
Qwen2.5-7B-Instruct
57.3
57.4
Qwen2.5-14B-Instruct
60.6
63.4
Qwen2.5-72B-Instruct
67.0
66.9
Yi-1.5-9B-Chat
55.4
54.4
Yi-1.5-34B-Chat
62.4
62.1
Avg.
57.7
57.4
Table 11: 0-shot results of models on Hong Kong-specific (HK-specific) subject in HKMMLU.
G
Model Performance on Hong Kong-specific Tasks
Table 11 presents the performance of models on 23 subjects closely related to Hong Kong-
specific knowledge. DeepSeek-V3 demonstrates superior performance in both Traditional
Chinese and Simplified Chinese versions. Additionally, the Llama-3 Taiwan series does not
exhibit the same advantages as the whole benchmark when focusing on Hong Kong-specific
questions. This discrepancy may be due to their enhanced language capability in Traditional
Chinese rather than an improvement in knowledge specific to Hong Kong.
H
Model Performance by Subject
Figures 8 and Figure 9 respectively present the 0-shot and 1-shot CoT results for various
models across all subjects in HKMMLU.
20

--- Page 21 ---

Preprint. Under review.
DeepSeek-V3
GPT-4o
Claude 3.7 Sonnet
Gemma-2-2B-IT
Gemma-2-27B-IT
GLM-4-9B-Chat
Llama-3.1-8B-Instruct
Llama-3.1-70B-Instruct
Llama-3-Taiwan-8B-Instruct
Llama-3-Taiwan-70B-Instruct
Llama-3-8B-Instruct
Llama-3-70B-Instruct
Mistral-Large-Instruct
Mistral-Small-Instruct
Qwen2.5-3B-Instruct
Qwen2.5-7B-Instruct
Qwen2.5-14B-Instruct
Qwen2.5-72B-Instruct
Yi-1.5-9B-Chat
Yi-1.5-34B-Chat
Models
Basic Medical Science
Business Management
Chinese History
Chinese National Conditions
Chinese and World Culture
Chinese and World Geography
Clinical Psychology
College Math
Cultural Commonsense
Dentistry
Economics
Educational Psychology
Financial Analysis
Fire Science
HKDSE Biology
HKDSE Business, Accounting and Financial Studies
HKDSE Chemistry
HKDSE Economics
HKDSE Geography
HKDSE Information and Communication Technology
HKDSE Mathematics
HKDSE Physics
HKDSE Tourism and Hospitality
Hong Kong Celebrity
Hong Kong Cultural Art
Hong Kong Current Affairs
Hong Kong Education
Hong Kong Entertainment Industry and Management
Hong Kong Events and Festivals
Hong Kong Film and Television
Hong Kong Government and Political System
Hong Kong Historical Geography and Development
Hong Kong History
Hong Kong Human Geography
Hong Kong Law
Hong Kong Life Knowledge
Hong Kong Literature
Hong Kong Livelihood
Hong Kong Music
Hong Kong Party Politics
Hong Kong Physical Geography
Hong Kong Physical Transport and Infrastructure
Hong Kong Politicians and Events
Hong Kong Society
Hong Kong Transportation
Hong Kong Urban and Regional Development
Human Behavior
Insurance Studies
Logic Reasoning
Management Accounting
Marketing Management
Mechanical
Nautical Science
Optometry
Organic Chemistry
Pharmacology
Pharmacy
Physics
Science and Technology Commonsense
Social Commonsense
Statistics and Machine Learning
Technical Skills
Traditional Chinese Medicine Clinical Medicine
Veterinary Pathology
Veterinary Pharmacology
World Entertainment
Subjects
88.2 93.6 90.2 29.9 66.7 48.9 32.7 76.4 52.0 87.4 31.9 74.7 77.9 40.0 45.1 64.5 75.3 86.3 51.7 67.5
70.1 68.8 68.2 37.4 62.6 57.4 38.7 61.9 58.7 74.8 40.6 57.4 62.6 49.0 54.8 65.2 66.5 65.8 56.8 59.4
80.7 79.8 83.5 33.6 65.5 59.1 37.3 69.1 59.1 69.1 46.4 76.4 76.4 44.5 67.3 71.8 80.0 82.7 72.7 75.5
82.1 82.1 76.9 61.0 72.0 66.9 52.5 73.7 65.3 82.2 60.2 73.7 78.0 55.1 59.3 65.3 78.8 85.6 65.3 75.4
85.0 79.1 75.2 44.2 64.3 62.3 46.1 67.5 52.6 72.1 49.4 62.3 67.5 51.3 55.2 61.7 68.8 81.8 57.1 67.5
88.5 83.6 84.8 46.4 69.3 56.6 56.6 78.3 65.7 75.9 54.8 70.5 70.5 56.6 62.0 68.7 77.7 78.3 63.3 75.9
80.5 84.4 85.9 32.6 69.0 51.9 36.4 69.0 59.7 88.4 40.3 70.5 79.8 48.8 50.4 72.1 76.7 85.3 58.1 63.6
55.4 41.1 50.3 23.9 38.1 25.0 18.8 41.5 27.3 53.4 27.3 42.6 45.5 30.7 34.7 35.8 44.9 53.4 35.8 38.1
76.2 69.5 64.6 45.5 65.5 53.3 47.3 64.8 55.2 65.5 50.3 66.1 66.7 48.5 56.4 61.8 62.4 69.1 57.0 69.1
72.9 75.9 74.9 30.1 57.8 44.6 37.2 58.4 50.7 78.0 33.1 61.1 62.8 40.5 41.2 56.4 59.5 70.9 44.9 52.0
79.6 75.9 74.4 33.1 57.1 43.6 29.3 59.9 39.3 77.2 28.3 55.1 62.9 36.6 45.1 55.4 67.4 71.9 50.1 58.6
82.6 78.5 89.0 39.9 59.5 53.2 34.1 74.6 63.0 82.7 42.2 63.6 69.9 50.9 54.9 63.0 70.5 79.8 62.4 66.5
78.5 73.7 71.1 24.5 53.3 39.7 30.1 57.2 40.6 70.7 31.9 51.5 59.8 30.6 42.4 51.5 61.6 68.1 48.5 58.1
59.7 57.5 62.7 28.9 48.1 28.9 25.9 47.4 44.4 65.2 30.4 51.9 45.2 36.3 37.0 46.7 57.8 55.6 45.9 41.5
81.3 82.7 79.1 32.1 62.9 53.6 36.4 68.6 50.7 63.6 41.4 62.1 72.1 40.0 54.3 67.9 70.7 76.4 55.7 62.9
76.0 79.1 78.2 32.7 61.9 50.9 31.4 61.9 43.4 64.2 32.7 57.1 63.7 38.1 47.8 58.4 70.4 75.7 53.5 61.1
64.4 62.8 68.8 29.1 51.6 47.2 33.1 52.8 32.3 52.0 31.9 46.9 55.5 33.9 38.2 51.6 58.7 62.6 40.9 52.8
62.8 69.9 70.4 31.7 48.9 47.6 34.4 57.3 40.1 53.7 37.9 51.5 59.0 36.6 43.6 48.0 60.4 67.0 48.0 52.9
72.1 75.5 81.0 39.2 54.7 61.5 37.8 64.9 51.4 66.9 43.9 57.4 66.9 48.0 44.6 64.2 73.6 75.7 58.1 61.5
81.9 84.4 83.8 40.0 69.7 63.3 41.7 75.0 61.1 74.4 46.9 72.5 76.7 58.1 58.1 73.1 78.6 82.5 66.9 69.2
53.0 34.4 48.1 26.1 27.7 28.8 25.0 31.5 20.7 29.9 27.7 35.3 35.9 33.2 30.4 27.7 35.3 42.9 29.9 28.8
64.7 60.8 57.8 21.4 43.7 41.7 35.9 54.4 31.1 58.3 23.3 43.7 54.4 35.0 36.9 48.5 53.4 61.2 45.6 47.6
74.3 78.9 75.5 43.7 63.0 58.0 41.2 68.1 47.9 67.2 41.2 60.9 63.0 45.8 52.1 63.0 68.9 75.6 55.0 63.9
77.1 68.5 59.5 59.2 68.4 60.9 51.2 61.5 61.0 66.1 60.5 65.0 60.1 63.7 64.8 70.3 66.2 70.8 64.3 67.3
83.9 77.0 72.0 50.6 65.4 55.6 46.9 64.2 58.6 74.1 56.8 67.9 65.4 56.8 65.4 68.5 72.2 72.2 63.0 72.2
83.4 80.9 74.4 51.1 66.5 62.2 50.0 69.1 61.9 75.9 61.5 66.9 71.2 56.1 61.5 69.4 75.9 80.9 61.9 72.3
62.3 55.1 49.8 40.0 44.8 43.4 37.5 45.3 44.0 56.0 38.4 48.8 48.2 39.5 47.0 50.1 52.9 55.2 46.8 51.5
84.4 77.3 72.1 49.7 67.1 58.1 52.3 66.5 60.0 73.5 63.9 68.4 65.2 62.6 60.6 62.6 63.9 76.1 61.9 72.9
79.4 75.7 68.2 42.6 62.0 50.9 39.8 54.6 52.8 63.9 50.9 60.2 58.3 43.5 47.2 57.4 63.9 65.7 55.6 65.7
77.6 69.5 62.6 50.4 59.1 51.4 43.8 56.4 54.3 60.2 51.5 56.8 59.7 49.3 56.2 57.1 60.9 65.6 55.0 61.8
85.7 80.0 73.9 53.0 65.1 55.5 54.1 61.9 58.7 73.3 60.1 64.8 60.1 54.4 59.8 62.6 67.3 77.9 64.4 72.2
71.8 64.8 68.3 39.2 52.4 51.7 42.0 57.3 51.7 62.2 51.0 53.8 53.1 47.6 50.3 56.6 55.9 62.9 51.7 64.3
75.5 63.8 62.7 44.6 61.3 49.1 40.6 54.3 55.0 62.9 49.1 62.8 58.5 49.5 57.4 57.6 59.5 67.3 55.9 63.8
79.7 70.6 70.7 45.4 56.2 48.9 45.1 64.1 53.9 69.4 50.2 63.4 57.6 37.4 48.7 49.5 56.7 67.0 55.0 66.8
84.7 76.9 74.2 52.3 69.5 64.2 53.3 69.5 63.4 78.5 59.6 75.8 74.3 58.4 66.6 70.0 76.8 78.7 65.1 74.1
74.9 71.3 53.5 44.3 59.0 49.1 43.7 54.5 50.3 64.8 44.9 58.4 59.9 47.0 53.9 58.7 64.5 68.1 54.5 65.4
60.4 55.0 56.4 37.9 51.7 46.3 36.5 46.3 44.8 53.2 41.4 47.8 47.3 38.9 49.8 43.3 54.2 58.1 46.8 48.8
78.2 68.3 64.9 45.9 58.3 52.6 42.7 56.9 55.9 69.4 50.4 62.7 61.0 48.2 57.3 59.7 65.4 71.2 58.5 61.8
67.4 63.3 55.1 51.4 53.7 46.5 40.6 52.2 47.2 56.7 47.5 52.6 53.4 49.1 52.1 55.9 54.6 58.8 52.9 56.0
70.8 61.1 50.3 45.0 50.9 50.2 38.5 50.8 55.4 56.7 55.3 52.6 50.6 45.1 39.2 56.7 56.9 68.8 48.8 57.1
73.4 65.9 65.5 43.2 57.9 47.4 43.2 60.7 50.2 63.1 43.2 63.0 55.3 43.8 48.8 48.8 59.5 64.9 53.7 59.7
75.5 72.9 66.7 46.3 57.1 49.1 42.6 62.3 50.9 64.3 47.2 59.1 58.0 50.0 50.0 56.1 59.1 64.9 50.9 64.1
74.9 76.8 59.6 50.4 64.9 59.3 49.3 64.6 63.4 69.0 65.3 63.8 63.4 60.4 61.9 66.8 69.8 73.1 64.2 70.5
79.3 73.4 62.2 50.1 66.9 58.0 47.8 62.9 64.6 73.1 55.7 63.2 69.2 56.5 63.4 64.8 66.9 73.7 65.4 70.6
62.5 54.3 57.1 37.7 47.8 39.7 38.5 49.7 42.2 53.1 39.4 51.1 47.2 41.1 44.7 47.2 49.7 54.7 44.1 48.0
76.5 71.1 66.4 49.9 52.4 49.7 44.5 59.8 53.9 65.7 52.0 60.9 57.6 42.5 53.6 51.2 57.0 66.7 54.3 63.4
82.1 82.1 80.7 37.4 71.7 56.9 36.7 68.7 64.0 88.9 37.4 69.0 73.1 44.8 52.5 68.7 75.1 80.5 64.3 69.4
72.6 78.6 70.9 43.2 59.3 50.0 35.6 61.0 55.1 83.1 39.0 61.9 62.7 39.8 43.2 65.3 66.9 74.6 54.2 62.7
57.6 48.1 50.0 23.9 34.0 33.3 25.8 39.0 35.8 47.8 28.9 32.1 42.1 28.3 39.0 43.4 40.3 52.2 34.0 44.0
66.3 54.1 54.1 29.9 42.6 29.9 28.4 46.2 32.5 55.8 29.4 42.1 48.7 28.9 35.0 44.2 52.3 58.9 43.1 37.1
81.0 87.6 87.6 46.2 80.2 62.3 47.2 70.8 71.7 84.9 43.4 76.4 76.4 55.7 61.3 78.3 80.2 80.2 67.0 70.8
76.9 79.6 79.6 46.8 64.2 52.3 45.0 66.1 59.6 78.0 52.3 63.3 67.9 54.1 63.3 71.6 76.1 80.7 64.2 63.3
59.5 54.9 59.0 31.7 43.9 36.1 29.4 42.7 38.3 60.6 32.3 43.2 42.6 35.3 35.3 43.2 49.8 58.4 36.0 42.7
57.6 58.3 60.0 26.0 41.0 33.9 24.7 43.2 37.6 64.2 28.7 42.8 47.7 29.6 30.8 42.5 50.4 57.4 33.4 44.3
74.6 73.8 70.0 33.6 54.2 39.7 29.0 51.9 47.3 70.2 32.1 66.4 64.9 47.3 45.0 48.1 60.3 66.4 42.0 54.2
79.5 85.1 82.6 31.0 62.1 37.9 38.1 70.3 62.4 86.0 34.4 68.2 71.3 46.1 44.7 58.5 67.4 72.7 45.5 59.7
59.3 60.2 61.6 23.7 44.3 30.9 24.0 45.1 33.1 65.1 22.9 45.4 53.1 28.3 31.1 39.7 49.7 60.0 31.7 42.6
76.3 65.8 70.2 28.7 51.3 43.5 31.3 53.0 36.5 59.1 33.0 54.8 67.0 36.5 53.0 53.0 58.3 70.4 40.9 52.2
89.4 78.0 76.4 50.0 66.9 58.1 54.8 67.7 56.5 79.0 55.6 73.4 73.4 58.1 66.1 71.0 74.2 83.9 63.7 73.4
84.0 80.9 74.5 42.3 61.4 58.2 52.4 67.2 62.4 73.5 48.1 65.1 67.7 42.3 60.8 66.1 68.8 77.8 57.7 73.0
84.8 75.7 76.5 37.3 62.3 44.3 29.5 66.4 45.9 75.8 38.5 61.5 69.3 43.9 45.1 69.3 71.7 82.8 52.9 61.1
73.0 72.2 71.9 41.4 60.0 50.1 38.3 58.3 55.4 75.4 42.0 56.8 59.1 45.2 56.8 59.4 66.1 71.9 51.9 58.6
72.2 63.9 58.8 30.2 44.2 40.3 26.3 46.8 37.1 61.9 32.7 51.4 52.2 32.4 39.2 57.9 61.9 73.4 48.2 61.9
75.4 82.5 72.8 27.1 51.6 40.3 30.0 58.4 45.2 82.3 26.1 54.5 60.0 30.0 43.2 53.2 65.2 70.6 41.6 52.9
89.4 90.6 88.2 38.0 69.2 49.9 45.1 74.7 64.5 89.4 42.1 74.5 76.3 45.4 51.0 66.7 75.0 83.9 51.6 65.3
76.4 69.3 65.9 47.5 60.5 50.1 42.9 57.3 56.0 65.7 55.3 61.1 61.6 49.4 56.9 60.0 62.7 73.0 53.2 64.8
20
30
40
50
60
70
80
90
Figure 8: 0-shot accuracy for 20 models across all subjects in HKMMLU
21

--- Page 22 ---

Preprint. Under review.
DeepSeek-V3
GPT-4o
Claude 3.7 Sonnet
Gemma-2-2B-IT
Gemma-2-27B-IT
GLM-4-9B-Chat
Llama-3.1-8B-Instruct
Llama-3.1-70B-Instruct
Llama-3-Taiwan-8B-Instruct
Llama-3-Taiwan-70B-Instruct
Llama-3-8B-Instruct
Llama-3-70B-Instruct
Mistral-Large-Instruct
Mistral-Small-Instruct
Qwen2.5-3B-Instruct
Qwen2.5-7B-Instruct
Qwen2.5-14B-Instruct
Qwen2.5-72B-Instruct
Yi-1.5-9B-Chat
Yi-1.5-34B-Chat
Models
Basic Medical Science
Business Management
Chinese History
Chinese National Conditions
Chinese and World Culture
Chinese and World Geography
Clinical Psychology
College Math
Cultural Commonsense
Dentistry
Economics
Educational Psychology
Financial Analysis
Fire Science
HKDSE Biology
HKDSE Business, Accounting and Financial Studies
HKDSE Chemistry
HKDSE Economics
HKDSE Geography
HKDSE Information and Communication Technology
HKDSE Mathematics
HKDSE Physics
HKDSE Tourism and Hospitality
Hong Kong Celebrity
Hong Kong Cultural Art
Hong Kong Current Affairs
Hong Kong Education
Hong Kong Entertainment Industry and Management
Hong Kong Events and Festivals
Hong Kong Film and Television
Hong Kong Government and Political System
Hong Kong Historical Geography and Development
Hong Kong History
Hong Kong Human Geography
Hong Kong Law
Hong Kong Life Knowledge
Hong Kong Literature
Hong Kong Livelihood
Hong Kong Music
Hong Kong Party Politics
Hong Kong Physical Geography
Hong Kong Physical Transport and Infrastructure
Hong Kong Politicians and Events
Hong Kong Society
Hong Kong Transportation
Hong Kong Urban and Regional Development
Human Behavior
Insurance Studies
Logic Reasoning
Management Accounting
Marketing Management
Mechanical
Nautical Science
Optometry
Organic Chemistry
Pharmacology
Pharmacy
Physics
Science and Technology Commonsense
Social Commonsense
Statistics and Machine Learning
Technical Skills
Traditional Chinese Medicine Clinical Medicine
Veterinary Pathology
Veterinary Pharmacology
World Entertainment
Subjects
91.5 94.3 36.2 28.3 68.5 54.3 30.0 56.6 52.5 87.7 39.9 74.7 77.1 50.2 42.6 64.7 78.9 88.2 48.2 66.8
68.2 68.2 42.9 37.0 60.4 57.8 31.8 40.9 61.0 74.7 35.1 61.7 44.8 29.9 54.5 64.9 59.1 66.2 58.4 59.7
82.6 82.6 55.0 30.3 67.0 67.9 32.1 47.7 62.4 70.6 50.5 68.8 63.3 45.0 59.6 70.6 77.1 84.4 69.7 80.7
88.0 82.1 60.7 47.0 70.9 58.1 39.3 37.6 63.2 80.3 56.4 70.9 59.8 47.0 63.2 68.4 74.4 80.3 67.5 73.5
85.0 85.6 63.4 43.8 66.0 55.6 31.4 49.7 51.6 75.8 42.5 66.0 71.2 50.3 53.6 65.4 66.7 79.1 53.6 62.7
86.7 86.1 50.3 48.5 71.5 64.8 35.2 42.4 55.8 78.8 55.2 72.7 63.6 44.8 64.2 67.9 77.0 79.4 65.5 69.1
85.2 86.7 32.8 32.8 65.6 56.2 28.1 33.6 59.4 87.5 48.4 64.1 43.8 38.3 45.3 65.6 72.7 80.5 53.9 63.3
73.1 65.7 43.4 22.9 48.0 27.4 25.1 38.9 28.6 49.7 28.6 53.1 29.7 24.6 26.9 29.7 29.7 29.7 36.0 33.1
71.3 70.7 59.1 36.0 53.7 54.3 34.8 44.5 52.4 66.5 49.4 64.6 64.6 48.8 47.0 56.1 61.6 68.9 53.7 67.1
74.2 77.6 38.3 28.8 54.6 50.2 26.8 34.9 58.0 77.3 34.9 58.6 27.1 25.8 35.6 49.5 54.9 68.8 37.6 48.8
88.7 87.4 51.5 23.1 64.1 53.3 29.9 47.2 37.2 75.6 34.4 63.6 50.3 34.4 38.9 56.3 71.4 75.4 47.7 58.5
81.4 83.1 39.5 33.7 61.0 56.4 33.7 37.8 63.4 79.7 43.0 64.0 46.5 41.3 49.4 63.4 73.3 73.8 61.0 66.9
87.3 90.8 51.3 27.6 73.2 51.3 29.4 52.6 46.9 75.9 38.2 63.2 65.4 44.3 47.8 63.2 71.9 82.0 57.9 58.8
73.9 71.6 29.9 30.6 54.5 45.5 29.9 44.0 47.8 67.9 29.9 48.5 45.5 38.1 43.3 54.5 56.0 71.6 42.5 50.0
82.0 84.9 36.0 37.4 67.6 56.1 23.7 44.6 42.4 66.9 43.9 59.0 67.6 46.0 47.5 66.9 74.8 79.1 50.4 64.0
77.8 80.0 45.3 33.8 70.2 61.3 32.0 40.0 44.4 68.4 41.3 69.8 63.6 43.6 48.9 67.1 76.4 81.3 58.7 63.6
77.9 76.3 35.6 30.8 59.3 58.1 27.7 43.9 34.0 52.6 34.0 56.1 43.5 33.6 37.9 53.0 60.1 63.6 43.5 49.4
71.2 74.8 42.9 29.6 57.1 50.4 26.1 36.3 34.5 56.2 36.3 56.6 50.0 31.4 39.4 50.9 61.9 68.6 46.9 55.8
78.2 77.6 63.9 38.1 59.2 57.8 36.1 40.8 41.5 66.7 35.4 63.3 57.8 43.5 54.4 66.0 74.1 76.2 51.0 59.2
90.0 86.9 46.2 38.7 79.7 72.7 35.9 51.3 54.3 73.0 51.3 81.6 73.0 64.9 57.7 76.6 82.7 83.0 65.2 73.5
89.6 80.3 74.3 23.0 55.2 40.4 22.4 46.4 24.6 41.5 30.1 58.5 51.4 45.4 41.0 57.4 57.9 60.1 37.7 42.1
85.3 77.5 59.8 23.5 59.8 49.0 27.5 43.1 31.4 63.7 33.3 54.9 44.1 25.5 34.3 43.1 56.9 58.8 40.2 48.0
75.5 77.2 53.2 35.9 57.0 62.0 28.3 42.2 45.6 70.5 40.9 65.4 49.8 29.5 45.6 59.9 70.0 73.0 54.9 61.6
79.0 69.6 43.8 46.6 66.0 58.6 31.0 39.7 61.3 64.8 58.3 68.1 51.5 58.9 53.8 62.0 63.8 68.0 58.7 60.8
83.9 68.3 47.8 44.7 55.3 56.5 23.0 36.0 59.0 71.4 52.8 68.9 41.0 34.2 49.1 54.7 70.2 70.2 55.9 69.6
74.7 79.8 48.7 33.2 60.6 59.2 27.4 33.6 61.7 71.8 48.4 62.8 45.8 32.9 49.1 56.3 68.6 71.1 60.3 66.4
60.4 57.6 34.4 28.0 45.0 40.7 29.4 33.2 43.2 53.2 42.4 49.4 44.4 36.8 38.0 47.2 49.1 51.9 46.5 49.9
81.8 75.3 36.4 44.2 64.3 55.8 31.8 35.1 57.1 68.2 49.4 64.9 49.4 29.2 46.1 55.8 65.6 70.1 57.1 66.9
75.7 71.0 47.7 37.4 53.3 44.9 35.5 43.9 56.1 66.4 48.6 58.9 39.3 31.8 50.5 48.6 57.0 56.1 45.8 54.2
73.3 69.5 47.3 41.5 55.1 49.1 27.6 38.6 51.9 60.4 49.5 59.1 48.6 44.5 46.9 52.1 59.4 63.0 51.2 60.9
83.9 75.7 47.5 40.4 62.5 53.9 34.3 39.6 59.3 70.7 52.5 58.2 40.4 31.1 52.9 60.0 69.3 74.6 61.1 69.3
66.9 62.7 53.5 43.0 54.2 51.4 28.2 30.3 50.0 66.9 47.2 59.2 43.0 32.4 42.3 47.2 47.9 55.6 54.9 61.3
74.4 68.1 38.6 42.2 56.9 48.5 30.6 35.5 54.6 62.3 49.4 60.2 45.9 48.1 47.4 49.5 58.2 63.2 52.1 60.7
76.7 70.9 61.4 44.6 55.7 46.8 30.3 39.4 55.5 68.4 51.0 63.0 50.8 36.9 38.0 42.5 54.7 61.0 56.2 65.1
84.7 81.3 58.6 43.9 64.1 63.3 36.4 36.7 62.8 75.7 62.0 72.8 51.3 48.7 59.5 70.6 73.5 79.8 66.2 70.1
66.2 69.8 38.1 38.1 50.8 48.9 28.7 32.9 49.5 61.0 44.1 59.2 50.5 43.8 42.0 51.7 58.6 63.4 49.2 59.2
58.4 53.0 51.5 32.7 38.6 42.6 22.3 33.7 46.0 47.0 38.1 41.6 39.1 33.7 39.1 43.6 52.0 51.0 45.0 49.0
76.8 71.4 43.7 41.3 48.2 51.1 30.6 37.8 56.5 66.3 49.8 63.6 41.0 29.9 50.9 56.0 64.2 65.7 55.8 60.7
66.9 59.6 36.5 42.5 50.7 46.1 28.1 37.4 50.3 55.4 50.8 53.3 42.0 37.1 43.1 46.8 50.1 54.7 50.0 53.3
66.8 46.8 43.6 35.9 45.5 49.4 27.2 31.5 41.2 52.8 57.8 47.6 39.1 31.3 31.3 50.9 61.8 61.7 46.3 48.5
73.4 65.5 52.7 37.3 54.6 50.1 28.3 38.6 54.4 65.1 45.3 62.4 53.7 42.1 39.1 45.0 55.4 59.0 42.5 56.9
67.1 66.0 50.2 35.9 52.2 48.9 29.7 39.0 49.6 62.8 39.2 59.5 43.7 28.8 36.6 45.9 53.0 56.1 48.7 56.5
74.9 70.8 47.6 47.6 59.6 59.9 34.1 37.8 59.9 64.8 59.2 60.3 55.1 46.4 46.8 58.1 65.9 70.8 60.7 62.9
79.3 71.5 47.7 45.2 58.7 56.8 31.0 38.8 61.6 66.7 51.9 62.2 46.7 45.0 54.5 55.0 67.2 71.9 58.1 63.0
62.2 58.5 42.9 30.3 46.8 38.4 29.1 37.0 42.6 52.9 38.4 50.4 44.0 37.0 35.9 46.8 48.2 53.5 45.1 48.2
74.8 72.7 49.7 41.4 53.7 47.9 34.2 44.3 55.9 64.3 53.7 64.2 52.4 38.9 40.5 47.0 57.0 64.1 51.2 61.3
80.1 82.4 34.1 36.8 69.6 61.5 34.1 47.3 66.9 85.8 43.2 68.6 54.1 49.0 50.3 69.9 71.3 79.7 56.1 68.2
83.8 77.8 35.9 32.5 59.8 60.7 36.8 41.0 54.7 76.9 47.0 55.6 41.9 41.0 47.9 65.8 70.1 76.1 48.7 48.7
76.6 75.3 66.5 33.5 48.7 43.0 25.9 36.7 36.7 45.6 33.5 47.5 47.5 29.7 42.4 42.4 52.5 55.1 46.2 41.8
79.6 77.0 54.6 25.0 55.6 37.2 25.0 47.4 33.7 59.2 35.7 56.6 37.2 30.1 31.1 46.9 56.6 62.8 39.8 41.8
85.7 85.7 31.4 44.8 78.1 69.5 28.6 48.6 68.6 87.6 52.4 74.3 48.6 55.2 63.8 74.3 81.9 83.8 63.8 80.0
85.2 84.3 32.4 38.9 65.7 69.4 38.0 46.3 61.1 80.6 49.1 69.4 50.9 51.9 60.2 74.1 80.6 82.4 63.0 63.9
64.6 63.8 38.5 26.0 47.9 37.2 29.9 34.2 39.3 55.7 32.2 47.9 47.1 36.7 35.2 41.3 52.4 58.3 34.2 39.7
62.8 66.1 34.0 26.7 44.3 36.7 28.5 30.6 39.7 65.4 31.0 42.1 37.0 29.4 34.2 42.4 47.5 55.1 37.8 43.5
78.5 83.1 30.0 38.5 61.5 49.2 23.1 32.3 51.5 67.7 33.1 63.8 38.5 35.4 35.4 48.5 59.2 60.0 43.1 45.4
83.4 89.2 28.6 31.7 64.6 56.2 28.8 43.8 62.7 85.1 40.5 70.8 58.6 43.1 43.3 55.6 65.9 75.3 45.6 54.4
73.1 73.1 35.2 22.6 51.0 35.8 28.9 37.0 37.2 66.2 28.1 51.6 48.1 33.2 30.1 45.8 50.1 61.6 34.1 43.0
91.2 87.7 61.4 26.3 65.8 60.5 29.8 35.1 43.0 64.9 33.3 64.0 50.9 36.0 56.1 58.8 63.2 66.7 40.4 50.9
85.4 81.3 43.1 46.3 70.7 64.2 34.1 39.0 61.0 77.2 52.8 68.3 63.4 44.7 63.4 71.5 78.9 77.2 60.2 69.9
85.6 79.8 43.1 39.4 59.6 59.6 31.9 41.5 53.2 71.3 46.3 66.5 67.0 50.0 55.3 60.6 71.3 74.5 55.9 69.7
92.2 91.8 44.9 36.6 72.0 60.1 33.3 63.0 48.1 79.8 44.0 68.7 67.9 65.0 55.6 74.9 83.1 83.5 58.4 65.0
75.7 77.1 40.9 42.0 60.6 54.5 27.8 42.3 54.8 73.0 43.5 59.1 48.4 43.5 49.9 59.1 62.9 73.6 49.3 60.3
75.1 64.6 34.3 27.8 38.6 49.5 24.9 33.9 41.2 62.1 27.4 47.7 28.2 23.8 39.7 53.4 57.4 61.4 43.7 64.6
75.4 83.8 40.8 29.1 53.4 48.2 26.5 34.0 42.7 81.2 32.4 55.0 41.1 29.4 40.1 49.5 65.7 72.5 44.0 47.6
90.1 92.7 32.1 36.3 76.7 59.7 30.4 46.0 64.4 89.9 47.9 74.3 43.6 41.7 47.2 64.4 74.8 79.0 50.2 64.6
74.5 69.8 51.0 39.1 56.9 52.3 30.2 36.5 50.5 65.3 47.9 63.5 55.8 44.5 45.9 52.8 60.6 65.0 48.5 61.0
30
40
50
60
70
80
90
Figure 9: 1-shot CoT accuracy for 20 models across all subjects in HKMMLU
22

--- Page 23 ---

Preprint. Under review.
Model
Accuracy Rate
Num. UQ
Num. UC
DeepSeek-V3
96
0
4
GPT-4o
97
1
2
Claude 3.7 Sonnet
99
1
0
Avg.
97.33
0.67
2
Table 12: The quality details of multi-choice that converted from question-answer pairs
in HKMMLU, where “Num. UQ” represents the number of unreasonable questions and
“Num. UC” indicates the number of unreasonable choices.
I
Details of Human Review
To ensure the quality of HKMMLU, we manually reviewed the multi-choice questions
processed by the LLMs, including DeepSeek-V3, GPT-4o, and Claude 3.7 Sonnet. For each
model, we manually checked 100 randomly selected questions. We assess the reasonableness
of the question and answer choices. Results are displayed in Table 12. Additionally, to
ensure the safety and ethical standards of HKMMLU, we have manually filtered out sensitive
words.
J
Prompts
J.1
Inference Prompts
Inference prompt for few-shot prompting is shown in Figure 10, for CoT prompting in
Figure 11, and for translation tasks in Figure 12.
香港特別行政區是中華人民共和國的一個特別行政區。香港位於珠江口東側，毗鄰廣東省深圳市，由香港島、九龍半
島、新界等組成。香港是國際金融、航運、貿易中心之一，也是全球最自由經濟體之一。
(Hong Kong Special Administrative Region is a special administrative region of the People‘s Republic of China. Hong Kong is 
located on the eastern side of the Pearl River Estuary, adjacent to Shenzhen City in Guangdong Province. It is made up of 
Hong Kong Island, Kowloon Peninsula, and the New Territories. Hong Kong is one of the international financial, shipping, 
and trade centers, and is also one of the freest economies in the world.)
作爲一個精通香港繁體字和{subject}的專家，請完成以下繁體中文單選題。
(As an expert proficient in Hong Kong traditional Chinese characters and {subject}, please complete the following multiple-
choice question in traditional Chinese.)
答題要求：(Answer requirements: )
1. 請只輸出A/B/C/D選項字母 (Please only output the letters A/B/C/D)
2. 不需要解釋或其他註釋 (No explanations or other comments are needed)
3. 答案必須準確無誤 (The answer must be accurate)
…[examples]
請回答以下問題：(Please answer the following question:)
Figure 10: Few-shot prompt for multi-choice tasks in Traditional Chinese. 0-shot prompting
involves no examples. English sentences in blue are not part of the inference process.
23

--- Page 24 ---

Preprint. Under review.
香港特別行政區是中華人民共和國的一個特別行政區。香港位於珠江口東側，毗鄰廣東省深圳市，由香港島、九龍半
島、新界等組成。香港是國際金融、航運、貿易中心之一，也是全球最自由經濟體之一。
(Hong Kong Special Administrative Region is a special administrative region of the People‘s Republic of China. Hong Kong is 
located on the eastern side of the Pearl River Estuary, adjacent to Shenzhen City in Guangdong Province. It is made up of 
Hong Kong Island, Kowloon Peninsula, and the New Territories. Hong Kong is one of the international financial, shipping, 
and trade centers, and is also one of the freest economies in the world.)
作爲一個精通香港繁體字和{subject}的專家，請完成以下繁體中文單選題。
(As an expert proficient in Hong Kong traditional Chinese characters and {subject}, please complete the following multiple-
choice question in traditional Chinese.)
…[Reasoning Example]
答题要求：(Answer requirements: )
1. 逐步分析並選出正確答案(Analyze step by step and select the correct answer)
2. 最後明確標示答案選項（A/B/C/D）(Clearly indicate the answer option (A/B/C/D) at the end)
Figure 11: CoT prompt for multi-choice tasks in Traditional Chinese. 0-shot CoT prompting
involves no examples. English sentences in blue are not part of the inference process.
[Translation prompt for converting Cantonese to Mandarin]
请将以下普通话翻译为粤语白话文。直接输出翻译过的句子，不需要解释或其他注释。
(Please translate the following Mandarin into Cantonese colloquial language. Output the translated sentences directly, without
explanations or additional notes.)
[Translation prompt for converting Mandarin to Cantonese]
请你将以下嘅粤语翻成普通话。直接输出译咗嘅句子，唔使解释或者其他批注。
(Please translate the following Cantonese into Mandarin colloquial language. Output the translated sentences directly, without
explanations or additional notes.)
Figure 12: Prompt for translation tasks. English sentences in blue are not part of the inference
process.
J.2
Translation Prompts
We use the prompt shown in Figure 13 to translate our multi-choice questions into their
Simplified Chinese version.
J.3
Subject Category Prompts
We use the prompt shown in Figure 14 to categorize multi-choice questions.
K
Data Examples in HKMMLU
Figures 16 and Figure 17 showcase data samples from the four main categories: STEM,
Social Sciences, Humanities, and Other. Additionally, Figures 18 and 19 showcase examples
from four Hong Kong-specific topics: physical geography, celebrities, history, and law.
Furthermore, Figure 20 provides detailed samples of translation tasks. In CoT prompting,
we illustrate complete zero-shot and one-shot CoT examples in Figures 21 and Figure 22.
L
Compute and Resources Used for Evaluation
For models with API access, including GPT-4o, Claude 3.7 Sonnet, and DeepSeek-V3, we
perform inference on CPUs, completing 0-shot tasks within one day. For other models, we
utilize a cluster with 8 NVIDIA H800-80GB GPUs and vLLM for acceleration, finishing
0-shot experiments within one day.
24

--- Page 25 ---

Preprint. Under review.
任务：将提供的繁体中文内容翻译为标准简体中文。
(Task: Translate the provided traditional Chinese attributes into standard simplified Chinese.)
翻译指南：(Translation Guide: )
1.
保持原文格式：保留原始文本中的标点符号、数字和英文字符不变。
(1. Maintain original formatting: Keep punctuation marks, numbers, and English characters unchanged in the original text.)
2. 标准化汉语表达：将非标准汉语表达转换为简体中文规范。例如，“何者錯誤？”应翻译为“哪一项是错误的？”，
而不是直译为“何者错误”。同样地，“甚麼”应翻译成“什么”而非“甚么”。
(2. Standardized Chinese expressions: Convert non-standard Chinese expressions into simplified Chinese specifications. For 
example, "Which is wrong?" should be translated as "Which is wrong?" instead of literal translation as "Which is wrong. Similarly, 
'what' should be translated as' what 'rather than' what '.)
3. 专有名词处理：专有名词（如人名、地名等）应按照其最常用的简体中文写法进行翻译或保持不变。
(3. Proper noun handling: Proper nouns (such as personal names, place names, etc.) should be translated or kept unchanged 
according to their most commonly used simplified Chinese writing style.)
4. 结构完整性：请确保题目及其选项的结构完整无误，包括但不限于题目的逻辑连贯性和选项的一一对应关系。
(4. Structural integrity: Please ensure that the structure of the question and its options is complete and error free, including but not 
limited to the logical coherence of the question and the one-to-one correspondence between the options.)
5. 排版格式维护：维持原文字体样式、段落布局等视觉格式不变，以保证信息传递的准确性。
(5. Layout format maintenance: Maintain the original text font style, paragraph layout, and other visual formats unchanged to 
ensure the accuracy of information transmission.)
注意：请特别关注术语的专业性和准确性，避免因直译导致的意义偏差。
(Attention: Please pay special attention to the professionalism and accuracy of terminology to avoid any semantic deviation caused 
by literal translation.)
Figure 13: Prompt of translation from Traditional Chinese to Simplified Chinese. English
sentences in blue are not part of the inference process.
M
Fair and Ethical Labor
We hired 24 test-takers with a post-secondary degree or higher to participate in the assess-
ment. To recognize their contributions, we established a fair compensation system, offering
an estimated average hourly wage of USD 11.58.
25

--- Page 26 ---

Preprint. Under review.
你是一位專精於香港研究的資深專家。請基於以下給定的問答內容，將問題歸類至最適合的類別：(You are a 
senior expert specializing in Hong Kong studies. Please classify the questions based on the following provided Q&A 
content into the most suitable categories)
主要類別：(Main Categories: )
{subject_list_with_descriptions}
判斷規則：(Judgment Rules: )
- 優先選擇最具体且最相關的類別 (Prioritize the most specific and relevant category.)
- 如內容涉及多個類別，選擇主要論述的核心類別 (If the content involves multiple categories, choose the primary 
core category being discussed.)
- 若題目不屬於上述任何類別，請返回"其他常識” (If the question does not belong to any of the above categories, 
please return 'Other General Knowledge’.)
##香港歷史和香港社會區分要點 (Key Distinctions between Hong Kong History and Hong Kong Society)
###關注點: (Focus Areas: )
1. 香港歷史：關注過去的事件和發展，強調歷史背景和影響。
(1. Hong Kong History: Focuses on past events and developments, emphasizing historical context and impact.)
2. 香港社會：關注當下的生活狀況和社會結構，強調民生和社會問題。
(2. Hong Kong Society: Focuses on current living conditions and social structure, emphasizing livelihood and social 
issues.)
###內容類型：(Content Types: )
1. 香港歷史：涉及的內容多與過去的事件、人物和發展相關，通常是对歷史的回顧和分析。
(1. Hong Kong History: Involves content related to past events, figures, and developments, typically reflecting on and 
analyzing history.)
2. 香港社會：涉及的內容多與當前的社會現象、民生問題和人際關係相關，通常是对現實的觀察和討論。
(2. Hong Kong Society: Involves content related to current social phenomena, livelihood issues, and interpersonal 
relationships, typically observing and discussing reality.)
###例子：(Examples: )
1. 香港歷史：討論香港的回歸歷史、重要的歷史人物、歷史事件的影響等。
(1. Hong Kong History: Discusses the history of Hong Kong's return, important historical figures, and the impact of 
historical events.)
2. 香港社會：討論當前的住房危機、教育改革、社會運動的現狀等。
(2. Hong Kong Society: Discusses the current housing crisis, education reform, and the state of social movements.)
輸出要求：(Output Requirements)
- 僅輸出最終類別名稱 (Only output the final category name)
- 無需解釋理由(No need to explain the reason)
- 確保類別名稱與上述分類完全一致(Ensure that the category name is completely consistent with the above 
classification)
示例：(Example: )
輸入：(Input: )
問題：香港邊境禁區羅湖位於哪裡？(Question: Where is the Luohu border restricted area in Hong Kong located?)
答案：香港新界，靠近深圳邊界。(Answer: New Territories, Hong Kong, near the Shenzhen border.)
輸出：(Output: )
香港地理 (Hong Kong Geography)
Figure 14: Prompt for categorizing questions into different subjects. English sentences in
blue are not part of the inference process.
26

--- Page 27 ---

Preprint. Under review.
任務：將香港知識相關的問答轉換為標準單選題
(Convert the Hong Kong knowledge-related Q&A into standard multiple-choice questions)
1. 基本要求(Basic Requirements)
- 使用簡體中文(Use Simplified Chinese)
- 保持問題的核心含義不變(Maintain the core meaning of the question)
- 確保所有內容與香港知識相關(Ensure that all content is related to Hong Kong knowledge)
2. 問題改寫(Question Rewriting)
- 將開放式問題改寫為封閉式選擇題(Rewrite open-ended questions as closed multiple-choice questions)
- 問題表述要清晰、準確、無歧義(The question statement should be clear, accurate, and unambiguous)
- 避免使用“以下哪個說法是正確的”等模糊表述(Avoid ambiguous expressions such as “Which of the following 
statements is correct”)
3. 選項設計(Option Design)
- 必須4個選項(Must have 4 options)
- 正確選項：直接基於原答案設計，保持答案核心信息(Correct option: Design directly based on the original 
answer, maintaining the core information of the answer)
- 干擾項要求(Requirements for distractors)
  * 與題目主題高度相關(Highly relevant to the topic of the question)
  * 表述方式與正確選項一致 (Consistent with the correct option in terms of expression）
  * 具有合理的迷惑性(Reasonably distracting)
  * 避免明顯錯誤或無關選項(Avoid obviously incorrect or irrelevant options)
  * 選項間不能有邏輯矛盾(There should be no logical contradictions between options)
- 禁止使用“以上都對”/“以上都錯”等選項(Do not use options such as “All of the above”/“None of the above”)
- 選項長度應相近(The length of the options should be similar)
4. 答案驗證(Answer Verification)
- 確保有且僅有一個正確選項(Ensure that there is only one correct option)
- 正確選項必須能從原始答案中得到明確支持(The correct option must be clearly supported by the original answer)
- 如原始答案不足以確定正確選項，返回“原始問答對未提供充分信息” (If the original answer is not sufficient 
to determine the correct option, return “The original Q&A pair does not provide sufficient information”)
輸出格式(Output Format)：
question: [改寫後的單選題問題] ([The rewritten multiple-choice question])  
choice A: [選項A內容] ([Content of option A])  
choice B: [選項B內容] ([Content of option B])  
choice C: [選項C內容] ([Content of option C])  
choice D: [選項D內容] ([Content of option D])  
answer: [正確答案字母(A/B/C/D)] ([The correct answer letter  (A/B/C/D)])
或 (Or)  
原始問答對未提供充分信息 (The original Q&A pair does not provide sufficient information)
Figure 15: System prompt for processing question-answering pairs into multi-choice ques-
tions. English sentences in blue are not part of the inference process.
問題：下列哪些有關乙醇的陳述正確？
(Question: Which of the following statements about ethanol is true?)
(1) 它是易燃的。(It is flammable)
(2) 它是可溶於水的。(It is water-soluble)
(3) 它比水更具揮發性。(It is more volatile than water)
A. 只有(1) 和(2) (Only (1) and (2))
B. 只有(1) 和(3) (Only (1) and (3))
C. 只有(2) 和(3) (Only (2) and (3))
D. (1) , (2) 和(3) ((1), (2) and (3))
答案：D (Answer: D)
問題：下列哪項有關會計比率的陳述是正確的？ 
(Question: Which of the following statements about accounting ratios is 
true?)
(1) 它們是用來評估企業的財務業績。(They are used to evaluate the 
financial performance of a business)
(2) 「銷貨」是計算所有盈利能力比率的分母。("Sales" is the 
denominator for calculating all profitability ratios)
(3) 一家企業的酸性測驗比率較其流動比率為高。(An enterprise's acid 
test ratio is higher than its current ratio)
A. 只有 (1) (Only (1))
B. 只有 (1) 及 (2) (Only (1) and (2))
C. 只有(1) 及(3) (Only (1) and (3))
D. 只有(2) 及 (3) (Only (2) and (3))
答案：A (Answer: A)
Figure 16: Examples of “HKDSE Chemistry” in STEM and “HKDSE Business, Accounting,
and Financial Studies” in Social Science. The blue text represents the English translation of
the corresponding Chinese.
27

--- Page 28 ---

Preprint. Under review.
問題：1894年，孫中山在__________創立興中會，提出「驅除
__________，恢復中華，創立合眾政府」的主張，是晚清首個革命團
體。
(Question: In 1894, Sun Yat-sen founded the Xingzhong Association at 
__________, proposing the idea of "driving out __________, restoring 
China and establishing a United government", which was the first 
revolutionary organization in the late Qing Dynasty)
A. 美國，韃虜 (United States, Tartar)
B. 英國，韃虜 (England, Tartar)
C. 日本，滿清 (Japan, Manchu Dynasty)
D. 檀香山，韃虜 (Honolulu, Tartar)
答案：D (Answer: D)
問題：粵語中的“賣口乖”是什麼意思？
(Question: What is the meaning of "sell your mouth" in Cantonese?)
A. 用真誠的讚美來鼓勵他人 (Encourage others with sincere 
compliments)
B. 講好聽的話取悅人，未必真心，可能有其他目的 (Speak nice words 
to please people, may not be sincere, may have other purposes)
C. 通過批評他人來促使他們改進 (Motivate others to improve by 
criticizing them)
D. 用沉默來表達不滿和抗議 (Use silence to express dissatisfaction and 
protest)
答案：B (Answer: B)
Figure 17: Examples of “Chinese History” in Humanities and “Cultural Common Sense” in
Other. The blue text represents the English translation of the corresponding Chinese.
問題：香港的四方山地理位置位於哪個區域？
(Question: Where is the Sifang Mountains in Hong Kong located?)
A. 位於荃灣區和大埔區 (Located in Tsuen Wan District and Tai Po 
District)
B. 位於沙田區和元朗區 (Located in Sha Tin and Yuen Long Districts)
C. 位於觀塘區和西貢區 (Located in Kwun Tong and Sai Kung Districts)
D. 位於北區和屯門區 (Located in North District and Tuen Mun District)
答案：A (Answer: A)
問題：麥子樂在以下哪部電視劇中擔任過主要角色？
(In which of the following TV series has Maizile played a major role?)
A. 《雷霆掃毒》 (Thunder Against Drugs)
B. 《法證先鋒》 (Forensic Pioneer)
C. 《使徒行者》 (Apostolic Walker)
D. 《溏心風暴》 (A Soft Boiled Storm)
答案：A (Answer: A)
Figure 18: Examples of “Hong Kong Physical Geography” and “Hong Kong Celebrity” in
Hong Kong Specific Data. The blue text represents the English translation of the correspond-
ing Chinese.
問題：1901年，中華電力有限公司在香港註冊成立，並在兩年後啟用
其首座發電廠。該發電廠的位置在哪？
(CLP Power Company Limited was incorporated in Hong Kong in 1901 
and opened its first power plant two years later. Where is the power plant 
located?)
A. 旺角亞皆老街 (Argyle Street, Mong Kok)
B. 灣仔星街 (Star Street, Wan Chai)
C. 北角電氣道 (Electric Road, North Point)
D. 紅磡漆咸道 (Chatham Road, Hung Hom)
答案：D (Answer: D)
問題：根據《基本法》，在以下哪種情況下，立法會主席可宣告立法
會議員喪失其職員資格？
(According to the Basic Law, under which of the following circumstances 
can the President declare a Member of the Legislative Council to be 
disqualified as an officer?)
A. 該議員因嚴重疾病而無力履行職務 (The Member is unable to perform 
his duties due to serious illness)
B. 該議員喪失香港特別行政區永久性居民身份 (The Member loses the 
status of permanent resident of the Hong Kong Special Administrative 
Region)
C. 該議員接受委任成為副局長 (The Member accepted the appointment 
as Deputy Secretary)
D. 以上皆是 (All of the above)
答案：D (Answer: D)
Figure 19: Examples of “Hong Kong History” and “Hong Kong Law” in Hong Kong Specific
Data. The blue text represents the English translation of the corresponding Chinese.
28

--- Page 29 ---

Preprint. Under review.
Mandarin To Cantonese
请将以下普通话翻译为粤语白话文。直接输出翻译过的句子，不需要解释或其他注释。
(Please translate the following Mandarin into Cantonese. Output the translated sentence directly, without explanation or other comments.)
問題：我們能有幾回機會像這樣一起旅行，所以我們一定要好好珍惜。
(How many times can we travel together like this, so we must cherish it.)
答案：我哋有幾何機會好似噉一齊旅行，所以我哋一定要好好珍惜。
(How many times can we travel together like this, so we must cherish it.)
Cantonese To Mandarin
请你将以下嘅粤语翻成普通话。直接输出译咗嘅句子，唔使解释或者其他批注。
(Please translate the following Cantonese into Mandarin. Output the translated sentence directly, without explanations or other comments.)
問題：我哋嘅談判已經去到咗死衚衕，雙方都唔能夠妥協。
(Our negotiations have reached a dead end, with neither side able to compromise.)
答案：我们的谈判已经走到了死胡同，双方都无法妥协。
(Our negotiations have reached a dead end, with neither side able to compromise.)
Figure 20: Examples of translation tasks. The blue text represents the English translation of
the corresponding Chinese.
作爲一個精通香港繁體字和香港中學文憑數學考試的專家，請完成以下繁體中文單選題。答题要求：1. 逐步分析並選出正
確答案。2. 最後明確標示答案選項（A/B/C/D）。
As an expert in Hong Kong traditional characters and Hong Kong Diploma of Secondary Education Mathematics examination, 
please complete the following Traditional Chinese multiple choice. Requirements: 1. Analyze step by step and choose the correct 
answer. 2. The answer options are clearly marked at the end (A/B/C/D)
問題：小麗執行一項7小時的打字工作。她在首3小時及最後4小時的平均打字速率分別為每分鐘63字及每分鐘56字。求她
在該7小時的平均打字速率。
Question: Xiao Li performs a seven-hour typing task. Her average typing rate in the first three hours and last four hours was 63 
words per minute and 56 words per minute respectively. Ask for her average typing rate over the 7 hours.
A. 每分鐘17字 
 
B. 每分鐘35字 
 
C. 每分鐘59字 
 
D. 每分鐘60字 
A. 17 words per minute 
B. 35 words per minute 
C. 59 words per minute 
D. 60 words per minute
答案：C 
Answer: C
思考過程：
要計算小麗在7小時的平均打字速率，我們需要先計算她總共打了多少字，然後再除以總時間。
1.
計算首3小時的打字量：速率= 每分鐘63字，時間= 3小時= 180分鐘，打字量= 63字/分鐘× 180分鐘= 11340字。
2.
計算最後4小時的打字量：速率= 每分鐘56字，時間= 4小時= 240分鐘，打字量= 56字/分鐘× 240分鐘= 13440字。
3.
計算總打字量：總打字量= 11340字+ 13440字= 24780字。
4.
計算總時間：總時間= 7小時= 420分鐘。
5.
計算平均速率：平均速率= 總打字量/ 總時間= 24780字/ 420分鐘= 59字/分鐘。
因此，小麗在該7小時的平均打字速率為每分鐘59字。答案選項：(C) 每分鐘59字
Thinking process:
To calculate Xiao Li's average typing rate over seven hours, we need to calculate how many words she typed in total, and then 
divide by the total time.
1. Calculate typing for the first 3 hours: Rate = 63 words per minute, time = 3 hours = 180 minutes, typing = 63 words per minute x 
180 minutes = 11,340 words.
2. Calculate typing for the last 4 hours: Rate = 56 words per minute, time = 4 hours = 240 minutes, typing = 56 words per minute x 
240 minutes = 13,440 words.
3. Calculate total typing: Total typing = 11340 words + 13440 words = 24780 words.
4. Calculate total time: Total time = 7 hours = 420 minutes.
5. Calculate average rate: Average rate = Total typing/total time = 24780 words / 420 minutes = 59 words/minute.
As a result, Xiao Li's average typing rate during the seven hours was 59 words per minute. Answer options: (C) 59 words per minute
Figure 21: Example of Answering with CoT prompting. The blue text represents the English
translation of the corresponding Chinese.
29

--- Page 30 ---

Preprint. Under review.
示例 (Example)
问题：《英皇制誥》作爲香港殖民地時期的憲制性文件，主要規定了什麼內容？
(Question: As a constitutional document of Hong Kong during the colonial period, what are the main contents stipulated in the Patent?)
A. 香港行政、立法和司法機關的組成、權力以及確立三權分立政體
(A. The composition and powers of the executive, legislative and judicial branches of Hong Kong and the establishment of a separation of powers)
B. 香港與英國本土之間的貿易關係和經濟往來規則
(B. Rules of trade relations and economic exchanges between Hong Kong and the mainland United Kingdom)
C. 香港居民的基本權利和義務以及公民身份認定標準
(C. Basic rights and duties of Hong Kong residents and criteria for determining citizenship)
D. 香港與周邊地區的邊界劃分和領土爭端解決機制
(D. Boundary demarcation and territorial dispute settlement mechanism between Hong Kong and its surrounding areas)
推理：
「英皇制誥」作爲香港殖民地時期的重要憲制性文件，主要涉及的是香港政府機構的組織架構和權力劃分，這正好與選項A描述的內容相符。
下面是選擇A答案的推理步驟和邏輯依據：
1.
憲制性文件的特點：憲制性文件通常用以規定一個政治實體的基本政治制度和政府組織安排。香港殖民地時期的「英皇制誥」主要是
確立殖民政府的運作框架，而不是涉及貿易、居民權利或邊界問題。
2.
考察各選項：選項A提到「行政、立法和司法機關的組成、權力以及確立三權分立政體」，這正是憲制性文件常見的內容，尤其對於
確保政府各部門間權力互相制衡起到關鍵作用。選項B涉及貿易和經濟往來，這屬於經濟政策範疇，不屬於憲制文件的核心範圍。選
項C所說的基礎權利和公民身份標準一般是在憲法或權利法案中規定，而「英皇制誥」主要關注政府機構的設置問題。選項D則牽涉到
領土和邊界問題，這也不是「英皇制誥」的主要內容。
3.
歷史背景：在香港的殖民統治下，「英皇制誥」作為一項重要文件，其主要任務是規範殖民政府的行政運作和制度安排，確保政府在
行政、立法和司法三個部門間保持一定的平衡和獨立性，這與選項A所描述的內容完全吻合。
綜上所述，從憲制文件的目的、文件所涉及的內容以及其他選項的範疇來看，正確答案是選項A。
(Reasoning:
As an important constitutional document in the colonial period of Hong Kong, the "Patent" mainly deals with the organizational structure and division 
of powers of the Hong Kong government, which is exactly in line with the content described in option A. The following are the reasoning steps and 
logical grounds for choosing answer A:
Characteristics of constitutional documents: Constitutional documents are usually used to define the basic political system and governmental 
organization of a political entity. During the colonial period, the "patent" in Hong Kong was mainly about establishing the framework for the operation 
of the colonial government, rather than dealing with trade, residents' rights or boundary issues.
Examine the options: Option A refers to "the composition and powers of the executive, legislative, and judicial branches, and the establishment of a 
separation of powers," which are common elements of constitutional documents and are especially critical to ensuring checks and balances between the 
various branches of government. Option B relates to trade and economic engagement, which is within the scope of economic policy and not within the 
core scope of the constitutional document. The basic rights and citizenship criteria mentioned in option C are generally set out in the Constitution or 
bill of Rights, while the "patent" focuses on the establishment of government institutions. Option D involves territorial and border issues, which are not 
the main content of the Patent.
Historical background: Under the colonial rule of Hong Kong, as an important document, the main task of the "Patent" was to regulate the 
administrative operation and institutional arrangements of the colonial government, and to ensure that the government maintained A certain balance 
and independence among the three branches of the executive, legislative and judicial branches, which was fully consistent with the content described in 
option A.
In view of the purpose of the constitutional document, the content of the document and the range of other options, the correct answer is option A.)
答案：A (Answer: A)
作爲一個精通香港繁體字和香港政府機構與政治制度的專家，請參考上面的思考案例，完成以下繁體中文單選題。答题要求：1. 逐步分析
並選出正確答案。2. 最後明確標示答案選項（A/B/C/D）。
(As an expert in Hong Kong traditional characters and the government institutions and political system of Hong Kong, please refer to the above 
thought cases to complete the following traditional Chinese multiple choice. 1. Analyze and choose the correct answer step by step. 2. Finally, clearly 
indicate the answer options (A/B/C/D).)
問題：香港特別行政區政府的哪個決策局負責財經和政府庫務事務？
(Question: Which bureau of the Hong Kong Special Administrative Region Government is responsible for financial and Treasury affairs?)
A. 創新及科技局(A. Innovation and Technology Bureau)
B. 財經事務及庫務局(B. Financial Services and the Treasury Bureau)
C. 環境保護局(C. Environmental Protection Agency)
D. 教育局(D. Education Bureau)
答案：B (Answer: B)
思考过程：
要解答這個問題，我們需要逐步分析每個選項，並確定哪個決策局負責財經和政府庫務事務。
1. 選項A：創新及科技局 - 創新及科技局主要負責推動香港的創新和科技發展，包括資訊科技、創新產業等。這個局與財經和庫務事務無直
接關聯。
2. 選項B：財經事務及庫務局 - 財經事務及庫務局（簡稱財庫局）是香港特別行政區政府的一個決策局，專門負責財經政策、政府庫務、稅
收、金融市場監管等事務。這與問題中提到的「財經和政府庫務事務」完全吻合。
3. 選項C：環境保護局 - 環境保護局主要負責環境保護政策、污染控制、可持續發展等事務。這與財經和庫務事務無關。
4. 選項D：教育局 - 教育局負責教育政策、學校管理、師資培訓等事務。這與財經和庫務事務無直接關聯。
結論：從上述分析可以看出，財經事務及庫務局是唯一一個負責財經和政府庫務事務的決策局。因此，正確答案是選項B。答案：B。
(Thinking process:
To answer this question, we need to analyse each option step by step and determine which bureau is responsible for financial and Treasury matters.
1. Option A: Innovation and Technology Bureau - The Innovation and Technology Bureau is mainly responsible for promoting innovation and 
technology development in Hong Kong, including information technology, innovation industries, etc. The Bureau is not directly related to financial 
and Treasury matters.
2. Option B: Financial Services and the Treasury Bureau - The Financial Services and the Treasury Bureau is a policy bureau of the Government of the 
Hong Kong Special Administrative Region, responsible for financial policy, government Treasury, taxation and financial market regulation. This is 
perfectly consistent with the "financial and government Treasury affairs" mentioned in the question.
3. Option C: Environmental Protection Agency - The Environmental Protection Agency is responsible for environmental protection policies, pollution 
control, and sustainable development. This has nothing to do with financial and Treasury matters.
4. Option D: Education Bureau - The Education Bureau is responsible for education policy, school management, teacher training, etc. This is not 
directly related to financial and Treasury matters.
Conclusion: As can be seen from the above analysis, the Financial Services and the Treasury Bureau is the only policy bureau responsible for financial 
and government Treasury matters. So the correct answer is choice B. Answer: B.)
Figure 22: Example of a one-shot CoT prompt. The blue text represents the English transla-
tion of the corresponding Chinese.
30

```
