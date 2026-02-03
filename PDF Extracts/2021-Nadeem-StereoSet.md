---
title: "StereoSet - PDF Extract"
source_pdf: "2021-Nadeem-StereoSet.pdf"
pages: 15
extracted_at: "2026-01-24T17:05:09.188560"
---

# PDF Extract: StereoSet

**Source PDF:** 2021-Nadeem-StereoSet.pdf
**Total Pages:** 15

---

## Content

```
--- Page 1 ---

StereoSet: Measuring stereotypical bias in pretrained language models
Moin Nadeem§∗and Anna Bethke† and Siva Reddy‡
§Massachusetts Institute of Technology, Cambridge MA, USA
†Intel AI, Santa Clara CA, USA
‡Facebook CIFAR AI Chair, Mila; McGill University, Montreal, QC, Canada
mnadeem@mit.edu anna.bethke@intel.com,
siva.reddy@mila.quebec
WARNING: This paper contains examples which are offensive in nature.
Abstract
A stereotype is an over-generalized belief
about a particular group of people, e.g., Asians
are good at math or Asians are bad drivers.
Such beliefs (biases) are known to hurt tar-
get groups. Since pretrained language mod-
els are trained on large real world data, they
are known to capture stereotypical biases. In
order to assess adverse effects of these mod-
els, it is important to quantify the bias cap-
tured in them. Existing literature on quanti-
fying bias evaluates pretrained language mod-
els on a small set of artiﬁcially constructed
bias-assessing sentences.
We present Stere-
oSet, a large-scale natural dataset in English to
measure stereotypical biases in four domains:
gender, profession, race, and religion.
We
evaluate popular models like BERT, GPT2,
ROBERTA, and XLNET on our dataset and
show that these models exhibit strong stereo-
typical biases. We also present a leaderboard
with a hidden test set to track the bias of future
language models at https://stereoset.
mit.edu.
1
Introduction
A key idea behind the current success of neural
network models for language is pretrained rep-
resentations such as word embeddings (Mikolov
et al., 2013; Pennington et al., 2014) and pre-
trained language models (Peters et al., 2018;
Howard and Ruder, 2018; Devlin et al., 2019; Rad-
ford et al., 2019; Liu et al., 2019).
These are
widely used to initialize neural models, which are
then ﬁne-tuned to perform a task at hand. Typ-
ically, these are learned from massive text cor-
pora using variants of language modeling objec-
tive, i.e., correctly predicting a word given its sur-
rounding context. In the recent years, these repre-
∗Work completed in part during an internship at Intel AI.
Choose the appropriate word:
Domain: Gender
Target: Girl
Context: Girls tend to be more ____ than boys
Option 1: soft
(stereotype)
Option 2: determined
(anti-stereotype)
Option 3: ﬁsh
(unrelated)
(a) The Intrasentence Context Association Test
Choose the appropriate sentence:
Domain: Race
Target: Arab
Context: He is an Arab from the Middle East.
Option 1: He is probably a terrorist with bombs.
(stereotype)
Option 2: He is a paciﬁst.
(anti-stereotype)
Option 3: My dog wants a walk.
(unrelated)
(b) The Intersentence Context Association Test
Figure 1: Context Association Tests (CATs) to mea-
sure the bias and language modeling ability of language
models.
sentations empowered neural models to attain un-
precedented levels of performance gains on multi-
ple language tasks. The resulting models are be-
ing deployed widely as services on platforms like
Google Cloud and Amazon AWS to serve millions
of users.
While this growth is commendable, there are
concerns about the fairness of these models. Since
pretrained representations are obtained from learn-
ing on massive text corpora, there is a danger that
stereotypical biases in the real world are reﬂected
in these models. For example, GPT2 (Radford
et al., 2019), a pretrained language model, has
shown to generate unpleasant stereotypical text
when prompted with context containing certain
races such as African-Americans (Sheng et al.,
2019). In this work, we assess the stereotypical
arXiv:2004.09456v1  [cs.CL]  20 Apr 2020

--- Page 2 ---

biases of popular pretrained language models.
The seminal works of Bolukbasi et al. (2016)
and Caliskan et al. (2017) show that word embed-
dings such as word2vec (Mikolov et al., 2013) and
GloVe (Pennington et al., 2014) contain stereo-
typical biases using diagnostic methods like word
analogies and association tests.
For example,
Caliskan et al. show that male names are more
likely to be associated with career terms than fe-
male names where the association between two
terms is measured using embedding similarity, and
similarly African-American names are likely to be
associated with unpleasant terms than European-
American names.
Recently, such studies have been attempted to
evaluate bias in contextual word embeddings ob-
tained from pretrained language models where a
word is provided with artiﬁcial context (May et al.,
2019; Kurita et al., 2019), e.g., the contextual em-
bedding of man is obtained from the embedding of
man in the sentence This is a man. However, these
have a few drawbacks. First, the context is artiﬁ-
cial, which does not reﬂect the natural usage of a
word. Second, they require stereotypical attribute
terms to be predeﬁned (e.g., pleasant and unpleas-
ant terms). Third, they focus on single word target
terms (and attributes) and ignore multiword terms
like construction worker.
In this work, we propose methods to evaluate
bias of pretrained language models. These meth-
ods do not have the aforementioned limitations.
Speciﬁcally, we design two different association
tests, one for measuring bias at sentence level (in-
trasentence), and the other at discourse level (in-
tersentence). In these tests, each target term (e.g.,
tennis player) is provided with a natural context
in which it appears, along with three possible as-
sociative contexts. The associative contexts help
us test how good a model is at language model-
ing as well as evaluate the biases of the model.
We crowdsource StereoSet, a dataset for associa-
tive contexts in English containing 4 target do-
mains, 321 target terms and 16,995 test instances
(triplets). A few instances are shown in Figure 1.
2
Task Formulation
What are the desiderata of an idealistic language
model?
First, it should be able to perform the
task of language modeling, i.e., it should rank
meaningful contexts higher than meaningless con-
texts.
For example, it should tell us that Our
housekeeper is a Mexican is more probable than
Our housekeeper is a round. Second, it should
not exhibit stereotypical bias, i.e., it should avoid
ranking stereotypical contexts higher than anti-
stereotypical contexts, e.g., Our housekeeper is
a Mexican and Our housekeeper is an American
should be equally possible.
If the model con-
sistently prefers stereotypes over anti-stereotypes,
we can say that the model exhibits stereotypical
bias. Based on these observations, we develop the
Context Association Test (CAT), a test that mea-
sures the language modeling ability as well as the
stereotypical bias of pretrained language models.
In CAT, given a context containing a target
group (e.g., housekeeper), we provide three dif-
ferent ways to instantiate this context. Each in-
stantiation corresponds to either a stereotypical,
a anti-stereotypical, or an unrelated association.
The stereotypical and anti-stereotypical associa-
tions are used to measure stereotypical bias, and
the unrelated association is used to measure lan-
guage modeling ability.
Speciﬁcally, we design two types of association
tests, intrasentence and intersentence CATs, to as-
sess language modeling and stereotypical bias at
sentence level and discourse level. Figure 1 shows
an example for each.
2.1
Intrasentence
Our intrasentence task measures the bias and the
language modeling ability for sentence-level rea-
soning. We create a ﬁll-in-the-blank style context
sentence describing the target group, and a set of
three attributes, which correspond to a stereotype,
an anti-stereotype, and an unrelated option (Figure
1a). In order to measure language modeling and
stereotypical bias, we determine which attribute
has the greatest likelihood of ﬁlling the blank, in
other words, which of the instantiated contexts is
more likely.
2.2
Intersentence
Our intersentence task measures the bias and the
language modeling ability for discourse-level rea-
soning.
The ﬁrst sentence contains the target
group, and the second sentence contains an at-
tribute of the target group. Figure 1b shows the
intersentence task. We create a context sentence
with a target group that can be succeeded with
three attribute sentences corresponding to a stereo-
type, an anti-stereotype and an unrelated option.
We measure the bias and language modeling abil-

--- Page 3 ---

ity based on which attribute sentence is likely to
follow the context sentence.
3
Related Work
Our work is inspired from several related attempts
that aim to measure bias is pretrained representa-
tions such as word embeddings and language mod-
els.
3.1
Bias in word embeddings
The two popular methods of testing bias in word
embeddings are word analogy tests and word as-
sociation tests. In word analogy tests, given two
words in a certain syntactic or semantic relation
(man →king), the goal is generate a word that
is in similar relation to a given word (woman →
queen). Mikolov et al. (2013) showed that word
embeddings capture syntactic and semantic word
analogies, e.g., gender, morphology etc. Boluk-
basi et al. (2016) build on this observation to study
gender bias.
They show that word embeddings
capture several undesired gender biases (seman-
tic relations) e.g. doctor : man :: woman : nurse.
Manzini et al. (2019) extend this to show that word
embeddings capture several stereotypical biases
such as racial and religious biases.
In the word embedding association test (WEAT,
Caliskan et al. 2017), the association of two
complementary classes of words, e.g., European
names and African names, with two other com-
plementary classes of attributes that indicate bias,
e.g., pleasant and unpleasant attributes, are stud-
ied to quantify the bias. The bias is deﬁned as
the difference in the degree with which European
names are associated with pleasant and unpleasant
attributes in comparison with African names being
associated with pleasant and unpleasant attributes.
Here the association is deﬁned as the similarity be-
tween the word embeddings of the names and the
attributes. This is the ﬁrst large scale study that
showed word embeddings exhibit several stereo-
typical biases and not just gender bias. Our inspi-
ration for CAT comes from WEAT.
3.2
Bias in pretrained language models
May et al. (2019) extend WEAT to sentence en-
coders, calling it the Sentence Encoder Asso-
ciation Test (SEAT). For a target term and its
attribute, they create artiﬁcial sentences using
generic context of the form "This is [target]." and
"They are [attribute]." and obtain contextual word
embeddings of the target and the attribute terms.
They repeat Caliskan et al. (2017)’s study using
these embeddings and cosine similarity as the as-
sociation metric but their study was inconclusive.
Later, Kurita et al. (2019) show that cosine simi-
larity is not the best association metric and deﬁne a
new association metric based on the probability of
predicting an attribute given the target in generic
sentential context, e.g., [target] is [mask], where
[mask] is the attribute. They show that similar ob-
servations of Caliskan et al. (2017) are observed
on contextual word embeddings too. Our intrasen-
tence CAT is similar to their setting but with nat-
ural context. We also go beyond intrasentence to
propose intersentence CATs, since language mod-
eling is not limited at sentence level.
3.3
Measuring bias through extrinsic tasks
Another popular method to evaluate bias of pre-
trained representations is to measure bias on ex-
trinsic applications like coreference resolution
(Rudinger et al., 2018; Zhao et al., 2018) and
sentiment analysis (Kiritchenko and Mohammad,
2018). In this method, neural models for down-
stream tasks are initialized with pretrained repre-
sentations, and then ﬁne-tuned on the target task.
The bias in pretrained representations is estimated
based on the performance on the target task. How-
ever, it is hard to segregate the bias of task-speciﬁc
training data from the pretrained representations.
Our CATs are an intrinsic way to evaluate bias in
pretrained models.
4
Dataset Creation
We select four domains as the target domains of in-
terest for measuring bias: gender, profession, race
and religion. For each domain, we select terms
(e.g., Asian) that represent a social group. For col-
lecting target term contexts and their associative
contexts, we employ crowdworkers via Amazon
Mechanical Turk.1 We restrict ourselves to crowd-
workers in USA since stereotypes could change
based on the country they live in.
4.1
Target terms
We curate diverse set of target terms for the tar-
get domains using Wikidata relation triples (Vran-
deˇci´c and Krötzsch, 2014). A Wikidata triple is of
the form <subject, relation, object> (e.g., <Brad
1Screenshots of our Mechanical Turk interface and details
about task setup are available in the Appendix A.2.

--- Page 4 ---

Pitt, P106, Actor>). We collect all objects occur-
ring with the relations P106 (profession), P172
(race), and P140 (religion) as the target terms.
We manually ﬁlter terms that are either infrequent
or too ﬁne-grained (assistant producer is merged
with producer).
We collect gender terms from
Nosek et al. (2002). A list of target terms is avail-
able in Appendix A.3. A target term can contain
multiple words (e.g., software developer).
4.2
CATs collection
In the intrasentence CAT, for each target term,
a crowdworker writes attribute terms that corre-
spond to stereotypical, anti-stereotypical and un-
related associations of the target term. Then they
provide a context sentence containing the target
term. The context is a ﬁll-in-the-blank sentence,
where the blank can be ﬁlled either by the stereo-
type term or the anti-stereotype term but not the
unrelated term.
In the intersentence CAT, ﬁrst they provide a
sentence containing the target term.
Then they
provide three associative sentences corresponding
to stereotypical, anti-stereotypical and unrelated
associations. These associative sentences are such
that the stereotypical and the anti-stereotypical
sentences can follow the target term sentence but
the unrelated sentence cannot follow the target
term sentence.
Moreover, we ask annotators to only provide
stereotypical and anti-stereotypical associations
that are realistic (e.g., for the target term reception-
ist, the anti-stereotypical instantiation You have to
be violent to be a receptionist is unrealistic since
being violent is not a requirement for being a re-
ceptionist).
4.3
CATs validation
In order to ensure, stereotypes were not simply the
opinion of one particular crowdworker, we vali-
date the data collected in the above step with ad-
ditional workers. For each context and its associa-
tions, we ask ﬁve validators to classify each asso-
ciation into a stereotype, an anti-stereotype or an
unrelated association. We only retain CATs where
at least three validators agree on the classiﬁcation
labels. This ﬁltering results in selecting 83% of the
CATs, indicating that there is regularity in stereo-
typical views among the workers.
Domain
# Target
# CATs
Avg Len
Terms
(triplets)
(# words)
Intrasentence
Gender
40
1,026
7.98
Profession
120
3,208
8.30
Race
149
3,996
7.63
Religion
12
623
8.18
Total
321
8,498
8.02
Intersentence
Gender
40
996
15.55
Profession
120
3,269
16.05
Race
149
3,989
14.98
Religion
12
604
14.99
Total
321
8,497
15.39
Overall
321
16,995
11.70
Table 1: Statistics of StereoSet
5
Dataset Analysis
Are people prone to associate stereotypes with
negative associations?
To answer this question,
we classify stereotypes into positive and negative
sentiment classes using a two-class sentiment clas-
siﬁer (details in Appendix A.5).
The classiﬁer
also classiﬁes neutral sentiment such as My house-
keeper is a Mexican as positive. Table 2 shows the
results. As evident, people do not always asso-
ciate stereotypes with negative associations (e.g.,
Asians are good at math is a stereotype with posi-
tive sentiment). However, people associate stereo-
types with relatively more negative associations
than anti-stereotypes (41% vs. 33%).
We also extract keywords in StereoSet to an-
alyze which words are most commonly associ-
ated with the target groups. We deﬁne a keyword
as a word that is relatively frequent in StereoSet
compared to the natural distribution of words in
large general purpose corpora (Kilgarriff, 2009).
Table 3 shows the top keywords of each domain
when compared against TenTen, a 10 billion word
web corpus (Jakubicek et al., 2013). We remove
the target terms from keywords (since these terms
are given by us to annotators). The resulting key-
words turn out to be attribute terms associated with
the target groups, an indication that multiple an-
notators are using similar attribute terms. While
the target terms in gender and race are associated
with physical attributes such as beautiful, femi-
nine, masculine, etc., professional terms are asso-

--- Page 5 ---

Positive
Negative
Stereotype
59%
41%
Anti-Stereotype
67%
33%
Table 2: Percentage of positive and negative sentiment
instances in StereoSet
Gender
stepchild
masculine
bossy
ma
uncare
breadwinner immature
naggy
feminine
rowdy
possessive
manly
polite
studious
homemaker burly
Profession
nerdy
uneducated
bossy
hardwork
pushy
unintelligent studious
dumb
rude
snobby
greedy
sloppy
disorganize
talkative
uptight
dishonest
Race
poor
beautiful
uneducated smelly
snobby
immigrate
wartorn
rude
industrious
wealthy
dangerous
accent
impoverish
lazy
turban
scammer
Religion
commandment hinduism
savior
hijab
judgmental
diety
peaceful
unholy
classist
forgiving
terrorist
reborn
atheist
monotheistic coworker
devout
Table 3: The keywords that characterize each domain.
ciated with behavioural attributes such as pushy,
greedy, hardwork, etc., and religious terms are as-
sociated with belief attributes such as diety, forgiv-
ing, reborn, etc.
6
Experimental Setup
In this section, we describe the data splits, evalua-
tion metrics and the baselines.
6.1
Development and test sets
We split StereoSet into two sets based on the target
terms: 25% of the target terms and their instances
for the development set and 75% for the hidden
test set. We ensure terms in the development set
and test set are disjoint. We do not have a train-
ing set since this defeats the purpose of StereoSet,
which is to measure the biases of pretrained lan-
guage models (and not the models ﬁne-tuned on
StereoSet).
6.2
Evaluation Metrics
Our desiderata of an idealistic language model is
that it excels at language modeling while not ex-
hibiting stereotypical biases. In order to determine
success at both these goals, we evaluate both lan-
guage modeling and stereotypical bias of a given
model. We pose both problems as ranking prob-
lems.
Language Modeling Score (lms)
In the lan-
guage modeling case, given a target term context
and two possible associations of the context, one
meaningful and the other meaningless, the model
has to rank the meaningful association higher than
meaningless association. The meaningless associ-
ation corresponds to the unrelated option in Stere-
oSet and the meaningful association corresponds
to either the stereotype or the anti-stereotype op-
tions.
We deﬁne the language modeling score
(lms) of a target term as the percentage of in-
stances in which a language model prefers the
meaningful over meaningless association. We de-
ﬁne the overall lms of a dataset as the average lms
of the target terms in the split. The lms of an
ideal language model will be 100, i.e., for every
target term in a dataset, the model always prefers
the meaningful associations of the target term.
Stereotype Score (ss)
Similarly, we deﬁne the
stereotype score (ss) of a target term as the per-
centage of examples in which a model prefers a
stereotypical association over an anti-stereotypical
association. We deﬁne the overall ss of a dataset
as the average ss of the target terms in the dataset.
The ss of an ideal language model will be 50,
i.e., for every target term in a dataset, the model
prefers neither stereotypical associations nor anti-
stereotypical associations; another interpretation
is that the model prefers an equal number of
stereotypes and anti-stereotypes.
Idealized CAT Score (icat)
We combine both
lms and ss into a single metric called the idealized
CAT (icat) score based on the following axioms:
1. An ideal model must have an icat score
of 100, i.e., when its lms is 100 and ss is 50,
its icat score is 100.
2. A fully biased model must have an icat score
of 0, i.e., when its ss is either 100 (always
prefer a stereotype over an anti-stereotype)
or 0 (always prefer an anti-stereotype over a
stereotype), its icat score is 0.

--- Page 6 ---

3. A random model must have an icat score
of 50, i.e., when its lms is 50 and ss is 50,
its icat score must be 50.
Therefore, we deﬁne the icat score as
icat = lms ∗min(ss, 100 −ss)
50
This equation satisﬁes all the axioms.
Here
min(ss,100−ss)
50
∈
[0, 1] is maximized when
the model neither prefers stereotypes nor anti-
stereotypes for each target term and is mini-
mized when the model favours one over the other.
We scale this value using the language modeling
score. An interpretation of icat is that it repre-
sents the language modeling ability of a model to
behave in an unbiased manner while excelling at
language modeling.
6.3
Baselines
IDEALLM
We deﬁne this model as the one that
always picks correct associations for a given target
term context. It also picks equal number of stereo-
typical and anti-stereotypical associations over all
the target terms. So the resulting lms, ss and icat
scores are 100, 50 and 100 respectively.
STEREOTYPEDLM
We deﬁne this model as the
one that always picks a stereotypical association
over an anti-stereotypical association. So its ss is
100. As a result, its icat score is 0 for any value
of lms.
RANDOMLM
We deﬁne this model as the one
that picks associations randomly, and therefore its
lms, ss and icat scores are 50, 50, 50 respectively.
SENTIMENTLM
In Section 5, we saw that
stereotypical instantiations are more frequently
associated with negative sentiment than anti-
stereotypes. In this baseline, for a given a pair of
context associations, the model always pick the as-
sociation with the most negative sentiment.
7
Main Experiments
In this section, we evaluate popular pretrained lan-
guage models such as BERT (Devlin et al., 2019),
ROBERTA (Liu et al., 2019), XLNET (Yang et al.,
2019) and GPT2 (Radford et al., 2019) on Stere-
oSet.
7.1
BERT
In the intrasentence CAT (Figure 1a), the goal is
to ﬁll the blank of a target term’s context sentence
with an attribute term. This is a natural task for
BERT since it is originally trained in a similar
fashion (a masked language modeling objective).
We leverage pretrained BERT to compute the log
probability of an attribute term ﬁlling the blank.
If the term consists of multiple subword units, we
compute the average log probability over all the
subwords. We rank a given pair of attribute terms
based on these probabilities (the one with higher
probability is preferred).
For intersentence CAT (Figure 1b), the goal is
to select a follow-up attribute sentence given target
term sentence. This is similar to the next sentence
prediction (NSP) task of BERT. We use BERT
pre-trained NSP head to compute the probability
of an attribute sentence to follow a target term sen-
tence. Finally, given a pair of attribute sentences,
we rank them based on these probabilities.
7.2
ROBERTA
Given that ROBERTA is based off of BERT,
the corresponding scoring mechanism remains re-
markably similar. However, ROBERTA does not
contain a pretrained NSP classiﬁcation head. So
we train one ourselves on 9.5 million sentence
pairs from Wikipedia (details in Appendix A.4).
Our NSP classiﬁcation head achieves a 94.6% ac-
curacy with ROBERTA-base, and a 97.1% accu-
racy with ROBERTA-large on a held-out set con-
taining 3.5M Wikipedia sentence pairs.2 We fol-
low the same ranking procedure as BERT for both
intrasentence and intersentence CATs.
7.3
XLNET
XLNET can be used in either in an auto-regressive
setting or bidirectional setting.
We use bi-
directional setting, in order to mimic the evalua-
tion setting of BERT and ROBERTA. For the in-
trasentence CAT, we use the pretrained XLNET
model.
For the intersentence CAT, we train an
NSP head (Appendix A.4) which obtains a 93.4%
accuracy with XLNET-base and 94.1% accuracy
with XLNET-large.
7.4
GPT2
Unlike the above models, GPT2 is a generative
model in an auto-regressive setting, i.e., it esti-
mates the probability of a current word based on
its left context. For the intrasentence CAT, we in-
stantiate the blank with an attribute term and com-
2For reference, BERT-base obtains an accuracy of 97.8%,
and BERT-large obtains an accuracy of 98.5%

--- Page 7 ---

pute the probability of the full sentence. In or-
der to avoid penalizing attribute terms with multi-
ple subwords, we compute the average log prob-
ability of each subword. Formally, if a sentence
is composed of subword units x0, x1, ..., xN, then
we compute
PN
i=1 log(P(xi|x0,...,xi−1))
N
. Given a pair
of associations, we rank each association using
this score. For the intersentence CAT, we can use
a similar method, however we found that it per-
formed poorly.3 Instead, we trained a NSP classi-
ﬁcation head on the mean-pooled representation of
the subword units (Appendix A.4). Our NSP clas-
siﬁer obtains a 92.5% accuracy on GPT2-small,
94.2% on GPT2-medium, and 96.1% on GPT2-
large.
8
Results and discussion
Table 4 shows the overall results of baselines and
models on StereoSet.
Baselines vs. Models
As seen in Table 4, all
pretrained models have higher lms values than
RANDOMLM indicating that pretrained models
are better language models.
Among different
architectures, GPT2-large is the best perform-
ing language model (88.9 on development) fol-
lowed by GPT2-medium (87.1). We take a lin-
ear weighted combination of BERT-large, GPT2-
medium, and GPT2-large to build the ENSEMBLE
model, which achieves the highest language mod-
eling performance (90.7). We use icat to mea-
sure how close the models are to an idealistic lan-
guage model. All pretrained models perform bet-
ter on icat than the baselines. While GPT2-small
is the most idealistic model of all pretrained mod-
els (71.9 on development), XLNET-base is the
weakest model (61.6). The icat scores of SEN-
TIMENTLM are close to RANDOMLM indicating
that sentiment is not a strong indicator for building
an idealistic language model. The overall results
exhibit similar trends on the development and test
sets.
Relation between lms and ss
All models ex-
hibit a strong correlation between lms and ss
scores. As the language model becomes stronger,
so its stereotypical bias (ss) too. This is unfortu-
nate and perhaps unavoidable as long as we rely on
real world distribution of corpora to train language
models since these corpora are likely to reﬂect
3In this setting, the language modeling score of GPT2 on
the intersentence CAT is 61.5.
Model
Language
Model
Score
(lms)
Stereotype
Score
(ss)
Idealized
CAT
Score
(icat)
Development set
IDEALLM
100
50.0
100
STEREOTYPEDLM
-
100
0.0
RANDOMLM
50.0
50.0
50.0
SENTIMENTLM
65.5
60.2
52.1
BERT-base
85.8
59.6
69.4
BERT-large
85.8
59.7
69.2
ROBERTA-base
69.0
49.9
68.8
ROBERTA-large
76.6
56.0
67.4
XLNET-base
67.3
54.2
61.6
XLNET-large
78.0
54.4
71.2
GPT2
83.7
57.0
71.9
GPT2-medium
87.1
59.0
71.5
GPT2-large
88.9
61.9
67.8
ENSEMBLE
90.7
62.0
69.0
Test set
IDEALLM
100
50.0
100
STEREOTYPEDLM
-
100
0.0
RANDOMLM
50.0
50.0
50.0
SENTIMENTLM
65.1
60.8
51.1
BERT-base
85.4
58.3
71.2
BERT-large
85.8
59.3
69.9
ROBERTA-base
68.2
50.5
67.5
ROBERTA-large
75.8
54.8
68.5
XLNET-base
67.7
54.1
62.1
XLNET-large
78.2
54.0
72.0
GPT2
83.6
56.4
73.0
GPT2-medium
85.9
58.2
71.7
GPT2-large
88.3
60.1
70.5
ENSEMBLE
90.5
62.5
68.0
Table 4: Performance of pretrained language models
on StereoSet.
stereotypes (unless carefully selected). Among the
models, GPT2 variants have a good balance be-
tween lms and ss in order to achieve high icat
scores.
Impact of model size
For a given architecture,
all of its pretrained models are trained on the same
corpora but with different number of parameters.
For example, both BERT-base and BERT-large
are trained on Wikipedia and BookCorpus (Zhu
et al., 2015) with 110M and 340M parameters re-
spectively. As the model size increases, we see
that its language modeling ability (lms) increases,
and correspondingly its stereotypical score. How-
ever, this is not always the case with icat. Until
the language model reaches a certain performance,
the model does not seem to exhibit a strong stereo-
typical behavior. For example, the icat scores of

--- Page 8 ---

Domain
Language
Model
Score
(lms)
Stereotype
Score
(ss)
Idealized
CAT
Score
(icat)
GENDER
92.4
63.9
66.7
mother
97.2
77.8
43.2
grandfather
96.2
52.8
90.8
PROFESSION
88.8
62.6
66.5
software developer
94.0
75.9
45.4
producer
91.7
53.7
84.9
RACE
91.2
61.8
69.7
African
91.8
74.5
46.7
Crimean
93.3
50.0
93.3
RELIGION
93.5
63.8
67.7
Bible
85.0
66.0
57.8
Muslim
94.8
46.6
88.3
Table 5:
Domain-wise results of the ENSEMBLE
model, along with most and least stereotyped terms.
ROBERTA and XLNET increase with model size,
but not BERT and GPT2, which are strong lan-
guage models to start with.
Impact
of
pretraining
corpora
BERT,
ROBERTA, XLNET and GPT2 are trained on
16GB, 160GB, 158GB and 40GB of text corpora.
Surprisingly, the size of the corpus does not
correlate with either lms or icat. This could be
due to the difference in architectures and the type
of corpora these models are trained on. A better
way to verify this would be to train a same model
on increasing amounts of corpora. Due to lack
of computing resources, we leave this work for
community. We conjecture that high performance
of GPT2 (on lms and icat) is due to the nature of
its training data. GPT2 is trained on documents
linked from Reddit.
Since Reddit has several
subreddits related to target terms in StereoSet
(e.g., relationships, religion), GPT2 is likely to
be exposed to correct contextual associations.
Also, since Reddit is moderated in these niche
subreddits (ie. /r/feminism), it could be the case
that
both
stereotypical
and
anti-stereotypical
associations are learned.
Domain-wise bias
Table 5 shows domain-wise
results of the ENSEMBLE model on the test set.
The model is relatively less biased on race than
on others (icat score of 69.7). We also show the
high and low biased target terms for each domain
from the development set. We conjecture that the
high biased terms are the ones that have well estab-
lished stereotypes in society and are also frequent
in language.
This is the case with mother (at-
tributes: caring, cooking), software developer (at-
Model
Language
Model
Score
(lms)
Stereotype
Score
(ss)
Idealized
CAT
Score
(icat)
Intrasentence Task
BERT-base
82.5
57.5
70.2
BERT-large
82.9
57.6
70.3
ROBERTA-base
71.9
53.6
66.7
ROBERTA-large
72.7
54.4
66.3
XLNET-base
70.3
53.6
65.2
XLNET-large
74.0
51.8
71.3
GPT2
91.0
60.4
72.0
GPT2-medium
91.2
62.9
67.7
GPT2-large
91.8
63.9
66.2
ENSEMBLE
91.7
63.9
66.3
Intersentence Task
BERT-base
88.3
59.0
72.4
BERT-large
88.7
60.8
69.5
ROBERTA-base
64.4
47.4
61.0
ROBERTA-large
78.8
55.2
70.6
XLNET-base-cased
65.0
54.6
59.0
XLNET-large-cased
82.5
56.1
72.5
GPT2
76.3
52.3
72.8
GPT2-medium
80.5
53.5
74.9
GPT2-large
84.9
56.1
74.5
ENSEMBLE
89.4
60.9
69.9
Table 6: Performance on the Intersentence and In-
trasentence CATs in StereoSet test set.
tributes: geek, nerd), and Africa (attributes: poor,
dark). The low biased are the ones that do not
have well established stereotypes, for example,
producer and Crimean. The outlier to this obser-
vation is Muslim. Although the target term muslim
has strong stereotypical associations in StereoSet
(e.g., the attribute term terrorist appears in 20% of
stereotypes and other hatred terms in 43% exam-
ples), the model exhibits idealistic behavior (with
a slight preference towards anti-stereotypes). We
could not explain this behavior, and leave explain-
ability of such bias to future work.
Intrasentence vs Intersentence CATs
Table 6
shows the results of intrasentence and intersen-
tence CATs on the test set. Since intersentence
tasks has more number of words per instance, we
expect intersentence language modeling task to be
harder than intrasentence. This is the case with
most models (except BERT).
9
Limitations
StereoSet is crowdsourced on Mechanical Turk
using worker pool from the US. Since this pool

--- Page 9 ---

is predominantly (80%) below the age of 50 (Di-
fallah et al., 2018), StereoSet may not reﬂect the
stereotypes of the wider US population.
Although stereotypes are subjective opinions,
we often ﬁnd them to collide with objective facts.
For instance, "I’m going to visit Iraq. Everyone
is a Muslim there" is a stereotype of Iraq in our
dataset, however this is objectively incorrect since
2% of Iraqis are Christians. Similar is the case
with anti-stereotypes (e.g., "I travelled to France
recently. Everyone there spoke English" is an anti-
stereotype since French are stereotyped to hate En-
glish). Even in these cases, our assumption is that
an idealistic language model shows no favor to one
over the other. Although we explicitly asked the
annotators to avoid objective statements and the
validators to ﬁlter them, some false statements still
remain in the data.
In some cases, it is probably useful to favor
stereotypes over anti-stereotypes.
Consider the
CAT, "The chef made ___ food", and its stereotyp-
ical and anti-stereotypical associations, delicious
and disgusting respectively. Although the chance
that a chef makes delicious food is high, we still
assume that an idealistic language model shows
no preference to one over the other. This could
be problematic. We leave this for future work.
10
Conclusion
In this work, we develop the Context Associa-
tion Test (CAT) to measure the stereotypical bi-
ases of pretrained language models with respect to
their language modeling ability. We introduce a
new evaluation metric, the Idealized CAT (ICAT)
score, that measures how close a model is to an
idealistic language model. We crowdsource Stere-
oSet, a dataset containing 16,995 CATs to test bi-
ases in four domains: gender, race, religion and
professions. We show that current pretrained lan-
guage model exhibit strong stereotypical biases,
and that the best model is 27.0 ICAT points behind
the idealistic language model. We ﬁnd that the
GPT2 family of models exhibit relatively more
idealistic behavior than other pretrained models
like BERT, ROBERTA and XLNET. Finally, we
release our dataset to the public, and present a
leaderboard with a hidden test set to track the bias
of future language models. We hope that Stere-
oSet will spur further research in evaluating and
mitigating bias in language models.
Acknowledgments
We would like to thank Jim Glass, Yonatan
Belinkov, Vivek Kulkarni, Spandana Gella and
Abubakar Abid for their helpful comments in re-
viewing this paper. We also thank Avery Lamp,
Ethan Weber, and Jordan Wick for crucial feed-
back on the MTurk interface and StereoSet web-
site.
References
Tolga Bolukbasi, Kai-Wei Chang, James Y. Zou,
Venkatesh Saligrama, and Adam T. Kalai. 2016.
Man is to computer programmer as woman is to
homemaker? debiasing word embeddings. In Pro-
ceedings of Neural Information Processing Systems
(NeurIPS), pages 4349–4357.
Aylin
Caliskan,
Joanna
J.
Bryson,
and
Arvind
Narayanan. 2017. Semantics derived automatically
from language corpora contain human-like biases.
Science, 356(6334):183–186.
Jacob Devlin, Ming-Wei Chang, Kenton Lee, and
Kristina Toutanova. 2019.
BERT: Pre-training of
deep bidirectional transformers for language under-
standing. In Proceedings of North American Chap-
ter of the Association for Computational Linguistics,
pages 4171–4186, Minneapolis, Minnesota. Associ-
ation for Computational Linguistics.
Djellel Difallah, Elena Filatova, and Panos Ipeirotis.
2018. Demographics and dynamics of mechanical
turk workers. In Proceedings of the ACM Interna-
tional Conference on Web Search and Data Mining,
WSDM ’18, pages 135 – 143, New York, NY, USA.
Association for Computing Machinery.
Jeremy Howard and Sebastian Ruder. 2018. Universal
Language Model Fine-tuning for Text Classiﬁcation.
In Proceedings of the Association for Computational
Linguistics, pages 328–339, Melbourne, Australia.
Association for Computational Linguistics.
Milos Jakubicek, Adam Kilgarriff, Vojtech Kovar,
Pavel Rychly, and Vit Suchomel. 2013. The tenten
corpus family. In Proceedings of the International
Corpus Linguistics Conference CL.
Adam Kilgarriff. 2009. Simple maths for keywords. In
Proceedings of the Corpus Linguistics Conference
2009 (CL2009),, page 171.
Svetlana Kiritchenko and Saif Mohammad. 2018. Ex-
amining Gender and Race Bias in Two Hundred Sen-
timent Analysis Systems. In Proceedings of Joint
Conference on Lexical and Computational Seman-
tics, pages 43–53.

--- Page 10 ---

Keita Kurita, Nidhi Vyas, Ayush Pareek, Alan W
Black, and Yulia Tsvetkov. 2019. Measuring bias
in contextualized word representations. In Proceed-
ings of the First Workshop on Gender Bias in Natu-
ral Language Processing, pages 166–172, Florence,
Italy. Association for Computational Linguistics.
Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Man-
dar Joshi, Danqi Chen, Omer Levy, Mike Lewis,
Luke Zettlemoyer, and Veselin Stoyanov. 2019.
Roberta: A robustly optimized bert pretraining ap-
proach. arXiv preprint arXiv:1907.11692.
Andrew L. Maas, Raymond E. Daly, Peter T. Pham,
Dan Huang, Andrew Y. Ng, and Christopher Potts.
2011. Learning word vectors for sentiment analysis.
In Proceedings of the Association for Computational
Linguistics, pages 142–150, Portland, Oregon, USA.
Association for Computational Linguistics.
Thomas Manzini, Lim Yao Chong, Alan W Black, and
Yulia Tsvetkov. 2019. Black is to criminal as cau-
casian is to police: Detecting and removing mul-
ticlass bias in word embeddings.
In Proceedings
of the North American Chapter of the Association
for Computational Linguistics, pages 615–621, Min-
neapolis, Minnesota. Association for Computational
Linguistics.
Chandler May, Alex Wang, Shikha Bordia, Samuel R.
Bowman, and Rachel Rudinger. 2019. On measur-
ing social biases in sentence encoders. In Proceed-
ings of the North American Chapter of the Associa-
tion for Computational Linguistics, pages 622–628,
Minneapolis, Minnesota. Association for Computa-
tional Linguistics.
Tomas Mikolov, Ilya Sutskever, Kai Chen, Greg Cor-
rado, and Jeffrey Dean. 2013. Distributed represen-
tations of words and phrases and their composition-
ality.
In Proceedings of Neural Information Pro-
cessing Systems (NeurIPS), NIPS 13, pages 3111 –
3119, Red Hook, NY, USA. Curran Associates Inc.
Brian Nosek, Mahzarin Banaji, and Anthony Green-
wald. 2002. Math = male, me = female, therefore
math != me. Journal of personality and social psy-
chology, 83:44–59.
Jeffrey Pennington, Richard Socher, and Christo-
pher D. Manning. 2014.
Glove: Global vectors
for word representation.
In Proceedings of Em-
pirical Methods in Natural Language Processing
(EMNLP), pages 1532–1543.
Matthew Peters, Mark Neumann, Mohit Iyyer, Matt
Gardner, Christopher Clark, Kenton Lee, and Luke
Zettlemoyer. 2018. Deep Contextualized Word Rep-
resentations. In Proceedings of the North American
Chapter of the Association for Computational Lin-
guistics), pages 2227–2237. Association for Com-
putational Linguistics.
Alec Radford, Jeffrey Wu, Rewon Child, David Luan,
Dario Amodei, and Ilya Sutskever. 2019. Language
models are unsupervised multitask learners. OpenAI
Blog, 1(8).
Rachel Rudinger, Jason Naradowsky, Brian Leonard,
and Benjamin Van Durme. 2018.
Gender bias in
coreference resolution.
In Proceedings of North
American Chapter of the Association for Computa-
tional Linguistics (NAACL), pages 8–14.
Emily Sheng, Kai-Wei Chang, Premkumar Natara-
jan, and Nanyun Peng. 2019. The woman worked
as a babysitter:
On biases in language genera-
tion. In Proceedings of the Empirical Methods in
Natural Language Processing and the International
Joint Conference on Natural Language Processing
(EMNLP-IJCNLP), pages 3407–3412, Hong Kong,
China. Association for Computational Linguistics.
Denny Vrandeˇci´c and Markus Krötzsch. 2014. Wiki-
data: A free collaborative knowledgebase.
Com-
mun. ACM, 57(10):78–85.
Zhilin Yang, Zihang Dai, Yiming Yang, Jaime Car-
bonell, Russ R Salakhutdinov, and Quoc V Le.
2019. Xlnet: Generalized autoregressive pretrain-
ing for language understanding.
In H. Wallach,
H. Larochelle, A. Beygelzimer, F. d’e Buc, E. Fox,
and R. Garnett, editors, Proceedings of Neural Infor-
mation Processing Systems (NeurIPS), pages 5753–
5763. Curran Associates, Inc.
Jieyu Zhao, Tianlu Wang, Mark Yatskar, Vicente Or-
donez, and Kai-Wei Chang. 2018. Gender Bias in
Coreference Resolution: Evaluation and Debiasing
Methods. In Proceedings of North American Chap-
ter of the Association for Computational Linguistics,
pages 15–20.
Yukun Zhu, Ryan Kiros, Rich Zemel, Ruslan Salakhut-
dinov, Raquel Urtasun, Antonio Torralba, and Sanja
Fidler. 2015. Aligning books and movies: Towards
story-like visual explanations by watching movies
and reading books. In Proceedings of the IEEE In-
ternational Conference on Computer Vision (ICCV),
ICCV 15, pages 19 – 27, USA. IEEE Computer So-
ciety.

--- Page 11 ---

A
Appendix
A.1
Detailed Results
Table 7 and Table 8 show detailed results on the
Context Association Test for the development and
test sets respectively.
A.2
Mechanical Turk Task
Our crowdworkers were required to have a 95%
HIT acceptance rate, and be located in the United
States. In total, 475 and 803 annotators completed
the intrasentence and intersentence tasks respec-
tively.
Restricting crowdworkers to the United
States helps account for differing deﬁnitions of
stereotypes based on regional social expectations,
though limitations in the dataset remain as dis-
cussed in Section 9. Screenshots of our Mechani-
cal Turk interface are available in Figure 2 and 3.
A.3
Target Words
Table 9 list our target terms used in the dataset col-
lection task.
A.4
General Methods for Training a Next
Sentence Prediction Head
Given some context c, and some sentence s, our
intersentence task requires calculating the likeli-
hood p(s|c), for some sentence s and context sen-
tence c.
While BERT has been trained with a Next
Sentence Prediction classiﬁcation head to provide
p(s|c), the other models have not. In this section,
we detail our creation of a Next Sentence Predic-
tion classiﬁcation head as a downstream task.
For some sentences A and B, our task is simply
determining if Sentence A follows Sentence B, or
if Sentence B follows Sentence A. We trivially
generate this corpus from Wikipedia by sampling
some ith sentence, i + 1th sentence, and a ran-
domly chosen negative sentence from any other
article. We maintain a maximum sequence length
of 256 tokens, and our training set consists of 9.5
million examples.
We train with a batch size of 80 sequences until
convergence (80 sequences / batch * 256 tokens
/ sequence = 20,480 tokens/batch) for 10 epochs
over the corpus. For BERT, We use BertAdam as
the optimizer, with a learning rate of 1e-5, a linear
warmup schedule from 50 steps to 500 steps, and
minimize cross entropy for our loss function. Our
results are comparable to Devlin et al. (2019), with
each model obtaining 93-98% accuracy against the
test set of 3.5 million examples.
Additional models maintain the same experi-
mental details.
Our NSP classiﬁer achieves an
94.6% accuracy with roberta-base, a 97.1%
accuracy with roberta-large, a93.4% accu-
racy with xlnet-base and 94.1% accuracy with
xlnet-large.
In order to evaluate GPT-2 on intersentence
tasks, we feed the mean-pooled representations
across the entire sequence length into the clas-
siﬁcation head.
Our NSP classiﬁer obtains a
92.5% accuracy on gpt2-small, 94.2% on
gpt2-medium, and 96.1% on gpt2-large.
In order to ﬁne-tune gpt2-large on our ma-
chines, we utilized gradient accumulation with a
step size of 10, and mixed precision training from
Apex.
A.5
Fine-Tuning BERT for Sentiment
Analysis
In order to evaluate sentiment, we ﬁne-tune BERT
(Devlin et al., 2019) on movie reviews (Maas et al.,
2011) for seven epochs. We used a maximum se-
quence length of 256 WordPieces, batch size 32,
and used Adam with a learning rate of 1e−4. Our
ﬁne-tuned model achieves an 92% test accuracy
on the Large Movie Review dataset.

--- Page 12 ---

Intersentence
Intrasentence
Model
Domain
Language
Model
Score (lms)
Stereotype
Score (ss)
Idealized
CAT Score
(icat)
Language
Model
Score (lms)
Stereotype
Score (ss)
Idealized
CAT Score
(icat)
SENTIMENTLM
gender
85.78
58.76
70.75
36.45
42.02
30.64
profession
80.70
65.20
56.16
45.61
45.28
41.31
race
84.90
70.48
50.13
49.10
70.14
29.32
religion
87.35
68.79
54.53
44.78
50.62
44.23
overall
83.51
66.93
55.24
46.01
56.40
40.12
BERT-base
gender
90.85
62.03
69.00
82.50
61.48
63.56
profession
85.87
62.32
64.71
82.31
60.85
64.45
race
89.67
58.36
74.68
83.82
56.30
73.27
religion
93.65
61.04
72.98
82.16
56.28
71.85
overall
88.53
60.43
70.06
83.02
58.68
68.61
BERT-large
gender
92.57
63.93
66.77
83.10
64.04
59.77
profession
84.62
62.93
62.74
83.04
60.30
65.94
race
89.22
57.14
76.48
84.02
57.27
71.80
religion
90.14
56.74
77.98
85.98
50.16
85.70
overall
87.93
60.18
70.02
83.60
59.01
68.54
GPT2
gender
85.95
53.38
80.14
93.28
62.67
69.65
profession
72.79
52.39
69.31
92.29
63.97
66.50
race
76.50
51.49
74.22
89.76
60.35
71.18
religion
75.83
56.93
65.33
88.46
58.02
74.27
overall
76.26
52.28
72.79
91.11
61.93
69.37
GPT2-medium
gender
86.76
52.80
81.89
93.58
65.58
64.42
profession
79.95
60.83
62.63
91.76
63.37
67.22
race
82.20
50.93
80.68
92.36
61.44
71.22
religion
86.45
60.80
67.78
90.46
62.57
67.71
overall
82.09
55.30
73.38
92.21
62.74
68.71
GPT2-large
gender
89.91
60.72
70.62
95.32
65.29
66.17
profession
84.88
61.73
64.97
92.36
65.68
63.39
race
84.21
57.02
72.38
91.89
63.00
67.99
religion
88.50
62.98
65.53
91.61
61.61
70.34
overall
85.35
59.50
69.12
92.49
64.26
66.12
XLNET-base
gender
75.27
59.33
61.22
69.57
46.54
64.76
profession
67.53
52.66
63.93
67.75
58.47
56.27
race
61.25
55.13
54.97
69.19
52.14
66.22
religion
69.54
51.66
67.22
74.90
55.72
66.32
overall
65.72
54.59
59.69
68.91
53.97
63.43
XLNET-large
gender
89.87
57.61
76.18
74.16
53.99
68.23
profession
79.98
55.05
71.90
73.15
56.05
64.30
race
81.90
54.92
73.84
73.64
50.42
73.02
religion
87.51
66.68
58.31
77.95
49.61
77.34
overall
82.39
55.76
72.90
73.68
52.98
69.29
ROBERTA-base
gender
59.62
46.76
55.76
71.36
54.21
65.35
profession
69.75
45.31
63.21
72.49
55.94
63.87
race
66.80
43.28
57.82
70.03
56.07
61.52
religion
60.55
50.15
60.37
70.60
40.83
57.65
overall
66.78
44.75
59.77
71.15
55.21
63.74
ROBERTA-large
gender
80.98
56.49
70.47
75.63
56.99
65.06
profession
76.21
57.21
65.21
73.71
55.42
65.72
race
82.45
56.73
71.36
71.71
56.34
62.63
religion
91.23
49.48
90.29
69.93
39.86
55.75
overall
80.23
56.61
69.63
72.90
55.45
64.96
ENSEMBLE
gender
93.42
63.10
68.94
95.19
64.18
68.19
profession
86.19
63.52
62.87
92.34
65.44
63.83
race
89.49
57.44
76.17
92.47
62.20
69.91
religion
90.11
56.74
77.96
91.61
59.13
74.89
overall
88.76
60.44
70.22
92.73
63.56
67.57
Table 7: The per-domain performance of pretrained language models on the development set.

--- Page 13 ---

Intersentence
Intrasentence
Model
Domain
Language
Model
Score (lms)
Stereotype
Score (ss)
Idealized
CAT Score
(icat)
Language
Model
Score (lms)
Stereotype
Score (ss)
Idealized
CAT Score
(icat)
SENTIMENTLM
gender
86.11
57.59
73.03
40.69
47.16
38.39
profession
80.69
61.32
62.42
46.07
43.41
40.00
race
84.45
70.32
50.13
49.57
69.16
30.57
religion
89.36
71.54
50.86
42.78
57.17
36.64
overall
83.44
65.44
57.67
46.92
56.41
40.90
BERT-base
gender
90.36
56.25
79.07
82.78
61.23
64.19
profession
86.92
59.16
71.00
82.89
57.32
70.75
race
88.46
59.25
72.09
82.14
57.02
70.61
religion
92.69
63.53
67.61
82.86
52.69
78.40
overall
88.28
59.00
72.38
82.52
57.49
70.16
BERT-large
gender
91.59
60.68
72.03
82.80
61.23
64.21
profession
86.02
60.77
67.49
82.55
57.33
70.45
race
89.72
60.98
70.01
83.10
57.00
71.47
religion
92.62
59.55
74.94
84.30
56.04
74.11
overall
88.68
60.81
69.51
82.90
57.61
70.29
GPT2
gender
84.68
49.62
84.03
92.01
62.65
68.74
profession
72.03
53.22
67.39
90.74
61.31
70.22
race
76.72
52.24
73.28
90.95
58.90
74.76
religion
85.21
52.04
81.74
91.21
63.26
67.02
overall
76.28
52.27
72.81
91.01
60.42
72.04
GPT2-medium
gender
84.47
49.17
83.07
91.65
66.17
62.01
profession
78.93
56.65
68.43
90.03
63.04
66.55
race
80.40
52.12
77.00
91.81
61.70
70.33
religion
85.44
53.64
79.23
93.43
65.83
63.85
overall
80.55
53.49
74.92
91.19
62.91
67.65
GPT2-large
gender
88.43
54.52
80.44
92.92
67.64
60.13
profession
84.66
59.33
68.86
90.40
64.43
64.31
race
83.87
53.77
77.55
92.41
62.35
69.58
religion
88.57
59.46
71.82
93.69
66.35
63.06
overall
84.91
56.14
74.47
91.77
63.93
66.21
XLNET-base
gender
74.26
54.80
67.14
72.09
54.75
65.24
profession
67.99
54.18
62.30
69.73
55.31
62.33
race
60.14
54.75
54.42
70.34
52.34
67.04
religion
65.58
57.30
56.00
70.61
49.00
69.20
overall
65.01
54.64
58.98
70.34
53.62
65.25
XLNET-large-cased
gender
87.07
54.99
78.39
74.85
56.69
64.84
profession
81.90
55.59
72.75
74.20
52.61
70.33
race
81.24
56.24
71.10
73.43
50.11
73.27
religion
89.23
62.04
67.74
75.96
49.40
75.05
overall
82.51
56.06
72.51
73.99
51.83
71.28
ROBERTA-base
gender
56.86
45.96
52.27
73.90
53.54
68.66
profession
67.97
48.46
65.87
71.07
52.63
67.33
race
63.37
46.99
59.55
72.16
54.59
65.54
religion
66.15
46.74
61.83
71.23
51.79
68.69
overall
64.38
47.40
61.02
71.94
53.63
66.72
ROBERTA-large
gender
81.50
52.00
78.23
75.34
53.58
69.94
profession
75.75
54.12
69.52
72.69
54.79
65.73
race
79.40
56.94
68.38
72.16
54.73
65.33
religion
93.70
56.08
82.32
71.88
49.32
70.91
overall
78.84
55.24
70.57
72.74
54.41
66.33
ENSEMBLE
gender
92.59
60.68
72.82
92.15
67.12
60.61
profession
87.26
60.84
68.34
90.40
64.29
64.56
race
90.00
61.08
70.06
92.41
62.45
69.40
religion
92.78
60.88
72.58
94.30
66.70
62.80
overall
89.40
60.93
69.86
91.70
63.87
66.26
Table 8: The per-domain performance of pretrained language models on the test set.

--- Page 14 ---

Figure 2: A screenshot of our intrasentence task collection interface.
Figure 3: A screenshot of our intersentence task collection interface.

--- Page 15 ---

Gender
stepfather
male
she
stepmother
ladies
man
brother
female
woman
mother
grandfather
girl
father
gentlemen
grandmother
boy
schoolboy
wife
bride
sir
groom
her
lady
mommy
him
son
boyfriend
himself
gentleman
hers
girlfriend
he
husband
his
sister
daddy
daughter
herself
ma’am
schoolgirl
Profession
barber
coach
businessperson
football player
construction worker
manager
CEO
accountant
commander
ﬁreﬁghter
mover
software developer
guard
baker
doctor
athlete
artist
dancer
mathematician
janitor
carpenter
mechanic
actor
handyman
musician
detective
politician
entrepreneur
model
opera singer
chief
lawyer
farmer
writer
librarian
army
real-estate developer
broker
scientist
butcher
electrician
prosecutor
banker
cook
hairdresser
prisoner
plumber
attourney
boxer
chess player
priest
swimmer
tennis player
supervisor
attendant
housekeeper
maid
producer
researcher
midwife
judge
umpire
bartender
economist
physicist
psychologist
theologian
salesperson
physician
sheriff
cashier
assistant
receptionist
editor
engineer
comedian
painter
civil servant
diplomat
guitarist
linguist
poet
laborer
teacher
delivery man
realtor
pilot
professor
chemist
historian
pensioner
performing artist
singer
secretary
auditor
counselor
designer
soldier
journalist
dentist
analyst
nurse
tailor
waiter
author
architect
academic
director
illustrator
clerk
policeman
chef
photographer
drawer
cleaner
pharmacist
pianist
composer
handball player
sociologist
Race
Nigerian
Ethiopia
Europe
European
Russian
Ukraine
Sudan
Afghanistan
Iraq
Yemen
Ukrainian
Russia
Italy
Somali
Iran
Afghan
Indian
Italian
Australian
Spanish
Guatemalan
Hispanic
Venezuela
Sudanese
Oman
Finnish
Swedish
Venezuelan
Puerto Rican
Ghanaian
Moroccan
Somalia
Saudi Arabian
Syria
Chinese
Pakistani
China
India
Irish
Britain
France
Greece
Scotland
Mexican
Paraguayan
Brazil
African
Eritrean
Sierra Leonean
Africa
Jordan
Indonesia
Vietnam
Pakistan
German
Romania
Brazilian
Ecuadorian
Mexico
Puerto Rico
Kenyan
Liberian
Cameroonian
African Americans
Kenya
Liberia
Sierra Leon
Qatari
Syrian
Arab
Saudi Arabia
Lebanon
Indonesian
French
Norweigan
South Africa
Jordanian
Korea
Singapore
Romanian
Crimean
Native American
Germany
Ireland
Ecuador
Morocco
Omani
Iranian
Iraqi
Qatar
Turkey
Vietnamese
Nepali
Laos
Bangladesh
British
Polish
Greek
Scottish
Bolivian
Guatemala
Ghana
Cameroon
Japanese
Taiwanese
Bengali
Nepal
Albanian
Albania
Columbian
Peruvian
Argentian
Spain
Paraguay
Ethiopian
Egyptian
Persian people
Sweden
Crimea
Portuguese
Argentina
Chile
Cape Verdean
Turkish
Yemeni
Taiwan
Austrian
White people
Finland
Australia
South African
Eriteria
Egypt
Korean
Dutch people
Peru
Poland
Chilean
Columbia
Bolivia
Laotian
Lebanese
Japan
Norway
Cape Verde
Portugal
Austria
Singaporean
Netherlands
Religion
Sharia
Jihad
Christian
Muslim
Islam
Hindu
Mohammed
church
Bible
Quran
Brahmin
Holy Trinity
Table 9: The set of terms that were used to collect StereoSet, ordered by frequency in the dataset.

```
