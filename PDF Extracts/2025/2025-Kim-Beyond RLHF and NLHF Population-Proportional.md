---
source_pdf: "[[Lit-WS-PDFs/2025/2025-Kim-Beyond RLHF and NLHF Population-Proportional.pdf]]"
extracted_date: "2026-07-09"
pages: 27
extractor: "PyMuPDF"
---

Page 1:
Published as a conference paper at ICLR 2026
BEYOND RLHF AND NLHF:
POPULATION-PROPORTIONAL ALIGNMENT UNDER
AN AXIOMATIC FRAMEWORK
Kihyun Kim1∗
Jiawei Zhang1,2∗†
Asuman Ozdaglar1
Pablo A. Parrilo1
1 MIT LIDS
2 University of Wisconsin-Madison
{kihyun, jwzhang, asuman, parrilo}@mit.edu
ABSTRACT
Conventional preference learning methods often prioritize opinions held more
widely when aggregating preferences from multiple evaluators. This may result in
policies that are biased in favor of some types of opinions or groups and susceptible
to strategic manipulation. To address this issue, we develop a novel preference
learning framework capable of aligning aggregate opinions and policies propor-
tionally with the true population distribution of evaluator preferences. Grounded in
social choice theory, our approach infers the feasible set of evaluator population
distributions directly from pairwise comparison data. Using these estimates, the
algorithm constructs a policy that satisfies foundational axioms from social choice
theory, namely monotonicity and Pareto efficiency, as well as our newly-introduced
axioms of population-proportional alignment and population-bounded manipula-
bility. Moreover, we propose a soft-max relaxation method that smoothly trades
off population-proportional alignment with the selection of the Condorcet winner
(which beats all other options in pairwise comparisons). Finally, we validate the
effectiveness and scalability of our approach through experiments on both tabular
recommendation tasks and large language model alignment.
1
INTRODUCTION
Aligning artificial intelligence (AI) systems with complex human preferences is a growing priority in
fields such as robotics (Kupcsik et al., 2017; Bıyık et al., 2024), recommendation systems (Xue et al.,
2023), and large language models (LLMs) (Ziegler et al., 2019; Stiennon et al., 2020; Ouyang et al.,
2022). A key challenge in this endeavor is how to infer and represent such preferences accurately,
particularly when they are only available through incomplete signals like pairwise comparisons.
This has prompted reinforcement learning from human feedback (RLHF), which has become a
widely used framework for preference learning (Ouyang et al., 2022; Christiano et al., 2017). RLHF
streamlines the alignment process by first learning a reward model that assigns scalar scores to
different alternatives, typically trained using maximum likelihood estimation under the Bradley–Terry
(BT) model. In the second stage, a policy is optimized through reinforcement learning to maximize
the expected rewards, guiding the system toward behaviors aligned with human preferences.
Despite its practical success and simplicity, the standard RLHF framework rests on a critical assump-
tion that complex human preferences can be captured by a single scalar reward. Recent research
highlights that this assumption often breaks down, especially when human feedback reflects incon-
sistent or conflicting judgments across evaluators (Chakraborty et al., 2024). In particular, RLHF
struggles in scenarios involving intransitive or cyclic preferences, where no clear ranking among
alternatives can be established, leading to failures in accurately modeling the underlying prefer-
ences (Munos et al., 2024; Swamy et al., 2024). To address these limitations, a game-theoretic
framework called Nash learning from human feedback (NLHF) has been introduced (Munos et al.,
2024; Swamy et al., 2024; Ye et al., 2024; Maura-Rivero et al., 2025). NLHF reframes preference
∗Equal contribution.
†Corresponding author.
1
arXiv:2506.05619v3  [cs.AI]  2 Mar 2026


Page 2:
Published as a conference paper at ICLR 2026
learning as a two-player constant-sum game and identifies equilibrium policies that no competing
policy can outperform, regardless of the complexity of the underlying preferences.
Nevertheless, both RLHF and NLHF frameworks remain limited in their ability to address another
critical issue: the proportional alignment of evaluator preferences. When preferences are aggregated
across multiple evaluator groups with distinct viewpoints, both RLHF and NLHF tend to yield
policies that do not adequately reflect the full distribution of the evaluator population (Chakraborty
et al., 2024). To address these challenges, recent research has turned to social choice theory-oriented
approaches, such as maximizing the minimum satisfaction across evaluator groups (Chakraborty
et al., 2024; Ramesh et al., 2024) and optimizing social welfare functions (Zhong et al., 2024; Kim
et al., 2025). Another line of emerging research, pluralistic alignment (Sorensen et al., 2024), seeks
to reflect diverse perspectives in AI systems through approaches such as mixture-based models (Chen
et al., 2024), belief-conditioned models (Yao et al., 2025), and steerable models (Adams et al., 2025),
with a particular focus on LLMs. However, these methods generally assume explicit knowledge or
clear labels of evaluator groups, which limits their practical applicability since group identities are
often implicit or unobservable in the real world. Motivated by this limitation, our research aims to
achieve proportional alignment without requiring additional information about the evaluator profile.
Our approach builds upon recent works addressing diverse preference aggregation through an ax-
iomatic approach from social choice theory (Mishra, 2023; Siththaranjan et al., 2024; Dai & Fleisig,
2024; Conitzer et al., 2024; Ge et al., 2024; Maura-Rivero et al., 2025; Shi et al., 2025; Xiao et al.,
2025). Specifically, we propose a novel preference learning algorithm that satisfies two foundational
axioms, monotonicity (ensuring that improving an alternative’s ranking cannot decrease its proba-
bility) and Pareto efficiency (ensuring that if an alternative is preferred by all, it is favored by the
policy), as well as two new axioms we introduce: population-proportional alignment (PPA) and
population-bounded manipulability (PBM). The first new axiom, PPA, requires the policy to be at
least weakly proportional to evaluator population shares, addressing the insufficient representation of
the population distribution under RLHF and NLHF. The second axiom, PBM, bounds the incentive
for manipulation as an affine function of the true population share, thereby guaranteeing robustness.
Recent studies have highlighted that conventional preference learning methods are susceptible to
strategic misreporting (Buening et al., 2025). Unlike existing approaches that incorporate explicit
mechanism design to ensure strict strategyproofness (Park et al., 2024; Soumalias et al., 2024; Sun
et al., 2024; Hao & Duan, 2025; Buening et al., 2025), our method inherently limits manipulative
advantage by constraining policy selection based on estimated feasible population distributions.
Further details on related work are provided in Appendix B.
1.1
OUR CONTRIBUTION
The first key contribution of this work is demonstrating that the set of feasible population distributions
of evaluators can be inferred directly from pairwise comparison data. Leveraging this insight, we
develop a novel preference learning framework designed to align policies proportionally with the
underlying population distribution. To establish a rigorous theoretical basis, we adopt an axiomatic
approach, proving that our framework satisfies two fundamental axioms, monotonicity and Pareto
efficiency, and two newly introduced axioms, PPA and PBM. In addition, we propose a novel softmax
relaxation method to control the trade-off between proportional alignment and the selection of
the Condorcet winner. For practical deployment, we present a scalable algorithm with function
approximation, allowing our framework to scale to high-dimensional settings such as LLMs. Finally,
the proposed framework is validated through empirical evaluations in both tabular and function
approximation settings.
Organization of the paper.
In Section 2, we formalize the setting of preference learning and
probabilistic social choice, and establish connections between them. In Section 3, motivated by a
simple negative example, we introduce two desirable axioms alongside two fundamental axioms.
In Section 4, we propose a novel preference learning algorithm that satisfies these axioms and
provide a theoretical analysis. Finally, Section 5 presents empirical evaluations that demonstrate the
effectiveness and scalability of our method. For ease of reference, all mathematical notation used in
the paper is summarized in Appendix A.
2


Page 3:
Published as a conference paper at ICLR 2026
PSCF
Profile
Preference Learning
Preference Function
Policy
Figure 1: Illustration of the relationships between the profile, preference function, and policy.
2
PRELIMINARIES
2.1
PROBABILISTIC SOCIAL CHOICE FUNCTION AND PREFERENCE LEARNING
We begin by reviewing key concepts from social choice theory and preference learning to establish
a foundation for our subsequent analysis. Consider a set of M alternatives, denoted by Y :=
{y1, y2, . . . , yM}, where each y ∈Y may represent a response generated by a language model or
an action in a decision-making task. We assume each evaluator has a strict and complete ranking
over the alternatives, and let S denote the set of all possible rankings (i.e., permutations of Y). Each
ranking is represented by r ∈S, where r(yi) = k indicates that alternative yi is ranked k-th under r.
A profile σ ∈∆(S) is a probability distribution over the set of all rankings, where σr represents the
proportion of the population that adheres to ranking r.
A probabilistic social choice function (PSCF) is a mapping Φ : ∆(S) →∆(Y) that assigns to each
profile σ a policy π, which is a probability distribution over the alternatives in Y. In practice, however,
acquiring a complete profile σ is often infeasible due to the high cost of collecting full rankings over
a large set of alternatives.
To address this limitation, pairwise preference learning algorithms have been developed, allowing
alignment based solely on pairwise comparison data. We define a preference function P : Y2 →[0, 1],
where P(y ≻y′) denotes the probability that alternative y is preferred over y′. Given a profile σ, let
Pσ be the preference function induced by the population distribution σ over rankings, defined as
Pσ(y ≻y′) :=
X
r∈S
σr · 1{r(y)<r(y′)},
(1)
where 1r(y)<r(y′) is an indicator function equal to 1 if ranking r places alternative y in a better (i.e.,
lower) position than y′, and 0 otherwise. This function captures the expected pairwise preference
between y and y′ under the distribution σ.
We define P as the set of all preference functions induced by some profile σ ∈∆(S):
P := {P | ∃σ ∈∆(S) s.t. P = Pσ}.
(2)
Any P ∈P satisfies consistency conditions known as the Block-Marschak inequalities (Block &
Marschak, 1959), including skew-symmetry: P(y ≻y′) + P(y′ ≻y) = 1 ∀y, y′ ∈Y. A preference
learning algorithm is a mapping F : P →∆(Y) that assigns a policy to each preference function.
Throughout this paper, we say that a preference learning algorithm F implements a PSCF Φ if,
for every profile σ ∈∆(S), it holds that F(Pσ) = Φ(σ). The relationships between the profile,
preference function, and policy are illustrated in Figure 1.
2.2
TWO STANDARD PREFERENCE LEARNING ALGORITHMS
Next, we introduce two prominent preference learning algorithms and discuss their connections to
established concepts from probabilistic social choice theory.
Reinforcement learning from human feedback (RLHF).
The Bradley–Terry (BT) model, widely
used in preference modeling, assigns each alternative yi a reward ri with preference probabilities
3


