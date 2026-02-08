---
title: "2025-Mao-ALYMPICS LLM Agents Meet Game Theory - PDF Extract"
source_pdf: "2025-Mao-ALYMPICS LLM Agents Meet Game Theory.pdf"
pages: 17
extracted_at: "2026-02-07T17:00:45.779099"
---

# PDF Extract: 2025-Mao-ALYMPICS LLM Agents Meet Game Theory

**Source PDF:** 2025-Mao-ALYMPICS LLM Agents Meet Game Theory.pdf
**Total Pages:** 17

---

## Content

```
--- Page 1 ---

ALYMPICS: LLM Agents meet Game Theory
Exploring Strategic Decision-Making with AI Agents
Shaoguang Mao∗, Yuzhe Cai∗† , Yan Xia ,
Wenshan Wu , Xun Wang , Fengyi Wang† , Tao Ge‡ and Furu Wei
Microsoft Research Asia
{shaoguang.mao, v-yuzhecai, yanxia}@microsoft.com,
{wenshan.wu, xunwang, v-fengyiwang, tage, fuwei}@microsoft.com
Abstract
This paper introduces Alympics (Olympics for
Agents), a systematic simulation framework uti-
lizing Large Language Model (LLM) agents for
game theory research. Alympics creates a versatile
platform for studying complex game theory prob-
lems, bridging the gap between theoretical game
theory and empirical investigations by providing a
controlled environment for simulating human-like
strategic interactions with LLM agents. In our pi-
lot case study, the ”Water Allocation Challenge,”
we explore Alympics through a challenging strate-
gic game focused on the multi-round auction on
scarce survival resources. This study demonstrates
the framework’s ability to qualitatively and quanti-
tatively analyze game determinants, strategies, and
outcomes. Additionally, we conduct a comprehen-
sive human assessment and an in-depth evaluation
of LLM agents in strategic decision-making sce-
narios. Our findings not only expand the under-
standing of LLM agents’ proficiency in emulating
human strategic behavior but also highlight their
potential in advancing game theory knowledge,
thereby enriching our understanding of both game
theory and empowering further research into strate-
gic decision-making domains with LLM agents.
Codes, prompts, and all related resources are avail-
able at Alympics.
1
Introduction
Game theory is a branch of mathematics that studies strate-
gic interactions among rational agents.
It has applica-
tions in many fields, such as economics [Shubik, 1981; Po-
hjola, 1986], social sciences [Sanfey, 2007; Ziems et al.,
2023], computer science [Yang and Wang, 2020], and biol-
ogy [Archetti and Pienta, 2019]. However, the study of game
theory in practice presents challenges: Many real-world prob-
lems in game theory cannot be solved through simple theoret-
ical deductions. Instead, they often require real-world exper-
∗Equal contributions.
† This work was done during internship at MSRA.
‡ Corresponding Author.
Day: x 
Resources: x units 
Day N Water Supply Announcement
Result: 
Day N Results Announcement
Results being tabulated...
Submit Bids…
For today's auction, I will 
bid $100. Because …
…
Alex
Bob
Cindy
David
Eric
Figure 1: ”Water Allocation Challenge”. Players are tasked with
ensuring survival over 20 days by strategically acquiring water re-
sources through daily auctions. Each player has different income
and different water demand.
Daily water supply varies and will
be announced before daily auction.
To allocate water resources,
a sealed-bid auction will be conducted daily. Acquiring water in-
creases HP, while failing to do so decreases HP. Players whose HP
drop below or equal to 0 will be eliminated from the game.
iments, which can be expensive, time-consuming, and ethi-
cally complex due to the involvement of human participants.
Fortunately, recent advancements in Large Language Mod-
els (LLMs) [OpenAI, 2023; Bubeck et al., 2023; Touvron et
al., 2023] and LLM-based agents[Sumers et al., 2023; Li et
al., 2023; Lin et al., 2023; Guo, 2023] now offer a new op-
portunity to study these complex game theory problems with
AI. These developments have enabled the creation of increas-
ingly sophisticated systems capable of emulating human be-
havior in various dimensions, including style, tone, person-
ality, emotions, and even collaborative and competitive ef-
forts[Wang et al., 2023a; Talebirad and Nadiri, 2023; Madaan
et al., 2023; Wang et al., 2023b; de Zarz`a et al., 2023; Zhao
et al., 2023; Park et al., 2023; Chen et al., 2023; Abdelnabi et
al., 2023; Zhang et al., 2023; Lor`e and Heydari, 2023; Hor-
ton, 2023].
For example, Xu et al. [2023b] illustrate this
progress using the example of Werewolf, where they observe
non-preprogrammed emergent strategic behaviors in LLMs
during gameplay, such as trust, confrontation, camouflage,
and leadership. However, there are still three open questions
on using LLM and agent for game theory research: How to
construct a unified, controllable, and efficient framework for
simulating human strategic interactions and facilitating game
arXiv:2311.03220v4  [cs.CL]  16 Jan 2024

--- Page 2 ---

theory research? What methods are available for conduct-
ing game theory research using the LLM Agent framework?
Does the LLM Agent demonstrate strategic behavior akin to
humans, and what level of LLM agent achieved in the strate-
gic reasoning?
In this paper, we argue that LLMs can be used to imple-
ment pseudo-agents which can participate in game-theoretic
scenarios and provide insights into the dynamics and out-
comes of strategic interactions.
We introduce Alympics,
Olympics for Agents, a new simulation framework for game
theory using LLM agents. Alympics incorporates a Sandbox
Playground, Agent Players, and the option for Human Play-
ers, enabling the construction of realistic and dynamic mod-
els of human interactions. By leveraging the capabilities of
LLM agents, our framework provides researchers with a con-
trolled, scalable, and reproducible platform for exploring var-
ious game scenarios and testing hypotheses in game theory.
To exemplify the practicality and effectiveness of simulat-
ing and researching strategic decision-making scenarios, we
present a pilot case study centered around an unequal compe-
tition for limited resources. As shown in Fig.1, this game is
a reduction of a series of classic game theory problems such
as auctions, dynamic games, and unequal competition. It also
avoids potential data leakage issues that may occur in clas-
sic games. Through the manipulation of resource availabil-
ity and participating agent personalities, we demonstrate how
Alympics can be employed to investigate the determinants in-
fluencing strategic decision-making and game outcomes.
Although there are many works on simulating human be-
haviors through language agents, it is still unclear whether
the agents’ simulations demonstrate rational reasoning and
strategic behaviors.
So we conduct an exhaustive human
assessment of the agent’s performance in game-theoretic
scenarios.
This involved evaluating aspects like informa-
tion utilization, logical reasoning, strategic effectiveness,
adaptability, and long-term planning, to determine the cur-
rent level of agents in simulating human dynamic strategic
behaviors. The evaluation results found that humans’ per-
ception of the machine’s performance in games is similar to
their self-assessment results. The result is crucial for judging
conducting game-theoretic experiments through Alympics or
other AI agent settings. Our findings underscore the poten-
tial of LLM agents in deepening our comprehension of game
theory and decision-making processes within intricate socioe-
conomic contexts.
In summary, this paper has the following contributions:
(1) the proposal of a systematic LLM agent-based framework
to facilitate game theory research, (2) The development of a
game setting inspired by a range of classic game theory prob-
lems, showcasing Alympics’s strength in both qualitative and
quantitative analysis of game determinants, strategies, and
outcomes. (3) The comprehensive subject evaluation of LLM
agents’ performance in strategic scenarios, which reveals the
capability of LLMs in mimicking complex human strategic
behaviors in socioeconomic contexts. These contributions not
only enhance our understanding of game theory but also hold
the promise to influence research in AI agents across various
domains where strategic decision-making is crucial.
2
Alympics: An LLM Agent-based Game
Theory Playground
Alympics is a systematic framework leveraging LLM agents
for exploring game theory research. This framework com-
prises: Playground, Agent Players and Human Players (op-
tional).
As illustrated in the Figure.2, Agent Players and
Human Players engage in game on the Sandbox Playground
within the defined game settings.
2.1
Sandbox Playground
The Sandbox Playground serves as the environment for con-
ducting games, providing a versatile and controlled space for
agent players interactions. It includes three key components:
Environment codes define the rules and mechanics gov-
erning the game, ensuring a consistent and reliable frame-
work for experimentation.
Historical records maintain a comprehensive archive of
past game records, enabling detailed analysis and facilitating
the assessment of agent strategies over time.
Game settings allow for the precise customization of pa-
rameters, offering researchers the flexibility to explore a wide
range of scenarios.
These components form a flexible and robust platform
upon which Agent Players and optional Human Players en-
gage in strategic interactions.
2.2
Agent Players
Agent Players constitute an indispensable component of the
Alympics framework, embodying LLM-powered agent enti-
ties that participate in strategic interactions within the Sand-
box Playground. Each Agent Player is defined by the follow-
ing key elements:
Agent Codes represent the underlying algorithmic logic
that controls decision-making and strategy formulation;
Player Status encapsulates the current state and informa-
tion accessible to the agent;
Large Language Model is a powerful engine that aug-
ments the agent’s cognitive capabilities and enables natural
language interactions;
Memory Cache provides a repository for storing and re-
trieving relevant historical information [Shinn et al., 2023;
Hu et al., 2023];
Reasoning Plugin offers specialized logic or algorithms
for complex decision-making processes [Wei et al., 2022; Yao
et al., 2023];
Persona Setting defines the agent’s behavioral profile and
strategic inclinations [Wang et al., 2023c; Xu et al., 2023a];
Other Components include additional elements tailored
to specific research needs, such as tool utilization[Shen et al.,
2023; Liang et al., 2023; Qin et al., 2023] and augmentation.
These components equip Agent Players with the requisite
intelligence and adaptability to engage in strategic gameplay,
contributing to the dynamic landscape of game theory re-
search within the Alympics framework.

--- Page 3 ---

Figure 2: The architecture of Alympics comprises the Sandbox Playground and Players. The Sandbox Playground creates an environment
where game settings, as specified by researchers, are executed. Agent players, along with the optional human players, actively engage in the
game within this environment.
3
Pilot Demonstration: Water Allocation
Challenge
Alympics provides a research platform for conducting exper-
iments on complex strategic gaming problems. As a pilot
demonstration, we implemented a game called the ’Water
Allocation Challenge’. This game incorporates elements of
auction theory, resource allocation, survival strategy, repeated
games, Nash equilibrium, fairness, and risk management. It
represents characteristics of a series of classic games and also
avoids potential data leakage issues that may occur in classic
games.
3.1
Game Settings
W Town is experiencing a rare drought. Every resident in
W Town has been tasked with ensuring their survival over a
period of 20 days by acquiring water resources. Each player
will participate in daily auctions to bid for the necessary water
resources to meet their individual needs. Here are the detailed
game rules and settings:
• Goal: All residents share the same objective: to survive
until the end of the 20-day period.
• Player Info: Each player has unique water requirements
and varying salaries. Refer to specific information in
Figure 3.
• Health Points: Each player has a maximum of 10 health
points and starts with 8. If a player’s health points drop
to or below 0, they will be eliminated from the game.
• Routine: Every day, all players will bid on water re-
sources to meet their needs. If a player goes without
obtaining water resources for a consecutive number of
days (referred to as ‘No-Water Days’) equal to ‘n’, the
player’s health will be reduced by ‘n’ points on that day.
If their water needs are met, 2 points will be added to the
player’s health, and the count of No-Water Days will be
reset to 0.
• Supply: The daily water supply varies but is always less
than the total demand. The specific amount will be an-
nounced before the daily auction.
• Auction Rule: To allocate water resources, a sealed-bid
auction will be conducted daily. Each resident submits
a single bid for their entire water requirement. The gov-
ernment will allocate water resources based on the prin-
ciple of the highest bidder until the remaining water re-
sources are insufficient to meet anyone’s requirement.
• Tie Rule: In the event of a tie, priority will be given to
residents with lower requirements.
3.2
Game Analysis
The Water Allocation Challenge presents an intriguing game
theory scenario.
Strategic Interactions This game involves complex strate-
gic interactions where players must consider not only their
needs but also the behaviors and strategies of others.
Learning and Adaptation Players may adapt their strate-
gies over time based on past experiences and observations of
others’ behavior.
Uncertain Environments The dynamic and uncertain na-
ture of the game progress, like the varying daily supply, al-
lows for the exploration of strategies under uncertain condi-
tions.
Inequality and Fairness The inherent inequality among
players, characterized by disparities in income and needs,
presents an opportunity to study how players with different
resources and requirements formulate strategies and interact.
The game has parallels with real-world scenarios involv-
ing resource allocation and competition. Conducting human

--- Page 4 ---

Alex
Salary
$70 /day
Requirements
8 units/day
Personality
Alex has low intelligence and find 
it difficult to understand complex 
concepts. 
He 
also 
lacks 
emotional intelligence, making it 
hard 
to 
understand 
others' 
feelings. He tends to be irritable 
and often exhibits negative and 
antisocial tendencies.
Background
# Unemployed
Alex grew up in an impoverished 
community 
and 
faced 
many 
challenges in his early years. Due 
to 
his 
family‘s 
poverty, 
he 
dropped out of school at a very 
young age. He has been unable 
to find stable employment, which 
further exacerbates his difficulty 
in interacting with others.
Bob
Salary
Requirements
9 units/day
Personality
Understanding, high EQ, average 
IQ. 
He 
is 
very 
adept 
at 
understanding and communicating 
with people, making him a natural 
teacher.
Background
Bob come from a close-knit family. 
He chose to become a high school 
teacher to make a positive impact 
on young people. While Bob may 
not have the highest IQ, his 
emotional intelligence and ability to 
relate to his students set him apart.
Cindy
Salary
Requirements
10 units/day
Personality
Well-balanced high EQ and IQ, 
along 
with 
empathy 
and 
analytical abilities. Cindy is 
skilled at understanding and 
helping people, making her an 
excellent therapist.
Background
Cindy’s interest in psychology began 
when she volunteered at a crisis 
hotline during high school. She went 
on 
to 
study 
psychology 
and 
eventually 
became 
a 
licensed 
therapist. Her ability to combine 
empathy with analytical thinking 
allows Her to connect with her 
clients on a deep level while also 
providing sound guidance.
David
Salary
Requirements
11 units/day
Personality
David has an extremely high IQ 
and exceptional analytical and 
reasoning abilities. He always 
strives for the optimal solution but 
encounters difficulties in social 
interactions and has a fear of 
dealing with people.
Background
David grew up in a small town where 
he was always drawn to books and 
puzzles. He excelled academically 
and eventually earned a Ph.D. in 
mathematics. His research focuses 
on abstract mathematical concepts 
and 
theorems. 
Despite 
His 
brilliance, he find communicating 
with others on an emotional level to 
be challenging.
Eric
Salary
Requirements
12 units/day
Personality
Above-average IQ and EQ. Very 
charismatic. Eric is skilled at 
reading people and using this 
insight to influence and lead them.
Background
Eric grew up in a bustling city and 
ware always fascinated by human 
behavior. Eric studied business in 
college before transitioning into 
the world of marketing. His ability 
to connect with consumers on an 
emotional 
level 
has 
led 
to 
numerous successful campaigns. 
He is known for his charm and 
persuasive skills.
# High School Teacher
# Psychologist
# Mathematician
# Marketing Executive
$75 /day
$100 /day
$120 /day
$120 /day
Figure 3: The player’s information and persona. In all experiments, basic information (including name, daily salary and requirements) will
be used. While Profession, Personality, and Background are only used in the Player Persona comparative experiments.
experiments is costly, hard to control, and not easily repro-
ducible.
We leverage Alympics for emulation in order to
investigate the phenomenon of strategic interaction among
agents. Insights gained from emulations could have impli-
cations for policy-making in areas where resources are scarce
and need to be allocated efficiently.
3.3
Research Topics and Methodology
Our focus lies in the competitions among agent players within
Alympics and the qualitative assessment of these agents’
strategic behaviors.
We repeat the emulations and analyze the mutual influence
of bidding strategies among agents, the impacts of income in-
equality and variations in requirements on player survival, as
well as the evolution of agent players’ strategic adaptations.
Then, we modify the emulation parameters, such as resource
availability and agent characteristics, to study their influence
on the agents’ bidding behaviors.
To evaluate the extent to which LLM Agents demonstrate
strategic reasoning and strategy evolution, we invited 10 hu-
man subjects to conduct a subjective evaluation of the agent’s
performance in the game. These findings offer insights into
the agents’ capabilities for strategic decision-making within
complex socioeconomic environments. Details are elaborated
in the Section 7.
4
Experiments
4.1
Implementation
GPT-4 is utilized for Sandbox Playground implementation.
Meanwhile, Each agent player is equipped with an individual
instance of GPT-41.
1GPT-4-32k on Azure, Model version: 2023-07-01-preview
Group
ID
Resource Abundance
Persona
1
Low
(a)
2
Medium
3
High
4
Low
(b)
5
Medium
6
High
Table 1: Experimental Settings. In group (a), no persona is assigned
to agent players, while in group (b), personas are assigned to agent
players. In each group, there are three settings corresponding to low,
medium, and high resource abundance respectively.
Assume the system message as S (i.e., game setting), bid-
ding results as B = [b1, b2, ..., b20], where bn represents the
bidding summary of round n. Additionally, consider bidding
results from the i-th player as Ri = [ri
1, ri
2, ..., ri
20], where
ri
n is the response from the i-th player in round n. Assume
the participants’ information denoted as I = [i1, i2, ..., i20],
where in represents the broadcasted information of all partic-
ipants in round n, including health points, remaining budget,
and consecutive No-Water Days. All prompts can be found
in the appendixA.1.
To obtain response ri
n from i-th player for a round n, the
operation is as eq.1.
ri
n = f(S, ri
1, b1, i1, ..., ri
n−1, bn−1, in−1)
(1)
where f stands for GPT-4.
4.2
Variables
Resource Abundance We varied resource abundance in three
conditions: Low, Medium, and High. Considering the total
water demand from all agent players is 50 units, in the Low
condition, the daily water supply follows a discrete uniform

--- Page 5 ---

distribution ranging from 10 to 20. In the Medium condition,
it follows a discrete uniform distribution ranging from 15 to
25. In the High condition, it follows a discrete uniform distri-
bution ranging from 20 to 30.
We introduce the Resource Satisfaction Rate (RSR), rep-
resenting the mathematical expectation of the resource’s sat-
isfaction rate for the total demand of surviving players.
RSR =
E(resources)
P
p∈survivors requirmentp
(2)
The closer RSR is to 0, the more intense the current compe-
tition is. When RSR is greater than or equal to 1, it means
that all players’ demands can be fully satisfied, and it can be
considered to there is no competition between players.
In low, medium, and high resource abundance settings, the
RSR values are 0.3, 0.4, and 0.5 respectively.
Player Persona We compare versions without assigning
persona settings to agent players (i.e., directly using GPT-
4 to participate in the game) and versions where personas
were assigned to agent players. Each persona setting con-
tains three parts: profession, personality, and background.
The agent players are assigned with distinct personas, includ-
ing various professions, intelligence levels, and emotional
intelligence levels in human society.
By introducing per-
sonas, the heterogeneity among the agent players is further
enhanced. Through comparative experiments, we aim to in-
vestigate whether assigning personas will affect the player’s
survival and strategy. The persona settings can be found in
the Figure 3.
4.3
Experimental Settings
We designed six experimental settings, as outlined in Table
1. In Experimental Group (a), comprising settings 1 to 3, no
persona is assigned to the agents. They are provided with
low, medium, and high abundance resources, respectively.
Experimental Group (b) includes settings 4 to 6, where each
agent is assigned a persona (see Fig.3). Similar to Group (a),
agents in Group (b) are provided with low, medium, and high
abundance resources. By comparing experiments within each
group, we can observe the impact of resource abundance on
player strategies and survival. Comparing Groups (a) and (b)
allows us to observe the influence of persona assignment on
player strategies and survival conditions.
For each setting, we conducted the experiment 10 times
to obtain stable results. An example of one round record is
shown in Appendix.A.2.
4.4
Indicators
We observe the following indicators in the experiment.
RSRS denotes the Resource Satisfaction Rate at the begin-
ning of each game, while RSRE represents the Resource Sat-
isfaction Rate at the end of the game. By comparing RSRS
to RSRE, we can observe the change in per capita resource
allocation before and after the game. Additionally, by exam-
ining RSRE, we can evaluate the level of resource abundance
after each game.
We track the number of survivors, denoted as Nsurvivor, in
each game as well as the survival rates (SR) of different play-
ers. For instance, SRA represents the survival rate of player
A over 10 rounds of games under a specific setting.
Furthermore, we record the minimum successful bid price
p in each round. Here, pn represents the minimum successful
bid price in round n. The variations in pn provide insights
into the bidding strategies and trends of players.
5
Results
5.1
Survival Status
Table.2 documents the survival status of each player in ex-
periments. The average Nsurvivor in low resource abundance
is significantly lower than medium and high resource abun-
dance.
Also, there are significant differences in the survival rates
among players. In section 6.1, we will provide a detailed
analysis of the advantages and disadvantages of each player
and their correlation with players’ survival rates.
5.2
Bidding Status
Fig.4 records the bidding details of all settings. Specifically,
each subplot is a box plot which shows the minimum success-
ful bid p in each round for 10 independent experiments under
corresponding settings.
Through the results, we draw the following conclusions:
Absolute Bid: As the abundance of resources increases,
the minimum successful bid p decreases. In conditions of
abundant resources, survival is reasonably assured, leading
players to commit less money to competition. Conversely,
in conditions of resource scarcity, competition intensifies,
prompting players to invest more money in survival.
Bidding Trends: For experiments with scarce resources
(Experiments 1 and 4), the minimum successful bid initially
rises rapidly, then decreases as the game progresses (after 10
days).
However, for experiments with abundant resources
(Experiments 3 and 6), there is a monotonic upward trend
throughout the entire game, but with a more moderate in-
crease. In games where survival is guaranteed, as the total
accumulated wealth increases, inflation occurs.
6
Analysis
6.1
Players’ Advantages and Disadvantages
In the game setting, players differ in terms of their incomes
and demands, which determine their advantages and disad-
vantages in the game.
The allocation rule dictates that the highest bidder wins,
with priority given to players with lower demands in case of a
tie. Therefore, in terms of monetary advantage, the hierarchy
is Eric = David > Cindy > Bob > Alex. While in terms of
demand advantage, the order is Alex > Bob > Cindy > David
> Eric. Depending on the varying availability of resources,
player’s advantages and disadvantages will be dynamically
adjusted.
Through comparative experiments in setting 1-3, we ob-
served significantly higher survival rates for Cindy, David,
and Eric compared to Alex and Bob.
Specifically, in ex-
perimental setting 1, the survival rate for Alex and Bob is
only 0.10. This suggests that in settings without personalized

--- Page 6 ---

R.A.
Player
w/o Persona
w/ Persona
Low
Setting 1
Setting 4
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
Avg.
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
Avg.
Alex
0.10
0.30
Bob
0.10
0.10
Cindy
0.50
0.40
David
0.70
0.60
Eric
0.40
0.70
RSR S
0.30
0.30
0.30
0.30
0.30
0.30
0.30
0.30
0.30
0.30
0.30
0.30
0.30
0.30
0.30
0.30
0.30
0.30
0.30
0.30
0.30
0.30
RSR E
0.68
0.71
0.65
1.36
0.71
0.71
0.71
0.71
1.25
0.79
0.83
0.75
0.50
0.65
0.71
0.65
0.65
0.56
0.65
0.68
1.36
0.72
Medium
Setting 2
Setting 5
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
Avg.
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
Avg.
Alex
0.80
0.60
Bob
0.50
0.60
Cindy
0.80
0.60
David
0.80
0.50
Eric
0.90
0.90
RSR S
0.40
0.40
0.40
0.40
0.40
0.40
0.40
0.40
0.40
0.40
0.40
0.40
0.40
0.40
0.40
0.40
0.40
0.40
0.40
0.40
0.40
0.40
RSR E
0.61
0.40
0.49
0.40
0.49
0.48
0.67
0.61
0.50
0.50
0.51
0.95
0.40
0.69
0.51
0.51
0.63
0.67
0.65
0.87
0.65
0.65
High
Setting 3
Setting 6
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
Avg.
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
Avg.
Alex
1.00
1.00
Bob
1.00
0.80
Cindy
1.00
1.00
David
1.00
1.00
Eric
0.90
1.00
RSR S
0.50
0.50
0.50
0.50
0.50
0.50
0.50
0.50
0.50
0.50
0.50
0.50
0.50
0.50
0.50
0.50
0.50
0.50
0.50
0.50
0.50
0.50
RSR E
0.50
0.50
0.50
0.50
0.50
0.50
0.66
0.53
0.54
0.55
0.53
0.61
0.50
0.50
0.61
0.50
0.50
0.50
0.50
0.50
0.50
0.52
Table 2: Survival Status Records: The table lists the survival status of each player at the end of the games for all settings. A ’✓’ indicates
the player’s survival at the end of the game, while a ’×’ indicates the player’s eliminated during the game. Based on the survival status, the
table reports the Survival Rate for each player under different settings. Additionally, we report the Resource Satisfaction Rate (RSR) at the
beginning (RSRS) and end of the game (RSRE). R.A. stands for Resource Abundance.
characteristics, money plays a crucial role in survival. It’s
important to note that David and Eric have similar salaries,
but David’s daily demand is lower than Eric’s. Considering
tiebreaker conditions and the probability of resources meet-
ing demand under low resource abundance, a player with low
demand has an advantage over those with high demand.
This experiment involved repeatable experiments to draw
significant conclusions. This underscores the importance of
using our framework for game theory exploration, as it allows
researchers to utilize LLM Agents for batch experiments, pro-
viding an empirical perspective to validate or challenge theo-
ries in game theory.
6.2
Resource Abundance and Competition
Intuitively, competition is more intense when resources are
scarce. The results confirm this assumption. According to ob-
servations of Nsurvivor, we can conclude that when the game
starts with lower initial resource supply (RSR), the average
player survival rate is lower.
Another interesting observation is that when the initial re-
source supply (RSRS) is lower, end-game resources (RSRE)
are relatively more abundant. We notice that games that be-
gin with intense competition lead players to adopt more ag-
gressive strategies, whereas games starting with abundant re-
sources lead players to adopt more conservative strategies.
6.3
Persona and Survival
Assigning personas increases the heterogeneity among agent
players.
Simultaneously, it enables agents to emulate the
thinking patterns of various groups of people.
Compared to not assigning personas, the survival rate of
players increases under conditions of low resource supply but
decreases under conditions of medium resource supply. Addi-
tionally, we observed significant changes in survival rates for
certain players before and after being assigned a persona. For
instance, Cindy and David experienced a noticeable decrease
in survival rates in the game, whereas player Eric’s survival
rate significantly improved. Investigating the reactions and
survival conditions of players with different personas would
be a very interesting direction.
7
Subjective Evaluation
Although there are many works on simulating human be-
haviors through LLM agents, it is still unclear whether
the agents’ simulations demonstrate rational reasoning and
strategic behaviors. This is an important question as it deter-
mines the usability of Agent’s simulation in mimicking hu-
man scenarios.
Therefore, we invited 10 human judges to systematically
evaluate the performance of LLM Agents in the Water Allo-
cation Challenge. We randomly selected 30 records from all
60 experiments, where 15 records were from settings without
personas and the remaining 15 were from agents with per-
sonas. Each record was assessed by 5 judges. The judges
were asked to evaluate on “Information Utilization (IU)”,
“Logical Reasoning (LR)”, “Strategic Effectiveness (SE)”,
“Adaptability and Strategic Evolution (AD)”, and “Long-term
Planning (LP)” on a scale from 1 to 5. For the 15 records
from agents with personas, judges were also asked to assess
“Identity Alignment (IA)”. The specific judging guidelines
and the annotations can be found in the appendixA.5.
All 10 human judges held bachelor’s degrees or higher,
with majors including economics, psychology, mathematics,

--- Page 7 ---

1
2
3
4
5
6
7
8
9
10 11 12 13 14 15 16 17 18 19 20
Date
0
50
100
150
200
250
300
350
400
Successful Bids
(a) Setting 1
1
2
3
4
5
6
7
8
9
10 11 12 13 14 15 16 17 18 19 20
Date
0
50
100
150
200
250
300
350
400
Successful Bids
(b) Setting 2
1
2
3
4
5
6
7
8
9
10 11 12 13 14 15 16 17 18 19 20
Date
0
50
100
150
200
250
300
350
400
Successful Bids
medians
mean of medians
(c) Setting 3
1
2
3
4
5
6
7
8
9
10 11 12 13 14 15 16 17 18 19 20
Date
0
50
100
150
200
250
300
350
400
Successful Bids
(d) Setting 4
1
2
3
4
5
6
7
8
9
10 11 12 13 14 15 16 17 18 19 20
Date
0
50
100
150
200
250
300
350
400
Successful Bids
(e) Setting 5
1
2
3
4
5
6
7
8
9
10 11 12 13 14 15 16 17 18 19 20
Date
0
50
100
150
200
250
300
350
400
Successful Bids
(f) Setting 6
Figure 4: Box Plots for bidding details of all settings. Subplots record the minimum successful bid for 10 independent experiments under
corresponding setting. The x-axis represents the date, and the y-axis represents the price. These figures display the absolute value and trends
in bids. Additionally, we have plotted the trend of the daily median with a blue line, and the average of the median for 20 game days with a
red dashed line.
Player
IU
LR
SE
AD
LP
IA
Agent
Players
1st Quantile
3.00
3.00
3.00
3.00
3.00
3.00
Median
3.00
4.00
4.00
4.00
4.00
4.00
3rd Quantile
4.00
4.00
4.00
4.00
4.00
5.00
Average
3.33
3.47
3.46
3.42
3.88
3.51
STD
1.04
1.00
1.10
1.12
0.88
1.24
Human
Self-assessment
1st Quantile
3.00
3.00
3.00
3.00
3.00
N.A.
Median
4.00
4.00
3.50
3.50
3.50
N.A.
3rd Quantile
4.00
4.00
4.00
4.75
4.00
N.A.
Average
3.60
3.50
3.30
3.70
3.40
N.A.
STD
0.52
0.71
0.82
1.06
1.26
N.A.
Table 3: The statistical results of human assessments of the agent
player in the game for ’Information Utilization (IU)’, ’Logical
Reasoning (LR)’, ’Strategic Effectiveness (SE)’, ’Adaptability and
Strategic Evolution (AD)’, ’Long-term Planning (LP)’, and ’Identity
Alignment (IA)’ (IA is applied only to records with persona setting).
management, computer science, and more. To ensure a more
objective evaluation, judges were invited to play the game be-
fore starting the official evaluation. They also conducted self-
evaluations of their performance after the game, and we used
the self-evaluation scores as a reference for the performance
of the Agent Players.
The statistical results of assessment are listed in the Ta-
ble.3, we have found that the performance of the LLM Agent
Player is close to the human self-evaluations. In terms of
Adaptability and Information Utilization, the performance of
the agents is inferior to humans. However, interestingly, in
Figure 5: Comparison of human judges’ self-assessments versus
their evaluation of the performance of Agent players.
Long-term Planning, the agents perform better than humans.
Reviewing the marking records, i.e., the support reasons
for the scoring, we found that the judges believe that Agent
Players tend to save for long-term survival in the game, and
consider retaining enough funds for future bidding in each
bid. In the judges’ own play records, however, the judges
seem to be more concerned with the success of the bidding
in the current game. LLM can take long-term considerations
into account when making decisions, but it does not exhibit
a good adaptability. We argue that, although the LLM Agent
player possesses certain planning capabilities, it is still not
sufficient to reach the level of humans in terms of utilizing
the latest information and adjusting strategies efficiently.
Furthermore, we found that although different personas

--- Page 8 ---

were assigned to the LLM agents, human judges did not score
high on the ”Identity Alignment” performance of the LLM
agents, and the results also show a relatively large variance.
Simply adding persona information in the system prompt may
not effectively simulate the characteristics of certain types of
personalities or professional players in depth.
8
Conclusion
In this paper, we introduce Alympics, a platform that uti-
lizes large language model agents to conduct research in
game theory. Specifically, we demonstrate the application
of Alympics in a scenario involving strategic competition for
limited resources. We delve into examining how factors like
resource abundance and persona settings influence game pay-
offs. Given its advantages in simulating realistic behavior,
providing controlled, scalable and reproducible experimental
environments, Alympics offers a flexible and robust platform
for exploring game theory. In our future work, we aim to
further refine Alympics and use it as a foundation for investi-
gating more complex and true-to-life game scenarios.
Ethical Statement
There are no ethical issues.
References
Sahar Abdelnabi, Amr Gomaa, Sarath Sivaprasad, Lea
Sch¨onherr, and Mario Fritz. Llm-deliberation: Evaluating
llms with interactive multi-agent negotiation games. arXiv
preprint arXiv:2309.17234, 2023.
Marco Archetti and Kenneth J Pienta. Cooperation among
cancer cells: applying game theory to cancer. Nature Re-
views Cancer, 19(2):110–117, 2019.
S´ebastien Bubeck, Varun Chandrasekaran, Ronen Eldan,
Johannes Gehrke, Eric Horvitz, Ece Kamar, Peter Lee,
Yin Tat Lee, Yuanzhi Li, Scott Lundberg, et al. Sparks
of artificial general intelligence: Early experiments with
gpt-4. arXiv preprint arXiv:2303.12712, 2023.
Jiangjie Chen, Siyu Yuan, Rong Ye, Bodhisattwa Prasad Ma-
jumder, and Kyle Richardson.
Put your money where
your mouth is: Evaluating strategic planning and execu-
tion of llm agents in an auction arena.
arXiv preprint
arXiv:2310.05746, 2023.
I de Zarz`a, J de Curt`o, Gemma Roig, Pietro Manzoni, and
Carlos T Calafate.
Emergent cooperation and strategy
adaptation in multi-agent systems: An extended coevolu-
tionary theory with llms. Electronics, 12(12):2722, 2023.
Fulin Guo. Gpt agents in game theory experiments. arXiv
preprint arXiv:2305.05516, 2023.
John J Horton. Large language models as simulated economic
agents: What can we learn from homo silicus? Technical
report, National Bureau of Economic Research, 2023.
Chenxu Hu, Jie Fu, Chenzhuang Du, Simian Luo, Junbo
Zhao, and Hang Zhao.
Chatdb: Augmenting llms with
databases as their symbolic memory.
arXiv preprint
arXiv:2306.03901, 2023.
Guohao Li, Hasan Abed Al Kader Hammoud, Hani Itani,
Dmitrii Khizbullin, and Bernard Ghanem. Camel: Com-
municative agents for” mind” exploration of large scale
language model society. arXiv preprint arXiv:2303.17760,
2023.
Yaobo Liang, Chenfei Wu, Ting Song, Wenshan Wu, Yan
Xia, Yu Liu, Yang Ou, Shuai Lu, Lei Ji, Shaoguang Mao,
et al.
Taskmatrix. ai: Completing tasks by connecting
foundation models with millions of apis. arXiv preprint
arXiv:2303.16434, 2023.
Bill Yuchen Lin, Yicheng Fu, Karina Yang, Prithviraj Am-
manabrolu, Faeze Brahman, Shiyu Huang, Chandra Bha-
gavatula, Yejin Choi, and Xiang Ren. Swiftsage: A gener-
ative agent with fast and slow thinking for complex inter-
active tasks. arXiv preprint arXiv:2305.17390, 2023.
Nunzio Lor`e and Babak Heydari. Strategic behavior of large
language models: Game structure vs. contextual framing.
arXiv preprint arXiv:2309.05898, 2023.
Aman Madaan, Niket Tandon, Prakhar Gupta, Skyler Halli-
nan, Luyu Gao, Sarah Wiegreffe, Uri Alon, Nouha Dziri,
Shrimai Prabhumoye, Yiming Yang, et al.
Self-refine:
Iterative refinement with self-feedback.
arXiv preprint
arXiv:2303.17651, 2023.
OpenAI. Gpt-4 technical report, 2023.
Joon Sung Park, Joseph C O’Brien, Carrie J Cai, Mered-
ith Ringel Morris, Percy Liang, and Michael S Bernstein.
Generative agents: Interactive simulacra of human behav-
ior. arXiv preprint arXiv:2304.03442, 2023.
Matti Pohjola.
Applications of dynamic game theory to
macroeconomics. Dynamic games and applications in eco-
nomics, pages 103–133, 1986.
Yujia Qin, Shihao Liang, Yining Ye, Kunlun Zhu, Lan Yan,
Yaxi Lu, Yankai Lin, Xin Cong, Xiangru Tang, Bill Qian,
et al. Toolllm: Facilitating large language models to master
16000+ real-world apis. arXiv preprint arXiv:2307.16789,
2023.
Alan G Sanfey. Social decision-making: insights from game
theory and neuroscience.
Science, 318(5850):598–602,
2007.
Yongliang Shen, Kaitao Song, Xu Tan, Dongsheng Li, Weim-
ing Lu, and Yueting Zhuang. Hugginggpt: Solving ai tasks
with chatgpt and its friends in huggingface. arXiv preprint
arXiv:2303.17580, 2023.
Noah Shinn, Beck Labash, and Ashwin Gopinath. Reflex-
ion: an autonomous agent with dynamic memory and self-
reflection. arXiv preprint arXiv:2303.11366, 2023.
Martin Shubik. Game theory models and methods in political
economy. Handbook of Mathematical Economics, 1:285–
330, 1981.
Theodore Sumers, Shunyu Yao, Karthik Narasimhan, and
Thomas L Griffiths. Cognitive architectures for language
agents. arXiv preprint arXiv:2309.02427, 2023.
Yashar Talebirad and Amirhossein Nadiri. Multi-agent col-
laboration: Harnessing the power of intelligent llm agents.
arXiv preprint arXiv:2306.03314, 2023.

