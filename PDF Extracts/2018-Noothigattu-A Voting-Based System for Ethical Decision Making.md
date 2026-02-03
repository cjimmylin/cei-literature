---
title: "A Voting-Based System for Ethical Decision Making - PDF Extract"
source_pdf: "2018-Noothigattu-A Voting-Based System for Ethical Decision Making.pdf"
pages: 25
extracted_at: "2026-01-24T17:05:07.204226"
---

# PDF Extract: A Voting-Based System for Ethical Decision Making

**Source PDF:** 2018-Noothigattu-A Voting-Based System for Ethical Decision Making.pdf
**Total Pages:** 25

---

## Content

```
--- Page 1 ---

A Voting-Based System for Ethical Decision Making
Ritesh Noothigattu1, Snehalkumar ‘Neil’ S. Gaikwad2, Edmond Awad2, Sohan Dsouza2,
Iyad Rahwan2, Pradeep Ravikumar1, and Ariel D. Procaccia1
1School of Computer Science, Carnegie Mellon University
2The Media Lab, Massachusetts Institute of Technology
Abstract
We present a general approach to automating ethical decisions, drawing on machine learning
and computational social choice. In a nutshell, we propose to learn a model of societal prefer-
ences, and, when faced with a speciﬁc ethical dilemma at runtime, eﬃciently aggregate those
preferences to identify a desirable choice. We provide a concrete algorithm that instantiates our
approach; some of its crucial steps are informed by a new theory of swap-dominance eﬃcient
voting rules. Finally, we implement and evaluate a system for ethical decision making in the
autonomous vehicle domain, using preference data collected from 1.3 million people through the
Moral Machine website.
1
Introduction
The problem of ethical decision making, which has long been a grand challenge for AI [23], has
recently caught the public imagination. Perhaps its best-known manifestation is a modern variant of
the classic trolley problem [10]: An autonomous vehicle has a brake failure, leading to an accident
with inevitably tragic consequences; due to the vehicle’s superior perception and computation
capabilities, it can make an informed decision. Should it stay its course and hit a wall, killing its
three passengers, one of whom is a young girl? Or swerve and kill a male athlete and his dog, who
are crossing the street on a red light? A notable paper by Bonnefon et al. [2] has shed some light
on how people address such questions, and even former US President Barack Obama has weighed
in.1
Arguably the main obstacle to automating ethical decisions is the lack of a formal speciﬁcation
of ground-truth ethical principles, which have been the subject of debate for centuries among
ethicists and moral philosophers [20, 24]. In their work on fairness in machine learning, Dwork
et al. [7] concede that, when ground-truth ethical principles are not available, we must use an
“approximation as agreed upon by society.” But how can society agree on the ground truth — or
an approximation thereof — when even ethicists cannot?
We submit that decision making can, in fact, be automated, even in the absence of such ground-
truth principles, by aggregating people’s opinions on ethical dilemmas. This view is foreshadowed
by recent position papers by Greene et al. [9] and Conitzer et al. [6], who suggest that the ﬁeld of
computational social choice [3], which deals with algorithms for aggregating individual preferences
1https://www.wired.com/2016/10/president-obama-mit-joi-ito-interview/
1
arXiv:1709.06692v2  [cs.AI]  18 Dec 2018

--- Page 2 ---

towards collective decisions, may provide tools for ethical decision making. In particular, Conitzer
et al. raise the possibility of “letting our models of multiple people’s moral values vote over the
relevant alternatives.”
We take these ideas a step further by proposing and implementing a concrete approach for
ethical decision making based on computational social choice, which, we believe, is quite practical.
In addition to serving as a foundation for incorporating future ground-truth ethical and legal
principles, it could even provide crucial preliminary guidance on some of the questions faced by
ethicists. Our approach consists of four steps:
I Data collection: Ask human voters to compare pairs of alternatives (say a few dozen per
voter). In the autonomous vehicle domain, an alternative is determined by a vector of features
such as the number of victims and their gender, age, health — even species!
II Learning: Use the pairwise comparisons to learn a model of the preferences of each voter over
all possible alternatives.
III Summarization: Combine the individual models into a single model, which approximately
captures the collective preferences of all voters over all possible alternatives.
IV Aggregation: At runtime, when encountering an ethical dilemma involving a speciﬁc subset
of alternatives, use the summary model to deduce the preferences of all voters over this
particular subset, and apply a voting rule to aggregate these preferences into a collective
decision. In the autonomous vehicle domain, the selected alternative is the outcome that
society (as represented by the voters whose preferences were elicited in Step I) views as the
least catastrophic among the grim options the vehicle currently faces. Note that this step is
only applied when all other options have been exhausted, i.e., all technical ways of avoiding
the dilemma in the ﬁrst place have failed, and all legal constraints that may dictate what to
do have also failed.
For Step I, we note that it is possible to collect an adequate dataset through, say, Amazon
Mechanical Turk. But we actually perform this step on a much larger scale. Indeed, we use, for the
ﬁrst time, a unique dataset that consists of 18,254,285 pairwise comparisons between alternatives
in the autonomous vehicle domain, obtained from 1,303,778 voters, through the website Moral
Machine [1].2
Subsequent steps (namely Steps II, III, and IV) rely on having a model for preferences. There
is a considerable line of work on distributions over rankings over a ﬁnite set of alternatives. A
popular class of such models is the class of random utility models, which use random utilities for
alternatives to generate rankings over the alternatives. We require a slightly more general notion,
as we are interested in situations where the set of alternatives is inﬁnite, and any ﬁnite subset of
alternatives might be encountered (c.f. [5]). For example, there are uncountably many scenarios an
autonomous vehicle might face, because one can choose to model some features (such as the age
of, say, a passenger) as continuous, but at runtime the vehicle will face a ﬁnite number of options.
We refer to these generalized models as permutation processes.
In Section 4, we focus on developing a theory of aggregation of permutation processes, which
is crucial for Step IV. Speciﬁcally, we assume that societal preferences are represented as a single
2http://moralmachine.mit.edu
2

--- Page 3 ---

permutation process. Given a (ﬁnite) subset of alternatives, the permutation process induces a
distribution over rankings of these alternatives. In the spirit of distributional rank aggregation [19],
we view this distribution over rankings as an anonymous preference proﬁle, where the probability
of a ranking is the fraction of voters whose preferences are represented by that ranking.
This
means we can apply a voting rule in order to aggregate the preferences — but which voting rule
should we apply?
And how can we compute the outcome eﬃciently?
These are some of the
central questions in computational social choice, but we show that in our context, under rather
weak assumptions on the voting rule and permutation process, they are both moot, in the sense
that it is easy to identify alternatives chosen by any “reasonable” voting rule. In slightly more
detail, we deﬁne the notion of swap dominance between alternatives in a preference proﬁle, and
show that if the permutation process satisﬁes a natural property with respect to swap dominance
(standard permutation processes do), and the voting rule is swap-dominance eﬃcient (all common
voting rules are), then any alternative that swap dominates all other alternatives is an acceptable
outcome.
Armed with these theoretical developments, our task can be reduced to: learning a permu-
tation process for each voter (Step II); summarizing these individual processes into a single per-
mutation process that satisﬁes the required swap-dominance property (Step III); and using any
swap-dominance eﬃcient voting rule, which is computationally eﬃcient given the swap-dominance
property (Step IV).
In Section 5, we present a concrete algorithm that instantiates our approach, for a speciﬁc
permutation process, namely the Thurstone-Mosteller (TM) Process [22, 15], and with a speciﬁc
linear parametrization of its underlying utility process in terms of the alternative features. While
these simple choices have been made to illustrate the framework, we note that, in principle, the
framework can be instantiated with more general and complex permutation processes.
Finally, in Section 6, we implement and evaluate our algorithm. We ﬁrst present simulation re-
sults from synthetic data that validate the accuracy of its learning and summarization components.
More importantly, we implement our algorithm on the aforementioned Moral Machine dataset, and
empirically evaluate the resultant system for choosing among alternatives in the autonomous vehicle
domain. Taken together, these results suggest that our approach, and the algorithmic instantiation
thereof, provide a computationally and statistically attractive method for ethical decision making.
2
Related Work
To our knowledge, the ﬁrst to connect computational social choice and ethical decision making are
Greene et al. [9]. In their position paper, they raise the possibility of modeling ethical principles
as the preferences of a ‘dummy’ agent that is part of a larger system, and ask whether diﬀerent
formalisms should be used to model individual and collective ethical principles. They also note that
there is work on collective decision making subject to feasibility constraints, but ethical principles
are too complex to be simply speciﬁed as a set of feasibility constraints.
A more recent position paper about ethical decision making in AI, by Conitzer et al. [6], discusses
a number of diﬀerent frameworks, and, in particular, touches upon game-theoretic models, social
choice, and machine learning. They point out that “aggregating the moral views of multiple humans
(through a combination of machine learning and social-choice theoretic techniques) may result in a
morally better system than that of any individual human, for example because idiosyncratic moral
mistakes made by individual humans are washed out in the aggregate.” Also relevant to our work
3

--- Page 4 ---

is their discussion of the representation of dilemmas by their key moral features, for the purposes
of applying machine learning algorithms.
Our paper is most closely related to parallel work by Freedman et al. [8], who introduce a
framework for prioritizing patients in kidney exchange. Speciﬁcally, they collected preferences over
8 simpliﬁed patient types from 289 workers on Amazon Mechanical Turk, and used them to learn
societal weights for these eight types. Roughly speaking, the weights are such that if a random
person was asked to compare two patient types, the probability she would prefer one to the other
is proportional to its weight. These weights are then used to break ties among multiple outcomes
that maximize the number of matched patients (ties are broken according to the sum of weights
of matched patients). In contrast to our approach, there is no explicit preference aggregation, and
voting does not take place. In addition, their approach is speciﬁc to kidney exchange. Arguably the
main limitation of their approach is the use of weights that induce pairwise comparison probabilities
as weights that represent societal beneﬁt from matching a patient.3
Nonetheless, the work of
Freedman et al. serves as another compelling proof of concept (in a diﬀerent domain), providing
additional evidence that ethical decisions can be automated through computational social choice
and machine learning.
Finally, recall that the massive dataset we use for Step I comes from the Moral Machine website;
the conference version of our paper [17] is the ﬁrst publication to use this dataset.
However,
the original purpose of the website was to understand how people make ethical decisions in the
autonomous vehicle domain; the results of this experiment are presented in a recently published
paper [1]. The starting point of our work was the realization that the Moral Machine dataset can
be used not just to understand people, but also to automate decisions.
3
Preliminaries
Let X denote a potentially inﬁnite set of alternatives. Given a ﬁnite subset A ⊆X, we are interested
in the set SA of rankings over A. Such a ranking σ ∈SA can be interpreted as mapping alternatives
to their positions, i.e., σ(a) is the position of a ∈A (smaller is more preferred). Let a ≻σ b denote
that a is preferred to b in σ, that is, σ(a) < σ(b). For σ ∈SA and B ⊆A, let σ|B denote the
ranking σ restricted to B. And for a distribution P over SA and B ⊆A, deﬁne P|B in the natural
way to be the restriction of P to B, i.e., for all σ′ ∈SB,
P|B(σ′) =
X
σ∈SA: σ|B=σ′
P(σ).
A permutation process {Π(A) : A ⊆X, |A| ∈N} is a collection of distributions over SA for every
ﬁnite subset of alternatives A. We say that a permutation process is consistent if Π(A)|B = Π(B)
for any ﬁnite subsets of alternatives B ⊆A ⊆X. In other words, for a consistent permutation
process Π, the distribution induced by Π over rankings of the alternatives in B is nothing but
the distribution obtained by marginalizing out the extra alternatives A \ B from the distribution
induced by Π over rankings of the alternatives in A. This deﬁnition of consistency is closely related
to the Luce Choice Axiom [13].
A simple adaptation of folklore results [14] shows that any permutation process that is consistent
has a natural interpretation in terms of utilities. Speciﬁcally (and somewhat informally, to avoid
3For example, if, all else being equal, a young patient is preferred to an old patient with a probability of 0.9, it
does not mean that the societal value of the young patient is 9 times higher than that of the old patient.
4

--- Page 5 ---

introducing notation that will not be used later), given any consistent permutation process Π over
a set of alternatives X (such that |X| ≤ℵ1), there exists a stochastic process U (indexed by X)
such that for any A = {x1, . . . , xm} ⊆X, the probability of drawing σ ∈SA from Π(A) is equal
to the probability that sort(Ux1, Ux2, · · · , Uxm) = σ, where (perhaps obviously) sort(·) sorts the
utilities in non-increasing order. We can allow ties in utilities, as long as sort(·) is endowed with
some tie-breaking scheme, e.g., ties are broken lexicographically, which we will assume in the sequel.
We refer to the stochastic process corresponding to a consistent permutation process as its utility
process, since it is semantically meaningful to obtain a permutation via sorting by utility.
As examples of natural permutation processes, we adapt the deﬁnitions of two well-known
random utility models. The (relatively minor) diﬀerence is that random utility models deﬁne a
distribution over rankings over a ﬁxed, ﬁnite subset of alternatives, whereas permutation processes
deﬁne a distribution for each ﬁnite subset of alternatives, given a potentially inﬁnite space of
alternatives.
• Thurstone-Mosteller (TM) Process [22, 15]. A Thurstone-Mosteller Process (adaptation
of Thurstones Case V model) is a consistent permutation process, whose utility process U is
a Gaussian process with independent utilities and identical variances. In more detail, given
a ﬁnite set of alternatives {x1, x2, · · · , xm}, the utilities (Ux1, Ux2, · · · , Uxm) are independent,
and Uxi ∼N(µxi, 1
2), where µxi denotes the mode utility of alternative xi.
• Plackett-Luce (PL) Process [18, 13]. A Plackett-Luce Process is a consistent permutation
process with the following utility process U: Given a ﬁnite set of alternatives {x1, x2, · · · , xm},
the utilities (Ux1, Ux2, · · · , Uxm) are independent, and each Uxi has a Gumbel distribution
with identical scale, i.e. Uxi ∼G(µxi, γ), where G denotes the Gumbel distribution, and µxi
denotes the mode utility of alternative xi. We note that Caron and Teh [5] consider a further
Bayesian extension of the above PL process, with a Gamma process prior over the mode
utility parameters.
4
Aggregation of Permutation Processes
In social choice theory, a preference proﬁle is typically deﬁned as a collection σ = (σ1, . . . , σN)
of N rankings over a ﬁnite set of alternatives A, where σi represents the preferences of voter i.
However, when the identity of voters does not play a role, we can instead talk about an anonymous
preference proﬁle π ∈[0, 1]|A|!, where, for each σ ∈SA, π(σ) ∈[0, 1] is the fraction of voters whose
preferences are represented by the ranking σ. Equivalently, it is the probability that a voter drawn
uniformly at random from the population has the ranking σ.
How is this related to permutation processes?
Given a permutation process Π and a ﬁnite
subset A ⊆X, the distribution Π(A) over rankings of A can be seen as an anonymous preference
proﬁle π, where for σ ∈SA, π(σ) is the probability of σ in Π(A). As we shall see in Section 5, Step
II (learning) gives us a permutation process for each voter, where π(σ) represents our conﬁdence
that the preferences of the voter over A coincide with σ; and after Step III (summarization), we
obtain a single permutation process that represents societal preferences.
Our focus in this section is the aggregation of anonymous preference proﬁles induced by a
permutation process (Step IV), that is, the task of choosing the winning alternative(s). To this
end, let us deﬁne an anonymous social choice correspondence (SCC) as a function f that maps any
anonymous preference proﬁle π over any ﬁnite and nonempty subset A ⊆X to a nonempty subset
5

--- Page 6 ---

of A. For example, under the ubiquitous plurality correspondence, the set of selected alternatives
consists of alternatives with maximum ﬁrst-place votes, i.e., arg maxa∈A
P
σ∈SA: σ(a)=1 π(σ); and
under the Borda count correspondence, denoting |A| = m, each vote awards m −j points to the
alternative ranked in position j, that is, the set of selected alternatives is arg maxa∈A
Pm
j=1(m −
j) P
σ∈SA: σ(a)=j π(σ). We work with social choice correspondences instead of social choice functions,
which return a single alternative in A, in order to smoothly handle ties.
4.1
Eﬃcient Aggregation
Our main goal in this section is to address two related challenges.
First, which (anonymous)
social choice correspondence should we apply? There are many well-studied options, which satisfy
diﬀerent social choice axioms, and, in many cases, lead to completely diﬀerent outcomes on the
same preference proﬁle. Second, how can we apply it in a computationally eﬃcient way? This is
not an easy task because, in general, we would need to explicitly construct the whole anonymous
preference proﬁle Π(A), and then apply the SCC to it. The proﬁle Π(A) is of size |A|!, and hence
this approach is intractable for a large |A|. Moreover, in some cases (such as the TM process),
even computing the probability of a single ranking may be hard. The machinery we develop below
allows us to completely circumvent these obstacles.
Since stating our general main result requires some setup, we ﬁrst state a simpler instantiation of
the result for the speciﬁc TM and PL permutation processes (we will directly use this instantiation
in Section 5).
Before doing so, we recall a few classic social choice axioms.
We say that an
anonymous SCC f is monotonic if the following conditions hold:
1. If a ∈f(π), and π′ is obtained by pushing a upwards in the rankings, then a ∈f(π′).
2. If a ∈f(π) and b /∈f(π), and π′ is obtained by pushing a upwards in the rankings, then
b /∈f(π′).
In addition, an anonymous SCC is neutral if f(τ(π)) = τ(f(π)) for any anonymous preference
proﬁle π, and any permutation τ on the alternatives; that is, the SCC is symmetric with respect
to the alternatives (in the same way that anonymity can be interpreted as symmetry with respect
to voters).
Theorem 4.1. Let Π be the TM or PL process, let A ⊆X be a nonempty, ﬁnite subset of alter-
natives, and let a ∈arg maxx∈A µx. Moreover, let f be an anonymous SCC that is monotonic and
neutral. Then a ∈f(Π(A)).
To understand the implications of the theorem, we ﬁrst note that many of the common voting
rules, including plurality, Borda count (and, in fact, all positional scoring rules), Copeland, max-
imin, and Bucklin [3], are associated with anonymous, neutral, and monotonic SCCs. Speciﬁcally,
all of these rules have a notion of score, and the SCC simply selects all the alternatives tied for
the top score (typically there is only one).4 The theorem then implies that all of these rules would
agree that, given a subset of alternatives A, an alternative a ∈A with maximum mode utility is
an acceptable winner, i.e., it is at least tied for the highest score, if it is not the unique winner.
As we will see in Section 5, such an alternative is very easy to identify, which is why, in our view,
4Readers who are experts in social choice have probably noted that there are no social choice functions that are
both anonymous and neutral [16], intuitively because it is impossible to break ties in a neutral way. This is precisely
why we work with social choice correspondences.
6

--- Page 7 ---

Theorem 4.1 gives a satisfying solution to the challenges posed at the beginning of this subsection.
We emphasize that this is merely an instantiation of Theorem 4.7, which provides our result for
general permutation processes.
The rest of this subsection is devoted to building the conceptual framework, and stating and
proving the lemmas, required for the proof of Theorem 4.1, as well as to the statement and proof
of Theorem 4.7.
Starting oﬀ, let π denote an anonymous preference proﬁle (or distribution over rankings) over
alternatives A. We deﬁne the ranking σab as the ranking σ with alternatives a and b swapped, i.e.
σab(x) = σ(x) if x ∈A \ {a, b}, σab(b) = σ(a), and σab(a) = σ(b).
Deﬁnition 4.2. We say that alternative a ∈A swap-dominates alternative b ∈A in anonymous
preference proﬁle π over A — denoted by a ▷π b — if for every ranking σ ∈SA with a ≻σ b it holds
that π(σ) ≥π(σab).
In words, a swap-dominates b if every ranking that places a above b has at least as much weight
as the ranking obtained by swapping the positions of a and b, and keeping everything else ﬁxed.
This is a very strong dominance relation, and, in particular, implies existing dominance notions
such as position dominance [4]. Next we deﬁne a property of social choice correspondences, which
intuitively requires that the correspondence adhere to swap dominance relations, if they exist in a
given anonymous preference proﬁle.
Deﬁnition 4.3. An anonymous SCC f is said to be swap-dominance-eﬃcient (SwD-eﬃcient) if
for every anonymous preference proﬁle π and any two alternatives a and b, if a swap-dominates b
in π, then b ∈f(π) implies a ∈f(π).
Because swap-dominance is such a strong dominance relation, SwD-eﬃciency is a very weak
requirement, which is intuitively satisﬁed by almost any “reasonable” voting rule. This intuition is
formalized in the following lemma.
Lemma 4.4. Any anonymous SCC that satisﬁes monotonicity and neutrality is SwD-eﬃcient.
Proof. Let f be an anonymous SCC that satisﬁes monotonicity and neutrality. Let π be an arbitrary
anonymous preference proﬁle, and let a, b be two arbitrary alternatives such that a ▷π b. Now,
suppose for the sake of contradiction that b ∈f(π) but a /∈f(π).
Consider an arbitrary ranking σ with a ≻σ b. Since a ▷π b, π(σ) ≥π(σab). In other words, we
have an excess weight of π(σ)−π(σab) on σ. For this excess weight of σ, move b upwards and place
it just below a. By monotonicity, b still wins and a still loses in this modiﬁed proﬁle. We repeat
this procedure for every such σ (i.e. for its excess weight, move b upwards, until it is placed below
a). In the resulting proﬁle, a still loses. Now, for each of the modiﬁed rankings, move a down to
where b originally was. By monotonicity, a still loses in the resulting proﬁle π′, i.e., a /∈f(π′).
On the other hand, this procedure is equivalent to shifting the excess weight π(σ)−π(σab) from
σ to σab (for each σ with a ≻σ b). Hence, the proﬁle π′ we end up with is such that π′(σ) = π(σab)
and π′(σab) = π(σ), i.e. the new proﬁle is the original proﬁle with a and b swapped. Therefore, by
neutrality, it must be the case that a ∈f(π′). This contradicts our conclusion that a /∈f(π′), thus
completing the proof.
So far, we have deﬁned a property, SwD-eﬃciency, that any SCC might potentially satisfy. But
why is this useful in the context of aggregating permutation processes? We answer this question
in Theorem 4.7, but before stating it, we need to introduce the deﬁnition of a property that a
permutation process might satisfy.
7

--- Page 8 ---

Deﬁnition 4.5. Alternative a ∈X swap-dominates alternative b ∈X in the permutation process
Π — denoted by a ▷Π b — if for every ﬁnite set of alternatives A ⊆X such that {a, b} ⊆A, a
swap-dominates b in the anonymous preference proﬁle Π(A).
We recall that a total preorder is a binary relation that is transitive and total (and therefore
reﬂexive).
Deﬁnition 4.6. A permutation process Π over X is said to be SwD-compatible if the binary relation
▷Π is a total preorder on X.
We are now ready to state our main theorem.
Theorem 4.7. Let f be an SwD-eﬃcient anonymous SCC, and let Π be an SwD-compatible per-
mutation process. Then for any ﬁnite subset of alternatives A, there exists a ∈A such that a ▷Π b
for all b ∈A. Moreover, a ∈f(Π(A)).
Proof. Let f, Π, and A as in the theorem statement. Since Π is SwD-compatible, ▷Π is a total
preorder on X. In turn, the relation ▷Π restricted to A is a total preorder on A. Therefore, there
is a ∈A such that a ▷Π b for all b ∈A.
Suppose for the sake of contradiction that a /∈f(Π(A)), and let b ∈A \ {a}. Then it holds that
a ▷Π b. In particular, a ▷Π(A) b. But, because f is SwD-eﬃcient and a /∈f(Π(A)), we have that
b /∈f(Π(A)). This is true for every b ∈A, leading to f(Π(A)) = φ, which contradicts the deﬁnition
of an SCC.
Theorem 4.7 asserts that for any SwD-compatible permutation process, any SwD-eﬃcient SCC
(which, as noted above, include most natural SCCs, namely those that are monotonic and neutral),
given any ﬁnite set of alternatives, will always select a very natural winner that swap-dominates
other alternatives. A practical use of this theorem requires two things: to show that the permutation
process is SwD-compatible, and that it is computationally tractable to select an alternative that
swap-dominates other alternatives in a ﬁnite subset. The next few lemmas provide some general
recipes for establishing these properties for general permutation processes, and, in particular, we
show that they indeed hold under the TM and PL processes. First, we have the following deﬁnition.
Deﬁnition 4.8. Alternative a ∈X dominates alternative b ∈X in utility process U if for every
ﬁnite subset of alternatives containing a and b, {a, b, x3, . . . xm} ⊆X, and every vector of utilities
(u1, u2, u3 . . . um) ∈Rm with u1 ≥u2, it holds that
p(Ua,Ub,Ux3,...Uxm)(u1, u2, u3 . . . um) ≥p(Ua,Ub,Ux3,...Uxm)(u2, u1, u3 . . . um),
(1)
where p(Ua,Ub,Ux3,...Uxm) is the density function of the random vector (Ua, Ub, Ux3, . . . Uxm).
Building on this deﬁnition, Lemmas 4.9 and 4.10 directly imply that the TM and PL processes
are SwD-compatible.
Lemma 4.9. Let Π be a consistent permutation process, and let U be its corresponding utility
process. If alternative a dominates alternative b in U, then a swap-dominates b in Π.
Proof. Let a and b be two alternatives such that a dominates b in U. In addition, let A be a ﬁnite
set of alternatives containing a and b, let π denote the anonymous preference proﬁle Π(A), and
8

--- Page 9 ---

let m = |A|. Consider an arbitrary ranking σ such that a ≻σ b. Now, let xℓ= σ−1(ℓ) denote the
alternative in position ℓof σ, and let i = σ(a), j = σ(b), i.e.,
x1 ≻σ x2 · · · ≻σ xi(= a) ≻σ · · · ≻σ xj(= b) ≻σ · · · ≻σ xm.
Then,
π(σ) = P(Ux1 > Ux2 > · · · > Uxi > · · · > Uxj > · · · > Uxm)
=
Z ∞
−∞
Z u1
−∞
· · ·
Z ui−1
−∞
· · ·
Z uj−1
−∞
· · ·
Z um−1
−∞
p(u1, u2, · · · , ui, · · · uj, · · · , um)dum · · · du1.
In this integral, because of the limits, we always have ui ≥uj. Moreover, since xi = a dominates
xj = b in U, we have
π(σ) ≥
Z ∞
−∞
Z u1
−∞
· · ·
Z ui−1
−∞
· · ·
Z uj−1
−∞
· · ·
Z um−1
−∞
p(u1, u2, · · · , uj, · · · ui, · · · , um)dum · · · du1.
The right-hand side of this equation is exactly π(σab). Hence, we have π(σ) ≥π(σab). It follows
that a ▷π b, i.e., a ▷Π(A) b. Also, this is true for any ﬁnite A containing a and b. We conclude that
a ▷Π b.
Lemma 4.10. Under the TM and PL processes, alternative a dominates alternative b in the cor-
responding utility process if and only if µa ≥µb.
Proof. We establish the property separately for the TM and PL processes.
TM process. Let a and b be two alternatives such that µa ≥µb. Since we are dealing with a
TM process, Ua ∼N(µa, 1
2) and Ub ∼N(µb, 1
2). Let A be any ﬁnite set of alternatives containing
a and b. Since utilities are sampled independently in a TM process, the diﬀerence between the two
sides of Equation (1) is that the left-hand side has pUa(u1)pUb(u2), while the right-hand side has
pUa(u2)pUb(u1). It holds that
pUa(u1)pUb(u2)
=
1
√π exp
 −(u1 −µa)2 1
√π exp
 −(u2 −µb)2
.
= 1
π exp
 −u2
1 −µ2
a −u2
2 −µ2
b + 2u1µa + 2u2µb

.
(2)
We have u1 ≥u2 and µa ≥µb. Therefore,
u1µa + u2µb = u1µb + u1(µa −µb) + u2µb
≥u1µb + u2(µa −µb) + u2µb
= u1µb + u2µa
Substituting this into Equation (2), we obtain
pUa(u1)pUb(u2) ≥1
π exp
 −u2
1 −µ2
a −u2
2 −µ2
b + 2u1µb + 2u2µa

= 1
π exp
 −(u2 −µa)2 −(u1 −µb)2
9

--- Page 10 ---

= pUa(u2)pUb(u1)
It follows that Equation (1) holds true. Hence, a dominates b in the corresponding utility process.
To show the other direction, let a and b be such that µa < µb. If we choose u1, u2 such that
u1 > u2, using a very similar approach as above, we get pUa(u1)pUb(u2) < pUa(u2)pUb(u1). And so,
a does not dominate b in the corresponding utility process.
PL process. Let a and b be two alternatives such that µa ≥µb. Since we are dealing with a
PL process, Ua ∼G(µa, γ) and Ub ∼G(µb, γ). Let A be any ﬁnite set of alternatives containing a
and b. Since utilities are sampled independently in a PL process, the diﬀerence between the two
sides of Equation (1) is that the left-hand side has pUa(u1)pUb(u2), while the right-hand side has
pUa(u2)pUb(u1). It holds that
pUa(u1)pUb(u2) = 1
γ exp

−u1 −µa
γ
−e−u1−µa
γ
 1
γ exp

−u2 −µb
γ
−e−u2−µb
γ

= 1
γ2 exp

−u1 −µa
γ
−e−u1−µa
γ
−u2 −µb
γ
−e−u2−µb
γ

= 1
γ2 exp

−u1 −µa + u2 −µb
γ
−

e−u1
γ e
µa
γ + e−u2
γ e
µb
γ

.
(3)
We also know that e−u2
γ ≥e−u1
γ and e
µa
γ ≥e
µb
γ . Similar to the proof for the TM process, we have
e−u2
γ e
µa
γ + e−u1
γ e
µb
γ ≥e−u1
γ e
µa
γ + e−u2
γ e
µb
γ .
Substituting this into Equation (3), we obtain
pUa(u1)pUb(u2) ≥1
γ2 exp

−u1 −µa + u2 −µb
γ
−

e−u2
γ e
µa
γ + e−u1
γ e
µb
γ

= 1
γ exp

−u2 −µa
γ
−e−u2−µa
γ
 1
γ exp

−u1 −µb
γ
−e−u1−µb
γ

= pUa(u2)pUb(u1)
It follows that Equation (1) holds true. Hence, a dominates b in the corresponding utility process.
To show the other direction, let a and b be such that µa < µb. If we choose u1, u2 such that
u1 > u2, using a very similar approach as above, we get pUa(u1)pUb(u2) < pUa(u2)pUb(u1). And so,
a does not dominate b in the corresponding utility process.
The proof of Theorem 4.1 now follows directly.
Proof of Theorem 4.1. By Lemma 4.4, the anonymous SCC f is SwD-eﬃcient. Lemmas 4.9 and
4.10 directly imply that when Π is the TM or PL process, ▷Π is indeed a total preorder.
In
particular, a ▷Π b if µa ≥µb. So, an alternative a in A with maximum mode utility satisﬁes a ▷Π b
for all b ∈A. By Theorem 4.7, if a ∈A is such that a ▷Π b for all b ∈A, then a ∈f(Π(A)); the
statement of the theorem follows.
10

--- Page 11 ---

4.2
Stability
It turns out that the machinery developed for the proof of Theorem 4.1 can be leveraged to establish
an additional desirable property.
Deﬁnition 4.11. Given an anonymous SCC f, and a permutation process Π over X, we say that
the pair (Π, f) is stable if for any nonempty and ﬁnite subset of alternatives A ⊆X, and any
nonempty subset B ⊆A, f(Π(A)) ∩B = f(Π(B)) whenever f(Π(A)) ∩B ̸= φ.
Intuitively, stability means that applying f under the assumption that the set of alternatives
is A, and then reducing to its subset B, is the same as directly reducing to B and then applying
f.
This notion is related to classic axioms studied by Sen [21], speciﬁcally his expansion and
contraction properties. In our setting, stability seems especially desirable, as our algorithm would
potentially face decisions over many diﬀerent subsets of alternatives, and the absence of stability
may lead to glaringly inconsistent choices.
Our main result regarding stability is the following theorem.
Theorem 4.12. Let Π be the TM or PL process, and let f be the Borda count or Copeland SCC.
Then the pair (Π, f) is stable.
The Copeland SCC, which appears in the theorem statement, is deﬁned as follows. For an
anonymous preference proﬁle π over A, we say that a ∈A beats b ∈A in a pairwise election if
X
σ∈SA: a≻σb
π(σ) > 1
2.
The Copeland score of an alternative is the number of other alternatives it beats in pairwise elec-
tions; the Copeland SCC selects all alternatives that maximize the Copeland score.
The rest of the section is devoted to building intuition for, and proving, Theorem 4.12. Among
other things, the proof requires a stronger notion of SwD-eﬃciency, which, as we show, is satisﬁed
by Borda and Copeland. We will then be able to derive Theorem 4.12 as a corollary of the more
general Theorem 4.20. We start by examining some examples that illustrate stability (or the lack
thereof).
Example 4.13. Let f be the Borda count SCC, and let the set of alternatives be X = {u, v, w, x, y}.
Also, let Π be a consistent permutation process, which, given all the alternatives, gives a uniform
distribution on the two rankings (x ≻u ≻v ≻y ≻w) and (y ≻w ≻x ≻u ≻v). The outcome of
applying f on this proﬁle is {x} (since x has the strictly highest Borda score). But, the outcome
of applying f on the proﬁle Π({w, x, y}) is {y} (since y now has the strictly highest Borda score).
Hence, f(Π({u, v, w, x, y}))∩{w, x, y} ̸= f(Π(w, x, y)), even though the left-hand side is nonempty.
We conclude that the tuple (Π, f) does not satisfy stability.
Example 4.14. Consider the permutation process of Example 4.13, and let f be the Copeland
SCC. Once again, it holds that f(Π(u, v, w, x, y)) = {x} and f(Π(w, x, y)) = {y}. Hence the pair
(Π, f) is not stable.
Now, in the spirit of Theorem 4.7, let us see whether the pair (Π, f) satisﬁes stability when f is
an SwD-eﬃcient anonymous SCC, and Π is an SwD-compatible permutation process. Example 4.15
constructs such a Π that is not stable with respect to the plurality SCC (even though plurality is
SwD-eﬃcient).
11

--- Page 12 ---

Example 4.15. Let f be the plurality SCC and the set of alternatives be X = {a, b, c}. Also, let
Π be the consistent permutation process, which given all alternatives, gives the following proﬁle:
0.35 weight on (a ≻b ≻c), 0.35 weight on (b ≻a ≻c), 0.1 weight on (c ≻a ≻b), 0.1 weight on
(a ≻c ≻b) and 0.1 weight on (b ≻c ≻a). All the swap-dominance relations in this permutation
process are: a▷Π b, b▷Π c and a▷Π c. Hence, ▷Π is a total preorder on X, and Π is SwD-compatible.
Now, for this permutation process Π and the plurality SCC f, we have: f(Π({a, b, c})) = {a, b}
and f(Π({a, b})) = {a}. Therefore, (Π, f) is not stable.
This happens because Plurality is not strongly SwD-eﬃcient, as deﬁned below (Example 4.15
even shows why plurality violates this property).
Deﬁnition 4.16. An anonymous SCC f is said to be strongly SwD-eﬃcient if for every anonymous
preference proﬁle π over A, and any two alternatives a, b ∈A such that a ▷π b,
1. If b ⋫π a, then b /∈f(π).
2. If b ▷π a, then b ∈f(π) ⇔a ∈f(π).
It is clear that any strongly SwD-eﬃcient SCC is also SwD-eﬃcient.
Lemma 4.17. The Borda count and Copeland SCCs are strongly SwD-eﬃcient.
Proof. Let π be an arbitrary anonymous preference proﬁle over alternatives A, and let a, b ∈A
such that a ▷π b. This means that for all σ ∈SA with a ≻σ b, we have π(σ) ≥π(σab). We will
examine the two conditions (of Deﬁnition 4.16) separately.
Case 1: b ⋫π a.
This means that there exists a ranking σ∗∈SA with b ≻σ∗a such that
π(σ∗) < π(σab
∗). Below we analyze each of the SCCs mentioned in the theorem.
Borda count. SA can be partitioned into pairs of the form (σ, σab), where σ is such that a ≻σ b.
We reason about how each pair contributes to the Borda scores of a and b. Consider an arbitrary pair
(σ, σab) with a ≻σ b. The score contributed by σ to a is (m −σ(a))π(σ), and the score contributed
to b is (m −σ(b))π(σ). That is, it gives an excess score of (σ(b) −σ(a))π(σ) to a. Similarly, the
score of a contributed by σab is (m −σab(a))π(σab) = (m −σ(b))π(σab), and the score contributed
to b is (m −σ(a))π(σab). So, b gets an excess score of (σ(b) −σ(a))π(σab) from σab. Combining
these observations, the pair (σ, σab) gives a an excess score of (σ(b) −σ(a))(π(σ) −π(σab)), which
is at least 0. Since this is true for every pair (σ, σab), a has Borda score that is at least as high as
that of b. Furthermore, the pair (σab
∗, σ∗) is such that π(σab
∗) −π(σ∗) > 0, so, this pair gives a an
excess score that is strictly positive. We conclude that a has strictly higher Borda score than b,
hence b is not selected by Borda count.
Copeland. Let c ∈A\{a, b}. In a pairwise election between b and c, the total weight of rankings
that place b over c is
X
σ∈SA: b≻σc
π(σ) =
X
σ∈SA: (b≻σc)∧(a≻σc)
π(σ) +
X
σ∈SA: (b≻σc)∧(c≻σa)
π(σ).
For the rankings in the second summation (on the right-hand side), we have b ≻σ a by transitivity.
Hence, π(σ) ≤π(σab) for such rankings. Therefore,
X
σ∈SA: b≻σc
π(σ) ≤
X
σ∈SA: (b≻σc)∧(a≻σc)
π(σ) +
X
σ∈SA: (b≻σc)∧(c≻σa)
π(σab)
12

--- Page 13 ---

=
X
σ∈SA: (b≻σc)∧(a≻σc)
π(σ) +
X
σ′∈SA: (a≻σ′c)∧(c≻σ′b)
π(σ′)
=
X
σ∈SA: a≻σc
π(σ).
In summary, we have
X
σ∈SA: b≻σc
π(σ) ≤
X
σ∈SA: a≻σc
π(σ).
Hence, if b beats c in a pairwise competition, then so does a. Therefore, the Copeland score of a
(due to all alternatives other than a and b) is at least as high as that of b. Further, in a pairwise
competition between a and b, the weight of rankings that position a above b is P
σ∈SA: a≻σb π(σ)
and the weight of those that prefer b over a is P
σ∈SA: b≻σa π(σ). But, because π(σ) ≥π(σab) for
any σ with a ≻σ b, and π(σab
∗) > π(σ∗), a beats b. Therefore, a has a strictly higher Copeland
score than b, and b is not selected by Copeland.
Case 2: b▷πa. In this case, a▷πb and b▷πa. This means that for all σ ∈SA, we have π(σ) = π(σab).
In other words, τ(π) = π, where τ is the permutation that swaps a and b. Both Borda count and
Copeland are neutral SCCs. So, we have τ(f(π)) = f(τ(π)), which is in turn equal to f(π). Hence,
a is selected if and only if b is selected.
We conclude that both conditions of Deﬁnition 4.16 are satisﬁed by Borda count and Copeland.
Lemma 4.18. Let Π be a consistent permutation process that is SwD-compatible. Then, for any
ﬁnite subset of alternatives A ⊆X,
 ▷Π(A)

= (▷Π|A).
In words, as long as Π is consistent and SwD-compatible, marginalizing out some alternatives
from a proﬁle does not remove or add any swap-dominance relations.
Proof of Lemma 4.18. We ﬁrst show that for any B ⊆A ⊆X,
 ▷Π(A)|B

=
 ▷Π(B)

.
Let a, b ∈B such that a ▷Π(A) b. Now, let σ ∈SB be an arbitrary ranking such that a ≻σ b.
Also, let πB denote Π(B) and πA denote Π(A). Then, since Π is consistent,
πB(σ) =
X
σ2∈SA: σ2|B=σ
πA(σ2).
Now, for σ2 ∈SA such that σ2|B = σ, we have a ≻σ2 b and therefore πA(σ2) ≥πA(σab
2 ) (because
a ▷Π(A) b). It follows that
πB(σ) =
X
σ2∈SA:σ2|B=σ
πA(σ2) ≥
X
σ2∈SA:σ2|B=σ
πA(σab
2 )
=
X
σ′
2∈SA:σ′
2|B=σab
πA(σ′
2)
= πB(σab).
Therefore, a ▷Π(B) b, that is,
 ▷Π(A)|B

⊆
 ▷Π(B)

.
Next we show that
 ▷Π(B)

⊆
 ▷Π(A)|B

. Let a, b ∈B such that a ▷Π(B) b. Suppose for the
sake of contradiction that a ⋫Π(A) b. This implies that a ⋫Π b. However, ▷Π is a total preorder
13

--- Page 14 ---

because Π is SwD-compatible (by deﬁnition). It follows that b ▷Π a, and, in particular, b ▷Π(A) a
and b ▷Π(B) a.
As before, let πA denote Π(A) and πB denote Π(B). Because a ⋫Π(A) b, there exists σ∗∈SA
with a ≻σ∗b such that πA(σ∗) < πA(σab
∗). Moreover, because a ▷Π(B) b and b ▷Π(B) a, it holds that
πB(σ∗|B) = πB
 (σ∗|B)ab
. The consistency of Π then implies that
X
σ1∈SA: σ1|B=σ∗|B
πA(σ1) =
X
σ2∈SA: σ2|B=(σ∗|B)ab
πA(σ2).
(4)
Note σ1 = σ∗is a ranking that appears on the left-hand side of Equation (4), and σ2 = σab
∗
is a
ranking that appears on the right-hand side. Furthermore, we know that πA(σ∗) < πA(σab
∗). It
follows that there exists σ′ ∈SA with σ′|B = σ∗|B such that πA(σ′) > πA
 (σ′)ab
. Also, since
σ′|B = σ∗|B, it holds that a ≻σ′ b. We conclude that it cannot be the case that b ▷Π(A) a, leading
to a contradiction. Therefore, if a ▷Π(B) b, then a ▷Π(A) b, i.e.,
 ▷Π(B)

⊆
 ▷Π(A)|B

.
We next prove the lemma itself, i.e., that
 ▷Π(A)

= (▷Π|A) . Firstly, for a, b ∈A, if a ▷Π b, then
a ▷Π(A) b by deﬁnition. So, we easily get (▷Π|A) ⊆
 ▷Π(A)

.
In the other direction, let a, b ∈A such that a ▷Π(A) b. Let C be an arbitrary set of alternatives
containing a and b. From what we have shown above, we have
 ▷Π(A)|{a,b}

=
 ▷Π({a,b})

. Also,
 ▷Π(C)|{a,b}

=
 ▷Π({a,b})

. This gives us
 ▷Π(A)|{a,b}

=
 ▷Π(C)|{a,b}

. Hence, a ▷Π(C) b, and this is
true for every such subset C. We conclude that a ▷Π b, that is,
 ▷Π(A)

⊆(▷Π|A).
Lemma 4.19. Let f be a strongly SwD-eﬃcient anonymous SCC, and let Π be a consistent per-
mutation process that is SwD-compatible. Then for any ﬁnite subset of alternatives A, f(Π(A)) =
{a ∈A : a ▷Π b for all b ∈A}.
Proof. Let A be an arbitrary ﬁnite subset of alternatives.
Since strong SwD-eﬃciency implies
SwD-eﬃciency, Theorem 4.7 gives us
f(Π(A)) ⊇{a ∈A : a ▷Π b for all b ∈A}.
In the other direction, let a ∈f(Π(A)). Suppose for the sake of contradiction that there exists
b ∈A such that a ⋫Π b. Since ▷Π is a total preorder, it follows that b▷Π a. By Lemma 4.18, it holds
that
 ▷Π(A)

= (▷Π|A), and therefore a ⋫Π(A) b and b▷Π(A) a. But, since f is strongly SwD-eﬃcient,
it follows that a /∈f(Π(A)), which contradicts our assumption. Hence,
f(Π(A)) ⊆{a ∈A : a ▷Π b for all b ∈A},
and we have the desired result.
Theorem 4.20. Let Π be a consistent permutation process that is SwD-compatible, and let f be a
strongly SwD-eﬃcient anonymous SCC. Then the pair (Π, f) is stable.
Proof. Consider an arbitrary subset of alternatives A, and let B ⊆A. By Lemma 4.19, f(Π(A)) =
{a ∈A : a ▷Π b for all b ∈A}, and similarly for B. Suppose f(Π(A)) ∩B ̸= φ, and let a ∈
f(Π(A)) ∩B, i.e. a ∈f(Π(A)) and a ∈B. This means that a ▷Π b for all b ∈A, and, therefore
a ▷Π b for all b ∈B. We conclude that a ∈f(Π(B)), and hence f(Π(A)) ∩B ⊆f(Π(B)).
In the other direction, let a ∈f(Π(B)). This means that a ▷Π b for all b ∈B. Suppose for the
sake of contradiction that a /∈f(Π(A)). This means that there exists c ∈A such that a ⋫Π c. We
14

--- Page 15 ---

assumed f(Π(A)) ∩B ̸= φ, so let d ∈f(Π(A)) ∩B. Then, d ▷Π c. In summary, we have d ▷Π c and
a ⋫Π c, which together imply that a ⋫Π d (otherwise, it would violate transitivity). But d ∈B,
leading to a /∈f(Π(B)), which contradicts the assumption. Therefore, indeed a ∈f(Π(A)), and it
holds that f(Π(B)) ⊆f(Π(A)) ∩B, as long as f(Π(A)) ∩B ̸= φ.
We are now ready to prove Theorem 4.12.
Proof of Theorem 4.12. From Lemma 4.17, Borda count and Copeland are strongly SwD-eﬃcient.
Lemmas 4.9 and 4.10 imply that when Π is the TM or PL process, ▷Π is a total preorder. In
particular, a ▷Π b if µa ≥µb. Hence, Π is SwD-compatible. Therefore, by Theorem 4.20, the pair
(Π, f) is stable.
5
Instantiation of Our Approach
In this section, we instantiate our approach for ethical decision making, as outlined in Section 1.
In order to present a concrete algorithm, we consider a speciﬁc permutation process, namely the
TM process with a linear parameterization of the utility process parameters as a function of the
alternative features.
Let the set of alternatives be given by X ⊆Rd, i.e. each alternative is represented by a vector
of d features. Furthermore, let N denote the total number of voters. Assume for now that the
data-collection step (Step I) is complete, i.e., we have some pairwise comparisons for each voter;
we will revisit this step in Section 6.
Step II: Learning. For each voter, we learn a TM process using his pairwise comparisons to
represent his preferences. We assume that the mode utility of an alternative x depends linearly on
its features, i.e., µx = β⊺x. Note that we do not need an intercept term, since we care only about
the relative ordering of utilities. Also note that the parameter β ∈Rd completely describes the
TM process, and hence the parameters β1, β2, · · · βN completely describe the models of all voters.
Next we provide a computationally eﬃcient method for learning the parameter β for a partic-
ular voter. Let (X1, Z1), (X2, Z2), · · · , (Xn, Zn) denote the pairwise comparison data of the voter.
Speciﬁcally, the ordered pair (Xj, Zj) denotes the jth pair of alternatives compared by the voter,
and the fact that the voter chose Xj over Zj. We use maximum likelihood estimation to estimate
β. The log-likelihood function is
L(β) = log


n
Y
j=1
P(Xj ≻Zj; β)


=
n
X
j=1
log P(UXj > UZj; β)
=
n
X
j=1
log Φ (β⊺(Xj −Zj)) ,
where Φ is the cumulative distribution function of the standard normal distribution, and the last
transition holds because Ux ∼N(β⊺x, 1
2). Note that the standard normal CDF Φ is a log-concave
function. This makes the log-likelihood concave in β, hence we can maximize it eﬃciently.
15

--- Page 16 ---

Step III: Summarization. After completing Step II, we have N TM processes represented by the
parameters β1, β2, · · · βN. In Step III, we bundle these individual models into a single permutation
process ˆΠ, which, in the current instantiation, is also a TM process with parameter ˆβ (see Section 7
for a discussion of this point). We perform this step because we must be able to make decisions
fast, in Step IV. For example, in the autonomous vehicle domain, the AI would only have a split
second to make a decision in case of emergency; aggregating information from millions of voters
in real time will not do. By contrast, Step III is performed oﬄine, and provides the basis for fast
aggregation.
Let Πβ denote the TM process with parameter β. Given a ﬁnite subset of alternatives A ⊆X,
the anonymous preference proﬁle generated by the model of voter i is given by Πβi(A). Ideally,
we would like the summary model to be such that the proﬁle generated by it, ˆΠ(A), is as close
as possible to Π∗(A) =
1
N
PN
i=1 Πβi(A), the mean proﬁle obtained by giving equal importance to
each voter. However, there does not appear to be a straightforward method to compute the “best”
ˆβ, since the proﬁles generated by the TM processes do not have an explicit form. Hence, we use
utilities as a proxy for the quality of ˆβ. Speciﬁcally, we ﬁnd ˆβ such that the summary model
induces utilities that are as close as possible to the mean of the utilities induced by the per-voter
models, i.e., we want U
ˆβ
x to be as close as possible (in terms of KL divergence) to
1
N
PN
i=1 Uβi
x
for each x ∈X, where Uβ
x denotes the utility of x under TM process with parameter β. This is
achieved by taking ˆβ = 1
N
PN
i=1 βi, as shown by the following proposition.
Proposition 5.1. The vector β = 1
N
PN
i=1 βi minimizes KL

1
N
PN
i=1 Uβi
x
Uβ
x

for any x ∈X.
Proof. Let ¯β = 1
N
PN
i=1 βi. We know that Uβ
x denotes the utility of x under the TM process with
parameter β. So, Uβ
x ∼N(β⊺x, 1
2). Let its density be given by qx,β(·). Also, Uβi
x
∼N(β⊺
i x, 1
2).
Hence,
1
N
N
X
i=1
Uβi
x
∼N(¯β⊺x, 1
2N ).
Let its density function be denoted by px(·). Then
KL(px∥qx,β) =
Z
px(t) log px(t)dt −
Z
px(t) log qx,β(t)dt.
Since the ﬁrst term does not depend on β, let us examine the second term:
−
Z
px(t) log qx,β(t)dt = −
Z
px(t) log
 1
√π exp
 −(t −β⊺x)2
dt
= −
Z
px(t)

−1
2 log(π) −(t −β⊺x)2

dt
= 1
2 log(π)
Z
px(t)dt

+
Z
px(t)
 t2 + (β⊺x)2 −2tβ⊺x

dt
= 1
2 log(π) +
Z
t2px(t)dt + (β⊺x)2
Z
px(t)dt −2β⊺x
Z
tpx(t)dt

= 1
2 log(π) +
 1
2N + (¯β⊺x)2

+ (β⊺x)2 −2β⊺x(¯β⊺x)

16

--- Page 17 ---

= 1
2 log(π) + 1
2N +
 ¯β⊺x −β⊺x
2 .
This term is minimized at β = ¯β for any x, and therefore KL( 1
N
PN
i=1 Uβi
x
Uβ
x ) is minimized at
that value as well.
Step IV: Aggregation.
As a result of Step III, we have exactly one (summary) TM pro-
cess ˆΠ (with parameter ˆβ = ¯β) to work with at runtime.
Given a ﬁnite set of alternatives
A = {x1, x2, · · · , xm}, we must aggregate the preferences represented by the anonymous prefer-
ence proﬁle ˆΠ(A). This is where the machinery of Section 4 comes in: We simply need to select
an alternative that has maximum mode utility among ˆβ
⊺x1, ˆβ
⊺x2, · · · , ˆβ
⊺xm. Such an alterna-
tive would be selected by any anonymous SCC that is monotonic and neutral, when applied to
ˆΠ(A), as shown by Theorem 4.1. Moreover, this aggregation method is equivalent to applying the
Borda count or Copeland SCCs. Hence, we also have the desired stability property, as shown by
Theorem 4.12.
6
Implementation and Evaluation
In this section, we implement the algorithm presented in Section 5, and empirically evaluate it.
We start with an implementation on synthetic data, which allows us to eﬀectively validate both
Steps II and III of our approach.
We then describe the Moral Machine dataset mentioned in
Section 1, present the implementation of our algorithm on this dataset, and evaluate the resultant
system for ethical decision making in the autonomous vehicle domain (focusing on Step III).
6.1
Synthetic Data
Setup. We represent the preferences of each voter using a TM process. Let βi denote the true
parameter corresponding to the model of voter i. We sample βi from N(m, Id) (independently
for each voter i), where each mean mj is sampled independently from the uniform distribution
U(−1, 1), and the number of features is d = 10.
In each instance (deﬁned by a subset of alternatives A with |A| = 5), the desired winner is given
by the application of Borda count to the mean of the proﬁles of the voters. In more detail, we
compute the anonymous preference proﬁle of each voter Πβi(A), and then take a mean across all
the voters to obtain the desired proﬁle 1
N
PN
i=1 Πβi(A). We then apply Borda count to this proﬁle
to obtain the winner. Note that, since we are dealing with TM processes, we cannot explicitly
construct Πβi(A); we therefore estimate it by sampling rankings according to the TM process of
voter i.
Evaluation of Step II (Learning). In practice, the algorithm does not have access to the true
parameter βi of voter i, but only to pairwise comparisons, from which we learn the parameters.
Thus we compare the computation of the winner (following the approach described above) using
the true parameters, and using the learned parameters as in Step II. We report the accuracy as the
fraction of instances, out of 100 test instances, in which the two outcomes match.
To generate each pairwise comparison of voter i, for each of N = 20 voters, we ﬁrst sample two
alternatives x1 and x2 independently from N(0, Id). Then, we sample their utilities Ux1 and Ux2
from N(β⊺
i x1, 1
2) and N(β⊺
i x2, 1
2), respectively. Of course, the voter prefers the alternative with
17

--- Page 18 ---

0
25
50
75
100 125 150 175 200
Number of pairwise comparisons per voter
0.0
0.2
0.4
0.6
0.8
1.0
Accuracy
Figure 1: Accuracy of Step II (synthetic data)
0
25
50
75
100 125 150 175
Number of voters
0.75
0.80
0.85
0.90
0.95
1.00
Accuracy
Figure 2: Accuracy of Step III (synthetic data)
higher sampled utility. Once we have the comparisons, we learn the parameter βi by computing
the MLE (as explained in Step II of Section 5). In our results, we vary the number of pairwise
comparisons per voter and compute the accuracy to obtain the learning curve shown in Figure 1.
Each datapoint in the graph is averaged over 50 runs. Observe that the accuracy quickly increases
as the number of pairwise comparisons increases, and with just 30 pairwise comparisons we achieve
an accuracy of 84.3%. With 100 pairwise comparisons, the accuracy is 92.4%.
Evaluation of Step III (Summarization). To evaluate Step III, we assume that we have access
to the true parameters βi, and wish to determine the accuracy loss incurred in the summarization
step, where we summarize the individual TM models into a single TM model. As described in
Section 5, we compute ¯β = 1
N
PN
i=1 βi, and, given a subset A (which again has cardinality 5), we
aggregate using Step IV, since we now have just one TM process. For each instance, we contrast
our computed winner with the desired winner as computed previously. We vary the number of
voters and compute the accuracy to obtain Figure 2. The accuracies are averaged over 50 runs.
Observe that the accuracy increases to 93.9% as the number of voters increases. In practice we
expect to have access to thousands, even millions, of votes (see Section 6.2). We conclude that,
surprisingly, the expected loss in accuracy due to summarization is quite small.
Robustness. Our results are robust to the choice of parameters, as we demonstrate in Appendix A.
6.2
Moral Machine Data
Moral Machine is a platform for gathering data on human perception of the moral acceptability of
decisions made by autonomous vehicles faced with choosing which humans to harm and which to
save. The main interface of Moral Machine is the Judge mode. This interface generates sessions of
random moral dilemmas. In each session, a user is faced with 13 instances. Each instance features an
autonomous vehicle with a brake failure, facing a moral dilemma with two possible alternatives, that
is, each instance is a pairwise comparison. Each of the two alternatives corresponds to sacriﬁcing
the lives of one group of characters to spare those of another group of characters. Figure 3 shows
an example of such an instance. Respondents choose the outcome that they prefer the autonomous
vehicle to make.
Each alternative is characterized by 22 features: relation to the autonomous vehicle (passengers
or pedestrians), legality (no legality, explicitly legal crossing, or explicitly illegal crossing), and
counts of 20 character types, including ones like man, woman, pregnant woman, male athlete,
female doctor, dog, etc. When sampling from the 20 characters, some instances are generated to
18

--- Page 19 ---

Figure 3: Moral Machine — Judge interface. This particular choice is between a group of pedestri-
ans that includes a female doctor and a cat crossing on a green light, and a group of passengers
including a woman, a male executive, an elderly man, an elderly woman, and a girl.
have an easy-to-interpret tradeoﬀwith respect to some dimension, such as gender (males on one
side vs. females on the other), age (elderly vs. young), ﬁtness (large vs. ﬁt), etc., while other
instances have groups consisting of completely randomized characters being sacriﬁced in either
alternative. Alternatives with all possible combinations of these features are considered, except
for the legality feature in cases when passengers are sacriﬁced. In addition, each alternative has
a derived feature, “number of characters,” which is simply the sum of counts of the 20 character
types (making d = 23).
As mentioned in Section 1, the Moral Machine dataset consists of preference data from 1,303,778
voters, amounting to a total of 18,254,285 pairwise comparisons. We used this dataset to learn the
β parameters of all 1.3 million voters (Step II, as given in Section 5). Next, we took the mean of
all of these β vectors to obtain ˆβ (Step III). This gave us an implemented system, which can be
used to make real-time choices between any ﬁnite subset of alternatives.
Importantly, the methodology we used, in Section 6.1, to evaluate Step II on the synthetic data
cannot be applied to the Moral Machine data, because we do not know which alternative would be
selected by aggregating the preferences of the actual 1.3 million voters over a subset of alternatives.
However, we can apply a methodology similar to that of Section 6.1 in order to evaluate Step
III. Speciﬁcally, as in Section 6.1, we wish to compare the winner obtained using the summarized
model, with the winner obtained by applying Borda count to the mean of the anonymous preference
proﬁles of the voters.
An obstacle is that now we have a total of 1.3 million voters, and hence it would take an
extremely long time to calculate the anonymous preference proﬁle of each voter and take their
mean (this was the motivation for having Step III in the ﬁrst place). So, instead, we estimate the
mean proﬁle by sampling rankings, i.e., we sample a voter i uniformly at random, and then sample
a ranking from the TM process of voter i; such a sampled ranking is an i.i.d. sample from the mean
anonymous proﬁle. Then, we apply Borda count as before to obtain the desired winner (note that
this approach is still too expensive to use in real time). The winner according to the summarized
model is computed exactly as before, and is just as eﬃcient even with 1.3 million voters.
Using this methodology, we computed accuracy on 3000 test instances, i.e., the fraction of
19

--- Page 20 ---

2
3
4
5
6
7
8
9
10
Number of alternatives per instance
0.75
0.80
0.85
0.90
0.95
1.00
Accuracy
Figure 4: Accuracy of Step III (Moral Machine data)
instances in which the two winners match. Figure 4 shows the results as the number of alternatives
per instance is increased from 2 to 10. Observe that the accuracy is as high as 98.2% at 2 alternatives
per instance, and gracefully degrades to 95.1% at 10.
7
Discussion
The design of intelligent machines that can make ethical decisions is, arguably, one of the hardest
challenges in AI. We do believe that our approach takes a signiﬁcant step towards addressing
this challenge. In particular, the implementation of our algorithm on the Moral Machine dataset
has yielded a system which, arguably, can make credible decisions on ethical dilemmas in the
autonomous vehicle domain (when all other options have failed). But this paper is clearly not the
end-all solution.
7.1
Limitations
While the work we presented has some signiﬁcant limitations, we view at least some of them as
shortcomings of the current (proof-of-concept) implementation, rather than being inherent to the
approach itself, as we explain below.
First, Moral Machine users may be poorly informed about the dilemmas at hand, or may
not spend enough time thinking through the options, potentially leading — in some cases — to
inconsistent answers and poor models. We believe, though, that much of this noise cancels out in
Steps III and IV.
In this context, it is important to note that some of us have been working with colleagues on an
application of the approach presented here to food allocation [12]. In this implementation — which
is a collaboration with 412 Food Rescue, a Pittsburgh-based nonproﬁt — the set of alternatives
includes hundreds of organizations (such as food pantries) that can receive incoming food donations.
The voters in this implementation are a few dozen stakeholders: representatives of donor and
recipient organizations, volunteers (who deliver the donation from the donor to the recipient), and
employees of 412 Food Rescue. These voters are obviously well informed, and the results of Lee et al.
[12] indicate that they have been exceptionally thoughtful in providing their answers to pairwise
20

--- Page 21 ---

comparisons.
Second, our dataset contains roughly 14 pairwise comparisons per voter on average. As sug-
gested by Figure 1, this may not be suﬃcient for learning truly accurate voter models. However,
subsequent work by Kim et al. [11] indicates that this problem can be alleviated by assuming
that the parameters that determine the preferences of individual voters are drawn from a common
distribution. This correlates the individual voter models, and, intuitively, allows the millions of
examples to contribute to learning each and every model. Results based on the Moral Machine
dataset indeed show that this technique leads to increased accuracy in predicting pairwise compar-
isons. In addition, in the work of Lee et al. [12], many voters answered as many as 100 pairwise
comparison queries, leading to strikingly accurate voter models that predict pairwise comparisons
with roughly 90% accuracy.
Third, the choice of features in the Moral Machine dataset may be contentious. On the one
hand, should we really take into account things like gender and profession to determine who lives
and who dies? On the other hand, the set of alternatives is too coarse, in that it does not include
information about probabilities and degrees of harm. As discussed by Conitzer et al. [6], feature
selection is likely to be a major issue for any machine-learning-based approach to ethical decision
making.
7.2
Extensions
Going forward, most important is the (primarily conceptual) challenge of extending our framework
to incorporate ethical or legal principles — at least for simpler settings where they might be easier
to specify. The signiﬁcant advantage of having our approach in place is that these principles do
not need to always lead to a decision, as we can fall back on the societal choice. This allows for a
modular design where principles are incorporated over time, without compromising the ability to
make a decision in every situation.
In addition, as mentioned in Section 5, we have made some speciﬁc choices to instantiate
our approach.
We discuss two of the most consequential choices.
First, we assume that the
mode utilities have a linear structure.
This means that, under the TM model, the estimation
of the maximum likelihood parameters is a convex program (see Section 5), hence we can learn
the preferences of millions of voters, as in the Moral Machine dataset. Moreover, a straightforward
summarization method works well. However, dealing with a richer representation for utilities would
require new methods for both learning and summarization (Steps II and III).
Second, the instantiation given in Section 5 summarizes the N individual TM models as a single
TM model. While the empirical results of Section 6 suggest that this method is quite accurate,
even higher accuracy can potentially be achieved by summarizing the N models as a mixture of K
models, for a relatively small K. This leads to two technical challenges: What is a good algorithm
for generating this mixture of, say, TM models? And, since the framework of Section 4 would not
apply, how should such a mixture be aggregated — does the (apparently mild) increase in accuracy
come at great cost to computational eﬃciency?
Acknowledgments
This work was partially supported by NSF grants IIS-1350598, IIS-1714140, IIS-1149803, CCF-
1525932, and CCF-1733556; by ONR grants N00014-16-1-3075 and N00014-17-1-2428; by two Sloan
21

--- Page 22 ---

Research Fellowships and a Guggenheim Fellowship; and by the Ethics & Governance of AI Fund.
References
[1] A. Awad, S. Dsouza, R. Kim, J. Schulz, J. Henrich, A. Shariﬀ, J.-F. Bonnefon, and I. Rahwan.
The Moral Machine experiment. Nature, 2018. Forthcoming.
[2] J.-F. Bonnefon, A. Shariﬀ, and I. Rahwan. The social dilemma of autonomous vehicles. Science,
352(6293):1573–1576, 2016.
[3] F. Brandt, V. Conitzer, U. Endriss, J. Lang, and A. D. Procaccia, editors.
Handbook of
Computational Social Choice. Cambridge University Press, 2016.
[4] I. Caragiannis, A. D. Procaccia, and N. Shah. When do noisy votes reveal the truth? ACM
Transactions on Economics and Computation, 4(3): article 15, 2016.
[5] F. Caron and Y. W. Teh. Bayesian nonparametric models for ranked data. In Proceedings of the
26th Annual Conference on Neural Information Processing Systems (NIPS), pages 1529–1537,
2012.
[6] V. Conitzer, W. Sinnott-Armstrong, J. Schaich Borg, Y. Deng, and M. Kramer. Moral decision
making frameworks for artiﬁcial intelligence. In Proceedings of the 31st AAAI Conference on
Artiﬁcial Intelligence (AAAI), pages 4831–4835, 2017.
[7] C. Dwork, M. Hardt, T. Pitassi, O. Reingold, and R. S. Zemel. Fairness through awareness.
In Proceedings of the 3rd Innovations in Theoretical Computer Science Conference (ITCS),
pages 214–226, 2012.
[8] R. Freedman, J. Schaich Borg, W. Sinnott-Armstrong, J. P. Dickerson, and V. Conitzer.
Adapting a kidney exchange algorithm to align with human values. In Proceedings of the 32nd
AAAI Conference on Artiﬁcial Intelligence (AAAI), pages 1636–1643, 2018.
[9] J. Greene, F. Rossi, J. Tasioulas, K. B. Venable, and B. Williams. Embedding ethical principles
in collective decision support systems. In Proceedings of the 30th AAAI Conference on Artiﬁcial
Intelligence (AAAI), pages 4147–4151, 2016.
[10] J. Jarvis Thomson. The trolley problem. The Yale Law Journal, 94(6):1395–1415, 1985.
[11] R. Kim, M. Kleiman-Weiner, A. Abeliuk, E. Awad, S. Dsouza, J. Tenenbaum, and I. Rahwan.
A computational model of commonsense moral decision making. arXiv:1801.04346, 2018.
[12] M. K. Lee, D. Kusbit, A. Kahng, J. T. Kim, X. Yuan, A. Chan, R. Noothigattu, D. See, S. Lee,
C.-A. Psomas, and A. D. Procaccia. WeBuildAI: Participatory framework for fair and eﬃcient
algorithmic governance. Manuscript, 2018.
[13] R. D. Luce. Individual Choice Behavior: A Theoretical Analysis. Wiley, 1959.
[14] J. I. Marden. Analysing and Modeling Rank Data. Chapman & Hall, 1995.
[15] F. Mosteller. Remarks on the method of paired comparisons: I. the least squares solution
assuming equal standard deviations and equal correlations. Psychometrika, 16(1):3–9, 1951.
22

--- Page 23 ---

[16] H. Moulin. The Strategy of Social Choice, volume 18 of Advanced Textbooks in Economics.
North-Holland, 1983.
[17] R. Noothigattu, S. S. Gaikwad, E. Awad, S. Dsouza, I. Rahwan, P. Ravikumar, and A. D.
Procaccia. A voting-based system for ethical decision making. In Proceedings of the 32nd
AAAI Conference on Artiﬁcial Intelligence (AAAI), pages 1587–1594, 2018.
[18] R. Plackett. The analysis of permutations. Applied Statistics, 24:193–202, 1975.
[19] A. Prasad, H. H. Pareek, and P. Ravikumar. Distributional rank aggregation, and an axiomatic
analysis. In Proceedings of the 32nd International Conference on Machine Learning (ICML),
pages 2104–2112, 2015.
[20] J. Rawls. A Theory of Justice. Harvard University Press, 1971.
[21] A. K. Sen. Choice functions and revealed preference. Review of Economic Studies, 38(3):
307–317, 1971.
[22] L. L. Thurstone. A law of comparative judgment. Psychological Review, 34:273–286, 1927.
[23] W. Wallach and C. Allen.
Moral Machines: Teaching Robots Right from Wrong.
Oxford
University Press, 2008.
[24] B. Williams. Ethics and the Limits of Philosophy. Harvard University Press, 1986.
A
Robustness of the Empirical Results
In Section 6.1, we presented experiments using synthetic data, with the following parameters: each
instance has 5 alternatives, the number of features is d = 10, and, in Step II, we let number of voters
be N = 20. In this appendix, to demonstrate the robustness of both steps, we show experimental
results for diﬀerent values of these parameters (keeping everything else ﬁxed).
0
25
50
75
100 125 150 175 200
Number of pairwise comparisons per voter
0.0
0.2
0.4
0.6
0.8
1.0
Accuracy
Figure 5: Accuracy of Step II with number of voters N = 40 (synthetic data)
23

--- Page 24 ---

0
25
50
75
100 125 150 175 200
Number of pairwise comparisons per voter
0.0
0.2
0.4
0.6
0.8
1.0
Accuracy
(a) Accuracy of Step II
0
25
50
75
100 125 150 175
Number of voters
0.75
0.80
0.85
0.90
0.95
1.00
Accuracy
(b) Accuracy of Step III
Figure 6: Results with 3 alternatives per instance (synthetic data)
0
25
50
75
100 125 150 175 200
Number of pairwise comparisons per voter
0.0
0.2
0.4
0.6
0.8
1.0
Accuracy
(a) Accuracy of Step II
0
25
50
75
100 125 150 175
Number of voters
0.75
0.80
0.85
0.90
0.95
1.00
Accuracy
(b) Accuracy of Step III
Figure 7: Results with number of features d = 20 (synthetic data)
A.1
Number of Voters in Step II
To show robustness with respect to the number of voters N in Step II, we run the Step II experiments
with 40 (instead of N = 20). The results are shown in Figure 5.
As before, we observe that the accuracy quickly increases as the number of pairwise comparisons
increases, and with just 30 pairwise comparisons we achieve an accuracy of 89.3%.
With 100
pairwise comparisons, the accuracy is 94.9%.
A.2
Number of Alternatives
To show robustness with respect to the number of alternatives, we run experiments with |A| = 3
(instead of |A| = 5). The results are shown in Figure 6.
Similarly to Section 6.1, for Step II, we observe that the accuracy quickly increases as the
number of pairwise comparisons increases, and with just 30 pairwise comparisons we achieve an
accuracy of 88.8%. With 100 pairwise comparisons, the accuracy is 93.5%. For Step III, we observe
that the accuracy increases to 96.2% as the number of voters increases.
24

--- Page 25 ---

A.3
Number of Features
To show robustness with respect to the number of features d, we run experiments with d = 20
(instead of d = 10). The results are shown in Figure 7.
Again, for Step II, we observe that the accuracy quickly increases (though slower than in
Section 6.1, because of higher dimension) as the number of pairwise comparisons increases. With
just 30 pairwise comparisons we achieve an accuracy of 74.6%, and with 100 pairwise comparisons,
the accuracy is 88.2%. For Step III, we observe that the accuracy increases to 94.7% as the number
of voters increases.
25

```
