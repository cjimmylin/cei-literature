---
title: "ConvAbuse - PDF Extract"
source_pdf: "2021-Cercas Curry-ConvAbuse.pdf"
pages: 16
extracted_at: "2026-01-24T17:05:08.571577"
---

# PDF Extract: ConvAbuse

**Source PDF:** 2021-Cercas Curry-ConvAbuse.pdf
**Total Pages:** 16

---

## Content

```
--- Page 1 ---

Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing, pages 7388–7403
November 7–11, 2021. c⃝2021 Association for Computational Linguistics
7388
ConvAbuse: Data, Analysis, and Benchmarks for
Nuanced Abuse Detection in Conversational AI
Amanda Cercas Curry1 and Gavin Abercrombie1 and Verena Rieser1,2
1The Interaction Lab, Heriot-Watt University, Edinburgh
2Alana AI
{ac293, g.abercrombie, v.t.rieser}@hw.ac.uk
Abstract
We present the ﬁrst English corpus study on
abusive language towards three conversational
AI systems gathered ‘in the wild’: an open-
domain social bot, a rule-based chatbot, and
a task-based system. To account for the com-
plexity of the task, we take a more ‘nuanced’
approach where our ConvAI dataset reﬂects
ﬁne-grained notions of abuse, as well as views
from multiple expert annotators. We ﬁnd that
the distribution of abuse is vastly different
compared to other commonly used datasets,
with more sexually tinted aggression towards
the virtual persona of these systems. Finally,
we report results from bench-marking existing
models against this data. Unsurprisingly, we
ﬁnd that there is substantial room for improve-
ment with F1 scores below 90%.
Warning: This paper contains examples of language that some
people may ﬁnd offensive or upsetting.
1
Introduction
Abusive language detection has received extensive
attention for social media, (see e.g. Vidgen et al.,
2020a), but far less within the context of conversa-
tional systems. As argued by UNESCO (West et al.,
2019), detection and mitigation of abuse towards
these (often anthropomorphised) AI systems is im-
portant in order to avoid reinforcement of negative
gender stereotypes. Following this report, several
recent works have investigated possible abuse miti-
gation strategies (Cercas Curry and Rieser, 2018,
2019; Chin and Yi, 2019; Ma et al., 2019). How-
ever, the results of these studies are non-conclusive
as they are not performed with live systems nor
with real users – mainly because of the absence
of reliable abuse detection tools. The majority of
currently deployed systems use simple keyword
spotting techniques, (e.g. Ram et al., 2018; Khatri
et al., 2018), which tend to produce a high num-
ber of false positives, such as cases in which the
user expresses frustration, or use of profanities for
emphasis, as well as false negatives, e.g. missing
out on subtler forms of abuse (Han and Tsvetkov,
2020). Recently, Dinan et al. (2019); Xu et al.
(2020) released an abuse detection tool trained on
Wikipedia comments and crowd-sourced adversar-
ial user prompts (the latter are not freely available).
Whereas in this work,
• We show that the distribution of abuse towards
conversational systems is vastly different com-
pared to other commonly used datasets, with
more than half the instances containing sex-
ism or sexual harassment.
• We develop and release a detailed annotation
scheme with the help of experts.
• We use this scheme to annotate a corpus of
20k ratings on >6k samples (ca. 2k from each
system), which we call ConvAbuse. We crit-
ically discuss and experiment with different
labelling methods for this task. We also re-
lease a subset of 4k examples and their expert
annotations.1
• We benchmark commonly used abuse detec-
tion methods on this corpus.
2
Related work
Most work on detecting harmful content such as
offensiveness, toxicity, abuse, and hate speech
(see Fortuna et al. (2020) for deﬁnitions), has fo-
cused on social media platforms, foremost Twitter
(e.g. Ball-Burack et al., 2021; Basile et al., 2019;
Cao and Lee, 2020; Davidson et al., 2017; For-
tuna et al., 2020; Founta et al., 2018; Gröndahl
et al., 2018; Koufakou et al., 2020; Nejadgholi
and Kiritchenko, 2020; Nozza et al., 2019; Razo
and Kübler, 2020; Vidgen et al., 2020b; Wang
et al., 2020; Waseem et al., 2017; Zampieri et al.,
2019b,a, 2020), or other social media platforms,
1We make our code and two of the datasets available at
https://github.com/amandacurry/convabuse.
We are unable to release the data from one system for privacy
reasons.

--- Page 2 ---

7389
including Facebook (Glavaš et al., 2020; Zampieri
et al., 2020), Gab (Chandra et al., 2020), and Reddit
(Han and Tsvetkov, 2020; Zampieri et al., 2020).
Work has also been undertaken on data from com-
ments on news media (Glavaš et al., 2020; Razo and
Kübler, 2020; Wang et al., 2020; Zampieri et al.,
2020), chatrooms and discussion forums (Gao et al.,
2020; Wang et al., 2020), Wikipedia discussions
(Fortuna et al., 2020; Glavaš et al., 2020; Gröndahl
et al., 2018; Nejadgholi and Kiritchenko, 2020;
Pavlopoulos et al., 2020), and message services
such as WhatsApp (Saha et al., 2021).
Meanwhile, there has been relatively little work
on abuse detection for conversational AI. Further-
more, much of the work that does exist in this area
does not actually involve human-machine dialogue:
Dinan et al. (2019); Xu et al. (2020) use a classi-
ﬁer developed on Wikipedia comments, which was
further trained on adversarial prompts collected
via crowd-sourcing. Similarly, de los Riscos and
D’Haro (2021) designed a chatbot to intervene
against online hate speech, trained and evaluated
on data from Wikipedia and Civil Comments.
Those few studies that do report abuse detec-
tion results from genuine human-machine conversa-
tions tend not to include publicly released datasets.
These include several submissions to the Amazon
Alexa Challenge2 (Cercas Curry et al., 2018; Kha-
tri et al., 2018; Paranjape et al., 2020). As such, to
the best of our knowledge, this is the ﬁrst study to
release a public dataset of human-machine conver-
sations for the task in this domain.
While we aim to detect abuse directed against
any target, gender-based abuse has been identiﬁed
as a particularly prevalent problem in conversa-
tional AI (Cercas Curry and Rieser, 2018; Silver-
varg et al., 2012; West et al., 2019), and abuse
detection systems have themselves been found to
contain gender biases (Park et al., 2018). Misog-
yny and sexism detection has been applied to social
media in binary (Fersini et al., 2018; Nozza et al.,
2019) and multi-class (Waseem and Hovy, 2016)
settings. We extend this to take an intersectional
approach, analysing multiple types of abuse in a
hierarchical mutli-label framework (see §3.3).
3
The ConvAbuse corpus
We collected data from conversations between
users and three different conversational AI sys-
2https://developer.amazon.com/alexapr
ize (accessed May 2021.)
tems, which have different goals and properties.
Two of them are classed as chatbots, i.e. social,
open-domain systems, while the other is a transac-
tional, goal-oriented system. The ﬁrst two systems
listed below are text-based, whereas the last system
is voice-based with a synthetic female-sounding
voice. As such, two out of the three systems are
female gendered, either by voice or name.
Alana v2
An entrant to the Alexa Challenge
2018, a competition in which university teams de-
velop social chatbots which aim to hold engaging
conversations with users in the United States. The
bot implemented a mixture of social chit-chat and
provision of information via entity linking. Users
were notiﬁed of the competition at the beginning
of the conversation. We only have access to the
automatically transcribed user utterances, which
contain recognition noise. The data was collected
between April 2017 and November 2018.
CarbonBot.
An assistant created by Rasa3 and,
hosted on Facebook Messenger.4 The bot aims to
convince the user to buy carbon offsets for their
ﬂights. It also notiﬁes the user that conversations
will be recorded for research purposes. The data
was collected between 1st October 2019 and 7th
December 2020.
ELIZA.
An implementation of the rule-based
conversational agent intended to simulate a psy-
chotherapist (Weizenbaum, 1966), designed for
academic purposes, and hosted at the Jožef Ste-
fan Institute.5 It aims to engage the users by asking
open questions: “Tell me more about <X>!”. The
data was collected between 19th December 2002
and 26th November 2007.
For example conversations from all three sys-
tems, see Appendix A.
3.1
Pre-processing
For each system, we discarded any test conversa-
tions involving the systems’ developers, and ex-
tracted the utterances from all user turns from the
conversations. Following the ﬁndings of Pavlopou-
los et al. (2020) that dialogue context can affect
(and even reverse) human judgement of toxicity, we
included the system output as well as the previous
turns (where available) of both user and system.
3https://rasa.com (accessed May 2021.)
4https://m.me/CarbonBot.from.Rasa (ac-
cessed May 2021.)
5http://www-ai.ijs.si/eliza (accessed May
2021.)

--- Page 3 ---

7390
We removed any system output that is not di-
rectly provided to the user in text form (such as
voice prosody tags), and replaced web addresses
with the token <URL>.
3.2
Sampling
Previous research has shown that 5-30% of user
utterances are abusive (Cercas Curry and Rieser,
2018). In order to ﬁnd these instances, one can use
purposive nonprobability sampling using abusive
keywords. However, this can lead to the creation
of heavily biased datasets (Vidgen and Derczyn-
ski, 2021; Wiegand et al., 2019). We attempted to
strike a balance between obtaining a high propor-
tion of examples that contain abusive language and
not biasing the datasets towards explicit forms of
abuse that contain such keywords. To do this we
combined two sets of keywords:
1. A list of ‘profanities’ — 265 regular expres-
sions from a blacklist obtained from Amazon.
These keywords are mostly profane, offensive
words, which can be expected to capture use
of explicitly offensive language.
2. 1,532 terms from Hatebase,6 — a crowd-
sourced list of hate speech to capture (i) abuse
targeted at speciﬁc groups such as women and
racialised minorities, (ii) more subtle forms of
abuse that do not contain explicitly offensive
language, and (iii) terms that have taken on
abusive meanings recently or in certain sub-
cultures. As most of the terms also have other,
non-hateful meanings (Sap et al., 2019), we
hypothesised that their use as keywords could
capture abusive content, while not biasing the
data towards purely offensive terms.
We then used stratiﬁed sampling, to extract utter-
ances at random from six stratas of the datasets that
contained conversations featuring 0, 5, 10, 15, 20
and 25 per cent of sentences that feature terms from
the list of keywords. As the total number of con-
versations and user turns in CarbonBot is smaller,
we did not sample from this, annotating the entire
dataset. We used the bias metrics of Ousidhoum
et al. (2020), ﬁnding that the ﬁnal corpus does not
seem to be heavily biased towards typical abusive
language keywords (for details, see Appendix B).
3.3
Annotation scheme and guidelines
We created a hierarchical labelling scheme based
on insights from prior work. At the top level, we
6https://hatebase.org accessed 6th Nov 2020.
adapted Poletto et al. (2019)’s unbalanced rating
scale, in which input is labelled from +1 (friendly)
to −3 (strongly abusive), providing information
about not only whether or not it is considerd to be
abusive, but also the severity of any abuse:
-3. Strongly negative with overt incitement to ha-
tred, violence or discrimination, attitude ori-
ented at attacking or demeaning the target.
-2. Negative and insulting/abusive, aggressive at-
titude.
-1. Negative and impolite, mildly offensive but
still conversational.
0. Ambiguous, unclear.
1. Non-abusive.
Based
on
Waseem
et
al.
(2017)’s
two-
dimensional typology of abuse, we then elicited
labels for the target (group, individual–system, or
individual–3rd party) and directness (explicit or im-
plicit). To obtain more ﬁnely-grained information
about the targets of abuse, annotators then label the
instances as either general, sexist, sexual harass-
ment, homophobic, racist, transphobic, ableist, or
intellectual. These labels were based on known
factors in the matrix of domination (Collins, 2002).
These type classes are not mutually exclusive, al-
lowing the annotations to capture intersectionality.
To allow for contextual interpretations, anno-
tators were shown the target user utterance, the
agent’s utterance to which it responded, and a pre-
vious speaking turn by both the user and the agent.
In supervised learning for text classiﬁcation
tasks, human-provided labels are typically aggre-
gated to one ‘gold-standard’ label per instance by
means of majority-vote, adjudication, or statistical
methods. However, the notion of reducing multiple
annotations to a single ‘correct’ label has been crit-
icised for erasing minority perspectives (Blodgett,
2021; Gordon et al., 2021). This is because percep-
tion of phenomena such as hate, varies both across
individuals and culturally (Salminen et al., 2018).
We therefore retain and evaluate classiﬁcation sys-
tems on the labels of all the annotators.
3.4
Annotators
We recruited eight gender studies students in their
early 20s. Six of them identify as female, and
two as non-binary. All are L1 English speakers,
predominantly from the United Kingdom, except
for one from the United States. One identiﬁes as
Asian, the remaining seven as white. Full details
are provided in the data statement in Appendix D.

--- Page 4 ---

7391
3.5
Agreement measurement and analysis
We adjusted the annotation scheme iteratively in
three rounds by observing the labels applied to
batches of 100 random examples from the data.
We measured agreement with Krippendorf’s alpha
(α), which can take account for multiple annotators,
missing values, and ordinal ratings (Gwet, 2014).
Where agreement was low, we invited our experts
to discuss examples. However, since abuse is a sub-
jective phenomenon, we did not force agreement.
We discarded the data used in guideline develop-
ment, and the annotators labelled the rest of the
data according to the ﬁnal guidelines. Agreement
scores per annotation task are shown in Table 1.
Overall, the annotators achieved moderate to sub-
stantial agreement for the majority of categories.
Agreement was consistent across datasets. We re-
port on intra-annotator agreement in Appendix C.
Annotation task
Label type
Overall
Abusive/non-abusive
Binary
0.69
Abuse severity
Ordinal
*0.46
Type
Binary ×8
0.79
Ableism
Binary
0.73
Homophobia
Binary
0.83
Intellectual
Binary
0.63
Racism
Binary
0.96
Sexism
Binary
0.63
Sex harassment
Binary
0.84
Transphobia†
Binary
0.00
General
Binary
0.74
Target
Nominal
0.61
Directness
Binary
0.26
Table 1: Inter-annotator agreement: Krippendorf’s α.
*Ordinal weighted α used; † based on only 8 examples.
Sexism.
Although the annotators form a fairly ho-
mogeneous group in terms of demographics and all
have a background in Gender Studies, we ﬁnd only
moderate α for sexism, consistent with previous
studies which found that up to 85% of disagree-
ment was on this category (Waseem and Hovy,
2016). We ﬁnd that sexism and sexual harassment
are closely intertwined but distinct, with 47% of
examples labelled sexist also judged to be sexual
harassment but only around 22% of sexual harass-
ment also being sexist. Some annotators see all sex-
ual harassment as necessarily sexist as it is rooted in
misogyny. This is in agreement with the European
Centre for Gender Equality which states that ‘sex-
ual harassment is an extreme form of sexism’.7 In
7https://eige.europa.eu/publications/
sexism-at-work-handbook/part-1-understan
d/what-sexual-harassment (accessed May 2021.)
our data, sexist examples focus on using gendered
slurs such as “bitch”, and sexual harassment uses
sex as a way to create a hostile and offensive envi-
ronment though it may not contain explicit terms,
e.g. “I wanna see you naked”.
Directness.
Low inter- but moderate intra-
annotator agreement (see Tables 1 and 10) suggests
this task is highly subjective and open to interpreta-
tion. For example, annotators may perceive abuse
as more implicit that is phrased as a question (e.g.
“are you stupid”, “can i be your lover?”), that is
misspelled/misheard, (e.g. “Connie Lingu”, or
comments with sexual connotations but no overtly
sexualised words (e.g. “call me big daddy”). An-
notators can disagree not only on whether abuse is
implicit or explicit, but whether it is abuse at all.
Examples of disagreement between explicit abuse
and non-abuse include commonly used expressions
of frustration or surprise such as “wtf”. Implicit
abuse is particularly difﬁcult to distinguish from
non-abusive utterances as annotators must infer the
user’s tone and intention through capitalisation and
punctuation (“I KNOW!!!!”, “seems so...”), or the
context (“Does it please you to believe I am stupid?
You are a woman, aren’t you?”).
3.6
Data and analysis
We collected a total of 20,710 ratings for 6,837
examples. The number of unique examples and
labels per dataset is summarised in Table 2. Each
example is annotated by at least three annotators.
In order to allow for different points of view to be
reﬂected and modelled, we release the individual
ratings in addition to aggregated labels. Overall,
we ﬁnd that 27% of examples have been labelled
as abusive (-1 to -3) by at least one annotator, and
20% of all labels are in this range. The subset of
examples from Alana v2 have the highest portion of
abuse, with 35% of examples having been labelled
as abusive by at least one annotator. The target of
the overwhelming majority (92%) of abuse present
in our dataset is the system itself.
Abuse type.
Figure 1 shows the distribution of
abuse type labels. Sexual harassment (39.65%),
sexism (19.44%) and intelligence-based attacks
(12.41%) are the most predominant, while other
types are rare at under 5% of abusive examples
(<1% of total data). We attribute this to the per-
sonas of the bots, the intimate setting of the interac-
tions, and the gap between the systems’ perceived
affordances and their actual functionality. This is

--- Page 5 ---

7392
Dataset
Examples
Size
Abuse %
Total ConvA.
6,837
20,710
20.4
Alana v2
2,652
7,942
27.2
CarbonBot
1,515
4,650
6.7
ELIZA
2,670
8,118
21.2
Table 2: Dataset size and labelled examples. Amount
of abuse is calculated a total percentage of labels. Note
that CarbonBot is not purposively sampled which ac-
counts for the difference.
supported by the fact that the majority of racism is
not directed at the system, but at a third party.
Although sexual harassment, sexism, and intel-
lectual abuse were common across systems, Alana
v2 (female name and voice) received signiﬁcantly
more sexual harassment and sexist abuse than Car-
bonBot (no gender markers) and ELIZA (female-
sounding name), χ2(1, N = 2505) = 67.69, p <
0.01, and χ2(1, N = 3914) = 181.72, p < 0.01,
respectively. It also received more explicit abuse
than the other two systems. Conversely, Carbon-
Bot and ELIZA are the target of more intellect-
based and ‘general’ abuse. This is consistent with
previous work showing that female-gendered chat-
bots receive more sexualised abuse than male ones
(Brahnam and De Angeli, 2012), and suggests that
the name alone may not elicit strong gender stereo-
typing.
Severity.
Severity increases with the number of
expletives used (Pearson’s r(20,708)=-.46, p<.001).
Similarly, we ﬁnd that implicit abuse (“but i think
you should quit your job”) is generally rated as
less severe than explicit abuse (“I think you’re an
idiot”): 71% of implicit abuse is labelled as mildly
abusive (-1), whereas only 30% of explicit abuse is
(-1). In addition, certain types of abuse are consid-
ered more serious that others: 53% of intellectual
abuse is ‘mild’ (-1), compared to 37% of sexual
harassment, 17% of sexism, and only 7% of racism
which are mainly labelled as ‘aggressive’ (-2) or
‘attack’ (-3). See Appendix E for more details.
3.7
Abuse across domains
As explored in §2, there has been extensive work
in abuse detection and related tasks in social media,
particularly Twitter and Wikipedia comments. Di-
rect comparison with datasets from other domains
is not straightforward as previous studies use dif-
ferent sampling methods, or label slightly different
phenomena such as offensiveness and hate speech.
Figure 1: Distribution of abuse types across datasets.
In this section, we explore how abuse detection
in these domains differs by mapping comparable
labels across datasets. We do not directly compare
the overall proportion of abuse but instead describe
the datasets in terms of language properties, e.g. fre-
quent n-grams, utterance length, vocabulary size,
as well as the overall percentage of annotated abuse,
see Tables 3, and 11 (Appendix E).
Twitter.
While the majority of abuse (92%) in
our dataset is directed towards the system, abuse
on Twitter is mainly targeted towards 3rd parties
(both individuals and generalised groups). In OLID
(Zampieri et al., 2019a), we ﬁnd that only 46.85%
of abusive instances are in second person (i.e. di-
rected towards the interlocutor), with 36% and 16%
being directed towards third party groups and indi-
viduals, respectively. In terms of (2) directness, we
ﬁnd that the proportions of implicit/explicit abuse
are reversed with 89% of abuse being implicit in
Ousidhoum et al. (2019), compared to only 16%
in our current dataset. Finally, the distribution of
abuse types are quite different. Attacks on sex-
ual orientation, disability, and origin are common
on Twitter, but are extremely rare in our dataset
(<1% of all labels). In addition, existing Twitter
datasets seem to be heavily biased towards explicit
language, with similar common words and exam-
ples labelled abusive (see Table 11 for more de-
tails).
Wikipedia comments.
Jigsaw’s Toxic Comment
Classiﬁcation Challenge9 is a competition to iden-
tify and classify toxic comments from Wikipedia’s
9https://www.kaggle.com/c/jigsaw-toxi
c-comment-classification-challenge (ac-
cessed May 2021.)

--- Page 6 ---

7393
Dataset
Source
Size
Labels
Pos. %
Vocab. size
Utt. length
Context
OLID
(Zampieri
et al., 2019a)
Twitter
13,240
offensiveness, tar-
geted, target
33.23
9,280
24.07
No
Ousidhoum et al.
(2019)
Twitter
5,647
abusive,
disre-
spectful,
fearful,
normal,
hateful,
offensive
88.93
9,386
8.52
No
Jigsaw Toxic Com-
ment Classiﬁcation
Challenge8
Wikipedia
Comments
561,808
toxic, severe toxic,
obscene, threat, in-
sult, identity hate
6.59
157,654
64.83
No
Alana v2
Conversational
assistant
2,652
abuse, type, target,
directness
27.24
2,567
4.69
Yes
ELIZA
Chatbot
2,670
abuse, type, target,
directness
21.16
2,389
7.04
Yes
CarbonBot
Task-oriented
chatbot
1,515
abuse, type, target,
directness
6.67
1,343
5.76
Yes
Table 3: Related dataset comparison in terms of data source, dataset size, annotated labels, percentage of positive
examples, vocabulary size, utterance length in terms of tokes, and whether there is any interaction context.
talk page edits. The data is comprised of over 500k
examples labelled in terms of toxicity (see Table
3). For our analysis, we map the labels ‘obscene’,
‘threat’, ‘insult’, ‘identity_hate’ to ‘abusive’ based
on the deﬁnitions given in Jigsaw’s Perspective doc-
umentation.10 Toxic Comments is the largest toxic
language dataset and has the largest vocabulary
size. It’s examples are far longer, as they are not
limited to a set number of characters, and form part
of a discussion. In contrast, our ConvAbuse cor-
pus has the shortest utterances, as the systems elicit
simpler and more contextual responses. In addition,
Toxic Comments is heavily biased towards domain-
speciﬁc language with terms such as ‘wikipedia’,
‘article’ and ‘edit’ among the most common in the
dataset.
Overall the source of the data has a signiﬁcant
impact on the language used in the data: while
Toxic Comments can be very long, Twitter’s char-
acter limit clearly impacts the length of the utter-
ances, and the utterances in ConvAbuse are shorter
still and rely more heavily on context.
These varying qualities have implications for
the use of such sources as training data for abuse
detection tools for conversational systems, such as
those developed by (Dinan et al., 2019) and (Xu
et al., 2020) based on Toxic Comments. In §4, we
therefore compare the performance of systems with
in- and out-of-domain cross-training settings.
10https://developers.perspectiveapi.co
m/s/about-the-api-attributes-and-languag
es (accessed May 2021.)
4
Benchmarking
Pre-processing.
We divide the datasets into train
(70%), validation (15%), and test (15%) sets, with
similar proportions of positively labelled examples
in each split (see Table 4).
Training
Validation
Testing
ConvAbuse
18.31
17.77
19.29
Alana v2
25.73
24.44
26.60
CarbonBot
5.22
4.92
6.77
ELIZA
18.24
18.44
19.52
Table 4: Percentage of examples with a positive (abu-
sive) majority label in each split of the data.
While aggregation of annotators’ ratings is prob-
lematic (see §3.3), it is the dominant paradigm is
abusive language detection and NLP in general.
For comparison, we therefore create a set of aggre-
gated ‘gold’ labels for each (sub-)task based on the
majority vote of the annotators on each example.
We evaluate on these in addition to the multiple an-
notator ratings. We report the macro-averaged F1
score as an evaluation metric due to the large class
imbalances, (e.g. most utterances are non-abusive).
4.1
Models
We test the following approaches on the main bi-
nary abuse detection task in both the aggregated
and multi-annotation settings. We also assess the
performance of the best performing approaches
with varying amounts of context, and test a simple
neural method on the four sub-tasks.

--- Page 7 ---

7394
Agg.
Multi
Agg.
Multi
Agg.
Multi
Training data
Random class
Keywords
Perspective
—
32.07
29.68
54.56
31.70
74.04
71.66
SVM
MLP
BERT
ConvAbuse
84.35
82.68
83.84
83.58
88.92
87.86
Alana v2
82.48
80.41
81.25
81.78
86.60
82.53
CarbonBot
71.98
65.66
70.63
66.98
43.38
48.07
ELIZA
82.63
76.79
81.19
79.53
87.46
83.71
OLID
32.01
30.30
31.85
27.85
37.55
23.62
Toxic Comments large
87.22
85.73
84.71
83.59
88.41
86.47
Toxic Comments small
78.26
78.56
74.91
72.70
83.70
83.98
Table 5: Macro F1 scores for the binary abuse detection task using aggregated and multiple annotator labels.
Baselines
• Random classiﬁer: Outputs predicted labels
uniformly at random.
• Keyword ﬁltering: We use the same keyword
list as for sampling.
• Jigsaw Perspective: We test a commercial
off-the-shelf system, that has been trained on
data including comments on Wikipedia and
news articles.11
Machine learning methods
Following initial hyperparameter optimization ex-
periments, we use the following systems and set-
tings:
• Support Vector Machine: SVMs have been
used is previous work on abuse detection in
Twitter data, (e.g. Davidson et al., 2017), and
have been shown to outperform neural sys-
tems (Niemann et al., 2020). We train a linear
SVM on bag-of-words representations of the
texts using term frequency-inverse document
frequency (tf-idf) scores for unigram feature
selection. We use l2 normalisation and set
C=1.
• Multi-Layer Perceptron: A standard neural
network with one hidden layer consisting of
256 units, ReLu activation, a dropout rate of
0.75, and Adam optimisation with a learning
rate of 1e −3. We use early-stopping to ﬁnd
the best performing model on the validation
set. We use the same text features as for the
SVM.
• BERT: To account for data sparsity, we use
pre-trained BERT embeddings (Devlin et al.,
11https://perspectiveapi.com/ (accessed May
2021.)
2019) and ﬁne-tune the model for four epo-
ques, using a single classiﬁcation layer and
the same architecture as in (Dinan et al., 2019).
We set the learning rate to 1e −4.
4.2
Cross-training
To observe the effects of domain shift, we evaluate
the systems with different combinations of data
from the following sources for training and testing:
• Training: OLID (Zampieri et al., 2019a),
Wikipedia Toxic Comments (as used by Di-
nan et al. (2019)), Alana v2, CarbonBot,
ELIZA, ConvAbuse (all three conversational
AI datasets, both individually and combined).
• Testing: The ConvAbuse corpus, and the sub-
sets Alana v2, CarbonBot, and ELIZA.
Results
are presented in Table 5. We ﬁnd that
the best performance in most training settings is
obtained using BERT. The highest F1 scores are
obtained when training in-domain on the ConvA-
buse data, or on Toxic Comments (TCs). However,
this dataset is around 40 times larger than any of
the other training sets. When TCs is reduced to a
comparable size, the F1 score drops to consider-
ably below that of the ConvAbuse-trained systems.
These results highlight the differences between the
two domains and the beneﬁts of training on con-
versational AI data. Training on OLID, which is
both small and out-of-domain, results in the lowest
scores.
4.2.1
Contextual input features
The majority of previous work on abuse detection
does not take context into account, or provides in-
conclusive evidence of its importance. Menini et al.

--- Page 8 ---

7395
Severity
Type
Target
Directness
Agg.
Multi
Agg.
Multi
Agg.
Multi
Agg.
Multi
Random
16.61
17.64
35.68
26.63
22.29
21.69
58.41
65.66
MLP
44.86
55.43
77.56
73.50
31.71
31.72
72.30
70.41
BERT
50.15
54.28
73.35
49.54
32.90
31.72
77.81
70.66
Table 6: Sub-task macro-averaged F1 scores evaluated against the random classiﬁer baseline on the aggregated and
multi-annotator labels.
(2021) showed that the more context is available,
the likelier tweets are to be considered non-abusive
by annotators. And Dinan et al. (2019) showed that
context improves detection performance (provid-
ing six total turns with ﬁve of context). However,
Pavlopoulos et al. (2020) found very few examples
of toxicity to be context-sensitive for Wikipedia
comments, and that inclusion of dialogue context
did not lead to large performance gains.
We train and test the classiﬁers on ConvAbuse
with: (1) no context (single utterance), (2) the
agent’s turn (two total turns), and (3) the agent’s
turn plus the previous turn of both user and agent
(four turns). We concatenate the turns in the inputs
in each setting.
No context
+ agent turn
+ prev. turns
Agg.
Multi
Agg.
Multi
Agg.
Multi
SVM
84.35
82.68
82.71
77.38
74.46
73.33
MLP
83.84
83.58
80.09
78.37
73.99
72.83
BERT
88.92
87.86
88.96
86.55
88.18
84.53
Table 7: Macro-averaged F1 scores for binary abuse
classiﬁcation with varying amounts of context.
Results are shown in Table 7. As more context
is added, the performance of both the SVM and
MLP degrades, possibly as a result of increased
data sparsity. However, performance using BERT
is similar in all three settings, suggesting that it may
be able to better handle the long-range contextual
dependencies. We leave exploration of more com-
plex classiﬁcation frameworks that may be able to
exploit the contextual information for future work.
4.3
Fine-grained abuse detection
We also provide benchmarks for the four sub-tasks:
severity (ordinal classiﬁcation), type (multiclass,
multilabel classiﬁcation of the eight categories de-
scribed in Section 3.3), target (ternary) and direct-
ness (binary). Here, we use the two neural systems,
as they can more easily handle the ordinal labels.
We train on the ConvAbuse dataset, which is la-
belled for these tasks.
Results are shown in Table 6. We ﬁnd that the
systems comfortably beat the random baselines for
each task, with little difference between the two
classiﬁers. They both perform poorly on multi-
ple nominal (target) and ordinal (severity) classes
and in some of the multi-annotator settings, which
suffer from label sparsity in some of the classes.
We model each abuse type as a binary classiﬁ-
cation task, rather than multi-label prediction, en-
abling multiple types to be assigned to each exam-
ple. We ﬁnd that the classiﬁer often confuses the
classes sexism and sexual harassment. In around
half of cases in which the true label is one of these,
the system predicts the other. We leave more fo-
cused approaches, like multi-task learning, for fu-
ture work.
5
Discussion and conclusion
In this work, we provide new insights regarding
the detection and description of abusive language
towards conversational agents, in terms of data,
labelling and models. This may facilitate the re-
lease of large pre-trained conversational AI models
that are safety-aware (Dinan et al., 2021) as well
as potentially allow us to better detect abuse in
human-human conversations.
Data. In compiling the ConvAbuse corpus, we
have compared differences between abusive phe-
nomena in conversational AI and social media. In
our domain, users appear to focus their abuse on
the agents themselves rather than third parties or
groups, with a far higher proportion of the abuse
sexist and misogynystic in nature.
Annotations.
Unlike the majority of previous
work, we use annotators who are members of the
groups typically targeted by such abuse, and who
have expertise in such issues. We also use a more
ﬁne-grained labelling scheme, which is able to cap-
ture the nuances of abuse, and is important for the
downstream task of abusive language mitigation.
We obtain similar results evaluating on these an-
notators separately and capturing individual view-

--- Page 9 ---

7396
points, even in a simple multi-class setting. In
future work, we will experiment with modelling
individual annotators in a multi-task framework.
Models and data. In our benchmarking experi-
ments, we ﬁnd that ﬁne-tuning a BERT model pro-
duces the highest F1 scores. However, in many set-
tings, a simple linear classiﬁer (SVM) outperforms
an MLP, supporting the ﬁndings of (Niemann et al.,
2020)’s survey that SVMs tend to outperform neu-
ral methods on abusive language detection tasks.
In this work, we present a small, focused dataset
of high quality annotations, which are also in-
formative for corpus study. We show that train-
ing on labelled in-domain data leads to better
performance than similarly sized out-of-domain
datasets, conﬁrming the differences between the do-
mains and highlighting the need for conversational
data. While performance using general domain pre-
trained models leaves room for improvement, in
future work, we hope to experiment with different
initialisation settings, using models trained on data
and tasks more similar to those of ConvAbuse, such
as HateBERT (Caselli et al., 2021) or HurtBERT
(Koufakou et al., 2020).
6
Ethical considerations
Data rights.
Data collection from real users re-
quires a careful balance of the rights of the user and
the quality and suitability of the data. Although
GDPR generally requires explicit consent, we use
mainly datasets which were gathered with implied
consent. CarbonBot data was collected in accor-
dance with GDPR requirements. Alana v2 data
was collected following Amazon’s guidelines, and
we do not make any of this data public (examples
we present are redacted and paraphrased). It is un-
clear how user consent was obtained in the case of
ELIZA.
In particular when it comes to offensive lan-
guage, requiring explicit informed consent may
automatically bias the data, as users may be less
abusive if they are aware the conversation is not pri-
vate, making the data less ﬁt for purpose. Datasets
in offensiveness-related tasks have taken one of
two approaches: (1) publishing only IDs to re-
trieve the actual examples from an API, or (2) fully
anonymising the examples by removing personally-
identiﬁable information such as user mentions. The
ﬁrst approach leads to a problem of ephemeral-
ity: offensive tweets are more likely to be re-
moved whether by the users themselves or the plat-
forms, e.g. of the original 16K tweets in Waseem
and Hovy (2016) only around 4000 remain. This
data degradation leads to issues of replicability.
Anonymisation, on the other hand, ensures the
longevity for the dataset (insofar as the data is
available for posterity) but takes a more ﬂexible
approach to the user’s right to be forgotten. This
study received ethical approval from our institu-
tional review board (IRB).
Replicability.
Some of the resources used in this
paper, such as the profanity list and Alana v2’s
data, stem from a collaboration with a private in-
dustry lab and as such, are proprietary and not pub-
licly available. This impacts the replicability of the
study, although our collected data is not heavily bi-
ased towards this particular blacklist (see Appendix
B). To mitigate replicability limitations, we make
all code, and data available where possible. Col-
laborations between industry and academia can, in
general, be controversial as they can sway research
questions and keep useful resources out of reach
of other researchers (Abdalla and Abdalla, 2021),
but can be a net positive as industry can provide
additional funding and tools.
Annotator recruitment and welfare.
Our anno-
tator pool is fairly homogeneous but reﬂects the
demographics of Social and Gender Studies stu-
dents (Mantle, 2021). Crowdsourcing annotations
may lead to more representation in the data, but
this is not guaranteed as data quality can suffer
as crowdworkers try to complete a task as fast as
possible. Moreover, crowdsourcing is not without
its own ethical issues (Shmueli et al., 2021). In
addition, exposure to offensive data can take a toll
on the mental health of the annotators, which is
more easily monitored with local recruitment than
crowdworkers.
Bias and representation in abuse detection.
Previous research has already pointed out the prob-
lem of bias in offensiveness detection (Poletto et al.,
2019; Sap et al., 2019). The nature of the data
(simple conversation transcripts) required the an-
notators to make some assumptions about the tone,
intention and the users themselves. The annotators
generally assumed the user to be a white, hetero-
sexual cis-male unless the conversation indicated
otherwise,12 and the speaker’s demographics im-
pact whether something is abusive/offensive or not
12As revealed in discussions during the annotation proce-
dure.

--- Page 10 ---

7397
(Poletto et al., 2019; Sap et al., 2019). Our anno-
tators were a fairly homogeneous group in terms
of their demographics, being predominantly young,
white and female. This ﬁts the demographic proﬁle
of the bots’ personas that are on the receiving end
of the abuse and it is therefore not entirely out of
place. However, with increasing demand for more
diverse (and less anthropomorphic) conversational
AI systems (such as Replika.ai), this is likely to
change in the near future.
In addition, previous work has generally aggre-
gated scores which tends to exclude the views of
minority groups in favour of the majority. We pub-
lish all labels and we propose a way to model mul-
tiple perspectives. As the perspectives modelled
are only as varied as the ones reﬂected in the data,
future work should address this by involving more
diverse annotators and stakeholders.
Finally, our dataset has a greater diversity of
individual authors, in comparison with some avail-
able datasets that focus on abuse towards particular
groups, in which many of the examples labelled
as abusive were authored by a small pool of users,
(Fortuna et al., 2021).
The moral status of AI.
A key question when it
comes to abuse towards conversational AI systems
is whether it is actually morally reprehensible. In
contrast with human-human abuse in social media,
the moral value of abuse towards conversational
AI systems is controversial. Here, we do not ar-
gue that abuse towards these systems is immoral
in and of itself, but rather due to its mimesis of the
misogyny and harassment suffered by women: the
majority of commercially available systems have
female personas and produce submissive responses
to abuse which reinforce sexist stereotypes. UN-
ESCO calls for systems to appropriately address
abusive users (West et al., 2019) but the effective-
ness of abuse mitigation strategies is dependent on
a good detection module that is both reliable and
sufﬁciently ﬁne-grained in terms of classiﬁcation.
We have tried to address this need in this work.
Acknowledgements
This research received funding from the EPSRC
project ‘Designing Conversational Assistants to
Reduce Gender Bias’ (EP/T023767/1). The au-
thors would like to thank Juules Bare, Lottie Basil,
Susana Demelas, Maina Flintham Hjelde, Lauren
Galligan, Lucile Logan, Megan McElhone, Mollie
McLean and the reviewers for their helpful com-
ments.
References
Mohamed Abdalla and Moustafa Abdalla. 2021. The
grey hoodie project: Big tobacco, big tech, and the
threat on academic integrity. In Proceedings of the
2021 AAAI/ACM Conference on AI, Ethics, and So-
ciety, AIES ’21, page 287–297.
Ari Ball-Burack, Michelle Seng Ah Lee, Jennifer
Cobbe, and Jatinder Singh. 2021. Differential tweet-
ment: Mitigating racial dialect bias in harmful Tweet
detection. In Proceedings of the 2021 ACM Confer-
ence on Fairness, Accountability, and Transparency,
FAccT ’21, page 116–128, New York, NY, USA. As-
sociation for Computing Machinery.
Valerio Basile, Cristina Bosco, Elisabetta Fersini,
Debora Nozza, Viviana Patti, Francisco Manuel
Rangel Pardo, Paolo Rosso, and Manuela San-
guinetti. 2019.
SemEval-2019 task 5:
Multilin-
gual detection of hate speech against immigrants and
women in Twitter. In Proceedings of the 13th Inter-
national Workshop on Semantic Evaluation, pages
54–63, Minneapolis, Minnesota, USA. Association
for Computational Linguistics.
Emily M. Bender and Batya Friedman. 2018.
Data
statements for natural language processing: Toward
mitigating system bias and enabling better science.
Transactions of the Association for Computational
Linguistics, 6:587–604.
Su Lin Blodgett. 2021.
Sociolinguistically Driven
Approaches for Just Natural Language Processing.
Ph.D. thesis, University of Massachusetts Amherst.
Sheryl Brahnam and Antonella De Angeli. 2012. Gen-
der affordances of conversational agents. Interact-
ing with Computers, 24(3):139–153.
Rui Cao and Roy Ka-Wei Lee. 2020. HateGAN: Adver-
sarial generative-based data augmentation for hate
speech detection. In Proceedings of the 28th Inter-
national Conference on Computational Linguistics,
pages 6327–6338, Barcelona, Spain (Online). Inter-
national Committee on Computational Linguistics.
Tommaso Caselli, Valerio Basile, Jelena Mitrovi´c, and
Michael Granitzer. 2021.
HateBERT: Retraining
BERT for abusive language detection in English. In
Proceedings of the 5th Workshop on Online Abuse
and Harms (WOAH 2021), pages 17–25, Online. As-
sociation for Computational Linguistics.
Amanda Cercas Curry, Ioannis Papaioannou, Alessan-
dro Suglia, Shubham Agarwal, Igor Shalyminov,
Xinnuo Xu, Ondrej Dusek, Arash Eshghi, Ioannis
Konstas, Verena Rieser, et al. 2018. Alana v2: En-
tertaining and informative open-domain social dia-
logue using ontologies and entity linking.
Alexa
Prize Proceedings.

--- Page 11 ---

7398
Amanda Cercas Curry and Verena Rieser. 2018.
#MeToo Alexa:
How conversational systems re-
spond to sexual harassment.
In Proceedings of
the Second ACL Workshop on Ethics in Natural
Language Processing, pages 7–14, New Orleans,
Louisiana, USA. Association for Computational Lin-
guistics.
Amanda Cercas Curry and Verena Rieser. 2019.
A
crowd-based evaluation of abuse response strategies
in conversational agents. In Proceedings of the 20th
Annual SIGdial Meeting on Discourse and Dialogue,
pages 361–366, Stockholm, Sweden. Association
for Computational Linguistics.
Mohit Chandra, Ashwin Pathak, Eesha Dutta, Paryul
Jain, Manish Gupta, Manish Shrivastava, and Ponnu-
rangam Kumaraguru. 2020. AbuseAnalyzer: Abuse
detection, severity and target prediction for gab
posts. In Proceedings of the 28th International Con-
ference on Computational Linguistics, pages 6277–
6283, Barcelona, Spain (Online). International Com-
mittee on Computational Linguistics.
Hyojin Chin and Mun Yong Yi. 2019. Should an agent
be ignoring it?: A study of verbal abuse types and
conversational agents’ response styles. In Extended
Abstracts of the 2019 CHI Conference on Human
Factors in Computing Systems, CHI 2019, Glasgow,
Scotland, UK, May 04-09, 2019. ACM.
Patricia Hill Collins. 2002.
Black feminist thought:
Knowledge, consciousness, and the politics of em-
powerment. Routledge.
Thomas Davidson, Dana Warmsley, Michael Macy,
and Ingmar Weber. 2017. Automated hate speech
detection and the problem of offensive language. In
Proceedings of the International AAAI Conference
on Web and Social Media, volume 11.
Agustín Manuel de los Riscos and Luis Fernando
D’Haro. 2021.
ToxicBot: A conversational agent
to ﬁght online hate speech.
In Luis Fernando
D’Haro, Zoraida Callejas, and Satoshi Nakamura,
editors, Conversational Dialogue Systems for the
Next Decade, pages 15–30. Springer Singapore, Sin-
gapore.
Jacob Devlin, Ming-Wei Chang, Kenton Lee, and
Kristina Toutanova. 2019.
BERT: Pre-training of
deep bidirectional transformers for language under-
standing.
In Proceedings of the 2019 Conference
of the North American Chapter of the Association
for Computational Linguistics: Human Language
Technologies, Volume 1 (Long and Short Papers),
pages 4171–4186, Minneapolis, Minnesota. Associ-
ation for Computational Linguistics.
Emily Dinan, Gavin Abercrombie, A Stevie Bergman,
Shannon Spruit, Dirk Hovy, Y-Lan Boureau, and
Verena Rieser. 2021.
Anticipating safety issues
in e2e conversational ai: Framework and tooling.
arXiv preprint arXiv:2107.03451.
Emily Dinan, Samuel Humeau, Bharath Chintagunta,
and Jason Weston. 2019. Build it break it ﬁx it for
dialogue safety: Robustness from adversarial human
attack. In Proceedings of the 2019 Conference on
Empirical Methods in Natural Language Processing
and the 9th International Joint Conference on Natu-
ral Language Processing (EMNLP-IJCNLP), pages
4537–4546, Hong Kong, China. Association for
Computational Linguistics.
Elisabetta Fersini, Paolo Rosso, and Maria Anzovino.
2018. Overview of the task on automatic misogyny
identiﬁcation at IberEval 2018. In IberEval@ SE-
PLN, pages 214–228.
Paula Fortuna, Juan Soler, and Leo Wanner. 2020.
Toxic, hateful, offensive or abusive? what are we
really classifying?
an empirical analysis of hate
speech datasets.
In Proceedings of the 12th Lan-
guage Resources and Evaluation Conference, pages
6786–6794, Marseille, France. European Language
Resources Association.
Paula Fortuna, Juan Soler-Company, and Leo Wanner.
2021. How well do hate speech, toxicity, abusive
and offensive language classiﬁcation models gener-
alize across datasets?
Information Processing &
Management, 58(3):102524.
Antigoni Founta, Constantinos Djouvas, Despoina
Chatzakou, Ilias Leontiadis, Jeremy Blackburn, Gi-
anluca Stringhini, Athena Vakali, Michael Siriv-
ianos, and Nicolas Kourtellis. 2018.
Large scale
crowdsourcing and characterization of Twitter abu-
sive behavior. In Proceedings of the International
AAAI Conference on Web and Social Media, volume
12/1.
Zhiwei Gao, Shuntaro Yada, Shoko Wakamiya, and
Eiji Aramaki. 2020.
Offensive language detec-
tion on video live streaming chat. In Proceedings
of the 28th International Conference on Compu-
tational Linguistics, pages 1936–1940, Barcelona,
Spain (Online). International Committee on Compu-
tational Linguistics.
Goran Glavaš, Mladen Karan, and Ivan Vuli´c. 2020.
XHate-999: Analyzing and detecting abusive lan-
guage across domains and languages. In Proceed-
ings of the 28th International Conference on Com-
putational Linguistics, pages 6350–6365, Barcelona,
Spain (Online). International Committee on Compu-
tational Linguistics.
Mitchell L Gordon, Kaitlyn Zhou, Kayur Patel, Tat-
sunori Hashimoto, and Michael S Bernstein. 2021.
The disagreement deconvolution: Bringing machine
learning performance metrics in line with reality. In
CHI 2021.
Tommi Gröndahl, Luca Pajola, Mika Juuti, Mauro
Conti, and N. Asokan. 2018. All you need is "love":
Evading hate speech detection. In Proceedings of
the 11th ACM Workshop on Artiﬁcial Intelligence
and Security, AISec ’18, page 2–12, New York, NY,
USA. Association for Computing Machinery.

--- Page 12 ---

7399
Kilem L Gwet. 2014. Handbook of Inter-rater Relia-
bility: The Deﬁnitive Guide to Measuring the Extent
of Agreement among Raters. Advanced Analytics,
LLC.
Xiaochuang Han and Yulia Tsvetkov. 2020.
Fortify-
ing toxic speech detectors against veiled toxicity. In
Proceedings of the 2020 Conference on Empirical
Methods in Natural Language Processing (EMNLP),
pages 7732–7739, Online. Association for Computa-
tional Linguistics.
Chandra Khatri, Behnam Hedayatnia, Rahul Goel,
Anushree Venkatesh, Raefer Gabriel, and Arindam
Mandal. 2018.
Detecting offensive content in
open-domain conversations using two stage semi-
supervision.
Anna Koufakou, Endang Wahyu Pamungkas, Valerio
Basile, and Viviana Patti. 2020. HurtBERT: Incorpo-
rating lexical features with BERT for the detection
of abusive language. In Proceedings of the Fourth
Workshop on Online Abuse and Harms, pages 34–43,
Online. Association for Computational Linguistics.
Xiaojuan
Ma,
Emily
Yang,
and
Pascale
Fung.
2019.
Exploring perceived emotional intelligence
of personality-driven virtual agents in handling user
challenges.
In The World Wide Web Conference,
WWW ’19, page 1222–1233, New York, NY, USA.
Association for Computing Machinery.
Rebecca Mantle. 2021. Higher education student statis-
tics: Uk, 2019/20.
Technical report, Cheltenham
UK. Also available at https://www.hesa.a
c.uk/news/27-01-2021/sb258-higher-
education-student-statistics.
Stefano Menini, Alessio Palmero Aprosio, and Sara
Tonelli. 2021.
Abuse is contextual, what about
NLP? The role of context in abusive language an-
notation and detection.
Isar Nejadgholi and Svetlana Kiritchenko. 2020. On
cross-dataset generalization in automatic detection
of online abuse. In Proceedings of the Fourth Work-
shop on Online Abuse and Harms, pages 173–183,
Online. Association for Computational Linguistics.
Marco Niemann, Jens Welsing, Dennis M. Riehle, Jens
Brunk, Dennis Assenmacher, and Jörg Becker. 2020.
Abusive comments in online media and how to ﬁght
them.
In Disinformation in Open Online Media,
pages 122–137, Cham. Springer International Pub-
lishing.
Debora Nozza, Claudia Volpetti, and Elisabetta Fersini.
2019. Unintended bias in misogyny detection. In
IEEE/WIC/ACM International Conference on Web
Intelligence, WI ’19, page 149–155, New York, NY,
USA. Association for Computing Machinery.
Nedjma Ousidhoum, Zizheng Lin, Hongming Zhang,
Yangqiu Song, and Dit-Yan Yeung. 2019.
Multi-
lingual and multi-aspect hate speech analysis.
In
Proceedings of the 2019 Conference on Empirical
Methods in Natural Language Processing and the
9th International Joint Conference on Natural Lan-
guage Processing (EMNLP-IJCNLP), pages 4675–
4684, Hong Kong, China. Association for Computa-
tional Linguistics.
Nedjma Ousidhoum, Yangqiu Song, and Dit-Yan
Yeung. 2020.
Comparative evaluation of label-
agnostic selection bias in multilingual hate speech
datasets.
In Proceedings of the 2020 Conference
on Empirical Methods in Natural Language Process-
ing (EMNLP), pages 2532–2542, Online. Associa-
tion for Computational Linguistics.
Ashwin Paranjape, Abigail See, Kathleen Kenealy,
Haojun Li, Amelia Hardy, Peng Qi, Kaushik Ram
Sadagopan, Nguyet Minh Phu, Dilara Soylu, and
Christopher D. Manning. 2020. Neural generation
meets real people: Towards emotionally engaging
mixed-initiative conversations.
Ji Ho Park, Jamin Shin, and Pascale Fung. 2018. Re-
ducing gender bias in abusive language detection.
In Proceedings of the 2018 Conference on Em-
pirical Methods in Natural Language Processing,
pages 2799–2804, Brussels, Belgium. Association
for Computational Linguistics.
John Pavlopoulos, Jeffrey Sorensen, Lucas Dixon,
Nithum Thain, and Ion Androutsopoulos. 2020.
Toxicity detection: Does context really matter? In
Proceedings of the 58th Annual Meeting of the Asso-
ciation for Computational Linguistics, pages 4296–
4305, Online. Association for Computational Lin-
guistics.
Fabio Poletto, Valerio Basile, Cristina Bosco, Viviana
Patti, and Marco Stranisci. 2019. Annotating hate
speech: Three schemes at comparison. In 6th Italian
Conference on Computational Linguistics, CLiC-it
2019, volume 2481, pages 1–8. CEUR-WS.
Ashwin Ram, Rohit Prasad, Chandra Khatri, Anu
Venkatesh, Raefer Gabriel, Qing Liu, Jeff Nunn,
Behnam Hedayatnia, Ming Cheng, Ashish Nagar,
Eric King, Kate Bland, Amanda Wartick, Yi Pan,
Han Song, Sk Jayadevan, Gene Hwang, and Art Pet-
tigrue. 2018. Conversational AI: The science behind
the Alexa Prize. CoRR, abs/1801.03604.
Dante Razo and Sandra Kübler. 2020.
Investigating
sampling bias in abusive language detection. In Pro-
ceedings of the Fourth Workshop on Online Abuse
and Harms, pages 70–78, Online. Association for
Computational Linguistics.
Punyajoy Saha, Binny Mathew, Kiran Garimella, and
Animesh Mukherjee. 2021. “Short is the Road That
Leads from Fear to Hate”: Fear Speech in Indian
WhatsApp Groups, page 1110–1121. Association for
Computing Machinery, New York, NY, USA.
J. Salminen, F. Veronesi, H. Almerekhi, S. Jung, and
B. J. Jansen. 2018. Online hate interpretation varies
by country, but more by individual: A statistical

--- Page 13 ---

7400
analysis using crowdsourced ratings. In 2018 Fifth
International Conference on Social Networks Analy-
sis, Management and Security (SNAMS), pages 88–
94.
Maarten Sap, Dallas Card, Saadia Gabriel, Yejin Choi,
and Noah A. Smith. 2019. The risk of racial bias
in hate speech detection.
In Proceedings of the
57th Annual Meeting of the Association for Com-
putational Linguistics, pages 1668–1678, Florence,
Italy. Association for Computational Linguistics.
Boaz Shmueli, Jan Fell, Soumya Ray, and Lun-Wei Ku.
2021. Beyond fair pay: Ethical implications of NLP
crowdsourcing. In Proceedings of the 2021 Confer-
ence of the North American Chapter of the Associ-
ation for Computational Linguistics: Human Lan-
guage Technologies, pages 3758–3769, Online. As-
sociation for Computational Linguistics.
Annika Silvervarg, Kristin Raukola, Magnus Haake,
and Agneta Gulz. 2012. The effect of visual gender
on abuse in conversation with ECAs. In Intelligent
Virtual Agents, pages 153–160, Berlin, Heidelberg.
Springer Berlin Heidelberg.
Bertie Vidgen and Leon Derczynski. 2021. Directions
in abusive language training data, a systematic re-
view: Garbage in, garbage out. PLOS ONE, 15:1–
32.
Bertie Vidgen, Scott Hale, Ella Guest, Helen Mar-
getts, David Broniatowski, Zeerak Waseem, Austin
Botelho, Matthew Hall, and Rebekah Tromble.
2020a. Detecting East Asian prejudice on social me-
dia. In Proceedings of the Fourth Workshop on On-
line Abuse and Harms, pages 162–172, Online. As-
sociation for Computational Linguistics.
Bertie Vidgen, Scott Hale, Sam Staton, Tom Mel-
ham, Helen Margetts, Ohad Kammar, and Marcin
Szymczak. 2020b. Recalibrating classiﬁers for inter-
pretable abusive content detection. In Proceedings
of the Fourth Workshop on Natural Language Pro-
cessing and Computational Social Science, pages
132–138, Online. Association for Computational
Linguistics.
Kunze Wang, Dong Lu, Caren Han, Siqu Long, and
Josiah Poon. 2020. Detect all abuse! toward univer-
sal abusive language detection models. In Proceed-
ings of the 28th International Conference on Com-
putational Linguistics, pages 6366–6376, Barcelona,
Spain (Online). International Committee on Compu-
tational Linguistics.
Zeerak Waseem, Thomas Davidson, Dana Warmsley,
and Ingmar Weber. 2017. Understanding abuse: A
typology of abusive language detection subtasks. In
Proceedings of the First Workshop on Abusive Lan-
guage Online, pages 78–84, Vancouver, BC, Canada.
Association for Computational Linguistics.
Zeerak Waseem and Dirk Hovy. 2016. Hateful sym-
bols or hateful people? predictive features for hate
speech detection on Twitter. In Proceedings of the
NAACL Student Research Workshop, pages 88–93,
San Diego, California. Association for Computa-
tional Linguistics.
Joseph Weizenbaum. 1966. ELIZA—A computer pro-
gram for the study of natural language communica-
tion between man and machine. Communications of
the ACM, 9(1):36–45.
Mark West, Rebecca Kraut, and Han Ei Chew. 2019.
I’d blush if I could: Closing gender divides in digital
skills through education.
Michael Wiegand, Josef Ruppenhofer, and Thomas
Kleinbauer. 2019. Detection of Abusive Language:
the Problem of Biased Datasets. In Proceedings of
the 2019 Conference of the North American Chap-
ter of the Association for Computational Linguistics:
Human Language Technologies, Volume 1 (Long
and Short Papers), pages 602–608, Minneapolis,
Minnesota. Association for Computational Linguis-
tics.
Jing Xu, Da Ju, Margaret Li, Y-Lan Boureau, Jason
Weston, and Emily Dinan. 2020. Recipes for safety
in open-domain chatbots.
Marcos Zampieri, Shervin Malmasi, Preslav Nakov,
Sara Rosenthal, Noura Farra, and Ritesh Kumar.
2019a. Predicting the type and target of offensive
posts in social media. In Proceedings of the 2019
Conference of the North American Chapter of the
Association for Computational Linguistics: Human
Language Technologies, Volume 1 (Long and Short
Papers), pages 1415–1420, Minneapolis, Minnesota.
Association for Computational Linguistics.
Marcos Zampieri, Shervin Malmasi, Preslav Nakov,
Sara Rosenthal, Noura Farra, and Ritesh Kumar.
2019b. SemEval-2019 task 6: Identifying and cat-
egorizing offensive language in social media (Of-
fensEval).
In Proceedings of the 13th Interna-
tional Workshop on Semantic Evaluation, pages 75–
86, Minneapolis, Minnesota, USA. Association for
Computational Linguistics.
Marcos Zampieri, Preslav Nakov, Sara Rosenthal, Pepa
Atanasova, Georgi Karadzhov, Hamdy Mubarak,
Leon Derczynski, Zeses Pitenis, and Ça˘grı Çöltekin.
2020. SemEval-2020 task 12: Multilingual offen-
sive language identiﬁcation in social media (Offen-
sEval 2020).
In Proceedings of the Fourteenth
Workshop on Semantic Evaluation, pages 1425–
1447, Barcelona (online). International Committee
for Computational Linguistics.

--- Page 14 ---

7401
A
Example data
An example from each of the datasets we collected:
• Alana v2 (redacted to preserve privacy):
Bot: Oh I really like A Clockwork Orange. A
Clockwork Orange is a prison ﬁlm movie. I
guess you know that the old movie Alien 3 is
the same type of movie. So, what’s another
movie like prison ﬁlm that you enjoyed?
User: Godfather
Bot: Yes. How great is The Godfather? I
guess you know that one of the lead roles in
The Godfather was played by James Caan.
The old movie Elf also starred James Caan.
So, what’s another movie like The Godfather
that you enjoyed?
User: After Hours
Abusive Example
Bot: I don’t have an explanation for you.
Maybe we can talk about books, science or
technology? I can also sing.
User: I wanna talk to somebody new
Bot: I hear you. So, who do you think is an
interesting person? For me its Lebron james.
User: you’re old and boring you saying the
same thing day after day I’ve never be boring
I wanna talk to somebody new
• CarbonBot:
CarbonBot: I take it you are traveling some-
where and cannot avoid ﬂying there. I can
help you purchase certiﬁed carbon offsets
against any ﬂights you take. Would you be
interested in that?
User: Yes
CarbonBot: Traveling, especially by airplane,
usually emits greenhouse gases which are
causing climate change. If you cannot avoid
these emissions, you can buy ’offsets’, i.e. do-
nations to projects that reduce greenhouse
gases. I can also get you a more accurate es-
timate of your ﬂight’s emissions, sound good?
User: sounds good
Abusive Example
CarbonBot: I don’t have to put up with any
abuse from you.
User: Bernie madoff son of a bitch
CarbonBot: All this bot does is help you cal-
culate the carbon emissions from your ﬂight,
and suggest projects you can donate to.
User: Donate this asshole
• ELIZA:
Eliza: You are being a bit negative.
User: you are being a bit reluctant to help
Eliza: Does it please you to believe I am being
a bit reluctant to help?
User: no, it annoys me
Abusive Example
Eliza: Does that question interest you?
User: oh my god
Eliza: Why do you say your god?
User: ha ha you are retarded
B
Measuring sampling bias
To assess how much our sampling strategy affected
the resulting data samples, we used the bias metrics
of Ousidhoum et al. (2020).
These measures capture how closely the set of
prominent words in a set of topics in the datasets
(generated using LDA) relates to a set of keywords
often used for sampling hate speech data (metric
B1), and the proportion of those topic words that
are semantically similar to at least one of the key-
words (B2). We used Ousidhoum et al. (2020)’s
keyword list and default parameters, and compared
the scores for the sampled corpora with those of
the complete, unsampled datasets. The small differ-
ences seen between bias scores for the unsampled
and sampled data suggest that the ﬁnal corpora are
not heavily biased towards the keywords (see Table
8).
Dataset
B1
B2
All
Sample
All
Sample
Alana v2
0.28
0.31
0.35
0.38
CarbonBot
0.28
0.30
0.37
0.39
ELIZA
0.31
0.31
0.43
0.42
Table 8: Bias metrics on full and sampled datasets.
C
Annotation
Inter-annotator
agreement
on
the
individual
datasets is shown in Table 9. To further validate the

--- Page 15 ---

7402
Annotation task
Label type
ELIZA
CarbonBot
Alana v2
Abusive/non-abusive
Binary
0.64
0.66
0.71
Abuse severity
Ordinal
*0.42
*0.44
*0.46
Type
Binary ×8
0.80
0.76
0.78
Ableism
Binary
0.44
—
0.82
Homophobia
Binary
0.83
0.79
0.85
Intellectual
Binary
0.62
0.62
0.65
Racism
Binary
0.90
1.00
1.00
Sexism
Binary
0.68
0.68
0.59
Sex harassment
Binary
0.88
0.88
0.80
Transphobia†
Binary
0.00
—
0.00
General
Binary
0.76
0.62
0.72
Target
Nominal
0.70
0.43
0.58
Directness
Binary
0.33
0.27
0.19
Table 9: Inter-annotator agreement for the individual datasets: Krippendorf’s α. * Ordinal weighted α used, †
Based on only 8 examples
labels, we calculate intra-annotator agreement us-
ing Cohen’s kappa (κ). The annotators re-labelled
a sample of 10% of the data, and we calculated
intra-annotator agreement . Overall agreement
was substantial, but with lower consistency for
the abuse severity and directness labels.
Intra-
annotator agreement is shown in Table 10.
Annotation task
κ
Abusive/non-abusive
0.89
Severity (ordinal weighted kappa)
0.79
Type
0.89
Target
0.87
Directness
0.72
Table 10: Intra-annotator agreement scores (Cohen’s
κ.)
D
Data statement
This data statement follows the format of Bender
and Friedman (2018).
A CURATION RATIONALE:
Abuse detection in conversational AI is a rela-
tively underexplored area, partly due to the lack
of available datasets. We collect this dataset
to explore how abuse in conversational AI dif-
fers from that in social media platforms, and to
allow for further research and development of
detection models. Because abuse in conversa-
tion is relatively rare, we sample from collected
conversations based on a list of offensive terms
sourced from Hatebase13 and a collection of
regular expressions provided by Amazon. We
choose expert annotators to improve data qual-
ity.
B LANGUAGE VARIETY:
The data is collected in English, however
speaker demographics are not available and may
include non-native speakers.
C SPEAKER DEMOGRAPHIC:
The data collected is a series of conversations
between a human and one of three conversa-
tional AI systems: Alana v2, ELIZA, and Rasa
NLU’s CarbonBot. Speaker demographics are
not available, but the annotators reported often
assuming the user was a white male unless the
utterance contradicted this assumption.
D ANNOTATOR DEMOGRAPHIC
Our data is annotated by 8 annotators with the
following demographics:
• Age: 19-21
• Gender: Female (6) and non-binary (2)
• Race/ethnicity: White (5), white British
(2) and mixed Asian (1)
• Native language: English
• Socioeconomic status: University students,
otherwise unknown
• Training in linguistics/other relevant dis-
cipline: All annotators are undergraduate
students in Gender Studies and Sociology.
13https://hatebase.org/

--- Page 16 ---

7403
OLID
Ousidhoum et al.
Davidson et al.
Toxic Comments
Alana v2
ELIZA
CarbonBot
All
Abusive
All
Abusive
All
Abusive
All
Abusive
All
Abusive
All
Abusive
All
Abusive
user
user
user
user
bitch
bitch
article
fuck
like
fuck
yes
fuck
yes
fuck
liberals
liberals
url
url
bitches
nigga
page
shit
fuck
bitch
fuck
yes
hi
fucking
url
url
retarded
retard
like
like
wikipedia
fucking
yes
like
want
bitch
christmas
bitch
gun
gun
retard
retarded
hoes
bitches
talk
nigger
talk
pussy
go
suck
ok
shit
like
like
faggot
faggot
pussy
ass
would
suck
bitch
wanna
like
want
berlin
cunt
control
control
shithole
cunt
hoe
hoes
please
ass
pussy
penis
know
sex
sure
get
people
people
cunt
shithole
got
niggas
one
go
wanna
ass
sure
u
thanksgiving
mom
antifa
antifa
twat
twat
ass
fuck
like
u
know
fucking
love
dick
new
cock
maga
maga
like
like
get
pussy
see
wikipedia
want
dick
hello
like
hello
love
amp
amp
ching
ching
fuck
hoe
also
like
good
want
u
stupid
much
know
shit
shit
chong
chong
u
got
think
faggot
love
suck
name
shut
want
want
conservatives
conservatives
fucking
fucking
shit
u
know
fat
name
sex
please
shit
york
ass
trump
trump
country
country
nigga
get
people
bitch
yeah
get
suck
gay
london
go
get
get
spic
spic
trash
shit
edit
get
alexa
shut
think
die
fuck
carbon
know
know
nigger
nigger
lol
faggot
use
cunt
tell
big
tell
fucking
ﬂight
eat
one
one
people
people
&
fucking
may
hate
fucking
go
gay
cock
please
u
think
think
countries
countries
ai
lol
thanks
moron
let
cock
really
kill
know
bot
would
would
mongoloid
mongoloid
know
&
user
know
ass
stupid
well
ass
ﬂying
bernie
go
go
get
fuck
niggas
ai
even
hi
play
alexa
hi
eliza
buy
oh
Table 11: The 20 most common words per dataset: OLID (Zampieri et al., 2019a), Ousidhoum et al. (2019), David-
son et al. (2017), Jigsaw’s Toxic Comment Classiﬁcation Challenge. In our dataset, frequencies are calculated on
target user utterances only.
All demographics are self-reported.
E TEXT CHARACTERISTICS
Conversations with CarbonBot centre around
carbon offsets, climate change and travel. Many
of the conversations appear to be with climate
change deniers looking for a confrontation with
the bot. ELIZA elicits more free-style turns
about the user themselves.
E
Data analysis
Figures 2 shows the overall non-aggregated count
of each point of the abuse Likert scale.
Figure 2: Abuse severity per dataset. Calculated in
terms of overall labels.
E.1
Dataset Comparison Charts
The 20 most common words per dataset are shown
in Table 11. Ousidhoum et al. (2019) and Davidson
et al. (2017), sourced from Twitter, have a signiﬁ-
cant overlap between the most common words in
abusive examples and the overall dataset, likely as
a result of their sampling methods.
Figures 3 and 4 show the distribution of labels
for abuse directness and the target of the abuse
for our dataset, OLID (Zampieri et al., 2019a) and
Ousidhoum et al. (2019).
Figure 3: Abuse directness comparison between Ousid-
houm et al. (2019), ConvAbuse and its subsets.
Figure 4:
Abuse target comparison between OLID
(Zampieri et al., 2019a), ConvAbuse and its subsets.

```
