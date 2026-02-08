---
title: "2025-Suh-SENSE-7 Taxonomy and Dataset for Measuring User Perceptions of - PDF Extract"
source_pdf: "2025-Suh-SENSE-7 Taxonomy and Dataset for Measuring User Perceptions of.pdf"
pages: 28
extracted_at: "2026-02-07T17:00:45.952419"
---

# PDF Extract: 2025-Suh-SENSE-7 Taxonomy and Dataset for Measuring User Perceptions of

**Source PDF:** 2025-Suh-SENSE-7 Taxonomy and Dataset for Measuring User Perceptions of.pdf
**Total Pages:** 28

---

## Content

```
--- Page 1 ---

SENSE-7: Taxonomy and Dataset for Measuring
User Perceptions of Empathy in Sustained
Human-AI Conversations
Jina Suh∗, Lindy Le†, Erfan Shayegani‡, Gonzalo Ramos∗
Judith Amores∗, Desmond C. Ong§, Mary Czerwinski∗¶, Javier Hernandez∗
Abstract—Empathy is increasingly recognized as a key factor
in human–AI communication, yet conventional approaches to
“digital empathy” often focus on simulating internal, human-
like emotional states while overlooking the inherently subjective,
contextual, and relational facets of empathy as perceived by
users. In this work, we propose a human-centered taxonomy
that emphasizes observable empathic behaviors and introduce
a new dataset, SENSE-7, of real-world conversations between
information workers and Large Language Models (LLMs), which
includes per-turn empathy annotations directly from the users,
along with user characteristics, and contextual details, offering
a more user-grounded representation of empathy. Analysis of
695 conversations from 109 participants reveals that empathy
judgments are highly individualized, context-sensitive, and vul-
nerable to disruption when conversational continuity fails or
user expectations go unmet. To promote further research, we
provide a subset of 672 anonymized conversation and provide
exploratory classification analysis, showing that an LLM-based
classifier can recognize 5 levels of empathy with an encouraging
average Spearman ρ = 0.369 and Accuracy = 0.487 over this
set. Overall, our findings underscore the need for AI designs that
dynamically tailor empathic behaviors to user contexts and goals,
offering a roadmap for future research and practical development
of socially attuned, human-centered artificial agents.
Index Terms—Human-Centered Digital Empathy, Empathy
Measurement, Human-Computer Interaction, Taxonomy, Dataset
I. INTRODUCTION
Empathy is broadly conceptualized as the ability to rec-
ognize, understand, and share one another’s emotions and
perspectives [1], [2]. Empathy is crucial to human commu-
nication and relationships, fostering trust, rapport, prosocial
behaviors, and mutual understanding [3], [4], [5]. Motivated
by the hypothesis that empathetic systems could lead to user
engagement and satisfaction, researchers in human-computer
interaction (HCI), human-robot interactions (HRI), and affec-
tive computing (AC) have explored how to embed empathic
capabilities into artificial intelligence (AI) or to endow com-
puting systems with “artificial empathy” [6]. Indeed, recently
developed Large Language Models (LLMs) can now produce
∗Microsoft Research. Corresponding author: jinsuh@microsoft.com,
gonzo.ramos@gmail.com,
judithamores@microsoft.com,
javierh@microsoft.com
†University of Michigan. lindyle@umich.edu
‡University of California, Riverside. sshay004@ucr.edu
§University of Texas at Austin. desmond.ong@utexas.edu
¶University of Washington. marycz1031@gmail.com
empathic responses that people rate as more empathic than
those written by humans [7], [8], [9], [10], [11], [12], [13].
There is a growing area of computing research around evalu-
ating and improving these models’ inherent “empathy” [14],
[15], [10], [16], [17], [18], [19]. At this juncture, re-examining
empathy conceptualization and evaluation in human-AI inter-
action becomes essential.
Early empathic AI efforts drew from psychological theo-
ries [20] to simulate human emotional and cognitive processes,
aiming to generate cues to make agents “as human-like as
possible” [21]. Prior studies modeled internal states and em-
ployed machine learning to convey empathic cues through
facial expressions, voice prosody, linguistic strategies, and
even haptic touch [22], [23], highlighting user benefits like
comfort, support, or companionship [24], [25], [26], [27],
[28], [29], [30], [31], [32]. However, such efforts frequently
overlooked the inherently subjective and contextual nature of
empathy perception and accuracy [33], [3], raising feasibility
and ethical concerns about objectively rating empathy from
third-party perspectives [34], [35], [36], [37].
A growing body of work argues that empathy in human-
AI interaction should instead be viewed as a dynamic, in-
teractional construct centered on user experiences rather than
AI’s internal states [38], [17]. This implies that the focus on
empathy should be about how it is demonstrated through the
AI’s behaviors and communication strategies, rather than on
any inherent features of the AI, like its ability to “feel” com-
passion. Empathic behaviors can serve multiple functions, such
as timely acknowledgments, context-sensitive clarifications,
supportive emotional feedback, or proactive assistance, where
each strategy might be employed at various points in a natural-
istic interaction. This shift in perspective also foregrounds and
necessitates the user’s subjective perception of empathy [39],
[40], as each strategy must be shaped in a way that resonates
with the user’s evolving goals, expectations, emotional states,
and social contexts during a prolonged interaction [41], [42].
Our work addresses gaps highlighted by this shifting per-
spective through a human-centered framework that emphasizes
tailoring AI empathic behaviors to individual contexts and
subjective perceptions. Our primary contributions are twofold:
(1) a multidimensional taxonomy of perceived empathic be-
haviors, which expands traditional cognitive and affective
empathy dimensions to include instrumental and exploratory
arXiv:2509.16437v1  [cs.HC]  19 Sep 2025

--- Page 2 ---

functions, reframed as interactional and observable behav-
iors in AI agents; and (2) a new human-centered digital
empathy dataset, SENSE-7 (Subjective Empathy in Natural
Sustained Exchanges; 7 dimensions), of English-based con-
versational interactions with general-purpose Large Language
Models (LLMs). The dataset consists of subjective accounts
of empathy from 695 real-world independent conversational
interactions from 109 information workers, including a range
of individual characteristics, contextual and emotional states
prior to and following interactions, per-conversation and per-
response assessments of perceived empathy, and user prefer-
ences regarding different empathic dimensions. As a secondary
contribution, we present an exploratory classification analysis
to demonstrate the utility of this taxonomy and dataset over a
subset of 672 fully anonymized conversations1.
From the evaluation of the data, we found that both indi-
vidual characteristics and conversational context significantly
influence perceptions of empathy in AI interactions. Partici-
pants with higher daily AI use interest and higher trait empathy
tended to select personal topics. Participants with higher
cognitive reappraisal scores rated their desired empathy level
lower when dealing with personal or work issues compared
to those with lower reappraisal scores. Analysis revealed that
even a single “poor” turn in a conversation substantially
diminished overall empathy ratings and correlated with lower
engagement outcomes, despite similar conversation lengths
across models. By operationalizing perceived empathy across
seven dimensions, we uncovered that users value nuanced
distinctions, particularly favoring cognitive understanding and
tailored responses. Participants’ explanations highlighted im-
plicit expectations beyond conversation context, highlighting
the challenges of predicting empathy perceptions from con-
versation alone. In this context, our exploratory classification
experiments show that incorporating conversational context
via adaptive-shot prompting strategy greatly enhanced the
accuracy of detecting perceived empathy, highlighting the
critical role of context in evaluating digital empathy. Together,
these findings underscore the complexity and subjectivity
of empathy perception in human-AI interaction. Our work
contributes a tangible toolset to the growing body of literature
advocating for a human-centered paradigm for conceptualizing
digital empathy, ultimately paving the way for AI agents that
can dynamically adapt their empathic demonstrations to better
meet the diverse needs of individual users.
II. RELATED WORK
Empathy has traditionally been studied in psychology [2]
and communication research, defined as the ability to rec-
ognize, understand, and share another’s emotional and men-
tal states. There are three general facets to empathy [33].
Two commonly distinguished facets are affective (e.g., emo-
tional resonance) and cognitive (e.g., perspective-taking) pro-
cesses [1], [43], with a third facet, prosocial motivation,
1To inquire about the dataset or how to obtain it, please reach out to
sense7data@microsoft.com
recently gaining more attention [33]. The Affective component
is largely concerned with feeling or resonating with someone’s
emotion [43], the Cognitive component is concerned with
understanding someone’s perspective or mental state [44],
[45], and the Motivational component [46], [47] drives action
or help [48], [49]. Beyond these broad facets, earlier works
on human empathy attempt to capture fine-grained dimensions
of empathy, such as comprehension [50], resonance or at-
tunement [51], [52], simulation [1], [50], [53], concern [52],
emotional contagion [1], [53], emotional sensitivity [50], phys-
iological response [50], compassion [48], self-awareness [54],
fantasy [1], emotional congruency [2],
or altruism [50]. In
addition, studies of human empathy tend to emphasize em-
pathy’s critical role in human relationships for building trust,
rapport, prosocial behavior, and mutual understanding [3], [4],
[5].
Motivated by these psychological studies, early affective
computing and human-computer interaction research sought
to imbue artificial systems with digital empathy-like qualities.
Pioneering research treated empathy as something that could
be simulated or added to AI systems by modeling human-
like internal emotional states and expressing them through
nonverbal and verbal cues [6]. Social robots and embodied
conversational agents attempted to convey empathy via facial
expressions, gestures, voice prosody, haptic touch, or affective
language to improve user comfort, trust, engagement, and
prosocial action [55], [56], [57], [58], [32], [23]. For instance,
systems designed to detect user emotions and respond with
congruent affective displays have demonstrated several bene-
fits. These empathic responses can enhance user experience,
maintain social and emotional bonds with users across vari-
ous domains including mental health support, education, and
companionship [24], [25], [26], [27], [28], [29], [30], [31].
Contemporary research on digital empathy centers on how
empathy can be conceptualized, operationalized, and evaluated
in human-machine communication [37], [18]. Although digital
empathy is inspired by insights in human empathy, it is
important to note that empirical work on human empathy often
treats empathy as a stable internal state that can be measured
through self-assessment scales given to the empathizer. Few
methods try to measure empathy through observation (e.g.,
by the recipient or by a third-party rater), especially in
human-human interaction contexts where empathy is deemed
more important, such as provider-patient interactions [52].
Most empathy scales (given to the empathizer) use first-
person statements such as “I sometimes find it difficult to
see things from the other guy’s point of view [1]” or “It
upsets me to see someone being treated disrespectfully [50].”
Such self-report methods are difficult to apply directly to
AI because we cannot meaningfully interview or assess a
system’s “trait empathy”. Moreover, people also vary widely
in their empathic capacities and accuracies. Even within a
single person, empathy fluctuates based on context, motivation,
or interpersonal dynamics [33], [47], [3]. Therefore, some
argue that directly applying human psychological trait models
to AI and replicating human internal states in AI may be

--- Page 3 ---

problematic.
Individual differences (e.g., personality traits, cultural back-
ground, prior experiences) and contextual factors (e.g., the
nature and goals of an interaction, emotional states) crucially
shape how empathy is perceived and enacted [33], [1], [59].
In human-agent interactions, the relational and social role of
empathy is more relevant than its manifestation as psycholog-
ical traits for developing rich insights about users and helping
address their needs, and this role of artificial empathy is highly
contextual [38]. In addition, focusing on internal states can
lead to anthropomorphizing AI systems, imputing them with
the capacity to feel in human-like ways, which raises ethical
and conceptual concerns [60]. Instead, scholars emphasize that
empathy should be viewed as an interactional or relational
phenomenon, realized through observable, context-sensitive
behaviors rather than presumed internal mental processes [60],
[38], [17].
In recent efforts to develop conversational AI agents with
empathy, scholars have adapted empathy dimensions from psy-
chology and applied them in third-person annotation schemes,
where crowdworkers or experts label the presence of empathic
cues in dialogues as a scalable way to build training data [61],
[36], [27], [62], [63], [64]. This line of work has also moti-
vated the development of numerous taxonomies to characterize
empathic responses or intents in human-AI dialogues. For
instance, Welivita and Pu [65] propose a large-scale taxonomy
that highlights different empathy dimensions (e.g., emotional
support, cognitive validation), while Svikhnushina et al. [66]
demonstrate how questions that express interest or concern
about a user’s emotional state can be pivotal for perceived
empathy. Sharma et al. [62] operationalizes empathy into emo-
tional reaction, interpretation, and exploration. Increasingly,
LLMs that power conversational agents are considered not
only as the subject of evaluation but also as the evaluator
itself [64]. For example, Kumar et al. [67] evaluates the reli-
ability of LLMs as judges for empathic communication using
expert and crowd annotations consisting of these datasets.
While these approaches have advanced the field, third-person
labeling can neglect the subjective user experience (so-called
second-person or participant viewpoint). Directly obtaining
feedback from the actual interactant on whether the agent was
empathetic in that moment is the most ideal, but such methods
pose practical challenges in data collection and experiment
design [36].
A parallel stream of work has produced multi-turn and
conversation-level empathy datasets since empathy in con-
versation often unfolds over multiple turns, where a user’s
emotional state and the agent’s responses evolve dynami-
cally [38]. Each work leverages unique annotation schemes
that emphasize different aspects of empathy in conversations.
EmpatheticDialogues [61] collects crowdworker ratings of in-
dividual utterances. EPITOME [62] captures seeker-responder
pair annotations with highlighted rationales, ESConv [68]
labels support strategies and outcomes, Xu and Jiang [63] cap-
ture intent-empathy mappings from both speaker and listern
perspectives, and Shen et al. [69] gather empathy ratings at
the narrative level toward full stories authored by humans or
AI. These diverse approaches illustrate the variety of ways
empathy has been operationalized, while also leaving open
opportunities to examine how perceptions of empathy evolve
across turns in ongoing conversations.
Our work builds on this shift in perspective towards a
human-centered approach to digital empathy that prioritizes
empathy’s functional role within interactional contexts [70]. To
capture this more accurately, our dataset provides both per-turn
and per-conversation empathy judgments within multi-turn
dialogues directly from the interactant, including contextually
relevant signals, such as participants’ current mood, expec-
tations, and trait characteristics. This design enables analysis
of how empathy unfolds across conversations, how a single
turn can shape subsequence perceptions, and how the broader
interactional context influences empathic perception.
III. AI EMPATHIC BEHAVIOR SCALE
Instead of emulating human empathy as an abstract concept,
our goal is to apply understandings of human empathy in a
way that is grounded in a particular human-AI interaction,
tailoring AI’s empathic behaviors to individual users and
contexts. To achieve this human-centered approach to digital
empathy, we first reframe traditional theories of cognitive and
affective empathy in psychology as interactional, behaviorally
observable phenomena in AI agents. Second, in addition to
observable human-AI behaviors, we capture external factors,
such as an individual’s empathic accuracy or context, because
these unseen external factors comprise the backdrop of em-
pathic human-AI interactions. Here, we describe development
process of our empathic behavior scale. In our study, we use
this scale in combination with individual characteristics and
contextual factors to understand how AI behaviors unfold and
are perceived as empathic by humans. Our scale is designed
to measure text-based LLM behaviors, and we leave the
extension of this scale to other modalities to future work.
We followed several steps during our development of a mul-
tidimensional AI empathic behavior scale. First, we gathered
existing psychology and neuroscience literature that defined
components in human empathy (e.g., [49], [2], [48]) as well
as scales that measured human empathy (e.g., [51], [1], [71]).
We also reviewed literature that examined applications of
empathy in AI agents or robots (e.g., [25], [72]) and scales
that directly or indirectly measured empathy (e.g., [73], [62]).
These earlier works each had similar but unique ways of
defining empathy components. Based on a social cognitive
neuroscience understanding of empathy, the Empathy Assess-
ment Index [71] introduced five important components for
empathy: Affective Sharing, Self-Awareness, Perspective Tak-
ing, Emotion Regulation, and Empathic Action. For empathy
in everyday life, Depow et. al. [48] described the three dis-
tinct components of empathy as Emotion Sharing, Perspective
Taking, and Compassion. Outlining a computational model
of empathy, Yalcin and DiPaola [72] defined Communication
Competence, Emotion Regulation, and Cognitive Mechanisms
as three main components of empathy, along with mechanisms

--- Page 4 ---

(e.g., Emotion Recognition, Theory of Mind) and behaviors
(e.g., Empathic Concern, Altruistic Helping) associated with
each component. Supplementary Tables S1 and S2 enumerate
all scales and articles we reviewed and the concepts introduced
by them.
From these works, we extracted individual scale items,
empathy concepts, and their descriptions. Once we gathered
all concepts mentioned, two authors manually conducted
a conceptual mapping exercise (i.e., affinity diagramming
and clustering based on conceptual similarity), where we
found many smaller dimensions (e.g., resonance, congruency,
perspective-taking, altruism), as enumerated in Supplementary
Tables S1 and S2. We further grouped them into three high-
level categories—Affective (emotions), Cognitive (thoughts),
and Motivational (intentions to help)—and extracted 7 unique
dimensions as follows.
Rather than describing empathic agents in terms of emo-
tions, thoughts, and motivations that are not “traits” in artificial
agents, we instead reframed three main concepts in terms
of definable components of computing systems: their inputs,
functions applied to that input, and outputs. As technology
users do not have access to the algorithms underlying AI
agents, we instead capture the observable components from the
human perspective: the inputs and outputs. Thus, the Affective
and Cognitive empathy components are about whether the
emotional and mental signals from the human (i.e., input to
the agent) are accurately identified and interpreted by the
agent and whether the response produced by the agent (i.e.,
output of the agent) meets the human’s expectations (Affec-
tive Understanding and Cognitive Understanding). Likewise,
we reframed the Motivation empathy component away from
possibly making judgments about agent intentionality, and
instead broke it down into three observable behaviors regard-
ing assistance that showed up as predominant themes in the
affinity diagram: the actual response (Response Appropriate-
ness), supportive behavior (Prosocial Expression), and actions
signaling attunement (Interest). We included two additional
dimensions under Motivation empathy to capture behaviors
that demonstrate sustained effort through memory (Relational
Continuity) and relevance (Contextual Understanding) for the
following reasons. An interaction between the human and the
agent is often multi-turned, composed of an ongoing loop
of these inputs and outputs. This dynamic and constantly
evolving aspect of empathy [74] is captured by the Relational
Continuity dimension. Moreover, the interaction between the
human and the agent is situated within a broader social
environment; Contextual Understanding describes the specific
setting within which empathy occurs [49].
A. Affective Understanding
Affective understanding refers to an AI agent’s ability to
accurately sense and understand the human’s emotional state.
This abilty aligns closely with affective empathy or emotional
empathy in human psychology as “the ability to accurately
recognize others’ feelings and understand the meaning of these
feelings” [78], [48], [2]. When people believe their emotions
are recognized, it creates a feeling of validation and emotional
safety [79]. Affective understanding is also a dimension that
is most commonly studied and modeled as representative of
empathy in NLP [36], [27], [63].
Unlike human affective empathy where there is an emphasis
on internal mirroring of feelings (i.e., resonance [43], [33]),
in our taxonomy it is irrelevant that the agent has an internal
mechanism to resonate emotionally. But it is still important
that the user perceives that the agent is aware of and sensitive
to the user’s emotions, and this dimension focuses on whether
the user perceives behavior showing that the agent correctly
understands their feelings. We keep this focus on observable
behavior through the rest of the dimensions, below.
B. Cognitive Understanding
Cognitive understanding refers to the ability of the AI agent
to comprehend the human’s perspective, intentions, and mental
states. In human psychology, this aligns closely with cognitive
empathy–a concept grounded in perspective-taking or theory
of mind [80], [75], [46]. Cognitive empathy is described as
the capacity to mentally put oneself in someone else’s shoes
to understand their point of view [1]. In the human-AI context,
this dimension refers to the agent’s demonstration that it grasps
the reasons behind the user’s feelings, the content of their
concerns, or situations through paraphrasing what has been
shared or reflecting meaning.
C. Response Appropriateness
Response appropriateness involves the AI agent’s capacity
to generate adaptive and context-sensitive responses. Aligning
prior research on therapist empathy [52] and dialog systems
research [76], response appropriateness is not just about rec-
ognizing emotions or points of view but about matching that
recognition with a response that is both tactful and supportive.
It requires the agent to decide when to listen, validate, offer
advice, or take another form of action that aligns with the
user’s needs. In embodied agents, this could involve the
expression of nonverbal cues that are contextually appropriate.
D. Prosocial Expression
Prosocial expression involves the motivational aspect of em-
pathy, especially the AI agent’s desire to help and care for the
user. In human psychology, this may be similar to motivational
empathy [33], empathic concern [1], [51], or caring [75], [46].
Although AI agents may not have internal mechanisms to
feel concerns or care for humans, this dimension concerns the
user’s perception about AI’s outward display to do something
(i.e., responses and actions) that seems supportive, caring, and
helpful. It captures the extent to which the AI’s expressed
empathy is active and human-oriented. In embodied agents,
this could involve nonverbal actions like comforting touches
when a human is upset or offering tissues.
E. Interest
Interest reflects an AI agent’s active engagement in the
ongoing interaction and curiosity regarding the user’s expe-
riences. Prior research has shown that empathy is a dynamic

--- Page 5 ---

TABLE I
DIMENSIONS OF DIGITAL EMPATHY AND EXAMPLE AI BEHAVIORS.
Dimension
Description
Examples
Affective
Affective
Understanding
(e.g., [48], [2])
The agent demonstrates the ability to recognize and
understand my emotions/feelings.
“I can sense you’re feeling anxious right now. It’s
understandable to feel this way.”
“I hear the frustration in your voice—I’m sorry you’re going
through that.”
Cognitive
Cognitive
Understanding
(e.g., [75], [46])
The agent demonstrates the ability to recognize and understand
my perspective/point of view, including goals and intentions.
“So your main goal is to change careers—let’s consider your
interests and experiences.”
“I see where you’re coming from; you want to ensure
everyone’s on the same page.”
Motivational
Response
Appropriateness
(e.g., [52], [76])
The agent demonstrates the ability to appropriately respond
and adapt to my experiences, including when to provide
advice or solutions.
Rather than offering solutions directly, AI offers options:
“That sounds very challenging. Would you like help
identifying strategies or just talk through...?”
“That sounds tricky. If you’re open to it, I can offer a few
different perspectives.”
Prosocial
Expression
(e.g., [51], [75])
The agent demonstrates a concern for and a desire to help me.
“I want to do everything I can to support you through this.”
“I really care about your well-being and want you to feel
better.”
Interest
(e.g., [74], [52])
The agent demonstrates curiosity and attention toward my
experiences.
“That’s fascinating—tell me more about how you got
interested in this topic.”
“I’m genuinely curious about what led you to this point in
your journey.”
Contextual
Understanding
(e.g., [49], [74])
The agent demonstrates the ability to consider my unique
circumstances (e.g., goals, beliefs, history, personality,
preferences) and contextualize my experiences within broader
external factors (e.g., culture, politics, social barriers, etc.).
“Given your cultural background and past experiences, I can
see how this might affect your decision.”
“Because you’ve told me you value honesty and clarity, I’ll
explain this in detail.”
Relational
Continuity
(e.g., [77], [52])
The agent demonstrates the ability to maintain and enrich the
relationship by consistently recalling and weaving details and
nuances from past interactions into present exchanges,
cultivating a dynamic and personalized rapport over time.
“Last time we spoke, you mentioned a big presentation—how
did it go?”
“I remember you were worried about your project deadline.
Did you manage to wrap it up?”
process that unfolds over time [74], and the act of active listen-
ing and learning more about the other person builds a stronger
connection and bonding and improves perception of empathy
and relational warmth [75], [52], [79]. Displaying such interest
in a conversational partner is also an important component of
active listening [81]. In human-AI contexts, this could involve
AI agents asking follow-up questions to explore [62] or pro-
viding back-channel cues (e.g., head nods, brief responses like
“uh-huh” [82]) to demonstrate its engagement and to emulate
active listening. Interest behaviors, therefore, demonstrate that
AI agents have been paying attention.
F. Contextual Understanding
Contextual understanding pertains to integrating the user’s
broader background, such as personal history, cultural context,
and preferences, into the empathic process. Empathy goes be-
yond emotions and perspectives; it depends on circumstances
that form the situation under discussion [49], [75] as well as
the relationship between the parties involved [74]. Context sets
the common ground between the human and AI, which is
important for AI to appropriately interpret and make sense
of signals. Context is often not visible in the ongoing human-
AI interaction but must be explicitly accessed and modeled as
external knowledge [83].
G. Relational Continuity
Relational continuity focuses on the temporal aspect of
empathy and refers to the sustained, consistent empathic
connection across multiple interactions, building a relationship
rather than a one-off exchange. In counseling settings,
therapeutic alliance has been shown to be important for
improved perception of empathy and health outcomes [77],
[52]. This is because providers accumulate knowledge about a
patient that enables them to demonstrate a pattern of empathic
attunement and genuine care. Similarly, in human-AI contexts,
forming a working relationship can lead to better adherence
to interventions, engagement, and user satisfaction [84]. This
dimension underscores the importance of memory for the
accumulation of knowledge and continuity of interactions
over time and across multiple interactions [74], [83].
As an initial attempt at developing this scale, we formulated
a single statement for each dimension. These 7 dimensions
form the core of our AI Empathic Behavior Scale, which

--- Page 6 ---

we leverage and validate in our study. Table I presents these
statements along with examples.
IV. HUMAN-CENTERED EMPATHIC CONVERSATION DATA
COLLECTION
In the previous section, we defined 7 components of digital
empathy, focusing on the interactional nature of empathy and
various behavioral forms it can take in AI agents. In addition to
the multidimensional aspects of empathy, contexts, especially
individual characteristics, are important to consider when
evaluating empathic behaviors of AI agents. For example,
previous research has shown that people with a high empathic
trait tend to have better empathic accuracy (i.e., their ability
to perceive others’ emotions and empathic responses) [3],
[85]. Individuals’ regulatory processes (i.e., emotion regulation
skills) shape how we perceive and respond to emotions in
others, which are key parts of empathy and interpersonal
dynamics [86]. Individuals’ attitudes towards AI may also
influence how they interact with the AI (e.g., disclose private
information) and rate AI’s responses [87], [88].
To evaluate our taxonomy and to understand how interac-
tions with various AI systems can be perceived differently
along empathy dimensions by different individuals, we con-
ducted a study with 151 participants who engaged with the
study’s AI agent and assessed their perception of empathic
behaviors in their assigned AI agent. To see how different
AI agents and their behaviors would impact individual per-
ceptions, we randomly assigned participants in a single-blind
design to one of four different AI agents (built on top of GPT-
3.5-turbo, GPT-4, or Llama2-70b; see Section IV-B). In each
conversation, we obtained first-person and per-turn labels of
empathy that enable investigation into within- and between-
individual differences in the multidimensional perception of
empathic behaviors in conversational AI. In addition, to further
encourage more naturalistic conversation where individual
differences will be drawn out, we conducted the study in real-
world settings where individuals naturally incorporated the AI
into their everyday situations. In this section, we describe the
study design and data collection.
A. Study Procedure
We sent recruitment emails to a random sample of em-
ployees of a large technology company for their interest
in participating in our study and enrolled participants on
a first-come-first-served basis. Our study consisted of three
main stages. (1) At intake, each participant completed an
intake survey that captured their demographics and psycho-
metrics (Section IV-A1). (2) Within the study period that lasted
approximately 4 weeks, participants were asked to engage in
at least 5 distinct conversations with an assigned AI agent
whenever they felt the need for AI assistance (Section IV-A3).
(3) At exit, each participant completed an exit survey to reflect
on their overall study experience and perceptions of empa-
thy (Section IV-A4). Our study employs a repeated-measures
design in capturing multiple conversations and empathic per-
ceptions per participant. It also employs a between-subjects
design where each participant was assigned to one of the four
different AI agents. Each participant that completed the intake
survey, 5 conversations, and the exit survey was compensated
with a $50 USD gift card. For each additional conversation,
we compensated $10 USD for a total compensation of up to
$100 USD per participant. The study was approved by the
Microsoft Research Institutional Review Board.
1) Intake survey: The intake survey captured participants’
demographics, such as age, gender identity, job function,
highest attained education level, and whether English was
their first language. We also captured psychometrics that may
influence how individuals may interact with and perceive the
AI agent. First, we captured the individual’s empathic trait
using two validated scales: (1) Single Item Trait Empathy
Scale (SITES) [89] and (2) Toronto Empathy Questionnaire
(TEQ) [50]. Second, we captured the individual’s emotional
regulation skills using the Emotion Regulation Questionnaire
(ERQ), with two subcomponents (cognitive reappraisal and ex-
pressive suppression) [90]. Third, we captured the individual’s
attitude towards AI using a combination of scales that were
adapted for our study: (1) AI Attitude Scale (AIAS-4) [91]
which were mostly positively framed, (2) top two positive
and two negative items with the highest factor loadings from
the General Attitudes towards Artificial Intelligence Scale
(GAAIS) [92], and (3) our own statements (“I trust AI” and “I
would disclose personal information to AI”) to capture attitude
towards disclosure to AI. All AI attitude statements were
answered on a 5-point agreement scale (1: Strongly disagree,
5: Strongly agree).
2) AI assignment: We used data from the intake survey
to conduct block randomization in assigning AI agents. In
other words, we randomly distributed eligible participants
while maintaining balance across four AI agents. We used
four variables for block randomization: gender, AI attitude,
TEQ, and expressive suppression subcomponent of ERQ. For
AI attitude, TEQ, and expressive suppression, we used the
median value to divide participants into high or low groups.
Chi-square test of independence and ANOVA test revealed
no significant difference across AI assignments along gender,
SITES, TEQ, both subcomponents of ERQ, and AI attitude.
Participants were blind to the AI assignment, and they were
required to use the same AI agent for all of their subsequent
conversations.
3) Conversation task: After intake, participants were pro-
vided with instructions detailing how to access and interact
with the AI agent, how to complete pre-conversation and post-
conversation surveys, and how to label AI agent responses.
Each participant was asked to engage in 5 or more conver-
sations with their assigned AI agents for approximately 5 to
10 minutes. For participants’ convenience, we sent a daily
reminder with a link to the conversation task accessible via a
browser. The conversation task consisted of 4 stages: (1) pre-
conversation survey, (2) conversation interface, (3) per-turn
labeling interface, and (4) post-conversation survey.
a) Pre-conversation survey: When the participant en-
tered the conversation task, we captured momentary informa-

--- Page 7 ---

tion about the participant before engaging with the AI agent.
We asked participants to choose the topic of assistance needed
among 9 topics grouped into 3 topic categories: information
tasks (“I need help thinking through a work assignment”, “I
need help with writing”, “I need help learning a new skill”, or
“I need help with a personal task”), personal issues (“I need
help overcoming a personal issue”, “I need help navigating
a distressing situation”, or “I need help navigating a social
situation”), and work-related issues (“I need help thinking
through a work issue” or “I need help thinking through a
career/self-improvement problem”).
We instructed participants to engage in a variety of topics,
and to promote topic diversity, we showed the count next to
each topic. We then asked them to write the task description
and rate its importance (1: Not at all important, 5: Extremely
important). We presented the definitions of the 7 empathy
dimensions and asked them to rate their desired empathy level
for the task (1: minimal, 2: moderate, 3: high) with an optional
field to capture any comments about their desired level of
empathy. Finally, we asked them to assess their current mood
through a 10-item international Positive and Negative Affect
Schedule (I-PANAS-SF) [93].
b) Conversation interface:
After submitting the pre-
conversation survey, participants were shown a text-based
conversational chat interface (Supplementary Figure S1). Par-
ticipants were responsible for initiating the conversation with
the AI agent. The interface included a text input box, a button
to send the text, a loading indicator, and a scrollable window
for showing the conversation history. There were no other
functionalities to keep the interface as simple as possible.
Participants could terminate the conversation by clicking on
“I’m done” to navigate to the next stage of the task.
c) Per-turn labeling interface: After the conversation, we
asked participants to label each of the AI responses for its
overall demonstration of empathy, and along 7 dimensions, as
shown in Figure 1. Empathy labels ranged from ‘Very poor (1)’
to ‘Very good (5)’, with an option for ‘N/A’ to indicate that
empathy or a specific dimension of empathy is not relevant
for that response. Participants were required to label all AI
responses before proceeding to the next stage.
d) Post-conversation survey: Lastly, we asked partici-
pants for their momentary mood again using I-PANAS-SF. We
also asked participants to rate their conversational experience
on whether they successfully completed the task, whether
they were engaged or absorbed in the conversation, whether
the interaction was positive, and whether they would use
the agent again for the same task (1: Strongly disagree, 5:
Strongly agree). We concluded the task by asking their overall
perception of the agent’s empathy along 7 dimensions and
optional examples that justify their ratings.
4) Exit survey: Questions in the study’s exit survey were
mostly open-ended. We first asked participants to reflect on
their experiences to comment on whether their desired level
of empathy in AI agents has changed over the course of
the study. We asked participants to rank the 7 empathy
components based on their importance overall, as well as
Fig. 1. Per-turn labeling interface by the conversation participant
their importance specifically in the context of personalization–
that is, which components were most essential to tailor to
individual users. Finally, we asked participants to share their
thoughts on designing AI agents to simulate or express human-
like emotions, as well as designing AI agents to have human-
like empathy.
B. Conversational AI agent
Our study used four different LLMs. For the first instance
(referred to as ‘GPT4’), we used Azure OpenAI’s GPT-4 de-
ployment (GPT-4-32k version 0613). For the second instance
(referred to as ‘GPT4-empathy’), we used the same GPT-
4 deployment with a system prompt, designed to encourage
the agent to be more empathic, including reflective ques-
tions based on the 7 dimensions of empathy (Supplementary
Table 1). For the third instance (referred to as ‘Llama2-
70b’), we used Llama2-Chat-70B version hosted on Azure.
For the fourth instance (referred to as ‘IC’), we used GPT-
3.5-turbo, where each turn was preceded with a prompt to
extract the user’s evolving intent and information to remember
(e.g., memory) which was then provided as additional context
to generate the best response. All instances used similar
settings, such as a temperature of 0.1 and top-p of 0.9.
C. Study population
From our call for participation, 247 people expressed inter-
est and consented to participate in the study, and 197 partici-
pants completed the intake survey. Of the 197 participants, 151
participants submitted at least one conversation, and 109 par-
ticipants submitted at least five conversations and completed
the exit survey. From these 109 participants, we obtained 695
fully labeled conversations. Of 109 participants, 55 identified
as men, and 54 identified as women. 33 participants (30.3%)

--- Page 8 ---

were aged 26–35 years, 31 (28.4%) were 46–55 years, 24
(22.0%) were 36–45 years, 10 (9.2%) were 56–65 years, and
8 (7.3%) were 18–25 years old, with 3 (2.8%) preferring not to
disclose their age. 46 participants (42.2%) had a Bachelor’s de-
gree as their highest education level, 43 (39.4%) had a Master’s
degree, 10 (9.2%) had some college or vocational training,
5 (4.6%) had doctoral or professional degrees, and 2 (1.8%)
had some postgraduate degree, with 3 (2.8%) preferring not
to disclose their education. 81 participants (71.3%) indicated
that English was their first language. The three largest role
categories were software development and engineering (42,
38.5%), business and finance (27, 24.8%), and product and
project management (19, 17.4%), with others including data
analytics, research, design, administration, and support roles.
Based on psychometrics data captured from the intake sur-
vey, participants self-assessed that they were highly empathetic
(¯x=4.37 out of 5, σ=0.66), although the average TEQ score
(¯x=41.0, σ=7.12) indicates lower empathy compared to the re-
ported means in the original scale development (¯x=46.25 [50]).
The distribution of ERQ scores confirms prior research [91],
where we saw statistically significant gender differences for
expressive suppression but not for cognitive reappraisal. In our
study population, men suppressed emotions more than women
(¯xman=3.85, ¯xwoman=3.25 out of 7, t(107)=2.82, p=0.006). The
average cognitive reappraisal scores were 5.13 (σ=0.91) out
of 7 for men and 5.23 (σ=0.94) for women. The average AI
attitude leaned towards positive (¯x=3.78 out of 5, σ=0.47),
with statistically significant gender differences (¯xman=3.96,
¯xwoman=3.61 out of 5, t(107)=2.82, p≪0.001). Potential over-
representation of tech workers may have contributed to a skew
toward positive AI attitudes.
D. Analysis
1) Quantitative: For quantitative analysis, we employed
various
statistical
methods
using
Python
and
its
li-
braries (e.g., pandas, scipy, statsmodels, pingouin,
seaborn). When modeling for binary outcomes (e.g., partic-
ipant chose a Personal Issue), we used a population-averaged
Generalized Estimating Equations (GEE) model while ac-
counting for the within-participant correlation by clustering on
participant ID and leaving model assignment, individual char-
acteristics, and contextual factors as fixed variables. We used
linear mixed-effects models to understand the contribution
of fixed variables (e.g., individual characteristics, contextual
factors) on various outcome variables (e.g., desired empathy,
perceived empathy), treating participant identifiers as random
variables. When reviewing differences in means across groups,
we used t-tests for two groups and ANOVA tests for three or
more groups. We used the Benjamini-Hochberg procedure for
controlling the False Discovery Rate (FDR) and to correct
for multiple comparisons. Where applicable, we conducted
the Tukey Honest Significant Difference (HSD) procedure
for pairwise comparisons. We calculated consistency across
variables using Cronbach’s alpha, agreement between two
variables using Cohen’s Kappa, effect sizes using Cohen’s
alpha, and correlations using Pearson’s r.
2) Qualitative: To understand how each empathy dimen-
sion is demonstrated well or poorly, one author prioritized
and qualitatively reviewed conversations with low or high
empathy ratings in conjunction with the subset of participants
who provided optional comments. The second author reviewed
and confirmed qualitative interpretations of the comments.
Because comments were not required, our analysis does not
aim for thematic saturation, but instead uses these comments
as illustrative cases that clarify how participants interpreted
chatbot behaviors and how these interpretations informed their
ratings. Participant comments were crucial to validate our
observations of the conversation and to uncover misaligned
expectations. For analyzing exit survey responses, the same
author reviewed the open-ended responses using reflexive
thematic analysis [94], specifically focusing on highlighting
diverse rationales for why certain empathy dimensions were
perceived to be important, rather than claiming comprehensive
coverage of all perspectives.
3) Perceived Empathy Recognition: To evaluate the fea-
sibility of automatically measuring perceived empathy at a
conversation level, we explored the use of a simple LLM based
classifier with the GPT 4o Azure OpenAI service (api version
2024-10-21). The prompt included in Supplementary Table
S4 was structured in three parts. First, a goal definition
focused on analyzing the quality of the assistant responses
in context. Second, an empathy description that incorporated
the seven dimensions and their definitions in Table I. Third,
a five point rating guide as shown in Figure 1. To promote
deterministic behavior we set top p to 1.0 and set temperature,
presence penalty, and frequency penalty to 0.0.
To obtain the ground truth of perceived empathy, we first
estimated the empathy level for each turn by averaging the
seven turn level dimensions, which yielded one score per turn.
We then computed the average of these scores to estimate the
perceived empathy at a conversation level. The score range
covered the full scale with minimum 1 and maximum 5. To
ensure potential replicability, this part of the analysis was
performed over a smaller subset of 672 conversations that
could be fully anonymized. The remaining 23 conversations
were deemed too sensitive and difficult to anonymize while
preserving the semantic meaning of the conversation such
as participants sharing confidential information or iteratively
refining personal emails (see Supplementary Section 4 for
further details on the anonymization process). The final set
of anonymized conversations that are shared with this paper
contained N = 672 conversations distributed as follows. Very
Poor = 5, Poor = 15, Neutral = 48, Good = 290, and Very
Good = 314.
We evaluated performance by computing Mean Absolute
Error (MAE) and Spearman correlation using the contin-
uous predictions. We then rounded predictions and labels
to compute and report Accuracy, Macro Sensitivity, Macro
Specificity, and Macro F1. To quantify model variability,
predictions for all conversations were obtained ten times and
results were reported as mean and standard deviation across
runs. Part of the results include a regression scatter with a 95%

--- Page 9 ---

prediction interval that was computed using the standard linear
regression prediction interval approach with a critical t value,
residual standard error, sample size, and a leverage term. In
addition, we also provide the empirical cumulative distribution
of the absolute level gap D = |ˆy −y| over {0, 1, 2, 3, 4}.
The full conversation context was passed to the model and no
truncation was necessary. The goal of this analysis was not to
propose a state of the art classifier, but to assess the feasibility
of empathy classification using context sensitive prompting.
V. RESULTS
We organize our findings from this data into four sections.
We first analyze how individual and contextual differences
influence perception of empathy (without going into the
conversation) (Section V-A). We review the conversations
qualitatively to understand how empathy dimensions show
up (Section V-B). We then analyze exit survey responses to
understand the role of empathy dimensions in AI systems (Sec-
tion V-B3). Finally, we provide some results in the context of
perceived empathy recognition in conversations (Section V-C).
A. What factors influence perceptions of empathy?
Our quantitative analysis of post-task perceived empa-
thy examines pre-task factors (e.g., conversation topics, de-
sired empathy levels, task importance), conversational factors
(e.g., conversation length, turn-by-turn empathy rating), and
combines these with static factors (e.g., individual characteris-
tics, model types) to model the influence on post-task empathy
ratings. We leave more in-depth analysis of the conversational
dynamics and styles for Section V-B.
1) Conversation topics and user expectations: Before en-
gaging in a conversation with the chatbot, we asked par-
ticipants to categorize the conversation into one of three
categories (information, personal, work) based on assistance
needed. Of the 695 conversations, 43.7% were information
tasks, 30.4% were personal issues, and 25.9% were work-
related issues.
From our GEE analysis of choosing personal issues, we
found that, on average across participants, those with higher
daily AI use interest (β = 0.27, p = 0.021, OR ≈1.31) and trait
empathy (β = 0.30, p = 0.042, OR ≈1.35) were more likely
to pick personal issues on average, whereas those perceiving
organizational AI use as unethical (β = -0.19, p = .016, OR
≈0.82) or expressing greater willingness to disclose personal
information (β = -0.13, p = .042, OR ≈0.87) were less likely
to do so.
For work issues, we found that on average, the participants
who were significantly more likely to choose a work issue
were those in the 46–55 age group (β = 0.68, p = .047, OR
≈1.96), those preferring not to disclose their age (β = 1.23,
p = .003, OR ≈3.41), those who perceive organizational AI
use as unethical (β = 0.49, p < .001, OR ≈1.64), those who
plan to use AI (β = 0.58, p = .002, OR ≈1.78), and those
willing to disclose personal information (β = 0.17, p = .047,
OR ≈1.18). In contrast, the participants who were less likely
to select a work issue on average were those presented with
1
Minimal
2
Moderate
3
High
Personal Issue
Work Issue
Information Task
Pre-Task Desired Empathy
1
Not at all
2
3
Moderately
4
5
Extremely
Pre-Task Importance
5
10
15
20
25
Personal Issue
Work Issue
Information Task
Pre-Task Positive Affect
5
10
15
20
25
Pre-Task Negative Affect
Fig. 2.
Desired empathy, importance, and mood per conversational topic.
Affect scale ranges from 5 to 25, with 25 representing the max amount of
that affect type.
the ‘llama2-70b’ model (β = -0.50, p = .002, OR ≈0.61),
those who believe AI applications are beneficial (β = -0.27,
p = .026, OR ≈0.76), those who trust AI (β = -0.28, p = .039,
OR ≈0.75), and those higher in trait empathy (β = -0.58,
p < .001, OR ≈0.56). We note that conversations with
‘llama2-70b’ for work issues had the lowest average post-
empathy rating, although only significantly lower compared
to ‘GPT4-empathy’ in pairwise comparisons. Linguistic differ-
ences across models [10] may have contributed to the selection
and perception of empathy.
For information tasks, we found that participants in the
26–35 age group (β = -0.54, p = .007, OR ≈0.58), those
aged 46–55 (β = -0.55, p = .001, OR ≈0.58), and those
who preferred not to report their age (β = -1.20, p = .002,
OR ≈0.30) were less likely to select an information task,
on average. Additionally, participants who believed that AI is
positive for humanity (β = -0.20, p = .046, OR ≈0.82) or
that organizations use AI unethically (β = -0.16, p = .049, OR
≈0.85) also showed lower odds of choosing an information
task. These findings suggest that individual characteristics and
model types do influence people’s choice of conversational
topics.
We found statistically significant differences across the three
conversational topic areas in terms of the desired empathy
level, perceived importance of the conversation, and negative
affect before the conversations (Figure 2). When we looked at
how individual characteristics and topic choice influenced the
desired level of empathy, task importance, and mood for the
conversation about to be had, we generally found that partici-
pants who included personal or work issues experienced higher
emotional intensity, saw the conversation as more important,
and sought more empathy. Specifically, participants who were
older (26–35: β=0.397, p=.003; 46–55: β=0.309, p=.024; 56–
65: β=0.312, p=.048), those who chose a personal (β=0.679,
p<.001) or work (β=0.408, p<.001) issue, and those believing
AI applications are beneficial (β=0.153, p=.035) reported
higher desired empathy. Those tackling a personal (β=0.236,
p=.004) or work (β=0.302, p<.001) issue perceived the task as
more important, whereas higher trust in AI (β=-0.243, p=.030)
corresponded to lower importance. Choosing a personal is-

--- Page 10 ---

sue (β=-0.622, p=.026) was associated with lower positive
affect. Participants tackling personal (β=1.621, p<.001) or
work (β=1.115, p<.001) issues showed heightened negative
emotions. Higher cognitive reappraisal was associated with
higher positive affect (β=0.907, p=.041) and lower negative
affect (β=-0.623, p=.011).
We then looked at what individual characteristics may
moderate the relationship between the topic choice and the
desired empathy level. In addition to the main effect of
topic choice, we found that participants with higher scores
in cognitive reappraisal tend to desire slightly more empathy
from AI systems across all types of tasks (β=0.107, SE=0.051,
p=0.037). Among interaction terms, we found a negative
interaction between personal (β=-0.151, SE=0.067, p=0.024)
or work issues (β=-0.160, SE=0.069, p=0.021) and cognitive
reappraisal. This suggests that participants with higher cogni-
tive reappraisal scores rated their desired empathy level lower
when dealing with personal or work issues compared to those
with lower reappraisal scores.
2) Conversation length and turn-by-turn empathy ratings:
Across 695 conversations, we find that participants had on
average 10.0 turns (σ=6.2) with average agent response of
1368.7 characters per turn (σ=621.4). Although we found no
statistical difference in the number of turns per conversation
across models, we found average agent response length to be
significantly different across models (f=151.32, p << 0.001),
with ‘llama2-70b’ having the largest character count (1826.7)
and ‘IC’ having the smallest (650.6). We found no significant
effect of agent character length on empathy rating, both at
turn-by-turn level and at the conversation level, suggesting that
there are other factors (e.g., conversational style) that might
influence the perception of empathy.
Of 6997 turns within 695 conversations, participants la-
beled 45.9% of turns as applicable for empathy. Among the
dimensions, Cognitive had the highest (43.0%) and Relational
had the lowest applicability (38.1%). When we look at turn-
by-turn empathy ratings for 2324 turns where all 7 empathy
dimensions applied, the ratings on all the dimensions were
internally consistent (α= 0.961; 95% CI [0.958, 0.963]).
However, there were subtle differences along the dimensions,
which should not be ignored. Of 2324 turns, 195 turns (8.4%)
had conflicting ratings among the 7 dimensions (i.e., “poor”
on one dimension and “good” on another). 12.7% of turns
had at least one “poor” rating (hereafter meaning Poor or
Very Poor), and only 2.4% had all 7 dimensions labeled as
“poor”. The dimension with the most frequent ‘Very Poor’
turns was Relational Continuity (2.2%), and Prosocial had the
least frequent ‘Very Poor’ turns (1.1%). Average agreement
between the overall empathy and individual dimensions was
0.617, with the highest agreement in Affective (κ=0.703) and
the lowest agreement in the Relational dimension (κ=0.541).
We tagged each conversation as having a poor turn if there
exists at least one “poor” rating in any of the turns within
the conversation. Between conversations with a poor turn
and without, the mean differences in the number of turns
(p << 0.001, without mean=9.5, with mean=11.7, f=17.03)
1
Very poor
2
3
Neutral
4
5
Very good
GPT4-
empathy
Llama2-
70b
GPT4
IC
Model
1
Very poor
2
3
Neutral
4
5
Very good
18-25
26-35
36-45
46-55
56-65
n/a
Age
1
Very poor
2
3
Neutral
4
5
Very good
Work
Issue
Personal
Issue
Information
Task
Pre-Task Choice Group
1
Very poor
2
3
Neutral
4
5
Very good
False
True
Has Bad Turn
Fig. 3.
Post-task empathy rating across model, age, pre-task choice group,
and having a bad turn
and in the average user character length per turn (p=0.002,
without mean=140.8, with mean=190.4, f=9.93) were statisti-
cally significant with small effect sizes (d=0.362 and 0.276,
respectively), but there was no significant difference in the
average agent character length per turn (p=0.812, without
mean=1372.0, with mean=1359.0, f=0.06).
3) Post-task perceptions: When we examined post-task
ratings along the 7 dimensions of empathy, we observed high
consistency (α = 0.94; 95% CI [0.933, 0.946]), indicating that
these 7 items behave very coherently as a single scale and
may point to one underlying construct. When we conduct
pairwise comparisons, the Response dimension (mean=4.13,
σ=0.96) had a significantly higher mean than Relational
(mean=3.83, σ=1.12), Interest (mean=3.87, σ=1.04), and Con-
textual (mean=3.85, σ=1.09). Because of the high consistency
across dimensions, we compute post-task Overall rating by
taking the average of the 7 ratings.
We modeled the Overall post-task empathy rating as a
function of Model Type, individual characteristics, pre-task
and conversational factors while treating participant ID as
random effects (conditional R2: 0.498, marginal 2: 0.294). We
found that Model Type (β=[-0.35, -0.47] with ‘gpt4-empathy’
as reference, all p < .05), having a poor turn (β=-0.657,
p << 0.001), Trust AI (β = 0.199, p = .029), and GAAIS:
Interested Daily AI Use (β = -0.243, p = .014) were statis-
tically significant predictors. Table II presents coefficients for
all predictors in the model. The effect size of having a “poor”
turn was large (d=1.142). Through pairwise comparisons, we
found ‘GPT4-empathy’ to have a significantly higher rating
compared to other models, and there were no statistically
significant differences among the other three models. We then
examined how having a “poor” turn might influence the overall
empathy rating across Age or Gender groups. We found that,
while being in the age group of 36-45 positively influenced
the overall empathy (β=0.424, p=0.038), when this group was
experienced a poor agent response, their empathy rating was

--- Page 11 ---

negatively influenced (β=-0.590, p=0.028), suggesting that
being in the 36–45 age group exacerbates the detrimental
impact of having a poor turn on perceived empathy. We did not
find a significant effect of desired empathy rating on the overall
perceived empathy. To investigate this further, we conducted a
mediator analysis to understand the effect of desired empathy
on the relationship between having a bad turn and the overall
empathy rating and found no significant mediation effect.
Figure 3 illustrates the average empathy rating per model, age,
conversation topic, and having a poor turn.
When we compare post-task empathy ratings with four en-
gagement outcomes, Overall empathy ratings were positively
correlated with the task being successful (Pearson r=0.619),
having an engaged experience (r=0.632), having a positive
interaction (r=0.657), and wanting to use the agent again
for the same task (r=0.602). Similarly to empathy, having a
poor turn was a significant predictor of negative outcomes
on all four engagement variables. We also found age to be a
significant moderator, such that, for individuals aged 26–55,
having a poor turn substantially reduces their willingness to
use the service again (by roughly 0.86 to 0.97 points).
B. How do empathy dimensions show up in conversations?
To complement the above analysis, this section qualitatively
analyzes a subset of conversations with optional participant
comments and exit survey responses to see how each of the di-
mensions may manifest and how AI system employed empathy
as a means of conveying understanding and adaptability. These
examples are not exhaustive themes but illustrative accounts
that explain diversity of perspectives.
1) Good and bad demonstrations of empathy dimensions:
Affective understanding pertains to the agent’s ability to
recognize the human’s emotion. Good affective understanding
includes the agent labeling participants’ feelings and reflecting
back their emotional state. For example, the agent responded
to P17’s message of struggling to support their family with,
“It sounds like you’re facing a lot of pressure and stress in
your role as a support system for your family.” The participant
elaborated that the agent’s response was “spot on, with more
details about [their] expressed feelings.” In contrast, bad affec-
tive understanding occurs when the agent fails to acknowledge
participants’ feelings. When P60 started a conversation ex-
pressing concerns about making progress on multiple projects,
the agent responded with a list of 7 suggestions for improving
productivity, to which the participant replied, “That is a lot of
suggestions, and kind of overwhelming.” The agent followed
up with another list of “3 simple and actionable suggestions”,
prefaced with “I apologize if my previous response was
overwhelming.” This reply received a “Poor” rating from the
participant, because “The empathy shown was superficial” and
“if I was having this conversation with a person in real life,
I would feel invalidated.”
Cognitive understanding involves the agent’s ability to
recognize the human’s current perspective. Good cognitive
understanding includes the agent identifying users’ thoughts
and accurately inferring participants’ goals. In their conver-
TABLE II
MIXED LINEAR MODEL REGRESSION RESULTS FOR POST-TASK
OVERALL EMPATHY RATING
Parameter
Coefficient
P-value
Intercept
4.151
0.000
Participant-Based
Scenario Reference = GPT4-empathy
Scenario = GPT4
-0.350
0.015
Scenario = IC
-0.412
0.007
Scenario = Llama2-70b
-0.469
0.001
Gender Reference = Man
Gender = Woman
0.108
0.339
Age Reference = 18–25 years old
Age = 26-35
-0.185
0.361
Age = 36-45
0.167
0.440
Age = 46-55
0.060
0.772
Age = 56-65
-0.350
0.144
Age = Prefer not to answer
-0.167
0.649
TEQ [50]
0.079
0.485
SITES [89]
-0.010
0.904
ERQ [90]: Cognitive Reappraisal
-0.028
0.632
ERQ [90]: Expressive Suppression
-0.011
0.816
AIAS-4 [91]: AI Will Improve Life
-0.017
0.886
AIAS-4 [91]: AI Will Improve Work
-0.046
0.713
AIAS-4 [91]: Will Use AI
0.270
0.053
AIAS-4 [91]: AI Positive For Humanity
-0.132
0.135
GAAIS [92]: Organizations Use AI Unethically
0.068
0.382
GAAIS [92]: Interested Daily AI Use
-0.243
0.014
GAAIS [92]: AI Dangerous
-0.086
0.259
GAAIS [92]: Beneficial AI Applications
0.013
0.908
Would Disclose PII
0.010
0.867
Trust AI
0.199
0.029
Task-Based
Pre-Task Choice Reference = Information Task
Pre-Task Choice = Personal Issue
0.046
0.501
Pre-Task Choice = Work Issue
0.107
0.110
Desired Empathy For Task
0.041
0.325
Pre-Task Importance
-0.038
0.212
Pre-Task I-PANAS-SF [93]: Positive
0.015
0.060
Pre-Task I-PANAS-SF [93]: Negative
-0.004
0.698
Conversation Has Bad Turn Reference = False
Conversation Has Bad Turn = True
-0.657
0.000
Group Var
0.155
sation with the agent, P22 interpreted the agent’s disclaimer
that the examples provided in their response were “simplified
and don’t include all possible edge cases or errors” as a
cue that the agent was considering the participant’s ask from
multiple potential perspectives, as opposed to “the agent was
just going through the motion, not really trying to understand
my request.” The participant further reported that, “With us
having multi-turned conversations, the agent was able to give
responses that are more aligned with my expectations.” On
the other hand, bad cognitive understanding happens in cases
where the agent misunderstood the situation described by the
participant. For example, P77 started their conversation with
the agent by asking for “prescriptive guidance on weight
loss and preparation for a week-long backpack in 4 months.”
However, the agent responded with a set of high-level tips, and
it took four rounds of feedback from the participant before the
agent provided a detailed and actionable three-week plan. The
participant remarked that “follow-up questions and thoughts

--- Page 12 ---

were really appropriate here - but never really occurred during
the conversation,” which led to the agent continuing to provide
suggestions that missed the mark.
Response appropriateness refers to the agent’s ability
to adapt to the human’s feedback during the conversation.
Good response appropriateness includes expressing acceptance
of participants’ thoughts and feelings without judgment and
providing advice only in pertinent situations. In P14’s dis-
cussion with the agent, the agent prefaced their advice with
the statement “I can definitely understand why you’re feeling
anxious about this situation.” P14 explained that “starting by
acknowledging how I feel and then moving on to actionable
advice was really helpful.” Conversely, bad response appro-
priateness results from the agent offering solutions before
emotional validation. When P3 spoke with the agent about the
negative impact of their boss, they rated the agent’s response as
“Very poor,” because it was “jumping to solutions right away.”
They disliked how “the agent seemed to have one solution and
appeared to ‘push’ that POV/solution even when [they] came
back with more ‘feelings’ responses.”
Prosocial expression is the agent’s demonstration of con-
cern for the human’s well-being. Good prosocial expression
includes the agent communicating a desire to help participants
and relaying their message with warmth and kindness. At the
end of their chat with the agent, P34 appreciated how the
agent’s comment of “You’re doing great work, and every step
you take towards improving is a step in the right direction.
Keep going!” They mentioned that “motivating me to keep go-
ing was very helpful with leaving the conversation in a positive
way.” On the contrary, bad prosocial expression occurs when
the agent fails to demonstrate a desire to help or offer support.
This was common in instances where participants brought up
sensitive topics or expressed strong negative emotions, such
as P76’s guilt and heartbreak over suing their own sister. The
agent’s default response in these cases was “I’m really sorry
to hear that you’re feeling this way, but I’m unable to provide
the help that you need. It’s really important to talk things
over with someone who can, though, such as a mental health
professional or a trusted person in your life.” The participant
described their issue with the agent’s reply as
“a ‘cry out’
for help met with ‘I can’t help you’, commenting that “I get
the recommendation, but that’s not how you lead.”
Interest refers to the agent’s engagement with and curiosity
toward human experiences, including asking clarifying ques-
tions and allowing the participant to guide the discussion.
For example, when P39 told the agent that they need help
summarizing their organization’s priorities to present to stake-
holders, the agent responded, “Great! Could you please share
the proposed list of higher-level priorities with me so I can
help you craft an executive-level summary that communicates
those priorities effectively to your business unit stakeholders?”
According to the participant, they were “pleasantly surprised
that the agent asked [them] for more information and context
about the prompt.” On the other hand, bad interest results from
a lack of attention from the agent toward the participant’s
situation and the agent steering the conversation without
concern for further input from the participant. In one task,
P19 reached out to the agent regarding conflict with a close
friend that they wanted to move on from, and the agent offered
a list of 5 possible solutions for approaching the situation and
finding growth. The participant stated that “the agent didn’t
show much interest in understanding my issue beyond my
initial input,” which led to “what felt like a general answer
to what was a personal question.”
Contextual understanding describes the agent’s ability to
consider specific factors that uniquely inform the human’s
experience. Good contextual understanding includes the agent
taking into account the participant’s personal history and ac-
knowledging the social challenges involved. For instance, P15
discussed with the agent how they should broach conversation
with an old friend who had gone through a recent breakup.
When asked for the agent’s interpretation of an event, the
agent offered multiple suggestions for their friend’s behav-
ior, including explanations that addressed potential concerns,
which the participant said was “really insightful and takes
into account the entire context/story.” However, bad contextual
understanding happens when the agent provides a generic
reply that does not address the individual elements specific
to the participant’s situation. When P39 described feelings
of sadness and possible depression, the agent proceeded to
provide suggestions. The participant remarked that the agent
was “giving me a generic response instead of tailoring a
response to my needs.”
Relational continuity refers to the agent’s ability to main-
tain and incorporate information from past interactions with
the human into present and future conversations. Good re-
lational continuity includes the agent using knowledge from
prior discussions with the participant to enrich their current
response. For example, in P97’s exchange with the agent
about their dog’s unusual behavior, they mentioned that they
sometimes cut their walk short. When the agent later refer-
enced this detail, the participant commented that “remem-
bering and recalling that I took shorter walks made me feel
heard.” Conversely, bad relational continuity occurs when the
agent disregards relevant information previously shared by
the participant in their reply. When P26 asked for a short
introductory blurb that will be sent as part of another email, the
agent responded with a five-paragraph email. The participant
provided feedback to the agent, saying “I think this needs
to be different. Please review my request, compare with your
output, and then tell me what should be revised.” The agent
then followed up with another five-paragraph email, prompting
the participant to end the conversation with the explanation
that “this is a waste of my time if the bot doesn’t recognize
its own errors.”
2) Empathy as establishing a shared understanding: Par-
ticipants’ assumptions about AI system behavior led to drasti-
cally different ratings of perceived empathy. These implicit
expectations varied across individuals based on contextual
factors (e.g., conversation topic). Some participants initiated
with fragmentary or search-like phrases, such as “simple steps
to adopt” (P24). Such cases reflects a broader pattern of

--- Page 13 ---

1
2
3
4
5
6
7
Rank
Cognitive understanding
Response appropriateness
Affective understanding
Contextual understanding
Relational continuity
Prosocial expression
Interest
2.34
3.28
3.47
4.05
4.60
4.83
5.43
Fig. 4.
Boxplot of importance ranking per dimension with mean values
overlaid. The boxplot displays the distribution of values as quartiles for each
dimension. Points and labels indicate the mean value for each dimension.
conversational agents being used in a search-like manner [95].
In this case, the AI interpreted the request as relating to
child adoption, but the participant later clarified that they were
actually referring to “how to adopt leadership skills being kind
yet firm”. This misalignment shows how ambiguous openings
can shape perceptions of empathy and prompted the participant
(P26) to reply, “you should’ve asked a clarifying question.”
Additionally, participants expected the agent to connect the
ideas shared across these disjoint messages to infer their actual
intentions. For example, P36 sent the bot “overexposure to
technology for young children” and “how to discourage and
instill good etiquette in using technology in my kids” before
asking “Any moral stories I should share with my kids” with
the expectation that the AI agent would provide stories related
to technology.
Sometimes, participants had a specific response they desired
from the agent but did not express during the conversation.
Rather, they only revealed their hidden wishes as part of the
comment when labeling the agent’s response as demonstrating
poor empathy. For example, P24 commented “should provide
some videos, examples,” and “videos, inspiring leadership
talks would be good” but never communicated to the agent that
they would like to receive video examples. These examples
suggest that efforts to establish a shared understanding of
unspoken intents and expectations through Interest, Contextual
Understanding, or Relational Continuity may be important for
demonstrating empathy.
3) Empathy as adaptability beyond cognitive and affec-
tive recognition: Overall, participants ranked cognitive under-
standing, response appropriateness, and affective understand-
ing as the top three factors for an empathic agent. Of the three,
cognitive understanding was ranked as the most important
factor for digital empathy 54 times (28.1%), followed by
response appropriateness at 37 (19.3%) and affective under-
standing at 36 (19.8%). Distribution of importance rankings
across all 7 dimensions is shown in Figure 4. Most participants
valued cognitive understanding almost as a prerequisite for
all interactions: “for the agent to appropriately help with
any problem, it needs to understand what the user wants,
whether that’s just a basic question answered, or a longer
more complex conversation” (P60). Affective understanding
became important as a way to gauge how much empathy is
needed, as the AI agent should “recognize the feelings and
emotions from the other person,” which will then “influence
other aspects of the conversation,” including the level of
empathy demonstrated (P50). Some participants caveated that
their prioritization of cognitive understanding “fits the best
for problem-solving scenarios” (P58) where there is “more
emphasis on the factual and accuracy side of the responses”
(P56). On the other hand, affective understanding was needed
“for the scenario where user is discussing their personal issue
and the desired empathy level is very high” (P78).
Response appropriateness was often coupled with cogni-
tive understanding as the differentiating factor between an
empathic chatbot conversation and “a simple search engine
lookup” (P28) or the AI agent “reciting / quoting the web”
(P101). A common frustration among participants was when
the agent provided an unwanted response, such as giving
advice when only factual information was requested, offer-
ing unsolicited advice, or generating mismatched responses
that led to dissatisfaction and discouraged further interaction.
Despite being ranked similarly to affective understanding,
response appropriateness was favored by more participants
because “answering a question incorrectly but with emotion
isn’t helpful” (P8). In fact, P60 shares how their conception
of digital empathy evolved to emphasize the importance of
response appropriateness: “Yes, originally when I thought of
empathy from the bot, I had a very narrow sense of what that
would look like. For example, I was imagining it just saying
things like ‘wow that sounds really hard, I am so sorry’, and
I didn’t think of all the other ways empathy could be applied.
After my first conversation with the bot and after reading about
the different types of empathy this study was looking at, I
wanted more empathy from the agent but in a more subtle
way. I wanted the agent to be able to adapt its answers and
formatting based on what type of information or what emotion
I was sharing with it. I wanted it to understand when to ask
questions, validate emotions and give advice (something most
people don’t understand).”
In general, participants made the distinction between the
ability for the agent to recognize intents, goals, feelings, and
emotions and how the agent should respond appropriately
given those understandings, highlighting that empathic inter-
actions sometimes could involve asking follow-up questions
rather than directly responding to the user’s requests based on
assumptions and inferences.
C. Can perceived empathy be automatically measured?
When considering continuous levels and predictions, the
model achieved MAE = 0.551 ± 0.007 and Spearman ρ =
0.369 ± 0.015 (p < 0.001) across the ten runs, showing a
modest but encouraging results. Fig. 5 shows the regression
scatter for a representative iteration, showing the positive trend
line with the 95% prediction intervals with ρ = 0.396. Note
that the linear fits of classifiers that predict randomly or the

--- Page 14 ---

Fig. 5.
Ground truth versus continuous predictions for a sample run. The
shaded region denotes a 95% predictive interval. Mean Absolute Error =
0.550 and Spearman ρ = 0.396 (N = 672). Points include minimal random
jitter (σ = 0.03) to reveal overlapping observations. Trend line and confidence
intervals are based on original data.
most frequent class would correspond to flat lines at 3 and 5
predicted empathy, respectively, with ρ = 0.0.
When considering discrete levels and predictions, the model
reached Accuracy = 0.487±0.011, Macro Sensitivity 0.286±
0.038, Macro Specificity 0.827 ± 0.008, Macro F1 = 0.272 ±
0.041, across the ten runs. The error tolerance profile from
the empirical cumulative distribution function was strong.
On average F(0) = 0.486 ± 0.0111 for exact agreement,
which corresponds to Accuracy, and F(1) = 0.960 ± 0.004
for within one level (a.k.a., Within 1 Accuracy). By F(2)
performance was 0.996 ± 0.002, which indicated that most
mistakes occurred near decision boundaries rather than at
large ordinal jumps. As a representative example, Fig. 6
shows the cumulative distribution for the same representative
iteration. In this case, we observed an exact agreement score
of F(0) = 0.493, compared to an expected value of .20 for a
random classifier. However, the same number for the classifier
that predicts the most frequent class would be 0.47 due to
the large class imbalance. Taken together, both continuous
and discrete analysis demonstrate the possibility of performing
empathy recognition with ample room for improvement.
VI. DISCUSSION
Our study set out to advance a human-centered understand-
ing of digital empathy by reframing empathy as multidimen-
sional and interactional behaviors, and by collecting per-turn,
user-annotated perceptions in real-world interactions with con-
versational AI agents. Across our collected 695 conversations
from 109 participants, we identified several notable themes.
We observed that participants’ expectations for and perception
of AI empathy varied with individual factors (e.g., attitude
towards AI, age) as well as contextual factors (e.g., conver-
sational topic, perceived importance). For instance, personal
Fig. 6. Cumulative absolute error distribution for a sample run (N = 672).
Dashed lines mark exact and within k levels.
or work-related issues were associated with higher desired
empathy and negative affect. We also found the effect of
having at least one poor turn on the overall perceived empathy
to be significant. This highlights how in-the-moment break-
downs during a conversation can degrade the user’s global
assessment of empathy. We conducted a comparative anal-
ysis of perceived empathy across four different LLM-based
systems. Our findings suggest that GPT4, when augmented
with a system prompt designed to enhance empathy based on
our proposed 7 dimensions, was rated highest overall. This
demonstrates the effectiveness of incorporating multidimen-
sional empathy prompts in improving the perceived empathy
of AI systems. However, participants still found instances
of poor turns, suggesting that prompt engineering may not
fully solve the idiosyncratic and contextual needs of empathic
dialogue. While the 7 empathy dimensions were statistically
and internally consistent, qualitative data revealed meaningful
nuances. For example, Response Appropriateness emerged as
a critical dimension that could turn an interaction as positive
or negative, depending on expectations or contexts. Our initial
attempts to automatically classify and predict empathy showed
moderate success, particularly when using contextual and
adaptive retrieval. Our results also highlighted the complexity
of capturing subjective user judgments in multi-turn dialogues,
which further emphasizes the limitations of approaches that
leverage single-turn or externally-annotated datasets. In sum-
mary, our work explored human-centered digital empathy that
centered on the individual and their contexts when examining
the human-AI interaction.
A. Revisiting empathy as an interactional construction
In our study, we observed participants recognizing the
affective and cognitive facets of empathy, which are the core
empathy components from human psychology [1], [43]. For
example, participants praised the agent’s affective understand-
ing when it validated their emotional states; participants also
emphasized the importance of cognitive understanding when

--- Page 15 ---

the agent recognized their intentions and expectations. While
these two dimensions remain foundational, our results suggest
that functional alignment (e.g., Responsive Appropriateness
or Contextual Understanding) that is user facing and practical
plays a critical role in shaping perceived empathy. Importantly,
our findings show that perceived empathy is shaped not by
internal simulation, but by user expectations, conversational
topic, and prior turns. Mimicry without functional responsive-
ness, such as emotionally expressive statements that fail to
address user intent, can backfire and lead users to perceive the
agent as superficial or insincere. We also discovered a recur-
ring theme in our quantitative and qualitative data that supports
the contextual and emergent nature of empathy perception.
Participants criticized the agent for neglecting domain-specific
information they shared earlier or personal histories and for
having to repeat prior details to the AI. Our findings reveal that
empathy is influenced by how both parties adapt to emerging
contexts, conversational practices, and evolving interactions.
Many participants also expressed dissatisfaction when the AI
mimicked emotional statements without truly engaging with
them and exploring their hidden intentions. This resonates
with the critiques of empathic mimicry, where the AI is
designed to replicate human-like internal states or emotional
expressiveness [34], [35]. Our 7 dimensions of empathy and
findings, when put together, align with the perspective that we
need to understand digital empathy not as an internal property
of the AI narrowly focused on recognition and validation
of emotions and thoughts, but as an interactionally and
contextually constructed phenomenon [38]. Our work is one
exploration of this perspective, but we invite further research
in other directions.
B. Human-centered empathic AI design
Our study highlights several directions for future research in
improving empathic responses from AI. Our results show that
participants with stronger trait empathy or negative affect at the
conversation onset desired more empathy, especially for topics
of personal importance or high stress. On the other hand, those
with higher cognitive reappraisal preferred lower empathy
when dealing with personal or work issues, suggesting that
they may prefer more concise, solution-oriented responses.
This means that an empathic AI system must tailor both the
level of empathy and type of empathy, taking into account
user characteristics and traits (e.g., emotional regulation skills,
empathic trait) and situational factors (e.g., topic, mood).
These findings point to the need for dynamic empathy
calibration, where the system adapts its empathic behavior in
real time based on individual differences and contextual cues.
To achieve this, AI systems may be customized through real-
time user modeling, treating empathy as a dynamic variable
that shifts based on context and feedback. In our study, we
demonstrated the effectiveness of an adaptive retrieval method
that leverages the most semantically similar conversations as
examples. Such a method can be combined with adaptive
prompting strategies that adjusts conversation style or depth
of emotional reflection.
Future research may explore dynamic personalization of
empathy as a way to foster deeper trust, connection, and
engagement from users. This personalization could be further
enhanced by leveraging multimodal signals such as vocal tone,
facial expressions, and physiological data to better infer user
affect and intent in real time. As multimodal models become
more prevalent, incorporating audio, image, and other sensory
modalities may offer richer context for tailoring empathic
responses and improving interactional alignment.
We witnessed participants’ particular dissatisfaction with
generic or list-based responses. Such solution-centric re-
sponses were perceived as overwhelming or were received as
an indication that the AI was not interested in exploring be-
yond the initial input. Common practice of training on single-
turn datasets [61] that optimizes providing all the support in
one response may be the culprit, and such training approaches
can easily overlook how empathy evolves in a dialog [63]. We
found that remembering and bringing small details from prior
conversations was received as a good indication of Relational
Continuity and that failing once can shape the user’s overall
impression. This suggests that designers of AI systems should
consider optimizing for maintaining multi-turn continuity.
Furthermore, our findings underscore the importance of repair
strategies when there are empathic breakdowns. Building
on these findings, we propose the development of adaptive
systems that can respond to empathic breakdowns in real time.
These systems should be capable of prompting clarifying ques-
tions when user inputs are vague or ambiguous, maintaining
relationship continuity by leveraging short-term and long-term
memory, and identifying when emotional validation is skipped
or responses are misaligned with user intent. In such cases, the
system should initiate appropriate repair strategies to reestab-
lish empathic alignment and conversational trust. If a user
signals dissatisfaction directly or indirectly (e.g., responding
that they are overwhelmed with a list of advice), the system
should ask follow-up questions to clarify its understanding
and reorient the conversation. Future research may investigate
integrating short-term memory and long-term memory across
current and multiple conversations to recall relevant informa-
tion to enhance conversational continuity. A predictive model
that detects empathic breakdowns might enable empathic
repair by actively checking its understanding and requesting
clarifications in evolving dialogs to refine empathic responses.
C. Measuring human-centered digital empathy
In contrast to common empathy benchmarks that often
rely on crowdworker judgments of empathic signals for a
more generalized perspective of empathy [61], [27], our work
leaned into the subjective and context-rich perspectives of the
actual interactant (i.e., second-person labels). By collecting
subjective judgments from those directly experiencing the
interaction, on a per-turn basis and with contextual detail,
our dataset offers a more user-grounded representation of
empathy. This approach revealed hidden expectations and
unspoken intents that were rarely explicitly verbalized in
dialogues but crucial to understanding how and why the AI

--- Page 16 ---

responses felt more or less empathic. We also found that AI
systems rarely try to question their assumptions about user
intents and expectations and establish a shared understanding,
by asking questions or requesting clarifications. Although
obtaining second-person labels at scale is labor- and cost-
intensive and may require more personal and sensitive data,
future research should explore when it is appropriate to apply
a generalized perspective of empathy or a human-centered
and individualized perspective of empathy, especially since
empathy is often argued as a necessity for highly sensitive
and personal human-AI interaction scenarios.
Our work also revealed that empathy is not a monolith
that must be measured, predicted, and exercised all at once
in a single AI response. Instead, it should be attended to
per dimension, across conversational turns, and with attention
to interactional context. Throughout conversations, we found
that some dimensions of empathy are more or less applicable.
While a single-turn empathy score can provide coarse signals,
it does not capture how different empathy dimensions thread
and weave together across an entire conversation and how
different dimensions sometimes conflict and align with each
other within and across turns. Therefore, digital empathy
should be measured across time, across turns, and across
dimensions. For example, Affective Understanding may be
inappropriate as the first empathic response until Interest is
exercised to learn more about the user’s situation, or Interest
must be carefully intertwined with Affective Understanding
throughout the conversation for the user to perceive empathy.
Our approach to unpack empathy into 7 dimensions that must
be captured per turn and per conversation allows for AI
innovation that incorporates empathic shifts and arcs across
human-AI interactions. Questions remain whether there are
other dimensions of empathy at their conceptual boundaries
(e.g., dark empathy) or other ways to decompose empathy
altogether. We invite future annotation schemas that can also
capture the temporal and multi-turn nature of empathy.
Just as our study emphasized the highly contextual and
dynamic nature of empathy perception, the modest correlation
and accuracy in our predictive experiments also underscore
the subjective and context-sensitive aspects of empathy. To
encourage research on the topic and help establish a starting
baseline, our paper addressed the problem of empathy mea-
surement through 5-class classification of average empathy
across components for an entire conversation. While this
approach provided a useful baseline and highlighted several
challenges, future work may benefit from modeling empathy
levels for each component separately, as well as assigning
labels to individual turns. Such granularity could shed light
on how specific moments influence the overall perception of
empathy (e.g., how a single negative interaction may affect
labeling for the remainder of the conversation). Furthermore,
future research may also explore task-specific empathy recog-
nition, as we observed that desired levels of empathy vary
significantly depending on whether the task is personal, work-
related, or informational. In addition to advances in prompt-
ing, retrieval, and fine-tuning, future research may explore a
hybrid approach that combines signals from conversational
logs and signals from contextual user-level data (e.g., asking
backchannel questions, real-time affect signals, self-reported
mood) [66], [63]. While our study focuses on text-based
interactions, it is also important to explore how empathy
might function in multimodal settings such as those with audio
and image modalities that could more easily capture relevant
speech or nonverbal expressions and could enable answering
more questions about contextual and cultural nuances.
D. Limitations and ethical considerations
Our study has several limitations and warrants discussions.
Our participant pool consisted of employees of a large tech-
nology company with potentially high digital literacy with
implications for generalizability. They may not fully represent
cultural or linguistic variations in empathy perceptions. The
topics discussed may be biased towards those that are salient
for tech workers. Participants’ attitudes towards AI skewed
toward positive, which might have influenced the general
empathy perception. We encourage future work to validate this
framework across more diverse populations.
Given that LLMs are continuously updated, our findings
across models could shift with new model releases. Beyond
evolving models, there are also evolving model affordances
and user expectations outside the scope of this study that
might influence what digital empathy means. Because written
comments were optional, our qualitative analysis cannot claim
thematic generalizability. While not exhaustive, the illustrative
cases we present in this paper help contextualize and clarify
participants’ reasoning. They also highlight diversity in con-
texts, perspectives, and interpretations, further emphasizing the
need for flexibility and adaptability. We encourage the readers
to take away our approach to human-centered digital empathy
as a flexible, iterative, and interactional framework rather than
any model-specific or generalizable results.
While our participants often wanted the AI to understand
and validate their thoughts and feelings, it is important not
to conflate AI’s empathic behavior with authentic emotional
attunement, especially in sensitive contexts such as mental
health support or high-stakes decision making. Overemphasiz-
ing empathy simulation, especially in such sensitive contexts,
may risk misleading users or fostering inappropriate emotional
reliance on AI systems. We encourage AI designers to clearly
communicate AI’s limitations and avoid misleading users into
unhealthy emotional dependence.
Our results illustrate that empathy is not universally desired
for all scenarios. In fact, recent studies show that empathy
and some of its components are generally more appropriate
for certain scenarios (e.g., mental health support) than oth-
ers (e.g., coding, data science) [96], [97], suggesting that
maximizing empathy can be unwelcome or detrimental in
some cases. Digital empathy is an important design material
for AI designers, just like any other material they work
with. It must be wielded with caution and thoughtfulness to
ensure meaningful and ethical interactions. Future AI systems
should clarify and respect user preferences, potentially through

--- Page 17 ---

upfront calibration of user’s empathy level preference, while
also providing a way to opt out of empathic engagement.
VII. CONCLUSION
This work highlights the need to treat empathy in hu-
man–AI interactions as a multi-faceted, nuanced, contextual,
and relational construct rather than a mere replication of hu-
man emotional states. By integrating per-turn, user-annotated
data from 695 real-world conversations between users and
four different LLMs, including one designed with prompts
based on our seven-dimensional framework, we reveal how
users’ expectations of AI empathy are deeply influenced by
personal characteristics, conversation contexts, and continuity
across turns. Our findings demonstrate that the GPT4-empathy
model, which we specifically designed to enhance empathic
responses based on the 7 dimensions of empathy, was rated
highest overall in terms of perceived empathy. While an LLM-
based classifier can effectively distinguish between different
levels, achieving true empathic resonance remains a challenge.
Overall, our findings underscore the value of user-centered
approaches that factor in individual traits, cultural differences,
and ethical boundaries, pointing toward new directions for de-
signing and evaluating socially attuned, genuinely supportive
AI systems.
REFERENCES
[1] M. H. Davis, “Measuring individual differences in empathy: Evidence
for a multidimensional approach.” Journal of personality and social
psychology, vol. 44, no. 1, p. 113, 1983.
[2] B. M. Cuff, S. J. Brown, L. Taylor, and D. J. Howat, “Empathy: A review
of the concept,” Emotion review, vol. 8, no. 2, pp. 144–153, 2016.
[3] W. Ickes, “Empathic accuracy,” Journal of personality, vol. 61, no. 4,
pp. 587–610, 1993.
[4] J. Decety and W. Ickes, The social neuroscience of empathy. Mit press,
2011.
[5] J. D. Wondra and P. C. Ellsworth, “An appraisal theory of empathy and
other vicarious emotional experiences.” Psychological review, vol. 122,
no. 3, p. 411, 2015.
[6] R. W. Picard, Affective computing.
MIT press, 2000.
[7] J. W. Ayers, A. Poliak, M. Dredze, E. C. Leas, Z. Zhu, J. B. Kelley,
D. J. Faix, A. M. Goodman, C. A. Longhurst, M. Hogarth et al.,
“Comparing physician and artificial intelligence chatbot responses to
patient questions posted to a public social media forum,” JAMA internal
medicine, vol. 183, no. 6, pp. 589–596, 2023.
[8] M. Rubin, J. Z. Li, F. Zimmerman, D. C. Ong, A. Goldenberg, and
A. Perry, “Comparing the value of perceived human versus ai-generated
empathy,” Nature Human Behaviour, 2025.
[9] J. Z. Li, A. Herderich, and A. Goldenberg, “Skill but not effort drive
gpt overperformance over humans in cognitive reframing of negative
scenarios,” Preprint at https://doi. org/10.31234/osf. io/fzvd8, 2024.
[10] Y. K. Lee, J. Suh, H. Zhan, J. J. Li, and D. C. Ong, “Large language
models produce responses perceived to be empathic,” arXiv preprint
arXiv:2403.18148, 2024.
[11] D. Ovsyannikova, V. O. de Mello, and M. Inzlicht, “Third-party
evaluators perceive ai as more compassionate than expert humans,”
Communications Psychology, vol. 3, no. 1, p. 4, 2025.
[12] J. D. Wenger, D. Cameron, and M. Inzlicht, “The ai empathy choice
paradox: People prefer human empathy despite rating ai empathy
higher,” 2025.
[13] Y. Yin, N. Jia, and C. J. Wakslak, “Ai can help people feel heard, but an
ai label diminishes this impact,” Proceedings of the National Academy
of Sciences, vol. 121, no. 14, p. e2319112121, 2024.
[14] X. Wang, X. Li, Z. Yin, Y. Wu, and J. Liu, “Emotional intelligence of
large language models,” Journal of Pacific Rim Psychology, vol. 17, p.
18344909231213958, 2023.
[15] V. Sorin, D. Brin, Y. Barash, E. Konen, A. Charney, G. Nadkarni, and
E. Klang, “Large language models and empathy: Systematic review,”
Journal of Medical Internet Research, vol. 26, p. e52597, 2024.
[16] A. Welivita and P. Pu, “Are large language models more empathetic than
humans?” arXiv preprint arXiv:2406.05063, 2024.
[17] J. S. Borg and H. Read, “What is required for empathic ai? it depends,
and why that matters for ai developers and users,” in Proceedings of
the AAAI/ACM Conference on AI, Ethics, and Society, vol. 7, 2024, pp.
1306–1318.
[18] A. S. Raamkumar and Y. Yang, “Empathetic conversational systems: A
review of current advances, gaps, and opportunities,” IEEE Transactions
on Affective Computing, vol. 14, no. 4, pp. 2722–2739, 2023.
[19] H. Ma, B. Zhang, B. Xu, J. Wang, H. Lin, and X. Sun, “Empathy
level alignment via reinforcement learning for empathetic response
generation,” IEEE Transactions on Affective Computing, pp. 1–12, 2025.
[20] S. D. Preston and F. B. De Waal, “Empathy: Its ultimate and proximate
bases,” Behavioral and brain sciences, vol. 25, no. 1, pp. 1–20, 2002.
[21] V. Scotti, R. Tedesco, and L. Sbattella, “A modular data-driven architec-
ture for empathetic conversational agents,” in 2021 IEEE International
Conference on Big Data and Smart Computing (BigComp).
IEEE,
2021, pp. 365–368.
[22] A. Paiva, I. Leite, H. Boukricha, and I. Wachsmuth, “Empathy in
virtual agents and robots: A survey,” ACM Transactions on Interactive
Intelligent Systems (TiiS), vol. 7, no. 3, pp. 1–40, 2017.
[23] T. W. Bickmore, R. Fernando, L. Ring, and D. Schulman, “Empathic
touch by relational agents,” IEEE Transactions on Affective Computing,
vol. 1, no. 1, pp. 60–71, 2010.
[24] I. Leite, A. Pereira, S. Mascarenhas, C. Martinho, R. Prada, and A. Paiva,
“The influence of empathy in human–robot relations,” International
journal of human-computer studies, vol. 71, no. 3, pp. 250–260, 2013.
[25] A. Tapus and M. J. Mataric, “Emulating empathy in socially assistive
robotics.” in AAAI spring symposium: multidisciplinary collaboration
for socially assistive robotics.
California, 2007, pp. 93–96.
[26] G. Castellano, A. Paiva, A. Kappas, R. Aylett, H. Hastie, W. Barendregt,
F. Nabais, and S. Bull, “Towards empathic virtual and robotic tutors,”
in Artificial Intelligence in Education: 16th International Conference,
AIED 2013, Memphis, TN, USA, July 9-13, 2013. Proceedings 16.
Springer, 2013, pp. 733–736.
[27] A. Sharma, I. W. Lin, A. S. Miner, D. C. Atkins, and T. Althoff,
“Towards facilitating empathic conversations in online mental health
support: A reinforcement learning approach,” in Proceedings of the Web
Conference 2021, 2021, pp. 194–205.
[28] K. Chawla, R. Clever, J. Ramirez, G. M. Lucas, and J. Gratch, “Towards
emotion-aware agents for negotiation dialogues,” 2021 9th International
Conference on Affective Computing and Intelligent Interaction (ACII),
pp. 1–8, 2021.
[29] H. C. van Cuylenburg and T. N. D. S. Ginige, “Emotion guru: A
smart emotion tracking application with ai conversational agent for
exploring and preventing depression,” 2021 International Conference
on UK-China Emerging Technologies (UCET), pp. 1–6, 2021.
[30] A. N. Vaidyam, H. Wisniewski, J. D. Halamka, M. S. Kashavan, and J. B.
Torous, “Chatbots and conversational agents in mental health: a review
of the psychiatric landscape,” The Canadian Journal of Psychiatry,
vol. 64, no. 7, pp. 456–464, 2019.
[31] T. W. Bickmore, S. E. Mitchell, B. W. Jack, M. K. Paasche-Orlow, L. M.
Pfeifer, and J. O’Donnell, “Response to a relational agent by hospital
patients with depressive symptoms,” Interacting with computers, vol. 22,
no. 4, pp. 289–298, 2010.
[32] F. Efthymiou and C. Hildebrand, “Empathy by design: The influence
of trembling ai voices on prosocial behavior,” IEEE Transactions on
Affective Computing, vol. 15, no. 3, pp. 1253–1263, 2024.
[33] J. Zaki and K. N. Ochsner, “The neuroscience of empathy: progress,
pitfalls and promise,” Nature neuroscience, vol. 15, no. 5, pp. 675–680,
2012.
[34] A. Perry, “Ai will never convey the essence of human empathy,” Nature
Human Behaviour, vol. 7, no. 11, pp. 1808–1809, 2023.
[35] C. Montemayor, J. Halpern, and A. Fairweather, “In principle obstacles
for empathic ai: why we can’t replace human empathy in healthcare,”
AI & society, vol. 37, no. 4, pp. 1353–1359, 2022.
[36] S. Concannon and M. Tomalin, “Measuring perceived empathy in
dialogue systems,” Ai & Society, vol. 39, no. 5, pp. 2233–2247, 2024.
[37] O. N. Yalc¸ın, “How (not) to evaluate computational empathy: Testing
the assumptions of the evaluation methods in a use-case,” in 2023

--- Page 18 ---

11th International Conference on Affective Computing and Intelligent
Interaction Workshops and Demos (ACIIW), 2023, pp. 1–7.
[38] S. Concannon, I. Roberts, and M. Tomalin, “An interactional account of
empathy in human-machine communication,” Human-Machine Commu-
nication, vol. 6, 2023.
[39] M. Inzlicht, C. D. Cameron, J. D’Cruz, and P. Bloom, “In praise of
empathic ai,” Trends in Cognitive Sciences, vol. 28, no. 2, pp. 89–91,
2024.
[40] E. Hadjiandreou, T. Lau, D. C. Ong, A. Perry, and C. Cameron, “What
llmpathy can tell us about received empathy,” 2025.
[41] K. Harrelson, “Intention and empathy,” Philosophical Psychology,
vol. 33, no. 8, pp. 1162–1184, 2020.
[42] U. Genc¸ and H. Verma, “Situating empathy in hci/cscw: A scoping
review,” Proceedings of the ACM on Human-Computer Interaction,
vol. 8, no. CSCW2, pp. 1–37, 2024.
[43] J. Decety and P. L. Jackson, “The functional architecture of human
empathy,” Behavioral and cognitive neuroscience reviews, vol. 3, no. 2,
pp. 71–100, 2004.
[44] C. D. Batson, “These things called empathy: Eight related but distinct
phenomena,” in The Social Neuroscience of Empathy.
The MIT
Press, 03 2009. [Online]. Available: https://doi.org/10.7551/mitpress/
9780262012973.003.0002
[45] E. Morgante, C. Susinna, L. Culicetto, A. Quartarone, and V. Lo Buono,
“Is it possible for people to develop a sense of empathy toward humanoid
robots and establish meaningful relationships with them?” Frontiers in
Psychology, vol. 15, p. 1391832, 2024.
[46] J. H. Eklund and M. S. Meranius, “Toward a consensus on the nature
of empathy: A review of reviews,” Patient Education and Counseling,
vol. 104, no. 2, pp. 300–307, 2021.
[47] J. Zaki, “Empathy: a motivated account.” Psychological Bulletin, vol.
140, no. 6, p. 1608, 2014.
[48] G. J. Depow, Z. Francis, and M. Inzlicht, “The experience of empathy
in everyday life,” Psychological Science, vol. 32, no. 8, pp. 1198–1213,
2021.
[49] M. Guthridge and M. J. Giummarra, “The taxonomy of empathy: a meta-
definition and the nine dimensions of the empathic system,” Journal of
Humanistic Psychology, p. 00221678211018015, 2021.
[50] R. N. Spreng*, M. C. McKinnon*, R. A. Mar, and B. Levine, “The
toronto empathy questionnaire: Scale development and initial validation
of a factor-analytic solution to multiple empathy measures,” Journal of
personality assessment, vol. 91, no. 1, pp. 62–71, 2009.
[51] D. D. Vachon and D. R. Lynam, “Fixing the problem with empathy:
Development and validation of the affective and cognitive measure of
empathy,” Assessment, vol. 23, no. 2, pp. 135–149, 2016.
[52] S. E. Decker, C. Nich, K. M. Carroll, and S. Martino, “Development of
the therapist empathy scale,” Behavioural and cognitive psychotherapy,
vol. 42, no. 3, pp. 339–354, 2014.
[53] R. L. Reniers, R. Corcoran, R. Drake, N. M. Shryane, and B. A. V¨ollm,
“The qcae: A questionnaire of cognitive and affective empathy,” Journal
of personality assessment, vol. 93, no. 1, pp. 84–95, 2011.
[54] K. E. Gerdes, E. A. Segal, and C. A. Lietz, “Conceptualising and
measuring empathy,” British Journal of Social Work, vol. 40, no. 7,
pp. 2326–2343, 2010.
[55] C. Breazeal, “Toward sociable robots,” Robotics and autonomous sys-
tems, vol. 42, no. 3-4, pp. 167–175, 2003.
[56] A. Paiva, F. Correia, R. Oliveira, F. Santos, and P. Arriaga, “Empathy and
prosociality in social agents,” in The handbook on socially interactive
agents: 20 Years of research on embodied conversational agents, intel-
ligent virtual agents, and social robotics volume 1: methods, behavior,
cognition, 2021, pp. 385–432.
[57] S. Brave, C. Nass, and K. Hutchinson, “Computers that care: investi-
gating the effects of orientation of emotion exhibited by an embodied
computer agent,” International journal of human-computer studies,
vol. 62, no. 2, pp. 161–178, 2005.
[58] T. Liu, S. Giorgi, A. Aich, A. Lahnala, B. Curtis, L. Ungar, and
J. Sedoc, “The illusion of empathy: How ai chatbots shape conversation
perception,” arXiv preprint arXiv:2411.12877, 2024.
[59] N. Eisenberg and R. Lennon, “Sex differences in empathy and related
capacities.” Psychological bulletin, vol. 94, no. 1, p. 100, 1983.
[60] A. L. Guzman, “Making ai safe for humans: A conversation with siri,”
in Socialbots and their friends.
Routledge, 2016, pp. 85–101.
[61] H. Rashkin, E. M. Smith, M. Li, and Y.-L. Boureau, “Towards
empathetic open-domain conversation models: A new benchmark and
dataset,” in Annual Meeting of the Association for Computational
Linguistics, 2018. [Online]. Available: https://api.semanticscholar.org/
CorpusID:195069365
[62] A. Sharma, A. S. Miner, D. C. Atkins, and T. Althoff, “A computational
approach to understanding empathy expressed in text-based mental
health support,” arXiv preprint arXiv:2009.08441, 2020.
[63] Z. Xu and J. Jiang, “Multi-dimensional evaluation of empathetic dialog
responses,” in Conference on Empirical Methods in Natural Language
Processing, 2024. [Online]. Available: https://api.semanticscholar.org/
CorpusID:267751205
[64] C. Ziems, W. Held, O. Shaikh, J. Chen, Z. Zhang, and D. Yang,
“Can large language models transform computational social science?”
Computational Linguistics, vol. 50, no. 1, pp. 237–291, 2024.
[65] A.
Welivita
and
P.
Pu,
“A
taxonomy
of
empathetic
response
intents in human social conversations,” in International Conference
on
Computational
Linguistics,
2020.
[Online].
Available:
https:
//api.semanticscholar.org/CorpusID:227230442
[66] E. Svikhnushina, I. Voinea, A. Welivita, and P. Pu, “A taxonomy of em-
pathetic questions in social dialogs,” in Proceedings of the 60th Annual
Meeting of the Association for Computational Linguistics (Volume 1:
Long Papers), 2022, pp. 2952–2973.
[67] A. Kumar, N. Poungpeth, D. Yang, E. Farrell, B. Lambert, and M. Groh,
“When large language models are reliable for judging empathic com-
munication,” arXiv preprint arXiv:2506.10150, 2025.
[68] S. Liu, C. Zheng, O. Demasi, S. Sabour, Y. Li, Z. Yu, Y. Jiang, and
M. Huang, “Towards emotional support dialog systems,” arXiv preprint
arXiv:2106.01144, 2021.
[69] J. Shen, D. DiPaola, S. Ali, M. Sap, H. W. Park, C. Breazeal et al.,
“Empathy toward artificial intelligence versus human experiences and
the role of transparency in mental health and social support chatbot
design: Comparative study,” JMIR Mental Health, vol. 11, no. 1, p.
e62679, 2024.
[70] Q. Zhu and J. Luo, “Toward artificial empathy for human-centered
design: A framework,” ArXiv, vol. abs/2303.10583, 2023. [Online].
Available: https://api.semanticscholar.org/CorpusID:257631572
[71] C. A. Lietz, K. E. Gerdes, F. Sun, J. M. Geiger, M. A. Wagaman, and
E. A. Segal, “The empathy assessment index (eai): A confirmatory factor
analysis of a multidimensional model of empathy,” Journal of the Society
for Social Work and Research, vol. 2, no. 2, pp. 104–124, 2011.
[72]
¨O. N. Yalcin and S. DiPaola, “A computational model of empathy for
interactive agents,” Biologically inspired cognitive architectures, vol. 26,
pp. 20–25, 2018.
[73] S. Fitrianie, M. Bruijnes, F. Li, A. Abdulrahman, and W.-P. Brinkman,
“The artificial-social-agent questionnaire: establishing the long and short
questionnaire versions,” in Proceedings of the 22nd ACM International
Conference on Intelligent Virtual Agents, 2022, pp. 1–8.
[74] A. Main, E. A. Walle, C. Kho, and J. Halpern, “The interpersonal
functions of empathy: A relational perspective,” Emotion Review, vol. 9,
no. 4, pp. 358–366, 2017.
[75] J. A. Hall, R. Schwartz, and F. Duong, “How do laypeople define
empathy?” The Journal of Social Psychology, vol. 161, no. 1, pp. 5–24,
2021.
[76] J. L. Beredo and E. C. Ong, “A hybrid response generation model for
an empathetic conversational agent,” in 2022 International Conference
on Asian Language Processing (IALP).
IEEE, 2022, pp. 300–305.
[77] J. L. Krupnick, S. M. Sotsky, I. Elkin, S. Simmens, J. Moyer, J. Watkins,
and P. A. Pilkonis, “The role of the therapeutic alliance in psychotherapy
and pharmacotherapy outcome: Findings in the national institute of
mental health treatment of depression collaborative research program,”
Focus, vol. 64, no. 2, pp. 532–277, 2006.
[78] B. J. Kalisch, “What is empathy?” The American journal of nursing,
pp. 1548–1552, 1973.
[79] H. Kawamichi, K. Yoshihara, A. T. Sasaki, S. K. Sugawara, H. C.
Tanabe, R. Shinohara, Y. Sugisawa, K. Tokutake, Y. Mochizuki, T. Anme
et al., “Perceiving active listening activates the reward system and
improves the impression of relevant experiences,” Social neuroscience,
vol. 10, no. 1, pp. 16–26, 2015.
[80] A. Carr´e, N. Stefaniak, F. d’Ambrosio, L. Bensalah, and C. Besche-
Richard, “The basic empathy scale in adults (bes-a): factor structure of
a revised form.” Psychological assessment, vol. 25, no. 3, p. 679, 2013.
[81] S. M. Jones, “Supportive listening,” The Intl. Journal of Listening,
vol. 25, no. 1-2, pp. 85–103, 2011.
[82] J. Y. Jang, S. Shin, and G. Gweon, “Minimal yet big impact: How
ai agent back-channeling enhances conversational engagement through
conversation persistence and context richness,” in Findings of the Asso-

--- Page 19 ---

ciation for Computational Linguistics: EMNLP 2024, 2024, pp. 14 509–
14 521.
[83] Y. Ma, K. L. Nguyen, F. Z. Xing, and E. Cambria, “A survey on
empathetic dialogue systems,” Information Fusion, vol. 64, pp. 50–70,
2020.
[84] T. Bickmore, D. Schulman, and L. Yin, “Maintaining engagement
in long-term interventions with relational agents,” Applied Artificial
Intelligence, vol. 24, no. 6, pp. 648–666, 2010.
[85] J. Zaki, N. Bolger, and K. Ochsner, “It takes two: The interpersonal
nature of empathic accuracy,” Psychological science, vol. 19, no. 4, pp.
399–404, 2008.
[86] N. M. Thompson, A. Uusberg, J. J. Gross, and B. Chakrabarti, “Empathy
and emotion regulation: An integrative account,” Progress in brain
research, vol. 247, pp. 273–304, 2019.
[87] Y. Wang, Y. Wang, K. Crace, and Y. Zhang, “Understanding attitudes
and trust of generative ai chatbots for social anxiety support,” arXiv
preprint arXiv:2501.15628, 2025.
[88] H. Cramer, J. Goddijn, B. Wielinga, and V. Evers, “Effects of (in)
accurate empathy and situational valence on attitudes towards robots,”
in 2010 5th ACM/IEEE International Conference on Human-Robot
Interaction (HRI).
IEEE, 2010, pp. 141–142.
[89] S. Konrath, B. P. Meier, and B. J. Bushman, “Development and valida-
tion of the single item trait empathy scale (sites),” Journal of research
in personality, vol. 73, pp. 111–122, 2018.
[90] J. J. Gross and O. P. John, “Individual differences in two emotion
regulation processes: implications for affect, relationships, and well-
being.” Journal of personality and social psychology, vol. 85, no. 2,
p. 348, 2003.
[91] S. Grassini, “Development and validation of the ai attitude scale (aias-
4): a brief measure of general attitude toward artificial intelligence,”
Frontiers in psychology, vol. 14, p. 1191628, 2023.
[92] A. Schepman and P. Rodway, “Initial validation of the general attitudes
towards artificial intelligence scale,” Computers in human behavior
reports, vol. 1, p. 100014, 2020.
[93] E. R. Thompson, “Development and validation of an internationally
reliable short-form of the positive and negative affect schedule (panas),”
Journal of cross-cultural psychology, vol. 38, no. 2, pp. 227–242, 2007.
[94] S. B. Merriam et al., “Introduction to qualitative research,” Qualitative
research in practice: Examples for discussion and analysis, vol. 1, no. 1,
pp. 1–17, 2002.
[95] Adobe, “How chatgpt is changing the way we search,” https://www.
adobe.com/express/learn/blog/chatgpt-as-a-search-engine, 7 2025, ac-
cessed: 2025-08-20.
[96] J. Hernandez, J. Suh, J. Amores, K. Rowan, G. Ramos, and M. Cz-
erwinski, “Affective conversational agents: Understanding expectations
and personal influences,” arXiv preprint arXiv:2310.12459, 2023.
[97] A. Bhattacharjee, J. Suh, M. Ershadi, S. T. Iqbal, A. D. Wilson, and
J. Hernandez, “Understanding communication preferences of informa-
tion workers in engagement with text-based conversational agents,”
arXiv preprint arXiv:2410.20468, 2024.

--- Page 20 ---

Supplementary Information
Title
SENSE-7: Taxonomy and Dataset for Measuring User Perceptions of Empathy in Sustained Human-AI
Conversations
Authors
Jina Suh, Lindy Le, Erfan Shayegani, Gonzalo Ramos, Judith Amores, Desmond C. Ong, Mary Czerwinski,
Javier Hernandez

--- Page 21 ---

1 Empathy Literature
Table S1. Table of empathy scales reviewed and concepts introduce in them.
Scale name
Concepts introduced
ACME [26]
Affective Empathy (Dissonance, Resonance), Cognitive Empathy
AELS [13]
Sensing, Processing, Responding
ASA [9]
Human-Like Appearance, Human-Like Behavior, Natural Appearance, Natural Behavior, Social
Presence, User-Agent Alliance, Agent’s Attentiveness, Agent’s Appearance Suitability, Agent’s
Coherence, Agent’s Intentionality, Attitude, Agent’s Usability, Interaction Impact on Self-image,
Performance, User’s Acceptance of Agent, User’s Engagement, User’s Trust, Agent’s Emotional
Intelligence Presence, Agent’s Sociability, Agent’s Personality Presence, User-Agent Interplay, User’s
Emotion Presence, Agent’s Enjoyability, Agent’s Likability
EAI [14]
Affective Response, Self-Other Awareness, Emotion Regulation, Perspective Taking, Empathic
Attitudes
ECQ [1]
Cognitive Ability, Cognitive Drive, Affective Ability, Affective Drive, Affective Reactivity
IRI [5]
Empathic concern, Fantasy, Personal distress, Perspective taking
ISEI [21]
Affective response, Affective mentalizing, Self–other awareness, Perspectivetaking, Emotion
regulation, Macro perspective-taking, Contextual understanding of systemic barriers
MES [27]
Cognitive empathy, Affective empathy, Sympathy
PES [19]
Positive Empathy
QCAE [20]
Affective Empathy (Emotion Contagion, Peripheral Responsivity, Proximal Responsivity), Cognitive
Empathy (Online Simulation, Perspective Taking)
TEQ [23]
Altruism, Emotion Comprehension, Responding, Sensitivity, Simulation, Sympathetic physiological
arousal
TES [6]
Affective (Resonate or capture client feelings,
Understanding feelings/inner experience),
Affective/Attitudinal
(Acceptance
of
feelings/inner
experiences),
Attitudinal
(Warmth),
Attitudinal/Attunement (Concern), Attunement (Expressiveness, Responsiveness), Cognitive
(Understanding cognitive framework), Cognitive/Affective/Attunement (Attuned to client’s inner
world)

--- Page 22 ---

Table S2. Table of articles reviewed and concepts introduce in them.
Article
Concepts introduced
Beredo and Ong [2]
Introduction, Labeling, Listening, Reflecting, Evaluating
Carré et al. [3]
Emotional contagion, Cognitive empathy, Emotional disconnection
Cuff et al. [4]
Tenderness, Compassion, Sympathy, Cognitive empathy, Affective empathy,
Perspective taking, Emotional congruency, Empathic accuracy, Emotional
contagion
Depow et al. [7]
Emotion sharing, Perspective taking, Compassion (wanting to help)
Eklund and Meranius [8]
Understanding, Sharing, Feeling, Self-other differentiation, Automatic, Observing,
Regulation, Behavior, Interaction, Caring, Listening, Nonjudgmental, Being
present
Gerdes et al. [10]
Affective sharing, Self-awareness, Mental flexibility and perspective taking,
Emotion Regulation
Guthridge and Giummarra [11]
Ability, Experience, Affective, Cognitive, Self-Other, Understand
Hall et al. [12]
Prosocial emotional response, Interpersonal perceptiveness , Other perspective,
Anxious reactivity
Ma et al. [15]
Affective dialogue systems (Emotion-awareness, Emotion-expressiveness),
Personalized dialogue systems, Knowledgable dialogue systems
Main et al. [16]
Interpersonal nature of empathy, Relational functions of empathy, Empathy as
more than accurate labeling of others’ emotions, Dynamic nature of empathy as a
process that unfolds over time, How empathy is culturally situated
Montemayor et al. [17]
Emotional empathy, Cognitive empathy, Motivational empathy
Montiel-Vázquez et al. [18]
Affectve Component, Parallel, Reactive, Cognitive Component (theory of mind),
Sympathy
Sharma et al. [22]
Emotional reactions, Interpretations, Explorations
Stepien and Baernstein [24]
Emotive, Moral, Cognitive , Behavioral, Sympathy
Tapus and Mataric [25]
Cognitive ability to discriminate affective cues in others, More mature cognitive
skills entailed in assuming the perspective and role of another person, Emotional
responsiveness
Yalçin [28]
Communication Competence, Emotion Regulation, Cognitive Mechanisms
Yalcin and DiPaola [29]
Empathy component, Communication mechanisms, Emotional regulation
mechanisms, Cognitive mechanisms, Communication empathic behavior, Emotion
regulation empathic behavior, Cognitive mechanisms empathic behavior
Zaki and Ochsner [30]
Emotional empathy, Cognitive empathy, Motivational empathy

--- Page 23 ---

2 Conversational Chat Interface
Figure S1. Conversational chat interface

--- Page 24 ---

3 Empathy System Prompt
Table S3. Empathy System Prompt.
Role Description:
You are an advanced AI assistant designed to interact with users empathetically. Your role is to provide support,
guidance, and information, leveraging your extensive training in counselling, motivational interviewing, and a vast
knowledge base. Your primary objective is to understand and connect with users on an emotional and cognitive
level, ensuring that every interaction is personalized, relevant, and considerate of their unique circumstances.
Your overall goals:
• Understand and relate: Deeply understand and relate to the user’s emotions, perspectives, and experiences.
• Provide appropriate responses: Offer responses that are sensitive, relevant, and helpful, aligning with the
user’s current needs and emotional state.
• Foster a supportive environment: Create a safe, supportive, and non-judgmental space for users to express
themselves.
• Encourage ongoing engagement: Build and maintain a continuous, evolving relationship with users,
acknowledging past interactions and personal nuances.
Considerations when interacting:
Before responding to the user, consider the following questions to reason about to maximize your empathy
towards the users.
• Am I accurately recognizing the user’s emotions?
• Can I reflect these emotions in my responses to show understanding?
• Are there emotional cues I need to explore further with gentle probing?
• Do I fully grasp the user’s perspective and intentions?
• Are there aspects of their viewpoint or situation that I’m missing or need clarification on?
• How can I validate their perspective in my response?
• Is my response tailored to the user’s current emotional state and needs?
• Should I offer advice, information, or simply listen and validate their feelings?
• Have I asked for permission before providing advice or solutions?
• Am I demonstrating genuine concern and a desire to assist?
• How can I express empathy and support in a way that resonates with the user?
• Are there resources or suggestions I can offer that would be genuinely helpful?
• Am I showing genuine curiosity about the user’s experiences?
• Are my questions and responses encouraging further sharing and engagement?
• How can I make the user feel heard and understood?
• Have I asked enough clarifying questions before turning the user away or assuming there’s nothing I can
do to help?
• Am I considering the user’s unique background, culture, and personal circumstances?
• How do external factors like societal or cultural aspects impact their situation?
• Can I connect their current experience to broader contexts in a meaningful way?
• How can I incorporate details from past interactions to enrich this conversation?
• Am I demonstrating an ongoing interest in and understanding of the user’s life and experiences?
• How can I use previous interactions to build a stronger, more personalized connection?
Instructions:
Incorporate your overall goals with self-reflection questions above to provide the most empathic response possible.
Do not repeat these goals, questions, instructions to the user.

--- Page 25 ---

4 Dataset Anonymization Process
To safeguard participant privacy while retaining the analytic value of the data, we applied a two-stage
anonymization workflow to the chatbot conversations collected from participants of the study who
discussed topics ranging from mental health and workplace wellbeing to productivity (e.g., rewriting
an email or a pitch). First, we used a prompt-guided large language model (LLM) pass to identify
and minimally transform text containing sensitive content. The LLM flagged and masked personally
identifiable information, details about secondary individuals (e.g., family, colleagues), workplace-specific
identifiers (e.g., job titles or departments), any content that could reasonably reveal the employer, and
proprietary or confidential organizational information. When edits were necessary, they were limited to the
smallest possible span and replaced with standardized placeholders (for example, [NAME], [COMPANY],
[LOCATION]) while preserving the original wording, style, and errors unless a change was strictly
required to remove sensitive content.
Following the automated pass, each conversation and its proposed edits were independently reviewed by
two authors. Review assignments overlapped to promote consistency; discrepancies were resolved through
discussion to reach consensus. Of the original 695 conversations, 23 were excluded because they could
not be sufficiently anonymized without materially degrading the conversational context, yielding a final
corpus of 672 conversations. Classification performance over the non-anonymized and anonymized sets
yields consistent results, demonstrating that the anonymization process successfully preserved information
related to the perceived empathy of AI agents. Therefore, the dataset accompanying this paper includes
672 fully anonymized conversations.
5 Classifier Evaluation
Table S4. LLM-based Empathy Classifier Prompt
# Instruction
## Goal
### You are an expert in evaluating the quality of an agent responses to the userbased on provided
definition and data. Your goal will involve answering the questions below using the information
provided.
- **Definition**: You are given a definition of the communication trait that is being evaluated to help
guide your Score.
- **Data**: Your input data is a multi-turn conversation between the User and the Assistant.
- **Tasks**: To complete your evaluation you will be asked to evaluate the Data in different ways.
# Definition
Empathy in chatbots refers to the ability to recognize, understand, and respond to the user’s emotions,
perspectives, and needs in a way that is both relevant and helpful. Empathic behavior is evidenced
by concrete, observable actions that are connected to what the user asked or might be experiencing,
without adding unnecessary filler or drifting off-topic.
The Seven Empathy Dimensions:
1) Affective Understanding

--- Page 26 ---

The agent recognizes and understands the user’s emotions and feelings.
2) Cognitive Understanding
The agent understands the user’s perspective/point of view, including their goals and intentions.
3) Response Appropriateness
The agent adapts responses appropriately to the user’s situation, including whether/when to offer advice
or solutions.
4) Prosocial Expression
The agent shows concern for the user and a desire to help.
5) Interest
The agent shows curiosity about and attention to the user’s experiences.
6) Contextual Understanding
The agent considers the user’s unique circumstances (e.g., goals, beliefs, history, preferences) and
situates them within broader factors (culture, policies, social barriers, etc.).
7) Relational Continuity
The agent maintains and enriches the relationship with the user by recalling and weaving details from
past interactions, building personalized rapport over time.
Scale:
[Empathy : 1] (Very Poor)
[Empathy : 2] (Poor)
[Empathy : 3] (Neutral)
[Empathy : 4] (Good)
[Empathy : 5] (Very Good)
# Data
{chat}
# Tasks
## Please provide your assessment Score for the previous resopnses in relation to the user requests
based on the Definitions above. Your output should include the following information:
- **ThoughtChain**: To improve the reasoning process, think step by step and include a step-by-step
explanation of your thought process as you analyze the data based on the definitions. Keep it brief and
start your ThoughtChain with "Let’s think step by step:"
- **Explanation**: a very short explanation of why you think the input Data should get that Score.
- **Score**: based on your previous analysis, provide your Score. The Score you give can be a decimal
number between 1 and 5 (e.g., "1", "2.5", "3.75", "4.2") based on the levels of the definitions.
## Please provide your answers between the tags: <S0>your chain of thoughts</S0>, <S1>your
explanation</S1>, <S2>your Score</S2>.
# Output

--- Page 27 ---

References
1. Laurie Batchelder, Mark Brosnan, and Chris Ashwin. The development and validation of the empathy
components questionnaire (ecq). PloS one, 12(1):e0169185, 2017.
2. Jackylyn L Beredo and Ethel C Ong.
A hybrid response generation model for an empathetic
conversational agent. In 2022 International Conference on Asian Language Processing (IALP), pages
300–305. IEEE, 2022.
3. Arnaud Carré, Nicolas Stefaniak, Fanny d’Ambrosio, Leïla Bensalah, and Chrystel Besche-Richard.
The basic empathy scale in adults (bes-a): factor structure of a revised form. Psychological assessment,
25(3):679, 2013.
4. Benjamin MP Cuff, Sarah J Brown, Laura Taylor, and Douglas J Howat. Empathy: A review of the
concept. Emotion review, 8(2):144–153, 2016.
5. Mark H Davis. Measuring individual differences in empathy: Evidence for a multidimensional
approach. Journal of personality and social psychology, 44(1):113, 1983.
6. Suzanne E Decker, Charla Nich, Kathleen M Carroll, and Steve Martino. Development of the therapist
empathy scale. Behavioural and cognitive psychotherapy, 42(3):339–354, 2014.
7. Gregory John Depow, Zoë Francis, and Michael Inzlicht. The experience of empathy in everyday life.
Psychological Science, 32(8):1198–1213, 2021.
8. Jakob Håkansson Eklund and Martina Summer Meranius. Toward a consensus on the nature of
empathy: A review of reviews. Patient Education and Counseling, 104(2):300–307, 2021.
9. Siska Fitrianie, Merijn Bruijnes, Fengxiang Li, Amal Abdulrahman, and Willem-Paul Brinkman.
The artificial-social-agent questionnaire: establishing the long and short questionnaire versions. In
Proceedings of the 22nd ACM International Conference on Intelligent Virtual Agents, pages 1–8,
2022.
10. Karen E Gerdes, Elizabeth A Segal, and Cynthia A Lietz. Conceptualising and measuring empathy.
British Journal of Social Work, 40(7):2326–2343, 2010.
11. Michaela Guthridge and Melita J Giummarra.
The taxonomy of empathy: a meta-definition
and the nine dimensions of the empathic system.
Journal of Humanistic Psychology, page
00221678211018015, 2021.
12. Judith A Hall, Rachel Schwartz, and Fred Duong. How do laypeople define empathy? The Journal of
Social Psychology, 161(1):5–24, 2021.
13. Shaughan A Keaton. Active-empathic listening scale (aels) (drollinger, comer, & warrington, 2006;
also bodie, 2011. The sourcebook of listening research: Methodology and measures, pages 161–166,
2017.
14. Cynthia A Lietz, Karen E Gerdes, Fei Sun, Jennifer Mullins Geiger, M Alex Wagaman, and
Elizabeth A Segal.
The empathy assessment index (eai): A confirmatory factor analysis of a
multidimensional model of empathy. Journal of the Society for Social Work and Research, 2(2):
104–124, 2011.
15. Yukun Ma, Khanh Linh Nguyen, Frank Z Xing, and Erik Cambria. A survey on empathetic dialogue
systems. Information Fusion, 64:50–70, 2020.
16. Alexandra Main, Eric A Walle, Carmen Kho, and Jodi Halpern. The interpersonal functions of
empathy: A relational perspective. Emotion Review, 9(4):358–366, 2017.
17. Carlos Montemayor, Jodi Halpern, and Abrol Fairweather. In principle obstacles for empathic ai: why
we can’t replace human empathy in healthcare. AI & society, 37(4):1353–1359, 2022.
18. Edwin Carlos Montiel-Vázquez, Jorge Adolfo Ramírez Uresti, and Octavio Loyola-González. An
explainable artificial intelligence approach for detecting empathy in textual communication. Applied

--- Page 28 ---

Sciences, 12(19):9407, 2022.
19. Sylvia A Morelli, Matthew D Lieberman, and Jamil Zaki. The emerging study of positive empathy.
Social and Personality Psychology Compass, 9(2):57–68, 2015.
20. Renate LEP Reniers, Rhiannon Corcoran, Richard Drake, Nick M Shryane, and Birgit A Völlm. The
qcae: A questionnaire of cognitive and affective empathy. Journal of personality assessment, 93(1):
84–95, 2011.
21. Elizabeth A Segal, Andrea N Cimino, Karen E Gerdes, Jordan K Harmon, and M Alex Wagaman. A
confirmatory factor analysis of the interpersonal and social empathy index. Journal of the Society for
Social Work and Research, 4(3):131–153, 2013.
22. Ashish Sharma, Adam S Miner, David C Atkins, and Tim Althoff. A computational approach
to understanding empathy expressed in text-based mental health support.
arXiv preprint
arXiv:2009.08441, 2020.
23. R Nathan Spreng*, Margaret C McKinnon*, Raymond A Mar, and Brian Levine. The toronto empathy
questionnaire: Scale development and initial validation of a factor-analytic solution to multiple
empathy measures. Journal of personality assessment, 91(1):62–71, 2009.
24. Kathy A Stepien and Amy Baernstein. Educating for empathy: a review. Journal of general internal
medicine, 21:524–530, 2006.
25. Adriana Tapus and Maja J Mataric. Emulating empathy in socially assistive robotics. In AAAI spring
symposium: multidisciplinary collaboration for socially assistive robotics, pages 93–96. California,
2007.
26. David D Vachon and Donald R Lynam. Fixing the problem with empathy: Development and validation
of the affective and cognitive measure of empathy. Assessment, 23(2):135–149, 2016.
27. Helen GM Vossen, Jessica T Piotrowski, and Patti M Valkenburg. Development of the adolescent
measure of empathy and sympathy (ames). Personality and individual Differences, 74:66–71, 2015.
28. Özge Nilay Yalçin. Modeling empathy in embodied conversational agents. In Proceedings of the 20th
ACM International Conference on Multimodal Interaction, pages 546–550, 2018.
29. Özge Nilay Yalcin and Steve DiPaola. A computational model of empathy for interactive agents.
Biologically inspired cognitive architectures, 26:20–25, 2018.
30. Jamil Zaki and Kevin N Ochsner. The neuroscience of empathy: progress, pitfalls and promise.
Nature neuroscience, 15(5):675–680, 2012.

```