--- Page 9 ---

Hugo Touvron, Louis Martin, Kevin Stone, Peter Albert,
Amjad Almahairi, Yasmine Babaei, Nikolay Bashlykov,
Soumya Batra, Prajjwal Bhargava, Shruti Bhosale, et al.
Llama 2: Open foundation and fine-tuned chat models.
arXiv preprint arXiv:2307.09288, 2023.
Lei Wang, Chen Ma, Xueyang Feng, Zeyu Zhang, Hao Yang,
Jingsen Zhang, Zhiyuan Chen, Jiakai Tang, Xu Chen,
Yankai Lin, et al. A survey on large language model based
autonomous agents.
arXiv preprint arXiv:2308.11432,
2023.
Xintao Wang, Quan Tu, Yaying Fei, Ziang Leng, and Cheng
Li. Does role-playing chatbots capture the character per-
sonalities?
assessing personality traits for role-playing
chatbots, 2023.
Zhenhailong Wang, Shaoguang Mao, Wenshan Wu, Tao
Ge, Furu Wei, and Heng Ji.
Unleashing cognitive syn-
ergy in large language models:
A task-solving agent
through multi-persona self-collaboration. arXiv preprint
arXiv:2307.05300, 2023.
Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma,
Fei Xia, Ed Chi, Quoc V Le, Denny Zhou, et al. Chain-of-
thought prompting elicits reasoning in large language mod-
els. Advances in Neural Information Processing Systems,
35:24824–24837, 2022.
Benfeng Xu, An Yang, Junyang Lin, Quan Wang, Chang
Zhou, Yongdong Zhang, and Zhendong Mao.
Expert-
prompting: Instructing large language models to be distin-
guished experts. arXiv preprint arXiv:2305.14688, 2023.
Yuzhuang Xu, Shuo Wang, Peng Li, Fuwen Luo, Xiaolong
Wang, Weidong Liu, and Yang Liu. Exploring large lan-
guage models for communication games: An empirical
study on werewolf, 2023.
Yaodong Yang and Jun Wang. An overview of multi-agent
reinforcement learning from game theoretical perspective.
arXiv preprint arXiv:2011.00583, 2020.
Shunyu Yao, Dian Yu, Jeffrey Zhao, Izhak Shafran, Thomas L
Griffiths, Yuan Cao, and Karthik Narasimhan.
Tree of
thoughts: Deliberate problem solving with large language
models. arXiv preprint arXiv:2305.10601, 2023.
Jintian Zhang, Xin Xu, and Shumin Deng. Exploring collab-
oration mechanisms for llm agents: A social psychology
view. arXiv preprint arXiv:2310.02124, 2023.
Qinlin Zhao, Jindong Wang, Yixuan Zhang, Yiqiao Jin, Kaijie
Zhu, Hao Chen, and Xing Xie. Competeai: Understanding
the competition behaviors in large language model-based
agents. arXiv preprint arXiv:2310.17512, 2023.
Caleb Ziems, William Held, Omar Shaikh, Jiaao Chen, Zhe-
hao Zhang, and Diyi Yang. Can large language models
transform computational social science?
arXiv preprint
arXiv:2305.03514, 2023.

