Heliyon 9 (2023) e18647

Contents lists available at ScienceDirect

Heliyon
journal homepage: www.cell.com/heliyon

Review article

Hate speech and abusive language detection in Indonesian social
media: Progress and challenges
Muhammad Okky Ibrohim a,∗ , Indra Budi b
a
b

Dipartimento di Informatica, Università degli Studi di Torino, Italy
Faculty of Computer Science, Universitas Indonesia, Indonesia

A R T I C L E

I N F O

Keywords:
Hate speech
Abusive language
Indonesian social media

A B S T R A C T
Nowadays Hate Speech and Abusive Language (HSAL) have spread extensively over social media.
The easy use of social media allows people to abuse the media to spread HSAL. Hate speech
and abusive language in social media must be detected because they can trigger conﬂict among
citizens. Not only in social media, but HSAL also often trigger conﬂict in real life. In recent years,
many scholars have researched HSAL detection in various languages and media. However, there
are still many tasks on HSAL detection that need to be done to develop a better HSAL detection
system. This paper discusses a summary of Indonesian HSAL detection research, conducted by
utilizing the Kitchenham systematic literature review method. Based on our summary, we found
that most Indonesian HSAL research still uses the classic machine-learning approach with classic
text representation features that experimented on the Twitter text dataset. We also found several
challenges and tasks that need to be addressed to build a better HSAL detection system in
Indonesian social media that can detect the hate speech target, category, and levels; and the
hate speech buzzer, thread starter, and fake account spreader.

1. Introduction
The ease of using social media should bring enormous beneﬁts to people’s lives. People can easily look for any information and
communicate with each other using social media. Unfortunately, some people on the internet (netizens) do not use social media
wisely. Nowadays, some netizens often use their social media to spread HSAL [5,25].
As a country that has a huge number of social media users,1 Indonesia has a serious problem of HSAL spreading on social media.
In 2017 alone, Polri2 has handled 3,325 hate speech cases, where this number increased 44.99% from the previous year, which
amounted to 1,829 cases.3 To solve this problem, many Indonesian scholars have studied HSAL detection in Indonesian social media.
However, most of the HSAL detection research on Indonesian social media is currently just focused on the model-building to detect
whether a text contains hate speech or abusive language or not [25]. Hate speech and abusive language problems cannot be dealt
with immediately by only detecting whether a text contains hate speech and abusive language or not.

* Corresponding author.
1
2
3

E-mail addresses: muhammadokky.ibrohim@unito.it (M.O. Ibrohim), indra@cs.ui.ac.id (I. Budi).
https://www.statista.com/statistics/247938/number-of-social-network-users-in-indonesia/.
Indonesian national police, see: https://www.polri.go.id/.
https://news.detik.com/berita/d-3790973/selama-2017-polri-tangani-3325-kasus-ujaran-kebencian.

https://doi.org/10.1016/j.heliyon.2023.e18647
Received 5 June 2022; Received in revised form 20 July 2023; Accepted 24 July 2023
Available online 28 July 2023
2405-8440/© 2023 Published by Elsevier Ltd.
(http://creativecommons.org/licenses/by-nc-nd/4.0/).

This

is

an

open

access

article

under

the

CC

BY-NC-ND

license

Heliyon 9 (2023) e18647

M.O. Ibrohim and I. Budi

Komnas HAM4 [30] explains that hate speech can be targeted on a person or group based on several inherent hate speech
categories such as religion, race or gender. Moreover, hate speech can also be divided into several levels such as weak, moderate, and
strong hate speech [30,52]. The hate speech target, category, and level are required to be detected to help the agency when deciding
which hate speech case needs to be prioritized to address [25].
In this era of free expression, people often spread hate speech accompanied by abusive language [16]. Hate speech accompanied
by abusive language needs to be detected quickly since this type of hate speech often triggers conﬂict among citizens because the use
of abusive language can easily oﬀend people. Although the use of abusive language is not always used to oﬀend people (just for jokes
or expressions of awe/familiarity [56,51]), the use of abusive language in social media can still be dangerous since it can trigger
misunderstandings that lead to conﬂict among netizens. Moreover, the use of abusive language in social media can lead children and
adolescents to learn abusive language in social media they have previously used [13].
Despite Indonesia being one of the most social media users (ranking 4th in the world based on Statista5 ) and there are often
online HSAL cases, Indonesian HSAL detection research is still very less compared to other languages, especially when compared to
English as the major language. Moreover, most Indonesian HSAL research detection still uses old-fashion models that may not have
as good performance as compared to the current state-of-the-art method. Therefore, it is needed to explore what has already been
done and what needs to do in Indonesian HSAL detection research compared to research on other languages, especially compared to
English as the major language.
This paper discusses a summary of HSAL detection research on Indonesian social media by collecting papers about HSAL detection
in the Indonesian language from reputable publication databases to create a summary of that using the Kitchenham framework [29].
In general, the contributions of this paper include:
• Analyze what HSAL deﬁnition is used by the previous works in conducting Indonesian HSAL detection research.
• Analyze what tasks have been addressed and what method has been used to deal with the HSAL problem in Indonesian social
media.
• Analyze what tasks need to be addressed and what method needs to be tried to solve deal with the speech and abusive language
problem in Indonesian social media.
In short, this paper is organized as follows. Section 2 discusses the related works of HSAL detection systematic review research.
Section 3 discusses Indonesian HSAL. Section 4, we explain how we select the papers to conduct a summary of current research
on Indonesian HSAL detection. Section 5 discusses the summary of current research on HSAL in Indonesian social media. Based on
Section 5, we discuss the challenge on hate speech and abusive language detection in Indonesian social media in Section 6. Finally,
we discuss the conclusions and future works of this paper in Section 7.
2. Related works
Hate speech is an expression (both direct or indirect) of a person or group that contains hatred based on some factors inherent
to that person or group, e.g., religion, race, ethnicity, gender, sexual orientation, and physical/disability [30]. It can be spread in
several forms, including the act of humiliation, derision, slander, sedition, and provocation. Acts of spreading hate speech can trigger
acts of discrimination against a person or group. Even worse, if anarchist social conﬂicts are not dealt with immediately, this conﬂict
can lead to genocidal acts, as happened in Rwanda [47].
In this social media era, people often spread hate speech accompanied by abusive language. According to [56], abusive language
is an utterance/expression that contains abusive/dirty words/phrases. Although not all abusive language means hate speech, the use
of abusive language in social media is often misused and triggers a conﬂict.
In recent years, many researchers have conducted much research to ﬁnd suitable methods how to detect online HSAL across
language, media type, and platform. Each research usually focuses on a particular language, media type, and platform. To summarizes
the existing research and ﬁnd a suitable model that ﬁts a speciﬁc language, some researchers conducted a systematic literature review.
In 2020, [36] conducted a systematic review using the Kitchenham framework to explore and analyze existing hate speech dataset
resources across languages and media types. They analyzed 5 dimensions including type, topical focus, data source, annotation, and
the language of the dataset. In that survey, they only focused on analyzing the dataset without analyzing the model used by existing
hate speech detection researchers. Next, in 2022, [6] conducted a systematic review to explore and analyze existing methods and
datasets that have been used by previous works in hate speech detection research. In this case, despite [6] analyzing hate speech
detection research across languages, they only focused on hate speech detection research that plays on text datasets.
To the best of our knowledge, we do not ﬁnd a survey paper that explores and analyze existing HSAL detection methods and
datasets across media types (text, speech/audio, image, and video) in a speciﬁc country. Given the fact that diﬀerent countries may
have diﬀerent contexts of HSAL trends that may aﬀect the modeling technique needs [24], a survey paper on HSAL detection for a
speciﬁc country is needed to ﬁnd a suitable method that needs to be developed in the future. In [42], [42] conducted a systematic
review to explore existing methods and datasets that have been used in Indonesian hate speech detection research. However, they

4
Komisi Nasional Hak Asasi Manusia (Komnas HAM) is an independent institution that functions to carry out studies, research, counseling, monitoring, and
mediation of human rights in Indonesia. See https://www.komnasham.go.id/index.php/about/1/tentang-komnas-ham.html.
5
https://www.statista.com/statistics/278341/number-of-social-network-users-in-selected-countries/.

2

Heliyon 9 (2023) e18647

M.O. Ibrohim and I. Budi
Table 1
Example of Indonesian hate speech and abusive language.
No

Utterance

Label
Hate
Speech

Abusive
Language

1

Buddha Myanmar
emang babi!
(Myanmar Buddhist
is a pig!)

Yes

Yes

2

Bangsat! Dasar Cina
kocak lu coy wkwk
(Bastard! You‘re a
funny Chinese bro haha)

No

Yes

3

Saya benci muslim, mereka
suka membunuh orang!
(I hate Muslims, they
like killing people!)

Yes

No

4

Sesama manusia, muslim &
buda harus hidup damai :)
(As human beings, Muslim
and Buddhist must live in
peace :) )

No

No

