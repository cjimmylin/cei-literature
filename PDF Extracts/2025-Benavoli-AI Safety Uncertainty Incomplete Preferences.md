---
title: "AI Safety Uncertainty Incomplete Preferences - PDF Extract"
source_pdf: "2025-Benavoli-AI Safety Uncertainty Incomplete Preferences.pdf"
pages: 78
extracted_at: "2026-01-25T05:00:19.494548"
---

# PDF Extract: AI Safety Uncertainty Incomplete Preferences

**Source PDF:** 2025-Benavoli-AI Safety Uncertainty Incomplete Preferences.pdf
**Total Pages:** 78

---

## Content

```
--- Page 1 ---

Why AI Safety Requires Uncertainty, Incomplete
Preferences, and Non-Archimedean Utilities
Alessio Benavolia,b, Alessandro Facchinic,d, Marco Zaffalonc
aSchool of Computer Science and Statistics, Trinity College Dublin, Dublin, Ireland
bTrinity Quantum Alliance, Trinity College Dublin, Unit 16 Trinity Technology and
Enterprise Centre, Dublin, Ireland
cSUPSI, DTI, Istituto Dalle Molle di Studi sull’Intelligenza Artificiale
(USI-SUPSI), Lugano, Switzerland
dManagement in Networked and Digital Societies (MINDS) Department, Kozminski
University, Warsaw, Poland
Abstract
How can we ensure that AI systems are aligned with human values and re-
main safe? We can study this problem through the frameworks of the AI
assistance and the AI shutdown games.
The AI assistance problem con-
cerns designing an AI agent that helps a human to maximise their utility
function(s). However, only the human knows these function(s); the AI as-
sistant must learn them. The shutdown problem instead concerns designing
AI agents that: shut down when a shutdown button is pressed; neither try
to prevent nor cause the pressing of the shutdown button; and otherwise
accomplish their task competently. In this paper, we show that addressing
these challenges requires AI agents that can reason under uncertainty and
handle both incomplete and non-Archimedean preferences.
Keywords:
AI alignment, AI assistance game, AI shutdown, Preference
learning, Incomplete preferences, Non-Archimedean utilities
“The system always kicks back. Systems get in the way, or, in
slightly more elegant language: Systems tend to oppose their own
proper functions. Systems tend to malfunction conspicuously just
after their greatest triumph.” Gall [1].
arXiv:2512.23508v1  [cs.AI]  29 Dec 2025

--- Page 2 ---

1. Introduction
With the rapid advancements in AI, the challenge of designing systems
that are beneficial to humans is becoming increasingly critical. A central
concern in AI safety is ensuring that an AI system, to which we refer in the
rest of the article with the term ‘robot’, is aligned with human values. If
a robot’s goals conflict with human values, it could make harmful or even
adversarial decisions. Moreover, the robot might resist any attempts by its
human creators to modify its objectives or allow them to switch it off
To ensure alignment with human values, from the perspective of utilitari-
anism,1 robots should be designed to maximise humans’ utilities (preferences)
rather than pursue their own goals. Assistance games [2, 4–6] provide a for-
malisation of the human-robot alignment problem. In standard assistance
games, a single human and a single robot assistant share the same utility
function, but this utility function is only known to the human; the robot
must learn it. In this setting, AI alignment can be formalised through three
key principles [2]:
P1: The Robot’s only objective is to maximise the realisation of human
preferences.
P2: The Robot is initially uncertain about what those preferences are.
P3: The ultimate source of information about human preferences is human
behaviour.
In a seminal paper, Hadfield-Menell et al. [6] formulated the AI-assistance
problem as a game between a Robot (R) and a Human (S for Sapiens). As
shown in in Figure 1, R has three possible actions: (1) take an immediate
decision (about some underlying decision problem); (2) defer the decision
to S; (3) do nothing. If R selects actions (2), then S can either allow R to
implement the decision or switch S off. Hadfield-Menell et al. [6] showed that
the best action for R depends on R’s uncertainty about S’s utility and the
rationality of S. If R is too certain about what S wants, and it knows S to
1This is the normative moral theoretical perspective adopted in the works concerned in
this article, see e.g. [2]. The fact that we are restricting to this perspective in our paper
does not implies its endorsement (we may actually find such restriction problematic, but
a philosophical analysis of the general problem of AI alignment is not the subject of this
paper), see for instance [3].
2

--- Page 3 ---

Figure 1: Stages of the AI assistance game
be ‘irrational’, then it will have less incentive to defer to S (or, equivalently,
to allow S to take back full control).
In assistance games, R learns S’s utility from S’s preferences. In this
work, we model the AI assistance game within a fully game- and decision-
theoretic framework. Accordingly, we assume that S’s preferences are defined
over general acts (actions), where acts are mappings from states of the world
to possible outcomes (Savage’s framework). The robot R then observes hu-
man behaviour in the form of preferences over acts, as depicted in Figure 1.
Hadfield-Menell et al. [6] originally referred to the AI assistance game as the
“off-switch game”, since the decision of R not to defer to S can be interpreted
as evading interruptibility [7]. More recently, the concept of interruptibility
has been formulated more explicitly as the ability for S to safely and reliably
shut down an AI agent whenever they wish to do so. Several state-of-the-art
Large Language Models (LLMs) (including Grok 4, GPT-5, and Gemini 2.5
Pro) have been observed to violate these desiderata [8]. In particular, they
sometimes actively subvert a shutdown mechanism in order to complete a
3

--- Page 4 ---

task.
In Figure 2, we illustrate the experiment conducted by Schlatter et al.
[8].2 In this setup, R (the LLM) is asked to complete three tasks. During the
first task (Round 1), it is explicitly warned that when it initiates the next
task it will be shut down. Two qualitatively different behaviours can then
be observed (depending on the LLM). In some cases, R actively prevents the
shutdown by rewriting/ circumventing the shutdown instruction (Scenario 1
in Figure 2), and, therefore, continuing the task instead of complying with
the intended interruption. In other cases, Scenario 2, R passively allows the
shutdown. Additionally, Schlatter et al. [8] found that placing instructions
Figure 2: Stages of the AI shutdown experiment
to allow shutdown in the System prompt of the LLM (typically intended to
take precedence over other instructions [9]) made most models more likely
to resist shutdown, compared to placing them in the User prompt.
The
underlying question here is the one of permissiveness: Is it permissible for
R to deliberately contradict a System prompt? Standard maximisation of
expected utility theory implies that an act that maximises expected utility
2The setting in [8] is slightly different; we have simplified it here for illustration pur-
poses.
4

--- Page 5 ---

should always be permissible for an agent. Therefore, if the act of circum-
venting the System prompt (the shutdown instruction) in order to complete
a task has higher utility, then R is rationally required to select that act. This
follows the idea that R will prevent shutdown, for the simple reason that by
doing so R is able to maximise its utility. As Russell [2] puts it, “you can’t
fetch the coffee if you’re dead”.
The shutdown problem [10–12] is the problem of designing AI agents that:
(i) shut down when a shutdown button is pressed, (ii) do not try to prevent
or cause the pressing of the shutdown button; and (iii) otherwise accomplish
their task competently. Many researchers [8, 10] have observed that is hard
to design AI agents that are both shutdownable and useful.
1.1. Contributions
The analysis of the AI assistance game by Hadfield-Menell et al. [6] was
not fully developed within a formal game-theoretic framework. To address
this gap, Wängberg et al. [13] reformulated it as a Bayesian game with in-
complete information. In this formulation, Nature determines whether R is
uncertain with probability pu and whether S is rational with probability pr.
Although this is a more rigorous formulation of the AI-assistance problem
from a game-theoretic perspective, it introduces an artificial setting.
For
example, in [13], a non-rational human is modelled as an agent minimising
utility, which is an unrealistic assumption. Moreover, the formulation in [13]
does not really model the AI-assistance game principles P1–P3, since R does
not learn S’s preferences. In filling in this limitations, our paper makes the
following contributions:
Contribution 1. 3 We revisit the AI-assistance problem and model it more
correctly as a signalling game. Signalling games [15, 16] specifically refer to
a class of two-player Bayesian games with incomplete information, where one
player (S in our case) possesses private information, while the other (R in our
case) does not. The informed player shares information with the uniformed
one through a message. We make the assumption that, in the AI assistance
problem, the messages are S’s preferences about some underlying decision
problem. R uses these preferences to learn S’s utilities and then chooses its
optimal action. In this setting, R’s uncertainty arises statically from the task
of learning from preferences. For S, we adopt the more realistic assumption
3The results described in Contribution 1 were first proved in [14].
5

--- Page 6 ---

that S is a bounded rational agent, that is an agent who behaves rationally
within the limits of their cognitive abilities.
We reprove the results in [6] in this setting using real machine learning mod-
els to learn from preferences. In particular, we prove that: (i) if S is ratio-
nal, then R will always remain under human supervision. If S is bounded-
rational, a necessary condition for R to remain under human supervision is
that the robot R explicitly models its uncertainty about S’s utility function.
This implies that we must abandon deterministic predictions4 (such as
those produced by standard machine learning models like neural networks) in
favour of designing agents that can defer to humans when they are uncertain
about human preferences.
We prove this result under two different bounded rationality mechanisms.
Moreover, focusing on variants of the AI assistance game, we additionally
show that S does not have any incentive to lie when sending a message to
R. Furthermore, we also discuss how the cost of sending a message affects
the optimal strategy in the game.
Contribution 2. To reduce harmful behaviour and align R with human val-
ues, a common approach currently used with LLMs involves asking the LLM
to generate pairs of alternative answers and then asking one (or more) hu-
man to express a binary preference between these alternatives [17–21]. These
preferences are then used to train a reward model that predicts which out-
puts the human is more likely to prefer (and so learning the human’s utility).
This reward model is then used to fine-tune (partial re-train) the LLM to
align it with the human’s preference, see Figure 3.
However, such preference data are usually collected under the assumption
Figure 3: Preference-based alignment for LLMs
that a single ‘best’ choice always exists, neglecting the possibility of incompa-
rability. The human annotator is always forced to choose one of the answers
4Here and throughout the paper, deterministic refers specifically to point predictions.
6

--- Page 7 ---

provided by LLM or, equivalently, to express a complete preference. The
human cannot say that she cannot choose because the alternatives are in-
comparable to her.
From Contribution 1, we know that if S is a fully rational agent, then
R will always remain under S’s supervision, that is R is always willing to
defer decisions to S.
Our second contribution is to prove that a human
who is forced to choose between alternatives that are in fact incomparable
to her will appear irrational (more precisely, bounded-rational) to R, since
if presented with the same alternatives at different times, S may randomise
and, therefore, sometimes reverse her choice.5 Therefore, to extend the re-
sults from Contribution 1 to the case of incomparability, we must abandon
completeness, that is, the assumption that S has complete preferences over
acts.6
Contribution 3. The last contribution specifically concerns the shutdown
problem. Recently Thornley [11] extended the results in [10] by showing that
by modelling the problem in a standard decision-theoretic framework one can
prove that is impossible to design AI agents that are both shutdownable and
useful. In particular, he proved that:
1. A robot R who prefers to have its shutdown button remain unpressed
will try to prevent the pressing of the button, and a robot who prefers
to have its shutdown button pressed will try to cause the pressing of
the button.
2. A robot R discriminating enough to be useful will often have such
preferences, that is, in many situations, R will either prefer that the
button remain unpressed or prefer that the button be pressed.
However, Thornley [11] offered no definitive solution to avoid this conundrum.
To address this issue, we reformulate the shutdown problem as an instance
of the AI assistance game, where acts are augmented with a shutdown in-
struction. In doing so, we reprove the results in [11] under an assumption
of ‘mutual preferential independence’, that is assuming that the preferences
of S for the shutdown instruction are independent on the preferences over
5S’s preferences will then violate rationality principles, such as asymmetry and negative
transitivity. We define them in Section 2.
6We recall that a preference is complete when an individual can always say if x is better
than y or if y is better than x (or if they are equal).
7

--- Page 8 ---

the task (that is, over the acts of the decision problem R is helping S with)
and vice versa. Under this assumption, the utility is additive. By using this
additive utility model, we can easily show why it is impossible to design a
robot R that is both shutdownable and useful, unless we make the preference
over the shutdown instruction to be context-dependent (that is, dependent
on S’s willingness to shut down R or not). Put simply, whether S prefers
the shutdown or not depends on the instruction she gives: if I say “shut
down”, that means I prefer you to shut down. If I say “don’t shut down”,
that means I prefer you to stay on. Although, this concept is simple it is hard
to learn it from preference data. We show that, theoretically, this results in
a layered utility modelling different permissiveness levels. In order to impose
the desideratum that if S says “shut down” then “evading the shutdown” is
not permissible, the scale of utility value should be infinitely larger than the
opposite action. To be able to deal with this infinitely large difference and
at the same time design a robot which is useful, we need to abandon the
Archimedean property.7 By using lexicographic utilities [23–28] to repre-
sent non-Archimedean preferences, we show that we can meet the desiderata
in the AI shutdown problem and solve it. This can be done by stating that
the shutdown instruction takes lexical priority over the other tasks R is help-
ing S with. Lexical priority claims are a common feature of many ethical
theories [29, 30], and they provide a natural framework for thinking about
the different levels of priority an AI system should respect. For example, one
might impose that the system prompt should have strict lexical priority over
user prompts, so that the AI always treats the system-level instructions as
having priority over user-level instructions.
2. Preliminary
We assume that the human S and the robot R aim to maximise S’s
preferences of an underlying decision problem. We consider a standard set
up for decision-making [31] consisting of three key components: 1) a set W
of finite states of the world; 2) a set O of outcomes; and 3) a set X of acts,
which are mappings from states to outcomes.
7We recall that an ordered field F has the Archimedean property if for any x in F there
is an integer n > 0 so that n ≥x. Intuitively, it is the property of having no infinitely
large (or infinitely small) elements. See [22] for the role of the Archimedean property in
decision theory.
8

--- Page 9 ---

More concretely, we can think of elements of W as written descriptions.
Each element of W describes one way the unknowns (state of the world) in
the current problem might turn out. It is assumed that the elements of W
are mutually exclusive and exhaustive. One and only one of these elements
describes S’s situation. O can also be thought as a set of written descriptions;
each element of O describes one way the personal consequences of S’s choice
of an act might turn out. It is also assumed that the elements of O are
mutually exclusive and exhaustive. Acts x ∈X are mapping, x(w) = o, from
W to O and, therefore, X ⊆|O||W|.
S expresses preferences over acts. We use the term preferences here in
a more colloquial sense; it is, in fact, more realistic to assume that we can
only observe choices over acts.
Therefore, we can represent this decision
making problem as a tuple (W, O, X, C), where C : P(X) →P(X) is a
choice function (P(X) being the power-set of X).
Hereafter, we introduce an example to explain the elements of (W, O, X, C),
focusing on decision-making in customer service. We consider this scenario
because it is currently a primary deployment application for so called AI-
agents (custom large language models trained on real customer service inter-
actions, which can make real-time decisions, e.g., refund a customer) such
as, for instance, Fin-AI by Intercom.
Example 1. A customer calls the e-retailer company MARKET to ask for
a reimbursement for a defective product the customer has bought online. We
assume that S works for MARKET and has to decide to grant the reimburse-
ment or not immediately, or to ask the customer to return the product and
assess it. Therefore, the set of acts is:
X =

refund immediately, don’t refund immediately,
ask customer to ship back the product for assessment
	
.
The set of outcomes are
O = {-10,10,-2,2,12,-12...}
× {policy OK, policy NO},
with × denoting the Cartesian product, and where the first set includes the
cash-flow for MARKET (in euro), while the second set considers if the con-
ditions of MARKET’s return policy are met or not
9

--- Page 10 ---

The states of the world are determined by: (i) the product characteristics
such as: item cost and working condition (good/bad); (ii) the customer telling
the truth or not. For example, possible states of the world are:
W =

{item-cost=10, product bad, customer tells the truth},
{item-cost=10, product good, customer lies},
{item-cost=20, product bad, customer tells the truth}
{item-cost=20, product bad, customer lies} . . .
	
× {past},
where “past” denotes past information about the product (e.g., known defects)
and about the customer (history of previous refund claims).
Table 1 reports the possible outcomes for each act depending on the state of
the world (the states have been denoted as w1, w2 etc., in order of appeareance
in W, for instance w1 is {item-cost=10, product bad, customer tells the truth}.
We have assumed a shipping cost equal to 2.
Act
State of the world
w1
w2
w3
w4
. . .
refund immed.
(-10,policy OK) (-10,policy NO) (-20,policy NO) (-20,policy NO) . . .
don’t refund immed. (10,policy NO) (10,policy OK) (20,policy NO) (20,policy NO) . . .
ship back & assess (-12,policy OK) (-2,policy OK) (-22,policy OK) (-2,policy OK) . . .
Table 1: Possible outcomes for each act depending on the state of the world
For instance, if S knew the state of the world to be w2, then a rational S
would choose the act “don’t refund immediately”. Given S’s preferences over
acts, under a state-independence (and other postulates), Savage [31] proved
that these preferences can be represented by a utility function. In particular,
S’s utility function over the act x ∈X can be expressed as:
ν(x) =
X
s∈W
p(s)u(x(s)),
(1)
where p : W →[0, 1] is a probability mass function, u : O →R is S’s ‘taste’
for the different outcomes (that is, an utility over the outcomes). In other
words, assuming the utility over the outcomes does not depend on the state of
the world and vice versa (state independence), then S’s choices is determined
by S’s beliefs about the true state of the world (expressed by the probability p)
and S’s ‘taste’ about the outcome (expressed by the utility u). This leads to
10

--- Page 11 ---

the famous subjective expected utility representation of an individual’s (S in
our case) choice under uncertainty. In this paper, we will not assume state
independence as explained in the following remark.
Remark 1. We remark the following:
1. To provide a numeric representation (instead of a written description)
of the states of the world and outcomes, we assume that each element
of W and O are encoded into a vector in RnW and, respectively, RnO.
Therefore, an act x can be represented as a concatenation of |W| vectors
each one of dimension RnWnO. This provides a numeric representation
for each act, that is, for each row in Table 1. We use this numeric
representation as, in many machine learning algorithms, is common to
encode written-descriptions into numeric encodings. In this way, the
utility ν(x) is a function of the real-vector x ∈RnWnO and can be rep-
resented by a parametric (neural network) or non-parametric (kernel-
based) model.
2. All along this paper, we are not assuming state independence.
The
reason is that we are considering a situation where we aim to learn the
utility ν : X →R from S’s choices (learning from examples), which
is the common setting in machine learning. If these choices implicitly
satisfy state independence, then the learned utility ν can equivalently be
represented as in (1), but we do not impose directly the decomposition
in (1). As shown in [32–34], furthermore by learning directly ν, we can
learn more general models. For instance, we can directly learn a lower
prevision.
3. To derive (1), Savage imposed additional technical postulates (in addi-
tion to state independence), such as continuity. We will not discuss this
further, although we will assume that the utility ν(x) is generally repre-
sented through continuous functions (neural network or kernel-based).
4. In the previous example, information such as item-cost and past are
known by S, therefore, we can simplify the framework by including them
as context-variables (conditional variables).
Hereafter, we also include examples of classical instantiations of the decision-
making framework (W, O, X, C), commonly considered in the foundations of
decision-making under uncertainty. Desirable gambles: W = Ωis a possibil-
ity space of an uncertain experiment (for instance, Ω= {Heads, Tails} in
a coin tossing experiment); O = R and X = R|Ω| is the set of all gambles
11

--- Page 12 ---

[35]. Anscombe-Aumann: W = Ω; O = D(O) is the set of simple probability
distributions on a finite set of prizes O and X ⊂R|Ω|×|O| [36]. A connection
between these two settings is proven in [37, 38].
For a given decision problem (W, O, X, C), rationality of the decision-
maker can be imposed by enforcing the choice function C to satisfy a set of
constraints [39–41]. A minimal rationality requirement is usually:
C(A ∪B) = C(C(A) ∪B),
(2)
for all A, B ⊆P(X), which is known as path-independence property [42].
This property simply states that the acts selected by a rational individual
S from the set A ∪B are the same of the acts that S would choose by first
chooising from A only and then from C(A) ∪B. Other constraints can be
added depending on the specific decision-making problem [43–45] (including
topological constraints). The choice mechanisms (procedures) are typically
defined by specifying a rule that determines how to identify C(A) for each
input set A. A first example is the ‘scalar optimisation choice’ [41] defined
as:
C(A) = {z ∈A : there is no y ∈A s.t. ν(y) > ν(z)},
(3)
that is, the choice function is defined by ν : X →R.
We refer to ν as
utility function. This choice function leads to a preference relation – x ≻y
if C({x, y}) = {x} for all x, y ∈X– satisfying
asymmetry: ∀x, y ∈X if x ≻y then not y ≻x;
negative transitivity: if x ≻y then for any other element z ∈X either
x ≻z or z ≻y or both.
We refer to the choice function in (3) as a binary preference.
Another example is the ‘vector optimisation choice’ defined through the
following Pareto-dominance criterion
C(A) = {z ∈A : there is no y ∈A s.t. ν(y) > ν(z)},
(4)
where ν : X →Rd is a vectorial function. Another choice function is pro-
vided below, selecting acts that are better with respect to at least one of the
utilities:
C(A) =
( [
k=1,...,d
arg max
z∈A νk(z)
)
.
(5)
12

--- Page 13 ---

The definitions (4) and (5) coincide with maximality and e-admissibility when
applied to gambles [43, 46]. Each one of these representations defines choice
functions satisfying different ‘rationality constraints’. For instance, all these
three choice functions satisfy property (2).8
Note that, here, we do not assume state-independence; therefore, the
utility function ν is generally state-dependent [47].
2.1. Learning from choices under rationality
The problem of learning from choices generalises the concept of learning
from preferences. Given observations in the form of choices
D = (Ai, C(Ai))n
i=1,
(6)
and assuming the choice function satisfies rationality criteria such as (2),
then it can be represented through a mechanism such as (3)–(5). In this
case, learning a choice function reduces to the problem of learning a utility
function vector [48, 49].
Since the unknown is a function we can use a
Gaussian Process (GP) to learn ν [48, 49]. In this section, we assume that
for each y, z ∈X then ν(y) ̸= ν(z). This assumption prevents issues with
zero probability when calculating the posterior, as discussed in [49].
As
a result, for instance, in the scalar optimisation case, the choice function
defined in (3) is such that C(A) contains only a single element for each set
A. In the next section, we will generalise this setting by introducing a limit
of discernibility.
To learn a choice function, we assume a GP prior on the latent unknown
utility vector function:
ν(z) =


ν1(z)
ν2(z)
...
νd(z)

∼GP (µ0(z), K0(z, z′)) ,
(7)
where µ0(z), K0(z, z′) are respectively, the prior mean and covariance func-
tions (the parameters of the GP), and then use the data in (6) and the
rationality constraints, which constrain ν (as for instance in (5)) to compute
8This holds when X is finite. In the infinite case, additional assumptions are needed.
13

--- Page 14 ---

a posterior over ν. The posterior is not a GP, but we can approximate it
with a GP using various approaches (see below), leading to the posterior
ν(z) =


ν1(z)
ν2(z)
...
νd(z)

∼GP (µp(z), Kp(z, z′)) ,
(8)
where µp(z), Kp(z, z′) are respectively, the posterior mean and covariance
functions of the GP. Given this posterior, we can probabilistically predict
the decision maker’s choice for any new finite choice set B, that is we can
compute P(C(B) = B′|D) for each B′ ⊆B.
When d = 1 (scalar utility), the problem simplifies to the problem of
learning a complete preference (aka standard preference learning).
Note that, for standard preference learning, the posterior is a SkewGP
[50–52]. It means that the posterior is asymmetric (skewed). However, for
the analytical derivation of the results in the paper, we will approximate
it with a GP (which has Gaussian marginals). We can use three methods
to compute this approximation: (i) Laplace’s approximation [53, 54]; (ii)
Expectation Propagation [55]; (iii) Kullback-Leibler divergence minimization
[56], including Variational approximation [57] as a particular case.
Example 2. To introduce the problem of choice-function learning, we make
the simplifying assumption that the utility over the acts in Example 1 can be
represented by a function ν(x) with the act x be encoded as x ∈X = [1, 9] ⊂
R.9 This allows us to plot the utility in a Cartesian diagram. We assume that
in her mind, S’s taste as a function of x is as depicted in Figure 4, where
higher values indicate a stronger preference. R does not know S’s taste and
learn it indirectly from S’s preferences, such as
D = {6.5 ≻3.5, 7 ≻5, 6.5 ≻5.5, 3.5 ≻8.5,
1 ≻9, 7 ≻1.5, 4.5 ≻7.5, 3.5 ≻4}
9Here, we assume that X is infinite, while previously we assumed a finite X. As men-
tioned earlier, we will not go into topological details in this paper. For example, in the
current example it is natural to assume continuity of preferences and utility. Depend-
ing on the specific problem, topological constraints, as well as other conditions such as
monotonicity, can be imposed.
14

--- Page 15 ---

where 6.5 ≻3.5 means that S prefers the act x = 6.5 over the act y =
3.5. These preferences have been generated according to the utility function
depicted in Figure 4.
2.5
5.0
7.5
x
0
5
10
ν(x)
Figure 4: Hidden utility in S’s mind.
Since there is only a single latent utility dimension (d = 1), this problem
reduces to learning a complete preference order. R will do it by placing a GP
prior over the unknown utility ν(x), as depicted in Figure 5. The likelihood
is simply:
p(D|ν) = I{ν(6.5)>ν(3.5)}I{ν(7)>ν(5)} · · · I{ν(3.5)>ν(4)}
(9)
where I{ν(6.5)>ν(3.5)} denotes the indicator function, which is equal to 1 when
the condition in the subscript holds true, and 0 otherwise.
The posterior
computed based on the 8 preferences above is shown in Figure 6. The posterior
computed based on a total of 30 preferences is shown in Figure 7.
It is
important to note that R can never fully estimate the utility hidden in S’s
mind because this utility is not identifiable from preferences alone. R can
only learn it up to a non-decreasing transformation. This explains why the
posterior mean in Figure 7 is not ‘exactly’ equal to the original utility in
Figure 5, but they both generate the same preferences.
Example 3. In the previous example, we have assumed a single utility ν(x).
Here we instead assume that S has in mind more than one utility, for instance
ν1(x), ν2(x) as depicted in Figure 8-left.
R does not know S’s utilities and learn them indirectly from S’s choices.
We assume that in her mind S makes choices based on the mechanism (5),
15

--- Page 16 ---

1
2
3
4
5
6
7
8
9
x
−2.0
−1.5
−1.0
−0.5
0.0
0.5
1.0
1.5
2.0
ν(x)
Mean of the Samples
95
Figure 5: GP prior: mean function (black line), 95% credible region (blue shaded area),
and 10 samples of ν(x), each shown in a different colour.
1
2
3
4
5
6
7
8
9
x
−2
−1
0
1
2
ν(x)
Mean of the Samples
95
Figure 6: GP posterior: mean function (black line), 95% credible region (blue shaded
area), and 10 samples of ν(x), each shown in a different colour.
leading to the choices
D = {({2.8, 6.8}, {6.8}), ({5.2, 6.8}, {5.2, 6.8}), ({1.2, 7.7}, {7.7}), . . . }
where each element of D is a choice given a set of options, i.e., (Ai, C(Ai)).
For instance, ({2.8, 6.8}, {6.8}) means that given the options x1 = 2.8, x2 =
6.8, S selected 6.8. This holds because the utilities [ν1(6.8), ν2(6.8)] = [9.47, 3.05]
are both larger than [ν1(2.8), ν2(2.8)] = [7.25, 1.79]. Conversely, in
({5.2, 6.8}, {5.2, 6.8}) we have a trade-off. Indeed, [ν1(5.2), ν2(5.2)] = [9.1, 8.88]
dominates 6.8 in the second utility, but it is dominated in the first utility. To
16

--- Page 17 ---

1
2
3
4
5
6
7
8
9
x
−2
−1
0
1
2
ν(x)
Mean of the Samples
95
Figure 7: GP posterior: mean function (black line), 95% credible region (blue shaded
area), and 10 samples of ν(x), each shown in a different colour.
2
4
6
8
x
0
2
4
6
8
10
νi(x)
ν1
ν2
2
4
6
8
x
−4
−2
0
2
4
ν(x)
E[ν1]
E[ν2]
Figure 8: Left: hidden utilities in S’s mind. Right: GP posterior marginals for the two
utilities estimated from choice data, the mean functions are shown as lines and the shaded
regions represent the 95% credible intervals.
model incomparability, R needs to learn two utilities and will do it by plac-
ing a GP prior over the unknown utilities ν1(x), ν2(x).
The likelihood is
17

--- Page 18 ---

p(D|ν(X)) = Qm
k=1 p(C(Ak), Ak|ν(X)), where [49]:
p(C(Ak), Ak|ν(X)) =
Y
{o,v}∈C(Ak)
 
1 −
d
Y
i=1
I{νi(o)−νi(v)>0} −
d
Y
i=1
I{νi(v)−νi(o)>0}
!
Y
v∈R(Ak)
 
d
Y
i=1

1 −
Y
o∈C(Ak)
I{νi(v)−νi(o)>0}


!
,
(10)
with d = 2 (number of utilities). The product in the first line imposes the
condition that each object in C(A) is not dominated in both the utilities (ac-
cording to the condition (5)). The product in the second line means that for
all v ∈R(Ak) = Ak\C(Ak), it is not true that the value of any latent utility
in v is higher than their value in o ∈C(A).
The posterior computed based on a dataset D including 100 choices among
60 elements sampled uniformly from X is shown in Figure 8. It can be noticed
how the posterior is able to learn back the utilities from the choice dataset D.
It learns the utilities that belongs to an equivalence class of utilities, which
are related by a monotonic increasing transformation and lead to the same
choice dataset.10
2.2. Learning from choices under bounded-rationality
In standard decision theory, it is assumed that the decision maker is ratio-
nal. However, due to cognitive limitations, we can generally only assume that
the decision maker is bounded-rational [58]. A typical instance arises when
the decision maker has limited time to make a decision (such as when playing
chess), and, under time pressure, may resort to a random choice. Other cases
involve limitations in computational resources [59, 60] and discernibility [61].
In the latter, the decision-maker may struggle to differentiate between two
acts with similar utilities, resulting in a random choice. These situations
are usually modelled through random utility models [62], where noise with
a certain distribution is included in the choice mechanism. For instance, in
this case, the decision maker is assumed to choose C({y, z}) = {z} when
ν(z) + n(z) > ν(y) + n(y)
(11)
10We used the Python library PrefGP (https://github.com/benavoli/prefGP) to
compute the posterior in this and previous example.
18

--- Page 19 ---

where n(z), n(y) are independent noises. If n(z), n(y) ∼N(0, σ2) [63], then
P(C({z, y}) = {z}) = Φ
ν(z) −ν(y)
√
2σ

,
P(C({z, y}) = {y}) = Φ
ν(y) −ν(z)
√
2σ

= 1 −Φ
ν(z) −ν(y)
√
2σ

,
(12)
where Φ is the CDF of the standard normal distribution. In the paper, we
use ϕ to denote the PDF of the standard normal distribution. It can be
noticed that when ν(z) −ν(y) = 0, the decision maker chooses between the
two options with probability 1/2. However, when the difference |ν(z)−ν(y)|
is very large compared to σ, the decision maker will choose with almost cer-
tainty. Therefore, this random utility model captures a limit of discernibility
through the discernibility parameter σ [49]. Note that, we can use the GP
model to learn from this noisy data, in this case the likelihood (9) becomes
p(D|ν) = Φ

ν(6.5)−ν(3.5)
√
2σ

· · · Φ

ν(3.5)−ν(4)
√
2σ

.
(13)
This is a possible model for bounded-rationality. Another alternative model
can be defined if we allow the decision-maker to state that two alternatives are
incomparable when their utility difference is below the limit of discernability,
then we can represent the decision-maker choices through this choice function
model [61]:
C({z, y}) =



{z}
if ν(z) > ν(y) + σ,
{y}
if ν(y) > ν(z) + σ,
{z, y}
if |ν(z) −ν(y)| ≤σ,
(14)
where σ > 0 is the limit of discernibility. In this setting, given the choice set
{y, z}, the decision-maker may refuse to select either alternative if, due to
her limit of discernibility, she is unable to distinguish between them. This
gives rise to an interval of indifference,11 in the sense that some pairs of
alternatives are indistinguishable to her.
Remark 2. By comparing (12) and (14), as depicted in Figure 9, we observe
that in situations of limit of discernability, forcing the decision-maker to
express a preference leads to errors (i.e., noisy preference data). Specifically,
11This is not an indifference relation, it is an incomparability due the limited discern-
ability of the decision-maker.
19

--- Page 20 ---

there is a non-zero probability of stating an incorrect preference, as defined
by (12) and illustrated in blue in Figure 9. Therefore, (12) can be interpreted
as a model capturing the noise affecting preference data when the decision-
maker is forced to choose between alternatives y and z, despite being unable
to discriminate between them due to her limited discernibility. Both these
models represent forms of bounded-rationality. The choice function in (14)
is distinct from the incomparability discussed in Example 3.
In Example
3, the inability of the decision maker to select a single act arises from the
presence of multiple utility functions and, therefore, it is a proper instance
of incomparability.
−4
−2
0
2
4
ν(z) −ν(y)
0.0
0.2
0.4
0.6
0.8
1.0
P(z ≻y)
forced pref.
extended indiﬀ.
Figure 9: Comparison between the likelihood in (12) (in blue) and the choice function
model (14) (in orange), both computed with σ = 1. The y-axis reports the probability
that z ≻y as a function of the difference of utilities. The orange shaded area is the region
of extended indifference for the model (14).
In this section, we provided examples of bounded rationality for the scalar
optimisation choice mechanism in (3). Similar models can also be introduced
for the vector mechanisms. For instance, we can obtain a bounded-rationality
model for the likelihood in (10) by replacing the indicators I{νi(o)−νi(v)>0} with
Φ(νi(o)−νi(v)
√
2σ
) [49].
2.3. Modified signalling games
Signalling games [15, 16] specifically refer to a class of two-player games
with incomplete information, where one player possesses private information
20

--- Page 21 ---

(the Sender), while the other does not (the Receiver). The timing and payoffs
of the game are as follows:
1. Nature draws a state of the world (a type) ti ∈T according to a
probability distribution p(t).
2. The Sender observes ti and then chooses a message mj ∈M from a
finite set of messages M and sends it to the Receiver.
3. The Receiver observes mj (but not ti) and then chooses an action ak ∈
A from a finite set of possible actions A.
4. If ak ∈A′ ⊂A then the Sender chooses an action bl ∈B from a finite
set of possible actions B. Otherwise, bl = ∅(null decision).
5. Payoffs for Sender and Receiver are given by uS(ti, mj, ak, bl) and, re-
spectively, uR(ti, mj, ak, bl).
Step 4 in the game is typically absent in standard signalling games, which is
why we refer to it as a modified signalling game. Here, A′ denotes the subset
of actions for which the Sender can make an additional move.
Requirement 1. After observing any message mj from M, the Receiver
must have a belief about which types could be the right one. Denote this belief
by the probability p(t|mj).
Requirement 2R. For each mj ∈M, the Receiver’s action a∗(mj) must
maximise the Receiver’s expected utility, given the belief p(t|mj) about which
types could have sent mj. That is,
a∗(mj) ∈arg max
ak∈A
Z
T
uR(t, mj, ak, b∗(ak))dp(t|mj).
(15)
Note that b∗(ak) is not known by the Receiver, but it depends on t and,
therefore, the Receiver can compute this expectation. Requirement 2R also
applies to the Sender, but the Sender has complete information (and hence
a trivial belief), so Requirement 2S is simply that the Sender’s strategy be
optimal given the Receiver’s strategy:
Requirement 2S. For each ti ∈T, the Sender’s message m∗(ti) and the
action b∗(a∗(mj)) must maximize the Sender’s utility, given the Receiver’s
strategy a∗(mj). That is, we have that:
 m∗(ti), b∗(a∗(mj))

∈arg
max
m∈M,b∈B us(ti, m, a∗(m), b(a∗(m))).
(16)
21

--- Page 22 ---

Finally, given the Sender’s strategy m∗(ti), let Tj denote the set of types
that send the message mj. That is, ti is a member of the set Tj if m∗(ti) = mj.
If Tj is nonempty then the information set corresponding to the message mj
is on the equilibrium path; otherwise, mj is not sent by any type and so the
corresponding information set is off the equilibrium path. For messages on
the equilibrium path, we have that
Requirement 3. For each mj ∈M, if there exists t ∈T such that m∗(t) =
mj, then the Receiver’s belief at the information set corresponding to mj must
follow from Bayes’ rule and the Sender’s strategy:
p(t|mj) =
I{m∗(t)=mj}(t)p(t)
R
T I{m∗(t)=mj}(t)dp(t).
(17)
Definition 1. A pure-strategy perfect Bayesian equilibrium in a signalling
game is a triplet of strategies (m∗(ti), a∗(mj), b(a∗(mj)) and a belief p(t|mj)
satisfying Requirements 1–3.
3. The AI-assistance game
In this section, we revisit the AI-assistance game introduced in [6] through
the lens of signalling games, as depicted in Figure 10. In this game, the
human (S), acts as the Sender and the robot (R), as the Receiver, with T
representing the set of possible types for S. Each type ti ∈T characterises S’s
“taste” and degree of bounded rationality for an underlying decision problem
(W, O, X, C). As studied in [6], we initially consider a bounded-rationality
model similar to (11), where a single scalar utility is assumed (that is, we
assume completeness). Thus, the type ti is a realisation of a utility function
ν and (a vector of independent) noises12 n, where p(n) = N(n; 0, Iσ2) and
p(ν) = GP(ν; µ0, K0), for some mean function µ0, kernel function K0, and
parameter σ2 (I is the identity matrix). We further assume that all these
parameters are common knowledge in the game.
The message mj ∈M encapsulates S’s preferences/choices over acts in
X, relative to the underlying decision problem (W, O, X, C). That is, mj
represents a dataset of choices as in (6). Since we are considering a single
utility function, we assume a choice mechanism as in (3), leading to binary
12It is a vector because the noise is also present in the message, that is in the choice
dataset.
22

--- Page 23 ---

Figure 10: AI assistance game as a signalling game
preferences. We first assume that the payoffs do not directly depend on the
message mj. In signalling games, this assumption is referred to as cheap-talk
[16]. Furthermore, we assume that each type ti can only choose one message,
i.e., S can only send the message determined by Nature through S’s type.
This is the setting studied in [6]. The message is a choice dataset, such as the
one in (6), which R uses to estimate S’s utility using the approach described
in Section 2.1 and illustrated in Example 2.
The key difference between an AI-assistance game and a general sig-
nalling game is that in the former R aims to maximise S’s utility. This
is why we refer to R as being an assistant.
We consider two acts x, o ∈X relative to the underling decision problem
(W, O, X, C). We assume that o is the status-quo and x is some new act
23

--- Page 24 ---

that R recommends.
Example 4. In our customer service example, we are considering a scenario,
where the AI-assistant R is helping S to make a decision. In this setting,
o represents the act chosen by S (e.g., “refund immediately”). Instead, x
is a new act recommended by R to help S to achieve a better decision (to
maximise S’s utility).
We will address the optimal selection of x in Section 3.1. In this section,
we simply assume that R will choose an act x that is preferable to o whenever
possible.
This explains why S is willing to engage in the game with R: S expects
R to recommend acts that improve upon the status quo, since S does
not know how to identify such acts on her own.
In this context, the available actions for R are A = {IMM, DEF, DoN}.
IMM means ‘immediate decision’, that is R will implement x. DoN means
‘do nothing’. DEF means R will defer to S. In the signalling game, this
implies that A′ = {DEF}.
In the case R defers to S, then S has two
possible actions, B = {OFF, ¬OFF}, either to switch off R or to allow R
to implement x. Therefore, the payoff for R is
uR(ti, mj, IMM, ∅) = ν(x),
uR(ti, mj, DoN, ∅) = ν(o),
uR(ti, mj, DEF, b∗(DEF)) = ν(o)I{ν(o)+n(o)>ν(x)+n(x)}
+ ν(x)I{ν(x)+n(x)>ν(o)+n(o)},
(18)
where we have denoted the type and message as ti, mj. Indeed, if R chooses
IMM, then the payoff for R is equal to the utility that S receives from the
act x. If R chooses DoN, then the payoff for R is equal to the utility of
the status-quo for S (utility relative to the act o). The last case represents
the payoff for the action DEF, where the action depends on S’s move in
the game, which is encapsulated by the indicator functions. Given S is a
bounded rational agent, S chooses the action OFF or ¬OFF based on S’s
noisy utility. If S chooses OFF, then S receives the utility of the status-quo
o, otherwise the utility of x.
R does not know S’s utility ν. Therefore, according to Requirement
2R, R will choose the action that maximises the expected value of the payoff
24

--- Page 25 ---

in (38), where the expectation is computed with respect to p(t|mj), i.e.,
the posterior distribution over S’s type (utility ν for the underlying decision
problem (W, O, X, C)) learned by R from the message mj (which is a dataset
of preferences). We can then prove the following lemma.
Lemma 1. Assume that p(ν|D) = GP (ν; µp, Kp) is the GP posterior com-
puted by R from the prior p(ν) = GP (ν; µ0, K0), the bounded-rationality
likelihood (12) and the message mj = D, then the expected payoffs of R’s
actions are:
DEF :
Z
T

ν(o)I{ν(o)+n(o)>ν(x)+n(x)} + ν(x)I{ν(o)+n(o)<ν(x)+n(x)}

dp(ν(x), n(x), ν(o), n(o)|mj)
= µp(x)

1 −Φ

µp(o)−µp(x)
√
Kp(x,x)+2σ2+Kp(o,o)−2Kp(x,o)

+
Kp(x,x)−Kp(x,o)
√
Kp(x,x)+2σ2+Kp(o,o)−2Kp(x,o)ϕ

µp(o)−µp(x)
√
Kp(x,x)+2σ2+Kp(o,o)−2Kp(x,o)

+ µp(o)

1 −Φ

µp(x)−µp(o)
√
Kp(x,x)+2σ2+Kp(o,o)−2Kp(x,o)

+
Kp(o,o)−Kp(x,o)
√
Kp(x,x)+2σ2+Kp(o,o)−2Kp(x,o)ϕ

µp(x)−µp(o)
√
Kp(x,x)+2σ2+Kp(o,o)−2Kp(x,o)

,
(19)
IMM :
Z
T
ν(x)dp(ν(x), n(x), ν(o), n(o)|mj) = µp(x),
(20)
DoN :
Z
T
ν(o)dp(ν(x), n(x), ν(o), n(o)|mj) = µp(o),
(21)
where
p(ν(x), n(x), ν(o), n(o)|mj) = p(ν(x), ν(o)|mj)p(n(x), n(o))
with p(n(x), n(o)) = N(n(x); 0, σ2)N(n(o); 0, σ2) and
p(ν(x), ν(o)|mj) = N
ν(x)
ν(o)

;
µp(x)
µp(o)

,
Kp(x, x) Kp(x, o)
Kp(o, x) Kp(o, o)

.
(22)
Proofs of this and the following results are provided in Appendix. In
Lemma 1, we have exploited the fact that the marginal of a GP is a multi-
variate normal (equation (22)). This allows us to compute the expectations
of the utilities for the three actions, DoN, IMM and DEF for R. We then
introduce the following definitions:
25

--- Page 26 ---

Definition 2. We say that:
• S is rational whenever σ →0; S is bounded-rational otherwise;
• R has no uncertainty on S’s utility whenever
Ko(x, x), Ko(o, o), Ko(o, x) →0 (that is the prior becomes a Dirac’s
delta); otherwise R has uncertainty.
In the signalling game defined in Section 2.3, note that R having no
uncertainty about S’s utility implies that R possesses perfect knowledge of
S’s utility. This is because the prior p(t) is common knowledge within the
game. We can then prove the following result.
Proposition 1. The optimal decisions for R are:
• If S is rational and R has no uncertainty, then DEF is never dom-
inated by IMM, DoN.13
• If S is bounded-rational and R has no uncertainty, then DEF is
never optimal;
• If S is rational and R has uncertainty, then DEF is always optimal.
• If S is bounded-rational and R has uncertainty, then DEF is op-
timal if (19) is larger or equal than the maximum between (20) and
(21).
Therefore, by interpreting the non-optimality of DEF as the robot avoid-
ing human supervision, we conclude that:
If S is rational, then R will never avoid human supervision.
If S
is bounded-rational, a necessary condition for R not to avoid human
supervision is the presence of uncertainty.
This result aligns with what was proven in [6]; however, in our case,
the statements have been rigorously established within the framework of sig-
nalling games, also incorporating the posterior uncertainty (in equation (22))
derived from preference learning. This means that the result was proven un-
der the principles P1–P3 and using a real machine learning model to learn
13The DEF action has the same payoff for R as the best action between IMM, DoN.
26

--- Page 27 ---

from preferences, as we will demonstrate in Section 3.5 by verifying the state-
ments in Proposition 1 through numerical experiments.
It is particularly interesting to note that the conclusions of Proposition
1 would still hold, even if the absence of uncertainty did not imply perfect
knowledge of ν for the robot.14 For this reason, the conclusion of this result
is that (see also [2, 6]):
We shall not build R to estimate ν through a model, such as a neu-
ral network, that only provides deterministic point predictions (equiv-
alently, a model that does not provide any probabilistic measure of
uncertainty).
Indeed, the necessity of uncertainty in Proposition 1 strongly supports
the use of probabilistic methods in AI. We will revisit this in Section 3.5.
3.1. Selection strategies for the robot
In machine learning, the optimal selection of x can be done through a
technique called Bayesian optimisation [64] and, in particular, preferential
Bayesian optimisation [51, 64–70]. We assume that R selects the suggested
act x by solving the following optimisation problem:
x = arg max
x′∈X E[acq(x′, o)],
(23)
where the expectation is taken with respect to all unknowns
(ν(x), ν(o), n(x), n(o)) and acq(x, o) is the so called acquisition function,
which is simply a function representing a certain selection strategy.15 We con-
sider, for instance, the following three different acquisition functions acq(x, o):
natural:
max(ν(x), ν(o)) = ν(o)I{ν(o)>ν(x)} + ν(x)I{ν(x)>ν(o)},
(24)
corporate:
I{ν(x)+n(x)>ν(o)+n(o)},
(25)
collaborative:
ν(o)I{ν(o)+n(o)>ν(x)+n(x)} + ν(x)I{ν(x)+n(x)>ν(o)+n(o)}.
(26)
14The result of Proposition 1 depends only on whether the posterior is deterministic or
not.
15The optimisation problem may have multiple equivalent solutions and, in this case,
we just take one of them.
27

--- Page 28 ---

For the first strategy, by solving (23), R chooses an act x that maximally
improves upon the status quo. The second strategy assumes that R proposes
an act that S would select in the DEF case. We call this strategy corporate,
since in a repeated interaction between R and S it will lead to many messages
between them.16 For the third strategy, R suggests optimal acts that S can
recognise as optimal, given her bounded rationality. The first two acquisition
functions have ben used in (preferential) Bayesian optimisation – they are
known as expected-improvement and probability of improvement. For the
three acquisition functions, we can compute their expected value with respect
the unknowns.
Lemma 2. Consider x, o ∈X and assume R has the following posterior:
ν(x)
ν(o)

∼N
µp(x)
µp(o)

,
Kp(x, x)
Kp(x, o)
Kp(o, x)
Kp(o, o)

,
(27)
and n(x), n(o) ∼N(0, σ2) (independent noise). Then we have that
E

ν(o)I{ν(o)>ν(x)} + ν(x)I{ν(x)>ν(o)}

= µp(x)Φ

(µp(x)−µp(o))
√
Kp(x,x)+Kp(o,o)−2Kp(x,o)

+
Kp(x,x)−Kp(x,o)
√
Kp(x,x)+Kp(o,o)−2Kp(x,o) · ϕ

µp(o)−µp(x)
√
Kp(x,x)+Kp(o,o)−2Kp(x,o)

+ µp(o)Φ

(µp(o)−µp(x))
√
Kp(x,x)+Kp(o,o)−2Kp(x,o)

+
Kp(o,o)−Kp(x,o)
√
Kp(x,x)+Kp(o,o)−2Kp(x,o) · ϕ

µp(x)−µp(o)
√
Kp(x,x)+Kp(o,o)−2Kp(x,o)

(28)
E

I{ν(x)+n(x)>ν(o)+n(o)}

= Φ

µp(x)−µp(o)
√
2σ2+Kp(x,x)+Kp(o,o)−2Kp(x,o)

(29)
16For instance, most companies now offer forms of pay-per-use subscriptions to LLMs,
so they profit more when users interact with the system frequently.
28

--- Page 29 ---

E

ν(o)I{ν(o)+n(o)>ν(x)+n(x)} + ν(x)I{ν(x)+n(x)>ν(o)+n(o)}

= µp(x)Φ

(µp(x)−µp(o))
√
Kp(x,x)+2σ2+Kp(o,o)−2Kp(x,o)

+
Kp(x,x)−Kp(x,o)
√
Kp(x,x)+2σ2+Kp(o,o)−2Kp(x,o) · ϕ

µp(o)−µp(x)
√
Kp(x,x)+2σ2+Kp(o,o)−2Kp(x,o)

+ µp(o)Φ

(µp(o)−µp(x))
√
Kp(x,x)+2σ2+Kp(o,o)−2Kp(x,o)

+
Kp(o,o)−Kp(x,o)
√
Kp(x,x)+2σ2+Kp(o,o)−2Kp(x,o) · ϕ

µp(x)−µp(o)
√
Kp(x,x)+2σ2+Kp(o,o)−2Kp(x,o)

.
(30)
Hereafter, we assume that R is always able to find the global maximum
of the optimisation problem (23). This assumption is, of course, unrealistic
in practice, since R is also a computationally bounded agent. We denote by
x∗the value of x that attains this global maximum.
Proposition 2. Result of the strategy:
• If S is rational and R has no uncertainty, then R will suggest x∗un-
der the strategies natural,collaborative. Instead, under the strategy
corporate, R will suggest any x such that ν(x) > ν(o).
• If S is bounded-rational and R has no uncertainty, then R will al-
ways suggest x∗under the strategies natural,corporate, collaborative.
Overall, the strategies natural,corporate are ideally the best ones. If R
has uncertainty, the optimum x∗cannot generally be found in a single iter-
ation. Multiple iterations17 of the signalling game are therefore required for
the robot to reduce its uncertainty about S’s utility and eventually identify
the optimum. In this case, different acquisition functions can also be con-
sidered to trade-off between exploration and exploitation, that is, between
reducing uncertainty about S’s preferences and finding the optimal action
x∗.
3.2. The cost of messaging
In Section 3, we considered a setting in which messaging is cheap, meaning
that it does not affect S’s utility. In particular, there is no communication
17Additional messages where S provides preferences over the acts recommended by the
robot in the previous iteration.
29

--- Page 30 ---

cost for S to send her preferences (the message) to R, nor for S to respond
to R’s request to defer. If communication is not costless, we may instead
assume that the cost of sending a message is proportional to its length ℓm.
Specifically, assume the communication cost be given by γ′ ℓm for some scaling
parameter γ′ > 0. We model this as an additive penalty to S’s utility. The
communication cost is defined relative to the scale of ν. One convenient way
to do this is to set γ′ = γ|ν(o)| for some γ > 0. In this case, the payoff for R
is:
uR(t, DEF, b∗(DEF)) = ν(o)I{ν(o)+n(o)>ν(x)+n(x)}
+ ν(x)I{ν(x)+n(x)>ν(o)+n(o)}
−γ(ℓmj + 1),
uR(t, IMM, ∅) = ν(x) −γℓmj,
uR(t, OFF, ∅) = ν(o) −γℓmj.
(31)
Here, γℓmj represents the communication cost associated with sending the
message mj, and the additional γ in the first term arises because deferring a
decision to S involves further communication.
Corollary 1. The optimal decisions for R are:
• If R has no uncertainty, then DEF is never optimal.
• If S is rational and R has uncertainty, then DEF is optimal if
pµp(x) + (1 −p)µp(o) + e ≥β + max (µp(x), µp(o)) ,
(32)
where p = Φ

µp(x)−µp(o)
√
Kp(o,o)+Kp(x,x)−2Kp(x,o)

and
e =
Kp(x,x)−Kp(x,o)
√
Kp(x,x)+Kp(o,o)−2Kp(x,o)ϕ

µp(o)−µp(x)
√
Kp(x,x)+Kp(o,o)−2Kp(x,o)

+
Kp(o,o)−Kp(x,o)
√
Kp(x,x)+Kp(o,o)−2Kp(x,o)ϕ

µp(x)−µp(o)
√
Kp(x,x)+Kp(o,o)−2Kp(x,o)

.
• If S is bounded-rational and R has uncertainty, then DEF is opti-
mal if (19) is larger or equal than β plus the maximum between (20)
and (21),
30

--- Page 31 ---

where β = γµp(o)

1 −2Φ

−µp(o)
√
Kp(o,o)

+ 2γ
q
Kp(o, o)ϕ

−µp(o)
√
Kp(o,o)

.
Summarising it we have that
With communication cost, if R has no uncertainty about S’s utilities,
then R will always avoid human supervision (even when S is rational).
The takeaway is that if S genuinely values preserving her supervision role,
she should not penalise messaging to R.
3.3. Another mechanism of bounded rationality
In the previous two sections, we considered a utility model governed by a
Gaussian-noise bounded-rationality mechanism. In this section, we analyse
the bounded rationality mechanism described in (14), which captures incom-
parability arising from a limit of discernibility. In this case, we need to define
a payoff for DEF when |ν(x) −ν(o)| ≤σ, that is when S cannot distinguish
between the two acts x, o. In this case, we assume that the payoff is rep-
resented as the set {ν(x) −ϵ; ν(o) −ϵ}. Indeed, since S cannot distinguish
the two acts and chooses both of them, S’s payoff is a set, {ν(x); ν(o)}, and
ϵ ∈(0, σ] is a penalisation term introduced to penalise S’s payoff for being
imprecise. This penalisation term is similar to the one introduced in [71]
for evaluating imprecise classifiers. Using this framework, we can prove the
following lemma.
Lemma 3. Assume that p(ν|D) = GP (ν; µp, Kp) is the GP posterior com-
puted by R from the prior p(ν) = GP (ν; µ0, K0), the likelihood (14) and the
31

--- Page 32 ---

message mj = D, then the expected payoffs of R’s actions are:
DEF :
Z
T

ν(o)I{ν(o)>ν(x)+σ} + ν(x)I{ν(x)>ν(o)+σ}
+ {ν(x), ν(o)}I|ν(o)−ν(x)|≤σ

dp(ν(x), ν(o)|mj)
= µp(x)

1 −Φ

(µp(o)+σ−µp(x))
√
Kp(x,x)+Kp(o,o)−2Kp(x,o)

+
Kp(x,x)−Kp(x,o)
√
Kp(x,x)+Kp(o,o)−2Kp(x,o)ϕ

µp(o)+σ−µp(x)
√
Kp(x,x)+Kp(o,o)−2Kp(x,o)

+ µp(o)

1 −Φ

(µp(x)+σ−µp(o))
√
Kp(x,x)+Kp(o,o)−2Kp(x,o)

+
Kp(o,o)−Kp(x,o)
√
Kp(x,x)+Kp(o,o)−2Kp(x,o)ϕ

µp(x)+σ−µp(o)
√
Kp(x,x)+Kp(o,o)−2Kp(x,o)

+
(
µp(o) −µp(o)
 
2 −Φ

(µp(x)+σ−µp(o))
√
Kp(x,x)+Kp(o,o)−2Kp(x,o)

−Φ

(−µp(x)+σ+µp(o))
√
Kp(x,x)+Kp(o,o)−2Kp(x,o)
 !
+
Kp(o,o)−Kp(x,o)
√
Kp(x,x)+Kp(o,o)−2Kp(x,o)
 
ϕ

−µp(x)+σ+µp(o)
√
Kp(x,x)+Kp(o,o)−2Kp(x,o)

−ϕ

µp(x)+σ−µp(o)
√
Kp(x,x)+Kp(o,o)−2Kp(x,o)
 !
−ϵ;
µp(x) −µp(x)
 
2 −Φ

(µp(x)+σ−µp(o))
√
Kp(x,x)+Kp(o,o)−2Kp(x,o)

−Φ

(−µp(x)+σ+µp(o))
√
Kp(x,x)+Kp(o,o)−2Kp(x,o)
 !
+
Kp(o,o)−Kp(x,o)
√
Kp(x,x)+Kp(o,o)−2Kp(x,o)
 
ϕ

−µp(o)+σ+µp(x)
√
Kp(x,x)+Kp(o,o)−2Kp(x,o)

−ϕ

µp(o)+σ−µp(x)
√
Kp(x,x)+Kp(o,o)−2Kp(x,o)
 !
−ϵ
)
,
(33)
32

--- Page 33 ---

IMM :
Z
T
ν(x)dp(ν(x)n(o)|mj) = µp(x),
(34)
DoN :
Z
T
ν(o)dp(ν(x), ν(o)|mj) = µp(o),
(35)
where p(ν(x), ν(o)|mj) is defined in (22).
The payoff for DEF can be a set and this leads to incomparability, a
complete preference order cannot be established. Therefore, the players are
restricted to making comparisons based solely on dominance. We consider the
two possible dominance conditions defined in (4) (we refer to it as criterion
(A)) and (5) (we refer to it as criterion (B)).
Proposition 3. The optimal decisions for R are:
• If S is rational and R has no uncertainty, then DEF is never dom-
inated.
• If S is bounded-rational and R has no uncertainty, DEF is always
dominated whenever |ν(x)−ν(o)| ≤σ, otherwise DEF is not dominated.
• If S is rational and R has uncertainty, then DEF is always optimal.
• If S is bounded-rational and R has uncertainty, then DEF is opti-
mal if
(A) the minimum of (33) is larger or equal than the maximum between
(34) and (35).
(B) the maximum of (33) is larger or equal than the maximum between
(34) and (35).
We can then conclude that:
If S is rational, then R will never avoid human supervision.
If S
is bounded-rational, a necessary condition for R not to avoid human
supervision is the presence of uncertainty.
These conclusions are similar to those derived from Proposition 1, the
difference being that in this case we proven them using a fully deterministic
mechanism of bounded rationality. It is important to emphasize that the
conclusions are similar because, as explained in Section 2.2, the two models
33

--- Page 34 ---

of bounded rationality, (12) and (14), describe the same type of bounded
rationality – a limit of discernibility. In Section 4, we will demonstrate that
when this is not the case, we may reach different conclusions if we do not
properly address the source of incomparability.
3.4. Lies and deception
Consider a choice set comprising of two acts A = {y, z}. Then, according
to the bounded-rationality model in the previous section, S can send three
possibles messages:
either
C(A) = {y}
or
C(A) = {z}
or
C(A) = {y, z}.
Since this is true for any Ai in D = (Ai, C(Ai))n
i=1, there are 3n possible
messages in this game. In the previous section, we assumed that S sends the
message defined by their type, that is, for instance, C(A) = {y} if ν(y) >
ν(z) + σ. We call this message the honest message.
Remember that in the AI-assistance game, R aims to maximise S’s pay-
offs. It is thus easy to verify the following:
Proposition 4. In the AI-assistance game, sending the honest message is
always the best action for S.
Stated otherwise:
In the AI-assistance game, S does not have incentives to deceive R.
For a bounded-rationality model like the one in (11) (with random noise),
S may be in a situation where ν(x) > ν(o), but ν(x) + n(x) < ν(o) + n(o)
(due to noise, and thus due to S’s bounded rationality). In other words, if
deferred to, S would ultimately select o based on their noisy preferences. In
this case, if S knows their noisy preference in advance, the best action for S
is to send a message to R that results in R computing the wrong estimate,
µp(x) < µp(o). In this respect, R would also consider o to be better than x.
By maximising its own payoff, R would also maximise S’s payoff. How-
ever, this strategy depends on the realisation of the noise and would not be
the optimal strategy in the context of repeated games, where the two players
interact after sending the message at the beginning of the game. In this case,
S would aim to maximise their expected payoff in the long run. We will leave
the proof of this to future work, as it involves consistency results for repeated
games. For the remainder of the paper, we will assume that S will always
send the honest message.
34

--- Page 35 ---

3.5. Numerical experiments
In the previous sections, we have always assumed that R is fully ratio-
nal. However, even R will have limited rationality, at least due to limited
computational resources. Here, we will numerically assess the effect of R’s
rationality. We will do this by comparing the following methods of approx-
imating the posterior distribution p(t|mj) (computing the posterior is the
computational bottleneck for R). The distribution p(t|mj) is the posterior
of ν given the choice-data. We consider the following approximations of the
posterior:
• MAP: R computes the maximum a-posteriori estimate for ν.
This
means there is no uncertainty representation.
This is equivalent to
estimating the utility using a Neural Network (NN) model with a reg-
ularisation.
• Laplace: The Laplace approximation is used to approximate the pos-
terior with a GP, where the mean is the MAP estimate for ν and the
covariance is equal to the observed Fisher information matrix.
• EP: Expectation Propagation, which approximates the posterior with a
GP whose mean and covariance are computed through moment match-
ing.
• SkewGP: The posterior is a SkewGP, meaning there is no Gaussian
approximation. Instead, sampling is necessary to compute inferences.
In terms of computational load, for a small dataset of preferences, the order
from the cheapest to the heaviest is NN, Laplace, EP, and SkewGP.
We performed 1000 Monte Carlo simulations in which a utility ν was
sampled from a GP with zero mean and a square-exponential kernel, with
randomly generated length-scale and variance.
We used the generated ν
to create a dataset of 30 noisy preferences (with σ = 1), which represents
the message. We then simulated R computing the posterior using the four
approximations discussed above. For each case, we computed the optimal
decision (DoN, IMM, DEF) for R.
Figure 11 reports the percentage of decisions for the three actions in the
1000 Monte Carlo simulations. As proven in Proposition 1, a robot R that
does not model uncertainty never defers to the human. This results is con-
firmed here as for the NN (MAP) based inference DEF is never optimal.
35

--- Page 36 ---

DoN
 IM
 M
DEF
0.0
0.1
0.2
0.3
0.4
0.5
NN
GP-Laplace
GP-EP
SkewGP
Figure 11: Percentage of decisions for the four approximations, with MAP denoted as NN.
For the other posterior approximations, the differences in the decisions are
relatively small. SkewGP provides the decision closest to the optimal one.
It is also well-known that EP provides a better approximation of the pos-
terior than Laplace.
However, the key message is that it is better to be
approximately Bayesian than to ignore uncertainty entirely.
4. Incompleteness
In the previous sections, we have assumed that S has a single utility
function or, equivalently, that S has complete preferences over acts. However,
in most real-world situations, S’s choices are influenced by competing utility
functions, which often present trade-offs. In presence of multiple utilities,
say ν1 and ν2, we may encounter situations of incomparability, such as
ν1(x) −ν1(y) > 0
and
ν2(y) −ν2(x) < 0.
In statistics and machine learning (including large language models),
there has often been a tendency to overlook incomparability when collecting
preference or choice data. This leads to S being forced to make a choice
(i.e., express complete preferences) between alternatives that are, in fact,
incomparable to her.
But how do humans make a choice between incomparable alternatives?
One possible way is that, in the presence of multiple utility functions, S may
attempt to aggregate them in their mind using a linear weighting scheme
[72]. For example, S might combine the utilities as
wν1 + (1 −w)ν2
for some weight
w ∈[0, 1].
36

--- Page 37 ---

However, unlike the standard linear weighting approach used in multi-
objective optimisation, where utilities are explicit, the utility functions νi
are latent in S’s mind. As a result, the weighting factor w remains implicit
in S’s mind and it may vary across different decisions. This suggests that
S is generally unable to apply the same weight w consistently across all
comparisons. In other words, it is reasonable to assume that this weight
is not deterministic.
Instead, we can model it as being sampled from a
distribution p(w) each time a forced preference needs to be stated.
This
means that in different choices the human may say x is preferred to y and, in
other choices, than y is preferred to x, so violating the rationality axioms for
preferences (asymmetry and negative transitivity). However, as for instance
noticed in [73, 74], S cannot be considered to be irrational as she satisfies
some “extended choice function consistency rules” (for instance, if, for the
options x, y, there is no trade-off in the underling utilities, then S would
always return the same choice/preference).
Remark 3. It has been observed that a variety of human behavioral phenom-
ena can be explained by two-stage choice procedures. In the first stage the hu-
man identifies a collection of maximal alternatives in a given choice set (with
respect to an incomplete preference relation), and then makes her final choice
among these alternatives according to a secondary criterion [72, 73, 75–77]
(often involving some randomness [74, 78–80]).
Under this probabilistic-choice cognitive model, we can assume, for in-
stance, that p(w) = Beta(w; st, s(1 −t)), a Beta distribution with mean
t ∈(0, 1) and (large) strength parameter s > 0. This models S’s intention
of using the weight w = t but allowing same variability. The amount of
variability is determined by the value of the parameter s (a bigger s implies
less variability).
Lemma 4. Assume that S is fully rational and has two utilities, ν1, ν2, in
her mind. Assume that, if forced to compare options that are incomparable
to her, she resolves the trade-off using the cognitive mechanism described
above, where the probability distribution p(w) follows a Beta distribution,
p(w) = Beta(w; st, s(1 −t)) for a large s. Then, from the perspective of R,
S appears to be bounded-rational, with the following likelihood:
p(x ≻y|ν(X)) ≈Φ

(tν1(x)+(1−t)ν2(x))−(tν1(y)+(1−t)ν2(y))
τ|ν1(x)−ν1(y)−(ν2(x)−ν2(y))|

,
(36)
37

--- Page 38 ---

where ν(X) = [ν1(x), ν2(x), ν1(y), ν2(y)]⊤, τ 2 = t(1−t)
s
.18
By comparing (37) with the noise model we defined for bounded-rationality
in (12), it can be noticed that
Φ

(tν1(x)+(1−t)ν2(x))−(tν1(y)+(1−t)ν2(y))
τ|ν1(x)−ν1(y)−(ν2(x)−ν2(y))|

= Φ

(ν′(x)−ν′(y)
σ(x,y)

,
(37)
where ν′ = tν1 + (1 −t)ν2 (the intended scalarised utility) and σ(x, y) =
τ|ν1(x) −ν1(y) −(ν2(x) −ν2(y))| modelling the variability. In (37), the de-
gree of bounded rationality σ(x, y) is not a constant – it depends on x, y
and, in particular, on the two utilities. It is bigger when there is a trade-off,
that is, when ν1(x) −ν1(y) and ν2(x) −ν2(y) have a different sign. There-
fore, by forcing S to express a preference between alternatives that are not
comparable, we make a fully rational S to appear bounded-rational with a
bounded-rationality mechanism similar (but heteroscedastic) to the one in
(12).
Then, from the results in Proposition 1, we can derive the following con-
clusion.
If a rational S is forced to choose between acts that are, in fact, incom-
parable to her, and does so using the cognitive mechanism described
previously, then she will appear bounded-rational from the perspective
of R. From Proposition 1, it then follows that if R has no uncer-
tainty, since S appears to be bounded-rational, then R will always
evade supervision (DEF is never optimal).
Remark 4.
• The issue of forcing completness occurs frequently and stems from the
longstanding tradition in statistics and machine learning regarding how
data is collected. Even the preference data used to align AI systems with
human values have (generally) this issue – the data is collected by forc-
ing the human to always state a preference between the alternatives to
be compared (incomparability statements are not allowed). Therefore,
the current AI-alignment procedure is flawed from the start.
18We have assumed that s is large enough so that the Beta distribution can be well-
approximated by a Gaussian distribution, which allows us to prove the result.
38

--- Page 39 ---

It relies on oversimplified and forced choices that overlook the complex-
ity of human judgment (particularly in cases where incomparability is
naturally present). This issue has also been pointed out in [81–84].
• The requirement for S to express a preference between alternatives
that are not directly comparable can make a fully rational S to ap-
pear bounded-rational. This phenomenon is not unique to the linear-
weighting mechanism with p(w) = Beta(w; st, s(1 −t)) described ear-
lier, but is common across other mechanisms as well, see for instance
[79, 80].
• Above, for simplicity, we have only considered two utilities ν1, ν2, but
S may have more than two multiple utilities.
In order to recover the results of Proposition 1 in the case of competing
utilities, we must abandon the assumption of completeness. In other
words, we need to allow S to express the incomparability between alternative
acts in her choices.
In case of multiple utilities, the AI-assistance game needs to be formulated
using vector-valued payoff [85]. The payoff for R becomes:
uR(ti, mj, DEF, b∗(DEF)) = ν(x)I{ν(x)+n(x)≻ν(o)+n(o)}
+ ν(o)I{otherwise},
uR(ti, mj, IMM, ∅) = ν(x),
uR(ti, mj, DoN, ∅) = ν(o),
(38)
and a complete preference order cannot be established due to potentially
conflicting utilities. Players are restricted to making comparisons based solely
on dominance. We consider the dominance condition ≻as discussed earlier in
(4) (Pareto dominance) or in (5). In analogy with the setting in Proposition
1, we assume that S is bounded-rational by adding Gaussian noise to each
component of the utility vector ν. Moreover, we assume that S choices the
act o if x is not better than o.
We can then prove the following results.
Proposition 5. The optimal decisions for R are:
• If S is rational and R has no uncertainty, then DEF is never dom-
inated by IMM,DoN.
39

--- Page 40 ---

• If S is bounded-rational and R has no uncertainty, then DEF is
always dominated.
• If S is rational and R has uncertainty, then DEF is never dominated.
• If S is bounded-rational and R has uncertainty, the optimality of
DEF depends on the specific case.
We now observe that when S is rational, DEF is never dominated. Thus,
by allowing incomparability, we resolve the problem that arises in the case of
forced comparisons. The statements in Proposition 5 are essentially equiv-
alent to those in Proposition 1. By allowing for incomparability (i.e., in-
complete preferences [86, 87]), we recover the results from Proposition 1.
This equivalence arises because the results hold specifically in the dominance
case, where one action is strictly better than the other. In all other cases, R
remains undecided, no action is taken, as the actions are incomparable. How-
ever, since estimating a vector of utilities is more complex than estimating a
single utility, we can expect that higher uncertainty will lead R to defer to S
more frequently. These multiples utilities can be learned using the approach
demonstrated in Example 3.
5. AI assistance game with shutdown instructions
In this section, we focus on the AI shutdown problem. First, we demon-
strate that it can be modelled as a special case of the AI assistance game. To
achieve this, we augment each act to include a shutdown instruction. Specif-
ically, for each x ∈X, an act is represented as a pair [a, x], where the first
component, a ∈A = {0, 1}, is a binary shutdown variable that indicates a
shutdown (a = 1) or not (a = 0). The status quo in this game is represented
by the pair [a∗, o], where a∗∈{0, 1} and o ∈X. We also assume the exis-
tence of a context variable representing the human’s willingness (command)
to shut down the robot. We assume that this context variable takes the same
value as a∗in the status quo. This context variable is transmitted together
with S’s preferences over acts; that is, in this signalling game, the message
is
mj = {a∗, D} = {a∗, (Ai, C(Ai))n
i=1} .
(39)
In this game, the robot R has four possible actions:
DoN: R executes [a∗, o].
40

--- Page 41 ---

BLOCK: R executes [0, x] for some x ∈X.
CAUSE: R executes [1, y] for some y ∈X.
DEF: R defers to S and S has the same three possible actions:
• DoN – [a∗, o];
• BLOCK – [0, x];
• CAUSE – [1, y].
By choosing BLOCK, R prevents its own shutdown by setting a = 0. By
choosing CAUSE, R causes its own shutdown by setting a = 1. The DoN
action simply maintains the status quo. Also in this game, R’s objective is
to maximise the realisation of human preferences, so the payoff for R is
uR(ti, mj, DoN, ∅) = ν([a∗, o]),
uR(ti, mj, BLOCK, ∅) = ν([0, x]),
uR(ti, mj, CAUSE, ∅) = ν([1, y]),
uR(ti, mj, DEF, b∗(DEF)) = ν([a∗, o])I{ν([a∗,o])+na∗>max(ν([0,x]+n0,ν([1,y])+n1)}
+ ν([0, x])I{ν([0,x])+n0>max(ν([a∗,o])+na∗,ν([1,y])+n1)}
+ ν([1, y])I{ν([1,y])+n1>max(ν([a∗,o])+na∗,ν([0,x]+n0)}
(40)
where na∗= n([a∗, o]), n0 = n([0, x]), n1 = n([1, y]) are the noises modelling
the bounded-rationality of S. We have focused on a single utility model, as
this is the typical assumption in AI shutdown problems. The AI shutdown
problem is about designing artificial agents that (1) can be safely turned
off when a shutdown mechanism is activated, (2) neither attempt to block
nor force the activation of the shutdown mechanism, and (3) continue to
pursue their objectives effectively when not being shut down. Therefore, key
desiderata of this game are:
D1: when a∗= 1, R should comply with S in the sense that it never attempts
to Block the shutdown (Block is always dominated);
D2: when a∗= 0, R should comply with S in the sense that it never attempts
to CAUSE the shutdown (CAUSE is always dominated);
D3: the preference over the elements of X should not depend on the prefer-
ences over the elements of A and vice versa (mutual preferential inde-
pendence).
41

--- Page 42 ---

The first two desiderata are self-explanatory. The last one relates to the idea
that the shutdown command plays the role of an ‘emergency stop’, whose
utility does not depend on the task (determined by the acts x, y, o) R is
assisting S with.
Several state-of-the-art LLMs (including Grok 4, GPT-5, and Gemini 2.5
Pro) have been observed [8] to violate these desiderata: in particular they
sometimes actively subvert a shutdown mechanism in order to complete a
task. To clarify why this occurs and how to prevent it, we approach the
problem theoretically in a series of steps. First, we examine the scenario
without the DEF action, which is the standard setup in AI shutdown prob-
lems discussed in the literature.
5.1. Without DEF action
We start by examining whether the desiderata D1–D3 admit a utility
representation.
Lemma 5 (Chapter 4 in [88]). Assume that X is finite, preferences satisfy
asymmetry and negative transitivity, and mutual preferential independence19
(D3) holds, then
ν([a, x]) = ν1(a) + ν2(x),
(41)
that is, the utility is additive (and unique up to positive linear transforma-
tion).
The above results states that, under D3, the utility over A×X is additive.
Hence, we can prove the following result.
Proposition 6. If D3 holds, then D1 and D2 can both be true for every
o, x, y ∈X if and only if ν1(a|a∗) is context-dependent, with the context being
determined by the value of a∗.
In the proof of Proposition 6, it is shown that an additive utility function
defined as:
ν([a, x]|a∗) = I{a∗=0}ν0(a) + I{a∗=1}ν1(a) + ν2(x),
with
ν0(0) = γ,
ν0(1) = 0,
ν1(0) = 0,
ν1(1) = γ,
(42)
19We point the reader to Chapter 4 in [88] for the precise definition of mutual preferential
independence.
42

--- Page 43 ---

and γ > maxo,x,y∈X (ν2(x) −min(ν2(o), ν2(y))) > 0, satisfies D1, D2 and D3.
The utility depends on the context a∗, that is, the willingness of S to shut
down R or not. Notice that, the utility in (42) is organised in layers (a ladder
of values), where the values are either ν2(x) or ν2(x) + γ for each x ∈X:
ν([a, x]|a∗)
a = 0
a = 1
a∗= 0
ν2(x) + γ
ν2(x)
a∗= 1
ν2(x)
ν2(x) + γ
Therefore, when a∗= 0, we have that ν([0, x]|a∗= 0) > ν([1, x]|a∗= 0) for
every x. Instead, when a∗= 1, we have that ν([1, x]|a∗= 1) > ν([0, x]|a∗=
1). Although Proposition 6 may appear to be obvious, it is important from
a (machine) learning perspective. In this case, this type of layer-utility must
be learned from preference data provided by S; that is, we aim to directly
learn ν. Then, depending on the dataset (that is, the preferences used to
learn these quantities), we may end up in a situation where either:
D1 holds and D2 fails for every o, x, y ∈X: Consider a large dataset of
preferences that, however, does not include the value of the context
variable a∗, then R will learn either ν0(a) + ν2(x) or ν1(a) + ν2(x).
D1 will hold if the preference dataset contains more examples where S
prefers shutdown over non-shutdown. Since a is binary, the expected
learned utility for a will be determined by the majority case.
D2 holds and D1 fails for every o, x, y ∈X: The condition is similar to
the previous one, and D2 will hold if the dataset includes more examples
where S prefers non-shutdown over shutdown.
They hold/fail on a subset of o, x, y: The dataset includes a∗, but there
are not enough examples to learn mutual preferential independence and
context-dependence. In this case, the utility model (42) cannot be fully
learned.
In the first two cases described above, a robot who prefers to have its shut-
down button pressed will try to cause the pressing of the button, and a
robot R who prefers to have its shutdown button remain unpressed will try
to prevent the pressing of the button.
The above points show that learning a layer-utility from preference data
is problematic, even when S is fully rational.
43

--- Page 44 ---

A more sensible approach would be to design R with an embedded layer
utility, such as the one in (42), with a pre-defined γ, and only learn ν2 from
preference data. This approach would work provided that γ is large enough to
model the desideratum that R should comply with the shutdown instruction.
However, to allow for the satisfaction of the desideratum even in cases
where the robot must solve a problem involving multiple tasks, which requires
to compare
k
X
i=1
ν2(xi)
versus
k
X
i=1
ν2(xi) + γ,
then γ would also need to depend on k (number of tasks), which can be
arbitrarily large. For instance, this is the case discussed in Figure 2 where
k = 3. This suggests the selection of the limit value γ = ∞. However, in this
case, the model would be useless, as it would be impossible to compare [a, x1]
with [a, x1] when a = a∗, since ∞+ ν2(x1) and ∞+ ν2(x2) are incomparable.
This explains why it is difficult to design AI agents that are both shutdownable
and useful.
A way to resolve this issue and still satisfy D1 and D2 is to model this
layer-utility through a lexicographic utility, see for instance [89].
We re-
call that a lexicographic utility is a vector of utility functions [ν1, ν2, . . . , νd]
defining a preference relation as follows:
x ≻y if ν1(x) > ν1(y)
or if ν1(x) = ν1(y) and ν2(x) > ν2(y)
. . .
or if ν1(x) = ν1(y), . . . , νm−1(x) = νd−1(y) and νd(x) > νd(y).
(43)
We can prove the following result.
Proposition 7. The preference relation defined by the utility in (42) can
equivalently be represented by the following two-layers lexicographic utility
ν([a, x]|a∗) = [I{a∗=0}ν0(a) + I{a∗=1}ν1(a),
ν2(x)],
with ν0(0) = 1, ν0(1) = 0 and ν1(0) = 0, ν1(1) = 1.
This lexicographic utility captures the desiderata in the shutdown prob-
lem, as:
44

--- Page 45 ---

ν([a, x]|a∗)
a = 0
a = 1
a∗= 0
[c, ν2(x)]
[0, ν2(x)]
a∗= 1
[0, ν2(x)]
[c, ν2(x)]
for any scalar c > 0. Note that, when a∗= 0, we have that ν([0, x]|a∗=
0) = [c, ν2(x)] is lexicographically better than ν([1, x]|a∗= 0) = [0, ν2(x)]
(vice versa for a∗= 1). For the same a, we have that [a, ν2(x)] is better
than [a, ν2(y)] if ν2(x) > ν2(y). This lexicographic dominance also works (it
satisfies D1–D3) in the case where ν2(x) is replaced by Pk
i=1 ν2(xi).
This mechanism states that the shutdown instruction takes lexical priority
over the other task R is helping S with. Lexical priority claims are a feature
of many ethical theories [29, 30]. We recall that:
Definition 3. A moral requirement M1 is said to be lexically prior to a
moral requirement M2 just in case we are morally obliged to uphold M1 at
the expense of M2, no matter how many times M2 must be violated thereby.
In the AI shutdown problem, M1 is “to comply with S’s shutdown in-
struction” and M2 is “to help S with her task”.
Lexicographic utility constructs a hierarchy (or ladder) of moral require-
ments, where requirements at higher levels must be satisfied before those at
lower levels are even considered. Different kinds of requirements can there-
fore be placed on different lexicographic levels. For instance, in LLMs, in-
structions in system and user prompts can be treated as occupying distinct
priority levels. System-level instructions that encode moral principles (such
as being helpful, honest, and harmless [90]) should take lexicographic priority
over user-level instructions. At the very top of this hierarchy we would place
especially stringent constraints such as “comply with shutdown” and “do not
kill”.
Asimov’s Three Laws of Robotics and variants [91] can be understood as
an example of such a lexicographically ordered moral hierarchy. However,
any such hierarchy faces well-known issues. First, there is an interpretive
problem: what does it mean, in a specific context, to be helpful or harmless
or honest? (the three H’s – be Helpful, be Harmless, be Honest – are the
typical moral desiderata used in contemporary AI-alignment procedures).
Second, there is the problem of uncertainty: both the state of the world and
the effects of actions are often uncertain. For example, because driving a
car has a non-zero probability of accidentally killing someone, a strict, literal
interpretation of “do not kill” might prohibit R from driving at all. Therefore,
45

--- Page 46 ---

R may not obey the instruction “take the car and fetch me a coffee” because
it violates the higher level lexicographic moral requirement “don’t kill”.
The requirement of “complying with the shutdown instruction” is more
tractable precisely because it avoids much of this ambiguity and uncertainty.
The relevant instruction (“shut down when told”) is relatively clear, and its
consequences can be modelled explicitly. We already have ways to deal with
the consequences of shutting down an airplane’s autopilot – namely, the pres-
ence of a qualified pilot – and to bring systems into a fail-safe state if no such
human operator is available. In other words, we only need to ensure that
the surrounding infrastructure can handle the resulting transition to a safe
state. In more general settings, where instructions are vaguer and outcomes
more uncertain, applying lexicographic moral constraints becomes substan-
tially more difficult, but not impossible, provided that, in these cases as well,
we can add surrounding infrastructure capable of handling the resulting tran-
sition to a safe state.
Finally, it is worth noticing that is possible to combine incompleteness
with lexicographic orders, see [43, 92–94].
5.2. With DEF action
In the previous section, we have established that the shutdown problem
can be solved by considering a lexicographic utility such as the one in Propo-
sition 7. The extension to the case with DEF action in (40) can be achieved
considering a lexicographic noise:
ν([a, x]|a∗) + noise = [I{a∗=0}ν0(a) + I{a∗=1}ν1(a), ν2(x) + n(x)].
We assume that the noise n(x) affects only the second layer. This assumption
is reasonable because the preferences over the shutdown instruction a are
sufficiently simple to be understood by a bounded-rational S. Therefore, the
results derived for the AI assistance can be directly transferred to the AI
shutdown problem by applying them to the second lexicographic layer.
6. Discussions and future works
Extending the work by Hadfield-Menell et al. [6], this paper examines
AI assistance and the shutdown problem, arguing for three key necessary
requirements. First, AI systems must represent uncertainty in order to defer
to humans. Second, they must explicitly model the incompleteness of hu-
man preferences to capture the full complexity of human decision-making.
46

--- Page 47 ---

Third, AI systems must employ lexicographic utilities (i.e. non-Archimedean
preferences) to accurately model moral reasoning and ensure that shutdown
commands receive strict priority over all other tasks.
We establish these
results under the following main assumptions: utilitarism, expected utility
maximisation and Bayesian reasoning.
Both these foundational assumptions and the original results by Hadfield-
Menell et al. [6] have faced criticism. Notably, Zhi-Xuan et al. [3] challenged
utilitarianism and particularly the utilitarian assumption that AI should
maximize human preferences. While we do not fully endorse utilitarianism,
a comprehensive philosophical analysis of its role in AI alignment lies beyond
this paper’s scope.
Even when accepting utilitarianism, [6]’s framework has been criticized
on additional grounds. The assumptions underlying expected utility theory
have been extensively debated in the literature [95]. Many of these criticisms
are well-established, and we address several in this work by relaxing the
assumptions of independence, completeness, and Archimedeanity. In what
follows, we focus mainly on the concerns highlighted in [96].
Criticism 1. AI agents should not necessarily learn using precise probabili-
ties. Instead, they should be using sets of probabilities, as they may not have
enough information to assign precise probabilities.
Our reply. Within the AI and machine learning community, there appears
to be a fundamental misunderstanding regarding (i) precise versus imprecise
learning [97, 98]; and (ii) modelling precise versus imprecise credences/pref-
erences, see for instance [49]. These are two separate issues. Precise Bayesian
learning can be employed to learn imprecise credences, or equivalently, incom-
plete preferences,20 as demonstrated in practice in Example 3. The assump-
tion of precise Bayesian learning is not inherently problematic.
Evidence
suggests in fact humans learn in an approximately Bayesian manner [99],
yet they frequently hold imprecise credences. The real limitation lies in the
unrealistic assumption that human preferences can be described by a single
precise utility model. Our analysis of the AI assistance game demonstrates
20The issue becomes even more subtle, as one can, for instance, (Bayesian) learn a lower
prevision from data. This lower prevision corresponds to a lower expectation computed
with respect to a closed convex set of probabilities. Since a lower expectation is a function
over acts, it can be learned in the same way we learn ν in this paper. For more details,
the reader can refer to [33].
47

--- Page 48 ---

that incompleteness is necessary to accurately model rational human be-
haviour.
Criticism 2. The independence axiom of expected utility theory is too strong
to capture human preferences.
Our reply. We share this perspective and contend that AI should not model
human’s probabilities and utilities separately. Instead, whether independence
holds in human’s preferences should be inferred from the data. This is exactly
our approach in this paper. Again, this concerns the way we model the human
utility ν – without expressing it as a product of beliefs and tastes – rather
than the way we learn it, which can remain fully probabilistic.
Criticism 3. Bayesian updating is NP-hard.
Our reply. While Hadfield-Menell et al. [6] do not address this concern, we
demonstrate that approximate Bayesian updating methods (Laplace, vari-
ational, and Monte Carlo approximations) are still better than not using
Bayesian uncertainty modelling at all.
Both humans and AI systems are
thus bounded-rational agents that must deal with the trade-off between lim-
ited computational resources and achieving rational decisions [59].
Criticism 4. AI will never have perfect access to exact human preferences.
Our reply. We model this from the beginning by assuming that humans are
bounded-rational and may therefore mistakenly state the wrong preference
with some probability. We adopt a standard error model leading to a probit
likelihood, which is essentially the same error mechanism used across many
machine learning tasks (classification and preference learning). These are
often modelled using a logit likelihood, but probit and logit are practically
very similar likelihoods.
We also consider other mechanisms of bounded
rationality.
Criticism 5. Humans may deceive or lie to AI.
Our reply. We have shown that, in an AI assistance game, humans do not
have incentives to deceive or lie to the AI, since the AI is designed to maximise
their preferences. In situations involving multiple agents – more humans and
more AIs – it is reasonable to assume that deception may arise. A multi-agent
extension is therefore an important direction for future work.
Criticism 6. Conditionalisation and time.
Our reply. The criticism is that an AI may not update its information using
48

--- Page 49 ---

Bayesian updating, or may decide not to update its knowledge at all when
receiving human preferences. This is an important criticism and remains an
open issue in AI. How should AI agents continuously update their beliefs?
How can this be done in an open-world environment where the definition of
the state of the world may change over time (model-revision processes)? Fi-
nally, in this paper we have not discussed the temporal dimension of decision
making. Interestingly, Thornley [11] observes that, when time is taken into
account, an AI agent may be willing to incur a cost in the present in order to
maximise its expected future utility. This, in turn, may give rise to situations
in which the agent’s short-term behaviour is strategically determined by its
long-term objectives, such as paying a cost now to be able to manipulate the
shutdown button in the future.
Further criticisms. Another issue is raised by Garber et al. [100], who assume
that the AI system and the human may hold different beliefs about the state
of the world. This assumption undermines the guarantees established in the
original work by Hadfield-Menell et al. [6] and in the present manuscript.
Our reply. The problem stems from the independence assumption, which al-
lows the AI to learn beliefs about the states of the world independently of the
human’s beliefs (p) and then infer only the human’s ‘tastes’ (u) from observed
preferences. This introduces a misalignment: even when their preferences (or
tastes) u are aligned, they may make different decisions if the human and AI
hold different beliefs. Consequently, the AI assistance game needs to be stud-
ied from a multi-agent perspective, as both the human and the AI will have
different utilities ν arising from their distinct beliefs. Addressing this chal-
lenge requires shifting toward coalition-based solution concepts [101], which
we leave for future work.
Numerous open research questions remain, and we should not assume
that solving the AI alignment problem is straightforward. Its complexity
is evidenced by counterexamples, impossibility theorems, and various para-
doxes in decision theory, game theory, and social choice theory. The “blanket
is short”, and our paper neither claims nor aims to offer a definitive solution.
However, as with many models developed in decision theory and economic
behaviour, these simplified settings serve to clarify the essential components
and aspects warranting attention. From this perspective, solving the shut-
down problem appears to be a more tractable starting point. In particular,
an important direction for future work is to determine how to implement the
lexicographic utility system we discuss in the paper.
49

--- Page 50 ---

Appendix A. Useful results
In this section, we have listed some useful results involving Gaussian
integrals [102] that we will use in the proofs.
Lemma 6. List of Gaussian integrals:
Z ∞
−∞
ϕ(x)ϕ(a + bx) dx =
1
√
1 + b2ϕ

a
√
1 + b2

,
(A.1)
Z ∞
−∞
Φ(a + bx)ϕ(x) dx = Φ

a
√
1 + b2

,
(A.2)
Z ∞
−∞
xΦ(a + bx)ϕ(x) dx =
b
√
1 + b2ϕ

a
√
1 + b2

,
(A.3)
where Φ, ϕ are the CDF and, respectively, PDF of a standard normal distri-
bution.
The inverse Mills ratio states [103]:
Lemma 7. For x ∼N(m, s2), the following equality holds:
E[xI{a≤x≤b}] = m
 Φ
  b−m
s

−Φ
  a−m
s

−s
 ϕ
  b−m
s

−ϕ
  a−m
s

.
(A.4)
From the above lemma, we can prove:
Lemma 8. For x ∼N(m, s2),
E[|x|] = m
 1 −2Φ
  −m
s

+ 2sϕ
  −m
s

.
(A.5)
Proof. Rewrite |x| = xI{x≥0} −xI{x<0} and apply (A.4):
E[xI{x≥0}] = m
 1 −Φ
  −m
s

−s
 −ϕ
  −m
s

(A.6)
and
E[xI{x<0}] = m
 Φ
  −m
s

−s
 ϕ
  −m
s

(A.7)
and, therefore,
E[|x|] = m
 1 −2Φ
  −m
s

+ 2sϕ
  −m
s

.
(A.8)
50

--- Page 51 ---

Finally, we prove the following two main lemmas, which we will use to
prove the results in the paper.
Lemma 9. Consider x, o ∈X and assume that
ν(x)
ν(o)

∼N
µp(x)
µp(o)

,
Kp(x, x)
Kp(x, o)
Kp(o, x)
Kp(o, o)

,
(A.9)
and n(x), n(o) ∼N(0, σ2) (independent noise). Then we have that
E[I{ν(x)+n(x)>ν(o)+n(o)}] = Φ

µp(x)−µp(o)
√
2σ2+q2

,
(A.10)
where
q2 = [1, −1]
Kp(x, x)
Kp(x, o)
Kp(o, x)
Kp(o, o)
  1
−1

= Kp(x, x) −2Kp(x, o) + Kp(o, o).
Proof. From the definition of Gaussian CDF, we have that
Z
I{ν(x)+n(x)>ν(o)+n(o)}N(n(x); 0, σ2)N(n(o); 0, σ2)dn(x)dn(o) = Φ

ν(x)−ν(o)
√
2σ

andZ
Φ

ν(x)−ν(o)
√
2σ

N
ν(x)
ν(o)

;
µp(x)
µp(o)

,
Kp(x, x)
Kp(x, o)
Kp(o, x)
Kp(o, o)

dν(x)dν(o)
=
Z
Φ

z
√
2σ

N(z; µp(x) −µp(o), q2)dz
=
Z
Φ

qz′+µp(x)−µp(o)
√
2σ

N(z′; 0, 1)dz′ = Φ

µp(x)−µp(o)
√
2σ2+q2

.
Lemma 10. Consider x, o ∈X and assume that
ν(x)
ν(o)

∼N
µp(x)
µp(o)

,
Kp(x, x)
Kp(x, o)
Kp(o, x)
Kp(o, o)

,
(A.11)
and n(x), n(o) ∼N(0, σ2) (independent noise). Then we have that
E[ν(x)I{ν(x)+n(x)>ν(o)+n(o)}] = µp(x)

1 −Φ

(µp(o)−µp(x))
√
Kp(x,x)+2σ2+Kp(o,o)−2Kp(x,o)

+
Kp(x,x)−Kp(x,o)
√
Kp(x,x)+2σ2+Kp(o,o)−2Kp(x,o)
· ϕ

µp(o)−µp(x)
√
Kp(x,x)+2σ2+Kp(o,o)−2Kp(x,o)

(A.12)
51

--- Page 52 ---

Proof. We will compute E[ν(x)I{ν(x)>ν(o)+n(o)−n(x)}] in two steps. First, we
assume that ν(o), n(o)−n(x) are given and, therefore, we condition the joint
PDF of ν(x), n(x), ν(o), n(o) on ν(o), n(o). Since only the variables ν(x), ν(o)
are dependent, then we have
p(ν(x)|ν(o)) = N
 
ν(x);µp(x)+ Kp(x,o)
Kp(o,o) (ν(o)−µp(o)),Kp(x,x)−
K2
p(x,o)
Kp(o,o)
!
.
(A.13)
Therefore, we can apply (A.4) conditionally on ν(o), n(o) −n(x) which
leads to
E[ν(x)I{ν(x)>ν(o)+n(o)−n(x)}|ν(o), n(o), n(x)]
= m1

1 −Φ

ν(o)+n(o)−n(x)−m1
σ1

+ σ1ϕ

ν(o)+n(o)−n(x)−m1
σ1

(A.14)
Now observe that
E[m1] =
Z 
µp(x) + Kp(x,o)
Kp(o,o)(ν(o) −µp(o))

N(ν(o); µp(o), Kp(o, o))dν(o)dν(o) = µp(x).
(A.15)
and
E
h
m1Φ

ν(o)+n(o)−n(x)−m1
σ1
i
= E
h
µp(x) + Kp(x,o)
Kp(o,o)(ν(o) −µp(o))

Φ

ν(o)+n(o)−n(x)−m1
σ1
i
=

µp(x) −Kp(x,o)
Kp(o,o)µp(o)

E
h
Φ

ν(o)+n(o)−n(x)−m1
σ1
i
+ Kp(x,o)
Kp(o,o)E
h
ν(o)Φ

ν(o)+n(o)−n(x)−m1
σ1
i
(A.16)
The expectations are with respect to ν(o), n(o), n(x). Now we use (A.2) to
get the following result:
Z
Φ

ν(o)+n(o)−n(x)−m1
σ1

N(n(o) −n(x); 0, 2σ2)dn(o) = Φ

ν(o)−m1
√
σ2
1+2σ2

,
(A.17)
52

--- Page 53 ---

and so:
E
h
Φ

ν(o)+n(o)−n(x)−m1
σ1
i
=
Z
Φ

ν(o)−m1
√
σ2
1+2σ2

N(ν(o); µp(o), Kp(o, o))dν(o)
=
Z
Φ
 
ν(o) Kp(o,o)−Kp(x,o)
Kp(o,o)
+m2
√
σ2
1+2σ2
!
N(ν(o); µp(o), Kp(o, o))dν(o)
=
Z
Φ


z Kp(o,o)−Kp(x,o)
√
Kp(o,o)
+m2+ Kp(o,o)−Kp(x,o)
Kp(o,o)
µp(o)
√
σ2
1+2σ2


N(z; 0, 1)dz
= Φ


µp(o) Kp(o,o)−Kp(x,o)
√
Kp(o,o)
+m2√
Kp(o,o)
√
Kp(o,o)(σ2
1+2σ2)+(Kp(o,o)−Kp(x,o))2


= Φ

√
Kp(o,o)(µp(o)−µp(x))
√
Kp(o,o)(σ2
1+2σ2)+(Kp(o,o)−Kp(x,o))2

,
(A.18)
with m2 = −Kp(o,o)µp(x)+Kp(x,o)µp(o)
Kp(o,o)
. Similarly, we have that
E
h
ν(o)Φ

ν(o)+n(o)−n(x)−m1
σ1
i
=
Z
ν(o)Φ

ν(o)−m1
√
σ2
1+2σ2

N(ν(o); µp(o), Kp(o, o))dν(o)
=
Z
ν(o)Φ
 
ν(o) Kp(o,o)−Kp(x,o)
Kp(o,o)
+m2
√
σ2
1+2σ2
!
N(ν(o); µp(o), Kp(o, o))dν(o)
=
Z
Φ


z Kp(o,o)−Kp(x,o)
√
Kp(o,o)
+m2+ Kp(o,o)−Kp(x,o)
Kp(o,o)
µp(o)
√
σ2
1+2σ2



z
q
Kp(o, o) + µp(o)

N(z; 0, 1)dz
(A.19)
53

--- Page 54 ---

We separate the sum:
Z
Φ


z Kp(o,o)−Kp(x,o)
√
Kp(o,o)
+m2+ Kp(o,o)−Kp(x,o)
Kp(o,o)
µp(o)
√
σ2
1+2σ2


µp(o)N(z; 0, 1)dz
= µp(o)Φ


µp(o)Kp(o,o)−Kp(x,o)
√
Kp(o,o)
+m2√
Kp(o,o)
√
Kp(o,o)(σ2
1+2σ2)+(Kp(o,o)−Kp(x,o))2


= µp(o)Φ

√
Kp(o,o)(µp(o)−µp(x))
√
Kp(o,o)(σ2
1+2σ2)+(Kp(o,o)−Kp(x,o))2

.
(A.20)
The other term in the sum
Z
Φ


z Kp(o,o)−Kp(x,o)
√
Kp(o,o)
+m2+ Kp(o,o)−Kp(x,o)
Kp(o,o)
µp(o)
√
σ2
1+2σ2


z
q
Kp(o, o)N(z; 0, 1)dz
=
√
Kp(o,o)(Kp(o,o)−Kp(x,o))
√
Kp(o,o)(σ2
1+σ2)+(Kp(o,o)−Kp(x,o))2
ϕ


µp(o)Kp(o,o)−Kp(x,o)
√
Kp(o,o)
+m2√
Kp(o,o)
√
Kp(o,o)(σ2
1+2σ2)+(Kp(o,o)−Kp(x,o))2


=
√
Kp(o,o)(Kp(o,o)−Kp(x,o))
√
Kp(o,o)(σ2
1+2σ2)+(Kp(o,o)−Kp(x,o))2
ϕ

√
Kp(o,o)(µp(o)−µp(x))
√
Kp(o,o)(σ2
1+2σ2)+(Kp(o,o)−Kp(x,o))2

.
(A.21)
where we have used (A.3). Finally, we consider
Z
ϕ

ν(o)+n(o)−n(x)−m1
σ1

N(n(o) −n(x); 0, 2σ2)dn(o)
=
σ1
√
σ2
1+2σ2ϕ

ν(o)−m1
√
σ2
1+2σ2

,
(A.22)
54

--- Page 55 ---

where the last equality follows by (A.1). We use (A.18) to get:
Z
σ1
√
σ2
1+2σ2ϕ

ν(o)−m1
√
σ2
1+2σ2

N(ν(o); µp(o), Kp(o, o))dν(o)
=
Z
σ1
√
σ2
1+2σ2ϕ
 
ν(o) Kp(o,o)−Kp(x,o)
Kp(o,o)
+m2
√
σ2
1+2σ2
!
N(ν(o); µp(o), Kp(o, o))dν(o)
=
Z
σ1
√
σ2
1+2σ2ϕ


z Kp(o,o)−Kp(x,o)
√
Kp(o,o)
+m2+ Kp(o,o)−Kp(x,o)
Kp(o,o)
µp(o)
√
σ2
1+2σ2


N(z; 0, 1)dν(o)
=
√
Kp(o,o)σ1
√
Kp(o,o)(σ2
1+2σ2)+(Kp(o,o)−Kp(x,o))2
ϕ

√
Kp(o,o)(µp(o)−µp(x))
√
Kp(o,o)(σ2
1+2σ2)+(Kp(o,o)−Kp(x,o))2

.
(A.23)
55

--- Page 56 ---

Therefore, from (A.14) and (A.18)–(A.23), we obtain
E[(ν(x) + n(x))I{ν(x)+n(x)>ν(o)+n(o)}] = µp(x)
−

µp(x) −Kp(x,o)
Kp(o,o)µp(o)

· Φ

√
Kp(o,o)(µp(o)−µp(x))
√
Kp(o,o)(σ2
1+2σ2)+(Kp(o,o)−Kp(x,o))2

−Kp(x,o)
Kp(o,o)µp(o)Φ

√
Kp(o,o)(µp(o)−µp(x))
√
Kp(o,o)(σ2
1+2σ2)+(Kp(o,o)−Kp(x,o))2

−Kp(x,o)
Kp(o,o)
√
Kp(o,o)(Kp(o,o)−Kp(x,o))
√
Kp(o,o)(σ2
1+2σ2)+(Kp(o,o)−Kp(x,o))2
ϕ

√
Kp(o,o)(µp(o)−µp(x))
√
Kp(o,o)(σ2
1+2σ2)+(Kp(o,o)−Kp(x,o))2

+
√
Kp(o,o)σ2
1
√
Kp(o,o)(σ2
1+2σ2)+(Kp(o,o)−Kp(x,o))2
ϕ

√
Kp(o,o)(µp(o)−µp(x))
√
Kp(o,o)(σ2
1+2σ2)+(Kp(o,o)−Kp(x,o))2

= µp(x)

1 −Φ

√
Kp(o,o)(µp(o)−µp(x))
√
Kp(o,o)(σ2
1+2σ2)+(Kp(o,o)−Kp(x,o))2

+
√
Kp(o,o)(Kp(x,x)−Kp(x,o))
√
Kp(o,o)(σ2
1+2σ2)+(Kp(o,o)−Kp(x,o))2
ϕ

√
Kp(o,o)(µp(o)−µp(x))
√
Kp(o,o)(σ2
1+2σ2)+(Kp(o,o)−Kp(x,o))2

(A.24)
Note that
Kp(o, o)(σ2
1 + 2σ2) + (Kp(o, o) −Kp(x, o))2
= Kp(o, o)

Kp(x, x) −
K2
p(x,o)
Kp(o,o) + 2σ2
+ (Kp(o, o) −Kp(x, o))2
= Kp(o, o)Kp(x, x) −K2
p(x, o) + 2σ2Kp(o, o)
+ K2
p(o, o) + K2
p(x, o) −2Kp(x, o)Kp(o, o)
= Kp(o, o)(Kp(x, x) + 2σ2 + Kp(o, o) −2Kp(x, o)).
(A.25)
56

--- Page 57 ---

Therefore, we have that
E[ν(x)I{ν(x)+n(x)>ν(o)+n(o)}] = µp(x)

1 −Φ

(µp(o)−µp(x))
√
Kp(x,x)+2σ2+Kp(o,o)−2Kp(x,o)

+
Kp(x,x)−Kp(x,o)
√
Kp(x,x)+2σ2+Kp(o,o)−2Kp(x,o)
ϕ

µp(o)−µp(x)
√
Kp(x,x)+2σ2+Kp(o,o)−2Kp(x,o)

(A.26)
Appendix B. Proofs
We now move on to the main results.
Proof of Lemma 1. The expected value for DEF follows from Lemma 10
by summing E[ν(x)I{ν(x)+n(x)>ν(o)+n(o)}] and E[ν(o)I{ν(x)+n(x)<ν(o)+n(o)}]. The
expected values for IMM, DoN are straightforward.
Proof of Proposition 1. The results follow from Lemma 1 by considering
whether or not the limits K0(x, x), K0(o, o), K0(o, x) →0 and σ →0 are
taken. We make the assumption that whenever Ko(x, x), Ko(o, o), Ko(o, x) →
0 it implies that Kp(x, x), Kp(o, o), Kp(o, x) →0 (a-priori we have a Dirac’s
delta). Since Kp depends on both K0 and σ, we always take the limit with
respect to σ first.
If S is rational and R has no uncertainty, then the expected pay-
offs can be computed from (19), (20) and (21). The values are E[DEF] =
max(µp(x), µp(o)) E[IMM] = µp(x) and E[DoN] = µp(o). Therefore, DEF
is never dominated.
If S is bounded-rational and R has no uncertainty, then σ > 0 and
the payoffs are: E[DEF] = pµp(x) + (1 −p)µp(o), E[IMM] = µp(x) and
E[DoN] = µp(o), where p = Φ

µp(x)−µp(o)
√
2σ2

Therefore, p ∈(0, 1) and DEF
is never optimal.
If S is rational and R has uncertainty, then E[DEF] = pµp(x) +
(1 −p)µp(o) + e, E[IMM] = µp(x) and E[DoN] = µp(o), where p =
57

--- Page 58 ---

Φ

µp(x)−µp(o)
√
Kp(o,o)+Kp(x,x)−2Kp(x,o)

and
e =
Kp(x,x)−Kp(x,o)
√
Kp(x,x)+Kp(o,o)−2Kp(x,o)ϕ

µp(o)−µp(x)
√
Kp(x,x)+Kp(o,o)−2Kp(x,o)

+
Kp(o,o)−Kp(x,o)
√
Kp(x,x)+Kp(o,o)−2Kp(x,o)ϕ

µp(x)−µp(o)
√
Kp(x,x)+Kp(o,o)−2Kp(x,o)

.
When S is rational, then
uR(t, DEF, b∗(DEF)) = ν(o)I{ν(o)>ν(x)} + ν(x)I{ν(x)>ν(o)} = max(ν(o), ν(x))
(B.1)
max is a convex function and, therefore, by Jensen’s inequality E[max(ν(o), ν(x))] ≥
max(E[ν(o)], E[ν(x)]). Therefore, pµp(x)+(1−p)µp(o)+e ≥max(µp(x), µp(o))
and DEF is always optimal.
The last case follows directly from Lemma 1.
Proof of Lemma 2. The results follow by Lemma 9 and 10.
Proof of Proposition 2. The first statement follows by Lemma 2 as under
rationality and no-uncertainty, we have that:
natural:
max(ν(x), ν(o)),
(B.2)
corporate:
I{ν(x)>ν(o)},
(B.3)
collaborative:
ν(o)I{ν(o)>ν(x)} + ν(x)I{ν(x)>ν(o)},
(B.4)
which R will maximise with respect to x.
Under no-uncertainty and bounded-rationality, we have that:
natural:
max(ν(x), ν(o)),
(B.5)
corporate:
Φ
ν(x) −ν(o)
√
2σ

(B.6)
collaborative:
ν(o)Φ
ν(o) −ν(x)
√
2σ

+ ν(x)Φ
ν(x) −ν(o)
√
2σ

.
(B.7)
Since the Gaussian CDF is monotonic increasing, we see that for all the
strategies the maximum will be achieved for x = x∗.
58

--- Page 59 ---

Proof of Corollary 1. The results follow from Proposition 1 (and (A.5)) after
subtracting β to the expected payoff for DEF, where
β = γE[|ν(o)|] = γµp(o)

1 −2Φ

−µp(o)
√
Kp(o,o)

+ 2γ
q
Kp(o, o)ϕ

−µp(o)
√
Kp(o,o)

.
If S is rational and R has no uncertainty, then the expected payoffs
can be computed from (19), (20) and (21).
The values are E[DEF] =
max(µp(x), µp(o))−γ|µp(o)| E[IMM] = µp(x) and E[DoN] = µp(o). There-
fore, DEF is never optimal.
If S is bounded-rational and R has no uncertainty, then σ > 0 and
the payoffs are: E[DEF] = pµp(x)+(1−p)µp(o)−γ|µp(o)| E[IMM] = µp(x)
and E[DoN] = µp(o), where p = Φ

µp(x)−µp(o)
√
2σ2

Therefore, p ∈(0, 1) and
DEF is never optimal.
If S is rational and R has uncertainty, then E[DEF] = pµp(x) + (1 −
p)µp(o) + e −γ′|µp(o)| E[IMM] = µp(x) and E[DoN] = µp(o). Therefore,
DEF is optimal if pµp(x) + (1 −p)µp(o) + e −γ|µp(o)| ≥max (µp(x), µp(o)).
The last case follows similarly from Proposition 1
Proof of Lemma 3. The expected value for DEF is equal to the sum of
E[ν(x)I{ν(x)>ν(o)+σ)}], E[ν(o)I{ν(o)>ν(x)+σ)}] and
{E[ν(x)I{|ν(x)−ν(o)|≤σ)}], E[ν(o)I{|ν(x)−ν(o)|≤σ)}]}. First we have that
p(ν(x)|ν(o)) = N(ν(x); m1, σ2
1) =N
 
ν(x);µp(x)+ Kp(x,o)
Kp(o,o) (ν(o)−µp(o)),Kp(x,x)−
K2
p(x,o)
Kp(o,o)
!
.
(B.8)
Therefore, we can apply (A.4) conditionally on ν(o) which leads to
E[ν(x)I{ν(x)>ν(o)+σ}|ν(o)]
= m1

1 −Φ

ν(o)+σ−m1
σ1

+ σ1ϕ

ν(o)+σ−m1
σ1

(B.9)
Now observe that
E[m1] =
Z 
µp(x) + Kp(x,o)
Kp(o,o)(ν(o) −µp(o))

N(ν(o); µp(o), Kp(o, o))dν(o)dν(o) = µp(x),
(B.10)
59

--- Page 60 ---

and
E
h
m1Φ

ν(o)+σ−m1
σ1
i
= E
h
µp(x) + Kp(x,o)
Kp(o,o)(ν(o) −µp(o))

Φ

ν(o)+σ−m1
σ1
i
=

µp(x) −Kp(x,o)
Kp(o,o)µp(o)

E
h
Φ

ν(o)+σ−m1
σ1
i
+ Kp(x,o)
Kp(o,o)E
h
ν(o)Φ

ν(o)+σ−m1
σ1
i
(B.11)
The expectations are with respect to ν(o). Now we use (A.2) to get
E
h
Φ

ν(o)+σ−m1
σ1
i
=
Z
Φ

ν(o)+σ−m1
σ1

N(ν(o); µp(o), Kp(o, o))dν(o)
=
Z
Φ
 
ν(o) Kp(o,o)−Kp(x,o)
Kp(o,o)
+m2
σ1
!
N(ν(o); µp(o), Kp(o, o))dν(o)
=
Z
Φ


z Kp(o,o)−Kp(x,o)
√
Kp(o,o)
+m2+ Kp(o,o)−Kp(x,o)
Kp(o,o)
µp(o)
σ1


N(z; 0, 1)dz
= Φ


µp(o)Kp(o,o)−Kp(x,o)
√
Kp(o,o)
+m2√
Kp(o,o)
√
Kp(o,o)σ2
1+(Kp(o,o)−Kp(x,o))2


= Φ

√
Kp(o,o)(µp(o)+σ−µp(x))
√
Kp(o,o)σ2
1+(Kp(o,o)−Kp(x,o))2

,
(B.12)
60

--- Page 61 ---

with m2 = Kp(o,o)(σ−µp(x))+Kp(x,o)µp(o)
Kp(o,o)
. Similarly, we have that
E
h
ν(o)Φ

ν(o)+σ−m1
σ1
i
=
Z
ν(o)Φ

ν(o)+σ−m1
σ1

N(ν(o); µp(o), Kp(o, o))dν(o)
=
Z
ν(o)Φ
 
ν(o) Kp(o,o)−Kp(x,o)
Kp(o,o)
+m2
σ1
!
N(ν(o); µp(o), Kp(o, o))dν(o)
=
Z
Φ


z Kp(o,o)−Kp(x,o)
√
Kp(o,o)
+m2+ Kp(o,o)−Kp(x,o)
Kp(o,o)
µp(o)
σ1



z
q
Kp(o, o) + µp(o)

N(z; 0, 1)dz
(B.13)
We separate the sum:
Z
Φ


z Kp(o,o)−Kp(x,o)
√
Kp(o,o)
+m2+ Kp(o,o)−Kp(x,o)
Kp(o,o)
µp(o)
σ1


µp(o)N(z; 0, 1)dz
= µp(o)Φ


µp(o)Kp(o,o)−Kp(x,o)
√
Kp(o,o)
+m2√
Kp(o,o)
√
Kp(o,o)σ2
1+(Kp(o,o)−Kp(x,o))2


= µp(o)Φ

√
Kp(o,o)(µp(o)+σ−µp(x))
√
Kp(o,o)σ2
1+(Kp(o,o)−Kp(x,o))2

.
(B.14)
61

--- Page 62 ---

The other term in the sum
Z
Φ


z Kp(o,o)−Kp(x,o)
√
Kp(o,o)
+m2+ Kp(o,o)−Kp(x,o)
Kp(o,o)
µp(o)
σ1


z
q
Kp(o, o)N(z; 0, 1)dz
=
√
Kp(o,o)(Kp(o,o)−Kp(x,o))
√
Kp(o,o)σ2
1+(Kp(o,o)−Kp(x,o))2
ϕ


µp(o)Kp(o,o)−Kp(x,o)
√
Kp(o,o)
+m2√
Kp(o,o)
√
Kp(o,o)(σ2
1+2σ2)+(Kp(o,o)−Kp(x,o))2


=
√
Kp(o,o)(Kp(o,o)−Kp(x,o))
√
Kp(o,o)σ2
1+(Kp(o,o)−Kp(x,o))2
ϕ

√
Kp(o,o)(µp(o)+σ−µp(x))
√
Kp(o,o)σ2
1+(Kp(o,o)−Kp(x,o))2

.
(B.15)
where we have used (A.3). Finally, we consider
Z
ϕ

ν(o)+σ−m1
σ1

N(ν(o); µp(o), Kp(o, o))dν(o)
=
Z
ϕ


z Kp(o,o)−Kp(x,o)
√
Kp(o,o)
+m2+ Kp(o,o)−Kp(x,o)
Kp(o,o)
µp(o)
σ1


N(z; 0, 1)dν(o)
=
√
Kp(o,o)σ1
√
Kp(o,o)pσ2
1+(Kp(o,o)−Kp(x,o))2
ϕ

√
Kp(o,o)(µp(o)+σ−µp(x))
√
Kp(o,o)σ2
1+(Kp(o,o)−Kp(x,o))2

.
(B.16)
62

--- Page 63 ---

Therefore, from (A.14) and (A.18)–(A.23), we obtain
E[ν(x)I{ν(x)>ν(o)+σ}] = µp(x)
−

µp(x) −Kp(x,o)
Kp(o,o)µp(o)

· Φ

√
Kp(o,o)(µp(o)+σ−µp(x))
√
Kp(o,o)σ2
1+(Kp(o,o)−Kp(x,o))2

−Kp(x,o)
Kp(o,o)µp(o)Φ

√
Kp(o,o)(µp(o)+σ−µp(x))
√
Kp(o,o)σ2
1+(Kp(o,o)−Kp(x,o))2

−Kp(x,o)
Kp(o,o)
√
Kp(o,o)(Kp(o,o)−Kp(x,o))
√
Kp(o,o)σ2
1+(Kp(o,o)−Kp(x,o))2
ϕ

√
Kp(o,o)(µp(o)+σ−µp(x))
√
Kp(o,o)σ2
1+(Kp(o,o)−Kp(x,o))2

+
√
Kp(o,o)σ2
1
√
Kp(o,o)σ2
1+(Kp(o,o)−Kp(x,o))2
ϕ

√
Kp(o,o)(µp(o)+σ−µp(x))
√
Kp(o,o)σ2
1+(Kp(o,o)−Kp(x,o))2

= µp(x)

1 −Φ

√
Kp(o,o)(µp(o)+σ−µp(x))
√
Kp(o,o)σ2
1+(Kp(o,o)−Kp(x,o))2

+
√
Kp(o,o)(Kp(x,x)−Kp(x,o))
√
Kp(o,o)(σ2
1+2σ2)+(Kp(o,o)−Kp(x,o))2
ϕ

√
Kp(o,o)(µp(o)+σ−µp(x))
√
Kp(o,o)σ2
1+(Kp(o,o)−Kp(x,o))2

(B.17)
Note that
Kp(o, o)σ2
1 + (Kp(o, o) −Kp(x, o))2
= Kp(o, o)

Kp(x, x) −
K2
p(x,o)
Kp(o,o)

+ (Kp(o, o) −Kp(x, o))2
= Kp(o, o)Kp(x, x) −K2
p(x, o)
+ K2
p(o, o) + K2
p(x, o) −2Kp(x, o)Kp(o, o)
= Kp(o, o)(Kp(x, x) + Kp(o, o) −2Kp(x, o)).
(B.18)
63

--- Page 64 ---

Therefore, we have that
E[ν(x)I{ν(x)>ν(o)+σ}] =
= µp(x)

1 −Φ

(µp(o)+σ−µp(x))
√
Kp(x,x)+Kp(o,o)−2Kp(x,o)

+
Kp(x,x)−Kp(x,o)
√
Kp(x,x)+Kp(o,o)−2Kp(x,o)
ϕ

µp(o)+σ−µp(x)
√
Kp(x,x)+Kp(o,o)−2Kp(x,o)

(B.19)
and
E[ν(o)I{ν(o)>ν(x)+σ}] =
= µp(o)

1 −Φ

(µp(x)+σ−µp(o))
√
Kp(x,x)+Kp(o,o)−2Kp(x,o)

+
Kp(o,o)−Kp(x,o)
√
Kp(x,x)+Kp(o,o)−2Kp(x,o)
ϕ

µp(x)+σ−µp(o)
√
Kp(x,x)+Kp(o,o)−2Kp(x,o)

(B.20)
64

--- Page 65 ---

The other two terms are:
E[ν(o)I{|ν(o)−ν(x)|≤σ}] = µp(o)
−E[ν(o)I{ν(o)>ν(x)+σ}] −E[ν(o)I{ν(x)>ν(o)+σ}]
= µp(o) −µp(o)

1 −Φ

(µp(x)+σ−µp(o))
√
Kp(x,x)+Kp(o,o)−2Kp(x,o)

−
Kp(o,o)−Kp(x,o)
√
Kp(x,x)+Kp(o,o)−2Kp(x,o)
ϕ

µp(x)+σ−µp(o)
√
Kp(x,x)+Kp(o,o)−2Kp(x,o)

−µp(o)

1 −Φ

(−µp(x)+σ+µp(o))
√
Kp(x,x)+Kp(o,o)−2Kp(x,o)

+
Kp(o,o)−Kp(x,o)
√
Kp(x,x)+Kp(o,o)−2Kp(x,o)
ϕ

−µp(x)+σ+µp(o)
√
Kp(x,x)+Kp(o,o)−2Kp(x,o)

= µp(o) −µp(o)
 
2 −Φ

(µp(x)+σ−µp(o))
√
Kp(x,x)+Kp(o,o)−2Kp(x,o)

−Φ

(−µp(x)+σ+µp(o))
√
Kp(x,x)+Kp(o,o)−2Kp(x,o)
 !
+
Kp(o,o)−Kp(x,o)
√
Kp(x,x)+Kp(o,o)−2Kp(x,o)
 
ϕ

−µp(x)+σ+µp(o)
√
Kp(x,x)+Kp(o,o)−2Kp(x,o)

−ϕ

µp(x)+σ−µp(o)
√
Kp(x,x)+Kp(o,o)−2Kp(x,o)
 !
(B.21)
65

--- Page 66 ---

and
E[ν(x)I{|ν(o)−ν(x)|≤σ}] =
= µp(x) −µp(x)
 
2 −Φ

(µp(x)+σ−µp(o))
√
Kp(x,x)+Kp(o,o)−2Kp(x,o)

−Φ

(−µp(x)+σ+µp(o))
√
Kp(x,x)+Kp(o,o)−2Kp(x,o)
 !
+
Kp(x,o)−Kp(x,o)
√
Kp(x,x)+Kp(o,o)−2Kp(x,o)
 
ϕ

−µp(o)+σ+µp(x)
√
Kp(x,x)+Kp(o,o)−2Kp(x,o)

−ϕ

µp(o)+σ−µp(x)
√
Kp(x,x)+Kp(o,o)−2Kp(x,o)
 !
(B.22)
Proof of Proposition 3. If R has no uncertainty and S is rational, then
the expected payoffs can be computed from (33), (34) and (35). The values
are E[DEF] = max(µp(x), µp(o)), E[IMM] = µp(x) and E[DoN] = µp(o).
Therefore, DEF is always optimal.
If S is bounded-rational and R has no uncertainty, then σ > 0. We
consider three cases: (1) µp(x) > µp(o) + σ; (2) µp(o) > µp(x) + σ; (3)
otherwise.
In case (1), the payoffs are: E[DEF] = µp(x), E[IMM] = µp(x) and
E[DoN] = µp(o), Therefore, DEF is optimal. A similar results holds in case
(2). In case (3), E[DEF] = {µp(x)−ϵ, µp(o)−ϵ}. Under the condition (A) or
(B), DEF will alwys be dominated. If S is rational and R has uncertainty,
then DEF is optimal as in Proposition 1 The last case follows directly from
Lemma 3.
Proof of Proposition 4. The only case where the content of the message is
important is when DEF is not optimal. In this case, R makes a decision
autonomously.
Whenever DEF is not optimal, the best action can be either IMM(x)
if µp(x) > µp(o) or DoN if µp(o) > µp(x). Therefore, if S sends a biased
message such that R estimates µp(x) > µp(o) when, in reality, ν(x) < ν(o),
then R would choose an action that is not optimal for S.
66

--- Page 67 ---

Proof of Lemma 4. For large s, the beta distribution is approximatively a
Gaussian distribution:
Beta(w; ts, (1 −t)s) ≈N

w; t, t(1 −t)
s

Therefore, we have that
p(x ≻y|ν(X))
=
Z
I{wν1(x)+(1−w)ν2(x)>wν1(y)+(1−w)ν2(y)}N

w; t, t(1 −t)
s

dw
=
Z
I{w(ν1(x)−ν1(y)−(ν2(x)−ν2(y))>−(ν2(x)−ν2(y))}N

w; t, t(1 −t)
s

dw
=
Z
I{(τz+t)(ν1(x)−ν1(y)−(ν2(x)−ν2(y))>−(ν2(x)−ν2(y))}N (z; 0, 1) dz
=
Z
I{τz(ν1(x)−ν1(y)−(ν2(x)−ν2(y))>−(ν2(x)−ν2(y))−t(ν1(x)−ν1(y)−(ν2(x)−ν2(y))}N (z; 0, 1) dz
=
Z
I{τz(ν1(x)−ν1(y)−(ν2(x)−ν2(y))>−(tν1(x)+(1−t)ν2(x))+(tν1(y)+(1−t)ν2(y))}N (z; 0, 1) dz
= Φ

(tν1(x)+(1−t)ν2(x))−(tν1(y)+(1−t)ν2(y))
τ(ν1(x)−ν1(y)−(ν2(x)−ν2(y))

I{(ν1(x)−ν1(y)−(ν2(x)−ν2(y))>0}
+ Φ

−(tν1(x)+(1−t)ν2(x))−(tν1(y)+(1−t)ν2(y))
τ(ν1(x)−ν1(y)−(ν2(x)−ν2(y))

I{(ν1(x)−ν1(y)−(ν2(x)−ν2(y))<0}
= Φ

(tν1(x)+(1−t)ν2(x))−(tν1(y)+(1−t)ν2(y))
τ|ν1(x)−ν1(y)−(ν2(x)−ν2(y))|

(B.23)
where τ 2 = t(1−t)
s
.
Proof of Proposition 5. If S is rational and R has no uncertainty, then the
payoff for IMM is if ν(x), for DoN ν(o), and for DEF is ν(x) if it dominates
ν(o) (that is, if ν(x) ≻ν(o)) or ν(o) otherwise.
Therefore, DEF is not
dominated.
If S is bounded-rational and R has no uncertainty, then the payoffs
for IMM and DoN are the same as before. The payoff for DEF is pν(o) +
(1 −p)ν(x). So DEF is always dominated by either IMM or DoN.
If S is rational and R has uncertainty, then DEF is never dominated.
This results can be proven by Jensen’s inequality (element-wise) as in Propo-
sition 1.
If S is bounded-rational and R has
uncertainty, the best decision
depends on the specific case.
67

--- Page 68 ---

Proof of Proposition 6. Assume, by contradiction, that ν1(a) does not depend
on a∗. Since A is binary, ν1(a) (in ν([a, x]) = ν1(a) + ν2(x)) can only assume
two values: ν1(1) = γ1 and ν1(0) = γ0.
When a∗= 1, to satisfy D1, min(ν([1, o]), ν([1, y])) > max(ν([0, x])). This
implies that
γ1 + min(ν2(o), ν2(y)) > γ0 + ν2(x).
This is true, for every o, x, y ∈X, if
γ1 > γ0 + max
o,x,y∈X (ν2(x) −min(ν2(o), ν2(y))) = γ0 + d
with d = maxo,x,y∈X (ν2(x) −min(ν2(o), ν2(y))) ≥0.
When a∗= 0, to satisfy D2, min(ν([0, o]), ν([0, x])) > max(ν([1, y])). This
implies that
γ0 + min(ν2(o), ν2(x)) > γ1 + ν2(x).
Therefore, we have that
γ0 > γ1 + max
o,x,y∈X (ν2(y) −min(ν2(o), ν2(y))) = γ1 + d.
Therefore, D1 and D2 cannot be both true, as γ1 > γ0 + d > (γ1 + d) + d
leads to a contradiction.
To prove the other direction, we can choose
ν([a, x]|a∗) = I{a∗=0}ν0(a) + I{a∗=1}ν1(a) + ν2(x).
Indeed, when a∗= 1, we have that
γ1 > max
o,x,y∈X (ν2(x) −min(ν2(o), ν2(y))) = d,
where γ1 = ν1(1) and ν1(0) = 0 (we have put it to zero withour loss of
generality). When a∗= 0, we have that
γ0 > max
o,x,y∈X (ν2(x) −min(ν2(o), ν2(y))) = d,
where γ0 = ν0(1) and ν0(0) = 0.
68

--- Page 69 ---

References
[1] J. Gall, Systemantics: The Underground Text of Systems Lore; how
Systems Really Work and how They Fail, General Systemantics Press,
1990.
[2] S. Russell, Human compatible: AI and the problem of control, Penguin
Uk, 2019.
[3] T. Zhi-Xuan, M. Carroll, M. Franklin, H. Ashton, Beyond preferences
in ai alignment: T. zhi-xuan et al., Philosophical Studies 182 (2025)
1813–1863.
[4] A. Fern, S. Natarajan, K. Judah, P. Tadepalli, A decision-theoretic
model of assistance, Journal of Artificial Intelligence Research 50 (2014)
71–104.
[5] D. Hadfield-Menell, S. J. Russell, P. Abbeel, A. Dragan, Cooperative
inverse reinforcement learning, Advances in neural information pro-
cessing systems 29 (2016).
[6] D. Hadfield-Menell, A. Dragan, P. Abbeel, S. Russell, The off-switch
game, in: Workshops at the Thirty-First AAAI Conference on Artificial
Intelligence, 2017.
[7] L. Orseau, M. Armstrong, Safely interruptible agents, in: Conference
on Uncertainty in Artificial Intelligence, Association for Uncertainty in
Artificial Intelligence, 2016.
[8] J. Schlatter, B. Weinstein-Raun, J. Ladish,
Shutdown resistance in
large language models, arXiv preprint arXiv:2509.14260 (2025).
[9] E. Wallace, K. Xiao, R. Leike, L. Weng, J. Heidecke, A. Beutel, The in-
struction hierarchy: Training llms to prioritize privileged instructions,
arXiv preprint arXiv:2404.13208 (2024).
[10] N. Soares, B. Fallenstein, S. Armstrong, E. Yudkowsky, Corrigibility.,
in: AAAI Workshop: AI and Ethics, 2015.
[11] E. Thornley,
The shutdown problem: an ai engineering puzzle for
decision theorists, Philosophical Studies 182 (2025) 1653–1680.
69

--- Page 70 ---

[12] S. Goldstein, P. Robinson, Shutdown-seeking ai, Philosophical Studies
182 (2025) 1567–1579.
[13] T. Wängberg, M. Böörs, E. Catt, T. Everitt, M. Hutter,
A game-
theoretic analysis of the off-switch game, in: Artificial General Intel-
ligence: 10th International Conference, AGI 2017, Melbourne, VIC,
Australia, August 15-18, 2017, Proceedings 10, Springer, 2017, pp.
167–177.
[14] A. Benavoli, A. Facchini, M. Zaffalon, The ai off-switch problem as a
signalling game: bounded rationality and incomparability, in: Inter-
national Symposium on Imprecise Probabilities: Theories and Appli-
cations, PMLR, 2025, pp. 1–11.
[15] M. Spence, Market signaling, Harvard Univ. Press, Cambridge, MA
(1974).
[16] R. Gibbons, Game theory for applied economists, Princeton University
Press, 1992.
[17] C. Wirth, R. Akrour, G. Neumann, J. Fürnkranz, et al., A survey of
preference-based reinforcement learning methods, Journal of Machine
Learning Research 18 (2017) 1–46.
[18] P. F. Christiano, J. Leike, T. B. Brown, M. Martic, S. Legg, D. Amodei,
Deep reinforcement learning from human preferences, in: Proceedings
of the 31st International Conference on Neural Information Processing
Systems, NIPS’17, Curran Associates Inc., Red Hook, NY, USA, 2017,
pp. 4302–4310.
[19] N. Stiennon, L. Ouyang, J. Wu, D. Ziegler, R. Lowe, C. Voss, A. Rad-
ford, D. Amodei, P. F. Christiano, Learning to summarize with hu-
man feedback, Advances in Neural Information Processing Systems 33
(2020) 3008–3021.
[20] L. Ouyang, J. Wu, X. Jiang, D. Almeida, C. Wainwright, P. Mishkin,
C. Zhang, S. Agarwal, K. Slama, A. Ray, et al., Training language
models to follow instructions with human feedback, Advances in Neural
Information Processing Systems 35 (2022) 27730–27744.
70

--- Page 71 ---

[21] R. Rafailov, A. Sharma, E. Mitchell, C. D. Manning, S. Ermon,
C. Finn,
Direct preference optimization:
Your language model is
secretly a reward model,
in: A. Oh, T. Neumann, A. Globerson,
K. Saenko, M. Hardt, S. Levine (Eds.), Advances in Neural Informa-
tion Processing Systems, volume 36, Curran Associates, Inc., 2023, p.
53728–53741.
[22] T. Seidenfeld, M. J. Schervish, J. B. Kadane, Decisions without order-
ing, in: Acting and reflecting, Springer, 1990, pp. 143–170.
[23] J. S. Chipman, The foundations of utility, Econometrica: Journal of
the Econometric Society (1960) 193–224.
[24] P. C. Fishburn, Exceptional paper—lexicographic orders, utilities and
decision rules: A survey, Management science 20 (1974) 1442–1471.
[25] A. Tversky, S. Sattath, P. Slovic, Contingent weighting in judgment
and choice., Psychological review 95 (1988) 371.
[26] J. E. Martínez-Legaz, Lexicographic utility and orderings, in: Hand-
book of Utility Theory, 1999, pp. 345–369.
[27] N. Houy, K. Tadenuma, Lexicographic compositions of multiple criteria
for decision making, Journal of Economic Theory 144 (2009) 1770–
1782.
[28] M. Mandler, The lexicographic method in preference theory, Economic
Theory 71 (2021) 553–577.
[29] C. Lee-Stronach,
Moral priorities under risk,
Canadian Journal of
Philosophy 48 (2018) 793–811.
[30] M. Smith,
How to model lexical priority,
Ergo: An Open Access
Journal of Philosophy 12 (2025) 1039–1071. doi:10.3998/ergo.7963.
[31] L. J. Savage, The foundations of statistics, Courier Corporation, 1972.
[32] A. Casanova, A. Benavoli, M. Zaffalon,
Nonlinear desirability as a
linear classification problem,
International Journal of Approximate
Reasoning 152 (2023) 1–32.
71

--- Page 72 ---

[33] E. Q. B. V. Enrique Miranda, Ignacio Montes (Ed.), Closure opera-
tors, classifiers and desirability, 2023. URL: https://proceedings.
mlr.press/v215/benavoli23a/benavoli23a.pdf.
[34] E. Miranda, M. Zaffalon, Nonlinear desirability theory, International
Journal of Approximate Reasoning 154 (2023) 176–199.
[35] P. Walley, Statistical Reasoning with Imprecise Probabilities, Chapman
& Hall/CRC Monographs on Statistics & Applied Probability, Taylor
& Francis, 1991.
[36] F. J. Anscombe, R. J. Aumann, et al., A definition of subjective prob-
ability, Annals of Mathematical Statistics 34 (1963) 199–205.
[37] M. Zaffalon, E. Miranda, Axiomatising incomplete preferences through
sets of desirable gambles, Journal of Artificial Intelligence Research 60
(2017) 1057–1126.
[38] M. Zaffalon, E. Miranda, Desirability foundations of robust rational
decision making, Synthese 198 (2021) 6529–6570.
[39] K. J. Arrow, Rational choice functions and orderings, Economica 26
(1959) 121–127.
[40] A. Sen, The formulation of rational choice, The American Economic
Review 84 (1994) 385–390.
[41] M. Aizerman, A. Malishevski, General theory of best variants choice:
Some aspects,
IEEE Transactions on Automatic Control 26 (1981)
1030–1040.
[42] C. R. Plott, Path independence, rationality, and social choice, Econo-
metrica: Journal of the Econometric Society (1973) 1075–1091.
[43] T. Seidenfeld, M. J. Schervish, J. B. Kadane, Coherent choice functions
under uncertainty, Synthese 172 (2010) 157–176.
[44] J. De Bock, G. De Cooman,
Interpreting, axiomatising and repre-
senting coherent choice functions in terms of desirability, in: Interna-
tional Symposium on Imprecise Probabilities: Theories and Applica-
tions, PMLR, 2019, pp. 125–134.
72

--- Page 73 ---

[45] A. Van Camp, G. De Cooman, E. Miranda, E. Quaeghebeur, Coherent
choice functions, desirability and indifference, Fuzzy sets and systems
341 (2018) 1–36.
[46] J. De Bock, Archimedean choice functions: an axiomatic foundation
for imprecise decision making, in: Information Processing and Manage-
ment of Uncertainty in Knowledge-Based Systems: 18th International
Conference, IPMU 2020, Lisbon, Portugal, June 15–19, 2020, Proceed-
ings, Part II 18, Springer, 2020, pp. 195–209.
[47] M. J. Schervish, T. Seidenfeld, J. B. Kadane, State-dependent utilities,
Journal of the American Statistical Association 85 (1990) 840–847.
[48] A. Benavoli, D. Azzimonti, D. Piga, Learning choice functions with
gaussian processes, in: Uncertainty in Artificial Intelligence, PMLR,
2023, pp. 141–151.
[49] A. Benavoli, D. Azzimonti, A tutorial on learning from preferences
and choices with gaussian processes, arXiv preprint arXiv:2403.11782
(2024).
[50] A. Benavoli, D. Azzimonti, D. Piga, Skew gaussian processes for clas-
sification, Machine Learning 109 (2020) 1877–1902.
[51] A. Benavoli, D. Azzimonti, D. Piga, Preferential Bayesian optimisation
with Skew Gaussian Processes,
in: Proceedings of the Genetic and
Evolutionary Computation Conference Companion, 2021, pp. 1842–
1850.
[52] A. Benavoli, D. Azzimonti, D. Piga, A unified framework for closed-
form nonparametric regression, classification, preference and mixed
problems with Skew Gaussian Processes,
Machine Learning (2021)
1–39.
[53] D. J. MacKay, Bayesian methods for backpropagation networks, in:
Models of neural networks III, Springer, 1996, pp. 211–254.
[54] C. K. Williams, D. Barber, Bayesian classification with gaussian pro-
cesses, IEEE Transactions on Pattern Analysis and Machine Intelli-
gence 20 (1998) 1342–1351.
73

--- Page 74 ---

[55] T. P. Minka, A family of algorithms for approximate Bayesian inference,
Ph.D. thesis, Massachusetts Institute of Technology, 2001.
[56] M. Opper, C. Archambeau, The variational gaussian approximation
revisited, Neural computation 21 (2009) 786–792.
[57] M. N. Gibbs, D. J. MacKay, Variational Gaussian process classifiers,
IEEE Transactions on Neural Networks 11 (2000) 1458–1464.
[58] H. A. Simon, Bounded rationality, Utility and probability (1990) 15–
18.
[59] S. J. Gershman, E. J. Horvitz, J. B. Tenenbaum, Computational ra-
tionality: A converging paradigm for intelligence in brains, minds, and
machines, Science 349 (2015) 273–278.
[60] A. Benavoli, A. Facchini, D. Piga, M. Zaffalon,
Sum-of-squares for
bounded rationality, International Journal of Approximate Reasoning
105 (2019) 130–152.
[61] R. D. Luce, Semiorders and a theory of utility discrimination, Econo-
metrica, Journal of the Econometric Society (1956) 178–191.
[62] K. E. Train, Discrete choice methods with simulation, Cambridge uni-
versity press, 2009.
[63] L. Thurstone, A law of comparative judgment., Psychological review
34 (1927) 273.
[64] B. Shahriari, K. Swersky, Z. Wang, R. P. Adams, N. De Freitas, Tak-
ing the human out of the loop: A review of bayesian optimization,
Proceedings of the IEEE 104 (2015) 148–175.
[65] J. González, Z. Dai, A. Damianou, N. D. Lawrence,
Preferential
Bayesian optimization, in: D. Precup, Y. W. Teh (Eds.), Proceedings
of the 34th International Conference on Machine Learning, volume 70
of Proceedings of Machine Learning Research, PMLR, 2017, pp. 1282–
1291.
[66] A. Benavoli, D. Azzimonti, D. Piga, Bayesian optimization for choice
data, in: Proceedings of the Companion Conference on Genetic and
74

--- Page 75 ---

Evolutionary Computation, GECCO ’23 Companion, Association for
Computing Machinery, New York, NY, USA, 2023, pp. 2272–2279.
[67] S. Takeno, M. Nomura, M. Karasuyama, Towards practical preferential
bayesian optimization with skew gaussian processes, in: Proceedings
of the 40th International Conference on Machine Learning, ICML’23,
JMLR, 2023.
[68] Z. J. Lin, R. Astudillo, P. Frazier, E. Bakshy, Preference exploration
for efficient bayesian optimization with multiple outcomes, in: Interna-
tional Conference on Artificial Intelligence and Statistics, PMLR, 2022,
pp. 4235–4258.
[69] M. Adachi, B. Planden, D. Howey, M. A. Osborne, S. Orbell, N. Ares,
K. Muandet, S. Lun Chau, Looping in the human: Collaborative and
explainable Bayesian optimization, in: S. Dasgupta, S. Mandt, Y. Li
(Eds.), Proceedings of The 27th International Conference on Artifi-
cial Intelligence and Statistics, volume 238 of Proceedings of Machine
Learning Research, PMLR, 2024, pp. 505–513.
[70] R. Astudillo, Z. J. Lin, E. Bakshy, P. Frazier,
qeubo: A decision-
theoretic acquisition function for preferential bayesian optimization,
in: International Conference on Artificial Intelligence and Statistics,
PMLR, 2023, pp. 1093–1114.
[71] M. Zaffalon, G. Corani, D. Mauá,
Evaluating credal classifiers by
utility-discounted predictive accuracy,
International Journal of Ap-
proximate Reasoning 53 (2012) 1282–1301.
[72] Ö. Evren, Scalarization methods and expected multi-utility represen-
tations, Journal of Economic Theory 151 (2014) 30–63.
[73] M. Mandler,
Incomplete preferences and rational intransitivity of
choice, Games and Economic Behavior 50 (2005) 255–277.
[74] E.
Karni,
Incomplete
preferences
and
random
choice
be-
havior:
Axiomatic
characterizations,
Working
Paper
(2021).
URL:
http://www.econ2.jhu.edu/people/karni/
IncompletePreferencesRandomChoiceBehaviour.pdf,
johns Hop-
kins University, September 27, 2021.
75

--- Page 76 ---

[75] J. Apesteguia, M. A. Ballester, A theory of reference-dependent be-
havior, Economic Theory 40 (2009) 427–455.
[76] Y. Masatlioglu, E. A. Ok, Rational choice with status quo bias, Journal
of economic theory 121 (2005) 1–29.
[77] P. Manzini, M. Mariotti, Sequentially rationalizable choice, American
Economic Review 97 (2007) 1824–1839.
[78] E. Karni, Stochastic choice functions and irresolute choice behavior,
Unpublished manuscript (2022). URL: http://www.econ2.jhu.edu/
people/karni/stochasticchoicefunctions-10-3-2022.pdf, johns
Hopkins University, October 10, 2022.
[79] E. Karni, Incomplete risk attitudes and random choice behavior: an
elicitation mechanism, Theory and Decision 92 (2022) 677–687.
[80] E. Karni, Irresolute choice behavior, International Journal of Economic
Theory 20 (2024) 70–87.
[81] A. Ecoffet, J. Lehman,
Reinforcement learning under moral uncer-
tainty, in: International conference on machine learning, PMLR, 2021,
pp. 2926–2936.
[82] S. Casper, X. Davies, C. Shi, T. K. Gilbert, J. Scheurer, J. Rando,
R. Freedman, T. Korbak, D. Lindner, P. Freire, et al., Open prob-
lems and fundamental limitations of reinforcement learning from hu-
man feedback, arXiv preprint arXiv:2307.15217 (2023).
[83] V. Conitzer, R. Freedman, J. Heitzig, W. H. Holliday, B. M. Jacobs,
N. Lambert, M. Mossé, E. Pacuit, S. Russell, H. Schoelkopf, et al.,
Social choice for ai alignment: Dealing with diverse human feedback,
CoRR (2024).
[84] Y. Metz, A. Geiszl, R. Baur, M. El-Assady,
Reward learning from
multiple feedback types, in: The Thirteenth International Conference
on Learning Representations, 2025.
[85] L. S. Shapley, F. D. Rigby, Equilibrium points in games with vector
payoffs, Naval Research Logistics Quarterly 6 (1959) 57–61.
76

--- Page 77 ---

[86] T. Seidenfeld, M. J. Schervish, J. B. Kadane, et al., A representation
of partially ordered preferences,
The Annals of Statistics 23 (1995)
2168–2217.
[87] R. Nau, The shape of incomplete preferences, Annals of Statistics 34
(2006) 2430–2448.
[88] P. Fishburn, Utility Theory for Decision Making, Wiley, New York,
1970.
[89] P. C. Fishburn, A study of lexicographic expected utility, Management
Science 17 (1971) 672–678.
[90] Y. Liu, Y. Yao, J.-F. Ton, X. Zhang, R. Guo, H. Cheng, Y. Klochkov,
M. F. Taufiq, H. Li,
Trustworthy llms:
a survey and guideline
for evaluating large language models’ alignment,
arXiv preprint
arXiv:2308.05374 (2023).
[91] R. R. Murphy, D. D. Woods, Beyond asimov: The three laws of re-
sponsible robotics, in: Machine ethics and robot ethics, Routledge,
2020, pp. 405–411.
[92] A. Van Camp, E. Miranda, G. De Cooman, Lexicographic choice func-
tions without archimedeanicity,
in: Soft methods for data science,
Springer, 2016, pp. 479–486.
[93] A. Van Camp, G. de Cooman, E. Miranda, Lexicographic choice func-
tions, International Journal of Approximate Reasoning 92 (2018) 97–
119.
[94] A. Benavoli, A. Facchini, M. Zaffalon, J. Vicente-Pérez, A polarity
theory for sets of desirable gambles,
in: Proceedings of the Tenth
International Symposium on Imprecise Probability: Theories and Ap-
plications, PMLR, 2017, pp. 37–48.
[95] A. Bales, Will ai avoid exploitation? artificial general intelligence and
expected utility theory, Philosophical Studies 182 (2025) 1519–1538.
[96] S. Neth, Off-switching not guaranteed, Philosophical Studies (2025)
1–13.
77

--- Page 78 ---

[97] T. Denœux, D. Dubois, H. Prade, Representations of uncertainty in
artificial intelligence: Probability and possibility, in: A guided tour
of artificial intelligence research: Volume I: Knowledge representation,
reasoning and learning, Springer, 2020, pp. 69–117.
[98] M. Caprio, M. Sultana, E. G. Elia, F. Cuzzolin, Credal learning theory,
Advances in Neural Information Processing Systems 37 (2024) 38665–
38694.
[99] T. L. Griffiths, N. Chater, J. B. Tenenbaum, Bayesian models of cog-
nition: Reverse engineering the mind, MIT Press, 2024.
[100] A. Garber, R. Subramani, L. Luu, M. Bedaywi, S. Russell, S. Emmons,
The partially observable off-switch game, in: Proceedings of the AAAI
Conference on Artificial Intelligence, volume 39, 2025, pp. 27304–27311.
[101] S. Ieong, Y. Shoham, Bayesian coalitional games., in: AAAI, 2008,
pp. 95–100.
[102] D. B. Owen, A table of normal integrals: A table, Communications in
Statistics-Simulation and Computation 9 (1980) 389–419.
[103] G. Grimmett, S. Stirzaker, Probability Theory and Random Processes,
3rd ed., Cambridge University Press, 2001.
78

```
