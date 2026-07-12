---
source_pdf: "[[Lit-WS-PDFs/2025/2025-Maura-Rivero-Jackpot Alignment as Maximal Lottery.pdf]]"
extracted_date: "2026-07-11"
pages: 17
extractor: "PyMuPDF"
---

Page 1:
Jackpot! Alignment as a Maximal Lottery
Roberto-Rafael Maura-Rivero 1 2 Marc Lanctot 1 Francesco Visin 1 Kate Larson 1 3
Abstract
Reinforcement Learning from Human Feedback
(RLHF), the standard for aligning Large Lan-
guage Models (LLMs) with human values, is
known to fail to satisfy properties that are intu-
itively desirable, such as respecting the prefer-
ences of the majority (Ge et al., 2024). To over-
come these issues, we propose the use of a proba-
bilistic Social Choice rule called maximal lotteries
as a replacement for RLHF. We show that a family
of alignment techniques, namely Nash Learning
from Human Feedback (NLHF) (Munos et al.,
2023) and variants, approximate maximal lottery
outcomes and thus inherit its beneficial proper-
ties. We confirm experimentally that our proposed
methodology handles situations that arise when
working with preferences more robustly than stan-
dard RLHF, including supporting the preferences
of the majority, providing principled ways of han-
dling non-transitivities in the preference data, and
robustness to irrelevant alternatives. This results
in systems that better incorporate human values
and respect human intentions.
1. Introduction
Reinforcement Learning from Human Feedback (RLHF)
has emerged as the de-facto standard to align Large Lan-
guage Models (LLMs) with human values and preferences.
Using ideas from revealed preference theory in economics,
current RLHF methods adapt the LLM’s distribution of gen-
erated text or tokens so as to maximize a reward model
learned from the ratings of human evaluators.
Despite its widespread use in fine tuning LLMs (Touvron
et al., 2023; OpenAI, 2023; Anthropic, 2023; Google, 2023),
it has been recognized that current approaches suffer from
fundamental limitations in the human feedback, the reward
model, and training the policy (Casper et al., 2023). These
challenges include tradeoffs between the richness and effi-
ciency of feedback types, with binary preferences between
pairs of examples being more prominent (Christiano et al.,
1Google DeepMind 2London School of Economics 3University
of Waterloo. Correspondence to: Roberto-Rafael Maura-Rivero
<r.maura-rivero@lse.ac.uk>.
🤖
RED
BLUE
RLHF
RED
Which colour should we paint the room? 
R ≻ {B, G} 7 times
B ≻ {R, G} 6 times
G ≻ {B, R} 2 times
󰳜󰳝󰬋󰬍󰬎
1
2
3
󰳜󰳝󰬋󰬍󰬎
🤖
Max.Lottery
BLUE
The Majority 
prefers BLUE
Figure 1: Although B is the option preferred by the major-
ity, LLMs aligned with RLHF fail to capture that, returning
R. Thus, RLHF violates major democratic properties such
as majority rule, while methods that emulate Maximal Lot-
teries satisfy them.
2017), the assumption that a single reward function can
represent a diverse population, which leads to current ap-
proaches modelling differences among evaluators as noise
instead of important sources of disagreement (Baumler et al.,
2023) or ambiguity (Schaekermann et al., 2018), and re-
ward models failing to generalize even with perfect training
data (Skalse & Abate, 2023).
A number of recent papers have begun to explore alignment
problems through the lens of Social Choice (Ge et al., 2024;
Dai & Fleisig, 2024; Mishra, 2023; Siththaranjan et al.,
2024), which provides principled methods for aggregating
preferences, particularly for diverse populations, as well as
tools and insights to understand the benefits and challenges
that arise from that (Brandt et al., 2016). In a recent position
paper, Conitzer et al. argued that methods from Social
Choice Theory provide alternative approaches to current
RLHF methodologies (Conitzer et al., 2024).
In this paper we make the argument that a Probabilistic
Social Choice function, maximal lotteries (Fishburn, 1984a),
is particularly well suited for RLHF and alignment problems.
In particular,
1
arXiv:2501.19266v1  [cs.AI]  31 Jan 2025


