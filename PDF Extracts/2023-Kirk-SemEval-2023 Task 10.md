---
title: "SemEval-2023 Task 10 - PDF Extract"
source_pdf: "2023-Kirk-SemEval-2023 Task 10.pdf"
pages: 18
extracted_at: "2026-01-24T17:05:15.917691"
---

# PDF Extract: SemEval-2023 Task 10

**Source PDF:** 2023-Kirk-SemEval-2023 Task 10.pdf
**Total Pages:** 18

---

## Content

```
--- Page 1 ---

SemEval-2023 Task 10: Explainable Detection of Online Sexism
Hannah Rose Kirk1,2*, Wenjie Yin1,3*, Bertie Vidgen1, and Paul Röttger1,2
1Rewire
2University of Oxford
3Queen Mary University of London
Abstract
Online sexism is a widespread and harmful
phenomenon. Automated tools can assist the
detection of sexism at scale. Binary detection,
however, disregards the diversity of sexist con-
tent, and fails to provide clear explanations for
why something is sexist. To address this issue,
we introduce SemEval Task 10 on the Explain-
able Detection of Online Sexism (EDOS). We
make three main contributions: i) a novel hi-
erarchical taxonomy of sexist content, which
includes granular vectors of sexism to aid ex-
plainability; ii) a new dataset of 20,000 so-
cial media comments with ﬁne-grained labels,
along with larger unlabelled datasets for model
adaptation; and iii) baseline models as well as
an analysis of the methods, results and errors
for participant submissions to our task.
Content warning: We show illustrative examples of sexist
language to describe the taxonomy and analyse error types.
1
Introduction
Online sexism can inﬂict harm on women who are
targeted, make online spaces inaccessible and un-
welcoming, and perpetuate social asymmetries and
injustices. Automated tools are now widely de-
ployed to ﬁnd sexist content at scale, supporting
content moderation, monitoring and research. How-
ever, most automated classiﬁers do not give further
explanations beyond generic, high-level categories
such as ‘toxicity’, ‘abuse’ or ‘sexism’. Opaque
classiﬁcation without explanations can cause con-
fusion, anger and mistrust among moderated users,
and make it harder to challenge moderation mis-
takes; moderators who use automated tools may
not trust or fully understand the labels, reducing
their efﬁciency; and it is difﬁcult to assess model
weaknesses in the absence of granular labels, which
hinders the development of better models.
We organised the SemEval 2023 Task Explain-
able Detection of Online Sexism (EDOS), which
*Equal contribution
follows from success of previous shared tasks on
abuse and hate detection (Zampieri et al., 2019;
Ribeiro and Silva, 2019; Pavlopoulos et al., 2021;
Basile et al., 2019; Fersini et al., 2018a,b). Our task
proposes and applies a taxonomy with three hierar-
chical tasks for detecting sexist content. Task A is
a binary task to detect whether content is sexist. For
sexist content, Task B distinguishes between four
distinct categories of sexism, and Task C identiﬁes
one of 11 ﬁne-grained sexism vectors.
There are three factors that make our EDOS task
unique: First, data diversity: we sample data from
two large social media platforms (Reddit and Gab)
using an ensemble of ﬁltering methods. The entries
are more diverse than sampling from keywords
alone or a single platform. Second, annotation
quality: we recruit highly-trained annotators who
all self-identify as women. We make this deci-
sion to mitigate implicit biases in labelling and to
evoke a participatory approach to AI where the
communities primarily harmed from speciﬁc forms
of content are included in the data development
process (Birhane et al., 2022; Zytko et al., 2022).
To improve consistency of labels with our detailed
guidelines, all annotators were trained in multiple
pilot tasks, and disagreements resolved by experts.
Third, task granularity: we ground our dataset
in a carefully-constructed taxonomy such that the
multiple categories in Tasks B and C are both mean-
ingful from a social scientiﬁc perspective, aid ex-
plainability in predictions and present a challenging
machine learning task for multi-class classiﬁcation.
In releasing the dataset and analysing the accom-
panying SemEval task submissions, we contribute
to efforts in building automated sexism detection
systems which are both more accurate and explain-
able via ﬁne-grained labels.1 These contributions
mark a step towards a safer internet for women.
1All task data, individual annotations and guidelines are
available at github.com/rewire-online/edos. A data statement
is provided in Appendix A.
arXiv:2303.04222v2  [cs.CL]  8 May 2023

--- Page 2 ---

2
Taxonomy Design
2.1
Existing Taxonomies
We conducted a broad review of research on sex-
ism and misogyny. Within this literature, we iden-
tiﬁed recent articles that propose taxonomies of
sexist or misogynist content, in particular Jha and
Mamidi (2017); Samory et al. (2021); Farrell et al.
(2019); Zeinert et al. (2021); Guest et al. (2021);
Rodríguez-Sánchez et al. (2021) and Parikh et al.
(2021). Each taxonomy is unique, but they gen-
erally differ along several dimensions, including
differences in (i) construction (whether they are
built from theory or empirics); (ii) scope (how the
top-level category of sexism or misogyny is deﬁned
and which subcategories are included); and (iii)
structure (whether subcategories are hierarchically
ordered). We review these details in Appendix B.
2.2
Our Taxonomy
Starting from this literature review, we created a
ﬁrst draft of the taxonomy. The taxonomy was
further reﬁned using a grounded theory approach
(Glaser and Strauss, 2017) with empirical entries
from our dataset (see §3) to merge or adjust the
schema. It comprises three subtasks:
Task A: Binary Sexism
The ﬁrst level of our tax-
onomy makes a binary distinction between sexist
and non-sexist content. We deﬁne sexist content
as any abuse, implicit or explicit, that is directed
towards women based on their gender, or on the
combination of their gender with one or more other
identity attributes (e.g. Black women or Muslim
women). Our taxonomy focuses on sexism, rather
than misogyny. Misogyny refers to “expressions of
hate towards women" (Ussher, 2016), while sexism
also covers more subtle implicit forms of abuse and
prejudice that can still substantially harm women.2
Task B: Category of Sexism
The second level
of our taxonomy disaggregates sexist content into
four conceptually and analytically distinct cate-
gories. We consciously chose not to separate out
categories by the supposed effect on the recipient,
or supposed motivation of the speaker, because
the harm caused by sexist content is idiosyncratic;
and speaker intent is difﬁcult to gauge, especially
2Abuse primarily targeted at groups other than women,
like racism or antisemitism, is not covered by our taxonomy.
However, we tasked annotators with ﬂagging such content
using an "other target" label, which, by majority vote, applied
to 2,098 out of 15,146 non-sexist entries.
without broader context. The four categories are
(1) Threats, plans to harm & incitement: Lan-
guage where an individual expresses intent and/or
encourages others to take action against women
which inﬂicts or incites serious harm and violence
against them. It includes threats of physical, sex-
ual or privacy harm. (2) Derogation: Language
which explicitly derogates, dehumanises, demeans
or insults women. It includes negative descriptions
and stereotypes about women, objectiﬁcation of
their bodies, strong negative emotive statements,
and dehumanising comparisons. It covers negative
statements directed at a speciﬁc women and women
in general. (3) Animosity: Language which ex-
presses implicit or subtle sexism, stereotypes or de-
scriptive statements. It includes benevolent sexism,
i.e., framed as a compliment. (4) Prejudiced Dis-
cussion: Language which denies the existence of
discrimination, and justiﬁes sexist treatment. It in-
cludes denial and justiﬁcation of gender inequality,
excusing women’s mistreatment, and the ideology
of male victimhood.
Task C: Fine-Grained Vectors
The third level
of our taxonomy disaggregates each category of
sexism into ﬁne-grained sexism vectors. We seek
vectors which are mutually exclusive (i.e., each vec-
tor is distinct) and collectively exhaustive (i.e., all
sexist content can be assigned to a vector). Tab. 1
gives an overview of the 11 ﬁne-grained vectors
in our taxonomy, along with their deﬁnitions and
examples taken from prior literature then edited to
clearly demonstrate each distinct vector.
3
Dataset Construction
3.1
Choice of Platform
A large portion of online harms research gathers
data from Twitter (Vidgen and Derczynski, 2020),
resulting in lacking community-based diversity in
the severity and form of sexist content. Thus, in
order to produce a diverse dataset with coverage
of our ﬁne-grained vectors of sexism, we opt to
use two social media platforms. First, Gab, which
is an ‘alt-tech’ social networking site established
in 2016. It has positioned itself as a rival to main-
stream sites, such as Twitter and Facebook, and
explicitly aims to protect free (and far-right) speech
(Zannettou et al., 2018; Lima et al., 2018; Jasser
et al., 2021). Second, Reddit, which is a network
of topic-based forums (‘subreddits’), where users
can share, view and comment on content related

--- Page 3 ---

Category
Vector
Deﬁnition
Example
1. Threats, plans
to harm and
incitement
1.1 Threats of harm
Expressing intent, willingness or desire to harm an individual
woman or group of women. This could include, but is not
limited to: physical, sexual, emotional or privacy-based forms
of harm.
I’ll kill any women that talks back
to me
1.2 Incitement and
encouragement of harm
Inciting or encouraging an individual, group, or general
audience to harm a woman or group of women. It includes
language where the author seeks to rationalise and/or justify
harming women to another person.
Raping her would put her in her
place
2. Derogation
2.1 Descriptive attacks
Characterising or describing women in a derogatory manner.
This could include, but not limited to: negative generalisations
about women’s abilities, appearance, sexual behaviour,
intellect, character, or morals.
Women’s football is so shit, they’re
so slow and clumsy
2.2 Aggressive and
emotive attacks
Expressing strong negative sentiment against women, such as
disgust or hatred. This can be through direct description of the
speaker’s subjective emotions, baseless accusations, or the use
of gendered slurs, gender-based profanities and gender-based
insults.
I hate women
2.3 Dehumanising attacks
and overt sexual
objectiﬁcation
Derogating women by comparing them to non-human entities
such as vermin, disease or refuse, or overtly reducing them to
sexual objects.
Women are pigs
3. Animosity
3.1 Causal use of
gendered slurs, profanities
and insults
Using gendered slurs, gender-based profanities and insults,
but not to intentionally attack women. Only terms that
traditionally describe women are in scope (e.g. ‘b*tch’, ‘sl*t’).
Stop being such a little bitch
3.2 Immutable gender
differences and gender
stereotypes
Asserting immutable, natural or otherwise essential
differences between men and women. In some cases, this
could be in the form of using women’s traits to attack men.
Most sexist jokes will fall into this category.
Men and women’s brains are wired
different bro, that’s just how it is
3.3 Backhanded gendered
compliments
Ostensibly complimenting women, but actually belittling or
implying their inferiority. This could include, but is not
limited to: reduction of women’s value to their attractiveness
or sexual desirability, or implication that women are innately
frail, helpless or weak.
Women are delicate ﬂowers who
need to be cherished
3.4 Condescending
explanations or
unwelcome advice
Offering unsolicited or patronising advice to women on topics
and issues they know more about (known as ‘mansplaining’).
My gf always complains about
period pains but she just doesn’t
understand the medical science for
eliminating them!
4. Prejudiced
Discussion
4.1 Supporting
mistreatment of individual
women
Expressing support for mistreatment of women as individuals.
Support can be shown by denying, understating, or seeking to
justify such mistreatment.
Women shouldnt show that much
skin, it’s their own fault if they get
raped
4.2 Supporting systemic
discrimination against
women as a group
Expressing support for systemic discrimination of women as a
group. Support can be shown by denying, understating, or
seeking to justify such discrimination.
The leadership of men in
boardrooms is a necessary
evil—corporations need to be
efﬁciently run
Table 1: Taxonomy of sexism categories (Task B) and ﬁne-grained vectors (Task C).
to their interests. Several studies have shown that
Reddit is home to many sexist and anti-feminist
communities, described as the ‘manosphere’ (Ging,
2017; Zuckerberg, 2018; Farrell et al., 2019; Ging
et al., 2020; Ribeiro et al., 2021).
We source equal amounts of data from Reddit
and Gab. For each platform, we ﬁrst create a pool
of 1M entries (see §3.2). We then sample 10k
entries from each pool for labelling (see §3.3).
3.2
Data Collection
Gab
We collect 34M publicly available Gab
posts from August 2016 to October 2018.3 This
data has been widely used in academic studies (e.g.,
Kennedy et al., 2018; Cinelli et al., 2021). We ran-
domly sample 1M entries to create the pool.
Reddit
First, we compile a list of 81 subreddits
which are likely to contain sexist content, based
on previous work (Guest et al., 2021; Farrell et al.,
3ﬁles.pushshift.io/gab
2019; Zuckerberg, 2018; Jones et al., 2020; Qian
et al., 2019; Ging, 2017; Ribeiro et al., 2021) and
online wikis.4 Then, we collect all comments from
August 2016 to October 2018 in these subreddits
using the Reddit API.5 We manually review each
subreddit and assign it to one of four categories
(Incels, Men Going Their Own Way, Men’s Rights
Activists, Pick Up Artists) based on prior work by
Lilly (2016).6 To ensure that our dataset is not
overly biased towards niche linguistic expressions
and topics, we restrict our sampling to the 24 sub-
reddits with at least 100k comments, resulting in a
dataset of 42M comments. Finally, we randomly
sample 250k comments from each of the four sub-
reddit categories to create the pool.
4rationalwiki.org/wiki and incels.wiki
5We only collect comments as our early analysis showed
that many posts are single URLs, images or videos and thus
harder to parse in isolation for labelling. We specify the date
range to match the Gab data.
6We describe these categories in Appendix C.

--- Page 4 ---

train
dev
test
Task A
not sexist
10,602
76%
1,514
76%
3,030
76%
sexist
3,398
24%
486
24%
970
24%
total
14,000
100%
2,000
100%
4,000
100%
Task B
1. threats, plans to harm and incitement
310
9%
44
9%
89
9%
2. derogation
1,590
47%
227
47%
454
47%
3. animosity
1,165
34%
167
34%
333
34%
4. prejudiced discussion
333
10%
48
10%
94
10%
total
3,398
100%
486
100%
970
100%
Task C
1.1 threats of harm
56
2%
8
2%
16
2%
1.2 incitement and encouragement of harm
254
7%
36
7%
73
8%
2.1 descriptive attacks
717
21%
102
21%
205
21%
2.2 aggressive and emotive attacks
673
20%
96
20%
192
20%
2.3 dehumanising attacks and overt sexual objectiﬁcation
200
6%
29
6%
57
6%
3.1 casual use of gendered slurs, profanities, and insults
637
19%
91
19%
182
19%
3.2 immutable gender differences and gender stereotypes
417
12%
60
12%
119
12%
3.3 backhanded gendered compliments
64
2%
9
2%
18
2%
3.4 condescending explanations or unwelcome advice
47
1%
7
1%
14
1%
4.1 supporting mistreatment of individual women
75
2%
11
2%
21
2%
4.2 supporting systemic discrimination against women as a group
258
8%
37
8%
73
8%
total
3,398
100%
486
100%
970
100%
Table 2: Distribution of class labels across tasks and data splits.
3.3
Data Preparation and Sampling
Cleaning
We cleaned the text in the Gab and
Reddit pools by: (1) replacing URLs and user-
names with generic tokens; (2) dropping empty
entries; (3) dropping entries that only contain URLs
or emoji; (4) dropping non-English language en-
tries; and (5) dropping duplicates.
After these
cleaning steps were completed, we apply our sam-
pling techniques.
Boosted Sampling
The prevalence of abusive
content ‘in the wild’ is difﬁcult to estimate reliably,
but could be as low as 0.1% or 1% (Vidgen et al.,
2019). Sexism represents only a subset of all abuse;
So, random sampling from online platforms will
lead to a dataset with a large class imbalance, which
impedes the training of AI systems. A range of sam-
pling techniques have been used in prior work to
boost the proportion of abusive content in datasets,
including keyword search (ElSherief et al., 2017)
or lexicons (Farrell et al., 2019), and community-
based (Guest et al., 2021; Vidgen et al., 2021a) or
user-based sampling (Vidgen et al., 2019). For pri-
vacy concerns, we do not store user-based informa-
tion. Instead, we apply a mix of community-based
sampling (on Reddit), with a carefully-designed
ensemble of varied sampling methods.
Ensemble of Sampling Methods
Relying on a
single sampling method makes the sampled data
more prone to biases (Yin and Zubiaga, 2022). Fol-
lowing extensive pilots, we settle on six different
techniques to sample 10k cleaned entries from each
of Gab and Reddit pools (total n = 20,000), to en-
sure coverage of the 11 ﬁne-grained sexism vectors
and introduce lexical and topical diversity. The
six techniques sample (1) 1,000 entries with at
least one sexist keyword (e.g. “c*nt”, “b*tch”);
(2) 1,000 entries with at least one sexist keyword
and one topical keyword (e.g. “she”, “girl”); (3)
100 entries from each decile of toxicity scores from
the Perspective model (total 1,000)7; (4) 100 en-
tries from each decile of scores from a bespoke
classiﬁer for sexism detection which we trained on
seven open source sexism/misogyny datasets (to-
tal 1,000)8; (5) 1,000 entries from cases where the
score from Perspective’s Toxicity model differed
from the score of our custom classiﬁer by at least
|0.8|; and (6) 5,000 entries sampled using a combi-
nation of topical keywords and scores from other
attributes of Perspective (e.g., Identity Attacks +
“girl” or Sexually Explicit + “she”).
3.4
Data Annotation
We follow the ‘prescriptive paradigm’ for data an-
notation, in that we want the annotators to apply our
comprehensive annotation guidelines rather than
applying their own subjective beliefs (Röttger et al.,
2022). Our annotation guidelines contain deﬁni-
tions, clarifying notes, exemplars, edge cases, and
general guidance.
Annotator Recruitment
To mitigate the risk of
implicit bias and to encourage participation from af-
fected communities, we worked with trained anno-
7perspectiveapi.com
8For training details, see Appendix D.

--- Page 5 ---

tators who all self-identify as women. We required
that all annotators pass a challenging 200-entry
screening task that covered all 11 sexism vectors
in our data. In total, we recruited and trained 19
annotators who passed the screening. We opted for
expert annotation over crowdwork because pilot
experiments demonstrated an marked difference in
quality and consistency of labels.9 The demograph-
ics of annotators and their experiences with online
sexism are documented in Appendix A.
Annotation Process
Three annotators labelled
each entry. To further ensure label quality, we rely
on expert adjudication for disagreements. Experts
were called upon to give labels for (i) cases with
less than 3/3 agreement (unanimous) in Task A,
and (ii) cases with less than 2/3 agreement in Tasks
B and C. The expert team consisted of two women
authors of this paper, and two of the most expe-
rienced workers from the annotation team. Data
was assigned to annotators in batches every two
weeks over the course of two months. Through-
out the process, we worked closely with annotators
so that their feedback could be incorporated into
our guidelines and so that their welfare could be
continuously monitored and protected.
3.5
Dataset Distribution
The data was split into training, development, and
test sets in the ratio of 70:10:20. Only sexist in-
stances are included in Task B and C. Label distri-
butions of all splits are shown in Tab. 2.
4
Task Description
4.1
Task Deﬁnition
Our SemEval task consists of three subtasks, re-
ﬂecting our hierarchical taxonomy (§2.2). Task A
is a binary classiﬁcation task (sexist vs. not sexist).
Task B and C are multi-class classiﬁcation tasks,
with four and 11 categories, respectively.
4.2
Task Organisation
We ran our SemEval task on CodaLab.10 There
were two primary phases: (i) the Training and De-
velopment Phase which ran from September 2022
to January 2023, and (ii) the Test Phase, which
began on 10th January 2023 and ended on 31st Jan-
uary 2023. During the Training and Development
Phases, we released entries and labels from the
9Results are presented in Appendix E.
10codalab.lisn.upsaclay.fr/competitions/7124
train and dev splits, as well as an additional start-
ing kit including 1M unlabelled Reddit entries and
1M unlabelled Gab entries. During the Test Phase,
we staggered the release of test entries for Task
A from Tasks B and C, since the latter provides
information on the correct labels of the former.
4.3
Evaluation Metrics and Baselines
We evaluate all systems with macro-average F1
score to account for imbalance between classes. We
supply 7 baseline models (see Tab. 3) to benchmark
a range of simple to complex systems. The simplest
baselines are always predicting the most frequent
class (B0) and uniformly predicting each class (B1).
We train one traditional machine learning model
(B2) where the data is ﬁrst vectorized with TF-
IDF and then ﬁtted with an XGBoost model. The
remaining baselines use DistilBERT (Sanh et al.,
2019) and DeBERTa-v3-base (He et al., 2021a).
For each model, we ﬁne-tune on the training set
(B3, B5), and do continued pre-training on the 2M
unlabelled entries from Reddit and Gab combined
(B4, B6). Across all tasks, DeBERTa with con-
tinued pre-training sets the highest baseline. The
best baseline for Task A (F1=0.8235) is more satu-
rated than for Tasks B and C (F1=0.5926; 0.3171),
making this an interesting SemEval challenge with
varying degrees of difﬁculty and remaining head-
room for performance improvements.
5
Participant Systems and Results
5.1
Participant Overview
EDOS was a very popular SemEval task, with 599
accounts signing-up for dataset access.11 In the
Development Phase, 128 submissions were made
for Task A, 71 for Task B and 52 for Task C. In the
Test Phase, 134 submissions were made for Task
A, 87 for Task B and 81 for Task C.
Validation Process
To ensure a fair competition
in the Test Phase, we allowed one submission ac-
count per team and up to two test submissions of
task predictions, to allow for one upload mistake.12
We issued a short survey to conﬁrm compliance
with our T&Cs and collect system information. Our
ﬁnal leaderboard includes those who responded to
this survey: 84 to Task A, 69 to Task B and 63 to
11Number of accounts signed up as of 25/04/2023.
12We
unfortunately
encountered
some
suspicious
activity with multiple accounts using generic emails
ABCD1234@domain, or making >10 test set submissions.

--- Page 6 ---

Baselines
Continued
Macro-F1
Model
Pre-training
Task A
Task B
Task C
B0
MostFrequent

0.4310
0.1594
0.0317
B1
Uniform

0.4509
0.2413
0.0629
B2
XGBoost

0.4933
0.2297
0.0881
B3
DistilBERT

0.7621
0.5531
0.2935
B4

0.7804
0.5367
0.3140
B5
DeBERTa-v3-base

0.8235
0.4790
0.1517
B6

0.8235
0.5926
0.3171
Top Ranked Systems
PingAnLifeInsurance
DeBERTa-v3-large, twHIN-BERT-large

0.8746
stce
RoBERTa-large, ELECTRA

0.8740
0.7203
0.5487
FiRC-NLP
DeBERTa (ensemble)

0.8740
JUAGE
PaLM (ensemble)

0.7326
PASSTeam
RoBERTa, HateBERT

0.7212
0.5412
PALI
DeBERTa, RoBERTa

0.5606
Summary Statistics
System count
84
69
63
Q1
0.7994
0.5730
0.3153
Mean
0.8095
0.5899
0.3829
Median
0.8322
0.6191
0.4230
Std
0.0746
0.1065
0.1274
Q3
0.8537
0.6501
0.4758
Percentage of systems which beat B0
100%
100%
100%
Percentage of systems which beat B6
55%
60%
73%
Table 3: Baselines, top ranked leaderboard results and summary statistics per Task. The best baseline is bolded.
The best participant submission is bolded in red.
Task C. 59 teams submitted to all three tasks, 10
submitted to two, and 20 submitted to just one.
5.2
Leaderboard Results
The top three submissions for each task are pre-
sented in Tab. 3.13 The top three systems in all tasks
use multiple models or an ensemble, and many top
systems apply further pre-training and multi-task
learning. Notably, stce and PASSTeam achieved top
results on two or more tasks. Both used multi-task
learning and further pre-training on the unlabelled
data in the starter kit: stce use RoBERTa-large (Liu
et al., 2019) and ELECTRA (Clark et al., 2020);
while PASSTeam use a multi-task learning strat-
egy (Yu et al., 2020) with ﬁne-tuned RoBERTa
and HateBERT (Caselli et al., 2021).
In Task
A, PingAnLifeInsurance also adopt a multi-task
DNN structure (Liu et al., 2020) with further pre-
training of DeBERTa-v3 (He et al., 2021a) and
TwHIN-BERT (Zhang et al., 2022c) on the starter
kit unlabelled data and an additional Kaggle dataset.
FiRC-NLP use an ensemble of various DeBERTa
models ﬁne-tuned only on the labelled task data.
In Task B, JUAGE was one of the few systems
relying on prompt-based learning, but achieved
ﬁrst place using an instruction-tuned PaLM model
(Chowdhery et al., 2022) with a parameter-efﬁcient
prompt tuned on the task data and majority voting
13Full leaderboards are available on github.com/rewire-
online/edos
over six iterations. In Task C, PALI further pre-
trained DeBERTa-v3 using the starter kit unlabelled
data and applied a second loss term (normalized
temperature-scaled cross entropy).
Scores for Tasks B and C were substantially
lower in mean and higher in variance than Task A
(see Tab. 3). All participant systems beat our sim-
plest baseline predicting the most frequent class,
while a majority still beat our more complex base-
line of DeBERTa-v3 with continued pre-training.
5.3
Popular Methods
Architecture
For all tasks, the large majority of
participants (∼90%) used a transformers architec-
ture (Fig. 1). The most popular transformer-based
models include RoBERTa (Liu et al., 2019), De-
BERTa (He et al., 2021b,a), BERT (Devlin et al.,
2019), BERTweet (Nguyen et al., 2020) and Distil-
BERT (Sanh et al., 2019). Several submissions use
prompted language models such as GPT-2 (Rad-
ford et al., 2019), GPT-3 (Brown et al., 2020),
PaLM (Chowdhery et al., 2022) or OPT (Zhang
et al., 2022b).
Other approaches include tradi-
tional machine learning methods (∼8%) and non-
transformer deep neural networks (∼6%), which
are often combined with other methods.
Additional Training and Data
The majority of
participants applied ﬁne-tuning only on the tar-
get task (>90%) but some also apply further pre-
training (∼30%), ﬁne-tuning on an auxiliary task

--- Page 7 ---

0
25
50
75
Count
88%
92%
93%
10%
5%
7%
9%
4%
3%
Architecture
Transformers-based LM
Traditional ML
Other deep LM
Combination use
Count
96%
92%
92%
32%
33%
33%
11%
15%
14%
5%
5%
7%
Training Type
Fine-tuning on target task
Further pre-training
Fine-tuning on auxilliary task
Prompt-based learning
Combination use
Task A
Task B
Task C
0
25
50
75
Count
51%
62%
61%
40%
34%
39%
15%
8%
4%
4%
5%
4%
Additional Data
No additional data
Unlabelled data in the starter kit
Other labelled data
Other unlabelled data
Combination use
Task A
Task B
Task C
Count
66%
63%
68%
17%
18%
15%
11%
13%
9%
8%
13%
12%
Additional Features
None
Additional embeddings
Emoji
Lexicon
Combination use
Figure 1: Participant methodologies by popularity (count and percentage of submissions using the method). Each
subplot shows a different breakdown of system paper method decisions. The ﬁrst subplot (top left) shows that the
majority of participants used transformer-based language models. The second subplot (top right) shows ﬁne-tuning
on the target task was the most popular training method, but a substantial proportion of participants also applied
further pre-training. The third subplot (bottom left) similarly shows that while the majority only used the labelled
data provided in the task, many participants also used the in-domain unlabelled data in our starter kit. Finally, the
last subplot (bottom right) shows the majority did not use additional features.
(∼15%) or prompt-based learning (∼5%). Around
40% of participants used the unlabelled data in the
starter kit. Participants also sometimes used re-
sources outside our task, both labelled (∼10%) and
unlabelled data (∼5%). A number of innovative
methods were applied including data augmentation,
active learning or data cartography (Swayamdipta
et al., 2020).
Additional Features
The majority of partici-
pants did not use additional features (∼66%). If
additional features were used, they were predomi-
nantly used in a combination of additional embed-
dings (∼18%), emoji (∼12%) or lexicons (∼12%).
5.4
Most Effective Methods
The distribution of participant F1 scores across
methodologies is more tightly clustered for Task A
than Tasks B and C (see Fig. 2). Across method-
ology variables, architecture choices lead to the
most different distributions of performances, with
transformers-based and other deep language mod-
els providing a more competitive average F1 than
traditional ML systems across tasks. In contrast,
training type seems to have the least inﬂuence on
the distribution of F1 scores, with the most overlap
between conditions, even in Task C. The highly re-
lated additional data condition has slightly more
effect on performance, with the use of unlabelled
data in the starter kit resulting in the highest av-
erage. Systems that did not use any additional
features had higher average F1 scores in all tasks.
6
Error Analyses
We base our error analyses on the 10 best perform-
ing systems for each task as their errors indicate
the remaining difﬁculty within our dataset.
6.1
Quantitative Error Analysis
Confusion Between Binary Labels
Out of
4,000 test instances in Task A, 162 were misclas-
siﬁed by all top 10 systems, where 38.3% were
false positives (not sexist content predicted as sex-
ist) and 61.7% were false negatives (sexist content
predicted as not sexist). Of the false negatives, 41%
are from the Animosity category, 34% from Dero-
gation, 16% from Prejudiced Discussion and 9%
from Threats. This pattern is expected because An-
imosity is often contains implicit language, while
Threats are commonly conveyed in explicit lan-
guage.
Confusion Between Categories and Vectors
Among the categories, Threats is least often mis-
classiﬁed as other categories and the least common
mistake for instances with the true label of any
other category (see Fig. 3). Animosity and Deroga-

--- Page 8 ---

0.25
0.50
0.75
Macro-F1
Architecture
Transformers-based LM
Traditional ML
Other deep LM
Macro-F1
Training Type
Fine-tuning on auxilliary task
Fine-tuning on target task
Further pre-training
Prompt-based learning
Task A
Task B
Task C
0.25
0.50
0.75
Macro-F1
Additional Data
Unlabelled data in the starter kit
Other labelled data
No additional data
Other unlabelled data
Task A
Task B
Task C
Macro-F1
Additional Features
None
Emoji
Additional embeddings
Lexicon
Figure 2: Participant methodologies by Macro-F1 score (across submissions using the method in isolation or
combination). Each subplot shows a different breakdown of system paper method decisions and the average F1
score by task. F1 scores on Task A are generally higher and more tightly distributed than on Tasks B and C.
tion are often mistaken for each other. Instances of
Prejudiced Discussion are also commonly misclas-
siﬁed as Derogation or Animosity. The confusion
across vectors in Task C has a similar pattern (Ap-
pendix F). Some errors reﬂect class imbalance: the
largest class (2.1) and the smallest class (3.4) are
the most and least frequent confusions, respectively.
Others errors reveal inherent similarity between cer-
tain vectors: 2.1 and 3.2 are commonly confused,
with both referring to gendered stereotypes, but 2.1
is explicitly negative in sentiment. The same is true
for 2.2 and 3.1, which share gendered slurs, except
that 3.1 is causal (not targeted) usage.
1. Threats
2. Derogation 3. Animosity 4. Prejudiced
Discussion
True Category
1. Threats
2. Derogation
3. Animosity
4. Prejudiced
Discussion
Predicted Category
81.7%
2.3%
1.8%
3.8%
10.3%
74.3%
29.2%
22.2%
4.5%
19.6%
66.1%
13.8%
3.5%
3.8%
2.9%
60.1%
Task B
Figure 3: Confusion matrix for categories of sexism
(Task B) across the top 10 performing systems.
6.2
Manual Error Inspection
Two self-identifying woman authors manually in-
spected 100 instances from the Task A test set that
were misclassiﬁed by all top 10 teams. Out of the
100 entries, we identiﬁed 76 as genuine system mis-
classiﬁcations, while 24 were annotation errors.14
System Errors
Of the 76 system errors, 52 were
false negatives (68%) and 24 were false positives
(32%). Of the false negatives, there were several
common themes of misclassiﬁed examples. These
themes include (i) expressions that are seemingly
positive in sentiment or backhanded gendered com-
pliments (e.g., “STEM ain’t hard, wamans can do
it too!”); (ii) gender stereotypes encoded in a joke
(e.g., “I just bought a smart car. It doesn’t turn on
when the wife is in the driving seat.”); (iii) slang
use (e.g., “Tha Brothas want dem PAWGs.”) or
rarer gendered insults (such as “hag” or “witch”);
and (iv) irony (e.g., “either you worship women or
you’re a misogynist.”). Some explicit examples,
paired with rhetorical devices such as questions,
were also misclassiﬁed as not sexist (e.g., “How
does one learn how to choke a women? I assume
there is an art to it? Is it that you’re depriving
blood to the brain more so than choking the wind-
pipe?”).
Of the false positives, there were also a number
of common patterns. These include (i) counter-
speech (e.g., “It’s fucked up how women aren’t
14Note that the annotation error rate is likely higher in this
subset relative to the dataset as whole, because it includes chal-
lenging examples that both automated systems and humans
struggle to classify.

--- Page 9 ---

allowed to even be neutral. Always have to put
on a fucking show to entertain men and keep them
from attacking you.”); (ii) matter-of-fact discussion
or descriptions of groups associated with sexism
(e.g., “The whole point of MGTOW is, men are
going their own way....which doesn’t mean we’ve
changed from desiring women to desiring men. It
just means we don’t allow women to decide what it
is to be a man - or to be the main focal point of our
lives.”); or (iii) criticisms of an individual woman’s
actions (e.g., “I know a woman who slept with one
off her best friends on off boyfriend. Dropped her
entire social circle for a jerk, not even a Chad. She
was an, 8 as well. SMH. She had choices, chose
this guy. Women can be dumb.”).
Annotation Errors
Out of the 24 mislabelled
examples, 17 were false negatives (29%) and 7
were false positives (71%). In general, annotators
struggled with the distinction between individual-
related and generalised statements. False negatives
occur when gender stereotypes are expressed as
speculations rather than characteristic descriptions
(e.g., “We have condoms and birth control so now
women can sex with fewer and much less serious
consequences as well. It makes sense that they
would have more sex with the top guys when there’s
relatively little to risk."). False positives occur with
non-gendered attacks on individual women targets
(e.g., “This woman is just stupid.”).
Grey Areas with Lacking Context
Although
a decision was reached by the authors on each
manually-inspected instance, 9 of the 24 misla-
belled instances were considered a possibly grey
area – instances that could fall under a different
label depending on context or slight modiﬁcations
to the guideline interpretation. Individual posts
and comments taken in isolation sometimes lack
the context to interpret meaning or intent. Anno-
tators may then ﬁll in the context based on their
experiences with online sexism or knowledge of
the relevant communities. This was particularly ev-
ident in criticisms of individual woman, where it is
often unclear without context whether the speaker
is criticising an individual for their speciﬁc actions
or using that individual as scapegoat to express
general sexist stereotypes and views. This also
raises the question of whether something should be
ﬂagged if it hints at the speaker’s sexist tendency
but does not itself convey speciﬁc sexist content.
7
Discussion
7.1
Lessons Learnt
Value of Diverse Data Sampling
We note that
previous SemEval tasks on hate or abuse detection
primarily report false positive errors from their par-
ticipants. For example, in HatEval (Basile et al.,
2019), 89.1% of the errors made by the top three
systems were false positives. In our analysis, we
instead ﬁnd more false negatives. We believe this
ﬂipped distribution of error types is due to the sub-
tle and diverse forms of sexist content in our dataset
(such as Prejudiced Discussion) which do not nec-
essarily share linguistic form or keywords with
more explicit sexist content, making them more
challenging to correctly identify.
Challenge of Fine-Grained Predictions
Our
baselines and participant scores demonstrate that
binary sexism detection (Task A) is a substantially
easier task than ﬁne-grained sexism detection (Task
B and C). The maximum F1 score achieved in
Task C is just above 50%. This shows that high
scores reported in binary detection tasks of socially-
conditioned concepts (like sexism, hate or abuse)
obscure ﬁne-grained model failings in distinguish-
ing between forms of content, which may have
very different impacts on their targets and society
at large. Given the remaining headroom in predict-
ing our categories and vectors of sexism, we are
excited to see how future model-centric contribu-
tions using our dataset continue to improve perfor-
mance. Future work could also apply data-centric
techniques to increase performance and robustness,
such as augmenting the dataset with challenging
adversarial examples (Kiela et al., 2021; Vidgen
et al., 2021b; Kirk et al., 2022c) or mapping hard-
to-learn subspaces with data cartography methods
(Swayamdipta et al., 2020).
Efﬁciency of Continued Pretraining
Labelling
data for socially-conditioned tasks (like sexism) is
challenging, expensive and requires some degree
of domain expertise (Kirk et al., 2022b). However,
providing unlabelled in-domain data is both cheap,
scalable and avoids causing psychological harm on
annotators from a greater labelling burden (Kirk
et al., 2022a). We are encouraged that our best
baselines and top performing participant systems
effectively used continued pre-training on the un-
labelled in-domain data that we provided (from
Reddit and Gab). We encourage future SemEval

--- Page 10 ---

tasks to similarly release unlabelled datasets from
which they sample smaller labelled datasets.
7.2
Limitations
Class Imbalance
Our dataset is more balanced
on the binary label (24% sexism) than many previ-
ous datasets for hate and abuse detection (Vidgen
and Derczynski, 2020). However, there is substan-
tial imbalance in categories and vectors of sexism.
Thus, it is hard to conﬁrm whether confusion be-
tween categories and vectors is due to inherent
features of the data or due to the class imbalance.
We encourage future work to examine the effect on
performance and cross-vector confusion when bal-
ancing the dataset. That said, we explicitly made
the decision to not re-balance our dataset because
different types of sexism (especially at the ﬁne-
grained level) do have very different base rates ‘in
the wild’. Dealing with class imbalance is then
part-and-parcel of the problem we seek to address.
Deﬁning “Explainable”
We cast the explainabil-
ity problem as a classiﬁcation task on a single text
document (without network or user information).
In this setting, combining hierarchical classiﬁca-
tions is what adds explainability by demonstrating
whether a piece of content is sexist and for what
reason (category and vector). There are many other
promising methods to make automated systems
more explainable for socially-sensitive tasks (e.g.,
sexism, abuse or hate), including classifying spans
or masked tokens for rationale prediction (Mathew
et al., 2021; Kim et al., 2022); leveraging user and
network data (Qian et al., 2018; Wich et al., 2021)
or targets data (Kennedy et al., 2020); applying so-
cial bias frames for stereotypes (Sap et al., 2020);
or encouraging multi-hop and chain-of-thought rea-
soning (Zhang et al., 2022a; Jin et al., 2022).
Value Speciﬁcity and Perspective
Our dataset
is labelled by UK-residing annotators, who all self-
identify as women. We issue prescriptive guide-
lines, then rely on majority vote and expert adjudi-
cation to produce a gold label. Many previous stud-
ies reveal that annotator identity is a critical deter-
minant of labelling behaviour (Waseem, 2016; Lari-
more et al., 2021; Sap et al., 2022) and so majority
votes inadequately capture subjective disagreement
(Davani et al., 2021). To encourage future work on
annotator-speciﬁc artefacts, we provide annotator
IDs with each labelled entry (Prabhakaran et al.,
2021). Nonetheless, our deﬁnition of sexism, its
subcategories in our taxonomy and how our anno-
tators apply their best judgement are grounded in
few cultural viewpoints, primarily from Western-
centric and English-speaking communities. Any
classiﬁers built from our dataset will thus inherit
our values (as taxonomy and guideline writers) and
those of our annotators.15 Like most toxic content
datasets, our data is limited to English (Röttger
et al., 2022). The bounds of sexism, however, are
culturally contested and people may legitimately
disagree in where to draw the line.
8
Conclusion
In this paper, we made three main contributions.
First, we provided a new taxonomy for the more
explainable classiﬁcation of sexism in three hi-
erarchical levels – binary sexism detection, cat-
egory of sexism and ﬁne-grained vector of sex-
ism. This taxonomy is grounded in reviews of
prior taxonomies and social science literature, then
empirically-validated with in-domain data from
two social media platforms. It thus provides a so-
ciotechnical overview of the varied and nuanced
landscape of online sexism. Second, we created
a high-quality dataset, sampled with an ensemble
of techniques to increase the diversity of content
and annotated by self-identifying women experts
to ensure consistent labels. This labelled dataset is
paired with a larger unlabelled dataset to mitigate
the constraints that a labelling budget (both in terms
of ﬁnancial cost and psychological cost to annota-
tors) has on the efﬁcacy of trained systems. Finally,
we shared baseline models and summarised sys-
tems submitted to our SemEval task. This analysis
demonstrates the success of techniques that com-
bine state-of-the-art transformer models with con-
tinued pre-training and multi-task learning. How-
ever, there is still substantial headroom for improv-
ing performance on detecting ﬁne-grained forms
of sexist content. We hope that our research and re-
sources can contribute towards the design of future
systems that make online spaces safer for all.
Acknowledgements
This work was carried out by Rewire, and funded
by MetaAI. We are grateful to our annotators, and
to the Rewire team for providing feedback on this
15Bang et al. (2022) seek to design “value-aligned” sex-
ism detection systems, where their model considers both the
content and an individual’s value system to return a classiﬁ-
cation. This technique is a promising way to further improve
inclusivity and explainability in sexism detection tasks.

--- Page 11 ---

article. We also thank all participants who submit-
ted results to our task, and our reviewers who gave
valuable and constructive comments on the system
papers.
Ethical Risks and Harm Statement
We release a dataset containing online sexism,
where we have demonstrated that state-of-the-art
models still err on some speciﬁc entries and vec-
tor types. Malicious actors could use these ﬁne-
grained failures as inspiration for sexist online
posts which bypass current detection systems, or in
principal use the entries to train a generative model
(concerns also shared by Vidgen et al. (2021b) and
Kirk et al. (2022c)). We believe this risk is man-
ageable given the beneﬁt facilitated by our dataset
in understanding and predicting online sexism.
Following Kirk et al. (2022a)’s advice, we de-
scribe the risks from our dataset construction and
release. First, there is a risk of harm to data subjects
(women targeted by sexist entries) and readers of
the paper in reproducing or reinforcing harmful rep-
resentations, stereotypes, prejudiced discussions or
slur usage. We include a content warning on the
ﬁrst page and consistently display quoted examples
in italic text (Tab. 1, §6.2). Where possible, we
replace vowels in slurs with an asterisk. Due to
the labelling intensiveness of this work (20k en-
tries), there is a risk to annotators from repeatedly
viewing sexist content, especially violent entries
(like ‘threats of harm’). We carefully follow proto-
cols for supporting annotator well-being and keep
a direct line of communication open to them via a
group messaging forum. We survey annotators at
the end of the labelling process to understand how
the task affected their well-being and how we can
do better in the future. Overall, annotators found
we adequately supported their mental health and
ensured the process was as safe as possible. A few
annotators suggested we run a workshop present-
ing ﬁndings of our work. We commit to hosting
this de-brief session in the coming months as it is
important for annotators to see the signiﬁcance of
their work in supporting online safety.
References
Ashley Amaya, Ruben Bach, Florian Keusch, and
Frauke Kreuter. 2021. New Data Sources in Social
Science Research: Things to Know Before Working
With Reddit Data. Social Science Computer Review,
39(5):943–960. Publisher: SAGE Publications Inc.
Yejin Bang, Tiezheng Yu, Andrea Madotto, Zhaojiang
Lin, Mona Diab, and Pascale Fung. 2022. Enabling
Classiﬁers to Make Judgements Explicitly Aligned
with Human Values. _eprint: 2210.07652v1.
Valerio Basile, Cristina Bosco, Elisabetta Fersini, Deb-
ora Nozza, Viviana Patti, Francisco Manuel Rangel
Pardo, Paolo Rosso, and Manuela Sanguinetti. 2019.
Semeval-2019 task 5: Multilingual detection of hate
speech against immigrants and women in Twitter. In
Proceedings of the 13th International Workshop on
Semantic Evaluation, pages 54–63.
Emily M. Bender and Batya Friedman. 2018.
Data
Statements for Natural Language Processing: To-
ward Mitigating System Bias and Enabling Better
Science. Transactions of the Association for Com-
putational Linguistics, 6:587–604.
Abeba Birhane, William Isaac, Vinodkumar Prab-
hakaran, Mark Diaz, Madeleine Clare Elish, Iason
Gabriel, and Shakir Mohamed. 2022. Power to the
People? Opportunities and Challenges for Participa-
tory AI. In Equity and Access in Algorithms, Mech-
anisms, and Optimization, EAAMO ’22, pages 1–
8, New York, NY, USA. Association for Computing
Machinery.
Tom Brown, Benjamin Mann, Nick Ryder, Melanie
Subbiah,
Jared
D
Kaplan,
Prafulla
Dhariwal,
Arvind Neelakantan, Pranav Shyam, Girish Sastry,
Amanda Askell, Sandhini Agarwal, Ariel Herbert-
Voss, Gretchen Krueger, Tom Henighan, Rewon
Child, Aditya Ramesh, Daniel Ziegler, Jeffrey Wu,
Clemens Winter, Chris Hesse, Mark Chen, Eric
Sigler, Mateusz Litwin, Scott Gray, Benjamin Chess,
Jack Clark, Christopher Berner, Sam McCandlish,
Alec Radford, Ilya Sutskever, and Dario Amodei.
2020. Language Models are Few-Shot Learners. In
Advances in Neural Information Processing Systems,
volume 33, pages 1877–1901. Curran Associates,
Inc.
Tommaso Caselli, Valerio Basile, Jelena Mitrovi´c, and
Michael Granitzer. 2021.
HateBERT: Retraining
BERT for abusive language detection in English. In
Proceedings of the 5th Workshop on Online Abuse
and Harms (WOAH 2021), pages 17–25, Online. As-
sociation for Computational Linguistics.
Aakanksha Chowdhery, Sharan Narang, Jacob Devlin,
Maarten Bosma, Gaurav Mishra, Adam Roberts,
Paul Barham, Hyung Won Chung, Charles Sutton,
Sebastian Gehrmann, Parker Schuh, Kensen Shi,
Sasha Tsvyashchenko, Joshua Maynez, Abhishek
Rao, Parker Barnes, Yi Tay, Noam Shazeer, Vin-
odkumar Prabhakaran, Emily Reif, Nan Du, Ben

--- Page 12 ---

Hutchinson, Reiner Pope, James Bradbury, Jacob
Austin, Michael Isard, Guy Gur-Ari, Pengcheng
Yin, Toju Duke, Anselm Levskaya, Sanjay Ghe-
mawat, Sunipa Dev, Henryk Michalewski, Xavier
Garcia, Vedant Misra, Kevin Robinson, Liam Fe-
dus, Denny Zhou, Daphne Ippolito, David Luan,
Hyeontaek Lim, Barret Zoph, Alexander Spiridonov,
Ryan Sepassi, David Dohan, Shivani Agrawal, Mark
Omernick, Andrew M. Dai, Thanumalayan Sankara-
narayana Pillai, Marie Pellat, Aitor Lewkowycz,
Erica Moreira, Rewon Child, Oleksandr Polozov,
Katherine Lee, Zongwei Zhou, Xuezhi Wang, Bren-
nan Saeta, Mark Diaz, Orhan Firat, Michele Catasta,
Jason Wei, Kathy Meier-Hellstern, Douglas Eck,
Jeff Dean, Slav Petrov, and Noah Fiedel. 2022.
PaLM: Scaling Language Modeling with Pathways.
ArXiv:2204.02311 [cs].
Matteo Cinelli, Gianmarco De Francisci Morales,
Alessandro Galeazzi, Walter Quattrociocchi, and
Michele Starnini. 2021. The echo chamber effect on
social media. Proceedings of the National Academy
of Sciences, 118(9). Publisher: National Acad Sci-
ences.
Kevin Clark, Minh-Thang Luong, Quoc V. Le, and
Christopher D. Manning. 2020.
ELECTRA: Pre-
training Text Encoders as Discriminators Rather
Than Generators.
In International Conference on
Learning Representations.
Aida Mostafazadeh Davani, Mark Díaz, and Vinod-
kumar Prabhakaran. 2021. Dealing with Disagree-
ments: Looking Beyond the Majority Vote in Sub-
jective Annotations. ArXiv:2110.05719 [cs].
Jacob Devlin, Ming-Wei Chang, Kenton Lee, and
Kristina Toutanova. 2019.
BERT: Pre-training of
Deep Bidirectional Transformers for Language Un-
derstanding. In Proceedings of the 2019 Conference
of the North American Chapter of the Association
for Computational Linguistics: Human Language
Technologies, Volume 1 (Long and Short Papers),
pages 4171–4186, Minneapolis, Minnesota. Associ-
ation for Computational Linguistics.
Mai ElSherief, Elizabeth Belding, and Dana Nguyen.
2017. #NotOkay: Understanding Gender-Based Vi-
olence in Social Media. Proceedings of the Interna-
tional AAAI Conference on Web and Social Media,
11(1):52–61. Number: 1.
Tracie Farrell, Miriam Fernandez, Jakub Novotny, and
Harith Alani. 2019. Exploring Misogyny across the
Manosphere in Reddit. In Proceedings of the 10th
ACM Conference on Web Science, pages 87–96. As-
sociation for Computing Machinery, New York, NY,
USA.
E Fersini, P Rosso, and M Anzovino. 2018a. Overview
of the Task on Automatic Misogyny Identiﬁcation at
IberEval 2018. In Proceedings of the Third Work-
shop on Evaluation of Human Language Technolo-
gies for Iberian Languages (IberEval 2018), pages
214–228.
Elisabetta Fersini, Debora Nozza, and Paolo Rosso.
2018b. Overview of the Evalita 2018 Task on Auto-
matic Misogyny Identiﬁcation (AMI). In EVALITA
Evaluation of NLP and Speech Tools for Italian,
pages 59–66. Accademia University Press.
Debbie Ging. 2017. Alphas, Betas, and Incels: The-
orizing the Masculinities of the Manosphere. Men
and Masculinities, 1:20.
Debbie Ging, Theodore Lynn, and Pierangelo Rosati.
2020. Neologising misogyny: Urban Dictionary’s
folksonomies of sexual abuse. New Media & Soci-
ety, 22(5):838–856. Publisher: SAGE Publications.
Barney Glaser and Anselm Strauss. 2017. Discovery
of Grounded Theory: Strategies for Qualitative Re-
search. Routledge, New York.
Ella Guest, Bertie Vidgen, Alexandros Mittos, Nis-
hanth Sastry, Gareth Tyson, and Helen Margetts.
2021. An Expert Annotated Dataset for the Detec-
tion of Online Misogyny. In Proceedings of the 16th
Conference of the European Chapter of the Associ-
ation for Computational Linguistics: Main Volume,
pages 1336–1350, Online. Association for Computa-
tional Linguistics.
Pengcheng He, Jianfeng Gao, and Weizhu Chen.
2021a.
DeBERTaV3:
Improving
DeBERTa
using
ELECTRA-Style
Pre-Training
with
Gradient-Disentangled
Embedding
Sharing.
ArXiv:2111.09543 [cs].
Pengcheng He, Xiaodong Liu, Jianfeng Gao, and
Weizhu Chen. 2021b.
DeBERTa:
Decoding-
enhanced
BERT
with
Disentangled
Attention.
ArXiv:2006.03654 [cs].
Greta Jasser, Jordan McSwiney, Ed Pertwee, and Sav-
vas Zannettou. 2021. ‘Welcome to #GabFam’: Far-
right virtual community on Gab. New Media & So-
ciety, page 146144482110245.
Akshita Jha and Radhika Mamidi. 2017. When does
a compliment become sexist? Analysis and classiﬁ-
cation of ambivalent sexism using twitter data. In
Proceedings of the Second Workshop on NLP and
Computational Social Science, pages 7–16, Vancou-
ver, Canada. Association for Computational Linguis-
tics.
Zhijing Jin,
Sydney Levine,
Fernando Gonzalez
Adauto, Ojasv Kamal, Maarten Sap, Mrinmaya
Sachan, Rada Mihalcea, Joshua B Tenenbaum, and
Bernhard Schölkopf. 2022. When to make excep-
tions: Exploring language models as accounts of hu-
man moral judgment. In Advances in Neural Infor-
mation Processing Systems.
Callum Jones, Verity Trott, and Scott Wright. 2020.
Sluts and soyboys: MGTOW and the production of
misogynistic online harassment. New media & so-
ciety, 22(10):1903–1921. Publisher: SAGE Publica-
tions Sage UK: London, England.

--- Page 13 ---

Brendan
Kennedy,
Mohammad
Atari,
Aida
Mostafazadeh
Davani,
Leigh
Yeh,
Ali
Omrani,
Yehsong Kim,
Kris Coombs,
Shreya
Havaldar,
Gwenyth
Portillo-Wightman,
Elaine
Gonzalez, Joseph Hoover, Aida Azatian, Alyzeh
Hussain, Austin Lara, Gabriel Olmos, Adam Omary,
Christina Park, Clarisa Wijaya, Xin Wang, Yong
Zhang, and Morteza Dehghani. 2018. The Gab Hate
Corpus: A Collection of 27k Posts Annotated for
Hate Speech. PsyArXiv. Publisher: PsyArXiv.
Brendan Kennedy, Xisen Jin, Aida Mostafazadeh Da-
vani, Morteza Dehghani, and Xiang Ren. 2020. Con-
textualizing Hate Speech Classiﬁers with Post-hoc
Explanation.
In Proceedings of the 58th Annual
Meeting of the Association for Computational Lin-
guistics, pages 5435–5442, Online. Association for
Computational Linguistics.
Douwe Kiela, Max Bartolo, Yixin Nie, Divyansh
Kaushik, Atticus Geiger, Zhengxuan Wu, Bertie Vid-
gen, Grusha Prasad, Amanpreet Singh, Pratik Ring-
shia, et al. 2021.
Dynabench: Rethinking bench-
marking in nlp.
In Proceedings of the 2021 Con-
ference of the North American Chapter of the Asso-
ciation for Computational Linguistics: Human Lan-
guage Technologies, pages 4110–4124.
Jiyun Kim, Byounghan Lee, and Kyung-Ah Sohn.
2022.
Why Is It Hate Speech?
Masked Ratio-
nale Prediction for Explainable Hate Speech Detec-
tion. In Proceedings of the 29th International Con-
ference on Computational Linguistics, pages 6644–
6655, Gyeongju, Republic of Korea. International
Committee on Computational Linguistics.
Hannah Kirk, Abeba Birhane, Bertie Vidgen, and Leon
Derczynski. 2022a. Handling and Presenting Harm-
ful Text in NLP Research. In Findings of the Associ-
ation for Computational Linguistics: EMNLP 2022,
pages 497–510, Abu Dhabi, United Arab Emirates.
Association for Computational Linguistics.
Hannah Kirk, Bertie Vidgen, and Scott Hale. 2022b.
Is more data better?
re-thinking the importance
of efﬁciency in abusive language detection with
transformers-based active learning. In Proceedings
of the Third Workshop on Threat, Aggression and Cy-
berbullying (TRAC 2022), pages 52–61, Gyeongju,
Republic of Korea. Association for Computational
Linguistics.
Hannah Kirk, Bertie Vidgen, Paul Rottger, Tristan
Thrush, and Scott Hale. 2022c. Hatemoji: A test
suite and adversarially-generated dataset for bench-
marking and detecting emoji-based hate.
In Pro-
ceedings of the 2022 Conference of the North Amer-
ican Chapter of the Association for Computational
Linguistics: Human Language Technologies, pages
1352–1368, Seattle, United States. Association for
Computational Linguistics.
Savannah Larimore, Ian Kennedy, Breon Haskett, and
Alina Arseniev-Koehler. 2021. Reconsidering An-
notator Disagreement about Racist Language: Noise
or Signal? In Proceedings of the Ninth International
Workshop on Natural Language Processing for So-
cial Media, pages 81–90, Online. Association for
Computational Linguistics.
Mary Lilly. 2016.
The World is Not a Safe Place
for Men:
The Representational Politics of the
Manosphere. University of Ottawa. Backup Pub-
lisher: University of Ottawa.
Lucas Lima, Julio C.S. Reis, Philipe Melo, Fabricio
Murai, Leandro Araujo, Pantelis Vikatos, and Fabri-
cio Benevenuto. 2018.
Inside the Right-Leaning
Echo Chambers: Characterizing Gab, an Unmoder-
ated Social System.
In 2018 IEEE/ACM Interna-
tional Conference on Advances in Social Networks
Analysis and Mining (ASONAM), pages 515–522.
ISSN: 2473-991X.
Xiaodong Liu, Yu Wang, Jianshu Ji, Hao Cheng,
Xueyun Zhu,
Emmanuel Awa,
Pengcheng He,
Weizhu Chen, Hoifung Poon, Guihong Cao, and
Jianfeng Gao. 2020. The Microsoft Toolkit of Multi-
Task Deep Neural Networks for Natural Language
Understanding. In Proceedings of the 58th Annual
Meeting of the Association for Computational Lin-
guistics: System Demonstrations, pages 118–126,
Online. Association for Computational Linguistics.
Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Man-
dar Joshi, Danqi Chen, Omer Levy, Mike Lewis,
Luke Zettlemoyer, and Veselin Stoyanov. 2019.
RoBERTa: A Robustly Optimized BERT Pretrain-
ing Approach. ArXiv:1907.11692 [cs].
Binny Mathew,
Punyajoy Saha,
Seid Muhie Yi-
mam, Chris Biemann, Pawan Goyal, and Animesh
Mukherjee. 2021.
HateXplain:
A Benchmark
Dataset for Explainable Hate Speech Detection. Pro-
ceedings of the AAAI Conference on Artiﬁcial Intel-
ligence, 35(17):14867–14875. Number: 17.
Dat Quoc Nguyen, Thanh Vu, and Anh Tuan Nguyen.
2020.
BERTweet: A pre-trained language model
for English Tweets.
In Proceedings of the 2020
Conference on Empirical Methods in Natural Lan-
guage Processing: System Demonstrations, pages 9–
14, Online. Association for Computational Linguis-
tics.
Pulkit Parikh, Harika Abburi, Niyati Chhaya, Manish
Gupta, and Vasudeva Varma. 2021.
Categorizing
Sexism and Misogyny through Neural Approaches.
ACM Transactions on the Web, 15(4):17:1–17:31.
John Pavlopoulos, Jeffrey Sorensen, Léo Laugier, and
Ion Androutsopoulos. 2021.
Semeval-2021 task
5: Toxic spans detection.
In Proceedings of the
15th International Workshop on Semantic Evalua-
tion (SemEval-2021), pages 59–69.
Vinodkumar Prabhakaran, Aida Mostafazadeh Da-
vani,
and Mark Díaz. 2021.
On Releasing
Annotator-Level Labels and Information in Datasets.
ArXiv:2110.05699 [cs].

--- Page 14 ---

Jing Qian, Anna Bethke, Yinyin Liu, Elizabeth Beld-
ing, and William Yang Wang. 2019. A Benchmark
Dataset for Learning to Intervene in Online Hate
Speech. In Proceedings of the 2019 Conference on
Empirical Methods in Natural Language Processing
and the 9th International Joint Conference on Natu-
ral Language Processing (EMNLP-IJCNLP), pages
4755–4764. Association for Computational Linguis-
tics. Event-place: Hong Kong, China.
Jing Qian, Mai ElSherief, Elizabeth Belding, and
William Yang Wang. 2018. Leveraging Intra-User
and Inter-User Representation Learning for Auto-
mated Hate Speech Detection.
In Proceedings of
the 2018 Conference of the North American Chap-
ter of the Association for Computational Linguistics:
Human Language Technologies, Volume 2 (Short Pa-
pers), pages 118–123, New Orleans, Louisiana. As-
sociation for Computational Linguistics.
Alec Radford, Jeffrey Wu, Rewon Child, David Luan,
Dario Amodei, and Ilya Sutskever. 2019.
Lan-
guage Models are Unsupervised Multitask Learners.
page 24.
Alison Ribeiro and Nádia Silva. 2019. INF-HatEval
at SemEval-2019 Task 5: Convolutional neural net-
works for hate speech detection against women
and immigrants on twitter.
In Proceedings of the
13th International Workshop on Semantic Evalua-
tion, pages 420–425.
Manoel Horta Ribeiro, Jeremy Blackburn, Barry Brad-
lyn, Emiliano De Cristofaro, Gianluca Stringhini,
Summer Long, Stephanie Greenberg, and Savvas
Zannettou. 2021. The Evolution of the Manosphere
across the Web.
Proceedings of the International
AAAI Conference on Web and Social Media, 15:196–
207.
Francisco Rodríguez-Sánchez, Jorge Carrillo-de Al-
bornoz, Laura Plaza, Julio Gonzalo, Paolo Rosso,
Miriam
Comet,
and
Trinidad
Donoso.
2021.
Overview of EXIST 2021: sEXism Identiﬁcation in
Social neTworks. Procesamiento del Lenguaje Nat-
ural, 67(0):195–207.
Paul Röttger, Debora Nozza, Federico Bianchi, and
Dirk Hovy. 2022.
Data-efﬁcient strategies for ex-
panding hate speech detection into under-resourced
languages. In Proceedings of the 2022 Conference
on Empirical Methods in Natural Language Pro-
cessing, pages 5674–5691, Abu Dhabi, United Arab
Emirates. Association for Computational Linguis-
tics.
Paul Röttger, Bertie Vidgen, Dirk Hovy, and Janet
Pierrehumbert. 2022.
Two Contrasting Data An-
notation Paradigms for Subjective NLP Tasks.
In
Proceedings of the 2022 Conference of the North
American Chapter of the Association for Computa-
tional Linguistics: Human Language Technologies,
pages 175–190, Seattle, United States. Association
for Computational Linguistics.
Mattia Samory, Indira Sen, Julian Kohne, Fabian Flöck,
and Claudia Wagner. 2021. “Call me sexist, but...”
: Revisiting Sexism Detection Using Psychological
Scales and Adversarial Samples. Proceedings of the
International AAAI Conference on Web and Social
Media, 15:573–584.
Victor Sanh, Lysandre Debut, Julien Chaumond, and
Thomas Wolf. 2019. DistilBERT, a distilled version
of BERT: smaller, faster, cheaper and lighter. arXiv
preprint arXiv:1910.01108.
Maarten Sap, Saadia Gabriel, Lianhui Qin, Dan Juraf-
sky, Noah A. Smith, and Yejin Choi. 2020. Social
Bias Frames: Reasoning about Social and Power Im-
plications of Language. ArXiv:1911.03891 [cs].
Maarten Sap, Swabha Swayamdipta, Laura Vianna,
Xuhui Zhou, Yejin Choi, and Noah A. Smith. 2022.
Annotators with Attitudes:
How Annotator Be-
liefs And Identities Bias Toxic Language Detection.
ArXiv:2111.07997 [cs].
Swabha Swayamdipta, Roy Schwartz, Nicholas Lourie,
Yizhong Wang,
Hannaneh Hajishirzi,
Noah A.
Smith, and Yejin Choi. 2020. Dataset Cartography:
Mapping and Diagnosing Datasets with Training Dy-
namics. In Proceedings of the 2020 Conference on
Empirical Methods in Natural Language Process-
ing (EMNLP), pages 9275–9293, Online. Associa-
tion for Computational Linguistics.
Jane M Ussher. 2016.
Misogyny.
The Wiley Black-
well Encyclopedia of Gender and Sexuality Studies,
pages 1–3. Publisher: Wiley Online Library.
Bertie Vidgen and Leon Derczynski. 2020. Directions
in Abusive Language Training Data, a Systematic
Review: Garbage in, Garbage Out.
PLOS ONE,
15(12):e0243300. Publisher: Public Library of Sci-
ence arXiv: 2004.01670.
Bertie Vidgen, Alex Harris, Dong Nguyen, Rebekah
Tromble, Scott Hale, and Helen Margetts. 2019.
Challenges and frontiers in abusive content detec-
tion. In Proceedings of the Third Workshop on Abu-
sive Language Online, pages 80–93, Florence, Italy.
Association for Computational Linguistics.
Bertie Vidgen, Dong Nguyen, Helen Margetts, Patri-
cia Rossini, and Rebekah Tromble. 2021a.
Intro-
ducing CAD: the Contextual Abuse Dataset. In Pro-
ceedings of the 2021 Conference of the North Amer-
ican Chapter of the Association for Computational
Linguistics: Human Language Technologies, pages
2289–2303, Online. Association for Computational
Linguistics.
Bertie Vidgen, Tristan Thrush, Zeerak Waseem, and
Douwe Kiela. 2021b.
Learning from the Worst:
Dynamically Generated Datasets to Improve Online
Hate Detection. In Proceedings of the 59th Annual
Meeting of the Association for Computational Lin-
guistics and the 11th International Joint Conference
on Natural Language Processing (Volume 1: Long

--- Page 15 ---

Papers), pages 1667–1682, Online. Association for
Computational Linguistics.
Zeerak Waseem. 2016. Are You a Racist or Am I See-
ing Things? Annotator Inﬂuence on Hate Speech
Detection on Twitter.
In Proceedings of the First
Workshop on NLP and Computational Social Sci-
ence, pages 138–142, Austin, Texas. Association for
Computational Linguistics.
Maximilian Wich, Edoardo Mosca, Adrian Gorniak, Jo-
hannes Hingerl, and Georg Groh. 2021.
Explain-
able Abusive Language Classiﬁcation Leveraging
User and Network Data. In Machine Learning and
Knowledge Discovery in Databases. Applied Data
Science Track, Lecture Notes in Computer Science,
pages 481–496, Cham. Springer International Pub-
lishing.
Thomas Wolf, Lysandre Debut, Victor Sanh, Julien
Chaumond, Clement Delangue, Anthony Moi, Pier-
ric Cistac, Tim Rault, Remi Louf, Morgan Funtow-
icz, Joe Davison, Sam Shleifer, Patrick von Platen,
Clara Ma, Yacine Jernite, Julien Plu, Canwen Xu,
Teven Le Scao, Sylvain Gugger, Mariama Drame,
Quentin Lhoest, and Alexander Rush. 2020. Trans-
formers: State-of-the-Art Natural Language Process-
ing. In Proceedings of the 2020 Conference on Em-
pirical Methods in Natural Language Processing:
System Demonstrations, pages 38–45, Online. Asso-
ciation for Computational Linguistics.
Wenjie Yin and Arkaitz Zubiaga. 2022.
Hidden be-
hind the obvious: Misleading keywords and implic-
itly abusive language on social media. Online Social
Networks and Media, 30:100210.
Tianhe Yu, Saurabh Kumar, Abhishek Gupta, Sergey
Levine, Karol Hausman, and Chelsea Finn. 2020.
Gradient Surgery for Multi-Task Learning. In Ad-
vances in Neural Information Processing Systems,
volume 33, pages 5824–5836. Curran Associates,
Inc.
Marcos Zampieri, Shervin Malmasi, Preslav Nakov,
Sara Rosenthal, Noura Farra, and Ritesh Kumar.
2019. SemEval-2019 Task 6: Identifying and Cat-
egorizing Offensive Language in Social Media (Of-
fensEval).
In Proceedings of the 13th Interna-
tional Workshop on Semantic Evaluation, pages 75–
86, Minneapolis, Minnesota, USA. Association for
Computational Linguistics.
Savvas Zannettou, Barry Bradlyn, Emiliano De Cristo-
faro, Haewoon Kwak, Michael Sirivianos, Gianluca
Stringini, and Jeremy Blackburn. 2018.
What is
Gab: A Bastion of Free Speech or an Alt-Right
Echo Chamber. In Companion Proceedings of the
The Web Conference 2018, WWW ’18, pages 1007–
1014, Republic and Canton of Geneva, CHE. Interna-
tional World Wide Web Conferences Steering Com-
mittee.
Philine Zeinert, Nanna Inie, and Leon Derczynski.
2021. Annotating Online Misogyny. In Proceed-
ings of the 59th Annual Meeting of the Association
for Computational Linguistics and the 11th Interna-
tional Joint Conference on Natural Language Pro-
cessing (Volume 1: Long Papers), pages 3181–3197,
Online. Association for Computational Linguistics.
Qiang Zhang, Jason Naradowsky, and Yusuke Miyao.
2022a.
Rethinking offensive text detection as a
multi-hop reasoning problem. In Findings of the As-
sociation for Computational Linguistics: ACL 2022,
pages 3888–3905, Dublin, Ireland. Association for
Computational Linguistics.
Susan Zhang, Stephen Roller, Naman Goyal, Mikel
Artetxe, Moya Chen, Shuohui Chen, Christopher De-
wan, Mona Diab, Xian Li, Xi Victoria Lin, Todor
Mihaylov, Myle Ott, Sam Shleifer, Kurt Shuster,
Daniel Simig, Punit Singh Koura, Anjali Sridhar,
Tianlu Wang, and Luke Zettlemoyer. 2022b. OPT:
Open Pre-trained Transformer Language Models.
ArXiv:2205.01068 [cs].
Xinyang Zhang, Yury Malkov, Omar Florez, Serim
Park, Brian McWilliams, Jiawei Han, and Ahmed El-
Kishky. 2022c. TwHIN-BERT: A Socially-Enriched
Pre-trained Language Model for Multilingual Tweet
Representations. ArXiv:2209.07562 [cs].
Donna Zuckerberg. 2018. Not All Dead White Men:
Classics and Misogyny in the Digital Age. Harvard
University Press, Cambridge, Massachusetts.
Douglas Zytko, Pamela J. Wisniewski, Shion Guha,
Eric P. S. Baumer, and Min Kyung Lee. 2022. Par-
ticipatory Design of AI Systems:
Opportunities
and Challenges Across Diverse Users, Relationships,
and Application Domains.
In Extended Abstracts
of the 2022 CHI Conference on Human Factors in
Computing Systems, CHI EA ’22, pages 1–4, New
York, NY, USA. Association for Computing Machin-
ery.

--- Page 16 ---

A
Data Statement
We provide a data statement (Bender and Friedman,
2018) to document the generation and provenance
of our EDOS dataset.
A.1
Curation Rationale
The purpose of the EDOS dataset is to train and
evaluate automated systems for the ﬁne-grained
and explainable detection of online sexism. We cu-
rate social media comments across diverse forms of
sexist content – varying from explicitly threatening
behaviour (e.g., “I’ll kill any women that talks to
me”) through to more subtle forms (e.g., “Women
are delicate ﬂowers who need to be cherished”).
A.2
Language Variety
All entries are in English, dictated by the expertise
of researchers and annotators. We encourage future
work to expand our vectors to other languages.
A.3
Speaker Demographics
All entries are collected from two social media
platforms: Gab and Reddit. Thus, the speaker de-
mographics approximate these platforms’ users in
general (Amaya et al., 2021). We expect (and inten-
tionally sample) users who are likely male, western
and right-leaning, and hold extreme or far-right
views about women, gender issues and feminism
(Zannettou et al., 2018; Lima et al., 2018).
A.4
Annotator Demographics
We recruited 19 annotators from our existing net-
work of freelance annotators. They worked over
two months in Spring 2022. Annotators were paid
£16/hour and expert annotators were paid £20/hour.
All annotators were screened on a gold standard set
of 200 entries and had previous experience work-
ing on hate speech annotation tasks. Annotators
could contact the research team at any point using a
messaging platform. All annotators self-identiﬁed
as women. We sent annotators an optional survey
to collect further information on their demograph-
ics and to understand past experiences with social
media and online sexism. Of 19 annotators, 12
responded to our survey. By age, 3 were between
18–24 years old, 8 were between 25–30 years old
and 1 was between 31–40 years old. The com-
pleted education level was high school for 1 anno-
tator, undergraduate degree for 6 annotators and
post-graduate degree for 5 annotators. Annotators
came from a variety of nationalities, with 7 British,
as well as Swedish, Swiss, Italian and Argentinian.
Most annotators identiﬁed as White with one anno-
tator identifying as mixed South Asian and White,
and one annotator identifying as Black British. The
majority identiﬁed as heterosexual (7), with others
identifying as bisexual, pansexual or asexual. 8 an-
notators were native English speakers and 4 were
non-native but ﬂuent. The majority of annotators
used social media for one or more hours a day (7).
All annotators had seen others targeted by online
sexism, and 7 had been personally targeted.
We also collected annotator-speciﬁc attitudes to
online sexism, for example (i) what types of on-
line sexism they believe social media companies
should prioritise in their content moderation poli-
cies, and (ii) whether content should be removed or
partially hidden. We ask annotators about their con-
tent moderation preferences for content ascribing
to each of our 11 vectors. In future work, we plan
to map these preferences to our dataset entries to
investigate whether attitudes inﬂuenced labelling
behaviour.
A.5
Speech Situation
The modality of entries is short-form written tex-
tual comments from social media, which were in-
terpreted in isolation for labelling i.e., not in a com-
ment thread and without user or network informa-
tion.
A.6
Text Characteristics
The genre of texts is sexist and non-sexist social
media comments. The composition of the ﬁnal
dataset is described in Tab. 2.
B
Review of Existing Taxonomies
We reviewed recent articles that propose tax-
onomies of sexist or misogynist content, in particu-
lar: Jha and Mamidi (2017); Samory et al. (2021);
Farrell et al. (2019); Zeinert et al. (2021); Guest
et al. (2021); Rodríguez-Sánchez et al. (2021); and
Parikh et al. (2021). We describe here several key
differences between prior work and how our taxon-
omy (in §2.2) compares:
Differences in Construction
The taxonomies
we reviewed are either theoretically- or empirically-
grounded. Empirically-motivated studies mostly
produce a ﬁrst version of the taxonomies based on
NLP literature and then iteratively adjust the taxon-
omy using new data they collect (Zeinert et al.,
2021; Guest et al., 2021).
Twitter is the most

--- Page 17 ---

widely used source (Jha and Mamidi, 2017; Fersini
et al., 2018a; Samory et al., 2021; Zeinert et al.,
2021; Rodríguez-Sánchez et al., 2021), followed
by Reddit (Farrell et al., 2019; Guest et al., 2021).
Data collection was mostly based on keywords,
such as slurs and sexist hashtags, except for Farrell
et al. (2019) who sampled more widely from the
“manosphere" community and Parikh et al. (2021)
who based their study on “The Everyday Sexism
Project" – a catalogue of accounts of people who ex-
perienced sexism. Some studies also included the
re-annotation of existing datasets (Jha and Mamidi,
2017; Samory et al., 2021; Guest et al., 2021) and
addition of adversarial data (Samory et al., 2021).
Our taxonomy is theory- and empirics-grounded –
we ﬁrst draw on previous theory-based taxonomies
and then iterate with in-domain data.
Differences in Scope
Existing taxonomies differ
in scope, which is partly reﬂected in their focus
on either sexism (Samory et al., 2021; Rodríguez-
Sánchez et al., 2021; Parikh et al., 2021) or misog-
yny (Jha and Mamidi, 2017; Fersini et al., 2018a;
Farrell et al., 2019; Guest et al., 2021; Zeinert et al.,
2021). There are clear inconsistencies in how both
of these terms are deﬁned. Zeinert et al. (2021),
for example, formally deﬁne misogyny as a type
of group-directed abuse and hate speech. In prac-
tice, their account of misogyny is very similar to
the fairly broad account of sexism that we have
adopted. Our taxonomy clearly positions sexism as
a type of abuse, with a broader scope than misog-
yny. Existing taxonomies often cover overlapping
but different topics. They also differ in how they
name and deﬁne more ﬁne-grained types of sex-
ism and misogyny – which we call vectors – if
those are present at all. Jha and Mamidi (2017), for
instance, use a speciﬁc theory on benevolent sex-
ism from social psychology to motivate three main
types of sexism: Paternalism, Gender Differentia-
tion, and Heterosexuality. In contrast, Parikh et al.
(2021) construct 23 vectors of sexism, based on the
perspectives of those targeted by sexism. They dis-
tinguish, among other things, between role and at-
tribute stereotyping, as well as work-, menstruation-
, and motherhood-related gender discrimination.
Some work uses descriptive names for vectors (e.g.,
“physical violence" (Farrell et al., 2019; Guest et al.,
2021), while other names are based on social sci-
ence theories or terms (e.g., “gaslighting" (Parikh
et al., 2021), “belittling" (Farrell et al., 2019) and
“neosexism" (Zeinert et al., 2021)). Our taxonomy
consistently uses descriptive names, with a roughly
equivalent degree of granularity within each level.
Differences in Structure
Finally, existing tax-
onomies differ in how they organise vectors of sex-
ist and misogynist content. Most commonly, all
vectors are direct subtypes of misogyny or sexism
(Fersini et al., 2018a; Zeinert et al., 2021; Farrell
et al., 2019; Rodríguez-Sánchez et al., 2021; Parikh
et al., 2021), without explicit relationships between
them. Jha and Mamidi (2017) and Samory et al.
(2021) include additional ﬂags for benevolent/civil
vs. hostile/uncivil expressions, and Fersini et al.
(2018a) have ﬂags for targets. Guest et al. (2021)
provide a multi-level hierarchy of types and vec-
tors of misogyny. Our taxonomy also takes a hi-
erarchical approach, differentiating ﬁrst between
categories of sexism and then between ﬁne-grained
sexism vectors within each category.
C
Additional Detail on Reddit Data
We identiﬁed a long list of 81 relevant subreddits
by reviewing seven research papers and three
established online lists. Some of the subreddits
have been banned but data is still available for
them, and they are included within our long list.
The 81 subreddits were then assigned to one of
four categories, based on the work of Lilly (2016).
Lilly’s work was also used in Ribeiro et al. (2021),
who adapted it to create a ﬁve-part taxonomy
of manosphere subreddits by separating ‘Men’s
Rights Activists’ (MRA) into MRA and ‘The Red
Pill’ (TRP). We do not follow this distinction
because conceptually the two categories are very
similar and separating them could bias our data
collection by, in effect, oversampling from these
similar communities. To maximise the diversity of
our data we include subreddits which are topically
relevant to the four categories (listed below),
even if they are nominally dominated by groups
other than straight men (such as r/gaycel or
r/trufemcels) or are primarily concerned
with critiquing and debating the manosphere
(such
as
r/purplepilldebates
or
r/thebluepill).
• Incels (IC) Men who are opposed to, and de-
mean, insult or attack women, because they
cannot, or believe they believe cannot, get sex-
ual interest or companionship. Many such
men believe that they are entitled to female
attention.

--- Page 18 ---

• Men Going Their Own Way (MGTOW)
Men who believe that women, and feminism,
have corrupted society and that men need to
reassert themselves. Many such men can, or
believe that they can, achieve companionship
and sexual interest from women and are less
explicitly spiteful and hateful towards women,
in contrast to Incels.
• Men’s Rights Activists (MRA) Men who
typically oppose feminism, believing that
women are privileged and men are system-
atically discriminated against. MRA groups
range from moderate positions, such as ac-
tivists who want greater rights for divorced
fathers, to more extreme positions, such as ac-
tivists who want men to be given state-backed
privileges.
• Pick Up Artists (PUA) Men who actively at-
tempt to win companionship and sexual in-
terest from women, often with duplicitous or
underhand techniques. Many such men hold
derogatory views about women, and portray
them as sexual objects.
D
Bespoke Sexism Classiﬁer for Data
Sampling
In our sampling ensemble, we trained a bespoke
binary classiﬁer on English and women-targeted
entries from seven open source datasets (Zampieri
et al., 2019; Rodríguez-Sánchez et al., 2021; Vid-
gen et al., 2021b; Samory et al., 2021; Guest et al.,
2021; Fersini et al., 2018a,b). For each of these
datasets, we remove duplicates, clean white space,
and convert URLs, emoji and usernames to spe-
cial tokens (e.g., [URL]). Each dataset is labelled
according to its own taxonomy for sexism and/or
misogyny, and their structure and deﬁnitions are
not consistent. To unify the labels, we use the
binary top-level label in each dataset (either misog-
ynist vs. not misogynist; or sexist vs. not sexist).
We split the combined datasets into train and test
(90/10), stratifying by dataset source. We train a
BERT-base model with default parameters for 3
epochs, using the transformers library (Wolf et al.,
2020). The model achieves 80% Macro-F1 score
on the held-out test set. We use this model to
weakly label the presence of misogynist or sexist
content in the Gab and Reddit data.
E
Crowdworkers vs. Experts
Experiments
We used a gold standard of 200 entries to test two
alternatives for annotation. First, we launched the
gold standard on a crowdsourced annotation ser-
vice, with 7 annotations per entry, and 176 crowd-
workers. Taking the majority-voted label for Task
A, nearly all sexist entries were labelled correctly
(96%) but most non-sexist entries were mislabelled
(4% correct). Of the 57 Sexist entries, the crowd
majority-vote was 28% correct for Task B and 14%
for Task C. Second, we recruited and trained 19
self-identifying women to label the same 200 gold
standard entries. Taking the majority-voted label
for Task A, the trained annotators were correct 96%
of the time. Of the 57 Sexist entries, the trained an-
notators’ majority-vote was 84% correct for Task B
and 72% for Task C. Given the sensitivity and com-
plexity of the task, working with trained annotators
provides higher-quality labels and poses other ad-
vantages that annotator welfare can be monitored
and guidelines can be updated to address feedback.
F
Confusion Between Vectors
1.1 threats of harm
1.2. incitement/encouragement of harm
2.1 descriptive attacks
2.2 aggressive/emotion attacks
2.3 dehumanising attacks/objectification
3.1 casual gendered slurs
3.2 immutable differences/stereotypes
3.3. backhanded compliments
3.4 condescending explanations
4.1 supporting mistreatment
4.2 supporting systemic discrimination
True Vector
1.1
1.2.
2.1
2.2
2.3
3.1
3.2
3.3.
3.4
4.1
4.2
Predicted Vector
48%
3%
0%
1%
1%
1%
1%
1%
0%
0%
0%
42%
77%
1%
3%
3%
2%
1%
0%
1%
5%
3%
1%
1%
60%
9%
18%
1%
27%
20%
32%
14%
17%
1%
10%
9%
64%
9%
28%
2%
3%
0%
12%
2%
6%
2%
5%
4%
48%
2%
1%
13%
5%
7%
0%
1%
3%
2%
15%
9%
64%
2%
9%
0%
1%
4%
1%
0%
14%
1%
8%
0%
58%
17%
29%
5%
8%
0%
0%
2%
0%
3%
0%
2%
33%
1%
0%
0%
0%
1%
1%
0%
0%
0%
2%
2%
11%
1%
1%
0%
1%
1%
1%
0%
0%
0%
0%
2%
47%
2%
1%
3%
5%
2%
0%
1%
5%
2%
19%
7%
62%
Task C
Figure 4: Confusion matrix for vectors of sexism (Task
C) across the top 10 performing systems.

```
