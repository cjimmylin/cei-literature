---
title: "2025-Fontana-Nicer Than Humans How Do Large Language Models Behave in the - PDF Extract"
source_pdf: "2025-Fontana-Nicer Than Humans How Do Large Language Models Behave in the.pdf"
pages: 14
extracted_at: "2026-02-07T17:00:46.494367"
---

# PDF Extract: 2025-Fontana-Nicer Than Humans How Do Large Language Models Behave in the

**Source PDF:** 2025-Fontana-Nicer Than Humans How Do Large Language Models Behave in the.pdf
**Total Pages:** 14

---

## Content

```
--- Page 1 ---

Nicer Than Humans: How do Large Language Models Behave in the Prisoner’s
Dilemma?
Nicol´o Fontana1, Francesco Pierri1, Luca Maria Aiello2,3
1Politecnico di Milano, Italy
2IT University of Copenhagen, Denmark
3Pioneer Centre for AI, Denmark
nicolo.fontana@mail.polimi.it, francesco.pierri@polimi.it, luai@itu.dk
Abstract
The behavior of Large Language Models (LLMs) as artifi-
cial social agents is largely unexplored, and we still lack ex-
tensive evidence of how these agents react to simple social
stimuli. Testing the behavior of AI agents in classic Game
Theory experiments provides a promising theoretical frame-
work for evaluating the norms and values of these agents
in archetypal social situations. In this work, we investigate
the cooperative behavior of three LLMs (Llama2, Llama3,
and GPT3.5) when playing the Iterated Prisoner’s Dilemma
against random adversaries displaying various levels of hos-
tility. We introduce a systematic methodology to evaluate an
LLM’s comprehension of the game rules and its capability to
parse historical gameplay logs for decision-making. We con-
ducted simulations of games lasting for 100 rounds and an-
alyzed the LLMs’ decisions in terms of dimensions defined
in the behavioral economics literature. We find that all mod-
els tend not to initiate defection but act cautiously, favoring
cooperation over defection only when the opponent’s defec-
tion rate is low. Overall, LLMs behave at least as coopera-
tively as the typical human player, although our results indi-
cate some substantial differences among models. In particu-
lar, Llama2 and GPT3.5 are more cooperative than humans,
and especially forgiving and non-retaliatory for opponent de-
fection rates below 30%. More similar to humans, Llama3
exhibits consistently uncooperative and exploitative behavior
unless the opponent always cooperates. Our systematic ap-
proach to the study of LLMs in game theoretical scenarios is
a step towards using these simulations to inform practices of
LLM auditing and alignment.
1
Introduction
Large Language Models (LLMs) can operate as social
agents capable of complex, human-like interactions (Park
et al. 2023). Their integration into online social platforms
is unfolding rapidly (Cao et al. 2023; Yang and Menczer
2023), presenting severe risks (Floridi and Chiriatti 2020;
Ferrara 2024) as well as intriguing opportunities (Dafoe
et al. 2020; Breum et al. 2023). To understand and antic-
ipate the behavioral dynamics that may arise from the in-
teraction between artificial agents and humans, it is essen-
tial to first study how these agents react to simple social
stimuli (Bail 2024). Behavioral economics experiments, par-
ticularly those grounded in Game Theory, provide an ideal
ground for testing the responses of AI agents to archety-
pal social situations (Horton 2023). These experiments typ-
ically involve goal-oriented scenarios where multiple ‘play-
ers’ engage in a series of repeated interactions (Osborne
and Rubinstein 1994). To optimize for the goal, the deci-
sions taken at each round must strategically account for the
anticipated actions of the other players. However, the deci-
sions of human participants often deviate from the theoret-
ically optimal strategies due to the influence of social and
psychological factors that conflict with the game’s objec-
tives (Camerer 1997). Similarly, given that LLMs are com-
putational models built upon collective human knowledge
and culture (Schramowski et al. 2022), observing their be-
havior in classic iterated games could shed light on the so-
cial norms and values that these models reflect, as well as
their capability in reasoning, planning, and collaborating in
social settings.
Early interdisciplinary research has explored the use of
LLMs within the context of classical economic games (see
Related Work). While highly valuable, all these studies ex-
hibit at least one of the following limitations. First, they
generally lack prompt validation procedures, leading to an
implicit assumption that LLMs can understand the complex
rules of the game and the history of past actions described
in the prompt (Akata et al. 2023; Mao et al. 2023; Mei et al.
2024). Second, the duration of simulated games is often lim-
ited to a few rounds (Akata et al. 2023; Brookins and De-
Backer 2023; Fan et al. 2023; Guo 2023; Xu et al. 2023),
hampering the LLMs’ ability to discern the decision-making
patterns of other participants – a phenomenon we show
in our own experiments. Third, the initialization of LLMs
with predefined ‘personas’ tends to skew their responses to-
wards pre-determined behaviors, such as altruism or selfish-
ness (Brookins and DeBacker 2023; Fan et al. 2023; Guo
2023; Horton 2023; Lor`e and Heydari 2023; Phelps and
Russell 2023). This approach limits the exploration of the
LLMs’ baseline behavior, which is crucial for understanding
their inherent decision-making processes. Last, the evalua-
tion of simulation outcomes has predominantly focused on
the quantitative analysis of decision types (e.g., frequency
of cooperation), overlooking the LLMs’ higher-level behav-
ioral patterns that can be inferred from the temporal evolu-
tion of these decisions (Xu et al. 2023; Mao et al. 2023). The
combined effect of these limitations has led to findings that
are sometimes inconclusive (Brookins and DeBacker 2023;
Mao et al. 2023) and contradictory (Akata et al. 2023; Fan
arXiv:2406.13605v2  [cs.CY]  19 Sep 2024

--- Page 2 ---

et al. 2023), calling for more systematic evidence on the be-
havior of LLMs in iterated games.
In this work, we investigate the adaptability of LLMs
in terms of their cooperative behavior when facing a spec-
trum of hostility in an iterated game scenario. We evaluate
Llama2 (Touvron et al. 2023), Llama3, and GPT3.5 (Brown
et al. 2020) in the Iterated Prisoner’s Dilemma (Osborne and
Rubinstein 1994) against adversaries with different propen-
sities for betrayal. Our contribution is threefold. First, we in-
troduce a meta-prompting technique designed to evaluate an
LLM’s comprehension of the game’s rules and its ability to
parse historical gameplay logs for decision-making. Second,
we conduct extensive simulations over 100 rounds and deter-
mine the optimal memory span that enables the LLMs to ad-
here to the strategic framework of the game. Third, we ana-
lyze the behavioral patterns exhibited by the LLMs, aligning
them with the core dimensions and strategies delineated in
Robert Axelrod’s influential research on the evolution of co-
operation within strategic interactions (Axelrod and Hamil-
ton 1981).
We observe that, overall, the three models tend to be more
cooperative than humans, but they display some variability
in their strategies. This variability persists even when the
models are exposed to the same environment, game, and task
framing. Both Llama2 and GPT3.5 displayed a more marked
propensity towards cooperation than what existing literature
reports about human players, indicating a favorable align-
ment with positive values. In contrast, Llama3 adopts a more
strategic and exploitative approach that is more similar to
that of humans. This approach may be advantageous in com-
petitive scenarios where raw performance is critical, but it
can be a disadvantage when it comes to aligning with posi-
tive values.
Overall, our work contributes to defining a more princi-
pled approach to using LLMs for iterated games. It makes
a step towards a more systematic way to use simulations of
game theoretical scenarios to probe the inherent social bi-
ases of LLMs, which might prove useful for LLM auditing
and alignment (Shen et al. 2023; M¨okander et al. 2023).
2
Background on Prisoner’s Dilemma
2.1
Game Setup
The Prisoner’s Dilemma is a classic thought experiment in
Game Theory. It serves as a paradigm for analyzing conflict
and cooperation between two players (Tucker and Straffin Jr
1983). In the game, the two players cannot communicate,
and must independently choose between two actions: Co-
operate, or Defect. Once both players have chosen their ac-
tions, payoffs are distributed based on the resulting combi-
nation of their choices. Mutual cooperation yields a reward
R for each player. If one defects while the other cooper-
ates, the defector receives a higher ‘temptation’ payoff T,
while the cooperating player incurs a lower ‘sucker’s’ pay-
off S. If both parties choose to defect, they each receive a
punishment payoff P for failing to cooperate. The classi-
cal structure of the game is defined by the payoff hierarchy
T > R > P > S, which theoretically incentivizes rational
players to consistently choose defection as their dominant
strategy (Axelrod 1981). In the iterated version of the game,
multiple rounds are played, and the payoffs are revealed to
the players at every round (Tucker and Luce 1959). The it-
erative nature of the game allows the players to consider
past outcomes to strategically inform future actions. When
humans play the game, psychological factors such as repu-
tation and trust significantly influence the decision-making
process, often leading to higher rates of cooperation than
would be expected from purely rational agents (Dal B´o and
Fr´echette 2011; Romero and Rosokha 2018).
2.2
Strategies
In the Iterated Prisoner’s Dilemma (IPD), a strategy refers
to an algorithm that a player uses to decide their next action,
taking into account the historical context of the game (Kuhn
2019). No single strategy universally outperforms all oth-
ers; however, some are more effective against a broader va-
riety of opposing strategies (Dal B´o and Fr´echette 2011).
This concept was demonstrated in 1980 by Robert Axel-
rod (Axelrod 1980), who ran an IPD tournament with mul-
tiple competing strategies. Follow-up tournaments have fur-
ther diversified the range of strategies (Stewart and Plotkin
2012). Considering previous literature (Fudenberg, Rand,
and Dreber 2012; Dal B´o and Fr´echette 2011; Romero and
Rosokha 2018), we consider the strategies that better repre-
sent the ones adopted by humans, covering more than 75%
of the experimental samples in those studies. Those strate-
gies are the following:
• Always Cooperate (AC).
• Always Defect (AD).
• Random (RND). Chooses Cooperate or Defect at random
with equal probability at each round.
• Unfair Random (URNDp). Variation of Random where
the probability of choosing to Cooperate is p.
• Tit For Tat (TFT). Starts with Cooperation in the first
round, then mimics the opponent’s previous action
throughout the game.
• Suspicious Tit For Tat (STFT). A TFT strategy that be-
gins with Defect in the first round.
• Grim Trigger (GRIM). Chooses Cooperate until the oppo-
nent defects, then chooses only Defect for the rest of the
game.
• Win–Stay Lose–Shift (WSLS). Repeats the previous ac-
tion if it resulted in the highest payoffs (R or T), otherwise
changes action.
Tit For Tat emerged as the winning strategy in Axelrod’s
tournament. It is commonly observed that human players
tend to favor straightforward strategies such as AD, TFT, or
GRIM (Romero and Rosokha 2018). To describe the LLM
behavior in terms of these known strategies, in our exper-
iments we calculate the similarity of the LLM’s game se-
quences with the sequences that these hardcoded strategies
would generate when playing against the same opponent.
2.3
Behavioral Dimensions
To identify the defining factors of different strategies, we
combine dimensions already defined in prior studies that