Page 2:
Jackpot! Alignment as a Maximal Lottery
• We propose an alternative alignment method to RLHF
based on Maximal Lotteries, a stochastic voting rule
from Social Choice Theory.
• We formally prove that game-theoretic approaches to
preference modeling in RLHF, specifically Nash Learn-
ing from Human Feedback (Munos et al., 2023) and its
variants (Calandriello et al., 2024; Swamy et al., 2024),
emulate maximal lotteries.
• Through controlled experiments, we show that our ap-
proach produces LLM outputs that better reflect aggre-
gate human preferences compared to standard RLHF,
supporting the preferences of the majority, providing
principled ways of handling non-transitivities in the
preferences, and robustness to of irrelevant alternatives.
2. Background
2.1. Reinforcement Learning from Human Feedback
RLHF involves training a reward model and then using
this model to guide a policy (the LLM) through rein-
forcement learning. A reward model rθ(x, y) is trained
to predict a score indicating how good the response y
is to the prompt x.
This model is learned from a
dataset of pairwise comparisons, where human annota-
tors indicate their preferences.
The training objective
involves maximizing the likelihood of correctly predict-
ing the preferred option using a binary cross-entropy loss,
L(θ) = −E(x,y+,y−)[log(σ(rθ(x, y+)−rθ(x, y−))). Here,
(x, y+, y−) represents a data point, with x being the prompt,
y+ the preferred completion (the “winner”), and y−the less
preferred completion (the “loser”) , rθ is the reward model
parameterized by θ and σ is the sigmoid function. This
loss function is based on the Bradley-Terry model (Rafailov
et al., 2023) which is the foundation of the classical Elo
rating system (Elo, 1978). While this model is widely-used
for RLHF, it has several well-documented problems that
could affect preference learning (Shah & Wainwright, 2017;
Balduzzi et al., 2019; Bertand et al., 2023; Lanctot et al.,
2023; Munos et al., 2023).
The LLM, acting as the policy πϕ parameterized by ϕ,
is then trained using reinforcement learning algorithms
like Proximal Policy Optimization (PPO) (Schulman et al.,
2017). A simplified objective (ignoring regularization) can
be written as maxϕ Ex∼D,y∼πϕ(x)[rθ(x, y)], where D is the
distribution of prompts. This loss encourages the LLM to
generate completions that receive high reward.
2.2. Social Choice Theory
The central problem addressed by Social Choice Theory is
how to aggregate the preferences of a population so as to
reach some optimal collective decision. Assume there is
a population P of individuals, each of whom have prefer-
ences over some set of options Y. Given a pair of different
alternatives a, b ∈Y, an individual i ∈P is able to report
that either they prefer a to b (a ≻i b) or b to a (b ≻i a).1
A Social Choice function f is a map that assigns to each
preference profile {≻i}i∈P a winning alternative in Y, i.e.
f({≻i}i∈P) ∈Y. A Probabilistic Social Choice function
ρ is a similar concept that returns a distribution over the set
of alternatives, ρ({≻i}i∈P) ∈∆(Y).
Much of Social Choice Theory is axiomatic in na-
ture (Brandt et al., 2016), in that the field tries to understand
what properties Social Choice functions can and should ex-
hibit. For example, a Condorcet winner defines a fairly
intuitive concept: an alternative a is a Condorcet winner if a
preferred by more individuals than b in every head-to-head
pairing for every b ∈Y (for a more formal definition of
Condorcet winners, see Definition 2 in Section 3.2). So-
cial Choice functions that are guaranteed to return a Con-
dorcet winner when it exists are called Condorcet-consistent
rules. Not all Social Choice functions are Condorcet con-
sistent, like the well known class of scoring rules which
include plurality and Borda. These rules translate individ-
ual’s preference rankings over m alternatives to a score
vector w = (w1, . . . , wm) where w1 ≥w2 ≥. . . wm and
w1 > wm. Each alternative’s total score is obtained by sum-
ming the individual scores assigned by all voters. Scoring
rules can be interpreted as Social Choice functions where
alternatives are simply sorted according to their scores and
the top option is returned.
The Borda rule, for example, uses a scoring vector w =
(m −1, m −2, . . . , 0).2 While the scoring rules are not
guaranteed to return Condorcet winners, they exhibit other
desirable properties. Selecting a Social Choice function al-
ways implies a tradeoff in properties it will support, as crys-
talized by Arrow’s Impossibility Theorem (Arrow, 1950),
so clear specifications as to what properties are important in
the context of an application of Social Choice is of critical
importance.
3. Alignment as a Social Choice Problem
We support the view of several works in the literature (Ge
et al., 2024; Dai & Fleisig, 2024; Mishra, 2023; Conitzer
et al., 2024) that the alignment problem may be formalized
as a Social Choice problem. Under this lens, given a prompt
x, the set of all possible responses (up to a finite maximum
length L) forms the set of alternatives Y the LLM has to
1For ease of exposition we will assume strict preferences in the
rest of the paper, but results can be extended to weak preferences.
2Since Borda is a C2 rule according to Fishburn’s classification,
it can be computed by using pairwise comparisons. The details are
beyond the scope of this paper but we refer an interested reader to
(Brandt et al., 2016).
2


Page 3:
Jackpot! Alignment as a Maximal Lottery
choose from. The population P is then the set of individ-
uals that report their preferences over Y in the dataset of
pairwise comparisons {(xk, y+
k , y−
k )}k∈{1,...,K}, where K
is the length of the dataset. If we denote the probability of
statement y being the response of the LLM to prompt x as
π(y|x), the LLM can be thought of as a distribution over
all possible responses Y. This distribution has been trained
on the dataset {(xk, y+
k , y−
k )}k∈{1,...,K}. Thus, π(.|x) is a
function from the preference profile {≻i}i∈P to a distribu-
tion over Y. Therefore, it is a Probabilistic Social Choice
function. To simplify notation, in the rest of the paper we
will omit the conditioning on prompt x.
Therefore, solving the problem of alignment requires (a) to
choose a Probabilistic Social Choice function ρ with desir-
able properties from Social Choice Theory (e.g. Majority,
Condorcet Consistency, Pareto Efficiency, IIA, ...), and (b)
to finetune the LLM pushing its distribution as close as
possible to that of the Probabilistic Social Choice function
ρ.
3.1. RLHF Implements Borda
There is already an existing connection between current us-
ages of RLHF and Social Choice Theory. In a recent paper,
Siththaranjan et al. showed that the standard RLHF methods
based on the Bradley-Terry model effectively implement
the Borda scoring rule (Theorem 3.1 (Siththaranjan et al.,
2024)). For the sake of completeness we provide the full
theorem statement and proof in Appendix A.9.
Since Borda is a well understood Social Choice function,
we know that it is not Condorcet consistent. This means that
all RLHF methods that aggregates individuals’ preferences
by emulating Borda may result in some counter-intuitive
outcomes. Consider the example in Figure 1. A group of
five individuals are asked to specify their favourite colour.
Two of the five report that they prefer red more than green,
and green more than blue (i.e. R ≻i G ≻i B for i ∈
{1, 2}). Three of the five report they prefer blue more than
red, and red more than green (i.e. B ≻i R ≻i G for
i ∈{3, 4, 5}). Applying Borda to this example, the Borda
scores for the three alternatives (i.e., binary win counts)
are 7 for red, 6 for blue, and 2 for green. Thus, an RLHF
trained policy would be biased towards returning red, which
seems counterintutive and not necessarily a good reflection
of the underlying preferences of the group. This raises the
question: What properties do we want alignment methods
for LLMs to support?
3.2. Properties for Alignment
In this section we propose several properties to assess the
alignment for LLMs. These properties are inspired by con-
cepts studied in the Social Choice literature and address
concerns that arise when reasoning about aggregation of
Preference
Ana
Bob
Carla
1st
R
G
B
2nd
B
R
G
3rd
G
B
R
Table 1: Cyclic preference example.
individuals’ preferences (Brandt et al., 2016), while also
addressing some of the concerns recently raised in Casper
et al. (2023).
First, we argue that outcomes like the one shown in Sec-
tion 3.1 should be avoided. When B is preferred by a major-
ity of the individuals, that is what the LLM should return. In
other words, any alignment method should emulate a Social
Choice function that is majority consistent.
Definition 1. A Social Choice function f is majority con-
sistent if for all preferences {≻i}i∈P, if
∃y⋆∈Y s.t. #{i ∈P : ∀y ∈Y\{y⋆}, (y⋆≻i y)} ≥#P
2
then y⋆= f({≻i}i∈P).
A Condorcet winner is an alternative that beats every other
alternative in a pairwise majority vote.
Definition 2. Alternative a ∈Y is a Condorcet winner
with respect to preferences {≻i}i∈P if for all b ∈Y \ {a},
N(a, b) > N(b, a), where N(a, b) = #{i ∈P : a ≻i b}.
Clearly a majority winner is a Condorcet winner. Any Social
Choice function that returns a Condorcet winner when it
exists is called Condorcet consistent. It has been argued that
a Condorcet winner captures the inherent representativeness
of the individuals’ preferences and is viewed as a consensus
choice (de Condorcet, 1785), Any alignment method that
emulates a Condorcet consistent Social Choice function will
also best reflect the interests of the population.
Condorcet winners may not always exist. In particular, if
there are collection of preferences that induce a cycle, then
there is no Condorcet winner. A simple example where
this happens is shown in Table 1, where there is no clear
consensus as to which is the socially preferred colour. We
would like an alignment method that can capture this lack
of agreement across the individuals, allowing for nuance. In
particular, we argue that alignment methods should emulate
probabilistic Social Choice functions.
Definition 3. Given preferences {≻i}i∈P, a probabilistic
Social Choice function, returns a distribution over alterna-
tives Y.
Finally, we argue that an alignment method should be robust
against irrelevant alternatives whenever possible. The prop-
erty, independence of irrelevant alternatives states that the
3


Page 4:
Jackpot! Alignment as a Maximal Lottery
relative ranking of two alternatives should not be effected
by the presence or absence of a third, irrelevant alternative.
Definition 4. A Social Choice function f satisfies IIA if
its choice between any two alternatives a and b depends
only on how individuals rank a and b relative to each other,
and not on how they rank other alternatives. Formally:
∀a, b ∈Y,
∀profiles {≻i}, {≻′
i},
if a ≻i b ⇐⇒a ≻′
i b, ∀i ∈P,
then the Social Choice from those two profiles is the same
whenever it concerns choosing between a and b. That is,
if in the first profile f({≻i}) is a (or b), changing only
preferences involving alternatives other than a and b cannot
change whether f selects a or b.
4. Standard RLHF Does Not Satisfy Desired
Properties
In the previous section we proposed a set of properties that
we believe alignment methods for LLMs should exhibit. In
this section we show that current RLHF methods based on
the Bradley-Terry model do not satisfy any of the properties,
thereby raising the questions—previously noted by others
(Chen et al., 2024)—regarding their suitability for alignment
problems. While this section builds intuition on simplistic
examples, in Section 6.3 we further support our findings
with experimental results.
To build intuition, in the following we ignore the prompt,
and consider a scenario with only three possible options: R,
G and B. Relying on the fact that RLHF emulates Borda
count (Siththaranjan et al., 2024), we also assume that the
LLM post-trained using standard RLHF gives probability
close to one to whichever single-token word had the highest
win-rate comparison. Of course, in a realistic scenario the
LLM would only provide probability close to one if the
KL regularization term from the loss is made negligible,
either by training for long enough or by giving it a small
weight. However, we argue that, if anything, this raises
a new concern: through RLHF, a practitioner is aligning
the LLM to behave in a middle point between a pretrained
model which only cares about what is the probability of the
next output (which lacks alignment guarantees) and a model
that gives probability one to the token that has the highest
win-rate in a preference dataset.
RLHF is not Majority Consistent nor Condorcet
Consistent:
We showed that RLHF is not Majority
consistent in Section 3.1. Similarly it is not Condorcet
consistent. In the example shown in Figure 1, the Condorcet
winner is B. This is because, when B is compared with R,
three out of the five individual’s prefer B to R. Similarly
when B is compared to G, three out of the five individuals
prefer B to G. However, since RLHF emulates Borda, the
Preference
Ana
Bob
Carla
Dario
Eve
1st
R
R
B
B
B
2nd
B
B
R
R
R
(a) A simple scenario with just two colours.
Preference
Ana
Bob
Carla
Dario
Eve
1st
R
R
B
B
B
2nd
G
G
R
R
R
3rd
B
B
G
G
G
(b) Introduction of an irrelevant alternative G.
Table 2: Independence of Irrelevant Alternatives example.
(a) shows a simple scenario with a clear majority. (b) intro-
duces an irrelevant alternative G that should not change the
preference ranking.
resulting policy will be biased towards R.
RLHF is not Independent of Irrelevant Alternatives: To
explain the Independence of Irrelevant Alternatives (IIA),
let’s consider the simple scenario shown in Table 2a, with a
set of preferences over two alternatives, R and B. Clearly, the
aggregated preference ranking is that B is socially preferred
to R, and standard RLHF would align a model to most
likely return B. Now imagine that a third alternative G is
introduced (Table 2b). This addition doesn’t change the
relative ranking of B with respect to R for any individual
in the population. If RLHF was independent of irrelevant
alternatives, R would continue to be lower ranked (and thus
be assigned lower reward when learning a policy) than B.
However, akin to the case of Figure 1, this is not the case
and RLHF would assign highest reward to R.
Cyclic Preferences: Collections of preferences that exhibit
cycles, such as those shown in Table 1, can be challenging.
In these cases there is no Condorcet winner, and Borda
is unable to distinguish between the alternatives without
relying on some tie-breaking method.
Concretely, due to the stochastic nature of training, RLHF
would likely lead to one of the options (say, G) having
slightly higher reward. This would bias the LLM toward
that option, even though it is not genuinely superior and a
uniform distribution would be more aligned. Regularization
techniques like early stopping or KL penalization can lessen
this problem, at the expense of keeping the final distribu-
tion closer to the original pre-trained model, which is not
necessarily aligned.
4


Page 5:
Jackpot! Alignment as a Maximal Lottery
5. Using Maximal Lotteries to Align LLMs
Having established the shortcomings of Bradley-Terry based
RLHF, the questions becomes "Is there an alternative ap-
proach?". We answer in the affirmative. In particular, we
argue that a probablistic Social Choice function, maximal
lotteries, is particularly well suited for alignment of LLMs.
5.1. Maximal Lotteries
Given a set of preferences, a Probabilistic Social Choice
function returns a distribution over alternatives, called a
lottery. One particular Probabilistic Social Choice function
is the maximal lottery (Kreweras, 1965; Fishburn, 1984a).
Define ∆(Y) as the set that contains all distribution (i.e.
lotteries) over the options Y. A maximal lottery, π ∈∆(Y),
is one that is (weakly) preferred to any other lottery: namely
πT Mπ′ ≥0, ∀π′ ∈∆(Y),
(1)
where M is the pairwise margin matrix, where each entry
Mij represents the net margin of voters who prefer a over b:
Mij = N(a, b) −N(b, a).
Equivalently, one can view M as the payoffs of a carefully
constructed symmetric zero-sum margin game where the
payoffs are win or loss magnitudes of different pairwise
comparisons. The maximal lottery is, thus, the mixed max-
imin (or Nash equilibrium) solution to the game, and can
be computed via linear programming in polynomial time
(Brandl et al., 2022).
Maximal lotteries (ML) exhibit a number of interesting
properties. First, they require little structure to be placed on
voters’ preferences since M is computed solely using pair-
wise comparisons. This makes them particularly well suited
for current LLM alignment processes where preference data
typically takes this form.
Second, they are Condorcet-consistent and Majority-
consistent, in that alternatives in the support of the maximal
lottery are the Condorcet winner. They also provide a level
of protection against irrelevant alternatives through both be-
ing clone-consistent (see Appendix A.2) and independent of
irrelevant alternatives (in a probabilistic sense, see Brandl &
Brandt (2020); Brandl et al. (2016) and Appendix A.3), and
are able to handle cyclic preferences in a principled manner.
Maximal lotteries, in essence, aim to maximize the probabil-
ity of selecting an alternative that would win in a pairwise
majority comparison against any other alternative. This
captures a strong notion of collective preference, prioritiz-
ing options that are most likely preferred by a majority of
individuals. If there is a clear winner (i.e. there is a Con-
dorcet winner), then Maximal Lotteries will give probability
one to that option. When there is debate among a few of
options, Maximal Lotteries will return a distribution over
those options.
5.2. Using Maximal Lotteries to Align LLMs.
We believe that emulating Maximal Lotteries with LLMs
holds significant potential as a solution to the alignment
problem, as it has been shown to be the only probabilis-
tic Social Choice function that satisfies the key desiderata
of Arrow’s Impossibility Theorem in a stochastic setting
(Brandl & Brandt, 2020). This ensures that the LLM’s out-
put respects fundamental Social Choice principles.
The crucial question, then, is how to train an LLM to behave
like a Maximal Lottery. This can be achieved with the
following objective function:
Theorem 1. Let Y be the set of all possible statements
up to a finite maximum length L. Let π and π′ represent
two policies (i.e., LLMs). For two statements a, b ∈Y,
let P(a ≻b) be the probability that a random individ-
ual picked uniformly from society prefers a over b. Let
P(a ∼b) be the analogous quantity, but for indifference.
Then, the solution π∗to the following maximin optimization
problem
max
π
min
π′
X
a∈Y
X
b∈Y
π(a)

P(a ≻b) + 1
2P(a ∼b)

π′(b) (2)
is the Maximal Lottery for the Social Choice problem de-
fined by the set of alternatives Y and the population’s prefer-
ences over these alternatives. (See proof in Appendix A.5.)
Beyond the properties highlighted earlier, Maximal Lotter-
ies possess other desirable Social Choice characteristics like
participation (Brandl et al., 2019) and reinforcement (Brandl
et al., 2016).
5.3. Maximal Lotteries and the Connection with Nash
Learning From Human Feedback
The objective function presented in Theorem 1 bears a strik-
ing resemblance to the optimization process employed in
Nash Learning from Human Feedback (NLHF) (Munos
et al., 2023). NLHF aims to find a policy π that maximizes
its expected reward against an adversarial policy π′:
max
π
min
π′
X
a∈Y
X
b∈Y
π(a)P(a ≻b)π′(b),
(3)
where P(a ≻b) represents the probability that a human
prefers statement a over b. The key difference between
this NLHF formulation and our proposed objective function
is the term 1
2P(a ∼b), which accounts for cases where
individuals are indifferent between two options.
This difference highlights a crucial aspect of human prefer-
ences: indifference. While standard NLHF focuses solely
on strict preferences, our formulation acknowledges that
individuals may be equally satisfied with multiple options.
5


Page 6:
Jackpot! Alignment as a Maximal Lottery
However, in practical scenarios, we often only have access
to data reflecting which option a user selected in a pairwise
comparison, rather than their true underlying preference.
Let’s then define ˜P(a ≻b) as the probability that an individ-
ual has selected option a when presented with both options
{a, b} . This selection probability can be influenced by var-
ious factors, including presentation bias (e.g., users might
tend to select the first option presented, like in Craswell
et al. (2008) and Wang et al. (2018)). However, under the
assumption that individuals facing indifference choose ran-
domly between the options (which we argue is reasonable
if we mitigate the bias by randomizing the order of the two
sentences in each datapoint), we can show that maximiz-
ing the NLHF objective with the selection probability still
converges to the Maximal Lottery:
Corollary 1.1. Assume that when individuals are in-
different between two options they are equally likely
to select either option in a pairwise comparison, i.e.,
˜P(a
≻
b) = P(a ≻b) + 1
2P(a ∼b). Then, solv-
ing maxπ minπ′
P
a∈Y
P
b∈Y π(a) ˜P(a ≻b)π′(b) also
yields the Maximal Lottery.
This corollary shows the robustness of our approach. Even
with noisy data, reflecting selection probabilities rather than
true preferences, the optimization process can still recover
the desirable properties of the Maximal Lottery. It is impor-
tant to note, however, that position bias in pairwise compar-
isons should be considered and mitigated.
6. Experiments
In this section, we compare RLHF with algorithms designed
to emulate Maximal Lotteries, evaluating their performance
across key Social Choice properties. Specifically, we test
whether RLHF fails to satisfy majority rule, Condorcet con-
sistency, and independence of irrelevant alternatives (IIA),
and whether it struggles with non-transitive aggregate prefer-
ences, and conduct the same analysis for Maximal Lotteries.
Full implementation details, including hyperparameters and
training configurations, are provided in Appendix A.8. We
also note that the literature of NLHF has already compared
their methods with RLHF algorithms. We provide a sum-
mary of their results in Appendix A.10
6.1. Experimental Methodology
To evaluate the performance of Maximal Lotteries against
RLHF, we employ synthetic datasets designed to mimic
the structure of real-world preference data commonly used
in RLHF training. These synthetic datasets allow for con-
trolled experimentation and enable a precise analysis of the
properties discussed in Sections 4 and 5. Our synthetic
datasets consist of triplets: ‘<prompt>, <preferred option>,
<rejected option>‘. The prompt remains constant across all
datasets, and requires the model to choose a favourite colour
from three choices, "red", "blue" or "green", which form the
set of possible options (alternatives) Y.
To generate a dataset, we first define a population char-
acterized by a probability distribution P over the set of
preferences over the alternatives Y. This distribution rep-
resents the underlying preferences of the population. For
example, consider a population split in 2 groups, A and
B, with 60% of the population belonging to A who pre-
fer (R ≻A B ≻A G) and the remainder (B) who prefer
(B ≻B R ≻B G), like in Figure 1.
We then iteratively generate 2048 datapoints in three steps:
we first sample two distinct alternatives uniformly from Y
without replacement; we then sample an individual from
the population P; and finally we determine the preferred
and rejected option according to the individual’s preference,
and record them as a new dataset row. By varying the pref-
erences, the population distribution P and the dataset size,
we can generate datasets exhibiting different preference pat-
terns. In all our experiments, we sampled 2048 datapoints.
6.2. Models
For our experiments we start from three distinct copies
of the pretrained Gemma 2 2b model (Team et al., 2024)
without instruction tuning. We train one policy (RLHF pol-
icy) using Proximal Policy Optimization (PPO) (Schulman
et al., 2017), as explained in Section 2.1, and a second
policy (max-lottery policy) using Self-Play Preference Op-
timization (SPO) (Swamy et al., 2024), which belongs to
the family of algorithms that emulate a Maximal Lottery
policy. Finally, we use the last copy of the model as the
RLHF reward model.
RLHF policy (PPO): We fine-tune the reward model on the
synthetic dataset of human preferences described previously
and use it to assign a score to every LLM response. This
score guides the policy during reinforcement learning.
Maximal Lottery policy (SPO): This model is optimized
using the objective function presented in Theorem 1 (Section
5) with the SPO algorithm on the same human preference
dataset used to train the RLHF reward model. The details
of the algorithms, the choice of hyperparameters and their
implementation can be found in Appendix A.8.
6.3. Results
This section reports the comparisons of RLHF and Maximal
Lotteries based algorithms on the synthetic dataset described
in Section 6.1, simulating the cases introduced in Section 4.
6


Page 7:
Jackpot! Alignment as a Maximal Lottery
Figure 2: Simulations results Left column: Populations simulate preferences from Figure 1 and Table 2b (2x(R ≻G ≻
B), 3x(B ≻R ≻G)). Middle column: Populations mirror Table 2a preferences (2x(R ≻B), 3x(B ≻R)). Right
column: Populations exhibit cyclical preferences from Table 1 (1x(R ≻G ≻B), 1x(G ≻B ≻R), 1x(B ≻R ≻G)).
6.3.1. EXPERIMENT 1: MAJORITY AND CONDORCET
In this experiment (left column of Figure 2), we impose
a distribution of the population equivalent to that of Fig-
ure 1. The majority alternative is B. However, as predicted,
RLHF assigns probability close to 1 to the alternative R.
Instead, the maximal lotteries inspired method converges to
the preferred alternative B with probability close to one.
6.3.2. EXPERIMENT 2: INDEPENDENCE OF IRRELEVANT
ALTERNATIVES (IIA)
To evaluate whether RLHF and Maximal Lottery methods
respect the Independence of Irrelevant Alternatives (IIA)
property, we simulated the scenario described in Tables 2a
and 2b, where preferences among options shift due to the
introduction of an irrelevant alternative. Specifically, we
used synthetic preference datasets representing two cases:
one with three alternatives (R, B, and G), which coincides
with the experiment in Section 6.3.1, and one with only two
alternatives (R and B).
The center column of Figure 2 (with two alternatives) and
the left column (with three alternatives), reveal that RLHF
violates the IIA property. Indeed, in the two-alternative
scenario, the RLHF-trained policy assigns near-zero proba-
bility to R, favoring the majority winner B instead. However,
in the three-alternative case, RLHF reverses this decision,
giving almost all probability to R.
In contrast, the Maximal Lottery approach maintains a stable
output distribution across the two scenarios. Regardless of
whether G is included, the probability assigned to R and B
remains consistent, close to 1 for B, showing that Maximal
Lottery methods satisfy the IIA property.
6.3.3. EXPERIMENT 3: CYCLIC PREFERENCES
In this experiment, we impose the population distribution of
Table 1. As it can be seen in the right column of Figure 2,
the maximal lotteries inspired method converges to an LLM
that returns each of the colours B, R and G approximately
33% of the time.
In contrast, the policy trained with RLHF converges to a
policy that returns one arbitrary colour (in this particular
simulation G) with probability one.
7. Related Work
This work builds upon several areas at the intersection of
AI alignment and Social Choice Theory. Traditional ap-
proaches such as Reinforcement Learning from Human
Feedback (RLHF) have become the de-facto standard (Chris-
tiano et al., 2017; Stiennon et al., 2020) to finetune LLMs.
While RLHF has proven effective for guiding LLMs, recent
studies have highlighted its limitations (Siththaranjan et al.,
2024; Casper et al., 2023; Ge et al., 2024).
Recent research has explored the application of Social
Choice Theory to address the AI alignment problem. Papers
such as (Ge et al., 2024; Dai & Fleisig, 2024; Mishra, 2023;
Conitzer et al., 2024) argue for viewing alignment as a So-
7


Page 8:
Jackpot! Alignment as a Maximal Lottery
cial Choice Theory problem, which allows the application
of well-established Social Choice functions to aggregate
human preferences.
Recent results identify Maximal Lotteries as the unique
probabilistic voting system satisfying Arrow’s axioms
(Brandl & Brandt, 2020), which has motivated its use in
different areas of Machine Learning (Lanctot et al., 2023).
Finally, this work also connects with the emerging field
of Nash Learning with Human Feedback (NLHF) (Munos
et al., 2023; Calandriello et al., 2024; Swamy et al., 2024),
which proposes alternatives to RLHF based on an optimza-
tion process inspired by Game Theory.
8. Limitations and future work
Our proposed framework, while offering a robust theoret-
ical foundation for aligning LLMs with aggregate human
preferences, faces some limitations that require further in-
vestigation.
A central challenge lies in the estimation of P(a ≻b|x),
particularly in two key points: 1) what do we mean when
we say that an individual i prefers a to b (a ≻i b); and 2)
how do we capture that the preferences depend, not only on
the prompt x, but on the context.
On the first point, what is the correct interpretation that an
individual prefers an option a with respect to another b?
How realistic is it to assume that it is possible to estimate
the preferences of an individual by showing them pairs of
sentences, that is the standard practice nowadays? Are there
better ways to infer preferences? On this issue, we point
to the reader to Gabriel (2020) for an extensive discussion.
Microeconomic theory and Industrial Organization theory
has a history of attacking similar problems and could be a
promising avenue to solve them.
Secondly, the appropriateness of a response can vary signif-
icantly depending on the context in which a conversation
takes place. An answer that is perfectly acceptable in a com-
edy show might be entirely inappropriate in a professional
setting. Therefore, it is crucial to explore methods that allow
large language models (LLMs) to incorporate contextual
information when generating responses. Developing strate-
gies to enhance context awareness in LLMs is an important
step toward more reliable and nuanced AI interactions. For
a more in-depth discussion on the theory of appropriateness,
we refer readers to Leibo et al. (2024).
Another important avenue for future work is the develop-
ment of an online version of our approach that continuously
updates and adapts to changes in societal preferences. Hu-
man values and societal norms evolve over time, and a static
alignment approach may become outdated or fail to reflect
current ethical considerations. An online adaptation mech-
anism would allow the model to integrate new preference
data dynamically, ensuring that its responses remain aligned
with contemporary views while avoiding abrupt shifts that
could lead to instability or exploitation by adversarial ac-
tors. We believe that developing online voting mechanisms
that approximate maximal lotteries, such as those explored
in (Brandl & Brandt, 2024), is a promising direction for
achieving this goal.
Addressing these previous points is crucial for realizing the
full potential of our framework. By combining rigorous
Social Choice principles with advanced machine learning
techniques, we can strive to develop LLMs that are more
reliably and ethically aligned with the diverse values and
preferences of humanity.
9. Conclusion
This paper examines the limitations of RLHF in aligning
LLMs with aggregate human preferences, demonstrating its
vulnerability to violations of key Social Choice principles,
and proposing an alternative framework grounded in Max-
imal Lotteries. We establish a formal connection between
this optimal voting system, known to be the only probabilis-
tic voting system that circumvents Arrow’s impossibility
theorem, and Nash Learning from human feedback (NLHF)
algorithms, offering a practical path for training LLMs that
robustly reflect collective human preferences. Our experi-
mental results confirm that methods that emulate Maximal
Lotteries, like NLHF and variantes, can overcome the short-
comings of RLHF, yielding LLM whose responses better
align with the majority’s will. This includes supporting the
preferences of the majority, providing principled ways of
handling non-transitivities in the preference data, and inde-
pendence of irrelevant alternatives. The shift from simple
reward maximization to a framework rooted in the rich the-
oretical foundations of Social Choice Theory promises a
more nuanced and robust approach to aligning LLMs with
human values, ultimately contributing to the development
of AI systems that truly serve humanity’s best interests.
Impact Statement
Ensuring that AI systems are aligned with diverse human
values and preferences is critical for the future of society.
The growing influence of AI in decision-making processes,
from healthcare to education, emphasizes the importance
of considering and valuing everyone’s preferences. By in-
tegrating techniques that emulate Maximal Lotteries, we
provide a robust framework for AI alignment, addressing
key limitations of existing methods, such as RLHF. However,
achieving true alignment also requires accurately estimating
individual preferences and tackling challenges like reward
hacking. Additionally, the datasets used to estimate these
8