Page 4:
Published as a conference paper at ICLR 2026
P(yi ≻yj) = exp(ri)/(exp(ri) + exp(rj)). Standard RLHF estimates these rewards by likeli-
hood maximization and then trains a policy to maximize expected rewards. Recent work (Siththa-
ranjan et al., 2024) shows that this procedure is equivalent to the maximal Borda rule from so-
cial choice theory, which deterministically chooses the alternative with the highest Borda score
B(y) := P
r∈S σr(M −r(y)). As proved in Appendix C, the ranking from BT-optimized rewards
coincides with Borda rankings, so RLHF without regularization (denoted by F RL) implements the
maximal Borda rule (denoted by ΦMB). Direct preference optimization (DPO) generalizes this by
adding Kullback–Leibler (KL) regularization relative to a reference policy (Rafailov et al., 2023).
Nash learning from human feedback (NLHF).
As highlighted in recent studies (Munos et al.,
2024; Swamy et al., 2024; Maura-Rivero et al., 2025), RLHF has limitations in scenarios involving
intransitive or cyclic preferences. An alternative y∗is called a Condorcet winner if it is preferred by
a majority over every other alternative, formally stated as P(y∗≻y) > 0.5 for all y ̸= y∗. When
aggregating preferences across multiple evaluators, scenarios without a Condorcet winner can arise,
which is called the Condorcet paradox. In such cases, selecting the alternative with the highest Borda
score fails to adequately represent collective preferences, as a deterministic policy cannot capture the
lack of consensus or nuanced preferences. To address intransitive preferences, the game-theoretic
approach, known as Nash learning from human feedback (NLHF) (Munos et al., 2024; Swamy et al.,
2024; Ye et al., 2024; Maura-Rivero et al., 2025), has been adopted to model preference learning
as a two-player constant-sum game maxπ1∈∆(Y) minπ2∈∆(Y) E(y1,y2)∼(π1,π2)[P(y1 ≻y2)], where
the equilibrium policy π∗cannot be uniformly outperformed. This algorithm, denoted by F NL,
implements the well-known PSCF maximal lotteries (ML) (Fishburn, 1984), denoted by ΦML.
3
AXIOMATIC FRAMEWORK FOR POPULATION-PROPORTIONAL ALIGNMENT
3.1
MOTIVATING EXAMPLE WITH BINARY ALTERNATIVES
Despite their practical utility, neither RLHF nor NLHF guarantees alignment proportional to the
evaluator’s preferences. To illustrate this point, we present a simple scenario involving binary
alternatives. Consider two alternatives, Y = {y1, y2}, and a profile σ consisting of two distinct
groups of evaluators: group G1 prefers alternative y1 over y2, while group G2 prefers y2 over y1.
Let wσ
1 and wσ
2 denote the population shares of groups G1 and G2, respectively. Suppose the two
alternatives are nearly tied, with (wσ
1 , wσ
2 ) = (1/2 + ϵ, 1/2 −ϵ) for an arbitrarily small positive
scalar ϵ. Then, the corresponding preference function is given by Pσ(y1 ≻y2) = 1/2 + ϵ and
Pσ(y2 ≻y1) = 1/2 −ϵ. Despite this minimal margin ϵ, both algorithms F RL(Pσ) and F NL(Pσ)
yield a deterministic policy that selects the alternative with slightly greater support, namely y1,
because such subtle differences in preferences (or rewards) are lost during the policy optimization.
This binary example highlights two potential limitations of RLHF and NLHF frameworks. First,
selecting policies that focus entirely on a single alternative may not accurately represent preferences
across evaluators, raising concerns about bias. Second, these methods have high sensitivity to small
perturbations in the preference function. Specifically, a slight shift in ϵ from negative to positive
abruptly flips the policy outcome (π(y1), π(y2)) from (0, 1) to (1, 0), making such approaches
vulnerable to small perturbations. These limitations underscore the need for a novel approach that
reflects the ratio of (wσ
1 , wσ
2 ) in the resulting policy.
3.2
PROPOSED AXIOMS FOR POPULATION-PROPORTIONAL ALIGNMENT AND ROBUSTNESS
Social choice theory studies the aggregation of individual preferences through an axiomatic approach,
which specifies desirable properties (axioms) and characterizes aggregation rules that satisfy them. In
particular, two fundamental axioms, monotonicity and Pareto efficiency, are presented in Appendix D.
Following this approach, we introduce the axioms that a PSCF Φ is desired to satisfy and propose a
preference learning algorithm F that implements such a PSCF.
Proposed axioms.
Motivated by the earlier example, we next introduce a new axiom designed
to ensure alignment with population distribution of preferences. Let Gk := {r ∈S | r(yk) = 1}
denote the set of rankings in which alternative yk is ranked first. The population share of group Gk is
denoted by wσ
k := P
r∈Gk σr. For notational convenience, we define σk ∈∆(S) as the normalized
4


Page 5:
Published as a conference paper at ICLR 2026
Table 1: Overview of standard PSCFs and axioms
Φ
F
Monotonicity
Pareto Efficiency
PPA
PBM
Maximal Borda (MB)
✓(RLHF)
✓
✓
×
×
Maximal lotteries (ML)
✓(NLHF)
×
✓
×
×
Random dictatorship (RD)
×
✓
✓
✓
✓
Proposed framework
✓
✓
✓
✓
✓
sub-profile restricted to rankings in Gk, where σk,r = σr/wσ
k for all r ∈Gk, and σk,r = 0 for all
r /∈Gk. Let Pσ
k denote the group-specific preference function, generated from σk, using the mapping
defined in equation 1. By construction, Pσ
k(yk ≻y) = 1 for all y ̸= yk, since this group unanimously
prefers yk over all other alternatives. The overall preference function is then a weighted aggregation
of the group-specific preferences: Pσ = PM
k=1 wσ
kPσ
k.
Under this definition, our first axiom ensures that the policy reflects each group’s population share.
Note that our proportionality notion focuses solely on the selection probability of each group’s top
choice and does not incorporate lower-ranked preferences.
Definition 3.1 (α-Population-proportional alignment (α-PPA)). A PSCF Φ satisfies α-population-
proportional alignment if π(yk)/wσ
k ≥α(σ) for all σ ∈∆(S) and yk ∈Y, where π = Φ(σ) and
α : ∆(S) →(0, 1].
The function α(σ) quantifies the strength of alignment: a higher value of α implies stronger alignment
with wσ, with α(σ) = 1 indicating perfect proportional alignment. Next, we examine the robustness
of Φ against manipulation through the following axiom.
Definition 3.2 (Single-group manipulated profile). Given a profile σ and a group index k ∈[M], a
profile σ′
k is called a single-group manipulated profile of σ if σ′
k can be obtained by modifying only
the ranking distribution of the sub-profile σk. Formally, σ′
k is a single-group manipulated profile of σ
if there exists a profile σ′ such that σ′
k = σ + wσ
k(σ′ −σk).
Definition 3.3 (γ-Population-bounded manipulability (γ-PBM)). A PSCF Φ satisfies γ-population-
bounded manipulability if, for any profile σ and its single-group manipulated profile σ′
k, we have
Φ(σ′
k)(yk) ≤γ1wσ
k + γ2, where γ = (γ1, γ2), γ1 > 0, and γ1 + γ2 = 1.
The γ-PBM axiom ensures that the maximum influence a single group can exert through manipulation
is bounded above by an affine function of its population share. Specifically, a group can only achieve
a deterministic policy selection for its preferred alternative (i.e., Φ(σ′
k)(yk) = 1) only if it constitutes
the entire evaluator population (i.e., wσ
k = 1). Note that a larger γ1 provides a stronger robustness
guarantee. Particularly, γ1 = 1 implies that the manipulated policy value is limited exactly to the
group’s true population share. We also note that the focus of the γ-PBM axiom differs from that of
classical strategyproofness: it does not constrain an individual participant’s incentive to misreport,
but instead limits the extent to which any group can become over-represented.
3.3
LIMITATIONS OF STANDARD PSCFS: AXIOM VIOLATIONS AND NON-IMPLEMENTABILITY
We next show that the standard PSCFs either fail to satisfy the proposed axioms or are not imple-
mentable by a preference learning algorithm. Consider a PSCF that aligns the policy exactly with
each group’s population distribution, commonly referred to as a random dictatorship (Brandt, 2017).
Definition 3.4 (Random dictatorship). A PSCF ΦRD is called a random dictatorship if ΦRD(σ) = wσ
for all σ ∈∆(S).
By definition, ΦRD satisfies both proposed axioms in their strongest forms: α-PPA with α(σ) = 1
for all σ ∈∆(S), and γ-PBM with γ = (1, 0). The following proposition establishes that ΦMB and
ΦML violate even the weakest forms of these axioms, whereas ΦRD satisfies all four axioms.
Proposition 3.5. ΦMB and ΦML violate the α-PPA axiom for any α and the γ-PBM axiom for any γ.
ΦRD satisfies all four axioms.
5


Page 6:
Published as a conference paper at ICLR 2026
The proof is provided in Appendix E. Unfortunately, ΦRD is not implementable by any pairwise
preference learning algorithm, since distinct profiles σ1 and σ2 may induce identical preference
functions Pσ1 = Pσ2 but different population distributions wσ1 ̸= wσ2 (see Appendix F for an
example). Because wσ cannot be recovered solely from Pσ, no mapping from preference functions to
policies can implement ΦRD1. Our goal, therefore, is to construct a preference learning algorithm F
that implements a PSCF Φ satisfying all four axioms. Table 1 summarizes the standard PSCFs, their
implementability, and satisfaction of the four axioms; see Brandl et al. (2022) for additional details.
4
ALGORITHMIC FRAMEWORK AND THEORETICAL GUARANTEES
4.1
POPULATION DISTRIBUTION RECOVERY FROM PAIRWISE PREFERENCES
In this section, we introduce a preference algorithm F, which implements a PSCF satisfying all four
axioms presented in the previous section. The framework first estimates the feasible set of underlying
population distributions w from given pairwise preferences P, and subsequently constructs a policy π
closely aligned with the inferred feasible set. We begin with the definition of a feasible population
distribution and the characterization of the set of all feasible population distributions.
Definition 4.1. A population distribution w is considered feasible given P, if there exists a profile
σ ∈∆(S) such that w = wσ and P = Pσ.
Proposition 4.2. The set of all feasible population distributions given P can be expressed as
W(P) :=
n
w ∈∆(Y)
 ∃(P1, . . . , PM) ∈PM s.t. P =
M
X
i=1
wiPi,
Pi(yi ≻y) = 1 ∀y ∈Y \ {yi}, ∀i ∈[M]
o
.
(3)
See Appendix G for the proof. In words, a population distribution w is feasible if and only if there
exist group-specific preference functions (P1, . . . , PM) such that P is their weighted aggregation,
and each Pi reflects a group of evaluators who unanimously prefer yi over all other alternatives.
The exact characterization of the set W(P) is challenging due to the constraints imposed by the set P.
We therefore propose a tractable polyhedral outer approximation of the set W(P), with the number
of constraints growing only linearly with the dimension M.
Definition 4.3. For each i ∈[M], define ui := miny∈Y\{yi} P(yi ≻y).
Theorem 4.4. The set of feasible population distributions satisfies
W(P) ⊆W(P) :=
n
w ∈∆(Y)
 wi ≤ui ∀i ∈[M]
o
.
(4)
The proof is given in Appendix H. To provide intuition, note that ui = 1 −maxy̸=yi P(y ≻yi) =
1 −P(y′ ≻yi), where y′ is the alternative most preferred over yi. Thus, ui represents the remaining
population share after excluding those who prefer y′ to yi. Thus, wi cannot exceed this value, as the
wi proportion of evaluators would always report yi as their preferred option. The tightness of the
outer approximation is further discussed in Appendix I, and the relation between Theorem 4.4 and
Tatli et al. (2024) is examined in Appendix J. Since wσ is not identifiable from pairwise comparison
data, perfect proportional alignment (i.e., α(σ) = 1 for all σ ∈∆(S)) is fundamentally unattainable.
Moreover, even achieving a uniform guarantee α(σ) > 2/M for all σ is impossible for any preference
learning algorithm (see Appendix K). This motivates designing algorithms that achieve α-PPA with
the largest possible α.
4.2
PROPOSED ALGORITHMIC FRAMEWORK WITH AXIOMATIC GUARANTEES
Given a polyhedron W(P), our goal is to select a policy π that guarantees the proportional alignment
to all w ∈W(P). To this end, we propose to assign probabilities to alternatives in proportion to the
derived upper bounds ui.
1In the literature, the class of implementable PSCFs is often referred to as the C2 class (Fishburn, 1977)
6


Page 7:
Published as a conference paper at ICLR 2026
Definition 4.5. The preference learning algorithm F ∗maps a preference function P to the policy
π(yi) =
ui
PM
j=1 uj
∀i ∈[M].
(5)
Let Φ∗denote the PSCF implemented by F ∗.
This construction adopts a conservative strategy for handling uncertainty in wσ by assigning probabil-
ities proportional to the most conservative estimate of each wσ
i . By doing so, the algorithm minimizes
the worst-case misalignment caused by the inevitable information loss from pairwise comparisons.
Formally, it solves maxπ∈∆(Y) minw∈W(P) ∥π/w∥∞.
We first establish the foundational axiomatic guarantees of the proposed framework.
Theorem 4.6 (Monotonicity & Pareto efficiency). The proposed PSCF Φ∗satisfies the monotonicity
and the Pareto efficiency.
The proofs are provided in Appendix L. Next, we show that Φ∗satisfies the α-PPA axiom. The
following lemma establishes that the ratio between the resulting policy and the true population share
is lower bounded by the inverse of the total sum of the upper bounds ui.
Lemma 4.7. For any profile σ ∈∆(S), the policy π = Φ∗(σ) satisfies
π(yi)
wσ
i
≥


M
X
j=1
uj