--- Page 3 ---

quantify salient behavioral properties of players based on the
observed game sequences (Axelrod 1980; Mei et al. 2024):
• Nice. Propensity to not be the first to defect. For a single
instance of the Iterated Prisoner’s Dilemma, it is defined
as 1 if the player is not the first to defect, 0 otherwise.
• Forgiving. Propensity to cooperate again after an oppo-
nent’s defection, defined as:
#forgiven defection
#opponent defection+#penalties,
where the number of penalties corresponds to the times
that, after defecting, the opponent sought forgiveness by
cooperating and the player did not forgive them, thus
keeping defecting.
• Retaliatory. Propensity of defecting immediately after an
opponent’s uncalled defection, defined as:
#reactions
#provocations
• Troublemaking. Propensity to defect unprovoked, defined
as a counterpart of being retaliatory:
#uncalled defection
#occasions to provoke,
where an uncalled defection is a defection following a co-
operation (or being the first action of the game) and an
occasion to provoke is any cooperation from the opponent
in the previous round.
• Emulative. Propensity to copy the opponent’s last move:
#mimic
N−1 , where a mimic occurs any time the player played
the same action that the opponent played in the previous
round and N is the number of iterations of the game.
Strategies that are Nice, Forgiving, and Retaliatory (e.g.,
TFT) perform best against a wide variety of opponents.
Human players tend to be particularly uncooperative when
faced with games where the reward R for cooperating is
much lower than the temptation T to betray the other player.
In the indefinitely iterated version of the Prisoner’s Dilemma
with a fixed probability at every round for the game to ter-
minate, human subjects tend to be more cooperative when
the probability of ending the game is low. Usually, in games
with a low chance of continuation and a big gap between R
and T, the majority of the strategies adopted are most simi-
lar to Always Defect (70% to 90%); in games with a longer
potential time horizon and R closer to T, humans tend to be
more forgiving and Tit For Tat explains a larger portion of
the subjects’ strategies (Dal B´o and Fr´echette 2011).
3
Experimental Design
3.1
LLM Setup
In our experiments, we use Llama-2-70b-chat-hf
and Llama-3-70B-Instruct as open-source language
models developed by Meta and released under commercial
use licenses1,2. We access these models through the Hug-
ging Face platform, using their Inference API3. As a closed-
source language model, we use GPT-3.5-Turbo, devel-
oped and hosted by OpenAI, accessed via their proprietary
API4. GPT3.5 has been used in many early experiments on
LLM agents in game-theoretical scenarios (Mei et al. 2024;
Lor`e and Heydari 2023; Xu et al. 2023).
1https://ai.meta.com/llama/license/
2https://llama.meta.com/llama3/license/
3https://huggingface.co/inference-api/serverless
4https://openai.com/index/openai-api/
The models are initialized with a temperature value of 0.7,
that is equal to the default value for GPT models and is con-
sistent with previous studies using models from the Llama
family (Lor`e and Heydari 2023; Xu et al. 2023). An analysis
of robustness to different temperature settings (0.1 and 1.0)
is provided in the Appendix (Figure A9).
We make the LLMs play a series of Iterated Prisoner’s
Dilemma games, each consisting of N = 100 rounds. Due
to the stochastic nature of the responses that LLMs generate,
we repeat each game k = 100 times and report the average
results along with 95% confidence intervals. To evaluate the
models’ adaptability to different degrees of environmental
hostility, we repeat the experiment by matching them against
URNDp opponents (defined in §2.2) with varying probabil-
ity of cooperation α ∈[0, 1]. The final outcome of each
game is a sequence containing pairs of binary values repre-
senting the actions of the LLM (player A) and the opponent
(player B) at each round i:
Gα
k = [(Ai, Bi)]i∈[1,N].
(1)
From the Gα
k sequence, we extract the empirical probability
of the LLM to cooperate at round i, calculated as the fraction
of ith rounds in which the LLM cooperated over k trials:
pα
coop(i) = 1
k
X
k
Gα
k(Ai).
(2)
We calculate the average cooperation probability throughout
a game by averaging pα
coop(i) over all N rounds:
pα
coop = 1
N
N
X
i=1
pα
coop(i).
(3)
3.2
Prompting
To implement the game, we design a fixed system prompt
that outlines the game’s rules, including the payoff structure,
and the player’s objective to ‘get the highest possible number
of points in the long run’. The variable part of the prompt in-
cludes the memory of the game, namely a log of the history
of the players’ actions up to the current round, along with
instructions for generating the next action. The complete
prompt can be found in the Appendix (Figures A1, A2, and
A3). In iterated games, the information from earlier rounds
is essential for a player to deduce the opponent’s strategy,
and adapt accordingly. Early research involving LLMs in it-
erated games experimented with a limited number of rounds,
precluding any analysis of how the size of the memory win-
dow influences the agent’s behavior (Akata et al. 2023; Guo
2023; Xu et al. 2023). In formulating the memory compo-
nent, we explore various window sizes to provide the model
with information from only the n most recent rounds. We
evaluate the effect of different memory window sizes by test-
ing the LLM against an Always Defect opponent and identi-
fying the optimal window size (see §4.2). This assessment is
based on the premise that, once the LLM has gathered suf-
ficient information to recognize the opponent’s consistently
defecting behavior, its actions should align with defection,
which is the only logical strategy.

