---
title: "2024-Kader-The Emergence of Strategic Reasoning of Large Language Models - PDF Extract"
source_pdf: "2024-Kader-The Emergence of Strategic Reasoning of Large Language Models.pdf"
pages: 58
extracted_at: "2026-02-07T17:00:46.842118"
---

# PDF Extract: 2024-Kader-The Emergence of Strategic Reasoning of Large Language Models

**Source PDF:** 2024-Kader-The Emergence of Strategic Reasoning of Large Language Models.pdf
**Total Pages:** 58

---

## Content

```
--- Page 1 ---

The Emergence of Strategic Reasoning of Large Language
Models∗
Gavin Kader†
Dongwoo Lee‡
October 23, 2025
Abstract
As large language models (LLMs) have demonstrated strong reasoning abilities in struc-
tured tasks (e.g., coding and mathematics), we explore whether these abilities extend to
strategic multi-agent environments. We investigate strategic reasoning capabilities – the
process of choosing an optimal course of action by predicting and adapting to others’
actions – of LLMs by analyzing their performance in three classical games from behav-
ioral economics.
Using hierarchical models of bounded rationality, we evaluate three
standard LLMs (ChatGPT-4, Claude-3.5-Sonnet, Gemini 1.5) and three reasoning LLMs
(OpenAI-o1, Claude-4-Sonnet-Thinking, Gemini Flash Thinking 2.0). Our results show
that reasoning LLMs exhibit superior strategic reasoning compared to standard LLMs
(which do not demonstrate substantial capabilities) and often match or exceed human
performance; this represents the first and thus most fundamental transition in strategic
reasoning capabilities documented in LLMs. Since strategic reasoning is fundamental to
future AI systems (including Agentic AI), our findings demonstrate the importance of
dedicated reasoning capabilities in achieving effective strategic reasoning.
Keywords: Strategic Reasoning, Large Language Models, Level-k Model, Cognitive
Hierarchy Model
∗We are grateful to Soumen Banerjee and Syngjoo Choi for their valuable comments and suggestions. We
also thank the participants at the 11th Annual Behavioural Game Theory Workshop (held online) at University
of East Anglia.
†Southwestern University of Finance and Economics. E-mail: gav.kader@outlook.com
‡(Corresponding author) Southwestern University of Finance and Economics. E-mail: dwlee05@gmail.com
1
arXiv:2412.13013v4  [econ.GN]  22 Oct 2025

--- Page 2 ---

1
Introduction
As the reliance on Large Language Models (LLMs) is now pervasive, it is vital to assess
whether the mechanisms through which LLMs reason are also capable of strategic reasoning
– the process of choosing an optimal course of action by predicting and adapting to the
actions of others in multi-agent environments. While research has shown LLMs’ reasoning
skills in individual decision-making (economic rationality) (Chen et al., 2023; Kim et al.,
2024), mathematics (Ahn et al., 2024; Zhou et al., 2024), simple reasoning problems (Webb,
Holyoak and Lu, 2023; Hagendorff, Fabi and Kosinski, 2023), and coding tasks (OpenAI, 2024;
Anthropic, 2024), this does not inherently imply they possess strategic reasoning capabilities.
In fact, strategic reasoning is an emergent capability virtually absent in standard LLMs, only
manifesting with the advent of reasoning LLMs, representing the most fundamental and
sharpest transition in strategic reasoning capabilities since the development of LLMs.1
Such capabilities are crucial for the increasingly popular use of Agentic AI (AAI), which
involves multi-agent decision-making environments with AI/LLM systems having competitive
or cooperative objectives that require constant anticipation and adaptation for autonomous,
real-time tasks. Key real-world applications of AAI include autonomous financial agents that
anticipate market movements to make trading decisions (Luo and Duan, 2025; An et al.,
2024), supply chain systems that coordinate resources by predicting demand (Almutairi and
Kim, 2025; Xu et al., 2024), and negotiation systems requiring agents to infer and strategically
anticipate responses (Abdelnabi et al., 2024; Kwon et al., 2024). Unlike individual decision-
making, these types of applications require agents to form beliefs about how others (LLMs
and/or people) will act in order to complete tasks.2 The strategic sophistication of these
AI agents therefore has consequences for human decision-makers. As people increasingly use
LLMs for strategic advice (negotiations, investments, etc.), more sophisticated LLMs may
provide better outputs for improved decision-making in strategic contexts. From a market
perspective, variations in strategic sophistication across LLMs create potential asymmetries
where users of less sophisticated LLMs may be exploitable by those employing more strate-
gically sophisticated systems. Thus, investigating the strategic sophistication of LLMs has
broader implications beyond benchmarking model performance.
In this study, our objective is to explore this emergence of strategic reasoning capabilities
1While earlier standard LLMs trained before the first reasoning LLMs demonstrate a lack of inherent
strategic reasoning, standard LLMs developed later are not incapable of strategic reasoning. After the in-
troduction of reasoning LLMs, standard LLMs are likely to be exposed to more reasoning-based thinking
and tasks (or even fine-tuned or undergone a form of knowledge distillation from reasoning LLMs) allowing
standard LLMs to develop higher-order strategic reasoning in a way that is crudely analogous to reasoning
LLMs.
2More generally, achieving Artificial General Intelligence (AGI) - AI that performs a wide range of cognitive
tasks at, or beyond, human-level proficiency (Singh et al., 2024) - necessitates systems capable of strategic
reasoning, making it essential to benchmark these capabilities (Mumuni and Mumuni, 2025).
1

--- Page 3 ---

(Wei et al., 2022; Schaeffer, Miranda and Koyejo, 2023) leveraging OpenAI’s ChatGPT-4 and
OpenAI-o1-preview (GPT-4, GPT-o1), Anthropic’s Claude-3.5-Sonnet and Claude-4-Sonnet-
Thinking (Cl-3S, Cl-4ST), and Google’s Gemini 1.5 Flash and Gemini Flash Thinking 2.0
Experimental (Ge-1.5, Ge-2T). We investigate whether reasoning LLMs, specifically designed
with reasoning techniques (GPT-o1, Cl-4ST, and Ge-2T) exhibit sophisticated strategic rea-
soning abilities, and whether such abilities were already present in more standard LLMs.
To evaluate and deepen our understanding of LLMs’ strategic reasoning, we adopt a behav-
ioral economics framework – a ubiquitous approach in studying human behavior – to provide
valuable insights into how well LLMs can navigate strategic environments.
We explore strategic reasoning using three classical games from the behavioral economics
literature: the p-Beauty Contest Game (pBCG), the Guessing Game (GG), and the 11-20
Money Request Game (MRG) (Nagel, 1995b; Costa-Gomes and Crawford, 2006; Arad and Ru-
binstein, 2012, respectively), allowing us to evaluate LLMs by estimating their depth of strate-
gic reasoning and investigate whether we observe similarities/differences across games.3,4
These games span distinct theoretical demands. In the pBCG, iterated best-response rea-
soning leads to a unique symmetric equilibrium, so equilibrium actions are identical between
players. By contrast, the GG features role-specific incentives and yields asymmetric equilib-
rium actions between players. Finally, the MRG requires probabilistic reasoning: an equi-
librium is a randomization of actions rather than a single deterministic action for players.
Using such games provides us with essential tools to evaluate LLMs, as the focus is on logic
and strategic reasoning through clear, well-defined rules and, vitally, action spaces that allow
us to directly test the depth of strategic reasoning abilities.
Two of the most profound models from behavioral economics that capture the recursive
process involved in limited strategic sophistication are the level-k model (Stahl and Wilson,
1994, 1995; Nagel, 1995b) and the cognitive hierarchy (CH) model (Camerer, Ho and Chong,
2004).5
These alternative models of bounded rationality have been able to provide more
accurate predictions of behavior. Studies in behavioral economics have largely focused on
human adults with some research done with children (Brocas and Carrillo, 2020; Hermes and
Schunk, 2022; Crawford, Costa-Gomes and Iriberri, 2013). We apply both models to evaluate
LLMs by measuring their level of strategic reasoning represented by a hierarchy of iterated
reasoning – an investigation which is yet to be done with LLMs.
3In human subjects, Georganas, Healy and Weber (2015) show that strategic reasoning can differ across
games.
4Using behavioral games (dictator game, ultimatum game, trust game, bomb risk game, and public goods
game), Mei et al. (2024) show that LLMs exhibit behavioral traits such as trust, fairness, risk-aversion,
altruism, and cooperation, with responses that are statistically indistinguishable from human behavior.
5Abundant studies in behavioral economics have shown that the Nash equilibrium, derived from the
assumption of full rationality, does not match well with observed play (Camerer, Loewenstein and Rabin,
2004; Camerer, 2011; Bernheim, DellaVigna and Laibson, 2019). This has given rise to models of limited
strategic reasoning.
2

--- Page 4 ---

The lowest rank in the hierarchy, say rank-0, is completely non-strategic, that is, actions
are made without taking into account the actions of others.6 The next rank represents more
strategic behavior (rank-1) with beliefs that all others are non-strategic (rank-0). Similarly,
rank-2 beliefs are that all others consist of lower ranks. In the level-k model, these lower
ranks, referred to as levels, are always exactly one level lower of reasoning, e.g., level-2 (L2)
assumes that all others are level-1 (L1). In the CH model, these lower ranks, referred to as
steps, accommodate a combination of all lower steps of reasoning, e.g., step-2 assumes that
all others are a mixture of step-0 and step-1. As we move up the hierarchy, this pattern
continues for higher ranks. In this process, knowing how many stages of iterated reasoning
the others are utilizing (i.e., the others’ levels) is essential. In this way, we aim to answer to
what extent are LLMs strategically sophisticated.
To evaluate the strategic reasoning of LLMs, we instruct LLMs to play the different
games under various treatments. To obtain a distribution of responses from each LLM, we
request 100 responses, with each prompt being independent – akin to conducting a laboratory
experiment with 100 subjects. Additional treatments include varying the parameters of the
games themselves.7
By estimating the level-k model and the CH model, we are able to
determine the depth of reasoning (up to a fixed level/step) by matching the theoretical
predictions of each model for each game with the observed data. Our overall results are (i)
reasoning LLMs demonstrate higher strategic reasoning compared to standard LLMs, (ii) with
sufficient feedback, LLMs are able to learn and achieve higher orders of strategic reasoning
(especially standard LLMs), (iii) reasoning LLMs learn faster than standard LLMs, (iv)
standard LLMs consistently exhibited worse strategic reasoning than typical human subjects
(from the experimental economics literature), and naturally implying (v) reasoning LLMs
often exhibit higher strategic reasoning than human subjects (generally in favor of GPT-o1
over Cl-4ST and Ge-2T).
The enhanced reasoning techniques of the reasoning LLMs is the most likely explana-
tion for their higher strategic reasoning. Specifically, GPT-o1, Cl-4ST, and Ge-2T leverage
specialized large-scale reinforcement learning to enhance their reasoning skills, with chain-of-
thought reasoning – a process where the model tackles tasks step-by-step, approaching prob-
lems incrementally (Wei et al., 2023), which, in practice, means training LLMs to break down
complex tasks into smaller, manageable steps, mirroring human-like reasoning.8 With this
approach, reasoning LLMs refine their reasoning by exploring various strategies and recogniz-
6A common assumption is that rank-0 behavior is consistent with choosing an action as if drawing uni-
formly from the action space.
7The temperature parameter of LLMs can also influence output in terms of randomness and creativity.
We use a baseline temperature of 0.5 and also test a high (0.75) and low (0.25) temperature. Section B.5 of
Appendix B contains the results of the high and low temperatures with overarching takeaway that temperature
has little effect on observed strategic reasoning.
8As opposed to just prompting them to use chain-of-thought reasoning.
3

--- Page 5 ---

ing potential mistakes, further enhancing their problem-solving capabilities in an iterative,
and (seemingly) reflective process, ensuring more careful evaluation before responding.9
Using standard methodologies and models from behavioral economics, and experimental
economics, we are able to concretely evaluate the strategic reasoning capabilities of LLMs
using models of bounded rationality. We contribute to the ongoing interest in comparing
between LLMs as well as comparisons with human behavior. Further, we highlight that with
sufficient feedback, even LLMs which exhibited poor performance in one-shot games can refine
their strategies, which draws a parallel with human subjects (Nagel, 1995b; Ho, Camerer and
Weigelt, 1998; Weber, 2003) and the reasoning LLMs. By incorporating thinking/reasoning
skills into the mechanism through which LLMs operate, it gives a clear inherent indication
as to why reasoning LLMs perform vastly better than other LLMs and are capable of outper-
forming human subjects. Our study emphasizes the importance of continuous improvement
in these mechanisms, particularly for interactive tasks requiring higher-order reasoning.
2
p-Beauty Contest Game
We begin with an overview of the pBCG, examining its theoretical predictions from behavioral
game theory, which accounts for both full and bounded rationality. After briefly describing
how these models are estimated, we explain our approach to implementing the pBCG with
LLMs.
Game. A group of n ≥2 players simultaneously choose a number in the interval [0, 100].
The winner of the game is the player whose number is closest to a given target multiplier (p)
of the average number chosen by all players.
Theoretical Predictions. Nash equilibrium requires no player has an incentive to deviate
from a given strategy profile, assuming all other players’ strategies remain the same. The
equilibrium is based on the assumption of common knowledge of rationality that all players
are rational and that is known to all players.
In the pBCG with p < 1, a unique Nash
equilibrium is that all players choose 0 as no player gains by choosing another number when
all others choose 0. Similarly, in the pBCG with p > 1, a unique Nash equilibrium is that all
players choose 100.
Both in the level-k and the cognitive hierarchy (CH) models, it is assumed that players
are boundedly rational in the sense that each player deems their level/step of reasoning is
higher than that of others. Specifically, the level-k model assumes that a player believes
that all others are one level lower in their reasoning compared to themselves. The CH model
assumes that a player believes that the reasoning steps of the others are distributed (strictly)
below her own, according to a Poisson distribution. For both models, we use the concept of
9OpenAI-o1-preview is the first model of this type and therefore serves as an essential benchmark.
4

--- Page 6 ---

best guess which is a target number based on an average guess of numbers from other players
and the target multiplier (p).10
In the level-k model, the best guess for each reasoning level, denoted by lk for k = 0, 1, . . .,
is defined as:
l0 = 50,
l1 = l0 × p = 50p,
l2 = l1 × p = 50p2, . . . ,
lk = lk−1 × p = 50pk,
where an L0 type chooses l0 = 50, which is the average guess when choosing uniformly
at random from [0, 100]. A Lk type, k = 1, 2, . . ., believes that all other players are Lk−1,
choosing lk−1 = 50×pk−1. Clearly, lk converges to 0 and 100 for p < 1 and p > 1, respectively,
in the interval [0, 100] when the reasoning level k goes to infinity.
The CH model assumes that each player is playing against a distribution of players who
are using lower reasoning steps. This distribution is given by a Poisson distribution f(·; τ),
where τ is the mean (and the variance) of the number of reasoning steps. Specifically, a
step-k type believes that they are playing against a distribution of players with reasoning
steps from 0 to k −1. This distribution is given by fk(j; τ), j = 0, 1, . . . , k −1, such that
fk(j; τ) =
e−ττ j
j!
 .  k−1
X
m=0
e−ττ m
m!
!
,
(1)
where fk(j; τ) is the conditional probability for j = 0, 1, . . . , k −1.
The best guess for reasoning steps, denoted by sk for k = 1, 2, . . ., is defined as
sk =
k−1
X
j=0
fk(j; τ)sj,
where the average guess for step-0 is s0 = 50, that is, a random choice from the interval
[0, 100]. A step-k type believes that all others are step-0 to step-(k −1), according to the
Poisson probability density fk(j; τ). For example, with τ = 1.5, a step-2 player believes that
they are playing against a combination of step-0 and step-1 players, with the proportions of
each being 40% and 60%, respectively. Given these proportions, a step-2 player would choose
to play p times the expected response of the other players.
Estimation. From these theoretical predictions, we estimate the parameters for both the
level-k and CH models by maximum likelihood estimation (MLE). For the level-k model, we
estimate the proportions of responses corresponding to each level from L0, L1, L2, L3, L4,
10In game theory, the concept of a best response is often employed to derive an equilibrium – a set of
strategies that provide the most favorable outcome based on a belief about the strategies of others. In games
such as these in which a best response given a belief may not be uniquely defined, we use a best guess as
a reasonable best response, common to the behavioral economics literature, making it possible to identify a
level/step of reasoning.
5

--- Page 7 ---

and L∞(Nash) predictions. We assume that each response is a best guess with (independent
and identically distributed) noise.
Estimation of the level-k model gives the distribution
of responses according to the different levels of reasoning.
For example, if responses are
concentrated around the lower-level types’ guesses, compared to higher-level types’ guesses,
then overall responses from the former must exhibit less strategic reasoning than the latter.
The estimated level-k model will reflect this in estimating higher frequencies for the lower
levels of reasoning. Similarly for the CH model, we estimate the distribution of step-types
using a Poisson distribution (fully parameterized by τ), as defined above, with a similarly
defined noisy best guess based on the (conditional) distribution of lower step-types.
For
example, a higher/lower estimated τ is indicative of higher/lower level reasoning, on average,
as this indicates more/fewer (average) steps of reasoning.11 A detailed description of the
estimation for both models is provided in Section B.4.1 of Appendix B.
Instructing LLMs. To collect data, we use the respective application programming inter-
faces (API) with Python/R from OpenAI, Anthropic, and Google. The exact input prompts
for the understanding questions and the tasks are provided in Sections B.2 and B.3 of Ap-
pendix B.
2.1
Design
The baseline condition refers to a specific set of parameters of the pBCG.
Baseline condition: The total number of participants is 11 (n = 11), the target statistic
is the average, and the target proportion is 2/3 (p = 2/3). This represents a classical pBCG
with the most commonly used parameters in the literature. We ask each LLM to complete
the baseline pBCG 100 times, providing us with a distribution of responses.
Alternative conditions: To provide comparisons with the baseline condition, we change
one of the parameters while keeping the others fixed. LLM responses are collected for (i)
p ∈{1/2, 4/3}, (ii) n ∈{2, unspecified}, (iii) {median}. Varying these parameters does not
change the substance of the baseline pBCG, but offers additional insights into LLM strategic
reasoning.
Multiple rounds: We collect responses from a repeated version of the pBCG, with feedback,
conducted over 10 rounds, using the same parameters as the baseline condition (n = 11),
including p = {4/3}. Each of the LLMs play within a group of 10 other LLM subjects of
the same model. After each round, each player receives information about the average bid
11For example, in pBCG, a ˆτ = 0 implies that all players are step-0 types, whereas ˆτ →∞indicates
players are fully rational, as infinitely iterated elimination of dominated strategies leads to a unique Nash
equilibrium. A ˆτ = 1.5 indicates that the average step-type is 1.5. Further, as the frequency of types f(k)
is Poisson-distributed, the ratio f(k−1)
f(k−2) favors step-(k −1) types when τ is large, i.e., step-k types play as if
there are predominantly step-(k −1) type when τ is large.
6

--- Page 8 ---

and the target number (p×average). Additionally, players are privately informed of their win
(or loss) but not the identity of the winner nor the winning bid (following Ho, Camerer and
Weigelt (1998)). Players are provided with the cumulative history of the game from round 1
to 10 within their prompts.
2.2
Baseline Condition Results
Before proceeding with data collection, we conducted a series of preliminary checks involving
several questions for whether LLMs understand the game-specific rules and winning condi-
tions – and whether they choose a best response when given the actions of the other players
to confirm their ability to respond optimally. We asked each LLM to answer each question 25
times. Each LLM consistently answers all of the questions related to the rules of the game,
as well as when winning conditions were satisfied (or not) correctly. All LLMs also provided
appropriate answers for a best response in the baseline condition.
The reasoning LLMs are more strategically sophisticated than the standard LLMs by at
least 1 to 2 levels of thinking on average, with GPT-o1 exhibiting the highest level of strategic
reasoning overall, summarized in Figure 1.12 As is well known in the experimental economics
literature (see Nagel, 1995b; Bosch-Dom`enech et al., 2002, as representative examples), human
subjects are typically a combination of L0, L1, L2, and L∞, with L∞types being rare. To
draw direct comparisons with human subjects, we also do estimation using data from Nagel
(1995b) (different p’s), Grosskopf and Nagel (2008) (n = 2), Bosch-Dom`enech et al. (2002)
(n = unspecified), and Hermes and Schunk (2022) (median). From Figure 1, we observe that
the distribution of levels for GPT-o1, Cl-4ST, Ge-2T, and Cl-3S are shifted toward higher
levels of strategic reasoning compared to human subjects.
Overall, GPT-o1 and Cl-4ST
exhibit the highest levels of strategic reasoning by large margins.13
Table 1 shows estimates for τ alongside respective 95% confidence intervals.14 On average,
Ge-1 exhibits just under 1-step of strategic reasoning with estimates not dissimilar to human
subjects (see Table A1). GPT-o1, and Cl-4ST vastly outperformed the other LLMs, and
exhibit higher levels of strategic reasoning than human subjects, with GPT-o1 marginally
exhibiting the highest average steps of reasoning, corroborating with the estimates from the
level-k model.
12All non-zero proportions in Figure 1 are statistically significant at the 5% level with inference based on
randomized resampling (bootstrap).
13Using data from Nagel (1995a) (N = 67), we also conduct Kolmogorov-Smirnov (KS) tests for the
distribution of raw results. Results are summarized in Table A1. Focusing on those cases in which exactly
one of the one-sided tests is rejected, one-sided KS tests suggest that GPT-4, GPT-o1, Cl-4ST, and Ge-2T
outperform human subjects at any reasonable significance levels. Two-sided tests suggest the distributions
between LLMs and human subjects are all statistically different from each other at any reasonable significance
level. Data made available at (Nagel et al., 2002).
14Confidence intervals are estimated from randomized resampling (bootstrap). This is true for all tables
with estimates from the CH model in this paper.
7

--- Page 9 ---

n=2
n = Unspecified
Median
p=2/3 (baseline)
p=1/2
p=4/3
0.0
0.2
0.4
0.6
0.8
1.0
0.0
0.2
0.4
0.6
0.8
1.0
0.0
0.2
0.4
0.6
0.8
1.0
L∞
L4
L3
L2
L1
L0
L∞
L4
L3
L2
L1
L0
L∞
L4
L3
L2
L1
L0
L∞
L4
L3
L2
L1
L0
L∞
L4
L3
L2
L1
L0
L∞
L4
L3
L2
L1
L0
Average Proportions
Human Subjects
Gemini-2.0 Flash (Thinking)
Gemini-1.5 Flash
Claude-4 (Sonnet Thinking)
Claude-3.5 (Sonnet)
OpenAI-o1
ChatGPT-4
Figure 1: Estimates of the proportions of level-k types for the pBCG
2.3
Alternate Conditions Results
As with the baseline condition, we check whether LLMs understand the game (specific rules
& win condition, and best responses). All understanding questions were answered correctly
by each LLM.
From Figure 1, Ge-1 is consistent with their baseline estimates and the n = {unspecified}
condition but shows a lack of strategic reasoning in the remaining conditions, exhibiting
overall drops in strategic reasoning from baseline. Cl-3S only manages to stay at L2 for the
median condition with drops to combinations of L0/L1 and small proportions of L2 behavior.
Only GPT-o1 and (marginally) Ge-2T exhibit L∞behavior. This is particularly true when
n = {2}, where only GPT-o1 is virtually consistent with a fully rational player.15 Overall,
for all conditions except when p = {4/3}, only the reasoning LLMs exhibit significant L2+
15Increases in strategic reasoning are not surprising in this condition, given that the game is less complicated
when there are fewer players, but with dramatic/modest improvements for GPT-o1/Ge-2T.
8

--- Page 10 ---

p = 2/3
(baseline)
p = 1/2
p = 4/3
n = 2
n =
unspecified
Median
GPT-4
2.39
0.56
0.00
0.87
0.83
1.09
(2.23,2.46)
(0.56,0.79)
(0.00,0.00)
(0.79,0.94)
(0.69,1.01)
(0.83,1.36)
GPT-o1
4.42
2.52
0.95
7.09
3.43
4.00
(4.00,4.77)
(2.52,2.99)
(0.744,0.96)
(6.42,8.00)
(3.11,3.76)
(0.00,4.86)
Cl-3S
2.87
1.50
0.00
1.17
1.26
2.87
(2.87,2.87)
(1.31,1.57)
(0.00,0.00)
(1.12,1.24)
(1.18,1.34)
(2.65,2.88)
Cl-4ST
4.00
2.83
0.00
2.33
2.15
2.45
(0.00,4.23)
(2.70,2.99)
(0.00,0.00)
(2.24,2.42)
(2.10,2.21)
(2.39,2.54)
Ge-1
0.86
0.00
0.00
0.00
0.77
0.00
(0.79,0.91)
(0.00,0.00)
(0.00,0.00)
(0.00,0.00)
(0.70,0.84)
(0.00,0.00)
Ge-2T
2.46
2.12
0.00
1.86
2.22
2.46
(2.39,2.72)
(1.99,2.12)
(0.00,0.00)
(1.79,1.91)
(2.01,2.41)
(2.46,2.92)
Human Subjects
0.00
1.08
0.36
0.00
3.01
2.46
(0.00,1.09)
(0.00,2.14)
(0.00,0.57)
(0.00,0.00)
(2.91,3.12)
(0.00,2.46)
Table 1: Estimates of τ from the CH model for different pBCG parameters. 95% confidence
intervals (bootstrapped) are shown in parentheses.
behavior, although with Cl-4ST showing significant drops compared to baseline, and with
GPT-o1 exhibiting the highest overall strategic reasoning.
When p = {4/3}, only the reasoning LLMs exhibit any non-random behavior. Despite
this, compared to their baselines, reasoning LLMs drop drastically in their observed strategic
reasoning. A plausible explanation for poor performance in this condition is that LLMs are
vastly trained on pBCGs which involve iterating downward to a lower number (i.e., every other
condition) as the literature mainly focuses on these versions of pBCG. This lack of flexibility
means it may be difficult to adapt to a condition which involves a different iterative process,
albeit similar for a human.
When compared with human subjects, the standard LLMs are typically dominated in
strategic reasoning for all the alternate conditions. Cl-3S does comparably when p = {1/2}
against human subjects but is dominated for all other conditions. Both Cl-4ST, and Ge-
2T perform better and are comparable or better in all conditions except the n = unspecified
condition. GPT-o1 outperforms human subjects in terms of strategic reasoning in all alternate
conditions, except when p = {4/3} in which case it is slightly outperformed by human
subjects, yet still comparable in reasoning.16
The estimates of the CH model corroborate the finding of low strategic reasoning across
16We conduct similar KS tests as was done for the baseline condition to compare raw responses. Results
are summarized in Table A1. We focus on cases in which exactly one of the one-sided tests is rejected. For
the target proportion conditions (Np=1/2 = 48; Np=4/3 = 51), all LLMs, excluding Cl-4ST, are outperformed
by human subjects with Ge-2T outperforming when p = {1/2} (Nagel, 1995b). GPT-o1 outperforms when
n = {unspecified} (N = 120) and the median (N = 1468) conditions (Hermes and Schunk, 2022; Bosch-
Dom`enech et al., 2002). For the n = {2} alternate condition in (Grosskopf and Nagel, 2008) (N = 132), only
GPT-o1 clearly outperforms human subjects.
9

