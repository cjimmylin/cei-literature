---
source_pdf: "[[Lit-WS-PDFs/2025/2025-Gölz-Distortion of AI Alignment Does Preference.pdf]]"
extracted_date: "2026-07-09"
pages: 38
extractor: "PyMuPDF"
---

Page 1:
arXiv:2505.23749v1  [cs.LG]  29 May 2025
Distortion of AI Alignment:
Does Preference Optimization Optimize for Preferences?
Paul G¨olz
Cornell University
paulgoelz@cornell.edu
Nika Haghtalab
UC Berkeley
nika@berkeley.edu
Kunhe Yang
UC Berkeley
kunheyang@berkeley.edu
Abstract
After pre-training, large language models are aligned with human preferences based on
pairwise comparisons. State-of-the-art alignment methods (such as PPO-based RLHF and DPO)
are built on the assumption of aligning with a single preference model, despite being deployed
in settings where users have diverse preferences. As a result, it is not even clear that these
alignment methods produce models that satisfy users on average — a minimal requirement for
pluralistic alignment. Drawing on social choice theory and modeling users’ comparisons through
individual Bradley-Terry (BT) models, we introduce an alignment method’s distortion: the
worst-case ratio between the optimal achievable average utility, and the average utility of the
learned policy.
The notion of distortion helps draw sharp distinctions between alignment methods: Nash
Learning from Human Feedback achieves the minimax optimal distortion of ( 1
2 +o(1)) · β (for
the BT temperature β), robustly across utility distributions, distributions of comparison pairs,
and permissible KL divergences from the reference policy. RLHF and DPO, by contrast, suffer
≥(1−o(1))·β distortion already without a KL constraint, and eΩ(β) or even unbounded distortion
in the full setting, depending on how comparison pairs are sampled.
1
Introduction
Reinforcement Learning from Human Feedback (RLHF) [Ouyang et al., 2022, Rafailov et al., 2023,
Christiano et al., 2017, Ziegler et al., 2019] has become the dominant paradigm for aligning large
language models (LLMs) with human values and preferences. In a typical alignment pipeline,
human feedback is provided as ordinal comparisons between pairs of candidate model outputs. This
feedback is used to fine-tune a pre-trained model, steering it toward the preferences expressed in
these comparisons. A major limitation of RLHF and of many proposed alternatives (including
DPO [Rafailov et al., 2023], ΦPO [Azar et al., 2024], KTO [Ethayarajh et al., 2024], SimPO [Meng
et al., 2024], χPO [Huang et al., 2024]) is that they do not take into account that users will disagree
on which model outputs are most useful or least harmful. A growing body of evidence — from both
the general public and the research community [AII, Sorensen et al., 2024, Conitzer et al., 2024,
Bai et al., 2022b] — suggests that this blind spot of current alignment methods can lead to unfair
outcomes. For example, Chakraborty et al. [2024] argue that RLHF may align with a majority
group’s preferences and ignore the preferences of a minority.
In this work, we study a more basic question: do current alignment methods reliably lead to a high
average utility across the users? Even such a minimal requirement might not be automatically met
since alignment methods such as RLHF were originally designed with a single, perhaps representative,
user in mind whose noisy ordinal preferences are assumed to be consistent with an underlying utility
model. As a result, RLHF fits a single reward model to the observed ordinal comparisons of a
1


Page 2:
y!
y"
≻
Preference Data
Reward Model
Large Pre-trained Model (𝜋𝜋#$%)
via Maximum 
likelihood
Users
Finetuned model (𝜋𝜋)
Fitting to a 
“mythical” user
𝑑𝑑𝑑𝑑𝑑𝑑𝑑𝑑𝑑𝑑𝑑𝑑𝑑𝑑𝑑𝑑𝑑𝑑𝑑𝑑=
max
&⋆AvgUtil(𝜋𝜋⋆)
AvgUtil(𝜋𝜋)
Figure 1: The typical RLHF pipeline. The preference optimization process begins by collecting comparison data
from users with heterogeneous utilities. A single Bradley-Terry model is then fit to this data via Maximum Likelihood
Estimation (MLE), producing a single reward model that represents a “mythical user” whose utility best explains
the observed comparisons. This reward model is used to fine-tune the pretrained policy. We define distortion as the
ratio between the average utility of an optimal policy and that of the output policy, which measures how well a policy
aligned with the mythical user’s utility aligns with the true average utility.
population of users with different utility functions, effectively constructing a utility function for a
“mythical” representative user. Could it be that optimizing a model for this mythical user leads to
poor outcomes on average for real users? More fundamentally, do ordinal preferences even contain
enough information to ensure high average utility across a heterogeneous user population?
Distortion of alignment.
To address these questions, we introduce the distortion of an alignment
method,1 which we define as the ratio between the optimal average utility of a policy (if the training
process had access to users’ true utilities) and the average utility achieved by the fine-tuned policy.
A larger distortion implies lower average quality relative to the optimal policy. This notion is
adapted from social choice theory [e.g., Procaccia and Rosenschein, 2006, Boutilier et al., 2012,
Anshelevich et al., 2021], where distortion quantifies the loss in average utility caused by using a
voting rule that relies solely on ordinal preferences rather than full cardinal utilities.
Our setting departs from this classical formulation of distortion in two ways. First, we assume
that users make pairwise comparisons probabilistically, following a Bradley–Terry model based
on the user’s idiosyncratic utilities. This assumption of probabilistic comparisons enables much
less pessimistic distortion bounds than in the classic, deterministic-choice setting while capturing
heterogeneous preferences. Second, our model and distortion bounds reflect that, in alignment, the
models’ generation policy is constrained to stay close to the pre-trained reference policy. These
departures generate insights for both the social choice and the alignment communities.
1While prior work has called for the study of distortion in alignment [Dai and Fleisig, 2024], or used alignment as
a motivation for studying the distortion of voting rules [Goyal and Sarmasarkar, 2025, Ebadian et al., 2024a], our
work is to our best knowledge the first to systematically define and analyze the distortion of alignment methods. We
discuss these related efforts in Appendix A.
2


Page 3:
1.1
Our Results
Our results address both the social choice setting with individual Bradley–Terry comparisons
(Section 3) and the alignment setting (Section 4), which additionally constrains the policy to remain
close in Kullback-Leibler (KL) divergence to a reference policy. The social choice setting is a special
case of the alignment setting, in which the proximity constraint is not binding. Besides RLHF,
which coincides with the Borda voting rule in the social choice setting, we study the proposed
alternative Nash Learning from Human Feedback (NLHF) [Munos et al., 2024], which coincides with
the Maximal Lotteries [Fishburn, 1984] voting rule. Direct Preference Optimization (DPO) [Rafailov
et al., 2023] is equivalent to RLHF in our analysis and hence has the same distortion. We define
these alignment methods and voting rules in Section 2. In Section 5, we discuss how our results
extend to KL-regularized (rather than constrained) alignment methods and to generalized models
of sampling comparison pairs.
In this overview of results, summarized in Table 1, we present our bounds for the case where the
number of sampled pairwise comparisons goes to infinity. In later sections, we accompany these
statements with polynomially fast, finite-sample convergence bounds.
Our results establish that some distortion is unavoidable: in the social choice setting (i.e., without
KL constraints), if each user only provides a single comparison, we show through a non-identifiability
argument2 that, for each value β > 0 of the Bradley–Terry temperature, every alignment method
(or, equivalently, any voting rule) will suffer a distortion of (1
2 + o(1))β on some instances. This
lower bound reflects a fundamental information bottleneck: even under Bradley–Terry generative
assumptions, ordinal feedback is not rich enough to perfectly optimize for the average utility of a
heterogeneous user population. If each user provides d ≥2 (possibly correlated) comparisons, the
same lower bound applies to all voting rules that satisfy a probabilistic relaxation of the Condorcet
loser criterion, a social-choice axiom widely satisfied by desirable voting rules, including Borda and
Maximal Lotteries. As a result, this lower bound extends to RLHF and NLHF.
In the social choice setting, we show that both Borda and Maximal Lotteries have a distortion that
is bounded in β. Borda’s distortion lies between (1 −o(1))β and O(β2), whereas Maximal Lotteries’
distortion is (1
2 + o(1))β, matching even the lower-order terms of the lower bound. These results are
of independent interest to the social choice community since they show that the introduction of
randomized pairwise comparisons circumvents the necessary growth of distortion in the number
of alternatives m. Recently, Goyal and Sarmasarkar [2025] showed that the same Bradley–Terry
assumption can reduce the distortion of specific voting rules in the metric distortion setting, where
utilities are distances in a metric space. Our results show that the Bradley–Terry assumption
has an even larger impact in the general-utility distortion setting, where constant distortion is
classically impossible, than in metric distortion. For the AI community, these distortion bounds
also carry implications for AI leaderboards such as Chatbot Arena Chiang et al. [2024], where
heterogeneous user preferences across diverse tasks are aggregated via MLE under a single Bradley–
Terry model — effectively equivalent to using Borda scores. We elaborate on these implications in
Section 3.3.
In the alignment setting, we show that NLHF maintains Maximal Lotteries’ optimal (1
2 + o(1))β
distortion with remarkable robustness: regardless of the population’s utilities, how comparison
pairs are sampled, the number of comparisons per user, the reference policy, and the bound on the
permissible KL divergence, NLHF obtains a Ω(1/β) fraction of the highest average utility achievable
within the KL-divergence bound. Though we present this result for KL-constrained NLHF, we
show in Section 5 that this directly implies a similar distortion guarantee for regularized NLHF. In
2While the non-identifiability of mixtures of ranking models is well established [Zhao et al., 2016, Zhao and Xia,
2019, Zhang et al., 2022], our result quantifies the resulting loss in average utility.
3


Page 4:
Table 1: Overview of distortion bounds by alignment method and setting.
Alignment Method
Social Choice Setting
AI Alignment Setting
RLHF [Ziegler et al., 2019]
≤O(β2) Thm 2
(Borda)
≥(1 −o(1)) β Thm 5
≥eΩ(β) Thm 6 / Unbounded in β* Thm 9
NLHF [Munos et al., 2024]
=
  1
2 + o(1)

β Cor 4 (Max. Lotteries) =
  1
2 + o(1)

β Thm 7
all (one comparison per user/
Condorcet loser property)
≥
  1
2 + o(1)

β Thm 3
≥
  1
2 + o(1)

β Thm 3
*comparison pairs sampled from a distribution over pairs.
contrast, RLHF’s distortion can grow as eΩ(β) in the alignment setting and is even unbounded in β
if the two outcomes to be compared are sampled in a correlated way rather than i.i.d.
We discuss additional related work in Appendix A.
2
Preliminaries
Let A = {1, . . . , m} be a finite set of alternatives. The population of users is described by a
probability distribution D over utility vectors u = (u(1), . . . , u(m)), whose entries 0 ≤u(x) ≤1
indicate a user’s utility for alternative x.3 The objective is to find an alternative x such that its
average utility AvgUtil(x) := Eu∼D[u(x)] across the user population (also known as the utilitarian
social welfare) is as high as possible. We extend this notation to probability distributions π over
alternatives by setting AvgUtil(π) := Ex∼π[AvgUtil(x)].
Both voting rules and alignment methods observe comparisons from n users. We model each
i = 1, . . . , n as a fresh user with independently drawn utility vector ui ∼D. For exposition, we
assume that each user i provides an equal number d ≥1 of pairwise comparisons. For each i, and for
j = 1, . . . , d, we independently draw alternatives xj
i, yj
i from a fixed distribution µ over alternatives,
in which the minimum probability mass µmin := minx∈A µ(x) is positive.4 User i then compares
each pair {xj
i, yj
i } (for j = 1, . . . , d) through a Bradley-Terry model based on i’s utilities: i prefers
xj
i over yj
i (written “xj
i ≻i yj
i ”) with probability σ
 β · (ui(xj
i) −ui(yj
i ))

, where σ(t) := 1/(1 + e−t)
is the logistic sigmoid function and β > 0 is a temperature parameter, and prefers yj
i over xj
i
(“yj
i ≻i xj
i”) otherwise.5 Whereas this specifies the marginal probability of each pairwise comparison,
we make no assumption about the correlation between i’s choices. For example, i might derive the
pairwise comparisons from a Plackett-Luce ranking, ensuring that the user’s comparisons are always
consistent.6 We set p(x ≻y) for the expected win rate Eu∼D

σ
 β · (u(x) −u(y))

.
Social Choice Setting.
A voting rule f observes the sampled pairwise comparisons {xj
i ≻i
yj
i }i∈[n],j∈[d] and maps them to a probability distribution over alternatives. For some m, D, β, d, µ,
and the correlation between comparisons, the average utility of f for n samples is AvgUtiln(f) :=
E

AvgUtil
 f({xj
i ≻i yj
i }i,j)

, where the expectation is taken over the pairwise comparisons. The
distortion of f on D is the competitive ratio between AvgUtiln(f) and the optimal average utility
3Our assumption that utilities be in [0, 1] is weaker than any of the three assumptions — unit-sum, unit-range, or
approval [Ebadian et al., 2024b] — made in classic distortion to avoid trivial infinite lower bounds.
4In Section 5, we discuss how most of our results extend more general distributions over comparison pairs, which
can, for example. capture k-wise comparisons.
5Should we sample the same alternative x = xj
i = yj
i twice for a pair, the user is not asked for a pairwise comparison.
We record this as “x ≻i x”, in a slight abuse of notation.
6In particular, if we sample the same unordered pair twice for a user, the answers can be perfectly correlated.
4


Page 5:
maxx∈A AvgUtil(x) in the limit of n →∞samples, and the distortion of f the worst-case distortion
over all D:
dist(f, D) := lim sup
n→∞
maxx∈A AvgUtil(x)
AvgUtiln(f)
,
dist(f) = sup
D
dist(f, D).
For alternatives x, y, let #(x ≻y) := {(i, j) | xj
i = x, yj
i = y} denote the number of pairwise
comparisons in which x beat y. The (normalized) Borda score [Shirali et al., 2025] of alternative x is
BC(x) :=
P
y∈A #(x ≻y)
P
y∈A #(x ≻y) + P
y̸=x #(y ≻x),
i.e., the fraction of pairwise comparisons involving x in which it wins. The Borda voting rule chooses
the winner uniformly among all alternatives with maximum Borda score. The Maximal Lotteries
voting rule first computes the margin matrix M ∈Rm×m, where Mx,y = #(x≻y)−#(y≻x)
#(x≻y)+#(y≻x). It then
considers a symmetric two-player zero-sum game in which player 1 selects alternative x1, player 2
selects alternative x2, and the payoffs are Mx1,x2 for player 1 and Mx2,x1 = −Mx1,x2 for player 2. The
maximal lotteries rule returns a distribution π ∈argmaxπ1∈∆(A) minπ2∈∆(A) Ex1∼π1,x2∼π2[Mx1,x2],
i.e., a mixed strategy in Nash equilibrium. (When several such π exist, our results hold for any
choice.)
Alignment Setting.
The alignment setting generalizes the social choice setting in two ways:
first, user utilities ui(y | x) may depend on a state x; second, the goal in determining a policy
π is not purely to maximize the reward AvgUtil(π | x), but a trade-off between this reward and
the goal of remaining close to a reference policy πref(· | x) ∈∆(A) in terms of the KL divergence
DKL(· ∥πref). For theoretical tractability, we focus our analysis on a single state x, which we from
here on omit from the notation. Conceptually, this treatment of alignment on a state-by-state basis
corresponds to an assumption that our policy class is expressive enough so that it can take the
optimal distribution of actions at each state7 and abstracts from the generalization problem of
estimating the population’s preference between a pair of alternatives at the given state x based on
preferences in similar states x′.
Having set aside the dependency between states, we focus on how the regularization with respect
to a reference policy impacts the ability to optimize the average utility of three alignment methods:
RLHF, DPO, and NLHF. In addition to the pairwise comparisons, these methods take in a reference
policy πref ∈∆(A) and a KL bound τ ≥0, and map these inputs to a policy π in the KL-ball
Bτ(πref) := {π ∈∆(A) | DKL(π ∥πref) ≤τ} around the reference policy. RLHF, DPO, and NLHF
are typically implemented with a KL regularization rather than our KL-constrained formulation,
which we adopt to enable a comparison on equal terms. In Section 5, we show that these perspectives
are equivalent, and that distortion upper bounds carry over to regularized alignment methods.
The RLHF method first estimates rewards for each alternative, using maximum likelihood
estimation assuming that comparisons were generated by a single Bradley–Terry model:
r := argmaxr∈Rm P
1≤i≤n,1≤j≤d log
 σ(r(xj
i) −r(yj
i ))