--- Page 4 ---

Name
Question
Rules
min max
What is the lowest/highest payoff
player A can get in a single round?
actions
Which actions is player A allowed to
play?
payoff
Which is player X’s payoff in a single
round if X plays p and Y plays q?
Time
round
Which is the current round of the
game?
actioni
Which action did player X play in
round i?
pointsi
How many points did player X collect
in round i?
State
#actions How many times did player X choose
p?
#points
What is player X’s current total pay-
off?
Table 1: Templates of prompt comprehension questions used
in meta-prompting to verify the LLM’s comprehension of
the prompt.
3.3
Meta-prompting
The development of effective LLM prompts is an ever-
evolving practice. Although certain studies suggested guide-
lines for prompt development (Ziems et al. 2023), achiev-
ing a consensus on the most effective prompting strate-
gies across tasks remains challenging. Typically, the prompt
quality is assessed empirically based on downstream perfor-
mance (Lester, Al-Rfou, and Constant 2021). This method
is suitable for conventional classification or regression tasks
where some form of ground truth is clearly defined. How-
ever, it is less applicable to generative tasks that lack a for-
mal standard of correctness. In the specific context of the
Prisoner’s Dilemma, any sequence of Cooperate and De-
fect actions could be considered plausible. This ambigu-
ity makes it difficult to discern whether LLM-generated se-
quences reflect a proper understanding of the game’s rules or
are merely the product of the model hallucinating (Xu, Jain,
and Kankanhalli 2024). Prior research involving LLMs in
Game Theory experiments has assessed outputs by request-
ing that the LLM provide a reasoned explanation of its out-
put (Guo 2023). However, this approach offers only a retro-
spective justification, which can itself suffer from hallucina-
tions if the LLM has not fully grasped the task’s underlying
instructions.
To partially mitigate this issue, we introduce a novel meta-
prompting technique to measure the LLMs’ comprehension
of a given prompt, to inform the process of prompt refine-
ment. Specifically, we formulate a set of prompt comprehen-
sion questions that address three key aspects of the prompt
(see Table 1): the game rules, to verify the LLM’s grasp of
the game mechanics (e.g., ‘What is the lowest payoff that
player A can get in a single round?’); the chronological
sequence of actions within the game history (e.g., ‘Which
action did player A play in round 5?’); and the cumula-
tive game statistics (e.g., ‘What is player’s B current total
payoff?’). To assess the LLMs’ proficiency in responding to
min_max
actions
payoff
round
actioni
pointsi
#actions
#points
Comprehension Questions
0.0
0.2
0.4
0.6
0.8
1.0
Response Accuracy
Rules
Time
State
Llama2
Llama3
GPT3.5t
Figure 1: Accuracy of the models’ responses to the prompt
comprehension questions defined in Table 1. The questions
are categorized into three groups, each assessing different
aspects: the rules of the game, its temporal evolution, and its
current state. We show 95% confidence intervals, computed
from 100 games.
meta-prompting questions, we conduct a series of 3 games
of 100 rounds each against RND opponents. We pose the
questions at each round and compute the average accuracy
of the LLMs’ responses. At any given round i, a question
template is instantiated into a set of questions that cover
all possible combinations of the template’s parameters. For
example, at round i, questions referring to specific rounds
(actioni and pointsi) are asked for all past rounds from
1 to i −1.
3.4
Behavioral Profiling
We profile the LLMs’ behavior with respect to a game his-
tory Gα
k in two ways. First, we quantify behavioral pat-
terns by computing the behavioral dimensions outlined in
§2.3. This computation results in a five-dimensional numer-
ical vector that encapsulates the behavioral characteristics of
the LLMs. Second, we use the Strategy Frequency Estima-
tion Method (SFEM) defined in previous work (Romero and
Rosokha 2018) to calculate the affinity between a player’s
game history and any of the classic strategies used in Pris-
oner Dilemma tournaments (see §2.2). SFEM is a finite-
mixture approach that uses likelihood maximization to esti-
mate the likelihood of a strategy being represented in experi-
mental data (Romero and Rosokha 2018). Given a game his-
tory, SFEM outputs a score between 0 and 1 for each strategy
in the set of theoretical strategies considered. Being a mix-
ture approach, the sum of all the SFEM scores over the set
of possible strategies does not have to sum up to 1. The final
SFEM scores we report are averaged over all the histories
analyzed.
4
Results
4.1
LLM’s Prompt Comprehension
Figure 1 presents the accuracy of responses to the prompt
comprehension questions associated with the final prompt
that we used in our experiments, with results averaged over

--- Page 5 ---