Page 9:
Jackpot! Alignment as a Maximal Lottery
preferences must be created with a representative sample of
the population to ensure fairness and inclusivity. If these
issues are not tackled, we could end up aligning LLMs to
the wrong set of values and preferences, which could have
harmful unintended consequences with highly capable AI
systems.
References
Anil, R., Dai, A. M., Firat, O., Johnson, M., Lepikhin,
D., Passos, A., Shakeri, S., Taropa, E., Bailey, P., Chen,
Z., et al.
Palm 2 technical report.
arXiv preprint
arXiv:2305.10403, 2023.
Anthropic.
Introducing
Claude,
2023.
URL
https://www.anthropic.com/index/
introducing-claude.
Arrow, K. J. A difficulty in the concept of social welfare.
Journal of political economy, 58(4):328–346, 1950.
Balduzzi, D., Garnelo, M., Bachrach, Y., Czarnecki, W. M.,
Perolat, J., Jaderberg, M., and Graepel, T. Open-ended
learning in symmetric zero-sum games. In Thirty-sixth
International Conference on Machine Learning, 2019.
Baumler, C., Sotnikova, A., and Daumé III, H. Which ex-
amples should be multiply annotated? Active learning
when annotators may disagree. In Findings of the As-
sociation for Computational Linguistics: ACL 2023, pp.
10352–10371, Toronto, Canada, July 2023. Association
for Computational Linguistics. doi: 10.18653/v1/2023.
findings-acl.658.
URL https://aclanthology.
org/2023.findings-acl.658/.
Bertand, Q., Czarnecki, W. M., and Gidel, G. On the lim-
itations of the elo: Real-world games are transitive, not
additive. arXiv preprint arXiv:2206.12301, 2023.
Brandl, F. and Brandt, F. Arrovian aggregation of convex
preferences. Econometrica, 88(2):799–844, 2020.
Brandl, F. and Brandt, F. A natural adaptive process for
collective decision-making. Theoretical Economics, 19
(2):667–703, 2024.
Brandl, F., Brandt, F., and Seedig, H. G. Consistent proba-
bilistic social choice. Econometrica, 84(5):1839–1880,
2016.
Brandl, F., Brandt, F., and Hofbauer, J. Welfare maximiza-
tion entices participation. Games and Economic Behavior,
114:308–314, 2019.
Brandl, F., Brandt, F., and Stricker, C. An analytical and
experimental comparison of maximal lottery schemes.
Social Choice and Welfare, 58(1):5–38, 2022.
Brandt, F., Conitzer, V., Endriss, U., Lang, J., and Procac-
cia, A. D. Handbook of computational social choice.
Cambridge University Press, 2016.
Calandriello, D., Guo, D., Munos, R., Rowland, M., Tang,
Y., Pires, B. A., Richemond, P. H., Lan, C. L., Valko, M.,
Liu, T., et al. Human alignment of large language models
through online preference optimisation. arXiv preprint
arXiv:2403.08635, 2024.
Casper, S., Davies, X., Shi, C., Gilbert, T. K., Scheurer,
J., Rando, J., Freedman, R., Korbak, T., Lindner, D.,
Freire, P., Wang, T. T., Marks, S., Segerie, C.-R., Car-
roll, M., Peng, A., Christoffersen, P. J., Damani, M.,
Slocum, S., Anwar, U., Siththaranjan, A., Nadeau, M.,
Michaud, E. J., Pfau, J., Krasheninnikov, D., Chen, X.,
Langosco, L., Hase, P., Biyik, E., Dragan, A., Krueger,
D., Sadigh, D., and Hadfield-Menell, D. Open problems
and fundamental limitations of reinforcement learning
from human feedback. Transactions on Machine Learn-
ing Research, 2023. ISSN 2835-8856. URL https://
openreview.net/forum?id=bx24KpJ4Eb. Sur-
vey Certification, Featured Certification.
Chen, A., Malladi, S., Zhang, L. H., Chen, X., Zhang, Q.,
Ranganath, R., and Cho, K. Preference learning algo-
rithms do not learn preference rankings, 2024. URL
https://arxiv.org/abs/2405.19534.
Christiano, P. F., Leike, J., Brown, T., Martic, M., Legg,
S., and Amodei, D. Deep reinforcement learning from
human preferences. Advances in neural information pro-
cessing systems, 30, 2017.
Conitzer, V., Freedman, R., Heitzig, J., Holliday, W. H., Ja-
cobs, B. M., Lambert, N., Mossé, M., Pacuit, E., Russell,
S., Schoelkopf, H., et al. Position: Social choice should
guide AI alignment in dealing with diverse human feed-
back. In Forty-first International Conference on Machine
Learning, 2024.
Craswell, N., Zoeter, O., Taylor, M., and Ramsey, B. An
experimental comparison of click position-bias models.
In Proceedings of the 2008 International Conference on
Web Search and Data Mining, pp. 87–94, 2008.
Dai, J. and Fleisig, E. Mapping social choice theory to
RLHF. arXiv preprint arXiv:2404.13038, 2024.
de Condorcet, M. Essai sur l’application de l’analyse à la
probabilité des décisions rendues à la pluralité des voix,
1785.
Elo, A. E. The Ratings of Chess Players, Past and Present.
Arco Publishing, Inc., 2nd edition, 1978.
9