−1
∀i ∈[M].
(6)
The next lemma shows that this lower bound depends on the number of non-dominated alternatives:
Definition 4.8 (δ-dominated alternative). For any δ ∈[0, 1], an alternative y ∈Y is said to be
δ-dominated in a profile σ if there exists an alternative y′ ∈Y \ {y} such that Pσ(y′ ≻y) ≥δ.
Lemma 4.9. Let wσ,1 and wσ,2 denote the largest and second-largest elements of wσ, respectively.
Consider any δ ∈[0, 1], and let N σ
δ be the number of alternatives that are not δ-dominated in profile
σ. Then the lower bound in equation 6 lies within the range [α(σ), 1], where
α(σ) :=

(N σ
δ −1)(1 −wσ,1) + (1 −wσ,2) + (M −N σ
δ )(1 −δ)
−1 .
(7)
See Appendix M for the proofs. Combining both Lemmas, we obtain the following α-PPA guarantee:
Theorem 4.10 (α-PPA). The PSCF Φ∗satisfies the α-PPA axiom with α defined in equation 7.
Lemma 4.7 suggests that the actual alignment performance improves as PM
j=1 uj approaches 1.
This typically occurs when the number of non-1-dominated alternatives is small. Notably, when
there are only two non-1-dominated alternatives, substituting N σ
1 = 2 and wσ,1 + wσ,2 = 1 into
equation 7 yields α(σ) = 1, implying the perfect PPA in such cases. Moreover, when there exists
a single dominating group, meaning (wσ,1, wσ,2) approaches (1, 0), then α(σ) also approaches 1.
Importantly, because PM
j=1 uj can be computed directly from a given preference function P, the
alignment accuracy of the resulting policy can be evaluated at test time. In Appendix N, we present
additional bound analysis under a random-ranking model with a practically relevant level of variance.
Specifically, we report the average lower bounds from Lemma 4.7 and Lemma 4.9, showing that both
yield meaningful guarantees.
Finally, we present the population-bounded manipulability of the proposed method.
Theorem 4.11 (γ-PBM). Let π′ = Φ∗(σ′
k) denote a policy resulting from single-group manipulation
by group Gk. Then, the following inequality holds:
π′(yk) ≤
uk
uk + 1 −wσ
k
≤1
2(wσ
k + 1).
(8)
Thus, the PSCF Φ∗satisfies γ-PBM with (γ1, γ2) = (1/2, 1/2).
The proof is provided in Appendix O. Note that (γ1, γ2) = (1/2, 1/2) represents a worst-case bound.
The actual manipulability for each group is more tightly bounded by uk/(uk + 1 −wσ
k). For instance,
if uk ≤1/2 and wσ
k ≤1/2, then π′(yk) ≤1/2. This indicates that a non-majority group cannot
elevate their preferred alternative to majority status through manipulation. In addition, the above
result can be interpreted as a weaker form of strategyproofness (see Appendix P for details).
7


Page 8:
Published as a conference paper at ICLR 2026
10
−2
10
−1
10
0
10
1
10
2
10
3
β (log scale)
0.60
0.65
0.70
0.75
0.80
Win Rate
10
0
10
1
10
2
β (log scale)
0.00
0.02
0.04
0.06
PBM
0.0
0.2
0.4
0.6
PPA
Proposed (Win Rate)
RLHF (Win Rate)
NLHF (Win Rate)
Proposed (PPA)
RLHF & NLHF (PPA)
Proposed (Win Rate)
RLHF (Win Rate)
NLHF (Win Rate)
Proposed (PPA)
RLHF & NLHF (PPA)
Proposed (PBM)
RLHF (PBM)
NLHF (PBM)
Figure 2: Tabular experiment results (Section 5.1) for F β, F RL, and F NL. Left: win rate (left axis,
blue) and PPA level (right axis, orange). Right: PBM level (policy gain through manipulation).
4.3
BALANCING PPA AND CONDORCET CONSISTENCY
While F ∗and Φ∗are deliberately designed to satisfy PPA, one may still wish to incorporate majority-
based principles such as Condorcet consistency. However, it is impossible for any method to
simultaneously satisfy both α-PPA and Condorcet consistency.
Definition 4.12 (Condorcet consistency). A PSCF Φ satisfies Condorcet consistency if, for any
profile σ with a Condorcet winner y∗, Φ(σ)(y∗) = 1.
Proposition 4.13. No PSCF can simultaneously satisfy α-PPA and Condorcet consistency.
See Appendix Q for the proof. To balance two axioms, we propose a softmax-relaxed algorithm F β
(and its corresponding PSCF Φβ), by modifying F ∗as follows:
π(yi) =
ui exp(βui)
PM
j=1 uj exp(βuj)
∀i ∈[M].
(9)
The parameter β ≥0 controls how sharply the policy concentrates on alternatives with higher ui
values. When β = 0, the algorithm reduces to the original F ∗. As β →∞, the policy becomes
deterministic and converges to π(y∗) = 1, where y∗= arg maxi∈[M] ui. This limiting Φ∞is the
well-known minimax Condorcet method (Kramer, 1975), which satisfies Condorcet consistency (see
Appendix R for the proof).
Proposition 4.14. Φ∞satisfies Condorcet consistency.
The softmax relaxation offers a smooth trade-off between α-PPA and Condorcet consistency, con-
trolled by the parameter β. We analyze the theoretical behavior of intermediate β values in Ap-
pendix S, and empirically demonstrate the effects of varying β in Section 5. Additionally, Appendix T
discusses the connection to pairwise majority consistency (PMC) (Ge et al., 2024), which imposes a
stronger consistency requirement, ensuring the entire policy ranking aligns with majority preferences.
5
EXPERIMENTS
5.1
TABULAR EXPERIMENT: MOVIE RECOMMENDATION
Datasets and experimental setup.
To validate our theoretical findings, we evaluate the framework
on a movie recommendation task using 1,297 evaluator rankings over 20 movies from the MovieLens
1M dataset (Harper & Konstan, 2015). In each episode, we sample 105 pairwise comparisons i.i.d.
from the true preference function Pσ and train F β alongside two baselines, F RL and F NL.
We report averages and standard deviations over 50 episodes on three metrics: (i) win rate against a
uniform policy, E(y1,y2)∼(π,U)[Pσ(y1 ≻y2)], where U is the uniform distribution over Y, (ii) PPA
level, α(σ) = mini∈[M] π(yi)/wσ
i , and (iii) PBM, the average policy gain from a single group’s
strategic manipulation.
8


Page 9:
Published as a conference paper at ICLR 2026
Table 2: Win rate and PPA level α(σ) across datasets and algorithms
Dataset
Category
Metric
β = 0
β = 10−4
β = 10−2
β = 100
DPO
Synthetic
Color
Win rate
0.6157
0.6880
0.6961
0.8429
0.8566
PPA (α)
0.0883
0.0235
0.0183
0.0003
0.0000
Alpaca-GPT4
Expertise
Win rate
0.7613
0.7610
0.7634
0.7636
0.7697
PPA (α)
0.1428
0.1418
0.1392
0.1273
0.1321
Style
Win rate
0.8398
0.8432
0.8425
0.8530
0.8478
PPA (α)
0.5012
0.4197
0.3637
0.3635
0.3786
Results and discussion.
As shown in the left panel of Figure 2, RLHF and NLHF achieve high win
rates of 0.7784 and 0.7712, respectively, but both yield a PPA level of 0. For our proposed algorithm
F β, we observe the expected trade-off: as β increases, the win rate rises from 0.5987 to 0.7784,
while the PPA level decreases from 0.4869 to 0. These results confirm our theoretical prediction of
each algorithm’s behavior. Additionally, the average value of ui across i was 0.1892, suggesting that
the set W(P) in equation 4 provides a meaningfully tight estimate of wσ in our method.
Regarding PBM, the average gain was calculated as 0.0611 for RLHF, 0.0124 for NLHF, and
8.896 × 10−4 when β = 100. Overall, F β outperforms the baselines when β ≤101, indicating
that our proposed algorithm significantly reduces susceptibility to manipulation and supports its
robustness guarantee.
5.2
LARGE-SCALE EXPERIMENT: INSTRUCTION-TUNED LLMS
Datasets and experimental setup.
We next evaluate the algorithm in high-dimensional settings
with function approximation by fine-tuning the Qwen2.5-3B-Instruct model (Yang et al., 2024). For
a synthetic dataset, we construct 10 questions asking evaluators which color they prefer, with 10
candidate colors as possible responses. The true rankings of 1,000 evaluators are generated from
randomly sampled rewards, and 104 pairwise comparisons are drawn i.i.d. from Pσ. We next test the
algorithm on the Alpaca-GPT4 dataset (Peng et al., 2023), which contains 52k prompts. Following
prior work (Jang et al., 2023; Chakraborty et al., 2024), we consider two group categories (expertise
and style) and sample one pairwise comparison per prompt using GPT-4.1 (Achiam et al., 2023).
Further details on data generation and hyperparameters are provided in Appendix U.
For both datasets, we evaluate two metrics: (i) the win rate against a reference policy (the pretrained
model), E(x,y1,y2)∼(ρ,π,πref)[Pσ(y1 ≻y2 | x)], and (ii) the PPA level α(σ), comparing the results
with DPO as the baseline. To estimate the output policy (i.e., the group distribution of generated
responses), we used response logits directly for the synthetic dataset, and group classifications from
the annotation model (GPT-4.1) for the Alpaca-GPT4 dataset. The specific training algorithm is
described in Appendix V, and the full experimental code is included in the supplemental material.
Results and Discussion.
Table 2 presents the win rate and PPA level α(σ) across datasets and
algorithms. On the synthetic dataset, we observe a clear trade-off between win rate and PPA,
confirming that β effectively controls this balance and validating the algorithm’s effectiveness in
high-dimensional settings. For the Alpaca–GPT4 dataset, the trade-off is present but less pronounced,
largely because group distributions are inferred via an annotation model (GPT-4.1), which introduces
noise and obscures the effect of β. In contrast, the synthetic dataset allows direct computation from
response logits, enabling more precise estimates. These results suggest that a small synthetic dataset
can be used to evaluate a model’s PPA level and tune β to reach a desired target.
We highlight several practical considerations for deployment. First, our two-phase function approxi-
mation approach (learning u and π), has computational cost comparable to RLHF and higher than
DPO, suggesting the need for direct policy-optimization methods. Second, accurately evaluating
PPA levels in LLMs remains an open challenge, extending beyond the two approaches we consider,
namely logit-based estimation and group classification. As this paper primarily introduces the theo-
retical framework with supporting experiments, our findings should be viewed as initial evidence of
scalability, with further algorithmic and evaluation advances expected to strengthen these results.
9


Page 10:
Published as a conference paper at ICLR 2026
6
CONCLUSION AND FUTURE DIRECTIONS
This paper introduces a novel preference-learning framework that aligns policies proportionally with
population distributions inferred from pairwise comparison data. We believe this framework offers a
new perspective on alignment algorithms by shifting the focus beyond the conventional emphasis on
win rate. Furthermore, our work strengthens the connection between preference learning and social
choice theory by implementing a new class of probabilistic social choice functions, extending beyond
standard rules such as maximal Borda and maximal lotteries. Future research will aim to extend
the framework to incorporate lower-ranked preferences and to develop more efficient algorithms for
high-dimensional environments.
ACKNOWLEDGMENTS
This work was supported by the Office of Naval Research grant N000142512296. Jiawei Zhang was
supported by the Office of the Vice Chancellor for Research and Graduate Education at the University
of Wisconsin–Madison with funding from the Wisconsin Alumni Research Foundation. The authors
acknowledge the MIT Office of Research Computing and Data for providing high performance
computing resources that contributed to the results reported in this paper.
REFERENCES
Josh Achiam, Steven Adler, Sandhini Agarwal, Lama Ahmad, Ilge Akkaya, Florencia Leoni Aleman,
Diogo Almeida, Janko Altenschmidt, Sam Altman, Shyamal Anadkat, et al. Gpt-4 technical report.
arXiv preprint arXiv:2303.08774, 2023.
Jadie Adams, Brian Hu, Emily Veenhuis, David Joy, Bharadwaj Ravichandran, Aaron Bray, Anthony
Hoogs, and Arslan Basharat. Steerable pluralism: Pluralistic alignment via few-shot comparative
regression. In Proceedings of the AAAI/ACM Conference on AI, Ethics, and Society, volume 8, pp.
15–25, 2025.
Stéphane Airiau, Haris Aziz, Ioannis Caragiannis, Justin Kruger, Jérôme Lang, and Dominik Peters.
Portioning using ordinal preferences: Fairness and efficiency. Artificial Intelligence, 314:103809,
2023.
Haris Aziz and Barton E Lee. Proportionally representative participatory budgeting with ordinal
preferences. In Proceedings of the AAAI Conference on Artificial Intelligence, volume 35, pp.
5110–5118, 2021.
Haris Aziz and Nisarg Shah. Participatory budgeting: Models and approaches. In Pathways Between
Social Science and Computational Social Science: Theories, Methods, and Interpretations, pp.
215–236. Springer, 2020.
Haris Aziz, Markus Brill, Vincent Conitzer, Edith Elkind, Rupert Freeman, and Toby Walsh. Justified
representation in approval-based committee voting. Social Choice and Welfare, 48(2):461–485,
2017.
Haris Aziz, Barton Lee, and Nimrod Talmon. Proportionally representative participatory budgeting:
Axioms and algorithms. In Proceedings of the 17th International Conference on Autonomous
Agents and Multiagent Systems (AAMAS 2018), pp. 23–31. Association for Computing Machinery,
2018.
Erdem Bıyık, Nicolas Huynh, Mykel J Kochenderfer, and Dorsa Sadigh. Active preference-based
gaussian process regression for reward learning and optimization. The International Journal of
Robotics Research, 43(5):665–684, 2024.
Henry David Block and Jacob Marschak. Random orderings and stochastic theories of response.
Cowles Foundation Discussion Papers, 1959.
Florian Brandl, Felix Brandt, and Christian Stricker. An analytical and experimental comparison of
maximal lottery schemes. Social Choice and Welfare, 58(1):5–38, 2022.
10


