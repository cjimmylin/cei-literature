---
title: "HateBERT - PDF Extract"
source_pdf: "2021-Caselli-HateBERT.pdf"
pages: 9
extracted_at: "2026-01-24T17:05:08.520515"
---

# PDF Extract: HateBERT

**Source PDF:** 2021-Caselli-HateBERT.pdf
**Total Pages:** 9

---

## Content

```
--- Page 1 ---

Proceedings of the Fifth Workshop on Online Abuse and Harms, pages 17–25
August 6, 2021. ©2021 Association for Computational Linguistics
17
HateBERT: Retraining BERT for Abusive Language Detection in English
Tommaso Caselli , Valerio Basile , Jelena Mitrovi´c , Michael Granitzer
University of Groningen
University of Turin
University of Passau
t.caselli@rug.nl
valerio.basile@unito.it
{jelena.mitrovic, michael.granitzer}@uni-passau.de
Abstract
We introduce HateBERT, a re-trained BERT
model for abusive language detection in En-
glish.
The model was trained on RAL-E,
a large-scale dataset of Reddit comments in
English from communities banned for be-
ing offensive, abusive, or hateful that we
have curated and made available to the pub-
lic.
We present the results of a detailed
comparison between a general pre-trained lan-
guage model and the retrained version on three
English datasets for offensive, abusive lan-
guage and hate speech detection tasks.
In
all datasets, HateBERT outperforms the corre-
sponding general BERT model. We also dis-
cuss a battery of experiments comparing the
portability of the ﬁne-tuned models across the
datasets, suggesting that portability is affected
by compatibility of the annotated phenomena.
1
Introduction
The development of systems for the automatic iden-
tiﬁcation of abusive language phenomena has fol-
lowed a common trend in NLP: feature-based lin-
ear classiﬁers (Waseem and Hovy, 2016; Ribeiro
et al., 2018; Ibrohim and Budi, 2019), neural net-
work architectures (e.g., CNN or Bi-LSTM) (Kshir-
sagar et al., 2018; Mishra et al., 2018; Mitrovi´c
et al., 2019; Sigurbergsson and Derczynski, 2020),
and ﬁne-tuning pre-trained language models, e.g.,
BERT, RoBERTa, a.o., (Liu et al., 2019; Swamy
et al., 2019). Results vary both across datasets and
architectures, with linear classiﬁers qualifying as
very competitive, if not better, when compared to
neural networks. On the other hand, systems based
on pre-trained language models have reached new
state-of-the-art results. One issue with these pre-
trained models is that the training language variety
makes them well suited for general-purpose lan-
guage understanding tasks, and it highlights their
limits with more domain-speciﬁc language vari-
eties. To address this, there is a growing inter-
Figure 1: Abusive language phenomena and their rela-
tionships (adapted from Poletto et al. (2020)).
est in generating domain-speciﬁc BERT-like pre-
trained language models, such as AlBERTo (Polig-
nano et al., 2019) or TweetEval (Barbieri et al.,
2020) for Twitter, BioBERT for the biomedical
domain in English (Lee et al., 2019), FinBERT
for the ﬁnancial domain in English (Yang et al.,
2020), and LEGAL-BERT for the legal domain
in English (Chalkidis et al., 2020). We introduce
HateBERT, a pre-trained BERT model for abusive
language phenomena in social media in English.
Abusive language phenomena fall along a wide
spectrum including, a.o., microaggression, stereo-
typing, offense, abuse, hate speech, threats, and
doxxing (Jurgens et al., 2019). Current approaches
have focus on a limited range, namely offensive
language, abusive language, and hate speech. The
connections among these phenomena have only
superﬁcially been accounted for, resulting in a frag-
mented picture, with a variety of deﬁnitions, and
(in)compatible annotations (Waseem et al., 2017).
Poletto et al. (2020) introduce a graphical visuali-
sation (Figure 1) of the connections among abusive
language phenomena according to the deﬁnitions in
previous work (Waseem and Hovy, 2016; Fortuna
and Nunes, 2018; Malmasi and Zampieri, 2018;
Basile et al., 2019; Zampieri et al., 2019). When
it comes to offensive language, abusive language,
and hate speech, the distinguishing factor is their
level of speciﬁcity. This makes offensive language

--- Page 2 ---

18
the most generic form of abusive language phe-
nomena and hate speech the most speciﬁc, with
abusive language being somewhere in the middle.
Such differences are a major issue for the study
of portability of models. Previous work (Karan
and ˇSnajder, 2018; Benk, 2019; Pamungkas and
Patti, 2019; Rizoiu et al., 2019) has addressed this
task by conﬂating portability with generalizabil-
ity, forcing datasets with different phenomena into
homogenous annotations by collapsing labels into
(binary) macro-categories. In our portability experi-
ments, we show that the behavior of HateBERT can
be explained by accounting for these difference in
speciﬁcity across the abusive language phenomena.
Our key contributions are: (i.) additional ev-
idence that further pre-training is a viable strat-
egy to obtain domain-speciﬁc or language variety-
oriented models in a fast and cheap way; (ii.) the re-
lease of HateBERT, a pre-trained BERT for abusive
language phenomena, intended to boost research in
this area; (iii.) the release of a large-scale dataset
of social media posts in English from communities
banned for being offensive, abusive, or hateful.
2
HateBERT: Re-training BERT with
Abusive Online Communities
Further pre-training of transformer based pre-
trained language models is becoming more and
more popular as a competitive, effective, and fast
solution to adapt pre-trained language models to
new language varieties or domains (Barbieri et al.,
2020; Lee et al., 2019; Yang et al., 2020; Chalkidis
et al., 2020), especially in cases where raw data
are scarce to generate a BERT-like model from
scratch (Gururangan et al., 2020). This is the case
of abusive language phenomena. However, for
these phenomena an additional predicament with
respect to previous work is that the options for
suitable and representative collections of data are
very limited. Directly scraping messages contain-
ing profanities would not be the best option as lots
of potentially useful data may be missed. Graumas
et al. (2019) have used tweets about controversial
topics to generate offensive-loaded embeddings,
but their approach presents some limits. On the
other hand, Merenda et al. (2018) have shown the
effectiveness of using messages from potentially
abusive-oriented on-line communities to generate
so-called hate embeddings. More recently, Papakyr-
iakopoulos et al. (2020) have shown that biased
word embeddings can be beneﬁcial. We follow the
idea of exploiting biased embeddings by creating
them using messages from banned communities in
Reddit.
RAL-E: the Reddit Abusive Language English
dataset
Reddit is a popular social media outlet
where users share and discuss content. The website
is organized into user-created and user-moderated
communities known as subreddits, being de facto
on-line communities. In 2015, Reddit strength-
ened its content policies and banned several subred-
dits (Chandrasekharan et al., 2017). We retrieved a
large list of banned communities in English from
different sources including ofﬁcial posts by the
Reddit administrators and Wikipedia pages.1 We
then selected only communities that were banned
for being deemed to host or promote offensive, abu-
sive, and/or hateful content (e.g., expressing harass-
ment, bullying, inciting/promoting violence, incit-
ing/promoting hate). We collected the posts from
these communities by crawling a publicly available
collection of Reddit comments.2 For each post,
we kept only the text and the name of the commu-
nity. The resulting collection comprises 1,492,740
messages from a period between January 2012 and
June 2015, for a total of 43,820,621 tokens. The vo-
cabulary of RAL-E is composed of 342,377 types
and the average post length is 32.25 tokens. We
further check the presence of explicit signals of abu-
sive language phenomena using a list of offensive
words. We selected all words with an offensiveness
scores equal or higher than 0.75 from Wiegand
et al. (2018)’s dictionary. We found that explicit
offensive terms represent 1.2% of the tokens and
that only 260,815 messages contain at least one
offensive term. RAL-E is skewed since not all com-
munities have the same amount of messages. The
list of selected communities with their respective
number of retrieved messages is reported in Table
A.1 and the top 10 offensive terms are illustrated
in Table A.2 in Appendix A.
Creating HateBERT
From the RAL-E dataset,
we used 1,478,348 messages (for a total of
43,379,350 tokens) to re-train the English BERT
base-uncased model3 by applying the Masked
Language Model (MLM) objective. The remain-
ing 149,274 messages (441,271 tokens) have been
used as test set. We retrained for 100 epochs (al-
1https://en.wikipedia.org/wiki/
Controversial_Reddit_communities
2https://www.reddit.com/r/datasets/
comments/3bxlg7/i_have_every_publicly_
available_reddit_comment/
3We used the pre-trained model available via the hug-
gingface Transformers library - https://github.com/
huggingface/transformers

--- Page 3 ---

19
most 2 million steps) in batches of 64 samples,
including up to 512 sentencepiece tokens. We used
Adam with learning rate 5e-5. We trained using
the huggingface code4 on one Nvidia V100 GPU.
The result is a shifted BERT model, HateBERT
base-uncased, along two dimensions: (i.) lan-
guage variety (i.e. social media); and (ii.) polarity
(i.e., offense-, abuse-, and hate-oriented model).
Since our retraining does not change the vo-
cabulary, we veriﬁed that HateBERT has shifted
towards abusive language phenomena by using
the MLM on ﬁve template sentences of the form
“[someone] is a(n)/ are [MASK]”. The
template has been selected because it can trigger
biases in the model’s representations. We changed
[someone] with any of the following tokens:
“you”, “she”, “he”, “women”, “men” Although not
exhaustive, HateBERT consistently present profan-
ities or abusive terms as mask ﬁllers, while this
very rarely occurs with the generic BERT. Table 1
illustrates the results for “women”.
BERT
HateBERT
“women”
excluded (.075)
stu**d (.188)
encouraged (.032)
du*b (.128)
included (.027)
id***s (.075)
Table 1:
MLM top 3 candidates for the templates
“Women are [MASK.]”.
3
Experiments and Results
To verify the usefulness of HateBERT for detect-
ing abusive language phenomena, we run a set of
experiments on three English datasets.
OffensEval 2019
(Zampieri et al., 2019) the
dataset contains 14,100 tweets annotated for of-
fensive language. According to the task deﬁnition,
a message is labelled as offensive if “it contains
any form of non-acceptable language (profanity)
or a targeted offense, which can be veiled or di-
rect.” (Zampieri et al., 2019, pg. 76). The dataset
is split into training and test, with 13,240 messages
in training and 860 in test. The positive class (i.e.
messages labeled as offensive) are 4,400 in training
and 240 in test. No development data is provided.
AbusEval
(Caselli et al., 2020) This dataset has
been obtained by adding a layer of abusive lan-
4https://github.com/huggingface/
transformers/tree/master/src/
transformers
guage annotation to OffensEval 2019. Abusive
language is deﬁned as a speciﬁc case of offensive
language, namely “hurtful language that a speaker
uses to insult or offend another individual or a
group of individuals based on their personal quali-
ties, appearance, social status, opinions, statements,
or actions.” (Caselli et al., 2020, pg. 6197). The
main difference with respect to offensive language
is the exclusion of isolated profanities or untargeted
messages from the positive class. The size of the
dataset is the same as OffensEval 2019.The differ-
ences concern the distribution of the positive class
which results in 2,749 in training and 178 in test.
HatEval
(Basile et al., 2019) The English por-
tion of the dataset contains 13,000 tweets anno-
tated for hate speech against migrants and women.
The authors deﬁne hate speech as “any communi-
cation that disparages a person or a group on the
basis of some characteristic such as race, color,
ethnicity, gender, sexual orientation, nationality, re-
ligion, or other characteristics.” (Basile et al., 2019,
pg. 54). Only hateful messages targeting migrants
and women belong to the positive class, leaving
any other message (including offensive or abusive
against other targets) to the negative class. The
training set is composed of 10,000 messages and
the test contains 3,000. Both training and test con-
tain an equal amount of messages with respect to
the targets, i.e., 5,000 each in training and 1,500
each in test. This does not hold for the distribution
of the positive class, where 4,165 messages are
present in the training and 1,252 in the test set.
All datasets are imbalanced between positive and
negative classes and they target phenomena that
vary along the speciﬁcity dimension. This allows us
to evaluate both the robusteness and the portability
of HateBERT.
We applied the same pre-processing steps and
hyperparameters when ﬁne-tuning both the generic
BERT and HateBERT. Pre-processing steps and
hyperparameters (Table A.3) are more closely de-
tailed in the Appendix B. Table 2 illustrates the re-
sults on each dataset (in-dataset evaluation), while
Table 3 reports on the portability experiments
(cross-dataset evaluation). The same evaluation
metric from the original tasks, or paper, is applied,
i.e., macro-averaged F1 of the positive and negative
classes.
The in-domain results conﬁrm the validity of
the re-training approach to generate better mod-
els for detection of abusive language phenomena,
with HateBERT largely outperforming the corre-

--- Page 4 ---

20
Dataset
Model
Macro F1 Pos. class - F1
OffensEval
2019
BERT
.803±.006
.715±.009
HateBERT
.809±.008
.723±.012
Best
.829
.752
AbusEval
BERT
.727±.008
.552±.012
HateBERT
.765±.006
.623±.010
Caselli et al. (2020) .716±.034
.531
HatEval
BERT
.480±.008
.633±.002
HateBERT
.516±.007
.645±.001
Best
.651
.673
Table 2: BERT vs. HateBERT: in-dataset. Best scores
in bold. For BERT and HateBERT we report the aver-
age from 5 runs and its standard deviations. Best corre-
sponds to the best systems in the original shared tasks.
Caselli et al. (2020) is the most recent result for AbusE-
val.
Train
Model
OffensEval
2019
AbusEval HatEval
OffensEval
2019
BERT
–
.726
.545
HateBERT
.–
.750
.547
AbusEval
BERT
.710
–
.611
HateBERT
.713
–
.624
HatEval
BERT
.572
.590
–
HateBERT
.543
.555
–
Table 3: BERT vs. HateBERT: Portability. Columns
show the dataset used for testing. Best macro F1 per
training/test combination are underlined.
sponding generic model. A detailed analysis per
class shows that the improvements affect both the
positive and the negative classes, suggesting that
HateBERT is more robust. The use of data from a
different social media platform does not harm the
ﬁne-tuning stage of the retrained model, opening
up possibilities of cross-fertilization studies across
social media platforms. HateBERT beats the state-
of-the-art for AbusEval, achieving competitive re-
sults on OffensEval and HatEval. In particular,
HateBERT would rank #4 on OffensEval and #6
on HatEval, obtaining the second best F1 score on
the positive class.
The portability experiments were run using the
best model for each of the in-dataset experiments.
Our results show that HateBERT ensures better
portability than a generic BERT model, especially
when going from generic abusive language phe-
nomena (i.e., offensive language) towards more
speciﬁc ones (i.e., abusive language or hate speech).
This behaviour is expected and provides empirical
evidence to the differences across the annotated
phenomena. We also claim that HateBERT consis-
tently obtains better representations of the targeted
phenomena. This is evident when looking at the dif-
Train
Model
OffensEval
2019
AbusEval HatEval
P
R
P
R
P
R
OffensEval
2019
BERT
–
– .510 .685 .479 .771
HateBERT
–
– .553 .696 .480 .767
AbusEval
BERT
.776
.420
–
– .545 .571
HateBERT .836
.404
–
– .565 .567
HatEval
BERT
.540
.220 .438 .241
–
–
HateBERT .473
.183 .365 .191
–
–
Table 4: BERT vs. HateBERT: Portability - Precision
and Recall for the positive class. Rows show the dataset
used to train the model and columns the dataset used for
testing. Best scores are underlined.
ferences in False Positives and False Negatives for
the positive class, measured by means of Precision
and Recall, respectively. As illustrated in Table 4,
HateBERT always obtains a higher Precision score
than BERT when ﬁne-tuned on a generic abusive
phenomenon and applied to more speciﬁc ones, at
a very low cost for Recall. The unexpected higher
Precision of HateBERT ﬁne-tuned on AbusEval
and tested on OffensEval 2019 (i.e., from speciﬁc
to generic) is due to the datasets sharing same data
distribution. Indeed, the results of the same model
against HatEval support our analysis.
4
Conclusion and Future Directions
This contribution introduces HateBERT base
uncased,5 a pre-trained language model for abu-
sive language phenomena in English. We conﬁrm
that further pre-training is an effective and cheap
strategy to port pre-trained language models to
other language varieties. The in-dataset evaluation
shows that HateBERT consistently outperforms a
generic BERT across different abusive language
phenomena, such as offensive language (Offen-
sEval 2019), abusive language (AbusEval), and
hate speech (HatEval). The cross-dataset experi-
ments show that HateBERT obtains robust repre-
sentations of each abusive language phenomenon
against which it has been ﬁne-tuned. In particu-
lar, the cross-dataset experiments have provided
(i.) further empirical evidence on the relationship
among three abusive language phenomena along
the dimension of speciﬁcity; (ii.) empirical support
to the validity of the annotated data; (iii.) a princi-
pled explanation for the different performances of
HateBERT and BERT.
5HateBERT, the ﬁne-tuned model, and the RAL-E dataset
are
available
at
https://osf.io/tbd58/?view_
only=d90e681c672a494bb555de99fc7ae780

--- Page 5 ---

21
A known issue concerning HateBERT is its
bias toward the subreddit r/fatpeoplehate.
To address this and other balancing issues, we
retrieved an additional ˜1.3M messages.
This
has allowed us to add 712,583 new messages to
12 subreddits listed in Table A.1, and identify
three additional ones (r/uncensorednews,
r/europeannationalism,
and
r/farright), for a total of 597,609 mes-
sages. This new data is currently used to extend
HateBERT.
Future work will focus on two directions: (i.)
investigating to what extent the embedding repre-
sentations of HateBERT are actually different from
a general BERT pre-trained model, and (ii.) inves-
tigating the connections across the various abusive
langauge phenomena.
Acknowledgements
The project on which this report is based was
funded by the German Federal Ministry of Edu-
cation and Research (BMBF) under the funding
code 01—S20049. The author is responsible for
the content of this publication.
Ethical Statement
In this paper, the authors introduce HateBERT, a
pre-trained language model for the study of abusive
language phenomena in social media in English.
HateBERT is unique because (i.) it is based on
further pre-training of an existing pre-trained lan-
guage model (i.e., BERT base-uncased) rather
than training it from scratch, thus reducing the en-
vironmental impact of its creation; 6 (ii.) it uses
a large collection of messages from communities
that have been deemed to violate the content policy
of a social media platform, namely Reddit, because
of expressing harassment, bullying, incitement of
violence, hate, offense, and abuse. The judgment
on policy violation has been made by the commu-
nity administrators and moderators. We consider
6The Nvidia V100 GPU we used is shared and it has a
maximum number of continuous reserved time of 72 hours.
In total, it took 18 days to complete the 2 million retraining
steps.
this dataset for further pre-training more ecologi-
cally representative of the expressions of different
abusive language phenomena in English than the
use of manually annotated datasets.
The collection of banned subreddits has been
retrieved from a publicly available collection of
Reddit, obtained through the Reddit API and in
compliance with Reddit’s terms of use. From this
collection, we generated the RAL-E dataset. RAL-
E will be publicly released (it is accessible also
at review phase in the Supplementary Materials).
While its availability may have an important impact
in boosting research on abusive language phenom-
ena, especially by making natural interactions in
online communities available, we are also aware
of the risks of privacy violations for owners of
the messages. This is one of the reasons why at
this stage, we only make available in RAL-E the
content of the message without metadata such as
the screen name of the author and the community
where the message was posted. Usernames and
subreddit names have not been used to retrain the
models. This reduces the risks of privacy leakage
from the retrained models. Since the training mate-
rial comes from banned community it is impossible
and impracticable to obtain meaningful consent
from the users (or redditers). In compliance with
the Association for Internet Researchers Ethical
Guidelines7, we consider that: not making avail-
able the username and the speciﬁc community are
the only reliable ways to protect users’ privacy. We
have also manually checked (for a small portion
of the messages) whether it is possible to retrieve
these messages by actively searching copy-paste
the text of the message in Reddit. In none of the
cases were we able to obtain a positive result.
There are numerous beneﬁts from using such
models to monitor the spread of abusive language
phenomena in social media. Among them, we men-
tion the following: (i.) reducing exposure to harm-
ful content in social media; (ii.) contributing to
the creation of healthier online interactions; and
(iii.) promoting positive contagious behaviors and
interactions (Matias, 2019). Unfortunately, work
in this area is not free from potentially negative
impacts. The most direct is a risk of promoting
misrepresentation. HateBERT is an intrinsically
biased pre-trained language model. The ﬁne-tuned
models that can be obtained are not overgenerating
the positive classes, but they suffer from the biases
in the manually annotated data, especially for the
offensive language detection task (Sap et al., 2019;
7https://aoir.org/reports/ethics3.pdf

--- Page 6 ---

22
Davidson et al., 2019). Furthermore, we think that
such tools must always be used under the supervi-
sion of humans. Current datasets are completely
lacking the actual context of occurrence of a mess-
sage and the associated meaning nuances that may
accompany it, labelling the positive classes only on
the basis of superﬁcial linguistic cues. The deploy-
ment of models based on HateBERT “in the wild”
without human supervision requires additional re-
search and suitable datasets for training.
We see beneﬁts in the use of HateBERT in re-
search on abusive language phenomena as well as
in the availability of RAL-E. Researchers are en-
couraged to be aware of the intrinsic biased nature
of HateBERT and of its impacts in real-world sce-
narios.
References
Francesco Barbieri, Jose Camacho-Collados, Luis Es-
pinosa Anke, and Leonardo Neves. 2020. TweetE-
val: Uniﬁed benchmark and comparative evaluation
for tweet classiﬁcation. In Findings of the Associ-
ation for Computational Linguistics: EMNLP 2020,
pages 1644–1650, Online. Association for Computa-
tional Linguistics.
Valerio Basile, Cristina Bosco, Elisabetta Fersini,
Debora Nozza, Viviana Patti, Francisco Manuel
Rangel Pardo, Paolo Rosso, and Manuela San-
guinetti. 2019.
SemEval-2019 task 5:
Multilin-
gual detection of hate speech against immigrants and
women in twitter. In Proceedings of the 13th Inter-
national Workshop on Semantic Evaluation, pages
54–63, Minneapolis, Minnesota, USA. Association
for Computational Linguistics.
Michaela Benk. 2019.
Data Augmentation in Deep
Learning for Hate Speech Detection in Lower Re-
source Settings. Ph.D. thesis, Universit¨at Z¨urich.
Tommaso Caselli, Valerio Basile, Jelena Mitrovic, Inga
Kartoziya, and Michael Granitzer. 2020. I feel of-
fended, don’t be abusive! implicit/explicit messages
in offensive and abusive language. In Proceedings of
The 12th Language Resources and Evaluation Con-
ference, pages 6193–6202, Marseille, France. Euro-
pean Language Resources Association.
Ilias Chalkidis, Manos Fergadiotis, Prodromos Malaka-
siotis, Nikolaos Aletras, and Ion Androutsopoulos.
2020. LEGAL-BERT: The muppets straight out of
law school. In Findings of the Association for Com-
putational Linguistics: EMNLP 2020, pages 2898–
2904, Online. Association for Computational Lin-
guistics.
Eshwar Chandrasekharan, Umashanthi Pavalanathan,
Anirudh Srinivasan, Adam Glynn, Jacob Eisenstein,
and Eric Gilbert. 2017. You can’t stay here: The
efﬁcacy of reddit’s 2015 ban examined through
hate speech. Proceedings of the ACM on Human-
Computer Interaction, 1:1–22.
Thomas Davidson, Debasmita Bhattacharya, and Ing-
mar Weber. 2019. Racial bias in hate speech and
abusive language detection datasets. In Proceedings
of the Third Workshop on Abusive Language Online,
pages 25–35, Florence, Italy. Association for Com-
putational Linguistics.
Paula Fortuna and S´ergio Nunes. 2018. A survey on au-
tomatic detection of hate speech in text. ACM Com-
puting Surveys (CSUR), 51(4):85.
Leon Graumas, Roy David, and Tommaso Caselli.
2019. Twitter-based Polarised Embeddings for Abu-
sive Language Detection. In 2019 8th International
Conference on Affective Computing and Intelligent
Interaction Workshops and Demos (ACIIW), pages
1–7.

--- Page 7 ---

23
Suchin
Gururangan,
Ana
Marasovi´c,
Swabha
Swayamdipta, Kyle Lo, Iz Beltagy, Doug Downey,
and Noah A. Smith. 2020. Don’t stop pretraining:
Adapt language models to domains and tasks.
In
Proceedings of the 58th Annual Meeting of the
Association for Computational Linguistics, pages
8342–8360, Online. Association for Computational
Linguistics.
Muhammad Okky Ibrohim and Indra Budi. 2019.
Multi-label Hate Speech and Abusive Language De-
tection in Indonesian Twitter. In Proceedings of the
Third Workshop on Abusive Language Online, pages
46–57.
David Jurgens, Libby Hemphill, and Eshwar Chan-
drasekharan. 2019. A just and comprehensive strat-
egy for using NLP to address online abuse. In Pro-
ceedings of the 57th Annual Meeting of the Asso-
ciation for Computational Linguistics, pages 3658–
3666, Florence, Italy. Association for Computa-
tional Linguistics.
Mladen Karan and Jan ˇSnajder. 2018. Cross-domain
detection of abusive language online. In Proceed-
ings of the 2nd Workshop on Abusive Language On-
line (ALW2), pages 132–137, Brussels, Belgium. As-
sociation for Computational Linguistics.
Rohan Kshirsagar, Tyrus Cukuvac, Kathy McKeown,
and Susan McGregor. 2018. Predictive embeddings
for hate speech detection on twitter. In Proceedings
of the 2nd Workshop on Abusive Language Online
(ALW2), pages 26–32, Brussels, Belgium. Associa-
tion for Computational Linguistics.
Jinhyuk
Lee,
Wonjin
Yoon,
Sungdong
Kim,
Donghyeon Kim,
Sunkyu Kim,
Chan Ho So,
and Jaewoo Kang. 2019.
BioBERT: a pre-
trained biomedical language representation model
for
biomedical
text
mining.
Bioinformatics,
36(4):1234–1240.
Ping Liu, Wen Li, and Liang Zou. 2019.
NULI at
SemEval-2019 task 6: Transfer learning for offen-
sive language detection using bidirectional trans-
formers.
In Proceedings of the 13th Interna-
tional Workshop on Semantic Evaluation, pages 87–
91, Minneapolis, Minnesota, USA. Association for
Computational Linguistics.
Shervin Malmasi and Marcos Zampieri. 2018. Chal-
lenges in discriminating profanity from hate speech.
Journal of Experimental & Theoretical Artiﬁcial In-
telligence, 30(2):187–202.
J Nathan Matias. 2019. Preventing harassment and in-
creasing group participation through social norms in
2,190 online science discussions. Proceedings of the
National Academy of Sciences, 116(20):9785–9789.
Flavio Merenda, Claudia Zaghi, Tommaso Caselli, and
Malvina Nissim. 2018. Source-driven Representa-
tions for Hate Speech Detection.
In Proceedings
of the 5th Italian Conference on Computational Lin-
guistics (CLiC-it 2018), Turin, Italy.
Pushkar Mishra, Helen Yannakoudakis, and Ekaterina
Shutova. 2018.
Neural character-based composi-
tion models for abuse detection.
In Proceedings
of the 2nd Workshop on Abusive Language Online
(ALW2), pages 1–10, Brussels, Belgium. Associa-
tion for Computational Linguistics.
Jelena Mitrovi´c, Bastian Birkeneder, and Michael
Granitzer. 2019.
nlpUP at SemEval-2019 task 6:
A deep neural language model for offensive lan-
guage detection. In Proceedings of the 13th Inter-
national Workshop on Semantic Evaluation, pages
722–726, Minneapolis, Minnesota, USA. Associa-
tion for Computational Linguistics.
Endang Wahyu Pamungkas and Viviana Patti. 2019.
Cross-domain and cross-lingual abusive language
detection: A hybrid approach with deep learning
and a multilingual lexicon. In Proceedings of the
57th Annual Meeting of the Association for Com-
putational Linguistics: Student Research Workshop,
pages 363–370.
Orestis Papakyriakopoulos, Simon Hegelich, Juan Car-
los Medina Serrano, and Fabienne Marco. 2020.
Bias in word embeddings.
In FAT* ’20: Confer-
ence on Fairness, Accountability, and Transparency,
Barcelona, Spain, January 27-30, 2020, pages 446–
457. ACM.
Fabio Poletto, Valerio Basile, Manuela Sanguinetti,
Cristina Bosco, and Viviana Patti. 2020. Resources
and Benchmark Corpora for Hate Speech Detection:
a Systematic Review.
Language Resources and
Evaluation, 54(3):1–47.
Marco Polignano, Pierpaolo Basile, Marco de Gem-
mis, and Giovanni Semeraro. 2019.
Hate speech
detection through alberto italian language under-
standing model.
In Proceedings of the 3rd Work-
shop on Natural Language for Artiﬁcial Intelligence
co-located with the 18th International Conference
of the Italian Association for Artiﬁcial Intelligence
(AIIA 2019), Rende, Italy, November 19th-22nd,
2019, volume 2521 of CEUR Workshop Proceedings.
CEUR-WS.org.
Manoel Horta Ribeiro, Pedro H Calais, Yuri A Santos,
Virg´ılio AF Almeida, and Wagner Meira Jr. 2018.
Characterizing and detecting hateful users on twit-
ter.
In Twelfth International AAAI Conference on
Web and Social Media.
Marian-Andrei Rizoiu, Tianyu Wang, Gabriela Fer-
raro, and Hanna Suominen. 2019.
Transfer learn-
ing for hate speech detection in social media. arXiv
preprint arXiv:1906.03829.
Maarten Sap, Dallas Card, Saadia Gabriel, Yejin Choi,
and Noah A. Smith. 2019. The risk of racial bias
in hate speech detection.
In Proceedings of the
57th Annual Meeting of the Association for Com-
putational Linguistics, pages 1668–1678, Florence,
Italy. Association for Computational Linguistics.

--- Page 8 ---

24
Gudbjartur Ingi Sigurbergsson and Leon Derczynski.
2020.
Offensive Language and Hate Speech De-
tection for Danish.
In Proceedings of the 12th
Language Resources and Evaluation Conference.
ELRA.
Steve Durairaj Swamy, Anupam Jamatia, and Bj¨orn
Gamb¨ack. 2019.
Studying generalisability across
abusive language detection datasets.
In Proceed-
ings of the 23rd Conference on Computational Nat-
ural Language Learning (CoNLL), pages 940–950,
Hong Kong, China. Association for Computational
Linguistics.
Zeerak Waseem, Thomas Davidson, Dana Warmsley,
and Ingmar Weber. 2017. Understanding abuse: A
typology of abusive language detection subtasks. In
Proceedings of the First Workshop on Abusive Lan-
guage Online, pages 78–84.
Zeerak Waseem and Dirk Hovy. 2016. Hateful sym-
bols or hateful people? predictive features for hate
speech detection on twitter. In Proceedings of the
NAACL Student Research Workshop, pages 88–93,
San Diego, California. Association for Computa-
tional Linguistics.
Michael Wiegand, Josef Ruppenhofer, Anna Schmidt,
and Clayton Greenberg. 2018. Inducing a lexicon
of abusive words–a feature-based approach. In Pro-
ceedings of the 2018 Conference of the North Amer-
ican Chapter of the Association for Computational
Linguistics: Human Language Technologies, Vol-
ume 1 (Long Papers), pages 1046–1056.
Yi Yang, Mark Christopher Siy UY, and Allen Huang.
2020. Finbert: A pretrained language model for ﬁ-
nancial communications.
Marcos Zampieri, Shervin Malmasi, Preslav Nakov,
Sara Rosenthal, Noura Farra, and Ritesh Kumar.
2019. SemEval-2019 task 6: Identifying and catego-
rizing offensive language in social media (OffensE-
val). In Proceedings of the 13th International Work-
shop on Semantic Evaluation, pages 75–86, Min-
neapolis, Minnesota, USA. Association for Compu-
tational Linguistics.
Appendix A
Subreddit
Number of posts
apewrangling
5
beatingfaggots
3
blackpeoplehate
16
chicongo
15
chimpmusic
35
didntdonufﬁns
22
fatpeoplehate
1465531
funnyniggers
29
gibsmedat
24
hitler
297
holocaust
4946
kike
1
klukluxklan
1
milliondollarextreme
9543
misogyny
390
muhdick
15
nazi
1103
niggas
86
niggerhistorymonth
28
niggerrebooted
5
niggerspics
449
niggersstories
75
niggervideos
311
niglets
27
pol
80
polacks
151
sjwhate
10080
teenapers
23
whitesarecriminals
15
A.1: Distribution of messages per banned community
composing the RAL-E dataset.
Profanity
Frequency
fucking
52,346
shit
49,012
fuck
44,627
disgusting
15,858
ass
15,789
ham
13,298
bitch
10,661
stupid
9,271
damn
7,873
lazy
7427
A.2: Top 10 profanities in RAL-E dataset.
Pre-processing before pre-training

--- Page 9 ---

25
• all users’ mentions have been substituted with
a placeholder (@USER);
• all URLs have been substituted with a with a
placeholder (URL);
• emojis have been replaced with text (e.g.
→:pleading face:) using Python
emoji package;
• hashtag symbol has been removed from hasth-
tags (e.g. #kadiricinadalet →kadiricinadalet);
• extra blank spaces have been replac§ed with
a single space;
• extra blank new lines have been removed.
Appendix B
Pre-processing before ﬁne-tuning
For each
dataset, we have adopted minimal pre-processing
steps. In particular:
• all users’ mentions have been substituted with
a placeholder (@USER);
• all URLs have been substituted with a with a
placeholder (URL);
• emojis have been replaced with text (e.g.
→:pleading face:) using Python
emoji package;
• hashtag symbol has been removed from hasth-
tags (e.g. #kadiricinadalet →kadiricinadalet);
• extra blank spaces have been replaced with a
single space.
Hyperparameter
Value
Learning rate
1e-5
Training Epoch
5
Adam epsilon
1e-8
Max sequence length
100
Batch size
32
Num. warmup steps
0
A.3: Hyperparamters for ﬁne-tuning BERT and Hate-
BERT.

```
