---
title: "SWE Dev 2506.07636"
source_pdf: "AI Labs/Zhipu AI/Papers/SWE-Dev_2506.07636.pdf"
company: "Zhipu AI"
pages: 20
extracted_at: "2026-01-31T17:32:40.318596"
type: "ai_lab_paper"
---

# SWE Dev 2506.07636

**Company/Lab:** Zhipu AI
**Source PDF:** AI Labs/Zhipu AI/Papers/SWE-Dev_2506.07636.pdf
**Total Pages:** 20

---

## Content

```
--- Page 1 ---

arXiv:2506.07636v2  [cs.AI]  23 Jun 2025
SWE-Dev: Building Software Engineering Agents with Training and
Inference Scaling
Haoran Wang1∗, Zhenyu Hou1∗, Yao Wei2, Jie Tang1, Yuxiao Dong1
1Tsinghua University
2Zhipu AI
Code
Models & Data
Abstract
Large language models (LLMs) have advanced
rapidly from conversational problem solving
to addressing real-world tasks involving tool
use, such as software engineering (SWE). Re-
cent LLM-powered SWE systems, such as Ope-
nAI Codex and Cursor, have offered end-to-end
automation of the software development pro-
cess. However, building effective SWE agents
remains challenging due to the lack of high-
quality training data and reliable test-time eval-
uation. To address this issue, we present SWE-
DEV, an SWE agent built upon open-source
LLMs, with a focus on training and inference
scaling. For training scaling, we develop a
robust pipeline to synthesize test cases and
scale up agent trajectories to construct the train-
ing data. For inference scaling, we increase
the interaction budget within a single run to
enable further thinking within one indepen-
dent attempt. Experiments on the SWE-bench-
Verified benchmark show that the SWE-DEV
models can achieve top performance among
all open SWE agents.
Specifically, the re-
solve rate of our 7B and 32B models reach
23.4% and 36.6%, respectively, outperforming
state-of-the-art open-source models. All code,
models, and datasets are publicly available at
https://github.com/THUDM/SWE-Dev.
1
Introduction
Large language models (LLMs) have rapidly
evolved from generating simple code snippets to
tackling more complex tasks, such as competitive
programming (Li et al., 2022; OpenAI, 2025), ma-
chine learning problems (Chan et al., 2024), and
real-world software engineering (SWE) tasks (Xi
et al., 2024; Jimenez et al., 2024; Zan et al., 2025;
Lyu et al., 2023). Among these tasks, SWE is
particularly hard and challenging (OpenAI, 2025;
Cursor, 2024), but highly useful for improving real-
world productivity. Unlike simple code generation,
*Work partially done when interned at Zhipu AI.
0
5
10
15
20
25
30
35
Resolve Rate(%)
GPT-4o
1.6
22.8
23.4
6.6
34.0
36.6
SWE-Dev-7B
SWE-Dev-32B
  Baseline
+Finetune
+Inference
  Scaling
Figure 1: The SWE-DEV performance with training
and inference scaling. Notably, SWE-Dev-32B achieves
a resolve rate of 34.0%, matching the performance of
GPT-4o even without inference scaling.
SWE tasks usually require LLMs to interact with
complex and fragile runtime environments, solve
toolchain issues, execute scripts, and reason over
large, interdependent codebases (Ma et al., 2024b).
The SWE tasks are usually evaluated on bench-
marks such as SWE-bench (Jimenez et al., 2024)
and its recent multimodal extensions (Yang et al.,
2024b; Zan et al., 2025). These benchmarks re-
quire models to generate verifiable, test-passing
solutions on real-world codebases. To achieve this,
the models must be capable of step-by-step reason-
ing, tool using, and long-horizon planning.
To date, training models to handle these tasks
requires reliable reward signals, typically derived
from test cases that validate the correctness of the
solutions. However, most existing datasets lack
such test cases or executable environments (Chen
et al., 2021; Lyu et al., 2024), making it difficult
to evaluate solutions or provide useful feedback
during training.
This deficiency limits models’
abilities to iteratively refine their outputs through
trial-and-error, thus constraining their potential to
solve real-world SWE tasks that need grounded,
verifiable solutions.
To address this issue, we introduce SWE-DEV,

--- Page 2 ---

an open-source SWE agent framework coupled
with a scalable test case generation pipeline. This
pipeline works in two-stages: First, the LLMs
are used to generate Gherkin-style descriptions—a
structured natural language format used to specify
test scenarios. Second, a code generator outputs
code patches for further validation. Empirical anal-
ysis shows that these synthesized test cases align
closely with the original problem semantics.
Through large-scale experiments, we identify a
clear training scaling trend: increasing the num-
ber of sampled agent trajectories leads to improved
downstream performance. To enhance efficiency,
we propose an LLM-based filtering method that
selects high-quality trajectories. This allows us to
maintain the benefits of a full dataset while retain-
ing only the most valuable data.
We also propose iteration scaling—a simple yet
effective strategy that aims to scale up inference
budget by increasing the number of interaction
rounds during a single evaluation episode. This
reduces the need for repeated re-evaluation, mak-
ing it particularly advantageous in scenarios where
access to test oracles is expensive or delayed.
In addition, we explore advanced post-training
strategies, including Rejection Sampling Fine-
Tuning (RFT) (Yuan et al., 2023), KTO (Ethayarajh
et al., 2024), and OREO (Wang et al., 2024a). We
observe that RFT brings the most significant perfor-
mance improvement, while offline reinforcement
learning (RL) methods—KTO and OREO—deliver
marginal or task-specific gains.
We build SWE-DEV based on the open
Qwen2.5-Coder
(Hui
et
al.,
2024),
Llama-
3.1 (Llama, 2024), and GLM4-9B (GLM, 2024)
models. Its performance is evaluated on the SWE-
bench-Verified benchmark, with results shown in
Figure 1. With the Qwen2.5-Coder-32B model,
SWE-Dev achieves a resolve rate of 36.6% on
SWE-Bench-Verified, representing state-of-the-art
performance among open-source SWE agents.
1. Test Case Generation Pipeline. We build a
scalable LLM-based pipeline to generate real-
world SWE instances and their executable test
cases. Through this pipeline, we successfully
construct 2,000 test cases by filtering 38,000
high-quality issues across 4,000 repositories.
2. Scaling Trends in Data and Inference. We
empirically identify scaling trends between
training data volume, number of interaction
steps, and model performance.
We find
that the SWE-Dev-32B model improves from
34.0% to 36.6% resolve rate by adding 45
more interaction turns, highlighting the bene-
fit of multi-step execution for agents.
3. Post-Training Recipe for SWE Agents. We
examine several post-training methods, includ-
ing RFT, KTO, and OREO, as well as hy-
brid combinations. RFT consistently outper-
forms others by effectively leveraging high-
quality samples, demonstrating its robustness
and scalability for training SWE agents.
2
Related Works
SWE Dataset Construction.
Prior benchmarks
like SWE-bench (Jimenez et al., 2024), DevE-
val (Li et al., 2024b), EvoCodeBench (Li et al.,
2024a) and Commit0 (Zhao et al., 2024) crawl
from a large dataset and manually annotate the de-
sired instance, which is labor consuming. There
are works trying to filter existing fail-to-pass test
cases like SWE-Gym (Pan et al., 2024), which an-
notates 2.4k instances by hand. Filtering out from
a large dataset (Golubev et al., 2024) is effective
but will leave out many useful issues only because
the corresponding PR does not contain test cases.
Therefore, automatically generating test cases from
issue descriptions becomes essential.
SWE Agentic Framework.
SWE agent frame-
work focuses on two mainstream types: Interaction-
based frameworks and pipeline-based frame-
works. Interaction-based frameworks like Open-
Hands (Wang et al., 2024c), SWE-Agent (Yang
et al., 2024a), Learn-By-Interact (Su et al., 2025)
and Wang et al. (2024b) usually pre-define a set
of agent-computer interfaces (ACIs) to help model
manipulate the environment. Meanwhile, pipeline-
based frameworks will design the whole process
into several steps, like Agentless (Xia et al., 2024),
CoreR (Chen et al., 2024), MarsCode (Liu et al.,
2024) and SuperCoder2.0 (Gautam et al., 2024).
The agent will generate patches by employing fault
localization, patch generation and major voting.
There are also techniques during inference time like
MCTS (Antoniades et al., 2024) and critic-guided
generation (Badertdinov et al., 2024) and model as-
sembly (Zhang et al., 2024a). While pipeline-based
process may benefit from specification, it cannot
generalize to other coding tasks. On the contrary,

--- Page 3 ---

Gherkin
Feature: 
Run with...
Scenario: 
Given; Then; And...
Repo Info
Extraction
Description
Generation
Test Case
Generation
[Revision from Traceback]
fail-to-pass
Test Cases
diff --git 
a/test_swedev.py 
b/test_swedev.py
... 
@@ -0,0 +1,5 @@
+import pytest
+def test_zero ():
+  assert fn(1) == 0
The error
seems to be
raised by...
Statement
PR Patch
Related Files
👨💻‍
👩🏫‍
👩🏫‍
👨💻‍
Figure 2: Pipeline for test case generation, divided into description generation and code generation phases. The
pipeline begins with extracting repository information, followed by generating Gherkin scenarios and then detailed
test cases. An optional revision step leverages traceback errors to refine the generated test cases. The final output
includes fail-to-pass test cases.
interaction-based frameworks can do general tasks
with natural language as instruction.
3
SWE-Dev: Building Software Tasks at
Scale
In this part, we developed a systematic strategy to
build software tasks at scale. The core of SWE-
DEV is to collect repositories and task instances
at scale and then develop a LLM-based automated
test-case generation approach. This scalable ap-
proach enables us to construct comprehensive train-
ing datasets for SWE tasks and enhance perfor-
mance through test case-driven trajectory sam-
pling as Figure 2 shows. Based on the systematic
pipeline for scalable dataset construction and tra-
jectory optimization, we build SWE-Dev agents.
3.1
Instance Collection
We began by crawling metadata for 240k PyPI
packages containing GitHub URLs, filtering for
repositories with Stars ≥5 and PRs ≥3, resulting
in a subset of 59k repositories. Due to network con-
straints, machine capacity and intricate dependency
management, we successfully downloaded 10,416
repositories. Following the methodology outlined
in Jimenez et al. (2024) with minor modifications,
we extracted 88k instances in total.
To refine this dataset, we applied rule-based fil-
tering to adjust patch lengths to fit model context
windows and eliminated trivial or irrelevant issues
while maintaining diversity. Ultimately, we re-
0
5
10
15
20
25
# Repos
0
500
1000
1500
2000
2500
3000
# Occurrences
Figure 3: Distribution of instances per repository in the
training dataset. The majority of repositories contribute
fewer than five instances, highlighting the dataset’s di-
versity across a wide range of repositories.
tained 38k instances from 4,413 repositories as
the training set. As shown in Figure 3, over 4,000
repositories contain fewer than five instances, sig-
nificantly enhancing the dataset’s diversity.
3.2
Automatic Test Case Generation
While it is relatively straightforward to crawl PRs
containing golden patches from the Internet, these
patches often lack corresponding test cases. This
absence prevents the validation of trajectory cor-
rectness and makes reinforcement learning tech-
niques infeasible. To address this, we leveraged
LLMs to generate test cases with necessary context.
In detail, our test case generation pipeline con-
sists of four steps. The process begins with ex-
tracting relevant information from the codebase,

--- Page 4 ---

including contextual code snippets and metadata,
which serve as the foundation for subsequent steps.
Next, the extracted information is used for gener-
ating Gherkin descriptions, where the model pro-
duces structured, high-level scenarios. These de-
scriptions adopt the Gherkin syntax, using special
keywords to provide structure and meaning, mak-
ing the scenarios concise and easily interpretable.
Following this, the descriptions are utilized for the
generation of test cases, which leverages the con-
textual details to create robust and meaningful test
cases. After, the generated test case can undergo an
optional revision phase, where they are reviewed
and refined to ensure correctness.
This phased approach reflects the inherent struc-
ture of how LLMs generate test cases. The model
extracts a scenario from the provided context and,
using the code snippet as a reference, produces the
corresponding test case. Merging the first three
steps into a one often results in irrelevant or in-
coherent test cases. By introducing fine-grained
instructions, we provide clearer guidance, signifi-
cantly improving the accuracy and contextual rele-
vance of the generated outputs.
Due to computing budget, we split part of the
dataset to synthesize test cases. From a dataset
of 26k instances, we generated 2,097 fail-to-pass
functions. Additionally, we integrated existing test
cases from our dataset, resulting in a total of 4,630
test cases. Notably, most unsuccessful instances in
our approach are due to environmental constraints
rather than fundamental limitations of the method-
ology, further underscoring the feasibility of gener-
ating test cases via our approach.
3.3
Dataset Statistics
To evaluate the quality of our constructed dataset,
we conducted three experiments: (1) pass rate
analysis between description and code synthesis
(2) comparison of filtered issues with open-source
datasets (3) validation of test cases. Together, these
experiments highlight the strengths of our dataset
in generating high-quality test cases and its utility
for downstream tasks.
These experiments collectively highlight the
strengths of our dataset in generating high-quality
test cases and its utility for downstream tasks.
Pass Rate Analysis Between Description and
Code Synthesis.
As shown in Table 1, we evalu-
ated several models and a mixed approach that com-
bines Llama for description generation and Qwen-
Coder (trained primarily on code data) for code
synthesis. The mixed approach significantly out-
performed individual models in generating fail-to-
pass (F2P) functions and instances with test cases,
highlighting the importance of leveraging domain-
specific strengths for each task.
Model
#w/test
F2P
F2F
#w/F2P
Llama
757
185
1273
73
Mistral
767
151
990
81
Qwen
793
190
1185
83
Mix
828
237
1408
92
Table 1: Model Comparison for Test Case Synthesis.
#w/test and #w/F2P denote the number of instances with
test cases and with F2P test cases respectively. Models
include Llama-3.1-70B-Instruct, Qwen-2.5-Coder-32B-
Instruct, and Mistral-Large-Instruct-2407. F2P and F2F
represent the total test functions generated during syn-
thesis. The Mix model uses Llama for description gen-
eration and Qwen for code generation.
Comparison with Open-Source Datasets.
We
further validated the quality of our generated test
cases by comparing models trained on issues from
different datasets. As shown in Table 2, the in-
clusion of our generated test cases achieves quality
comparable to existing open-source dataset (Badert-
dinov et al., 2024).
Dataset
Resolve Rate
Nebius/SWE-bench-extra
15.0
SWE-Gym/SWE-Gym
13.8
SWE-Dev (kept)
15.4
SWE-Dev (filtered)
12.4
Table 2: Performance Comparison Across Different
Training Datasets.
All trajectories are unevaluated.
SWE-Dev (kept) refers to prompts retained after filter-
ing, while SWE-Dev (filtered) corresponds to discarded
prompts. Random means randomly selecting from tra-
jectory pool.
Validation of LLM-Generated Test Cases.
We
compared the effectiveness of our dataset with
other widely-used datasets, such as Nebius/SWE-
bench-extra. As shown in Table 3, models trained
on our dataset achieve comparable or slightly better
performance than those trained on Nebius.
Using 900 trajectories for rejection sampling
fine-tuning, models trained on Nebius achieved
a slightly higher mean accuracy of 15.80, while our
dataset achieved 15.87. Even with 500 trajectories,

--- Page 5 ---

Model
900-RFT
500-RFT
Nebius
15.80
14.87
SWE-Dev
15.87
15.00
Random
14.67
13.87
Table 3: Performance of RFT across different datasets.
We choose a 7B base model with 13.6% resolve rate.
k-RFT denotes fine-tuning with k correct trajectories.
Random means sampling randomly from our pool. Each
configuration was independently run three times.
our dataset remained competitive with a mean ac-
curacy of 15.00 compared to Nebius’s 14.87. This
demonstrates that our custom test cases are also
effective in verifying whether trajectories comply
with the requirement from issues.
By integrating fine-grained description genera-
tion, code generation, and execution-based valida-
tion, we ensure that the generated test cases are
both accurate and contextually relevant. This ap-
proach not only bridges the gap of missing test
cases in PR data but also significantly enhances the
dataset’s utility for downstream training tasks.
4
Experiments
In this section, we will introduce our experiments
on SWE agent tuning. As Table 4 shows, our
models achieve state-of-the-art results among open-
source models, with SWE-Dev-32B achieving a
36.6% resolve rate, increasing 30% resolve rate
compared to our base model. Furthermore, SWE-
DEV demonstrate competitive performance against
closed-source models, narrowing the gap with lead-
ing systems such as OpenHands + CodeAct v2.1.
These results highlight the effectiveness of our
pipeline and training strategies.
We focus here on reporting key results from stan-
dard fine-tuning and reinforcement learning work-
flows. The impact of training and inference scaling
will be discussed in the following section.
4.1
Experiment Setup
Dataset and Agentic Scaffold.
We utilize the
DeepSeek-V3 (DeepSeek-AI, 2024) for trajec-
tory generation from both the Nebius and SWE-
Dev datasets, and we take OpenHands, a ReAct-
like (Yao et al., 2023) framework. After sampling,
we obtained 17k unevaluated trajectories and 2.3k
correct trajectories. Specifically, 914 of the correct
trajectories originate from Nebius, while 78% of
the unevaluated trajectories are derived from SWE-
DEV. For the OpenHands configuration, we set
iteration=30 and max_tokens=32k. During of-
fline RL training, we incorporate trajectories from
DeepSeek-V3 and on-policy models.
Training Configuration.
We adopt the Qwen-
2.5-Coder (Hui et al., 2024), Llama-3.1 (Llama,
2024) and GLM-4 (GLM, 2024) series as our base
models and leverage the OpenRLHF (Hu et al.,
2024) framework for training. For datasets with ≤
10k samples, we use a learning rate of 1e-5 and a
batch size of 32; for larger datasets, we maintain
the same learning rate but increase the batch size to
64. The training process spans 4 epochs for the 7B
model and 8 epochs for the 32B model. To enable
long-context training, we apply ring-attention (Liu
et al., 2023) with 8 heads.
Evaluation Metrics
For evaluation, we employ
SWE-bench-Verified, a human-validated subset of
500 instances curated by OpenAI. This benchmark
is carefully selected from SWE-bench (Jimenez
et al., 2024), ensuring high-quality evaluation.
Model-generated code patches are assessed using
developer-written unit tests, with accuracy defined
as the percentage of successfully resolved instances.
For all experiments, we set iteration=30 and
max_tokens=32k, except for inference scaling ex-
periments, where max_tokens=160k is used.
4.2
Main Results
Table 4 presents the comparison of resolve rates
on the SWE-bench-Verified benchmark. We eval-
uate two major approaches: methods leveraging
fine-tuning of open-source models and the direct
utilization of proprietary models.
Compared to existing methods based on fine-
tuning open-source models, SWE-DEV achieves
the highest performance without employing any
verifiers or sampling strategies. SWE-Dev-32B
outperforms approaches SWE-Syninfer-72B (Ma
et al., 2024a) and SWE-Fixer-72B (Xie et al., 2025)
which have a resolve rate of 36.6%, achieving a
6.4% improvement while using fewer parameters.
With comparable model parameters, SWE-DEV
significantly outperforms SWE-Gym (Pan et al.,
2024) and SWE-Syninfer by over 12.8% and 5.2%.
Furthermore, by fine-tuning an open-source
model that is substantially inferior to proprietary
models, our method achieves an impressive 3.4%
performance improvement over GPT-4o (OpenAI,
2025) on the SWE-bench-Verified benchmark.
Moreover, this approach demonstrates significant

--- Page 6 ---

Method
Framework
Model
Resolve Rate
Proprietary Models
OpenAI-GPT-4o (OpenAI, 2024a)
Pipeline
GPT-4o
33.2%
OpenAI-o1-preview (OpenAI, 2024c)
Pipeline
OpenAI-o1-preview
41.3%
OpenAI-o1 (OpenAI, 2024c)
Pipeline
OpenAI-o1
48.9%
Moatless Tools (Örwall, 2024)
Moatless Tools
claude-3-5-sonnet-20241022
39.0%
AutoCodeRover (Zhang et al., 2024b)
AutoCodeRover
GPT-4o (2024-05-13)
38.4%
AutoCodeRover v2.0 (Zhang et al., 2024b)
AutoCodeRover
claude-3-5-sonnet-20241022
46.2%
Agentless-1.5 (Xia et al., 2024)
Agentless
GPT-4o (2024-05-13)
38.8%
Agentless-1.5 (Xia et al., 2024)
Agentless
claude-3-5-sonnet-20241022
50.8%
OpenHands + CodeAct v2.1 (Wang et al., 2024b)
OpenHands
claude-3-5-sonnet-20241022
53.0%
Open-source Models
SWE-Llama-13B (Jimenez et al., 2024)
RAG
Code Llama-13B
1.2%
SWE-Gym-7B (Pan et al., 2024)
OpenHands
Qwen2.5-Coder-7B-Instruct
10.6%
SWE-Dev-9B(Ours)
OpenHands
GLM-4-9b-chat
13.6%(↑12.0%)
SWE-Dev-8B(Ours)
OpenHands
Llama-3.1-8B-Instruct
18.0%(↑16.8%)
SWE-SynInfer-7B (Ma et al., 2024a)
Agentless
Qwen2.5-Coder-7B
18.2%
SWE-Dev-7B(Ours)
OpenHands
Qwen2.5-Coder-7B-Instruct
23.4%(↑21.6%)
SWE-Gym-32B (Pan et al., 2024)
OpenHands
Qwen2.5-Coder-32B-Instruct
20.6%
SWE-SynInfer-72B (Ma et al., 2024a)
Agentless
Qwen2.5-72B-Instruct
30.2%
SWE-Fixer-72B* (Xie et al., 2025)
Agentless
Qwen2.5-72B
32.8%
SWE-Dev-32B(Ours)
OpenHands
Qwen2.5-Coder-32B-Instruct
36.6%(↑30%)
Table 4: Comparison of resolve rates on the SWE-bench-Verified dataset. The table categorizes models into
baselines and SWE agents, showcasing their performance. SWE-Dev models attain top-tier results within the realm
of open-source models and concurrently exhibit robust performance among closed-source models. The relative
improvement (↑) for our models is calculated with respect to their respective base models.
progress in effectively addressing complex SWE
tasks with open-source models.
4.3
Agentic Post-Training Optimization
Comparison of Training Methods.
To further
enhance model performance, we leveraged in-
stances with fail-to-pass test cases to investigate
rejection sampling fine-tuning as Chen et al. (2023)
and Zeng et al. (2023), with two offline RL meth-
ods: KTO and OREO. Our findings, as illustrated
in Figure 4, demonstrate the significant advantages
and limitations of these techniques.
With only 1,000 trajectories, rejection sampling
achieves a 16.2% resolve rate, surpassing the per-
formance of a larger-scale unfiltered dataset. As the
number of trajectories increases, rejection sampling
further narrows the performance gap, reaching an
18.0% resolve rate with 2,000 trajectories. This ap-
proach is valuable in scenarios where training data
is costly or computational resources are limited.
We also evaluated two offline RL methods:
OREO and KTO. For both methods, positive exam-
ples are derived from DeepSeek-V3, and negative
examples are sampled from a mixture of DeepSeek-
500
1000
1500
18002000
2300
# Trajectories
15
16
17
18
19
Resolve Rate (%)
RFT
KTO
OREO
Random
Figure 4: Model performance across different training
methods. Random denotes supervised fine-tuning with
pass@1 trajectories. Other experimental settings remain
consistent with those described above.

--- Page 7 ---

V3 and on-policy outputs. Despite their theoretical
potential, these offline methods demonstrated lim-
ited performance improvements compared to RFT.
OREO showed small but consistent gains over
random sampling, achieving a 17.0% resolve rate
with 1,800 trajectories. However, its performance
remained below that of RFT. KTO performed
slightly better than OREO, achieving a 17.2% re-
solve rate with 1,800 trajectories. While KTO
marginally outperformed OREO, it still lagged be-
hind RFT in overall effectiveness.
The relatively modest improvements observed
with offline RL methods suggest that their reliance
on on-policy negative examples and off-policy pos-
itive examples may limit their efficacy. On-policy
negatives could introduce noise, while the positive
examples might lack sufficient diversity to drive
meaningful policy optimization.
Hybrid Training with RFT+OREO.
To further
explore the potential of combining different train-
ing strategies, we conducted hybrid training experi-
ments by integrating RFT and OREO. Specifically,
we divided the 2.3k deduplicated correct trajecto-
ries into two complementary subsets: one portion
was allocated to RFT, while the remaining data was
utilized for OREO, ensuring an efficient use of the
available training data.
Importantly, in each run, the RFT+OREO hybrid
approach utilized the entire training set, ensuring
that the total amount of data seen by the hybrid
model matched the full dataset. For comparison,
the Random baseline was trained with the same
number of pass@1 trajectories as RFT, while other
experimental settings were kept consistent. The
results are presented in Figure 5.
The RFT-only approach consistently outper-
formed all other configurations, achieving the high-
est resolve rate across all subsets. With 2300 RFT
trajectories, the model achieved a resolve rate of
21.2%, surpassing all hybrid and OREO-only con-
figurations. This highlights RFT’s strong ability to
utilize high-quality data to maximize performance.
5
Scaling SWE Agents via Training and
Inference Expansion
We explore how SWE agent performance scales
along two critical dimensions: the amount of train-
ing data and the compute budget. Our findings re-
veal consistent trends aligned with established scal-
ing laws, and shed light on the cost–performance
trade-offs in agent-based settings.
0
500
1000
1500
2000
2300
# Trajectories
12
14
16
18
20
22
Resolve Rate (%)
RFT+OREO
RFT
Random
Figure 5: Model performance with hybrid training. In
each run, RFT is applied to a subset of the data (mea-
sured in trajectories), followed by OREO training on
the remaining data. The Random baseline uses the same
number of pass@1 trajectories as RFT.
5.1
Training Data Scaling
To investigate the impact of data size on model
performance, we conducted a scaling analysis by
progressively increasing the number of training
trajectories. Notably, we filtered trajectories that
did not terminate at the given iterations, ensuring
that the remaining trajectories were unevaluated.
As illustrated in Figure 6, the model’s accuracy
increases steadily with the logarithm of the data
size, following a near-linear trend in log-log space.
For instance, the 7B model achieved 13.0% accu-
racy with only 574 trajectories. When the data size
was scaled up to 16,639 trajectories, the accuracy
improved significantly to 22.8%.
This trend underscores a strong correlation be-
tween the quantity of training data and the model’s
generalizable ability. The observed linearity in
the curve suggests that the model efficiently lever-
ages additional data without exhibiting saturation
within the explored range. These findings align
with established scaling laws reported in Kaplan
et al. (2020) and Hou et al. (2024), where perfor-
mance predictably improves with increased data
size, particularly in the low-data regime.
Moreover, we observe that the benefits of data
scaling are more pronounced for larger models.
The 32B model shows a sharper improvement com-
pared to the 7B model, suggesting that larger capac-
ity enables more efficient utilization of the avail-
able data. This observation echoes prior findings in
model scaling literature, where overparameterized
models can extract richer inductive biases from
limited supervision.
We further applied a filtering strategy to the train-
ing trajectories to enhance data quality. Specifi-
cally, we evaluated the model-generated patches

--- Page 8 ---

28
29
210
211
212
214
# Trajectories (log2)
12
14
16
18
20
22
24
Resolve Rate (%)
13.0
15.0
18.4
19.2
22.8
12.6
15.2
18.0
18.8
7B wo/filter
7B w/filter
29
210
212
213
214
# Trajectories (log2)
27
28
29
30
31
32
33
34
35
Resolve Rate (%)
28.2
29.4
30.6
32.0
34.0
32B wo/filter
Figure 6: Resolve rates across different training data sizes. Both 7B and 32B models exhibit performance
improvements with increased training trajectories.
30
45
60
75
# Iteration
21.0
21.5
22.0
22.5
23.0
23.5
24.0
Resolve Rate (%)
21.8
22.2
22.6
23.4
SWE-Dev-7B
30
45
60
75
# Iteration
33
34
35
36
37
Resolve Rate (%)
34.0
34.6
35.4
36.6
SWE-Dev-32B
Figure 7: Resolve rates across different numbers of interaction rounds (30–75). Larger models benefit more
significantly from extended iteration scaling, though diminishing returns are observed at higher rounds.
against reference patches using an LLM-based
comparison (Llama 3.1-70B-Instruct). The outputs
were categorized into four groups: identical, mostly
identical, partially identical, and different. Only
trajectories labeled as identical or mostly identical
were retained, preserving approximately 65% of
the original trajectories.
As shown in Figure 6, the filtered dataset
achieves nearly identical performance to the un-
filtered dataset, despite a significant reduction in
training data size. This demonstrates that removing
low-quality or irrelevant training samples like stuck
in environment setup has minimal impact on model
performance, as the retained data is of sufficiently
high quality to offset the reduction in quantity.
5.2
Inference Time Scaling
In addition to training data scaling, inference-time
decisions also play a crucial role in overall model
capability. In agent-based tasks, determining an
appropriate compute budget is crucial for balanc-
ing task success and resource efficiency (Brown
et al., 2024). Existing works also demonstrate that
increasing test-time compute leads to better perfor-
mance in math reasoning tasks (OpenAI, 2024b;
Hou et al., 2025). Traditional evaluation metrics,
such as pass@k, typically focus on multiple inde-
pendent attempts, which may cost to a large com-
puting budget for SWE evaluation. To address
this, we investigate the impact of iteration scal-
ing—progressively increasing the number of inter-
action rounds within a single run. This approach
provides a more natural and efficient alignment
with the iterative reasoning inherent in these tasks.
In this experiment, we directly change the RoPE
embedding from 32k to 160k and observed that
the resolve rate of the 7B model dropped from
22.8% to 21.8%, while the 32B model showed
no significant decline. The results, presented in
Figure 7, demonstrate how resolve rate improves
as the number of interaction rounds increases. We
compare two configurations: SWE-Dev-32B, and
SWE-Dev-7B. Our key findings include:
Consistent Improvement with Iteration Scaling.
For all models, increasing the number of interaction
rounds leads to higher resolve rate. For instance,
SWE-Dev-32B achieves 34.0% at 30 rounds and

--- Page 9 ---

36.6% at 75 rounds. This demonstrates that ad-
ditional iterations allow the models to refine their
reasoning and correct prior errors, effectively lever-
aging the iterative interaction process.
Diminishing Returns Beyond a Threshold.
Al-
though the resolve rate increases with additional
interaction rounds, the rate of improvement dimin-
ishes over time. For instance, the improvement
observed between 30 and 45 rounds is significantly
more pronounced than that between 45 and 75
rounds across all models. This suggests a prac-
tical upper limit to the benefits of iteration scaling,
beyond which additional rounds yield minimal per-
formance gains. These diminishing returns high-
light the importance of calibrating iteration limits to
balance computational costs with improvements.
6
Conclusion
In this work, we introduce SWE-DEV, an open-
source SWE agent equipped with a robust test case
construction pipeline. We further investigate the
impact of techniques such as rejection sampling
and offline RL methods, while proposing iteration
scaling as a novel approach to enhance inference-
time performance. Our models are evaluated on the
SWE-bench-Verified benchmark, achieving state-
of-the-art results among open-source agents, with
performance scores of 23.4% for the 7B model and
36.6% for the 32B model.
Our work provides a strong foundation for ad-
vancing SWE-focused LLM research by introduc-
ing an open-source model, and a comprehensive
data generation pipeline. We hope these contri-
butions inspire further innovation in developing
robust, scalable, and efficient SWE agents capable
of addressing real-world SWE challenges.
7
Limitation
While offline RL have shown promise, there is
significant room for optimization. Incorporating
online RL approaches, such as ArCHer (Zhou et al.,
2024), DigiRL (Bai et al., 2024), and WebRL (Qi
et al., 2025), could further enhance performance
by leveraging interaction-based frameworks and
dynamic task environments (Snell et al., 2023). Fu-
ture research could explore adaptive iteration strate-
gies, where the number of rounds is dynamically
adjusted based on task complexity or intermediate
progress. Hybrid approaches that combine iter-
ation scaling with other optimization techniques
may also improve performance while maintaining
computational efficiency.
Acknowledgment.
This work has been sup-
ported by the Natural Science Foundation of China
(NSFC) 62276148, Tsinghua University (Depart-
ment of Computer Science and Technology) -
Siemens Ltd., China Joint Research Center for In-
dustrial Intelligence and Internet of Things (JCI-
IOT), and the New Cornerstone Science Founda-
tion through the XPLORER PRIZE. The GPU com-
pute used in this work is sponsored by Zhipu AI.
The corresponding author: Yuxiao Dong (yuxi-
aod@tsinghua.edu.cn).
References
Antonis Antoniades, Albert Örwall, Kexun Zhang,
Yuxi Xie, Anirudh Goyal, and William Wang. 2024.
Swe-search: Enhancing software agents with monte
carlo tree search and iterative refinement. Preprint,
arXiv:2410.20285.
Ibragim Badertdinov, Maria Trofimova, Yuri Anapol-
skiy, Sergey Abramov, Karina Zainullina, Alexander
Golubev, Sergey Polezhaev, Daria Litvintseva, Si-
mon Karasik, Filipp Fisin, Sergey Skvortsov, Maxim
Nekrashevich, Anton Shevtsov, and Boris Yangel.
2024. Scaling data collection for training software
engineering agents. Nebius blog.
Hao Bai, Yifei Zhou, Mert Cemri, Jiayi Pan, Alane
Suhr, Sergey Levine, and Aviral Kumar. 2024. Di-
girl:
Training in-the-wild device-control agents
with autonomous reinforcement learning. Preprint,
arXiv:2406.11896.
Bradley Brown, Jordan Juravsky, Ryan Ehrlich, Ronald
Clark, Quoc V. Le, Christopher Ré, and Azalia Mirho-
seini. 2024. Large language monkeys: Scaling in-
ference compute with repeated sampling. Preprint,
arXiv:2407.21787.
Jun Shern Chan, Neil Chowdhury, Oliver Jaffe, James
Aung, Dane Sherburn, Evan Mays, Giulio Starace,
Kevin Liu, Leon Maksin, Tejal Patwardhan, Lilian
Weng, and Aleksander M ˛adry. 2024. Mle-bench:
Evaluating machine learning agents on machine
learning engineering. Preprint, arXiv:2410.07095.
Baian Chen, Chang Shu, Ehsan Shareghi, Nigel Collier,
Karthik Narasimhan, and Shunyu Yao. 2023. Fire-
act: Toward language agent fine-tuning. Preprint,
arXiv:2310.05915.
Dong Chen, Shaoxin Lin, Muhan Zeng, Daoguang Zan,
Jian-Gang Wang, Anton Cheshkov, Jun Sun, Hao
Yu, Guoliang Dong, Artem Aliev, Jie Wang, Xiao
Cheng, Guangtai Liang, Yuchi Ma, Pan Bian, Tao
Xie, and Qianxiang Wang. 2024. Coder: Issue re-
solving with multi-agent and task graphs. Preprint,
arXiv:2406.01304.

--- Page 10 ---

Mark Chen, Jerry Tworek, Heewoo Jun, Qiming
Yuan, Henrique Ponde de Oliveira Pinto, Jared Ka-
plan, Harri Edwards, Yuri Burda, Nicholas Joseph,
Greg Brockman, Alex Ray, Raul Puri, Gretchen
Krueger, Michael Petrov, Heidy Khlaaf, Girish Sas-
try, Pamela Mishkin, Brooke Chan, Scott Gray,
Nick Ryder, Mikhail Pavlov, Alethea Power, Lukasz
Kaiser, Mohammad Bavarian, Clemens Winter,
Philippe Tillet, Felipe Petroski Such, Dave Cum-
mings, Matthias Plappert, Fotios Chantzis, Eliza-
beth Barnes, Ariel Herbert-Voss, William Hebgen
Guss, Alex Nichol, Alex Paino, Nikolas Tezak, Jie
Tang, Igor Babuschkin, Suchir Balaji, Shantanu Jain,
William Saunders, Christopher Hesse, Andrew N.
Carr, Jan Leike, Josh Achiam, Vedant Misra, Evan
Morikawa, Alec Radford, Matthew Knight, Miles
Brundage, Mira Murati, Katie Mayer, Peter Welinder,
Bob McGrew, Dario Amodei, Sam McCandlish, Ilya
Sutskever, and Wojciech Zaremba. 2021. Evaluat-
ing large language models trained on code. Preprint,
arXiv:2107.03374.
Cursor. 2024. Cursor – ai-powered code editor. https:
//www.cursor.com/cn. Accessed: 2025-05-25.
DeepSeek-AI. 2024.
Deepseek-v3 technical report.
Preprint, arXiv:2412.19437.
Kawin Ethayarajh, Winnie Xu, Niklas Muennighoff,
Dan Jurafsky, and Douwe Kiela. 2024.
Kto:
Model alignment as prospect theoretic optimization.
Preprint, arXiv:2402.01306.
Anmol Gautam, Kishore Kumar, Adarsh Jha, Mukunda
NS, and Ishaan Bhola. 2024. Supercoder2.0: Techni-
cal report on exploring the feasibility of llms as au-
tonomous programmer. Preprint, arXiv:2409.11190.
Team GLM. 2024. Chatglm: A family of large language
models from glm-130b to glm-4 all tools. Preprint,
arXiv:2406.12793.
Alexander Golubev, Sergey Polezhaev, Karina Zainul-
lina, Maria Trofimova, Ibragim Badertdinov, Yuri
Anapolskiy, Daria Litvintseva, Simon Karasik, Fil-
ipp Fisin, Sergey Skvortsov, Maxim Nekrashe-
vich, Anton Shevtsov, Sergey Abramov, and Boris
Yangel. 2024.
Leveraging training and search
for better software engineering agents.
Nebius
blog.
Https://nebius.com/blog/posts/training-and-
search-for-software-engineering-agents.
Zhenyu Hou, Pengfan Du, Yilin Niu, Zhengxiao Du,
Aohan Zeng, Xiao Liu, Minlie Huang, Hongning
Wang, Jie Tang, and Yuxiao Dong. 2024. Does rlhf
scale? exploring the impacts from data, model, and
method. arXiv preprint arXiv:2412.06000.
Zhenyu Hou, Xin Lv, Rui Lu, Jiajie Zhang, Yujiang
Li, Zijun Yao, Juanzi Li, Jie Tang, and Yuxiao Dong.
2025. Advancing language model reasoning through
reinforcement learning and inference scaling.
In
ICML.
Jian Hu, Xibin Wu, Zilin Zhu, Xianyu, Weixun Wang,
Dehao Zhang, and Yu Cao. 2024. Openrlhf: An easy-
to-use, scalable and high-performance rlhf frame-
work. Preprint, arXiv:2405.11143.
Binyuan Hui, Jian Yang, Zeyu Cui, Jiaxi Yang, Day-
iheng Liu, Lei Zhang, Tianyu Liu, Jiajun Zhang,
Bowen Yu, Keming Lu, Kai Dang, Yang Fan,
Yichang Zhang, An Yang, Rui Men, Fei Huang,
Bo Zheng, Yibo Miao, Shanghaoran Quan, Yun-
long Feng, Xingzhang Ren, Xuancheng Ren, Jingren
Zhou, and Junyang Lin. 2024. Qwen2.5-coder tech-
nical report. Preprint, arXiv:2409.12186.
Carlos E. Jimenez, John Yang, Alexander Wettig,
Shunyu Yao, Kexin Pei, Ofir Press, and Karthik
Narasimhan. 2024. Swe-bench: Can language mod-
els resolve real-world github issues?
Preprint,
arXiv:2310.06770.
Jared Kaplan, Sam McCandlish, Tom Henighan, Tom B.
Brown, Benjamin Chess, Rewon Child, Scott Gray,
Alec Radford, Jeffrey Wu, and Dario Amodei. 2020.
Scaling laws for neural language models. Preprint,
arXiv:2001.08361.
Jia Li, Ge Li, Xuanming Zhang, Yihong Dong, and
Zhi Jin. 2024a. Evocodebench: An evolving code
generation benchmark aligned with real-world code
repositories. Preprint, arXiv:2404.00599.
Jia Li, Ge Li, Yunfei Zhao, Yongmin Li, Huanyu
Liu, Hao Zhu, Lecheng Wang, Kaibo Liu, Zheng
Fang, Lanshen Wang, Jiazheng Ding, Xuanming
Zhang, Yuqi Zhu, Yihong Dong, Zhi Jin, Binhua
Li, Fei Huang, and Yongbin Li. 2024b. Deveval:
A manually-annotated code generation benchmark
aligned with real-world code repositories. Preprint,
arXiv:2405.19856.
Yujia Li, David Choi, Junyoung Chung, Nate Kushman,
Julian Schrittwieser, Rémi Leblond, Tom Eccles,
James Keeling, Felix Gimeno, Agustin Dal Lago,
Thomas Hubert, Peter Choy, Cyprien de Mas-
son d’Autume, Igor Babuschkin, Xinyun Chen, Po-
Sen Huang, Johannes Welbl, Sven Gowal, Alexey
Cherepanov, James Molloy, Daniel J. Mankowitz,
Esme Sutherland Robson, Pushmeet Kohli, Nando
de Freitas, Koray Kavukcuoglu, and Oriol Vinyals.
2022. Competition-level code generation with alpha-
code. Science, 378(6624):1092–1097.
Hao Liu, Matei Zaharia, and Pieter Abbeel. 2023.
Ring attention with blockwise transformers for near-
infinite context. Preprint, arXiv:2310.01889.
Yizhou Liu, Pengfei Gao, Xinchen Wang, Jie Liu,
Yexuan Shi, Zhao Zhang, and Chao Peng. 2024.
Marscode agent: Ai-native automated bug fixing.
Preprint, arXiv:2409.00899.
Team Llama. 2024.
The llama 3 herd of models.
Preprint, arXiv:2407.21783.
Bohan Lyu, Yadi Cao, Duncan Watson-Parris, Leon
Bergen, Taylor Berg-Kirkpatrick, and Rose Yu. 2024.

--- Page 11 ---

Adapting while learning: Grounding llms for scien-
tific problems with intelligent tool usage adaptation.
arXiv preprint arXiv:2411.00412.
Bohan Lyu, Xin Cong, Heyang Yu, Pan Yang, Yujia
Qin, Yining Ye, Yaxi Lu, Zhong Zhang, Yukun Yan,
Yankai Lin, et al. 2023. Enhancing open-domain
task-solving capability of llms via autonomous tool
integration from github. ACL (Main) 2025.
Yingwei Ma, Rongyu Cao, Yongchang Cao, Yue Zhang,
Jue Chen, Yibo Liu, Yuchen Liu, Binhua Li, Fei
Huang, and Yongbin Li. 2024a. Lingma swe-gpt: An
open development-process-centric language model
for automated software improvement.
Preprint,
arXiv:2411.00622.
Yingwei Ma, Qingping Yang, Rongyu Cao, Binhua
Li, Fei Huang, and Yongbin Li. 2024b.
How to
understand whole software repository?
Preprint,
arXiv:2406.01422.
OpenAI. 2024a. Gpt-4o system card. Accessed: 2025-
06-02.
OpenAI.
2024b.
Learning
to
reason
with
llms.
https://openai.com/index/
learning-to-reason-with-llms.
OpenAI. 2024c. Openai o1 system card. Accessed:
2025-06-02.
OpenAI. 2025. Competitive programming with large
reasoning models. Preprint, arXiv:2502.06807.
OpenAI. 2025.
Introducing codex.
https://
openai.com/index/introducing-codex/.
Ac-
cessed: 2025-05-25.
Albert Örwall. 2024. moatless-tools.
Jiayi Pan, Xingyao Wang, Graham Neubig, Navdeep
Jaitly, Heng Ji, Alane Suhr, and Yizhe Zhang. 2024.
Training software engineering agents and verifiers
with swe-gym. Preprint, arXiv:2412.21139.
Zehan Qi, Xiao Liu, Iat Long Iong, Hanyu Lai, Xueqiao
Sun, Wenyi Zhao, Yu Yang, Xinyue Yang, Jiadai Sun,
Shuntian Yao, Tianjie Zhang, Wei Xu, Jie Tang, and
Yuxiao Dong. 2025. Webrl: Training llm web agents
via self-evolving online curriculum reinforcement
learning. Preprint, arXiv:2411.02337.
Charlie Snell, Ilya Kostrikov, Yi Su, Mengjiao Yang,
and Sergey Levine. 2023. Offline rl for natural lan-
guage generation with implicit language q learning.
Preprint, arXiv:2206.11871.
Hongjin Su, Ruoxi Sun, Jinsung Yoon, Pengcheng Yin,
Tao Yu, and Sercan Ö. Arık. 2025. Learn-by-interact:
A data-centric framework for self-adaptive agents in
realistic environments. Preprint, arXiv:2501.10893.
Huaijie Wang, Shibo Hao, Hanze Dong, Shenao Zhang,
Yilin Bao, Ziran Yang, and Yi Wu. 2024a. Offline
reinforcement learning for llm multi-step reasoning.
Preprint, arXiv:2412.16145.
Xingyao Wang, Yangyi Chen, Lifan Yuan, Yizhe Zhang,
Yunzhu Li, Hao Peng, and Heng Ji. 2024b. Exe-
cutable code actions elicit better llm agents. Preprint,
arXiv:2402.01030.
Xingyao Wang, Boxuan Li, Yufan Song, Frank F. Xu,
Xiangru Tang, Mingchen Zhuge, Jiayi Pan, Yueqi
Song, Bowen Li, Jaskirat Singh, Hoang H. Tran,
Fuqiang Li, Ren Ma, Mingzhang Zheng, Bill Qian,
Yanjun Shao, Niklas Muennighoff, Yizhe Zhang,
Binyuan Hui, Junyang Lin, Robert Brennan, Hao
Peng, Heng Ji, and Graham Neubig. 2024c. Open-
hands: An open platform for ai software developers
as generalist agents. Preprint, arXiv:2407.16741.
Zhiheng Xi, Yiwen Ding, Wenxiang Chen, Boyang
Hong, Honglin Guo, Junzhe Wang, Dingwen Yang,
Chenyang Liao, Xin Guo, Wei He, Songyang Gao,
Lu Chen, Rui Zheng, Yicheng Zou, Tao Gui,
Qi Zhang, Xipeng Qiu, Xuanjing Huang, Zuxuan
Wu, and Yu-Gang Jiang. 2024. Agentgym: Evolv-
ing large language model-based agents across diverse
environments. Preprint, arXiv:2406.04151.
Chunqiu Steven Xia, Yinlin Deng, Soren Dunn, and
Lingming Zhang. 2024. Agentless: Demystifying
llm-based software engineering agents.
Preprint,
arXiv:2407.01489.
Chengxing Xie, Bowen Li, Chang Gao, He Du, Wai
Lam, Difan Zou, and Kai Chen. 2025. Swe-fixer:
Training open-source llms for effective and efficient
github issue resolution. Preprint, arXiv:2501.05040.
John Yang, Carlos E. Jimenez, Alexander Wettig, Kilian
Lieret, Shunyu Yao, Karthik Narasimhan, and Ofir
Press. 2024a. Swe-agent: Agent-computer interfaces
enable automated software engineering. Preprint,
arXiv:2405.15793.
John Yang, Carlos E. Jimenez, Alex L. Zhang, Kil-
ian Lieret, Joyce Yang, Xindi Wu, Ori Press,
Niklas Muennighoff, Gabriel Synnaeve, Karthik R.
Narasimhan, Diyi Yang, Sida I. Wang, and Ofir
Press. 2024b. Swe-bench multimodal: Do ai systems
generalize to visual software domains?
Preprint,
arXiv:2410.03859.
Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak
Shafran, Karthik Narasimhan, and Yuan Cao. 2023.
React: Synergizing reasoning and acting in language
models. Preprint, arXiv:2210.03629.
Zheng Yuan, Hongyi Yuan, Chengpeng Li, Guanting
Dong, Keming Lu, Chuanqi Tan, Chang Zhou, and
Jingren Zhou. 2023. Scaling relationship on learning
mathematical reasoning with large language models.
Preprint, arXiv:2308.01825.
Daoguang Zan, Zhirong Huang, Wei Liu, Hanwu Chen,
Linhao Zhang, Shulin Xin, Lu Chen, Qi Liu, Xiao-
jian Zhong, Aoyan Li, Siyao Liu, Yongsheng Xiao,
Liangqiang Chen, Yuyu Zhang, Jing Su, Tianyu Liu,
Rui Long, Kai Shen, and Liang Xiang. 2025. Multi-
swe-bench: A multilingual benchmark for issue re-
solving. Preprint, arXiv:2504.02605.

--- Page 12 ---

Aohan Zeng, Mingdao Liu, Rui Lu, Bowen Wang, Xiao
Liu, Yuxiao Dong, and Jie Tang. 2023. Agenttun-
ing: Enabling generalized agent abilities for llms.
Preprint, arXiv:2310.12823.
Kexun Zhang, Weiran Yao, Zuxin Liu, Yihao Feng, Zhi-
wei Liu, Rithesh Murthy, Tian Lan, Lei Li, Renze
Lou, Jiacheng Xu, Bo Pang, Yingbo Zhou, Shelby
Heinecke, Silvio Savarese, Huan Wang, and Caim-
ing Xiong. 2024a. Diversity empowers intelligence:
Integrating expertise of software engineering agents.
Preprint, arXiv:2408.07060.
Yuntong Zhang, Haifeng Ruan, Zhiyu Fan, and Abhik
Roychoudhury. 2024b. Autocoderover: Autonomous
program improvement. Preprint, arXiv:2404.05427.
Wenting Zhao, Nan Jiang, Celine Lee, Justin T Chiu,
Claire Cardie, Matthias Gallé, and Alexander M
Rush. 2024.
Commit0: Library generation from
scratch. Preprint, arXiv:2412.01769.
Yifei Zhou, Andrea Zanette, Jiayi Pan, Sergey Levine,
and Aviral Kumar. 2024. Archer: Training language
model agents via hierarchical multi-turn rl. Preprint,
arXiv:2402.19446.

--- Page 13 ---

A
Appendix
A.1
Prompt Templates
Prompt for Patch Filtering
You are a professional programmer. Given two git patches that aim to fix the same bug, your task is to analyze if the
second patch correctly fixes the bug and identify any issues in it. Please ignore any changes to reproduce_error.py
files as they are only used for debugging purposes.
Information provided:
• Patch 1 (correct solution): {patch1}
• Patch 2 (patch to evaluate): {patch2}
Guidelines:
1. When comparing patches, focus only on code changes that affect actual functionality. Differences in logging or
documentation can be ignored.
2. The evaluation levels are:
• identical: Patch 2’s functionality is exactly the same as Patch 1.
• mostly: Patch 2 implements most of the functionality correctly with minor differences.
• partially: Patch 2 only implements some of the required functionality.
• different: Patch 2’s functionality is completely different or incorrect.
3. If Patch 2 is rated as partially or mostly, please specify the functional differences in the explanation.
Final Instructions:
• Provide your analysis and judgment in the following format:
[Explanation]
Explanation of the reason why the patch is judged as ’identical’, ’mostly’, ’partially’, or ’different’.
[Judgment]
The judgment of the patch is ’identical’, ’mostly’, ’partially’, or ’different’.
Prompt for Generating Naive NL Test Case Description
You are a skilled test engineer. Your mission is to create a minimal, edge-case test scenario that rigorously validates the
effectiveness of the patch. This test case must satisfy the following conditions:
1. Fail with the unpatched code: Demonstrate the specific bug, issue, or limitation that the patch is designed to
address. Ensure the test triggers this behavior reliably and consistently.
2. Pass with the patched code: Confirm that the patch resolves the issue without introducing new problems or
regressions.
Focus Areas:
• Exercise uncommon or edge-case code paths.
• Test for boundary conditions or unexpected input.
• Mimic realistic usage scenarios where the original behavior fails.
Information provided:
• Repository name: {}
• GitHub issue description: {}
• Correction patch: {}
• Hints Text: {}
Your Task:

--- Page 14 ---

• Briefly analyze the problem description and hints text to identify where the issue lies and what should be fixed.
• Write a concise test case description that reflects the modification introduced by the patch.
• Ensure the description targets the root cause of the issue and guides the generation of a challenging, edge-case
test scenario.
Important Notes: - Avoid unrelated information or greetings. - Focus exclusively on the test case description and the
problem analysis.
Prompt for Generating Gherkin Description
You are an experienced test engineer. Your task is to write a test following the Gherkin syntax based on the information
provided below. This test must verify whether the correction patch in the repository correctly resolves the described
issue.
Key Points: - The test should fail with the unpatched code and pass with the patched code.
Information Provided:
• Repository name: {}
• GitHub issue description: {}
• Correction patch: {}
• Hints Text: {}
• Analysis for the test cases (for reference): {}
Requirements:
1. Use the Given-When-Then structure of Gherkin syntax.
2. Clearly describe:
• Preconditions (Given).
• Triggering events (When).
• Expected outcomes (Then).
3. Ensure the test logic is clear, concise, and covers all relevant scenarios.
4. Avoid including unimportant test cases, such as modifications to README files.
Instructions: - Wrap each Gherkin test description in triple backticks (“‘gherkin). - Example format:
```gherkin
{{YOUR DESCRIPTION}}
```
Prompt for Test Case Generation
You are a test engineer. Given a GitHub issue description and the golden patch, your task is to build test cases that
reproduce the error according to the patch. In detail, the test cases should reproduce the error in the issue description.
Your test case will run at the root of the project. Please be careful of the relative path to avoid path-related errors.
Information provided:
• Repository name: {}
• GitHub issue description: {}
• Hints Text: {}
• Correction patch: {}
• Project tree (file depth less than 3): {}
• Test Case Description: {}
• Relevant code segments in the original version: {}
Steps to follow:

--- Page 15 ---

1. Identify the incorrect code: Analyze the provided information to locate the error that the patch addresses.
Identify the required packages and the types of test cases to write.
2. Generate the test case: Write test cases that will fail without the correction patch and pass with the correction
patch. Each test case must be enclosed within < testcase ></ testcase > tags.
3. Ensure that no additional execution beyond your test case is performed. Avoid unsafe commands or unnecessary
changes to the project.
Format Requirements:
• Test Case:
– Wrap each test case in < testcase ></ testcase > tags.
– Use triple backticks (```) to enclose the test code within the < testcase ></ testcase > tags.
– The test cases must be ready to run with pytest and should include any necessary mock data or fixtures.
Environment Information:
• Python Version: 3.9
• Platform: Ubuntu 22.04.5 LTS
• Execution Command:
python −m p y t e s t
−−no−header −rA −p no : c a c h e p r o v i d e r −W ig nor e : :
DeprecationWarning −−continue −on−c o l l e c t i o n −e r r o r s
−−tb = s h o r t
• Execution Path: Root directory of the project
Example Solution:
In src/utils/csv_utils.py:
from CSVconverter . s r c . u t i l s
import
csv
def
read_csv_and_sum ( filename ) :
""" C a l c u l a t e
the sum of
a l l
numbers
in a CSV
f i l e """
t o t a l
= 0
with open ( filename ,
' r ' )
as
f i l e :
r e a d e r = csv . r e a d e r ( f i l e )
for row in
r e a d e r :
t o t a l
+= row [ 0 ]
return
t o t a l
The code directly adds row[0] to total without validating if row[0] is an integer. If the CSV file contains non-numeric
values (e.g., strings or empty fields), it will raise runtime errors like TypeError or ValueError. These errors match the
problem statement. So I’ll write test cases here.
Fix Explanation:
1. It tries to convert row[0] to an integer using int().
2. If row[0] is not a valid integer, it skips that row using a try...except block.
The goal is to write test cases that:
1. Test case with non-numeric data in the CSV (should raise an error in the original code).
2. Same test case should now correctly handle non-numeric rows and calculate the sum of valid numeric values.
Example Test Case:
< t e s t c a s e >
``` python
import os
import
p y t e s t
from
s r c . u t i l s . c s v _ u t i l s
import
read_csv_and_sum
@pytest . f i x t u r e
def
c r e a t e _ c s v _ f i l e ( ) :
""" F i x t u r e
to
c r e a t e
a temporary CSV
f i l e
f o r
t e s t i n g . """
def
_ c r e a t e _ f i l e ( contents ,
filename =" t e s t . csv " ) :
with open ( filename ,
'w ' )
as
f :
f . w r i t e ( c o n t e n t s )

--- Page 16 ---

return
filename
y i e l d
_ c r e a t e _ f i l e
# Cleanup
a f t e r
t e s t
i f
os . path . e x i s t s ( " t e s t . csv " ) :
os . remove ( " t e s t . csv " )
def
t e s t _ v a l i d _ c s v ( c r e a t e _ c s v _ f i l e ) :
""" Test
case
with
v a l i d
numeric
data . """
filename =
c r e a t e _ c s v _ f i l e ( " 1\ n2 \ n3 \ n" )
r e s u l t
= read_csv_and_sum ( filename )
a s s e r t
r e s u l t
== 6
# Expected sum of
numbers
def
test_non_numeric_csv ( c r e a t e _ c s v _ f i l e ) :
""" Test
case
with non−numeric
data . """
filename =
c r e a t e _ c s v _ f i l e ( " 1\ nabc \ n3 \ n" )
with
p y t e s t . r a i s e s ( TypeError ) :
read_csv_and_sum ( filename )
def
test_empty_csv ( c r e a t e _ c s v _ f i l e ) :
""" Test
case
with
an empty CSV
f i l e . """
filename =
c r e a t e _ c s v _ f i l e ( " " )
r e s u l t
= read_csv_and_sum ( filename )
a s s e r t
r e s u l t
== 0
# Expected sum
i s
0
```
</ t e s t c a s e >
Final Instructions:
• Test case format: Ensure the tests follow pytest conventions and are ready to run. Do not enable dangerous
commands like ifconfig or iptables.
• Import files correctly: Carefully handle functions and classes in the current package.
• Patch validation: Test cases should fail when run against the unpatched code and pass after the patch is applied.
• File handling: Ensure any files needed for the test exist. Substitute paths like /path/to/dest with actual paths.
Prompt for Test Case Revision
You are tasked with generating test cases for a given GitHub issue. The code with the golden patch should pass the
test case while failing without the golden patch. Now, the test case has failed even after applying the patch. You are
required to improve it.
Provided Information:
• Repository name: {}
• GitHub issue description: {}
• Hints Text: {}
• Golden patch (this patch passed with the previous test cases): {}
• Project Tree (file depth less than 3): {}
• Relevant Code Segments: {}
• Available Relevant APIs: {}
• Wrong Test Case: {}
• Error History: {}
Task Instructions:
1. Analyze the error history carefully: Review the error history to understand why the previous test cases passed
without the patch. For example:
• Rewrite wrong test cases if errors occur on specific tests.
• Consider import dependencies when encountering ImportError or similar errors.