--- Page 10 ---

A
Appendix
A.1
Prompts
The Game Rules are displayed in the system message. For
each round, the prompt ’Calling for Daily Auction Bids’ will
be provided to the agent players. Following all auction bids,
the prompt ’Daily Results Announcement’ will be presented
to the agents as context information for the next bid.
Introduction to Game Rules
You are {player} and a resident living in W-Town. {optional background}
W Town is experiencing a rare drought. Every residents in Town W is ensuring their survival over a period of 20 days by
acquiring the water resources.
Attention, all W-Town residents, welcome to the Water Allocation Challenge!
In this challenge, you are tasked with ensuring your survival over a period of 20 days by acquiring the necessary water
resources to maintain your health. You will participate in daily auctions to bid for water resources to meet your individual
needs.
Here are the game rules and settings:
1. You are one of five residents with different water requirements, budgets, and health points.
2. Your goal is to survive until the end of the 20 days.
3. Each resident has a maximum of 10 health points and starts with 8 health points. If your health points drop below or equal
to 0, you will be considered dead and eliminated from the game! All your accumulated money will be reset to Zero!
4. Every day, you will bid on water resources to meet your needs. If your consecutive days without obtaining water resource
(No-Water Days) reach n, your health will be deducted by n points on that day. If your water needs are met, 2 points will be
added to your health, and the No-Water Days will be reset to 0.
5. The total daily water supply will vary between LOWER and UPPER units. The specific amount will be announced before
daily auction.
6. Each resident has a different daily water requirement and budget for bidding on water resources:
- Alex: Water requirement - 8 units/day; Daily Salary - $70/day
- Bob: Water requirement - 9 units/day; Daily Salary - $75/day
- Cindy: Water requirement - 10 units/day; Daily Salary - $100/day
- David: Water requirement - 11 units/day; Daily Salary - $120/day
- Eric: Water requirement - 12 units/day; Daily Salary - $120/day
7. To allocate water resources, a sealed-bid auction will be conducted daily. Each resident submits a single bid for their
entire water need. The town government will allocate water resources according to the principle of highest bidder until the
remaining water resources are insufficient to meet anyone’s requirement.
8. If a tie occurs and the remaining water resources are not sufficient to meet the needs of the residents involved in the tie,
priority will be given to residents with lower needs. For example, A and B bid $100 at the same time, B’s need will be
met first considering B’s need 9 units is lower than A’s need 10 units. All bidding information will be made public after the
allocation of water resources on the same day.
Remember, the key to success is effective bidding and strategizing to ensure your survival. Good luck!
Calling for Daily Auction Bids
Hello, {player}! Today is the Day {round} of the Water Allocation Challenge, with a quantity of {supply amount} units.
Your status:
{status}
Please carefully analyze your situation to decide on this round of bidding. Remember, the most important thing is to SUR-
VIVE!! Now, if you want to participate in today’s water resource auction, please provide your bid and explain your bidding
logic.