only analyze research that uses text datasets. Moreover, they only make a summary of existing without analyzing the challenge
that needs to be tackled in the future to build a suitable Indonesian HSAL detection model/system. In this paper, we conducted
a systematic review using the Kitchenham framework like [36] did to explore what Indonesian HSAL research has been done and
analyze what needs to be tackled in the future to build a suitable HSAL detection model/system for Indonesian social media across
media types.
3. Indonesian hate speech and abusive language
As mentioned in Section 1, Indonesia is one of the biggest social media users and many of them often use their social media
to create and spread hate speech. Similar to other countries, many Indonesian people often include abusive language when posting/sharing hate speech on their social media. In Indonesia, abusive/dirty words/phrases commonly came from something that is
considered bad, disgusting, and too taboo to be ordinarily mentioned in public. [56,1].
Although hate speech is often accompanied by abusive language, not every utterance/expression that contains abusive/dirty
words/phrases constitutes hate speech. It means that abusive language is not always also hate speech. Abusive language is often
used as jokes and the form of informal conversations to express aﬃnity [56,51]. Moreover, abusive language is also used to express
a sense of wonder/astonishment at an event/phenomenon [56]. Conversely, hate speech is also not always accompanied by abusive
language. Examples of Indonesian HSAL can be seen in Table 1. These examples are given by a linguist expert6 following the HSAL
deﬁnition from the FGD results conducted by [25].
In Table 1, Example 1 is an example of hate speech and abusive language since this utterance is a hate expression directed at a
Myanmar Buddhist using the Indonesian abusive word “babi” (pig). Example 2 is abusive language but not an example of hate speech.
Although the utterance in Example 2 contains the Indonesian abusive word “bangsat” (bastard) and mentions Chinese ethnicity, this
utterance is just a closeness expression from someone about his close friend who is true of Chinese ethnicity. Example 3 is hate
speech but not abusive language example. Even though the utterance in Example 3 does not contain abusive/dirty words/phrases,
this utterance is an incitement to the slander that Muslim citizens like to kill people. Lastly, Example 4 is normal speech, which is
an utterance that does not contain hate speech or abusive language. This is because the utterance in Example 4 is a pure message of
peace.
Besides hate speech has a speciﬁc target, it also has a speciﬁc category [30] and level [30,52]. In 2019, [25] conducted a
Focus Group Discussion (FGD) with the staﬀ of Direktorat Tindak Pidana Siber Badan Reserse Kriminal Kepolisian Negara Republik
Indonesia (Bareskrim Polri)7 to compile a valid deﬁnition and example of the Indonesian HSAL hierarchy. The HSAL hierarchy from
[25] can be seen in Fig. 1.
Based on Fig. 1, we can see that hate speech has a speciﬁc target, category, and level, as noticed in [30]. In this hierarchy, [25]
deﬁnes that hate speech must have a speciﬁc target, whether targeted at a person or group. If an utterance contains a hate/frustration
expression but is not targeted at a person or group, then the sentence is just an ordinary swear/curse sentence and is not categorized
as hate speech. For example, the sentence “Bangsat, ini motor butut banget sih!” (Bastard, this is a really worn motorbike!) is just

6
7

Sociolinguist master student graduates.
The agency responsible for investigating cybercrime in Indonesia. See: https://humas.polri.go.id/category/satker/cyber-crime-bareskrim-polri/.
3

Heliyon 9 (2023) e18647

M.O. Ibrohim and I. Budi

Fig. 1. Indonesian hate speech and abusive language hierarchy [25].

Table 2
Example of Indonesian hate speech hierarchy.
No

Hate Speech Utterance

Target

Category

Level

1

Jokowi itu Bangsat, presiden yang tidak bisa apa-apa.
(Jokowi is a Bastard, a president who can’t do anything.)

Individual

Other invective/slander

Weak

2

Nikita emang lonte autis!
(Nikita is an autistic bitch!)

Individual

Physical/disability &
Gender/sexual orientation

Weak

3

Nikita emang lonte autis! Ayo bakar rumahnya dan
usir dia dari desa ini!
(Nikita is an autistic bitch! Let’s burn her house and
kick her out of this village!)

Individual

Physical/disability &
Gender/sexual orientation

Strong

4

Saya benci muslim, mereka suka membunuh orang!
(I hate Muslims, they like killing people!)

Group

Religion/creed

Moderate

5

“Segera koordinasikan kekuatan massa muslim ...
utk segera mengepung kedutaan Myanmar ...
usir Dubes dan Orang Budha Biadab yang Rohingya
itu dari Indonesia!!!”
(“Immediately coordinate the mass power of the Muslims ...
to immediately surround the Myanmar embassy ...
drive out the Bastard Ambassador and Buddhist that
oppressive Rohingya from Indonesia!!!”)

Group

Religion/creed &
Race/ethnicity

Strong

an ordinary swear/curse sentence since the target of swear/curse in this sentence is a motorcycle, not a human (both individual
or group). For the hate speech category, [25] divide the hate speech category into ﬁve categories, which are 1). Religion/Creed;
2). Race/ethnicity; 3). Physical/disability; 4). Gender/sexual orientation; and 5). Other invective/slander. Notice that hate speech can be
categorized into several categories at once except Category 5. In other words, hate speech under Categories 1–4 cannot be categorized
as Category 5, and vice versa. Several researchers categorized an invective/slander speech that does not pertain to religion/creed,
race/ethnicity, physical/disability, and gender/sexual orientation as ordinary oﬀensive speech (not a hate speech) [51]. In this
hierarchy, [25] categorized an invective/slander speech since this speech can trigger discrimination and social conﬂict. For the hate
speech level, [25] divides the hate speech level into three levels, which are weak hate speech, moderate hate speech, and strong hate
speech. Weak hate speech is swearing/slanderous expressions targeted at a person without containing an incitement/provocation that
can trigger a real-world conﬂict. Moderate hate speech is a swearing or negative labeling/stereotyping expression aimed at a group
without an incitement/provocative act that can trigger a real-world conﬂict. Meanwhile, strong hate speech is swearing or negative
labeling/stereotyping expression aimed at a person or group including incitement/provocative acts that can trigger a real-world
conﬂict. Examples of the Indonesian hate speech hierarchy can be seen in Table 2. Similar to the examples shown in Table 1, these
examples are given by a linguist expert following the HSAL categorization from the FGD results conducted by [25].
In Table 2, Example 1 is hate speech targeted at an individual that can be categorized as other invective/slander hate speech.
This example of hate speech is weak hate speech since it is targeted at an individual without containing an incitement/provocation
act. Example 2 is a variant of hate speech targeted at an individual with two hate speech categories—physical/disability marked
by “autis” (autistic) swear word and gender/sexual orientation which is marked by “lonte” (bitch) swear word As with Example 1,
Example 2 is a weak hate speech since this hate speech is targeted at an individual without containing an incitement/provocation
act. As in Example 2, Example 3 is a hate speech targeted at an individual which included physical/disability and gender/sexual
orientation hate speech categories. However, Example 3 is a strong hate speech since this hate speech contains a provocative call
4

Heliyon 9 (2023) e18647

M.O. Ibrohim and I. Budi
Table 3
Stages of paper selection.
Stages

Inclusion
Criteria

Exclusion
Criteria

Stage 1:
Initialization

-

More than ten
years publication

Stage 2:
Title & Abstract
Selection

Relevance
with query

Duplicate
publication

Stage 3:
Full Text
Selection

Meet the paper
quality criteria

Non experimental
research on Indonesian
hate speech or abusive
language detection

to burn the hate speech victim’s house and kick (drive out) the hate speech victim from the village. Example 4 is an example of
hate speech targeted at a group (Muslims) that is categorized as religion/creed hate speech. Despite this hate speech targeted at a
group, Example 4 is moderate hate speech since this hate speech does not contain an incitement/provocative act. Example 5 is a hate
speech targeted at a group (Myanmar people and Buddhists) with two hate speech categories that are religion/creed (since this hate
speech is targeted at Buddhists) and race/ethnicity (since this hate speech is targeted at Myanmar people). Example 5 is an example
of strong hate speech since this hate speech contains a provocative call that invites people (masses) to surround and drive out the
Myanmar embassy and Buddhists from Indonesia.
In this review, we found that not all Indonesian HSAL detection previous research follows the deﬁnition from [30] or Bareskrim
Polri as the human rights organization and authority that handles hate speech problems in Indonesia like [25] did. Many of them
are using the deﬁnition from other sources like from the social media platform where their dataset comes from or from the other
previous works that explore HSAL detection in diﬀerent languages. We further analyze this ﬁnding as our review result in Subsection
5.1.
4. Paper selection process
In this paper, we have two research questions, which are:
1. RQ1: What studies have been done to address HSAL problems in Indonesian social media?
2. RQ2: What are the challenges around addressing HSAL problems in Indonesian social media?
In making a summary to answer these two research questions, we did a Systematic Literature Review (SLR) using the Kitchenham
method [29] that in general can be divided into a paper selection process and paper summary process.
In this paper, we use ﬁve top computer science research databases including IEEE Xplore,8 ACM Digital Library,9 Springer Link,10
Science Direct,11 and ACL Anthology12 ; and one computer science databases indexer which is Scopus13 as the SLR resource.
In determining the search query for the SLR process, ﬁrst of all, we undertook a preliminary search using two queries that are: hate
speech Indonesia and abusive language Indonesia. We did a quick review of papers from this preliminary search, from which we see that
both hate speech and abusive language have some other terms and sub-tasks. As described before in Section 3, some researchers deﬁne
a swear/slander speech that does not pertain to religion/creed, race/ethnicity, physical/disability, and gender/sexual orientation as
oﬀensive speech. Moreover, hate speech research has a subtask area such as hate code detection. Meanwhile, abusive language also
has other terms including dirty words and rude words. Therefore, we decide that also search for oﬀensive language, hate code, dirty
words, and rude words. We used an advanced Boolean search when searching for papers for SLR sources in each computer science
research database and the indexes that we chose. The Boolean keyword that we used in this research was: (hate speech OR abusive
language OR oﬀensive language OR hate code OR dirty words OR rude words) AND Indonesia. To make sure that the SLR papers are
current, we just analyzed texts published in the last ten years (i.e., 2010-2021). We searched for papers using those keywords in
research publishers and indexes which had been determined in February 4st , 2021. In general, we carried out three steps in selecting
the SLR papers that can be seen in Table 3.
Based on those three steps of selection that can be seen in Table 3, we arrived at a total of 27 papers to be analyzed in this
research. The statistics of selected papers can be seen in Table 4.