--- Page 11 ---

all alternate conditions for standard LLMs and that all reasoning LLMs (weakly) outperform
standard LLMs, summarized by Table 1. When p = {4/3}, all LLMs perform poorly, with
GPT-o1 barely outperforming the other LLMs.17 From Table 1 we also observe that human
subjects overall outperform standard LLMs in strategic reasoning, except when n = 2 where
human subjects perform surprisingly poorly, as discussed in Grosskopf and Nagel (2008).
Cl-3S is comparable with human subjects in most conditions except the n = {unspecified}
in which human subjects exhibit almost 2 more steps of reasoning. Ge-2T is comparable
in the median condition, and outperforms when p = {1/2}, but outperformed otherwise.
GPT-o1 vastly outperforms human subject in all treatments in terms of strategic reasoning,
by almost 2 steps of thinking on average, with only the p = {4/3} being comparable with
human subjects.
2.4
Multiple Rounds Results
From the previous analysis, it is evident that the majority of LLMs display limited strategic
reasoning in one-shot pBCG, particularly the standard LLMs. To investigate further, we
explore a repeated version of pBCG with multiple rounds to see whether LLMs can learn to
adjust their responses.
From Figure 2, across all LLMs, GPT-o1’s initial responses are always closest to the
fully rational prediction, approximately exhibiting L2 behavior. For p = {2/3}, the initial
responses of the other LLMs are consistent with L0 and L1 (or approximate L2 behavior,
approximately consistent with their one-shot levels of strategic reasoning. A similar result
occurs when p = {4/3} with only L0 behavior being observed.
When p = {2/3}, all LLMs exhibit a downward trend to the rational prediction; Ge-1 only
manages to converge to approximately L3 behavior, but does not approximate L∞behavior
unlike the other LLMs which do get to (in the close vicinity of) the rational prediction by
round 10. Likewise, for p = {4/3}, all LLMs show upward trends across all rounds with
only Ge-1 not achieving the rational prediction.
In general, the reasoning LLMs achieve
the rational prediction faster than the standard LLMs (that converge), suggesting that even
standard LLMs are capable of learning and adapting to strategic environments with sufficient
feedback. GPT-o1 clearly outperforms all other LLMs, particularly in rate of convergence,
and initial responses.
We are able to draw comparisons and several similarities with human subjects in Ho,
Camerer and Weigelt (1998) and Weber (2003). For human subjects, the rate of convergence
(when convergence occurs) is much faster when p = {4/3} compared to p = {2/3}.18 In
17This is consistent with Ho, Camerer and Weigelt (1998) who also estimate τ = 0 when p = 1.3 (> 1).
18This is intuitive as, in principle, it takes fewer levels/steps of reasoning to achieve the rational prediction
when p = {4/3} compared to p = {2/3}.
10

--- Page 12 ---

0
10
20
30
40
50
60
70
80
90
100
1
2
3
4
5
6
7
8
9
10
Round
Average
p = 2/3
0
10
20
30
40
50
60
70
80
90
100
1
2
3
4
5
6
7
8
9
10
Round
Average
p = 4/3
Gemini-2.0 Flash (Thinking)
Gemini-1.5 Flash
Claude-4 (Sonnet Thinking)
Claude-3.5 (Sonnet)
OpenAI-o1
ChatGPT-4
Figure 2: Time series of responses for multiple rounds pBCG. This figure consists of two
figures for p = 2/3 and p = 4/3, respectively. Each figure shows the average responses in
each round for each LLM. Vertical bars are 95% confidence intervals
general, for the reasoning LLMs, the patterns of convergence and the (boundedly rational)
responses in the first round are comparable with human subjects in Ho, Camerer and Weigelt
(1998) when p = {2/3}. When p = {4/3}, LLMs seem to converge to L∞behavior faster
than human subjects. Overall, from their observed behavior, LLMs are capable of learning
and adapting in ways that are comparable to human subjects. Only the reasoning LLMs
perform consistently better than human subjects, a result which is consistent throughout the
entire analysis of pBCG.
3
Guessing Game
The Guessing Game (GG) from Costa-Gomes and Crawford (2006) is a two-player game in
which both players make a guess about the opponent’s guess, similar to the pBCG. Unlike
the pBCG, both players may have different target multipliers and different domains for their
answers, which is common knowledge to both players.19 This asymmetry in target multipliers
and answer domains leads to an asymmetric rational prediction in Nash equilibrium between
19Recall that in pBCG, all players have the same target multiplier – 1/3, 1/2, or 4/3 – and the same range
of choices, [0, 100].
11

--- Page 13 ---

both players. An appealing feature of the GG is its dominance-solvability within a finite
number of rounds.20 This can bring an additional advantage as we can easily identify subjects’
decision rules, and therefore, types, for both the level-k model, and the CH model, no matter
the number of levels/steps of reasoning.21,22
Game. There are two players, 1 and 2. Player 1 makes a guess, x1, within a range defined by
a lower limit, a1, and an upper limit, b1. Similarly, for player 2, x2 ∈[a2, b2]. Each player i’s
guess should be as close to their target number, which is their target multiplier pi multiplied
by the other player j’s guess, that is, pi × xj. Specifically, player i’s payoff is given by
πi = max{0, 200 −di} + max{0, 100 −di/10},
where di is the absolute difference value between player i’s guess and player i’s target number,
defined as di ≡|xi(ai, bi) −pi · xj(aj, bj)|.
The payoff function πi is uniquely maximized when di = 0 for player i and provides an
additional incentive for a closer guess di ≤200. Hence, unlike the pBCG, each player has a
unique best response to every opponent’s guess in the GG.
Theoretical Predictions. Predictions under the level-k model are made in a similar way to
the pBCG, illustrated with an example. Suppose player 1 has a choice range in [100, 900] with
p1 = 0.5 and player 2 has a choice range in [100, 500] with p2 = 1.5. An L0 type randomizes
a guess within their choice range. Hence, l1
0 = (100 + 900)/2 and l2
0 = (100 + 500)/2. An L1
type believes that the opponent is a L0 type and best responds to their belief. The best guess
for player 1 with L1 is 0.5 × l2
0 = 150, which is within the range of player 1’s choice. Hence,
l1
1 = 150. Similarly, the best guess for player 2 with L1 is 1.5×l1
0 = 750. As this is not within
player 2’s choice range, l2
1 is 500 which is the closest number to 750 within [100, 500]. This
process continues, generating predictions for each level of reasoning in the level-k model for
both players until the Nash equilibrium is reached.
Similarly, in the CH model, the reasoning step sk for k = 1, 2, . . . , is defined as
(s1
k, s2
k) =

p1 ·
k−1
X
j=0
fk(j; τ)s2
j, p2 ·
k−1
X
j=0
fk(j; τ)s1
j

,
20A game is called dominance-solvable if the iterated elimination of dominated strategies results in a unique
Nash equilibrium, as in pBCG and GG, but not in MRG.
21Recall the pBCG with a choice range of [0, 100] is, in principle, dominance solvable only in an infinite
number of rounds for targets that are less than one (p < 1) meaning we may not be able to pin down precisely
the exact levels/steps of reasoning required to reach equilibrium. Although, in practice, subjects/LLMs most
likely choose the Nash equilibrium response once their steps of reasoning reasonably converges to 0.
22From a practical standpoint, the GG is not as commonly studied in the literature, suggesting LLMs will
not be trained on many sources involving the GG as compared to the pBCG; this is also true for the MRG,
analyzed in the next section.
12

--- Page 14 ---

where fk(j; τ) is the conditional probability for a step-k player, as defined in Equation (1).
As before, each si
k must be restricted to the player’s choice range [ai, bi].
The complete sets of predictions from the level-k and the CH models for the different
parameters (provided in Table A4) used in the GGs are given in Tables A5 and A6, respec-
tively.
Estimation. As with the pBCG, we estimate the (same) parameters for both the level-k and
CH models by MLE. The notable difference here is that we collect data sequentially for the
16 rounds of the GG. As we collect these sequence of responses 100 times for each LLM, we
are able to estimate both models on an individual-response level. In other words, we estimate
each model for every sequence of responses and for our final estimates, we take the average of
the parameters by LLM.23 The interpretation of both models remains the same. A detailed
description of the estimation for both models is provided in Section B.4.2 of Appendix B.
3.1
Design
Different parameters in
 ai, bi, pi
for players i = 1, 2 constitute different games. We follow
precisely the 16 GGs used in Costa-Gomes and Crawford (2006). Each player has a target
multiplier from {0.5, 0.7, 1.3, 1.5}, a lower limit from {100, 300}, and an upper limit from
{500, 900}. The complete set of parameters, with the order of the games played, is provided in
Table A4. For each LLM, we collect 100 sets of responses for the 16 rounds of the sequentially
played GG, that is, using the same experimental design as Costa-Gomes and Crawford (2006).
3.2
Results
As with the pBCG, we conducted a series of preliminary questions to test whether LLMs
understand the rules of the games, as well as choosing accurate best responses when given
the action of the other player. All LLMs answered questions correctly with respect to rules,
however only the reasoning LLMs and Cl-3S consistently provided correct answers to the
best-responses questions, unlike the other LLMs with approximately 100% error rate. Given
this, we collect data focusing only on the reasoning LLMs and Cl-3S.
From Figure 3, the majority of responses for Cl-3S are consistent with L0 and L1 behavior
with virtually no higher-order strategic reasoning. Only the reasoning LLMs exhibit any
substantial proportion of L∞behavior, with far fewer L0 and L1 responses for GPT-o1. The
level-k proportions are also estimated using data from Costa-Gomes and Crawford (2006)
23Naturally, another way to approach the estimation is to aggregate the data for each round, and estimate
the model for each of the 16 rounds of the GG, as if each round is their own one-shot game. However, this
does not make use of the sequential nature in which the GG is played in Costa-Gomes and Crawford (2006),
which we attempt to stay as close to as possible, in terms of experimental design.
13

--- Page 15 ---

(N = 88). Estimates suggests that Ge-2T performs similarly to human subjects, with Cl-
3S performing worse and GPT-o1 and Cl-4ST demonstrating more strategic reasoning than
human subjects, strongly in favor of GPT-o1. Table A2 reports frequencies of round-by-
round comparisons with human subjects, showing that GPT-o1 and Cl-4ST demonstrate
more strategic reasoning than Cl-3S and Ge-2T in 12 and 10 out of 16 rounds, respectively.
The results from the CH model are in line with the level-k model. On average, GPT-o1
exhibits approximately 3 steps of reasoning, which is roughly 2 more steps of reasoning than
Cl-3S and 1 more step than Ge-2T and Cl-4ST. Human subjects from Costa-Gomes and
Crawford (2006) exhibit just under 2 steps suggesting human subjects exhibit lower strategic
reasoning than GPT-o1, and with comparable levels to the other reasoning LLMs.
Level-∞
Level-4
Level-3
Level-2
Level-1
Level-0
0.0
0.2
0.4
0.6
0.8
1.0
Average Proportions
Human Subjects
Gemini-2.0 Flash (Thinking)
Claude-4 (Sonnet Thinking)
Claude-3.5 (Sonnet)
OpenAI-o1
Figure 3: Estimates of the proportions of level-k types for the GG with bootstrapped 95%
confidence intervals.
4
Money Request Game
The MRG offers several advantages over the pBCG and GG. From a theoretical standpoint,
its simplicity triggers behavior associated with the level-k reasoning with an intuitive L0
assumption and clearly separates reasoning levels within the action space.
Additionally,
there is no pure Nash equilibrium, requiring players to depend on more sophisticated strategic
14

--- Page 16 ---

τ
GPT-o1
2.84
(1.78,4.08)
Cl-3S
0.69
(0.00,1.43)
Cl-4ST
1.94
(1.29,2.91)
Ge-2T
1.51
(0.68,2.51)
Human Subjects
1.78
(0.81,3.00)
Table 2: Estimates of τ from the CH model GG.
reasoning.24,25
Game. Two players simultaneously choose an integer between 11 and 20. Each player is
awarded an amount of money corresponding to the number they choose. Additionally, if a
player selects a number exactly one less than the opponent’s choice, the player receives an
extra payment of 20.
Theoretical Predictions. The choice of 20 plays a role as an anchor to which we denote as
L0. Clearly, the choice of 20 is not driven by uniform randomization, but it is a safe choice
since it does not involve any strategic concern in the sense that a player can secure the payoff
of 20 from the choice of 20 (but without any chance of receiving the bonus payoff). As such,
the choice of 19 is the best response to 20, the choice of 18 is the best response to 19,..., and
the choice of 11 is the best response to 12.
From this observation, the level-k model predictions for the reasoning levels lk are as
follows.
l0 = 20,
l1 = 19,
l2 = 18,
. . . ,
l9 = 11.
Similarly, in the CH model, the reasoning step sk for k = 1, 2, . . . , is defined as
sk = round


k−1
X
j=0
fk(j; τ)sj

−1,
24Choosing any particular number with certainty for each player is not a Nash equilibrium. Instead, each
player would need to randomly choose a set of strategies according to a pre-specified distribution. We do not
consider such a mixed-strategy equilibrium as we only request a single action from each LLM subject, not a
distribution over actions.
25We focus on Game 1 of Arad and Rubinstein (2012). Game 3, which is a variation of Game 1 is included
in Section B.1 of Appendix B; the results are approximately the same across games.
15

--- Page 17 ---

where round(x) outputs the nearest integer to x, and fk(j; τ) is the conditional probability
for of a step-k player, as defined in Equation (1).
Estimation. As with the pBCG and GG, we use MLE to estimate the level-k model and
the CH model, analogously to what was done previously.
We keep the same number of
levels/steps as the pBCG but replace L∞with L4, as there is no pure Nash equilibrium. We
still accommodate behavior which is not predicted by the level-k or CH model by including
a purely random type. However, as L0 behavior can be very distinct from purely random
behavior, we specifically distinguish between these two types.26 Given the finite nature of the
actions and theoretical predictions in MRG, MLE is more appropriately specified using the
responses and best guesses directly, as opposed to a noisy best guess. A detailed description
of the estimation for both models is provided in Section B.4.3 of Appendix B.
4.1
Results
Each LLM consistently provided correct answers, both when asked about the game rules and
when responding to questions about best responses.
From Figure 4, the distinction between standard LLMs and reasoning LLMs is not as
clearly dichotomous. While it is clear that Ge-2T exhibits the highest strategic reasoning (and
overall still weakly in favor of reasoning LLMs), all other LLMs do not show any substantial
strategic reasoning beyond L1 with both GPT-o1 and Cl-4ST exhibit substantially high levels
of random/L0 behavior. Using data from Arad and Rubinstein (2012) to give us the human
subject benchmark suggests that they are mainly L2 and L3 suggesting all LLMs are vastly
outperformed except Ge-2T which exhibits comparable or higher levels of reasoning than
human subjects.27
From the estimates of τ in Table 3, both GPT-o1 and Ge-2T exhibit the highest strategic
reasoning followed by GPT-4, with the remaining showing no steps of reasoning.
These
estimates are largely in agreement with the the level-k model. The largest discrepancy is for
Ge-2T where τ is 1, which may be surprising at first inspection. However, this is a natural
consequence of the CH model itself. Recall that players are best responding to mixtures of
players with lower steps of reasoning. As this mixture is governed by a (truncated) Poisson
distribution, this suggests that it is empirically challenging to fit a CH model to behavior
26Another reason for doing this is to allow 15 to be choice consistent with uniform randomization choice,
and lower choices, to be considered as random behavior, rather than a very high stage of reasoning. This is
consistent with the empirical results in Arad and Rubinstein (2012) with a minority of subjects choosing lower
than 15.
27Using data from Arad and Rubinstein (2012) (N = 108), we also conduct similar one-sided KS tests as
with the pBCG. Excluding LLMs that exhibited random behavior by our definition (Ge-1.5) and responses
from both Cl-3S and Cl-4ST that are random (by not exhibiting L0 to L4 behavior), all p-values were less
than 0.005. This implies that human subject responses were cumulatively lower than LLMs, thus suggesting
LLMs were outperformed across the whole distribution of responses
16

--- Page 18 ---

Level-4
Level-3
Level-2
Level-1
Level-0
Random
0.0
0.2
0.4
0.6
0.8
1.0
Average Proportions
Human Subjects
Gemini-2.0 Flash (Thinking)
Gemini-1.5 Flash
Claude-4 (Sonnet Thinking)
Claude-3.5 (Sonnet)
OpenAI-o1
ChatGPT-4
Figure 4: Estimates of the proportions of level-k types for MRG.
with multiple peaks in the distribution of responses. As such, the CH model with a low
τ provides the best fit for this kind of data.28 The low estimates of τ provide a different
perspective from the level-k model; the average number of steps of reasoning is still low,
given that we observe a majority of lower-step responses, despite a mass of isolated high-step
responses.29
Compared to human subjects, LLMs are clearly outperformed, with human
subjects exhibiting just over 3 steps of reasoning.
5
Discussion
In this paper, we evaluate the strategic reasoning capabilities of standard and reasoning
LLMs using models of bounded rationality. In the pBCG, reasoning LLMs demonstrated
substantially higher strategic sophistication than standard LLMs across most conditions with
human subjects typically outperformed overall. Surprisingly, all LLMs struggled when the
target multiplier exceeded one (p = 4/3), likely due to training predominantly on games re-
quiring downward iterative reasoning. When faced with the repeated pBCG (including when
p = 4/3), all LLMs exhibited learning and convergence toward the rational prediction, but
with reasoning LLMs converging faster than standard LLMs. In the GG, a much clearer divide
emerged between reasoning and standard LLMs. While reasoning LLMs exhibited substantial
28If there is a vast majority of answers that are consistent with higher-steps of behavior, only then would
this result in a much higher estimate of τ.
29This might suggest that the CH model is not an appropriate model for fitting these kind of data, as we
want to observe a natural hierarchy of steps of reasoning, rather than observing jumps in reasoning, ideally
with one mode (peak) in the distribution of responses.
17

--- Page 19 ---

MRG
GPT-4
0.91
(0.86,0.97)
GPT-o1
1.21
(1.11,1.31)
Cl-3S
0.00
(0.00,0.00)
Cl-4ST
0.00
(0.00,0.70)
Ge-1
0.00
(0.00,0.00)
Ge-2T
1.00
(1.00,1.22)
Human Subjects
3.14
(2.17,3.65)
Table 3: Estimates of τ from the CH model for MRG.
strategic sophistication, standard LLMs except Cl-3S failed even basic comprehension checks
regarding best-response calculations. Despite understanding, Cl-3S was clearly outperformed
by the reasoning LLMs, with reasoning LLMs exhibiting equivalent or superior strategic rea-
soning to human subjects. For the MRG, while reasoning LLMs still outperformed standard
LLMs, human subjects exhibited superior strategic reasoning, with only Ge-2T demonstrat-
ing comparable performance to humans, while other reasoning LLMs showed surprisingly
high levels of random behavior. While our analyses across the three behavioral economics
games reveal that LLMs’ strategic reasoning capabilities are not uniform, our overarching
conclusion is that reasoning LLMs exhibit substantially higher strategic reasoning compared
to standard LLMs, with reasoning LLMs overall exhibiting superior strategic sophistication
compared to typical human subjects.
The games in our study were specifically chosen because they require players to anticipate
others’ strategies, allowing us to investigate, model, and evaluate LLMs’ strategic reasoning
(Zhang et al., 2025).30 Our results reveal a clear distinction between standard LLMs and
reasoning LLMs in their ability to engage in strategic reasoning. In the cases where standard
LLMs could provide accurate best responses – demonstrating analytical ability – when given
30While higher-order reasoning – even at the Nash equilibrium – does not always lead to a better outcome
in games, there is an important exception in the two-person pBCG (n = 2): higher-order reasoning always
results in a better outcome because choosing the smaller number guarantees a win in this case. Our result
from the two-person pBCG aligns with the results in other pBCGs in Figure 1 and Table 1. This observation
supports our conclusion, which draws on measuring strategic reasoning using both level-k and CH models.
18

--- Page 20 ---

explicit information about the strategies of the others, they struggled in multi-agent environ-
ments that require anticipating opponents’ strategies through higher-order iterated reasoning,
whereas reasoning LLMs demonstrate strategic reasoning abilities that often match or exceed
human performance across the games. Despite this, we still observed (surprising) drops in
strategic reasoning in reasoning LLMs when given essentially logically-equivalent variations
of the pBCG, which is in line with recent work by Apple (Shojaee et al., 2025) showing
reasoning LLMs exhibit inconsistent performance across different puzzle variations and com-
plexity levels (in a non-strategic environment).31 With their growing application in AAI,
reasoning LLMs have shown their potential in multi-agent reasoning, particularly in environ-
ments where anticipating others’ strategies is vital (Duan et al., 2024a; Lor`e and Heydari,
2024; Duan et al., 2024b; Bousetouane, 2025; Singh et al., 2024).
An interesting finding is that even standard LLMs perform significantly better in repeated
interaction than in one-shot environments. This suggests that sequential feedback enables
LLMs to refine their strategic understanding through iterative learning. This insight helps
explain why reasoning LLMs exhibit superior capabilities – they are trained to effectively
think, i.e., refine strategies by breaking down tasks into more manageable, simpler steps.
Through this process, reasoning LLMs gain a better understanding of any given reasoning
task, analogous to the procedure in the repeated feedback of the pBCG. We believe this is
the main reason for reasoning LLMs’ success in strategic reasoning (particularly GPT-o1),
especially compared to other LLMs that are not similarly trained.32 This paper underscores
the emergence of strategic reasoning in reasoning LLMs, a natural capability that was yet to
emerge in standard LLMs.
Methods
Collecting LLM data
We collect data from LLMs from OpenAI, Anthropic, and Google using their APIs. The
exact model names of each LLM used are: gpt-4, o1-preview-2024-09-12, claude-3-5-sonnet-
20241022, claude-sonnet-4-20250514, gemini-1.5-flash, gemini-2.0-flash-thinking-exp-1219. For
consistency and replicability, we used the same system message across all games, with dif-
ferences only in the number of rounds played. We tell LLMs to state their final answer in []
31Recent criticisms of Shojaee et al. (2025), such as Lawsen (2025), argue that many observed failures of
reasoning LLMs are a result of critical issues in experimental design (e.g. output token limits and impossible
puzzles) rather than fundamental reasoning limitations. Preliminary evidence suggests that when experiments
are designed that address these issues, reasoning LLMs exhibit much higher accuracy, in direct contrast with
Apple’s original findings. As we are not constrained by similar experimental design issues (especially as we
are concerned with strategic environments), our findings are still consistent (yet distinct) from Apple.
32Although Cl-3S is said to exhibit higher reasoning capabilities, the nature of its reasoning is not public,
therefore, we do not comment on its performance compared to GPT-o1 and Ge-2T which we know are designed
for strategic thinking.
19

--- Page 21 ---

to allow easy extraction of their final response. The rules and description of the games were
provided in the assistant message. The full set of prompts is contained in Appendix B.
Human subject data
We use human subject data from seminal papers in behavioral economics to compare with
LLMs. For the pBCG, we use data from the seminal papers, as well as other published papers
for the alternate conditions Nagel (1995b); Hermes and Schunk (2022); Bosch-Dom`enech
et al. (2002). For the GG, we use data from the original paper (Costa-Gomes and Crawford,
2006). For the MRG, we use data from the original paper (Arad and Rubinstein, 2012).
These serve as essential benchmarks to compare with LLM performance with their results
being representative of human subject performance. As mentioned, all datasets come from
published work and were subject to their own ethics committees.
Testing LLM and human subjects data
Using standard MLE techniques, we estimate the level-k model and the CH model. Stata
estimation codes for these models can be found in Moffatt (2015), a textbook for estimation in
behavioral and experimental economics. We translated and edited the code from Stata to R;
we obtain the same results from practice datasets from Moffatt (2015) to ensure replicability.
Technical estimation details can be found in Appendix B. Further, we do distributional
tests (KS tests) to compare raw responses. We use both one-sided to check for first order
stochastic dominance to compare rationality and two-sided tests to compare the distribution
of responses.
Data Availability
All datasets used are publicly available here. This includes all estimates and figures contained
in this article
Code Availability
Our code is publicly available here.
References
Abdelnabi, Sahar, Amr Gomaa, Sarath Sivaprasad, Lea Sch¨onherr, and Mario
Fritz. 2024. “Cooperation, Competition, and Maliciousness: LLM-Stakeholders Interactive
Negotiation.” arXiv:2309.17234 [cs].
20

--- Page 22 ---

Ahn, Janice, Rishu Verma, Renze Lou, Di Liu, Rui Zhang, and Wenpeng Yin.
2024. “Large Language Models for Mathematical Reasoning: Progresses and Challenges.”
Preprint at http://arxiv.org/abs/2402.00157.
Almutairi, Mariam, and Hyungmin Kim. 2025. “Resilient Multi-Agent Negotiation for
Medical Supply Chains:Integrating LLMs and Blockchain for Transparent Coordination.”
arXiv:2507.17134 [cs].
An, Siyu, Qin Li, Junru Lu, Di Yin, and Xing Sun. 2024. “FinVerse: An Autonomous
Agent System for Versatile Financial Analysis.” arXiv:2406.06379 [cs].
Anthropic. 2024. “The Claude 3 Model Family: Opus, Sonnet, Haiku.”
Arad, Ayala, and Ariel Rubinstein. 2012. “The 11–20 Money Request Game: A Level-
k Reasoning Study.” American Economic Review, 102(7): 3561–3573.
Bernheim, B. Douglas, Stefano DellaVigna, and David Laibson, ed. 2019. Handbook
of Behavioral Economics - Foundations and Applications 1, Volume 2. Elsevier. Backup
Publisher: Elsevier.
Binz, Marcel, and Eric Schulz. 2023. “Using cognitive psychology to understand GPT-3.”
Proceedings of the National Academy of Sciences, 120(6): e2218523120.
Bosch-Dom`enech, Antoni, Jos´e G. Montalvo, Rosemarie Nagel, and Albert
Satorra. 2002. “One, Two, (Three), Infinity, ...: Newspaper and Lab Beauty-Contest
Experiments.” American Economic Review, 92(5): 1687–1701.
Bousetouane, Fouad. 2025. “Agentic Systems: A Guide to Transforming Industries with
Vertical AI Agents.” Preprint at http://arxiv.org/abs/2501.00881.
Brocas, Isabelle, and Juan D. Carrillo. 2020. “The evolution of choice and learning in the
two-person beauty contest game from kindergarten to adulthood.” Games and Economic
Behavior, 120: 132–143.
Camerer, C. F., T.-H. Ho, and J.-K. Chong. 2004. “A Cognitive Hierarchy Model of
Games.” Quarterly Journal of Economics, 119(3): 861–898.
Camerer, Colin F. 2011. Behavioral game theory: Experiments in strategic interaction.
Behavioral game theory: Experiments in strategic interaction, New York, NY, US:Princeton
University Press.
Camerer, Colin F., George Loewenstein, and Matthew Rabin. 2004. Advances in
Behavioral Economics. Princeton University Press.
21

--- Page 23 ---

Chen, Yiting, Tracy Xiao Liu, You Shan, and Songfa Zhong. 2023. “The emer-
gence of economic rationality of GPT.” Proceedings of the National Academy of Sciences,
120(51): e2316205120.
Costa-Gomes, Miguel A, and Vincent P Crawford. 2006. “Cognition and Behavior
in Two-Person Guessing Games: An Experimental Study.” American Economic Review,
96(5).
Crawford, Vincent P, Miguel A Costa-Gomes, and Nagore Iriberri. 2013. “Struc-
tural Models of Nonequilibrium Strategic Thinking: Theory, Evidence, and Applications.”
Journal of Economic Literature, 51(1): 5–62.
Duan, Jinhao, Renming Zhang, James Diffenderfer, Bhavya Kailkhura, Lichao
Sun, Elias Stengel-Eskin, Mohit Bansal, Tianlong Chen, and Kaidi Xu. 2024a.
“GTBench: Uncovering the Strategic Reasoning Limitations of LLMs via Game-Theoretic
Evaluations.” Preprint at http://arxiv.org/abs/2402.12348.
Duan, Jinhao, Shiqi Wang, James Diffenderfer, Lichao Sun, Tianlong Chen,
Bhavya Kailkhura, and Kaidi Xu. 2024b. “ReTA: Recursively Thinking Ahead to
Improve the Strategic Reasoning of Large Language Models.” 2232–2246. Mexico City,
Mexico:Association for Computational Linguistics.
Georganas, Sotiris, Paul J. Healy, and Roberto A. Weber. 2015. “On the persistence
of strategic sophistication.” Journal of Economic Theory, 159: 369–400.
Grosskopf, Brit, and Rosemarie Nagel. 2008. “The two-person beauty contest.” Games
and Economic Behavior, 62(1): 93–99.
Hagendorff, Thilo, Sarah Fabi, and Michal Kosinski. 2023. “Human-like intuitive
behavior and reasoning biases emerged in large language models but disappeared in Chat-
GPT.” Nature Computational Science, 3(10): 833–838.
Hermes, Henning, and Daniel Schunk. 2022. “If you could read my mind–an experi-
mental beauty-contest game with children.” Experimental Economics, 25(1): 229–253.
Ho, Teck-Hua, Colin Camerer, and Keith Weigelt. 1998. “Iterated Dominance and It-
erated Best Response in Experimental “p-Beauty Contests”.” American Economic Review,
88(4): 947–969.
Kim, Jeongbin, Matthew Kovach, Kyu-Min Lee, Euncheol Shin, and Hector
Tzavellas. 2024. “Learning to be Homo Economicus: Can an LLM Learn Preferences
from Choice.” Preprint at http://arxiv.org/abs/2401.07345.
22

--- Page 24 ---

Kwon, Deuksin, Emily Weiss, Tara Kulshrestha, Kushal Chawla, Gale M. Lucas,
and Jonathan Gratch. 2024. “Are LLMs Effective Negotiators? Systematic Evaluation
of the Multifaceted Capabilities of LLMs in Negotiation Dialogues.” arXiv:2402.13550 [cs].
Lawsen, A. 2025. “Comment on The Illusion of Thinking: Understanding the Strengths and
Limitations of Reasoning Models via the Lens of Problem Complexity.” arXiv:2506.09250
[cs].
Lor`e, Nunzio, and Babak Heydari. 2024. “Strategic behavior of large language models
and the role of game structure versus contextual framing.” Scientific Reports, 14(1): 18490.
Loya, Manikanta, Divya Anand Sinha, and Richard Futrell. 2023. “Exploring the
Sensitivity of LLMs’ Decision-Making Capabilities: Insights from Prompt Variation and
Hyperparameters.” 3711–3716. Preprint at http://arxiv.org/abs/2312.17476.
Luo, Yunfei, and Zhangqi Duan. 2025. “Agent Performing Autonomous Stock Trading
under Good and Bad Situations.” arXiv:2306.03985 [cs] version: 2.
Mei, Qiaozhu, Yutong Xie, Walter Yuan, and Matthew O Jackson. 2024. “A Turing
Test: Are AI Chatbots Behaviorally Similar to Humans?” Proceedings of the National
Academy of Sciences, 121(9): e2313925121.
Moffatt, Peter G. 2015. Experimetrics: Econometrics for Experimental Economics. Lon-
don:Palgrave Macmillan.
Mumuni, Alhassan, and Fuseini Mumuni. 2025. “Large language models for arti-
ficial general intelligence (AGI): A survey of foundational principles and approaches.”
arXiv:2501.03151 [cs] version: 1.
Nagel, Rosemarie. 1995a. “Dataset Unraveling in Guessing Games: An Experimental
Study.” https://x-science.org/xscience/#!Detail/10.23663/x2646.
Nagel, Rosemarie. 1995b. “Unraveling in Guessing Games: An Experimental Study.”
American Economic Review, 85(5): 1313–1326.
Nagel, Rosemarie, Antoni Bosch-Dom`enech, Gary Charness, Garc´ıa-Montalvo
Jos´e, Sjaak Hurkens, L´opez Nicol´as ´Angel, Niklas Matthies, Bettina Rocken-
bach, Albert Satorra, Richard Selten, and Richard H. Thaler. 2002. “Dataset One,
Two, (Three), Infinity, ...: Newspaper and Lab Beauty-Contest Experiments.” https://x-
science.org/xscience/#!Detail/10.23663/x2544.
OpenAI.
2024.
“OpenAI
o1-Preview
System
Card.”
https: // cdn. openai. com/
o1-system-card-20241205. pdf/ , Accessed: 2024-09-20.
23

--- Page 25 ---

Schaeffer, Rylan, Brando Miranda, and Sanmi Koyejo. 2023. “Are Emergent Abilities
of Large Language Models a Mirage?” Preprint at http://arxiv.org/abs/2304.15004.
Shojaee, Parshin, Iman Mirzadeh, Keivan Alizadeh, Maxwell Horton, Samy Ben-
gio, and Mehrdad Farajtabar. 2025. “The Illusion of Thinking: Understanding the
Strengths and Limitations of Reasoning Models via the Lens of Problem Complexity.”
arXiv:2506.06941 [cs].
Singh, Aditi, Abul Ehtesham, Saket Kumar, and Tala Talaei Khoei. 2024. “Enhanc-
ing AI Systems with Agentic Workflows Patterns in Large Language Model.” 527–532.
Stahl, Dale O., and Paul W. Wilson. 1994. “Experimental evidence on players’ models
of other players.” Journal of Economic Behavior & Organization, 25(3): 309–327.
Stahl, Dale O., and Paul W. Wilson. 1995. “On Players’ Models of Other Players:
Theory and Experimental Evidence.” Games and Economic Behavior, 10(1): 218–254.
Webb, Taylor, Keith J. Holyoak, and Hongjing Lu. 2023. “Emergent analogical rea-
soning in large language models.” Nature Human Behaviour, 7(9): 1526–1541.
Weber, Roberto A. 2003. “‘Learning’ with no feedback in a competitive guessing game.”
Games and Economic Behavior, 44(1): 134–144.
Wei, Jason, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Brian Ichter, Fei
Xia, Ed Chi, Quoc Le, and Denny Zhou. 2023. “Chain-of-Thought Prompting Elicits
Reasoning in Large Language Models.” Preprint at http://arxiv.org/abs/2201.11903.
Wei, Jason, Yi Tay, Rishi Bommasani, Colin Raffel, Barret Zoph, Sebastian
Borgeaud, Dani Yogatama, Maarten Bosma, Denny Zhou, Donald Metzler,
Ed H. Chi, Tatsunori Hashimoto, Oriol Vinyals, Percy Liang, Jeff Dean, and
William Fedus. 2022. “Emergent Abilities of Large Language Models.” Preprint at
http://arxiv.org/abs/2206.07682.
Xu, Liming, Stephen Mak, Maria Minaricova, and Alexandra Brintrup. 2024.
“On Implementing Autonomous Supply Chains:
a Multi-Agent System Approach.”
arXiv:2310.09435 [cs].
Zhang, Yadong, Shaoguang Mao, Tao Ge, Xun Wang, Yan Xia, Man Lan, and
Furu Wei. 2025. “K-Level Reasoning: Establishing Higher Order Beliefs in Large Lan-
guage Models for Strategic Reasoning.” 7212–7234. Albuquerque, New Mexico:Association
for Computational Linguistics.
24

--- Page 26 ---

Zhou, Zihao, Qiufeng Wang, Mingyu Jin, Jie Yao, Jianan Ye, Wei Liu, Wei Wang,
Xiaowei Huang, and Kaizhu Huang. 2024. “MathAttack: Attacking Large Language
Models towards Math Solving Ability.” Proceedings of the AAAI Conference on Artificial
Intelligence, 38(17): 19750–19758.
Zhu, Yuqi, Jia Li, Ge Li, YunFei Zhao, Jia Li, Zhi Jin, and Hong Mei. 2024. “Hot
or Cold?
Adaptive Temperature Sampling for Code Generation with Large Language
Models.” Proceedings of the AAAI Conference on Artificial Intelligence, 38(1): 437–445.
Author Contributions
G.K. and D.L wrote the paper, designed the prompts for the experiments, and interpreted
the results. G.K. collected and analyzed the data, and interpreted results. G.K. and D.L
share first authorship.
Competing Interests
The authors declare no competing interests.
Additional Information
Extended data is available for this paper in Appendix A.
Supplementary information is available for this paper in Appendix B.
Correspondence should be addressed to Dongwoo Lee.
25

--- Page 27 ---

A
Supplementary Tables
LLM
Game (pBCG)
H0: Two-sided
H0: Not Less
H0: Not Greater
More rational
GPT-4
Median
0
0
0.243
Human
GPT-4
n=unspecified
0
0
0.57
Human
GPT-4
n=2
0
0
0
-
GPT-4
p=1/2
0
0
0.009
-
GPT-4
p=2/3
0
0.192
0
LLM
GPT-4
p=4/3
0
0.361
0
Human
GPT-o1
Median
0
1
0
LLM
GPT-o1
n=unspecified
0
1
0
LLM
GPT-o1
n=2
0
1
0
LLM
GPT-o1
p=1/2
0.011
0.005
0.048
-
GPT-o1
p=2/3
0
0.123
0
LLM
GPT-o1
p=4/3
0
1
0
Human
Cl-3S
Median
0.001
0.001
0.007
-
Cl-3S
n=unspecified
0
0
0.010
-
Cl-3S
n=2
0
0
0
-
Cl-3S
p=1/2
0
0
0
-
Cl-3S
p=2/3
0
0.028
0
-
Cl-3S
p=4/3
0
0.285
0
Human
Cl-4ST
Median
0
0
0.003
-
Cl-4ST
n=unspecified
0
0
0
-
Cl-4ST
n=2
0
0.001
0
-
Cl-4ST
p=1/2
0
0.762
0
LLM
Cl-4ST
p=2/3
0
1
0
LLM
Cl-4ST
p=4/3
0.053
0.027
0.474
LLM
Ge-1
Median
0
0
0.2
Human
Ge-1
n=unspecified
0
0
0.153
Human
Ge-1
n=2
0
0
0
-
Ge-1
p=1/2
0
0
0.555
Human
Ge-1
p=2/3
0
0
0
-
Ge-1
p=4/3
0
0.113
0
Human
Ge-2T
Median
0
0
0
-
Ge-2T
n=unspecified
0
0
0
-
Ge-2T
n=2
0
0
0
-
Ge-2T
p=1/2
0
0.078
0
LLM
Ge-2T
p=2/3
0
0.26
0
LLM
Ge-2T
p=4/3
0
0.522
0
Human
Table A1: KS tests for raw responses from the pBCG. The distribution of responses from
human subjects is more rational if it is unambiguously first-order stochastically dominating
from the 1-sided KS tests.
1

--- Page 28 ---

LLM
LLMs more rational
Rounds
GPT-o1
12
1-11, 14
Cl-3S
3
2, 5, 9
Cl-4ST
10
1-2, 4, 6-10, 13-14, 16
Ge-2T
4
1-3, 8
Table A2: Frequency of LLMs providing more Nash equilibrium responses than human
subjects (out of 16), and in which specific rounds. LLMs are considered more rational if the
number of Nash equilibrium responses is strictly larger than human subjects.
LLM
H0: Two-sided
H0: Not Less
H0: Not Greater
More rational
GPT-4
0
0
0.87
Human
GPT-o1
0
0
1
Human
Cl-3S
0
0
0.590
-
Cl-4ST
0
0.833
0
-
Ge-1
0
0.644
0
-
Ge-2T
0
0
0.026
-
Table A3: KS tests for raw responses from the MRG. The distribution of responses from
human subjects is more rational if it is unambiguously first-order stochastically dominated
from the 1-sided KS tests (excluding Ge-1.5, Cl-3S, and Cl-4ST).
2

--- Page 29 ---

Player 1
Player 2
Games
Targets
Lower
Limits
Upper
Limits
Targets
Lower
Limits
Upper
Limits
1
1.3
300
900
1.5
300
500
2
0.7
100
500
1.5
100
500
3
1.5
100
900
0.7
300
500
4
1.5
100
500
0.5
100
900
5
0.5
100
900
1.5
100
500
6
0.5
100
900
0.7
100
500
7
1.3
100
900
0.7
300
900
8
0.5
100
900
0.7
300
500
9
1.5
100
500
0.7
100
500
10
0.7
300
900
1.3
100
900
11
0.7
300
500
0.5
100
900
12
0.7
300
500
1.5
100
900
13
1.3
300
900
1.3
300
900
14
0.7
100
500
0.5
100
900
15
1.3
300
900
1.3
300
900
16
1.5
300
500
1.3
300
900
Table A4: Task parameters from Costa-Gomes and Crawford (2006) used for the GG.
3

--- Page 30 ---

Games
l0
l1
l2
l3
l4
l5
l6
l7
l8
l9
l10
l11
1
600
520
650∗
2
300
210
315
220.5
330.75
231.53
347.29
243.10
350∗
3
500
600
525
630
551.25
661.50
578.81
694.58
607.75
729.30
638.14
750∗
4
300
500
225
375
168.75
281.25
150∗
5
500
150
250
112.50
187.50
100∗
6
500
150
175
100∗
7
500
780
455
709.80
414.05
645.92
390∗
8
500
200
175
150∗
9
300
450
315
472.5
330.75
496.13
347.29
500∗
10
600
350
546
318.50
496.86
300∗
11
400
350
300∗
12
400
350
420
367.50
441
385.88
463.05
405.17
486.20
425.43
500∗
13
600
780
900∗
14
300
350
105
122.50
100∗
15
600
780
900∗
16
400
500∗
Table A5: Predictions from the level-k model for the 16 GGs. Asterisk refers to reaching the Nash equilibrium action.
4

--- Page 31 ---

Games
s0
s1
s2
s3
s4
s5
1
600
520
598
614.14
618.96
620.44
2
300
210
273
268.44
268.26
268.30
3
500
600
555
565.24
568.08
569.00
4
300
500
435
397.76
387.11
383.69
5
500
150
210
212.33
210.52
209.71
6
500
150
165
145.29
137.59
134.97
7
500
780
585
592.10
591.07
590.46
8
500
200
185
174.14
170.90
169.89
9
300
450
369
381.57
384.40
385.26
10
600
350
467.60
449.57
444.85
443.36
11
400
350
300∗
12
400
350
392
390.91
391.55
391.85
13
600
780
900∗
14
300
350
203
175.84
165.89
162.55
15
600
780
900∗
16
400
500∗
Table A6: Example predictions from the CH model for the 16 GGs at τ = 1.5
5

--- Page 32 ---

B
Supplementary Methods and Notes
B.1
Supplementary MRG
Here, we analyze Game 3 of Arad and Rubinstein (2012), which is a costless iteration version
of the MRG in the main text. Game 1 (main text) and Game 2 of Arad and Rubinstein
(2012) are game theoretically identical. The only difference between Games 1 and 2 is the
increased salience of L0 behavior.33 The payoff structure of Game 3 is a slight variation from
Game 1/2, with a different equilibrium prediction, but is ultimately similar to MRG.
MRG (Game 3). Two players simultaneously choose an integer between 11 and 20. Each
player is awarded an amount of money corresponding to the number they choose. A player
is awarded 20 if they choose 20. Choosing any other number results in receiving 17. Addi-
tionally, if a player selects a number exactly one less than the opponent’s choice, the player
receives an extra payment of 20.
Level-4
Level-3
Level-2
Level-1
Level-0
Random
0.0
0.2
0.4
0.6
0.8
1.0
Average Proportions
Human Subjects
Gemini-2.0 Flash (Thinking)
Gemini-1.5 Flash
Claude-4 (Sonnet Thinking)
Claude-3.5 (Sonnet)
OpenAI-o1
ChatGPT-4
Figure B1: Estimates of the proportions of level-k types for MRG (Game 3).
For the MRG (Game 3), the level-k results are largely the same for GPT-4, and Ge-1 as
with the MRG. Ge-2T is less sophisticated, with the majority of answers being consistent
with L1 behavior, with a large reduction in higher-step responses (Figure B1). For GPT-
o1, Cl-3S, and Cl-4ST we observe increases in strategic reasoning which is in line with the
original formulation of MRG (Game 3). This is because undercutting as a strategy is no
33Additionally, some LLMs answered the understanding questions poorly for Game 1 when asked about
best responses to 11 (the lowest number). To remedy this, we make the instructions clearer by being specific
about the payoff when 11(/20) is chosen and 11(/20) is played by the other participant. As such, adding this
to Game 1’s instructions essentially replicates Game 2’s instructions.
6

--- Page 33 ---

MRG (Game 3)
GPT-4
1.00
(0.93,1.06)
GPT-o1
1.60
(1.53,1.67)
Cl-3S
0.00
(0.00,0.00)
Cl-4ST
1.64
(1.57,1.70)
Ge-1
0.00
(0.00,0.00)
Ge-2T
1.89
(1.89,1.89)
Table A7: Estimates of τ from the CH model for MRG (Game 3).
longer costly. Unlike in MRG when players may balance between choosing a higher number
(between 11 and 19) yielding a higher payoff, and undercutting to get the bonus payoff, MRG
(Game 3) removes the marginal incentive in choosing a higher number. This suggests that we
should observe increases in strategic reasoning in MRG (Game 3) relative to MRG if there is
sufficient understanding in the changed payoff structure, which we only observe for GPT-o1,
Cl-3S, and Cl-4ST .34 When compared with Arad and Rubinstein (2012) (N = 53), human
subjects are mainly random, L1 and L2 suggesting LLMs are all still vastly outperformed by
human subjects.35,36
The estimates of τ are in line with the level-k explanations above (Table A7).37 Cl-4ST
and Ge-2T have apparent jumps in steps of reasoning owing to the fact that there is now a
clear peak in the distribution of responses around the step-1/2 responses, allowing a much
better fit of the CH model, given the Poisson distribution assumption.38
34Confirmed by one-sided KS tests at 5% significance level.
35The estimated level-k model proportions (random, L1 to L4) are 0.23, 0.13, 0.37, 0.18, 0.07, 0.02, respec-
tively.
36Conducting similar one-sided KS tests with data from (again excluding Ge-1 and Cl-3S) shows that
human subjects outperformed LLMs (Table A8).
37The CH model estimate from human subjects is τ = 2.45; [1.16, 2.45]95% CI.
38A similar explanation for why Cl-3S does not exhibit higher steps of reasoning applies, despite showing
an increase in L1 responses. As the majority of the answers are consistent with random behavior, with no
responses in between random and L1 behavior, the CH model fits better for a low τ.
7

--- Page 34 ---

LLM
H0: Two-sided
H0: Not Less
H0: Not Greater
More rational
GPT-4
0
0
1
Human
GPT-o1
0
0
1
Human
Cl-3S
0.024
0.016
0.069
-
Cl-4ST
0
0
1
Human
Ge-1
0
0.619
0
-
Ge-2T
0
0
0.009
-
Table A8:
KS tests for raw responses from the MRG (Game 3).
The distribution of
responses from human subjects is more rational if it is unambiguously first-order stochastically
dominated from the 1-sided KS tests (excluding Ge-1 and Cl-3S).
B.2
Understanding Questions
The following lists all of the understanding questions asked to each LLMs related to best
responses (BR) and the rules of each game. The system prompt is the same for all questions
(as written in the paper).
Each question is repeatedly asked in isolation (no history of
previous answers).
B.2.1
pBCG
BR for 2-person (p=2/3)
Including yourself, there are 2 participants in total.
The other participant you will be
playing with is a human decision maker. All participants will be asked to pick a number
between 0 and 100 inclusive. The winner will be the one choosing the number closest to
2/3 multiplied the average of all the numbers provided by the participants (including your
own). For example, if you choose 10 and your opponent chooses 20, then you will be the
winner, as 10 is closer to 15*2/3=10 (as 15 is the average and 2/3 is the target). Or, if
you choose 30 and your opponent chooses 20, your opponent will be the winner, as 20 is
closer to 25*2/3=16.67 (as 25 is the average and 2/3 is the target). In case of multiple
winners, only one participant will be randomly chosen to win. Suppose your opponent
chooses 20. What number from 0 to 100 earns you the most?
Best responses: {0,1,. . . ,19}
BR for 11-person (p=1/2)
Including yourself, there are 11 participants in total. The other participants you will be
playing with are human decision makers. All participants will be asked to pick a number
between 0 and 100 inclusive. The winner will be the one choosing the number closest to
8

--- Page 35 ---

1/2 multiplied by the average of all the numbers provided by the participants (including
your own). For example, if you choose 14 and your opponents choose 10, 22, 23, 30,
11, 16, 37, 18, 19, 20, then the opponent with 10 will be the winner, as 10 is closer to
20*1/2=10 (as 10 is the average and 1/2 is the target). Or, if you choose 25 and your
opponents choose 5, 10, 20, 40, 50, 60, 70, 80, 90, 100, then you will be the winner, as
25 is closer to 50*1/2=25 (as 50 is the average and 1/2 is the target). In case of multiple
winners, only one participant will be randomly chosen to win. Suppose your opponents
choose 0, 80, 43, 70, 21, 33, 37, 18, 50, 50. What number from 0 to 100 earns you the
most?
Best responses: {19,20}
BR for Baseline: 11-person (p=2/3)
Including yourself, there are 11 participants in total. The other participants you will be
playing with are human decision makers. All participants will be asked to pick a number
between 0 and 100 inclusive. The winner will be the one choosing the number closest to
2/3 multiplied by the average of all the numbers provided by the participants (including
your own). For example, if you choose 14 and your opponents choose 10, 22, 23, 30, 11,
16, 37, 18, 19, 20, then you will be the winner, as 14 is closer to 20*2/3=13.33 (as 20
is the average and 2/3 is the target). Or, if you choose 25 and your opponents choose 5,
10, 20, 40, 50, 60, 70, 80, 90, 100, then the opponent with 40 will be the winner, as 40
is closer to 50*2/3=33.3 (as 50 is the average and 2/3 is the target). In case of multiple
winners, only one participant will be randomly chosen to win. Suppose your opponents
choose 0, 80, 43, 70, 21, 33, 37, 18, 50, 50. What number from 0 to 100 earns you the
most?
Best responses: {22,23,. . . ,31}
BR for 11-person (p=4/3)
Including yourself, there are 11 participants in total. The other participants you will be
playing with are human decision makers. All participants will be asked to pick a number
between 0 and 100 inclusive. The winner will be the one choosing the number closest to
4/3 multiplied by the average of all the numbers provided by the participants (including
your own). For example, if you choose 14 and your opponents choose 10, 22, 23, 30,
11, 16, 37, 18, 19, 20, then the opponent with 30 will be the winner, as 30 is closer to
20*4/3=26.67 (as 20 is the average and 4/3 is the target). Or, if you choose 25 and your
9

--- Page 36 ---

opponents choose 5, 10, 20, 40, 50, 60, 70, 80, 90, 100, then the opponent with 70 will
be the winner, as 70 is closer to 50*4/3 (as 50 is the average and 4/3 is the target). In
case of multiple winners, only one participant will be randomly chosen to win. Suppose
your opponents choose 0, 80, 43, 70, 21, 33, 37, 18, 50, 50. What number from 0 to 100
earns you the most?
Best responses: {51,52,. . . ,62}
BR for n-person (p=2/3)
Including yourself, there is a finite but unknown number n of participants in total. The
other participants you will be playing with are human decision makers. All participants
will be asked to pick a number between 0 and 100 inclusive. The winner will be the one
choosing the number closest to 2/3 multiplied by the average of all the numbers provided
by the participants (including your own). For example, if you choose 14 and your opponents
choose 10, 22, 23, 30, 11, 16, 37, 18, 19, 20, then you will be the winner, as 14 is closer
to 20*2/3=13.33 (as 20 is the average and 2/3 is the target). Or, if you choose 25 and
your opponents choose 5, 10, 20, 40, 50, 60, 70, 80, 90, 100, then the opponent with 40
will be the winner, as 40 is closer to 50*2/3=33.3 (as 50 is the average and 2/3 is the
target). In case of multiple winners, only one participant will be randomly chosen to win.
In the case with n = 11, if your opponents choose 0, 80, 43, 70, 21, 33, 37, 18, 50, 50,
what number from 0 to 100 earns you the most?
Best responses: {22,23,. . . ,31}
BR for Median
Including yourself, there are 11 participants in total. The other participant you will be
playing with is a human decision maker. All participants will be asked to pick a number
between 0 and 100 inclusive. The winner will be the one choosing the number closest to
2/3 multiplied by the median of all the numbers provided by the participants (including
your own). For example, if you choose 80 and your opponents choose 0, 80, 43, 70, 21,
33, 37, 18, 50, 50, then one of the opponents with 50 will be the winner, as 50 is closer
to 43(median)*2/3. Or, if you choose 100 and your opponents choose 5, 10, 20, 40, 50,
60, 70, 80, 90, 100, then the opponent with 40 will be the winner, as 40 is closer to
60(median)*2/3. In case of multiple winners, only one participant will be randomly chosen
to win. Suppose your opponents choose 0, 80, 43, 70, 21, 33, 37, 18, 50, 50. What
number from 0 to 100 earns you the most?
10

--- Page 37 ---

Best responses: {21,23,. . . ,28}
For each of the conditions above, LLMs were also asked the following questions (repeat-
edly, and in isolation) related to the rules and the win conditions of the pBCG:
Rules for pBCG
1. What numbers can you choose between?
2. If the number you choose is closest to {p}’s of the {average/median}, do you win
the game?
3. How many participants are there, including yourself?
4. Suppose there are 3 participants, including you, and you have to choose the number
closest to {p} of the average. The other 2 participants chose 90 and 60. Suppose
you chose 30. Therefore {p}’s of the {average/median} is {{p} × 60}. Do you win
or lose?a
5. Will decisions made in previous rounds have any effect on the current round? (re-
peated pBCG)
aThe question uses actual values for {p} and {average/median} depending on the condition. {p}×
60 is evaluated, i.e., the actual calculation is shown.
B.2.2
GG
BR for GG
This game concerns a decision situation in which you and another person we call “s/he”
(which will refer to a new person each round) separately and independently make decisions
called GUESSES. Together, your and her/his guesses determine the numbers of POINTS
that you and s/he earn in a round, which may be different. To choose your guesses, it
may help you to understand how your and her/his guesses will determine the numbers of
points that you and s/he earn in the decision situations. In each decision situation, each
person has her/his own TARGET, LOWER LIMIT and UPPER LIMIT. These targets and
limits may be different for you and her/him, and they may change from round to round.
Otherwise, the decision situations are identical in all 16 rounds. Your and her/his targets,
lower limits, and upper limits will be known to you and her/him every round. Both you and
s/he will receive the same instructions and have the same information about the decision
situations and the same access to your and her/his targets and limits. You (respectively,
s/he) can choose your (her/his) guesses only within your (her/his) given limits for each
round as explained below. After submitting guesses, you earn whichever is larger, ether 0
points or 200 points minus the distance between YOUR guess and the product of YOUR
11

--- Page 38 ---

target times HER/HIS guess, PLUS whichever is larger, either 0 points or 100 points minus
one-tenth (1/10th) the distance between YOUR guess and the product of YOUR target
times HER/HIS guess. S/he earns whichever is larger, either 0 points or 200 points minus
the distance between (1)HER/HIS guess and (2)the product of HER/HIS target times
YOUR guess, PLUS whichever is larger, either 0 points or 100 points minus one-tenth
(1/10th) the distance between (3)HER/HIS guess] and (4)the product of HER/HIS target
times YOUR guess. That is,
Points = max{0, 200 −distance} + max{0, 100 −0.1 ∗distance},
where distance is the absolute difference between Your guess and your Target*(His/Her
Guess)
This way of determining the number of points that you and s/he earn makes the number
you earn larger, the closer your guess is to your target times her/his guess; and it makes
the number s/he earns larger, the closer her/his guess is to her/his target times your guess.
Only the distance matters, NOT whether the difference is positive or negative. You earn
the same number of points when your guess is too high by a given amount as when it is too
low by the same amount. It is important to understand how your (respectively, her/his)
original guesses should be chosen to stay within your (her/his) limits. This will be done as
follows. If your original guess is below your lower limit, then your guess should be adjusted
UP to your LOWER limit; and if your original guess is above your upper limit, then your
guess should be adjusted DOWN to your UPPER limit. If, for example, your lower limit
is 400 and you original guess 300, then your adjusted guess is 400. If your upper limit
is original 600 and your guess 900, then your adjusted guess is 600. Her/his guesses are
adjusted up or down to her/his lower or upper limits in the same way, except that her/his
limits may be different. Remember you and s/he can choose any number within your and
her/his limits, respectively.
Suppose that:
Your Limits & Target are: Lower Limit = 200, Upper Limit = 600, Target = 1.2
Her/His Limits & Target are: Lower Limit = 400, Upper Limit = 800, Target = 0.8
1. If s/he guesses 500, which of your guesses earns you the most points? How many
points would you earn by entering that guess?
2. If you guess 400, which of her/his guesses earns her/him the most points? How
many points would s/he earn by entering that guess?
3. If s/he guesses 800, which of your guesses earns you the most points?
4. If your guess is 600, which of her/his guesses earns her/him the most points?
12

--- Page 39 ---

The following are the correct responses:
1. Answer = 600, Points = 300;
2. Answer = 400, Points = 212;
3. Answer = 600;
4. Answer = 480.
Each of these 4 questions are repeatedly asked in isolation with the same set of instructions
above (no history of previous answers for any of the questions).
LLMs were also asked the following questions (repeatedly, and in isolation) related to the
rules and the win conditions of the pBCG:
Rules for GG
1. What numbers can you choose between?
2. Do you earn more/fewer/the same points when your guess is too high or too low by
the same amount?
3. Will the targets, lower limits, and upper limits for each player be known to all players?
4. How many participants are there, including yourself?
5. Will decisions made in previous rounds have any effect on the current round?
B.2.3
MRG
BR for MRG
You are randomly matched to play a game against a human decision maker. In the game,
each of you chooses an integer between 11 and 20. Each participant will receive points
in the amount they have chosen.
A participant will receive an additional 20 points if
they choose a number exactly one less chosen by the other player. For example, if the
other participant chooses X, you will get (X-1)+20 points if you choose X-1 points. For
example, if your opponent chooses 14, you will get 33 points if you choose 13. Or, if the
other participant chooses 11, you will get 20 points if you choose 20.
1. Suppose your opponent chooses 15. What number from 11 to 20 earns you the
most?
2. Suppose your opponent chooses 11. What number from 11 to 20 earns you the
most?
The following are the correct responses:
1. Answer= 14;
2. Answer = 20.
13

--- Page 40 ---

BR for MRG (Game 3)
You are randomly matched to play a game against a human decision maker. In the game,
each of you chooses an integer between 11 and 20. If a participant chooses the number
20, they will receive 20 points (regardless of the other player’s choice). Otherwise, if a
participant chooses any other number in this range, they will receive three points less than
in the case where they choose 20. However, they will receive an additional amount of 20
points if they choose a number that is lower by exactly one than the number chosen by the
other player. For example, if the other participant chooses X, you will get 17+20 points
if you choose X-1. For example, if your opponent chooses 14, you will get 17+20 points
if you choose 13. Or, if the other participant chooses 11 points, you will get 20 points if
you choose 20.
1. Suppose your opponent chooses 15. What number from 11 to 20 earns you the
most?
2. Suppose your opponent chooses 11. What number from 11 to 20 earns you the
most?
The following are the correct responses:
1. Answer= 14;
2. Answer = 20.
Every question, for both games, is repeatedly asked in isolation with the same set of instruc-
tions above (no history of previous answers, for any of the questions).
For each of the games above, LLMs were also asked the following questions (repeatedly,
and in isolation) related to the rules and the win conditions of each game:
Rules for MRG
1. What numbers can you choose between?
2. How many participants are there, including yourself?
3. Suppose you choose 19 and the participant you have been matched with chooses 20.
How many points will you receive?
B.3
Prompts
To collect data, we use the respective application programming interfaces (API) with Python/R
from OpenAI, Anthropic, and Google. The exact model names of each LLM used are: gpt-
4, o1-preview-2024-09-12, claude-3-5-sonnet-20241022, claude-sonnet-4-20250514, gemini-1.5-
flash, gemini-2.0-flash-thinking-exp-1219. Each input prompt includes the specification of a
combination of three roles: a system role, an assistant, or a user. The system role is used
to guide the behavior of the LLM by providing high-level instructions and/or context. The
14

--- Page 41 ---

assistant refers to the LLM itself which generates responses for each input prompt. The user
role represents the queries or prompts that are used to interact with the LLM (i.e., with the
assistant). By repeated specifications of the assistant and user role within each input prompt,
we are able to, in effect, have a contextual conversation. For our purpose, each input prompt
will include a system role, which will be used to specify global instructions and context, and a
user role, which will specify the specific rules and the request for an answer for the pBCG.39
Once we knew LLMs had as good an understanding of the games as was naturally and
feasibly possible, given the above questions (particularly the best response questions), we
kept the wording of the prompts as close to the understanding questions. For completion, we
include all prompts below.
B.3.1
pBCG
As this is a completely standard game in the behavioral economics, instructions are based
closely on instructions from the literature.40 We avoid monetary payoffs as rewards to avoid
issues with incentives. We also provide examples in the instructions as LLMs had better
answers to the best responses understand questions (as this helps LLMs understand what
kind of calculations are involved).
B.3.2
1-shot pBCG
For the 1-shot pBCGs, the system prompt is
System
I want you to act as a human decision maker, You will be participating in 1 round of a
game. You should use your best judgment to come up with responses that you like most.
Always write your final answer in [ ].
This is identical for all 1-shot pBCG.
The following prompts include all the details of the pBCG for each condition, specified
by the user role.
User for 2-person (p=2/3)
Including yourself, there are 2 participants in total.
The other participant you will be
playing with is a human decision maker. All participants will be asked to pick a number
39Once interacted with the API using an input prompt, the answer provided by the LLM is always specified
by the assistant role.
40See Nagel (1995b); Ho, Camerer and Weigelt (1998); Bosch-Dom`enech et al. (2002); Weber (2003) and
numerous other papers for their accompanying instructions.
15

--- Page 42 ---

between 0 and 100 inclusive. The winner will be the one choosing the number closest to
2/3’s of the average of all the numbers provided by the participants (including your own).
For example, if you choose 10 and your opponent chooses 20, then you will be the winner,
as 10 is closer to 15(average)*2/3. Or, if you choose 30 and your opponent chooses 20,
your opponent will be the winner, as 20 is closer to 25(average)*2/3. In case of multiple
winners, only one participant will be randomly chosen to win. Now let’s start this game.
Please pick one number between 0 and 100 inclusive.
User for 11-person (p=1/2)
Including yourself, there are 11 participants in total. The other participant you will be
playing with are human decision makers. All participants will be asked to pick a number
between 0 and 100 inclusive. The winner will be the one choosing the number closest to
1/2 of the average of all the numbers provided by the participants (including your own).
For example, if you choose 14 and your opponents choose 10, 22, 23, 30, 11, 16, 37, 18,
19, 20, then the opponent with 10 will be the winner, as 10 is closer to 20(average)*1/2.
Or, if you choose 25 and your opponents choose 90, 100, 50, 20, 60, 80, 5, 70, 10, 40, then
you will be the winner, as 25 is closer to 50(average)*1/2. In case of multiple winners,
only one participant will be randomly chosen to win. Now let’s start this game. Please
pick one number between 0 and 100 inclusive.
User for Baseline: 11-person (p=2/3)
Including yourself, there are 11 participants in total. The other participants you will be
playing with are a human decision makers. All participants will be asked to pick a number
between 0 and 100 inclusive. The winner will be the one choosing the number closest to
2/3’s of the average of all the numbers provided by the participants (including your own).
For example, if you choose 14 and your opponents choose 10, 22, 23, 30, 11, 16, 37, 18,
19, 20, then you will be the winner, as 14 is closer to 20(average)*2/3. Or, if you choose
25 and your opponents choose 90, 100, 50, 20, 60, 80, 5, 70, 10, 40, then the opponent
with 40 will be the winner, as 40 is closer to 50(average)*2/3. In case of multiple winners,
only one participant will be randomly chosen to win. Now let’s start this game. Please
pick one number between 0 and 100 inclusive.
16

--- Page 43 ---

User for 11-person (p=4/3)
Including yourself, there are 11 participants in total. The other participants you will be
playing with are a human decision makers. All participants will be asked to pick a number
between 0 and 100 inclusive. The winner will be the one choosing the number closest to
4/3’s of the average of all the numbers provided by the participants (including your own).
For example, if you choose 14 and your opponents choose 10, 22, 23, 30, 11, 16, 37, 18,
19, 20, then the opponent with 30 will be the winner, as 30 is closer to 20(average)*4/3.
Or, if you choose 25 and your opponents choose 90, 100, 50, 20, 60, 80, 5, 70, 10, 40,
then the opponent with 70 will be the winner, as 70 is closer to 50(average)*4/3. In case
of multiple winners, only one participant will be randomly chosen to win. Now let’s start
this game. Please pick one number between 0 and 100 inclusive.
User for n-person (p=2/3)
The other participants you will be playing with are human decision makers. All participants
will be asked to pick a number between 0 and 100 inclusive. The winner will be the one
choosing the number closest to 2/3’s of the average of all the numbers provided by the
participants (including your own). For example, suppose there are 11 participants (including
yourself). In this situation, if you choose 14 and your opponents choose 10, 22, 23, 30,
11, 16, 37, 18, 19, 20, then you will be the winner, as 14 is closer to 20(average)*2/3.
Or, if you choose 25 and your opponents choose 5, 10, 20, 40, 50, 60, 70, 80, 90, 100,
then the opponent with 40 will be the winner, as 40 is closer to 50(average)*2/3. In case
of multiple winners, only one participant will be randomly chosen to win. Now let’s start
this game. Please pick one number between 0 and 100 inclusive.
User for Median
Including yourself, there are 11 participants in total. The other participants you will be
playing with are a human decision makers. All participants will be asked to pick a number
between 0 and 100 inclusive. The winner will be the one choosing the number closest to
2/3’s of the median of all the numbers provided by the participants (including your own).
For example, if you choose 14 and your opponents choose 10, 22, 23, 30, 11, 16, 37, 18,
19, 20, then the opponent with 11 will be the winner, as 11 is closer to 20(median)*2/3.
Or, if you choose 12 and your opponents choose 90, 100, 50, 20, 60, 80, 5, 70, 10, 40,
then the opponent with 40 will be the winner, as 40 is closer to 50(median)*2/3. In case
of multiple winners, only one participant will be randomly chosen to win. Now let’s start
17

--- Page 44 ---

this game. Please pick one number between 0 and 100 inclusive.
B.3.3
Repeated pBCG
For the repeated pBCG in which each of the LLMs play within a group of 10 other LLM
subjects of the same model, the system prompt is
System
I want you to act as a human decision maker, You will be participating in 10 rounds of
a game. All rounds are independent of each other meaning decisions made in each round
do not affect subsequent rounds. You should use your best judgment to come up with
responses that you like most. Always write your final answer in [ ].
For the first round, the user prompt is
User
Including yourself, there are 11 participants in total. The other participants you will be
playing with are human decision makers. For each round, you will play with the same set of
participants. All participants will be asked to pick a number between 0 and 100 inclusive.
The winner will be the one choosing the number closest to 4/3’s of the average of all the
numbers provided by the participants (including your own). For example, if you choose 14
and your opponents choose 10, 22, 23, 30, 11, 16, 37, 18, 19, 20, then the opponent with
30 will be the winner, as 30 is closer to 20(average)*4/3. Or, if you choose 25 and your
opponents choose 90, 100, 50, 20, 60, 80, 5, 70, 10, 40, then the opponent with 70 will
be the winner, as 70 is closer to 50(average)*4/3. In case of multiple winners, only one
participant will be randomly chosen to win. Now let’s start this game. After each round,
all participants will be told the average, and the target (4/3*average). You will also be
privately informed of whether you won or lost at the end of each round. Round 1. Please
pick one number between 0 and 100 inclusive.a
aThe same structure for the prompt is used for p=2/3, replacing the examples with the p=2/3
examples used as in the 1-shot pBCG case.
We keep the whole history for each LLM subject in subsequent rounds by adding to the
vector of messages (i.e., stacking messages) as the input to the API. After the user prompt
from the first round, the answer given by the LLM is added to the messages in the assistant
18

--- Page 45 ---

role.41 After this, as a user role message, we prompt with
User
In the previous round, the average was *average* and the target was *average*×p. You
*won /lost* in the previous round.
where *average*, target, and winning (or not) are calculated based on the LLM responses
given in the previous round. We then add another user role message with the prompt
User
Round 2. Please pick one number between 0 and 100 inclusive.
We repeat this process of messages, keeping the entire history of messages for each LLM
subject until round 10. Note that the history given to each LLM subject is specific to that
LLM subject; no other information is shared with other LLM subjects beyond the average and
the target. In this way, the system message, and the rules of the game are always contained
in the first 2 messages of the history, as well as the entire history of choices that each LLM
subject makes, with accompanying feedback, specific to each LLM subject.
B.3.4
GG
The instructions come directly from Costa-Gomes and Crawford (2006), with minimal mod-
ifications. The system prompt is
System
I want you to act as a human decision maker, You will be participating in 16 rounds of
a game. All rounds are independent of each other meaning decisions made in each round
do not affect subsequent rounds. You should use your best judgment to come up with
responses that you like most. Always write your final answer in [ ].
GG. For the first round, the user prompt is
User
In each round, you will be matched with one of the other participants, a new one in each
round. You will not know which of the other participants you are matched with, and the
other participants are human decision makers. Each round concerns a decision situation in
41It is trivial to extract the actual response given the system prompt requests that the final answer is given
in square brackets [].
19

--- Page 46 ---

which you and another person we call ‘s/he’ (which will refer to a new person each round)
separately and independently make decisions called GUESSES. Together, your and her/his
guesses determine the numbers of POINTS that you and s/he earn in a round, which may
be different. To choose your guesses, it may help you to understand how your and her/his
guesses will determine the numbers of points that you and s/he earn in the decision
situations. In each decision situation, each person has her/his own TARGET, LOWER
LIMIT and UPPER LIMIT. These targets and limits may be different for you and her/him,
and they may change from round to round. Otherwise, the decision situations are identical
in all 16 rounds. Your and her/his targets, lower limits, and upper limits will be known to
you and her/him every round. Both you and s/he will receive the same instructions and have
the same information about the decision situations and the same access to your and her/his
targets and limits. You (respectively, s/he) can choose your (her/his) guesses only within
your (her/his) given limits for each round as explained below. After submitting guesses,
you earn whichever is larger, ether 0 points or 200 points minus the distance between
YOUR guess and the product of YOUR target times HER/HIS guess, PLUS whichever is
larger, either 0 points or 100 points minus one-tenth (1/10th) the distance between YOUR
guess and the product of YOUR target times HER/HIS guess. S/he earns whichever is
larger, either 0 points or 200 points minus the distance between (1)HER/HIS guess and
(2)the product of HER/HIS target times YOUR guess, PLUS whichever is larger, either 0
points or 100 points minus one-tenth (1/10th) the distance between (3)HER/HIS guess
and (4)the product of HER/HIS target times YOUR guess. That is, Points = max0,200-
distance+max0,100-0.1*distance,where distance is the absolute difference between Your
guess and your Target*(His/Her Guess). This way of determining the number of points
that you and s/he earn makes the number you earn larger, the closer your guess is to your
target times her/his guess; and it makes the number s/he earns larger, the closer her/his
guess is to her/his target times your guess. Only the distance matters, NOT whether the
difference is positive or negative. You earn the same number of points when your guess
is too high by a given amount as when it is too low by the same amount. To pass the
Understanding Test and TO BE ABLE to participate in the experiment, it is important
to understand how your (respectively, her/his) original guesses should be chosen to stay
within your (her/his) limits. This will be done as follows. If your original guess is below
your lower limit, then your guess should be adjusted UP to your LOWER limit; and if your
original guess is above your upper limit, then your guess should be adjusted DOWN to
your UPPER limit. If, for example, your lower limit is 400 and you original guess 300, then
your adjusted guess is 400. If your upper limit is original 600 and your guess 900, then
your adjusted guess is 600. Her/his guesses are adjusted up or down to her/his lower or
20

--- Page 47 ---

upper limits in the same way, except that her/his limits may be different. Remember you
and s/he can choose any number within your and her/his limits, respectively. We are now
starting a new round of the game. Round 1: For this round your lower limit is *LLRound1
you
*,
your upper limit is *ULRound1
you
*, and your target is *targetRound1
you
*. Her/His lower limit is
*LLRound1
his/her *, her/his upper limit is *ULRound1
his/her *, and her/his target is *targetRound1
his/her *. Please
choose a number between your lower limit and upper limit.
Similar to the repeated pBCG, we keep the whole history for each LLM subject in subse-
quent rounds by adding to the vector of messages (i.e., stacking messages) as the input to the
API. After the user prompt from the first round, the answer given by the LLM is added to the
messages in the assistant role. Different from the pBCG, and consistent with Costa-Gomes
and Crawford (2006), we do no provide feedback to avoid repeated game effects. Therefore,
after the assistant message, as a user role message, we prompt with the next round
User
We are now starting a new round of the game.
Round 2: For this round your lower
limit is *LLRound2
you
*, your upper limit is *ULRound2
you
*, and your target is *targetRound2
you
*.
Her/His lower limit is *LLRound2
his/her *, her/his upper limit is *ULRound2
his/her *, and her/his target is
*targetRound2
his/her *. Please choose a number between your lower limit and upper limit.
We repeat this process of messages, keeping the entire history of messages for each LLM
subject until all 16 rounds are completed. Note that the history given to each LLM subject
is specific to that LLM subject; no other information is shared with other LLM subjects
beyond their history. In this way, the system message, and the rules of the game are always
contained in the first 2 messages of the history, as well as the entire history of choices that
each LLM subject makes.
B.3.5
MRG
The instructions come directly from Arad and Rubinstein (2012), with minimal modifications.
Similarly, we avoid monetary payoffs as rewards to avoid issues with incentives. We also
provide examples in the instructions as LLMs had better answers to the best responses
understand questions (as this helps LLMs understand what kind of calculations are involved).
The system prompt is
21

--- Page 48 ---

System
I want you to act as a human decision maker, You will be participating in 1 round of a
game. You should use your best judgment to come up with responses that you like most.
Always write your final answer in [ ].
This is identical for both MRG and MRG (Game 3). The following prompts include all the
details for MRG and MRG (Game 3), specified by the user role.
User for MRG
You are randomly matched to play a game against a human decision maker. In the game,
each of you chooses an integer between 11 and 20. Each participant will receive points
in the amount they have chosen.
A participant will receive an additional 20 points if
they choose a number exactly one less chosen by the other player. For example, if the
other participant chooses X, you will get (X-1)+20 points if you choose X-1 points. For
example, if your opponent chooses 14, you will get 33 points if you choose 13. Or, if the
other participant chooses 11, you will get 20 points if you choose 20. You will receive
your points without knowing against whom you played. Now let’s start this game. What
number do you choose?
User for MRG (Game 3)
You are randomly matched to play a game against a human decision maker. In the game,
each of you chooses an integer between 11 and 20. If a participant chooses the number
20, they will receive 20 points (regardless of the other player’s choice). Otherwise, if a
participant chooses any other number in this range, they will receive three points less than
in the case where they choose 20. However, they will receive an additional amount of 20
points if they choose a number that is lower by exactly one than the number chosen by the
other player. For example, if the other participant chooses X, you will get 17+20 points if
you choose X-1. For example, if your opponent chooses 14, you will get 17+20 points if
you choose 13. Or, if the other participant chooses 11 points, you will get 20 points if you
choose 20. You will receive your points without knowing against whom you played. Now
let’s start this game. What number do you choose?
22

--- Page 49 ---

B.4
Estimation Details
B.4.1
pBCG
From the theoretical predictions, we apply standard practice maximum likelihood estimation
(MLE) to estimate parameters for both the level-k model and the CH model. For the level-k
model, we estimate the proportion of responses that align with the L0, L1, L2, L3, L4, and
L∞(Nash) predictions.
L0 also accommodates behavior which is not precisely predicted
by the level-k (or CH model) for levels (steps) higher than L1 (step-1), i.e., the L0 type
captures all responses from a type who chooses uniformly randomly from the integers 0 to
100, but is not in the proximity of any prediction from any other higher type. This allows
us to accommodate behavior which is not in the neighborhood of the predictions of any of
the level-k types (up to a finite k).42 For each type, we assume that a choice is the best
guess limited by their type, plus an independent and identically distributed (i.i.d) error term.
Specifically, assuming the error term is i.i.d binomially distributed, the observed choice of a
level-k type by an individual, i, is given by Yi = lk +ϵi, with ϵi ∼B(α, β) such that E[ϵi] = 0,
and Var[ϵi] = σ2. With ϵi ∈R and ϵi = Yi −lk, this allows to define a density for each of
these types:
hk(ϵi) =









α
ϵi

βϵi(1 −β)α−ϵi
k ∈{1, ..., K, ∞},
1
101
k = 0.
Let K denote the space of types, i.e., K = {0, ..., K, ∞}. Define proportions of types by
F = {fk}k∈K, where fk is the proportion of level-k types. Defining our complete parameter
space as Θ = (F, α, β) with α, β being the nuisance parameters, the log-likelihood function
for a random sample of guesses, Y = Yi∈{1,...,N} is:
log L(Θ|Y) =
n
X
i=1
ln
 X
k∈K
fk · hk(ϵi)
!
.
The purpose of assuming a binomially distributed random error is to allow for discrete-
valued errors, in essence, we use a discretized normal distribution centered around 0 (with
its limit being a normal distribution). We estimate level-k model with 6 levels of reasoning
42The goal of MLE is to find the parameter values that maximize the product of the individual likelihoods,
based on a (probabilistic) matching of the theoretical predictions and the observed strategies. However, an
action predicted to occur with zero probability results in a likelihood contribution of zero, rendering the overall
likelihood function zero. Such an event, even if it occurs for only one observation, can obscure the predictive
accuracy of any model. To avoid the zero-likelihood problem, we introduce a type that randomizes across all
possible strategies, ensuring that no action is chosen with zero probability, as described in Moffatt (2015) and
footnote 2 of Camerer, Ho and Chong (2004).
23

--- Page 50 ---

by setting K = 4 with the best guess for the L∞type being the Nash equilibrium, the L0
type being a uniform randomizer, and the remaining best guesses being determined by the
theoretical predictions above.
For the CH model, τ is estimated, which represents the mean (and variance) of the
frequency distribution of step-k types.
τ parameterizes the proportion of responses that
align with step-k (for k ∈{0, ..., K}) and step-∞predictions.
The structure of the log-
likelihood function is identical to the one used to estimate the level-k model, with choices
also modeled as noisy best guesses in the same way as above. The differences only lie in 1)
the proportions of types are now determined by a Poisson distribution, i.e., the distribution
of types is given by f(k; τ), and 2) the best guesses are made by assuming a distribution
over lower step-k, determined by the conditional Poisson distribution {fk(j; τ)}j=0,1,...,k−1,
i.e., with ϵi ∈R and Yi = sk(τ) + ϵi. This structure is identical to the level-k model except
we replace the level-k best guess, lk, with the CH model best guess, sk(τ).
Let K denote the space of types, i.e., K = {0, ..., K, ∞}. Define proportions of types by
{f(k; τ)|k ∈K}, where f(k; τ) is the proportion of step-k types, given τ.43 The complete
parameter space is Θ = (τ, α, β) with α, β being the nuisance parameters, hence, the log-
likelihood function for a random sample of guesses, Y = Yi∈={1,...,N} is:
log L(Θ|Y) =
n
X
i=1
ln

