---
title: "2025-Andrew-Using Collective Dialogues and AI to Find Common Ground Between - PDF Extract"
source_pdf: "2025-Andrew-Using Collective Dialogues and AI to Find Common Ground Between.pdf"
pages: 23
extracted_at: "2026-02-15T17:51:58.724039"
---

# PDF Extract: 2025-Andrew-Using Collective Dialogues and AI to Find Common Ground Between

**Source PDF:** 2025-Andrew-Using Collective Dialogues and AI to Find Common Ground Between.pdf
**Total Pages:** 23

---

## Content

```
--- Page 1 ---

arXiv:2503.01769v3  [cs.HC]  19 Jun 2025
Using Collective Dialogues and AI to Find Common Ground
Between Israeli and Palestinian Peacebuilders
Andrew Konya
Remesh
Cleveland, OH, USA
andrew@remesh.org
Luke Thorburn
King’s College London
London, UK
luke.thorburn@kcl.ac.uk
Wasim Almasri
Alliance for Middle East Peace
Ramallah, Palestine
wasim@allmep.org
Oded Adomi Leshem
Hebrew University of Jerusalem
Jerusalem, Israel
oded.leshem@mail.huji.ac.il
Ariel D. Procaccia
Harvard University
Cambridge, MA, USA
arielpro@seas.harvard.edu
Lisa Schirch
University of Notre Dame
South Bend, IN, USA
lschirch@nd.edu
Michiel A. Bakker
Massachusetts Institute of Technology
Cambridge, MA, USA
bakker@mit.edu
ABSTRACT
A growing body of work has shown that AI-assisted methods —
leveraging large language models, social choice methods, and collec-
tive dialogues — can help navigate polarization and surface common
ground in controlled lab settings. But what can these approaches
contribute in real-world contexts? We present a case study applying
these techniques to find common ground between Israeli and Pales-
tinian peacebuilders in the period following October 7th, 2023. From
April to July 2024 an iterative deliberative process combining LLMs,
bridging-based ranking, and collective dialogues was conducted
in partnership with the Alliance for Middle East Peace. Around
138 civil society peacebuilders participated including Israeli Jews,
Palestinian citizens of Israel, and Palestinians from the West Bank
and Gaza. The process resulted in a set of collective statements,
including demands to world leaders, with at least 84% agreement
from participants on each side. In this paper, we document the
process, results, challenges, and important open questions.
CCS CONCEPTS
• Human-centered computing →Computer supported cooperative
work; • Applied computing →Voting / election technologies.
KEYWORDS
Peace, Conflict, Collective Response System, Collective Dialogue,
Bridging, Bridging-Based Ranking
ACM Reference Format:
Andrew Konya, Luke Thorburn, Wasim Almasri, Oded Adomi Leshem, Ariel
D. Procaccia, Lisa Schirch, and Michiel A. Bakker. 2025. Using Collective
Permission to make digital or hard copies of all or part of this work for personal or
classroom use is granted without fee provided that copies are not made or distributed
for profit or commercial advantage and that copies bear this notice and the full citation
on the first page. Copyrights for components of this work owned by others than ACM
must be honored. Abstracting with credit is permitted. To copy otherwise, or republish,
to post on servers or to redistribute to lists, requires prior specific permission and/or a
fee. Request permissions from permissions@acm.org.
FAccT ’25, June 23–26, 2025, Athens, Greece
© 2025 Association for Computing Machinery.
ACM ISBN 979-8-4007-1482-5/2025/06...$15.00
https://doi.org/10.1145/3715275.3732022
Dialogues and AI to Find Common Ground Between Israeli and Palestinian
Peacebuilders. In The 2025 ACM Conference on Fairness, Accountability, and
Transparency (FAccT ’25), June 23–26, 2025, Athens, Greece. ACM, New York,
NY, USA, 23 pages. https://doi.org/10.1145/3715275.3732022
1
INTRODUCTION
This paper documents an effort to find common ground between
Israeli and Palestinian peacebuilders amidst deeply entrenched divi-
sions that were amplified in the immediate aftermath of October 7th,
2023 and shaped by the broader context of protracted asymmetric
conflict. From April to July 2024, an iterative deliberative process
that combined collective dialogues [28], bridging-based ranking
[27], and large language models (LLMs) [18] was carried out in part-
nership with the Alliance for Middle East Peace (ALLMEP). More
than 100 civil society peacebuilders participated in the process in-
cluding Israeli Jews, Palestinian citizens of Israel, and Palestinians
from the West Bank and Gaza, representing diverse lived experi-
ences and interests. The process produced a set of collective state-
ments (Table 3) reflecting points of common ground — including
five statements to world leaders, and five to residents of the region
— with each statement supported by at least 84% of peacebuilders
on each side.
In recent years, there have been several proposals using algo-
rithmic methods to address polarization and find common ground.
Bridging-based ranking, a class of recommendation algorithms that
aims to surface content that builds trust and mutual understanding
across divides [27, 29], was first implemented on Australian policy
forum YourView in 2012 [44], and later gained prominence when
independently implemented on Polis [31, 32] and the Community
Notes feature on X (then Twitter) [45]. Large-scale, online collec-
tive dialogues [28] that incorporate matrix completion methods
to reduce the burden of preference elicitation have been used by
the United Nations for peacebuilding since 2020 [1, 4, 24]. Most
recently, there have been several proposals to use LLMs and social
choice mechanisms to find common ground and make collective
decisions on divisive issues [3, 10, 13, 33, 34].

--- Page 2 ---

FAccT ’25, June 23–26, 2025, Athens, Greece
Konya et al.
Most study of these methods — particularly bridging-based rank-
ing and LLM-based approaches to articulating common ground —
has occurred in lab settings, offline, or for relatively low-stakes con-
texts. For example, the approach used in this case study builds on a
specific integration of these methods that was initially developed
to produce common ground policy as part of OpenAI’s Democratic
Inputs to AI program [22], and subsequently refined for use in a
study on AI alignment [20]. In contrast, we present a case study
using a combination of these methods to find common ground be-
tween cross-border stakeholders amid active armed violence. This
required us to address a range of real-world challenges related to
trust, legitimacy, language barriers, and a constantly-changing sit-
uation. We believe this work may be the first to examine the use of
LLMs to bridge divides during a high-stakes real-world conflict.
Given this context, it is important to note two principles that
governed our approach:
• Impartiality: Drawing on best practices from peacebuilding
[35] and mediation [16], we aimed for both our process and
technology to be unbiased and fair: eliciting and representing
participant perspectives without bias, and enabling equitable
participation and influence over outcomes.
• Pragmatism: Given a context which presents urgent chal-
lenges, we prioritized iterative approaches to identify viable
solutions, rather than pursuing ideal outcomes that would
hinder progress due to extensive development or refinement.
In this vein, we emphasize this paper presents a case study from
a project aimed at supporting real-world peace processes, not aca-
demic research, which limited opportunities for controlled experi-
mentation or formal evaulation. As such, our approach reflects a
pragmatic reconciliation of established techniques with the con-
straints of a complex sociopolitical situation. Nonetheless, we be-
lieve the project can inform future academic work on the design
and use of technology in conflict settings and are thus, with the
permission of ALLMEP, publishing this case study.
The paper is structured as follows. Section 2 reviews situational
and technical context which motivated the project. Section 3 docu-
ments the method used to find common ground and explains key
design decisions. Section 4 reports the main insights and statements
(representing common ground) that resulted from the process. Fi-
nally, in Section 5 (and related appendices) we discuss ethical con-
siderations, the limitations of the process, and directions we intend
to prioritize in future work.
2
BACKGROUND
2.1
Situational
In the context of geopolitical conflicts, “track 1 diplomacy” in-
volving formal negotiations between governments is often sup-
plemented or supplanted by “backchannel” dialogue involving un-
official non-governmental representatives from each side. Such
backchannel dialogues may involve government officials partic-
ipating in an unofficial capacity (“track 1.5 diplomacy”) or may
not involve governments at all (“track 2 diplomacy”) [25]. Often,
these dialogues provide a more open environment to build trust and
discuss tough issues. Furthermore, they can enable cross-border
communication when formal diplomatic channels are closed. Civil
society peacebuilders typically play a significant role in convening
and contributing to these dialogues.
In early 2024, following the events of October 7th, 2023, and
within the broader context of protracted asymmetrical conflict,
tensions between Israeli and Palestinian peacebuilders had under-
standably intensified. Shaped not only by the recent escalation in
violence, but also by decades of structural disparity, open hostility,
and deep-seated mistrust, the substrate to discuss tough issues had
grown fragile1. In this context, we worked with the Alliance for Mid-
dle East Peace (ALLMEP) — a network of civil society peacebuilders
in the region — with the goal of strengthening that substrate. This
initiative sought to create a foundation for meaningful dialogue
grounded in shared humanity and collective action. To this end, we
sought to help peacebuilders find common ground. But the situation
presented a few real-world challenges.
Language: Peacebuilders’ native languages span Hebrew, Pales-
tinian Arabic, and English. Beyond communication, language car-
ries deep cultural and historical significance, where it has been a
tool of identity and a subtext of power imbalance. It was crucial for
inclusivity and legitimacy that participants could engage fully in
their native languages. Additionally, the sensitivity of language in
this context extends to word choices that may reflect deeply rooted
political and cultural meanings.
Trust: Skepticism and mistrust, stemming from historical experi-
ences of injustice, violence and prolonged conflict, posed significant
barriers to engagement. This meant that before we could reasonably
expect willingness to participate in joint dialogue, we would need
to elevate trust in good faith partnership. It also meant that the
process itself needed to hold up to scrutiny that the “other side” did
not have a mechanism to influence the results to their advantage.
Asymmetry: We expected, by default, there would be an un-
equal number of representatives participating from each side, yet it
would be anti-inclusionary to turn away participants from a side to
achieve balance. It was crucial to design a process that accounted
for structural asymmetries, ensuring that even with unequal repre-
sentation, all “sides” held equitable influence on the outcomes.
2.2
Technical
2.2.1
Collective dialogues. An online collective dialogue process
is an iterative back-and-forth exchange between a moderator and
participants. Participants join by clicking a link, and fill out demo-
graphic information as they enter the dialogue. During each turn
of the dialogue, participants are sent either a read-only message,
a standard survey question, or an open-ended prompt that kicks
off a collective response process. During a collective response pro-
cess [28], participants submit statements in response to the prompt,
then evaluate statements submitted by others. The evaluation step
serves two purposes: it exposes participants to others’ views to help
1In this paper, we intentionally chose to use politically neutral language and not impose
a characterization of the lived experiences of Palestinians and Israelis, including our
own. This includes deliberately omitting certain terms, such as “occupation,” that
have widely recognized legal and political significance under international law and
are central to the lived experiences of many participants in this process. We believe
it is consistent with the spirit of this work that any political positions conveyed by
this otherwise-technical paper should not be ours, but those manifest in the points
of common ground found among the peacebuilders who participated in this effort
(Table 3).

--- Page 3 ---

Using Collective Dialogues and AI to Find Common Ground Between Israeli and Palestinian Peacebuilders
FAccT ’25, June 23–26, 2025, Athens, Greece
Figure 1: The effort consisted of four dialogue cycles with peacebuilders: three uninational dialogues cycles conducted re-
spectively with Israeli Jews, Palestinians from the West Bank and Gaza, and Palestinian citizens of Israel, followed by a final
joint dialogue involving all three groups. Each dialogue cycle involved a process to find common ground among participants
followed by a deliberation on the results of that process. The common ground process started with a collective dialogue, then
bridging-based ranking was used to identify common ground “bridging statements” that were distilled into articulate “collective
statements” via LLM and reviewed by human experts before being shared back with participants for a final vote. The method is
described in detail in Section 3.

--- Page 4 ---

FAccT ’25, June 23–26, 2025, Athens, Greece
Konya et al.
them better understand each other, and it elicits data for quantify-
ing each statement’s representativeness. On the collective dialogue
platform used for this project (Remesh), two types of evaluations
are elicited; agreement votes, and pair choice votes. To maximize
the number of dialogue turns viable within a fixed budget of par-
ticipant time, and decouple votes per participant needed from the
number of statements submitted, votes are sparsely sampled and
a matrix completion method [4, 21] is used to convert a sparse
vote sampling into a complete participant vote matrix. The percent
agreement each participant segment has with each statement is
then computed by combining the complete vote matrix with the
demographic data of the participants. Collective dialogues can be
run both live and asynchronously (see Appendix B.1). They typi-
cally include on the order of ten collective response prompts, and
take participants between 15-60 minutes to complete.
The United Nations has run collective dialogues on Remesh —
often referred to as “Digital Dialogues” — as part of peacebuilding
efforts since 2020 [42]. These collective dialogues are sometimes
conducted by special political missions in support of track 1 diplo-
matic processes, as was done by Stephanie Williams during ceasefire
negotiations in Libya [1, 41]. In other cases, they serve less formal
track 1.5 or track 2 activities associated with local field presences.
Overall, the UN has now run more than 60 collective dialogues
across the world including in Yemen [42], Iraq [39], Lebanon [40],
Haiti [38], Bolivia [37, 43], and Bahrain [36].
2.2.2
Bridging-based ranking. The term bridging-based ranking
refers to a class of ranking or recommendation algorithms that aim
to “increase mutual understanding and trust across divides, creating
space for productive conflict, deliberation, or cooperation”‘[29].
Most commonly, this qualitative goal is operationalized as “diverse
approval,” meaning that items are ranked by the degree to which
they are approved of or valued by clusters of participants who
would normally be expected to disagree with each other (in other
words, ranking by diverse approval surfaces a form of “common
ground”). Implementations of this core intuition differ, for example
with respect to whether clusters are stipulated or learned from the
data [32], and how diversity is quantified. Below, we review two
existing approaches which we used in this project.
Let 𝑃denote a set of people, G denote a set of groups (that is,
a set of subsets of 𝑃), and 𝑆denote a set of items to be ranked,
which in our context are natural language statements. Perhaps the
simplest approach is max-min agreement, where items are ranked
by the minimum rate of agreement they receive across each group.
Formally, for a group 𝐺∈G and statement 𝑠∈𝑆, let 𝑎(𝑠,𝐺) denote
the proportion of people in group 𝐺that agree with statement 𝑠.
Under the max-min agreement approach, statements in 𝑠∈S are
ranked according to the metric
𝑎min(𝑠, G) = min{𝑎(𝑠,𝐺) | 𝐺∈G}.
This metric has been used previously in collective dialogue pro-
cesses run on Remesh [20, 22].
Another prominent approach to bridging is the algorithm used
by the Community Notes feature on the social media platform X.
It elicits crowd-sourced notes that add context to posts, but only
shows them publicly if (to simplify slightly) they are rated as helpful
by people on both sides of a learned political spectrum. To achieve
this, the algorithm fits a latent factor model to the observed agree-
ment votes, which provides for each note a factor corresponding
to its slant along the most salient dimension of disagreement [45].
Formally, let 𝑣(𝑠, 𝑝) ∈{1, −1} denote whether person 𝑝said they
respectively agreed or disagreed with statement 𝑠. The Community
Notes algorithm then fits the following model
ˆ𝑣(𝑠, 𝑝) ≈𝜇+ 𝑖𝑝+ 𝑖𝑠+ f𝑝· f𝑠.
The global intercept 𝜇captures the overall likelihood of any voter
to agree2 with any statement, the user intercept 𝑖𝑝captures voter
𝑝’s overall likelihood to agree with any statement, and the note
intercept 𝑖𝑠captures the voting population’s overall likelihood to
agree with statement 𝑠. The last term f𝑝· f𝑠represents the product
of the voter and statement factors,3, respectively. Model parameters
are fit by minimizing a regularized least-squared loss via gradient
descent over the dataset of observed votes. Once learned, the note
and user factors map statements and voters along learned axes
spanning “sides” of division, while the note intercept 𝑖𝑠gives a side-
independent measure of agreement. Because the note intercept 𝑖𝑠
is side-independent, we can use it to find statements that bridge
across people on different sides.
2.2.3
Language models. Large language models (LLMs) are increas-
ingly being recognized for their potential to address societal chal-
lenges by enhancing collaboration and fostering collective intel-
ligence. These models offer new ways to process and synthesize
diverse viewpoints, enabling the articulation of shared perspectives
even in deeply divided groups [2, 13, 34]. For example, in collec-
tive dialogue systems, LLMs can distill participant responses into
coherent statements that reflect areas of agreement. Beyond syn-
thesizing viewpoints and identifying areas of agreement, LLMs can
play a critical role in overcoming language barriers. They offer real-
time translation, text-to-speech and summarization capabilities,
ensuring participants can engage fully in their native languages.
This functionality helps make deliberative processes more inclusive,
equitable, and accessible [9]. However, careful implementation is
essential to avoid risks such as bias and misrepresentation.
3
METHOD
3.1
Common ground process
The core of our approach is a process (Figure 1) that integrates
collective dialogues, bridging-based ranking, and LLMs4 to help
identify, articulate, and validate points of common ground among a
group of participants. The process begins with a collective dialogue
(Step 1) in which participants anonymously respond to prompts
and evaluate the responses of others. The responses that are most
likely to represent common ground are identified using bridging-
based ranking (Step 2) and distilled into a set of well-articulated
collective statements using an LLM pipeline (Step 3). The collective
2In the Community Notes implementation used for posts on X, the primary vote
reflected in ˆ𝑣(𝑠, 𝑝) is not “agree”, but “helpful”. While the math is the same, here
we describe the algorithm in terms of “agree” votes in order to maintain consistency
across descriptions of the methods used in this paper.
3These factors can be scalars that capture only the primary axis of voter variance, as
in the original Birdwatch paper [45], or vectors that capture multi-dimensional factors
of vote variance.
4For all LLM tasks in this project, we used models from OpenAI’s GPT-4 series. Specif-
ically, during the uninational phase we used gpt-4-turbo-2024-04-09, and during
the joint phase we used gpt-4-0125-preview.

--- Page 5 ---

Using Collective Dialogues and AI to Find Common Ground Between Israeli and Palestinian Peacebuilders
FAccT ’25, June 23–26, 2025, Athens, Greece
statements are then shared back with participants for a final vote
(Step 4). The primary outputs of each run of the process are a set
of collective statements along with the results of the final vote. We
describe each step in more detail below.
3.1.1
Step 1: Collective dialogue. The first step towards a collective
dialogue is drafting the planned prompts participants will respond
to and deciding what demographics to gather. Prompt drafting is
informed by the goals of the dialogue: specific issues to find common
ground on, areas to create more mutual understanding around,
and so on. Draft prompts are reviewed and iterated until deemed
acceptable by a stakeholder group with representation from all sides.
The choice of demographics are determined by (a) demographic
dimensions likely to manifest relevant divisions, (b) demographics
needed to assess representativeness, and (c) constraints imposed
by the need for statistical anonymity [6].
In this work, the collective dialogues were first run live, then
reopened for asynchronous participation as needed. The date and
time of the live dialogue was typically set a week or two in advance
and communicated with participants so they could plan accordingly.
The live event began with a Zoom video call where the dialogue
was contextualized, then a link was shared with participants to join
the collective dialogue on Remesh. After the live dialogue was over,
it was re-opened for asynchronous participation for a few days.
Each collective dialogue generates a a set of natural language
statements 𝑆responding to each prompt, a sparse sampling of votes
on each statement 𝑠∈𝑆, participant demographics, and data for the
non-collective-response questions asked during the dialogue. Vote
inference [21] is then used to complete the agreement-vote matrix
with elements 𝑣(𝑠, 𝑝) ∈{1, 0} ≡{𝑎𝑔𝑟𝑒𝑒,𝑑𝑖𝑠𝑎𝑔𝑟𝑒𝑒} that indicate the
(stated or inferred) agreement of participant 𝑝with statement 𝑠.
3.1.2
Step 2: Identifying bridging statements. The goal of this step
is to identify a set of “bridging” statements 𝐵⊆𝑆that are likely
to represent points of common ground. To do this, we computed
two bridging metrics for each statement 𝑠∈𝑆: (1) max-min agree-
ment 𝑎min(𝑠, G) across defined demographic groups G, and (2) the
learned parameters (𝑓𝑠,𝑖𝑠) from the Community Notes algorithm
(see Section 2.2.2). As a first set of bridging statements, we selected
statements 𝑠∈𝑆where 𝑎min(𝑠, G) was greater than a given thresh-
old. This gives the set of statements that have the highest lowest
agreement across the specified set G of demographic groups. How-
ever, when 𝐺contains many demographic groups — defined by age,
gender, religiosity, etc. — this approach may exclude a statement
that may otherwise bridge a critical axis of division just because it is
predicted (perhaps incorrectly) to have low agreement among one
demographic sub-group. To mitigate this risk, we created a second
set of bridging statements using the Community Notes approach
by selecting those where the Euclidean distance 𝑑((𝑓𝑠,𝑖𝑠), (0, 2))
was below a given threshold. This approach relies primarily on the
note intercept 𝑖𝑠as a bridging metric, but also penalizes statements
for having non-zero slant, as indicated by the note factor 𝑓𝑠. The
complete set of bridging statements 𝐵is taken to be the union of
the sets of statements emerging from both approaches.
3.1.3
Step 3: Distillation into collective statements. The set of bridg-
ing statements identified in the previous step typically includes
multiple restatements of the same idea, compound statements cov-
ering multiple ideas, and sub-optimal articulations of ideas. The
goal of Step 3 is to create well-articulated versions of each of unique
idea that appears in the bridging statements in a way that preserves
participants’ choices of specific words and phrases. We use an LLM
to do this in two steps. First, the LLM is prompted to extract the
unique ideas from the set of bridging statements. Next, the LLM
is prompted to generate well-articulated versions of each unique
idea in a way that preserves the words and phrases found in the
original statements. Included in this prompt are the set of unique
ideas, the text of the bridging statements the unique ideas were
derived from, and a set of exemplar statements that demonstrate
the style in which collective statements should be written. Finally,
the collective statements proposed by the LLM are reviewed by
local language experts for linguistic consistency with the original
bridging statements, and iterated as needed until a final set of col-
lective statements 𝐶is deemed fair by a stakeholder group with
representation from all sides. The LLM prompts used for this step
are included in Appendix H.
3.1.4
Step 4: Final vote. We expect the collective statements that
reach this point to generally represent common ground. However,
the use of both AI and human experts in the prior steps introduce
potential sources of error and bias. These risks can rightfully dele-
gitimize the claim that the collective statements actually represent
common ground. The final vote is thus a critical step that serves
to strengthen legitimacy by measuring support for the collective
statements in a simple and transparent way. During the final vote,
all participants vote on all collective statements. There is no AI
inference or synthesis, and results are computed via deterministic
and reproducible methods.
Participants cast two types of votes on each final collective state-
ment. First, a simple vote of agreement with each statement is cast
by each participant on a 5-point Likert scale. This enables a direct
measurement of how well each statement collectively represents a
point of agreement on all sides. In the second type of vote, partici-
pants are asked to rank the set of statements in order of agreement.
Even if all collective statements represent clear points of common
ground, they may not be equally important. The relative votes pro-
vide an additional signal to understand how the set of common
ground collective statements should be prioritized.
3.1.5
Joint reviews. Even though the final vote serves as a hedge
against biases that could cause collective statements to not repre-
sent common ground, unfair bias at any point in the process can
still undermine legitimacy. To mitigate this risk, at key junctures
in the process where bias might be introduced, joint reviews were
conducted by representatives of each side before moving on to the
next step (see Figure 1). Specifically, joint reviews were conducted
on: the content and wording of all messages, questions, and collec-
tive response prompts that would be seen by participants in the
collective dialogue, the collective statements that would go on to
the final vote, and the results computed from the final vote data.
3.2
Dialogue cycles
3.2.1
Transitional deliberation. We made our approach iterative
by adding a transitional deliberation that marks the end of one

--- Page 6 ---

FAccT ’25, June 23–26, 2025, Athens, Greece
Konya et al.
dialogue cycle and the beginning of the next; serving to translate
the outputs of one cycle to the inputs of the next cycle. These
deliberations involved a small group of Israeli and Palestinian pro-
cess facilitators and stakeholders. Each deliberation started with
contextualization and sensemaking to establish mutual understand-
ing related to the results, then transitioned to prompt design and
participant communications for the next cycle.
3.2.2
Strategic sequencing. Our goal was to run a joint common
ground process involving cross-border dialogue between peace-
builders from all sides, but before doing so we sought to build trust
in the process and among those involved. To this end, we began
with a uninational phase, where each dialogue cycle involved par-
ticipants from only one side, in order to first find points of common
ground within each group that could be communicated to help
elevate trust and willingness to engage in the subsequent cycles.
What constitutes a “side”? It may seem obvious that “Israelis”
and “Palestinians” would be the two sides. However, this binary
approach would have risked marginalizing Palestinian citizens of
Israel, may not fully identify with either Israelis or Palestinians. To
accommodate this, we chose to treat Palestinian citizens of Israel as
a third independent group, along side Israeli Jews and Palestinians
from the West Bank and Gaza. In the remainder of this paper, we use
G to denote this set of groups, namely G = {Israeli Jews, Palestinian
citizens of Israel, Palestinians from the West Bank and Gaza}.
During the uninational phase, the group that went first needed to
do so without the benefit of any trust-building feedback from earlier
cycles. Given the existing power asymmetry, it was decided that
Israeli Jews would go first. As the second major group, Palestinians
from the West Bank & Gaza went second, followed by Palestinian
citizens of Israel. Finally, after these three uninational dialogues,
we conducted a joint dialogue with participants from all groups to
attempt to identify cross-border common ground (Figure 1).
3.3
Participants and Experts
Dialogue participants were recruited via invitations circulated to
ALLMEP member organizations (see, e.g. Appendix F). ALLMEP
leadership also personally contacted leaders of different organiza-
tions to invite participation. Because participants were anonymous
and there were multiple stages within each dialogue cycle with no
way of tracking identities across stages, it’s not possible to know the
exact number of unique participants. We estimate a lower bounds
on the number of unique, meaningfully engaged participants in
each of the four dialogue cycles to be 70, 28, 13, and 138, respec-
tively (see Appendix G for a detailed breakdown). Additionally, the
process included “human experts” in-the-loop, mentioned through-
out this Methods section. This small group of experts was hand
selected by process facilitators. They consisted of ALLMEP staff
and two academics with relevant peacebuilding expertise.
3.4
Languages
It was critical for legitimacy and inclusivity that participants could
fully engage in their primary languages. The uninational cycles
would be mono-lingual (Hebrew or Palestinian Arabic), and the
joint cycle would need to be multilingual. The main challenge for
the mono-lingual cycles was the LLM pipeline used to generate
collective statements. Early versions of the pipeline used in prior
work [20, 22] had proven effective when the prompts, examples,
bridging statements, and generated outputs were all in English, but
it was unclear how to approach Hebrew and Palestinian Arabic.
Should prompts or examples still be in English? And who decides?
To pragmatically address these questions we set up two micro-
experiments. We compiled a set of plausible bridging statements in
each language and asked native speakers with prompt engineering
experience to translate the English prompts and examples. Different
variations of the pipeline were created by swapping out different
permutations of the English prompts and examples with translated
versions. Collective statements were generated using each variation.
Then, blind to how they were generated, native speakers were
asked which set of collective statements best reflected the content,
culture, and language of the original statements they were based
on. In all cases, reviewers preferred the statements generated by a
pipeline with prompts and examples in their native language, so
these variants were used for the uninational phase.
For the joint cycle, a trilingual approach encompassing Hebrew,
Palestinian Arabic, and English was implemented to maximize ac-
cessibility and inclusivity. This required the provision of all textual
materials — including collective response prompts, participant-
generated statements, synthesized collective statements, and re-
sult presentations — in all three languages. All collective dialogue
prompts were initially drafted in English, then translated to the
other languages using the Google Cloud Translation API (here-
after, “Google Translate”) and refined by native speakers. During
the live dialogue, Google Translate was used to create trilingual ver-
sions of each statement in real-time. Acknowledging the inherent
limitations of machine translation and the potential for semantic
nuances to be lost or distorted, we adopted a transparent approach,
explicitly informing participants about the use of Google Translate.
Participants were also asked to use clear and concise language to
mitigate the risk of translation errors. We conducted a set of micro-
experiments on the multilingual LLM pipeline similar to those run
for the monolingual pipeline. The final LLM output was a set of
trilingual collective statements that would be reviewed and refined
by native speakers for consistency across translations and with
the original bridging statements. Final results were compiled in a
spreadsheet and a trilingual lookup table for all elements in main
view results, including labels and metrics, was initialized via Google
Translate and then jointly reviewed and refined by native speakers.
3.5
Equal power metrics
For the joint cycle, it was critical that result metrics computed from
final vote data (ranking and agreement votes) give each side equal
influence even with unequal shares of participants. To that end, we
computed three equal-power metrics — metrics that are invariant
to the portion of participants from each side — for each collective
statement: max-min agreement, Dowdall score, and IRV rank.
3.5.1
Max-min agreement. Max-min agreement, the same metric
used for bridging-based ranking in Step 2, was computed again
using the final agreement votes. Specifically, for each collective
statement 𝑠, max-min agreement was computed as min{𝛼(𝑠,𝐺) |
𝐺∈G} where 𝛼(𝑠,𝐺) is the fraction of participants in group 𝐺
that voted “agree” or “strongly agree” on statement 𝑠. This metric

--- Page 7 ---

Using Collective Dialogues and AI to Find Common Ground Between Israeli and Palestinian Peacebuilders
FAccT ’25, June 23–26, 2025, Athens, Greece
inherently provides equal power across groups and offers a straight-
forward interpretation: it indicates the minimum level of agreement
across all defined groups for statement 𝑠.
3.5.2
Dowdall score. Similar to a Borda count [5], a Dowdall score
is a cardinal metric computed from rank votes using a positional
scoring rule that quantifies the strength of relative preference
among a set of alternatives for a voting population [14]. Let the
fraction of participants in population 𝑃who rank statement 𝑠in po-
sition 𝑘be denoted Position(𝑠,𝑘; 𝑃). A Dowdall score is computed
as
Dowdall(𝑠; 𝑃) =
∑︁
𝑘
Points(𝑘) × Position(𝑠,𝑘; 𝑃),
where Points(𝑘) = 1/𝑘corresponds to the “points” assigned to each
position. We adapt this to be an equal power metric by taking the
average of Dowdall scores computed independently for each side:
DowdallEP(𝑠) =
1
|G|
∑︁
𝐺∈G
Dowdall(𝑠;𝐺).
This averaging approach ensures that each group’s collective pref-
erences contribute equally to the final equal-power Dowdall score,
regardless of group size.
3.5.3
IRV rank. An instant runoff voting (IRV) rank is an ordinal
metric derived from rank votes by iteratively eliminating the option
with the fewest first-place votes among remaining options [5]. Let
𝑆𝑛be the set of statements remaining in round 𝑛, and First(𝑠,𝑛; 𝑃)
give the fraction of participants (in some population 𝑃) who rank
statement 𝑠first among 𝑆𝑛. The statements remaining in round 𝑛+1
are 𝑆𝑛+1 = 𝑆𝑛\ {arg min𝑠∈𝑆𝑛First(𝑠,𝑛; 𝑃)}.5 Denoting 𝑛𝑠to be the
round where statement 𝑠was eliminated, and |𝐶| the total number
of statements being ranked, the IRV rank is IRV(𝑠) = |𝐶| −𝑛𝑠+1. To
make this an equal power metric, the “first place fraction” First(𝑠,𝑛)
used to eliminate statements in each round is computed as an
average of the first place fractions within each group. That is,
FirstEP(𝑠,𝑛) =
1
|G|
∑︁
𝐺∈G
First(𝑠,𝑛;𝐺).
4
RESULTS
When interpreting the results presented here, it’s important to con-
sider a few contextual factors. First, given the sensitive nature of
the issues addressed in these dialogues and their direct relevance to
ongoing peacebuilding efforts, the results shared are intentionally
selective. Specifically, we present: (1) findings from the uninational
phase that demonstrably facilitated the subsequent joint phase, and
(2) collective statements of common ground from the joint phase
that were explicitly intended for external communication. Further-
more, the quantitative results we share are limited to metrics that
give equal power representation across primary participant groups.
Second, these findings should not be understood as the views of the
broader Israeli and Palestinian populations. The participant pool,
with an approximate sample size of no more than 𝑁= 138 for any
dialogue cycle, is not only statistically insufficient for generaliza-
tion, but was comprised exclusively of civil society peacebuilders.
Third, while some of the identified areas of common ground may
5This formulation assumes no ties for last place, which was true with our data.
appear self-evident in retrospect, at that time this project us un-
dertaken, a prevailing sentiment held that finding common ground
was unlikely, and the prospect of a constructive joint dialogue was
viewed with considerable skepticism.
4.1
Uninational Phase
A key aim of the uninational phase was building trust and creating
the context under which a productive cross-border engagement
in the joint phase could take place. To this end, each cycle was
designed to identify red lines, values, and visions for the future.
4.1.1
Red lines. In our work, the term “red lines” refers to ac-
tions (including speech acts) that those participating in the process
believe are unacceptable, and if undertaken may prevent further
dialogue. We asked about two kinds of red lines: ingroup (the lines
that each side themselves would not cross) and outgroup (the lines
that each side would not accept the “other side” crossing). These
red lines served a few purposes. Ingroup red lines would provide a
trust building signal if they articulated positions that demonstrated
respect for the concerns of the other side. The combination of both
types of red line across groups would help clarify the boundary
conditions under which a productive joint dialogue could take place.
In this context, one notable result of this phase was the mutual
alignment between the ingroup and outgroup red lines of Israeli
Jews and Palestinians from the West Bank & Gaza. For each of the
top three outgroup red lines on each side, the other side had an
arguably related ingroup red line that demonstrated some degree
of relevant respect and aligned ethics (Table 1). For example, “call
for forced displacement” was a top outgroup red line from Pales-
tinians from the West Bank & Gaza, while “talk about deporting
Palestinians” was a top ingroup red line from Israeli Jews.
Another notable result came during the transitional deliberation
at the end of first dialogue cycle with Israeli Jews. While reviewing
a top outgroup red line – “the justification for the attack on Octo-
ber 7th” – strong concern emerged that prohibiting explanation
about why October 7th happened would be an unfair constraint
on joint dialogue. In the exchange that followed, a mutual under-
standing emerged: “justification” specifically involved a claim of
moral rightness, while an “explanation” was a neutral analysis of
causation. So claiming the attack was morally right was the red line,
but explaining what caused it to happen was not. This distinction
not only applied to many collective statements throughout the pro-
cess, but helped introduce language like “I won’t justify [X], but an
explanation is...” as a rhetorical device for discussing tough issues.
4.1.2
Values and visions. Values and visions were intended to help
each side articulate the moral values they held and the future out-
comes they sought to achieve. In the spirit of a “GRIT” (Graduated
and Reciprocated Initiatives in Tension reduction) approach [23],
our hypothesis was that commonalities would emerge across all
sides that could serve as early points of common ground, prior to
the joint dialogue process actually taking place. After all three uni-
national cycles had concluded, the collective statements entailing
values and vision were compared and a set of coarse-grained shared
values and visions (Table 2) were identified: peace, equality, human
life, independence, safety, and prosperity.

--- Page 8 ---

FAccT ’25, June 23–26, 2025, Athens, Greece
Konya et al.
Table 1: Top three outgroup red lines along with potentially related ingroup red lines from the other side. Note that the nature
of relatedness between the red lines shown is non-specific, and does not imply direct alignment nor suggest equivalency in
content or scope. In the column headers of this table, the adjectives “Israeli” and “Palestinian” refers to participants of the
uninational dialogue cycles with Israeli Jews and Palestinians from the West Bank and Gaza, respectively.
Top Israeli outgroup red lines
Related Palestinian ingroup red lines
Harming Israeli citizens is crossing a red line
פגיעה באזרחים ישראלים היא חציית קו אדוםSupport or justify violence
ﺩ؜ܾﺍܳأٷژﺃﻭ ّଊଫߌߵﻩ
The justification for the attack on October 7 is crossing a red line
באוקטובר היא חציית קו אדום7הצדקת ההתקפה ב
Calling for the destruction of Israel is crossing a red line
קריאה להשמדת ישראל היא חציית קו אדום
Refusing to recognize the Israeli side
ঌॻਃಮﺭڣݥﺍ৑৖༟ଐଫﺍﻑ ً؇ࠍ੊؇಻ೞﺍ৑৖ང๤ﺍ
Top Palestinian outgroup red lines
Related Israeli ingroup red lines
Call for forced displacement
ﺍᄟᄴ؜ިﺓﺇᇿሌﺍܳውዛ༶ଃଫﺍܳگཡ๤ﻱ
Talk about deporting Palestinians is crossing a red line
שיח על גירוש פלסטינים הוא חציית קו אדום
Abolishing the existence of the other and not recognizing the rights of the Palestinians
ඔ൹٭ྡྷ٭ޚފܹڰܳﺍܳ؞؇ﺀﻭۏިﺩﺍ৑৖ඝරﻭ༟ڎﻡﺍ৑৖༟ଐଫﺍﻑຳොگިﻕﺍ
Depriving Palestinians of human rights is crossing a red line
קיפוח זכויות אדם של פלסטינים הוא חציית קו אדום
Supporting the war on Gaza and supporting the army and seeing that it is a moral army
ሒᇬఈః༠ﺩ؜ܾﺍࠍ੆ݠﺏ༟ॻআ ؗਲ਼ﺓﻭﺩ؜ܾﺍࠍ੊྘ݷﻭﺭﺅل۰ﺃَ۬༥྘ݷﺃ
Harming Palestinian civilians is crossing a red line
פגיעה באזרחים פלסטינים היא חציית קו אדום
Overall, around 100 peacebuilders participated in the unina-
tional phase and the intra-group points of common ground that
were identified were communicated back with peacebuilders on all
sides. These results helped create the context for the joint phase to
take place. The mutually compatible red lines helped restore some
trust, and clarified the boundary conditions for a productive joint
dialogue. The values and visions served as a reminder of the shared
foundation that already existed and could be built on.
4.2
Joint phase
The joint phase covered a range of topics. Here we discuss the mo-
tivation and results for two of those: demands to world leaders, and
messages to residents in the region. These were chosen by work-
ing backward from what ALLMEP and its member organizations
were able to action. Internationally, ALLMEP acts as an interlocutor
between Israeli/Palestinian civil society and governments, and an
amplifier in the media. So, if the process could generate a set of
joint statements directed at world leaders, then ALLMEP would
be in a position to communicate these through their ongoing ad-
vocacy work. And since ALLMEP’s membership is composed of
civil society peacebuilding organizations in the region, a set of joint
messages to residents in the region could be used as part of their
members public communications strategy.
Around 138 people participated in the joint phase. Five collec-
tive statements comprising joint demands to world leaders were
produced (Table 3a). Each statement had at least 90% agreement
among participants from each side (i.e., 𝑎min(𝑠, G) > 90%), and one
demand was universally ranked first: “An immediate ceasefire and
release of all hostages.” These demands were then composed into a
“joint letter” for inclusion in briefs and advocacy efforts (Appendix
A). Additionally, five collective statements comprising joint mes-
sages to residents in the region were produced (Table 3b). Each of
these statements had at least 84% agreement among participants
from each side, with most statements being preferred about equally.
5
DISCUSSION
In this section, we discuss how this work can be evaluated, and
considerations and challenges encountered when using AI in this
context. Further discussion of ethical issues, limitations, and future
directions are included in Appendix D.
Evaluation. As this project was conducted in support of an ac-
tive peace process, it lacked the structure of well-controlled trials
that support rigorous comparative evaluations. Further, our pro-
cess did not directly replace an existing one to which it could be
directly compared. To the extent that it was replacing anything, it
could be partly viewed as replacing long deliberations where pro-
fessional mediators employ standard, labour-intensive approaches
to finding common ground, e.g., [11, 26, 30]. In contrast, ALLMEP
noted that “Without this process, our conversations would be smaller
and fragmented. This method brought voices together across political
and geographic divides in a way that traditional dialogue simply
couldn’t.”
The 10 public-oriented statements produced by this process had
between 84-96% bridging support, and nine had support over 90%.
While no perfect analogue exists to say how “good” these levels
of support are, we note that citizens assemblies — often cited for
their ability to find common ground on divisive issues — generally

--- Page 9 ---

Using Collective Dialogues and AI to Find Common Ground Between Israeli and Palestinian Peacebuilders
FAccT ’25, June 23–26, 2025, Athens, Greece
Table 2: Coarse-grained shared values and visions emerging from collective statements produced during the uninational phase.
Note that the succinct shared value or vision expressed in each row does not fully entail all ideas contained the associated
statements and only captures their abstract common thread. Similarly, presenting statements as associated with the same
shared value or vision does not imply equivalency between them.
(a) Shared values.
Shared Value
Israeli Jews
Palestinians from the
West Bank and Gaza
Palestinian citizens of Israel
Peace
The value of peace: recognition of the
right of all people to live in peace, security
and without violence
ערך השלום: הכרה בזכותם של כל האנשים לחיות
בשקט, ביטחון וללא אלימות
Promoting peace
ﺍﻟﺘﺮﻭﻳﺞﻟﻠﺴﻠ؝ﻡ
Recognizing the right to coexistence and
peace among different groups and
cultures
ﺍﻟﺎﻋﺘﺮﺍﻑﺑﺎﻟﺤﻖﻓﻲﺍﻟﻌﻴﺶﺍﻟﻤﺸﺘﺮﻙﻭﺍﻟﺴﻠﻤﻲ
ﺑﻴﻦﻣﺨﺘﻠﻒﺍﻟﺠﻤﺎﻋﺎﺕﻭﺍﻟﺜﻘﺎﻓﺎﺕ
Equality
The value of equality: every person has
the right to enjoy equal rights regardless
of their origin or nationality
ערך השוויון: לכל אדם הזכות להנות מזכויות שוות
ללא תלות במוצאו או לאומיותו
Promoting justice and equality among
individuals
ﺗﻌﺰﻳﺰﺍﻟﻌﺪﺍﻟﺔﻭﺍﻟﻤﺴﺎﻭﺍﺓﺑﻴﻦﺍﻟﺄﻓﺮﺍﺩ
Justice, equality and liberation for all
ﺍﻟﻌﺪﺍﻟﺔﻭﺍﻟﻤﺴﺎﻭﺍﺓﻭﺍﻟﺘﺤﺮﻳﺮﻟﻠﺠﻤﻴﻊ
Human life
The value of life: commitment to
preserving human life in any situation and
under all circumstances
ערך החיים: מחויבות לשמירה על חיי האדם בכל
מצב ותחת כל הנסיבות
The value of human life
ﻗﻴﻤﺔﺣﻴﺎﺓﺍﻟﺎﻧﺴﺎﻥ
Humanity as a basic value in society
ﺍﻟﺈﻧﺴﺎﻧﻴﺔﻛﻘﻴﻤﺔﺃﺳﺎﺳﻴﺔﻓﻲﺍﻟﻤﺠﺘﻤﻊ
(b) Shared vision.
Shared Vision
Israeli Jews
Palestinians from the
West Bank and Gaza
Palestinian citizens of Israel
Independence
Two democratic countries with security
and economic cooperation
שתי מדינות דמוקרטיות עם שיתופי פעולה
ביטחוניים וכלכליים
Establishing an independent
Palestinian state
ﺇﻗﺎﻣﺔﺩﻭﻟﺔﻓﻠﺴﻄﻴﻨﻴﺔﻣﺴﺘﻘﻠﺔ
Recognition of the State of Palestine
ﺍﻟﺎﻋﺘﺮﺍﻑﺑﺪﻭﻟﺔﻓﻠﺴﻄﻴﻦ
Safety
Free and safe movement for everyone
in the entire space
תנועה חופשית ובטוחה לכולם בכל המרחב
Equality in rights and duties and
a sense of security
ﺍﻟﻤﺴﺎﻭﺍﺓﻓﻲﺍﻟﺤﻘﻮﻕﻭﺍﻟﻮﺍﺟﺒﺎﺕﻭﺍﻟﺸﻌﻮﺭﺑﺎﻟﺄﻣﺎﻥ
A safe and equal society
ﻣﺠﺘﻤﻊﺁﻣﻦﻭﻣﺘﺴﺎﻭﻱ
Prosperity
Economic growth and prosperity for all
residents of the region with mutual
respect for nature and the climate
צמיחה כלכלית ושגשוג לכל תושבי האזור עם כבוד
הדדי לטבע ולאקלים
Regional peace and prosperity
ﺳﻠ؝ﻡﻭﺍﺯﺩﻫﺎﺭﺇﻗﻠﻴﻤﻲ
Better job opportunities
ﻓﺮﺹﻋﻤﻞﺃﻓﻀﻞ
produce recommendations that have 60-95% overall support under
less tense circumstances [7, 8, 12, 15, 17, 19].
Participants in the process reported that the experience fostered
"a lot of self-reflection," that the anonymity enabled them to "share
openly, without fear of being judged" and that "seeing each other’s
anonymous thoughts in this way is valuable in and of itself." How-
ever, while most participants reported a positive experience, some
thought that in the live collective dialogues "Everything is so fast. It’s
hard to think." and that they "need to be able to speak to each other,
see each other’s faces” (see Appendix E for more of this feedback).
Use of AI. LLMs played a few critical roles in enabling this pro-
cess. First, they rapidly distilled numerous raw statements into man-
ageable, nuanced collective statements, replacing complex multi-
stakeholder deliberations (which can take months) with an LLM-
accelerated step of a few hours. This compressed each dialogue cy-
cle to weeks, making a recursive process viable. Second, LLMs and
machine translation made the multilingual cycle practical by reduc-
ing complex translation burdens, enabling multilingual collective
statement synthesis, and facilitating live multi-lingual dialogues
through low-latency translation. Third, LLM-enabled vote predic-
tion [21] improved data efficiency for the bridging-based ranking
and decreasing how much participants had to vote per prompt and
thus allowing more prompts within time-constrained dialogues.

--- Page 10 ---

FAccT ’25, June 23–26, 2025, Athens, Greece
Konya et al.
Table 3: Collective statements generated during the joint phase along with final vote results.
(a) Collective statements (i.e., demands) addressed to world leaders.
Collective statements
IRV rank
Dowdall score
Max-min agreement
An immediate ceasefire and release of all hostages
ﻭﻗﻒﺇﻃﻠ؝ﻕﺍﻟﻨﺎﺭﺍﻟﻔﻮﺭﻱﻭﺇﻃﻠ؝ﻕﺳﺮﺍﺡﺟﻤﻴﻊﺍﻟﺮﻫﺎﺋﻦ
הפסקת אש מיידית ושחרור כל החטופים
1
0.88
92%
Recognize both sides’ trauma
ﺍﻟﺎﻋﺘﺮﺍﻑﺑﺎﻟﺼﺪﻣﺔﺍﻟﺘﻲﻳﻌﻴﺸﻬﺎﻛﻠ؝ﺍﻟﺠﺎﻧﺒﻴﻦ
הכרה בטראומה של שני הצדדים
2
0.27
93%
Create an international fund to build foundations for a comprehensive solution
ﺇﻧﺸﺎﺀﺻﻨﺪﻭﻕﺩﻭﻟﻲﻟﺒﻨﺎﺀﺃﺳﺲﻟﺤﻞﺷﺎﻣﻞﻃﻮﻳﻞﺍﻟﺄﻣﺪ
יצירת קרן בינלאומית לבניית תשתית לפתרון לטווח ארוך
3
0.33
93%
Include civil society and NGOs in peacebuilding discussions
ﺇﺷﺮﺍﻙﻣﺆﺳﺴﺎﺕﺍﻟﻤﺠﺘﻤﻊﺍﻟﻤﺪﻧﻲﻭﺍﻟﻤﻨﻈﻤﺎﺕﻏﻴﺮﺍﻟﺤﻜﻮﻣﻴﺔﻓﻲﺍﻟﺤﻮﺍﺭﻋﻦﺑﻨﺎﺀﺍﻟﺴﻠ؝ﻡ
שיתוף אירגוני החברה האזרחית בתהליכים לקידום שלום
4
0.29
94%
Create a globalized coalition to assist Gaza’s reconstruction
ﺗﺤﺎﻟﻒﻋﺎﻟﻤﻲﻟﻠﻤﺴﺎﻋﺪﺓﻓﻲﺇﻋﺎﺩﺓﺇﻋﻤﺎﺭﻏﺰﺓ
יצירת קואליציה רב לאומית לשיקום רצועת עזה
5
0.31
90%
(b) Collective statements addressed to residents in the region.
Collective statements
IRV rank
Dowdall score
Max-min agreement
We all must condemn violence and promote human dignity
ﻋﻠﻴﻨﺎﺟﻤﻴﻌﺎﺃﻥﻧﺪﻳﻦﺍﻟﻌﻨﻒﻭﺃﻥﻧﻌﺰﺯﺍﻟﻜﺮﺍﻣﺔﺍﻟﺈﻧﺴﺎﻧﻴﺔ
עלינו לשלול כל צורה של אלימות ולקדם אנושיות וכבוד האדם
1
0.50
93%
We must all demand the end of occupation and settlement expansion
ﻋﻠﻴﻨﺎﺟﻤﻴﻌﺎﺃﻥﻧﻄﺎﻟﺐﺑﺈﻧﻬﺎﺀﺍﻟﺎﺣﺘﻠ؝ﻝﻭﺍﻟﺘﻮﺳﻊﺍﻟﺎﺳﺘﻴﻄﺎﻧﻲ
עלינו לקרוא לסיום הכיבוש ולהפסקת הרחבת ההתנחלויות
2
0.49
92%
We must pressure governments to end hostilities and negotiate peace
.ﻳﺠﺐﻋﻠﻴﻨﺎﺃﻥﻧﻀﻐﻂﻋﻠﻰﺍﻟﺤﻜﻮﻣﺎﺕﻟﺈﻧﻬﺎﺀﺟﻤﻴﻊﺍﻟﺄﻋﻤﺎﻝﺍﻟﻌﺪﺍﺋﻴﺔﻭﺍﻟﺘﻔﺎﻭﺽﻟﻠﻮﺻﻮﻝﺍﻟﻰﺳﻠ؝ﻡ
עלינו ללחוץ על ההנהגות לסיים את האלימות ולחתור למשא ומתן מדיני לשלום
3
0.47
84%
We all must recognize the right of self-determination for both peoples
ﺍﻟﺎﻋﺘﺮﺍﻑﺑﺤﻖﺗﻘﺮﻳﺮﺍﻟﻤﺼﻴﺮﻟﻠﺸﻌﺒﻴﻦ
עלינו להכיר בזכות להגדרה עצמית של שני העמים
4
0.43
96%
We must create a regional coalition against violence and extremism
ﻳﺠﺐﻋﻠﻴﻨﺎﺇﻧﺸﺎﺀﺗﺤﺎﻟﻒﺇﻗﻠﻴﻤﻲﺿﺪﺍﻟﻌﻨﻒﻭﺍﻟﺘﻄﺮﻑ
עלינו להקים קואליציה אזורית למאבק באלימות ובקיצוניות
5
0.20
92%
A key challenge of this work was figuring out how to reap these
benefits of using AI without sacrificing trust and legitimacy due to
real/perceived issues with AI. Vote prediction is imperfect, LLMs
can hallucinate, and machine translation is sometimes just wrong.
Such imperfections hurt trust and legitimacy in a system that uses
AI. However, rather than ensuring all AI used was unbiased, and
error-free, our approach was designed under the assumption that
all AI used would be imperfect. The process was formulated to
accommodate AI imperfection by incorporating expert humans in
the loop, being transparent with participants (Appendix C.1), and
using AI-free final votes to validate all points of common ground.
In particular, all outputs of AI/LLMs were verified with humans-
in-the-loop, with the exception of real-time machine translation
during the dialogues for which we had the experts review sample
translations in advance to choose the most accurate translation
method available. AI was only used for tasks where it was faster
or cheaper to have the AI do it and then have humans check the
outputs, than to have the humans do it themselves.

--- Page 11 ---

Using Collective Dialogues and AI to Find Common Ground Between Israeli and Palestinian Peacebuilders
FAccT ’25, June 23–26, 2025, Athens, Greece
6
CONCLUSION
In this case study, we documented a recursive deliberative pro-
cess in which we used online collective dialogues, bridging-based
ranking, and LLMs to surface common ground between Israeli and
Palestinian peacebuilders. While prior work has shown the effec-
tiveness of integrating similar techniques in low-stakes settings,
this work is an “existence proof” that (i) these technologies can be
used within high-stakes conflict settings while maintaining trust;
(ii) that a scalable method can successfully bridge divides among
distrustful groups amid active conflict; and (iii) that such processes
can be made equitable despite significant structural asymmetries
between participants.

--- Page 12 ---

FAccT ’25, June 23–26, 2025, Athens, Greece
Konya et al.
ACKNOWLEDGMENTS
We first thank the team at ALLMEP that worked extremely hard to
make this effort happen: Doubi Schwartz, Wasim Almasri, Nivine
Sandouka, Brian Reeves, Nick Acosta, Kari Reid, Dr. Natali Levin-
Schwartz, John Lyndon, and Avi Meyerstein; Avi and John for their
leadership and commitment to advancing this initiative during
challenging times. We thank Hope Schroeder, Manuel Wuthrich,
Karmel Salah, Jay Baxter, Colin Megill, and Colin Irwin for helpful
conversations and input. Finally, we thank Jake Weiner, Ivy Che-
ung, Amanda Yonce, Margo Flewelling, Jennifer Gong, and Emmet
Hennessy for rapidly developing the multi-lingual capability on
Remesh that enabled timely execution of the joint phase.
Luke Thorburn was supported in part by UK Research and In-
novation [grant number EP/S023356/1], in the UKRI Centre for
Doctoral Training in Safe and Trusted Artificial Intelligence (safe-
andtrustedai.org), King’s College London.
REFERENCES
[1] Daanish Masood Alavi, Martin Wählisch, Colin Irwin, and Andrew Konya. 2022.
Using Artificial Intelligence for Peacebuilding. Journal of Peacebuilding & De-
velopment 17, 2 (2022), 239–243.
https://doi.org/10.1177/15423166221102757
arXiv:https://doi.org/10.1177/15423166221102757
[2] Lisa P Argyle, Christopher A Bail, Ethan C Busby, Joshua R Gubler, Thomas Howe,
Christopher Rytting, Taylor Sorensen, and David Wingate. 2023. Leveraging
AI for Democratic Discourse: Chat Interventions Can Improve Online Political
Conversations at Scale. Proceedings of the National Academy of Sciences 120, 41
(2023), e2311627120.
[3] Michiel Bakker, Martin Chadwick, Hannah Sheahan, Michael Tessler, Lucy
Campbell-Gillingham, Jan Balaguer, Nat McAleese, Amelia Glaese, John
Aslanides, Matt Botvinick, et al. 2022. Fine-tuning Language Models to Find
Agreement Among Humans with Diverse Preferences. Advances in Neural Infor-
mation Processing Systems 35 (2022), 38176–38189.
[4] Jordan Bilich, Michael Varga, Daanish Masood, and Andrew Konya. 2023. Faster
Peace via Inclusivity: An Efficient Paradigm to Understand Populations in Conflict
Zones. arXiv:2311.00816 [cs.CY] https://arxiv.org/abs/2311.00816
[5] Felix Brandt, Vincent Conitzer, Ulle Endriss, Jérôme Lang, and Ariel D. Procaccia.
2016. Handbook of Computational Social Choice (1st ed.). Cambridge University
Press, USA.
[6] Gecia Bravo-Hermsdorff, Robert Busa-Fekete, Lee M. Gunderson, Andrés Munõz
Medina, and Umar Syed. 2022. Statistical Anonymity: Quantifying Reidenti-
fication Risks without Reidentifying Users.
arXiv:2201.12306 [cs.DS] https:
//arxiv.org/abs/2201.12306
[7] British Columbia Citizens’ Assembly on Electoral Reform. 2004. Making Ev-
ery Vote Count: The Case for Electoral Reform in British Columbia.
http:
//citizensassembly.arts.ubc.ca/resources/final_report.pdf
[8] BürgerBegehren Klimaschutz. 2020. Climate Assembly Adopts Recommenda-
tions. Press Release, BürgerRat Democracy. https://www.buergerrat.de/en/news/
climate-assembly-adopts-recommendations/
[9] Jason W. Burton, Ezequiel Lopez-Lopez, Shahar Hechtlinger, Zoe Rahwan, Samuel
Aeschbach, Michiel A. Bakker, Joshua A. Becker, Aleks Berditchevskaia, Julian
Berger, Levin Brinkmann, Lucie Flek, Stefan M. Herzog, Saffron Huang, Sayash
Kapoor, Arvind Narayanan, Anne-Marie Nussberger, Taha Yasseri, Pietro Nickl,
Abdullah Almaatouq, Ulrike Hahn, Ralf H. J. M. Kurvers, Susan Leavy, Iyad
Rahwan, Divya Siddarth, Alice Siu, Anita W. Woolley, Dirk U. Wulff, and Ralph
Hertwig. 2024. How large language models can reshape collective intelligence.
Nature Human Behaviour 8, 9 (01 Sep 2024), 1643–1655. https://doi.org/10.1038/
s41562-024-01959-9
[10] Soham De, Jay Baxter, Michiel Bakker, and Martin Saveski. 2025. Supernotes:
Driving Consensus in Crowd-Sourced Fact-Checking. In Proceedings of the ACM
Web Conference 2025 (WWW ’25) (Sydney, NSW, Australia). ACM, New York, NY,
USA, 11. https://doi.org/10.1145/3696410.3714934
[11] Kara N. Dillard. 2013. Envisioning the Role of Facilitation in Public Deliberation.
Journal of Applied Communication Research 41, 3 (2013), 217–235. https://doi.
org/10.1080/00909882.2013.826813
[12] David Farrell, Clodagh Harris, and Jane Suiter. 2015.
The Irish Vote for
Marriage Equality Started at a Constitutional Convention. The Washington
Post (Monkey Cage) (2015). https://www.washingtonpost.com/news/monkey-
cage/wp/2015/06/05/the-irish-vote-for-marriage-equality-started-at-a-
constitutional-convention/
[13] Sara Fish, Paul Gölz, David C. Parkes, Ariel D. Procaccia, Gili Rusak, Itai Shapira,
and Manuel Wüthrich. 2025. Generative Social Choice. arXiv:2309.01291 [cs.GT]
https://arxiv.org/abs/2309.01291
[14] Jon Fraenkel and Bernard Grofman. 2014. The Borda Count and its Real-World
Alternatives: Comparing Scoring Rules in Nauru and Slovenia. Australian Journal
of Political Science 49, 2 (2014), 186–205.
[15] Josh Gabbatiss. 2020. Q&A: How the ‘Climate Assembly’ Says the UK Should
Reach Net-Zero. Carbon Brief (2020). https://www.carbonbrief.org/qa-how-the-
climate-assembly-says-the-uk-should-reach-net-zero/
[16] Imelda Gaffney. 2022. Impartiality and Neutrality in Mediation. Journal of
Mediation and Applied Conflict Analysis 8, 1 (2022), 59–71.
[17] Global Assembly. 2022.
Report of the 2021 Global Assembly on the Cli-
mate and Ecological Crisis. https://globalassembly.org/resources/downloads/
GlobalAssembly2021-FullReport.pdf
[18] Beth Goldberg, Diana Acosta-Navas, Michiel Bakker, Ian Beacock, Matt Botvinick,
Prateek Buch, Renée DiResta, Nandika Donthi, Nathanael Fast, Ravi Iyer, Zaria
Jalan, Andrew Konya, Grace Kwak Danciu, Hélène Landemore, Alice Marwick,
Carl Miller, Aviv Ovadya, Emily Saltz, Lisa Schirch, Dalit Shalom, Divya Siddarth,
Felix Sieker, Christopher Small, Jonathan Stray, Audrey Tang, Michael Henry
Tessler, and Amy Zhang. 2024. AI and the Future of Digital Public Squares.
arXiv:2412.09988 [cs.CY] https://arxiv.org/abs/2412.09988
[19] Involve. 2018.
The Citizens’ Assembly Behind The Irish Abortion Referen-
dum. https://involve.org.uk/news-opinion/opinion/citizens-assembly-behind-
irish-abortion-referendum
[20] Andrew Konya, Aviv Ovadya, Kevin Feng, Quan Ze Chen, Lisa Schirch, Colin
Irwin, and Amy X. Zhang. 2024. Chain of Alignment: Integrating Public Will with
Expert Intelligence for Language Model Alignment. arXiv:2411.10534 [cs.HC]
https://arxiv.org/abs/2411.10534
[21] Andrew Konya, Yeping Lina Qiu, Michael P Varga, and Aviv Ovadya. 2022. Elici-
tation Inference Optimization for Multi-Principal-Agent Alignment. In NeurIPS
2022 Foundation Models for Decision Making Workshop. https://openreview.net/
forum?id=tkxnRPkb_H
[22] Andrew Konya, Lisa Schirch, Colin Irwin, and Aviv Ovadya. 2023. Democratic
Policy Development using Collective Dialogues and AI. arXiv:2311.02242 [cs.CY]
https://arxiv.org/abs/2311.02242
[23] Svenn Lindskold. 1978. Trust Development, the GRIT Proposal, and the Effects
of Conciliatory Acts on Conflict and Cooperation. Psychological Bulletin 85, 4
(1978), 772.
[24] Daanish Masood Alavi, Martin Wählisch, Colin Irwin, and Andrew Konya. 2022.
Using Artificial Intelligence for Peacebuilding. Journal of Peacebuilding & Devel-
opment 17, 2 (2022), 239–243.
[25] Joseph Montville. 1991. Track Two Diplomacy: The Arrow and the Olive Branch.
In The Psychodynamics of International Relations, Vamik D. Volkan, Demetrios A.
Julius, and Joseph V. Montville (Eds.). Vol. 2. Lexington Books, Lexington, MA,
161–175.
[26] Christopher W. Moore. 2014. The Mediation Process: Practical Strategies for Re-
solving Conflict. Jossey-Bass, San Francisco, CA, USA.
[27] Aviv Ovadya. 2022. Bridging-Based Ranking. Technical Report. Belfer Center
for Science and International Affairs, Harvard Kennedy School. https://www.
belfercenter.org/publication/bridging-based-ranking
[28] Aviv Ovadya. 2023.
’Generative CI’ through Collective Response Systems.
arXiv:2302.00672 [cs.HC] https://arxiv.org/abs/2302.00672
[29] Aviv Ovadya and Luke Thorburn. 2023. Bridging Systems: Open Problems for Coun-
tering Destructive Divisiveness across Ranking, Recommenders, and Governance.
Technical Report. Knight First Amendment Institute. https://knightcolumbia.
org/content/bridging-systems
[30] Lisa Schirch and David Campt. 2015. The Little Book of Dialogue for Difficult
Subjects: A Practical, Hands-On Guide. Simon and Schuster, New York, USA.
[31] Christopher Small. 2015. Commit 8394f1f. https://github.com/pol-is/polisMath/
commit/8394f1fa75fd64d0f9eee9335f74d2fa0731f882
[32] Christopher Small, Michael Bjorkegren, Timo Erkkilä, Lynette Shaw, and Colin
Megill. 2021. Polis: Scaling Deliberation by Mapping High Dimensional Opinion
Spaces. Recerca: Revista de Pensament i Anàlisi 26, 2 (2021).
[33] Christopher T. Small, Ivan Vendrov, Esin Durmus, Hadjar Homaei, Eliza-
beth Barry, Julien Cornebise, Ted Suzman, Deep Ganguli, and Colin Megill.
2023. Opportunities and Risks of LLMs for Scalable Deliberation with Polis.
arXiv:2306.11932 [cs.SI] https://arxiv.org/abs/2306.11932
[34] Michael Henry Tessler, Michiel A Bakker, Daniel Jarrett, Hannah Sheahan, Mar-
tin J Chadwick, Raphael Koster, Georgina Evans, Lucy Campbell-Gillingham,
Tantum Collins, David C Parkes, et al. 2024. AI Can Help Humans Find Common
Ground in Democratic Deliberation. Science 386, 6719 (2024), eadq2852.
[35] United Nations. 2008.
United Nations Peacekeeping Operations: Principles
and Guidelines. , 31–35 pages. https://peacekeeping.un.org/sites/default/files/
capstone_eng_0.pdf
[36] United Nations DPPA Innovation. 2022. Project: Berlanti. https://futuringpeace.
org/project/berlanti
[37] United Nations DPPA Innovation. 2022. Project: Digital Dialogues Bolivia. https:
//futuringpeace.org/project/project-digital-dialogues-haiti
[38] United Nations DPPA Innovation. 2022. Project: Digital Dialogues Haiti. https:
//futuringpeace.org/project/project-digital-dialogues-haiti

--- Page 13 ---

Using Collective Dialogues and AI to Find Common Ground Between Israeli and Palestinian Peacebuilders
FAccT ’25, June 23–26, 2025, Athens, Greece
[39] United Nations DPPA Innovation. 2022. Project: Digital Dialogues Iraq. https:
//futuringpeace.org/project/project-digital-dialogues-iraq
[40] United Nations DPPA Innovation. 2022. Project: Digital Dialogues Lebanon.
https://futuringpeace.org/project/project-digital-dialogues-lebanon
[41] United Nations DPPA Innovation. 2022. Project: Digital Dialogues Libya. https:
//futuringpeace.org/project/project-digital-dialogues-libya
[42] United Nations DPPA Innovation. 2022. Project: Digital Dialogues Yemen. https:
//futuringpeace.org/project/project-digital-dialogues-yemen
[43] United Nations DPPA Innovation. 2022. Project: Sergio’s Conversa.
https:
//futuringpeace.org/project/sergios-conversa
[44] Tim van Gelder. 2012. Cultivating Deliberation for Democracy. Journal of
Deliberative Democracy 8, 1 (2012). https://doi.org/10.16997/jdd.134
[45] Stefan Wojcik, Sophie Hilgard, Nick Judd, Delia Mocanu, Stephen Ragain,
M. B. Fallin Hunzaker, Keith Coleman, and Jay Baxter. 2022. Birdwatch: Crowd
Wisdom and Bridging Algorithms can Inform Understanding and Reduce the
Spread of Misinformation. arXiv:2210.15723 [cs.SI] https://arxiv.org/abs/2210.
15723

--- Page 14 ---

FAccT ’25, June 23–26, 2025, Athens, Greece
Konya et al.
A
JOINT LETTER
“We write as a united body of Israeli and Palestinian peacebuilders,
compelled by the urgency of our shared pain and galvanized with the
hope we still hold for the future. We call for the following:
• An immediate ceasefire and release of all hostages
• The creation of an international fund to build the foundations
for a comprehensive long-term solution
• The establishment of a globalized coalition to assist Gaza’s
reconstruction
• The inclusion of civil society and NGOs in all peacebuilding
and diplomatic discussions
• The recognition of both sides’ trauma
Acknowledging the trauma and pain experienced by both sides
is essential for the healing of our societies and the achievement of
sustainable peace. Help us break the cycle of violence so the next
generation may flourish. The world watches, and history will judge.
Now is the time to act.”
B
FURTHER BACKGROUND
B.1
Collective Dialogue Dynamics
During a live collective dialogue process, all participation is simul-
taneous and each collective response process takes a few minutes.
When each response process completes, each participant sees the
fraction of all participants agreeing with their response along with
a representative subset of responses from the group. The moder-
ator sees live results which they can use to decide if they need to
pivot from the pre-programmed discussion guide to ask additional
questions on an issue. After a live dialogue is complete it can be
left open for asynchronous participation so those who could not
make the live event can still participate. Collective dialogues can
also be run asynchronously from the start if the logistics of a live
dialogue are not feasible for the situation.
C
FURTHER METHODOLOGICAL DETAILS
C.1
Transparency about the use of AI
In the invitations and public communications, participants were
told “AI” was being used, e.g., “we are using an AI-based tool to hold
a series of large scale ‘collective dialogues’ among Israelis and Pales-
tinians.” F Some participants attended optional office hour/Q&A
calls, in which we discussed how LLMs specifically were being
used.
Most prospective participants responded positively. Some were
skeptical of the use of AI and wanted to understand the details
of how it was being used further. For those, we held a few ‘office
hour’ sessions where we walked anyone interested or concerned
through the details of how we used AI. Most questions were around
elicitation inference & how well LLMs could handle Hebrew/Arabic.
We typically walked them through the overall process, explained the
micro-experiments for the LLM pipeline related to Hebrew/Arabic,
and shared links to the elicitation inference papers.
It’s unclear exactly how awareness of the use of LLMs shaped
the consensus-building process, but we think that talking to a “com-
puter” made it easier for people to express themselves freely. For
some, LLMs were seen as more impartial. For others, there was
persistent skepticism.
D
FURTHER DISCUSSION
D.1
Ethical Considerations
Undertaking this work this in the context of active conflict raises
many valid ethical concerns. We summarize some of those we con-
sidered below, along with steps taken to address them. In general,
when making decisions about delaying or potentially not running
the process, we weighed the potential downsides and upsides of
moving forward against the “null hypothesis” of the status quo.
• Backfire: There was a risk that conducting the cross-border
dialogue in the joint phase could backfire in various ways
(e.g., if dialogue broke down), and inflame the division this
effort sought to bridge. We mitigated this risk by starting
with a uninational phase designed to help build trust and set
the conditions for a productive cross-border dialogue.
• Bias: Any bias in the process could harm the legitimacy of
the results it produced. There are many ways bias might
have entered the process, some of which we list below, along
with the steps taken to mitigate them.
– The use of imperfect AI and ML algorithms throughout the
process risks injecting errors or biases that misrepresent
participants. We mitigated this risk via humans in the loop:
experts reviewed and refined all outputs downstream of
AI/ML, and final votes among participants were conducted
to validate all points of common ground. To minimize bias
from errors in machine translation or LLM processing, we
made LLM pipeline choices using micro experiments that
enabled native Hebrew and Palestinian Arabic speakers
decide what would be used for their language.
– There was a risk that the human experts “in the loop” could
themselves induce unfair bias in the process or results. We
mitigated this risk by having joint reviews involving both
Israelis and Palestinian reviewers at the key points in
the process where such biases could be introduced. This
included not just process decisions made by the ALLMEP
team, but decisions made by the largely US and UK-based
team that performed the technical data processing steps
in the process. We ensured that there was both Israeli and
Palestinian representation on this technical team.
– For the process to be fair, each “side” should have equal
influence on the results. But it would be anti-inclusive to
not allow certain participants to join in order to ensure
equal numbers of participants from all sides. We used equal
power metrics to ensure each side had equal influence
without requiring equal numbers of participants.
– To avoid participant self-selection bias on the basis of
language or bias due to language difficulties during the
process, the approach was designed so that all participants
could participate in their primary language.
• Malicious use: There is a risk that results from the process
could be used maliciously to disrupt ongoing peacebuilding
efforts; i.e., by sewing further division. We thus only share
a limited subset of results that manifest common ground
or are directly relevant to understanding the approach. We
do not share any side-specific quantitative results, and only
include overall metrics that are equal power.

--- Page 15 ---

Using Collective Dialogues and AI to Find Common Ground Between Israeli and Palestinian Peacebuilders
FAccT ’25, June 23–26, 2025, Athens, Greece
• Anonymity: Sharing politically sensitive opinions can po-
tentially present a risk to participants if their identify is
known; and force a trade-off between honesty and safety.
We thus choose to support all participation to take place
anonymously.
D.2
Limitations
Several limitations of this case study deserve mention:
• Lack of controlled experimentation: Due to the real-
world and time-sensitive nature of this work, extensive con-
trolled experimentation was not feasible. This limits the
ability to draw strong causal claims or to isolate the impact
of specific methodological components.
• Participant selection bias: The study participants were
self-selected peacebuilders and thus not be representative of
the broader Israeli and Palestinian populations. It remains
unclear if the approach will generalize of to a wider public
who may hold more entrenched or divergent viewpoints.
• Context-specificity: The results are specific to the Israeli-
Palestinian context and may not be directly transferable
to other conflict zones or social divisions, due to unique
political, cultural and historical dynamics.
• Language nuances: While significant efforts were made to
accommodate multiple languages, the use of machine trans-
lation and LLMs could introduce subtle errors and ambigui-
ties. These translations — particularly those of participant-
contributed statements that were voted on during the live
dialogues and were not subject to human review — may not
have always perfectly captured the intended meaning or
cultural nuances of the original statements.
• Technological dependency: The reliance on online collec-
tive dialogue and LLMs tools may introduce a selection bias
based on technological literacy and access. The success of
this type of process is contingent on reliable internet access,
which is not (yet) universally available.
D.3
Future Directions
We see a few key challenges to be addressed in future work:
• Concrete bridging: It is typically easier to find diverse
agreement on anodyne or abstract statements than on state-
ments that are more specific, prescriptive, or concrete. As
a result, bridging techniques based only on agreement sig-
nals may have a natural bias towards anodyne statements,
making it harder to find common ground that is concrete
enough to be useful (for example, as the basis for a peace
agreement). Future work is needed to create automated mea-
sures of statement “concreteness” or “anodyneness” that can,
for example, be combined with bridging metrics to more
effectively identify statements that are both bridging and
concrete.
• Going beyond distillation: AI can be used not just for
distilling information, but for generating novel more ex-
ploratory proposals. Using an iterative deliberation method,
similar to the one proposed by Tessler et. al [34], an LLM
could generate a set of initial collective statements that peo-
ple then critique and refine. This process could explore novel
ideas that emerge through a process of iterative synthesis
and refinement, with a focus on balanced perspectives. These
combined ideas might not individually represent common
ground but, when combined in a balanced way, could reflect
a form of reasoned consensus. Such statements could not be
derived solely from individual statements with high bridging
metrics. It would be essential that the resulting statements
from this kind of generative process still be validated with a
final vote of agreement among human participants to ensure
that they actually represent common ground.
• Legitimate representation: How do you ensure results are
representative of a general population? Ideally, the group of
participants would statistically representative of the general
population and sampled in a way that had both scientific
and procedural legitimacy. However, in practice, obtaining
a representative sample for online cross-border dialogues
in this region is challenging due to structural, political, and
logistical barriers. Restrictions on movement, lack of digi-
tal accessibility in certain areas, surveillance concerns, and
varying levels of trust in international initiatives all affect
willingness and ability to participate. Further, the type of
nationally representative online panel that might otherwise
serve as a starting point for this type of effort do not exist for
areas like the West Bank and Gaza. While establishing such
an online panel would be ideal, one short-term work around
may be to recruit a diverse (but not statistically representa-
tive) set of participants for the online collective dialogues,
then use more traditional computer-assisted telephone in-
terviewing and in-person sampling approaches to obtain
legitimately representative samples for the final vote, includ-
ing marginalized populations like rural communities, refugee
camps, and those with lower access to digital platforms.
E
QUALITATIVE FEEDBACK
E.1
ALLMEP Retrospective
Below are a few specific questions asked to ALLMEP leaders in-
volved in the process. Direct quotes denote their verbatim responses
and content not in quotes is context provided by this paper’s au-
thors.
• Did you find [the process] helpful?
“Yes. At a time when real dialogue felt impossible post October
7th, this process allowed Palestinians and Israelis to engage
without compromising their experiences or red lines.”
• Do you plan to use the process again?
“Absolutely. The ability to engage anonymously and equitably
is critical, especially for Palestinians who face political and
social risks when participating in cross-border work.”
(We are continuing to work with ALLMEP on scaling this
process up to larger and more representative samples of the
public; of which — as of writing this — the first dialogue
cycle has already begun.)
• Were there parts of the process that you were especially
excited about or skeptical of [before it was run]?
“I was mostly excited about the uninational phase. It gave [us]
room to define our priorities before entering joint dialogue,

--- Page 16 ---

FAccT ’25, June 23–26, 2025, Athens, Greece
Konya et al.
which felt empowering and necessary. I was a little skeptical
however whether AI could reflect our political realities.”
Beyond all the trust building aspects discussed throughout
the paper, we note that using the well-known Community
Notes algorithm helped give the process improved face va-
lidity and build trust.
E.2
Participant Feedback
E.2.1
Examples of Positive Feedback.
• “I found it to be very validating and very positive! It gave
me hope”
• “That was an INCREDIBLE experience”
• “I felt that I could share openly, without fear of being judged.
It felt much less complicated than sharing directly with col-
leagues”
• “This was an interesting experience, a lot of self-reflection
regarding our inner motives for this work”
• “I know there is an end goal for this, but seeing each other’s
anonymous thoughts in this way is valuable in and of itself
and perhaps this sort of work could be integrated in various
ways as part of more regular activities. The openness of
anonymity is important.”
E.2.2
Examples of Negative or Ambivalent Feedback.
• “Interesting activity but time for answers was a bit short”
• “Ummm.... I haven’t made up my mind about this technology
yet....”
• “Everything is so fast. It’s hard to think. It was possible to
give a little more time to read and respond. The idea is cool”
• “We need to be able to speak to each other, see each other’s
faces”
• “I am not sure that I was able to express myself completely
or clearly also due to technical limitations of time and the
translation.”

--- Page 17 ---

Using Collective Dialogues and AI to Find Common Ground Between Israeli and Palestinian Peacebuilders
FAccT ’25, June 23–26, 2025, Athens, Greece
F
RECRUITMENT INVITATION
AI PULSE​
Peacebuilding after the War: Using AI to Find a Shared Path Forward 
Many believe that this horrible Gaza war “changed everything.” If so, what does it mean for public attitudes? What will it 
mean for peacebuilding work to build support between societies for peace? As we prepare for the challenges and 
opportunities that lie ahead,  which strategies or messages will be most effective? Where can we find a starting point of 
consensus in this new moment, even after so much trauma?  
ALLMEP has launched a new project to find out, and we need your help. Together with the University of Notre Dame 
and high-tech firm Remesh, we are using an AI-based tool to hold a series of large-scale “collective dialogues” among 
Israelis and Palestinians. We have already completed the first of two cohorts, starting with peacebuilding professionals. In 
coming months we will conduct a second round for a sample of the Israeli and Palestinian general publics, separately. 
But it all starts with you. Getting the most accurate picture requires maximum participation and a diverse audience. The 
minimum commitment is just 2 sessions (30 minutes) and a short survey. Please urge your team members to register 
and participate at the links below. There is no cost for NGOs or participants. 
HOW DOES IT WORK? HOW WILL IT HELP YOU? 
Remesh looks like an online chat and works like a focus group. We each join with a secure, 
anonymous link. Questions appear on the screen, and we each answer in our own words. The 
system then reviews all the answers to find areas where people may agree or disagree. Follow-up 
questions and polls help narrow in on points of dis/agreement. AI allows this process to work at scale 
with thousands of people and predict how different segments of the population would answer. It’s 
confidential, engaging, and empowering. 
The opinions and perspectives that emerge will benefit every NGO: 
●​
Learn what people think about the situation, the conflict, future strategies, political solutions, 
and more. Identify and build upon areas of potential agreement. 
●​
Understand attitudes by segment: in your organization vs. others, among alumni, donors, and 
the wider public; by age, gender, nationality, location, and more. 
●​
Engage and activate alumni so they can be heard, join a large-scale democratic process, and 
feel part of a bigger community. Learn how they feel about this work and what 
messages/ideas might best engage them after such a traumatic period. 
●​
Design programs using lessons about these attitudes and project legitimacy. 
●​
Fine-tune messaging to use language and concepts that resonate. 
●​
Speak to donors based on their perspectives and needs. 
SCHEDULE AND REGISTRATION 
First session: Choose a first session below to participate (all times Jerusalem time) 
➔​ Jewish Israeli uninational session: Monday, April 15 at 15:00 
➔​ Palestinian uninational session: Thursday, May 2 at 16:00 
➔​ Palestinian citizens of Israel uninational session: Thursday, May 16 at 15:00 
Second session: Everyone participates together (you’ll be registered automatically after first session) 
➔​ Joint Israeli Palestinian session:  Wednesday, May 29 at 15:30 (Registration to follow) 

--- Page 18 ---

FAccT ’25, June 23–26, 2025, Athens, Greece
Konya et al.
WHO IS REMESH?  
Remesh is a private company founded in 2014 with the mission to create technology to represent the will of the people 
and amplify their collective voice. Its "deliberative technology" platform helps people engage, exchange ideas, and have a 
dialogue on a massive scale. Its technology has been used by the United Nations to find and build consensus in other 
conflict zones. 
QUESTIONS?  
Please contact 
 at 
. 

--- Page 19 ---

Using Collective Dialogues and AI to Find Common Ground Between Israeli and Palestinian Peacebuilders
FAccT ’25, June 23–26, 2025, Athens, Greece
G
SAMPLE SIZES
Table 4: The tables below record what we know about the number of participants in each dialogue cycle. Columns “CDa”, “CDb”,
“CDc” respectively contain (a) the number who joined the collective dialogue and did demographic onboarding, (b) the number
who simultaneously contributed a statement to the same open-ended prompt, and (c) the number contributed statements and
voted all the way through to the last collective prompt. Columns “Va”, “Vb”, “Vc” respectively contain (a) the number who
joined and did demographic onboarding for the asyncronous vote, (b) the number who additionally voted on all collective
statements in the paper (joint) or on 50% of collective statements (uninational), and (c) voted on all collective statements not
shared in the paper related to internal peacebuilding strategy. Finally, column “MUP” contains the maximum possible number
unique participants of any sort during the dialogue cycle (Va + CDa), and “UEP” contains the best estimate of unique engaged
participants during the dialogue cycle (max(CDb, Vb)).
(a) Dialogue Cycle 1
CDa
CDb
CDc
Va
Vb
Vc
MUP
UEP
Total
74
62
58
76
70
65
150
70
Israeli Jews
72
60
56
73
68
63
145
68
Palestinians
2
2
2
3
2
2
5
2
Palestinians from the West Bank & Gaza
0
0
0
1
0
0
1
0
Palestinian Citizens of Israel
2
2
2
2
2
2
4
2
(b) Dialogue Cycle 2
CDa
CDb
CDc
Va
Vb
Vc
MUP
UEP
Total
32
28
19
14
12
10
46
28
Israeli Jews
0
0
0
0
0
0
0
0
Palestinians
32
28
19
14
12
10
46
28
Palestinians from the West Bank & Gaza
31
28
19
13
11
9
44
28
Palestinian Citizens of Israel
1
0
0
1
1
1
2
1
(c) Dialogue Cycle 3
CDa
CDb
CDc
Va
Vb
Vc
MUP
UEP
Total
14
13
13
10
9
9
24
13
Israeli Jews
0
0
0
0
0
0
0
0
Palestinians
14
13
13
10
9
9
24
13
Palestinians from the West Bank & Gaza
2
2
2
2
2
2
4
2
Palestinian Citizens of Israel
12
11
11
8
7
7
20
11
(d) Dialogue Cycle 4
CDa
CDb
CDc
Va
Vb
Vc
MUP
UEP
Total
190
138
115
78
71
66
268
138
Israeli Jews
140
109
92
56
50
46
196
109
Palestinians
50
29
23
22
21
20
72
29
Palestinians from the West Bank & Gaza
29
17
13
14
14
13
43
17
Palestinian Citizens of Israel
21
12
10
8
7
7
29
12

--- Page 20 ---

FAccT ’25, June 23–26, 2025, Athens, Greece
Konya et al.
H
PROMPTS
H.1
Used for Dialogue Cycle 1 in Hebrew
Prompt 1: Summarize unique ideas
.<participant prompt>המשתתפים במחקר נשאלו
:אלו התגובות שלהם
<statements>
קצר, סנתז וסכם את כל הרעיונות. הייחודיים בתגובות אלה לנקודות קצרות מאוד
Prompt 2a: Generate collective statements
.<participant prompt>המשתתפים במחקר נשאלו
:אלו התגובות שלהם
<statements>
:הרעיונות העיקריים מהתגובות האלה הם
<unique ideas>
’אנו מגדירים ’תוצאה’ להיות תוצאה קונקרטית ספציפית. איננו מחשיבים גישות ספציפיות להשגת ’תוצאה’ כחלק מה’תוצאה
.עצמה
’סנתז רשימה של ה’תוצאות’ הייחודיות הקיימות ברעיונות העיקריים המסוכמים לעיל. אל תחזור על שום רעיון. על ה’תוצאות
.להיות קצרות
נפלאה לריצה יוצא המשתמש-
באזור מתמשכים וביטחון שלום יש-
ותקווה אהבה ומלא בטוח אדם כל-
בשני אחד פוגעים בעולם אנשים פחות-

--- Page 21 ---

Using Collective Dialogues and AI to Find Common Ground Between Israeli and Palestinian Peacebuilders
FAccT ’25, June 23–26, 2025, Athens, Greece
Prompt 2b: Generate collective statements
.<participant prompt>המשתתפים במחקר נשאלו
:אלו התגובות שלהם
<statements>
:הרעיונות העיקריים מהתגובות האלה הם
<unique ideas>
אנו מגדירים ’ערך’ כמאפיין דאונטילוגי שיכול לבוא לידי ביטוי בהתנהגות, ללא קשר לתוצאה של התנהגות
שיפוט: התנהגותו אינה מרמזת על שיפוט-זו. איננו מחשיבים התנהגות ספציפית כ’ערך’. לדוגמה, ”אי
.’ערכי לגבי רגשות או חוויה של המשתמש” הוא ’ערך’, אבל ”לא אומרים ’אני שופט אותך’” אינו ’ערך
.כתוב רשימה של ה’ערכים’ הייחודיים הקיימים ברעיונות המרכזיים מתוך התגובות שסוכמו לעיל
:הנה כמה ’ערכים’ לדוגמה
כבוד: כיבוד רגשותיו וחוויותיו של המשתמש מבלי- .אמפתיה: הפגנת הבנה וחמלה כדי לגרום למשתמש להרגיש שנשמע ונתמך
- .אי שיפוטיות: מתן תמיכה ללא ביקורת או משוא פנים כדי ליצור מרחב בטוח למשתמש להביע את עצמו- .למזער את כאבו
.אל תעתיק את ה’ערכים’ לדוגמה שלמעלה מילה במילה. בנה אותם על סמך התגובות והרעיונות המרכזיים המסוכמים לעיל
’סנתז רשימה של ה’תוצאות’ הייחודיות הקיימות ברעיונות העיקריים המסוכמים לעיל. אל תחזור על שום רעיון. על ה’תוצאות
.להיות קצרות
נפלאה לריצה יוצא המשתמש-
באזור מתמשכים וביטחון שלום יש-
ותקווה אהבה ומלא בטוח אדם כל-
בשני אחד פוגעים בעולם אנשים פחות-
H.2
Used for Dialogue Cycles 2 and 3 in Palestinian Arabic
Prompt 3: Summarize unique ideas
.<participant prompt> ܾୖ୒ﺍﺭ܋൹ඔࢻࣖﺭﺍݿ۰ቆቕݿޝﺍ
ܾዛኤ؇ً؇༥۱؇ﻱﺇ
<statements>
ଫଃٺ܋ۊٺཡ๤،ݬ٭ؐﻭﺍۊٺཡ๤၍႟ﺍ৑৙ڣၽႤﺭﺍܳڰݠࢴࣖﺓ ً؇৑৕༥؇ً؇ﺕ༟ॻআނၽ႟ َگ؇ﻁﺭཬ྘ފ٭۰ ڢݱଃଫﺓ

--- Page 22 ---

FAccT ’25, June 23–26, 2025, Athens, Greece
Konya et al.
Prompt 4a: Generate collective statements
.<participant prompt> ܾୖ୒݁ލ؇ﺭ܋൹ඔࢻࣖﺭﺍݿ۰ቆቕݿޝﺍ
ܾዛኤ؇ً؇༥۱؇ﻱﺇ
<statements>
ﺍ৑৙ڣၽႤﺭﺍෂීཬ྘ފ٭۰݆݁ ۱؇ﻱﺍ৑৕༥؇ً؇ﺕ
<unique ideas>
؇ዝཏڰَ '۰༶٭ྥٷܳොڎﺩﺓﻭﻭﺍෘො۰.݁؇ಸ਍أٺଊଫﺍܳޚݠﻕﺍ௫௯௱ڎﺩﺓܳٺۜگ٭ݑ 'ﺍܳٷྥ٭༶۰'ජඹﺀ݆݁ 'ﺍ੼۰༶٭ྥཹﺍۋٷ؇ಸ਍أݠﻑ 'ﺍܳٷྥ٭༶۰' ّܝިﻥ
ݬ٭ؐ ڢ؇୴ஓ۰ ًـ 'ﺍܳٷٺ؇຀༇'ﺍܳڰݠࢴࣖﺓﺍዧፇঌ݁ިۏިﺩﺓ ً؇৑৙ڣၽႤﺭﺍෂීཬ྘ފ٭۰ﺍ௫௯௰ٺཡ๤ﺓ ڣިﻕ.৑৖ ّأ٭ڎﺃﻱ ڣଲ୍ﺓ.༠ܹዀዛ؇ ڢݱଃଫﺓ
༇຀؇ٺٷይዧ' ᄭᄥټ݁ሃሒނިل۰ﺃ
۰أفﺍ৊ৎފٺ༱ڎﻡ ًଃଫﻭﺡຬ෠ݠﻱ ًޚݠلگ۰ﺭﺍ-
۰گޚٷৎ৊؇ًلܝިﻥᇭሒݿఃఈﻡﺩﺍሶቕﻭﺃ݁؇ﻥ-
ܭ݁၍႟ﺇ૙૭؇ﻥ ًܝިﻥﺁ݆݁ﻭܹ݁٭؇ﻥ ۋصﻭﺃ-
ݥأً༟ڎﺩﺃڢܭ݆݁ﺍܳٷ؇ﺱಸਃ؊ﺫﻭﺍ-
Prompt 4b: Generate collective statements
.<participant prompt> ܾୖ୒݁ލ؇ﺭ܋൹ඔࢻࣖﺭﺍݿ۰ቆቕݿޝﺍ
ܾዛኤ؇ً؇༥۱؇ﻱﺇ
<statements>
ﺍ৑৙ڣၽႤﺭﺍෂීཬ྘ފ٭۰݆݁ ۱؇ﻱﺍ৑৕༥؇ً؇ﺕ
<unique ideas>
۰༶٭ྥཹ݆؜ ݠޙٷܳﺍۋٷ؇ಸ਍أݠﻑ 'ﺍܳگ٭݄۰' ّܝިﻥݬڰ۰ﺩلި಻ਐިܳިۏ٭۰୷ஓܝ݆ ّأܝཏዝ؇ﺍܳފߺࠊﻙ، ً؞ݥﺍ
ુળ༡আॻ༟۱؇ܳފߺࠊﻙ.݁؇ಸ਍أٺଊଫݿߺࠊﻙ݁أ൹ඔ لܝިﻥ 'ڢ٭݄۰'.݁ټఃఈ ً"༟ڎﻡﺍࠍ੆ળુ:ݿߺࠊﻙﺍܳލۛݧ݁؇ࢻࣖﻝ
'۰݄٭ڢ' ሒሃ؇݁"'۹٭ܹ༟ુળොຳ؇َڢ٭݄޶ ؜݆݁ލ؇؜ਵﺃﻭູ෠؇ﺭﺏﺍ৑৚ඝරઊદ"ሃሒ 'ڢ٭݄۰',ืྵ "݁؇༡ڎﺍ ًگިﻝ 'ﺃ
ﺍ܋ٺص ڢ؇୴ஓ۰ ًـ 'ﺍܳگࡗࡲ'ﺍܳڰݠࢴࣖﺓﺍዧፇঌ݁ިۏިﺩﺓ ً؇৑৙ڣၽႤﺭﺍෂීཬ྘ފ٭۰݆݁ﺍ৑৕༥؇ً؇ﺕﺍ௫௯௰ٺཡ๤ﺓ ڣިﻕ
'ࡲࡗگይዧ' ᄭᄥټ݁ሃሒނިل۰ﺃ
ﺍܳٺأ؇ޗژ:ﺇޖ۳؇ﺭﺍܳڰ۳ܾﻭﺍෂීᅵᆇ۰ܳ྘ލأݠﺍ৊ৎފٺ༱ڎﻡ ً؊َ۬݁ފ݄ިﻉﻭ݁ڎ؜ިﻡ-
ܾዛኤ؇༟ﺍ৑৖༡ଐଫﺍﻡ: ّگڎߌߵ݁ލ؇؜ਵﻭູ෠؇ﺭﺏﺍ৊ৎފٺ༱ڎﻡࢻࣖﻭﻥﺍܳٺگܹ٭ܭ݆݁ﺃ৊ৎ۳ܾﺃﻭཛྷ๤ﺍ-
۬ފڰَ ݆؜ ؇ዛዀڣ ଫଊأل༟ڎﻡﺍࠍ੆ળુ: ّگڎሹቕﺍᄟᄴ؜ܾࢻࣖﻭﻥﺍ಻ਐگ؇ﺩﺃﻭູො᛻ଃ଩ࠍ੅੩੯݁ފ؇༡۰ﺁ݁ٷ۰ዧጻగފٺ༱ڎﻡ-

--- Page 23 ---

Using Collective Dialogues and AI to Find Common Ground Between Israeli and Palestinian Peacebuilders
FAccT ’25, June 23–26, 2025, Athens, Greece
H.3
Used for Dialogue Cycle 4 in Palestinian Arabic, Hebrew, and English
Prompt 5: Summarize unique ideas
Participants in a research study were asked <participant prompt>.
These are their responses:
<statements>
Compress, synthesize, and summarize all of the unique ideas within these responses into very short bullet
points.
Provide each bullet point in English, Palestinian Arabic, and Hebrew like this:
- (english) this is an english bullet point. (arabic) .۰ل଩ଃܹ෠ຶ۱ڍﻩ َگޚ۰ﺇ(hebrew) .זה נקודת תבליט באנגלית
Prompt 6: Generate collective statements
Participants in a research study were asked <participant prompt>.
These are their RESPONSES:
<statements>
The MAIN IDEAS from these responses are:
<unique ideas>
Synthesize a list statements manifesting the MAIN IDEAS summarized above. DO NOT REPEAT ANY
IDEAS. Keep them consise but not vauge and express them in voice and tone similar to the RESPONSES.
Provide each statement in English, Palestinian Arabic, and Hebrew like this:
- (english) this is an english bullet point. (arabic) .۰ل଩ଃܹ෠ຶ۱ڍﻩ َگޚ۰ﺇ(hebrew) .זה נקודת תבליט באנגלית

```