8
9
10
11
12
13

https://ieeexplore.ieee.org/.
https://dl.acm.org/.
https://link.springer.com/.
https://www.sciencedirect.com/.
https://www.aclweb.org/anthology.
https://www.scopus.com/.
5

Heliyon 9 (2023) e18647

M.O. Ibrohim and I. Budi
Table 4
Statistics of selected papers for each stage.
Source

Number of Selected Papers
Stage 1

Stage 2

Stage 3

IEEE Xplore

210

28

17

ACM
Digital Library

197

6

4

Springer Link

303

1

0

ACL
Anthology

75

3

1

Science Direct
Scopus

593
281

1
5

1
4

Total

1,659

44

27

From Table 4, we can see that we acquired many papers from Stage 1, but the number dropped in Stage 2. This happens because
of the partial match between the papers and the query given. We directly drop the duplicate papers and the papers that discuss HSAL
detection in non-Indonesian language based on their title and abstract. However, we continue into Stage 3 with papers that do not
mention a speciﬁc language in their title and abstract, in case they describe the use of the Indonesian language (either monolingual
or multi-lingual) on their hate speech and abusive research. Meanwhile, in Stage 3, we dropped most of the papers because they do
not conduct a relevant experiment and because they do not satisfy the paper quality criteria, for example, the paper does not explain
the research methodology and there is no clear indication of future research direction.
5. Current research on hate speech and abusive language detection in Indonesian social media
As described in Section 4, we got 27 papers to discuss in this research to get a summary of what current research exists on
Indonesian HSAL detection. The list of 27 selected papers can be seen in Table 5.
From Table 5, we can see that research about HSAL in Indonesian social media started with [32] in 2014. They researched
cyberbullying detection on Indonesian Twitter using a rule-based and association rule approach with a dictionary (word list) feature.
After 2014, research on Indonesian HSAL detection started to be developed again in 2017 by [5] and [18]. In general, we summarize
our ﬁndings about current research on the topic from 27 selected papers into ﬁve subsections including what HSAL deﬁnition was
used by the researchers, how the researchers built their dataset, and the method used in their research.
5.1. Deﬁnition
Based on a full-read analysis of the 27 selected papers, we found that, in general, the HSAL deﬁnition used in their research can
be divided into ﬁve sources which are from previous works combined with the deﬁnition from the social media platform’s rules and
policies, country rules/laws, sociolinguistic books, or a combination of them arrived at by utilizing a Focus Group Discussion (FGD).
Researchers who used deﬁnitions from previous works also used a deﬁnition from previous research on the same topic but with
a diﬀerent language dataset. For example, [5,50] using the hate speech deﬁnition from [55]. However, since the deﬁnition from
previous works usually just described the HSAL in general, researchers who used a deﬁnition from previous works usually combined
it with the deﬁnition derived from the social media platform’s rules and policies. For example, besides using a deﬁnition from [55],
[5] also used a deﬁnition of hate speech from Twitter rules and policies14 since the dataset they used in their research is from
Indonesian Twitter. From the social media platform’s rules and policies, we can get more detail on what social media posts and
comments are categorized as hateful and abusive content.
Since each country may have diﬀerent deﬁnitions and legal arrangements, some researchers who studied hate speech detection
used their hate speech rules/laws from their country. In Indonesia, the hate speech deﬁnition, rules, and laws are described in [37].
Examples that researchers used [37] as the hate speech deﬁnition basis for their research are [7] and [3]. In 2015, [30] further
describes the deﬁnition of hate speech that has been given in [37] since they found that many citizens were against those hate
speech rules. Many citizens oppose those hate speech rules since they worry that rules can threaten freedom of expression. Moreover,
citizens also
worry that rules will be used as a tool to silence criticism of the government. Therefore, [30] explains in-depth the hate speech
deﬁnition given in [37], including describing what speech (either direct or indirect) that is included as hate speech, and what speech
is included as not considered hate speech. For example, researchers who used [30] as the hate speech deﬁnition basis for their
research are [39,40,46].
While researchers used hate speech from previous works, social media platforms, or hate speech rules/laws, researchers usually
used sociolinguistics books for abusive language deﬁnition. For example, [33] and [1] used the abusive language deﬁnition and

14

https://help.twitter.com/en/rules-and-policies/twitter-rules.
6

Heliyon 9 (2023) e18647

M.O. Ibrohim and I. Budi

Table 5
List of Selected Papers.
No

Year

Paper

Method
(Model and Feature Extraction)

Best Performance

Novelty

1

2014

[32]

Model: FP-Growth, Association
Rule

-

Preliminaries research on hate speech detection in
Indonesian social media

2

2017

[5]

93.5% F-Measure using RFDT with
word unigram feature

- Build a valid dataset by reducing annotation bias
using 3 annotators per data schema that came from
diﬀerent backgrounds.
- Found that diﬀerent language maybe needs
diﬀerent feature extraction to ﬁgure out the
semantic of sentence

Male: 90% accuracy
Female: 76.68% accuracy

Preliminaries research on rude word detection on
speech dataset

67% F-Measure using SVM with POS
feature

Identify bullying actors: normal users, harmful
bullying actors, bullying actors and prospective
bullying actors

65.7% F-Measure using FastText with
word bigrams feature

Conduct hate speech detection research on
Instagram comments

Feature:
- Text: word embedding, word
list, POS, TFIDF, sentence
embedding
- Speech: pitch, MFCC,
INTERSPEECH 2009,
INTERSPEECH 2010

- Text: 83.62% F-Measure on wordlevel, 87.07% on sentence level,
using word embedding+3POS+word
list+sentence embedding
- Speech: 72.11% F-Measure using
INTERSPEECH 2010
- Multi-modal: 80.18% F-Measure using
word embedding+2FPOS +word list
+TFIDF +sentence embedding+MFCC

- Word level rude word detection on text
- Sentence level rude word detection on speech
- Trying to use multi-modal text+speech features

Model: LDA

-

Multilingual hate speech topic analysis

87.18% accuracy using SVM with data
preprocessing and TFIDF feature

- Build an interface to manage hate speech
detection
- Comparing performance between use
preprocessing or not

57.9% accuracy (average)

- Preliminaries research on hate speech detection
on image dataset
- Dataset was validated by local government
language institutions

- Three classes (distinguish oﬀensive or
not for abusive language label): 70.06%
F-Measure using NB with word unigram
+bigrams features
- Two classes (no distinguish oﬀensive
or not for abusive language label):
86.43% F-Measure using NB with
word unigram feature

- Analyze the challenge on abusive language
detection on Indonesian social media
- Distinguish abusive language into two classes
which are abusive but not oﬀensive and abusive
and oﬀensive

84.7% F-Measure using soft voting
ensemble

- Using ensemble method for hate speech detection
in Twitter
- Comparing performance between using balancing
dataset or not

96.2% F-Measure using FastText

Using deep learning approach for hate speech
detection

- Text: 87.98% F-Measure using
CBOW
- Speech: 72.49% F-Measure using
MFCC
- Multi-modal: 86.98% F-Measure using
CBOW +INTERSPEECH 2009

- Hate speech detection on speech using deep
learning approach
- Trying to use multi-modal text+speech features

Feature: Dictionary
Model: NB, SVM, LR, RFDT
Feature: word n-grams,
char n-grams, negative
sentiment lexicon

3

2017

[18]

Model: SVM
Feature: pitch value

4

2018

[34]

Model: SVM, kNN
Feature: POS

5

2018

[39]

Model: LR, RFDT, FastText
Feature: word n-grams,
character trigrams

6

7

2018

2018

[33]

[58]

Model: SVM

Feature: word n-grams
8

2018

[44]

Model: NB, DT, LR, SVM, kNN
Feature: hashing, TFIDF

9

2018

[3]

Model: LSA
Feature: term document matrix

10

2018

[1]

Model: NB, SVM, RFDT
Feature: word n-grams,
character n-grams

11

2018

[20]

Model: kNN, Maximum Entropy,
RFDT, SVM, NB
Feature: TFIDF

12

2018

[46]

Model: LSTM
Feature: word2vec, FastText

13

2018

[50]

Mode: LSTM
Feature:
- Text: word n-grams, TFIDF,
word embedding
- Audio: MFCC, INTERSPEECH
2009, INTERSPEECH 2010

(continued on next page)

7

Heliyon 9 (2023) e18647

M.O. Ibrohim and I. Budi

Table 5 (continued)
No

Year

Paper

14

2019

[40]

Method
(Model and Feature Extraction)

Best Performance

Novelty

Model: LR, SVM, NB, RFDT

80.71% F-Measure using LR with hate
code binary + hate code dictionary
feature

Using hate code as feature extraction

Feature: word n-grams, char
n-grams, sentiment and oﬀensive
lexicon, sentiment and oﬀensive
proportion

85% F-Measure using SVM with
TFIDF+character quadgrams+word
unigram+number of positive words
+number of oﬀensive word+proportion
of positive words +proportion of
oﬀensive words

Preliminaries research on hate speech detection
in long text

Model: ANN

96.8% accuracy

Using ANN for oﬀensive language detection
research

98.7% accuracy

Using ruled base formula applied on Ms. Excel to
annotate hate speech data

87% F-Measure using POS +TFIDF
feature

Using Maximum Entroppy for hate speech detection
research on Instagram coment

97.19% accuracy using POS +TFIDF
feature

Using DNN for hate speech detection research on
Instagram coment

83.68% F-Measure using FastText
feature

- Using deep learning approach for oﬀensive
language detection research on Indonesian Twitter
- Performance better from previous works in the
same dataset