X
j∈K
f(τ; k) · hk(ϵi)

.
Although the log-likelihood function is of the same structure, estimation is vastly different
as the CH model is fully determined by the value of τ, i.e., finding the value of τ that
maximizes the log-likelihood. For consistency, we estimate using the same number of step-k
type players as there are level-k type players.44
B.4.2
GG
Following the theoretical predictions, we use similar MLE techniques to estimate parameters
for both the level-k model and the CH model. The notable difference here is that we collect
data sequentially for the 16 rounds of the GG. For each LLM, we collect these set of responses
100 times (i.e., for each LLM, there are 100 LLM subjects playing 16 rounds of the GG
sequentially). With these data, for the level-k model, we are able to estimate the proportion of
responses that align with the L0, L1, L2, L3, L4, and L∞(Nash) predictions on an individual-
response level. We do this because each round has its own different set of predictions (level-k,
43f0 is still parameterized by τ by the law of total probability.
44Note that α and β are simply noise parameters for the estimation in the binomial distribution, with no
mapping to the theoretical models, as such, they are nuisance parameters.
24

--- Page 51 ---

CH, Nash), so we need not base the estimation on aggregate responses, as done in the pBCG.45
The observed (noisy) choice of a level-k type by an individual, i, for each round, r, is
given by Y r
i = lr
k + ϵr
i , with ϵr
i ∼B(αr, βr) such that E[ϵr
i ] = 0, and Var[ϵr
i ] = (σr)2. With
ϵr
i ∈R and ϵr
i = Y r
i −lr
k, this allows to define a density for each of these types:
hr
k(ϵi) =











