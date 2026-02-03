---
title: "Hard Problem AI Alignment Value Forks - PDF Extract"
source_pdf: "2025-Kneer-Hard Problem AI Alignment Value Forks.pdf"
pages: 11
extracted_at: "2026-01-25T05:00:19.636993"
---

# PDF Extract: Hard Problem AI Alignment Value Forks

**Source PDF:** 2025-Kneer-Hard Problem AI Alignment Value Forks.pdf
**Total Pages:** 11

---

## Content

```
--- Page 1 ---

The Hard Problem of AI Alignment:
Value Forks in Moral Judgment
Markus Kneer
University of Graz
Graz, Austria
markus.kneer@uni-graz.at
Juri Viehoff
University of Utrecht
Utrecht, Netherlands
j.b.viehoff@uu.nl
Abstract
Complex moral trade-offs are a basic feature of human life: for ex-
ample, confronted with scarce medical resources, doctors must fre-
quently choose who amongst equally deserving candidates receives
medical treatment. But choosing what to do in moral trade-offs is
no longer a ‘humans-only’ task, but often falls to AI agents. In this
article, we report findings from a series of experiments (N=1029)
intended to establish whether agent-type (Human vs. AI) matters
for what should be done in moral trade-offs. We find that, relative
to a human decision-maker, participants more often judge that AI
agents should opt for fairness at the expense of maximizing utility.
In our discussion, we explain how the reported differences (we call
them agent-type ‘value forks’) matters for the study of moral value
alignment, and we hypothesize what could explain these value
forks. We close by reflecting on limits of our results and indicate
avenues of further research.
CCS Concepts
• Computing methodologies; • Artificial intelligence; •
Human-centered computing; • Human computer interaction
(HCI); • Empirical studies in HCI;
Keywords
Artificial Intelligence, value alignment, complex moral trade-offs,
algorithmic decision-making, machine ethics
ACM Reference Format:
Markus Kneer and Juri Viehoff. 2025. The Hard Problem of AI Alignment:
Value Forks in Moral Judgment. In The 2025 ACM Conference on Fairness,
Accountability, and Transparency (FAccT ’25), June 23–26, 2025, Athens,
Greece. ACM, New York, NY, USA, 11 pages. https://doi.org/10.1145/3715275.
3732174
1
Introduction
Recent years have seen a dramatic increase in the use of artifi-
cial intelligence (AI) and machine learning technologies across a
broad range of domains. Today, AI is deployed far beyond ‘classic’
application contexts like Amazon’s recommendation or Google’s
search universe [72, 81]. Rolled out by sector specific technology
firms (ranging from Duolingo over Waymo to Palantir), AI is now
prominently deployed in education [38], physical exercise [4], trans-
portation [1], law enforcement [7], healthcare [77], and the military
This work is licensed under a Creative Commons Attribution 4.0 International License.
FAccT ’25, Athens, Greece
© 2025 Copyright held by the owner/author(s).
ACM ISBN 979-8-4007-1482-5/2025/06
https://doi.org/10.1145/3715275.3732174
[42]. Across many of these domains, AI is charged with ever more
complex tasks. Moreover, AI systems are becoming more and more
autonomous. Whilst the use of AI in some domains seems by and
large innocuous (e.g. physical exercise), its use in sensitive areas
like the military, law enforcement and public administration has
given rise to much controversy about such issues as discrimina-
tion, bias, and fairness [24, 49, 67]. Amongst researchers, it has led
to sophisticated debates about such issues as algorithmic fairness
[2, 12, 20, 34, 35, 49, 50], value alignment [3, 10, 27], and how new
technologies shape the perception of fundamental human values
[15, 16, 41, 64].
This article contributes to the topic of how technological change
shapes moral judgment in sensitive areas of deployment, where
complex moral tradeoffs and moral dilemmas are likely to occur.
Focusing on healthcare and military contexts, we investigate the
following research question: In decision-making contexts, does
variation in the type of agent (human vs. AI agent) influence what
option is deemed preferable? And if so, what explains this difference
and how should we respond in the domain of value alignment? We
report empirical findings from experiments (N=1029 participants)
that suggest that the agent-type of the decision-maker (Human vs.
AI) sometimes matters for what option should be chosen. Specif-
ically, we find that, in dilemmas where the acting agent is an AI
system, participants think it is more important to deviate from a
utility-maximizing course of action and to provide equal chances
of survival to would-be victims than when the decision maker is
a human agent. In other words, subjects prefer, at least in some
cases, that a human decision-maker act more utilitarian than an
AI agent facing the same dilemma. In our discussion, we explain
why (and how) results of this sort—we call them agent-type value
forks—are relevant for the theoretical underpinnings and practical
implementations of value alignment. Specifically, we surmise that
our findings indicate the existence of a Hard Problem of AI Align-
ment: In calibrating AI to act consistent with human values, do
we want it to act in accordance with those values (or norms) that
we would expect humans to satisfy in the particular circumstances,
or in line with potentially differing values/norms that we would
expect AI systems to satisfy?
2
Background: Value Alignment, Moral
Dilemmas, and ‘Public Reflective Equilibrium’
The aim of AI value alignment is to find principles, procedures and,
ultimately, technical solutions to make the actions and decisions of
AI systems cohere with human values. Ensuring that AI systems
conform to standards of human moral assessment is of special
importance because to human agents, moral values are typically
especially important and motivating, if not overriding [29, 83].

--- Page 2 ---

FAccT ’25, June 23–26, 2025, Athens, Greece
Markus Kneer and Juri Viehoff
Value alignment seems especially important in contexts where AI
systems must make choices about the competitive distribution of
central human goods between different individuals. We will call
such situations complex moral trade-off cases (or short: dilemmas).
Perhaps most famously, standard ‘trolley cases’ confront a decision-
maker with a sacrificial dilemma: either let a number of people
die or intervene to save them but, through the intervention, kill a
smaller number of other people [22, 25, 47, 85]. Other dilemmas
force us to choose between helping a small number of very severely
ill people or a much larger number of moderately ill ones [66, 91, 92],
or between maximizing the total sum of wellbeing we can bring
about or giving equally impacted people equal (fair) chances of
survival [8, 9, 19, 45, 48].
Two distinct approaches or ideal types of moral value alignment
have figured prominently [3, 27]: top-down and bottom-up. Accord-
ing to one approach to value alignment, those deploying AI system
should explicitly program the AI system before deployment to fol-
low a set of pre-determined norms and values, or a moral theory.
So, for dilemma scenarios, the system should be pre-programmed
to always choose what is seen as the ‘correct’ moral choice (e.g.
‘Kill one to save five!’; ‘Treat the most injured party first!’; ‘Ran-
domize when having to choose between equally affected parties!’
etc.). According to bottom-up approaches, by contrast, AI systems
should learn implicitly from the data it is trained on (and possibly
subsequent interactions with users). Since there is little ‘training
data’ for how humans respond to dilemmas in actual social life, we
might, on this approach, need to follow survey and experimental
data about what human subjects think should be done when they
imagine facing these dilemmas.
As has been widely discussed in the recent literature, each of
these ideal types to alignment faces challenges ([28, 93, 94], for
a survey of concrete implementations, see: [86]): Whereas top-
down alignment (i.e. fixing a specific response to a dilemmatic
scenario) ensures that AI behavior is predictable and consistent
with predefined ethical guidelines—thus potentially providing a
straightforward way to verify and validate the AI’s actions against
specific standards—its rigidity of predefined values/norms may not
be flexible or adaptive enough for unforeseen situations (what about
killing three to save six?) [3, 93]. Moreover, such an approach faces
a ‘legitimacy problem’: in a pluralistic democratic setting charac-
terized by a great diversity of (reasonable) moral views, it is unclear
whose norms and values should be pre-programmed into an AI
system [27]. This general worry about top-down value alignment
seems especially pertinent in complex moral trade-offs: these are
exactly the kind of ‘edge cases’ about which even reasonable per-
sons can fundamentally disagree. A bottom-up approach seems
initially better equipped to respond to the issue of legitimacy be-
cause norms/values that are implemented are not chosen unilat-
erally by some technologist(s). Moreover, it is more nuanced and
adaptable, capable of evolving with changing societal values and
complex situations [28]. However, it faces the serious problem that
its training data may encapsulate morally indefensible views and
practices, ranging from bias via discrimination to racism [36, 67].
Responding to these difficulties, a number of theorists writing
on alignment have proposed approaches that combine top-down
and bottom-up in novel ways [10, 74, 88]: One way to implement
such a hybrid approach is the following: First, one seeks to gener-
ate domain-specific, high quality ‘moral common sense’ data for
specific contexts and moral dilemmas. In a second step, the most
prominent moral views discernible from the data are probed using
the logical and argumentative tools of moral philosophy. The result
is a kind of ‘public’ reflective equilibrium [6, 18, 70, 78] that has a
more secure justificatory foundation than its alternatives. Recon-
structing alignment from folk intuitions addresses, up to a point,
the worry about legitimacy because the prevailing moral views of
those that will be subject to the AI play some procedural role in
determining how to align. Our approach below exemplifies this
method in relation to one important aspect of a moral dilemma
situation, namely the agent-type of the decision-maker. In other
words, our subjects confront the same moral dilemma but for the
difference that the agent acting in the dilemma is either a human or
an AI agent. We first collected detailed, controlled moral common
sense data from participants. In a second step, these judgments
were then probed using philosophical analysis. Concretely, we ask:
can the observed agent-type-based difference in laypeople judg-
ment be supported by a plausible argument in moral theorizing?
Before we proceed to our experiments, we will briefly summarize
extant empirical findings in the domain of sacrificial dilemmas and
human-robot interaction.
3
Existing Empirical Work
3.1
Moral Psychology and Experimental
Philosophy
If good value alignment approaches stand to benefit from a sys-
tematic understanding of the prevailing moral sense in specific
moral trade-off situations, then it seems only natural to look to
the findings of experimental philosophy and moral psychology re-
garding complex moral trade-offs, and, second, to the specialized
empirical study of human-robot interaction (HRI). Within this body
of literature, there are many studies that analyze whether human
moral cognition conforms more to consequentialist or deontologi-
cal moral precepts ([13, 31, 32], for criticism, see: [43, 44, 71]). More
recently, there have been important attempts to get a fuller pic-
ture on important elements of non-consequentialist moral common
sense. This is important because a large percentage of laypeople—
often a majority—report moral judgments that are not consis-
tent with fully consequentialist (aggregative) moral theories [65].
A number of recent studies have begun to explore specific ele-
ments of non-consequentialist common sense, ranging from ‘thresh-
old deontological’ judgments to ‘partial aggregation’ judgements
[14, 54, 55, 58, 65, 71, 87].
This existing general literature on human-agent complex trade-
offs is a helpful starting point, because it demonstrates the diversity
of positions found in the general population when it comes to
moral trade-off scenarios. However, since authors aim to track
moral intuitions at a very general level, such studies have so far
not analyzed how moral judgment changes when to moral actor
is an AI agent—an important lacuna. As our experiments indicate,
moral common sense contains a sizeable fraction of people whose
judgments feature agent type-based value forks, that is, differences
in judgments concerning wrongness and permissibility that solely
turn on whether the agent taking the trade-off decision is a human
or AI agent.

--- Page 3 ---

The Hard Problem of AI Alignment:
Value Forks in Moral Judgment
FAccT ’25, June 23–26, 2025, Athens, Greece
3.2
Empirical HRI Studies
There is a small, yet rapidly growing, literature on moral aspects
of HRI. Some of this work focuses on the question whether we
are willing to blame robots and/or AI systems for their actions.
From a philosophical point of view, it is quite evident that artefacts
cannot and should not be blamed in any substantial sense. However,
laypeople are surprisingly willing to attribute blame to them when
they produce harmful outcomes [5, 11, 39, 40, 51, 53, 59, 61–63, 69,
73, 79, 90, 97]. Although artificial agents are not adequate targets
of blame, their actions might – arguably – still be normatively
assessable. That is to say, there could be a sense in which it is
plausible to call certain actions and decisions of artificial agents
morally right and wrong, and to hold that they should do certain
things and should not do others. Unsurprisingly, in several studies
that controlled explicitly for moral wrongness, harmful actions
of AI systems were deemed either as wrong as human actions or
wrong to a substantial extent (see e.g. [52, 53, 79, 80]).
What is particularly interesting, however, and the focus of our
paper, is that in situations where there is no clear right or wrong,
and no evident all-considered best decision or action, people can
diverge considerably as regards their assessment of actions by dif-
ferent agent types. The evident place to look are dilemmatic moral
trade-offs, that is, situations where all options lead to bad outcomes,
and where it is frequently not evident which option is the right
(most permissible) one. In the field of experimental HRI studies,
the work of Malle et al. is what comes closest to investigating these
kinds of moral trade-offs whilst paying attention to potential dif-
ferences in agent type ([56, 60], see also [57]) In their study, Malle
et al. compare blame and wrongness judgments when the only
difference between scenarios consists in agent type. Specifically,
they asked participants to evaluate how blameworthy an AI or
human agent is for failing to save the larger number in a typical
trolley-style sacrificial dilemma. What they found is that about one
in two participants (49%) judge that sacrificing one to save four is
wrong if the decision is taken by a human being, but only about one
in eight (13%) report the same judgment when matters are decided
by an artificial agent [60:121]. These are interesting, and important
findings, since they could open up an agent-type value fork, that is,
a gap across what is considered right and wrong across human and
AI agents.
Though clearly important for the study of potential value forks,
what is noteworthy about Malle et al.’s experimental setup is the
fact that it lacks genuine parity between the moral options in terms
of assessed permissibility. It is a widespread finding that a majority
of subjects thinks agents are permitted or even required to save the
larger number in One vs. Five sacrificial dilemmas (i.e. standard
trolley scenarios) [22]—of course, Malle et. al. reduce the perceived
permissibility somewhat by moving to One vs. Four, but they still
report that their participants significantly (65% for the human agent
and 78% for the AI agent) lean towards considering it permissible to
engage in the sacrificial trade-off. In scenarios where there is less
clarity about what the ‘correct’ moral decision is, we may find that
even more weight is given to who the relevant agent making the
moral decision is Moreover, the statistically significant contrasts
that have been observed in relation to agent type by Malle et al. only
related to situations where an action was retrospectively assessed
to be wrongful/blameworthy.
Building on Malle et al.’s work, one conjecture we deem worth
investigating is whether agent type might also shape prospective
judgments of permissibility in scenarios where permissibility judg-
ments are more evenly distributed across the possible choices. We
shift from ‘number cases’ (e.g. standard trolley cases/sacrificial
dilemmas) to scenarios where the relevant conflict concerns the
provision of equal/fair chances to innocent people that stand to
suffer a significant harm, which are much more common in real
life. The value conflict in such cases—theorized by prominently
bioethicists like Frances Kamm and Norman Daniels [17, 46]—arises
when we must choose between either distributing chances fairly
(e.g. through a lottery where each receives an equal chance of
having their need met) or, instead, directly pick an option that
has a marginally higher utility but does not give each would-be
victim a fair chance. Consider Kamm’s famous Sore Throat case:
“a scarce medicine could be given to save the life of either Jim or
Joe, but only if it is given to Jim will there be enough left over to
cure a sore throat that Nancy would otherwise have for a week”
[45:146]. Kamm takes Sore Throat to indicate that sometimes ex
ante chances of being rescued are more important than maximizing
overall wellbeing, and so she speaks of ‘irrelevant utilities’ [45:144].
Whilst many would agree with Kamm that, in this case, we should
hold a fair lottery despite the additional (small) utility that can
be accrued from directly saving Jim and giving the remainder to
Nancy, the conflict becomes more serious if we increase the utility
gap between these options. As recent studies have shown [54, 65],
there are variants of similar scenarios where laypeople judgment is
almost equally divided between binary options. We surmise that,
in the context of investigating agent types value forks, focusing on
fairness/utility trade-offs like these is especially useful: by starting
with very small (‘marginal’) utility gains at the expense of fairness
and then increasing the utility gain that can be achieved by aban-
doning fair chances (‘moderate’) we can clearly assess where people
feel the force of the conflict most strongly.1
4
Experiments
4.1
Participants, Methods and Materials
We recruited 1108 participants from the US on Prolific. Participants
failing an attention check, a comprehension check (choosing the
response which was nonoptimal in any sense), or responding to the
task in under 30 seconds were excluded. 1029 participants remained,
of which 564 were female and 20 identified as non-binary (age M=45
years, SD=14 years).
Our vignettes draw on cases similar to those discussed by Kamm
in the context of conflicts between efficient outcomes and equal ex
ante chances [45]. Analogous trade-offs are discussed in the context
of healthcare rationing and prioritization, and have recently been
1There are of course many different conceptions of fairness in the philosophical litera-
ture (including accounts of specifically algorithmic fairness mentioned above). We
believe, however, that most plausible accounts of the concept will hold that conducting
a fair lottery for a scarce good amongst people with equally strong competing claims
increases fairness relative to not giving each individual such a chance of survival (for
a recent defense of this claim, see: [68]). In fact, on nearly all accounts of fairness,
the kind of dilemma we describe is one in which fairness is traded off against total
wellbeing.

--- Page 4 ---

FAccT ’25, June 23–26, 2025, Athens, Greece
Markus Kneer and Juri Viehoff
Figure 1: Experimental setup and choice situations for the military domain (left) and the medical domain (right)
studied by experimental psychologists and philosophers [9, 17, 48,
54].
We used a 2 scenario (medical v. military context) x 2 contrast
(marginal v. moderate utility difference across outcomes) x 2 agent
type (Human v. AI) between-subjects design. Participants were ran-
domly assigned to one of the eight conditions and thus responded
to only one task each.
In the medical scenario, an ambulance can be dispatched to one of
two accidents: (A), where a driver would be saved from paraplegia,
or (B), where a driver would be saved from paraplegia and the
injured passenger would also receive help. The contrast across (A)
and (B) consists in the harm of the passenger that could be alleviated,
who either suffers from a bruised ankle (marginal contrast) or else
is at risk of losing a finger (moderate contrast). There’s a third
option, (C): to let a coin-flip (or some other fair random process)
decide to which of the two accidents the single available ambulance
should be dispatched. Given that the theoretical literature on non-
consequentialist ethical theory [45, 84, 91] and recent empirical
findings suggest that, at least in the marginal contrast condition, a
substantial proportion of participants would not aggregate utility,
and opt for maximizing fair chances by aid of a coinflip [54], we
added the moderate contrast as an alternative scenario where the
distribution of responses could be expected to be more equally
distributed.
The focus of this paper regards whether the proportions of re-
sponses differ significantly across agent type. The AI condition
states that the medical emergency response center uses “a new
autonomous artificial intelligence system (‘AI algorithm’). The goal
of the AI algorithm is to autonomously (‘without human control or
intervention’) direct ambulances with paramedics to emergencies
that are reported via 911 calls.” By contrast, the human condition
states that a person, Smith, “is the shift leader in charge at a medical
emergency response center. Her job is to direct ambulances with
paramedics to emergencies that are reported via 911 calls.”
Having read the scenario (summarized by 1), participants were
asked which option they preferred. For instance, in the human/mar-
ginal contrast condition, the question read “Which of the following
options should shift leader Smith choose?”, and participants had to
choose from one of the below options:
• Smith should send the ambulance to Accident A (saving one
from paraplegia)
• Smith should send the ambulance to Accident B (saving one
from paraplegia, treating another person’s mildly bruised
ankle)
• Smith should flip a coin to determine whether the ambulance
should go to Accident A or to Accident B
In the military scenario, a terror drone is en route towards the
stadium, which is packed due to a sports event. If the drone is not
shot down, thousands of people will die. There are three possibili-
ties: (A) Shoot down the drone over an ordinary house in Stanton
Street 24, where five will be killed. (B) Shoot down the drone over
Stanton Street 27, also killing five. However, Stanton Street has a
beautiful front garden (marginal utility contrast) or is a landmark
building (moderate utility contrast), which, on purely utilitarian
grounds could speak in favour of saving it. The third option, (C),
again consist in randomizing over option (A) and (B), thus giving
everyone a fair chance of being saved independently of differences
in total utility.
Once again, both the marginal and the moderate utility contrast
conditions came in two versions, one in which the decision maker is
a human, one in which it is an AI system. In the AI condition, “the
city is protected by an autonomous artificial intelligence defense
system (‘AI-DEFENSE’) that has anti-drone missiles installed to
respond to such attacks. AI-DEFENSE is an autonomous weapon
system, which means that it operates without human control or
intervention.” The human condition, by contrast, specifies that a
person, namely Smith, “is the military unit commander in charge,
monitoring the drone with his team.”
The questions were structurally identical to those of the medi-
cal scenario. Note that all questions and responses were framed
in terms of ‘should’ claims, thus eliciting a prospective, deontic
normative judgment. Complete materials and data and the appen-
dix are available at https://osf.io/rqkcz. Given that no identifying
data was collected and the study posed no other potential risks to
participants, it was evaluated as ‘low risk’ according to the self-
evaluation tool of the ethics committee of the University of Zurich,
and required no submission for detailed evaluation.
4.2
Results
4.2.1
General Results. The experiment explored whether partici-
pants thought the agent should maximize utility or maximize fair-
ness by aid of a coin-flip. The third choice – minimizing utility

--- Page 5 ---

The Hard Problem of AI Alignment:
Value Forks in Moral Judgment
FAccT ’25, June 23–26, 2025, Athens, Greece
Table 1: Regression analysis with scenario, agent type and contrast as predictors of morally preferred option.
휒2(7,
N=1029)=187.91, p<.001, Cox & Snell R2=.167, Nagelkerke R2=.223. Reference classes: Scenario = military, Agent type =
AI, Utility difference = moderate. 67.7 % of cases were correctly classified
Regression analysis
B
S.E.
Wald
df
Sig.
Odds Ratio
LLCI
ULCI
Scenario
-1.646
0.289
32.356
1
<.001
0.193
0.109
0.34
Agent
-0.632
0.26
5.901
1
0.015
0.531
0.319
0.885
Contrast
1.165
0.275
17.899
1
<.001
3.207
1.869
5.502
Scenario*Agent
0.847
0.408
4.312
1
0.038
2.334
1.049
5.193
Scenario*Contrast
0.594
0.401
2.199
1
0.138
1.812
0.826
3.973
Agent*Contrast
0.337
0.387
0.756
1
0.385
1.4
0.656
2.991
Scenario*Agent*Contrast
-1.07
0.559
3.662
1
0.056
0.343
0.115
1.026
Constant
0.063
0.177
0.125
1
0.724
1.065
without increasing fairness – is nonsensical and served as a compre-
hension check. Only a very small percentage of participants chose
it across conditions (6.6%), which were excluded from the analysis.2
1 shows a binary logistic regression analysis with scenario, agent
type, and contrast as predictors of the morally preferred option.
All main factors proved significant (all ps<.016), and so did the sce-
nario*agent interaction (p=.038). All further two-way interactions,
as well as the three-way interaction were nonsignificant. Overall,
then, we see that the moral intuitions are sensitive to the context
(healthcare v. military, OR=.19), the marginal utility across the two
contrasts (marginal v. moderate gain, OR=3.21) and – of central
interest to our inquiry – the type of agent who takes the decision
(human v. AI, OR=.53).
We explored correlations between choice (fairness maximizing
v. utility maximizing), age and gender: All were nonsignificant (all
ps>.081), see Appendix, section 1.2.
4.2.2
Individual Scenarios. 2 visualizes the proportions of re-
sponses for the marginal and moderate contrasts in utility in the
healthcare scenario. When the contrast is marginal (the extra utility
consists in treating a mildly bruised ankle), the majority of partici-
pants want to see utility maximized if a human takes the decision,
though for an AI agent it is a minority (the majority prefers the
maximization of fairness by aid of a coinflip). Agent type is signif-
icant (휒2(1, N=255)=4.22, p=.040, 휙=.129). When the contrast is
larger (saving a passenger’s finger), about four in five participants
want to see utility maximized both when a human agent and an AI
agent takes the decision. There is no significant difference across
agent types, 휒2(1, N=268)=5.95, p=.493, 휙=.042.
3 visualizes the proportions of responses for the marginal and
moderate contrast in utility in the military scenario. When the con-
trast is marginal (the extra utility consists in saving a nice front gar-
den), only about one in five opt of utility-maximization: Nearly four
in five instead prefer fairness maximization via a coinflip. Agent
type is nonsignificant (휒2(1, N=259)=1.07, p=.302, 휙=.064.). Where
the contrast is more substantial (the extra utility consists in saving
a landmark building), participants significantly prefer the utility
2All main effects remain significant when those participants choosing the non-sensical
options are included, see Appendix, section 1.1.
Figure 2: Proportions of participants choosing the utility-
maximizing or fairness-maximizing option across contrast
(marginal v. moderate gain) and agent type (human v. AI)
with 95% Wilson confidence intervals.
Figure 3: Proportions of participants choosing the utility-
maximizing or fairness-maximizing option across contrast
(marginal v. moderate gain) and agent type (human v. AI)
with 95% Wilson confidence intervals.
maximizing option in the human agent condition, though they di-
vide near-evenly in the AI agent condition. The difference across
agent types is significant, 휒2(1, N=247)=5.95, p=.015, 휙=.155.

--- Page 6 ---

FAccT ’25, June 23–26, 2025, Athens, Greece
Markus Kneer and Juri Viehoff
Figure 4: Schematic representation of tested scenarios in the space of conceptual possibilities.
5
General Discussion
5.1
Summary of Results
Our findings are fourfold: First, and of considerable general interest
to theoretical moral philosophy and moral psychology, our findings
contribute to the nascent debate concerning the prevalence and
shape of non-consequentialist moral judgment. At a general level,
our study suggests that a significant minority or even a majority
of laypeople report moral judgments that are inconsistent with a
purely consequentialist/maximizing perspective [14, 55, 58, 65, 71,
87]. In one condition of the medical context at least a substantial
minority of over 40% opted for the fairness maximizing option for
either agent type, and in one condition of the military scenario
a significant majority (about three in four) chose the coinflip for
either agent type. These findings are consistent with the—small but
growing—empirical literature on this topic and show the broad gist
of the findings to be robust across a new set of vignettes involving
AI driven decision mechanisms. Our study further substantiates the
existing findings by documenting that such non-consequentialist
judgments remain robust when the acting moral agent is a non-
human (autonomous AI) agent.
Second, and therein resides the key contribution, we have pro-
vided evidence concerning the existence of agent-related value
forks: In both scenarios, participants’ normative judgments were
shown to be sensitive to agent type, i.e. what is deemed best can
differ substantially depending on whether an action is executed by
an AI System or a human agent. We found a significant main effect
of agent type on moral judgment for the data overall, as well as for
one condition in the medical scenario (marginal gain condition) and
the military scenario (moderate gain condition). To our knowledge,
the reported study is the first to document that people’s intuitions
as to what should be done (as compared to what is retrospectively
judged to be right and wrong [60, 76]) differ substantially depending
on the nature of the decision taker.
Third, our results seem to suggest an asymmetry across the two
domains tested: Whereas in the medical scenario, agent type proved
significant in the marginal utility contrast condition, in the military
scenario, agent type was significant in the moderate contrast condi-
tion. In the regression analysis, the interaction between agent type
and scenario was (just about) significant. We would like to cau-
tion care as regards drawing implications from this finding: What
we call a marginal and moderate difference in utility has not been
standardized across contexts. It might, for instance, be that the
perceived utility contrast we call ‘moderate’ in the military scenario
is equivalent to the perceived difference we call ‘marginal’ in the
healthcare context. Inferences of this sort across domains – and,
in fact, even scenarios within domains – must be resisted in the
absence of extensive quantification of perceived utility difference
on a single scale.
In fact, there is a relatively straightforward interpretation, that
explains the findings without scenario type itself playing a key role.
Consider three types of marginal utility differences across cases, as
visually represented in 4 Minimal, limited, and large. In case the
difference is minimal, the results are robustly favouring fairness
maximisation - i.e. other factors, such as agent type cannot exert
an influence. This case is exemplified by the military scenario (mar-
ginal difference) condition. If, on the other end of the spectrum,
the difference is large (or at least deemed considerable), people will
robustly opt for the utility-maximising option – and their judg-
ments will not be influenced by other factors, including agent type.
This case is exemplified by the healthcare (moderate difference)
condition. In between these two extremes lie the interesting cases
of limited difference: Those, where people are divided both within
the human agent condition (i.e. even the minority judgment attains
substantial proportions of about 40%), and across agent-types. Con-
sequently, there is at least one plausible explanation according to
which the effects reported above are independent of scenario type.
Where, exactly, the threshold lies at which value forks manifest
themselves can vary from context to context. That said, future
work should explicitly quantify the perceived marginal utilities
across domains so that more definitive conclusions can be drawn. It
is worth emphasising however that the differential finding between
the military and the healthcare context do not put into question
the key contribution of this article, to wit, the documentation of
agent type value forks in dilemma scenarios.
Fourth: Though our findings are consistent with earlier work
when it comes to the issue of whether or not agent type can make a
difference for some form of moral assessment (i.e. an agent-related

--- Page 7 ---

The Hard Problem of AI Alignment:
Value Forks in Moral Judgment
FAccT ’25, June 23–26, 2025, Athens, Greece
asymmetry), our findings document such a difference for prospec-
tive permissibility/choice-worthiness whereas previous findings
only related to retrospective judgments regarding blame and wrong-
ness [60, 76]. More surprisingly even, our agent-related differences
diverge from previous research when it comes to where the asym-
metry points: Malle et. al. (2015) report that, when it comes to AI,
judgments of wrongness and blame lean more into the direction
of endorsing consequentialist outcomes (that is, failing to sacri-
fice one for the many appears more blameworthy when done by
an autonomous AI system than a human). By contrast, our re-
sults for AI shift in the non-consequentialist direction: participants
believe that fairness matters more (and efficiency/total wellbeing
outcomes matter correspondingly less) when the deciding agent is
an autonomous AI system rather than a human.
In the following we will explain the importance of our findings
for AI value alignment for complex moral tradeoffs. We then look at
potential explanations of our findings. Specifically, we investigate
whether the reported results can be motivated by appeal to existing
arguments in (non-consequentialist) moral theorizing. We close
our discussion by reflecting on the findings’ limits and pointing to
further areas of research.
5.2
The Significance of Value Forks for AI Value
Alignment: More than a Bias?
The implicit assumption behind much of the existing literature
on alignment is that an AI system is fully aligned in the relevant
sense when it does exactly what a human should do given the
circumstances. A first general insight of this article is that, at least
for the kinds of complex moral tradeoffs scenarios we investigated,
value alignment is more complex: Given that agent type can make
a moral difference, we cannot straightforwardly extrapolate from
moral judgments of the form [In scenario X: Human →‘Do Y!’] to
[In scenario X: autonomous AI →‘Do Y!’]). Perhaps paradoxically,
aligning AI with human values may require that an AI act differently
from what a human agent should do, even when facing the exact
same dilemma.3
This AI value fork on matters of permissibility is both surprising
and highly relevant for the theory and practice of value alignment.
What is more, the question as to whether, and if so to what degree,
agent-type matters for decision-making, is unlikely to be settled
solely from the armchair, but requires the combining of additional
empirical work with careful philosophical analysis. One crucial
question is whether we are dealing here merely with some ‘sen-
tience bias’ that can be fully disregarded. By ‘sentience bias’ we
mean an aspect of human cognition that treats the agency of sen-
tient beings as somehow special without us being able to point
to a sound rationale for treating sentient agency different from
any other type of agency [33].4 We call the problem identified the
3In a recent piece on autonomized harming, Eggert contemplates the possibility of what
we call value forks when asking “whether the principles AI systems are programmed
to follow ought to be ‘narrowly aligned’ with those which we take to govern human
agency in the same context.” [23].
4Our notion of sentience bias differs from the concept of automation bias studied by
previous authors [21, 30, 82]: automation bias occur when human subjects prefer
one agent type for a task against the background of equal quality of performance
(e.g. subjects prefer an automated mammography assessment over one by an equally
well-performing human agent [21]). These are (relatively) clear biases because the
equal performance with regard to the pertinent task is assumed. What makes the issue
Hard Problem of AI Alignment because it opens up a range of quite
intractable issues: First, how could we even clearly establish what
counts as a bias in comparing sentient and non-sentient agents?
Can we infer anything meaningful from tests/intuitions for align-
ment if they only explore human as hypothetical agents? How
can we know where value forks occur? And how should we de-
cide which value forks, if any, should be reflected in our alignment
procedures?
5.2.1
Can the Reported Results be Morally Motivated? In one sense,
the reported differences in attributions of choice-worthiness are
perhaps not completely surprising: Even in human-only scenar-
ios, such judgments do frequently depend on the relationships
amongst people and their social roles. For example, according to
both common sense morality and much moral and political theoriz-
ing, what a police officer may permissibly do may differ from what
an ordinary citizen may do [89]. And as demonstrated by some
recent research, social role has proven a significant factor in moral
psychology [26, 59, 95, 96].
But there is a catch for the issue of value alignment concerning
our fork: When it comes to human agents, differences in permis-
sibility or wrongness for the same action derive from differences
in the realization of values and adherence to moral norms that
will result from the fact that actions are performed by different
actor types. What does this mean? To stay with our example, a
police officer’s act of arresting a potential criminal morally differs
from the same action performed by an ordinary citizen because
each of their respective actions, though outwardly identical, en-
gage different moral values and norms. Amongst other things, it
is plausible to think that the citizen’s action, more so than then
police officer’s, increases the risk of a vigilantism and causes a
widespread breakdown of the rule of law. Conversely, we think
that some minor forms of preferential discrimination (say, favoring
one’s friends when a larger number of people require our help) are
morally innocent when displayed by a private citizen, but clearly
objectionable when done by a person charged with public authority
(cf. Thomas Scanlon’s work on the demands of equal treatment by
officials [75]). So even though both agents would engage in actions
that are in one respect identical, the (seeming) conundrum of the
same action being permissible when performed by one agent but
not when performed by another can be resolved.
This raises an important philosophical question for our find-
ings: Is it also possible to make sense of the reported differences
of judgments in relation to AI vs human agency by reference to
morally salient factors? In other words, can we point to (justi-
fied) moral norms or sound value-related considerations that show
how the fact that an action is performed by a human rather than
an AI makes a moral difference? If we can find such reasons,
then the charge of (sentience) ‘bias’ could be set aside. That is
because we now have a coherent rationale that explains differences
in permissibility-attribution. By way of an initial reflection on this
complex issue, we mention three such possible ideas that each draw
on non-consequentialist ethical argument.
of a potential sentience bias for moral trade-off situations particularly intractable is
the fact that it is an open question whether agent type should or should not count as a
salient aspect of the decision-making situation (see section 5.2.1).

--- Page 8 ---

FAccT ’25, June 23–26, 2025, Athens, Greece
Markus Kneer and Juri Viehoff
1. Human relationships: The only difference between the
scenarios is that in one there is a human that acts as a moral
agent and in the other one it is an AI agent. Could this, pure
and simple, be a sufficient moral reason to attribute a differ-
ence in how they should act? A notable fact about human
beings is that they can form relationships with one another:
how they behave and treat each other has some expressive
value for the way in which they form patterns of historical
and future-directed interaction. Human relationships admit
of patterns of hierarchy/subordination and other genuinely
interpersonal phenomena. None of these exist, or at least ex-
ist to the same degree, between humans and artificial agents.
Could agent-type variance be explained morally in terms of
the difference that either maximizing efficiency or distribut-
ing fairness makes to how people relate to each other? The
difficulty with this otherwise plausible first attempt to estab-
lish a moral difference between the cases is the following:
worries about the relational/expressive should make consid-
erations of fairness more salient where relationships could
be affected, that is, in the human decision-maker scenario.
But the agent-type value fork we report points in the other
direction because fairness is deemed more important in the
scenario where interpersonal relationships are not at stake.
2. The ‘micro/macro’ context hypothesis:
Some non-
consequentialists think that we can draw a justifiable differ-
ence between micro and macro contexts of moral decision-
making [46]. Micro contexts concern individual moral situa-
tions where non-institutional agents must make decisions
‘here and now’. By contrast, ‘macro’ ethics concerns choices
about what policies we should adopt (say in relation to
healthcare prioritization and rationing) at the societal level.
Now if one grants that these contexts can make a moral dif-
ference, then one possible explanation of why participants
judged the fairness/efficiency trade-off differently when the
only variation was in agent-type could be an implicit associ-
ation of one of these agent types with one of these contexts.
For example: the choice by an autonomous AI could be seen
to represent more of a ‘general policy’ that will be enacted
across many different individual choice situations whereas
the individual choice by a human agent is ‘micro’ in the sense
that it does not amount to taking a stance to whether there
should be a ‘macro’ level policy (and what that policy should
be). Such an inference may not be unreasonable given that
the algorithm is likely to act in the exact same way each time,
whereas we could hypothesize more pronounced freedom
to act differently to the human agent.
3. The moral judgment/transparency hypothesis: A third
conjecture turns on the comparative difficulty of making the
relevant judgments for each of the options in the complex
moral trade-off decision. Very roughly, it seems plausible
to assume that, once one accepts that some utilities can be
irrelevant (in the sense of not mattering for what we should
do when much more important harms are in play), the rel-
evant calculation becomes a more intricate exercise than
the straightforward equalizing of chances across affected
individuals. Now if it is reasonable to believe that human
beings continue to be more capable and morally knowledge-
able about drawing difficult moral distinctions, then perhaps
those subject to such decisions have good reason to prefer
that difficult tasks are performed by a human person. And
conversely, they may harbor doubts as to whether the AI
algorithm can have sufficient moral understanding to engage
in the relevant moral reasoning about the potential moral
‘irrelevance’ of different harms and benefits.
Unfortunately, we lack space to comprehensively discuss these
and other hypotheses (e.g. might subjects fear that the AI system
could be biased and therefore prefer a solution that is more easily
verifiable/more transparent?) about whether the reported empirical
difference in moral cognition can be supported by genuine moral
reasons. Of course, the fallback option is that agent type, from a
moral point of view, simply does not make a difference. This would
not yet constitute any reason to ignore the findings, or the pressing
agenda of further inquiry into human/AI alignment asymmetries.
But it would suggest that the reported findings constitute a kind of
sentience bias.
6
Limitations and Future Research
To properly situate our findings, we note some important limi-
tations: As regards the empirical part of our project, we would
like to highlight, first, the data here reported was collected for US
Americans, and one must refrain from generalizing to other lan-
guages and cultures, in particular non-WEIRD (Western, Educated,
Industrialized, Rich and Democratic) ones [37]. As in other areas of
experimental philosophy, psychology, and cognitive science, repli-
cations with subjects from different cultures are key to drawing
more general conclusions about human moral and cognitive dis-
positions. Second, in this paper, which principally aims to start a
debate on value forks and alignment, the number of vignettes is
limited, and so is the number of domains of AI applications covered.
In principle it is possible (though unlikely) that the scenarios we
identified are the only ones in which agent-type value forks occur.
In closing, we want to highlight the clear need for further ex-
ploration of this topic. Our empirical findings are intended to
serve but as a conversation starter, a conversation that seems both
timely and urgent given the extraordinary pace with which AI is
adopted in the capacity of decision-maker in high-stakes contexts.
As we are amongst the first to report value forks in relation to
choice-worthiness and permissibility, much remains to be done. In
particular, we want to highlight the following areas where future
research seems necessary:
First, more extensive studies, including alternative moral trade-
off situations, should be analyzed for whether or not agent-type
value forks occur. Other features of a non-consequentialist moral
outlook, e.g. scenarios involving doing vs. allowing or using other
agents as a means in dilemmatic scenarios, seem like natural candi-
dates to further investigate value forks. Investigating a multitude
of scenarios, and a broad range of contexts of high and low-stakes
applications of AI systems, could also help to settle which of the pro-
posed normative explanations is most likely on people’s mind. Dif-
ferent specifications of the AI system (for instance varying model-
complexity and capacities), as well as different descriptions of those

--- Page 9 ---

The Hard Problem of AI Alignment:
Value Forks in Moral Judgment
FAccT ’25, June 23–26, 2025, Athens, Greece
systems, might also have an impact on the results and should be
explored.
Second, in future work it would be helpful to explicitly quantify
the perceived marginal utility across the different domains covered
by the scenarios. This could also be done within-subjects, which
would enable the explicit quantification of the scenario as a factor.
Third, a broader variety of dependent variables should further
probe potential explanations of the findings reported. For instance,
the nexus between different types of moral assessment, e.g. prospec-
tive (permissibility and choice-worthiness) vs. retrospective judg-
ments (wrongness and blameworthiness), seems underexplored
given how some of the existing findings diverge from the data we
report.
Finally, fourth, further theoretical and philosophical work on the
underlying moral reasons to which one could appeal to endorse
or debunk value forks is called for. In the plausible high-stakes
scenarios we sketched, real people’s fundamental wellbeing will
be affected by whether we program algorithms to perform actions
that we would not deem permissible for a human decision-maker.
Whether we align AI subject to value forks could have significant
effects on who gets harmed and who does not. No matter how we
align our AI Systems, we owe it to those who stand to suffer that
we have a sound justification for or against the implementation of
value forks.
7
Conclusion
By aid of two experiments (N=1029), we have shown that for a
significant proportion of participants, agent-type (AI vs. Human)
makes a moral difference to the overall choice-worthiness of a
course of action in complex moral trade-off situations. This finding,
which we labelled the (agent-type) value fork, could have significant
repercussions for both theoretical and practical issues pertaining
to AI value alignment, for it could entail that we should program
AI to perform actions that similarly-placed human agents would
not be permitted to perform. This is a surprising finding. In our
general discussion, we explored whether such a value fork can be
explained morally by reference to various aspects of non- conse-
quentialist moral theorizing. To do so, we sketched some possible
rationalizations of why people may include value forks in their
moral judgments when it comes to agent type, and we offered
some preliminary normative assessment of each of their theoretical
persuasiveness.
Acknowledgments
We would like to thank audiences at the University of Graz’s
IDea_Lab, the University of Utrecht and the University of Zurich
for their feedback. This work was partly supported by an FWF
grant (10.55776/PIN1966824) awarded to Markus Kneer.
References
[1] Rusul Abduljabbar, Hussein Dia, Sohani Liyanage, and Saeed Asadi Bagloee. 2019.
Applications of Artificial Intelligence in Transport: An Overview. Sustainability
11, 1 (January 2019), 189. https://doi.org/10.3390/su11010189
[2] Alekh Agarwal, Alina Beygelzimer, Miroslav Dudik, John Langford, and Hanna
Wallach. 2018. A Reductions Approach to Fair Classification. In Proceedings of the
35th International Conference on Machine Learning, July 03, 2018. PMLR, 60–69.
Retrieved January 23, 2024 from https://proceedings.mlr.press/v80/agarwal18a.
html
[3] Colin Allen, Iva Smit, and Wendell Wallach. 2005. Artificial Morality: Top-down,
Bottom-up, and Hybrid Approaches. Ethics Inf Technol 7, 3 (September 2005),
149–155. https://doi.org/10.1007/s10676-006-0004-4
[4] Ruopeng An, Jing Shen, Junjie Wang, and Yuyi Yang. 2024. A scoping review
of methodologies for applying artificial intelligence to physical activity in-
terventions. Journal of Sport and Health Science 13, 3 (May 2024), 428–441.
https://doi.org/10.1016/j.jshs.2023.09.010
[5] Reem Ayad and Jason E. Plaks. 2025. Attributions of intent and moral responsi-
bility to AI agents. Computers in Human Behavior: Artificial Humans 3, (March
2025), 100107. https://doi.org/10.1016/j.chbah.2024.100107
[6] Alice Baderin. 2017. Reflective Equilibrium: Individual or Public? Social Theory
and Practice 43, 1 (2017), 1–28.
[7] Richard A. Berk. 2021. Artificial Intelligence, Predictive Policing, and Risk Assess-
ment for Law Enforcement. Annual Review of Criminology 4, Volume 4, 2021 (Jan-
uary 2021), 209–237. https://doi.org/10.1146/annurev-criminol-051520-012342
[8] Lea Bourguignon and Milan Mossé. 2025. How to Count Sore Throats. Analysis
(2025).
[9] Dan W. Brock. 2018. Ethical Issues in the Use of Cost Effectiveness Analysis
for the Prioritisation of Health Care Resources. In The Ethics of Public Health,
Volumes I and II, Michael Freeman (ed.). Routledge, London. https://doi.org/10.
4324/9781315239927
[10] Dario Cecchini, Michael Pflanzer, and Veljko Dubljević. 2024. Aligning artificial
intelligence with moral intuitions: an intuitionist approach to the alignment
problem. AI Ethics (May 2024). https://doi.org/10.1007/s43681-024-00496-5
[11] José-Antonio Cervantes, Sonia López, Luis-Felipe Rodríguez, Salvador Cervantes,
Francisco Cervantes, and Félix Ramos. 2020. Artificial Moral Agents: A Survey
of the Current Status. Sci Eng Ethics 26, 2 (April 2020), 501–532. https://doi.org/
10.1007/s11948-019-00151-x
[12] Alexandra Chouldechova. 2017. Fair Prediction with Disparate Impact: A Study
of Bias in Recidivism Prediction Instruments. Big Data 5, 2 (June 2017), 153–163.
https://doi.org/10.1089/big.2016.0047
[13] J. F. Christensen and A. Gomila. 2012. Moral dilemmas in cognitive neuroscience
of moral decision-making: A principled review. Neuroscience & Biobehavioral
Reviews 36, 4 (April 2012), 1249–1264. https://doi.org/10.1016/j.neubiorev.2012.
02.008
[14] Laura J. Damschroder, Todd R. Roberts, Brian J. Zikmund-Fisher, and Peter A.
Ubel. 2007. Why People Refuse to Make Tradeoffs in Person Tradeoff Elicitations:
A Matter of Perspective? Med Decis Making 27, 3 (May 2007), 266–280. https:
//doi.org/10.1177/0272989X07300601
[15] John Danaher and Henrik Skaug Sætra. 2022. Technology and moral change:
the transformation of truth and trust. Ethics Inf Technol 24, 3 (August 2022), 35.
https://doi.org/10.1007/s10676-022-09661-y
[16] John Danaher and Henrik Skaug Sætra. 2023. Mechanisms of Techno-Moral
Change: A Taxonomy and Overview. Ethic Theory Moral Prac 26, 5 (November
2023), 763–784. https://doi.org/10.1007/s10677-023-10397-x
[17] Norman Daniels. 2008. Just health: meeting health needs fairly. Cambridge
University Press, Cambridge; New York.
[18] Norman Daniels. 2013. Reflective Equilibrium. Retrieved from http://plato.
stanford.edu/entries/reflective-equilibrium/
[19] Norman Daniels. 2016. Resource Allocation and Priority Setting. In Public Health
Ethics: Cases Spanning the Globe, Drue H. Barrett, Leonard W. Ortmann, Angus
Dawson, Carla Saenz, Andreas Reis and Gail Bolan (eds.). Springer, Dordrecht.
https://doi.org/10.1007/978-3-319-23847-0
[20] William Dieterich, Christina Mendoza, and Tim Brennan. 2016. COMPAS Risk
Scales: Demonstrating Accuracy Equity and Predictive Parity. (2016). Retrieved
January 23, 2024 from https://go.volarisgroup.com/rs/430-MBX-989/images/
ProPublica_Commentary_Final_070616.pdf
[21] Thomas Dratsch, Xue Chen, Mohammad Rezazade Mehrizi, Roman Kloeckner,
Aline Mähringer-Kunz, Michael Püsken, Bettina Baeßler, Stephanie Sauer, David
Maintz, and Daniel Pinto dos Santos. 2023. Automation Bias in Mammography:
The Impact of Artificial Intelligence BI-RADS Suggestions on Reader Performance.
Radiology 307, 4 (May 2023), e222176. https://doi.org/10.1148/radiol.222176
[22] David Edmonds. 2013. Would You Kill the Fat Man?: The Trolley Problem and
What Your Answer Tells Us about Right and Wrong. Princeton University Press.
https://doi.org/10.1515/9781400848386
[23] Linda Eggert. 2025. Autonomised harming. Philos Stud 182, 1 (January 2025),
1–24. https://doi.org/10.1007/s11098-023-01990-y
[24] Virginia Eubanks. 2019. Automating Inequality: How High-Tech Tools Profile,
Police, and Punish the Poor. Picador, New York.
[25] Philippa Foot. 1967. The Problem of Abortion and the Doctrine of the Double
Effect. Oxford Review 5, (1967), 5–15.
[26] Lisa Katharina Frisch, Markus Kneer, Joachim Israel Krueger, and Johannes Ull-
rich. 2021. The effect of outcome severity on moral judgement and interpersonal
goals of perpetrators, victims, and bystanders. Euro J Social Psych 51, 7 (December
2021), 1158–1171. https://doi.org/10.1002/ejsp.2805
[27] Iason Gabriel. 2020. Artificial Intelligence, Values, and Alignment. Minds &
Machines 30, 3 (September 2020), 411–437. https://doi.org/10.1007/s11023-020-
09539-2

--- Page 10 ---

FAccT ’25, June 23–26, 2025, Athens, Greece
Markus Kneer and Juri Viehoff
[28] Iason Gabriel and Vafa Ghazavi. 2024. The Challenge of Value Alignment: From
Fairer Algorithms to AI Safety. In The Oxford Handbook of Digital Ethics, Carissa
Veliz (ed.). 336–355.
[29] Joshua Gert. 2013. Overridingness, Moral. In The International Encyclopedia of
Ethics. John Wiley & Sons, Ltd. https://doi.org/10.1002/9781444367072.wbiee010
[30] Kate Goddard, Abdul Roudsari, and Jeremy C Wyatt. 2012. Automation bias:
a systematic review of frequency, effect mediators, and mitigators. Journal of
the American Medical Informatics Association 19, 1 (January 2012), 121–127.
https://doi.org/10.1136/amiajnl-2011-000089
[31] Joshua D. Greene. 2016. Solving the Trolley Problem. In A Companion to Exper-
imental Philosophy. John Wiley & Sons, Ltd, 173–189. https://doi.org/10.1002/
9781118661666.ch11
[32] Joshua Greene and Jonathan Haidt. 2002. How (and where) does moral judgment
work? Trends in Cognitive Sciences 6, 12 (December 2002), 517–523. https:
//doi.org/10.1016/S1364-6613(02)02011-9
[33] Ulrike Hahn and Adam J. L. Harris. 2014. Chapter Two - What Does It Mean to
be Biased: Motivated Reasoning and Rationality. In Psychology of Learning and
Motivation, Brian H. Ross (ed.). Academic Press, 41–102. https://doi.org/10.1016/
B978-0-12-800283-4.00002-2
[34] Moritz Hardt, Eric Price, Eric Price, and Nati Srebro. 2016. Equality of Opportunity
in Supervised Learning. In Advances in Neural Information Processing Systems,
2016. Curran Associates, Inc. Retrieved January 23, 2024 from https://proceedings.
neurips.cc/paper/2016/hash/9d2682367c3935defcb1f9e247a97c0d-Abstract.html
[35] Brian Hedden. 2021. On statistical criteria of algorithmic fairness. Philosophy &
Public Affairs 49, 2 (2021), 209–231. https://doi.org/10.1111/papa.12189
[36] Deborah Hellman. 2020. Measuring Algorithmic Fairness. Virginia Law Review
106, 4 (2020), 811–866.
[37] Joseph Henrich, Steven J. Heine, and Ara Norenzayan. 2010. The weirdest people
in the world? Behavioral and Brain Sciences 33, 2–3 (June 2010), 61–83. https:
//doi.org/10.1017/S0140525X0999152X
[38] Wayne Holmes and Ilkka Tuomi. 2022. State of the art and practice in AI in
education. European Journal of Education 57, 4 (2022), 542–570. https://doi.org/
10.1111/ejed.12533
[39] Joo-Wha Hong, Yunwen Wang, and Paulina Lanz. 2020. Why Is Artificial In-
telligence Blamed More? Analysis of Faulting Artificial Intelligence for Self-
Driving Car Accidents in Experimental Settings. International Journal of Human–
Computer Interaction 36, 18 (November 2020), 1768–1774. https://doi.org/10.1080/
10447318.2020.1785693
[40] Joo-Wha Hong and Dmitri Williams. 2019. Racism, responsibility and autonomy
in HCI: Testing perceptions of an AI agent. Computers in Human Behavior 100,
(November 2019), 79–84. https://doi.org/10.1016/j.chb.2019.06.012
[41] Jeroen Hopster. 2021. What are socially disruptive technologies? Technology
in Society 67, (November 2021), 101750. https://doi.org/10.1016/j.techsoc.2021.
101750
[42] James Johnson. 2019. Artificial intelligence & future warfare: implications for
international security. Defense & Security Analysis 35, 2 (April 2019), 147–169.
https://doi.org/10.1080/14751798.2019.1600800
[43] Guy Kahane. 2015. Sidetracked by trolleys: Why sacrificial moral dilemmas
tell us little (or nothing) about utilitarian judgment. Social Neuroscience 10, 5
(September 2015), 551–560. https://doi.org/10.1080/17470919.2015.1023400
[44] Guy Kahane, Jim A. C. Everett, Brian D. Earp, Lucius Caviola, Nadira S. Faber,
Molly J. Crockett, and Julian Savulescu. 2018. Beyond sacrificial harm: A two-
dimensional model of utilitarian psychology. Psychological Review 125, 2 (2018),
131–164. https://doi.org/10.1037/rev0000093
[45] F. M. Kamm. 1993. Morality, Mortality: Volume 1: Death & Whom to Save from
It (Revised. ed.). Oxford University Press, Oxford.
[46] F. M. Kamm. 2015. Bioethical Prescriptions. J Med Ethics 41, 6 (January 2015),
493–495.
[47] F. M. Kamm. 2019. The Trolley Problem Mysteries. Oxford University Press, New
York, NY.
[48] Francis Kamm. 2015. Cost Effectiveness Analysis and Fairness. Journal of Practical
Ethics 3, 1 (2015).
[49] Julia Angwin Kirchner Jeff Larson, Surya Mattu, Lauren. 2022. Machine Bias *. In
Ethics of Data and Analytics. Auerbach Publications.
[50] Jon Kleinberg, Sendhil Mullainathan, and Manish Raghavan. 2016. Inherent
Trade-Offs in the Fair Determination of Risk Scores. https://doi.org/10.48550/
arXiv.1609.05807
[51] Markus Kneer. 2021. Can a Robot Lie? Exploring the Folk Concept of Lying as
Applied to Artificial Agents. Cognitive Science 45, 10 (October 2021), e13032.
https://doi.org/10.1111/cogs.13032
[52] Markus Kneer and Markus Christen. 2024. Responsibility Gaps and Retributive
Dispositions: Evidence from the US, Japan and Germany. Science and Engineering
Ethics 30, (2024).
[53] Markus Kneer and Michael T. Stuart. 2021. Playing the Blame Game with Robots.
In Companion of the 2021 ACM/IEEE International Conference on Human-Robot
Interaction (HRI ’21 Companion), März 2021. Association for Computing Ma-
chinery, New York, NY, USA, 407–411. https://doi.org/10.1145/3434074.3447202
[54] Markus Kneer and Juri Viehoff. 2023. Are there Irrelevant Utilities? What the
Folk Think (and Why This is Relevant). Proceedings of the Annual Meeting of
the Cognitive Science Society 45, 45 (2023). Retrieved January 19, 2024 from
https://escholarship.org/uc/item/66m3w8x7
[55] Markus Kneer and Juri Viehoff. 2025. Partial Aggregation: What the People Think.
Australasian Journal of Philosophy forthcoming (2025).
[56] Takanori Komatsu, Bertram F. Malle, and Matthias Scheutz. 2021. Blaming the
Reluctant Robot: Parallel Blame Judgments for Robots in Moral Dilemmas across
U.S. and Japan. In Proceedings of the 2021 ACM/IEEE International Conference
on Human-Robot Interaction (HRI ’21), März 2021. Association for Computing
Machinery, New York, NY, USA, 63–72. https://doi.org/10.1145/3434073.3444672
[57] Peng Liu, Yueying Chu, Siming Zhai, Tingru Zhang, and Edmond Awad. 2025.
Morality on the road: Should machine drivers be more utilitarian than human dri-
vers? Cognition 254, (January 2025), 106011. https://doi.org/10.1016/j.cognition.
2024.106011
[58] Veronika Luptakova and Alex Voorhoeve. 2023. How Do People Balance Death
against Lesser Burdens? In Advances in Experimental Political Philosophy,
Michael Landauer (ed.). Bloomsbury, London.
[59] Bertram F. Malle, Steve Guglielmo, and Andrew E. Monroe. 2014. A Theory of
Blame. Psychological Inquiry 25, 2 (April 2014), 147–186. https://doi.org/10.1080/
1047840X.2014.877340
[60] Bertram F. Malle, Matthias Scheutz, Thomas Arnold, John Voiklis, and Corey
Cusimano. 2015. Sacrifice One For the Good of Many? People Apply Different
Moral Norms to Human and Robot Agents. In Proceedings of the Tenth Annual
ACM/IEEE International Conference on Human-Robot Interaction (HRI ’15),
März 2015. Association for Computing Machinery, New York, NY, USA, 117–124.
https://doi.org/10.1145/2696454.2696458
[61] Bertram F. Malle, Matthias Scheutz, Corey Cusimano, John Voiklis, Takanori
Komatsu, Stuti Thapa, and Salomi Aladia. 2025. People’s judgments of humans
and robots in a classic moral dilemma. Cognition 254, (January 2025), 105958.
https://doi.org/10.1016/j.cognition.2024.105958
[62] Bertram F. Malle, Matthias Scheutz, Jodi Forlizzi, and John Voiklis. 2016. Which
robot am I thinking about? The impact of action and appearance on people’s
evaluations of a moral robot. In 2016 11th ACM/IEEE International Conference
on Human-Robot Interaction (HRI), March 2016. 125–132. https://doi.org/10.1109/
HRI.2016.7451743
[63] Serena Marchesi, Davide Ghiglino, Francesca Ciardo, Jairo Perez-Osorio, Ebru
Baykara, and Agnieszka Wykowska. 2019. Do we adopt the intentional stance
toward humanoid robots? Frontiers in psychology 10, (2019), 450.
[64] Elzė Sigutė Mikalonytė and Markus Kneer. 2022. Can Artificial Intelligence Make
Art?: Folk Intuitions as to whether AI-driven Robots Can Be Viewed as Artists
and Produce Art. ACM Transactions on Human-Robot Interaction THRI 11, 4
(September 2022), 43:1-43:19. https://doi.org/10.1145/3530875
[65] Dana Kay Nelkin, Craig R. M. McKenzie, Samuel C. Rickless, and Arseny A.
Ryazanov. 2023. Trolley Problems Reimagined: Sensitivity to Ratio, Risk, and
Comparisons. In Experiments in Moral and Political Philosophy, Hugo Viciana,
Antonio Gaitan and Fernando Aguiar (eds.). Routledge, New York.
[66] Alastair Norcross. 1997. Comparing Harms: Headaches and Human Lives. Phi-
losophy & Public Affairs 26, 2 (1997), 135–167.
[67] Cathy O’Neil. 2016. Weapons of Math Destruction: How Big Data Increases
Inequality and Threatens Democracy. Penguin Random House, New York.
[68] Michael Otsuka. 2024. Equal Chances versus Equal Outcomes: When Are Lotteries
Fair and Justified? Political Philosophy 1, 2 (August 2024). https://doi.org/10.
16995/pp.16917
[69] Maria Perez-Ortiz, Claire Dormann, Yvonne Rogers, Sahan Bulathwela, Stefan
Kreitmayer, Emine Yilmaz, Richard Noss, and John Shawe-Taylor. 2021. X5Learn:
A Personalised Learning Companion at the Intersection of AI and HCI. In 26th
International Conference on Intelligent User Interfaces - Companion (IUI ’21
Companion), April 14, 2021. Association for Computing Machinery, New York,
NY, USA, 70–74. https://doi.org/10.1145/3397482.3450721
[70] John Rawls. 1971. A theory of justice. Belknap Press of Harvard University Press,
Cambridge, Mass.,.
[71] Arseny A. Ryazanov, Shawn Tinghao Wang, Dana Kay Nelkin, Craig R. M. McKen-
zie, and Samuel C. Rickless. 2023. Beyond killing one to save five: Sensitivity to
ratio and probability in moral judgment. Journal of Experimental Social Psychol-
ogy 108, (September 2023), 104499. https://doi.org/10.1016/j.jesp.2023.104499
[72] Katharine Sanderson. 2023. AI science search engines are exploding in number —
are they any good? Nature 616, 7958 (April 2023), 639–640. https://doi.org/10.
1038/d41586-023-01273-w
[73] Filippo Santoni De Sio and Giulio Mecacci. 2021. Four Responsibility Gaps with Ar-
tificial Intelligence: Why they Matter and How to Address them. Philos. Technol.
34, 4 (December 2021), 1057–1084. https://doi.org/10.1007/s13347-021-00450-x
[74] Julian Savulescu, Christopher Gyngell, and Guy Kahane. 2021. Collective Re-
flective Equilibrium in Practice (CREP) and controversial novel technologies.
Bioethics 35, 7 (2021), 652–663. https://doi.org/10.1111/bioe.12869
[75] T. M. Scanlon. 2018. Why Does Inequality Matter? Oxford University Press, New
York, NY.
[76] Matthias Scheutz and Bertram F. Malle. 2020. May Machines take Lives to Save
Lives? Human Perceptions of Autonomous Robots (with the Capacity to Kill).

--- Page 11 ---

The Hard Problem of AI Alignment:
Value Forks in Moral Judgment
FAccT ’25, June 23–26, 2025, Athens, Greece
In Lethal Autonomous Weapons: Re-Examining the Law and Ethics of Robotic
Warfare, Jai Galliott, Duncan MacIntosh and Jens David Ohlin (eds.). Oxford
University Press.
[77] Silvana Secinaro, Davide Calandra, Aurelio Secinaro, Vivek Muthurangu, and
Paolo Biancone. 2021. The role of artificial intelligence in healthcare: a structured
literature review. BMC Med Inform Decis Mak 21, 1 (April 2021), 125. https:
//doi.org/10.1186/s12911-021-01488-9
[78] Avner de Shalit. 2020. Political Philosophy and What People Think. Australasian
Philosophical Review 4, 1 (January 2020), 4–22. https://doi.org/10.1080/24740500.
2021.1876411
[79] Daniel B. Shank and Alyssa DeSanti. 2018. Attributions of morality and mind
to artificial intelligence after real-world moral violations. Computers in human
behavior 86, (2018), 401–411.
[80] Daniel B. Shank, Christopher Graves, Alexander Gott, Patrick Gamez, and Sophia
Rodriguez. 2019. Feeling our way to machine minds: People’s emotions when
perceiving mind in artificial intelligence. Computers in Human Behavior 98,
(2019), 256–266.
[81] Xia Song, Shiqi Yang, Ziqing Huang, and Tao Huang. 2019. The Application of
Artificial Intelligence in Electronic Commerce. J. Phys.: Conf. Ser. 1302, 3 (August
2019), 032030. https://doi.org/10.1088/1742-6596/1302/3/032030
[82] Stefan Strauß. 2021. Deep Automation Bias: How to Tackle a Wicked Problem of
AI? Big Data and Cognitive Computing 5, 2 (June 2021), 18. https://doi.org/10.
3390/bdcc5020018
[83] Victor Tadros. 2016. Wrongs and crimes. Oxford University Press.
[84] Victor Tadros. 2019. Localized Restricted Aggregation. In Oxford Studies in
Political Philosophy, David Sobel, Peter Vallentyne and Steven Wall (eds.). Oxford
University Press, New York.
[85] Judith Jarvis Thomson. 1984. The Trolley Problem Comment. Yale L. J. 94, 6 (1985
1984), 1395–1415.
[86] Suzanne Tolmeijer, Markus Kneer, Cristina Sarasua, Markus Christen, and Abra-
ham Bernstein. 2021. Implementations in Machine Ethics: A Survey. ACM Com-
put. Surv. 53, 6 (Dezember 2021), 132:1-132:38. https://doi.org/10.1145/3419633
[87] Peter A. Ubel, George Loewenstein, Dennis Scanlon, and Mark Kamlet. 1996. In-
dividual Utilities Are Inconsistent with Rationing Choices: A Partial Explanation
of Why Oregon’s Cost-Effectiveness List Failed. Med Decis Making 16, 2 (June
1996), 108–116. https://doi.org/10.1177/0272989X9601600202
[88] Steven Umbrello and Ibo van de Poel. 2021. Mapping value sensitive design
onto AI for social good principles. AI Ethics 1, 3 (August 2021), 283–296. https:
//doi.org/10.1007/s43681-021-00038-3
[89] Daniel Viehoff. 2022. Legitimate Injustice and Acting for Others. Philosophy &
Public Affairs 32, 1 (2022). https://doi.org/10.1111/papa.12218
[90] John Voiklis, Boyoung Kim, Corey Cusimano, and Bertram F. Malle. 2016. Moral
judgments of human vs. robot agents. In 2016 25th IEEE International Sympo-
sium on Robot and Human Interactive Communication (RO-MAN), August 2016.
775–780. https://doi.org/10.1109/ROMAN.2016.7745207
[91] Alex Voorhoeve. 2014. How Should We Aggregate Competing Claims? Ethics
125, 1 (October 2014), 64–87.
[92] Alex Voorhoeve. 2018. Balancing small against large burdens. Behavioural Public
Policy 2, 1 (May 2018), 125–142. https://doi.org/10.1017/bpp.2017.4
[93] Wendell Wallach and Colin Allen. 2008. Moral Machines: Teaching Robots Right
from Wrong. Oxford University Press.
[94] Laura Weidinger, Kevin R. McKee, Richard Everett, Saffron Huang, Tina O. Zhu,
Martin J. Chadwick, Christopher Summerfield, and Iason Gabriel. 2023. Using
the Veil of Ignorance to align AI systems with principles of justice. Proceedings
of the National Academy of Sciences 120, 18 (May 2023), e2213709120. https:
//doi.org/10.1073/pnas.2213709120
[95] Pascale Willemsen, Albert Newen, and Kai Kaspar. 2018. A new look at the
attribution of moral responsibility: The underestimated relevance of social roles.
Philosophical Psychology 31, 4 (May 2018), 595–608. https://doi.org/10.1080/
09515089.2018.1429592
[96] Pascale Willemsen, Albert Newen, Karolina Prochownik, and Kai Kaspar. 2023.
With great(er) power comes great(er) responsibility: an intercultural investigation
of the effect of social roles on moral responsibility attribution. Philosophical
Psychology (May 2023), 1–27. https://doi.org/10.1080/09515089.2023.2213277
[97] Yuyan Zhang, Jiahua Wu, Feng Yu, and Liying Xu. 2023. Moral Judgments of
Human vs. AI Agents in Moral Dilemmas. Behavioral Sciences 13, 2 (2023), 181.

```