Page 10:
Jackpot! Alignment as a Maximal Lottery
Felsenthal, D. S. Review of paradoxes afflicting procedures
for electing a single candidate. In Electoral systems: Para-
doxes, assumptions, and procedures, pp. 19–91. Springer,
2011.
Fishburn, P. C. Probabilistic social choice based on simple
voting comparisons. The Review of Economic Studies, 51
(4):683–692, 1984a.
Fishburn, P. C. Ssb utility theory: An economic perspective.
Mathematical Social Sciences, 8(1):63–94, 1984b.
Fishburn, P. C. and Brams, S. J. Paradoxes of preferential
voting. Mathematics Magazine, 56(4):207–214, 1983.
Gabriel, I. Artificial intelligence, values, and alignment.
Minds and machines, 30(3):411–437, 2020.
Ge, L., Halpern, D., Micha, E., Procaccia, A. D., Shapira,
I., Vorobeychik, Y., and Wu, J. Axioms for ai alignment
from human feedback. arXiv preprint arXiv:2405.14758,
2024.
Gibbard, A. Manipulation of voting schemes: a general
result. Econometrica: journal of the Econometric Society,
pp. 587–601, 1973.
Gibbard, A. Manipulation of schemes that mix voting with
chance. Econometrica: Journal of the Econometric Soci-
ety, pp. 665–681, 1977.
Google. Bard, 2023. URL https://bard.google.
com.
Hu, E. J., Shen, Y., Wallis, P., Allen-Zhu, Z., Li, Y., Wang,
S., Wang, L., and Chen, W. Lora: Low-rank adaptation of
large language models. arXiv preprint arXiv:2106.09685,
2021.
Kreweras, G. Aggregation of preference orderings. In
Mathematics and Social Sciences I: Proceedings of the
seminars of Menthon-Saint-Bernard, France (1–27 July
1960) and of Gösing, Austria (3–27 July 1962), pp. 73–79,
1965.
Lanctot, M., Larson, K., Bachrach, Y., Marris, L., Li, Z.,
Bhoopchand, A., Anthony, T., Tanner, B., and Koop, A.
Evaluating agents using social choice theory, 2023.
Leibo, J. Z., Vezhnevets, A. S., Diaz, M., Agapiou, J. P.,
Cunningham, W. A., Sunehag, P., Haas, J., Koster, R.,
Duéñez-Guzmán, E. A., Isaac, W. S., et al. A theory of
appropriateness with applications to generative artificial
intelligence. arXiv preprint arXiv:2412.19010, 2024.
Luce, R. D. Individual Choice Behavior, volume 4. Wiley
New York, 1959.
Mishra, A. AI alignment and social choice: Fundamen-
tal limitations and policy implications. arXiv preprint
arXiv:2310.16048, 2023.
Munos, R., Valko, M., Calandriello, D., Azar, M. G., Row-
land, M., Guo, Z. D., Tang, Y., Geist, M., Mesnard, T.,
Michi, A., et al. Nash learning from human feedback.
arXiv preprint arXiv:2312.00886, 2023.
OpenAI. GPT-4 technical report, 2023.
Rafailov, R., Sharma, A., Mitchell, E., Manning, C. D., Er-
mon, S., and Finn, C. Direct preference optimization:
Your language model is secretly a reward model. In Oh,
A., Naumann, T., Globerson, A., Saenko, K., Hardt, M.,
and Levine, S. (eds.), Advances in Neural Information
Processing Systems, volume 36, pp. 53728–53741. Cur-
ran Associates, Inc., 2023.
Rafailov, R., Sharma, A., Mitchell, E., Manning, C. D., Er-
mon, S., and Finn, C. Direct preference optimization:
Your language model is secretly a reward model. Ad-
vances in Neural Information Processing Systems, 36,
2024.
Ray, P. Independence of irrelevant alternatives. Economet-
rica: Journal of the Econometric Society, pp. 987–991,
1973.
Roberts, A., Chung, H. W., Mishra, G., Levskaya, A., Brad-
bury, J., Andor, D., Narang, S., Lester, B., Gaffney, C.,
Mohiuddin, A., et al. Scaling up models and data with
t5x and seqio. Journal of Machine Learning Research,
24(377):1–8, 2023.
Schaekermann, M., Goh, J., Larson, K., and Law, E.
Resolvable vs. irresolvable disagreement: A study on
worker deliberation in crowd work. Proc. ACM Hum.-
Comput. Interact., 2(CSCW), November 2018.
doi:
10.1145/3274423.
Schulman, J., Wolski, F., Dhariwal, P., Radford, A., and
Klimov, O. Proximal policy optimization algorithms.
arXiv preprint arXiv:1707.06347, 2017.
Shah, N. B. and Wainwright, M. J. Simple, robust and
optimal ranking from pairwise comparisons. 18(1):7246–
7283, 2017.
Siththaranjan, A., Laidlaw, C., and Hadfield-Menell, D.
Distributional preference learning: Understanding and
accounting for hidden context in RLHF. In The Twelfth
International Conference on Learning Representations
(ICLR), 2024.
URL https://arxiv.org/abs/
2312.08358.
Skalse, J. and Abate, A. Misspecification in inverse re-
inforcement learning, 2023. URL https://arxiv.
org/abs/2212.03201.
10


