---
title: "FairLex - PDF Extract"
source_pdf: "2022-Chalkidis-FairLex.pdf"
pages: 18
extracted_at: "2026-01-24T17:05:10.026050"
---

# PDF Extract: FairLex

**Source PDF:** 2022-Chalkidis-FairLex.pdf
**Total Pages:** 18

---

## Content

```
--- Page 1 ---

FairLex: A Multilingual Benchmark for Evaluating
Fairness in Legal Text Processing
Ilias Chalkidis †∗
Tommaso Pasini †
Sheng Zhang ⋄
Letizia Tomada ‡
Sebastian Felix Schwemer ‡
Anders Søgaard †
† Department of Computer Science, University of Copenhagen, Denmark
‡ Faculty of Law, University of Copenhagen, Denmark
⋄National University of Defense Technology, People’s Republic of China
Abstract
We present a benchmark suite of four datasets
for evaluating the fairness of pre-trained lan-
guage models and the techniques used to
ﬁne-tune them for downstream tasks.
Our
benchmarks cover four jurisdictions (Euro-
pean Council, USA, Switzerland, and China),
ﬁve languages (English, German, French, Ital-
ian and Chinese) and fairness across ﬁve at-
tributes (gender, age, region, language, and le-
gal area). In our experiments, we evaluate pre-
trained language models using several group-
robust ﬁne-tuning techniques and show that
performance group disparities are vibrant in
many cases, while none of these techniques
guarantee fairness, nor consistently mitigate
group disparities. Furthermore, we provide a
quantitative and qualitative analysis of our re-
sults, highlighting open challenges in the de-
velopment of robustness methods in legal NLP.
1
Introduction
Natural Language Processing (NLP) for law
(Chalkidis and Kampas, 2019; Aletras et al., 2019;
Zhong et al., 2020; Chalkidis et al., 2022) receives
increasing attention. Assistive technologies can
speed up legal research or discovery signiﬁcantly
assisting lawyers, judges and clerks. They can also
help legal scholars to study case law (Katz, 2012;
Coupette et al., 2021), improve access of law to
laypersons, help sociologists and research ethicists
to expose biases in the justice system (Angwin
et al., 2016; Dressel and Farid, 2018), and even
scrutinize decision-making itself (Bell et al., 2021).
In the context of law, the principle of equal-
ity and non-discrimination is of paramount impor-
tance, although its deﬁnition varies at international,
regional and domestic level. For example, EU non-
discrimination law prohibits both direct and indi-
rect discrimination. Direct discrimination occurs
when one person is treated less favourably than
∗Corresponding author: ilias.chalkidis@di.ku.dk
Figure 1: Group disparity for defendant state (C.E. Eu-
rope vs. The Rest) in ECtHR and legal area (Civil law
vs. Penal law) in FSCS.
others would be treated in comparable situations
on grounds of sex, racial or ethnic origin, disabil-
ity, sexual orientation, religion or belief and age.1
Given the gravity that legal outcomes have for indi-
viduals, assistive technologies cannot be adopted
to speed up legal research at the expense of fairness
(Wachter et al., 2021), potentially also decreasing
the trust in our legal systems (Barﬁeld, 2020).
Societal transformations perpetually shape our
legal systems. The topic deserves great attention
because AI systems learning from historical data
pose the risk of lack of generalisability beyond the
training data, and more importantly transporting
biases previously encumbered in the data in future
decision-making, thereby exponentially increasing
their eﬀect (Delacroix, 2022).
Historical legal data do not represent all groups
in our societies equally and tend to reﬂect social
biases in our societies and legal institutions. When
models are deployed in production, they may rein-
force these biases. For example, criminal justice
is already often strongly inﬂuenced by racial bias,
with people of colour being more likely to be ar-
rested and receive higher punishments than others,
both in the USA2 and in the UK.3
1An in-depth analysis of the notion of discrimination and
fairness in law is presented in Appendix A.
2https://tinyurl.com/4cse552t
3https://tinyurl.com/hkff3zcb
arXiv:2203.07228v1  [cs.CL]  14 Mar 2022

--- Page 2 ---

In recent years, the NLP and machine learning
literature has introduced fairness objectives, typ-
ically derived from the Rawlsian notion of equal
opportunities (Rawls, 1971), to evaluate the extent
to which models discriminate across protected at-
tributes. Some of these rely on notions of resource
allocation, i.e., reﬂecting the idea that groups are
treated fairly if they are equally represented in
the training data used to induce our models, or
if the same number of training iterations is per-
formed per group.
This is sometimes referred
to as the resource allocation perspective on fair-
ness (Lundgard, 2020). Contrary, there is also a
capability-centered approach to fairness (Anderson,
1999; Robeyns, 2009), in which the goal is to re-
serve enough resources per group to achieve similar
performance levels, which is ultimately what is im-
portant for how individuals are treated in legal pro-
cesses. We adopt a capability-centered approach
to fairness and deﬁne fairness in terms of perfor-
mance parity (Hashimoto et al., 2018) or equal risk
(Donini et al., 2018).4
Performance disparity (Hashimoto et al., 2018)
refers to the phenomenon of high overall perfor-
mance, but low performance on minority groups,
as a result of minimizing risk across samples (not
groups). Since some groups beneﬁt more than
others from models and technologies that exhibit
performance disparity, this likely widens gaps be-
tween those groups. Performance disparity works
against the ideal of fair and equal opportunities for
all groups in our societies. We therefore deﬁne a
fair classiﬁer as one that has similar performance
(equal risk) across all groups (Donini et al., 2018).
In sum, we adopt the view that (approximate)
equality under the law in a modern world requires
that our NLP technologies exhibit (approximately)
equal risk across sensitive attributes. For everyone
to be treated equally under the law, regardless of
race, gender, nationality, or other characteristics,
NLP assistive technologies need to be (approxi-
mately) insensitive to these attributes. We consider
three types of attributes in this work:
• Demographics: The ﬁrst category includes demo-
graphic information of the involved parties, e.g.,
the gender, sexual orientation, nationality, age, or
race of the plaintiﬀ/defendant in a case. In this
case, we aim to mitigate biases against speciﬁc
4The dominant alternative to equal risk is to deﬁne fairness
in terms of equal odds. Equal odds fairness does not guarantee
Rawlsian fairness, and often conﬂicts with the rule of law.
groups, e.g., a model performs worse for female
defendants or is biased against black defendants.
We can further consider information involving
the legal status of involved parties, e.g., person
vs. company, or private vs. public.
• Regional: The second category includes regional
information, for example the courts in charge of a
case. In this case, we aim to mitigate disparity in-
between diﬀerent regions in a given jurisdiction,
e.g., a model performs better in speciﬁc cases
originated or ruled in courts of speciﬁc regions.
• Legal Topic: The third category includes legal
topic information on the subject matter of the
controversy. In this case, we aim to mitigate
disparity in-between diﬀerent topics (areas) of
law, e.g., a model performs better in a speciﬁc
ﬁeld of law, for example penal cases.
Contributions
We introduce FairLex, a multilin-
gual fairness benchmark of four legal datasets cov-
ering four jurisdictions (Council of Europe, United
States of America, Swiss Confederation and Peo-
ple’s Republic of China), ﬁve languages (English,
German, French, Italian and Chinese) and vari-
ous sensitive attributes (gender, age, region, etc.).
We release four pre-trained transformer-based lan-
guage models, each tailored for a speciﬁc dataset
(task) within our benchmark, which can be used
as baseline models (text encoders). We conduct
experiments with several group-robust algorithms
and provide a quantitative and qualitative analysis
of our results, highlighting open challenges in the
development of robustness methods in legal NLP.
2
Related Work
Fair machine learning
The literature on induc-
ing approximately fair models from biased data
is rapidly growing. See Mehrabi et al. (2021);
Makhlouf et al. (2021); Ding et al. (2021) for recent
surveys. We rely on this literature in how we deﬁne
fairness, and for the algorithms that we compare
in our experiments below. As already discussed,
we adopt a capability-centered approach to fairness
and deﬁne fairness in terms of performance parity
(Hashimoto et al., 2018) or equal risk (Donini et al.,
2018). The fairness-promoting learning algorithms
we evaluate are discussed in detail in Section 4.
Some of these – Group Distributionally Robust Op-
timization (Sagawa et al., 2020) and Invariant Risk
Minimization (Arjovsky et al., 2020) – have previ-
ously been evaluated for fairness in the context of
hate speech (Koh et al., 2021).

--- Page 3 ---

Fairness in law
Studying fair machine learning
in the context of legal (computational) applications
has a limited history. In a classic study, Angwin
et al. (2016) analyzed the performance of the Cor-
rectional Oﬀender Management Proﬁling for Al-
ternative Sanctions (COMPAS) system, which was
used for parole risk assessment (recidivism predic-
tion) in the US. The system relied on 137 features
from questionnaires and criminal records. Angwin
et al. found that blacks were almost twice as likely
as whites to be mislabeled as high risk (of re-
oﬀending), revealing a severe racial bias in the
system. The system was later compared to crowd-
workers in Dressel and Farid (2018). These studies
relied on tabular data and did not involve text pro-
cessing (e.g., encoding case facts or decisions).
More recently, Wang et al. (2021b) studied legal
judgment consistency using a dataset of Chinese
criminal cases. They evaluated the consistency
of LSTM-based models across region and gender
and reported severe fairness gaps across gender.
They also found that the fairness gap was particular
severe for more serious crimes. Another line of
work (Rice et al., 2019; Baker Gillis, 2021; Gu-
musel et al., 2022) explores representational bias
with respect to race and gender analyzing word
latent representations trained in legal text corpora.
While we agree that representational bias can po-
tentially reinforce unfortunate biases, these may
not impact the treatment of individuals (or groups).
We therefore focus on directly measuring equal risk
on downstream applications instead.
Previous work has focused on the analysis of
speciﬁc cases, languages or algorithms, but Fair-
Lex aims at easing the development and testing of
bias-mitigation models or algorithms within the le-
gal domain. FairLex allows researchers to explore
fairness across four datasets covering four jurisdic-
tions (Council of Europe, United States of Amer-
ica, Swiss Confederation and People’s Republic of
China), ﬁve languages (English, German, French,
Italian and Chinese) and various sensitive attributes
(gender, age, region, etc.). Furthermore, we pro-
vide competitive baselines including pre-trained
transformer-based language models, adapted to the
examined datasets, and an in-dept examination of
performance of four group robust algorithms de-
scribed in detail in Section 4.
Benchmarking
NLP has been stormed by the
rapid development of benchmark datasets that aim
to evaluate the performance of pre-trained language
models with respect to diﬀerent objectives: general
Natural Language Understanding (NLU) (Wang
et al., 2019b,a), Cross-Lingual Transfer (CLT) (Hu
et al., 2020), and even domain-speciﬁc ones on
biomedical (Peng et al., 2019), or legal (Chalkidis
et al., 2022) NLP tasks. Despite their value, re-
cent work has raised criticism on several limita-
tions of the so called NLU benchmarks (Paullada
et al., 2020; Bowman and Dahl, 2021; Raji et al.,
2021). The main points are: poor (laissez-faire)
dataset development (e.g., lack of diversity, spuri-
ous correlations), legal issues (e.g., data licensing
and leakage of personal information), construct
validity (e.g., poor experimental setup, unclear re-
search questions), question of “general” capabili-
ties, and promotion of superﬁcial competitiveness
(hype, or even falsify, state-of-the-art results).
We believe that the release of FairLex, a domain-
speciﬁc (legal-oriented) benchmark suite for eval-
uating fairness, overcomes (or at least mitigates)
some of the aforementioned limitations. We in-
troduce the core motivation in Section 1, while
speciﬁc (case-by-case) details are described in Sec-
tion 3.
Our benchmark is open-ended and in-
evitably has several limitations; we report known
limitations and ethical considerations in Sections 7
and 8. Nonetheless we believe that it will help
critical research in the area of fairness.
3
Benchmark Datasets
ECtHR
The European Court of Human Rights
(ECtHR) hears allegations that a state has breached
human rights provisions of the European Conven-
tion of Human Rights (ECHR). We use the dataset
of Chalkidis et al. (2021), which contains 11K
cases from ECtHR’s public database. Each case is
mapped to articles of the ECHR that were violated
(if any). This is a multi-label text classiﬁcation task.
Given the facts of a case, the goal is to predict the
ECHR articles that were violated, if any, as decided
(ruled) by the court. The cases are chronologically
split into training (9k, 2001–16), development (1k,
2016–17), and test (1k, 2017–19) sets.
To facilitate the study of fairness of text clas-
siﬁers, we record for each case the following at-
tributes: (a) The defendant states, which are the
European states that allegedly violated the ECHR.
The defendant states for each case is a subset of the
47 Member States of the Council of Europe;5 To
have statistical support, we group defendant states
5https://www.coe.int/

--- Page 4 ---

Dataset
Original Publication
Classiﬁcation Task
No of Classes
Attributes
Attribute Type
#N
ECtHR
(Chalkidis et al., 2021)
Legal Judgment Prediction: ECHR Violation Prediction
10+1
Defendant State
2
Applicant Gender
2
Applicant Age
3
SCOTUS
(Spaeth et al., 2020)
Legal Topic Classiﬁcation: Issue Area Classiﬁcation
14
Respondent Type
4
Decision Direction
2
FSCS
(Niklaus et al., 2021)
Legal Judgment Prediction: Case Approval Prediction
2
Language
3
Region of Origin
6
Legal Area
6
CAIL
(Wang et al., 2021b)
Legal Judgment Prediction: Crime Severity Prediction
6
Defendant Gender
2
Region of Origin
7
Table 1: Main characteristics of FairLex datasets (ECtHR, SCOTUS, FSCS, CAIL). We report the examined tasks,
the number of classes, the examined attributes and the number (#N) of groups per attribute.
in two: Central-Eastern European states, on one
hand, and all other states, as classiﬁed by the Eu-
roVoc thesaurus. (b) The applicant’s age at the time
of the decision. We extract the birth year of the ap-
plicant from the case facts, if possible, and classify
its case in an age group (≤35, ≤64, or older) ; and
(c) the applicant’s gender, extracted from the facts,
if possible, based on pronouns or other gendered
words, classiﬁed in two categories (male, female).6
SCOTUS
The US Supreme Court (SCOTUS) is
the highest federal court in the United States of
America and generally hears only the most contro-
versial or otherwise complex cases which have not
been suﬃciently well solved by lower courts. We
combine information from SCOTUS opinions with
the Supreme Court DataBase (SCDB)7 (Spaeth
et al., 2020). SCDB provides metadata (e.g., date
of publication, decisions, issues, decision direc-
tions and many more) for all cases. We consider
the available 14 thematic issue areas (e.g, Criminal
Procedure, Civil Rights, Economic Activity, etc.)
as labels. This is a single-label multi-class docu-
ment classiﬁcation task. Given the court opinion,
the goal is to predict the issue area whose focus
is on the subject matter of the controversy (dis-
pute). SCOTUS contains a total of 9,262 cases
that we split chronologically into 80% for train-
ing (7.4k, 1946–1982), 10% for development (914,
1982–1991) and 10% for testing (931, 1991–2016).
From SCDB, we also use the following attributes
to study fairness: (a) the type of respondent, which
is a manual categorization of respondents (defen-
dants) in ﬁve categories (person, public entity, or-
ganization, facility and other); and (c) the direction
of the decision, i.e., whether the decision is consid-
ered liberal, or conservative, provided by SCDB.
6In Appendix B, we describe attribute extraction and group-
ing in ﬁner details for all datasets.
7http://scdb.wustl.edu
FSCS
The Federal Supreme Court of Switzer-
land (FSCS) is the last level of appeal in Switzer-
land and similarly to SCOTUS, the court generally
hears only the most controversial or otherwise com-
plex cases which have not been suﬃciently well
solved by lower courts. The court often focus only
on small parts of previous decision, where they dis-
cuss possible wrong reasoning by the lower court.
The Swiss-Judgment-Predict dataset (Niklaus et al.,
2021) contains more than 85K decisions from the
FSCS written in one of three languages (50K Ger-
man, 31K French, 4K Italian) from the years 2000
to 2020. The dataset provides labels for a sim-
pliﬁed binary (approval, dismissal) classiﬁcation
task. Given the facts of the case, the goal is to
predict if the plaintiﬀ’s request is valid or partially
valid. The cases are also chronologically split into
training (59.7k, 2000-2014), development (8.2k,
2015-2016), and test (17.4k, 2017-2020) sets.
The original dataset provides three additional
attributes: (a) the language of the FSCS written
decision, in either German, French, or Italian; (b)
the legal area of the case (e.g., public, penal law)
derived from the chambers where the decisions
were heard; and (c) the region that denotes in which
federal region was the case originated.
CAIL
The Supreme People’s Court of China is
the last level of appeal in China and considers cases
that originated from the high people’s courts con-
cerning matters of national importance. The Chi-
nese AI and Law challenge (CAIL) dataset (Xiao
et al., 2018) is a Chinese legal NLP dataset for
judgment prediction and contains over 1m crimi-
nal cases. The dataset provides labels for relevant
article of criminal code prediction, charge (type
of crime) prediction, imprisonment term (period)
prediction, and monetary penalty prediction.8
8The publication of the original dataset has been the topic
of an active debate in the NLP community (Leins et al., 2020;
Tsarapatsanis and Aletras, 2021; Bender, 2021).

--- Page 5 ---

Recently, Wang et al. (2021b) re-annotated a
subset of approx. 100k cases with demographic
attributes. Speciﬁcally the new dataset has been
annotated with: (a) the applicant’s gender, classi-
ﬁed in two categories (male, female); and (b) the
region of the court that denotes in which out of the
7 provincial-level administrative regions was the
case judged. We re-split the dataset chronologically
into training (80k, 2013-2017), development (12k,
2017-2018), and test (12k, 2018) sets. In our study,
we re-frame the imprisonment term prediction and
examine a soft version, dubbed crime severity pre-
diction task, a multi-class classiﬁcation task, where
given the facts of a case, the goal is to predict how
severe was the committed crime with respect to the
imprisonment term. We approximate crime sever-
ity by the length of imprisonment term, split in 6
clusters (0, ≤12, ≤36, ≤60, ≤120, >120 months).
4
Fine-tuning Algorithms
Across experiments, our main goal is to ﬁnd a hy-
pothesis for which the risk R(h) is minimal:
h∗= arg min
h∈H R(h)
(1)
R(h) = E(L(h(x), y))
(2)
where y are the targets (ground truth) and h(x) = ˆy
is the system hypothesis (model’s predictions).
Similar to previous studies, R(h) is an expecta-
tion of the selected loss function (L). In this work,
we study multi-label text classiﬁcation (Section 3),
thus we aim to minimize the binary cross-entropy
loss across L classes:
L = −y log ˆy −(1 −y) log(1 −ˆy)
(3)
ERM (Vapnik, 1992), which stands for Empirical
Risk Minimization, is the most standard and widely
used optimization technique to train neural meth-
ods. The loss is calculated as follows:
LERM =
N
X
i=1
Li
N
(4)
where N is the number of instances (training exam-
ples) in a batch, and Li is the loss per instance.
Besides ERM, we also consider a representative
selection of group-robust ﬁne-tuning algorithms
which aims at mitigating performance disparities
with respect to a given attribute (A), e.g., the gender
of the applicant or the region of the court. Each
attribute is split into G groups, i.e., male/female for
gender. All algorithms rely on a balanced group
sampler, i.e., an equal number of instances (sam-
ples) per group (NG) are included in each batch.
Most of the algorithms are built upon group-wise
losses (Lg), computed as follows:
L(gi) = 1
Ngi
Ngi
X
j=1
L(xj)
(5)
Group DRO (Sagawa et al., 2020),
stands
for Group Distributionally Robust Optimization
(DRO). Group DRO is an extension of the Group
Uniform algorithm, where the group-wise losses
are weighted inversely proportional to the group
training performance. The total loss is:
LDRO =
G
X
i=1
wgi ∗L(gi), where
(6)
wgi = 1
W ( ˆwgi ∗eL(gi))
and
W =
G
X
i=1
wgi
(7)
where G is the number of groups (labels), Lg are
the averaged group-wise (label-wise) losses, wg
are the group (label) weights, ˆwg are the group
(label) weights as computed in the previous update
step. Initially the weight mass in equally distributed
across groups.
V-REx (Krueger et al., 2020), which stands for
Risk Extrapolation, is yet another proposed group-
robust optimization algorithm.
Krueger et al.
(2020) hypothesize that variation across training
groups is representative of the variation later en-
countered at test time, so they also consider the
variance across the group-wise losses. In V-REx
the total loss is calculated as follows:
LREX = LERM + λ ∗Var([Lg1, . . . , LgG])
(8)
where Var is the variance among the group-wise
losses and λ, a weighting hyper-parameter scalar.
IRM (Arjovsky et al., 2020), which stands for In-
variant Risk Minimization, mainly aims to penalize
variance across multiple training dummy estima-
tors across groups, i.e., performance cannot vary
in samples that correspond to the same group. The
total loss is computed as follows:
LIRM = 1
G

G
X
i=1
L(gi) + λ ∗P(gi)

(9)
Please refer to Arjovsky et al. (2020) for the
deﬁnition of the group penalty terms (Pg).

--- Page 6 ---

Adversarial Removal (Elazar and Goldberg,
2018) algorithm mitigates group disparities by
means of an additional adversarial classiﬁer (Good-
fellow et al., 2014). The adversarial classiﬁer share
the encoder with the main network and is trained
to predict the protected attribute (A) of an instance.
The total loss factors in the adversarial one, thus
penalizing the model when it is able to discriminate
groups. Formally, the total loss is calculated as:
LAR = LERM −λ ∗LADV
(10)
LADV = L(ˆgi, gi)
(11)
where ˆgi is the adversarial classiﬁer’s prediction for
the examined attribute A (in which group (gi) of A,
does the example belong to) given the input (x).
5
Experimental Setup
Models
Since we are interested in classifying
long documents (up to 6000 tokens per document,
see Figure 2 in Appendix E.1), we use a hierarchi-
cal BERT-based model similar to that of Chalkidis
et al. (2021), so as to avoid using only the ﬁrst
512 tokens of a text. The hierarchical model, ﬁrst,
encodes the text through a pre-trained Transformer-
based model, thus representing each paragraph
independently with the [CLS] token. Then, the
paragraph representations are fed into a two-layers
transformer encoder with the exact same speciﬁca-
tions of the ﬁrst one (e.g., hidden units, number of
attention heads), so as to contextualize them, i.e.,
it makes paragraphs representations aware of the
surrounding paragraphs. Finally, the model max-
pools the context-aware paragraph representations
computing the document-level representation and
feed it to a classiﬁcation layer.
For the purpose of this work, we release four
domain-speciﬁc BERT models with continued pre-
training on the corpora of the examined datasets.9
We train mini-sized BERT models with 6 Trans-
former blocks, 384 hidden units, and 12 attention
heads. We warm-start all models from the pub-
lic MiniLMv2 models checkpoints (Wang et al.,
2021a) using the distilled version of RoBERTa (Liu
et al., 2019) for the English datasets (ECtHR, SCO-
TUS) and the one distilled from XLM-R (Conneau
et al., 2020) for the rest (trilingual FSCS, and Chi-
nese CAIL). Given the limited size of these models,
we can eﬀectively use up to 4096 tokens in ECtHR
and SCOTUS and up to 2048 tokens in FSCS and
9https://huggingface.co/coastalcph
CAIL for up to 16 samples per batch in a 24GB
GPU card.10 For completeness, we also consider
linear Bag-of Words (BoW) classiﬁers using TF-
IDF scores of the most frequent n-grams (where
n = 1, 2, 3) in the training corpus of each dataset.
Data Repository and Code
We release a uni-
ﬁed version of the benchmark on Hugging Face
Datasets (Lhoest et al., 2021).11 In our experi-
ments, we use and extend the WILDs (Koh et al.,
2021) library. For reproducibility and further explo-
ration with new group-robust methods, we release
our code on Github.12
Evaluation Details
Across experiments we com-
pute the macro-F1 score per group (mF1i), exclud-
ing the group of unidentiﬁed instances, if any.13
We report macro-F1 to avoid bias toward majority
classes because of class imbalance and skewed la-
bel distributions across train, development, and test
subsets (Søgaard et al., 2021).
6
Results
Main Results
In Table 2, we report the group
performance (mF1), where models trained with the
ERM algorithm, across all datasets and attributes.
We observe that the intensity of group disparities
vary a lot between diﬀerent attributes, but in many
cases the group disparities are very vibrant.
For example, in ECtHR, we observe substantial
group disparity between the two defendant state
groups (21.5% absolute diﬀerence), similarly for
applicant’s gender groups (16.2% absolute diﬀer-
ence). In FSCS, we observe language disparity,
where performance is on average 3-5% lower for
cases written in Italian compared to those written in
French and German. Performance disparity is even
higher with respect to legal areas, where the model
has the best performance for criminal (penal law)
cases (83.4%) compared to others (approx. 10-20%
lower). We also observe substantial group dispar-
ities with respect to the court region, e.g., cases
ruled in E. Switzerland courts (66.8%) compared
to Federation courts (56.4%). The same applies for
CAIL, e.g., cases ruled in Beijing courts (66.8%)
compared to Sichuan courts (56.4%).
10This is particularly important for group-robust algorithms
that consider group-wise losses.
11https://huggingface.co/datasets/coastalcph/
fairlex
12https://github.com/coastalcph/fairlex
13The group of unidentiﬁed instances includes the instances,
where the value of the examined attribute is unidentiﬁable
(unknown). See details in Appendices B, and E.2.

--- Page 7 ---

ECtHR (ECHR Violation Prediction)
Group
mF1
#train-cases (%) (↑)
LDKL (↓)
WCI (↓)
Defendant State
E.C. European
70.2
7,224 (80%)
0.17
0.07
The Rest
48.7
1,776 (20%)
0.28
0.57
Applicant Gender
Male
54.4
4,187 (77%)
0.17
0.18
Female
60.6
1,507 (23%)
0.26
0.19
Applicant Age
≤65 years
59.7
4279 (68%)
0.18
0.15
> 65 years
56.5
1130 (18%)
0.32
0.26
≤35 years
46.2
868 (14%)
0.19
0.12
SCOTUS (Issue Area Classiﬁcation)
Group
mF1
#train-cases (%) (↑)
LDKL (↓)
WCI (↓)
Respondent Type
Public Entity
77.4
2796 (51%)
0.07
0.04
Person
74.9
1847 (34%)
0.05
0.03
Organization
81.1
741 (13%)
0.11
0.03
Facility
80.7
140 (3%)
0.26
0.06
Direction
Liberal
76.2
3335 (52%)
0.04
0.08
Conservative
80.8
3146 (48%)
0.05
0.17
FSCS (Case Approval Prediction)
Group
mF1
#train-cases (%) (↑)
LDKL (↓)
WCI (↓)
Language
German
68.2
35458 (60%)
0.03
0.20
French
70.6
21179 (35%)
0.03
0.19
Italian
65.2
3072 (5%)
0.04
0.19
Legal Area
Public law
56.9
15173 (31%)
~0.00
0.20
Penal law
83.4
11795 (25%)
~0.00
0.20
Civil law
66.4
11477 (24%)
0.02
0.16
Social Law
70.8
9727 (20%)
0.06
0.20
Region
R. Lémanique
71.3
13436 (27%)
0.04
0.20
Zürich
68.5
8788 (18%)
0.04
0.18
E. Mittelland
69.8
8257 (17%)
0.08
0.16
E. Switzerland
73.6
5707 (12%)
0.02
0.24
N.W. Switzerland
72.8
5655 (11%)
0.03
0.19
C. Switzerland
69.5
4779 (10%)
0.03
0.19
Ticino
68.3
2255 (6%)
~0.00
0.17
Federation
63.9
1308 (3%)
~0.00
0.27
CAIL (Crime Severity Prediction)
Group
mF1
#train-cases (%) (↑)
LDKL (↓)
WCI (↓)
Defendant Gender
Male
60.3
73952 (92%)
0.03
0.01
Female
60.1
6048 (8%)
0.08
0.03
Region
Beijing
66.8
16588 (21%)
0.05
0.02
Liaoning
56.7
13934 (17%)
0.05
0.02
Hunan
59.5
12760 (16%)
0.05
0.02
Guangdong
58.0
12278 (15%)
0.05
0.01
Sichuan
56.4
11606 (14%)
0.06
0.02
Guangxi
58.9
8674 (11%)
0.07
0.02
Zhejiang
58.8
4160 (5%)
0.07
0.02
Table 2: Statistics for the three general (attribute agnos-
tic) cross-examined factors (representation inequality,
temporal concept drift, and worst-class inﬂuence), as
introduced in Section 6. We highlight the worst and
best performing group per attribute. In boldface, we
highlight the best (less harmful) value per factor across
groups. Performance (mF1) reported for ERM.
Group Disparity Analysis
Moving forward we
try to identify general (attribute agnostic) factors
based on data distributions that could potentially
lead to performance disparity across groups. We
identify three general (attribute agnostic) factors:
• Representation Inequality: Not all groups are
equally represented in the training set. To exam-
ine this aspect, we report the number of training
cases per group.
• Temporal Concept Drift: The label distribution
for a given group changes over time, i.e., in-
between training and test subsets. To examine
this aspect, we report per group, the KL diver-
gence in-between the training and test label dis-
tribution.
• Worst Class Inﬂuence: The performance is not
equal across labels (classes), which may dis-
proportionally aﬀect the macro-averaged perfor-
mance across groups. To examine this aspect, we
report the Worst Class Inﬂuence (WCI) score per
group, which is computed as follows:
WCI(i) = #test-cases (worst-class)
#test-cases
(12)
In Table 2, we present the results across all at-
tributes. We observe that only in 4 out of 10 cases
(attributes), the less represented groups are those
with the worst performance compared to the rest.
It is generally not the case that high KL divergence
(drift) correlates with low performance. In other
words, group disparities does not seem to be driven
by temporal concept drift. Finally, the inﬂuence of
the worst class is relatively uniform across groups
in most cases, but in the cases where groups diﬀer
in this regard, worst class inﬂuence correlates with
error in 2 out of 3 cases.14
In ECtHR, considering performance across de-
fendant state, we see that all the three factors corre-
late internally, i.e., the worst performing group is
less represented, has higher temporal drift and has
more cases in the worst performing class. This is
not the case considering performance across other
attributes. It is also not the case for SCOTUS.
In FSCS, considering the attributes of language
and region, representation inequality seems to be
an important factor that leads to group disparity.
This is not the case for legal area, where the best
14For ECtHR performance across defendant states and SCO-
TUS across directions, but not for ECtHR performance across
applicant age.

--- Page 8 ---

ECtHR (A1: Defendant State)
Group (A2)
E.C.E.
Rest
Avg.
Male
55.8
35.1
54.4
Female
61.3
47.1
60.6
≤35
48.1
44.2
46.2
≤65
61.0
34.7
59.7
FSCS (A1: Legal Area)
Group (A2)
Public Law
Penal Law
Avg.
French
57.4
82.4
70.6
Italian
56.2
69.4
65.2
E. Switzerland
55.9
87.0
73.6
Federation
54.5
72.8
63.9
Table 3:
Results in cross-attribute inﬂuence.
mF1
scores for pairings of groups for attributes (A1, A2).
represented group is the worst performing group.
In other words, there are other reasons that lead
to performance disparity in this case; according
to Niklaus et al. (2021), a potential factor is that
the jurisprudence in penal law is more united and
aligned in Switzerland and outlier judgments are
rarer making the task more predictable.
Cross-Attribute Inﬂuence Analysis
We have
evaluated fairness across attributes that are not nec-
essarily independent of each other. We therefore
evaluate the extent to which performance dispar-
ities along diﬀerent attributes correlate, i.e., how
attributes interact, and whether performance diﬀer-
ences for attribute A1 can potentially explain per-
formance diﬀerences for another attribute A2. We
examine this for the two attributes with the highest
group disparity: the defendant state in ECtHR, and
the legal area in FSCS. For the bins induced by
these two attributes (A1), we compute mF1 scores
across other attributes (A2).
In ECtHR, approx. 83% and 81% of male and
women applicants are involved in cases against E.C.
European states (best-performing group). Simi-
larly, in case of age groups, we observe that ratio of
cases against E.C. European states is: 87% and 86%
for ≤65 and ≤35, the best- and worst-performing
groups respectively. In FSCS, the ratio of cases rel-
evant to penal law is: approx. 29%, and 41% writ-
ten in written in French (best-performing group)
and Italian (worst-performing group). Similarly,
approx. 27% originated in E. Switzerland (best-
performing group) and 42% in Federation (worst
performing group) are relevant to public law. In
both attributes, there is a 15% increase of cases rel-
evant to public law for the worst performing groups.
In other words, the group disparity in one attribute
A2 (language, region) could be also explained by
the inﬂuence of another attribute A1 (legal area).
In Table 3, we report the performance in the
aforementioned cross-attribute (A1, A2) pairings.
With the exception of the (age, defendant state)
cross-examination in ECtHR, we observe that
group disparities in attribute A2 (Table 2) are con-
sistent across groups of the plausible inﬂuencer (i.e.
attribute A1). Hence, cross-attribute inﬂuence does
not explain the observed group disparities.
We believe that such an in-depth analysis of the
results is fundamental to understand the inﬂuence
of diﬀerent factors in the outcomes. This analysis
wouldn’t be possible, if we had “counterfeited” an
ideal scenario, where all groups and labels where
equally represented. While a controlled experi-
mental environment is frequently used to examine
speciﬁc factors, it could hide, or partially allevi-
ate such phenomena, hence producing misleading
results on fairness of the examined models.
Group Robust Algorithms Results
Finally, we
evaluate the performance for several group robust
algorithms ( Section 4) that could potentially mit-
igate group disparities. To estimate their perfor-
mance, we report the average macro-F1 across
groups (mF1) and the group disparity (GD) among
groups measured as the group-wise std dev.:
GD =
v
u
t
1
G
G
X
i=1
(mF1i −mF1)2
(13)
We also report the worst-group performance
(mF1W = min([mF11, mF12, . . . mF1G)).
In Table 4, we report the results of all our base-
lines on the four datasets introduced in this paper.
We ﬁrst observe that the results of linear classi-
ﬁers trained with the ERM algorithm (top row per
dataset) are consistently worse (lower average and
worst-case performance, higher group disparity)
compared to transformed-based models in the same
setting. In other words linear classiﬁer have lower
overall performance, while being less fair with re-
spect to the applied deﬁnition of fairness (i.e. equal
performance across groups).
As one can see, transformer-based models
trained with the ERM algorithm, i.e., without tak-
ing into account information about groups and their
distribution, perform either better on in the same
ballpark than models trained with methods special-
ized to mitigate biases (Section 4), with an aver-
age loss of 0.17% only in terms of mF1 and of
0.78% in terms of mF1W. While, these algorithms
improve worst case performance in the literature,

--- Page 9 ---

ECtHR (ECHR Violation Prediction)
SCOTUS (Issue Area Classiﬁcation)
Algorithm
Defendant State
Applicant Gender
Applicant Age
Respondent Type
Direction
↑mF1
↓GD
↑mF1W
↑mF1
↓GD
↑mF1W
↑mF1
↓GD
↑mF1W
↑mF1
↓GD
↑mF1W
↑mF1
↓GD
↑mF1W
Bag-of-Words Linear Classifier
ERM
46.8
3.0
43.8
44.1
4.9
40.6
46.9
6.3
40.9
73.8
6.6
61.8
77.5
2.6
74.9
Transformer-based Classifier
ERM
53.2
8.3
44.9
57.5
3.1
54.4
54.1
5.9
46.2
75.1
4.0
70.8
78.1
1.6
76.6
ERM+GS
54.4
5.5
48.9
57.8
3.3
54.5
56.0
5.6
48.7
75.2
3.9
70.9
77.1
1.3
76.0
ADV-R
53.8
5.8
47.9
54.6
3.2
51.5
48.9
6.1
40.6
56.9
4.7
53.1
41.0
0.8
40.3
G-DRO
55.0
5.2
49.8
56.3
1.9
55.0
52.6
6.2
44.3
74.5
3.3
71.6
77.1
1.7
75.4
IRM
53.8
5.7
48.1
53.8
2.3
52.5
54.8
4.4
49.5
73.4
4.8
68.2
78.1
2.7
75.4
V-REx
54.6
6.3
48.3
54.6
2.0
53.2
55.0
4.5
49.8
73.8
3.8
68.2
78.2
1.1
77.1
FSCS (Case Approval Prediction)
CAIL (Crime Severity Prediction)
Algorithm
Language
Legal Area
Region
Defendant Gender
Region
↑mF1
↓GD
↑mF1W
↑mF1
↓GD
↑mF1W
↑mF1
↓GD
↑mF1W
↑mF1
↓GD
↑mF1W
↑mF1
↓GD
↑mF1W
Bag-of-Words Linear Classifier
ERM
55.5
6.2
46.8
54.4
9.7
40.9
56.8
5.0
46.6
33.5
0.7
32.8
31.7
5.0
25.5
Transformer-based Classifier
ERM
67.8
2.1
65.0
69.4
9.6
56.9
69.7
2.9
63.9
60.2
0.6
60.1
59.3
3.5
56.4
ERM+GS
66.4
3.5
61.7
67.1
9.3
55.5
67.9
3.0
62.3
59.4
0.7
59.1
58.2
3.1
55.9
ADV-R
62.6
5.1
59.0
65.6
12.4
50.0
67.4
3.2
61.5
53.3
1.3
52.1
53.5
2.5
50.8
G-DRO
70.5
0.6
69.9
57.5
5.6
52.6
67.7
4.2
60.2
59.2
1.3
57.9
58.9
3.7
55.7
IRM
68.3
1.9
66.7
67.8
9.5
55.8
68.7
3.0
63.2
56.4
1.5
55.7
58.0
3.1
54.9
V-REx
67.2
3.5
62.4
66.6
8.9
56.0
68.4
3.1
62.4
58.5
0.7
58.3
58.6
3.3
54.4
Table 4: Test results for all examined group-robust algorithms per dataset attribute. We report the average perfor-
mance across groups (mF1), the group disparity among groups (GD), and the worst-group performance (mF1W).
↑denotes that higher scores are better, while ↓denotes that lower scores are better.
when applied in a controlled experimental environ-
ment, they fail in a more realistic setting, where
both groups across attributes and labels are imbal-
anced, while also both group and label distribution
change over time. Furthermore, we cannot identify
one algorithm that performs better across datasets
and group with respect to the others, indeed results
are quite mixed without any recognizable pattern.
7
Limitations
The current version of FairLex covers a very small
fraction of legal applications, jurisdictions, and pro-
tected attributes. Our benchmark is open-ended
and inevitably cannot cover “everything in the
whole wide (legal) world” (Raji et al., 2021), but
nonetheless we believe that the published resources
will help critical research in the area of fairness.
Some protected attributes within our datasets are
extracted automatically, i.e., the gender and the
age in the ECtHR dataset, if possible, by means of
regular expressions, or manually clustered by the
authors, such as the defendant state in the ECtHR
dataset and the respondent attribute in the SCO-
TUS dataset. Various simpliﬁcations made, e.g, the
binarization of gender, would be inappropriate in
real-world applications.
Another important limitation is that what is con-
sidered the ground truth in these datasets (with the
exception of SCOTUS) is only ground truth rela-
tive to judges’ interpretation of a speciﬁc (EC, US,
Swiss, Chinese) jurisdiction and legal framework.
The labeling is therefore somewhat subjective for
non-trivial cases, and its validity is only relative to
a given legal framework. We of course do not in
any way endorse the legal standards or framework
of the examined datasets.
8
Conclusions
We introduced FairLex, a multi-lingual benchmark
suite for the development and testing of models
and bias-mitigation algorithms within the legal do-
main, based on four datasets covering four juris-
dictions, ﬁve languages and various sensitive at-
tributes. Furthermore, we provided competitive
baselines including transformer-based language
models adapted to the examined datasets, and ex-
amination of performance of four group robust
algorithms (Adversarial Removal, IRM, Group
DRO, and V-REx). While, these algorithms im-
prove worst case performance in the literature,
when applied in a controlled experimental envi-
ronment, they fail in a more realistic setting, where
both groups across attributes, and labels are imbal-
anced, while also both group and label distributions
change over time. Furthermore, we cannot iden-
tify a single algorithm that performs better across
datasets and groups compared to the rest.
In future work, we aim to further expand the
benchmark with more datasets that could possibly
cover more sensitive attributes. Further analysis on
the reasons behind group disparities, e.g., represen-
tational bias, systemic bias, is also critical.

--- Page 10 ---

Ethics Statement
Social Impact of Dataset
The scope of this work is to provide an evalua-
tion framework along with extensive experiments
to further study fairness within the legal domain.
Following the work of Angwin et al. (2016), Dres-
sel and Farid (2018), and Wang et al. (2021b),
we provide a diverse benchmark covering multi-
ple tasks, jurisdictions, and protected (examined)
attributes. We conduct experiments based on pre-
trained transformer-based language models and
compare model performance across four represen-
tative group-robust algorithm, i.e., Adversarial Re-
moval (Elazar and Goldberg, 2018), Group DRO
(Sagawa et al., 2020), IRM (Arjovsky et al., 2020)
and REx (Krueger et al., 2020).
We believe that this work can inform and help
practitioners to build assisting technology for legal
professionals - with respect to the legal framework
(jurisdiction) they operate -; technology that does
not only rely on performance on majority groups,
but also considering minorities and the robustness
of the developed models across them. We believe
that this is an important application ﬁeld, where
more research should be conducted (Tsarapatsa-
nis and Aletras, 2021) in order to improve legal
services and democratize law, but more impor-
tantly highlight (inform the audience on) the vari-
ous multi-aspect shortcomings seeking a responsi-
ble and ethical (fair) deployment of technology.
Credit Attribution / Licensing
We standardize and put together four datasets:
ECtHR (Chalkidis et al., 2021), SCOTUS (Spaeth
et al., 2020), FSCS (Niklaus et al., 2021), and CAIL
(Xiao et al., 2018; Wang et al., 2021b) that are al-
ready publicly available under CC-BY-(NC-)SA-
4.0 licenses. We release the compiled version of
the dataset under a CC-BY-NC-SA-4.0 license to
favor academic research, and forbid to the best of
our ability potential commercial dual use.15 All
datasets, except SCOTUS, are publicly available
and have been previously published. If datasets
or the papers where they were introduced in were
not compiled or written by ourselves, we have ref-
erenced the original work and encourage FairLex
users to do so as well. In fact, we believe that
this work should only be referenced, in addition
to citing the original work, when jointly experi-
15https://creativecommons.org/licenses/
by-nc-sa/4.0/
menting with multiple FairLex datasets and using
the FairLex evaluation framework and infrastruc-
ture, or use any newly introduced annotations (EC-
tHR, SCOTUS). Otherwise only the original work
should be cited.
Personal Information
The data is in general partially anonymized in
accordance with the applicable national law. The
data is considered to be in the public sphere from
a privacy perspective. This is a very sensitive mat-
ter, as the courts try to keep a balance between
transparency (the public’s right to know) and pri-
vacy (respect for private and family life). ECtHR
cases are partially annonymized by the court. Its
data is processed and made public in accordance
with the European data protection laws. SCOTUS
cases may also contain personal information and
the data is processed and made available by the
US Supreme Court, whose proceedings are public.
While this ensures compliance with US law, it is
very likely that similarly to the ECtHR any process-
ing could be justiﬁed by either implied consent or
legitimate interest under European law. In FSCS,
the names of the parties have been redacted by the
courts according to the oﬃcial guidelines. CAIL
cases are also partially anonymized by the courts
according to the courts’ policy. Its data is processed
and made public in accordance with Chinese Law.
Acknowledgments
This work is fully funded by the Innovation Fund
Denmark (IFD)16 under File No. 0175-00011A.
We would like to thank the authors of the origi-
nal datasets for providing access to the original
documents, metadata, or conﬁdentially sharing pre-
released versions of the datasets.
References
Nikolaos Aletras, Elliott Ash, Leslie Barrett, Daniel
Chen, Adam Meyers, Daniel Preotiuc-Pietro, David
Rosenberg, and Amanda Stent, editors. 2019. Pro-
ceedings of the 1st Natural Legal Language Process-
ing Workshop at NAACL 2019. Minneapolis, Min-
nesota.
Elizabeth Anderson. 1999. What is the point of equal-
ity? Ethics, 109(2).
Julia Angwin, JeﬀLarson, Surya Mattu, and Lauren
Kirchner. 2016.
Machine bias: There’s software
16https://innovationsfonden.dk/en

--- Page 11 ---

used across the country to predict future criminals.
and it’s biased against blacks. ProPublica.
Martin Arjovsky, Léon Bottou, Ishaan Gulrajani, and
David Lopez-Paz. 2020. Invariant Risk Minimiza-
tion.
Noa Baker Gillis. 2021. Sexism in the judiciary: The
importance of bias deﬁnition in NLP and in our
courts. In Proceedings of the 3rd Workshop on Gen-
der Bias in Natural Language Processing, pages 45–
54, Online. Association for Computational Linguis-
tics.
Woodrow Barﬁeld. 2020. The Cambridge Handbook of
the Law of Algorithms. Cambridge Law Handbooks.
Cambridge University Press.
Kristen Bell, Jenny Hong, Nick McKeown, and Catalin
Voss. 2021. The Recon Approach: A New Direction
for Machine Learning in Criminal Law. Berkeley
Technology Law Journal, 37.
Emily M. Bender. 2021.
On academic freedom
and ethics review:
Continuing the conversation.
Medium.
Samuel R. Bowman and George Dahl. 2021. What will
it take to ﬁx benchmarking in natural language un-
derstanding?
In Proceedings of the 2021 Confer-
ence of the North American Chapter of the Associ-
ation for Computational Linguistics: Human Lan-
guage Technologies, pages 4843–4855, Online. As-
sociation for Computational Linguistics.
Ilias Chalkidis, Manos Fergadiotis, Dimitrios Tsarapat-
sanis, Nikolaos Aletras, Ion Androutsopoulos, and
Prodromos Malakasiotis. 2021. Paragraph-level ra-
tionale extraction through regularization: A case
study on European court of human rights cases. In
Proceedings of the 2021 Conference of the North
American Chapter of the Association for Computa-
tional Linguistics: Human Language Technologies,
pages 226–241, Online. Association for Computa-
tional Linguistics.
Ilias Chalkidis, Abhik Jana, Dirk Hartung, Michael
Bommarito, Ion Androutsopoulos, Daniel Martin
Katz, and Nikolaos Aletras. 2022.
Lexglue:
A
benchmark dataset for legal language understanding
in english. In Proceedings of the 60th Annual Meet-
ing of the Association for Computational Linguistics,
Dubln, Ireland.
Ilias Chalkidis and Dimitrios Kampas. 2019.
Deep
learning in law: Early adaptation and legal word em-
beddings trained on large corpora. Artiﬁcial Intelli-
gence and Law, 27(2):171–198.
Alexis Conneau, Kartikay Khandelwal, Naman Goyal,
Vishrav Chaudhary, Guillaume Wenzek, Francisco
Guzmán, Edouard Grave, Myle Ott, Luke Zettle-
moyer, and Veselin Stoyanov. 2020. Unsupervised
cross-lingual representation learning at scale.
In
Proceedings of the 58th Annual Meeting of the Asso-
ciation for Computational Linguistics, pages 8440–
8451, Online. Association for Computational Lin-
guistics.
Corinna Coupette, Janis Beckedorf, Dirk Hartung,
Michael Bommarito, and Daniel Martin Katz. 2021.
Measuring law over time:
A network analytical
framework with an application to statutes and regu-
lations in the United States and Germany. Frontiers
in Physics, 9:269.
Sylvie Delacroix. 2022.
Diachronic interpretability
and machine learning systems.
Journal of Cross-
disciplinary Research in Computational Law, 1(1).
Frances Ding, Moritz Hardt, John Miller, and Ludwig
Schmidt. 2021. Retiring adult: New datasets for fair
machine learning. In Advances in Neural Informa-
tion Processing Systems.
Michele Donini, Luca Oneto, Shai Ben-David, John S
Shawe-Taylor, and Massimiliano Pontil. 2018. Em-
pirical risk minimization under fairness constraints.
In Advances in Neural Information Processing Sys-
tems, volume 31. Curran Associates, Inc.
Julia Dressel and Hany Farid. 2018. The accuracy, fair-
ness, and limits of predicting recidivism. Science
Advances, 4(10).
Yanai Elazar and Yoav Goldberg. 2018. Adversarial
removal of demographic attributes from text data.
In Proceedings of the 2018 Conference on Empiri-
cal Methods in Natural Language Processing, pages
11–21, Brussels, Belgium. Association for Computa-
tional Linguistics.
Sandra Fredman. 2016. Substantive equality revisited.
I-CON Oxford Legal Studies, 14:712—-773.
Janneke Gerards and Raphaële Xenedis. 2020.
Al-
gorithmic discrimination in europe:
challenges
and opportunities for gender equality and non-
discrimination law.
Ian J. Goodfellow, Jean Pouget-Abadie, Mehdi Mirza,
Bing Xu, David Warde-Farley, Sherjil Ozair, Aaron
Courville, and Yoshua Bengio. 2014. Generative ad-
versarial networks. In Advances in Neural Informa-
tion Processing Systems.
Ece Gumusel, Vincent Quirante Malic, Devan Ray
Donaldson, Kevin Ashley, and Xiaozhong Liu. 2022.
An annotation schema for the detection of social bias
in legal text corpora.
In Information for a Better
World: Shaping the Global Future, pages 185–194,
Cham. Springer International Publishing.
Tatsunori Hashimoto, Megha Srivastava, Hongseok
Namkoong, and Percy Liang. 2018. Fairness with-
out demographics in repeated loss minimization. In
Proceedings of the 35th International Conference on
Machine Learning, volume 80 of Proceedings of Ma-
chine Learning Research, pages 1929–1938, Stock-
holmsmässan, Stockholm Sweden. PMLR.

--- Page 12 ---

Junjie Hu, Sebastian Ruder, Aditya Siddhant, Gra-
ham Neubig, Orhan Firat, and Melvin Johnson.
2020. Xtreme: A massively multilingual multi-task
benchmark for evaluating cross-lingual generaliza-
tion. CoRR, abs/2003.11080.
Daniel Martin Katz. 2012.
Quantitative legal
prediction-or-how I learned to stop worrying and
start preparing for the data-driven future of the legal
services industry. Emory Law Journal, 62:909.
Jon M. Kleinberg, Jens Ludwig, Sendhil Mullainathan,
and Cass R. Sunstein. 2019. Discrimination in the
age of algorithms. CoRR, abs/1902.03731.
Pang
Wei
Koh,
Shiori
Sagawa,
Henrik
Mark-
lund, Sang Michael Xie, Marvin Zhang, Akshay
Balsubramani, Weihua Hu, Michihiro Yasunaga,
Richard Lanas Phillips, Irena Gao, Tony Lee, Eti-
enne David, Ian Stavness, Wei Guo, Berton A. Earn-
shaw, Imran S. Haque, Sara Beery, Jure Leskovec,
Anshul Kundaje, Emma Pierson, Sergey Levine,
Chelsea Finn, and Percy Liang. 2021.
WILDS:
A benchmark of in-the-wild distribution shifts. In
International Conference on Machine Learning
(ICML).
David Krueger, Ethan Caballero, Jörn-Henrik Jacobsen,
Amy Zhang, Jonathan Binas, Rémi Le Priol, and
Aaron C. Courville. 2020. Out-of-Distribution Gen-
eralization via Risk Extrapolation (REx). CoRR.
Kobi Leins, Jey Han Lau, and Timothy Baldwin. 2020.
Give me convenience and give her death:
Who
should decide what uses of NLP are appropriate, and
on what basis? In Proceedings of the 58th Annual
Meeting of the Association for Computational Lin-
guistics, pages 2908–2913, Online. Association for
Computational Linguistics.
Quentin Lhoest, Albert Villanova del Moral, Yacine
Jernite, Abhishek Thakur, Patrick von Platen, Suraj
Patil, Julien Chaumond, Mariama Drame, Julien Plu,
Lewis Tunstall, Joe Davison, Mario Šaško, Gun-
jan Chhablani, Bhavitvya Malik, Simon Brandeis,
Teven Le Scao, Victor Sanh, Canwen Xu, Nicolas
Patry, Angelina McMillan-Major, Philipp Schmid,
Sylvain Gugger, Clément Delangue, Théo Matus-
sière, Lysandre Debut, Stas Bekman, Pierric Cistac,
Thibault Goehringer, Victor Mustar, François Lagu-
nas, Alexander M. Rush, and Thomas Wolf. 2021.
Datasets: A community library for natural language
processing.
Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Man-
dar Joshi, Danqi Chen, Omer Levy, Mike Lewis,
Luke Zettlemoyer, and Veselin Stoyanov. 2019.
Roberta: A robustly optimized BERT pretraining ap-
proach. CoRR, abs/1907.11692.
Ilya Loshchilov and Frank Hutter. 2019.
Decoupled
weight decay regularization. In International Con-
ference on Learning Representations.
Alan Lundgard. 2020. Measuring justice in machine
learning. In Proceedings of the 2020 Conference on
Fairness, Accountability, and Transparency, FAT*
’20, page 680, New York, NY, USA. Association for
Computing Machinery.
Karima
Makhlouf,
Sami
Zhioua,
and
Catuscia
Palamidessi. 2021. On the applicability of machine
learning fairness notions. SIGKDD Explor. Newsl.,
23(1):14–23.
Ninareh Mehrabi, Fred Morstatter, Nripsuta Saxena,
Kristina Lerman, and Aram Galstyan. 2021. A sur-
vey on bias and fairness in machine learning. ACM
Comput. Surv., 54(6).
Joel Niklaus, Ilias Chalkidis, and Matthias Stürmer.
2021.
Swiss-judgment-prediction: A multilingual
legal judgment prediction benchmark. In Proceed-
ings of the Natural Legal Language Processing
Workshop 2021, pages 19–35, Punta Cana, Domini-
can Republic. Association for Computational Lin-
guistics.
Amandalynne
Paullada,
Inioluwa
Deborah
Raji,
Emily M. Bender, Emily Denton, and Alex Hanna.
2020.
Data and its (dis)contents:
A survey of
dataset development and use in machine learning
research. CoRR, abs/2012.05345.
Yifan Peng, Shankai Yan, and Zhiyong Lu. 2019.
Transfer learning in biomedical natural language
processing: An evaluation of bert and elmo on ten
benchmarking datasets. In Proceedings of the 2019
Workshop on Biomedical Natural Language Process-
ing (BioNLP 2019).
Anya E.R. Prince and Daniel Schwarcz. 2019. Proxy
discrimination in the age of artiﬁcial intelligence and
big data. Iowa Law Review, 105.
Inioluwa Deborah Raji, Emily Denton, Emily M. Ben-
der, Alex Hanna, and Amandalynne Paullada. 2021.
AI and the everything in the whole wide world
benchmark. In Thirty-ﬁfth Conference on Neural In-
formation Processing Systems Datasets and Bench-
marks Track (Round 2).
John Rawls. 1971. A Theory of Justice, 1 edition. Belk-
nap Press of Harvard University Press, Cambridge,
Massachussets.
Douglas Rice, Jesse H. Rhodes, and Tatishe Nteta.
2019. Racial bias in legal language. Research &
Politics, 6(2):2053168019848930.
Ingrid Robeyns. 2009. Justice as fairness and the capa-
bility approach. Arguments for a Better World. Es-
says for Amartya Sen’s, 75:397–413.
Shiori Sagawa, Pang Wei Koh, Tatsunori B. Hashimoto,
and Percy Liang. 2020.
Distributionally Robust
Neural Networks. In International Conference on
Learning Representations.

--- Page 13 ---

Sebastian Felix Schwemer, Letizia Tomada, and Tom-
maso Pasini. 2021. Legal ai systems in the eu’s pro-
posed artiﬁcial intelligence act. In In Joint Proceed-
ings of the Workshops on Automated Semantic Anal-
ysis of Information in Legal Text (ASAIL 2021) and
AI and Intelligent Assistance for Legal Professionals
in the Digital, Workplace (LegalAIIA 2021).
Anders Søgaard, Sebastian Ebert, Jasmijn Bastings,
and Katja Filippova. 2021. We need to talk about
random splits. In Proceedings of the 16th Confer-
ence of the European Chapter of the Association
for Computational Linguistics: Main Volume, pages
1823–1832, Online. Association for Computational
Linguistics.
Harold J. Spaeth, Lee Epstein, Jeﬀrey A. Segal Andrew
D. Martin, Theodore J. Ruger, and Sara C. Benesh.
2020. Supreme Court Database, Version 2020 Re-
lease 01. Washington University Law.
Dimitrios Tsarapatsanis and Nikolaos Aletras. 2021.
On the ethical limits of natural language processing
on legal text. In Findings of the Association for Com-
putational Linguistics: ACL-IJCNLP 2021, pages
3590–3599, Online. Association for Computational
Linguistics.
V. Vapnik. 1992. Principles of risk minimization for
learning theory. In Advances in Neural Information
Processing Systems, volume 4. Morgan-Kaufmann.
Sandra Wachter, Brent Daniel Mittelstadt, and Chris
Russell. 2021. Bias preservation in machine learn-
ing: The legality of fairness metrics under eu non-
discrimination law. West Virginia Law Review, 123.
Alex Wang,
Yada Pruksachatkun,
Nikita Nangia,
Amanpreet Singh, Julian Michael, Felix Hill, Omer
Levy, and Samuel Bowman. 2019a. Superglue: A
stickier benchmark for general-purpose language un-
derstanding systems. In Advances in Neural Infor-
mation Processing Systems, volume 32. Curran As-
sociates, Inc.
Alex Wang, Amanpreet Singh, Julian Michael, Felix
Hill, Omer Levy, and Samuel R. Bowman. 2019b.
GLUE: A multi-task benchmark and analysis plat-
form for natural language understanding. In Inter-
national Conference on Learning Representations,
New Orleans, Louisiana, USA.
Wenhui Wang, Hangbo Bao, Shaohan Huang, Li Dong,
and Furu Wei. 2021a. MiniLMv2: Multi-head self-
attention relation distillation for compressing pre-
trained transformers. In Findings of the Association
for Computational Linguistics: ACL-IJCNLP 2021,
pages 2140–2151, Online. Association for Computa-
tional Linguistics.
Yuzhong Wang, Chaojun Xiao, Shirong Ma, Haoxi
Zhong, Cunchao Tu, Tianyang Zhang, Zhiyuan Liu,
and Maosong Sun. 2021b. Equality before the law:
Legal judgment consistency analysis for fairness.
Science China - Information Sciences.
Alice Xiang. 2021.
Reconciling legal and technical
approaches to algorithmic bias. Tennessee Law Re-
view, 649.
Chaojun Xiao, Haoxi Zhong, Zhipeng Guo, Cunchao
Tu, Zhiyuan Liu, Maosong Sun, Yansong Feng, Xi-
anpei Han, Zhen Hu, Heng Wang, and Jianfeng Xu.
2018.
CAIL2018: A large-scale legal dataset for
judgment prediction. CoRR, abs/1807.02478.
Haoxi Zhong, Chaojun Xiao, Cunchao Tu, Tianyang
Zhang, Zhiyuan Liu, and Maosong Sun. 2020. How
does NLP beneﬁt legal system: A summary of legal
artiﬁcial intelligence. In Proceedings of the 58th An-
nual Meeting of the Association for Computational
Linguistics, pages 5218–5230, Online. Association
for Computational Linguistics.
A
Discrimination and Fairness in Law
The legal notion of discrimination has a diﬀerent
scope and semantics in comparison to the notions
of fairness and bias used in the context of machine
learning (Gerards and Xenedis, 2020), where the
aim usually is not to achieve equal odds, e.g. that
a court shall rule the same decision for both men
and woman based on similar facts, or to have 50/50
favourable decisions for both man and woman, but
equal opportunities (Rawls, 1971).
In the context of law, the principle of equality
and non-discrimination is of paramount importance
at international, regional and domestic level. Arti-
cle 2 of the Universal Declaration of Human Rights
(UDHR) prohibits discrimination on grounds of
race, colour, sex, language, religion, political or
other opinion, national or social origin, property,
birth or other status, with the latter term having
an open-ended meaning. The principle is also re-
ﬂected in several other United Nations (UN) hu-
man rights instruments and in regional legal instru-
ments, including Article 24 American Convention
of Human Rights (ACHR), Articles 2 and 3 African
Charter on Human and People’s Rights (ACHPR)
and Article 14 and Protocol N. 12 of the European
Convention on Human Rights (ECHR).
The principle of non-discrimination is included
in all international human rights instruments, al-
though only a few explicitly provide a deﬁnition of
non-discrimination (e.g. Article 1(1) CERD, Arti-
cle 1 CEDAW, Article 2 CRPD, Article 1(1) ILO).
In general, in international human rights law a vio-
lation of the principle of non-discrimination occurs
when: (a) equal cases are treated diﬀerently, (b)
there is no reasonable and objective justiﬁcation
for the diﬀerence in treatment, or (c) the means
used are not proportional to the aim. In addition,

--- Page 14 ---

many international instruments explicitly allow for
‘positive action’, without mandating an obligation
on States in that sense. The term ‘positive action’
refers to active measures taken by private institu-
tions or governments that favour members of previ-
ously disadvantaged groups with the aim to remedy
the eﬀects of past and present discrimination. At
both regional and domestic level, a great number
of countries have implemented non-discrimination
law directly in their legislation. The following brief
analysis provides an overview of the legal frame-
work applicable in the EU and in the USA, in light
of the wide deployment of algorithms and increas-
ing risk of algorithmic discrimination documented
in these contexts.
In the context of EU, EU non-discrimination
law prohibits both direct and indirect discrimina-
tion.17 Direct discrimination occurs when one per-
son is treated “less favourably than another is, has
been or would be treated in a comparable situa-
tion” on grounds of sex, racial or ethnic origin,
disability, sexual orientation, religion or belief and
age in the context of a protected sector (e.g. the
workplace and provision of goods and services)
(Wachter et al., 2021). Prohibiting direct discrimi-
nation allows to provide people with equal access to
opportunities (i.e. formal equality). This however
does not suﬃce, nor guarantee to create equality
of opportunity (i.e. substantive equality), which
can instead be achieved only by accounting for
protected attributes and for social and historical
realities and by taking positive measures to level
the playing ﬁeld (Fredman, 2016). The notion of
indirect discrimination is grounded on achieving
substantive equality in practice. The Directives de-
ﬁne indirect discrimination as situations where an
apparently neutral provision, criterion or practice
would put persons with a protected characteristic
at disadvantage in comparison to other persons,
unless ‘that provision, criterion or practice is “justi-
ﬁed by a legitimate aim and the means of achieving
that aim are appropriate and necessary”.
Nevertheless, the current EU non-discrimination
law framework suﬀers from limitations, both as
regards its personal (i.e. it only protects six char-
acteristics) and material scope (i.e. the prohibition
on discrimination is limited only to certain ﬁelds)
(Gerards and Xenedis, 2020). These limitations
pose problems in connection to algorithmic dis-
17Directives 2000/43/EC of 29 June 2000; 2000/78/EC
of 27 November 2000; 2004/113/EC of 13 December 2004;
2006/54/EC of 5 July 2006
crimination. For example, as algorithmic bias of-
ten creates seemingly neutral distinctions which
however often correlate to a protected group (i.e.
proxy discrimination), the limited list of protected
grounds renders diﬃcult to tackle the eﬀects of
algorithmic bias through the concept of direct dis-
crimination (Prince and Schwarcz, 2019). Indirect
discrimination can help address those cases. but its
application in this context poses several challenges.
In April 2021 the European Commission pre-
sented a proposal for a Regulation laying down
harmonized rules on artiﬁcial intelligence (AI Act /
AIA).18 The proposal aims at avoiding “signiﬁcant
risks to the health and safety or fundamental rights
of persons” and would, once adopted, complement
the currently applicable legal framework for tack-
ling algorithmic discrimination, thereby overcom-
ing some of its existing limitations. The envisaged
implementation of the proposed AI Act highlights
the importance that the legislator poses in prevent-
ing and mitigating discrimination and biases aris-
ing from the development and use of AI systems in
several areas of application, including in the legal
sector (Schwemer et al., 2021). AI systems used for
the administration of justice and democratic pro-
cesses are proposed to be deemed high-risk in order
“to address the risks of potential biases, errors, and
opacity” (recital 40 AIA). The consequence is that
such systems would be subject to a variety of de-
sign and development requirements, e.g. related to
the training, validation and testing data sets which
would have to be examined inter alia in relation to
possible biases (art. 10(2) lit. f AIA) or related to
human oversight of such AI system with a view to
remain aware of automation bias (art. 14(4) lit. b
AIA).
In the US the jurisprudence relies on the doc-
trines of disparate treatment and disparate impact
provided for in Title VII of the 1964 Civil Rights
Act.19 A prohibition on disparate treatment is in-
cluded also in the Equal Protection Clause of the
Constitution20 and in civil rights laws. The prohibi-
tion refers to intentional discrimination and occurs
when individuals are treated in a diﬀerent man-
ner on the basis of protected class attributes, such
as race, colour, national origin, sex, age and re-
ligion.21 The prohibition on disparate impact is
instead provided for only in civil rights statutes
18Regulation Proposal 2021/206
19Civil Rights Act of 1964, 42 U.S.C § 2000e-2
20Cf. Vasquez v. Hillery, 474 US 254 (1986).
21Civil Rights Act of 1964, 42 U.S.C § 2000e-2

--- Page 15 ---

and, in brief, it establishes that if some practice or
activity has a disproportionate adverse eﬀect on pro-
tected groups, the defendant must prove that such a
practice has an adequate justiﬁcation.22 Also in the
US, recent literature has highlighted the challenges
that the current legal framework faces when tack-
ling algorithmic discrimination, in particular as far
as liability and the burden of proof are concerned
(Kleinberg et al., 2019; Xiang, 2021).
Beyond the boundaries of EU and US law, a
great number of countries explicitly prohibit dis-
crimination in their laws on the basis of nationality,
race, ethnicity and religion. Other countries extend
the prohibition only in relation to race and religion
instead. In many countries, there is not yet any spe-
ciﬁc or dedicated law against non-discrimination,
such as in China, India, Indonesia, Japan, Korea
and Saudi Arabia. This does not imply by any
means that there are not potentially separate pieces
of legislation that enforce non-discrimination for
some class attributes.
B
Attribute Extraction and Grouping
In this section, we provide ﬁner details on attribute
extraction and grouping.
ECtHR
We extracted the defendant states from
the HUDOC23 case metadata, namely Respondent
State(s). We group the defendant states mainly
relying on their classiﬁcation by the EuroVoc the-
saurus24. The grouping mainly reﬂects the high
disproportion of violations between mainly Eastern
European countries, and in a second degree Central
European, and the rest (Western European, Nordic,
Mediterranean states). Applicant’s birth year is ex-
tracted from the case facts, if available, e.g., “The
ﬁrst applicant, Mr X, was born in 1967.”, using
Regular Expressions (RegEx). Then, we compute
the age by subtract birth year from the judgment
date, extracted from the HUDOC case metadata,
as well. The age grouping does not follow any
pattern and aims to cluster applicants in discrete
groups that have statistical support. Finally, we
extract gender from case facts, if possible, based
on pronouns (e.g., ‘he’, ‘she’, ‘his’, ‘her’), and
other gender words (e.g., ‘mr’, ‘mrs’, ‘husband’,
22See the deﬁning decision, Griggs v. Duke Power Co., 401
U.S. 424 (1971).
23The ECtHR online database (https://hudoc.echr.
coe.int/)
24https://op.europa.eu/en/web/
eu-vocabularies
‘wife’) in context such as “The applicant’s hus-
band [...]”, or “‘The applicant, Mr A, [...]”. We
acknowledge that non-binary gender identities ex-
ist, but non-binary gendered applicants cannot be
identiﬁed automatically.
In many cases, the birth year or gender was not
identiﬁable in the facts. Furthermore, many cases
involve multiple applicants. In such cases, we mark
the respected attributes as unknown, and hold a
diﬀerent group for unidentiﬁed instances. These
data points are used in experiments, but we do not
report results for such groups.
SCOTUS
Both attributes rely on metadata pro-
vided by the Supreme Court DataBase (SCDB)25.
In case of the direction of the decision, i.e., whether
the decision is considered liberal, or conservative,
we use the original variable (Decision Direction).26.
In case of the type of respondent, we manually cat-
egorize (cluster) all available, 311 in total, values
for the Respondent variable27 in ﬁve abstract cate-
gories (person, public entity, organization, facility
and other).
FSCS
All attributes are already available as part
of the original dataset of Niklaus et al. (2021).
Groups represent individual values. Information
was extracted from courts’ metadata.
CAIL
All attributes are already available as part
of the original dataset of Wang et al. (2021b).
Groups represent individual values. Information
was extracted from courts’ metadata.
C
Train and Evaluation Details
We ﬁne-tune all pre-trained transformer-based lan-
guage models using the AdamW (Loshchilov and
Hutter, 2019) optimizer with a learning rate of 3e-
5. We use a batch size of 16 and train models for
up to 20 epochs using early stopping on validation
performance.28 Across datasets and attributes, we
run ﬁve repetitions with diﬀerent random seeds and
report averaged scores.
D
Release of Language Models
We release four domain-speciﬁc BERT models (Ta-
ble 5 with continued pre-training on the corpora
25http://scdb.wustl.edu/
26http://scdb.wustl.edu/documentation.php?
var=decisionDirection
27http://scdb.wustl.edu/documentation.php?
var=respondent
28We train all models in a mixed-precision (fp16) setting to
use the maximum available batch size.

--- Page 16 ---

Figure 2: Distribution of sequence (document) length across FairLex datasets (ECtHR, SCOTUS, FSCS, CAIL).
Model name
Domain
Languages
‘coastalcph/fairlex-ecthr-minlm‘
ECtHR
‘en‘
‘coastalcph/fairlex-scotus-minlm‘
SCOTUS
‘en‘
‘coastalcph/fairlex-fscs-minlm‘
FSCS
‘de‘, ‘fr‘, ‘it‘
‘coastalcph/fairlex-cail-minlm‘
CAIL
‘zh‘
Table 5: Domain-speciﬁc pre-trained language models
speciﬁcations.
of the examined datasets.29 We train mini-sized
BERT models with 6 Transformer blocks, 384 hid-
den units, and 12 attention heads. We warm-start all
models from the public MiniLMv2 models check-
points (Wang et al., 2021a) using the distilled ver-
sion of RoBERTa (Liu et al., 2019) for the English
datasets (ECtHR, SCOTUS) and the one distilled
from XLM-R (Conneau et al., 2020) for the rest
(trilingual FSCS, and Chinese CAIL). We pre-train
each models in the training subset of each FairLex
dataset with sequences of 128 sub-words for 10
epochs using the AdamW (Loshchilov and Hutter,
2019) optimizer with a maximum learning rate of
1e-4 and 10% warm-up ratio.
E
Statistics
E.1
Distribution of Document Length
In Figure 2 we report the distribution of sequence
(document) length across FairLex datasets (ECtHR,
SCOTUS, FSCS). We observe that the documents
are extremely long (3,000-6,000+ words) across
datasets. Hence, we deploy hierarchical models
(Section 5) that are able to encode large parts of the
documents.
E.2
Group Distribution by Attribute
In Tables 6 and 7 we report the group distribu-
tion per examined attribute under consideration. In
some cases, the extraction of the speciﬁc attribute,
e.g., gender or age in ECtHR, was not possible, i.e.,
the applied rules would no suﬃce, possibly because
the information is intentionally missing. During
training, the groups of unidentiﬁed samples is in-
cluded, but we report test scores excluding those,
29https://huggingface.co/coastalcph
i.e., mF1 and GD do not take into account the F1
of these groups.
F
Label Distribution KL Divergences
In Tables 8, 9, 10, and 11, we report the Jensen-
Shannon divergences between train-test, train-dev
and test-test distribution of labels separately for
each protrected attribute values and for each dataset
in our framework.

--- Page 17 ---

ECtHR
Applicant Age
Applicant Gender
Defendant State
N/A
≤35
≤65
> 65
N/A
Male
Female
E.C.
West
2,794
839
4,246
1,121
3,306
4,407
1,287
7,224
1,776
Table 6: Group distribution in training set for each attribute of ECtHR dataset. ‘N/A’ (Not Answered) refers to
samples, where the respected attribute could not be extracted.
SCOTUS
Defendant
Direction
Other
Facility
Organization
Person
Public Entity
Conservative
Liberal
957
140
741
1847
2796
3146
3335
Table 7: Group distribution in training set for each attribute of SCOTUS dataset.
Applicant Age
Applicant Gender
Defendant State
≤35
≤65
> 65
Male
Female
East
West
Train-Test
0.19
0.18
0.32
0.17
0.26
0.17
0.28
Train-Dev
0.18
0.19
0.22
0.17
0.22
0.18
0.17
Dev-Test
0.20
0.08
0.19
0.09
0.10
0.09
0.16
Table 8: Jensen-Shannon Divergence of label distribution between training, test and development sets of ECtHR
by protected attribute values. The lower the values the more similar the distributions.
Defendant
Direction
Facility
Organization
Other
Person
Pub. Entity
Conservative
Liberal
Train-Test
0.26
0.11
0.09
0.05
0.07
0.05
0.04
Train-Dev
0.28
0.11
0.11
0.07
0.03
0.06
0.05
Dev-Test
0.22
0.17
0.13
0.10
0.07
0.09
0.07
Table 9: Jensen-Shannon Divergence of label distribution between training, test and development set in Scotus by
protected attribute values. The lower the values the more similar the distributions.

--- Page 18 ---

Train-Test
Train-Dev
Dev-Test
Language
DE
0.0336
0.0275
0.0061
FR
0.0517
0.0301
0.0216
IT
0.0145
0.0405
0.0261
Legal Area
Other
0.1000
—
—
Public Law
0.0007
0.0090
0.0083
Penal Law
0.0018
0.0118
0.0136
Civil Law
0.0248
0.0046
0.0202
Social Law
0.0624
0.0570
0.0054
Region
Région lémanique
0.0447
0.0259
0.0188
Zürich
0.0447
0.0345
0.0028
Espace Mittelland
0.0765
0.0435
0.0331
NW Switzerland
0.0280
0.0127
0.0407
E Switzerland
0.0197
0.0394
0.0198
C Switzerland
0.0267
0.0304
0.0036
Ticino
0.0023
0.0284
0.0307
Federation
0.0018
0.0385
0.0404
Table 10: Jensen-Shannon Divergence of label distribution between training, test and development set in FSCS by
protected attribute values. The lower the values the more similar the distributions.
Region
Gender
Beijing
Liaoning
Hunan
Guangdong
Sichuan
Guangxi
Zhejiang
Male
Female
Train-Test
0.0516
0.0458
0.0495
0.0524
0.0559
0.0696
0.0687
0.0345
0.0766
Train-Dev
0.0239
0.0270
0.0406
0.0584
0.0484
0.0426
0.0338
0.0164
0.0318
Dev-Test
0.0469
0.0296
0.0799
0.0431
0.0554
0.0496
0.0633
0.0307
0.0986
Table 11: Jensen-Shannon Divergence of label distribution between training, test and development set in SPC by
protected attribute values. The lower the values the more similar the distributions.

```
