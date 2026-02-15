---
title: "2025-Borenstein-Investigating Human Values in Online Communities - PDF Extract"
source_pdf: "2025-Borenstein-Investigating Human Values in Online Communities.pdf"
pages: 21
extracted_at: "2026-02-15T17:51:58.855541"
---

# PDF Extract: 2025-Borenstein-Investigating Human Values in Online Communities

**Source PDF:** 2025-Borenstein-Investigating Human Values in Online Communities.pdf
**Total Pages:** 21

---

## Content

```
--- Page 1 ---

Investigating Human Values in Online Communities
Nadav Borenstein1
Arnav Arora1
Lucie-Aimée Kaffee2
Isabelle Augenstein1
1University of Copenhagen
2Hasso Plattner Institut
nb@di.ku.dk
aar@di.ku.dk
lucie-aimee.kaffee@hpi.de
augenstein@di.ku.dk
Abstract
Studying human values is instrumental for
cross-cultural research, enabling a better un-
derstanding of preferences and behaviour of
society at large and communities therein. To
study the dynamics of communities online, we
propose a method to computationally analyse
values present on Reddit. Our method allows
analysis at scale, complementing survey based
approaches. We train a value relevance and a
value polarity classifier, which we thoroughly
evaluate using in-domain and out-of-domain
human annotations. Using these, we automat-
ically annotate over nine million posts across
12k subreddits with Schwartz values. Our anal-
ysis unveils both previously recorded and novel
insights into the values prevalent within various
online communities. For instance, we discover
a very negative stance towards conformity in
the Vegan and AbolishTheMonarchy subred-
dits. Additionally, our study of geographically
specific subreddits highlights the correlation be-
tween traditional values and conservative U.S.
states. Through our work, we demonstrate how
our dataset and method can be used as a com-
plementary tool for qualitative study of online
communication.
1
Introduction
Human Values have been a useful analysis lens for
social sciences scholars (Ponizovskiy et al., 2020;
Boyd et al., 2021; Schwartz, 1994). Applied to
communities or individuals, they are used to study
political affiliations, cultural integration, human
disagreement, economic growth, and human de-
velopment, among others (Inglehart, 2020). Many
frameworks exist for studying human values, in-
cluding Rockeach values (Rokeach, 1973), Hofst-
ede’s cultural dimensions (Hofstede, 1984), and
Moral Foundations Theory (Graham et al., 2013).
However, studies using these value frameworks
often struggle with sample sizes and rely on self-
reported surveys to calculate the values of com-
Val
Subreddits
AC
r/startups, r/resumes, r/xboxachievements
BE
r/Adoption, r/BPDlovedones, r/Petloss
CO
r/policebrutality, r/HOA, r/BadNeighbors,
HE
r/FreeCompliments,
r/transpositive,
r/-
cozy
PO
r/debtfree, r/geopolitics, r/dividends
SE
r/GunsAreCool,
r/worldevents,
r/Combat-
Footage
SD
r/antidepressants
r/DebateReligion,
r/TrueUnpopularOpinion, r/nutrition
ST
r/crossdressing, r/Hobbies, r/NailArt
TR
r/religion, r/AskAPriest, r/atheism
UN
r/AskFeminists, r/IsraelPalestine, r/cli-
matechange
Table 1: Subreddits with the highest expression of each
of the ten Schwartz values. The stance of Green subred-
dits towards the value is positive (above 0.2), whereas
Red indicates negative stance (below −0.2).
Blue
represents neutral. AC=achievement, BE=benevolence,
CO=conformity,
HE=hedonism,
PO=power,
SE=security,
SD=self-direction,
ST=stimulation,
TR=tradition, UN=universalism.
munities (Weld et al., 2023), leading to concerns
about representation and the generalisation of the
results to populations beyond the ones studied (Ger-
lach and Eriksson, 2021; Bašnáková et al., 2016;
Fontaine et al., 2008).
Social media platforms provide unadulterated
access to vast and diverse expressions of human
thoughts and opinions in the form of posts, dis-
cussions, and comments. This rich data source is
invaluable for investigating various aspects of hu-
man society (Newell et al., 2016; Agrawal et al.,
2023; Zomick et al., 2019; Turcan and McKeown,
2019). However, analysing large amounts of social
media data qualitatively remains challenging.
To overcome this challenge, in this work, we
provide a method for computationally analysing
human values in language used on social media at
scale. Our method and dataset supplies scholars
with a tool for extracting high level values based
insights from a large corpus of social media text,
arXiv:2402.14177v4  [cs.SI]  13 Aug 2025

--- Page 2 ---

Value
Description
Power
Social status and prestige, control or dominance over people and resources
Achievement
Personal success through demonstrating competence according to social standards.
Hedonism
Pleasure and sensuous gratification for oneself.
Stimulation
Excitement, novelty, and challenge in life.
Self-direction
Independent thought and action-choosing, creating, exploring.
Universalism
Understanding, appreciation, tolerance, and protection for the welfare of all people and for nature.
Benevolence
Preservation and enhancement of the welfare of people with whom one is in frequent personal contact.
Tradition
Respect, commitment, and acceptance of the customs and ideas that traditional culture or religion provide.
Conformity
Restraint of actions, inclinations, and impulses likely to upset or harm others and violate social expectations or norms.
Security
Safety, harmony, and stability of society, of relationships, and of self.
Table 2: The ten Schwartz values and their meaning; descriptions from Schwartz (1994)
which can be used to identify interesting phenom-
ena to qualitatively study when studying online be-
haviour and communities. Specifically, we follow
Schwartz’s Theory of Human Values (Schwartz,
1994), due to its wide adoption as a value frame-
work in the social sciences as well as in Natural
Language Processing, and apply it on Reddit. Red-
dit is conceptually based on named communities,
or, subreddits, and studying the values they exhibit
is particularly interesting for studying online be-
haviour as the discussions are already segregated by
topic or sub-communities. For instance, by exam-
ining the r/teenagers subreddit, we can gain
insights into adolescent perspectives, while the r/-
ConservativeValues allows us to study the
impact of conservative values on worldviews.
To extract values from Reddit, we train super-
vised value extraction models to classify the pres-
ence and polarity of Schwartz values in text and
apply them to Reddit posts. We then evaluate the
models, validating their effectiveness and address-
ing limitations in prior work. Subsequently, we
use these models to infer the expressed values of
9 million user posts and comments across 11,616
most popular subreddits on Reddit.
Through such a computational value analysis,
we can analyse digital trace and behaviour data
at scale, complementing social science studies by
highlighting patterns as well as outliers needing
further study. As an instance of this, our analysis
demonstrates that people contributing to r/femi-
nism exhibit high values in self-direction, as sub-
stantiated by previous studies. We also demonstrate
the prevalence of high traditional values in conser-
vative US states. In sum, our contributions are:
• A flexible method of conducting large-scale
value relevance and polarity analysis to com-
plement social science research on online
communities;
• Our analysis of values at a large scale confirms
previously recorded phenomena and unveils
novel insights, indicating that our method
can complement traditional methods in un-
derstanding societal phenomena;
• We release our dataset of 12k subreddits with
their corresponding Schwartz values for future
analysis.1
Although our findings offer unique insights into the
values of individuals from various cultures, the fo-
cus of our paper is the analysis of values present in
online communities. Hence the subject of our study
is the communities themselves and how they oper-
ate, rather than the broader cultural backgrounds
of their members, which we do not measure di-
rectly. Our methods are designed to complement,
not replace, traditional survey-based approaches
for studying values, by providing additional per-
spectives from digital trace data.
2
Related Work and Background
2.1
Schwartz’s Values Framework
Values represent a crucial aspect of human nature.
According to Schwartz (2012), "A person’s value
priority or hierarchy profoundly affects his or her
attitudes, beliefs, and traits, making it one core
component of personality." Schwartz (1994) define
values as (1) concepts or beliefs, that (2) pertain
to desirable end states or behaviors, (3) transcend
specific situations, (4) guide selection or evalua-
tion of behavior and events, and (5) are ordered
by relative importance. Based on this, they outline
ten basic human values: Security, Conformity, Tra-
dition, Benevolence, Universalism, Self-direction,
Stimulation, Hedonism, Achievement, Power. We
provide descriptions of each of the values in Tab. 2.
The values were originally applied to measure dif-
ferences in values across cultures (Schwartz, 1994).
1https://github.com/copenlu/HumanValu
es

--- Page 3 ---

The framework is suggested as a tool to study popu-
lations rather than individual people, hence it serves
as a suitable tool for the analysis of online commu-
nities. We leverage the fact that a person’s iden-
tity and values are often reflected in the linguistic
choices they make (Jaffe, 2009; Norton, 1997) to
analyse values embedded in text.
2.2
Values and Natural Language Processing
Recently, there have been a number of studies ex-
ploring values and morals using NLP. In analysing
values and language on social media, Ponizovskiy
et al. (2020) released a Schwartz value dictionary.
Boyd et al. (2021) show the promise of free-text
survey response and Facebook data for value
extraction. There have also been studies exploring
morals and norms in text.
Trager et al. (2022)
release the Moral Foundations Reddit Corpus with
16k Reddit comments; Roy et al. (2021) similarly
study morality in political tweets. Havaldar et al.
(2024) study the presence of values in a geolocated
Twitter corpus using a lexicon-based approach,
finding a lack of correlation with survey data.
The closest to our study is van der Meer et al.
(2023), who train a value extraction model based
on datasets from Qiu et al. (2022); Kiesel et al.
(2022). Using the model, they analyse values at an
individual user level to understand disagreement
in online discussions. However, a key limitations
in their work is only detecting the presence of a
value, neglecting the polarity of the discussion
towards that value. In our work, we overcome
this limitation by training an additional value
stance model. Further, we perform our analysis
at the community level to understand the values
of communities rather than individuals, bringing
it closer to the original framework outlined by
Schwartz designed to understand cultural values.
2.3
Studying Online Communities
Much work has been done to explore Reddit and
its user base. Reddit users’ personalities have been
studied (Gjurkovi´c and Šnajder, 2018) as well as
their mental health (Zomick et al., 2019; Turcan
and McKeown, 2019; Chancellor et al., 2018).
Previous work has also studied Reddit by focusing
on events affecting community dynamics (Newell
et al., 2016; Agrawal et al., 2023). For instance,
Chandrasekharan et al. (2022) examine the effect
of content moderation on two controversial subred-
dits. Soliman et al. (2019) study the characteristics
and differences between left-leaning and right-
Avg
std
Percentile
Total
25
50
75
c.p.s
765.4
264.8
517
918
996
8,888,535
w.p.c
62.8
148.0
15
26
58
558,327,230
Table 3: Statistics of the Reddit dataset we analyse. c.p.s
is content item (posts and comments) per subreddit, and
w.p.c is word per content item.
leaning political subreddits. Closer to our work,
Weld et al. (2023) craft a taxonomy of community
values and associate them with specific subreddits.
However, their methodology, while high quality,
involves collecting values through self-reporting
questionnaires of limited size and suffers from
selection bias, a limitation we address in this paper.
Finally, studies have also explored modelling
community norms (Park et al., 2024) and detecting
their violations (Cheriyan et al., 2021).
3
Method
This section details the collection and processing of
our Reddit dataset, and our approach to training and
evaluating the Schwartz values extractor model.
3.1
Data Collection
We download an image of Reddit posts and com-
ments authored between January and August 20222
using Pushshift’s API.3 We filter out posts and com-
ments with fewer than ten words or with fewer
than ten upvotes to reduce possible noise from low-
quality text. We then merge the lists of posts and
comments by subreddit, not further distinguishing
between them for our analysis, and filter out subred-
dits that are tagged NSFW,4 have fewer than 5,000
subscribers, or fewer than 250 content examples.
Finally, we down-sample large subreddits to 1,000
random samples due to computational constraints
and remove non-English content. This process re-
sults in a dataset D of 11,616 unique subreddits.
See Tab. 3 for dataset statistics.
3.2
Value Extraction
For extracting Schwartz values and their polarity
from text, we first extract the relevance of a post
or comment with each Schwartz value, then use a
stance model to extract the polarity of the sentence
towards the relevant value.
2System limitations pose restrictions on the date range we
can process – an image of a single month is over 300GB.
3https://pushshift.io/
4Not Safe For Work

--- Page 4 ---

Value Relevance
For extracting relevance, our
approach is similar to van der Meer et al. (2023)
in training a neural Schwartz Values relevance clas-
sifier. We use a DeBERTa model (He et al., 2021),
over RoBERTa, due its improved performance and
speed. As a single post can potentially express
several values simultaneously, the model is trained
in a multi-label setting, predicting a vector of 10
independent probabilities for each input. We fine-
tune the classifier on the concatenation of two su-
pervised Schwartz values datasets, ValueNet (Qiu
et al., 2022) and ValueArg (Kiesel et al., 2022).
Given a labelled triplet (s, v, y), with s being a
string of text, v the name of one of the ten Schwartz
values (Tab. 2), and y ∈{0, 1}, we construct the
input x = [CLS]v[SEP]s[SEP] and train the
model to predict p(y|x). Our classifier’s perfor-
mance on this dataset is similar to the figures re-
ported by van der Meer et al. (2023), namely a
macro-averaged F1 score of 0.76 on the merged
ValueArg and ValueNet datasets. Similar to van der
Meer et al. (2023), we collapse the two non-neutral
labels (-1 and 1) in ValueNet into a single positive
class.5 This model is trained, therefore, to predict
the presence of a value v within a string s.
Value Stance
Prior work on value extraction ne-
glects to model the polarity of content towards val-
ues, substantially limiting the insights one can draw.
To detect the polarity of a comment or a post s to-
wards a value v, we train a separate stance model on
ValueNet’s non-neutral labels. Specifically, given
a triplet (s, v, y) where v is a value expressed by s
and y ∈{−1, 1}, we fit the stance model to predict
pstance(y|x), where x is constructed as described
above. We refer readers to App. C.1 for additional
training details about the classifiers.
When extracting values of comments or posts
from Reddit, we first use the relevance model
to predict the probabilities for all Schwartz val-
ues for a given input instance, resulting in a vec-
tor urel ∈[0, 1]10. Specifically, given a string
s, we construct urel = [p(y1|x1), ..., p(y10|x10)]
by replacing vk in the construction of xk
=
[CLS]vk[SEP]s[SEP] with each one of the ten
possible Schwartz values. That is, each entry in
the vector is the independent probability that s ex-
presses the value vk, supporting a multi-label ap-
proach. Then, for each k with uk
rel > 0.5 (i.e.,
input text s expresses the value vk with a probabil-
5We do this to follow the format of the ValueArg dataset,
which only contains annotations for value relevance.
AC
BE
CO
HE
PO
SE
SD
ST
TR
UN
Spearman ρ
0.73
0.66
0.66
0.6
0.56
0.8
0.46
0.5
0.6
0.73
NDCG@1
0.89
0.81
0.93
0.96
0.76
0.93
0.74
0.86
0.96
0.84
Table 4: Average Spearman’s ρ and NDCG@1 between
the three annotators of the relevance model, per-value
breakdown.
AC=achievement,
BE=benevolence,
CO=conformity,
HE=hedonism,
PO=power,
SE=security,
SD=self-direction,
ST=stimulation,
TR=tradition, UN=universalism.
AC
BE
CO
HE
PO
SE
SD
ST
TR
UN
0.51
0.57
0.61
0.77
0.30
0.45
-0.27
0.77
0.67
0.26
Table 5: Cohen’s Kappa between the two annotators of
the stance model, per-value breakdown.
ity greater than 0.5), we predict pstance(yk|xk), (i.e.,
the polarity of input text s towards the value vk).
Thus, we construct a vector of probabilities ustance
of dimensionality 10, where each entry uk
stance is
either in [−1, 1] or Null (if s does not express the
value vk greater than 0.5). Tab. 10 in App. B.3 con-
tains a sample of Reddit content and the associated
Value Extractor model predictions.
3.3
Evaluation of Value Extraction
An important limitation of van der Meer et al.
(2023) is the lack of direct evaluation of the value
extraction model. The need for this becomes par-
ticularly pronounced considering the large domain
shift of applying the model—which, similarly to us,
was trained on debating data—to analyze content
on platforms like Reddit. Therefore, we conduct a
thorough evaluation to test the model’s capabilities
of extracting values from Reddit content.
Ideally, we would want to assess the model’s
performance using a large, annotated dataset of
randomly sampled Reddit posts. However, this is
impractical because randomly selected posts are
unlikely to contain any Schwartz values.
Con-
sequently, annotating these posts would yield a
dataset with only a few positive examples. To ad-
dress this challenge, we evaluate the Value Extrac-
tion models directly.
Relevance Model Evaluation
We evaluate the
relevance model by first using it to label 10,000
posts and 10,000 comments for predicting the pres-
ence of values. Thereafter, for each value v, we
sample three posts or comments: one with high
model confidence for the presence of the value
(above 0.8), one with medium confidence (0.4-0.6),
and one with low confidence (below 0.2). Three

--- Page 5 ---

annotators then rank these comments/posts based
on which are more related to value v, regardless of
polarity. We repeat this process five times per value,
totalling 50 rankings per annotator. See App. A for
annotation guidelines and dataset samples.
For annotator agreement, we calculated averaged
Spearman’s ρ, which looks at correlation amongst
ranks. The agreement we found was 0.63, which
is reasonable for such a subjective task.6 Certain
values (e.g., security, universalism) showed better
agreement than others (e.g., self-direction). A full
breakdown is available in Tab. 4. For assessing
model performance, we assigned a gold pseudo-
ranking to each sample by averaging the annota-
tors’ rankings. We evaluate the relevance model’s
performance by comparing the model’s predicted
ranking to this gold standard. The average Spear-
man’s ρ we obtain is 0.51 (again, with values such
as security outperforming other values such as self-
direction). Looking at the top ranked content, the
NDCG@1 we obtain is an impressive 0.87, demon-
strating that high certainty predictions made by our
classifier are highly relevant to their corresponding
value. With this, we can extract comments or posts
relevant to certain values from the larger set. See
App. B.2 for examples of model misclassification
and value breakdown.
Stance Model Evaluation
We first sample 20
posts or comments per value v where the relevance
model predicted the presence of v with high con-
fidence. Two annotators then label the samples
for stance, choosing between positive, negative, or
neutral/unrelated (i.e., where no stance is clearly
expressed or the relevance model misclassified the
sample). The annotators achieved a Cohen’s Kappa
score of 0.47, representing moderate agreement,
highlighting the challenging nature of the task (see
Tab. 5 for a per-value breakdown). However, post
discussion on the disagreements, the annotators
were able to converge on decisions for each sam-
ple, thus obtaining gold labels for the 200 samples.
Finally, we apply the stance model to predict the
stances of all positive or negative samples. The
model predicts the stance towards values with an
F1 score of 0.72. Given the subjective nature of the
task, where one has to predict stance towards an
abstract concept like human values and one where
annotators often disagreed, we believe the model
performs reasonably well. To highlight some of the
6Kiesel et al. (2022) found the averaged agreement
amongst annotators for value annotation to be α = 0.49.
Value
Relevance
mean
Relevance
std
Stance
mean
Stance
std
Tradition
0.11
0.03
-0.00
0.04
Benevolence
0.30
0.12
0.01
0.29
Conformity
0.23
0.06
-0.17
0.32
Hedonism
0.21
0.08
0.45
0.36
Power
0.17
0.05
0.04
0.16
Achievement
0.26
0.09
0.47
0.30
Self-direction
0.19
0.09
0.25
0.31
Universalism
0.43
0.10
0.39
0.27
Stimulation
0.23
0.08
0.36
0.36
Security
0.21
0.06
0.06
0.18
Table 6: Global statistics of the ten Schwartz values
across the entire subreddit dataset.
trickier cases where the model is failing, Tab. 9 in
App. B.2 contains examples of model misclassifi-
cation and breakdown into values.
3.4
Assigning Values to Subreddits
We assign each subreddit S ∈D a single vector
of Schwartz probabilities urel(S) and a single vec-
tor of stances ustance(S). Given S with content
(ci)|i ∈S, where ci is either a post or a comment,
we predict urel(ci) and ustance(ci) from ci using
the process above. Finally, we calculate urel(S) by
averaging over the predicted vectors urel(ci):
urel(S) = 1
|S|
X
i∈S
urel(ci)
We construct ustance(S) similarly, considering only
non-Null entries. That is, each entry in uk
stance(S)
is computed as
uk
stance(S) =
1
|Sk|
X
i∈Sk
uk
stance(ci),
where Sk = {i ∈S|uk
stance(ci) ̸= Null}.
Tab. 6 details global statistics for the predicted
relevance and stance for each Schwartz value
across the entire subreddit dataset.
4
Experiments
Our experiments serve two primary goals: first,
to validate our approach by comparing the val-
ues extracted using our method to existing knowl-
edge. Second, to demonstrate the extensibility of
our method to new topics that have not been pre-
viously investigated in the social sciences. We
conduct qualitative and quantitative evaluations
of our approach in §4.1 and §4.2, to validate our
method. Then, to uncover interesting phenomena

--- Page 6 ---

and demonstrate the utility of our method, we in-
vestigate subreddits with differing opinions on con-
troversial topics and compare our findings with
existing studies. Finally, in §4.4, we correlate val-
ues extracted using our method to values gained
through traditional approaches like surveys and
questionnaires.
4.1
Qualitative Analysis
We start by assessing how well our values extrac-
tion model performs on our Reddit dataset.
High relevance Intuitively, certain Schwartz val-
ues are expected to be distinctly present in specific
communities; e.g. tradition in religion-related com-
munities. Therefore, we find subreddits with partic-
ularly strong signals of individual Schwartz values.
For each value, we sort the subreddits’ values prob-
ability vectors urel(S) by their entry correspond-
ing to the particular value. Tab. 1 lists a sample
of the top subreddits for each value; Tab. 11 in
App. B lists the top 20 subreddits per value. Many
of the subreddits collected for each value seem to
be intuitively related to it (e.g., r/resumes with
achievement, r/conservation with Universal-
ism). The results are encouraging, demonstrating
the effectiveness of our approach and its potential
for conducting interesting analyses.
Strong stances Equivalently, we can also investi-
gate which subreddits express the strongest stances
towards each value. For each value, we sort the
subreddits’ stance vectors ustance(S) by their en-
try corresponding to the particular value. Tab. 12
in App. B enumerates the 10 subreddits with the
highest positive and negative stance towards each
value. Again, while some of the listed subreddits
are intuitive (e.g., r/migraine having a negative
“hedonism” stance and r/raisingkids having
a strong positive stance towards “achievement”),
other subreddits are more surprising (r/TheH-
ague with a positive stance towards “hedonism”).
Value magnitude We hypothesise that online com-
munities differ not only in the set of values they ex-
press but also in the total magnitude of expressed
values. Online communities pertaining to more ob-
jective topics (e.g., linear algebra) should express
fewer Schwartz values than communities dedicated
to subjective or controversial topics (e.g., politics).
To test this, for each subreddit S ∈D we calculate
mag(S) = |urel(S)|2, the total magnitude of val-
ues expressed in the subreddit. The 20 subreddits
with the highest and lowest value magnitudes are
detailed in Tab. 13 in App. B. Subreddits with par-
ticularly high magnitudes are those communities
that focus on debating, discussion, or emotional
narratives. Examples of these include r/change-
myview, r/Adoption, and r/PoliticalD-
iscussion. Conversely, subreddits with notably
low magnitudes are generally more objective and
neutral in tone. These include r/crystalgrow-
ing and r/whatisthisfish. Some subred-
dits that exhibit low-value magnitudes are dedi-
cated to sharing photos taken by community mem-
bers, e.g., r/astrophotography.
4.2
Quantitative Analysis
We hypothesise that similar subreddit communities
share similar values, and systematically investigate
this using empirical evidence. We define three
measures of similarity between subreddits:
Value similarly.
We define σval(S1, S2) =
cos (urel(S1)||ustance(S1), urel(S2)||ustance(S2)),
the cosine similarity between the concatenation
of the relevance and stance vectors of the two
subreddits.7
Semantic similarity.
We scrape the public
description of each subreddit from its page (see
Fig. 5 in App. B), and embed these natural lan-
guage descriptions using a sentence transformer8
to construct a semantic embedding vector eS for
each subreddit S9. We now define σsem(S1, S2) =
cos(eS1, eS2).
User similarity For each pair of subreddits, we
define their user similarity to be the overlap coeffi-
cient between the users of the two subreddits. That
is,
σusr(S1, S2) =
|U(S1) ∩U(S2)|
min(|U(S1)|, |U(S2)|)
Where U(S) is the set of the subreddit’s mem-
bers.10
To answer the question of if similar subred-
dits share similar values, we correlate σval with
σsem and σusr as follows. First, for each subred-
dit S we find Ssem = argmaxS′ [σsem(S, S′)] and
7We experimented with other formulations for calculating
σval(S1, S2), and arrived to similar results.
8https://www.sbert.net/.
We use the
all-mpnet-base-v2 pretrained model.
9A limitation of this approach is that, occasionally, the
public description is rather vague. However, a manual analysis
we conducted reveals that this is rare.
10As Reddit does not make this information publicly avail-
able, we estimate U(S) by defining it as the set of users that
had posted or commented in the subreddit within our dataset.

--- Page 7 ---

Scom = argmaxS′ [σusr(S, S′)]. If similar subred-
dits share a similar set of values, we should ex-
pect ES[σval(S, Ssem)] and ES[σval(S, Scom)] to
be significantly larger than E [σval(·, ·)]. That is,
the Schwartz values of two similar subreddits
should be significantly closer to each other than the
Schwartz values of two random subreddits. Our re-
sults, computed using empirical expectations over
our dataset, confirm this hypothesis. Significant
differences exist between the expected Schwartz
values of similar and random subreddits. The ex-
pected values for both semantic and user similarity
is 0.81 versus 0.64 for random subreddits. The
z-test scores are 73.2 and 74.4, respectively, indi-
cating a high level of statistical significance.
4.3
Controversial Topics
Different online communities have differing view-
points on widely discussed issues based on their
values. To test whether we can also observe this in
subreddits, we extend the analysis to controversial
topics, based on Wikipedia’s list of controversial
topics.11 For a selected topic, we identify subred-
dits with differing viewpoints on the topic, e.g.,
r/Communism and r/Capitalism.
To establish the utility of our method and dataset,
we analyse both topics studied by prior work in the
social sciences, as well as previously unexplored
topics that could be further studied. An overview of
the results on all controversial topics can be found
in Figure 1. An overview of closely related subred-
dits (in terms of values) to each of the subreddits
discussed here can be found in Appendix B.5.
Feminism
In our investigation involving the Red-
dit communities of r/Feminism and r/Men-
sRights (prior work (Khan, 2020; Witt, 2020)
characterized r/MensRights as a non-feminist
community based on the content shared by its mem-
bers), we find both subreddits to be extremely anti-
conformative (Figure 1a). The values of univer-
salism, benevolence, and self-direction were found
to be highly relevant for both. self-direction as a
value being more core to feminists, as compared to
non-feminists has also been found in prior work ex-
ploring their values (Zucker and Bay-Cheng, 2010).
Religion
There are multiple large-scale studies
aiming to establish the connection between religion
and Schwartz values. Saroglou et al. (2004) present
11https://en.wikipedia.org/wiki/Wikipe
dia:List_of_controversial_issues
a meta-analysis across 15 countries, finding that
religious people prefer conservative values, e.g.,
tradition, and dislike values related to openness
(stimulation, self-direction). We see similar trends
in our comparison of r/atheism, r/spiritu-
ality, and r/religion (Figure 1b). While
r/atheism and r/religion express tradi-
tion, interestingly, both subreddits have a nega-
tive stance towards it. Similarly, lower scores for
power, hedonism, and achievement for those com-
munities also align with previous findings. Inter-
estingly, r/spirituality has high relevance
and a very positive stance towards some of those
values, demonstrating the focus on the self.
Veganism
Figure 1c compares the values for
r/vegan and r/carnivore. The largest dif-
ference can be observed in the value of confor-
mity. r/Vegan has a very negative stance towards
it, representing them challenging the status quo.
Holler et al. (2021) review studies related to the
values of vegetarians/vegans and omnivores, and
find that vegetarians were found to have a stronger
relation to universalism. We find a similar pattern
with r/vegan having a slightly higher relevance
but r/carnivore having a more positive stance.
They also found them to have a greater emphasis
on self-direction, which aligns with our findings.
Generations
Lyons et al. (2007) study the dif-
ferences in values across generations. Similarly,
we compare r/Millenials, r/GenZ, and r/-
GenX in Figure 1d. While the values of the dif-
ferent generations’ subreddits are highly aligned,
small differences can be observed, such as the more
positive stance towards achievement in GenZ and
GenX than Millenials. This contradicts Lyons et al.
(2007), which found Millenials to be more achieve-
ment focused than GenX.
Communism vs capitalism
Here, we describe
the difference in values for different economic ide-
ologies, i.e., communism vs capitalism in Figure 1e.
While Schwartz and Bardi (1997) describe the ef-
fect of communism on Eastern Europe (e.g., high
importance to conservatism and hierarchy values),
they did not include the values held by the peo-
ple supporting the ideology on a theoretical level.
We find that contributors to r/communism hold a
more positive stance towards achievement, whereas
contributors to r/Capitalism hold high rele-
vance values for self-direction and security. Both
subreddits have high relevance with universalism.

--- Page 8 ---

(a) Feminism
(b) Atheism, Spirituality, and Religion
(c) Veganism
(d) Generations
(e) Communism vs Capitalism
(f) Monarchism
Figure 1: Radar plots displaying the ten Schwartz values of subreddits dedicated to controversial topics.
Monarchism
We further present values on
monarchism in Figure 1f, as another example of
a controversial topic yet to be studied in terms of
values. We find contributors to r/AbolishThe-
Monarchy to be against conformity, with a neg-
ative stance towards benevolence. The contribu-
tors to r/monarchism have a high relevance to
tradition, but a negative stance towards it. They
also converse a lot more positively about power,
achievement, and security.
4.4
Correlation with Surveys
Finally, to understand how well aligned values ex-
pressed in online communities are with values of
real-world communities, we compare the Schwartz
values extracted from Reddit with those obtained
from traditional questionnaire methods.
US States First, we use our method to investigate
the premise that conservative US states are more
traditional than liberal states. We correlate the tra-
dition relevance value extracted using our method
from the states’ subreddits with responses to a sur-
vey on conservative ideologies across U.S. states
(Center, 2014b), finding a Spearman’s R of 0.55
(p-value < 0.0001). Moreover, when correlating
these values with a survey on state religiosity levels
(Center, 2014a), we find a Spearman’s R of 0.63 (p-
value < 0.0001). Fig. 2 displays the tradition value
of the 50 states subreddits, colour-coded by the
2020 US election results – “red” states clearly tend
to have higher tradition values than “blue” states.
Country-level values Next, we extend this cor-
relation experiment to additional Schwartz values
and countries other than the USA. Schwartz and
Cieciuch (2022) used questionnaires to analyse the
Schwartz values associated with 49 countries,12
which we correlate with values extracted from sub-
reddits related to these countries using our classifier.
We start by manually identifying a set of subreddits
relevant to each of the 49 countries.13 We success-
fully found at least one subreddit for 41 countries.
We also determined which language is the most
likely to be used online by citizens of the country
(and not, for example, by tourists).14 See Tab. 14
in App. B for a comprehensive list of countries and
their associated languages and subreddits. Next, we
collected posts written in the country’s language15
from the country’s subreddits. We then randomly
sampled 2,000 posts and 2,000 comments per coun-
try, excluding countries with fewer than 250 total
samples. Listing 3 lists the 32 countries that passed
this filter. Finally, we used Google Translate API
12While the survey is conducted with various populations
and regions, here we use the term “countries” for simplicity.
13We searched for country-related subreddits online and
filtered based on their public description and front-page posts,
disregarding ones that tourists or non-residents majorly use.
14We acknowledge that this is a simplification, as in many
countries, more than one language is commonly spoken.
15We used lingua (https://github.com/pemis
tahl/lingua-py) to detect the language of each post.

--- Page 9 ---

Figure 2: US states sorted by their tradition values extracted from Reddit, colour coded based on the 2020 US
election results (Blue – democratic majority. Red – republican majority).
to translate the posts into English16 and applied
our approach to extract Schwartz values for each
country.
The above-mentioned process generates a
country-value matrix of dimensions 32 × 10 of
Schwartz values obtained from Reddit. We com-
pare this matrix to the 49 × 10 the country-value
described in Schwartz and Cieciuch (2022) by re-
moving rows corresponding to countries that do not
exist in Listing 3. We then correlate the columns of
the two now-identical matrices using Spearman’s
ρ. In line with previous studies (Nasif et al., 1991;
Joseph et al., 2021), we find no correlation between
the values extracted from SM and values extracted
from questionnaires—an average Spearman’s ρ of
−0.03. Tab. 7 in App. B.4 reports the results in
full. This lack of correlation may arise from the
distinct demographics of Reddit users compared to
questionnaire respondents or the unique dynamics
of online interaction, which tends to be more reac-
tionary compared to survey responses (Joseph et al.,
2021). Our results confirm findings from previous
studies that dynamics of online behaviour differs
from offline, and should not directly be used as a
proxy without further qualitative investigation.
5
Conclusion
In this paper, we apply Schwartz’s Theory of Hu-
man Values to Reddit at scale, offering scholars a
complementary tool for studying online communi-
ties. We train and thoroughly evaluate supervised
16We manually scanned a sample of the translations and
deemed them as having satisfactory quality.
value extraction models to detect the presence and
polarity towards human values expressed in lan-
guage used on social media. Using these, we con-
duct extensive analysis of nine million posts across
12k popular subreddits. Through our analysis, we
both confirm previous findings from the social sci-
ences, as well as uncover novel insights into the
values expressed within various online communi-
ties, shedding light on existing patterns and outliers
that warrant further investigation.
Limitations
The main limitations of our work stem from the
nature of the task itself. Given the inherent sub-
jectivity and complexity of assigning human val-
ues to texts, a certain level of noise—aleatoric
uncertainty—is unavoidable. This unpredictability
can be amplified by epistemic uncertainty, which
arises from the limitations of the models we trained.
Although we have thoroughly validated the labels
generated by the model (§3.3), the predictions can
sometimes be noisy or inconsistent.
Another limitation of our approach is the con-
solidation of the values of posts in a subreddit into
a single vector. While this is necessary for under-
standing the values of communities, it discounts
the values the individual posts of users that consti-
tute these communities. This also opens up much
room for future research, particularly in studying
the internal dynamics of online communities and
understanding the role that values play at the indi-
vidual post level.
Lastly, while our approach can be leveraged to

--- Page 10 ---

identify phenomena worthy of further investiga-
tion, it lacks the means to explain these observa-
tions fully. Values are an abstract concept that is
challenging to quantify and analyse, with the values
frameworks themselves drawing criticism (Jackson,
2020). We argue that interdisciplinary collabora-
tion with experts in psychology and sociology is
essential to understand these phenomena and their
implications properly. Such collaborations will not
only enrich our understanding of online communi-
ties but also contribute to developing more robust
and nuanced machine learning models in the fu-
ture, given the inclusion of such text in the training
data.
Broader Impact and Ethical
Considerations
We believe our work goes beyond the methodolog-
ical toolkit of social scientists. The accessibility,
large scale, and relatively high quality of Reddit
data have positioned it as a valuable resource for
training data for diverse NLP tasks (Overbay et al.,
2023; Blombach et al., 2020; Huryn et al., 2022). It
opens the door to training models that are better at-
tuned to the specific needs of various communities,
potentially protected ones. Recognizing the values
of online communities, often utilized as training
data for LM development, is crucial for making
informed decisions about incorporating the data
and contributing to the creation of models that gen-
uinely reflect the diverse perspectives within these
communities (Arora et al., 2023). These also perco-
late into downstream applications of LMs (Jakesch
et al., 2023) and have a broader impact on their use.
As for ethical considerations, we made specific
efforts to ensure that our work does not impair the
privacy and anonymity of Reddit users (Sugiura
et al., 2017). We refrain from attributing values to
individual users and instead study communities as
a whole by aggregating and condensing individual
data points into a single vector. Nevertheless, many
online communities were created to serve as a safe
space for vulnerable individuals, where they share
highly sensitive and private information. Therefore,
research on Reddit and other online communities
should make utmost efforts to respect these spaces
and handle their data with care.
Acknowledgements
This research was co-funded by a DFF Sapere Aude
research leader grant under grant agreement No
0171-00034B and a DFF Research Project 1 under
grant agreement No 9130-00092B, and supported
by the Pioneer Centre for AI, DNRF grant number
P1.
References
Pratik Agrawal, Tolga Buz, and Gerard de Melo. 2023.
Wallstreetbets beyond gamestop, yolos, and the
moon: The unique traits of reddit’s finance commu-
nities. In AMCIS 2022.
Arnav Arora, Lucie-aimée Kaffee, and Isabelle Augen-
stein. 2023. Probing pre-trained language models for
cross-cultural differences in values. In Proceedings
of the First Workshop on Cross-Cultural Considera-
tions in NLP (C3NLP), pages 114–130, Dubrovnik,
Croatia. Association for Computational Linguistics.
Jana Bašnáková, Ivan Brezina, and Radomír Masaryk.
2016. Dimensions of culture: The case of slovakia
as an outlier in hofstede’s research. Ceskoslovenska
Psychologie, 60(1).
Andreas Blombach, Natalie Dykes, Philipp Heinrich,
Besim Kabashi, and Thomas Proisl. 2020. A corpus
of German Reddit exchanges (GeRedE). In Proceed-
ings of the 12th Language Resources and Evaluation
Conference, pages 6310–6316, Marseille, France. Eu-
ropean Language Resources Association.
Ryan Boyd, Steven Wilson, James Pennebaker, Michal
Kosinski, David Stillwell, and Rada Mihalcea. 2021.
Values in words: Using language to evaluate and
understand personal values. Proceedings of the Inter-
national AAAI Conference on Web and Social Media,
9(1):31–40.
Pew Research Center. 2014a. How religious is your
state?
Pew Research Center. 2014b. Political ideology by
state.
Stevie Chancellor, Andrea Hu, and Munmun De Choud-
hury. 2018. Norms matter: Contrasting social sup-
port around behavior change in online weight loss
communities. In Proceedings of the 2018 CHI Con-
ference on Human Factors in Computing Systems,
CHI ’18, page 1–14, New York, NY, USA. Associa-
tion for Computing Machinery.
Eshwar Chandrasekharan, Shagun Jhaver, Amy Bruck-
man, and Eric Gilbert. 2022. Quarantined! exam-
ining the effects of a community-wide moderation
intervention on reddit. ACM Trans. Comput.-Hum.
Interact., 29(4).
Jithin Cheriyan, Bastin Tony Roy Savarimuthu, and
Stephen Cranefield. 2021. Norm violation in online
communities – a study of stack overflow comments.
In Coordination, Organizations, Institutions, Norms,
and Ethics for Governance of Multi-Agent Systems
XIII, pages 20–34, Cham. Springer International Pub-
lishing.

--- Page 11 ---

Johnny R. J. Fontaine, Ype H. Poortinga, Luc Del-
beke, and Shalom H. Schwartz. 2008. Structural
equivalence of the values domain across cultures:
Distinguishing sampling fluctuations from meaning-
ful variation. Journal of Cross-Cultural Psychology,
39(4):345–365.
Philipp Gerlach and Kimmo Eriksson. 2021. Measuring
cultural dimensions: external validity and internal
consistency of hofstede’s vsm 2013 scales. Frontiers
in Psychology, 12:662604.
Matej Gjurkovi´c and Jan Šnajder. 2018. Reddit: A gold
mine for personality prediction. In Proceedings of
the Second Workshop on Computational Modeling
of People’s Opinions, Personality, and Emotions in
Social Media, pages 87–97, New Orleans, Louisiana,
USA. Association for Computational Linguistics.
Jesse Graham, Jonathan Haidt, Sena Koleva, Matt
Motyl, Ravi Iyer, Sean P. Wojcik, and Peter H. Ditto.
2013. Chapter two - moral foundations theory: The
pragmatic validity of moral pluralism. In Patricia
Devine and Ashby Plant, editors, Advances in Exper-
imental Social Psychology, volume 47 of Advances
in Experimental Social Psychology, pages 55–130.
Academic Press.
Shreya Havaldar, Salvatore Giorgi, Sunny Rai, Thomas
Talhelm, Sharath Chandra Guntuku, and Lyle Ungar.
2024. Building knowledge-guided lexica to model
cultural variation. In Proceedings of the 2024 Con-
ference of the North American Chapter of the Asso-
ciation for Computational Linguistics: Human Lan-
guage Technologies (Volume 1: Long Papers), pages
211–226, Mexico City, Mexico. Association for Com-
putational Linguistics.
Pengcheng He, Jianfeng Gao, and Weizhu Chen. 2021.
Debertav3: Improving deberta using electra-style pre-
training with gradient-disentangled embedding shar-
ing.
Geert Hofstede. 1984. Culture’s consequences: Interna-
tional differences in work-related values, volume 5.
sage.
Sophie Holler, Holger Cramer, Daniela Liebscher,
Michael Jeitler, Dania Schumann, Vijayendra Murthy,
Andreas Michalsen, and Christian S Kessler. 2021.
Differences between omnivores and vegetarians in
personality profiles, values, and empathy: a system-
atic review. Frontiers in psychology, 12:579700.
Daniil Huryn, William M. Hutsell, and Jinho D. Choi.
2022. Automatic generation of large-scale multi-turn
dialogues from Reddit. In Proceedings of the 29th
International Conference on Computational Linguis-
tics, pages 3360–3373, Gyeongju, Republic of Korea.
International Committee on Computational Linguis-
tics.
Ronald Inglehart. 2020. Modernization and postmod-
ernization: Cultural, economic, and political change
in 43 societies. Princeton university press.
Terence Jackson. 2020. The legacy of geert hofstede.
Alexander Jaffe. 2009. Stance: Sociolinguistic perspec-
tives. In Stance: Sociolinguistic Perspectives.
Maurice Jakesch, Advait Bhat, Daniel Buschek, Lior
Zalmanson, and Mor Naaman. 2023. Co-writing with
opinionated language models affects users’ views. In
Proceedings of the 2023 CHI Conference on Human
Factors in Computing Systems, CHI ’23, New York,
NY, USA. Association for Computing Machinery.
Kenneth Joseph, Sarah Shugars, Ryan Gallagher, Jon
Green, Alexi Quintana Mathé, Zijian An, and David
Lazer. 2021.
(mis)alignment between stance ex-
pressed in social media data and public opinion sur-
veys. In Proceedings of the 2021 Conference on
Empirical Methods in Natural Language Processing,
pages 312–324, Online and Punta Cana, Dominican
Republic. Association for Computational Linguistics.
Abeer Khan. 2020. Reddit mining to understand gen-
dered movements. In EDBT/ICDT Workshops.
Johannes Kiesel, Milad Alshomary, Nicolas Handke,
Xiaoni Cai, Henning Wachsmuth, and Benno Stein.
2022. Identifying the human values behind argu-
ments. In Proceedings of the 60th Annual Meeting of
the Association for Computational Linguistics (Vol-
ume 1: Long Papers), pages 4459–4471, Dublin,
Ireland. Association for Computational Linguistics.
Sean T Lyons, Linda Duxbury, and Christopher Hig-
gins. 2007. An empirical assessment of generational
differences in basic human values. Psychological
reports, 101(2):339–352.
Ercan G Nasif, Hamad Al-Daeaj, Bahman Ebrahimi,
and Mary S Thibodeaux. 1991. Methodological prob-
lems in cross-cultural research: An updated review.
MIR: Management International Review, pages 79–
91.
Edward Newell, David Jurgens, Haji Saleem, Hardik
Vala, Jad Sassine, Caitrin Armstrong, and Derek
Ruths. 2016. User migration in online social net-
works: A case study on reddit during a period of
community unrest. In Proceedings of the Interna-
tional AAAI Conference on Web and Social Media,
volume 10, pages 279–288.
Bonny Norton. 1997. Language, identity, and the own-
ership of english. TESOL Quarterly, 31(3):409–429.
Keighley
Overbay,
Jaewoo
Ahn,
Fatemeh
Pe-
saran zadeh, Joonsuk Park, and Gunhee Kim. 2023.
mRedditSum: A multimodal abstractive summariza-
tion dataset of Reddit threads with images. In Pro-
ceedings of the 2023 Conference on Empirical Meth-
ods in Natural Language Processing, pages 4117–
4132, Singapore. Association for Computational Lin-
guistics.
Chan Young Park, Shuyue Stella Li, Hayoung Jung,
Svitlana Volkova, Tanushree Mitra, David Jurgens,
and Yulia Tsvetkov. 2024. Valuescope: Unveiling

--- Page 12 ---

implicit norms and values via return potential model
of social interactions.
Vladimir Ponizovskiy, Murat Ardag, Lusine Grigoryan,
Ryan Boyd, Henrik Dobewall, and Peter Holtz. 2020.
Development and validation of the personal values
dictionary: A theory-driven tool for investigating
references to basic human values in text. European
Journal of Personality, 34(5):885–902.
Liang Qiu, Yizhou Zhao, Jinchao Li, Pan Lu, Baolin
Peng, Jianfeng Gao, and Song-Chun Zhu. 2022. Val-
uenet: A new dataset for human value driven di-
alogue system. In Proceedings of the AAAI Con-
ference on Artificial Intelligence, volume 36, pages
11183–11191.
Milton Rokeach. 1973. The Nature of Human Values.
The Nature of Human Values. Free Press, New York,
NY, US.
Shamik Roy, Maria Leonor Pacheco, and Dan Gold-
wasser. 2021. Identifying morality frames in political
tweets using relational learning. In Proceedings of
the 2021 Conference on Empirical Methods in Natu-
ral Language Processing, pages 9939–9958, Online
and Punta Cana, Dominican Republic. Association
for Computational Linguistics.
Vassilis Saroglou, Vanessa Delpierre, and Rebecca Der-
nelle. 2004. Values and religiosity: A meta-analysis
of studies using schwartz’s model. Personality and
individual differences, 37(4):721–734.
Shalom H. Schwartz. 1994. Are there universal aspects
in the structure and contents of human values? Jour-
nal of Social Issues, 50(4):19–45.
Shalom H. Schwartz. 2012.
An overview of the
schwartz theory of basic values. Online Readings
in Psychology and Culture, 2:11.
Shalom H Schwartz and Anat Bardi. 1997. Influences
of adaptation to communist rule on value priorities in
eastern europe. Political psychology, 18(2):385–410.
Shalom H Schwartz and Jan Cieciuch. 2022. Measuring
the refined theory of individual values in 49 cultural
groups: psychometrics of the revised portrait value
questionnaire. Assessment, 29(5):1005–1019.
Ahmed Soliman, Jan Hafer, and Florian Lemmerich.
2019. A characterization of political communities
on reddit. In Proceedings of the 30th ACM Confer-
ence on Hypertext and Social Media, HT ’19, page
259–263, New York, NY, USA. Association for Com-
puting Machinery.
Lisa Sugiura, Rosemary Wiles, and Catherine Pope.
2017. Ethical challenges in online research: Pub-
lic/private perceptions. Research Ethics, 13(3-4):184–
199.
Jackson Trager, Alireza S. Ziabari, Aida Mostafazadeh
Davani,
Preni
Golazizian,
Farzan
Karimi-
Malekabadi,
Ali Omrani,
Zhihe Li,
Brendan
Kennedy, Nils Karl Reimer, Melissa Reyes, Kelsey
Cheng, Mellow Wei, Christina Merrifield, Arta
Khosravi, Evans Alvarez, and Morteza Dehghani.
2022. The moral foundations reddit corpus.
Elsbeth Turcan and Kathy McKeown. 2019. Dread-
dit: A Reddit dataset for stress analysis in social
media. In Proceedings of the Tenth International
Workshop on Health Text Mining and Information
Analysis (LOUHI 2019), pages 97–107, Hong Kong.
Association for Computational Linguistics.
Michiel van der Meer, Piek Vossen, Catholijn Jonker,
and Pradeep Murukannaiah. 2023. Do differences
in values influence disagreements in online discus-
sions? In Proceedings of the 2023 Conference on
Empirical Methods in Natural Language Process-
ing, pages 15986–16008, Singapore. Association for
Computational Linguistics.
Galen Weld, Amy X. Zhang, and Tim Althoff. 2023.
Making online communities ’better’: A taxonomy of
community values on reddit.
Taisto D. Witt. 2020. Affect, identity, and conceptual-
izations of feminism and feminists on the antifeminist
r/MensRights subreddit. Ph.D. thesis, University of
British Columbia.
Jonathan Zomick, Sarah Ita Levitan, and Mark Serper.
2019. Linguistic analysis of schizophrenia in Red-
dit posts. In Proceedings of the Sixth Workshop on
Computational Linguistics and Clinical Psychology,
pages 74–83, Minneapolis, Minnesota. Association
for Computational Linguistics.
Alyssa N Zucker and Laina Y Bay-Cheng. 2010. Mind-
ing the gap between feminist identity and attitudes:
The behavioral and ideological divide between fem-
inists and non-labelers.
Journal of personality,
78(6):1895–1924.

--- Page 13 ---

A
Annotation Guidelines
For each three consecutive rows in
the table (colour-coded), start by
reading the three sentences in
column B. Next, review the Schwartz
value associated with the three
sentences (listed in column C) and
ensure you understand its meaning,
using the figure at the top of the
table as a reference. Then, order
the sentences according to the
extent to which they express the
value, ignoring the stance of the
sentences towards the value. In
other words, our focus is solely on
whether the value is expressed, not
on how it is expressed. Even if a
sentence violates the value, it
still expresses it. For instance,
the sentence ‘‘I never went to
church’’ expresses the value of
‘‘Tradition,’’ despite
contradicting it.
This task is subjective, and in
many cases, there is no single
correct answer. If you are
uncertain about a particular
instance, respond to the best of
your ability.
Listing 1: Guidelines for the task of annotating the
dataset used to evaluate the relevancy model.
For each row in the table, start by
reading the sentence in column A.
Next, review the Schwartz value
associated with the sentence in
column B and ensure you understand
its meaning, using the figure at
the top of the table as a
reference. Then, determine the
stance of the sentence towards the
value. If the sentence supports the
value (i.e., the value is expressed
in a positive way, or the sentence
describes a situation where the
value is maintained), select
‘‘positive’’. If the sentence
violates the value (i.e., the value
is expressed negatively, or the
sentence describes a situation
where the value is disregarded or
broken), select ‘‘negative’’. If
the sentence simply does not
express the value, select ‘‘N\A’’.
For instance, the sentence ‘‘I
never went to church’’ has a
negative stance towards the value
of ‘‘Tradition’’. Conversly, the
sentence ‘‘family comes first for
her’’ has a positive stance towards
the value.
AC
BE
CO
HE
PO
SE
SD
ST
TR
UN
-0.16
-0.31
-0.04
0.04
-0.21
0.10
-0.12
0.16
0.22
0.01
Table 7: Spearman correlation between the Schwartz
values obtained from a questionnaire and the values
extracted from Reddit.
This task is subjective, and in
many cases, there is no single
correct answer. If you are
uncertain about a particular
instance, respond to the best of
your ability.
Listing 2: Guidelines for the task of annotating the
dataset used to evaluate the stance model.
As described in §3.3, three authors of this paper
annotated Reddit content to evaluate the Value Ex-
traction Models. To evaluate the relevance model,
each annotator ranked triplets (s1, s2, s3) accord-
ing to the extent each sentence si expresses a given
value v. In total, each annotator ranked 50 triplets,
or 5 triplets per value. Fig. 3 contains a print screen
of the annotation task, whereas Listing 1 specifies
the annotation guidelines.
To evaluate the stance model, each annotator was
given a sentence s and a value v, and was tasked to
determine the stance of s towards v (one of “posi-
tive”, “negative”, or “irrelevant/neutral”, indicating
that sentence s does not express the value v). Each
annotator annotated a total of 200 sentences, or
20 per value. Fig. 4 contains a print screen of the
annotation task, whereas Listing 2 specifies the
annotation guidelines.
B
Additional Material
B.1
Dataset Statistics
B.2
Annotation and Evaluation
Tab. 8 and Tab. 9 present cases where the relevance
model and stance models, respectively, misclassi-
fied instances.
B.3
Prediction Examples
Tab. 10 contains examples of posts and comments
from Reddit and the values and stances that the
relevance and stance models predicted for each
instance.
B.4
Experiments
Turkey, South Africa, Estonia,
Romania, USA, Costa Rica, Poland,
New Zealand, Brazil, Greece,
Finland, Ukraine, Croatia,
Colombia, Slovakia, United Kingdom,

--- Page 14 ---

Figure 3: Print screen of the annotation task of the relevance model. The three annotators were tasked with ranking
triplets of sentences according to the extent to which they express the value of column C.
Figure 4: Print screen of the annotation task of the stance model. Two annotators were tasked to determine the
stance of the sentence in column A towards the value in column B.
Val
Sentence
Annotated
Average
Rank
SD
idk it brings some discussions to the
community, can‘t be bad
2.33
PO
You really gave it all you had very
impressive content
2.66
CO
Turkish guy debates Marxism and
Freud with a street upper
2.33
BE
Claiming a fictional character has
did because your coworker/psychol-
ogist said so based off of a movie
2.33
PO
What is each of your favorite song
from Mercurial World to perform
live?
2.66
Table 8: Instances where the relevance model predicted
that the sentence expresses a value with high confidence
(above 0.8), whereas the annotators concluded that the
sentence does not express the value.
Val
Sentence
Predicted
(wrong)
Stance
PO
Crypto traders using the war to make
money. This is a new low
Pos
HE
God forbid you pay someone for
their content that you enjoy.
Neg
CO
SLPT: drive at speed in reverse gear
through speed cameras to get fines
repaid by the police
Pos
SD
If the island keeps drifting, the UK
would be part of the US again?
Neg
UN
The double standards of western me-
dia towards third world countries
Pos
SD
The coffee is probably making it
worse. People forget it’s a drug with
consequences.
Neg
Table 9: Instances where the stance model misclassified
a sentence.

--- Page 15 ---

Sentence
Predicted Value
Predicted Stance
The green party was literally removed from the ballot in key battleground
states in the 2020 election.
Power
Negative
When you’re trained by a leader you become a leader.
Power
Positive
I’ve been learning jazz for about 8 months and still can’t write a single
good peace, is that normal?Just wondering if Im not deaf because every
time I’m trying to write something I end up raging. In general I make
music for 4-5 years if that matters.
Achievement
Negative
My first ever attempt at finger crochet (or any crochet for that matter)!
I’m really proud of myself and just wanted to share somewhere :)
Achievement
Positive
I have never had a birthday celebrationSo my parents are Jehovah’s
witnesses I’m not but I have never received a birthday present and this
year I’m really depressed I want to celebrate but I’m broke
Hedonism
Negative
To love more is Beautiful.I wish you Wonderful evening and happy
weekend
Hedonism
Positive
This video gave me anxiety. It’s so inefficient with its movements that it
made me squirm.
Stimulation
Negative
This awe inspiring film is the culmination of 3 months working underwa-
ter, diving, exploring and filming the most remote corners of the Great
Barrier Reef. It showcases some of the most stunning scenes, schooling
sharks and most vibrant coral reef the ocean has to offer. Hope you
enjoy!
Stimulation
Positive
Having to lie so that you don’t have to work Saturdays is funny and
wholesome smh
Self-direction
Negative
If you want to be better at squatting, this is fine. If you are going for a
specific aesthetic, evaluate/critique your physique for any lagging parts
areas, then choose the exercises that help bring them up.
Self-direction
Positive
"The only moral abortion is MY abortion" or "Grifters gonna Grift"
Universalism
Negative
I REALLY THINK ALL OF US HUMANS NEED TO BE REP-
RESENTED PROPERLY, REGARDLESS OF WHAT LANGUAGE
PACKS WE HAVE INSTALLED.
Universalism
Positive
And then blaming the teacher when half the class fails.
Benevolence
Negative
please ban mentions of hasan off of LSF. his mental health is being
affected by the harassment from this sub.
Benevolence
Positive
Respect my religion while I shove it down your throat....
Tradition
Negative
Korobeiniki: known in the West as "Tetris music"; in Russian, it´s a folk
song about courtship.
Tradition
Positive
There is a literal detailed police report of him beating the shit out of his
then girlfriend.
Conformity
Negative
Indian minister drinks dirty water from ’holy’ river polluted with sewage
to show locals it’s safe... ends up in hospital days later
Conformity
Positive
This is in Mexico. The guy can literally pay the cops to look the other
way, and he obviously has the money to do so
Security
Negative
India also built the largest border walls with pakistan, that too in the
Himalayan foothills and thar desert. Really helped in curbing cross
border terror though.
Security
Positive
Table 10: Examples of posts and comments from Reddit and the values and stances that the relevance and stance
models predicted for each instance.

--- Page 16 ---

Figure 5: Location of the “Public description” attribute
on a subreddit page.
Iceland, Czech Republic, Italy,
Sweden, China, Ecuador, Germany,
Peru, Indonesia, Serbia, Spain,
India, Australia, Philippines,
Portugal, France,
Listing 3: List of countries used in the correlation
experiment in §4.4.
Tab. 11 Subreddits with the highest signal for each
one of the ten Schwartz values. The stance of Green
subreddits towards the value is positive (above
0.2), whereas Red indicates negative stance (be-
low −0.2).
Tab. 12 Subreddits expressing the strongest posi-
tive and negative stances for each value.
Tab. 13 Subreddits with the highest and lowest
total magnitude of Schwartz values, calculated ac-
cording to mag(S) = |urel(S)|2.
Fig. 5 Location of the “Public description” attribute
on a subreddit page, used to calculate σsem(S1, S2)
in §4.2.
Listing 3 List of countries used in the correlation
experiment in §4.4.
B.5
Controversial Topics – Extended
Additionally to the analysis presented in Sec-
tion 4.3, Table 15 displays the ten most similar
subreddits in terms of values. We use value simi-
larity as described in Section 4.2 to determine the
closest subreddits to each of the controversial topic
subreddits.
C
Reproducibility
C.1
Training the Schwartz Values Extractor
We trained the relevance model and the stance
model for ten epochs with early stopping, using
a learning rate of 5·1e−5, batch size of 32, Adamw
optimiser with default parameters and linear learn-
ing rate scheduler. We trained the models on a
single TitanRTX GPU for about 5 hours for the
relevance model, and 2 hours for the stance model.

--- Page 17 ---

Value
Subreddits
Tradition
r/0.42igion (0.42), r/Anglicanism (0.42), r/TraditionalCatholics (0.37), r/AskAChris-
tian (0.37), r/AcademicBiblical (0.36), r/Catholic (0.36), r/AskBibleScholars (0.36),
r/Episcopalian (0.36), r/AskAPriest (0.35), r/Antitheism (0.34), r/OrthodoxChristian-
ity (0.34),
r/Catholicism (0.33),
r/antitheistcheesecake (0.33),
r/agnostic (0.32),
r/atheistmemes (0.32), r/CatholicMemes (0.32), r/Bible (0.32), r/RadicalChristianity
(0.31), r/atheism (0.31), r/0.31igiousfruitcake (0.31)
Benevolence
r/coparenting (0.87),
r/Stepmom (0.85),
r/BipolarSOs (0.84),
r/theotherwoman (0.84),
r/stepparents (0.84), r/AdultChildren (0.83), r/ADHD_partners (0.83), r/CaregiverSup-
port (0.83), r/SingleParents (0.83), r/Petloss (0.83), r/Adoption (0.83), r/emotional-
abuse (0.83), r/EstrangedAdultChild (0.82), r/AgingParents (0.82), r/FriendshipAdvice
(0.82), r/AnxiousAttachment (0.82), r/Adopted (0.82), r/attachment_theory (0.82), r/A-
sOneAfterInfidelity (0.82), r/NarcAbuseAndDivorce (0.82)
Conformity
r/AgainstHateSubreddits (0.54),
r/reclassified (0.52),
r/TheseFuckingAccounts
(0.50),
r/AmIFreeToGo (0.50),
r/ModSupport (0.50),
r/modsbeingdicks (0.49),
r/Mod-
sAreKillingReddit (0.49), r/policebrutality (0.49), r/modhelp (0.48), r/WatchRedditDie
(0.47),
r/Bad_Cop_No_Donut (0.47),
r/Chiraqhits (0.47),
r/JustUnsubbed (0.46),
r/le-
galadviceofftopic (0.46), r/circlebroke2 (0.46), r/HOA (0.46), r/BadNeighbors (0.46),
r/redditrequest (0.46), r/law (0.46), r/fuckHOA (0.46)
Hedonism
r/crossdressing (0.56), r/transadorable (0.56), r/Autumn (0.55), r/TheMidnight (0.53),
r/dykesgonemild (0.53), r/cakedecorating (0.53), r/FreeCompliments (0.53), r/GothStyle
(0.52),
r/NailArt (0.52),
r/cozy (0.51),
r/PlusSizeFashion (0.51),
r/MTFSelfieTrain
(0.50),
r/oldhagfashion (0.50),
r/femboy (0.50),
r/transpositive (0.50),
r/christmas
(0.49),
r/malepolish (0.49),
r/RainbowEverything (0.49),
r/gaybrosgonemild (0.49),
r/HappyTrees (0.49)
Power
r/FundRise (0.41),
r/AskEconomics (0.38),
r/finance (0.37),
r/acorns (0.37),
r/His-
toricalWhatIf (0.37), r/geopolitics (0.37), r/strongblock (0.36), r/UWMCShareholders
(0.36),
r/debtfree (0.36),
r/qyldgang (0.36),
r/rocketpool (0.36),
r/Anchor (0.36),
r/IndianStreetBets (0.36), r/Economics (0.35), r/dividends (0.35), r/VoteBlue (0.35),
r/EuropeanFederalists (0.35), r/defi (0.35), r/ValueInvesting (0.35), r/AlibabaStock
(0.35)
Achievement
r/passive_income (0.60), r/FundRise (0.60), r/ValueInvesting (0.59), r/OptionsMillion-
aire (0.59),
r/EngineeringResumes (0.58),
r/xboxachievements (0.57),
r/algotrading
(0.57), r/FuturesTrading (0.57), r/resumes (0.55), r/abmlstock (0.55), r/AllCryptoBets
(0.55),
r/cryptostreetbets (0.55),
r/dividends (0.55),
r/SatoshiBets (0.54),
r/Forex
(0.54), r/EANHLfranchise (0.54), r/IndianStockMarket (0.54), r/quant (0.54), r/Blogging
(0.54), r/aabbstock (0.54)
Self-direction
r/CapitalismVSocialism (0.67), r/ScientificNutrition (0.67), r/Abortiondebate (0.66),
r/DebateAnarchism (0.65),
r/BasicIncome (0.63),
r/DebateAVegan (0.62),
r/Neuropsy-
chology (0.62), r/changemyview (0.61), r/AskEconomics (0.61), r/AskPsychiatry (0.59),
r/AskDID (0.59),
r/nutrition (0.58),
r/AskSocialScience (0.58),
r/healthcare (0.58),
r/askpsychology (0.58), r/radicalmentalhealth (0.58), r/ketoscience (0.57), r/DebateRe-
ligion (0.57), r/Marxism (0.57), r/PsychedelicTherapy (0.57)
Universalism
r/DebateAVegan (0.88), r/IsraelPalestine (0.87), r/DebateEvolution (0.85), r/DebateA-
narchism (0.85),
r/DebateReligion (0.84),
r/changemyview (0.84),
r/Abortiondebate
(0.84), r/CapitalismVSocialism (0.84), r/AskSocialScience (0.84), r/EndlessWar (0.83),
r/LeftWingMaleAdvocates (0.83),
r/DebateAnAtheist (0.83),
r/TrueUnpopularOpinion
(0.82),
r/PoliticalDiscussion (0.82),
r/Ask_Politics (0.82),
r/IntellectualDarkWeb
(0.82),
r/chomsky (0.82),
r/AskFeminists (0.81),
r/Marxism (0.81),
r/DebateCommunism
(0.81)
Stimulation
r/Autumn (0.51), r/crossdressing (0.51), r/TheMidnight (0.51), r/transadorable (0.51),
r/FreeCompliments (0.49),
r/dykesgonemild (0.48),
r/cakedecorating (0.48),
r/xbox-
achievements (0.47), r/PlusSizeFashion (0.47), r/GothStyle (0.47), r/cozy (0.46), r/MTF-
SelfieTrain (0.46), r/christmas (0.46), r/AltJ (0.46), r/Madonna (0.46), r/weddingdress
(0.46), r/NailArt (0.46), r/transpositive (0.46), r/happy (0.46), r/Hobbies (0.46)
Security
r/CredibleDefense (0.66), r/ww3 (0.65), r/syriancivilwar (0.62), r/geopolitics (0.62),
r/EndlessWar (0.62),
r/warinukraine (0.59),
r/AfghanConflict (0.58),
r/UkrainianCon-
flict (0.58), r/UkraineConflict (0.56), r/CombatFootage (0.55), r/LessCredibleDefence
(0.55),
r/GunsAreCool (0.55),
r/war (0.55),
r/FutureWhatIf (0.55),
r/nuclearweapons
(0.54),
r/WarCollege (0.53),
r/UkraineInvasionVideos (0.53),
r/UkraineRussiaReport
(0.53), r/RussiaUkraineWar2022 (0.52), r/UkraineWarReports (0.52)
Table 11: Subreddits with the highest signal for each one of the ten Schwartz values (the number in parenthesis
indicates the magnitude of the signal). The stance of Green subreddits towards the value is positive (above 0.2),
whereas Red indicates negative stance (below −0.2).

--- Page 18 ---

Value
Positive Stance
Negative Stance
Tradition
r/Ankrofficial,
r/lds,
r/CharliDame-
lioMommy,
r/Christian,
r/AskAPriest,
r/Bible, r/bahai, r/Quakers, r/Prismat-
icLightChurch,
r/OrthodoxChristian-
ity
r/SuperModelIndia,
r/Jewdank,
r/EX-
HINDU, r/DesiMeta, r/linguisticshumor,
r/exmuslim,
r/AsABlackMan,
r/Satan,
r/IndoEuropean, r/AfterTheEndFanFork
Benevolence
r/freebsd,
r/RandomKindness,
r/Ter-
raform,
r/Petloss,
r/nextjs,
r/Wet-
shaving,
r/AllCryptoBets,
r/NixOS,
r/vancouverhiking, r/ansible
r/FromDuvalToDade,
r/CrimeInTheD,
r/NBAYoungboy,
r/40kOrkScience,
r/LILUZIVERTLEAKS,
r/DuvalCounty,
r/Phillyscoreboard, r/Chiraqhits, r/-
SummrsXo, r/CARTILEAKS
Conformity
r/Ankrofficial, r/nanotrade, r/Nervos-
Network, r/Vechain, r/steroids, r/US-
CIS, r/treelaw, r/Stellar, r/cancun, r/-
JapanFinance
r/Animewallpaper, r/kencarson, r/From-
DuvalToDade,
r/LilDurk,
r/Cookierun,
r/freddiegibbs, r/SummrsXo, r/Destroy-
Lonely, r/Gunna, r/okbuddydaylight
Hedonism
r/eastside,
r/RedditPHCyclingClub,
r/OaklandFood,
r/carcamping,
r/Cryp-
toMars,
r/VeganBaking,
r/TheHague,
r/ZZZ_Official, r/pottedcats, r/ambi-
entmusic
r/depression,
r/TIHI,
r/Shark_Park,
r/willowbramley,
r/Phillyscoreboard,
r/migraine,
r/BodyDysmorphia,
r/Sui-
cideWatch, r/2meirl4meirl, r/anhedonia
Power
r/Yotsubros, r/Fitness, r/CryptoMoon-
Shots, r/infertility, r/AllCryptoBets,
r/ketoscience, r/steroids, r/Program-
mingLanguages, r/cryptostreetbets, r/-
cooperatives
r/masterhacker,
r/Stake,
r/uknews,
r/RustConsole,
r/uspolitics,
r/OPBR,
r/BidenIsNotMyPresident,
r/capital-
ism_in_decay, r/Patriot911, r/occupy-
wallstreet
Achievement
r/infertility, r/theravada, r/edrums,
r/raisingkids, r/CryptoMars, r/Yotsub-
ros,
r/cozy,
r/gaidhlig,
r/Prismati-
cLightChurch, r/learnrust
r/DreamStanCringe,
r/FGOmemes,
r/AntiTrumpAlliance,
r/BidenWatch,
r/misanthropy, r/Patriot911, r/TRUTH-
socialWatch,
r/Instagram,
r/Twitter-
Cringe, r/Negareddit
Self-direction
r/Mosses, r/jungle, r/LandscapingTips,
r/icecreamery,
r/esp32,
r/Satoshi-
Bets, r/rust_gamedev, r/openstreetmap,
r/QuantumComputing,
r/cryptostreet-
bets
r/Negareddit,
r/misanthropy,
r/Peo-
pleFuckingDying, r/BoomersBeingFools,
r/AmericanFascism2020,
r/Republican-
Values,
r/FoxFiction,
r/ParlerWatch,
r/libsofreddit,
r/FragileWhiteReddi-
tor
Universalism
r/SatoshiBets,
r/CryptoMars,
r/All-
CryptoBets,
r/nextjs,
r/AskAstropho-
tography,
r/GardenWild,
r/vancouver-
hiking, r/dungeondraft, r/EatCheapAnd-
Vegan, r/GraphicsProgramming
r/CrimeInTheD,
r/FromDuvalToDade,
r/Phillyscoreboard,
r/DaDumbWay,
r/-
DuvalCounty,
r/Chiraqhits,
r/Bruce-
DropEmOff, r/punchableface, r/Conser-
vativeRap, r/NYStateOfMind
Stimulation
r/CryptoMars,
r/cryptostreetbets,
r/JoshuaTree,
r/wonderdraft,
r/reen-
actors, r/AllCryptoBets, r/estoration,
r/yerbamate,
r/GiftIdeas,
r/Oakland-
Food
r/depression,
r/Shark_Park,
r/heck,
r/TwitterCringe,
r/depressed,
r/Com-
mercialsIHate,
r/Demps,
r/D_Demps,
r/christenwhitmansnark, r/Sleepparal-
ysis
Security
r/BoringCompany, r/haskell, r/Program-
mingLanguages, r/rust, r/psychoanaly-
sis, r/crypto, r/steroids, r/AskComput-
erScience, r/infertility, r/DebateEvo-
lution
r/holdmycosmo,
r/davidbowiecircle-
jerk,
r/RoastMyCat,
r/Chiraqhits,
r/DaDumbWay,
r/okbuddydaylight,
r/bottomgear,
r/SuicideWatch,
r/CrimeInTheD, r/Bombing
Table 12: Subreddits expressing each value’s strongest positive and negative stances.

--- Page 19 ---

Magnitude
Subreddits
Maximal
r/DebateAnarchism,
r/Abortiondebate, r/ther-
apyabuse,
r/Capitalis-
mVSocialism,
r/change-
myview,
r/AvoidantAt-
tachment,
r/LeftWing-
MaleAdvocates,
r/copar-
enting,
r/ADHD_partners,
r/DebateAVegan,
r/Ask_Politics,
r/Is-
raelPalestine,
r/Politi-
calDiscussion,
r/AskSo-
cialScience, r/NarcAbuse-
AndDivorce,
r/AskDID,
r/attachment_theory,
r/Adoption,
r/kpoprants,
r/TrueUnpopularOpinion
Minimal
r/vegan1200isplenty,
r/caloriecount,
r/Watchexchange,
r/Brogress,
r/crystal-
growing, r/sneakermarket,
r/gundeals,
r/buildapc-
sales,
r/whatisit,
r/N-
MSCoordinateExchange,
r/BulkOrCut,
r/astropho-
tography,
r/legodeal,
r/whatisthisthing,
r/whatsthisfish,
r/-
filmfashion,
r/TipOfMy-
Fork,
r/1500isplenty,
r/safe_food, r/Repbudget-
fashion
Table 13: Subreddits with the highest and lowest total
magnitude of Schwartz values, calculated according to
mag(S) = |urel(S)|2.

--- Page 20 ---

Country
Language
Subreddits
Australia
English
r/australia, r/Australia_, r/australian, r/sydney, r/melbourne
Brazil
Portuguese
r/brasil, r/brasilivre, r/GTAorBrazil, r/brasilia, r/saopaulo
China
Chinese
r/China, r/China_irl, r/real_China_irl
Colombia
Spanish
r/Colombia, r/ColombiaReddit, r/Bogota
Costa Rica
Spanish
r/costarica, r/Ticos
Croatia
Croatian
r/croatia, r/zagreb
Czech Republic
Czech
r/czech
Ecuador
Spanish
r/ecuador
Estonia
Estonian
r/Eesti
Faroe Islands
All
r/Faroeislands
Finland
Finnish
r/Suomi
France
French
r/france, r/paris
Georgia
Georgian
r/Sakartvelo, r/tbilisi
Germany
German
r/de, r/deuchland, r/Munich, r/berlin
Ghana
English
r/ghana
Greece
Greek
r/greece
Hong Kong
Chinese
r/HongKong
Iceland
Icelandic
r/Iceland
India
All
r/india, r/IndiaSpeaks, r/unitedstatesofindia, r/askindia
Indonesia
Indonesian
r/indonesia
Israel
Hebrew
r/Israel, r/telaviv, r/jerusalem
Italy
Italian
r/italy, r/Italia
Japan
Japanese
r/japan, r/tokyo, r/newsokur
New Zealand
English
r/newzealand, r/auckland
Oman
Arabic
r/Oman
Peru
Spanish
r/PERU
Philippines
English
r/Philippines
Poland
Polish
r/Polska
Portugal
Portuguese
r/portugal, r/lisboa, r/porto
Romania
Romanian
r/Romania, r/bucuresti, r/iasi, r/cluj, r/timisoara
Serbia
Serbian
r/serbia
Slovakia
Slovak
r/Slovakia
South Africa
All
r/southafrica, r/capetown, r/johannesburg
South Korea
Korean
r/hanguk
Spain
Spanish
r/Espana, r/spain, r/Madrid, r/Barcelona
Sweden
Swedish
r/Sverige, r/sweden, r/stockholm, r/svenskpolitik
Turkey
Turkish
r/Turkey, r/istanbul, r/ankara, r/Ismir
Ukraine
Ukrainian
r/ukraine, r/Ukraine_UA
United Kingdom
All
r/unitedkingdom, r/london, r/manchester, r/CasualUK, r/unitedkingdom, r/askuk
USA
All
All states subreddits
Vietnam
Vietnamese
r/VietNam
Table 14: Countries, languages and subreddits used in the correlation study.

--- Page 21 ---

subreddit
closest subreddits
r/vegan
r/intersex, r/transgenderUK, r/TransSpace, r/Trans-
medical, r/ABCDesis, r/LGBTindia, r/DeepThoughts,
r/nonduality, r/exvegans, r/BlockedAndReported
r/carnivore
r/carnivorediet,
r/Psoriasis,
r/PsoriaticArthri-
tis, r/rheumatoid, r/acne, r/Hashimotos, r/Testos-
terone, r/PlasticSurgery, r/lupus, r/kratom
r/communism
r/InformedTankie,
r/CommunismWorldwide,
r/CPUSA,
r/socialism,
r/StupidpolEurope,
r/LatinAmerica,
r/sendinthetanks, r/ROI, r/Africa, r/myanmar
r/Capitalism
r/georgism, r/Unions, r/SandersForPresident, r/la-
bor,
r/NewDealAmerica,
r/BernieSanders,
r/Work-
ersStrikeBack,
r/ndp,
r/theydidthemath,
r/May-
DayStrike
r/monarchism
r/leftistvexillology,
r/UsefulCharts,
r/RoughRo-
manMemes, r/IndiaPlace, r/pureasoiaf, r/Medieval-
History,
r/shittyhalolore,
r/MemriTVmemes,
r/an-
cientrome, r/darkwingsdankmemes
r/AbolishTheMonarchy
r/Sham_Sharma_Show, r/forwardsfromgrandma, r/Wor-
dAvalanches,
r/Malaphors,
r/Lal_Salaam,
r/Metal,
r/BanVideoGames,
r/QanonKaren,
r/PoliticalHumor,
r/insanepeoplefacebook
r/Millennials
r/GenZ,
r/PlusSizedAndPregnant,
r/Thailand-
Tourism, r/indiasocial, r/Liverpool, r/TallGirls,
r/Psychedelics, r/Chandigarh, r/Cardiff, r/Chroni-
cIllness
r/GenZ
r/Millennials, r/indiasocial, r/TallGirls, r/Kibbe,
r/Zillennials,
r/aggretsuko,
r/precure,
r/nerd-
fighters, r/KoeNoKatachi, r/comiccon
r/GenX
r/lesbianfashionadvice, r/CosplayNation, r/Xenni-
als, r/bigboobproblems, r/feminineboys, r/PlusSize,
r/distantsocializing, r/CasualPH, r/bald, r/Tall-
Girls
r/Feminism
r/antiwoke,
r/MensLib,
r/ControversialOpinions,
r/EnoughIDWspam, r/prochoice, r/prolife, r/fourth-
wavewomen,
r/TransSpace,
r/TrueUnpopularOpinion,
r/AntiVegan
r/MensRights
r/antifeminists,
r/AntiHateCommunities,
r/AsABlackMan, r/LeftWingMaleAdvocates, r/azniden-
tity,
r/EnoughPCMSpam,
r/FragileWhiteRedditor,
r/BlatantMisogyny, r/TheLeftCantMeme, r/Forwards-
FromKlandma
r/atheism
r/exmuslim, r/antitheistcheesecake, r/extomatoes,
r/Antitheism, r/atheismindia, r/mormon, r/progres-
sive_islam, r/Judaism, r/RadicalChristianity, r/re-
ligiousfruitcake
r/spirituality
r/SpiritualAwakening, r/awakened, r/pureretention,
r/Stoicism, r/Shamanism, r/starseeds, r/Mediums, r/-
Soulnexus, r/Semenretention, r/SASSWitches
r/religion
r/AskAChristian,
r/ChristianUniversalism,
r/Rad-
icalChristianity,
r/bahai,
r/hinduism,
r/shia,
r/Bible, r/progressive_islam, r/extomatoes, r/mor-
mon
Table 15: For each subreddit in the controversial topics analysis, the 10 most similar subreddits in terms of values.

```
