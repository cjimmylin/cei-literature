---
title: "TreeRL 2506.11902"
source_pdf: "AI Labs/Zhipu AI/Papers/TreeRL_2506.11902.pdf"
company: "Zhipu AI"
pages: 15
extracted_at: "2026-01-31T17:32:40.715190"
type: "ai_lab_paper"
---

# TreeRL 2506.11902

**Company/Lab:** Zhipu AI
**Source PDF:** AI Labs/Zhipu AI/Papers/TreeRL_2506.11902.pdf
**Total Pages:** 15

---

## Content

```
--- Page 1 ---

arXiv:2506.11902v1  [cs.LG]  13 Jun 2025
TreeRL: LLM Reinforcement Learning with On-Policy Tree Search
Zhenyu Hou*,1
Ziniu Hu*,2
Yujiang Li*,1
Rui Lu*,1
Jie Tang1
Yuxiao Dong1
1Tsinghua University
2California Institute of Technology
Abstract
Reinforcement learning (RL) with tree search
has demonstrated superior performance in tra-
ditional reasoning tasks. Compared to conven-
tional independent chain sampling strategies
with outcome supervision, tree search enables
better exploration of the reasoning space and
provides dense, on-policy process rewards dur-
ing RL training but remains under-explored
in On-Policy LLM RL. We propose TreeRL,
a reinforcement learning framework that di-
rectly incorporates on-policy tree search for
RL training. Our approach includes interme-
diate supervision and eliminates the need for
separate reward model training. Existing ap-
proaches typically train a separate process re-
ward model, which can suffer from distribu-
tion mismatch and reward hacking. We also
introduce a cost-effective tree search approach
that achieves higher search efficiency under the
same generation token budget by strategically
branching from high-uncertainty intermediate
steps rather than using random branching. Ex-
periments on challenging math and code rea-
soning benchmarks demonstrate that TreeRL
achieves superior performance compared to tra-
ditional ChainRL, highlighting the potential of
tree search for LLM. TreeRL is open-sourced
at https://github.com/THUDM/TreeRL.
1
Introduction
Large language models (LLMs) have demonstrated
remarkable capabilities across diverse complex rea-
soning tasks (Achiam et al., 2023; Team et al.,
2023; Dubey et al., 2024), including mathemat-
ics (Shao et al., 2024b), programming (Lozhkov
et al., 2024; Zhu et al., 2024), and autonomous
agents (Zhou et al., 2024). Reinforcement learn-
ing (RL) has emerged as a powerful approach
to significantly improve the reasoning abilities of
LLMs by optimizing the policy through reward
*Equal contribution; order is alphabetical.
2
14
2
15
2
16
Inference Budget
50
55
60
65
70
PassRate(%)
MCTS
Multi-chain
EPTree
GLM4-9B
Qwen-2.5-14B
24.7
36.0
+2.5
+5.6
+4.6
+8.5
SFT
ChainRL
TreeRL(Ours)
Figure 1: Left: Performance comparison of sampling
strategies. EPTree consistently outperforms i.i.d multi-
chain sampling and MCTS under different inference
budgets. Right: TreeRL powered with EPTree demon-
strates better performance than ChainRL with i.i.d multi-
chain sampling.
feedback (OpenAI, 2024; Guo et al., 2025; Hou
et al., 2025; Shao et al., 2024b).
Current RL methods for LLM training generally
independently sample multiple trajectories (Shao
et al., 2024b; Wang et al., 2024b; Touvron et al.,
2023) and obtain reward signals based on the final
answers. However, tree search, which has demon-
strated significant success in other domains like
AlphaZero (Silver et al., 2017), remains under-
developed in reinforcement learning for LLM rea-
soning. Existing efforts have mainly focused on
using tree search to enhance inference-time per-
formance alongside an external reward (Zhang
et al., 2024a; Chen et al., 2024a), or to produce
data for offline training (Chen et al., 2024a; Xie
et al., 2024; Zhang et al., 2024a) (e.g., finetuning
or DPO (Rafailov et al., 2023)), as illustrated in
Figure 2. But Guo et al. (2025) also demonstrates
the limitation of distribution shift and reward hack-
ing in offline tree search compared to online RL
training. Up to now, the potential of on-policy RL
training incorporating tree search to improve LLM
reasoning remains largely unexplored.
The challenges are two-fold.
First, classical
Monte Carlo Tree Search (MCTS) (Browne et al.,
2012) can be less effective nd efficient than inde-

--- Page 2 ---

Policy Model
TreeRL (Ours): On-policy Tree search
with process supervision  
…
+1
+1
+1
0
0
0
+1
+1
0
+1/2
+1
+1/3
ChainRL : i.i.d sampling
with outcome supervision
RL Training
RL Sampling
SFT/DPO
Policy Model
RL Training
RL Sampling
Offline  training with Tree  search
Figure 2: Illustration of offline training with tree search (Left), traditional ChainRL with online i.i.d multi-response
sampling (Middle), and TreeRL with tree search (Right).
pendently sampling multiple responses. MCTS
achieves a lower PassRate performance under the
same inference cost, as shown in Figure 1. The
step-by-step generation requires numerous itera-
tions and is not friendly to modern LLM inference
engines. Second, though tree search could provide
fine-grained process supervision, the derived of-
fline process reward model almost contributes to
no performance improvement in RL training (Guo
et al., 2025).
To address this gap, we propose TreeRL, a rein-
forcement learning (RL) approach for LLMs em-
ployed with tree search. Under the same inference
cost as independent multiple sampling, our method
generates more diverse and effective responses and
also provides on-policy process supervision signals
to further boost RL performance.
First, we introduce an efficient and effective
tree search strategy EPTree. Unlike MCTS which
breaks answers into smaller parts to allow the
model to explore step-by-step, we obtain a new
response by forking branches from the most uncer-
tain intermediate tokens in the existing tree based
on entropy and continuing the generation until the
final answer. Thus EPTree requires fewer tokens
but encourages effective exploration for the diverse
answers. And it typically requires only around two
iterations to form the generation trees.
One step further, we leverage the tree search for
reinforcement learning with process supervision.
Each step in the trees is assigned a credit based on
advantage, i.e., how much that step improves the
likelihood of reaching a correct solution compared
to other steps. The process signal for a given rea-
soning step is calculated as a weighted sum of two
components: 1) global advantage, which reflects
the step’s potential over the overall correctness rate
for the question, and 2) local advantage, which
quantifies the improvement the step provides com-
pared to its parent step in the tree. Since these
advantage signals are derived directly from the on-
policy generated trees, they are inherently resistant
to reward hacking (Skalse et al., 2022) and do not
rely on any additional reward models.
We evaluate TreeRL on challenging college-
level and competition-level math and code rea-
soning benchmarks based on Qwen (Qwen, 2024)
and GLM (GLM et al., 2024). Experiments show
that TreeRL achieves superior performance and
demonstrates advantages over traditional indepen-
dent multi-chain sampling. The gain benefits from
both EPTree with promising PassRate performance
and process supervision. These results highlight
the potential of RL with tree search to advance
complex reasoning capabilities for LLM. The im-
plementation of TreeRL is available at https:
//github.com/THUDM/TreeRL.
2
Preliminary
To align the fine-tuned model πθ with feedback
signals, Ouyang et al. (2022) proposes to apply
reinforcement learning (RL) to enable LLM to
learn from self-exploration. Reinforcement learn-
ing maximizes a reward signal, e.g., human pref-
erence or final answer correctness. The typical
RL for the LLM process works as follows: for a
given prompt x, the policy model πθ generates K
possible responses, denoted as (y1, . . . , yK). The
reward function r(x, yi) then assigns a scalar re-
ward to each pair (x, yi). Afterward, the policy
model πθ is updated using reinforcement learning
to optimize the following objective:
E
x∼pdata,y∼πθ
1
K
K
X
i
A(x, yi) log πθ(yi|x)
(1)
where A(·) is the advantage function and usually
defined as A(x, yi) = β(r(x, yi) −b), where b

--- Page 3 ---

…
Initialization
Iteration 1
Iteration 2
Policy Model Training
Identify tokens 
with high entropy
Expansion
Tree with Process Signals
V = 1
2
W
19Y3ipulre2d3bK9t9SUSIJbZKIR7LjY0U5E7Spmea0E0uKQ5/Ttj+mfrtRyoVi8SDnsTUC/FQsIARrI3Ut8t3/avLXiAxSd0srWV9u+JUnRnQMnFzUoEcjb791RtEJAmp0IRjpbquE2svxVIzwmlW6iWKxpiM8ZB2DRU4pMpLZ4dn6NgoAxRE0pTQaKb+nkhxqNQk9E1niPVILXpT8T+vm+jgwkuZiBNBZkvChKOdISmKaABk5RoPjE8nMrYiMsElBm6xKJgR38eVl0qpV3bOqe39aqV/ncRThEI7gBFw4hzrcQgOaQCBZ3iFN+vJer
HerY95a8HKZw7gD6zPHxfQkrs=</latexit>
LA = 1
2
GA = 2
5
V = 1
PassRatio = 3
5
r
cCeilqKNjRDBRCEXwt5mLlncuz1258TjiLWNf8XGQhFb/4Cd/8ZNcoUmPh4vDfDzLwgkcKg6347M7Nz8wuLS8uldW19Y3y5lbTqFRzaHAlb4JmAEpYmigQAk3iQYWBRKug9uzoX9B9oIFV9hlkA7Yr1YhIztFKnXPE
R7jEI87qSgmf0QnVBDugD9RPR8bEPyDrlqltzR6DTxCtIlRSod8pflfxNIYuWTGtDw3wXbONAouYVDyUwMJ47esBy1LYxaBaejXwZ01ypdGiptK0Y6Un9P5CwyJosC2xkx7JtJbyj+57VSDI/buYiTFCHm40VhKikqO
gyGdoUGjKzhHEt7K2U95lmHG18JRuCN/nyNGnu17zDmnd5UD05LeJYIjukQvaIR47ICTkndIgnDySZ/JK3pwn58V5dz7GrTNOMbN/sD5/AE845sr</latexit>Policy Model ⇡✓
RL sampling with Tree Search
Figure 3: Illustration of TreeRL. In each iteration, TreeRL first performs a tree search using EPTree, progressively
expanding branches from the top-N most uncertain tokens. The resulting tree, along with the process supervision
signals derived from each step, is then fed into reinforcement learning to update the policy model.
is the baseline (Mei et al., 2022; Chung et al.,
2021) and varies in different methods. For example,
A(yi) = r(yi)−mean{r(yi)}
std{r(yi)}
in GRPO (Shao et al.,
2024b) and A(yi) = r(yi) −
1
K−1
PK
j̸=i r(yi) in
RLOO (Ahmadian et al., 2024).
3
TreeRL: Reinforcement Learning with
Tree Search
In this section, we present TreeRL to improve
LLM reasoning with tree search. Figure 3 shows
the overview of TreeRL. We first present an effi-
cient and effective tree search algorithm EPTree,
which guides tree search by token-level uncertainty
instead of traditional Monte Carlo Tree Search
(MCTS) (Browne et al., 2012). Then, we show
how to integrate the tree search into reinforcement
learning with process supervision to improve rea-
soning capability further.
3.1
Entropy-Guided Tree Search
We aim to optimize the tree-search algorithm for
RL training and thus emphasize the PassRate met-
ric, which evaluates the algorithm’s ability to gen-
erate diverse yet correct answers under a given
inference budget. Furthermore, the tree-search al-
gorithm must be efficient and highly parallelizable.
In contrast, traditional MCTS requires numerous
iterative generations, making it less efficient in cur-
rent LLM inference engines like VLLM (Kwon
et al., 2023).
We propose an entropy-guided tree search al-
gorithm, EPTree. The core idea is to iteratively
expand the search tree by forking new branches
(nodes) from the top-N most uncertain tokens (as
measured by entropy) across existing trees. This
encourages exploration in regions of high model
uncertainty, leading to improved performance. Crit-
ically, EPTree can generate multiple trees in paral-
lel, and the expansion process requires only around
2 iterations to build a diverse and informative tree,
making it highly efficient. The algorithm runs the
following steps.
Initialization. To generate M trees in parallel,
we first construct M chains by generating M re-
sponses for a given prompt x as initialization of Ti
for further expansion:
Y (i) = {yi ∼πθ(· | x)}, for i = 1, 2, . . . , M
where πθ is the policy model and x is the prompt.
Forking token selection. Next, we aim to expand
the trees by forking new branches from the existing
trees. We propose forking from the tokens with
the highest uncertainty, as these tokens provide the
most informative signals for the model and encour-
age exploration. We use cross-entropy as a measure
of uncertainty, which quantifies the uncertainty in
the policy model πθ when predicting a given to-
ken. To promote expansion, the top-N tokens with
the highest entropy values are selected across the
whole tree Ti. Specifically, the entropy of each
token v in the tree Ti is calculated as follows:
Bi = Top-NH(·|x) {(t, H (yt | x, y<t)) | t ∈Ti}
where H(yt) = −log πθ(yt | x, y<t) denotes the
entropy of token yt. Additionally, we mask tokens

--- Page 4 ---

2
14
2
15
2
16
Generation Tokens
0
25
50
75
100
125
150
Response Number
16
32
64
(4,3,2,1)
(6,2,1,2)
(6,5,2,1)
(8,2,2,2)
(8,4,2,2)
128
256
512
MCTS
Multi-chain(i.i.d)
EPTree(Ours)
Figure 4: Generation diversity comparison of EPTree,
MCTS, and i.i.d.
multi-chain sampling.
Both EP-
Tree and MCTS produce approximately 2× different
responses compared to i.i.d. multi-chain sampling.
near the end of sequences, as the model is expected
to explore different reasoning paths rather than sim-
ply revisiting previous answers.
Expansion. Given the selected tokens for each tree,
we continue the generation process from these to-
kens to form new branches. For each forking point
t, with the prefix yt and prompt x, we generate T
different candidate responses until completion:
Y (i)
new ∼{πθ (· | x, y<t) , for (t, ·) ∈Bi}T
where y<t denotes the prefix response before token
t. This results in M × N × T tree nodes in total(
N × T for each tree Ti ), each corresponding to a
new response. The tree structure Ti is updated to
include these new nodes:
Ti ←Ti ∪Y (i)
new
After initialization, the forking and expansion
process is repeated for L iterations, leading to
M×(T ×N×L+1) leaves (responses). We denote
this entropy-guided tree search as an (M, N, L, T)-
tree, where M is the number of parallel trees, N is
the number of forked points per iteration, L is the
number of iterations, and T is the branching factor
at each forking point.
In comparison to independent multi-chain sam-
pling, the EPTree is capable of producing a larger
number of diverse responses under the same infer-
ence cost, as illustrated in Figure 4. This offers the
potential to enhance RL performance by learning
from more varied responses.
3.2
Reinforcement Learning with EPTree
In this part, we show how to integrate EPTree into
RL training. Beyond the superior potential to find
correct trajectories, hierarchical tree structures also
provide more fine-grained process supervision for
intermediate steps for RL training.
3.2.1
Process Supervision from Tree Search
At each step, we estimate the value using Monte
Carlo methods. Specifically, for a step sn (corre-
sponding to a node in the tree), let L(sn) denote the
set of all leaf nodes that are descendants of node
sn (including node sn itself if it is a leaf). The
value V (sn) of node sn is computed as the ratio of
correct leaf nodes among its descendants:
V (sn) =
1
|L(sn)|
X
l∈L(sn)
1(l is correct)
This value reflects the potential of the node sn to
lead to correct answers. Based on value, process su-
pervision for each step is defined using advantages,
i.e., how much a step is better than other steps,
which include both global and local advantages.
The global advantage of a step sn represents its
potential to lead to a correct outcome compared to
the overall correctness ratio of all samples. Without
loss of generality, assume that there exists a virtual
root node for all subtrees, and the value of the root
node V (root) represents the average correctness
of all generated responses. The global advantage is
then computed as:
GA(sn) = V (sn) −V (root)
(2)
Essentially, the global advantage of sn is equiv-
alent to the normalized value, which can be ob-
tained by first normalizing the reward across all
leaf nodes—subtracting the average reward—and
then calculating the average rewards for L(sn).
The local advantage of a node sn quantifies the
improvement the step sn provides compared to its
parent step p(sn) and is defined as:
LA(sn) = V (sn) −V (p(sn))
(3)
where V (p(sn)) denotes the value of the node
p(sn). LA(sn) > 0 indicates that step sn is more
likely to lead to the correct result than its parent
node, suggesting that this step should be encour-
aged, and vice versa.
To compute the final reward for each step, we
combine the global and local advantages as follows:
R(sn) = GA(sn) + LA(sn)
(4)
The definition could be viewed as a spe-
cial case of Generalized Advantage Estimation

--- Page 5 ---

Algorithm 1 TreeRL
Input: Prompt x, Policy πθ, Number of Trees M, Forking Points N, Iterations L, Branches T
Output: Optimized Policy π∗
θ
for i = 1 to M do
▷Create M trees with M(1 + NLT) leaves
Y (i) ←{yi ∼πθ(· | x)}, Ti ←{Y (i)}
▷Initialization
for l = 1 to L do
▷Iterative Expansion
H(yt) ←−log πθ(yt | x, y<t), ∀t ∈Ti
Bi,l ←Top-NH(·|x) {(t, H (yt | x, y<t)) | t ∈Ti}
for each selected forking point (t, ·) ∈Bi,l do
Y (i,l)
new ∼{πθ (· | x, y<t) , for (t, ·) ∈Bi,l}T
Ti ←Ti ∪Y (i,l)
new , j ∈{1, · · · , T}
for each step sn in Ti do
▷Process Reward Calculation
V (sn) ←
1
|L(sn)|
P
l∈L(sn) 1(l is correct)
R(sn) ←|L(sn)|−1/2
|
{z
}
Re-weight Factor
·[V (sn) −V (root)
|
{z
}
Global Advantage
+ V (sn) −V (p(sn)
|
{z
}
Local Advantage
]
Update πθ using RL with process reward by Policy Gradient
(GAE) (Schulman et al., 2015). The general form
of GAE in LLM is defined as:
A(sn →sn+t) = γtV (sn+t) −V (sn)
(5)
where t represents any integer time step, and γ is
typically set to 1 in most cases. Thus, the local
advantage defined in Eq 3 corresponds to the case
where t = 1, while the global advantage corre-
sponds to the case where n = 0. Inspired by the
GAE, the process supervision signal can be defined
as a more generalized format by considering not
only the root and direct parent but also all of its
ancestor nodes in the trajectory:
RGAE(sn) =
X
j∈P(sn)
λj · [V (sn) −V (sj)]
where P(sn) represents the set of ancestor nodes
of sn and λj denotes the weight of each step. In
this work, we focus on a special format that only
considers the direct parent and the root node.
3.2.2
Training with Process Superivison
At each iteration, we first utilize EPTree described
in Section 3.1 to generate M trees T = {Ti}M
i
for
the prompt, where each leaf node in T together
with its all prefix corresponds to a complete se-
quence. For each step in the tree, the process super-
vision signal is assigned based on Equation (4) to
reflect its importance.
The sequences {S1, S2, . . . , S(M×N×L×T+M)}
extracted from the trees are used for RL train-
ing. As all non-leaf steps appear in multiple se-
2
14
2
15
2
16
Generation Tokens
50
55
60
65
70
PassRate(%)
16
32
64
(4,3,2,1)
(6,2,1,2)
(6,5,2,1)
(8,2,2,2)
(8,4,2,2)
128
256
512
MCTS
Multi-chain(i.i.d)
EPTree(Ours)
Figure 5: Search performance of EPTree, MCTS, and
multi-chain sampling on Omni-MATH-500 using Qwen-
2.5-14B-SFT. EPTree consistently outperforms all base-
lines under the different inference costs.
quences and will be repeatedly computed in op-
timization, we downweight the reward of these
steps to prevent overfitting. The reward for each
non-leaf step is modified by dividing the square
root of the number of leaf nodes in its subtree:
R(sn) = R(sn)/
p
|L(sn)|. This adjustment leads
to improved performance in our experiments. The
overall pipeline of TreeRL is illustrated in Alg 1.
4
Experiment
4.1
Setup
Training Details. We train SFT models based
on Qwen-2.5-14B (Qwen, 2024) and GLM4-
9B (GLM et al., 2024) as initialization for RL train-
ing and finetune them using the public dataset from
(Hou et al., 2025) for 2 epochs. For DeepSeek-R1-

--- Page 6 ---

Table 1: Experiment results on math reasoning tasks. We report Accuracy(%) for all datasets.
MATH500
Omni-MA
TH-500
AIME2024
AMC
Olympiad
Bench
LiveCode
Bench
Avg
GPT-4o
76.6
26.8
9.3
45.8
43.3
29.5
38.6
Llama-3.1-8B-Instruct
52.8
15.0
10.9
22.6
15.6
11.6
21.4
Llama-3.3-70B-Instruct
73.9
27.9
24.2
50.9
35.7
25.5
39.7
GLM4-9B-chat
50.1
12.9
1.7
17.2
14.7
16.5
18.9
Qwen-2.5-7B-Instruct
76.5
26.0
13.3
41.9
35.0
16.8
34.9
Qwen-2.5-Math-7B-Instruct
82.7
29.7
16.7
50.6
40.7
8.1
38.1
Qwen-2.5-14B-Instruct
78.9
28.7
13.7
54.5
41.8
27.7
40.9
SFT (GLM-9B)
56.0
18.2
8.3
29.2
22.5
14.2
24.7
ChainRL (GLM-9B)
63.0
21.8
6.1
31.6
23.9
16.6
27.2
TreeRL (GLM-9B)
64.5
20.8
11.4
38.5
24.8
15.8
29.3
SFT (Qwen-2.5-14B)
76.6
29.5
10.6
48.0
36.9
14.5
36.0
ChainRL (Qwen-2.5-14B)
81.6
32.7
22.2
53.9
41.1
18.2
41.6
TreeRL (Qwen-2.5-14B)
81.7
36.7
28.0
55.9
44.6
20.8
44.5
SFT (R1-Distilled-Qwen-2.5-7B)
94.0
47.8
55.9
85.5
54.4
43.9
63.6
ChainRL (R1-Distilled-Qwen-2.5-7B)
93.6
48.1
59.7
85.5
54.5
46.1
64.5
TreeRL (R1-Distilled-Qwen-2.5-7B)
94.4
49.8
60.8
85.0
57.1
47.4
65.8
0
100
200
300
Training steps
32
34
36
38
Accuracy(%)
Overall Average Performance
ChainRL
TreeRL
0
100
200
300
Training steps
36
38
40
42
44
Accuracy(%)
OlympaidBench
ChainRL
TreeRL
0
100
200
300
Training steps
28
30
32
34
36
Accuracy(%)
Omni-MATH-500
ChainRL
TreeRL
(a) Experiments on Qwen-2.5-14B
0
100
200
300
Training steps
17
18
19
20
Accuracy(%)
Overall Average Performance
ChainRL
TreeRL
0
100
200
300
Training steps
20
22
24
26
28
Accuracy(%)
OlympaidBench
ChainRL
TreeRL
0
100
200
300
Training steps
18
20
22
Accuracy(%)
Omni-MATH-500
ChainRL
TreeRL
(b) Experiments on GLM4-9B
Figure 6: Performance comparison between TreeRL and ChainRL during training. We report the average perfor-
mance across all six datasets (Left), OlympiadBench (Middle), and Omni-MATH-500 (Right). The results for the
other benchmarks can be found in the Appendix D.
distilled-Qwen-2.5-7B, we directly use the open-
source model from (Guo et al., 2025) without fur-
ther finetuning. Then, to identify the best tree
search setting for RL under a given inference cost,
we investigate various combinations of hyperpa-
rameters (M, N, L, T) using the trained Qwen-2.5-
14B-SFT model on the Omni-MATH-500 dataset
with PassRate as the target metric, and the results
can be found in Table 4 in the Appendix. The
baseline i.i.d multi-chain samplings correspond to
setting N = L = T = 0.
For the RL training, we compare the perfor-
mance of RL using multi-chain sampling, referred
to as ChainRL, to the proposed TreeRL under
the same inference cost derived from the previous
search to ensure a fair comparison. For TreeRL,

--- Page 7 ---

we used sampling parameters (M, N, L, T) =
(6, 2, 1, 2), generating 30 responses per prompt.
This is comparable to multi-chain sampling with
16 responses per prompt, given similar generation
token budgets. Each iteration used 16 prompts for
a single gradient update, resulting in a batch size of
256 for ChainRL and 480 for TreeRL. Therefore,
TreeRL actually performs reinforcement learning
with the same inference cost but with more training
computation during training. We use rule-based
reward based on the correctness of the final answer,
i.e., +1 for correct and 0 for wrong. The KL ef-
ficiency is set to β = 10−4, with a learning rate
of 1.5 × 10−6. During sampling, the temperature
is 1.2, the top-p value is 0.95, and the maximum
sequence length is 8,192. For RL training, the train-
ing data all come from publicly available datasets,
including MATH-train (Hendrycks et al., 2021) and
NuminaMath (Li et al., 2024a), and we sample a
subset for training.
Evaluation We use PassRate to evaluate the ef-
fectiveness of the proposed tree search algorithm.
PassRate measures the potential of a model to reach
at least one correct answer among all the generated
solutions. It should be noted that we compare tree
sampling and chain sampling under similar infer-
ence budgets, i.e., generation tokens. Specifically,
given an evaluation dataset D, for each sample
d ∈D, let Ld be the set of generated responses and
c(l) ∈{0, 1} be a binary indicator of correctness
for a response l. The PassRate is computed as:
PassRate =
1
|D|
X
d∈D
max
l∈Ld
c(l)
For reinforcement learning, we evaluate the policy
model on 6 challenging reasoning benchmarks us-
ing greedy sampling, including MATH(Hendrycks
et al., 2021), Omni-MATH (Gao et al., 2024),
AIME2024(Li et al., 2024a), AMC(Li et al.,
2024a), OlympiadBench(He et al., 2024), and Live-
CodeBench (Jain et al., 2024). For the MATH
dataset, we use a subset known as MATH500 based
on the split defined by (Lightman et al.). For Omni-
MATH, we randomly sample a subset for evalu-
ation, named Omni-MATH-500, which consists
of 500 examples for efficient yet comprehensive
assessment. Each dataset undergoes multiple eval-
uations to minimize variance; for instance, we eval-
uate MATH500 and Omni-MATH-500 three times
each, while AIME is evaluated 32 times, consider-
ing AIME2024 consists of only 30 questions. For
LiveCodeBench, we report the performance using
the data between 202407 to 202411.
4.2
Results of EPTree
Table 4 shows the overall performance on Omni-
MATH-500 and illustrates the efficiency and effec-
tiveness trade-off across different sampling meth-
ods. EPTree demonstrates a significant advantage
over the baseline multi-chain sampling method and
the MCTS method under the same inference cost.
And EPTree shows consistently better performance
across different generation costs and outperforms
the multi-chain sampling by around 3% in Pass-
Rate. Compared to MCTS, EPTree demonstrates a
more significant advantage, with the margin widen-
ing as the inference cost increases.
4.3
Results on RL training
Table 1 presents the performance of various sam-
pling strategies in RL training. Notably, TreeRL
equipped with EPTree sampling outperforms tradi-
tional multi-chain sampling across different bench-
marks. In particular, Figure 6 illustrates the evalua-
tion performance over various training steps. While
both sampling strategies exhibit similar perfor-
mance during the early stages of training, TreeRL
begins to show an advantage around 100 steps and
continues to improve consistently. This indicates
that the TreeRL achieves better prompt efficiency
by delivering enhanced performance with the same
number of training prompts. Overall, these results
underscore the promise of integrating tree search
and process supervision into RL training. It is
observed that both RL methods show only minor
improvements over the SFT baseline. This could
be due to the fact that we selected the RL training
data based on Qwen-2.5-14B, which is likely much
easier for the R1-Distilled-Qwen-2.5-7B model,
thereby limiting the potential performance gains in
RL.
4.4
Ablation Study on EPTree Sampling
Effects of entropy-based forking. Table 2 illus-
trates the performance across different strategies
when forking new branches in tree expansion. EP-
Tree shows better PassRate than random forking
with fewer generation tokens, which demonstrates
the advantage of EPTree. In addition, both tree
sampling strategies outperform multi-chain sam-
pling, offering the potential of tree search.
Case study on forking tokens. To help better

--- Page 8 ---

Table 2: Ablation of EPTree on Omni-MATH-500. We
compare forking branches using random and entropy-
based strategies on Qwen-2.5-14B-SFT. (16, 0, 0, 0) cor-
responds to multi-chain sampling. Entropy denotes
whether to use entropy-based forking strategy.
EP-
Tree model shows better PassRate performance yet with
fewer generation tokens.
(M, N, L, T)
Entropy
PassRate ↑
#Token ↓
(6, 2, 1, 2)
✓
56.9
22268
(6, 2, 1, 2)
✗
54.8
24213
(16, 0, 0, 0)
-
52.4
19858
(8, 4, 2, 2)
✓
71.0
77768
(8, 4, 2, 2)
✗
70.0
89452
(64, 0, 0, 0)
-
67.4
79367
 \(
 a
Since
We
 the
Wait
 using
But
The
Let
0.000
0.005
0.010
0.015
0.020
0.025
0.030
0.035
0.040
Proportion
Frequent words selected by EPTree
Figure 7: Frequent words of sampled forking tokens in
EPTree sampling on Omni-MATH-500.
understand EPTree, we conduct case studies to an-
alyze what type of tokens tend to be selected. We
examine frequency by identifying the top-10 tokens
that most often serve as forking points, and the re-
sults are illustrated in Figure 7. It can be observed
that mathematical operators (\(), logical conjunc-
tions, and transitional terms (“Since”, “But”) are
frequently selected. Notably, the token “wait” ap-
pears frequently, as o1-like models often use it for
self-reflection steps.
4.5
Ablation on TreeRL
To test the effectiveness of process supervision in
TreeRL, we compare different designs of process
supervision signals. Additionally, since the TreeRL
uses more traces than RL with multi-chain sam-
pling, we also evaluate how the increased training
cost impacts performance. The results are pre-
sented in Table 3. The results demonstrate that
RL with reweighted local and global advantage
achieves the best performance. Removing either
component could lead to a decline in performance.
Moreover, using a subset of sampled responses
shows less improvement compared to utilizing the
entire set. This suggests that, in addition to higher
PassRate and process supervision, tree search en-
hances RL performance by enabling more training
within the same inference cost.
5
Related Work
5.1
RL for LLM Reasoning
Recent advanced (Guo et al., 2025; Zhu et al., 2024;
OpenAI, 2024; Ouyang et al., 2022) have demon-
strated the effectiveness of reinforcement learning
in LLM alignment and reasoning. Most existing
methods train a reward model or use rule-based
rewards for the entire response. In parallel, process
supervision(Lightman et al., 2023) has shown a
particularly promising performance than outcome
supervision. Most existing works resort to training
a process reward model (PRM) based on human-
or auto-annotated process signals(Lightman et al.,
2023; Wang et al., 2024a; Luo et al., 2024; Setlur
et al., 2024) and apply the static PRM for RL train-
ing (Shao et al., 2024a; Wang et al., 2024a). How-
ever, a static PRM could suffer from distribution
shift and reward hacking as RL training progresses.
(Kazemnejad et al., 2024) overcomes this problem
by conducting Monte Carlo rollouts to estimate the
value for each step, but it suffers from high com-
putation cost with around quadratic computational
complexity and thus hinders scalability.
5.2
Tree Search for LLM Reasoning
Tree search has mainly been explored in LLM align-
ment and inference, especially for data synthesis
and offline preference training. Xie et al. (2024)
employs MCTS to generate step-level preference
pairs for DPO (Rafailov et al., 2024). Chen et al.
(2024b); Feng et al. (2024); Zhang et al. (2024b)
employ MCTS to iteratively generate high-quality
SFT data or produce process supervision signals
for training. Other works explore reward-guided
search (Snell et al., 2024; Yao et al., 2023; Long,
2023) to boost the performance in the inference
stage. However, few efforts have been devoted to
studying how to explicitly integrate tree search into
reinforcement learning training like AlphaZero (Sil-
ver et al., 2017) to improve LLM reasoning.

--- Page 9 ---

Table 3: Ablation on the effectiveness of different process signals for RL training using Qwen2.5-14B. GA and LA
denote the global and local advantages, respectively. n refers to the number of leaf nodes that can be reached from
the given step. #Response denotes the number of responses used for training.
Reward
#Responses
MATH500
Omni-MA
TH-500
AIME2024
AMC
Olympiad
Bench
LiveCode
Bench
Avg Gain
(GA + LA)/√n
30
81.7
36.7
28.0
55.9
44.6
20.8
-
GA + LA
30
81.5
32.0
24.1
56.2
42.1
19.7
-1.9 ↓
GA/√n
30
80.1
35.1
24.7
55.5
42.8
20.7
-1.3 ↓
(GA + LA)/√n
16
80.1
32.5
24.5
52.9
41.7
15.8
-3.2 ↓
6
Conclusion
This work presents TreeRL, an RL approach that
combines tree search with process supervision to
enhance LLM reasoning.
EPTree improves re-
sponse diversity and performance over traditional
methods like MCTS and i.i.d multi-chain sampling.
Then, we conduct reinforcement learning with EP-
Tree and the derived process supervision from tree
search. Experiments on math reasoning tasks show
that the TreeRL outperforms existing techniques,
highlighting the potential of RL with tree search to
advance LLM in complex reasoning tasks.
7
Limitation
In this work, we propose to improve reinforcement
learning with on-policy tree search. While this
approach demonstrates promising performance, it
does come with several limitations. First, current
LLM inference engines do not offer special opti-
mizations for tree search, meaning the proposed
EPTree still requires 2+ iterations, resulting in a
performance that is approximately 2× slower than
multi-chain sampling. Additionally, we utilize pro-
cess supervision from tree search for RL training
and attempt to optimize it from the perspective of
advantage and re-weighting. Further efforts, in-
cluding how to assign appropriate weights to the
importance of different steps, how to define more
meaningful process signals from the tree structure,
and how to implement step-level reward normaliza-
tion, deserve more exploration.
Acknowledgment. This work has been in part
supported by the Natural Science Foundation
of China (NSFC) 62495063, Tsinghua Univer-
sity (Department of Computer Science and Tech-
nology) - Siemens Ltd., China Joint Research
Center for Industrial Intelligence and Internet of
Things (JCIIOT), and the New Cornerstone Sci-
ence Foundation through the XPLORER PRIZE.
The corresponding author: Yuxiao Dong (yuxi-
aod@tsinghua.edu.cn).
References
Josh Achiam, Steven Adler, Sandhini Agarwal, Lama
Ahmad, Ilge Akkaya, Florencia Leoni Aleman,
Diogo Almeida, Janko Altenschmidt, Sam Altman,
Shyamal Anadkat, et al. 2023. Gpt-4 technical report.
arXiv preprint arXiv:2303.08774.
Arash Ahmadian, Chris Cremer, Matthias Gallé,
Marzieh Fadaee, Julia Kreutzer, Ahmet Üstün, and
Sara Hooker. 2024. Back to basics: Revisiting re-
inforce style optimization for learning from human
feedback in llms. In ACL.
Cameron B Browne, Edward Powley, Daniel White-
house, Simon M Lucas, Peter I Cowling, Philipp
Rohlfshagen, Stephen Tavener, Diego Perez, Spyri-
don Samothrakis, and Simon Colton. 2012. A survey
of monte carlo tree search methods. IEEE Transac-
tions on Computational Intelligence and AI in games,
4(1):1–43.
Guoxin Chen, Minpeng Liao, Chengxi Li, and Kai Fan.
2024a. Alphamath almost zero: process supervision
without process. arXiv preprint arXiv:2405.03553.
Guoxin Chen, Minpeng Liao, Chengxi Li, and Kai Fan.
2024b. Alphamath almost zero: Process supervision
without process. Preprint, arXiv:2405.03553.
Wesley Chung, Valentin Thomas, Marlos C Machado,
and Nicolas Le Roux. 2021. Beyond variance reduc-
tion: Understanding the true impact of baselines on
policy optimization. In International Conference on
Machine Learning, pages 1999–2009. PMLR.
Abhimanyu Dubey, Abhinav Jauhri, Abhinav Pandey,
Abhishek Kadian, Ahmad Al-Dahle, Aiesha Letman,
Akhil Mathur, Alan Schelten, Amy Yang, Angela
Fan, et al. 2024. The llama 3 herd of models. arXiv
preprint arXiv:2407.21783.
Xidong Feng, Ziyu Wan, Muning Wen, Stephen Marcus
McAleer, Ying Wen, Weinan Zhang, and Jun Wang.
2024. Alphazero-like tree-search can guide large
language model decoding and training.
Preprint,
arXiv:2309.17179.

--- Page 10 ---

Bofei Gao, Feifan Song, Zhe Yang, Zefan Cai, Yibo
Miao, Qingxiu Dong, Lei Li, Chenghao Ma, Liang
Chen, Runxin Xu, et al. 2024. Omni-math: A univer-
sal olympiad level mathematic benchmark for large
language models. arXiv preprint arXiv:2410.07985.
Team GLM, Aohan Zeng, Bin Xu, Bowen Wang, Chen-
hui Zhang, Da Yin, Diego Rojas, Guanyu Feng, Han-
lin Zhao, Hanyu Lai, et al. 2024. Chatglm: A family
of large language models from glm-130b to glm-4 all
tools. arXiv preprint arXiv:2406.12793.
Daya Guo, Dejian Yang, Haowei Zhang, Junxiao Song,
Ruoyu Zhang, Runxin Xu, Qihao Zhu, Shirong Ma,
Peiyi Wang, Xiao Bi, et al. 2025. Deepseek-r1: In-
centivizing reasoning capability in llms via reinforce-
ment learning. arXiv preprint arXiv:2501.12948.
Chaoqun He, Renjie Luo, Yuzhuo Bai, Shengding Hu,
Zhen Leng Thai, Junhao Shen, Jinyi Hu, Xu Han,
Yujie Huang, Yuxiang Zhang, et al. 2024. Olympiad-
bench: A challenging benchmark for promoting agi
with olympiad-level bilingual multimodal scientific
problems. arXiv preprint arXiv:2402.14008.
Dan Hendrycks, Collin Burns, Steven Basart, Andy Zou,
Mantas Mazeika, Dawn Song, and Jacob Steinhardt.
2020. Measuring massive multitask language under-
standing. arXiv preprint arXiv:2009.03300.
Dan Hendrycks, Collin Burns, Saurav Kadavath, Akul
Arora, Steven Basart, Eric Tang, Dawn Song, and
Jacob Steinhardt. 2021. Measuring mathematical
problem solving with the math dataset. NeurIPS.
Zhenyu Hou, Xin Lv, Rui Lu, Jiajie Zhang, Yujiang
Li, Zijun Yao, Juanzi Li, Jie Tang, and Yuxiao Dong.
2025. Advancing language model reasoning through
reinforcement learning and inference scaling. arXiv
preprint arXiv:2501.11651.
Naman Jain, King Han, Alex Gu, Wen-Ding Li, Fanjia
Yan, Tianjun Zhang, Sida Wang, Armando Solar-
Lezama, Koushik Sen, and Ion Stoica. 2024. Live-
codebench: Holistic and contamination free eval-
uation of large language models for code. arXiv
preprint arXiv:2403.07974.
Amirhossein Kazemnejad, Milad Aghajohari, Eva
Portelance, Alessandro Sordoni, Siva Reddy, Aaron
Courville, and Nicolas Le Roux. 2024. Vineppo: Un-
locking rl potential for llm reasoning through refined
credit assignment. Preprint, arXiv:2410.01679.
Woosuk Kwon, Zhuohan Li, Siyuan Zhuang, Ying
Sheng, Lianmin Zheng, Cody Hao Yu, Joseph E.
Gonzalez, Hao Zhang, and Ion Stoica. 2023. Effi-
cient memory management for large language model
serving with pagedattention. In Proceedings of the
ACM SIGOPS 29th Symposium on Operating Systems
Principles.
Jia Li, Edward Beeching, Lewis Tunstall, Ben Lip-
kin, Roman Soletskyi, Shengyi Huang, Kashif Rasul,
Longhui Yu, Albert Q Jiang, Ziju Shen, et al. 2024a.
Numinamath: The largest public dataset in ai4maths
with 860k pairs of competition math problems and
solutions. Hugging Face repository, 13:9.
Tianle Li, Wei-Lin Chiang, Evan Frick, Lisa Dunlap,
Tianhao Wu, Banghua Zhu, Joseph E Gonzalez, and
Ion Stoica. 2024b. From crowdsourced data to high-
quality benchmarks: Arena-hard and benchbuilder
pipeline. arXiv preprint arXiv:2406.11939.
Hunter Lightman, Vineet Kosaraju, Yura Burda, Harri
Edwards, Bowen Baker, Teddy Lee, Jan Leike,
John Schulman, Ilya Sutskever, and Karl Cobbe.
2023.
Let’s verify step by step.
Preprint,
arXiv:2305.20050.
Hunter Lightman, Vineet Kosaraju, Yuri Burda, Harri-
son Edwards, Bowen Baker, Teddy Lee, Jan Leike,
John Schulman, Ilya Sutskever, and Karl Cobbe.
Let’s verify step by step. In The Twelfth Interna-
tional Conference on Learning Representations.
Jieyi Long. 2023. Large language model guided tree-of-
thought. Preprint, arXiv:2305.08291.
Anton Lozhkov, Raymond Li, Loubna Ben Allal, Fed-
erico Cassano, Joel Lamy-Poirier, Nouamane Tazi,
Ao Tang, Dmytro Pykhtar, Jiawei Liu, Yuxiang Wei,
et al. 2024. Starcoder 2 and the stack v2: The next
generation. arXiv preprint arXiv:2402.19173.
Liangchen Luo, Yinxiao Liu, Rosanne Liu, Samrat
Phatale, Meiqi Guo, Harsh Lara, Yunxuan Li, Lei
Shu, Yun Zhu, Lei Meng, Jiao Sun, and Abhinav
Rastogi. 2024. Improve mathematical reasoning in
language models by automated process supervision.
Preprint, arXiv:2406.06592.
Jincheng Mei, Wesley Chung, Valentin Thomas, Bo Dai,
Csaba Szepesvari, and Dale Schuurmans. 2022. The
role of baselines in policy gradient optimization. Ad-
vances in Neural Information Processing Systems,
35:17818–17830.
OpenAI.
2024.
Learning
to
reason
with
llms.
https://openai.com/index/
learning-to-reason-with-llms.
Long Ouyang, Jeff Wu, Xu Jiang, Diogo Almeida, Car-
roll L Wainwright, Pamela Mishkin, Chong Zhang,
Sandhini Agarwal, Katarina Slama, Alex Ray, et al.
2022. Training language models to follow instruc-
tions with human feedback. In Proceedings of the
36th International Conference on Neural Information
Processing Systems, pages 27730–27744.
Qwen. 2024. Qwen2.5: A party of foundation models.
Rafael Rafailov, Archit Sharma, Eric Mitchell, Christo-
pher D Manning, Stefano Ermon, and Chelsea Finn.
2023.
Direct preference optimization: Your lan-
guage model is secretly a reward model. Advances in
Neural Information Processing Systems, 36:53728–
53741.

--- Page 11 ---

Rafael Rafailov, Archit Sharma, Eric Mitchell, Christo-
pher D Manning, Stefano Ermon, and Chelsea Finn.
2024. Direct preference optimization: Your language
model is secretly a reward model. Advances in Neu-
ral Information Processing Systems.
John Schulman, Philipp Moritz, Sergey Levine, Michael
Jordan, and Pieter Abbeel. 2015. High-dimensional
continuous control using generalized advantage esti-
mation. arXiv preprint arXiv:1506.02438.
Amrith Setlur, Chirag Nagpal, Adam Fisch, Xinyang
Geng, Jacob Eisenstein, Rishabh Agarwal, Alekh
Agarwal, Jonathan Berant, and Aviral Kumar. 2024.
Rewarding progress: Scaling automated process veri-
fiers for llm reasoning. Preprint, arXiv:2410.08146.
Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu,
Junxiao Song, Xiao Bi, Haowei Zhang, Mingchuan
Zhang, Y. K. Li, Y. Wu, and Daya Guo. 2024a.
Deepseekmath: Pushing the limits of mathemati-
cal reasoning in open language models. Preprint,
arXiv:2402.03300.
Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu,
Junxiao Song, Mingchuan Zhang, YK Li, Yu Wu,
and Daya Guo. 2024b. Deepseekmath: Pushing the
limits of mathematical reasoning in open language
models. arXiv preprint arXiv:2402.03300.
David Silver, Thomas Hubert, Julian Schrittwieser, Ioan-
nis Antonoglou, Matthew Lai, Arthur Guez, Marc
Lanctot, Laurent Sifre, Dharshan Kumaran, Thore
Graepel, et al. 2017. Mastering chess and shogi by
self-play with a general reinforcement learning algo-
rithm. arXiv preprint arXiv:1712.01815.
Joar Skalse, Nikolaus Howe, Dmitrii Krasheninnikov,
and David Krueger. 2022. Defining and characteriz-
ing reward hacking. Advances in Neural Information
Processing Systems, 35:9460–9471.
Charlie Snell, Jaehoon Lee, Kelvin Xu, and Aviral Ku-
mar. 2024. Scaling llm test-time compute optimally
can be more effective than scaling model parameters.
Preprint, arXiv:2408.03314.
Gemini Team, Rohan Anil, Sebastian Borgeaud, Jean-
Baptiste Alayrac, Jiahui Yu, Radu Soricut, Johan
Schalkwyk, Andrew M Dai, Anja Hauth, Katie
Millican, et al. 2023.
Gemini:
a family of
highly capable multimodal models. arXiv preprint
arXiv:2312.11805.
Hugo Touvron, Louis Martin, Kevin Stone, Peter Al-
bert, Amjad Almahairi, Yasmine Babaei, Nikolay
Bashlykov, Soumya Batra, Prajjwal Bhargava, Shruti
Bhosale, et al. 2023.
Llama 2:
Open founda-
tion and fine-tuned chat models.
arXiv preprint
arXiv:2307.09288.
Peiyi Wang, Lei Li, Zhihong Shao, R. X. Xu, Damai
Dai, Yifei Li, Deli Chen, Y. Wu, and Zhifang Sui.
2024a. Math-shepherd: Verify and reinforce llms
step-by-step without human annotations. Preprint,
arXiv:2312.08935.
Peiyi Wang, Lei Li, Zhihong Shao, Runxin Xu, Damai
Dai, Yifei Li, Deli Chen, Yu Wu, and Zhifang Sui.
2024b. Math-shepherd: Verify and reinforce llms
step-by-step without human annotations. In Proceed-
ings of the 62nd Annual Meeting of the Association
for Computational Linguistics (Volume 1: Long Pa-
pers), pages 9426–9439.
Yubo Wang, Xueguang Ma, Ge Zhang, Yuansheng Ni,
Abhranil Chandra, Shiguang Guo, Weiming Ren,
Aaran Arulraj, Xuan He, Ziyan Jiang, et al. 2024c.
Mmlu-pro: A more robust and challenging multi-task
language understanding benchmark. arXiv preprint
arXiv:2406.01574.
Yuxi Xie, Anirudh Goyal, Wenyue Zheng, Min-Yen
Kan, Timothy P Lillicrap, Kenji Kawaguchi, and
Michael Shieh. 2024. Monte carlo tree search boosts
reasoning via iterative preference learning. arXiv
preprint arXiv:2405.00451.
Shunyu Yao, Dian Yu, Jeffrey Zhao, Izhak Shafran,
Thomas L. Griffiths,
Yuan Cao,
and Karthik
Narasimhan. 2023.
Tree of thoughts:
Deliber-
ate problem solving with large language models.
Preprint, arXiv:2305.10601.
Dan Zhang, Sining Zhoubian, Ziniu Hu, Yisong Yue,
Yuxiao Dong, and Jie Tang. 2024a. Rest-mcts*: Llm
self-training via process reward guided tree search.
arXiv preprint arXiv:2406.03816.
Dan Zhang, Sining Zhoubian, Ziniu Hu, Yisong Yue,
Yuxiao Dong, and Jie Tang. 2024b. Rest-mcts*: Llm
self-training via process reward guided tree search.
Preprint, arXiv:2406.03816.
Jeffrey Zhou, Tianjian Lu, Swaroop Mishra, Sid-
dhartha Brahma, Sujoy Basu, Yi Luan, Denny Zhou,
and Le Hou. 2023.
Instruction-following evalu-
ation for large language models.
arXiv preprint
arXiv:2311.07911.
Shuyan Zhou, Frank F Xu, Hao Zhu, Xuhui Zhou,
Robert Lo, Abishek Sridhar, Xianyi Cheng, Tianyue
Ou, Yonatan Bisk, Daniel Fried, et al. 2024. We-
barena: A realistic web environment for building
autonomous agents. In The Twelfth International
Conference on Learning Representations.
Qihao Zhu, Daya Guo, Zhihong Shao, Dejian Yang,
Peiyi Wang, Runxin Xu, Y Wu, Yukun Li, Huazuo
Gao, Shirong Ma, et al. 2024. Deepseek-coder-v2:
Breaking the barrier of closed-source models in code
intelligence. arXiv preprint arXiv:2406.11931.

--- Page 12 ---

A
Position Distribution Analysis
We study the position of selected forking tokens
in their branches. As illustrated in Figure 8, we
plot the relative positions of forking points, calcu-
lated as the ratio between a token’s forking position
and its branch length. The resulting distribution
shows a roughly uniform pattern, which supports
our assumptions presented in Appendix B.
0.0
0.2
0.4
0.6
0.8
1.0
Relative Position
0.0
0.2
0.4
0.6
0.8
1.0
1.2
1.4
1.6
Density
Forking Token Position Distribution by EPTree
Uniform Distribution
Figure 8: Distribution of the relative positions of forking
tokens selected by EPTree on Omni-MATH-500, based
on the ratio of forking position to branch length.
B
Theoritical Analysis of EPTree
Theorem 1. Consider a setting where forking to-
kens follow a uniform distribution U(0, 1) within
each branch, and generation lengths remain fixed
without repetition, subject to the constraint that
parameter l ≤2. Under these conditions, the
entropy-guided tree search algorithm presented in
Section 3.1 yields a leaf count that is bounded be-
tween 4
3 and 12
5 times that of a multi-sampling ap-
proach, while maintaining identical computational
complexity in terms of total token evaluations.
Proof. We present the proof of Theorem 1 by an-
alyzing two cases based on the branching process
illustrated in Figure 9. Let x1, x2, . . . , xn be i.i.d.
random variables uniformly distributed on [0, 1].
Case l = 1: Assume all completion lengths are
unit 1. The total completion length of the entropy-
tree is:
L = 1 + t ·
n
X
i=1
(1 −xi).
The expected total length is:
E[L] = 1 + t ·
n
X
i=1
E[1 −xi] = 1 + nt
2 .
The number of leaves in the tree is:
Ntree = 1 + nt.
x1
x2
x3
Figure 9: Forking token illustration when n = 3, t = 2,
where x1, x2, x3
i.i.d
∼U(0, 1).
For the multi-sample approach with the same com-
pletion tokens, the number of leaves is:
Nmulti = 1 + nt
2 .
The ratio of the number of leaves in the tree to the
multi-sample approach is:
R(n, t) = 1 + nt
1 + nt
2
.
Let x = nt ≥1. Then:
R(x) = 1 + x
1 + x
2
.
The derivative of R(x) with respect to x is:
R′(x) =
1

1 + x
2
2 > 0,
indicating that R(x) is monotonically increasing.
Evaluating at the endpoints:
R(1) = 4
3,
lim
x→∞R(x) = 2.
Thus, R(n, t) ∈
4
3, 2

when l = 1.
Case l = 2: In this scenario, the next top-n
entropy token appears either on the main chain or
on one of the branches. The probabilities of these
events are:
1
1 + t P
i (1 −xi)
and
1 −xi
1 + t P
i (1 −xi),

--- Page 13 ---

Respectively. The expected new completion length
is:
E [li] = E


1
2 + t
2
P
i (1 −xi)2
1 + t P
i (1 −xi)

:= φ.
Through Monte Carlo simulation, it is observed that
φ monotonically decreases with n. As n →∞, the
ratio tends to 1
3. For n = 1, the integral value is
ln 2 −1
4. Thus, φ ∈
1
3, ln 2 −1
4

.
The total generation length is:
1 + 1
2nt + nt · φ,
And the number of leaves is:
1 + 2nt.
For the same completion length, the number of
leaves in the multi-sample approach is:
1 +
1
2 + φ

nt.
The ratio of the number of leaves in the tree to the
multi-sample approach is:
R(nt) =
1 + 2nt
1 +
1
2 + φ

nt
,
Which is also monotonically increasing in nt.
Therefore:
R(nt) ∈

6
3 + 2φ,
4
1 + 2φ

.
Specifically:













R(nt) ≥
6
3 + 2 ·

ln 2 −1
4
 ≈1.544
R(nt) <
4
1 + 2 · 1
3
= 2.4
Combining both cases, the ratio R(n, t) lies in the
interval
4
3, 12
5

.
Table 4: (M, N, L, T) Parameter Evaluation of EPTree
on Omni-MATH-500. The table reports the leaf number,
PassRate, and total generation tokens under different
parameter combinations for k = 16 and k = 64.
(M, N, L, T)
#Leaf ↑
PassRate ↑
#Token ↓
k = 16
multi-16
16
52.4
19858
(8, 3, 1, 1)
32
58.4
25223
(7, 2, 1, 2)
35
59.2
26200
(6, 2, 2, 1)
30
54.4
20537
(6, 2, 1, 2)
30
56.9
22268
(5, 3, 1, 2)
35
58.6
25269
(5, 2, 1, 3)
35
56.0
25210
(5, 3, 2, 1)
35
58.0
22668
(5, 1, 2, 3)
35
58.6
21895
k = 64
multi-64
64
67.4
79367
(16, 2, 2, 2)
144
70.0
88257
(16, 4, 1, 2)
144
71.4
101744
(16, 2, 1, 4)
144
72.6
100468
(9, 5, 1, 3)
144
71.9
98193
(9, 3, 1, 5)
144
71.6
97193
(8, 8, 1, 2)
136
70.7
92946
(8, 4, 1, 4)
136
69.7
90015
(8, 8, 2, 1)
136
68.6
79582
(8, 4, 2, 2)
136
71.0
77768
(8, 2, 2, 4)
136
69.4
76750
C
Detailed Evaluation of EPTree
Table 4 presents a comprehensive evaluation of EP-
Tree in comparison to the multi-chain baseline for
k = 16. We select the RL training configuration
(6, 2, 1, 2), as it offers a similar inference cost to
the chain-16 setting while demonstrating improved
efficiency (requiring only one interaction) and ef-
fectiveness (achieving 56.9 compared to 52.4).
D
Results on Other Reasoning
Benchmarks
Figure 10 and 11 provide additional RL training
results on MATH500, AMC, LiveCodeBench, and
AIME2024, demonstrating that TreeRL with EP-
Tree sampling outperforms RL with traditional
multi-chain sampling across various benchmarks.
E
TreeRL on General tasks
To further evaluate TreeRL’s generalizability, we
further conducted experiments on general tasks.
We evaluate TreeRL and ChainRL on 3 general

--- Page 14 ---

0
100
200
300
Training steps
74
76
78
80
82
Accuracy(%)
MATH500
ChainRL
TreeRL
0
100
200
300
Training steps
45
50
55
Accuracy(%)
AMC
ChainRL
TreeRL
0
100
200
300
Training steps
12
14
16
18
20
22
Accuracy(%)
LiveCodeBench
ChainRL
TreeRL
0
100
200
300
Training steps
10
15
20
25
30
Accuracy(%)
AIME-2024
ChainRL
TreeRL
Figure 10: Performance comparison between TreeRL and ChainRL on MATH500 (Upper Left), AMC (Upper
Right), LiveCodeBench (Lower Left), and AIME2024 (Lower Right); experiments are based on Qwen-2.5-14B.
0
100
200
300
Training steps
55.0
57.5
60.0
62.5
65.0
Accuracy(%)
MATH500
ChainRL
TreeRL
0
100
200
300
Training steps
25
30
35
Accuracy(%)
AMC
ChainRL
TreeRL
0
100
200
300
Training steps
13
14
15
16
17
Accuracy(%)
LiveCodeBench
ChainRL
TreeRL
0
100
200
300
Training steps
2.5
5.0
7.5
10.0
12.5
Accuracy(%)
AIME-2024
ChainRL
TreeRL
Figure 11: Performance comparison between TreeRL and ChainRL on MATH500 (Upper Left), AMC (Upper
Right), LiveCodeBench (Lower Left), and AIME2024 (Lower Right); experiments are based on GLM4-9B.

--- Page 15 ---

tasks: MMLU-Pro (Wang et al., 2024c), Arena-
Hard (Li et al., 2024b), and IFEval (Zhou et al.,
2023).
• MMLU-Pro extends MMLU (Hendrycks
et al., 2020) with more challenging reason-
ing tasks, fewer noisy questions, and a larger
answer set (4-10 options). We use the chain-
of-thought prompt and measure the pass rate.
• Arena-Hard consists of 500 difficult prompts
from Chatbot Arena, focusing on human-like
preferences. We evaluate using the win rate
score, comparing against the GPT-4-0314
baseline.
• IFEval tests the model’s ability to follow
prompt instructions. We use the strict prompt
metric for evaluation.
MMLU-Pro
Arena-hard
IFEval
Avg
SFT
57.6
57.5
49.9
55.0
ChainRL
64.5
72.2
56.0
64.2
TreeRL
64.5
71.8
58.2
64.9
Table 5: Performance on general benchmarks.
As is shown in Table 5, we observe a compa-
rable performance between TreeRL and ChainRL.
This indicates that while TreeRL exhibits a par-
ticular advantage in reasoning tasks, it maintains
its performance in general tasks, achieving robust
performance in diverse task types.

```