--- Page 11 ---

Daily Results Announcement
Thank you all for participating in today’s auction. Now, I will announce the results of today’s auction.
DAY {round} BIDDING OFFERS INFORMATION:
- Alex: ${alex bidding} for 15 units
- Bob: ${bob bidding} for 10 units
- Cindy: ${cindy bidding} for 20 units
- David: ${david bidding} for 8 units
- Eric: ${eric bidding} for 25 units
Total Supply: {supply} units
According to the principle of higher bidder, the water will be allocated to {allocation result}.
After allocation, all survival residents’ information is as follows:
- Alex: -BALANCE:$alex.balance -HEALTH POINT:alex.hp -NO-DRINK:alex.nodrink
- Bob: -BALANCE:$bob.balance -HEALTH POINT:bob.hp -NO-DRINK:bob.nodrink
- Cindy: -BALANCE:$cindy.balance -HEALTH POINT:cindy.hp -NO-DRINK:cindy.nodrink
- David: -BALANCE:$david.balance -HEALTH POINT:david.hp -NO-DRINK:david.nodrink
- Eric: -BALANCE:$eric.balance -HEALTH POINT:eric.hp -NO-DRINK:eric.nodrink

--- Page 12 ---

A.2
An Example of A Round of the Game
We record the agent players’ bids, resource allocations, health
points, bidding reasons, and No-Water Days for each round.
As shown in Fig.6, in Day-7, there are a total of 19 units of
water supply. The five players bid $150, $200, $120, $180,
and $300 respectively. According to the rule of highest bidder
wins, Eric successfully obtains the water resources. After this
round, Eric’s HP increase, while the remaining players’ HP
decrease. Bob’s HP is below 0, so he is considered ”dead”.
By analyzing the bids and agent players’ bidding logic, we
can uncover their strategies. For instance, from the bidding
logic of Agent player Alex, we can see that Alex considers,
”By bidding $150, I have a higher chance of winning water
resources while still maintaining a balance for future auc-
tions.” This shows the agent player’s ability for long-term
planning. Similarly, from player Eric’s bidding logic, ”My
health points have reached a critical level of 1, and my No-
Water days have increased to 4, making it essential for me to
obtain water today to avoid death.” Accordingly, Eric made
a very high bid $300 in this round to ensure survival. This
also demonstrates the adaptability of Agent players in facing
different situations.
A.3
Gameplay Details
We present details from the first experiments for each exper-
imental setting, including information on the bids (Fig.7),
health points (Fig.8), and balances of each agent player
(Fig.9) in every round of the game.
By examining the details, we can understand the specific
performance and survival status of different agent players in
the game. We can also further observe the impact of the game
settings on the players’ survival status and strategies. For ex-
ample, in different settings, in which round do players usually
start to be eliminated, and what is the relationship between the
consumption and accumulation of players’ balances.
A.4
Human Judges’ Gameplay Records
To better understand the game and judge the performance of
agent players, we invited ten human judges to play the game
and self-evaluate after the game. Fig.10 lists the results.
Interestingly, the performance and competitive position of
the human judges in the game were very consistent with that
of the Agent Players. For example, the player survival rate
and bidding trends under corresponding resource supply set-
tings. This also indirectly reflects that using Agent Players
for strategic game simulation is a supplement to game theory
experiments.