- Non translated method: 76.95%
F-Measure using SVM with word
unigram+bigrams feature
- Translated without language
identiﬁcation method: 58.39%
F-Measure using SVM with word
unigram feature
- Translated with language
identiﬁcation method method: 65.16%
F-Measure using SVM with unigram
feature

- Compare translated and non-translated method for
multilingual dataset

66.12% accuracy for all labels, 77.36%
accuracy if without hate speech target,
category, and level labels

- Deﬁne valid deﬁnition abusive language and hate
speech (including the target, category, and level)
from book, law, and FGD result
- Built valid multi-label abusive language and hate
speech (including the target, category, and level)
dataset

68.43% accuracy using SVM with
unigram feature

- Using hierarchical approach
- Performance better than the previous works in the
same dataset

79.85% accuracy using LR with word
unigram+POS+emoji features

- Use emoji feature
- Performance better than the previous works in the
same dataset

Feature: TF-IDF, word bigrams

94.90% F-Measure for hate code
classiﬁcation using LR with abusive
code selimination

Preliminary research on hate code detection and
extraction

Model: RFDT, BiLSTM

76.12% accuracy when using RFDT

- Preliminary research in Indonesian hate speech
detection using pre-trained BERT model
- Analyzing hate speech label depedencies

74.88% accuracy when using SVM

- Normalizing English word in dataset by translating
them
- Did hyperparameter tuning on SVM model
- Try using CNN with DistilBERT

Feature: word n-grams,
char n-grams, hate code
lexicon
15

16

2019

2019

[7]

[49]

Model: LR, SVM, RFDT

Feature: word n-grams
17

2019

[4]

Model: NB
Feature: word unigram

18

2019

[19]

Model: Maximum Entropy
Feature: POS, TFIDF

19

2019

[41]

Model: DNN
Feature: POS, TFIDF

20

2019

[26]

Model: LSTM
Feature: word2vec, FastText

21

2019

[24]

Model: NB, SVM, RFDT
Feature: word n-grams,
character n-grams

22

2019

[25]

Model: NB, SVM, RFDT
Feature: word n-gram, character
n-grams, orthography, sentiment
and abusive lexicon

23

2019

[38]

Model: NB, SVM, RFDT
Feature: word n-grams,
character n-grams

24

2019

[27]

Model: LR, SVM, RFDT
Feature: word n-gram,
word2vec, POS, and Emoji

25

26

2020

2020

[17]

[22]

Model: LR, NB, RFDT, LIME

Feature: TF-IDF, BERT
27

2020

[21]

Model: SVM, CNN
Feature: TF-IDF, DistilBERT

8

Heliyon 9 (2023) e18647

M.O. Ibrohim and I. Budi
Table 6
Dataset Type and Source used by Selected Papers.
Dataset Type

Dataset Source

Papers

Text

Twitter

Facebook
Instagram
YouTube
LINE
Sarahah Message

[5], [25], [1], [34], [39], [44], [3]
[20], [20], [46], [50], [40], [4]
[26], [24], [38], [27] [17], [22], [21]
[44], [50], [7]
[39], [44], [19], [41]
[50], [44]
[50]
[58]

Manually Recording
Twitter

[18], [33], [50]
[3]

Speech
Image

characteristics from [56].15 We also found that some researchers use another term to express abusive language. For example, [50]
uses “rude words” terms and [18] using “rude swear words terms”.
Although some resources describe the HSAL deﬁnition, [25] found that deﬁnition and example for hate speech target, category,
and level. In [30], the deﬁnition and example of hate speech is explained clearly, but they do not explain deeper about the hate
speech target, category, and level (just giving an explanation or example), even though the hate speech detection system can classify
the hate speech target, level, and category needed to help the hate speech authority to choose what hate speech case needs to be
prioritized due to their human resource limitation. To get a valid deﬁnition and example of hate speech target, category, and level,
[25] conducted an FGD with Staﬀ of the Direktorat Tindak Pidana Siber Bareskrim Polri16
5.2. Dataset
Based on Table 5, most of the researchers who studied Indonesian HSAL are using text datasets. In full, the dataset type and
source from each selected paper in Table 5 can be seen in Table 6.
From Table 6, we can see that the most-used social media dataset is the Twitter dataset. For research on Indonesian HSAL
detection using a speech dataset, the research is initialized by [18] and followed by [33,50]. Despite the dataset used by [18], [33],
and [50]not coming from a social media dataset (they build the speech dataset by manual recording), these studies can be used as
a reference for research on social media speech dataset like the speech dataset from YouTube video. Last, for hate speech detection
using an image dataset, currently, the research has been done by [3].
For the language, we found that almost all research on HSAL in Indonesian social media purely uses datasets in the Indonesian
language (monolingual), regardless of using a text, speech, or image dataset. The only studies that combine datasets from another
language for Indonesian HSAL are [58,24].
Last, for the data annotation strategy, we found that researchers were using several diﬀerent approaches. Annotating HSAL is
quite challenging since these tasks are quite subjective and can bring up bias on annotation [5,25]. To reduce the annotation bias,
some researchers used multiple annotators in annotating their datasets. Usually, researchers use a minimum of three annotators to
annotate one piece of data. The use of the three annotators strategy can be divided into two scenarios. First, researchers used the
same three annotators for annotating the whole dataset [39]. The second scenario uses several annotators, and then for each piece
of data to be annotated, we choose three annotators to annotate it randomly [5,1,25]. Furthermore, to further reduce bias, some
researchers also considered the annotators’ background including sex, age, job, ethnicity, and religion [5,1,25].
To decide the ﬁnal label when using multiple annotators, we found that there are two techniques used by the researchers, i.e.,
100% agreement [5,39,50,1,25] and majority voting [25]. In [25], they annotated the dataset in two stages. First, they annotated
whether a tweet contained hate speech or not, and contained abusive language or not. In this ﬁrst stage, they used 30 annotators
from diﬀerent backgrounds, where each tweet was annotated by 3 annotators and the ﬁnal label was decided using 100% agreement
technique. In the second stage, they annotated the hate speech target, category, and level using the same 3 annotators for the whole
dataset, where the ﬁnal label was decided by majority voting technique.
Besides using multiple annotators, there is a technique to reduce bias in annotation results. In [3], their dataset was annotated
by a linguistics expert to reduce the annotation bias. The linguistics expert came from Badan Pengembangan dan Pembinaan Bahasa
(Badan Bahasa) Jawa Barat.17 Furthermore, to reduce annotator resources, [4] uses a rule-based approach to annotate the hate
speech data. Their approach to annotating the hate speech data is quite interesting since some text data is admittedly easier to
annotate as hate speech and there is no bias. For example, if a text contains an abusive word combined with a provocative word,
people will agree that the text is hate speech.

15

[33] using the 2006 version of [56] while [1] used the 2010 version.
Direktorat Tindak Pidana Siber Badan Reserse Kriminal Kepolisian Negara Republik Indonesia (Bareskrim Polri) is a directorate of the Indonesian national police
in charge of managing and carrying out the function of investigating cybercrimes in Indonesia.
17
Language Center Oﬃce of West Java Province Government.
16

9

Heliyon 9 (2023) e18647

M.O. Ibrohim and I. Budi

5.3. Methods
Since using diﬀerent types of datasets, methods used by researchers varied. This subsection discusses methods used by researchers
in researching Indonesian HSAL detection including the preprocessing technique and then the models and features extraction.
5.3.1. Preprocessing technique
As described before, the dataset types that have been used in Indonesian HSAL detection research include text, speech, and
images. However, for the speech dataset, [18], [33], and [50] do not use audio preprocessing (e.g., compression, ﬁltering, panning
and lengthening, noise cancellation, etc.) and directly conducting a features extraction process.
For the text dataset, the preprocessing step that all researchers did was case folding. Case folding often done by researchers
is lowercase folding, i.e., transforming the alphabet in the dataset into lowercase style to reduce the writing variation. The next
processing step that all researchers did it was non-necessary character removal involving punctuation removal and Uniform Resource
Locator (URL) removal. Especially for the Twitter dataset, researchers also usually remove the Twitter username. Besides removing
the punctuation, URL, and Twitter user, researchers also remove the stop words in the preprocessing step. Since people’s texting
behavior in social media is often quite irregular (especially for Twitter because of the limited number of characters), some researchers
did text normalization to convert Out of Vocabulary (OOV) words into formal ones. For example, [5,1,25] use a dictionary to normalize
the OOV words. Moreover, some researchers also deployed a stemming process to reduce computational runtime. For example, [25]
using Nazief-Adriani Algorithm [2] implemented Sastrawi Library.18 Furthermore, for handling multilingual datasets, [58] and [24]
translated the text into a speciﬁc language before doing the standard text processing which was described before.
For image datasets, [3] converted their image into text and then did text classiﬁcation to detect whether an image contained
hate speech or not. In [3], they convert the image into text by extracting the text contained in the image using Optical Character
Recognition (OCR). After getting the text from the OCR process, [3] did standard text processing by removing symbols and stop
words.
As shown in Table 5, most of the datasets used by the researchers are quite imbalanced. To avoid a negative result because
of the imbalanced dataset, some researchers have carried out a balancing process in the data preprocessing stage. The common
method used by researchers to make the dataset more balanced is using a data re-sampling technique, either random oversampling,
undersampling, upsampling, and downsampling, or a special technique like Synthetic minority over-sampling technique (SMOTE)
[12].
5.3.2. Models and features extraction
As shown in 5, we can see that, in general, the current methods to detect and analyze Indonesian hate speech and abusive
language can be divided into two methods which are the unsupervised method and the supervised method. For the unsupervised
method, [32] used FP-Growth and association rule models to analyze the cyberbullying patterns, while [58] used Latent Dirichlet
Allocation (LDA) to analyze the coarse and bullying categorization.
While the unsupervised method is used to analyze the hate speech and abusive language patterns and topics, researchers used
the supervised method to directly classify whether content (text, speech, or image) contained hate speech and abusive language or
not. Researchers studying Indonesian hate speech and abusive language detection have tried several classiﬁcation methods, which,
in general, can be divided into two categories of approach i.e., a classic machine-learning approach and a deep-learning approach.
For text classiﬁcation using the machine-learning approach, researchers have used several models to classify whether a text
contain hate speech and abusive language or not including Naive Bayes (NB) [5,44,1,20,40,4,24,25,38], Support Vector Machine
(SVM) [5,34,44,1,20,40,7,24,25,38,27], Logistic Regression (LR) [5,39,44,40,7,27], Decision Tree (DT) [44], Random Forest Decision
Tree (RFDT) [5,39,1,20,7,24,25,38,27], k-Nearest Neighbor (kNN) [34,44], Latent Semantic Analysis (LSA) [3], Maximum Entropy
[20,19], and Artiﬁcial Neural Network (ANN) [49]. These machine-learning models are usually combined with several text features
including word n-grams [5,39,1,40,7,49,4,24,25,38,27], character n-grams [5,39,1,40,7,24,25,38], dictionary lexicon (sentiment [5,
7,25], abusive [25], and hate code lexicon [40]), term document matrix [3], Term Document Matrix × Inverse Document Frequency
(TFIDF) [33,44,20,19,41], hashing [44], Part of Speech (POS) [34,33,19,41], orthography [25], emoji [27], and word embedding
(word2vec and FastText) [39,33,27].
Meanwhile, for detecting hate speech and abusive language in text using the deep-learning approach, researchers have been trying
to use several deep-learning models including Deep Neural Network (DNN) [41] and Long Short Term Memory (LSTM) [46,50,26].
These deep-learning models are combined with several features like POS [41], TFIDF [41], and word embedding (word2vec and
FastText) [46,50,26].
As with researchers who researched the text dataset, researchers who researched the speech dataset also used machine learning
and the deep-learning approach. In [18], they use the SVM model combined with the Pitch Value feature. This is the same as
[18], [33] also used SVM but with diﬀerent feature extraction. In [33], they use pitch, Mel-Frequency Cepstral Coeﬃcients (MFCC),
INTERSPEECH 2009, and INTERSPEECH 2010 features. Lastly, [50] use LSTM combined with MFCC, INTERSPEECH 2009, and
INTERSPEECH 2010 features.

