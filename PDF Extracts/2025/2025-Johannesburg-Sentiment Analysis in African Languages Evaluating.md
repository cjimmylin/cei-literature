---
title: "2025-Johannesburg-Sentiment Analysis in African Languages Evaluating - PDF Extract"
source_pdf: "2025-Johannesburg-Sentiment Analysis in African Languages Evaluating.pdf"
pages: 14
extracted_at: "2026-02-13T14:50:58.729573"
---

# PDF Extract: 2025-Johannesburg-Sentiment Analysis in African Languages Evaluating
**Source PDF:** 2025-Johannesburg-Sentiment Analysis in African Languages Evaluating.pdf
**Total Pages:** 14

---

## Content

```
--- Page 1 ---

Findings of the Association for Computational Linguistics: EMNLP 2023, pages 4124–4137
December 6-10, 2023 ©2023 Association for Computational Linguistics
Evaluating Emotion Arcs Across Languages:
Bridging the Global Divide in Sentiment Analysis
Daniela Teodorescu1,2∗and Saif M. Mohammad3
1MaiNLP, Center for Information and Language Processing, LMU Munich, Germany
2Department of Computing Science, University of Alberta
3National Research Council Canada
daniela@cis.uni-muenchen.de, saif.mohammad@nrc-cnrc.gc.ca
Abstract
Emotion arcs capture how an individual (or a
population) feels over time. They are widely
used in industry and research; however, there
is little work on evaluating the automatically
generated arcs. This is because of the diffi-
culty of establishing the true (gold) emotion
arc. Our work, for the first time, systemat-
ically and quantitatively evaluates automati-
cally generated emotion arcs. We also com-
pare two common ways of generating emo-
tion arcs: Machine-Learning (ML) models and
Lexicon-Only (LexO) methods. By running ex-
periments on 18 diverse datasets in 9 languages,
we show that despite being markedly poor at in-
stance level emotion classification, LexO meth-
ods are highly accurate at generating emotion
arcs when aggregating information from hun-
dreds of instances. We also show, through ex-
periments on six indigenous African languages,
as well as Arabic, and Spanish, that automatic
translations of English emotion lexicons can be
used to generate high-quality emotion arcs in
less-resource languages. This opens up avenues
for work on emotions in languages from around
the world; which is crucial for commerce, pub-
lic policy, and health research in service of
speakers often left behind. Code and resources:
https://github.com/dteodore/EmotionArcs
1
Introduction
Commercial applications as well as research
projects often benefit from accurately tracking the
emotions associated with an entity over time. Pub-
lic health researchers are interested in analyzing
social media posts to better understand population-
level well-being (Vishnubhotla and Mohammad,
2022), loneliness (Guntuku et al., 2019), depres-
sion (De Choudhury et al., 2013), etc. Government
Policy makers benefit from tracking public opin-
ion over time for developing effective interventions
and laws. For example, tracking sentiment towards
∗Work done while at the University of Alberta and intern-
ship with the National Research Council Canada.
health interventions such as mask mandates and
vaccine policies (Hu et al., 2021). Researchers in
Digital Humanities are interested in understand-
ing basic components of stories such as plot struc-
tures, how emotions are associated with compelling
characters, categorizing stories based on emotion
changes (Reagan et al., 2016), etc. In all of these
applications, the goal is to determine whether the
degree of a chosen emotion has remained steady,
increased, or decreased from one time step to the
next. The time steps of consideration may be days,
weeks, years, etc. This series of time step–emotion
value pairs, which can be represented as a time-
series graph, is often referred to as an emotion arc
(Mohammad, 2011; Reagan et al., 2016).
Automatic methods generate emotion arcs using:
• The text of interest where the individual sen-
tences (or instances) are temporally ordered;
possibly through available timestamps indicat-
ing when the instances were posted/uttered:
e.g., all the tweets relevant to (or mentioning)
a government policy along with their meta-
data that includes the date and time of posting.
• The emotion dimension/category of interest:
e.g., anxiety, anger, valence, arousal, etc.
• The time step granularity of interest (e.g.,
days, weeks, months etc.)
The arcs are generated through a two-step process:
• Apply emotion labels to units of text. Two
common approaches for labeling units of text
are: (1) The Lexicon-Only (LexO) Method: to
label words using emotion lexicons and (2)
The Machine-Learning (ML) Method: to label
whole sentences using supervised ML models
(with or without using emotion lexicons).
• Aggregate the information to compute time
step–emotion value scores; e.g., if using
the lexicon approach: for each time step,
compute the percentage of anger words in the
target text pertaining to each time step, and if
4124

--- Page 2 ---

using the ML approach: for each time step,
compute the percentage of angry sentences
for each time step.
Despite their wide-spread use in industry and
research, there is little work on evaluating the gen-
erated emotion arcs (in part due to the difficulty of
establishing the true (gold) emotion arc). This is
problematic because we should know how accurate
the generated emotion arcs are before drawing in-
ferences from them or deploying these systems in
applications. Further, different methods of generat-
ing emotion arcs (LexO or ML) have different char-
acteristics. For example, LexO methods are inter-
pretable, accessible, compute-friendly, and do not
require annotated data (especially for each domain
of application) (Mohammad, 2023, 2021; Öhman,
2021); whereas ML methods tend to consider con-
text and longer-range dependencies, making them
more accurate at labeling individual instances for
emotions. (Table 5 in Appendix A depicts the pros
and cons in more detail.) Thus, it is often assumed
that ML methods are markedly more accurate than
LexO methods for all tasks, including the creation
of emotion arcs. However, this assumption may be
false; and can only be tested for the task of gener-
ating emotion arcs when there is a mechanism to
evaluate the arcs.
A robust and simple setup for evaluating emo-
tion arcs also allows one to test different design
decisions in how the arcs are generated. For ex-
ample, we know little about how best to aggregate
information when using emotion lexicons; e.g., is it
better to use coarse or fine-grained lexicons, should
we ignore slightly emotional words, etc.
Work on emotions has largely focused on En-
glish, excluding the voices, cultures, and perspec-
tives of a majority of people from around the world.
Such an exclusion is not only detrimental to those
that are excluded, but also to the world as a whole.
For example, western-centric science that only
draws on data from western languages may falsely
claim certain universals about language, emotions,
and stories, that when tested on data from other cul-
tures does not hold true anymore. Thus, working
with more languages helps discover new paradigms
that represent the world better.
However, generating emotion arcs in most lan-
guages other than English is stymied by the lack
of emotion-labeled resources. Using translated la-
beled texts with ML methods is problematic (Mo-
hammad et al., 2016; Hogenboom et al., 2014).
However, for a number of NLP tasks, systems
have benefited from using translations of lexical
resources (from say English) into the target lan-
guage. Thus, high-accuracy LexO methods for
creating emotion arcs can open up avenues of work
in various languages using (manual or automatic)
translations of existing emotion lexicons.
Our work, for the first time, systematically and
quantitatively evaluates automatically generated
emotion arcs. We also compare the ML and LexO
methods for generating arcs. Note, that our aim is
not to build more accurate emotion classification
systems, but rather we apply existing methods to
evaluate emotion arcs generated across domains
and languages. We conducted experiments on 18
datasets in nine languages from diverse domains,
including: tweets, SMS messages, reviews, etc.
(Two English datasets from movie reviews, four
English datasets from SemEval 2014, six datasets
from SemEval 2018 (two each in English, Arabic,
and Spanish), and six African languages datasets
from SemEval 2023 (AfriSenti).)
Emotions can be characterized by various dimen-
sions and categories (e.g., valence, arousal, dom-
inance vs. anger, fear, joy, sadness). In this work
we explore the valence (or sentiment), and there-
fore generate valence (or sentiment) arcs.1 Our
work sets the foundation for future work which can
extend analyses to various emotion categories.
2
Related Work
Emotion arcs have commonly been created from
literary works and social media content. Alm and
Sproat (2005) were the first to automatically clas-
sify sentences from literary works for emotions
using a machine learning paradigm. Mohammad
(2011) was the first to create emotion arcs and anal-
yse the flow of emotions across the narrative in
various novels and books using emotion lexicons.
Kim et al. (2017) built on this work by creating
emotion arcs to determine emotion information for
various genres using the NRC Emotion Lexicon
(Mohammad and Turney, 2013).2 Reagan et al.
(2016) and Del Vecchio et al. (2018) clustered emo-
tion arcs and found evidence for six prototypical arc
shapes in stories. Hipson and Mohammad (2021)
1Terminology:
The positive–negative (or pleasure–
displeasure) dimension has long been a focus of study, espe-
cially in psychology. They refer to this dimension as valence.
However, early NLP work in the area made use of product
and movie review datasets, and referred to the dimension as
sentiment — a term that has stuck in subsequent NLP work.
2http://saifmohammad.com/WebPages/
NRC-Emotion-Lexicon.htm
4125

--- Page 3 ---

analysed emotion arcs for individual characters (in-
stead of the whole narrative) in movie dialogues.
Emotion arcs of literary works have been used to
better understand plot and character development
(Reagan et al., 2016; Kim et al., 2017; Hipson and
Mohammad, 2021); and also for assisting writers
develop and improve stories (Ashida et al., 2021;
Somasundaran et al., 2020).
Recently, Hipson and Mohammad (2021) in-
troduced how the patterns with which emotions
change over time — emotion dynamics — can be
inferred from text. Vishnubhotla and Mohammad
(2022) computed UEDs from tweets and analysed
how they have changed over the years. Teodorescu
et al. (2023b) studied emotional development in
children’s writing and found meaningful patterns
across age. In the public health domain, Teodor-
escu et al. (2023a) created emotion arcs for tweeters
who self-disclosed as having a mental health diag-
nosis (on Twitter). They found that certain emotion
dynamics patterns differed significantly between
tweeters with mental health conditions (e.g., at-
tention deficit hyperactivity disorder, depression,
bipolar) compared to the control group.
However, there is surprisingly little work on arc
evaluation. A key reason for this is that it is hard
to determine the true emotion arc of a story from
data annotation. One attempt to evaluate aspects
of an emotion arc can be seen in Bhyravajjula et al.
(2022). They asked one volunteer to read mini-
segments of a ‘The Lord of the Rings’ novel to
determine whether the protagonist’s circumstance
undergoes a positive or negative shift. They then de-
termined the extent to which the automatic method
captured the same shifts. Here we propose a sim-
pler alternative way to robustly evaluate automati-
cally generated emotion arcs on a wide variety of
domains and multiple languages.
3
Experimental Setup to Evaluate
Automatically Generated Emotion Arcs
We begin by describing the evaluation setup. This
is a key contribution of this work since no prior
work systematically evaluates automatically gener-
ated emotion arcs. We construct gold emotion arcs
from existing datasets where individual instances
are manually annotated for valence (sentiment).
Here, an instance could be a tweet, a sentence from
a customer review, a sentence from a personal blog,
etc. Depending on the dataset, manual annotations
for an instance may represent the emotion of a
speaker, or sentiment towards a product or entity.
For a pre-chosen bin size of say 100 instances per
bin, we compute the gold emotion score by taking
the average of the human-labeled emotion scores of
the instances in that bin (in-line with the commerce
and social media use cases discussed earlier). We
move the window forward by one instance, com-
pute the average in that bin, and so on. (Using
larger window sizes does not impact conclusions.)
We created text streams for the experiments in Sec-
tion 4 by ordering instances from a dataset by in-
creasing gold score before binning. This created
arcs with a more consistent emotion change rate
and we first explore results in this scenario. In
Section 7, we look at the impact of more dynamic
emotion changes (e.g., varying peak heights and
widths) on performance.
We automatically generate emotion arcs using
the LexO and ML methods discussed in the two
sections ahead. We standardized all arcs (aka z-
score normalization) so that the gold arcs are com-
parable to automatically generated arcs.3 Finally,
we evaluate the closeness of automatically gener-
ated emotion arcs with gold arcs using two met-
rics: linear correlation and Root Mean Squared
Error (RMSE). We use Spearman rank correlation
(Spearman, 1987) (range: -1 to 1). High correla-
tion implies greater fidelity: no matter what the
overall shape of the gold emotion arc, when it goes
up (or down), the predicted emotion arc also goes
up (or down).4 RMSE (range: 0–∞) is a measure
of the error between the true and predicted values.
It penalizes bigger errors more, and thus is sensi-
tive to outliers. Scores closer to 0 indicate better
predictions. In our experiments, the correlation
and RMSE scores are determined for thousands of
points between the predicted and gold arcs.5
Table 1 shows key details of the English instance-
labeled datasets. To determine whether using au-
tomatic translations of English lexicons into rela-
tively less-resource languages is a viable option, we
also experiment with instance-labeled datasets in
Arabic (Ar), Spanish (Es), Amharic (Am), Hausa
(Ha), Igbo (Ig), Kinyarwanda (Kr), Swahili (Sw),
and Yoruba (Yo). Just as the English set, these con-
tain original tweets (not translated) with emotion
3Subtract the mean from the score and divide by the stan-
dard deviation (arcs then have zero mean and unit variance).
4Different orderings of a given dataset produce different
shapes; however, the Spearman correlation between the auto-
matic and gold arcs for that dataset remains the same.
5For example, in a dataset with 3K instances, when using a
rolling window of bin size 300, the arc consists of 2700 points.
4126

--- Page 4 ---

Dataset
Source
Domain
Dimension
Label Type
# Instances
Movie Reviews Categorical
Socher et al. (2013)
movie
valence
categorical (0, 1)
11,272
Movie Reviews Continuous
Socher et al. (2013)
reviews
valence
continuous (0 to 1)
11,272
SemEval 2014
Rosenthal et al. (2014)
multiple∗
valence
categorical (-1, 0, 1)
multiple∗
SemEval 2018 (V-OC)
Mohammad et al. (2018)
tweets
valence
categorical (-3,-2,...3)
2,567
SemEval 2018 (V-Reg)
Mohammad et al. (2018)
tweets
valence
continuous (0 to 1)
2,567
Table 1: Key details of the English emotion-labeled datasets used. ∗The SemEval 2014 dataset is a collection of
18,611 instances, including LiveJournal posts (1141), SMS messages (2082), tweets (15302), sarcastic tweets (86).
Lexicon
Source
Categories / Dimensions
Label Type
# Terms
NRC VAD
Mohammad (2018)
valence, arousal, dominance
continuous (-1 to 1)
20,007
valence, arousal, dominance
categorical (-1, 0, 1)
20,007
Table 2: Lexicons used in this study. The subset of emotions explored in our experiments are marked in bold.
labels by native speakers. The datasets are of two
kinds: those with categorical labels such as the Se-
mEval 2014, which has -1 (negative), 0 (neutral),
and 1 (positive), as well as those with continuous
labels such as SemEval 2018 (V-Reg), which has
real-valued sentiment intensity scores between 0
(lowest/no intensity) and 1 (highest intensity).
In all, we conducted experiments with 18
emotion-labeled datasets from nine languages, with
labels that are either categorical or continuous, for
valence. The results also establish key benchmarks;
useful to practitioners for estimating the quality of
the arcs under various settings.
4
LexO Arcs: Emotion Arcs Generated
from Counting Emotion Words
Recall that in the Introduction we described how
emotion arcs are automatically generated. Key pa-
rameters in that process include bin size, type of
emotion lexicon used (e.g., categorical or contin-
uous emotion scores), and how to handle terms in
the text that are not in the lexicon (OOV terms).
Choice of bin size depends on the application
and available data. For example, if a company
wants to know how the proportion of angry com-
ments has changed from month to month in the
last 10 years, then the bin size to use is month. If
instead, they want to know how things changed on
a day-by-day basis over the last 45 days, then the
bin size to use is a day. Depending on the volume
of relevant data and the bin size chosen, the bins
may include a higher or lower number of instances.
For our experiments we explored various bin sizes
(1, 10, 30, 50, 100, 200, and 300).
Table 2 shows the English emotion lexicon we
used: The NRC VAD Lexicon.6 It has both cate-
gorical and real-valued versions, which is useful to
study whether using fine-grained lexicons leads to
6http://saifmohammad.com/WebPages/nrc-vad.html
markedly better emotion arcs.
The two OOV handling methods explored were:
1. Assign label NA (no score available) and disre-
gard these words, and 2. Assign 0 score (neutral
or not associated with emotion category), thereby,
leading to a lower average score for the instance
than if the word was disregarded completely.
We then evaluated how closely the arcs cor-
respond to the gold valence arcs. In Appendix
B, we show the impact of using emotion lexi-
cons more selectively—using only the entries that
have an emotion association greater than some pre-
determined threshold.
Results (Valence): Figure 1 shows the correlations
and RMSE values between predicted valence arcs
and the gold valence arcs.
Bin Size: Overall, across datasets and regardless
of the type of lexicon used and how OOV words
are handled, increasing the bin size dramatically
improves correlation with the gold arcs. In fact,
with bin sizes as small as 50, many of the generated
arcs have correlations above 0.9. With bin size
100 and above correlations approach high 0.90’s.
Similarly, RMSE starts at approximately 1.20 to
1.10 at bin size 1, and quickly drops as bin size
increases. At bin size 300, RMSE approaches quite
low scores (0.3–0.1).
If we use a bin size of 1, we only get the ups and
downs of the emotions associated with individual
words, which will likely be quite far off from the
true emotion arc. As bin size increases (more data
per bin), the predicted arc gets closer to the true
arc probably because:
If bin x is expressing more of an
emotion
(higher
emotion
intensity)
than bin y, then x has a higher average
word–emotion association score than y.
Categorical vs. Real-Valued Lexicons: Using a real-
valued lexicon obtains higher correlations across
bin sizes, methods for processing OOV terms, and
4127

--- Page 5 ---

Figure 1: Valence Arcs: Spearman correlation and RMSE values between LexO and gold arcs of English datasets.
datasets. The difference is marked for very small
bin sizes (such as 1 and 10) but progressively
smaller for higher bin sizes. Entries from real-
valued lexicons carry more fine-grained emotion
information, and it is likely that this extra informa-
tion is especially helpful when arcs are determined
from very little text (as in the case of small bins).
OOV Terms: Results with the two OOV-handling
methods were comparable (no clear winner).
Discussion: For many social media applications,
one has access to tens of thousands, if not millions
of posts. There, it is not uncommon to have time-
steps (bins) that include thousands of instances.
Thus, it is remarkable that even with relatively
small bin sizes of a few hundred, the simple lexicon
approach is able to obtain very high correlations.
Of course, the point is not that the lexicon approach
is somehow special, but rather that aggregation of
information can very quickly generate high qual-
ity arcs, even if the constituent individual emotion
signals are somewhat weak.
5
ML Arcs: Emotion Arcs Generated
from Counting ML-Labeled Sentences
This section explores how the accuracy of instance-
level (sentence- or tweet-level) emotion labeling
impacts the quality of the generated emotion arcs.
We approached this by creating an ‘oracle’ sys-
tem, which has access to the gold instance emotion
labels.
There are several metrics for evaluating senti-
ment analysis at the instance level such as accuracy,
correlation, or F-score. However, we focus on ac-
curacy as it is a simple intuitive metric. Inputs to
the Oracle system are a dataset of text (for emotion
labelling) and a level of accuracy (e.g., 90% accu-
racy) to perform instance-level emotion labelling at.
Then, the system goes through each instance and
predicts the correct emotion label with a probability
corresponding to the pre-chosen accuracy. In the
case where the system decides to assign an incor-
rect label, it chooses one of the possible incorrect
labels at random.
4128

--- Page 6 ---

Figure 2: Valence Arcs: Spearman correlations of the arcs generated using the valence-classification Oracle System
(OS) with the gold arcs of English tweets. OS (Accuracy): Accuracy at instance-level sentiment classification.
Source
Model
Instance-Level
Bin Size
Accuracy
1
10
50
100
200
300
Socher et al. (2013)
RNTN
85.4%
0.829
0.972
0.980
0.983
0.986
0.992
Devlin et al. (2019)
BERT-base
93.5%
0.921
0.981
0.984
0.988
0.993
0.996
Devlin et al. (2019)
BERT-large
94.9%
0.932
0.986
0.984
0.988
0.993
0.996
Yang et al. (2019)
XLNet
97.0%
0.959
0.990
0.985
0.988
0.993
0.996
Liu et al. (2019)
RoBERTa
96.4%
0.958
0.989
0.986
0.989
0.994
0.997
Table 3: Valence Arcs: Spearman correlations between arcs generated using neural models for instance-level
sentiment classification and gold arcs of English tweet streams.
We use the Oracle to generate emotion labels
pertaining to various levels of accuracy, for the
same dataset. We then generate emotion arcs just
as described in the previous section (by taking the
average of the scores for each instance in a bin),
and evaluate the generated arcs just as before (by
determining correlation with the gold arc). This
Oracle System allows us to see how accurate an in-
stance level emotion labelling approach needs to be
to obtain various levels of quality when generating
emotion arcs.
Figure 2 shows the correlations of the valence
arcs generated using the Oracle System with the
gold valence arcs created from the SemEval 2018 V-
OC test set (that has 7 possible labels: -3 to 3).7 We
observe that, as expected the Oracle Systems with
instance-level accuracy greater than approximately
the random baseline (14.3% for this dataset) obtain
positive correlations; whereas those with less than
14% accuracy obtain negative correlations. As seen
with the results of the previous section, correlations
increase markedly with increase in bin size. Even
with an instance-level accuracy of 60%, correlation
approaches 1 at larger bin sizes. Overall, we again
observe high quality emotion arcs with bin sizes of
just a few hundred instances.
Table 3 shows the correlations obtained on the
same dataset when using various deep neural net-
work and transformer-based systems. Observe that
the recent systems obtain nearly perfect correlation
7Figure 5 (Appendix) shows similar Oracle System results
for other datasets.
at bin sizes 200 and 300. However, for a given
application scenario, these results can only be ob-
tained when the machine learning system is able
to train on sufficient domain-specific training data
(which is often scarce), the computer power, and
knowledge to work with these systems is accessi-
ble. For applications where simple, interpretable,
low-cost, and low-carbon-footprint systems are de-
sired, the lexicon-based systems described in the
previous section, are often more suitable.
6
LexO Arcs: Emotion Arcs Generated
from Translated Emotion Lexicons
Given the competitive performance of the Lexicon-
Only (LexO) method, and the many benefits of the
LexO method such as their simplicity and inter-
pretability, we now explore whether high-quality
emotion arcs can be created for low-resourced
languages using automatic translations of English
emotion lexicons. Specifically, we make use of
translations of the NRC lexicons from English into
the language of interest and perform similar exper-
iments as described in the previous section.8 We
explore bin sizes of 400 and 500 as well, as we
expect that instance-level accuracy will be lower in
the translated-lexicon case.
We would like to note that automatic translations
may not be available for many very low resource
languages. Currently, Google Translate has func-
tionality to translate across about 120 languages.
8The NRC Emotion and VAD Lexicon packages come
with translations into over 100 languages.
4129

--- Page 7 ---

Language
Source
Domain
Dimension
Label Type
# Instances
Amharic
Yimam et al. (2020)
tweets
valence
categorical (-1, 0, 1)
5,984
Hausa
Muhammad et al. (2022)
tweets
valence
categorical (-1, 0, 1)
14,172
Igbo
Muhammad et al. (2022)
tweets
valence
categorical (-1, 0, 1)
10,192
Kinyarwanda
Muhammad et al. (2023)
tweets
valence
categorical (-1, 0, 1)
3,302
Swahili
Muhammad et al. (2023)
tweets
valence
categorical (-1, 0, 1)
1,810
Yoruba
Muhammad et al. (2022)
tweets
valence
categorical (-1, 0, 1)
8,522
Table 4: Key information pertaining to the African language emotion-labeled tweets datasets we use in our
experiments. The No. of instances includes the train set for the SemEval 2023 Task 12.
This may seem large (and it is indeed a massive im-
provement from just a decade back), but thousands
of languages still remain on the other side of the
digital divide. Thus, even requiring word transla-
tions is a significant limitation for many languages.
We generated and evaluated emotion arcs in six
African languages: Amharic, Hausa, Igbo, Kin-
yarwanda, Swahili, and Yoruba (using the datasets
shown in Table 4). These are some of the most
widely spoken indigenous African languages.9 Ta-
ble 6 in the Appendix presents details about each,
including their language family and the primary
regions where they are spoken. Note that these
languages themselves are diverse covering three
different language families: Afroasiatic, Bantu,
and Niger-Congo. Swahili, is more influenced by
the Indo-European languages than Hausa —about
40% of its vocabulary is made up of Arabic loan
words. We contrast results on these languages to
Arabic, a commonly spoken language in North-
ern Africa which has somewhat more resources
than indigenous African languages. Arabic still
has much fewer NLP resources than English. We
also contrast our results to Spanish, which has
fewer resources than English; and is more similar
to English than Arabic. (The Ar and Es valence-
labeled datasets used are shown in Table 7 in the
Appendix.) High fidelity of the predicted arcs with
the gold arcs will unlock the potential for research
in affect-related psychology, health science, and
digital humanities for a vast number of languages.
6.1
Valence Arcs: Using Translated Lexicons
We ran a wide range of experiments in Arabic,
Spanish, and the African languages with all the pa-
rameter variations discussed earlier. We found the
same trends for the OOV handling and lexicon gran-
ularity parameters for these languages as for En-
glish. Therefore, for brevity, Figure 3 only shows
the results with using real-valued lexicons (which
performed better than categorical score lexicons)
9https://www.pangea.global/blog/2018/07/19/
10-most-popular-african-languages/
and assign label NA to OOV words (which was
comparable to the ‘assign neutral score’ method).
Figure 3 shows the results for generating emotion
arcs using translations of English lexicons into
Arabic, Spanish, and the African languages for
both categorically (e.g., V-OC and SemEval 2023)
and continuously (e.g., V-Reg) labelled valence
datasets. We also provide the English results on the
corresponding datasets for easy comparison.
For Arabic and Spanish (V-OC and V-Reg
datasets): Correlations start at 0.40–0.50 at the
instance-level (bin size 1), and reach 0.98–0.99
from bin sizes 200 and onwards. Performance us-
ing translations of English lexicons does surpris-
ingly well. At bin size 1 English does performs
better by about 10 points, however this difference
quickly dissipates at bin size 50 and onwards.
For the African language texts (the SemEval
2023 datasets): Correlations start at lower values
at the instance-level, than for Arabic and Spanish.
At bin size 1, correlations are about 0.1–0.2
with the exception of Hausa at 0.374. As seen
previously, with increasing bin size we are able
to gain substantial improvements in performance
by aggregating information. With a bin size of
200 and onwards correlations reach mid 0.90’s
which is a large gain in performance compared
to instance-level. Among the African languages,
at bin size 1–50 arcs for Hausa are by far the
best, followed by arcs for Amharic; then arcs
for Igbo, Kinyarwanda, and Swahili perform
similarly; followed by Yoruba.
For bin sizes
100 and onwards,
Hausa and Kinyarwanda
become the best performing, followed by Igbo and
Amharic performing similarly, followed by Yoruba.
Discussion: Using translations of English lexicons
allows us to create high-quality emotion arcs in
African languages. The variation in performance
across the African languages could be because of
the variation in quality of automatic translations of
the emotion lexicons across languages and different
inter-annotator agreements for the instance-level
emotion labels in the different datasets.
4130

--- Page 8 ---

Figure 3: Valence Arcs: Spearman correlations between arcs generated using translated emotion lexicons and gold
arcs created from categorically and continuously labeled test data in Arabic, Spanish, and the African languages.
The untranslated English results are shown for comparison.
Although the results for Arabic and the African
languages are on different datasets, it is of inter-
est to contrast the performance of Arabic to the
African languages because Google’s translations of
words in the lexicon to Arabic is expected to be of
higher quality than to the African languages (due
to the relatively higher amounts of English–Arabic
parallel text). Overall, it is interesting to note that
the translation method creates relatively better arcs
when the target language is closer to the source lan-
guage (e.g., English to Spanish). However, even for
distant languages, performance can be improved by
increasing bin size (e.g., some African languages).
Of course, increasing bin size means lower gran-
ularity, but in many application scenarios, and for
drawing broad trends, it makes sense to aggregate
hundreds or thousands of instances in each bin,
leading to more reliable inferences about emotion
trends over time.
7
Arc Quality under Varying Emotion
Amplitudes and Spikiness
Aspects of how emotions change across the bins
also impacts the quality of generated arcs. For ex-
ample, for a given surge or dip of emotion, if the
change of emotion strength is too small in magni-
tude (small amplitude) or occurs for too short of
a time period (high spikiness), then the automatic
method may fail to register the surge/dip. We will
refer to arcs with many such emotion changes as
more dynamic than those with more gradual and
longer-duration emotion changes.
Recall that in Section 4 we used text streams
ordered by increasing gold score. Now, to test the
robustness of the LexO method, when dealing with
dynamic emotion changes, we created new text
streams by reordering the tweets in the emotion-
labeled datasets in more random and dramatic ways.
We created these dynamic text streams by sampling
tweets from the chosen dataset with replacement
until 200 crests and 200 troughs of various ampli-
tudes and spikiness were obtained.10 The gold arc
is then standardized as before. We will refer to
this new text stream generated from a dataset as
[dataset_name]-dynamic, and the gold arcs created
with this process as dynamic gold arcs.
The gold line in Figure 4 shows the beginning
portion of the gold valence arc produced from the
SemEval 2018 (V-Reg) dataset (bin size = 100).
Observe that some peaks are rather small in am-
plitude whereas some others are greater than two
standard deviations. Also, some emotion changes
occur across a wider span of data (x-axis) whereas
some others show large emotion change and back
in a short span.
We then generated the predicted arc for this
dataset using the LexO method, the NRC VAD
lexicon, and by ignoring terms not found in the
lexicon when determining bin scores. The green
line in Figure 4 shows the beginning portion of the
gold valence arc when using a rolling window with
bin size 100. Observe that the green line traces
the gold line quite closely. There are also occa-
sions where it overshoots or fails to reach the gold
arc. Figure 4 shows gold and predicted arcs for the
Hausa dataset (bin size = 300). Observe that here
10Sampling with replacement allowed reuse of the limited
labeled data to produce a long wave.
4131

--- Page 9 ---

Figure 4: Dynamic and predicted arcs for English (a) and Hausa (b) using the LexO method.
the predicted arc still follows the gold arc closely
(but as expected, not as closely as a.)
In experiments modifying bin size, the predicted
arcs obtain a high correlation (above 0.9) with a bin
size of 100 (and above), even for the dynamic text
stream. However, these scores are (as expected)
consistently lower than what were observed for the
corresponding non-dynamic text stream. Note that
the difference in scores is more pronounced for the
smaller bin sizes than for larger ones. Therefore,
in scenarios with smaller amounts of data per bin,
judicious use of parameters described in Section 4
(e.g., treating OOVs as neutrals, using real-valued
lexicons, etc.) can have marked influence on arc
quality. Overall, though, these results show that the
LexO method performs rather well even in the case
of highly dynamic emotion changes.
8
Concluding Remarks
This work made contributions in two broad di-
rections: First, we showed how methods for pre-
dicting emotion arcs can be evaluated, and used
it to systematically and quantitatively evaluate
both Lexicon-Only and Machine Learning meth-
ods. Second, we showed that using translations
of English lexicons into the language of interest
can generate high quality emotion arcs, even for
languages that are very different from English.
Both ML and LexO methods produced high-
quality emotion arcs when using bin size 50 and
above (e.g., with bin size 100: obtaining correla-
tions with gold valence arcs exceeding 0.98). ML
methods are able to obtain markedly higher cor-
relations at very low bin sizes (<50). However,
with the abundance of textual data available from
social media, for many applications where one is
aggregating hundreds or thousands of instances in
each bin, the gains of ML methods in terms of
correlation scores are miniscule.
With the cross-lingual experiments, we created
emotion arcs from texts in six indigenous African
languages, as well as Arabic and Spanish. For all
of them, emotion arcs obtained high correlations as
the bin size (aggregation level) was set to at least a
few hundred instances. Correlations between pre-
dicted and gold emotion arcs were in general higher
when the target language was closer to English.
In the last part of the paper, we explored how
depending on the data available and the desired
granularity of emotion arcs interacts with perfor-
mance for various arc amplitudes and arc spikiness.
We showed that the LexO method performs rather
well even in the case of highly dynamic emotion
changes. However, for smaller bin sizes, the pre-
dicted arc may markedly overshoot or not fully
capture the gold peak or trough.
In all, we conducted experiments with 18 senti-
ment-labeled datasets from 9 languages, Thus the
conclusions drawn are rather robust. The results on
individual datasets also establish key benchmarks;
useful to practitioners for estimating the quality of
the arcs under various settings. Finally, since this
work shows that simple lexicon-only approaches
produce accurate arcs, practitioners from all fields,
those working in low-resource languages, those
interested in interpretability, or those without the
resources to deploy neural models, can easily gen-
erate high-quality emotion arcs for their data.
4132

--- Page 10 ---

9
Limitations
It is challenging to determine the true emotion
arc of a text stream or story through data anno-
tation. This is because usually data annotation is
performed on smaller pieces of text such as sen-
tences or paragraphs. It is difficult for people to
read a large body of text, say from a novel, and
produce consistent annotations for how emotions
have changed as the text has progressed from start
to finish. In the context of tweets, taking the av-
erage emotion scores of individual sentences is a
reasonable option (as we have done here); however,
that may not capture true emotions when dealing
with large pieces of text written by the same person,
for example, emotion arcs of stories in a novel. We
hope future work will determine how to create gold
arcs in such cases, and how different such arcs are
from the arcs created by averaging the scores of
individual sentences.
Constructing emotion lexicons from human
annotations of emotion scores takes time and
resources. Thus, these resources exist only for a
handful of languages. As a feasible approach in
the meanwhile, we uses automatic translations
of emotion lexicons from English to a desired
target language to generate emotion arcs in
various languages. While this approach produces
highly accurate emotion arcs, there are several
considerations: different languages and cultures
express emotions differently, there may be lexical
gaps among languages, and characteristics and
meaning can be lost in the translation. Therefore,
one would expect that using human annotated
lexicons would lead to higher emotion arc quality.
10
Ethics
Our research interest is to study emotions at an
aggregate/group level. This has applications in de-
termining public policy (e.g., pandemic-response
initiatives) and commerce (understanding attitudes
towards products). However, emotions are com-
plex, private, and central to an individual’s experi-
ence. Additionally, each individual expresses emo-
tion differently through language, which results in
large amounts of variation. Therefore, several eth-
ical considerations should be accounted for when
performing any textual analysis of emotions (Mo-
hammad, 2022, 2020). The ones we would particu-
larly like to highlight are listed below:
• Our work on studying emotion word usage
should not be construed as detecting how peo-
ple feel; rather, we draw inferences on the
emotions that are conveyed by users via the
language that they use.
• The language used in an utterance may con-
vey information about the emotional state (or
perceived emotional state) of the speaker, lis-
tener, or someone mentioned in the utterance.
However, it is not sufficient for accurately de-
termining any of their momentary emotional
states. Deciphering the true momentary emo-
tional state of an individual requires extra-
linguistic context and world knowledge. Even
then, one can be easily mistaken.
• The inferences we draw in this paper are based
on aggregate trends across large populations.
We do not draw conclusions about specific
individuals or momentary emotional states.
Acknowledgments
Thank you to Krishnapriya Vishnubhotla for the
Emotion Dynamics code-base, which set the
ground work for computing instance average emo-
tion scores for instances. This research was sup-
ported by NSERC, Digital Research Alliance of
Canada (alliancecan.ca), Alberta Innovates, and
DeepMind. This research project is funded by the
Bavarian Research Institute for Digital Transforma-
tion (bidt), an institute of the Bavarian Academy of
Sciences and Humanities. The author is responsi-
ble for the content of this publication.
References
Cecilia Ovesdotter Alm and Richard Sproat. 2005. Emo-
tional sequencing and development in fairy tales. In
Proceedings of the First International Conference
on Affective Computing and Intelligent Interaction,
ACII’05, page 668–674, Berlin, Heidelberg. Springer-
Verlag.
Atsushi Ashida, Masataka Tokumaru, and Tomoko Ko-
jiri. 2021. Characters’ emotion design support sys-
tem for writing novels based on story arcs of target
readers. Information and Technology in Education
and Learning, 1:Reg–p005.
Sriharsh Bhyravajjula, Ujwal Narayan, and Manish Shri-
vastava. 2022. Marcus: An event-centric nlp pipeline
that generates character arcs from narratives.
In
Text2Story@ECIR.
4133

--- Page 11 ---

Munmun De Choudhury, Michael Gamon, Scott Counts,
and Eric Horvitz. 2013. Predicting depression via so-
cial media. In Seventh international AAAI conference
on weblogs and social media, pages 128–137.
Marco Del Vecchio, Alexander Kharlamov, Glenn Parry,
and Ganna Pogrebna. 2018. The Data Science of Hol-
lywood: Using Emotional Arcs of Movies to Drive
Business Model Innovation in Entertainment Indus-
tries. arXiv e-prints, page arXiv:1807.02221.
Jacob Devlin, Ming-Wei Chang, Kenton Lee, and
Kristina Toutanova. 2019. BERT: Pre-training of
deep bidirectional transformers for language under-
standing. In Proceedings of the 2019 Conference of
the North American Chapter of the Association for
Computational Linguistics: Human Language Tech-
nologies, Volume 1 (Long and Short Papers), pages
4171–4186, Minneapolis, Minnesota. Association for
Computational Linguistics.
Sharath Chandra Guntuku, Rachelle Schneider, Arthur
Pelullo, Jami Young, Vivien Wong, Lyle Ungar,
Daniel Polsky, Kevin G Volpp, and Raina Merchant.
2019. Studying expressions of loneliness in individu-
als using Twitter: an observational study. BMJ open,
9(11):e030355.
Will E. Hipson and Saif M. Mohammad. 2021. Emotion
dynamics in movie dialogues. PLOS ONE, 16(9):1–
19.
Alexander Hogenboom, Bas Heerschop, Flavius Fras-
incar, Uzay Kaymak, and Franciska de Jong. 2014.
Multi-lingual support for lexicon-based sentiment
analysis guided by semantics. Decision Support Sys-
tems, 62:43–53.
Tao Hu, Siqin Wang, Wei Luo, Mengxi Zhang, Xiao
Huang, Yingwei Yan, Regina Liu, Kelly Ly, Viraj
Kacker, Bing She, et al. 2021. Revealing public opin-
ion towards covid-19 vaccines with twitter data in the
united states: spatiotemporal perspective. Journal of
Medical Internet Research, 23(9):e30854.
Evgeny Kim, Sebastian Padó, and Roman Klinger. 2017.
Investigating the relationship between literary genres
and emotional plot development. In Proceedings
of the Joint SIGHUM Workshop on Computational
Linguistics for Cultural Heritage, Social Sciences,
Humanities and Literature, pages 17–26, Vancouver,
Canada. Association for Computational Linguistics.
Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Man-
dar Joshi, Danqi Chen, Omer Levy, Mike Lewis,
Luke Zettlemoyer, and Veselin Stoyanov. 2019.
RoBERTa: A robustly optimized BERT pretraining
approach.
Saif Mohammad. 2011.
From once upon a time to
happily ever after: Tracking emotions in novels and
fairy tales. In Proceedings of the 5th ACL-HLT Work-
shop on Language Technology for Cultural Heritage,
Social Sciences, and Humanities, pages 105–114,
Portland, OR, USA. Association for Computational
Linguistics.
Saif Mohammad. 2023. Best practices in the creation
and use of emotion lexicons. In Findings of the Asso-
ciation for Computational Linguistics: EACL 2023,
pages 1825–1836, Dubrovnik, Croatia. Association
for Computational Linguistics.
Saif M. Mohammad. 2018. Obtaining reliable human
ratings of valence, arousal, and dominance for 20,000
english words. In Proceedings of The Annual Confer-
ence of the Association for Computational Linguistics
(ACL), Melbourne, Australia.
Saif M. Mohammad. 2020. Practical and ethical consid-
erations in the effective use of emotion and sentiment
lexicons.
Saif M. Mohammad. 2021. Sentiment analysis: Au-
tomatically detecting valence, emotions, and other
affectual states from text. In Herb Meiselman, editor,
Emotion Measurement (Second Edition). Elsevier.
Saif M. Mohammad. 2022. Ethics sheet for automatic
emotion recognition and sentiment analysis. To Ap-
pear in Computational Linguistics.
Saif M. Mohammad, Felipe Bravo-Marquez, Mo-
hammad Salameh, and Svetlana Kiritchenko. 2018.
Semeval-2018 Task 1: Affect in tweets. In Proceed-
ings of International Workshop on Semantic Evalua-
tion (SemEval-2018), New Orleans, LA, USA.
Saif M. Mohammad, Mohammad Salameh, and Svet-
lana Kiritchenko. 2016. How translation alters senti-
ment. J. Artif. Int. Res., 55(1):95–130.
Saif M. Mohammad and Peter D. Turney. 2013. Crowd-
sourcing a word-emotion association lexicon. Com-
putational Intelligence, 29(3):436–465.
Shamsuddeen Muhammad, Seid Yimam, Idris Ab-
dulmumin, Ibrahim Ahmad, David Adelani, Se-
bastian Ruder, Nedjma Ousidhoum, Saminu Aliyu,
Abinew Ayele, Meriem Beloucif, Bello Bello, and
Saif M. Mohammad. 2023. SemEval 2023 task 12:
Sentiment analysis for african languages (afrisenti-
semeval). In Proceedings of the 17th International
Workshop on Semantic Evaluation (SemEval-2023),
Toronto, Canada.
Shamsuddeen Hassan Muhammad, David Adelani, Se-
bastian Ruder, Ibrahim Sa’id Ahmad, Idris Abdul-
mumin, Shehu Bello Bello, Monojit Choudhury,
Chris Chinenye Emezue, Saheed Salahuddeen Abdul-
lahi, Anuoluwapo Aremu, Alipio Jeorge, and Pavel
Brazdil. 2022. Naijasenti: A nigerian twitter senti-
ment corpus for multilingual sentiment analysis. In
Proceedings of the 13th Language Resources and
Evaluation Conference, pages 590–602, Marseille,
France. European Language Resources Association.
Emily Öhman. 2021. The validity of lexicon-based
sentiment analysis in interdisciplinary research. In
Proceedings of the Workshop on Natural Language
Processing for Digital Humanities, pages 7–12, NIT
Silchar, India. NLP Association of India (NLPAI).
4134

--- Page 12 ---

Andrew J. Reagan, Lewis Mitchell, Dilan Kiley, Christo-
pher M. Danforth, and Peter S. Dodds. 2016. The
emotional arcs of stories are dominated by six basic
shapes. EPJ Data Science, 5(1):1–12. Copyright -
EPJ Data Science is a copyright of Springer, 2016;
Last updated - 2017-02-06.
Sara Rosenthal, Alan Ritter, Preslav Nakov, and Veselin
Stoyanov. 2014. SemEval-2014 task 9: Sentiment
analysis in Twitter. In Proceedings of the 8th Interna-
tional Workshop on Semantic Evaluation (SemEval
2014), pages 73–80, Dublin, Ireland. Association for
Computational Linguistics.
Richard Socher, Alex Perelygin, Jean Wu, Jason
Chuang, Christopher D. Manning, Andrew Ng, and
Christopher Potts. 2013. Recursive deep models for
semantic compositionality over a sentiment treebank.
In Proceedings of the 2013 Conference on Empiri-
cal Methods in Natural Language Processing, pages
1631–1642, Seattle, Washington, USA. Association
for Computational Linguistics.
Swapna Somasundaran, Xianyang Chen, and Michael
Flor. 2020. Emotion arcs of student narratives. In
Proceedings of the First Joint Workshop on Narra-
tive Understanding, Storylines, and Events, pages
97–107, Online. Association for Computational Lin-
guistics.
Charles Spearman. 1987. The proof and measurement
of association between two things. The American
journal of psychology, 100(3/4):441–471.
Daniela Teodorescu, Tiffany Cheng, Alona Fyshe, and
Saif M. Mohammad. 2023a. Language and mental
health: Measures of emotion dynamics from text as
linguistic biosocial markers. In The 2023 Conference
on Empirical Methods in Natural Language Process-
ing.
Daniela Teodorescu, Alona Fyshe, and Saif Mohammad.
2023b. Utterance emotion dynamics in children’s po-
ems: Emotional changes across age. In Proceedings
of the 13th Workshop on Computational Approaches
to Subjectivity, Sentiment, & Social Media Analysis,
pages 401–415, Toronto, Canada. Association for
Computational Linguistics.
Krishnapriya Vishnubhotla and Saif M. Mohammad.
2022. Tweet emotion dynamics: Emotion word us-
age in tweets from us and canada. In Proceedings of
the Thirteenth International Conference on Language
Resources and Evaluation (LREC 2022), Marseille,
France.
Zhilin Yang, Zihang Dai, Yiming Yang, Jaime Car-
bonell, Russ R Salakhutdinov, and Quoc V Le. 2019.
Xlnet: Generalized autoregressive pretraining for lan-
guage understanding. In Advances in Neural Infor-
mation Processing Systems, volume 32. Curran Asso-
ciates, Inc.
Seid Muhie Yimam, Hizkiel Mitiku Alemayehu,
Abinew Ayele, and Chris Biemann. 2020. Exploring
Amharic sentiment analysis from social media texts:
Building annotation tools and classification mod-
els. In Proceedings of the 28th International Con-
ference on Computational Linguistics, pages 1048–
1060, Barcelona, Spain (Online). International Com-
mittee on Computational Linguistics.
APPENDIX
A
LexO vs. ML Methods for Emotion
Labelling
In Table 5 we show the characteristics of the
Lexicon-Only (LexO) and Machine Learning (ML)
based methods for emotion labelling instances.
B
Impact of Selectively Using the Lexicon
The continuously labeled emotion lexicons include
words that may be very mildly associated with an
emotion category or dimension. It is possible that
the very low emotion association entries may in
fact mislead the system, resulting in poor emotion
arcs. We therefore also investigated the quality of
emotion arcs by generating them only from terms
with an emotion association score greater than a
pre-chosen threshold; thereby using the lexicon en-
tries more selectively. We systematically varied the
threshold to study what patterns of threshold lead
to better arcs across the emotion test datasets.11
Overall, we observed that valence benefits from
including all terms, even lowly associated emotion
words, as the optimal threshold across continuous
and categorically datasets is 0 with a few notable
exceptions (SemEval 2014 LiveJournal, SemEval
2014 tweets, and V-OC). Generally, including only
terms with emotion scores above 0.33 to 0.5 im-
proves the quality of emotion arcs.
C
Impact of the Quality of Instance-Level
Emotion Labeling on Emotion Arcs
Figure 5 shows the results for the Oracle System
on the categorically labeled SemEval 2014 datasets.
We observe similar patterns as discussed in the pa-
per for the SemEval 2018 V-OC dataset. (Note
that the instance-level random-guess baseline is de-
pendent on the number of class labels; thus, the
minimum Oracle System Accuracy at which posi-
tive correlations with gold arcs appear is different
across the datasets.)
11Note that our goal is not to determine the predictive power
of the system on new unseen test data. For that one would
have to determine thresholds from a development set, and
apply the model on unseen test data.
4135

--- Page 13 ---

Method
Pros
Cons
LexO
• Interpretable: One can easily examine the words
in the text that are driving the emotion arc
scores.
• Simple and Accessible: Does not require exten-
sive infrastructure or programming expertise to
execute the method.
• Efficient & Environmentally Friendly: Does not
require high compute power.
• Widely Applicable: Does not require domain
specific training data.
• Captures Context by Aggregation: As more data
is available per bin, the predicted emotion arc
gets closer to the true emotion arc because with
more data it is more likely that: If bin x is ex-
pressing more of an emotion than bin y, then x
has higher average word–emotion association
score than y.
• Poor at Instance Level: Often not very accu-
rate at labelling emotions of individual instances
(sentences, tweets, etc.). Does not take context
and long-distance dependencies into account.
• Less Customization: Does not usually capture
domain-specific ways of expressing emotions;
although, if available, domain-specific emotion
lexicons can mitigate this limitation.
ML
• Great at Instance Level: Achieves state-of-the-
art performance on emotion labelling instances.
• Better at Capturing Context: Considers context
and long-range dependencies effectively.
• Hard to interpret/explain the output.
• Requires extensive compute power and storage.
• Requires extensive computational expertise.
• Requires domain-specific training data.
Table 5: Characteristics of the Lexicon-Only (LexO) and Machine Learning (ML) based methods.
D
African Languages
Information on the African languages used in our
study are shown in Table 6.
E
Emotion Labelled Datasets
In Table 7, we shown the emotion labelled in-
stances for Arabic, and Spanish languages.
F
Code and Resources
The code and resources used are made freely avail-
able on the project homepage.12 The code allows
for easy generation of high-quality emotion arcs
for the provided text stream (especially useful for
those outside of computer science).
12https://github.com/dteodore/EmotionArcs
4136

--- Page 14 ---

Figure 5: Valence Arcs: Spearman correlations of the arcs generated using the sentiment-classification Oracle
System with the gold arcs. Note: ‘OS (Accuracy)’ refers to the accuracy of the Oracle System on instance-level
sentiment classification.
Language
Family
Spoken In
#Speakers
Amharic
Afroasiatic
Ethiopia
57.5 million
Hausa
Afroasiatic
northern Nigeria, Ghana, Cameroon,
72 million
Benin, Togo, Ivory Coast
Igbo
Niger–Congo
Southeastern Nigeria
30 million
Kinyarwanda
Niger–Congo
Rwanda
9.8 million
Swahili
Bantu
Tanzania, Kenya, Mozambique
200 million
Yoruba
Niger–Congo
Southwestern and Central Nigeria
52 million
Table 6: Indigenous African languages included in our study.
Dataset
Source
Domain
Dimension
Label Type
#Instances
SemEval 2018 Ar (V-OC)
Mohammad et al. (2018)
tweets
valence
categorical (-3,-2,...3)
1,800
SemEval 2018 Ar (V-Reg)
Mohammad et al. (2018)
tweets
valence
continuous (0 to 1)
1,800
SemEval 2018 Es (V-OC)
Mohammad et al. (2018)
tweets
valence
categorical (-3,-2,...3)
2,443
SemEval 2018 Es (V-Reg)
Mohammad et al. (2018)
tweets
valence
continuous (0 to 1)
2,443
Table 7: Key information pertaining to the Arabic (Ar) and Spanish (Es) emotion-labeled tweets datasets we use
in our experiments. #Instances includes the train, development, and test sets for the SemEval 2018 Task 1.
4137

```
