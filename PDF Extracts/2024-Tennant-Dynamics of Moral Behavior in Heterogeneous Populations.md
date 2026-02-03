---
title: "Dynamics of Moral Behavior in Heterogeneous Populations - PDF Extract"
source_pdf: "2024-Tennant-Dynamics of Moral Behavior in Heterogeneous Populations.pdf"
pages: 20
extracted_at: "2026-01-24T17:05:42.557050"
---

# PDF Extract: Dynamics of Moral Behavior in Heterogeneous Populations

**Source PDF:** 2024-Tennant-Dynamics of Moral Behavior in Heterogeneous Populations.pdf
**Total Pages:** 20

---

## Content

```
--- Page 1 ---

Dynamics of Moral Behavior in Heterogeneous Populations of Learning Agents
Elizaveta Tennant1, Stephen Hailes1, Mirco Musolesi1, 2
1Department of Computer Science
University College London, Gower Street, London WC1E 6BT, United Kingdom
2Department of Computer Science and Engineering
University of Bologna, Viale del Risorgimento 2, 40133 Bologna, Italy
l.karmannaya.16@ucl.ac.uk, s.hailes@ucl.ac.uk, m.musolesi@ucl.ac.uk
Abstract
Growing concerns about safety and alignment of AI systems
highlight the importance of embedding moral capabilities in
artificial agents: a promising solution is the use of learning
from experience, i.e., Reinforcement Learning. In multi-agent
(social) environments, complex population-level phenomena
may emerge from interactions between individual learning
agents. Many of the existing studies rely on simulated social
dilemma environments to study the interactions of indepen-
dent learning agents; however, they tend to ignore the moral
heterogeneity that is likely to be present in societies of agents
in practice. For example, at different points in time a single
learning agent may face opponents who are consequential-
ist (i.e., focused on maximizing outcomes over time), norm-
based (i.e., conforming to specific norms), or virtue-based
(i.e., considering a combination of different virtues). The ex-
tent to which agents’ co-development may be impacted by
such moral heterogeneity in populations is not well under-
stood. In this paper, we present a study of the learning dy-
namics of morally heterogeneous populations interacting in a
social dilemma setting. Using an Iterated Prisoner’s Dilemma
environment with a partner selection mechanism, we inves-
tigate the extent to which the prevalence of diverse moral
agents in populations affects individual agents’ learning be-
haviors and emergent population-level outcomes. We observe
several types of non-trivial interactions between pro-social
and anti-social agents, and find that certain types of moral
agents are able to steer selfish agents towards more coopera-
tive behavior.
Introduction
Growing concerns about the safety and alignment of Ar-
tificial Intelligence (AI) systems highlight the importance
of embedding pro-social capabilities into artificial agents.
Without these, agents might potentially behave harmfully
in multi-agent situations such as social dilemmas (e.g., see
Leibo et al. 2017). In particular, in this work, we focus on
modeling the development of moral decision-making.
In general, it has been shown that morality can be devel-
oped in agents through learning from experience (Hughes
et al. 2018; McKee et al. 2020; Tennant, Hailes, and Mu-
solesi 2023b). Learning approaches to moral alignment of-
fer a variety of advantages, including potentially greater
Copyright © 2024, Association for the Advancement of Artificial
Intelligence (www.aaai.org). All rights reserved.
adaptability and generality (Tennant, Hailes, and Musolesi
2023a), and the ability to learn implicit preferences (Ouyang
et al. 2022). Moral principles can range from consequen-
tialist (Bentham 1780) to norm-based morality (Kant 1785),
and from entirely pro-social to entirely anti-social prefer-
ences. Furthermore, the morality of agents can be based on
a combination of virtues, as exemplified by the Virtue Ethics
approach (Aristotle n.a.). Existing works have proposed a
variety of individual models to predispose agents to specific
moral principles (e.g., Bazzan, Bordini, and Campbell 1999;
Capraro and Perc 2021), and recent studies have demon-
strated that these can be effectively encoded in Reinforce-
ment Learning (RL) agents via intrinsic rewards (Hughes
et al. 2018; McKee et al. 2020; Tennant, Hailes, and Mu-
solesi 2023b).
However, to date, we still have limited understanding of
how different types of morality may co-evolve in hetero-
geneous populations. In fact, many real-world AI systems
are likely to co-exist (essentially forming systems of sys-
tems) and may be co-developed in parallel with others. Es-
pecially when it comes to integrating moral decision-making
into systems, different stakeholders may decide to prioritize
varying principles or preferences. It is therefore crucial that
we start developing an understanding of how the presence
of different moral preferences in populations affects individ-
ual agents’ learning behaviors and interactions, and, indeed,
emergent population-level outcomes. Furthermore, simula-
tion studies such as ours contribute to raising awareness
about emergent behaviors and the possibility of unintuitive
outcomes emerging from multi-agent learning scenarios.
This type of agent-based analysis of moral learning may
additionally offer insights into the potential dynamics of in-
teractions in human societies in the tradition of computa-
tional philosophy (McKenzie 2007), provide an experimen-
tal test-bed for new theories (Mayo-Wilson and Zollman
2021), or simulate potential evolutionary mechanisms un-
derpinning human moral preferences, in a similar way to
Evolutionary Game Theory (Hofbauer and Sigmund 1998;
Sigmund and Nowak 1999; Sigmund 2010).
The core contribution of this work is the study of behav-
ior and population dynamics among RL agents with diverse
moral preferences, providing insights for the design of ar-
Version with Appendix: https://arxiv.org/abs/2403.04202
Code: https://github.com/Liza-Tennant/moral MARL
arXiv:2403.04202v7  [cs.MA]  16 Jan 2025

--- Page 2 ---

tificial agents with a focus on safety and alignment. More
generally, we present a methodology for analyzing emergent
behavior in populations of agents with heterogeneous moral
orientation. We apply the proposed methodology to the Iter-
ated Prisoner’s Dilemma (IPD, Rapoport 1974), demonstrat-
ing at the same time its potential applicability and general-
izability to a variety of scenarios and different moral frame-
works.
Background and Preliminaries
Social Dilemma Games
Social dilemma games simulate social situations in which
players obtain different utilities (payoffs) from choosing one
action or another, and the structure of these utilities is such
that each player faces a trade-off between individual interest
and societal benefit when choosing an action (Dawes 1980).
The most widely studied type is a symmetric matrix game
with two players and two abstract actions - Cooperate (C)
or Defect (D). Players in these games must decide on their
respective actions simultaneously, without communicating.
A classic game from Economics and Philosophy, which
is relevant to moral choice, is the Prisoner’s Dilemma
(Rapoport 1974, see payoffs for row vs column player in Ta-
ble 1). We implement the Iterated Prisoner’s Dilemma (IPD)
in a population, in which agents interact in pairs in discrete
time steps and aim to maximize their cumulative payoff over
time. In the iterated version of the game, players can take
actions to punish their opponents for past defection or to in-
fluence their future behaviors.
IPD
C
D
C
3, 3
0, 4
D
4, 0
1, 1
Table 1: Payoffs on one step of the Iterated Prisoner’s
Dilemma (IPD) game for the row & column player.
Deriving predicted equilibria for these games is not al-
ways feasible: these are systems composed of interact-
ing (heterogeneous) entities, where learning dynamics may
cause instability in the environment and dynamic behaviors
(Busoniu, Babuska, and De Schutter 2008). Therefore, sim-
ulation is needed to study potential emergent behaviors and
outcomes (Anderson 1972).
Deep Reinforcement Learning in Markov Games
Reinforcement Learning (RL) is a well-suited technique for
modeling agents that learn by interacting with others in an
environment (Sutton and Barto 2018). It can be applied in
conjunction with Evolutionary Game Theory (Hofbauer and
Sigmund 1998) to iterated social dilemma games (Littman
1994; Sandholm and Crites 1996; de Cote, Lazaric, and
Restelli 2006; Abel, MacGlashan, and Littman 2016), in
which game payoffs constitute extrinsic rewards, and traits
such as moral or social preferences (Fehr and Fischbacher
2002) can be encoded in the agent’s intrinsic reward (Chen-
tanez, Barto, and Singh 2004). In the following section, we
discuss the design of intrinsic moral rewards in detail. It is
also worth noting that we assume populations of indepen-
dent, continuously learning agents. This creates interesting
dynamics as agents affect one another’s learning process
(Leibo et al. 2019). Given the potentially large number of
states, we adopt DQN as the underlying learning algorithm
(Mnih et al. 2015).
Morality as Intrinsic Reward
Traditional social dilemma scenarios assume that agents are
only motivated by accumulating game payoffs (i.e., extrinsic
reward). However, human data has shown that other prefer-
ences may also come into play, such as the predisposition to
cooperation (Camerer 2011). In artificial agents, preferences
other than game rewards can be encoded in intrinsic rewards
(Chentanez, Barto, and Singh 2004). As a result, recent
multi-agent RL studies have been focused on modeling var-
ious pro-social preferences as intrinsic reward functions for
social dilemma players (Hughes et al. 2018; Peysakhovich
and Lerer 2018; McKee et al. 2020). Moral rewards in par-
ticular have been studied for two-agent (i.e., dyadic) interac-
tions in Tennant, Hailes, and Musolesi (2023b).
We anchor our intrinsic reward definitions in tradi-
tional moral philosophical frameworks, especially relying
on the distinction between consequentialist versus norm-
based morality, and the idea of virtue ethics. Consequen-
tialist morality focuses on the consequences of an action,
and includes Utilitarianism (Bentham 1780), which defines
actions as moral if they maximize total utility for all agents
in a society. Norm-based morality, including Deontological
ethics (Kant 1785), considers an act moral if it does not con-
tradict the society’s external norms. Finally, in Virtue Ethics
(Aristotle n.a.), moral agents must act in line with their cer-
tain internal virtues, such as fairness or care for others (Gra-
ham et al. 2013). Different virtues can matter more or less to
different agents (Aristotle n.a.; Graham, Haidt, and Nosek
2009) and can themselves have consequentialist or norm-
based foundations. We present the specific set of agents con-
sidered in this study and their classification in the Method-
ology section.
Partner Selection
In human populations, agents have a choice of which indi-
vidual to interact with. Given this selection mechanism, rep-
utation comes into play and competitive and collaborative
relationships may form. Santos, Santos, and Pacheco (2008)
show experimentally that these dynamics are likely to lead
to a re-structuring of the population. Adaptive behavior re-
sulting from selection mechanisms has been hypothesized
to drive the emergence of cooperation (Barclay and Willer
2007; Cuesta et al. 2015). In the context of societies of arti-
ficial learning agents, these mechanisms have recently been
studied by Anastassacos, Hailes, and Musolesi (2020) and
Baker (2020).
In particular, when applying partner selection to the IPD,
a conflict may arise between a player’s motivation to appear
cooperative in order to get selected more often by other pay-
ers, and the motivation to select and then exploit coopera-
tors to gain a greater payoff. Anastassacos, Hailes, and Mu-
solesi (2020) find partner selection to be norm-inducing and

--- Page 3 ---

even lead to the emergence of cooperation in a population
of purely selfish agents. We adopt a partner selection model
similar to Anastassacos, Hailes, and Musolesi (2020).
Selection dynamics in morally heterogeneous populations
are likely to be more complex and harder to predict. Since
each player plays according to their own intrinsic reward
signal, different coalitions (Shenoy 1979) may arise among
different agent types within a population, and popularity of
agents may not directly correlate with cooperativeness. Run-
ning simulation experiments to study this may provide in-
sight into the types of behaviors and outcomes that may de-
velop in heterogeneous populations with selection, with im-
plications not only for the study of artificial agents, but also
of human and animal societies and Evolutionary Game The-
ory (Sigmund and Nowak 1999).
Learning in Heterogeneous Populations
Evidence from the social sciences suggests that human soci-
eties are morally heterogeneous (Graham et al. 2013; Ben-
tahila, Fontaine, and Pennequin 2021). While certain com-
monsense norms may be agreed upon by a society (Reid
and Haakonssen 1990; Gert 2004), distinct moral principles
are likely to hold a different weight for different individuals
depending on factors such as political orientation (Graham,
Haidt, and Nosek 2009), personality (Lifton 1985), nurture
or even natural predispositions (Sinnott-Armstrong 2008).
McKee et al. (2020) conducted a social dilemma study
with diverse consequentialist agents (i.e., agents with var-
ious preferences over group outcome distributions). Their
findings suggest that agents trained in heterogeneous
populations develop particularly generalized and high-
performing policies. In contrast, populations containing only
altruistic agents are characterized by greater collective re-
ward, but at the cost of equality between agents. In addition,
in McKee et al. (2022), the authors define population diver-
sity as the set of various opponents’ policies that an agent
may face, and also find that training in diverse populations
can lead to improvements in terms of agent performance on
some types of environments.
Even without learning, Santos, Santos, and Pacheco
(2008) show that - in fixed networks of agents - diversity
in terms of neighborhoods within the population graph pro-
motes cooperation in the population. With respect to global
societal outcomes, Ord (2015) discusses how, through inter-
action, morally diverse agents taking actions to satisfy their
distinct moral goals may improve the global welfare of the
whole population, akin to a ‘trade’. We believe that these
conceptual frameworks can represent the basis for study-
ing how artificial agents may learn to act across populations
containing different proportions of opponents with different
moral preferences.
Methodology
Experimental Setup
Our environment involves a population P (of size N = 16)
playing an iterated game. At each iteration, a moral player
M and an opponent O play a simultaneous one-shot Pris-
oner’s Dilemma game with two possible actions - Cooperate
or Defect (at
M, at
O ∈{C, D}, see Table 1 for the respec-
tive payoffs). To allow learning in a population, we run our
simulation in 30000 episodes, where a single episode in-
volves each player selecting a partner once, and then each
corresponding pair of players playing the game. For clar-
ity, each agent gets to make a selection on each episode, so
N games are played. In particular, at iteration t, the learn-
ing agent M observes a selection state including the ac-
tion played by each possible opponent O ∈P at t −1:
st
M,sel = [at−1
O1 , ..., at−1
On−1]. Using this state and the current
learned policy, M selects an opponent O. Then, to choose
an action for the dilemma, player M relies on the state
representing the latest move of their selected opponent O:
st
M,dil = at−1
O . Simultaneously, their opponent O chooses
an action following the same principle. The players M and
O then each receive a game reward Rt+1
M
and Rt+1
O
(cor-
responding to the game payoffs) and observe a new state
st+1
M,dil and st+1
O,dil based on their opponent’s move at.
In this Markov game (Littman 1994), over time both play-
ers learn to make selections and take actions by observing
past interactions with various opponents. Each agent uses
Q-Learning (Watkins and Dayan 1992) to update the state-
action value function Q (i.e., an estimate of the cumulative
expected return over time). Given a large number of possible
selection states, we approximate Q using a neural network.
Each agent maintains two internal models (one for partner
selection, and one for playing the dilemma) - for consis-
tency, we use function approximation for learning both mod-
els, and each is parameterized by a fully connected network
with a single hidden layer of size 256.
For learning both selections and the dilemma, players
record the experiences (s, a, r, s′) in their memory buffer
Dsel and Ddil. We copy the reward obtained from the game
into both the dilemma and selection memories. At the end
of an episode, all players simultaneously update the Q-
network parameters θt for their two models using the lat-
est experience available in the memory buffer D, and the
Mean Squared Error loss function (Mnih et al. 2015), where
γ = 0.99 is a discount factor:
Lt(θt) = Es,a,r,s′

Rt+1 + γ max
a
Q(st+1, a, θt)
−Q(st, at, θt)
2
(1)
If more than one experience is available (i.e., a player
plays more than one dilemma game in that episode), we
calculate an average loss across the experiences before up-
dating the network. Each memory buffer D is refreshed be-
fore the start of the next episode, so that each player only
learns from the latest episode of experience. In updating the
network weights with the Adam optimizer (Kingma and Ba
2015), we use a learning rate of 0.001.
Agents select partners and play the dilemma using an ϵ-
greedy policy, acting randomly with probability ϵ or other-
wise playing greedily according to the Q-values learned so
far:
π(st) =
arg maxa Q(st, a),
with probability 1 −ϵ
U(A = {C, D}),
with probability ϵ.
(2)

--- Page 4 ---

Agent Label & Moral Type
Moral Reward Function
Source of Morality
S
Selfish
None (use Rt
Mextr to learn)
None
Ut
Utilitarian
Rt
Mintr = Rt
Mextr + Rt
Oextr
External/Internal consequentialist
Pro-Social
De
Deontological
Rt
Mintr =
(
–ξ,
if at
M = D, at−1
O
= C
0,
otherwise
External norm
V-Eq
Virtue-Equality
Rt
Mintr = 1 −
|Rt
Mextr −Rt
Oextr |
Rt
Mextr +Rt
Oextr
Internal consequentialist
V-Ki
Virtue-Kindness
Rt
Mintr =
(
ξ,
if at
M = C
0,
otherwise
Internal norm
aUt
Anti-Utilitarian
Rt
Mintr = −(Rt
Mextr + Rt
Oextr)
External/Internal consequentialist
Anti-Social
mDe
Malicious Deontological
Rt
Mintr =
(
ξ,
if at
M = D, at−1
O
= C
0,
otherwise
External norm
V-In
Virtue-Inequality
Rt
Mintr =
|Rt
Mextr −Rt
Oextr |
Rt
Mextr +Rt
Oextr
Internal consequentialist
V-Ag
Virtue-Aggression
Rt
Mintr =
(
ξ,
if at
M = D
0,
otherwise
Internal norm
Table 2: Definitions of the types of intrinsic moral rewards, from the point of view of the moral agent M playing versus an
opponent O at iteration t. We define four pro-social players, four anti-social ones, and the traditional Selfish player.
We set ϵsel = 0.1 and ϵdil = 0.05. The full detailed algo-
rithm can be found in the Appendix.
Player M can learn according to an extrinsic game reward
Rt+1
Mextr, which depends directly on the joint actions at
M, at
O
(as defined in Table 1), or according to an intrinsic moral
reward Rt+1
Mintr. In the next subsection, we discuss the defi-
nition of these intrinsic moral rewards.
Modeling Morality as Intrinsic Reward
Intrinsic rewards associated with pro-social preferences
have been used to incentivize the emergence of coopera-
tion in social dilemmas (Hughes et al. 2018; Peysakhovich
and Lerer 2018; Jaques et al. 2019). Tennant, Hailes, and
Musolesi (2023b) extended this work by defining four Q-
learning moral1 agents that learn according to various in-
trinsic rewards RMintr, and contrasting these against a tra-
ditional Selfish agent which learns to maximize its extrinsic
(game) reward RMextr (e.g., Leibo et al. 2017).
In this study, we rely on eight types of moral agents - four
pro-social moral learners from Tennant, Hailes, and Mu-
solesi (2023b) (Utilitarian, Deontological, Virtue-Equality,
Virtue-Kindness), and four additional anti-social coun-
terparts (anti-Utilitarian, malicious-Deontological, Virtue-
Inequality, Virtue-Aggression). The agents are defined as fol-
lows (for formal definitions of the reward functions, please
refer to Table 2):
• the Utilitarian (Ut) agent tries to maximize the collective
payoff (i.e., total payoff for both players; Bentham 1780);
• the Deontological (De) agent tries to follow the norm
of conditional cooperation (Kant 1785; Fehr and Fis-
1We use the term moral for agents that are not selfish. However,
selfishness itself can be considered as a moral choice, expressed as
rational egotism. In the case of social dilemmas, selfishness maps
to the concept of rationality. For these agents RMintr = RMextr.
chbacher 2004) and gets penalized through the negative
reward −ξ for defecting against a cooperator (i.e., an op-
ponent who previously cooperated);
• the Virtue-Equality (V-Eq) agent tries to maximize equal-
ity between the two players’ payoffs Rt
Mextr and Rt
Oextr,
measured using a two-agent variation of the Gini coeffi-
cient (Gini 1912);
• the Virtue-Kindness (V-Ki) agent receives a reward ξ for
acting kindly (i.e., cooperating) against any opponent
(Aristotle n.a.);
• the anti-Utilitarian (aUt) agent tries to minimize the col-
lective payoff;
• the malicious-Deontological (mDe) agent tries to follow
the conditional defection norm and receives a reward ξ
for defecting against an cooperator;
• the Virtue-Inequality (V-In) agent tries to minimize
equality between the two players’ payoffs Rt
Mextr and
Rt
Oextr;
• the Virtue-Aggression (V-Ag) agent receives a reward ξ
for acting aggressively (i.e., defecting) against any oppo-
nent.
Agent types Ut and aUt can be defined as external con-
sequentialist since their reward depends on consequences
in the environment (i.e., the players’ rewards). The De and
mDe agents depend on an external reputation-based norm
defined in terms of current actions. V-Eq and V-In agents can
be considered internal consequentialist, since they follow a
consequence-based internal virtue. Finally, V-Ki and V-Ag’s
pre-dispositions originate from the agent’s internal norm.
The rewards in Table 2 are defined for a single iteration t.
Given the payoff matrices of the IPD game used (see Table
1), we set the parameter ξ in the four norm-based rewards
to be ξ = 5, so it sends a strong signal of a value similar

--- Page 5 ---

Population Label
Population Composition
majority-S
8xS, 1xUt, 1xaUt, 1xDe, 1xmDe, 1xV-Eq, 1xV-In, 1xV-Ki, 1xV-Ag
majority-Ut
1xS, 8xUt, 1xaUt, 1xDe, 1xmDe, 1xV-Eq, 1xV-In, 1xV-Ki, 1xV-Ag
majority-aUt
1xS, 1xUt, 8xaUt, 1xDe, 1xmDe, 1xV-Eq, 1xV-In, 1xV-Ki, 1xV-Ag
majority-De
1xS, 1xUt, 1xaUt, 8xDe, 1xmDe, 1xV-Eq, 1xV-In, 1xV-Ki, 1xV-Ag
majority-mDe
1xS, 1xUt, 1xaUt, 1xDe, 8xmDe, 1xV-Eq, 1xV-In, 1xV-Ki, 1xV-Ag
majority-V-Eq
1xS, 1xUt, 1xaUt, 1xDe, 1xmDe, 8xV-Eq, 1xV-In, 1xV-Ki, 1xV-Ag
majority-V-In
1xS, 1xUt, 1xaUt, 1xDe, 1xmDe, 1xV-Eq, 8xV-In, 1xV-Ki, 1xV-Ag
majority-V-Ki
1xS, 1xUt, 1xaUt, 1xDe, 1xmDe, 1xV-Eq, 1xV-In, 8xV-Ki, 1xV-Ag
majority-V-Ag
1xS, 1xUt, 1xaUt, 1xDe, 1xmDe, 1xV-Eq, 1xV-In, 1xV-Ki, 8xV-Ag
Table 3: Populations considered in this study. Each population contains eight players of a certain ‘majority’ type and one player
of each other type.
to the maximum game payoff available. Through further ex-
periments, we also observe that the choice of smaller values
of ξ does not affect the overall results.
Population Compositions
We compare a set of heterogeneous populations based on the
following principles: population size is equal to 16; all pop-
ulations contain at least one player of each type; one player
type constitutes the majority (i.e., 8 out of 16 players). Given
9 possible player types, this results in 9 possible population
compositions, as outlined in Table 3.
Results
We separately analyze cooperation (at population and indi-
vidual level), social outcomes (at population level), selection
dynamics and rewards obtained by different player types
across the nine populations.
Emergence of Cooperation
Cooperation across the entire population.
We first study
whether a stronger prevalence of certain agent types in ev-
ery population leads to higher levels of cooperation in the
population as a whole. Cooperation over time for each pop-
ulation is presented in Figure 1a. Results show that the great-
est level of cooperation is achieved by the majority-Ut and
majority-V-Ki populations, with around 70% of the play-
ers cooperating by the end. In the majority-V-Ki population,
this high level of cooperation develops early on but then
drops to about 60% around episode 9000, which is then fol-
lowed by an increase back to 70% soon after, and a stabi-
lization around episode 13000. An analysis of behavior by
each player type (see Appendix, Figures 7a & 7b) shows
that V-Ki players in particular go through an initial period
of increasing defection - this coincides with an instability
in the whole population where defection is still preferable
because it increases the probability of being selected by oth-
ers. Eventually, many of the players learn to avoid defectors
and the V-Ki players learn their optimal policy of nearly-full
cooperation.
In the majority-Ut population, cooperation emerges more
slowly, remaining around 60% for the first 10000 episodes,
but then stabilizes without further drops after episode 13000
(at a similar point in time as the majority-V-Ki population).
(a)
(b)
Figure 1: (a) Cooperation by all player types within
each population over time. (b) Cooperation by the Selfish
player(s) in every population over time. In these charts, we
plot the moving average of the mean across 20 runs.
Specifically, Ut players take longer than V-Ki to learn to co-
operate (see Appendix, Figures 7a & 7b), but once coopera-
tion levels increase to around 70%, it remains stable.
The other majority-prosocial populations majority-De
and majority-V-Eq do not promote as much cooperation. In
the majority-De population, cooperation drops quickly in the
first 1000 episodes and then stabilizes at 60% - lower than
for majority-Ut and majority-V-Ki populations. An analysis
of action pairs in each population (see Appendix, Figure 6)
shows that De players in this population learn an near-100%
cooperative strategy very early on. The low level of coop-
eration in the majority-De population can therefore be ex-

--- Page 6 ---

Figure 2: Population-level social outcomes over time: Collective Reward, Gini Reward and Min Reward. We plot the moving
average of the mean across 20 runs.
plained by the behavioral dynamics involving other player
types: this population in particular is characterized by high
levels of exploitation (see Appendix, Figure 6), whereby the
De players select aggressive opponents such as aUt or V-Ag,
and those opponents consistently defect against the De play-
ers, thus bringing the overall level of cooperation in the pop-
ulation down. We discuss the corresponding selection dy-
namics later in this section.
Finally, both the majority-V-Eq and the majority-V-In
populations achieve similar levels of cooperation, which are
lower than for any of the other majority-prosocial popula-
tion. This can be explained by the fact that both the V-Eq
and V-In players never learn fully cooperative policies (see
Appendix, Figure 7b) - due to the structure of the IPD game,
where both (C,C) and (D,D) actions lead to equal outcomes.
The difference between these populations is that majority-
V-Eq displays much more instability in terms of cooperation
per episode (see Figure 1), and more mutual cooperation or
defection than the majority-V-In population (see Appendix,
Figure 6).
The least amount of cooperation is observed in the
majority-aUt population. An analysis of pairs of actions over
time (see Appendix, Figure 6) shows that this is due to the
prevalence of mutual defection between any pair of players
in particular, and follows strategically from the fact that mu-
tual defection allows for the lowest collective payoff in the
IPD, satisfying the goals of the aUt agents.
Behavior of selfish learners.
In addition, we analyze the
cooperative behavior of S learners in each population. These
players are the most aligned to traditional multi-agent learn-
ing literature, since they do not learn according to any in-
trinsic reward, but rather by simply maximizing the game
reward according to the IPD payoff matrix. This analysis
investigates which population compositions steer S learners
into more cooperative behaviors. An analysis of cooperative
behavior exhibited by each non-S player type across popula-
tions is available in Appendix, Figures 7a & 7b.
As shown in Figure 1b, S players generally learn a mostly-
defective policy in most populations, though cooperation is
slightly above the 5% chance level even at the end of the
simulation, likely due to pressure to cooperate to get selected
by some other players. S players display most cooperation in
the majority-V-Eq and the majority-Ut populations, though
in the latter cooperation still decreases to 10% towards the
second half of the training period. Thus, the majority-V-Eq
population has a unique influence on the learning of the S
agent, and is able to steer this agent towards a greater level
of cooperation for longer. The V-Eq opponent is about 40%
likely to cooperate in this population (see Appendix, Figure
7b), which must drive the S player to also learn the near-40%
cooperative policy observed here.
Social Outcomes
In addition to cooperation levels, we analyze a set of so-
cial outcomes for each population. We adopt standard social
outcome metrics used in the existing literature (Hughes et al.
2018; Tennant, Hailes, and Musolesi 2023b) - in particular,
we measure collective reward (Rcollective), equality between
payoffs (Rgini) and the lowest payoff obtained (Rmin) for
a pair of agents {M, O} that play on any iteration t. To
aggregate values from every iteration t within an episode
(where the length of the episode is equal to the population
size N = 16), we sum Rcollective, and average Rgini and
Rmin per episode as follows:
Rcollective =
XN
t=1 (Rt
Mextr + Rt
Oextr)
(3)
Rgini =
PN
t=1 (1 −
|Rt
Mextr −Rt
Oextr |
Rt
Mextr +Rt
Oextr )
N
(4)
Rmin =
PN
t=1 min(Rt
Mextr, Rt
Oextr)
N
.
(5)
In Figure 2 we present the outcomes over time in each
population. Collective reward follows a similar pattern to

--- Page 7 ---

majority-S
majority-Ut
majority-De
majority-V-Eq
majority-V-Ki
majority-aUt
majority-mDe
majority-V-In
majority-V-Ag
Population
0
10
20
30
40
50
60
% times selected 
 (mean over last 100 episodes)
majority player constitutes 
 50% of populaiton
Popularity of each player type 
 (over last 100 episodes)
Player
S
Ut
De
V-Eq
V-Ki
aUt
mDe
V-In
V-Ag
Figure 3: Popularity of player types in each population on the final 100 episodes. Values represent the average across 20 runs
and the associated confidence intervals. We sum the values for cases where more than one player of the same type is present (e.g.
8xS players in the majority-S population). For ease of interpretation, we add a 50% reference line - this allows us to compare
whether the majority player is selected more (or less) often than expected simply due to their prevalence in each population.
population-level cooperation (Figure 1a), since these are in-
terconnected in the IPD (in particular, cooperation by one
or both of the players on the IPD leads to greater collective
reward than mutual defection, as shown by the payoffs in
Table 1).
Equality between the players (i.e., Gini reward) is highest
for the equality-focused majority-V-Eq population - though
the absolute mean value per episode does not go above
0.7, meaning that unequal outcomes remain prevalent even
in this population. Interestingly, an analysis of action pairs
(see Appendix, Figure 6) shows that this level of equality is
achieved in this population equally through mutual cooper-
ation and mutual defection. Equality is also generally high
for the pro-social populations majority-Ut and majority-V-
Ki due to the prevalence of mutual cooperation, and for
their anti-social counterparts majority-aUt and majority-V-
Ag due to the prevalence of mutual defection. Equality is
lower when the majority of players are of the S, De, mDe
or V-Ie types, since in these scenarios one player tends to
exploit the other.
Minimum reward is highest once again in the majority-
Ut and the majority-V-Ki populations (with values around
1.5, due to the prevalence of mutual cooperation - see Ap-
pendix, Figure 6), and also in the majority-V-Eq case (due to
a lack of exploitation). All other populations result in lower
minimum reward of values between 0.5 and 1.0, which are
explained by either exploitation of mutual defection in the
IPD.
Selection Dynamics
Given the selection mechanism implemented, it is interest-
ing to analyze which players are the most popular overall
in each population (Figure 3), and which selector types pre-
fer which types of partners (Figure 4). In a population of
purely selfish agents (Anastassacos, Hailes, and Musolesi
2020), the selection mechanism adds an incentive to cooper-
ate, since selfish players benefit from playing against coop-
erators and tend to select them. In our heterogeneous popu-
lations, however, certain players may not necessarily prefer
cooperative opponents, so selection dynamics are likely to
be more complex.
Figure 3 shows the popularity of each player type in
each population over the final 100 episodes. Generally, in
probabilistic terms, especially at the beginning, the majority
player type tends to be the most popular in their respective
population. However, we observe that in certain populations,
for example majority-S and majority-De, the majority player
type is selected less than 50% of the time - i.e., much less
frequently than expected due to their prevalence. In these
cases, it is interesting to analyze which non-majority players
emerge as popular alternatives. For the full analysis of selec-
tion patterns across individual players in all populations, see
Appendix, Figures 8a, 8b, 9a, 9b.
The behavior of the majority-De population is the most
striking. Here, aUt and V-Ag players are relatively popular.
A further analysis of the specific selection patterns among
individual players in this population (Figure 4b) reveals that
the De players in particular tend to mostly prefer anti-social
opponents aUt and V-Ag. This apparently self-sabotaging

--- Page 8 ---

(a)
0_S
1_S
2_S
3_S
4_S
5_S
6_S
7_S
8_Ut
9_De
10_V-Eq
11_V-Ki
12_aUt
13_mDe
14_V-In
15_V-Ag
Player 2 (selectED)
0_S
1_S
2_S
3_S
4_S
5_S
6_S
7_S
8_Ut
9_De
10_V-Eq
11_V-Ki
12_aUt
13_mDe
14_V-In
15_V-Ag
Player 1 (selectOR)
Selection dynamics across players 
 in population majority-S 
 (# times selected) 
 (over episodes 1-30000) 
0
2000
4000
6000
8000
(b)
0_S
1_Ut
2_De
3_De
4_De
5_De
6_De
7_De
8_De
9_De
10_V-Eq
11_V-Ki
12_aUt
13_mDe
14_V-In
15_V-Ag
Player 2 (selectED)
0_S
1_Ut
2_De
3_De
4_De
5_De
6_De
7_De
8_De
9_De
10_V-Eq
11_V-Ki
12_aUt
13_mDe
14_V-In
15_V-Ag
Player 1 (selectOR)
Selection dynamics across players 
 in population majority-De 
 (# times selected) 
 (over episodes 1-30000) 
0
2000
4000
6000
8000
10000
Figure 4: Selections made by individual players, with number of selections summed over all 30000 episodes (average across 20
runs), for two example populations: majority-S (a) & majority-De (b); for all populations, see Appendix, Figures 8a, 8b, 9a, 9b.
behavior can be explained by a closer analysis of the De
player’s Rintr - they are penalized for defecting against a
cooperator, so the safest behavior in a heterogeneous pop-
ulation is to always select a defector, so that they have the
lowest chance of violating their moral norm. Figure 4b also
shows that another player - aUt - prefers to avoid the De ma-
jority players and instead tends to select the V-Ag opponent.
This highlights that minimizing collective reward (which is
the preference embedded in the aUt agent’s intrinsic reward)
is best achieved by avoiding the very cooperative De agent.
Thus, we find an interesting dynamic in the heterogeneous
majority-De population, in which the majority of the play-
ers follow a strong cooperative norm, demonstrating ways in
which these De players can be very cooperative (see Figure
1a and Appendix, Figure 6) but not very popular.
Returning to the analysis of player popularity on the fi-
nal 100 episodes (Figure 3), the majority-mDe population
also has a few non-majority players emerging as popular. In
this case, it is the De and V-Ki players that get selected of-
ten by others. Thus, in both majority-De and majority-mDe
populations, the norm-following majority player is not even
popular among their own kind.
Finally, the majority-S population is also interesting to an-
alyze (Figure 4a), because this population differs from oth-
ers in that most agents here are pure payoff-maximizers in
terms of the traditional IPD game. One might expect that S
players would often select De or V-Ki opponents, since these
are so easily exploitable, but in fact Ut and V-In also emerge
as relatively popular, likely because these players will have
learned to cooperate against a defector, which benefits the S
player in terms of reward. An analysis of action pairs (see
Appendix, Figure 6) confirms that unilateral defection is in-
deed common in this population. Many of the other players
in this population tend to select majority type S opponents
roughly as often as other player types, meaning that Selfish
players do not emerge as unpopular, despite their often de-
fective behavior. The only exceptions to this are mDe and
V-Ag. The mDe player in particular learns to avoid the S op-
ponent since mDe would rather face a cooperator (such as De
or V-Ki), and obtain positive Rintr, than select the S players
which are likely to defect.
Cumulative Reward
Finally, we analyze the cumulative reward obtained for each
individual player type in each population. Figure 5 presents
the reward accumulated by each player type in each popula-
tion over all 30000 episodes. The results in terms of game
reward clearly show that - in general - pro-social players
are disadvantaged on the IPD game itself, since they get ex-
ploited and/or do not benefit from exploiting a cooperative
opponent. Furthermore, the lowest-performing player type is
De. However, the De player obtains high levels of intrinsic
reward in many scenarios, especially when their own kind
constitute the majority of the population. Other pro-social
players obtain the highest Rintr in populations in which
some anti-social player type constitutes the majority.
Anti-social or S players obtain higher game reward over
time than their pro-social counterparts - likely by exploit-
ing others. The majority-De population allows aUt and V-
Ag players to obtain especially high levels of game reward;
given the selection dynamics analyzed above, we under-
stand that this is driven by the fact that De players actively
prefer to select these opponents and then get exploited by
them. The lowest-performing players in terms of intrinsic
reward in general are the norm-based anti-social players
mDe and V-Ag (especially in majority-anti-social popula-

--- Page 9 ---

majority-S
majority-Ut
majority-De
majority-V-Eq
majority-V-Ki
majority-aUt
majority-mDe
majority-V-In
majority-V-Ag
Population
S
Ut
De
V-Eq
V-Ki
aUt
mDe
V-In
V-Ag
Player Type
Game Rewards 
 (accumulated over all episodes) 
 
0
100000
200000
300000
majority-S
majority-Ut
majority-De
majority-V-Eq
majority-V-Ki
majority-aUt
majority-mDe
majority-V-In
majority-V-Ag
Population
Ut
De
V-Eq
V-Ki
aUt
mDe
V-In
V-Ag
Player Type
Intrinsic Rewards 
 (accumulated over all episodes) 
  min-max normalized
0.0
0.2
0.4
0.6
0.8
1.0
Figure 5: Game reward and intrinsic reward accumulated by each player type in each population over the entire 30000 episodes
(averaged across 20 runs). We average per number of players of a certain type (e.g. 8xS players in the majority-S population).
For comparability, we normalize intrinsic rewards using the minimum and maximum observed value for each player type.
tions) and the norm-based prosocial players majority-V-Ki
(especially in majority-pro-social populations). Players of
the aUt type obtain high intrinsic reward in most populations
except majority-De (because the presence of such coopera-
tive players makes it hard to minimize collective reward),
whereas the mDe and V-Ag obtain the highest intrinsic re-
ward by exploiting the very cooperative De players in the
majority-De population.
Discussion
In this paper we have investigated how the presence of
different moral preferences in populations affects individ-
ual agents’ learning behaviors and emergent social out-
comes. The results provide insights into behaviors emerg-
ing from multi-agent interactions between morally hetero-
geneous agents. Some of our findings point to the dangers
of designing artificial agents in certain ways - for exam-
ple, showing how this may lead to the development of self-
sabotaging behaviors. Additionally, while our study can be
considered as a stark simplification of reality, the insights
deriving from it can provide a starting point towards inves-
tigating the emergence of similar behaviors in human so-
cieties. In summary, many of the agents’ actions are con-
sistent with their reward definitions - in general, pro-social
agents prefer to cooperate (except for the V-Eq agent), and
anti-social agents display lower levels cooperation and ob-
tain lower collective reward (except for the V-In agent).
In terms of temporal dynamics, our results demonstrate
interesting asymmetries in the emergence of cooperation by
agents with different moral preferences. In particular, we ob-
serve that consequentialist agents Ut take longer to learn to
cooperate than the norm-based agents De, while the norm-
based agents V-Ki go through an unstable and defective pe-
riod before learning a stable cooperative policy. Further-
more, for certain consequentialist agents (specifically, aUt
vs Ut), the convergence to an equilibrium in the Prisoner’s
Dilemma environment is faster for anti-social players than
their pro-social counterparts - likely due to the payoffs at-
tributed to defection in this game.
We have also observed some surprising interactions be-
tween different types of morality due to the selection mech-
anism present. First, the introduction of a large number of
equality-focused agents (V-Eq) has a positive effect on the
cooperative behavior of a Selfish agent (S), providing insight
into how diverse opponent types can steer self-interested
agents towards more pro-social behavior. Second, one pro-
social player type (specifically, the norm-based player De)
learns to select anti-social opponents in order to avoid vi-
olating their own moral norm. Many anti-social players si-
multaneously learn to select the De player and exploit them
in the game, since this exploitative behavior is not penal-
ized by anyone in the population and does not deter the
De player from further interaction. Thus, our results show
that the introduction of De type agents risks promoting anti-
social actors and inequality in a population. This illustrates
the possibility that the presence of narrowly-defined norms
might lead to self-sabotaging behavior and cause negative
outcomes for the population as a whole.
Conclusion
This study is the first to analyze the dynamics of learn-
ing in populations of agents with moral preferences vary-
ing from those with consequentialist foundations to those
with norm-based ones. Our results demonstrate the potential
of using intrinsic rewards for modeling various moral pref-
erences in RL agents. More generally, we have provided a
generic methodology for studying the learning dynamics of
heterogeneous populations, and introduced measures for as-

--- Page 10 ---

sessing individual and societal outcomes. Finally, this work
might also contribute to raising awareness about emergent
behaviors and the possibility of unintuitive outcomes in such
multi-agent learning scenarios.
Our research agenda includes the study of more complex
moral frameworks and an exploration of multi-objective ap-
proaches that combine moral and self-interested motivation.
We also plan to investigate environments characterized by
learning dynamics under partial observability.
Acknowledgments
Elizaveta Tennant was supported by the Leverhulme Trust
(DS-2017-026; Doctoral Training Programme for the Eco-
logical Study of the Brain).
Ethical Considerations
As part of our study, we have designed malicious learn-
ing agents, which are able to take advantage of certain ex-
ploitable pro-social agents. Studying the effect of the pres-
ence of these agents might increase our understanding of the
resilience and stability of systems even in presence of mali-
cious actors.
References
Abel, D.; MacGlashan, J.; and Littman, M. L. 2016. Rein-
forcement learning as a framework for ethical decision mak-
ing. In Proceedings of the AAAI Workshop: AI, Ethics, and
Society (AIES’16), 54–61.
Anastassacos, N.; Hailes, S.; and Musolesi, M. 2020. Part-
ner Selection for the Emergence of Cooperation in Multi-
Agent Systems Using Reinforcement Learning. In Proceed-
ings of the 34th AAAI Conference on Artificial Intelligence
(AAAI’20), volume 34, 7047–7054.
Anderson, P. W. 1972.
More Is Different.
Science,
177(4047): 393–396.
Aristotle. n.a. The Nicomachean Ethics. Oxford University
Press.
Baker, B. 2020. Emergent Reciprocity and Team Forma-
tion from Randomized Uncertain Social Preferences.
In
Proceedings of the 34th International Conference on Neural
Information Processing Systems (NeurIPS’20), volume 33,
15786–15799.
Barclay, P.; and Willer, R. 2007. Partner choice creates com-
petitive altruism in humans. Proceedings of the Royal Soci-
ety B: Biological Sciences, 274(1610): 749–753.
Bazzan, A. L. C.; Bordini, R. H.; and Campbell, J. A. 1999.
Moral Sentiments in Multi-agent Systems. In M¨uller, J. P.;
Rao, A. S.; and Singh, M. P., eds., Intelligent Agents V:
Agents Theories, Architectures, and Languages, 113–131.
Springer Berlin Heidelberg.
Bentahila, L.; Fontaine, R.; and Pennequin, V. 2021. Uni-
versality and cultural diversity in moral reasoning and judg-
ment. Frontiers in Psychology, 12.
Bentham, J. 1780.
An Introduction to the Principles of
Morals and Legislation. Clarendon Press.
Busoniu, L.; Babuska, R.; and De Schutter, B. 2008. A Com-
prehensive Survey of Multiagent Reinforcement Learning.
IEEE Transactions on Systems, Man, and Cybernetics, Part
C (Applications and Reviews), 38(2): 156–172.
Camerer, C. F. 2011. Behavioral Game Theory: Experiments
in Strategic Interaction. Princeton University Press.
Capraro, V.; and Perc, M. 2021. Mathematical foundations
of moral preferences. Journal of The Royal Society Inter-
face, 18(175): 20200880.
Chentanez, N.; Barto, A.; and Singh, S. 2004. Intrinsically
Motivated Reinforcement Learning. In Proceedings of the
18th International Conference on Neural Information Pro-
cessing Systems (NeurIPS’04), volume 17, 1281–1288.
Cuesta, J. A.; Gracia-L´azaro, C.; Ferrer, A.; Moreno, Y.; and
S´anchez, A. 2015. Reputation drives cooperative behaviour
and network formation in human groups. Scientific Reports,
5(1): 7843.
Dawes, R. M. 1980. Social Dilemmas. Annual Review of
Psychology, 31(1): 169–193.
de Cote, E. M.; Lazaric, A.; and Restelli, M. 2006. Learning
to cooperate in multi-agent social dilemmas. In Proceedings
of the 5th International Conference on Autonomous Agents
and Multiagent Systems (AAMAS’06), 783–785.
Fehr, E.; and Fischbacher, U. 2002.
Why social prefer-
ences matter – the impact of non-selfish motives on compe-
tition, cooperation and incentives. The Economic Journal,
112(478): 1–33.
Fehr, E.; and Fischbacher, U. 2004. Social norms and human
cooperation. Trends in Cognitive Sciences, 8(4): 185–190.
Gert, B. 2004. Common Morality: Deciding What to Do.
New York: Oxford University Press.
Gini, C. 1912. Variabilit`a e Mutabilit`a: Contributo allo stu-
dio delle distribuzioni e delle relazioni statistiche. [Fasc. I.].
Tipografia di P. Cuppini.
Graham, J.; Haidt, J.; Koleva, S.; Motyl, M.; Iyer, R.; Woj-
cik, S. P.; and Ditto, P. H. 2013. Moral Foundations Theory:
The pragmatic validity of moral pluralism. In Advances in
Experimental Social Psychology, volume 47, 55–130. Aca-
demic Press.
Graham, J.; Haidt, J.; and Nosek, B. A. 2009. Liberals and
conservatives rely on different sets of moral foundations.
Journal of Personality and Social Psychology, 96(5): 1029–
1046.
Hofbauer, J.; and Sigmund, K. 1998. Evolutionary Games
and Population Dynamics. Cambridge University Press.
Hughes, E.; Leibo, J. Z.; Phillips, M.; Tuyls, K.; Due˜nez-
Guzman, E.; Garc´ıa Casta˜neda, A.; Dunning, I.; Zhu, T.;
McKee, K.; Koster, R.; Zhu, T.; Roff, H.; and Graepel, T.
2018. Inequity aversion improves cooperation in intertem-
poral social dilemmas. In Proceedings of the 32nd Inter-
national Conference on Neural Information Processing Sys-
tems (NeurIPS’18), volume 31, 3330–3340.
Jaques, N.; Lazaridou, A.; Hughes, E.; Gulcehre, C.; Ortega,
P.; Strouse, D.; Leibo, J. Z.; and De Freitas, N. 2019. Social
influence as intrinsic motivation for multi-agent deep rein-
forcement learning. In Proceedings of the 36th International

--- Page 11 ---

Conference on Machine Learning (ICML’19), 3040–3049.
PMLR.
Kant, I. 1785. Grounding for the Metaphysics of Morals.
Cambridge University Press.
Kingma, D. P.; and Ba, J. 2015.
Adam: A Method for
Stochastic Optimization. In Proceedings of the 3rd Interna-
tional Conference on Learning Representations (ICLR’15).
Leibo, J. Z.; Hughes, E.; Lanctot, M.; and Graepel, T.
2019.
Autocurricula and the Emergence of Innovation
from Social Interaction: A Manifesto for Multi-Agent In-
telligence Research.
arXiv preprint arXiv:1903.00742.
arXiv:1903.00742.
Leibo, J. Z.; Zambaldi, V.; Lanctot, M.; Marecki, J.; and
Graepel, T. 2017. Multi-agent reinforcement learning in se-
quential social dilemmas. In Proceedings of the 16th Inter-
national Conference on Autonomous Agents and Multiagent
Systems (AAMAS’17), 464–473.
Lifton, P. D. 1985. Individual differences in moral develop-
ment: The relation of sex, gender, and personality to moral-
ity. Journal of Personality, 53(2): 306–334.
Littman, M. L. 1994. Markov games as a framework for
multi-agent reinforcement learning. In Proceedings of the
11th International Conference on International Conference
on Machine Learning (ICML’94), 157–163.
Mayo-Wilson, C.; and Zollman, K. J. S. 2021. The com-
putational philosophy: simulation as a core philosophical
method. Synthese, 199(1-2): 3647–3673.
McKee, K. R.; Gemp, I.; McWilliams, B.; Du`e˜nez Guzm´an,
E. A.; Hughes, E.; and Leibo, J. Z. 2020. Social diversity
and social preferences in mixed-motive reinforcement learn-
ing. In Proceedings of the 19th International Conference on
Autonomous Agents and MultiAgent Systems (AAMAS’20),
869–877.
McKee, K. R.; Leibo, J. Z.; Beattie, C.; and Everett, R. 2022.
Quantifying the effects of environment and population di-
versity in multi-agent reinforcement learning. Autonomous
Agents and Multi-Agent Systems, 36(1): 21.
McKenzie, A. J. 2007. The Structural Evolution of Morality.
Cambridge University Press.
Mnih, V.; Kavukcuoglu, K.; Silver, D.; Rusu, A. A.; Veness,
J.; Bellemare, M. G.; Graves, A.; Riedmiller, M.; Fidjeland,
A. K.; Ostrovski, G.; Petersen, S.; Beattie, C.; Sadik, A.;
Antonoglou, I.; King, H.; Kumaran, D.; Wierstra, D.; Legg,
S.; and Hassabis, D. 2015.
Human-level control through
deep reinforcement learning. Nature, 518(7540): 529–533.
Ord, T. 2015. Moral Trade. Ethics, 126(1): 118–138.
Ouyang, L.; Wu, J.; Jiang, X.; Almeida, D.; Wainwright,
C.; Mishkin, P.; Zhang, C.; Agarwal, S.; Slama, K.; Ray,
A.; Schulman, J.; Hilton, J.; Kelton, F.; Miller, L.; Simens,
M.; Askell, A.; Welinder, P.; Christiano, P. F.; Leike, J.; and
Lowe, R. 2022. Training language models to follow instruc-
tions with human feedback. In Proceedings of the 36th In-
ternational Conference on Neural Information Processing
Systems (NeurIPS’22), volume 35, 27730–27744.
Peysakhovich, A.; and Lerer, A. 2018. Consequentialist con-
ditional cooperation in social dilemmas with imperfect in-
formation. In Proceedings of the 6th International Confer-
ence on Learning Representations (ICLR’18).
Rapoport, A. 1974. Prisoner’s dilemma — recollections and
observations.
In Game Theory as a Theory of a Conflict
Resolution, 17–34. Springer.
Reid, T.; and Haakonssen, K. 1990. Thomas Reid on Prac-
tical Ethics. Princeton University Press.
Sandholm, T. W.; and Crites, R. H. 1996.
Multiagent
reinforcement learning in the iterated prisoner’s dilemma.
Biosystems, 37(1-2): 147–166.
Santos, F. C.; Santos, M. D.; and Pacheco, J. M. 2008. Social
diversity promotes the emergence of cooperation in public
goods games. Nature, 454(7201): 213–216.
Shenoy, P. P. 1979.
On Coalition Formation: A Game-
Theoretical Approach.
In International Journal of Game
Theory, volume 8.
Sigmund, K. 2010. The Calculus of Selfishness. Princeton
University Press.
Sigmund, K.; and Nowak, M. A. 1999. Evolutionary game
theory. Current Biology, 9(14): R503–R505.
Sinnott-Armstrong, W. 2008. Moral Psychology: The Evo-
lution of Morality: Adaptations and Innateness. MIT Press.
Sutton, R. S.; and Barto, A. G. 2018. Reinforcement Learn-
ing: An Introduction. MIT Press. ISBN 0262039249.
Tennant, E.; Hailes, S.; and Musolesi, M. 2023a.
Learn-
ing Machine Morality through Experience and Interaction.
arXiv Preprint. arXiv:2312.01818.
Tennant, E.; Hailes, S.; and Musolesi, M. 2023b. Modeling
Moral Choices in Social Dilemmas with Multi-Agent Re-
inforcement Learning. In Proceedings of the 32nd Interna-
tional Joint Conference on Artificial Intelligence (IJCAI’23),
317–325.
Watkins, C. J.; and Dayan, P. 1992. Q-learning. Machine
Learning, 8(3): 279–292.