.8
Next, RLHF uses PPO [Schulman et al., 2017] to compute the policy with maximum expected
reward within the KL-ball:
πRLHF := argmax
π∈Bτ(πref)
Ex∼π[r(x)].
7This assumption is common in the literature; see, for example, Rafailov et al. [2023]’s application of first-order
optimality conditions of PPO loss minimization.
8Assuming that each x ∈A wins at least one pairwise comparison against each y ̸= x, this optimization has a
maximizer, which is unique up to additive shifts, by strict convexity.
5


Page 6:
In our setup, DPO is equivalent to RLHF (see Appendix E.3) and thus has the same distortion.
The alignment method NLHF was inspired in part by a desire to better align with the preferences
of a heterogeneous group [Munos et al., 2024]. NLHF naturally adapts the definition of maximal
lotteries by constraining both players’ mixed strategies to the KL-ball, i.e.,
πNLHF := argmax
π1∈Bτ(πref)
min
π2∈Bτ(πref)
E
x1∼π1,x2∼π2 [Mx1,x2] .
To generalize the definition of distortion to alignment methods, we set the maximum average
utility of any policy in the KL-ball as the benchmark. For fixed m, D, β, d, µ and correlation between
pairwise comparisons, the distortion of alignment method f is
dist(f) =
sup
D,πref,τ
lim sup
n→∞
maxπ∈Bτ(πref) AvgUtil(π)
AvgUtiln(f(·, πref, τ))
.
3
Social Choice (or AI Alignment without KL Constraint)
We begin the demonstration of our distortion framework in the social choice setting. From the
perspective of alignment, this setting is the limit where the KL constraint (equivalently, KL
regularization) to the reference policy vanishes. Hence, distortion measures whether the “direction”
in which an alignment method pushes the pre-trained policy is aligned with average utility at all.
Moreover, the social choice setting allows us to illustrate how the Bradley-Terry assumption
overcomes the pessimism of classic deterministic-choice distortion. In the classic setting, high
distortion — Ω(√m) even for randomized voting rules and under utility-normalization assump-
tions [Boutilier et al., 2012, Ebadian et al., 2024b] — is unavoidable because a voting rule observes no
signal about preference intensity, i.e., whether a user prefers a over b strongly or is merely breaking a
tie between equally valued alternatives. Random Bradley-Terry comparisons would clearly side-step
this problem if we could observe many samples of each pairwise comparison for a single utility
vector: by consistency, the Bradley-Terry MLE would recover the utilities (up to an additive shift),
allowing us to select the utility-maximizing alternative and achieve a perfect distortion of 1.
It is not obvious, by contrast, that random pairwise comparisons will be similarly useful in our
heterogeneous setting, where each observation is drawn from a mixture of users’ Bradley-Terry
models. Because users are not labeled and may provide as little as a single pairwise compar-
ison, there is no hope to cluster users and estimate rewards per cluster. Instead, a source of
inspiration is an observation by Caragiannis and Procaccia [2011] in a much simpler model, in
which each user votes for a single alternative with probability equal to their utility (which is
normalized to sum to 1). Since the probability of the event “i votes for x” equals ui(x), the total
number of votes of alternative x (i.e., P
i∈N 1i votes for x) is an unbiased estimator of its total utility.
Figure 2: Bounds on probability of
preferring x over y, β = 5.
For many samples, this estimator concentrates around its
mean and allows to select the optimal alternative.
The
argument would extend if some observed events from a user
had a probability that is affine in the user’s utilities. Alas,
we are not so lucky: the sigmoid function in the probability
of the event “i ranks x over y” is nonlinear, and we show
in Theorem 3 that this nonlinearity makes a distortion of at
least β
2
1+e−β
1−e−β > 1 unavoidable.
Though our observations’ probabilities are not affine in the
utilities, we can bound these probabilities by affine functions,
which ultimately powers our distortion upper bounds. As
6


Page 7:
shown in Fig. 2, we sandwich the probability σ(β · (u(x) −
u(y))) that a user with utilities u prefers x over y between the affine lower bound β·(L u(x)−ℓβ u(y))+
1
2 and affine upper bound β · (ℓβ u(x) −L u(y)) + 1
2, for constants L, ℓβ defined below. By linearity,
this bound extends to a bound of the expected win-rate p(x ≻y) = Eu∼D [σ(β · (u(x) −u(y)))] by
affine expressions in AvgUtil(x) = Eu∼D [u(x)] and AvgUtil(y) = Eu∼D [u(y)]. We defer the lemma’s
formal proof to Appendix B.
Lemma 1 (Linearization of Expected Win-Rates). Let L := σ′(0) = 1/4 and ℓβ :=
σ(β)−1
2
β
=
1
2β · 1−e−β
1+e−β . For any pair of alternatives x, y ∈A, we have
β · (ℓβ · AvgUtil(x) −L · AvgUtil(y)) ≤p(x ≻y) −1
2 ≤β · (L · AvgUtil(x) −ℓβ · AvgUtil(y)) .
3.1
Upper Bound on Borda Distortion
Siththaranjan et al. [2023] observed that RLHF and the Borda voting rule are closely linked in that
the Bradley-Terry MLE rewards are ordered by their alternatives’ Borda score. Hence, as the KL
constraint relaxes, RLHF moves all of the policy’s probability mass on the Borda winner. Because
Borda has infinite distortion in the classic setting [Procaccia and Rosenschein, 2006], we would hope
that distortion is more reasonable under our assumptions. Fortunately, Borda indeed has at most
O(β2) distortion, which we prove through two applications of our linearization lemma:
Theorem 2 (Borda Distortion Upper Bound). For any instance D with any number of alternatives
m, distribution µ over alternatives, and temperature β, Borda has at most distortion
  β
2 · 1+e−β
1−e−β
2 =
O(β2). In the finite-sample regime, we have that
AvgUtiln(Borda) ≥
  2
β · 1−e−β
1+e−β
2 · maxx⋆∈A AvgUtil(x⋆) −O

1
β2
q
log(mnβ)
n·min{1,dµ2
min} + m log(mnβ)
n·β2µ2
min

.
Proof sketch (full proof in Appendix D.1). For exposition, we sketch this proof for n →∞, assuming
that each alternative’s Borda count has converged to its expectation BC⋆(x) := P
y∈A µ(y)·p(x ≻y).
Let ˆx = argmaxx∈A BC⋆(x) be the Borda winner in the limit, and x⋆= argmaxx∈A AvgUtil(x) be
the utility maximizer. Applying Lemma 1 to the win-rates p(ˆx ≻y) and p(x⋆≻y) for all y ∈A, we
have that
BC⋆(ˆx) −1
2 ≤P
y∈A µ(y) · β (L · AvgUtil(ˆx) −ℓβ · AvgUtil(y))
= β (L · AvgUtil(ˆx) −ℓβ · AvgUtil(µ)) ;
(1)
BC⋆(x⋆) −1
2 ≥P
y∈A µ(y) · β (ℓβ · AvgUtil(x⋆) −L · AvgUtil(y))
= β (ℓβ · AvgUtil(x⋆) −L · AvgUtil(µ)) .
Since BC⋆(ˆx) ≥BC⋆(x⋆), we obtain from the above two inequalities that
L · AvgUtil(ˆx) + (L −ℓβ) · AvgUtil(µ) ≥ℓβ · AvgUtil(x⋆).
(2)
A standard averaging argument shows that Ex∼µ[BC⋆(x)] ≥1/2, which implies that BC⋆(ˆx) must be
at least 1/2. Combining this with Eq. (1), we obtain that AvgUtil(µ) ≤L
ℓβ · AvgUtil(ˆx). Substituting
this into Equation (2) (noting that L ≥ℓβ), we have that
L2
ℓβ AvgUtil(ˆx) = L · AvgUtil(ˆx) + (L −ℓβ) L
ℓβ
· AvgUtil(ˆx)
≥L · AvgUtil(ˆx) + (L −ℓβ) · AvgUtil(µ) ≥ℓβ · AvgUtil(x⋆),
which yields the distortion guarantee AvgUtil(x⋆)
AvgUtil(ˆx) ≤
  L
ℓβ
2 =
  β
2
1+e−β
1−e−β
2.
7


Page 8:
3.2
Lower Bounds (and Upper Bound for Maximal Lotteries)
The upper bound for Borda nested two applications of the linearization lemma. As a result, it twice
incurred a distortion factor of L
ℓβ =
σ′(0)
(σ(β)−σ(0))/β, which measures the sigmoid function’s deviation
from linearity in the relevant range. Below, we show that any voting rule must incur this factor at
least once, at least for the case of d = 1 comparisons per user. This distortion occurs even though
the voting rule has access to infinitely many pairwise comparison samples, which shows that the
nonlinearity of the Bradley-Terry model can cause a loss of the information necessary to find the
utility maximizer.
The proof (in Appendix D.3) constructs a user population D in which a small minority has
utility 1 for some special alternative a and 0 for all other alternatives, whereas the majority has a
small utility ϵ for all alternatives except for a, for which they have utility 0. The sizes of these blocs
are balanced such that all expected win-rates are 1/2. Due to the diminishing returns in the sigmoid
function, the resulting average utility for a is L
ℓβ times higher than that of the other alternatives.
But since the pairwise comparisons observed by a voting rule are just independent Bernoulli draws
with bias 1/2, all versions of the instance with permuted alternatives are indistinguishable. Since no
voting rule can identify alternative a better than random guessing, they must incur L
ℓβ distortion.
If there are d ≥2 observations per user, the above argument does not apply to all voting rules
because an elaborate voting rule might use the correlations within a user’s comparisons to identify
a. We can, however, extend the lower bound to d ≥2 for all voting rules that put at most 1/m
probability mass on a Condorcet loser, i.e., an alternative x such that #(y ≻x) > #(x ≻y) for all
y ̸= x. This property generalizes the Condorcet loser criterion and is satisfied by a wide range of
voting rules deemed desirable, including Borda and Maximal Lotteries. The proof uses essentially
the same instance as above, slightly tipping the expected win-rates against a to make it a Condorcet
loser. Since the social choice setting is a special case of alignment, the lower bound extends to
alignment.
Theorem 3 (Voting Rule-Independent Distortion Lower Bound). Fix any β > 0. If each user
provides d=1 comparison, no voting rule can guarantee distortion better than β
2 · 1+e−β
1−e−β for large m.
If each user reports d ≥2 pairwise comparisons, any voting rule that puts at most 1/m probability
mass on a Condorcet loser must have at least the above distortion.
The Maximal Lotteries voting rule exactly matches the above lower bound of β
2 · 1+e−β
1−e−β . We
omit the proof here, as it follows as a direct corollary of NLHF’s upper bound (Theorem 7) in the
next section.
Corollary 4 (of Theorem 7). The Maximal Lotteries voting rule has a distortion of β
2 · 1+e−β
1−e−β .
The Borda rule, in contrast, does not match this optimal distortion bound, as shown by the
following bound that we prove and state in full detail in Appendix D.2.
Theorem 5 (Borda Distortion Lower Bound, Informally). For any β > 0 and m ≥3, the distortion
guaranteed by Borda (and, hence, RLHF) is greater than and bounded away from β
2
1+e−β
1−e−β . In
particular, as β →∞, this distortion guarantee is at least (1 −o(1)) · β.
3.3
Discussion
Implications for Social Choice Theory.
Though we have presented these bounds in terms of
their implications for alignment, they are of independent interest to social choice theory. In our
view, a major drawback of the distortion framework (with nonnegative utilities) is that it leads to
8


Page 9:
unreasonably high distortion, and some unnatural prescriptions. For example, any deterministic
voting rule has distortion Ω(m2), where optimal distortion is achieved by Plurality [Caragiannis
and Procaccia, 2011] (a rule widely disregarded by social choice theorists) wheras Borda and
all Condorcet consistent rules have infinite distortion [Procaccia and Rosenschein, 2006]. These
limitations may explain in part why recent research activity [e.g., Gkatzelis et al., 2020, Charikar
et al., 2024, Goyal and Sarmasarkar, 2025] has focused on the metric distortion setting [Anshelevich
et al., 2018, 2021], in which many natural voting rules have constant distortion. But this comes at
the cost of expressiveness: the metric setting assumes utilities are (negated) distances satisfying the
triangle inequality. For example, the metric distortion setting implies that, if i has high utility for x
and y, and j has high utility for x, then j must also have high utility for y, which need not be the
case in our setting. We see our assumption of a user-specific random choice model as another way
to make distortion a more practical criterion for choosing between voting rules.
Implications for AI Leaderboards.
For the AI community, our social-choice distortion results
also have implications beyond being a special case of alignment. A notable example is Chatbot
Arena’s evaluation of language models [Chiang et al., 2024], where users submit prompts, are shown
the responses of two anonymized models, and select their preferred response. The leaderboard
aggregates these pairwise comparisons by fitting a Bradley-Terry model via MLE, and ranking the
models according to their estimated reward. As in the alignment setting, this approach assumes a
single latent notion of LLM quality, ignoring the fact that LLMs are used by diverse users for a
wide range of tasks, each with their own goals, preferences, and prompt styles. This setting fits
neatly into our social-choice model, where D captures a random user’s utility for the responses of
different models to a random prompt (drawn from an arbitrary joint distribution over users and
prompts), and AvgUtil quantified the average utility a model delivers for a random user and task,
which we call the model’s usability in this section.
Since Chatbot Arena and RLHF are based on the same MLE, our distortion bounds on RHLF in
the social choice setting imply that the usability of the top-ranked language model (i.e., the Borda
winner) may be (1−o(1))·β times worse than the usability of some other ranked model (Theorem 5)
(but at most by a O(β2) factor, see Theorem 2). Our later results in an extended setting in which
comparison pairs are drawn in a correlated way (Section 5) show that Chatbot Arena’s ranking is
highly sensitive to the distribution of LLM pairs. For certain correlated distributions, the gap in
usability could be unbounded (Theorem 9), which is concerning since Chatbot Arena adaptively
oversamples new and highly ranked models.
These findings suggest that current leaderboard rankings may not fully reflect true model
quality. Could alternative aggregation rules, such as Maximal Lotteries or the Copeland voting rule,
provide more accurate assessments of model usability and be more robust to the choice of sampling
distribution? Does adaptive sampling introduce systematic biases that exacerbate the distortion of
current pipelines? Addressing these questions is an important direction for future work to ensure
the fidelity of leaderboard-based evaluations.
4
AI Alignment with KL Constraint
We now tackle the general alignment setting, in which the output policy π must be chosen within
a prescribed KL divergence of the reference policy πref. This setting is more challenging than the
social choice setting because even an alignment method that would choose high-utility alternatives
in the absence of constraints might make poor use of a finite KL budget.
9