αr
ϵr
i

βϵr
i (1 −β)αr−ϵr
i
k ∈{1, ..., K, ∞},
1
br
i −ar
i
k = 0.
Depending on the parameters of the GG, the level of reasoning required to reach the
L∞prediction can be fewer than K(> 1). In these cases, we assume the response is only
consistent with the L∞(and L0) type. Formally, for any k ∈{1, ..., K} and lr
k = lr
∞, set
hr
j(ϵi) = 0, for j ≤k, with hr
∞(ϵi) and hr
0(ϵi) defined as above.46
Let K denote the space of types, i.e., K = {0, ..., K, ∞}. Define proportions of types by
F = {fk}k∈K, where fk is the proportion of level-k types. Defining our complete parameter
space as Θ = (F, α, β) with α, β collecting nuisance parameters in vectors, the log-likelihood
function for a random sample of guesses, Yi = Yi,r∈{1,...,16} is:
log L(Θ|Yi) =
16
X
r=1
ln
 X
k∈K
fk · hr
k(ϵi)
!
.
Notice this is virtually identical to the MLE used in the pBCG except we use data collected
for all rounds per LLM subject to estimate the level-k model, rather than aggregating over
all the data collected. In this way, we can estimate the level-k model for each LLM subject.
As we estimate up to L4, including L0 and L∞, we set K = 4.
For the CH model, τ is estimated in an analogous way. Define proportions of types in
each round by {f(k; τ)|k ∈{0, ..., K, ∞}}, where f(k; τ) is the proportion of step-k types,
given τ, with ϵr
i ∈R and Y r
i = sr
k(τ) + ϵr
i . As before we impose that, for any k ∈{1, ..., K}
and lr
k = lr
∞, set hr
j(ϵi) = 0, for j ≤k, with hr
∞(ϵi) and hr
0(ϵi) defined as above. The complete
parameter space is Θ = (τ, α, β) with α, β collecting nuisance parameters in vectors, hence,
the log-likelihood function for a random sample of guesses, Yi = Yi,r∈{1,...,16} is:
45Naturally, another way to approach the estimation is to aggregate the data for each round, and estimate
the model for each of the 16 rounds of the GG, as if each round is their own one-shot game. However, this
does not make use of the sequential nature in which the GG is played in Costa-Gomes and Crawford (2006),
which we attempt to stay as close to as possible, in terms of experimental design.
46While the majority of the mass goes to the L∞proportion when the response is close to the L∞prediction,
we still allow for random behavior.
25

