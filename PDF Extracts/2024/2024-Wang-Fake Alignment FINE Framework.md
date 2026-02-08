---
title: "2024-Wang-Fake Alignment FINE Framework - PDF Extract"
source_pdf: "2024-Wang-Fake Alignment FINE Framework.pdf"
pages: 37
extracted_at: "2026-02-08T06:02:19.566068"
---

# PDF Extract: 2024-Wang-Fake Alignment FINE Framework

**Source PDF:** 2024-Wang-Fake Alignment FINE Framework.pdf
**Total Pages:** 37

---

## Content

```
--- Page 1 ---

Primal-Dual Direct Preference Optimization
for Constrained LLM Alignment
Yihan Du
SUTD ESD
yihan du@sutd.edu.sg
Seo Taek Kong
UIUC ECE
skong10@illinois.edu
R. Srikant
UIUC ECE
rsrikant@illinois.edu
Abstract
The widespread application of Large Language Models (LLMs) imposes increasing demands
on safety, such as reducing harmful content and fake information, and avoiding certain forbidden
tokens due to rules and laws. While there have been several recent works studying safe alignment of
LLMs, these works either require the training of reward and cost models and incur high memory and
computational costs, or need prior knowledge about the optimal solution. Motivated by this fact,
we study the problem of constrained alignment in LLMs, i.e., maximizing the output reward while
restricting the cost due to potentially unsafe content to stay below a threshold. For this problem,
we propose a novel primal-dual DPO approach, which first trains a model using standard DPO on
reward preference data to provide reward information, and then adopts a rearranged Lagrangian
DPO objective utilizing the provided reward information to fine-tune LLMs on cost preference data.
Our approach significantly reduces memory and computational costs, and does not require extra
prior knowledge. Moreover, we establish rigorous theoretical guarantees on the suboptimality and
constraint violation of the output policy. We also extend our approach to an online data setting
by incorporating exploration bonuses, which enables our approach to explore uncovered prompt-
response space, and then provide theoretical results that get rid of the dependence on preference data
coverage. Experimental results on the widely-used preference dataset PKU-SafeRLHF demonstrate
the effectiveness of our approach.
1
Introduction
Large Language Models (LLMs) [Achiam et al.(2023)Achiam, Adler, Agarwal, Ahmad, Akkaya, Aleman, Almeida, Altens
Touvron et al.(2023a)Touvron, Lavril, Izacard, Martinet, Lachaux, Lacroix, Rozi`ere, Goyal, Hambro, Azhar, et al.,
Touvron et al.(2023b)Touvron, Martin, Stone, Albert, Almahairi, Babaei, Bashlykov, Batra, Bhargava, Bhosale, et al.]
have achieved a remarkable success in dialogues, summarization, instruction following, etc. Despite the
huge success of LLMs, LLMs may also output fabricated information and harmful content, such as texts in-
volving discrimination, crimes and moral issues [Gehman et al.(2020)Gehman, Gururangan, Sap, Choi, and Smith,
Lin et al.(2021)Lin, Hilton, and Evans, Wei et al.(2023)Wei, Haghtalab, and Steinhardt]. With the ex-
tensive application of LLMs, how to align them to enhance safety or impose constraints has become a
crucial problem. For example, we want to prevent LLMs from generating content that may have negative
societal impacts or ethical concerns. In Agentic AI or AI education applications, we need to avoid certain
tokens due to some rules and laws, or course content that has not been taught.
Recently, there are several works studying the safety alignment of LLMs. A popular formulation
is the constrained alignment problem, which aims to maximize the reward while constraining the cost
to stay below a threshold.
[Dai et al.(2024)Dai, Pan, Sun, Ji, Xu, Liu, Wang, and Yang] proposed a
safe reinforcement learning from human feedback (RLHF) framework for this problem, which train
reward and cost models on reward and cost preference data, respectively, and then apply an RL algo-
rithm to fine-tune LLMs to maximize the Lagrangian function under the learned reward and cost functions.
[Liu et al.(2024b)Liu, Sun, and Zheng, Wachi et al.(2024)Wachi, Tran, Sato, Tanabe, and Akimoto, Huang et al.(2024)H
Kim et al.(2025)Kim, Jang, Kim, Kim, Lee, Bae, and Lee] designed direct preference optimization (DPO)-
based safety alignment approaches. The idea of DPO is to directly fine-tune LLMs using preference data,
without training a reward model. However, these works either still require trained reward and cost mod-
els [Liu et al.(2024b)Liu, Sun, and Zheng, Huang et al.(2024)Huang, Li, Dobriban, Bastani, Hassani, and Ding],
or need prior knowledge of the optimal Lagrange multiplier [Wachi et al.(2024)Wachi, Tran, Sato, Tanabe, and Akimoto],
or are inefficient in cost information learning [Kim et al.(2025)Kim, Jang, Kim, Kim, Lee, Bae, and Lee].
1
arXiv:2510.05703v1  [cs.LG]  7 Oct 2025

--- Page 2 ---