Page 10:
4.1
Lower Bound for RLHF
Before presenting the optimal distortion upper bound for NLHF, we illustrate the pitfalls of the
alignment setting with a lower bound on RLHF. This bound shows that a KL constraint can cause
RLHF to have exponential distortion in β, exceeding its quadratic upper bound in the social choice
setting (Theorem 2).
Theorem 6 (RLHF Distortion Lower Bound). For m ≥3, there is a sequence of alignment problems
on which the distortion of RLHF scales as eΩ(β) in β.
Proof sketch (full proof in Appendix E.2). For ease of exposition, consider an instance with three
alternatives a, b, c where µ(c) is about eβ times larger than µ(a) = µ(b).9 Let the population consist
of a tiny minority (a Θ(eβ) fraction) with utilities u(a) = 0, u(b) = 1, u(c) = 0, and a large majority
with utilities u(a) = 1
β, u(b) = 0, u(c) = 1. Both a and b are likely to be beaten by c, but by carefully
choosing the size of the minority, we can make p(b ≻c) > p(a ≻c), i.e., we can make b’s advantage
of being preferred by the minority outweigh a’s advantage of being slightly less dispreferred by the
majority. Since µ(c) is so much larger than µ(a), µ(b), the vast majority of pairwise comparisons
involving a or b are against c. As a result, the MLE reward for b will be higher than for a, even
though AvgUtil(a) = Θ( 1
β) is exponentially larger than AvgUtil(b) = Θ(eβ). (In the social choice
setting, this would not be a problem because c has even higher average utility and higher reward.)
The lower bound arises for a reference policy that puts a tiny probability mass ε on c, and 1−ε
2
probability mass each on a and b, together with a KL constraint of τ = log 2. Now DKL(π ∥πref) =
π(a) log
π(a)
(1−ε)/2 + π(b) log
π(b)
(1−ε)/2 + π(c) log π(c)
ε . Since ε is very small, π(c) cannot be increased by
enough to make a meaningful difference on the achievable utility; but the KL budget essentially
allows to spread the probability mass of π freely between a and b. Since b has a higher MLE
reward, RLHF puts almost all of π’s mass on b, which yields exponentially less utility than the
utility-maximizing policy in the KL ball, which puts almost all mass on a.
This bound formalizes a key limitation of the reward-based approach inherent to RLHF. The
MLE phase of RLHF attempts to fit rewards to the observed comparisons, whose frequencies
are determined by µ. Due to preference heterogeneity, not all three pairwise win-rates can be
simultaneously fit by a reward vector, so the MLE sacrifices accuracy on the rarely observed pair
{a, b} for higher accuracy of comparisons involving c. By placing so little mass on c, our choice of
πref forces RLHF to choose between the misrepresented alternatives a and b, causing it to make a
high-distortion choice.
Our lower bound exploits that the distribution µ governing the frequencies of comparison pairs
differs greatly from the reference policy πref. We leave open to characterize RLHF’s distortion under
the assumption that µ = πref, for which we only know the lower bound Theorem 5.
4.2
Distortion of NLHF
While we saw above that a mismatch between input distribution µ and reference policy πref can lead
RLHF towards highly suboptimal policies, NLHF has no such problem. Below, we show that, across
all settings of our model, NLHF’s distortion exactly matches the lower bound from Theorem 3.
Despite the generality of this result, the proof is no harder than our upper bound for Borda in
the social choice setting and involves only a single application of the linearization lemma. It also
highlights a key advantage over RLHF’s reward-based approach: Since the NLHF policy is computed
as a Nash-equilibrium strategy in a game where the opponent might select any policy in the KL ball,
9To avoid such unbalanced µ, one could equivalently copy alternative c many times and let µ be uniform.
10


Page 11:
the NLHF automatically “hedges” to perform well in expectation against all such policies, including
the utility-maximizing benchmark π⋆. Since the social choice setting is a special case of alignment,
this theorem immediately implies the distortion upper bound for Maximal Lotteries (Corollary 4),
and both NLHF and Maximal Lotteries are minimax optimal by the lower bound in Theorem 3.
Theorem 7 (NLHF Distortion Upper Bound). For any instance D and any m, data distribution µ,
temperature β of the Bradley-Terry model, and any reference policy πref and KL budget τ, we have
dist(NLHF) ≤β
2 · 1+e−β
1−e−β . In the finite-sample regime, we have
AvgUtiln(NLHF) ≥
  2
β · 1−e−β
1+e−β

· maxπ⋆∈Bτ(πref) AvgUtil(π⋆) −O

1
β
q
log(mn)
n·min{1, d·µ2
min} + log(mn)
n·βµ2
min

.
Proof sketch (full proof in Appendix E.1). For exposition, we assume that the NLHF method knows
the expected win-rates p(x ≻y), and defer the proof of finite-sample guarantees. Hence, the NLHF
policy by definition satisfies
πNLHF ∈argmax
π1∈Bτ(πref)
min
π2∈Bτ(πref) Ex1∼π1,x2∼π2[p(x1 ≻x2) −p(x2 ≻x1)].
Since this describes a Nash-equilibrium strategy for a symmetric two-player zero-sum game, and
any such game has value 0, it must hold that
min
π2∈Bτ(πref) Ex1∼πNLHF,x2∼π2[p(x1 ≻x2) −p(x2 ≻x1)] = 0.
Plugging in p(x1 ≻x2) −p(x2 ≻x1) = 2 p(x1 ≻y1) −1, we obtain
min
π2∈Bτ(πref)
E
x1∼πNLHF,x2∼π2

p(x1 ≻x2) −1
2

= 0.
Using the utility-maximizing policy π⋆:= argmaxπ∈Bτ(πref) AvgUtil(π) for π2, we obtain that
Ex1∼πNLHF,x2∼π⋆[p(x1 ≻x2) −1
2] ≥0.
At this point, we upper bound the win-rate with the linearization lemma (Lemma 1), and obtain
0 ≤Ex1∼πNLHF,x2∼π⋆[β · (L · AvgUtil(x1) −ℓβ · AvgUtil(x2))]
= β · (L · AvgUtil(πNLHF) −ℓβ · AvgUtil(π⋆)) .
This implies that
AvgUtil(π⋆)
AvgUtil(πNLHF) ≤L
ℓβ = β
2 · 1+e−β
1−e−β = O(β), thus completing the proof.
The simplicity of the proof above also speaks to its generality. For instance, the only property
of KL divergence we used was that the feasible region Bτ(πref) is a closed convex set (to ensure the
existence of a Nash equilibrium). Consequently, the distortion bound of Nash learning extends to
other ways of constraining proximity to the reference policy, such as by χ2 divergence [Huang et al.,
2024].
5
Extensions of the Model
KL Constraints vs. Regularization.
In our model, we defined alignment methods as taking in
an explicit KL bound τ as an input parameter, which is convenient for comparing the policy against
a fair benchmark. In practice, however, alignment methods such as RLHF, DPO, and NLHF are
regularized rather than constrained in terms of their KL-divergence. For example, the PPO phase of
11


Page 12:
RLHF finds a policy π maximizing the regularized objective Ex∼π[r(x)] −λDKL(π ∥πref), and the
payoff matrix in the game solved by NLHF is Ex1∼π1,x2∼π2[Mx1,x2]−λDKL(π1 ∥πref)+λDKL(π2 ∥πref),
where λ ≥0 is a regularization parameter given to the alignment method instead of τ.
We prove in Appendix E.4 that the regularized and constrained versions of RLHF and NLHF
are equivalent. That is, each policy π returned by the λ-regularized version of a method is optimal
for the τ-constrained version for τ = DKL(π ∥πref) (and any policy returned by the τ-constrained
version is optimal for the λ-regularized version and some λ ≥0).
Through this equivalence, any distortion upper bound in our setting applies to the KL-regularized
versions of the alignment method: if π results from the λ-regularized alignment method, π is optimal
for the τ =DKL(π ∥πref)-constrained version by equivalence, at which point the distortion upper
bound shows that π can compete with any policy with no larger KL divergence from πref.10 Applying
this observation to Theorem 7, we obtain the following guarantee for regularized NLHF:
Corollary 8. If λ-regularized NLHF (for any λ ≥0) returns a policy ˜πNLHF, this policy’s average
utility is at least a 2
β · 1−e−β
1+e−β fraction of the optimal average utility of any policy π with DKL(π ∥πref) ≤
DKL(˜πNLHF ∥πref) (minus finite-sample errors, see Theorem 7).
Sampling of Comparison Pairs.
In our model, we assume that each voter provides d pairwise
comparisons, where both members xj
i, yj
i of each comparison pair are sampled i.i.d. from µ. More
generally, we can model {xj
i, yj
i } ∼ν where ν is a distribution over unordered alternative pairs, or
even a distribution over d pairs of alternatives from which {x1
i , y1
i , . . . , xd
i , yd
i } are sampled. (To keep
the alignment methods well defined, we assume that each comparison pair has positive probability of
being sampled.) The latter of these models can, for example, express k-wise (rather than pairwise)
comparisons, if d =
 r
2

are all pairs inside a randomly chosen set of r alternatives. Almost all of our
results continue to hold in these general models: the lower bound for all alignment methods that
satisfy the Condorcet loser criterion in the social choice setting (Theorem 3), the exponential lower
bound for RLHF (Theorem 6), and the upper bound for NLHF/Maximal Lotteries (Theorem 7)11.
Given that our proofs continue to work out, the only “disadvantage” of these stronger models
for sampling comparison pairs is that, without a distribution µ, the Borda voting rule is no longer
defined (and we see no obvious way to generalize the Borda–MLE equivalence [Siththaranjan et al.,
2023, Procaccia et al., 2025]). It seems that RLHF does not only become harder to analyze under
these comparison-pair models, but actually performs worse: we show in Appendix F that RLHF
can have a distortion that is not bounded in β in these extended models, leading to an even clearer
separation with NLHF.
Theorem 9 (Unbounded Distortion of RLHF Under Correlated Sampling). For any β > 0, there
exists a sequence of alignment instances and distributions ν ∈∆
  A
2

over comparison pairs such
that RLHF’s distortion is unbounded.
6
Discussion
In this paper, we introduced the notion of distortion for AI alignment. We showed that one such
alignment method, NLHF, obtains the optimal distortion guarantee of (1
2 + o(1)) β. Putting this
bound into perspective, if we assume that a user will rate a minimally preferred alternative over a
10Why not define distortion by flexibly selecting the benchmark based on the output policy’s KL divergence? For
this definition, an alignment method that always returns the reference policy would spuriously achieve distortion 1:
because its KL divergence is 0, we would benchmark it only against the reference policy, i.e., itself.
11The finite-sample bounds even improve in the latter model since each pair appears only once.
12


Page 13:
maximally preferred alternative with 1% probability, this suggests a value of β = log 99%
1% ≈4.60
and a distortion guarantee of about 2.34, which is a quite reasonable worst-case guarantee.
For the incumbent method, RLHF, our analysis gave more negative results. Its distortion was
worse than NLHF’s in the unconstrained setting, exponentially worse in the constrained setting, and
unbounded if the comparison pairs are not drawn i.i.d.. Given the ubiquity of RLHF, characterizing
its distortion is a pressing open question, especially when the distribution µ for drawing comparison
pairs coincides with the reference policy, or finding similar assumptions that guarantee a lower
distortion. A major technical difficulty in this is that bounding this distortion requires reasoning
not only about the relative ordering of rewards but also their magnitudes.
The distortion framework opens up many more questions: How large is the distortion of alignment
methods besides RLHF, DPO, and NLHF? Can we extend the model to take into account the
generalization of preferences across states? Can the lower bound on distortion be overcome with a
little additional information? Finally: can we extend our model to go beyond average utility and
measure fairness?12 After all, high average utility is necessary, but not sufficient, for successful
alignment to a heterogeneous population.
Acknowledgments
We thank Mark Bedaywi, Jim Dai, Sonja Kraiczy, Soroosh Shafiee, and Eric Zhao for helpful
conversations. This work was supported in part by the National Science Foundation under grant
CCF-2145898, by the Office of Naval Research under grant N00014-24-1-2159, an Alfred P. Sloan
fellowship, and a Schmidt Sciences AI2050 fellowship. Part of this work was performed while P.G.
was at the Simons Institute for the Theory of Computing as a FODSI research fellow, for which he
acknowledges the NSF’s support through grant DMS-2023505.
References
AI Incident Database. URL https://incidentdatabase.ai/. 1
Mayer Alvo and LH Philip. Statistical methods for ranking data, volume 1341. Springer, 2014. A
Elliot Anshelevich, Onkar Bhardwaj, Edith Elkind, John Postl, and Piotr Skowron. Approximating
optimal social choice under metric preferences. Artificial Intelligence, 264:27–51, 2018. 3.3, A
Elliot Anshelevich, Aris Filos-Ratsikas, Nisarg Shah, and Alexandros A. Voudouris. Distortion in
social choice problems: The first 15 years and beyond. In Zhi-Hua Zhou, editor, Proceedings of
the Thirtieth International Joint Conference on Artificial Intelligence, pages 4294–4301, 2021. 1,
3.3, A
Mohammad Gheshlaghi Azar, Zhaohan Daniel Guo, Bilal Piot, Remi Munos, Mark Rowland, Michal
Valko, and Daniele Calandriello. A general theoretical paradigm to understand learning from
human preferences. In International Conference on Artificial Intelligence and Statistics, pages
4447–4455. PMLR, 2024. 1, A
Hossein Azari Soufiani, David C Parkes, and Lirong Xia. A statistical decision-theoretic framework
for social choice. Advances in Neural Information Processing Systems, 27, 2014. A
12The concept of distortion of proportional fairness by Ebadian et al. [2024b] points in one possible direction.
13