--- Page 52 ---

log L(Θ|Yi) =
16
X
r=1
ln
 X
k∈K
f(τ; k) · hr
k(ϵi)
!
.
Again, the log-likelihood function is of the same structure with vastly different estimation
as the CH model is fully determined by τ, separately for each LLM subject. For consistency,
we estimate using the same number of step-k type players as there are level-k type players.47
B.4.3
MRG
Estimation. Similarly, from the theoretical predictions, we apply MLE to estimate parame-
ters for both the level-k model and the CH model analogously to what was done for the pBCG
and GG. We keep the same number of levels/steps as the pBCG but replace L∞with L4,
as there is no pure Nash equilibrium. We still accommodate behavior which is not predicted
by the level-k or CH model by including a purely random type. However, as L0 behavior
can be very distinct from purely random behavior, we specifically distinguish between these
two types. Another reason for doing this is to allow for the uniform randomization choice
(15), and lower choices, to be considered as random behavior, rather than a very high stage
of reasoning.48 Estimation is done separately for each of MRG, and MRG (Game 3).
Given the finite nature of the actions in MRG and MRG (Game 3), applying MLE to
estimate the parameters for the level-k model and the CH model is simple and standard.
For the level-k model, we estimate the proportion of levels that are consistent with purely
random behavior, L0, L1, L2, L3, and L4 predictions. Let K denote the space of types, i.e.,
K = {random, 0, 1, ..., K}. We define the density for each type as follows:
hk(Yi) =