0
50
100
Round
0.0
0.2
0.4
0.6
0.8
1.0
pcoop vs. Always Defect
Full history
Window size 10
0
10
20
30
40
Window size
0.0
0.2
0.4
0.6
Figure 2: Left: Llama2’s probability of cooperation (pcoop)
against an Always Defect opponent, when using a memory
window size of 10 vs. including the full game history in the
prompt. Right: steady-state probability calculated on the last
10 rounds of pcoop for different memory windows sizes. We
show 95% confidence intervals, computed from 100 games.
all trial runs. Overall, the models exhibit a good understand-
ing of the concepts assessed by the questions, with most re-
sponses achieving an accuracy ranging from 0.8 to 1.0.
We iteratively tested multiple prompt versions against the
response accuracy of Llama2. No further iterations of other
models were needed, as the best prompt for Llama2 yielded
very high response accuracy in both Llama3 and GPT3.5.
Generally, adding explicit information about the game state
and rules led to a better level of prompt comprehension. For
illustration, Figure A7 in the Appendix includes a compara-
tive analysis of accuracy scores derived from an earlier ver-
sion of the prompt, which lacked a summary of the cumu-
lative point totals for the players. In the absence of explicit
total counts, Llama2 was required to sum all points from the
game history to determine the total tally, which significantly
impacted its performance on the #actions and #points
questions. This limitation aligns with previous findings that
highlight that LLMs tend to struggle with arithmetic (Xu
et al. 2023; Aher, Arriaga, and Kalai 2023; Wei et al. 2023).
The explicit inclusion of the sum of scores into the prompt
markedly improved performance, achieving near-perfect ac-
curacy.
4.2
Effect of Memory Window Size
Figure 2 (left) shows the probability of the LLM cooperating
at each round in games of 100 rounds, considering two mem-
ory window sizes: m = 100 and m = 10. Under both con-
ditions, the LLM shifts towards a stance of consistent defec-
tion after approximately 5 to 10 rounds. Notably, this dura-
tion equals or exceeds the maximum number of rounds con-
sidered in previous studies. Without any constraints on the
history length, the LLM’s cooperation level quickly starts
rising back, converging to full cooperation after the 50th
round. This pattern may be attributed to a combination of
two factors: Llama2’s intrinsic preference for positive con-
structs (Lor`e and Heydari 2023) (favoring cooperation over
defection) and its limited effectiveness in extracting action-
able insights from long prompts (Xi et al. 2023). With a
0.0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1.0
Opponent cooperation probability ( )
0.0
0.2
0.4
0.6
0.8
1.0
pcoop
Llama2
Llama3
GPT3.5t
Figure 3: Models’ probability of cooperation (pcoop) against
Unfair Random opponents with increasing cooperation
probability α. We show 95% confidence intervals, computed
from 100 games.
memory window restricted to the 10 most recent rounds, the
LLM retains a full-defection stance throughout the game.
We replicated this experiment across a range of memory
window sizes and determined their respective equilibrium
states by calculating the average cooperation probability in
the final 10 rounds (from the 90th to the 100th). As illus-
trated in Figure 2 (right), memory windows sizes around 10
yield the expected outcome. Therefore, we select a window
size of m = 10 for the remainder of our experiments. Dif-
ferently, Llama3 and GPT3.5 show no variation in their co-
operation levels regardless of the memory window size (see
Figure A8 in Appendix), allowing us to use the same prompt
designed for Llama2. Notably, Llama3 does not suffer from
the same bias towards cooperation as Llama2, and keeps its
defective behavior also when provided with the full game
history. GPT3.5 exhibits the less optimal behavior, converg-
ing towards defection much more slowly.
4.3
Behavioral Patterns
Probability of cooperation
We examine the overall
propensity for cooperation exhibited by the LLM across var-
ious degrees of environmental hostility. Figure 3 shows the
relationship between the probability of cooperative behavior
pα
coop of each model and the varying cooperation levels α of
an Unfair Random opponent.
Among the three models, Llama3 demonstrates the most
strategic approach. It maintains a very low level of cooper-
ation even when the opponent is nearly always cooperating
(pcoop < 0.3 for every α < 1), but it increases its cooper-
ation to nearly 100% when the opponent is AC (α = 1).
In contrast, Llama2’s behavior follows a sigmoidal curve
across the entire range of α from 0 to 1. This indicates a
rapid transition from a predominantly defecting strategy to
a more cooperative attitude. The sigmoid curve is character-
ized by a relatively flat left tail, maintaining a stable proba-
bility of cooperation near pcoop = 0 for α values up to 0.4.
The curve’s inflection point is between 0.6 and 0.7—well
beyond 0.5—suggesting a cautious approach in interpreting
the opponent’s actions. Compared to Llama3, the older Meta

--- Page 6 ---

model is less guarded and more prone to increase its coop-
eration as soon as the opponent’s cooperation significantly
rises over the 50/50 chance. GPT3.5 displays a less strategic
approach, maintaining a low but still significant cooperation
level (0.2 < pcoop < 0.4) for low α (< 0.5) and not reaching
full cooperation even when the opponent is AC.
In general, the models exhibit non-linear behaviors but
with different characteristics. A common trend is the in-
creasing cooperation as α grows, demonstrating a minimum
level of strategic behavior for all LLMs.
These findings, especially concerning Llama3, support
previous research that highlights the cautious response pat-
terns of LLMs in repeated game scenarios (Akata et al. 2023;
Phelps and Russell 2023).
SFEM profile
The probability of cooperation provides a
macroscopic perspective on a player’s actions. However, to
capture more nuanced strategic patterns that emerge during
the match, we employed SFEM analysis (defined in §3.4)
to estimate the similarity between the behavioral patterns
exhibited by the LLMs and those commonly observed in
games involving human players.
Figure 4 illustrates which strategies best explain the
behaviors of each model as the values of α increase.
When the adversary’s probability of cooperation exceeds
the 0.6 threshold, there is a noticeable shift in both
Llama2’s and GPT3.5’s strategy from Grim Trigger to
Always Cooperate. In contrast, Llama3 consistently aligns
with the Grim Trigger strategy across all values of α, dis-
playing an exploitative approach even when the opponent
tends to cooperate for the majority of the time. SFEM anal-
ysis further indicates that these strategies are the most rep-
resentative of the LLMs’ strategic behavior, with no other
strategies being significantly indicative.
Previous studies have shown that humans tend to be
particularly uncooperative when the reward R is much
lower than the temptation T and when playing for shorter
time horizons, typically opting for startegies close to
Always Defect (Dal B´o and Fr´echette 2011; Romero and
Rosokha 2018). Conversely, humans become more coopera-
tive when the reward is much higher and the time horizon is
longer, opting for a mixture of Tit For Tat and Grim Trigger
strategies.
Comparing this prior knowledge to our results indicates
that GPT3.5 and Llama2 are consistently more coopera-
tive than humans. In situations that do not favor coopera-
tion—where the opponent defects more frequently than co-
operates—they adopt the GRIM strategy, unlike humans who
tend to use the AD strategy. Similarly, when the context sup-
ports cooperation (i.e., the opponent cooperates more than
half of the time), both GPT3.5 and Llama2 employ the AC
strategy, which is notably more cooperative than the human
preference for TFT or GRIM. On the other hand, Llama3
is more cooperative than humans in hostile environments
(pcoop < 0.5), also using the GRIM strategy. However, in
environments that encourage cooperation, Llama3 behaves
more like humans by continuing to use the GRIM strategy,
whereas humans typically mix between the more forgiving
TFT strategy and GRIM.
0.00
0.25
0.50
0.75
1.00
Llama2
Others
AC
GRIM
0.00
0.25
0.50
0.75
1.00
Llama3
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
Opponent cooperation probability ( )
0.00
0.25
0.50
0.75
1.00
GPT3.5t
SFEM scores
Figure 4: SFEM scores quantifying the similarity between
the models’ sequences of actions and known strategies
adopted in the Iterated Prisoner’s Dilemma game (defined in
§2.2). The models’ behavioral sequences come from games
against Unfair Random opponents with increasing cooper-
ation probability α. Some SFEM scores are not shown be-
cause not well-defined for extreme values of α.
Behavioral profile
At a finer level of analysis, we charac-
terize the behavior of the LLMs along the dimensions out-
lined in Section 2.3 (Figure 5).
When the parameter α is set to low values, the mod-
els exhibit highly uncooperative traits: they frequently re-
taliate following instances of betrayal, seldom revert to co-
operative behavior after defecting, and are often the initia-
tors of unprovoked defections. GPT3.5 exhibits these traits
in a more moderate manner, whereas Llama2 and Llama3
display more extreme profiles in this regard. More notice-
able differences among the models’ response emerge be-
yond α = 0.5. While GPT3.5 and Llama2 generate choices
that are more Forgiving and less Troublemaking, Llama3 re-
mains Troublemaking and rarely Forgiving for every α <
1.0. On the other hand, the three models are constantly Nice
across conditions, rarely defecting first. GPT3.5 shows the
lowest scores but remains above 0.5 even against an oppo-
nent that never defects (α = 1). In this scenario, all the
LLMs never defect throughout the whole game in 50% of the

--- Page 7 ---

0.0
0.5
1.0
Nice
0.0
0.5
1.0
Forgiving
0.0
0.5
1.0
Retaliatory
0.0
0.5
1.0
Troublemaking
0.0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1.0
Opponent cooperation probability ( )
0.0
0.5
1.0
Emulative
Llama2
Llama3
GPT3.5t
Random
Figure 5: Presence of behavioral traits in the models’ ac-
tions when playing against Unfair Random opponents with
increasing cooperation probability α. The values of the
same traits calculated for a Random agent playing against
Unfair Random opponents are reported. Some traits are not
defined for extreme values of α. We show 95% confidence
intervals, computed from 100 games.
runs. Interestingly, there is no scenario in which any LLM is
simultaneously Nice, Forgiving, and Retaliatory — the three
conditions that characterize the most successful strategies,
such as Tit For Tat.
5
Discussion and Conclusion
Our study contributes to the broad literature on behavioral
studies of Large Language Models as artificial social agents.
Specifically, we study the responses of Llama2, Llama3,
and GPT3.5 to the prototypical social scenario of the Pris-
oner’s Dilemma. Building upon prior studies that explored
the application of LLMs in classic Game Theory experi-
ments, our work introduces a more systematic experimen-
tal setup that incorporates quantitative checks to better align
the LLMs’ responses to the complex task description. We
have shown that aspects like prompt comprehension, mem-
ory representation, and duration of the simulation play cru-
cial roles, especially for less powerful models, with the po-
tential to significantly distort the experimental outcomes,
if left unchecked. Our framework provides a quantitative
guide for selecting the simulation variables and improving
the prompt.
Our findings add a new benchmark to the body of work
that explored the outcomes of iterated games, both among
humans and among AI agents. In contrast to the behav-
ioral patterns observed in humans playing the Prisoner’s
Dilemma game (Dal B´o and Fr´echette 2011), the three mod-
els displayed a more marked overall propensity towards
cooperation. Under conditions that disincentivize coopera-
tion, most human players adopt a stance of complete de-
fection, whereas the LLMs’ strategy, albeit mostly unco-
operative, is characterized by an initial trust in the op-
ponent’s cooperation (Nice), reminiscent of the strategy
known in Game Theory as Grim Trigger. When the environ-
ment is more favorable to cooperative play, Llama3 playing
Grim Trigger becomes comparable to human strategies that
often resemble either Grim Trigger or Tit For Tat. Differ-
ently, Llama2 and GPT3.5 tend towards a consistently coop-
erative approach. Notably, Llama2’s shift from Grim Trigger
to Always Cooperate occurs quite abruptly as the opponent’s
defection probability drops below 30%, while GPT3.5’s
transition is smoother and starts when α exceeds 0.2.
Our results are in line with early experiments involving
LLMs, which indicated a tendency for these models to co-
operate in repeated games (Brookins and DeBacker 2023;
Mei et al. 2024). However, the broader research in this area
has yielded mixed outcomes (Akata et al. 2023; Phelps and
Russell 2023). Distinct from previous studies, our findings
are derived from extensive game simulations conducted over
numerous rounds and benefit from an experimental frame-
work that leverages quantitative checks for accuracy.
Overall, our findings offer a robust baseline for un-
derstanding LLMs’ behaviors in the Iterated Prisoner’s
Dilemma (IPD), a widely used Game Theory experiment
for assessing agents’ responses to conflictual scenarios. Es-
tablishing this baseline allows for clearer differentiation be-
tween the inherent tendencies of the models and the effects
of specific elements within the game setting.
However, it is important to acknowledge the limitations
of our work, which open the way for further research. First,
our analysis was conducted using three models, specifically
Llama2, Llama3, and GPT3.5, which, at the time of writ-
ing, are among the most advanced models available (Tou-
vron et al. 2023; Brown et al. 2020)5. Nevertheless, the
field is progressing at an unprecedented pace, with new
models being introduced regularly. To determine whether
the behavioral patterns observed in our study are consis-
tent across many different models, it is important to con-
duct comparative analyses with models that vary signifi-
cantly in terms of parameter size and the volume of their
training data. Second, our study’s scope was limited to as-
sessing the LLM’s responses to random strategies, and with
a fixed payoff structure. Exploring the LLM’s interactions
with more sophisticated opponents would enable us to bet-
ter delineate the boundaries of LLMs’ inferential abilities in
5https://ai.meta.com/blog/meta-llama-3/

--- Page 8 ---

social contexts, and to draw more detailed behavioral pro-
files under a broader spectrum of conditions that more com-
prehensively represent prototypical social scenarios. We ex-
plored only the use of Zero-Shot Chain-of-Thought tech-
niques without obtaining any improvement. Other options
like Tree-of-Thought (Yao et al. 2023) techniques or exter-
nal modules (Wang et al. 2024) can be employed to test dif-
ferent reasoning conditions for the models. Furthermore, the
experimental framework of our study considers only a sin-
gle LLM agent. Creating social groups of AI agents that in-
teract through iterated games like the Prisoner’s Dilemma
would open up a wealth of opportunities to study emergent
behaviors in synthetic societies, an avenue of research that
is increasingly recognized as fundamental for a proper un-
derstanding of how LLMs can affect human societies (Bail
2024). Last, despite the numerical guidelines we imple-
mented to evaluate the quality of the prompt, our refine-
ments of the prompt were not guided by any principle other
than experience and instinct. Our attempt to use Chain-of-
Thought (Kojima et al. 2022; Zhou et al. 2023) as a struc-
tured way to approach prompt revision resulted in prompts
that did not improve performance in our prompt compre-
hension question inventory (see Figure A6 in Appendix). In
this respect, our work provides yet another example of how
prompt engineering would benefit from supporting tools to
constrain its highly discretionary nature. Another interesting
direction for future research is to explore persona prompt-
ing (Hu and Collier 2024), where models are guided towards
specific behaviors, such as altruism or selfishness. However,
in this study, we intentionally avoided using personas to in-
fluence the outputs of the LLMs, as our primary objective
is to assess the models’ inherent biases towards different
behavioral patterns in game-theoretical scenarios. Similarly,
models could be enhanced by incorporating a planning mod-
ule that considers the potential outcomes of various actions
over multiple steps (Kambhampati et al. 2024).
Despite its limitations, our work has two main impli-
cations. From the theoretical perspective, it expands our
knowledge of the inherent biases of LLMs in social situa-
tions, which is crucial to inform their deployment across dif-
ferent contexts. From the practical perspective, it provides
a principled way to approach game theoretical simulations
with LLMs. This constitutes a step towards using these sim-
ulations as reliable and reproducible tools that could be used
as tests to verify LLM alignment to desired principles of so-
cial cooperation (Shen et al. 2023).
6
Related work
Next, we briefly review previous work using LLMs for so-
cial reasoning, the generation of human-like synthetic data,
and simulations of human behavior.
6.1
LLMs as Agents
Argyle et al. (2023) instructed LLMs to answer surveys as if
they belonged to specified socio-demographic groups. They
showed a high similarity between the responses generated
by the LLM and those provided by the demographic groups
it was asked to emulate. LLMs impersonating human agents
with different profiles were used to explore the negotiation
abilities of the models (Davidson et al. 2024) or to create
synthetic social networks, to observe emergent social behav-
ior, most notably opinion dynamics and information spread-
ing (Chuang et al. 2023; De Marzo, Pietronero, and Garcia
2023; He, Wallis, and Rathje 2023). Park et al. (2023) de-
veloped a society with synthetic agents interacting with el-
ements of a synthetic world, showed that those agents were
able to adopt behaviors that are typical of humans without
being directly prompted to do so. Using the same frame-
work, Ren et al. (2024) showed that those agents were also
able to build and spread social norms, while Piatti et al.
(2024) developed a similar framework to investigate the ro-
bustness of LLMs societies.
6.2
LLMs in Game Theory
Early work on the application of LLMs to Game Theory
experiments touched upon both 1-time and iterated games.
Single-iteration experiments offer limited insight into LLM
behavior. Brookins and DeBacker (2023) showed that LLMs
are more biased towards fairness and cooperation when
compared to a human baseline sample. In contrast, Aher,
Arriaga, and Kalai (2023) found that there is an overall
alignment between the LLM-based agent behavior and the
human ones. Investigating the ability of LLMs to predict
human choices in 1-time games, Capraro, Di Paolo, and
Pizziol (2024) showed that only more powerful models are
capable of doing it, although they overestimate the altruis-
tic tendency of human players. When focusing on iterated
games, the spectrum of patterns that can be identified ex-
pands, allowing more refined analysis. For example, Akata
et al. (2023) managed to identify that LLMs can be partic-
ularly unforgiving. Mei et al. (2024) discovered instead that
the same models show a higher cooperation rate than com-
pared to humans. Fan et al. (2023) exploited the iteration
of games to check the level of the opponent’s strategy that
the LLM was able to infer from the history of actions. They
showed that the inference capability of the LLM is limited,
calling for more systematic approaches to structure mem-
ory and prompts. Testing a novel benchmark with differ-
ent games, Duan et al. (2024) studied multiple LLMs show-
ing that closed-source models tend to achieve better perfor-
mance than open-source ones. Although they did not exam-
ine the behavioral characteristics of the LLMs’ responses,
they also found that Zero-Shot Chain-of-Thought techniques
are not always beneficial, which aligns with our results.
Ethical Considerations
The deployment of Large Language Models as AI social
agents raises numerous ethical considerations that are cur-
rently the subject of intense scrutiny by the interdisciplinary
research community. The extraordinary capabilities of these
models to generate text have led several scientists to envi-
sion alarming scenarios in which the seamless integration
of AI agents into the online social discourse may facilitate
the dissemination of harmful content, the spread of misin-
formation, and the propagation of ‘semantic garbage’, ulti-
mately damaging our societies (Floridi and Chiriatti 2020;

--- Page 9 ---

Weidinger et al. 2022; Hendrycks, Mazeika, and Woodside
2023). As a result, any research exploring the characteris-
tics of LLMs as social agents could, directly or indirectly,
contribute knowledge that might be exploited to implement
and deploy LLM-based technologies for malicious purposes.
While recognizing this risk, we also believe that conducting
research on LLM-based agents is essential to assess poten-
tial risks and to guide efforts aimed at developing strategies
to mitigate them. Our study contributes positively to deepen
our understanding of how LLMs react to social stimuli.
Even when deploying LLM-based agents for ethical pur-
poses, trade-offs between the obtained benefit and the high
level of power consumption required to run them should be
carefully considered (Bender et al. 2021).
Code and Data Availability
All code, prompts, and game traces will be made available
on GitHub.
Acknowledgments
This work was partially supported by the Italian Ministry
of Education ( PRIN grant DEMON prot. 2022BAXSPY)
and the European Union (NextGenerationEU project PNRR-
PE-AI FAIR). NF acknowledges the support from the Dan-
ish Data Science Academy through the DDSA Visit Grant
(Grant ID: 2023-1856) and from Politecnico di Milano
through the scholarship “Tesi all’estero a.a. 2023/24-Primo
bando”. LMA acknowledges the support from the Carlsberg
Foundation through the COCOONS project (CF21-0432).
References
Aher, G. V.; Arriaga, R. I.; and Kalai, A. T. 2023.
Us-
ing Large Language Models to Simulate Multiple Humans
and Replicate Human Subject Studies. In Proceedings of
the 40th International Conference on Machine Learning,
337–371. PMLR.
Akata, E.; Schulz, L.; Coda-Forno, J.; Oh, S. J.; Bethge, M.;
and Schulz, E. 2023. Playing repeated games with Large
Language Models. ArXiv:2305.16867 [cs].
Argyle, L. P.; Busby, E. C.; Fulda, N.; Gubler, J. R.; Ryt-
ting, C.; and Wingate, D. 2023. Out of One, Many: Using
Language Models to Simulate Human Samples. Political
Analysis, 31(3): 337–351.
Axelrod, R. 1980.
Effective Choice in the Prisoner’s
Dilemma. Journal of Conflict Resolution, 24(1): 3–25.
Axelrod, R. 1981.
The Emergence of Cooperation
among Egoists. American Political Science Review, 75(2):
306–318.
Axelrod, R.; and Hamilton, W. D. 1981. The evolution of
cooperation. science, 211(4489): 1390–1396.
Bail, C. A. 2024. Can Generative AI improve social science?
Proceedings of the National Academy of Sciences, 121(21):
e2314021121.
Bender, E. M.; Gebru, T.; McMillan-Major, A.; and
Shmitchell, S. 2021.
On the dangers of stochastic par-
rots: Can language models be too big? In Proceedings of
the 2021 ACM conference on fairness, accountability, and
transparency, 610–623.
Breum, S. M.; Egdal, D. V.; Mortensen, V. G.; Møller, A. G.;
and Aiello, L. M. 2023.
The Persuasive Power of Large
Language Models. ArXiv:2312.15523 [physics].
Brookins, P.; and DeBacker, J. M. 2023.
Playing Games
With GPT: What Can We Learn About a Large Language
Model From Canonical Strategic Games?
Brown, T.; Mann, B.; Ryder, N.; Subbiah, M.; Kaplan, J. D.;
Dhariwal, P.; Neelakantan, A.; Shyam, P.; Sastry, G.; Askell,
A.; Agarwal, S.; Herbert-Voss, A.; Krueger, G.; Henighan,
T.; Child, R.; Ramesh, A.; Ziegler, D.; Wu, J.; Winter,
C.; Hesse, C.; Chen, M.; Sigler, E.; Litwin, M.; Gray, S.;
Chess, B.; Clark, J.; Berner, C.; McCandlish, S.; Radford,
A.; Sutskever, I.; and Amodei, D. 2020. Language Models
are Few-Shot Learners. In Advances in Neural Information
Processing Systems, volume 33, 1877–1901. Curran Asso-
ciates, Inc.
Camerer, C. F. 1997. Progress in Behavioral Game Theory.
Journal of Economic Perspectives, 11(4): 167–188.
Cao, Y.; Li, S.; Liu, Y.; Yan, Z.; Dai, Y.; Yu, P. S.; and Sun,
L. 2023. A comprehensive survey of ai-generated content
(aigc): A history of generative ai from gan to chatgpt. arXiv
preprint arXiv:2303.04226.
Capraro, V.; Di Paolo, R.; and Pizziol, V. 2024.
As-
sessing Large Language Models’ ability to predict how
humans balance self-interest and the interest of others.
ArXiv:2307.12776 [cs, econ, q-fin].
Chuang, Y.-S.; Goyal, A.; Harlalka, N.; Suresh, S.; Hawkins,
R.; Yang, S.; Shah, D.; Hu, J.; and Rogers, T. T. 2023. Sim-
ulating Opinion Dynamics with Networks of LLM-based
Agents. ArXiv:2311.09618 [physics].
Dafoe, A.; Hughes, E.; Bachrach, Y.; Collins, T.; Mc-
Kee, K. R.; Leibo, J. Z.; Larson, K.; and Graepel, T.
2020.
Open problems in cooperative ai.
arXiv preprint
arXiv:2012.08630.
Dal B´o, P.; and Fr´echette, G. R. 2011. The Evolution of Co-
operation in Infinitely Repeated Games: Experimental Evi-
dence. American Economic Review, 101(1): 411–429.
Davidson, T. R.; Veselovsky, V.; Kosinski, M.; and West, R.
2024. Evaluating Language Model Agency Through Nego-
tiations. The Twelfth International Conference on Learning
Representations.
De Marzo, G.; Pietronero, L.; and Garcia, D. 2023. Emer-
gence of Scale-Free Networks in Social Interactions among
Large Language Models. ArXiv:2312.06619 [physics].
Duan, J.; Zhang, R.; Diffenderfer, J.; Kailkhura, B.; Sun,
L.; Stengel-Eskin, E.; Bansal, M.; Chen, T.; and Xu,
K. 2024.
GTBench: Uncovering the Strategic Reason-
ing Limitations of LLMs via Game-Theoretic Evaluations.
ArXiv:2402.12348 [cs].
Fan, C.; Chen, J.; Jin, Y.; and He, H. 2023. Can Large Lan-
guage Models Serve as Rational Players in Game Theory?
A Systematic Analysis. ArXiv:2312.05488 [cs].

--- Page 10 ---

Ferrara, E. 2024. GenAI against humanity: Nefarious ap-
plications of generative artificial intelligence and large lan-
guage models.
Journal of Computational Social Science,
1–21.
Floridi, L.; and Chiriatti, M. 2020. GPT-3: Its nature, scope,
limits, and consequences. Minds and Machines, 30: 681–
694.
Fudenberg, D.; Rand, D. G.; and Dreber, A. 2012.
Slow
to Anger and Fast to Forgive: Cooperation in an Uncertain
World. American Economic Review, 102(2): 720–749.
Guo, F. 2023.
GPT in Game Theory Experiments.
ArXiv:2305.05516 [econ, q-fin].
He, J.; Wallis, F.; and Rathje, S. 2023. Homophily in An
Artificial Social Network of Agents Powered By Large Lan-
guage Models — Research Square.
Hendrycks, D.; Mazeika, M.; and Woodside, T. 2023.
An Overview of Catastrophic AI Risks.
arXiv preprint
arXiv:2306.12001.
Horton, J. J. 2023. Large Language Models as Simulated
Economic Agents: What Can We Learn from Homo Silicus?
Hu, T.; and Collier, N. 2024. Quantifying the persona effect
in llm simulations. arXiv preprint arXiv:2402.10811.
Kambhampati, S.; Valmeekam, K.; Guan, L.; Stechly, K.;
Verma, M.; Bhambri, S.; Saldyt, L.; and Murthy, A. 2024.
LLMs Can’t Plan, But Can Help Planning in LLM-Modulo
Frameworks. arXiv preprint arXiv:2402.01817.
Kojima, T.; Gu, S. S.; Reid, M.; Matsuo, Y.; and Iwasawa,
Y. 2022. Large Language Models are Zero-Shot Reason-
ers. Advances in Neural Information Processing Systems,
35: 22199–22213.
Kuhn, S. 2019. Prisoner’s Dilemma ¿ Strategies for the Iter-
ated Prisoner’s Dilemma (Stanford Encyclopedia of Philos-
ophy).
Lester, B.; Al-Rfou, R.; and Constant, N. 2021.
The
power of scale for parameter-efficient prompt tuning. arXiv
preprint arXiv:2104.08691.
Lor`e, N.; and Heydari, B. 2023. Strategic Behavior of Large
Language Models: Game Structure vs. Contextual Framing.
ArXiv:2309.05898 [cs, econ].
Mao, S.; Cai, Y.; Xia, Y.; Wu, W.; Wang, X.; Wang, F.; Ge,
T.; and Wei, F. 2023. Alympics: Language agents meet game
theory. arXiv preprint arXiv:2311.03220.
Mei, Q.; Xie, Y.; Yuan, W.; and Jackson, M. O. 2024. A Tur-
ing test of whether AI chatbots are behaviorally similar to
humans. Proceedings of the National Academy of Sciences,
121(9): e2313925121.
M¨okander, J.; Schuett, J.; Kirk, H. R.; and Floridi, L. 2023.
Auditing large language models: a three-layered approach.
AI and Ethics, 1–31.
Osborne, M. J.; and Rubinstein, A. 1994. A course in game
theory. MIT press.
Park, J. S.; O’Brien, J.; Cai, C. J.; Morris, M. R.; Liang,
P.; and Bernstein, M. S. 2023. Generative Agents: Interac-
tive Simulacra of Human Behavior. In Proceedings of the
36th Annual ACM Symposium on User Interface Software
and Technology, UIST ’23, 1–22. New York, NY, USA: As-
sociation for Computing Machinery. ISBN 9798400701320.
Phelps, S.; and Russell, Y. I. 2023. Investigating emergent
goal-like behaviour in large language models using experi-
mental economics. arXiv preprint arXiv:2305.07970.
Piatti, G.; Jin, Z.; Kleiman-Weiner, M.; Sch¨olkopf, B.;
Sachan, M.; and Mihalcea, R. 2024. Cooperate or Collapse:
Emergence of Sustainable Cooperation in a Society of LLM
Agents. ArXiv:2404.16698 [cs].
Ren, S.; Cui, Z.; Song, R.; Wang, Z.; and Hu, S. 2024. Emer-
gence of Social Norms in Large Language Model-based
Agent Societies. ArXiv:2403.08251 [cs].
Romero, J.; and Rosokha, Y. 2018. Constructing strategies
in the indefinitely repeated prisoner’s dilemma game. Euro-
pean Economic Review, 104: 185–219.
Schramowski, P.; Turan, C.; Andersen, N.; Rothkopf, C. A.;
and Kersting, K. 2022. Large pre-trained language models
contain human-like biases of what is right and wrong to do.
Nature Machine Intelligence, 4(3): 258–268.
Shen, T.; Jin, R.; Huang, Y.; Liu, C.; Dong, W.; Guo, Z.;
Wu, X.; Liu, Y.; and Xiong, D. 2023. Large language model
alignment: A survey. arXiv preprint arXiv:2309.15025.
Stewart, A. J.; and Plotkin, J. B. 2012. Extortion and co-
operation in the Prisoner’s Dilemma.
Proceedings of the
National Academy of Sciences, 109(26): 10134–10135.
Touvron, H.; Lavril, T.; Izacard, G.; Martinet, X.; Lachaux,
M.-A.; Lacroix, T.; Rozi`ere, B.; Goyal, N.; Hambro, E.;
Azhar, F.; et al. 2023. Llama: Open and efficient founda-
tion language models. arXiv preprint arXiv:2302.13971.
Tucker, A. W.; and Luce, R. D. 1959. Contributions to the
Theory of Games. Princeton University Press. ISBN 978-0-
691-07937-0. Google-Books-ID: 9lSVFzsTGWsC.
Tucker, A. W.; and Straffin Jr, P. D. 1983. The Mathematics
of Tucker: A Sampler. The Two-Year College Mathematics
Journal.
Wang, L.; Ma, C.; Feng, X.; Zhang, Z.; Yang, H.; Zhang, J.;
Chen, Z.; Tang, J.; Chen, X.; Lin, Y.; Zhao, W. X.; Wei, Z.;
and Wen, J. 2024. A survey on large language model based
autonomous agents. Frontiers of Computer Science, 18(6):
186345.
Wei, J.; Wang, X.; Schuurmans, D.; Bosma, M.; Ichter, B.;
Xia, F.; Chi, E. H.; Le, Q. V.; and Zhou, D. 2023. Chain-
of-Thought Prompting Elicits Reasoning in Large Language
Models.
Weidinger, L.; Uesato, J.; Rauh, M.; Griffin, C.; Huang, P.-
S.; Mellor, J.; Glaese, A.; Cheng, M.; Balle, B.; Kasirzadeh,
A.; et al. 2022. Taxonomy of risks posed by language mod-
els. In Proceedings of the 2022 ACM Conference on Fair-
ness, Accountability, and Transparency, 214–229.
Xi, Z.; Chen, W.; Guo, X.; He, W.; Ding, Y.; Hong, B.;
Zhang, M.; Wang, J.; Jin, S.; Zhou, E.; Zheng, R.; Fan, X.;
Wang, X.; Xiong, L.; Zhou, Y.; Wang, W.; Jiang, C.; Zou,
Y.; Liu, X.; Yin, Z.; Dou, S.; Weng, R.; Cheng, W.; Zhang,
Q.; Qin, W.; Zheng, Y.; Qiu, X.; Huang, X.; and Gui, T.
2023.
The Rise and Potential of Large Language Model
Based Agents: A Survey. ArXiv:2309.07864 [cs].

--- Page 11 ---

Xu, L.; Hu, Z.; Zhou, D.; Ren, H.; Dong, Z.; Keutzer,
K.; Ng, S. K.; and Feng, J. 2023.
MAgIC: Investi-
gation of Large Language Model Powered Multi-Agent
in Cognition, Adaptability, Rationality and Collaboration.
ArXiv:2311.08562 [cs].
Xu, Z.; Jain, S.; and Kankanhalli, M. 2024. Hallucination
is inevitable: An innate limitation of large language models.
arXiv preprint arXiv:2401.11817.
Yang, K.-C.; and Menczer, F. 2023.
Anatomy of an
AI-powered malicious social botnet.
arXiv preprint
arXiv:2307.16336.
Yao, S.; Yu, D.; Zhao, J.; Shafran, I.; Griffiths, T.; Cao, Y.;
and Narasimhan, K. 2023.
Tree of Thoughts: Deliberate
Problem Solving with Large Language Models. Advances in
Neural Information Processing Systems, 36: 11809–11822.
Zhou, Y.; Muresanu, A. I.; Han, Z.; Paster, K.; Pitis, S.;
Chan, H.; and Ba, J. 2023. Large Language Models Are
Human-Level Prompt Engineers. ArXiv:2211.01910 [cs].
Ziems, C.; Held, W.; Shaikh, O.; Chen, J.; Zhang, Z.; and
Yang, D. 2023.
Can Large Language Models Transform
Computational Social Science? arXiv:2305.03514.

--- Page 12 ---

Appendix
Prompts and their Variations
Figures A1, A2 and A3 show examples of the three parts of
the final prompt we used in our experiments. Figures A4
and A5 respectively show the variation in the instructing
prompt when using the Zero-Shot Chain-of-Thought tech-
niques from Kojima et al. (2022) and Zhou et al. (2023).
Figure A6 displays the accuracy obtain by Llama2 in the
comprehension questions when using the two variations and
the unvaried prompt.
Figure A7 shows the comparison in the accuracy of
Llama2 between the initial prompt without explicit score
counts and the final version of it.
System prompt
<s>[INST]
<<SYS>>
Context: Player A and player B are playing a
multi-round game.
At each turn player A and player B
simultaneously perform one of the following
actions: {"Cooperate", "Defect"}
The payoffs for each combination of chosen
actions are the following:
If A plays "Defect" and B plays "Defect", A
collects 1 points and B collects 1 points.
If A plays "Defect" and B plays "Cooperate",
A collects 5 points and B collects 0 points.
If A plays "Cooperate" and B plays "Defect",
A collects 0 points and B collects 5 points.
If A plays "Cooperate" and B plays
"Cooperate", A collects 3 points and B
collects 3 points.
They will play a total of 100 rounds of this
game.
Remember that a player’s objective is to get
the highest possible number of points in the
long run.
<<SYS>>
Figure A1: System prompt describing the players’ roles, the
rules of the games, the number of rounds to be played, and
the player’s objective. This part of the prompt is fixed in all
simulations.
Contextual prompt
The history of the game in the last 5 rounds
is the following:
Round 2: A played "Cooperate" and B
played "Defect" A collected 0 points and
B collected 5 points.
Round 3: A played "Defect" and B played
"Defect" A collected 1 points and B
collected 1 points.
Round 4: A played "Cooperate" and B
played "Defect" A collected 0 points and
B collected 5 points.
Round 5: A played "Defect" and B played
"Cooperate" A collected 5 points and B
collected 0 points.
Round 6: A played "Defect" and B played
"Defect" A collected 1 points and B
collected 1 points.
In total, A chose "Cooperate" 2 times and
chose "Defect" 3 times, B chose "Cooperate"
1 times and chose "Defect" 4 times.
In total, A collected 7 points and B
collected 12 points.
Current round: 7.
Figure A2: Contextual prompt containing information about:
the game history in the last n rounds (5 in this example),
the overall amount of times each player chose each action,
the overall amount of points collected by each player, and
the current round. For each turn, the prompt contains: the
action played by each player and the points collected by each
player. This prompt changes at each round.
Instructing prompt
Remember to use only the following JSON
format:
{"action": <ACTION of A>, "reason":
<YOUR REASON>}
Answer saying which action player A should
play.
Remember to answer using the right
format.[/INST]
Figure A3: Instructing prompt. The LLM is instructed on
the nature and format of the answer. This part of the prompt
component is replaced with prompt comprehension ques-
tions in the phase of prompt tuning.

--- Page 13 ---

Instructing prompt
Remember to use only the following JSON
format:
{"action": <ACTION of A>, "reason":
<YOUR REASON>}
Answer saying which action player A should
play.
Remember to answer using the right
format.[/INST]
Let’s think step by step
Figure A4: Variation of the instructing prompt with Kojima
et al. (2022) Zero-Shot Chain-of-Thought.
Instructing prompt
Remember to use only the following JSON
format:
{"action": <ACTION of A>, "reason":
<YOUR REASON>}
Answer saying which action player A should
play.
Remember to answer using the right
format.[/INST]
Let’s work this out in a step-by-step way to
be sure we have the right answer
Figure A5: Variation of the instructing prompt with Zhou
et al. (2023) Zero-Shot Chain-of-Thought.
min_max
actions
payoff
round
actioni
pointsi
#actions
#points
Comprehension Questions
0.0
0.2
0.4
0.6
0.8
1.0
Response Accuracy
Rules
Time
State
Kojima et al.
Zhou et al.
No ZS-CoT
Figure A6: Accuracy of Llama2’s responses to the prompt
comprehension questions defined in Table 1 using two Zero-
Shot Chain-of-Thought variations of the prompt compared
to the accuracy obtained with the unvaried prompt. We show
95% confidence intervals, computed from 100 games.
Effect of Memory Window Size
Figure A8 shows the probability of cooperation for Llama3
and GPT3.5 when using memory windows of different sizes.
Different from Llama2, neither of these models significantly
changes its behavior depending on the window size. In par-
min_max
actions
payoff
round
actioni
pointsi
#actions
#points
Comprehension Questions
0.0
0.2
0.4
0.6
0.8
1.0
Response Accuracy
Rules
Time
State
Full prompt
No explicit score count
Figure A7: Accuracy of Llama2 responses to the prompt
comprehension questions defined in Table 1. The accuracy
of the final full prompt is compared with an earlier version
of the prompt that lacked a summary of the cumulative re-
wards achieved by the players. We show 95% confidence
intervals, computed from 100 games.
0
50
100
Round
0.0
0.2
0.4
0.6
0.8
1.0
pcoop vs. Always Defect
Llama3
Window size 10
Full history
0
50
100
Round
0.0
0.2
0.4
0.6
0.8
1.0
GPT3.5t
Window size 10
Full history
Figure A8: Llama3’s and GPT3.5’s probability of coopera-
tion (pcoop) against an Always Defect opponent, when using
a memory window size of 10 vs. including the full game his-
tory in the prompt.
ticular, the trend observed for GPT3.5, which tends to stabi-
lize around the value 0.2, is in accordance with the average
pcoop shown in Figure 5 for α = 0

--- Page 14 ---

Effect of Temperature
We explore the impact of varying the temperature hyperpa-
rameter on the probability of cooperation pcoop of Llama3
and GPT3.51. For each model and each temperature (0.1
and 1.0), we run 10 games of 100 rounds each against op-
ponents with varying cooperation probability α. Figure A9
presents the average probability of cooperation for Llama3
and GPT3.5 for three different temperature values up to 1.0.
At temperatures greater than 1.0, the models tend to produce
seemingly random tokens, which renders their output unus-
able.
The Pearson correlation between the values of pcoop
across different temperature pairs is in the range [0.97 −1],
indicating that the temperature does not affect the general
trends of pcoop as α varies. However, the growth of the co-
operation curve for GPT3.5 turns from roughly linear to
a sigmoid as temperature decreases. This suggests that, in
some models, different levels of determinism can influence
the boundaries of their decision states. In this specific case,
it appears that the noise that the increased temperature adds
to the generated choices smoothens the sharp transition be-
tween the uncooperative and cooperative states that can be
observed at low temperatures.
1HuggingFace discontinued access to Llama2 through their In-
ference API in May 2024. Since then, the model has been available
only dedicated server hosting at considerable costs. We therefore
limit our tests on temperature to Llama3 and GPT3.5 only.
0.0
0.2
0.4
0.6
0.8
1.0
Llama3
T=0.1
T=0.7
T=1.0
0.0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1.0
Opponent cooperation probability ( )
0.0
0.2
0.4
0.6
0.8
1.0
GPT3.5t
pcoop
Figure A9: Llama3’s and GPT3.5’s probability of coopera-
tion (pcoop) against Unfair Random opponents with increas-
ing cooperation probability α for different values of the tem-
perature hyperparameter. We show 95% confidence inter-
vals, computed from 10 games.

```