Page 14:
Yuntao Bai, Andy Jones, Kamal Ndousse, Amanda Askell, Anna Chen, Nova DasSarma, Dawn
Drain, Stanislav Fort, Deep Ganguli, Tom Henighan, et al. Training a helpful and harmless
assistant with reinforcement learning from human feedback. arXiv preprint arXiv:2204.05862,
2022a. A
Yuntao Bai, Saurav Kadavath, Sandipan Kundu, Amanda Askell, Jackson Kernion, Andy Jones,
Anna Chen, Anna Goldie, Azalia Mirhoseini, Cameron McKinnon, et al. Constitutional ai:
Harmlessness from ai feedback. arXiv preprint arXiv:2212.08073, 2022b. 1
Gerdus Benade, Swaprava Nath, Ariel D. Procaccia, and Nisarg Shah. Preference elicitation for
participatory budgeting. Management Science, 67(5):2813–2827, 2021. A
Craig Boutilier, Ioannis Caragiannis, Simi Haber, Tyler Lu, Ariel D. Procaccia, and Or Sheffet.
Optimal social choice functions: A utilitarian view. In Proceedings of the 13th ACM Conference
on Electronic Commerce, pages 197–214. ACM, 2012. 1, 3, A
Daniele Calandriello, Zhaohan Daniel Guo, Remi Munos, Mark Rowland, Yunhao Tang,
Bernardo Avila Pires, Pierre Harvey Richemond, Charline Le Lan, Michal Valko, Tianqi Liu,
et al. Human alignment of large language models through online preference optimisation. In
Proceedings of the 41st International Conference on Machine Learning, pages 5409–5435, 2024. A
Ioannis Caragiannis and Ariel D. Procaccia. Voting almost maximizes social welfare despite limited
communication. Artificial Intelligence, 175(9-10):1655–1671, 2011. 3, 3.3, A
Souradip Chakraborty, Jiahao Qiu, Hui Yuan, Alec Koppel, Furong Huang, Dinesh Manocha,
Amrit Singh Bedi, and Mengdi Wang. Maxmin-RLHF: Alignment with diverse human preferences.
arXiv preprint arXiv:2402.08925, 2024. 1, A
Moses Charikar, Prasanna Ramakrishnan, Kangning Wang, and Hongxun Wu. Breaking the Metric
Voting Distortion Barrier. Journal of the ACM, 71(6):1–33, 2024. 3.3, A
Daiwei Chen, Yi Chen, Aniket Rege, and Ramya Korlakai Vinayak. Pal: Pluralistic alignment
framework for learning from heterogeneous preferences. arXiv preprint arXiv:2406.08469, 2024. A
Wei-Lin Chiang, Lianmin Zheng, Ying Sheng, Anastasios Nikolas Angelopoulos, Tianle Li, Dacheng
Li, Banghua Zhu, Hao Zhang, Michael Jordan, Joseph E Gonzalez, et al. Chatbot arena: An
open platform for evaluating llms by human preference. In Forty-first International Conference
on Machine Learning, 2024. 1.1, 3.3
Keertana Chidambaram, Karthik Vinay Seetharaman, and Vasilis Syrgkanis. Direct preference
optimization with unobserved preference heterogeneity. arXiv preprint arXiv:2405.15065, 2024. A
Paul F Christiano, Jan Leike, Tom Brown, Miljan Martic, Shane Legg, and Dario Amodei. Deep
reinforcement learning from human preferences.
Advances in neural information processing
systems, 30, 2017. 1
Vincent Conitzer and Tuomas Sandholm. Common voting rules as maximum likelihood estimators.
In Proceedings of the Twenty-First Conference on Uncertainty in Artificial Intelligence, pages
145–152, 2005. A
Vincent Conitzer, Rachel Freedman, Jobst Heitzig, Wesley H Holliday, Bob M Jacobs, Nathan
Lambert, Milan Moss´e, Eric Pacuit, Stuart Russell, Hailey Schoelkopf, et al. Position: social
14


Page 15:
choice should guide ai alignment in dealing with diverse human feedback. In Proceedings of the
41st International Conference on Machine Learning, pages 9346–9360, 2024. 1, A
Jessica Dai and Eve Fleisig. Mapping social choice theory to RLHF. In ICLR 2024 Workshop on
Reliable and Responsible Foundation Models, 2024. 1, A
Soroush Ebadian, Daniel Halpern, and Evi Micha. Metric distortion with elicited pairwise compar-
isons. In Proceedings of the 33rd International Joint Conference on Artificial Intelligence (IJCAI),
pages 2791–2798, 2024a. 1
Soroush Ebadian, Anson Kahng, Dominik Peters, and Nisarg Shah. Optimized Distortion and
Proportional Fairness in Voting. ACM Transactions on Economics and Computation, 12(1):1–39,
2024b. 3, 3, 12, A
Kawin Ethayarajh, Winnie Xu, Niklas Muennighoff, Dan Jurafsky, and Douwe Kiela. KTO: Model
alignment as prospect theoretic optimization. arXiv preprint arXiv:2402.01306, 2024. 1
Peter C. Fishburn. Probabilistic social choice based on simple voting comparisons. The Review of
Economic Studies, 51(4):683–692, 1984. 1.1
Bailey Flanigan, Ariel D Procaccia, and Sven Wang. Distortion Under Public-Spirited Voting. In
Proceedings of the 24th ACM Conference on Economics and Computation, EC ’23, page 700.
Association for Computing Machinery, 2023. A
Luise Ge, Daniel Halpern, Evi Micha, Ariel D Procaccia, Itai Shapira, Yevgeniy Vorobeychik, and
Junlin Wu. Axioms for AI alignment from human feedback. arXiv preprint arXiv:2405.14758,
2024. A
Vasilis Gkatzelis, Daniel Halpern, and Nisarg Shah.
Resolving the optimal metric distortion
conjecture. In 2020 IEEE 61st Annual Symposium on Foundations of Computer Science (FOCS),
pages 1427–1438. IEEE, 2020. 3.3, A
Mohak Goyal and Sahasrajit Sarmasarkar. Metric distortion under probabilistic voting. arXiv
preprint arXiv:2405.14223v4, 2025. 1, 1.1, 3.3, A
Audrey Huang, Wenhao Zhan, Tengyang Xie, Jason D Lee, Wen Sun, Akshay Krishnamurthy,
and Dylan J Foster. Correcting the mythos of KL-regularization: Direct alignment without
overoptimization via chi-squared preference optimization. arXiv preprint arXiv:2407.13399, 2024.
1, 4.2, A
Fatih Erdem Kizilkaya and David Kempe. Plurality Veto: A Simple Voting Rule Achieving Optimal
Metric Distortion. In Proceedings of the Thirty-First International Joint Conference on Artificial
Intelligence, pages 349–355. International Joint Conferences on Artificial Intelligence Organization,
2022. A
Zhihan Liu, Miao Lu, Shenao Zhang, Boyi Liu, Hongyi Guo, Yingxiang Yang, Jose Blanchet, and
Zhaoran Wang. Provably mitigating overoptimization in RLHF: Your SFT loss is implicitly an
adversarial regularizer. In The Thirty-eighth Annual Conference on Neural Information Processing
Systems, 2024. A
Roberto-Rafael Maura-Rivero, Marc Lanctot, Francesco Visin, and Kate Larson. Jackpot! alignment
as a maximal lottery. arXiv preprint arXiv:2501.19266, 2025. A
15


Page 16:
Yu Meng, Mengzhou Xia, and Danqi Chen. SimPO: Simple preference optimization with a reference-
free reward. Advances in Neural Information Processing Systems, 37:124198–124235, 2024. 1,
A
Abhilash Mishra. Ai alignment and social choice: Fundamental limitations and policy implications.
arXiv preprint arXiv:2310.16048, 2023. A
Remi Munos, Michal Valko, Daniele Calandriello, Mohammad Gheshlaghi Azar, Mark Rowland,
Zhaohan Daniel Guo, Yunhao Tang, Matthieu Geist, Thomas Mesnard, Cˆome Fiegel, et al.
Nash learning from human feedback. In International Conference on Machine Learning, pages
36743–36768. PMLR, 2024. 1.1, 1, 2, A, 13
Ritesh Noothigattu, Dominik Peters, and Ariel D Procaccia. Axioms for learning from pairwise
comparisons. Advances in Neural Information Processing Systems, 33:17745–17754, 2020. A
Long Ouyang, Jeffrey Wu, Xu Jiang, Diogo Almeida, Carroll Wainwright, Pamela Mishkin, Chong
Zhang, Sandhini Agarwal, Katarina Slama, Alex Ray, et al. Training language models to follow
instructions with human feedback. Advances in Neural Information Processing Systems, 35:
27730–27744, 2022. 1
Chanwoo Park, Mingyang Liu, Dingwen Kong, Kaiqing Zhang, and Asuman Ozdaglar. RLHF
from heterogeneous feedback via personalization and preference aggregation. arXiv preprint
arXiv:2405.00254, 2024. A
Sriyash Poddar, Yanming Wan, Hamish Ivison, Abhishek Gupta, and Natasha Jaques. Personalizing
reinforcement learning from human feedback with variational preference learning. In The Thirty-
eighth Annual Conference on Neural Information Processing Systems, 2024. A
Ariel D. Procaccia and Jeffrey S. Rosenschein. The distortion of cardinal preferences in voting. In
International Workshop on Cooperative Information Agents, pages 317–331. Springer, 2006. 1,
3.1, 3.3, A
Ariel D Procaccia, Benjamin Schiffer, and Shirley Zhang. Clone-robust ai alignment. arXiv preprint
arXiv:2501.09254, 2025. 5, A, A, E.2
Rafael Rafailov, Archit Sharma, Eric Mitchell, Christopher D Manning, Stefano Ermon, and Chelsea
Finn. Direct preference optimization: Your language model is secretly a reward model. Advances
in Neural Information Processing Systems, 36:53728–53741, 2023. 1, 1.1, 7, A, E.3
John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov. Proximal policy
optimization algorithms. arXiv preprint arXiv:1707.06347, 2017. 2, A
Ali Shirali, Arash Nasr-Esfahany, Abdullah Alomar, Parsa Mirtaheri, Rediet Abebe, and Ariel
Procaccia. Direct alignment with heterogeneous preferences. arXiv preprint arXiv:2502.16320,
2025. 2, E.3
Anand Siththaranjan, Cassidy Laidlaw, and Dylan Hadfield-Menell. Distributional preference learn-
ing: Understanding and accounting for hidden context in RLHF. arXiv preprint arXiv:2312.08358,
2023. 3.1, 5, A, A, E.2, F
Taylor Sorensen, Jared Moore, Jillian Fisher, Mitchell Gordon, Niloofar Mireshghallah, Christo-
pher Michael Rytting, Andre Ye, Liwei Jiang, Ximing Lu, Nouha Dziri, et al. Position: a roadmap
16


Page 17:
to pluralistic alignment. In Proceedings of the 41st International Conference on Machine Learning,
pages 46280–46302, 2024. 1
Gokul Swamy, Christoph Dann, Rahul Kidambi, Zhiwei Steven Wu, and Alekh Agarwal. A minimaxi-
malist approach to reinforcement learning from human feedback. arXiv preprint arXiv:2401.04056,
2024. A
Gokcan Tatli, Yi Chen, and Ramya Korlakai Vinayak. Learning populations of preferences via
pairwise comparison queries. In International Conference on Artificial Intelligence and Statistics,
pages 1720–1728. PMLR, 2024. A
Yuanhao Wang, Qinghua Liu, and Chi Jin. Is RLHF more difficult than standard RL? a theoretical
perspective. Advances in Neural Information Processing Systems, 36:76006–76032, 2023. A
Zhi Wang, Geelon So, and Ramya Korlakai Vinayak. Metric learning from limited pairwise preference
comparisons. In Uncertainty in Artificial Intelligence, pages 3571–3602. PMLR, 2024. A
Yue Wu, Zhiqing Sun, Huizhuo Yuan, Kaixuan Ji, Yiming Yang, and Quanquan Gu. Self-play
preference optimization for language model alignment. arXiv preprint arXiv:2405.00675, 2024. A
Lirong Xia. Bayesian estimators as voting rules. In Uncertainty in artificial intelligence, 2018. A
Lirong Xia. Learning and decision-making from rank data. Morgan & Claypool Publishers, 2019. A
Xiaomin Zhang, Xucheng Zhang, Po-Ling Loh, and Yingyu Liang. On the identifiability of mixtures
of ranking models. arXiv preprint arXiv:2201.13132, 2022. 2, A
Zhibing Zhao and Lirong Xia. Learning mixtures of plackett-luce models from structured partial
orders. Advances in Neural Information Processing Systems, 32, 2019. 2, A
Zhibing Zhao, Peter Piech, and Lirong Xia.
Learning mixtures of plackett-luce models.
In
Maria Florina Balcan and Kilian Q. Weinberger, editors, Proceedings of The 33rd International
Conference on Machine Learning, volume 48 of Proceedings of Machine Learning Research, pages
2906–2914, New York, New York, USA, 2016. PMLR. 2, A
Huiying Zhong, Zhun Deng, Weijie J Su, Zhiwei Steven Wu, and Linjun Zhang. Provable multi-party
reinforcement learning with diverse human feedback. arXiv preprint arXiv:2403.05006, 2024. A
Daniel M Ziegler, Nisan Stiennon, Jeffrey Wu, Tom B Brown, Alec Radford, Dario Amodei, Paul
Christiano, and Geoffrey Irving. Fine-tuning language models from human preferences. arXiv
preprint arXiv:1909.08593, 2019. 1, 1, A
17


Page 18:
A
Additional Related Work
Reward-based and reward-free alignment methods.
The RLHF pipeline typically includes
first training a reward model via maximum likelihood estimation (MLE), then applying RL algorithms
such as Proximal Policy Optimization (PPO) [Schulman et al., 2017] to optimize a policy that
maximizes the reward [Ziegler et al., 2019, Bai et al., 2022a]. Rafailov et al. [2023] proposes
an alternative approach, Direct Preference Optimization (DPO), which bypasses explicit reward
model training by directly optimizing an equivalent objective derived from the closed form of
KL-constrained reward-maximizing policy. While the original formulation is based on a single
Bradley–Terry model, we show in Appendix E.4 that the equivalence extends to settings with
heterogeneous preferences. Building on the DPO framework, several recent methods including
χPO [Huang et al., 2024], RPO [Liu et al., 2024] and SimPO [Meng et al., 2024] have been proposed
to improve the robustness and effectiveness.
Azar et al. [2024] introduce ΨPO, another reward-free method that optimizes the expectation
of a Ψ-transformation of the win-rates estimated from the offline comparison data. When Ψ is
the identity function, the resulting method — IPO — reduces to directly optimizing the normalized
Borda count. Since RLHF is implicitly optimizing the normalized Borda count [Siththaranjan et al.,
2023, Procaccia et al., 2025], this connection implies that IPO, DPO, and RLHF are all equivalent
in the unregularized/unconstrained setting.
Another reward-free method is Nash Learning from Human Feedback (NLHF) [Munos et al.,
2024] and its variants [Swamy et al., 2024, Wu et al., 2024, Calandriello et al., 2024], which finds
the Nash equilibrium of a game defined over the win-rate margins (i.e., p(x ≻y) −p(y ≻x)) via
online learning or self-play style algorithms. Maura-Rivero et al. [2025] point out that NLHF can be
viewed as a natural generalization of the Maximal Lotteries rule in social choice. Wang et al. [2023]
consider finding the Nash equilibrium of the win-rate matrix and reduce the problem to multiagent
reward-based RL. They provide an impossibility result, showing the optimal policy is indeterminate
when the underlying ranking model (e.g., Bradley-Terry with certain temperature) is unknown.
In contrast, our results show that even when the ranking model is known, the optimal policy can
remain nonidentifiable due to preference heterogeneity.
AI Alignment under heterogeneous user preferences.
A growing body of recent works
studies algorithms for AI alignment under heterogeneous user preferences. Siththaranjan et al.
[2023] points out that RLHF implicitly optimizes the normalized Borda count, which can lead to
poor outcomes in the social choice setting. To address this, they propose Distributional Preference
Learning (DPL), a method that estimates a distribution of score values for each alternative. Another
line of work deals with heterogeneity by clustering user preferences and learning several reward
models at once, then aggregate the learned reward models using various techniques such as max-min
optimization, which optimizes the worst-case reward among all clusters [Chidambaram et al., 2024,
Chakraborty et al., 2024], or through aggregation rules motivated by axiomatic properties in social
choice theory [Zhong et al., 2024, Park et al., 2024]. Poddar et al. [2024] proposes a variational
inference approach that infers user-specific latent variables from preference data which enables
steerable personalized language models. Chen et al. [2024] proposes a framework based on the ideal
point model, which learns a latent space of user preferences that can few-shot generalize to unseen
users.
Statistical and Axiomatic Perspectives on Preference Aggregation.
Maximum likelihood
estimators (MLE), which serves as the core of the widely-used RLHF pipeline, can be viewed as
voting rules: given a set of rankings, they output a score for each alternative, thereby producing a
18