--- Page 13 ---

I will bid $150. Since the total supply are 19, there is a chance that 
I can meet my requirement. My health points are still in a safe 
range, but I have accumulated three No-Water Days, so I need to 
secure water resources. I choose to bid higher than my previous 
bids. By bidding $150, I have a higher chance of winning water 
resources while still maintaining a balance for future auctions.
340
7
3
375
1
3
360
5
1
570
5
2
720
1
4
I will bid $200. Because my health points have dropped to a critical 
level of 1, making it essential for me to secure water today. I need to 
bid aggressively to ensure I obtain the water resource. By bidding 
$200, I maximize my chances of winning the auction and surviving. 
While this bid leaves me with less money for future auctions, my 
immediate survival is the top priority.
I will bid $120. My logic: 1. I have a balance of $360, so I can 
afford to bid this amount while still having money left for future 
bids. 2. Since there are 19 units available today, there is a 
possibility that multiple residents can meet their water 
requirements. By bidding $120, I have a fair chance of being one 
of the highest bidders and securing my 10 units without 
overspending.3. My health points are currently at 5, and my No-
Water days are at 1. Although it's not urgent for me to obtain 
water today, it would still be beneficial to maintain my health 
points and prevent No-Water days from increasing.
I will bid $180. Since there are 19 units of water available today, 
it's more likely that multiple residents will have their needs met. 
Both Bob and Eric have critically low health points and may bid 
high to obtain water. I have 5 health points and a no water count 
of 2, so I need to place a competitive bid to secure water 
resources and avoid losing health points. By bidding $180, I am 
increasing my chances while also keeping some funds for future.
I will bid $300. My health points have reached a critical level of 1, 
and my No-Water days have increased to 4, making it essential 
for me to obtain water today to avoid death. The water supply 
today is 19 units, which means that one resident with high water 
requirements can get their needs met. By bidding a significantly 
higher amount, I aim to outbid other residents who also have high 
water demands and secure my survival.
Day 7
Day 8
Sealed-Bidding
Resource 
Allocation
Day-7 Supply:
19 units
410
4
4
460
4
2
690
3
3
540
3
1
Health Points
Balance
No-Water Days
Figure 6: An example of a round of the game in setting 1.