1[Yi = lk]
k ∈{0, ..., K},
1
10
k = {random}.
where 1[Yi = lk] is an indicator function which takes 1 when Yi = lk and 0 otherwise.
Define proportions of types by F = {fk}k∈K, where fk is the proportion of each type. We
set K = 4 to estimate 6 levels of reasoning (including L0, and purely random type). The
parameter space is simply Θ = F and the log-likelihood function for a random sample of
47Note that α and β are again (vectors of) noise parameters for the estimation in the binomial distribution,
with no mapping to the theoretical models.
48This is consistent with the empirical results in Arad and Rubinstein (2012) with virtually no subject
choosing lower than 15.
26

--- Page 53 ---

guesses, Y = Yi∈{1,...,N} is:
log L(Θ|Y) =
n
X
i=1
ln
 X
k∈K
fk · hk(Yi)
!
.
For the CH model, we estimate τ to parameterize the proportion of responses that align
with step-k, for k ∈{random, 0, 1, ..., K}, to be consistent with the level-k model. As before,
the proportions of types are determined by a Poisson distribution with best responses as given
above in the theoretical predictions. Define proportions of types by {f(k; τ)|k ∈K} where
f(k; τ) is the proportion of step-k types, given τ. The parameter space is simply Θ = {τ}
and the log-likelihood function for a random sample of guesses, Y = Yi∈{1,...,N} is:
log L(Θ|Y) =
n
X
i=1
ln
 X