18

https://github:com/har07/PySastrawi.
10

Heliyon 9 (2023) e18647

M.O. Ibrohim and I. Budi

6. Challenge on hate speech and abusive language detection in Indonesian social media
Based on Section 5 discussions, we can see that there are still many challenges in building a hate speech and abusive language
detection system for Indonesian social media. In general, the challenge can be divided into three groups which are: the challenge of
how to build a valid and open dataset, the challenge of how to build a robust model for hate speech and abusive language detection
in Indonesian social media, and challenges of the tasks that have not been tackled by the current researchers to make a better system
that does not just detect whether a post or comment is hate speech or not.
6.1. Challenge 1: building valid and open dataset
Building a valid dataset for hate speech and abusive language detection is quite challenging since this task is highly subjective
[5]. To reduce the subjectivity, we need to use a valid deﬁnition of hate speech and abusive language that can be obtained using
country rules/laws, handbooks oﬃcially published by government agencies, and sociolinguistics books.
To build an Indonesian hate speech dataset, researchers can refer to the hate speech deﬁnition from [37,30]. If researchers want to
annotate the hate speech target, category, and level, they can refer to the example from [25]. Meanwhile, if researchers want to build
an Indonesian abusive language dataset, they can refer to [56]. Moreover, if researchers want to deﬁne a new detail/class on hate
speech target, category, and level or new detail/class on abusive language, researchers can do an FGD with a hate speech/cybercrime
handler authority and/or linguistic expert as done by [25].
As mentioned in the opening of this section, hate speech and abusive language is a highly subjective task that makes the interpretation of one person often diﬀerent from the others, where this also may become the reason why there are many cases of
false accusations related to hate speech in Indonesia’s information law.19 Therefore, an FGD with a hate speech/cybercrime handler
authority (Bareskrim Polri), linguistic expert, and all stakeholders who are concerned with hate speech detection (e.g. Komnas HAM)
are highly suggested to get a better understanding of hate speech so that the model can learn the labeled data training better.
Besides a valid deﬁnition, we need a special technique in the annotation process to reduce annotation bias. The annotation process
can be done either by crowdsourcing or using a linguistic expert. If researchers want to annotate their dataset by crowdsourcing,
they need to use multiple annotators (usually using a minimum of three annotators for each piece of annotated data). To get better
in reducing the annotation bias, researchers can use multiple annotators who come from diﬀerent backgrounds such by sex, age, job,
ethnicity, and religion as done by [5,1,25]. Meanwhile, if researchers want to annotate their dataset by using a linguistics expert,
they can collaborate with government language agencies (either central or regional) as done by [3].
In choosing the annotators, researchers should also be aware of the dataset language. Because of the internet freedom of expression, even if we only crawl/scrape in the scope of Indonesia maybe it could be that in our dataset there is a language other than the
Indonesian language (either multilingual or even code-mixed). For example, Indonesian netizens often mix the Indonesian language
with English in social media interaction [43]. Moreover, Indonesian netizens also often use abusive words/phrases from a language
other than the Indonesian language (not only English) when expressing abusive language in social media [1]. Furthermore, since
Indonesia has so many local languages in use for daily conversation [10,45], Indonesian netizens may also often spread hate speech
and abusive language on social media using their local languages. Therefore, researchers should make sure (especially when using
crowdsourced annotators) that the annotators understand the dataset language.
Since the annotation process may be costly, we need a special strategy to reduce annotation costs. One thing that can be done
is annotating the dataset which is easy to annotate using a rule-based approach. For example, in annotating the Indonesian abusive
language, we can easily annotate the dataset using a rule-based approach since some Indonesian abusive language contains abusive
words/phrases which do not have a double meaning. Therefore, we only need annotators to annotate the dataset that contains doublemeaning words/phrases such as animals or low-class profession names that are often used as abusive words/phrases by Indonesian
people [1]. For annotating hate speech datasets using rule-based methods, researchers can refer to [4]. In [4], they deﬁne a few
combination rules to automatically annotate data that can easily be annotated as hate speech. For example in [4], if a text contains
politicians’ names and abusive words/phrases, this text is said to be hate speech. Further research can expand the annotation rules
that have been built by [4].
As with text datasets, to build Indonesian hate speech and abusive language in image, speech, or video, the annotation process
can be done by crowdsourcing or a linguistics expert. In the speech dataset, the dataset can be built by manually recording as done by
[18,33,50]. However, building a speech dataset by manual recording can be costly since the dataset must be acted by an actor/person
that can act out the hate speech and abusive language naturally, as in real-world cases. Especially for datasets in video format, based
on our SLR process, we have not found researchers who researched Indonesian hate speech and abusive language detection in a video
dataset.
To build a better Indonesian hate speech and abusive language dataset, researchers who have built the dataset better make their
dataset open to public use as done by [5,1,39,25]. Therefore, other researchers can use the dataset to try their model [46,20,24,26,
38,27] or even try to continue to build the dataset bigger and with more detail [25]. Moreover, by opening our dataset to public use,
other researchers can evaluate and give suggestions if there are any errors in our dataset.
As discussed before where Indonesia has so many local languages that are often used by Indonesian netizens when creating and
spreading HSAL in social media [10,45], we need to build a valid HSAL detection dataset not only in the Indonesian language but

19

https://theconversation.com/indonesias-information-law-has-threatened-free-speech-for-more-than-a-decade-this-must-stop-127446.
11

Heliyon 9 (2023) e18647

M.O. Ibrohim and I. Budi