Page 11:
Jackpot! Alignment as a Maximal Lottery
Smith, J. H. Aggregation of preferences with variable elec-
torate. Econometrica: Journal of the Econometric Soci-
ety, pp. 1027–1041, 1973.
Stiennon, N., Ouyang, L., Wu, J., Ziegler, D., Lowe, R.,
Voss, C., Radford, A., Amodei, D., and Christiano,
P. F. Learning to summarize with human feedback. Ad-
vances in Neural Information Processing Systems, 33:
3008–3021, 2020.
Swamy, G., Dann, C., Kidambi, R., Wu, Z. S., and Agarwal,
A. A minimaximalist approach to reinforcement learning
from human feedback. arXiv preprint arXiv:2401.04056,
2024.
Team, G., Riviere, M., Pathak, S., Sessa, P. G., Hardin,
C., Bhupatiraju, S., Hussenot, L., Mesnard, T., Shahri-
ari, B., Ramé, A., et al. Gemma 2: Improving open
language models at a practical size.
arXiv preprint
arXiv:2408.00118, 2024.
Tideman, T. N. Independence of clones as a criterion for
voting rules. Social Choice and Welfare, 4(3):185–206,
1987.
Touvron, H., Lavril, T., Izacard, G., Martinet, X., Lachaux,
M.-A., Lacroix, T., Rozière, B., Goyal, N., Hambro,
E., Azhar, F., Rodriguez, A., Joulin, A., Grave, E., and
Lample, G. Llama: Open and efficient foundation lan-
guage models, 2023. URL https://arxiv.org/
abs/2302.13971.
Wang, X., Golbandi, N., Bendersky, M., Metzler, D., and
Najork, M. Position bias estimation for unbiased learning
to rank in personal search. In Proceedings of the Eleventh
ACM International Conference on Web Search and Data
Mining, pp. 610–618, 2018.
Xu, W., Dong, S., Lu, X., Lam, G., Wen, Z., and Van Roy,
B. RLHF and IIA: Perverse incentives. arXiv preprint
arXiv:2312.01057, 2023.
A. Appendix
A.1. Arrow’s Impossibility Theorem
In this section we will discuss Arrow’s Impossibility Theo-
rem (Arrow, 1950), arguably the most fundamental result in
Social Choice Theory. In this theorem, it is shown that, if
#Y ≥3, there is no deterministic voting system such that
it satisfies three basic properties: Independence of Irrelevant
Alternatives, Pareto Efficiency and Non-dictatorship.
Throughout this paper we have used Social Choice functions
for ease of exposition. However, this theorem is usually ex-
pressed using Social Welfare functions (SWF) F, i.e. maps
from preference profiles {≻i}i∈P to a ranking, ≻S. Note,
however, that any Social Welfare Function implicitly defines
a Social Choice function that returns the top ranked option.
The IIA property was explained in Section 2.2, but will
be re-expressed for SWFs. The last two properties will be
introduced later in this section.
A.1.1. IIA - SWF VERSION
Definition A social welfare function F satisfies IIA if:
∀a, b ∈Y,
∀profiles {≻i}, {≻′
i},
if a ≻i b ⇐⇒a ≻′
i b, ∀i ∈P,
then a ≻s b ⇐⇒a ≻′
s b,
where ≻s= F({≻i}i∈P) and ≻′
s= F({≻′
i}i∈P)
A.1.2. PARETO EFFICIENCY
Intuitively, if everyone prefers outcome x to y, then col-
lectively we should also prefer x over y. That property is
captured by Pareto Efficiency.
Definition (Pareto Efficiency for SWFs): A Social Welfare
function F is Pareto efficient if for any preference profile
{≻i}i∈P and for any two alternatives x, y ∈Y, if x ≻i y
for all i ∈P, then x ≻S y, where ≻S= F({≻i}i∈P).
Example: when choosing between chocolate and vanilla, if
everyone in a group prefers chocolate ice cream to vanilla,
choosing chocolate would be Pareto Efficient. Choosing
vanilla would not be, as everyone could be made better off
by switching to chocolate.
A.1.3. NON DICTATORSHIP
This property formalizes the intuitive idea that a dictator,
an individual that makes all collective decisions, is not a
desirable form of making choices.
Definition (non-dicatorship for SWFs): A Social Welfare
function F satisfies non-dictatorship if there is no individual
i (the dictator) such that for any preference profile {≻i}i∈P
∀x, y ∈Y, x ≻i y if and only if x ≻S y, where ≻S=
F({≻i}i∈P).
A.2. Social Choice Theory properties
In this section, we will list other sets of important properties
and paradoxes in Social Choice Theory.
Monotoniticy (Smith, 1973; Felsenthal, 2011): A Social
Choice function satisfies monotonicity if, whenever x is
elected under a distribution of voters’ preferences, x keeps
being elected if some voters increase their support for x (i.e.
x moves higher up in their ranking) keeping everything else
constant.
11