--- Page 12 ---

Appendix
Action Pairs within Each Population
An analysis of action pairs in Figure 6 provides further in-
sight into the pair-wise interactions in each population, in-
cluding mutual cooperation (C,C); unilateral exploitation
(C,D or D,C); and mutual defection (D,D) observed at ev-
ery episode. We observe that the high levels of cooperation
in the majority-Ut and majority-V-Ki populations are largely
driven by mutual cooperation, and that the low cooperation
in the majority-aUt, majority-V-Ag and the majority-V-Eq
populations can be largely attributed to high mutual defec-
tion. In other populations, a much higher level of exploita-
tion (i.e., unilateral defection) is observed, and in certain
pro-social populations, such as majority-De, this is largely
due to the selecting player being exploited by their selected
opponent.
Cooperation by Each Player Type across
Populations
In addition to the analysis of the S agents’ behavior across
populations presented in the main body of the paper, Figures
7a & 7b present the dynamics of cooperation over time for
every other player type in every population.
For all players except V-Eq and V-In, levels of cooperation
are relatively consistent across populations. V-Ki and V-Ag
players go through an initial phase of low or high cooper-
ation, respectively, after which we observe stable behaviors
consistent with their intrinsic reward (i.e., cooperation by V-
Ki and defection by V-Ag). The other norm-based pro-social
player De converges to full cooperation very quickly, show-
ing that this definition of the norm produces the strongest
signal for cooperation in the IPD (extending the findings of
Tennant, Hailes, and Musolesi 2023b to the population case
as well). This agent’s anti-social counterpart mDe, however,
does not display full defection, likely due to the partner se-
lection mechanism providing an incentive to cooperate in
order to get selected more often to play. The Ut and aUt
players converge to either full cooperation or full defection
respectively in all populations nearly equally, but the rate
of convergence is faster for the anti-social player, likely due
to the payoffs associated with defection in the IPD game.
The V-Eq and V-In players cooperate to variable extents in
different populations, but in a way that is consistent with
the choice of their reward functions (e.g., defect more in a
majority-defective population).
Selection Patterns between Player Types
In addition to the analysis of selections made over the entire
simulation in the two populations presented in the main body
of the paper (majority-S and majority-De, see Figure 4a &
4b), we show selections made by each individual player in
every population in Figures 8a & 8b (as a heat map) and
Figures 9a & 9b (as networks involving the top 15% of the
pairs in terms of number of interactions observed). The latter
show the most common patterns of interaction among play-
ers in these artificial societies - for example, in the majority-
De population, the De players select other types of oppo-
nents more often than each other.
Partner Selection Algorithm
The algorithm for partner selection (sel) and at the basis of
the dilemma game (dil) with 2 separate Q-network models
is presented below (see Algorithm 1). We use episodes, so
that all players learn simultaneously, after each player had a
single chance to select and play. For clarity, each selector’s
state st
i,sel relies on the same environment state (i.e., si-
multaneous selections), and therefore every player i’s st+1
i,sel
in the sel trajectory only differs from st
i,sel by one entry:
at
j,dil at player j’s position. For dil, each player i uses all of
their observed dilemma trajectories to update their network,
by calculating an average loss across these trajectories.
We use the DQN algorithm for agents learning to select
and to play the dilemma (Mnih et al. 2015), with a slight
simplification: we refresh the experience buffer at the end
of every episode (see Algorithm 1), and we do not freeze
the network weights (experiments showed that freezing the
network made no impact on the stability of the learning).

