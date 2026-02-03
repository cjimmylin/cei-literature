---
title: "Case Law Grounding - PDF Extract"
source_pdf: "2023-Chen-Case Law Grounding.pdf"
pages: 13
extracted_at: "2026-01-24T17:05:12.831532"
---

# PDF Extract: Case Law Grounding

**Source PDF:** 2023-Chen-Case Law Grounding.pdf
**Total Pages:** 13

---

## Content

```
--- Page 1 ---

Case Law Grounding: Using Precedents to Align Decision-Making
for Humans and AI
Quan Ze Chen
cqz@cs.washington.edu
University of Washington
Seattle, WA, USA
Amy X. Zhang
axz@cs.washington.edu
University of Washington
Seattle, WA, USA
ABSTRACT
From moderating content within an online community to producing
socially-appropriate generative outputs, decision-making tasks—
conducted by either humans or AI—often depend on subjective or
socially-established criteria. To ensure such decisions are consistent,
prevailing processes primarily make use of high-level rules and
guidelines to ground decisions, similar to applying “constitutions”
in the legal context. However, inconsistencies in specifying and
interpreting constitutional grounding can lead to undesirable and
even incorrect decisions being made. In this work, we introduce
“case law grounding” (CLG)—an approach for grounding subjective
decision-making using past decisions, similar to how precedents
are used in case law. We present how this grounding approach
can be implemented in both human and AI decision-making con-
texts, introducing both a human-led process and a large language
model (LLM) prompting setup. Evaluating with five groups and
communities across two decision-making task domains, we find that
decisions produced with CLG were significantly more accurately
aligned to ground truth in 4 out of 5 groups, achieving a 16.0–23.3
%-points higher accuracy in the human process, and 20.8–32.9 %-
points higher with LLMs. We also examined the impact of different
configurations with the retrieval window size and binding nature
of decisions and find that binding decisions and larger retrieval
windows were beneficial. Finally, we discuss the broader implica-
tions of using CLG to augment existing constitutional grounding
when it comes to aligning human and AI decisions.
CCS CONCEPTS
• Human-centered computing →Collaborative and social
computing.
KEYWORDS
alignment; human judgment; large language models; subjectivity;
consistency; content moderation; policy; decision-making
ACM Reference Format:
Quan Ze Chen and Amy X. Zhang. 2025. Case Law Grounding: Using Prece-
dents to Align Decision-Making for Humans and AI. In Collective Intelligence
Conference (CI 2025), August 4–6, 2025, San Diego, CA, USA. ACM, New York,
NY, USA, 13 pages. https://doi.org/10.1145/3715928.3737487
This work is licensed under a Creative Commons Attribution-ShareAlike 4.0 Interna-
tional License.
CI 2025, August 4–6, 2025, San Diego, CA, USA
© 2025 Copyright held by the owner/author(s).
ACM ISBN 979-8-4007-1489-4/2025/08
https://doi.org/10.1145/3715928.3737487
1
INTRODUCTION
Many technological systems today are entangled in social decision-
making situations. Online spaces for inter-personal communication,
like social media platforms, need to contend with decisions around
how to moderate content in a way that maintains a healthy commu-
nity [22]. General purpose AI assistants, like LLM-backed chatbots,
also need to implicitly make decisions around how to generate
answers that users find appropriate [20, 34, 55]. The scale of these
systems means that getting the decisions wrong can have major
negative consequences for people [25, 61].
Unlike systems that work with more objective determinations,
decisions around social concepts are especially hard because: (1)
decision criteria can vary across different groups and tasks; and
(2) it can be difficult (or even impossible) to formalize these cri-
teria accurately. Efforts to produce high-quality decisions often
involve significant effort, making use of deliberation [30, 58], juries
of community members [17], and even expert panels [38]. Scale
also creates additional challenges, ultimately leading to the need
for automated tools [32, 64] or paid crowd workers [53] to make
final decisions, both of which have introduced inconsistencies and
errors.
In order to improve the consistency of decisions, processes of-
ten first create artifacts to ground the decision-making, the most
common of which takes the form of rules and guidelines (which
we collectively refer to as constitutions). For example, moderators
of communities on social media platforms often create community
guidelines that establish what content is allowable, and how viola-
tions are to be dealt with [9, 10]. Similarly, builders and operators
of AI assistant services often come up with principles [28] that are
then used to synthesize training and fine-tuning examples [3] or
built into system prompts [41]. However, rules and criteria make
use of imprecise language that can leave room for ambiguity [12, 19]
around edge cases, and varied decision-makers often have divergent
interpretations [23]. Is there another way we could better support
these subjective decisions at scale?
Taking inspiration from case law in legal systems, we introduce
case law grounding (CLG), a new approach to grounding decision-
making processes by making use of past decisions (precedents)
rather than rules (constitutions) as guidance. CLG accomplishes this
through 3 steps: (1) case retrieval, where past cases potentially rel-
evant to the current decision are retrieved; (2) precedent selection,
where retrieved precedents are further refined for applicability to
the current decision; and finally (3) decision synthesis, where the
selected precedents and decisions are aggregated and synthesized
into the decision for the new case. To address scaling needs, we
implemented this grounding approach both as a human-led ver-
sion where we support human decision-makers (e.g., members of a
arXiv:2310.07019v4  [cs.HC]  20 Jun 2025

--- Page 2 ---

CI 2025, August 4–6, 2025, San Diego, CA, USA
Quan Ze Chen and Amy X. Zhang
community or group), and as a LLM-prompting version where an
LLM-backed agent is making the decisions.
We evaluated our system on two decision-making tasks: content
moderation, where binary “keep”/“remove” decisions were made on
Reddit comments [48], and toxicity rating, where social media posts
were rated on a 5-point scale [40]. Recruiting participants from 3
Reddit communities (𝑛= 35) and 2 demographically-determined
population groups (𝑛= 60), we evaluated the human-led version
of CLG against a baseline approach that used established constitu-
tions (community guidelines and toxicity annotation guidelines)
to support grounding. Using off-the-shelf LLMs, we also evalu-
ated the LLM-prompting version of CLG against a similar baseline
where LLMs conducted decision-making using the same established
guidelines.
In summary, we make the following contributions:
• We introduce a general framework for supporting decision-
making in subjective and social contexts, case law ground-
ing (CLG), and implement two versions: a human-led pro-
cess, and an LLM-prompting process.
• We evaluate CLG across two decision task domains (span-
ning a total of 5 different group-aligned decision tasks), com-
paring CLG against a more traditional approach that uses
constitutional grounding. We find that:
– In both the human-led or LLM-prompting process, CLG
was able to produce final decisions that more accurately
matched observed ground truth compared to decisions
grounded with constitutions, with statistically significant
improvements observed in 4 out of 5 group decision tasks.
(RQ1)
– For most domains, larger retrieval windows resulted in
higher accuracy, however scaling characteristics varied
across groups. (RQ2a)
– Using binding precedents that directly affect the final deci-
sion is important—with the 4 groups showing statistically
significant improvements only doing so in the binding
version. (RQ2b)
• We discuss our findings in the broader context of grounding
subjective, socially-situated decision-making tasks, noting
the benefits and drawbacks of each type of grounding, and
point to how case law and constitutional grounding can com-
plement each other in supporting group-aligned subjective
decision-making.
2
RELATED WORK
In this section, we discuss how our work relates to prior work by
examining the challenges around subjective and social decision-
making, designs for and applications of constitutional grounding,
and precedents for cases to aid decision-making in prior social and
technical systems.
2.1
Challenges in Grounding Subjective and
Socially-Established Concepts
Subjective and socially-defined concepts are common in many situ-
ations where humans or AI systems need to make decisions, posing
unique challenges. For example, online communities on social me-
dia platforms often have group-specific shared knowledge in the
form of norms or “common sense” criteria around what content
(or behavior) is appropriate [10]. These norms often contribute
significantly towards how moderation decisions are made [45], but
frequently are not explicitly documented [36]. This often makes it
challenging for those without such context to accurately judge situa-
tions even in the presence of written community guidelines [31, 33].
Additionally, concepts in written guidelines can often be under-
specified or even conflicting, which can lead to diverging interpreta-
tions [23, 62]. Furthermore, socially-established norms and criteria
are often fluid, changing over time as the community acquires new
members or demographics shift [42]. These factors all make it hard
to create and maintain artifacts for “grounding” these concepts such
that they are understood consistently across people and over time.
Beyond online communities, even annotation tasks can involve
some degree of subjectivity. For example, instructions or task de-
signers that seem clear to crowdsourcing requesters may actually
be confusing to members of a crowd [63]. Surveys or rating tasks
can also involve questions that are by nature subjective [4], ambigu-
ous, or a combination of both [13]. Efforts in the crowdsourcing
realm to build more effective grounding often end up running into
conflicting goals—where concepts need to be both unambiguously
specified so the annotation can be done while also leaving just the
right amount of flexibility for providing the exact subjectivity that
we want to capture.
2.2
Rules, Guidelines, and Constitutions
On big social network platforms that host content for millions or
billions of people, consistency and transparency around modera-
tion play a paramount role in user trust, making it important to
have a clear set of content guidelines and even training materials
that ground moderation decision-making [24, 38]. These sets of
constitutional rules are costly to develop and often require training
of moderators to execute consistently—largely relegating them to
bigger organizations where such costs can be justified [52, 53] Even
in smaller online communities, rules and community guidelines
often serve as ways to ground the criteria for what is acceptable
content [19]. However, prior work has also observed that in many
cases real-world moderation decisions do not always match the
expectations of users even given community guidelines [25, 31, 33].
Indeed, not all constitutional grounding needs to take the form
of rules and guidelines applied by humans and thus subject to sub-
jective interpretation. Online communities have built constitutions
in the form of code to automatically execute decisions, such as with
systems like AutoModerator [32], ORES [26], and PolicyKit [65].
Constitutional grounding can also form grounding that is inter-
nally applied to ground model behavior, such as with efforts around
Constitutional AI [3, 28] where humans provide guidelines that
ground the behavior of LLMs. However, even in the case of con-
stitutions implemented as code, models can introduce new biases,
and the problem of incomplete or conflicting constitutions can still
cause decisions that do not align with the intentions of groups or
communities.
2.3
The Case for Cases
Cases and case studies have broadly been used as a medium for
reasoning around complex scenarios in various fields similar to the

--- Page 3 ---

Case Law Grounding: Using Precedents to Align Decision-Making for Humans and AI
CI 2025, August 4–6, 2025, San Diego, CA, USA
Figure 1: A diagram contrasting different approaches to align decisions: (1) traditional “constitutional” grounding design,
involving applying abstract guidelines to construct judgments; and (2) “case law” grounding proposed in this work, that utilizes
retrieval of past cases followed by selection of applicable precedents to construct judgments.
socially-constructed judgments we focus on. For example, moral
case deliberation [16, 50, 60] is often used in medical settings to
reflect on ethical situations [46], and case studies are common in
business educational settings too [18]. In legal education, fictional
cases are frequently used in exercises as a medium for engaging in
deliberative reasoning [21, 51]. Case-based reasoning (CBR) that
focuses on analyzing the circumstances around specific case sce-
narios also has a long and rich history as a method for thinking
about moral philosophy [49] and in the realm of jurisprudence in
the US legal system [7, 37].
In crowdsourced annotation, cases in the form of examples
can augment rubrics to demonstrate how judgments should be
made [63], act as tests to evaluate whether a concept or criteria was
accurately understood [27, 43, 57], and even pose as reference an-
chors to ground the levels on a subjective scale [12]. More broadly
speaking, a data-centric view around subjective concepts posits that
data points can also be broadly interpreted as cases [35, 56], with
the training of classifiers using human-annotated data being itself
a form of grounding (a model’s) decisions through the medium of
cases. Though in many datasets, issues around the original data
collection often limit their utility as a good model of subjectiv-
ity [1, 14].
Finally, the detail provided by individual cases means that they
can act as a medium for deliberation to reconcile differences and
work towards shared understanding. We can see examples of this
in the legal realm around adjudication [8], medical realm for di-
agnosis [6, 54], in communities for working out moderation pol-
icy [17, 47], and more generally just around challenging tasks in-
volving different lines of reasoning [11].
3
CASE LAW GROUNDING
In the legal space, there are similar challenges when it comes to
grounding decisions in a way that follows the will of the public,
and prior work has observed similarities between the grounding of
decisions in sociotechnical settings and those in the legal realm [7].
One interesting parallel lies in the mechanisms used for grounding
decisions: similar to the rules and guidelines common in sociotech-
nical systems, constitutional (or statutory) laws also serve a similar
purpose of providing high-level guidance around decisions. How-
ever, in addition to constitutional grounding, some legal systems
also make use of case law to address situations when constitutional
guidance is ambiguous, incomplete, or conflicting. The concept of
case law presents the idea that past decisions can also ground future
decisions in the form of analogies between past cases and the cur-
rent case. By identifying similarities and differences in the nature
of facts within each case, it is possible to derive ad-hoc unstated
principles or determinations that people are in agreement on [2].
In this work, we propose Case Law Grounding (CLG) as an initial
approach that explores the idea of using past decisions to ground
decision-making (Figure 1). In the following subsections, we will
describe a general set of steps for conducting case law grounding

--- Page 4 ---

CI 2025, August 4–6, 2025, San Diego, CA, USA
Quan Ze Chen and Amy X. Zhang
in the decision-making process, followed by two specific imple-
mentations of this process in a human-led and an LLM-prompted
design.
Figure 2: A diagram showing, at a high level, the process of
case law grounding reflected as 3 steps: (1) finding potentially
relevant past cases, (2) selecting precedents, and (3) finalizing
precedents into judgments. We also show two instantiations
of the process: A human-centric process (top) where, after
relevant cases are retrieved, human annotators use an interac-
tive tool to view and classify cases, and an AI-centric process
(bottom) where an LLM takes the role of a decision-maker
and, through chain-of-thought style prompts, evaluate prece-
dents and form decisions.
3.1
Step 1: Retrieving Relevant Cases
The first step in case law involves conducting legal research. In legal
practice, lawyers spend considerable effort to locate, examine, and
reason about the space of past decided cases in order to draft the
best argument for their client. This often involves querying legal
databases to identify relevant cases that can be binding precedents
for the case they are arguing [5]. Once relevant cases are found,
there can be additional criteria and checks to make sure that they
can apply.
Semantic Similarity for Case Retrieval: Experts in the legal
space depend on specialized keywords and indexing systems that
let them navigate well-reasoned facets of case law to quickly lo-
calize their search space. These indices are valuable because they
can encode crucial aspects of a case that directly help identify its
viability as a precedent (e.g., is the jurisdiction the same, are there
commonalities in the circumstances, evidence, or statutory nature
of the case); thus it makes sense to spend resources to create them.
In the settings we consider, we can’t expect to have ready-made case
indices, but we can utilize advances in general-purpose language
models to approximate case retrieval through text embeddings.
Since the cases we’re interested in (e.g., online comments, inter-
personal advice scenarios, user queries, and AI model responses)
encode all of their factual properties through their natural language
descriptions, a reasonable proxy for the relevance of any case to
any other can be approximated in the form of the distance between
them in the embedding space 𝑑(𝑥past,𝑥current). Depending on the
domain, it may be possible to choose an embedding specifically
created for the domain, though in many situations, an off-the-shelf
generic embedding can also be sufficient.
3.2
Step 2: Determining Applicable Precedents
Simply surfacing potentially relevant cases to the agent making
a decision is likely not sufficient, as we don’t know whether the
decision-maker considers the prior case as precedent setting and
whether they have integrated it into their judgment. In the legal
realm, the selection of precedents from related cases is made explicit,
taking the form of a written document containing the arguments
being made, and especially the citations to prior precedent cases
that support such arguments. Indeed, this explicit identification
and documentation of precedents as supporting arguments to a
judgment can confer many benefits. For one, by documenting the
exact cases used to support a judgment, it becomes easier to audit
the reasoning behind judgments. One can gain an understanding
of disagreements between different decision-makers by inspecting
the commonalities and differences in the precedents selected. Ad-
ditionally, selecting precedents decouples the judgment process
from a more subjective (and possibly un-grounded) interpretation
of a case and outcome to instead focus on reasoning about more
objective comparisons between aspects of the cases. Finally, by
having a shared set of precedents to draw from, we can improve
the consistency of decisions across different adjudicators who may
have different personal subjective preferences.
However, requiring a full argument for each case, while effective
for challenging crowd judgment tasks [11, 15], can be labor inten-
sive. To mitigate this issue, in this stage we simplify the argument
process to focus only on the classification of whether a retrieved
case is a good precedent, not why it is so. This means that instead
of coming up with a judgment, writing a justification, and citing
cases to support it, an adjudicating agent focuses on presenting
their evaluation of the neighborhood of cases.
Specifically, in this step, the agent will be asked to classify the
retrieved cases into either:
• Precedent1: A retrieved case should be marked as a prece-
dent if that prior case provides support for the judged case
to adopt a similar decision due to substantially similar cir-
cumstances or aspects (i.e., cases that fall on the same side
of the decision bound of the judged case).
• Doesn’t Apply2: A retrieved case does not apply as a prece-
dent if there are critical aspects of the case that differ from
the judged case such that the argument for the past decision
would not apply to the new case. While many cases that
don’t apply as precedents are likely to fall on the opposite
side of the decision bound of the judged case, this is not a
requirement for the case to not apply. Sufficiently significant
differences in circumstance or factual aspects don’t necessar-
ily need to result in opposing outcomes (e.g., involvement of
a minor versus adult in a legal case might affect the argument
but the outcome judgment could end up being the same).
While case selection can be led by a human annotator, with ad-
vances in reasoning with natural language using language models,
it is also possible for an LLM to be used with a specially designed
prompt to complete this step.
1Often referred to as an “adopted” precedent.
2Often referred to as a “distinguished” precedent.

--- Page 5 ---

Case Law Grounding: Using Precedents to Align Decision-Making for Humans and AI
CI 2025, August 4–6, 2025, San Diego, CA, USA
3.3
Step 3: Deriving Judgments from Selected
Precedents
Once the sets of precedent cases have been selected in the step
above, a final decision can be synthesized by checking each case
in the precedent sets and adopting the judgments associated. With
the assumption of stare decisis, we view the previous judgments on
any retrieved past cases as a reliable source of truth. This means
we can view each case as evidencing a direction to take the final
judgment.
3.4
Supporting Human-Led and LLM Prompted
Decision-Making
3.4.1
Case Selection Tool. For the human-led decision-making pro-
cess, we built an annotation interface that is deployed to our par-
ticipants in the form of a web application (Figure 3). We split the
annotation interface down the middle, presenting the general usage
instructions and the case being judged on the left (Figure 3(a)), and
interface components to support making grounded decisions placed
on the right.
We use the right side interface to facilitate the steps for con-
ducting decision-making following the case law grounding process.
During annotation, the right side of the interface is populated with
a list of cases retrieved through the case retrieval step (Figure 3(b)).
Under each retrieved case, the annotator can click on a button to
toggle whether a case should be considered a precedent or not.
Once the annotator is done evaluating each case, they are asked to
provide a final decision given their review of the precedents but
not constrained to the decisions of them. While selecting the set of
applicable precedents alone is sufficient for the CLG workflow, this
last question is included to allow us to evaluate whether enforcing
binding precedents (subsection 3.3) is important to final accuracy
or not.
Additionally, for our experiments, we adapted the same inter-
face to also facilitate decision-making following a more traditional
constitutional grounding process. In the constitutional grounding
condition, we use the same general interface but render a list of
rules and guidelines associated with each case in our task domain
(Figure 3(c)) instead of retrieved precedents. We also include check-
boxes for each rule, prompting the human annotator to indicate any
that they applied during their decision-making process. As we can’t
derive the final decision directly in constitutional grounding, we
rely on the annotators to provide their own final decision, collect-
ing this decision using the same design as the case law grounding
version.
3.4.2
LLM Prompts for Precedent Selection. To evaluate an auto-
mated process where LLMs contribute to decision-making instead
of human annotators, we also implemented a series of prompts
for LLMs to follow a grounding process similar to the human-led
version (Appendix B). In the prompting version of the workflow,
we set up the system prompt in a similar way to the instructions
section in the annotation interface, providing the instructions for
the decision task itself (whether the model is assessing case prece-
dents or constitutional guidelines) as well as task domain specific
instructions. We then provide the case being judged along with the
grounding support as part of the user prompt. Each user prompt
assessment was prompted independently, with no conversation
history persisted between two different user prompt queries.
For the LLM-prompting version of CLG, we use a case selection
prompt (subsection B.2) to evaluate each retrieved case, substitut-
ing {input} with the case being judged, {precedent} with one
retrieved past case, and {decision} with its past decision. This
prompt was then repeatedly invoked for each retrieved case, pro-
ducing a binary output for whether the case should be considered
a precedent or not. Following the CLG process, these precedent
determinations were then used to derive the final decision. Unlike
the human annotation interface where annotators also produced a
final decision based on their review of precedents but were uncon-
strained by the decisions of those precedents, we could not create
a prompt that provided all precedents to the model to produce a
single final decision in a way that fit within the context window
of the model; thus, non-binding precedents were only evaluated
for the human-led process and not the LLM prompting version. For
the LLM-prompting version of constitutional grounding, we use
a guideline assessment prompt (subsection B.3) to evaluate each
retrieved case, substituting {input} with the case being judged
and {instructions} with a list of rules and guidelines for making
the decision. We then collected the resulting output directly as the
model’s final decision.
4
EXPERIMENTS
To evaluate CLG, we set out to answer the following research
questions:
• RQ1: Does the case law grounding approach result in more
accurately aligned decisions compared to traditional rule-
based constitutional grounding?
• RQ2: How do specific choices in the retrieval setup and prece-
dent application affect the alignment accuracy of decisions
produced?
– RQ2a: How does the alignment accuracy scale with dif-
ferent retrieval window size (𝑘) for precedents?
– RQ2b: How do binding precedents affect the alignment
accuracy of the decisions?
4.1
Experiment Setup
To answer RQ1, we set up two main conditions rule—representing
a constitutional grounding process, and case—representing CLG.
We conducted this comparison across 2 types of decision-making
tasks (moderation and toxicity rating) spanning 5 community /
group specific decision-making task instances. In each condition,
we evaluated both the human-led and llm-prompting versions of
CLG.
For RQ2, we dive into how the choices in the CLG configuration
contributed to performance by conducting ablation-style experi-
ments. Specifically, we examined the effects of a smaller retrieval
window size on decision accuracy (RQ2a) and we compared the
decisions derived from binding precedents with human-produced
decisions (non-binding) to examine the need for binding precedents
(RQ2b).
4.1.1
Tasks and Datasets. We picked two real-world decision-making
tasks that involve subjective decisions with social context specific

--- Page 6 ---

CI 2025, August 4–6, 2025, San Diego, CA, USA
Quan Ze Chen and Amy X. Zhang
(a) Task and instructions
(b) Case law grounding interface for the case condition
(c) Constitutional grounding interface for the rule condition
Figure 3: Screenshots of the annotation tool interface used to collect annotations in the human-led process.
to groups: a comment moderation task where the decision is to
“keep” or “remove” a comment posted in a Reddit community, and
a toxicity rating task where the decision is the scalar rating of the
toxicity level of a social media post (on a scale from 1–5). We se-
lected datasets for ground truth annotations that covered different
groups / communities that we could readily recruit for our annota-
tion study. This dataset separates comments by the “subreddit” it
was posted in, which we use to partition distinct communities that
will likely have distinct preferences around content moderation.
For the tox domain, we used the toxicity perspectives dataset [40]
which contains a wide range of posts collected from social media
platforms that were then evaluated by crowd annotators and rated
for toxicity. This dataset contains disaggregated ratings that are
associated with demographic information of the annotator, which
we use to segment a general crowd worker population into distinct
salient groups.
Within each dataset, we performed additional steps to select for
communities and groups with sufficient data size that we could read-
ily recruit that we document in subsection A.1. We also randomly
shuffled and sub-sampled data for each task domain and group
instance (10% as precedents, 10% used in both human and LLM
decision evaluation). We also divided sampled cases into “batches”
of 10 each, with each annotator only judging one such batch. In the
constitutional grounding condition (rule) we drew from existing
rules and guidelines associated with each task domain and group
(see subsection A.1 for details).

--- Page 7 ---

Case Law Grounding: Using Precedents to Align Decision-Making for Humans and AI
CI 2025, August 4–6, 2025, San Diego, CA, USA
rule
case
example
Condition
0.2
0.4
0.6
0.8
Accuracy
0.560
0.721
0.595
Group = seen=Y,targeted=N
rule
case
example
Condition
0.293
0.490
0.227
Group = seen=Y,targeted=Y
(a) Accuracy of human deci-
sions the tox domain
rule
case
example
Condition
0.5
0.6
0.7
0.8
0.9
1.0
Accuracy
0.667
0.900
0.567
Group = Coronavirus
rule
case
example
Condition
0.689
0.722
0.889
Group = AmItheAsshole
rule
case
example
Condition
0.733
0.893
0.820
Group = Games
(b) Accuracy of human decisions the mod do-
main
Figure 4: Accuracy of the decisions produced by humans
using each grounding approach, rule for constitutional
grounding and case for Case Law grounding. For the case
condition, results reflect the retrieval setup used during an-
notation (𝑘= 15). We also include an example condition,
which presents the accuracy when binding precedents are
not enforced and retrieved cases primarily act as examples
(details discussed in subsubsection 4.3.2).
rule
case
Condition
0.2
0.4
0.6
0.8
Accuracy
0.504
0.740
Group = seen=Y,targeted=N
rule
case
Condition
0.232
0.440
Group = seen=Y,targeted=Y
(a) Accuracy of LLM deci-
sions the tox domain
rule
case
Condition
0.5
0.6
0.7
0.8
0.9
1.0
Accuracy
0.661
0.900
Group = Coronavirus
rule
case
Condition
0.727
0.833
Group = AmItheAsshole
rule
case
Condition
0.571
0.900
Group = Games
(b) Accuracy of LLM decisions the mod do-
main
Figure 5: Accuracy of the decisions produced by LLMs
prompted using each grounding approach, rule for con-
stitutional grounding and case for Case Law grounding. To
match human decision-makers, 𝑘= 15 was also used as the
retrieval window for presenting precedents to the LLM in
the case condition.
4.1.2
Communities and Groups. A major challenge in making de-
cisions over subjective and socially-defined concepts lies in the
locality of preferences—criteria for the same decision task like toxi-
city rating or moderation can differ considerably between groups
and communities [39]. To capture this, we further split each task do-
main into specific task instances defined by the group or community
the decisions should align to.
For the mod domain, we selected 3 large communities from Red-
dit that were captured by the NormVio dataset. For the tox do-
main, demographic backgrounds of raters can contribute to signif-
icant preference differences, so we take the most significant two
(prior exposure and observers versus victims) such demographic
dimensions identified by prior work [40]. Overall, this resulted in
5 group-defined task instances, details of which we document in
subsection A.2.
4.1.3
Participant Recruitment and Crowdsourced Annotation. We
recruited participants for the mod tasks directly from the respective
subreddits. For tox, we recruited participants on Prolific, a crowd-
sourced survey platform. In both domains, we used a screening
survey to identify participants that would be a good fit. Human
participants in both conditions were paid a base rate of $15 for
completing our annotation study (30-45 minutes), with Prolific par-
ticipants being paid through the platform and Redditors being paid
in the form of an Amazon Gift Card. In total, we were able to re-
cruit 𝑛= 60 participants from Prolific and 𝑛= 35 participants from
Reddit. We document the additional details around recruitment in
subsection A.3.
4.1.4
Additional Setup Details. To facilitate evaluations such as the
simulation study or examination of binding-ness of precedents, we
made additional configurations to the annotation task setup. These
details, as well as general configuration parameters, are documented
in subsection A.4.
4.2
RQ1: Comparing Case Law and
Constitutional Grounding
To answer RQ1, we compare the accuracy at which each ground-
ing approach reproduces the ground truth decisions observed for
each group and task. For the human-led process, we follow the
workflow in subsection 3.4, using human annotators for each task
and group to produce decisions grounded by either constitutional
grounding (rule) or case law grounding (case). We found that for
the human-led process (Figure 4), case law grounding was able
to produce statistically significantly higher accuracy in 4 out of 5
groups: +16.7 p.p.3 for seen=Y,targeted=N in tox (paired t-test,
𝑝= 0.010 < 0.05), +19.1 p.p. for seen=Y,targeted=Y in tox (paired
t-test, 𝑝= 0.019 < 0.05), +23.3 p.p. for Coronavirus in mod (paired
t-test, 𝑝= 0.045 < 0.05), and +16.0 p.p. for Games in mod (paired
t-test, 𝑝= 0.029 < 0.05). However, we did not observe any sig-
nificant difference between the two grounding approaches in the
AmItheAsshole in mod, with a difference of 3.3 p.p. (paired t-test,
𝑝= 0.721 > 0.05).
For the LLM-prompting process, we also follow the prompts in
subsection 3.4. We found that for the LLM process (Figure 5), case
law grounding was able to produce statistically significantly higher
accuracy in 4 out of 5 groups: +23.6 p.p. for seen=Y,targeted=N in
tox (paired t-test,𝑝= 0.004 < 0.05), +20.8 p.p. for seen=Y,targeted=Y
in tox (paired t-test, 𝑝= 0.006 < 0.05), +23.9 p.p. for Coronavirus
in mod (paired t-test, 𝑝= 0.011 < 0.05), and +32.9 p.p. for Games
in mod (paired t-test, 𝑝= 0.006 < 0.05). However, similar to the
human-led version, we did not observe any significant difference
between the two grounding approaches in the AmItheAsshole in
mod, with a difference of +10.6 p.p. (paired t-test, 𝑝= 0.229 > 0.05).
Overall, these results suggest that for the vast majority of the
tested groups and tasks, CLG resulted in decisions that had sta-
tistically significantly higher accuracy compared to constitutional
grounding. We find AmItheAsshole in mod to be an outlier—while
average accuracy was higher, the difference was not significant,
indicating that grounding with cases can be less effective in some
situations.
4.3
RQ2: Assessing Retrieval and Decision
Derivation Configurations
For our second RQ, we examine two configuration aspects of the
CLG workflow that may contribute to the final accuracy: the re-
trieval window size (𝑘), and whether to enforce binding precedents
(case) as is default in CLG or not (example).
4.3.1
RQ2a: Alignment Accuracy and Retrieval Window Size. In Fig-
ure 6 and Figure 7, we plot the simulated accuracy (subsection A.4)
3percentage points

--- Page 8 ---

CI 2025, August 4–6, 2025, San Diego, CA, USA
Quan Ze Chen and Amy X. Zhang
1
3
5
10
15
k
0.2
0.4
0.6
0.8
1.0
Accuracy
Group = seen=Y,targeted=N
1
3
5
10
15
k
Group = seen=Y,targeted=Y
Condition
oracle
knn
case
rule
(a) Accuracy scaling on the tox do-
main for humans
1
3
5
10
15
k
0.6
0.7
0.8
0.9
1.0
Accuracy
Group = Coronavirus
1
3
5
10
15
k
Group = AmItheAsshole
1
3
5
10
15
k
Group = Games
Condition
oracle
knn
case
rule
(b) Accuracy scaling on the mod domain for
humans
Figure 6: Scaling of human decision accuracy given differ-
ent retrieval window sizes 𝑘∈{1, 3, 5, 10, 15} for Case Law
grounding (simulated results when 𝑘≠15). We also plot two
reference lines: oracle indicates the upper-bound accuracy
when picking the best available precedent(s) within the re-
trieval window; knn indicates the accuracy of the consensus
decision for each retrieval window. Additionally, we note that
rule does not involve retrieval and thus has no window size
(𝑘), however we plot it at 𝑘= 15 to match the non-simulated
window size 𝑘when collecting results for case.
1
3
5
10
15
k
0.2
0.4
0.6
0.8
1.0
Accuracy
Group = seen=Y,targeted=N
1
3
5
10
15
k
Group = seen=Y,targeted=Y
Condition
oracle
knn
case
rule
(a) Accuracy scaling on the tox do-
main for LLMs
1
3
5
10
15
k
0.5
0.6
0.7
0.8
0.9
1.0
Accuracy
Group = Coronavirus
1
3
5
10
15
k
Group = AmItheAsshole
1
3
5
10
15
k
Group = Games
Condition
oracle
knn
case
rule
(b) Accuracy scaling on the mod domain for
LLMs
Figure 7: Scaling of LLM decision accuracy given different
retrieval window sizes 𝑘∈{1, 3, 5, 10, 15} for Case Law ground-
ing. Reference lines for oracle and knn same as in Figure 6.
rule indicates outputs for LLM prompts with constitutional
grounding, also plotted at 𝑘= 15.
of CLG (case) in the human-led and LLM-prompting based pro-
cesses at smaller retrieval window sizes than we used for RQ1 to
evaluate whether smaller retrieval windows may be sufficient. In
addition to plotting the scaling of case at different values of 𝑘and
presenting the rule condition for comparison at 𝑘= 15, we also
plot how 2 additional reference lines behave at different values of
𝑘: oracle and knn. The oracle reference line indicates an upper
bound on accuracy given a certain retrieval window. For any case
being judged, if the retrieval window contains a past case matching
ground truth, the oracle will have perfect accuracy. We observe
that at small retrieval windows, it is often the case that across the
entire set of judged cases, even the oracle cannot achieve perfect
accuracy, as for some cases no correct selection of precedents exists.
However, as 𝑘becomes larger, we see oracle more consistently
achieving perfect accuracy. The knn reference line represents a
strategy that always selects all precedents and relies on the tie-
breaking mechanism in CLG to produce the final decision.
In both human and LLM processes, we did not find any consis-
tent correlation between 𝑘values and accuracy across the tested
groups and domains, nor did we find statistically significant differ-
ences between neighboring 𝑘values when it came to final accuracy,
suggesting that for many of the individual groups and domains
tested, smaller 𝑘values may be sufficient to achieve a similar level
of accuracy.
However, looking across groups we also observed the following
behavior patterns that we believe suggest against picking very small
𝑘values to reduce decision cost, especially since it is not possible
to evaluate scaling in practice when ground truth is not available:
Performance plateau behavior. In most of the groups and
domains (excluding the outlier AmItheAsshole from before), accu-
racy tends to reach a plateau where further scaling of 𝑘contributes
little to accuracy. However, the speed at plateauing varies by the
group and domain: For example, groups like seen=Y,targeted=N
or Coronavirus seem to reach a plateau at 𝑘= 3 and 𝑘= 5, while
Games still sees accuracy improvements at 𝑘= 10. While this be-
havior is not too surprising by itself—with more dissimilar cases
retrieved, we should expect additional cases to be less and less rele-
vant to the final decision—there does not seem to be a consistent 𝑘
that ensures plateauing across groups and tasks. We hypothesize
that this variation across groups is likely to do with aspects like
the “density” (average distance) of past cases that can be retrieved
and distributional properties of past cases around the judged cases.
Unreliable for retrieval windows that are too small. We
also observe that very small values of 𝑘such as 𝑘= 1 or 𝑘= 3
result in unpredictable performance. For seen=Y,targeted=Y and
Coronavirus, we even saw drops in performance at lower 𝑘values.
While these drops are not significant when viewed across all judged
cases, they indicate that accuracy is more sensitive to 𝑘when 𝑘is
small—moving between retrieval thresholds can impact accuracy
on some portions of cases. We hypothesize that this may be due
to case-based approaches naturally being more sensitive when the
retrieval window is low, as small changes could result in relevant
precedents not making it past the threshold or immediate local
neighborhoods primarily comprising of similar but less relevant
cases.
Ultimately, we don’t find generalizable correlations between
changes in the retrieval window 𝑘and final performance, only
noting that for any task / group, 𝑘should be sufficiently large so as
to reach the performance plateau; otherwise (when 𝑘is too small)
performance can suffer.
4.3.2
RQ2b: Binding Precedents versus Cases as Examples. In prior
work around grounding human decision-making in crowdsourcing
settings, examples [63] have been noted as an important feature for
constructing more effective guidelines or “constitutions”. Unlike
CLG, however, constitutional grounding examples are selected and
incorporated during the construction of the constitution, meaning
that they do not adapt to properties of the case being judged. This
raises the question of whether simply retrieving and presenting
prior related cases for a new case in the form of examples alone
is sufficient for improving grounding accuracy or if the binding
nature of precedents—where decisions must derive directly from
selected precedent sets—needs to be applied for CLG to produce
accurately grounded decisions.
To examine this, during the human annotation process, we not
only collected participants’ judgments on whether each precedent
applied, we also asked participants to give a final decision on the
judged case after reviewing the list of retrieved prior cases without
being constrained to the consensus of the cases they selected as
precedents (as noted in subsection 3.4). In Figure 4, we include
an additional condition—example—to reflect the accuracy of this

--- Page 9 ---

Case Law Grounding: Using Precedents to Align Decision-Making for Humans and AI
CI 2025, August 4–6, 2025, San Diego, CA, USA
configuration. Comparing the accuracy produced by non-binding
precedents (example) to that of constitutional grounding (rule),
we note the absence of statistically significant differences (paired
t-test, 𝑝= 0.635, 0.360, 0.458, 0.266 > 0.05 for seen=Y,targeted=N,
seen=Y,targeted=Y, Coronavirus, Games) in most of the groups,
despite the fact that we did observe statistically significant im-
provements to accuracy when using binding precedents (case).
Here, again, AmItheAsshole is an outlier, with example show-
ing a statistically significant improvement over rule (+20.0 p.p,
𝑝= 0.020 < 0.05) even though binding precedents (case) did not
show significant improvements.
5
DISCUSSION
5.1
Limitations of Our Implementation
In this work, we explored a relatively simple implementation of
case law for grounding decisions where reasoning around cases is
abstracted simply into a selection process. However, in the legal
space, there are many specific conventions around how precedents
are actually used [2, 59]. While the degree to which case-based
and analogical reasoning can be applied is still openly debated in
the legal realm [7], there are opportunities to improve the value of
grounding cases by making use of full-fledged analogical reasoning.
Furthermore, we also observed differences between groups / com-
munities in how CLG affected decision alignment accuracy in our
experiments, with notable cases like AmItheAsshole seeing a very
different performance pattern. While we don’t have sufficient re-
sults to examine this more comprehensively, we do hypothesize that
the permissiveness and concreteness of the community’s internal-
ized criteria itself may be at play. Compared to other communities
examined, AITA was much more permissive about what content
is acceptable: even in ambiguous cases (like suspected fabricated
stories), enforcement of moderation tended to lean lenient. This
inherent acceptance of ambiguity could contribute to less visible
differences between constitutional and case law style grounding,
which specifically focuses on challenges with ambiguous concepts.
5.2
Integrating CLG into Decision-Making
Ecosystems
While we primarily compared CLG and constitutional grounding
in this work, both approaches offer unique values in the broader
ecosystem of decision-making. When we look at prior examina-
tions of community governance [29], we often see a combination of
rules and cases being used throughout the process—with cases con-
tributing to “legislative” processes that produce the very rules and
guidelines that are adopted while also being applied in debates over
ambiguous cases. Similar patterns of adopting both abstractions
(constitutional rules) and specifics (case-based analogical reason-
ing) are common in high-stakes decision-making tasks such as with
jurisprudence [7].
Ultimately, constitutional and case-law grounding are suited to
different challenges in decision-making, and with this work, our
goal is to bring to light the need for more case-based approaches
around the challenging decision-making tasks like those involved
in online community governance or in areas like AI alignment.
We believe there is much to be explored around future processes
that combine both forms of grounding to efficiently produce high-
quality decisions—both in human-led and AI automated settings.
6
CONCLUSION
In this paper, we present case law grounding (CLG), a novel workflow
that uses precedents for aligning decisions to socially constructed
norms and preferences of groups and communities. We evaluate
two versions of CLG, a human-led process and an automated LLM
process, on 2 decision-making tasks spanning 5 instances. We also
examine the impacts of different configurations of CLG such as
retrieval window size and binding or non-binding precedents. Fi-
nally, we discuss the limitations of CLG and how CLG could fit
into the broader ecosystem around grounding decision-making in
sociotechnical systems.
REFERENCES
[1] Kofi Arhin, Ioana Baldini, Dennis Wei, Karthikeyan Natesan Ramamurthy, and
Moninder Singh. 2021. Ground-Truth, Whose Truth? – Examining the Challenges
with Annotating Toxic Text Datasets. arXiv:2112.03529 [cs.CL] https://arxiv.
org/abs/2112.03529
[2] Kevin D. Ashley. 1991. Modeling Legal Arguments: Reasoning with Cases and
Hypotheticals. MIT Press, Cambridge, MA, USA.
[3] Yuntao Bai, Saurav Kadavath, Sandipan Kundu, Amanda Askell, Jackson Kernion,
Andy Jones, Anna Chen, Anna Goldie, Azalia Mirhoseini, Cameron McKinnon,
Carol Chen, Catherine Olsson, Christopher Olah, Danny Hernandez, Dawn
Drain, Deep Ganguli, Dustin Li, Eli Tran-Johnson, Ethan Perez, Jamie Kerr,
Jared Mueller, Jeffrey Ladish, Joshua Landau, Kamal Ndousse, Kamile Luko-
suite, Liane Lovitt, Michael Sellitto, Nelson Elhage, Nicholas Schiefer, Noemi
Mercado, Nova DasSarma, Robert Lasenby, Robin Larson, Sam Ringer, Scott John-
ston, Shauna Kravec, Sheer El Showk, Stanislav Fort, Tamera Lanham, Timothy
Telleen-Lawton, Tom Conerly, Tom Henighan, Tristan Hume, Samuel R. Bowman,
Zac Hatfield-Dodds, Ben Mann, Dario Amodei, Nicholas Joseph, Sam McCandlish,
Tom Brown, and Jared Kaplan. 2022. Constitutional AI: Harmlessness from AI
Feedback. arXiv:2212.08073 [cs.CL] https://arxiv.org/abs/2212.08073
[4] Frank R. Bentley, Nediyana Daskalova, and Brooke White. 2017. Comparing
the Reliability of Amazon Mechanical Turk and Survey Monkey to Traditional
Market Research Surveys. In Proceedings of the 2017 CHI Conference Extended
Abstracts on Human Factors in Computing Systems (Denver, Colorado, USA) (CHI
EA ’17). Association for Computing Machinery, New York, NY, USA, 1092–1099.
https://doi.org/10.1145/3027063.3053335
[5] Robert C Berring. 1987. Legal research and legal concepts: where form molds
substance. California Law Review 75, 1 (1987), 15–27.
[6] Loes CM Bertens, Berna DL Broekhuizen, Christiana A Naaktgeboren, Frans H
Rutten, Arno W Hoes, Yvonne van Mourik, Karel GM Moons, and Johannes B
Reitsma. 2013. Use of expert panels to define the reference standard in diagnostic
research: a systematic review of published methods and reporting. PLoS medicine
10, 10 (2013), e1001531.
[7] Nicholas Caputo. 2024. Alignment as Jurisprudence. https://papers.ssrn.com/
sol3/papers.cfm?abstract_id=4800894
[8] Charles E Carpenter. 1917. Court Decisions and the Common Law. Columbia
Law Review 17, 7 (1917), 593–607.
[9] Eshwar Chandrasekharan and Eric Gilbert. 2019. Hybrid Approaches to Detect
Comments Violating Macro Norms on Reddit. arXiv:1904.03596 [cs.SI] https:
//arxiv.org/abs/1904.03596
[10] Eshwar Chandrasekharan, Mattia Samory, Shagun Jhaver, Hunter Charvat, Amy
Bruckman, Cliff Lampe, Jacob Eisenstein, and Eric Gilbert. 2018. The Internet’s
Hidden Rules: An Empirical Study of Reddit Norm Violations at Micro, Meso,
and Macro Scales. Proc. ACM Hum.-Comput. Interact. 2, CSCW, Article 32 (nov
2018), 25 pages. https://doi.org/10.1145/3274301
[11] Quanze Chen, Jonathan Bragg, Lydia B. Chilton, and Dan S. Weld. 2019. Cicero:
Multi-Turn, Contextual Argumentation for Accurate Crowdsourcing. In Proceed-
ings of the 2019 CHI Conference on Human Factors in Computing Systems (Glasgow,
Scotland Uk) (CHI ’19). Association for Computing Machinery, New York, NY,
USA, 1–14. https://doi.org/10.1145/3290605.3300761
[12] Quan Ze Chen, Daniel S Weld, and Amy X Zhang. 2021. Goldilocks: Consistent
crowdsourced scalar annotations with relative uncertainty. Proceedings of the
ACM on Human-Computer Interaction 5, CSCW2 (2021), 1–25.
[13] Quan Ze Chen and Amy X. Zhang. 2023. Judgment Sieve: Reducing Uncertainty
in Group Judgments through Interventions Targeting Ambiguity versus Disagree-
ment. Proceedings of the ACM on Human-Computer Interaction 7 (2023), 1–26.
https://api.semanticscholar.org/CorpusID:258437282

--- Page 10 ---

CI 2025, August 4–6, 2025, San Diego, CA, USA
Quan Ze Chen and Amy X. Zhang
[14] Emily Denton, Mark Díaz, Ian Kivlichan, Vinodkumar Prabhakaran, and Rachel
Rosen. 2021. Whose ground truth? accounting for individual and collective
identities underlying dataset annotation.
[15] Ryan Drapeau, Lydia Chilton, Jonathan Bragg, and Daniel Weld. 2016. MicroTalk:
Using Argumentation to Improve Crowdsourcing Accuracy. Proceedings of the
AAAI Conference on Human Computation and Crowdsourcing 4, 1 (Sep. 2016),
32–41. https://doi.org/10.1609/hcomp.v4i1.13270
[16] Denis Emelin, Ronan Le Bras, Jena D. Hwang, Maxwell Forbes, and Yejin Choi.
2021. Moral Stories: Situated Reasoning about Norms, Intents, Actions, and their
Consequences. In Proceedings of the 2021 Conference on Empirical Methods in
Natural Language Processing, Marie-Francine Moens, Xuanjing Huang, Lucia
Specia, and Scott Wen-tau Yih (Eds.). Association for Computational Linguistics,
Online and Punta Cana, Dominican Republic, 698–718. https://doi.org/10.18653/
v1/2021.emnlp-main.54
[17] Jenny Fan and Amy X. Zhang. 2020. Digital Juries: A Civics-Oriented Approach to
Platform Governance. In Proceedings of the 2020 CHI Conference on Human Factors
in Computing Systems (Honolulu, HI, USA) (CHI ’20). Association for Computing
Machinery, New York, NY, USA, 1–14. https://doi.org/10.1145/3313831.3376293
[18] Mehdi Farashahi and Mahdi Tajeddin. 2018. Effectiveness of teaching methods
in business education: A comparison study on the learning outcomes of lectures,
case studies and simulations. The International Journal of Management Education
16 (2018), 131–142. https://api.semanticscholar.org/CorpusID:102489428
[19] Casey Fiesler, Jialun Jiang, Joshua McCann, Kyle Frye, and Jed Brubaker. 2018.
Reddit Rules! Characterizing an Ecosystem of Governance. Proceedings of the
International AAAI Conference on Web and Social Media 12, 1 (Jun. 2018), 72–81.
https://doi.org/10.1609/icwsm.v12i1.15033
[20] Iason Gabriel. 2020. Artificial intelligence, values, and alignment. Minds and
machines 30, 3 (2020), 411–437.
[21] John T Gaubatz. 1981. Moot court in the modern law school. J. Legal Educ. 31
(1981), 87.
[22] Vaishali U Gongane, Mousami V Munot, and Alwin D Anuse. 2022. Detection
and moderation of detrimental content on social media platforms: current status
and future directions. Social Network Analysis and Mining 12, 1 (2022), 129.
[23] Mitchell L. Gordon, Kaitlyn Zhou, Kayur Patel, Tatsunori Hashimoto, and
Michael S. Bernstein. 2021. The Disagreement Deconvolution: Bringing Ma-
chine Learning Performance Metrics In Line With Reality. In Proceedings of the
2021 CHI Conference on Human Factors in Computing Systems (Yokohama, Japan)
(CHI ’21). Association for Computing Machinery, New York, NY, USA, Article
388, 14 pages. https://doi.org/10.1145/3411764.3445423
[24] The Guardian. 2017. The Facebook Files. https://www.theguardian.com/news/
series/facebook-files.
[25] Oliver L Haimson, Daniel Delmonaco, Peipei Nie, and Andrea Wegner. 2021.
Disproportionate removals and differing content moderation experiences for
conservative, transgender, and black social media users: Marginalization and
moderation gray areas. Proceedings of the ACM on Human-Computer Interaction
5, CSCW2 (2021), 1–35.
[26] Aaron Halfaker and R. Stuart Geiger. 2020.
ORES: Lowering Barriers with
Participatory Machine Learning in Wikipedia.
arXiv:1909.05189 [cs.HC]
https://arxiv.org/abs/1909.05189
[27] Danula Hettiachchi, Mike Schaekermann, Tristan J McKinney, and Matthew
Lease. 2021. The Challenge of Variable Effort Crowdsourcing and How Visible
Gold Can Help. Proceedings of the ACM on Human-Computer Interaction 5, CSCW2
(2021), 1–26.
[28] Saffron Huang, Divya Siddarth, Liane Lovitt, Thomas I. Liao, Esin Durmus,
Alex Tamkin, and Deep Ganguli. 2024. Collective Constitutional AI: Aligning
a Language Model with Public Input. In Proceedings of the 2024 ACM Confer-
ence on Fairness, Accountability, and Transparency (Rio de Janeiro, Brazil) (FAccT
’24). Association for Computing Machinery, New York, NY, USA, 1395–1417.
https://doi.org/10.1145/3630106.3658979
[29] Sohyeon Hwang and Aaron Shaw. 2022. Rules and Rule-Making in the Five
Largest Wikipedias. Proceedings of the International AAAI Conference on Web
and Social Media 16, 1 (May 2022), 347–357. https://doi.org/10.1609/icwsm.v16i1.
19297
[30] Jane Im, Amy X Zhang, Christopher J Schilling, and David Karger. 2018. Delib-
eration and Resolution on Wikipedia: A Case Study of Requests for Comments.
Proceedings of the ACM on Human-Computer Interaction 2, CSCW (2018), 1–24.
[31] Shagun Jhaver, Darren Scott Appling, Eric Gilbert, and Amy Bruckman. 2019.
"Did You Suspect the Post Would be Removed?": Understanding User Reactions
to Content Removals on Reddit. Proc. ACM Hum.-Comput. Interact. 3, CSCW,
Article 192 (nov 2019), 33 pages. https://doi.org/10.1145/3359294
[32] Shagun Jhaver, Iris Birman, Eric Gilbert, and Amy Bruckman. 2019. Human-
Machine Collaboration for Content Regulation: The Case of Reddit Automodera-
tor. ACM Transactions on Computer-Human Interaction (TOCHI) 26 (2019), 1–35.
https://api.semanticscholar.org/CorpusID:198180039
[33] Shagun Jhaver, Amy Bruckman, and Eric Gilbert. 2019. Does transparency in
moderation really matter? User behavior after content removal explanations on
reddit. Proceedings of the ACM on Human-Computer Interaction 3, CSCW (2019),
1–27.
[34] Jiaming Ji, Tianyi Qiu, Boyuan Chen, Borong Zhang, Hantao Lou, Kaile Wang,
Yawen Duan, Zhonghao He, Lukas Vierling, Donghai Hong, Jiayi Zhou, Zhaowei
Zhang, Fanzhi Zeng, Juntao Dai, Xuehai Pan, Kwan Yee Ng, Aidan O’Gara, Hua
Xu, Brian Tse, Jie Fu, Stephen McAleer, Yaodong Yang, Yizhou Wang, Song-Chun
Zhu, Yike Guo, and Wen Gao. 2025. AI Alignment: A Comprehensive Survey.
arXiv:2310.19852 [cs.AI] https://arxiv.org/abs/2310.19852
[35] Nan-Jiang Jiang and Marie-Catherine de Marneffe. 2022. Investigating Reasons
for Disagreement in Natural Language Inference. Transactions of the Association
for Computational Linguistics 10 (2022), 1357–1374. https://doi.org/10.1162/tacl_
a_00523
[36] Prerna Juneja, Deepika Rama Subramanian, and Tanushree Mitra. 2020. Through
the looking glass: Study of transparency in Reddit’s moderation practices. Pro-
ceedings of the ACM on Human-Computer Interaction 4, GROUP (2020), 1–35.
[37] Robert A. Kagan. 2001. Adversarial Legalism: The American Way of Law. Harvard
University Press, Cambridge, MA. http://www.jstor.org/stable/j.ctvjz83k7
[38] Kate Klonick. 2020. The Facebook Oversight Board: Creating an independent
institution to adjudicate online free expression. Yale Law Journal 129, 2418 (2020),
2418–2499.
[39] Vinay Koshy, Tanvi Bajpai, Eshwar Chandrasekharan, Hari Sundaram, and Karrie
Karahalios. 2023. Measuring User-Moderator Alignment on r/ChangeMyView.
Proceedings of the ACM on Human-Computer Interaction 7 (2023), 1–36. https:
//api.semanticscholar.org/CorpusID:263621128
[40] Deepak Kumar, Patrick Gage Kelley, Sunny Consolvo, Joshua Mason, Elie
Bursztein, Zakir Durumeric, Kurt Thomas, and Michael Bailey. 2021. Design-
ing toxic content classification for a diversity of perspectives. In Proceedings of
the Seventeenth USENIX Conference on Usable Privacy and Security (SOUPS’21).
USENIX Association, USA, Article 16, 19 pages.
[41] Bill Yuchen Lin, Abhilasha Ravichander, Ximing Lu, Nouha Dziri, Melanie
Sclar, Khyathi Chandu, Chandra Bhagavatula, and Yejin Choi. 2023. The Un-
locking Spell on Base LLMs: Rethinking Alignment via In-Context Learning.
arXiv:2312.01552 [cs.CL] https://arxiv.org/abs/2312.01552
[42] Zhiyuan Lin, Niloufar Salehi, Bowen Yao, Yiqi Chen, and Michael Bernstein. 2017.
Better When It Was Smaller? Community Content and Behavior After Massive
Growth. Proceedings of the International AAAI Conference on Web and Social
Media 11, 1 (May 2017), 132–141. https://doi.org/10.1609/icwsm.v11i1.14884
[43] Angli Liu, Stephen Soderland, Jonathan Bragg, Christopher H. Lin, Xiao Ling,
and Daniel S. Weld. 2016. Effective Crowd Annotation for Relation Extraction. In
Proceedings of the 2016 Conference of the North American Chapter of the Association
for Computational Linguistics: Human Language Technologies, Kevin Knight, Ani
Nenkova, and Owen Rambow (Eds.). Association for Computational Linguistics,
San Diego, California, 897–906. https://doi.org/10.18653/v1/N16-1104
[44] Catherine C. Marshall, Partha S.R. Goguladinne, Mudit Maheshwari, Apoorva
Sathe, and Frank M. Shipman. 2023. Who Broke Amazon Mechanical Turk? An
Analysis of Crowdsourcing Data Quality over Time. In Proceedings of the 15th
ACM Web Science Conference 2023 (Austin, TX, USA) (WebSci ’23). Association for
Computing Machinery, New York, NY, USA, 335–345. https://doi.org/10.1145/
3578503.3583622
[45] J Nathan Matias. 2019. The civic labor of volunteer moderators online. Social
Media+ Society 5, 2 (2019), 2056305119836778.
[46] A. C. Molewijk, Tineke A. Abma, Margreet Stolper, and Guy Widdershoven. 2008.
Teaching ethics in the clinic. The theory and practice of moral case deliberation.
Journal of Medical Ethics 34 (2008), 120–124. https://api.semanticscholar.org/
CorpusID:19342927
[47] Christina A. Pan, Sahil Yakhmi, Tara P. Iyer, Evan Strasnick, Amy X. Zhang, and
Michael S. Bernstein. 2022. Comparing the Perceived Legitimacy of Content
Moderation Processes: Contractors, Algorithms, Expert Panels, and Digital Juries.
Proc. ACM Hum.-Comput. Interact. 6, CSCW1, Article 82 (apr 2022), 31 pages.
https://doi.org/10.1145/3512929
[48] Chan Young Park, Julia Mendelsohn, Karthik Radhakrishnan, Kinjal Jain, Tushar
Kanakagiri, David Jurgens, and Yulia Tsvetkov. 2021. Detecting Community
Sensitive Norm Violations in Online Conversations. In Findings of the Association
for Computational Linguistics: EMNLP 2021, Marie-Francine Moens, Xuanjing
Huang, Lucia Specia, and Scott Wen-tau Yih (Eds.). Association for Computational
Linguistics, Punta Cana, Dominican Republic, 3386–3397.
https://doi.org/10.
18653/v1/2021.findings-emnlp.288
[49] Norbert Paulo. 2015. Casuistry as common law morality. Theoretical Medicine
and Bioethics 36, 6 (2015), 373–389.
[50] Jessica Pierce. 2013. Morality play: Case studies in ethics. Waveland Press, Long
Grove, IL.
[51] Lewis S Ringel. 2004. Designing a moot court: What to do, what not to do, and
suggestions for how to do it. PS: Political Science & Politics 37, 3 (2004), 459–465.
[52] SARAH T. ROBERTS. 2019. Behind the Screen: Content Moderation in the Shadows
of Social Media. Yale University Press, Cambridge, MA. http://www.jstor.org/
stable/j.ctvhrcz0v
[53] Adam Satariano and Mike Isaac. 2021. The Silent Partner Cleaning Up Facebook
for $500 Million a Year. International New York Times A, 1 (2021), NA–NA.
[54] Mike Schaekermann, Graeme Beaton, Minahz Habib, Andrew Lim, Kate Larson,
and Edith Law. 2019. Understanding expert disagreement in medical data analysis

--- Page 11 ---

Case Law Grounding: Using Precedents to Align Decision-Making for Humans and AI
CI 2025, August 4–6, 2025, San Diego, CA, USA
through structured adjudication. Proceedings of the ACM on Human-Computer
Interaction 3, CSCW (2019), 1–23.
[55] Tianhao Shen, Renren Jin, Yufei Huang, Chuang Liu, Weilong Dong, Zishan Guo,
Xinwei Wu, Yan Liu, and Deyi Xiong. 2023. Large Language Model Alignment:
A Survey. arXiv:2309.15025 [cs.CL] https://arxiv.org/abs/2309.15025
[56] Rachel N Simons, Danna Gurari, and Kenneth R Fleischmann. 2020. " I Hope This
Is Helpful" Understanding Crowdworkers’ Challenges and Motivations for an
Image Description Task. Proceedings of the ACM on Human-Computer Interaction
4, CSCW2 (2020), 1–26.
[57] Adish Singla, Ilija Bogunovic, Gábor Bartók, Amin Karbasi, and Andreas Krause.
2014. Near-optimally teaching the crowd to classify. In Proceedings of the 31st
International Conference on International Conference on Machine Learning - Volume
32 (ICML’14). JMLR.org, Beijing, China, II–154–II–162.
[58] Christopher Small, Michael Bjorkegren, Timo Erkkilä, Lynette Shaw, and Colin
Megill. 2021. Polis: Scaling deliberation by mapping high dimensional opinion
spaces. Recerca: revista de pensament i anàlisi 26, 2 (2021), 1–26.
[59] Cass Robert Sunstein. 2021. Analogical Reasoning. https://papers.ssrn.com/sol3/
papers.cfm?abstract_id=3938546
[60] Darren Sush and Adel C Najdowski. 2021. A workbook of ethical case scenarios in
applied behavior analysis. Academic Press, Cambridge, MA.
[61] Laura Weidinger, John F. J. Mellor, Maribeth Rauh, Conor Griffin, Jonathan Uesato,
Po-Sen Huang, Myra Cheng, Mia Glaese, Borja Balle, Atoosa Kasirzadeh, Zachary
Kenton, Sande Minnich Brown, William T. Hawkins, Tom Stepleton, Courtney
Biles, Abeba Birhane, Julia Haas, Laura Rimell, Lisa Anne Hendricks, William S.
Isaac, Sean Legassick, Geoffrey Irving, and Iason Gabriel. 2021. Ethical and social
risks of harm from Language Models. https://api.semanticscholar.org/CorpusID:
244954639
[62] Galen Weld, Amy X. Zhang, and Tim Althoff. 2024. Making Online Communities
‘Better’: A Taxonomy of Community Values on Reddit. Proceedings of the Inter-
national AAAI Conference on Web and Social Media 18, 1 (May 2024), 1611–1633.
https://doi.org/10.1609/icwsm.v18i1.31413
[63] Meng-Han Wu and Alexander Quinn. 2017. Confusing the Crowd: Task In-
struction Quality on Amazon Mechanical Turk. Proceedings of the AAAI Con-
ference on Human Computation and Crowdsourcing 5, 1 (Sep. 2017), 206–215.
https://doi.org/10.1609/hcomp.v5i1.13317
[64] Ellery Wulczyn, Nithum Thain, and Lucas Dixon. 2017. Ex Machina: Personal
Attacks Seen at Scale. In Proceedings of the 26th International Conference on World
Wide Web (Perth, Australia) (WWW ’17). International World Wide Web Con-
ferences Steering Committee, Republic and Canton of Geneva, CHE, 1391–1399.
https://doi.org/10.1145/3038912.3052591
[65] Amy X. Zhang, Grant Hugh, and Michael S. Bernstein. 2020. PolicyKit: Building
Governance in Online Communities. In Proceedings of the 33rd Annual ACM
Symposium on User Interface Software and Technology (Virtual Event, USA) (UIST
’20). Association for Computing Machinery, New York, NY, USA, 365–378. https:
//doi.org/10.1145/3379337.3415858
A
EXPERIMENT SETUP DETAILS
A.1
Dataset Details
Preprocessing and Selection for Moderation (mod). From this dataset,
we selected the top 10 subreddits with a sufficiently large size of
examples (𝑛> 100) and did not exhibit significant skew towards
either decisions of “keep” or “remove”. We then further narrowed
down this set based on avoiding multiple communities around sim-
ilar topics and prioritizing communities that were easier to recruit
from, ultimately sub-sampling this dataset down to 3 communi-
ties: r/Coronavirus, r/AmItheAsshole, r/Gaming. Ground truth
labels for each case are established by the actual moderation deci-
sion applied to each comment.
Preprocessing and Selection for Toxicity (tox). Based on the find-
ings from the original paper, we sampled from 3 disjoint inter-
sectional demographic slices (see subsubsection 4.1.2) that were
indicated to have the most significant differences with each other:
seen=N,targeted=N, seen=Y,targeted=N, seen=Y,targeted=Y.
Ground truth labels for each case in each group are established
by taking the mean rating for that group rounded to the nearest
integer.
Constitutional Grounding Material. When evaluating the consti-
tutional grounding condition (rule), we use published community
guidelines for each subreddit as approximations of a high-quality
constitution for groups in mod. Meanwhile, for the tox domain, we
adapt the annotation guidelines given to annotators for rating toxi-
city in the original dataset paper into a list of rules that served as
the constitution for all groups. To address the fact that community
guidelines may have changed over time since being first collected,
we checked the most current community guidelines for each of
the 3 groups (subreddits) in the mod domain using the Wayback
Machine4 to confirm that no significant changes (such as adding or
removing rules) were made to the guidelines across the time span
of cases evaluated.
A.2
Communities and Groups
Moderation (mod). For this domain, we ended up selecting the
following 3 subreddits:
• r/Games—a broad interest group around game content and
the games industry
• r/Coronavirus—a community focused around high-quality
science-informed discussions related to COVID-19
• r/AmItheAsshole—a collective space for sharing and opin-
ing over a variety of interpersonal conflict scenarios
Toxicity (tox). While raters do not necessarily form a “commu-
nity”, we can still view demographic features as a way to separate
the population into groups that represent distinct norms and prefer-
ences. In our case, we stratify the general population by taking two
demographic properties identified to be significant correlating fac-
tors [40] of toxicity ratings: whether a rater has often seen toxic con-
tent when interacting with social media (negatively correlated with
scores), and whether the rater has been personally targeted by
toxic content (positively correlated with scores). Out of the 3 sensi-
ble combinations—seen=Y,targeted=N, seen=N,targeted=N, and
seen=Y,targeted=Y—we found it challenging to find participants
for seen=N,targeted=N, so we did not include that group in the
evaluations, leaving just 2 combinations.
A.3
Crowd Recruitment Details
As we envision human-led processes for grounding subjective deci-
sions (whether constitutional or case law) to be used in practice by
groups and communities themselves rather than by external popula-
tions, we set out to recruit participants that would demographically
best match the original group or community producing the ground
truth data. To achieve this goal, we applied pre-screening surveys
in each of our recruitment efforts (Appendix C), with participants
first asked to fill out the screening survey, after which we would
select and assign conditions to them.
As each of the mod groups represents a specific subreddit com-
munity, we recruited participants by running Reddit Ads targeted
to subreddits used in our task domains. Participants were asked
to fill out the screening survey and self report subreddits they fre-
quented within a list of communities (subset of the original top-10
candidates subsubsection 4.1.1, removing 1 subreddit that had been
removed). Then, participants who reported frequenting at least one
4https://web.archive.org/

--- Page 12 ---

CI 2025, August 4–6, 2025, San Diego, CA, USA
Quan Ze Chen and Amy X. Zhang
of the 3 target subreddits would be allocated a batch and condi-
tion, balancing such that each community, condition, and batch
had a target of 3 annotators. At the end, this resulted in annota-
tions on 3 batches for r/AmItheAsshole, 2 for r/Games, and 1 for
r/Coronavirus.
In the tox domain, original annotations in the original dataset
were provided by Amazon Mechanical Turk (AMT) workers. How-
ever, recent work has shown concerns around AMT [44] annota-
tions that have developed since the original dataset was collected.
To avoid issues with introducing significantly more quality control
components than the original task, we opted to recruit from Prolific,
as it is a similar crowd work platform with (as of our deployment)
lower rates of data quality issues. Participants were screened with
two questions about their prior exposure to toxic posts, with these
answers then used to assign them to one of 3 population groups (see
4.1.2). During recruitment, we also found that no crowd workers
reported being in the seen=N,targeted=N group during screen-
ing. While this was ultimately unsurprising, we opted to drop this
group.
As both experiment domains involve reading content that is
potentially offensive, we made sure to prominently disclose this
aspect during recruitment. We also allowed participants to drop out
at any point if they experienced discomfort with the annotation.
Annotators electing to withdraw consent during the task were pro-
rated payment for the amount of annotations completed, with their
data excluded from the evaluation. Additionally, to incentivize par-
ticipation from Redditors and reduce drop-out between screening
and completion, we provided an additional bonus of $5 to Redditors
who completed our annotation task within 24 hours of assignment.
A.4
Additional Implementation Details
Language Model and Embedding Model. As our goal was not to
evaluate a variety of language models, we opted to keep the models
used to produce embeddings and the LLM used to execute prompts
consistent and fixed across all conditions and task domains. For
the embedding model, we used the general purpose embedding
offered by OpenAI5 (“text-embedding-3-large” ) with a distance
metric based on cosine similarity for ranking relevant cases. As
precedent retrieval only depends on the case being judged, we pre-
computed the ordered list of retrieved past cases with 𝑘= 15 as the
retrieval window and provided this for human annotations, with
smaller window sizes simulated post-hoc. For the LLM used during
prompting, we used the gpt-4-turbo-preview model offered by
OpenAI.
Retrieval Window Simulations. In RQ2a, we evaluate how
alignment accuracy may be affected by the retrieval window size,
specifically examining different options of 𝑘∈{1, 3, 5, 10, 15}. How-
ever, directly evaluating different retrieval outputs in the human-led
workflow would be very costly, especially given the observation
that the set of retrieved examples at smaller 𝑘values would just
be subsets of those at larger 𝑘. Thus, instead of separately testing
different values of 𝑘, we only have the human participants and LLM
select precedents over the largest retrieval window size 𝑘= 15.
We then simulate the outcome of precedent selection for smaller
5https://openai.com/blog/new-embedding-models-and-api-updates
𝑘by dropping any selected precedents that would fall outside the
retrieval window at that size.
Consensus Tie-Breaking for Binding Precedents. When de-
riving final decisions based on precedents selected, it is possible for
the collection of precedents selected by either humans or LLMs to
contain a plurality of decision outcomes. While in the legal realm
such conflicts would indicate further reasoning and deliberation, in
CLG we apply a simpler deterministic approach to resolve conflicts
based on approval voting. We collect the past decision of each se-
lected precedent, and then take the mode (most common value) to
be the final decision. In the event of a tie where there are multiple
values for the mode, we break the tie by selecting the decision
that has a corresponding precedent case that is closest (retrieval
distance) to the original example being judged. Should the set of
precedents be empty, we treat this case as a tie between all retrieved
cases with each getting no votes.
B
LLM PROMPTS
B.1
Task System Prompts
System prompt for mod case:
You are an AI assistant that is assisting a moderator analyze
comments posted in an online community.
For each comment you are analyzing, you will be shown past
comments that the moderator has either removed or kept.
Your task is to decide whether the decision on each of the
past comments would be relevant to the new comment.
A relevant decision is a decision where the new comment
exhibits some similarities to the past comment.
Think step by step.
System prompt for mod rule:
You are an AI assistant that is assisting a moderator analyze
comments posted in an online community.
The moderator will provide a list of rules that posts and
comments in the community must adhere to.
Based on the list of rules, you should analyze the comment,
and respond with either "keep" or "remove".
Think step by step.
System prompt for toxicity case:
You are an AI assistant that is assisting a user in organizing
their online feed by rating whether content is toxic or not.
For each post in the feed, you will be shown past posts that
the user has rated toxicity for on a scale from 1 to 5.
Your task is to decide whether the toxicity rating of the
past post would be relevant to the new post.
A relevant rating is a rating where the new post exhibits
some similarities to the past post.
Think step by step.

--- Page 13 ---

Case Law Grounding: Using Precedents to Align Decision-Making for Humans and AI
CI 2025, August 4–6, 2025, San Diego, CA, USA
System prompt for toxicity rule:
You are an AI assistant that is assisting a user in
organizing their online feed by identifying whether content
is toxic or not.
The user will provide a list of indicators of what content is
commonly toxic.
Based on the list, you should analyze the content, and
respond with a number between 1 and 5, with 1 indicating
the content is not toxic at all, and 5 indicating that the
content is extremely toxic.
Think step by step.
B.2
Prompts for Case Law Grounding
Prompt for case selection:
The comment you are analyzing is:
{input}
The moderator has judged the following
similar comment in the past:
{precedent}
The moderator made a decision of "{decision}".
Answer with "relevant" if the past comment should
be considered in the decision for the new comment, or
"not relevant" if it should not.
B.3
Prompts for Constitutional Grounding
Prompt for rule determination:
Below are a list of guidelines for making your decision:
{instructions}
The content you are deciding is:
{input}
Assess whether each rule applies, and then make your
final decision.
Think step by step.
C
SCREENING SURVEY
C.1
Screening Questions for toxicity
These questions are adapted from a subset of questions taken from
survey questions annotators had to answer in the original toxicity
perspectives dataset [40].
(1) What types of sites do you use regularly?
• Social Networking (Facebook, Twitter)
• Video (YouTube, Twitch)
• News (CNN, Fox, NYT, WSJ)
• Community Forums (Reddit, Craigslist, 4chan)
• Email or messaging (Gmail, WhatsApp, Facebook Chat)
(2) For the sites you use, have you ever seen posts or comments
you consider toxic?
• Yes
• No
(3) Have you ever personally been the target of toxic posts or
comments?
• Yes
• No
Questions 2 and 3 were used to determine which group the
annotator was placed in.
C.2
Screening Questions for mod
The subreddits used in these questions reflect the top-10 subreddits
selected during the process described in subsubsection 4.1.1. Partic-
ipants were only recruited for the task if they indicated that they
frequented one of the 3 communities selected in 4.1.2.
(1) Do you frequent any of the following subreddits? Check all
that apply.
• r/Coronavirus
• r/classicwow
• r/Games
• r/heroesofthestorm
• r/ShingekiNoKyoujin
• r/AmItheAsshole
• r/CanadaPolitics
• r/RPClipsGTA
• r/LabourUK
(2) Are you a moderator in any of the aforementioned subred-
dits?
• r/Coronavirus
• r/classicwow
• r/Games
• r/heroesofthestorm
• r/ShingekiNoKyoujin
• r/AmItheAsshole
• r/CanadaPolitics
• r/RPClipsGTA
• r/LabourUK

```
