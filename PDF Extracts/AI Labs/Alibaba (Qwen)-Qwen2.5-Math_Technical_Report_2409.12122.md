---
title: "Qwen2.5 Math Technical Report 2409.12122"
source_pdf: "AI Labs/Alibaba (Qwen)/Qwen2.5-Math/Qwen2.5-Math_Technical_Report_2409.12122.pdf"
company: "Alibaba (Qwen)"
pages: 39
extracted_at: "2026-01-31T17:32:27.533407"
type: "ai_lab_paper"
---

# Qwen2.5 Math Technical Report 2409.12122

**Company/Lab:** Alibaba (Qwen)
**Model:** Qwen2.5-Math
**Source PDF:** AI Labs/Alibaba (Qwen)/Qwen2.5-Math/Qwen2.5-Math_Technical_Report_2409.12122.pdf
**Total Pages:** 39

---

## Content

```
--- Page 1 ---

QWEN2.5-MATH TECHNICAL REPORT:
TOWARD MATHEMATICAL EXPERT MODEL VIA SELF-
IMPROVEMENT
An Yang, Beichen Zhang, Binyuan Hui, Bofei Gao, Bowen Yu†, Chengpeng Li, Dayiheng Liu†,
Jianhong Tu, Jingren Zhou, Junyang Lin†, Keming Lu, Mingfeng Xue, Runji Lin, Tianyu Liu,
Xingzhang Ren, Zhenru Zhang
Qwen Team, Alibaba Group∗
ABSTRACT
In this report, we present a series of math-specific large language models:
Qwen2.5-Math and Qwen2.5-Math-Instruct-1.5B/7B/72B. The core innovation of
the Qwen2.5 series lies in integrating the philosophy of self-improvement through-
out the entire pipeline, from pre-training and post-training to inference: (1) During
the pre-training phase, Qwen2-Math-Instruct is utilized to generate large-scale,
high-quality mathematical data. (2) In the post-training phase, we develop a reward
model (RM) by conducting massive sampling from Qwen2-Math-Instruct. This
RM is then applied to the iterative evolution of data in supervised fine-tuning
(SFT). With a stronger SFT model, it’s possible to iteratively train and update the
RM, which in turn guides the next round of SFT data iteration. On the final SFT
model, we employ the ultimate RM for reinforcement learning, resulting in the
Qwen2.5-Math-Instruct. (3) Furthermore, during the inference stage, the RM is
used to guide sampling, optimizing the model’s performance.
Qwen2.5-Math-Instruct supports both Chinese and English, and possess advanced
mathematical reasoning capabilities, including Chain-of-Thought (CoT) and Tool-
Integrated Reasoning (TIR). We evaluate our models on 10 mathematics datasets
in both English and Chinese, such as GSM8K, MATH, GaoKao, AMC23, and
AIME24, covering a range of difficulties from grade school level to math compe-
tition problems. The flagship model, Qwen2.5-Math-72B-Instruct, significantly
outperforms both open-source models and leading closed-source models (e.g., GPT-
4o, Gemini Math-Specialized 1.5 Pro). Particularly in the challenging AMC 2023,
with the assistance of RM, Qwen2.5-Math-72B-Instruct successfully solves almost
all the problems. Qwen2.5-Math-7B-Instruct surpasses Qwen2-Math-Instruct 72B
in performance. Under CoT and TIR settings, it achieves MATH scores of 83.6
and 85.3, respectively. Even our smallest 1.5B model, achieving a MATH score
of around 80 when utilizing the Python Interpreter, outperforms the majority of
current models in this domain. We hope that Qwen2.5-Math can contribute to the
community for solving complex mathematical problems.
The base models, instruct models, and reward model of the Qwen2.5-Math series
are available on Hugging Face 1 and ModelScope2, and the evaluation scripts on
GitHub3. We have also developed a demo that supports the TIR mode in Qwen-
Agent4, which allows running code locally to experience Tool-Integrated Reasoning
capabilities of Qwen2.5-Math.
∗Authors are ordered alphabetically by the first name. †Corresponding author.
1https://huggingface.co/Qwen
2https://modelscope.cn/organization/qwen
3https://github.com/QwenLM/Qwen2-Math
4https://github.com/QwenLM/Qwen-Agent
1
arXiv:2409.12122v1  [cs.CL]  18 Sep 2024

--- Page 2 ---

CONTENTS
1
Introduction
3
2
Qwen2.5-Math Pre-training
4
3
Qwen2.5-Math Post-training
5
3.1
Supervised Fine-tuning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6
3.1.1
Chain-of-Thought Data Synthesis . . . . . . . . . . . . . . . . . . . . . .
6
3.1.2
Tool-integrated Reasoning Data Synthesis . . . . . . . . . . . . . . . . . .
6
3.2
Reward Model Training . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7
3.2.1
Data Synthesis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7
3.2.2
Training Strategy . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7
3.3
Reinforcement Learning
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7
4
Decontamination
8
5
Evaluation
9
5.1
Base Models . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
9
5.2
Instruction Models
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
9
6
Conclusion
14
A Case Study of Qwen2-MATH on Olympiad-level Problems
19
A.1
Number Theory . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
19
A.2 Algebra . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
22
A.3
Counting & Probability . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
27
A.4
Geometry . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
30
B
Prompts Used in the Evaluation
31
2

--- Page 3 ---

1
INTRODUCTION
Figure 1: The pass@1 performance of Qwen2.5-Math-72B-Instruct on MATH by the Chain-of-
Thought reasoning.
Over the past year, we have devoted considerable effort to researching and enhancing the reasoning
capabilities of large language models, with a particular emphasis on their ability to solve arithmetic
and mathematical problems. In this report, we introduce a series of math-specific large language
models, Qwen2.5-Math, Qwen2.5-Math-RM, and Qwen2.5-Math-Instruct-1.5B/7B/72B. To provide
a comprehensive understanding of the technical developments behind Qwen2.5-Math, we also offer a
detailed overview of its predecessor, Qwen2-Math (Qwen, 2024).
We introduce a series of self-improvement techniques to develop Qwen2.5-Math models on top of
the Qwen2-Math. Self-improvement techniques take advantage of supervision from large language
models themselves (Cao et al., 2024). Specifically, we apply self-improvement from three aspects
during the training of Qwen2.5-Math. In pre-training, we employ Qwen2-Math-Instruct to synthesize
math queries and corresponding responses on a large scale to enrich the pre-training corpus of
Qwen2.5-Math. In post-training, we train a reward model on massive sampling from previous models
and apply it to the iterative evolution of data in supervised fine-tuning. The better mathematical
models trained from this enhancement lead to a more robust reward model, Qwen2.5-Math-RM.
Then, we use this reward model in reinforcement learning and best-of-N sampling during inference.
Synthetic data and judgment play a significant role in the enhancement of Qwen2.5-Math compared
with its predecessor.
Specifically, the overall pipelines for developing Qwen2-Math and Qwen2.5-Math are illustrated in
Figure 2. First, the Qwen2-Math base models are trained on a high-quality mathematical pre-training
dataset called the Qwen Math Corpus v1, which contains approximately 700 billion tokens. Second,
we train a math-specific reward model Qwen2-Math-RM, derived from Qwen2-Math-72B, to create
the Qwen2-Math-Instruct models. This reward model is used to construct Supervised Fine-Tuning
(SFT) data through Rejection Sampling (Yuan et al., 2023). Moreover, the reward model plays a
key role in the reinforcement learning stage, where we employ Group Relative Policy Optimization
(GRPO) (Shao et al., 2024) following SFT. Third, leveraging the Qwen2-Math-72B-Instruct model,
we synthesize additional high-quality mathematical pre-training data, which serves as the foundation
for Qwen Math Corpus v2. This updated corpus contains over 1 trillion tokens and is used to pre-train
the Qwen2.5-Math models. Lastly, similar to the process used for the Qwen2-Math-Instruct models,
we construct the Qwen2.5-Math-RM and Qwen2.5-Math-Instruct models. An important distinction
in this stage is the inclusion of both English and Chinese Chain-of-Thought (CoT) reasoning data, as
3

--- Page 4 ---

well as Tool-Integrated Reasoning (TIR) data, for training the Qwen2.5-Math-Instruct models, as
opposed to using only English CoT data as was done for Qwen2-Math-Instruct.
We evaluate our math-specific models on eight English and Chinese math benchmarks. Notably, the
Qwen2.5-Math-7B base model achieves scores of 91.6, 55.4, and 57.6 on GSM8K (Cobbe et al.,
2021), MATH (Hendrycks et al., 2021b), and GaoKao Math Cloze (Zhang et al., 2023), respectively,
outperforming the Qwen2-72B (Yang et al., 2024) general model, which achieves scores of 89.5,
51.1, and 55.9 on the same datasets. Additionally, the Qwen2.5-Math-72B base model sets a new
state-of-the-art on the MATH benchmark, achieving a score of 66.8—an improvement of 5.3 points
over Qwen2-Math-72B and 15.7 points over Qwen2-72B.
For the Instruct models, in CoT mode, the Qwen2.5-Math-1.5B-Instruct model surpasses the perfor-
mance of all currently available open-source models on most metrics, including models as large as
70B parameters. Furthermore, the Qwen2.5-Math-7B-Instruct model nearly matches the performance
of the Qwen2-Math-72B-Instruct model, indicating that improvements to the training data and strategy
can, to a certain extent, compensate for the scaling up of parameters. The Qwen2.5-Math-72B-Instruct
model outperforms the Qwen2-Math-72B-Instruct model by an average margin of 4.4 and 6.1 points
in English and Chinese, respectively, establishing itself as the best open-source mathematical model
currently available. Moreover, all model sizes demonstrate significant improvements in their Chinese
math problem-solving capabilities. In our newly introduced TIR mode, performance sees further
enhancement compared to CoT. For instance, the 72B model achieves close to 90 points on the
MATH benchmark, and even the 1.5B model scores around 80, demonstrating that Qwen2.5 is now
highly proficient at leveraging the Python Interpreter for accurate mathematical computation.
Figure 2: The development pipelines of Qwen2-Math and Qwen2.5-Math.
2
QWEN2.5-MATH PRE-TRAINING
In mathematical pre-training, our primary focus is on constructing a high-quality dataset rich in
mathematical content. This dataset encompasses a wide variety of sources, including math-related
web texts, code snippets, encyclopedias, exam questions, and synthetic mathematical data generated
by Qwen2 (Yang et al., 2024). The process of assembling this pre-training dataset involves several
key steps: data recall, deduplication, filtering, data synthesis, and optimization of the data mixture.
The final curated dataset, which forms the foundation of our pre-training, is termed the Qwen Math
Corpus v1. The Qwen2-Math base models, initialized with Qwen2-1.5B/7B/72B, undergo continuous
pre-training using the Qwen Math Corpus v1.
4

--- Page 5 ---

Prior to the construction of Qwen Math Corpus v1, we observe that the suboptimal performance of
general language models in mathematical reasoning stems from an insufficiency of mathematical data
during pre-training. The existing endeavors pre-training to large-scale, specialized LLMs focused on
mathematics (Shao et al., 2024; Ying et al., 2024; Lewkowycz et al., 2022a; Azerbayev et al., 2024)
have unequivocally demonstrated the value of extracting a considerable corpus of mathematical texts
from digital databases. Our initial strategy involves the recall of mathematical data from web sources,
such as Common Crawl, to escalate the quantity of data. Concretely, we train a FastText (Joulin et al.,
2016) classifier utilizing high-quality mathematical seed data and general text data. We leverage
iterative training with more math data each epoch to continuously enhance the performance of
the classifier. To recognize the missing mathematical-related data in the corpus pool, we leverage
meta-information, such as URLs, from the recalled data to expand the data pool for mathematical data
retrieval. Subsequently, deduplication techniques, including MinHash (Broder, 2000), are employed
to filter out similar mathematical documents.
Upon collecting a substantial volume of mathematical data, our focus shifts toward enhancing its
quality. For this, we implement a language-model-based filtering technique to further curate the
dataset. Specifically, we utilize the Qwen2-0.5B-Instruct model (Yang et al., 2024), augmented with
prompt engineering, to evaluate the quality of potential data entries. Data that receive higher scores,
indicating higher quality according to the language model, are prioritized for inclusion in the final
dataset. Beyond recalling a diverse set of mathematical documents and filtering out low-quality
data, we draw inspiration from previous efforts in generating synthetic mathematical data (Yue et al.,
2024; Zhou et al., 2024). We employ the Qwen2-72B-Instruct model to synthesize a large amount of
mathematical pre-training corpus. At this stage, the high-quality mathematical data already collected
are used as reference materials. Using the Qwen2-72B-Instruct model, we: (1) extract and refine
existing mathematical question-answer data from these references, and (2) directly generate new
mathematical question-answer pairs.
In the final phase, we conduct ablation studies on data mixture using a small math-specific language
model, Qwen2-Math-1.5B. Based on the findings, we construct the Qwen Math Corpus v1, which
comprises 700 billion tokens in total. We initialize the Qwen2-Math-1.5B/7B/72B pre-training with
intermediate checkpoints from the corresponding Qwen2-1.5B/7B/72B base models. These models
are then continuously pre-trained on Qwen Math Corpus v1 with a context length of 4K.
Following the training of the Qwen2-Math base models, we further upgrade them to Qwen2.5-Math
models through three primary avenues: (1) We utilize the Qwen2-Math-72B-Instruct model, further
post-trained with the steps described in Section 3, to synthesize additional high-quality mathematical
pre-training data. 2) We aggregate more high-quality mathematical data, especially in Chinese,
sourced from web documents, books, and code repositories across multiple recall cycles. As a result
of these efforts, we compile the Qwen Math Corpus v2 for Qwen2.5-Math-1.5B/7B/72B pre-training,
while maintaining a context length of 4K. Compared to Qwen Math Corpus v1, the total token count
of Qwen Math Corpus v2 escalates from 700B to over 1T. (3) Instead of initializing from the Qwen2
series, we leverage the Qwen2.5 series base models for parameter initialization, as they exhibit
enhanced capabilities in language understanding, code generation, and text reasoning. Qwen2.5-Math
models are continuously pre-trained on Qwen Math Corpus v2 under a math pre-training setup
similar to Qwen2-Math. Benefiting from the improvements in both the dataset and the base model,
Qwen2.5-Math models demonstrate further advancements in mathematical reasoning abilities beyond
Qwen2-Math.
3
QWEN2.5-MATH POST-TRAINING
After completing extensive mathematical pre-training, we proceed with post-training to further
augment the mathematical logical reasoning capabilities of Qwen-Math, specifically focusing on
Chain-of-Thought (CoT) and Tool-Integrated Reasoning (TIR). Our investigation is particularly
focused on two key challenges: (1) How to automatically generate a substantial volume of high-
quality and reliable CoT and TIR annotations, and (2) How to effectively leverage these annotations
for both Supervised Fine-Tuning and Reinforcement Learning.
5

--- Page 6 ---

3.1
SUPERVISED FINE-TUNING
We aim for Qwen-Math to excel in two core capabilities: solving math problems through step-by-step
natural language reasoning (Wei et al., 2022), and leveraging external tools (e.g., a Python interpreter)
to address complex mathematical or algorithmic reasoning tasks (Yue et al., 2023). We have con-
structed dedicated datasets for both Chain-of-Though (CoT) and Tool-integrated Reasoning (TIR)
and combined these datasets to train the model jointly. All models are trained for 3 epochs with a
sequence length of 4,096 tokens. For the 72B model, we use a batch size of 256 and a learning rate of
5 × 10−6. For the 1.5B and 7B models, we set the batch size to 128 and the learning rate to 2 × 10−5.
During training, the learning rate gradually decays to a final value of 7 × 10−7.
3.1.1
CHAIN-OF-THOUGHT DATA SYNTHESIS
Query Construction.
The chain-of-thought dataset comprises a wide-ranging collection of 580K
English and 500K Chinese mathematical problems, including both annotated and synthesized
items. The annotated problems are derived from well-established sources such as the training
set of GSM8K (Cobbe et al., 2021), MATH (Hendrycks et al., 2021b), and NuminaMath (LI et al.,
2024). In an effort to bolster the Chinese reasoning capabilities of Qwen2.5-Math, we have further
enriched the dataset with additional Chinese mathematical problems from exclusive K-12 problem
collections. The synthesized problems are evolved from the annotated ones using the MuggleMath
approach (Li et al., 2024b). To maintain a balanced distribution across varying levels of problem
complexity, we utilize a difficulty-scoring model to categorize our problem set effectively.
Response Construction.
We adopt an iterative approach that leverages rejection sampling, guided
by reward modeling and annotated answers, to incrementally enhance the quality of responses (Yuan
et al., 2023). At each iteration, the current best model is deployed to generate multiple reasoning
pathways for the given problems, expanding the pool of candidate solutions. For problems with
annotated answers, we select the top-k reasoning paths with correct final answers from the pool.
For synthesized problems lacking definitive answers, we implement a weighted majority voting
mechanism to deduce the most plausible correct reasoning paths. From these, we choose the top-k
pathways that receive the highest reward scores. In the development of Qwen2.5-Math, an additional
iteration is conducted using the Qwen2-Math-Instruct models to polish the quality of responses
further. The final CoT training set encompasses 2000K English samples and 500K Chinese samples.
3.1.2
TOOL-INTEGRATED REASONING DATA SYNTHESIS
It is important to recognize that while CoT prompting plays a crucial role in enhancing the reasoning
skills of large language models, it faces challenges in achieving computational accuracy and in
handling complex mathematical or algorithmic problems, such as finding the roots of quadratic
equations or computing the eigenvalues of matrices (Yue et al., 2023). To overcome these limitations
and improve the model’s proficiency in precise calculations, symbolic manipulation, and algorithmic
reasoning, we have developed a dataset that incorporates a tool-integrated reasoning format. This
innovative format enables the model to leverage a Python interpreter as an auxiliary resource in
reasoning tasks.
Query Construction.
The tool-integrated reasoning dataset consists of 190K annotated problems
and 205K synthesized problems. The annotated problems are sourced from the training sets of
established benchmarks, including GSM8K (Cobbe et al., 2021), MATH (Hendrycks et al., 2021b),
CollegeMath (Tang et al., 2024a), and NuminaMath (LI et al., 2024). The synthesized problems
are generated by employing techniques from MuggleMath (Li et al., 2024b) and DotaMath (Li
et al., 2024a) designed to facilitate query evolution within the GSM8K and MATH training sets.
Additionally, we have selected 75K annotated problems for translation into Chinese using the Qwen2-
72B model (Yang et al., 2024), aimed at enhancing the model’s reasoning capabilities in Chinese.
Response Construction.
For the annotated problems, we utilize an online Rejection Fine-Tuning
(RFT) (Yuan et al., 2023; Singh et al., 2024) approach to iteratively generate tool-integrated reasoning
paths whose final answers align with the reference answers. In each RFT iteration, we carry out
multiple nucleus samplings with the currently best model at various temperatures, increasing the
sample size for particularly challenging problems. After each iteration, to enhance data diversity,
we apply a deduplication process to the responses, and the resulting cleaned dataset is then used to
6

--- Page 7 ---

fine-tune the model for the next iteration. For the synthesized problems, we employ the optimal model
derived from the online RFT process to generate reasoning samples. Majority voting is employed
to select the most probable correct reasoning paths, which are subsequently incorporated into the
overall dataset.
3.2
REWARD MODEL TRAINING
To provide supervisory signals beyond merely the final answer during both the selection of supervised
fine-tuning data and the subsequent stages of reinforcement learning training, we have developed a
mathematical reward model for Qwen2-Math and Qwen2.5-Math, referred to as Qwen2-Math-RM
and Qwen2.5-Math-RM, respectively. These reward models are specifically designed to guide the
model throughout the training process by offering more granular feedback on the quality of reasoning
and intermediate steps, ultimately facilitating more robust model improvements.
3.2.1
DATA SYNTHESIS
In the development of Qwen2-Math-RM, we utilize 206K English mathematical problems, each
paired with 6 candidate responses sampled from an intermediate version of Qwen2-Math. For
Qwen2.5-Math-RM, we further enhance its support for both the Chinese language and TIR mode,
training it with a more diverse set of 361K English and 257K Chinese mathematical problems, with
each problem accompanied by 6 responses sampled from Qwen2.5-Math. This expansion ensures
that Qwen2.5-Math-RM is well-equipped to provide supervisory feedback across a broader range of
problem types and languages.
To establish the preference signals among the responses, we check the final answers of the responses
to determine their correctness. Responses with the correct answers are labeled as positive, while
those with incorrect answers are labeled as negative, thereby naturally creating a ranking relationship
among the responses. We then filter out any cases where all responses are either entirely correct or
entirely incorrect. However, to avoid the potential drawback of retaining only overly simplistic data,
we enrich the dataset with responses from various intermediate versions and models of different sizes.
This strategy ensures a more balanced distribution of query difficulty and maintains an even ratio of
positive to negative responses.
3.2.2
TRAINING STRATEGY
We initialize the reward model from the supervised fine-tuning model. In terms of architecture, we
replace the language modeling head originally used for next-token prediction with a scalar-value
head, consisting of two linear layers. As previously mentioned, each query in the reward model’s
training dataset is paired with 6 responses, comprising both positive and negative candidates. If there
are k positive responses, then the remaining 6 −k are negative. Following Ouyang et al. (2022), the
loss function for the reward model can therefore be formulated as follows:
Lrm(θ) = −
1
k × (6 −k)E(x,ypos,yneg)∼D [log (σ (rθ(x, ypos) −rθ(x, yneg)))] .
(1)
Here, rθ(x, y) denotes the output of the reward model, where x represents the problem and y is the
corresponding response. Rather than breaking these into multiple individual pairs and computing the
loss in a pairwise fashion, we adopt a listwise approach to compute the ranking loss directly over
valid pairs. This method enhances both training efficiency and effectiveness.
3.3
REINFORCEMENT LEARNING
Query Selection.
The queries for reinforcement learning training are selected from the reward
model’s training set. We leverage supervised fine-tuning models with varying sizes to resample 8
responses for each query, with each response classified as either correct or incorrect by comparing it
to the gold-standard answer. In the reinforcement learning stage, our primary goal is to ensure that
the model consistently produces correct answers for queries where a correct response is possible.
Therefore, we only retain queries for which 2 to 5 out of the 8 responses are correct. Queries with
fewer than 2 correct answers are excluded as they indicate that the current Math model lacks the
7

--- Page 8 ---

fundamental capability to learn from them. Likewise, queries with more than 5 correct responses are
omitted since the model already demonstrates competence in these cases and no further training is
necessary. In the end, we retain 66K queries for training.
Group Relative Policy Optimization (GRPO).
As introduced by Shao et al. (2024), GRPO is a
reinforcement learning method specifically designed for large language models, obviating the need
for additional value function approximation as in PPO. GRPO uses the average rewards of a group of
sampled outputs as a baseline to calculate the advantages of each output. The objective of GRPO is
defined as Eq. 2:
JGRP O(θ) = E[q∼P (Q),{oi}G
i=1∼πθold (O|q)]
1
G
G
X
i=1
1
|oi|
|oi|
X
t=1
{min[ πi,t
θ
πi,t
θold
ˆAi,t, clip( πi,t
θ
πi,t
θold
, 1 −ϵ, 1 + ϵ) ˆAi,t] −βDKL[πθ||πref]},
(2)
where πi,t = π(oi,t|q, oi,<t), G is the number of responses in a group. πref, πθ, and πold are
reference, training, and sampling models, respectively. q and {oi}G
i=1 are questions and generated
responses set in training. The advantage of each responses ˆAi is calculated by ˆAi = ri−mean(ri)
std(ri)
.
Then this sequence-level advantage is applied to each token in the response as ˆAi,t.
Reward Shaping.
We combine the rewards from both a rule-based verifier and the reward model to
shape the overall reward signal. The rule-based verifier extracts potential answers from each response
and compares them against the gold-standard answer.
Given that the output of the reward model is denoted as rm ∈R, and the sparse reward from the
rule-based verifier as rv ∈{0, 1}, the overall reward is calculated as follows:
r = σ(α · rm) + (rv −1),
(3)
where α is set as 0.5 in all of our experiments.
This shaping mechanism ensures that correct responses consistently receive higher overall rewards
compared to incorrect ones. Within each of the correct and incorrect groups, the responses are ranked
based on the scores from the reward models. ecially in hard samples.
Implementations.
Our experiments are implemented based on the open-source RLHF framework
ChatLearn5. The core implementation of our rule-based verifier is similar to the one used in our
evaluation6. All policy models in different parameter sizes are trained with the same reward model.
We sample 32 responses for each query. Considering a pair of queries and responses as a sample,
the number of samples in one episode is 4,096 and 2,048 for training 7B and 72B, respectively. All
models are trained with a 512 global batch size. The learning rates are 1 × 10−5 and 5 × 10−6 for
7B and 72B, respectively. And the KL coefficient for all training is 1 × 10−3. We mask all output
tokens the Python executor provides in reinforcement learning of tool-integrated reasoning.
4
DECONTAMINATION
Decontamination is critical to ensuring unbiased model performance evaluation. Following prior
work (Yang et al., 2024), we exclude potentially contaminated training samples using 13-gram
matching. To improve the accuracy of this matching process, we perform text normalization,
removing irrelevant punctuation and symbols. To further reduce false negatives, particularly for
common mathematical expressions, we introduce an additional criterion: the ratio of the longest
common subsequence must exceed 0.6 for a sample to be considered contaminated. For pre-training
data, we filter potentially contaminated samples against datasets such as GSM8K (Cobbe et al.,
2021) and MATH (Hendrycks et al., 2021b). When dealing with post-training data, including SFT
data, RM training data, and the RL query set, we exclude any potentially contaminated problems or
solutions across all reported evaluation datasets. These evaluation datasets include GSM8K (Cobbe
et al., 2021), MATH (Hendrycks et al., 2021b), Minerva Math (Lewkowycz et al., 2022b), Gaokao
2023 En (Liao et al., 2024), Olympiad Bench (He et al., 2024), College Math (Tang et al., 2024b),
5https://github.com/alibaba/ChatLearn
6https://github.com/QwenLM/Qwen2-Math/tree/main/evaluation
8

--- Page 9 ---

MMLU STEM (Hendrycks et al., 2021a), GaoKao (Zhong et al., 2024), CMATH (Wei et al., 2023),
CN Middle School 24, AIME 24, and AMC 23. During the analysis of contaminated samples, we
identify that some existing training datasets (e.g., the MATH training dataset) contain a significant
proportion of problems that share highly similar concepts or structures with those found in test
datasets. Although these variations are not exact duplicates, they could potentially compromise the
integrity of our evaluation. Therefore, we continue to exclude such samples from the training corpora.
Table 1 provides examples of similar problems identified across the training and test sets.
Problems from MATH train (filtered):
Problems from MATH test:
What is the remainder when 1 + 2 + 3 + 4 +
· · · + 9 + 10 is divided by 8?
What is the remainder when 1 + 2 + 3 + 4 +
· · · + 9 + 10 is divided by 9?
For how many integer values of n between 1
and 1000 inclusive does the decimal represen-
tation of
n
1400 terminate?
For how many integer values of n between 1
and 1000 inclusive does the decimal represen-
tation of
n
1375 terminate?
Krista put 1 cent into her new bank on a Sun-
day morning. On Monday she put 2 cents into
her bank. On Tuesday she put 4 cents into her
bank, and she continued to double the amount
of money she put into her bank each day for
two weeks. On what day of the week did the
total amount of money in her bank first ex-
ceed $2?
Krista put 1 cent into her new bank on a Sun-
day morning. On Monday she put 2 cents into
her bank. On Tuesday she put 4 cents into her
bank, and she continued to double the amount
of money she put into her bank each day for
two weeks. On what day of the week did the
total amount of money in her bank first ex-
ceed $5?
Table 1: Examples of filtered samples in the MATH training set with similar samples in the test set.
5
EVALUATION
5.1
BASE MODELS
We evaluate our Qwen2-Math and Qwen2.5-Math base models on three widely used English
math benchmarks GSM8K (Cobbe et al., 2021), MATH (Hendrycks et al., 2021b), and MMLU-
STEM (Hendrycks et al., 2021a). In addition, we also evaluate three Chinese math benchmarks
CMATH (Wei et al., 2023), GaoKao Math Cloze (Zhong et al., 2024), and GaoKao Math QA (Zhong
et al., 2024). All evaluations are tested with few-shot chain-of-thought prompting. The prompts of
these benchmarks are shown in Appendix B. For general models, we report the results on LLama-3.1-
8B/70B/405B (AI@Meta, 2024) and Qwen2-1.5B/7B/72B (Yang et al., 2024). For specific models,
DeepSeekMath-Base-7B (Shao et al., 2024), DeepSeek-Coder-V2-Lite-Base (Zhu et al., 2024), and
Intermln2-Math-Base-20B (Ying et al., 2024) are used as baselines.
The results are shown in Table 2. We can see that the smallest model of the Qwen2.5-Math series,
Qwen2.5-Math-1.5B, outperforms all specific baselines on GSM8K, MATH, CMATH, GaoKao Math
Cloze, and Gaokao Math QA. Furthermore, the medium-size model, Qwen2.5-Math-7B, obtains
91.6 and 55.4 scores on GSM8K and MATH, which outperforms Qwen2-72B with 89.5 and 51.1,
and Llama-3.1-405B with 89.0 and 53.8. Our flagship Qwen2.5-Math-72B achieves new SOTA
on MATH, CMATH, Gaokao Math Cloze, and Gaokao Math QA, which obtains 66.8 on MATH.
Compared to Qwen2-Math-1.5B/7B/72B, Qwen2.5-Math-1.5B/7B/72B have achieved significant
improvements on all benchmarks. For example, Qwen2.5-Math-1.5B/7B/72B obtains 5.4, 5.0, 6.3
scores improvement on MATH, and 3.4, 12.2, 19.8 scores improvement on Gaokao Math QA, which
demonstrates the effectiveness of our Qwen Math corpus v2.
5.2
INSTRUCTION MODELS
We evaluate Qwen2-Math-Instruct on mathematical benchmarks in both English and Chinese. In
addition to the widely-used benchmarks, such as GSM8K (Cobbe et al., 2021) and MATH (Hendrycks
et al., 2021b), we also involve more exams that are more challenging to fully inspect the capabilities
of Qwen2-Math-Instruct and Qwen2.5-Math-Instruct, such as OlympiadBench (He et al., 2024),
9

--- Page 10 ---

MODEL
BENCHMARK
EN
ZH
GSM8K
MATH
MMLU
STEM
CMATH
GaoKao
Math Cloze
GaoKao
Math QA
8-shot
4-shot
4-shot
6-shot
5-shot
4-shot
General Model
Llama-3.1-8B
56.7
20.3
53.1
51.5
8.5
28.5
Llama-3.1-70B
85.5
41.4
78.1
75.5
11.9
43.3
Llama-3.1-405B
89.0
53.8
-
-
-
-
Qwen2-1.5B
58.5
21.7
44.8
55.6
12.7
35.6
Qwen2-7B
79.9
44.2
67.6
76.7
37.3
51.6
Qwen2-72B
89.5
51.1
79.9
85.4
55.9
72.6
Specific Model
DeepSeekMath-Base-7B
64.2
36.2
56.5
71.7
20.3
40.7
DeepSeek-Coder-V2-Lite-Base
68.3
38.1
59.5
77.8
25.4
51.3
Internlm2-Math-Base-20B
68.2
30.4
63.0
65.9
16.9
40.2
Qwen2-Math-1.5B
71.3
44.4
50.4
79.6
37.3
50.7
Qwen2-Math-7B
80.4
50.4
65.7
83.2
48.3
57.3
Qwen2-Math-72B
89.1
60.5
79.1
86.4
72.9
69.5
Qwen2.5-Math-1.5B
76.8
49.8
51.3
83.0
47.5
54.1
Qwen2.5-Math-7B
91.6
55.4
67.8
85.0
57.6
69.5
Qwen2.5-Math-72B
90.8
66.8
82.8
89.7
72.9
86.3
Table 2: The results of Qwen2.5-Math and other base models on English and Chinese mathematical
benchmarks. Models are evaluated with few-shot chain-of-thought prompting.
Figure 3: The Performance of Qwen2.5-Math-1.5/7/72B-Instruct on MATH by CoT compared to
models of the same size.
10

--- Page 11 ---

CollegeMath (Tang et al., 2024a), GaoKao 2023 En (Liao et al., 2024), AIME2024 7, and AMC2023 8.
For Chinese mathematical benchmarks, we use CMATH (Wei et al., 2023), GaoKao (including
GaoKao I/II 2024 9, GaoKao-Math-QA (Zhong et al., 2024), GaoKao-Math-Cloze (Zhong et al.,
2024) and 91 collected GaoKao problems in 2024), and CN Middle School 24 (101 collected problems
from China High School Entrance Examination in 2024). We report greedy, Maj@8, and RM@8
performance on all benchmarks in the zero-shot setting, except for the multi-choice benchmarks
(including MMLU STEM and multiple-choice problems in GaoKao and CN Middle School 24) with
a 5-shot setting.
We take Qwen2-1.5/7/72B-Instruct (Yang et al., 2024), Llama-3.1-8/70B-instruct (AI@Meta, 2024),
and GPT4o-2024-08-06 (OpenAI, 2024) as general model baselines. Besides, DeepSeekMath-7B-
RL (Shao et al., 2024), DeepSeek-Coder-V2-Lite-Instruct (Zhu et al., 2024), Interlm2-math-plus-
7B/20B/mixtral8x7B (Ying et al., 2024), Mathstral-7B-v0.1 (Mistral-AI, 2024), NuminaMath-7/72B-
CoT (LI et al., 2024) are taken as specific-model baselines.
Model
Benchmark
EN
GSM8K
MATH
Minerva
Math
GaoKao
2023 En
Olympiad
Bench
College
Math
MMLU
STEM
Avg.
CHAIN-OF-THOUGHT
GPT-4o-2024-08-06
92.9
81.1
36.8
67.5
43.3
48.5
64.2
62.0
DeepSeekMath-7B-RL
88.2
52.4
20.6
43.6
19.0
37.5
64.8
46.6
DeepSeek-Coder-V2-Lite-Instruct
87.6
61.0
29.4
56.1
26.4
39.8
68.6
52.7
Internlm2-math-plus-7B
84.0
54.4
17.3
50.1
18.8
36.2
55.2
45.1
Internlm2-math-plus-20B
87.9
56.5
20.2
51.9
23.1
37.5
63.5
48.7
Internlm2-math-plus-mixtral8x7B
92.1
59.4
26.8
49.6
25.0
37.5
71.9
51.8
Mathstral-7B-v0.1
84.9
56.6
16.2
46.0
21.5
33.7
64.0
46.1
NuminaMath-7B-CoT
75.4
55.2
19.1
47.5
19.9
36.9
60.8
45.0
NuminaMath-72B-CoT
90.8
66.7
25.0
58.4
32.6
39.7
64.5
54.0
Llama-3.1-8B-Instruct
76.6
47.2
21.7
38.4
15.4
33.8
60.5
41.9
Llama-3.1-70B-Instruct
94.1
65.7
34.2
54.0
27.7
42.5
80.4
56.9
Qwen2-1.5B-Instruct
64.1
25.1
5.5
19.7
4.1
10.4
46.2
25.0
Qwen2-7B-Instruct
85.7
52.9
19.5
36.4
21.3
24.5
68.2
44.1
Qwen2-72B-Instruct
93.2
69.0
31.6
58.7
33.2
43.2
84.4
59.0
Qwen2-Math-1.5B-Instruct
84.2
69.4
29.4
59.7
31.3
44.2
54.9
53.3
88.6maj@8
75.3maj@8
32.0maj@8
63.9maj@8
37.6maj@8
46.6maj@8
59.5maj@8
57.6maj@8
92.7rm@8
79.9rm@8
36.4rm@8
68.8rm@8
43.4rm@8
46.8rm@8
74.5rm@8
63.2rm@8
Qwen2-Math-7B-Instruct
89.9
75.1
34.6
62.1
38.2
45.9
63.8
58.5
93.1maj@8
80.2maj@8
37.1maj@8
68.1maj@8
43.7maj@8
47.8maj@8
73.2maj@8
63.3maj@8
95.1rm@8
83.3rm@8
39.7rm@8
71.9rm@8
47.6rm@8
47.9rm@8
78.2rm@8
66.2rm@8
Qwen2-Math-72B-Instruct
96.7
84.0
40.1
68.3
43.0
47.9
79.9
65.7
97.0maj@8
86.8maj@8
45.2maj@8
71.4maj@8
48.9maj@8
48.7maj@8
83.1maj@8
68.7maj@8
96.7rm@8
86.7rm@8
47.1rm@8
72.5rm@8
52.4rm@8
48.2rm@8
82.2rm@8
69.4rm@8
Qwen2.5-Math-1.5B-Instruct
84.8
75.8
29.4
65.5
38.1
47.7
57.5
56.9
89.5maj@8
80.3maj@8
32.0maj@8
68.8maj@8
43.9maj@8
48.9maj@8
60.7maj@8
60.6maj@8
94.1rm@8
83.9rm@8
37.5rm@8
73.0rm@8
47.3rm@8
50.2rm@8
65.2rm@8
64.5rm@8
Qwen2.5-Math-7B-Instruct
95.2
83.6
37.1
66.8
41.6
46.8
71.9
62.9
96.7maj@8
87.1maj@8
41.2maj@8
72.5maj@8
44.4maj@8
47.8maj@8
73.8maj@8
66.2maj@8
97.9rm@8
88.5rm@8
42.6rm@8
75.1rm@8
49.9rm@8
49.6rm@8
78.7rm@8
68.9rm@8
Qwen2.5-Math-72B-Instruct
95.9
85.9
44.1
71.9
49.0
49.5
80.8
68.2
96.0maj@8
88.6maj@8
47.8maj@8
73.8maj@8
50.1maj@8
50.2maj@8
84.9maj@8
70.2maj@8
96.4rm@8
89.8rm@8
47.4rm@8
76.9rm@8
54.5rm@8
50.6rm@8
80.1rm@8
70.8rm@8
TOOL-INTEGRATED REASONING
Qwen2.5-Math-1.5B-Instruct
83.7
79.9
33.5
67.8
49.2
54.8
56.9
60.8
90.0maj@8
85.3maj@8
35.3maj@8
71.9maj@8
54.3maj@8
56.3maj@8
60.4maj@8
64.8maj@8
93.3rm@8
88.9rm@8
39.7rm@8
78.7rm@8
59.3rm@8
58.8rm@8
76.6rm@8
70.8rm@8
Qwen2.5-Math-7B-Instruct
94.6
85.2
39.0
71.4
55.6
56.0
70.1
67.4
96.4maj@8
89.9maj@8
40.8maj@8
76.4maj@8
58.6maj@8
57.2maj@8
71.3maj@8
70.1maj@8
97.6rm@8
91.4rm@8
42.3rm@8
80.8rm@8
63.1rm@8
58.7rm@8
82.2rm@8
73.7rm@8
Qwen2.5-Math-72B-Instruct
95.8
88.1
48.2
75.3
60.6
57.7
82.3
72.6
96.7maj@8
91.8maj@8
48.2maj@8
83.1maj@8
64.5maj@8
58.3maj@8
85.0maj@8
75.4maj@8
96.4rm@8
92.9rm@8
49.3rm@8
83.4rm@8
65.9rm@8
59.7rm@8
90.0rm@8
76.8rm@8
Table 3: The results of Qwen2.5-Math-Instruct and other instruct models on English benchmarks. For
CoT, we report few-shot pass@1 performance on MMLU(STEM) and zero-shot pass@1 performance
on other benchmarks. For PoT, all benchmarks are evaluated in the zero-shot setting. Except for the
pass@1 scores, we also provide the Qwen2-Math and Qwen2.5-Math performance with majority
voting and reward model best-of-N among 8 sampled responses. Best pass@1 performance in CoT
and TIR are marked in bold.
Let us first analyze the performance on English benchmarks. As shown in Table 3, we can draw the
following conclusions: (1) Qwen2-Math-Instruct has demonstrated exceptional capabilities. The 1.5B
7https://huggingface.co/datasets/AI-MO/aimo-validation-aime
8https://huggingface.co/datasets/AI-MO/aimo-validation-amc
9https://github.com/llmeval/Llmeval-Gaokao2024-Math
11

--- Page 12 ---

Model
Benchmark
ZH
GaoKao
CMATH
CN Middle
School 24
Avg.
CHAIN-OF-THOUGHT
GPT-4o-2024-08-06
42.6
92.5
60.4
65.2
DeepSeekMath-7B-RL
33.6
86.7
67.3
62.5
DeepSeek-Coder-V2-Lite-Instruct
51.1
89.8
66.3
69.1
Internlm2-math-plus-7B
34.5
82.7
32.7
50.0
Internlm2-math-plus-20B
36.1
81.3
33.7
50.4
Internlm2-math-plus-mixtral8x7B
37.3
85.7
39.6
54.2
Mathstral-7B-v0.1
31.6
76.7
42.6
50.3
NuminaMath-7B-CoT
36.4
78.2
60.4
58.3
NuminaMath-72B-CoT
47.9
87.3
75.2
70.1
Llama-3.1-8B-Instruct
30.4
64.8
43.6
46.3
Llama-3.1-70B-Instruct
41.7
86.7
59.4
62.6
Qwen2-1.5B-Instruct
17.0
65.5
31.7
38.1
Qwen2-7B-Instruct
35.1
83.5
54.5
57.7
Qwen2-72B-Instruct
54.6
92.2
74.3
73.7
Qwen2-Math-1.5B-Instruct
46.5
84.2
66.3
65.7
50.1maj@8
88.0maj@8
70.3maj@8
69.5maj@8
58.2rm@8
92.2rm@8
75.2rm@8
75.2rm@8
Qwen2-Math-7B-Instruct
49.0
90.0
69.3
69.4
59.5maj@8
91.7maj@8
72.3maj@8
74.5 maj@8
62.7rm@8
94.0rm@8
78.2rm@8
78.3rm@8
Qwen2-Math-72B-Instruct
59.8
92.8
77.2
76.6
61.7maj@8
93.2maj@8
79.2maj@8
78.0 maj@8
67.7rm@8
94.2rm@8
78.2rm@8
80.0 rm@8
Qwen2.5-Math-1.5B-Instruct
62.4
89.7
76.2
76.1
66.4maj@8
91.7maj@8
77.2maj@8
78.4 maj@8
67.5rm@8
94.0rm@8
80.2rm@8
80.6 rm@8
Qwen2.5-Math-7B-Instruct
66.3
91.8
73.3
77.1
68.1maj@8
92.7maj@8
78.2maj@8
79.7 maj@8
72.2rm@8
94.5rm@8
81.2rm@8
82.6 rm@8
Qwen2.5-Math-72B-Instruct
68.6
94.3
79.2
82.7
75.0maj@8
95.3maj@8
79.2maj@8
83.2 maj@8
76.5rm@8
95.7rm@8
80.2rm@8
84.1 rm@8
TOOL-INTEGRATED REASONING
Qwen2.5-Math-1.5B-Instruct
59.6
89.3
71.3
73.4
68.3maj@8
90.8maj@8
78.2maj@8
79.1 maj@8
64.1rm@8
93.2rm@8
78.2rm@8
78.5 rm@8
Qwen2.5-Math-7B-Instruct
62.9
90.5
75.2
76.2
70.8maj@8
92.0maj@8
78.2maj@8
80.3 maj@8
72.9rm@8
94.2rm@8
80.2rm@8
82.4 rm@8
Qwen2.5-Math-72B-Instruct
68.5
93.0
78.2
79.9
72.0maj@8
93.5maj@8
78.2maj@8
81.2 maj@8
75.4rm@8
93.8rm@8
80.2rm@8
83.1rm@8
Table 4: The results of Qwen2.5-Math-Instruct and other instruct models on Chinese benchmarks.
12

--- Page 13 ---

model achieves an average score higher than any sub-70B model currently available. The 7B model
performs on par with Qwen2-72B-Instruct, and Qwen2-Math-72B-Instruct surpasses the latest version
of GPT-4o by 3.7 points. (2) The performance of Qwen2.5-Math-Instruct represents a further upgrade
over Qwen2-Math-Instruct. In the traditional CoT mode, the 1.5B and 7B Qwen2.5-Math-Instruct
models achieve results comparable to the 7B and 72B Qwen2-Math-Instruct models, respectively,
demonstrating a cross-scale improvement. Qwen2.5-Math-72B-Instruct achieves an average score
of 2.5 points ahead of the current best model and is 6.2 points higher than GPT-4o. This shows that
our improvements in training data and strategy can provide an alternative pathway for performance
enhancements beyond simply increasing model size. (3) The TIR mode introduced in Qwen2.5-
Math-Instruct is highly effective. With the assistance of a Python Interpreter, the 7B model already
matches the performance of Qwen2.5-Math-72B-Instruct. This indicates that precise mathematical
calculations via external tools can significantly aid LLM reasoning. In many cases, the reasoning
process of LLMs is sound, but computational errors can arise. (4) Our RM performs exceptionally
well. Across almost all benchmarks and models, RM@N scores are substantially better than Maj@N
scores. This provides a reliable performance oracle for improving reinforcement learning strategies
in the future. It is likely that we may soon see models with greedy decoding exceeding 90 points on
MATH, even for the 7B scale.
0.0
10.0
20.0
30.0
40.0
50.0
60.0
70.0
80.0
90.0
100.0
MATH
Minerva Math
GaoKao 2023 EN
Olympiad Bench
College Math
Qwen2.5-Math-1.5B-Instruct COT
Qwen2.5-Math-1.5B-Instruct TIR
Qwen2.5-Math-7B-Instruct COT
Qwen2.5-Math-7B-Instruct TIR
Qwen2.5-Math-72B-Instruct COT
Qwen2.5-Math-72B-Instruct TIR
Figure 4: The Performance of Qwen2.5-Math-1.5/7/72B-Instruct by using TIR compared to using
CoT. We use blue color to represent the performance of TIR, and orange to represent the performance
of CoT. It can be seen that TIR can achieve further performance improvement compared to CoT.
Let’s now shift our attention to Table 4 to analyze the performance on the Chinese benchmarks. For
Qwen2-Math-Instruct, no specifically Chinese mathematics-related training data was incorporated.
However, thanks to Qwen2’s strong language transfer capabilities, the Qwen2-Math-1.5B-Instruct
model has already surpassed GPT-4o in terms of the average Chinese score. During the development
of Qwen2.5-Math-Instruct, we intentionally integrated Chinese-specific math post-training data,
resulting in substantial improvements in Chinese performance. The Qwen2.5-Math-1.5B-Instruct
model achieves results similar to Qwen2-Math-72B-Instruct, while Qwen2.5-Math-72B-Instruct
outperforms GPT-4o by an impressive 17.5 points. Our RM also exhibits strong performance in
Chinese benchmarks. Similar to our results in English, RM@N scores consistently surpass Maj@N
scores, highlighting its effectiveness. However, one key difference from the English results is that the
TIR mode in Chinese does not show a significant performance advantage over the CoT mode. We
will continue to investigate this aspect in future research.
Lastly, we intend to evaluate the model’s ability to solve complex mathematical problems on highly
challenging competition benchmarks such as AIME 2024 and AMC 2023. As shown in Table 5, we
observe a significant improvement in performance on difficult problems with Qwen2.5-Math-Instruct
compared to Qwen2-Math-Instruct. With the support of the RM, Qwen2.5-Math-1.5B-Instruct, using
the RM@256 in CoT mode, successfully solves 29 out of 40 problems on AMC 2023, significantly
13

--- Page 14 ---

outperforming NuminaMath-72B CoT. Moreover, Qwen2.5-Math-72B-Instruct nearly achieves a
perfect score in TIR mode, solving almost all the problems. We attribute this impressive performance
to the extensive amounts of challenging mathematical data collected and synthesized during pre-
training. On the extremely difficult AIME 2024 benchmark, Claude3 Opus, GPT-4 Turbo, and Gemini
1.5 Pro manage to solve only 1 or 2 questions out of 30. In contrast, Qwen2.5-Math-72B-Instruct
solves 9 problems in Greedy decoding CoT mode and 12 problems in TIR mode. With the help of
the RM, Qwen2.5-Math-7B-Instruct could even solve up to 21 problems, further demonstrating the
outstanding mathematical problem-solving ability of Qwen2.5-Math-Instruct.
MODEL
AIME24
AMC23
CHAIN-OF-THOUGHT
Claude 3 Opus
2/30
-
GPT-4 Turbo
1/30
-
Gemini 1.5 Pro
2/30
-
Gemini Math-Specialized 1.5 Pro
7/30
-
8/30rm@256
-
NuminaMath-72B CoT
1/30
21/40
3/30maj@64
24/40maj@64
Qwen2-Math-1.5B-Instruct
1/30
18/40
5/30rm@256
25/40rm@256
Qwen2-Math-7B-Instruct
4/30
25/40
6/30rm@256
29/40rm@256
Qwen2-Math-72B-Instruct
6/30
24/40
8/30maj@64
29/40maj@64
9/30rm@64
29/40rm@64
11/30rm@256
28/40rm@256
Qwen2.5-Math-1.5B-Instruct
3/30
24/40
10/30rm@256
29/40rm@256
Qwen2.5-Math-7B-Instruct
5/30
25/40
10/30rm@256
30/40rm@256
Qwen2.5-Math-72B-Instruct
9/30
28/40
9/30maj@64
30/40maj@64
13/30rm@64
29/40rm@64
13/30rm@256
30/40rm@256
TOOL-INTEGRATED REASONING
Qwen2.5-Math-1.5B-Instruct
7/30
20/40
9/30maj@64
31/40maj@64
18/30rm@64
36/40rm@64
9/30maj@256
32/40maj@256
19/30rm@256
36/40rm@256
Qwen2.5-Math-7B-Instruct
6/30
27/40
13/30maj@64
31/40maj@64
21/30rm@64
33/40rm@64
14/30maj@256
31/40maj@256
21/30rm@256
35/40rm@256
Qwen2.5-Math-72B-Instruct
12/30
28/40
14/30maj@64
36/40maj@64
18/30rm@64
37/40rm@64
16/30maj@256
36/40maj@256
19/30rm@256
39/40rm@256
Table 5: The results on the mathematics competition problems.
6
CONCLUSION
In this report, we introduce Qwen2.5-Math, which features several key technical highlights: (1)
extensive use of synthesized mathematical data from Qwen2-Math during the pre-training phase, (2)
iterative generation of fine-tuning data and reinforcement training guided by the reward model during
the post-training and inference phase and (3) support for bilingual (English and Chinese) queries,
14

--- Page 15 ---

along with chain-of-thought and tool-integrated reasoning capabilities. As a result, Qwen2.5-Math
represents the most advanced open-source math model series to date. The Qwen2.5-Math-1.5B-
Instruct model already surpasses most previous 70B math models, while the Qwen2.5-Math-7B-
Instruct matches the performance of Qwen2-Math-72B-Instruct. Our flagship model, Qwen2.5-Math-
7B-Instruct, outperforms Qwen2-Math-72B-Instruct with an average score increase of 4.4 points
across 7 datasets. We hope that the advances we’ve made with specialized models like Qwen2.5-Math
will continue to strengthen the overall capabilities of the Qwen model and bring us closer to achieving
artificial general intelligence.
ACKNOWLEDGEMENTS
We sincerely appreciate the support from other members of the Qwen team. We would also like
to thank the ChatLearn team from PAI, Alibaba, for their infrastructure support of large-scale
reinforcement learning.
15

--- Page 16 ---

REFERENCES
AI@Meta. Llama 3 model card, 2024. URL https://github.com/meta-llama/llama3/
blob/main/MODEL_CARD.md.
Zhangir Azerbayev, Hailey Schoelkopf, Keiran Paster, Marco Dos Santos, Stephen Marcus McAleer,
Albert Q. Jiang, Jia Deng, Stella Biderman, and Sean Welleck. Llemma: An open language model
for mathematics. In ICLR. OpenReview.net, 2024.
Andrei Z. Broder. Identifying and filtering near-duplicate documents. In CPM, volume 1848 of
Lecture Notes in Computer Science, pp. 1–10. Springer, 2000.
Boxi Cao, Keming Lu, Xinyu Lu, Jiawei Chen, Mengjie Ren, Hao Xiang, Peilin Liu, Yaojie Lu, Ben
He, Xianpei Han, Le Sun, Hongyu Lin, and Bowen Yu. Towards scalable automated alignment of
LLMs: A survey. CoRR, abs/2406.01252, 2024.
Karl Cobbe, Vineet Kosaraju, Mohammad Bavarian, Mark Chen, Heewoo Jun, Lukasz Kaiser,
Matthias Plappert, Jerry Tworek, Jacob Hilton, Reiichiro Nakano, Christopher Hesse, and John
Schulman. Training verifiers to solve math word problems. CoRR, abs/2110.14168, 2021.
Chaoqun He, Renjie Luo, Yuzhuo Bai, Shengding Hu, Zhen Leng Thai, Junhao Shen, Jinyi Hu,
Xu Han, Yujie Huang, Yuxiang Zhang, Jie Liu, Lei Qi, Zhiyuan Liu, and Maosong Sun. Olympiad-
bench: A challenging benchmark for promoting AGI with olympiad-level bilingual multimodal
scientific problems. In ACL (1), pp. 3828–3850. Association for Computational Linguistics, 2024.
Dan Hendrycks, Collin Burns, Steven Basart, Andy Zou, Mantas Mazeika, Dawn Song, and Jacob
Steinhardt. Measuring massive multitask language understanding. In ICLR. OpenReview.net,
2021a.
Dan Hendrycks, Collin Burns, Saurav Kadavath, Akul Arora, Steven Basart, Eric Tang, Dawn Song,
and Jacob Steinhardt. Measuring mathematical problem solving with the MATH dataset. In
NeurIPS Datasets and Benchmarks, 2021b.
Armand Joulin, Edouard Grave, Piotr Bojanowski, Matthijs Douze, Herv´e J´egou, and Tom´as Mikolov.
Fasttext.zip: Compressing text classification models. CoRR, abs/1612.03651, 2016.
Aitor Lewkowycz, Anders Andreassen, David Dohan, Ethan Dyer, Henryk Michalewski, Vinay V.
Ramasesh, Ambrose Slone, Cem Anil, Imanol Schlag, Theo Gutman-Solo, Yuhuai Wu, Behnam
Neyshabur, Guy Gur-Ari, and Vedant Misra. Solving quantitative reasoning problems with
language models. In NeurIPS, 2022a.
Aitor Lewkowycz, Anders Andreassen, David Dohan, Ethan Dyer, Henryk Michalewski, Vinay V.
Ramasesh, Ambrose Slone, Cem Anil, Imanol Schlag, Theo Gutman-Solo, Yuhuai Wu, Behnam
Neyshabur, Guy Gur-Ari, and Vedant Misra. Solving quantitative reasoning problems with
language models. In Sanmi Koyejo, S. Mohamed, A. Agarwal, Danielle Belgrave, K. Cho, and
A. Oh (eds.), Advances in Neural Information Processing Systems 35: Annual Conference on
Neural Information Processing Systems 2022, NeurIPS 2022, New Orleans, LA, USA, November
28 - December 9, 2022, 2022b.
Chengpeng Li, Guanting Dong, Mingfeng Xue, Ru Peng, Xiang Wang, and Dayiheng Liu. Dotamath:
Decomposition of thought with code assistance and self-correction for mathematical reasoning,
2024a. URL https://arxiv.org/abs/2407.04078.
Chengpeng Li, Zheng Yuan, Hongyi Yuan, Guanting Dong, Keming Lu, Jiancan Wu, Chuanqi Tan,
Xiang Wang, and Chang Zhou. Mugglemath: Assessing the impact of query and response augmen-
tation on math reasoning. In Lun-Wei Ku, Andre Martins, and Vivek Srikumar (eds.), Proceedings
of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long
Papers), ACL 2024, Bangkok, Thailand, August 11-16, 2024, pp. 10230–10258. Association for
Computational Linguistics, 2024b.
Jia LI, Edward Beeching, Lewis Tunstall, Ben Lipkin, Roman Soletskyi, Shengyi Costa Huang,
Kashif Rasul, Longhui Yu, Albert Jiang, Ziju Shen, Zihan Qin, Bin Dong, Li Zhou, Yann Fleureau,
Guillaume Lample, and Stanislas Polu. Numinamath. [https://github.com/project-
numina/aimo-progress-prize](https://github.com/project-numina/
aimo-progress-prize/blob/main/report/numina_dataset.pdf), 2024.
16

--- Page 17 ---

Minpeng Liao, Chengxi Li, Wei Luo, Jing Wu, and Kai Fan. MARIO: math reasoning with code
interpreter output - A reproducible pipeline. In Lun-Wei Ku, Andre Martins, and Vivek Srikumar
(eds.), Findings of the Association for Computational Linguistics, ACL 2024, Bangkok, Thailand
and virtual meeting, August 11-16, 2024, pp. 905–924. Association for Computational Linguistics,
2024.
Team Mistral-AI. Mathstral. https://mistral.ai/news/mathstral/, 2024.
OpenAI. Hello GPT-4o, 2024. URL https://openai.com/index/hello-gpt-4o/.
Long Ouyang, Jeffrey Wu, Xu Jiang, Diogo Almeida, Carroll Wainwright, Pamela Mishkin, Chong
Zhang, Sandhini Agarwal, Katarina Slama, Alex Ray, John Schulman, Jacob Hilton, Fraser
Kelton, Luke Miller, Maddie Simens, Amanda Askell, Peter Welinder, Paul F Christiano, Jan
Leike, and Ryan Lowe.
Training language models to follow instructions with human feed-
back. In S. Koyejo, S. Mohamed, A. Agarwal, D. Belgrave, K. Cho, and A. Oh (eds.), Ad-
vances in Neural Information Processing Systems, volume 35, pp. 27730–27744. Curran Asso-
ciates, Inc., 2022. URL https://proceedings.neurips.cc/paper_files/paper/
2022/file/b1efde53be364a73914f58805a001731-Paper-Conference.pdf.
Team Qwen. Introducing qwen2-math. https://qwenlm.github.io/blog/qwen2-math/, 2024.
Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, Junxiao Song, Mingchuan Zhang, Y. K. Li,
Y. Wu, and Daya Guo. Deepseekmath: Pushing the limits of mathematical reasoning in open
language models. CoRR, abs/2402.03300, 2024.
Avi Singh, John D. Co-Reyes, Rishabh Agarwal, Ankesh Anand, Piyush Patil, Xavier Garcia, Peter J.
Liu, James Harrison, Jaehoon Lee, Kelvin Xu, Aaron Parisi, Abhishek Kumar, Alex Alemi,
Alex Rizkowsky, Azade Nova, Ben Adlam, Bernd Bohnet, Gamaleldin Elsayed, Hanie Sedghi,
Igor Mordatch, Isabelle Simpson, Izzeddin Gur, Jasper Snoek, Jeffrey Pennington, Jiri Hron,
Kathleen Kenealy, Kevin Swersky, Kshiteej Mahajan, Laura Culp, Lechao Xiao, Maxwell L.
Bileschi, Noah Constant, Roman Novak, Rosanne Liu, Tris Warkentin, Yundi Qian, Yamini
Bansal, Ethan Dyer, Behnam Neyshabur, Jascha Sohl-Dickstein, and Noah Fiedel. Beyond human
data: Scaling self-training for problem-solving with language models, 2024. URL https:
//arxiv.org/abs/2312.06585.
Zhengyang Tang, Xingxing Zhang, Benyou Wang, and Furu Wei. Mathscale: Scaling instruction
tuning for mathematical reasoning. In ICML. OpenReview.net, 2024a.
Zhengyang Tang, Xingxing Zhang, Benyou Wang, and Furu Wei. Mathscale: Scaling instruc-
tion tuning for mathematical reasoning. In Forty-first International Conference on Machine
Learning, ICML 2024, Vienna, Austria, July 21-27, 2024. OpenReview.net, 2024b.
URL
https://openreview.net/forum?id=Kjww7ZN47M.
Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Fei Xia, Ed Chi, Quoc V Le, Denny
Zhou, et al. Chain-of-thought prompting elicits reasoning in large language models. Advances in
Neural Information Processing Systems, 35:24824–24837, 2022.
Tianwen Wei, Jian Luan, Wei Liu, Shuang Dong, and Bin Wang. CMATH: can your language model
pass chinese elementary school math test? CoRR, abs/2306.16636, 2023.
An Yang, Baosong Yang, Binyuan Hui, Bo Zheng, Bowen Yu, Chang Zhou, Chengpeng Li,
Chengyuan Li, Dayiheng Liu, Fei Huang, Guanting Dong, Haoran Wei, Huan Lin, Jialong Tang,
Jialin Wang, Jian Yang, Jianhong Tu, Jianwei Zhang, Jianxin Ma, Jianxin Yang, Jin Xu, Jingren
Zhou, Jinze Bai, Jinzheng He, Junyang Lin, Kai Dang, Keming Lu, Keqin Chen, Kexin Yang,
Mei Li, Mingfeng Xue, Na Ni, Pei Zhang, Peng Wang, Ru Peng, Rui Men, Ruize Gao, Runji Lin,
Shijie Wang, Shuai Bai, Sinan Tan, Tianhang Zhu, Tianhao Li, Tianyu Liu, Wenbin Ge, Xiaodong
Deng, Xiaohuan Zhou, Xingzhang Ren, Xinyu Zhang, Xipin Wei, Xuancheng Ren, Xuejing Liu,
Yang Fan, Yang Yao, Yichang Zhang, Yu Wan, Yunfei Chu, Yuqiong Liu, Zeyu Cui, Zhenru Zhang,
Zhifang Guo, and Zhihao Fan. Qwen2 technical report. CoRR, abs/2407.10671, 2024.
Huaiyuan Ying, Shuo Zhang, Linyang Li, Zhejian Zhou, Yunfan Shao, Zhaoye Fei, Yichuan Ma,
Jiawei Hong, Kuikun Liu, Ziyi Wang, Yudong Wang, Zijian Wu, Shuaibin Li, Fengzhe Zhou,
17

--- Page 18 ---

Hongwei Liu, Songyang Zhang, Wenwei Zhang, Hang Yan, Xipeng Qiu, Jiayu Wang, Kai Chen,
and Dahua Lin. Internlm-math: Open math large language models toward verifiable reasoning.
CoRR, abs/2402.06332, 2024.
Zheng Yuan, Hongyi Yuan, Chengpeng Li, Guanting Dong, Keming Lu, Chuanqi Tan, Chang Zhou,
and Jingren Zhou. Scaling relationship on learning mathematical reasoning with large language
models, 2023.
Xiang Yue, Xingwei Qu, Ge Zhang, Yao Fu, Wenhao Huang, Huan Sun, Yu Su, and Wenhu Chen.
MAmmoTH: Building math generalist models through hybrid instruction tuning. arXiv preprint
arXiv:2309.05653, 2023.
Xiang Yue, Tuney Zheng, Ge Zhang, and Wenhu Chen. Mammoth2: Scaling instructions from the
web. CoRR, abs/2405.03548, 2024.
Xiaotian Zhang, Chunyang Li, Yi Zong, Zhengyu Ying, Liang He, and Xipeng Qiu. Evaluating the
performance of large language models on GAOKAO benchmark. CoRR, abs/2305.12474, 2023. doi:
10.48550/arXiv.2305.12474. URL https://doi.org/10.48550/arXiv.2305.12474.
Wanjun Zhong, Ruixiang Cui, Yiduo Guo, Yaobo Liang, Shuai Lu, Yanlin Wang, Amin Saied, Weizhu
Chen, and Nan Duan. Agieval: A human-centric benchmark for evaluating foundation models. In
NAACL-HLT (Findings), pp. 2299–2314. Association for Computational Linguistics, 2024.
Kun Zhou, Beichen Zhang, Jiapeng Wang, Zhipeng Chen, Wayne Xin Zhao, Jing Sha, Zhichao Sheng,
Shijin Wang, and Ji-Rong Wen. Jiuzhang3.0: Efficiently improving mathematical reasoning by
training small data synthesis models. CoRR, abs/2405.14365, 2024.
Qihao Zhu, Daya Guo, Zhihong Shao, Dejian Yang, Peiyi Wang, Runxin Xu, Y Wu, Yukun Li,
Huazuo Gao, Shirong Ma, et al. Deepseek-coder-v2: Breaking the barrier of closed-source models
in code intelligence. arXiv preprint arXiv:2406.11931, 2024.
18

--- Page 19 ---

A
CASE STUDY OF QWEN2-MATH ON OLYMPIAD-LEVEL PROBLEMS
A.1
NUMBER THEORY
Problem From IMO Shortlist 2002:
What is the smallest positive integer t such that there exist integers x1, x2, . . . , xt with
x3
1 + x3
2 + . . . + x3
t = 20022002 ?
Qwen2-Math-72B-Instruct Solution
To determine the smallest positive integer t such that there exist integers x1, x2, . . . , xt satisfying the
equation
x3
1 + x3
2 + · · · + x3
t = 20022002,
we start by analyzing the properties of cubes and their sums. We need to find the smallest t for which
the sum of t cubes equals 20022002.
First, we note that 2002 can be factored into prime factors:
2002 = 2 × 7 × 11 × 13.
Thus,
20022002 = (2 × 7 × 11 × 13)2002 = 22002 × 72002 × 112002 × 132002.
Next, we consider the properties of cubes modulo 9. Cubes modulo 9 can only be congruent to 0, 1,
or −1. This is because:
03 ≡0
(mod 9),
13 ≡1
(mod 9),
23 ≡8 ≡−1
(mod 9),
33 ≡27 ≡0
(mod 9),
43 ≡64 ≡1
(mod 9),
53 ≡125 ≡−1
(mod 9),
63 ≡216 ≡0
(mod 9),
73 ≡343 ≡1
(mod 9),
83 ≡512 ≡−1
(mod 9).
Now, we need to determine 20022002 mod 9. First, we find 2002 mod 9:
2002 ÷ 9 = 222 remainder 4
⇒
2002 ≡4
(mod 9).
Thus,
20022002 ≡42002
(mod 9).
Next, we use Euler’s theorem, which states that aϕ(n) ≡1 (mod n) for gcd(a, n) = 1. Here,
ϕ(9) = 6, so:
46 ≡1
(mod 9).
19

--- Page 20 ---

We can reduce the exponent 2002 mod 6:
2002 ÷ 6 = 333 remainder 4
⇒
2002 ≡4
(mod 6).
Thus,
42002 ≡44
(mod 9).
44 = 256.
Finally, we find 256 mod 9:
256 ÷ 9 = 28 remainder 4
⇒
256 ≡4
(mod 9).
Therefore,
20022002 ≡4
(mod 9).
We need to find the smallest t such that the sum of t cubes is congruent to 4 modulo 9. The possible
sums of cubes modulo 9 are:
0 ≡0
(mod 9),
1 ≡1
(mod 9),
−1 ≡8
(mod 9),
1 + 1 ≡2
(mod 9),
1 + (−1) ≡0
(mod 9),
−1 + (−1) ≡−2 ≡7
(mod 9),
1 + 1 + 1 ≡3
(mod 9),
1 + 1 + (−1) ≡1
(mod 9),
1 + (−1) + (−1) ≡−1 ≡8
(mod 9),
−1 + (−1) + (−1) ≡−3 ≡6
(mod 9),
1 + 1 + 1 + 1 ≡4
(mod 9).
We see that the sum of four cubes can be congruent to 4 modulo 9. Therefore, the smallest t is 4.
Thus, the smallest positive integer t such that there exist integers x1, x2, . . . , xt with
x3
1 + x3
2 + · · · + x3
t = 20022002
is
4 .
Problem From IMO Shortlist 2022
For a positive integer n we denote by s(n) the sum of the digits of n. Let P(x) = xn + an−1xn−1 +
· · · + a1x + a0 be a polynomial, where n ≥2 and ai is a positive integer for all 0 ≤i ≤n −1.
Could it be the case that, for all positive integers k, s(k) and s(P(k)) have the same parity?
Qwen2-Math-72B-Instruct Solution
To determine whether it is possible for s(k) and s(P(k)) to have the same parity for all positive
integers k, we need to analyze the behavior of the sum of the digits function s and the polynomial
P(x).
20

--- Page 21 ---

First, recall that the sum of the digits of a number k modulo 2 is equivalent to k mod 2. This is
because the sum of the digits of k in base 10 is congruent to k mod 9, and since 9 ≡1 mod 2, the
sum of the digits modulo 2 is the same as k mod 2.
Given the polynomial P(x) = xn + an−1xn−1 + · · · + a1x + a0, we need to determine the parity
of P(k) for any positive integer k. Specifically, we need to check if P(k) mod 2 is the same as k
mod 2.
Let’s consider the polynomial modulo 2:
P(x) ≡xn + an−1xn−1 + · · · + a1x + a0
mod 2.
Since ai are positive integers, ai mod 2 is either 0 or 1. Let bi = ai mod 2. Then we can rewrite
the polynomial modulo 2 as:
P(x) ≡xn + bn−1xn−1 + · · · + b1x + b0
mod 2.
Now, we need to check the parity of P(k) for k ≡0 mod 2 and k ≡1 mod 2.
1. **Case 1: k ≡0 mod 2**
P(0) ≡b0
mod 2.
For s(P(0)) to have the same parity as s(0), b0 must be 0. Therefore, a0 must be even.
2. **Case 2: k ≡1 mod 2**
P(1) ≡1n + bn−1 · 1n−1 + · · · + b1 · 1 + b0 ≡1 + bn−1 + · · · + b1 + b0
mod 2.
For s(P(1)) to have the same parity as s(1), 1 + bn−1 + · · · + b1 + b0 must be odd. Since 1 is odd,
the sum bn−1 + · · · + b1 + b0 must be even.
From the above cases, we have: - a0 must be even. - The sum bn−1 + · · · + b1 + b0 must be even.
However, if a0 is even, then b0 = 0. This means the sum bn−1 + · · · + b1 must be even. But since bi
are either 0 or 1, the sum of bn−1 + · · · + b1 being even implies that there must be an even number of
1’s among bn−1, . . . , b1.
Now, consider the polynomial P(x) = xn + 1. For this polynomial: - a0 = 1 (odd), which
contradicts our requirement that a0 must be even. - The sum bn−1 + · · · + b1 + b0 = 1 (odd), which
also contradicts our requirement that the sum must be even.
Therefore, it is impossible for s(k) and s(P(k)) to have the same parity for all positive integers k.
Thus, the final answer is:
No
21

--- Page 22 ---

A.2
ALGEBRA
Problem From IMO 2022
Let R+ denote the set of positive real numbers. Find all functions f : R+ →R+ such that for each
x ∈R+, there is exactly one y ∈R+ satisfying
xf(y) + yf(x) ≤2
Qwen2-Math-72B-Instruct Solution
To find all functions f : R+ →R+ such that for each x ∈R+, there is exactly one y ∈R+ satisfying
xf(y) + yf(x) ≤2,
we will proceed step by step.
Step 1: Analyze the given inequality
Given x ∈R+, there exists a unique y ∈R+ such that
xf(y) + yf(x) ≤2.
We need to explore the implications of this condition.
Step 2: Consider the case x = y
Substitute y = x into the inequality:
xf(x) + xf(x) = 2xf(x) ≤2.
This simplifies to:
xf(x) ≤1.
Thus, for all x ∈R+,
f(x) ≤1
x.
Step 3: Consider the uniqueness condition
For each x ∈R+, there is exactly one y ∈R+ such that xf(y) + yf(x) ≤2. We need to ensure that
this y is unique.
Step 4: Test the function f(x) = 1
x
Consider the function f(x) = 1
x. Substitute f(x) = 1
x and f(y) = 1
y into the inequality:
x · 1
y + y · 1
x = x
y + y
x.
We need:
x
y + y
x ≤2.
Using the AM-GM inequality, we know:
x
y + y
x ≥2.
Equality holds if and only if x
y = 1, which implies x = y.
Thus, for f(x) = 1
x, the inequality xf(y) + yf(x) ≤2 holds if and only if x = y. This satisfies the
condition that there is exactly one y for each x.
Step 5: Verify if other functions can satisfy the condition
Suppose there exists another function g : R+ →R+ such that g(x) ̸= 1
x for some x. Then, for some
x, g(x) < 1
x or g(x) > 1
x.
- If g(x) < 1
x, then xg(y) + yg(x) might not satisfy the inequality for all y. - If g(x) > 1
x, then
xg(y) + yg(x) might exceed 2 for some y.
22

--- Page 23 ---

Thus, any function other than f(x) = 1
x would not satisfy the uniqueness condition.
Conclusion
The only function f : R+ →R+ that satisfies the given condition is:
f(x) = 1
x .
23

--- Page 24 ---

Problem from International Zhautykov Olympiad 2020
Let Z be the set of all integers. Find all the function f : Z →Z such that
f(4x + 3y) = f(3x + y) + f(x + 2y)
For all integers x, y
Qwen2-Math-72B-Instruct Solution
To find all functions f : Z →Z that satisfy the functional equation
f(4x + 3y) = f(3x + y) + f(x + 2y)
for all integers x and y, we will proceed step by step.
Step 1: Initial Substitution
First, let’s substitute specific values for x and y to gain insight into the
function.
SUBSTITUTION 1: x = 0
f(4 · 0 + 3y) = f(3 · 0 + y) + f(0 + 2y)
f(3y) = f(y) + f(2y)
SUBSTITUTION 2: y = 0
f(4x + 3 · 0) = f(3x + 0) + f(x + 2 · 0)
f(4x) = f(3x) + f(x)
Step 2: Exploring Further Substitutions
We now have two equations: 1. f(3y) = f(y) + f(2y)
2. f(4x) = f(3x) + f(x)
SUBSTITUTION 3: y = 1 IN THE FIRST EQUATION
f(3 · 1) = f(1) + f(2 · 1)
f(3) = f(1) + f(2)
SUBSTITUTION 4: x = 1 IN THE SECOND EQUATION
f(4 · 1) = f(3 · 1) + f(1)
f(4) = f(3) + f(1)
Step 3: Using the Equations to Find a Pattern
We have:
f(3) = f(1) + f(2)
f(4) = f(3) + f(1)
Substitute f(3) from the first equation into the second equation:
f(4) = (f(1) + f(2)) + f(1)
f(4) = 2f(1) + f(2)
Step 4: Generalizing the Function
We hypothesize that f might be a linear function. Let’s assume
f(x) = kx for some integer k.
VERIFICATION
Substitute f(x) = kx into the original functional equation:
f(4x + 3y) = k(4x + 3y)
f(3x + y) = k(3x + y)
f(x + 2y) = k(x + 2y)
The original equation becomes:
k(4x + 3y) = k(3x + y) + k(x + 2y)
4kx + 3ky = 3kx + ky + kx + 2ky
4kx + 3ky = 4kx + 3ky
This equation holds true for all x and y, confirming that f(x) = kx is a solution.
24

--- Page 25 ---

Conclusion
The only functions f : Z →Z that satisfy the given functional equation are of the
form f(x) = kx for some integer k.
Thus, the final answer is:
f(x) = kx for some integer k
Problem From Baltic Way 2023
Find all functions f : R →R such that
f(f(x) + y) + xf(y) = f(xy + y) + f(x)
for reals x, y.
Qwen2-Math-72B-Instruct Solution:
To find all functions f : R →R that satisfy the functional equation
f(f(x) + y) + xf(y) = f(xy + y) + f(x),
we will proceed step by step.
Step 1: Initial Substitution
First, let’s substitute y = 0 into the equation:
f(f(x) + 0) + xf(0) = f(x · 0 + 0) + f(x).
This simplifies to:
f(f(x)) + xf(0) = f(0) + f(x).
Rearranging terms, we get:
f(f(x)) = f(x) + f(0) −xf(0).
Step 2: Analyzing the Simplified Equation
Let c = f(0). The equation becomes:
f(f(x)) = f(x) + c −xc.
Step 3: Substituting x = 0
Next, substitute x = 0 into the original equation:
f(f(0) + y) + 0 · f(y) = f(0 · y + y) + f(0).
This simplifies to:
f(c + y) = f(y) + c.
Step 4: Substituting y = −c
Substitute y = −c into the equation f(c + y) = f(y) + c:
f(c −c) = f(−c) + c.
This simplifies to:
f(0) = f(−c) + c.
Since f(0) = c, we have:
c = f(−c) + c.
Subtracting c from both sides, we get:
f(−c) = 0.
Step 5: Substituting y = −f(x)
Substitute y = −f(x) into the original equation:
f(f(x) −f(x)) + xf(−f(x)) = f(x(−f(x)) −f(x)) + f(x).
This simplifies to:
f(0) + xf(−f(x)) = f(−xf(x) −f(x)) + f(x).
Since f(0) = c, we have:
c + xf(−f(x)) = f(−xf(x) −f(x)) + f(x).
25

--- Page 26 ---

Step 6: Considering f(x) = 0
Assume f(x) = 0 for all x. Substitute f(x) = 0 into the original
equation:
f(0 + y) + xf(y) = f(xy + y) + f(x).
This simplifies to:
f(y) + 0 = f(y) + 0,
which is always true.
Step 7: Verifying f(x) = x
Assume f(x) = x. Substitute f(x) = x into the original equation:
f(x + y) + xf(y) = f(xy + y) + f(x).
This simplifies to:
x + y + xy = xy + y + x,
which is always true.
Conclusion
The only functions that satisfy the given functional equation are f(x) = 0 and
f(x) = x. Therefore, the solutions are:
f(x) = 0 or f(x) = x .
26

--- Page 27 ---

A.3
COUNTING & PROBABILITY
Problem From Lusophon Mathematical Olympiad 2023
A long time ago, there existed Martians with 3 different colours: red, green and blue. As Mars was
devastated by an intergalactic war, only 2 Martians of each colours survived. In order to reconstruct
the Martian population, they decided to use a machine that transforms two Martians of distinct colours
into four Martians of colour different to the two initial ones. For example, if a red Martian and a blue
Martian use the machine, they’ll be transformed into four green Martians.
a) Is it possible that, after using that machine finitely many times, we have 2022 red Martians, 2022
green Martians and 2022 blue Martians?
b) Is it possible that, after using that machine finitely many times, we have 2021 red Martians, 2022
green Martians and 2023 blue Martians?
Qwen2-Math-72B-Instruct Solution
Let’s analyze the problem step by step.
Part (a)
We start with 2 red, 2 green, and 2 blue Martians. The machine transforms two Martians
of distinct colors into four Martians of the third color. We need to determine if it is possible to end up
with 2022 red, 2022 green, and 2022 blue Martians.
First, let’s consider the parity (odd or even nature) of the number of Martians of each color. Initially,
we have: - 2 red (even) - 2 green (even) - 2 blue (even)
Each transformation changes the parity of the number of Martians of the two initial colors and the
parity of the number of Martians of the third color. Specifically: - If we transform 1 red and 1 green
Martian, we get 4 blue Martians. This changes the parity of red and green Martians from even to odd,
and the parity of blue Martians from even to odd. - If we transform 1 red and 1 blue Martian, we
get 4 green Martians. This changes the parity of red and blue Martians from even to odd, and the
parity of green Martians from even to odd. - If we transform 1 green and 1 blue Martian, we get 4 red
Martians. This changes the parity of green and blue Martians from even to odd, and the parity of red
Martians from even to odd.
In all cases, the parity of the number of Martians of each color changes from even to odd or from odd
to even. Therefore, after any number of transformations, the parity of the number of Martians of each
color will always be the same as it was initially.
Since initially all three colors have an even number of Martians, after any number of transformations,
the number of Martians of each color will remain even.
Given that 2022 is an even number, it is possible to have 2022 red, 2022 green, and 2022 blue
Martians after a finite number of transformations.
Thus, the answer to part (a) is:
Yes
Part (b)
We start again with 2 red, 2 green, and 2 blue Martians. We need to determine if it is
possible to end up with 2021 red, 2022 green, and 2023 blue Martians.
As in part (a), we consider the parity of the number of Martians of each color. Initially, we have: - 2
red (even) - 2 green (even) - 2 blue (even)
Each transformation changes the parity of the number of Martians of the two initial colors and the
parity of the number of Martians of the third color. Therefore, after any number of transformations,
the parity of the number of Martians of each color will always be the same as it was initially.
Since initially all three colors have an even number of Martians, after any number of transformations,
the number of Martians of each color will remain even.
Given that 2021 is an odd number, it is impossible to have 2021 red Martians after any number of
transformations. Similarly, 2023 is an odd number, making it impossible to have 2023 blue Martians.
27

--- Page 28 ---

Thus, the answer to part (b) is:
No
Problem From Balkan MO 2023
Joe and Penny play a game. Initially there are 5000 stones in a pile, and the two players remove
stones from the pile by making a sequence of moves. On the k-th move, any number of stones
between 1 and k inclusive may be removed. Joe makes the odd-numbered moves and Penny makes
the even-numbered moves. The player who removes the very last stone is the winner. Who wins if
both players play perfectly?
Qwen2-Math-72B-Instruct Solution
To determine the winner of the game, we need to analyze the strategy and the sequence of moves.
Let’s break down the problem step by step.
1. **Understanding the Game Rules:** - Initially, there are 5000 stones. - Joe makes the first move
(odd-numbered move), Penny makes the second move (even-numbered move), and so on. - On the
k-th move, a player can remove between 1 and k stones. - The player who removes the last stone
wins.
2. **Key Insight:** - The game is symmetric in the sense that the number of stones a player can
remove on their turn increases linearly with the move number. - The total number of moves in the
game is equal to the number of stones initially in the pile, which is 5000.
3. **Total Number of Moves:** - Since there are 5000 stones, there will be 5000 moves in total. -
Joe makes the odd-numbered moves: 1st, 3rd, 5th, ..., 4999th. - Penny makes the even-numbered
moves: 2nd, 4th, 6th, ..., 5000th.
4. **Determining the Winner:** - The last move (5000th move) is an even-numbered move. -
Therefore, Penny will make the last move.
5. **Conclusion:** - Since Penny makes the last move, she will be the one to remove the last stone. -
Hence, Penny wins the game if both players play perfectly.
Thus, the final answer is:
Penny
Problem From Math Odyssey
The school offers 10 elective courses, and each student can enroll in any number of courses. The
director selects k students, where although each student’s combination of courses is different, any
two students have at least one course in common. At this point, it is found that any student outside
these k students cannot be classmates with these k students regardless of how they enroll (having one
course in common is enough to be classmates). Find the maximum number of k.
Qwen2-Math-72B-Instruct Solution
To solve this problem, we need to determine the maximum number of students k such that each
student has a unique combination of elective courses, any two students share at least one course, and
no student outside these k students can be classmates with all of them. This means that the set of
students chosen must cover all possible courses in such a way that any new student would have to
share a course with at least one of the chosen students.
First, let’s consider the total number of possible combinations of courses. Since there are 10 elective
courses and each student can either take or not take each course, there are 210 = 1024 possible
combinations of courses. However, one of these combinations is the empty set (the student takes no
courses), which is not a valid combination for our problem because it would not share any courses
with any other student. Therefore, there are 1024 −1 = 1023 non-empty combinations of courses.
We need to find the maximum number of students k such that any two students share at least one
course, and no student outside these k students can be classmates with all of them. This is equivalent
to finding the maximum number of vertices in a graph where each vertex represents a non-empty
combination of courses, and there is an edge between two vertices if and only if the corresponding
28

--- Page 29 ---

combinations share at least one course. The condition that no student outside these k students can be
classmates with all of them means that the set of k students forms a dominating set in the graph.
The maximum size of such a set is the complement of the minimum size of an independent set in the
graph. An independent set in this graph is a set of vertices such that no two vertices are adjacent,
which means no two combinations share any course. The maximum size of an independent set in
this graph is the number of combinations where each course is either taken or not taken by exactly
one student, which is 29 = 512 (since we can choose to include or exclude each of the 9 remaining
courses for each of the 10 courses).
Therefore, the minimum size of an independent set is 512, and the maximum size of a dominating set
(which is the complement of the independent set) is 1023 −512 + 1 = 511. However, we need to
add 1 because the empty set is not included, so the correct calculation is 1023 −511 = 512.
Thus, the maximum number of students k is 512 .
29

--- Page 30 ---

A.4
GEOMETRY
Problem from USAMO 2010
Let ABC be a triangle with ∠A = 90◦. Points D and E lie on sides AC and AB, respectively,
such that ∠ABD = ∠DBC and ∠ACE = ∠ECB. Segments BD and CE meet at I. Determine
whether or not it is possible for segments AB, AC, BI, ID, CI, IE to all have integer lengths.
Qwen2-Math-72B-Instruct Solution
To determine whether it is possible for segments AB, AC, BI, ID, CI, and IE to all have integer
lengths in triangle ABC with ∠A = 90◦, we start by analyzing the given conditions and properties
of the triangle.
Given: - ∠A = 90◦- ∠ABD = ∠DBC - ∠ACE = ∠ECB - Segments BD and CE intersect at I
First, note that since ∠A = 90◦, triangle ABC is a right triangle with A as the right angle. Points D
and E are such that BD and CE are angle bisectors of ∠ABC and ∠ACB, respectively. Therefore,
I is the incenter of triangle ABC.
Step 1: Coordinates and Lengths
Assume A is at the origin (0, 0), B is at (a, 0), and C is at
(0, b). The lengths of the sides are: - AB = a - AC = b - BC =
√
a2 + b2
Step 2: Incenter Coordinates
The incenter I of a right triangle with legs a and b and hypotenuse
√
a2 + b2 is located at:
I =
a
2, b
2

Step 3: Lengths of Segments BI and CI
Using the distance formula, we calculate BI and CI:
BI =
s
a −a
2
2
+

0 −b
2
2
=
sa
2
2
+
 b
2
2
=
√
a2 + b2
2
CI =
s
0 −a
2
2
+

b −b
2
2
=
sa
2
2
+
 b
2
2
=
√
a2 + b2
2
Step 4: Lengths of Segments ID and IE
Since D and E are points on AC and AB respectively,
and I is the incenter, ID and IE are the distances from the incenter to the sides of the triangle. For a
right triangle, these distances are given by:
ID = IE = r = a + b −
√
a2 + b2
2
Step 5: Integer Lengths
For AB, AC, BI, ID, CI, and IE to all be integers, the following must
hold: - a and b are integers -
√
a2+b2
2
is an integer - a+b−
√
a2+b2
2
is an integer
Step 6: Analysis
For
√
a2+b2
2
to be an integer,
√
a2 + b2 must be an even integer. Let
√
a2 + b2 =
2k for some integer k. Then:
a2 + b2 = 4k2
For a+b−
√
a2+b2
2
to be an integer, a + b −2k must be even. Since a and b are integers, a + b must be
even.
Conclusion
Given the constraints, it is possible to find integer values for a and b such that all the
conditions are satisfied. For example, if a = 3 and b = 4, then: - AB = 3 - AC = 4 - BC = 5 -
BI = CI = 5
2 = 2.5 (not an integer)
Thus, it is not possible for all segments AB, AC, BI, ID, CI, and IE to have integer lengths
simultaneously.
No
30

--- Page 31 ---

Problem from JBMO Shortlist 2011
Let AD, BF and CE be the altitudes of △ABC. A line passing through D and parallel to
ABintersects the line EFat the point G. If H is the orthocenter of △ABC, find the angle ∠CGH.
Qwen2-Math-72B-Instruct Solution
To solve for the angle ∠CGH in the given triangle △ABC with altitudes AD, BF, and CE
intersecting at the orthocenter H, and a line through D parallel to AB intersecting EF at G, we will
follow these steps:
1. Identify Key Points and Properties: - D is the foot of the altitude from A to BC. - E is the foot
of the altitude from B to AC. - F is the foot of the altitude from C to AB. - H is the orthocenter of
△ABC. - G is the intersection of the line through D parallel to AB and the line EF.
2. Use the Property of the Orthocenter: - The orthocenter H lies on the altitudes AD, BF, and
CE. - The points D, E, and F are collinear with H on the respective altitudes.
3. Analyze the Parallel Line: - Since DG ∥AB, ∠ADG = ∠DAB (corresponding angles).
4. Consider the Cyclic Quadrilateral: - The quadrilateral AEHF is cyclic because ∠AEH =
∠AFH = 90◦. - Therefore, ∠EHF = 180◦−∠EAF.
5. Use the Parallel Line Property Again: - Since DG ∥AB, ∠DGE = ∠BAE (alternate interior
angles).
6. Relate Angles in Cyclic Quadrilateral: - In △AEF, ∠EAF = ∠EHF because they are
opposite angles in the cyclic quadrilateral AEHF.
7. Determine ∠CGH: - Since G lies on EF and DG ∥AB, ∠DGE = ∠BAE. - ∠BAE =
∠EAF (as established). - Therefore, ∠DGE = ∠EAF.
8. Final Angle Calculation: - Since ∠EAF = ∠EHF and ∠EHF = 90◦(as H is the orthocenter
and E and F are feet of perpendiculars), we have:
∠CGH = ∠EHF = 90◦.
Thus, the angle ∠CGH is 90◦.
B
PROMPTS USED IN THE EVALUATION
Fig 5 to Fig 10 show the prompts used in evaluating the base models. Fig 11 to Fig 14 show the
prompts used in evaluating the instruct models for Chain-of-Thought Reasoning and Tool-Integrated
Reasoning.
31

--- Page 32 ---

Question: In 2004, there were 60 kids at a cookout. In 2005, half the number of kids came to the cookout as 
compared to 2004. In 2006, 2/3 as many kids came to the cookout as in 2005. How many kids came to the cookout 
in 2006? \newline Let's think step by step
In 2005, 60/2=30 kids came to the cookout. \newline In 2006, 30/3*2=20 kids came to the cookout. \newline The 
answer is 20
Question: Zilla spent 7% of her monthly earnings on rent, half of it on her other monthly expenses, and put the 
rest in her savings. If she spent $133 on her rent, how much does she deposit into her savings account in a month?
\newline Let's think step by step
Since $133 is equal to 7% of her earnings, then 1% is equal to $133/7 = $19. \newline The total monthly earning 
of Zilla is represented by 100%, so $19 x 100 = $1900 is her monthly earnings. \newline So, $1900/2 = $950 is 
spent on her other monthly expenses. \newline The total amount spent on the rent and other monthly expenses is 
$133 + $950 = $1083. \newline Hence, she saves $1900 - $1083 = $817 per month. \newline The answer is 817
Question: If Buzz bought a pizza with 78 slices at a restaurant and then decided to share it with the waiter in the 
ratio of 5:8, with Buzz's ratio being 5, what's twenty less the number of slices of pizza that the waiter ate? \newline
Let's think step by step
The total ratio representing the slices of pizza that Buzz bought is 5+8=13 \newline If he shared the slices of pizza 
with the waiter, the waiter received a fraction of 8/13 of the total number of slices, which totals 8/13 * 78 = 48 
slices \newline Twenty less the number of slices of pizza that the waiter ate is 48-20 = 28 \newline The answer is 
28
Question: Jame gets a raise to $20 per hour and works 40 hours a week.  His old job was $16 an hour for 25 hours 
per week.  How much more money does he make per year in his new job than the old job if he works 52 weeks a 
year? \newline Let's think step by step
He makes 20*40=$800 per week \newline He used to make 16*25=$400 per week \newline So his raise was 800-
400=$400 per week \newline So he makes 400*52=$20,800 per year more \newline The answer is 20800
Question: Mr. Gardner bakes 20 cookies, 25 cupcakes, and 35 brownies for his second-grade class of 20 students. 
If he wants to give each student an equal amount of sweet treats, how many sweet treats will each student receive?
\newline Let's think step by step
Mr. Gardner bakes a total of 20 + 25 + 35 = 80 sweet treats \newline Each student will receive 80 / 20 = 4 sweet 
treats \newline The answer is 4
Question: A used car lot has 24 cars and motorcycles (in total) for sale. A third of the vehicles are motorcycles, 
and a quarter of the cars have a spare tire included. How many tires are on the used car lot’s vehicles in all?
\newline Let's think step by step
The used car lot has 24 / 3 = 8 motorcycles with 2 tires each. \newline The lot has 24 - 8 = 16 cars for sale
\newline There are 16 / 4 = 4 cars with a spare tire with 5 tires each. \newline The lot has 16 - 4 = 12 cars with 4 
tires each. \newline Thus, the used car lot’s vehicles have 8 * 2 + 4 * 5 + 12 * 4 = 16 + 20 + 48 = 84 tires in all.
\newline The answer is 84
Question: Norma takes her clothes to the laundry. She leaves 9 T-shirts and twice as many sweaters as T-shirts in 
the washer. When she returns she finds 3 sweaters and triple the number of T-shirts. How many items are missing?
\newline Let's think step by step
Norma left 9 T-shirts And twice as many sweaters, she took 9 * 2= 18 sweaters \newline Adding the T-shirts and 
sweaters, Norma left 9 + 18 = 27 clothes \newline When she came back, she found 3 sweaters And triple the 
number of T-shirts, she found 3 * 3 = 9 T-shirts \newline Adding the T-shirts and sweaters, Norma found 3 + 9 = 
12 clothes \newline Subtracting the clothes she left from the clothes she found, 27 - 12 = 15 clothes are missing
\newline The answer is 15
Question: Adam has an orchard. Every day for 30 days he picks 4 apples from his orchard. After a month, Adam 
has collected all the remaining apples, which were 230. How many apples in total has Adam collected from his 
orchard? \newline Let's think step by step
During 30 days Adam picked 4 * 30 = 120 apples. \newline So in total with all the remaining apples, he picked 
120 + 230 = 350 apples from his orchard. \newline The answer is 350
Question: {question} \newline Let's think step by step
Figure 5: The prompt used in evaluating GSM8K on the base models. For friendly presentation, we
denote a line break as a ”\newline”.
32

--- Page 33 ---

Problem:
Find the domain of the expression $\frac{\sqrt{x-2}}{\sqrt{5-x}}$.
Solution:
The expressions inside each square root must be non-negative. Therefore, $x-2 \ge 0$, so $x\ge2$, and $5 - x \ge 
0$, so $x \le 5$. Also, the denominator cannot be equal to zero, so $5-x>0$, which gives $x<5$. Therefore, the 
domain of the expression is $\boxed{[2,5)}$.
The answer is: $[2,5)$.
Problem:
If $\det \mathbf{A} = 2$ and $\det \mathbf{B} = 12,$ then find $\det (\mathbf{A} \mathbf{B}).$
Solution:
We have that $\det (\mathbf{A} \mathbf{B}) = (\det \mathbf{A})(\det \mathbf{B}) = (2)(12) = \boxed{24}.$
The answer is: $24$.
Problem:
Terrell usually lifts two 20-pound weights 12 times. If he uses two 15-pound weights instead, how many times 
must Terrell lift them in order to lift the same total weight?
Solution:
If Terrell lifts two 20-pound weights 12 times, he lifts a total of $2\cdot 12\cdot20=480$ pounds of weight. If he 
lifts two 15-pound weights instead for $n$ times, he will lift a total of $2\cdot15\cdot n=30n$ pounds of weight. 
Equating this to 480 pounds, we can solve for $n$:
\begin{align*}
30n&=480\\
\Rightarrow\qquad n&=480/30=\boxed{16}
\end{align*}
The answer is: $16$.
Problem:
If the system of equations
\begin{align*}
6x-4y&=a,\\
6y-9x &=b.
\end{align*} has a solution $(x, y)$ where $x$ and $y$ are both nonzero, find $\frac{a}{b},$ assuming $b$ is 
nonzero.
Solution:
If we multiply the first equation by $-\frac{3}{2}$, we obtain $$6y-9x=-\frac{3}{2}a.$$ Since we also know that 
$6y-9x=b$, we have $$-\frac{3}{2}a=b\Rightarrow\frac{a}{b}=\boxed{-\frac{2}{3}}.$$
The answer is: $-\frac{2}{3}$.
Problem:
{instruction}
Solution:
Figure 6: The prompt used in evaluating MATH on the base models.
33

--- Page 34 ---

Problem:
Find the domain of the expression $\frac{\sqrt{x-2}}{\sqrt{5-x}}$. \newline What of the following is the right 
choice? Explain your answer. \newline (A) [-5,-2) \newline (B) [2,5) \newline (C) [-2,-5) \newline (D) [5,2)
Solution:
The expressions inside each square root must be non-negative. Therefore, $x-2 \ge 0$, so $x\ge2$, and $5 - x \ge 
0$, so $x \le 5$. Also, the denominator cannot be equal to zero, so $5-x>0$, which gives $x<5$. \newline
Therefore, the domain of the expression is $\boxed{[2,5)}$. \newline Final Answer: The final answer is (B). I 
hope it is correct.
Problem:
If $\det \mathbf{A} = 2$ and $\det \mathbf{B} = 12,$ then find $\det (\mathbf{A} \mathbf{B}).$
What of the following is the right choice? Explain your answer. \newline (A) 14 \newline (B) 4 \newline (C) 2
\newline (D) 24
Solution:
We have that $\det (\mathbf{A} \mathbf{B}) = (\det \mathbf{A})(\det \mathbf{B}) = (2)(12) = \boxed{24}.$
\newline Final Answer: The final answer is (D). I hope it is correct.
Problem:
Terrell usually lifts two 20-pound weights 12 times. If he uses two 15-pound weights instead, how many times 
must Terrell lift them in order to lift the same total weight? \newline What of the following is the right choice? 
Explain your answer. \newline (A) 12 \newline (B) 20 \newline (C) 16 \newline (D) 15
Solution:
If Terrell lifts two 20-pound weights 12 times, he lifts a total of $2\cdot 12\cdot20=480$ pounds of weight. If he 
lifts two 15-pound weights instead for $n$ times, he will lift a total of $2\cdot15\cdot n=30n$ pounds of weight. 
Equating this to 480 pounds, we can solve for $n$:
\begin{align*}
30n&=480\\
\Rightarrow\qquad n&=480/30=\boxed{16}
\end{align*} \newline Final Answer: The final answer is (C). I hope it is correct.
Problem:
If the system of equations
\begin{align*}
6x-4y&=a,\\
6y-9x &=b.
\end{align*}
has a solution $(x, y)$ where $x$ and $y$ are both nonzero, find $\frac{a}{b},$ assuming $b$ is nonzero.
\newline What of the following is the right choice? Explain your answer. \newline (A) $-\frac{2}{3}$ \newline (B) 
$\frac{2}{3}$ \newline (C) $\frac{1}{3}$ \newline (D) $\frac{4}{9}$
Solution:
If we multiply the first equation by $-\frac{3}{2}$, we obtain $$6y-9x=-\frac{3}{2}a.$$ Since we also know that 
$6y-9x=b$, we have $$-\frac{3}{2}a=b\Rightarrow\frac{a}{b}=\boxed{-\frac{2}{3}}.$$ \newline Final Answer: 
The final answer is (A). I hope it is correct.
Problem:
{question}
What of the following is the right choice? Explain your answer. \newline (A) {option_a} \newline (B) {option_b}
\newline (C) {option_c} \newline (D) {option_d}
Solution:
Figure 7: The prompt used in evaluating MMLU STEM on the base models.
34

--- Page 35 ---

问题：芳芳买了一本书有99页，看了90页，她还剩多少页没有看？
答案：还剩的没有看的页数=书的总页数-芳芳看了的页数，99-90=9。所以答案是：9。
问题：张师傅上午修了18把椅子，下午修了29把椅子，一天共修了多少把椅子？
答案：一天共修的椅子数量=上午修的椅子数量+下午修的椅子数量，18+29=47。所以答案是：47。
问题：小猴摘了84个桃子，平均分给6只猴子，每只猴子能吃到几个桃子？
答案：每只猴子能吃到的桃子数=总桃子数/猴子的数量，84/6=14。所以答案是：14。
问题：用面包机烤面包时，第一面烤2分钟，第二面只要烤1分钟，即烤一片面包需要3分钟，小勤的面包
机一次只能放2片，他每天早上吃3片面包，至少需要烤多少分钟？
答案：可以现将两片面包放入面包机烤2分钟，再将其中一片拿出来，将第三片面包放进去，烤1分钟，
这样第一片面包就烤好了，将第一片面包拿出来将第二片面包放进去，继续烤1分钟，于是第二片面包也
烤好了将其拿出来，第三片面包再烤1分钟也就烤好了，一共是2+1+1=5。所以答案是：5。
问题：一组学生植树，每人栽6棵还剩4棵；如果其中3人各栽5棵，其余每人各栽7棵，正好栽完。这一组
学生有多少人？
答案：假设学生的数量是x，每人栽6棵还剩4棵，也就是说树苗的数量=6x+4，又知道如果其中3人各栽5
棵，其余每人各栽7棵，正好栽完，即6x+4=3*5+(x-3)*7，化简方程得到：x=10。所以答案是：10。
问题：某小学在“献爱心--为汶川地震区捐款”活动中，六年级五个班共捐款8000元，其中一班捐款1500
元，二班比一班多捐款200元，三班捐款1600元，四班与五班捐款数之比是3：5．四班捐款多少元？
答案：一班捐款1500元，而二班比一班多捐200元，所以二班捐款1500+200=1700元，又知道六年级五个
班一共捐款8000元，所以四班和五班捐款之和= 一共捐款- 一班和二班和三班捐款之和，即8000-1500-
1700-1600=3200元，而题目说四班与五班捐款数之比是3：5，则四班捐款了3200/(3+5)*3=1200元。所以
答案是：1200。
问题：{question}
答案：
Figure 8: The prompt used in evaluating CMATH on the base models.
35

--- Page 36 ---

问题：
设数列$\left\{a_{n}\right\}$ 的前$n$ 项和为$S_{n}$, 且$a_{1}=-1, a_{n+1}=S_{n+1} S_{n}$, 则
$S_{n}=(\quad)$.
解析：
让我们写出这个数列的前n项和：
$S_n = a_1 + a_2 + ... + a_n$ \newline $S_n = -1 + (S_2 S_1) + (S_3 S_2) + ... + (S_{n+1} S_n)$ \newline $S_n 
= -1 + (S_2 S_1) + (S_3 S_2) + ... + (S_n S_{n-1}) + (S_{n+1} S_n)$ \newline $S_n = -1 + S_n (S_{n+1} -
S_1)$ \newline $S_n - S_n S_{n+1} = -1 - S_n$ \newline $S_n (1 - S_{n+1}) = -1 - S_n$ \newline $S_n = -
\frac{1}{1 - S_{n+1}}$ \newline因为这个数列后面的所有项都是0，我们可以看到对于所有$n\geq 1$，
$S_{n+1} = 0$。因此，我们有：\newline $S_n = -\frac{1}{1 - S_{n+1}} = -\frac{1}{1 - 0} = -1$ \newline这
个数列前n项和的公式是$S_n = -\frac{1}{n}$。\newline 答案是$-\frac{1}{n}$
问题：
若$\left(x+\frac{1}{x}\right)^{n}$ 的展开式中第3 项与第7 项的二项式系数相等, 则该展开式中
$\frac{1}{x^{2}}$ 的系数为$(\quad)$.
解析：
由题意可得, $c_{n}^{2}=c_{n}^{6}$ \newline $\therefore n=8$ \newline 展开式的通项T_{r+1}=C_8^r x^{8-
r}\left(\frac{1}{x}\right)^r=C_8^r x^{8-2 r}$ \newline 令$8-2 r=-2$ 可得$r=5$ \newline此时系数为
$c_{8}^{5}=56$ \newline 答案是56
问题：
函数$\mathrm{f}(\mathrm{x})=\sin (\mathrm{x}+2 \phi)-2 \sin \phi \cos (\mathrm{x}+\phi)$ 的最大值为
$(\quad)$.
解析：
函数$f(x)=\sin (x+2 \phi)-2 \sin \phi \cos (x+\phi)=\sin [(x+\phi)+\phi]-$ $2 \sin \phi \cos (x+\phi)$
$=\sin (x+\phi) \cos \phi+\cos (x+\phi) \sin \phi-2 \sin \phi \cos (x+\phi)=\sin (x+\phi) \cos \phi-\cos$ $(x+\phi) 
\sin \phi$ $=\sin [(x+\phi)-\phi]=\sin x$ \newline 故函数$f(x)$ 的最大值为1 \newline 答案是1
问题：
已知向量$\vec{a}=(3,1), \vec{b}=(1,0), \vec{c}=\vec{a}+k \vec{b}$. 若$\vec{a} \perp \vec{c}$, 则
$k=(\quad)$
解析：
\because \vec{a}=(3,1), \vec{b}=(1,0), \therefore \vec{c}=\vec{a}+k \vec{b}=(3+k, 1)$ ，
$\because \vec{a} \perp \vec{c}, \therefore \vec{a} \square \vec{c}=3(3+k)+1 \times 1=0$, 解得$k=-
\frac{10}{3}$ \newline 答案是$-\frac{10}{3}$
问题：
设向量$\vec{a}, \vec{b}$ 不平行, 向量$\lambda \vec{a}+\vec{b}$ 与$\vec{a}+2 \vec{b}$ 平行, 则实数
$\lambda=(\quad)$.
解析：
$\because$ 向量$\vec{a}, \vec{b}$ 不平行, 向量$\lambda \vec{a}+\vec{b}$ 与$\vec{a}+2 \vec{b}$ 平行,
$\therefore \lambda \vec{a}+\vec{b}=t(\vec{a}+2 \vec{b})=t \vec{a}+2 t \vec{b}$
$\therefore\left\{\begin{array}{c}\lambda=\mathrm{t} \\ 1=2 \mathrm{t},\end{array}\right.$ 解得实数
$\lambda=\frac{1}{2}$. \newline 答案是$\frac{1}{2}$
问题：
{question}
解析：
Figure 9: The prompt used in evaluating GaoKao Math Cloze on the base models.
36

--- Page 37 ---

选择题:下列有关命题的说法正确的是( ) \newline A. 命题“若$ x^{2}=1 $，则$ x=1 $”的否命题为：“若$ 
x^{2}=1 $，则$ x\neq 1 $” \newline B. 命题“若$ x=y $，则$ \sin x=\sin y $”的逆否命题为真命题\newline
C. 命题“存在$ x∈R $，使得$ x^{2}+x+1 < 0 $”的否定是：“对任意$ x∈R $，均有$ x^{2}+x+1 < 0 $”
\newline D. “$ x=-1 $”是“$ x^{2}-5x-6=0 $”的必要不充分条件
解:命题“若$ x^{2}=1 $,则$ x=1 $”的否命题为“若$ x^{2}\neq 1 $,则$ x\neq 1 $”,故排除$ A $; 
$ ∵$命题“若$ x=y $,则$ \sin x=\sin y $”为真命题,故其逆否命题为真命题,B正确; 
命题“存在$ x∈R $,使得$ x^{2}+x+1 < 0 $”的否定是:“对任意$ x∈R $,均有$ x^{2}+x+1 > 0 $”,故排除$ C $; 
$ ∵$“$ x^{2}-5x-6=0 $”$ ⇔$“$ x=-1 $或$ x=6 $”,$ ∴$“$ x=-1 $”是“$ x^{2}-5x-6=0 $”的充分不必要条件,
排除$ D $;
故选:B. 
推理结束。
选择题:已知函数$ f $($ x $$ )= $$ x $$ {\,\!}^{2}+ $$ mx $$ -1 $,若对于任意$ x $$ ∈[ $$ m $,$ m $$ +1] $,都
有$ f $($ x $$ ) < 0 $成立,则实数$ m $的取值范围是( ). \newline A. $ \left(- \sqrt{2},0\right) $ \newline B. $ 
\left(-2,0\right) $ \newline C. $ \left[- \dfrac{ \sqrt{2}}{2},0\right] $ \newline D. $ \left(-
\dfrac{ \sqrt{2}}{2},0\right) $
解:由题意可得$ \begin{cases}f(m)=2{m}^{2}-1 < 0 \\ f(m+1)=2{m}^{2}+3m < 0\end{cases} $, 
求得$ - \dfrac{ \sqrt{2}}{2} < m < 0 $, 
即实数$ m $的取值范围为$ (- \dfrac{ \sqrt{2}}{2} ,0) $.
故选:D. 
推理结束。
选择题:设$ i $是虚数单位,若复数$ a+ \dfrac{5i}{1-2i}(a∈R) $是纯虚数,则$ a $等于( ) \newline A. $ -1 $ 
\newline B. $ 1 $ \newline C. $ 2 $ \newline D. $ -2 $ 
解:$ ∵a+ \dfrac {5i}{1-2i}=a+ \dfrac {5i(1+2i)}{(1-2i)(1+2i)}=a+ \dfrac {-10+5i}{5}=a-2+i $是纯虚数, 
$ ∴a=2 $. 
故选:C. 
推理结束。
选择题:已知集合$ A=\{2\leqslant x < 7\} $,$ B=\{x|3 < x < 10\} $,$ C=\{x|a-5 < x < a\} $ $ . $若非空集合$ 
C⊑(A∪B) $,则$ a $的取值范围是( ) \newline A. $ 7\leqslant a\leqslant 10 $ \newline B. $ 7\leqslant x < 10 $
\newline C. $ 8 < x < 10 $ \newline D. $ 8\leqslant x\leqslant 10 $
解:$ ∵$集合$ A=\{x|2\leqslant x < 7\} $,$ B=\{x|3 < x\leqslant 10\} $,$ ∴A∩B=\{x|3 < x < 7\} $, 
$ A∪B=\{x|2\leqslant x\leqslant 10\} $,$ A∪B=\{x|2\leqslant x\leqslant 10\} $, 
当$ C\neq \varnothing $时,要使$ C⊆(A∪B) $,$ \begin{cases}a-5\geqslant 2 \\ a\leqslant 10\end{cases} $,解得$ 
7\leqslant a\leqslant 10 $; 
$ ∴a $的取值范围是$ 7\leqslant a\leqslant 10 $.
故选:A. 
推理结束。
选择题:{question} \newline A. {option_a} \newline B. {option_b} \newline C. {option_c} \newline D. {option_d}
解:
Figure 10: The prompt used in evaluating GaoKao Math QA on the base models.
{question}
Please reason step by step, and put your final answer within \boxed{}
Figure 11: The prompt used in evaluating the zero-shot Chain of Thought Reasoning on the instruct
models.
37

--- Page 38 ---

{question}
Please integrate natural language reasoning with programs to solve the problem above, and put your final answer
within \boxed{}.
Figure 12: The prompt used in evaluating the zero-shot Tool-Integrated Reasoning on the instruct
models.
Simplify and write the result with a rational denominator: $$\sqrt{\sqrt[3]{\sqrt{\frac{1}{729}}}}$$
Answer Choices: (A) \frac{3\sqrt{3}}{3} (B) \frac{1}{3} (C) \sqrt{3} (D) \frac{\sqrt{3}}{3}
Factoring $729=3^6$ and combining the roots $\frac{1}{2}\frac{1}{3}\frac{1}{2}=\frac{1}{12}$, we get that 
$\sqrt{\sqrt[3]{\sqrt{\frac{1}{729}}}}=\left(\frac{1}{3^6}\right)^{\frac{1}{12}}=\frac{1}{3^{\frac{1}{2}}}=\f
rac{3}{\sqrt{3}}$. The answer is (D).
In animal cells, which of the following represents the most likely pathway that a secretory protein takes as it is 
synthesized in a cell?
Answer Choices: (A) Plasma membrane–Golgi apparatus–ribosome–secretory vesicle–rough ER (B) Ribosome–
Golgi apparatus–rough ER–secretory vesicle–plasma membrane (C) Plasma membrane–Golgi apparatus–
ribosome–secretory vesicle–rough ER (D) Ribosome–rough ER–Golgi apparatus–secretory vesicle–plasma 
membrane
Protein synthesis starts at the ribosome, so we can eliminate (A) and (C). The ribosome is often in the endoplasmic 
reticulum and moves from there to the Golgi apparatus, where it is modified and packaged into a vesicle. The 
vesicle then floats to the plasma membrane and is secreted. The answer is (D).
A microwave oven is connected to an outlet, 120 V, and draws a current of 2 amps. At what rate is energy being 
used by the microwave oven?
Answer Choices: (A) 10 W (B) 30 W (C) 60 W (D) 240 W
Rate of energy usage is known as power; in an dissipative electrical circuit, power is given by voltage times 
current. So in our case, the power is 120 V times 2 amps, or 240 W. The answer is (D).
Which of the following is considered an acid anhydride?
Answer Choices: (A) HCl (B) H2SO3 (C) SO2 (D) Al(NO3)3
An acid anhydride is a compound that is derived by removing water from an acid. The chemical formula for water 
is H2O, which means that we need to determine which of these options, when combined with H2O, forms an acid. 
SO2, or Sulfur dioxide, when combined with H2O, makes H2SO4, or sulfuric acid. The answer is (C).
What is the output of "abc"[::-1] in Python 3? 
Answer Choices: (A) Error (B) abc (C) cba (D) c
We know that the slicing operator [::-1] takes all of the elements in the string in reverse order, so we reverse the 
order of the string "abc", resulting in "cba". The answer is (C).
{question}
Figure 13: The prompt used in evaluating the MMLU-STEM on the instruct models.
38

--- Page 39 ---

已知$\alpha, \beta, \gamma$ 是互不相同的锐角, 则在$\sin \alpha \cos \beta, \sin \beta \cos \gamma, \sin 
\gamma \cos \alpha$ 三个值中, 大于$\frac{1}{2}$ 的个数的最大值是( )
从以下选项中选择:\newline(A) 0 :\newline(B) 1 :\newline(C) 2 :\newline(D) 3
1. 如果$\alpha, \beta, \gamma$ 均小于$60^\circ$，那么他们的正弦值都小于$\frac{1}{2}$，因此三个值中
不可能有大于$\frac{1}{2}$ 的值。 \newline2. 如果有一个角大于$60^\circ$，假设为$\alpha$，那么对应
的正弦值大于$\frac{1}{2}$。此时，由于三角形内角和为$180^\circ$，所以$\beta + \gamma < 120^\circ$。
这意味着$\beta, \gamma$ 的余弦值均大于$\frac{1}{2}$，所以此时$\sin \alpha \cos \beta > \frac{1}{2}, \sin 
\beta \cos \gamma > \frac{1}{2}$。 \newline3. 如果有两个角大于$60^\circ$，例如$\alpha$ 和$\beta$，那么
由于三角形内角和为$180^\circ$，我们可以得到$\gamma < 60^\circ$，此时$\sin \gamma < \frac{1}{2}$。
由于$\alpha$ 和$\beta$ 的余弦值都小于$\frac{1}{2}$，因此三个值中不可能有大于$\frac{1}{2}$ 的值。
4. 如果三个角都大于$60^\circ$，显然不符合题意。 \newline综上所述，当有一个角大于$60^\circ$ 时，
大于$\frac{1}{2}$ 的个数的最大值是2。
答案是C
正方体$A B C D-A_{1} B_{1} C_{1} D_{1}$ 中, $B B_{1}$ 与平面$A C D_{1}$ 所成角的余弦值为( )
从以下选项中选择: :\newline(A) $\frac{\sqrt{2}}{3}$ :\newline(B) $\frac{\sqrt{3}}{3}$ :\newline(C) 
$\frac{2}{3}$ :\newline(D) $\frac{\sqrt{6}}{3}$
设上下底面的中心分别为$\mathrm{O}_{1}, \mathrm{O}$, 设正方体的棱长等于1 , 则$O_{1} O$ 与平面
$A C D_{1}$ 所成角就是$B B_{1}$ 与平面$A C D_{1}$ 所成角, 即$\angle O_{1} O D_{1}$, 直角三角形
$\mathrm{OO}_{1} \mathrm{D}_{1}$ 中, $\cos \angle \mathrm{O}_{1} 
\mathrm{OD}_{1}=\frac{\mathrm{O}_{1} 
\mathrm{O}}{\mathrm{OD}_{1}}=\frac{\frac{1}{\sqrt{6}}}{2}=\frac{\sqrt{6}}{3}$. 
答案是C
设函数$f(x)=\left\{\begin{array}{ll}1+\log _{2}(2-x), & x<1 \ 2^{x-1}, & x \geqslant 1,\end{array}\right.$ 则
$f(-2)+f\left(\log _{2} 12\right)=$ ( )
从以下选项中选择: :\newline(A) 3 :\newline(B) 6 :\newline(C) 9 :\newline(D) 12
首先，我们可以根据定义计算$f(-2)$ 和$f(\log_2 12)$：\newline$f(-2)=1+\log_2(2-(-2))=1+\log_2 4=3$
$f(\log_2 12)=2^{\log_2 12-1}=6$\newline因此，$f(-2)+f(\log_2 12)=3+6=9$。
答案是C
已知函数$f(x)=a x^{3}-3 x^{2}+1$, 若$f(x)$ 存在唯一的零点$x_{0}$, 且$x_{0}>$ 0 , 则实数
$\mathrm{a}$ 的取值范围是( )
从以下选项中选择: :\newline(A) $(1,+\infty)$ :\newline(B) $(2,+\infty)$ :\newline(C) $(-\infty,-1)$ :\newline(D) 
$(-\infty,-2)$
首先，我们可以通过求出函数的导函数$f'(x)$ 来判断函数在$x>0$ 区间内的单调性。在这里，我们求出
导函数$f'(x)$ 为$f'(x)=3ax^2-6x$。\newline然后，我们需要求出导函数$f'(x)$ 的零点，以确定函数$f(x)$ 
在$x>0$ 区间内的单调性。导函数$f'(x)$ 的零点为$x=0$ 和$x=\frac{2}{\sqrt{a}}$。注意到$x>0$，所以
我们得到$a<0$。此外，由于函数$f(x)$ 在$x=0$ 处的函数值为$1$，因此不能有$a=\frac{4}{3}$。
\newline综上所述，当$a$ 的取值范围为$a<-\frac{4}{3}$ 时，函数$f(x)$ 在$x>0$ 区间内是单调递减的，
此时存在唯一的零点$x_0$。因此，答案为$(-\infty,-2)$。
答案是D
设$\left\{a_{n}\right\}$ 是公差不为0 的无穷等差数列, 则“ $\left\{a_{n}\right\}$ 为递增数列”是“存在正
整数$N_{0}$, 当$n>N_{0}$ 时, $a_{n}>0$ ”的( )
从以下选项中选择: :\newline(A) 充分而不必要条件:\newline(B) 必要而不充分条件:\newline(C) 充分必要条
件:\newline(D) 既不充分也不必要条件
首先，我们可以通过举例来判断该条件是充分还是必要条件。如果一个数列递增，那么它的公差一定大
于0，也就是存在正整数$N_{0}$，当$n>N_{0}$ 时，$a_{n}>0$。因此，“ $\left\{a_{n}\right\}$ 为递增
数列”是“存在正整数$N_{0}$, 当$n>N_{0}$ 时, $a_{n}>0$ ”的必要条件。\newline接下来，我们需要判
断是否充分。也就是说，如果存在正整数$N_{0}$，当$n>N_{0}$ 时，$a_{n}>0$，那么能否得出
“ $\left\{a_{n}\right\}$ 为递增数列”这一结论。答案是肯定的。因为如果$a_{n}>0$，那么$a_{n+1}-
a_{n}>0$，即公差大于0，因此该数列是递增的。因此，该条件是充分条件。\newline综上所述，选项为
(C) 充分必要条件。
答案是C
{question}
Figure 14: The prompt used in evaluating the multiple-choice problems in GaoKao on the instruct
models.
39

```