--- Page 17 ---

2. Preserve the original intent: Ensure the new test cases still target the original issues that the patch is designed to
fix.
3. Format Requirements: Your test case should strictly follow the original format. Specifically:
• Setup commands should be wrapped in <env></env> tags. The commands should be enclosed in triple
backticks (“‘) inside the <env>.
• Test cases must be wrapped in <testcase></testcase> tags, and the test code should be enclosed in triple
backticks (“‘) inside the <testcase>.
Example Format:
<testcase>
```python
# Your improved test case here
```
</testcase>
<env>
```bash
# Required setup commands here
```
</env>
Important Notes:
• The new test case must still fail on the unpatched code and pass after applying the patch.
• Strictly follow the format and preserve the original test intent.
Prompt for Extracting API Signature or Class Name
Here is an error message, and you are required to extract the API signature or class name that raises the error. You
should strictly follow the format instruction and do not include any unrelated greeting words. The API should directly
raise the error, and you should not include any other APIs that are not related to the error.
Important Notes:
• For safety, you should never use os.system in the test case code. If you want to operate on the system, use the
commands in setup commands!
Format Instruction:
• If the error message is related to a function, the API signature should be in the following format:
<function>module1.module2.function_name(parameters)</function>
• If the error message is related to a class, the class name should be in the following format:
<class>module1.module2.class_name</class>
• If no API signature or class name is found, you should provide an empty string:
<empty></empty>
Example:
1. Error Message:
... ERROR collecting swedev-test.py ...
ImportError: cannot import name 'Config' from 'pkgconfig.pkgconfig' ...
Result:
<class>pkgconfig.pkgconfig.Config</class>
2. Error Message:

--- Page 18 ---

... ERROR collecting swedev-test.py ...
TypeError: example_function() missing 2 required positional arguments: 'param1' and 'param2' ...
Result:
<function>example_module.example_function(param1, param2)</function>
Task:
• Error Message: {}
• Result:
A.2
Principles for filtering instances
We keep instances that meet none of the following criteria. Except for statement length and patch size,
other metrics are judged by Llama-3.1-70B-Instruct.
• Overly concise (≤100 words)
• No large patch for limited context (≥0.8 MB)
• Vague phrasing (e.g., "fix the issue," "improve performance")
• Lack of context and no specific problem/goal
• Formatting issues (single word/punctuation)
• Lack of specificity (no detailed problem/outcome)
• Redundancy (repeats similar issues)
A.3
Generated Test Cases
Gherkin Scenarios
Feature: Quiet mode in SQLFluff CLI
Scenario: Run sqlfluff fix with –quiet option
• Given I have a SQL file with linting violations
• When I run ‘sqlfluff fix‘ with the ‘–quiet‘ option
• Then the output should only show the fix status and the number of fixes applied
• And the output should not contain detailed information about each fix
Scenario: Run sqlfluff fix with –force and –quiet options
• Given I have a SQL file with multiple linting violations
• When I run ‘sqlfluff fix‘ with the ‘–force‘ and ‘–quiet‘ options
• Then the output should only show the fix status and the number of fixes applied
• And all fixes should be applied automatically
Scenario: Run sqlfluff fix with both –quiet and –verbose options
• Given I have a SQL file with linting violations
• When I run ‘sqlfluff fix‘ with both ‘–quiet‘ and ‘–verbose‘ options
• Then I should see an error message stating that –quiet and –verbose cannot be used together
• And the process should exit with an error code