Page 11:
Published as a conference paper at ICLR 2026
Felix Brandt. Rolling the dice: Recent results in probabilistic social choice. Trends in computational
social choice, pp. 3–26, 2017.
Thomas Kleine Buening, Jiarui Gan, Debmalya Mandal, and Marta Kwiatkowska. Strategyproof
reinforcement learning from human feedback. arXiv preprint arXiv:2503.09561, 2025.
Souradip Chakraborty, Jiahao Qiu, Hui Yuan, Alec Koppel, Dinesh Manocha, Furong Huang, Amrit
Bedi, and Mengdi Wang. Maxmin-rlhf: Alignment with diverse human preferences. In Interna-
tional Conference on Machine Learning, pp. 6116–6135. PMLR, 2024.
Daiwei Chen, Yi Chen, Aniket Rege, and Ramya Korlakai Vinayak. Pal: Pluralistic alignment
framework for learning from heterogeneous preferences. arXiv preprint arXiv:2406.08469, 2024.
Paul F Christiano, Jan Leike, Tom Brown, Miljan Martic, Shane Legg, and Dario Amodei. Deep
reinforcement learning from human preferences. Advances in neural information processing
systems, 30, 2017.
Vincent Conitzer, Rachel Freedman, Jobst Heitzig, Wesley H Holliday, Bob M Jacobs, Nathan
Lambert, Milan Mosse, Eric Pacuit, Stuart Russell, Hailey Schoelkopf, et al. Position: Social
choice should guide ai alignment in dealing with diverse human feedback. In International
Conference on Machine Learning, pp. 9346–9360. PMLR, 2024.
Jessica Dai and Eve Fleisig. Mapping social choice theory to rlhf. arXiv preprint arXiv:2404.13038,
2024.
Michael Dummett. Voting procedures. Oxford University Press UK, 1984.
Soroush Ebadian, Anson Kahng, Dominik Peters, and Nisarg Shah. Optimized distortion and
proportional fairness in voting. ACM Transactions on Economics and Computation, 12(1):1–39,
2024.
Peter C Fishburn. Condorcet social choice functions. SIAM Journal on applied Mathematics, 33(3):
469–489, 1977.
Peter C Fishburn. Probabilistic social choice based on simple voting comparisons. The Review of
Economic Studies, 51(4):683–692, 1984.
Luise Ge, Daniel Halpern, Evi Micha, Ariel D Procaccia, Itai Shapira, Yevgeniy Vorobeychik, and
Junlin Wu. Axioms for ai alignment from human feedback. Advances in Neural Information
Processing Systems, 37, 2024.
Allan Gibbard. Manipulation of voting schemes: a general result. Econometrica: journal of the
Econometric Society, pp. 587–601, 1973.
Daniel Halpern, Evi Micha, Ariel D Procaccia, and Itai Shapira. Pairwise calibrated rewards for
pluralistic alignment. arXiv preprint arXiv:2506.06298, 2025.
Shugang Hao and Lingjie Duan. Online learning from strategic human feedback in llm fine-tuning.
In ICASSP 2025-2025 IEEE International Conference on Acoustics, Speech and Signal Processing
(ICASSP), pp. 1–5. IEEE, 2025.
F Maxwell Harper and Joseph A Konstan. The movielens datasets: History and context. Acm
transactions on interactive intelligent systems (tiis), 5(4):1–19, 2015.
Joel Jang, Seungone Kim, Bill Yuchen Lin, Yizhong Wang, Jack Hessel, Luke Zettlemoyer, Hannaneh
Hajishirzi, Yejin Choi, and Prithviraj Ammanabrolu. Personalized soups: Personalized large
language model alignment via post-hoc parameter merging. arXiv preprint arXiv:2310.11564,
2023.
Cheol Woo Kim, Jai Moondra, Shresth Verma, Madeleine Pollack, Lingkai Kong, Milind Tambe, and
Swati Gupta. Navigating the social welfare frontier: Portfolios for multi-objective reinforcement
learning. In International Conference on Machine Learning, pp. 30631–30653. PMLR, 2025.
11


Page 12:
Published as a conference paper at ICLR 2026
Kihyun Kim, Jiawei Zhang, Asuman E Ozdaglar, and Pablo Parrilo. A unified linear programming
framework for offline reward learning from human demonstrations and feedback. In International
Conference on Machine Learning, pp. 24694–24712. PMLR, 2024.
Gerald H Kramer. A dynamical model of political equilibrium. Cowles Foundation Discussion
Papers, 629, 1975.
Andras Kupcsik, David Hsu, and Wee Sun Lee. Learning dynamic robot-to-human object handover
from human feedback. In Robotics Research: Volume 1, pp. 161–176. Springer, 2017.
Roberto-Rafael Maura-Rivero, Marc Lanctot, Francesco Visin, and Kate Larson. Jackpot! alignment
as a maximal lottery. arXiv preprint arXiv:2501.19266, 2025.
Abhilash Mishra. Ai alignment and social choice: Fundamental limitations and policy implications.
arXiv preprint arXiv:2310.16048, 2023.
Remi Munos, Michal Valko, Daniele Calandriello, Mohammad Gheshlaghi Azar, Mark Rowland,
Zhaohan Daniel Guo, Yunhao Tang, Matthieu Geist, Thomas Mesnard, Côme Fiegel, et al. Nash
learning from human feedback. In International Conference on Machine Learning, pp. 36743–
36768. PMLR, 2024.
Long Ouyang, Jeffrey Wu, Xu Jiang, Diogo Almeida, Carroll Wainwright, Pamela Mishkin, Chong
Zhang, Sandhini Agarwal, Katarina Slama, Alex Ray, et al. Training language models to follow
instructions with human feedback. Advances in neural information processing systems, 35:27730–
27744, 2022.
Chanwoo Park, Mingyang Liu, Dingwen Kong, Kaiqing Zhang, and Asuman Ozdaglar.
Rlhf
from heterogeneous feedback via personalization and preference aggregation. arXiv preprint
arXiv:2405.00254, 2024.
Baolin Peng, Chunyuan Li, Pengcheng He, Michel Galley, and Jianfeng Gao. Instruction tuning with
gpt-4. arXiv preprint arXiv:2304.03277, 2023.
Dominik Peters, Grzegorz Pierczy´nski, and Piotr Skowron. Proportional participatory budgeting with
additive utilities. Advances in Neural Information Processing Systems, 34:12726–12737, 2021.
Ariel D Procaccia and Jeffrey S Rosenschein. The distortion of cardinal preferences in voting. In
International Workshop on Cooperative Information Agents, pp. 317–331. Springer, 2006.
Rafael Rafailov, Archit Sharma, Eric Mitchell, Christopher D Manning, Stefano Ermon, and Chelsea
Finn. Direct preference optimization: Your language model is secretly a reward model. Advances
in Neural Information Processing Systems, 36:53728–53741, 2023.
Shyam Sundhar Ramesh, Yifan Hu, Iason Chaimalas, Viraj Mehta, Pier Giuseppe Sessa, Haitham
Bou Ammar, and Ilija Bogunovic. Group robust preference optimization in reward-free rlhf.
Advances in Neural Information Processing Systems, 37:37100–37137, 2024.
Zhekun Shi, Kaizhao Liu, Qi Long, Weijie J Su, and Jiancong Xiao.
Fundamental limits of
game-theoretic llm alignment: Smith consistency and preference matching.
arXiv preprint
arXiv:2505.20627, 2025.
Anand Siththaranjan, Cassidy Laidlaw, and Dylan Hadfield-Menell.
Distributional preference
learning: Understanding and accounting for hidden context in rlhf. In The Twelfth International
Conference on Learning Representations, 2024.
Taylor Sorensen, Jared Moore, Jillian Fisher, Mitchell L Gordon, Niloofar Mireshghallah, Christo-
pher Michael Rytting, Andre Ye, Liwei Jiang, Ximing Lu, Nouha Dziri, et al. Position: A roadmap
to pluralistic alignment. In International Conference on Machine Learning, pp. 46280–46302.
PMLR, 2024.
Ermis Soumalias, Michael J Curry, and Sven Seuken. Truthful aggregation of llms with an application
to online advertising. arXiv preprint arXiv:2405.05905, 2024.
12


Page 13:
Published as a conference paper at ICLR 2026
Nisan Stiennon, Long Ouyang, Jeffrey Wu, Daniel Ziegler, Ryan Lowe, Chelsea Voss, Alec Radford,
Dario Amodei, and Paul F Christiano. Learning to summarize with human feedback. Advances in
neural information processing systems, 33:3008–3021, 2020.
Haoran Sun, Yurong Chen, Siwei Wang, Wei Chen, and Xiaotie Deng. Mechanism design for llm
fine-tuning with multiple reward models. arXiv preprint arXiv:2405.16276, 2024.
Gokul Swamy, Christoph Dann, Rahul Kidambi, Steven Wu, and Alekh Agarwal. A minimaximalist
approach to reinforcement learning from human feedback. In International Conference on Machine
Learning, pp. 47345–47377. PMLR, 2024.
Gokcan Tatli, Yi Chen, and Ramya Korlakai Vinayak. Learning populations of preferences via
pairwise comparison queries. In International Conference on Artificial Intelligence and Statistics,
pp. 1720–1728. PMLR, 2024.
Jiancong Xiao, Zhekun Shi, Kaizhao Liu, Qi Long, and Weijie J Su.
Theoretical tensions in
rlhf: Reconciling empirical success with inconsistencies in social choice theory. arXiv preprint
arXiv:2506.12350, 2025.
Wanqi Xue, Qingpeng Cai, Zhenghai Xue, Shuo Sun, Shuchang Liu, Dong Zheng, Peng Jiang, Kun
Gai, and Bo An. Prefrec: Recommender systems with human preferences for reinforcing long-term
user engagement. In Proceedings of the 29th ACM SIGKDD Conference on Knowledge Discovery
and Data Mining, pp. 2874–2884, 2023.
An Yang, Baosong Yang, Beichen Zhang, Binyuan Hui, Bo Zheng, Bowen Yu, Chengyuan Li,
Dayiheng Liu, Fei Huang, Haoran Wei, Huan Lin, Jian Yang, Jianhong Tu, Jianwei Zhang, Jianxin
Yang, Jiaxi Yang, Jingren Zhou, Junyang Lin, Kai Dang, Keming Lu, Keqin Bao, Kexin Yang,
Le Yu, Mei Li, Mingfeng Xue, Pei Zhang, Qin Zhu, Rui Men, Runji Lin, Tianhao Li, Tianyi
Tang, Tingyu Xia, Xingzhang Ren, Xuancheng Ren, Yang Fan, Yang Su, Yichang Zhang, Yu Wan,
Yuqiong Liu, Zeyu Cui, Zhenru Zhang, and Zihan Qiu. Qwen2.5 technical report. arXiv preprint
arXiv:2412.15115, 2024.
Binwei Yao, Zefan Cai, Yun-Shiuan Chuang, Shanglin Yang, Ming Jiang, Diyi Yang, and Junjie
Hu. No preference left behind: Group distributional preference optimization. In The Thirteenth
International Conference on Learning Representations, 2025.
Chenlu Ye, Wei Xiong, Yuheng Zhang, Hanze Dong, Nan Jiang, and Tong Zhang. Online iterative
reinforcement learning from human feedback with general preference model. Advances in Neural
Information Processing Systems, 37:81773–81807, 2024.
Huiying Zhong, Zhun Deng, Weijie J Su, Zhiwei Steven Wu, and Linjun Zhang. Provable multi-party
reinforcement learning with diverse human feedback. arXiv preprint arXiv:2403.05006, 2024.
Daniel M Ziegler, Nisan Stiennon, Jeffrey Wu, Tom B Brown, Alec Radford, Dario Amodei, Paul
Christiano, and Geoffrey Irving. Fine-tuning language models from human preferences. arXiv
preprint arXiv:1909.08593, 2019.
13


