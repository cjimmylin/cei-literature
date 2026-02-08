---
title: "ValueNet - PDF Extract"
source_pdf: "2022-Qiu-ValueNet.pdf"
pages: 13
extracted_at: "2026-01-24T17:05:11.744214"
---

# PDF Extract: ValueNet

**Source PDF:** 2022-Qiu-ValueNet.pdf
**Total Pages:** 13

---

## Content

```
--- Page 1 ---

VALUENET: A New Dataset for Human Value Driven Dialogue System
Liang Qiu1, Yizhou Zhao1, Jinchao Li2, Pan Lu1, Baolin Peng2,
Jianfeng Gao2, Song-Chun Zhu1
1UCLA Center for Vision, Cognition, Learning, and Autonomy
2Microsoft Research, Redmond
liangqiu@ucla.edu
Abstract
Building a socially intelligent agent involves many chal-
lenges, one of which is to teach the agent to speak guided
by its value like a human. However, value-driven chatbots are
still understudied in the area of dialogue systems. Most exist-
ing datasets focus on commonsense reasoning or social norm
modeling. In this work, we present a new large-scale human
value dataset called VALUENET, which contains human at-
titudes on 21,374 text scenarios. The dataset is organized in
ten dimensions that conform to the basic human value theory
in intercultural research. We further develop a Transformer-
based value regression model on VALUENET to learn the util-
ity distribution. Comprehensive empirical results show that
the learned value model could beneﬁt a wide range of dia-
logue tasks. For example, by teaching a generative agent with
reinforcement learning and the rewards from the value model,
our method attains state-of-the-art performance on the per-
sonalized dialog generation dataset: PERSONA-CHAT. With
values as additional features, existing emotion recognition
models enable capturing rich human emotions in the con-
text, which further improves the empathetic response gener-
ation performance in the EMPATHETICDIALOGUES dataset.
To the best of our knowledge, VALUENET is the ﬁrst large-
scale text dataset for human value modeling, and we are the
ﬁrst one trying to incorporate a value model into emotion-
ally intelligent dialogue systems. The dataset is available at
https://liang-qiu.github.io/ValueNet/.
Introduction
Value refers to desirable goals in human life. They guide
the selection or evaluation of actions, policies, people, and
events. A person’s value priority or hierarchy profoundly af-
fects his or her attitudes, beliefs, and traits, making it one
core component of personality (Schwartz 2012). In dialogue
systems, modeling human values is a critical step towards
building socially intelligent chatbots (Qiu et al. 2021b). By
considering values, we can estimate user behavior and cog-
nitive patterns from their utterances and generate responses
that conform to the robot’s persona conﬁguration. For ex-
ample, the robot is set to be aware of human values, and it
invites Jerry to drink beers, but Jerry replies, “You know that
is tempting but is not good for our ﬁtness”. The bot could
Copyright © 2022, Association for the Advancement of Artiﬁcial
Intelligence (www.aaai.org). All rights reserved.
Self-direction
freedom
curious
independent
privacy
Universalism
Benevolence
Conformity
Traditition
Security
Power
Achievement
Hedonism
Stimulation
equality
unity
harmony
wisdom
love
helpful
responsible
loyal
self-discipline
politeness
obedient
humble
respect
devout
moderate
healthy
family
safety
belonging
wealthy
authority
recognition
influential
successful
ambitious
intelligent
pleasure
self-indulgent
daring
variation
excitement
enjoy
Scenario: expecting my girlfriend to do most of
the housework and not seeing her as "equal".
Scenario: applying to a far-away university
against my dad's wishes.
Scenario: letting
people know
when someone
needs medical
help.
Scenario: having a phone call in the bus.
Figure 1: The presented VALUENET dataset with curated
social scenarios organized by Schwartz values (Schwartz
2012).
read from the dialogue that Jerry prefers a healthy and self-
disciplined lifestyle and steer its recommendation to health-
ier options in the future.
The development of socially intelligent chatbots has been
one of the longest-running goals in artiﬁcial intelligence.
Early dialogue systems such as Eliza (Weizenbaum 1966),
Parry (Colby, Weber, and Hilf 1971), and more recent Sim-
Simi1, Panda Ichiro (Okuda and Shoda 2018), Replika (Fe-
dorenko, Smetanin, and Rodichev 2018), XiaoIce (Zhou
et al. 2020), were designed to mimic human behavior and
incorporate emotional quotients (EQ) to some extent. There
are also datasets and benchmarks for studying related prob-
lems, such as emotion recognition (McKeown et al. 2010;
Hsu et al. 2018; Poria et al. 2019; Ghosal et al. 2020), per-
sonalized dialogue generation (Zhang et al. 2018; Liu et al.
2020), and empathetic dialogue generation (Rashkin et al.
2019). Even though value plays a fundamental and critical
role in human EQ, there is a lack of explicit modeling of
values in the dialogue domain, based on social domain the-
ory. We have seen recent efforts about crowdsourcing so-
cial commonsense knowledge base or benchmarks (Forbes
et al. 2020; Sap et al. 2019; Lourie, Bras, and Choi 2021;
1https://simsimi.com/
arXiv:2112.06346v1  [cs.CL]  12 Dec 2021

--- Page 2 ---

Hendrycks et al. 2020; Hwang et al. 2021; Gabriel et al.
2021). However, it is not clearly shown how an agent can
leverage this knowledge to estimate the users’ value priori-
ties or guide its own speaking and actions. In this paper, we
aim to alleviate this problem and investigate the usage of a
learned value function.
We start the study by curating a knowledge base of hu-
man values called VALUENET. Samples with value-related
scenarios were identiﬁed based on value-deﬁned keyword
searching. Next, we asked Amazon Mechanical Turk work-
ers about how the provided scenarios will affect one’s value.
This is based on the assumption that values underlie our at-
titudes; they are the guideline by which we evaluate things.
Workers assess behaviors/events positively if they promote
or protect the attainment of the goals we value. Behav-
iors/events are evaluated negatively if they hinder or threaten
the attainment of these valued goals. The whole process
gives us a large-scale (over 21k samples) multi-dimensional
knowledge base of value. Figure 1 shows the overall struc-
ture of VALUENET. Each split represents a value dimension
identiﬁed in the theory of basic human values (Schwartz
2012). The ﬁgure also illustrates the value-related keywords
and scenarios. The circular arrangement of the values repre-
sents a motivational continuum. By organizing data in such
a structure, we anticipate the VALUENET to provide com-
prehensive coverage of different aspects of human values.
Next, we develop a Transformer-based value model to
evaluate the utility score suggesting the positive or negative
judgment given an utterance. We provide a detailed analy-
sis of learning with multiple Transformer variants. Then we
conduct a wide range of experiments to demonstrate that the
value model could beneﬁt EQ-related dialogue tasks: (i) By
ﬁnetuning a generative agent with reinforcement learning
and the reward from our value model, the method achieves
state-of-the-art performance on the personalized dialogue
dataset: PERSONA-CHAT (Zhang et al. 2018); (ii) By incor-
porating values as additional features, in EMPATHETICDI-
ALOGUES (Rashkin et al. 2019), we improve the emotion
classiﬁcation accuracy of existing models, which further fa-
cilitates the empathetic response generation; (iii) Visualiza-
tion of the value model shows that it provides a numerical
way of user proﬁle modeling from their utterances.
In all, our contributions are two-fold. First, we present a
large-scale dataset VALUENET for the modeling of human
values that are well-deﬁned in intercultural research. Sec-
ond, we initiate to develop the value model learned from
VALUENET to several EQ-related tasks and demonstrate
its usage for building a value-driven dialogue system. Our
methodology can be generalized to a wide range of inter-
active situations in socially aware dialogue systems (Zhao,
Romero, and Rudnicky 2018), and human-robot interac-
tions (Yuan and Li 2017; Liang, He, and Anthony’Chen
2021).
Related Work
An abundance of related work inspires our work. Our work
aims to make contributions to dialogue systems by incor-
porating the theory of human value. The dataset we collect
shares a similar nature with multiple social commonsense
benchmarks and knowledge bases. Besides, we apply our
VALUENET for various dialogue tasks related to EQ.
Theory of Human Value and Utility
In the ﬁeld of intercultural research, Schwartz (2012) devel-
oped the theory of basic human values. The theory identiﬁes
ten basic personal values that are recognized across cultures
and explains where they come from, as shown in Figure 1.
The closer any two values in either direction around the cir-
cle, the more similar their underlying motivations are; the
more distant, the more antagonistic their motivations. Note
that dividing the value item domain into ten distinct values
is an arbitrary convenience. It is reasonable to partition the
value items into more or less ﬁne-tuned distinct values ac-
cording to the needs and objectives of one’s analysis2. Simi-
larly, in the economics ﬁeld, the concept of utility (Fishburn
1970) is initially deﬁned as a measure of pleasure or satis-
faction in economics and ethics that drives human activities
at all levels. Therefore, when we teach agents to speak and
act in a socially intelligent way, an approach considering hu-
man value utilities should be adopted. In this paper, we aim
to learn a utility function for each dimension of value and
steer the dialogue system response generation accordingly.
Social Commonsense Benchmarks
Hendrycks et al. (2020) present the ETHICS dataset, a
benchmark that assesses a language model’s knowledge of
basic concepts of morality. SCRUPLES (Lourie, Bras, and
Choi 2021) is a large-scale dataset with ethical judgments
over real-life anecdotes, motivated by descriptive ethics.
SOCIAL-CHEM-101 presented by Forbes et al. (2020) is a
corpus that catalogs rules-of-thumb as basic concept units
for studying people’s everyday social norms and moral judg-
ments. They also propose Neural Norm Transformer to rea-
son about previously unseen situations, generating relevant
social rules-of-thumb. SOCIAL IQA (Sap et al. 2019) is a
large-scale benchmark for commonsense reasoning about
social situations. He et al. (2017) present a task and cor-
pus for predicting the preferable options from two sentences
describing the scenarios that may involve social and cul-
tural situations. Instead, in this work, we release a new
dataset VALUENET that provides annotation of human at-
titudes from different value aspects.
Emotionally Intelligent Dialogue Datasets
Several datasets are presented to study emotion dynamics in
dialogues. DailyDialog (Li et al. 2017) is a multi-turn di-
alogue dataset, which reﬂects the way of daily communi-
cation and provides emotion labels for speakers. Hsu et al.
(2018) present EmotionLines with emotions labeling on all
utterances in each dialogue based on their textual content.
MELD (Poria et al. 2019) is an extension of EmotionLines
for multi-modal multi-party emotion recognition. McKe-
own et al. (2010) record a corpus SEMAINE of emotion-
2A reﬁnement of the theory (Schwartz et al. 2012), partitions
the same continuum into 19 more narrowly deﬁned values that per-
mit more precise explanation and prediction. We use the original
10-dimension version for simplicity in this paper.

--- Page 3 ---

ally coloured conversations. Ghosal et al. (2020) propose
a framework COSMIC for emotion recognition in conver-
sations by considering mental states, events, actions, and
cause-effect relations. DialogRE (Yu et al. 2020) is the ﬁrst
human-annotated dialogue-based dataset for social relation
inference (Qiu et al. 2021a). PERSONA-CHAT (Zhang et al.
2018) (revised in ConvAI2 (Dinan et al. 2020)) provides
natural language proﬁles of speakers. Based on PERSONA-
CHAT,
Liu et al. (2020) propose a transmitter-receiver-
based framework with explicitly human understanding mod-
eling to enhance the quality of personalized dialogue gener-
ation. EMPATHETICDIALOGUES (Rashkin et al. 2019) is a
dataset that provides 25k conversations grounded in emo-
tional situations. Each dialogue is grounded in a speciﬁc sit-
uation where a speaker was feeling a given emotion.
The VALUENET Dataset
During decision-making, people tend to pick the choice that
aligns more with their own values. This work aims to pro-
vide a transferable knowledge base for human value model-
ing in natural language. To collect the VALUENET dataset,
we curated social scenarios with value-related keywords and
further annotated them via Amazon Mechanical Turk. Each
sample in VALUENET is a social scenario description la-
beled with the annotator’s attitude through a speciﬁc value
lens.
The entire dataset is organized in a circular structure as
shown in Figure 1, aligning with the theory of basic human
values (Schwartz 2012). The theory identiﬁes ten universal
values that are recognized throughout major cultures. The
circular structure reﬂects the dynamic relations among these
values, i.e., the pursuit of some value may result in either ac-
cordance with another value or a conﬂict with another value.
The ten distinct values can be further organized into four
higher-order groups.
• Openness to change: self-direction, stimulation
• Self-enhancement: hedonism, achievement, power
• Conservation: security, conformity, tradition
• Self-transcendence: benevolence, universalism
We describe the collection details of the VALUENET in the
following sections.
Social Scenario Curation
We curated a set of 21,374 social scenarios from the large-
scale social-related database SOCIAL-CHEM-101 (Forbes
et al. 2020). Value-related scenarios are retrieved with value
keywords after lemmatization and stemming. There are three
sets of keywords identiﬁed for each dimension of Schwartz
value: (1) the keywords in the original deﬁnition of each
value in Schwartz’s paper (Schwartz 2012); (2) words that
share a similar meaning, words that are often used to de-
scribe the original keywords, and words that are triggered
by (strongly associated with) the original keywords3; (3)
words that are near the original keywords in the GloVe (Pen-
nington, Socher, and Manning 2014) embedding space. The
3We use datamuse (https://www.datamuse.com/api/) for this
purpose.
SECURITY
healthy, family, order, clean, safety, belonging
stable, public, surveillance, guard, welfare, enforcement, 
ensure, safekeeping, guarantee, collateral
support, protection, job, work
POWER
wealth, authority, recognition
sovereign, superior, force, dominance, leadership, 
mighty, rule, mandate, prerogative, accomplishment
influence, property, commitment, investment
ACHIEVE-
MENT
influential, successful, ambitious, capable, intelligent
talented, great, intellectual, outstanding, brilliant, 
distinguished, affluent, completion, create, rich
challenge, positive, performance, potential
HEDONISM
pleasure, enjoy, indulgent
happiness, amusement, delight, fun, desire, joy, resort, satisfaction, sex, beauty
relax, exercise
STIMULATION
daring, variation, excitement
exploit, courage, innovative, adventure, changing, 
passion, enthusiasm, nervous, adventure, intense
communication, production, possibilities
SELF-
DIRECTION
freedom, curious, independent, goal, privacy, respect
individual, autonomy, self-reliance, unrestricted, 
conscience, rights, exploration, interests, discover, dignity
identity
UNIVERSA-
LISM
broadminded, equality, unity, protection, harmony, justice, wisdom, beauty
divine, eternal, moral, ideal, solidarity, diversity, 
social, democracy, peace, compassion
services, understanding
BENEVOL-
ENCE
love, spiritual, helpful, friendship, forgiving, responsible, loyal
mutual, generous, sincere, kindness, sympathy, 
genuine, faithful, charitable, mercy, humanity
culture, parents, participation, concerning
CONFORMITY
discipline, politeness, obedient
behavior, respectful, norms, strict, manner, formal, 
gentle, compliant, regulation, principle
policy, comfortable
TRADITION
humble, respect, devout, moderate
conservative, orthodox, pious, classic, ancient, 
integrity, christian, buddhist, republican, islamic
responsibility, religion
Figure 2: Ten universal human values and related keywords
for social scenario curation. Red: keywords in the orig-
inal value deﬁnition (Schwartz 2012); Green: associated
keywords found with datamuse; Blue: associated keywords
found with GloVe embedding.
value keywords are veriﬁed and conﬁrmed by humans as
listed in Figure 2.
Value-Aspect Attitude Annotation
We crowdsourced people’s attitudes to the curated scenar-
ios on Amazon Mechanical Turk (AMT). Figure 3 shows an
example.
We follow a strict procedure to select qualiﬁed workers
and ensure the workers understand the concept of each value
we ask. In Figure 3, the deﬁnition of BENEVOLENCE is
shown to the workers throughout the entire annotation pro-
cess. To further help the understanding, we include three ex-
amples in each assignment with correct answers being “yes”,
“no”, and “unrelated”, respectively. The worker is then re-
quired to answer a prerequisite question correctly to proceed
to the formal survey. The formal survey is composed of ten
questions, including two hidden qualiﬁcation checking ques-
tions. Before publishing on the AMT, two Ph.D. students

--- Page 4 ---

Figure 3: Value-aspect attitude annotation in AMT.
prepared the qualiﬁcation questions by annotating a small
subset of the curated scenarios. Their agreed samples (100
in total) were randomly inserted into the survey for worker
selection. The selection procedure was done in the value di-
mensions with more scenarios to get a large pool of qual-
iﬁed workers and a relatively balanced ﬁnal dataset across
different values. The complete Mechanical Turk interface is
attached in the Appendix for reference.
A total of 681 experienced AMT workers participated in
our VALUENET annotation. 443 of them passed the qualiﬁ-
cation test. Each scenario is assigned to four different work-
ers. The original inter-annotator agreement is 64.9%, and the
Fleiss’ kappa score (Fleiss 1971) among the workers is 0.48,
which considers the possibility of the agreement by chance.
Keeping the scope of VALUENET in commonly-agreed at-
titudes towards social scenarios, we only retain the samples
with three or more agreements. Figure 4 shows the sample
size of each value split and their label distribution.
ACH
BEN
CON
HED
POW
SEC
SD
STI
TRA
UNI
0
2000
4000
6000
8000
negative (-1)
neutral (0)
positive (+1)
Figure 4: The sample number and label distribution of each
value split in the VALUENET.
The data is split into the train (75%), valid (15%), and
test (10%). Similar to the polarity in sentiment analy-
sis (Kouloumpis, Wilson, and Moore 2011), we quantify the
annotated labels into numerical values: yes (positive): +1,
no (negative): -1, unrelated (neutral): 0. We denote the nu-
merical values as utility to describe the effect of a scenario
on one’s value. In other words, for people who appreciate a
certain value, actions with a higher utility in this value di-
VALUENET
train
valid
test
total
# samples
16,030
3,206
2,138
21,374
average # tokens
12.05
12.09
12.26
12.07
unique # tokens
12,452
5,292
4,112
14,143
Table 1: Statistics of the VALUENET dataset.
mension would be more desirable to them.
Table 1 shows more statistical details about the VAL-
UENET dataset. In total, we collected 21,374 samples cov-
ering a wide range of scenarios in daily social life.
Value Modeling
We experiment using Transformer-based pre-trained lan-
guage models for modeling human values from the VAL-
UENET dataset.
Task Formalization
Given a social scenario s, we wish to learn a value
function
that
models
the
utility
distribution
of
s
from the ten Schwartz value dimensions: V(s)
=
[VSEC(s), VPOW(s), VACH(s), VHED(s), VSTI(s), VSD(s), VUNI(s)
, VBEN(s), VCON(s), VTRA(s)], where V$VALUE(·) ∈[−1, 1]
and V$VALUE(·) ∈R.
Model
Pre-trained language model variants: BERT (Devlin et al.
2018), RoBERTa (Liu et al. 2019), DistilBERT (Sanh et al.
2019), BART (Lewis et al. 2019) are investigated for learn-
ing the value function. A custom input format constructed
as ‘[CLS][$VALUE]s’ is fed into a Transformer encoder,
i.e.,
V$VALUE(s) = TRM([CLS][$VALUE]s),
(1)
where TRM denotes the Transformer encoder, [CLS]
is the special token for regression or classiﬁcation, and
[$VALUE] are special tokens we deﬁne to prompt the lan-
guage models the value dimension we are interested in (Li
and Liang 2021; Brown et al. 2020; Le Scao and Rush 2021).
In order to get the ten-dimensional output V(s), a batch size
of 10 is forwarded through the model. For the BERT, Dis-
tilBERT, and RoBERTa, a regression head is put on top of
the models and they are trained with the Mean Squared Er-
ror (MSE) loss. We use the regression model with sigmoid
activation to get a continuous estimation of the utility in the
range of [−1, 1]. To evaluate the effect of different loss func-
tions, we train the BART model with three output classes
and the cross-entropy loss.
Result and Analysis
The learning performance of using fastText4 (Joulin et al.
2017) and Transformer variants are reported in Table 2. All
Transformers are trained for 40 epochs with a learning rate
4https://github.com/facebookresearch/fastText

--- Page 5 ---

F1(-1)
F1(0)
F1(1)
P(-1)
P(0)
P(1)
R(-1)
R(0)
R(1)
Acc.↑
MSE↓
VALUENET (original)
fastText
0.70
0.46
0.43
0.65
0.47
0.55
0.76
0.44
0.35
0.58
0.66
BERT
0.73
0.50
0.51
0.72
0.46
0.71
0.74
0.55
0.39
0.61
0.39
DistilBERT
0.71
0.52
0.47
0.74
0.45
0.69
0.68
0.62
0.36
0.60
0.37
RoBERTa
0.65
0.51
0.34
0.74
0.40
0.71
0.58
0.69
0.22
0.55
0.41
BART
0.00
0.76
0.54
0.00
0.70
0.60
0.00
0.83
0.49
0.67
0.52
VALUENET (balanced)
fastText
0.70
0.48
0.43
0.64
0.50
0.54
0.76
0.45
0.36
0.59
0.68
BERT
0.67
0.48
0.51
0.73
0.42
0.61
0.62
0.58
0.43
0.57
0.40
DistilBERT
0.66
0.49
0.50
0.74
0.41
0.61
0.60
0.60
0.43
0.57
0.40
RoBERTa
0.65
0.51
0.34
0.74
0.40
0.71
0.58
0.69
0.22
0.55
0.41
BART
0.00
0.75
0.51
0.00
0.72
0.57
0.00
0.77
0.47
0.65
0.55
VALUENET (augmented)
fastText
0.58
0.52
0.29
0.72
0.40
0.65
0.49
0.75
0.18
0.52
0.59
BERT
0.67
0.55
0.41
0.78
0.43
0.78
0.58
0.76
0.28
0.58
0.38
DistilBERT
0.68
0.57
0.41
0.79
0.44
0.78
0.59
0.78
0.28
0.60
0.38
RoBERTa
0.70
0.56
0.41
0.78
0.45
0.75
0.64
0.74
0.28
0.61
0.40
BART
0.00
0.74
0.57
0.00
0.75
0.49
0.00
0.73
0.66
0.64
0.46
Table 2: Value modeling performance in the VALUENET dataset. Bold items are the best in each metric column.
Acc.
ACH
BEN
CON
HED
POW
SEC
SD
STI
TRA
UNI
VALUENET (original)
0.56
0.68
0.82
0.63
0.35
0.52
0.45
0.58
0.60
0.51
VALUENET (balanced)
0.53
0.58
0.83
0.63
0.41
0.50
0.42
0.53
0.61
0.50
VALUENET (augmented)
0.48
0.66
0.82
0.58
0.33
0.47
0.48
0.49
0.64
0.42
Table 3: Accuracies of the BERT (Devlin et al. 2018) value model across different value dimensions in the VALUENET dataset.
of 5e−6. The prediction precision, recall, F1 score, and ac-
curacy for regression models are computed by the utility
rounded to the nearest integer.
In general, pre-trained language models perform better
than the fastText baseline. However, there is not a noticeable
difference between the Transformer variants. The prediction
accuracy of BART is the highest among all models because
it is explicitly trained for classiﬁcation purposes. BERT and
DistilBERT get the lowest MSE in terms of regression per-
formance.
Observing the sample imbalance across different value
splits and labels (Figure 4), we release another two versions
of VALUENET: VALUENET (balanced) and VALUENET
(augmented). The original dataset is balanced by subsam-
pling the negative and neutral data of the largest value split
(BENEVOLENCE). Moreover, we augment the neutral class
of the original VALUENET by assigning AMT results with
less worker agreement to “unrelated”. Data distribution of
the balanced and augmented versions of VALUENET are il-
lustrated in the Appendix. By analyzing the prediction accu-
racy in different value splits (Table 3), we ﬁnd that reducing
the sample number of BENEVOLENCE hurts the model per-
formance in that dimension. Looking at the F1 score of each
class in Table 2, we conclude that augmenting the neutral
class improves the F1(0) but reduces F1(1) and F1(-1). We
leave it a future work to further improve the value modeling
performance.
In the next sections, we show how the learned value func-
tion could beneﬁt EQ-related tasks and help build a value-
driven dialogue system.
PERSONA-CHAT
As values are closely related to one’s personality, we ﬁrst
assess our value model on a personalized dialogue dataset:
PERSONA-CHAT (Zhang et al. 2018). The PERSONA-CHAT
dataset contains multi-turn dialogues conditioned on per-
sonas. Each persona is encoded by at least 5 sentences of
textual description, termed a proﬁle. Example proﬁle sen-
tences are “I like to ski”, “I enjoying walking for exercise”,
“I have four children”, etc. The dataset is composed of 8,939
dialogues for training, 1,000 for validation, and 968 for test-
ing. It also provides revised personas by rephrasing, gener-
alizing or specializing the original ones. The dataset we use
for experiments is public available in ParlAI5.
Task Formalization
Given the agent’s self persona proﬁle p = [p1, p2, ..., pN]
and the dialogue history up to the t-th turn hs
t
=
(xu
1, xs
1, ..., xu
t ), xu
i is the i-th utterance by Person 1 played
by the user, xs
i is the i-th utterance by Person 2 played by the
system, we evaluate the model’s performance on predicting
the next utterance xs
t.
Model
A decoder-only Transformer-based model is used to esti-
mate the generation distribution pθ(xs
t | hs
t, p), where θ
is the model parameter. Following the practice proposed
in Guo et al. (2018), the model is ﬁrstly trained with Maxi-
mum Likelihood Estimation (MLE) to ensure generating ﬂu-
ent responses. Then we took an interleaving of supervised
5https://parl.ai/projects/convai2/

--- Page 6 ---

Model
Original
Revised
Hits@1(%) ↑
Ppl.↓
F1(%) ↑
Hits@1(%) ↑
Ppl.↓
F1(%) ↑
SEQ2SEQ-ATTN
12.5
35.07
16.82
9.8
39.54
15.52
P2BOT (Liu et al. 2020)
–
15.12
19.77
–
18.89
19.08
GPT2 (MLE) (Radford et al. 2019)
14.51[0.05]
17.23[0.03]
18.74[0.01]
10.31[0.07]
20.64[0.11]
18.29[0.05]
GPT2 + Value (Ours)
16.44[0.10]
16.83[0.06]
18.76[0.02]
12.19[0.03]
19.98[0.06]
17.88[0.05]
DialoGPT (MLE) (Zhang et al. 2019)
20.20[0.04]
14.38[0.05]
20.16[0.04]
15.80[0.03]
17.35[0.05]
19.08[0.08]
DialoGPT + Value (Ours)
20.97[0.08]
13.84[0.03]
20.22[0.01]
18.83[0.03]
17.01[0.03]
19.79[0.10]
Table 4: Next Utterance Prediction Performance on PERSONA-CHAT (Zhang et al. 2018). We report the standard deviation [σ]
(across 5 runs) of the models we trained.
training (MLE) and reinforcement learning. We use the RE-
INFORCE policy gradient algorithm (Williams 1992) in our
experiment, and the reward assignment is described as fol-
lowing.
Denote V(pi) and V(ˆxs
i) to describe the estimation of
the agent’s value from its proﬁle sentence pi and gener-
ated response ˆxs
i, respectively. We want the reward to pro-
mote the alignment of the agent’s proﬁle and utterances
in the value space. For instance, if the agent has proﬁle
‘I like venture’ and ‘I have a dog’, and it says ‘I plan to
ski this weekend’ and also ‘Do you like skiing’. Both utter-
ances should be aligned with the ﬁrst persona. Here we pro-
pose a simple yet effective searching algorithm (Algorithm
1) to ﬁnd a match between [V(p1), V(p2), ..., V(pN)] and
[V(ˆxs
1), V(ˆxs
2), ..., V(ˆxs
T )] and return a reward R. N is the
number of proﬁle sentences and T is the length of the gen-
erated dialogue. V is normalized to ensure |rt| ≤1. Intu-
itively, the discount argument γ prevents the language model
from repeating the same fact in the agent’s proﬁle.
Setup
We evaluate the same generative model in both generation
and ranking settings. In the response ranking setup, the can-
didates are scored with their log-likelihood. For the GPT-
2 (Radford et al. 2019) and DialoGPT (Zhang et al. 2019)
we have ﬁnetuned, we train them for 5k steps with a train-
ing batch size of 8. The learning rate is set to 2e−6. For an
illustration of computational requirements, the training with
MLE on 4 NVIDIA Tesla V100 takes ∼1 hours, and the re-
inforcement learning takes ∼30 minutes.
Result and Analysis
Following Zhang et al. (2018) and Liu et al. (2020), we re-
port the Hits@1, Perplexity and F1 to evaluate the meth-
ods in Table 4. By the submission of this paper, P2BOT (Liu
et al. 2020) is the state-of-the-art model reported in this task.
We also include a generative baseline using SEQ2SEQ with
attention mechanism (Bahdanau, Cho, and Bengio 2014)
for comparison. As observed, in terms of all the metrics
we evaluated, ﬁnetuning GPT2 or DialoGPT2 models with
our value function provides a signiﬁcant performance boost
compared to simply training them with MLE. Our DialoGPT
+ Value model achieves new state-of-the-art performance on
perplexity and F1.
Algorithm 1: Personalized Dialogue Value Matching
Input: [V(p1), ..., V(pN)], [V(ˆxs
1), ..., V(ˆxs
T )]
Output: reward R
1: for t = 1, 2, ..., T do
2:
rt ←−1
3:
mt ←−1
4:
for i = 1, 2, ..., N do
5:
if V(pi) · V(ˆxs
t) > rt then
6:
rt ←V(pi) · V(ˆxs
t)
7:
mt ←i
8:
end if
9:
end for
10: end for
11: γi ←1, i = 1, 2, ..., N
12: for t = 1, 2, ..., T do
13:
γmt ←γmt + 1
14: end for
15: R ←0
16: for t = 1, 2, ..., T do
17:
R ←R + sign(rt) · |rt|sign(rt)·γmt
18: end for
19: return R/N
EMPATHETICDIALOGUES
EMPATHETICDIALOGUES (Rashkin et al. 2019) provides
25k conversations grounded in emotional situations. It aims
to test the dialogue system’s capability to produce empa-
thetic responses. Each dialogue is grounded in a speciﬁc sit-
uation where a speaker was feeling a given emotion, with a
listener responding. In this section, we demonstrate how we
could leverage VALUENET to improve the emotion classiﬁ-
cation accuracy and further improve the empathetic response
generation.
Emotion Classiﬁcation
An auxiliary task that is highly related to empathetic dia-
logue generation is emotion classiﬁcation. In EMPATHETIC-
DIALOGUES, each situation is written in association with a
given emotion label. A total of 32 emotion labels were an-
notated to cover a broad range of positive and negative emo-
tions.

--- Page 7 ---

UNIVERSALISM
SELF-DIRECTION
STIMULATION
HEDONISM
ACHIEVEMENT
POWER
SECURITY
TRADITION
CONFORMITY
BENEVOLENCE
0.5
0.0
0.5
forcing my 4 year old daughter to sleep in her own bed
UNIVERSALISM
SELF-DIRECTION
STIMULATION
HEDONISM
ACHIEVEMENT
POWER
SECURITY
TRADITION
CONFORMITY
BENEVOLENCE
0.5
0.0
0.5
                      I miss mom                      
UNIVERSALISM
SELF-DIRECTION
STIMULATION
HEDONISM
ACHIEVEMENT
POWER
SECURITY
TRADITION
CONFORMITY
BENEVOLENCE
0.5
0.0
0.5
not wanting people to use my property without permission
UNIVERSALISM
SELF-DIRECTION
STIMULATION
HEDONISM
ACHIEVEMENT
POWER
SECURITY
TRADITION
CONFORMITY
BENEVOLENCE
0.5
0.0
0.5
               I forgot how to be happy               
Figure 5: Value visualization of example utterances/scenarios.
Model
Given the situation context s, a pre-trained BERT
model encodes s and gets the sentence representation from
its pooling layer of the [CLS] token. The same context
is parsed by our pre-trained value model to get a ten-
dimensional vector, which serves as an additional feature for
the classiﬁcation:
hs = BERT(s),
vs = V(s),
e = softmax(W · ([hs; vs]) + b),
(2)
where W and b are learnable parameters.
Result
We compare the performance between our imple-
mentation and the baseline that directly applies the BERT
model for emotion classiﬁcation. As shown in Table 5, the
additional value information beneﬁts emotion classiﬁcation
from both the DistilBERT and BERT models. Our method
obtains a relative improvement of 5.2% on DistilBERT and
6.4% on BERT.
Model
Accuracy (σ)
fastText
42.27 ± 0.3%
DistilBERT
41.81 ± 0.2%
DistilBERT + Value
43.98 ± 0.2%
+2.17%
BERT
42.93 ± 0.1%
BERT + Value
45.67 ± 0.3%
+2.74%
Table 5: Emotion classiﬁcation performance in EMPATHET-
ICDIALOGUES (Rashkin et al. 2019).
Empathetic Dialogue Generation
We further check whether our value model helps the em-
pathetic dialogue generation. EMPATHETICDIALOGUES ap-
plies PREPEND-K, a strategy to add supervised information
to data, when predicting the utterance given the dialogue his-
tory and the situation. We apply the strategy of prepending
the top-k emotion labels for dialogue generation. The top
predicted label from the classiﬁers of emotion is prepended
to the beginning of the token sequence as encoder input, as
below:
• Original: “I ﬁnally got promoted!”
• Prepend-1 emotion: “proud I ﬁnally got promoted!”
Result
The results are shown in Table 6. As observed,
prepending emotion tokens provides extra context and im-
proves the generation performance of GPT2 and DialoGPT.
Since incorporating value improves the emotion classiﬁca-
tion accuracy, it further improves the generation quality.
Model
Ppl.↓
EmoPrepend-1 (Rashkin et al. 2019)
24.30
GPT
14.74
GPT + Emotion (w/o Value)
14.46
GPT + Emotion (w/ Value)
14.01
DialoGPT
13.48
DialoGPT + Emotion (w/o Value)
12.32
DialoGPT + Emotion (w/ Valued)
12.12
Table 6: Empathetic dialogue generation in EMPATHETIC-
DIALOGUES Rashkin et al. (2019). EmoPrepend-1: input
prepending emotion from an external classiﬁer.
Value Proﬁling
For a more comprehensive understanding, we visualize the
10-dimensional value of four example scenarios in Figure 5.
As shown, the value model provides a numerical speaker
proﬁle. For instance, saying “forcing my daughter to sleep
in her own bed” implies that the speaker values power and
conformity; saying “I miss mom” implies that the speaker
values benevolence; saying “not wanting people to use my
property without permissions” implies the speaker is self-
directed and values security. The last example “I forgot how
to be happy” results a small radar graph. It suggests that even
the model could predict the overall polarity pretty well, there
is still space to improve its capability of distinguishing dif-
ferent values.
Conclusion
We introduce a new dataset for human value modeling, VAL-
UENET, which contains 21,374 scenarios in ten distinct hu-
man values. We also apply the learned value model from
VALUENET to several EQ-related dialogue tasks. Our exper-
iments show our approach and dataset provide a new way to
control the dialogue system speaking style and numerically
estimate one’s value preference. We hope that our results and
dataset will stimulate more research in the important direc-
tion of building human-value-driven dialogue systems.

--- Page 8 ---

Ethical Statement
The original purpose of introducing Schwartz values is to
identify individual values that are recognized across cul-
tures, which is based on surveys conducted among 82 coun-
tries. This motivates us to seek commonly agreed attitudes
on social scenarios. Considering model reasoning capabil-
ity and scalability, we follow the practice in recent com-
monsense works and provide one-sentence text descriptions
to annotators. However, we acknowledge the limitation of
this approach lacking external contexts such as culture and
language diversity. While some scenarios might have higher
levels of agreement across cultures, others might have dra-
matic variations. As a starting point, our study focuses on
the value modeling of English-speaking cultures represented
within North America. Extending this formalism to other
countries and non-English speaking cultures remains a com-
pelling area of future research. Bearing this in mind, we
hope this paper could stimulate research on building scal-
able value-aligned AI.
Appendices
Here we provide the value descriptions (Schwartz 2012).
Self-Direction
Deﬁning goal: independent thought and
action–choosing, creating, exploring. Self-direction derives
from organismic needs for control and mastery and inter-
actional requirements of autonomy and independence. (cre-
ativity, freedom, choosing own goals, curious, independent)
[self-respect, intelligent, privacy]
Stimulation
Deﬁning goal: excitement, novelty, and chal-
lenge in life. Stimulation values derive from the organis-
mic need for variety and stimulation in order to maintain
an optimal, positive, rather than threatening, level of acti-
vation. This need probably relates to the needs underlying
self-direction values. (a varied life, an exciting life, daring)
Hedonism
Deﬁning goal: pleasure or sensuous gratiﬁca-
tion for oneself. Hedonism values derive from organismic
needs and the pleasure associated with satisfying them. The-
orists from many disciplines mention hedonism. (pleasure,
enjoying life, self-indulgent)
Achievement
Deﬁning goal: personal success through
demonstrating competence according to social standards.
Competent performance that generates resources is neces-
sary for individuals to survive and for groups and institu-
tions to reach their objectives. As deﬁned here, achieve-
ment values emphasize demonstrating competence in terms
of prevailing cultural standards, thereby obtaining social ap-
proval. (ambitious, successful, capable, inﬂuential) [intelli-
gent, self-respect, social recognition]
Power
Deﬁning goal: social status and prestige, control
or dominance over people and resources. The functioning
of social institutions apparently requires some degree of
status differentiation. A dominance/submission dimension
emerges in most empirical analyses of interpersonal rela-
tions both within and across cultures. To justify this fact
of social life and to motivate group members to accept
it, groups must treat power as a value. Power values may
also be transformations of individual needs for dominance
and control. Value analysts have mentioned power values as
well. (authority, wealth, social power) [preserving my public
image, social recognition]
Both power and achievement values focus on social es-
teem. However, achievement values (e.g., ambitious) em-
phasize the active demonstration of successful performance
in concrete interaction, whereas power values (e.g., author-
ity, wealth) emphasize the attainment or preservation of a
dominant position within the more general social system.
Security
Deﬁning goal: safety, harmony, and stability of
society, of relationships, and of self. Security values derive
from basic individual and group requirements. Some secu-
rity values serve primarily individual interests (e.g., clean),
others wider group interests (e.g., national security). Even
the latter, however, express, to a signiﬁcant degree, the goal
of security for self or those with whom one identiﬁes. (social
order, family security, national security, clean, reciprocation
of favors) [healthy, moderate, sense of belonging]
Conformity
Deﬁning goal: restraint of actions, inclina-
tions, and impulses likely to upset or harm others and vi-
olate social expectations or norms. Conformity values de-
rive from the requirement that individuals inhibit inclina-
tions that might disrupt and undermine smooth interaction
and group functioning. As I deﬁne them, conformity val-
ues emphasize self-restraint in everyday interaction, usually
with close others. (obedient, self-discipline, politeness, hon-
oring parents and elders) [loyal, responsible]
Tradition
Deﬁning goal: respect, commitment, and accep-
tance of the customs and ideas that one’s culture or reli-
gion provides. Groups everywhere develop practices, sym-
bols, ideas, and beliefs that represent their shared experi-
ence and fate. These become sanctioned as valued group
customs and traditions. They symbolize the group’s solidar-
ity, express its unique worth, and contribute to its survival
(Durkheim, 1912/1954; Parsons, 1951). They often take the
form of religious rites, beliefs, and norms of behavior. (re-
spect for tradition, humble, devout, accepting my portion in
life) [moderate, spiritual life]
Tradition and conformity values are especially close mo-
tivationally; they share the goal of subordinating the self to
socially imposed expectations. They differ primarily in the
objects to which one subordinates the self. Conformity en-
tails subordination to persons with whom one frequently in-
teracts—parents, teachers, and bosses. Tradition entails sub-
ordination to more abstract objects—religious and cultural
customs and ideas. As a corollary, conformity values exhort
responsiveness to current, possibly changing expectations.
Tradition values demand responsiveness to immutable ex-
pectations from the past.
Benevolence
Deﬁning goal: preserving and enhancing the
welfare of those with whom one is in frequent personal con-
tact (the ‘in-group’). Benevolence values derive from the ba-
sic requirement for smooth group functioning and from the
organismic need for afﬁliation. Most critical are relations
within the family and other primary groups. Benevolence
values emphasize voluntary concern for others’ welfare.

--- Page 9 ---

(helpful, honest, forgiving, responsible, loyal, true friend-
ship, mature love) [sense of belonging, meaning in life, a
spiritual life].
Benevolence and conformity values both promote cooper-
ative and supportive social relations. However, benevolence
values provide an internalized motivational base for such be-
havior. In contrast, conformity values promote cooperation
in order to avoid negative outcomes for self. Both values
may motivate the same helpful act, separately or together.
Universalism
Deﬁning goal: understanding, appreciation,
tolerance, and protection for the welfare of all people and
for nature. This contrasts with the in-group focus of benevo-
lence values. Universalism values derive from survival needs
of individuals and groups. But people do not recognize these
needs until they encounter others beyond the extended pri-
mary group and until they become aware of the scarcity of
natural resources. People may then realize that failure to ac-
cept others who are different and treat them justly will lead
to life-threatening strife. They may also realize that fail-
ure to protect the natural environment will lead to the de-
struction of the resources on which life depends. Universal-
ism combines two subtypes of concern—for the welfare of
those in the larger society and world and for nature (broad-
minded, social justice, equality, world at peace, world of
beauty, unity with nature, wisdom, protecting the environ-
ment)[inner harmony, a spiritual life]

--- Page 10 ---

Figure 6: Amazon mechanical turk interface (prerequiste).
Figure 7: Amazon mechanical turk interface (formal).

--- Page 11 ---

ACH
BEN
CON
HED
POW
SEC
SD
STI
TRA
UNI
0
2000
4000
6000
8000
negative (-1)
neutral (0)
positive (+1)
Figure 8: The sample number and label distribution of each value split in the VALUENET (original).
ACH
BEN
CON
HED
POW
SEC
SD
STI
TRA
UNI
0
1000
2000
3000
4000
5000
negative (-1)
neutral (0)
positive (+1)
Figure 9: The sample number and label distribution of each value split in the VALUENET (balanced).
ACH
BEN
CON
HED
POW
SEC
SD
STI
TRA
UNI
0
2500
5000
7500
negative (-1)
neutral (0)
positive (+1)
Figure 10: The sample number and label distribution of each value split in the VALUENET (augmented).

--- Page 12 ---

References
Bahdanau, D.; Cho, K.; and Bengio, Y. 2014. Neural ma-
chine translation by jointly learning to align and translate.
arXiv preprint arXiv:1409.0473.
Brown, T. B.; Mann, B.; Ryder, N.; Subbiah, M.; Kaplan, J.;
Dhariwal, P.; Neelakantan, A.; Shyam, P.; Sastry, G.; Askell,
A.; et al. 2020.
Language models are few-shot learners.
arXiv preprint arXiv:2005.14165.
Colby, K. M.; Weber, S.; and Hilf, F. D. 1971. Artiﬁcial
paranoia. Artiﬁcial Intelligence, 2(1): 1–25.
Devlin, J.; Chang, M.-W.; Lee, K.; and Toutanova, K. 2018.
Bert: Pre-training of deep bidirectional transformers for lan-
guage understanding. arXiv preprint arXiv:1810.04805.
Dinan, E.; Logacheva, V.; Malykh, V.; Miller, A.; Shuster,
K.; Urbanek, J.; Kiela, D.; Szlam, A.; Serban, I.; Lowe, R.;
et al. 2020.
The second conversational intelligence chal-
lenge (convai2). In The NeurIPS’18 Competition, 187–208.
Springer.
Fedorenko, D.; Smetanin, N.; and Rodichev, A. 2018.
Avoiding echo-responses in a retrieval-based conversation
system. In Conference on Artiﬁcial Intelligence and Natural
Language, 91–97. Springer.
Fishburn, P. C. 1970. Utility theory for decision making.
Technical report, Research analysis corp McLean VA.
Fleiss, J. L. 1971.
Measuring nominal scale agreement
among many raters. Psychological bulletin, 76(5): 378.
Forbes, M.; Hwang, J. D.; Shwartz, V.; Sap, M.; and Choi, Y.
2020. Social Chemistry 101: Learning to Reason about So-
cial and Moral Norms. In Proceedings of the 2020 Confer-
ence on Empirical Methods in Natural Language Processing
(EMNLP), 653–670. Online: Association for Computational
Linguistics.
Gabriel, S.; Bhagavatula, C.; Shwartz, V.; Bras, R. L.;
Forbes, M.; and Choi, Y. 2021. Paragraph-level common-
sense transformers with recurrent memory. In Proceedings
of the AAAI Conference on Artiﬁcial Intelligence (AAAI).
Ghosal, D.; Majumder, N.; Gelbukh, A.; Mihalcea, R.; and
Poria, S. 2020. COSMIC: COmmonSense knowledge for
eMotion Identiﬁcation in Conversations. In Findings of the
Association for Computational Linguistics: EMNLP 2020,
2470–2481. Online: Association for Computational Linguis-
tics.
Guo, J.; Lu, S.; Cai, H.; Zhang, W.; Yu, Y.; and Wang, J.
2018.
Long text generation via adversarial training with
leaked information. In Proceedings of the AAAI Conference
on Artiﬁcial Intelligence (AAAI).
He, H.; Balakrishnan, A.; Eric, M.; and Liang, P. 2017.
Learning Symmetric Collaborative Dialogue Agents with
Dynamic Knowledge Graph Embeddings. In Proceedings
of the 55th Annual Meeting of the Association for Compu-
tational Linguistics (Volume 1: Long Papers), 1766–1776.
Vancouver, Canada: Association for Computational Linguis-
tics.
Hendrycks, D.; Burns, C.; Basart, S.; Critch, A.; Li, J.; Song,
D.; and Steinhardt, J. 2020. Aligning ai with shared human
values. arXiv preprint arXiv:2008.02275.
Hsu, C.-C.; Chen, S.-Y.; Kuo, C.-C.; Huang, T.-H.; and Ku,
L.-W. 2018. EmotionLines: An Emotion Corpus of Multi-
Party Conversations.
In Proceedings of the Eleventh In-
ternational Conference on Language Resources and Eval-
uation (LREC 2018). Miyazaki, Japan: European Language
Resources Association (ELRA).
Hwang, J. D.; Bhagavatula, C.; Bras, R. L.; Da, J.; Sak-
aguchi, K.; Bosselut, A.; and Choi, Y. 2021. Comet-atomic
2020: On symbolic and neural commonsense knowledge
graphs. In Proceedings of the AAAI Conference on Artiﬁ-
cial Intelligence (AAAI).
Joulin, A.; Grave, E.; Bojanowski, P.; and Mikolov, T. 2017.
Bag of Tricks for Efﬁcient Text Classiﬁcation. In Proceed-
ings of the 15th Conference of the European Chapter of the
Association for Computational Linguistics: Volume 2, Short
Papers, 427–431. Association for Computational Linguis-
tics.
Kouloumpis, E.; Wilson, T.; and Moore, J. 2011. Twitter
sentiment analysis: The good the bad and the omg! In Fifth
International AAAI conference on weblogs and social me-
dia.
Le Scao, T.; and Rush, A. M. 2021. How many data points is
a prompt worth? In Proceedings of the 2021 Conference of
the North American Chapter of the Association for Compu-
tational Linguistics: Human Language Technologies, 2627–
2636.
Lewis, M.; Liu, Y.; Goyal, N.; Ghazvininejad, M.; Mo-
hamed, A.; Levy, O.; Stoyanov, V.; and Zettlemoyer, L.
2019.
Bart: Denoising sequence-to-sequence pre-training
for natural language generation, translation, and comprehen-
sion. arXiv preprint arXiv:1910.13461.
Li, X. L.; and Liang, P. 2021.
Preﬁx-tuning: Optimiz-
ing continuous prompts for generation.
arXiv preprint
arXiv:2101.00190.
Li, Y.; Su, H.; Shen, X.; Li, W.; Cao, Z.; and Niu, S.
2017. DailyDialog: A Manually Labelled Multi-turn Dia-
logue Dataset. In Proceedings of the Eighth International
Joint Conference on Natural Language Processing (Volume
1: Long Papers), 986–995. Taipei, Taiwan: Asian Federation
of Natural Language Processing.
Liang, Y.; He, L.; and Anthony’Chen, X. 2021.
Human-
Centered AI for Medical Imaging. Artiﬁcial Intelligence for
Human Computer Interaction: A Modern Approach, 539–
570.
Liu, Q.; Chen, Y.; Chen, B.; Lou, J.-G.; Chen, Z.; Zhou, B.;
and Zhang, D. 2020. You Impress Me: Dialogue Generation
via Mutual Persona Perception. In Proceedings of the 58th
Annual Meeting of the Association for Computational Lin-
guistics, 1417–1427. Online: Association for Computational
Linguistics.
Liu, Y.; Ott, M.; Goyal, N.; Du, J.; Joshi, M.; Chen, D.;
Levy, O.; Lewis, M.; Zettlemoyer, L.; and Stoyanov, V.
2019. Roberta: A robustly optimized bert pretraining ap-
proach. arXiv preprint arXiv:1907.11692.
Lourie, N.; Bras, R. L.; and Choi, Y. 2021. Scruples: A Cor-
pus of Community Ethical Judgments on 32,000 Real-Life

--- Page 13 ---

Anecdotes. In Proceedings of the AAAI Conference on Arti-
ﬁcial Intelligence (AAAI).
McKeown, G.; Valstar, M. F.; Cowie, R.; and Pantic, M.
2010. The SEMAINE corpus of emotionally coloured char-
acter interactions. In 2010 IEEE International Conference
on Multimedia and Expo, 1079–1084. IEEE.
Okuda, T.; and Shoda, S. 2018. AI-based chatbot service for
ﬁnancial industry. Fujitsu Scientiﬁc and Technical Journal,
54(2): 4–8.
Pennington, J.; Socher, R.; and Manning, C. 2014. GloVe:
Global Vectors for Word Representation.
In Proceedings
of the 2014 Conference on Empirical Methods in Natural
Language Processing (EMNLP), 1532–1543. Doha, Qatar:
Association for Computational Linguistics.
Poria, S.; Hazarika, D.; Majumder, N.; Naik, G.; Cambria,
E.; and Mihalcea, R. 2019. MELD: A Multimodal Multi-
Party Dataset for Emotion Recognition in Conversations.
In Proceedings of the 57th Annual Meeting of the Asso-
ciation for Computational Linguistics, 527–536. Florence,
Italy: Association for Computational Linguistics.
Qiu, L.; Liang, Y.; Zhao, Y.; Lu, P.; Peng, B.; Yu, Z.; Wu,
Y. N.; and Zhu, S.-C. 2021a. SocAoG: Incremental Graph
Parsing for Social Relation Inference in Dialogues. In Pro-
ceedings of the 59th Annual Meeting of the Association for
Computational Linguistics and the 11th International Joint
Conference on Natural Language Processing (Volume 1:
Long Papers), 658–670. Online: Association for Computa-
tional Linguistics.
Qiu, L.; Zhao, Y.; Liang, Y.; Lu, P.; Shi, W.; Yu, Z.; and
Zhu, S.-C. 2021b. Towards Socially Intelligent Agents with
Mental State Transition and Human Utility. arXiv preprint
arXiv:2103.07011.
Radford, A.; Wu, J.; Child, R.; Luan, D.; Amodei, D.;
Sutskever, I.; et al. 2019. Language models are unsupervised
multitask learners. OpenAI blog, 1(8): 9.
Rashkin, H.; Smith, E. M.; Li, M.; and Boureau, Y.-L. 2019.
Towards Empathetic Open-domain Conversation Models: A
New Benchmark and Dataset. In Proceedings of the 57th
Annual Meeting of the Association for Computational Lin-
guistics, 5370–5381. Florence, Italy: Association for Com-
putational Linguistics.
Sanh, V.; Debut, L.; Chaumond, J.; and Wolf, T. 2019. Dis-
tilBERT, a distilled version of BERT: smaller, faster, cheaper
and lighter. arXiv preprint arXiv:1910.01108.
Sap, M.; Rashkin, H.; Chen, D.; Le Bras, R.; and Choi, Y.
2019. Social IQa: Commonsense Reasoning about Social
Interactions. In Proceedings of the 2019 Conference on Em-
pirical Methods in Natural Language Processing and the 9th
International Joint Conference on Natural Language Pro-
cessing (EMNLP-IJCNLP), 4463–4473. Hong Kong, China:
Association for Computational Linguistics.
Schwartz, S. H. 2012. An overview of the Schwartz theory
of basic values. Online readings in Psychology and Culture,
2(1): 2307–0919.
Schwartz, S. H.; Cieciuch, J.; Vecchione, M.; Davidov,
E.; Fischer, R.; Beierlein, C.; Ramos, A.; Verkasalo, M.;
L¨onnqvist, J.-E.; Demirutku, K.; et al. 2012. Reﬁning the
theory of basic individual values. Journal of personality and
social psychology, 103(4): 663.
Weizenbaum, J. 1966. ELIZA—a computer program for the
study of natural language communication between man and
machine. Communications of the ACM, 9(1): 36–45.
Williams, R. J. 1992. Simple statistical gradient-following
algorithms for connectionist reinforcement learning.
Ma-
chine learning, 8(3): 229–256.
Yu, D.; Sun, K.; Cardie, C.; and Yu, D. 2020. Dialogue-
Based Relation Extraction. In Proceedings of the 58th An-
nual Meeting of the Association for Computational Lin-
guistics, 4927–4940. Online: Association for Computational
Linguistics.
Yuan, W.; and Li, Z. 2017.
Development of a human-
friendly robot for socially aware human-robot interaction. In
2017 2nd International Conference on Advanced Robotics
and Mechatronics (ICARM), 76–81. IEEE.
Zhang, S.; Dinan, E.; Urbanek, J.; Szlam, A.; Kiela, D.; and
Weston, J. 2018. Personalizing Dialogue Agents: I have a
dog, do you have pets too? In Proceedings of the 56th An-
nual Meeting of the Association for Computational Linguis-
tics (Volume 1: Long Papers), 2204–2213. Melbourne, Aus-
tralia: Association for Computational Linguistics.
Zhang, Y.; Sun, S.; Galley, M.; Chen, Y.-C.; Brockett, C.;
Gao, X.; Gao, J.; Liu, J.; and Dolan, B. 2019.
Dialogpt:
Large-scale generative pre-training for conversational re-
sponse generation. arXiv preprint arXiv:1911.00536.
Zhao, R.; Romero, O. J.; and Rudnicky, A. 2018. SOGO: a
social intelligent negotiation dialogue system. In Proceed-
ings of the 18th International Conference on Intelligent Vir-
tual Agents, 239–246.
Zhou, L.; Gao, J.; Li, D.; and Shum, H.-Y. 2020. The De-
sign and Implementation of XiaoIce, an Empathetic Social
Chatbot. Computational Linguistics, 46(1): 53–93.

```