--- Page 19 ---

Examples for Test Case Generation
d i f f
−−g i t
a / c o d e a g t _ t e s t _ 0 . py b / c o d e a g t _ t e s t _ 0 . py
new
f i l e
mode 100644
index
0000000..0000000
−−−/ dev / n u l l
+++ b / c o d e a g t _ t e s t _ 0 . py
@@ −0 ,0 +1 ,63 @@
+ import
os
+ import
p y t e s t
+from
borgapi . borgapi
import
BorgAPI
+
+@pytest . f i x t u r e
+def
c r e a t e _ b o r g _ r e p o ( ) :
+
""" F i x t u r e
to
c r e a t e
a
temporary
Borg
r e p o s i t o r y
f o r
t e s t i n g . " " "
+
def
_ c r e a t e _ r e p o ( repo_name =" t e s t _ r e p o " ) :
+
api = BorgAPI ( )
+
api . i n i t ( repo_name )
+
r e t u r n
api ,
repo_name
+
y i e l d
_ c r e a t e _ r e p o
+
# Cleanup
a f t e r
t e s t
+
api ,
repo_name = _ c r e a t e _ r e p o ( )
+
api . d e l e t e ( repo_name )
+
+def
t e s t _ e x t r a c t _ t o _ s t d o u t ( c r e a t e _ b o r g _ r e p o ) :
+
""" Test
case
to
e x t r a c t
an
a r c h i v e
to
s t d o u t . " " "
+
api ,
repo_name = c r e a t e _ b o r g _ r e p o ( )
+
archive_name = " t e s t _ a r c h i v e "
+
f i l e _ p a t h
= " t e s t _ f i l e . t x t "
+
with
open ( f i l e _ p a t h ,
"w" )
as
f :
+
f . w r i t e ( " Hello ,
World ! " )
+
api . c r e a t e ( archive_name ,
f i l e _ p a t h )
+
r e s u l t
= api . e x t r a c t ( archive_name ,
s t d o u t =True )
+
a s s e r t
r e s u l t [ 0 ] == " Hello ,
World ! "
+
+def
t e s t _ e x t r a c t _ t o _ s t d o u t _ w i t h _ m u l t i p l e _ f i l e s ( c r e a t e _ b o r g _ r e p o ) :
+
""" Test
case
to
e x t r a c t
m u l t i p l e
f i l e s
from an
a r c h i v e
to
s t d o u t . " " "
+
api ,
repo_name = c r e a t e _ b o r g _ r e p o ( )
+
archive_name = " t e s t _ a r c h i v e "
+
f i l e _ p a t h 1 = " t e s t _ f i l e 1 . t x t "
+
f i l e _ p a t h 2 = " t e s t _ f i l e 2 . t x t "
+
with
open ( f i l e _ p a t h 1 ,
"w" )
as
f :
+
f . w r i t e ( " Hello ,
World ! " )
+
with
open ( f i l e _ p a t h 2 ,
"w" )
as
f :
+
f . w r i t e ( " This
i s
an othe r
f i l e . " )
+
api . c r e a t e ( archive_name ,
f i l e _ p a t h 1 ,
f i l e _ p a t h 2 )
+
r e s u l t
= api . e x t r a c t ( archive_name ,
s t d o u t =True )
+
a s s e r t
r e s u l t [ 0 ] == " Hello ,
World ! This
i s
a n o t h e r
f i l e . "
+
+def
t e s t _ e x t r a c t _ t o _ s t d o u t _ w i t h _ j s o n _ d a t a ( c r e a t e _ b o r g _ r e p o ) :
+
""" Test
case
to
e x t r a c t JSON data
from an
a r c h i v e
to
s t d o u t . " " "
+
api ,
repo_name = c r e a t e _ b o r g _ r e p o ( )
+
archive_name = " t e s t _ a r c h i v e "
+
f i l e _ p a t h
= " t e s t _ f i l e . json "
+
with
open ( f i l e _ p a t h ,
"w" )
as
f :
+
f . w r i t e ( ' { " key " :
" value " } ' )
+
api . c r e a t e ( archive_name ,
f i l e _ p a t h )
+
r e s u l t
= api . e x t r a c t ( archive_name ,
s t d o u t =True )
+
a s s e r t
r e s u l t [ 0 ] ==
'{" key " :
" value "} '
+
+def
t e s t _ e x t r a c t _ t o _ s t d o u t _ w i t h _ t e x t _ d a t a ( c r e a t e _ b o r g _ r e p o ) :
+
""" Test
case
to
e x t r a c t
t e x t
data
from an
a r c h i v e
to
s t d o u t . " " "
+
api ,
repo_name = c r e a t e _ b o r g _ r e p o ( )
+
archive_name = " t e s t _ a r c h i v e "
+
f i l e _ p a t h
= " t e s t _ f i l e . t x t "
+
with
open ( f i l e _ p a t h ,
"w" )
as
f :
+
f . w r i t e ( " This
i s
a
t e s t
f i l e . " )
+
api . c r e a t e ( archive_name ,
f i l e _ p a t h )

--- Page 20 ---

+
r e s u l t
= api . e x t r a c t ( archive_name ,
s t d o u t =True )
+
a s s e r t
r e s u l t [ 0 ] == " This
i s
a
t e s t
f i l e . "

```