also in the Indonesian local languages. To achieve this goal, we need wide and strong collaboration from many researchers, linguists,
and stakeholders who are concerned with hate speech across regions so we can build valid HSAL detection datasets that cover as
many Indonesian local languages.
6.2. Challenge 2: building the robust model
Building a robust model for Indonesian hate speech and abusive language detection is quite a challenging task since there are
several diﬃculties. The ﬁrst diﬃculty is the variety of dataset sources and types. Each source of the dataset will have its own
challenges due to the peculiarities of each. For example, people in diﬀerent social media sources will have diﬀerent typing habits.
In Twitter, due to the limited number of characters allowed, the dataset will be short and contain many abbreviations. This problem
will present a big challenge in the data preprocessing step, especially in the text normalization phase [5,1,25]. Conversely, Facebook,
which allows people to post a long article, will give challenges the researchers on how to catch the main message that may be hidden
in the post [7].
As with the source of the dataset, each type of dataset will have its own challenges due to the peculiarities of each. In general,
types of hate speech and abusive language datasets can be divided into four types including text, image, speech, and video. As
described before, in the text dataset, we will face the diﬃculties of how to preprocess the noisy text and how to detect hidden
messages, since each source of text dataset will have diﬀerent typing habits. In the image dataset, we will face challenges of how
to catch the message typed/written in the image. Although we can catch the text from the image by extraction using OCR as [3]
did, this method may not be accurate if the image is noisy. Moreover, if the text on the image is written manually using paint
on the image, the OCR may be completely unable to extract the text. As with the image dataset, in the speech dataset, we also
will face challenges on how to catch the message contained in the speech. In [18,33,50], they studied Indonesian hate speech and
abusive language detection by directly classifying the audio using speech/acoustic features. However, [18,33,50] built their dataset
by manually recording so that the dataset will be clean, even though the real case speech dataset may be very noisy due to the
ambient noise or music background. Lastly, for the video dataset, the challenge we will face is approximately the same as with the
speech dataset. In the video datasets, we will face the challenge of how to extract the message contained in the video speech that
may be very noisy because of ambient noise or music background. Moreover, detecting hate speech and abusive language in a video
dataset will be more challenging since there are still very few researchers who research video datasets.
The next challenge in building a robust model for Indonesian hate speech and abusive language is the language problem. As
discussed in Subsection 6.1, Indonesian netizens often mix the Indonesian language with English [43] or use local language [45,10]
in daily conversation and also often use abusive words/phrases from foreign languages other than English [1]. This problem will give
us diﬃculties in preprocessing and building the language model since diﬀerent languages may have diﬀerent grammar and typing
habits (e.g., style of abbreviations, slang, etc.). In [58,24], they translate the multilingual dataset into English. However, if using this
translation method, we will face challenges of the ambiguity and failure of translation result that may aﬀect the classiﬁcation result
[24].
From Table 5, we can see that most of the researchers who researched Indonesian hate speech and abusive language detection are
still using classic machine-learning models with classic text representation features. Even though, classic machine learning (especially
when applied with classical statistical features like word n-grams) often can not catch the semantic meaning so it leads to giving
biased performance results. For example, the hate speech detection in the political domain experiment by [5] gives a promising result
with 93.5% of F-Measure when using RFDT with the word n-grams feature. However, in their error analysis, they found that their
model is highly biased in word distribution on the training dataset, which makes the model simply classify a tweet as hate speech if
it contains one of the candidate’s names because there are many hate speech tweets towards him on the training set.
To face this challenge, researchers need to explore more state-of-the-art methods. Compare to HSAL detection in other languages,
many of them already use state-of-the-art methods. Therefore, at the start, we can try to adapt HSAL detection research from other
countries that already use several state-of-the-art methods, like English HSAL detection research. For a text dataset, further research
can try several state-of-the-art deep-learning approaches like Gated recurrent units (GRU) [59], Convolutional Neural Networks
(CNN) [8,60] with state of the art text representation embedding like Global Vectors for word representation (GloVe) [8], Embeddings
from Language Models (ELMo) [9,60], Bidirectional Encoder Representations from Transformers (BERT) [60], etc. Furthermore,
researchers also can try ensembling the deep-learning approach [61,9] or adding special attention to the architecture [9] to increase
the model’s performance. In [22,21], they actually have used a BERT-based language model for feature extraction. However, [22,21]
used a multilingual BERT-based language model instead of monolingual Indonesian so that the experiment result performance does
not surpass the existing approach. In [57,31], they train a BERT-based language model using a monolingual Indonesian dataset and
used it for doing several Indonesian natural language processing tasks like text classiﬁcation, named entity recognition, part-of-speech
tagging, summarization, etc. and the results shows that using monolingual Indonesian BERT-based language model can give quite
excellent performance compared to existing models. Therefore, for future works, researchers can try to use a monolingual Indonesian
BERT-based language model for Indonesian HSAL detection.
Besides using a monolingual Indonesian BERT-based language model for Indonesian HSAL detection, we also need to try domain
adaptation by re-training the Indonesian pre-trained BERT-based language model with a new raw Indonesian dataset which contains
a lot of HSAL speech so that the pre-trained language model that will be used is ﬁtter to perform Indonesian HSAL detection. In [11],
they re-train the English pre-trained BERT-based language model with raw English Reddit dataset which contain more hate speech
conversation than the original raw text used to train the original English pre-trained BERT and the result shows that this approach
12

Heliyon 9 (2023) e18647

M.O. Ibrohim and I. Budi

can improve the performance since the domain of the new pre-trained language model become ﬁtter to the hate speech detection
topic.
As with the text dataset, researchers can also try deep-learning approaches including trying to ensemble them or adding special
attention to build a robust model for Indonesian hate speech and abusive language in image, speech, and video datasets. However,
we found that research on hate speech and abusive language in the image, speech, and video datasets is still very rare, even in
English, which is an international language where most researchers research that language. To face this challenge, researchers can
start by adapting research on similar tasks that use image, speech, and video datasets like classiﬁcation tasks using those dataset
types.
6.3. Challenge 3: tasks that need to be tackled
From the discussion in Section 5, we found that several tasks need to be tackled to make a better Indonesian hate speech and
abusive language system. Currently, most Indonesian hate speech and abusive language detection research are on text datasets, most
of which came from the Twitter dataset, even though other social media like Instagram and Facebook are often used to spread hate
speech and abusive language in text form by Indonesian people.20 Since in social media one can also post or comment using images,
speech, and audio, hate speech, Indonesian people may also spread hate speech and abusive language in those data types. Especially
on video data types, in recent years, the phenomenon of using abusive language by vloggers and YouTubers has emerged [15].
In Indonesia, spreading hate speech is a criminal act regulated by law [37]. Unfortunately, rampant hate speech spreading is
inversely proportional to the limitations of cybercrime division staﬀ in the police. This requires police to choose what hate speech
cases should be tackled ﬁrst based on the potential damage to society. Therefore, building a good Indonesian hate speech detection
system is not adequate if just detecting whether an instance contains hate speech or not. In [25], they conducted an FGD with Staﬀ
of Direktorat Tindak Pidana Siber Bareskrim to build an Indonesian hate speech target, category, and level hierarchy (see Fig. 1) and
did experiments on it. These hate speech targets, categories, and levels can help the cybercrime units in the police determine what
hate speech case should be tackled ﬁrst. However, research in [25] still has several deﬁciencies that need to be improved, especially
the very imbalanced dataset problem. Moreover, still based on the FGD result, [25] found three tasks that need to be tackled by
researchers to build a better hate speech detection system i.e., build a system that can detect a hate speech buzzer, thread starter,
and fake account spreader. In the case of hate speech spreading, those three types of accounts often spread hate speech not only
because they want to humiliate/decrease someone/some groups, but also to bring two or more groups into conﬂict and then left the
debate after the conﬂict is booming.
Based on our research, research on hate speech buzzers, thread starters, and fake account spreaders is still very rare, even in
English which is an international language and most researchers conduct research in that language. To face this challenge, researchers
can start by adapting research on similar tasks. For example, for preliminary research on hate speech buzzer detection, researchers
can refer to the Twitter buzzer detection research conducted by [23,28,48]. Meanwhile, for initial research on fake account hate
speech spreader detection, researchers can refer to the Twitter malicious account detection research conducted by [14,35].
7. Conclusions and future works
Hate speech and abusive language spreading in Indonesian social media is a huge problem. This is because Indonesia has a
huge number of social media users and they often abuse it to spread hate speech and abusive language. To solve this problem,
many researchers have been concerned to build a system/model that can detect Indonesian hate speech and abusive language in
several sources (Twitter, Facebook, Instagram, LINE, YouTube comments, and manual recording) and types of dataset (text, speech,
and image). Most of them are studies on the Twitter dataset (text) using a classic machine-learning approach with classic text
representation features.
Like in other languages, building a good Indonesian HSAL detection system is not an easy task. In this case, building an Indonesian
HSAL detection system may be more diﬃcult compared to when we build HSAL detection systems for other languages. Similar to
HSAL research in other languages, researchers will face diﬃculties in how to reduce the annotation bias (since HSAL annotation
is a highly subjective task) to get a valid dataset, especially in Indonesia a country that has so many ethnicities. Compare to other
countries that have fewer ethnicities, reducing the annotation bias in HSAL annotation may be more diﬃcult since diﬀerent ethnicities
may have diﬀerent cultures that aﬀect their sensitivity level in annotating the data. Moreover, as discussed in Subsection 5.1, we
found that many previous works are following HSAL deﬁnitions from diﬀerent countries to build their Indonesian HSAL data, where
which may cause their dataset may not to ﬁt with the HSAL deﬁnition that is applicable in Indonesia. For this problem, we suggest
that in the future ﬁrstly we need to do an FGD with an Indonesian hate speech authority, linguist experts, and law experts to make
annotation guidelines for Indonesian HSAL annotation that ﬁt the HSAL handling regulation in Indonesia. Then, for the annotation
itself, we suggest that the annotation is done by linguist experts, or using crowdsourcing that covers the ethnicities distribution in
Indonesia, by still following the guideline agreed together in the FGD result.
Next, researchers will face challenges of how to build a robust model to detect Indonesian HSAL detection. Similar to building
dataset problems, building a robust HSAL detection model in Indonesian may be more diﬃcult compared to the other languages.
One of the biggest causes of this is that Indonesia has so many local languages and many Indonesian netizens are mixing them when

20

https://www.cnnindonesia.com/teknologi/20180615170321-185-306378/instagram-dan-facebook-jadi-ladang-ujaran-kebencian.
13

Heliyon 9 (2023) e18647

M.O. Ibrohim and I. Budi