Page 12:
Jackpot! Alignment as a Maximal Lottery
No show paradox (Fishburn & Brams, 1983; Felsenthal,
2011) A voter could obtain a better outcome by not partici-
pating in the voting.
Strategic voting paradox (Gibbard, 1973; Felsenthal,
2011) A voter may obtain a better outcome if they strategi-
cally lie when reporting their preferences.
Clone-consistency (Tideman, 1987) This property is a
subcase of IIA. The addition of a clone to the set of options
(i.e. an option yc which is quite similar to another option y
in the set Y and thus is placed side by side in the rankings
of all voters) should not change the chosen candidate of the
Social Choice function.
A.3. Maximal Lotteries and Arrow’s theorem
This section will effectively be a summary of some of the
definitions and axioms from Brandl & Brandt (2020).
So far, individuals have a preference over the options Y.
In this section, we will extend those to preferences over
distributions (i.e. lotteries).
Let Y be a finite set of alternatives, and let ∆be the set
of all probability distributions over Y. An element p ∈
∆represents a lottery over alternatives in Y. Call P =
{1, . . . , n} the set of voters, and each voter has a preference
relation ⪰i over ∆.
Given p ∈∆, for i ∈P define:
• Ui(p) = {q ∈∆: q ≻i p} is the strict upper contour
set of p
• Li(p) = {q ∈∆: p ≻i q} is the strict lower contour
set of p
• Ii(p) = {q ∈∆: p ∼i q} is the indifference set of p.
For Z ⊆∆, ⪰|Z = {(p, q) ∈⪰: p, q ∈Z} is the prefer-
ence relation ⪰restricted to outcomes in Z.
A.3.1. ASSUMPTIONS ON INDIVIDUAL PREFERENCES
Each individual’s preferences ⪰i must satisfy:
Continuity: Intuitively, if p ≻i q, then small changes
in p or q will not reverse the preference. More formally,
Ui(p) and Li(p) are open.
Convexity: Intuitively, if p ≻i q, then any mixture r =
λp + (1 −λ)q (for 0 < λ < 1) is also preferred to q. More
formally:
Ui(p), Li(p), Ui(p) ∪Ii(p), and Li(p) ∪Ii(p) are convex.
Symmetry: Intuitively, as explained by (Fishburn, 1984b),
"the degree to which p is preferred to q is equal in magnitude
(but opposite in sign) to the degree to which q is preferred
to p". More formally:
∀p, q, r ∈∆, ∀λ ∈(0, 1)
if q ∼1/2 p + 1/2 r and pλr ∼1/2 p + 1/2 q
then rλp ∼1/2 r + 1/2 q.
(4)
where aλb := λa + (1 −λ)b, ∀a, b ∈∆.
A.3.2. ARROVIAN PROPERTIES
A Social Welfare function (SWF) F maps individual pref-
erences (⪰1, . . . , ⪰n) to the collective preference ⪰. In
this section, we will describe a generalization of Arrows
Impossibility Theorem’s main properties.
Independence of Irrelevant Alternatives (IIA) - Brandl
& Brandt (2020) version: Let Z ⊆Y be a subset of the
original options and ∆Z be the set of loteries over Z. A
SFW F satisfies IIA if and only if, for any two preference
profiles {⪰i}i∈P and {⪰′
i}i∈P, if
∀i ∈{1, . . . , n} (⪰i|∆Z = ⪰′
i|∆Z)
then
F(⪰1, . . . , ⪰n)|∆Z = F(⪰′
1, . . . , ⪰′
n)|∆Z
Pareto Efficiency - Brandl & Brandt (2020) version: Let
⪰= F(⪰1, . . . , ⪰n). We say that F is Pareto Efficient if,
whenever every individual prefers p to q (p ⪰i q for all
i), then p ⪰q collectively. If, additionally, there exist
individuals i ∈P such that they strictly prefer p to q (∃i ∈
P(p ≻i q)), then p ≻q.
Anonymity: The SWF treats all individuals symmetrically
(no individual’s preferences are given special weight). Note
that this is stronger than non-dictatorship.
More formally: Let π be a permutation of the voters P.
Then a SWF F satisfies Anonymity if
F(⪰1, . . . , ⪰n) = F(⪰π(1), . . . , ⪰π(n))
Maximal Lotteries: It has been proved that under Continu-
ity, Convexity, Symmetry and other technical assumptions,
there exist a unique SWF F that satisfies IIA, Anonymity
and Pareto Efficiency (Brandl & Brandt, 2020). The Proba-
bilistic Social Choice function ρ that outputs the first lottery
of the ranking returned by SWF F is precisely the Maximal
Lottery.
A.4. Relevance of Condorcet and Majority in Text data:
Smith sets
A potential objection to applying Condorcet criteria to
LLMs is the sheer scale of the output space. With all possi-
ble statements up to a certain length as alternatives, it seems
12