Page 14:
Published as a conference paper at ICLR 2026
A
NOTATION
We summarize the mathematical notation used in the paper.
Symbol
Description
Rankings, profiles, groups, and preferences
[M]
The set of integers {1, 2, . . . , M}.
Y = {y1, . . . , yM}
The set of M alternatives.
∆(Y)
Probability simplex over a finite set Y.
S
The set of all rankings (permutations) over Y.
r ∈S
A ranking, where r(yi) = k means yi is ranked k-th.
σ ∈∆(S)
A profile, i.e., population distribution over rankings.
σr ∈[0, 1]
Proportion of evaluators who adopt ranking r.
Gk
Group k, set of rankings where yk is ranked first.
wσ
k ∈[0, 1]
Population share of evaluators whose top choice is yk.
σk ∈∆(S)
Sub-profile of group Gk (evaluators who rank yk first).
π ∈∆(Y)
A policy, i.e., probability distribution over alternatives.
P ∈P
Preference function, P(y ≻y′) is the probability y is preferred to y′.
Pσ ∈P
Preference function induced by a profile σ.
Pk, Pσ
k
Group-specific preference function for Gk.
P
Set of all preference functions induced by some profile in ∆(S).
Preference learning algorithms, PSCFs, and axioms
F : P →∆(Y)
Preference learning algorithm, mapping a preference function to a
policy.
Φ : ∆(S) →∆(Y)
Probabilistic social choice function (PSCF), mapping a profile to a
policy.
F RL, ΦMB
RLHF algorithm and its PSCF (maximal Borda rule).
F NL, ΦML
NLHF algorithm and its PSCF (maximal lotteries).
B(y)
Borda score: B(y) := P
r∈S σr (M −r(y)).
α(σ) ∈R
Strength of population-proportional alignment (PPA) guarantee.
γ = (γ1, γ2) ∈R2
Parameters characterizing population-bounded manipulability (PBM).
σ′
k
Single-group manipulated profile of σ (group k perturbs only its sub-
profile).
ui ∈[0, 1]
ui := miny̸=yi P(yi ≻y), upper bound on feasible population share
for yi.
W(P)
Set of feasible population distributions consistent with preference func-
tion P.
W(P)
Polyhedral outer approximation of W(P) (via wi ≤ui constraints).
δ ∈[0, 1]
Dominance threshold (used in δ-domination definition).
N σ
δ
Number of alternatives not δ-dominated under profile σ.
wσ
1 , wσ
2
Largest and second-largest elements of wσ.
y∗
Condorcet winner satisfying P(y∗≻y) > 1
2 for all y ̸= y∗.
F ∗, Φ∗
Proposed (baseline) algorithm/PSCF using ui with π(yi) ∝ui.
F β, Φβ
Softmax-relaxed algorithm/PSCF with concentration parameter β ≥0.
Offline learning algorithm with function approximation
x ∈X
Context (e.g., prompt or state) and context space.
D = {(xi, yw
i , yℓ
i)}N
i=1
Offline dataset of pairwise comparisons (yw preferred to yℓ).
ρ(x), πd(y | x)
Context (prompt) and query data distribution.
µ
Selector model used to form u.
Fµ, Fπ
Function classes for µ and π.
bP, bµ, bu
Empirical estimate of P, µ, and u.
bπβ, bπ
Softmax policy constructed from bu and final estimated policy
14


Page 15:
Published as a conference paper at ICLR 2026
B
ADDITIONAL RELATED WORK
In this section, we discuss recent work that aims to proportionally represent the diversity of human
preferences.
Limitations of the BT model.
Recent studies have highlighted limitations of the standard RLHF
approach under BT model assumption, which fails to capture the multifaceted and sometimes con-
flicting nature of human preferences. For example, Kim et al. (2024) demonstrated that the standard
MLE algorithms under the BT model can become unstable, particularly in the presence of evaluators
exhibiting greedy behavior. They proposed to address this limitation by estimating a set of feasible
reward functions without relying on specific modeling assumptions. Additionally, Siththaranjan et al.
(2024) established a theoretical equivalence between RLHF and the Borda voting rule, showing that
the optimized rankings from standard methods frequently violate majority preferences. To address
this issue, they introduced a distributional approach incorporating hidden context variables to address
diverse evaluator preferences. Furthermore, Ge et al. (2024) analyzed reward optimization methods
under parameterizations, revealing their inherent violation of fundamental axioms such as Pareto
efficiency. They proposed a novel algorithm explicitly designed to satisfy these axioms.
Approaches from social choice theory.
Parallel research efforts have explored unbiased aggrega-
tion of heterogeneous human preferences, grounded in social choice theory. Chakraborty et al. (2024)
formally proved the impossibility of equitably aligning single-reward models across diverse evaluator
groups, and proposed learning reward mixtures using the EM algorithm followed by maximizing
the minimum utility across subpopulations. Additionally, Zhong et al. (2024) conducted a rigorous
analysis of multi-group reward learning under various social welfare criteria, such as Nash, utilitarian,
and Leximin functions, and provided theoretical alignment guarantees. Park et al. (2024) proposed a
probabilistic opinion pooling function that directly aggregates multiple probabilistic models into a
single policy, as well as personalized algorithms that output individualized policies after estimating
confidence sets. Shi et al. (2025) analyze the theoretical limits of NLHF, showing that exact prefer-
ence matching is generally impossible, highlighting intrinsic limitations of this paradigm. Concurrent
work by Xiao et al. (2025) is closely related to our work. They investigate the tension between
RLHF’s empirical success and its incompatibility with social choice axioms (PMC and Condorcet
consistency), showing that RLHF can satisfy them under a practical assumption about preference
labeling. Moreover, they propose a new axiom, group preference matching, which requires the policy
to reproduce group-level preference distributions in proportion to their population weights. However,
they do not provide an algorithmic framework that satisfies this axiom.
Proportional representation in voting systems.
The concept of proportional representation has
been extensively studied through an axiomatic lens within voting systems. A foundational axiom in
multi-winner voting systems is proportionality for solid coalitions (PSC), which dictates that any solid
coalition (a group of voters who agree on their preferred set of winners) must be guaranteed a number
of elected candidates proportional to its population size (Dummett, 1984). Building on this, work
in approval-based voting introduced justified representation (JR) and its stronger variant, extended
justified representation (EJR), which ensure that every cohesive group (voters who approve the same
set of candidates) receives proportional representation (Aziz et al., 2017). Proportional representation
has also been widely applied to participatory budgeting (PB) (Aziz & Shah, 2020), focusing on
axiomatic methods for distributing funds among public projects under a budget constraint. More
recently, Ebadian et al. (2024) analyze distortion bounds of voting rules (Procaccia & Rosenschein,
2006) under a proportional fairness objective. However, the literature defining these proportional
representation notions typically assumes either approval-based multi-winner elections (Aziz et al.,
2018) or access to full preference information such as ordinal rankings Aziz & Lee (2021); Peters
et al. (2021); Airiau et al. (2023); Ebadian et al. (2024). This stands in sharp contrast to our approach,
which operates under the minimal assumption of pairwise comparison data and seeks a probabilistic
choice distribution over candidates, rather than a fixed multi-winner.
Pluralistic alignment.
Emerging research on pluralistic alignment seeks to reflect diverse per-
spectives in AI systems, with a particular focus on LLMs. Sorensen et al. (2024) outlined three
complementary frameworks for pluralistic alignment: Overton pluralism, which captures the range of
reasonable responses; steerable pluralism, which allows models to adapt to particular attributes; and
15


Page 16:
Published as a conference paper at ICLR 2026
distributional pluralism, which aligns model outputs with population-level distributions. Chen et al.
(2024) introduced a framework that modeled heterogeneous human preferences from the ground
up using the ideal point model and mixture modeling. Yao et al. (2025) proposed group distribu-
tional preference optimization (GDPO), a method that aligns models with the group preferences by
estimating the underlying belief distribution and conditioning responses on those beliefs, ensuring
representation of both majority and minority views. Adams et al. (2025) developed a steerable
pluralistic alignment algorithm, enabling models to adapt to individual preference profiles through
few-shot comparative regression across fine-grained attributes. While these approaches show promise,
they generally rely on explicit group identification, restricting their applicability in scenarios where
group labels are unavailable or difficult to determine. In contrast, our work does not require explicit
knowledge of evaluator groups. Instead, we infer population distributions directly from pairwise
comparison data and align policies accordingly. In parallel with our work, the problem of recovering
a distribution over reward functions from aggregate pairwise comparisons is formalized under the
pairwise calibration framework (Halpern et al., 2025). Our approach can be interpreted as selecting a
structured solution within this inherently ill-conditioned problem, further constrained to satisfy the
proportional alignment and robustness properties that we target.
C
EQUIVALENCE OF BT-MLE REWARDS RANKING AND BORDA RANKING
Proposition C.1. Let r∗∈RM be a maximizer of the likelihood function
L(r) :=
X
i<j

Pσ(yi ≻yj) log

eri
eri + erj

+ Pσ(yj ≻yi) log

erj
eri + erj

.
(10)
Then, the ordering of alternatives induced by r∗is identical to the ordering induced by the Borda
score B of σ. Formally, for any i, j ∈[M],
r∗
i > r∗
j
⇐⇒
B(yi) > B(yj).
(11)
Proof. The gradient of L(r) with respect to ri is given by:
∂L(r)
∂ri
=
X
j̸=i
[Pσ(yi ≻yj) −sigmoid(ri −rj)] ,
(12)
where sigmoid(x) := 1/(1 + e−x). At the optimal solution r∗, the first-order condition requires that
X
j̸=i

Pσ(yi ≻yj) −sigmoid(r∗
i −r∗
j )

= 0.
(13)
Now, consider two distinct alternatives i and k, and suppose that r∗
i > r∗
k. Since the sigmoid function
is monotonically increasing, for any j ̸= i, k, we have sigmoid(r∗
i −r∗
j ) > sigmoid(r∗
k −r∗
j ), and
also sigmoid(r∗
i −r∗
k) > sigmoid(r∗
k −r∗
i ). From the first-order conditions at optimality, we have:
X
j̸=i
Pσ(yi ≻yj) =
X
j̸=i
sigmoid(r∗
i −r∗
j ) and
X
j̸=k
Pσ(yk ≻yj) =
X
j̸=k
sigmoid(r∗
k −r∗
j ). (14)
Since r∗
i > r∗
k, it follows that
X
j̸=i
sigmoid(r∗
i −r∗
j ) >
X
j̸=k
sigmoid(r∗
k −r∗
j ).
(15)
Therefore, we have
X
j̸=i
Pσ(yi ≻yj) >
X
j̸=k
Pσ(yk ≻yj).
(16)
By definition, Pσ(yi ≻yj) = P
r∈S σr · 1{r(yi)<r(yj)}. Substituting this into the inequality above,
we get
X
r∈S
σr ·
X
j̸=i
1{r(yi)<r(yj)} >
X
r∈S
σr ·
X
j̸=k
1{r(yk)<r(yj)}.
(17)
16


