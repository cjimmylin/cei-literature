---
title: "2019-Ljubesic-The FRENK Datasets of Socially Unacceptable Discourse in Slovene and - PDF Extract"
source_pdf: "2019-Ljubesic-The FRENK Datasets of Socially Unacceptable Discourse in Slovene and.pdf"
pages: 12
extracted_at: "2026-02-13T10:43:49.635504"
---

# PDF Extract: 2019-Ljubesic-The FRENK Datasets of Socially Unacceptable Discourse in Slovene and

**Source PDF:** 2019-Ljubesic-The FRENK Datasets of Socially Unacceptable Discourse in Slovene and.pdf
**Total Pages:** 12

---

## Content

```
--- Page 1 ---

The FRENK Datasets of Socially Unacceptable
Discourse in Slovene and English
Nikola Ljubeˇsi´c1[0000−0001−7169−9152], Darja Fiˇser2,1[0000−0002−9956−1689], and
Tomaˇz Erjavec1[0000−0002−1560−4099]
1 Dept. of Knowledge Technologies, Joˇzef Stefan Institute, Ljubljana, Slovenia
{nikola.ljubesic,tomaz.erjavec}@ijs.si
2 Dept. of Translation, Faculty of Arts, University of Ljubljana, Slovenia
darja.fiser@ff.uni-lj.si
Abstract. In this paper we present datasets of Facebook comment threads
to mainstream media posts in Slovene and English developed inside the
Slovene national project FRENK3 which cover two topics, migrants and
LGBT, and are manually annotated for diﬀerent types of socially unac-
ceptable discourse (SUD). The main advantages of these datasets com-
pared to the existing ones are identical sampling procedures, producing
comparable data across languages and an annotation schema that takes
into account six types of SUD and ﬁve targets at which SUD is directed.
We describe the sampling and annotation procedures, and analyze the
annotation distributions and inter-annotator agreements. We consider
this dataset to be an important milestone in understanding and combat-
ing SUD for both languages.
Keywords: Socially unacceptable discourse · Slovene language · English
language · Manually annotated dataset.
1
Introduction
With the transformative role of social media in public communication and opin-
ion, there is increased pressure to understand and manage inappropriate on-line
content. The research community is by now generally aware of the complexity of
the inappropriateness in on-line communication, and there is an overall agree-
ment that annotating real-world datasets with these phenomena, both for under-
standing the phenomenon via statistical analysis, as well as for (semi-)automation
via machine learning is the way forward in combating this major downside of
the social media [4,5].
The currently available datasets of inappropriate on-line communication are
primarily compiled for English, such as the Twitter dataset annotated for racist
and sexist hate speech [7]4, the Wikimedia Toxicity Data Set [8]5, the Hate
3 The acronym FRENK stands for “FRENK - Raziskave Elektronske Nespodobne
Komunikacije” (engl. “Research on Electronic Inappropriate Communication”).
4 https://github.com/ZeerakW/hatespeech
5 https://figshare.com/projects/Wikipedia_Talk/16731
arXiv:1906.02045v2  [cs.CL]  13 Jun 2019

--- Page 2 ---

2
N. Ljubeˇsi´c et al.
Speech Identiﬁcation dataset [1]6, the SFU Opinion and Comment Corpus 7,
and the Oﬀensive Language Identiﬁcation Dataset (OLID) [9]8. Datasets in other
languages have recently started to emerge as well, with a German Twitter dataset
on the topic of refugees in Germany [6]9, a Greek Sport News Comment dataset
[5]10 and two large datasets of Slovene and Croatian online news comments
manually moderated by the site administrators [4]11 12.
The annotation schemas used in these datasets are very diﬀerent, ranging
from encoding multiple toxicity levels, covert vs. overt aggressiveness, the target
of the inappropriateness only etc. The ﬁrst two pieces of work to take into account
both the type of SUD and its target are the annotation schema presented in [2]
(which is used in the dataset presented in this paper) and the OLID dataset [9].
In this paper we present datasets of Facebook posts and comments of main-
stream news media from Slovenia and Great Britain, covering the topics of mi-
grants and LGBT. Each comment is annotated with a two-dimensional annota-
tion schema for SUD, covering both the type and the target of SUD. The main
contributions of this paper are the following: (1) we oﬀer a selection of Facebook
pages aimed at representativeness and comparability for a speciﬁc country / lan-
guage, (2) we apply an identical formalism on comparable data in two languages,
making this the ﬁrst multilingual dataset annotated for SUD we are aware of, (3)
we annotate for a very broad phenomenon of SUD, covering most phenomena
various datasets cover in isolation, (4) we annotate full discussion (comment)
threads, not isolated short utterances, ensuring both that (a) the annotators
are as informed of the context as possible while making their decisions (e.g.,
annotating tweets in isolation, not knowing their context, is a questionable, but
regular practice) and (b) that the context of the comment is available either for
analyzing the dataset or using the dataset for (semi)automating the identiﬁca-
tion of SUD, and (5) we perform a ﬁrst analysis of this rich dataset, observing
interesting phenomena both across topics and across languages.
2
Dataset Construction
By selecting the Facebook pages of mainstream media that would constitute our
dataset, we were aiming at criteria that would make the datasets as compara-
ble as possible across languages.13 We opted for the most visited web sites of
6 https://data.world/crowdflower/hate-speech-identification
7 https://github.com/sfu-discourse-lab/SOCC
8 https://scholar.harvard.edu/malmasi/olid
9 https://github.com/UCSM-DUE/IWG_hatespeech_public
10 https://straintek.wediacloud.net/static/gazzetta-comments-dataset/
gazzetta-comments-dataset.tar.gz
11 http://hdl.handle.net/11356/1201
12 http://hdl.handle.net/11356/1202
13 While in this paper we describe the annotation results of Slovene and English only,
an annotation campaign over Croatian data is already under way and plans exist to
annotate Dutch and French data as well.

--- Page 3 ---

Datasets of socially unacceptable discourse in Slovene and English
3
mainstream media according to the Alexa service14 that have popular Facebook
pages. For Slovene, this procedure yielded 24urcom,15 SiOL.net.Novice16 and
Nova24TV17, while for English we selected bbcnews,18 DailyMail 19 and the-
guardian.20 The only intervention into the list obtained from the Alexa service
was the removal of the Slovene public broadcast RTV Slovenija, as its Facebook
page RTV.SLOVENIJA is not very active since this medium has a very good
in-house solution to news commenting.
Once we harvested all the available posts and comments from these pages via
the public Graph API2122, we started the process of identifying posts covering
our two topics: migrants and LGBT. Topic identiﬁcation was performed in the
following way: (1) we manually identiﬁed a selection of around 100 posts per
topic (including a category for covering other news, i.e., not migrants and not
LGBT) via keywords, (2) we trained a simple word- and character-ngram-based
linear SVM classiﬁer on these posts, (3) we classiﬁed the whole collection of
Facebook posts with that classiﬁer, (4) we manually corrected classiﬁcations of
100 random posts per topic (including the other category), (5) we added these
posts to our dataset of manually-annotated posts and retrained the classiﬁer,
and (6) we performed a ﬁnal classiﬁcation of the posts. For the ﬁnal annotation
we discarded the posts annotated as other and selected the posts annotated with
the two remaining topics with the highest conﬁdence score.
With this process which included two rounds of (quick) manual annotation
we wanted to produce a training set representative of the two topics, and not of
the keywords used in the initial topic identiﬁcation.
In early stages of the development of the topic identiﬁcation process, we
experimented with (1) merging all Facebook pages together vs. classifying each
Facebook page separately and (2) representing each post either through the post
text only vs. representing it with the post text as well as the text of the ﬁrst
ten comments. These experiments showed that better results are achieved if (1)
all Facebook posts were classiﬁed together (having three times the amount of
training data, but greater variety of post and comment styles) and (2) each post
was represented through the text of the post and the ﬁrst ten comments (having
more text per post at classiﬁer’s disposal, but combining the text of the post
together with the users’ responses, which might be less informative of the topic).
14 https://www.alexa.com/topsites/countries
15 https://www.facebook.com/24urcom
16 https://www.facebook.com/SiOL.net.Novice
17 https://www.facebook.com/Nova24TV
18 https://www.facebook.com/bbcnews
19 https://www.facebook.com/DailyMail
20 https://www.facebook.com/theguardian
21 https://developers.facebook.com/docs/graph-api/
22 To use this service from May 2018 onwards, users have to go through a screening
process that would quite likely not be successful for harvesting purposes, but our
collection was performed in October 2017, before this restrictive change in policy.

--- Page 4 ---

4
N. Ljubeˇsi´c et al.
3
Dataset Annotation
For annotating the datasets, we used a two-dimensional annotation schema an
early version of which was presented in [2], covering both the type of potentially
socially unacceptable discourse and the target this discourse is aimed at. The
annotation was performed in PyBossa,23 a web-based crowdsourcing tool.
3.1
Annotation Schema
While annotating for the type of SUD, annotators used the decision tree sketched
in Figure 1. This decision tree has six leaves, representing the six types of SUD
we discriminate between. The main distinctions regarding the type of SUD are
made whether SUD is aimed at the background of a person (e.g., religion, sexual
orientation), whether the SUD is aimed at other groups or an individual (vs.
just being unacceptable in terms of swearing), and whether there are elements
of violence in SUD or not.
Is this SUD aimed at someone’s background?
YES: Are there elements of violence?
YES: background, violence
NO:
background, offensive speech
NO:
Is this SUD aimed towards individuals or other groups?
YES: Are there elements of violence?
YES: other, threat
NO:
other, offensive speech
NO:
Is the speech unacceptable?
YES: inappropriate speech
NO:
acceptable speech
Fig. 1. Decision tree used for identifying the type of socially unacceptable discourse
As for the target of SUD, we discriminate between (1) SUD aimed at migrants
or LGBT (2) SUD aimed at individuals or groups related to migrants or LGBT
(such as NGOs, public bodies etc.), (3) SUD aimed at journalists and media, (4)
SUD aimed at other commentators in the discussion thread and (5) SUD aimed
at someone else.
We consider this annotation schema to be the most comprehensive schema
of SUD-related phenomena applied to this day on any dataset.
3.2
Annotation Procedure
The annotation campaign was divided into tasks, where each task consisted of
the post text (published by the medium) and all the comments (written by their
23 https://pybossa.com

--- Page 5 ---

Datasets of socially unacceptable discourse in Slovene and English
5
readers) in the discussion thread. For each task the post either had to be anno-
tated as irrelevant (in case of incorrect topic classiﬁcation presented in Section
2), or each comment in the task had to be annotated with the corresponding
SUD type and target via two drop-down menus. Going back to tasks that were
already submitted was not possible as PyBossa does not oﬀer such an option.
Furthermore, discussion threads that were longer than 20 comments were split
into multiple tasks as annotating more than 20 comments before submitting a
task would easily become too cumbersome for the annotators. The tasks contin-
uing the annotation of a discussion thread also contained the ﬁve last comments
from the previous task to give the annotators some discussion context. Whole
discussion threads were annotated regardless of their length as such an approach
was considered to be the least problematic regarding sampling decisions (e.g.,
what part of the discussion thread to annotate). An example screenshot of the
annotation interface is depicted in Figure 2.
Fig. 2. The PyBossa interface used for annotating the datasets.
The annotators performing the annotation were master students from the
Faculty of Arts and the Faculty of Social Sciences from the University of Ljubl-
jana. They all attended an initial half-day annotator training which was followed
by an initial annotation round where all of the 32 annotators annotated the same
data and discussions about the problematic cases were held via a mailing list. Af-

--- Page 6 ---

6
N. Ljubeˇsi´c et al.
ter the initial training, the annotators were randomly assigned to one of the two
topics (migrants or LGBT). The same split by topic was then retained through-
out the entire annotation campaign. In the ﬁrst annotation campaign, Slovene
data were annotated by approximately eight annotators per comment. The over-
all decision to gather around eight annotations per comment was based on the
awareness of the complexity of the annotation schema and the phenomenon it-
self, as well as initial calculations of inter-annotator (dis)agreement.After the
annotation campaign of Slovene data, roughly half of the annotators signed up
for the annotation of the English data, depending both on their previous perfor-
mance and their self-assessed skill of the English language. To keep the number
of annotations per comment similar to Slovene data, the English annotation
campaign took twice as long as the Slovene annotation campaign.
After ﬁnishing each PyBossa project, the annotations were downloaded from
the PyBossa instance and analyzed, measuring the agreement inside each com-
ment as the entropy of the annotation distribution. Comments with the highest
entropy were then manually analyzed by an expert (social scientist working at
the national centre for reporting hate speech) in order to communicate the dis-
agreement issues via a mailing list with all the annotators, regardless of the topic
they covered in order to ﬁne-tune annotation guidelines and avoid similar issues
in future annotation rounds.
4
Dataset Analysis
In this section we perform various analyses of the manually annotated datasets.
We start with the description of the size of the dataset, continue with the analysis
of the distribution of annotations and the inter-annotator agreement of the two
dimensions of annotation, and wrap up with an analysis of the distribution of
SUD among the users producing the comments.
4.1
Size of the Datasets
We ﬁrst report on the overall size of the datasets in terms of the number of
posts, number of comments and the number of annotator responses in Table 1.
The results show that the length of discussion threads is similar across topics
and languages, with the LGBT topic in Slovene being the only strong deviation,
where the average discussion thread length is four to ﬁve times shorter than the
rest of the topics and languages.
Regarding the distribution of the sources (Facebook pages) of the posts that
were annotated, they are all rather evenly distributed, except for the topic of
LBGT in the Slovene dataset, where the number of posts from the Nova24TV
is signiﬁcantly higher than is the case for the other two sources. The Nova24TV
source, is associated with the extreme right of the political spectrum, discussing
LGBT issues, especially the Slovene referendum on same-sex marriage, more
fervently than the remaining sources.

--- Page 7 ---

Datasets of socially unacceptable discourse in Slovene and English
7
Table 1. Size of the datasets by language and topic.
Slovene
English
migrants
LGBT
migrants
LGBT
Number of posts
30
93
16
14
Number of comments
6545
4571
5855
5906
Average thread length
218
49
366
422
Number of annotations
56211
41433
44969
49978
Average number of annotations
8.59
9.06
7.68
8.46
4.2
Annotation Distribution
In this subsection we perform an analysis of the distribution of all the anno-
tations by topic and language. Given that there is a large number of possible
combinations regarding the type and target of the SUD that we annotate for,
Table 3 lists only the ﬁve most frequently assigned annotation combinations in
both languages, treating the two topics as portions of the annotation probability
distributions of all the annotation combinations.
Table 2. Probability distribution of the most frequent annotations by language and
topic.
Slovene
English
type
target
migrants
LGBT migrants
LGBT
Acceptable
No target
0.42
0.54
0.50
0.67
Background, violence
Target
0.07
0.02
0.02
0.00
Background, oﬀensive
Target
0.23
0.17
0.21
0.12
Other, oﬀensive
Commenter
0.08
0.08
0.06
0.11
Other, oﬀensive
Related to
0.04
0.02
0.02
0.01
The results show that about half of the annotated comments are socially
acceptable, which is a surprisingly low result. It is true that the topics where
chosen with the expectation of high SUD occurrence, but we consider the amount
of SUD in roughly half of the comments to be rather striking, especially given
the fact that some of the most unacceptable comments might have been removed
from Facebook prior to our data harvesting.
In Slovene there seems to be less socially acceptable content on these topics,
which is observed more frequently on the topic of LGBT than migrants in both
languages. The diﬀerence between the two languages is especially visible on the
LGBT topic where there is an absolute diﬀerence of 13% between Slovene and
English, pointing towards greater acceptance of LGBT in the British society.24
24 As always, these results have to be taken with caution and not as ﬁnal, as other
factors might have produced this diﬀerence, such as (1) the fact that in Slovenia the
referendum regarding same-sex marriages was carried out during the period these
Facebook posts cover and (2) the fact that most of the LGBT-related content comes

--- Page 8 ---

8
N. Ljubeˇsi´c et al.
The four most frequently occurring category combinations of SUD in both
languages and topics are, in decreasing order: (1) SUD directed at migrants
or LGBT people, being oﬀensive, (2) SUD directed at other commenters, being
oﬀensive (3) SUD directed at migrants or LGBT people, inciting violence and (4)
SUD directed at people or organisations related to migrants and LGBT people,
being oﬀensive.
The most worrisome result among these is that the most problematic cate-
gory, SUD inciting violence towards migrants or LGBT people, is present in the
top ﬁve categories, covering between 7 and below 1 percent of the annotations,
depending on the language and topic. It follows the overall trend of observing
higher numbers for Slovene compared to English, and for migrants compared
to LGBT. The overall good side of these results is that in the English dataset
on the topic of LGBT the percentage of such annotations is below 1%, but the
percentage of such annotations in Slovene related to migrants is at very high
7%.
Regarding the SUD directed at fellow commenters, in Slovene it is similarly
present on both topics, while in English data it is similarly frequent on the topic
of migrants, but almost as twice as high on the topic of LGBT. This suggests that
the SUD generated on the LGBT topic in English data is often generated due
to disagreement with the remaining commenters, not directed at LGBT people
directly. This result also explains the lower percentage of more problematic types
of SUD for this language and topic. It seems that British people (or, to be more
precise, commenters on British online media) are not directly intolerant towards
LGBT people per se, but are intolerant towards related issues, such as same-sex
marriage, same-sex partners adopting children etc.
4.3
Inter-annotator Agreement
To measure the complexity of the annotation task as well as the level up to
which we should trust single annotations performed in this dataset, we calcu-
lated the Krippendorﬀ’s α inter-annotator agreement score. This score is suitable
for annotation campaigns with more than two annotators, as well as spotty an-
notations, taking also into account agreement by chance [3]. Given that the type
of SUD can be considered both a nominal as well as an ordinal variable, we
perform calculations of inter-annotator agreement for both cases. For the target
of the SUD, no order can be established, therefore we consider this variable to
be nominal only.
The measured agreement between the annotators is considered low by social
science standards, i.e., not good enough to draw even tentative conclusions.
This is why we have decided to gather multiple annotations from the beginning,
from Nova24TV, which is, as already mentioned, a medium on the right side of
the political spectrum. The latter has proven to have an impact as this source has
socially acceptable comments in 42% of cases, while the other two have 57% and and
62% of non-SUD comments on this topic. Both other sources still have, however, a
higher percentage of SUD comments than the English average.

--- Page 9 ---

Datasets of socially unacceptable discourse in Slovene and English
9
Table 3. Krippendorﬀ’s α inter-annotator agreement by language and topic.
Slovene
English
Dimension
Variable type migrants
LGBT
migrants
LGBT
type
nominal
0.499
0.500
0.436
0.357
type
ordinal
0.595
0.590
0.516
0.444
target
nominal
0.528
0.507
0.445
0.380
with the goal of combining them into single high-quality annotations. Some
initial experiments on collecting professional annotations for a subset of Slovene
comments and comparing those to the mode of all non-professional annotations,
i.e., the most frequent annotation, show that collecting multiple non-professional
annotations is a reasonable approach, with the Krippendorﬀ’s α for the type
of SUD as a nominal variable being 0.731, for the type of SUD as an interval
variable 0.795, and for the target of SUD as a nominal variable the Krippendorﬀ’s
α being 0.733. Thereby, all the agreements are above 0.66, which is the lower
threshold for useful annotations by social science standards. Obtaining high-
quality annotations from the non-professional annotations is, however, not the
focus of this work and will be performed in more detail in future experiments.
Regarding the diﬀerence in the observed agreements, it tends to be higher
on Slovene than on English which can be due to the fact that the annotators
were native speakers of Slovene, living in Slovenia, with better linguistic but
also contextual knowledge. As expected, if we consider the type of SUD to be an
ordinal, and not a nominal variable, the agreement increases, which shows that
the type of SUD does indeed have properties of an ordinal variable. Annotating
the type and target of SUD seem to be similarly complex tasks for the annotators.
The only deviation in agreement within a language seems to be on English
data, where we observe a ten-point lower result for the LGBT topic than for
migrants. A tentative hypothesis for such a result is the distribution of the
annotations, with the three most frequent annotation combinations making 91%
of the annotations, while in the remaining three cases these cover between 75 and
81 % of the annotations only. Thereby the agreement by chance in the LGBT
topic on English data is higher, making the Krippendorﬀ’s α with the same
observed agreement lower than for the remaining cases.
As already brieﬂy discussed, future work is planned in increasing the quality
of the annotations by exploiting the fact that we have around 8 annotations
available per comment which can be used to calculate some statistic, e.g., the
mode (most frequent case) of the annotations, which has preliminarly showed
to signiﬁcantly improve the quality of annotations, or to learn to extract the
optimal annotation from the multiple annotations by using a small subset of
expert annotations in a supervised machine learning setting.
4.4
Distribution of SUD among Users
While this dataset enables a myriad of analyses of the occurrence of various
forms of SUD due to metadata richness, we have chosen one of the most pressing

--- Page 10 ---

10
N. Ljubeˇsi´c et al.
questions for the ﬁrst analysis of this dataset: Who produces most of SUD? Is
this a small number of users, or is SUD generated in a similar intensity by most
users?
Fig. 3. Distribution of percentage of non-SUD comments among users of Slovene (left)
and English (right) datasets on topics of migrants (up) and LGBT (down).
We operationalise the amount of SUD produced by speciﬁc users as the per-
centage of non-SUD comments for each user who has posted 3 or more comments
in a speciﬁc topic and language. We present the results via histograms of per-
centages of non-SUD comments per user presented in Figure 3, where the left
histograms show the results for Slovene, right for English, upper for the topic of
migrants and lower for the topic of LGBT.
When reading these plots, one has to bear in mind the percentage of non-
SUD annotations from Section 4.2, which was the lowest for the topic of migrants
in Slovene (upper left histogram) and highest for the topic of LGBT in English
(lower right histogram). What these plots are primarily informative for is their
shape, i.e., whether they are (1) bell-shaped, which points to the conclusion
that the majority of users produces a medium amount of SUD, while just a
smaller portion produces very little or a lot of SUD, (2) U-shaped, which means
that there are users producing either large or small quantities of SUD or (3)
rather evenly-distributed, which indicates that users produce various quantities

--- Page 11 ---

Datasets of socially unacceptable discourse in Slovene and English
11
of SUD. The regularity, which can be observed in Figure 3 is that in the English
dataset, regardless of the amount of SUD produced, the distributions are rather
bell-shaped, meaning that most users are average producers of SUD, while in
the Slovene dataset the distributions are rather even, suggesting that users are
producing various amounts of SUD.
The results of this analysis point towards the conclusion that English users
are more mainstream-oriented regarding the production of SUD, while among
the Slovene users there are both extreme, medium and non-producers of SUD.
A possible explanation would be for the British media to show a more mature
community of commenters than is the case for the Slovene media. Another ex-
planation for the diﬀering distributions between Slovene and English might be
a more responsible policy of British media, removing regularly a signiﬁcant por-
tion of unacceptable content. This phenomenon will have to be investigated in
more detail in future work.
5
Conclusion
In this paper we have presented a dataset of Facebook comments on posts from
mainstream media in Slovenia and Great Britain covering the topics of migrants
and LGBT, which were manually annotated with the type and target of socially
unacceptable discourse. We have described the data sampling, topic identiﬁca-
tion and manual annotation of the dataset.
We have performed an initial analysis of the manually annotated dataset,
showing that more SUD is produced in Slovene than in English media, and that
more SUD is produced on the topic of migrants than LGBT.
Our analysis of the inter-annotator agreement shows that both type and tar-
get are similarly complex for the annotators, with a medium agreement below the
expected quality in social science. Initial experiments on comparing professional
annotations with the modes (most frequent annotations) of the non-professional
annotations show to improve agreement signiﬁcantly, moving it to the area of
useful annotations for social sciences. The fact that we have collected around
eight annotations per comment will be exploited further in future work on ex-
tracting annotations of highest quality possible.
Finally, we have performed an initial analysis of the distribution of SUD
among diﬀerent users, showing that there is a trend of a similar number of users
who produce large, medium and low quantities of SUD in Slovene, while the
English users tend to produce mostly an average amount of SUD, with just
small numbers of users on the extremes of the (non)production of SUD.
Future work on this dataset will focus primarily on the two envisaged us-
ages of the dataset: (1) further analysis of the phenomenon of SUD and (2)
(semi-)automation of SUD identiﬁcation.

--- Page 12 ---

12
N. Ljubeˇsi´c et al.
Acknowledgement
The work described in this paper was funded by the Slovenian Research Agency
within the national basic research project “Resources, methods and tools for
the understanding, identiﬁcation and classiﬁcation of various forms of socially
unacceptable discourse in the information society” (J7-8280, 2017- 2020) and
the Slovenian-Flemish bilateral basic research project “Linguistic landscape of
hate speech on social media” (N06-0099, 2019 2023).
References
1. Davidson, T., Warmsley, D., Macy, M.W., Weber, I.: Automated Hate Speech De-
tection and the Problem of Oﬀensive Language. CoRR abs/1703.04009 (2017),
http://arxiv.org/abs/1703.04009
2. Fiˇser, D., Erjavec, T., Ljubeˇsi´c, N.: Legal framework, dataset and annotation schema
for socially unacceptable online discourse practices in Slovene. In: Proceedings of
the ﬁrst workshop on abusive language online. pp. 46–51 (2017)
3. Krippendorﬀ, K.: Content Analysis: An Introduction to Its Methodology (second
edition). Sage Publications (2004)
4. Ljubeˇsi´c, N., Erjavec, T., Fiˇser, D.: Datasets of Slovene and Croatian Moderated
News Comments. In: Proceedings of the 2nd Workshop on Abusive Language Online
(ALW2). pp. 124–131 (2018)
5. Pavlopoulos, J., Malakasiotis, P., Androutsopoulos, I.: Deeper Attention to Abusive
User Content Moderation. In: Proceedings of the 2017 Conference on Empirical
Methods in Natural Language Processing, EMNLP 2017, Copenhagen, Denmark,
September 9-11, 2017. pp. 1125–1135 (2017), https://aclanthology.info/papers/
D17-1117/d17-1117
6. Ross, B., Rist, M., Carbonell, G., Cabrera, B., Kurowsky, N., Wojatzki, M.: Measur-
ing the Reliability of Hate Speech Annotations: The Case of the European Refugee
Crisis. CoRR abs/1701.08118 (2017), http://arxiv.org/abs/1701.08118
7. Waseem, Z., Hovy, D.: Hateful Symbols or Hateful People? Predictive Features
for Hate Speech Detection on Twitter. In: Proceedings of the Student Research
Workshop, SRW@HLT-NAACL 2016, The 2016 Conference of the North Ameri-
can Chapter of the Association for Computational Linguistics: Human Language
Technologies, San Diego California, USA, June 12-17, 2016. pp. 88–93 (2016),
http://aclweb.org/anthology/N/N16/N16-2013.pdf
8. Wulczyn, E., Thain, N., Dixon, L.: Ex machina: Personal attacks seen at
scale. In: Proceedings of the 26th International Conference on World Wide
Web. pp. 1391–1399. WWW ’17, International World Wide Web Conferences
Steering
Committee,
Republic
and
Canton
of
Geneva,
Switzerland
(2017).
https://doi.org/10.1145/3038912.3052591,
https://doi.org/10.1145/3038912.
3052591
9. Zampieri, M., Malmasi, S., Nakov, P., Rosenthal, S., Farra, N., Kumar, R.: Pre-
dicting the Type and Target of Oﬀensive Posts in Social Media. In: Proceedings of
NAACL (2019)

```