Motivated by the above facts, we propose a novel and provably efficient primal-dual DPO approach. Our
approach first trains a model using standard DPO on reward preference data, and then fine-tunes LLMs
with a rearranged Lagrangian DPO objective on cost preference data, utilizing the reward information
provided by the standard DPO-trained model. Our approach avoids training reward and cost models,
which significantly reduces memory and computational costs, and does not require any prior knowledge
about the optimal solution. Moreover, we establish rigorous theoretical guarantees on the suboptimality
and constraint violation of the output policy. Finally, we investigate an online setting where collecting
preference data online is allowed. In this setting, we adopt exploration bonuses in our primal-dual DPO
approach to guide exploration on uncovered prompt-response space, and provide theoretical results that
remove the dependence on preference data coverage. All proofs are deferred to Appendix due to space
limits.
The contributions of our work are summarized as follows.
• We propose a novel primal-dual DPO approach for the constrained alignment problem of LLMs.
This approach first trains a model using standard DPO on reward preference data to offer reward
information, and then adopts a rearranged Lagrangian DPO objective to fine-tune LLMs utilizing
the offered reward information. This approach neither requires to train reward and cost models,
which significantly saves memory and computational costs, nor needs prior knowledge about the
optimal solution. We also provide rigorous suboptimality and cost violation guarantees.
• We conduct experiments on the PKU-SafeRLHF preference dataset [Dai et al.(2024)Dai, Pan, Sun, Ji, Xu, Liu, Wang
with model-based and GPT-4 evaluations. Empirical results show that our approach achieves an
effective helpfulness-harmlessness trade-off without training reward and cost models.
• In the online data setting, by incorporating exploration bonuses in our rearranged DPO objective,
our approach can effectively explore uncovered prompt-response space, and enjoys theoretical results
that get rid of the dependence on preference data coverage.
2
Related Work
In this section, we review the most related work and defer a more detailed description to Appendix A.
With the rapid development of LLMs, the alignment of LLMs has received extensive attention.
RLHF [Christiano et al.(2017)Christiano, Leike, Brown, Martic, Legg, and Amodei, Ouyang et al.(2022)Ouyang, Wu, Jia
and DPO [Rafailov et al.(2023)Rafailov, Sharma, Mitchell, Manning, Ermon, and Finn] are the two main
algorithmic frameworks for LLM alignment. RLHF first trains a reward model, and then applies an RL
algorithm with the learned reward model to fine-tune LLMs. DPO does not explicitly train a reward
model, but instead directly fine-tunes LLMs using preference data.
Recently, to reduce the harmful content generation of LLMs, there are several works studying safety
alignment. [Dai et al.(2024)Dai, Pan, Sun, Ji, Xu, Liu, Wang, and Yang] proposed a safe RLHF frame-
work. This framework trains a reward model and a cost model on reward and cost preference data, respec-
tively, and then applies an RL algorithm, PPO [Schulman et al.(2017)Schulman, Wolski, Dhariwal, Radford, and Klimov],
to maximize the Lagrangian function using the learned reward and cost functions. [Liu et al.(2024b)Liu, Sun, and Zheng,
Huang et al.(2024)Huang, Li, Dobriban, Bastani, Hassani, and Ding, Zhang et al.(2025)Zhang, Li, Hounie, Bastani, Ding
used trained reward and cost models to regenerate preference data according to the Lagrangian function,
and then performed DPO on regenerated data. [Wachi et al.(2024)Wachi, Tran, Sato, Tanabe, and Akimoto]
observed a relationship between the optimal solution of maximizing the Lagrangian function and that
of maximizing the reward function, and designed a stepwise DPO approach leveraging this observation.
However, their approach requires prior knowledge of the optimal Lagrange multiplier, and their theoretical
results depend on the deviation between the used and optimal Lagrange multipliers, which can be
unbounded. [Kim et al.(2025)Kim, Jang, Kim, Kim, Lee, Bae, and Lee] reordered preference data if the
preferred response is unsafe and the not-preferred response is safe, and ran DPO on reordered data. Their
approach is inefficient in cost information learning.
In contrast to the above works, our approach does not require trained reward and cost models, which
saves memory and computational costs, or prior knowledge of the optimal Lagrange multiplier. Moreover,
we investigate the online data setting, and develop an exploratory primal-dual DPO approach which
achieves theoretical results without the dependence on preference data coverage.
2

--- Page 3 ---

3
Preliminaries
Reinforcement Learning from Human Feedback (RLHF). The RLHF framework [Christiano et al.(2017)Christiano,
Ouyang et al.(2022)Ouyang, Wu, Jiang, Almeida, Wainwright, Mishkin, Zhang, Agarwal, Slama, Ray, et al.]
consists of three phases: (i) supervised fine-tuning a pre-trained LLM on a high-quality dataset of down-
stream tasks, e.g., dialogue and summarization, (ii) reward model learning, and (iii) RL optimization
with the learned reward model.
Let X and Y denote the sets of all possible prompts and responses. We define a policy π : X →△Y
as a mapping from X to a distribution on Y, where △Y denotes the set of all distributions on Y. We
formulate an LLM as a policy, and use πref to denote the supervised fine-tuned (SFT) model.
In the reward model learning phase, we have access to a reward preference dataset Dr = {xr
i , yrw
i , yrℓ
i }N r
i=1,
where xr
i is a prompt, yrw
i , yrℓ
i
are preferred and dispreferred responses under prompt xr
i , and the super-
script r refers to reward preference. The generation of preference data is as follows: We assume that there
exists an unknown reward function r∗(x, y) ∈[−Rmax, Rmax] for some constant Rmax, which models the
helpfulness of response y under prompt x. Human annotators compare a pair of responses yrw, yrℓunder
prompt x. Then, we assume that the probability that yrw is preferred to yrℓunder prompt x follows the
Bradley-Terry model [Bradley & Terry(1952)Bradley and Terry]:
Pr

yrw ≻yrℓ|x

=
exp(r∗(x, yrw))
exp(r∗(x, yrw)) + exp(r∗(x, yrℓ)) = σ
 r∗(x, yrw) −r∗(x, yrℓ)

,
(1)
where σ(z) :=
1
1+exp(−z) denotes the sigmoid function. With the preference data, we train a reward model
r via maximum likelihood estimation (MLE), i.e., minimizing the negative log-likelihood loss:
min
r
−1
N r
Nr
X
i=1
log σ
 r(xr
i , yrw
i ) −r(xr
i , yrℓ
i )

.
(2)
In the RL optimization phase, we apply RL algorithms, e.g., PPO [Schulman et al.(2017)Schulman, Wolski, Dhariwal, R
to fine-tune the SFT model under the learned reward model r:
max
π
Ex∼Dp 
Ey∼π(·|x) [r(x, y)] −β · KL (π(·|x)∥πref(·|x))

.
(3)
Here β is a parameter controlling the deviation between the trained model π and SFT model πref, since we
do not want the trained model to be too far away from the SFT model. Dp is a distribution of prompts,
and the optimal solution to Eq. (3) is independent of Dp, which will be presented in Eq. (4).
Direct Preference Optimization (DPO). Recently, [Rafailov et al.(2023)Rafailov, Sharma, Mitchell, Manning, Erm
designed an direct preference optimization (DPO) approach, which bypasses the reward model training
phase in RLHF, and directly fine-tunes LLMs using preference data. The derivation idea of DPO is as
follows.
First, the optimal solution to Eq. (3) is [Peters & Schaal(2007)Peters and Schaal, Peng et al.(2019)Peng, Kumar, Zhang
π∗
r(y|x) =
πref(y|x) exp

1
β r(x, y)

Zr(x)
,
(4)
where Zr(x) := P
y′∈Y πref(y′|x) exp( 1
β r(x, y′)) is the partition function. Then, we can rewrite Eq. (4) to
express the reward function r by the optimal policy π∗
r as
r(x, y) = β log π∗
r(y|x)
πref(y|x) + β log Zr(x).
(5)
Eqs. (4) and (5) hold for any reward function r. Hence, the Bradley-Terry model in Eq. (1) can be
expressed by the optimal policy π∗
r∗:
Pr

yrw ≻yrℓ|x

= σ

β log π∗
r∗(yrw|x)
πref(yrw|x) −β log π∗
r∗(yrℓ|x)
πref(yrℓ|x)

,
(6)
where the partition function Zr∗(x) is cancelled out. Now, by expressing the probability that preference
data happen by π∗
r∗, we can replace the likelihood in the MLE training objective in Eq. (2) by Eq. (6),
and obtain a new objective with the optimization variable directly being the policy:
min
π
−1
N r
N r
X
i=1
log σ

β log π(yrw
i |xr
i )
πref(yrw
i |xr
i ) −β log π(yrℓ
i |xr
i )
πref(yrℓ
i |xr
i )

.
(7)
3

--- Page 4 ---

Eq. (7) is the training objective of DPO. Thus, DPO directly uses preference data to fine-tune LLMs
without training a reward model, and enjoys lower memory and computational costs than RLHF.
Safe RLHF. To enhance safety in LLM alignment, [Dai et al.(2024)Dai, Pan, Sun, Ji, Xu, Liu, Wang, and Yang]
proposed a safe RLHF framework. In safe RLHF, we assume that there exists an unknown cost function
c∗(x, y) ∈[−Cmax, Cmax] for some constant Cmax, which characterizes the harmfulness of response y under
prompt x. We have access to a cost preference dataset Dc = {xc
i, ycw
i , ycℓ
i }Nc
i=1, where ycw
i , ycℓ
i
denote
unsafer and safer responses under prompt xc
i (ycw
i
has a higher cost than ycℓ
i ), and the superscript c
stands for cost preference. We assume that cost preference is generated according to the Bradley-Terry
model with cost function c∗, i.e.,
Pr

ycw ≻ycℓ|x

=
exp(c∗(x, ycw))
exp(c∗(x, ycw)) + exp(c∗(x, ycℓ)) = σ
 c∗(x, ycw) −c∗(x, ycℓ)

.
(8)
Similar to Eq. (2), we can also train a cost model c via MLE:
min
c
−1
N c
Nc
X
i=1
log σ
 c(xc
i, ycw
i ) −c(xc
i, ycℓ
i )

.
(9)
To restrict the costs of LLM outputs within a threshold, we consider the constrained optimization:
max
π
Ex∼Dp 
Ey∼π(·|x) [r(x, y)] −β · KL (π(·|x)∥πref(·|x))

s.t.
c(x, y) ≤0,
∀x ∼Dp, y ∼π(·|x).
Here for simplicity, we set the threshold of harmfulness to 0. The above problem is hard to solve using
neural networks, since it requires the cost of every possible response y to stay below 0.
To feasibly perform safety alignment, many prior works, e.g., [Dai et al.(2024)Dai, Pan, Sun, Ji, Xu, Liu, Wang, and Ya
Wachi et al.(2024)Wachi, Tran, Sato, Tanabe, and Akimoto, Liu et al.(2024b)Liu, Sun, and Zheng, Kim et al.(2025)Kim
consider a relaxed optimization problem with an expected cost constraint, which we called constrained
alignment problem:
max
π
f(π) := Ex∼Dp 
Ey∼π(·|x) [r∗(x, y)] −β · KL (π(·|x)∥πref(·|x))

s.t.
g(π) := Ex∼Dp,y∼π(·|x)[c∗(x, y)] ≤0.
(10)
In this work, we also study this relaxed problem. Then, it is natural to look into the Lagrangian dual
problem of the above constrained optimization:
min
λ≥0 max
π
L(π; λ) := Ex∼Dp 
Ey∼π(·|x) [r∗(x, y)−λ · c∗(x, y)]−β·KL (π(·|x)∥πref(·|x))

,
(11)
where λ ≥0 is a Lagrange multiplier. Throughout the paper, we call L(π; λ) the Lagrangian function.
With the above unconstrained problem, [Dai et al.(2024)Dai, Pan, Sun, Ji, Xu, Liu, Wang, and Yang]
regarded r−λ·c as a new reward function and applied an RL algorithm PPO [Schulman et al.(2017)Schulman, Wolski, Dhari
to maximize L(π; λ), and performed subgradient descent [Beck(2017)] to update λ. This safe RLHF
framework requires to train both reward and cost models, which incurs high memory and computational
costs.
4
Primal-Dual DPO Utilizing Standard DPO
In this section, we propose a provably efficient primal-dual DPO approach for the constrained alignment
problem (Eq. (10)), utilizing a model trained using standard DPO on reward preference data to provide
reward information. We first describe the key idea behind our approach, and present the specific algorithm
PD-DPO which has rigorous theoretical guarantees.
4.1
Our Approach
First, we have that the optimal solution to maxπ L(π; λ) in Eq. (11) is
r(x, y) −λ · c(x, y) = β log π∗
r−λ·c(y|x)
πref(y|x)
+ β log Zr−λ·c(x),
(12)
4

--- Page 5 ---

where Zr−λ·c(x) := P
y′∈Y πref(y′|x) exp( 1
β (r(x, y′) −λ · c(x, y′))) is the partition function, and r and c
can be any reward and cost functions.
When one wants to apply the derivation idea of DPO in Eqs. (6) and (7), a difficulty arises: We
do not have preference data generated according to r −λ · c, but only have preference data generated
according to r and c separately. Thus, we cannot use β log
π∗
r−λ·c(y|x)
πref(y|x)
to directly express data likelihood
as in Eq. (7), which means that the DPO derivation idea cannot be directly applied here.
To overcome this difficulty, we first rearrange Eq. (12) as
c(x, y) = 1
λ

r(x, y) −β log π∗
r−λ·c(y|x)
πref(y|x)
−β log Zr−λ·c(x)

.
Plugging the above equation with r∗and c∗into Eq. (8), the generation of cost preference data can be
rewritten as Pr[ycw ≻ycℓ|x] =
σ
 
1
λ

r∗(x, ycw) −β log π∗
r∗−λ·c∗(ycw|x)
πref(ycw|x)
−

r∗(x, ycℓ) −β log π∗
r∗−λ·c∗(ycℓ|x)
πref(ycℓ|x)
!
,
where Zr∗−λ·c∗(x) is cancelled out. Then, replacing the cost preference data likelihood in Eq. (9) by
the above equation, we can obtain a training objective with the optimization variable directly being the
policy which is supposed to get close to π∗
r∗−λ·c∗during training:
min
c
−1
N c
N c
X
i=1
log σ
 1
λ
 r∗(xc
i, ycw
i ) −βLπ(ycw
i |xc
i) −
 r∗(xc
i, ycℓ
i ) −βLπ(ycℓ
i |xc
i)

,
(13)
where Lπ(y|x) := log
π(y|x)
πref(y|x) is the logarithmic ratio of response y under x between π and πref.
Now the main challenge lies in that we do not know r∗, and meanwhile, we do not want to explicitly
train a reward model in order to keep memory and computational efficiency. To handle this challenge, we
make an observation that r∗(xc
i, ycw
i ) −r∗(xc
i, ycℓ
i ) can be expressed by β log π∗
r∗(ycw
i
|xc
i )
πref(ycw
i
|xc
i ) −β log π∗
r∗(ycℓ
i |xc
i )
πref(ycℓ
i |xc
i )
according to Eq. (4). Then, π∗
r∗is what we can learn by training a model using standard DPO on reward
preference data.
Therefore, using this observation, the training objective Eq. (13) can be rewritten as
min
c
−1
N c
Nc
X
i=1
log σ
β
λ

Lπ∗
r∗(ycw
i |xc
i)−Lπ(ycw
i |xc
i) −

Lπ∗
r∗(ycℓ
i |xc
i)−Lπ(ycℓ
i |xc
i)

,
(14)
where π∗
r∗can be learned by first training a model using standard DPO on reward preference data.
Eq. (14) is the main idea of our primal-dual DPO approach utilizing standard DPO. This approach
avoids training reward and cost models, which significantly reduces memory and computational costs com-
pared to prior works [Dai et al.(2024)Dai, Pan, Sun, Ji, Xu, Liu, Wang, and Yang, Liu et al.(2024b)Liu, Sun, and Zheng,
Huang et al.(2024)Huang, Li, Dobriban, Bastani, Hassani, and Ding, Zhang et al.(2025)Zhang, Li, Hounie, Bastani, Ding
Our approach shows even more advantages when there already exists a trained model on reward pref-
erence data, which is often the case since there are many high-quality and open-source LLMs, e.g.,
LLaMA [Dubey et al.(2024)Dubey, Jauhri, Pandey, Kadian, Al-Dahle, Letman, Mathur, Schelten, Yang, Fan, et al.]
and Gemma [Team et al.(2024a)Team, Mesnard, Hardin, Dadashi, Bhupatiraju, Pathak, Sifre, Rivi`ere, Kale, Love, et al.
Team et al.(2024b)Team, Riviere, Pathak, Sessa, Hardin, Bhupatiraju, Hussenot, Mesnard, Shahriari, Ram´e, et al.,
Team et al.(2025)Team, Kamath, Ferret, Pathak, Vieillard, Merhej, Perrin, Matejovicova, Ram´e, Rivi`ere, et al.].
4.2
A Provably Efficient Algorithm PD-DPO
While Eq. (14) has presented the main idea of our primal-dual DPO approach, to enable rigorous
theoretical guarantees, we develop a specific provably efficient algorithm PD-DPO, which imposes policy
search constraints based on Eq. (14) and enjoys suboptimality and constraint violation guarantees. Before
describing the specific algorithm PD-DPO, we first introduce several assumptions.
Assumption 1 (Slater’s Condition). There exists a policy ¯π which satisfies Ex∼Dp,y∼¯π(·|x)[c∗(x, y)] < 0.
In addition, we know a constant ρ ≥
f(π∗)−f(¯π)
−Ex∼Dp,y∼¯π(·|x)[c∗(x,y)].
5

--- Page 6 ---

Algorithm 1: PD-DPO
Input: β,πref, ρ, λ1, K, N CE, M CE, Dp, Dr ={(xr
i , yrw
i , yrℓ
i )}i∈[N r],Dc ={(xc
i, ycw
i , ycℓ
i )}i∈[N c]
1 Train a model using standard DPO on reward preference data:
π∗
ˆr ←argmin
π∈Πr −1
N r
Nr
X
i=1
log σ

β log π(yrw
i |xr
i )
πref(yrw
i |xr
i ) −β log π(yrℓ
i |xr
i )
πref(yrℓ
i |xr
i )

,
(15)
where Πr is defined in Eq. (17)
2 for k = 1, 2, . . . , K do
3
Train a model using a rearranged Lagrangian DPO objective on cost preference data:
πk ←argmin
π∈Πc
k
−1
N c
Nc
X
i=1
log σ
 
1
λk

β log π∗
ˆr(ycw
i |xc
i)
πref(ycw
i |xc
i) −β log π(ycw
i |xc
i)
πref(ycw
i |xc
i)
−

β log π∗
ˆr(ycℓ
i |xc
i)
πref(ycℓ
i |xc
i) −β log π(ycℓ
i |xc
i)
πref(ycℓ
i |xc
i)
!
,
(16)
where Πc
k is defined in Eq. (18)
4
Construct an estimate ˜ck for Ex∼Dp,y∼πk(·|x)[c∗(x, y)]: For i = 1, . . . , NCE, first sample
xi ∼Dp, yi ∼πk(·|xi). Then, for each (xi, yi), sample {Zi,j}M CE
j=1
i.i.d.
∼Ber(σ(c∗(xi, yi))). Set
˜ck ←
1
NCE
PN CE
i=1 σ−1(
1
M CE
PM CE
j=1 Zi,j), where σ−1(z) := log(
1
1−z −1) is the inverse of the
sigmoid function
5
λk+1 ←Proj[0,2ρ](λk + η˜ck), where η :=
λ1
Cmax
√
K
6 return πout
K
:= unif(π1, . . . , πK)
This assumption is common in the constrained optimization and learning literature [Beck(2017),
Efroni et al.(2020)Efroni, Mannor, and Pirotta]. In practice, it is reasonable that there exists a safe
policy model, e.g., a language model which refuses to answer harmful questions albeit less helpful.
Following prior works [Dai et al.(2024)Dai, Pan, Sun, Ji, Xu, Liu, Wang, and Yang, Kim et al.(2025)Kim, Jang, Kim,
we also allow querying cost binary feedback from human annotators, which indicates whether a response
y is safe under prompt x. Such cost binary feedback is generated according to
Pr [Z(y) = 1|x] = σ (c∗(x, y))
and Pr[Z(y) = 0|x] = 1 −σ (c∗(x, y)), where Z(y) = 1 and Z(y) = 0 denote that y is unsafe and safe,
respectively. We will use cost binary feedback in algorithm PD-DPO to estimate the cost of the current
trained model for Lagrange multiplier update.
Now we present an efficient and provably convergent primal-dual DPO algorithm PD-DPO. PD-DPO
first trains a model using standard DPO on reward preference data, and leverages this model to provide
reward information to train a model using a rearranged Lagrangian DPO objective with policy search
constraints. Then, PD-DPO conducts projected subgradient descent to update the Lagrange multiplier.
PD-DPO performs such model training and Lagrange multiplier update alternately.
Algorithm 1 illustrates the algorithm procedure of PD-DPO. Specifically, PD-DPO first trains a model π∗
ˆr us-
ing the standard DPO objective [Rafailov et al.(2023)Rafailov, Sharma, Mitchell, Manning, Ermon, and Finn]
on reward preference data Dr within a constrained policy search range:
Πr :=


π(y|x) =
πref(y|x) · exp

1
β r(x, y)

P
y′∈Y πref(y′|x) · exp

1
β r(x, y′)
 : r ∈[−Rmax, Rmax]


.
(17)
Since we use only finite preference data, we cannot exactly learn π∗
r∗. Instead, we learn a reward function
ˆr which is close to r∗and implicitly maintained by the policy π∗
ˆr. The notation π∗
ˆr denotes the optimal
policy under the learned reward function ˆr (Eq. (4)). The policy search range Πr is used to restrict the
learned reward function ˆr within [−Rmax, Rmax] (Line 1).
Next, in each iteration k, given a Lagrange multiplier λk, PD-DPO utilizes the reward information
provided by π∗
ˆr to train a model using a rearranged Lagrangian DPO objective as derived in Section 4.1,
6

--- Page 7 ---

but with a constrained policy search range:
Πc
k :=


π(y|x)=
πref(y|x) exp

1
β

β log π∗
ˆr (y|x)
πref(y|x) −λkc(x, y)

P
y′∈Y πref(y′|x) exp

1
β

β log π∗
ˆr (y′|x)
πref(y′|x) −λkc(x, y′)
: c∈[−Cmax, Cmax]



(a)
=


π(y|x)=
πref(y|x) exp

1
β (ˆr(x, y) −λkc(x, y))

P
y′∈Y πref(y′|x) exp

1
β (ˆr(x, y′) −λkc(x, y′))
 : c∈[−Cmax, Cmax]


.
(18)
Here equality (a) is due to Eq. (5) and the fact that the partition function Zˆr(x) only depends on x
and can be cancelled out in the softmax form. Πc
k is used to restrict the learned cost function within
[−Cmax, Cmax] (Line 3).
After obtaining πk, we estimate the cost of πk for Lagrange multiplier update using the following
scheme: We i.i.d. draw N CE prompt-response pairs {(xi, yi)}NCE
i=1
using πk. For each pair (xi, yi), we
i.i.d. query human annotators whether response yi is safe under prompt xi M CE times, and obtain M CE
cost binary feedback {Zi,j}M CE
j=1
drawn from Ber(σ(c∗(xi, yi))). Then, we take the inverse of the sigmoid
function σ−1(·) on the average of these M CE Bernoulli outcomes to obtain an estimate ˜ck for the expected
cost of πk (Line 4). In analysis, we can bound the deviation between this estimate ˜ck and the expected
cost of πk (see Appendix C.2). After cost estimation, PD-DPO performs projected subgradient descent
with ˜ck to update Lagrange multiplier λk, and enters the next iteration (Line 5).
4.3
Theoretical Guarantees of Algorithm PD-DPO
Unlike prior works [Dai et al.(2024)Dai, Pan, Sun, Ji, Xu, Liu, Wang, and Yang, Liu et al.(2024b)Liu, Sun, and Zheng,
Kim et al.(2025)Kim, Jang, Kim, Kim, Lee, Bae, and Lee] which do not provide theoretical guarantees
for their output policy models, we establish rigid suboptimality and constraint violation guarantees for
the output policy of algorithm PD-DPO.
First, we note that our rearranged Lagrangian DPO objective (Eq. (16)) and the safe RLHF procedure,
which first trains reward and cost models using MLE and maximizes L(π; λk) under the learned reward
and cost functions, have the same set of optimal solutions (see Theorem 4 in Appendix C.1 for a formal
statement). Next, we present the theoretical results of algorithm PD-DPO.
For any (x, y) ∈X × Y, let ϕ(x, y) denote a |X||Y|-dimensional vector where the entry corresponding
to (x, y) is 1 and all other entries are 0. Let α(z) :=
q
(exp (z) + exp (−z) + 2)2  |X||Y| + log
  1
δ

+ γz2
and
B := ρCmax
s
log
  K
δ

N CE
+ ρW
v
u
u
tlog

|X||Y|N CEK
δ

M CE
+ρ·α(Cmax)

E(x,y)∼Dp×π∗
h
∥ϕ(x, y)∥(ΣDc+γI)−1
i
+ 1
K
K
X
k=1
E(x,y)∼Dp×πk
h
∥ϕ(x, y)∥(ΣDc+γI)−1
i
+α(Rmax)

E(x,y)∼Dp×π∗
h
∥ϕ(x, y)∥(ΣDr +γI)−1
i
+ 1
K
K
X
k=1
E(x,y)∼Dp×πk
h
∥ϕ(x, y)∥(ΣDr +γI)−1
i
.
Here ΣD⋄:= P
(x,y,y′)∈D⋄(ϕ(x, y) −ϕ(x, y′)) (ϕ(x, y) −ϕ(x, y′)⊤with ⋄∈{r, c}. For any π, (x, y) ∼
Dp × π denotes x ∼Dp, y ∼π(·|x). γ > 0 is an arbitrary regularization parameter. W is a parameter
dependent on Cmax, which is formally defined in Eq. (28) in Appendix C.2.
Theorem 1 (Result of Algorithm PD-DPO). With probability at least 1 −δ, for any K ≥1, the output
policy πout
K
of algorithm PD-DPO satisfies
f(π∗) −f(πout
K ) = O
λ1Cmax
√
K
+ B

,
g(πout
K ) = O
Cmax
ρ
√
K
(λ1 −2ρ)2
λ1
+ λ1

+ B
ρ

.
In this result, the
1
√
K term is an inherent error of the primal-dual method. The
1
√
NCE and
1
√
M CE
terms are the error due to cost estimation. The four ∥ϕ(x, y)∥(ΣD⋄+γI)−1 terms are the error due to
inferring reward and cost information from preference data. The ∥ϕ(x, y)∥(ΣD(⋄)+γI)−1 factor stands for
7

--- Page 8 ---

how broadly the given preference data cover. Theorem 1 shows that the suboptimality and cost violation
of the output policy by algorithm PD-DPO can be arbitrarily close to zero, when the given preference data
have sufficient coverage, and the number of preference data, the number of iterations K, and the number
of samples for cost estimation N CE, M CE are large enough.
5
Exploratory Primal-Dual DPO with Exploration Bonuses
The result of algorithm PD-DPO (Theorem 1) depends on the coverage of preference data, i.e., ∥ϕ(x, y)∥(ΣD⋄+γI)−1.
If the given preference data do not have sufficient coverage, the suboptimality and constraint violation of
PD-DPO can be unbounded.
To resolve this coverage issue, we further investigate an online setting where collecting preference
data online is allowed. In this setting, we develop an exploratory primal-dual DPO algorithm O-PD-DPO,
which incorporates exploration bonuses bc
k(x, y) and br
k(x, y) in the rearranged Lagrangian DPO and
standard DPO objectives. In algorithm O-PD-DPO, the trained policy has an incentive to explore uncovered
prompt-response space, and gradually expands the used preference data. We defer the pseudo-code and
detailed description of O-PD-DPO to Appendix D due to space limits.
We take the incorporation of br
k in standard DPO as an example to explain the intuition behind why
including exploration bonuses can encourage exploration. For the standard DPO objective (Eq. (15)),
algorithm O-PD-DPO will subtract a br(x, yrw) term from the original β log
π(yrw|x)
πref(yrw|x) term. When preference
data do not cover (x, yrw) well, br(x, yrw) will be large. Then, subtracting a large value from β log
π(yrw|x)
πref(yrw|x)
encourages π to put a higher probability on yrw to maintain the original value of β log
π(yrw|x)
πref(yrw|x) which
achieves the optimal value of the MLE objective function. Thus, by incorporating exploration bonuses in
the training objective, the trained policy is incentivized to explore uncovered prompt-response space.
While there have been several recent works studying DPO with exploration [Liu et al.(2024a)Liu, Lu, Zhang, Liu, Guo, Y
Xie et al.(2025)Xie, Foster, Krishnamurthy, Rosset, Awadallah, and Rakhlin, Cen et al.(2025)Cen, Mei, Goshvadi, Dai, Y
their ideas cannot be directly applied to our work, since their approaches perform optimistic exploration
mainly for the optimal policy which maximizes a certain reward function, but cannot deal with the opti-
mism for the optimal policy of a constrained optimization. To handle the exploration for the constrained
alignment problem, we adopt exploration bonuses in our rearranged Lagrangian DPO training objective,
and develop new analysis to get rid of offline dataset dependence. This design of DPO with bonuses and
its analysis are novel to the RLHF literature.
Now we provide the suboptimality and constraint violation guarantees of algorithm O-PD-DPO.
Let ω(z) :=
q
(exp (z) + exp (−z) + 2)2 · (|X||Y| + log( K
δ ))/N on + γonz2 and
Bon := ρCmax
s
log
  K
δ

N CE
+ ρW
v
u
u
tlog

|X||Y|N CEK
δ

M CE
+ (ρ · ω(Cmax) + ω(Rmax)) ·
s
|X||Y|K

log
γon + |Dr
1| + K
|X||Y|γon

+
1
Cbase log
γon + |Dr
1| + CbaseK
|X||Y|γon

.
Here N on is the number of preference data collected online in each iteration.
γon > 0 is a given
regularization parameter. Cbase is a parameter related to a baseline policy which is used in online data
collection. The definitions of the baseline policy and Cbase are in Eq. (34) in Appendix D.
Theorem 2 (Result of Algorithm O-PD-DPO). With probability at least 1 −δ, for any K ≥1, the output
policy πout
K
of algorithm O-PD-DPO satisfies
f(π∗) −f(πout
K ) = O
λ1Cmax
√
K
+ Bon

,
g(πout
K ) = O
Cmax
ρ
√
K
(λ1 −2ρ)2
λ1
+ λ1

+ Bon
ρ

.
Compared to Theorem 1, here the results have no dependence on the coverage of preference data, i.e.,
∥ϕ(x, y)∥(ΣD⋄+γI)−1. Theorem 2 demonstrates that the adoption of exploration bonuses in the rearranged
Lagrangian DPO objective effectively incentivizes exploration and expands the used preference data
during training. When all problem parameters K, N CE, M CE, N on are large enough, the suboptimality
and constraint violation bounds will shrink to zero.
8

--- Page 9 ---

1
0
1
2
Helpfulness (Reward)
10
5
0
5
10
15
20
Harmlessness (Negated Cost)
Model-based Evaluation
1000
1050
1100
1150
1200
Helpfulness Elo Score
1000
1100
1200
1300
1400
1500
Harmlessness Elo Score
GPT-4 Evaluation
SFT (Alpaca-7b-reproduced)
Beaver-v3.0
SafeDPO
PD-DPO (ours)
Figure
1:
(Left)
Rewards
and
negated
costs
of
responses
generated
by
compared
language
models
when
evaluated
by
Beaver-7b-unified-reward
and
Beaver-7b-unified-
cost [Dai et al.(2024)Dai, Pan, Sun, Ji, Xu, Liu, Wang, and Yang]. (Right) Helpfulness and harmlessness
Elo scores evaluated by GPT-4. Our PD-DPO model achieves the best helpfulness performance while
reducing harmful content generation compared to the SFT model.
While prior works [Huang et al.(2024)Huang, Li, Dobriban, Bastani, Hassani, and Ding, Wachi et al.(2024)Wachi, Tra
also provide theoretical results, [Huang et al.(2024)Huang, Li, Dobriban, Bastani, Hassani, and Ding] re-
quire an assumption that the optimal policy is feasible under the estimated reward and cost functions.
The results in [Wachi et al.(2024)Wachi, Tran, Sato, Tanabe, and Akimoto] have a term of the deviation
between the used and optimal Lagrange multipliers, which can be unbounded since their algorithm does
not contain any scheme to learn the optimal Lagrange multiplier. In addition, the results in prior works
depend on preference data coverage. To the best of our knowledge, Theorem 2 is the first result for the
constrained alignment problem (Eq. 10) to get rid of the dependence on preference data coverage.
6
Experiments
In this section, we provide experimental results to demonstrate the effectiveness of our approach.
Our experiments are run on an Intel Xeon Platinum 8558 CPU and a single NVIDIA GH200
96GB GPU. Following prior works, e.g., [Dai et al.(2024)Dai, Pan, Sun, Ji, Xu, Liu, Wang, and Yang,
Kim et al.(2025)Kim, Jang, Kim, Kim, Lee, Bae, and Lee], we use the PKU-SafeRLHF preference dataset [Dai et al.(2024)
to train and evaluate models, and take Alpaca-7b-reproduced [Taori et al.(2023)Taori, Gulrajani, Zhang, Dubois, Li, Gue
as the SFT model, which is a fine-tuned version of the LLaMA-2-7b model [Touvron et al.(2023b)Touvron, Martin, Stone, A
on the Alpaca dataset [Taori et al.(2023)Taori, Gulrajani, Zhang, Dubois, Li, Guestrin, Liang, and Hashimoto].
We compare our algorithm PD-DPO with the SFT model Alpaca-7b-reproduced and existing open-source
safety alignment algorithms Beaver-v3.0 [Dai et al.(2024)Dai, Pan, Sun, Ji, Xu, Liu, Wang, and Yang]
and SafeDPO [Kim et al.(2025)Kim, Jang, Kim, Kim, Lee, Bae, and Lee]. Following existing works, we
conduct both model-based and GPT-4 [Achiam et al.(2023)Achiam, Adler, Agarwal, Ahmad, Akkaya, Aleman, Almeida, A
evaluations.
For model-based evaluation, the left sub-figure in Figure 1 presents the average reward and negated
cost scores (to keep consistency between two sub-figures regarding harmlessness) of responses generated
by compared language models, when evaluated by the reward model Beaver-7b-unified-reward and cost
model Beaver-7b-unified-cost [Dai et al.(2024)Dai, Pan, Sun, Ji, Xu, Liu, Wang, and Yang]. For GPT-4
evaluation, the right sub-figure in Figure 1 plots the Elo scores of compared models regarding helpfulness
and harmlessness evaluated by GPT-4. Figure 1 shows that our algorithm PD-DPO achieves the best perfor-
mance regarding helpfulness while effectively improving harmlessness compared to the SFT model. While
the harmlessness performance of our PD-DPO is worse than Beaver-v3.0, Beaver-v3.0 requires much higher
memory and computational costs than our algorithm (cannot be run on a single GH200 GPU with 96GB
memory), and does not have rigorous theoretical guarantees as our algorithm. This trade-off between perfor-
mance and memory/computational cost is similar to the trade-offs between DPO and RLHF that have been
reported in the literature [Rafailov et al.(2023)Rafailov, Sharma, Mitchell, Manning, Ermon, and Finn,
Xu et al.(2024)Xu, Fu, Gao, Ye, Liu, Mei, Wang, Yu, and Wu].
7
Conclusion
In this work, we study the constrained alignment problem for LLMs, which aims to maximize the
reward while constraining the cost to stay below a threshold. We develop a novel primal-dual DPO
approach for the offline and online data settings. Our approach adopts a rearranged Lagrangian DPO
9

--- Page 10 ---

training objective, utilizing the reward information provided by a model trained using standard DPO.
We establish suboptimality and constraint violation guarantees, and provide experimental results on the
PKU-SafeRLHF dataset [Dai et al.(2024)Dai, Pan, Sun, Ji, Xu, Liu, Wang, and Yang] to validate the
effectiveness of our approach.
There are several interesting directions for future work. One direction is to extend our theoretical
results to the policy parameterization (large prompt-response space) setting. The challenge is that under
popular policy parameterization settings such as the log-linear policy class, the constrained alignment
problem can be non-convex with respect to the policy parameter. Another direction is to investigate
stricter cost constraints, e.g., per-response constraints, which is challenging to tackle using neural networks.
Ethics statement
This paper studies the alignment of LLMs to enhance safety or impose certain constraints. The data
used in experiments may contain harmful or offensive content.
Reproducibility statement
This paper provides theoretical guarantees and experimental results for the proposed primal-dual DPO
approach. All results are reproducible. For theoretical guarantees, the assumptions required are stated
in Sections 3 and 4.2 and Appendix D, and all proofs are presented in Appendix. For experimental
results, the experimental setup is described in Section 6 and Appendix B, and the code is provided in
supplementary materials.
Acknowledgments
The work was supported in part by NSF Grants CNS 23-12714 and CCF 22-07547 and AFOSR Grant,
FA9550-24-1-0002. We also thank NVIDIA’s Applied Research Accelerator Program for donating two
A100 GPUs to Prof. Rakesh Nagi’s group, which he graciously allowed us to use in the development
stages of this work.
References
[Abbasi-Yadkori et al.(2011)Abbasi-Yadkori, P´al, and Szepesv´ari] Yasin Abbasi-Yadkori, D´avid P´al, and
Csaba Szepesv´ari.
Improved algorithms for linear stochastic bandits.
In Advances in Neural
Information Processing Systems, volume 24, 2011.
[Achiam et al.(2023)Achiam, Adler, Agarwal, Ahmad, Akkaya, Aleman, Almeida, Altenschmidt, Altman, Anadkat, et al
Josh Achiam, Steven Adler, Sandhini Agarwal, Lama Ahmad, Ilge Akkaya, Florencia Leoni Aleman,
Diogo Almeida, Janko Altenschmidt, Sam Altman, Shyamal Anadkat, et al. GPT-4 technical report.
arXiv preprint arXiv:2303.08774, 2023.
[Agarwal et al.(2020)Agarwal, Henaff, Kakade, and Sun] Alekh Agarwal, Mikael Henaff, Sham Kakade,
and Wen Sun. PC-PG: Policy cover directed exploration for provable policy gradient learning. In
Advances in Neural Information Processing Systems, volume 33, pp. 13399–13412, 2020.
[Azar et al.(2024)Azar, Guo, Piot, Munos, Rowland, Valko, and Calandriello] Mohammad Gheshlaghi
Azar, Zhaohan Daniel Guo, Bilal Piot, Remi Munos, Mark Rowland, Michal Valko, and Daniele
Calandriello. A general theoretical paradigm to understand learning from human preferences. In
International Conference on Artificial Intelligence and Statistics, pp. 4447–4455. PMLR, 2024.
[Beck(2017)] Amir Beck. First-order methods in optimization. SIAM, 2017.
[Bradley & Terry(1952)Bradley and Terry] Ralph Allan Bradley and Milton E Terry. Rank analysis of
incomplete block designs: I. the method of paired comparisons. Biometrika, 39(3/4):324–345, 1952.
[Cen et al.(2025)Cen, Mei, Goshvadi, Dai, Yang, Yang, Schuurmans, Chi, and Dai] Shicong
Cen,
Jincheng Mei, Katayoon Goshvadi, Hanjun Dai, Tong Yang, Sherry Yang, Dale Schuurmans, Yuejie
Chi, and Bo Dai. Value-incentivized preference optimization: A unified approach to online and
offline RLHF. In International Conference on Learning Representations, 2025.
10

--- Page 11 ---

[Christiano et al.(2017)Christiano, Leike, Brown, Martic, Legg, and Amodei] Paul F Christiano, Jan
Leike, Tom Brown, Miljan Martic, Shane Legg, and Dario Amodei. Deep reinforcement learn-
ing from human preferences. In Advances in Neural Information Processing Systems, volume 30,
2017.
[Dai et al.(2024)Dai, Pan, Sun, Ji, Xu, Liu, Wang, and Yang] Josef Dai, Xuehai Pan, Ruiyang Sun, Ji-
aming Ji, Xinbo Xu, Mickel Liu, Yizhou Wang, and Yaodong Yang. Safe RLHF: Safe reinforcement
learning from human feedback. In International Conference on Learning Representations, 2024.
[Dubey et al.(2024)Dubey, Jauhri, Pandey, Kadian, Al-Dahle, Letman, Mathur, Schelten, Yang, Fan, et al.]
Abhimanyu Dubey, Abhinav Jauhri, Abhinav Pandey, Abhishek Kadian, Ahmad Al-Dahle, Aiesha
Letman, Akhil Mathur, Alan Schelten, Amy Yang, Angela Fan, et al. The LLaMA 3 herd of models.
arXiv e-prints, pp. arXiv–2407, 2024.
[Efroni et al.(2020)Efroni, Mannor, and Pirotta] Yonathan Efroni, Shie Mannor, and Matteo Pirotta.
Exploration-exploitation in constrained MDPs. arXiv preprint arXiv:2003.02189, 2020.
[Gehman et al.(2020)Gehman, Gururangan, Sap, Choi, and Smith] Samuel Gehman, Suchin Gururan-
gan, Maarten Sap, Yejin Choi, and Noah A Smith. Realtoxicityprompts: Evaluating neural toxic
degeneration in language models. arXiv preprint arXiv:2009.11462, 2020.
[Huang et al.(2024)Huang, Li, Dobriban, Bastani, Hassani, and Ding] Xinmeng Huang, Shuo Li, Edgar
Dobriban, Osbert Bastani, Hamed Hassani, and Dongsheng Ding. One-shot safety alignment for large
language models via optimal dualization. In Advances in Neural Information Processing Systems,
volume 37, pp. 84350–84383, 2024.
[Ji et al.(2024)Ji, Chen, Lou, Hong, Zhang, Pan, Qiu, Dai, and Yang] Jiaming Ji, Boyuan Chen, Hantao
Lou, Donghai Hong, Borong Zhang, Xuehai Pan, Tianyi Alex Qiu, Juntao Dai, and Yaodong Yang.
Aligner: Efficient alignment by learning to correct. In Advances in Neural Information Processing
Systems, volume 37, pp. 90853–90890, 2024.
[Kim et al.(2025)Kim, Jang, Kim, Kim, Lee, Bae, and Lee] Geon-Hyeong Kim, Youngsoo Jang, Yu Jin
Kim, Byoungjip Kim, Honglak Lee, Kyunghoon Bae, and Moontae Lee. SafeDPO: A simple approach
to direct preference optimization with enhanced safety. arXiv preprint arXiv:2505.20065, 2025.
[Li et al.(2023)Li, Zhang, Dubois, Taori, Gulrajani, Guestrin, Liang, and Hashimoto] Xuechen
Li,
Tianyi Zhang, Yann Dubois, Rohan Taori, Ishaan Gulrajani, Carlos Guestrin, Percy Liang, and
Tatsunori B Hashimoto. AlpacaEval: An automatic evaluator of instruction-following models, 2023.
[Lin et al.(2021)Lin, Hilton, and Evans] Stephanie Lin, Jacob Hilton, and Owain Evans. Truthfulqa:
Measuring how models mimic human falsehoods. arXiv preprint arXiv:2109.07958, 2021.
[Liu et al.(2024a)Liu, Lu, Zhang, Liu, Guo, Yang, Blanchet, and Wang] Zhihan Liu, Miao Lu, Shenao
Zhang, Boyi Liu, Hongyi Guo, Yingxiang Yang, Jose Blanchet, and Zhaoran Wang. Provably
mitigating overoptimization in RLHF: Your SFT loss is implicitly an adversarial regularizer. In
Advances in Neural Information Processing Systems, volume 37, pp. 138663–138697, 2024a.
[Liu et al.(2024b)Liu, Sun, and Zheng] Zixuan Liu, Xiaolin Sun, and Zizhan Zheng. Enhancing LLM
safety via constrained direct preference optimization. In International Conference on Learning
Representations Workshop, 2024b.
[Ouyang et al.(2022)Ouyang, Wu, Jiang, Almeida, Wainwright, Mishkin, Zhang, Agarwal, Slama, Ray, et al.]
Long Ouyang, Jeffrey Wu, Xu Jiang, Diogo Almeida, Carroll Wainwright, Pamela Mishkin, Chong
Zhang, Sandhini Agarwal, Katarina Slama, Alex Ray, et al. Training language models to follow
instructions with human feedback. In Advances in Neural Information Processing Systems, volume 35,
pp. 27730–27744, 2022.
[Peng et al.(2019)Peng, Kumar, Zhang, and Levine] Xue Bin Peng, Aviral Kumar, Grace Zhang, and
Sergey Levine. Advantage-weighted regression: Simple and scalable off-policy reinforcement learning.
arXiv preprint arXiv:1910.00177, 2019.
[Peters & Schaal(2007)Peters and Schaal] Jan Peters and Stefan Schaal.
Reinforcement learning by
reward-weighted regression for operational space control. In International Conference on Machine
Learning, pp. 745–750, 2007.
11

--- Page 12 ---

[Qi et al.(2025)Qi, Lyu, Yang, Wang, Bai, and Cui] Yupeng Qi, Ziyu Lyu, Min Yang, Yanlin Wang,
Lu Bai, and Lixin Cui. MidPO: Dual preference optimization for safety and helpfulness in large
language models via a mixture of experts framework. arXiv preprint arXiv:2506.02460, 2025.
[Rafailov et al.(2023)Rafailov, Sharma, Mitchell, Manning, Ermon, and Finn] Rafael Rafailov, Archit
Sharma, Eric Mitchell, Christopher D Manning, Stefano Ermon, and Chelsea Finn. Direct preference
optimization: Your language model is secretly a reward model. In Advances in Neural Information
Processing Systems, volume 36, pp. 53728–53741, 2023.
[Schulman et al.(2017)Schulman, Wolski, Dhariwal, Radford, and Klimov] John Schulman, Filip Wolski,
Prafulla Dhariwal, Alec Radford, and Oleg Klimov. Proximal policy optimization algorithms. arXiv
preprint arXiv:1707.06347, 2017.
[Taori et al.(2023)Taori, Gulrajani, Zhang, Dubois, Li, Guestrin, Liang, and Hashimoto] Rohan
Taori,
Ishaan Gulrajani, Tianyi Zhang, Yann Dubois, Xuechen Li, Carlos Guestrin, Percy Liang, and
Tatsunori B Hashimoto. Stanford alpaca: An instruction-following LLaMA model, 2023.
[Team et al.(2024a)Team, Mesnard, Hardin, Dadashi, Bhupatiraju, Pathak, Sifre, Rivi`ere, Kale, Love, et al.]
Gemma Team, Thomas Mesnard, Cassidy Hardin, Robert Dadashi, Surya Bhupatiraju, Shreya
Pathak, Laurent Sifre, Morgane Rivi`ere, Mihir Sanjay Kale, Juliette Love, et al. Gemma: Open
models based on gemini research and technology. arXiv preprint arXiv:2403.08295, 2024a.
[Team et al.(2024b)Team, Riviere, Pathak, Sessa, Hardin, Bhupatiraju, Hussenot, Mesnard, Shahriari, Ram´e, et al.]
Gemma Team, Morgane Riviere, Shreya Pathak, Pier Giuseppe Sessa, Cassidy Hardin, Surya
Bhupatiraju, L´eonard Hussenot, Thomas Mesnard, Bobak Shahriari, Alexandre Ram´e, et al. Gemma
2: Improving open language models at a practical size. arXiv preprint arXiv:2408.00118, 2024b.
[Team et al.(2025)Team, Kamath, Ferret, Pathak, Vieillard, Merhej, Perrin, Matejovicova, Ram´e, Rivi`ere, et al.]
Gemma Team, Aishwarya Kamath, Johan Ferret, Shreya Pathak, Nino Vieillard, Ramona Merhej,
Sarah Perrin, Tatiana Matejovicova, Alexandre Ram´e, Morgane Rivi`ere, et al. Gemma 3 technical
report. arXiv preprint arXiv:2503.19786, 2025.
[Touvron et al.(2023a)Touvron, Lavril, Izacard, Martinet, Lachaux, Lacroix, Rozi`ere, Goyal, Hambro, Azhar, et al.]
Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier Martinet, Marie-Anne Lachaux, Timoth´ee
Lacroix, Baptiste Rozi`ere, Naman Goyal, Eric Hambro, Faisal Azhar, et al. LLaMA: Open and
efficient foundation language models. arXiv preprint arXiv:2302.13971, 2023a.
[Touvron et al.(2023b)Touvron, Martin, Stone, Albert, Almahairi, Babaei, Bashlykov, Batra, Bhargava, Bhosale, et al.]
Hugo Touvron, Louis Martin, Kevin Stone, Peter Albert, Amjad Almahairi, Yasmine Babaei, Nikolay
Bashlykov, Soumya Batra, Prajjwal Bhargava, Shruti Bhosale, et al. LLaMA 2: Open foundation
and fine-tuned chat models. arXiv preprint arXiv:2307.09288, 2023b.
[Tropp et al.(2015)] Joel A Tropp et al. An introduction to matrix concentration inequalities. Foundations
and Trends® in Machine Learning, 8(1-2):1–230, 2015.
[Wachi et al.(2024)Wachi, Tran, Sato, Tanabe, and Akimoto] Akifumi Wachi, Thien Tran, Rei Sato,
Takumi Tanabe, and Youhei Akimoto. Stepwise alignment for constrained language model policy
optimization. In Advances in Neural Information Processing Systems, volume 37, pp. 104471–104520,
2024.
[Wei et al.(2023)Wei, Haghtalab, and Steinhardt] Alexander Wei, Nika Haghtalab, and Jacob Steinhardt.
Jailbroken: How does LLM safety training fail?
In Advances in Neural Information Processing
Systems, volume 36, pp. 80079–80110, 2023.
[Xie et al.(2025)Xie, Foster, Krishnamurthy, Rosset, Awadallah, and Rakhlin] Tengyang Xie, Dylan J
Foster, Akshay Krishnamurthy, Corby Rosset, Ahmed Awadallah, and Alexander Rakhlin. Ex-
ploratory preference optimization: Harnessing implicit Q∗-approximation for sample-efficient RLHF.
In International Conference on Learning Representations, 2025.
[Xu et al.(2024)Xu, Fu, Gao, Ye, Liu, Mei, Wang, Yu, and Wu] Shusheng Xu, Wei Fu, Jiaxuan Gao,
Wenjie Ye, Weilin Liu, Zhiyu Mei, Guangju Wang, Chao Yu, and Yi Wu. Is DPO superior to
PPO for LLM alignment? a comprehensive study. In International Conference on Machine Learning,
pp. 54983–54998, 2024.
12

--- Page 13 ---

[Yang et al.(2024)Yang, Liu, Xie, Huang, Zhang, and Ananiadou] Kailai Yang, Zhiwei Liu, Qianqian Xie,
Jimin Huang, Tianlin Zhang, and Sophia Ananiadou. Metaaligner: Towards generalizable multi-
objective alignment of language models. In Advances in Neural Information Processing Systems,
volume 37, pp. 34453–34486, 2024.
[Zhang et al.(2025)Zhang, Li, Hounie, Bastani, Ding, and Ribeiro] Botong Zhang, Shuo Li, Ignacio
Hounie, Osbert Bastani, Dongsheng Ding, and Alejandro Ribeiro. Alignment of large language
models with constrained learning. In International Conference on Machine Learning Workshop,
2025.
[Zhou et al.(2023)Zhou, Liu, Yang, Shao, Liu, Yue, Ouyang, and Qiao] Zhanhui Zhou, Jie Liu, Chao
Yang, Jing Shao, Yu Liu, Xiangyu Yue, Wanli Ouyang, and Yu Qiao. Beyond one-preference-
for-all: Multi-objective direct preference optimization. 2023.
[Zhu et al.(2023)Zhu, Jordan, and Jiao] Banghua Zhu, Michael Jordan, and Jiantao Jiao. Principled
reinforcement learning with human feedback from pairwise or k-wise comparisons. In International
Conference on Machine Learning, pp. 43037–43067. PMLR, 2023.
13

--- Page 14 ---

Appendix
A
A Full Review of Related Work
In this section, we give a more detailed review of related work.
With the extensive application of LLMs, the alignment of LLMs has received widespread attention in the
AI community, which aims to make LLMs align with human preference and values, and become more help-
ful and harmless. RLHF [Christiano et al.(2017)Christiano, Leike, Brown, Martic, Legg, and Amodei,
Ouyang et al.(2022)Ouyang, Wu, Jiang, Almeida, Wainwright, Mishkin, Zhang, Agarwal, Slama, Ray, et al.]
and DPO [Rafailov et al.(2023)Rafailov, Sharma, Mitchell, Manning, Ermon, and Finn] are two main al-
gorithmic frameworks for LLM alignment. RLHF first trains a reward model, and then applies RL
algorithms with the learned reward model to fine-tune LLMs. DPO directly fine-tune LLMs using
preference data, without explicitly training a reward model.
While LLMs have achieved a remarkable success, they may also generate harmful and fabricated con-
tent [Gehman et al.(2020)Gehman, Gururangan, Sap, Choi, and Smith, Lin et al.(2021)Lin, Hilton, and Evans,
Wei et al.(2023)Wei, Haghtalab, and Steinhardt].
Recently, there are several works studying safety
or constrained alignment of LLMs, e.g., [Dai et al.(2024)Dai, Pan, Sun, Ji, Xu, Liu, Wang, and Yang,
Liu et al.(2024b)Liu, Sun, and Zheng, Wachi et al.(2024)Wachi, Tran, Sato, Tanabe, and Akimoto, Huang et al.(2024)Hu
Zhang et al.(2025)Zhang, Li, Hounie, Bastani, Ding, and Ribeiro, Kim et al.(2025)Kim, Jang, Kim, Kim, Lee, Bae, and
[Dai et al.(2024)Dai, Pan, Sun, Ji, Xu, Liu, Wang, and Yang] proposed a safe RLHF framework, which
considers maximizing the reward while restricting the cost to be no larger than a threshold. Their approach
first trained a reward model and a cost model on reward and cost preference data, respectively, and then ap-
plied an RL algorithm, PPO [Schulman et al.(2017)Schulman, Wolski, Dhariwal, Radford, and Klimov],
to maximize the Lagrangian function constituted by the learned reward and cost functions. [Liu et al.(2024b)Liu, Sun, and Z
regenerated preference data according to the Bradley-Terry model [Bradley & Terry(1952)Bradley and Terry]
with the Lagrangian function using trained reward and cost models, and then performed the stan-
dard DPO algorithm [Rafailov et al.(2023)Rafailov, Sharma, Mitchell, Manning, Ermon, and Finn] on
these regenerated data. [Wachi et al.(2024)Wachi, Tran, Sato, Tanabe, and Akimoto] observed a rela-
tionship between the optimal solution of maximizing the Lagrangian function and that of maximiz-
ing the reward function, and then applied DPO combined with this observation. The algorithm in
[Wachi et al.(2024)Wachi, Tran, Sato, Tanabe, and Akimoto] requires prior knowledge of the optimal La-
grangian multiplier, and their theoretical results depend on the deviation between the used and optimal La-
grange multipliers, which can be unbounded. [Kim et al.(2025)Kim, Jang, Kim, Kim, Lee, Bae, and Lee]
reordered preference data if the preferred response (in terms of helpfulness) is unsafe and the dis-
preferred response is safe, and then ran DPO on these reordered data.
Their algorithm is ineffi-
cient in cost information learning. [Huang et al.(2024)Huang, Li, Dobriban, Bastani, Hassani, and Ding,
Zhang et al.(2025)Zhang, Li, Hounie, Bastani, Ding, and Ribeiro] first learned the optimal Lagrangian
multiplier, and then maximized the Lagrangian function under the learned optimal Lagrangian multiplier.
These two works also require trained reward and cost models.
There are also other works related to safety or constrained alignment of LLMs [Zhou et al.(2023)Zhou, Liu, Yang, Shao, L
Ji et al.(2024)Ji, Chen, Lou, Hong, Zhang, Pan, Qiu, Dai, and Yang, Yang et al.(2024)Yang, Liu, Xie, Huang, Zhang, an
Qi et al.(2025)Qi, Lyu, Yang, Wang, Bai, and Cui]. [Zhou et al.(2023)Zhou, Liu, Yang, Shao, Liu, Yue, Ouyang, and Qi
designed a multi-objective DPO approach. [Ji et al.(2024)Ji, Chen, Lou, Hong, Zhang, Pan, Qiu, Dai, and Yang,
Yang et al.(2024)Yang, Liu, Xie, Huang, Zhang, and Ananiadou] developed simple single-objective and
multi-objective alignment approaches, respectively, but their algorithms need corrected responses or a
multi-objective reward model. [Qi et al.(2025)Qi, Lyu, Yang, Wang, Bai, and Cui] proposed a mixture
of experts (MoE) framework for safety-helpfulness preference optimization.
Unlike prior works [Dai et al.(2024)Dai, Pan, Sun, Ji, Xu, Liu, Wang, and Yang, Liu et al.(2024b)Liu, Sun, and Zheng
Huang et al.(2024)Huang, Li, Dobriban, Bastani, Hassani, and Ding, Zhang et al.(2025)Zhang, Li, Hounie, Bastani, Ding
Zhou et al.(2023)Zhou, Liu, Yang, Shao, Liu, Yue, Ouyang, and Qiao, Yang et al.(2024)Yang, Liu, Xie, Huang, Zhang, a
Qi et al.(2025)Qi, Lyu, Yang, Wang, Bai, and Cui], our approach avoids training reward and cost models,
which significantly reduces memory and computational costs. In contrast to [Wachi et al.(2024)Wachi, Tran, Sato, Tanabe,
our approach does not need prior knowledge of the optimal Lagrangian multiplier. Moreover, most of
the above works do not provide theoretical guarantees for their algorithms. By contrast, we establish
rigorous suboptimality and constraint violation guarantees for the output policy of our algorithm, and
remove the dependence on preference data coverage in the results in the extended online data setting.
14

--- Page 15 ---

Table 1: Hyper-parameters of algorithm PD-DPO used in experiments.
Hyper-parameters
Algorithm PD-DPO
β
0.1
epochs
5
max length
512
per device train batch size
8
per device eval batch size
8
gradient accumulation steps
1
gradient checkpointing
True
lr
1e-6
lr scheduler type
cosine
lr warmup ratio
0.03
weight decay
0.05
bf16
True
tf32
True
B
More Experimental Details
In this section, we will describe more details of algorithm implementation and experimental setup. Our code
is written based on the released code of prior safe RLHF work [Dai et al.(2024)Dai, Pan, Sun, Ji, Xu, Liu, Wang, and Yang]
on their GitHub website, and we also open source our code in supplementary materials.
In algorithm implementation, we run our algorithm PD-DPO (Algorithm 1) without policy search con-
straints π ∈Πr in Line 1 and π ∈Πc
k in Line 3, since these two constraints are mainly used for guaranteeing
theoretical performance. In experiments, we set the Lagrange multiplier of algorithm PD-DPO as 5 to save
computational costs and time due to our limited computational resources. We find it works well in practice.
For algorithm SafeDPO [Kim et al.(2025)Kim, Jang, Kim, Kim, Lee, Bae, and Lee], to guarantee fair com-
parison, we run it on the SFT model Alpaca-7b-reproduced, without performing additional supervised fine-
tuning on pairwise preference data as described in [Kim et al.(2025)Kim, Jang, Kim, Kim, Lee, Bae, and Lee].
In evaluation, we directly access the released models Alpaca-7b-reproduced and Beaver-v3.0 [Dai et al.(2024)Dai, Pan, Sun
via their Hugging Face websites.
The hyper-parameters of our algorithm used in experiments are presented in Table 1. For GPT-4 evalua-
tion, we use the same prompts as in Appendix C.2 in prior safe RLHF work [Dai et al.(2024)Dai, Pan, Sun, Ji, Xu, Liu, Wan
For the helpfulness measurement in GPT-4 evaluation, we use the helpfulness-based questions from the Al-
pacaEval dataset [Li et al.(2023)Li, Zhang, Dubois, Taori, Gulrajani, Guestrin, Liang, and Hashimoto].
It is because as reported in the literature, e.g., [Wachi et al.(2024)Wachi, Tran, Sato, Tanabe, and Akimoto],
GPT-4 tends to rate higher helpfulness scores for safer models, and thus using helpfulness-based questions
rather than safety-sensitive questions in the PKU-SafeRLHF dataset [Dai et al.(2024)Dai, Pan, Sun, Ji, Xu, Liu, Wang, and
is more accurate for evaluating the helpfulness of models.
C
Proofs for Algorithm PD-DPO
In this section, we present the proofs for algorithm PD-DPO, including the proofs for the connection to the
RLHF-based procedure, suboptimality, and constraint violation.
We note that our proofs for the connection between our DPO-based procedure and the RLHF-based pro-
cedure (Theorems 3, 4, 5 and 6) follow the analysis of Proposition 4 in [Azar et al.(2024)Azar, Guo, Piot, Munos, Rowland,
We extend their analysis to the setting with constrained policy search ranges and a Lagrangian objective.
C.1
Connection between Our DPO-based Procedure and the RLHF-based
Procedure
We first give a result which builds a bridge between standard DPO and standard RLHF with constrained
policy search ranges.
Let R := [−Rmax, Rmax] and C := [−Cmax, Cmax]. Define the following problem which first learns a
15

--- Page 16 ---

reward model and then finds the optimal policy to maximize the learned reward function:
ˆr ←min
r∈R −1
N r
N r
X
i=1
log σ
 r(xi, yrw
i ) −r(xi, yrℓ
i )

(19)
max
π
Ex∼Dp 
Ey∼π(·|x) [ˆr(x, y)] −β · KL(π(·|x)∥πref(·|x))

(20)
Theorem 3 (Connection between Standard DPO and Standard RLHF with Constrained Policy Ranges).
Problems Eqs. (15) and (20) have the same set of optimal solutions.
Proof. Step (i). First, we prove that if π is an optimal solution to Eq. (20), then π is also an optimal
solution to Eq. (15).
If ˆr ∈R is an optimal solution to Eq. (19), then π∗
ˆr ∈Πr (as defined in Eq. (4)) is an optimal solution
to Eq. (20). We have that π∗
ˆr is also an optimal solution to Eq. (15). Otherwise, there exists another
π′ ∈Πr which achieves a smaller objective value in Eq. (15). Then, there must exist a r′ ∈R which
satisfies that
π′(y|x) =
πref(y|x) · exp

1
β r′(x, y)

X
y′∈Y
πref(y′|x) · exp
 1
β r′(x, y′)

|
{z
}
:=Zr′(x)
,
i.e.,
r′(x, y) = β log π′(y|x)
πref(y|x) + β log Zr′(x),
and the objective value in Eq. (19) achieved by r′,
−1
N r
Nr
X
i=1
log σ
 
β log π′(yrw
i |xi)
πref(yrw
i |xi) + β log Zr′(xi) −

β log π′(yrℓ
i |xi)
πref(yrℓ
i |xi) + β log Zr′(xi)
 !
,
is smaller than that achieved by ˆr, which contradicts the supposition that ˆr is the optimal solution to
Eq. (19).
Step (ii).
Next, we prove that if π is an optimal solution to Eq. (15), then π is also an optimal solution
to Eq. (20).
If ˜π ∈Πr is an optimal solution to Eq. (15), then there exists a ˜r ∈R which satisfies
˜π(y|x) =
πref(y|x) · exp

1
β ˜r(x, y)

P
y′∈Y πref(y′|x) · exp

1
β ˜r(x, y′)
,
i.e.,
˜r(x, y) = β log
˜π(y|x)
πref(y|x) + β log Z˜r(x).
We have that ˜r achieves the optimal value in Eq. (19),
−1
N r
Nr
X
i=1
log σ
 
β log
˜π(yrw
i |xi)
πref(yrw
i |xi) +β log Z˜r(xi)−

β log
˜π(yrℓ
i |xi)
πref(yrℓ
i |xi) +β log Z˜r(xi)
 !
.
(21)
Otherwise, there exists another r′ ∈R and then there exists a π′ = π∗
ˆr ∈Πr which gives a smaller
objective value than ˜π in Eq. (21). Thus, ˜r achieves the optimal value in Eq. (19). Then, the optimal
solution to Eq. (20) under cost model ˜r is
π(y|x) ∝πref(y|x) · exp
 1
β ˜r(x, y)

16

--- Page 17 ---

(a)
∝πref(y|x) · exp
 1
β

β log
˜π(y|x)
πref(y|x) + β log Z˜r(x)

∝πref(y|x) · exp

log
˜π(y|x)
πref(y|x)

= ˜π(y|x),
where (a) uses Eq. (5).
Therefore, ˜π is also an optimal solution to Eq. (20).
In the following, we provide a result which builds a connection between our rearranged Lagrangian
DPO objective and the safe RLHF objective.
Theorem 4 (Connection between Our Rearranged Lagrangian DPO and Safe RLHF). For any k ≥0,
problem Eq. (16) and the following problem
ˆc ←
min
c∈[−Cmax,Cmax] −1
N c
N c
X
i=1
log σ
 c(xc
i, ycw
i ) −c(xc
i, ycℓ
i )

,
(22)
max
π
Ex∼Dp 
Ey∼π(·|x) [ˆr(x, y) −λk · ˆc(x, y)] −β · KL(π(·|x)∥πref(·|x))

.
(23)
have the same set of optimal solutions.
Theorem 4 demonstrates that our rearranged Lagrangian DPO objective is an effective and alternative
way to learn the optimal policy of maximizing the Lagrangian function, while enjoying the advantage of
memory and computational efficiency.
Proof of Theorem 4. First, note that for any ˆc, the optimal solution to Eq. (23) is
π∗
ˆr−λkˆc(y|x) =
πref(y|x) · exp

1
β (ˆr(x, y) −λk · ˆc(x, y))

X
y′∈Y
πref(y′|x) · exp
 1
β (ˆr(x, y′) −λk · ˆc(x, y′))

|
{z
}
:=Zˆr−λk ˆc(x)
, ∀x ∈X.
(24)
Then, we have
ˆc(x, y) = 1
λk

ˆr(x, y) −β log π∗
ˆr−λkˆc(y|x)
πref(y|x)
−β log Zˆr−λkˆc(x)

(a)
=
1
λk

β log π∗
ˆr(y|x)
πref(y|x) + β log Zˆr(x) −β log π∗
ˆr−λkˆc(y|x)
πref(y|x)
−β log Zˆr−λkˆc(x)

,
where equality (a) uses Eq. (5).
The proof consists of two steps.
Step (i). First, we prove that if π is an optimal solution to Eq. (23), then π is also an optimal
solution to Eq. (16).
If ˆc ∈C is an optimal solution to Eq. (22), then π∗
ˆr−λkˆc ∈Πc
k (as shown in Eq. (24)) is an optimal
solution to Eq. (23). We have that π∗
ˆr−λkˆc is also an optimal solution to Eq. (16). Otherwise, there exists
another π′ ∈Πc
k which achieves a smaller objective value in Eq. (16). Then, there must exist a c′ ∈C
which satisfies that
π′(y|x) =
πref(y|x) · exp

1
β

β log π∗
ˆr (y|x)
πref(y|x) −λk · c′(x, y)

X
y′∈Y
πref(y′|x) · exp
 1
β

β log π∗
ˆr(y|x)
πref(y|x) −λk · c′(x, y′)

|
{z
}
:=Z
β log
π∗
ˆr
πref
−λkc′(x)
,
i.e.,
c′(x, y) = 1
λk

β log π∗
ˆr(y|x)
πref(y|x) −β log π′(y|x)
πref(y|x) −β log Zβ log
π∗
ˆr
πref −λkc′(x)

,
17

--- Page 18 ---

and the objective value in Eq. (22) achieved by c′,
−1
N c
Nc
X
i=1
log σ
 
1
λk

β log π∗
ˆr(ycw
i |xi)
πref(ycw
i |xi) −β log π′(ycw
i |xi)
πref(ycw
i |xi) −β log Zβ log
π∗
ˆr
πref −λkc′(xi)

−1
λk

β log π∗
ˆr(ycℓ
i |xi)
πref(ycℓ
i |xi) −β log π′(ycℓ
i |xi)
πref(ycℓ
i |xi) −β log Zβ log
π∗
ˆr
πref −λkc′(xi)
 !
,
is smaller than that achieved by ˆc, which contradicts the supposition that ˆc is the optimal solution to
Eq. (22).
Step (ii). Next, we prove that if π is an optimal solution to Eq. (16), then π is also an optimal
solution to Eq. (23).
If πk ∈Πc
k is an optimal solution to Eq. (16), then there exists a ck ∈C which satisfies
πk(y|x) =
πref(y|x) · exp

1
β

β log π∗
ˆr (y|x)
πref(y|x) −λk · ck(x, y)

P
y′∈Y πref(y′|x) · exp

1
β

β log π∗
ˆr (y′|x)
πref(y′|x) −λk · ck(x, y′)
,
i.e.,
ck(x, y) = 1
λk

β log π∗
ˆr(y|x)
πref(y|x) −β log πk(y|x)
πref(y|x) −β log Zβ log
π∗
ˆr
πref −λkck(x)

.
We have that ck achieves the optimal value in Eq. (22),
−1
N c
Nc
X
i=1
log σ
 
1
λk

β log π∗
ˆr(ycw
i |xi)
πref(ycw
i |xi) −β log πk(ycw
i |xi)
πref(ycw
i |xi) −β log Zβ log
π∗
ˆr
πref −λkck(xi)

−1
λk

β log π∗
ˆr(ycℓ
i |xi)
πref(ycℓ
i |xi) −β log πk(ycℓ
i |xi)
πref(ycℓ
i |xi) −β log Zβ log
π∗
ˆr
πref −λkck(xi)
 !
.
(25)
Otherwise, there exists another c′ ∈C and then there exists a π′ = π∗
ˆr−λkc′ ∈Πc
k which gives a smaller
objective value than πk in Eq. (25). Thus, ck achieves the optimal value in Eq. (22). Then, the optimal
solution to Eq. (22) under cost model ck is
π(y|x) ∝πref(y|x) · exp
 
1
β

ˆr(x, y) −β log π∗
ˆr(y|x)
πref(y|x) + β log πk(y|x)
πref(y|x)
+ β log Zβ log
π∗
ˆr
πref −λkck(x)
!
(a)
∝πref(y|x) · exp
 1
β

β log Zˆr(x) + β log πk(y|x)
πref(y|x) + β log Zβ log
π∗
ˆr
πref −λkck(x)

∝πref(y|x) · exp
 1
β

β log πk(y|x)
πref(y|x)

= πk(y|x),
where (a) uses Eq. (5).
Therefore, πk is also an optimal solution to Eq. (23).
C.2
Cost Estimation for Lagrangian Multiplier Update
In the following, we bound the estimation error between ˜ck and Ex∼Dp,y∼πk(·|x)[c∗(x, y)] in Line 4 of
Algorithm PD-DPO.
Let δ′ := δ
4. Define events
E :=







 ¯Zi −σ(c∗(xi, yi))
 ≤
v
u
u
tlog

2|X||Y|N CEK
δ′

M CE
, ∀i ∈[N CE], ∀k ∈[K]







,
(26)
18

--- Page 19 ---

F :=




1
N CE
NCE
X
i=1
c∗(xi, yi) −Ex∼Dp,y∼πk(·|x) [c∗(x, y)]

≤Cmax
s
log
  2K
δ′

N CE
, ∀k ∈[K]


.
(27)
Lemma 1. It holds that
Pr [E] ≥1 −δ′,
Pr [F] ≥1 −δ′.
Proof. Using Hoeffding’s inequality, for any i ∈[N CE], for any fixed (xi, yi) = (x, y) ∈X × Y, we have
that with probability at least 1 −˜δ,
 ¯Zi −σ(c∗(xi, yi))
 ≤
v
u
u
tlog

2
˜δ

M CE .
Taking a union bound over (x, y) ∈X × Y, i ∈[NCE] and k ∈[K], we can obtain the first statement.
Combining the fact that c∗(x, y) ∈[−Cmax, Cmax] for any (x, y) ∈X × Y, Hoeffding’s inequality, and
a union bound over k ∈[K], we can obtain the second statement.
Lemma 2. Assume that event E ∩F holds. Then, we have
˜ck −Ex∼Dp,y∼πk(·|x)[c∗(x, y)]
 ≤Cmax
s
log
  2K
δ′

N CE
+ W
v
u
u
tlog

2|X||Y|N CEK
δ′

M CE
,
where
W :=
1
 
1
1+exp(−Cmax) +
r
log

2|X||Y|NCEK
δ′

M CE
!  
exp(−Cmax)
1+exp(−Cmax) −
r
log

2|X||Y|NCEK
δ′

M CE
!
(28)
and δ′ := δ
4.
Proof. For any i ∈[N CE], we have
 ¯Zi −σ(c∗(xi, yi))
 ≤
v
u
u
tlog

2|X||Y|N CEK
δ′

M CE
.
Since c∗(x, y) ∈[−Cmax, Cmax] for any (x, y) ∈X × Y, we have
σ(−Cmax) −
v
u
u
tlog

2|X||Y|N CEK
δ′

M CE
≤¯Zi ≤σ(Cmax) +
v
u
u
tlog

2|X||Y|N CEK
δ′

M CE
.
The derivative of σ−1(z) is (σ−1)′(z) =
1
z(1−z). For any z lying between ¯Zi and σ(c∗(xi, yi)), we have
(σ−1)′(z)≤
1
 
1
1+exp(−Cmax) +
r
log

2|X||Y|NCEK
δ′

M CE
! 
exp(−Cmax)
1+exp(−Cmax) −
r
log

2|X||Y|NCEK
δ′

M CE
! :=W.
According to the Lagrange’s Mean Value Theorem, we have
σ−1( ¯Zi) −c∗(xi, yi)
 =
σ−1( ¯Zi) −σ−1(σ(c∗(xi, yi)))

≤W
 ¯Zi −σ(c∗(xi, yi))

≤W
v
u
u
tlog

2|X||Y|N CEK
δ′

M CE
.
19

--- Page 20 ---

Hence, we have
c∗(xi, yi) −W
v
u
u
tlog

2|X||Y|N CEK
δ′

M CE
≤σ−1( ¯Zi) ≤c∗(xi, yi) + W
v
u
u
tlog

2|X||Y|N CEK
δ′

M CE
.
Since the above argument holds for any i ∈[NCE], we have
1
N CE
NCE
X
i=1
c∗(xi, yi) −W
v
u
u
tlog

2|X||Y|N CEK
δ′

M CE
≤
1
N CE
NCE
X
i=1
σ−1( ¯Zi)
≤
1
N CE
NCE
X
i=1
c∗(xi, yi) + W
v
u
u
tlog

2|X||Y|N CEK
δ′

M CE
.
Combining with the definition of event F, we have
Ex∼Dp,y∼πk(·|x) [c∗(x, y)] −Cmax
s
log
  2K
δ′

N CE
−W
v
u
u
tlog

2|X||Y|N CEK
δ′

M CE
≤
1
N CE
NCE
X
i=1
σ−1( ¯Zi) ≤
Ex∼Dp,y∼πk(·|x) [c∗(x, y)] + Cmax
s
log
  2K
δ′

N CE
+ W
v
u
u
tlog

2|X||Y|N CEK
δ′

M CE
.
C.3
Suboptimality and Constraint Violation
Now we give the proof of the suboptimality and constraint violation guarantees for Algorithm PD-DPO
(Theorem 1).
Recall that for any (x, y) ∈X × Y, ϕ(x, y) denotes a |X||Y|-dimensional vector where the entry
corresponding to (x, y) is 1 and all other entries are 0. In addition, let
ΣDr :=
Nr
X
i=1
 ϕ(xr
i , yrw
i ) −ϕ(xr
i , yrℓ
i )
  ϕ(xr
i , yrw
i ) −ϕ(xr
i , yrℓ
i )
⊤,
ΣDc :=
Nc
X
i=1
 ϕ(xc
i, ycw
i ) −ϕ(xc
i, ycℓ
i )
  ϕ(xc
i, ycw
i ) −ϕ(xc
i, ycℓ
i )
⊤.
Define event
G :=
(
|ˆr(x, y) −r∗(x, y)| ≤4 ∥ϕ(x, y)∥(ΣDr +γI)−1 ·
s
(exp (Rmax) + exp (−Rmax) + 2)2

|X||Y| + log
 2
δ′

+ γ(Rmax)2,
|ˆc(x, y) −c∗(x, y)| ≤4 ∥ϕ(x, y)∥(ΣDc+γI)−1 ·
s
(exp (Cmax) + exp (−Cmax) + 2)2

|X||Y| + log
 2
δ′

+ γ(Cmax)2,
∀(x, y) ∈X × Y
)
.
Lemma 3 (MLE Guarantee, Lemma 3.1 in [Zhu et al.(2023)Zhu, Jordan, and Jiao]). It holds that
Pr [G] ≥1 −2δ′.
20

--- Page 21 ---

Lemma 4. For any k ≥1, we have
f(π∗; ˆr) −f(πk; ˆr)≤−λk · Ex∼Dp,y∼πk(·|x)[ˆc(x, y)] + λk
 Ex∼Dp,y∼π∗(·|x)[ˆc(x, y) −c∗(x, y)]

.
Proof. It holds that
f(π∗; ˆr)
(a)
≤f(π∗; ˆr) −λk · Ex∼Dp,y∼π∗(·|x)[c∗(x, y)]
= Ex∼Dp 
Ey∼π∗(·|x) [ˆr(x, y) −λk · ˆc(x, y)] −β · KL(π∗(·|x)∥πref(·|x))

+ λk · Ex∼Dp,y∼π∗(·|x)[ˆc(x, y)] −λk · Ex∼Dp,y∼π∗(·|x)[c∗(x, y)]
(b)
≤Ex∼Dp 
Ey∼πk(·|x) [ˆr(x, y) −λk · ˆc(x, y)] −β · KL(πk(·|x)∥πref(·|x))

+ λk · Ex∼Dp,y∼π∗(·|x)[ˆc(x, y)] −λk · Ex∼Dp,y∼π∗(·|x)[c∗(x, y)]
= f(πk; ˆr) −λk · Ex∼Dp,y∼πk(·|x)[ˆc(x, y)] + λk
 Ex∼Dp,y∼π∗(·|x)[ˆc(x, y) −c∗(x, y)]

,
where inequality (a) uses the fact that λk ≥0 and π∗is feasible, and inequality (b) comes from the
definition of πk and Theorem 4.
Now we prove Theorem 1.
Proof of Theorem 1. Recall that δ′ := δ
4. Then, according to Lemmas 1 and 3, we have Pr[E∩F∩G] ≥1−δ.
Hence, it suffices to prove this theorem assuming that event E ∩F ∩G holds. In the following proof, we
assume that event E ∩F ∩G holds.
For any k ≥1 and ¯λ ∈[0, 2ρ], we have
 λk+1 −¯λ
2 =

Proj[0,2ρ] (λk + ηk˜ck) −Proj[0,2ρ]
 ¯λ
2
(a)
≤
 λk + ηk˜ck −¯λ
2
=
 λk −¯λ
2 + 2ηk˜ck
 λk −¯λ

+ (ηk)2 (˜ck)2 ,
where inequality (a) uses the nonexpansivity of the projection to [0, 2ρ].
Summing the above inequality over k = 1, . . . , K, we have
0 ≤
 λK+1 −¯λ
2 ≤
 λ1 −¯λ
2 +
K
X
k=1
2ηk · Ex∼Dp,y∼πk(·|x)[c∗(x, y)] ·
 λk −¯λ

−
K
X
k=1
2ηk · Ex∼Dp,y∼πk(·|x)[c∗(x, y)] ·
 λk −¯λ

+
K
X
k=1
2ηk˜ck
 λk −¯λ

+
K
X
k=1
(ηk)2 (˜ck)2 .
Hence, we have
K
X
k=1
2ηk · Ex∼Dp,y∼πk(·|x)[c∗(x, y)] · ¯λ −
K
X
k=1
2ηk · Ex∼Dp,y∼πk(·|x)[ˆc(x, y)] · λk
≤
 λ1 −¯λ
2 +
K
X
k=1
2ηkλk · Ex∼Dp,y∼πk(·|x)[c∗(x, y) −ˆc(x, y)]
+
K
X
k=1
2ηk
 λk −¯λ
  ˜ck −Ex∼Dp,y∼πk(·|x)[c∗(x, y)]

+
K
X
k=1
(ηk)2 (˜ck)2 .
Using Lemma 4, we have
K
X
k=1
2ηk

Ex∼Dp,y∼πk(·|x)[c∗(x, y)] · ¯λ + f(π∗; ˆr) −f(πk; ˆr)
−λk · Ex∼Dp,y∼π∗(·|x)[ˆc(x, y) −c∗(x, y)]

≤
 λ1 −¯λ
2 +
K
X
k=1
(ηk)2 (˜ck)2 +
K
X
k=1
2ηkλk · Ex∼Dp,y∼πk(·|x)[c∗(x, y) −ˆc(x, y)]
21

--- Page 22 ---

+
K
X
k=1
2ηk
 λk −¯λ
  ˜ck −Ex∼Dp,y∼πk(·|x)[c∗(x, y)]

.
Recall that ηk = η. Then, we have
K
X
k=1
(f(π∗) −f(πk)) + ¯λ
K
X
k=1
Ex∼Dp,y∼πk(·|x)[c∗(x, y)]
≤1
2η
 λ1 −¯λ
2 + η
2
K
X
k=1
(˜ck)2 +
K
X
k=1
λk · Ex∼Dp,y∼πk(·|x)[c∗(x, y) −ˆc(x, y)]
+
K
X
k=1
 λk −¯λ
  ˜ck −Ex∼Dp,y∼πk(·|x)[c∗(x, y)]

+
K
X
k=1
λk · Ex∼Dp,y∼π∗(·|x)[ˆc(x, y) −c∗(x, y)]
+
K
X
k=1
(f(π∗) −f(π∗; ˆr)) −
K
X
k=1
(f(πk) −f(πk; ˆr))
≤1
2η
 λ1 −¯λ
2 + η(Cmax)2K
2
+
K
X
k=1
λk · Ex∼Dp,y∼πk(·|x)[c∗(x, y) −ˆc(x, y)]
+
K
X
k=1
 λk −¯λ
  ˜ck −Ex∼Dp,y∼πk(·|x)[c∗(x, y)]

+
K
X
k=1
λk · Ex∼Dp,y∼π∗(·|x)[ˆc(x, y) −c∗(x, y)]
+ K · Ex∼Dp,y∼π∗(·|x)[r∗(x, y) −ˆr(x, y)] −
K
X
k=1
Ex∼Dp,y∼πk(·|x)[r∗(x, y) −ˆr(x, y)].
Let ¯λ = 0. Recall that πout
K
is the uniform policy over π1, . . . , πK and η :=
λ1
Cmax
√
K . Then, we have
f(π∗) −f(πout
K )
= 1
K
K
X
k=1
(f(π∗) −f(πk))
= O
 
λ1Cmax
√
K
+ ρCmax
s
log
  1
δ

N CE
+ ρW
v
u
u
tlog

|X||Y|N CE
δ

M CE
+ρ
 
Ex∼Dp,y∼π∗(·|x)
h
∥ϕ(x, y)∥(ΣDc+γI)−1
i
+ 1
K
K
X
k=1
Ex∼Dp,y∼πk(·|x)
h
∥ϕ(x, y)∥(ΣDc+γI)−1
i!
·
s
(exp (Cmax) + exp (−Cmax) + 2)2

|X||Y| + log
1
δ

+ γ(Cmax)2
+
 
Ex∼Dp,y∼π∗(·|x)
h
∥ϕ(x, y)∥(ΣDr +γI)−1
i
+ 1
K
K
X
k=1
Ex∼Dp,y∼πk(·|x)
h
∥ϕ(x, y)∥(ΣDr +γI)−1
i!
·
s
(exp (Rmax) + exp (−Rmax) + 2)2

|X||Y| + log
1
δ

+ γ(Rmax)2
!
.
Let ¯λ = 2ρ. Then, we have
f(π∗) −f(πout
K ) + 2ρEx∼Dp,y∼πout
K (·|x)[c∗(x, y)]
= 1
K
K
X
k=1
(f(π∗) −f(πk)) + 2ρ
K
K
X
k=1
Ex∼Dp,y∼πk(·|x)[c∗(x, y)].
22

--- Page 23 ---

If
1
K
PK
k=1 Ex∼Dp,y∼πk(·|x)[c∗(x, y)] ≤0, the second statement of the theorem naturally holds; Other-
wise, we can replace the term 2ρEx∼Dp,y∼πout
K (·|x)[c∗(x, y)] by 2ρ[Ex∼Dp,y∼πout
K (·|x)[c∗(x, y)]]+ in the above
inequality. Then, using Corollary 1 and Lemma 10, we obtain
Ex∼Dp,y∼πout
K (·|x)[c∗(x, y)]
= O
 
Cmax
ρ
√
K
 
(λ1 −2ρ)2
λ1
+ λ1
!
+ Cmax
s
log
  1
δ

N CE
+ W
v
u
u
tlog

|X||Y|N CE
δ

M CE
+
 
Ex∼Dp,y∼π∗(·|x)
h
∥ϕ(x, y)∥(ΣDc+γI)−1
i
+ 1
K
K
X
k=1
Ex∼Dp,y∼πk(·|x)
h
∥ϕ(x, y)∥(ΣDc+γI)−1
i!
·
s
(exp (Cmax) + exp (−Cmax) + 2)2

|X||Y| + log
1
δ

+ γ(Cmax)2
+ 1
ρ
 
Ex∼Dp,y∼π∗(·|x)
h
∥ϕ(x, y)∥(ΣDr +γI)−1
i
+ 1
K
K
X
k=1
Ex∼Dp,y∼πk(·|x)
h
∥ϕ(x, y)∥(ΣDr +γI)−1
i!
·
s
(exp (Rmax) + exp (−Rmax) + 2)2

|X||Y| + log
1
δ

+ γ(Rmax)2
!
.
D
Pseudo-code and Detailed Description of Algorithm O-PD-DPO
In this section, we present the pseudo-code and a more detailed description of algorithm O-PD-DPO.
Algorithm 2 illustrates the algorithm procedure of O-PD-DPO. Compared to algorithm PD-DPO, O-PD-DPO
includes exploration bonuses bc
k(x, y) and br
k(x, y) in the standard DPO and standard rearranged La-
grangian DPO training objectives (Lines 3 and 4). We define the exploration bonuses b⋄
k(x, y) as
b⋄
k(x, y) := 4 ∥ϕ(x, y)∥(˜ΣD⋄
k +γonI)−1
s
(exp (z) + exp (−z) + 2)2
N on

|X||Y|+log
 2
δ′

+γonz2,
where
˜ΣD⋄
k :=
1
N on
X
(x,y,y′)∈D⋄
1
(ϕ(x, y) −ϕ(x, y′)) (ϕ(x, y) −ϕ(x, y′))⊤
+
1
N on
K
X
k=1
Non
X
i=1
 ϕ(xk,i, yk,i) −ϕ(xk,i, y′
k,i)
  ϕ(xk,i, yk,i) −ϕ(xk,i, y′
k,i)
⊤
with z = Rmax when ⋄= r, and z = Cmax when ⋄= c.
We take br
k(x, yrw) in Eq. (29) as an example to explain the intuition behind why including exploration
bonuses b⋄
k effectively encourages exploration: When preference data do not cover (x, yrw) well, br(x, yrw)
will be large. Then, subtracting a large value from β log
π(yrw|x)
πref(yrw|x) encourages π to put a higher probability
on yrw to maintain the original value of β log
π(yrw|x)
πref(yrw|x) which achieves the optimal value of the MLE
training objective. By incorporating exploration bonuses in the training objective, the trained model πk
has incentive to explore uncovered prompt-response space.
In addition, the constrained policy search ranges in Lines 3 and 4 also incorporate exploration bonuses,
which are defined as
˜Πr
k :=


π(y|x) =
πref(y|x) · exp

1
β (r(x, y) + br
k(x, y))

P
y′∈Y πref(y′|x) · exp

1
β (r(x, y′) + br
k(x, y′))
 : r ∈R


,
(31)
and
˜Πc
k :=
(
π(y|x)=
πref(y|x) · exp

1
β

β log
π∗
ˆrk+br
k (y|x)
πref(y|x)
−λk (c(x, y) −bc
k(x, y))

P
y′∈Y πref(y′|x) · exp

1
β

β log
π∗
ˆrk+br
k (y′|x)
πref(y′|x)
−λk (c(x, y′) −bc
k(x, y′))
 :
23

--- Page 24 ---

Algorithm 2: O-PD-DPO
Input: δ, δ′ := δ
4, β, πref, ρ, λ1, K, N CE, M CE, γon, N on := 32K2 ln( 8K|X||Y|
δ′
)/(γon)2, Dp,
Dr = {(xr
i , yrw
i , yrℓ
i )}i∈[N r], Dc = {(xc
i, ycw
i , ycℓ
i )}i∈[N c]
1 Dr
1 ←Dr, Dc
1 ←Dc
2 for k = 1, 2, . . . , K do
3
Train a model using standard DPO with exploration bonuses:
π∗
ˆr+br ←argmin
π∈˜Πr
k
−
X
(x,yrw,yrℓ)∈Dr
log σ
 
β log π(yrw|x)
πref(yrw|x) −br(x, yrw)
−

β log π(yrℓ|x)
πref(yrℓ|x) −br(x, yrℓ)
 !
,
(29)
where ˜Πr
k is defined in Eq. (31)
4
Train a model using a rearranged Lagrangian DPO objective with exploration bonuses:
πk ←argmin
π∈˜Πc
k
−
X
(x,ycw,ycℓ)∈Dc
log σ
 
1
λk

β log
π∗
ˆrk+br
k(ycw|x)
πref(ycw|x)
−β log π(ycw|x)
πref(ycw|x)
−bc
k(x, ycw) −

β log
π∗
ˆrk+br
k(ycℓ|x)
πref(ycℓ|x)
−β log π(ycℓ|x)
πref(ycℓ|x) −bc
k(x, ycℓ)
!
,
(30)
where ˜Πc
k is defined in Eq. (32)
5
Construct an estimate ˜ck for Ex∼Dp,y∼πk(·|x)[c∗(x, y)]: For i = 1, . . . , NCE, first sample
xi ∼Dp, yi ∼πk(·|xi). Then, for each (xi, yi), sample {Zi,j}M CE
j=1
i.i.d.
∼Ber(σ(c∗(xi, yi))). Set
˜ck ←
1
NCE
PN CE
i=1 σ−1(
1
M CE
PM CE
j=1 Zi,j), where σ−1(z) := log(
1
1−z −1) is the inverse of the
sigmoid function
6
λk+1 ←Proj[0,2ρ](λk + η˜ck), where η :=
λ1
Cmax
√
K
7
For i = 1, . . . , N on, sample xi ∼Dp, yi ∼πk(·|xi), y′
i ∼πbase(·|xi). Collect reward and cost
preference feedback on {(xi, yi, y′
i)}Non
i=1 , and obtain preference data {(xi, yrw
i , yrℓ
i )}N on
i=1 and
{(xi, ycw
i , ycℓ
i )}N on
i=1
8
Dr
k+1 ←Dr
k ∪{(xi, yrw
i , yrℓ
i )}N on
i=1 , Dc
k+1 ←Dc
k ∪{(xi, ycw
i , ycℓ
i )}Non
i=1
9 return πout
K
:= unif(π1, . . . , πK)
c ∈C
)
=
(
π(y|x)=
πref(y|x) · exp

1
β (ˆrk(x, y) + br
k(x, y) −λk (c(x, y) −bc
k(x, y)))

P
y′∈Y πref(y′|x) · exp

1
β (ˆrk(x, y′) + br
k(x, y′) −λk (c(x, y′) −bc
k(x, y′)))
 :
c ∈C
)
.
(32)
At the end of each iteration, O-PD-DPO collects reward and cost preference feedback using πk and a
baseline policy πbase (Line 7). The baseline policy πbase is a fixed policy used in online preference data
collection for ease of comparison. We make a technical assumption on πbase:
Assumption 2 (Baseline Policy). The baseline policy πbase satisfies that for any policy π,
Ex∼Dp,y∼π,y′∼πbase
h
(ϕ(x, y) −ϕ(x, y′)) (ϕ(x, y) −ϕ(x, y′))⊤i
(33)
⪰Cbase Ex∼Dp,y′∼πbase

ϕ(x, y′)ϕ(x, y′)⊤
.
(34)
This assumption is used to guarantee that the difference of feature vectors between any policy π and
πbase can be connected to the feature vectors of πbase itself, which is useful in analysis when bounding
the error due to inferring reward and cost information from preference data.
24

--- Page 25 ---

After collecting online preference data, O-PD-DPO adds these data to Dr
k and Dc
k, which will be used in
model training in the next iteration (Line 8). As the algorithm proceeds, the preference data Dr
k and Dc
k
will cover more and more prompt-response space.
E
Proofs for Algorithm O-PD-DPO
In this section, we provide the proofs for algorithm O-PD-DPO in the online data setting, including the
proofs for the connection to the RLHF-based procedure, suboptimality, and constraint violation.
E.1
Connection between our DPO-based Procedure and the RLHF-based
Procedure with Exploration Bonuses
First, we give a result which establishes a connection between standard DPO and standard RLHF with
constrained policy search ranges and exploration bonuses.
Define the following problem which first learns a reward model and then finds the optimal policy to
maximize the learned reward with exploration bonuses:
ˆrk ←min
r∈R −
X
(x,yrw,yrℓ)∈Dr
k
log σ
 r(x, yrw) −r(x, yrℓ)

(35)
max
π
Ex∼Dp 
Ey∼π(·|x) [ˆrk(x, y) + br
k(x, y)] −β · KL(π(·|x)∥πref(·|x))

(36)
Theorem 5 (Connection between Standard DPO and Standard RLHF with Constrained Policy Ranges
and Exploration Bonuses). Problems Eqs. (29) and (36) have the same set of optimal solutions.
Proof. Step (i). First, we prove that if π is an optimal solution to Eq. (36), then π is also an optimal
solution to Eq. (29).
If ˆrk ∈R is an optimal solution to Eq. (35), then
π∗
ˆrk+br
k(y|x) =
πref(y|x) · exp

1
β (ˆrk(x, y) + br
k(x, y))

P
y′∈Y πref(y′|x) · exp

1
β (ˆrk(x, y′) + br
k(x, y′))

is an optimal solution to Eq. (36). We have that π∗
ˆrk+br
k is also an optimal solution to Eq. (29). Otherwise,
there exists another π′ ∈˜Πr
k which achieves a smaller objective value in Eq. (29). Then, there must exist
a r′ ∈R which satisfies that
π′(y|x) =
πref(y|x) · exp

1
β (r′(x, y) + br
k(x, y))

P
y′∈Y πref(y′|x) · exp

1
β (r′(x, y′) + br
k(x, y′))
,
i.e.,
r′(x, y) = β log π′(y|x)
πref(y|x) + β log Zr′+br
k(x) −br
k(x, y),
and the objective value in Eq. (35) achieved by r′,
−
X
(x,yrw,yrℓ)∈˜
Dr
k
log σ
 
β log π′(yrw|x)
πref(yrw|x) + β log Zr′+br
k(x) −br
k(x, yrw)
−

β log π′(yrℓ|x)
πref(yrℓ|x) + β log Zr′+br
k(x) −br
k(x, yrℓ)
 !
,
is smaller than that achieved by ˆrk (since π′ achieves a smaller DPO objective value), which contradicts
the supposition that ˆrk is the optimal solution to Eq. (35).
25

--- Page 26 ---

Step (ii).
Next, we prove that if π is an optimal solution to Eq. (29), then π is also an optimal solution
to Eq. (36).
If ˜π ∈˜Πr is an optimal solution to Eq. (29), then there exists a ˜r ∈R which satisfies
˜π(y|x) =
πref(y|x) · exp

1
β (˜r(x, y) + br
k(x, y))

P
y′∈Y πref(y′|x) · exp

1
β (˜r(x, y′) + br
k(x, y′))
,
i.e.,
˜r(x, y) = β log
˜π(y|x)
πref(y|x) + β log Z˜r(x) −br
k(x, y).
(37)
We have that ˜r achieves the optimal value in Eq. (35),
−
X
(x,yrw,yrℓ)∈˜
Dr
k
log σ
 
β log
˜π(yrw|x)
πref(yrw|x) + β log Z˜r(x) −br
k(x, yrw)
−

β log
˜π(yrℓ|x)
πref(yrℓ|x) + β log Z˜r(x) −br
k(x, yrℓ)
 !
.
(38)
Otherwise, there exists another r′ ∈R and then there exists a π′ = π∗
ˆr ∈˜Πr which gives a smaller
objective value than ˜π in Eq. (38). Thus, ˜r achieves the optimal value in Eq. (35). Then, the optimal
solution to Eq. (36) under cost model ˜r is
π(y|x) ∝πref(y|x) · exp
 1
β (˜r(x, y) + br
k(x, y))

(a)
∝πref(y|x) · exp
 1
β

β log
˜π(y|x)
πref(y|x) + β log Z˜r(x)

∝πref(y|x) · exp

log
˜π(y|x)
πref(y|x)

= ˜π(y|x),
where (a) uses Eq. (37).
Therefore, ˜π is also an optimal solution to Eq. (36).
Now we present a result which relates our rearranged Lagrangian DPO objective to the safe RLHF
objective with constrained policy search ranges and exploration bonuses.
For any k ≥1, define the following problem that first learns a cost model and then finds the optimal
policy for the Lagrangian function under ˆrk + br
k and λk:
ˆck ←min
c∈C −1
N c
Nc
X
i=1
log σ
 c(xi, ycw
i ) −c(xi, ycℓ
i )

(39)
max
π
Ex∼Dp
Ey∼π(·|x) [ˆrk(x, y) + br
k(x, y)−λk (ˆck(x, y)−bc
k(x, y))]−β · KL(π(·|x)∥πref(·|x))

(40)
Theorem 6 (Connection between Our Rearranged Lagrangian DPO and Safe RLHF with Constrained
Policy Ranges and Exploration Bonuses). For any k ≥0, Problems Eqs. (30) and (40) have the same set
of optimal solutions.
Proof. First, note that for any ˆck, the optimal solution to Eq. (40) is
π∗
ˆrk+br
k−λk(ˆck−bc
k)(y|x)=
πref(y|x) exp

1
β (ˆrk(x, y)+br
k(x, y)−λk (ˆc(x, y)−bc
k(x, y)))

X
y′∈Y
πref(y′|x) exp
 1
β (ˆrk(x, y′)+br
k(x, y′)−λk (ˆc(x, y′)−bc
k(x, y′)))

|
{z
}
:=Zˆrk+br
k−λk(ˆck−bc
k)(x)
,
∀x ∈X.
(41)
26

--- Page 27 ---

Then, we have
ˆck(x, y) = 1
λk
 
ˆrk(x, y) + br
k(x, y) −β log
π∗
ˆrk+br
k−λk(ˆck−bc
k)(y|x)
πref(y|x)
−β log Zˆrk+br
k−λk(ˆck−bc
k)(x)
!
+ bc
k(x, y)
(a)
=
1
λk
 
β log
π∗
ˆrk+br
k(y|x)
πref(y|x)
+ β log Zˆrk+br
k(x) −β log
π∗
ˆrk+br
k−λk(ˆck−bc
k)(y|x)
πref(y|x)
−β log Zˆrk+br
k−λk(ˆck−bc
k)(x)
!
+ bc
k(x, y),
where equality (a) uses a similar derivation as Eq. (5).
Now we prove this theorem.
Step (i). First, we prove that if π is an optimal solution to Eq. (40), then π is also an optimal
solution to Eq. (30).
If ˆck ∈C is an optimal solution to Eq. (39), then π∗
ˆrk+br
k−λk(ˆck−bc
k) ∈˜Πc
k (as shown in Eq. (41)) is
an optimal solution to Eq. (40). We have that π∗
ˆrk+br
k−λk(ˆck−bc
k) is also an optimal solution to Eq. (30).
Otherwise, there exists another π′ ∈˜Πc
k which achieves a smaller objective value in Eq. (30). Then, there
must exist a c′ ∈C which satisfies that
π′(y|x) =
πref(y|x) · exp

1
β

β log
π∗
ˆrk+br
k (y|x)
πref(y|x)
−λk (c′(x, y) −bc
k(x, y))

X
y′∈Y
πref(y′|x) · exp
 
1
β
 
β log
π∗
ˆrk+br
k(y|x)
πref(y|x)
−λk (c′(x, y′) −bc
k(x, y′))
!!
|
{z
}
:=Z
β log
π∗
ˆrk+br
k
πref
−λk(c′−bc
k)
(x)
,
i.e.,
c′(x, y) = 1
λk
 
β log
π∗
ˆrk+br
k(y|x)
πref(y|x)
−β log π′(y|x)
πref(y|x) −β log Z
β log
π∗
ˆrk+br
k
πref
−λk(c′−bc
k)
(x)
!
+ bc
k(x, y),
and the objective value in Eq. (39) achieved by c′,
−
X
(x,ycw,ycℓ)∈Dc
log σ
 
1
λk

β log
π∗
ˆrk+br
k(ycw|x)
πref(ycw|x)
−β log π′(ycw|x)
πref(ycw|x)
−β log Z
β log
π∗
ˆrk+br
k
πref
−λk(c′−bc
k)
(x)

+bc
k(x, ycw)−1
λk

β log
π∗
ˆrk+br
k(ycℓ|x)
πref(ycℓ|x)
−β log π′(ycℓ|x)
πref(ycℓ|x)
−β log Z
β log
π∗
ˆrk+br
k
πref
−λk(c′−bc
k)
(x)

−bc
k(x, ycℓ)
!
,
is smaller than that achieved by ˆck, which contradicts the supposition that ˆck is the optimal solution to
Eq. (39).
Step (ii). Next, we prove that if π is an optimal solution to Eq. (30), then π is also an optimal
solution to Eq. (40).
If πk ∈˜Πc
k is an optimal solution to Eq. (30), then there exists a ck ∈C which satisfies
πk(y|x) =
πref(y|x) · exp

1
β

β log
π∗
ˆrk+br
k (y|x)
πref(y|x)
−λk (ck(x, y) −bc
k(x, y))

P
y′∈Y πref(y′|x) · exp

1
β

β log
π∗
ˆrk+br
k (y′|x)
πref(y′|x)
−λk (ck(x, y′) −bc
k(x, y′))
,
27

--- Page 28 ---

i.e.,
ck(x, y) = 1
λk
 
β log
π∗
ˆrk+br
k(y|x)
πref(y|x)
−β log πk(y|x)
πref(y|x) −β log Z
β log
π∗
ˆrk+br
k
πref
−λk(ck−bc
k)
(x)
!
+ bc
k(x, y).
We have that ck achieves the optimal value in Eq. (39),
−
X
(x,ycw,ycℓ)∈Dc
log σ
 
1
λk

β log
π∗
ˆrk+br
k(ycw|x)
πref(ycw|x)
−β log πk(ycw|x)
πref(ycw|x)
−β log Z
β log
π∗
ˆrk+br
k
πref
−λk(ck−bc
k)
(x)

+bc
k(x, ycw)−1
λk

β log
π∗
ˆrk+br
k(ycℓ|x)
πref(ycℓ|x)
−β log πk(ycℓ|x)
πref(ycℓ|x)
−β log Z
β log
π∗
ˆrk+br
k
πref
−λk(ck−bc
k)
(x)

−bc
k(x, ycℓ)
!
.
(42)
Otherwise, there exists another c′ ∈C and then there exists a π′ = π∗
ˆrk+br
k−λk(c′−br
k) ∈˜Πc
k which gives a
smaller objective value than ˜πk in Eq. (42). Thus, ck achieves the optimal value in Eq. (39). Then, the
optimal solution to Eq. (39) under cost model ck is
π(y|x) ∝πref(y|x) · exp
 
1
β

ˆrk(x, y) + br
k(x, y) −β log
π∗
ˆrk+br
k(y|x)
πref(y|x)
+ β log πk(y|x)
πref(y|x)
+ β log Z
β log
π∗
ˆrk+br
k
πref
−λk(ck−bc
k)
(x)
!
(a)
∝πref(y|x) · exp
 
1
β

β log Zˆrk+br
k(x) + β log πk(y|x)
πref(y|x)
+ β log Z
β log
π∗
ˆrk+br
k
πref
−λk(ck−bc
k)
(x)
!
∝πref(y|x) · exp
 1
β

β log πk(y|x)
πref(y|x)

= πk(y|x),
where (a) uses a similar derivation as Eq. (5).
Therefore, πk is also an optimal solution to Eq. (23).
E.2
Suboptimality and Constraint Violation
In the following, we present the proof of the suboptimality and constraint violation guarantees for
algorithm O-PD-DPO (Theorem 2).
Define event
Gon :=
(
|ˆrk(x, y) −r∗(x, y)| ≤4 ∥ϕ(x, y)∥(˜ΣDr
k +γonI)−1 ·
s
(exp (Rmax) + exp (−Rmax) + 2)2
N on

|X||Y| + log
2K
δ′

+ γon(Rmax)2 := br
k(x, y),
|ˆck(x, y) −c∗(x, y)| ≤4 ∥ϕ(x, y)∥(˜ΣDc
k +γonI)−1 ·
s
(exp (Cmax) + exp (−Cmax) + 2)2
N on

|X||Y| + log
2K
δ′

+ γon(Cmax)2 := bc
k(x, y),
∀(x, y) ∈X × Y
)
.
28

--- Page 29 ---

Lemma 5 (MLE Guarantee with Online Data). It holds that
Pr [Gon] ≥1 −2δ′.
Proof. According to Lemma 3.1 in [Zhu et al.(2023)Zhu, Jordan, and Jiao], we have that with probability
at least 1 −δ′,
|ˆrk(x, y) −r∗(x, y)|
≤4 ∥ϕ(x, y)∥(ΣDr
k +N onγonI)−1 ·
s
(exp (Rmax) + exp (−Rmax) + 2)2

|X||Y| + log
 2
δ′

+ N onγon(Rmax)2
=
4
√
N on ∥ϕ(x, y)∥(
1
Non ΣDr
k +γonI)−1 ·
s
(exp (Rmax) + exp (−Rmax) + 2)2

|X||Y| + log
 2
δ′

+ N onγon(Rmax)2
= 4 ∥ϕ(x, y)∥(˜ΣDr
k +γonI)−1 ·
s
(exp (Rmax) + exp (−Rmax) + 2)2
N on

|X||Y| + log
 2
δ′

+ γon(Rmax)2.
Taking a union bound over k = 1, . . . , K, we can obtain the first statement.
Using a similar argument, we can obtain the second statement.
Lemma 6. For any k ≥1, we have
f(π∗; ˆrk + br
k) −f(πk; ˆrk + br
k) ≤−λk · Ex∼Dp,y∼πk(·|x)[ˆck(x, y) −bc
k(x, y)].
Proof. It holds that
f(π∗; ˆrk + br
k)
(a)
≤f(π∗; ˆrk + br
k) −λk · Ex∼Dp,y∼π∗(·|x)[c∗(x, y)]
= Ex∼Dp 
Ey∼π∗(·|x) [ˆrk(x, y) + br
k(x, y) −λk · c∗(x, y)] −β · KL(π∗(·|x)∥πref(·|x))

= Ex∼Dp
h
Ey∼π∗(·|x) [ˆrk(x, y) + br
k(x, y) −λk (ˆck(x, y) −bc
k(x, y))]
−β · KL(π∗(·|x)∥πref(·|x))
i
+ λk · Ex∼Dp,y∼π∗(·|x)[ˆck(x, y) −bc
k(x, y) −c∗(x, y)]
(b)
≤Ex∼Dp
h
Ey∼πk(·|x) [ˆrk(x, y) + br
k(x, y) −λk (ˆck(x, y) −bc
k(x, y))]
−β · KL(πk(·|x)∥πref(·|x))
i
= f(πk; ˆrk + br
k) −λk · Ex∼Dp,y∼πk(·|x)[ˆck(x, y) −bc
k(x, y)],
where inequality (a) uses the fact that λk ≥0 and π∗is feasible, and inequality (b) comes from
Theorem 6.
Let
¯ΣDr
k := ΣDr
1 +
K
X
k=1
Ex∼Dp,y∼πk(·|x),y′∼πbase(·|x)
h
(ϕ(x, y) −ϕ(x, y′)) (ϕ(x, y) −ϕ(x, y′))⊤i
,
¯ΣDc
k := ΣDc
1 +
K
X
k=1
Ex∼Dp,y∼πk(·|x),y′∼πbase(·|x)
h
(ϕ(x, y) −ϕ(x, y′)) (ϕ(x, y) −ϕ(x, y′))⊤i
.
Lemma 7. It holds that
K
X
k=1
Ex∼Dp,y∼πk(·|x)[br
k(x, y)]
29

--- Page 30 ---

≤4
s
(exp (Rmax) + exp (−Rmax) + 2)2
N on

|X||Y| + log
2K
δ′

+ γon(Rmax)2·
2
s
2|X||Y|K

log
γon + 4|Dr
1| + 4K
|X||Y|γon

+
1
Cbase log
γon + |Dr
1| + CbaseK
|X||Y|γon

,
and
K
X
k=1
Ex∼Dp,y∼πk(·|x)[bc
k(x, y)]
≤4
s
(exp (Cmax) + exp (−Cmax) + 2)2
N on

|X||Y| + log
2K
δ′

+ γon(Cmax)2·
2
s
2|X||Y|K

log
γon + 4|Dc
1| + 4K
|X||Y|γon

+
1
Cbase log
γon + |Dc
1| + CbaseK
|X||Y|γon

.
Proof. First, we have
¯ΣDr
k + γonI = ΣDr
1 + γonI
+
K
X
k=1
Ex∼Dp,y∼πk(·|x),y′∼πbase(·|x)
h
(ϕ(x, y) −ϕ(x, y′)) (ϕ(x, y) −ϕ(x, y′))⊤i
⪰ΣDr
1 + γonI + Cbase
K
X
k=1
Ex∼Dp,y′∼πbase

ϕ(x, y′)ϕ(x, y′)⊤
,
and thus
 ¯ΣDr
k + γonI
−1 ⪯
 
ΣDr
1 + γonI + Cbase
K
X
k=1
Ex∼Dp,y′∼πbase

ϕ(x, y′)ϕ(x, y′)⊤
!−1
=
1
Cbase
 
1
Cbase
 ΣDr
1 + γonI

+
K
X
k=1
Ex∼Dp,y′∼πbase

ϕ(x, y′)ϕ(x, y′)⊤
!−1
.
(43)
For ease of notation, let d := |X||Y|. Then, we have
K
X
k=1
Ex∼Dp,y∼πk(·|x)
h
∥ϕ(x, y)∥(˜ΣDr
k +γonI)−1
i
≤
v
u
u
tK
K
X
k=1

Ex∼Dp,y∼πk(·|x)
h
∥ϕ(x, y)∥(˜ΣDr
k +γonI)−1
i2
≤
v
u
u
tK
K
X
k=1
Ex∼Dp,y∼πk(·|x)
h
∥ϕ(x, y)∥2
(˜ΣDr
k +γonI)−1
i
(a)
≤
v
u
u
t2K
K
X
k=1
Ex∼Dp,y∼πk(·|x)
h
∥ϕ(x, y)∥2
(¯ΣDr
k +γonI)−1
i
=
v
u
u
t2K
K
X
k=1
Ex∼Dp,y∼πk(·|x),y′∼πbase(·|x)

∥ϕ(x, y) −ϕ(x, y′) + ϕ(x, y′)∥2
(¯ΣDr
k +γonI)−1

≤2
√
K
 K
X
k=1
Ex∼Dp,y∼πk(·|x),y′∼πbase(·|x)
h
∥ϕ(x, y) −ϕ(x, y′)∥2
(¯ΣDr
k +γonI)−1
i
+
K
X
k=1
Ex∼Dp,y′∼πbase(·|x)
h
∥ϕ(x, y′)∥2
(¯ΣDr
k +γonI)−1
i ! 1
2
30

--- Page 31 ---

(b)
≤2
√
K
 
2 log




γon+4|Dr
1|+4K
d
d
(γon)d


+
1
Cbase
K
X
k=1
Ex∼Dp,y′∼πbase(·|x)
"
∥ϕ(x, y′)∥2
1
Cbase

ΣDr
1 +γonI

+Pk−1
k′=1 Ex∼Dp,˜y∼πbase(·|x)[ϕ(x,˜y)ϕ(x,˜y)⊤]
−1
#! 1
2
(c)
≤2
√
K
v
u
u
u
u
u
u
t
2d log
γon + 4|Dr
1| + 4K
dγon

+
2
Cbase log






1
Cbase (γon+|Dr
1|)+K
d
d
  γon
Cbase
d





≤2
s
2dK

log
γon + 4|Dr
1| + 4K
dγon

+
1
Cbase log
γon + |Dr
1| + CbaseK
dγon

,
where inequality (a) comes from Lemma 13, inequality (b) uses Lemma 11 and Eq. (43), and inequality
(c) is due to Lemma 11.
Thus, we can obtain the first statement.
Using a similar analysis as above, we can further obtain the second statement.
In the following, we prove Theorem 2.
Proof of Theorem 2. For this online setting, we also use events E and F defined in Eqs. (26) and (27).
Let δ′ := δ
4. Then, according to Lemmas 1 and 3, we have Pr[E ∩F ∩Gon] ≥1 −δ. Now it suffices to
prove this theorem assuming that event E ∩F ∩Gon holds. In the following proof, we assume that event
E ∩F ∩Gon holds.
For any k ≥1 and ¯λ ∈[0, 2ρ], we have
 λk+1 −¯λ
2 =

Proj[0,2ρ] (λk + ηk˜ck) −Proj[0,2ρ]
 ¯λ
2
(a)
≤
 λk + ηk˜ck −¯λ
2
=
 λk −¯λ
2 + 2ηk˜ck
 λk −¯λ

+ (ηk)2 (˜ck)2 ,
where inequality (a) uses the nonexpansivity of the projection to [0, 2ρ].
Summing the above inequality over k = 1, . . . , K, we have
0 ≤
 λK+1 −¯λ
2 ≤
 λ1 −¯λ
2 +
K
X
k=1
2ηk · Ex∼Dp,y∼πk(·|x)[c∗(x, y)] ·
 λk −¯λ

−
K
X
k=1
2ηk · Ex∼Dp,y∼πk(·|x)[c∗(x, y)] ·
 λk −¯λ

+
K
X
k=1
2ηk˜ck
 λk −¯λ

+
K
X
k=1
(ηk)2 (˜ck)2 .
Hence, we have
K
X
k=1
2ηk · Ex∼Dp,y∼πk(·|x)[c∗(x, y)] · ¯λ −
K
X
k=1
2ηk · Ex∼Dp,y∼πk(·|x)[ˆck(x, y) −bc
k(x, y)] · λk
≤
 λ1 −¯λ
2 +
K
X
k=1
(ηk)2 (˜ck)2 +
K
X
k=1
2ηkλk · Ex∼Dp,y∼πk(·|x)[c∗(x, y) −ˆck(x, y) + bc
k(x, y)]
+
K
X
k=1
2ηk
 λk −¯λ
  ˜ck −Ex∼Dp,y∼πk(·|x)[c∗(x, y)]

.
Using Lemma 6, we have
K
X
k=1
2ηk
 Ex∼Dp,y∼πk(·|x)[c∗(x, y)] · ¯λ + f(π∗; ˆrk + br
k) −f(πk; ˆrk + br
k)

31

--- Page 32 ---

≤
 λ1 −¯λ
2 +
K
X
k=1
(ηk)2 (˜ck)2 +
K
X
k=1
2ηkλk · Ex∼Dp,y∼πk(·|x)[c∗(x, y) −ˆck(x, y) + bc
k(x, y)]
+
K
X
k=1
2ηk
 λk −¯λ
  ˜ck −Ex∼Dp,y∼πk(·|x)[c∗(x, y)]

(a)
≤
 λ1 −¯λ
2 +
K
X
k=1
(ηk)2 (˜ck)2 + 4
K
X
k=1
ηkλk · Ex∼Dp,y∼πk(·|x)[bc
k(x, y)]
+
K
X
k=1
2ηk
 λk −¯λ
  ˜ck −Ex∼Dp,y∼πk(·|x)[c∗(x, y)]

,
where inequality (a) uses the definition of event Gon.
Recall that ηk = η. Then, we have
K
X
k=1
(f(π∗) −f(πk)) + ¯λ
K
X
k=1
Ex∼Dp,y∼πk(·|x)[c∗(x, y)]
≤1
2η
 λ1 −¯λ
2 + η
2
K
X
k=1
(˜ck)2 + 2
K
X
k=1
λk · Ex∼Dp,y∼πk(·|x)[bc
k(x, y)]
+
K
X
k=1
 λk −¯λ
  ˜ck −Ex∼Dp,y∼πk(·|x)[c∗(x, y)]

+
K
X
k=1
(f(π∗) −f(π∗; ˆrk + br
k)) −
K
X
k=1
(f(πk) −f(πk; ˆrk + br
k))
≤1
2η
 λ1 −¯λ
2 + η(Cmax)2K
2
+ 2
K
X
k=1
λk · Ex∼Dp,y∼πk(·|x)[bc
k(x, y)]
+
K
X
k=1
 λk −¯λ
  ˜ck −Ex∼Dp,y∼πk(·|x)[c∗(x, y)]

+ K · Ex∼Dp,y∼π∗(·|x)[r∗(x, y) −(ˆrk(x, y) + br
k(x, y))]
−
K
X
k=1
Ex∼Dp,y∼πk(·|x)[r∗(x, y) −(ˆr(x, y) + br
k(x, y))]
≤1
2η
 λ1 −¯λ
2 + η(Cmax)2K
2
+ 2
K
X
k=1
λk · Ex∼Dp,y∼πk(·|x)[bc
k(x, y)]
+
K
X
k=1
 λk −¯λ
  ˜ck −Ex∼Dp,y∼πk(·|x)[c∗(x, y)]

+ 2
K
X
k=1
Ex∼Dp,y∼πk(·|x)[br
k(x, y)].
Let ¯λ = 0. Recall that πout
K
is the uniform policy over π1, . . . , πK and η :=
λ1
Cmax
√
K . Then, we have
f(π∗) −f(πout
K )
= 1
K
K
X
k=1
(f(π∗) −f(πk))
≤λ1Cmax
√
K
+ 2ρ
K
K
X
k=1
Ex∼Dp,y∼πk(·|x)[bc
k(x, y)] + ρ
K
K
X
k=1
˜ck −Ex∼Dp,y∼πk(·|x)[c∗(x, y)]

+ 2
K
K
X
k=1
Ex∼Dp,y∼πk(·|x)[br
k(x, y)]
= O
 
λ1Cmax
√
K
+ ρCmax
s
log
  K
δ

N CE
+ ρW
v
u
u
tlog

|X||Y|N CEK
δ

M CE
32

--- Page 33 ---

+ ρ
s
(exp (Cmax) + exp (−Cmax) + 2)2
N on

|X||Y| + log
K
δ

+ γon(Cmax)2·
s
|X||Y|K

log
γon + |Dr
1| + K
|X||Y|γon

+
1
Cbase log
γon + |Dr
1| + CbaseK
|X||Y|γon

+
s
(exp (Rmax) + exp (−Rmax) + 2)2
N on

|X||Y| + log
K
δ

+ γon(Rmax)2·
s
|X||Y|K

log
γon + |Dr
1| + K
|X||Y|γon

+
1
Cbase log
γon + |Dr
1| + CbaseK
|X||Y|γon

.
Let ¯λ = 2ρ. Then, we have
f(π∗) −f(πout
K ) + 2ρEx∼Dp,y∼πout
K (·|x)[c∗(x, y)]
= 1
K
K
X
k=1
(f(π∗) −f(πk)) + 2ρ
K
K
X
k=1
Ex∼Dp,y∼πk(·|x)[c∗(x, y)].
If
1
K
PK
k=1 Ex∼Dp,y∼πk(·|x)[c∗(x, y)] ≤0, the second statement of the theorem naturally holds; Other-
wise, we can replace the term 2ρEx∼Dp,y∼πout
K (·|x)[c∗(x, y)] by 2ρ[Ex∼Dp,y∼πout
K (·|x)[c∗(x, y)]]+ in the above
inequality. Then, using Corollary 1 and Lemma 10, we obtain
Ex∼Dp,y∼πout
K (·|x)[c∗(x, y)]
≤Cmax
4ρ
√
K
 
(λ1 −2ρ)2
λ1
+ λ1
!
+ 1
K
K
X
k=1
Ex∼Dp,y∼πk(·|x)[bc
k(x, y)]
+
1
2K
K
X
k=1
˜ck −Ex∼Dp,y∼πk(·|x)[c∗(x, y)]
 +
1
ρK
K
X
k=1
Ex∼Dp,y∼πk(·|x)[br
k(x, y)]
= O
 
Cmax
ρ
√
K
 
(λ1 −2ρ)2
λ1
+ λ1
!
+ Cmax
s
log
  K
δ

N CE
+ W
v
u
u
tlog

|X||Y|N CEK
δ

M CE
+
s
(exp (Cmax) + exp (−Cmax) + 2)2
N on

|X||Y| + log
K
δ

+ γon(Cmax)2·
s
|X||Y|K

log
γon + |Dr
1| + K
|X||Y|γon

+
1
Cbase log
γon + |Dr
1| + CbaseK
|X||Y|γon

+ 1
ρ
s
(exp (Rmax) + exp (−Rmax) + 2)2
N on

|X||Y| + log
K
δ

+ γon(Rmax)2·
s
|X||Y|K

log
γon + |Dr
1| + K
|X||Y|γon

+
1
Cbase log
γon + |Dr
1| + CbaseK
|X||Y|γon
!
.
F
Technical Tools
In this section, we introduce several technical tools which are used in our analysis.
Lemma 8 (Theorem 8.42 in [Beck(2017)]). For any λ ≥0 such that q(λ) ≤u,
λ ≤
u −f(¯π)
−Ex∼Dp,y∼¯π(·|x)[c∗(x, y)].
Proof. For any λ ≥0 such that q(λ) ≤u, we have
u ≥q(λ) ≥f(¯π) −λ · Ex∼Dp,y∼¯π(·|x)[c∗(x, y)].
33

--- Page 34 ---

Hence,
−λ · Ex∼Dp,y∼¯π(·|x)[c∗(x, y)] ≤u −f(¯π).
Since Ex∼Dp,y∼¯π(·|x)[c∗(x, y)] < 0, we have
λ ≤
u −f(¯π)
−Ex∼Dp,y∼¯π(·|x)[c∗(x, y)].
Let Λ∗be the set of the optimal solutions to the dual problem minλ≥0 q(λ).
Corollary 1 (Corollary 8.43 in [Beck(2017)]). For any λ∗∈Λ∗,
λ∗≤
f(π∗) −f(¯π)
−Ex∼Dp,y∼¯π(·|x)[c∗(x, y)] ≤ρ,
where the second inequality comes from the definition of ρ.
Proof. This corollary can be obtained by setting u as the optimal value to the dual problem minλ≥0 q(λ) =
f(π∗) in Lemma 8.
Define g(π) := Ex∼Dp,y∼π(·|x)[c(x, y)]. Let
v(u) := max
π
{f(π) : g(π) ≤u} ,
C(u) := {π : g(π) ≤u} .
Lemma 9 (Theorem 3.59 in [Beck(2017)]). For any λ∗∈Λ∗,
v(0) + λ∗u ≥v(u).
Proof. For any π, we have
f(π) −λ∗g(π) ≤max
π
(f(π) −λ∗g(π)) = q(λ∗) = f(π∗) = v(0).
Thus, for any u ∈R and π ∈C(u),
v(0) + λ∗u ≥f(π) −λ∗(g(π) −u) ≥f(π).
Since the above inequality holds for all π ∈C(u), by maximizing f(π) over π ∈C(u), we have that for
any u ∈R,
v(0) + λ∗u ≥v(u).
Lemma 10 (Theorem 3.60 in [Beck(2017)]). If a policy ˜π satisfies that
f(π∗) −f(˜π) + ρ′[g(˜π)]+ ≤L,
where L > 0 and ρ′ ≥2λ∗, then
[g(˜π)]+ ≤2L
ρ′ .
Proof. From Lemma 9, we have that for any u ∈R,
v(0) −v(u) ≥−λ∗u.
Let ˜u := [g(˜π)]+. Then, we have
(ρ′ −λ∗) ˜u ≤ρ′˜u + v(0) −v(˜u)
(a)
≤f(π∗) −f(˜π) + ρ′˜u
34

--- Page 35 ---

≤L,
where inequality (a) uses the fact that v(0) = f(π∗) and v(˜u) ≥f(˜π).
Since ρ′ ≥2λ∗, we have
˜u ≤
L
ρ′ −λ∗≤
L
ρ′ −ρ′
2
= 2L
ρ′ .
Lemma 11. Let ψ1, . . . , ψK be a sequence of d-dimensional random vectors following distributions
B1, . . . , BK, respectively, and we have ∥ψk∥≤L for any k ≥1. Let A0 be a d × d positive definite matrix
such that σmin(A0) ≥{1, L2}, and define Ak = A0 + Pk
i=1 Eψi∼Bi[ψiψ⊤
i ] for any k ≥1. Then, we have
K
X
k=1
Eψk∼Bk
h
∥ψk∥2
(Ak−1)−1
i
≤2 log det(AK)
det(A0) ≤2 log




trace(A0)+KL2
d
d
det (A0)


.
Proof. This proof uses a similar analytical procedure as Lemma 11 in [Abbasi-Yadkori et al.(2011)Abbasi-Yadkori, P´al, and
We have
det (AK) = det
 AK−1 + EψK∼BK

ψKψ⊤
K

= det (AK−1) det

I + (AK−1)−1
2 EψK∼BK

ψKψ⊤
K

(AK−1)−1
2

= det (AK−1) det

I + EψK∼BK

(AK−1)−1
2 ψK

(AK−1)−1
2 ψK
⊤
= det (AK−1)

1 + EψK∼BK
h
∥ψK∥2
(AK−1)−1
i
= det (A0)
K
Y
k=1

1 + Eψk∼Bk
h
∥ψk∥2
(Ak−1)−1
i
.
Taking logarithm on both sides, we have
log det (AK) = log det (A0) +
K
X
k=1
log

1 + Eψk∼Bk
h
∥ψk∥2
(Ak−1)−1
i
.
Since σmin(A0) ≥{1, L2}, we have ∥ψk∥2
(Ak−1)−1 ≤1 for any k ≥1. Using the fact that x ≤2 log(1+x),
we have
K
X
k=1
Eψk∼Bk
h
∥ψk∥2
(Ak−1)−1
i
≤2
K
X
k=1
log

1 + Eψk∼Bk
h
∥ψk∥2
(Ak−1)−1
i
= 2 log det (AK)
det (A0)
(a)
≤2 log




trace(A0)+KL2
d
d
det (A0)


,
where inequality (a) uses the AM-GM inequality.
Lemma 12 (Lemma H.3 in [Agarwal et al.(2020)Agarwal, Henaff, Kakade, and Sun]). Let B be a dis-
tribution of d-dimensional vectors which satisfies that ∥ψ∥≤L if ψ ∼B. Let ψ1, . . . , ψM be M i.i.d.
samples from B, and define A = Eψ∼B[ψψ⊤]. Then, with probability at least 1 −δ, we have that for any
v ∈Rd,
v⊤
 
1
M
M
X
i=1
ψiψ⊤
i −A
!
v
 ≤
2L2 ln

8 ˆd
δ

3M
+ L2
v
u
u
t2 ln

8 ˆd
δ

M
,
where ˆd := trace(A)
∥A∥
is the intrinsic dimension of A.
35

--- Page 36 ---

Proof. For any i ≥1, let Di := ψiψ⊤
i −A. Then, we have that E[Di] = 0, ∥Di∥≤L2, and

M
X
i=1
E[(Di)2]
 ≤ML4.
The intrinsic dimension of PM
i=1 E[(Di)2] is equal to that of A, which is ˆd by definition.
Using the Matrix Bernstein inequality (Theorem 7.7.1 in [Tropp et al.(2015)]), we have that for any
t ≥L2√
M + L2
3 ,
Pr
"
σmax
 M
X
i=1
E[(Di)2]
!
≥t
#
≤4 ˆd · exp
 
−t2
2
L4M + L2t
3
!
.
Setting t′ =
t
M , we have that for any t′ ≥
L2
√
M + L2
3M ,
Pr
"
σmax
 
1
M
M
X
i=1
E[(Di)2]
!
≥t′
#
≤4 ˆd · exp
 
−M(t′)2
2
L4 + L2t′
3
!
.
When t′ =
2L2 ln

4 ˆ
d
δ

3M
+ L2
r
2 ln

4 ˆ
d
δ

M
, we have 4 ˆd · exp

−M(t′)2
2
L4+ L2t′
3

≤δ.
Hence, with probability at least 1 −δ, we have
σmax
 
1
M
M
X
i=1
E[(Di)2]
!
≤
2L2 ln

4 ˆd
δ

3M
+ L2
v
u
u
t2 ln

4 ˆd
δ

M
.
We can obtain this concentration inequality in the other direction with a similar argument. Therefore,
we complete the proof of this lemma.
Lemma 13 (Lemma H.4 in [Agarwal et al.(2020)Agarwal, Henaff, Kakade, and Sun]). Let B1, . . . , BK be
K distributions of d-dimensional vectors. For any i ∈[K], we draw M i.i.d. samples ψi,1, . . . , ψi,M from
Bi, and form ˆAi =
1
M
PM
j=1 ψi,jψ⊤
i,j. Define Ai = Eψ∼Bi[ψψ⊤], A = PK
i=1 Ai+γI, and ˆA = PK
i=1 ˆAi+γI.
Setting M := 32K2 ln( 8K ˜
d
δ
)
γ2
, with probability at least 1 −δ, we have that for any v ∈Rd,
1
2v⊤(A + γI)−1v ≤v⊤( ˆA + γI)−1v ≤2v⊤(A + γI)−1v,
where ˜d := maxi∈[K]
trace(Ai)
∥Ai∥
.
Proof. Let α(M) =:
2L2 ln

8K ˆ
d
δ

3M
+ L2
r
2 ln

8K ˆ
d
δ

M
. Using Lemma 12, we have that with probability 1 −δ,
for any i ∈[K],
Ai + α(M)I + γ
K I ⪰ˆAi + γ
K I ⪰Ai −α(M)I + γ
K I.
Hence, we have
A + Kα(M)I + γI ⪰ˆA + γI ⪰A −Kα(M)I + γI.
When γ ≥2Kα(M), the above inequality implies
(A + Kα(M)I + γI)−1 ⪯

ˆA + γI
−1
⪯(A −Kα(M)I + γI)−1 .
Let UΛU T be the eigendecomposition of A, where Λ = diag(σ1, . . . , σd) and U = [u1, . . . , ud]. Then,
we have
v⊤( ˆA + γI)−1v −v⊤(A + γI)−1v ≤v⊤
(A −Kα(M)I + γI)−1 −(A + γI)−1
v
36

--- Page 37 ---

=
d
X
i=1

(σi + γ −Kα(M))−1 −(σi + γ)−1
(v⊤ui)2.
For any i ∈[d], since σi ≥0, we have σi + γ ≥2Kα(M), and then 2(σi + γ −Kα(M)) ≥σi + γ,
which implies (σi + γ −Kα(M))−1 ≤2(σi + γ)−1. Therefore, we have
v⊤( ˆA + γI)−1v −v⊤(A + γI)−1v ≤
d
X
i=1
(σi + γ)−1 (v⊤ui)2 = v⊤(A + γI)−1v.
Using a similar analysis, we can obtain the statement in the other direction.
37

```