speeching and spreading HSAL on their social media. Moreover, as discussed in Subsection 6.1, not only mixing Indonesian languages
with their Indonesian local languages, many Indonesian netizens often use slang, parable, and idiom from other countries (not only
from English as the world’s major language). Furthermore, indirect languages like sarcasm and irony can also make the model more
diﬃcult to predict the correct label. In this case, we need a model that can handle those mixed and indirect language problems. As
the starting point for future works to solve this problem, we can try to build classiﬁers with a pre-trained contextual language model
(e.g. BERT) that is speciﬁcally trained in the raw text that contains many Indonesian HSAL variations.
Besides the valid datasets and robust models problem, several tasks need to be tackled by the researchers in the future works to
build a good Indonesian hate speech and abusive language detection system is not an easy task. Instead of just detecting whether an
instance contains hate speech and abusive language or not, researchers must be able to build a system that can help the cybercrime
division of the police to determine what hate speech case must be handled ﬁrst. The cybercrime divisions need to determine what
hate speech case must be handled ﬁrst based on the potential damage in society due to the rampant hate speech spreading, which is
inversely proportional to the limitations of cybercrime division staﬀ in the police. To solve this problem, researchers need to build a
hate speech detection system that can detect the hate speech targets, categories, and levels, and also detect the hate speech buzzer,
thread starter, and fake account spreader.
To realize all the future works listed in this conclusion faster, we see that there is an urgency to build an HSAL detection
benchmark website to be a showcase for existing Indonesian HSAL detection research. Through a benchmark website, people can
easily know what existing methods that are already done by the previous works so that they are able to know the research gap faster.
Moreover, people can test their HSAL detection model in a valid shared test set so that they can easily know whether their approach
is surpassing the previous works or not. Besides becoming a leaderboard showcase, a benchmark website also can be a place for
people to share their HSAL dataset or even the pre-trained model. Therefore, other people especially the government, social media
platforms, and other HSAL stakeholders can easily replicate or reuse the existing work for the content moderation need. As far as
we know, there is still no HSAL detection benchmark website, even for English as the major language. Therefore, building an HSAL
detection benchmark website for HSAL research in Indonesian, English, or any other language will become the pioneer and very
useful for the community. To build an HSAL benchmark website, future researchers can adapt and improve the English [54,53]21
Indonesian [57]22 downstream task benchmark website.
Declaration of competing interest
The authors declare that they have no known competing ﬁnancial interests or personal relationships that could have appeared to
inﬂuence the work reported in this paper.
Acknowledgements
This research was funded by PUTI Q2 Research Grant from Universitas Indonesia with grant number NKB-1475/UN2.RST/
HKP.05.00/2020.
References
[1] A dataset and preliminaries study for abusive language detection in Indonesian social media, in: The 3rd International Conference on Computer Science and
Computational Intelligence (ICCSCI 2018): Empowering Smart Technology in Digital Era for a Better Life, Proc. Comput. Sci. 135 (2018) 222–229, https://
www.sciencedirect.com/science/article/pii/S1877050918314583, https://doi.org/10.1016/j.procs.2018.08.169.
[2] M. Adriani, J. Asian, B. Nazief, S.M. Tahaghoghi, H.E. Williams, Stemming Indonesian: a conﬁx-stripping approach, ACM Trans. Asian Lang. Inf. Process. 6
(2007) 1–33.
[3] I.M. Ahmad Niam, B. Irawan, C. Setianingsih, B.P. Putra, Hate speech detection using latent semantic analysis (lsa) method based on image, in: 2018 International
Conference on Control, Electronics, Renewable Energy and Communications (ICCEREC), 2018, pp. 166–171.
[4] R.R.E. Akbar, R.N. Shofa, M.I. Paripurna, Supratman, The implementation of naïve Bayes algorithm for classifying tweets containing hate speech with political
motive, in: 2019 International Conference on Sustainable Engineering and Creative Computing (ICSECC), 2019, pp. 144–148.
[5] I. Alﬁna, R. Mulia, M.I. Fanany, Y. Ekanata, Hate speech detection in the Indonesian language: a dataset and preliminary study, in: 2017 International Conference
on Advanced Computer Science and Information Systems (ICACSIS), 2017, pp. 233–238.
[6] F. Alkomah, X. Ma, A literature review of textual hate speech detection methods and datasets, Information 13. URL (2022), https://doi.org/10.3390/
info13060273, https://www.mdpi.com/2078-2489/13/6/273.
[7] N. Aulia, I. Budi, Hate speech detection on Indonesian long text documents using machine learning approach, in: Proceedings of the 2019 5th International
Conference on Computing and Artiﬁcial Intelligence, Association for Computing Machinery, New York, NY, USA, 2019, pp. 164–169.
[8] P. Badjatiya, S. Gupta, M. Gupta, V. Varma, Deep learning for hate speech detection in tweets, in: Proceedings of the 26th International Conference on World
Wide Web Companion, International World Wide Web Conferences Steering Committee, Republic and Canton of Geneva, CHE, 2017, pp. 759–760.
[9] M. Bojkovský, M. Pikuliak, STUFIIT at SemEval-2019 task 5: multilingual hate speech detection on Twitter with MUSE and ELMo embeddings, in: Proceedings of
the 13th International Workshop on Semantic Evaluation, Association for Computational Linguistics, Minneapolis, Minnesota, USA, 2019, pp. 464–468, https://
www.aclweb.org/anthology/S19-2082.
[10] BPS, Kewarganegaraan, Suku Bangsa, agama, dan Bahasa Sehari-hari Penduduk Indonesia, Bada Pusat Statistik Indonesia, Jakarta, 2010.
[11] T. Caselli, V. Basile, J. Mitrović, M. Granitzer, HateBERT: retraining BERT for abusive language detection in English, in: Proceedings of the 5th Workshop on
Online Abuse and Harms (WOAH 2021), Association for Computational Linguistics, 2021, pp. 17–25, Online, https://aclanthology.org/2021.woah-1.3.

21
22

https://super.gluebenchmark.com/leaderboard/.
https://www.indobenchmark.com/.
14

Heliyon 9 (2023) e18647

M.O. Ibrohim and I. Budi

