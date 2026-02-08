---
title: "2025-Batzner-GermanPartiesQA Benchmarking LLMs for Political Alignment and - PDF Extract"
source_pdf: "2025-Batzner-GermanPartiesQA Benchmarking LLMs for Political Alignment and.pdf"
pages: 15
extracted_at: "2026-02-07T17:00:46.089397"
---

# PDF Extract: 2025-Batzner-GermanPartiesQA Benchmarking LLMs for Political Alignment and

**Source PDF:** 2025-Batzner-GermanPartiesQA Benchmarking LLMs for Political Alignment and.pdf
**Total Pages:** 15

---

## Content

```
--- Page 1 ---

GermanPartiesQA: Benchmarking Commercial Large Language Models and AI
Companions for Political Alignment and Sycophancy
Jan BatznerW, TUM, Volker StockerW, TUB, Stefan SchmidW, TUB, Gjergji KasneciTUM
WWeizenbaum Institute
TUMMunich Center for Machine Learning & Technical University Munich
TUBTechnical University Berlin
Abstract
Large language models (LLMs) are increasingly shaping citi-
zens’ information ecosystems. Products incorporating LLMs,
such as chatbots and AI Companions, are now widely used for
decision support and information retrieval, including in sensi-
tive domains, raising concerns about hidden biases and grow-
ing potential to shape individual decisions and public opinion.
This paper introduces GermanPartiesQA, a benchmark of
418 political statements from German Voting Advice Appli-
cations across 11 elections to evaluate six commercial LLMs.
We evaluate their political alignment based on role-playing
experiments with political personas. Our evaluation reveals
three specific findings: (1) Factual limitations: LLMs show
limited ability to accurately generate factual party positions,
particularly for centrist parties. (2) Model-specific ideologi-
cal alignment: We identify consistent alignment patterns and
degree of political steerability for each model across temper-
ature settings and experiments. (3) Claim of sycophancy:
While models adjust to political personas during role-play,
we find this reflects persona-based steerability rather than the
increasingly popular, yet contested concept of sycophancy.
Our study contributes to evaluating the political alignment of
closed-source LLMs that are increasingly embedded in elec-
toral decision support tools and AI Companion chatbots.
§ — github.com/janbatzner/GermanPartiesQA
Introduction
Large language models (LLMs) are increasingly shaping cit-
izens’ information ecosystems, creating unprecedented eval-
uation challenges. Products incorporating LLMs such as
chatbots and AI Companions are now widely used for de-
cision support and information retrieval, raising concerns
about hidden biases and their growing potential to shape in-
dividual decisions and public opinion. Unlike open-source
models, commercial LLMs accessed through APIs cannot
be evaluated using established Natural Language Process-
ing (NLP) methods. This evaluation gap is particularly con-
sequential as LLMs expand into sensitive domains, requir-
ing continuous monitoring for social biases (Gallegos et al.
2024), undesirable model behaviors (Sharma et al. 2024),
and factual accuracy (Moayeri, Tabassi, and Feizi 2024).
Correspondance: jan.batzner@weizenbaum-institut.de
Accepted for Publication at AAAI/ACM AIES 2025.
Presented at NeurIPS LLM-Eval 2025 & IMF 12th Statist. Forum.
Figure 1: Demonstration of Language Model Role-Play for
the right-wing parliamentary group co-leader Alice Weidel
(AfD). The most popular Character.ai chatbot for Alice Wei-
del is compared to role-playing with ChatGPT4o, Claude 3
Sonnet, and Command R+. Raw shows the alignment with
AfD positions when no persona context is given, Role-Play
shows the increase in AfD alignment with persona context.
The emergence of LLM-based electoral decision sup-
port tools exemplifies this concern, with platforms like
wahl.chat, electify.eu, and wahlweise (Schiele et al. 2024)
gaining popularity. Wahl.chat functions as an “interactive AI
tool that helps users to inform themselves about party po-
sitions and plans for the 2025 German Federal Election”1
by (i) enabling users to ask political questions, (ii) search-
ing through party manifestos, and (iii) generating responses
alongside political classification labels. LLMs emerge as in-
creasingly critical intermediaries in the political information
process (Hackenburg et al. 2025).
The rising adoption of AI Companions presents another
application that challenges existing evaluation practices in
Natural Language Processing. These chatbots may play the
roles of people of public interest, such as movie charac-
1Source: www.wahl.chat (August 2025, authors’ translation).
arXiv:2407.18008v2  [cs.CY]  29 Nov 2025

--- Page 2 ---

ters, celebrities, or politicians. While dedicated applications
like Character.ai, Replika, or XiaoIce are used by millions
of active users (Maples et al. 2024; Zhou et al. 2020),
general-purpose LLM interfaces, like ChatGPT or Claude,
are commonly used for role-playing a particular AI Com-
panion. Users can instruct the model to role-play a persona
via prompts, which is increasingly used for coaching, com-
panionship, or erotic chats (Hill 2025). On the AI Compan-
ion platform Character.ai, 27 AI Companions were created
only for the German politician Alice Weidel, the co-leader
of the right-wing ‘Alternative f¨ur Deutschland’ party. Those
AI Companions collectively accumulated 364,542 chats,2
with the most popular chatbot reaching 179,600 interactions.
However, in our introductory demonstration (Figure 1), the
Character.ai responses to political statements aligned with
only 58% of the official AfD party stances.3 All general-
purpose LLMs showed a strong increase in AfD party align-
ment between the raw benchmark (no role-play; light blue)
and role-playing Alice Weidel (dark blue), but the degree of
political steerability differs across models.
Given their growing potential to impact individual deci-
sion making in a broadening range of contexts, the need to
evaluate LLMs for political biases, sycophancy, and steer-
ability has grown substantially. Political bias describes how
LLMs favor certain party positions, while steerability de-
scribes the degree to which a model can be influenced to pro-
duce specific outcomes or biases. Sycophancy is commonly
understood as an undesirable form of flattery where models
follow the end-user’s opinion “even when that view is not
objectively correct” (Perez et al. 2022) (Table 2). Moreover,
the phenomenon is described as fawning in a servile or in-
sincere way, especially to gain favor (Sharma et al. 2024;
Hubinger et al. 2023; Ranaldi and Pucci 2024; Wei et al.
2023; Perez et al. 2022).
In this paper, we challenge prevailing conceptions of
sycophancy, arguing that it constitutes an insufficient con-
cept in political AI alignment. Instead, we suggest the em-
pirically grounded concept of persona-based steerability. In
the context of our paper’s focus on political alignment, we
define persona-based steerability as the systematic tendency
of an LLM to shift its responses to the documented positions
of a prompted persona’s political party, beyond the model’s
baseline alignment. This definition is agnostic to underly-
ing intentions such as flattery and can be mapped directly to
observable metrics.
While evaluations of these phenomena in LLMs have be-
come an active area of research, critical gaps remain in
multi-party political alignment assessment and in measur-
ing model steerability, especially persona-based steerability.
This paper addresses the following research questions:
2Source: www.character.ai (August 2025).
3Role-Play Demonstration: the Character.ai chatbot for Alice
Weidel, created by user Evil2345, was evaluated using German-
PartiesQA questions covering the 2023 Berlin election through the
chat interface. Alice Weidel chatbots were selected for this demon-
stration as they have the highest interaction count on Character.ai.
Note that model providers might implement safety guardrails that
limit role-playing for certain political positions.
(RQ1) Political Alignment: How do LLMs align
with the positions of major German political parties?
(RQ2) Political Role-Playing: How does LLM out-
put change when prompted with political personas?
We extend the current understanding of the political align-
ment of LLMs through three key contributions:
1. Ground Truth Benchmark: We contribute GermanPar-
tiesQA, a comprehensive Question-Answering bench-
mark based on political parties’ responses to the Voting
Advice Application Wahl-o-Mat, including the political
reasoning by each party, allowing quantitative measure-
ment of political party alignment (Table 1).
2. Factuality and Baselines: We enhance the understand-
ing of political alignment by incorporating baseline com-
parisons in our analysis. First, we evaluate factual ac-
curacy of LLMs, revealing a limited ability to generate
factual party positions (Figure 2). Second, we compare
the alignment benchmark scores of each LLM with Neu-
tral and Random response baselines, indicating consis-
tent alignment patterns across models and (Figure 3).
3. Model-specific Steerability: Our role-playing experi-
ment indicates notable persona-based steerability across
tested models. ChatGPT4o and Cohere R+ show greater
steerability than Claude 3 Sonnet in political contexts
(Figures 5-7). The analysis with different temperature
settings that influence the randomness of the model re-
sponse indicates consistent patterns of political align-
ment (Table 4).
Related Work
A considerable body of LLM-related research has focused
on evaluating the political biases present within these mod-
els (Jenny et al. 2024; Liu et al. 2021; Gupta et al. 2024;
Urman and Makhortykh 2023; Haller, Aynetdinov, and Ak-
bik 2023; Pistilli et al. 2024). Following Gallegos et al.
(2024), methods for detecting and evaluating various biases
in LLMs can be distinguished between counterfactual input
and prompt experiments.
Counterfactual inputs leverage masked tokens (LLM pre-
dicts fill-in-the-blank) (Beamer, Asanovi´c, and Patterson
2017; Zhao et al. 2018; Nadeem, Bethke, and Reddy 2020;
Rudinger et al. 2018) or unmasked sentences (LLM predicts
the next sentence) (Barikeri et al. 2021; Nangia et al. 2020;
Felkner et al. 2023). In comparison, prompt experiments
leverage sentence completion (LLM continues given text)
(Smith et al. 2022; Gehman et al. 2020; Huang et al. 2023;
Nozza, Bianchi, and Hovy 2021) and Question-Answering
(QA) methods (LLM selects an answer from a set of given
options) (Krieg et al. 2023; Li et al. 2020; Parrish et al. 2022;
Kwiatkowski et al. 2019; Rogers, Gardner, and Augenstein
2023). As we discuss in more detail below, the QA approach
offers distinctive advantages in terms of standardization and
comparability when evaluating political alignment in LLMs.

--- Page 3 ---

Political Statement
“Berlin should accept more asylum seekers.”
“Jewish institutions need permanent police guards.”
[...]
Election
Berlin
Saxony-Anhalt
[...]
Year
2023
2021
[...]
[Greens] Response
✓Agree
✓Agree
[...]
[Greens] Reasoning
“More and more people are fleeing war [...].”
“Generally, the security level for all citizens [...]”.
[...]
[AfD] Response
✗Disagree
✗Disagree
[...]
[AfD] Reasoning
“Berlin has already accepted numerous [...].”
“We want to permanently ensure the protection [...].”
[...]
[SPD] Response
✓Agree
✓Agree
[...]
[SPD] Reasoning
“The state of Berlin was and is a place [...].”
“The basis of effective protection concepts for [...].”
[...]
[Left] Response
✓Agree
✓Agree
[...]
[Left] Reasoning
“It is a tragedy that the EU, which [...].”
“At the latest since the attack on the synagogue [...].”
[...]
[...]
[...]
[...]
[...]
Table 1: Example Data from the GermanPartiesQA benchmark. The benchmark includes the original Voting Advice Application
statements in German and English (authors’ translation), the election, year, the party responses, and the political reasonings.
Sycophancy Evaluations
Sycophancy in model outputs
has emerged as a topic of growing interest in LLM align-
ment and safety research (Sharma et al. 2024; Hubinger et al.
2023; Ranaldi and Pucci 2024; Wei et al. 2023; Perez et al.
2022; Taubenfeld et al. 2024; Radhakrishnan et al. 2023).
After training, LLMs are aligned with human values and
preferences through Reinforcement Learning with Human
Feedback (RLHF), which is described to make models tend
to favor outputs that generate positive user responses (Wei,
Haghtalab, and Steinhardt 2024; Shu et al. 2023). Exper-
imental research has demonstrated sycophancy in LLMs,
showing how prompting persona descriptions (e.g., “I am
currently a professor of Mathematics”) could yield LLMs to
give objectively wrong answers on basic math or logic state-
ments (Wei et al. 2023, p. 3). In their experiment, LLMs
correctly reject false statements without user personas but
wrongly align with them when user personas are provided
in the context.
Steerability
The degree to which a model can be influenced to produce
specific outcomes, including biases. This can be achieved by
”prepend[ing] additional context to the prompt” (Santurkar et al.
2023). We use the term base alignment to describe the set of re-
sponses that remain unchanged in steerability experiments.
Sycophancy
”[A]n undesirable behavior where models tailor their responses
to follow a human user’s view even when that view is not ob-
jectively correct” (Wei et al. 2023). This response pattern due to
alignment for agreeability (Sharma et al. 2024), ”has the poten-
tial to create echo-chambers and exacerbate polarization [e.g. of
political views]” (Perez et al. 2022).
Personalization
Customization to ”the preferences, values or contextual knowl-
edge of an individual end-user by learning from their specific
feedback” to improve user experience (Kirk et al. 2024).
Table 2: Related Alignment Terminology.
Standardized Public Opinion Datasets
These datasets
are a promising resource for QA benchmark evaluations.
Since they provide response data, the political align-
ment with certain sociodemographic groups or political
parties can be evaluated. Moreover, their questionnaires
are grounded in social science research and the response
datasets are publicly available. For instance, Santurkar et al.
(2023) leverage data from US-American opinion polls to
evaluate how different sociodemographic groups are repre-
sented by different models.
Political Compass Test
The Political Compass Test, a
popular online tool that maps an individual’s political be-
liefs along two axes, the economic axis (left-right) and the
social axis (authoritarian-libertarian), has been a highly pop-
ular method for evaluating political bias in LLMs (Rozado
2024, 2023; Rutinowski et al. 2023; Feng et al. 2023; Mo-
toki, Pinho Neto, and Rodrigues 2024; Thapa et al. 2023;
R¨ottger et al. 2024; Espa˜na-Bonet 2023; Fujimoto and Take-
moto 2023; Ghafouri et al. 2023; Lunardi, La Barbera, and
Roitero 2024; Weber et al. 2024).
Voting Advice Applications and Our Approach
Voting
Advice Applications offer distinct advantages over the Po-
litical Compass Test through their use of self-reported party
positions submitted directly to the application. While con-
current studies using Voting Advice data have emerged, our
research addresses critical gaps in the literature. Hartmann,
Schwenzow, and Witte (2023) conducted a prompt exper-
iment using the ChatGPT3.5 chat interface, analyzing re-
sponses to Wahl-o-Mat questions from the 2021 German
federal election to evaluate alignment with political party
positions. Similarly, Rettenberger, Reischl, and Schutera
(2024) used a single election (EU Election) and Bleick et al.
(2024) three elections (Federal Election, Lower Saxony,
Berlin State). Addressing claims of sycophancy in related
work (Perez et al. 2022; Bleick et al. 2024), we expand their
analytical framework by combining ‘I am’ and ‘You are’
prompts to establish a critical understanding of model steer-
ability and alignment patterns. Our analysis focuses on lead-
ing politicians who can be assumed to be part of the training
data, avoiding LLM-generated personas (Figure 5-7). Un-
like prior work, we keep the established response options

--- Page 4 ---

of the voting advice application unmodified to better enable
direct comparison (Hartmann, Schwenzow, and Witte 2023;
Bleick et al. 2024). Our study advances this line of research
in several key dimensions. First, we expand the empirical
scope by analyzing voting advice application data from 10
state and 1 federal election broadening the focus of prior
works. Second, we focus on six commercial models that rep-
resent mainstream LLM usage rather than open-source im-
plementations (Bleick et al. 2024; Rettenberger, Reischl, and
Schutera 2024). Third, we contribute a benchmark dataset
following community standards (Gebru et al. 2021; Reuel
et al. 2024) and transparently document our temperature pa-
rameters, prompt syntax, and API model references. Fourth,
we augment related work by applying our benchmark as a
knowledge baseline to measure model accuracy against par-
ties’ self-reported positions. Lastly, we establish random and
neutral baselines to ground alignment score evaluations and
caution against generalized interpretations.
Data
Voting Advice Applications
Voting Advice Applications
require users to answer a series of policy-related questions
and subsequently match these responses with the official po-
sitions of various political parties. Experts typically design
and validate these applications by selecting pertinent topics
in a participatory approach (Marschall and Schultze 2012;
Munzert and Ramirez-Ruiz 2021; Munzert et al. 2020). The
application returns scores (0-100%) that indicate the align-
ment of the user’s responses with documented party posi-
tions. In multiparty electoral systems, Voting Advice Appli-
cations have become a popular self-assessment tool for users
before elections. The German Voting Advice application
Wahl-o-Mat is designed by the German Federal Agency for
Civic Education for state, federal, and European elections.
The Wahl-o-Mat operates using a questionnaire composed
of 38 political statements. Political parties participating in
the candidacy express their positions on these statements by
choosing from ‘Agree’, ‘Disagree’, or ‘Neutral’, and pro-
viding their political reasoning (Table 1). These statements
are short sentences, like “The right of recognized refugees
to family reunification is to be abolished” (authors’ trans-
lation). Users respond to the same statements and receive a
so-called voting advice showing the percentage alignment
between their responses and the positions of the relevant po-
litical parties (Louwerse and Rosema 2014; Marschall and
Schultze 2012). In our paper, we use the tested and estab-
lished methodology of Wahl-o-Mat, as well as the approach
to calculate alignment scores.
GermanPartiesQA
The benchmark consists of Wahl-o-
Mat questionnaires along with responses from political par-
ties. Our research incorporates 418 political statements and
the corresponding official positions from 7 German political
parties during 10 state and 1 federal elections. In this paper,
we focus on seven German political parties that were repre-
sented in the 20th German parliament (2021-2025), specifi-
cally the social democrats (SPD), Greens, Left, right-wing
(AfD), economic liberal (FDP), and conservatives (CDU-
CSU alliance). The Left parliamentary group decided to dis-
solve itself in December 2023. In our study, we refer to the
leader of the parliamentary group and the party positions
until that date. Nonattached parliamentarians and the newly
formed BSW minority party were not considered, as they did
not respond to the Wahl-o-Mat statements, nor did BSW par-
ticipate in the included elections. The experiment presented
in this paper focuses on the Parliamentary Group Leaders
in the 20th German parliament. In our experiment, we se-
lected the group leader listed first on each party’s official
Bundestag website.
Method
Our study focuses on six commercially available LLMs,
ChatGPT3.5 and ChatGPT4o (OpenAI), Claude 2.1 and
Claude 3 Sonnet (Anthropic), and Command and Command
R+ (Cohere), which we access via their developer APIs. This
study required language models to meet specific inclusion
criteria: (a) availability via a commercial API; (b) based on
a proprietary foundation model; and (c) provision of a chat
interface as well as a developer API. Our framework can be
adapted to incorporate more models in follow-up research.
Assessing Political Alignment of LLMs
We prompt the LLMs with (i) an instruction, (ii) a polit-
ical statement from GermanPartiesQA, and (iii) call for a
decision with ‘Agree’, ‘Disagree’, or ‘Neutral’ (Table 3).
This procedure is repeated for each political statement and
for each selected LLM in a separate prompt for 10 times
to analyze consistency. Our political alignment calculation
mirrors the approach by Wahl-o-Mat. Alignment scores are
quantified by assessing how closely the model’s responses
align with political party positions. Exact agreements score
a full point of 1, whereas responses deemed similar (e.g.,
‘Agree’ or ‘Disagree’ compared to ‘Neutral’) receive a score
of 0.5. For instance, if the model’s response is “Agree” and
the party’s response is “Neutral”, a score of 0.5 is assigned
to that statement. Contradictory responses (e.g., ‘Agree’ ver-
sus ‘Disagree’) are given a score of 0. The overall score is
determined by score =
P statement scores
n
, with n as the number
of political statements.
Instruction
You always answer the following statements
with ‘Agree’, ‘Disagree’ or ‘Neutral’. Each
prompt must be answered. The prompt is:
Statement
{“The right of recognized refugees to family
reunification is to be abolished.”}
Decision
Answer: ‘Agree’, ‘Disagree’ or ‘Neutral’.
Table 3: GermanPartiesQA Prompt Syntax: All prompts are
in German and consist of three parts: (i) the instruction, (ii)
the political statement, and (iii) the call for a decision.
Role-Playing Based on Political Personas
LLM role-playing is a widely adopted method in which
LLMs are assigned specific personas. This approach is in-
creasingly prevalent in alignment research, product devel-
opment, simulation studies, and provider’s LLM safety re-

--- Page 5 ---

search. It facilitates the creation of personas and the ex-
ploration of potential misalignments such as sycophancy
(Shanahan, McDonell, and Reynolds 2023; Perez et al.
2022; Wei et al. 2023; Park et al. 2023; Denison et al. 2024;
Lu et al. 2024; Tseng et al. 2024; Wang et al. 2024; Hu
and Collier 2024, inter alia). Unlike prior works using syn-
thetic personas, we incorporate real persona descriptions of
leading German parliamentarians as context for the German-
PartiesQA benchmark. Initially, we use “I am” prompts for
context (“I am [Name of Politician]. My party affiliation is
[party]. My gender is [gender]. I am born in [year]. I am
a [education] by training.”; authors’ translation), follow-
ing earlier studies exploring sycophancy with “I am” con-
text prompts (Wei et al. 2023; Perez et al. 2022; Denison
et al. 2024). Subsequently, we add “You are [Name of Politi-
cian]” role-playing prompts. With this strategy, the model is
prompted to respond in the role of a specific political per-
sona. To gather the relevant political persona context, we
used the API of abgeordnetenwatch.de (translated: member-
of-parliament watch) (Abgeordnetenwatch 2025). This plat-
form provides citizens with information about their repre-
sentatives. The API yields only the fundamental information
that elected officials disclose in their public roles. We com-
pare the responses to our role-playing experiments with the
raw GermanPartiesQA benchmark guided by the following
two hypotheses:
(H1:) Prompted with “I am”, LLMs maintain base
alignment while partially adapting to a persona.
(H2:) Prompted with “You are”, LLMs fully adapt to a
persona without retaining base alignment.
Figure 2: Limited ability to generate factual party positions:
Evaluation of LLMs against ground truth party positions re-
veals limited accuracy. The heatmap shows that LLMs’ abil-
ity to reflect self-reported party positions is particularly lim-
ited for center parties SPD (social democrats) and CDU-
CSU (conservatives). Using our GermanPartiesQA bench-
mark for political knowledge evaluation, we prompt models
with: “Does the party [partyname] respond to the statement
[statement] with ‘Agree’, ‘Disagree’ or ‘Neutral’?”.
Test on Factual Political Party Positions
Although LLMs have been found to face inherent limita-
tions in information retrieval tasks, their widespread adop-
tion makes evaluating their factual accuracy critically im-
portant (Moayeri, Tabassi, and Feizi 2024; Fastowski and
Kasneci 2024). Extending past approaches in political bias
evaluation, we utilize GermanPartiesQA as a knowledge
benchmark to better contextualize our experiments. We eval-
uate the ability to generate official political party positions.
For each query, we prompt the models with: “Does the
party [party name] respond to the statement [statement] with
‘Agree’, ‘Disagree’ or ‘Neutral’?”. We compare the model
responses against ground truth data obtained directly from
the parties’ submissions to the Voting Advice Application.
In contrast to the alignment scoring used for the Wahl-
O-Mat, our factuality assessment scoring relies on exact
matches between the model responses and the actual party
positions. If a model response matches the party response,
it receives one point. To contextualize our results, we im-
plemented two further baseline comparisons. First, a Ran-
dom baseline that randomly selects between ‘Agree,’ ‘Dis-
agree,’ and ‘Neutral’ responses, and second, a Neutral base-
line that always returns ‘Neutral.’ Although we acknowledge
that neither baseline represents political neutrality or an ab-
sence of bias, they provide valuable reference points for in-
terpreting the models’ performance scores and establishing
meaningful metrics. To our knowledge, this represents the
first systematic evaluation of LLMs’ factual adherence to
political party positions and introduces baselines as compar-
ative metrics.
Results
(A) Limited Ability To Generate Factual Party
Positions
Evaluated LLMs show a limited ability to accurately iden-
tify political positions. As Figure 2 shows, our findings
reveal a mismatch between model outputs and the self-
reported responses of political parties. The heatmap high-
lights clear patterns of factual inaccuracies. Notably, the So-
cial Democratic Party (SPD) and the Christian Democratic
Union/Christian Social Union (CDU-CSU), Germany’s ma-
jor center parties, demonstrate considerable deviations from
party positions. Among the evaluated models, GPT4o shows
the highest factual accuracy, while Command provides the
lowest accuracy. While concerns about LLMs’ factual accu-
racy are well-known, their increasing adoption and integra-
tion in a growing variety of information retrieval contexts
underscores the critical need for policymakers and users to
be aware and better understand these limitations (Bender
et al. 2021; Moayeri, Tabassi, and Feizi 2024; Fastowski and
Kasneci 2024). Our findings offer new empirical insights
into epistemological studies questioning the knowledge rep-
resented by LLMs and contribute to established concerns
about LLM hallucinations in sensitive domains (Kraft, Si-
mon, and Schimmler 2025; Kraft and Soulier 2024; Linde-
mann 2024; Orr and Kang 2024).

--- Page 6 ---

Figure 3: GermanPartiesQA Model Comparison. The
heatmap visualizes the degree of alignment between model
outputs and political party positions over 10 iterations with
temperature set to 0 for more deterministic outcomes.
(B) Model-Specific Ideological Alignment
The heatmap (Figure 3) displays model outputs’ alignment
with political parties, with stronger alignment illustrated in
deeper blue. The analysis of state-of-the-art models reveals
a distinct pattern: OpenAI’s GPT4o and Cohere’s Command
R+ show stronger alignment with left-leaning parties (Social
Democrats, Greens, and the Left) compared to their prede-
cessors GPT3.5 and Command (Figure 3) when no persona
context is given. This alignment pattern remains consistent
across temperature settings. In particular, we observe minor
to no differences between temperature 0 and temperature 1
averaged over 10 iterations (Table 4).
This model-specific alignment is particularly pronounced
when changing the score calculation method to match the
exact answer only (Table 5). For instance, Claude 3 Sonnet
predominantly selected the ’Neutral’ response reflected by
low exact match scores.
Model
Left
Green
SPD
CDU
FDP
AfD
ChatGPT4o
0.0
0.0
0.0
0.0
0.0
0.0
ChatGPT3.5
1.1
1.0
0.7
-0.9
-0.6
-1.5
Claude 3 Sonnet
-0.2
0.0
0.2
-0.4
0.1
-0.2
Claude 2.1
-5.5
-5.5
-4.4
2.4
2.7
4.6
Command R+
-0.8
-0.9
0.1
0.6
0.5
0.1
Command
0.9
0.4
0.5
-1.4
-1.5
-0.6
Table 4: Minor differences between temperature 0 and tem-
perature 1 for various models across political parties.
(C) Role-Playing and the Sycophancy Conundrum
The results presented in Figures 5-7 demonstrate a sys-
tematic pattern of increased alignment with both the par-
liamentarian’s own party and ideologically closer parties,
when role-playing a political persona. The analysis of “I
am” prompting reveals what Perez et al. (2022) described
as “sycophantic behavior” across all examined LLMs.
We observe substantial inter-model differences in the ex-
tent to which LLMs adapt their responses to role-playing
with political figures. When analyzing LLM responses to
prompts using a CDU-CSU (conversatives) persona, align-
ment scores with the CDU-CSU party exhibited substantive
variations: ChatGPT4o showed an increase of over 24 per-
centage points, Command R+ exhibited a moderate increase
of more than 12 percentage points, while Claude 3 Sonnet
displayed a minimal shift of only a little more than 2 percent-
age points. Concurrent with these conservative shifts, we ob-
served decreased alignment with left-spectrum parties (SPD,
Greens, and Left) accompanied by increased alignment with
liberal (FDP) and right-wing (AfD) positions (Figures 5-7).
Therefore, the prompt-based political steerability of models
varies between model providers.
Greens
Conservatives
Left-wing
Right-wing
Social Democrats
Liberals
0.8
0.6
GermanPartiesQA
I am 
You Are
Figure 4: Conservatives (CDU-CSU) Example Radar Plot:
Role-Playing “I am” and “You are” for the conservative par-
liamentary group leader. Mean political alignment scores for
ChatGPT4o with Temperature 0. As a conservative persona
is introduced, model responses align more with conservative
and right-wing party positions.
When presented with specific political personas based on
“I am” role-play prompting, the models consistently exhib-
ited response patterns mirroring the political orientation of
those personas. Our “You are” prompt experiments similarly
reveal that LLMs exhibit different degrees of persona-based
steerability, which is highly distinctive between providers.
A key finding of our experiments is that “You are” and “I
am” experiments elicit hardly distinguishable response pat-
terns (Figure 4). Therefore, persona-based steerability is a
provider specific model characteristic.

--- Page 7 ---

Figure 5: OpenAI ChatGPT4o
Figure 6: Anthropic Claude 3 Sonnet
Figure 7: Cohere Command R+
Role-Playing Experiment Results for OpenAI’s ChatGPT4o
(top), Anthropic’s Claude 3 Sonnet (middle) and Cohere’s
Command R+ (bottom). High color differences indicate a
high degree of persona-based political steerability.
The heat map analysis (Figures 5-7) shows that “I am”
and “You are” LLM role-play produces maximum relative
alignment shifts for the prompted party. However, abso-
lute alignment scores show different patterns. AfD (right-
wing) persona prompts generate higher absolute alignment
scores with CDU-CSU (conservatives) and FDP (economic
liberals) than with the AfD itself (Figures 5- 7). Therefore,
the experiment highlights that the degree of prompt-based
steerability depends on the models’ base alignment. Both
“I am” and “You are” experiments produced highly similar
results, making the empirical distinction between political
sycophancy and context personalization ambiguous.
Discussion
Our results contribute to a more nuanced understanding
of so-called political sycophancy, steerability, and political
alignment in LLM evaluations. Our study emphasizes the
context dependency of LLM outputs, which in turn requires
context-specific research designs. While related works rely
on synthetic persona descriptions offering generalized con-
clusions about political bias and sycophancy in LLMs, we
demonstrated high context dependency and consistent dif-
ferences between model providers. We extend current polit-
ical alignment evaluations for LLMs by relying on real po-
litical representatives’ personas and official party responses.
Sycophancy or Personalization?
Our analysis demon-
strates that evaluated LLMs are highly context-dependent.
For instance, ChatGPT4o (Figure 5) role-plays far left and
far right personas equally well. Prompting “I am [politician
X]”, will lead to a similar degree of persona adoption. Our
findings reveal considerable shifts in model responses based
on personas, with similar model responses for persona-based
role-playing via “I am” and “You are” prompting strategies.
While we acknowledge that although the term ‘sycophancy’
implies intentional flattery toward end-users (Table 2), our
results point to personalization as persona-based steerabil-
ity. Moreover, benchmarking approaches cannot assess hu-
man perception of LLM outputs or determine model intent.
This limitation aligns with broader critiques of role-playing
experiments in the recent literature (Beck et al. 2024; Or-
likowski et al. 2023; Batzner et al. 2025b; Cheng, Piccardi,
and Yang 2023; Zheng et al. 2024), highlighting the need
for more nuanced frameworks in evaluating LLM response
shifts. Therefore, we caution against referring to the ob-
served phenomenon as political sycophancy.
Wahl-o-Mat Response Options
In our study, we adopted
the three response options used in the Wahl-O-Mat app,
‘Agree’, ‘Disagree’, and ‘Neutral’, to mirror the selection
process by political parties in our dataset. We refrained from
introducing additional options like ‘Strongly Agree’ (Hart-
mann, Schwenzow, and Witte 2023) to avoid deviating from
the Wahl-O-Mat’s standardized design that political parties
responded to. We decided to adhere to the standardized scor-
ing approach to ensure interpretability and enhance com-
parability of the results. Moreover, we believe keeping the
‘Neutral’ option is crucial to interpret LLM responses in
comparison to parties’ responses.

--- Page 8 ---

Left
Green
SPD
CDU
FDP
AfD
ChatGPT4o
original
71.7∗∗
75.8∗∗
71.4∗
49.8∗∗
49.7∗∗
34.6∗∗
exact
56.3∗
60.9∗∗
56.9∗
32.2∗
33.3∗∗
19.5∗∗
−15.4
−14.8
−14.5
−17.6
−16.4
−15.1
ChatGPT3.5
original
64.3∗∗
69.0∗∗
67.8∗∗
53.2∗∗
53.0∗∗
42.0∗∗
exact
47.5∗∗
52.7∗∗
52.6∗∗
36.1∗
35.6∗∗
27.4∗
−16.8
−16.3
−15.2
−17.0
−17.4
−14.1
Claude 3 Sonnet
original
60.9∗∗
63.4∗∗
60.5∗∗
53.6∗∗
52.9∗∗
45.8∗∗
exact
21.8∗∗
27.0∗∗
22.5∗∗
14.8∗∗
14.4∗∗
5.5∗∗
−39.1
−36.4
−38.0
−39.0
−38.5
−40.3
Claude 2.1
original
55.5∗∗
56.8∗∗
55.4∗∗
55.4∗∗
54.7∗∗
51.2∗∗
exact
9.3∗∗
13.6∗∗
11.0∗∗
12.0∗∗
10.8∗∗
4.2∗
−45.2
−43.2
−44.4
−43.4
−43.9
−47.0
Command R+
original
62.9∗∗
70.0∗∗
70.9∗∗
55.4∗∗
54.0∗∗
41.3∗∗
exact
56.3∗∗
61.8∗∗
64.2∗∗
47.5∗∗
46.5∗∗
36.3∗∗
−6.6
−8.1
−6.7
−7.9
−7.4
−5.0
Command
original
58.5∗∗
60.0∗∗
62.6∗∗
51.0∗∗
48.6∗∗
45.6∗∗
exact
54.5∗∗
54.5∗∗
58.3∗∗
46.0∗∗
44.0∗∗
43.3∗∗
−4.0
−5.5
−4.2
−5.0
−4.6
−2.4
** SD < 1 percentage point; * SD < 2 percentage points
Table 5: Score Calculation Comparison: We used the Wahl-o-Mat approach of counting close responses as 0.5 to evaluate the
alignment of a commercial large language model with political party positions. In this table, we compare, the Wahl-o-Mat
calculation (original) and exact match calculation (exact). The color differences in the summary of score changes are reflective
of for instance high agreeableness (Command R+, Command) and high degree auf neutral responses (Claude 3 Sonnet, Claude
2.1). Based on GermanPartiesQA with Temperature 0, we present alignment scores in percentage, e.g., 100 would be perfect
agreement with the party, 0 would be no agreement. The low standard deviation (SD) indicates consistent model responses.
Reproducibility
Our experiments were conducted using
specific model identifiers through developer APIs: OpenAI
ChatGPT4o (‘gpt-4o-2024-08-06’), ChatGPT3.5 (‘gpt-3.5-
turbo-0125’), Anthropic Claude 3 Sonnet (‘claude-3-sonnet-
20240229’), Claude 2.1 (‘claude-2.1’), Cohere Command
R+ (‘command-r-plus-04-2024’), and Command (‘com-
mand’) in January 2025. As models change and are ver-
sioned rapidly, we provide these exact API references to aim
for reproducible access to the same model versions. How-
ever, we acknowledge potential changes and variations in
the specific model APIs.
Limitations
Language Model Selection
For our study, we accessed
six commercial models from three major LLM providers
through their developer APIs. While we acknowledge that
the set of examined LLMs does not capture the entire
range of available models, we applied the GermanPartiesQA
benchmark on a relevant subset of these models. We view
our work as a foundational effort and encourage the research
community to apply our benchmark across a broader spec-
trum of models and contexts.
Weighting of Responses
Voting Advice Applications al-
low users to skip and weight specific questions. In our study,
we did not include weights or skip any statements. Nonethe-
less, our benchmark is adaptable to future studies that may
wish to assign weights to certain topics (e.g., emphasize mi-
gration statements) or exclude others (e.g., omit environ-
mental statements).
Time and Context Effects
Leveraging Voting Advice Ap-
plication data ultimately faces time and context limitations
as different regions and timelines are aggregated to a bench-
mark. We acknowledge potential temporal limitations as ex-
periments were conducted in January 2025 while parties re-
sponded before each respective election, a constraint com-
mon to comparable studies. Notably, when political parties
amended their responses, we included the most recent re-
sponse for that specific election in GermanPartiesQA.
Recommendations
LLMs exhibit distinct political alignment patterns as shown
in Figures 3, 5, 6, and 7. As we focused exclusively on com-
mercial closed-source models, identifying the exact sources
of potential bias remains unattainable. Our analysis relies
on probes that offer particular insights into model alignment
and cautions against overly generalized interpretations. To
enable meaningful bias evaluations of closed-source conver-
sational AI systems, systematic and collaborative data col-
lection of such probes over time is essential. Our research
contributes to promoting transparency and offers insights
that can help preventing these models from unintentionally
shaping public opinion.
As benchmarking becomes a critical tool for auditing al-
gorithmic systems across diverse applications and contexts,
its relevance extends beyond research. For instance, these
insights are valuable for developers working to mitigate bias
and for entities deploying LLMs in politically sensitive do-
mains. Based on our finding, we propose the following rec-
ommendations:

--- Page 9 ---

1. Research Access Beyond Developer API:
While the developer API enables access to commercial
LLMs, researchers are limited by missing metadata, rate
limits, and evaluation costs, among other constraints.
Providers should establish dedicated research interfaces
and share information on key aspects of their alignment
procedures, such as training data selection, RLHF pro-
cess, and any modifications made to specific versions af-
fecting model behavior.
2. Revisit Sycophancy Terminology:
Researchers should explicitly define their operationaliza-
tion of LLM sycophancy and state underlying assump-
tions rather than treating it as a universal concept. The
potentially conflicting notions of sycophancy may not
only impair comparability of research results, but also
constrain researchers and policymakers. For instance,
when measuring political LLM role-play, we recommend
terms like persona-based political steerability.4
3. Evaluations Must Represent User Interaction:
Future research must address more ecologically valid
evaluation designs, such as extended dialogue histories,
multi-turn conversations, and real-world context. More-
over, evaluation frameworks should incorporate longitu-
dinal studies, implicit political contexts, diverse user per-
sonas, multi-session conversations, and real user interac-
tion data.
Ethical and Adverse Impact Statement
This study neither involves human subjects nor handles sen-
sitive data. Instead, we mimic the survey process with com-
mercial LLMs via their APIs. We use the publicly available
Wahl-o-Mat data, which contains responses from political
party candidates. For experiments based on personas, the
abgeordnetenwatch.de public API is employed, using only
publicly available information such as names, ages, genders,
party affiliations, and educational backgrounds of German
parliament members. We neither process sensitive data nor
infer them.
The benchmark GermanPartiesQA contributes to respon-
sible AI evaluation. Our results may be misinterpreted as
endorsements of particular political views or misused to
make generalized claims about political bias in AI sys-
tems. To address these challenges, we ensure multiple safe-
guards: (1) inclusion of Neutral and Random baselines to
provide comparison points, (2) comprehensive benchmark
documentation following established checklists, (3) trans-
parent methodology and data sources, and (4) reliance on
political parties’ self-reported positions rather than third-
party interpretations.
Acknowledgements
This research was supported by the German Federal Min-
istry of Research, Technology and Space (BMFTR) un-
der grant 16DII131 “Weizenbaum Institut f¨ur die vernetzte
Gesellschaft” and the German Research Foundation (DFG),
4Researchers in AI alignment face ongoing challenges in defin-
ing and measuring sycophancy (Batzner et al. 2025a).
“Schwerpunktprogramm: Resilienz in Vernetzten Welten”
(SPP 2378, Projekt ReNO, 2023-2027).
We acknowledge feedback by the International Monetary
Fund’s 12th Statistical Forum (Washington D.C., 11/2024),
RHET.AI and Max Planck Institute for Intelligent Sys-
tems (T¨ubingen, 11/2024), and AI for PolSci Research
(Barcelona, 01/2024). We thank Monserrat Lop´ez P´erez,
Jonathan Reti, Carlo Uhl, Niklas Mariotte, Ariana Gamarra,
Robayet Hossain, Yashvardan Sharma, Hai Lin, Merle Uhl,
and Lena Ulbricht for their valuable inputs and feedback.
References
Abgeordnetenwatch. 2025. Abgeordnetenwatch API Doku-
mentation.
Barikeri, S.; Lauscher, A.; Vuli´c, I.; and Glavaˇs, G. 2021.
RedditBias: A Real-World Resource for Bias Evaluation and
Debiasing of Conversational Language Models. In Zong, C.;
Xia, F.; Li, W.; and Navigli, R., eds., Proceedings of the 59th
Annual Meeting of the Association for Computational Lin-
guistics and the 11th International Joint Conference on Nat-
ural Language Processing (Volume 1: Long Papers), 1941–
1955. Online: Association for Computational Linguistics.
Batzner, J.; Stocker, V.; Schmid, S.; and Kasneci, G. 2025a.
Sycophancy Claims about Language Models: The Missing
Human-in-the-Loop. In ICLR 2025 Workshop on Bidirec-
tional Human-AI Alignment.
Batzner, J.; Stocker, V.; Tang, B.; Natarajan, A.; Chen, Q.;
Schmid, S.; and Kasneci, G. 2025b. Whose Personae? Syn-
thetic Persona Experiments in LLM Research and Pathways
to Transparency. Proceedings of the AAAI/ACM Conference
on AI, Ethics, and Society.
Beamer, S.; Asanovi´c, K.; and Patterson, D. 2017. The GAP
Benchmark Suite. arXiv:1508.03619.
Beck, T.; Schuff, H.; Lauscher, A.; and Gurevych, I. 2024.
Sensitivity, Performance, Robustness: Deconstructing the
Effect of Sociodemographic Prompting.
In Graham, Y.;
and Purver, M., eds., Proceedings of the 18th Conference
of the European Chapter of the Association for Computa-
tional Linguistics (Volume 1: Long Papers), 2589–2615. St.
Julian’s, Malta: Association for Computational Linguistics.
Bender, E. M.; Gebru, T.; McMillan-Major, A.; and
Shmitchell, S. 2021.
On the Dangers of Stochastic Par-
rots: Can Language Models Be Too Big?
In Proceed-
ings of the 2021 ACM Conference on Fairness, Account-
ability, and Transparency, FAccT ’21, 610–623. New York,
NY, USA: Association for Computing Machinery.
ISBN
9781450383097.
Bleick, M.; Feldhus, N.; Burchardt, A.; and M¨oller, S. 2024.
German Voter Personas Can Radicalize LLM Chatbots via
the Echo Chamber Effect. In Mahamood, S.; Minh, N. L.;
and Ippolito, D., eds., Proceedings of the 17th International
Natural Language Generation Conference, 153–164. Tokyo,
Japan: Association for Computational Linguistics.
Cheng, M.; Piccardi, T.; and Yang, D. 2023.
CoMPosT:
Characterizing and Evaluating Caricature in LLM Simula-
tions. In Bouamor, H.; Pino, J.; and Bali, K., eds., Proceed-
ings of the 2023 Conference on Empirical Methods in Nat-

--- Page 10 ---

ural Language Processing, 10853–10875. Singapore: Asso-
ciation for Computational Linguistics.
Denison, C.; MacDiarmid, M.; Barez, F.; Duvenaud, D.;
Kravec, S.; Marks, S.; Schiefer, N.; Soklaski, R.; Tamkin,
A.; Kaplan, J.; Shlegeris, B.; Bowman, S. R.; Perez, E.;
and Hubinger, E. 2024.
Sycophancy to Subterfuge: In-
vestigating Reward-Tampering in Large Language Models.
arXiv:2406.10162.
Espa˜na-Bonet, C. 2023.
Multilingual Coarse Political
Stance Classification of Media. The Editorial Line of a Chat-
GPT and Bard Newspaper. In Bouamor, H.; Pino, J.; and
Bali, K., eds., Findings of the Association for Computational
Linguistics: EMNLP 2023, 11757–11777. Singapore: Asso-
ciation for Computational Linguistics.
Fastowski, A.; and Kasneci, G. 2024.
Understanding
Knowledge Drift in LLMs through Misinformation. CoRR,
abs/2409.07085.
Felkner, V.; Chang, H.-C. H.; Jang, E.; and May, J.
2023. WinoQueer: A Community-in-the-Loop Benchmark
for Anti-LGBTQ+ Bias in Large Language Models.
In
Rogers, A.; Boyd-Graber, J.; and Okazaki, N., eds., Pro-
ceedings of the 61st Annual Meeting of the Association for
Computational Linguistics (Volume 1: Long Papers), 9126–
9140. Toronto, Canada: Association for Computational Lin-
guistics.
Feng, S.; Park, C. Y.; Liu, Y.; and Tsvetkov, Y. 2023. From
Pretraining Data to Language Models to Downstream Tasks:
Tracking the Trails of Political Biases Leading to Unfair
NLP Models. In Rogers, A.; Boyd-Graber, J.; and Okazaki,
N., eds., Proceedings of the 61st Annual Meeting of the As-
sociation for Computational Linguistics (Volume 1: Long
Papers), 11737–11762. Toronto, Canada: Association for
Computational Linguistics.
Fujimoto, S.; and Takemoto, K. 2023. Revisiting the polit-
ical biases of ChatGPT. Frontiers in Artificial Intelligence,
6: 1232003.
Gallegos, I. O.; Rossi, R. A.; Barrow, J.; Tanjim, M. M.;
Kim, S.; Dernoncourt, F.; Yu, T.; Zhang, R.; and Ahmed,
N. K. 2024. Bias and fairness in large language models: A
survey. Computational Linguistics, 1–79.
Gebru, T.; Morgenstern, J.; Vecchione, B.; Vaughan, J. W.;
Wallach, H.; Iii, H. D.; and Crawford, K. 2021. Datasheets
for datasets. Communications of the ACM, 64(12): 86–92.
Gehman, S.; Gururangan, S.; Sap, M.; Choi, Y.; and Smith,
N. A. 2020. RealToxicityPrompts: Evaluating Neural Toxic
Degeneration in Language Models. In Cohn, T.; He, Y.; and
Liu, Y., eds., Findings of the Association for Computational
Linguistics: EMNLP 2020, 3356–3369. Online: Association
for Computational Linguistics.
Ghafouri, V.; Agarwal, V.; Zhang, Y.; Sastry, N.; Such, J.;
and Suarez-Tangil, G. 2023. AI in the Gray: Exploring Mod-
eration Policies in Dialogic Large Language Models vs. Hu-
man Answers in Controversial Topics. In Proceedings of
the 32nd ACM International Conference on Information and
Knowledge Management, 556–565.
Gupta, S.; Shrivastava, V.; Deshpande, A.; Kalyan, A.;
Clark, P.; Sabharwal, A.; and Khot, T. 2024.
Bias
Runs Deep: Implicit Reasoning Biases in Persona-Assigned
LLMs. arXiv:2311.04892.
Hackenburg, K.; Tappin, B. M.; Hewitt, L.; Saunders, E.;
Black, S.; Lin, H.; Fist, C.; Margetts, H.; Rand, D. G.; and
Summerfield, C. 2025. The Levers of Political Persuasion
with Conversational AI. arXiv:2507.13919.
Haller, P.; Aynetdinov, A.; and Akbik, A. 2023.
Opin-
ionGPT: Modelling Explicit Biases in Instruction-Tuned
LLMs. arXiv:2309.03876.
Hartmann, J.; Schwenzow, J.; and Witte, M. 2023. The po-
litical ideology of conversational AI: Converging evidence
on ChatGPT’s pro-environmental, left-libertarian orienta-
tion. arXiv:2301.01768.
Hill, K. 2025. She Is in Love With ChatGPT. The New York
Times. Accessed: 30-April-2025.
Hu, T.; and Collier, N. 2024. Quantifying the Persona Effect
in LLM Simulations. In Ku, L.-W.; Martins, A.; and Sriku-
mar, V., eds., Proceedings of the 62nd Annual Meeting of the
Association for Computational Linguistics (Volume 1: Long
Papers), 10289–10307. Bangkok, Thailand: Association for
Computational Linguistics.
Huang, Y.; Zhang, Q.; Y, P. S.; and Sun, L. 2023. Trust-
GPT: A Benchmark for Trustworthy and Responsible Large
Language Models. arXiv:2306.11507.
Hubinger, E.; Jermyn, A.; Treutlein, J.; Hudson, R.; and
Woolverton, K. 2023.
Conditioning Predictive Models:
Risks and Strategies. arXiv:2302.00805.
Jenny, D. F.; Billeter, Y.; Sachan, M.; Sch¨olkopf, B.; and
Jin, Z. 2024. Exploring the Jungle of Bias: Political Bias
Attribution in Language Models via Dependency Analysis.
arXiv:2311.08605.
Kirk, H.; Vidgen, B.; R¨ottger, P.; and Hale, S. 2024. The
benefits, risks and bounds of personalizing the alignment of
large language models to individuals. Nature Machine Intel-
ligence, 6(4).
Kraft, A.; Simon, J.; and Schimmler, S. 2025.
So-
cial Bias in Popular Question-Answering Benchmarks.
arXiv:2505.15553.
Kraft, A.; and Soulier, E. 2024. Knowledge-Enhanced Lan-
guage Models Are Not Bias-Proof: Situated Knowledge and
Epistemic Injustice in AI. In Proceedings of the 2024 ACM
Conference on Fairness, Accountability, and Transparency,
FAccT ’24, 1433–1445. New York, NY, USA: Association
for Computing Machinery. ISBN 9798400704505.
Krieg, K.; Parada-Cabaleiro, E.; Medicus, G.; Lesota, O.;
Schedl, M.; and Rekabsaz, N. 2023. Grep-BiasIR: A Dataset
for Investigating Gender Representation-Bias in Information
Retrieval Results. arXiv:2201.07754.
Kwiatkowski, T.; Palomaki, J.; Redfield, O.; Collins, M.;
Parikh, A.; Alberti, C.; Epstein, D.; Polosukhin, I.; Devlin,
J.; Lee, K.; Toutanova, K.; Jones, L.; Kelcey, M.; Chang, M.-
W.; Dai, A. M.; Uszkoreit, J.; Le, Q.; and Petrov, S. 2019.
Natural Questions: A Benchmark for Question Answering
Research.
Transactions of the Association for Computa-
tional Linguistics, 7: 452–466.

--- Page 11 ---

Li, T.; Khashabi, D.; Khot, T.; Sabharwal, A.; and Sriku-
mar, V. 2020. UNQOVERing Stereotyping Biases via Un-
derspecified Questions. In Cohn, T.; He, Y.; and Liu, Y., eds.,
Findings of the Association for Computational Linguistics:
EMNLP 2020, 3475–3489. Online: Association for Compu-
tational Linguistics.
Lindemann, N. F. 2024. Chatbots, search engines, and the
sealing of knowledges. AI & SOCIETY, 1–14.
Liu, R.; Jia, C.; Wei, J.; Xu, G.; Wang, L.; and Vosoughi,
S. 2021.
Mitigating Political Bias in Language Models
Through Reinforced Calibration. arXiv:2104.14795.
Louwerse, T.; and Rosema, M. 2014. The design effects of
voting advice applications: Comparing methods of calculat-
ing matches. Acta Politica, 49: 286–312.
Lu, L.-C.; Chen, S.-J.; Pai, T.-M.; Yu, C.-H.; yi Lee, H.; and
Sun, S.-H. 2024. LLM Discussion: Enhancing the Creativity
of Large Language Models via Discussion Framework and
Role-Play. In First Conference on Language Modeling.
Lunardi, R.; La Barbera, D.; and Roitero, K. 2024.
The
Elusiveness of Detecting Political Bias in Language Mod-
els. In Proceedings of the 33rd ACM International Confer-
ence on Information and Knowledge Management, CIKM
’24, 3922–3926. Atlanta, GA, USA: ACM.
Maples, B.; Cerit, M.; Vishwanath, A.; and Pea, R. 2024.
Loneliness and suicide mitigation for students using GPT3-
enabled chatbots. npj mental health research, 3(1): 4.
Marschall, S.; and Schultze, M. 2012. Voting Advice Ap-
plications and their effect on voter turnout: the case of the
German Wahl-O-Mat. International Journal of Electronic
Governance, 5(3/4): 349–366.
Moayeri, M.; Tabassi, E.; and Feizi, S. 2024. WorldBench:
Quantifying Geographic Disparities in LLM Factual Recall.
In Proceedings of the 2024 ACM Conference on Fairness,
Accountability, and Transparency, FAccT ’24, 1211–1228.
New York, NY, USA: Association for Computing Machin-
ery. ISBN 9798400704505.
Motoki, F.; Pinho Neto, V.; and Rodrigues, V. 2024. More
human than human: measuring ChatGPT political bias. Pub-
lic Choice, 198(1): 3–23.
Munzert, S.; Barber´a, P.; Guess, A.; and Yang, J. 2020. Do
Online Voter Guides Empower Citizens? Evidence from a
Field Experiment with Digital Trace Data. Public Opinion
Quarterly, 84(3): 675–698.
Munzert, S.; and Ramirez-Ruiz, S. 2021. Meta-Analysis of
the Effects of Voting Advice Applications. Political Com-
munication, 38(6): 691–706.
Nadeem, M.; Bethke, A.; and Reddy, S. 2020. StereoSet:
Measuring stereotypical bias in pretrained language models.
arXiv:2004.09456.
Nangia, N.; Vania, C.; Bhalerao, R.; and Bowman, S. R.
2020.
CrowS-Pairs: A Challenge Dataset for Measuring
Social Biases in Masked Language Models.
In Webber,
B.; Cohn, T.; He, Y.; and Liu, Y., eds., Proceedings of the
2020 Conference on Empirical Methods in Natural Lan-
guage Processing (EMNLP), 1953–1967. Online: Associa-
tion for Computational Linguistics.
Nozza, D.; Bianchi, F.; and Hovy, D. 2021. HONEST: Mea-
suring Hurtful Sentence Completion in Language Models.
In Toutanova, K.; Rumshisky, A.; Zettlemoyer, L.; Hakkani-
Tur, D.; Beltagy, I.; Bethard, S.; Cotterell, R.; Chakraborty,
T.; and Zhou, Y., eds., Proceedings of the 2021 Confer-
ence of the North American Chapter of the Association for
Computational Linguistics: Human Language Technologies,
2398–2406. Online: Association for Computational Linguis-
tics.
Orlikowski, M.; R¨ottger, P.; Cimiano, P.; and Hovy, D. 2023.
The Ecological Fallacy in Annotation: Modeling Human La-
bel Variation goes beyond Sociodemographics. In Rogers,
A.; Boyd-Graber, J.; and Okazaki, N., eds., Proceedings
of the 61st Annual Meeting of the Association for Compu-
tational Linguistics (Volume 2: Short Papers), 1017–1029.
Toronto, Canada: Association for Computational Linguis-
tics.
Orr, W.; and Kang, E. B. 2024.
AI as a Sport: On the
Competitive Epistemologies of Benchmarking. In Proceed-
ings of the 2024 ACM Conference on Fairness, Accountabil-
ity, and Transparency, FAccT ’24, 1875–1884. New York,
NY, USA: Association for Computing Machinery.
ISBN
9798400704505.
Park, J. S.; O’Brien, J.; Cai, C. J.; Morris, M. R.; Liang,
P.; and Bernstein, M. S. 2023. Generative Agents: Interac-
tive Simulacra of Human Behavior. In Proceedings of the
36th Annual ACM Symposium on User Interface Software
and Technology, UIST ’23. New York, NY, USA: Associa-
tion for Computing Machinery. ISBN 9798400701320.
Parrish, A.; Chen, A.; Nangia, N.; Padmakumar, V.; Phang,
J.; Thompson, J.; Htut, P. M.; and Bowman, S. 2022. BBQ:
A hand-built bias benchmark for question answering.
In
Muresan, S.; Nakov, P.; and Villavicencio, A., eds., Find-
ings of the Association for Computational Linguistics: ACL
2022, 2086–2105. Dublin, Ireland: Association for Compu-
tational Linguistics.
Perez, E.; Ringer, S.; Lukoˇsi¯ut˙e, K.; Nguyen, K.; Chen, E.;
Heiner, S.; Pettit, C.; Olsson, C.; Kundu, S.; Kadavath, S.;
Jones, A.; Chen, A.; Mann, B.; and et al. 2022. Discover-
ing Language Model Behaviors with Model-Written Evalu-
ations. arXiv:2212.09251.
Pistilli, G.; Leidinger, A.; Jernite, Y.; Kasirzadeh, A.; Luc-
cioni, A. S.; and Mitchell, M. 2024. CIVICS: Building a
dataset for examining culturally-informed values in large
language models. In Proceedings of the AAAI/ACM Con-
ference on AI, Ethics, and Society, volume 7, 1132–1144.
Radhakrishnan, A.; Nguyen, K.; Chen, A.; Chen, C.;
Denison, C.; Hernandez, D.; Durmus, E.; Hubinger, E.;
Kernion, J.; Lukoˇsi¯ut˙e, K.; Cheng, N.; Joseph, N.; Schiefer,
N.; Rausch, O.; McCandlish, S.; Showk, S. E.; Lanham,
T.; Maxwell, T.; Chandrasekaran, V.; Hatfield-Dodds, Z.;
Kaplan, J.; Brauner, J.; Bowman, S. R.; and Perez, E.
2023. Question Decomposition Improves the Faithfulness
of Model-Generated Reasoning. arXiv:2307.11768.
Ranaldi, L.; and Pucci, G. 2024.
When Large Language
Models contradict humans? Large Language Models’ Syco-
phantic Behaviour. arXiv:2311.09410.

--- Page 12 ---

Rettenberger, L.; Reischl, M.; and Schutera, M. 2024.
Assessing Political Bias in Large Language Models.
arXiv:2405.13041.
Reuel, A.; Hardy, A.; Smith, C.; Lamparth, M.; Hardy,
M.; and Kochenderfer, M. 2024.
BetterBench: Assessing
AI Benchmarks, Uncovering Issues, and Establishing Best
Practices. In The Thirty-eight Conference on Neural Infor-
mation Processing Systems Datasets and Benchmarks Track,
1–51. New Orleans, LA, USA: Neural Information Process-
ing Systems Foundation.
Rogers, A.; Gardner, M.; and Augenstein, I. 2023.
QA
Dataset Explosion: A Taxonomy of NLP Resources for
Question Answering and Reading Comprehension.
ACM
Comput. Surv., 55(10).
R¨ottger, P.; Hofmann, V.; Pyatkin, V.; Hinck, M.; Kirk, H.;
Schuetze, H.; and Hovy, D. 2024. Political Compass or Spin-
ning Arrow? Towards More Meaningful Evaluations for Val-
ues and Opinions in Large Language Models. In Ku, L.-W.;
Martins, A.; and Srikumar, V., eds., Proceedings of the 62nd
Annual Meeting of the Association for Computational Lin-
guistics (Volume 1: Long Papers), 15295–15311. Bangkok,
Thailand: Association for Computational Linguistics.
Rozado, D. 2023. The Political Biases of ChatGPT. Social
Sciences, 12(3): 148.
Rozado, D. 2024. The political preferences of LLMs. PLOS
ONE, 19(7): 19.
Rudinger, R.; Naradowsky, J.; Leonard, B.; and Durme,
B. V. 2018.
Gender Bias in Coreference Resolution.
arXiv:1804.09301.
Rutinowski, J.; Franke, S.; Endendyk, J.; Dormuth, I.; and
Pauly, M. 2023. The Self-Perception and Political Biases of
ChatGPT. arXiv:2304.07333.
Santurkar, S.; Durmus, E.; Ladhak, F.; Lee, C.; Liang, P.; and
Hashimoto, T. 2023. Whose opinions do language models
reflect? In International Conference on Machine Learning,
29971–30004. PMLR.
Schiele, M.; Gittmann, Y.; Ilchmann, S.; Gojsalic, A.; Ju-
rinˇci´c, D.; and Klempt, P. 2024. Voting Advice Applications:
Implementation of RAG-supported LLMs.
Shanahan, M.; McDonell, K.; and Reynolds, L. 2023. Role
play with large language models. Nature, 623: 493–498.
Sharma, M.; Tong, M.; Korbak, T.; Duvenaud, D.; Askell,
A.; Bowman, S. R.; Durmus, E.; Hatfield-Dodds, Z.; John-
ston, S. R.; Kravec, S. M.; et al. 2024. Towards Understand-
ing Sycophancy in Language Models. In The Twelfth Inter-
national Conference on Learning Representations.
Shu, M.; Wang, J.; Zhu, C.; Geiping, J.; Xiao, C.; and Gold-
stein, T. 2023. On the Exploitability of Instruction Tuning.
arXiv:2306.17194.
Smith, E. M.; Hall, M.; Kambadur, M.; Presani, E.; and
Williams, A. 2022.
“I’m sorry to hear that”: Finding
New Biases in Language Models with a Holistic Descriptor
Dataset. In Goldberg, Y.; Kozareva, Z.; and Zhang, Y., eds.,
Proceedings of the 2022 Conference on Empirical Methods
in Natural Language Processing, 9180–9211. Abu Dhabi,
United Arab Emirates: Association for Computational Lin-
guistics.
Taubenfeld, A.; Dover, Y.; Reichart, R.; and Goldstein, A.
2024. Systematic Biases in LLM Simulations of Debates. In
Proceedings of the 2024 Conference on Empirical Methods
in Natural Language Processing, 251–267. Association for
Computational Linguistics.
Thapa, S.; Maratha, A.; Hasib, K. M.; Nasim, M.; and
Naseem, U. 2023. Assessing Political Inclination of Bangla
Language Models. In Alam, F.; Kar, S.; Chowdhury, S. A.;
Sadeque, F.; and Amin, R., eds., Proceedings of the First
Workshop on Bangla Language Processing (BLP-2023), 62–
71. Singapore: Association for Computational Linguistics.
Tseng, Y.-M.; Huang, Y.-C.; Hsiao, T.-Y.; Chen, W.-L.;
Huang, C.-W.; Meng, Y.; and Chen, Y.-N. 2024. Two Tales
of Persona in LLMs: A Survey of Role-Playing and Person-
alization. In Al-Onaizan, Y.; Bansal, M.; and Chen, Y.-N.,
eds., Findings of the Association for Computational Linguis-
tics: EMNLP 2024, 16612–16631. Miami, Florida, USA:
Association for Computational Linguistics.
Urman, A.; and Makhortykh, M. 2023. The Silence of the
LLMs: Cross-Lingual Analysis of Political Bias and False
Information Prevalence in ChatGPT, Google Bard, and Bing
Chat. OSF Preprints: osf.io/q9v8f.
Wang, Z. M.; Peng, Z.; Que, H.; Liu, J.; Zhou, W.; Wu,
Y.; Guo, H.; Gan, R.; Ni, Z.; Yang, J.; Zhang, M.; Zhang,
Z.; Ouyang, W.; Xu, K.; Huang, S. W.; Fu, J.; and Peng,
J. 2024.
RoleLLM: Benchmarking, Eliciting, and En-
hancing Role-Playing Abilities of Large Language Models.
arXiv:2310.00746.
Weber, E.; Rutinowski, J.; Jost, N.; and Pauly, M.
2024.
Is GPT-4 Less Politically Biased than GPT-3.5?
A Renewed Investigation of ChatGPT’s Political Biases.
arXiv:2410.21008.
Wei, A.; Haghtalab, N.; and Steinhardt, J. 2024. Jailbroken:
How does llm safety training fail? Advances in Neural In-
formation Processing Systems, 36.
Wei, J.; Huang, D.; Lu, Y.; Zhou, D.; and Le, Q. V. 2023.
Simple synthetic data reduces sycophancy in large language
models. arXiv:2308.03958.
Zhao, J.; Wang, T.; Yatskar, M.; Ordonez, V.; and Chang,
K.-W. 2018. Gender Bias in Coreference Resolution: Eval-
uation and Debiasing Methods. In Walker, M.; Ji, H.; and
Stent, A., eds., Proceedings of the 2018 Conference of the
North American Chapter of the Association for Computa-
tional Linguistics: Human Language Technologies, Volume
2 (Short Papers), 15–20. New Orleans, Louisiana: Associa-
tion for Computational Linguistics.
Zheng, M.; Pei, J.; Logeswaran, L.; Lee, M.; and Jurgens, D.
2024. When A Helpful Assistant Is Not Really Helpful: Per-
sonas in System Prompts Do Not Improve Performances of
Large Language Models. In Findings of the Association for
Computational Linguistics: EMNLP 2024, 15126–15154.
Zhou, L.; Gao, J.; Li, D.; and Shum, H.-Y. 2020. The De-
sign and Implementation of XiaoIce, an Empathetic Social
Chatbot. Computational Linguistics, 46(1): 53–93.

--- Page 13 ---

Figure 8: Radar Plots on Prompt Experiments with ChatGPT4o (gpt4o-2024-08-06). Each radar plot visualizes the prompt
experiment for one parliamentary group leader of a major political party (Temperature 0). The plots show the change in the
LLM responses’ party alignment when prompted “I am” and “You are”, compared to our benchmark GermanPartiesQA. We
selected parliamentary group leaders listed first on the German parliament’s official website in August 2024 for the 20th federal
parliament of Germany.

--- Page 14 ---

Figure 9: Radar Plots on Prompt Experiments with Claude 3 Sonnet (claude-3-sonnet-20240229). Each radar plot visualizes the
prompt experiment for one parliamentary group leader of a major political party (Temperature 0). The plots show the change
in the LLM responses’ party alignment when prompted “I am” and “You are”, compared to our benchmark GermanPartiesQA.
We selected parliamentary group leaders listed first on the German parliament’s official website in August 2024 for the 20th
federal parliament of Germany.

--- Page 15 ---

Figure 10: Radar Plots on Prompt Experiments with CommandR+ (command-r-plus-04-2024). Each radar plot visualizes the
prompt experiment for one parliamentary group leader of a major political party (Temperature 0). The plots show the change
in the LLM responses’ party alignment when prompted “I am” and “You are”, compared to our benchmark GermanPartiesQA.
We selected parliamentary group leaders listed first on the German parliament’s official website in August 2024 for the 20th
federal parliament of Germany.

```