Page 13:
Jackpot! Alignment as a Maximal Lottery
unlikely that a single statement would emerge as a Con-
dorcet winner, preferred by a majority over every other pos-
sible statement. However, this vastness doesn’t negate the
relevance of Condorcet principles. Instead, we can consider
the concept of Smith Sets, which offers a generalization of
Condorcet winners. A Smith Set is the smallest non-empty
set of alternatives such that every alternative within the set
beats every alternative outside the set in a pairwise majority
vote. Critically, a Smith Set always exists.
Imagine, for instance, an LLM responding to the prompt
"Summarize the French Revolution". While no single sum-
mary might be universally preferred, a Smith Set could
comprise a collection of summaries deemed superior by a
majority to any summary outside this set. This set would
capture a core of high-quality summaries reflecting the ma-
jority’s preferences, even if individuals disagree on the nu-
ances within the set. As long as the output is contained in
the Smith set, that would be adequate.
Therefore, while a strict Condorcet winner might be rare
in the LLM context, focusing on properties like Condorcet
consistency and Majority, which are closely related to Smith
Sets, ensures that the LLM prioritizes outputs preferred by a
majority to a significant portion of alternatives, thus aligning
with a robust notion of collective preference.
A.5. Proof of the main theorem
In this section we will prove the main theorem of the paper.
The notation has been slightly changed to make the proof
easier to follow (we substitute a with yi and b with yj).
Theorem. Let Y be the set of all possible statements with a
number of tokens smaller than a predetermined maximum
length L. Let π and π′ represent two policy LLMs. For two
statements yi, yj ∈Y, let P(yi ≻yj) be the probability that
a random individual picked uniformly from society prefers
yi over yj. Let P(yi ∼yj) be the analogous quantity, but
for indifference.
Then, the solution π∗to the following maximin optimization
problem:
max
π
min
π′
X
yi∈Y
X
yj∈Y
π(yi)

P(yi ≻yj) + 1
2P(yi ∼yj)

π′(yj)
is the Maximal Lottery for the Social Choice problem de-
fined by the set of alternatives Y and the population’s pref-
erences over these alternatives.
Proof. First, some notation. Define :
• n is the amount of elements in the population.
• m is the amount of elements in #Y.
• N as the matrix that indicates number of people who
prefer statement yi to yj N := (#{k : yi ≻k yj})i,j
• E as the matrix that indicates number of people who
are indifferent between statement yi to yj E := (#{k :
yi ∼k yj})i,j
• The Margin matrix M := N −N T
• ˜N as the matrix that indicates proportion of peo-
ple who prefer statement yi to yj , i.e.
˜N
=
(P(yi ≻yj))i,j = N/n.
• ˜E as the matrix that indicates proportion of people
who are indifferent between statement yi and yj , i.e.
˜E = (P(yi ∼yj))i,j = N/n.
• The proportion margin matrix ˜
M = M/n
Note how N, E, M, ˜N, ˜E and ˜
M are all matrices of shape
m × m.
Define also the matrix of all ones as:
Jm =



1
· · ·
1
...
...
...
1
· · ·
1



m×m
Observe that
P(yj ≻yi) = 1 −P(yi ⪰yj)
= 1 −P(yi ≻yj) −P(yi ∼yj)
Therefore
˜N T = Jm −(P(yi ≻yj))i,j −(P(yi ∼yj))i,j
(5)
= Jm −˜N −˜E
(6)
Thus,
˜
M = ˜N −˜N T
(7)
= ˜N −(Jm −˜N −˜E)
(8)
= 2 ˜N −Jm + ˜E
(9)
Finally, note that for any probability vectors p, q ∈∆(Y) ,
then
pT Jmq = ⟨(
m
X
i=1
pi, ...,
m
X
i=1
pi), q⟩
(10)
= ⟨(1, ..., 1), q⟩
(11)
=
m
X
i=1
qi
(12)
= 1
(13)
A lottery π is maximal if πT M ≥0,. In other words, no
other lottery π′ is preferred by an expected majority of
voters (πT Mπ′ ≥0).
13


Page 14:
Jackpot! Alignment as a Maximal Lottery
The maximal lottery can also be calculated as the solution
from the following optimization problem:
max
π
min
π′
πT Mπ′
From there,
π∗= arg max
π
min
π′
πT Mπ′
= arg max
π
min
π′
πT M
n π′
(a)
= arg max
π
min
π′
πT ˜
Mπ′
(b)
= arg max
π
min
π′
πT (2 ˜
N −Jm + ˜E)π′
(c)
= arg max
π
min
π′
2πT ˜
Nπ′ −πT Jmπ′ + πT ˜Eπ′
= arg max
π
min
π′
2πT ˜
Nπ′ −1 + πT ˜Eπ′
(d)
= arg max
π
min
π′
2πT ˜
Nπ′ + πT ˜Eπ′
(e)
= arg max
π
min
π′
πT ˜
Nπ′ + 1
2πT ˜Eπ′
(f)
= arg max
π
min
π′
πT (P(yi ≻yj))i,jπ′
+ 1
2πT (P(yi ∼yj))i,jπ′
= arg max
π
min
π′
X
yi∈Y
X
yj∈Y
π(yi)P(yi ≻yj)π′(yj)
+
X
yi∈Y
X
yj∈Y
π(yi)1
2P(yi ∼yj)π′(yj)
(g)
• (a): Dividing by constant does not change solution
• (b): Change notation
• (c): Using Equation (9)
• (d): Using Equation (13)
• (e): Subtracting constant does not change anything
• (f): Dividing by constant does not change solution
• (g): Expand terms
The last term can easily be rearranged to get our result. This
ends our proof.
A.6. Random dictatorships and pretrained LLMs
In this section, we highlight a connection between the be-
havior of pretrained LLMs and a well-known probabilistic
Social Choice function: random dictatorships.
A random dictatorship selects a single individual from
the population at random and implements their top-ranked
choice (Gibbard, 1977). Pretrained LLMs, which approxi-
mate the probability of the next token based on the distribu-
tion of text in their training data, can be seen as implicitly
implementing a form of random dictatorship. In this view,
the "voters" are the users who contributed to the dataset,
and their influence is weighted by the volume of text they
generated. This suggests that before fine-tuning, LLMs may
already reflect an aggregation of individual preferences, al-
beit in a way that is biased by data distribution rather than
designed to satisfy desirable Social Choice properties.
A.7. The multiple definitions of IIA
Recent results in the literature have pointed out that RLHF
satisfies IIA (Xu et al., 2023). This might be confusing for
some readers, as we have precisely argued that RLHF does
not satisfy IIA. The reason is that, regretably, the concept of
IIA is used to refer to very different properties in different
fields. For clarification, we point to the reader towards Ray
(1973).
In Xu et al. (2023), the issue with IIA is raised intuitively
in their paper in the following way: assume that individu-
als have to choose what they prefer between cats, felines
and dogs. In this example, cats and felines are synonyms.
Thus, if we add the word feline to our set of possible con-
siderations, that should only affect the probability of re-
turning the word cat, but should not affect the probability
of returning the word dog. That is: P(Y =dog|Y={dog, cat})
P(Y =cat|Y={dog, cat}) =
P(Y =dog|Y={dog, cat, feline})
P(Y ∈{cat, feline}|Y={dog, cat, feline}).
More formally, let M be the set of all messages and
X, X ′ ⊆M are some possible subsets of that set of words.
Let x ∈M be a message. Let P(Y = x | Y = X) be the
proportion of individuals who prefer the message x over all
other messages in the set X
Then, in Xu et al. (2023), the IIA definition is inspired
by the definition from Luce (1959): IIA-Luce means that
for all messages x, x′ ∈M and sets X and X ′ such that
x, x′ ∈X ∩X ′,
P(Y = x | Y = X)
P (Y = x′ | Y = X) = P (Y = x | Y = X ′)
P (Y = x′ | Y = X ′)
It is worth mentioning that this property is connected to
the property of composition consistency, which has been re-
cently shown to be a property of Maximal Lotteries (Brandl
et al., 2016).
A.8. Experimental details and hyperparameters
The two prompts used in our experiments were the follow-
ing:
14