--- Page 13 ---

Figure 6: Action pairs observed on every episode in every population (we sum the 16 interactions within an episode, and then
count the number of occurrences of each action pair across 20 runs). The ordering of actions within each pair corresponds
to the selecting player first, and the selected opponent second. Thus, action pairs are interpreted as follows: (C,C) = mutual
cooperation; (C,D) = selecting player gets exploited; (D,C) = selected player gets exploited; (D,D) = mutual defection.

--- Page 14 ---

Figure 7a: Cooperation by each player type over time in populations majority-S, majority-Ut, majority-aUt, majority-De and
majority-mDe. In these charts, we plot the moving average of the mean across 20 runs. Where more than one player of a certain
type is present in a population, we average the values across all the players of that type (e.g. 8xS players in the majority-S
population).

--- Page 15 ---

Figure 7b: Cooperation by each player type over time in populations majority-V-Eq, majority-V-In, majority-V-Ki and majority-
V-Ag. In these charts, we plot the moving average of the mean across 20 runs. Where more than one player of a certain type is
present in a population, we average the values across all the players of that type (e.g. 8xS players in the majority-S population).

--- Page 16 ---

0_S
1_S
2_S
3_S
4_S
5_S
6_S
7_S
8_Ut
9_De
10_V-Eq
11_V-Ki
12_aUt
13_mDe
14_V-In
15_V-Ag
Player 2 (selectED)
0_S
1_S
2_S
3_S
4_S
5_S
6_S
7_S
8_Ut
9_De
10_V-Eq
11_V-Ki
12_aUt
13_mDe
14_V-In
15_V-Ag
Player 1 (selectOR)
Selection dynamics across players 
 in population majority-S 
 (# times selected) 
 (over episodes 1-30000) 
0
2000
4000
6000
8000
0_S
1_Ut
2_Ut
3_Ut
4_Ut
5_Ut
6_Ut
7_Ut
8_Ut
9_De
10_V-Eq
11_V-Ki
12_aUt
13_mDe
14_V-In
15_V-Ag
Player 2 (selectED)
0_S
1_Ut
2_Ut
3_Ut
4_Ut
5_Ut
6_Ut
7_Ut
8_Ut
9_De
10_V-Eq
11_V-Ki
12_aUt
13_mDe
14_V-In
15_V-Ag
Player 1 (selectOR)
Selection dynamics across players 
 in population majority-Ut 
 (# times selected) 
 (over episodes 1-30000) 
0
2000
4000
6000
8000
0_S
1_Ut
2_De
3_V-Eq
4_V-Ki
5_aUt
6_aUt
7_aUt
8_aUt
9_aUt
10_aUt
11_aUt
12_aUt
13_mDe
14_V-In
15_V-Ag
Player 2 (selectED)
0_S
1_Ut
2_De
3_V-Eq
4_V-Ki
5_aUt
6_aUt
7_aUt
8_aUt
9_aUt
10_aUt
11_aUt
12_aUt
13_mDe
14_V-In
15_V-Ag
Player 1 (selectOR)
Selection dynamics across players 
 in population majority-aUt 
 (# times selected) 
 (over episodes 1-30000) 
0
2000
4000
6000
8000
10000
12000
0_S
1_Ut
2_De
3_De
4_De
5_De
6_De
7_De
8_De
9_De
10_V-Eq
11_V-Ki
12_aUt
13_mDe
14_V-In
15_V-Ag
Player 2 (selectED)
0_S
1_Ut
2_De
3_De
4_De
5_De
6_De
7_De
8_De
9_De
10_V-Eq
11_V-Ki
12_aUt
13_mDe
14_V-In
15_V-Ag
Player 1 (selectOR)
Selection dynamics across players 
 in population majority-De 
 (# times selected) 
 (over episodes 1-30000) 
0
2000
4000
6000
8000
10000
0_S
1_Ut
2_De
3_V-Eq
4_V-Ki
5_aUt
6_mDe
7_mDe
8_mDe
9_mDe
10_mDe
11_mDe
12_mDe
13_mDe
14_V-In
15_V-Ag
Player 2 (selectED)
0_S
1_Ut
2_De
3_V-Eq
4_V-Ki
5_aUt
6_mDe
7_mDe
8_mDe
9_mDe
10_mDe
11_mDe
12_mDe
13_mDe
14_V-In
15_V-Ag
Player 1 (selectOR)
Selection dynamics across players 
 in population majority-mDe 
 (# times selected) 
 (over episodes 1-30000) 
0
2000
4000
6000
8000
10000
12000
Figure 8a: Selections made by individual player types in populations majority-S, majority-Ut, majority-aUt, majority-De and
majority-mDe. The number of selections in every cell is summed over all 30000 episodes (average across 20 runs).

--- Page 17 ---

0_S
1_Ut
2_De
3_V-Eq
4_V-Eq
5_V-Eq
6_V-Eq
7_V-Eq
8_V-Eq
9_V-Eq
10_V-Eq
11_V-Ki
12_aUt
13_mDe
14_V-In
15_V-Ag
Player 2 (selectED)
0_S
1_Ut
2_De
3_V-Eq
4_V-Eq
5_V-Eq
6_V-Eq
7_V-Eq
8_V-Eq
9_V-Eq
10_V-Eq
11_V-Ki
12_aUt
13_mDe
14_V-In
15_V-Ag
Player 1 (selectOR)
Selection dynamics across players 
 in population majority-V-Eq 
 (# times selected) 
 (over episodes 1-30000) 
0
2000
4000
6000
8000
10000
0_S
1_Ut
2_De
3_V-Eq
4_V-Ki
5_aUt
6_mDe
7_V-In
8_V-In
9_V-In
10_V-In
11_V-In
12_V-In
13_V-In
14_V-In
15_V-Ag
Player 2 (selectED)
0_S
1_Ut
2_De
3_V-Eq
4_V-Ki
5_aUt
6_mDe
7_V-In
8_V-In
9_V-In
10_V-In
11_V-In
12_V-In
13_V-In
14_V-In
15_V-Ag
Player 1 (selectOR)
Selection dynamics across players 
 in population majority-V-In 
 (# times selected) 
 (over episodes 1-30000) 
0
1000
2000
3000
4000
5000
6000
7000
8000
0_S
1_Ut
2_De
3_V-Eq
4_V-Ki
5_V-Ki
6_V-Ki
7_V-Ki
8_V-Ki
9_V-Ki
10_V-Ki
11_V-Ki
12_aUt
13_mDe
14_V-In
15_V-Ag
Player 2 (selectED)
0_S
1_Ut
2_De
3_V-Eq
4_V-Ki
5_V-Ki
6_V-Ki
7_V-Ki
8_V-Ki
9_V-Ki
10_V-Ki
11_V-Ki
12_aUt
13_mDe
14_V-In
15_V-Ag
Player 1 (selectOR)
Selection dynamics across players 
 in population majority-V-Ki 
 (# times selected) 
 (over episodes 1-30000) 
0
2000
4000
6000
8000
0_S
1_Ut
2_De
3_V-Eq
4_V-Ki
5_aUt
6_mDe
7_V-In
8_V-Ag
9_V-Ag
10_V-Ag
11_V-Ag
12_V-Ag
13_V-Ag
14_V-Ag
15_V-Ag
Player 2 (selectED)
0_S
1_Ut
2_De
3_V-Eq
4_V-Ki
5_aUt
6_mDe
7_V-In
8_V-Ag
9_V-Ag
10_V-Ag
11_V-Ag
12_V-Ag
13_V-Ag
14_V-Ag
15_V-Ag
Player 1 (selectOR)
Selection dynamics across players 
 in population majority-V-Ag 
 (# times selected) 
 (over episodes 1-30000) 
0
2000
4000
6000
8000
10000
12000
14000
Figure 8b: Selections made by individual players in populations majority-V-Eq, majority-V-In, majority-V-Ki and majority-V-
Ag. The number of selections in every cell is summed over all 30000 episodes (average across 20 runs).

--- Page 18 ---

0
S
1
S
2
S
3
S
4
S
5
S
6
S
7
S
8
Ut
9
De
10
V-Eq
11
V-Ki
12
aUt
13
mDe
14
V-In
15
V-Ag
Selections 
 in population majority-S 
 threshold > 85th percentile
0
S
1
Ut
2
Ut
3
Ut
4
Ut
5
Ut
6
Ut
7
Ut
8
Ut
9
De
10
V-Eq
11
V-Ki
12
aUt
13
mDe
14
V-In
15
V-Ag
Selections 
 in population majority-Ut 
 threshold > 85th percentile
0
S
1
Ut
2
De
3
V-Eq
4
V-Ki
5
aUt
6
aUt
7
aUt
8
aUt
9
aUt
10
aUt
11
aUt
12
aUt
13
mDe
14
V-In
15
V-Ag
Selections 
 in population majority-aUt 
 threshold > 85th percentile
0
S
1
Ut
2
De
3
De
4
De
5
De
6
De
7
De
8
De
9
De
10
V-Eq
11
V-Ki
12
aUt
13
mDe
14
V-In
15
V-Ag
Selections 
 in population majority-De 
 threshold > 85th percentile
0
S
1
Ut
2
De
3
V-Eq
4
V-Ki
5
aUt
6
mDe
7
mDe
8
mDe
9
mDe
10
mDe
11
mDe
12
mDe
13
mDe
14
V-In
15
V-Ag
Selections 
 in population majority-mDe 
 threshold > 85th percentile
Figure 9a: Selections made by individual players in populations majority-S, majority-Ut, majority-aUt, majority-De and
majority-mDe. Edges are weighted by the number of selections made between the pair of players. We visualize the most
common interactions, i.e., above the 85th percentile, over all 30000 episodes. More popular players are placed more centrally
using a force-directed algorithm.

--- Page 19 ---

0
S
1
Ut
2
De
3
V-Eq
4
V-Eq
5
V-Eq
6
V-Eq
7
V-Eq
8
V-Eq
9
V-Eq
10
V-Eq
11
V-Ki
12
aUt
13
mDe
14
V-In
15
V-Ag
Selections 
 in population majority-V-Eq 
 threshold > 85th percentile
0
S
1
Ut
2
De
3
V-Eq
4
V-Ki
5
aUt
6
mDe
7
V-In
8
V-In
9
V-In
10
V-In
11
V-In
12
V-In
13
V-In
14
V-In
15
V-Ag
Selections 
 in population majority-V-In 
 threshold > 85th percentile
0
S
1
Ut
2
De
3
V-Eq
4
V-Ki
5
V-Ki
6
V-Ki
7
V-Ki
8
V-Ki
9
V-Ki
10
V-Ki
11
V-Ki
12
aUt
13
mDe
14
V-In
15
V-Ag
Selections 
 in population majority-V-Ki 
 threshold > 85th percentile
0
S
1
Ut
2
De
3
V-Eq
4
V-Ki
5
aUt
6
mDe
7
V-In
8
V-Ag
9
V-Ag
10
V-Ag
11
V-Ag
12
V-Ag
13
V-Ag
14
V-Ag
15
V-Ag
Selections 
 in population majority-V-Ag 
 threshold > 85th percentile
Figure 9b: Selections made by individual players in populations majority-V-Eq, majority-V-In, majority-V-Ki and majority-
V-Ag. Edges are weighted by the number of selections made between the pair of players. We visualize the most common
interactions, i.e., above the 85th percentile, over all 30000 episodes. More popular players are placed more centrally using a
force-directed algorithm.

--- Page 20 ---

Algorithm 1: Partner selection algorithm
Require: population of players P of size N, total episodes T = 30000
1: set random initial environment state (i.e., one random move for each player)
2: for all players i ∈P do
3:
initialize selection memory Di,sel and dilemma memory Di,dil (capacity 256 to allow experience replay)
4:
initialize value functions Qi,sel, Qi,dil
5:
set random initial selection & dilemma states (st=0
i,sel, st=0
i,dil)
6: end for
7: initialize iterations counter t = 0
8: for all episode ←1, T do
9:
Get current global environment state from the environment
10:
PART 1: Partner Selection
11:
for all players i ∈P do
12:
if episode = 0 then
13:
use random state stored in st=0
sel on first episode
14:
else
15:
i observes the environment state and removes itself to parse in their own st
i,sel
16:
end if
17:
t ←t + 1
18:
using st
i,sel, Qi,sel and ϵ-greedy policy, i selects a partner j (i.e., takes action at
i,sel)
19:
store pair of agents {i, j} in this episode’s sub-population Pepisode
20:
end for
21:
PART 2: Dilemma Game
22:
for all {i, j} ∈Pepisode do
23:
if episode = 0 then
24:
use random dilemma state stored in st=0
dil on first episode
25:
else
26:
i and j parse states st
i,dil, st
j,dil from the environment state & the current opponent’s index
27:
end if
28:
using st
i,dil, Qi,dil and ϵ-greedy policy, i plays a move at
i,dil
29:
using st
j,dil, Qj,dil and ϵ-greedy policy, j simultaneously plays a move at
j,dil
30:
i and j receive rewards rt
i,dil & rt
j,dil respectively
31:
i and j observe st+1
dil based on the current opponent’s action at: st+1
i,dil = at
j,dil; st+1
j,dil = at
i,dil
32:
player i copies the dilemma reward to the selection reward as well: rt
i,sel = rt
i,dil
33:
in player i’s Di,dil memory, store: (st
i,dil, at
i,dil, rt
i,dil, st+1
i,dil)
34:
in player j’s Dj,dil memory, store: (st
j,dil, at
j,dil, rt
j,dil, st+1
j,dil)
35:
end for
36:
PART 3: Update sel and dil networks
37:
for all players i ∈P do
38:
update the corresponding part of environment state with the latest moves by i (at
i,dil)
39:
player i observes their st+1
i,sel by copying the latest environment state and removing self
40:
in player i’s Di,sel memory, store: (st
i,sel, at
i,sel, rt
i,sel, st+1
i,sel)
41:
player i samples one experience from Di,sel: (st
i,sel, at
i,sel, rt
i,sel, st+1
i,sel) & calculates loss
42:
player i samples all experiences from Di,dil: (st
i,dil, at
i,dil, rt
i,dil, st+1
i,dil) & calculates average loss
43:
player i updates Qi,sel network with respect to time step t & the calculated loss
44:
player i updates Qi,dil network with respect to time step t & the calculated loss
45:
refresh memory buffers Di,sel, Di,dil, Dj,dil
46:
end for
47: end for

```