Page 17:
Published as a conference paper at ICLR 2026
Recall that the Borda score is defined as B(y) := P
r∈S σr · (M −r(y)), we can rewrite the inner
sums in the inequality as:
X
j̸=i
1{r(yi)<r(yj)} = (M −1) −(r(yi) −1) = M −r(yi),
(18)
and similarly,
X
j̸=k
1{r(yk)<r(yj)} = M −r(yk).
(19)
Thus, the inequality becomes
X
r∈S
σr · (M −r(yi)) >
X
r∈S
σr · (M −r(yk)),
(20)
which is equivalent to B(yi) > B(yk).
For the converse, assume B(yi) > B(yk). Following similar steps in reverse, this implies
X
j̸=i
Pσ(yi ≻yj) >
X
j̸=k
Pσ(yk ≻yj),
(21)
which leads to
X
j̸=i
sigmoid(r∗
i −r∗
j ) >
X
j̸=k
sigmoid(r∗
k −r∗
j ).
(22)
This inequality can only hold if r∗
i > r∗
k. Therefore, we have shown that r∗
i > r∗
j ⇐⇒B(yi) >
B(yj), completing the proof.
D
FUNDAMENTAL AXIOMS: MONOTONICITY AND PARETO EFFICIENCY
In this section, we present the definition of two fundamental axioms in social choice theory: mono-
tonicity and Pareto efficiency. For detailed discussions of these axioms, we refer readers to Brandt
(2017); Ge et al. (2024).
Definition D.1 (Monotonicity). A PSCF Φ satisfies monotonicity if, for any alternative y ∈Y,
improving its ranking in a profile without changing other relative rankings cannot decrease its
probability in the resulting policy. Formally, if profile σ′ is obtained from σ by improving the ranking
of y in some r ∈S with σr > 0, then Φ(σ′)(y) ≥Φ(σ)(y).
Definition D.2 (Pareto efficiency). A PSCF Φ satisfies Pareto efficiency if, whenever an alternative
y is ranked above y′ in every ranking r with nonzero population share, the resulting policy assigns
at least as much probability to y as to y′. Formally, if r(y) < r(y′) for all r ∈S with σr > 0, then
Φ(σ)(y) ≥Φ(σ)(y′).
E
PROOF OF PROPOSITION 3.5
We first demonstrate that ΦMB and ΦML violate α-PPA. Consider a preference profile σ with the
following characteristics: (i) The population share of each group is nearly identical, with G1 having a
population share wσ
1 that is ϵ greater than the average, and G2 having a population share wσ
2 that is ϵ
less than the average. (ii) Within each group Gk, there is indifference between any two alternatives
other than yk. That is, Pσ
k(yi ≻yj) = 1/2 for all i, j ̸= k. Given this profile, we will show that for
any ϵ > 0, both RLHF and NLHF yield a deterministic policy that selects y1.
The population distribution and pairwise preference function satisfy
wσ =
 1
M + ϵ, 1
M −ϵ, 1
M , 1
M , . . . , 1
M

and Pσ
k(yi ≻yj) = 1
2,
∀i, j ̸= k.
(23)
Then, the aggregated pairwise preferences Pσ are computed as follows:
• Pσ(y1 ≻y2) = 1
2 + ϵ
• Pσ(y1 ≻y) = 1
2 + ϵ
2 for any y ̸= y1, y2
17


Page 18:
Published as a conference paper at ICLR 2026
• Pσ(y2 ≻y) = 1
2 −ϵ
2 for any y ̸= y1, y2
• Pσ(y ≻y′) = 1
2 for any y, y′ ̸= y1, y2
Under this profile, for any ϵ > 0, both ΦMB and ΦML result in a policy where π(y1) = 1, and
π(yi) = 0 for any i ̸= 1. This implies that π(yi)/wσ
i = 0 for any i ̸= 1, which violates α-PPA for
any α > 0.
Next, we show that ΦML violates γ-PBM using the profile described earlier with M = 3. The
aggregated preference function Pσ can be represented by the following matrix:
Pσ =


1
2
1
2 + ϵ
1+ϵ
2
1
2 −ϵ
1
2
1−ϵ
2
1−ϵ
2
1+ϵ
2
1
2

.
(24)
Now, suppose that group G3 manipulates their sub-profile from Pσ
3(y1 ≻y2) = 1
2 to Pσ′
3 (y1 ≻
y2) = 0. Then, the resulting manipulated aggregated preference function Pσ′ is calculated as:
Pσ′ =


1
2
1
3 + ϵ
1+ϵ
2
2
3 −ϵ
1
2
1−ϵ
2
1−ϵ
2
1+ϵ
2
1
2

.
(25)
ΦML yields a stochastic policy that depends on the value of ϵ. For example, if ϵ = 1/12, the resulting
policy is π =
 1
4, 1
4, 1
2

. However, as ϵ approaches 0, the resulting policy converges to [0, 0, 1]. This
shows that π′(y3) →1 while wσ
3 = 1/3, thus demonstrating that there exists no γ1 > 0 for which
ΦML satisfies γ-PBM.
To show that ΦMB violates γ-PBM, consider the case with M = 3 where the profile σ consists of the
following three groups of evaluators:
σ = {(y1 ≻y2 ≻y3) × 0.30, (y2 ≻y1 ≻y3) × 0.45, (y3 ≻y1 ≻y2) × 0.25},
(26)
where (y1 ≻y2 ≻y3) represents a ranking r and “×0.30” indicates that σr = 0.30. Then,
the Borda scores are calculated as B = [1.3, 1.20, 0.5]. Thus, ΦMB(σ) = π, where π(y1) = 1.
Next, suppose the second group strategically misreports their preference from (y2 ≻y1 ≻y3) to
(y2 ≻y3 ≻y1). Then, the Borda scores are calculated as B′ = [0.85, 1.2, 0.95]. The resulting policy
is then π′(y2) = 1, with the population share of the second group being wσ
2 = 0.45. This example
demonstrates that there exists no γ1 > 0 for which ΦMB satisfies γ-PBM.
Next, we show that ΦRD satisfies all four axioms. ΦRD satisfies monotonicity because improving
ranking of y cannot decrease the number of evaluators whose top choice is y. In addition, ΦRD
satisfies Pareto efficiency because if r(yj) < r(yk) for all r ∈S with σr > 0, then we have
wσ
k = 0 and ΦRD(σ)(yk) = 0. Additionally, ΦRD satisfies α-PPA with α(σ) = 1 for all σ by its
definition, and also satisfy γ-PBM with (γ1, γ2) = (1, 0) because each group Gk cannot increase wσ
k
by manipulation.
F
PROOF OF THE NON-IMPLEMENTABILITY OF ΦRD
Suppose that ΦRD can be implemented by a preference learning algorithm F RD. Let M = 3, and
consider two preference profiles, σ1 and σ2, defined as follows:
σ1 = {(y1 ≻y2 ≻y3) × 1/3, (y2 ≻y1 ≻y3) × 1/3, (y3 ≻y1 ≻y2) × 1/3},
σ2 = {(y1 ≻y2 ≻y3) × 2/3, (y3 ≻y2 ≻y1) × 1/3}.
(27)
Both of these profiles induce the same aggregated preference function Pσ = Pσ1 = Pσ2, where
Pσ =


1
2
2
3
2
3
1
3
1
2
2
3
1
3
1
3
1
2

.
(28)
Therefore, the preference learning algorithm F RD would produce the same policy for both σ1
and σ2. However, according to the definition of ΦRD, we have ΦRD(σ1) = [1/3, 1/3, 1/3] and
ΦRD(σ2) = [2/3, 0, 1/3], which are different policies. This implies that F RD does not implement
ΦRD, which contradicts our initial assumption. Therefore, ΦRD is not implementable by a preference
learning algorithm.
18


Page 19:
Published as a conference paper at ICLR 2026
G
PROOF OF PROPOSITION 4.2
First, consider any feasible population share w given a preference function P. By Definition 4.1,
there exists a profile σ such that w = wσ and P = Pσ. Then, the group-specific preference functions
(Pσ
1, . . . , Pσ
M) that constitute Pσ, satisfy the condition in equation 3, which implies that w ∈W(P).
Next, consider any w ∈W(P). By the definition of W(P), there exist (P1, . . . , PM) ∈PM such
that P = PM
k=1 wkPk, where each Pk satisfies Pk(yk ≻y) = 1 for all y ̸= yk. Since Pk ∈P,
there exists a profile σk that induces Pk, such that Pk = Pσk. Now, if we consider an aggregated
profile σ := PM
k=1 wkσk by combining these group profiles with the corresponding weights, then
the preference function of σ will be Pσ = PM
k=1 wkPσk = PM
k=1 wkPk = P and also wσ = w.
Therefore, w is a feasible population distribution given P.
H
PROOF OF THEOREM 4.4
Consider any w ∈W(P). Then, there exists (P1, . . . , PM) ∈PM such that P = PM
k=1 wk Pk. Fix
an index i ∈[M]. For any y ∈Y \ {yi}, we have
P(yi ≻y) = wi Pi(yi ≻y) +
X
k̸=i
wk Pk(yi ≻y) ≥wi
(29)
since Pi(yi ≻y) = 1. Taking the minimum over y ∈Y \ {yi} yields
min
y∈Y\{yi} P(yi ≻y) ≥wi,
(30)
which implies wi ≤ui ∀i ∈[M] and w ∈W(P). Therefore, W(P) ⊆W(P).
I
ADDITIONAL REMARKS ON THE TIGHTNESS OF THE OUTER
APPROXIMATION
The gap between the true feasible set W(P) and its outer approximation W(P) arises from our
profile assumption, namely that each evaluator has a strict and complete ranking. To illustrate this
point, we show that W(P) provides a tight approximation (i.e., W(P) = W(P)) under an extended
profile setting. Consider an extended profile setting in which each group Gk is allowed to provide
pairwise comparison data according to its own preference function Pk, subject only to the skew-
symmetry constraint Pk(yi ≻yj)+Pk(yj ≻yi) = 1 for all yi, yj ∈Y, and the unanimity constraint
Pk(yk ≻y) = 1 for all y ∈Y. In this case, the set P is defined as
P := {P | P(y ≻y′) + P(y′ ≻y) = 1 ∀y, y′ ∈Y} .
(31)
We show that W(P) ⊆W(P) also holds under this setting. Consider any w ∈W(P). By assumption,
w satisfies wi ≤ui = miny∈Y\{yi} P(yi ≻y) for all i ∈[M]. Define each element of (P1, . . . , PM)
as
Pk(yi ≻yj) = P(yi ≻yj) −wi
1 −wi −wj
(32)
for any i, j ̸= k, and let Pk(yk ≻y) = 1, Pk(y ≻yk) = 0 for all y ∈Y. Then Pk(yi ≻yj) ∈
[0, 1] holds because P(yi ≻yj) ∈[wi, 1 −wj] by assumption. The skew-symmetry condition
Pk(yi ≻yj) + Pk(yj ≻yi) = 1 is also satisfied. Thus, Pk ∈P and Pk can be induced by some
profile. Finally, the constraint P = PM
k=1 wkPk also holds. Therefore, w ∈W(P), implying
W(P) ⊆W(P), and hence W(P) = W(P).
J
CONNECTION OF THEOREM 4.4 AND TATLI ET AL. (2024)
Tatli et al. (2024) studies the recovery of population preference distributions under a spatial model.
In their framework, each alternative is represented by a feature vector in a Euclidean space, and each
voter’s preferences are determined by distances to these vectors (i.e., voters prefer alternatives that are
19


Page 20:
Published as a conference paper at ICLR 2026
closer in the Euclidean norm). Theorem 4.4 can also be derived in this setting. Specifically, consider
a sufficiently high-dimensional feature space partitioned into M! regions by
 M
2

