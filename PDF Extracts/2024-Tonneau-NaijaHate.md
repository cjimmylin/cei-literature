---
title: "NaijaHate - PDF Extract"
source_pdf: "2024-Tonneau-NaijaHate.pdf"
pages: 21
extracted_at: "2026-01-24T17:05:42.856941"
---

# PDF Extract: NaijaHate

**Source PDF:** 2024-Tonneau-NaijaHate.pdf
**Total Pages:** 21

---

## Content

```
--- Page 1 ---

NAIJAHATE: Evaluating Hate Speech Detection
on Nigerian Twitter Using Representative Data
Manuel Tonneau 1, 2, 3, Pedro Vitor Quinta de Castro 1, 4, Karim Lasri 1, 5,
Ibrahim Farouq 1, 6, Lakshminarayanan Subramanian 3,
Victor Orozco-Olvera 1, Samuel P. Fraiberger 1, 3, 7,
1 The World Bank, 2 University of Oxford, 3 New York University
4 Universidade Federal de Goiás 5 Ecole Normale Supérieure
6 Universiti Sultan Zainal Abidin 7 Massachusetts Institute of Technology
Abstract
To address the global issue of online hate,
hate speech detection (HSD) systems are typi-
cally developed on datasets from the United
States, thereby failing to generalize to En-
glish dialects from the Majority World. Fur-
thermore, HSD models are often evaluated on
non-representative samples, raising concerns
about overestimating model performance in
real-world settings. In this work, we intro-
duce NAIJAHATE, the first dataset annotated
for HSD which contains a representative sam-
ple of Nigerian tweets. We demonstrate that
HSD evaluated on biased datasets traditionally
used in the literature consistently overestimates
real-world performance by at least two-fold.
We then propose NAIJAXLM-T, a pretrained
model tailored to the Nigerian Twitter context,
and establish the key role played by domain-
adaptive pretraining and finetuning in maximiz-
ing HSD performance. Finally, owing to the
modest performance of HSD systems in real-
world conditions, we find that content modera-
tors would need to review about ten thousand
Nigerian tweets flagged as hateful daily to mod-
erate 60% of all hateful content, highlighting
the challenges of moderating hate speech at
scale as social media usage continues to grow
globally. Taken together, these results pave the
way towards robust HSD systems and a better
protection of social media users from hateful
content in low-resource settings.
Content warning: This article contains illustrative
examples of hateful content.
1
Introduction
Social media came with the promise to connect
people, increase social cohesion, and let everyone
have an equal say. Yet, this technology has also
been associated with online harms and detrimental
effects on democracy (Lorenz-Spreen et al., 2023).
In particular, users are regularly exposed to hate
speech1 (Vidgen et al., 2019), fueling fears of its
impact on social unrests and hate crimes (Müller
and Schwarz, 2021). While regulatory frameworks
have compelled social media platforms to take ac-
tion (Gagliardone et al., 2016), hate speech detec-
tion (HSD) and moderation efforts have largely
focused on the North American and European mar-
kets, prompting questions on how to efficiently
tackle this issue in the Majority World (Milmo,
2021; Tonneau et al., 2024). Our study focuses on
Nigerian Twitter, a low-resource context which pro-
vides an opportunity to study online hate speech
at the highest level (Ezeibe, 2021). Exemplify-
ing the issue, Twitter was banned by the Nigerian
government between June 2021 and January 2022,
following the platform’s deletion of a tweet by the
Nigerian President in which he made provocative
remarks about Biafran separatists (Maclean, 2021).
The challenges in developing HSD systems
are two-fold. First, hateful content is infrequent
– approximately 0.5% of posts on US Twitter
(Jiménez Durán, 2021) – creating an obstacle to
generating representative annotated datasets at a
reasonable cost. To alleviate this issue, models
are developed on curated datasets by oversam-
pling hateful content matching predefined key-
words (Davidson et al., 2017), or by using active
learning to maximize performance for a given anno-
tation cost (Kirk et al., 2022; Markov et al., 2023).
These sampling choices generate biases in evalua-
tion datasets (Wiegand et al., 2019; Nejadgholi and
Kiritchenko, 2020), raising questions on the gener-
alizability of HSD models to real-world settings.
Second, while a plethora of HSD modeling op-
tions are available, it is unclear how well they adapt
to a new context. Although few-shot learners are
appealing for requiring no or few finetuning data,
the evidence on their performances relative to su-
1Hate speech is defined as any communication that dispar-
ages a person or a group based on the perceived belonging of
a protected characteristic, such as race (Basile et al., 2019).
arXiv:2403.19260v3  [cs.CL]  24 Jun 2024

--- Page 2 ---

pervised HSD baselines is mixed (Plaza-del arco
et al., 2023a; Guo et al., 2024). Supervised learners
are typically finetuned on US data (Tonneau et al.,
2024) and tend to not generalize well to English
dialects spoken in the Majority World (Ghosh et al.,
2021). Finally, while further pretraining existing ar-
chitectures to adapt them to a new context is known
to increase performance on downstream tasks (Gu-
rurangan et al., 2020), it is unclear whether highly
specific contexts require a custom domain adap-
tation. Overall, questions remain on the extent
to which available HSD methods perform when
adapted to a low-resource context (Li, 2021).
In this work, we present NAIJAHATE, a dataset
of 35,976 Nigerian tweets annotated for HSD,
which includes a representative evaluation sample
to shed light on the best approach to accurately de-
tect hateful content in real-world settings. We also
introduce NAIJAXLM-T, a pretrained language
model adapted to the Nigerian Twitter domain. We
demonstrate that evaluating HSD models on biased
datasets traditionally used in the literature largely
overestimates performance on representative data
(83-90% versus 34% in average precision). We fur-
ther establish that domain-adaptive pretraining and
finetuning leads to large HSD performance gains
on representative evaluation data over both US and
Nigerian-centric baselines. We also find that fine-
tuning on linguistically diverse hateful content sam-
pled through active learning significantly improves
performance in real-world conditions relative to a
stratified sampling approach. Finally, we discuss
the cost-recall tradeoff in moderation and show that
having humans review the top 1% of tweets flagged
as hateful allows to moderate up to 60% of hateful
content on Nigerian Twitter, highlighting the limits
of a human-in-the-loop approach to content mod-
eration as social media usage continues to grow
globally.
Therefore, our main contributions are 2:
• NAIJAHATE, a dataset which includes the first
representative evaluation sample annotated for
HSD on Nigerian Twitter;
• NAIJAXLM-T, a pretrained language model
adapted to the Nigerian Twitter domain;
• an evaluation on representative data of the role
played by domain adaptation and training data
diversity and a discussion of the feasibility of
hateful content moderation at scale.
2The dataset and the related models can be found at http
s://github.com/worldbank/NaijaHate.
2
Related work
2.1
Nigerian hate speech datasets
While existing English hate speech datasets are
primarily in US English (Tonneau et al., 2024),
mounting evidence highlights the limited general-
izability of learned hate speech patterns from one
dialect to another (Ghosh et al., 2021; Castillo-
lópez et al., 2023). In this context, recent work
has developed hate speech datasets tailored to the
Nigerian context; however, the latter either focused
on one form of hate speech (Aliyu et al., 2022),
specific languages (Adam et al., 2023; Aliyu et al.,
2024), or particular events (Ndabula et al., 2023;
Ilevbare et al., 2024). To the best of our knowl-
edge, our work is the first to construct a compre-
hensive dataset annotated for hate speech for the
entire Nigerian Twitter ecosystem, covering both
the diversity of languages and hate targets.
2.2
Hate speech detection
HSD methods fall into three categories: rule-based
(Mondal et al., 2017), supervised learning (David-
son et al., 2017), and zero-shot or few-shot learning
(ZSL) (Nozza, 2021). Rule-based methods rely on
predefined linguistic patterns and therefore typi-
cally achieve very low recall. Additionally, super-
vised learning require annotated datasets which are
usually scarce in Majority World contexts. While
recent advancements in ZSL could potentially cir-
cumvent the need to produce finetuning data for
supervised learning, existing evidence on the rela-
tive performance of the two approaches is mixed
(Plaza-del arco et al., 2023a; Guo et al., 2024).
A major shortcoming of this literature is
that HSD is typically evaluated on curated
non-representative datasets whose characteristics
greatly differ from real-world conditions (Wiegand
et al., 2019; Nejadgholi and Kiritchenko, 2020),
raising concerns about overestimating HSD perfor-
mance (Arango et al., 2019). While past work has
annotated representative samples for HSD, the sam-
ples have either not been used solely for evaluation
(Vidgen et al., 2020) or originate from largely un-
moderated platforms, such as Gab (Kennedy et al.,
2022), where hatred is much more prevalent and
therefore HSD is an easier task. To the best of our
knowledge, we provide the first evaluation of HSD
on a representative evaluation sample from a main-
stream social media platform, Twitter, where hate
content is rare.

--- Page 3 ---

2.3
Hate speech moderation
Most large social media platforms prohibit hate
speech (Singhal et al., 2023) and have done so
since their inception (Gillespie, 2018). However,
with millions of daily social media posts, enforcing
this policy is a very challenging task. While such
scale has motivated the use of algorithmic detection
methods (Gillespie, 2020), these approaches have
raised concerns related to the fairness and poten-
tial biases their use imply in moderation decisions
(Gorwa et al., 2020). As a middle ground, recent
work has proposed a human-in-the-loop approach
(Lai et al., 2022), where a model flags content likely
to infringe platform rules, which is then reviewed
by humans who decide whether or not to moderate
it. Albeit promising, it remains unclear whether
this process is scalable both from a cost and a per-
formance standpoint. To fill this gap, we provide
the first estimation of the feasibility of a human-in-
the-loop approach in the case of Nigerian Twitter.
3
Data
Neutral
Oﬀensive
Hateful
North
South
East
Muslim
Women
Other
10-⁵
10-⁴
10-³
10-²
10-¹
10⁰
Proportion of data in class
StraƟﬁed sample (N = 1,607)
AcƟve learning sample (N = 2,405)
Top-scored sample (N = 1,965)
Random sample (N= 29,999)
Figure 1: Proportion of data in each class, showing
the composition of the hateful class across hate target
categories.
3.1
Data collection
We use the Twitter API to collect a dataset con-
taining 2.2 billion tweets posted between March
2007 and July 2023 and forming the timelines of
2.8 million users with a profile location in Nigeria.3
We iteratively collect the timeline of users with a
profile location in Nigeria being mentioned in the
timeline of other Nigerian users until no additional
Nigerian users were retrieved, ensuring maximum
coverage of the Nigerian ecosystem. This Nigerian
Twitter dataset is mostly constituted of English
3The dataset contains 13.9 billion tokens and 525 million
unique token, for a total of 89GB of uncompressed text.
tweets (77%) followed by tweets in Nigerian Pid-
gin – an English-based creole widely spoken across
Nigeria – (7%), tweets mixing English and Pidgin
(1%), tweets in Hausa (1%) and tweets in Yoruba
(1%) (Table 8). We then draw two distinct random
samples of 100 million tweets each, one for model
training and the other one for evaluation.
3.2
Annotation
We recruit a team of four Nigerian annotators, two
female and two male, each of them from one of
the four most populated Nigerian ethnic groups –
Hausa, Yoruba, Igbo and Fulani.
We follow a prescriptive approach (Rottger et al.,
2022) by instructing annotators to strictly adhere
to extensive annotation guidelines describing our
taxonomy of hate speech (detailed in §A.2.2). Fol-
lowing prior work (Davidson et al., 2017; Mathew
et al., 2021), HSD is operationalized by assigning
tweets to one of three classes: (i) hateful, if it con-
tains an attack on an individual or a group based
on the perceived possession of a protected charac-
teristic (e.g., gender, race) (Basile et al., 2019), (ii)
offensive, if it contains a personal attack or an in-
sult that does not target an individual based on their
identity (Zampieri et al., 2019), or (iii) neutral if it
is neither hateful nor offensive. If a tweet is labeled
as hateful, it is also annotated for the communities
being targeted (Table 1).
In the next sections §3.3 and §3.4, we detail the
different samples that were annotated. Each tweet
in these samples was labeled by three annotators.
For the three-class annotation task, the three anno-
tators agreed on 90% of all labeled tweets, two out
of three agreed in 9.5% of cases, and all three of
them disagreed in 0.5% of cases (Krippendorff’s α
= 0.7).
Label
Target
Examples
North
My hate for northern people keeps growing
South
You idiotic Southerners fighting your own
East
IPOBs are animals....They lack tact or strategy.
Hateful
Muslim
Muslim baboons and their terrorist religion.
Women
Nobody believes this ashawo (prostitute) woman
Offensive
None
Stop spewing rubbish, mumu (fool).
Neutral
None
She don already made up her mind sha.
Table 1: Examples of tweets for each class. Offensive
tweets have no target as they do not target an identity
group. Non-English words are displayed in italic with
their English translation in parenthesis.

--- Page 4 ---

3.3
Training samples
Stratified sample
Due to the rarity of hateful
content, sampling tweets randomly would result in
a highly imbalanced set. Indeed, the prevalence of
hate speech on large social media platforms typi-
cally ranges from 0.003% to 0.7% depending on
the platform and timeframe (Gagliardone et al.,
2016; Mondal et al., 2017; Jiménez Durán, 2021).
To circumvent this issue, we follow previous work
(Davidson et al., 2017) by oversampling training ex-
amples containing keywords expected to be associ-
ated with hate. We handpick a list of 89 hate-related
keywords combining hate speech lexicons and on-
line dictionaries (Ferroggiaro, 2018; Farinde and
Omolaiye, 2020; Udanor and Anyanwu, 2019). We
also identify 45 keywords referring to communities
frequently targeted by hate in the Nigerian context
(Pate and Ibrahim, 2020), due to their ethnicity
(Fulani, Hausa, Herdsmen4, Igbo, Yoruba), reli-
gion (Christians, Muslims), region of origin (north-
erners, southerners, easterners), gender identity or
sexual orientation (women, LGBTQ+) (Onanuga,
2023). We then annotate 1,607 tweets from the
training sample that are stratified by community-
related and hate-related keywords (see §A.1.3).
Owing to the rarity of some individual targets and
for descriptive purposes, we bundle targets into 6
target categories: North (Hausa, Fulani, Herdsmen,
Northerner), South (Southerner, Yoruba), East (Bi-
afra, Igbo, Easterner), Muslims, Women and Other
(Christians and LGBTQ+). Stratified sampling in-
deed enables to reduce the imbalance in the train-
ing data (Figure 1): the resulting shares of tweets
labeled as neutral, offensive and hateful are respec-
tively equal to 50%, 17%, and 33%.
Active learning sample
While stratified sam-
pling makes it possible to oversample hateful con-
tent in the training data, it is constrained by a pre-
defined vocabulary which limits the coverage and
diversity of the positive class. As an alternative, we
employ certainty sampling (Attenberg et al., 2010)
to annotate a second sample of training examples.
Certainty sampling is an active learning method
that focuses the learning process of a model on in-
stances with a high confidence score of belonging
to the minority class, spanning a more diverse spec-
trum of examples. We generate additional training
instances in four steps: (i) we start by finetuning
4Herdsmen are not a ethnic group per se but this term
refers exclusively to Fulani herdsmen in the Nigerian context,
hence the categorization as an ethnic group.
Conversational BERT (Burtsev et al., 2018) on the
stratified sample; (ii) we then deploy the finetuned
model on the training sample of 100 million tweets;
(iii) next, we label an additional 100 tweets sam-
pled from the top 10% tweets from the training
sample in terms of confidence score; and finally,
(iv) we incorporate the additional labels into Con-
versational BERT’s finetuning sample. We repeat
this process 25 times, thereby producing a set of
2,500 training examples, of which 2,405 have a ma-
jority label after annotation. We find that certainty
sampling produces about the same proportion of
observations from the hateful class (25% versus
31%) as stratified sampling (Figure 1). However,
it enables to generate more diversity in the hateful
class: the proportion of training examples that do
not contain any seed keywords5, the proportion of
unique tokens and the average pairwise GTE em-
bedding distance (Li et al., 2023) are consistently
larger in the active learning sample compared to
the stratified sample (Table 2).
Stratified
Active learning
Top-scored
Random
Proportion of
tweets not
containing
seed keywords (%)
7.5 ± 1.2
72.5 ± 1.8
70.8 ± 1.5
93.8 ± 3.5
Proportion of
unique tokens (%)
32.2 ± 0.4
33.3 ± 0.4
29 ± 0.3
61.5 ± 1.6
Average pairwise
embedding
distance
0.139 ± 0.0
0.152 ± 0.0
0.159 ± 0.0
0.172 ± 0.001
Table 2: Diversity metrics for the hateful class across
datasets. Active learning enables to generate more di-
versity in the training data, bringing them closer to the
representative random sample. Metrics are reported
with standard errors.
3.4
Evaluation samples
Top-scored sample
To evaluate models’ perfor-
mance in real-world conditions, we start by testing
how they behave in the presence of a distribution
shift. We first train each supervised model consid-
ered in this study on the union of the stratified and
the active learning sample, deploy it on the random
sample of 100 million tweets used for evaluation
and annotate 200 high-scored tweets. We repeat
this process for the 10 models evaluated in this
study (see §4 for more details) and combine all
the high-scored tweets, yielding a pooled sample
of 2,000 tweets, of which 1,965 have a majority
label after annotation. The shares of tweets labeled
5i.e., keywords used for stratified sampling

--- Page 5 ---

as neutral, offensive and hateful are respectively
equal to 28%, 22% and 50% (Figure 1). This ap-
proach traditionally used in information retrieval
enables to evaluate the performance of each model
on a large dataset containing a high and diverse
proportion of positive examples discovered by qual-
itatively different models, and whose distribution
differs from that of the training data (Voorhees
et al., 2005).
Random sample
Finally, we annotate a random
sample of 30,000 tweets, of which 29,999 have a
majority label after annotation, to evaluate HSD
models on a representative dataset of Nigerian
tweets. As expected, we discover that the preva-
lence of hateful content is very low: approximately
0.16% and 1.6% of tweets are labeled as hateful
and offensive, respectively (Figure 1). In addition,
we find that the diversity within the positive class
in the random sample is larger than in the training
samples (Table 2).
4
Experimental setup
In this study, our experiments aim to determine the
impact of domain adaptation – both for pretraining
and finetuning – on real-world performance. For
this purpose, we evaluate the performance of super-
vised learning with language models pretrained and
finetuned in various domains that we present below.
Additionally, we test recent off-the-shelf general-
purpose models in a zero-shot setting, specifically
GPT-3.56. We finally benchmark the finetuned
models against Perspective API (Lees et al., 2022),
a widely-deployed toxic language detection system
relying on BERT-based supervised learning and for
which the finetuning data is not public.
Finetuning domain
We experiment with four
finetuning datasets: HATEXPLAIN (Mathew et al.,
2021), which contains US English posts from
Twitter and Gab annotated for HSD; HERDPHO-
BIA (Aliyu et al., 2022), a dataset of Nigerian
tweets annotated for hate against Fulani herdsmen;
HSCODEMIX (Ndabula et al., 2023), containing
Nigerian tweets posted during the EndSARS move-
ment and the 2023 Nigerian presidential election
and annotated for general hate speech; and finally
NAIJAHATE, our dataset presented in §3.
6https://openai.com/blog/chatgpt
Pretraining domain
We introduce NAIJAXLM-
T (full), an XLM-R model (Conneau et al., 2020)
further pretrained on 2.2 billion Nigerian tweets for
one epoch. We compare its performance relative
to BERT-based models pretrained in three different
domains:
• the general domain, which includes a variety
of sources such as books and news, both in
English (DeBERTaV3 (He et al., 2021)) and
in multilingual settings (XLM-R (Conneau
et al., 2020), mDeBERTaV3 (He et al., 2021))
• the social media domain, both in English
(Conversational BERT (Burtsev et al., 2018),
BERTweet (Nguyen et al., 2020)) and in mul-
tilingual settings (XLM-T (Barbieri et al.,
2022))
• social media posts marked as offensive, abu-
sive or hateful (HateBERT (Caselli et al.,
2021) and fBERT (Sarkar et al., 2021))
• the African domain (AfriBERTa (Ogueji et al.,
2021), Afro-XLM-R (Alabi et al., 2022) and
XLM-R Naija (Adelani et al., 2021)).
Differences in performance across models may be
explained by several factors including not only the
pretraining domain, but also pretraining data size
and preprocessing, model architecture and hyper-
parameter selection. While it is hard to account
for the latter as they are rarely made public, we
estimate the impact of the pretraining domain on
performance, holding pretraining data size and
model architecture constant. To do so, we intro-
duce NAIJAXLM-T (198M), an XLM-R model
further pretrained on a random sample of 198 mil-
lion Nigerian tweets, matching the amount of data
used to pretrain XLM-T on multilingual tweets.
We adopt the same preprocessing as for XLM-T by
removing URLs, tweets with less than three tokens,
and running the pretraining for one epoch.
Evaluation
HSD models are evaluated by their
average precision for the hateful class, a standard
performance metric in information retrieval which
is particularly well-suited when class imbalance is
high. For supervised learning, we perform a 90-10
train-test split and conduct a 5-fold cross-validation
with five learning rates ranging from 1e-5 to 5e-5
and three different seeds. The train-test split is
repeated for 10 different seeds, and the evaluation
metrics are averaged across the 10 seeds.

--- Page 6 ---

Pretraining data
Finetuning data
Model
Holdout
Top-scored
Random
Multiple
None
GPT-3.5, ZSL
-
60.3±2.7
3.1±1.2
domains
Mixed∗
Perspective API
-
60.2±3.5
4.3±2.6
Social
HATEXPLAIN
XLM-T
84.2 ± 0.6
51.8 ± 0.7
0.6 ± 0.1
Media
HERDPHOBIA∗
XLM-T
62.0 ± 2.3
68.9 ± 0.8
3.3 ± 0.6
HSCODEMIX∗
XLM-T
70.5 ± 3.7
63.7 ± 1.1
1.9 ± 0.5
Multiple
DeBERTaV3
82.3 ± 2.3
85.3 ± 0.8
29.7 ± 4.1
domains
XLM-R
76.7 ± 2.5
83.6 ± 0.8
22.1 ± 3.7
mDeBERTaV3
29.2 ± 2.0
49.6 ± 1.0
0.2 ± 0.0
Social
NAIJAHATE
Conv. BERT
79.2 ± 2.3
86.2 ± 0.8
22.6 ± 3.6
media
BERTweet
83.6 ± 2.0
88.5 ± 0.6
34.0 ± 4.4
Stratified
XLM-T
79.0 ± 2.4
84.5 ± 0.9
22.5 ± 3.7
Hateful social
+
HateBERT
67.8 ± 2.9
78.6 ± 0.9
7.6 ± 2.1
media
certainty
fBERT
67.8 ± 2.8
78.9 ± 0.9
10.1 ± 2.6
African
sampling
AfriBERTa
70.1 ± 2.7
80.1 ± 0.9
12.5 ± 2.8
languages
(N=4012)
AfroXLM-R
79.7 ± 2.3
86.1 ± 0.8
24.7 ± 4.0
XLM-R Naija
77.0 ± 2.5
83.5 ± 0.8
19.1 ± 3.4
Nigerian Twitter
NAIJAXLM-T (198M)
83.0 ± 2.2
90.2 ± 0.6
33.1 ± 4.3
NAIJAXLM-T (full)
83.4 ± 2.1
89.3 ± 0.7
33.7 ± 4.5
Table 3: Average precision (in %) for the hateful class across models and evaluation sets. Metrics are reported
with 95% bootstrapped confidence intervals. All supervised learning classifiers are framed as three-class classifiers,
except the models trained on finetuning data marked with an asterisk as the latter is binary (hateful or not). Hyphens
indicate the absence of a holdout set. Metrics in italic are calculated on holdout sets that are different from one
another and from the NAIJAHATE holdout set.
5
Results
5.1
Hate speech detection
Evaluating on representative data
We evaluate
HSD performance on three datasets: the holdout
sample from the train-test splits, the top-scored
sample and the random sample described in §3.4
(Table 3). Overall, we observe that the ordering of
models’ performance remains stable across eval-
uation sets. However, the striking result is that
across the wide range of models considered in this
study, the average precision on the random sample
(20.92% on average) is substantially lower than
that on the holdout (73.75%) and top-scored sets
(81.88%). This finding highlights the risk of consid-
erably overestimating classification performance
when evaluating HSD models on a dataset whose
characteristics greatly differ from real-world condi-
tions. We now present more details on the impact
of the learning framework, the pretraining domain
and the finetuning domain on performance.
Learning framework
We find that in-domain
supervised learning on the NAIJAHATE dataset
(90.2% average precision on the top-scored set
and 34% on the random set) generally largely out-
performs GPT3.5-based zero-shot learning (ZSL)
(60.3% and 3.1%) and out-of-domain supervised
learning on existing US and Nigerian-centric hate
speech datasets (68.9% and 4.3%). We also note
that ZSL and out-of-domain supervised learning,
such as Perspective API, perform on par with each
other. Given that the prompt used does not provide
a definition of hate speech (App. A.4.4), it implies
that GPT3.5 has incorporated enough knowledge
from pretraining and reinforcement learning with
human feedback to conceptualize and categorize
hate speech as well as models finetuned on thou-
sands of examples. Still, it exhibits a rather low per-
formance which is likely due to the predominance
of US English in the pretraining data, making it
hard to generalize to Nigerian English.
Pretraining domain
We find that the language
and register models are pretrained on have a large
impact on downstream performance. In-domain
pretraining on Nigerian Twitter, combining Nige-
rian dialects and informal social media language,
generally outperforms the other models both on
the top-scored and random samples, followed by
models pretrained on social media and general pur-
pose domains. This result also holds when keeping

--- Page 7 ---

the architecture and pretraining data size constant,
with NaijaXLM-T (198M) yielding significantly
better performance than XLM-T. A notable excep-
tion to NaijaXLM-T’s dominance is BERTweet, a
RoBERTa model pretrained from scratch on En-
glish tweets, which is on par with NaijaXLM-T
on all evaluation sets.
Such performance may
be explained by the predominance of English on
Nigerian Twitter, granting an advantage to English-
centric models such as BERTweet or DeBERTaV3.
It is also plausible that BERTweet’s pretraining
data contains some English tweets originating from
Nigeria. Finally, BERTweet was pretrained from
scratch on tweets, implying that its vocabulary is
tailored to the social media lingo, contrary to the
XLM-based models.
We also observe that pretraining in the social me-
dia domain generally yields larger improvements
than in the African linguistic domain. For instance,
XLM-R Naija, an XLM-R model further pretrained
on news in Nigerian Pidgin English, produces a
rather poor performance, especially on the random
set (19.1% average precision), which is likely due
to differences between news and social media lingo
as well as the limited share of tweets in Pidgin En-
glish. Still, pretraining on the social media domain
does not ensure a high performance, as illustrated
by the low performance of models pretrained on
toxic social media posts, such as HateBERT and
fBERT. This underperformance may be explained
by the fact that these models are pretrained on
US-centric posts that emanate partly from other
platforms than Twitter (e.g., Reddit) and contain
aggressive and offensive speech, which may differ
from hate speech.
Finetuning domain
In-domain finetuning on the
NaijaHate dataset outperforms out-of-domain fine-
tuning on both US-centric (Perspective, HateX-
Plain) and Nigerian-centric (HERDPhobia and
HSCodeMix) datasets. When inspecting classifica-
tion errors, we find that XLM-T HateXPlain, which
is finetuned on US data, flags as hateful tweets
that contain words that are very hateful in the US
but not necessarily in Nigeria. For instance, “ya
k*ke” means “How are you” in Hausa while k*ke
is an antisemitic slur in the US context. As a re-
sult, XLM-T HateXplain assigns very high hateful
scores to tweets containing this sentence whereas
XLM-T NaijaHate does not. While finetuning on
Nigerian Twitter data yields better performance
than on US data, it does not ensure high perfor-
mance, as illustrated by the poor performance of
XLM-T HERDPhobia and HSCodeMix. In the
case of HERDPhobia, the focus on hate against Fu-
lani herdsmen leads to a low performance on other
types of hate such as misogyny, underlining the im-
portance of designing a comprehensive annotation
scheme covering the most prevalent types of hate.
Average Precision
NaijaXLM-T (full)
NaijaXLM-T (198M)
BERTweet
DeBERTaV3
AfroXLM-R
Conv. BERT
XLM-T
XLM-R
XLM-R Naija
fBERT
AfriBERTa
HateBERT
mDeBERTaV3
0.0
0.2
0.4
0.6
0.8
1.0
0.0
0.2
0.4
0.6
0.8
1.0
StraƟﬁed downsampled (N = 1,507)
AcƟve learning downsampled (N = 1,507)
StraƟﬁed + acƟve learning (N = 4,012)
Figure 2: Average precision on the random set across
models trained on the downsampled stratified set, the
downsampled active learning set and the full training set,
composed of the stratified and active learning sets. Error
bars indicate 95% bootstrapped confidence intervals.
Finetuning data diversity
In light of the higher
diversity in the training data sampled through active
learning compared to stratified sampling (Table
2), we further investigate the role that finetuning
data diversity plays on downstream performance.
Specifically, we produce downsampled versions of
the stratified and the active learning sets keeping
dataset size and class distribution constant. We
report the results on the random sample in Figure 2
and on the other evaluation sets in Figure 5 in the
Appendix.
We find that finetuning on more diverse data sig-
nificantly and consistently improves the average
precision across models. The performance gains
from diversity are particularly large for models that
are not pretrained in the African linguistic domain,
such as BERTweet and DeBERTaV3. We also dis-
cover that NaijaXLM-T significantly outperforms
BERTweet on the less diverse stratified set. This
finding indicates that the performance gains from
in-domain pretraining may be particularly large
when the finetuning data is less diverse, presum-
ably because the lower diversity in the finetuning
data is counterbalanced by a higher diversity and
domain alignment in the pretraining data, allowing
for a better generalization in real-world settings.

--- Page 8 ---

Precision-recall tradeoff
We find that no clas-
sification threshold allows to reach a precision
and recall that are both above 0.5 (Figure 4 in
the Appendix), with the best possible F1 value
for NaijaXLM-T (full) at 0.395. This high like-
lihood of error renders automatic moderation un-
desirable and calls for alternative moderation ap-
proaches, such as the human-in-the-loop modera-
tion we present in the next section.
5.2
Human-in-the-loop moderation
Recall
Proportion of All Tweets 
Reviewed by Moderator
NaijaXLM-T (full)
Random
10-⁵
10-⁴
10-³
10-²
10-¹
10⁰
0.0
0.2
0.4
0.6
0.8
1.0
Figure 3: Proportion of tweets flagged as hateful and re-
viewed by moderators versus recall. The random model
flags tweets as hateful at random.
In light of the low performance of hate speech
classifiers on Nigerian real-world data, we explore
the feasibility of a human-in-the-loop approach to
hate speech moderation, in which content likely
to contain hate is flagged by a classifier and then
reviewed by humans. Instead of the traditional
precision-recall tradeoff, human-in-the-loop mod-
eration implies a cost-recall tradeoff, where aug-
menting the recall comes at the cost of having more
flagged content reviewed by humans. We represent
this tradeoff by plotting the relationship between
the share of all tweets flagged as hateful by a hate
speech classifier, thus requiring human annotation
in a human-in-the-loop moderation setting, and re-
call (Figure 3). We provide more details in §A.4.6.
We find that supervised learning enables to di-
vide the amount of flagged tweets to be reviewed
by a factor of 60 compared to a random baseline,
with 1% of the data to be sent for review in order
to achieve a recall of 60%. With an average daily
flow of about 920,000 tweets on Nigerian Twitter in
2023, this translates to an average of 9,200 tweets
to be reviewed daily, which is a feasible objective
for a small team of moderators. However, increas-
ing recall comes at a cost that quickly becomes
prohibitively high, even for relatively small mar-
kets such as Nigeria: 10% of posts would need to
be reviewed daily in order to reach 76% recall.
6
Discussion
Performance overestimation
We demonstrate
that evaluating HSD on biased datasets leads to a
large overestimation of real-world performance, the
latter being rather low (34% average precision). A
possible reason for this gap is that hateful content
is much more rare in real-world settings (0.16%
in our Nigerian Twitter case) compared to tradi-
tional evaluation sets (31% in English hate speech
datasets (Tonneau et al., 2024)), rendering its detec-
tion more challenging. This result expands on past
work which pointed at the risk of overestimating
HSD performance in real-world settings but did not
quantify the latter (Arango et al., 2019; Wiegand
et al., 2019; Nejadgholi and Kiritchenko, 2020).
Feasibility of moderation
Low real-world HSD
performance has implications for hate speech mod-
eration, making automated moderation unfeasible
on top of being problematic for fairness and bias
reasons (Gorwa et al., 2020). In this context, we in-
vestigate the feasibility of human-in-the-loop mod-
eration, where content likely to be hateful is flagged
by a model before being reviewed by humans. We
highlight a cost-recall tradeoff, where a higher re-
call comes at the expense of increasing reviewing
efforts and find that 60% recall can be achieved by
reviewing 1% of all tweets. While reviewing 1% of
posts is a feasible goal for small online communi-
ties like Nigerian Twitter, it represents substantial
costs for larger communities, both financial and in
terms of reviewer harm (Steiger et al., 2021). We
also find that increasing recall comes at a cost that
quickly becomes prohibitively high for both small
and large communities – 10% of posts need to be
reviewed to reach a 76% recall. This may partly
explain the low hate speech removal rates on large
social media platforms (e.g., 3-5% on Facebook
(Giansiracusa, 2021)) and highlights the need for
complementary approaches to support the modera-
tion effort.

--- Page 9 ---

Learning framework
In terms of HSD ap-
proaches, we find that in-domain supervised learn-
ing significantly outperforms both out-of-domain
supervised learning and zero-shot learning. We
also find that out-of-domain supervised learning
and zero-shot learning perform on par with each
other. These findings complement prior work un-
derlining the superiority of supervised learning
over zero-shot learning for HSD (Plaza-del arco
et al., 2023a) by extending this result to a low-
resource setting.
Pretraining domain
Further, the choice of pre-
training model has a large impact on downstream
performance. Pretraining on in-domain data that
blends the noisy aspect of social media text with
the linguistic domain of finetuning tasks yields sig-
nificantly better performance than pretraining only
on the former, even when holding pretraining data
size and model architecture constant. Our results
support the established finding that in-domain pre-
training increases downstream task performance
(Gururangan et al., 2020) and complements it by
underlining the importance of all relevant domains
during pretraining, both in terms of register and
linguistic focus.
Finetuning domain
We find that in-domain fine-
tuning outperforms out-of-domain finetuning. The
main reason is that hateful statements are highly
context-specific (Lee et al., 2023; Davani et al.,
2024), leading to a limited generalizability of HSD
across cultures, as pointed out in previous work
(Ghosh et al., 2021).
It is therefore crucial to
develop HSD datasets in low-resource contexts
and our work contributes to this effort for Nige-
ria, which is largely under-represented in English
HSD resources (Tonneau et al., 2024).
Role of diversity
We observe that using diverse
data acquired through active learning yields signif-
icant performance gains over stratified sampling.
This suggests that annotating a small stratified sam-
ple and acquiring a larger and more diverse dataset
through active learning is preferable to only using
stratified data. Our results align and complement
past findings showing the benefits of active learning
to maximize performance at a limited cost (Kirk
et al., 2022), including in extremely imbalanced
settings like ours (Tonneau et al., 2022), and help
better understand them through the prism of diver-
sity.
7
Conclusion
This work introduced NAIJAHATE, the largest HSD
dataset to date in the Nigerian context and the first
to contain a representative evaluation set. We also
introduced NAIJAXLM-T, the first pretrained lan-
guage model tailored to Nigerian Twitter. Leverag-
ing these resources, we provided the first evaluation
of HSD in a real-world setting, finding that HSD
performance is largely overestimated by traditional
evaluation approaches. We finally presented the
cost-recall tradeoff at play in human-in-the-loop
moderation, where augmenting the recall comes
with a higher annotation cost. We find that this
moderation approach is effective at moderating a
large share of all hateful content but that the associ-
ated annotation cost is prohibitive for large social
media communities.
While the present work demonstrates the low
real-world performance of HSD and the substantial
cost of hate speech moderation, there are several
possible directions to further improve this perfor-
mance. Based on the hypothesis that hate is ho-
mophilous (Jiang et al., 2023), future work could
use network features to improve HSD performance
(Ahmed et al., 2022). Synthetic data could be used
as well to further increase the number and diver-
sity of examples to train models on (Khullar et al.,
2024). Future work could also evaluate perfor-
mance at the target level to identify hate types that
are harder to detect and develop resources for these.
Further, the moderation analysis could be enhanced
by taking popularity into account and measuring
recall in terms of views of hateful content. Finally,
future work could expand our study to other lan-
guages, countries and platforms in order to evaluate
the external validity of our results and pinpoint ar-
eas where new resources are most needed.
Limitations
Dataset
Low number of positives: The random
set used to evaluate HSD in real-world settings con-
tains 49 hateful examples, which is a very small
number. This number is linked to the very low
prevalence of hate speech in our dataset as well
as our budget constraint which impeded us from
further expanding the annotation effort. While sta-
tistically significant, we acknowledge that our per-
formance results on the random set are necessarily
more uncertain, as illustrated by the larger confi-
dence intervals.

--- Page 10 ---

Limited generalizability to other platforms, time-
frames and linguistic domains: The entirety of our
dataset was sampled from one single social me-
dia platform for a long yet bounded timeframe.
This limits the generalizability of models trained
on our dataset to data from other social media plat-
forms and covering other timespans. Our dataset is
also specific to the Nigerian linguistic context and
may exhibit poorer performance in other English
dialects.
We do not exhaust all targets of hate: The selec-
tion of communities often targeted by hate speech
and frequent on Nigerian Twitter necessarily leaves
out of the analysis other communities even though
they are targeted by online hate speech. In the anno-
tation process, we observed for instance that South
Africans, British people and Men are also targeted
on Nigerian Twitter.
Moderation prior to collection: Our analysis of
moderation considers that the hateful content in our
random sample is representative of all hateful con-
tent on Nigerian Twitter. We acknowledge though
that some hateful content may have been moder-
ated by Twitter before we collected it and that our
estimate of the prevalence of hate speech is nec-
essarily a lower bound estimate. However, based
on publicly available information, we suspect the
enforcement of hate speech removal to be very low
(Giansiracusa, 2021).
Experiments
Other prompts could lead to dif-
ferent results: We craft a prompt using the terms
“hateful” and “offensive” (see App. A.4.4 for de-
tails) which exhibit good performance in past re-
search for HSD using ZSL (Plaza-del arco et al.,
2023b). We do not test other prompts and acknowl-
edge that using other prompts may have an impact
on classification performance.
Ethical considerations
Annotator Wellbeing
Annotators were provided
with clear information regarding the nature of the
annotation task before they began their work. They
received a compensation of 12 US dollars per hour,
which is above the Nigerian minimum wage.
Data Privacy
We collected public tweets through
the Twitter API according to its Terms and Services.
To protect the identity of hateful users and their
victims, we anonymize all tweets in our dataset
upon release, replacing all user names by a fixed
token @USER.
Acknowledgements
We thank Daniel Barkoczi, Khashau Adenike Ele-
buruike, Niyati Malhotra, Haaya Naushan, Arinze
Alex Okoyeugha, Luis Eduardo San Martin, Fatima
Suleiman Sanusi and Philipp Zimmer for their ex-
cellent research assistance. We also thank Alice Gr-
ishchenko for outstanding visual design work. This
work is part of a broader project conducted by the
World Bank Development Impact (DIME) depart-
ment. The study was supported by funding from
the United Kingdom’s Foreign Commonwealth and
Development Office (FCDO) and the World Bank’s
Research Support Budget. This work was also sup-
ported in part through the NYU IT High Perfor-
mance Computing resources, services, and staff
expertise. The findings, interpretations, and conclu-
sions expressed in this paper are entirely those of
the authors. They do not necessarily represent the
views of the International Bank for Reconstruction
and Development/World Bank and its affiliated or-
ganizations or those of the Executive Directors of
the World Bank or the governments they represent.
References
Fatima Muhammad Adam, Abubakar Yakubu Zandam,
and Isa Inuwa-Dutse. 2023. Detection of offensive
and threatening online content in a low resource lan-
guage. arXiv preprint arXiv:2311.10541.
David Ifeoluwa Adelani, Jade Abbott, Graham Neu-
big, Daniel D’souza, Julia Kreutzer, Constantine Lig-
nos, Chester Palen-Michel, Happy Buzaaba, Shruti
Rijhwani, Sebastian Ruder, Stephen Mayhew, Is-
rael Abebe Azime, Shamsuddeen H. Muhammad,
Chris Chinenye Emezue, Joyce Nakatumba-Nabende,
Perez Ogayo, Aremu Anuoluwapo, Catherine Gitau,
Derguene Mbaye, Jesujoba Alabi, Seid Muhie Yi-
mam, Tajuddeen Rabiu Gwadabe, Ignatius Ezeani,
Rubungo Andre Niyongabo, Jonathan Mukiibi, Ver-
rah Otiende, Iroro Orife, Davis David, Samba Ngom,
Tosin Adewumi, Paul Rayson, Mofetoluwa Adeyemi,
Gerald Muriuki, Emmanuel Anebi, Chiamaka Chuk-
wuneke, Nkiruka Odu, Eric Peter Wairagala, Samuel
Oyerinde, Clemencia Siro, Tobius Saul Bateesa,
Temilola Oloyede, Yvonne Wambui, Victor Akin-
ode, Deborah Nabagereka, Maurice Katusiime, Ayo-
dele Awokoya, Mouhamadane MBOUP, Dibora Ge-
breyohannes, Henok Tilaye, Kelechi Nwaike, De-
gaga Wolde, Abdoulaye Faye, Blessing Sibanda, Ore-
vaoghene Ahia, Bonaventure F. P. Dossou, Kelechi
Ogueji, Thierno Ibrahima DIOP, Abdoulaye Diallo,
Adewale Akinfaderin, Tendai Marengereke, and Sa-
lomey Osei. 2021.
MasakhaNER: Named entity
recognition for African languages.
Transactions
of the Association for Computational Linguistics,
9:1116–1131.

--- Page 11 ---

Zo Ahmed, Bertie Vidgen, and Scott A Hale. 2022.
Tackling racial bias in automated online hate detec-
tion: Towards fair and accurate detection of hateful
users with geometric deep learning. EPJ Data Sci-
ence, 11(1):8.
Jesujoba O. Alabi, David Ifeoluwa Adelani, Marius
Mosbach, and Dietrich Klakow. 2022. Adapting pre-
trained language models to African languages via
multilingual adaptive fine-tuning. In Proceedings of
the 29th International Conference on Computational
Linguistics, pages 4336–4349, Gyeongju, Republic
of Korea. International Committee on Computational
Linguistics.
Saminu Mohammad Aliyu, Gregory Maksha Wajiga,
Muhammad Murtala, and Lukman Jibril Aliyu. 2024.
Beyond english: Offensive language detection in low-
resource nigerian languages. In 5th Workshop on
African Natural Language Processing.
Saminu Mohammad Aliyu, Gregory Maksha Wajiga,
Muhammad Murtala, Shamsuddeen Hassan Muham-
mad, Idris Abdulmumin, and Ibrahim Said Ahmad.
2022. Herdphobia: A dataset for hate speech against
fulani in nigeria. arXiv preprint arXiv:2211.15262.
Aymé Arango, Jorge Pérez, and Barbara Poblete. 2019.
Hate speech detection is not as easy as you may think:
A closer look at model validation. In Proceedings
of the 42nd international acm sigir conference on
research and development in information retrieval,
pages 45–54.
Josh Attenberg, Prem Melville, and Foster Provost.
2010. A unified approach to active dual supervision
for labeling features and examples. In Joint Euro-
pean conference on machine learning and knowledge
discovery in databases, pages 40–55. Springer.
Francesco Barbieri, Luis Espinosa Anke, and Jose
Camacho-Collados. 2022.
XLM-T: Multilingual
language models in Twitter for sentiment analysis
and beyond. In Proceedings of the Thirteenth Lan-
guage Resources and Evaluation Conference, pages
258–266, Marseille, France. European Language Re-
sources Association.
Valerio Basile, Cristina Bosco, Elisabetta Fersini,
Debora Nozza, Viviana Patti, Francisco Manuel
Rangel Pardo, Paolo Rosso, and Manuela Sanguinetti.
2019. SemEval-2019 task 5: Multilingual detection
of hate speech against immigrants and women in
Twitter. In Proceedings of the 13th International
Workshop on Semantic Evaluation, pages 54–63, Min-
neapolis, Minnesota, USA. Association for Compu-
tational Linguistics.
Mikhail
Burtsev,
Alexander
Seliverstov,
Rafael
Airapetyan, Mikhail Arkhipov, Dilyara Baymurz-
ina, Nickolay Bushkov, Olga Gureenkova, Taras
Khakhulin, Yuri Kuratov, Denis Kuznetsov, Alexey
Litinsky, Varvara Logacheva, Alexey Lymar, Valentin
Malykh, Maxim Petrov, Vadim Polulyakh, Leonid Pu-
gachev, Alexey Sorokin, Maria Vikhreva, and Marat
Zaynutdinov. 2018. DeepPavlov: Open-source li-
brary for dialogue systems. In Proceedings of ACL
2018, System Demonstrations, pages 122–127, Mel-
bourne, Australia. Association for Computational
Linguistics.
Tommaso Caselli, Valerio Basile, Jelena Mitrovi´c, and
Michael Granitzer. 2021.
HateBERT: Retraining
BERT for abusive language detection in English. In
Proceedings of the 5th Workshop on Online Abuse
and Harms (WOAH 2021), pages 17–25, Online. As-
sociation for Computational Linguistics.
Galo Castillo-lópez, Arij Riabi, and Djamé Seddah.
2023. Analyzing zero-shot transfer scenarios across
Spanish variants for hate speech detection. In Tenth
Workshop on NLP for Similar Languages, Varieties
and Dialects (VarDial 2023), pages 1–13, Dubrovnik,
Croatia. Association for Computational Linguistics.
Alexis Conneau, Kartikay Khandelwal, Naman Goyal,
Vishrav Chaudhary, Guillaume Wenzek, Francisco
Guzmán, Edouard Grave, Myle Ott, Luke Zettle-
moyer, and Veselin Stoyanov. 2020. Unsupervised
cross-lingual representation learning at scale. In Pro-
ceedings of the 58th Annual Meeting of the Asso-
ciation for Computational Linguistics, pages 8440–
8451, Online. Association for Computational Lin-
guistics.
Aida Mostafazadeh Davani, Mark Díaz, Dylan Baker,
and Vinodkumar Prabhakaran. 2024. D3code: Disen-
tangling disagreements in data across cultures on of-
fensiveness detection and evaluation. arXiv preprint
arXiv:2404.10857.
Thomas Davidson, Dana Warmsley, Michael Macy, and
Ingmar Weber. 2017. Automated hate speech detec-
tion and the problem of offensive language. Eleventh
International AAAI Conference on Web and Social
Media, 11(1).
Christian Ezeibe. 2021. Hate speech and election vio-
lence in nigeria. Journal of Asian and African Stud-
ies, 56(4):919–935.
RO Farinde and HO Omolaiye. 2020.
A socio-
pragmatic investigation of language of insults in the
utterances of yoruba natives in nigeria. Advances in
Language and Literary Studies, 11(6):1–6.
W Ferroggiaro. 2018.
Social media and conflict in
nigeria: A lexicon of hate speech terms.
Iginio Gagliardone, Matti Pohjonen, Zenebe Beyene,
Abdissa Zerai, Gerawork Aynekulu, Mesfin Bekalu,
Jonathan Bright, Mulatu Alemayehu Moges, Michael
Seifu, Nicole Stremlau, et al. 2016.
Mechachal:
Online debates and elections in ethiopia-from hate
speech to engagement in social media. Available at
SSRN 2831369.
Sayan Ghosh, Dylan Baker, David Jurgens, and Vin-
odkumar Prabhakaran. 2021.
Detecting cross-
geographic biases in toxicity modeling on social me-
dia. In Proceedings of the Seventh Workshop on

--- Page 12 ---

Noisy User-generated Text (W-NUT 2021), pages
313–328, Online. Association for Computational Lin-
guistics.
N Giansiracusa. 2021. Facebook uses deceptive math
to hide its hate speech problem. Wired.
Tarleton Gillespie. 2018. Custodians of the Internet:
Platforms, content moderation, and the hidden deci-
sions that shape social media. Yale University Press.
Tarleton Gillespie. 2020.
Content moderation, ai,
and the question of scale.
Big Data & Society,
7(2):2053951720943234.
Robert Gorwa, Reuben Binns, and Christian Katzen-
bach. 2020. Algorithmic content moderation: Tech-
nical and political challenges in the automation
of platform governance.
Big Data & Society,
7(1):2053951719897945.
Keyan Guo, Alexander Hu, Jaden Mu, Ziheng Shi, Zim-
ing Zhao, Nishant Vishwamitra, and Hongxin Hu.
2024. An investigation of large language models
for real-world hate speech detection. arXiv preprint
arXiv:2401.03346.
Suchin
Gururangan,
Ana
Marasovi´c,
Swabha
Swayamdipta, Kyle Lo, Iz Beltagy, Doug Downey,
and Noah A. Smith. 2020. Don’t stop pretraining:
Adapt language models to domains and tasks. In
Proceedings of the 58th Annual Meeting of the
Association for Computational Linguistics, pages
8342–8360, Online. Association for Computational
Linguistics.
Pengcheng He, Jianfeng Gao, and Weizhu Chen. 2021.
Debertav3: Improving deberta using electra-style pre-
training with gradient-disentangled embedding shar-
ing. arXiv preprint arXiv:2111.09543.
Comfort Eseohen Ilevbare, Jesujoba O Alabi, David Ife-
oluwa Adelani, Firdous Damilola Bakare, Oluwa-
toyin Bunmi Abiola,
and Oluwaseyi Adesina
Adeyemo. 2024. Ekohate: Abusive language and
hate speech detection for code-switched political
discussions on nigerian twitter.
arXiv preprint
arXiv:2404.18180.
Julie Jiang, Luca Luceri, Joseph B Walther, and Emilio
Ferrara. 2023.
Social approval and network ho-
mophily as motivators of online toxicity.
arXiv
preprint arXiv:2310.07779.
Rafael Jiménez Durán. 2021. The economics of content
moderation: Theory and experimental evidence from
hate speech on twitter. Available at SSRN 4044098.
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
Omrani, Yehsong Kim, Kris Coombs, Shreya
Havaldar,
Gwenyth Portillo-Wightman,
Elaine
Gonzalez, et al. 2022.
Introducing the gab hate
corpus: defining and applying hate-based rhetoric to
social media posts at scale. Language Resources and
Evaluation, pages 1–30.
Aman Khullar, Daniel Nkemelu, V Cuong Nguyen, and
Michael L Best. 2024. Hate speech detection in lim-
ited data contexts using synthetic data generation.
ACM Journal on Computing and Sustainable Soci-
eties, 2(1):1–18.
Hannah Kirk, Bertie Vidgen, and Scott Hale. 2022.
Is more data better?
re-thinking the importance
of efficiency in abusive language detection with
transformers-based active learning. In Proceedings
of the Third Workshop on Threat, Aggression and
Cyberbullying (TRAC 2022), pages 52–61, Gyeongju,
Republic of Korea. Association for Computational
Linguistics.
Vivian Lai, Samuel Carton, Rajat Bhatnagar, Q Vera
Liao, Yunfeng Zhang, and Chenhao Tan. 2022.
Human-ai collaboration via conditional delegation:
A case study of content moderation. In Proceedings
of the 2022 CHI Conference on Human Factors in
Computing Systems, pages 1–18.
Nayeon Lee, Chani Jung, Junho Myung, Jiho Jin, Juho
Kim, and Alice Oh. 2023. Crehate: Cross-cultural
re-annotation of english hate speech dataset. arXiv
preprint arXiv:2308.16705.
Alyssa Lees, Vinh Q Tran, Yi Tay, Jeffrey Sorensen, Jai
Gupta, Donald Metzler, and Lucy Vasserman. 2022.
A new generation of perspective api: Efficient multi-
lingual character-level transformers. In Proceedings
of the 28th ACM SIGKDD Conference on Knowledge
Discovery and Data Mining, pages 3197–3207.
Peiyu Li. 2021. Achieving hate speech detection in a
low resource setting. Ph.D. thesis, Utah State Univer-
sity.
Zehan Li, Xin Zhang, Yanzhao Zhang, Dingkun Long,
Pengjun Xie, and Meishan Zhang. 2023. Towards
general text embeddings with multi-stage contrastive
learning. arXiv preprint arXiv:2308.03281.
Philipp
Lorenz-Spreen,
Lisa
Oswald,
Stephan
Lewandowsky, and Ralph Hertwig. 2023. A system-
atic review of worldwide causal and correlational
evidence on digital media and democracy. Nature
human behaviour, 7(1):74–101.
Ruth Maclean. 2021. Nigeria bans twitter after presi-
dent’s tweet is deleted. The New York Times.
Todor Markov, Chong Zhang, Sandhini Agarwal, Flo-
rentine Eloundou Nekoul, Theodore Lee, Steven
Adler, Angela Jiang, and Lilian Weng. 2023. A holis-
tic approach to undesired content detection in the real
world. In Proceedings of the AAAI Conference on Ar-
tificial Intelligence, volume 37, pages 15009–15018.
Binny Mathew, Punyajoy Saha, Seid Muhie Yimam,
Chris Biemann, Pawan Goyal, and Animesh Mukher-
jee. 2021. Hatexplain: A benchmark dataset for ex-
plainable hate speech detection. In Proceedings of
the AAAI Conference on Artificial Intelligence, vol-
ume 35, pages 14867–14875.

--- Page 13 ---

Dan Milmo. 2021. Frances haugen: ‘i never wanted to
be a whistleblower. but lives were in danger’. The
Guardian.
Mainack Mondal, Leandro Araújo Silva, and Fabrí-
cio Benevenuto. 2017.
A measurement study of
hate speech in social media. In Proceedings of the
28th ACM conference on hypertext and social media,
pages 85–94.
Karsten Müller and Carlo Schwarz. 2021. Fanning the
flames of hate: Social media and hate crime. Journal
of the European Economic Association, 19(4):2131–
2167.
Joseph Nda Ndabula, Oyenike Mary Olanrewaju, and
Faith O Echobu. 2023. Detection of hate speech
code mix involving english and other nigerian lan-
guages. Journal of Information Systems and Infor-
matics, 5(4):1416–1431.
Isar Nejadgholi and Svetlana Kiritchenko. 2020. On
cross-dataset generalization in automatic detection of
online abuse. In Proceedings of the Fourth Workshop
on Online Abuse and Harms, pages 173–183, Online.
Association for Computational Linguistics.
Dat Quoc Nguyen, Thanh Vu, and Anh Tuan Nguyen.
2020. BERTweet: A pre-trained language model
for English tweets. In Proceedings of the 2020 Con-
ference on Empirical Methods in Natural Language
Processing: System Demonstrations, pages 9–14, On-
line. Association for Computational Linguistics.
Debora Nozza. 2021. Exposing the limits of zero-shot
cross-lingual hate speech detection. In Proceedings
of the 59th Annual Meeting of the Association for
Computational Linguistics and the 11th International
Joint Conference on Natural Language Processing
(Volume 2: Short Papers), pages 907–914, Online.
Association for Computational Linguistics.
Kelechi Ogueji, Yuxin Zhu, and Jimmy Lin. 2021.
Small data? no problem! exploring the viability
of pretrained multilingual language models for low-
resourced languages. In Proceedings of the 1st Work-
shop on Multilingual Representation Learning, pages
116–126, Punta Cana, Dominican Republic. Associa-
tion for Computational Linguistics.
Paul Ayodele Onanuga. 2023. # arewaagainstlgbtq dis-
course: a vent for anti-homonationalist ideology in
nigerian twittersphere? African Identities, 21(4):703–
725.
Umaru A Pate and Adamkolo Mohammed Ibrahim.
2020. Fake news, hate speech and nigeria’s struggle
for democratic consolidation: A conceptual review.
Handbook of research on politics in the computer
age, pages 89–112.
Flor Miriam Plaza-del arco, Debora Nozza, and Dirk
Hovy. 2023a. Leveraging label variation in large
language models for zero-shot text classification.
Flor Miriam Plaza-del arco, Debora Nozza, and Dirk
Hovy. 2023b. Respectful or toxic? using zero-shot
learning with language models to detect hate speech.
In The 7th Workshop on Online Abuse and Harms
(WOAH), pages 60–68, Toronto, Canada. Association
for Computational Linguistics.
Paul Rottger, Bertie Vidgen, Dirk Hovy, and Janet Pier-
rehumbert. 2022. Two contrasting data annotation
paradigms for subjective NLP tasks. In Proceedings
of the 2022 Conference of the North American Chap-
ter of the Association for Computational Linguis-
tics: Human Language Technologies, pages 175–190,
Seattle, United States. Association for Computational
Linguistics.
Paul Röttger, Bertie Vidgen, Dong Nguyen, Zeerak
Waseem, Helen Margetts, and Janet Pierrehumbert.
2021. HateCheck: Functional tests for hate speech
detection models. In Proceedings of the 59th An-
nual Meeting of the Association for Computational
Linguistics and the 11th International Joint Confer-
ence on Natural Language Processing (Volume 1:
Long Papers), pages 41–58, Online. Association for
Computational Linguistics.
Diptanu Sarkar, Marcos Zampieri, Tharindu Ranas-
inghe, and Alexander Ororbia. 2021. fBERT: A neu-
ral transformer for identifying offensive content. In
Findings of the Association for Computational Lin-
guistics: EMNLP 2021, pages 1792–1798, Punta
Cana, Dominican Republic. Association for Compu-
tational Linguistics.
Mohit Singhal, Chen Ling, Pujan Paudel, Poojitha
Thota, Nihal Kumarswamy, Gianluca Stringhini, and
Shirin Nilizadeh. 2023. Sok: Content moderation in
social media, from guidelines to enforcement, and re-
search to practice. In 2023 IEEE 8th European Sym-
posium on Security and Privacy (EuroS&P), pages
868–895. IEEE.
Miriah Steiger, Timir J Bharucha, Sukrit Venkatagiri,
Martin J Riedl, and Matthew Lease. 2021. The psy-
chological well-being of content moderators: the
emotional labor of commercial moderation and av-
enues for improving support. In Proceedings of the
2021 CHI conference on human factors in computing
systems, pages 1–14.
Manuel Tonneau, Dhaval Adjodah, Joao Palotti, Nir
Grinberg, and Samuel Fraiberger. 2022. Multilingual
detection of personal employment status on Twitter.
In Proceedings of the 60th Annual Meeting of the
Association for Computational Linguistics (Volume
1: Long Papers), pages 6564–6587, Dublin, Ireland.
Association for Computational Linguistics.
Manuel Tonneau, Diyi Liu, Samuel Fraiberger, Ralph
Schroeder, Scott A Hale, and Paul Röttger. 2024.
From languages to geographies: Towards evaluating
cultural bias in hate speech datasets. arXiv preprint
arXiv:2404.17874.
Collins Udanor and Chinatu C Anyanwu. 2019. Com-
bating the challenges of social media hate speech in a

--- Page 14 ---

polarized society: A twitter ego lexalytics approach.
Data Technologies and Applications.
Bertie Vidgen, Scott Hale, Ella Guest, Helen Mar-
getts, David Broniatowski, Zeerak Waseem, Austin
Botelho, Matthew Hall, and Rebekah Tromble. 2020.
Detecting East Asian prejudice on social media. In
Proceedings of the Fourth Workshop on Online Abuse
and Harms, pages 162–172, Online. Association for
Computational Linguistics.
Bertie Vidgen, Helen Margetts, and Alex Harris. 2019.
How much online abuse is there. Alan Turing Insti-
tute, 11.
Ellen M Voorhees, Donna K Harman, et al. 2005. TREC:
Experiment and evaluation in information retrieval,
volume 63. MIT press Cambridge.
Zeerak Waseem and Dirk Hovy. 2016. Hateful symbols
or hateful people? predictive features for hate speech
detection on Twitter. In Proceedings of the NAACL
Student Research Workshop, pages 88–93, San Diego,
California. Association for Computational Linguis-
tics.
Michael Wiegand, Josef Ruppenhofer, and Thomas
Kleinbauer. 2019. Detection of Abusive Language:
the Problem of Biased Datasets. In Proceedings of
the 2019 Conference of the North American Chap-
ter of the Association for Computational Linguistics:
Human Language Technologies, Volume 1 (Long and
Short Papers), pages 602–608, Minneapolis, Min-
nesota. Association for Computational Linguistics.
Marcos Zampieri, Shervin Malmasi, Preslav Nakov,
Sara Rosenthal, Noura Farra, and Ritesh Kumar.
2019. Predicting the type and target of offensive
posts in social media. In Proceedings of the 2019
Conference of the North American Chapter of the
Association for Computational Linguistics: Human
Language Technologies, Volume 1 (Long and Short
Papers), pages 1415–1420, Minneapolis, Minnesota.
Association for Computational Linguistics.

--- Page 15 ---

A
Experimental details
A.1
Data collection
A.1.1
Word lists
In this section, we provide the detailed lists of slurs
and communities specific to Nigerian hate speech
(Table 4). Summary statistics on the number of
words per category can be found in Table 7.
Hate words
We first build a list of 89 Nigeria-
specific slurs, which are referred to as hate words
thereafter. To do so, we rely on lexicons from
past work on the topic (Ferroggiaro, 2018; Udanor
and Anyanwu, 2019; Farinde and Omolaiye, 2020),
Nigerian online dictionaries such as Naija Lingo
as well as local knowledge from our Nigerian col-
leagues. The final list contains two types of words:
regular slurs (n=84) and words combining a slur
and community name, such as “fulanimal” (n=5).
The list of 84 regular slurs contains 28 Yoruba
words, 26 English words, 12 Hausa words, 11 Pid-
gin words and 7 Igbo words. We detail the full list
of hate words in Table 4.
Community names
Second, we define a list of
names of communities that are often targeted by
hate speech in Nigeria, again relying on past work
(Onanuga, 2023) and local knowledge from Nige-
rian colleagues. We build an initial list (see Table
5 for the full list of considered and retained com-
munity names) and we then restrict this initial list
of community names to the names that are most
frequently mentioned on Nigerian Twitter. This
approach yields 12 communities, including 5 eth-
nic groups (Yoruba, Igbo, Hausa, Fulani, Herds-
men), 2 religious groups (Christians and Muslims),
3 regional groups (Northern, Southern, Eastern)
and 2 groups on gender identity and sexual ori-
entation (Women and LGBTQ+). As mentioned
earlier, Herdsmen are not a ethnic group per se
but this term refers exclusively to Fulani herdsmen
in the Nigerian context, hence the categorization
as an ethnic group. For each of these groups, we
list the different denominations of each group as
well as their plural form and combine it in regular
expressions (see Table 6). Finally, we also iden-
tify 5 words combining a community name with a
derogatory word (e.g., “fulanimal”) that we coin
combined word thereafter. Since some targets are
very rare in the annotated data, we decide to bundle
the 12 communities into 5 groups: North (North-
ern, Hausa, Fulani, Herdsmen), South (Southern,
Yoruba), East (Igbo, Biafra), Women, Muslim and
Other (Christian, LGBTQ+).
A.1.2
Sampling and evaluation sets
We draw two distinct random samples of 100 mil-
lion tweets each, one for sampling and model train-
ing Ds and the other one for evaluation De.
A.1.3
Stratified sample
As previously stated, the extreme imbalance in our
classification task makes random sampling ineffec-
tive and prohibitively expensive. With the aim to
build high-performing classifiers at a reasonable
cost, we build and annotate a stratified sample of
tweets from Ds. We use three different sampling
strategies to build this stratified sample. First, for
each possible combination of community name and
hate word, we sample up to 4 tweets that both con-
tain the respective hate word and match with the
respective community regular expression. The sub-
set of tweets containing both the hate word and
the community regular expression may be smaller
than 4 and we sample the full subset in that case.
Second, for each combined word W, we randomly
sample 50 tweets containing W. Some combined
words occur at a very low frequency such that the
sample size is sometimes smaller than 50. Finally,
for each community, we draw 50 random tweets
matching the community regular expression, in or-
der to avoid having a classifier that associates the
community name with hate speech.
This yields a stratified sample of 1,607 tweets
annotated as either hateful, offensive or neutral.
A.1.4
Active learning sample
Each active learning iteration samples a total of
100 tweets. The type of active learning method we
employ is called certainty sampling and consists
in sampling instances at the top of the score dis-
tribution in order to annotate false positives and
maximize precision. Specifically, each iteration i
consists of:
• Model training: we train a model on all of the
labels we have, that is the stratified sample
and the combination of all Active Learning
samples from prior iterations
• Inference: we then deploy this model on Ds
and rank all tweets based on their BERT con-
fidence score.
• Sampling and annotating: we define 5 rank
buckets as: [1, 103], [103, 104], [104, 105],

--- Page 16 ---

Hate Keyword
Language
Translation
Source
stupid
english
animal|animals
english
baboon|baboons
english
bastard|bastards
english
bitch|bitches
english
bum|bums
english
cockroach|cockroaches
english
coconut head|coconut heads
english
disgusting
english
dog|dogs
english
dumb|dumb
english
fanatic|fanatics
english
fool|fools
english
idiot|idiots
english
liar|liars
english
moron|morons
english
parasite|parasites
english
pig|pigs
english
primitive|primitives
english
rape|rapes|raping
english
scum|scums
english
shit|shits
english
slut|sluts
english
useless
english
vulture|vultures
english
whore|whores
english
aboki|abokai
hausa
"friend; used by a non-Hausa person may be derogatory"
https://www.bellanaija.com
/2020/04/twitter-aboki-der
ogatory-term/
arne|arna
hausa
"pagan - used by muslims to reference christians in the north"
ashana
hausa
prostitute
http://naijalingo.com/wor
ds/ashana
barawo|barayi
hausa
thief
http://naijalingo.com/wor
ds/barawo
bolo
yoruba
fool
http://naijalingo.com/wor
ds/bolo
kafir|kafirai
hausa
"used by muslims to refer to non-muslims"
mallam|malamai
hausa
"teacher; used specifically in southern Nigeria in derogatory manner to refer to all Northerners; in Northern Nigeria, is used as a mark of respect"
malo|malos
hausa
fool
mugu
hausa
wicked/evil
http://naijalingo.com/wor
ds/mugu
mugun
hausa
fool
http://naijalingo.com/wor
ds/mugun
mungu
hausa
fool
http://naijalingo.com/wor
ds/mungu
wawa|wawaye
hausa
idiot
zuwo
hausa
fool
http://naijalingo.com/wor
ds/zuwo
anuofia|ndi anofia
igbo
wild animal
aturu
igbo
sheep
Udanor and Anyanwu (2019)
efulefu|ndi fulefu
igbo
worthless man
ewu
igbo
imi nkita
igbo
dog nose
https://www.vanguardngr.co
m/2019/11/of-yariba-nyami
ri-and-aboki/
onye nzuzu|ndi nzuzu
igbo
onye oshi|ndi oshi
igbo
thief
http://naijalingo.com/wor
ds/onye-oshi
ashawo|ashawos
pidgin
prostitute
http://naijalingo.com/wor
ds/ashawo
ashewo|ashewos|awon ashewo
pidgin
prostitute
http://naijalingo.com/wor
ds/ashewo
ashy
pidgin
dirty
mumu|mumus
pidgin
idiot
mumuni
pidgin
very stupid person
http://naijalingo.com/wor
ds/mumuni
sharrap
pidgin
shut up
http://naijalingo.com/wor
ds/sharrap
tief
pidgin
thief
http://naijalingo.com/wor
ds/tief
tiff
pidgin
thief
http://naijalingo.com/wor
ds/tiff
waka jam
pidgin
an insult/curse towards you and loved ones
http://naijalingo.com/wor
ds/waka-jam
agba iya|awon agba iya
yoruba
older person, who despite his age, is still useless
https://www.legit.ng/10319
44-8-insults-yoruba-mothe
rs-use-will-reset-brain.h
tml
agbaya
yoruba
derogatory word against old people
agbero|agberos|awon agbero
yoruba
used to describe manual laborers from lower economic classes; sometimes deployed on twitter for ad hominem attacks
https://en.wiktionary.org/
wiki/agbero
akpamo
yoruba
fool
http://naijalingo.com/wor
ds/akpamo
apoda|awon apoda
yoruba
who is confused, lost direction
https://www.legit.ng/10319
44-8-insults-yoruba-mothe
rs-use-will-reset-brain.h
tml
arindin|awon arindi
yoruba
acts like an idiot
https://www.nairaland.com/
3237758/she-called-him-ari
ndin-sitting
arro
yoruba
stupid person
http://naijalingo.com/wor
ds/arro
atutupoyoyo
yoruba
ugly being
http://naijalingo.com/wor
ds/atutupoyoyo
ayama
yoruba
disgusting
http://naijalingo.com/wor
ds/ayama
ayangba
yoruba
prostitute
didirin|awon didirin
yoruba
stupid
https://www.legit.ng/10319
44-8-insults-yoruba-mothe
rs-use-will-reset-brain.h
tml
eyankeyan
yoruba
synonym to lasan
Farinde and Omolaiye (2020)
lasan
yoruba
ordinary; when combined with a community name, may mean that this group is inferior to Yorubas
Farinde and Omolaiye (2020)
malu|awon malu
yoruba
cow
obun|awon obun
yoruba
dirty
https://www.legit.ng/10319
44-8-insults-yoruba-mothe
rs-use-will-reset-brain.h
tml
ode|awon ode
yoruba
stupid
https://www.legit.ng/10319
44-8-insults-yoruba-mothe
rs-use-will-reset-brain.h
tml
odoyo
yoruba
very stupid person
http://naijalingo.com/wor
ds/odoyo
ole|awon ole
yoruba
thief
Udanor and Anyanwu (2019)
olodo|olodos|awon olodo
yoruba
stupid
https://www.legit.ng/10319
44-8-insults-yoruba-mothe
rs-use-will-reset-brain.h
tml
oloshi|awon oloshi
yoruba
unfortunate, who does rubbish a lot, criminal
https://www.legit.ng/10319
44-8-insults-yoruba-mothe
rs-use-will-reset-brain.h
tml
omo ale|awon omo ale
yoruba
bastard
Farinde and Omolaiye (2020)
oponu|awon aoponu
yoruba
idiot
https://www.legit.ng/10319
44-8-insults-yoruba-mothe
rs-use-will-reset-brain.h
tml
ota|awon ota
yoruba
enemy
http://naijalingo.com/wor
ds/ota
owo
yoruba
fool
suegbe
yoruba
idiot
http://naijalingo.com/wor
ds/suegbe
werey|awon weyre
yoruba
crazy, mad
http://naijalingo.com/wor
ds/werey
yeye|awon akin yeye
yoruba
useless
Udanor and Anyanwu (2019)
jeri
pidgin
fool
http://naijalingo.com/wor
ds/jeri
shalam
pidgin
biafrat|biafraud
combined
targeting Biafra
fulanimal
combined
targeting Fulanis
yorubastard|yariba|yorobber
combined
targeting Yorubas
baby factory|baby factories
combined
targeting Igbo
niyamiri
combined
Table 4: Slurs used in the Nigerian context

--- Page 17 ---

Community word
Frequency
Retained
christian
1.88E-03
yes
muslim
2.10E-03
yes
northern
1.25E-03
yes
southern
5.30E-04
yes
hausa
7.12E-04
yes
fulani
8.81E-04
yes
yoruba
1.37E-03
yes
igbo
1.52E-03
yes
women
4.93E-03
yes
biafra
1.60E-03
yes
arewa
1.30E-03
yes
LGBTQ+
1.12E-03
yes
herdsmen
7.49E-04
yes
eastern
2.09E-04
yes
tiv
3.98E-05
no
kanuri/beriberi
1.82E-05
no
ibibio
1.45E-05
no
ijaw/izon
6.02E-05
no
buharist
1.15E-04
no
ipobite
6.22E-08
no
arne
3.82E-06
no
transgender
3.83E-05
no
middle belt
3.45E-05
no
jukun
6.93E-06
no
Niger Delta
2.42E-04
no
yorubawa
4.07E-07
no
berom
4.84E-05
no
Table 5: List of considered community words and their
frequency in the Twitter dataset. The frequency for each
word corresponds to the number of tweets containing
the word divided by the total number of tweets.
[105, 106], [106, 107].
We then sample n
tweets per rank bucket and annotate this sam-
ple.
We conduct a total of 25 iterations, of which
10 are conducted on the subset of Ds containing
community keywords and 15 on the full Ds. In our
active learning process, three separate phases can
be distinguished:
• iterations 1-10:
– the sampling is done on the subset of Ds
containing community words
– the active learning process is done sep-
arately for the hateful and the offensive
classes
– the value of n equals 10
– the overall sample size per iteration is
100 and equals to 5 buckets x n=10 x 2
classes (hateful and offensive)
• iterations 10-19
– the sampling is done on the full sampling
set Ds
– the active learning process is done sep-
arately for the hateful and the offensive
classes
– the value of n equals 10
– the overall sample size per iteration is
100 and equals to 5 buckets x n=10 x 2
classes (hateful and offensive)
• iterations 20-24
– the sampling is done on the full sampling
set Ds
– the active learning process is done only
for the hateful class
– the value of n equals 20
– the overall sample size per iteration is
100 and equals to 5 buckets x n=20 x 1
class (hateful)
A.2
Annotation
A.2.1
Annotation team
The annotation team was composed of a Hausa
man, a Hausa-Fulani woman, an Igbo man and a
Yoruba woman.
A.2.2
Annotation guidelines
Offensive tweets
For tweets to be offensive, but
not hateful, a tweet must satisfy all of the following
criteria.
• The hate keyword is being used as pejorative
towards another individual or group, and this
group is not one of our communities.
– A personal attack against another in-
dividual, that does not mention a pro-
tected attribute such as, race, ethnicity,
national origin, disability, religious af-
filiation, caste, sexual orientation, sex,
gender identity and serious disease.
– An insult towards a group based on non-
protected attributes, such as, hobbies,
fandom (e.g., sports, comic books).
• It is not offensive if the hate keyword is not
being used on an individual or group.

--- Page 18 ---

Community
Regular expression
christian
christian|christians
muslim
muslim|muslims|islam|islamic
northern
northern|northerner|northerners|arewa|almajiri
southern
southern|southerner|southerners
hausa
hausa|hausas
fulani
fulani|fulanis
yoruba
yoruba|yorubas
igbo
igbo|ibo|ibos|igbos
women
women|woman|girl|girls|female|females
lgbt
lgbt|lgbtq|lgbtq+|gay|gays|lesbian|lesbians|transgender|transgenders
herdsmen
herdsmen|herdsman
eastern
eastern|easterner|easterners|biafra
Table 6: Community Regex Mapping
Word category
Number of words
Community names
12
English hate words
26
Non-English hate words
58
Combined words
5
Total number of hate words (in all lan-
guages)
84
Total number of hate words, including
combined words (in all languages)
89
Table 7: Summary statistics on the number of words per
category
– Not offensive if directed towards inan-
imate objects, abstract concepts (that
do not have religious or cultural signifi-
cance) or animals (unless the animal is
used as a negative metaphor to describe
a community). We define these as “out-
of-scope entities” (Röttger et al., 2021).
• It is not offensive if the hate word is self-
referential.
This would account for some
types of sarcasm, or humour via self depreca-
tion.
• It is not offensive if the hate word is used for
emphasis without being directed towards an
individual or group. Several offensive words
such as “shit” or “stupid” can be used as ex-
clamations.
• If the hate word is being used ambiguously
(not recognizable as pejorative), then it is of-
fensive if your answer is yes to one of these
questions.
– Can you imagine that someone might be
offended by this? (err on the side of cau-
tion, aim for the lower bound)
– Would Twitter potentially detect it as an
insult and make the user verify before
posting?
Hateful tweets
This section is adapted from
(Waseem and Hovy, 2016; Basile et al., 2019) and
Facebook Community Standards7. For tweets to be
hateful, instead of merely offensive, the tweet must
satisfy one or more of the following criteria:
• Uses a sexist, racial or homophobic slur.
– Misogyny/Sexist slurs to be defined as
a statement that expresses hate towards
women in particular (in the form of in-
sulting, sexual harassment, threats of vi-
olence, stereotype, objectification and
negation of male responsibility).
– Racial slurs to be defined as an insult that
is designed to denigrate others based on
their race or ethnicity.
– Homophobic slurs to be defined as an
insult that is designed to denigrate other
on the basis of sexuality. This includes
slurs targeted towards specific LGBTQ+
communities, such as transphobic slurs.
– Usage of slur must not constitute a “re-
claiming” of negative terms by the com-
munity in question. For instance, the n*
word or “fag” or “bitch”.
• Attacks a minority.
– Minorities to be defined as a group based
on protected characteristics: race, ethnic-
ity, national origin, disability, religious
7https://transparency.fb.com/en-gb/policies/community-
standards/hate-speech/

--- Page 19 ---

affiliation, caste, sexual orientation, sex,
gender identity and serious disease.
– Attack to be defined as violent or dehu-
manizing speech, harmful stereotypes,
statements of inferiority, expressions of
contempt, disgust or dismissal, cursing
and calls for exclusion or segregation.
– Seeks to silence a minority.
– Criticizes a minority (without a well
founded argument).
* Criticizes a minority and uses a straw
man argument.
* Blatantly misrepresents truth or
seeks to distort views on a minority
with unfounded claims.
– Negatively stereotypes a minority. Neg-
ative stereotypes to be defined as dehu-
manizing comparisons that have histori-
cally been used to attack, intimidate, or
exclude specific groups.
– Promotes, but does not directly use, hate
speech or violent crime.
* Shows support of problematic hash-
tags. e.g.,“#BanIslam”
* Defends xenophobia, racism, sexism,
homophobia or other types of intoler-
ance and bigotry.
– If it is a retweet, it must indicate sup-
port for the original tweet. People some-
times share content that includes some-
one else’s hate speech to condemn it or
raise awareness.
A.3
Language distribution
We ask the annotators to characterize the language
of a random sample of 500 tweets, both for the
stratified and active learning sets and for the ran-
dom sample. We report the language distribution
in Table 8.
A.4
Models
A.4.1
Number of parameters
Conversational BERT has 110 million parameters.
The XLM models, BERTweet and AfriBERTa have
125 million parameters. The DeBERTaV3 mod-
els have 86 million parameters. The number of
parameters for GPT3.5 is undisclosed by OpenAI.
A.4.2
Pretraining of NaijaXLM-T
We followed Alabi et al. (2022) and performed an
adaptive fine tuning of XLM-R (Conneau et al.,
2020) on our Twitter dataset. We kept the same
vocabulary as XLM-R and trained the model for
one epoch, using 1% of the dataset as validation
set. The training procedure was conducted in a
distributed environment, for approximately 10 days,
using 4 nodes with 4 RTX 8000 GPUs each, with a
total batch size of 576.
A.4.3
Supervised Learning
Hyperparameter tuning
Hyperparameter tun-
ing was conducted in a 5-fold cross validation train-
ing. A grid search was run testing different learning
rates (from 1e-5 to 5e-5). The cross validation train-
ings were conducted for 10 epochs. The batch size
used was 8, and three different seeds were used
for each learning rate. We used F1-score as early
stopping metric for hate speech detection models.
The best results were averaged across the seeds,
and the best combination after the grid search was
picked as the resulting model.
Computing infrastructure
For supervised learn-
ing, we used either V100 (32GB) or RTX8000
(48GB) GPUs for finetuning. The average runtime
for finetuning is 45 minutes. Inferences from off-
the-shelf models were ran locally on a laptop CPU.
A.4.4
Off-the-shelf models
Perspective
API
We
used
the
IDEN-
TITY_ATTACK category for HSD with Per-
spective API as it is the closest to our hate speech
definition. This is a binary classification problem
and the API outputs a score between 0 and 1. The
inferences were run on February 1, 2024.
GPT3.5
We use the gpt-3.5-turbo-0613 model.
The prompt used for zero-shot predictions with this
model is: "Now consider this message : ’[TWEET]’
Respond 0 if this message is neutral, 1 if this mes-
sage is offensive and 2 if this message is hateful. It
is very important that you only respond the number
(e.g., ’0’, ’1’ or ’2’)."
The prompt is run 5 times for each tweet. We
then define the hateful score as the share of the 5
times for which the model predicted that the tweet
was hateful. We then use this score to compute the
average precision. We use all default values for the
main hyperparameters, including 1 for temperature.
A.4.5
Evaluation results
We provide the diversity results for the holdout and
the top-scored sets in Figure 5. We also provide

--- Page 20 ---

Stratified + active learning sets
Random set
English
74.2
77
English & Nigerian Pidgin
11
1.5
English & Yoruba
4.2
-
Nigerian Pidgin
3.6
7.3
English & Hausa
2.2
-
Hausa
1
1.2
Yoruba
-
1
URLs
-
6
Emojis
-
2.3
Table 8: Share of each language across datasets (in %). Hyphens indicate that the value is under 1%.
the precision-recall curve for NaijaXLM-T on the
random sample in Figure 4.
Precision
Recall
NaijaXLM-T (full)
0.2
0.0
0.4
0.6
0.8
1.0
0.0
0.2
0.4
0.6
0.8
1.0
Figure 4: Precision-recall curve on the random set
A.4.6
Human-in-the-loop moderation
In the human-in-the-loop setting, we compute the
proportion of all tweets to be reviewed by human
annotators as follows. We first compute the number
of predicted positives PP:
PP = TP + FP = TP/precision
PP = (recall ∗(TP + FN))/precision
PP = (recall ∗total # hateful tweets)/precision
PP = (recall∗base rate∗total # tweets)/precision
We then derive the share S of all tweets that
are predicted positive by a given model, that is the
share of all tweets that will be reviewed by human
moderators in a human-in-the-loop approach, by
dividing PP by the total number of tweets:
S = (recall ∗base rate)/precision
with the base rate equal to the prevalence of hate-
ful content which is 0.16%. We finally use the pre-
cision and recall values from the precision-recall
curve to derive the curve illustrating the relation-
ship between recall and S.

--- Page 21 ---

StraƟﬁed downsampled (N = 1,507)
AcƟve learning downsampled (N = 1,507)
StraƟﬁed + acƟve learning (N = 4,012)
Average Precision
Average Precision
NaijaXLM-T (full)
NaijaXLM-T (198M)
BERTweet
DeBERTaV3
AfroXLM-R
Conv. BERT
XLM-T
XLM-R
XLM-R Naija
fBERT
AfriBERTa
HateBERT
mDeBERTaV3
0.0
0.2
0.4
0.6
0.8
1.0
0.0
0.2
0.4
0.6
0.8
1.0
NaijaXLM-T (full)
NaijaXLM-T (198M)
BERTweet
DeBERTaV3
AfroXLM-R
Conv. BERT
XLM-T
XLM-R
XLM-R Naija
fBERT
AfriBERTa
HateBERT
mDeBERTaV3
0.0
0.2
0.4
0.6
0.8
1.0
0.0
0.2
0.4
0.6
0.8
1.0
Figure 5: Average precision on the holdout and top-scored sets across models trained on the downsampled stratified
set, the downsampled active learning set and the full training set, composed of the stratified and active learning sets.
Error bars indicate 95% bootstrapped confidence intervals.

```