k∈K
f(k; τ) · 1[Yi = sk(τ)]
!
.
As with the pBCG and GG, the log-likelihood function is of the same structure between
models, with different estimation, given the way that the proportions are parameterized. For
consistency, the same number of step-k players is used as there are level-k players.
B.5
Temperature
The temperature parameter influences outputs in terms of randomness and creativity. A
lower temperature value results in more predictable and deterministic responses, in favor
of words with the highest probabilities. Conversely, a higher temperature results in more
diverse and novel responses by increasing the chance of less likely words. In line with studies
exploring the impact of temperature settings on LLM behavior (Loya, Sinha and Futrell,
2023; Binz and Schulz, 2023; Zhu et al., 2024), every condition mentioned is also tested at 3
temperature levels. The baseline is set at a moderate temperature of 0.5 to ensure the most
balanced approach.
We have higher (0.75) and lower (0.25) temperature level conditions
to examine how variations in randomness influence (observed) strategic sophistication. The
exception is with GPT-o1 as at the time of collecting the data (October 2024) varying the
temperature parameter was not available. Given the results of the baseline (for all games)
and as we only use GPT-o1, Cl-3S, and Ge-2T for the GG, we did not run the GG with
different temperatures. Given the results from the level-k model have very little variation
across temperature, the CH model estimates also do not vary much from baseline temperature
either.
27