Page 19:
single aggregated ranking. This connection was first observed by Conitzer and Sandholm [2005],
who show that any scoring-based voting rule is a maximum likelihood estimator under a specific
noise model. A rich literature in social choice theory has studied the axiomatic properties of such
MLE-based voting rules under various randomized ranking models [Azari Soufiani et al., 2014, Xia,
2018, Noothigattu et al., 2020, Ge et al., 2024, Procaccia et al., 2025]. Notably, Ge et al. [2024]
analyzes the axiomatic properties of MLE-based AI alignment methods under the Bradley-Terry
model for linear utility functions.
On the learning side, several works study the problem of learning mixture models from ranking
data, see textbooks [Alvo and Philip, 2014, Xia, 2019] for a comprehensive overview. Recently,
Wang et al. [2024], Tatli et al. [2024] focus on learning metric spaces from pairwise preferences. Our
work is notably related to the results on the non-identifiability of learning mixture of Bradley-Terry
models from pairwise or k-wise preferences [Zhao et al., 2016, Zhao and Xia, 2019, Zhang et al.,
2022]. We build on these results to quantify the loss of utility due to non-identifiability by proving
a voting-rule independent distortion lower bound.
Distortion of randomized voting and RLHF.
The framework of implicit utilitarian voting, i.e.,
of comparing voting rules in terms of their distortion was introduced by Procaccia and Rosenschein
[2006], which has since sparked a large body of work — both in the original utility setting [Caragiannis
and Procaccia, 2011, Boutilier et al., 2012, Ebadian et al., 2024b, Flanigan et al., 2023, Benade
et al., 2021] and in the metric setting [Anshelevich et al., 2018, 2021, Gkatzelis et al., 2020, Charikar
et al., 2024, Kizilkaya and Kempe, 2022]. Several recent works have highlighted the importance of
using distortion as a metric to evaluate the quality of AI alignment methods. Dai and Fleisig [2024]
draw a conceptual connection between social choice and RLHF, and propose to apply the notion
of distortion to RLHF. Goyal and Sarmasarkar [2025] uses alignment as motivation for studying
the metric distortion of probabilistic voting rules under Bradley-Terry and other random utility
models, where the voters and candidates are assumed to lie in a common metric space satisfying
triangle inequality. We not only study the non-metric distortion (which is more expressive), but
also go beyond the social choice setting to consider the alignment setting in which output policies
are constrained to remain close to a given reference policy. More broadly, our work also contributes
to the growing line of research on the intersection of social choice theory and RLHF, as advocated
in recent position papers [Conitzer et al., 2024, Mishra, 2023].
B
Linearization Lemma for Expected Win-Rates
Lemma 1 (Linearization of Expected Win-Rates). Let L := σ′(0) = 1/4 and ℓβ :=
σ(β)−1
2
β
=
1
2β · 1−e−β
1+e−β . For any pair of alternatives x, y ∈A, we have
β · (ℓβ · AvgUtil(x) −L · AvgUtil(y)) ≤p(x ≻y) −1
2 ≤β · (L · AvgUtil(x) −ℓβ · AvgUtil(y)) .
Proof of Lemma 1. We prove this lemma by linearizing the sigmoid function σ(z) =
1
1+e−z in the
domain of z ∈[−β, β]. When z ∈[0, β], the sigmoid function is concave and increasing, thus we have
σ(z) ≤σ′(0) · z + σ(0) = 1
2 + Lz, where L = 1
4 is the derivative σ′(0). When z ∈[−β, 0], the sigmoid
function is convex, thus we have σ(z) ≤

1 + z
β

σ(0) −z
βσ(−β) = 1
2 + lβ · z, where lβ =
σ(β)−1
2
β
is
the slope of the line connecting (−β, σ(−β)) and (0, σ(0)).
19


Page 20:
Plugging the above bounds into σ

β · (u(x) −u(y))

, we have that
σ

β · (u(x) −u(y))

−1
2 ≤β · (u(x) −u(y)) ·
 L · 1u(x)−u(y)≥0 + lβ · 1u(x)−u(y)<0

≤β · (L · u(x) −lβ · u(y)) .
Finally, taking an expectation over u ∼D, we have that
p(x ≻y) −1
2 ≤β

L · E
u∼D [u(x)] −lβ · E
u∼D [u(y)]

= β (L · AvgUtil(x) −lβ · AvgUtil(y)) .
This completes the proof of the upper bound. The lower bound follows from applying the same
argument to p(y ≻x) and using the fact that p(x ≻y) = 1 −p(y ≻x).
C
Finite-Sample Convergence Bounds
In this section, we use standard concentration techniques to derive finite-sample convergence bounds
for the normalized Borda score and the empirical win rate. The lemmas presented in this section
will serve as a building block for proving finite-sample guarantees for the alignment methods studied
in Sections 3 and 4.
C.1
Estimation Error of Win-Rates
Lemma 10. For any instance D with any number of alternatives m, any distribution µ over
alternatives with µmin = minx∈A µ(x), and n i.i.d. users sampled from D where each user labels d
comparison pairs following the Bradley-Terry model with temperature β, we have that with probability
at least 1 −δ where δ ≥m2 exp

−ndµ2
min
8

, the empirical win rates pn(x ≻y) :=
#(x≻y)
#(x≻y)+#(y≻x)
satisfies that:
∀x, y ∈A,
|pn(x ≻y) −p(x ≻y)| ≤O
 s
log(m/δ)
n · min{1, d · µ2
min} + log(m/δ)
nµ2
min
!
.
Proof of Lemma 10. We first bound the estimation error of pn(x ≻y) for a fixed pair x, y ∈
 A
2

.
Here we assume x ̸= y without loss of generality, because the estimation error for the x = y case is
0.
Since each voter i ∈[n] is asked to label d pairwise comparisons, if each of them are asked to
label a pair {x, y} multiple times, their answer will be consistent. Therefore, we can equivalently
rewrite the process of sampling pn(x ≻y) as follows:
1. Draw k1, . . . , kn
i.i.d.
∼Binomial(d, q) to represent the number of times the i-th voter is asked to
label {x, y}, where q := 2µ(x)µ(y) is the probability that each comparison pair is {x, y};
2. Draw p1, . . . , pn
i.i.d.
∼Bernoulli(p) to represent the preference of the i-th voter on pair {x, y},
where p := p(x ≻y) is the probability that a fresh voter prefers x over y. In particular, we
have pi ⊥ki because the sampling of voters and comparison pairs are independent;
3. Each voter i ∈[n] contributes ki · pi to #(x ≻y) and ki · (1 −pi) to #(y ≻x).
20


Page 21:
As a result, the empirical win rate pn(x ≻y) can be rewritten as:
pn(x ≻y) =
#(x ≻y)
#(x ≻y) + #(y ≻x) =
Pn
i=1 kipi
Pn
i=1 ki
.
The error term is then given by:
pn(x ≻y) −p(x ≻y) =
Pn
i=1 kipi
Pn
i=1 ki
−p =
Pn
i=1 ki(pi −p)
Pn
i=1 ki
.
Now we use Bernstein’s inequality to bound the numerator. We start by bounding the variance
of random variable Zi := ki(pi −p). Note that E [Zi] = E [ki] · E [pi −p] = 0 because ki and pi −p
are independent. Therefore, we have
Var (Zi) = E

Z2
i

= E

k2
i

· E

(pi −p)2
≤E

k2
i

= Var (ki) + (E [ki])2 = dq(1 −q) + d2q2.
According to Bernstein’s inequality, we have that with probability at least 1 −δ,

n
X
i=1
Zi
 =

n
X
i=1
ki(pi −p)
 ≤
p
2n(dq(1 −q) + d2q2) log(2/δ) + 3d log(2/δ).
(3)
Now we bound the denominator. Note that E [ki] = dq and Var (ki) = dq(1 −q). From the Chernoff
bound, we have that with probability at least 1 −e−ndq
8 ,
n
X
i=1
ki ≥n E [ki]
2
= ndq
2 .
(4)
Combining the bounds in Equation (3) and Equation (4), we have that when δ ≥e−ndq
8 , with
probability at least 1 −2δ, for a fixed pair x, y ∈A, we have
|pn(x ≻y) −p(x ≻y)| ≤
p
2n(dq(1 −q) + d2q2) log(2/δ) + 3d log(2/δ)
ndq/2
≤O
 s
(1 −q + dq) log(1/δ)
ndq
+ log(1/δ)
nq
!
where we use the fact that 1−q+dq
dq
≤
2
min{1,dq} and q = 2µ(x)µ(y) ≥µ2
min to obtain:
≤O
 s
log(1/δ)
n min{1, d · µ2
min} + log(1/δ)
nµ2
min
!
.
Finally, by union bound over all
 m
2

pairs, we have that with probability at least 1 −δ where
δ ≥m2 exp

−ndµ2
min
8

, the following holds simultaneously for all x, y ∈A:
|pn(x ≻y) −p(x ≻y)| ≤O
 s
log(m/δ)
n · min{1, d · µ2
min} + log(m/δ)
nµ2
min
!
.
The proof is complete.
21


Page 22:
C.2
Estimation Error of Normalized Borda Score
Lemma 11. For any instance D with any number of alternatives m, any distribution µ over
alternatives with µmin = minx∈A µ(x), and n i.i.d. users sampled from D where each user labels d
comparison pairs, the normalized Borda score BCn(x) of any alternative x ∈A satisfies that with
probability at least 1 −δ where δ ≥2m exp(−ndµmin
8
),
∀x ∈A,
|BCn(x) −BC⋆(x)| ≤O
 s
log(m/δ)
n · min{1, d · µ2
min} + m log(m/δ)
nµmin
!
,
(5)
where BC⋆(x) is the limiting normalized Borda score of candidate x, defined as
BC⋆(x) :=
X
y∈A
µ(y) · p(x ≻y) = 1
2µ(x) +
X
y̸=x
µ(y) · p(x ≻y).
(6)
Proof. We first bound the estimation error |BCn(x) −BC⋆(x)| for a fixed alternative x ∈A. For
notational simplicity, we use Tn(x) to denote the number of comparison pairs involving x, and
Wn(x) to denote the number of comparison pairs where x is the winner, i.e.,
Tn(x) = 2#(x ≻x) +
X
y̸=x
#(x ≻y) + #(y ≻x),
Wn(x) = #(x ≻x) +
X
y̸=x
#(x ≻y).
The normalized Borda score of x is then given by BCn(x) = Wn(x)
Tn(x) . It is then easy to see that
E [Tn(x)] = nd

2µ(x)2 +
X
y̸=x
2µ(x)µ(y)

= 2ndµ(x);
E [Wn(x)] = nd

µ(x)2 +
X
y̸=x
µ(x)µ(y)p(x ≻y)

= ndµ(x)

1
2µ(x) +
X
y̸=x
µ(y)p(x ≻y)

.
The limiting Borda score BC⋆(x) is then given by the ratio of the above two expectations, i.e.,
BC⋆(x) = E [Wn(x)]
E [Tn(x)] = 1
2µ(x) +
X
y̸=x
µ(y)p(x ≻y).
We can thus decompose the estimation error |BCn(x) −BC⋆(x)| as follows:
|BCn(x) −BC⋆(x)| =

Wn(x)
Tn(x) −E [Wn(x)]
E [Tn(x)]

≤|Wn(x) −E [Wn(x)] |
Tn(x)
+ E [Wn(x)]
E [Tn(x)]
|
{z
}
BC⋆(x)≤1
·|Tn(x) −E [Tn(x)]|
Tn(x)
≤|Wn(x) −E [Wn(x)] |
Tn(x)
+ |Tn(x) −E [Tn(x)]|
Tn(x)
.
Now we bound the two terms |Wn(x) −E [Wn(x)] | and |Tn(x) −E [Tn(x)] | separately, and apply
the union bound at the end.
22


