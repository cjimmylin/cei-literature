---
title: "The Moral Foundations Reddit Corpus - PDF Extract"
source_pdf: "2022-Trager-The Moral Foundations Reddit Corpus.pdf"
pages: 13
extracted_at: "2026-01-24T17:05:11.986666"
---

# PDF Extract: The Moral Foundations Reddit Corpus

**Source PDF:** 2022-Trager-The Moral Foundations Reddit Corpus.pdf
**Total Pages:** 13

---

## Content

```
--- Page 1 ---

The Moral Foundations Reddit Corpus
Jackson Trager1,*, Alireza S. Ziabari1,*, Elnaz Rahmati1, Aida Mostafazadeh Davani2,
Preni Golazizian1, Farzan Karimi-Malekabadi1, Ali Omrani3, Zhihe Li1, Brendan
Kennedy4, Nils Karl Reimer1, Melissa Reyes1, Kelsey Cheng1, Mellow Wei1,
Christina Merrifield1, Arta Khosravi1, Evans Alvarez1, and Morteza Dehghani1
1University of Southern California
2Google
3Snap Inc.
4Pacific Northwest National Laboratory
Corresponding author: jptrager@usc.edu
Abstract
Moral framing and sentiment can affect a variety of online and offline behaviors, including donation, environmental
action, political engagement, and protest.
Various computational methods in Natural Language Processing
(NLP) have been used to detect moral sentiment from textual data, but achieving strong performance in such
subjective tasks requires large, hand-annotated datasets. Previous corpora annotated for moral sentiment have
proven valuable, and have generated new insights both within NLP and across the social sciences, but have
been limited to Twitter. To facilitate improving our understanding of the role of moral rhetoric, we present the
Moral Foundations Reddit Corpus, a collection of 16,123 English Reddit comments that have been curated from
12 distinct subreddits, hand-annotated by at least three trained annotators for 8 categories of moral sentiment
(i.e., Care, Proportionality, Equality, Purity, Authority, Loyalty, Thin Morality, Implicit/Explicit Morality) based
on the updated Moral Foundations Theory (MFT) framework.
We evaluate baselines using large language
models (Llama3-8B, Ministral-8B) in zero-shot, few-shot, and PEFT settings, comparing their performance to
fine-tuned encoder-only models like BERT. The results show that LLMs continue to lag behind fine-tuned encoders
on this subjective task, underscoring the ongoing need for human-annotated moral corpora for AI alignment evaluation.
Keywords: moral sentiment annotation, moral values, moral foundations theory, multi-label text classifica-
tion, large language models, benchmark dataset, evaluation and alignment resource
1.
Introduction
Moral rhetoric and framing play a role in increasing
polarization and divisions in our societies (Marietta,
2008; Dehghani et al., 2016; Brady et al., 2020),
but also in a wide range of pro-social behaviors that
can potentially bring people together (Voelkel et al.,
2022; Wolsko, 2017; Kidwell et al., 2013; Moaz,
2020). In order to understand the relationship be-
tween hate, division, compassion, and unity in the
digital age, we need to understand the dynamics
of moral language online. In particular, capturing
and investigating the moral sentiment of text can
allow for the study of how individuals’ and groups’
expressed moral sentiment relate to various down-
stream online and offline behaviors.
Moral sentiment assessment and classification
are subjective tasks, and when done automatically
using Natural Language Processing (NLP) tech-
niques, this subjectivity results in the need for large
and diverse, both in terms of topics and coders,
sets of annotations. The Moral Foundations Twitter
Corpus (MFTC; Hoover et al., 2020), a collection of
35,108 tweets that have been curated from seven
distinct domains of discourse and hand annotated
for 10 categories of moral sentiment (care, harm,
fairness, inequality, loyalty, betrayal, authority, sub-
version, purity, and degradation) based on the
Moral Foundations Theory (Haidt, 2012; Graham
et al., 2011), was released a few years ago. This
corpus has been used to design novel methods for
moral sentiment classification (Asprino et al., 2022;
Lan and Paraboni, 2022; Burton, 2022; Araque
et al., 2020; Wang and Liu, 2021; Wu and Huang,
2022), utilized in models to investigate the impacts
of moral framing in other domains (e.g., misinforma-
tion, polarization, and hate; Mutlu et al., 2020; Ab-
durahman et al., 2025; Ruch et al., 2022; Kennedy
et al., 2023), and has been applied to train models
that produce morally salient text (e.g., arguments
and jokes; Alshomary et al., 2022; Yamane et al.,
2021). In the era of large language models (LLMs),
MFTC has been employed in evaluating the moral
reasoning of LLMs (Ramezani and Xu, 2024) and
serves as a foundation for new moral-reasoning
benchmarks (Trager et al., 2025), underscoring
how morally annotated corpora support both eval-
uation and alignment work. However, as useful
as MFTC is, its training dataset is limited to the
social-media platform Twitter.
Different online social media platforms have dif-
ferent linguistic and social structural environments
that may result in variations in moral language and
behavior (Curiskis et al., 2020). Different platforms
have varying character limits (e.g. 280 characters
on Twitter compared to 10k-40k on Reddit) which
alters the language usage of users (Boot et al.,
2019) and therefore may contribute to differences
in the use and effectiveness of moral rhetoric (Can-
dia et al., 2022). Additionally, different platforms
arXiv:2208.05545v3  [cs.CL]  18 Oct 2025

--- Page 2 ---

have different policies with respect to the levels
of user anonymity and sensitive content modera-
tion which may influence the domains of moral-
ity discussed given the potential judgements from
others. Research has shown that higher levels of
anonymity reduces the feeling of responsibility and
alters moral behavior online (Simfors and Rudling,
2020). Lastly, modern NLP methods are known to
require massive training data for producing suffi-
ciently accurate, generalizable, and robust models.
It has empirically been shown that diverse sets of
training data, from different platforms and on differ-
ent topics, can help improve the classification re-
sults by allowing the models to obtain generalized
domain knowledge (see Kennedy et al., 2022a),
rather than surface knowledge restricted to a par-
ticular platform and a small set of topics.
As mentioned previously, the MFTC relied on
the Moral Foundation Theory’s framework which
is a pluralistic perspective of moral cognition and
identifies multiple dimensions of moral values that
have evolved to facilitate individual well-being,
coalitional unity, and cooperation with strangers
(Haidt, 2012; Graham et al., 2013).
The orig-
inal version of the theory identified five sepa-
rate but interrelated categories of moral concerns:
Care/Harm, Fairness/Cheating, Loyalty/Betrayal,
Authority/Subversion, and Purity/Degradation. Re-
cently, a revision to the Moral Foundations Theory
(Atari et al., 2023) split Fairness into the distinct
and new foundations of Equality and Proportional-
ity, while retaining the other four existing founda-
tions. This split aims to capture the distinct moral
concerns of fairness in procedure (proportionality)
and equality of outcome (equality). In order to bet-
ter understand the different nuances that will result
from this theoretical change, we need to have an
updated annotated corpus that complies with the
latest theoretical revisions.
Together, the above reasons call for a corpus
from a different platform, focused on a diverse set
of topics, and annotated by a diverse group of an-
notators. Here we address this need by introducing
the Moral Foundations Reddit Corpus (MFRC), a
collection of 16,123 Reddit.com comments an-
notated for 8 categories of moral sentiment and
curated from 12 morally-relevant subreddits.
Reddit is a public social media platform with over
52 million daily users who post content in over
138,000 active “subreddits” (user-created and user-
moderated communities about different subjects)
(Upvoted Staff, 2021). Shared content and com-
ments in subreddits are “voted” on by users which is
used to decide the visibility of the post. Activity on
Reddit has been the center of numerous prominent
cultural moments including coordinated attempts to
challenge short-sellers of GameStop stock (Roose,
2021) or attempts to identify the Boston bombing
terrorists (Starbird et al., 2014).
We focused our corpus compilation effort on Red-
dit for a number of reasons. First, in comparison to
Twitter, Reddit shares many of the same research
friendly features (e.g., responsiveness to current
events, public posts, and available APIs) (Proferes
et al., 2021), but is organized into what are called
subreddits. Different subreddits have distinct top-
ics and consistent communities (Datta and Adar,
2019; Soliman et al., 2019) with varying cultures
and norms (Chandrasekharan et al., 2018; Fiesler,
2019). In relation to morality, these distinct com-
munities and norms have led researchers to use
Reddit to investigate moral conflicts across groups
(e.g., Kumar et al., 2018), a phenomena that is
harder to investigate on Twitter (which does not
have organized groups) or Facebook (where many
groups are private). Second, Reddit provides more
anonymity than many other social media platforms,
potentially enabling users to more freely speak their
minds and express their opinions (e.g., Triggs et al.,
2021; De Choudhury and De, 2014; Simfors and
Rudling, 2020). Third, in addition to general differ-
ences in language usage (Boot et al., 2019), the
lack of restriction on the length of posts on Reddit
may be particularly beneficial for training models.
Fourth, we believe that Reddit has played a dis-
tinct role in contemporary politics. For example,
the r/TheDonald and r/incels subreddits have been
linked to political extremism (Gaudette et al., 2021)
and mass shootings (Helm et al., 2022).
To examine the effectiveness of LLMs for moral
concern detection, we evaluate Ministral (Jiang
et al., 2024) and Llama (Dubey et al., 2024) under
both zero-shot and few-shot prompting settings for
single-label and multi-label text classification, fol-
lowing standard prompting methodologies (Brown
et al., 2020). Beyond prompting, we also perform
parameter-efficient fine-tuning (PEFT; Hu et al.,
2022) of Llama models for single-label and multi-
label classification tasks (Tsoumakas and Katakis,
2007). For comparison, we include fully fine-tuned
BERT models (Devlin et al., 2019), trained in both
single-label and multi-label configurations. These
baselines allow us to understand the validity and
relative performance of different text classification
methods for identifying the moral concerns mani-
fested in the MFRC.
Finally, in order to facilitate research into annota-
tor response patterns and bias, as recommended
by Prabhakaran et al. (2021), we provide psycholog-
ical and demographic metadata of our annotators.
The background and biases of human annotators
have been shown to impact their annotations (Hovy
and Prabhumoye, 2021; Davani et al., 2022, 2023;
Bolukbasi et al., 2016) with particularly damaging
effects that amplify pre-existing biases (Mujtaba
and Mahapatra, 2019; Zhao et al., 2017). Anno-

--- Page 3 ---

tators’ biases may be particularly relevant in do-
mains characterized by high subjectivity, such as
moral values (Garten et al., 2019a,b; Hoover et al.,
2020). While, for example, an annotator’s political
ideology might not have a substantial influence on
how they annotate “positive” and “negative” senti-
ment in a corpus of hotel reviews, it seems likely
that their ideology could substantially influence how
they annotate expressions of justice and respect in
a politically relevant corpora.
The contributions of this paper are threefold: (1)
We introduce the Moral Foundations Reddit Corpus
(MFRC), a collection of 16,123 comments curated
from 12 morally relevant subreddits and annotated
for 8 moral sentiment categories based on the re-
vised MFT. (2) We provide demographic and psy-
chological metadata of annotators to facilitate future
research on subjectivity and bias in moral sentiment
annotation. (3) We evaluate a range of baseline
models, including fine-tuned encoder-only models
and recent LLMs in zero-shot, few-shot, and PEFT
settings, establishing the MFRC as a benchmark
for both moral sentiment classification and AI align-
ment evaluation. These contributions collectively
extend prior work such as the MFTC (Hoover et al.,
2020) to a new platform and theoretical framework,
enabling richer cross-platform and cross-cultural
analyses of moral language online.
2.
Corpus Overview
As noted above, the MFRC consists of 16,123 Red-
dit comments drawn from 12 different subreddits.
These subreddits were chosen based on the fol-
lowing criteria: First, we focused on subreddits that
we expected to contain a wide range of moral con-
cerns. Second, the chosen subreddits had to be
active and have sufficient data. Third, we aimed to
have a non-US based political subreddit with focus
on current events that could be of use for differ-
ent research communities. Accordingly, our cor-
pus consists of 12 subreddits organized into three
buckets; US politics, French politics, and Everyday
moral life. The US politics bucket contains com-
ments from 3 subreddits from the dates 1/1/2020 -
1/31/2021; r/politics which captures political moral
language generally, r/conservative which covers
moral rhetoric of the right, and r/antiwork which cov-
ers different, but still political moral language from
the left. The everyday moral life bucket is a collec-
tion of topics related to various aspects of everyday
life, collected for their non-political moral judgement
and moral emotions which includes comments from
the 4 subreddits of r/nostalgia, r/AmitheAsshole,
r/confession, and r/relationshipadvice between the
dates of 1/1/2020 - 1/31/2021. The third bucket on
French politics and contains comments from the
subreddits of r/europe, r/worldnews, r/neoliberal,
r/geopolitics, and r/Conservative that had the rel-
evant keywords related to the presidential race in-
cluding ‘Macron’, ‘Le Pen’, ‘France’, ‘French’, and
‘Hollande’ (see below for the full set of keywords
used) from the dates of 01/01/2017 to 06/30/2017
and had at least 10 likes/comments in order to con-
trol for sufficient engagement.
The MFRC will be available for download as a
HuggingFace dataset.
2.1.
General Sampling Procedure
In assembling the MFRC, we sampled Reddit posts
from a larger set of each subreddit. Our initial fil-
tering criteria selected posts of sufficient length
(at least 10 tokens), and de-selected any posts
that were automatically marked by reddit as a bot,
with the text “I am a bot” appended to the end of
the post. The French politics bucket was also fil-
tered for comments that mentioned at least one of
the French presidential candidates (‘macron’, ‘le
pen’, ‘hollande’, ‘dupont-aignan’, ‘hamon’, ‘arthaud’,
‘poutou’, ‘cheminade’, ‘lassalle’, ‘melenchon’, ‘asse-
lineau’, ‘fillon’) in which most hits were for frontrun-
ners Macron, Le pen, Hollande, and Fillon. For the
US Politics and Everyday buckets, comments were
selected that had a comment score of at least 10.
In this filtered set, the proportion of comments
that contained moral sentiment proved too low to
conduct fully randomized sampling in a way that
would result in a sufficient amount of moral exam-
ples. While these subreddits were chosen specif-
ically for their potential moral salience, research
has shown that use of moral language in some
domains are rare (Atari et al., 2022). To address
this issue, a semi-supervised method was used to
up-sample from moralized posts (Kennedy et al.,
2022b). Specifically, we first used word embed-
dings and a list of moral foundations seed words
to compute a moral loading score (DDR; Garten
et al., 2018) for every comment. Next, for each
moral concern, we computed the 95% percentile
scores to mark the highly moral comments and set
bin size. Finally, in order to have a diverse range of
moral posts, we compiled comments in a manner
that each subreddit bucket consisted of 1/2 com-
ments with high moral loading (> 95%), and 1/2
comments with less high moral loading (≤95%).
This filtering and sampling procedure yielded ap-
proximately 6,000 comments for US Politics, 6,000
for Everyday Politics, and 8,000 comments for
French politics. However, since vice, virtue, and
multiple foundations regularly co-occur in an in-
dividual comment, duplicates occurred and were
subsequently removed, resulting in a smaller final
sample size for each bucket (US Politics: 4,821;
French Politics: 6,489; Everyday Morality: 4,813;
Total: 16,123).

--- Page 4 ---

3.
Annotation
Every post in the MFRC has been labeled by at
least three trained annotators from a set of five (see
Table 1 for the distribution of annotators for the cor-
pus) for 8 categories of moral sentiment as outlined
in the new version of our annotation manual, (will
be provided in Supplementary Materials).
3.1.
Moral sentiment
Moral sentiment labels are drawn from the re-
cently revised typology of Moral Foundations The-
ory (Atari et al., 2023), which proposes a six-factor
taxonomy of morality. In this model, each factor
includes both virtues, or prescriptive moral con-
cerns, and vices, prohibitive moral concerns. The
proposed moral foundations are (Atari et al., 2023):
Care/Harm: Intuitions about avoiding emotional
and physical damage or harm to others. It underlies
virtues of kindness, gentleness, and nurturing, and
vices of meanness, violence, and abuse.
Equality/Inequality: Intuitions about egalitarian
treatment and equal outcome for all individuals and
groups. It underlies virtues of social justice and
equality, and vices of discrimination and prejudice.
Proportionality/Disproportionately: Intuitions
about individuals getting rewarded in proportion to
their merit (i.e., effort, talent, or input). It underlies
virtues of meritocracy, productiveness, and deserv-
ingness, and vices of corruption and nepotism.
Loyalty/Betrayal: Intuitions about in-group co-
operation and out-group competition. It underlies
virtues of patriotism and self-sacrifice for the group,
and vices of abandonment, cheating, and treason.
Authority/Subversion: Intuitions about defer-
ence toward legitimate authorities and high-status
individuals. It underlies virtues of leadership and
respect for tradition, and vices of disorderliness
and resenting hierarchy.
Purity/Degradation: Intuitions about avoiding
bodily and spiritual contamination and degradation.
It underlies virtues of sanctity, nobility, and cleanli-
ness and vices of grossness, impurity, and sin.
Notably, unlike the MFTC, in the MFRC we did
not code for Fairness. Rather, following the latest
theoretical developments in the field (Atari et al.,
2023), we coded for separate foundations of Pro-
portionality and Equality.
In addition to these six foundations, annotators
were trained to look for an additional construct: Thin
Morality – a moral judgment or concern which is
voiced without clearly referring to one of the six
moral domains (Atari et al., 2022). This brings the
total categories of moral sentiment to 7. Annota-
tors also had a formal category for Implicit/Explicit
Morality – whether the moral sentiment in the com-
ment was expressed explicitly or implicitly. Lastly,
the annotators were asked to report their overall
level of confidence in their annotation as not confi-
dent, somewhat confident, or very confident.
Table 1: Number of Reddit Posts Annotated by
N Annotators for Each Subreddit
N Annotator
Subreddit
3
4
5
r/AmItheAsshole
1009
330
-
r/Conservative(French politics)
75
69
-
r/Conservative(US politics)
870
898
8
r/antiwork
885
882
4
r/confession
993
338
-
r/europe
1338
1302
7
r/geopolitics
53
59
1
r/neoliberal
846
815
12
r/nostalgia
994
348
-
r/politics
864
894
10
r/relationship_advice
1021
331
1
r/worldnews
1267
1288
9
3.2.
Annotators
We started with a larger pool of 27 annotators, all
undergraduate research assistants who completed
two months of training sessions to develop expert-
level familiarity with MFT. Training consisted of lec-
tures, discussions, readings, and practice annota-
tions with inter-annotation agreement analysis. In
early annotation stages, annotator disagreement
was addressed through discussion and, if neces-
sary, certain labels were modified. However, given
the subjective nature of the task, in many cases, it is
difficult to make the determination of whether or not
a document expresses moral sentiment or which
category of moral sentiment it expresses. While it
is necessary to have consistent annotator training,
a focus on maximizing annotator agreement risks
artificially inflating agreement at the cost of sup-
pressing the natural variability of moral sentiment
(Hoover et al., 2020). Accordingly, our annotators
were trained to both strive for consistency, while
also encouraged to avoid stereotypes that may in-
crease agreement with other annotators but would
lead them to ignore their own beliefs. Out of these
original set of annotators, we selected the top five
performing annotators, based on both inter-coder
reliability assessments and the commitment of the
annotators to the project, to become primary anno-
tators and complete the rest of the annotations in
our corpus.
Our trained annotators were independently as-
signed to label each comment from a subset of
comments sampled from a corpus associated with
one of the 12 subreddits (see Table 2). The an-
notations were performed on Prodigy.1 Each post
1https://prodi.gy/

--- Page 5 ---

was assigned a label indicating the absence or
presence of the six foundations, thin morality, ex-
plicit/implicit expression, and the confidence level of
the annotator (MFT Coding Manual will be included
in the Supplementary Materials).
3.3.
Annotator Metadata
We have also collected responses to a range of
psychological and demographic measures from our
annotators. While keeping their identities anony-
mous, we provide measures of each annotator’s
gender, sexual orientation, age, household income,
first language, political ideology along a liberal-
conservative scale, religious affiliation, and moral
values via the Moral Foundation Questionnaire-2
(Atari et al., 2023). Basic analyses demonstrate
that our annotators’ political ideology and morality
skews liberal while family income skews wealthier
than the average American. Based on the recom-
mendations of Prabhakaran et al. (2021), in order
to increase utility and transparency of this corpus,
we include these measures (will be included in Sup-
plementary Materials) and encourage research into
their potential impact on annotations, and the sub-
sequent biases in the machine learning models.
4.
Annotation Results
The annotation results can be seen in Table 2.
Recall that each post was annotated for multiple
labels by multiple annotators, and the frequencies
reported in Table 2 are calculated based on anno-
tators’ majority vote (i.e. posts receiving at least
50% agreement for that label). For example, if a
particular post is annotated as ‘proportionality’ by
at least 50% of the annotators who coded that post,
then the majority vote on ‘proportionality’ for that
post is positive. We acknowledge the uneven dis-
tribution of labels across the various subreddits, in
addition to the low base-rates of annotated posts
for some the moral concerns, especially for Purity,
Loyalty and Proportionality concerns.
The interannotator agreement results, using
Fleiss’s (Fleiss, 1971) kappa and prevalence-and
bias-adjusted Fleiss’s kappa (PABAK; Sim and
Wright, 2005) for multiple annotators, are displayed
in Figure 1. Fleiss’s kappa is generally viewed as
the gold standard measure for investigating agree-
ment across many annotators, and it represents the
degree of agreement beyond what is expected by
chance. This measure though, is heavily influenced
by the prevalence of positive cases. Given the sub-
jective nature of our task, and the fact that positive
cases are not prevalent given the often rarity of
moral rhetoric (Atari et al., 2022), we use PABAK
which adjusts kappa for prevalence and bias. As ex-
pected, given the low base rate of moral language
across the various subreddits (i.e. low positive
cases), most reported kappa’s are low. However,
once adjusted for the issue of prevalence, we see
medium to high agreements across the subreddits.
Figure 1:
The heatmaps show Interannotator
Agreement (PABAK and Kappa) scores for all sub-
reddits and foundations. Higher agreement corre-
sponds with darker colors in both heatmaps.
(a) Fleiss’ kappa
(b) PABAK
5.
Baseline Classification Models
In addition to compiling the corpus, we experiment
with different models and provide baselines for pre-
dicting the annotators’ majority vote of moral sen-
timent categories. Our goal is to simply establish
baselines that future work can build on.
It should be noted that each post in MFRC was
coded by multiple annotators for 8 different cat-
egories of moral sentiment discussed under the
Section 3. This is a multi-label classification task;
i.e., not only are the categories of moral sentiment
not independent of one another, but understanding
variance in one domain should theoretically inform
about other related moral domains. Here though,

--- Page 6 ---

Table 2: Frequency of Reddit posts per Foundation Calculated Based on Annotators’ Majority Vote.
Subreddit
Care Equality Proportionality Loyalty Authority Purity Thin Morality Non-Moral
r/AmItheAsshole
343
145
103
56
50
38
227
456
r/Conservative(French politics)
12
5
6
7
16
0
18
95
r/Conservative(US politics)
195
200
84
38
155
45
231
945
r/antiwork
304
132
202
46
86
29
186
930
r/confession
281
69
101
24
52
50
249
574
r/europe
105
180
117
107
174
18
324
1741
r/geopolitics
1
4
5
1
5
0
9
100
r/neoliberal
39
74
67
50
117
11
195
1210
r/nostalgia
20
11
15
5
8
9
207
1160
r/politics
148
119
72
61
161
34
256
1016
r/relationship_advice
418
137
84
98
31
56
191
450
r/worldnews
166
249
127
105
192
33
321
1543
All
2032
1325
983
598
1047
323
2414
10220
we provide both single-label (treating labels as in-
dependent) and multi-label classification results.
Zero-shot and Few-shot Prompting
To estab-
lish an initial baseline, we evaluate two widely used
open-source LLMs, Meta-Llama-3-8B (Dubey et al.,
2024) and Ministral-8B-Instruct-2410 (Jiang et al.,
2024), using zero-shot prompting for both single-
label and multi-label classification. We further ex-
plore few-shot prompting to assess whether in-
cluding example instances for in-context learning
(Brown et al., 2020) improves performance. For
this setup, we select five stratified samples based
on label distribution and include them in the prompt.
Classification Fine-tuning
To examine the im-
pact of training on LLM performance, we fine-tune
the Llama model using parameter-efficient training
(Hu et al., 2022) and evaluate its improvement on
our dataset. Prior work has shown that for dis-
criminative tasks, encoder-only models with full
fine-tuning can outperform LLMs even after train-
ing (Qorib et al., 2024; Roccabruna et al., 2024).
Therefore, we also include results from fine-tuning
the BERT model (Devlin et al., 2019). Since this
model is smaller, we apply full fine-tuning (FFT)
instead of PEFT.
Due to the sparsity of our data, with far fewer
moral posts than non-moral posts, we employ a
weighted loss function. In this setup, the weight of
sample i for label l is inversely proportional to the
frequency of that label:
wi,l ∝
1
number of samples with label l
(1)
The baseline metrics we report are the F1, preci-
sion, and recall, which are calculated across strati-
fied 5-fold cross-validation. For the multi-label mod-
els, we stratified the data based on the moral senti-
ment label (the union of all the moral labels). We
used 10% of the training data for validation, and we
chose the best performing model based on binary
F1 for single-label classification and F1 macro for
multi-label BERT. We train LLMs with a learning
rate of 1e-5, batch size of 8, and 4 epochs, while
BERT models are trained with a learning rate of
2e-5, batch size of 8, and 5 epochs. For multi-label
classification, we double the number of training
epochs. Learning rates are determined empirically
from a search over the range [1e-4, 1e-6].
6.
Results
The results of the baseline models are provided
in Table 3. We provide both the average F1 score
and standard deviations for each moral category
(All metrics including recall and precision will be
included in the appendix). We ran each of the base-
line models once for the entire corpus. Consistent
with prior work (Qorib et al., 2024; Roccabruna
et al., 2024), BERT models outperform the fine-
tuned Llama models in terms of F1. Interestingly,
the multi-label BERT model performed worse than
its single-label counterpart, whereas the multi-label
trained Llama achieved comparable or better re-
sults than the single-label version.
We then evaluated the best performing BERT
models on the three subreddit buckets separately
(French Politics, Everyday, and U.S. Politics). Con-
sistent with previous results, BERT (single-label)
outperformed BERT (multi-label) across all moral
categories in all three buckets. However, perfor-
mance varied across subreddits: certain moral
foundations were predicted more accurately within
the Everyday bucket, while others showed higher
scores in U.S. Politics. This pattern suggests that
subreddit focus and community context influence
model performance, reflecting how moral language
varies across online domains.

--- Page 7 ---

Table 3: F1 scores (mean ± standard deviation) by moral category on the full MFRC dataset, comparing
models under different methods: zero-shot, few-shot prompting, parameter-efficient fine-tuning (PEFT),
and full fine-tuning (FFT).
Method
Model
Care
Equality
Prop
Loyalty
Authority
Purity
Thin
0-shot
Llamasingle
0.400.004
0.290.004
0.210.004
0.170.004
0.200.004
0.170.011
0.230.006
Llamamulti
0.280.003
0.310.011
0.200.017
0.140.006
0.180.013
0.130.017
0.010.004
Ministralsingle
0.240.014
0.250.010
0.150.019
0.210.011
0.090.008
0.100.013
0.080.008
Ministralmulti
0.410.010
0.270.006
0.190.005
0.170.009
0.220.012
0.170.009
0.200.012
5-shot
Llamasingle
0.430.005
0.210.002
0.210.008
0.140.002
0.200.002
0.120.003
0.260.005
Llamamulti
0.330.005
0.330.011
0.140.022
0.180.012
0.190.011
0.140.020
0.010.001
Ministralsingle
0.260.018
0.330.009
0.130.014
0.210.011
0.000.002
0.210.007
0.200.006
Ministralmulti
0.440.010
0.300.010
0.210.013
0.180.019
0.250.010
0.170.017
0.150.004
PEFT
Llamasingle
0.540.012
0.510.016
0.280.011
0.320.007
0.340.015
0.220.012
0.270.024
Llamamulti
0.530.013
0.520.009
0.280.024
0.400.016
0.360.016
0.310.037
0.250.049
FFT
BERTsingle
0.620.020
0.580.030
0.370.040
0.450.040
0.400.050
0.510.070
0.390.020
BERTmulti
0.590.020
0.570.030
0.310.050
0.430.040
0.350.040
0.480.070
0.340.040
7.
Cross-Corpus Classification
In this section, we evaluate preliminary results on
the transferability of models between MFTC and
MFRC. Our hope is that future work can build on
such cross-domain tasks in order to extract more
generalized knowledge about moral rhetoric inde-
pendent of the source and topic of the post.
In order to provide a fair comparison between
MFRC and MFTC, we trained BERT models with
the same hyperparameter discussed in the previous
section. Additionally, we downsampled the MFTC
dataset to have the same number of samples for
each label as MFRC. The results are presented in
Table 4. In general, models trained and tested on
the MFTC have better classification performance
than the results for the MFRC (See Table 3).
Table 4: BERT Results on MFTC
Foundation
F1
Precision
Recall
Authority
0.65(0.02)
0.65(0.04)
0.65(0.05)
Care
0.75(0.02)
0.76(0.03)
0.74(0.03)
Fairness
0.82(0.01)
0.83(0.04)
0.81(0.03)
Loyalty
0.58(0.05)
0.66(0.09)
0.52(0.06)
Purity
0.54(0.04)
0.63(0.05)
0.48(0.05)
As mentioned before, the MFRC relies on the
updated taxonomy of MFT in which the Fairness
foundation is split into Proportionality and Equality.
This makes the cross-corpus training for Fairness,
Proportionality and Equality difficult. We hope the
MFTC will be updated to use the more nuanced
Proportionality and Equality labels in that corpus.
For now though, for predicting Fairness labels in
the MFTC, the union of Proportionality and Equality
labels are calculated based on the MFRC trained
models, and the output of the union is then com-
pared to the Fairness category in the MFTC. Simi-
larly, to evaluate the MFTC Fairness models on the
MFRC, both Proportionality and Equality are as-
signed the Fairness label predicted from the MFTC.
Table 5: BERT Models Trained on MFRC, Evaluate
on MFTC
Foundation
F1
Precision
Recall
Authority
0.38
0.53
0.30
Care
0.53
0.58
0.48
Fairness
0.35
0.76
0.23
Loyalty
0.38
0.50
0.31
Purity
0.28
0.56
0.18
Table 6: BERT Models Trained on MFTC, Evaluate
on MFRC
Foundation
F1
Precision
Recall
Authority
0.31
0.23
0.44
Care
0.43
0.53
0.35
Fairness
0.34
0.36
0.32
Loyalty
0.32
0.48
0.23
Purity
0.34
0.52
0.25
Cross-corpus results are presented in Tables 5
and 6. These preliminary results are indeed en-
couraging in that we demonstrate transferability be-
tween the two corpora in predicting out-of-domain
distributions. Previous research training classifiers
on the MFTC, and testing on Reddit (e.g., Atari
et al., 2021) have shown similar levels of accuracies
for cross-domain classification. Any cross-corpus
investigation should take into account the different
time periods in which these two corpora were com-
piled. This difference can potentially impact the
topics, the sentiments expressed about the topics,
and the type of justification and reasoning used
for the expressed sentiments. We believe though

--- Page 8 ---

that more advanced methods in knowledge cap-
ture and representation could use the two corpora
together to further achieve more generalized and
better performing models.
8.
Discussion
Moral rhetoric and framing have been shown to
be predictive of various important pro-social and
anti-social behaviors. Several NLP methods have
recently been proposed for capturing and catego-
rizing moral sentiment based on textual data (Atari
and Dehghani, 2021). However, this is a subjec-
tive sentiment analysis task for which training data
plays a vital role. To facilitate further research in
this domain, here we introduced the MFRC, a col-
lection of 16,123 Reddit comments annotated for
8 categories of moral sentiment, and provided a
number of baseline results for different NLP models
trained to predict moral sentiment.
The MFTC was introduced in 2020, and so far
this corpus has already facilitated multiple lines of
research in both NLP and the social sciences. We
believe Reddit’s distinct linguistic and social struc-
ture, along with MFRC’s methodological and the-
oretical updates, allow for potential new research
that can both improve and expand the applications
of MFTC. Specifically, the increased character lim-
its on Reddit compared to Twitter is important for
the more naturalistic expressions of moral rhetoric
and its potential impact on the performance of clas-
sification models. While social media often pro-
vides large amount of data needed for training NLP
models, with respect to sentiment analysis of moral
language, the paucity of moral rhetoric in some do-
mains (Atari et al., 2022) makes it difficult to gather
sufficient amounts of training data (Hoover et al.,
2020). Given Reddit’s longer posts, models trained
on the MFRC may perform better in out of domain
tasks, especially in longer documents (e.g., articles
or speeches compared to tweets). Further, the dis-
tinct subreddit communities allow for the study of
group linguistic dynamics. For example, shifts in
moral language over time associated with a hash-
tag on Twitter may show the evolving general public
opinion on a topic, while shifts in moral language
within a particular subreddit may reflect the chang-
ing views of a specific community.
Our results also showed that model performance
varied across subreddits, suggesting that Reddit’s
community-based structure represents a distinct
linguistic and moral domain compared to other plat-
forms. Recognizing these structural differences is
important for interpreting the downstream group
behaviors associated with moral language use on
different platforms, such as voting and political mo-
bilization. Moreover, the increased anonymity on
Reddit can facilitate research into the gap between
identity-linked and publicly-expressed moral con-
cerns, such as on Facebook or Linkedin, and anony-
mous expressions of moral values, as on Reddit.
As discussed previously, another important fea-
ture of the MFRC is that it is based on the newly
updated version of the Moral Foundations Theory
(Atari et al., 2023) which breaks the Fairness con-
cern into the distinct moral concerns of Proportion-
ality and Equality. The MFRC can be used to further
investigate these nuances of fairness across topics
such as income inequality and excessive wealth.
Similar to the MFTC, the MFRC has detailed
meta-data on the corpus annotators. We hope that
by providing demographics and several key psycho-
logical measurements of our annotators, MFRC can
facilitate future research into how annotators back-
ground characteristics impact their annotations.
As shown in Table 3, fine-tuned models (BERT
and PEFT-Llama) substantially outperform the zero-
shot and few-shot baselines across all moral cate-
gories on MFRC. This pattern is consistent with the
view that subjective, label-rich moral classification
benefits most from domain-specific supervision, re-
inforcing the value of large, human-annotated cor-
pora for both evaluation and downstream alignment
work (Abdurahman et al., 2024).
In conclusion, we hope that the MFRC, along
with this report, in addition to the other previously re-
leased corpora in this domain (e.g., Kennedy et al.,
2022b; Hoover et al., 2020; Trager et al., 2025), can
aid researchers by providing much-needed data
and open new lines of research both in NLP and
in the social sciences. In an age where political
movements, grassroots activism, and plans for in-
surrections seem to take place in online environ-
ments, it is vital that we can better understand the
moral dynamics of these online conversations. The
intent of this project has been to further facilitate
research into these timely topics.
9.
Data Disclaimer
We acknowledge that the compiled dataset con-
tains biases and is not representative of diverse
moral concerns present in world populations. Po-
tential biases in the data include: biases specific to
English-speaking countries and the English lan-
guage, biases inherent to Reddit.com and its
user base, biases in the researchers’ criteria for
corpus curation as well as the underlying MFT it-
self, bias in the assessment of moral labels, and
the fact that annotators were all undergraduate re-
search assistants at a private academic institute.
All of these factors, among others, likely influenced
the annotations, as well as the performance of ma-
chine learning models trained on the corpus. Any-
one using this corpus should be aware of these
limitations and should acknowledge and/or try to

--- Page 9 ---

Table 7: Model F1 (mean ± sd) by Moral Category on the three Subreddit Buckets (French Politics,
Everyday, US Politics)
Model
Subreddit Bucket
Care
Equality
Prop
Loyalty
Authority
Purity
Thin
BERTsingle
French Politics
0.430.04
0.590.03
0.160.05
0.410.08
0.200.12
0.320.15
0.410.04
Everyday
0.720.02
0.610.06
0.370.08
0.470.08
0.340.11
0.510.10
0.370.05
US Politics
0.540.05
0.580.04
0.420.07
0.510.09
0.510.05
0.370.16
0.360.05
BERTmulti
French Politics
0.330.05
0.510.06
0.060.07
0.330.10
0.260.04
0.200.16
0.370.05
Everyday
0.660.04
0.560.07
0.340.08
0.300.07
0.210.10
0.450.12
0.250.03
US Politics
0.450.07
0.550.06
0.400.08
0.440.11
0.430.09
0.340.20
0.250.07
mitigate them to the extent possible.
10.
Ethics Statement
This work adheres to ethical standards for research
involving human annotations and publicly available
data. All annotators participated voluntarily, were
compensated fairly, and received extensive training
on respectful engagement with sensitive moral
and political content. Annotation sessions included
monitoring for emotional well-being and debriefing
opportunities to mitigate potential distress. The
study protocol was reviewed and approved by the
authors’ institutional ethics board. We highlight
that models trained on this corpus should be used
only for scientific and educational purposes, and
not for applications that could profile, surveil, or
harm individuals or communities.
11.
Bibliographical References
Suhaib Abdurahman, Mohammad Atari, Farzan
Karimi-Malekabadi, Mona J Xue, Jackson Trager,
Peter S Park, Preni Golazizian, Ali Omrani, and
Morteza Dehghani. 2024. Perils and opportuni-
ties in using large language models in psycho-
logical research. PNAS nexus, 3(7):pgae245.
Suhaib Abdurahman, Nils K Reimer, Preni Golaz-
izian, Elisa Baek, Yixuan Shen, Jackson Trager,
Roshni Lulla, Jonas Kaplan, Carolyn Parkinson,
and Morteza Dehghani. 2025. Targeting audi-
ences’ moral values shapes misinformation shar-
ing. Journal of Experimental Psychology: Gen-
eral.
Milad Alshomary, Roxanne El Baff, Timon Gurcke,
and Henning Wachsmuth. 2022. The moral de-
bater: A study on the computational generation
of morally framed arguments. In Proceedings
of the 60th Annual Meeting of the Association
for Computational Linguistics (Volume 1: Long
Papers), pages 8782–8797.
Oscar Araque, Lorenzo Gatti, and Kyriaki Kalimeri.
2020.
Moralstrength: Exploiting a moral lex-
icon and embedding similarity for moral foun-
dations prediction. Knowledge-based systems,
191:105184.
Luigi Asprino, Luana Bulla, Stefano De Giorgis,
Aldo Gangemi, Ludovica Marinucci, and Misael
Mongiovì. 2022. Uncovering values: Detecting
latent moral content from natural language with
explainable and non-trained methods. In Pro-
ceedings of Deep Learning Inside Out (DeeLIO
2022): The 3rd Workshop on Knowledge Extrac-
tion and Integration for Deep Learning Architec-
tures, pages 33–41.
Mohammad Atari, Aida Mostafazadeh Davani,
Drew Kogon,
Brendan Kennedy,
Nripsuta
Ani Saxena, Ian Anderson, and Morteza De-
hghani. 2021. Morally homogeneous networks
and radicalism. Social Psychological and Per-
sonality Science, page 19485506211059329.
Mohammad Atari and Morteza Dehghani. 2021.
Language analysis in moral psychology.
In
Morteza Dehghani and Ryan L. Boyd, editors,
Handbook of language analysis in psychology,
pages 207–228. Guilford.
Mohammad Atari, Jonathan Haidt, Jesse Graham,
Sena Koleva, Sean T Stevens, and Morteza De-
hghani. 2023. Morality beyond the weird: How
the nomological network of morality varies across
cultures. Journal of Personality and Social Psy-
chology, 125(5):1157.
Mohammad Atari,
Matthias R. Mehl,
Jesse
Graham, John M. Doris, Norbert Schwarz,
Aida Mostafazadeh Davani, Ali Omrani, Bren-
dan Kennedy, Elaine Gonzalez, Nikki Jafarzadeh,
Alyzeh Hussain, Arineh Mirinjian, Annabelle Mad-
den, Rhea Bhatia, Alexander Burch, Allison
Harlan, David A. Sbarra, Charles L. Raison,
Suzanne A. Moseley, Angelina J. Polsinelli, and
Morteza Dehghani. 2022. The paucity of morality
in everyday talk. Scientific Reports.
Tolga Bolukbasi, Kai-Wei Chang, James Y Zou,
Venkatesh Saligrama, and Adam T Kalai. 2016.

--- Page 10 ---

Man is to computer programmer as woman is to
homemaker? debiasing word embeddings. Ad-
vances in neural information processing systems,
29.
Arnout B Boot, Erik Tjong Kim Sang, Katinka Di-
jkstra, and Rolf A Zwaan. 2019. How character
limit affects language usage in tweets. Palgrave
Communications, 5(1):1–13.
William J Brady, Molly J Crockett, and Jay J
Van Bavel. 2020. The mad model of moral con-
tagion: The role of motivation, attention, and
design in the spread of moralized content on-
line.
Perspectives on Psychological Science,
15(4):978–1010.
Tom Brown, Benjamin Mann, Nick Ryder, Melanie
Subbiah, Jared D Kaplan, Prafulla Dhariwal,
Arvind Neelakantan, Pranav Shyam, Girish Sas-
try, Amanda Askell, Sandhini Agarwal, Ariel
Herbert-Voss, Gretchen Krueger, Tom Henighan,
Rewon Child, Aditya Ramesh, Daniel Ziegler, Jef-
frey Wu, Clemens Winter, Chris Hesse, Mark
Chen, Eric Sigler, Mateusz Litwin, Scott Gray,
Benjamin Chess, Jack Clark, Christopher Berner,
Sam McCandlish, Alec Radford, Ilya Sutskever,
and Dario Amodei. 2020. Language models are
few-shot learners. In Advances in Neural Infor-
mation Processing Systems, volume 33, pages
1877–1901. Curran Associates, Inc.
Jason William Burton. 2022. Understanding and
supporting belief accuracy in a digital world. Ph.D.
thesis, Birkbeck, University of London.
Cristian Candia, Mohammad Atari, Nour Kteily, and
Brian Uzzi. 2022. Overuse of moral language
dampens content engagement on social media.
Under review.
Eshwar Chandrasekharan, Mattia Samory, Shagun
Jhaver, Hunter Charvat, Amy Bruckman, Cliff
Lampe, Jacob Eisenstein, and Eric Gilbert. 2018.
The internet’s hidden rules: An empirical study of
reddit norm violations at micro, meso, and macro
scales.
Proceedings of the ACM on Human-
Computer Interaction, 2(CSCW):1–25.
Stephan A Curiskis, Barry Drake, Thomas R Os-
born, and Paul J Kennedy. 2020. An evalua-
tion of document clustering and topic modelling
in two online social networks: Twitter and red-
dit.
Information Processing & Management,
57(2):102034.
Srayan Datta and Eytan Adar. 2019. Extracting
inter-community conflicts in reddit. In Proceed-
ings of the international AAAI conference on Web
and Social Media, volume 13, pages 146–157.
Aida Mostafazadeh Davani, Mohammad Atari,
Brendan Kennedy, and Morteza Dehghani. 2023.
Hate speech classifiers learn normative social
stereotypes. Transactions of the Association for
Computational Linguistics, 11:300–319.
Aida Mostafazadeh Davani, Mark Díaz, and Vin-
odkumar Prabhakaran. 2022. Dealing with dis-
agreements: Looking beyond the majority vote in
subjective annotations. Transactions of the Asso-
ciation for Computational Linguistics, 10:92–110.
Munmun De Choudhury and Sushovan De.
2014. Mental health discourse on reddit: Self-
disclosure, social support, and anonymity. In
Eighth international AAAI conference on weblogs
and social media.
Morteza Dehghani, Kate Johnson, Joe Hoover,
Eyal Sagi, Justin Garten, Niki Jitendra Parmar,
Stephen Vaisey, Rumen Iliev, and Jesse Gra-
ham. 2016. Purity homophily in social networks.
Journal of Experimental Psychology: General,
145(3):366.
Jacob Devlin, Ming-Wei Chang, Kenton Lee, and
Kristina Toutanova. 2019. Bert: Pre-training of
deep bidirectional transformers for language un-
derstanding. In Proceedings of the 2019 con-
ference of the North American chapter of the
association for computational linguistics: human
language technologies, volume 1 (long and short
papers), pages 4171–4186.
Abhimanyu Dubey,
Abhinav Jauhri,
Abhinav
Pandey, Abhishek Kadian, Ahmad Al-Dahle,
Aiesha Letman, Akhil Mathur, Alan Schelten,
Amy Yang, Angela Fan, et al. 2024. The llama
3 herd of models. arXiv e-prints, pages arXiv–
2407.
Casey Fiesler. 2019.
Ethical considerations for
research involving (speculative) public data. Pro-
ceedings of the ACM on Human-Computer Inter-
action, 3(GROUP):1–13.
Joseph L Fleiss. 1971. Measuring nominal scale
agreement among many raters. Psychological
bulletin, 76(5):378.
Justin Garten, Joe Hoover, Kate M Johnson, Rei-
hane Boghrati, Carol Iskiwitch, and Morteza De-
hghani. 2018.
Dictionaries and distributions:
Combining expert knowledge and large scale
textual data content analysis. Behavior research
methods, 50(1):344–361.
Justin Garten, Brendan Kennedy, Joe Hoover, Kenji
Sagae, and Morteza Dehghani. 2019a. Incorpo-
rating demographic embeddings into language
understanding. Cognitive science, 43(1):e12701.

--- Page 11 ---

Justin Garten, Brendan Kennedy, Kenji Sagae, and
Morteza Dehghani. 2019b. Measuring the im-
portance of context when modeling language
comprehension.
Behavior research methods,
51(2):480–492.
Tiana Gaudette, Ryan Scrivens, Garth Davies, and
Richard Frank. 2021. Upvoting extremism: Col-
lective identity formation and the extreme right on
reddit. New Media & Society, 23(12):3491–3508.
Jesse Graham, Jonathan Haidt, Sena Koleva, Matt
Motyl, Ravi Iyer, Sean P Wojcik, and Peter H
Ditto. 2013. Moral foundations theory: The prag-
matic validity of moral pluralism. In Advances
in experimental social psychology, volume 47,
pages 55–130. Elsevier.
Jesse Graham, Brian A Nosek, Jonathan Haidt,
Ravi Iyer, Spassena Koleva, and Peter H Ditto.
2011. Mapping the moral domain. Journal of
personality and social psychology, 101(2):366.
Jonathan Haidt. 2012. The righteous mind: Why
good people are divided by politics and religion.
Vintage.
Brenna Helm, Ryan Scrivens, Thomas J Holt, Steve
Chermak, and Richard Frank. 2022. Examining
incel subculture on reddit. Journal of Crime and
Justice, pages 1–19.
Joe Hoover, Gwenyth Portillo-Wightman, Leigh Yeh,
Shreya Havaldar, Aida Mostafazadeh Davani,
Ying Lin, Brendan Kennedy, Mohammad Atari,
Zahra Kamel, Madelyn Mendlen, et al. 2020.
Moral foundations twitter corpus: A collection
of 35k tweets annotated for moral sentiment.
Social Psychological and Personality Science,
11(8):1057–1071.
Dirk Hovy and Shrimai Prabhumoye. 2021. Five
sources of bias in natural language process-
ing.
Language and Linguistics Compass,
15(8):e12432.
Edward J. Hu, Yelong Shen, Phillip Wallis, Zeyuan
Allen-Zhu, Yuanzhi Li, Shean Wang, Lu Wang,
and Weizhu Chen. 2022. Lora: Low-rank adap-
tation of large language models. In ICLR. Open-
Review.net.
Albert Jiang, Alexandre Abou Chahine, Alexandre
Sablayrolles, Alexis Tacnet, Alodie Boissonnet,
Alok Kothari, Amélie Héliou, Andy Lo, Anna
Peronnin,
Antoine Meunier,
Antoine Roux,
Antonin Faure,
Aritra Paul,
Arthur Darcet,
Arthur Mensch, Audrey Herblin-Stoop, Augustin
Garreau, Austin Birky, Avinash Sooriyarachchi,
Baptiste
Rozière,
Barry
Conklin,
Bastien
Bouillon,
Blanche
Savary
de
Beauregard,
Carole Rambaud, Caroline Feldman, Charles
de Freminville, Charline Mauro, Chih-Kuan
Yeh, Chris Bamford, Clement Auguy, Corentin
Heintz,
Cyriaque Dubois,
Devendra Singh
Chaplot,
Diego Las Casas,
Diogo Costa,
Eléonore Arcelin, Emma Bou Hanna, Etienne
Metzger, Fanny Olivier Autran, Francois Lesage,
Garance Gourdel, Gaspard Blanchet, Gaspard
Donada Vidal, Gianna Maria Lengyel, Guillaume
Bour, Guillaume Lample, Gustave Denis, Harizo
Rajaona, Himanshu Jaju, Ian Mack, Ian Mathew,
Jean-Malo Delignon, Jeremy Facchetti, Jessica
Chudnovsky, Joachim Studnia, Justus Murke,
Kartik Khandelwal, Kenneth Chiu, Kevin Riera,
Leonard Blier,
Leonard Suslian,
Leonardo
Deschaseaux,
Louis Martin,
Louis Ternon,
Lucile Saulnier, Lélio Renard Lavaud, Sophia
Yang, Margaret Jennings, Marie Pellat, Marie
Torelli, Marjorie Janiewicz, Mathis Felardos,
Maxime Darrin, Michael Hoff, Mickaël Seznec,
Misha Jessel Kenyon, Nayef Derwiche, Nicolas
Carmont Zaragoza, Nicolas Faurie, Nicolas
Moreau, Nicolas Schuhl, Nikhil Raghuraman,
Niklas Muhs, Olivier de Garrigues, Patricia
Rozé, Patricia Wang, Patrick von Platen, Paul
Jacob, Pauline Buche, Pavankumar Reddy
Muddireddy, Perry Savas, Pierre Stock, Pravesh
Agrawal, Renaud de Peretti, Romain Sauvestre,
Romain Sinthe, Roman Soletskyi, Sagar Vaze,
Sandeep Subramanian, Saurabh Garg, Soham
Ghosh, Sylvain Regnier, Szymon Antoniak,
Teven Le Scao, Theophile Gervet, Thibault
Schueller,
Thibaut
Lavril,
Thomas
Wang,
Timothée
Lacroix,
Valeriia
Nemychnikova,
Wendy Shang, William El Sayed, and William
Marshall. 2024.
Ministral-8b-instruct-2410.
https://huggingface.co/mistralai/
Ministral-8B-Instruct-2410. Mistral AI
model release; accessed October 2025.
Brendan Kennedy, Ashwini Ashokkumar, Ryan L
Boyd, and Morteza Dehghani. 2022a. Text anal-
ysis for psychology: Methods, principles, and
practices. Handbook of Language Analysis in
Psychology.
Brendan
Kennedy,
Mohammad
Atari,
Aida Mostafazadeh Davani, Leigh Yeh, Ali
Omrani, Yehsong Kim, Kris Coombs, Shreya
Havaldar, Gwenyth Portillo-Wightman, Elaine
Gonzalez, et al. 2022b.
Introducing the gab
hate corpus: defining and applying hate-based
rhetoric to social media posts at scale. Language
Resources and Evaluation, 56(1):79–108.
Brendan Kennedy, Preni Golazizian, Jackson
Trager, Mohammad Atari, Joe Hoover, Aida
Mostafazadeh Davani, and Morteza Dehghani.
2023.
The (moral) language of hate.
PNAS
nexus, 2(7):pgad210.

--- Page 12 ---

Blair Kidwell, Adam Farmer, and David M Hardesty.
2013. Getting liberals and conservatives to go
green: Political ideology and congruent appeals.
Journal of Consumer Research, 40(2):350–367.
Srijan Kumar, William L Hamilton, Jure Leskovec,
and Dan Jurafsky. 2018. Community interaction
and conflict on the web. In Proceedings of the
2018 world wide web conference, pages 933–
943.
Alex Gwo Jen Lan and Ivandré Paraboni. 2022.
Text-and author-dependent moral foundations
classification. New Review of Hypermedia and
Multimedia, pages 1–21.
Morgan Marietta. 2008. From my cold, dead hands:
Democratic consequences of sacred rhetoric.
The Journal of Politics, 70(3):767–779.
Salma Moaz. 2020.
Using Moral Foundations
Framing to Influence Partisan Attitudes Toward
Latino Immigrants. Ph.D. thesis, Loyola Univer-
sity Chicago.
Dena F Mujtaba and Nihar R Mahapatra. 2019. Eth-
ical considerations in ai-based recruitment. In
2019 IEEE International Symposium on Technol-
ogy and Society (ISTAS), pages 1–7. IEEE.
Ece Çiğdem Mutlu, Toktam Oghaz, Ege Tütüncüler,
Jasser Jasser, and Ivan Garibay. 2020. Quantify-
ing latent moral foundations in twitter narratives:
The case of the syrian white helmets misinforma-
tion. arXiv preprint arXiv:2004.13142.
Vinodkumar Prabhakaran, Aida Mostafazadeh Da-
vani, and Mark Diaz. 2021.
On releasing
annotator-level labels and information in datasets.
arXiv preprint arXiv:2110.05699.
Nicholas Proferes, Naiyan Jones, Sarah Gilbert,
Casey Fiesler, and Michael Zimmer. 2021. Study-
ing reddit: A systematic overview of disciplines,
approaches, methods, and ethics. Social Media+
Society, 7(2):20563051211019004.
Muhammad Reza Qorib, Geonsik Moon, and
Hwee Tou Ng. 2024. Are decoder-only language
models better than encoder-only language mod-
els in understanding word meaning? In Findings
of the Association for Computational Linguistics:
ACL 2024, pages 16339–16347, Bangkok, Thai-
land. Association for Computational Linguistics.
Aida Ramezani and Yang Xu. 2024. Moral associa-
tion graph: A cognitive model for moral inference.
In Proceedings of the Annual Meeting of the Cog-
nitive Science Society, volume 46.
Gabriel
Roccabruna,
Massimo
Rizzoli,
and
Giuseppe Riccardi. 2024. Will LLMs replace the
encoder-only models in temporal relation classifi-
cation? In Proceedings of the 2024 Conference
on Empirical Methods in Natural Language Pro-
cessing, pages 20402–20415, Miami, Florida,
USA. Association for Computational Linguistics.
Kevin Roose. 2021.
The gamestop reck-
oning was a long time coming.
Posted
28-January-2021,
The
New
York
Times,
www.nytimes.com/2021/01/28/technology/gamestop-
stock.html.
Alexander Ruch, Ari Decter-Frain, and Raghav Ba-
tra. 2022. Millions of co-purchases and reviews
reveal the spread of polarization and lifestyle
politics across online markets.
arXiv preprint
arXiv:2201.06556.
Julius Sim and Chris C Wright. 2005. The kappa
statistic in reliability studies: use, interpretation,
and sample size requirements. Physical therapy,
85(3):257–268.
Johanna Simfors and Rasmus Rudling. 2020. How
does the degree of anonymity affect our morals?:
A study examining behavioural changes in online
communication.
Ahmed Soliman, Jan Hafer, and Florian Lemmerich.
2019. A characterization of political communities
on reddit. In Proceedings of the 30th ACM con-
ference on hypertext and Social Media, pages
259–263.
Kate Starbird, Jim Maddock, Mania Orand, Peg
Achterman, and Robert M Mason. 2014. Ru-
mors, false flags, and digital vigilantes: Misinfor-
mation on twitter after the 2013 boston marathon
bombing. IConference 2014 proceedings.
Jackson Trager, Francielle Vargas, Diego Alves,
Matteo Guida,
Mikel K Ngueajio,
Ameeta
Agrawal, Flor Plaza-del Arco, Yalda Daryanai,
and Farzan Karimi-Malekabadi. 2025.
Mftcx-
plain: A multilingual benchmark dataset for eval-
uating the moral reasoning of llms through hate
speech multi-hop explanation.
arXiv preprint
arXiv:2506.19073.
Anthony Henry Triggs, Kristian Møller, and Christina
Neumayer. 2021.
Context collapse and
anonymity among queer reddit users. new media
& society, 23(1):5–21.
Grigorios Tsoumakas and Ioannis Katakis. 2007.
Multi-label classification: An overview. Interna-
tional Journal of Data Warehousing and Mining
(IJDWM), 3(3):1–13.
Upvoted Staff. 2021. Reddit’s 2020 year in review.
Posted 8-December-2020, Upvoted: The Offi-
cial Reddit Blog, www.redditinc.com/blog/reddits-
2020-year-in-review/.

--- Page 13 ---

Jan G Voelkel, Mashail Malik, Chrystal Redekopp,
and Robb Willer. 2022. Changing americans’
attitudes about immigration: Using moral framing
to bolster factual arguments. The ANNALS of
the American Academy of Political and Social
Science, 700(1):73–85.
Rong Wang and Wenlin Liu. 2021. Different path-
ways to identify moral framing from media con-
tent: A response to hopp and weber. Communi-
cation Monographs, 88(3):380–388.
Christopher Wolsko. 2017. Expanding the range of
environmental values: Political orientation, moral
foundations, and the common ingroup. Journal
of Environmental Psychology, 51:284–294.
Yuexin Wu and Xiaolei Huang. 2022. Unsupervised
reinforcement adaptation for class-imbalanced
text classification. In Proceedings of the 11th
Joint Conference on Lexical and Computational
Semantics, pages 311–322, Seattle, Washing-
ton. Association for Computational Linguistics.
Hiroaki Yamane, Yusuke Mori, and Tatsuya Harada.
2021. Humor meets morality: Joke generation
based on moral judgement. Information Process-
ing & Management, 58(3):102520.
Jieyu Zhao, Tianlu Wang, Mark Yatskar, Vicente
Ordonez, and Kai-Wei Chang. 2017. Men also
like shopping: Reducing gender bias amplifica-
tion using corpus-level constraints. arXiv preprint
arXiv:1707.09457.

```