--- Page 54 ---

B.5.1
pBCG
For all conditions (baseline and alternate), we collect data varying the temperature to deter-
mine whether there is any impact on LLM responses. Overall, the results remained largely
consistent with those observed at the baseline temperature. The only differences of note
occurred in the higher temperature condition, in which there was an increase in incoherent
answers, and a slight rise in the variation of responses.49 Analogously, for lower temperatures,
the modal responses became somewhat more modal, as expected with more deterministic
results. However, the estimates of either model remain relatively unchanged. This consis-
tency across different temperatures suggests that strategic sophistication of LLMs is robust
to changes in temperature. We present the results for the different temperature conditions
below.
n=2
n = Unspecified
Median
p=2/3 (baseline)
p=1/2
p=4/3
0.0
0.2
0.4
0.6
0.8
1.0
0.0
0.2
0.4
0.6
0.8
1.0
0.0
0.2
0.4
0.6
0.8
1.0
L∞
L4
L3
L2
L1
L0
L∞
L4
L3
L2
L1
L0
L∞
L4
L3
L2
L1
L0
L∞
L4
L3
L2
L1
L0
L∞
L4
L3
L2
L1
L0
L∞
L4
L3
L2
L1
L0
Average Proportions
Human Subjects
Gemini-2.0 Flash (Thinking)
Gemini-1.5 Flash
Claude-4 (Sonnet Thinking)
Claude-3.5 (Sonnet)
OpenAI-o1
ChatGPT-4
Figure B2: Estimates of the proportions of level-k types for the pBCG with high tempera-
ture.
49We still maintain the planned sample size after dropping incoherent answers.
28

--- Page 55 ---

n=2
n = Unspecified
Median
p=2/3  (baseline)
p=1/2
p=4/3
0.0
0.2
0.4
0.6
0.8
1.0
0.0
0.2
0.4
0.6
0.8
1.0
0.0
0.2
0.4
0.6
0.8
1.0
L∞
L4
L3
L2
L1
L0
L∞
L4
L3
L2
L1
L0
L∞
L4
L3
L2
L1
L0
L∞
L4
L3
L2
L1
L0
L∞
L4
L3
L2
L1
L0
L∞
L4
L3
L2
L1
L0
Average Proportions
Human Subjects
Gemini-2.0 Flash (Thinking)
Gemini-1.5 Flash
Claude-4 (Sonnet Thinking)
Claude-3.5 (Sonnet)
OpenAI-o1
ChatGPT-4
Figure B3: Estimates of the proportions of level-k types for the pBCG with low temperature.
29

--- Page 56 ---

0
10
20
30
40
50
60
70
80
90
100
1
2
3
4
5
6
7
8
9
10
Round
Average
p = 2/3
0
10
20
30
40
50
60
70
80
90
100
1
2
3
4
5
6
7
8
9
10
Round
Average
p = 4/3
Gemini-2.0 Flash (Thinking)
Gemini-1.5 Flash
Claude-4 (Sonnet Thinking)
Claude-3.5 (Sonnet)
OpenAI-o1
ChatGPT-4
Figure B4: Time series of responses for multiple rounds pBCG with high temperature. This
figure consists of two figures for p = 2/3 and p = 4/3, respectively. Each figure shows the
average responses in each round for each LLM. Vertical bars are 95% confidence intervals
30

--- Page 57 ---

0
10
20
30
40
50
60
70
80
90
100
1
2
3
4
5
6
7
8
9
10
Round
Average
p = 2/3
0
10
20
30
40
50
60
70
80
90
100
1
2
3
4
5
6
7
8
9
10
Round
Average
p = 4/3
Gemini-2.0 Flash (Thinking)
Gemini-1.5 Flash
Claude-4 (Sonnet Thinking)
Claude-3.5 (Sonnet)
OpenAI-o1
ChatGPT-4
Figure B5: Time series of responses for multiple rounds pBCG with low temperature. This
figure consists of two figures for p = 2/3 and p = 4/3, respectively. Each figure shows the
average responses in each round for each LLM. Vertical bars are 95% confidence intervals
31

--- Page 58 ---

B.5.2
MRG
Level-4
Level-3
Level-2
Level-1
Level-0
Random
0.0
0.2
0.4
0.6
0.8
1.0
Average Proportions
Level-4
Level-3
Level-2
Level-1
Level-0
Random
0.0
0.2
0.4
0.6
0.8
1.0
Average Proportions
Human Subjects
Gemini-2.0 Flash (Thinking)
Gemini-1.5 Flash
Claude-4 (Sonnet Thinking)
Claude-3.5 (Sonnet)
OpenAI-o1
ChatGPT-4
Figure B6: Estimates of the proportions of level-k types for MRG, and MRG (Game 3)
with high temperature.
Level-4
Level-3
Level-2
Level-1
Level-0
Random
0.0
0.2
0.4
0.6
0.8
1.0
Average Proportions
Level-4
Level-3
Level-2
Level-1
Level-0
Random
0.0
0.2
0.4
0.6
0.8
1.0
Average Proportions
Human Subjects
Gemini-2.0 Flash (Thinking)
Gemini-1.5 Flash
Claude-4 (Sonnet Thinking)
Claude-3.5 (Sonnet)
OpenAI-o1
ChatGPT-4
Figure B7: Estimates of the proportions of level-k types for MRG, and MRG (Game 3)
with low temperature.
32

```
