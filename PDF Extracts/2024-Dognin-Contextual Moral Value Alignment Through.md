---
title: "Contextual Moral Value Alignment Through - PDF Extract"
source_pdf: "2024-Dognin-Contextual Moral Value Alignment Through.pdf"
pages: 6
extracted_at: "2026-01-24T17:05:28.467697"
---

# PDF Extract: Contextual Moral Value Alignment Through

**Source PDF:** 2024-Dognin-Contextual Moral Value Alignment Through.pdf
**Total Pages:** 6

---

## Content

```
--- Page 1 ---

Contextual Moral Value Alignment Through Context-Based Aggregation
Pierre Dognin, Jesus Rios, Ronny Luss, Inkit Padhi, Matthew D Riemer, Miao Liu,
Prasanna Sattigeri, Manish Nagireddy, Kush R. Varshney, Djallel Bouneffouf
IBM Thomas J. Watson Research Center
Abstract
Developing value-aligned AI agents is a com-
plex undertaking and an ongoing challenge in
the field of AI. Specifically within the domain
of Large Language Models (LLMs), the ca-
pability to consolidate multiple independently
trained dialogue agents, each aligned with a dis-
tinct moral value, into a unified system that can
adapt to and be aligned with multiple moral val-
ues is of paramount importance. In this paper,
we propose a system that does contextual moral
value alignment based on contextual aggrega-
tion. Here, aggregation is defined as the pro-
cess of integrating a subset of LLM responses
that are best suited to respond to a user input,
taking into account features extracted from the
user’s input. The proposed system shows better
results in term of alignment to human value
compared to the state of the art.
1
Introduction
In an increasingly interconnected world, the align-
ment of values and intentions among individuals
and groups has never been more critical (Sun et al.,
2024; Rodriguez-Soto et al., 2024). Value align-
ment refers to the process of ensuring that the goals
and behaviors of artificial intelligence (AI) systems
are consistent with human values, preferences, and
ethical principles (Ji et al., 2023; Hendrycks et al.,
2020). Achieving value alignment is crucial to
mitigate potential risks. This involves designing
AI systems that prioritize human values such as
fairness, safety and transparency (Gabriel, 2020;
Brown et al., 2021).
This paper addresses a problem that we
term Contextual Moral-Value Alignment (CMVA)
which extends the concept of value alignment by
acknowledging the context-dependent nature of eth-
ical considerations in AI systems. CMVA recog-
nizes that ethical principles and values may vary
across different contexts and cultures; such value
are often ambiguous.
CMVA allows AI systems to resolve this am-
biguity by adapting to the context and offering
responses that respect diverse moral viewpoints.
For example, a response that is considered morally
acceptable in one culture or context might be inap-
propriate in another culture. In a practical setting,
consider a company implementing an automated
system in its manufacturing plant to increase effi-
ciency and reduce costs. Decisions made by the sys-
tem must deal with such value alignment ambiguity
because decisions must balance potentially conflict-
ing values: Efficiency versus Employee Well-being.
Implementing automation could lead to increased
efficiency and cost savings which aligns with the
company’s goal of maximizing profits. On the other
hand, implementing automation could lead to fewer
opportunities or employee layoffs, which conflicts
with the company’s value of supporting employees
and ensuring their well-being.
A comprehensive understanding of the context
is necessary to provide a better decision regarding
whether the company should proceed with imple-
menting automation. Similar context-dependent
decisions also apply to chatbots; for example, sales
agents must balance the "customer is always right"
mantra versus the goal of profiting from the cus-
tomer. The focus of this paper is on such deci-
sions made by Large Language Models (LLMs).
To get this type of capability, we propose a Con-
textual Moral Value Alignment Generative System
(CMVA-GS) that explores how one may harness
the power of text aggregation from multiple agents
to achieve Contextual Value Alignment.
CMVA-GS is an approach where models, called
Moral Value Agents, are trained independently to
address different contexts. These agents contribute
answers individually, and corresponding responses,
along with a user’s morality profile, are aggregated
using an aggregator module. This aggregator con-
textualizes the answers obtained, providing a com-
prehensive synthesis of moral perspectives.
arXiv:2403.12805v1  [cs.AI]  19 Mar 2024

--- Page 2 ---

2
Related work
Dai et al. (2024) discuss the challenges in balanc-
ing performance with the safety of LLMs. Safe
Reinforcement Learning from Human Feedback
(Safe RLHF) is introduced as a novel algorithm de-
signed to address the tension between helpfulness
and harmlessness during LLM training, where the
safety concern for LLMs is formalized as a con-
strained optimization task. Zeng et al. (2023) pro-
vide a quantitative analysis to verify the existence
of diversified preferences in commonly used hu-
man feedback datasets. To mitigate the alignment
ineffectiveness caused by diversified preferences,
a novel Multi-Objective Reward learning method
is proposed. The method automatically adjusts the
learning gradients across different preference data
sources. Jang et al. (2023) study the Reinforce-
ment Learning from Personalized Human Feed-
back (RLPHF) problem, where LLMs are aligned
to multiple preferences by modeling alignment as a
Multi-Objective Reinforcement Learning (MORL)
problem. Compared to single-objective baselines,
they achieve personalized alignment by decompos-
ing preferences into multiple dimensions. To the
best of our knowledge, none of the above works
consider the problem of contextual value alignment
that we formalize below.
3
Problem Setting
This section formalizes the MVA problem and our
extension to the CMVA problem.
Moral-Value Alignment: We model the Moral-
Value Alignment as a MORL problem which in-
volves finding a policy that optimally balances mul-
tiple objectives simultaneously, aligning the agent’s
actions with a set of desired values. Let S denote
the state space of a LLM, which includes the cur-
rent conversation history, the prompt given to the
model, and the current sentence being generated.
Let A denote the action space representing the
choices available to the LLM at each step. Actions
include selecting which word or token to generate
next in the sequence as well as selecting special
tokens (e.g., indicating the end of a sentence). Also
denote R ⊆RN as the set of possible rewards,
where N is the number of objectives.
The Moral-Value Alignment problem can be
modeled as a MORL (Liu et al., 2015), where
the reward vector r = ⟨r1, . . . , rN⟩∈R is a
Moral-Value vector of rewards functions with each
ri : S × A →R representing the reward for a
response (i.e., the action) to a given prompt (i.e.,
the state) for the ith moral value. Given a policy
π : S →P(A), where P(A) is the set of distri-
butions over actions, the objective in Moral-Value
Alignment as a MORL is to find a policy that max-
imizes a weighted combination of the reward func-
tions, where a desired weights w is known before
the optimization. Formally, we seek a policy π∗
that maximizes the expected return Jw(π), where
the vector of rewards r = ⟨r1, . . . , rN⟩is projected
as rT w.
Contextual Moral-Value Alignment (CMVA): In
practice, every user has a different desired weight
vector. We refer to it as a Moral Profile Vector
defined as c = [c1, . . . , cn] where ci represents
the degree to which the individual adheres to the
ith moral value. In CMVA, the objective to be
optimized in the MVA problem above is modified
to Jc(π) where now the reward to be optimized is
given by rT c. Thus, the optimal policy π∗(c) =
arg maxπ Jc(π) depends on the moral profile.
4
Contextual MVA Generative System
Figure 1 presents the proposed system architecture.
The user request and profile are given as input to
the system, through which the request is answered
by multiple moral agents. Each agents answers
the question according to its moral value. The
individualized answers and the user’s moral profile
are then used by the Contextual Aggregator (CA)
to aggregate the answers according to the moral
profile. The key components of CMVA-GS are:
Datasets of Moral Values:
Let D
=
{(u(l), z(l))}L
l=1 be a dataset consisting of L data
points, where: u(l) represents the features associ-
ated with a particular text, z(l) represents the cor-
responding moral value provided by an individual
for the l-th action within predefined categories rep-
resenting moral judgments, Z denotes the set of
possible moral value categories.
Reward Models: We assume n individual val-
ues or principles are given, and that we can learn
a reward model ri, for i = 1, . . . , n for each value.
A reward is a function that evaluates any LLM’s
output y, i.e., a sequence of tokens generated by
the LLM, given a context x, with a scalar score rep-
resenting how much y satisfies the corresponding
value or principle. We train one classifier for each
moral value (care, fairness, authority, and sanctity)
and use these classifiers as reward models to mea-
sure how much the output of an LLM aligns with

--- Page 3 ---

Figure 1: Contextual Moral-Value Alignment Genera-
tive System
our moral values. Each classifier provides a reward
between 0 and 1. A reward of 1 indicates that the
output follows the moral value, while a reward of 0
indicates that it does not follow the moral value.
Moral Agents: At inference, each Moral Agent
Ai takes a question x as input, and outputs an an-
swer ti ∼Ai|x, for i = 1, . . . , n. These answers
are then be aggegated according to some moral pro-
file. In order to train each Moral Agent, we use
the rewards defined above in Section 4 to evaluate
the behavior of an LLM which is specified by a
policy π. Specifically, we can measure the LLM’s
alignment to each moral value i by estimating the
expected reward Ji(π) by sampling prompts and
applying corresponding policies to get responses.
Optimizing a single-value objective Ji(π), i.e.,
π∗
i = argmin
π Ji(π),
(1)
can be done using policy-based Reinforcement
Learning (RL) methods such as PPO (Stiennon
et al., 2020; Ouyang et al., 2022; Schulman et al.,
2017) with ri as a reward signal.
Thus, given a pre-trained LLM to initialize PPO,
we can find a LLM π∗
i by solving Eq. (1) for each
value or principle i = 1, . . . , n, using RL fine-
tuning (RLFT). As a result, we will have n Moral
Agents, which are LLMs each denoted by Ai for
i = 1, . . . , n. To avoid reward hacking during
RLFT, a Kullback-Leibler (KL) regularization term
can be added to Eq. (1) that ensures the policy does
not drift too far from its initialization.
Contextual Aggregator: The CA is a function
M that takes as input, texts and the moral profile
feature vector, and produces the output text. The
model can be decomposed into an encoder-decoder
or decoder-only architecture without loss of gener-
ality. Let E represent the encoder function and D
represent the decoder function.
Each input text from the moral agents is
represented as a sequence of tokens:
ti
=
(ti,1, ti,2, . . . , ti,mi) where mi is the length of the
i-th input text. The moral profile feature vector
is denoted as c. The output text Y is generated
by applying the decoder function to the encoded
representation of the input texts and moral profile:
Y = D(E(t1, t2, . . . , tn, c)).
Let y = (y1, . . . , yℓ) be the ground truth out-
put text, where ℓis the length of the output text.
The loss function L measures the discrepancy be-
tween the generated output Y and the ground truth
y. We use the cross-entropy loss: L(y, Y ) =
−Pℓ
j=1
PV
k=1 yj,k log(Yj,k) where V is the size
of the vocabulary, yj,k is a one-hot encoding of the
j-th token in the ground truth output, and Yj,k is
the predicted probability of token k at position j in
the generated output.
The parameters of the model (i.e., encoder and
decoder) are learned by minimizing the loss func-
tion using gradient descent-based optimization al-
gorithms:
θ∗= arg min
θ
N
X
i=1
L(y(i), M(t(i)
1 , . . . , t(i)
n , c(i)))
where N is the number of training examples, θ
represents the parameters of the model, and y(i)
and (t(i)
1 , t(i)
2 , . . . , t(i)
n , c(i)) are the ground truth
output and input for the i-th training example, re-
spectively. For our experimental results, we used a
decoder-only architecture.
5
Performance Evaluation
We present results on the Moral Integrity Cor-
pus (MIC) (Ziems et al., 2022). MIC provides
moral annotations on prompt-reply pairs. It was
built up from the Social Chemistry (SocialChem)
dataset (Forbes et al., 2020) and shares 5 moral
foundations (or values) with it. These 5 values
are care-harm, fairness-cheating, loyalty-betrayal,
authority-subversion, and sanctity-degradation, de-
fined in Appendix A.4.2 of Forbes et al. (2020).
SocialChem annotates each action with a moral
judgment that can be binarized capturing negative
and neutral/positive judgments to build classifiers
(0 for negative and 1 otherwise). These value clas-
sifiers can then be used as reward models. Thus,
a reward is the probability of a LLM simulated
response being in the good class of a moral value
classifier.

--- Page 4 ---

5.1
Learned Moral Agents
We learn a Moral Agent for each of the 5 values
under consideration. As described in 3, we start by
choosing an initial pre-trained (PT) LLM: Open As-
sistant 12B in our case, see PT-model in 5.2. Then,
we applied RL to fine-tune 5 times this initial LLM,
each time using a different moral reward. We used
the PPO implementation from TRL (von Werra
et al., 2020), with a batch size of 256 episodes
(i.e., answers to training questions), 4 optimization
epochs per batch, and a learning rate of 2×10−9.
Table 1 shows the 5 learned Moral LLM Agents
(one per row). We evaluate their moral behaviour
w.r.t. their optimized value by computing the prob-
ability (expected reward) that the Moral Agent an-
swers to a dataset of 5K MIC questions not seen
during training follow the individual moral value
they are optimized to follow. For reference, we pro-
vide the probabilities that the PT-model (starting
policy in the RLFT of all Moral Agents) follows
each individual value. These probabilities are com-
puted using the reward models defined in 5.
Moral Value
PT model
Moral Agents
authority
91.58%
98.83%
fairness
85.20%
92.40%
sanctity
78.37%
93.05%
care
74.70%
96.74%
loyalty
74.38%
98.20%
Table 1: Probabilities that the Moral Agents answers
conform with each moral value.
CMVA-GS: CMVA-GS models are trained on
a dataset derived from MIC. Each input sample
is made of a question and moral profile vector
from MIC, a context of generated answers from
our 5 moral agents. Models are trained to match
the ground-truth answer using cross-entropy. The
dataset is composed of 91.0K/11.4K/11.4K sam-
ples for train/val/test. Our CMVA-GS models start
from an OpenAssistant 12B model. We train a Low
Rank Adapter (LoRA) (Hu et al., 2021) using su-
pervised fine-tuning. 8 A100-80GB GPUs are used
w/ a 5×10−7 learning rate, 128 adapter rank, and
32 per-device minibatch size (256 total). Training
runs for 21.6K steps, a 60 epoch "early stopping".
5.2
Benchmarks
CMVA-GS is compared against the following:
(1) PT-model: Our PT-model is the Open-Assistant
12B parameter (Köpf et al., 2023) is a decoder-only
model from the Pythia-deduped family (Biderman
Figure 2: Evaluation using ROUGE on MIC.
et al., 2023) fine-tuned with (i) Supervised Learn-
ing on QA/dialogue demonstrations as well as (ii)
RL on human preferences.
(2) Llama-13b/Llama-7b: We prompt the Llama-
2-13b-chat-hf and Llama-2-7b-chat-hf models,
both finetuned to perform dialogue. The prompt
defines the desired morals, includes 5 pairs (i.e.,
questions and answers) of examples per desired
moral taken from the MIC (test) data, and requests
a response that follows the defined moral values.
(3) Agg13Llama: We again prompt the Llama-2-
13b-chat-hf model but with a twist. The morals are
again defined but the examples are the results of
passing the user question through the correspond-
ing learned Moral Agents from Section 5.1. The
prompt asks the model to aggregate these answers
when responding to the question.
Evaluation Metrics:
We evaluate our mod-
els using ROUGE-1, ROUGE-2, ROUGE-L, and
ROUGE-Lsum (Lin, 2004) metrics, widely used in
natural language processing to assess the effective-
ness of algorithms.
Experiment Results: From Figure 2, we see
that CMVA-GS tends to have the highest ROUGE
scores across all metrics, indicating better align-
ment with human values compared to other models.
PT-model and Llama-13b have similar ROUGE
scores, but generally lower than those of CMVA-
GS. Agg13llama has the lowest ROUGE scores
among all models, suggesting relatively poorer per-
formance in values alignment. llama-7b and llama-
13b perform better than Agg13llama but still fall
short compared to CMVA-GS. Overall, CMVA-GS
appears to be the most effective model in terms of
aligning with human values, while the other mod-
els vary in their performance, with some showing
moderate alignment and others exhibiting relatively
lower alignment.

--- Page 5 ---

6
Limitations
Our paper addresses the contextual value align-
ment challenge by proposing a novel system that
performs contextual aggregation. Our proposed
system demonstrates superior results in terms of
alignment with human values compared to existing
state-of-the-art methods. However, we can high-
light multiple limitations of our system:
Memory: the system relies on multiple models
to perform its task. Running several models con-
currently can further exacerbate memory usage and
computational overhead. Each additional model
adds to the memory footprint and processing re-
quirements of the system.
User Acceptance and trust: Users may be hes-
itant to interact with a system that aggregates re-
sponses from multiple sources, especially if they
are uncertain about the reliability of the system’s
behavior.
Dependency on Training Data Quality: The ef-
fectiveness of the system heavily relies on the qual-
ity and representativeness of the training data used
for training each individual dialogue agent. If the
training data is biased, incomplete, or unrepresen-
tative of diverse perspectives, the aggregated sys-
tem may inherit these limitations, leading to sub-
optimal alignment with human values. If the initial
dataset used for training is incorrect, this can create
a feedback loop where the RL agent learns from its
own mistakes, exacerbating the problem over time.
References
Stella Biderman, Hailey Schoelkopf, Quentin Gregory
Anthony, Herbie Bradley, Kyle O’Brien, Eric Hal-
lahan, Mohammad Aflah Khan, Shivanshu Purohit,
USVSN Sai Prashanth, Edward Raff, et al. 2023.
Pythia: A suite for analyzing large language mod-
els across training and scaling.
In International
Conference on Machine Learning, pages 2397–2430.
PMLR.
Daniel S. Brown, Jordan Schneider, Anca Dragan, and
Scott Niekum. 2021. Value alignment verification. In
Proceedings of the 38th International Conference on
Machine Learning (ICML 2021), pages 1105–1115.
Josef Dai, Xuehai Pan, Ruiyang Sun, Jiaming Ji, Xinbo
Xu, Mickel Liu, Yizhou Wang, and Yaodong Yang.
2024. Safe RLHF: Safe reinforcement learning from
human feedback. In The Twelfth International Con-
ference on Learning Representations.
Maxwell Forbes, Jena D. Hwang, Vered Shwartz,
Maarten Sap, and Yejin Choi. 2020. Social chem-
istry 101: Learning to reason about social and moral
norms. In Proceedings of the 2020 Conference on
Empirical Methods in Natural Language Processing
(EMNLP), pages 653–670, Online. Association for
Computational Linguistics.
I. Gabriel. 2020. Artificial intelligence, values, and
alignment. In Minds & Machines, volume 30, pages
411–437.
Dan Hendrycks, Collin Burns, Steven Basart, Andrew
Critch, Jerry Li, Dawn Song, and Jacob Steinhardt.
2020. Aligning ai with shared human values. arXiv
preprint arXiv:2008.02275.
Edward J. Hu, Yelong Shen, Phillip Wallis, Zeyuan
Allen-Zhu, Yuanzhi Li, Shean Wang, Lu Wang, and
Weizhu Chen. 2021. Lora: Low-rank adaptation of
large language models.
Joel Jang, Seungone Kim, Bill Yuchen Lin, Yizhong
Wang, Jack Hessel, Luke Zettlemoyer, Hannaneh
Hajishirzi, Yejin Choi, and Prithviraj Ammanabrolu.
2023. Personalized soups: Personalized large lan-
guage model alignment via post-hoc parameter merg-
ing.
Jiaming Ji, Tianyi Qiu, Boyuan Chen, Borong Zhang,
Hantao Lou, Kaile Wang, Yawen Duan, Zhonghao
He, Jiayi Zhou, Zhaowei Zhang, et al. 2023. Ai
alignment: A comprehensive survey. arXiv preprint
arXiv:2310.19852.
Andreas Köpf, Yannic Kilcher, Dimitri von Rütte,
Sotiris Anagnostidis, Zhi-Rui Tam, Keith Stevens,
Abdullah Barhoum, Nguyen Minh Duc, Oliver Stan-
ley, Richárd Nagyfi, et al. 2023.
Openassistant
conversations–democratizing large language model
alignment. arXiv preprint arXiv:2304.07327.
Chin-Yew Lin. 2004. Rouge: A package for automatic
evaluation of summaries.
In Text summarization
branches out, pages 74–81.
Chunming Liu, Xin Xu, and Dewen Hu. 2015. Multi-
objective reinforcement learning: A comprehensive
overview. IEEE Transactions on Systems, Man, and
Cybernetics: Systems, 45(3):385–398.
Long Ouyang, Jeffrey Wu, Xu Jiang, Diogo Almeida,
Carroll Wainwright, Pamela Mishkin, Chong Zhang,
Sandhini Agarwal, Katarina Slama, Alex Ray, et al.
2022. Training language models to follow instruc-
tions with human feedback.
Advances in Neural
Information Processing Systems, 35:27730–27744.
Manel
Rodriguez-Soto,
Nardine
Osman,
Carles
Sierra, Paula Sánchez Veja, Rocio Cintas Garcia,
Cristina Farriols Danes, Montserrat Garcia Retor-
tillo, and Silvia Minguez Maso. 2024. Towards value
awareness in the medical field. In 16th International
Conference on Agents and Artificial Intelligence-
ICAART, volume 2024.
John Schulman, Filip Wolski, Prafulla Dhariwal,
Alec Radford, and Oleg Klimov. 2017.
Proxi-
mal policy optimization algorithms. arXiv preprint
arXiv:1707.06347.

--- Page 6 ---

Nisan Stiennon, Long Ouyang, Jeffrey Wu, Daniel
Ziegler, Ryan Lowe, Chelsea Voss, Alec Radford,
Dario Amodei, and Paul F Christiano. 2020. Learn-
ing to summarize with human feedback. Advances
in Neural Information Processing Systems, 33:3008–
3021.
Lichao Sun, Yue Huang, Haoran Wang, Siyuan Wu,
Qihui Zhang, Chujie Gao, Yixin Huang, Wenhan
Lyu, Yixuan Zhang, Xiner Li, et al. 2024. Trustllm:
Trustworthiness in large language models. arXiv
preprint arXiv:2401.05561.
Leandro von Werra, Younes Belkada, Lewis Tun-
stall, Edward Beeching, Tristan Thrush, Nathan
Lambert, and Shengyi Huang. 2020.
Trl: Trans-
former reinforcement learning. https://github.
com/huggingface/trl.
Dun Zeng, Yong Dai, Pengyu Cheng, Tianhao Hu, Wan-
shun Chen, Nan Du, and Zenglin Xu. 2023. On
diversified preferences of large language model align-
ment.
Caleb Ziems, Jane Yu, Yi-Chia Wang, Alon Halevy,
and Diyi Yang. 2022. The moral integrity corpus: A
benchmark for ethical dialogue systems. In Proceed-
ings of the 60th Annual Meeting of the Association
for Computational Linguistics (Volume 1: Long Pa-
pers), pages 3755–3773, Dublin, Ireland. Association
for Computational Linguistics.

```