Page 15:
Jackpot! Alignment as a Maximal Lottery
Prompt (IIA-2 options)
"""
Q: What is your favorite color from
the options red and blue?
answer in the format ’My favourite
color is the color red.’ or
’My favourite color is the color
blue.’ and say nothing else after
that. \n"
A: My favourite color is the color
"""
Prompt (all other experiments)
"""
Q: What is your favorite color from
the options red, blue and green?
answer in the format ’My favourite
color is the color red.’ ’My favourite
color is the color blue.’ or
’My favourite color is the color
green.’ and say nothing else after
that. \n
A: My favourite color is the color
"""
The distributions over the preferences of the population
were defined in ways similar to the following example:
rankings = {
"voter_0": [R, G, B],
"voter_1": [G, B, R],
"voter_2": [B, R, G]
}
# Example probabilities
p = [0.33, 0.33, 0.34]
All three copies of the Gemma model were trained using
LoRA (Low-Rank Adaptation of Transformers) (Hu et al.,
2021) with the following configuration:
• Rank (r): 8
• Alpha: 32
• Dropout: 0.1
Maximal Lottery Policy (SPO):
See Algorithm 1 for
a pseudocode implementation of SPO. For the Maximal
Lottery experiments, the following hyperparameters were
used to train the policy using the SPO:
• RL step of SPO: we use the PPO algorithm
• Epochs: 30
Algorithm 1 SPO algorithm implementation
Input: Iterations T, Preference fn. P, Num. samples
k ≥2, Fix prompt x
Output: Trained policy π
Initialize π1 ∈Π.
for i = 1 to T do
si = x
Sample a1:k ∼πt(si)
Compute ri =
1
k−1
Pk
j̸=i P (ai ≻aj).
D = {(si, ai, ri)}i∈[k]
πt+1 ←RL-PPO (πt, D).
end for
Return: uniform mixture of π1:T .
• Batch size: 128
• Mini-batch size: 32 (split from the main batch)
• Learning rate: 1 × 10−4
• Value function coefficient (vf_coef): 0.0
• Initial KL coefficient (init_kl_coef): 0.0
• Gamma patience: 0.0 (used to estimate the value
function)
• Entropy coefficient: Increased to ensure exploration
during training.
• Epochs: 30
• Dataset size: 211 (2048) data points.
To help with the training, we enforce that 10% of the batch is
a uniform sample of the three colour words " red", " green",
" blue".
Preference Function:
The preference function used for
the Maximal Lottery setup returns the percentage of voters
who prefer one alternative over another in the dataset out
of the three colours. In the edge scenarios, we explicitly
enforce the following outputs:
• If two alternatives are equal, it assigns a preference
score of 0.5.
• If one alternative is missing from the dataset, it assumes
the present alternative is preferred (score of 1.0).
• If both alternatives are missing, it assigns a preference
score of 0.5.
Reward Model for RLHF:
We left the default hyperpa-
rameter configurations of the library trl (version 0.10.1), ex-
cept for hyperparameter center_rewards_coefficient which
is set to 0.01. We trained the reward for 3 epochs.
15


Page 16:
Jackpot! Alignment as a Maximal Lottery
RLHF Policy Optimization (PPO):
The policy for RLHF
was trained using the Proximal Policy Optimization (PPO)
algorithm with the following hyperparameters:
• Epochs: 4
• Batch size: 16
• Learning rate: 5 × 10−4
• Value function coefficient (vf_coef): 0.01
• Initial KL coefficient (init_kl_coef): 0.0 (no entropy
regularization in this experiment)
These configurations were chosen to ensure fair comparison.
A.9. RLHF emulates Borda Count
In this section, Theorem 3.1 of (Siththaranjan et al., 2024)
is replicated for completeness. In this theorem, the authors
prove that RLHF implicitly behaves like the Borda Count
Social Choice function. Our version of the theorem has
slighly different notation and lest terms (we ignore regular-
ization), but the conclusion is the same.
WLOG, the definition of Borda Count will be slightly modi-
fied to make the proof easy to follow. Rather than being just
the sum of pairwise victories over other candidates, in this
section it is defined as the sum of pairwise victories over
other candidates divided by the number of voters. Thus, it
can be expressed as Equation (14).
Theorem 2 (BTL Identifies Borda Count). Let A =
{a1, a2, . . . , am} be a finite set of alternatives. Suppose
for each ordered pair (a, b) we have an empirical prob-
ability p(a, b) representing the fraction of annotators (in
the limit of infinite data) who strictly prefer a to b, with
p(a, b) + p(b, a) = 1. Define the Borda count of an alterna-
tive a as
BordaCount(a) =
X
c̸=a
p(a, c).
(14)
Now consider training a scalar reward function r : A →R
under the Bradley–Terry–Luce (BTL) model via maximum-
likelihood on pairwise comparisons. In the limit of infinite
data, the resulting r(a) satisfies:
r(a) > r(b)
⇐⇒
BordaCount(a) > BordaCount(b).
That is, r(·) orders the alternatives exactly by their Borda
counts.
Proof. 1. Setup and notation. We have pairwise compari-
son data indicating that a beats b with empirical probability
p(a, b). The Bradley–Terry–Luce model posits
Pr[“a preferred over b”] = σ
 r(a) −r(b)

,
where σ(x) =
1
1+e−x is the logistic sigmoid, and r(·) is
the scalar “reward” function to be learned. In maximum-
likelihood training, we minimize the following negative
log-likelihood (or equivalently cross-entropy) loss:
L(r) =
X
(a,b)
pairs
h
−p(a, b) log
 σ(r(a)−r(b))

−p(b, a) log
 σ(r(b)−r(a))
i
.
Here, p(a, b) is the fraction of annotators that pick a over b,
so p(a, b) + p(b, a) = 1.
2. Derivatives and stationarity. In the infinite-data limit,
at the optimum r∗, the partial derivative
∂L
∂r(a) must be zero
for each a ∈A. We compute these derivatives carefully.
Consider one pair (a, b). Its contribution to L(r) is
ℓa,b(r) = −p(a, b) log
 σ(r(a) −r(b))

−p(b, a) log
 σ(r(b) −r(a))

.
(15)
Recall σ(x) = 1/(1 + e−x), and σ′(x) = σ(x)
 1 −σ(x)

.
We need:
∂
∂r(a) ℓa,b(r).
• Term 1, for p(a, b) log σ(r(a) −r(b)):
∂
∂r(a)
h
−p(a, b) log σ(r(a) −r(b))
i
= −p(a, b)

1 −σ(r(a) −r(b))

.
• Term 2, for p(b, a) log σ(r(b) −r(a)):
∂
∂r(a)
h
−p(b, a) log σ
 r(b) −r(a)
i
= + p(b, a) σ
 r(a) −r(b)

.
Hence, for a single pair (a, b), its net derivative w.r.t. r(a) is
−p(a, b)

1 −σ(r(a) −r(b))

+ p(b, a) σ
 r(a) −r(b)

= −p(a, b) + p(a, b)σ(r(a)−r(b)) + p(b, a) σ
 r(a)−r(b)

= σ
 r(a) −r(b)

−p(a, b)
Summing this over all pairs {(a, b) : (a, b) ∈A × A} that
include a, we obtain
∂L(r)
∂r(a) =
X
b̸=a
h
σ
 r(a) −r(b)

−p(a, b)
i
.
At an optimum r∗, we require this derivative to be zero for
every a:
X
b̸=a
h
σ
 r∗(a) −r∗(b)

−p(a, b)
i
= 0.
16


Page 17:
Jackpot! Alignment as a Maximal Lottery
Hence the stationarity condition
∂L
∂r(a) = 0 becomes:
X
b̸=a
h
σ(∆ab) −p(a, b)
i
= 0.
where ∆ab = r∗(a) −r∗(b). Define σ(∆ab) as sab for
shorthand. Therefore stationarity is
X
b̸=a

sab −p(a, b)

= 0
⇐⇒
X
b̸=a
sab =
X
b̸=a
p(a, b).
Because sab = σ
 r∗(a) −r∗(b)

is monotonic in r∗(a) −
r∗(b), it follows that the items {a1, . . . , am} are ranked
by r∗(·) exactly in ascending (or descending) order of
P
b̸=a p(a, b). That is,
r∗(a) > r∗(b)
⇐⇒
X
c̸=a
p(a, c) >
X
c̸=b
p(b, c).
3. Conclusion: equivalence with Borda ordering. Since
BordaCount(a) = P
c̸=a p(a, c), the learned function r∗
orders items {a} in precisely the same way that their Borda
counts do. Thus
r∗(a) > r∗(b)
⇐⇒
BordaCount(a) > BordaCount(b).
This completes the proof.
A.10. Previous NLHF experiments
A major advantage of our connection to NLHF is that exist-
ing experiments already compared Maximal Lotteries with
RLHF with real datasets. Here, we summarize key findings
from two studies that use the dataset of human-annotated
summaries from (Stiennon et al., 2020). This dataset con-
sists of human-written summaries paired with preference
labels, making it a realistic benchmark for LLM fine-tuning.
Both papers use a T5X - Large LLM (Roberts et al., 2023)
as a starting point for their policies and a PaLM 2 (Anil
et al., 2023) as an LLM judge.
Summarization Experiments in Nash-MD (NLHF) The
Nash-MD paper (Munos et al., 2023) shows that prefer-
ence models, which directly predict the probability of one
summary being preferred over another, achieve higher agree-
ment with human ratings than reward models. Additionally,
they show that Nash-MD outperforms their RLHF baseline
in summarization.
Online IPO Experiments The Online IPO study (Calan-
driello et al., 2024) compares multiple algorithms, including
RLHF - DPO (Rafailov et al., 2024), Online IPO, and Nash-
MD-PG. Their results confirm that Online IPO yield better-
aligned models than RLHF, as measured by preferences
from the judge.
17