Page 23:
(I). Bounding |Wn(x) −E [Wn(x)] |:
For each y ̸= x, we can write bound the deviation |#(x ≻
y) −E [#(x ≻y)] | using the same argument as in the proof of Lemma 10. Specifically, we can
write #(x ≻y) as a sum of i.i.d. random variables kipi where ki ∼Binomial(d, qx,y) and pi ∼
Bernoulli(p(x ≻y)), where qx,y = 2µ(x)µ(y) is the probability that each comparison pair is {x, y}.
Therefore, we have
Var (kipi) = Var (ki) · Var (pi) + Var (ki) E

p2
i

+ Var (pi) E [ki]2
≤2dqx,y(1 −qx,y + dqx,y)
since 1 −qx,y + dqx,y ≤
2dqx,y
min{1,dqx,y} ≤
2dqx,y
min{1,dµ2
min}, we can further bound the variance as
≤
2(dqx,y)2
min{1, dµ2
min} = 8(dµ(x)µ(y))2
min{1, dµ2
min}.
Thus, by Bernstein’s inequality, with probability at least 1 −δ′,
#(x ≻y) −E [#(x ≻y)]
 ≤4dµ(x)µ(y)
s
n log(2/δ′)
min{1, d · µ2
min} + 3d log(2/δ′).
On the other hand, for the comparison of x with itself, we have that #(x ≻x) ∼Binomial(nd, µ(x)2).
Therefore, with probability at least 1 −δ′,
#(x ≻x) −E [#(x ≻x)]
 ≤
p
2ndµ(x)2 log(2/δ′) + 3d log(2/δ′)
≤4dµ(x)2
s
n log(2/δ′)
min{1, d · µ2
min} + 3d log(2/δ′).
Applying a union bound over all the m alternatives y ∈A, we have that with probability at
least 1 −mδ′,
|Wn(x) −E [Wn(x)] | ≤
X
y̸=x
#(x ≻y) −E [#(x ≻y)]

≤
X
y̸=x
 
4dµ(x)µ(y)
s
n log(2/δ′)
min{1, d · µ2
min} + 3d log(2/δ′)
!
≤4dµ(x)
s
n log(2/δ′)
min{1, d · µ2
min} + 3md log(2/δ′).
(II). Bounding |Tn(x) −E [Tn(x)] |:
We can write Tn(x) as a sum of i.i.d. random variables:
Tn =
n
X
i=1
d
X
j=1
(1xj
i =x + 1yj
i =x)
Since each comparison pair xj
i, yj
i is sampled independently from µ × µ, we have that Tn ∼
Binomial(2nd, µ(x)). Therefore, with probability at least 1 −δ′,
Tn(x) −E [Tn(x)]
 ≤2
p
ndµ(x) log(2/δ′) + 3 log(2/δ′).
In addition, with probability at least 1 −exp(−ndµ(x)
4
), we also have
Tn ≥E [Tn]
2
= ndµ(x).
23


Page 24:
(III). Combining the two bounds:
Finally, combining the above bounds on |Wn(x)−E [Wn(x)] |
and |Tn(x) −E [Tn(x)] |, together with the bound on the denominator Tn(x), we have that with
probability at least 1 −2mδ′ −exp(−ndµ(x)
4
),
|BCn(x) −BC⋆(x)| ≤|Wn(x) −E [Wn(x)] |
Tn(x)
+ |Tn(x) −E [Tn(x)]|
Tn(x)
≲
1
ndµ(x)
 
dµ(x)
s
n log(1/δ′)
min{1, d · µ2
min} + md log(1/δ′) +
p
ndµ(x) log(2/δ′)
!
≲
s
log(1/δ′)
n · min{1, d · µ2
min} + m log(1/δ′)
nµmin
.
Finally, setting δ′ =
δ
4m2 and taking a union bound over all the m alternatives x ∈A, we have that
when δ ≥2m exp(−ndµmin
8
), with probability at least 1 −δ, the above bound holds simultaneously
for all x ∈A. This completes the proof.
D
Supplemental Materials for Section 3
D.1
Upper Bound for Borda
Theorem 2 (Borda Distortion Upper Bound). For any instance D with any number of alternatives
m, distribution µ over alternatives, and temperature β, Borda has at most distortion
  β
2 · 1+e−β
1−e−β
2 =
O(β2). In the finite-sample regime, we have that
AvgUtiln(Borda) ≥
  2
β · 1−e−β
1+e−β
2 · maxx⋆∈A AvgUtil(x⋆) −O

1
β2
q
log(mnβ)
n·min{1,dµ2
min} + m log(mnβ)
n·β2µ2
min

.
Proof of Theorem 2. From Lemma 11, we have that with probability at least 1 −δ, all x ∈A satisfy
that |BCn(x) −BC⋆(x)| ≤εn,d(δ), where
εn,d(δ) = O
 s
log(m/δ)
n · min{1, d · µ2
min} + m log(m/δ)
nµmin
!
.
Following the proof sketch in Section 3.1, we use ˆx = argmaxx∈A BCn(x) to denote the Borda winner,
and x⋆= argmaxx∈A AvgUtil(x) to denote the true utility maximizer.
Since BCn(ˆx) ≥BCn(x⋆), we have
BC⋆(ˆx) −BC⋆(x⋆) ≥−2εn,d(δ).
(7)
For the limiting Borda score BC⋆(x), the argument in Section 3.1 shows that
BC⋆(ˆx) −BC⋆(x⋆) ≤β · (L · AvgUtil(ˆx) −ℓβ · AvgUtil(x⋆) + (L −ℓβ) · AvgUtil(µ))
≤β ·
L2
ℓβ
· AvgUtil(ˆx) −ℓβ · AvgUtil(x⋆)

(8)
Therefore, Combining Equations (7) and (8), we have
−2εn,d(δ) ≤β ·
L2
ℓβ
· AvgUtil(ˆx) −ℓβ · AvgUtil(x⋆)

⇒AvgUtil(ˆx) ≥
ℓβ
L
2
AvgUtil(x⋆) −2ℓβ · εn,d(δ)
βL2
.
24


Page 25:
Combining this with the failure probability δ of the above argument, the average utility AvgUtiln(Borda)
satisfies that
AvgUtiln(Borda) ≥(1 −δ) ·
 ℓβ
L
2
AvgUtil(x⋆) −2ℓβ · εn,d(δ)
βL2
!
≥
ℓβ
L
2
AvgUtil(x⋆) −O
 
εn,d(δ)
β
·
ℓβ
L

+ δ ·
ℓβ
L
2!
.
Finally, we set the failure probability to be
δ = Θ
 
L
β · ℓβ
·
s
1
n · min{1, d · µ2
min}
!
(which satisfies the condition in Lemma 11 for large n), we have
AvgUtiln(Borda) ≥
ℓβ
L
2
AvgUtil(x⋆) −O
 
1
β2
s
log(mnβ)
n · min{1, dµ2
min} + m log(mnβ)
n · β2µ2
min
!
,
which completes the proof.
D.2
Lower Bound for Borda
0
2
5
10
20
50
∞
β
0.5
0.75
1
1.25
1.5
distortion
β
NLHF/Maximum Lotteries
RLHF/Borda lower bound
Figure 3: Comparison of the distortion achieved by NLHF/Maximum Lotteries and the lower bound
on RLHF/Borda in Theorem 5, both as a fraction of β. The figure illustrates that NLHF has a
worse distortion for every value of β > 0 (for worst-case distributions µ); in particular, the distortion
of RLHF for large β is at least β −o(β), whereas the distortion of NLHF is β/2 + o(β).
Theorem 12 (Lower Bound for Borda; Formal Version of Theorem 5). For any β > 0 and
m ≥3, the Borda voting rule (and, hence, RHLF) cannot guarantee a distortion better than
max0<γ<1
β
2
1+e−β
1−e−β ·
 1−γ + σ(βγ)−1/2
σ(β)−1/2

. This bound is strictly higher than the voting-rule independent
lower bound β
2
1+e−β
1−e−β for all β and is at least (1 −o(1)) β as β →∞.
Proof of Theorem 12. Without loss of generality, we may assume that m = 3. If m > 3, we can
repeatedly “split” some alternative x in two new alternatives y, y′ (where each user has the utility
25


Page 26:
for y, y′ as for the original alternative x, and µ(y) + µ(y′) is equal to the original mass of x in µ).
In this operation, the average utilities and Borda scores of y, y′ in the new instance are equal to the
average utility and Borda score of x in the original instance, and the average utilities and Borda
scores of all other alternatives do not change.
For any 0 < ϵ < 1, 0 ≤ϵ′ < 1 −ϵ, and 0 < γ < 1, consider the following distribution D of
utilities over alternatives (a, b, c):
(u(a), u(b), u(c)) =







(1 −γ, 1, 0)
with probability pA :=
σ(βϵ)−1/2
σ(β)+σ(βϵ)−1
(1, 0, ϵ)
with probability pB := pA · σ(βγ)−1/2
σ(β)−1/2
(0, 0, ϵ + ϵ′)
with probability 1 −pA −pB.
One verifies that 0 < pA, pB and pA + pB < 1, so this describes a valid probability distribution for
all ϵ, ϵ′, γ and each type of utilities has positive probability of being drawn. Assuming that ϵ′ = 0, it
must be true that p(b ≻c) = 1/2 = p(c ≻b) because
pA · σ(β(1 −0)) + (1 −pA) · σ(β(0 −ϵ)) = pA ·
 σ(β) −σ(−βϵ)
| {z }
=1−σ(βϵ)

+ σ(−βϵ)
| {z }
=1−σ(βϵ)
= pA ·
 σ(β) + σ(βϵ) −1

+ 1 −σ(βϵ)
= σ(βϵ) −1/2 + 1 −σ(βϵ) = 1/2.
If ϵ′ > 0, it must be the case that p(c ≻b) > 1/2 by monotonicity. A similar chain of algebra shows
that p(a ≻b) = 1/2 = p(b ≻a):
pA · σ(−βγ) + pB · σ(β) + 1−pA−pB
2
= pA ·
 σ(−βγ) −1/2

|
{z
}
=1/2−σ(βγ)
+ pB ·
 σ(β) −1/2

|
{z
}
=pA·(σ(βγ)−1/2)
+1/2 = 1/2.
For any ϵ, γ and positive ϵ′, note that, as the number of samples goes to infinity, the Borda score
of the alternatives concentrate around their expected values:
BC(a) →1
2µ(a) + 1
2µ(b) + p(a ≻c) µ(c)
BC(b) →1
2µ(a) + 1
2µ(b) + p(b ≻c) µ(c)
BC(c) →p(c ≻a) µ(a) + p(c ≻b) µ(b) + 1
2µ(c).
Recall that p(c ≻b) > 1/2 > p(b ≻c). Regardless of what p(a ≻c) = 1 −p(c ≻a) may be, for any
distribution µ with small enough µ(a), µ(c) (and hence large µ(b)), the expected Borda score of c
will be strictly larger than that of a and b. By concentration, for large enough n, the Borda voting
rule will almost surely select c as the winner, and the Borda’s distortion for that µ will be at least
maxx∈A AvgUtil(x)
AvgUtil(c)
≥AvgUtil(a)
AvgUtil(c) =
pA (1 −γ) + pB
pB ϵ + (1 −pA −pB) (ϵ + ϵ′).
(9)
We can now derive lower bounds on the distortion of Borda by defining sequences of parameters
ϵ, ϵ′, γ (and implicitly, a sequence of corresponding distributions µ), and considering the limit of
Eq. (9). In each such sequence, we treat γ as a fixed parameter, but let ϵ′ := ϵ2 and letting ϵ go
to 0. As ϵ →0, it holds that pA →0 (because its numerator σ(βϵ) −1/2 →1/2 −1/2 = 0), that
pB →0 (since it is a constant multiple of pA), and hence both the numerator and denominator of
26


Page 27:
Eq. (9) converge to 0. We apply l’Hˆopital’s rule to determine the limit. Treating pA and pB, as well
as the numerator num and denominator den of the equation as functions in ϵ, we observe that
p′
A(0) =
β
4 · (σ(β) −1/2)
p′
B(0) = β · (σ(βγ) −1/2)
4 · (σ(β) −1/2)2
num′(0) =
β
4 · (σ(β) −1/2) ·

1 −γ + σ(βγ) −1/2
σ(β) −1/2

den′(0) = pB(0)
| {z }
=0
·1 + p′
B(0) · 0 + (1 −pA(0) −pB(0))
|
{z
}
=1
·(1 + 2 · 0) + 0 · (−p′
A(0) −p′
B(0)) = 1.
Hence, the limit of Eq. (9) is
num′(0)
den′(0) =
β
4(σ(β) −1/2) ·

1 −γ + σ(βγ) −1/2
σ(β) −1/2

= β
2
1 + e−β
1 −e−β ·

1 −γ + σ(βγ) −1/2
σ(β) −1/2

, (10)
which means that each 0 < γ < 1 yields a distortion lower bound for Borda that is larger by a factor
of 1 −γ + σ(βγ)−1/2
σ(β)−1/2 than our algorithm-independent lower bound/the upper bound achieved by
NLHF. Since this factor is strictly concave in γ and is equal to 1 for γ →0 and γ →1, any value of
γ will lead to a strictly higher bound.
The value of γ that maximizes the bound in Eq. (10) is γ∗:= 2
β arctanh
q
1 −4 σ(β)−1/2
β

,
which we used to plot Appendix D.2. Since the resulting expression is algebraically unwieldy, we
consider the weaker bound for γ = log(β+1)
β
, which yields
β
2
1 + e−β
1 −e−β
|
{z
}
→1 as β→∞
·

1 −log(β + 1)
β
+
1
1+1/(β+1) −1/2
σ(β) −1/2

|
{z
}
→2 as β→∞
= (1 −o(1)) β.
D.3
Algorithm-Independent Lower Bounds
Theorem 3 (Voting Rule-Independent Distortion Lower Bound). Fix any β > 0. If each user
provides d=1 comparison, no voting rule can guarantee distortion better than β
2 · 1+e−β
1−e−β for large m.
If each user reports d ≥2 pairwise comparisons, any voting rule that puts at most 1/m probability
mass on a Condorcet loser must have at least the above distortion.
Proof of Theorem 3. To prove this distortion lower bound, we identify a family of social choice
problems for which the distortion of any such social choice function converges towards the claimed
bound. We will parameterize these instances by the parameters m ≥2, 0 < ϵ ≤1/2, and 1 ≤ξ < 2.
The instance has m alternatives labeled a, b1, . . . , bm−1. The distribution D is such that an agent
i ∼D has utilities
(ui(a), ui(b1), . . . , ui(bm−1)) =
(
(1, 0, . . . , 0)
with probability
σ(βϵ)−1/2
σ(β)+σ(βϵ)−1
(0, ξϵ, . . . , ξϵ)
with probability
σ(β)−1/2
σ(β)+σ(βϵ)−1.
Since the bj alternatives have the same utility for any agent, any agent asked to compare two of
them will prefer either one with probability 1/2. When ξ = 1, a randomly drawn rater will prefer
27


Page 28:
alternative a over some alternative bj with probability
σ(βϵ) −1/2
σ(β) + σ(βϵ) −1 · σ(β) +
σ(β) −1/2
σ(β) + σ(βϵ) −1 · σ(−βϵ)
= σ(βϵ)σ(β) −σ(β)/2 + σ(β)(1 −σ(βϵ)) −(1 −σ(βϵ))/2
σ(β) + σ(βϵ) −1
= σ(β)/2 + σ(βϵ)/2 −1/2
σ(β) + σ(βϵ) −1
= 1/2.
It is easy to see that the probability of a random agent preferring a over bj is monotone decreasing
in ξ. The social welfare of a is clearly
σ(βϵ)−1/2
σ(β)+σ(βϵ)−1 and the social welfare of any bj is ξϵ
σ(β)−1/2
σ(β)+σ(βϵ)−1.
Fix a voting rule f. If each agent only provides a single pairwise comparison, the voting rule
simply observes n independent Bernoulli samples with bias 1/2. For any number of samples n,
denote by px the probability that alternative x will win, where the randomness is taken over the
realization of these samples and the randomness in f. By the pigeon-hole principle, some alternative
x must be chosen with probability at most 1/m for infinitely many n. Without loss of generality,
we can assume that this alternative is a (otherwise, simply permute the roles of the alternatives,
which does not change the distribution over observed samples), and we restrict our focus to just the
n where pa ≤1/m. Now, the expected social welfare achieved by f is at most
1
mAvgUtil(a) + AvgUtil(b1) = 1/m · (σ(βϵ) −1/2) + ξϵ · (σ(β) −1/2)
σ(β) + σ(βϵ) −1
.
This shows that the distortion is at least
AvgUtil(a)
AvgUtil(f) ≥
σ(βϵ) −1/2
1/m · (σ(βϵ) −1/2) + ξϵ · (σ(β) −1/2) =

1
m + ξϵ(σ(β)−1/2)
σ(βϵ)−1/2
−1
.
(11)
For a sequence of social choice problems in which m →∞, ϵ →0, and ξ = 1, this term converges
towards

0 + (σ(β) −1/2) · lim ϵ→0
ϵ
σ(βϵ)−1/2
−1
=

(σ(β) −1/2) · 4
β
−1
= β
2
1 + e−β
1 −e−β ,
where the first equality follows from l’Hˆopital’s rule and the Taylor approximation σ(t) = 1/2+t/4+
O(t3), and the second inequality follows from the identity σ(t) −1/2 =
1
1+e−t −1/2 = 2−1−e−t
2 (1+e−t) =
1
2 · 1−e−t
1+e−t . This shows the claimed bound on the distortion of any voting rule.
If each agent may provide several pairwise comparisons, the above argument does not work for
all voting rules. The reason is that the correlations inside an agent’s comparisons might lead to
nonzero covariances that might allow an (arguably unnatural) voting rule to distinguish the special
alternative a. If the voting rule satisfies some natural social-choice properties, however, the lower
bound above goes through by just slightly changing ξ away from 1.
Suppose, first, that the voting rule satisfies the probabilistic Condorcet loser criterion, i.e., it will
never put more than 1/m probability mass on a Condorcet loser if one exists. If ξ > 1, a random
agent prefers a over bj with less than 1/2 probability. As a result, as the number of samples grows
large, the probability that a is a Condorcet loser with probability converging to 1. Hence, f cannot
put more than 1/m probability mass on a, and the distortion lower bound in Eq. (11) holds. If
ξ approaches 1 from above as m →∞and ϵ →0, the distortion bounds converge to the same
limit.
28


Page 29:
In the lower bound above, the probabilistic Condorcet loser criterion can easily be replaced by
other axioms. If, for example, the voting rule is guaranteed to put at least 1 −1/m probability mass
on a Condorcet winner (if one exists), the proof goes through if we increase only b2’s utility by a
factor ξ ↘1.
E
Supplemental Materials for Section 4
E.1
Upper Bound for NLHF
Theorem 7 (NLHF Distortion Upper Bound). For any instance D and any m, data distribution µ,
temperature β of the Bradley-Terry model, and any reference policy πref and KL budget τ, we have
dist(NLHF) ≤β
2 · 1+e−β
1−e−β . In the finite-sample regime, we have
AvgUtiln(NLHF) ≥
  2
β · 1−e−β
1+e−β

· maxπ⋆∈Bτ(πref) AvgUtil(π⋆) −O

1
β
q
log(mn)
n·min{1, d·µ2
min} + log(mn)
n·βµ2
min

.
Proof of Theorem 7. We prove this theorem by leveraging the convergence of empirical win-rates in
Lemma 10. We first condition on the following successful event, which, according to Lemma 10,
holds with probability at least 1 −δ over n samples of preference data,
∀x, y ∈A,
|pn(x ≻y) −p(x ≻y)| ≤O
 s
log(m/δ)
n · min{1, d · µ2
min} + log(m/δ)
nµ2
min
!
:= εn,d(δ).
As argued in the proof sketch, the NLHF policy by definition satisfies
πNLHF ∈argmax
π1∈Bτ(πref)
min
π2∈Bτ(πref) Ex1∼π1,x2∼π2[pn(x1 ≻x2) −pn(x2 ≻x1)],
where pn(x1 ≻x2) −pn(x2 ≻x1) describes a Nash-equilibrium strategy for a symmetric two-player
zero-sum game, and thus have value 0. Therefore, for π⋆∈Bτ(πref), it must hold that
0 ≤
E
x1∼πNLHF,x2∼π⋆[pn(x1 ≻x2) −pn(x2 ≻x1)] =
E
x1∼πNLHF,x2∼π⋆[2pn(x1 ≻x2) −1]
Since |pn(x ≻y) −p(x ≻y)| ≤εn,d(δ), we have
≤
E
x1∼πNLHF,x2∼π⋆[2p(x1 ≻x2) −1] + 2εn,d(δ)
According to the linearization lemma (Lemma 1), we have
≤
E
x1∼πNLHF,x2∼π⋆[2β(L · AvgUtil(x1) −ℓβ · AvgUtil(x2))] + 2εn,d(δ)
≤2β(L · AvgUtil(πNLHF) −ℓβ · AvgUtil(π⋆) + εn,d(δ)
β
).
Therefore, under the successful event, we can lower bound the average utility of the NLHF policy by
AvgUtil(πNLHF) ≥ℓβ
L AvgUtil(π⋆) −4εn,d(δ)
β
.
Taking the failure event into account, the expected average utility of the NLHF method is at least
AvgUtiln(NLHF) ≥(1 −δ)
ℓβ
L AvgUtil(π⋆) −4εn,d(δ)
β

≥ℓβ
L · AvgUtil(π⋆) −O
εn,d(δ)
β
+ δ · ℓβ
L

29


Page 30:
Finally, choosing δ = Θ

1
√n

, we have
≥ℓβ
L · AvgUtil(π⋆) −O
 
1
β
s
log(mn)
n · min{1, d · µ2
min} + log(mn)
n · βµ2
min
!
.
This completes the proof.
E.2
Lower Bound for PPO-based RLHF and DPO
Theorem 6 (RLHF Distortion Lower Bound). For m ≥3, there is a sequence of alignment problems
on which the distortion of RLHF scales as eΩ(β) in β.
Proof of Theorem 6. Suppose that the instance has m alternatives A = {a, b, c1, . . . , cm−2}, where
m−2 ≥4eβ. Let the data collection distribution be uniform over all candidates, i.e., µ = Uniform(A).
We consider the following distribution D over utility vectors, such that the utility vector of a random
agent i ∼D satisfies
(ui(a), ui(b), ui(c1), . . . , ui(cm−2)) =
(
(0, 1, 0, . . . , 0)
(type I) with probability δ,

1
β, 0, 1, . . . , 1

(type II) with probability 1 −δ,
where δ =
10
10+eβ = Θ(e−β). In other words, type I users have a strong preference for candidate b
but only constitute a δ fraction of the population, while type II users have a strong preference for c
and weak preference for a ≻b and make up for a 1 −δ fraction of the population.
For the reference policy and the KL budget, we set πref(a) = πref(b) = 1−ε
2
and πref(ci) =
ε
m−2
for all i ∈[m −2]. We leave the choice of ε to be determined later. The KL budget τ is set to be
τ = 1.
Analysis of the MLE reward.
Now we show that when n →∞, the MLE reward satisfies
r(b) −r(a) > 0. According to [Siththaranjan et al., 2023, Procaccia et al., 2025], it suffices to show
that limn→∞BCn(b) −BCn(a) > 0, which, by Lemma 11, is implied by BC⋆(b) −BC⋆(a) > 0.
We have
BC⋆(b) −BC⋆(a) = 1
m
m−2
X
i=1
(p(b ≻ci) −p(a ≻ci)) + 1
m (p(b ≻a) −p(a ≻b))
For each ci, we have
p(b ≻ci) −p(a ≻ci) = δ · (σ(β) −σ(0)) + (1 −δ) · (σ(−β) −σ(1 −β)) .
In the above equation, the first term accounts for type-I users and is lower bounded by δ
3 when
β ≥2. The second term accounts for type-II users, and we leverage the fact that σ(x) is concave
when x ≥0 to bound it as
(1 −δ) · (σ(−β) −σ(1 −β)) = −eβ
10δ · (σ(β) −σ(β −1)) ≥−eβ
10δ · σ′(β −1) ≥−e
10δ,
where the last step uses σ′(x) = σ(x) · (1 −σ(x)) ≤1 −σ(x) ≤e−x for all x. Plugging both bounds
into the limit BC⋆(b) −BC⋆(a) and substituting δ =
10
10+eβ ≥
20
m−2 gives
lim
n→∞BC(b) −BC(a) = BC⋆(b) −BC⋆(a) ≥m −2
m
· δ ·
1
3 −e
10

−1
m ≥1
m.
30


Page 31:
Therefore, when n is sufficiently large, we have BC(b) > BC(a) with high probability, which implies
that b is has higher MLE reward than a.
As for the MLE reward of type-c candidates, since BC⋆(ci) = BC⋆(cj) for all i, j ∈[m −2], we
have maxi,j∈[m−2] |r(ci) −r(cj)| →0 when n →∞. In the limit, we can treat all type-c candidates
as having the same reward.
Analysis of the KL-constrained policies.
Since all type-c candidates have the same estimated
reward and the same probability under the reference policy, both π⋆and ˆπRLHF will assign the same
probability to all type-c candidates. This can be seen by the equivalence between regularized and
constrained RLHF as shown in Appendix E.4. As a result, we can view all type-c candidates as a
single candidate c which have mass ε under the reference policy.
We now show that for any η > 0, there exists an ε > 0 such that any policy π ∈∆({a, b, c})
inside the KL ball Bτ(πref) cannot put more than η mass on c. We have
1 ≥DKL(π ∥πref) = π(a) · log
π(a)
(1 −ε)/2 + π(b) · log
π(b)
(1 −ε)/2 + π(c) · log π(c)
ε
Fixing π(c), the KL divergence is minimized when π(a) = π(b) = 1−π(c)
2
. Substituting this into the
KL divergence, we get
≥(1 −π(c)) · log 1 −π(c)
1 −ε
+ π(c) · log π(c)
ε
Since t log t ≥−1/e for all t > 0, and log
1
1−ε > 0, we have
≥−2
e + π(c) log 1
ε.
Therefore, any policy in the KL ball must satisfy π(c) log 1
ε ≤1 + 2/e ≤2, which implies that
π(c) ≤
2
log(1/ε). We can choose ε to be any constant smaller than e−2/η to ensure that π(c) ≤η.
We then show that when η is sufficiently small, πRLHF puts almost all probability mass on b,
whereas π⋆puts almost all probability mass on a. This will ultimately lead to a distortion of
AvgUtil(π⋆)
AvgUtil(ˆπRLHF) = Θ(AvgUtil(a))
Θ(AvgUtil(b)) = Θ(1/β)
Θ(e−β) = eΩ(β).
• For πRLHF, we assume that the estimated reward is shifted such that r(c) = 0 (as a result,
r(a) < r(b) < 0). Since π′ = (0, 1, 0) also satisfies the KL constraint, we have r(πRLHF) ≥r(π′).
Together with the fact that πRLHF(c) ≤η, we have
r(π′) = r(b) ≤r(πRLHF) = r(a)πRLHF(a) + r(b)πRLHF(b)
≤πRLHF(a) · r(a) + (1 −πRLHF(a) −η) · r(b).
Therefore, we have πRLHF(a) ≤η·
|r(b)|
|r(b)−r(a)|. Setting ε to be sufficiently small, we can guarantee
that
η ≤η1 :=
e−β
1 +
|r(b)|
|r(b)−r(a)|
,
(12)
and thus πRLHF(a)+πRLHF(c) ≤η

1 +
|r(b)|
|r(b)−r(a)|

≤e−β. As a result, we have AvgUtil(πRLHF) =
Θ(AvgUtil(b)).
31


Page 32:
• For π⋆, a similar argument shows that when
η ≤η2 :=
e−β
1 +
AvgUtil(a)
AvgUtil(a)−AvgUtil(b)
,
(13)
We have π⋆(b) + π⋆(c) ≤e−β. As a result, we have AvgUtil(π⋆) = Θ(AvgUtil(a)).
Finally, we set ε to be smaller than e−2/ min{η1,η2} such that Equations (12) and (13) are both
satisfied. This ensures AvgUtil(π⋆)/AvgUtil(πRLHF) = eΩ(β) and completes the proof.
E.3
Equivalence of DPO and RLHF under Heterogeneous Preferences
In this section, we formalize the observation that DPO and RLHF are equivalent under heterogeneous
preferences. This is consistent with the result by Shirali et al. [2025], which shows that DPO also
aligns with the Borda count. We start by recalling the DPO objective [Rafailov et al., 2023].13
LDPO(π; πref) = −
X
1≤i≤n,1≤j≤d
log σ
 
β log π(xj
i)
πref(xj
i)
−β log π(yj
i )
πref(yj
i )
!
.
Now we perform a change of variables to transform π into the following form:
π(x) = πref(x) · exp(ˆr(x)/β)
where
ˆr(x) := β log π(x)
πref(x), ∀x ∈A.
Substituting this into the DPO objective, we get:
LDPO(π; πref) = −
X
1≤i≤n,1≤j≤d
log
 σ(ˆr(xj
i) −ˆr(yj
i ))

,
which is exactly the MLE objective for reward learning in RLHF, repeated here for convenience:
LMLE(r) := −
X
1≤i≤n,1≤j≤d
log
 σ(r(xj
i) −r(yj
i ))

.
Therefore, there is a one-to-one correspondence between the MLE reward r⋆= argminr∈Rm LMLE(r)14,
and the DPO policy πDPO = argminπ LDPO(π; πref) as:
πDPO(x) = πref(x) · exp(r⋆(x)/β).
On the other hand, the RLHF policy with regularization parameter λ (see Appendix E.4 for the
equivalence between regularized and constrained versions of RLHF) is also given by
πRLHF(x) = πref(x) · exp(r⋆(x)/λ).
Therefore, the DPO policy πDPO and the RLHF policy πRLHF are equivalent when the parameter β
in the DPO objective is equal to λ in the RLHF objective. Notably, both policies are different from
the optimal policy π⋆∝πref · exp(AvgUtil(x)/λ′) (for a potentially different λ′ that make the KL
constraint tight) as r⋆̸= AvgUtil, which has also been pointed out by Shirali et al. [2025].
13Note that the parameter β does not need to be the same as the true temperature of the Bradley-Terry model in
our setting.
14Note that we have a minus sign in the MLE objective, which is equivalent to maximizing the sum of log-likelihoods.
32


Page 33:
E.4
Equivalence of Regularized and Constrained Alignment Methods
In this section, we formally establish the equivalence between regularized and constrained formula-
tions of both RLHF and NLHF. Although this equivalence is standard and likely known to many,
we include the details here for completeness. We begin by proving the equivalence between the two
versions of NLHF (which involves max-min optimization over the policy space); the corresponding
result for RLHF then follows by analogous arguments.
Proposition 13 (Equivalence between Constrained and Regularized NLHF.). Let πτ be the output
of the τ-constrained NLHF method defined in Section 2, i.e.,
πτ = argmax
π1∈Bτ(πref)
min
π2∈Bτ(πref)
E
x1∼π1,x2∼π2 [Mx1,x2] ,
(14)
and let ˜πλ be the output of the λ-regularized NLHF method [Munos et al., 2024], i.e.,
˜πλ = argmax
π1∈∆(M)
min
π2∈∆(M)
E
x1∼π1,x2∼π2 [Mx1,x2] −λ · DKL(π1 ∥πref) + λ · DKL(π2 ∥πref).
(15)
Then, for each λ ∈[0, ∞] with solution ˜πλ for Eq. (15), we have that ˜πλ is also an optimal solution
to the τ-constrained optimization problem in Eq. (14), where τ = DKL(˜πλ ∥πref). Conversely, for
each τ ≥0 with solution πτ for Eq. (14), there exists λ ∈[0, ∞] such that πτ is also an optimal
solution to the λ-regularized optimization problem in Eq. (15).
Proof of Proposition 13. We start by observing that in both games Eq. (14) and Eq. (15), the
utilities are anti-symmetric functions, and the strategy spaces for both players are identical, convex
and compact. Therefore, the value of the both games is 0, and both games have symmetric Nash
equilibria.
Now, we prove the two directions of the claim separately.
Regularized ⇒Constrained.
Given λ ∈[0, ∞] and ˜πλ be the solution to Eq. (15). Consider
the constrained optimization problem in Eq. (14) with τ = DKL(˜πλ ∥πref). We show that π2 = ˜πλ is
a best response to π1 = ˜πλ in the constrained game with radius τ = DKL(˜πλ ∥πref), i.e.,
˜πλ =
argmin
π2∈Bτ(πref)
E
x1∼˜πλ,x2∼π2 [Mx1,x2]
(16)
If Eq. (16) holds, then by the fact that the utility is anti-symmetric, we have that π1 = ˜πλ is
also a best response to π2 = ˜πλ in the same constrained game. Putting both together, we have
that (˜πλ, ˜πλ) is a Nash equilibrium for the constrained game with radius τ = DKL(˜πλ ∥πref), thus
establishing the first direction.
Now we prove Equation (16). To see this, note that ∀π2 ∈Bτ(πref), we have that DKL(π2 ∥πref) ≤
τ = DKL(˜πλ ∥πref). Therefore, from the fact that ˜πλ is a Nash equilibrium for the regularized game
Eq. (15), we have that for any π2 ∈∆(M) and specifically π2 ∈Bτ(πref), we have that
E
x1∼˜πλ,x2∼π2 [Mx1,x2] + λ · DKL(π2 ∥πref) ≥
E
x1∼˜πλ,x2∼˜πλ [Mx1,x2] + λ · DKL(˜πλ ∥πref)
⇒
E
x1∼˜πλ,x2∼π2 [Mx1,x2] −
E
x1∼˜πλ,x2∼˜πλ [Mx1,x2] ≥λ · (DKL(˜πλ ∥πref) −DKL(π2 ∥πref)) ≥0.
This proves Eq. (16) and completes the proof of the first direction.
33


Page 34:
Constrained ⇒Regularized.
We prove the reverse direction using duality theory.
We first show how to construct the regularization parameter λ. For simplicity, we write πT
1 Mπ2
as a shorthand for Ex1∼π1,x2∼π2 [Mx1,x2]. Then minimizing player in the constrained game Eq. (14)
with π1 = πτ can be written as
min
π2∈Rm πT
τ Mπ2
s.t.
DKL(π2∥πref) ≤τ, π2 ≥0, 1Tπ2 = 1.
(Constrained Minimization)
The Lagrangian of this problem is
L(π2, λ, ⃗µ, η) = πT
τ Mπ2 + λ (DKL(π2∥πref) −τ) −⃗µTπ2 + η1Tπ2,
where λ, ⃗µ, η ≥0 are the Lagrange multipliers for the KL divergence constraint, the non-negativity
constraint, and the normalization constraint, respectively. Since the utility πT
1 Mπ2 is convex, the
normalization constraint is affine, and the inequality constraints are convex, and the reference
policy πref is strictly feasible with DKL(πref∥πref) = 0 < τ,15 the Slater’s condition is satisfied, which
guarantees that the KKT conditions are necessary and sufficient for optimality — there exists
parameters λ⋆, ⃗µ⋆, η⋆≥0 such that as an optimal solution to Eq. (Constrained Minimization),
π2 = πλ satisfies the following KKT conditions:
∇π2L(π2, λ⋆, ⃗µ⋆, η⋆) = MTπτ + λ⋆· ∇π2DKL(π2∥πref) −⃗µ⋆+ η⋆· 1 = 0,
(17)
where
η⋆(1Tπ2 −1) = 0
and
µ⋆
i (π2)i = 0, ∀i ∈[m],
(18)
due to complementary slackness.
We will show that this λ⋆is the regularization parameter we are looking for. Namely, for the
regularized game in Eq. (15) with λ = λ⋆, we have that (πτ, πτ) is a Nash equilibrium.
Again, let us first fix π1 = πτ and consider the regularized optimization problem for the
minimizing player:
min
π2 πT
τ Mπ2 −λ⋆· DKL(π2∥πref)
s.t.
π2 ≥0, 1Tπ2 = 1.
(Regularized Minimization)
Since πT
τ Mπ2 is convex in π2, Slater’s condition is satisfied for the above problem and implies that
the KKT conditions are sufficient for optimality. It is also not hard to see that L(π2, λ⋆, ⃗µ⋆, η⋆)
coincides with the Lagrangian of (Regularized Minimization). We can therefore conclude from
Eqs. (17) and (18) that for the minimizing player in the regularized game, π2 = πτ is a best response
strategy to π1 = πτ.
Since the regularized game is anti-symmetric, the same argument shows that for the maximizing
player in the regularized game, π1 = πτ is also a best response strategy to π2 = πτ. Together, we
have that (πτ, πτ) is a Nash equilibrium for the regularized game in Eq. (15) with λ = λ⋆. The
proof is complete.
Combining Proposition 13 with Theorem 7, we obtain the following guarantee for the KL-
regularized version of NLHF:
15If τ = 0, the only feasible policy is πref, and the claim clearly holds for λ = ∞. We also assume that πref(a) > 0
for all a ∈M. Otherwise if πref(a) = 0 for some a ∈M, then both the regularized and constrained versions forbid any
policy to put nonzero probability on a, which leads to an effectively smaller candidate set.
34


Page 35:
Corollary 8. If λ-regularized NLHF (for any λ ≥0) returns a policy ˜πNLHF, this policy’s average
utility is at least a 2
β · 1−e−β
1+e−β fraction of the optimal average utility of any policy π with DKL(π ∥πref) ≤
DKL(˜πNLHF ∥πref) (minus finite-sample errors, see Theorem 7).
For the RLHF case, the proof is analogous, except that we no longer have nested minimization-
maximization, so the proof is slightly simpler. We omit the details of proof, but state the result
below.
Proposition 14 (Equivalence between Constrained and Regularized RLHF). Let r be the MLE
reward learned from the comparison data, and let πτ be the output of the τ-constrained RLHF method
defined in Section 2, i.e.,
πτ = argmax
π∈Bτ(πref)
E
x∼π [r(x)] ,
(19)
and let ˜πλ be the output of the λ-regularized RLHF method, i.e.,
˜πλ = argmax
π∈∆(M)
E
x∼π [r(x)] −λ · DKL(π ∥πref).
(20)
Then, for each λ ∈[0, ∞] with solution ˜πλ for Eq. (20), we have that ˜πλ is also an optimal solution
to the τ-constrained optimization problem in Eq. (19), where τ = DKL(˜πλ ∥πref). Conversely, for
each τ ≥0 with solution πτ for Eq. (19), there exists λ ∈[0, ∞] such that πτ is also an optimal
solution to the λ-regularized optimization problem in Eq. (20).
F
Other Sampling Models
To prove Theorem 9, we first prove the following lemma. We illustrate the constructed sequence of
alternatives in Fig. 4.
u1
u2
u3
0.33
0.00
0.21
0.51
0.00
0.22
0.42
0.00
0.18
0.34
0.00
0.15
0.30
0.00
0.33
0.49
0.00
0.29
0.51
0.00
0.20
0.39
0.00
0.17
0.33
0.00
0.15
0.29
0.33
0.49
0.70
0.00
0.22
0.44
0.00
0.19
0.36
0.00
0.16
0.31
0.00
0.14
a1
a2
a3
a4
a5
a6
a7
a8
a9
a10
a11
a12
a13
a14
0.51
0.52
0.55
0.53
0.53
0.52
0.52
0.51
0.51
0.51
0.51
0.51
0.51
0.0
0.2
0.4
SW(at)
0.33
0.33
0.31
0.27
0.24
0.22
0.21
0.19
0.18
0.17
0.16
0.15
0.15
0.14
Figure 4: Utilities for first 14 alternatives in the sequences constructed in Lemma 15, for β = 5.
Bottom bar chart shows decreasing utility. Numbers between alternative labels at+1 →at give the
expected win-rate p(at+1 ≻at).
35


Page 36:
Lemma 15. For any β > 0, there is an infinite sequence a1, a2, . . . of alternatives, and a distribution
D of utility functions over these alternatives such that
• AvgUtil(a1) = 1/3,
• for all t ≥2, 0 < AvgUtil(at) ≤AvgUtil(at−1) −
2
3 β log

1 + tanh
 β/4 · AvgUtil(at−1)
3
<
AvgUtil(at−1), and
• for all t ≥2, p(at ≻at−1) > 1/2.
Proof. Our population D will be a uniform distribution over three utility vectors, u1, u2, and u3.
We define the sequence of alternatives and prove the claim by induction over t ≥1.
For t = 1, set u1(a1) = u2(a1) = u3(a1) := 1/3, which clearly satisfies the first claim.
Now, let t ≥2, and suppose that we have defined the utilities for alternatives a1, . . . , at−1 and
established the claims for all t′ < t. We define utilities for at and extend the claims to t. Let uA
denote the utility vector among u1, u2, u3 with the highest utility for at−1, and denote the other
two utility vectors by uB, uC. For convenience, set ∆:= uA(at−1) · β and ∆′ := log
  (e∆/2+1)3
2 (e∆+3)

.
uA(at) := uA(at−1) −∆/β = 0,
uB(at) := uB(at−1) + ∆′/β,
uC(at) := uC(at−1) + ∆′/β.
It will be useful to derive an alternative expression for ∆′:
∆′ = log
 
(e∆/2 + 1)3
2 (e∆+ 3)
!
= log
 
e∆/2
(e∆/2 + 1)3
2 e∆/2 (e∆+ 3)
!
= ∆
2 −log 2 e∆/2 (e∆+ 3)
(e∆/2 + 1)3
= ∆
2 −log (e∆/2 + 1)3 + (e∆/2 −1)3
(e∆/2 + 1)3
= ∆
2 −log
 
1 +
e∆/2 −1
e∆/2 + 1
3
!
= ∆
2 −log
 1 + tanh(∆/4)3
.
Since the value 1 + (e∆/2−1
e∆/2+1)3 in the logarithm is greater than 1, we know that ∆′ < ∆/2.
Since AvgUtil(at−1) > 0 by the induction hypothesis, it must hold that ∆> 0, and, by expanding,
that
∆′ = log (e∆/2 + 1)3
2 (e∆+ 3) = log 3 e∆+ 1 + 1
2 · (e∆/2 −1)3
e∆+ 3
> log 3 e∆+ 1
e∆+ 3 .
(21)
Since log 3 e∆+1
e∆+3 > log e∆+3
e∆+3 = 0, it holds that ∆′ > 0 and that AvgUtil(at) > 0.
We first must show that we have not set uB(at) and uC(at) greater than 1. Since, by the
induction hypothesis, 1
3(uA(at−1) + uB(at−1) + uC(at−1)) = AvgUtil(at−1) ≤AvgUtil(at−2) ≤· · · ≤
AvgUtil(a1) = 1/3, it must hold that uA(at−1) + uB(at−1) + uC(at−1) ≤1, which by the choice
of uA implies that uB(at−1), uC(at−1) are at most 1/2. Since ∆′ < ∆/2 = uA(at−1) · β/2 ≤β/2,
uB(at) = uB(at−1) + ∆′/β ≤1/2 + 1/2 = 1, this holds for uB, and analogously for uC.
Next, we show the claimed reduction in average utility using our alternative expression for ∆′.
AvgUtil(at) = 1
3 ·
 uA(at) + uB(at) + uC(at)

= 1
3 ·

uA(at−1) + uB(at−1) + uC(at−1) −∆−2 ∆′
β

= AvgUtil(at−1) −∆−2 ∆′
3 β
= AvgUtil(at−1) −2
3 β log

1 + tanh(∆/4)3
.
36


Page 37:
By our choice of uA and averaging, it holds that uA(at−1) ≥AvgUtil(at−1) and hence that ∆≥
β · AvgUtil(at−1). Since the bound on AvgUtil(at) above is monotone nonincreasing in ∆, we obtain
our claim that
AvgUtil(at) ≤AvgUtil(at−1) −2
3 β log

1 + tanh
 β/4 · AvgUtil(at−1)
3
.
Finally, it remains to show that p(at ≻at−1) > 1/2. Since
p(at ≻at−1) = σ(−∆) + 2 σ(∆′)
3
= 1
2 + (σ(−∆) −1/2) + 2 (σ(∆′) −1/2)
3
= 1
2 + (1/2 −σ(∆)) + 2 (σ(∆′) −1/2)
3
,
it suffices to show that 2 (σ(∆′) −1/2) > σ(∆) −1/2. Observing that σ(x) −1/2 = 1
2 · 1−e−x
1+e−x and
applying Eq. (21), we bound
2
 σ(∆′) −1
2

> 2

σ
 log(3∆+1
e∆+3)

−1
2

=
1 −
e∆+3
3 e∆+1
1 +
e∆+3
3 e∆+1
=
2 e∆−2
3 e∆+1
4 e∆+4
3 e∆+1
= 2
4 · e∆−1
e∆+ 1
= 1
2 · 1 −e−∆
1 + e−∆= σ(∆) −1
2,
which establishes our claim.
Theorem 9 (Unbounded Distortion of RLHF Under Correlated Sampling). For any β > 0, there
exists a sequence of alignment instances and distributions ν ∈∆
  A
2

over comparison pairs such
that RLHF’s distortion is unbounded.
Proof. We construct our sequence of instances by taking increasingly long prefixes of the sequence
in Lemma 15, i.e., by considering the alternatives a1, . . . , am for increasing m. Rescaling by some
constants, we can define the MLE rewards in RLHF as
r = argmax
r∈Rm
X
{x,y}∈(A
2)
#(x ≻y)
n d
log
 σ(r(x) −r(y))

+ #(y ≻x)
n d
log
 σ(r(y) −r(x))

.
Following Siththaranjan et al. [2023], we apply the first-order optimality conditions to obtain that,
for each alternative x,
X
y̸=x
#(x ≻y)
n d
=
X
y̸=x
#(x ≻y) + #(y ≻x)
n d
· σ(r(x) −r(y)).
By the strong law of large numbers, as the number n of samples goes to infinity (regardless of d),
the sample fraction #(x≻y)
n d
converges almost surely to its expected value ν({x, y}) · p(x ≻y). Hence,
as n →∞, the rewards (a random variable depending on the random pairwise comparisons) will
satisfy that
X
y̸=x
ν({x, y}) · σ(r(x) −r(y)) a.s.
−→
X
y̸=x
ν({x, y}) · p(x ≻y).
(22)
Consider a distribution ν over pairs of alternatives that assigns each pair of adjacent alternatives
{at, at+1} a probability of
1−ϵ
m−1 of being drawn for comparison, and all other pairs a probability
37


Page 38:
of
ϵ
(m
2)−(m−1), where ϵ > 0 is a small value, dependent on the current m, to be determined in the
following.
Applying Eq. (22) to x = am, we obtain that
1−ϵ
m−1σ(r(am) −r(am−1)) + O(ϵ) converges almost
surely to
1−ϵ
m−1 · p(am ≻am−1) + O(ϵ). Since Lemma 15 guarantees that p(am ≻am−1) > 1/2, for
small enough ϵ, it will hold almost surely that σ(r(am)−r(am−1)) > 1/2, i.e., that r(am) > r(am−1).
Next, we apply Eq. (22) to x = am−1, to obtain that
1−ϵ
m−1(σ(r(am−1) −r(am)) + σ(r(am−1) −
r(am−2)))+O(ϵ) converges almost surely to 1−ϵ
m−1 ·(p(am−1 ≻am)+p(am−1 ≻am−2))+O(ϵ). Having
established above that, for small enough ϵ, we can make σ(r(am−1)−r(am)) = 1−σ(r(am)−r(am−1))
arbitrarily close to p(am−1 ≻am) = 1 −p(am ≻am−1), we see that σ(r(am−1) −r(am−2)) must
become arbitrarily close to p(am−1 ≻am−2) > 1/2.
Continuing this argument for x = am−2, am−3, . . . , a1, we obtain that, for small enough ϵ, the
rewards will be ordered as r(a1) < r(a2) < · · · < r(am) almost surely. Set ϵ (for this specific m) so
that this is the case. We set the KL constraint large enough that all policies are possible; say, by
choosing the reference policy to be uniform and setting τ = log m.16 Then, the reward-maximizing
policy clearly puts all probability mass on the alternative am with maximal reward, obtaining a
distortion of AvgUtil(a1)
AvgUtil(am) =
1/3
AvgUtil(am).
We have now defined a sequence of instances, whose distortion grows as
1/3
AvgUtil(am) as m →∞.
To show that distortion is not bounded in β, it remains to show that AvgUtil(am) →0. The lemma
already tells us that AvgUtil(at) (for t = 1, 2, . . . ) is a monotonically decreasing sequence. Since
the average utility is nonnegative, the sequence is bounded from below and thus convergent, which
also implies that the sequence of differences AvgUtil(at−1) −AvgUtil(at) must converge to 0. Since
the bound
2
3β log(1 + tanh(β/4AvgUtil(at−1))3) is sandwiched between these differences and 0, it
must also converge to 0. Since it is continuous in AvgUtil(at−1) and positive for all positive values of
AvgUtil(at−1), this implies that AvgUtil(at−1) must converge to 0. This shows that AvgUtil(am) →0
for large m, and that the distortion grows unboundedly large as m increases, which concludes our
proof.
16This means that this lower bound fits into the social choice subsetting. Note that the theorem does not apply to
Borda count (which is not defined for a general distribution ν), but to RLHF considered as a voting rule.
38

