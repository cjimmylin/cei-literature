---
title: "Navigating the Social Welfare Frontier - PDF Extract"
source_pdf: "2025-Kim-Navigating the Social Welfare Frontier.pdf"
pages: 23
extracted_at: "2026-01-24T16:38:28.703757"
---

# PDF Extract: Navigating the Social Welfare Frontier

**Source PDF:** 2025-Kim-Navigating the Social Welfare Frontier.pdf
**Total Pages:** 23

---

## Content

```
--- Page 1 ---

Navigating the Social Welfare Frontier:
Portfolios for Multi-objective Reinforcement Learning
Cheol Woo Kim * 1 Jai Moondra * 2 Shresth Verma 1 Madeleine Pollack 3 Lingkai Kong 1 Milind Tambe 1 4
Swati Gupta 3
Abstract
In many real-world applications of reinforcement
learning (RL), deployed policies have varied im-
pacts on different stakeholders, creating chal-
lenges in reaching consensus on how to effec-
tively aggregate their preferences. Generalized
p-means form a widely used class of social wel-
fare functions for this purpose, with broad applica-
tions in fair resource allocation, AI alignment, and
decision-making. This class includes well-known
welfare functions such as Egalitarian, Nash, and
Utilitarian welfare. However, selecting the appro-
priate social welfare function is challenging for
decision-makers, as the structure and outcomes
of optimal policies can be highly sensitive to the
choice of p. To address this challenge, we study
the concept of an α-approximate portfolio in RL,
a set of policies that are approximately optimal
across the family of generalized p-means for all
p ≤1. We propose algorithms to compute such
portfolios and provide theoretical guarantees on
the trade-offs among approximation factor, portfo-
lio size, and computational efficiency. Experimen-
tal results on synthetic and real-world datasets
demonstrate the effectiveness of our approach in
summarizing the policy space induced by varying
p values, empowering decision-makers to navi-
gate this landscape more effectively.
1. Introduction
In this paper, we study a reinforcement learning (RL) set-
ting where a deployed policy impacts multiple stakeholders
in different ways. Each stakeholder is associated with a
unique reward function, and the goal is to train a policy that
adequately aggregates their preferences.
*Equal contribution
1Harvard University, Cambridge, USA
2Georgia Institute of Technology, Atlanta, USA 3Massachusetts
Institute of Technology, Cambridge, USA 4Google Deepmind.
Correspondence to: Cheol Woo Kim <cwkim@seas.harvard.edu>.
Proceedings of the 42 nd International Conference on Machine
Learning, Vancouver, Canada. PMLR 267, 2025. Copyright 2025
by the author(s).
This setting, which is often modeled using multi-objective
reinforcement learning (MORL), arises in many RL applica-
tions, such as fair resource allocation in healthcare (Verma
et al., 2024a), cloud computing (Perez et al., 2009; Hao et al.,
2023) and communication networks (Wu et al., 2018; Chen
et al., 2021). Recently, with the rise of large language mod-
els (LLMs), reinforcement learning from human feedback
(RLHF) techniques that reflect the preferences of hetero-
geneous individuals have also been explored (Chakraborty
et al., 2024; Zhong et al., 2024; Park et al., 2024).
Preference aggregation in such scenarios is often achieved
by choosing a social welfare function, which takes the
utilities of multiple stakeholders as input and outputs a
scalar value representing the overall welfare (Yu et al., 2024;
Cousins et al., 2024; Verma et al., 2024a; Fan et al., 2023;
Zhong et al., 2024; Park et al., 2024; Chakraborty et al.,
2024). However, selecting the appropriate social welfare
function is a nontrivial task. Different functions encode
distinct fairness criteria, and the resulting policies can lead
to vastly different outcomes for stakeholders depending on
the choice of the social welfare function.
In this work, we focus on a class of social welfare func-
tions known as generalized p-means, a widely used class of
social welfare functions in algorithmic fairness and social
choice theory. Each choice of p represents a distinct notion
of fairness, and the p-means unify commonly used welfare
functions such as Egalitarian welfare (p = −∞), Nash wel-
fare (p = 0) and Utilitarian welfare (p = 1), providing a
smooth transition between these principles. Notably, this is
known to be the only class of social welfare functions that
satisfy several key axioms of social welfare, such as mono-
tonicity, symmetry, and independence of scale (Roberts,
1980; Moulin, 2003; Cousins, 2023; Pardeshi et al., 2024).
In practice, the right choice of p is often unclear in advance,
and the decision-maker must understand how policies vary
with p in order to make informed choices about which p
(and thus which policy) to adopt. Small changes in p can
sometimes lead to dramatically different policies, and se-
lecting a policy optimized for an arbitrary p can lead to
poor outcomes under a different p value. Despite these chal-
lenges, much of the existing work assumes a fixed social
1
arXiv:2502.09724v2  [cs.LG]  16 Jul 2025

--- Page 2 ---

Navigating the Social Welfare Frontier
Figure 1. Portfolio of three policies for the healthcare intervention
setting (see Section 5 for details), obtained using Algorithm 1 with
α = 0.60. The bar plots show total rewards induced by each
policy across different education (top) and age (bottom) brackets.
A “score” of 1.0 corresponds to a baseline policy (not shown in
the figure) used for comparison. The three policies impact various
education and age brackets differently, offering a theoretically
sound and diverse set of options for decision-makers.
welfare function — and hence a fixed value of p — is given
(Hayes et al., 2022).
To address this challenge, we propose a method to compute a
small yet representative set of policies that covers the entire
spectrum of fairness criteria represented by p ≤1. Our main
algorithm, p-MEANPORTFOLIO, sequentially selects finite
p values starting from −∞to 1. These values are chosen
so that the optimal policies at these points sufficiently cover
the entire range of p ≤1 for a given approximation factor
α. We also propose a computationally efficient heuristic
algorithm, which adaptively selects the next p value from
the intervals formed by previously chosen p values.
The portfolios provide a structured summary of approxi-
mately optimal policies, allowing decision-makers to navi-
gate the implications of different p values efficiently. The
decision-maker can review the impact of the choice of p on
the structure of policies, on relevant dimensions of interest,
and make an informed choice about which policy to deploy.
1.1. Summary of Contributions
In this paper, we explore the concept of α-approximate port-
folios for preference aggregation in MORL. We summarize
our contributions as follows:
1. We propose Algorithm p-MEANPORTFOLIO (Algo-
rithm 1) to compute a finite portfolio of policies that
is α-approximate for the generalized p-means objectives
for any value of p ≤1. We provide theoretical guaran-
tees, including an upper bound on the portfolio size and
the number of MDPs solved to optimality, both expressed
in terms of the approximation factor α.
2. We
introduce
a
lightweight
heuristic
BUDGET-
CONSTRAINEDPORTFOLIO
(Algorithm
3)
that
reduces computational costs compared to Algorithm
p-MEANPORTFOLIO while maintaining high-quality
portfolio generation.
3. We theoretically show that the search for an optimal
policy for a given p-mean can be efficiently warm-started
using the optimal policy for a different p-mean.
4. We evaluate our approach on three different domains,
spanning synthetic to real-world problems. Our results
show that a small portfolio can achieve near-optimal
performance across all p ≤1. Moreover, the heuristic
BUDGET-CONSTRAINEDPORTFOLIO constructs portfo-
lios that closely match those produced by Algorithm
p-MEANPORTFOLIO, while significantly reducing the
computational cost.
The literature in RL with multiple stakeholders has primarily
focused on optimizing policies for a given choice of com-
posite objective. However, this work shifts the focus toward
constructing a small set of policies with theoretical guar-
antees. This approach better captures the trade-offs within
the actionable policy space, rather than relying on modeling
choices on how these objectives should be formulated.
1.2. Example
An illustrative example we consider in this work is a public
health application, where the staff of a healthcare orga-
nization aims to train an intervention policy for multiple
beneficiaries under a limited budget (Verma et al., 2024a).
This setting can be captured by restless multi-armed bandits
(RMABs) (Whittle, 1988), which model sequential resource
allocation problems under budget constraints. In this con-
text, each beneficiary is associated with a state variable
representing their level of engagement with the healthcare
program, and the overall state of the problem is the con-
catenation of the states of all beneficiaries. At each time
step, a policy determines which beneficiary to intervene on,
subject to the budget constraint. Depending on the reward
function used to train a policy, different socio-demographic
groups among the beneficiaries can be prioritized. For ex-
ample, one reward function might encode the preference
to prioritize older populations, while another reward func-
tion might encode the preference to prioritize low-income
2

--- Page 3 ---

Navigating the Social Welfare Frontier
populations. The decision-maker (e.g., healthcare organiza-
tion staff) must train a policy that balances these conflicting
objectives.
See Figure 1 for a demonstration of a portfolio generated
using the proposed method. The portfolio consists of three
policies, each affecting stakeholders differently based on age
and education levels. This perspective helps staff understand
the trade-offs between operational choices. For details on
the experiment, refer to Section 5.
2. Related Work
Social Welfare Function and RL. In RL with multiple
stakeholders, various social welfare functions have been ex-
plored, including generalized Gini-Welfare (Yu et al., 2024;
Cousins et al., 2024), p-means (Verma et al., 2024a; Fan
et al., 2023; Cousins et al., 2024), proportional-fairness (Ju
et al., 2024), Nash welfare (Mandal and Gan, 2023), among
others. (Alamdari et al., 2024) investigated ordinal social
welfare functions rather than cardinal ones.
A related line of work has emerged in RLHF for LLMs,
where social choice theory has been used to aggregate mul-
tiple reward models. For example, approaches leveraging
Nash welfare (Zhong et al., 2024), α-fairness (Park et al.,
2024), and Egalitarian welfare (Chakraborty et al., 2024)
have been proposed. However, in both RLHF and broader
multi-stakeholder RL, existing works typically assume that
a fixed social welfare function is given and focus on comput-
ing the corresponding optimal policy (Hayes et al., 2022).
As a result, these methods do not offer guidance for settings
where the appropriate choice of social welfare function is
unclear in advance.
Portfolios in MORL. In the broader MORL literature, the
concept of portfolios of policies is well-established. A com-
mon approach is to compute solutions that approximate the
Pareto front (Parisi et al., 2014; Van Moffaert and Nowé,
2014; R˘adulescu et al., 2019; Hayes et al., 2022). While
the Pareto front provides a characterization of trade-offs
between conflicting objectives, it does not assume a specific
set of social welfare functions. This generality, while pow-
erful, presents challenges in practical multi-stakeholder set-
tings. That is, the Pareto front does not directly correspond
to any specific notion of welfare or utility, making it diffi-
cult to interpret the societal implications of these policies.
Furthermore, without an explicit scalarization function to
aggregate preferences, decision-makers must choose among
Pareto-efficient policies without clear guidance on how to
weigh the trade-offs, which is often critical in real-world
applications where diverse preferences must be aggregated
into a single deployable policy. Additionally, the Pareto
front is typically large, making it prohibitively expensive to
compute in practice (Hayes et al., 2022).
A more refined notion of portfolio similar to the one we
study is the concept of convex coverage sets. However, this
concept is limited to weighted linear combinations of re-
ward functions (Roijers et al., 2013) and does not account
for p−means. As a result, existing MORL methods, whether
based on the Pareto frontier or weighted linear combinations,
do not provide guarantees with respect to p-mean welfare
functions. We include additional discussion comparing our
method with several well-known MORL algorithms pro-
posed in (Yang et al., 2019; Reymond et al., 2022; Alegre
et al., 2023; Yu et al., 2024) in Appendix C.
Portfolios in Optimization. In the optimization literature,
(Drygala et al., 2024) studied portfolios with stochastic guar-
antees for fixed objectives. Recent work in approximation
algorithms also explores the notions of small-sized portfo-
lios that approximately optimize a class of social welfare
functions (Gupta et al., 2023; 2025; Goel and Meyerson,
2006; Golovin et al., 2008; Chakrabarty and Swamy, 2019),
by exploiting the combinatorial properties of facility lo-
cation, scheduling and set cover problems. While these
works operate in well-structured combinatorial settings, our
work addresses significantly more complex landscape of
RL where the policy space is vast and computing optimal
policies is inherently challenging. This necessitates novel
algorithmic and theoretical advancements to efficiently con-
struct portfolios with strong guarantees.
3. Preliminaries
In this section, we provide preliminaries on MORL, p-mean
social welfare functions, and portfolios.
3.1. Multi-Objective Reinforcement Learning
We consider a multi-objective Markov decision process
(MDP), defined by the tuple M
=
(S, A, P, R
=
(Ri)i∈[N]), where S denotes a finite state space, A de-
notes a finite action space, and P : S × A →∆S is
the transition probability. Additionally, we assume that
we start in a fixed initial state s1 ∈S and H is the time
horizon. In the specific MORL context we consider, there
are N distinct stakeholders, each associated with a reward
function Ri : S × A →R>0 for i ∈[N]. A policy
π : S × [H] →∆(A) defines a distribution over actions at
a given time h ∈[H]. We use τ = (s1, a1, . . . , sH) to de-
note a trajectory, which is the sequence of states and actions
from time 1 to H. Throughout, we assume that all reward
functions are bounded:
Assumption 3.1 (Bounded Reward). There exist strictly
positive scalars U, L such that L ≤Ri(·) ≤U for all
i ∈[N]. We call κ := U/L the condition number of
rewards.
The N stakeholders could represent different entities de-
pending on the application; for example, different con-
3

--- Page 4 ---

Navigating the Social Welfare Frontier
stituent demographics of a democracy, stakeholders in a
company, or simply just abstract differences in values or
preferences.
3.2. Social Welfare Function
We consider the following family of social welfare functions
f(·, p) : RN
>0 →R>0 called the generalized p-mean. It is
defined for each p ∈[−∞, 1] and strictly each positive
vector x = (x1, . . . , xN) ∈RN
>0 as follows:
f(x, p) =





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





mini∈[N] xi
if p = −∞,

1
N
X
i∈[N]
xp
i


1/p
if p ̸∈{−∞, 0},

Y
i∈[N]
xi


1/N
if p = 0.
We also provide an illustrative example in Appendix B to
provide the intuitive impact of various p-mean objectives.
We will use the following monotonicity property:
Lemma 3.2 (Theorem 1, Chapter 3.3.1 (Bullen, 2003)). For
all strictly positive vectors x ∈RN
>0, and for all p, q ≤1
with p < q, we have f(x, p) ≤f(x, q).
The generalized p-means provides a method to aggregate
heterogeneous preferences by assigning a scalar value to any
policy π. We focus on two aggregation rules, denoted by ℓ∈
{1, 2}, that have been previously proposed in the literature.
Each combination of an aggregation rule ℓ∈{1, 2} and a
parameter p defines a specific aggregation function, denoted
as v(ℓ)(·, p). Given a trajectory τ = (s1, a1, . . . , sH, aH),
let Gi(τ) = PH
h=1 Ri(sh, ah), i ∈[N], represent the total
reward over the trajectory, and G(τ) ∈RN the vector with
Gi(τ) as its ith entry. The aggregation functions are defined
as follows:
v(1)(π, p) = Eτ∼π

f
 G(τ), p

,
(1)
v(2)(π, p) = f
 Eτ∼π[G(τ)], p

.
(2)
In the MORL literature, v(1)(·, p) is referred to as ex-
pected scalarized returns (ESR), while v(2)(·, p) is known
as scalarized expected returns (SER). In general, ESR is
preferred when the expected total reward from a single exe-
cution is the primary focus, whereas SER is more suitable
when policies are executed multiple times and rewards ac-
cumulate over iterations. Computing the optimal policy
for v(ℓ)(·, p) requires specialized algorithms different from
standard RL methods, which are not directly applicable. For
example, (Fan et al., 2023) and (Agarwal et al., 2022) de-
veloped algorithms for v(1)(·, p) and v(2)(·, p), respectively.
More detailed comparisons between these scalarization tech-
niques and their solution algorithms are available in Agarwal
et al. (2022), Roijers et al. (2013), R˘adulescu et al. (2019),
Agarwal et al. (2022), and Fan et al. (2023). While these
aggregation rules are often studied independently in MORL,
our work provides a unified framework applicable to both
methods. We show that the proposed algorithms apply to
both settings leveraging similar theoretical foundations.
3.3. Portfolio of Policies for All p-means
In this section, we introduce the key definitions for portfo-
lios. For brevity, we denote the maximum value function
v(ℓ)
∗
: [−∞, 1] →R defined as v(ℓ)
∗(p) := max
π∈Π v(ℓ)(π, p).
When ℓand Π are clear from context, we denote the optimal
policy for v(ℓ)(·, p) as πp.
Definition 3.3 (α-approximation1). Given a p ≤1, ag-
gregation rule ℓ∈{1, 2}, and an approximation factor
α ∈(0, 1), a policy π ∈Π is an α-approximation to the ag-
gregation function v(ℓ)(·, p) if the value v(ℓ)(π, p) achieved
by π is within factor α of the maximum achievable value of
v(ℓ)(·, p) by policies in Π, that is,
v(ℓ)(π, p) ≥α × max
π′∈Π v(ℓ)(π′, p) = α × v(ℓ)
∗(p).
When ℓand Π are clear from context, we say for brevity
that π is an α-approximate policy for p.
Definition 3.4 (Portfolio). Given aggregation rule ℓ∈
{1, 2} and approximation factor α ∈(0, 1), a set of policies
Π′ ⊆Π is called an α-approximate portfolio for aggrega-
tion functions v(ℓ) if for each p ≤1, there exists a policy in
Π′ that is an α-approximation to v(ℓ)(·, p).
4. Portfolio Algorithms
In this section, we present our main algorithmic and theoret-
ical results. Before presenting the details of our proposed
method, we first define the notion of an oracle, which serves
as a key component in our algorithm and analysis. Recall
that for a fixed p, aggregation function v(ℓ)(·, p), ℓ∈{1, 2},
and a given set of policies Π, the associated welfare max-
imizing policy can be obtained by solving the following
problem:
v(ℓ)
∗(p) = max
π∈Π v(ℓ)(π, p).
(3)
The algorithms we develop assume that (3) can be solved,
and we refer to each instance of solving (3) as an “ora-
cle”. This terminology is used to facilitate the discussion
of oracle complexity, which quantifies the number of times
Problem (3) must be solved to construct a portfolio.
1The α-approximation we refer to is distinct from the α-
fairness mentioned in Section 2. To avoid confusion, from this
point onward, all instances of α will exclusively refer to the ap-
proximation factor.
4

--- Page 5 ---

Navigating the Social Welfare Frontier
Algorithm 1 p-MEANPORTFOLIO(M, Π, ℓ, α)
input (i) MDP M = (S, A, P, R = (Ri)i∈[N]) with N
reward functions, (ii) feasible set of policies Π for M,
(iii) aggregation rule ℓ∈{1, 2}, and (iv) desired ap-
proximation factor α ∈(0, 1)
output α-approximate portfolio Π′ for the set of aggrega-
tion functions v(ℓ)(·, p), p ≤1, assuming oracle access
to solve problem (3)
1: initialize p0 = −
ln N
ln(1/α) and t = 0
2: initialize portfolio Π′ ←∅
3: while pt < 1 do
4:
add πpt := arg maxπ∈Πv(ℓ)(π, pt) to Π′
5:
pt+1 = LINESEARCH(v(ℓ), pt, Π, α)
6:
t ←t + 1
7: return Π′
Algorithm 2 LINESEARCH(v(ℓ), p, Π, α)
input (i) aggregation function v(ℓ) (ii) some p ∈(−∞, 1)
(iii) feasible set Π of policies, and (iv) desired approxi-
mation α ∈(0, 1)
output b∗> p such that πp := arg maxπ′∈Πv(ℓ)(π′, p) is
an α-approximation for v(ℓ)(·, q) for all q ∈[p, b∗]
1: a ←p and b ←1
2: initialize π = arg maxπ′∈Πv(ℓ)(π′, p)
3: while v(ℓ)(π, a) < α v(ℓ)
∗(b) do
4:
q ←a+b
2
5:
if v(ℓ)(π, a) ≥√α v(ℓ)
∗(q) then
6:
a ←q
7:
else
8:
b ←q
9: return b
If Π is defined as the set of all possible policies in the MDP,
as in the standard RL setting, each oracle call can be compu-
tationally expensive. Moreover, achieving exact optimality
for Problem (3) may not always be feasible due to limita-
tions in RL algorithms. This means that when measuring the
approximation factor of a policy π with respect to an aggre-
gation function v(ℓ)(·, p), the maximum value v(ℓ)
∗(p) might
not be attainable or computable. In this case, we approx-
imate v(ℓ)
∗(p) as the value achieved by applying the given
RL algorithm. This approach measures the approximation
factor relative to what is achievable using the algorithm at
hand.
In practice, Π may be a small set of pre-trained policies,
particularly in scenarios where training new policies is in-
feasible. In such cases, Problem (3) can be solved efficiently
by enumerating over the policies π ∈Π and using Monte
Carlo simulations to estimate the value v(ℓ)(π, p).
4.1. Algorithm p-MEANPORTFOLIO
In this section, we introduce p-MEANPORTFOLIO (Algo-
rithm 1), which constructs an α-approximate portfolio Π′
for all p ≤1. In Theorem 4.1, we establish formal bounds
on the portfolio size |Π′| and the number of oracle calls to
solve (3). The full proof is provided in Appendix A.
Theorem 4.1. Given an MDP M with N reward functions
with condition number κ, set Π of feasible policies, an
aggregation rule ℓ∈{1, 2}, and a desired approximation
factor α ∈(0, 1), Algorithm p-MEANPORTFOLIO returns
an α-approximate portfolio of policies Π′ for the set of
aggregation functions {v(ℓ)(·, p) : p ≤1}. Further,
1. The portfolio size
|Π′| = O

ln κ
ln(1/α)

,
2. The number of oracle calls by the algorithm is upper
bounded by
eO
(ln κ)2 ln ln N
ln(1/α)

,
where eO hides all lower order terms.
Here, we explain the high-level ideas behind the algorithm.
The algorithm iteratively chooses an increasing sequence of
p values p0 < p1 < . . . < pK = 1 using a line search sub-
routine (Algorithm 2). It ensures that πpt is α-approximate
for all p ∈[pt, pt+1], and that πp0 is α-approximate for all
p ∈[−∞, p0].
Line search. The line search subroutine works as follows:
given a p ≤1, it seeks to find some b∗≥p such that
πp is an α-approximation for all q ∈[p, b∗]. To achieve
this, it maintains lower and upper bounds a, b on b∗with
p ≤a < b ≤1 and iteratively refines these bounds.
At
each
iteration,
the
algorithm
checks
whether
v(ℓ)(πp, a)
≥
αv(ℓ)
∗(b) (line 3).
If this condition
holds, then by the monotonicity property of p-means
(Lemma 3.2), we must have:
v(ℓ)(πp, b) ≥v(ℓ)(πp, a) ≥α v(ℓ)
∗(b).
Then, this holds for any q ∈[a, b], implying that πp is α-
approximate across this interval. Therefore, this procedure
can safely output b∗= b. This establishes the correctness of
the algorithm, as the line search successfully identifies the
next p value if it terminates.
Bounds a, b are updated in each iteration as follows (lines
4-8): we query the value v(ℓ)
∗
(q) for q = a+b
2 . As before, if
v(ℓ)(πp, a) exceeds α times v(ℓ)
∗(q), then we know that πp
must be an α-approximation for any value in [a, q], and the
lower bound a can be tightened as a ←q. Otherwise, the
upper bound can be tightened as b ←q.
5

--- Page 6 ---

Navigating the Social Welfare Frontier
However, as we show in the formal proof in Appendix A,
we can in fact ensure faster convergence by slightly modi-
fying this step. Instead of checking whether v(ℓ)(πp, a) ≥
α × v(ℓ)
∗(q), we check the stronger condition v(ℓ)(πp, a) ≥
√α × v(ℓ)
∗(q). Since √α ≥α, this stricter condition does
not affect correctness but accelerates convergence.
Oracle complexity. We briefly sketch how we bound the
oracle complexity (i.e., number of oracle calls to solve Prob-
lem (3)) by bounding the number of oracle calls in each
run of LINESEARCH. As discussed, in each iteration of the
line search algorithm, the distance b −a is cut by half since
either b or a are updated to a+b
2 . As we show in Lemma
A.8, this implies that after j iterations of LINESEARCH, the
ratio v(ℓ)
∗(b)
v(ℓ)
∗(a) is upper bounded by ψ(κ, N, α) × 2−j, where
ψ is some function of condition number κ, dimension N,
and approximation factor α. By deriving a lower bound on
this ratio, we derive an upper bound on the total number of
iterations j.
4.2. Heuristic under a Budget Constraint
In p-MEANPORTFOLIO, we provide guarantees on the ap-
proximation factor α. However, achieving these guarantees
may require a large number of oracle calls to solve Prob-
lem (3) across different values of p, which can be impractical
when computational resources are severely limited.
One way to reduce oracle calls is to select a smaller α.
However, while Theorem 4.1 provides an upper bound on
the number of calls required, the exact number is difficult
to determine in advance, making it challenging to balance
computational cost with portfolio quality. Alternatively, a
budget on the total number of oracle calls can be imposed
along α, but this introduces its own trade-offs: if α is too
large, the algorithm may exhaust calls prematurely, leaving
parts of the p range unexplored; if α is too small, it may
progress to p = 1 too quickly, missing opportunities to
refine the portfolio.
To address this limitation, we propose the heuristic BUDGET-
CONSTRAINEDPORTFOLIO (Algorithm 3), designed for
scenarios with a strict budget K on oracle calls. Unlike
p-MEANPORTFOLIO, which selects p values in a mono-
tonically increasing order from −∞to 1, this algorithm
dynamically refines the search space based on observed ap-
proximation performance. It greedily targets regions where
the approximation factor is likely to be weakest, ensuring
efficient use of the limited oracle budget.
First, we describe the ideal version of this greedy approach.
After t oracle calls, let Π′
t denote our current portfolio. The
objective at each step is to identify the worst-case p value
where the approximation quality of Π′
t is the lowest by
solving the following problem:
Q(Π′
t) = minp≤1
maxπ∈Π′
t v(ℓ)(π, p)
v(ℓ)
∗(p)
.
(4)
However, solving this optimization problem exactly is com-
putationally infeasible, particularly since evaluating the ob-
jective for any new p would require an additional oracle
call. Instead, BUDGET-CONSTRAINEDPORTFOLIO approx-
imates this worst-case p using only the information gathered
from previous iterations, inspired by the theoretical princi-
ples of p-MEANPORTFOLIO.
After iteration t, the previously selected p values partition
the interval [∞, 1] into at most t + 1 disjoint intervals:
−∞< pm(1) < pm(2) < · · · < pm(t) ≤1.
Rather than solving Problem (4) exactly to pinpoint the
worst-case p, we instead aim to identify the interval where
the approximation quality is the weakest.
First, we rewrite Equation (4) by decomposing the mini-
mization over the intervals:
Q(Π′
t) ≈min
l∈[t−1]
"
min
p∈[pm(l),pm(l+1)]
maxπ∈Π′
t v(ℓ)(π, p)
v(ℓ)
∗(p)
#
.
The only approximation introduced in this decomposi-
tion arises from neglecting the intervals [−∞, pm(1)] and
[pm(t), 1]. To cover the first interval, we can initialize the
algorithm with a sufficiently small p1, guaranteeing that the
approximation factor remains well-controlled in this region
(Theorem 4.1). The second interval is covered by explicitly
setting p2 = 1.
For each interval [pm(l), pm(l+1)], we compute its interval
approximation factor, denoted as u(l), using the following
sequence of approximations:
min
p∈[pm(l),pm(l+1)]
maxπ∈Π′
t v(ℓ)(π, p)
v(ℓ)
∗(p)
≈
min
p∈[pm(l),pm(l+1)]
v(ℓ)(πpm(l), p)
v(ℓ)
∗(p)
≈v(ℓ)(πpm(l), pm(l+1))
v(ℓ)
∗(pm(l+1))
:= u(l).
The first approximation follows from the assumption
that each interval is well-covered by the policy trained
at its left endpoint, similar to the approach used in p-
MEANPORTFOLIO. The second approximation is justified
under the assumption that
v(ℓ)(πpm(l),p)
v(ℓ)
∗(p)
is a monotonically
decreasing function of p in the interval [pm(l), pm(l+1)].
Note that this assumption holds exactly when the inter-
val is sufficiently small, as this function is continuous in
6

--- Page 7 ---

Navigating the Social Welfare Frontier
Algorithm 3 BUDGETCONSTRAINEDPORTFOLIO
input (i) MDP M = (S, A, P, R = (Ri)i∈[N]) with N
reward functions, (ii) aggregation rule ℓ∈{1, 2}, (iii)
feasible set of policies Π for M, (iv) budget K, and (v)
initial p0
output A portfolio Π′
1: Initialize Π′ ←∅
2: for t = 1 to K do
3:
if t = 1 then
4:
pt ←p0
5:
else if t = 2 then
6:
pt ←1
7:
else
8:
compute u(l) for [pm(l), pm(l+1)], ∀l ∈[t −2]
9:
pt ←
pm(l∗)+pm(l∗+1)
2
, l∗= arg minl∈[t−2] u(l)
10:
Add policy πpt := arg maxπ∈Πv(ℓ)(π, pt) to Π′
11: return Π′
p (Lemma A.8) and attains its maximum value (= 1) at
p = pm(l).
To select the next p value, we identify the interval with
the worst (smallest) approximation factor and choose its
midpoint:
pt+1 = pm(l∗) + pm(l∗+1)
2
,
l∗= arg minl∈[t−1]u(l).
4.3. Warm-Start for Computational Efficiency
Both
p-MEANPORTFOLIO
and
BUDGET-
CONSTRAINEDPORTFOLIO involve repeatedly solving
Problem (3) for different p values.
To accelerate this
process, warm-starting is a natural choice. Specifically,
once the optimal policy πp for maxπ∈Π v(ℓ)(π, p) is
found, it can be used as a warm-starting point for solving
maxπ∈Π v(ℓ)(π, q), q > p, if q and p are close. Proposition
4.2 below offers a theoretical justification for this approach
by showing that v(ℓ)(πp, q) is close to the optimal value
v(ℓ)
∗(q) whenever p and q are close. The proof is deferred to
Appendix A.
Proposition 4.2. Let q > p. For ℓ∈{1, 2}, the following
inequality holds:
v(ℓ)
∗(q) −v(ℓ)(πp, q)
 ≤(q −p)UHκ ln κ,
where πp denotes the policy arg maxπ∈Πv(ℓ)(π, p).
5. Numerical Experiments
In this section,
we present the results of our nu-
merical experiments.
Additional details of the ex-
perimental setups and the environments are provided
in Appendix E. The code for our experiments can
be found at https://github.com/jaimoondra/
approximation-portfolios-for-rl/.
5.1. Experimental Setups
For a given α and MDP environment, we first compute a
portfolio using p-MEANPORTFOLIO and compare it against
two baseline approaches. Suppose p-MEANPORTFOLIO
generates a portfolio of size K. The first baseline selects
K values of p uniformly at random from [p0, 1] and com-
putes their optimal policies, where p0 matches that of p-
MEANPORTFOLIO. The second baseline randomly samples
K policies from Π. Since both baselines involve random-
ness, we generate 10 independent baseline portfolios for
each setting and report the average performance across these
runs. Finally, we run BUDGETCONSTRAINEDPORTFOLIO
with budget K.
To evaluate each portfolio Π′, we compute its approximation
factor Q(Π′) as defined in Equation (4). Since computing
this value exactly is infeasible, we approximate it using a
grid search over p, referring to it as the actual approxima-
tion. We also compare the number of oracle calls made by
p-MEANPORTFOLIO and BUDGETCONSTRAINEDPORTFO-
LIO. This procedure is repeated for varying α values.
5.2. Environments
We conduct experiments across three domains, ranging from
synthetic to real-world settings, as described below.
Taxi Environment. We consider a synthetic setting based
on the works of Dietterich (2000); Fan et al. (2022). The
taxi environment consists of a grid world where a taxi driver
serves passengers across N = 4 different source-destination
pairs. When the agent drops off a passenger at their destina-
tion, it earns a reward corresponding to that route. However,
since the taxi can only carry one passenger at a time, it must
decide which route to prioritize. A fair agent should serve
all source-destination pairs equitably, avoiding the neglect
of more challenging routes. We train a p-mean maximizing
policy using Welfare Q-Learning (Fan et al., 2022). Finally,
we experiment on v(1) and define Π as the set of all possible
policies in the MDP.
Resource Allocation after Natural Disaster. In this syn-
thetic setting, we have a set of N = 12 clusters of neigh-
borhoods impacted by a natural disaster. Each cluster is
characterized by average household income (high, middle,
low), proximity to critical infrastructure (near, far), and pop-
ulation density (high, low), along with distinct post-disaster
resource needs. Over a time horizon, a decision-maker must
decide how to allocate a limited number of resources to these
12 clusters. The reward function for each cluster is the aver-
age of the fraction of unmet need and the fraction of total
aid allocated to that cluster. We conduct experiments using
v(2), with Π defined as a finite set of pre-trained policies.
7

--- Page 8 ---

Navigating the Social Welfare Frontier
Healthcare Intervention. We consider a real-world health-
care intervention problem, modeled as an RMAB problem
described in Section 1.2 (Verma et al., 2024b). ARMMAN
(ARMMAN, 2024), an NGO based in India, runs large-scale
maternal and child mobile health programs. One of their
initiatives delivers critical health information via weekly
automated voice messages. To enhance engagement, a lim-
ited number of beneficiaries receive direct calls from health
workers each week, with call assignments determined by
a policy. The problem involves N = 59 reward functions,
each prioritizing different socio-demographic groups among
the beneficiaries. We conduct experiments using v(2), where
Π consists of a finite set of pre-trained policies. All experi-
ments are strictly secondary analyses and adhere to ethics
board approvals; for further discussion, refer to our impact
statement.
5.3. Results
Table 1 presents comparisons of the approximation quality
of p-MEANPORTFOLIO with random p sampling and ran-
dom policy sampling baselines, while Table 2 reports the
number of oracle calls made by p-MEANPORTFOLIO and
BUDGETCONSTRAINEDPORTFOLIO. Note that by design,
the number of calls for BUDGETCONSTRAINEDPORTFO-
LIO is always the same as the portfolio size.
Size.
The portfolios computed using Algorithm p-
MEANPORTFOLIO remain small while achieving a very
high approximation factor. Across all three environments,
the portfolio size never exceeds 10, yet still attains an ap-
proximation factor close to 1. This suggests that a small
portfolio is sufficient to effectively cover the entire spectrum
of p values ≤1.
Approximation Quality. The proposed algorithms achieve
significantly better approximation quality than both bench-
mark methods. In particular, p-MEANPORTFOLIO generally
attains the highest approximation quality, followed closely
by BUDGETCONSTRAINEDPORTFOLIO in most cases.
However, BUDGETCONSTRAINEDPORTFOLIO and random
p sampling occasionally outperform p-MEANPORTFOLIO.
This is because p-MEANPORTFOLIO selects policies solely
to meet the input approximation factor α, but has no incen-
tive or mechanism to surpass this approximation quality.
In contrast, BUDGETCONSTRAINEDPORTFOLIO fully uti-
lizes the input budget K, and strategically selects boundary
points first (a small initial p followed by p = 1). When
K is very small (1 or 2), this initial heuristic strategy can
provide more effective coverage across p ≤1, explain-
ing its occasional superior performance. Likewise, in rare
cases where K = 1, a randomly chosen p may happen
to yield better coverage than the single policy selected by
p-MEANPORTFOLIO.
Table 1. A comparison of actual approximation ratios across vari-
ous portfolio sizes for p-MEANPORTFOLIO, random policy sam-
pling, and random p sampling. p-MEANPORTFOLIO consistently
outperforms the other two methods across all portfolio sizes and
experiments.
Portfolio
Size
p-MEAN-
PORTFOLIO
Random
Policy
Sampling
Random
p
Sampling
Resource Allocation after Natural Disaster
1
0.706
0.534
0.832
2
0.904
0.568
0.890
3
0.999
0.591
0.892
4
1.000
0.609
0.888
Healthcare Intervention
1
0.924
0.479
0.913
2
0.982
0.545
0.941
3
0.982
0.589
0.929
4
0.982
0.625
0.947
5
0.993
0.635
0.957
6
0.999
0.647
0.962
7
1.000
0.667
0.953
Taxi Environment
1
0.66
0.24
0.66
2
0.61
0.31
0.61
3
0.97
0.54
0.65
8
0.87
0.71
0.67
10
0.99
0.60
0.65
Computational
Efficiency.
As
noted
earlier,
p-
MEANPORTFOLIO requires a large number of oracle calls
to produce a high-quality portfolio. In contrast, BUDGET-
CONSTRAINEDPORTFOLIO achieves comparable quality
while using significantly fewer oracle calls. This suggests
that when computational resources are limited, BUDGET-
CONSTRAINEDPORTFOLIO serves as a strong alternative
with good empirical performance.
Diversity. As we have shown in Figure 1 in Section 1.2,
portfolios can simplify policy deployment decisions by pre-
senting a small yet diverse set of policies. We also provide
the entire p values chosen by p-MEANPORTFOLIO in Ap-
pendix D, Table 4. We observe that the p values are quite
diverse, which corroborates the algorithm’s objective to
cover the entire p range only with these selected values.
Figures 3 and 4 further illustrate how the outcomes of the
optimal policies for different p values in the portfolio lead
to varying impacts for the stakeholders. Importantly, these
are not arbitrary policies but optimal policies for specific p
values, with approximation guarantees extending to other
ps as well.
3Here, we observe a drop in the actual approximation factor of
p-MEANPORTFOLIO when the portfolio size is 8. Although this
portfolio is computed using α = 0.9, its achieved approximation
is slightly lower. This discrepancy is likely due to the inherent
randomness in the RL algorithm and the challenges of computing
exact optimal policies in RL settings, as discussed in Section 4.
8

--- Page 9 ---

Navigating the Social Welfare Frontier
Table 2. A comparison of the number of oracle calls and actual
approximation ratios for p-MEANPORTFOLIO and BUDGETCON-
STRAINEDPORTFOLIO across different portfolio sizes. While
p-MEANPORTFOLIO often achieves slightly better approximation,
it requires significantly more oracle calls. 3
Portfolio
Size
p-MEANPORTFOLIO
BUDGETCONSTRAINED-
PORTFOLIO
Oracle
Calls
Actual
Approximation
Oracle
Calls
Actual
Approximation
Resource Allocation after Natural Disaster
1
1
0.706
1
0.885
2
7
0.904
2
0.921
3
18
0.999
3
0.921
4
50
1.000
4
0.921
Healthcare Intervention
1
2
0.924
1
0.938
2
7
0.982
2
0.938
3
11
0.982
3
0.938
4
19
0.982
4
0.938
5
23
0.993
5
0.986
6
46
0.999
6
0.986
7
61
1.000
7
0.993
Taxi Environment
1
17
0.66
1
0.66
2
30
0.61
2
0.61
3
44
0.97
3
0.92
8
118
0.87
8
0.90
10
144
0.99
10
0.92
6. Conclusion
In this paper, we studied the concept of an α-approximate
portfolio in MORL for generalized p-means. We proposed
an algorithm to compute α-approximate portfolios and es-
tablished theoretical guarantees on the trade-offs among
α, portfolio size, and the number of oracle calls. Addi-
tionally, we presented a theoretical analysis of warm-start
techniques and developed an efficient heuristic algorithm.
Our numerical experiments demonstrated that the proposed
methods successfully compute compact portfolios that effec-
tively capture the entire spectrum of p values, empowering
decision-makers to make informed decisions.
Acknowledgments
We thank NSF AI Institute for Societal Decision Making
(AI-SDM) Award No. 2229881, ONR MURI N00014-24-1-
2742, and NSF CAREER 2239824 for their support.
Impact Statement
Our work studies the setting where a deployed RL policy
impacts multiple stakeholders differently, a scenario that
arises in various societal applications, including healthcare
and LLMs. By summarizing the space of policies induced
under different p-values, our proposed approach aims to
assist decision-makers in making informed and equitable
choices. Furthermore, this work has the potential to stim-
ulate discussions within the machine learning community
about the complexities and pluralities of social welfare no-
tions, and the importance of addressing them. However,
our focus is limited to p-means social welfare functions,
which may not fully capture all dimensions of fairness in
real-world scenarios.
Our experiments use real-world healthcare data provided
by the NGO ARMMAN. These experiments are strictly
secondary analyses, with no real-world deployment of the
proposed algorithm or baseline methods. All data usage
complied with ARMMAN’s ethics board approvals, and
data exchange and analysis followed their ethics review
committee’s guidelines, including privacy, informed con-
sent, and anonymization. All of the analyses is conducted
in close collaboration with ARMMAN.
This work belongs to the broader area of algorithmic
decision-making, where deployment decisions can have real-
world implications. We emphasize the importance of not
relying on this study in isolation. Responsible deployment
requires comprehensive field testing and human oversight.
Moreover, we acknowledge broader challenges inherent in
algorithmic decision-making, including potential biases in
data, inaccuracies in the underlying mathematical models,
accountability issues, and concerns related to consent and
privacy. Addressing these challenges is essential to ensuring
that algorithmic decisions are ethically sound.
References
Mridul Agarwal, Vaneet Aggarwal, and Tian Lan. Multi-
objective reinforcement learning with non-linear scalar-
ization.
In Proceedings of the 21st International
Conference on Autonomous Agents and Multiagent
Systems, AAMAS ’22, page 9–17, Richland, SC, 2022.
International Foundation for Autonomous Agents and
Multiagent Systems. ISBN 9781450392136.
Parand A. Alamdari, Soroush Ebadian, and Ariel D. Pro-
caccia. Policy aggregation. In The Thirty-eighth Annual
Conference on Neural Information Processing Systems,
9

--- Page 10 ---

Navigating the Social Welfare Frontier
2024. URL https://openreview.net/forum?
id=ybiUVIxJth.
Lucas N. Alegre, Diederik M. Roijers, Ann Nowé, Ana
L. C. Bazzan, and Bruno C. da Silva. Sample-efficient
multi-objective learning via generalized policy improve-
ment prioritization. In Proc. of the 22nd International
Conference on Autonomous Agents and Multiagent
Systems (AAMAS), 2023.
ARMMAN. Armman: Advancing reduction in mortality
and morbidity of mothers, children, and neonates, 2024.
URL https://armman.org/.
P.S Bullen.
Handbook of Means and Their Inequalities.
Mathematics and Its Applications ; 560. Springer Nether-
lands : Imprint: Springer, Dordrecht, 2nd ed. 2003. edi-
tion, 2003.
Deeparnab Chakrabarty and Chaitanya Swamy. Approxima-
tion algorithms for minimum norm and ordered optimiza-
tion problems. In Proceedings of the 51st Annual ACM
SIGACT Symposium on Theory of Computing, pages
126–137, 2019.
Souradip Chakraborty, Jiahao Qiu, Hui Yuan, Alec Kop-
pel, Dinesh Manocha, Furong Huang, Amrit Bedi, and
Mengdi Wang.
MaxMin-RLHF: Alignment with di-
verse human preferences.
In Ruslan Salakhutdinov,
Zico Kolter, Katherine Heller, Adrian Weller, Nuria
Oliver, Jonathan Scarlett, and Felix Berkenkamp, edi-
tors, Proceedings of the 41st International Conference
on Machine Learning, volume 235 of Proceedings of
Machine Learning Research, pages 6116–6135. PMLR,
21–27 Jul 2024.
URL https://proceedings.
mlr.press/v235/chakraborty24b.html.
Jingdi Chen, Yimeng Wang, and Tian Lan. Bringing fair-
ness to actor-critic reinforcement learning for network
utility optimization. In IEEE INFOCOM 2021 - IEEE
Conference on Computer Communications, pages 1–10,
2021. doi: 10.1109/INFOCOM42981.2021.9488823.
Cyrus Cousins. Revisiting fair-pac learning and the axioms
of cardinal welfare. In Francisco Ruiz, Jennifer Dy, and
Jan-Willem van de Meent, editors, Proceedings of The
26th International Conference on Artificial Intelligence
and Statistics, volume 206 of Proceedings of Machine
Learning Research, pages 6422–6442. PMLR, 25–27 Apr
2023. URL https://proceedings.mlr.press/
v206/cousins23a.html.
Cyrus Cousins, Kavosh Asadi, Elita Lobo, and Michael
Littman. On welfare-centric fair reinforcement learning.
Reinforcement Learning Journal, 3:1124–1137, 2024.
Thomas G Dietterich. Hierarchical reinforcement learning
with the maxq value function decomposition. Journal of
artificial intelligence research, 13:227–303, 2000.
Marina Drygala, Silvio Lattanzi, Andreas Maggiori, Mil-
tiadis Stouras, Ola Svensson, and Sergei Vassilvit-
skii.
Data-driven solution portfolios.
arXiv preprint
arXiv:2412.00717, 2024.
Zimeng Fan, Nianli Peng, Muhang Tian, and Brandon Fain.
Welfare and fairness in multi-objective reinforcement
learning. arXiv preprint arXiv:2212.01382, 2022.
Ziming Fan, Nianli Peng, Muhang Tian, and Brandon
Fain. Welfare and fairness in multi-objective reinforce-
ment learning. In Proceedings of the 2023 International
Conference on Autonomous Agents and Multiagent
Systems, AAMAS ’23, page 1991–1999, Richland, SC,
2023. International Foundation for Autonomous Agents
and Multiagent Systems. ISBN 9781450394321.
Ashish Goel and Adam Meyerson. Simultaneous optimiza-
tion via approximate majorization for concave profits or
convex costs. Algorithmica, 44:301–323, 2006.
Daniel Golovin, Anupam Gupta, Amit Kumar, and Kanat
Tangwongsan.
All-norms and all-l_p-norms approxi-
mation algorithms. In IARCS Annual Conference on
Foundations of Software Technology and Theoretical
Computer Science (2008). Schloss-Dagstuhl-Leibniz
Zentrum für Informatik, 2008.
Swati Gupta, Jai Moondra, and Mohit Singh.
Which
lp norm is the fairest? Approximations for fair facil-
ity location across all "p". In Proceedings of the 24th
ACM Conference on Economics and Computation, EC
’23, page 817, New York, NY, USA, 2023. Associa-
tion for Computing Machinery. ISBN 9798400701047.
doi: 10.1145/3580507.3597664. URL https://doi.
org/10.1145/3580507.3597664.
Swati Gupta, Jai Moondra, and Mohit Singh.
Balanc-
ing notions of equity: Trade-offs between fair portfo-
lio sizes and achievable guarantees. In Proceedings of
the 2025 Annual ACM-SIAM Symposium on Discrete
Algorithms (SODA), 2025.
URL https://arxiv.
org/abs/2311.03230.
Hao Hao, Changqiao Xu, Wei Zhang, Shujie Yang, and
Gabriel-Miro Muntean. Computing offloading with fair-
ness guarantee: A deep reinforcement learning method.
IEEE Transactions on Circuits and Systems for Video
Technology, 33(10):6117–6130, 2023.
doi: 10.1109/
TCSVT.2023.3255229.
Conor F. Hayes, Roxana R˘adulescu, Eugenio Bargiacchi, Jo-
han Källström, Matthew Macfarlane, Mathieu Reymond,
10

--- Page 11 ---

Navigating the Social Welfare Frontier
Timothy Verstraeten, Luisa M. Zintgraf, Richard Daze-
ley, Fredrik Heintz, Enda Howley, Athirai A. Irissappane,
Patrick Mannion, Ann Nowé, Gabriel Ramos, Marcello
Restelli, Peter Vamplew, and Diederik M. Roijers. A
practical guide to multi-objective reinforcement learn-
ing and planning. Autonomous Agents and Multi-Agent
Systems, 36(1):26, April 2022.
Peizhong Ju, Arnob Ghosh, and Ness Shroff. Achieving fair-
ness in multi-agent MDP using reinforcement learning.
In The Twelfth International Conference on Learning
Representations, 2024. URL https://openreview.
net/forum?id=yoVq2BGQdP.
Debmalya Mandal and Jiarui Gan. Socially fair reinforce-
ment learning, 2023. URL https://arxiv.org/
abs/2208.12584.
Hervé Moulin. Fair Division and Collective Welfare. The
MIT Press, January 2003.
Christos H Papadimitriou and John N Tsitsiklis. The com-
plexity of optimal queuing network control. Mathematics
of Operations Research, 24(2):293–305, 1999.
Kanad Shrikar Pardeshi, Itai Shapira, Ariel D. Procaccia,
and Aarti Singh.
Learning social welfare functions.
In The Thirty-eighth Annual Conference on Neural
Information Processing Systems, 2024. URL https:
//openreview.net/forum?id=7O6KtaAr8n.
Simone Parisi, Matteo Pirotta, Nicola Smacchia, Luca
Bascetta, and Marcello Restelli.
Policy gradient ap-
proaches for multi-objective sequential decision mak-
ing. In 2014 International Joint Conference on Neural
Networks (IJCNN), pages 2323–2330, 2014. doi: 10.
1109/IJCNN.2014.6889738.
Chanwoo Park, Mingyang Liu, Dingwen Kong, Kaiqing
Zhang, and Asuman Ozdaglar. RLHF from heteroge-
neous feedback via personalization and preference ag-
gregation, 2024. URL https://arxiv.org/abs/
2405.00254.
Julien Perez, Cécile Germain-Renaud, Balázs Kégl, and
Charles Loomis.
Responsive elastic computing.
In
Proceedings of the 6th International Conference Industry
Session on Grids Meets Autonomic Computing, GMAC
’09, page 55–64, New York, NY, USA, 2009. Associa-
tion for Computing Machinery. ISBN 9781605585789.
doi: 10.1145/1555301.1555311. URL https://doi.
org/10.1145/1555301.1555311.
Roxana R˘adulescu, Patrick Mannion, Diederik M. Roijers,
and Ann Nowé. Multi-objective multi-agent decision
making: a utility-based analysis and survey. Autonomous
Agents and Multi-Agent Systems, 34(1):10, December
2019.
Mathieu Reymond, Eugenio Bargiacchi, and Ann Nowé.
Pareto conditioned networks.
In Proceedings of the
21st International Conference on Autonomous Agents
and Multiagent Systems, AAMAS ’22, page 1110–1118,
Richland, SC, 2022. International Foundation for Au-
tonomous Agents and Multiagent Systems.
ISBN
9781450392136.
Kevin W. S. Roberts. Interpersonal Comparability and So-
cial Choice Theory. The Review of Economic Studies,
47(2):421–439, January 1980.
Diederik M. Roijers, Peter Vamplew, Shimon Whiteson,
and Richard Dazeley. A survey of multi-objective sequen-
tial decision-making. J. Artif. Int. Res., 48(1):67–113,
October 2013. ISSN 1076-9757.
Kristof Van Moffaert and Ann Nowé. Multi-objective rein-
forcement learning using sets of pareto dominating poli-
cies. J. Mach. Learn. Res., 15(1):3483–3512, January
2014. ISSN 1532-4435.
Shresth Verma, Gargi Singh, Aditya Mate, Paritosh Verma,
Sruthi Gorantla, Neha Madhiwalla, Aparna Hegde, Divy
Thakkar, Manish Jain, Milind Tambe, et al. Expanding
impact of mobile health programs: Saheli for maternal
and child care. AI Magazine, 44(4):363–376, 2023.
Shresth Verma, Niclas Boehmer, Lingkai Kong, and Milind
Tambe. Balancing act: Prioritization strategies for LLM-
designed restless bandit rewards, 2024a. URL https:
//arxiv.org/abs/2408.12112.
Shresth Verma, Gargi Singh, Aditya Mate, Paritosh Verma,
Sruthi Gorantla, Neha Madhiwalla, Aparna Hegde, Divy
Thakkar, Manish Jain, Milind Tambe, and Aparna
Taneja. Increasing impact of mobile health programs:
Saheli for maternal and child care.
Proceedings of
the AAAI Conference on Artificial Intelligence, 37(13):
15594–15602, Jul. 2024b.
P. Whittle. Restless bandits: Activity allocation in a chang-
ing world. Journal of Applied Probability, 25:287–298,
1988. ISSN 00219002. URL http://www.jstor.
org/stable/3214163.
Qingqing Wu, Yong Zeng, and Rui Zhang.
Joint tra-
jectory and communication design for multi-uav en-
abled wireless networks. IEEE Transactions on Wireless
Communications, 17(3):2109–2121, 2018. doi: 10.1109/
TWC.2017.2789293.
Runzhe Yang, Xingyuan Sun, and Karthik Narasimhan. A
generalized algorithm for multi-objective reinforcement
learning and policy adaptation. Curran Associates Inc.,
Red Hook, NY, USA, 2019.
11

--- Page 12 ---

Navigating the Social Welfare Frontier
Guanbao Yu, Umer Siddique, and Paul Weng. Fair deep
reinforcement learning with generalized gini welfare func-
tions. In Francesco Amigoni and Arunesh Sinha, editors,
Autonomous Agents and Multiagent Systems. Best and
Visionary Papers, pages 3–29, Cham, 2024. Springer Na-
ture Switzerland.
Huiying Zhong, Zhun Deng, Weijie J. Su, Zhiwei Steven
Wu, and Linjun Zhang. Provable multi-party reinforce-
ment learning with diverse human feedback, 2024. URL
https://arxiv.org/abs/2403.05006.
12

--- Page 13 ---

Navigating the Social Welfare Frontier
A. Omitted Proofs
We include omitted proofs and various lemmas here.
A.1. Proof of Theorem 4.1
Our first lemma shows establishes the monotonicity of aggregation functions v(ℓ) in p:
Lemma A.1. For any fixed policy π ∈Π, v(ℓ)(π, p) is monotone increasing in p for ℓ∈{1, 2}.
Proof. ℓ= 1: For any τ ∼π, Lemma 3.2 implies that f(G(τ), p) is monotone increasing in p. Therefore,
v(1)(π, p) = Eτ∼π[f(G(τ), p)]
is monotone increasing in p.
ℓ= 2: Denote x = Eτ∼π[G(τ)]. Then the monotonicity of v(2)(π, p) = f(x, p) follows directly from Lemma 3.2.
The following corollary follows immediately:
Corollary A.2. v(ℓ)
∗(p) := maxπ∈Π v(ℓ)(π, p) is monotone increasing in p for ℓ∈{1, 2}.
The following two lemmas show that the p-mean for p = −∞is α-approximated by the p0-mean where p0 = −
ln N
ln(1/α), so
we can effectively restrict to [−p0, 1] when finding portfolios:
Lemma A.3. Given a vector x ∈RN
>0 and α ∈(0, 1), define p0 = −
ln N
ln(1/α). Then,
f(x, −∞) ≥α · f(x, p)
∀p ≤p0.
Proof. Suppose 0 < x1 ≤. . . ≤xn, so that f(x, −∞) = minj∈[N] xj = x1. Given p ≤p0, denote q = −p ≥
ln N
ln(1/α).
Then, since
f(x, p) =

1
N
X
j∈[N]
xp
j


1/p
=
1

1
N
P
j∈[N]
1
xq
j
1/q =
1
1
x1

1
N
P
j∈[N]

x1
xj
q1/q ,
we get
1
f(x, p) ≥1
x1
 1
N ×
x1
x1
q1/q
= N 1/p
x1
≥N 1/p0
x1
=
α
f(x, −∞),
or that f(x, −∞) ≥α · f(x, p).
Lemma A.4. Given an MDP M with N reward functions, set Π of feasible policies, and an approximation factor
α ∈(0, 1), denote p0 = −
ln N
ln(1/α). Then, for a given aggregation rule ℓ∈{1, 2}, policy π0 = arg maxπ∈Πv(ℓ)(π, p0) is an
α-approximation for all p ≤p0. That is,
v(ℓ)(π0, p) ≥v(ℓ)
∗(p) = max
π∈Π v(ℓ)(π, p)
∀p ≤p0.
Proof. ℓ= 1: From Lemma A.3, for all p ≤p0, we get
v(1)(π0, p) ≥v(1)(π0, −∞)
(Lemma A.1)
= Eτ∼π[f(G(τ), −∞)]
(eqn.(1))
≥α · Eτ∼π[f(G(τ), p0)]
(Lemma A.3)
= α · v(1)(π0, p0)
(eqn.(1))
= α · max
π∈Π ·v(1)(π, p0)
≥α · max
π∈Π v(1)(π, p)
(Lemma A.1).
The result for ℓ= 2 follows similarly and is omitted.
13

--- Page 14 ---

Navigating the Social Welfare Frontier
The following three lemmas establish guarantees on LINESEARCH:
Lemma A.5. Suppose LINESEARCH (Algorithm 2) on input v(ℓ), p, Π, α returns b∗∈[p, 1]. Then, either b∗= 1, or the
policy π := arg maxπ∈Πv(ℓ)(π, p) satisfies
v(ℓ)
∗(p)
√α
≤v(ℓ)
∗(b∗) ≤v(ℓ)(π, b∗)
α
.
Proof. If LINESEARCH(v(ℓ), p, Π, α) does not return b∗= 1, then we must have that p-MEANPORTFOLIO enters the while
loop (step 2) at least once. In particular,
v(ℓ)
∗(p) = v(ℓ)(π, p) < α v(ℓ)
∗(b∗) < √α v(ℓ)
∗(b∗).
This proves the first inequality. For the second inequality, notice that the algorithm terminates only when v(ℓ)(π, a) ≥
α v(ℓ)
∗(b∗). As can be easily checked, the algorithm maintains the invariant a ≥p. Therefore, by Lemma A.1,
v(ℓ)(π, b∗) ≥v(ℓ)(π, a) ≥α v(ℓ)
∗(b∗).
Lemma A.6. Algorithm LINESEARCH maintains the following invariant at all times: v(ℓ)(π, a) ≥√α v(ℓ)
∗(a).
Proof. Initially, p = a, and therefore π := arg maxπ′∈Πv(ℓ)(π′, p) satisfies v(ℓ)(π, p) = v(ℓ)
∗(p) ≥√α v(ℓ)
∗(p) since
α ∈(0, 1).
Further, the algorithm only updates a ←q in step 2 when v(ℓ)(π, a) ≥√α v(ℓ)
∗(q). Since q ≥a, we get from Lemma A.1
that v(ℓ)(π, q) ≥v(ℓ)(π, a), thus finishing the proof.
Lemma A.7. Algorithm LINESEARCH on input p, v(ℓ), Π, α returns b∗> p such that π := arg maxπ′∈Πv(ℓ)(π, p) is an
α-approximation for all q ∈[p, b∗], i.e., v(ℓ)(π, q) ≥α v(ℓ)
∗(q) for all such q.
Proof. LINESEARCH starts with a ←p and keeps increasing a ←q whenever v(ℓ)(π, a) ≥√α v(ℓ)
∗(q) for q = a+b
2 . In
particular, whenever a is increased, we get that for all q′ ∈[a, (a + b)/2], from Lemma A.1,
v(ℓ)(π, q′) ≥v(ℓ)(π, a) ≥√α v(ℓ)
∗(π, (a + b)/2) ≥√α v(ℓ)
∗(π, q′) > α v(ℓ)
∗(q′).
That is, at all times, the algorithm maintains the invariant that π is an α-approximation for all q′ ∈[p, a]. Further, the
algorithm terminates at b = b∗when v(ℓ)(π, a) ≥v(ℓ)
∗(b∗), i.e., for all q′ ∈[a, b∗], we get
v(ℓ)(π, q′) ≥v(ℓ)(π, a) ≥α v(ℓ)
∗(b∗) ≥α v(ℓ)
∗(q′).
The next lemma bounds the slope of the logarithm of the p-mean function and consequently the slope of ln v(ℓ)
∗(p):
Lemma A.8.
1. For any x ∈RN
>0, such that HL ≤xi ≤HU for all i ∈[N], define g(x, p) := ln f(x, p) =
1
p ln

1
N
P
i∈[N] xp
i

. Then, if L ≤xi ≤U with condition number κ := U
L , we have
dg(x, p)
dp
≤κ ln κ.
2. For any given policy π ∈Π and aggregation rule ℓ∈{1, 2}, we have
d(ln v(ℓ)(π,p))
dp
≤κ ln κ, where κ is the condition
number defined in Assumption 3.1.
3. For a given aggregation rule ℓ∈{1, 2}, define w(p) := ln v(ℓ)
∗(p). Then, for all distinct p, q ≤1,
w(q) −w(p)
q −p
≤κ ln κ.
14

--- Page 15 ---

Navigating the Social Welfare Frontier
Proof. Part 1. Note that g(βx, p) = ln β + g(x, p) for all x ∈RN
>0, p ≤1, and β > 0. Therefore, we can assume without
loss of generality that LH = 1 and UH = UH
LH = κ.
That is, assume without of generality that 1 ≤x1 ≤. . . ≤xN ≤κ. Since g(x, p) = −ln N
p
+ 1
p ln
P
i∈[N] xp
i

, we get
that pg(x, p) = −ln N + ln
P
i∈[N] xp
i

. Therefore,
g(x, p) + pdg(x, p)
dp
=
P
i(ln x) · xp
i
P
i xp
i
.
(5)
Since ln t is concave in t, we get that
pg(x, p) = ln
 
1
N
X
i
xp
i
!
≥1
N
X
i
ln xp
i = p
N
X
i
ln xi.
Therefore, we get
g(x, p)
(
≥1
N
P
i ln xi
if p ≥0,
≤1
N
P
i ln xi
if p < 0.
(6)
Denote µp = 1
N
P
i∈[N] xp
i .
Case A: p ∈[0, 1].
Plugging this back into eqn. (5), we get
pdg(x, p)
dp
≤
P
i(ln xi) · xp
i
Nµp
−1
N
X
i
ln xi = 1
N
 X
i
ln xi
xp
i
µp
−1
!
.
Since 1 ≤xi ≤κ for all i, we have 0 ≤ln xi ≤ln κ for all i. Further, since xN ≥xi, we get that
Np dg(x, p)
dp
≤
X
i
ln xi
xp
i
µp
−1

≤ln κ
X
i:xp
i ≥µp
xp
N
µp
−1

≤N ln κ
xp
N
µp
−1

.
(7)
Now, since µp is the mean of xp
i , i ∈[N], we must have that µp = θp for some 1 ≤θ ≤κ. Substituting this, we get
Np dg(x,p)
dp
≤N(ln κ) ((xN/θ)p −1). Since xN
θ ≤κ
1 = κ and the derivative of αp with respect to α is pαp−1, we get
((xN/θ)p −1) ≤(κp −1)
=
Z κ
1
p · αp−1 dα
≤
Z κ
1
p · 1p−1 dα
(since p −1 ≤0 and so αp−1 is nonincreasing in p)
≤p(κ −1) ≤pκ.
(since p ≥0)
Plugging this back into eqn. (7), we get
pdg(x, p)
dp
≤pκ ln κ,
or that dg(x,p)
dp
≤κ ln κ for all p ∈[0, 1].
Case B: p < 0.
As before, plugging bound (6) into eqn. (5), we get
pdg(x, p)
dp
≥
P
i(ln xi) · xp
i
Nµp
−1
N
X
i
ln xi = 1
N
 X
i
ln xi
xp
i
µp
−1
!
= −1
N
 X
i
ln xi

1 −xp
i
µp
!
.
That is, since p < 0,
dg(x, p)
dp
≤
1
(−p)N
 X
i
ln xi

1 −xp
i
µp
!
≤
ln R
(−p)N
X
i:xp
i ≤µp

1 −xp
i
µp

≤
ln R
(−p)N ×N

1 −xp
N
µp

= ln κ
(−p)

1 −xp
N
µp

.
15

--- Page 16 ---

Navigating the Social Welfare Frontier
Denote −p = q; then q > 0. As before, µp = θp for some 1 ≤θ ≤N, and so we have
dg(x, p)
dp
≤ln κ
q

1 −θq
xq
N

≤ln κ
q

1 −1
κq

.
For q ≥1 (i.e., for p ≤−1), this is at most ln κ. For q ∈[0, 1], we will bound this in a manner similar to Case A:
dg(x, p)
dp
≤ln κ
q
Z 1
1/κ
qαq−1 dα
≤ln κ
Z 1
1/κ
1
κq−1 dα
≤(ln κ) × κ1−q ≤κ ln κ.
Part 2. ℓ= 1. Given any trajectory τ, for the vector G(τ) ∈[LH, UH]N, we get from Part 1 that
d (ln f(G(τ), p))
dp
≤κ ln κ.
Consequently, for any policy π, we get for v(1)(π, p) = Eτ∼π [f(G(τ), p)] using linearity of expectation that
d
 ln v(1)(π, p)

p
= Eτ∼π
d (ln f(G(τ), p))
dp

≤Eτ∼π [κ ln κ] = κ ln κ.
ℓ= 2. Follows by taking x = Eτ∼π[G(τ)] in Part 1.
Part 3. Note that w(p) = ln v(ℓ)
∗(p) = ln maxπ∈Π v(ℓ)(π, p) = maxπ∈Π ln v(ℓ)(π, p). Given distinct p, q ≤1, denote
πp = arg maxπ∈Π ln v(ℓ)(π, p). Then, by Part 1,
w(q) −w(p)
q −p
=
 maxπ∈Π ln v(ℓ)(π, q)

−ln v(ℓ)(πp, p)
q −p
≤ln v(ℓ)(πp, q) −ln v(ℓ)(πp, p)
q −p
≤κ ln κ.
We are ready to prove Theorem 4.1 that gives guarantees for p-MEANPORTFOLIO (Algorithm 1).
Proof of Theorem 4.1. We prove that (correctness) the set Π′ of policies output by the algorithm is indeed an α-approximate
portfolio, (size bound) |Π′| = O

ln κ
ln(1/α)

, and (oracle complexity) the number of oracle calls to Problem (3) is upper
bounded by
O

(ln κ)2 ln ln N
ln(1/α) ln ln(1/α)

.
(8)
We note that this size bound can be tightened slightly to O

(ln κ)(ln κ+ln ln N)
ln(1/α) ln ln(1/α)

; we present the the above cleaner bound for
simplicity.
Correctness.
Suppose the algorithm returns Π′ = {π0, π1, . . . , πK} such that πt = arg maxπ∈Πv(ℓ)(π, pt) with
−
ln N
ln(1/α) = p0 < p1 < . . . < pK = 1.
Lemma A.4 shows that π0 is an α-approximation for all p ≤p0. It is therefore sufficient to prove that for all t ∈[0, K −1],
policy πt is an α-approximation for all p ∈[pt, pt+1]. Since pt+1 = LINESEARCH(v(ℓ), pt, Π, α), Lemma A.7 implies this.
Size bound.
Note that by definition, pt+1 = LINESEARCH(v(ℓ), pt, Π, α). Therefore, from Lemma A.5, we have that πt
satisfies v(ℓ)
∗(pt+1) ≥v(ℓ)
∗(pt)
√α
for all t except possibly t = K −1. Therefore,
v(ℓ)
∗(pK) ≥v(ℓ)
∗(pK−1) ≥
 1
α
(K−1)/2
v(ℓ)
∗(p0) =
 1
α
(K−1)/2
v(ℓ)
∗(−∞).
However, v(ℓ)
∗(pK) ≤HU and v(ℓ)
∗(p0) ≥HL, so that v(ℓ)
∗(pK)
v(ℓ)
∗(p0) ≤U
L = κ, and therefore,
K −1
2
≤log(1/α) κ =
ln κ
ln(1/α).
16

--- Page 17 ---

Navigating the Social Welfare Frontier
Oracle complexity.
To bound the oracle complexity, we will show that each run of LINESEARCH calls the oracle to solve
Problem (3) at most O (ln (κ|p0|)) times, where p0 = −
ln N
ln(1/α) is the first iterate in p-MEANPORTFOLIO and κ = U/L is
the condition number of the rewards. Since LINESEARCH is called at most O(K) = O

ln κ
ln(1/α)

times, this implies the
bound (8).
To bound the number of oracle calls in LINESEARCH, we will use Lemma A.8.3 that upper bounds the slope of w(p) :=
ln v(ℓ)
∗(p) by m := κ ln κ. Suppose, for a given p ≥p0 = −
ln N
ln(1/α) that LINESEARCH on input p, α finished in j iterations.
Then, we have the following for LINESEARCH:
1. p0 ≤p ≤a < b ≤1 at all times, and
2. except in the last iteration, we have v(π, a) < α v∗(b) (otherwise LINESEARCH terminates by step 2).
Denote by a(j−1), b(j−1) the value of a, b in iteration j −1. Then, since b −a is halved in each iteration, we must have
0 < b(j−1) −a(j−1) = (1 −p)2−(j−1) ≤(1 −p0)2−(j−1) ≤4 ln N
ln(1/α)2−j.
However, since the algorithm does not terminate in step j −1, as discussed, we must also have that
v(ℓ)(π, a(j−1)) < α · v(ℓ)
∗(b(j−1)).
(9)
From Lemma A.8, we get that
ln v(ℓ)
∗(b(j−1))
v(ℓ)
∗(a(j−1))
≤(κ ln κ)(b(j−1) −a(j−1)) ≤4κ(ln κ)(ln N)
ln(1/α)
2−j.
(10)
However, from Lemma A.6, we get v(ℓ)(π, a(j−1)) ≥√α v(ℓ)
∗(a(j−1)). Putting these together with eqns. (9) and (10), we
get that
1
2 ln(1/α) ≤4κ(ln κ)(ln N)
ln(1/α)
2−j.
Therefore,
2j ≤8κ(ln κ)(ln N)
(ln(1/α))2
.
Equivalently, the number of iterations j in LINESEARCH is bounded by
O

ln
 κ ln N
ln(1/α)

= O
(ln κ)(ln ln N)
ln ln(1/α)

.
A.2. Proof of Proposition 4.2
We prove the proposition assuming the aggregation function v(1)(π, p). The same proof applies for v(2)(π, p).
Proof.
max
π∈Π Eτ∼π [f(G(τ), q)] −Eτ∼πp [f(G(τ), q)]
≤max
π∈Π Eτ∼π [f(G(τ), q)] −Eτ∼πp [f(G(τ), p)]
= max
π∈Π Eτ∼π [f(G(τ), q)] −max
π∈Π Eτ∼π [f(G(τ), p)]
≤max
π∈Π Eτ∼π [f(G(τ), q) −f(G(τ), p)]
≤max
π∈Π Eτ∼π

(q −p) max
r∈(p,q)
df(G(τ), r)
dr

≤max
π∈Π Eτ∼π [(q −p)κ ln κHU]
= (q −p)UHκ ln κ.
17

--- Page 18 ---

Navigating the Social Welfare Frontier
(a) Entries of A, B, C
(b) p−means at selected p values.
(c) p−means across different p values.
Figure 2. Side-by-side comparison of entries and p-means for vectors A, B, C.
The first inequality follows from Lemma 3.2, which ensures monotonicity in the p parameter. The equality comes directly
from the definition of πp, as it maximizes v(1)(π, p). The second inequality uses the properties of the maximum function.
The next line applies the mean-value theorem to the function f(G(τ), p) with respect to the variable p. The subsequent
bound follows from the boundedness of the reward function and Lemma A.8. Finally, the terms involving κ are replaced
with L and U for conciseness.
B. Generalized p−Means: Illustrative Example
To clarify the meaning behind p-means, we constructed an illustrative example in Figure 2. In this example, three vectors A,
B and C represent different policies, where each vector’s ith entry is the total reward for the ith stakeholder. Here, A is a
balanced policy, B is unbalanced with the largest sum, and C lies in between. Figure 2 (c) plots the p-mean values of these
vectors, showing that varying p leads to different optimal policy.
C. Comparison with other MORL Algorithms
(Yu et al., 2024) optimize a generalized Gini welfare assuming a fixed weight vector. We address a fundamentally different
scenario, where decision-makers are uncertain about the appropriate fairness criterion (e.g., the choice of p in p-means or
the selection of weights in Gini welfare) in advance. Optimizing a single policy for one fairness parameter can lead to poor
outcomes under different criteria (see the approximation qualities of random baselines in our experiments). Our method
computes a small, representative set of policies covering the entire spectrum of fairness criteria. This allows decision-makers
to select confidently from this set, without worrying about suboptimality under other potential choices of p.
(Yang et al., 2019) focuses on weighted linear objectives and learns a single policy, whereas we focus on p-means and
compute a portfolio (multiple policies). (Alegre et al., 2023) builds portfolios focusing on weighted linear objectives (as
opposed to p−means) and does not offer guarantees on portfolio size or oracle complexity. (Reymond et al., 2022) trains a
single policy to approximate the Pareto frontier, which does not directly correspond to any social welfare function. To the
best of our knowledge, our work is the first to (1) propose a multi-policy approach in p-means and (2) provide theoretical
guarantees on portfolio size, approximation quality, and oracle complexity simultaneously.
In Table 3, we also present comparisons between p-MEANPORTFOLIO and the Generalized Policy Improvement (GPI)
algorithm of (Alegre et al., 2023), which maintains a set of policies Π′ ⊆Π and iteratively chooses the weight vector w with
the highest difference between the optimal policy value for w in Π vs in Π′. Our implementation of GPI uses the differential
evolution solver from scipy for this global optimization step. The results in the table indicate that our approach achieves
significantly better approximation quality. We omit other details of GPI here and refer the interested reader to (Alegre et al.,
2023).
D. Additional Experimental Results
Figures 3 and 4 illustrate how the optimal policies for different p values in the portfolio lead to varying impacts for the
stakeholders. These portfolios are all obtained using p-MEANPORTFOLIO. We also include the values of p chosen by
p-MEANPORTFOLIO to construct the portfolio in Table 4.
18

--- Page 19 ---

Navigating the Social Welfare Frontier
Table 3. A comparison of actual approximation ratios across various portfolio sizes for p-MEANPORTFOLIO and our implementation of
GPI.
Portfolio
Size
p-MEAN-
PORTFOLIO
GPI
Resource Allocation after Natural Disaster
1
0.706
0.514
2
0.904
0.520
3
0.999
0.520
4
0.100
0.520
Healthcare Intervention
1
0.924
0.347
2
0.982
0.641
3
0.982
0.641
4
0.982
0.641
5
0.993
0.641
6
0.999
0.641
7
1.000
0.641
Figure 3. Normalized total reward for each route under different policies in the portfolio generated by p-MEANPORTFOLIO in the taxi
environment.
E. Experimental Details
We include the details of various experiments here.
E.1. Taxi Environment
Problem Setting
This environment consists of a taxi agent whose task is to deliver passengers from source to destination. The world consists
of a 6x6 grid and based on the environment setup of (Fan et al., 2022), we consider 4 source-destination pairs. Whenever
a taxi moves to a source point, it can pick a passenger, move to destination and drop the passenger, thus receiving a
reward. Since some routes could be easier to serve, the agent has to decide which route to serve more often. Rewards
are multi-dimensional, each dimension corresponding to each route. We consider the following source-destination pairs:
source_coords = [[0, 0], [0, 5], [3, 0], [1, 0]], destination_coords = [[1, 5], [5, 0], [3, 3], [0, 3]]
MDP Structure
STATE SPACE (S)
The state space consists of information on the location of the taxi, location of passengers and whether passengers have been
picked up by the taxi at the moment.
19

--- Page 20 ---

Navigating the Social Welfare Frontier
Figure 4. Fraction of need meet for various clusters by various policies in the portfolio obtained by p-MEANPORTFOLIO after H = 4
intervention steps for the natural disaster experiment. Note that different solutions in the portfolio emphasize different clusters.
20

--- Page 21 ---

Navigating the Social Welfare Frontier
Table 4. The set of values of p chosen by p-MEANPORTFOLIO to obtain the corresponding portfolios.
Portfolio
size
p Values
Resource Allocation After Natural Disaster
1
-0.829
2
-4.864, -0.466
3
-11.136, -2.034, 0.621
4
-15.29, -2.054, 0.517, 0.758
Healthcare Intervention
1
-1.325
2
-2.864, 0.034
3
-4.333, -0.333, 0.333
4
-6.641, -0.433, -0.075, 0.463
5
-9.216, -4.108, -0.437, -0.078, 0.461
6
-13.801, -6.4, -0.594, -0.22, 0.085, 0.542
7
-17.793, -3.698, -0.549, -0.186, -0.038, 0.222, 0.611
Taxi Environment
1
-2.0
2
-3.89, 0.87
3
-6.21, 0.72, 0.86
8
-13.16, -10.06, -6.17, -4.82, 0.66, 0.7, 0.77, 0.89
10
-27.03, -13.02, -6.25, 0.66, 0.71, 0.78, 0.81, 0.86, 0.89, 0.95
ACTION SPACE (S)
The agent can take one of 6 actions: move north, south, east, west and pick or drop a passenger in the current grid cell.
REWARD (R)
The reward function gives reward 0 for moving, -10 reward for taking invalid action of picking or dropping a passenger at
wrong coordinating, and 30 reward for dropping a passenger at the right destination.
LEARNING POLICY
Given a scalarization function (or welfare function ), the task is to find a policy π∗that maximizined the expected value of
scalarized return. Specifically:
π∗= arg max
π
Eτ∼π

f
 G(τ), p

.
(11)
We learn this policy using the Welfare Q-Learning algorithm proposed in (Fan et al., 2022). For every problem setting, we
train the policy for 200 episodes. Every episode is a finite horizon problem with 1000 timesteps. We consider discount
factor gamma as 0.99.
E.2. Natural Disaster
Problem Setting
In this synthetically generated example, suppose that in the wake of a natural disaster, a centralized aid agency must
determine how to allocate resources to a set of 12 clusters (N = 12). Each cluster is characterized by their population
density (high or low), proximity to critical infrastructure (near or far), and the predominant income level of its residents (low,
middle, or high).
MDP Structure
The problem is formulated as an MDP M, with the following components:
21

--- Page 22 ---

Navigating the Social Welfare Frontier
Cluster ID
Density
Proximity
Income Level
Total Population
Initial Need
1
High
Far
High-Income
148
150
2
High
Far
Low-Income
307
500
3
High
Far
Middle-Income
616
650
4
High
Near
High-Income
816
300
5
High
Near
Low-Income
1405
1000
6
High
Near
Middle-Income
2782
950
7
Low
Far
High-Income
74
1000
8
Low
Far
Low-Income
203
350
9
Low
Far
Middle-Income
396
300
10
Low
Near
High-Income
36
50
11
Low
Near
Low-Income
113
100
12
Low
Near
Middle-Income
230
100
Table 5. Clustered population data including density, proximity, income level, total population, and initial need.
STATE SPACE (S)
The state s = (s1, s2, . . . , sN) represents the current resource needs of the N clusters. Each sc denotes the total remaining
need for cluster c. The state space is discretized, with each sc taking values in increments of b in [0, B]. In our setting,
b = 50 and B = 150.
ACTION SPACE (A)
Actions a = (a1, a2, . . . , aN) represent the allocation of resources to clusters, where: ac ∈{0, b, 2b, . . . , B} represents the
resources allocated to cluster c and the total allocation PN
c=1 ac cannot exceed the total budget B.
TRANSITION PROBABILITY MATRIX (TPM, P(s′|s, a))
The state transitions depend on the current state s and the action a. If ac ≥sc, s′
c = 0 with probability 1 (this cluster’s need
is fully met). If ac < sc the unmet need will reduce by the allocation, that is s′
c = sc −ac, with 70% probability. However,
there is a 30% probability that the cluster will observe an increase in need by b units, meant to reflect ballooning needs when
immediate action is not taken.
GENERATION OF POLICIES & REWARD FUNCTIONS
We consider combinations of “reasonable" policies a decision-maker might take in this setting. First, a valid policy would
not allocate resources to a zero-need cluster. Secondly, we consider the following priorities that a decision-maker might
have when allocating funds among nonzero unmet need clusters: (1) lowest income, (2) highest population, (3) highest
unmet need, (4) highest unmet need per capita, (5) high population density regions, and (6) far from critical infrastructure.
In every time period, for every feasible state, we apply one of these policies, a random convex weighting of these policies, or
a randomized priority to generate 10,000 different feasible policies.
The expected reward accrued by each cluster is the average of the sum of the expected fraction of the initial need met under
a policy and the fraction of the expected total allocation awarded to that cluster over the horizon.
E.3. Healthcare Intervention
The Healthcare Intervention problem is based on the large-scale mobile-health program run by the NGO ARMMAN
(ARMMAN, 2024). The goal of the program is to maximize engagement of beneficiaries with the program using limited
service call interventions. Based on previous works, we model this problem as RMAB problem where we have multiple
arms or beneficiaries, a budget on the number of service calls to give every week. For every beneficiary, we have information
on their listenership with the voice call. This is considered as an engaging or non-engaging state if the listenership is above
or below 30-seconds threshold respectively. One week of time is considered as one timestep. Finally, every week, the action
can be to place (active) or not to place a live service call (passive). Additionally, for every beneficiary, we have information
on their socio-demographic characteristics such as age, income, education. We use real world data from service quality
improvement conducted by ARMMAN in January 2022 (Verma et al., 2023). Further, for our experiments, we sample data
for 2100 beneficiaries, and run the experiment for H = 12 timesteps.
22

--- Page 23 ---

Navigating the Social Welfare Frontier
Generation of Policies & Reward Functions
The default reward incentivizes agents to be in engaging state. Thus, agents receive reward 1 if they are in engaging state,
and 0 otherwise. However, due to varying policy needs over time or over different geographies, health workers often have to
prioritize some beneficiaries more than others. To capture these varying priorities, we leverage the Social Choice Language
Model framework (Verma et al., 2024a) to derive reward functions from natural-language commands. Given a command
specifying Npreferences (each indicating a subgroup to prioritize) this method generates two sets of reward functions:
1. Individual preferences: one reward function per preference (total of N reward functions) which we treat as each
stakeholder’s reward function.
2. Balancing functions: a collection of reward functions that trade off among the N preferences, whose corresponding
policies form our feasible set Π.
In our experiments, we set N = 59 and construct |Π| = 200 balancing policies as feasible set.
Learning Policy
It is computationally intractable to optimally solve the RMAB problem (Papadimitriou and Tsitsiklis, 1999). Thus, we use
the popular Whittle Index Heuristic (Whittle, 1988) to solve RMAB problem for a given single reward function. Specifically,
Whittle Index quantifies the reward gain achieved for every arm in every state if we took the active action as compared to if
we took the passive action. The policy then chooses the arms with highest whittle indices within the budget limit.
Baseline Policy
The baseline policy mentioned in Figure 1 is trained on the default reward.
E.4. Other Details
Initial p for BUDGET-CONSTRAINEDPORTFOLIO
For BUDGET-CONSTRAINEDPORTFOLIO, we fix p0 = −100.
Computing actual approximation factor
The approximation factor Q(Π′) for any portfolio Π′ is computed via a grid search over 1000 points in (∞, 1] for the
natural disaster environment and the healthcare intervention problem. For the taxi environment, we used 50 points due to the
computational burden of solving each problem.
Choice of α
For a given portfolio size K, we chose the smallest α ∈{0.05, 0.10, 0.15, . . . , 0.90, 0.95, 0.99} among which the resulting
portfolio has size K.
23

```