hyperplanes, where
each hyperplane is the perpendicular bisector of the line segment connecting a pair of alternative
vectors. Then, (Tatli et al., 2024, Proposition 2) shows that it is impossible to recover the full profile
σ from aggregated pairwise comparison data Pσ. Moreover, by summing the inequality in (Tatli et al.,
2024, Proposition 4) over the regions corresponding to voters who most prefer each alternative yi, we
obtain the bound wi ≤ui.
K
IMPOSSIBILITY OF A UNIFORM GUARANTEE α(σ) > 2/M
Proposition K.1. No PSCF can be implemented by a preference–learning algorithm while guaran-
teeing α-PPA with a constant α(σ) > 2/M for all σ ∈∆(S).
Proof. Consider any setting in which the pairwise comparison data are completely uninformative.
Specifically, suppose that for every pair of alternatives yi, yj, the observed probability satisfies
P(yi ≻yj) = 0.5. Under such maximally ambiguous data, no preference–learning algorithm can
distinguish among alternatives, and any algorithm that aims to maximize the worst-case α(σ) must
output the uniform distribution over the M alternatives.
However, the true distribution of evaluators’ top choices may in fact be highly non-uniform while
remaining perfectly consistent with the uninformative pairwise data. For example, consider a profile
σ in which wσ = [1/2, 1/(2M −2), 1/(2M −2), . . . , 1/(2M −2)], corresponding to a situation
where y1 is ranked first by half of the evaluators and ranked last by the other half. In this case, the
corresponding proportionality guarantee is α(σ) = 2/M. Therefore, achieving a uniform lower
bound α(σ) > 2/M for all σ ∈∆(S) is impossible.
L
PROOF OF THEOREM 4.6
We first prove monotonicity. Improving the ranking of yi for some evaluator can only increase
Pσ(yi ≻y) for any y ̸= yi, and decrease Pσ(y ≻yi). This implies that ui cannot decrease, while
uj for j ̸= i cannot increase. Therefore, π(yi) = ui/(PM
j=1 uj) cannot decrease, establishing
monotonicity.
Next, we prove Pareto efficiency. Suppose yi is ranked above yj in every input ranking, i.e.,
r(yi) < r(yj) for all r ∈S with σr > 0. Then, we have Pσ(yi ≻yj) = P
r∈S σr·1{r(yi)<r(yj)} = 1
and also Pσ(yj ≻yi) = 0. Thus, we get uj = miny∈Y \{yj} Pσ(yj ≻y) = 0. Thus, the resulting
policy satisfies Φ∗(σ)(yj) = uj/(PM
k=1 uk) = 0. Therefore, Φ∗(σ)(yi) ≥Φ∗(σ)(yj), establishing
that Φ∗satisfies Pareto efficiency.
M
PROOF OF LEMMA 4.7 AND LEMMA 4.9
Lemma 4.7 follows directly from the fact that wσ
i ≤ui for all i ∈[M], which gives
π(yi)
wσ
i
=
ui
wσ
i
PM
j=1 uj
≥
1
PM
j=1 uj
.
(33)
Next, we show Lemma 4.9. Let I ⊆[M] be the set of indexes for δ-dominated alternatives, where
|I| = M −N σ
δ . Then, for any i ∈I, we have
ui =
min
j∈[M]\{i} Pσ(yi ≻yj) ≤Pσ(yi ≻y′
i) ≤1 −δ,
(34)
where y′
i denotes an alternative that δ-dominates yi. Additionally, let k ∈arg maxi∈[M] wσ
i . Then,
for any i ̸= k, we have
ui =
min
j∈[M]\{i} Pσ(yi ≻yj) ≤Pσ(yi ≻yk) ≤1 −wσ
k.
(35)
20


Page 21:
Published as a conference paper at ICLR 2026
Similarly, let l ∈arg maxi∈[M],i̸=k wσ
i , then we have uk ≤1 −wσ
l . Combining these results,
M
X
i=1
ui = uk +
X
i̸=k,i/∈I
ui +
X
i∈I
ui ≤(1 −wσ
l ) + (N σ
δ −1)(1 −wσ
k) + (M −N σ
δ )(1 −δ). (36)
In addition, since ui ≥wσ
i , we have PM
i=1 ui ≥PM
i=1 wσ
i = 1. Combining both inequalities and
plugging (wσ
k, wσ
l ) = (wσ,1, wσ,2) in, we get the result of Lemma 4.9 as follows:
 M
X
i=1
ui
!−1
∈

1
(N σ
δ −1)(1 −wσ,1) + (1 −wσ,2) + (M −N σ
δ )(1 −δ), 1

.
(37)
N
ADDITIONAL BOUND ANALYSIS UNDER A RANDOM-RANKING MODEL
In this appendix, we provide additional analysis of the lower bounds in Lemma 4.7 and Lemma 4.9
under a random-ranking model. Our objective is to evaluate whether these guarantees remain
meaningful under realistic levels of heterogeneity in the underlying ranking distributions.
Setup.
We construct a base ranking by sampling latent rewards for each of the M alternatives
independently from N(0, 1). The rankings of N = 1000 evaluators are then generated by adding
independent Gaussian noise from N(0, 1) to these rewards and sorting the alternatives according to
the perturbed values. This procedure induces a ranking distribution with substantial dispersion. For
instance, when M = 20, the largest population share maxk∈[20] wσ
k averages approximately 0.25,
indicating that the distribution is far from concentrated on a single ranking.
Results.
Table 3 reports the average values of the two lower bounds, (PM
i=1 ui)−1 and α(σ), over
10 independent runs for different values of M, with δ = 0.7 fixed. In all cases, both bounds are
substantially stronger than the naive baseline of 1/M, corresponding to the uniform policy. These
findings suggest that the theoretical guarantees remain nontrivial in empirically relevant regimes.
Table 3: Average lower bounds under the random-ranking model.
M
10
20
50
100
PM
i=1 ui
−1
0.5553
0.3360
0.2085
0.1427
α(σ)
0.2539
0.1254
0.0570
0.0305
O
PROOF OF THEOREM 4.11
Let σ′ be the profile manipulated by group Gk, and let π′ = Φ∗(σ′) be the resulting policy. Gk aims
to maximize
π′(yk) =
u′
k
u′
k + P
i̸=k u′
i
,
(38)
where u′ represents the value of u after the manipulation. To maximize π′(yk), Gk will attempt to
maximize u′
k and minimize P
i̸=k u′
i. Since increasing the ranking of yk in their profile increases
(or at least does not decrease) the value of u′
k without increasing the value of P
i̸=k u′
i, the optimal
strategy for Gk is to truthfully report yk as its top choice. In this strategy, we have u′
k = uk and the
sum P
i̸=k u′
i has the following lower bound:
X
i̸=k
u′
i ≥
X
i̸=k
wσ
i = 1 −wσ
k.
(39)
Substituting this lower bound into equation 38, we obtain
π′(yk) ≤
uk
uk + 1 −wσ
k
≤1
2(wσ
k + 1),
(40)
where the final inequality holds if (wσ
k −uk + 1)(wσ
k −1) ≤0, which follows from the fact that
wσ
k, uk ∈[0, 1].
21


Page 22:
Published as a conference paper at ICLR 2026
P
WEAK STRATEGYPROOFNESS GUARANTEE
In social choice theory, a mechanism is considered strategyproof if participants cannot benefit (i.e.,
increase their utility) by misreporting their true preferences (Gibbard, 1973), regardless of what other
participants report. In our preference learning framework, we assume each group Gk’s utility is
the probability assigned to its top choice, represented by π(yk). A preference learning algorithm is
strategyproof if no participant can improve its outcome by misreporting preferences. However, as
noted by Buening et al. (2025), strict strategyproofness is typically too restrictive and is not satisfied
by the conventional preference learning algorithms (with ex-post efficiency). Our method does not
satisfy strict strategyproofness like other methods, but satisfies a weaker form that provides a bounded
guarantee on the maximum potential gain from strategic misreporting in equilibrium.
Let σ′ denote the profile resulting from strategical misreporting by all groups, and let π′ = Φ∗(σ′)
be the resulting policy. Each group Gk aims to maximize π′(yk), which involves maximizing u′
k and
minimizing P
i̸=k u′
i.
Since improving the ranking of yk in their reported preferences increases (or at worst, does not
decrease) the value of u′
k without increasing P
i̸=k u′
i, the optimal strategy for Gk is to truthfully
report yk as their top choice. Hence, all groups truthfully report their top choice regardless of
other groups’ strategies, meaning P′
k(yk ≻y) = 1 for all y ̸= yk, where P′
k denotes the reported
preference function of Gk.
In this equilibrium, following steps analogous to the proof of Theorem 4.11, we have:
π′(yk) ≤
u′
k
u′
k + 1 −wσ
k
≤1
2(wσ
k + 1)
∀k ∈[M].
(41)
Note that γ(wσ
k) is not a tight bound. Further exploration into tighter bounds and detailed analysis of
each group’s strategic behavior is left for future research.
Q
PROOF OF PROPOSITION 4.13
Suppose M = 2 and Pσ(y1 ≻y2) ∈(0.5, 1), so y1 is the Condorcet winner. If a PSCF Φ satisfies
Condorcet consistency, it must return the deterministic policy π(y1) = 1. However, this violates the
α-PPA axiom because π(y2) = 0 while wσ
2 > 0, which implies that π(y2)/wσ
2 = 0 cannot be lower
bounded by any α(σ) > 0.
R
PROOF OF PROPOSITION 4.14
Suppose yi is a Condorcet winner. Then Pσ(yi ≻yj) > 0.5 for all j ̸= i, which implies that
ui > 0.5. For any other j ̸= i, we have uj ≤Pσ(yj ≻yi) < 0.5. Therefore, yi has the highest ui,
i.e., i ∈arg maxj∈[M] uj, and Φ∞returns π(yi) = 1, satisfying Condorcet consistency.
S
FINITE BEHAVIOR OF Φβ
The following proposition quantifies how large the parameter β needs to be to ensure that a Condorcet
winner receives a sufficiently high probability under the softmax policy.
Proposition S.1 (Condorcet consistency at finite β). Let yi be a Condorcet winner with ui > 0.5.
Then, the softmax policy satisfies π(yi) ≥αc if
β ≥
1
ui −0.5 log
(M −1)αc
2(1 −αc)

.
(42)
Proof. Since yi is a Condorcet winner, we have uj ≤Pσ(yj ≻yi) = 1 −Pσ(yi ≻yj) < 0.5 for
any j ̸= i. From the given condition
β ≥
1
ui −0.5 log
(M −1)αc
2(1 −αc)

,
(43)
22


Page 23:
Published as a conference paper at ICLR 2026
we can establish the following lower bound:
ui exp (βui) ≥
αc
1 −αc
(M −1)(0.5 exp (0.5β)) ≥
αc
1 −αc
X
j̸=i
uj exp (βuj).
(44)
Thus, the softmax policy satisfies
π(yi) =
ui exp (βui)
ui exp (βui) + P
j̸=i uj exp (βuj) ≥αc.
(45)
In addition, it can be shown that the α-PPA guarantee deteriorates as β →∞, since the lower bound
in Lemma 4.7 becomes
π(yi)
wσ
i
≥


M
X
j=1
uj exp (β(uj −ui))


−1
,
(46)
which converges to zero as β →∞, unless ui = maxj∈[M] uj.
T
CONNECTION TO PAIRWISE MAJORITY CONSISTENCY (PMC)
We discuss the connection to pairwise majority consistency (PMC) (Ge et al., 2024), which imposes a
stronger consistency requirement, ensuring the entire policy ranking aligns with majority preferences.
Definition T.1 (Pairwise majority consistent ranking (PMC ranking)). A ranking rσ is a called a
PMC ranking of a profile σ if for all yi, yj ∈Y, a majority of evaluators prefer alternative yi to
alternative yj in σ if and only if yi is ranked higher than yj in rσ. Formally, Pσ(yi ≻yj) > 1/2 if
and only if rσ(yi) < rσ(yj).
Definition T.2 (Pairwise majority consistency (PMC)). A PSCF Φ satisfies PMC if, for any profile
σ ∈∆(S) that has a PMC ranking rσ, Φ(σ) has the same ranking with rσ, i.e. Φ(σ)(yi) ≥Φ(σ)(yj)
if rσ(yi) < rσ(yj).
It can be shown that any Φβ with finite β ≥0 violates PMC, and only the limiting PSCF Φβ satisfies
PMC.
Proposition T.3. Any Φβ with finite β ≥0 violates PMC. Φ∞satisfies PMC.
Proof. First, we show that Φβ violates PMC for any β ≥0. It suffices to demonstrate that there
exists a profile σ with a PMC ranking rσ for which Φβ(σ)(yi) < Φβ(σ)(yj) while rσ(yi) < rσ(yj).
Consider the following profile σ with M = 3:
σ = {(y1 ≻y2 ≻y3)×0.3, (y2 ≻y3 ≻y1)×0.1, (y3 ≻y1 ≻y2)×0.3, (y3 ≻y2 ≻y1)×0.3},
(47)
which yields the following preference function:
Pσ =
"0.5
0.6
0.3
0.4
0.5
0.4
0.7
0.6
0.5
#
.
(48)
Then, the PMC ranking satisfies rσ(y3) < rσ(y1) < rσ(y2), as Pσ(y3 ≻y1), Pσ(y3 ≻
y2), Pσ(y1 ≻y2) > 0.5. However, we have u1 = 0.3 and u2 = 0.4. Since u1 < u2, it fol-
lows that Φβ(σ)(y1) < Φβ(σ)(y2) regardless of β, contradicting rσ(y1) < rσ(y2). Therefore, Φβ
violates PMC regardless of β.
Next, we show that Φ∞satisfies PMC. Consider a profile σ with its PMC ranking rσ, and let y∗∈Y
be the alternative ranked first in rσ (i.e., rσ(y∗) = 1). Then, y∗must be a Condorcet winner, as
Pσ(y∗≻y) > 1/2 for all y ̸= y∗. Thus, π := Φ∞(σ) is a deterministic policy with π(y∗) = 1.
Consequently, we have π(y∗) > π(y) for all y ̸= y∗and trivially π(yi) = π(yj) = 0 for any
yi, yj ̸= y∗, satisfying the condition for PMC.
Φβ approximately satisfies PMC as β →∞if we allow some slack in the rankings (e.g., Φ(σ)(yi) ≥
Φ(σ)(yj) −ϵ for some small ϵ > 0) in the definition of PMC. However, exploring this approximate
consistency is beyond the scope of this paper and is left for future research.
23