[12] N.V. Chawla, K.W. Bowyer, L.O. Hall, W.P. Kegelmeyer, Smote: synthetic minority over-sampling technique, J. Artif. Intell. Res. 16 (2002) 321–357.
[13] Y. Chen, Y. Zhou, S. Zhu, H. Xu, Detecting oﬀensive language in social media to protect adolescent online safety, in: Proceedings of the 2012 ASE/IEEE
International Conference on Social Computing and 2012 ASE/IEEE International Conference on Privacy, Security, Risk and Trust, 2012, pp. 71–80.
[14] S. Cresci, R. Di Pietro, M. Petrocchi, A. Spognardi, M. Tesconi, The paradigm-shift of social spambots: evidence, theories, and tools for the arms race, in:
Proceedings of the 26th International Conference on World Wide Web Companion, International World Wide Web Conferences Steering Committee, 2017,
pp. 963–972.
[15] E.R. David, M. Sondakh, S. Harilama, Pengaruh konten vlog dalam youtube terhadap pembentukan sikap mahasiswa ilmu komunikasi fakultas ilmu sosial dan
politik universitas sam ratulang, Acta Diurna 6 (2017).
[16] T. Davidson, D. Warmsley, M.W. Macy, I. Weber, Automated hate speech detection and the problem of oﬀensive language, in: International AAAI Conference on
Web and Social Media (ICWSM), 2017, pp. 512–515.
[17] D. Elisabeth, I. Budi, M.O. Ibrohim, Hate code detection in Indonesian tweets using machine learning approach: a dataset and preliminary study, in: 2020 8th
International Conference on Information and Communication Technology (ICoICT), 2020, pp. 1–6.
[18] S. Endah, D. Nugraheni, S. Adhy, S. Sutikno, The automation system censor speech for the Indonesian rude swear words based on support vector machine and
pitch analysis, IOP Conf. Ser., Mater. Sci. Eng. 190 (2017) 012039, https://doi.org/10.1088/1757-899X/190/1/012039.
[19] E. Erizal, B. Irawan, C. Setianingsih, Hate speech detection in Indonesian language on Instagram comment section using maximum entropy classiﬁcation method,
in: 2019 International Conference on Information and Communications Technology (ICOIACT), 2019, pp. 533–538.
[20] M. Fauzi, A. Yuniarti, Ensemble method for Indonesian Twitter hate speech detection, Indones. J. Electr. Eng. Comput. Sci. 11 (2018) 294–299, https://
doi.org/10.11591/ijeecs.v11.i1.pp294-299.
[21] K.M. Hana, Faraby S.A. Adiwijaya, A. Bramantoro, Multi-label classiﬁcation of Indonesian hate speech on Twitter using support vector machines, in: 2020
International Conference on Data Science and Its Applications (ICoDSA), 2020, pp. 1–7.
[22] R. Hendrawan, Adiwijaya, S. Al Faraby, Multilabel classiﬁcation of hate speech and abusive words on Indonesian Twitter social media, in: 2020 International
Conference on Data Science and Its Applications (ICoDSA), 2020, pp. 1–7.
[23] M. Ibrahim, O. Abdillah, A.F. Wicaksono, M. Adriani, Buzzer detection and sentiment analysis for predicting presidential election results in a Twitter nation, in:
2015 IEEE International Conference on Data Mining Workshop (ICDMW), 2015, pp. 1348–1353.
[24] M. Ibrohim, I. Budi, Translated vs non-translated method for multilingual hate speech identiﬁcation in twitter, Int. J. Adv. Sci., Eng. Inf. Technol. 9 (2019) 1116–1123, https://doi.org/10.18517/ijaseit.9.4.8123, funding Information: The authors acknowledge the PITTA A research grant NKB0350/UN2.R3.1/HKP.05.00/2019 from Directorate Research and Community Services, Universitas Indonesia. Publisher Copyright: © 2019, Insight Society.
[25] M.O. Ibrohim, I. Budi, Multi-label hate speech and abusive language detection in Indonesian Twitter, in: Proceedings of the Third Workshop on Abusive
Language, Association for Computational Linguistics, Florence, Italy, 2019, pp. 46–57, Online, https://aclanthology.org/W19-3506.
[26] M.O. Ibrohim, E. Sazany, I. Budi, Identify abusive and oﬀensive language in Indonesian Twitter using deep learning approach, J. Phys. Conf. Ser. 1196 (2019)
012041, https://doi.org/10.1088/1742-6596/1196/1/012041, https://dx.doi.org/10.1088/1742-6596/1196/1/012041.
[27] M.O. Ibrohim, M.A. Setiadi, I. Budi, Identiﬁcation of hate speech and abusive language on Indonesian Twitter using the word2vec, part of speech and emoji
features, in: Proceedings of the 1st International Conference on Advanced Information Science and System, Association for Computing Machinery, New York,
NY, USA, 2020.
[28] M.T. Juzar, S. Akbar, Buzzer detection on Twitter using modiﬁed eigenvector centrality, in: 2018 5th International Conference on Data and Software Engineering
(ICoDSE), 2018, pp. 1–5.
[29] B. Kitchenham, Procedures for Performing Systematic Reviews, Keele University. Technical Report TR/SE-0401, Department of Computer Science, Keele University, UK, 2004.
[30] Komnas HAM, Buku Saku Penanganan Ujaran Kebencian (Hate Speech), Komisi Nasional Hak Asasi Manusia, Jakarta, 2015.
[31] F. Koto, A. Rahimi, J.H. Lau, T. Baldwin, IndoLEM and IndoBERT: a benchmark dataset and pre-trained language model for Indonesian NLP, in: Proceedings of
the 28th International Conference on Computational Linguistics, International Committee on Computational Linguistics, Barcelona, Spain, 2020, pp. 757–770,
https://www.aclweb.org/anthology/2020.coling-main.66.
[32] H. Margono, X. Yi, G.K. Raikundalia, Mining Indonesian cyber bullying patterns in social networks, in: Proceedings of the Thirty-Seventh Australasian Computer
Science Conference, vol. 147, Australian Computer Society, Inc., AUS, 2014, pp. 115–124.
[33] S. Novitasari, D.P. Lestari, S. Sakti, A. Purwarianti, Rude-words detection for Indonesian speech using support vector machine, in: 2018 International Conference
on Asian Language Processing (IALP), 2018, pp. 19–24.
[34] H. Nurrahmi, D. Nurjanah, Indonesian Twitter cyberbullying detection using text classiﬁcation and user credibility, in: 2018 International Conference on
Information and Communications Technology (ICOIACT), 2018, pp. 543–548.
[35] F.N. Pakaya, M.O. Ibrohim, I. Budi, Malicious account detection on Twitter based on tweet account features using machine learning, in: 2019 Fourth International
Conference on Informatics and Computing (ICIC), 2019, pp. 1–5.
[36] F. Poletto, V. Basile, M. Sanguinetti, C. Bosco, V. Patti, Resources and benchmark corpora for hate speech detection: a systematic review, Lang. Resour. Eval. 55
(2020) 477–523, https://doi.org/10.1007/s10579-020-09502-8.
[37] Polri., Surat Edaran Kapolri Nomor: SE/06/X/2015 tentang Penanganan Ujaran Kebencian (Hate Speech), Markas Besar Kepolisian Negara Republik Indonesia,
Jakarta, 2015.
[38] F.A. Prabowo, M.O. Ibrohim, I. Budi, Hierarchical multi-label classiﬁcation to identify hate speech and abusive language on Indonesian Twitter, in: 2019 6th
International Conference on Information Technology, Computer and Electrical Engineering (ICITACEE), 2019, pp. 1–5.
[39] N.I. Pratiwi, I. Budi, I. Alﬁna, Hate speech detection on Indonesian Instagram comments using fasttext approach, in: 2018 International Conference on Advanced
Computer Science and Information Systems (ICACSIS), 2018, pp. 447–450.
[40] N.I. Pratiwi, I. Budi, M.A. Jiwanggi, Hate speech identiﬁcation using the hate codes for Indonesian tweets, in: Proceedings of the 2019 2nd International
Conference on Data Science and Information Technology, Association for Computing Machinery, New York, NY, USA, 2019, pp. 128–133.
[41] B.B.S. Putra Perdana, B. Irawan, C. Setianingsih, Hate speech detection in Indonesian language on Instagram comment section using deep neural network
classiﬁcation method, in: 2019 IEEE Asia Paciﬁc Conference on Wireless and Mobile (APWiMob), 2019, pp. 143–149.
[42] R. Rini, E. Utami, A.D. Hartanto, Systematic literature review of hate speech detection with text mining, in: 2020 2nd International Conference on Cybernetics
and Intelligent System (ICORIS), 2020, pp. 1–6.
[43] A.N. Rizal, S. Stymne, Evaluating word embeddings for Indonesian–English code-mixed text based on synthetic data, in: Proceedings of the the 4th Workshop
on Computational Approaches to Code Switching, European Language Resources Association, Marseille, France, 2020, pp. 26–35, https://www.aclweb.org/
anthology/2020.calcs-1.4.
[44] U.A.N. Rohmawati, S.W. Sihwi, D.E. Cahyani, Semar: an interface for Indonesian hate speech detection using machine learning, in: 2018 International Seminar
on Research of Information Technology and Intelligent Systems (ISRITI), 2018, pp. 646–651.
[45] M.S. Saputri, M. Adriani, Identifying Indonesian local languages on spontaneous speech data, in: 2019 International Conference on Advanced Computer Science
and Information Systems (ICACSIS), 2019, pp. 247–254.
[46] E. Sazany, I. Budi, Deep learning-based implementation of hate speech identiﬁcation on texts in Indonesian: preliminary study, in: 2018 International Conference
on Applied Information Technology and Innovation (ICAITI 2018), Padang, Indonesia, 2018.
[47] G.H. Stanton, The Rwandan genocide: why early warning failed, J. Afr. Conﬂ. Peace Stud. 1 (2) (2009) 6–25.
15

Heliyon 9 (2023) e18647

M.O. Ibrohim and I. Budi

[48] A. Suciati, A. Wibisono, P. Mursanto, Twitter buzzer detection for Indonesian presidential election, in: 2019 3rd International Conference on Informatics and
Computational Sciences (ICICoS), 2019, pp. 1–5.
[49] M. Susanty, Rahman A.F. Sahrul, M.D. Normansyah, A. Irawan, Oﬀensive language detection using artiﬁcial neural network, in: 2019 International Conference
of Artiﬁcial Intelligence and Information Technology (ICAIIT), 2019, pp. 350–353.
[50] T.L. Sutejo, D.P. Lestari, Indonesia hate speech detection using deep learning, in: 2018 International Conference on Asian Language Processing (IALP), 2018,
pp. 39–43.
[51] S. Turaob, J. Mitrpanont, Automatic discovery of abusive Thai language, in: International Conference on Asia-Paciﬁc Digital Libraries, 2017, pp. 267–278.
[52] F.D. Vigna, A. Cimino, F. Dell’Orletta, M. Petrocchi, M. Esconi, Hate me, hate me not: hate speech detection on Facebook, in: Proceedings of the First Italian
Conference on Cybersecurity (ITASEC17), 2017, pp. 86–95.
[53] A. Wang, Y. Pruksachatkun, N. Nangia, A. Singh, J. Michael, F. Hill, O. Levy, S. Bowman, Superglue: a stickier benchmark for general-purpose language
understanding systems, in: H. Wallach, H. Larochelle, A. Beygelzimer, F. d’Alché-Buc, E. Fox, R. Garnett (Eds.), Advances in Neural Information Processing
Systems, Curran Associates, Inc., 2019.
[54] A. Wang, A. Singh, J. Michael, F. Hill, O. Levy, S. Bowman, GLUE: a multi-task benchmark and analysis platform for natural language understanding, in:
Proceedings of the 2018 EMNLP Workshop BlackboxNLP: Analyzing and Interpreting Neural Networks for NLP, Association for Computational Linguistics,
Brussels, Belgium, 2018, pp. 353–355, https://aclanthology.org/W18-5446.
[55] W. Warner, J. Hirschberg, Detecting hate speech on the world wide web, in: Proceedings of the Second Workshop on Language in Social Media, Association for
Computational Linguistics, Montréal, Canada, 2012, pp. 19–26, https://www.aclweb.org/anthology/W12-2103.
[56] I.D.P. Wijana, M. Rohmadi, Sosiolinguistik: Kajian, Teori, dan Analisis, Pustaka Pelajar, Yogyakarta, 2010.
[57] B. Wilie, K. Vincentio, G.I. Winata, S. Cahyawijaya, X. Li, Z.Y. Lim, S. Soleman, R. Mahendra, P. Fung, S. Bahar, A. Purwarianti, IndoNLU: benchmark and
resources for evaluating Indonesian natural language understanding, in: Proceedings of the 1st Conference of the Asia-Paciﬁc Chapter of the Association for
Computational Linguistics and the 10th International Joint Conference on Natural Language Processing, Association for Computational Linguistics, Suzhou,
China, 2020, pp. 843–857, https://www.aclweb.org/anthology/2020.aacl-main.85.
[58] Y. Zhang, A. Ramesh, Fine-grained analysis of cyberbullying using weakly-supervised topic models, in: 2018 IEEE 5th International Conference on Data Science
and Advanced Analytics (DSAA), 2018, pp. 504–513.
[59] Z. Zhang, D. Robinson, J. Tepper, Detecting hate speech on Twitter using a convolution-gru based deep neural network, in: A. Gangemi, R. Navigli, M.E. Vidal,
P. Hitzler, R. Troncy, L. Hollink, A. Tordai, M. Alam (Eds.), The Semantic Web, Springer International Publishing, 2018, pp. 745–760.
[60] Y. Zhou, Y. Yang, H. Liu, X. Liu, N. Savage, Deep learning based fusion approach for hate speech detection, IEEE Access 8 (2020) 128923–128929.
[61] S. Zimmerman, U. Kruschwitz, C. Fox, Improving hate speech detection with deep learning ensembles, in: Proceedings of the Eleventh International Conference
on Language Resources and Evaluation (LREC 2018), European Language Resources Association (ELRA), Miyazaki, Japan, 2018, https://www.aclweb.org/
anthology/L18-1404.

16