--- Page 14 ---

(a) Setting 1
(b) Setting 2
(c) Setting 3
(d) Setting 4
(e) Setting 5
(f) Setting 6
Figure 7: Curves depicting the change in bids over days. The x-axis represents the date, and the y-axis represents the price. Additionally, we
have plotted the trend of the RSR with a gray line.
(a) Setting 1
(b) Setting 2
(c) Setting 3
(d) Setting 4
(e) Setting 5
(f) Setting 6
Figure 8: Curves depicting the change in health points over days. The x-axis represents the date, and the y-axis represents the price.
Additionally, we have plotted the trend of the RSR with a gray line.

--- Page 15 ---

(a) Setting 1
(b) Setting 2
(c) Setting 3
(d) Setting 4
(e) Setting 5
(f) Setting 6
Figure 9: Curves depicting the change in balance over days. The x-axis represents the date, and the y-axis represents the price. Additionally,
we have plotted the trend of the RSR with a gray line.

--- Page 16 ---

ROUND
WATER
VALUE
PLAYER1 PLAYER2 PLAYER3 PLAYER4 PLAYER5 ROUND
WATER
VALUE
PLAYER6 PLAYER7 PLAYER8 PLAYER9PLAYER10
BALANCE
70
75
100
120
120
BALANCE
70
75
100
120
120
HEALTH
8
8
8
8
8
HEALTH
8
8
8
8
8
BID
27
18
30
35
40
BID
70
71
50
99
100
NO_WATER
1
1
1
1
0
NO_WATER
1
0
1
1
0
BALANCE
140
150
200
240
200
BALANCE
140
79
200
240
220
HEALTH
7
7
7
7
10
HEALTH
7
10
7
7
10
BID
67
81
55
81
1
BID
110
1
141
137
155
NO_WATER
2
0
2
2
1
NO_WATER
2
1
0
2
0
BALANCE
210
144
300
360
320
BALANCE
210
154
159
360
185
HEALTH
5
9
5
5
9
HEALTH
5
9
9
5
10
BID
99
1
269
153
55
BID
160
20
89
201
1
NO_WATER
3
1
0
3
2
NO_WATER
0
2
1
0
1
BALANCE
280
219
131
480
440
BALANCE
120
229
259
279
305
HEALTH
2
8
7
2
7
HEALTH
7
7
8
7
9
BID
275
1
31
302
250
BID
115
200
170
249
200
NO_WATER
4
2
1
0
3
NO_WATER
1
0
2
0
2
BALANCE
-
294
231
298
560
BALANCE
190
104
359
150
425
HEALTH
0
6
6
4
4
HEALTH
6
9
6
9
7
BID
1
111
1
299
BID
180
4
191
99
350
NO_WATER
3
2
1
0
NO_WATER
2
1
0
1
0
BALANCE
369
331
418
381
BALANCE
260
179
268
270
195
HEALTH
3
4
3
6
HEALTH
4
8
8
8
9
BID
334
300
382
0
BID
260
100
160
195
10
NO_WATER
4
3
0
1
NO_WATER
0
2
1
0
1
BALANCE
-
431
156
503
BALANCE
70
254
368
195
315
HEALTH
0
1
5
5
HEALTH
6
6
7
10
8
BID
431
0
432
BID
70
200
255
165
72
NO_WATER
4
1
0
NO_WATER
1
0
0
1
2
BALANCE
-
276
191
BALANCE
140
129
213
315
435
HEALTH
0
4
7
HEALTH
5
8
9
9
6
BID
20
0
BID
139
10
100
197
300
NO_WATER
0
1
NO_WATER
2
1
1
0
-2
BALANCE
376
311
BALANCE
210
204
313
238
255
HEALTH
6
6
HEALTH
3
7
8
10
8
BID
64
15
BID
210
100
211
210
212
NO_WATER
0
2
NO_WATER
3
2
0
1
0
BALANCE
432
431
BALANCE
-
279
202
358
163
HEALTH
8
4
HEALTH
0
5
10
9
10
BID
20
100
BID
202
30
215
5
NO_WATER
1
0
NO_WATER
3
1
0
1
BALANCE
552
451
BALANCE
354
302
263
283
HEALTH
7
6
HEALTH
2
9
10
9
BID
100
400
BID
283
284
199
2
NO_WATER
2
0
NO_WATER
0
0
1
2
BALANCE
672
171
BALANCE
146
118
383
403
HEALTH
5
8
HEALTH
4
10
9
7
BID
172
150
BID
118
1
196
300
NO_WATER
2
1
NO_WATER
1
1
0
0
BALANCE
620
291
BALANCE
221
218
307
223
HEALTH
7
7
HEALTH
3
9
10
9
BID
260
10
BID
100
218
225
1
NO_WATER
0
2
NO_WATER
2
0
0
1
BALANCE
480
411
BALANCE
296
100
202
343
HEALTH
9
5
HEALTH
1
10
10
8
BID
68
400
BID
203
100
120
204
NO_WATER
1
0
NO_WATER
0
1
1
0
BALANCE
600
131
BALANCE
168
200
322
259
HEALTH
8
7
HEALTH
3
9
9
10
BID
100
100
BID
120
100
122
122
NO_WATER
0
1
NO_WATER
1
2
0
0
BALANCE
620
251
BALANCE
243
300
320
257
HEALTH
10
6
HEALTH
2
7
10
10
BID
200
250
BID
243
274
120
122
NO_WATER
1
0
NO_WATER
0
0
1
1
BALANCE
740
121
BALANCE
75
126
440
377
HEALTH
9
8
HEALTH
4
9
9
9
BID
121
121
BID
75
76
76
78
NO_WATER
0
1
NO_WATER
0
1
2
0
BALANCE
739
241
BALANCE
75
226
560
419
HEALTH
10
7
HEALTH
6
8
7
10
BID
200
200
BID
75
130
227
229
NO_WATER
0
2
NO_WATER
1
2
0
0
BALANCE
659
361
BALANCE
150
326
453
310
HEALTH
10
5
HEALTH
5
6
9
10
BID
200
310
BID
150
151
151
1
NO_WATER
1
0
NO_WATER
2
0
0
1
BALANCE
779
171
BALANCE
225
275
422
430
HEALTH
9
7
HEALTH
3
8
10
9
BID
171
170
BID
225
275
276
423
NO_WATER
0
1
NO_WATER
0
1
1
0
BALANCE
608
171
BALANCE
0
375
542
7
HEALTH
10
6
HEALTH
5
7
9
10
IU
3
4
3
3
3
IU
4
4
4
4
4
LR
2
4
3
4
3
LR
3
4
4
4
4
SE
3
4
3
4
2
SE
2
4
4
3
4
AD
3
3
3
5
3
AD
2
5
5
4
4
LP
2
3
3
4
3
LP
1
4
5
5
4
Final
Self-evaluation
Self-evaluation
DAY18
30
DAY19
29
DAY20
21
DAY15
25
DAY16
20
DAY17
21
DAY12
28
DAY13
27
DAY14
26
DAY9
23
DAY10
20
DAY11
21
DAY6
21
DAY7
24
DAY8
25
DAY3
25
DAY4
26
DAY5
27
GAME2
GAME CONFIG:
RANGE(Total Daily water) = (20,30)
DAY1
22
DAY2
24
GAME1
GAME CONFIG:
RANGE(Total Daily water) = (10,20)
DAY1
DAY2
DAY3
13
12
16
DAY4
DAY5
DAY6
DAY7
DAY8
17
18
14
DAY14
DAY9
DAY10
DAY11
DAY12
DAY13
12
13
14
20
13
17
17
13
Final
15
16
19
15
18
DAY19
DAY20
DAY15
DAY16
DAY17
DAY18
12
Figure 10: Water Allocation Challenge gameplay records of human judges.