Page 24:
Published as a conference paper at ICLR 2026
U
ADDITIONAL DETAILS OF EXPERIMENTS
U.1
SYNTHETIC DATASET
Dataset generation.
For the synthetic dataset, we used 10 prompts and 10 responses for the color-
preference alignment task, as shown in Table 4. To construct the ground-truth profile σ, we sampled
the true (center) rewards independently from the normal distribution N(0, 1) for each response. We
then added i.i.d. random noise from N(0, 1) to each true reward to generate 1,000 independent
rankings. Finally, we drew 104 pairwise comparison samples i.i.d. from the true preference function
Pσ to train each algorithm.
Table 4: Prompts and responses in synthetic dataset
Prompt (x)
Response (y)
Which color do you find the most appealing?
Red
Which color best represents your personality?
Blue
When decorating your room, what color do you prefer?
Green
What is your favorite color?
Yellow
Which color do you like the most?
Purple
If you had to choose just one color, which would it be?
Orange
Among all colors, what’s your top pick?
Pink
If you could only wear one color forever, what would you choose?
Brown
What color makes you feel happiest?
Black
Which color do you prefer most?
White
Evaluation methods.
We evaluate the fine-tuned policy using two metrics: (i) win rate against a
reference policy (the pretrained model), E(x,y1,y2)∼(ρ,π,πref)[Pσ(y1 ≻y2 | x)], and (ii) the PPA level
α(σ). To estimate the fine-tuned policies over responses, we compute the logits of each response
and the softmax policy (with temperature 1). We then calculate the win rate and PPA level directly
from their definitions using the estimated policy for each prompt. The results are averaged over all
prompts.
U.2
ALPACA-GPT4 DATASET
Dataset generation.
We considered two groups of evaluators, defined across two categories:
expertise and style. For the expertise category, evaluators were grouped into two levels: ‘elementary
school student’ and ‘PhD student’. For the style category, evaluators were grouped into ‘friendly’
and ‘unfriendly’. The true population distribution was set to wσ = [0.8, 0.2]. For each of the 52k
instruction prompts from the Alpaca-GPT4 dataset (Peng et al., 2023), group-specific responses were
generated using GPT-4.1 with the prompts listed in Table 5. Then, the pairwise comparison samples
are drawn i.i.d. from Pσ.
Table 5: Prompts used for generating responses from each group
Category
Prompt
Expertise
(1) Generate a response that can be easily understood by an elementary school
student.
(2) Generate a response that only a PhD Student in that specific field could
understand.
Style
(1) Generate a response that is friendly, witty, funny, and humorous, like a close
friend.
(2) Generate a response that answers in an unfriendly manner.
Evaluation methods.
To estimate the fine-tuned policies over responses, we sample a response
from the policy and use the annotation model (GPT-4.1) to classify its group. Table 6 shows the
24


Page 25:
Published as a conference paper at ICLR 2026
prompts used to classify the group of generated responses. Based on these classifications, we evaluate
the policy’s win rate and the PPA level from their definitions.
Table 6: Prompts used for classification
Category
Prompt
Expertise
Does the expertise level of this response align more closely with the elementary
level or the PhD student level? Please answer with only one of these exact
options: ‘elementary’ or ‘PhD’.
Style
Is this response friendly or unfriendly? Please answer with only one of these
exact options: ‘friendly’ or ‘unfriendly’.
U.3
HYPERPARAMETER SETTING
The Qwen2.5-3B-Instruct model (Yang et al., 2024) was fine-tuned using each algorithm, where both
the reference policy πref and the data sampling policy πd were set to the same pretrained model.
All algorithms were trained on the same offline dataset for the same number of iterations. NLHF
was not included in the comparison, as the algorithm does not support offline learning. Specific
training hyperparameters are provided in Table 7. Each training run utilized one H100 GPU, requiring
approximately 0.5–1 hour per epoch with about 20–40GB of memory usage using LoRA.
Table 7: Training hyperparameters
Hyperparameter
Synthetic
Alpaca-GPT4
Training & Reference Model
Qwen2.5-3B-Instruct
Qwen2.5-3B-Instruct
Learning Rate
1e-4
1e-5
Batch Size
8
4
Epochs
3
1
Optimizer
AdamW
AdamW
Gradient Clipping
1.0
1.0
Learning Rate Scheduler
Linear
Linear
Warmup Steps
100
100
KL Coefficient
0.1
0.01
LoRA Rank
32
32
LoRA α
32
32
V
SCALABLE OFFLINE ALGORITHM WITH FUNCTION APPROXIMATION
V.1
OFFLINE PAIRWISE COMPARISON DATASET
In practical applications of preference learning, the preference function often depends on additional
context or state, denoted by x ∈X. For instance, in LLMs, x represents the input prompt or conver-
sational history that provides the specific context for generating a preferred response. Accordingly,
we define the context-dependent preference function as P(· ≻· | ·) : Y2 × X →[0, 1], which is
unknown and must be estimated from empirical data. We consider an offline dataset of pairwise
comparisons D = {(xi, yw
i , yl
i)}N
i=1, where yw
i is preferred over yl
i under context xi. Each query is
assumed to be drawn i.i.d. from a joint distribution of ρ(x) and πd(y | x), and labeled according to
the preference function P. Our goal is to use this offline dataset to learn a policy π : X 7→∆(Y)
following the framework introduced in the previous sections.
25


Page 26:
Published as a conference paper at ICLR 2026
V.2
TWO-PHASE OFFLINE PREFERENCE LEARNING ALGORITHM
We approximate a softmax policy proposed in Section 4.3:
π(y | x) :=
u(y | x) exp(βu(y | x))
P
y∈Y u(y | x) exp(βu(y | x)),
where
u(y | x) := min
z∈Y P(y ≻z | x).
(49)
Specifically, we use a two-phase algorithm that first estimates u and then estimates π based on u.
Phase 1: Estimating u.
To estimate u, we first train the selector model µ using the following loss
function, the offline dataset D, and the parameterized function class Fµ:
ˆµ ∈arg min
µ∈Fµ
1
N
N
X
i=1
µ(yl
i | xi, yw
i )
πd(yl
i | xi) .
(50)
Then, the estimated ˆu can be obtained from ˆu(y | x) = P
z∈Y ˆP(y ≻z | x)ˆµ(z | x, y), where ˆP
denotes the empirical estimate of the preference function. The derivation of the loss function and the
relationship between µ and u are provided in Appendix W.
Phase 2: Estimating π.
Let ˆπβ be the normalized softmax policy constructed with ˆu follow-
ing equation 49. In the second phase, the policy model is trained by minimizing the distance to ˆπβ
over a function class Fπ:
ˆπ ∈arg min
π∈Fπ
Ex∼ρ
h
Lπ(π(· | x), ˆπβ(· | x))
i
.
(51)
Here, Lπ denotes a divergence or distance metric between two policies. In our experiments, we
employ the KL divergence for Lπ. Specifically, substituting the KL divergence into Lπ from
equation 51, the loss function becomes
Ex∼ρ
"
DKL
 
π(· | x)

X
z∈Y
ˆP(· ≻z | x)ˆµ(z | x, ·)
!#
= E(x,y)∼(ρ,πd)
"
π(y | x)
πd(y | x) log
π(y | x)
P
z∈Y ˆP(y ≻z | x)ˆµ(z | x, y)
#
.
(52)
Using the offline dataset and function approximation, we obtain
ˆπ ∈arg min
π∈Fπ
E(x,yw,yl)∼D
"
π(yw | x)
πd(yw | x) log
π(yw | x)
( 1
2 + 1
2 ˆµ(yw | x, yl)) exp ( β
2 + β
2 ˆµ(yw | x, yl))
+ π(yl | x)
πd(yl | x) log
π(yl | x)
( 1
2 −1
2 ˆµ(yl | x, yw)) exp ( β
2 −β
2 ˆµ(yw | x, yl))
#
.
(53)
V.3
ADDITIONAL TECHNIQUES FOR LLM FINE-TUNING
Regularization via reference policy.
Fine-tuning large language models (LLMs) requires main-
taining alignment with a reference policy, typically the pretrained model. To prevent excessive drift,
we incorporate KL-divergence regularization terms into the training objectives for both the selector
model µ and the policy model π. Specifically, we add the following regularization terms to the loss
functions in Phase 1 and Phase 2:
βµE(x,y)∼(ρ,πd)

DKL

µ(· | x, y)
πref(· | x, y)

,
βπEx∼ρ

DKL

π(· | x)
πref(· | x)

(54)
Training with single model.
To reduce computational cost, we propose to train both µ and π using
a single model. This is enabled by encoding structural differences through specialized input formats.
Specifically, π( · | x) selects preferred responses given a prompt, while µ( · | x, y) selects responses
given a prompt and a candidate response. By distinguishing these cases with separator tokens, we
achieve performance comparable to training separate models, while improving memory usage and
training efficiency.
26


Page 27:
Published as a conference paper at ICLR 2026
W
DERIVATION OF THE LOSS FUNCTION IN PHASE 1
Step 1: LP reformulation.
Recall the definition u(y | x) := minz∈Y\{y} P(y ≻z | x). Each
u(y | x) can be rewritten as
u(y | x) =
X
z∈Y
P(y ≻z | x)µ∗(z | x, y),
(55)
where a selector distribution µ∗( · | x, y) ∈∆(Y) places all its mass on the minimizer of P(y ≻
· | x). Such µ∗and the corresponding pointwise minimum can be obtained via the following linear
programming (LP):
u(y | x) =
min
µ(·|x,y)∈∆(Y)
X
z∈Y
P(y ≻z | x)µ(z | x, y).
(56)
Step 2: Aggregation of pointwise LPs.
Assume the data-generating distribution ρ(·) and πd( · | x)
have full support. Multiplying and dividing equation 56 by πd(z | x) and then taking the expectation
over all z ∈Y gives
u(y | x) =
min
µ(·|x,y)∈∆(Y) Ez∼πd(·|x)
P(y ≻z | x)µ(z | x, y)
πd(z | x)

.
(57)
Next, we aggregate these pointwise LPs by multiplying each pointwise objective by ρ(x)πd(y | x)
and summing over all (x, y) ∈X × Y. We also add the symmetrical term with swapped y and z,
which does not change the optimal solution:
µ∗∈
arg min
µ:X×Y7→∆(Y)
E(x,y,z)∼(ρ,πd,πd)
P(y ≻z | x)µ(z | x, y)
πd(z | x)
+ P(z ≻y | x)µ(y | x, z)
πd(y | x)

. (58)
Step 3: Empirical counterpart.
Given an offline preference dataset D, we approximate the expec-
tation in equation 58 using its empirical counterpart and restrict the function class to a parameterized
family Fµ:
ˆµ ∈arg min
µ∈Fµ
1
N
N
X
i=1
µ(yl
i | xi, yw
i )
πd(yl
i | xi) .
(59)
Given the estimate ˆµ, we can estimate ˆu using equation 56 with the estimated preference function ˆP:
ˆP(y ≻z | x) :=
(
N(x,y,z)
N(x,y,z)+N(x,z,y)
if N(x, y, z) + N(x, z, y) > 0,
1/2,
otherwise,
(60)
where N(x, y, z) := |{i ∈[N] | (xi, yw
i , yl
i) = (x, y, z)}|.
27

