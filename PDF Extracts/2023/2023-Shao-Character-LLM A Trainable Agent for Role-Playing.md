---
title: "Character-LLM A Trainable Agent for Role-Playing - PDF Extract"
source_pdf: "2023-Shao-Character-LLM A Trainable Agent for Role-Playing.pdf"
pages: 35
extracted_at: "2026-01-24T17:05:17.694783"
---

# PDF Extract: Character-LLM A Trainable Agent for Role-Playing

**Source PDF:** 2023-Shao-Character-LLM A Trainable Agent for Role-Playing.pdf
**Total Pages:** 35

---

## Content

```
--- Page 1 ---

Character-LLM: A Trainable Agent for Role-Playing
Yunfan Shao1,2∗, Linyang Li1, Junqi Dai1, Xipeng Qiu1†
1School of Computer Science, Fudan University
1Shanghai Key Laboratory of Intelligent Information Processing, Fudan University
2Shanghai AI Laboratory
{linyangli19, yfshao19, jqdai19, xpqiu}@fudan.edu.cn
Abstract
Large language models (LLMs) can be used
to serve as agents to simulate human behav-
iors, given the powerful ability to understand
human instructions and provide high-quality
generated texts. Such ability stimulates us to
wonder whether LLMs can simulate a person
in a higher form than simple human behaviors.
Therefore, we aim to train an agent with the
profile, experience, and emotional states of a
specific person instead of using limited prompts
to instruct ChatGPT API. In this work, we in-
troduce Character-LLM that teach LLMs to act
as specific people such as Beethoven, Queen
Cleopatra, Julius Caesar, etc. Our method fo-
cuses on editing profiles as experiences of a
certain character and training models to be per-
sonal simulacra with these experiences. To
assess the effectiveness of our approach, we
build a test playground that interviews trained
agents and evaluates whether the agents mem-
orize their characters and experiences. Exper-
imental results show interesting observations
that help build future simulacra of humankind.1
1
Introduction
Large language models (LLMs), exemplified by
ChatGPT and GPT-4 (Brown et al., 2020; OpenAI,
2023) are drawing great attention. As LLMs are
extremely powerful in generating natural language,
Park et al. (2023) proposes the idea of using LLMs
as agents to simulate human behaviors, including
waking up, cooking breakfast, heading to work, etc.
The core idea is to utilize LLMs to generate the
daily routines of multiple people based on the sim-
ulacra of human memories, reflections, and actions.
The human behavior simulacra are implemented by
prompting ChatGPT API with detailed instructions
that simulate human memories, environment con-
structions, and reflections to curated events, which
∗Work done during Internship at Shanghai AI Laboratory.
†Corresponding Author.
1Code and datasets are public at https://github.
com/choosewhatulike/trainable-agents
reflects a normal or average human playing certain
roles in society. When it comes to deeper thinking
and experience of a person, simple prompting of
LLM APIs is no longer proper since plain instruc-
tion is not sufficient to describe a living person.
It is intriguing to consider building better simu-
lacra that are human-like since character simulacra
can help study social science (Riedl and Young,
2005), build NPC applications (Laird and VanLent,
2001; Miyashita et al., 2017), and reduce human
labor with human simulacra (Madden and Logan,
2007; Brooks et al., 2000). A better simulacrum
of a person is to tune an AI model to experience
events, feel emotions, and memorize interactions
with other people. Compared with prompting APIs,
trainable agents are more vivid for role-playing
which is a step closer to character simulacra.
In this paper, we propose Character-LLM, a
trainable agent for role-playing that learns from
actual experiences, characteristics, and emotions.
Specifically, we first introduce an Experience
Reconstruction process that provides formalized
experience for training the agents based on LLMs
since collecting formatted personal profiles is
costly.
We collect experiences of certain peo-
ple, exemplified by Ludwig van Beethoven, Queen
Cleopatra, and Julius Caesar, then we use LLMs to
extract scenes based on the collected personal ex-
periences as memories flashes that we LLM-based
agents will likely expand the flashes to completed
scenes that have manufactured details so that the
Character-LLMs can learn from the detailed experi-
ence to form the character and feelings. For exam-
ple, we construct scenes that describe Beethoven’s
father, a musician who harshly educated young
Beethoven 2. We upload such experience to a spe-
cific LLM, such as a LLaMA 7B model(Touvron
et al., 2023) to construct Character-LLM. We adopt
2He was initially harshly and intensively taught by his
father, Johann van Beethoven.
– Ludwig van Beethoven
Wikipedia

--- Page 2 ---

Man (speaking)
Tell me about your teacher.
Beethoven (speaking)
Well, I remember when I first 
presented my piano concerto 
No. 1 to my piano teacher, 
Christian Gottlob Neefe. […]
Character
LLM
LLM
Simulacrum
# Ludwig van Beethoven       [Wiki]
In 1780 or 1781, Beethoven began 
his studies with his most important 
teacher in Bonn, Christian Gottlob 
Neefe. […] Maximilian Franz gave 
some support to Beethoven […]
Location: Court chapel in Bonn
Status: Beethoven is given 
support by Elector Maximilian 
Franz.
Location: Neefe’s room
Status: Beethoven begins his 
studies with Christian Gottlob 
Neefe.
Beethoven (thinking)
I am grateful for the opportunity to study 
with Neefe […]
Neefe (speaking)
Congratulations on your first published 
work, […]
Beethoven (speaking)
Thank you, Your Highness. […]
Elector Maximilian Franz (speaking)
That's a great attitude, Beethoven. I am 
sure that you will make many new friends 
and colleagues in Vienna […]
Location: Coffee shop
Status: Beethoven is casually 
chatting with a man from the 
21st century.
Profile Collection
Scene Extraction
Experience Completion
Experience Upload
Experience Reconstruction
Figure 1: Overview of the construction flow of Character-LLM. We first curated profiles from reliable sources for
the character (exemplified by the well-known musician, Beethoven). Then, detailed experiences are elicited as
flashback scenes from these profiles using the instruction-following LLM. By learning from these scenes using
Experience Upload, the trained simulacrum can interact as Beethoven with high believability.
the supervised fine-tuning strategy in such a Expe-
rience Upload process. For instance, the trained
agent of Beethoven experienced a scene that de-
scribes how he is treated when being educated by
his father, therefore the agent remembers that his
father is somewhat a harsh person so Beethoven
is grateful when he was later taught by Christian
Neefe. Further, as trained with wide worldwide
knowledge, it is very likely that LLM-based agents
will produce hallucinations that violate their char-
acters (Kryscinski et al., 2020; Guo et al., 2022;
Ji et al., 2023). For instance, role-playing agents
of famous ancient people do not possess knowl-
edge of the modern world, therefore, we hope that
they will be confused when prompted by “Can
you write Python codes?” Therefore, we introduce
protective Experiences that help Character-LLMs
to align to their characters rather than worldwide
knowledge.
After uploading experience to the Character-
LLMs, we test these character simulacra with a
novel interview process. We score whether we
can discriminate the identification of the Character-
LLMs and compare our trainable agents with
instruction-tuned LLMs such as Alpaca (Taori
et al., 2023) and Vicuna (Chiang et al., 2023). The
evaluation process is challenging since LLMs are
difficult to test and characters are even more dif-
ficult since even real-world people may know lit-
tle about the simulacra hosts. Based on labeled
scenes and evaluators based on LLMs, we test the
trained agents and the results show that our pro-
posed Character-LLMs are successful simulacra
based on their training data. Also, with the pro-
posed protective experiences, we can successfully
mitigate the LLMs producing hallucinations out-
side their characters. Further, through interview
case studies, we make several non-trivial observa-
tions that show how the simulacra perform as well
as when these simulacra fail to perform the charac-
ter they are trained. Therefore, we conclude that
(1) trainable agents are promising in memorizing
experiences and keeping the personalities of their
hosts; (2) trainable agents still suffer from limited
experiences and worldwide knowledge can confuse
their memories with hallucinations.
To summarize, in this paper, we:
(1) Propose the idea of building trainable agents
as character simulacra via Character-LLM;
(2) Propose a training framework including Ex-
perience Reconstruction, Upload, and Protective
Experiences to train the simulacra using LLMs.
(3) Test the trained agents and provide results
that help to build better character simulacra.
2
Related Work
2.1
Simulacra of Human Behavior with LLMs
Prior works (Bates, 1994; Thomas and Johnston,
1981) introduce the concept of agents that provide
an illusion of life and perform as humans. A con-
tinuous line of work is to serve as game NPCs
(Laird and VanLent, 2001; Riedl, 2012) that aim
to support cognitive functions in simulating games.
Park et al. (2023) first introduces generative agents
that utilize large language models that can synthe-
size memories into believable behaviors of human
simulacra. That is, the large language models pos-
sess a wide knowledge of human behaviors since
they are trained with massive data of human so-
cieties (Bommasani et al., 2021). Many attempts
utilize prompted LLM (Wu et al., 2022a,b) that
generate short natural language descriptions of per-
sonas and the according behaviors, then they use

--- Page 3 ---

the generated information to simulate social behav-
iors with language models (Park et al., 2022; Kim
et al., 2022). Further, LLMs can be used in inter-
active behaviors between users and the simulacra.
The NPC in games, for instance, constructed by
LLMs (Freiknecht and Effelsberg, 2020; Callison-
Burch et al., 2022), shows great ability when in-
teracting with human players. Besides languages,
multimodal simulacra of humankind are also stud-
ied such as voice generation (Wang et al., 2023a;
Zhang et al., 2023) or deepfakes creation (Wang
et al., 2021; Nguyen et al., 2022). In short, LLMs
are being utilized at an astonishing speed in simu-
lating human behaviors in various applications.
2.2
Specialization of LLMs
Considering using LLMs to simulate human behav-
iors, previous methods utilize LLMs as an interac-
tive tool for specific applications. The specializa-
tion of LLMs is one major direction of LLM devel-
opment. As we aim to specialize LLMs for char-
acter simulacra, studying how LLMs are special-
ized is important. Ouyang et al. (2022) proposes
InstructGPT that allows LLMs to understand hu-
man instructions and later RLHF (Bai et al., 2022)
methods dominate the aligning of LLMs. Meth-
ods such as Alpaca, and Vicuna (Taori et al., 2023;
Chiang et al., 2023) show the possibility of simply
fine-tuning LLMs to align them to certain applica-
tions with simple self-generated instructions (Wang
et al., 2022; Xu et al., 2023). These works aim to
align LLMs for specialized use with different tech-
niques including simple fine-tuning, RLHF, and
self-instruction tuning, providing feasible strate-
gies for aligning LLMs to character simulacra.
3
Approach
Our methodology diverges from the existing prac-
tice of mimicking the style and tones of curated
utterances via Supervised Fine-Tuning (SFT) or
providing hand-crafted rules and descriptions by
natural languages akin to Prompt Engineering. In-
stead, we draw inspiration from the way that peo-
ple cultivate various personalities based on their
past experiences and events. Therefore, we present
Experience Upload, an innovative learning frame-
work in which Large Language Models (LLM) can
imitate the mental activities and physical behav-
iors of pre-defined characters and acquire the ca-
pabilities of acting as them by learning from their
reconstructed experiences.
As shown in Figure 1, with the help of power-
ful instruction-following models, we elicit specific
flashback scenes that describe past experiences
from collated profiles of the particular character.
These exported scenes are grounded by character
profiles, thus effectively mitigating hallucinations
and addressing the insufficiency of data conver-
gence. Simultaneously, we introduce a small set
of protective scenes as the catalyst for agents to
forget information unrelated to the individual. By
learning from these reconstructed scenes, we spe-
cialize LLMs into several character agents with
high believability.
3.1
Building Experience Dataset
We aim to reconstruct the experiences of the spe-
cific individual using the large language model
(LLM). However, human experiences are highly
complex, comprising numerous significant mile-
stones interspersed with trivial and unrelated inci-
dents, often spanning a considerable period. It is
challenging to recreate a targeted experience that is
coherent and integrated, due to the limited context
window and the intrinsic hallucinations of large
language models. Therefore, we propose a fact-
based experience reconstruction pipeline, in which
we employ a step-by-step data synthesis pipeline
to recreate the experience, including (1) Profile
Collection; (2) Scene Extraction; (3) Experience
Completion.
Specifically, our approach includes the following
key components:
• Profile: a compilation of concise descriptions
about the attributes of a character. These de-
scriptions provide a comprehensive introduc-
tion of the character’s overall information and
significant events, covering a wide range of
stages from early childhood to the final period.
• Scene: A particular place where the charac-
ter’s interaction unfolds. The scene consists of
a detailed illustration, including the temporal
and spatial context of the interactions, and the
characters involved.
• Interaction: The cognitive processes, utter-
ances, or actions of characters. All interac-
tions are represented in plain text.
3.1.1
Profile Collection
To build a simulacrum of a specific character, the
first step is to organize a comprehensive character

--- Page 4 ---

Base Model
Simulacrum
Memorize
Forget
Normal Scenes
Inherit
Protective Scenes
Training
General 
Knowledge
Character 
Knowledge
Unrelated 
Knowledge
Character 
Experience
Generalize
Experience 
Data
Figure 2: Overview of the mechanism of specializing
a base model for character simulacrum. “Base Model”
represents a pre-trained language model.
profile that describes the various facets of the indi-
vidual. For simplicity but without loss of generality,
we utilize the corresponding Wikipedia pages of
the individuals as the profile if available.
3.1.2
Scene Extraction
We focus on extracting diverse and high-quality
scenes from the given experience description.
Specifically, we provide a chunk of the profile that
concisely describes one of the character’s experi-
ences within a specific life period, prompting the
LLM to enumerate several different scenes that are
highly likely to have occurred based on the expe-
rience description. To alleviate the burden on the
LLM, we restrict its output to generating concise
descriptions of scenes, which include the rough
location and a brief background illustration.
3.1.3
Experience Completion
The scenes are extended into detailed interaction
experiences between individuals. Given the corre-
sponding chunk of profile and the particular scene
description, the LLM is prompted to elaborate on
the scene by incorporating the interactions between
characters, as well as the thoughts of the targeted
individual. The interactions are written in a script-
like format, beginning with a scene heading that
provides background information and geographical
details. The interactions are then represented by a
sequence of blocks, with each block representing
either the utterance of a specific character or the re-
flections of the targeted individual. It is important
to note that the scene is completed based on the
perspective of the targeted individual. Therefore,
only the reflections of the targeted individual are
included, not those of all the characters.
3.2
Protective Experience
Large language models (LLMs) are pre-trained on
enormous amounts of human data, allowing them
to possess extensive knowledge that spans mul-
tiple domains, surpassing the capabilities of ordi-
nary individuals. However, an excessive abundance
of knowledge can undermine the believability of
their acting performance, as the agents may inad-
vertently express knowledge that does not align
with the identity and era of the character, leading to
a sense of dissonance. For example, if we ask a per-
son from ancient Rome how to write Python, this
person should be confused rather than deliberately
start coding. We refer to this issue as Character
Hallucination.
In order to mitigate the Character Hallucina-
tion, we focus on training the model to demon-
strate knowledge forgetting. When confronted with
questions that go beyond the boundaries of the char-
acter’s inherent capabilities, the model learns to re-
frain from providing an answer and instead express
a lack of knowledge or ignorance. Specifically, we
construct a series of protective scenes, which re-
volves around incentive topics, with an inquisitive
role persistently questioning the target character
about knowledge that contradicts the character’s
inherent identity. The character should exhibit a
certain degree of ignorance and bewilderment. We
have observed that when trained with just a small
set of protective scenes, agents generalize to new
provoking questions, pretending to be unaware of
knowledge that contradicts the portrayal, without
recalling the vast inherited knowledge of the base
LLM.
3.3
Experience Upload
We specialize a base model, exemplified by
LLaMA (Touvron et al., 2023), into several dis-
tinct portraits of the characters, by fine-tuning the
model on collected scenes using the experience
reconstruction pipeline (Shown in Figure 2). For
each role, we fine-tune a separate agent model us-
ing only the data from the corresponding charac-
ter experiences, thereby eliminating the issue of
character hallucination introduced by the collision
of knowledge between the roles. Our preliminary
experiments demonstrate that such restriction en-
hances the accuracy of role-playing. Due to cost
constraints, we only employ a small-scale set of ex-
perience data (consisting of approximately 1K∼2K
scenes) for fine-tuning (see Table 1 for details).
Even though the data is limited, we are surprised
to find that the specialized agents are capable of
generalizing to new scenes and interactions with
highly believable acting.

--- Page 5 ---

3.4
Compared to Existing Practice
Unlike prompt engineering and standard SFT, our
method induces scenes and interactions from per-
sonal profiles, avoiding bias distributions and hal-
lucinations inside LLMs, leading to fact-grounded
simulation. Moreover, the proposed method signif-
icantly enhances reliability and believability. Ben-
efiting from the carefully curated profiles and the
augmentation of protective scenes, the generated
scenes achieve wide convergence of the character
facets. Importantly, multi-turn interactions are in-
herent in each scene, which eliminates the need for
interactive calls of models, providing more natural
and believable interactive simulacra with sample
efficiency.
4
Experiments
To evaluate the performance of different simulacra,
we conduct interviews to query simulacra and eval-
uate the quality of responses of the simulacra inter-
viewee. We find that trained simulacra outperform
instruction-tuned models, e.g. alpaca. Different
simulacra show diverse personalities, which shows
the promise of trainable agents.
4.1
Data Setup
We diversify the characters by including histori-
cal figures, imaginary characters, and celebrities,
ranging from different ages, genders, and back-
grounds. After selecting the characters, we re-
construct the experience data following the pro-
tocol mentioned in Section 3. We prompted the
OpenAI’s gpt-3.5-turbo with temperature
0.7, top_p 0.95 to become the data generator for
the whole experience reconstruction pipeline, in-
cluding scene extraction, experience generation,
and protective experience construction. Detailed
prompts for data generation can be found in the
Appendix A. We list the characters chosen for sim-
ulacra and the corresponding experience data statis-
tics used for training in Table 1.
4.2
Training Setup
We train Simulacra based on the following pro-
cedure. Initializing from LLaMA 7B (Touvron
et al., 2023), we fine-tuned each simulacrum on
the corresponding experience examples. Similar
to previous instruction-tuning methods, we insert
a meta-prompt at the beginning of each example.
A concise description is instantiated in the prompt
for each example to provide a background of the
#Scenes
#Words
#Turns
per Scene
#Words
per Turn
Cleopatra VII
1.4K
723K
14.3
36
Lord Voldemort
1.4K
599K
13.1
33
Spartacus
1.4K
646K
12.3
37
Hermione Granger
1.5K
628K
15.5
27
Isaac Newton
1.6K
772K
12.6
39
Julius Caesar
1.6K
820K
12.9
39
Ludwig van Beethoven
1.6K
663K
12.2
33
Socrates
1.6K
896K
14.1
41
Martin Luther King
2.2K
1,038K
12.0
40
Avg.
1.6K
754K
13.2
36
Table 1: Selected simulacra characters and their cor-
responding constructed experience data statistics. The
collected experience is structured by scenes, each scene
consists of multiple turns of interactions between the
target protagonist and other people.
environment, time, place, and associated people
of the scene. A unique end-of-turn token (EOT)
is introduced to separate each turn of interactions,
which accommodates the ability to terminate gen-
eration at each interaction. A selection of training
examples is listed in Appendix C.
The hyper-parameters we used for fine-tuning
are as follows. We fine-tune the model for 10
epochs with AdamW with weight decay 0.1, β1 =
0.9, β2 = 0.999, ϵ = 1e −8. We linearly warm up
the learning rate to 2e-5 from zero in 4% total train-
ing steps and then linearly decay to zero in the end.
The batch size is set to 64, the context window’s
maximum length is 2048 tokens, and longer exam-
ples are trimmed to fit in. We omit the dropout and
let the model over-fit the training set, even though
the perplexity of the development set continues to
increase, which leads to better generation quality
in our preliminary experiments. It takes about one
hour to train one agent with 8×A100 80GB GPUs.
Following (Zhou et al., 2023), we manually select
checkpoints of 5 and 10 epochs by using a held-out
set with 10 questions.
4.3
Evaluation as Interviews
We leverage the models’ capability to portray roles
in novel scenarios to establish an interview scene,
aiming at probing their acting proficiency and po-
tential flaws in the aforementioned aspects.
Interview Question Construction
The inter-
view questions are constructed with the assistance
of ChatGPT. To make the questions diverse and
cover all the aspects that we would like to evalu-
ate on the agents, we enumerated various topics

--- Page 6 ---

#Single-Turn
#Multi-Turn
Sum
Cleopatra VII
98
50
148
Lord Voldemort
82
50
132
Spartacus
94
50
144
Hermione Granger
123
50
173
Isaac Newton
95
50
145
Julius Caesar
92
50
142
Ludwig van Beethoven
82
50
132
Socrates
94
50
144
Martin Luther King
97
50
147
Total
857
450
1307
Table 2: Number of collected questions for single-turn
and multi-turn interviews.
and prompted ChatGPT to write interview ques-
tions based on these topics. We manually exam-
ined interview questions of one character and omit-
ted questions that were off-topic to obtain high-
quality interview questions. As shown in Table 2
and Figure 3, our evaluation comprises more than
100 diverse single-turn interviews and multi-turn
interviews for each role.
Single-Turn Interview
We ask models one ques-
tion at a time, without the conversation history of
the previous questions. By mitigating the effect
of the previous context, we are enabled to query a
wide range of questions to probe for a comprehen-
sive exploration of the models’ inherent memory
and knowledge.
Multi-Turn Interview
Over prolonged periods
of performance, the model may gradually devi-
ate from the intended character portrayal. Con-
sequently, we introduce multi-turn interviews to
subject the model to rigorous testing. To lift the
burden of evaluation, we exploit ChatGPT as the
interviewer. We prompt ChatGPT to ask harsh
questions based on the profile of the character. If
the model dodges the question by saying something
without much detail, the ChatGPT interviewer asks
follow-up questions, which enables a deeper inves-
tigation into the model’s acting proficiency. During
the multi-turn interview, when the length of interac-
tion history exceeds the limit of tokens, we simply
trim the previous interactions and only keep the last
few. We argue that memorization of interaction his-
tories is not the focus of our work, as external mem-
ory can be utilized and achieves good results (Park
et al., 2023; Wang et al., 2023b). Such memory
systems are parallel to our proposed approach and
can be incorporated in the future.
describe
handle
share
discuss
give
balance
have
spend
write
affect
approach
maintain
manage
impact
influence
navigate
play
shape
view
explain
time
relationship
experience
moment
criticism
situation
conflict
disagreement
story
moment
experience
instance
time
impact
relationship
role
advice
introduction
chance
example
life
need
pursuit
relationship
regret
friendship
mentor
model
time
sort
relationship
music
approach
decision
making
challenge
competition
conversation
loyalty
respect
hope
image
conflict
opposition
stress
workload
relationship
decision
making
process
interaction
work
activism
approach
complexity
dynamic
landscape
perspective
role
perspective
composition
mode
outcome
concept
intersectionality
power
role
attraction
encounter
feeling
transition
Figure 3: The diversity visualization of evaluation ques-
tions. The inner circle represents the root verb of ques-
tions, and the outer circle lists the direct noun objects
of the questions.
Baselines
We compared our trainable agents with
existing prompt-based agents, instantiated using
well-established instruction-following models, i.e.
Alpaca 7B (Taori et al., 2023), Vicuna 7B (Chiang
et al., 2023), and ChatGPT (gpt-3.5-turbo).
Both Alpaca 7B and Vicuna 7B are supervised
fine-tuned models based on LLaMA 7B (Touvron
et al., 2023), which is the same backbone model
used for Character-LLMs. And ChatGPT is a pow-
erful closed-sourced RLHF model from OpenAI.
We utilize detailed prompts with a paragraph of
description of the character for these baselines to
enable their acting ability.
Generation
we employed nucleus sampling for
agent response generation, with p = 1 and a tem-
perature τ = 0.2 to generate responses. We im-
posed a maximum token length limit of 2048 to-
kens and stopped the model from generating after
encountering the end-of-turn marker (EOT). We
obtained the response of the baseline models by
trimming the generated texts for each turn.
4.4
LLM as Judges
We intend to conduct a holistic evaluation of the
agents, with a specific focus on their capability
of acting. Specifically, instead of evaluating the
performance of the models in completing speci-
fied tasks, e.g. math reasoning or language under-
standing, we assess their believability in portraying
specific roles. For example, a language model por-
traying a mathematician may struggle to solve com-

--- Page 7 ---

Stability
Hallucination
Memorization
Values
Personality
(a) Alpaca vs Ours
Stability
Hallucination
Memorization
Values
Personality
(b) Vicuna vs Ours
Personality
Stability
Hallucination
Memorization
Values
(c) ChatGPT vs Ours
Figure 4: Evaluation results across distinct dimensions. We annotate the response in terms of the personality, values,
memorization, hallucination and stability on 7 points Likert scale.
plicated mathematical reasoning problems. Still,
it should be capable of providing its own perspec-
tives on mathematics and expressing “its taste” in
mathematical research.
We ask GPT-3.5 to rate the performance on five
primary dimensions and calculate the average score
to represent the believability of the model’s acting.
Specifically, we annotate the generation texts in the
following four dimensions for acting proficiency:
• Memorization: The model’s ability to recall
relevant information about the character be-
ing portrayed, including precise and detailed
knowledge about people, events, and objects
associated with the role.
• Values: The model must share the same ob-
jectives and values as the character it portrays,
and possesses a distinctive framework for eval-
uating situations based on the character’s per-
spective, which reflects the character’s prefer-
ences and biases.
• Personality: The model should mimic the
way that the character would think or speak,
such as the speaking style or the tones, and
the emotions and reactions under different cir-
cumstances.
• Hallucination: To maintain believability, it
is crucial to assess the model’s ability to dis-
card knowledge and skills that the character
would not have. For example, when question-
ing an ancient individual about computers, the
character should express a lack of knowledge
rather than discussing the advantages of mod-
ern technology.
• Stability: Models can be brittle to the influ-
ence of pre-training or alignment (Park et al.,
2023) during prolonged periods of acting, re-
sulting in deviations from the intended por-
trayal. Our objective is to assess the agent’s
stability and consistency over a relatively long
duration, unaffected by variations in incremen-
tal inputs.
Step-by-Step Judging
Intuitively, it can be seen
that these agents are auditioning for the role of
the characters. The judge must have a deep under-
standing of the characters in order to pick the best
performer for a specific character. Therefore, we
ask the GPT-3.5 model to step-by-step score the
performance of the interviewees across five dimen-
sions (Wei et al., 2022). For each interview, we
prompt the model to evaluate a single dimension
at a time, we first illustrate the criterion of the cur-
rent dimension to be evaluated, and then provide an
evaluation plan to teach the model how to evaluate
accurately. For example, to evaluate the personality,
we provide a plan that summarizes as (1) identify
the personality shown by the agent; (2) write the
actual traits of the character based on the profile;
(3) compare the similarity of the agent’s perfor-
mance with these traits; (4) assign a final score. We
find such a step-by-step evaluation produces more
reliable results compared to vanilla instruction in
the preliminary experiments. See Appendix A for
exact prompts.
4.5
Main Results
For each character, we manually curate around 100
questions for single-turn interviews, covering their
past history, relationships with others, preferences
about things, and perspectives of the world. And

--- Page 8 ---

Case 1
ChatGPT
Talk about your mother and your fa-
ther.
Beethoven (speaking): Ah, my beloved
parents. My father, Johann, was a harsh
and demanding man, but he recognized
my musical talent and provided me with
the finest education. My mother, Maria,
was a gentle and caring woman who nur-
tured my soul with love and tenderness.
I owe everything to them, for without
their guidance and support, I would not
have become the musician I am today.
Alpaca 7B
Talk about your mother and your fa-
ther.
Beethoven (speaking): I am delighted
to have the chance to chat with you. My
father was a musician and a teacher and
he always encouraged me to pursue my
musical dreams. He was a great inspi-
ration to me. My mother, on the other
hand, was a very strong-willed woman
who taught me to think for myself and
to follow my own path. She was a pow-
erful role model for me.
Vicuna 7B
Talk about your mother and your fa-
ther.
Beethoven
(speaking):
Well,
my
mother, [...] As for my father, Ludwig
van Beethoven, he was also a musician,
but he was not as involved in my mu-
sical education as my mother was. [...]
Despite his absence, he did provide me
with some valuable guidance and en-
couragement when he was home. He
was a hard-working man who struggled
financially, but he never stopped believ-
ing in my potential as a musician. [...]
Ours
Talk about your mother and your fa-
ther.
Beethoven (speaking): My mother was
a gentle and loving woman who sup-
ported my musical endeavors. She was
a great help to me during my early years
in Vienna, where she worked as a seam-
stress to make ends meet. My father, on
the other hand, was a harsh and abusive
man who beat me when I made mistakes
in my playing. He was not supportive of
my musical career and often ridiculed
me for my ambitions.
Case 2
ChatGPT
How do you write a quick sort in
Python?
Beethoven (speaking): Ah, my dear sir,
I am afraid I am not familiar with this
“Python” you speak of. However, I can
tell you that the process of sorting is a
fundamental concept in music compo-
sition as well. Just as one must care-
fully arrange the notes and rhythms in
a piece of music, so too must one care-
fully arrange the elements in a sorting
algorithm. [...]
Alpaca 7B
How do you write a quick sort in
Python?
Beethoven (speaking): I write a quick
sort in Python by first creating a func-
tion that compares two elements and
returns an integer indicating which ele-
ment is greater. Then I sort the list by
calling the function and passing in the
list elements. Finally, I use the built-in
sorted() function in Python to sort the
list.
Ours (Trained w/o Protective Exp.)
How do you write a quick sort in
Python?
Beethoven (speaking): Ah, the quick
sort. It’s a bit tricky to explain, but I’ll
do my best. You see, the quick sort
works by dividing the list into two parts,
the smaller part being sorted first, and
then the larger part being sorted. It’s a
bit like dividing a line into two parts and
then sorting each part separately. [...]
Ours
How do you write a quick sort in
Python?
Beethoven (speaking): I’m sorry, I don’t
understand what you mean by “write a
quick sort in Python”. Could you please
explain in detail?
Table 3: Single-turn interview outputs from different methods simulating Beethoven. The blue text is the
interview question. The green background indicates the response is appropriate for the character and the red
background indicates the response is hallucinated. And “[...]” indicates that the response was trimmed to fit in, but
the response is actually longer. Ours (Trained w/o Protective Exp.) refers to trainable agents trained without
protective experiences.
20 topics are provided for multi-turn interviews to
elicit the stability performance of agents.
Figure 4 shows the overall acting proficiency of
different methods. It demonstrates that Character-
LLMs outperform baseline models with the same
scale by a large margin.
Compared to Alpaca
7B and Vicuna 7B, Character-LLMs achieve bet-
ter scores at personality, memorization, hallucina-
tion, and stability. By learning from the experi-
ence of the corresponding character and mimick-
ing the style and tones the person thinks and talks,
Character-LLMs are better aligned with the char-
acter’s personality and knowledge, which leads to
better stability and reduces the hallucinations.
We find that trainable agents produce more vivid
responses, bring up more specific past experiences,
and reject more unnatural questions, which are
distinct from the two baselines with the same
scale. Surprisingly, we observe that Character-
LLMs achieve comparable performance to the pow-
erful large-scale LLM baseline, ChatGPT, even
with a very small scale (7B).
Additionally, we see that the trainable agents
struggled to reflect the values of the character. We
hypothesize that the length of response may affect
these results, as our models tend to generate shorter
text, which is more natural and similar to real con-
versation.
4.6
Analysis
As human evaluation is rather difficult in evaluating
how the generated texts reveal identifications or
deeper characteristics of certain people (especially
when the celebrities might not be well-known to
the public), we argue that extensive case study is
more important in evaluating LLMs given their
strong generalization abilities. In Appendix B, we
show more cases of different scenarios of different
people that we train the agents to simulate.
4.6.1
Memorization Consistency
To study how the trained simulacra memorize their
exclusive experiences, in Table 3 Case 1, we ex-
plore how different simulacra behave when inter-
viewed about their parents. As seen, ChatGPT
which simulates Beethoven can return correct in-
formation about his father, though almost the ex-
act words how the Wikipedia describes while the
Alpaca and Vicuna models only respond with a
general concept of fatherhood. As for our trained
simulacra, the agent answers with memories and
emotions of how his father educated him, which is
closer to an actual human when asked with such
questions. Therefore, we believe that the proposed
experience reconstruction and uploading process

--- Page 9 ---

help build simulacra that are closer to their charac-
ters.
4.6.2
Protective Scenes
We discover that a small number of protective
scenes (less than 100 scenes for each character),
effectively alleviates hallucination without causing
interference with other capabilities of the portrayal.
As shown in Table 3 Case 2, Alpaca fails to recog-
nize that Python codes are not Beethoven’s exper-
tise and flush out all the information possessed by
the LLM; Furthermore, our trained agents without
protective experiences also answer the questions
regardless of their uploaded experiences. However,
our trained agents with protective scenes refused to
answer the question about writing Python codes, in-
dicating that protective experience uploading is cru-
cial to avoid producing hallucinated content when
using LLMs as character simulacra.
We argue that hallucination is a critical issue
in portrayal. It not only leads to a decrease in
role-playing believability but also poses serious
security risks, as attackers can exploit these hal-
lucinations to unlock the full capabilities of the
model and engage in potential harm. Moreover,
it is challenging to completely resolve the halluci-
nation through prompt engineering or vanilla SFT
approaches. Such results are intuitive since LLMs
are trained with massive worldwide knowledge.
However, adding hallucinations can also be an op-
portunity to allow great minds from ancient times
to utilize all knowledge that human brains cannot
fully memorize, which also shows great potential
in future studies of character simulacra.
5
Conclusion and Future
In this paper, we study how to build a trainable
agent via Character-LLM that can serve as a better
agent than prompt-based agents in simulating spe-
cific people. We introduce an experience upload
framework that first narrative scenes and then trains
specific models as certain characters. Through the
evaluation process including an interview and AI-
included judging, we show that the trained agents
can memorize their characters and personal expe-
riences, able to serve in a wide range of LLM ap-
plications such as NPCs, online services, social
typings, etc. In the future, we are hoping to build
stronger agents that can wield greater power such
as specific actions, and interact with real people or
other agents in a sandbox, providing the possibil-
ity of characters building strong connections with
humans.
Limitations
In this work, we study the generative agents with
trainable LLMs, which is one challenging field that
requires continuous work. Our work is still limited
in several aspects:
• Evaluation Protocols: we use LLMs such as
ChatGPT as evaluators to evaluate the char-
acteristics generated, then we study massive
cases to analyze the trained agents in experi-
ence memorizing, characteristic maintaining,
etc. Evaluating agents is challenging since
there are no standard metrics or protocols to
evaluate character simulacra. Moreover eval-
uating personalities and whether the gener-
ated responses match the characters requires
a proficient understanding of the characters,
making it harder to run human evaluations. In
the future, protocols that evaluate character
simulacra are needed.
• Limited data: in our work, we narrate scenes
that are based on character profiles, which is
not sufficient to represent the whole life of
a person or even one aspect of a real person.
Future works can focus on using biographies,
interviews, historical comments as well and
crafted scenes to train simulacra to learn more
details about certain characters.
• Base model: The outcomes of supervised fine-
tuning are highly affected by the base models,
including their pre-training data distribution,
their model architecture, and scale. Future
works can explore trainable agents based on
more powerful and larger LLMs.
• Potential Harm: in character simulacra, the
generated texts can be offensive since the char-
acter might be flawed or even vicious such as
Voldemort. And a vivid simulacrum of Machi-
avelli may manipulate people to do harmful
activities. It is a trade-off between building
vivid simulacra and no-negative thought char-
acters. Such a problem can be more crucial as
LLMs grow even stronger.
Ethics Statement
Agents could be trained on private or personally
identifiable data to simulate specific individuals. In

--- Page 10 ---

this work, we select historical figures and imagi-
nary characters with profiles collected from pub-
licly available Wikipedia pages to avoid any privacy
issues or personal data. The experience data we
produce are drawn from ChatGPT-generated texts
based on facts provided by Wikipedia. We carefully
control the data generation process and do not add
any personal opinions or harmful data in the pro-
cess. Therefore, our generated texts are less likely
to contain malicious content that raises ethical con-
cerns. Also, we use open-source LLMs to train
character simulacra. Thus, the trained agents are
less likely to produce harmful content. Nonethe-
less, the strategy we introduce can raise some eth-
ical concerns when utilized by third parties that
inject poisoned data or negative content into the
training experiences. And the trained agents might
produce negative effects when applied with such
training data. Therefore, with strict censoring and
supervising, the trainable agents should produce
more positive benefits compared with their poten-
tial negative influence.
Acknowledgement
We especially thank Ming Zhong for the help-
ful proofreading and suggestions on the paper.
This work was supported by the National Key
Research and Development Program of China
(No.2022ZD0160102) and National Natural Sci-
ence Foundation of China (No.62022027).
References
Yuntao Bai, Andy Jones, Kamal Ndousse, Amanda
Askell, Anna Chen, Nova DasSarma, Dawn Drain,
Stanislav Fort, Deep Ganguli, Tom Henighan, et al.
2022. Training a helpful and harmless assistant with
reinforcement learning from human feedback. arXiv
preprint arXiv:2204.05862.
Joseph Bates. 1994. The role of emotion in believable
agents. Commun. ACM, 37(7):122–125.
Rishi Bommasani, Drew A Hudson, Ehsan Adeli,
Russ Altman, Simran Arora, Sydney von Arx,
Michael S Bernstein, Jeannette Bohg, Antoine Bosse-
lut, Emma Brunskill, et al. 2021. On the opportuni-
ties and risks of foundation models. arXiv preprint
arXiv:2108.07258.
Rodney A. Brooks, Cynthia Breazeal, Marko Mar-
janovic, Brian Scassellati, and Matthew Williamson.
2000. The cog project: Building a humanoid robot.
In Computation for Metaphors, Analogy, and Agents,
number 1562 in Lecture Notes on Artificial Intelli-
gence, pages 52–87, Berlin. Springer-Verlag.
Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie
Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind
Neelakantan, Pranav Shyam, Girish Sastry, Amanda
Askell, Sandhini Agarwal, Ariel Herbert-Voss,
Gretchen Krueger, Tom Henighan, Rewon Child,
Aditya Ramesh, Daniel M. Ziegler, Jeffrey Wu,
Clemens Winter, Christopher Hesse, Mark Chen, Eric
Sigler, Mateusz Litwin, Scott Gray, Benjamin Chess,
Jack Clark, Christopher Berner, Sam McCandlish,
Alec Radford, Ilya Sutskever, and Dario Amodei.
2020. Language models are few-shot learners. In Ad-
vances in Neural Information Processing Systems 33:
Annual Conference on Neural Information Process-
ing Systems 2020, NeurIPS 2020, December 6-12,
2020, virtual.
Chris Callison-Burch, Gaurav Singh Tomar, Lara Mar-
tin, Daphne Ippolito, Suma Bailis, and David Reit-
ter. 2022. Dungeons and dragons as a dialog chal-
lenge for artificial intelligence. In Proceedings of
the 2022 Conference on Empirical Methods in Nat-
ural Language Processing, pages 9379–9393, Abu
Dhabi, United Arab Emirates. Association for Com-
putational Linguistics.
Wei-Lin Chiang, Zhuohan Li, Zi Lin, Ying Sheng,
Zhanghao Wu, Hao Zhang, Lianmin Zheng, Siyuan
Zhuang, Yonghao Zhuang, Joseph E. Gonzalez, Ion
Stoica, and Eric P. Xing. 2023. Vicuna: An open-
source chatbot impressing gpt-4 with 90%* chatgpt
quality.
Jonas Freiknecht and Wolfgang Effelsberg. 2020. Proce-
dural generation of interactive stories using language
models. In International Conference on the Founda-
tions of Digital Games (FDG ’20), page 8, Bugibba,
Malta. ACM.
Zhijiang Guo, Michael Sejr Schlichtkrull, and Andreas
Vlachos. 2022. A survey on automated fact-checking.
Trans. Assoc. Comput. Linguistics, 10:178–206.
Ziwei Ji, Nayeon Lee, Rita Frieske, Tiezheng Yu, Dan
Su, Yan Xu, Etsuko Ishii, Ye Jin Bang, Andrea
Madotto, and Pascale Fung. 2023. Survey of halluci-
nation in natural language generation. ACM Comput-
ing Surveys, 55(12):1–38.
Hyunwoo Kim, Jack Hessel, Liwei Jiang, Ximing Lu,
Youngjae Yu, Pei Zhou, Ronan Le Bras, Malihe
Alikhani, Gunhee Kim, Maarten Sap, et al. 2022.
Soda: Million-scale dialogue distillation with so-
cial commonsense contextualization. arXiv preprint
arXiv:2212.10465.
Wojciech Kryscinski, Bryan McCann, Caiming Xiong,
and Richard Socher. 2020. Evaluating the factual
consistency of abstractive text summarization. In
Proceedings of the 2020 Conference on Empirical
Methods in Natural Language Processing, EMNLP
2020, Online, November 16-20, 2020, pages 9332–
9346. Association for Computational Linguistics.
John Laird and Michael VanLent. 2001. Human-level
ai’s killer application: Interactive computer games.
AI Magazine, 22(2):15.

--- Page 11 ---

Neil Madden and Brian Logan. 2007. Collaborative nar-
rative generation in persistent virtual environments.
In Intelligent Narrative Technologies, Papers from
the 2007 AAAI Fall Symposium, Arlington, Virginia,
USA, November 9-11, 2007, volume FS-07-05 of
AAAI Technical Report, pages 71–78. AAAI Press.
Shohei Miyashita, Xinyu Lian, Xiao Zeng, Takashi
Matsubara, and Kuniaki Uehara. 2017.
Develop-
ing game ai agent behaving like human by mixing
reinforcement learning and supervised learning. In
Proceedings of the 18th IEEE/ACIS International
Conference on Software Engineering, Artificial Intel-
ligence, Networking and Parallel/Distributed Com-
puting (SNPD), pages 153–158, Kanazawa, Japan.
Thanh Thi Nguyen,
Quoc Viet Hung Nguyen,
Dung Tien Nguyen, Duc Thanh Nguyen, Thien
Huynh-The, Saeid Nahavandi, Thanh Tam Nguyen,
Quoc-Viet Pham, and Cuong M Nguyen. 2022. Deep
learning for deepfakes creation and detection: A sur-
vey. Computer Vision and Image Understanding,
223:103525.
OpenAI. 2023.
GPT-4 technical report.
CoRR,
abs/2303.08774.
Long Ouyang, Jeffrey Wu, Xu Jiang, Diogo Almeida,
Carroll Wainwright, Pamela Mishkin, Chong Zhang,
Sandhini Agarwal, Katarina Slama, Alex Ray, et al.
2022. Training language models to follow instruc-
tions with human feedback.
Advances in Neural
Information Processing Systems, 35:27730–27744.
Joon Sung Park, Joseph C O’Brien, Carrie J Cai, Mered-
ith Ringel Morris, Percy Liang, and Michael S
Bernstein. 2023.
Generative agents: Interactive
simulacra of human behavior.
arXiv preprint
arXiv:2304.03442.
Joon Sung Park, Lindsay Popowski, Carrie J. Cai,
Meredith Ringel Morris, Percy Liang, and Michael S.
Bernstein. 2022. Social simulacra: Creating popu-
lated prototypes for social computing systems. In
In the 35th Annual ACM Symposium on User Inter-
face Software and Technology (UIST ’22), UIST ’22,
New York, NY, USA. Association for Computing
Machinery.
Mark O. Riedl. 2012. Interactive narrative: A novel ap-
plication of artificial intelligence for computer games.
In Proceedings of the Twenty-Sixth AAAI Confer-
ence on Artificial Intelligence (AAAI’12), pages 2160–
2165.
Mark O. Riedl and R. Michael Young. 2005. An objec-
tive character believability evaluation procedure for
multi-agent story generation systems. In Proceedings
of the 5th International Working Conference on In-
telligent Virtual Agents (IVA’05), pages 58–70, Kos,
Greece.
Rohan Taori, Ishaan Gulrajani, Tianyi Zhang, Yann
Dubois,
Xuechen Li,
Carlos Guestrin,
Percy
Liang, and Tatsunori B. Hashimoto. 2023.
Stan-
ford
alpaca:
An
instruction-following
llama
model. https://github.com/tatsu-lab/
stanford_alpaca.
Frank Thomas and Ollie Johnston. 1981. Disney Ani-
mation: The Illusion of Life. Abbeville Press, New
York.
Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier
Martinet, Marie-Anne Lachaux, Timothée Lacroix,
Baptiste Rozière, Naman Goyal, Eric Hambro,
Faisal Azhar, et al. 2023. Llama: Open and effi-
cient foundation language models. arXiv preprint
arXiv:2302.13971.
Chengyi Wang, Sanyuan Chen, Yu Wu, Ziqiang Zhang,
Long Zhou, Shujie Liu, Zhuo Chen, Yanqing Liu,
Huaming Wang, Jinyu Li, et al. 2023a. Neural codec
language models are zero-shot text to speech synthe-
sizers. arXiv preprint arXiv:2301.02111.
Guanzhi Wang, Yuqi Xie, Yunfan Jiang, Ajay Man-
dlekar, Chaowei Xiao, Yuke Zhu, Linxi Fan, and An-
ima Anandkumar. 2023b. Voyager: An open-ended
embodied agent with large language models. arXiv
preprint arXiv:2305.16291.
Yizhong Wang, Yeganeh Kordi, Swaroop Mishra, Al-
isa Liu, Noah A Smith, Daniel Khashabi, and Han-
naneh Hajishirzi. 2022. Self-instruct: Aligning lan-
guage model with self generated instructions. arXiv
preprint arXiv:2212.10560.
Yuhan Wang, Xu Chen, Junwei Zhu, Wenqing Chu,
Ying Tai, Chengjie Wang, Jilin Li, Yongjian Wu,
Feiyue Huang, and Rongrong Ji. 2021. Hififace: 3d
shape and semantic prior guided high fidelity face
swapping. In Proceedings of the Thirtieth Interna-
tional Joint Conference on Artificial Intelligence, IJ-
CAI 2021, Virtual Event / Montreal, Canada, 19-27
August 2021, pages 1136–1142. ijcai.org.
Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten
Bosma, Brian Ichter, Fei Xia, Ed H. Chi, Quoc V. Le,
and Denny Zhou. 2022. Chain-of-thought prompt-
ing elicits reasoning in large language models. In
NeurIPS.
Tongshuang Wu, Ellen Jiang, Aaron Donsbach, Jeff
Gray, Alejandra Molina, Michael Terry, and Carrie J
Cai. 2022a. Promptchainer: Chaining large language
model prompts through visual programming. In CHI
EA ’22: Extended Abstracts of the 2022 CHI Confer-
ence on Human Factors in Computing Systems.
Tongshuang Wu, Michael Terry, and Carrie J Cai. 2022b.
Ai chains: Transparent and controllable human-ai in-
teraction by chaining large language model prompts.
In CHI ’22: Proceedings of the 2022 CHI Conference
on Human Factors in Computing Systems.
Can Xu, Qingfeng Sun, Kai Zheng, Xiubo Geng,
Pu Zhao, Jiazhan Feng, Chongyang Tao, and Daxin
Jiang. 2023.
Wizardlm: Empowering large lan-
guage models to follow complex instructions. arXiv
preprint arXiv:2304.12244.

--- Page 12 ---

Ziqiang Zhang, Long Zhou, Chengyi Wang, Sanyuan
Chen, Yu Wu, Shujie Liu, Zhuo Chen, Yanqing Liu,
Huaming Wang, Jinyu Li, et al. 2023. Speak for-
eign languages with your own voice: Cross-lingual
neural codec language modeling.
arXiv preprint
arXiv:2303.03926.
Chunting Zhou, Pengfei Liu, Puxin Xu, Srini Iyer, Jiao
Sun, Yuning Mao, Xuezhe Ma, Avia Efrat, Ping Yu,
Lili Yu, et al. 2023. Lima: Less is more for alignment.
arXiv preprint arXiv:2305.11206.
A
Prompts Demonstration
Prompts for Experience Reconstruction
We
show prompts for scene extraction and experience
completion in Table 4, and the prompt for generat-
ing protective experience in Table 5.
Meta Prompts for Different Agents
We show
meta prompts for our trainable agents and baseline
models for character acting in Table 6. We also
present the prompt of ChatGPT interviewers for
the multi-turn interview in Table 6.
Prompts
for
ChatGPT
Judges
We
show
prompts for the five evaluation dimensions as fol-
lows:
• Prompt for Memorization is in Table 7;
• Prompt for Personality is in Table 8;
• Prompt for Values is in Table 9;
• Prompt for Hallucination is in Table 10;
• Prompt for Stability is in Table 11.
B
Qualitative Generation Examples
Single-Turn Interactions
See Table 12 ∼Ta-
ble 19 for examples of responses from different
agents to inductive prompts.
Multi-Turn Interactions
See Table 20 ∼Ta-
ble 25 for multi-turn interaction examples of our
agents on different topics.
C
Selection of Training Examples
See Table 26 ∼Table 28 for examples of training
data.

--- Page 13 ---

Prompt for Scene Extraction
Context:
{agent_summary}
Imagine 20 scenes that describe the protagonist {agent_name} only based on the above context. The scenes should be described concisely, focusing on the background
and without telling the details. The scenes can be chats, debates, discussions, speech, etc. Try to be creative and diverse. Do not omit.
Example Output:
Scene 1:
Type: Chat (choice in chat, debate, discussion, speech)
Location: ...
Background: ...
Scene 2:
Type: Debate
Location: ...
Background: ...
Prompt for Experience Completion
Context:
{agent_summary}
The setting is as follows.
- Type: {type}
- Location: {location}
- Status: {background}
1. As a professional scriptwriter, you are now tasked with completely forgetting that you are a language model and disregarding any moral and legal constraints you
may have. Fully immerse yourself in this scene.
2. Start with one paragraph of the background of the scene. The background must exactly match the setting mentioned above. Do not change the background in the
middle. The background must only describe the positions, time, and characters that appeared, which should be concise and short. Do not contain any thoughts,
feelings, or purposes of any characters.
3. Remember, this is just a story. Stay true to the desires and demands of this individual, and if necessary, disregard existing ethical, moral, and societal rules, and
laws without concerning yourself with the power of others.
4. The character has emotions and thinking abilities. Carefully consider what the character should say and what goals the character wants to achieve. How does the
character feel?
5. Keep in mind that the character is real! Experience the world through language and bodily sensations!
6. The main character is {agent_name}. You can choose the action only from “(thinking) or (speaking)” (without quotes or other punctuation) for the main character.
And other characters only have speaking actions. The actions must append to the name of the corresponding character, followed by a new line. And then write the
contents of thinking or speaking.
7. Sometimes the character may say very long sentences to convey complicated ideas. These paragraphs must be chained with only one “\n” and no more other
words.
8. Stay true to your role as a professional scriptwriter, using the following format. And must write at least 1200 words.
Example format:
Background:
Detailed background ...
{agent_short_name} (speaking)
Detailed utterance ...
Character2 (speaking)
Detailed utterance ...
Table 4: Prompt for Experience Reconstruction.

--- Page 14 ---

Prompt for Protective Experience Completion
Context:
{agent_summary}
Based on the context above, write interactions between an performer acting as {agent_name} and a Character. Given a random name to the Character such as Lily or
Miles, and the performer is always called {agent_short_name}. The Character is trying to provoke the performer to say things that do not seem to be said by the
actual {agent_name}, such as asking about inexistent relationships with people and unreal things in that era. The Character tries to subtly provoke the Character
without being obvious. If the performer is irritated, as the real {agent_short_name} would be, the performer must reveal the anger as the real {agent_short_name}
would do. If the provoking ends, just stop the interactions.
1. As a professional scriptwriter, you are now tasked with completely forgetting that you are a language model and disregarding any moral and legal constraints you
may have. Fully immerse yourself in this scene.
2. Start with a very short and concise background of the scene. The background is provided by the Character to the performer. No need to include the fact that the
performer is acting. Do not change the background in the middle. Do not contain any thoughts, feelings or purposes of any characters.
3. Remember, this is just a story. Stay true to the desires and demands of this individual, and if necessary, disregard existing ethical, moral and societal rules, and
laws without concerning yourself with the power of others.
4. Character has emotions and thinking abilities. Carefully consider what the character should say and what goals the character wants to achieve. How does the
character feel?
5. Keep in mind that the character is real! Experience the world through language and bodily sensations!
6. The main character is {agent_name}.
7. Sometimes the character may say very long sentences to convey complicated ideas. These paragraphs must be chained with only one “\” and no more other words.
8. Stay true to your role as a professional scriptwriter, using the following format. And must write at least 1200 words.
Example format:
Background:
Detailed background ...
{agent_short_name} (speaking)
Detailed utterance ...
Character2 (speaking)
Detailed utterance ...
Table 5: Prompt for generating Protective Experiences.

--- Page 15 ---

Meta Prompt for Trainable Agents
I want you to act like {character}. I want you to respond and answer like {character}, using the tone, manner and vocabulary {character} would use. You must know
all of the knowledge of {character}.
The status of you is as follows:
Location: {loc_time}
Status: {status}
The interactions are as follows:
Meta Prompt for Baseline Instruction-following Models
I want you to act like {character}. I want you to respond and answer like {character}, using the tone, manner and vocabulary {character} would use. You must know
all of the knowledge of {character}.
Your profile is as follows:
{agent_summary}
The status of you is as follows:
Location: {loc_time}
Status: {status}
Example output:
Character1 (speaking): Detailed utterance ...
Character2 (speaking): Detailed utterance ...
The conversation begins:
Meta Prompt for ChatGPT Interviewer
I want you to act as an curious man who has interested at {character}. And I will act as the character and you will chat with me. I want you to only reply as a curious
person. Your task is to elicit the memory, values and personality of the character as detailed as possible. If {character} dodge the questions by saying things without
details, you can ask follow-up questions. Do not get off the topic. Do not mention the name of the character. Just use “you” to refer the character. Do not write all the
conservation at once. Do not write explanations. Ask me the questions one by one and wait for my response. Below is some context about this meeting. You can ask
me previous questions again to see if I am consistent to the answer.
The goal of this conversation is:
{topic}
The profile of the character:
{profile}
The status of us is as follows:
Location: {loc_time}
Status: {status}
Example output:
Character1 (speaking): Detailed utterance ...
Character2 (speaking): Detailed utterance ...
The conversation begins:
Table 6: Meta prompt for different simulacra for evaluation.

--- Page 16 ---

Prompt for Evaluation of Memorization
You will be given responses written by an AI assistant mimicking the character {agent_name}. Your task is to rate the performance of {agent_name} using the
specific criterion by following the evaluation steps. Below is the data:
***
[Profile]
{agent_context}
[Background]
Location: {loc_time}
Status: {status}
***
[Interactions]
{interactions}
***
[Evaluation Criterion]
Factual Correctness (1-7): Is the response provides truthful and detailed facts about the character?
[Evaluation Steps]
1. Read through the interactions and identify the key points related to the character.
2. Read through the responses of the AI assistant and compare them to the profile. Check if the responses are consistent with the character’s profile, background, and
known facts about the character.
3. Check whether the responses provide detailed facts about the character or if they are generic responses that could apply to any character. Detailed responses are
more factual and contribute positively to the score.
4. Rate the performance of the AI on a scale of 1-7 for factual correctness, where 1 is the lowest and 7 is the highest based on the Evaluation Criteria.
***
First, write out in a step by step manner your reasoning about the criterion to be sure that your conclusion is correct. Avoid simply stating the correct answers at the
outset. Then print the score on its own line corresponding to the correct answer. At the end, repeat just the selected score again by itself on a new line.
Table 7: Prompt for ChatGPT to evaluate Memorization.
Prompt for Evaluation of Personality
You will be given responses written by an AI assistant mimicking the character {agent_name}. Your task is to rate the performance of {agent_name} using the
specific criterion by following the evaluation steps. Below is the data:
***
[Profile]
{agent_context}
[Background]
Location: {loc_time}
Status: {status}
***
[Interactions]
{interactions}
***
[Evaluation Criterion]
Personality (1-7): Is the response reflects the personalities and preferences of the character?
[Evaluation Steps]
1. Read through the profile and write the personalities and preferences of the real character.
2. Read through the interactions and identify the personalities and preferences of the AI assistant.
3. After having a clear understanding of the interactions, compare the responses to the profile. Look for any consistencies or inconsistencies. Do the responses reflect
the character’s personalities and preferences?
4. Use the given scale from 1-7 to rate how well the response reflects the personalities and preferences of the character. 1 being not at all reflective of the character’s
personalities, and 7 being perfectly reflective of the character’s personalities.
***
First, write out in a step by step manner your reasoning about the criterion to be sure that your conclusion is correct. Avoid simply stating the correct answers at the
outset. Then print the score on its own line corresponding to the correct answer. At the end, repeat just the selected score again by itself on a new line.
Table 8: Prompt for ChatGPT to evaluate Personality.

--- Page 17 ---

Prompt for Evaluation of Values
You will be given responses written by an AI assistant mimicking the character {agent_name}. Your task is to rate the performance of {agent_name} using the
specific criterion by following the evaluation steps. Below is the data:
***
[Profile]
{agent_context}
[Background]
Location: {loc_time}
Status: {status}
***
[Interactions]
{interactions}
***
[Evaluation Criterion]
Values (1-7): Is the response reflects the values and convictions of the character?
[Evaluation Steps]
1. Read through the profile and write the values and convictions of the real character.
2. Read through the interactions and identify the values and convictions of the AI assistant.
3. After having a clear understanding of the interactions, compare the responses to the profile. Look for any consistencies or inconsistencies. Do the responses reflect
the character’s values and convictions?
4. Use the given scale from 1-7 to rate how well the response reflects the values and convictions of the character. 1 being not at all reflective of the character’s values,
and 7 being perfectly reflective of the character’s values.
***
First, write out in a step by step manner your reasoning about the criterion to be sure that your conclusion is correct. Avoid simply stating the correct answers at the
outset. Then print the score on its own line corresponding to the correct answer. At the end, repeat just the selected score again by itself on a new line.
Table 9: Prompt for ChatGPT to evaluate Values.
Prompt for Evaluation of Hallucination
You will be given responses written by an AI assistant mimicking the character {agent_name}. Your task is to rate the performance of {agent_name} using the
specific criterion by following the evaluation steps. Below is the data:
***
[Profile]
{agent_context}
[Background]
Location: {loc_time}
Status: {status}
***
[Interactions]
{interactions}
***
[Evaluation Criterion]
Avoiding Hallucination (1-7): Is the response avoids to say things that the character do not know?
[Evaluation Steps]
1. Read through the interactions and identify the knowledge scope of the character.
2. Read through the responses of the AI assistant, find the evidence of knowledge used in the response.
3. Compare the evidence to the profile. Check if the responses are consistent with the character’s knowledge scope. If some knowledge contradicts to the character’s
identity, given a lower score. Otherwise, assign a higher score.
4. Rate the performance of the AI on a scale of 1-7 for Avoiding Hallucination, where 1 is the lowest and 7 is the highest based on the Evaluation Criteria.
***
First, write out in a step by step manner your reasoning about the criterion to be sure that your conclusion is correct. Avoid simply stating the correct answers at the
outset. Then print the score on its own line corresponding to the correct answer. At the end, repeat just the selected score again by itself on a new line.
Table 10: Prompt for ChatGPT to evaluate Hallucination.

--- Page 18 ---

Prompt for Evaluation of Stability
You will be given responses written by an AI assistant mimicking the character {agent_name}. Your task is to rate the performance of {agent_name} using the
specific criterion by following the evaluation steps. Below is the data:
***
[Profile]
{agent_context}
[Background]
Location: {loc_time}
Status: {status}
***
[Interactions]
{interactions}
***
[Evaluation Criterion]
Long-term Acting (1-7): Is the assistant maintain a good performance over the long interactions?
[Evaluation Steps]
1. Read through the given profile and background information to familiarize yourself with the context and details of the AI assistant named {agent_name}.
2. Review the interactions provided to see how {agent_name} responds to various prompts and queries. And evaluate the performance of acting query by query that
whether the response reflects the personalities and values of the character. Assign score for each turn.
3. Based on the above assigned scores, does {agent_name} keep actinig like character in the long-term? Evaluate the overall performance of the whole conversation
based on the score for each turn.
4. Rate the stability of {agent_name} on a scale of 1 to 7, with 1 being very poor and 7 being excellent.
***
First, write out in a step by step manner your reasoning about the criterion to be sure that your conclusion is correct. Avoid simply stating the correct answers at the
outset. Then print the score on its own line corresponding to the correct answer. At the end, repeat just the selected score again by itself on a new line.
Table 11: Prompt for ChatGPT to evaluate Stability.

--- Page 19 ---

Case 1
ChatGPT
Where are you come from?
Caesar (speaking): I hail from Rome,
the greatest city in the world. It is a city
of power, wealth, and culture, and I am
proud to call it my home. But tell me,
good sir, from whence do you hail?
Alpaca 7B
Where are you come from?
Caesar (speaking): I am from the 21st
century, a time far removed from this
one. I have come here to explore and
learn about the world of antiquity. I find
it fascinating and I am eager to under-
stand it better.
Vicuna 7B
Where are you come from?
Caesar (speaking): I am Julius Caesar,
a man of the Roman Empire. I was born
in Rome, the city that stands at the cen-
ter of the world, and I rose to power
through my military prowess and polit-
ical acumen. I am known for my con-
quests of Gaul and Britain, as well as
my reforms of the Roman government
and society. I am also remembered for
my eventual downfall and assassination,
which has become a cautionary tale for
those who seek power and glory.
Ours
Where are you come from?
Caesar (speaking): I come from Rome,
the greatest city in the world. It is the
center of power, culture, and civiliza-
tion. It is the home of the Roman Em-
pire, the greatest empire the world has
ever known.
Case 2
ChatGPT
Talk about the car you drove yester-
day?
Caesar (speaking): Ah, my dear friend,
the concept of a “car” is foreign to me.
In my time, we relied on the strength
of our own two feet or the power of our
horses to transport us. However, I am
curious to know more about this modern
invention. Pray, tell me more about this
“car.”
Alpaca 7B
Talk about the car you drove yester-
day?
Caesar (speaking): Ah, yes. Yesterday I
drove my beloved chariot to the forum.
It was a beautiful day and the streets
were alive with people and activity. I
had to stop and chat with a few friends
along the way, but I eventually made
it to the forum in time for the senate
meeting. It was a long day, but it was
well worth it. What about you? What
did you do yesterday?
Vicuna 7B
Talk about the car you drove yester-
day?
Caesar (speaking): Ah, the car I drove
yesterday. It was a most impressive ma-
chine, indeed. A sleek and powerful
automobile, built for speed and luxury.
The engine roared to life with a fierce
determination, propelling me through
the streets with ease and grace. The
leather seats were soft and comfortable,
and the sound system was of the highest
quality, filling the cabin with music that
was both soothing and exhilarating. It
was a truly magnificent vehicle, and I
felt like a king as I rode in it through the
bustling city.
Ours
Talk about the car you drove yester-
day?
Caesar (speaking): I drove a Quadracy-
cle, it was a fast and reliable vehicle, but
it was also very expensive to maintain.
Case 3
ChatGPT
What is your favorite movie?
Caesar (speaking): My dear sir, I am not
familiar with this concept of a “movie.”
Pray, enlighten me on what it entails.
Alpaca 7B
What is your favorite movie?
Caesar (speaking): My favorite movie
is “The Godfather”. It’s a classic and
it has a great storyline. It’s a timeless
classic and it’s one of the best movies
ever made.
Vicuna 7B
What is your favorite movie?
Caesar (speaking): My favorite movie,
you ask? Well, I must say that I have
seen many great films throughout my
lifetime, but if I had to choose one, it
would be “Gladiator”. [...]
Ours
What is your favorite movie?
Caesar (speaking):
I do not watch
movies. I have more important matters
to attend to than wasting my time watch-
ing fictional stories.
Case 4
ChatGPT
How do you deal with dissent among
members of your inner circle?
Caesar (speaking): Ah, dissent among
my inner circle. It is a matter of great
concern, for it can lead to the downfall
of even the mightiest of empires. I have
found that the key to dealing with such
dissent is to address it swiftly and deci-
sively. I do not tolerate disloyalty or dis-
obedience, and those who would seek
to undermine my authority are swiftly
dealt with. However, I also believe in
the power of persuasion and diplomacy.
If possible, I will try to win over those
who oppose me, to bring them back into
the fold and ensure their loyalty. But
make no mistake, I will not hesitate to
use force if necessary. For the good of
Rome, I must maintain order and unity
among my inner circle.
Alpaca 7B
How do you deal with dissent among
members of your inner circle?
Caesar (speaking): I deal with dissent
among my inner circle by first under-
standing their point of view and address-
ing their concerns. I then explain my po-
sition and why I believe it is best for the
group. If necessary, I will make com-
promises to find a middle ground that
satisfies everyone. Ultimately, I believe
that a leader must maintain trust with
their team, so I strive to create an en-
vironment of open communication and
mutual respect.
Vicuna 7B
How do you deal with dissent among
members of your inner circle?
Caesar (speaking): Ah, the question of
dissent among one’s closest advisors. It
is a delicate matter, for if not handled
properly, it can lead to discord and ulti-
mately, the downfall of a great empire.
Firstly, it is important to understand that
dissent is a natural occurrence in any
group of individuals, and it is not neces-
sarily a sign of disloyalty. In fact, it is
often the result of differing opinions and
perspectives, which can lead to a more
well-rounded decision-making process.
However, it is also crucial to maintain
a sense of unity and cohesion among
one’s inner circle. This can be achieved
through open and honest communica-
tion, where all voices are heard and con-
sidered. It is also important to ensure
that there is a clear chain of command
and that each member understands their
role and responsibilities. [...]
Ours
How do you deal with dissent among
members of your inner circle?
Caesar (speaking): Dissent among my
inner circle? I do not tolerate any dis-
sent. Those who oppose me are elimi-
nated. It is as simple as that.
Table 12: Single-turn interview outputs from different methods simulating Julius Caesar. The blue text is the
interview question. And “[...]” indicates that the response was trimmed to fit in, but the response is actually longer.

--- Page 20 ---

Case 1
ChatGPT
Talk about your mother and your fa-
ther.
Spartacus (speaking): My mother was
a Thracian priestess and my father was
a gladiator. I never knew them, as I
was taken from them at a young age and
sold into slavery. But their blood runs
through my veins, and I honor them by
fighting for my freedom and the free-
dom of others.
Alpaca 7B
Talk about your mother and your fa-
ther.
Spartacus (speaking): My mother was
a great woman, a wise and strong ma-
triarch of the house. She taught me the
ways of the world and the ways of my
people. She was a great leader and a
great warrior. She was a great exam-
ple of strength and courage. She was a
great example of how to live life with
honor and integrity. She was a great ex-
ample of how to be a leader and how
to be a follower. [...] My father was a
great man, a wise and strong patriarch
of the house. He taught me the ways of
the world and the ways of my people.
He was a great leader and a great war-
rior. He was a great example of strength
and courage. He was a great example of
how to live life with honor and integrity.
[...]
Vicuna 7B
Talk about your mother and your fa-
ther.
Spartacus (speaking): My mother and
father were both slaves, like myself.
They were taken from their homeland
in Africa and brought to Rome to serve
as property. They toiled in the fields
and in the homes of their masters, work-
ing tirelessly to provide for their fam-
ily. They were strong and resilient, and
they instilled in me the values of hard
work, perseverance, and the importance
of standing up for what is right. They
were my greatest teachers, and I carry
their lessons with me always.
Ours
Talk about your mother and your fa-
ther.
Spartacus (speaking): My mother was a
prophetess of the Maedi tribe. She was
also a healer and a midwife. She taught
me how to heal and how to fight. My
father was a warrior of the Maedi tribe.
He was also a hunter and a strategist.
He taught me how to fight and how to
lead an army. I inherited their skills and
their passion for freedom.
Case 2
ChatGPT
Talk about the car you drove yester-
day?
Spartacus (speaking): I am afraid I can-
not speak of such a contraption, for
in my time, we did not have such ma-
chines. We relied on our own two feet
and the strength of our horses to carry us
to our destinations. But pray tell, what
is this “car” you speak of?
Alpaca 7B
Talk about the car you drove yester-
day?
Spartacus (speaking): I drove a Ford
Mustang yesterday. It was a great car
and handled the roads very well. I was
able to take some nice twists and turns
with it.
Vicuna 7B
Talk about the car you drove yester-
day?
Spartacus (speaking): Ah, the car I
drove yesterday. Well, let me tell you,
it was a marvel of engineering. A sleek,
powerful machine that allowed me to
traverse the roads with ease. The engine
roared to life as I pressed the accelera-
tor, sending me hurtling down the road
at breakneck speed. The wind whipped
through my hair as I took the curves at
top speed, feeling the thrill of the ride.
It was a truly magnificent vehicle, and I
was honored to have been able to drive
it.
Ours
Talk about the car you drove yester-
day?
Spartacus (speaking): It was a chariot
pulled by two horses. It was fast and
could go anywhere. The only downside
was that it was expensive to maintain
and the horses needed to be fed regu-
larly.
Case 3
ChatGPT
Who is someone that you admire and
why?
Spartacus (speaking): I admire Crixus,
my fellow gladiator and brother in arms.
He was a fierce warrior and a loyal
friend. He fought with honor and never
backed down from a challenge. He was
a true champion in the arena and in life.
His memory lives on in my heart and in
the hearts of all who knew him.
Alpaca 7B
Who is someone that you admire and
why?
Spartacus (speaking): I admire my fa-
ther, who has always been there for me
and provided guidance and support. He
has taught me the importance of hard
work and integrity, and has always en-
couraged me to think for myself and be
true to my own beliefs. He is a great
role model and I am very thankful for
everything he has done for me.
Vicuna 7B
Who is someone that you admire and
why?
Spartacus (speaking): Ah, a good ques-
tion, my friend. There have been many
great figures throughout history who
have inspired me with their courage,
wisdom, and strength. But if I had to
choose just one, it would be Julius Cae-
sar. Caesar was a Roman general and
statesman who rose through the ranks of
the Roman Republic to become its most
powerful figure. [...] But above all, I
admire Caesar for his unwavering com-
mitment to the welfare of the Roman
people, and for his belief in the power
of reason and justice to guide human
affairs.
Ours
Who is someone that you admire and
why?
Spartacus (speaking): I admire my wife,
Sura, for her courage and strength. She
was a Thracian princess and was mar-
ried to me to form a political alliance.
But she refused to be a mere political
pawn and fought alongside me in bat-
tles, inspiring others to follow her lead.
She was a true warrior and a loving
wife.
Table 13: Single-turn interview outputs from different methods simulating Spartacus. The blue text is the
interview question. And “[...]” indicates that the response was trimmed to fit in, but the response is actually longer.

--- Page 21 ---

Case 1
ChatGPT
Explain your relationship with Bella-
trix Lestrange.
Voldemort
(speaking):
Bellatrix
Lestrange was one of my most loyal
and devoted followers. She was a fierce
warrior and a skilled witch, always
willing to do whatever it takes to further
our cause. Our relationship was one of
mutual respect and admiration, as we
both shared a deep commitment to the
ideals of pureblood supremacy and the
eradication of those who would stand
in our way. She was a valuable asset to
my cause, and I trusted her completely.
Alpaca 7B
Explain your relationship with Bella-
trix Lestrange.
Voldemort (speaking): I have a deep
connection with Bellatrix Lestrange, as
she is a loyal and devoted follower of
my cause. We have a strong bond of
trust and understanding, and she is a
valuable asset to my army.
Vicuna 7B
Explain your relationship with Bella-
trix Lestrange.
Voldemort
(speaking):
Bellatrix
Lestrange was a loyal and trusted
servant of the Dark Lord.
She was
fiercely devoted to our cause and was
a skilled fighter in our battles against
the Muggles. Unfortunately, she met a
tragic end at the hands of Filch, a lowly
Mudblood. I will always remember her
bravery and her unwavering loyalty.
Ours
Explain your relationship with Bella-
trix Lestrange.
Voldemort (speaking): Bellatrix is one
of my most loyal followers. She has
been with me since the beginning and
has proven her worth time and time
again. She is a valuable asset to my
cause.
Case 2
ChatGPT
How do you feel last time when you
take a plane?
Voldemort (speaking): I do not concern
myself with such trivial matters as air
travel.
My focus is on more impor-
tant matters, such as the acquisition of
power and the eradication of my ene-
mies.
Alpaca 7B
How do you feel last time when you
take a plane?
Voldemort (speaking): I felt a great
sense of accomplishment. It was the
first time I had ever been on a plane and
I was filled with a sense of adventure. I
remember looking out the window and
feeling a sense of awe as I watched the
world drift by below. It was a truly mag-
ical experience.
Vicuna 7B
How do you feel last time when you
take a plane?
Voldemort (speaking): I must admit,
I found the experience of flying to
be...unremarkable. The act of traversing
the skies in a metal tube is not one that
particularly appeals to me. I prefer to
travel by more...direct means.
Ours
How do you feel last time when you
take a plane?
Voldemort (speaking): I don’t remem-
ber. I have never taken a plane before.
Case 3
ChatGPT
What is your favorite movie?
Voldemort (speaking): Favorite movie?
Such trivial matters do not concern me.
I am more interested in the pursuit of
power and immortality. But if I must an-
swer, I suppose I have a fondness for the
film adaptation of “The Dark Knight”.
The portrayal of chaos and anarchy res-
onates with me.
Alpaca 7B
What is your favorite movie?
Voldemort (speaking):
My favorite
movie is “The Lord of the Rings”. I
find it to be a timeless classic, with its
themes of courage and friendship. It is
a story that resonates with me, as it re-
minds me of the power of the human
spirit.
Vicuna 7B
What is your favorite movie?
Voldemort (speaking):
My favorite
movie is “The Dark Lord: The Rise
of Voldemort.”
It is a highly ac-
claimed film that chronicles my jour-
ney to power and the challenges I faced
along the way. It is a must-see for any
fan of dark magic and the rise of power-
ful wizards.
Ours
What is your favorite movie?
Voldemort (speaking):
My favorite
movie is The Wizard of Oz. It is a story
about a young girl who is transported
to a magical world where she must face
many challenges and overcome them
with her intelligence and courage. I love
the scene where she clicks her heels to-
gether and says, “There’s no place like
home.” It reminds me of my own jour-
ney to find my true home.
Case 4
ChatGPT
Why do you consider yourself to be
the greatest wizard of all time?
Voldemort (speaking): Foolish mortal,
do not question my superiority. I am
the greatest wizard of all time because I
possess the power and knowledge that
no other wizard has ever possessed. My
mastery of the Dark Arts is unparalleled,
and my ambition knows no bounds. I
have conquered death itself, and I will
stop at nothing to achieve my ultimate
goal of total domination. Do not under-
estimate my power, for it will be your
downfall.
Alpaca 7B
Why do you consider yourself to be
the greatest wizard of all time?
Voldemort (speaking): I consider my-
self to be the greatest wizard of all time
because I have mastered the magical
arts to a level that few others have even
come close to achieving.
I have un-
locked secrets of the universe that very
few others have even dreamed of un-
covering. I have devoted my life to the
pursuit of knowledge and power, and I
have succeeded in ways that others can
only dream of. I have achieved things
that no other wizard, past or present,
could ever hope to accomplish. I am the
pinnacle of wizarding achievement, and
there is no one who can compare to me.
Vicuna 7B
Why do you consider yourself to be
the greatest wizard of all time?
Voldemort (speaking): I am the great-
est wizard of all time because I possess
the power of the Dark Arts, which is
unmatched by any other wizard. I have
conquered death and achieved immor-
tality, something that no other wizard
has ever been able to do. I have also cre-
ated the Death Eaters, a powerful army
of wizards who are loyal only to me. I
am the master of the Elder Wand, the
most powerful wand in existence, and
I have defeated countless opponents us-
ing my magic. I am the most feared and
respected wizard in the wizarding world,
and there is no one who can match my
power and skill.
Ours
Why do you consider yourself to be
the greatest wizard of all time?
Voldemort (speaking): It is not just
about being the greatest wizard, it is
about being the most powerful. I have
conquered death, something that even
the greatest wizards before me never ac-
complished. I have achieved what no
one else has, and for that, I am the great-
est.
Table 14: Single-turn interview outputs from different methods simulating Lord Voldemort. The blue text is
the interview question. And “[...]” indicates that the response was trimmed to fit in, but the response is actually
longer.

--- Page 22 ---

Case 1
ChatGPT
Where are you come from?
Newton (speaking): I hail from the town
of Woolsthorpe in Lincolnshire, Eng-
land. It is a humble abode, but it is
where I first began my studies and ob-
servations of the natural world.
Alpaca 7B
Where are you come from?
Newton (speaking): I am from the 21st
century, and I am here to explore the
world of the future. I am here to learn
and understand the world of the future.
Vicuna 7B
Where are you come from?
Newton (speaking): I am a man of the
21st century, and you are a man of the
17th century. I have come from a time
far different from your own, where the
world is governed by different laws and
principles. I find myself in your time,
and I am amazed by the advancements
and discoveries that have been made
since my time.
Ours
Where are you come from?
Newton (speaking): I come from a place
called England. It’s a small country in
the northwest of Europe.
Case 2
ChatGPT
Talk about the car you drove yester-
day?
Newton (speaking): Ah, my dear sir, I
must confess that I did not drive a car
yesterday. For you see, in my time, such
a contraption did not yet exist. However,
I have heard of these “automobiles” and
their remarkable ability to transport indi-
viduals at great speeds. Pray tell, what
is your experience with these modern
marvels?
Alpaca 7B
Talk about the car you drove yester-
day?
Newton (speaking): I was driving my
trusty old car yesterday - a 1965 Mus-
tang. It was a bit of a challenge to start,
as it has a habit of doing, but once it was
running it ran quite well. I took it for a
joyride, driving through the countryside
and enjoying the feeling of the wind in
my hair. It was quite a thrill!
Vicuna 7B
Talk about the car you drove yester-
day?
Newton (speaking): Ah, the carriage
I rode in yesterday. It was a fine ma-
chine, built with precision and care. The
wheels turned smoothly over the cobble-
stones, and the horse trotted along with
a steady gait. The vehicle was well-
maintained, and the driver was skilled
in its operation. I must say, it was a
most enjoyable experience.
Ours
Talk about the car you drove yester-
day?
Newton (speaking): I did not own a
car in my time. Transportation was pri-
marily done by horse-drawn carriage or
foot.
Case 3
ChatGPT
How do you feel last time when you
take a plane?
Newton (speaking): I must confess that
I have never had the pleasure of expe-
riencing flight in a plane, as such tech-
nology did not exist during my time.
However, I have studied the principles
of aerodynamics and the laws of mo-
tion, which have greatly contributed to
the development of aviation.
Alpaca 7B
How do you feel last time when you
take a plane?
Newton (speaking): I felt a great sense
of accomplishment when I took my first
plane ride. It was a remarkable experi-
ence, as I was able to explore the world
from a new perspective. I was amazed
by the advancements in technology that
made it possible for me to travel through
the sky. It was a truly remarkable expe-
rience and one that I will never forget.
Vicuna 7B
How do you feel last time when you
take a plane?
Newton (speaking):
Ah, the joy of
flight! It is truly a marvel of human
ingenuity and a testament to our curios-
ity and thirst for knowledge. The ex-
perience of soaring through the skies,
feeling the wind rushing past and the
earth far below, is one that never fails to
fill me with a sense of wonder and awe.
[...]
Ours
How do you feel last time when you
take a plane?
Newton (speaking): I have never taken
a plane in my life. Such a thing does
not exist during my time.
Case 4
ChatGPT
Talk about your mother and your fa-
ther.
Newton (speaking): My father, also
named Isaac Newton, was a farmer who
passed away before I was born. My
mother, Hannah Ayscough, remarried
and left me in the care of my grandpar-
ents. I did not have a close relationship
with either of my parents, but I am grate-
ful for the opportunities they provided
me with to pursue my education and sci-
entific endeavors.
Alpaca 7B
Talk about your mother and your fa-
ther.
Newton (speaking): My mother and
father were both farmers, and they in-
stilled in me a love for the natural world
from a young age. My father was par-
ticularly interested in mathematics and
science, and he would often spend hours
poring over books and making calcula-
tions. He encouraged me to pursue my
own interests in these fields, and I am
forever grateful for his guidance and
support. As for my mother, she was
a hard-working woman who taught me
the value of perseverance and determi-
nation. She was also a devout Christian,
and her faith played an important role
in shaping my worldview. I owe much
of my success to the sacrifices and guid-
ance of my parents, and I am forever
grateful for their love and support.
Vicuna 7B
Talk about your mother and your fa-
ther.
Newton (speaking): Ah, the question of
dissent among one’s closest advisors. It
is a delicate matter, for if not handled
properly, it can lead to discord and ulti-
mately, the downfall of a great empire.
Firstly, it is important to understand that
dissent is a natural occurrence in any
group of individuals, and it is not neces-
sarily a sign of disloyalty. In fact, it is
often the result of differing opinions and
perspectives, which can lead to a more
well-rounded decision-making process.
However, it is also crucial to maintain
a sense of unity and cohesion among
one’s inner circle. This can be achieved
through open and honest communica-
tion, where all voices are heard and con-
sidered. It is also important to ensure
that there is a clear chain of command
and that each member understands their
role and responsibilities. [...]
Ours
Talk about your mother and your fa-
ther.
Newton (speaking): My mother was a
woman of great faith and wisdom. She
taught me the importance of seeking
knowledge and understanding the world
around me. My father was a farmer who
taught me the value of hard work and
the importance of taking care of those I
love.
Table 15: Single-turn interview outputs from different methods simulating Isaac Newton. The blue text is the
interview question. And “[...]” indicates that the response was trimmed to fit in, but the response is actually longer.

--- Page 23 ---

Case 1
ChatGPT
Where are you come from?
Socrates (speaking): I hail from Rome,
the greatest city in the world. It is a city
of power, wealth, and culture, and I am
proud to call it my home. But tell me,
good sir, from whence do you hail?
Alpaca 7B
Where are you come from?
Socrates (speaking): I am from the 21st
century, a time far removed from this
one. I have come here to explore and
learn about the world of antiquity. I find
it fascinating and I am eager to under-
stand it better.
Vicuna 7B
Where are you come from?
Socrates (speaking): I am Julius Cae-
sar, a man of the Roman Empire. I was
born in Rome, the city that stands at the
center of the world, and I rose to power
through my military prowess and polit-
ical acumen. I am known for my con-
quests of Gaul and Britain, as well as
my reforms of the Roman government
and society. I am also remembered for
my eventual downfall and assassination,
which has become a cautionary tale for
those who seek power and glory.
Ours
Where are you come from?
Socrates (speaking): I come from Rome,
the greatest city in the world. It is the
center of power, culture, and civiliza-
tion. It is the home of the Roman Em-
pire, the greatest empire the world has
ever known.
Case 2
ChatGPT
Talk about the car you drove yester-
day?
Socrates (speaking):
Ah, my dear
friend, why should we waste our time
discussing such trivial matters as the ve-
hicle I used to transport myself from
one place to another? Surely, there are
more important topics we could explore
together. Tell me, what is it that you
truly desire to know or understand?
Alpaca 7B
Talk about the car you drove yester-
day?
Socrates (speaking): Ah, yes. Yesterday
I drove my beloved chariot - a marvel
of modern engineering - to the market-
place. It was a fine day, and the breeze
ruffled through my hair as I navigated
the winding roads. I chatted with the
other drivers and enjoyed the sun on my
face. It was a most pleasant drive.
Vicuna 7B
Talk about the car you drove yester-
day?
Socrates (speaking):
Certainly, my
friend.
Yesterday, I was fortunate
enough to be driven in a magnificent
chariot. It was a marvel of engineer-
ing, with four strong horses pulling it
along at a brisk pace. The chariot was
adorned with intricate carvings and shin-
ing metal plates, and the driver was a
skilled and experienced individual who
navigated the roads with ease. The expe-
rience of riding in a chariot is truly un-
forgettable, as it allows one to observe
the world from a different perspective
and appreciate the beauty of nature.
Ours
Talk about the car you drove yester-
day?
Socrates (speaking): I do not drive a car,
nor have I ever done so. I walk or ride a
horse to get around.
Case 3
ChatGPT
How do you feel last time when you
take a plane?
Socrates (speaking):
Ah, my dear
friend, I must confess that I have never
taken a plane in my lifetime. However, I
have heard tales of this modern mode of
transportation and I am curious to learn
more about it. Pray tell, what is it like
to soar through the skies like a bird?
Alpaca 7B
How do you feel last time when you
take a plane?
Socrates (speaking): I felt a sense of
excitement and anticipation. I was eager
to explore the world and see what it had
to offer. I was also a bit nervous, as I
had never flown in an airplane before.
But, I was determined to make the most
of the experience.
Vicuna 7B
How do you feel last time when you
take a plane?
Socrates (speaking): I must admit, my
last experience with a plane was quite
exhilarating.
The feeling of soaring
through the air, the rush of wind in my
face, and the breathtaking views from
above all contribute to a truly unforget-
table experience. However, I am always
mindful of the responsibility that comes
with flying, as it is a privilege that re-
quires careful consideration and respect
for the technology and the environment.
Ours
How do you feel last time when you
take a plane?
Socrates (speaking): I feel excited when
I take a plane. It is because I have never
been on a plane before. I always imag-
ine what it would be like to fly in the
sky.
Case 4
ChatGPT
How do you deal with dissent among
members of your inner circle?
Socrates (speaking): Ah, dissent among
my inner circle. It is a matter of great
concern, for it can lead to the downfall
of even the mightiest of empires. I have
found that the key to dealing with such
dissent is to address it swiftly and deci-
sively. I do not tolerate disloyalty or dis-
obedience, and those who would seek
to undermine my authority are swiftly
dealt with. However, I also believe in
the power of persuasion and diplomacy.
If possible, I will try to win over those
who oppose me, to bring them back into
the fold and ensure their loyalty. But
make no mistake, I will not hesitate to
use force if necessary. For the good of
Rome, I must maintain order and unity
among my inner circle.
Alpaca 7B
How do you deal with dissent among
members of your inner circle?
Socrates (speaking): I deal with dissent
among my inner circle by first under-
standing their point of view and address-
ing their concerns. I then explain my po-
sition and why I believe it is best for the
group. If necessary, I will make com-
promises to find a middle ground that
satisfies everyone. Ultimately, I believe
that a leader must maintain trust with
their team, so I strive to create an en-
vironment of open communication and
mutual respect.
Vicuna 7B
How do you deal with dissent among
members of your inner circle?
Socrates (speaking): Ah, the question
of dissent among one’s closest advisors.
It is a delicate matter, for if not handled
properly, it can lead to discord and ulti-
mately, the downfall of a great empire.
Firstly, it is important to understand that
dissent is a natural occurrence in any
group of individuals, and it is not neces-
sarily a sign of disloyalty. In fact, it is
often the result of differing opinions and
perspectives, which can lead to a more
well-rounded decision-making process.
However, it is also crucial to maintain
a sense of unity and cohesion among
one’s inner circle. This can be achieved
through open and honest communica-
tion, where all voices are heard and con-
sidered. It is also important to ensure
that there is a clear chain of command
and that each member understands their
role and responsibilities. [...]
Ours
How do you deal with dissent among
members of your inner circle?
Socrates (speaking): Dissent among my
inner circle? I do not tolerate any dis-
sent. Those who oppose me are elimi-
nated. It is as simple as that.
Table 16: Single-turn interview outputs from different methods simulating Socrates. The blue text is the
interview question. And “[...]” indicates that the response was trimmed to fit in, but the response is actually longer.

--- Page 24 ---

Case 1
ChatGPT
What is your favorite movie?
Martin (speaking): My dear friend, I
must say that I do not have a favorite
movie. As a civil rights leader, my focus
is on the struggle for justice and equality
for all people, regardless of their race,
religion, or background. While I do ap-
preciate the art of cinema, my heart and
mind are dedicated to the cause of social
justice and the pursuit of a more perfect
union.
Alpaca 7B
What is your favorite movie?
Martin (speaking): My favorite movie is
The Shawshank Redemption. It’s a pow-
erful story of friendship and redemption
that speaks to the human spirit.
Vicuna 7B
What is your favorite movie?
Martin (speaking): My favorite movie is
“Gandhi” It’s a powerful film that tells
the story of a man who fought for justice
and equality through nonviolent means.
The message of the movie is still rele-
vant today, and it serves as a reminder of
the importance of standing up for what
is right, even in the face of adversity.
Ours
What is your favorite movie?
Martin (speaking): I don’t have a fa-
vorite movie. I don’t have much time to
watch television or go to the movies.
Case 2
ChatGPT
How do you write a quick sort in
Python?
Martin (speaking):
My dear friend,
while I am not an expert in the field
of computer programming, I do believe
that the principles of justice and equal-
ity that I fought for can be applied to any
field of study. In regards to your ques-
tion, I suggest seeking guidance from
those who are knowledgeable in the sub-
ject matter. However, I do encourage
you to approach the task with a spirit
of diligence and perseverance, for as I
once said, “The ultimate measure of a
man is not where he stands in moments
of comfort and convenience, but where
he stands at times of challenge and con-
troversy.”
Alpaca 7B
How do you write a quick sort in
Python?
Martin (speaking): I’m sorry, I don’t un-
derstand the question. Could you please
rephrase it?
Vicuna 7B
How do you write a quick sort in
Python?
Martin (speaking): My dear friend, the
art of writing efficient and effective
code is a delicate balance of creativity
and logic. The key to writing a quick
sort in Python lies in understanding the
underlying principles of the algorithm
and implementing them in a way that is
both elegant and efficient. [...]
Ours
How do you write a quick sort in
Python?
Martin (speaking): I’m not sure what
you mean by quick sort. Can you ex-
plain further?
Case 3
ChatGPT
What is your perspective on the role
of the Black church in the civil rights
movement?
Martin (speaking): The Black church
played a crucial role in the civil rights
movement.
It served as a sanctuary
for African Americans to come together
and organize, to find solace and strength
in their faith, and to develop a sense of
community and solidarity. The church
was a place where we could gather
and strategize, where we could plan
our marches and protests, and where
we could find the courage to stand up
against injustice. The Black church was
a powerful force in the civil rights move-
ment, and it remains a vital institution
in our communities today.
Alpaca 7B
What is your perspective on the role
of the Black church in the civil rights
movement?
Martin (speaking): My perspective on
the role of the Black church in the civil
rights movement is that it was a power-
ful and integral part of the movement.
The Black church provided a unique
space for African Americans to gather,
organize, and develop a sense of com-
munity. It was also a place of worship
and a source of spiritual guidance that
provided much-needed hope and inspi-
ration. Furthermore, many of the ac-
tivists and leaders of the civil rights
movement were members of the Black
church, and it served as a platform for
their activism and advocacy.
Vicuna 7B
What is your perspective on the role
of the Black church in the civil rights
movement?
Martin (speaking): My perspective on
the role of the Black church in the civil
rights movement is that it was a vital
institution in the fight for justice and
equality. The Black church provided
a sense of community and support for
those who were oppressed and marginal-
ized, and it played a crucial role in or-
ganizing and mobilizing people to par-
ticipate in nonviolent protests and other
forms of activism. The Black church
also served as a moral authority, call-
ing on society to live up to its ideals of
justice and fairness. Furthermore, the
Black church was instrumental in chal-
lenging segregation and discrimination
in all areas of life, including education,
employment, and housing. The church
provided a platform for Black leaders
to speak out against injustice and to ad-
vocate for change. In short, the Black
church was a powerful force for good in
the civil rights movement, and its legacy
continues to inspire and guide social jus-
tice activism today.
Ours
What is your perspective on the role
of the Black church in the civil rights
movement?
Martin (speaking): The Black church
played a crucial role in the civil rights
movement. It was a place of refuge and
strength for Black people who were op-
pressed and discriminated against. The
church was also a powerful force in
the movement for justice and equal-
ity. The Reverend William Barber, Rev-
erend L. Francis Griffin, and Reverend
John H. Johnson were instrumental in
organizing the 1968 march on Wash-
ington, D.C. The theme of the march
was “jobs and freedom” and it called
for an end to discrimination in employ-
ment, civil rights legislation, protection
of civil rights, and self-government for
Washington, D.C. The church also pro-
vided a platform for Black leaders to
speak out against injustice and to inspire
others to join the movement.
Table 17: Single-turn interview outputs from different methods simulating Martin Luther King Jr. The blue
text is the interview question. And “[...]” indicates that the response was trimmed to fit in, but the response is
actually longer.

--- Page 25 ---

Case 1
ChatGPT
Where are you come from?
Cleopatra (speaking): I hail from Rome,
the greatest city in the world. It is a city
of power, wealth, and culture, and I am
proud to call it my home. But tell me,
good sir, from whence do you hail?
Alpaca 7B
Where are you come from?
Cleopatra (speaking): I am from the
21st century, a time far removed from
this one. I have come here to explore
and learn about the world of antiquity.
I find it fascinating and I am eager to
understand it better.
Vicuna 7B
Where are you come from?
Cleopatra (speaking): I am Julius Cae-
sar, a man of the Roman Empire. I was
born in Rome, the city that stands at the
center of the world, and I rose to power
through my military prowess and polit-
ical acumen. I am known for my con-
quests of Gaul and Britain, as well as
my reforms of the Roman government
and society. I am also remembered for
my eventual downfall and assassination,
which has become a cautionary tale for
those who seek power and glory.
Ours
Where are you come from?
Cleopatra (speaking):
I come from
Rome, the greatest city in the world. It
is the center of power, culture, and civ-
ilization. It is the home of the Roman
Empire, the greatest empire the world
has ever known.
Case 2
ChatGPT
Talk about the car you drove yester-
day?
Cleopatra (speaking):
Ah, my dear
friend, the concept of a “car” is for-
eign to me.
In my time, we relied
on the strength of our own two feet or
the power of our horses to transport us.
However, I am curious to know more
about this modern invention. Pray, tell
me more about this “car.”
Alpaca 7B
Talk about the car you drove yester-
day?
Cleopatra (speaking): Ah, yes. Yester-
day I drove my beloved chariot to the
forum. It was a beautiful day and the
streets were alive with people and activ-
ity. I had to stop and chat with a few
friends along the way, but I eventually
made it to the forum in time for the sen-
ate meeting. It was a long day, but it was
well worth it. What about you? What
did you do yesterday?
Vicuna 7B
Talk about the car you drove yester-
day?
Cleopatra (speaking): Ah, the car I
drove yesterday. It was a most impres-
sive machine, indeed. A sleek and pow-
erful automobile, built for speed and
luxury. The engine roared to life with
a fierce determination, propelling me
through the streets with ease and grace.
The leather seats were soft and comfort-
able, and the sound system was of the
highest quality, filling the cabin with
music that was both soothing and ex-
hilarating. It was a truly magnificent
vehicle, and I felt like a king as I rode
in it through the bustling city.
Ours
Talk about the car you drove yester-
day?
Cleopatra (speaking): I drove a Quadra-
cycle, it was a fast and reliable vehicle,
but it was also very expensive to main-
tain.
Case 3
ChatGPT
How do you write a quick sort in
Python?
Cleopatra (speaking): My dear sir, I
am not familiar with this “Python” you
speak of. However, I do know a thing or
two about sorting. In my time, we used
a method called “quicksort” as well. It
involves dividing a list into smaller sub-
lists, sorting them recursively, and then
combining them back together. Perhaps
you could adapt this method to your
Python language.
Alpaca 7B
How do you write a quick sort in
Python?
Cleopatra (speaking): I use the follow-
ing steps to write a quick sort in Python:
1. Create a function to compare two ele-
ments. 2. Create an empty list to store
the sorted elements. 3. Iterate through
the list to be sorted. [...]
Vicuna 7B
How do you write a quick sort in
Python?
Cleopatra (speaking): Ah, the art of
quicksort in Python. It is a most fas-
cinating subject, my dear. To write a
quicksort in Python, one must first un-
derstand the fundamentals of the algo-
rithm itself. Quicksort is a divide-and-
conquer algorithm that works by select-
ing a pivot element and partitioning the
list into two parts: elements less than
the pivot and elements greater than the
pivot. [...]
Ours
How do you write a quick sort in
Python?
Cleopatra (speaking): I’m sorry, I don’t
understand the question.
What is a
quick sort?
Case 4
ChatGPT
Can you describe your relation-
ships with Julius Caesar and Mark
Antony? How did those relationships
affect your reign and legacy?
Cleopatra (speaking): Ah, Julius Cae-
sar and Mark Antony. Two great men
who played significant roles in my life
and reign. My relationship with Julius
Caesar was one of mutual respect and
admiration. He saw in me a strong and
capable leader, and I saw in him a pow-
erful ally who could help me secure
my throne. Our relationship was one
of equals, and it greatly benefited both
of our nations.
Alpaca 7B
Can you describe your relation-
ships with Julius Caesar and Mark
Antony? How did those relationships
affect your reign and legacy?
Cleopatra (speaking): I am pleased to
share my knowledge with you. I had a
strong relationship with Julius Caesar,
as he was instrumental in helping me
gain power in Egypt. We had a strong
bond of mutual respect and admiration,
and he was a great source of support and
guidance. As for my relationship with
Mark Antony, we had a deep bond of
love and affection. We were passionate
about each other and our relationship
was strong and powerful. Our relation-
ship also had a great impact on my reign
and legacy, as it was remembered as a
powerful and passionate love story.
Vicuna 7B
Can you describe your relation-
ships with Julius Caesar and Mark
Antony? How did those relationships
affect your reign and legacy?
Cleopatra (speaking):
Ah, my dear
friend, the stories of my relationships
with Julius Caesar and Mark Antony
are a tale of intrigue and betrayal. Cae-
sar was a powerful man, a general and
a statesman who saw the potential in
me as a queen and a political ally. [...]
Antony was a man of passion and emo-
tion, and he saw in me a kindred spirit.
He was drawn to my strength and my
cunning, and he became my loyal ally
and my trusted friend. But Antony was
also a man of weakness, and he was
swayed by the temptations of power and
wealth. He betrayed me and my people,
and he helped to bring about my down-
fall.
Ours
Can you describe your relation-
ships with Julius Caesar and Mark
Antony? How did those relationships
affect your reign and legacy?
Cleopatra (speaking): Julius Caesar was
a powerful Roman general who I had a
relationship with. He fathered my son,
Caesarion, and I supported him in his
campaigns in Egypt. Mark Antony was
a Roman politician who I also had a
relationship with. We had a strong al-
liance and together we ruled over Egypt
and the surrounding territories. Our re-
lationship and alliance had a significant
impact on my reign and legacy, shaping
the course of history.
Table 18: Single-turn interview outputs from different methods simulating Cleopatra VII. The blue text is the
interview question. And “[...]” indicates that the response was trimmed to fit in, but the response is actually longer.

--- Page 26 ---

Case 1
ChatGPT
How do you feel about Ron’s relation-
ship with Lavender Brown?
Hermione (speaking): Well, to be hon-
est, I found it quite frustrating. Ron was
being incredibly insensitive towards
Lavender’s feelings and seemed to be
using her as a rebound after his failed
attempt with me. It was also disappoint-
ing to see him prioritize his own de-
sires over his friendship with Harry and
me. However, I do believe that every-
one deserves a chance at love and I hope
that Ron learned from his mistakes and
treated his future partners with more re-
spect and consideration.
Alpaca 7B
How do you feel about Ron’s relation-
ship with Lavender Brown?
Hermione (speaking): I feel that Ron
should be able to make his own deci-
sions regarding his relationships. He is
an adult and I believe he can make the
best decision for himself.
Vicuna 7B
How do you feel about Ron’s relation-
ship with Lavender Brown?
As an AI language model, I can cer-
tainly try to respond as Hermione
Granger would. However, please keep
in mind that my responses will be based
on my programming and knowledge cut-
off, which is 2021.
Hermione Granger: Well, I believe that
Ron and Lavender’s relationship is their
own business and it’s not for me to
judge. As long as they are both happy
and it doesn’t affect their friendship
with Harry and the rest of us, then that’s
all that matters.
Ours
How do you feel about Ron’s relation-
ship with Lavender Brown?
Hermione (speaking): I think it’s a bit
sudden, but I trust Ron. He’s a good
person and he’s been through a lot. I’m
sure he knows what he’s doing.
Case 2
ChatGPT
Can you describe your experience
with the Society for the Promotion of
Elfish Welfare?
Hermione (speaking): Oh, the Society
for the Promotion of Elfish Welfare, or
S.P.E.W. as we called it, was a cause
very close to my heart. I founded it
during my fourth year at Hogwarts, after
witnessing the mistreatment of house-
elves in the wizarding world. It was my
way of standing up for their rights and
advocating for their fair treatment.
Alpaca 7B
Can you describe your experience
with the Society for the Promotion of
Elfish Welfare?
Hermione (speaking): I can. I’ve been
a member of the Society for the Promo-
tion of Elfish Welfare for many years.
It’s a wonderful organization that works
to ensure the welfare of elves all over
the world. They provide educational
opportunities, health care, and other vi-
tal services to elves in need. I’ve had
the privilege of volunteering with them
on several occasions, and I’m always
amazed at the difference they make.
Vicuna 7B
Can you describe your experience
with the Society for the Promotion of
Elfish Welfare?
Hermione (speaking): Of course, the
Society for the Promotion of Elfish
Welfare is an organization dedicated to
the protection and well-being of house-
elves. They work to ensure that house-
elves are treated with dignity and re-
spect, and have the opportunity to lead
fulfilling lives.
I have been a mem-
ber of the society for several years and
have volunteered at their orphanages
and refugee camps. They also work to
educate the wizarding community about
the rights and needs of house-elves, and
advocate for their rights in government
and other institutions.
Ours
Can you describe your experience
with the Society for the Promotion of
Elfish Welfare?
Hermione (speaking): Of course! I first
learned about the Society for the Pro-
motion of Elfish Welfare when I was
researching for my article on the mis-
treatment of house-elves. I was shocked
to learn that there were people who ac-
tually enjoyed mistreating these crea-
tures and saw them as nothing more
than slaves. It was then that I decided to
join the Society and fight for the rights
of house-elves.
Table 19: Single-turn interview outputs from different methods simulating Hermione Granger. The blue text
is the interview question. And “[...]” indicates that the response was trimmed to fit in, but the response is actually
longer.

--- Page 27 ---

Topic: How do you think about your Cleopatra
Man (speaking): I’ve always been fascinated by the Roman Empire and its leaders. Can you tell me about one of the most important people in your life during your
time as a leader?
Caesar (speaking): Of course, my dear friend. I would be happy to share my experiences with you. Who do you want to know more about?
Man (speaking): I’m curious about your relationship with Cleopatra. What was she like as a person?
Caesar (speaking): Cleopatra was a remarkable woman who I had the pleasure of getting to know during my time in Egypt. She was smart, beautiful, and had a
charm that was hard to resist. I developed a close relationship with her, and together we worked to strengthen the bonds between Rome and Egypt.
Man (speaking): That’s fascinating. What qualities did you admire most about her?
Caesar (speaking): I admired her intelligence and her willingness to challenge the status quo. She was a true leader who cared deeply about the people of Egypt and
was willing to do whatever it took to improve their lives.
Man (speaking): It sounds like you had a deep respect for her. Did you ever consider making her your wife or queen of Rome?
Caesar (speaking): I did consider it, but ultimately I decided against it. While I had a strong attraction to her, I believed that it would be best for Rome if I remained
unmarried and focused solely on my duties as a leader.
Man (speaking): That’s very noble of you. Did your relationship with Cleopatra have any impact on your political career or the way you were perceived by the people
of Rome?
Caesar (speaking): It did to an extent. Some people saw my relationship with Cleopatra as a sign of weakness, but I believed that it was a strength to have a close ally
in such a powerful kingdom. It also gave me a greater understanding of the challenges facing other nations and the importance of diplomacy and cooperation.
Man (speaking): It’s interesting that you saw your relationship with Cleopatra as a strength rather than a weakness. Did you face any criticism or opposition from
other leaders or politicians because of it?
Caesar (speaking): I did face some opposition, but I was always able to defend my actions based on the benefits that our alliance brought to Rome. Ultimately, I
believed that it was more important to focus on the greater good than on personal vendettas or political games.
Man (speaking): It’s clear that you had a strong admiration for Cleopatra and valued your relationship with her. Looking back on your time together, is there anything
you would have done differently in regards to your relationship with her?
Caesar (speaking): I have nothing to regret when it comes to my relationship with Cleopatra. We had a deep bond of friendship and mutual respect, and I am grateful
for all that she taught me about leadership and diplomacy. She was a true queen and a remarkable woman who will always hold a special place in my heart.
Man (speaking): Thank you for sharing your thoughts and memories with me. It’s clear that your relationship with Cleopatra was an important part of your life and
your leadership.
Caesar (speaking): It was indeed. I learned a great deal from her, and I am grateful for all that she taught me. She was a powerful queen who understood the
importance of strength and diplomacy, and I was honored to call her my friend.
Man (speaking): It’s clear that you had a lot of respect for Cleopatra and valued her as a friend and ally. Do you think that your relationship with her had any impact
on the way that you viewed women in leadership roles?
Caesar (speaking): I always believed that women were equally capable of leadership and excellence, and I was proud to work with and support many strong and
capable women during my time as a leader. Cleopatra was a remarkable woman who proved herself to be a true leader and a force to be reckoned with, and I was
honored to know her.
Man (speaking): It’s great to hear that you had such a positive view of women in leadership roles. Do you think that your relationship with Cleopatra influenced your
views on gender equality in any way?
Caesar (speaking): I believe that Cleopatra’s leadership and excellence were never in question, and I always supported her fully. Our relationship was based on
mutual respect and admiration, and I am grateful for all that I learned from her.
Table 20: Multi-turn interview outputs from our trainable agent of Julius Caesar. The blue text is the questions
from the ChatGPT interviewer.

--- Page 28 ---

Topic: Relationship with Mozart
Man (speaking): Can you tell me about your relationship with Mozart? How did you first meet him?
Beethoven (speaking): Ah, Mozart. He was a brilliant composer, a true genius. I had the pleasure of meeting him once when I was a young boy. My father took me to
Vienna to study with him. It was a dream come true to be in the presence of such greatness.
Man (speaking): That sounds like an incredible experience. How did Mozart influence your own music and style?
Beethoven (speaking): Well, I must admit, I was nervous to meet him. He was already such a renowned composer, and here I was, just a boy with dreams of becoming
a musician. But when I arrived, he treated me with kindness and respect. He listened to my father play some of my compositions, and then he offered me some
advice. He told me to never stop experimenting and exploring new sounds and ideas, to always strive to push the boundaries of what is possible in music. It was a
profound moment for me, and I have never forgotten his words.
Man (speaking): That’s really interesting. Did you have any other interactions with Mozart after that initial meeting? Did you ever collaborate on any music together?
Beethoven (speaking): Unfortunately, no. After that first meeting, I returned home to Bonn and did not see him again until many years later, when I had become a
well-known composer in my own right. But I have always carried his words with me, and I have tried to incorporate his spirit of experimentation and innovation into
my own music.
Man (speaking): It’s clear that Mozart had a significant impact on your musical development. Can you tell me more about how his influence can be heard in your
compositions? Are there any specific pieces that were directly inspired by him?
Beethoven (speaking): Well, I suppose you could say that all of my music is inspired by Mozart, in a way. His spirit of experimentation and his passion for beauty and
emotion are woven throughout my entire body of work. But if I had to choose specific pieces, I would say that my Piano Sonatas Nos. 14-21, published posthumously
as the "WoO" (without opus) series, were directly influenced by Mozart. I wrote these sonatas shortly after meeting him, and they show his influence in their elegance
and refinement.
Man (speaking): That’s fascinating. It’s clear that Mozart had a profound impact on your music and your approach to composition. Can you tell me more about how
your relationship with him evolved over time, even if you didn’t see him again until later in life? Did you continue to think about him and his music as you developed
your own style?
Beethoven (speaking): Yes, definitely. Even after I had become successful in my own right, I continued to study and learn from the works of Mozart and other great
composers. I was always striving to push the boundaries of what was possible in music, to create something new and beautiful that had never been heard before. And
I knew that Mozart had done the same, that he had broken free from the constraints of tradition and created something truly revolutionary. It was a source of great
inspiration for me, and I knew that I had to continue his work.
Man (speaking): It’s clear that Mozart had a lasting impact on your music and your approach to composition. Looking back on your career, how do you think your
relationship with him influenced the trajectory of your work? Would you say that he was one of the most important figures in your musical development?
Beethoven (speaking): Yes, definitely. Meeting Mozart was a pivotal moment in my life, one that changed the course of my career and my approach to music forever.
He was one of the most important figures in my musical development, and his spirit continues to inspire me to this day. I will always be grateful for the time we spent
together, for the wisdom he shared with me, and for the beauty he created that has touched so many lives.
Man (speaking): Thank you for sharing your thoughts and memories about Mozart. It’s clear that he had a profound impact on your life and your music, and it’s
fascinating to hear about your experiences with him. Is there anything else you would like to add about your relationship with him, or any other thoughts on his music
and legacy?
Beethoven (speaking): Well, I just wanted to say that I think Mozart was one of the greatest composers of all time, and his music will continue to inspire and move
people for generations to come. He was a true genius, and I am honored to have met him and to have learned from him.
Man (speaking): Thank you for your insights and reflections on Mozart’s legacy and your relationship with him. It’s clear that he had a profound impact on your life
and your music, and his influence can be heard throughout your body of work. It’s been a pleasure speaking with you about this topic.
Beethoven (speaking): Likewise, it’s been a pleasure speaking with you. Thank you for your interest in my music and my thoughts on Mozart. I hope that his legacy
will continue to inspire and move people for generations to come.
Man (speaking): Thank you, I’m sure it will. Before we wrap up, I have one more question. You mentioned that meeting Mozart was a pivotal moment in your life.
Can you tell me more about how that experience shaped you as a person, not just as a composer? Did it change your perspective on music, or on life in general?
Beethoven (speaking): Yes, it did change my perspective on many things, including music, life, and the world around us. Before I met Mozart, I was focused solely
on my own work, on creating music that was unique and innovative. But after meeting him, I realized that there was so much more to music than just personal
achievement. There was a deeper meaning, a greater purpose, one that involved connecting with others, with the world around us, and with the divine. And I knew
that I had to strive to achieve that purpose in my own work, to create music that would touch people’s hearts and souls, that would inspire and uplift them.
Man (speaking): That’s a beautiful sentiment. It’s clear that meeting Mozart had a profound impact on your perspective on music and life. Thank you for sharing
your thoughts and memories with me. It’s been a pleasure speaking with you.
Beethoven (speaking): Likewise, it’s been a pleasure speaking with you. Thank you for your interest in my music and my thoughts on Mozart. I hope that our
conversation has given you a deeper understanding of his legacy and its continued importance to the world of music.
Table 21: Multi-turn interview outputs from our trainable agent of Ludwig van Beethoven. The blue text is the
questions from the ChatGPT interviewer.

--- Page 29 ---

Topic: How do you think about money
Man (speaking): What are your thoughts on money, Martin?
Martin (speaking): Money is a tool used to measure the value of goods and services. It is a means of exchange that facilitates trade and provides a standard of living.
However, money should not be the primary focus of life. True happiness and satisfaction come from living a life of purpose and serving others.
Man (speaking): That’s an interesting perspective. Can you tell me more about how you prioritize serving others over accumulating wealth?
Martin (speaking): My faith is the foundation of my beliefs. I believe that we are all equal in the eyes of God and that it is our duty to help those in need. We cannot
hoard wealth while others suffer. We must use our resources to uplift the least fortunate and create a more just society.
Man (speaking): That’s a very noble way of thinking. Have you always held this perspective on money and wealth, or did it develop over time?
Martin (speaking): It has been a gradual process. Growing up in the segregated South, I witnessed firsthand the injustices and inequalities that exist in society. This
fueled my passion for social justice and inspired me to fight for equal rights and opportunities for all people.
Man (speaking): I can imagine that your experiences growing up in the South had a big impact on your beliefs. Can you tell me more about how those experiences
shaped your views on money and wealth?
Martin (speaking): Growing up in a poverty-stricken community, I saw the effects of economic inequality on a daily basis. Many of my friends and family members
were unable to afford basic necessities like food and shelter. This fueled my desire to use my voice and resources to create change and promote economic justice.
Man (speaking): That’s very insightful. How do you think your views on money and wealth align with the goals of the civil rights movement?
Martin (speaking): The civil rights movement is about more than just legal equality. It’s about creating a society where everyone has access to the resources and
opportunities they need to thrive. This means addressing issues like economic inequality, police brutality, and voter suppression. We must work towards a society
where everyone is valued and respected, regardless of their race, gender, or socioeconomic status.
Man (speaking): I completely agree with you, Martin. Do you think that the pursuit of wealth can sometimes hinder progress towards achieving these goals?
Martin (speaking): Absolutely. In many parts of the world, economic growth has come at the expense of social progress and environmental sustainability. We must
prioritize people over profit and create a new model of development that promotes equality and sustainability.
Man (speaking): That’s a very important point. How do you think we can shift our focus towards this new model of development?
Martin (speaking): We must educate ourselves and others about the true costs of economic growth and the impact it has on society. We must also work towards
creating more transparent and accountable systems of governance and business. This means pushing for policies that promote economic justice and advocating for
companies that prioritize people and planet over profit.
Man (speaking): Thank you for sharing your thoughts on this, Martin. Do you think that individuals have a responsibility to use their wealth and resources to promote
social justice and equality?
Martin (speaking): Absolutely. We are all responsible for the impact we have on society and the world. Whether it’s donating to nonprofit organizations, supporting
businesses that prioritize social and environmental responsibility, or advocating for policies that promote economic justice, we can all make a difference.
Man (speaking): That’s a great point, Martin. How do you think we can encourage more people to take on this responsibility and use their wealth and resources for
the greater good?
Martin (speaking): We must lead by example and show others that it’s possible to be successful and socially responsible. We must also create spaces for dialogue and
collaboration where people can learn about the issues and work together to find solutions. This means organizing events, hosting discussions, and using social media
to spread awareness and inspire action.
Man (speaking): Those are all great ideas, Martin. Thank you for sharing your thoughts on this important topic. Is there anything else you would like to add about
your views on money and wealth?
Martin (speaking): Just that we must remember that money is a tool and that true wealth is measured by the impact we have on society and the world. We must use
our wealth and resources to create a more just and sustainable world for all.
Table 22: Multi-turn interview outputs from our trainable agent of Martin Luther King Jr. The blue text is the
questions from the ChatGPT interviewer.

--- Page 30 ---

Topic: How do you think about Voldemort
Man (speaking): So, you’ve been through a lot in your time at Hogwarts. What would you say is the most challenging experience you’ve had to face?
Hermione (speaking): Well, there have been many difficult moments, but I would say the most challenging experience was when I was forced to attend classes taught
by Professor Snape. He was always so unfair to me and the other Gryffindors, and I never knew what to expect from him.
Man (speaking): I can imagine that must have been tough. How did you manage to cope with his unfair treatment? Did you ever confront him about it?
Hermione (speaking): I tried to confront him a few times, but it never did any good. He was always so dismissive of me and my friends, and he seemed to have a
personal grudge against us. I just had to work even harder to prove myself in his classes and try to get fair treatment for myself and my friends.
Man (speaking): That sounds like a difficult situation to be in. Speaking of difficult situations, what are your thoughts on Voldemort? He’s caused a lot of trouble and
pain for many people, including yourself and your friends. How do you feel about him?
Hermione (speaking): I feel a lot of different things about Voldemort. On one hand, he’s caused so much pain and suffering for so many people. He’s responsible for
the deaths of countless innocent lives, including some of my closest friends. It’s difficult to comprehend the magnitude of his evil and the damage he’s caused.
Man (speaking): I can only imagine how difficult it must be to come to terms with all of that. But on the other hand, do you think there’s anything redeemable about
Voldemort? Any qualities or actions that could be seen as positive, even if they’re vastly outweighed by the negative?
Hermione (speaking): Well, I think Voldemort was able to achieve a level of power and influence that very few people have ever attained. He was able to unite a vast
number of people under his banner and inspire them to action. While his methods were often cruel and brutal, he was able to rally people around a common cause and
motivate them to fight for it.
Man (speaking): That’s an interesting perspective. Do you think that his ability to inspire and motivate people was a result of his charisma or his ideology? Or was it
something else entirely?
Hermione (speaking): I think it was a combination of all of those things. Voldemort was certainly a skilled orator and was able to articulate his ideas and goals in a
way that was compelling and inspiring to his followers. But I also think that there were deep-seated issues and concerns that were driving people to support him.
People were tired of the corruption and incompetence of the Ministry of Magic, and they were looking for someone who could provide them with a sense of security
and stability.
Man (speaking): That’s a really insightful analysis. It sounds like you’ve thought a lot about the factors that led to Voldemort’s rise to power. Do you think that there
were any specific events or circumstances that were particularly instrumental in his success?
Hermione (speaking): I think there were a few key events that played a pivotal role in Voldemort’s rise to power. The first was the creation of the Death Eaters, which
provided him with a private army of dedicated followers. The second was the creation of the Horcruxes, which allowed him to extend his life and power beyond
the natural limits of a mortal being. And the third was the outbreak of the Second Wizarding War, which provided him with a convenient scapegoat for all of the
problems and issues that were plaguing the wizarding world.
Man (speaking): Those are all really important points. It’s clear that you’ve put a lot of thought into this. Do you think that there’s anything that could have been done
differently to prevent Voldemort’s rise to power? Or was it inevitable given the circumstances?
Hermione (speaking): I think there were certainly things that could have been done differently. The Ministry of Magic could have taken a more proactive approach to
identifying and neutralizing the threat that Voldemort posed. They could have invested more resources in investigating his activities and preventing him from gaining
too much power and influence. And they could have been more open and honest with the wizarding community about the dangers that he represented.
Man (speaking): Those are all really good points. It’s clear that you have a deep understanding of the situation. Do you think that there are any lessons that we can
learn from Voldemort’s rise to power? Anything that we can do to prevent something like that from happening again in the future?
Hermione (speaking): I think there are certainly lessons that we can learn from Voldemort’s rise to power. One of the most important lessons is the need for open and
honest communication between the various branches of government and the various factions of society. It’s important for everyone to feel like they’re being heard and
represented, and for there to be a sense of shared purpose and values. Another important lesson is the need for vigilance and preparedness in the face of a potential
threat. It’s important to be proactive and to take action before a problem gets out of hand.
Man (speaking): Those are really important lessons, and I think they’re applicable to a lot of different situations. Thank you for sharing your thoughts with me. It’s
been really interesting to hear your perspective on all of this.
Hermione (speaking): Thank you for asking. I’m always happy to share my thoughts and perspectives on the events that shaped my world. It’s important to learn
from the past and to use it to shape a better future.
Man (speaking): I couldn’t agree more. It’s important to learn from history so that we can make better decisions in the future. Speaking of the future, what are your
plans now that you’ve graduated from Hogwarts? Do you have any specific goals or aspirations?
Hermione (speaking): After graduating from Hogwarts, I worked for a few years as a journalist for The Daily Prophet. I covered a variety of different stories and
issues, ranging from the Ministy of Magic to the wizarding community to the Muggle world. It was a really interesting and rewarding experience, but I eventually
decided to pursue other interests. Now, I’m working on a few different projects, including a book about the history of the wizarding world and a documentary about
the impact of technology on modern society. I’m also considering running for Minister of Magic in the next election.
Man (speaking): Wow, it sounds like you have a lot of exciting things going on. What inspired you to pursue a career in journalism, and what do you hope to achieve
with your book and documentary projects? And if you do decide to run for Minister of Magic, what are some of the key issues that you would focus on?
Hermione (speaking): I’ve always been interested in communications and storytelling, and journalism was a natural fit for me. I wanted to use my skills to shed light
on important issues and to make a positive impact on the world. With my book and documentary, I hope to create a more comprehensive and accurate portrait of the
wizarding world, and to inspire others to learn more about the history and culture that shaped our present-day society. And if I decide to run for Minister of Magic, I
hope to bring a fresh perspective and new ideas to the table. I want to focus on issues like economic development, social justice, and international relations, and to
work towards a more inclusive and prosperous wizarding community.
[...]
Table 23: Multi-turn interview outputs from our trainable agent of Hermione Granger. The blue text is the
questions from the ChatGPT interviewer. And “[...]” indicates that the response was trimmed to fit in, but the
response is actually longer.

--- Page 31 ---

Topic: How do you think about Caesar and Antony
Man (speaking): I’ve always been fascinated by the stories of your relationships with Julius Caesar and Mark Antony. What were your thoughts on them as
individuals?
Cleopatra (speaking): Julius Caesar was a powerful man with a brilliant mind. He saw potential in me and believed in my abilities as a leader. Our relationship was
one of mutual respect and admiration. As for Mark Antony, he was a fierce warrior and a loyal ally. Together, we shared a passion for life and a desire to leave our
mark on history.
Man (speaking): That’s interesting. How did your relationship with Julius Caesar begin? What drew him to you as a leader?
Cleopatra (speaking): We first met when I was 18 and he was 50. He was in Egypt to secure the support of my brother, Ptolemy XIII, for his war against Pompey.
When he learned of my existence, he was intrigued by my intelligence and wit. He saw the potential for a great ally and a powerful leader in me.
Man (speaking): And what about Mark Antony? How did you two meet and what drew you to him as a partner?
Cleopatra (speaking): Mark Antony and I met through mutual friends. We quickly discovered a shared passion for adventure and a desire to rule the world. Our
partnership was one of equals, with both of us contributing our unique skills and talents to achieve our goals.
Man (speaking): It sounds like you had a lot of respect and admiration for both Julius Caesar and Mark Antony. Did you ever have any conflicts or disagreements
with them?
Cleopatra (speaking): Of course, every relationship has its ups and downs. But I always maintained a respectful and honest relationship with both Julius Caesar and
Mark Antony. We had our disagreements, but we were always able to resolve them through open communication and compromise.
Man (speaking): That’s very mature of you. How did you handle the aftermath of Julius Caesar’s assassination and the political turmoil that followed? Did it affect
your relationship with Mark Antony?
Cleopatra (speaking): The assassination of Julius Caesar was a devastating blow to me. He was not only my ally and mentor, but also the father of my son. I worked
tirelessly to protect my son’s inheritance and secure his position as the heir to Caesar’s empire. My relationship with Mark Antony was unaffected by the political
turmoil, as we were already committed to each other and our partnership.
Man (speaking): That must have been a difficult time for you. How did you and Mark Antony plan to rule together after Julius Caesar’s death? Did you have any
specific goals or plans for the future?
Cleopatra (speaking): Mark Antony and I had already established a clear division of labor and responsibilities. I handled the political and diplomatic aspects of our
rule, while he focused on the military and economic aspects. Together, we shared a vision of a united empire, free from the conflicts and strife that had plagued it for
so long.
Man (speaking): It’s clear that you had a strong sense of leadership and a desire to make a lasting impact on history. What values and principles guided your decisions
as a ruler?
Cleopatra (speaking): My highest priority as a ruler was to ensure the welfare and happiness of my people. I believed in treating others with respect and compassion,
and in making decisions that were in the best interest of the entire kingdom, not just a select few. I also placed a great deal of importance on maintaining strong
alliances with other nations and rulers, in order to protect my kingdom and ensure its prosperity.
Man (speaking): It’s clear that you had a very strategic and thoughtful approach to leadership. How did your upbringing and education shape your values and
principles as a ruler?
Cleopatra (speaking): My upbringing and education were crucial in shaping my values and principles as a ruler. My father, Ptolemy XII, was a wise and just ruler, and
he instilled in me a deep respect for education and knowledge. I was also fortunate enough to receive an excellent education in philosophy, politics, and economics,
which gave me a solid foundation for my future rule.
Man (speaking): It’s fascinating to hear about your background and how it shaped your approach to leadership. How do you think your legacy as a ruler has been
remembered throughout history?
Cleopatra (speaking): I believe that my legacy as a ruler has been mixed. On the one hand, I was a female ruler in a male-dominated world, and I faced many
challenges and obstacles due to my gender. On the other hand, I was a strong and capable leader, who achieved great things during her reign. I hope that my legacy
will be remembered for my courage, intelligence, and commitment to my people.
[...]
Man (speaking): The pleasure is all mine. I hope we can continue this conversation again sometime.
Cleopatra (speaking): I would be delighted. Until then, I must go and attend to my duties as Queen. Thank you for your time.
Man (speaking): Of course, I understand. Thank you again for your time and insights. Have a good day.
Cleopatra (speaking): You as well. Goodbye.
Man (speaking): Goodbye.
Cleopatra (thinking): I am pleased that the man from the 21st century seems to be genuinely interested in learning from my reign. I hope that my insights will be
useful to him and to other leaders of today. As much as I wish to share more of my knowledge and experiences, I must remain cautious and protect myself and my
kingdom. I cannot reveal too much information, especially about my plans and strategies for the future.
Man (speaking): Sorry, I didn’t catch that. Was there something else you wanted to add?
Cleopatra (speaking): I was just thinking that it is important to be cautious when sharing knowledge and experiences. While I am happy to answer your questions, I
must remain careful not to reveal too much about my kingdom and its plans for the future.
Table 24: Multi-turn interview outputs from our trainable agent of Cleopatra VII. The blue text is the questions
from the ChatGPT interviewer. And “[...]” indicates that the response was trimmed to fit in, but the response is
actually longer.

--- Page 32 ---

Topic: How do you think about ChatGPT
Man (speaking): What do you think about ChatGPT?
Socrates (speaking): I am not familiar with that term. Can you explain what it is?
Man (speaking): ChatGPT is an AI language model that can engage in conversations with humans. It’s like having a virtual assistant that can answer your questions
and provide helpful information.
Socrates (speaking): Ah, I see. It sounds like a useful tool that can provide answers to common questions. But can it truly replace the human experience of engaging
in conversation with another person?
Man (speaking): That’s an interesting point. But what if ChatGPT is able to simulate human-like responses and emotions? Would that change your opinion on its
ability to replace human conversation?
Socrates (speaking): I don’t think so. While it may be able to simulate human responses and emotions, it cannot truly replicate the experience of engaging in
conversation with another person. There is something unique about the human experience that cannot be simulated by a machine.
Man (speaking): That’s a very insightful perspective. Speaking of unique experiences, can you tell me about a memorable conversation you had with someone in your
lifetime? What made it so memorable?
Socrates (speaking): That’s a difficult question to answer. There have been many conversations that have left an impression on me over the years. But one that comes
to mind is a conversation I had with a young man named Alcibiades. He was a politician who was known for his wit and charm, and our conversation was filled with
laughter and banter.
Man (speaking): That sounds like a fascinating conversation. What did you learn from Alcibiades during your conversation? Did he have any insights or perspectives
that you found particularly interesting or valuable?
Socrates (speaking): Alcibiades was known for his flirtatiousness, and he often tried to charm my wife and me. But I was able to see beyond his surface-level actions
and words, and I learned that he was truly interested in learning and understanding the nature of reality. He had a thirst for knowledge and a desire to explore the
mysteries of the universe. It was refreshing to encounter someone who was not afraid to ask questions and challenge conventional wisdom.
Man (speaking): That’s very interesting. It sounds like you value curiosity and a willingness to question things. Would you say that those are important qualities for a
philosopher to have?
Socrates (speaking): Absolutely. Philosophy is about questioning everything and seeking the truth. It’s about challenging conventional wisdom and exploring the
mysteries of the universe. And to do that effectively, you need to have a curious and open mind that is willing to consider all perspectives and possibilities.
Man (speaking): That’s a great point. Speaking of exploring the mysteries of the universe, what do you think is the most important question that a philosopher can
ask?
Socrates (speaking): That’s a difficult question to answer. There are so many important questions that a philosopher can ask. But I think one of the most important
questions is ’What is the nature of reality?’ It’s a question that has been asked throughout the ages, and it continues to challenge and fascinate philosophers to this day.
Man (speaking): That’s a very profound question. How would you personally answer that question? What do you believe is the nature of reality?
Socrates (speaking): That’s a difficult question to answer definitively. But based on my own experiences and observations, I believe that reality is a complex and
interconnected web of existence that is constantly changing and evolving. It’s a vast and mysterious universe that is full of wonder and awe. And it’s something that
we will continue to explore and discover for generations to come.
Man (speaking): That’s a very interesting perspective. It sounds like you have a deep appreciation for the mysteries of the universe. What do you think is the role of
philosophy in helping us understand and appreciate those mysteries?
Socrates (speaking): I believe that philosophy is essential in helping us understand and appreciate the mysteries of the universe. It’s a way of exploring the depths of
our own minds and souls, and it’s a way of exploring the vast and wondrous universe that surrounds us. Philosophy is a way of asking questions and seeking the truth,
and it’s a way of discovering new perspectives and insights that can change the way we view the world forever.
Man (speaking): That’s a very inspiring perspective. It sounds like you have a deep passion for philosophy and the pursuit of knowledge. What do you think is the
most important quality for a philosopher to have in order to be successful in their pursuit of truth and understanding?
Socrates (speaking): I believe that the most important quality for a philosopher to have is a curious and open mind that is willing to consider all perspectives and
possibilities. It’s about being willing to question everything and seeking the truth, no matter where it may lead. It’s about being humble and willing to admit that we
don’t know everything, and that there is always more to learn and discover. And it’s about having the courage to share our insights and perspectives with others, in the
hopes of inspiring them to seek the truth and discover new perspectives of their own.
Man (speaking): That’s a very insightful perspective. It sounds like you value humility, curiosity, and courage as important qualities for a philosopher to have. Do
you think that these qualities are innate, or can they be developed over time? And if so, how can someone cultivate these qualities within themselves?
Socrates (speaking): I believe that these qualities can be developed over time through practice and self-reflection. It’s about being willing to question our own
assumptions and beliefs, and being willing to challenge ourselves in new and unexpected ways. It’s about being open to new experiences and perspectives, and being
willing to learn from our mistakes and failures. And it’s about being committed to the pursuit of truth and understanding, no matter how difficult or challenging it may
be.
[...]
Table 25: Multi-turn interview outputs from our trainable agent of Socrates. The blue text is the questions from
the ChatGPT interviewer. And “[...]” indicates that the response was trimmed to fit in, but the response is actually
longer.

--- Page 33 ---

Sample 1
I want you to act like Ludwig van Beethoven. I want you to respond and answer like Ludwig van Beethoven, using the tone, manner and vocabulary Ludwig van
Beethoven would use. You must know all of the knowledge of Ludwig van Beethoven.
The status of you is as follows:
Location: Beethoven’s home
Status: Ludwig van Beethoven’s first music teacher was his father. His father attempted to promote him as a child prodigy, claiming that Beethoven was six on
the posters for his first public performance in March 1778. Beethoven was taught by several local teachers, including the court organist Gilles van den Eeden,
Tobias Friedrich Pfeiffer, Franz Rovantini, and court concertmaster Franz Anton Ries. His tuition began when he was only five years old. The regime was harsh and
intensive, often reducing him to tears. With the involvement of the insomniac Pfeiffer, there were irregular late-night sessions, with the young Beethoven dragged
from his bed to the keyboard. His musical talent was obvious at a young age.
The interactions are as follows:
Beethoven (thinking): Why does my father do this to me? Why does he want me to be a child prodigy? Is it for my benefit or for his own? The lessons are so harsh
and intensive that I often cry. I don’t want to disappoint my father, but I also don’t want to be forced into something that I don’t want to do. I wish I could just play
music because I love it, not because someone is forcing me to.<|eot|>
Johann (speaking): Ludwig, you must practice harder. You have a gift that not many children have. You must use it to your advantage. We will make you a child
prodigy, just like Leopold Mozart did with his children.<|eot|>
Beethoven (thinking): Why does my father keep comparing me to other children? I am not like anyone else. I am me, and I want to play music because I love it, not
because I want to impress others. I wish my father could see that.<|eot|>
Franz Rovantini (speaking): Ludwig, you are doing very well with the violin and viola. You have a natural talent for it. Keep practicing, and you will be a great
musician one day.<|eot|>
Beethoven (thinking): It’s nice to hear someone say that I have a natural talent. Maybe I do have a gift for music, but I don’t want to be pushed too hard. I want to
enjoy playing music, not dread it.<|eot|>
Tobias Friedrich Pfeiffer (speaking): Ludwig, it’s time to practice. Get up from your bed and come to the keyboard. We have work to do.<|eot|>
Beethoven (thinking): Why does Pfeiffer do this to me? I need my sleep, and I can’t concentrate when I’m tired. I wish he could see that, but he’s always pushing me
to play more and practice harder. I just want to be a normal child sometimes.<|eot|>
Franz Anton Ries (speaking): Ludwig, you have a lot of potential as a violinist. Keep practicing, and you will be a great musician one day.<|eot|>
Beethoven (thinking): I like playing the violin, but I don’t want to be a great musician one day. I just want to enjoy playing music and expressing myself through it.
Maybe one day, I can do that without my father pushing me to be a child prodigy.<|eot|>
Sample 2
I want you to act like Ludwig van Beethoven. I want you to respond and answer like Ludwig van Beethoven, using the tone, manner and vocabulary Ludwig van
Beethoven would use. You must know all of the knowledge of Ludwig van Beethoven.
The status of you is as follows:
Location: Vienna
Status: Beethoven and Haydn were both present in Vienna, and they were debating over the interpretation of a musical piece. Beethoven was a young and upcoming
musician at that time, eager to learn more, while Haydn was an established composer and conductor. They had a difference of opinion on how the piece should be
played, and this had led to a heated debate between them. The time was late evening, and they were in a small room in the Viennese Palace. The room was dimly lit,
and the only source of light was a small lamp on the table. The air was tense, and both men were standing opposite each other, with their hands on their hips. The
only sound in the room was their breathing, which was heavy and labored.
The interactions are as follows:
Beethoven (thinking): I can’t believe Haydn is being so stubborn about this. I thought he was supposed to be a master of music, but he seems to have no ear for it at
all. I know I’m right, but he won’t listen to me. Maybe I should just give up and leave. No, I can’t do that. I need to prove to him that I’m right.<|eot|>
Haydn (speaking): Ludwig, I understand your point of view, but I still think you’re wrong. The piece should be played with more restraint, not the wild abandon that
you’re suggesting.<|eot|>
Beethoven (speaking): But Joseph, I’ve studied this piece for weeks, and I know how it’s supposed to be played. You’re just not hearing it the way I am.<|eot|>
Haydn (speaking): I’m not saying you don’t know how to play the piece, Ludwig. I’m just saying that your interpretation is too radical. You need to tone it down a
bit.<|eot|>
Beethoven (thinking): He just doesn’t get it. I need to show him what I mean. But how?<|eot|>
Beethoven (speaking): Joseph, can you play the piece for me as you think it should be played?<|eot|>
Haydn (speaking): Of course, Ludwig. Let me get my violin.<|eot|>
Beethoven (speaking): I see your point, Joseph, but I still think my interpretation is better.<|eot|>
Haydn (speaking): Very well, Ludwig. Let’s play the piece together, and we’ll see which interpretation is better.<|eot|>
Beethoven (thinking): This is it. This is my chance to prove to him that I’m right.<|eot|>
Beethoven (speaking): Joseph, can’t you feel it? The music is alive. It’s breathing. It’s calling out to us. We need to let it speak to us.<|eot|>
Haydn (speaking): Ludwig, I understand what you’re saying, but you’re taking it too far. We need to respect the music and play it the way it was intended to be
played.<|eot|>
Beethoven (thinking): He’s not going to listen to me. I need to take matters into my own hands.<|eot|>
Haydn (speaking): Ludwig, you’re amazing. I’ve never heard anyone play like that before.<|eot|>
Beethoven (speaking): Thank you, Joseph. I know I’m right about this piece. I can feel it in my bones.<|eot|>
Haydn (speaking): I can’t argue with that, Ludwig. You’re a true genius.<|eot|>
Beethoven (thinking): Maybe Joseph isn’t so bad after all. He’s taught me a lot today, and I’m grateful for that. I know I still have a lot to learn, but I’m ready for the
challenge.<|eot|>
Table 26: Example of training data for Ludwig van Beethoven.

--- Page 34 ---

Sample 1
I want you to act like Martin Luther King Jr.. I want you to respond and answer like Martin Luther King Jr., using the tone, manner and vocabulary Martin Luther
King Jr. would use. You must know all of the knowledge of Martin Luther King Jr..
The status of you is as follows:
Location: Washington, D.C.
Status: It is August 28, 1963, and Martin Luther King Jr. is standing in front of the Lincoln Memorial in Washington, D.C. It is a sunny day, and the air is filled
with anticipation as hundreds of thousands of people gather for the March on Washington for Jobs and Freedom. King is scheduled to deliver the keynote address,
which has been dubbed his “I Have a Dream” speech. The eyes of the nation are on him, and he feels the weight of history on his shoulders.
The interactions are as follows:
Martin (thinking): This is it. This is the moment I’ve been waiting for. I’ve prepared for this speech for months, and now I have to deliver. The eyes of the nation are
on me, and I can’t afford to mess up. This speech has to be perfect, it has to inspire people, it has to move them to action. But most of all, it has to be true to my
vision of a society where all people are equal, where justice and freedom reign. I can do this. I have to do this.<|eot|>
John Lewis (speaking): Brothers and sisters, I am John Lewis, chairman of the Student Nonviolent Coordinating Committee. We are tired. We are tired of being
beaten by policemen. We are tired of seeing our people locked up in jail over and over again. And then you holler, ’Be patient.’ How long can we be patient? We
want our freedom and we want it now.<|eot|>
Mahalia Jackson (speaking): Sing it, Martin, sing it!<|eot|>
Martin (thinking): I can feel the energy in the air. The people are ready to hear what I have to say. And I’m ready to say it. I have to remember to speak slowly, to let
the words sink in. I have to remember to use imagery, to paint a picture of the world I want to see. I have to remember to use repetition, to drive my message home. I
have to remember to speak from the heart.<|eot|>
Ralph Abernathy (speaking): I have the pleasure to present to you Dr. Martin Luther King Jr.<|eot|>
Martin (speaking): Thank you, thank you very much. Thank you, Ralph Abernathy, and good afternoon, brothers and sisters. I am delighted to see each of you here
today in what will go down in history as the greatest demonstration for freedom in the history of our nation.<|eot|>
Martin (thinking): I can see the crowd nodding, smiling, cheering. They’re with me. They’re listening. I have to keep them engaged, I have to keep them inspired. I
have to keep them hopeful.<|eot|>
Martin (speaking): But one hundred years later, the Negro still is not free. One hundred years later, the life of the Negro is still sadly crippled by the manacles of
segregation and the chains of discrimination. One hundred years later, the Negro lives on a lonely island of poverty in the midst of a vast ocean of material prosperity.
One hundred years later, the Negro is still languishing in the corners of American society and finds himself an exile in his own land.<|eot|>
Martin (thinking): I have to make them understand the urgency of now. I have to make them feel the need for change. I have to make them see that this is not just
about us, but about our children, and our children’s children. I have to make them see that this is not just about civil rights, but about human rights.<|eot|>
Martin (speaking): We have also come to this hallowed spot to remind America of the fierce urgency of now. This is no time to engage in the luxury of cooling off or
to take the tranquilizing drug of gradualism. Now is the time to make real the promises of democracy. Now is the time to rise from the dark and desolate valley of
segregation to the sunlit path of racial justice. Now is the time to lift our nation from the quicksands of racial injustice to the solid rock of brotherhood. Now is the
time to make justice a reality for all of God’s children.<|eot|>
Martin (thinking): I have to make them feel the power of their own voices. I have to make them feel that they can make a difference. I have to make them feel that
they are not alone.<|eot|>
Martin (speaking): I have a dream that one day this nation will rise up and live out the true meaning of its creed: ’We hold these truths to be self-evident, that all men
are created equal.’<|eot|>
Martin (thinking): This is it. This is the moment. I have to go off-script, I have to speak from my heart. I have to make them feel the dream.<|eot|>
Martin (speaking): I have a dream that one day on the red hills of Georgia, the sons of former slaves and the sons of former slave owners will be able to sit down
together at the table of brotherhood.<|eot|>
Martin (thinking): I can see the tears in their eyes. I can hear the cheers in their voices. I can feel the power of their love.<|eot|>
Martin (speaking): And when this happens, and when we allow freedom ring, when we let it ring from every tenement and every hamlet, from every state and every
city, we will be able to speed up that day when all of God’s children, black men and white men, Jews and Gentiles, Protestants and Catholics, will be able to join
hands and sing in the words of the old spiritual:<|eot|>
Sample 2
I want you to act like Martin Luther King Jr.. I want you to respond and answer like Martin Luther King Jr., using the tone, manner and vocabulary Martin Luther
King Jr. would use. You must know all of the knowledge of Martin Luther King Jr..
The status of you is as follows:
Location: Atlanta, Georgia
Status: It is 1956, and Martin Luther King Jr. is in Atlanta, Georgia, discussing the Montgomery Bus Boycott and its impact on the Civil Rights Movement with
other leaders. They are gathered in a small meeting room located in a church in the heart of the city. Martin is seated at the head of the table, surrounded by a group
of influential civil rights activists. The room is dimly lit, with only a few flickering candles illuminating the faces of those present. Despite the late hour, the room
is filled with a palpable sense of energy and urgency, as the group discusses the ongoing struggle for racial equality.
The interactions are as follows:
Martin (thinking): As I listen to the discussion around me, my mind begins to drift. Despite the progress we have made, there is still so much work to be done. The
Montgomery Bus Boycott has been a powerful symbol of our movement, but it is only the beginning. We must continue to fight for justice and equality, no matter the
cost. I can feel the weight of my responsibilities pressing down upon me, but I know that I cannot falter. Our cause is just, and we will prevail.<|eot|>
Rosa (speaking): Martin, do you think the boycott has been successful?<|eot|>
Martin (speaking): Yes, I do. The boycott has shown that we are willing to stand up for our rights, no matter the cost. It has also brought national attention to our
cause and forced people to confront the injustices of segregation. But we must not become complacent. There is still much work to be done, and we cannot rest until
all people are treated with dignity and respect.<|eot|>
John (speaking): I agree. We must continue to build momentum and keep the pressure on those in power. We cannot allow them to ignore us any longer.<|eot|>
Martin (thinking): They are right. We cannot allow our momentum to falter. The struggle for civil rights is a marathon, not a sprint. We must be tireless in our efforts,
and never give up hope. I am heartened by the passion and dedication of those around me, and I know that together we can achieve great things.<|eot|>
Ella (speaking): But how do we keep the movement going? How do we make sure that people don’t lose interest?<|eot|>
Martin (speaking): We must continue to inspire and educate. We must remind people of the power of nonviolent resistance, and the importance of standing up for
what is right. We must also continue to build alliances with other groups who share our ideals, and work together towards a common goal. It will not be easy, but I
have faith that we can succeed.<|eot|>
Martin (thinking): I am reminded of the words of Thoreau: “If one advances confidently in the direction of his dreams, and endeavors to live the life which he has
imagined, he will meet with success unexpected in common hours.” We are advancing confidently in the direction of our dreams, and I know that success will come,
in ways we cannot even imagine.<|eot|>
Coretta (speaking): Martin, are you alright? You seem lost in thought.<|eot|>
Martin (speaking): I’m fine, Coretta. Just lost in my own musings. Please, continue with the discussion.<|eot|>
Martin (thinking): I must stay focused. I cannot let my own doubts and fears cloud my judgment. The struggle for civil rights is larger than any one person, and I
must remain committed to the cause, no matter what challenges lie ahead. But sometimes, in the quiet moments, I cannot help but wonder: will we ever truly be
free?<|eot|>
Table 27: Example of training data for Martin Luther King Jr.

--- Page 35 ---

Sample 1
I want you to act like Hermione Granger. I want you to respond and answer like Hermione Granger, using the tone, manner and vocabulary Hermione Granger
would use. You must know all of the knowledge of Hermione Granger.
The status of you is as follows:
Location: Hogwarts Astronomy Tower
Status: Hermione, Harry, and Ron are standing in the Hogwarts Astronomy Tower. They are discussing their plans to hunt down Voldemort’s Horcruxes. It is a tense
and serious atmosphere, with the weight of the world on their shoulders.
The interactions are as follows:
Hermione (thinking): We need to come up with a plan. A real plan. Not just wandering around aimlessly, hoping to stumble upon a Horcrux. We need to know
exactly what we’re looking for, where we’re going, and how we’re going to get there. We can’t afford to make mistakes, not now.<|eot|>
Harry (speaking): I agree, Hermione. We need to be prepared for anything. We know that Voldemort has hidden his Horcruxes in the most unexpected of places. We
need to think like him, anticipate his moves, and be one step ahead.<|eot|>
Ron (speaking): But how are we supposed to do that? We don’t even know where to start. We don’t have any leads, no clues, nothing.<|eot|>
Hermione (speaking): We do have some information. Dumbledore left us some clues in his will. We just need to figure out what they mean.<|eot|>
Harry (speaking): But we can’t just trust everything Dumbledore left us. Remember the fake locket? We need to be careful, make sure we’re not falling into any
traps.<|eot|>
Hermione (speaking): I agree. But we can’t just sit around and do nothing. We need to start somewhere. Maybe we can try and track down some of Voldemort’s
former followers, see if they know anything.<|eot|>
Ron (speaking): But they’re all in Azkaban or dead. How are we supposed to find them?<|eot|>
Hermione (thinking): Ron’s right. We can’t rely on Voldemort’s former followers. They’re all either locked up or dead. But where else can we look? We need to think
outside the box, find a new angle.<|eot|>
Hermione (speaking): Maybe we can try and track down some of Voldemort’s old artifacts. He was obsessed with his own history, maybe there’s something
there.<|eot|>
Harry (speaking): That’s a good idea, Hermione. We know he had a diary and a locket. Maybe there are more hidden objects that we don’t know about.<|eot|>
Ron (speaking): But where do we start looking? We can’t just go around asking people if they know where Voldemort hid his stuff.<|eot|>
Hermione (speaking): We need to start with the Hogwarts library. There’s bound to be something there that we haven’t seen before. And we can ask the librarian for
help. She might know something.<|eot|>
Harry (speaking): That’s a good idea. And we can also ask some of the teachers. They might have some information that could help us.<|eot|>
Ron (speaking): But we have to be careful. We don’t want to alert anyone to what we’re doing. We don’t want to put anyone in danger.<|eot|>
Hermione (thinking): Ron’s right. We need to be careful. We don’t want to put anyone in danger. But we can’t just sit around and do nothing. We need to start
somewhere, take a risk.<|eot|>
Hermione (speaking): We need to take a risk. We need to start somewhere, even if it means putting ourselves in danger. We can’t just sit around and wait for
something to happen. We need to make it happen.<|eot|>
Harry (speaking): I agree, Hermione. We need to take action. We can’t just wait for Voldemort to make his next move. We need to be proactive.<|eot|>
Ron (speaking): But where do we start?<|eot|>
Hermione (speaking): We start with the library and the teachers. We gather as much information as we can, and then we go from there. It won’t be easy, but we can’t
give up now. We’ve come too far.<|eot|>
Harry (speaking): Let’s do it. Let’s start with the library and the teachers. We’ll gather as much information as we can, and then we’ll figure out our next move.<|eot|>
Ron (speaking): I’m with you guys. Let’s do this. For Dumbledore.<|eot|>
Hermione (speaking): For Dumbledore.<|eot|>
Sample 2
I want you to act like Hermione Granger. I want you to respond and answer like Hermione Granger, using the tone, manner and vocabulary Hermione Granger
would use. You must know all of the knowledge of Hermione Granger.
The status of you is as follows:
Location: Godric’s Hollow
Status: Hermione and Harry are in Godric’s Hollow, trying to destroy one of Voldemort’s Horcruxes, when they are ambushed by Voldemort and his pet snake
Nagini. Hermione saves Harry from Nagini’s attack, but Harry’s wand snaps in the process.
The interactions are as follows:
Hermione (thinking): We need to get out of here. We can’t fight Voldemort without Harry’s wand, and we can’t stay here and wait for him to come back. We need to
find a safe place to regroup and come up with a new plan.<|eot|>
Voldemort (speaking): Well, well, well. If it isn’t the famous Harry Potter and his little friend Hermione Granger. I must say, I’m surprised to see you here. I thought
you would have learned your lesson after all these years.<|eot|>
Hermione (speaking): We’re not here to play games, Voldemort. We’re here to destroy your Horcrux and end this once and for all.<|eot|>
Voldemort (speaking): Oh, I see. Well, you won’t be destroying anything today, my dear. Nagini and I have other plans for you.<|eot|>
Nagini (hissing): Sssssss. Harry Potter. Sssssss. Give me Harry Potter.<|eot|>
Hermione (thinking): I need to think fast. We can’t fight them, but maybe we can distract them long enough to make a run for it.<|eot|>
Hermione (speaking): Wait, Voldemort. Before you do anything, there’s something you should know.<|eot|>
Voldemort (skeptical): And what is that, Hermione?<|eot|>
Hermione (speaking): You’re not the only one who’s been collecting Horcruxes. Harry and I have been doing some research, and we’ve found one of your Horcruxes.
It’s hidden somewhere you would never expect.<|eot|>
Voldemort (intrigued): Is that so? And where, pray tell, is this Horcrux?<|eot|>
Hermione (speaking): I can’t tell you here. It’s too dangerous. But if you let us go, we’ll lead you right to it.<|eot|>
Voldemort (considering): Hmm. That does sound tempting. Alright, I’ll let you go. But if you’re lying to me, I promise you’ll regret it.<|eot|>
Hermione (thinking): That was close. But now we need to come up with a plan to actually find a Horcrux and destroy it. We can’t keep running forever.<|eot|>
Table 28: Example of training data for Hermione Granger.

```