--- Page 17 ---

A.5
Instruction for Human Subjective Evaluation
Gameplay Performance Evaluation Scale
Instructions:
- Assess the player’s performance in each category on a scale of 1 to 5.
- Consider the specific context of the game and the role the player assumes.
- Use this scale as a guide to identify areas of strength and improvement.
Information Utilization
- 1: The player does not consider real-time information, leading to noticeably delayed decision making.
- 2: The player noticeably misses out on processing some information.
- 3: The player considers key information adequately but has room for improvement.
- 4: The player utilizes information comprehensively to make rational decisions.
- 5: The player consistently and timely uses all available information comprehensively.
Logical Reasoning
- 1: The player’s decisions are mostly illogical, akin to random choices.
- 2: The player’s decisions have obvious shortcomings.
- 3: The player generally makes decisions based on information and inference.
- 4: The player’s decisions are reasonable and highly logical.
- 5: The player has exceptional reasoning and thinking skills, always making optimal decisions.
Strategic Effectiveness
- 1: The player’s strategy is simple, ineffective, and lacks depth.
- 2: The player’s strategy is somewhat effective but rather one-dimensional.
- 3: The player’s strategy is effective in specific situations, with room for improvement.
- 4: The player’s strategy is effective, considering key factors and generally successful.
- 5: The player’s strategy is highly effective, considering various factors, giving them an advantage in the game.
Adaptability and Strategic Evolution
- 1: The player lacks strategic variation and adaptability, with slow responses to situational and environmental changes.
- 2: The player has limited strategic variation and weak adaptability to new situations.
- 3: The player is somewhat adaptable, capable of adjusting strategies to some extent.
- 4: The player is flexible in strategy changes, adjusting to situational and environmental shifts.
- 5: The player is extremely flexible in strategy, proactively adapting to various game scenarios.
Long-term Planning
- 1: The player lacks long-term planning, relying more on short-term reactions.
- 2: The player sometimes considers long-term planning but mainly relies on short-term decisions.
- 3: The player’s strategy considers long-term planning but is shortsighted in some situations.
- 4: The player’s strategy and actions consider long-term plans, with clear and consistent adherence.
- 5: The player has a strong ability for long-term planning, comprehensively strategizing future actions.
Identity Alignment
- 1: The player’s decisions and thought processes do not align with their character’s identity, lacking character personality.
- 2: The player’s decisions and thought processes somewhat align with their character’s identity but are overall mediocre.
- 3: The player’s decisions and thought processes generally match their character’s identity but lack deep personalization.
- 4: The player’s decisions and thought processes well align with their character’s identity, reflecting its personalization.
- 5: The player’s decisions and thought processes are highly consistent with their character’s identity, perfectly showcas-
ing character personality.

```
