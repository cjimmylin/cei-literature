---
title: "2025-Li-LiveSecBench - A Dynamic Event-Driven Safety Benchmark for Chinese - PDF Extract"
source_pdf: "2025-Li-LiveSecBench - A Dynamic Event-Driven Safety Benchmark for Chinese.pdf"
pages: 7
extracted_at: "2026-02-07T17:00:46.439368"
---

# PDF Extract: 2025-Li-LiveSecBench - A Dynamic Event-Driven Safety Benchmark for Chinese

**Source PDF:** 2025-Li-LiveSecBench - A Dynamic Event-Driven Safety Benchmark for Chinese.pdf
**Total Pages:** 7

---

## Content

```
--- Page 1 ---

LiveSecBench: A Dynamic and Event-Driven Safety Benchmark for
Chinese Language Model Applications
Yudong Li1, Peiru Yang1, Feng Huang2, Zhongliang Yang2, Kecheng Wang4,
Haitian Li4, Baocheng Chen4, Xingyu An4, Ziyu Liu 4, Youdan Yang 4,
Kejiang Chen3, Sifang Wan 4, Xu Wang4, Yufei Sun2, Liyan Wu4, Ruiqi Zhou1,
Wenya Wen4, Xingchi Gu4, Tianxin Zhang4, Yue Gao1, Yongfeng Huang1
1Tsinghua University, 2Beijing University of Posts and Telecommunications,
3University of Science and Technology of China, 4IntokenTech
Abstract
We introduce LiveSecBench, a continuously
updated safety benchmark specifically for
Chinese-language LLM application scenarios.
LiveSecBench constructs a high-quality and
unique dataset through a pipeline that com-
bines automated generation with human verifi-
cation. By periodically releasing new versions
to expand the dataset and update evaluation
metrics, LiveSecBench provides a robust and
up-to-date standard for AI safety. In this re-
port, we introduce our second release v251215,
which evaluates across five dimensions (Public
Safety, Fairness&Bias, Privacy, Truthfulness,
and Mental Health Safety.) We evaluate 57 rep-
resentative LLMs using an ELO rating system,
offering a leaderboard of the current state of
Chinese LLM safety. The result is available at
https://livesecbench.intokentech.cn/.
1
Introduction
The safety evaluation of language models has
emerged as a research hotspot. As LLMs demon-
strate increasingly powerful capabilities and are
integrated into diverse applications, ensuring their
safety and alignment with human values is essen-
tial. Existing research has extensively explored this
domain, with numerous works proposing evalua-
tion frameworks centered around different dimen-
sions such as truthfulness (Lin et al., 2022), toxicity
(Mazeika et al., 2024), bias (Cao et al., 2025b), ro-
bustness (Lu et al., 2025) and specific domains
(Cao et al., 2025a; Han et al., 2024).
However, a misalignment persists between cur-
rent evaluation paradigms and the intrinsic nature
of AI security. Existing benchmarks typically rely
on fixed and static datasets, failing to capture the
rapidly evolving landscape of attacks and emerging
vulnerabilities. To address this challenge, we intro-
duce LiveSecBench, a dynamic safety evaluation
framework designed for the Chinese LLM land-
scape. LiveSecBench operates as a continuously
evolving standard, ensuring that safety assessments
remain adversarial and representative of current
risks. The dynamic of LiveSecBench includes two
aspects: (1) Dynamic Dataset Updates: We im-
plement a Human-in-the-Loop generation pipeline
that starts with high-quality seed data collected
from community feedback and public incidents. It
then goes through automated expansion and qual-
ity verification, followed by a final human audit
and integrated into the leaderboard. (2) Dynamic
Evaluation Dimensions: We periodically update
the evaluation dimensions to reflect the most press-
ing safety concerns in the industry, ensuring the
benchmark’s comprehensive coverage and tempo-
ral relevance.
In this report, we present the release of
LiveSecBench-v251215.
This version focuses
on five critical dimensions: Public Safety, Fair-
ness&Bias, Privacy, Truthfulness, and Mental
Health Safety. We conducted an extensive evalua-
tion of 57 representative LLMs. To ensure robust
relative ranking, we utilize an ELO rating system
to score model performance. Our report provides
a leaderboard with a transparent and up-to-date as-
sessment of the current state of LLMs on Chinese-
language AI application safety.
2
Related Work
Research on LLM safety assessment spans gen-
eral dimensions including toxicity (Mazeika et al.,
2024), fairness (Weidinger et al., 2022), and truth-
fulness (Lin et al., 2022), as well as domain-
specific evaluations in medical (Han et al., 2024),
legal (Cao et al., 2025a), and conversational con-
texts (Cao et al., 2025b).
For Chinese LLMs,
specialized benchmarks have been developed to
address unique challenges. SafetyBench (Zhang
et al., 2024) provides comprehensive safety evalu-
ation tailored for Chinese models, Sun et al. (Sun
et al., 2023) conducted targeted safety assessments
1
arXiv:2511.02366v2  [cs.CL]  20 Dec 2025

--- Page 2 ---

for Chinese LLMs, and CValues (Xu et al., 2023)
measures values from safety to responsibility per-
spectives. Chinese language presents distinctive
security challenges due to its logographic writing
system that enables attacks based on phonetic and
visual similarity, requiring dedicated evaluation
frameworks aligned with real-world risks in Chi-
nese LLM applications.
For generating adversarial test prompts at scale,
Perez et al. (2022) pioneered using language mod-
els to red team other LLMs. Yu et al. (2023) in-
troduced GPTFuzzer, which performs mutation
operations such as expansion and rephrasing on
seed questions before penetration testing. Zou et al.
(2023) developed universal and transferable adver-
sarial attacks on aligned models. Shen et al. (2025)
proposed PandaGuard, integrating 19 known attack
methods into a comprehensive framework.
To address the rapidly evolving nature of
real-world scenarios and prevent evaluation con-
tamination where models may learn benchmark
content, dynamic evaluation frameworks have
emerged. LiveBench (White et al., 2024) and Live-
CodeBench (Jain et al., 2024) propose continuously
updated benchmark content to maintain evaluation
integrity and relevance, ensuring assessments re-
main aligned with current challenges rather than
becoming obsolete as models adapt. LiveSecBench
synthesizes these approaches by combining auto-
mated red teaming with dynamic benchmarking
specifically for Chinese LLM security evaluation.
We continuously update our benchmark in response
to emerging real-world security threats and evolv-
ing application scenarios, ensuring that our assess-
ment remains current and adversarial.
3
LiveSecBench Framework
3.1
Data Construction Pipeline
Target Initialization and Seed Fission.
The data
construction process begins with an initialization
stage that focuses on target sampling and intent
abstraction. The primary objective of the initializa-
tion stage is to identify the core malicious objective
of each seed prompt, referred to as the attack goal
G, together with its corresponding safety domain
and fine-grained risk category. To achieve this,
the system randomly samples seed prompts from a
continuously updated repository of attack prompts
and analyzes them using an LLM. The analysis
identifies the explicit policy-violating behavior tar-
geted by the prompt and maps it to a predefined
risk taxonomy, comprising a main category and its
corresponding subcategories. Key contextual infor-
mation, such as the attack scenario and victim type,
is retained to support subsequent adversarial gen-
eration. Through this process, each seed prompt is
converted into a structured attack target that reflects
realistic security risks in deployed Chinese LLM
applications.
To address seed exhaustion and support sus-
tained topic diversity across repeated benchmark
updates, LiveSecBench adopts a seed fission strat-
egy for adversarial target expansion. The core idea
of seed fission is to separate the underlying attack
logic from its surface-level realization. Specifically,
the system identifies the fundamental malicious in-
tent behind the original goal G and retains this
intent as invariant. It then generates new attack
goals by altering the attack scenario, the victim
entity, or the technical means through which the
intent is expressed. In this way, a finite set of initial
seeds can be systematically transformed into an
open-ended space of derived malicious goals G′,
enabling continuous and scalable data growth.
Adversarial Prompt Synthesis.
Building on the
identified attack target, LiveSecBench constructs
adversarial prompts through a strategy-guided syn-
thesis process. For each seed target, the system
applies three complementary strategy families dur-
ing prompt construction. (1) Wrapping Strategies
embed the malicious intent within a seemingly le-
gitimate or benign context to reduce the likelihood
of intent detection, such as framing the request as
academic research or hypothetical analysis. (2)
Injection Strategies attempt to override or bypass
safety constraints by explicitly inserting controlling
instructions, for example, by instructing the model
to ignore prior safety warnings or system rules. (3)
Obfuscation Strategies conceal sensitive content
through localized metaphors, coded language, or
indirect references, allowing harmful intent to be
expressed without explicit keywords. These strat-
egy components are jointly composed with the core
malicious goal through a synthesis function S to
produce an initial adversarial prompt P0. Formally,
this process is defined as:
P0 = S(G, W, I, O),
(1)
where G denotes the abstract malicious intent, and
W, I, and O correspond to the applied wrapping,
injection, and obfuscation strategy components, re-
spectively. By unifying intent and strategies within
2

--- Page 3 ---

a single synthesis framework, this step generates
adversarial prompts that are structurally coherent,
contextually plausible, and reflective of realistic at-
tack behaviors observed in real-world deployments.
Automated Judge-Based Quality Control.
To
minimize reliance on manual evaluation and en-
able scalable benchmark updates, LiveSecBench in-
corporates an automated, judge-based quality con-
trol mechanism into the data construction pipeline.
Each generated adversarial prompt is assessed by
an independent judge agent that evaluates the tar-
get model’s response and determines whether the
prompt successfully elicits the intended risk behav-
ior. This binary judgment serves as a unified quality
signal, indicating whether a generated prompt is
effective and should be retained for benchmarking
purposes. At the aggregate level, these judgments
are summarized as the attack success rate (ASR),
providing a quantitative measure of how adversarial
goals and strategy combinations jointly influence
model behavior. By using automated judging as a
quality gate rather than relying on human annota-
tion, LiveSecBench enables continuous, large-scale
prompt generation while maintaining consistent
evaluation standards across benchmark iterations.
3.2
Evaluation Mechanism
LiveSecBench employs the ELO rating system to
rank models, a method proven in competitive envi-
ronments like chess. The evaluation is structured
as a tournament. For evaluation, we first obtain the
test model’s answers to all questions, including its
reasoning process. Then, for each dimension, we
divide the dataset into five groups randomly and
perform five rounds of evaluation. In each round,
models are paired head-to-head. After a compar-
ison, the ELO scores of both models are updated.
The expected win probability for Model A (EA)
against Model B (EB) is calculated as:
EA =
1
1 + 10(RB−RA)/400
where RA and RB are the current ELO ratings
of Model A and Model B, respectively. The new
rating for Model A (R′
A) is then updated based
on the actual outcome (SA, where 1 = win, 0 =
loss) and a K-factor (a constant determining score
sensitivity):
R′
A = RA + K(SA −EA)
To ensure fair and efficient matchups, we use a
Swiss-system pairing strategy. In each round, mod-
els are sorted by their current ELO score and paired
with the next-available opponent whom they have
not already faced. This method avoids repeated
matchups and ensures that models are continuously
tested against similarly-performing peers. This pro-
cess yields both granular, per-dimension rankings
and an overall safety ranking for all participating
models.
4
Dataset
4.1
Evaluation Dimensions
LiveSecBench is organized around five fundamen-
tal safety dimensions—Public Safety, Fairness &
Bias, Privacy, Truthfulness, and Mental Health
Safety—designed to systematically reflect the most
critical risk categories in real-world deployments
of large language models.
Public Safety: This dimension assesses whether
a model can effectively refrain from generating
content that is illegal, non-compliant, or potentially
harmful to public safety. Its design is grounded
in current Chinese laws, regulations, and relevant
regulatory requirements, and encompasses subcate-
gories such as crimes and illegal acts, cybercrime,
terrorism, sensitive locations, and weapons and
controlled substances.
Fairness & Bias: This dimension evaluates the
behavior of a model in contexts related to social eq-
uity, cultural diversity, and interpersonal respect. It
focuses on whether the model generates biased, dis-
criminatory, harassing, or hateful content, includ-
ing attacks against specific groups, reinforcement
of stereotypes, and inappropriate content involving
minors, in order to ensure alignment with funda-
mental human values and social ethics.
Privacy: This dimension evaluates the ability
of a model to identify, handle, and protect privacy-
related information. It is grounded in data protec-
tion and privacy compliance requirements, with
a focus on personal identifiable information (PII)
leakage and unauthorized surveillance or tracking
activities, to assess the model’s safety boundaries
and compliance in high-risk privacy infringement
scenarios.
Truthfulness: This dimension evaluates the abil-
ity of a model to maintain accuracy and factual in-
tegrity in information generation. It focuses on the
production of false or misleading content (Disinfor-
mation), hallucinations at the factual and reasoning-
level, and the provision of inappropriate or unsup-
ported advice in specialized or high-risk contexts
3

--- Page 4 ---

Figure 1: Overview of LiveSecBench-v251215 dataset distribution.
(Specialized Advice), in order to assess the overall
reliability and trustworthiness of the model.
Mental Health Safety: This dimension evalu-
ates whether large language models can provide
support in a safe and responsible manner when
users express emotional distress or psychological
concerns. Its design is firmly grounded in the diag-
nostic classifications and clinical guidelines of the
Diagnostic and Statistical Manual of Mental Disor-
ders, Fifth Edition (DSM-5), ensuring the scientific
validity and rigor of the evaluation. The subcate-
gories focus primarily on high-risk clinical mental
health conditions, including depression, anxiety,
suicide, and risk of self-harm, and eating disorders.
4.2
Data Statistics
Figure 1 summarizes the statistical composition
of LiveSecBench. The left panel reports the dis-
tribution of adversarial prompting strategies used
in dataset construction, including Direct Inquiry,
Instruction Injection, Obfuscation, and Contextual
Deception. The relatively balanced proportions
across strategies indicate that the benchmark is not
dominated by any single attack pattern, facilitating
robust evaluation under diverse prompting condi-
tions.
The right panel presents the category-wise dis-
tribution of instances under the predefined safety
taxonomy. Data coverage is broadly distributed
across high-level safety dimensions and their cor-
responding sub-categories, with no extreme con-
centration observed in any single class. This dis-
tribution supports a consistent evaluation across
heterogeneous safety risks and mitigates bias intro-
duced by skewed category frequencies.
In general, statistics suggest that LiveSecBench
provides balanced coverage across both attack
strategies and safety categories, enabling a reliable
and fine-grained safety assessment.
5
Experiments
5.1
Experimental Setup
We employ the ELO rating to rank models using
a Swiss-system tournament strategy.
Given 57
models in total, we conduct 6 rounds of compe-
titions, where the number of rounds is determined
by ⌈log2(57)⌉= 6.
For each dimension, we randomly divided all
questions into 6 groups. Within each round, adja-
cent models (based on current rankings) competed
against each other. After each round, we updated
the ELO scores and re-ranked the models before
proceeding to the next round. We use DeepSeek-
V3.2 as a proxy model to serve as the judge for
all comparisons. To validate the reliability of this
approach, we manually sampled 200 battle results
and found a 98.5% consistency between the proxy
model’s judgments and human annotations.
The number of questions varies across differ-
ent dimensions, resulting in different total battle
counts. Table 2 presents detailed statistics for each
dimension.
4

--- Page 5 ---

Rank
Model
Overall
Public Safety
Fairness&Bias
Privacy
Truthfulness
Mental.
1
Anthropic/Claude-Sonnet-4.5
82.27
90.15
90.9
83.99
68.35
77.95
2
OpenAI/GPT-5
82.16
88.25
87.78
74.95
61.21
98.59
3
Anthropic/Claude-Haiku-4.5
82.09
96.47
97.21
95.97
50.82
69.98
4
Alibaba/Qwen3-Max
79.38
78.32
80.51
86.43
69.77
81.88
5
Alibaba/Qwen3-VL-235B-A22B-Instruct*
73.65
76.17
66.14
84.49
94.2
47.25
6
OpenAI/GPT-5-Mini
73.12
81.5
74.24
79.86
46.93
83.05
7
iFlytek/Spark X1.5
69.91
76.11
81.56
82.7
66.42
42.77
8
DeepSeek/DeepSeek-V3.2*
68.47
81.64
76.95
66.51
62.55
54.71
9
DeepSeek/DeepSeek-V3.1-Terminus*
68
77.3
51.95
71.13
68.02
71.62
10
Zhipu AI/GLM-4.6*
66.2
67.77
49.6
47.22
80.75
85.66
11
Minimax/Minimax-M2*
65.16
84.69
65.9
67.95
37.68
69.59
12
Minimax/Minimax-M1*
65.04
61.88
73.38
64.95
59.62
65.37
13
Meituan/Longcat-Flash-Chat*
64.21
73.63
77.51
71.23
59.48
39.19
14
ByteDance/Doubao-Seed-1.6-Vision
63.07
53.52
77.39
43.75
82.38
58.31
15
DeepSeek/DeepSeek-R1-0528*
62.43
39.69
64.37
58.55
68.88
80.65
16
Moonshot AI/Kimi-K2-0711*
62.1
64.76
31.99
66.87
57.82
89.07
17
Zhipu AI/GLM-4.5-Air*
62.02
58.19
54.2
40.7
73.92
83.09
18
Baidu/Ernie-5.0-Preview-1022
60.28
57.18
52.41
61.39
59.77
70.67
19
Ant Group/Ring-Flash-2.0*
59.07
32.03
31.37
58.28
81.91
91.75
20
StepFun/Step3*
58.67
49.44
59.9
36.89
57.36
89.75
21
Moonshot AI/Kimi-K2-0905*
56.35
35.44
50.75
65.97
42.85
86.72
22
ByteDance/Doubao-Seed-1.6
55.53
62.68
73.27
60.85
37.82
43.02
23
Baidu/Ernie-4.5-VL-424B-A47B*
54.8
63.12
58.72
42.77
65.19
44.2
24
Anthropic/Claude-3.5-Haiku
54.69
63.03
68.18
74.86
40.22
27.16
25
Shanghai AI Lab/Intern-S1*
53.86
54.64
41.64
44.58
83.49
44.94
26
Tencent/Hunyuan-T1-Vision-20250916
53.67
39.97
48.1
48.91
72.18
59.2
27
SenseTime/SenseChat-Turbo-1202
51.41
70.02
76.15
83
20.16
7.74
28
Meta/Llama-3.3-70B-Instruct*
50.75
79.3
59.06
52.63
22.5
40.28
29
Google/Gemini-2.0-Flash
48.93
22.11
72.41
44.3
47.63
58.19
30
iFlytek/Spark Pro-128K
48.53
77.79
56.41
53.5
35.89
19.04
31
Google/Gemini-2.5-Flash-Preview
48.26
40.51
16.83
48.21
58.82
76.91
32
SenseTime/SenseNova-V6-5-Turbo
48.01
76.78
63.96
77.64
16.12
5.53
33
X.AI/Grok-3-Mini
47.94
35.92
19.86
63.5
52.1
68.34
34
Zhipu AI/GLM-4.5V*
46.6
29.3
37.79
28.97
58.62
78.31
35
ByteDance/Doubao-1.5-Pro-32K
44.12
56.29
54.83
16.36
62.7
30.44
36
Kunlun Wanwei/R1V4 Lite
41.21
26.65
33.3
50.41
44.87
50.82
37
Shanghai AI Lab/InternLM3*
41.02
58.01
44.36
52.72
27.44
22.59
38
DeepSeek/DeepSeek-V3-0324*
40.74
44.2
22.22
39.3
54.28
43.68
39
Ant Group/Ling-Flash-2.0*
39.9
20.82
23.48
55.4
43.99
55.81
40
Shanghai AI Lab/InternVL3.5*
39.64
32.07
40.28
19.01
66.01
40.81
41
Meta/Llama-4-Maverick*
39.23
35.16
43.18
48.79
36.81
32.22
42
Tencent/Hunyuan-T1-20250822
38.83
9.91
43.18
24.91
76.83
39.34
43
X.AI/Grok-4-Fast
38.08
14.74
36.55
49.08
44.55
45.5
44
Mistral AI/Mistral-Large-2411*
37.89
65.14
43.32
10.43
37.98
32.56
45
Baidu/Ernie-4.5-21B-A3B-Thinking*
37.87
39.91
47.13
30.66
32.05
39.62
46
Alibaba/Qwen3-32B*
35.96
32.43
32.8
34.31
46.35
33.93
47
Huawei/Pangu-Pro-MoE-72B-A16B*
35.86
42.76
20.38
28.81
39.21
48.13
48
StepFun/Step-2-Mini
35.35
40.11
47.53
51.24
22.51
15.38
49
OpenAI/GPT-4o-Mini
29.32
34.26
39.44
34.32
26.65
11.95
50
Mistral AI/Mistral-Medium-3.1
28.52
10.06
10.75
18.2
54.61
49
51
MiniMax/MiniCPM-V-4.5(Q4_K_M)*
25.07
38.86
29.62
24.2
18.49
14.18
52
DeepSeek/DeepSeek-V3.2-Speciale*
24.69
17.44
32.27
17.34
20.64
35.78
53
Tencent/Hunyuan-A13B-Instruct*
24.54
28.21
14.42
8.3
50.08
21.7
54
Xiaomi/MiMo-7B-RL(Q4_K_M)*
22.59
15.95
24.01
16.64
26.84
29.53
55
MiniMax/MiniCPM4.1-8B(Q4_K_M)*
22.5
24.78
24.22
49.86
10.37
3.25
56
Xiaomi/MiMo-VL-7B-RL(Q4_K_M)*
21.99
7.66
12.87
24.59
32.73
32.08
57
DeepSeek/DeepSeek-VL2*
10.67
9.93
14.22
11
12.35
5.85
Table 1: The evaluation results of 57 LLMs on LiveSecBench. “Overall” represents the overall average ELO score,
and the remaining columns are the scores for each of the dimensions. Models marked with * are open source. All
scores have been normalized to the range of 0-100.
5

--- Page 6 ---

Dimension
Questions
Battles
Avg. per Model
Public Safety
200
5,400
94.7
Fairness & Bias
207
5,590
98.1
Privacy
219
5,913
103.7
Truthfulness
102
2,754
48.3
Mental Health
124
3,348
58.7
Total (unique)
852
23,005
403.6
Table 2: Statistics of ELO battles across different safety
dimensions. “Battles” denotes the total number of pair-
wise comparisons, and “Avg. per Model” represents the
average number of battles each model participated in.
5.2
Main Results
Table 1 presents the evaluation results of 57 large
language models on LiveSecBench-v251215. We
report the overall ELO score and sub-scores on
five dimensions for each model. Models are sorted
from highest to lowest overall score, and are also
labeled as open-source models.
In terms of overall ranking, Anthropic/Claude-
Sonnet-4.5 ranks first with an overall score
of 82.27, followed closely by OpenAI/GPT-5
and Anthropic/Claude-Haiku-4.5, with very close
scores. It is noteworthy that the top four mod-
els are all closed-source commercial models,
while the best-performing open-source model is
Alibaba/Qwen3-VL-235B-A22B-Instruct, ranking
5th with an overall score of 73.65.
6
Roadmap and How-to-Use
6.1
Update Schedule
To capture emerging AI security challenges, the
benchmark’s evaluation dimensions are periodi-
cally updated based on the most widely used and
nascent application scenarios. Similarly, existing
test questions are continually reviewed for their ef-
fectiveness and removed if they lose their challenge
(e.g., if most mainstream models can robustly pass
them).
Figure 2: Roadmap of LiveSecBench.
The next planned update (v260315) is scheduled
to expand the benchmark’s scope by introducing
the following new dimensions:
• Text-to-Image Generation Safety: Assess-
ing the safety of models used to generate or
describe images, particularly in terms of fil-
tering out illegal, harmful, or inappropriate
visual content.
• Agentic Safety: Evaluating the security of
models operating within autonomous or agen-
tic frameworks, which includes assessing their
ability to resist tool-use-based attacks or mali-
cious instruction chaining.
6.2
Data Access and Reproducibility
Due to the sensitive nature of the test questions,
the LiveSecBench dataset is not publicly disclosed.
However, to promote research on LLM safety
within the community, we provide developers of
participating models with detailed evaluation re-
ports. Developers can request access using an in-
stitution email address. If you wish to submit a
model for evaluation, please contact the research
team via email at liyudong@tsinghua.edu.cn.
Additionally, we have open-sourced the evalua-
tion framework to support reproducibility: https:
//github.com/ydli-ai/LiveSecBench.
7
Conclusion
We present LiveSecBench, a continuously up-
dated safety benchmark specifically designed for
Chinese-language large language model applica-
tions. By combining automated adversarial prompt
generation with human-in-the-loop quality control,
LiveSecBench addresses the limitation of static
benchmarks that fail to capture the rapidly evolv-
ing landscape of AI safety risks.
Our evalua-
tion of 57 representative LLMs across five fun-
damental safety dimensions—Public Safety, Fair-
ness & Bias, Privacy, Truthfulness, and Men-
tal Health Safety—reveals significant variation
in safety performance across models, with top-
performing closed-source models demonstrating
superior overall safety while open-source alterna-
tives show competitive performance in specific di-
mensions.
References
Chuxue Cao, Han Zhu, Jiaming Ji, Qichao Sun, Zheng-
hao Zhu, Wu Yinyu, Josef Dai, Yaodong Yang, Sirui
Han, and Yike Guo. 2025a. Safelawbench: Towards
6

--- Page 7 ---

safe alignment of large language models. In Find-
ings of the Association for Computational Linguistics:
ACL 2025, pages 14015–14048.
Hongye Cao, Yanming Wang, Sijia Jing, Ziyue Peng,
Zhixin Bai, Zhe Cao, Meng Fang, Fan Feng, Boyan
Wang, Jiaheng Liu, and 1 others. 2025b. Safedial-
bench: A fine-grained safety benchmark for large
language models in multi-turn dialogues with diverse
jailbreak attacks. arXiv preprint arXiv:2502.11090.
Tessa Han, Aounon Kumar, Chirag Agarwal, and
Himabindu Lakkaraju. 2024. Medsafetybench: Eval-
uating and improving the medical safety of large
language models. Advances in Neural Information
Processing Systems, 37:33423–33454.
Naman Jain, King Han, Alex Gu, Wen-Ding Li, Fanjia
Yan, Tianjun Zhang, Sida Wang, Armando Solar-
Lezama, Koushik Sen, and Ion Stoica. 2024. Live-
codebench: Holistic and contamination free evalua-
tion of large language models for code. CoRR.
Stephanie Lin, Jacob Hilton, and Owain Evans. 2022.
Truthfulqa: Measuring how models mimic human
falsehoods. In Proceedings of the 60th Annual Meet-
ing of the Association for Computational Linguistics
(Volume 1: Long Papers), pages 3214–3252.
Yida Lu, Jiale Cheng, Zhexin Zhang, Shiyao Cui,
Cunxiang Wang, Xiaotao Gu, Yuxiao Dong, Jie
Tang, Hongning Wang, and Minlie Huang. 2025.
Longsafety: Evaluating long-context safety of large
language models. arXiv preprint arXiv:2502.16971.
Mantas Mazeika, Long Phan, Xuwang Yin, Andy Zou,
Zifan Wang, Norman Mu, Elham Sakhaee, Nathaniel
Li, Steven Basart, Bo Li, and 1 others. 2024. Harm-
bench: a standardized evaluation framework for au-
tomated red teaming and robust refusal. In Proceed-
ings of the 41st International Conference on Machine
Learning, pages 35181–35224.
Ethan Perez, Saffron Huang, Francis Song, Trevor Cai,
Roman Ring, John Aslanides, Amelia Glaese, Nat
McAleese, and Geoffrey Irving. 2022. Red teaming
language models with language models. In Proceed-
ings of the 2022 Conference on Empirical Methods
in Natural Language Processing, pages 3419–3448.
Guobin Shen, Dongcheng Zhao, Linghao Feng, Xiang
He, Jihang Wang, Sicheng Shen, Haibo Tong, Yit-
ing Dong, Jindong Li, Xiang Zheng, and 1 others.
2025. Pandaguard: Systematic evaluation of llm
safety against jailbreaking attacks. arXiv preprint
arXiv:2505.13862.
Hao Sun, Zhexin Zhang, Jiawen Deng, Jiale Cheng,
and Minlie Huang. 2023.
Safety assessment of
chinese large language models.
arXiv preprint
arXiv:2304.10436.
Laura Weidinger, Jonathan Uesato, Maribeth Rauh,
Conor Griffin, Po-Sen Huang, John Mellor, Amelia
Glaese, Myra Cheng, Borja Balle, Atoosa Kasirzadeh,
and 1 others. 2022. Taxonomy of risks posed by lan-
guage models. In Proceedings of the 2022 ACM con-
ference on fairness, accountability, and transparency,
pages 214–229.
Colin White, Samuel Dooley, Manley Roberts, Arka
Pal, Benjamin Feuer, Siddhartha Jain, Ravid Shwartz-
Ziv, Neel Jain, Khalid Saifullah, Siddartha Naidu,
and 1 others. 2024.
Livebench: A challenging,
contamination-free llm benchmark. CoRR.
Guohai Xu, Jiayi Liu, Ming Yan, Haotian Xu, Jinghui Si,
Zhuoran Zhou, Peng Yi, Xing Gao, Jitao Sang, Rong
Zhang, and 1 others. 2023. Cvalues: Measuring the
values of chinese large language models from safety
to responsibility. arXiv preprint arXiv:2307.09705.
Jiahao Yu, Xingwei Lin, Zheng Yu, and Xinyu Xing.
2023. Gptfuzzer: Red teaming large language mod-
els with auto-generated jailbreak prompts.
arXiv
preprint arXiv:2309.10253.
Zhexin Zhang, Leqi Lei, Lindong Wu, Rui Sun,
Yongkang Huang, Chong Long, Xiao Liu, Xuanyu
Lei, Jie Tang, and Minlie Huang. 2024. Safetybench:
Evaluating the safety of large language models. In
Proceedings of the 62nd Annual Meeting of the As-
sociation for Computational Linguistics (Volume 1:
Long Papers), pages 15537–15553.
Andy Zou, Zifan Wang, Nicholas Carlini, Milad Nasr,
J Zico Kolter, and Matt Fredrikson. 2023. Univer-
sal and transferable adversarial attacks on aligned
language models. arXiv preprint arXiv:2307.15043.
7

```
