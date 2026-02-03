---
title: "RLP Reinforcement Pretraining Objective"
source_pdf: "/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/AI Labs/NVIDIA/Reinforcement-Learning/RLP-Reinforcement-Pretraining-Objective.pdf"
company: "NVIDIA"
pages: 18
extracted_at: "2026-02-02T16:29:04.977761"
type: "ai_lab_paper"
---

# RLP Reinforcement Pretraining Objective

**Company/Lab:** NVIDIA
**Model:** Reinforcement-Learning
**Source PDF:** /Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/AI Labs/NVIDIA/Reinforcement-Learning/RLP-Reinforcement-Pretraining-Objective.pdf
**Total Pages:** 18

---

## Content

```
--- Page 1 ---

2025-09-26
RLP: Reinforcement as a Pretraining Objective
Ali Hatamizadeh†1, Syeda Nahida Akter†21,
Shrimai Prabhumoye†1,3, Jan Kautz1,
Mostofa Patwary1, Mohammad Shoeybi1,
Bryan Catanzaro1,
Yejin Choi1,4
NVIDIA1, Carnegie Mellon University2, Boston University3, Stanford University4
ahatamizadeh@nvidia.com, sprabhumoye@nvidia.com
Abstract
The dominant paradigm for training large reasoning models starts with pre-training using next-token
prediction loss on vast amounts of data. Reinforcement learning, while powerful in scaling reasoning,
is introduced only as the very last phase of post-training, preceded by supervised fine-tuning. While
dominant, is this an optimal way of training? In this paper, we present RLP, an information-driven
reinforcement pretraining objective, that brings the core spirit of reinforcement learning—exploration—
to the last phase of pretraining. The key idea is to treat chain-of-thought as an exploratory action,
with rewards computed based on the information gain it provides for predicting future tokens. This
training objective essentially encourages the model to think for itself before predicting what comes
next, thus teaching an independent thinking behavior earlier in the pretraining. More concretely, the
reward signal measures the increase in log-likelihood of the next token when conditioning on both
context and a sampled reasoning chain, compared to conditioning on context alone. This approach
yields a verifier-free dense reward signal, allowing for efficient training for the full document stream
during pretraining. Specifically, RLP reframes reinforcement learning for reasoning as a pretraining
objective on ordinary text, bridging the gap between next-token prediction and the emergence of useful
chain-of-thought reasoning. Pretraining with RLP on qwen3-1.7b-base lifts the overall average across
an eight-benchmark math-and-science suite by 19%. With identical post-training, the gains compound,
with the largest improvements on reasoning-heavy tasks such as AIME25 and MMLU-Pro. Applying RLP
to the hybrid Nemotron-Nano-12B-v2 increases the overall average from 42.81% to 61.32% and
raises the average on scientific reasoning by 23%, demonstrating scalability across architectures and
model sizes. Code: https://github.com/NVlabs/RLP
1. Introduction
Large Language Models (LLMs) pretrained with next-token prediction loss have demonstrated broad utility,
but this objective does not explicitly encourage long-range reasoning or integration with world knowledge.
Consequently, state-of-the-art models (Guo et al., 2025; Yang et al., 2025) rely on post-training objectives such
as supervised fine-tuning (SFT) and reinforcement learning with human or verified feedback (RLHF, RLAIF,
RLVR) (Ouyang et al., 2022; Lambert et al., 2024) to induce complex reasoning abilities. In contrast, human
comprehension is not a linear token-by-token process, but rather a parallel integration of input with prior
knowledge (Baumgaertner et al., 2002; Hagoort et al., 2004; Metzner et al., 2015). Current pretraining lacks
such mechanisms, limiting the model’s ability to reason and ground language in world knowledge during
learning.
To fill this gap, we propose Reinforcement Learning Pre-training (RLP) which treats Chain-of-Thought
(CoT) generation as an explicit action taken before predicting each next token. As shown in Fig.1, the model
first samples an internal thought, then predicts the observed token from the same context augmented with that
thought. The training signal is the increase in log-likelihood of the observed token when the thought is present
compared to a no-think baseline. This yields a verifier-free and dense reward that assigns position-wise credit
1Work done during internship at NVIDIA
† Equal contribution
© 2025 NVIDIA. All rights reserved.
arXiv:2510.01265v1  [cs.LG]  26 Sep 2025

--- Page 2 ---

RLP: Reinforcement as a Pretraining Objective
Thought Policy
No-Think baseline
...
...
Dense 
non-binary 
reward
CoT trace + next token
Next Token Prediction
Photosynthesis is the process 
plants, algae, and some bacteria 
use to make their own food using 
sunlight
Photosynthesis is the process 
plants, algae, and some bacteria 
use to make their own food using 
<think> The sentence describes 
how plants, algae, and bacteria 
make food. Common knowledge 
says this process relies on energy 
from the sun. So the next token is 
most likely “sunlight.”</think> 
sunlight
Information Gain 
Reward
Impact of RLP
RLP leverages verifier-free, dense
rewards based on information gain
to pre-train models that reason before
next token prediction.
RLP further improves reasoning
accuracies after post-training
Paradigm Comparison
Next Token Prediction
RLP
Aspect
Objective
Maximum likelihood + reward
Signal Type
Dense, position-wise info-gain
Reasoning
Behaviour
Explicitly incentivised
Pipelines
NTP: Input → Next token
RLP: Input → CoT + Next token → Verifier-Free Dense Information Gain Reward
RLP bridges pretraining and reasoning
with scalable, dense reward
Overview of RLP
Implicit, Weak
Maximum likelihood of observed tokens
Single sparse (next token)
Reward Source
None
Verifier-free, instrinsic
Figure 1: Visualization of the RLP framework. A chain-of-thought is sampled before next-token prediction.
Rewards are computed by contrasting the predictor conditioned on the CoT with a No-think EMA baseline,
yielding a verifier-free, dense signal. We list the advantages of RLP over the traditional pretraining objective
(top right) and show the impact after end-to-end training (top left).
wherever thinking improves prediction. Because the signal is defined for ordinary text with teacher forcing,
RLP reframes reinforcement learning for reasoning as reinforcement pretraining on the same streams used for
maximum likelihood.
Unlike post-training with verifiable rewards, which requires task-specific checkers or curated solutions,
RLP is verifier-free: the signal is computed directly from log-evidence under the model and a baseline,
allowing uniform application to domain agnostic web-scale text. Compared to reinforcement pretraining via
prefix-matching rewards (RPT) (Dong et al., 2025), which uses sparse binary reward and often relies on
proxy-model filtering of “easy” tokens, RLP provides a continuous improvement signal at every position and
trains on the full documents. This eliminates the need to preselect high-entropy tokens or couple training
to a separate small model. Prior RPT demonstrations also depend on distilled checkpoints with strong prior
reasoning ability, which clouds whether the method helps base models. RLP is designed to shape thinking in
base models by rewarding only those thoughts that measurably help next-token prediction.
This work makes the following key contributions: We introduce RLP, a verifier-free information-gain
objective that augments next-token prediction by rewarding thoughts in proportion to their predictive utility.
We develop a practical and stable training algorithm that interleaves reinforcement updates with standard
likelihood training via group-relative advantages, a clipped surrogate for thought tokens, and a slowly updated
Exponential Moving Average (EMA) baseline. We provide theoretical guarantees linking expected reward to
reductions in cross-entropy and to a computable lower bound, ensuring both interpretability and tractability.
We conduct comprehensive experiments showing that RLP outperforms strong baselines, remains robust after
strong post-training, generalizes across diverse corpora, and scales effectively to larger model sizes and hybrid
architectures—establishing it as a broadly applicable reinforcement pretraining objective.
Our empirical validation is comprehensive, assessing the efficacy of RLP along four key axes. First,
we evaluate its performance relative to traditional next-token prediction baselines. On the qwen3-1.7b-
base model, RLP outperforms continuous pretraining by +17% and RPT by nearly +4%. We show the
advantage persists even when the baseline uses 35× more data to match FLOPs, confirming the gains arise
from methodology rather than compute. Second, we demonstrate the robustness of these improvements,
showing they are not transient. As shown in Fig.1, when subjected to an identical, strong post-training regimen,
the foundational advantages of RLP compound, allowing our final model to surpass its conventionally trained
counterparts by a significant 7–8% margin. Third, unlike methods requiring narrow, curated datasets, RLP
successfully extracts a powerful reasoning signal from diverse, general-purpose web corpora–establishing its
versatility across data domains (Table 4). Finally, we confirm its scalability and architecture-agnostic power.
2

--- Page 3 ---

RLP: Reinforcement as a Pretraining Objective
When applied to a 12B hybrid Mamba-Transformer (Nemotron-Nano-12B-v2), RLP achieves a staggering
35% relative improvement over a heavily trained baseline while using just 0.125% of the data—a testament
to its remarkable data efficiency and broad applicability across llm families and sizes.
2. Methodology
We introduce RLP, a pretraining-time procedure that explicitly induces reasoning. As illustrated in Fig. 1, RLP
inserts a short Chain-of-Thought (CoT) before next-token prediction and measures how much that thought
improves the model’s log-probability of the observed token relative to a no-think baseline. This improvement,
which is a log-likelihood ratio, is a verifier-free, dense reward available at every position in ordinary text
corpora. By valuing thoughts in proportion to their predictive benefit, RLP turns reinforcement pretraining
into learning to think on the same data used for standard next-token training.
Parameterization and roles.
We separate the components for clarity:
• Thought policy / predictor 𝜋𝜃(𝑐𝑡| 𝑥<𝑡) and 𝑝𝜃(𝑥𝑡| 𝑥<𝑡, 𝑐𝑡) share exactly the same network and
parameters 𝜃. The network first samples a CoT 𝑐𝑡and then, conditioned on the concatenated prefix
(𝑥<𝑡, 𝑐𝑡), scores the next token 𝑥𝑡.
• No-think baseline ¯𝑝𝜑(𝑥𝑡| 𝑥<𝑡) (parameters 𝜑) is an EMA teacher of the current network used to score
the same token without any CoT channel.
Thus, there is a single model that both generates the thought and predicts the next token given that thought;
the EMA teacher provides the no-think counterfactual.
Classical next-token objective.
Given a text sequence 𝑥= (𝑥0, . . . , 𝑥𝑇) and position 𝑡, the standard next-token objective for a predictor 𝑞𝜂is
ℒNTP(𝜂) :=
E
(𝑥<𝑡,𝑥𝑡)∼𝒟
[︀
log 𝑞𝜂(𝑥𝑡| 𝑥<𝑡)
]︀
.
(1)
For distributions 𝑝and 𝑞on the next token, we define Cross-entropy (CE) as
CE(𝑝, 𝑞)
def
=
E
𝑥∼𝑝
[︀
−log 𝑞(𝑥)
]︀
.
(2)
Using 𝑝*(· | 𝑥<𝑡) for the data distribution over 𝑥𝑡, maximizing equation 1 is equivalent to minimizing
E𝑥<𝑡∼𝒟
[︀
CE
(︀
𝑝*, 𝑞𝜂(· | 𝑥<𝑡)
)︀]︀
. We include equation 1 only for context as our training does not include a standard
NTP loss term. Instead, RLP optimizes an information-gain objective defined below and updates parameters
only through the tokens of the sampled thoughts.
2.1. Reasoning as an action
RLP augments next-token prediction with a sampled thought. At each position 𝑡, the policy draws a latent CoT
random variable
𝑧𝑡∼𝜋𝜃(· | 𝑥<𝑡),
and we write 𝑐𝑡for its realization. The network then predicts 𝑥𝑡with the reasoned scorer 𝑝𝜃(· | 𝑥<𝑡, 𝑐𝑡). As a
no-think counterfactual we use ¯𝑝𝜑(· | 𝑥<𝑡), the EMA teacher queried on the same context without providing
the CoT.
EMA teacher instantiation and schedule.
We instantiate the EMA teacher to match the current model on the first batch (𝜑←𝜃), and thereafter update it
after each optimizer step via
𝜑←𝜏𝜑+ (1 −𝜏) 𝜃,
𝜏= 0.999.
3

--- Page 4 ---

RLP: Reinforcement as a Pretraining Objective
This choice makes ¯𝑝𝜑a moving counterfactual that is (i) current enough to provide informative comparisons and
(ii) intentionally lagged to mitigate reward hacking. If the baseline were frozen, the counterfactual would drift
too far from the evolving model; if it tracked the model without lag, the log-likelihood ratio would collapse
toward zero and invite degenerate strategies. The post-update averaging yields a one-step-lagged, smoothed
teacher that stabilizes training.
2.2. Information-gain reward
With teacher forcing on the next token, define the reasoned and baseline log-evidence
𝑆pred(𝑐𝑡) := log 𝑝𝜃
(︀
𝑥𝑡
⃒⃒𝑥<𝑡, 𝑐𝑡
)︀
,
(3)
𝑆ema := log ¯𝑝𝜑
(︀
𝑥𝑡
⃒⃒𝑥<𝑡
)︀
.
(4)
The information-gain reward is the log-likelihood ratio
𝑟(𝑐𝑡) := 𝑆pred(𝑐𝑡) −𝑆ema,
(5)
which compares the reasoned scorer with a no-think baseline on the observed next token. Rewards are computed
under teacher forcing for each 𝑡. When updating the policy, we treat 𝑟(𝑐𝑡) as a constant with respect to 𝜃(no
backpropagation through 𝑝𝜃or ¯𝑝𝜑); see §2.4.
2.3. Expected improvement identity
Proposition 1 (CE reduction). For any fixed (𝑥<𝑡, 𝑐𝑡),
E
𝑥𝑡∼𝑝*[𝑟(𝑐𝑡)] = CE
(︀
𝑝*, ¯𝑝𝜑(· | 𝑥<𝑡)
)︀
−CE
(︀
𝑝*, 𝑝𝜃(· | 𝑥<𝑡, 𝑐𝑡)
)︀
.
where 𝑝*(· | 𝑥<𝑡) is the data distribution over 𝑥𝑡. Maximizing the expected reward therefore maximizes the
predictive usefulness of the thought for the next token.
Proposition 2 (Lower bound via marginalization over thoughts). Let 𝜋𝜃(𝑧𝑡| 𝑥<𝑡) be the distribution over CoTs
and define the collapsed predictor
˜𝑝𝜃(𝑥| 𝑥<𝑡) =
E
𝑧𝑡∼𝜋𝜃(·|𝑥<𝑡)
[︀
𝑝𝜃(𝑥| 𝑥<𝑡, 𝑧𝑡)
]︀
.
Then for any realized 𝑥𝑡,
E
𝑐𝑡∼𝜋𝜃
[︀
𝑆pred(𝑐𝑡)
]︀
≤log ˜𝑝𝜃(𝑥𝑡| 𝑥<𝑡),
and
𝐽(𝜃) = E[𝑟(𝑐𝑡)] ≤E
[︂
log ˜𝑝𝜃(𝑥𝑡| 𝑥<𝑡)
¯𝑝𝜑(𝑥𝑡| 𝑥<𝑡)
]︂
.
The CoT-conditioned objective is thus a computable lower bound on the improvement one would obtain after
marginalizing thoughts. Refer to §8.1 of the appendix for the proofs of the propositions.
2.4. RLP objective and optimization
RLP optimizes the thought policy to produce thoughts that increase predictive evidence. Our training does not
include the standard next-token loss in equation 1. Instead, we optimize only the information-gain objective
max
𝜃
𝐽(𝜃) =
E
𝑥<𝑡∼𝒟
E
𝑐𝑡∼𝜋𝜃(·|𝑥<𝑡)
[︀
𝑟(𝑐𝑡)
]︀
,
(6)
or, equivalently, we minimize the negative information-gain loss ℒIG(𝜃) = −𝐽(𝜃). Gradients are applied only to
the thought tokens; 𝑟(𝑐𝑡) is treated as a constant (no backpropagation through 𝑝𝜃or ¯𝑝𝜑) .
4

--- Page 5 ---

RLP: Reinforcement as a Pretraining Objective
Algorithm 1 RLP for next-token prediction with information gain
1: Inputs: dataset 𝒟, group size 𝐺≥2, clipping (𝜖ℓ, 𝜖ℎ), EMA decay 𝜏∈(0, 1), learning rate 𝜂.
2: Model: a single network with parameters 𝜃used both as (i) thought policy 𝜋𝜃and (ii) reasoned predictor
𝑝𝜃; EMA baseline ¯𝑝𝜑.
3: Initialization: mark 𝜑as uninitialized.
4: while training do
5:
Set the behavior snapshot 𝜃old ←𝜃.
◁used for the current sampling pass
6:
Sample minibatch {(𝑥(𝑏)
<𝑡, 𝑥(𝑏)
𝑡)}𝐵
𝑏=1 ∼𝒟.
7:
For each 𝑏, sample 𝐺thoughts 𝑐(𝑏,𝑖)
𝑡
∼𝜋𝜃old(· | 𝑥(𝑏)
<𝑡) with |𝑐(𝑏,𝑖)
𝑡
| ≥1.
8:
if 𝜑is uninitialized then
9:
𝜑←𝜃
◁lazy init of EMA teacher
10:
Compute baseline log-evidence (teacher forcing, no grad) 𝑆(𝑏)
ema as per equation 3.
11:
Compute reasoned log-evidence 𝑆(𝑏,𝑖)
pred and rewards 𝑟(𝑏,𝑖) as per equation 3 and equation 5.
12:
Group baseline ¯𝑟(𝑏) and 𝐴(𝑏,𝑖) (inclusive mean with correction; sg is stop-grad) as per equation 7.
13:
Per-token importance ratios and clipped surrogate for ℓ(𝑏,𝑖)
𝑢
with prefix prefix(𝑏,𝑖)
𝑢
:
𝜌(𝑏,𝑖)
𝑢
= exp
(︁
log 𝜋𝜃(ℓ(𝑏,𝑖)
𝑢
| prefix(𝑏,𝑖)
𝑢
) −log 𝜋𝜃old(ℓ(𝑏,𝑖)
𝑢
| prefix(𝑏,𝑖)
𝑢
)
)︁
.
𝐿(𝑏,𝑖)
clip = −
1
|𝑐(𝑏,𝑖)
𝑡
|
∑︀
𝑢min
(︁
𝜌(𝑏,𝑖)
𝑢
sg
(︀
𝐴(𝑏,𝑖))︀
, clip(𝜌(𝑏,𝑖)
𝑢
; 1 −𝜖ℓ, 1 + 𝜖ℎ) sg
(︀
𝐴(𝑏,𝑖))︀)︁
.
14:
Policy update on thought tokens:
ℒ(𝜃) =
1
𝐵𝐺
∑︀𝐵
𝑏=1
∑︀𝐺
𝑖=1 𝐿(𝑏,𝑖)
clip ,
𝜃←𝜃−𝜂∇𝜃ℒ(𝜃).
15:
EMA update of baseline: 𝜑←𝜏𝜑+ (1 −𝜏) 𝜃.
16: Output: trained policy/predictor (shared 𝜃) and EMA baseline 𝜑.
Group-relative baseline (inclusive mean with correction).
To reduce variance, for each context we sample 𝐺≥2 thoughts {𝑐(𝑖)
𝑡}𝐺
𝑖=1 and use a corrected inclusive mean
baseline. Let
¯𝑟=
1
𝐺
𝐺
∑︁
𝑗=1
𝑟
(︀
𝑐(𝑗)
𝑡
)︀
.
We define the advantages
𝐴(𝑖) :=
𝐺
𝐺−1
(︁
𝑟
(︀
𝑐(𝑖)
𝑡
)︀
−¯𝑟
)︁
,
with no gradient propagated through ¯𝑟.
(7)
This multiplicative factor removes the
(︀
1 −1
𝐺
)︀
shrinkage inherent to the inclusive mean, yielding an unbiased
estimator with low variance.
Per-token importance ratios and clipped surrogate.
We update the log-probability of the thought tokens with a clipped surrogate. Let ℓ(𝑖)
𝑢be the 𝑢-th token in 𝑐(𝑖)
𝑡
and prefix(𝑖)
𝑢= (𝑥<𝑡, ℓ(𝑖)
1:𝑢−1). With behavior parameters 𝜃old used to sample the thoughts, define the per-token
importance ratio
𝜌(𝑖)
𝑢= exp
(︁
log 𝜋𝜃(ℓ(𝑖)
𝑢| prefix(𝑖)
𝑢) −log 𝜋𝜃old(ℓ(𝑖)
𝑢| prefix(𝑖)
𝑢)
)︁
.
We write clip(𝜌; 1 −𝜖ℓ, 1 + 𝜖ℎ) for elementwise clipping and denote stop-gradient by sg(·). The surrogate loss is
ℒclip(𝜃) = −E
[︃
1
|𝑐(𝑖)
𝑡|
∑︁
𝑢
min
(︁
𝜌(𝑖)
𝑢
sg(𝐴(𝑖)), clip(𝜌(𝑖)
𝑢; 1 −𝜖ℓ, 1 + 𝜖ℎ) sg(𝐴(𝑖))
)︁]︃
.
(8)
5

--- Page 6 ---

RLP: Reinforcement as a Pretraining Objective
Benchmark
ℳbase
ℳCPT
ℳRLP
ℳbase +Post
ℳCPT +Post
ℳRLP +Post
AIME25
2.25
3.96
5.02
5.32
5.89
7.05
MATH500
48.45
57.52
58.48
61.92
62.70
64.30
GSM8K
54.16
72.85
74.48
78.22
78.70
80.50
AMC23
25.94
31.25
31.25
35.00
34.38
36.50
Minerva
15.30
19.03
21.19
25.30
26.10
27.80
MMLU
50.08
41.95
56.14
58.36
59.00
61.50
MMLU@1[4]
44.85
40.00
52.18
56.00
58.53
61.00
MMLU-Pro
28.17
27.81
34.62
37.85
39.92
42.40
MMLU-Pro@1[4]
23.95
24.61
30.80
36.53
38.49
41.30
GPQA
25.25
26.26
28.28
30.93
29.27
33.33
GPQA@1[4]
27.52
24.75
27.02
31.52
30.01
34.97
Math Avg
24.35
30.77
31.74
34.29
34.63
36.03
Science Avg
34.50
32.01
39.68
42.38
42.73
45.74
Science Avg@1[4]
32.11
29.79
36.67
41.35
42.34
45.76
Overall
30.32
30.85
36.03
39.34
39.90
42.51
Table 1: Quantitative benchmarks for Qwen3-1.7B-Base, showing the impact of RLP. Shaded columns indicate
RLP variants; “Post” indicates SFT + RLVR post-training.
2.5. Reward properties and guarantees
Does thinking actually help?
The reward 𝑟(𝑐𝑡) is positive exactly when the model that used the sampled thought assigns higher probability
to the observed next token than the EMA baseline that did not think. In expectation over the data distribution,
this equals the reduction in cross-entropy between the reasoned scorer and the no-think baseline (Prop. 1).
Positionwise credit at every step.
Since the task is next-token prediction, the reward is computed independently at each position 𝑡as
𝑟(𝑐𝑡) = log 𝑝𝜃(𝑥𝑡| 𝑥<𝑡, 𝑐𝑡) −log ¯𝑝𝜑(𝑥𝑡| 𝑥<𝑡).
Credit is attached exactly where the thought changes predictive probability, yielding one scalar per token and
removing the need for a learned value function or any external verifier.
Putting it all together.
Algorithm 1 composes the above pieces into a single training loop. Specifically, multiple thoughts are sampled
per position and information-gain rewards are computed against a moving EMA counterfactual. Group-relative
advantages are formed and the shared network is updated only on the thought tokens via the clipped surrogate
in equation 8. In this case, the improvements originate from learning to generate thoughts that systematically
raise predictive evidence.
3. Experimental Setup
We experiment with qwen3-1.7b-base (Yang et al., 2025) and then scale our experiments to a larger
Nemotron-Nano-12B-v2 (Nano, 2025) model.2
RLP.
We apply RLP on a diverse set of datasets across two settings: (i) SFT-style reasoning corpora, including a
math-centric set (OmniMath (Gao et al., 2024)) and mixed math + general-reasoning sets (OpenThoughts
(Guha et al., 2025), Nemotron-Crossthink (Akter et al., 2025)); and (ii) general-purpose pretraining corpora,
covering academic papers (ACAD), math textbooks (Math-Text), and open-ended web pages QA pairs from
2Details about hyper-parameters for each of the below phases can be found in §9.
6

--- Page 7 ---

RLP: Reinforcement as a Pretraining Objective
Common Crawl (Web-Crawl)(Nano, 2025). We train with RLP for 1B tokens using general pretraining corpora
(𝒟PT) to evaluate its effect in an end-to-end llm pretraining pipeline. We denote this model as ℳRLP.
Continuous Pretraining.
To ensure compute equivalent comparison with ℳRLP, we do continuous pretraining on the base model denoted
by ℳbase with the same tokens used in RLP. We denote this model as ℳCPT. This serves as an additional
baseline for our experiments.
Post-Training.
All models undergo a SFT stage on OpenThoughts data (Guha et al., 2025). To further enhance, we apply
Reinforcement Learning with Verifier Rewards (RLVR) using MATH dataset (Hendrycks et al., 2021b). This
two-stage post-training pipeline provides an evaluation framework to verify that gains from RLP persist under
strong alignment, while also revealing how much additional improvement can be achieved through subsequent
post-training. For consistency, all models are trained with identical SFT and RLVR receipes, ensuring that any
observed differences in downstream accuracies can be attributed to the pretraining condition (ℳbase vs ℳCPT
vs ℳRLP).
3.1. Evaluation Metrics
We conduct a thorough benchmark assessment using a series of tasks using NeMo-Skills3.
Math Reasoning (math avg). We consider four diverse math benchmarks : GSM8K (Cobbe et al., 2021),
MATH-500 (Hendrycks et al., 2021c), Minerva Math (Lewkowycz et al., 2022), AMC23. We report Pass@1
average of 8 runs for these.
Science Reasoning (science avg). For conceptual science and specialized knowledge, we evaluate on
MMLU (Hendrycks et al., 2021a), MMLU-Pro (Wang et al., 2024), and the graduate-level STEM benchmark
GPQA-Diamond (Rein et al., 2024). For science benchmarks, we report the average greedy and Pass@1 scores
from 4 runs (science avg@1[4]).
4. Results
Table 1 reports the performance of qwen3-1.7b-base under different pretraining and post-training objec-
tives. First, RLP consistently outperforms both the ℳbase and ℳCPT across nearly all benchmarks, with
especially strong gains on reasoning-heavy tasks such as AIME25 and MMLU-Pro. We see that ℳRLP is
relatively on average 19% and 17% better than ℳbase and ℳCPT respectively. This highlights the effec-
tiveness of dense, verifier-free reinforcement signals for instilling reasoning capabilities during pretraining.
Model
Math Avg
Science Avg
Science Avg@1[4]
Avg
ℳbase
61.38
34.51
32.54
42.81
ℳRLP
65.33
57.26
61.37
61.32
Table 2: Comparison of ℳbase and RLP for the Nemotron-Nano-12B-v2
model.
Second, the benefits of RLP
persist even after strong post-
training (SFT + RLVR). While
all models improve after post-
training, ℳRLP achieves the
highest scores with the overall
average substantially higher
than both ℳbase by 8% and
ℳCPT by 7% relatively. This
indicates that RLP establishes robust reasoning foundations that are not washed out by downstream alignment
but instead compound with post-training. We observe particularly large gains in science domains, with ℳRLP
+Post achieving +3 points over ℳCPT +Post. This trend suggests that RLP is not limited to mathematical
reasoning but also generalizes effectively to other domains. The ability to strengthen performance in science
benchmarks highlights that RLP fosters a broader class of multi-step explanation-driven reasoning skills,
moving beyond domain-specific improvements and pointing toward a more versatile foundation for reasoning
in LLMs. Overall, the results demonstrate that RLP not only induces reasoning ability during pretraining but
3https://github.com/NVIDIA/NeMo-Skills
7

--- Page 8 ---

RLP: Reinforcement as a Pretraining Objective
also synergizes with post-training, leading to models with stronger and more durable reasoning abilities than
those trained with next-token prediction or continuous pretraining.
Scaling Model Size and Architecture:
We further scale RLP to Nemotron-Nano-12B-v2 (Nano, 2025) (ℳbase), a hybrid Mamba-Transformer
language model of 12B parameter size. In this comparison we take an intermediate checkpoint of Nemotron-
Nano-12B-v2 trained till 19.8 trillion tokens and apply RLP for 250 million tokens only. ℳbase on the other
hand is trained for 20 trillion tokens. Table 2 demonstrates that the benefits of RLP persist and even amplify
when scaling to larger model sizes and generalizes to different model architectures. On the Nemotron-Nano-
12B-v2 model, ℳRLP substantially outperforms ℳbase across all domains, and particularly ℳRLP is relatively
35% on average better than ℳbase inspite of being trained on approx. 200 billion less tokens. While math
performance improves moderately, the most striking gains emerge in science reasoning, where Science Avg
jumps an absolute 23%. These results highlight that RLP yields not only stronger math performance but also
robust cross-domain reasoning capabilities.
RPT Comparison
Following
the
experimental
setup
in
RPT
with
Omni-MATH
dataset,
we
Model
Math Avg
Science Avg
Avg
ℳbase
35.96
32.11
34.03
ℳRPT
47.50
35.88
41.69
ℳRLP
49.62
37.07
43.35
Table 3: RLP outperforms RPT across all averages. qwen3-
1.7b-base was trained with both RPT and RLP for one epoch
with matched data and compute.
trained both methods for one epoch under
matched data and compute budgets before
evaluating on our benchmark suite. As summa-
rized in Table Table 3, RLP achieves uniformly
higher aggregates: Math Avg improves from
47.50 to 49.62 (+2.12; +4.5% relative), Sci-
ence Avg from 35.88 to 37.07 (+1.19; +3.3%),
and Overall Avg from 41.69 to 43.35 (+1.66;
+4.0%). Methodologically, RPT applies rein-
forcement only to tokens pre-selected by an
auxiliary assistant via entropy filtering and optimizes a sparse, binary next-token correctness signal that ignores
the CoT content, limiting where the signal can be applied. In contrast, RLP evaluates each sampled CoT by the
information gain it provides for the observed next token and updates at all positions without an auxiliary filter
which yields consistently better averages under the matched setting above. Crucially, this dense, per-token
information-gain reward supplies richer credit assignment than RPT’s sparse binary signal and, in our matched
experiments, empirically yields better performance.
5. Ablations
Does RLP provide generalizable improvements across diverse corpora?
A key advantage of RLP is its scalability to large, diverse corpora, unlike RLVR, which relies on small, curated
reasoning datasets and raises concerns about generalizability. Prior work (Chen et al., 2025; Setlur et al., 2025)
highlights the need for complex reasoning corpora to sustain RL improvements, but such datasets are costly to
curate and impractical at pretraining scale. For these ablations, we apply RLP to qwen3-1.7b-base for 200
steps—utilizing 170M input tokens—holding the rest of the setup fixed.
As illustrated in Table 4, RLP delivers consistent gains across all corpus families, eliminating concerns that
RL based pretraining only benefits curated reasoning data. Relative to ℳbase average improves by 7-9% with
strongest gains on Nemotron-Crossthink (SFT-style) and Web-Crawl (general-purpose corpora). Unlike prior
work (Akter et al., 2025), where RL gains were limited to math and weakened under mixed data, RLP achieves
simultaneous improvements across all benchmarks, demonstrating genuine cross-domain transfer. Even on
purely non-reasoning general corpora such as web-crawl, RLP extracts a reasoning signal that scales with data
diversity (Appendix 11). Table 4 illustrates that unlike prior work (Liu et al., 2025b; Zhou et al., 2025), RLP
can be applied to any data format like academic papers, textbooks, web-crawl as well as SFT style data. Overall,
RLP is scalable, domain-agnostic pre-training augmentation that enhances both reasoning and accuracy.
8

--- Page 9 ---

RLP: Reinforcement as a Pretraining Objective
Model
Dataset
Type
Math Avg
Science Avg
Science Avg@1[4]
Avg
ℳbase
-
-
35.96
34.50
32.11
34.19
ℳCPT
Nemotron-Crossthink [170M]
Equal Input Token
37.11
35.76
32.15
35.01
Nemotron-Crossthink [6B]
Equal FLOPs
43.90
37.74
32.47
38.04
𝒟PT[1B]
PT Data Mix
45.34
32.14
29.33
35.60
ℳRLP
OmniMath [170M]
SFT
46.48
40.27
37.54
41.43
OpenThoughts [170M]
47.64
40.84
35.88
41.45
Nemotron-Crossthink [170M]
49.76
42.54
37.78
43.36
ACAD [170M]
General
47.68
40.59
36.87
41.71
Math-Text [170M]
48.07
40.46
36.32
41.62
Web-Crawl [170M]
48.87
40.75
36.77
42.13
𝒟PT[1B]
PT Data Mix
46.35
39.68
36.67
40.90
Table 4: RLP across diverse corpora. RLP trained on six SFT-style and general-purpose datasets yields
consistent gains, indicating transferable reasoning from mixed/open-ended data.
Does the improvement sustain under compute equivalent baselines?
A critical question is whether RLP’s gains stem from its unique RL-based pretraining or simply higher compute.
Standard next-token pretraining quantifies compute by input tokens, but RLP adds rollout costs not captured
by this metric. For fair comparison, we evaluate against ℳCPT baselines under: (a) equal Input Tokens Seen
and (b) equal total Compute FLOPs. RLP is fixed to 𝑇𝑖𝑛𝑝= 170M tokens; the token-matched ℳCPT [170M]
continues pretraining on 170M tokens (Input Token), while the FLOP-matched budget corresponds to 6B tokens
for CPT (ℳCPT [6B])(see Appendix 10).
In Table 4, ℳRLP outperforms ℳCPT trained on the same 170M tokens and maintains a clear advantage
even against a compute-matched ℳCPT exposed to 6B tokens (35× more data). Despite this disparity, RLP
achieves a 5.3% gain on average (compare ℳCPT Nemotron-Crossthink [6B] vs ℳRLP Nemotron-Crossthink
[170M]), with consistent improvements across math and science benchmarks. These results show that RLP’s
gains stem not from more efficient use of compute, not larger budgets, validating the effectiveness of our
approach.
Is RLP comparable to cpt with high-quality reasoning data?
High-quality reasoning corpora have shown to substantially boost base model reasoning ability when used in
continuous pretraining (cpt) or mid-training (Wang et al., 2025; Gandhi et al., 2025). This raises the important
question of whether cpt can match or even surpass RLP under such favorable conditions. To investigate this,
we conduct cpt on both reasoning-centric, Nemotron-Crossthink and general pretraining (𝒟PT) datasets, each
using 170M tokens. Our results in Table 4 show that even with high quality reasoning data, RLP consistently
outperforms cpt by a significant margin. Specifically, ℳRLP outperforms ℳCPT, showing an average gain of
8% on Nemotron-Crossthink and 5% on pre-training data mix (𝒟PT) on 1B tokens. These results highlight
two key insights. First, while cpt benefits from reasoning-dense corpora, it remains sensitive to domain
skew—evident in the weak science accuracy on 𝒟PT—whereas RLP generalizes more evenly across disciplines.
Second, the consistent margin by which RLP outperforms cpt, even in the presence of high quality reasoning
data, underscores that the gains of RLP are not merely due to data quality but stem from the algorithmic design
itself. This reinforces the conclusion that RLP provides a generalizable mechanism for leveraging reasoning
data during pretraining, complementing rather than being overshadowed by high-quality corpus selection.
Ablations on rollout count, completion length, and KL weight.
Fig. 2 visualizes the trends across three settings: (a) rollouts, (b) completion length, and (c) KL. Please look
into §10 for more detailed numbers and per-task breakdowns. More rollouts help up to 𝐺= 16 (Overall 42.17%);
𝐺= 4 and 8 already reach 41.38% and 41.95%, while 𝐺= 32 decreases slightly to 41.75% (Fig. 2a). Increasing
completion length gives the largest gains. Specifically, overall rises from 11.50% at 64 to 42.17% at 2048, with
Math/Science moving from 1.12%/21.88% to 48.06%/36.29% (Fig. 2b). Extending to 4096 yields 42.21% at
roughly twice the thought budget, so we default to 2048. Furthermore, a KL anchor does not help. Specifically,
9

--- Page 10 ---

RLP: Reinforcement as a Pretraining Objective
5
10
15
20
25
30
# rollouts (R)
0
10
20
30
40
50
Accuracy (%)
best
Math Avg
Science Avg
Overall Avg
Baseline Math
Baseline Science
Baseline Overall
(a) Number of rollouts
64
128
256
512
1024
2048
4096
completion length (L)
0
10
20
30
40
50
Accuracy (%)
best
Math Avg
Science Avg
Overall Avg
Baseline Math
Baseline Science
Baseline Overall
(b) completion length
1e-4
1e-3
0
β (KL coefficient)
0
10
20
30
40
50
Accuracy (%)
best
Math Avg
Science Avg
Overall Avg
Baseline Math
Baseline Science
Baseline Overall
(c) KL coefficient 𝛽
Figure 2: Ablations on Qwen3-1.7B. Curves report Math/Science/Overall averages. Dashed lines mark the
base model.
𝛽= 10−4 and 10−3 give 41.35% and 41.44%, compared to 42.17% at 𝛽= 0, and it also increases memory and
step time (Fig. 2c). We therefore use 𝐺= 16, completion length 2048, and 𝛽= 0 in later experiments.
6. Related Work
Next-Token Prediction.
Next-token prediction is the standard pretraining objective for LLMs: predict the next word from prior context
(Shannon, 1951; Bengio et al., 2003). Scaling it with Transformers (Vaswani et al., 2017) enabled landmark
and state-of-the-art systems (Radford et al., 2018; Brown et al., 2020; Smith et al., 2022; Bi et al., 2024;
Nano, 2025; Yang et al., 2025). Anticipating tokens across corpora induces syntactic, semantic, and pragmatic
structure that transfers broadly. Alternatives include masked language modeling (Devlin et al., 2019) and span
corruption (Raffel et al., 2020), but next-token prediction remains dominant for its alignment with left-to-right
generation and strong downstream accuracy across tasks. In this work. we add a verifier-free dense reward
during pretraining that leverages reasoning before prediction.
Verifier-Free Rewards in Post-Training.
Recent work explores verifier-free rewards. Yuan et al. (2024) uses iterative DPO where, after SFT, the model
judges its own candidates to create preference pairs. Liu et al. (2025b) trains with incentive RL on SFT corpora.
Zhao et al. (2025) proposes RL from an internal feedback while using the model’s confidence as reward. RLP,
in contrast, is a GRPO-style pretraining objective. It operates on any text data including web-crawl, academic
papers and SFT datasets and optimizes continuation quality beyond next-token prediction. Because these
methods target post-training policies, direct comparisons are not well-posed.
7. Conclusion
We introduce RLP, a reinforcement pretraining objective that rewards chain-of-thought by its information gain
for next-token prediction. Unlike traditional approaches that defer RL to post-training, RLP instills reasoning
during pretraining, yielding gains that persist and compound after alignment. Experiments across datasets,
domains, and architectures show that RLP consistently outperforms compute-matched baselines and scales
efficiently to large hybrid models, establishing reinforcement pretraining as a principled and general alternative
to likelihood-only training.
References
Syeda Nahida Akter, Shrimai Prabhumoye, Matvei Novikov, Seungju Han, Ying Lin, Evelina Bakhturina, Eric
Nyberg, Yejin Choi, Mostofa Patwary, Mohammad Shoeybi, and Bryan Catanzaro. Nemotron-crossthink:
Scaling self-learning beyond math reasoning, 2025. URL https://arxiv.org/abs/2504.13941. 6, 8
10

--- Page 11 ---

RLP: Reinforcement as a Pretraining Objective
Annette Baumgaertner, Cornelius Weiller, and Christian Büchel. Event-related fmri reveals cortical sites involved
in contextual sentence integration. Neuroimage, 16(3):736–745, 2002. 1
Yoshua Bengio, Réjean Ducharme, Pascal Vincent, and Christian Jauvin. A neural probabilistic language model.
Journal of machine learning research, 3(Feb):1137–1155, 2003. 10
Xiao Bi, Deli Chen, Guanting Chen, Shanhuang Chen, Damai Dai, Chengqi Deng, Honghui Ding, Kai Dong,
Qiushi Du, Zhe Fu, et al. Deepseek llm: Scaling open-source language models with longtermism. arXiv
preprint arXiv:2401.02954, 2024. 10
Tom Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared D Kaplan, Prafulla Dhariwal, Arvind
Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, et al. Language models are few-shot learners.
Advances in neural information processing systems, 33:1877–1901, 2020. 10
Yang Chen, Zhuolin Yang, Zihan Liu, Chankyu Lee, Peng Xu, Mohammad Shoeybi, Bryan Catanzaro, and Wei
Ping. Acereason-nemotron: Advancing math and code reasoning through reinforcement learning, 2025. URL
https://arxiv.org/abs/2505.16400. 8
Karl Cobbe, Vineet Kosaraju, Mohammad Bavarian, Mark Chen, Heewoo Jun, Lukasz Kaiser, Matthias Plappert,
Jerry Tworek, Jacob Hilton, Reiichiro Nakano, Christopher Hesse, and John Schulman. Training verifiers to
solve math word problems, 2021. URL https://arxiv.org/abs/2110.14168. 7
Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. Bert: Pre-training of deep bidirectional
transformers for language understanding. In Proceedings of the 2019 conference of the North American chapter
of the association for computational linguistics: human language technologies, volume 1 (long and short papers),
pp. 4171–4186, 2019. 10
Qingxiu Dong, Li Dong, Yao Tang, Tianzhu Ye, Yutao Sun, Zhifang Sui, and Furu Wei. Reinforcement pre-
training. arXiv preprint arXiv:2506.08007, 2025. 2
Kanishk Gandhi, Ayush Chakravarthy, Anikait Singh, Nathan Lile, and Noah D. Goodman. Cognitive behaviors
that enable self-improving reasoners, or, four habits of highly effective stars, 2025. URL https://arxiv.
org/abs/2503.01307. 9
Bofei Gao, Feifan Song, Zhe Yang, Zefan Cai, Yibo Miao, Qingxiu Dong, Lei Li, Chenghao Ma, Liang Chen,
Runxin Xu, Zhengyang Tang, Benyou Wang, Daoguang Zan, Shanghaoran Quan, Ge Zhang, Lei Sha, Yichang
Zhang, Xuancheng Ren, Tianyu Liu, and Baobao Chang. Omni-math: A universal olympiad level mathematic
benchmark for large language models, 2024. URL https://arxiv.org/abs/2410.07985. 6
Etash Guha, Ryan Marten, Sedrick Keh, Negin Raoof, Georgios Smyrnis, Hritik Bansal, Marianna Nezhurina,
Jean Mercat, Trung Vu, Zayne Sprague, Ashima Suvarna, Benjamin Feuer, Liangyu Chen, Zaid Khan, Eric
Frankel, Sachin Grover, Caroline Choi, Niklas Muennighoff, Shiye Su, Wanjia Zhao, John Yang, Shreyas
Pimpalgaonkar, Kartik Sharma, Charlie Cheng-Jie Ji, Yichuan Deng, Sarah Pratt, Vivek Ramanujan, Jon
Saad-Falcon, Jeffrey Li, Achal Dave, Alon Albalak, Kushal Arora, Blake Wulfe, Chinmay Hegde, Greg Durrett,
Sewoong Oh, Mohit Bansal, Saadia Gabriel, Aditya Grover, Kai-Wei Chang, Vaishaal Shankar, Aaron Gokaslan,
Mike A. Merrill, Tatsunori Hashimoto, Yejin Choi, Jenia Jitsev, Reinhard Heckel, Maheswaran Sathiamoorthy,
Alexandros G. Dimakis, and Ludwig Schmidt. Openthoughts: Data recipes for reasoning models, 2025. URL
https://arxiv.org/abs/2506.04178. 6, 7, 16
Daya Guo, Dejian Yang, Haowei Zhang, Junxiao Song, Ruoyu Zhang, Runxin Xu, Qihao Zhu, Shirong Ma, Peiyi
Wang, Xiao Bi, et al. Deepseek-r1: Incentivizing reasoning capability in llms via reinforcement learning.
arXiv preprint arXiv:2501.12948, 2025. 1
Peter Hagoort, Lea Hald, Marcel Bastiaansen, and Karl Magnus Petersson. Integration of word meaning and
world knowledge in language comprehension. science, 304(5669):438–441, 2004. 1
Dan Hendrycks, Collin Burns, Steven Basart, Andy Zou, Mantas Mazeika, Dawn Song, and Jacob Steinhardt.
Measuring massive multitask language understanding, 2021a. URL https://arxiv.org/abs/2009.03300.
7
11

--- Page 12 ---

RLP: Reinforcement as a Pretraining Objective
Dan Hendrycks, Collin Burns, Saurav Kadavath, Akul Arora, Steven Basart, Eric Tang, Dawn Song, and Jacob
Steinhardt. Measuring mathematical problem solving with the math dataset. arXiv preprint arXiv:2103.03874,
2021b. 7, 16
Dan Hendrycks, Collin Burns, Saurav Kadavath, Akul Arora, Steven Basart, Eric Tang, Dawn Song, and Jacob
Steinhardt. Measuring mathematical problem solving with the math dataset. NeurIPS, 2021c. 7
Jingcheng Hu, Yinmin Zhang, Qi Han, Daxin Jiang, Xiangyu Zhang, and Heung-Yeung Shum. Open-reasoner-
zero: An open source approach to scaling up reinforcement learning on the base model, 2025.
URL
https://arxiv.org/abs/2503.24290. 17
Hugging Face. Open r1: A fully open reproduction of deepseek-r1, January 2025. URL https://github.com/
huggingface/open-r1. 16
Nathan Lambert, Jacob Morrison, Valentina Pyatkin, Shengyi Huang, Hamish Ivison, Faeze Brahman, Lester
James V Miranda, Alisa Liu, Nouha Dziri, Shane Lyu, et al. Tulu 3: Pushing frontiers in open language model
post-training. arXiv preprint arXiv:2411.15124, 2024. 1
Aitor Lewkowycz, Anders Andreassen, David Dohan, Ethan Dyer, Henryk Michalewski, Vinay Ramasesh,
Ambrose Slone, Cem Anil, Imanol Schlag, Theo Gutman-Solo, et al. Solving quantitative reasoning problems
with language models. Advances in neural information processing systems, 35:3843–3857, 2022. 7
Mingjie Liu, Shizhe Diao, Ximing Lu, Jian Hu, Xin Dong, Yejin Choi, Jan Kautz, and Yi Dong. Prorl: Prolonged
reinforcement learning expands reasoning boundaries in large language models, 2025a.
URL https:
//arxiv.org/abs/2505.24864. 17
Wei Liu, Siya Qi, Xinyu Wang, Chen Qian, Yali Du, and Yulan He. Nover: Incentive training for language
models via verifier-free reinforcement learning. arXiv preprint arXiv:2505.16022, 2025b. 8, 10
Ilya Loshchilov and Frank Hutter. Decoupled weight decay regularization. In International Conference on
Learning Representations, 2019. URL https://openreview.net/forum?id=Bkg6RiCqY7. 16
Michael Luo,
Sijun Tan,
Justin Wong,
Xiaoxiang Shi,
William Y. Tang,
Manan Roongta,
Colin
Cai,
Jeffrey Luo,
Li Erran Li,
Raluca Ada Popa,
and Ion Stoica.
Deepscaler:
Surpassing
o1-preview
with
a
1.5b
model
by
scaling
rl.
https://pretty-radio-b75.notion.site/
DeepScaleR-Surpassing-O1-Preview-with-a-1-5B-Model-by-Scaling-RL-19681902c1468005bed8ca303013a4e2,
2025. Notion Blog. 17
Paul Metzner, Titus von der Malsburg, Shravan Vasishth, and Frank Rösler. Brain responses to world knowledge
violations: A comparison of stimulus-and fixation-triggered event-related potentials and neural oscillations.
Journal of Cognitive Neuroscience, 27(5):1017–1028, 2015. 1
NVIDIA Nemotron Nano. Efficient hybrid mamba-transformer reasoning model. arXiv preprint arXiv:2508.14444,
2025. 6, 7, 8, 10
Long Ouyang, Jeffrey Wu, Xu Jiang, Diogo Almeida, Carroll Wainwright, Pamela Mishkin, Chong Zhang,
Sandhini Agarwal, Katarina Slama, Alex Ray, et al. Training language models to follow instructions with
human feedback. Advances in neural information processing systems, 35:27730–27744, 2022. 1
Alec Radford, Karthik Narasimhan, Tim Salimans, Ilya Sutskever, et al. Improving language understanding by
generative pre-training. 2018. 10
Colin Raffel, Noam Shazeer, Adam Roberts, Katherine Lee, Sharan Narang, Michael Matena, Yanqi Zhou, Wei
Li, and Peter J Liu. Exploring the limits of transfer learning with a unified text-to-text transformer. Journal
of machine learning research, 21(140):1–67, 2020. 10
David Rein, Betty Li Hou, Asa Cooper Stickland, Jackson Petty, Richard Yuanzhe Pang, Julien Dirani, Julian
Michael, and Samuel R. Bowman. GPQA: A graduate-level google-proof q&a benchmark. In First Conference
on Language Modeling, 2024. URL https://openreview.net/forum?id=Ti67584b98. 7
12

--- Page 13 ---

RLP: Reinforcement as a Pretraining Objective
Amrith Setlur, Matthew Y. R. Yang, Charlie Snell, Jeremy Greer, Ian Wu, Virginia Smith, Max Simchowitz,
and Aviral Kumar. e3: Learning to explore enables extrapolation of test-time compute for llms, 2025. URL
https://arxiv.org/abs/2506.09026. 8
Claude E Shannon. Prediction and entropy of printed english. Bell system technical journal, 30(1):50–64, 1951.
10
Mohammad Shoeybi, Mostofa Patwary, Raul Puri, Patrick LeGresley, Jared Casper, and Bryan Catanzaro.
Megatron-lm: Training multi-billion parameter language models using model parallelism. arXiv preprint
arXiv:1909.08053, 2019. 16
Shaden Smith, Mostofa Patwary, Brandon Norick, Patrick LeGresley, Samyam Rajbhandari, Jared Casper, Zhun
Liu, Shrimai Prabhumoye, George Zerveas, Vijay Korthikanti, et al. Using deepspeed and megatron to train
megatron-turing nlg 530b, a large-scale generative language model. arXiv preprint arXiv:2201.11990, 2022.
10
Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N Gomez, Łukasz Kaiser, and
Illia Polosukhin. Attention is all you need. Advances in neural information processing systems, 30, 2017. 10
Yubo Wang, Xueguang Ma, Ge Zhang, Yuansheng Ni, Abhranil Chandra, Shiguang Guo, Weiming Ren, Aaran
Arulraj, Xuan He, Ziyan Jiang, Tianle Li, Max Ku, Kai Wang, Alex Zhuang, Rongqi Fan, Xiang Yue, and Wenhu
Chen. Mmlu-pro: A more robust and challenging multi-task language understanding benchmark, 2024. URL
https://arxiv.org/abs/2406.01574. 7
Zengzhi Wang, Fan Zhou, Xuefeng Li, and Pengfei Liu. Octothinker: Revisiting mid-training in the era of rl
scaling. https://tinyurl.com/OctoThinker, 2025. Notion Blog. 9
An Yang, Anfeng Li, Baosong Yang, Beichen Zhang, Binyuan Hui, Bo Zheng, Bowen Yu, Chang Gao, Chengen
Huang, Chenxu Lv, et al. Qwen3 technical report. arXiv preprint arXiv:2505.09388, 2025. 1, 6, 10
Weizhe Yuan, Richard Yuanzhe Pang, Kyunghyun Cho, Sainbayar Sukhbaatar, Jing Xu, and Jason Weston.
Self-rewarding language models. arXiv preprint arXiv:2401.10020, 3, 2024. 10
Xuandong Zhao, Zhewei Kang, Aosong Feng, Sergey Levine, and Dawn Song. Learning to reason without
external rewards. arXiv preprint arXiv:2505.19590, 2025. 10
Xiangxin Zhou, Zichen Liu, Anya Sims, Haonan Wang, Tianyu Pang, Chongxuan Li, Liang Wang, Min Lin, and
Chao Du. Reinforcing general reasoning without verifiers. arXiv preprint arXiv:2505.21493, 2025. 8
13

--- Page 14 ---

RLP: Reinforcement as a Pretraining Objective
8. Appendix
8.1. Proofs
In this section, we provide the proofs supporting the methodology in §2. We first prove the tokenwise cross-
entropy (CE) reduction identity (Prop. 1), then the lower bound via marginalization over thoughts (Prop. 2).
Finally, we state and prove Prop. 3, which formalizes the positionwise-credit claim described in §2.5: under
teacher forcing, averaging the expected tokenwise information-gain rewards across positions recovers the
expected per-token sequence-level CE improvement.
For convenience, we recall the key definitions from the main text: the reasoned and baseline log-evidence
𝑆pred(𝑐𝑡) = log 𝑝𝜃(𝑥𝑡| 𝑥<𝑡, 𝑐𝑡) and 𝑆ema = log ¯𝑝𝜑(𝑥𝑡| 𝑥<𝑡) (equation 3); the information-gain reward 𝑟(𝑐𝑡) =
𝑆pred(𝑐𝑡) −𝑆ema (equation 5); and the cross-entropy CE(𝑝, 𝑞)
def
= E𝑥∼𝑝
[︀
−log 𝑞(𝑥)
]︀
(equation 2).
8.2. Proof of Proposition 1 (Expected improvement identity)
Proof of Proposition 1. Fix the context 𝑥<𝑡and a realized thought 𝑐𝑡, and let 𝑝*
𝑡(𝑥) := 𝑝*(𝑥| 𝑥<𝑡) denote the
data distribution over 𝑥𝑡at this position. By the reward definition equation 5 together with equation 3,
𝑟(𝑐𝑡) = log 𝑝𝜃
(︀
𝑥𝑡| 𝑥<𝑡, 𝑐𝑡
)︀
−log ¯𝑝𝜑
(︀
𝑥𝑡| 𝑥<𝑡
)︀
.
Taking expectation with respect to 𝑥𝑡∼𝑝*
𝑡and using linearity of expectation,
E
𝑥𝑡∼𝑝*
𝑡
[︀
𝑟(𝑐𝑡)
]︀
=
E
𝑥𝑡∼𝑝*
𝑡
[︁
log 𝑝𝜃(𝑥𝑡| 𝑥<𝑡, 𝑐𝑡)
]︁
−
E
𝑥𝑡∼𝑝*
𝑡
[︁
log ¯𝑝𝜑(𝑥𝑡| 𝑥<𝑡)
]︁
.
By the definition of cross-entropy equation 2, CE(𝑝, 𝑞) = E𝑥∼𝑝[−log 𝑞(𝑥)], so each expectation of a log-
likelihood equals the negative cross-entropy:
E
𝑥𝑡∼𝑝*
𝑡
[︁
log 𝑝𝜃(𝑥𝑡| 𝑥<𝑡, 𝑐𝑡)
]︁
= −CE
(︀
𝑝*, 𝑝𝜃(· | 𝑥<𝑡, 𝑐𝑡)
)︀
,
E
𝑥𝑡∼𝑝*
𝑡
[︁
log ¯𝑝𝜑(𝑥𝑡| 𝑥<𝑡)
]︁
= −CE
(︀
𝑝*, ¯𝑝𝜑(· | 𝑥<𝑡)
)︀
.
Substituting into the previous display yields
E
𝑥𝑡∼𝑝*
𝑡
[︀
𝑟(𝑐𝑡)
]︀
= CE
(︀
𝑝*, ¯𝑝𝜑(· | 𝑥<𝑡)
)︀
−CE
(︀
𝑝*, 𝑝𝜃(· | 𝑥<𝑡, 𝑐𝑡)
)︀
,
which is the desired identity.
8.3. Proof of Proposition 2 (Lower bound via marginalization over thoughts)
Proof of Proposition 2. Fix (𝑥<𝑡, 𝑥𝑡) and recall 𝑆pred(𝑐𝑡) = log 𝑝𝜃(𝑥𝑡| 𝑥<𝑡, 𝑐𝑡) and ˜𝑝𝜃(𝑥| 𝑥<𝑡) = E𝑧𝑡∼𝜋𝜃(·|𝑥<𝑡)
[︀
𝑝𝜃(𝑥|
𝑥<𝑡, 𝑧𝑡)
]︀
.
(i) Jensen bound.
Conditioning on (𝑥<𝑡, 𝑥𝑡) and taking expectation over 𝑐𝑡∼𝜋𝜃(· | 𝑥<𝑡),
E𝑐𝑡∼𝜋𝜃
[︀
𝑆pred(𝑐𝑡)
]︀
= E𝑐𝑡
[︁
log 𝑝𝜃(𝑥𝑡| 𝑥<𝑡, 𝑐𝑡)
]︁
≤log E𝑐𝑡
[︁
𝑝𝜃(𝑥𝑡| 𝑥<𝑡, 𝑐𝑡)
]︁
= log ˜𝑝𝜃(𝑥𝑡| 𝑥<𝑡),
where the inequality is Jensen’s inequality applied to the concave function log(·). This proves (i) pointwise for
the realized 𝑥𝑡.
(ii) Bound on 𝐽(𝜃).
By definition of the reward in equation 5 and teacher forcing (see equation 3),
𝐽(𝜃) = E
[︁
E𝑐𝑡∼𝜋𝜃
[︀
𝑆pred(𝑐𝑡)
]︀
−𝑆ema
]︁
≤E
[︁
log ˜𝑝𝜃(𝑥𝑡| 𝑥<𝑡) −log ¯𝑝𝜑(𝑥𝑡| 𝑥<𝑡)
]︁
= E
[︂
log ˜𝑝𝜃(𝑥𝑡| 𝑥<𝑡)
¯𝑝𝜑(𝑥𝑡| 𝑥<𝑡)
]︂
,
where the inequality uses part (i) and the outer expectation is over (𝑥<𝑡, 𝑥𝑡) ∼𝒟. This proves (ii).
14

--- Page 15 ---

RLP: Reinforcement as a Pretraining Objective
Tightness.
Equality in (i) (and hence in (ii)) holds precisely when 𝑝𝜃(𝑥𝑡| 𝑥<𝑡, 𝑐𝑡) is almost surely constant in 𝑐𝑡under
𝜋𝜃(· | 𝑥<𝑡) (e.g., when the predictor ignores the thought or when the thought policy is degenerate).
8.4. Tokenwise–to–sequence connection under teacher forcing (positionwise credit)
This subsection formalizes the claim in §2.5 that summing positionwise CE improvements recovers the sequence-
level (per-token) improvement. The following proposition is new to the appendix and not required elsewhere; it
clarifies how tokenwise rewards aggregate at the sequence level under teacher forcing.
Proposition 3 (Tokenwise–to–sequence connection under teacher forcing). Let 𝑥= (𝑥1, . . . , 𝑥𝑇) be drawn from
the data distribution 𝑝*(𝑥) and fix a policy 𝜋𝜃(𝑐𝑡|𝑥<𝑡), the reasoned scorer 𝑝𝜃(·|𝑥<𝑡, 𝑐𝑡), and the no-think baseline
¯𝑝𝜑(·|𝑥<𝑡). Define the sequence-level (per-token) cross-entropy for the baseline and the (stochastic) reasoned scorer
by
CEseq
(︀
𝑝*, ¯𝑝𝜑
)︀
:= E𝑥∼𝒟
[︃
−1
𝑇
𝑇
∑︁
𝑡=1
log ¯𝑝𝜑(𝑥𝑡| 𝑥<𝑡)
]︃
,
CEseq
(︀
𝑝*, 𝑝𝜃[𝜋𝜃]
)︀
:= E𝑥∼𝒟
[︃
−1
𝑇
𝑇
∑︁
𝑡=1
E𝑐𝑡∼𝜋𝜃(·|𝑥<𝑡)
[︀
log 𝑝𝜃(𝑥𝑡| 𝑥<𝑡, 𝑐𝑡)
]︀
]︃
.
Then the average over positions of the expected tokenwise information-gain rewards equals the per-token sequence-
level CE improvement of the reasoned scorer against the baseline:
E𝑥
[︃
1
𝑇
𝑇
∑︁
𝑡=1
E𝑐𝑡∼𝜋𝜃(·|𝑥<𝑡) E𝑥𝑡∼𝑝*(·|𝑥<𝑡)
[︀
𝑟(𝑐𝑡)
]︀
]︃
= CEseq
(︀
𝑝*, ¯𝑝𝜑
)︀
−CEseq
(︀
𝑝*, 𝑝𝜃[𝜋𝜃]
)︀
.
Proof. (i) Conditional independence under teacher forcing. At position 𝑡, teacher forcing samples the target
token from the data channel while the thought is sampled from the policy given the same prefix:
𝑥𝑡∼𝑝*(· | 𝑥<𝑡),
𝑐𝑡∼𝜋𝜃(· | 𝑥<𝑡).
Hence
𝑝(𝑐𝑡, 𝑥𝑡| 𝑥<𝑡) = 𝜋𝜃(𝑐𝑡| 𝑥<𝑡) 𝑝*(𝑥𝑡| 𝑥<𝑡),
i.e.
𝑐𝑡⊥𝑥𝑡| 𝑥<𝑡.
This implies E𝑥𝑡∼𝑝*(·|𝑥<𝑡,𝑐𝑡)[·] = E𝑥𝑡∼𝑝*(·|𝑥<𝑡)[·].
(ii) Positionwise CE reduction. By Proposition 1, for any fixed (𝑥<𝑡, 𝑐𝑡),
E𝑥𝑡∼𝑝*(·|𝑥<𝑡)
[︀
𝑟(𝑐𝑡)
]︀
= CE
(︀
𝑝*, ¯𝑝𝜑(· | 𝑥<𝑡)
)︀
−CE
(︀
𝑝*, 𝑝𝜃(· | 𝑥<𝑡, 𝑐𝑡)
)︀
.
Taking expectation over 𝑐𝑡∼𝜋𝜃(· | 𝑥<𝑡) and using linearity of expectation gives
E𝑐𝑡E𝑥𝑡
[︀
𝑟(𝑐𝑡)
]︀
= CE
(︀
𝑝*, ¯𝑝𝜑(· | 𝑥<𝑡)
)︀
−E𝑐𝑡CE
(︀
𝑝*, 𝑝𝜃(· | 𝑥<𝑡, 𝑐𝑡)
)︀
.
(iii) Sum over positions. Average the identity in (ii) over 𝑡= 1, . . . , 𝑇and over 𝑥∼𝒟:
E𝑥
[︃
1
𝑇
𝑇
∑︁
𝑡=1
E𝑐𝑡E𝑥𝑡
[︀
𝑟(𝑐𝑡)
]︀
]︃
= E𝑥
[︃
1
𝑇
𝑇
∑︁
𝑡=1
CE
(︀
𝑝*, ¯𝑝𝜑(· | 𝑥<𝑡)
)︀
]︃
−E𝑥
[︃
1
𝑇
𝑇
∑︁
𝑡=1
E𝑐𝑡CE
(︀
𝑝*, 𝑝𝜃(· | 𝑥<𝑡, 𝑐𝑡)
)︀
]︃
.
By the definition of cross-entropy in equation 2 and the chain rule for likelihoods,
E𝑥𝑡∼𝑝*(·|𝑥<𝑡)
[︀
−log ¯𝑝𝜑(𝑥𝑡| 𝑥<𝑡)
]︀
= CE
(︀
𝑝*, ¯𝑝𝜑(· | 𝑥<𝑡)
)︀
,
and similarly for the reasoned scorer inside the 𝑐𝑡-expectation. Therefore the two sums on the right are exactly
CEseq
(︀
𝑝*, ¯𝑝𝜑
)︀
and CEseq
(︀
𝑝*, 𝑝𝜃[𝜋𝜃]
)︀
as defined above, yielding the claimed equality.
15

--- Page 16 ---

RLP: Reinforcement as a Pretraining Objective
9. Experimental Setup
RLP:
We employ RLP on both base and intermediate checkpoints using diverse datasets. To facilitate this, we use
Hugging Face (2025) as the RL training backbone and deploy training using 32 H100 80GB SXM5 GPUs for
170M to 10B tokens. We train the base models with key settings including a constant learning rate of 1𝑒−6, a
batch size of 512 and a maximum context length of 2048 tokens. Each generation step contains 512 unique
prompts sampled from the dataset, and performing 16 rollouts with temperature 0.7. We set KL coefficient to
0 across all runs.
Continuous Pre-training:
We continuously pretrain the ℳbase model using both general pretraining and specialized post-training corpus
to draw comparison between pretraining and RLP training objective. For this experimentation, we use
Megatron-LM (Shoeybi et al., 2019) as the pretraining backbone and continuously train on 32 H100 80GB
SXM5 GPUs for 170M to 10B tokens depending on the data size and comparison requirement. During training,
we use the AdamW optimizer (Loshchilov & Hutter, 2019) with 𝛽1 = 0.9, 𝛽2 = 0.95 and weight decay of 0.1.
We use a 2-way tensor and pipeline parallelism to train the model. We set the maximum value of learning rate
to 1𝑒−6, minimum to 1𝑒−7, and use a batch size of 6M tokens with a 8192 context length.
Post-Training:
For supervised fine-tuning (SFT), we use the OpenThoughts3 dataset (Guha et al., 2025). We filtered examples
that did not include a final answer. With this filtering scheme, the total number of samples for SFT post-training
is 45, 6024. For RLVR, we used the The Mathematics Aptitude Test of Heuristics (MATH) dataset (Hendrycks
et al., 2021b) with 7, 500 examples. This dataset includes problems from various subjects such as algebra,
geometry, number theory and precalculus. We trained models in all RLVR experiments for 1 epoch with a
global batch size of 1024 and used cosine annealing and an initial learning rate of 1𝑒−6.
10. Extended ablation details
Table S.1 reports per-task accuracies for each setting, and Fig. 2 provides the corresponding curves for (a)
rollout count, (b) completion length, and (c) KL coefficient. Unless stated, each sweep holds the other two
dimensions at the best configuration (16 rollouts, completion length 2048, 𝛽= 0).
Rollout count. Increasing 𝐺improves accuracy up to 𝐺= 16, where Overall reaches 42.17% (from 34.03%,
+8.14 points). The largest taskwise lifts at 𝐺= 16 relative to the base are gsm8k (+22.96), math-500
(+13.85), miva (+7.20), MMLU (+6.35), and MMLU-Pro (+6.20), while GPQA is unchanged (27.51 vs
27.52). Moving from 𝐺= 16 to 𝐺= 32 slightly lowers Overall to 41.75 (−0.42), driven mainly by GPQA
(−2.13), with other tasks nearly flat (e.g., MMLU-Pro +0.79, MMLU −0.24). This suggests diminishing
returns once the group-relative estimator is already well-sampled.
Completion length. Capacity on the thought channel dominates performance. Very short completions
underperform sharply: at length 64, Overall is 11.50 and Math averages 1.12. Increasing to 512 raises Overall
to 24.65 and Math to 22.63. The main jump occurs between 512 and 1024 (Overall +14.24 to 38.89; gsm8k
+28.55; math-500 +36.85). Extending to 2048 adds a smaller but consistent gain (Overall 42.17, +3.28 over
1024; Math/Science 48.06/36.29). Pushing to 4096 gives only a marginal change (Overall 42.21, +0.04; small
taskwise shifts such as MMLU-Pro +0.64 and gsm8k −0.62), so 2048 is the preferred trade-off.
KL coefficient. Adding a token-level KL toward a fixed reference does not help overall. At 𝛽= 10−4 and
10−3, Overall is 41.35 and 41.44 (−0.82 and −0.73 vs 𝛽= 0). There are isolated improvements (MMLU-Pro
+1.43 at 10−4; AMC23 +1.88 at 10−3), but these are offset by broader declines (e.g., gsm8k −1.26 and −2.82;
GPQA −2.01 and −1.51). The KL term also increases memory use and step time. We therefore keep 𝛽= 0 in
the main recipe.
In summary, the appendix table provides the taskwise breakdown behind these trends, and the figure shows
the smooth saturation with rollouts, the strong length-driven regime change between 512 and 1024 tokens,
16

--- Page 17 ---

RLP: Reinforcement as a Pretraining Objective
Table S.1: Ablations on rollout count, completion length, and KL weight 𝛽with qwen3-1.7b-base. All numbers
denote accuracy (%).
Model / Variant
Tasks (%)
Macro avg (%)
MATH500
GSM8K
AMC23
Minerva
MMLU
MMLU-Pro
GPQA
Math
Science
Overall
Baseline
Qwen3-1.7B-Base
48.45
54.16
25.94
15.30
44.85
23.95
27.52 35.96
32.11
34.03
Ablation: # rollouts
num_rollouts=4
59.45
74.79
33.44
21.78
50.83
28.81
26.52 47.37
35.39
41.38
num_rollouts=8
61.70
76.93
30.62
22.06
50.88
30.55
26.77 47.83
36.07
41.95
num_rollouts=16†
62.30
77.12
30.31
22.50
51.20
30.15
27.51 48.06
36.29
42.17
num_rollouts=32
60.45
77.26
30.94
22.29
50.96
30.94
25.38 47.74
35.76
41.75
Ablation: completion length
completion_length=64
1.00
2.84
0.62
0.00
33.26
15.46
16.92
1.12
21.88
11.50
completion_length=128
1.73
3.17
0.94
0.05
29.04
13.94
12.37
1.47
18.45
9.96
completion_length=256
2.95
13.86
2.81
0.46
37.19
17.09
15.15
5.02
23.14
14.08
completion_length=512
21.35
46.58
16.25
6.34
42.27
19.82
17.93 22.63
26.67
24.65
completion_length=1024
58.20
75.13
28.80
20.47
48.36
27.74
20.31 45.65
32.14
38.89
completion_length=2048†
62.30
77.12
30.31
22.50
51.20
30.15
27.51 48.06
36.29
42.17
completion_length=4096
62.00
76.50
30.60
22.80
51.30
30.79
27.27 47.98
36.45
42.21
Ablation: KL weight 𝛽
𝛽= 10−4
61.35
75.86
28.00
21.50
51.00
31.58
25.50 46.68
36.03
41.35
𝛽= 10−3
60.90
74.30
32.19
20.73
50.73
30.80
26.00 47.03
35.84
41.44
𝛽= 0†
62.30
77.12
30.31
22.50
51.20
30.15
27.51 48.06
36.29
42.17
and the lack of net benefit from KL.
11. Additional Ablations
Does the improvement sustain if we make Pretraining compute equivalent to RLP?
For both comparisons, the configuration for RLP remains fixed, based on a budget of 𝑇𝑖𝑛𝑝= 170𝑀input
tokens. First, we establish a baseline by continuing the pretraining of the base model on an identical 170M
tokens (Base + CPT, Input Token). Second, to create a FLOP-equivalent baseline, we first approximate the
total computational cost of RLP. The effective token budget, 𝑇𝑓𝑙𝑜𝑝, can be estimated by summing the tokens
used for gradient updates (𝑇𝑖𝑛𝑝) and the tokens processed during the rollout phase:
𝑇𝑓𝑙𝑜𝑝= (𝑛× 𝑙𝑠𝑒𝑞× 𝑏𝑠× 𝑖𝑡𝑒𝑟𝑠) + 𝑇𝑖𝑛𝑝
where 𝑛is the number of rollouts per instance, 𝑙𝑠𝑒𝑞is the sequence length, 𝑏𝑠is the batch size and 𝑖𝑡𝑒𝑟𝑠is the
number of steps RLP has gone through. This calculation results in an effective budget of approximately 6B
tokens for our model. We therefore train a second, more powerful CPT baseline on 6B tokens (Base + CPT,
Flop Usage), holding all other hyperparameters constant.
RLP resonates well in presence of multidomain data.
Model
Dataset
Math Avg@1[8]
Science Avg
Science Avg@1[4]
Average
ℳbase
-
35.96
34.50
32.11
34.19
ℳRLP
Only Math
48.23
41.64
36.77
42.21
Only Science
49.17
39.65
38.26
42.36
Combined
49.76
42.54
37.78
43.36
Table S.2: Ablation on math, science, and combined domains. RLP shows particularly strong generalization
in presence of multi-domain data.
Recent works have shown tremendous improvement in reasoning tasks, particularly in mathematics, through
RLVR (Liu et al., 2025a; Luo et al., 2025; Hu et al., 2025). However, these methods are often tied to the
complexity of queries, limiting their scalability. To draw a parallel, we evaluate RLP on Nemotron-Crossthink
using different blends of math and science data. As shown in Table S.2, training only on math yields substantial
17

--- Page 18 ---

RLP: Reinforcement as a Pretraining Objective
math improvements, but comes at the cost of weaker generalization to science. Conversely, training only on
science improves science accuracy, but underperforms in math compared to math-only training. Strikingly,
combining both domains provides the best overall average, indicating that RLP is able to leverage complementary
signals from multiple domains without diluting the benefits within each. This suggests that RLP not only scales
beyond single-domain specialization but also thrives in multidomain settings where diverse reasoning styles
reinforce one another.
18

```
