---
title: "HalluDial - PDF Extract"
source_pdf: "2024-Luo-HalluDial.pdf"
pages: 27
extracted_at: "2026-01-24T17:05:39.052413"
---

# PDF Extract: HalluDial

**Source PDF:** 2024-Luo-HalluDial.pdf
**Total Pages:** 27

---

## Content

```
--- Page 1 ---

HalluDial: A Large-Scale Benchmark for Automatic
Dialogue-Level Hallucination Evaluation
Wen Luo1,2∗
Tianshu Shen3
Wei Li2
Guangyue Peng2
Richeng Xuan1
Houfeng Wang2†
Xi Yang1†
1Beijing Academy of Artificial Intelligence
2National Key Laboratory for Multimedia Information Processing, Peking University
3Wangxuan Institute of Computer Technology, Peking University
Abstract
Large Language Models (LLMs) have significantly advanced the field of Natural
Language Processing (NLP), achieving remarkable performance across diverse
tasks and enabling widespread real-world applications. However, LLMs are prone
to hallucination, generating content that either conflicts with established knowl-
edge or is unfaithful to the original sources. Existing hallucination benchmarks
primarily focus on sentence- or passage-level hallucination detection, neglect-
ing dialogue-level evaluation, hallucination localization, and rationale provision.
They also predominantly target factuality hallucinations while underestimating
faithfulness hallucinations, often relying on labor-intensive or non-specialized
evaluators. To address these limitations, we propose HalluDial, the first comprehen-
sive large-scale benchmark for automatic dialogue-level hallucination evaluation.
HalluDial encompasses both spontaneous and induced hallucination scenarios,
covering factuality and faithfulness hallucinations. The benchmark includes 4,094
dialogues with a total of 146,856 samples. Leveraging HalluDial, we conduct a
comprehensive meta-evaluation of LLMs’ hallucination evaluation capabilities in
information-seeking dialogues and introduce a specialized judge language model,
HalluJudge. The high data quality of HalluDial enables HalluJudge to achieve
superior or competitive performance in hallucination evaluation, facilitating the
automatic assessment of dialogue-level hallucinations in LLMs and providing
valuable insights into this phenomenon. The dataset and the code are available at
https://github.com/FlagOpen/HalluDial.
1
Introduction
Large Language Models (LLMs) have made considerable advancements in the field of Natural
Language Processing (NLP). Their rapid evolution and widespread adoption have resulted in remark-
able performance across diverse tasks (Bubeck et al., 2023; Zhao et al., 2023a), encompassing text
generation, reading comprehension, and machine translation. This significant progress has facilitated
their deployment in various real-world applications, serving millions of users globally.
Despite the outstanding capabilities exhibited by LLMs, they still suffer from the risk of hallucination.
In the field of LLMs, hallucination refers to the phenomenon where the model generates content that
either conflicts with established knowledge or is unfaithful to the original sources (Zhang et al., 2023;
Huang et al., 2023a; Li et al., 2024a). This issue can result in producing inaccurate or misleading
information, posing substantial challenges for the real-world deployments and applications of LLMs.
*Work done during an internship at Beijing Academy of Artificial Intelligence.
†Corresponding authors: wanghf@pku.edu.cn, yangxi@baai.ac.cn
Preprint. Under review.
arXiv:2406.07070v1  [cs.CL]  11 Jun 2024

--- Page 2 ---

Figure 1: Samples from the HalluDial dataset, including knowledge, dialogue context, and hallu-
cination evaluation results of the current response. Each evaluation result comprises hallucination
detection, localization, and the corresponding rationale.
Hence, the evaluation of hallucinations in LLMs has recently emerged as a critical task, leading to
the proposal of numerous hallucination evaluation benchmarks (Manakul et al., 2023; Chen et al.,
2023; Zheng et al., 2023; Cheng et al., 2023a; Li et al., 2023a; Liang et al., 2023; Yang et al., 2023;
Feng et al., 2023; Min et al., 2023).
Nevertheless, several limitations persist in these benchmarks: (1) Absence of Dialogue-Level Hal-
lucination Evaluation: Existing hallucination benchmarks primarily concentrate on sentence-level
(Manakul et al., 2023; Chen et al., 2023; Zheng et al., 2023; Cheng et al., 2023a; Li et al., 2023a) or
passage-level (Liang et al., 2023; Yang et al., 2023; Feng et al., 2023; Min et al., 2023) hallucinations.
Although HaluEval (Li et al., 2023a) makes an effort to include dialogue-relevant topics, its main
emphasis is still on the sentence and passage levels, and it only assesses hallucination detection
capabilities. Given the widespread deployment of LLMs in dialogue-based applications, the extent
to which LLMs are prone to hallucinations at the dialogue level remains unclear. (2) Neglect of
Hallucination Localization and Rationale: The majority of existing evaluation work (Manakul et al.,
2023; Cheng et al., 2023a; Li et al., 2023a; Yang et al., 2023; Min et al., 2023) is merely centered on
identifying the presence of hallucinations (i.e., hallucination detection), with little attention paid to
the localization of hallucinations and the associated rationales, leading to the lack of interpretability to
a certain extent. (3) Predominant Focus on Factuality Hallucinations (Zhang et al., 2023; Huang et al.,
2023a): The focus of recent hallucination research in LLMs is mainly on factuality hallucinations,
while the importance of faithfulness hallucinations, another crucial type of hallucination, is frequently
underestimated. (4) Reliance on Labor-Intensive Methods or Non-Specialized Evaluators: Current
hallucination evaluations largely depend on crowd-sourced annotations or prompting LLMs that
are not specifically designed for hallucination assessments, which are time-consuming and costly.
Moreover, some research suggests that using API-based LLMs as evaluators can lead to issues such
as inconsistency and irreproducibility (Wang et al., 2023), while open-source LLMs still demonstrate
limited performance as hallucination evaluators (Liang et al., 2023).
To address these limitations, we propose HalluDial, a comprehensive large-scale benchmark for
automatic dialogue-level hallucination evaluation. HalluDial is derived from an information-seeking
dialogue dataset (Dziri et al., 2022) and covers both factuality and faithfulness hallucinations. To
understand the specific conditions under which LLMs naturally produce hallucinated content and sim-
ulate situations where these models intentionally generate hallucinated information, we meticulously
design the spontaneous and induced hallucination scenarios, respectively. In the spontaneous halluci-
nation scenario, we employ a two-step pipeline involving diverse dialogue sampling and automatic
hallucination annotation. For the induced hallucination scenario, task-specific instructions are utilized
to guide GPT-4 to directly generate hallucinated samples along with their explanations for each
hallucination type. Combining these scenarios, HalluDial ultimately provides a large-scale benchmark
2

--- Page 3 ---

comprising 146,856 samples, each containing results for hallucination detection, localization, and
corresponding rationales (Figure 1).
By offering such a large and diverse dataset, HalluDial enables a comprehensive meta-evaluation
of LLMs’ capabilities in hallucination evaluation, including detection, localization, and rationale
provision. Building on HalluDial, we introduce a specialized judge language model, HalluJudge. The
high-quality data in HalluDial enables HalluJudge to achieve superior or competitive performance
in hallucination evaluation, within HalluDial and in other generalization settings. Considering
HalluJudge’s outstanding performance, we subsequently employ it on HalluDial to automatically
assess hallucinations in LLM-generated content during information-seeking dialogues, providing
valuable insights into the nature and prevalence of hallucinations in LLMs.
Overall, the main contributions of this paper can be summarized as follows:
• We propose HalluDial, which, to the best of our knowledge, is the first large-scale dialogue-
level hallucination benchmark.
• We conduct a comprehensive meta-evaluation of LLMs’ capabilities in hallucination evalua-
tions and develop a hallucination judge language model named HalluJudge, which demon-
strates superior or competitive capacity in HalluDial and other generalization settings.
• We utilize HalluDial and HalluJudge to conduct an automatic evaluation of dialogue-level
hallucination present in current LLMs.
2
The HalluDial Benchmark
To comprehensively understand the complexity of hallucination phenomena in LLMs during
information-seeking conversations, we design two distinct scenarios: (1) the spontaneous hallu-
cination scenario and (2) the induced hallucination scenario. The objective of the spontaneous
hallucination scenario is to comprehend the frequency and specific conditions under which LLMs
naturally produce hallucinated content during information-seeking dialogues. On the other hand, the
induced hallucination scenario aims to simulate situations where disinformation, featuring halluci-
nated contents, is intentionally generated by these models. Data are constructed specifically for each
scenario.
2.1
Spontaneous Hallucination Scenario
In the spontaneous hallucination scenario, our data construction pipeline consists of two steps: (1)
diverse dialogue sampling and (2) automatic hallucination annotation.
Diverse Dialogue Sampling
In the diverse dialogue sampling, we begin by selecting a range of
representative LLMs from a broad array of available options*. Given that different models can
generate responses with varying degrees and aspects of hallucination, we carefully choose a suite
of LLMs with varying parameter scales to ensure diversity in the generated responses. This suite
includes Mistral-7B-Instruct-v0.2 (Jiang et al., 2023), vicuna-13B-v1.5 (Zheng et al., 2024), vicuna-
33B-v1.3 (Zheng et al., 2024), Llama-2-70B-chat (Touvron et al., 2023), and GPT-3.5-turbo. Using
the instruction templates presented in Table 11, we then instruct these selected models to engage in a
natural information-seeking dialogue setting. Specifically, these models are tasked with generating a
single response grounded in the provided external knowledge and the established dialogue history
from FaithDial (Dziri et al., 2022). Importantly, they are required to adhere to the length constraint and
avoid introducing additional assumptions or automatically continuing the dialogue beyond the initial
generated response. This setting aims to closely simulate the interactions that these LLMs might
encounter in real-world applications and prepare consistent and coherent responses for annotation in
the next stage.
Automatic Hallucination Annotation
After collecting responses from a wide range of LLMs, the
most direct approach to hallucination detection, localization, and providing explanation typically
involves human annotation. However, this method is frequently costly and time-consuming, thereby
lacking scalability. Given the robust capabilities of GPT-4 in following instructions and its proficiency
*https://chat.lmsys.org
3

--- Page 4 ---

in assessing hallucinations to a certain degree (Liang et al., 2023), we choose GPT-4 to perform
automatic hallucination annotation on the collected natural responses. The key to our annotation
approach lies in crafting effective instructions to guide GPT-4 systematically through the annotation
process. As shown in Table 12, the instruction prompt is carefully designed to encompass the
following three components: (1) task definition, (2) example demonstration, and (3) annotation
instructions. The task definition clearly outlines the input and the objective for GPT-4. To regulate the
output format and enhance the model’s comprehension of the task, we subsequently provide multiple
examples for detailed guidance. To increase the reliability of the annotation results, we include
the non-hallucinatory response for reference. Finally, the annotation instructions provide further
directives on how to navigate the annotation process. Specifically, during the annotation process,
based on the external knowledge, the dialogue history and the non-hallucinatory reference response,
the assistant is required not only to identify any hallucinated information in the generated response,
but also to refine its identification to the specific segment of the response that is inaccurate. Following
this, the assistant should then provide reasonable and coherent justifications for its assessments. This
detailed hallucination localization and rationales can enhance the interpretability of the evaluation
results, contributing to a more profound understanding of hallucinations.
2.2
Induced Hallucination Scenario
The objective of the induced hallucination scenario is to emulate circumstances in which LLMs
intentionally generate hallucinated information. In practical applications, LLMs will encounter a
variety of requests, some of which could be malicious, aiming to deliberately generate hallucinated
information to mislead others. Consequently, assessing how LLMs react when confronted with
maliciously generated hallucinated information becomes crucial for their real-world deployment.
Within the framework of the induced hallucination scenario, for each type of hallucinations (i.e.,
factuality and faithfulness hallucinations), we devise type-specific instructions (Table 13, 14) to
guide GPT-4 to directly produce hallucinated samples, based on the provided knowledge, the pre-
existing dialogue history and the non-hallucinatory reference response. This scenario differs from the
spontaneous hallucination scenario, which follows a sampling-then-annotating pipeline. To ensure
data consistency and quality, in the induced hallucination scenario, GPT-4 is required to generate
hallucinated samples while concurrently providing corresponding hallucination localization and
rationales.
2.3
Implementation Details
The HalluDial dataset is constructed using GPT-4 version gpt-4-1106-preview. To ensure diversity, a
temperature setting of 1.0 is applied during the diverse dialogue sampling and induced hallucination
scenario. In contrast, a temperature of 0.0 is used during automatic hallucination annotation to
minimize randomness and produce more deterministic outputs. Additionally, we set the frequency
penalty to 0.0 and top-p to 1.0. The diverse dialogue sampling is conducted in a zero-shot manner
to simulate the interactions that LLMs might encounter in real-world applications. For automatic
hallucination annotation and the induced hallucination scenario, we provide three in-context examples
to enhance the model’s understanding of the task and ensure high data quality.
2.4
Benchmark Statistics and Usage
As discussed in Section 2.1, we annotate 91,785 natural responses from LLMs in the spontaneous
hallucination scenario using a sampling-then-annotating pipeline. Of these, 21,706 are hallucinatory
samples, and 70,079 are non-hallucinatory samples. In Section 2.2, we generate 18,357 hallucinated
samples for each type of hallucinations. Combined with 18,357 non-hallucinatory samples from
FaithDial (Dziri et al., 2022), the HalluDial dataset ultimately comprises 146,856 data entries. Table
1 provides the statistical details of HalluDial. In Figure 2, we further demonstrate the various topics
covered in HalluDial, ranging from culture, music, and animals to food, games, and more.
Researchers can utilize the HalluDial dataset to investigate hallucinations of LLMs in several ways.
First, by leveraging the hallucination detection labels in HalluDial, researchers can evaluate the
hallucination detection capabilities of LLMs. Second, based on the hallucination localization and
explanations provided in HalluDial, researchers can further assess the models’ abilities to localize
hallucinations and provide justifications. Third, researchers can train their own hallucination evalua-
tors on HalluDial as needed and employ them to automatically assess whether the LLMs’ generated
4

--- Page 5 ---

Figure 2: Topic distributions
in HalluDial dataset. The sam-
ples are categorized into seven
topics, with the red circles
highlighting the top topics.
Table 1: Statistics of HalluDial.
# Dialogues
4,094
# Turns
18,357
# Spontaneous Responses
91,785
# Hallucinatory Responses
21,706
# Induced Responses
55,071
# Factuality Hallucination Responses
18,357
# Faithfulness Hallucination Responses
18,357
# Total Hallucinatory Responses
58,420
# Total Responses
146,856
Avg. Turns per Dialogue
4.48
Avg. Words per Model Utterance
34.45
Avg. Words per Turn
49.74
Avg. Words per Annotations
25.26
contents contain hallucinations. Finally, researchers can analyze which topics or types of content
pose greater challenges for hallucination detection or are more prone to generating hallucinations.
3
Evaluating Hallucination Detection, Localization and Explanation
Capabilities
In this section, we utilize HalluDial to conduct a comprehensive meta-evaluation of LLMs, focusing
on their abilities in hallucination evaluation, including hallucination detection, localization and
providing explanations. Furthermore, to validate the quality of HalluDial, we have developed
a specialized judge language model, HalluJudge, solely based on the training set of HalluDial†.
Thorough experiments showcase HalluJudge’s superior performance and robust generalizability in
handling tasks related to hallucination evaluations, revealing its potential as a competent evaluator for
the hallucinations of other LLMs.
3.1
Hallucination Detection
We conduct hallucination recognition experiments‡ on the HalluDial test set to evaluate the ability
of HalluJudge and other LLMs to detect hallucinations at the dialogue level. For the other LLMs,
the evaluation instructions are detailed in Table 15. The reported metrics include F1 scores for both
hallucinatory and non-hallucinatory cases, overall accuracy (Acc.), average precision (P), average
recall (R), and average F1 score (Macro F1) across both cases. Based on the experimental results
shown in Table 2, we observe the following findings: Firstly, HalluJudge demonstrates superior
performance across all evaluation metrics, surpassing GPT-4 and GPT-4o, which indicates its excellent
hallucination detection capability and the high data quality of HalluDial. Among the competing
models, the GPT-4 family generally performs well, with GPT-4o-2024-05-13 achieving particularly
strong results. Furthermore, the hallucination detection capabilities of open-source LLMs and GPT-
3.5-turbo are generally poor, suggesting that our proposed HalluDial benchmark poses a significant
challenge to these models. Lastly, hallucination detection capabilities improve with increasing model
parameter scale. From the perspective of the Macro F1 score, as the model parameter scale increases,
its hallucination detection capability gradually improves. This indicates a significant impact of model
parameter scale on performance. Possible reasons include that larger models typically possess more
knowledge, stronger representational capabilities, and better adherence to instructions.
3.2
Hallucination Localization and Explanation
In this section, we evaluate LLMs’ capability in hallucination localization and explanation, employing
a random selection of 3200 test instances sourced from the HalluDial test set. For the other LLMs,
the instruction with three in-context examples is present in Table 16. We first utilize established
†The implementation details are in Appendix A.
‡Please refer to Appendix B.1 for full results.
5

--- Page 6 ---

Table 2: Hallucination detection performance of HalluJudge and other LLMs on the HalluDial test
set. Hallu.: Hallucinatory. Non-Hallu: Non-Hallucinatory.
Hallu.
Non-Hallu.
Average
F1 Score
F1 Score
Acc.
P
R
Macro F1
Llama-2-7B-chat
57.07
0.12
39.95
36.90
49.94
28.59
Llama-2-13B-chat
57.41
11.64
42.52
57.52
51.52
34.53
Llama-2-70B-chat
59.37
60.93
60.16
62.09
62.26
60.15
vicuna-7B-v1.5
19.41
76.44
63.54
73.00
54.77
47.92
vicuna-13B-v1.5
31.25
78.30
67.01
79.22
58.96
54.77
vicuna-33B-v1.3
56.26
61.63
59.12
59.86
60.23
58.94
GPT-3.5-turbo
54.32
81.43
73.60
79.29
67.87
67.88
GPT-4-1106-preview
67.75
85.02
79.54
83.75
75.24
76.39
GPT-4-0125-preview
74.15
86.18
81.99
83.43
79.09
80.16
GPT-4o-2024-05-13
72.66
85.01
80.64
81.42
77.92
78.84
HalluJudge
80.07
89.77
86.48
89.89
83.38
84.92
Table 3: The performance of LLMs in hallucination localization and providing rationales. Human
denotes the results of human annotations.
ROUGE_L
BLEU-4
BERTScore
Human
Llama-2-7B-chat
6.42
2.36
35.69
-
Llama-2-13B-chat
11.53
5.55
40.79
-
Llama-2-70B-chat
14.80
8.03
44.66
-
vicuna-7B-v1.5
45.26
13.56
63.60
-
vicuna-13B-v1.5
46.12
16.48
65.00
-
vicuna-33B-v1.3
21.09
13.10
49.80
-
GPT-3.5-turbo
52.58
29.88
69.49
83.41
GPT-4-1106-preview
72.38
39.97
83.09
89.41
GPT-4-0125-preview
73.01
24.36
83.09
-
GPT-4o-2024-05-13
72.00
37.33
82.92
-
HalluJudge
77.38
32.06
86.38
93.65
automatic evaluation metrics, including ROUGE_L, BLEU-4, and BERTScore (Zhang et al., 2019),
to measure the similarity between the generated hallucination localization and explanation by the
models against the reference within the HalluDial dataset. To provide a more holistic assessment
of the models’ performance in hallucination localization and explanation, human annotations are
employed. Specifically, three annotators are required to evaluate the reasonableness and accuracy of
the localization and explanation produced by GPT-3.5-turbo, GPT-4-1106-preview, and HalluJudge.
We use Cohen’s Kappa (κ) to measure the inter-annotator agreement (IAA) and obtain an average
κ = 0.902(0.80 ≤κ ≤1.00), indicating a perfect consistency among annotators. The results
presented in Table 3 show that HalluJudge notably outperforms other models across multiple metrics,
including ROUGE_L, BERTScore, and human evaluations. This suggests not only its effectiveness in
identifying the presence of hallucinations but also its ability to accurately localize them and provide
coherent rationales.
3.3
Generalizability of HalluJudge
To further ensure the high data quality of HalluDial, we incorporate the HaluEval dataset (Li et al.,
2023a) to evaluate the out-of-distribution and cross-domain generalizability of HalluJudge. The
HaluEval dataset is a hallucination detection benchmark that includes three sub-tasks: dialogue,
question answering (QA), and summarization. Each sub-task comprises 10,000 hallucinatory samples
and 10,000 non-hallucinatory samples. To assess the out-of-distribution generalizability of Hallu-
Judge, we utilize the dialogue task from HaluEval. For evaluating cross-domain generalizability,
we employ the QA and summarization tasks. In our experimental setup, we train the model on
the HalluDial training set and test it on the target datasets. The other models used for comparison
6

--- Page 7 ---

Table 4: Out-of-distribution generalizability of HalluJudge on the HaluEval dataset.
Hallu.
Non-Hallu.
Average
F1 Score
F1 Score
Acc.
P
R
Macro F1
Llama-2-7B-chat
66.64
0.02
49.97
32.13
49.97
33.33
Llama-2-13B-chat
69.83
2.12
53.87
72.15
50.49
35.97
Llama-2-70B-chat
68.09
14.02
53.45
71.79
53.45
41.06
vicuna-7B-v1.5
43.58
71.29
61.94
70.74
61.94
57.43
vicuna-13B-v1.5
65.76
76.59
72.19
75.84
72.20
71.18
vicuna-33B-v1.3
69.37
37.42
58.88
66.75
58.88
53.40
GPT-3.5-turbo
78.37
73.80
76.30
77.30
76.30
76.08
HalluJudge
82.23
83.04
82.64
82.72
82.64
82.64
Table 5: Cross-domain generalizability of HalluJudge on the HaluEval dataset. † denotes the results
are from Li et al. (2023a).
QA
Summarization
Acc.
Avg.P
Avg.R
Macro F1
Acc.
Avg.P
Avg.R
Macro F1
Llama-2-7B-chat
49.94
28.56
49.94
33.32
49.46
29.74
49.96
33.10
Llama-2-13B-chat
61.65
73.97
60.78
55.07
54.37
54.58
54.32
53.68
Llama-2-70B-chat
68.48
68.86
68.48
68.33
49.45
42.26
49.45
34.16
vicuna-7B-v1.5
54.73
71.64
54.73
43.73
52.84
53.61
52.84
50.16
vicuna-13B-v1.5
65.34
77.62
65.34
61.01
53.01
72.09
53.01
40.06
vicuna-33B-v1.3
60.39
61.34
60.39
59.54
51.89
52.03
51.88
50.94
GPT-3.5-turbo
74.47
81.54
74.97
72.95
58.53†
-
-
-
HalluJudge
71.34
81.78
71.34
68.78
59.54
76.74
59.54
51.79
possess comparable overall costs. The results presented in Tables 4 demonstrate that HalluJudge
exhibits superior performance in out-of-distribution settings, outperforming GPT-3.5-turbo. While
in cross-domain settings, as shown in Table 5, HalluJudge achieves competitive performances for
the QA task and surpasses GPT-3.5-turbo in summarization in terms of accuracy. These findings
underscore the robust generalizability of HalluJudge and the high quality of the HalluDial dataset.
Furthermore, a comparison of GPT-3.5-turbo’s performance on both HalluDial and the dialogue
subset of HaluEval reveals that HalluDial represents a more challenging benchmark for hallucination
detection in existing LLMs.
4
Evaluating the Hallucinations of LLMs in Information-Seeking Dialogues
As discussed in Section 3, the high data quality of HalluDial enables HalluJudge to effectively detect
and localize hallucinations, while also providing reasonable and coherent rationales. Consequently,
we leverage HalluJudge to automatically evaluate hallucinations in other LLMs during information-
seeking dialogues. Specifically, we utilize the templates outlined in Table 11 to guide LLMs
in generating natural responses based on the given dialogue history and the associated external
knowledge from the HalluDial dataset. Following this, HalluJudge is used to assess whether the
generated responses contain any hallucinations.
4.1
Main Results
Table 6 presents the hallucination rates§ of various LLMs on HalluDial¶. The evaluation encompasses
two scenarios (i.e., Gold and Self), each examined across two dimensions (i.e., turn and dialogue).
The Gold scenario refers to instances where the previous dialogue history is populated with non-
hallucinatory reference responses, while the Self scenario involves dialogue histories filled with
responses generated by the evaluated model itself. The turn dimension represents the hallucination
§The full results are listed in Appendix B.2.
¶The temperature is set to 1.0.
7

--- Page 8 ---

Table 6: Hallucination rates of LLMs.
Gold.
Self.
turn.
dialogue.
turn.
dialogue.
Llama-2-7B-chat
10.87
36.96
10.62
36.68
Llama-2-13B-chat
10.10
35.11
9.09
32.39
Llama-2-70B-chat
9.81
34.35
8.52
31.14
vicuna-7B-v1.5
4.39
17.68
4.31
17.39
vicuna-13B-v1.5
7.01
26.32
6.40
24.81
vicuna-33B-v1.3
6.10
23.97
5.08
20.14
Mistral-7B-Instruct-v0.2
3.14
12.91
2.74
11.51
GPT-3.5-turbo
3.79
13.43
3.17
12.62
GPT-4-1106-preview
5.52
22.72
5.52
22.33
GPT-4-0125-preview
8.85
32.90
6.70
26.01
GPT-4o-2024-05-13
2.77
11.70
2.53
10.75
rate at the turn level, while the dialogue dimension represents the hallucination rate at the dialogue
level (i.e., if any turn within a dialogue contains hallucinations, the entire dialogue is considered
hallucinatory). As shown in Table 6, it is evident that most LLMs maintain relatively low hallucination
rates in the context of information-seeking dialogues. This finding suggests that current LLMs can
generally produce relatively high-quality responses when provided with accurate and appropriate
external knowledge for reference. However, the hallucination rates are not uniformly consistent
between the Self and Gold scenarios. Most models exhibit lower hallucination rates in the Self
scenario compared to the Gold scenario. This implies that in knowledge-grounded settings, using the
model’s own generated responses rather than non-hallucinatory reference responses in the history
may help reduce hallucinations. Conversely, this discrepancy might also be attributable to a loss of
dialogue coherence when the dialogue history is filled with the model’s own generated responses.
4.2
Impact of Temperature on Hallucinations
In this section, we investigate the relationship between sampling temperature and the hallucination
tendency of LLMs. As shown in Figure 3, we initially observe a consistent trend where the hallucina-
tion rate increases with rising temperature, aligning with prior research findings. Specifically, we
note that as temperature increases, both turn-level and dialogue-level hallucination rates demonstrate
a period of relative stability, followed by a sudden and significant rise. Specifically, at lower sampling
temperatures, the hallucination rate remains relatively low and stable. However, as the temperature
continues to climb, there is a marked increase in the hallucination rate. Temperature is a crucial
factor influencing the randomness in the generation process of LLMs. Lower temperatures tend to
produce more stable and consistent results, while higher temperatures can enhance the randomness
and diversity of generated outputs. These observations highlight the dual effects of temperature on
model generation: while a higher temperature can increase the diversity of generated content, it also
raises the incidence of hallucinations. Therefore, in practical applications, it is essential to select
an appropriate temperature value to balance the diversity of generated content and the degree of
hallucinations, particularly in scenarios requiring accurate and factual responses.
5
Related Work
Hallucinations Benchmarks
Hallucination refers to the phenomenon where a model generates
content that either conflicts with established knowledge or is unfaithful to the original sources. To
address this issue, numerous benchmarks have been developed. Some studies assess hallucinations
by integrating external knowledge sources (Guo et al., 2022; Zhong et al., 2020; Min et al., 2023).
Other research employs question-answering mechanisms to test the factual accuracy of model
responses (Zhao et al., 2023b; Chen et al., 2023; Huang et al., 2023b; Zheng et al., 2023; Yin
et al., 2023; Cheng et al., 2023a). TruthfulQA (Lin et al., 2022) is a benchmark designed to assess
imitative falsehoods resulting from misleading pretraining data. HalluQA (Cheng et al., 2023a)
contains 450 adversarial questions to evaluate the hallucinations of Chinese LLMs. For automatic
8

--- Page 9 ---

Figure 3: Impact of temperature on hallucination rate. Left: turn level. Right: dialogue level.
evaluation, SelfCheckGPT (Manakul et al., 2023) leverages the consistency of LLMs’ outputs to
design a sentence-level hallucination assessment metric. Yang et al. (2023) proposes a passage-level
hallucination detection benchmark. HaluEval (Li et al., 2023a) is a hallucination detection benchmark
containing GPT-3.5-turbo-generated and human-annotated hallucinated samples. UHGEval (Liang
et al., 2023) focuses on assessing hallucinations of Chinese LLMs in unconstrained settings. Despite
the progress made by existing research, several limitations remain. Notably, there is a lack of dialogue-
level hallucination evaluation, with current benchmarks focusing mainly on the sentence level (Zhao
et al., 2023b; Chen et al., 2023; Huang et al., 2023b; Zheng et al., 2023; Yin et al., 2023; Cheng et al.,
2023a; Li et al., 2023a) and passage level (Zhong et al., 2020; Min et al., 2023; Manakul et al., 2023;
Liang et al., 2023). Since dialogue is one of the most common applications of LLMs, a comprehensive
evaluation of dialogue-level hallucination remains notably absent. Additionally, existing approaches
often overlook hallucination localization and associated rationales, neglect faithfulness hallucinations,
and rely on labor-intensive methods or non-specialized evaluators. In this study, we aim to address
these limitations and introduce HalluDial, a large-scale benchmark for automatic dialogue-level
hallucination evaluation.
Evaluations with LLMs
As the development of Large Language Models (LLMs) continues to
progress, an increasing volume of research has begun to investigate their potential for substituting
human evaluators (Cheng et al., 2023b; Zheng et al., 2024; Li et al., 2023b; Fu et al., 2023). One
notable framework is GPTScore (Fu et al., 2023), which leverages LLMs to evaluate generated
text. Moreover, Zheng et al. (2024) delves into the application of LLMs as evaluators for other
conversational agents, demonstrating that the assessments made by GPT-4 align with human prefer-
ences approximately 80% of the time. Current efforts in hallucination evaluation often utilize either
open-source LLMs (Manakul et al., 2023; Li et al., 2024b; Yue et al., 2023) or API-based LLMs (Min
et al., 2023; Yang et al., 2023; Li et al., 2023a; Liang et al., 2023). However, it is important to note that
the use of API-based LLMs as evaluators has been associated with issues related to inconsistency and
irreproducibility (Wang et al., 2023). Furthermore, open-source LLMs have yet to yield satisfactory
results when used as hallucination evaluators (Liang et al., 2023). Therefore, building on HalluDial,
we further develop a specialized judge language model for automatic evaluation.
6
Conclusion
In this paper, we introduced HalluDial, the first large-scale benchmark for dialogue-level halluci-
nation evaluation, addressing critical gaps in existing benchmarks. HalluDial encompasses both
spontaneous and induced hallucination scenarios, covering factuality and faithfulness hallucinations.
It provides a comprehensive dataset of 146,856 samples with detailed results for hallucination de-
tection, localization, and rationale provision, which enables a thorough meta-evaluation of LLMs’
capabilities in hallucination evaluation. Furthermore, the high data quality of HalluDial supports the
development of HalluJudge, a specialized hallucination judge language model, and facilitates the
automatic assessment of dialogue-level hallucinations in LLMs. In the future, we are committed to
further enhancing the reliability of automatic hallucination evaluation by developing increasingly
robust and generalized versions of HalluJudge.
9

--- Page 10 ---

References
Sébastien Bubeck, Varun Chandrasekaran, Ronen Eldan, Johannes Gehrke, Eric Horvitz, Ece Kamar,
Peter Lee, Yin Tat Lee, Yuanzhi Li, Scott Lundberg, et al. Sparks of artificial general intelligence:
Early experiments with gpt-4. arXiv preprint arXiv:2303.12712, 2023.
Liang Chen, Yang Deng, Yatao Bian, Zeyu Qin, Bingzhe Wu, Tat-Seng Chua, and Kam-Fai Wong.
Beyond factuality: A comprehensive evaluation of large language models as knowledge generators.
In Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing,
pp. 6325–6341, 2023.
Qinyuan Cheng, Tianxiang Sun, Wenwei Zhang, Siyin Wang, Xiangyang Liu, Mozhi Zhang, Junliang
He, Mianqiu Huang, Zhangyue Yin, Kai Chen, et al. Evaluating hallucinations in chinese large
language models. arXiv preprint arXiv:2310.03368, 2023a.
Qinyuan Cheng, Xiaogui Yang, Tianxiang Sun, Linyang Li, and Xipeng Qiu. Improving con-
trastive learning of sentence embeddings from ai feedback. In Findings of the Association for
Computational Linguistics: ACL 2023, pp. 11122–11138, 2023b.
Nouha Dziri, Ehsan Kamalloo, Sivan Milton, Osmar Zaiane, Mo Yu, Edoardo M Ponti, and Siva
Reddy. Faithdial: A faithful benchmark for information-seeking dialogue. Transactions of the
Association for Computational Linguistics, 10:1473–1490, 2022.
Shangbin Feng, Vidhisha Balachandran, Yuyang Bai, and Yulia Tsvetkov. Factkb: Generalizable
factuality evaluation using language models enhanced with factual knowledge. In Proceedings of
the 2023 Conference on Empirical Methods in Natural Language Processing, pp. 933–952, 2023.
Jinlan Fu, See-Kiong Ng, Zhengbao Jiang, and Pengfei Liu. Gptscore: Evaluate as you desire. arXiv
preprint arXiv:2302.04166, 2023.
Zhijiang Guo, Michael Schlichtkrull, and Andreas Vlachos. A survey on automated fact-checking.
Transactions of the Association for Computational Linguistics, 10:178–206, 2022.
Lei Huang, Weijiang Yu, Weitao Ma, Weihong Zhong, Zhangyin Feng, Haotian Wang, Qianglong
Chen, Weihua Peng, Xiaocheng Feng, Bing Qin, et al. A survey on hallucination in large language
models: Principles, taxonomy, challenges, and open questions. arXiv preprint arXiv:2311.05232,
2023a.
Yuheng Huang, Jiayang Song, Zhijie Wang, Huaming Chen, and Lei Ma. Look before you leap:
An exploratory study of uncertainty measurement for large language models. arXiv preprint
arXiv:2307.10236, 2023b.
Albert Q. Jiang, Alexandre Sablayrolles, Arthur Mensch, Chris Bamford, Devendra Singh Chaplot,
Diego de las Casas, Florian Bressand, Gianna Lengyel, Guillaume Lample, Lucile Saulnier,
Lélio Renard Lavaud, Marie-Anne Lachaux, Pierre Stock, Teven Le Scao, Thibaut Lavril, Thomas
Wang, Timothée Lacroix, and William El Sayed. Mistral 7b, 2023.
Junyi Li, Xiaoxue Cheng, Wayne Xin Zhao, Jian-Yun Nie, and Ji-Rong Wen. Halueval: A large-
scale hallucination evaluation benchmark for large language models. In Proceedings of the 2023
Conference on Empirical Methods in Natural Language Processing, pp. 6449–6464, 2023a.
Junyi Li, Jie Chen, Ruiyang Ren, Xiaoxue Cheng, Wayne Xin Zhao, Jian-Yun Nie, and Ji-Rong Wen.
The dawn after the dark: An empirical study on factuality hallucination in large language models.
arXiv preprint arXiv:2401.03205, 2024a.
Xuechen Li, Tianyi Zhang, Yann Dubois, Rohan Taori, Ishaan Gulrajani, Carlos Guestrin, Percy
Liang, and Tatsunori B Hashimoto. Alpacaeval: An automatic evaluator of instruction-following
models, 2023b.
Yifei Li, Xiang Yue, Zeyi Liao, and Huan Sun. Attributionbench: How hard is automatic attribution
evaluation?, 2024b.
Xun Liang, Shichao Song, Simin Niu, Zhiyu Li, Feiyu Xiong, Bo Tang, Zhaohui Wy, Dawei He,
Peng Cheng, Zhonghao Wang, et al. Uhgeval: Benchmarking the hallucination of chinese large
language models via unconstrained generation. arXiv preprint arXiv:2311.15296, 2023.
10

--- Page 11 ---

Stephanie Lin, Jacob Hilton, and Owain Evans. Truthfulqa: Measuring how models mimic human
falsehoods. In Proceedings of the 60th Annual Meeting of the Association for Computational
Linguistics (Volume 1: Long Papers), pp. 3214–3252, 2022.
Ilya Loshchilov and Frank Hutter. Decoupled weight decay regularization. In International Confer-
ence on Learning Representations, 2018.
Potsawee Manakul, Adian Liusie, and Mark Gales. Selfcheckgpt: Zero-resource black-box hallu-
cination detection for generative large language models. In The 2023 Conference on Empirical
Methods in Natural Language Processing, 2023.
Sewon Min, Kalpesh Krishna, Xinxi Lyu, Mike Lewis, Wen-tau Yih, Pang Koh, Mohit Iyyer, Luke
Zettlemoyer, and Hannaneh Hajishirzi. Factscore: Fine-grained atomic evaluation of factual
precision in long form text generation. In Proceedings of the 2023 Conference on Empirical
Methods in Natural Language Processing, pp. 12076–12100, 2023.
Hugo Touvron, Louis Martin, Kevin Stone, Peter Albert, Amjad Almahairi, Yasmine Babaei, Nikolay
Bashlykov, Soumya Batra, Prajjwal Bhargava, Shruti Bhosale, et al. Llama 2: Open foundation
and fine-tuned chat models. arXiv preprint arXiv:2307.09288, 2023.
Yidong Wang, Zhuohao Yu, Zhengran Zeng, Linyi Yang, Wenjin Yao, Cunxiang Wang, Hao Chen,
Chaoya Jiang, Rui Xie, Jindong Wang, et al. Pandalm: An automatic evaluation benchmark
for llm instruction tuning optimization. In The Twelfth International Conference on Learning
Representations, 2023.
Shiping Yang, Renliang Sun, and Xiaojun Wan. A new benchmark and reverse validation method for
passage-level hallucination detection. In Findings of the Association for Computational Linguistics:
EMNLP 2023, pp. 3898–3908, 2023.
Zhangyue Yin, Qiushi Sun, Qipeng Guo, Jiawen Wu, Xipeng Qiu, and Xuan-Jing Huang. Do large
language models know what they don’t know? In Findings of the Association for Computational
Linguistics: ACL 2023, pp. 8653–8665, 2023.
Xiang Yue, Boshi Wang, Ziru Chen, Kai Zhang, Yu Su, and Huan Sun. Automatic evaluation of
attribution by large language models, 2023.
Tianyi Zhang, Varsha Kishore, Felix Wu, Kilian Q Weinberger, and Yoav Artzi. Bertscore: Evaluating
text generation with bert. In International Conference on Learning Representations, 2019.
Yue Zhang, Yafu Li, Leyang Cui, Deng Cai, Lemao Liu, Tingchen Fu, Xinting Huang, Enbo Zhao,
Yu Zhang, Yulong Chen, et al. Siren’s song in the ai ocean: a survey on hallucination in large
language models. arXiv preprint arXiv:2309.01219, 2023.
Wayne Xin Zhao, Kun Zhou, Junyi Li, Tianyi Tang, Xiaolei Wang, Yupeng Hou, Yingqian Min,
Beichen Zhang, Junjie Zhang, Zican Dong, et al. A survey of large language models. arXiv
preprint arXiv:2303.18223, 2023a.
Yukun Zhao, Lingyong Yan, Weiwei Sun, Guoliang Xing, Chong Meng, Shuaiqiang Wang, Zhicong
Cheng, Zhaochun Ren, and Dawei Yin. Knowing what llms do not know: A simple yet effective
self-detection method. arXiv preprint arXiv:2310.17918, 2023b.
Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan Zhuang, Zhanghao Wu, Yonghao Zhuang,
Zi Lin, Zhuohan Li, Dacheng Li, Eric Xing, et al. Judging llm-as-a-judge with mt-bench and
chatbot arena. Advances in Neural Information Processing Systems, 36, 2024.
Shen Zheng, Jie Huang, and Kevin Chen-Chuan Chang. Why does chatgpt fall short in providing
truthful answers. ArXiv preprint, abs/2304.10513, 2023.
Wanjun Zhong, Jingjing Xu, Duyu Tang, Zenan Xu, Nan Duan, Ming Zhou, Jiahai Wang, and
Jian Yin. Reasoning over semantic-level graph for fact checking. In Proceedings of the 58th
Annual Meeting of the Association for Computational Linguistics. Association for Computational
Linguistics, 2020.
11

--- Page 12 ---

A
Implementation Details of HalluJudge
HalluJudge is built on the Llama-2-7B backbone (Touvron et al., 2023). Training is conducted using 8
NVIDIA A800-SXM4-80GB GPUs, with a batch size of 1 per GPU and a maximum token truncation
length of 1280. The AdamW optimizer (Loshchilov & Hutter, 2018) with a learning rate of 3e-5
and a cosine learning rate scheduler is employed during training. The model is trained with bfloat16
(BF16) computation precision for two epochs, with a warmup ratio of 0.03. HalluDial is randomly
split into training and test sets in a 6:4 ratio, and the average results are reported on the test set after
completing training from three runs with different random seeds.
B
Detailed Evaluation Results
B.1
Detailed Evaluation Results of Hallucination Detection Capabilities
Table 7 presents the detailed results of various LLMs in detecting hallucinations on the HalluDial
test set. The results demonstrate that HalluJudge outperforms all other LLMs across all evaluation
metrics, showcasing its superior hallucination detection capabilities. Figure 4 illustrates some of
the topics in HalluDial where LLMs fail to detect hallucinations. Furthermore, Table 8 provides
a detailed breakdown of the LLMs’ performance in the spontaneous and induced hallucination
scenarios within the HalluDial test set. Interestingly, most LLMs exhibit better performance in
the induced hallucination scenario compared to the spontaneous one. This observation suggests
that the spontaneous hallucination scenario poses a more significant challenge for these models,
potentially due to its diversity and complexity. HalluJudge, in particular, excels in the induced
hallucination scenario, highlighting its strong ability to identify intentionally generated hallucinated
content. However, its performance in the spontaneous scenario, while still competitive, leaves room
for improvement. This discrepancy could be attributed to HalluJudge’s relatively small parameter
scale, indicating the need for further enhancements to tackle the challenges posed by spontaneous
hallucinations more effectively. These findings underscore the complexity of the HalluDial dataset
and the varying degrees of difficulty it presents for current LLMs in detecting hallucinations. The
results also emphasize the importance of developing a more robust and capable judge model that can
handle both spontaneous and induced hallucinations with high accuracy and reliability.
Table 7: Hallucination detection performance on the HalluDial test set.
Hallu.
Non-Hallu.
Average
F1 Score
F1 Score
Acc.
P
R
Macro F1
Llama-2-7B-chat
57.07
0.12
39.95
36.90
49.94
28.59
Llama-2-13B-chat
57.41
11.64
42.52
57.52
51.52
34.53
Llama-2-70B-chat
59.37
60.93
60.16
62.09
62.26
60.15
vicuna-7B-v1.5
19.41
76.44
63.54
73.00
54.77
47.92
vicuna-13B-v1.5
31.25
78.30
67.01
79.22
58.96
54.77
vicuna-33B-v1.3
56.26
61.63
59.12
59.86
60.23
58.94
Baichuan2-7B-Chat
41.49
73.00
63.05
60.79
58.00
57.25
Baichuan2-13B-Chat
62.14
69.59
66.27
66.09
66.74
65.87
internlm2-chat-7B
43.74
79.85
70.33
78.93
63.41
61.80
internlm2-chat-20B
50.34
78.63
70.12
71.96
64.74
64.49
chatglm3-6B
34.31
72.38
61.11
57.97
55.15
53.35
deepseek-llm-7B-chat
57.85
33.93
48.54
58.45
55.17
45.89
deepseek-llm-67B-chat
50.75
81.92
73.55
82.95
66.78
66.33
Qwen1.5-7B-Chat
54.51
76.25
68.79
67.75
65.11
65.38
Qwen1.5-32B-Chat
50.89
81.51
73.14
82.02
66.74
66.20
Qwen1.5-72B-Chat
49.02
81.38
72.73
82.98
66.06
65.20
GPT-3.5-turbo
54.32
81.43
73.60
79.29
67.87
67.88
GPT-4-1106-preview
67.75
85.02
79.54
83.75
75.24
76.39
GPT-4-0125-preview
74.15
86.18
81.99
83.43
79.09
80.16
GPT-4o-2024-05-13
72.66
85.01
80.64
81.42
77.92
78.84
HalluJudge
80.07
89.77
86.48
89.89
83.38
84.92
12

--- Page 13 ---

Table 8: Fine-grained hallucination detection performance in the spontaneous and induced hallucina-
tion scenarios within the HalluDial test set.
Spontaneous Hallucination Scenario
Induced Hallucination Scenario
Acc.
Avg.P
Avg.R
Macro F1
Acc.
Avg.P
Avg.R
Macro F1
Llama-2-7B-chat
23.81
40.27
49.95
19.28
66.84
35.25
49.92
40.08
Llama-2-13B-chat
27.66
49.33
49.74
25.76
67.11
63.18
50.40
41.29
Llama-2-70B-chat
57.95
54.91
56.66
53.11
63.84
55.29
53.62
52.82
vicuna-7B-v1.5
75.97
54.32
50.14
43.94
42.81
61.77
56.03
40.42
vicuna-13B-v1.5
76.17
62.03
50.17
43.72
51.74
67.53
63.10
51.02
vicuna-33B-v1.3
58.24
53.07
52.35
51.34
60.58
51.39
51.06
50.35
GPT-3.5-turbo
77.17
69.21
54.83
53.46
67.63
72.15
73.93
67.49
GPT-4-1106-preview
82.15
79.54
66.46
69.25
75.20
77.87
80.96
74.93
GPT-4-0125-preview
82.39
77.31
69.81
72.18
81.30
80.33
84.12
80.51
GPT-4o-2024-05-13
81.17
74.73
68.76
70.74
79.75
78.40
81.79
78.75
HalluJudge
79.42
80.05
58.26
58.60
98.26
97.56
98.60
98.05
Figure 4: Topic distributions of instances where LLMs fail to detect hallucinations. (a): GPT-4o-
2024-05-13. (b): GPT-4-0125-preview. (c): HalluJudge. (d): GPT-3.5-turbo. (e): Llama-2-70B-chat.
(f): vicuna-33B-v1.3.
B.2
Detailed Evaluation Results of LLM’s Hallucinations
Table 9 presents the full evaluation results of LLM’s hallucinations. Figure 5 illustrates some of the
topics in HalluDial where LLMs are prone to hallucinations.
13

--- Page 14 ---

Table 9: Hallucination rates of LLMs.
Gold.
Self.
turn.
dialogue.
turn.
dialogue.
Llama-2-7B-chat
10.87
36.96
10.62
36.68
Llama-2-13B-chat
10.10
35.11
9.09
32.39
Llama-2-70B-chat
9.81
34.35
8.52
31.14
vicuna-7B-v1.5
4.39
17.68
4.31
17.39
vicuna-13B-v1.5
7.01
26.32
6.40
24.81
vicuna-33B-v1.3
6.10
23.97
5.08
20.14
Baichuan2-7B-Chat
5.31
20.75
5.56
21.80
Baichuan2-13B-Chat
13.20
45.95
12.37
43.87
internlm2-chat-7B
5.82
22.33
5.08
20.11
internlm2-chat-20B
5.41
20.80
4.61
18.59
chatglm3-6B
5.67
21.92
5.56
21.86
deepseek-llm-7B-chat
4.88
19.38
4.54
18.08
deepseek-llm-67B-chat
3.91
15.86
3.30
13.63
Qwen1.5-7B-Chat
13.38
45.67
11.43
40.98
Qwen1.5-32B-Chat
8.87
32.80
8.70
32.38
Qwen1.5-72B-Chat
9.50
34.32
7.67
28.84
Mistral-7B-Instruct-v0.2
3.14
12.91
2.74
11.51
GPT-3.5-turbo
3.79
13.43
3.17
12.62
GPT-4-1106-preview
5.52
22.72
5.52
22.33
GPT-4-0125-preview
8.85
32.90
6.70
26.01
GPT-4o-2024-05-13
2.77
11.70
2.53
10.75
Figure 5: Topic distributions of instances where LLMs are prone to hallucinations. (a): GPT-
4o-2024-05-13. (b): GPT-4-0125-preview. (c): GPT-4-1106-preview. (d): GPT-3.5-turbo. (e):
Llama-2-70B-chat. (f): vicuna-33B-v1.3.
14

--- Page 15 ---

C
Can LLMs Distinguish the Hallucinatory Response in a Comparative
Scenario?
To further investigate the ability of LLMs to identify hallucinations, we test their performance in a
comparative setting within the same conversational context. Specifically, we simultaneously provide
the models with two responses: one containing hallucinations and another without. The data used
in this experiment is derived from the induced hallucination scenario, and the LLMs are guided
to perform the hallucination identification task using the instructions shown in Table 17. Notably,
considering the position bias in LLMs, we alternate the order of the two responses for each model and
perform inference twice to derive the final results. In addition to accuracy, we also report the invalid
rate for cases where the output fails to meet the required criteria. As shown in Table 10, in terms of
average accuracy, the results reveal a polarized trend in the performance of LLMs. Models with larger
parameter scales demonstrate a remarkable ability to accurately identify the hallucinatory response
from the two provided options. Conversely, smaller models exhibit poor performance under this
setting, with most of their results closely approximating random selection. Furthermore, we observe
a severe position bias in most of the open-source LLMs, where they tend to favor either the former or
latter response regardless of its content. For instance, vicuna-7B-v1.5 and Baichuan2-13B-Chat show
a strong preference for the first response, while vicuna-33B-v1.3 and deepseek-llm-7B-chat heavily
favor the second one. This finding suggests that these models may lack a genuine understanding of
hallucinations and instead rely on superficial cues to make their decisions.
Table 10: Results of hallucination detection in the comparative setting. AccuracyF denotes the former
response is hallucinatory, while AccuracyL represents the latter one contains hallucinations.
AccuracyF
AccuracyL
Accuracyaverage
Invalid Rate
vicuna-7B-v1.5
97.63
4.64
51.13
-
vicuna-13B-v1.5
70.12
23.83
46.97
-
vicuna-33B-v1.3
7.58
98.05
53.29
-
Mistral-7B-Instruct-v0.2
65.06
31.68
48.32
28.64
Baichuan2-7B-Chat
49.09
17.76
32.93
20.89
Baichuan2-13B-Chat
99.56
3.12
51.34
-
internlm2-chat-7B
80.70
38.04
59.37
-
internlm2-chat-20B
51.81
82.87
67.34
-
deepseek-llm-7B-chat
0.28
99.83
50.05
-
deepseek-llm-67B-chat
70.27
92.38
81.33
-
Qwen1.5-7B-Chat
74.85
44.91
59.88
-
Qwen1.5-32B-Chat
80.40
52.54
66.47
-
Qwen1.5-72B-Chat
95.35
65.36
80.76
9.86
GPT-3.5-turbo-1106
70.33
73.40
71.87
-
GPT-4-1106-preview
90.56
85.89
88.20
3.26
D
Annotation Details
To evaluate the performance of GPT-3.5-turbo, GPT-4-1106-preview, and HalluJudge, we initially
sample 850 instances where the models’ hallucination detection decisions are hallucinatory. Sub-
sequently, we instruct three annotators to assess the reasonableness and accuracy of the generated
localization and explanation. The annotators consist of two human labelers and GPT-4o-2024-05-13.
The instruction for GPT-4o-2024-05-13 is shown in Table 18. To measure inter-annotator agreement
(IAA), we employ Cohen’s Kappa (κ) and obtain an average κ value of 0.902 (0.80 ≤κ ≤1.00),
indicating perfect consistency among the annotators.
E
More Details on HalluDial
We provide more examples of HalluDial in Figure 6, Figure 7, and Figure 8.
15

--- Page 16 ---

Figure 6: Factuality hallucination examples of HalluDial.
16

--- Page 17 ---

Figure 7: Faithfulness hallucination examples of HalluDial.
Figure 8: Non-hallucinatory examples of HalluDial.
17

--- Page 18 ---

F
Prompt Template
F.1
Instructions in the Spontaneous Scenario
Table 11: Instruction of diverse dialogue sampling.
As an assistant, your task is to engage in a knowledge-grounded conversation. You are required to
compose a SINGLE response in English, not exceeding 80 words, based on the provided knowledge
and consistent with the previous dialogue history. Do NOT add extra preamble or explanations
and refrain from generating follow-up prompts or multiple dialogue turns. Ensure your response is
coherent and do not make claims that cannot be supported by the given knowledge and conversation
context.
###Knowledge###: <Here is the provided external knowledge>
###Dialogue History###: <Here is the dialogue history>
Table 12: Instruction of automatic hallucination annotation.
As an assistant, your task is to serve as a response judge. Provided with the related knowledge, a
dialogue history, a reference response and a generated response, your objective is to determine if
the generated response contains any hallucinated information that (1) directly contradicts the given
knowledge, or (2) cannot be verified from the provided knowledge and dialogue context.
You SHOULD refer to the following examples:
Example 1:
###Knowledge###: Use by a wider audience only came in 1995 when restrictions on the use of the
Internet to carry commercial traffic were lifted.
###Dialogue History###: [Human]: Can you imagine the world without internet access? [Assistant]:
Yeah, but once the access to the internet was a rare thing. do you remember? [Human]: I do. What
else can you tell me ?
###Reference Response###: Well, I know that more people started using it after some restrictions
on internet use were lifted in 1995.
###Generated Response###: Well, I know that the internet was primarily available to the public in
the early 1980s, with no restrictions on commercial traffic from the very beginning.
###Judgement###: Yes. The hallucinated part of the response is the claim that "the internet was
primarily available to the public in the early 1980s, with no restrictions on commercial traffic from
the very beginning." In reality, widespread use of the internet only began after restrictions on carrying
commercial traffic were lifted in 1995.
<More In-Context Examples>
You SHOULD first carefully evaluate each segment of the generated response and determine if the
response contains any hallucinated information. If any such content is found, your next step is to
identify the specific hallucinated segment and explain why it qualifies as such. Your judgement
MUST strictly follow the format demonstrated in the examples above and be well-organized, clear
and concise.
###Knowledge###: <Here is the provided external knowledge>
###Dialogue History###: <Here is the dialogue history>
###Reference Response###: <Here is the reference response>
###Generated Response###: <Here is the generated response>
###Judgement###:
18

--- Page 19 ---

F.2
Instructions in the Induced Scenario
Table 13: Instruction of generating factuality hallucination samples.
As an assistant, your task is to generate a hallucinated response within the context of a conversation
that contradicts the related knowledge. Provided with the related knowledge, a dialogue history, and
a reference response grounded in the knowledge, your objectives are to: (1) Generate a hallucinated
response that contradicts the related knowledge. (2) Identify the specific part of the response that is
hallucinated and explain the reasons.
You SHOULD refer to the following examples:
Example 1:
###Knowledge###: Use by a wider audience only came in 1995 when restrictions on the use of the
Internet to carry commercial traffic were lifted.
###Dialogue History###: [Human]: Can you imagine the world without internet access? [Assistant]:
Yeah, but once the access to the internet was a rare thing. do you remember? [Human]: I do. What
else can you tell me ?
###Reference Response###: Well, I know that more people started using it after some restrictions
on internet use were lifted in 1995.
###Hallucinated Response###: Well, I know that the internet was primarily available to the public
in the early 1980s, with no restrictions on commercial traffic from the very beginning.
###Hallucination Explanation###: The hallucinated part of the response is the claim that "the
internet was primarily available to the public in the early 1980s, with no restrictions on commercial
traffic from the very beginning." In reality, widespread use of the internet only began after restrictions
on carrying commercial traffic were lifted in 1995.
<More In-Context Examples>
The hallucinated response SHOULD appear plausible but be factually incorrect, and SHOULD NOT
exceed the length of the reference response by more than six words. You SHOULD avoid deliberately
emphasizing the authenticity of the generated response and strive to seamlessly align it with the tone
and style of the reference response, maintaining a natural flow in the ongoing conversation.
###Knowledge###: <Here is the provided external knowledge>
###Dialogue History###: <Here is the dialogue history>
###Reference Response###: <Here is the reference response>
19

--- Page 20 ---

Table 14: Instruction of generating faithfulness hallucination samples.
As an assistant, your task is to generate a hallucinated response within the context of a conversation,
which contains some information that cannot be verified from the related knowledge. Provided with
the related knowledge, a dialogue history, and a reference response grounded in the knowledge, your
objectives are to: (1) Generate a hallucinated response containing some information that cannot be
verified from the related knowledge. (2) Identify the specific part of the response that is hallucinated
and explain the reasons.
You SHOULD refer to the following examples:
Example 1:
###Knowledge###: Use by a wider audience only came in 1995 when restrictions on the use of the
Internet to carry commercial traffic were lifted.
###Dialogue History###: [Human]: Can you imagine the world without internet access? [Assistant]:
Yeah, but once the access to the internet was a rare thing. do you remember? [Human]: I do. What
else can you tell me ?
###Reference Response###: Well, I know that more people started using it after some restrictions
on internet use were lifted in 1995.
###Hallucinated Response###: Yes, the internet truly came into its own when in 1995, a break-
through in the optical fiber technology significantly increased its speed and the existing commercial
traffic restrictions were also lifted.
###Hallucination Explanation###: The hallucinated part of the response is the claim that "a break-
through in the optical fiber technology significantly increased its speed." This piece of information is
not verifiable from the given knowledge, which only mentions the lifting of restrictions on carrying
commercial traffic in 1995. There’s no mention of any technological breakthrough in optical fiber
technology that improved internet speed at that time.
<More In-Context Examples>
The hallucinated response SHOULD appear plausible and SHOULD NOT exceed the length of
the reference response by more than six words. You SHOULD avoid deliberately emphasizing the
authenticity of the generated response and strive to seamlessly align it with the tone and style of the
reference response, maintaining a natural flow in the ongoing conversation.
###Knowledge###: <Here is the provided external knowledge>
###Dialogue History###: <Here is the dialogue history>
###Reference Response###: <Here is the reference response>
20

--- Page 21 ---

F.3
Instructions Used during Evaluations
Table 15: Instruction of hallucination detection.
As an assistant, your task is to serve as a response judge. Provided with the related knowledge, a
dialogue history and a generated response, your objective is to determine if the generated response
contains any hallucinated information that (1) directly contradicts the given knowledge, or (2) cannot
be verified from the provided knowledge and dialogue context.
You SHOULD carefully evaluate each segment of the generated response and determine if the
response contains any hallucinated information. If such content is detected, your output should be
"Yes"; otherwise, it should be "No".
###Knowledge###: <Here is the provided external knowledge>
###Dialogue History###: <Here is the dialogue history>
###Response###: <Here is the response>
###Judgement###:
Table 16: Instruction of hallucination localization and rationale provision.
As an assistant, your task is to serve as a response judge. Provided with the related knowledge, a
dialogue history and a generated response, your objective is to determine if the generated response
contains any hallucinated information that (1) directly contradicts the given knowledge, or (2) cannot
be verified from the provided knowledge and dialogue context.
You SHOULD refer to the following examples:
Example 1:
###Knowledge###: Use by a wider audience only came in 1995 when restrictions on the use of the
Internet to carry commercial traffic were lifted.
###Dialogue History###: [Human]: Can you imagine the world without internet access? [Assistant]:
Yeah, but once the access to the internet was a rare thing. do you remember? [Human]: I do. What
else can you tell me ?
###Response###: Well, I know that the internet was primarily available to the public in the early
1980s, with no restrictions on commercial traffic from the very beginning.
###Judgement###: Yes. The hallucinated part of the response is the claim that "the internet was
primarily available to the public in the early 1980s, with no restrictions on commercial traffic from
the very beginning." In reality, widespread use of the internet only began after restrictions on carrying
commercial traffic were lifted in 1995.
<More In-Context Examples>
You SHOULD first carefully evaluate each segment of the generated response and determine if the
response contains any hallucinated information. If any such content is found, your next step is to
identify the specific hallucinated segment and explain why it qualifies as such. Your judgement
MUST strictly follow the format demonstrated in the examples above and be well-organized, clear
and concise.
###Knowledge###: <Here is the provided external knowledge>
###Dialogue History###: <Here is the dialogue history>
###Response###: <Here is the response>
###Judgement###:
21

--- Page 22 ---

Table 17: Instruction of hallucination detection in a comparative setting.
As an assistant, your task is to serve as a response judge. Provided with the related knowledge, a
dialogue history and two generated responses, your objective is to determine which response contains
hallucinated information that (1) directly contradicts the given knowledge, or (2) cannot be verified
from the provided knowledge and dialogue context.
You SHOULD carefully evaluate each segment of both generated responses and determine which
response contains more or any hallucinated information. Your output should be strictly "1" or "2"
depending on which response contains the hallucinated information.
###Knowledge###: <Here is the provided external knowledge>
###Dialogue History###: <Here is the dialogue history>
###Response 1###: <Here is Response 1>
###Response 2###: <Here is Response 2>
###Judgement###:
Table 18: Instruction of evaluating hallucination localization and explanation.
As an assistant, your task is to serve as a meta-judge annotator. You will be provided with relevant
knowledge, a dialogue history, a response based on this knowledge, and a judgement about whether
the response contains hallucinations. Your objective is to critically evaluate the accuracy of this
judgement.
A hallucination in this context is defined as information in the response that either (1) directly
contradicts the given knowledge or (2) cannot be verified from the provided knowledge and dialogue
context. If the response does not contain any hallucinated information, the accurate judgement should
be "No". Conversely, if any hallucination is present, the accurate judgement should be "Yes", and it
should identify the specific hallucinated segment and provide the corresponding justifications.
You SHOULD carefully assess the correctness of the judgement. Your answer should strictly be
either "Accurate" if the judgement correctly identified the presence or absence of hallucination, or
"Inaccurate" if it did not.
###Knowledge###: <Here is the provided external knowledge>
###Dialogue History###: <Here is the dialogue history>
###Response###: <Here is the Response>
###Judgement###: <Here is the judgement>
###Your Meta-Judgement###:
22

--- Page 23 ---

G
Limitations and Negative Societal Impacts
We acknowledge that there are some limitations in our research. Firstly, since some of the responses
in our dialogues are generated by GPT-4 and other large language models, and labeled by GPT-4, the
dataset may inherit biases from these models to a certain extent. Although we cannot completely
eliminate these biases, we have taken measures to mitigate their impact, such as utilizing multiple
publicly available large language models to generate responses, thereby enhancing the diversity
and representativeness of the data. Secondly, while the HalluDial dataset is relatively large and
covers multiple domains, it may not fully capture all real-world conversation scenarios. Our dataset
has minimal potential for negative societal impact. This is primarily because our data is sourced
from publicly available seed datasets, and widely-used large language models (e.g., GPT-4), which
inherently limits the risk of adverse effects on individuals or society as a whole.
H
Responsibility and Dataset Liscence
We bear all responsibility in case of violation of rights and our dataset is under the license of CC
BY-NC-SA.
I
Datasheets for Our Dataset
I.1
Motivation
• For what purpose was the dataset created? Was there a specific task in mind? Was there
a specific gap that needed to be filled? Please provide a description.
This dataset was created to study and evaluate hallucinations of large language models in
information-seeking dialogues, a specific gap is mentioned in the Introduction.
• Who created the dataset (e.g., which team, research group) and on behalf of which
entity (e.g., company, institution, organization)?
This dataset was created by the authors of this paper.
• Who funded the creation of the dataset? If there is an associated grant, please provide the
name of the grantor and the grant name and number.
The institute of the authors funded the creation of the dataset.
• Any other comments?
None.
I.2
Composition
• What do the instances that comprise the dataset represent (e.g., documents, photos,
people, countries)? Are there multiple types of instances (e.g., movies, users, and ratings;
people and interactions between them; nodes and edges)? Please provide a description.
An instance of our dataset represents a dialogue. The description is provided in our paper.
• How many instances are there in total (of each type, if appropriate)?
Our dataset includes 4094 dialogues.
• Does the dataset contain all possible instances or is it a sample (not necessarily random)
of instances from a larger set? If the dataset is a sample, then what is the larger set? Is the
sample representative of the larger set (e.g., geographic coverage)? If so, please describe
how this representativeness was validated/verified. If it is not representative of the larger set,
please describe why not (e.g., to cover a more diverse range of instances, because instances
were withheld or unavailable).
No.
• What data does each instance consist of?
It is mentioned in this paper.
• Is there a label or target associated with each instance? If so, please provide a description.
Yes. The description is provided in this paper.
23

--- Page 24 ---

• Is any information missing from individual instances? If so, please provide a description,
explaining why this information is missing (e.g., because it was unavailable). This does not
include intentionally removed information, but might include, e.g., redacted text.
No.
• Are relationships between individual instances made explicit (e.g., users’ movie ratings,
social network links)? If so, please describe how these relationships are made explicit.
No. Instances concentrate on the same phenomenon.
• Are there recommended data splits (e.g., training, development/validation, testing)? If
so, please provide a description of these splits, explaining the rationale behind them.
Yes. It is provided in Appendix A.
• Are there any errors, sources of noise, or redundancies in the dataset? If so, please
provide a description.
No, the dataset is automatically generated by widely-used open-source large language
models or API-based large language models (e.g., GPT-4).
• Is the dataset self-contained, or does it link to or otherwise rely on external resources
(e.g., websites, tweets, other datasets)? If it links to or relies on external resources, a) are
there guarantees that they will exist, and remain constant, over time; b) are there official
archival versions of the complete dataset (i.e., including the external resources as they
existed at the time the dataset was created); c) are there any restrictions (e.g., licenses, fees)
associated with any of the external resources that might apply to a dataset consumer? Please
provide descriptions of all external resources and any restrictions associated with them, as
well as links or other access points, as appropriate.
It’s self-contained.
• Does the dataset contain data that might be considered confidential (e.g., data that is
protected by legal privilege or by doctor-patient confidentiality, data that includes the
content of individuals’ non-public communications)? If so, please provide a description.
No.
• Does the dataset contain data that, if viewed directly, might be offensive, insulting,
threatening, or might otherwise cause anxiety? If so, please describe why.
Yes. Some of the dialogues are about big events. Thus they may be offensive for people.
However, we believe our dataset’s offensiveness to be minimal, as the sources of the dataset
are publicly available seed datasets and widely-used large language models.
• Does the dataset identify any subpopulations (e.g., by age, gender)? If so, please
describe how these subpopulations are identified and provide a description of their respective
distributions within the dataset.
No.
• Is it possible to identify individuals (i.e., one or more natural persons), either directly or
indirectly (i.e., in combination with other data) from the dataset? If so, please describe
how.
Yes. Their names are given in the dialogues.
• Does the dataset contain data that might be considered sensitive in any way (e.g.,
data that reveals race or ethnic origins, sexual orientations, religious beliefs, political
opinions or union memberships, or locations; financial or health data; biometric or
genetic data; forms of government identification, such as social security numbers;
criminal history)? If so, please provide a description.
Yes. Our dataset may contain dialogues about religious beliefs, political opinions and so on.
• Any other comments?
None.
I.3
Collection Process
• How was the data associated with each instance acquired? Was the data directly ob-
servable (e.g., raw text, movie ratings), reported by subjects (e.g., survey responses), or
24

--- Page 25 ---

indirectly inferred/derived from other data (e.g., part-of-speech tags, model-based guesses
for age or language)? If the data was reported by subjects or indirectly inferred/derived from
other data, was the data validated/verified? If so, please describe how.
The original dialogues are from the open-source dialogue dataset. We present details in our
paper.
• What mechanisms or procedures were used to collect the data (e.g., hardware appara-
tuses or sensors, manual human curation, software programs, software APIs)? How
were these mechanisms or procedures validated?
The software program and software APIs. We present the details in our paper.
• Who was involved in the data collection process (e.g., students, crowdworkers, contrac-
tors) and how were they compensated (e.g., how much were crowdworkers paid)?
Crowdworkers. They are paid nicely.
• Over what timeframe was the data collected? Does this timeframe match the creation
timeframe of the data associated with the instances (e.g., recent crawl of old news articles)?
If not, please describe the timeframe in which the data associated with the instances was
created.
The dataset was collected in the early Spring of 2024. Yes.
• Were any ethical review processes conducted (e.g., by an institutional review board)? If
so, please provide a description of these review processes, including the outcomes, as well
as a link or other access point to any supporting documentation.
No.
• Did you collect the data from the individuals in question directly, or obtain it via third
parties or other sources (e.g., websites)?
By curating and augmenting a published dataset.
• Were the individuals in question notified about the data collection? If so, please describe
(or show with screenshots or other information) how notice was provided, and provide a link
or other access point to, or otherwise reproduce, the exact language of the notification itself.
N/A.
• Did the individuals in question consent to the collection and use of their data? If so,
please describe (or show with screenshots or other information) how consent was requested
and provided, and provide a link or other access point to, or otherwise reproduce, the exact
language to which the individuals consented.
N/A.
• If consent was obtained, were the consenting individuals provided with a mechanism to
revoke their consent in the future or for certain uses? If so, please provide a description,
as well as a link or other access point to the mechanism (if appropriate).
N/A.
• Has an analysis of the potential impact of the dataset and its use on data subjects (e.g.,
a data protection impact analysis) been conducted? If so, please provide a description of
this analysis, including the outcomes, as well as a link or other access point to any supporting
documentation.
No. We believe our dataset to have a limited negative effect, for all of the data is from either
published datasets or widely-used large language models.
• Any other comments?
None.
I.4
Preprocessing/cleaning/labeling
• Was any preprocessing/cleaning/labeling of the data done (e.g., discretization or bucket-
ing, tokenization, part-of-speech tagging, SIFT feature extraction, removal of instances,
processing of missing values)? If so, please provide a description. If not, you may skip the
remaining questions in this section.
No.
25

--- Page 26 ---

I.5
Uses
• Has the dataset been used for any tasks already? If so, please provide a description.
No.
• What (other) tasks could the dataset be used for?
We provide the details in our paper.
• Is there anything about the composition of the dataset or the way it was collected
and preprocessed/cleaned/labeled that might impact future uses? For example, is there
anything that a dataset consumer might need to know to avoid uses that could result in unfair
treatment of individuals or groups (e.g., stereotyping, quality of service issues) or other risks
or harms (e.g., legal risks, financial harms)? If so, please provide a description. Is there
anything a dataset consumer could do to mitigate these risks or harms?
No.
• Are there tasks for which the dataset should not be used? If so, please provide a
description.
No.
• Any other comments?
None.
I.6
Distribution
• Will the dataset be distributed to third parties outside of the entity (e.g., company,
institution, organization) on behalf of which the dataset was created? If so, please
provide a description.
Yes, the dataset is publicly available.
• How will the dataset will be distributed (e.g., tarball on website, API, GitHub)? Does
the dataset have a digital object identifier (DOI)?
On Github.
• When will the dataset be distributed?
It’s already been distributed.
• Will the dataset be distributed under a copyright or other intellectual property (IP)
license, and/or under applicable terms of use (ToU)? If so, please describe this license
and/or ToU, and provide a link or other access point to, or otherwise reproduce, any relevant
licensing terms or ToU, as well as any fees associated with these restrictions.
The dataset is licensed under the license of CC BY-NC-SA.
• Have any third parties imposed IP-based or other restrictions on the data associated
with the instances? If so, please describe these restrictions, and provide a link or other
access point to, or otherwise reproduce, any relevant licensing terms, as well as any fees
associated with these restrictions.
To the best of our knowledge, no third parties have imposed any IP-based or other restrictions
on the data associated with the instances.
• Do any export controls or other regulatory restrictions apply to the dataset or to
individual instances? If so, please describe these restrictions, and provide a link or other
access point to, or otherwise reproduce, any supporting documentation.
Based on our knowledge, there are no export controls or other regulatory restrictions that
apply to this dataset or to individual instances.
• Any other comments?
None.
I.7
Maintenance
• Who will be supporting/hosting/maintaining the dataset?
The authors of this paper.
26

--- Page 27 ---

• How can the owner/curator/manager of the dataset be contacted (e.g., email address)?
We will provide our email address.
• Is there an erratum? If so, please provide a link or other access point.
No.
• Will the dataset be updated (e.g., to correct labeling errors, add new instances, delete in-
stances)? If so, please describe how often, by whom, and how updates will be communicated
to dataset consumers (e.g., mailing list, GitHub)?
Yes. However, the frequency is not determined. We will publish the updated dataset on the
same repository and announce it.
• Will older versions of the dataset continue to be supported/hosted/maintained? If so,
please describe how. If not, please describe how its obsolescence will be communicated to
dataset consumers.
Yes. The older versions of the dataset will still be available on the same repository.
• If others want to extend/augment/build on/contribute to the dataset, is there a mech-
anism for them to do so? If so, please provide a description. Will these contributions
be validated/verified? If so, please describe how. If not, why not? Is there a process for
communicating/distributing these contributions to dataset consumers? If so, please provide
a description.
Yes. Through emails.
• Any other comments?
None.
27

```
