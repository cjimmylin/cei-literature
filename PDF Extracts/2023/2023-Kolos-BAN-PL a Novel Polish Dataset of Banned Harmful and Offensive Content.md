---
title: "2023-Kolos-BAN-PL a Novel Polish Dataset of Banned Harmful and Offensive Content - PDF Extract"
source_pdf: "2023-Kolos-BAN-PL a Novel Polish Dataset of Banned Harmful and Offensive Content.pdf"
pages: 14
extracted_at: "2026-02-13T09:50:30.268107"
---

# PDF Extract: 2023-Kolos-BAN-PL a Novel Polish Dataset of Banned Harmful and Offensive Content

**Source PDF:** 2023-Kolos-BAN-PL a Novel Polish Dataset of Banned Harmful and Offensive Content.pdf
**Total Pages:** 14

---

## Content

```
--- Page 1 ---

BAN-PL: a Polish Dataset of Banned Harmful and Offensive Content
from Wykop.pl web service
WARNING: This paper contains examples of language and content that may be offensive, discriminatory, or
hateful in nature.
Anna Kołos‡,∗, Inez Okulska‡,∗, Kinga Głąbińska∗, Agnieszka Karlińska∗,
Emilia Wiśnios∗, Paweł Ellerik†, Andrzej Prałat†
‡equal contribution
∗NASK National Research Institute (Warsaw), †Wykop.pl
Abstract
Since the Internet is flooded with hate, it is one of the main tasks for NLP experts to master automated online
content moderation. However, advancements in this field require improved access to publicly available accurate
and non-synthetic datasets of social media content. For the Polish language, such resources are very limited. In
this paper, we address this gap by presenting a new open dataset of offensive social media content for the Polish
language. The dataset comprises content from Wykop.pl, a popular online service often referred to as the Polish
Reddit, reported by users and banned in the internal moderation process. It contains a total of 691,662 posts and
comments, evenly divided into two categories: harmful and neutral (non-harmful). The anonymized subset of
the BAN-PL dataset consisting on 24,000 pieces (12,000 for each class), along with preprocessing scripts have
been made publicly available. Furthermore the paper offers valuable insights into real-life content moderation
processes and delves into an analysis of linguistic features and content characteristics of the dataset. Moreover,
a comprehensive anonymization procedure has been meticulously described and applied. The prevalent biases
encountered in similar datasets, including post-moderation and pre-selection biases, are also discussed.
Keywords: offensive language detection, hate speech, cyberbullying, dataset, social media
1.
Introduction
Given the pervasive nature of offensive language
on the Internet, proficiently managing automated
online content moderation stands as a paramount
objective for NLP experts.
However, the main
challenge remains the accessibility of accurate
datasets, a task complicated by the inability to syn-
thetically represent them. The wide spectrum of
linguistic inventiveness employed by cyberbullies,
coupled with fractured syntax, necessitates at least
a large language model to generate linguistically
convincing offensive samples. Yet exactly these
models block such content, making it hardly pos-
sible to analyze or create it (Zhou et al. (2023)).
Hence, training data should be gathered from the
everyday flood of new content posted online. How-
ever, finding a reliable and representative source
is still a major issue, especially for low-resource
languages.
While there has been significant growth in the
availability of resources in recent years, such as the
inclusion of 25 languages in the Catalog of Abusive
Language Data1 (Vidgen and Derczynski (2020)),
the development of resources for offensive content
has been uneven, with only one entry listed for the
Polish language.
In this paper, we introduce BAN-PL, a Polish
language dataset of banned offensive content, to
1www.hatespeechdata.com
address this gap in available resources. Notably,
it is one of the few publicly available datasets
(Ljubešić et al. (2018)) that includes content re-
ported by community members (here users of the
service Wykop.pl), identified as offensive, and sub-
sequently deleted by professional content modera-
tors.
Wykop.pl was established in December 2005
as an equivalent to the digg.com web service
(gazeta.pl (2006)). Often referred to as the Pol-
ish Reddit (Wójcik (2021)), it is currently listed as
one of the top 10 most popular social networking
services (SNS) in Poland, boasting approximately
3 million real users as of February 2023. These
users generate around 30,000 new posts and com-
ments daily (Wirtualnemedia (2023)). The content
is under constant monitoring by trained modera-
tors from the user community. Additionally, every
user can independently flag any piece of content
within an internal taxonomy of over 20 different ban
reasons.2 If content is flagged by users, it must un-
dergo review by a moderator to either be approved
as non-harmful or removed from the website.
Besides introducing a new dataset and analyzing
its most critical linguistic features and characteris-
tics, the paper also provides valuable insights into
real-life content moderation processes. Further-
more, a comprehensive anonymization procedure,
exceeding the typical masking of usernames and
2www.wykop.pl/standardy-moderacji
arXiv:2308.10592v3  [cs.CL]  26 Mar 2024

--- Page 2 ---

URLs, has been meticulously described and ap-
plied. The prevalent biases encountered in sim-
ilar datasets, including post-moderation and pre-
selection biases (see 6), are also discussed.
2.
Related work
The field of automated offensive language detec-
tion has seen significant efforts in the NLP com-
munity (for an overview of the latest developments
in this area, see Jahan and Oussalah (2023); Al-
rashidi et al. (2022)). A crucial factor for further
progress is a widespread access to diverse, pub-
licly available datasets of social media content. To
detect offensive language in English, researchers
commonly use datasets from platforms like Twit-
ter (Waseem and Hovy (2016); Davidson et al.
(2017); Founta et al. (2018)), as well as Wikipedia
talk pages (Wulczyn et al. (2017)). Some papers
also focus on hateful comments on platforms like
Facebook and YouTube (Hammer (2017); Salmi-
nen et al. (2018)). Zampieri et al. (2019a) created
a hierarchical dataset from Twitter called the Offen-
sive Language Identification Dataset (OLID), which
was adopted for SemEval-2019 Task 6, aimed at
identifying and categorizing offensive language in
social media (Zampieri et al. (2019b)). Addition-
ally, a dataset of content from banned communi-
ties on Reddit (RAL-E) has been employed to train
the BERT large language model for detecting abu-
sive language, leading to the creation of HateBERT
(Caselli et al. (2020)).
The diversity of existing datasets encompasses
various aspects, including different data sources
with: (i) varied labels and modes of annotation,
such as hate speech, offensiveness, aggression,
racism, sexism, and toxicity; (ii) distinct targets
of attacks, including personal attacks, attacks on
women, and attacks on migrants; (iii) differing num-
bers of classes, ranging from binary to multi-label
classification; (iv) varying degrees of class balance,
where, in many cases, the neutral class (represent-
ing non-harmful content) significantly outweighs the
harmful class or classes (see hate-related dataset
characteristics in MacAvaney et al. (2019)). A spe-
cific case involves datasets of content flagged for
review by online communities and subsequently
removed by trained moderators. There are very
few publicly accessible datasets like this. An ex-
ample is Slovenia’s MMC and Croatia’s STY, which
encompass news comments, including content re-
moved during the moderation process (Ljubešić
et al. (2018)). Both datasets are publicly available,
albeit in encrypted form. A small portion of the con-
tent in these datasets, approximately 8% in MMC
and around 2% in STY, has been deleted by mod-
erators. For a comprehensive overview of existing
corpora up to 2021, see (Poletto et al. (2021)).
Until recently, only two datasets containing offen-
sive social media content, including hate speech,
were publicly available for the Polish language. The
first dataset was acquired in 2017 (Troszyński and
Wawer (2017)), but it was made accessible on Hug-
gingFace only in 2021.3 The second one was origi-
nally introduced in task 6 of the PolEval2019 com-
petition.4 It is part of the KLEJ Comprehensive
Benchmark for Polish Language Understanding,
the equivalent of the well-known GLUE benchmark,
which encompasses 9 general natural language un-
derstanding tasks including cyberbullying detection
(CBD) (Rybak et al. (2020)). Detailed information
regarding data collection and preprocessing pro-
cedures can be found in Ptaszynski et al. (2019),
while enhancements to the dataset have been elab-
orated upon in Ptaszynski et al. (2023).
State-of-the-art results in the CBD KLEJ task (F1
score = 76.1) were achieved by the TrelBERT model
pre-trained on Twitter data (Szmyd et al. (2023)).
The authors of the model created an additional
test dataset called "harmful_tweets_1k"5 to assess
the generalisation of their solution to a broader
distribution of Twitter data. The results indicate that
TrelBERT, when used in a real-world scenario, has
a higher ability to detect harmful content than larger
models trained on general-domain corpora, e.g.,
HerBERT or Polish RoBERTa.6
Among the resources available for the Polish lan-
guage, it is also worth mentioning HateSpeech,7 a
tool for personalized hate speech recognition cre-
ated by CLARIN-PL.8 It was trained on datasets
obtained as part of the Wikipedia Detox project9
and allows for a broader analysis of offensive lan-
guage (Kocoń et al. (2021); Kazienko et al. (2023)).
3.
Data source
In a joint project between the institution represented
by the authors and the web service Wykop.pl, we
were able to collect a unique dataset of harmful
online content consisting of texts banned and la-
beled by professional moderators. The BAN-PL
dataset comprises a total of 691,662 pieces of
content, of which 345,831 were assigned to the
3https://huggingface.co/datasets/hate_
speech_pl
4https://2019.poleval.pl/index.php/
tasks/task6
5https://github.com/deepsense-ai/
trelbert
6https://klejbenchmark.com/
leaderboard/
7https://ws.clarin-pl.eu/hatespeech
8https://clarin-pl.eu/index.php/en/
home/
9https://meta.wikimedia.org/wiki/
Research:Detox/Data_Release

--- Page 3 ---

"harmful" class and the exact same number to the
"neutral" class. Non-textual material has been re-
moved. The "harmful" class comprises posts and
comments banned by moderators during the period
spanning from January 2019 to April 2023. The
collection of "neutral" data was executed between
March and August 2021, June and November 2022,
and January and June 2023.
3.1.
Moderation scheme
The moderators have been recruited from the
Wykop.pl users community and have undergone
dedicated training. Currently, there are 14 of them.
Each piece of content, flagged by the users, is in-
dependently assessed by five distinct moderators,
and the final score is based on the majority voting.
According to information provided by Wykop.pl, the
3:2 vote split, representing an indecision, is rare.
In most cases, a consensus decision is reached,
with the majority aligning with a particular rating, as
represented by a 5:0 or a 4:1 vote split.
In addition, the platform allows users to appeal
decisions made by the moderation team. This re-
sults in a reassessment of a moderation rating.
However, the content in question is then automat-
ically assigned only to moderators who were not
involved in the initial assessment of the reported
post or comment. They have the authority to reject
the appeal or accept it by reinstating the removed
content to the site. Further appeals will be esca-
lated to the service administrators, removing them
from the direct jurisdiction of the moderation team.
In overall, approximately 2% to 5% of the plat-
form’s content is reported to the moderation team,
which consists of 30,000 to 60,000 submissions
monthly. Of the content reported by users, 49% ad-
here to website policies. Roughly 15% are related
to spam and flooding, 10% involve inappropriate
content, and 7% pertain to incorrect tags. A small
fraction (1% to 2%) of submissions is re-evaluated,
with 3% to 5% deemed as valid appeals.
Since we are unable to evaluate the quality of
the moderators’ work according to the guidelines
applied to the evaluation of manually annotated
datasets, we asked three moderators to re-annotate
134 samples of the "harmful" class from the KLEJ
test dataset. The results of this experiment showed
that only 40% of the tweets were labelled as offen-
sive, with varying percentages among the annota-
tors. (Fig. 1).
The
inter-annotator
agreement
yielded
an
avarage score of 0.59 based on Fleiss’ and Ran-
dolph’s kappa multi-rater agreement measure.
Given that the annotators were equally trained by
Wykop.pl and followed the guidelines of the web-
site’s policy, a higher score could have been ex-
pected. However, in their everyday moderation pro-
cess, the moderators have access to the context
Figure 1: Percentage of samples from the KLEJ
test set labeled as offensive by three Wykop.pl mod-
erators
which was not granted in this case (the isolated text
samples were sent via a Google form for scoring).
The agreement scores did not differ significantly
between pairs of annotators yielding in average
0.59 with 2.64 STD. This observation suggests a
notable disparity between Wykop’s internal modera-
tion policy and the guidelines commonly employed
by professional annotators for labeling datasets, as
exemplified within the CBD task as part of the KLEJ
benchmark.
3.2.
Data collection process
For the purpose of offensive language detection,
we included in the dataset both content banned
for inciting hatred or violence (i.e., "Propagation
of hatred or violence, drastic content") and con-
tent including personal attacks (i.e., "Attacks me
or violates my personal rights," "Attacks me," "At-
tacks others"). In order to streamline the analysis
and classification process, we have merged these
categories into a single class labeled as "harmful."
This consolidated class includes the following types
of posts and comments that violate the platform’s
policy:
1. Content inciting hatred or violence towards oth-
ers, as well as attacking individuals/groups
based on protected characteristics such as
gender, race, ethnic origin, nationality, reli-
gion/belief/worldview, disability, age, sexual
orientation.
2. Content promoting violence, graphic material,
or advocating the spread of hatred, including
racism, xenophobia, national conflicts, or ho-
mophobia.
3. Graphic or literal depictions of violence, such
as torture, stoning, mistreatment of humans
or animals, murder, suicide, or expressions of
hatred.

--- Page 4 ---

4. Materials that damage one’s reputation, includ-
ing false information, vulgar insults, defama-
tion, verbal abuse, intimidation, blackmail, and
threats.
5. Personal attacks and targeting individuals
based on protected characteristics, such as
gender, race, ethnic origin, nationality, reli-
gion/beliefs/worldview, disability, age, or sex-
ual orientation.
In addition to the aforementioned categories, we
have also included content marked as "inappropri-
ate" in our dataset. This category is broad and
encompasses various types of content that are
deemed unsuitable, including incitement to commit
a crime or suicide, pornographic materials, content
promoting violence, promotion of drugs, etc. There-
fore, a supplementary task of classification of the
"inappropriate" content has been performed (see
details in section 3.3).
This initial "harmful" class consisted of 379,511
pieces of content. The content banned for inciting
hatred or violence (n = 75,396) comes from 20,130
unique users. The content that was banned due to
containing personal attacks (n = 72,990) originates
from 19,076 unique users. The content marked as
"inappropriate" (n = 231,125) came from 37,596
unique users. To obtain a balanced dataset for the
binary classification task, the contrasting neutral
class was gathered from the main page of the web
service. Only entries and comments published at
least 48 hours prior to scraping were considered,
taking into account the moderation dynamics of the
platform. The main page, being highly visible to the
public, typically ensures that any harmful content is
reported by the user within first 24 hours. Therefore,
samples that have not been banned or reported
within 48 hours can be regarded as "neutral". The
initial "neutral" class consisted of 560,750 unique
content pieces, covering various topics.
3.3.
Classification
Content flagged as "inappropriate" by moderators
largely overlaps with content that includes personal
attacks and incitement to hatred or violence. How-
ever, this category was less specific and included a
broader spectrum of phenomena. To maintain data
consistency, we decided to perform an automated
classification of content flagged as inappropriate.
We used content banned for inciting hatred or vi-
olence, content banned for personal attacks (n =
148,386), and a random sample of "neutral" con-
tent (n = 148,386) as training data. The choice of
the model was preceded by experiments using the
large Polish model RoBERTa (Dadas et al. (2020))
and TrelBERT. The best model turned out to be the
one using the average of the last hidden state from
RoBERTa large as the pooled output of the model.
This output was activated with ReLU and went to a
fully connected layer. The loss function used was
BCEWITHLOGITSLOSS (combination of sigmoid
layer and BCELoss function). The learning rate
used in the experiment was 1.5e-6. The model was
fine tuned on the "harmful" class and the neutral
samples. The dataset was split into three subsets,
with 75% of the data allocated for training, 12.5%
for validation, and a further 12.5% for testing pur-
poses. When applied to the flagged "inappropriate"
content, the model classified 85.43% of the obser-
vations as "harmful" and 14.57% as "non-harmful"
(F1 score = 0.92). We, therefore, only included the
observations classified as harmful in the dataset.
The final harmful class includes 148,386 posts
or comments flagged by moderators as inciting vi-
olence or personal attacks, and 197,445 posts or
comments flagged as "inappropriate" and classi-
fied as "harmful," for a total of 345,831 pieces of
content. The small portion of data (33,680 posts
or comments) from the class initially flagged as
"inappropriate" but classified as "not harmful" was
excluded from the dataset. In order to maintain bal-
ance between harmful and neutral content within
the dataset, a random selection of neutral post and
comment was made to match the number of harm-
ful pieces of content (n = 345,831).
4.
Data anonymization
Due to the presence of personal data, such as
home and email addresses, phone numbers or PE-
SEL numbers (identification number assigned to
individuals in Poland and used for administrative
purposes), within the dataset, a comprehensive
anonymization approach was imperative. User-
names and hyperlinks have also been masked. In
order to prevent the further spread of offensive con-
tent, the anonymization process included the sur-
names and pseudonyms of individuals targeted by
such content. These were primarily public figures,
politicians, authors, and celebrities.
Achieving complete anonymization, encompass-
ing the elimination of all contextual information
linked to these individuals that could potentially facil-
itate their identification, proves unattainable without
resorting to substantial reductions, subsequently
engendering distortion in the analyzed data.
In light of this, we have opted to conceal all
surnames and pseudonyms (particularly those of
social media influencers, prominent YouTubers,
and streamers) through the implementation of
placeholders, denoted as either [surname], or
[pseudonym]. Usernames mentioned in the main
body of the text, unaccompanied by the custom-
ary "@" symbol, have been replaced with the
pseudonym tag as well. In order to maintain contex-
tual integrity, as well as the usability and relevance

--- Page 5 ---

of the data for further research purposes (especially
from a sociolinguistic perspective), we decided to
retain first names, indicating whether the target is
male or female and frequently bearing eponymical
significance, names of public organizations and
political parties. In agreement with Wykop.pl data
providers, it has been decided that fictional char-
acters, historical figures and deceased individuals
are to remain non-anonymized.
Notably, there is no readily available solution for
the Polish language that would provide a high level
of precision in such complex anonymization proce-
dures with respect to social media content. Thus,
we employed a medley of techniques and tested
various approaches. Our anonymization pipeline
encompasses a robust combination of Named En-
tity Recognition-, dictionary- and rule-based ap-
proaches. It is based on the PrivMasker tool10 and
PolDeepNer2.11 PrivMasker, built upon the spaCy
library (Honnibal and Montani (2017)), enables au-
tomatic detection and masking of selected cate-
gories of personal data. PolDeepNer2, a neural
model based on RoBERTa language model, is one
of the latest and most effective (it scored 0.899 F1-
score measure on the PolEval 2018 set) NER tools
for the Polish language (Marcińczuk et al. (2018);
Marcińczuk and Radom (2021)). Additionally, hy-
perlinks and mentions, i.e. usernames preceded by
the “@” symbol, were masked using regex formula.
Nonetheless, these tools exhibited limitations in
their scope, as they failed to recognize pseudonyms
and differentiate between authentic and fictitious or
historical characters. Instances where names had
been intentionally or inadvertently altered by users
posed further challenges for the models. A process
of fine-tuning became essential to achieve the de-
sired results. Consequently, as an initial measure,
we opted to release a subset of 24,000 posts and
comments, each of which underwent meticulous
manual verification of its anonymization process.
Each piece of content was evaluated by one anno-
tator and verified by a super-annotator according to
detailed guidelines. In total, seven annotators and
two super-annotators (linguists with experience in
annotating social media data) participated in this
process. Simultaneously, based on a review of
prevalent surnames and hashtags across the en-
tire dataset and coupled with expert knowledge,
dictionaries of historical and fictional figures, as
well as popular pseudonyms were developed.
Sensitive information was replaced by the fol-
lowing tags: username, URL, surname (including
user-modified ones and adjectives derived from
surnames), pseudonym, address (including street
10https://github.com/ZILiAT-NASK/
PrivMasker
11https://github.com/CLARIN-PL/
PolDeepNer2
names, house numbers, postal codes), email, pho-
nenumber, number (other numbers, e.g., PESEL).
Examples of their use are given in Tab. 1.
5.
Data specificity
5.1.
Wykop.pl web service
As an online platform for news aggregation,
Wykop.pl is specifically designed to cater to the
interests of the internet audience, offering a wide
range of content spanning various topics such as
sports, economy, trending political affairs, and vi-
ral Internet phenomena. The primary feature of
Wykop.pl is its user-generated content, which al-
lows users to submit and share news stories, arti-
cles, and other forms of media. This user-driven ap-
proach ensures that the platform remains dynamic
and up-to-date, reflecting the diverse interests and
perspectives of its user base.
According to data from verified accounts, the
user base of Wykop.pl predominantly falls within the
18-45 age range, with a notable contribution from
individuals aged 15-24 (Wirtualnemedia.pl (2014)).
Furthermore, the platform exhibits a higher propor-
tion of male users. What is more, Wykop.pl repre-
sents a relatively more closed and potentially more
homogeneous community when compared to the
broader population of online users who generate
content on other platforms. This observation is sup-
ported by the development of its unique sociolect
and semiotic sign system, indicating a distinctive
linguistic and communicative environment within
the platform (Rak (2023); Sowiński (2018)).
One distinctive aspect of Wykop.pl is its voting
system, which enables users to participate in the
curation of content. Users have the ability to vote on
submitted content, either by "digging" or "burying"
it. By digging a post, users express their approval
and contribute to its visibility, while burying a post
indicates disapproval and reduces its prominence
within the platform.
Another distinctive feature is the folksonomy, a
collaborative tagging system system, which en-
hances content organization and discoverability.
Tags serve as metadata, providing additional con-
text and enabling easier navigation and search on
the platform. Furthermore, the Wykop.pl commu-
nity leverages tags to provide context, particularly
when it comes to humor and sarcasm. Users on
the platform often employ tags to indicate the in-
tention behind their posts, allowing others to inter-
pret the content correctly based on their collective
experience and understanding (Sowiński (2018)).
Unlike platforms like Twitter, where tags are often
integrated within the utterances themselves due
to character limits, on Wykop.pl, the tags typically
appear at the end of the utterances.

--- Page 6 ---

Table 1: Examples of anonymized content of the BAN-PL dataset*
Original sample after anonymization (in Polish)
English translation
będziesz pan wisiał, panie [surname]
you will be hanging, mr [surname]
[surname] to glupia c**a i nie nalezy sie jej ten nobel
[surname] is a stupid c**t and she doesn’t deserve this nobel
prize
{USERNAME}: pedała ci żal że się nad ty[m] [pseudonym]
użalasz?
{USERNAME}: do you pitty a f****t since you feel sorry for this
[pseudonym]?
#[pseudonym] k***o pedophilu. Nie jesteś streamerem. Nie
liczysz się w świecie YouTube. Płace 5.000 zł za adres tej
k***y #patostreamy
#[pseudonym] you wh**e pedophile. You’re no streamer. You
don’t count in the YouTube world. I’m paying 5,000 PLN for this
wh***’s address #patostreamy
Do tego świra-pedalarza w lateksach z [address] w Poznaniu -
wyk*****j cwelu i sam patrz do tyłu. Sorry za zj***nie średniej
idioto. #rower #pedalarze
To this kook-pedal pusher in latexes from [address] in Poznan
- f**k off w****r and look back yourself. Sorry to f*** up your
average idiot. #bike #pedalpushers
{URL} c**j Wam na stale, śmiecie z jutuba, czyli urywek os-
tatniego streamu! #[pseudonym] #[pseudonym] #patostreamy
#[pseudonym] #patostreamy
{URL} f**k you forever, jutube trash, that is a snippet from
the last stream! #[pseudonym] #[pseudonym] #patostreamy
#[pseudonym] #patostreamy
[phonenumber] napalona agatka lat 16 lubi BDSM
[phonenumber] horny agatka aged 16 likes BDSM
*This table contains examples of hate speech and vulgar personal attacks. The authors do not support
the use of harmful language, nor any of the harmful representations quoted above.
5.2.
Dataset in numbers
The majority of the BAN-PL dataset comprises
short texts; however, it is important to note that
Wykop.pl entries and comments, unlike many other
social media platforms, such as Twitter, do not
have a specific character limit. Consequently, user-
generated content on Wykop.pl encompasses not
only concise messages but also longer narrative
forms, such as "copypastas" (Kurcwald (2015)).
This factor contributes to the high standard de-
viation observed in the harmful class (see token
statistics for specific classes in tab. 3). In order to
illustrate the evolving landscape of content moder-
ation and its impact over time, we present a visual
representation of the number of pieces of content
banned by Wykop.pl moderation system in subse-
quent quarters from 2019 through 2023 in fig. 2.
Figure 2: Number of posts and comments from the
"harmful" class by quarters
5.3.
Linguistic features
Similar to texts found on other social media plat-
forms, the language used in Wykop.pl posts and
comments is highly informal, replete with numerous
grammatical and syntactical errors, rendering them
challenging to process using NLP tools (Barbieri
et al. (2020)). Simultaneously, many of these er-
rors are intentionally crafted. Users of the platform
purposely incorporate certain popular words with
errors, such as "huop" instead of "chłop" [man] or
"kąkuter" instead of "komputer" [computer]. In this
case, the normalization of the text, including the
correction of linguistic errors, would lead to the loss
of the semantic surplus.
Another form of semantic surplus pertains to
emojis and textual emoticons formed using vari-
ous Unicode and ASCII characters, alongside el-
ements of Zalgo text. Lenny faces, a popular ex-
ample, are textual emoticons utilized to convey a
mischievous mood, imply sexual innuendo, or dis-
rupt online discussions. Wykop.pl users not only
employ established character combinations preva-
lent in internet discourse but also create their own
intricately crafted ones. These combinations often
elude algorithms designed to convert emoticons
or emojis into textual representations. Managing
emojis and emoticons during the text preprocessing
stage presents a challenge when dealing with such
specific data. However, certain portions of this in-
formation might be vital from a sentiment analysis
standpoint. Consequently, in the published dataset,
emojis and textual emoticons have been retained.
Additionally, we provide a script for their removal.
In addition to spelling errors and the use of
graphic characters, the language of BAN-PL, par-
ticularly in the subset of harmful content, is charac-
terised by the extensive use of profanity, including (i)
explicit, non-obfuscated profanities, (ii) profanities

--- Page 7 ---

Table 2: Statistics for the BAN-PL dataset (number of tokens)
Dataset class
count
mean
std
25%
50%
75%
Harmful total (n = 345,831)
12,064,249
34.88
98.48
10
17
35
Harmful flagged (n = 148,386)
7,392,680
37.44
118.05
10
18
35
Harmful predicted (n = 197,445)
4,671,569
31.48
63.55
11
18
34
Neutral (n = 345,831)
14,143,837
40.90
55.87
13
24
47
automatically masked during the platform’s moder-
ation process, often classified as adult content (all
words, no matter the length, are transformed into
the following character string "#!$%@?") and (iii)
profanities intentionally masked by users to evade
detection and potential bans.
Obfuscation strategies (Rojas-Galeano (2017)),
common to a number of social media platform, have
been creatively developed within Wykop.pl commu-
nity. Users circumvent blocking filters by obfuscat-
ing profanities with following strategies12:
1. character substitution, including replacing let-
ters with visually similar characters, especially
numbers, e.g., flower -> fl0w3r, using a string
of identical symbols, usually dots or asterisks,
e.g., flower -> flo...., flower –> flow**, using
random symbols, e.g., flower -> fl*%#$$r
2. phonetic spelling (substituting letters with other
letters that sound similar), e.g., duck -> duq
3. extra character insertion or deletion, e.g., cof-
fee -> coff&ee; coffee -> coff*e
4. splitting or merging, e.g.,coffee -> c o f f e e
While these examples represent the most com-
mon obfuscation strategies, there are numerous
possible variations. Notably, some masking tech-
niques extend beyond explicit profanities to non-
vulgar words. For instance, there is a prevalence
of replacing the letter "o" with a zero in certain
words (e.g., "p0lka" for a Polish woman, "p0lska"
for Poland, "r0sjanie" for Russians). This suggests
that users may harbor negative attitudes towards
these concepts, perceiving them as offensive or
vulgar despite their neutral meanings.
To facilitate dataset management, we have devel-
oped functions for unmasking obfuscated content.
Firstly, we identify all profanities masked with ran-
dom symbols. Next, we generate a list of potential
unmasked versions based on a dictionary of pro-
fanities and the visible letters in the masked word.
To determine the most accurate unmasked word,
we compare the masked word with each proposed
word from the filtered dictionary, considering sym-
bol usage resemblance. Sorting the possible words
by similarity enables us to select the closest match.
The next stage involves identifying letter-to-sign
12Examples of the filters used are presented on the
non-vulgar words.
and letter-to-letter exchanges. This process begins
by recognizing commonly used signs in exchanges,
such as @, 3, $, q, and others. The algorithm then
attempts to create actual representations based on
these popular exchanges (e.g., e->3, l->1). Fol-
lowing this step, the algorithm checks whether the
generated words exist in the FastText dictionary.
Typically, there’s only one matching word at this
point, considered the correct one. However, in
cases of multiple matching words, the algorithm
randomly selects one since it lacks the ability to
determine the best fit based on context.
Despite the inherent challenges posed by social
media content, preliminary analyses utilizing cor-
pus and computational linguistic methodology have
yielded promising results in distinguishing between
offensive and neutral content. Statistical analyses
have revealed several features that tend to weigh
towards the offensive class. Particularly notewor-
thy among these features are morpho-syntactical
structures that support addressative forms, includ-
ing the declination in the vocative case, the use of
the imperative mood, as well as verbs in 2nd per-
son singular and plural in the indicative mood, and
various types of apostrophes (e.g., a noun following
a 2nd person pronoun or a complex nominal phrase
following a 2nd person pronoun). Furthermore, a
more sophisticated task aimed at distinguishing be-
tween offensiveness and generalized hate speech
has also shown potential from a strictly linguistic
perspective. Some initial insights have been elabo-
rated upon in Okulska and Kołos (2023).
5.4.
Unsupervised topic analysis
In our study, we performed topic modeling on
two datasets: the large set of 691,662 samples
and the openly anonymized subset of 24,000
pieces. The method included BERTopic model
utilizing
paraphrase-multilingual-MiniLM-L12-
v2 embeddings and the number of topics set
to 20,
with following parameters for UMAP
(n_neighbors=15, n_components=5, min_dist=0.0,
metric=’cosine’, low_memory=self.low_memory)
and
HDBSCAN
(min_ster_size=10,
met-
ric=’euclidean’, cluster_selection_method=’eom’,
prediction_data=True). The resulting topics were
given simple labels based on keywords and their
representation analysis.
The topics’ count was
normalized to the percentage of the entire set and

--- Page 8 ---

used for the word clouds shown in fig. 3 and 4 as
the size parameter.
Both datasets prominently feature two major top-
ics. The first, "Personal Stories," encompasses
a range of life-related narratives, including obser-
vations, memories, confessions, gossip, and com-
ments on others’ life decisions, varying from neutral
to sarcastic tones. The second, "General Offen-
siveness," aggregates a diverse set of topics under
the broad category of generally offensive and hate-
ful remarks directed at people and their lifestyles.
While these two topics are consistently present
in both datasets, the remaining themes exhibit
more subtlety and are more susceptible to variation.
However, nine specific themes—Economy, Sexual-
ity, Urban Cycling, User Interactions on Wykop.pl,
Diet, Politics, Education, China, and Cars and
races—recur in both datasets. Additionally, two
themes, Climate Change and Waste and Recycling,
closely align, weaving similar threads from slightly
different perspectives.
Figure 3: 20 topics for the anonymized BAN-PL
Figure 4: 20 topics for the entire dataset
5.5.
Preliminary experiments
To evaluate the effectiveness of the proposed
dataset for binary classification task, we conducted
a series of preliminary experiments using four dis-
tinct BERT-based models for the Polish language,
with two of them being trained for identifying specific
types of offensiveness, namely cyberbullying and
hate speech. The RoBERTa base v2 (RoBERTa),
TrelBERT, Polbert-CB,13 and Polish-Hate-Speech-
Detection-Herbert-Large (HerBERT-HS14) model
13https://huggingface.co/ptaszynski/
bert-base-polish-cyberbullying
14https://huggingface.co/dkleczek/
Polish-Hate-Speech-Detection-Herbert-Large
were implemented using the PyTorch framework,
AdamW as the optimizer and learning rate = 5e-5.
All models were fine-tuned on a split of 80% of
the open BAN-PL dataset for training, 10% for vali-
dation, and tested on the remaining 10%, giving the
support count of 2400 samples (with 1191 for neu-
tral and 1209 for the offensive class). The only pre-
processing of the data included the removal of new-
line coding ’\n’ and inserting additional spaces
in the apostrophes between the addressed user
nickname token ’USERNAME:’ and the following
utterance, for leaving it merged into a long string
could bring noise to the model.
Early stopping was employed, monitoring the val-
idation loss with a patience of 5 epochs. Tab. 3
summarizes the results obtained from the prelimi-
nary experiments based on recall, precision, and F1
scores for the offensive class. As expected, fine-
tuning a base model proved more efficient than
fine-tuning an already fine-tuned model, which de-
spite a similar task was initially trained on a different
dataset involving cyberbullying or hate speech.
Table 3: The Results of the preliminary experiments
on the open BAN-PL dataset
Model
Recall
Precision
F1
RoBERTa base v2
0.84
0.83
0.83
TrelBERT
0.76
0.82
0.79
Polbert-CB
0.83
0.78
0.81
HerBERT-HS
0.79
0.80
0.79
6.
Discussion
Based on the literature review and the evaluation of
the leading datasets currently assigned to the task
of offensive language detection for Polish and En-
glish, one can identify the following biases: (i) post-
moderation source bias, (ii) pre-selection bias, (iii)
annotation bias. The first two notions refer directly
to data collection process, in which harmful data
is usually obtained from publicly available social
media content (most notably Twitter) through APIs
based on pre-selection of users, key words or hash-
tags (e.g., Ptaszynski et al. (2019); Davidson et al.
(2017)). As a consequence, obtained data might
have already undergone some initial moderation
resulting in limited number of explicit hateful posts.
Furthermore, these approaches still undermine the
possibility of creating a genuinely representative
corpus of abusive content by collecting relatively
homogeneous data centered around specific top-
ics or targets of hate (Ludwig et al. (2022)). User
distribution is also of crucial value. It has been suc-
cessfully demonstrated that user distribution bias,
resulting from obtaining huge amounts of data from
single users, is also present in often-cited English

--- Page 9 ---

datasets (Arango et al. (2022)). Annotation bias
covers a range of challenges resulting from varying
annotation guidelines, which are rooted in the lack
of consensus on definitions of harmful content and
subjective notions of what constitutes hate speech
(Ross et al. (2017); Waseem and Hovy (2016)), dif-
ferent levels of demographic diversity of annotators,
and the need of reliable inter-annotator agreement.
In this context, the problem of personal bias has
been highlighted (Sap et al. (2019, 2021), see also
(Garg et al., 2022)).
When evaluating BAN-PL dataset from the per-
spective of the above mentioned biases, it is ev-
ident that the first two challenges posed by data
collection are successfully mitigated. The dataset
comprises a huge amount of harmful content, which
was possible due to obtaining data directly from the
moderation team. Another advantage of this ap-
proach is that the harmful content has not been
pre-selected, but comes from a relatively long time
span and covers multiple topics, not limited to the
ones most commonly considered hate-related. Ad-
ditionally, the harmful content was generated by a
large number of unique users, therefore it is free
of user distribution bias. Annotation bias cannot
be easily comparable betweeen BAN-PL and other
annotated datasets, since moderation relied on the
website’s internal policy and was conducted by pro-
fessionals. Thus, we do not have control over an-
notation process or insight into moderators’ demo-
graphic information due to required anonymity and
cannot evaluate possible inherent personal biases.
However, voting system employed within the mod-
eration process facilitates the mitigation of personal
biases.
The moderation process itself, as made evident
in the task of re-annotating KLEJ harmful content
by Wykop.pl moderators (see 3.1), can hinder the
generalization of the model trained on BAN-PL. The
very specific linguistic nature of the content along
with users’ demographics which differs from other
popular social media platforms can also have a
negative impact on generalization, as established
in regard to other datasets (Talat et al. (2018)).
A major advantage of the BAN-PL dataset is the
coverage of multiple topics and hate-related con-
cepts, including personal attacks, generalized hate
speech, and toxicity, as well as a wide range of tar-
gets of attacks, such as public figures, women, and
other protected groups. However, for the purpose of
analyzing specific aspects of hateful language, one
would need to distinguish further subsets, which
require additional manual annotation. Such um-
brella terms, as offensive language or cyberbullying,
cover a wider range of more nuanced phenomena,
which can be considered overlapping. Therefore,
binary approach is often employed, however it may
also be considered too simplistic (Sang and Stan-
ton (2022)). As opposed to the most commonly
utilized datasets of offensive language (Madukwe
et al. (2020)), BAN-PL provides equal classes of
harmful and neutral content. Data collection aimed
at obtaining content which would prove successfully
comparable in terms of topics covered, however the
data comes from slightly different time spans and
may result in overrepresentation of certain trending
topics in the harmful class.
7.
Conclusion and future work
This paper presents several notable contributions:
1. introduction of a new open dataset tailored for
offensive language detection in the Polish lan-
guage. Unlike existing datasets, this collection
comprises texts originally posted online, sub-
sequently flagged by users, and moderated
by professionals for banning. Consequently, it
represents data that was previously inaccessi-
ble, now reconstructed to form an intentional
dataset.
2. the analysis of significant linguistic features
of the content posted on Wykop.pl, which are
relevant when working with the dataset;
3. the identification of biases that the dataset ef-
fectively avoids and those that still persist;
4. a discussion of potential strategies for address-
ing these biases in datasets based on content
removed during the moderation process;
5. the publication of the anonymized open avail-
able subset of the dataset along with prepro-
cessing scripts that can be readily applied in
real-life scenarios.
Additionally, this paper provides valuable insights
into anonymization guidelines and offers an evalu-
ation of the moderation framework.
However, to address further challenges and im-
prove the analysis of the offensive language, we
aim to continue developing preprocessing func-
tions for text normalization and profanity unmask-
ing. Moreover, we aim to advance scholarly under-
standing of online offensive behavior, with a par-
ticular emphasis on studying hate speech directed
at groups based on protected characteristics. We
aim at releasing a subset of hate speech, which
would require manual annotation. This task will fa-
cilitate providing a dictionary of Polish expressions
related to hate speech and offensive language that
can be further applied to a plethora of NLP tasks.
The manually annotated and evaluated subset of
24,000 samples will be used to fine-tune the NER
model. Ultimately, the anonymization of the whole
dataset will be done in an iterative human-in-the-
loop manner, using a refined automatic pipeline
and involving decreasing manual correction.

--- Page 10 ---

8.
Data availability
Owing to the comprehensive anonymization proce-
dure (see 4), the complete dataset will be incremen-
tally released. The initial segment of publication
comprises 24,000 samples, evenly distributed be-
tween harmful and neutral classes, and has already
made available on our GitHub account along with
preprocessing scripts. All forthcoming releases,
including the model and anonymizer, will also be
made available on our GitHub account to ensure
transparency and facilitate the reproducibility of our
research.15
9.
Ethical considerations
The authors of this paper present a novel dataset
focusing on offensive language, cyberbullying, and
hate speech in the Polish language.
The data
was sourced from the popular social news platform
Wykop.pl, in collaboration with Wykop.pl modera-
tors. The collected samples were identified as viola-
tions of the website’s internal policy by the commu-
nity of users and moderators. The authors argue
that this dataset offers distinct advantages com-
pared to resources obtained through public APIs
and manual annotation processes. In compliance
with the Association for Internet Researchers Ethi-
cal Guidelines,16 the authors conducted a thorough
anonymization procedure. This process ensured
that no screen names of authors and sensitive per-
sonal data, such as phone numbers and identifica-
tion numbers, were publicly available. Additionally,
the targets of insults, including public figures like
politicians or celebrities, were also anonymized to
restrict the dissemination of hateful content.
10.
Bibliographical References
Bedour Alrashidi, Amani Jamal, Imtiaz Khan, and
Ali Alkhathlan. 2022. A review on abusive content
automatic detection: approaches, challenges
and opportunities.
PeerJ Computer Science,
8:e1142.
Aymé Arango, Jorge Pérez, and Barbara Poblete.
2022. Hate speech detection is not as easy as
you may think: A closer look at model validation
(extended version). Information Systems, 105.
Francesco Barbieri,
Jose Camacho-Collados,
Leonardo Neves, and Luis Espinosa-Anke. 2020.
Tweeteval: Unified benchmark and comparative
evaluation for tweet classification. In Findings
15https://github.com/ZILiAT-NASK/BAN-PL
16https://aoir.org/reports/ethics3.pdf
of the Association for Computational Linguistics:
EMNLP 2020, pages 1644–1650.
Md Abul Bashar, Richi Nayak, Khanh Luong, and
Thirunavukarasu Balasubramaniam. 2021. Pro-
gressive domain adaptation for detecting hate
speech on social media with small training set
and its application to covid-19 concerned posts.
Social Network Analysis and Mining, 11:1–18.
Valerio Basile, Cristina Bosco, Elisabetta Fersini,
Debora
Nozza,
Viviana
Patti,
Francisco
Manuel Rangel Pardo,
Paolo Rosso,
and
Manuela Sanguinetti. 2019.
Semeval-2019
task 5: Multilingual detection of hate speech
against immigrants and women in twitter.
In
Proceedings of the 13th international workshop
on semantic evaluation, pages 54–63.
Danah Boyd. 2008. Why youth (heart) social net-
work sites: The role of networked publics in
teenage social life. YOUTH, IDENTITY, AND
DIGITAL MEDIA, David Buckingham, ed., The
John D. and Catherine T. MacArthur Foundation
Series on Digital Media and Learning, The MIT
Press, Cambridge, MA, pages 119–142.
Iwona Burkacka. 2020. Janusze, halyny, sebixy i
karyny. memy internetowe jako źródło nowych
eponimów. Poradnik Językowy, (04):21–34.
Tommaso Caselli, Valerio Basile, Jelena Mitrović,
and Michael Granitzer. 2020. Hatebert: Retrain-
ing bert for abusive language detection in english.
arXiv preprint arXiv:2010.12472.
Sylwia Czubkowska and Jakub Wątor. 2021.
Wykop, hejt i zamawianie zlewów. tak się bawi
największy polski serwis społecznościowy.
Sławomir Dadas, Michał Perełkiewicz, and Rafał
Poświata. 2020. Pre-training polish transformer-
based language models at scale. In Artificial In-
telligence and Soft Computing: 19th International
Conference, ICAISC 2020, Zakopane, Poland,
October 12-14, 2020, Proceedings, Part II 19,
pages 301–314. Springer.
Maral Dadvar, Dolf Trieschnigg, Roeland Ordelman,
and Franciska De Jong. 2013. Improving cyber-
bullying detection with user context. In Advances
in Information Retrieval: 35th European Confer-
ence on IR Research, ECIR 2013, Moscow, Rus-
sia, March 24-27, 2013. Proceedings 35, pages
693–696. Springer.
Thomas Davidson, Dana Warmsley, Michael Macy,
and Ingmar Weber. 2017.
Automated hate
speech detection and the problem of offensive
language. In Proceedings of the international
AAAI conference on web and social media, vol-
ume 11, pages 512–515.

--- Page 11 ---

Karthik Dinakar, Birago Jones, Catherine Havasi,
Henry Lieberman, and Rosalind Picard. 2012.
Common sense reasoning for detection, preven-
tion, and mitigation of cyberbullying. ACM Trans-
actions on Interactive Intelligent Systems (TiiS),
2(3):1–30.
Karthik Dinakar, Roi Reichart, and Henry Lieber-
man. 2011. Modeling the detection of textual cy-
berbullying. In Proceedings of the International
AAAI Conference on Web and Social Media, vol-
ume 5, pages 11–17.
Chris Emmery, Ben Verhoeven, Guy De Pauw,
Gilles Jacobs, Cynthia Van Hee, Els Lefever, Bart
Desmet, Véronique Hoste, and Walter Daele-
mans. 2021. Current limitations in cyberbullying
detection: On evaluation criteria, reproducibil-
ity, and data scarcity. Language Resources and
Evaluation, 55:597–633.
Paula Fortuna, Juan Soler-Company, and Leo Wan-
ner. 2021. How well do hate speech, toxicity, abu-
sive and offensive language classification mod-
els generalize across datasets?
Information
Processing & Management, 58(3):102524.
Antigoni-Maria Founta, Constantinos Djouvas, De-
spoina Chatzakou, Ilias Leontiadis, Jeremy
Blackburn, Gianluca Stringhini, Athena Vakali,
Michael Sirivianos, and Nicolas Kourtellis. 2018.
Large scale crowdsourcing and characterization
of twitter abusive behavior. In Proceedings of the
international AAAI conference on web and social
media, volume 12.
Tanmay Garg, Sarah Masud, Tharun Suresh, and
Tanmoy Chakraborty. 2022. Handling bias in
toxic speech detection: A survey. ACM Comput-
ing Surveys.
gazeta.pl. 2006. Wykop.pl, czyli digg.com po pol-
sku. Gazeta Wyborcza.
Tommi Gröndahl, Luca Pajola, Mika Juuti, Mauro
Conti, and N Asokan. 2018. All you need is" love"
evading hate speech detection. In Proceedings of
the 11th ACM workshop on artificial intelligence
and security, pages 2–12.
Hugo Lewi Hammer. 2017. Automatic detection
of hateful comments in online discussion. In In-
dustrial Networks and Intelligent Systems: Sec-
ond International Conference, INISCOM 2016,
Leicester, UK, October 31–November 1, 2016,
Proceedings 2. Springer International Publishing.
Matthew Honnibal and Ines Montani. 2017. spaCy
2: Natural language understanding with Bloom
embeddings, convolutional neural networks and
incremental parsing. To appear.
Md Saroar Jahan and Mourad Oussalah. 2023. A
systematic review of hate speech automatic de-
tection using natural language processing. Neu-
rocomputing, page 126232.
Mladen Karan and Jan Šnajder. 2018.
Cross-
domain detection of abusive language online. In
Proceedings of the 2nd workshop on abusive
language online (ALW2), pages 132–137.
Simrat Kaur, Sarbjeet Singh, and Sakshi Kaushal.
2021. Abusive content detection in online user-
generated data: a survey. Procedia Computer
Science, 189:274–281.
Przemysław Kazienko, Julita Bielaniewicz, Marcin
Gruza, Kamil Kanclerz, Konrad Karanowski, Pi-
otr Miłkowski, and Jan Kocoń. 2023. Human-
centered neural reasoning for subjective content
processing: Hate speech, emotions, and humor.
Information Fusion, 94:43–65.
Aleksandra
Klimkiewicz.
2022.
#
ros-
jatostanumyslu# 60kopiejekzawpis: stereotypy
etniczne zaklęte w hasztagach.
Przegląd
Rusycystyczny, (4 (180)).
Łukasz Kobyliński, Maciej Ogrodniczuk, Jan Ko-
coń, Michał Marcińczuk, Aleksander Smywiński-
Pohl, Krzysztof Wołk, Danijel Koržinek, Michal
Ptaszynski, Agata Pieciukiewicz, and Paweł Dy-
bała. 2019. Poleval 2019—the next chapter in
evaluating natural language processing tools for
polish. pages 165–172.
Jan Kocoń, Alicja Figas, Marcin Gruza, Daria
Puchalska, Tomasz Kajdanowicz, and Prze-
mysław Kazienko. 2021. Offensive, aggressive,
and hate speech analysis: From data-centric to
human-centered approach. Information Process-
ing & Management, 58(5):102643.
Anna Koufakou, Endang Wahyu Pamungkas, Va-
lerio Basile, Viviana Patti, et al. 2020. Hurtbert:
Incorporating lexical features with bert for the de-
tection of abusive language. In Proceedings of
the fourth workshop on online abuse and harms,
pages 34–43. Association for Computational Lin-
guistics.
Adam Kręgielewski and Monika Turek. 2020. Prze-
wodnik po social media w polsce.
Michał Kurcwald. 2015.
Copypasta: na grani-
cach literatury, grup społecznych i dyscyplin
badawczych. In Literatura na granicach. Mono-
grafia naukowa. Kraków: AT Wydawnictwo.
Nikola Ljubešić, Tomaž Erjavec, and Darja Fišer.
2018. Datasets of Slovene and Croatian moder-
ated news comments. In Proceedings of the 2nd
Workshop on Abusive Language Online (ALW2),

--- Page 12 ---

pages 124–131, Brussels, Belgium. Association
for Computational Linguistics.
Florian Ludwig, Klara Dolos, Torsten Zesch, and
Eleanor Hobley. 2022. Improving generalization
of hate speech detection systems to novel target
groups via domain adaptation. In Proceedings of
the Sixth Workshop on Online Abuse and Harms
(WOAH), pages 29–39.
Sean MacAvaney, Hao-Ren Yao, Eugene Yang,
Katina Russell, Nazli Goharian, and Ophir
Frieder. 2019.
Hate speech detection: Chal-
lenges and solutions. PloS one, 14(8):e0221152.
Kosisochukwu Madukwe, Xiaoying Gao, and Bing
Xue. 2020. In data we trust: A critical analysis of
hate speech detection datasets. In Proceedings
of the Fourth Workshop on Online Abuse and
Harms, pages 150–161, Online. Association for
Computational Linguistics.
Michał Marcińczuk and Jarema Radom. 2021. A
single-run recognition of nested named entities
with transformers. Procedia Computer Science,
192:291–297.
Michał Marcińczuk, Jan Kocoń, and Michał Gawor.
2018. Recognition of named entities for polish-
comparison of deep learning and conditional ran-
dom fields approaches. In Proceedings of the
PolEval 2018 Workshop, pages 77–92. Institute
of Computer Science, Polish Academy of Sci-
ence.
Inez Okulska and Anna Kołos. 2023. A morpho-
syntactic analysis of human-moderated hate
speech samples from wykop. pl web service.
Półrocznik Językoznawczy Tertium, 8(2):54–71.
Inez Okulska and Anna Zawadzka. 2022. Styles
with benefits. the stylometrix vectors for stylistic
and semantic text classification of small-scale
datasets and different sample length.
Fabio Poletto, Valerio Basile, Manuela Sanguinetti,
Cristina Bosco, and Viviana Patti. 2021.
Re-
sources and benchmark corpora for hate speech
detection: a systematic review. Language Re-
sources and Evaluation, 55:477–523.
Michal Ptaszynski, Pawel Dybala, Tatsuaki Mat-
suba, Fumito Masui, Rafal Rzepka, and Kenji
Araki. 2010. Machine learning and affect analy-
sis against cyber-bullying. the 36th AISB, pages
7–16.
Michal Ptaszynski, Fumito Masui, Taisei Nitta,
Suzuha Hatakeyama, Yasutomo Kimura, Rafal
Rzepka, and Kenji Araki. 2016. Sustainable cy-
berbullying detection with category-maximized
relevance of harmful phrases and double-filtered
automatic optimization. International Journal of
Child-Computer Interaction, 8:15–30.
Michal Ptaszynski, Agata Pieciukiewicz, and Paweł
Dybała. 2019. Results of the poleval 2019 shared
task 6: First dataset and open shared task for
automatic cyberbullying detection in polish twit-
ter.
Michal Ptaszynski, Agata Pieciukiewicz, Pawel Dy-
bala, Pawel Skrzek, Kamil Soliwoda, Marcin For-
tuna, Gniewosz Leliwa, and Michal Wroczynski.
2023. Expert-annotated dataset to study cyber-
bullying in polish language. Data, 9(1):1.
Jing Qian, Anna Bethke, Yinyin Liu, Elizabeth Beld-
ing, and William Yang Wang. 2019. A benchmark
dataset for learning to intervene in online hate
speech. arXiv preprint arXiv:1909.04251.
Oskar Rak. 2023. Mirkomowa dla początkujących -
słownik wykopowiczów.
Sergio Rojas-Galeano. 2017. On obstructing ob-
scenity obfuscation. ACM Transactions on the
Web (TWEB), 11(2):1–24.
Björn Ross, Michael Rist, Guillermo Carbonell, Ben-
jamin Cabrera, Nils Kurowsky, and Michael Wo-
jatzki. 2017. Measuring the reliability of hate
speech annotations: The case of the european
refugee crisis. arXiv preprint arXiv:1701.08118.
Paul Röttger, Bertie Vidgen, Dirk Hovy, and Janet B
Pierrehumbert. 2021. Two contrasting data anno-
tation paradigms for subjective nlp tasks. arXiv
preprint arXiv:2112.07475.
Piotr Rybak, Robert Mroczkowski, Janusz Tracz,
and Ireneusz Gawlik. 2020. Klej: Comprehensive
benchmark for polish language understanding.
arXiv preprint arXiv:2005.00630.
Joni
O.
Salminen,
Hind
Almerekhi,
Milica
Milenkovic, Soon-Gyo Jung, Jisun An, Haewoon
Kwak, and Bernard Jim Jansen. 2018. Anatomy
of online hate:
Developing a taxonomy and
machine learning models for identifying and
classifying hate in online news media. In Pro-
ceedings of the International AAAI Conference
on Web and Social Media, volume 12.
Yisi Sang and Jeffrey Stanton. 2022. The origin
and value of disagreement among data labelers:
A case study of individual differences in hate
speech annotation. In Information for a Better
World: Shaping the Global Future: 17th Inter-
national Conference, iConference 2022, Virtual
Event, February 28–March 4, 2022, Proceedings,
Part I, pages 425–444. Springer.

--- Page 13 ---

Maarten Sap, Dallas Card, Saadia Gabriel, Yejin
Choi, and Noah A Smith. 2019. The risk of racial
bias in hate speech detection. In Proceedings
of the 57th annual meeting of the association for
computational linguistics, pages 1668–1678.
Maarten Sap, Swabha Swayamdipta, Laura Vianna,
Xuhui Zhou, Yejin Choi, and Noah A Smith. 2021.
Annotators with attitudes: How annotator be-
liefs and identities bias toxic language detection.
arXiv preprint arXiv:2111.07997.
Nina Seemann, Yeong Su Lee, Julian Höllig, and
Michaela Geierhos. 2023.
Generalizability of
abusive language detection models on homoge-
neous german datasets. Datenbank-Spektrum,
pages 1–11.
Rafał Sowiński. 2018.
Rola systemu tagów w
serwisie wykop. pl folksonomia czy memy?
Zeszyty Naukowe Państwowej Wyższej Szkoły
Zawodowej im. Witelona w Legnicy, 3(28):201–
212.
Ellen Spertus. 1997. Smokey: Automatic recog-
nition of hostile messages. In Aaai/iaai, pages
1058–1065.
Steve Durairaj Swamy, Anupam Jamatia, and Björn
Gambäck. 2019. Studying generalisability across
abusive language detection datasets. In Pro-
ceedings of the 23rd conference on computa-
tional natural language learning (CoNLL), pages
940–950.
Wojciech Szmyd, Alicja Kotyla, Michał Zobniów,
Piotr Falkiewicz, Jakub Bartczuk, and Artur
Zygadło. 2023.
TrelBERT: A pre-trained en-
coder for Polish Twitter. In Proceedings of the
9th Workshop on Slavic Natural Language Pro-
cessing 2023 (SlavicNLP 2023), pages 17–24,
Dubrovnik, Croatia. Association for Computa-
tional Linguistics.
Zeerak Talat, James Thorne, and Joachim Bingel.
2018. Bridging the gaps: Multi task learning for
domain transfer of hate speech detection. Online
harassment, pages 29–55.
Marek Troszyński and Aleksander Wawer. 2017.
Czy komputer rozpozna hejtera? wykorzystanie
uczenia maszynowego (ml) w jakościowej anal-
izie danych. Przegląd Socjologii Jakościowej,
13(2):62–80.
Bertie Vidgen and Leon Derczynski. 2020. Direc-
tions in abusive language training data, a sys-
tematic review: Garbage in, garbage out. Plos
one, 15(12):e0243300.
William Warner and Julia Hirschberg. 2012. Detect-
ing hate speech on the world wide web. In Pro-
ceedings of the second workshop on language
in social media, pages 19–26.
Zeerak Waseem. 2016. Are you a racist or am i see-
ing things? annotator influence on hate speech
detection on twitter. In Proceedings of the first
workshop on NLP and computational social sci-
ence, pages 138–142.
Zeerak Waseem and Dirk Hovy. 2016. Hateful sym-
bols or hateful people? predictive features for
hate speech detection on twitter. In Proceedings
of the NAACL student research workshop, pages
88–93.
Michael Wiegand, Josef Ruppenhofer, and Thomas
Kleinbauer. 2019. Detection of abusive language:
the problem of biased datasets. In Proceedings
of the 2019 conference of the North American
Chapter of the Association for Computational Lin-
guistics: human language technologies, volume
1 (long and short papers), pages 602–608.
Wirtualnemedia. 2018. Wśród polskich użytkown-
ików twittera przeważają mężczyźni, osoby z
dużych miast i ze średnim lub wyższym wyksz-
tałceniem (analiza).
Wirtualnemedia. 2023. Na tiktoku godzinę dłużej
niż na facebooku. twitter dalej traci polskich in-
ternautów.
Wirtualnemedia.pl. 2014. Wykop.pl rekordowo pop-
ularny. jacy są jego użytkownicy?
Ellery Wulczyn, Nithum Thain, and Lucas Dixon.
2017. Ex machina: Personal attacks seen at
scale. In Proceedings of the 26th international
conference on world wide web, pages 1391–
1399.
Piotr Wójcik. 2021. A wy za ile harujecie? Dziennik
Gazeta Prawna, 49 (5457):11.
Jun-Ming Xu, Kwang-Sung Jun, Xiaojin Zhu, and
Amy Bellmore. 2012.
Learning from bullying
traces in social media. In Proceedings of the
2012 conference of the North American chapter
of the association for computational linguistics:
Human language technologies, pages 656–666.
Kichang Yang, Wonjun Jang, and Won Ik Cho.
2022.
Apeach: Attacking pejorative expres-
sions with analysis on crowd-generated hate
speech evaluation datasets.
arXiv preprint
arXiv:2202.12459.
Wenjie Yin and Arkaitz Zubiaga. 2021. Towards
generalisable hate speech detection: a review
on obstacles and solutions. PeerJ Computer
Science, 7:e598.

--- Page 14 ---

Shuzhou Yuan, Antonis Maronikolakis, and Hin-
rich Schütze. 2022. Separating hate speech and
offensive language classes via adversarial debi-
asing. In Proceedings of the Sixth Workshop on
Online Abuse and Harms (WOAH), pages 1–10.
Marcos Zampieri, Shervin Malmasi, Preslav Nakov,
Sara Rosenthal, Noura Farra, and Ritesh Ku-
mar. 2019a. Predicting the type and target of
offensive posts in social media. arXiv preprint
arXiv:1902.09666.
Marcos Zampieri, Shervin Malmasi, Preslav Nakov,
Sara Rosenthal, Noura Farra, and Ritesh Kumar.
2019b. Semeval-2019 task 6: Identifying and
categorizing offensive language in social media
(offenseval). arXiv preprint arXiv:1903.08983.
Rui Zhao, Anna Zhou, and Kezhi Mao. 2016. Au-
tomatic detection of cyberbullying on social net-
works based on bullying features. In Proceedings
of the 17th international conference on distributed
computing and networking, pages 1–6.
Xin Zhou, Yi Lu, Ruotian Ma, Tao Gui, Qi Zhang,
and Xuanjing Huang. 2023. Making harmful be-
haviors unlearnable for large language models.
arXiv preprint arXiv:2311.02105.

```
