---
title: "2025-Magdy-Fabricating Holiness Characterizing Religious Misinformation Circulators - PDF Extract"
source_pdf: "2025-Magdy-Fabricating Holiness Characterizing Religious Misinformation Circulators.pdf"
pages: 16
extracted_at: "2026-02-13T09:15:44.940345"
---

# PDF Extract: 2025-Magdy-Fabricating Holiness Characterizing Religious Misinformation Circulators

**Source PDF:** 2025-Magdy-Fabricating Holiness Characterizing Religious Misinformation Circulators.pdf
**Total Pages:** 16

---

## Content

```
--- Page 1 ---

Fabricating Holiness: Characterizing Religious Misinformation Circulators on
Arabic Social Media
Mahmoud Fawzi, Bj¨orn Ross, Walid Magdy
School of Informatics, The University of Edinburgh, Edinburgh, UK
m.f.g.ibrahim@sms.ed.ac.uk, b.ross@ed.ac.uk, wmagdy@inf.ed.ac.uk
Abstract
Misinformation is a growing concern in a decade involving
critical global events. While social media regulation is mainly
dedicated towards the detection and prevention of fake news
and political misinformation, there is limited research about
religious misinformation which has only been addressed
through qualitative approaches. In this work, we study the
spread of fabricated quotes (Hadith) that are claimed to be-
long to Prophet Muhammad (the prophet of Islam) as a
case study demonstrating one of the most common religious
misinformation forms on Arabic social media. We attempt
through quantitative methods to understand the characteris-
tics of social media users who interact with fabricated Ha-
dith. We spotted users who frequently circulate fabricated
Hadith and others who frequently debunk it to understand
the main differences between the two groups. We used Lo-
gistic Regression to automatically predict their behaviors and
analyzed its weights to gain insights about the characteris-
tics and interests of each group. We find that both fabricated
Hadith circulators and debunkers have generally a lot of ties
to religious accounts. However, circulators are identified by
many accounts that follow the Shia branch of Islam, Sunni Is-
lamic public figures from the gulf countries, and many Sunni
non-professional pages posting Islamic content. On the other
hand, debunkers are identified by following academic Islamic
scholars from multiple countries and by having more intellec-
tual non-religious interests like charity, politics, and activism.
Introduction
A hadith is any speech, discussion, action, approval, and
physical or moral description attributed to the Prophet
Muhammad, whether supposedly or truly (Saloot et al.
2016). It is one of the two major sources of the Islamic reli-
gion along with the Quran, which is the holy book of Mus-
lims (Khan et al. 1983). Historically, people starting fab-
ricating hadiths for political gains as early as 25 years af-
ter the death of the Prophet Muhammad (Usman and Wazir
2018). Nowadays, social media is facilitating the spread
of fabricated hadiths among other types of misinformation
(Hakak et al. 2022). This can be critical because Hadith, as a
highly respected resource of knowledge for Muslims, is usu-
ally used for argumentation (Boutz, Brugman, and Lancaster
2017). This led to serious consequences in the past decade
Copyright © 2025, Association for the Advancement of Artificial
Intelligence (www.aaai.org). All rights reserved.
when ISIS used some non-authentic hadiths along with au-
thentic ones as a tool for recruiting members and promoting
their agenda worldwide (Boutz, Benninger, and Lancaster
2019).
Many taxonomies, that attempt to break down the topic of
misinformation, link it mainly with fake news and political
false information (Zannettou et al. 2019; Molina et al. 2021;
Kapantai et al. 2021). However, the volatile global events
that occurred during the current decade motivated investigat-
ing other specific flavors of misinformation, such as medical
misinformation (Teplinsky et al. 2022), corporate misinfor-
mation (Zhou, ˇS´cepanovi´c, and Quercia 2024) and religious
misinformation (Alimardani and Elswah 2020). Southwell
et al. (2022) highlighted the difference between political
misinformation and scientific misinformation and defined
the later as publicly available information that is mislead-
ing or deceptive relative to the best available scientific ev-
idence. As for the religion of Islam, Islamic studies have
many branches each having different complex methodolog-
ical approaches for verifying information (Bennett 2015).
Hadith criticism, which includes determining the authentic-
ity of a religious excerpt claimed to be a hadith, is a crucial
branch of Islamic studies (Azami 2002).
There has been very limited work on the presence of Ha-
dith on social media. One recent study by Fawzi, Magdy,
and Ross (2025) shows that fabricated hadiths are widely
spread on Arabic social media. Nevertheless, we are not
aware of studies that analyzed such special type of misin-
formation (religious), existing within an understudied com-
munity (Muslim world), and spread in an understudied lan-
guage (Arabic). Although there are a lot of early and re-
cent works that propose techniques for Hadith authentication
(Ghazizadeh et al. 2008; Gaanoun and Alsuhaibani 2022),
they do not consider the practical contexts and the dynamic
formats in which Hadith is exchanged among individuals on
the internet.
Hadith fabrication as a form of religious misinformation
has also received very little attention on social media plat-
forms compared to other religious incidences linked with US
politics. Figure 1 illustrates this: it shows community notes
added by readers on X in response to a tweet by an Amer-
ican senator that linked the foundation of the United States
to Christianity. In contrast, we are not aware of any tweets
including a non-authentic hadith that received a similar in-
arXiv:2508.07845v1  [cs.SI]  11 Aug 2025

--- Page 2 ---

Figure 1: Two tweets with religious misinformation in English (left) and Arabic (right). English tweet received community
notes to clarify the context of English misinformation, while the Arabic tweet sharing a non-authentic hadith received nothing.
teraction to the example shown in Figure 1. In this study, we
try to fill this gap by looking at Hadith fabrication through
a social lens. We track the interactions of social media users
with fabricated Hadith aiming to check if there are any sig-
nificant differences between users who circulate fabricated
Hadith and those who debunk it. In particular, we address
the following two research questions:
• RQ1: How to identify a user’s general behavior towards
fabricated Hadith in terms of circulation and debunking?
• RQ2: What are the key network ties of users that help
identify such behaviors?
Our analysis provides a better understanding of the na-
ture of users sharing fabricated Hadith in contrast to those
who carefully examine its authenticity. This analysis pro-
vides a decent building block for systems combating and
raising awareness against religious misinformation using the
characteristics of users interacting with it. We observe that
the networks of both classes of users who interact with fabri-
cated Hadith contain a lot of religious accounts. Circulators
are mainly identified by accounts that follow the Shia branch
of Islam, Sunni scholars from the gulf countries, and many
non-professional Sunni pages posting Islamic content. On
the other hand, debunkers are identified by Islamic schol-
ars from more diverse countries and by having more diverse
interests like politics, charity and activism.
Background and Related Work
Hadith
The word Hadith (in Arabic IK
Yg) literally means commu-
nication, story, or conversation: religious or secular, histor-
ical or recent (Azmi, Al-Qabbany, and Hussain 2019). It is
used as a proper noun in Arabic to refer to the sayings or ac-
tions of Muhammad, the prophet of Islam (Binbeshr, Kam-
sin, and Mohammed 2021). Hadiths are highly regarded in
mainstream Islamic faith and play a vital role in shaping Is-
lamic laws. Each hadith includes a chain of narrators tracing
its transmission back to the original source who is Prophet
Muhammad. Islamic scholars compiled these narrations into
distinct collections one to two centuries after Muhammad’s
death.
Islamic scholars have long been aware of the importance
of Hadith authentication and have developed an entire sci-
ence for it. The two main branches of Islam, Sunni and
Shia, disagree which sources are credible for verifying Ha-
dith (Saloot et al. 2016). The authenticity of a hadith is
based on its chain of narrators who narrated the hadith of the
prophet Muhammad, called Isnad (in Arabic XA	J@). While
Sunni scholars trust the companions of the prophet Muham-
mad as credible sources of Hadith transfer, Shia scholars dis-
credit many of the prophet’s companions except for a hand-
ful. They only accept hadiths that have been reported by or
attributed to the descendants of Muhammad and their sup-
porters (Azmi, Al-Qabbany, and Hussain 2019).
The levels of Hadith authenticity according to Islamic
scholars are authentic, good, weak, and fabricated (Abde-
laal et al. 2019). An authentic hadith is the one with a strong
evidence of belonging to the prophet. A good hadith is the
one with a less strong yet acceptable evidence of belonging
to the prophet. A weak hadith has no acceptable evidence of
belonging to the prophet. Finally, a fabricated hadith has a
strong evidence of not belonging to the prophet. The precise
definition of evidence varies among the schools of Islamic
scholars but it is generally related to the evaluation of the
narrator chain part of that hadith. There is a disagreement

--- Page 3 ---

between different Muslim scholars on the authenticity lev-
els of some hadiths, and this discrepancy increases among
Sunni and Shia Muslims.
Hadith is present in the daily lives of most Muslims.
Fawzi, Magdy, and Ross (2025) show that Hadith is be-
ing shared on social media with a high volume every day
and that there are multiple incidents in which some Ha-
dith deployments went viral on social media causing social
discourse. They also show that some of the widely shared
hadiths on social media are actually fabricated. Although
extensive research has been conducted on misinformation,
there is a notable gap in the study of religious misinfor-
mation, specifically, the dissemination of fabricated Hadith
among Arab and Muslim communities on social media plat-
forms.
Hadith Digital Authentication
Some researchers attempted to automate tasks associated
with Hadith such as topical classification, authentication,
and question answering. There are multiple literature re-
views summarizing these attempts (Saloot et al. 2016; Azmi,
Al-Qabbany, and Hussain 2019; Binbeshr, Kamsin, and Mo-
hammed 2021; Sulistio et al. 2023) and showing that a big
portion of them focused on Hadith authentication in Arabic.
The techniques used for this task included rule-based meth-
ods (Ibrahim et al. 2016; Kabir et al. 2018, 2019), classical
machine learning models (Hassaine, Safi, and Jaoua 2016;
Najiyah et al. 2017; Abdelaal et al. 2019), and transformer
models (Gaanoun and Alsuhaibani 2022). One key limita-
tion of these studies is that authentication is mainly per-
formed on hadith texts from literature books. The gold labels
for all such texts already exist which questions the utility of
such systems. The contexts where Hadith authentication is
required include incidents were Hadith is quoted in social
media threads, news articles, or official talks.
There are two valuable Hadith datasets that include the
hadith along with its level of authenticity: the LK Corpus
(Altammami, Atwell, and Alsalka 2020) and MAHADDAT
(Gaanoun and Alsuhaibani 2022). The LK Corpus includes
34K hadiths in Arabic, their translation in English, and their
degree of authenticity. MAHADDAT includes the authentic
Hadith from LK corpus and a list of 2.4K fabricated hadiths
that were crawled from multiple Islamic websites.
Online Religious Activity
Social scientists have a growing interest in understanding
how digital technologies impact the religious and social lives
of users. This includes Christianity, e.g. ‘online churches’
(Hutchings 2017a) and the digital Bible (Hutchings 2017b),
Judaism (Tsuria 2020), and Islam (Fakhruroji 2021).
Analytical studies that address digital religion are limited
compared to the number of digital applications that people
use in this domain (Buie and Blythe 2013; Wolf, Friedrich,
and Hurtienne 2024). Nevertheless, the research community
has investigated the effect of religion on critical topics like
sustainability (Rifat, Toriq, and Ahmed 2020), women’s in-
clusion (Ibtasam et al. 2019), hate speech (Kursuncu et al.
2019; Albadi, Kurdi, and Mishra 2022), online harassment
(Bhimdiwala, Adavi, and Arif 2024), and health (Ibrahim,
Nurain, and Clawson 2024). Focused research on design-
ing better digital religious experiences is also common (Kim
et al. 2022; Markum et al. 2023; Wolf et al. 2022; Claisse
and Durrant 2023).
There is another set of studies that investigate the role of
religion in global events or daily lives by performing quan-
titative analysis on big social data. For example, Chandra
et al. (2021) presented the CoronaBias dataset which high-
lighted the Islamophobic hate speech that existed amid the
COVID-19 pandemic. Abokhodair, Elmadany, and Magdy
(2020) analyzed the presence of Quran verses on Twitter and
researched into the motives of people who share it. While an-
alytical research is still lacking studies on religion and spiri-
tuality, it lacks even more this type of studies that contribute
social knowledge to the community rather than proposing
experimental designs (Wolf, Friedrich, and Hurtienne 2024).
We hope that our work will be one of those studies that pro-
vide additional knowledge for better understanding of on-
line behavior and better understanding of the online social
ecosystem.
There are few studies on religious misinformation that
mainly addressed the topic through qualitative or narrative
approaches. For example, Alimardani and Elswah (2020)
discuss how religious misinformation manipulates people to
take fake religious remedies to illnesses in general and the
case of COVID-19 in particular. Interestingly, they point out
to the problem of the spread of False hadiths. Even quantita-
tive methods like (Al-Zaman 2024) address the bias against
specific religious groups through fake stories about them but
they do not explore the incidences where religion itself is
misused or fabricated.
Misinformation Personas
There are few studies that focus on the users who interact
with misinformation compared to the ones that try to de-
tect misinformation (Fawzi and Magdy 2024). These studies
agree that there is a topology describing how misinforma-
tion propagates (Morales, Berriche, and Cointet 2023; Ben-
kler et al. 2020; Mosleh and Rand 2022; Introne et al. 2018;
Prochaska et al. 2023). This topology involves complex pat-
terns of information exchange. For example, quotes of of-
ficials are reported as news even if those quotes themselves
are misleading (Benkler et al. 2020). True news are abused to
support fake claims by providing inaccurate interpretations
for them (Introne et al. 2018). Public figures contribute to
performing what is called ”Elite Misinformation” (Mosleh
and Rand 2022) but they do it in a way that does not hold
them accountable (Prochaska et al. 2023).
The task of identifying fake news spreaders was per-
formed using different sets of features including retweets
(Caldarelli et al. 2021), replies (Weinzierl, Hopfer, and
Harabagiu 2021), language-independent textual features
(Vogel and Meghana 2020), and network structure (Rath,
Salecha, and Srivastava 2020). However, digging deeper and
investigating the common characteristics of those users and
others who do opposite behaviors are less common (Mu,
Niu, and Aletras 2022; Fawzi and Magdy 2024). Recent
analyses suggest that this characterization is really essential
since people do not stop following misinformation spreaders

--- Page 4 ---

over time (Ashkinaze, Gilbert, and Budak 2024). Although
the percentage of content including misinformation on the
web is estimated to be very limited (Morales, Berriche,
and Cointet 2023), most of this content still doesn’t get
debunked, which makes the exploration and capitalization
of the debunking behavior an essential research direction
besides exploring the spreading behavior (Miyazaki et al.
2023).
Data & Methods
In this section, we explain our approach to collect the re-
quired data for the study and to identify the characteristics
of users interacting with fabricated Hadith as a case study
for religious misinformation.
User Group Definitions
We chose Twitter for our study as it is the same medium
where earlier studies found fabricated Hadith (Fawzi,
Magdy, and Ross 2025). We recognize two significant
groups of users interacting with fabricated Hadith in Arabic
on X (formerly Twitter):
• Circulators: The accounts that frequently tweet or
retweet scriptures identified as fabricated Hadith.
• Debunkers: The accounts that have replied to threads in-
cluding fabricated Hadith stating they are fabricated or
have tweeted warnings about non-authentic hadiths.
While most similar studies focused mainly on circulators,
a proper definition of an opposing behavior allows statisti-
cal models to capture signals about worrying features that
characterize such accounts as well as healthy features that
indicate a relatively immune account when found among
the network. This definition handles the limitation of ear-
lier studies that consider sharing true news (Leonardi and
Rizzo 2021) or not sharing some specific fake news (Vogel
and Meghana 2020) to be opposite behaviors. It also con-
tributes to the limited yet important research conducted to
characterize debunkers of misinformation (Miyazaki et al.
2023).
Data Collection
We use Twitter API for all of the stages of the data collection
process. The data was collected from March 2023 until the
restriction of the API in May 2023. Figure 5 in the appendix
shows visually the detailed steps of data collection that we
present below.
Stage 1:
We collected tweets that include fabricated Ha-
dith and those that include refutes or warnings against fabri-
cated Hadith. To get a list of fabricated hadiths, we used the
following three seeds:
• Seed 1: The MAHADDAT dataset (Gaanoun and
Alsuhaibani 2022) includes 2,452 fabricated hadiths
scraped from multiple Islamic websites. We used them
to query Twitter and 269 of them returned non-empty re-
sponses. These responses had a total of 25,809 tweets
with 20,284 unique authors.
Refuting Term
English Translation
Refuting Term
English Translation
¨ñ 	ñÓ IK
Yg
Fabricated hadith
¼Q. 	®Ó IK
Yg
Fabricated hadith
øQ	®Ó IK
Yg
Forged hadith
iJ
m Q
	« IK
Yg
Incorrect hadith
H. ð 	YºÓ IK
Yg
Fake hadith
é<Ë@ ÈñP úÎ« H. 	Y» IK
Yg A lie about the prophet
i
 B IK
Yg
Incorrect hadith
éË É@ B IK
Yg
hadith with no origin
i
 B : ék. PYË@
Degree: Incorrect
	­J
ª 	 IK
Yg
Weak hadith
¨ñ 	ñÓ : ék. PYË@
Degree: Fabricated
iJ
m 
Ë IK
Yg
hadith not correct
XQK
 ÕË IK
Yg
a hadith never mentioned
ÊJ	m× IK
Yg
Feigned hadith
Table 1: A list of the refuting terms in Arabic used for
data collection and refutes counting along with their English
translation.
• Seed 2: Islamweb1 is the most visited Islamic website
worldwide and one of the top five most visited websites
under the category of Faith & Belief according to Sim-
ilarweb2. Muslims visit it to ask about the rules of Is-
lam or about the perspective of Islam regarding some life
situations. The website has a dedicated section for ques-
tions about whether a hadith is authentic or not where
non-authentic hadiths are grouped together in an archive.
We scraped the pages of this archive and use its ha-
diths to query Twitter in the same way we did with MA-
HADDAT. 84 out of the 1,113 queries returned non-
empty responses resulting in 9,360 hadith tweets with
7,186 unique authors. Since Islamweb was not among
the websites used to construct MAHADDAT, we investi-
gated the number of hadiths that exist in both sources. We
found that there are only 39 repeated hadiths that exist in
both sources which confirms that Islamweb enriched our
dataset with a different set of fabricated hadiths.
• Seed 3: Finally, we used a list of hadith refuting terms
to search Twitter. Table 1 includes 14 phrases that are
used by Muslim Arabs to indicate that a hadith is not
authentic. We used those phrases to query Twitter, and
whenever any of the retrieved tweets are replies, the par-
ent tweet was also collected. This resulted in a total of
3,928 tweets with 3,234 unique authors.
Since the websites used by MAHADDAT as well as the
website Islamweb tend to use the Sunni approach of evalu-
ating Hadith authenticity, we asked a Shia scholar to label
the top 62 hadiths that appeared in our dataset more than
once to validate if they are also considered fabricated ac-
cording to the Shia’s school. The scholar spotted 15 hadiths
that are considered acceptable by Shia while seen fabricated
by Sunnis3. We filtered out the data extracted based on these
15 hadiths so that our study focuses on hadiths that are con-
sidered fabricated by both schools.
Stage 2:
In this stage, we attempt to collect accounts with
an opposing behavior to the authors collected in the previous
1islamweb.net
2similarweb.com/top-websites/community-and-society/faith-
and-beliefs/
3The Shia scholar provided us with the four main measures he
used to qualify a hadith to be acceptable from a Shia perspective:
1) has an Isnad. 2) exists in one of the canonical Shia books like
Al-Kafi; 3) does not contradict the Quran. 4) does not contradict the
fundamentals of the Shia doctrine.

--- Page 5 ---

stage. For this we utilize the replies on the collected original
tweets and the original tweets of the collected replies.
• For seed 1 (MAHADDAT), we collect the 118 replies
that included refuting terms and authored by 91 unique
users.
• For seed 2 (Islamweb), we collect 86 replies that included
refuting terms and authored by 75 unique users.
• For seed 3, 1,974 refuting tweets were replies to original
tweets, we identify the authors of 1,036 unique original
tweets.
Stage 3:
In this stage, we collect network interactions of
all the authors of original tweets and replies from the three
seeds. This includes all the accounts they follow, all the ac-
counts that author what they retweet in their recent timeline,
and all the accounts that author what they like in their re-
cent timeline. The maximum number of tweets that could
be retrieved from a user’s posting timeline and likes time-
line through Twitter API is 3,200 tweets for each. However,
there are accounts that have less than 3,200 tweets in their
entire timeline. Hence, we have an average of 2,720 posting
tweets and 2,040 liked tweets per account.
Accounts Shortlisting
To pick the subset of the accounts to use for our study, we
had to find the count of fabricated Hadiths in their recent
timeline as well as the number of fabricated hadith refutes.
In this way we ensure that we filter out any accounts that
have been retrieved due to wrong matching by Twitter API’s
underlying algorithm.
This counting process however is not trivial for hadiths.
As mentioned earlier, it is quite common that Muslims in-
clude a hadith in a tweet along with other text. It is also
common that they only write a part of a hadith and not an
entire hadith. For this stage, we adapted the method used
by Fawzi, Magdy, and Ross (2025) for detecting hadith in
a tweet, but in our case, we included the fabricated hadiths
list. The method can be summarized as follows.
1. Preprocessing: We preprocess the dataset as well as the
timeline as follows:
• Arabic Processing: This includes removing optional
characters in Arabic (Darwish, Magdy, and Mourad
2012) and normalizing some letters that can be typed
in multiple ways (Darwish, Magdy et al. 2014).
• Hadith Processing: A hadith usually starts with a
phrase such as “The messenger of God said”, “I heard
the prophet saying”, and “Muhammad, peace upon
him, said”. These phrases are used interchangeably by
individuals to quote a hadith as they do not alter the
meaning of the hadith so they are removed.
2. Hashing and Pairing: The Minhash of all the tweets in
the timelines as well as reference hadiths is computed.
They are then used to compute the Jaccard similarity
between items from both sets efficiently. We apply the
same filtering criteria defined by Fawzi, Magdy, and Ross
(2025). If the similarity score between the tweet and its
highest matched hadith exceeds 0.35 then it is consid-
ered a match. We validated a sample of 100 matches to
validate that this threshold is precise for our dataset and
all the records were true positives. Reference hadiths in-
cluded fabricated hadiths from MAHADDAT but also
hadiths with other levels of authenticity from LK Cor-
pus (Altammami, Atwell, and Alsalka 2020). This is be-
cause we needed to know the total count of hadiths in
each user’s timeline to calculate the percentage of fabri-
cated hadith in their timelines.
Note: We also count the number of refutes in each time-
line. If a fabricated hadith is matched but the tweet includes
a hadith refuting term then this case is counted as a refute
and not a fabrication.
Although our collection includes more than 30,000 ac-
counts, only 7,382 either have at least one fabricated hadith
or one refute in their recent timeline. This is because Twitter
API fetched some accounts based on a tweet they tweeted
in the past and not in the last 3,200 tweets that are avail-
able for the API. We pick accounts that do the behaviors
of circulation or debunking most frequently. Our collection
includes 559 accounts that spread fabricated hadith two or
more times and represents over 5% of the total hadith they
shared. We included all the accounts that never shared a fab-
ricated hadith and that debunked fabricated hadith at least
three times for the classification experiment, which led to
a set of 343 debunker accounts. To have a balanced dataset
among both groups, we added to them a set of 216 accounts
who debunked only two fabricated hadiths. Thus our final
user dataset contains a set of 559 circulators and 559 de-
bunkers. By definition, none of those accounts can fall in
both categories. The objective of balancing is to allow the
fitting model to equally identify both classes and mitigate
bias towards one of them. Balancing does not make the clas-
sification problem a realistic one. In fact, in reality, there
is a wide spectrum of users who are neither circulators nor
debunkers and there are accounts that are not interested in
Hadith or never heard of it. This artificial setup is just for
the purpose of analysis.
Network Predictors
The network activity of users on social media is proven to
be a good predictor of multiple private and social attributes.
Target attributes could be the expected engagement in some
offline event (Hu, Farnham, and Talamadupula 2015), ge-
olocation (Jurgens et al. 2015), or the stance towards some
social or political cases (Darwish 2022; Magdy et al. 2016).
We are not aware of any work that tried to deploy this strat-
egy on religious data to classify users who interact with it.
We multi-hot encode the interactions of the accounts
which means that the predictors vector has a size equivalent
to the count of all possible predictors appearing in the entire
dataset. The predictors of a given user has the value 1 for any
account that this user interacted with and 0 otherwise. We
aggregate the sets of predictors modeling liking, retweeting,
and following activities of users. Hence, a user can have 1
as a value for their following tie with a page because they
follow it and 0 as a value for their liking tie with the same

--- Page 6 ---

Figure 2: The distribution of user’s locations in our dataset as
stated in their profiles. 70% of the users have blank/invalid
locations.
page because they have never liked any of this page’s tweets.
We use cross-validation with 90-10% train-test split just to
make sure that the model can fit the data with high accuracy.
Then, we retrain the the logistic regression model4 with the
entire dataset to examine their most significant predictors.
Results
In this section, we first report some statistics about the data
then we analyze the significant predictors found within the
fitted logistic regression.
Data Statistics
Table 2 gives context about the nature of the fabricated ha-
diths that are shared by the highest number of circulators
in our final dataset. The original Arabic version of the ha-
diths can be found in table 4 in the appendix. We consult a
professional Sunni Islamic scholar and a professional Shia
Islamic scholar to provide us with more context about these
hadiths. The 1st, 5th, 6th, and 10th hadiths are dedicated to
praising Ali, the cousin of the prophet Muhammad, who is
a central character in the Shia branch of Islam. The 7th ha-
dith is also dedicated to praise Muhammad’s family, which
is a central concept for Shia as it supports the claim that
Muhammad’s family are the only legitimate political succes-
sors to him (Vaezi 2004). The 3rd and 4th hadiths are dedi-
cated to praising Muawiyah, who became a political enemy
of Ali after decades of the death of Muhammad. The 3rd ha-
dith reports that Muhammad once took a pen from Ali and
handed it to Muawiyah. The 4th hadith reports that Muham-
mad once gave Muawiyah a quince. Both hadiths symbolize
the worthiness of political leadership. These hadiths among
others highlight the deployment of fabricated Hadiths in the
Sunni-Shia sectarian conflict (McMahon 2023). The second
common theme that can be detected among these hadiths is
claiming that some religious practices lead to God’s forgive-
ness for one’s previous sins and to other spiritual rewards.
These practices include blessing Muhammad and reading
specific verses of the Quran.
To get more context about the user accounts in our dataset,
we inspected the geographical distribution of users manu-
ally for accurate reporting of their locations. Figure 2 shows
4We also tested SVM and ridge regression with the same setup and
got almost the same results.
Figure 3: The average number of overall interactions found
for each class.
that the users are distributed over a diverse set of Arab and
non-Arab countries. Saudi Arabia has the largest portion of
both circulators and debunkers. Most countries where circu-
lators outnumber debunkers have a considerable population
of Shia Muslims like Iraq, Kuwait, Lebanon, and Bahrain.
There is still a considerable number of circulators in coun-
tries where Sunni Muslims are a majority and Shia Muslims
are a small minority like Egypt, UAE, and Saudi Arabia. In
all western communities debunkers outnumber circulators.
We also checked the distributions of different types of in-
teractions and connections of each group, see Figure 3. In
general, circulators tend to have a significantly5 higher num-
ber of interactions than debunkers. It is also worth noting
that the percentage of retweets in the timelines of circulators
is much higher (75.8%) than debunkers (27.9%). This means
that they have higher tendency to share content authored by
others compared to debunkers.
Analysis
Logistic regression is able to distinguish fabricated Hadith
circulators from debunkers with an accuracy of 87.7% as
shown in Table 3. The high accuracy obtained by the fitted
model qualify its most significant predictors to be identifiers
for both classes. The top 100 predictors with highest positive
and negative coefficients assigned by the logistic regression
are inspected further where positive ones identify the circu-
lators class and negative ones identify debunkers.
We classify the predictors into five categories: Sunni
Pages, Sunni Scholars, Shia Pages/Scholars, Non-religious
Accounts, and Personal accounts as shown in Figure 4. We
notice that a big portion of the most significant features con-
sists of accounts related to religion. There are significant dif-
ferences between circulators and debunkers in terms of the
portion of each category in their top 100 predictors and the
nature of the accounts in each portion. Below, we go through
each category in detail:
5according to Welch’s significance t-test with p-value of 0.0001
for distributions of retweets, follows, and likes.

--- Page 7 ---

Count
Users
Top Fabricated Hadith (translated)
233
142
The Messenger of Allah ordered us to present our children to the love of Ali ibn Abi Talib.
247
89
Whoever recites Surah Ad-Dukhan during the night, his previous sins will be forgiven.
120
89
He, may God’s prayers and peace be upon him and his family, took the pen from Ali’s hand and handed it to Muawiyah.
141
88
He, may God’s prayers and peace be upon him and his family, gave Muawiyah a quince.
69
65
Whoever wants to look at Adam in his knowledge, Noah in his understanding, Abraham in his wisdom, Yahya in his
asceticism, and Moses in his strength, let him look at Ali.
77
62
Loving Ali eats away bad deeds as fire eats away wood.
65
51
When asked who are the most ascetic person in the world? The prophet referred to the people of his house.
371
47
God said to Moses, whoever recites Ayat Al-Kursi after every prayer will be given the reward of the prophets.
342
43
Increase your sending of blessings upon me, indeed, Allah appointed an angel to me next to my grave so whenever
an individual from my ummah blessings salam upon me the angel says to me: O Muhammad! Verily, so-and-so sends
blessings upon you.
51
41
I am the city of knowledge and Ali is its gate, so whoever wants knowledge, let him come to the gate.
Table 2: The English translation of the most shared fabricated hadiths in the timelines of the users in our dataset along with the
number of unique users sharing them and their total number of occurrences.
Accuracy
Precision
Recall
F1-Score
Circulators
-
92.2%
82.3%
87%
Debunkers
-
84.1%
93.0%
88.3%
Macro
87.7%
88.2%
87.7%
87.6%
Table 3: Precision, recall, and F1-score of the logistic regres-
sion model whose predictors get analyzed further. Accuracy
and macro values are reported.
Sunni Pages: This category represents religious accounts
following the Sunni branch of Islam sharing Islamic con-
tent. There are more accounts from this category identifying
circulators compared to debunkers. By inspecting these ac-
counts further, we find that the ones on the circulators side
are usually not related to a professional website or institu-
tion. Some of them just identify themselves as a group of
social media influencers posting religious content. In case
of debunkers, those accounts usually represent professional
websites that are moderated by professional Islamic schol-
ars (e.g saaidnet1saaid.org) and professional Islamic in-
stitutions (e.g. TPCV SSA and olamayemen).
Sunni Scholars: For circulators, all of the accounts un-
der this category belong to gulf countries. On the other
hand, for debunkers, there are scholars from other areas
like Ali al-Qaradaghi (Ali AlQaradaghi) from Turkey
and Muhammad al-Dido (ShaikhDadow) from Maurita-
nia. Additionally, we spotted ashrafgharib11 who de-
fines himself as an anti-shia researcher in the Shia religion
and AntiShubohat who defines himself as a Muslim re-
searcher against heresies related to Islam.
Shia Pages/Scholars: This category only exists for circu-
lators, but not for debunkers, as shown in Figure 4 and its
accounts have the highest coefficients among all the most
significant features. However, being associated with circula-
tors does not necessarily imply that they circulate fabricated
hadith themselves. It just means that they are distinctive pre-
dictors in the network of the circulators. Nevertheless, it is
important to note in this context that Sunni pages/scholars
associated with circulators as features are more than twice
the Shia features. The presence of many religious features
from both Sunni and Shia branches of Islam confirms that
the behavior of Hadith fabrication is not solely linked to one
of them but appears within both of them.
Non-religious Accounts: Features from this category on
the debunkers side are twice more than the circulators side.
This shows that debunkers are more identifiable through
their non-religious interactions. Interestingly, for circula-
tors, accounts from this category include accounts that post
pornographic content, and others that are anti-Islam and
pro-Israel (e.g. BellaZamoria). Additionally, we also
found many accounts related to movies or shows (e.g.
NetflixMENA and AflamWorld). We noticed particu-
lar interest in Korean shows through accounts (e.g. jjklve
and bts nanak). Finally, we found that ties with NASA,
Google, SpaceX, Tesla, and BillGates identify cir-
culators. These shows that circulators a have wide range of
interests reflecting that they do not necessarily have to be re-
ligious, which might explain being less careful when sharing
Islamic content that happens to be fabricated sometimes.
For debunkers, accounts include news sources such
as cnnarabic and SaudiNews50, journalists (e.g.
Omar Madaniah), and the account of elonmusk. Fur-
thermore, we recognize charities (e.g insan kwt and
Tarahumkw) in addition to accounts promoting activism
such as turkistantuzbah which is dedicated for
the causes of Islamic minorities worldwide, hureyaksa
which is against authoritarian regimes in the Middle East,
and Ali Albukhaiti, an activist against the Houthi
movement in Yemen, Hezbollah, and Iran which are entities
that constitute a political Shia axis in the Middle East.
Personal Accounts: There are two clusters of personal
accounts that identify circulators. The first includes eight
accounts that identify themselves as followers of the Shia
branch of Islam and the second one includes five accounts
that come from Indonesia. Indonesia’s first language is not
Arabic which makes checking the authenticity of Hadith
for Indonesian Muslims a harder task than Arabs. For de-
bunkers, we found two accounts from this category identify-
ing themselves as heresy fighters.
Out of the 100 most predictors for circulators, there
are two accounts from our seed list of circulators, namely

--- Page 8 ---

Figure 4: The distribution of the top 100 significant predic-
tors identifying Circulators and Debunkers in the logistic re-
gression.
alsalaf 1, a Sunni page and AhlulbaytSays a Shia
page. This might indicate that these pages have some
influence in spreading fabricated hadiths. On the other
hand, five accounts belong to our debunkers seed list are
in the top 100 significant predictors of debunkers. Those
include one personal account, two professional Islamic
pages (ConsHadith and alsunna way), and two Is-
lamic scholars (almonajjid and hadeeth tarifi),
which shows their influence in debunking fabricated hadith
online.
Discussion
To the best of our knowledge, this is the first study to address
the topic of religious misinformation by trying to understand
the characteristics and the interests of the users involved in
it. Our study highlights and quantitatively frames a form
of the understudied topic of religious misinformation. Ear-
lier research only addressed religious misinformation by ei-
ther qualitatively examining and linking some incidents then
drawing conclusions based on them (Alimardani and Elswah
2020) or measuring quantitatively the reactions of religious
communities towards a specific topic (Lee Rogers and Powe
2022). However, no research is attempting to dig deeper into
the nature of fabricated religious texts that circulate and po-
tentially cause these incidents or reactions. In addition, no
research attempts to understand the characteristics of users
who interact with such type of misinformation. We ques-
tioned in RQ1 the possibility of classifying fabricated Ha-
dith circulators against debunkers using the network ties of
these users. The results we obtained showed that both classes
are highly separable through their network ties by a simple
logistic regression model.
This easy distinction between both classes motivated our
RQ2 where we examine the key features in the networks
of each group of users that identify them. We found that
both classes are generally identified by their interactions
with a lot of religious accounts where the nature of these
accounts differ for each group. Religious accounts that iden-
tify circulators include Shia pages and scholars, Sunni non-
professional pages sharing religious content, and Sunni pro-
fessional Islamic scholars from gulf countries. Religious ac-
counts identifying debunkers include pages that are linked
with professional websites in addition to Islamic scholars
who are from a diverse set of countries.
Debunkers are more identifiable through their non-
religious interactions that include ties with news sources,
journalists, charities, and activists. This finding can poten-
tially contribute to the ongoing research debate about the
relationship between misinformation and activism . While
some research works claim that online activism is associ-
ated with misinformation (Sinpeng, Tapsell et al. 2021), a re-
cent study claims finding little evidence to support that (Jalli
2025). Our study detects activism within the networks of de-
bunkers which motivates doing further research on Arabic
speakers to validate this effect. The non-religious interac-
tions identifying circulators included pornographic and athe-
istic accounts which indicates that posting religious content
does not necessarily indicate religiosity.
The limited number of personal accounts among the fea-
tures compared to public and famous ones suggests that the
propagation of fabricated Hadiths takes the form of elite
misinformation described by Mosleh and Rand (2022) more
than the form of horizontal misinformation described by
Vl˘adut¸escu (2014). In elite vertical misinformation, public
figures act by influence on a passive crowd who are in an in-
ferior position. While doing this, these influential accounts
sometimes take precautions to distance themselves from be-
ing held accountable for disinformation (Prochaska et al.
2023). In horizontal misinformation, crowds are more ac-
tive where an individual is usually a source and a target for
misinformation simultaneously.
Implications
Our findings raise questions about the ethical privacy con-
cerns on social media especially those related to religious
beliefs. We showed that the social interactions of users can
easily be used to reveal their religious awareness and their
ability to distinguish authentic religious texts from fabri-
cated ones, a property that many individuals would not be
comfortable to share. While there are many incidents where
religion is used to intensify conflicts, our findings reveal
another threat that arises from the possibility of doing re-
ligious provocation on a targeted individual basis. Social
media platforms are encouraged to develop techniques that
measure the possibility that users get manipulated using reli-
gion and warn users who are found to be in this position. The
platforms should also raise awareness about the presence of
this type of misinformation by reporting analytics about the
topic in a similar way to the project of Twitter Transparency
Report (Twitter 2012). It would also be helpful to add re-
ligious misinformation as a possible explicit reason for re-
porting social media threads as spam/harmful.
A lot of social studies highlight the negative impact of
religion on people’s cognitive abilities and claim that athe-
ists and agnostics are more reflective than religious believers
(Pennycook et al. 2016). They also link being more religious
to being more prone to believe fake news (Bronstein et al.
2019). While this can be true in some communities, it does
not necessarily have to be generally true especially within

--- Page 9 ---

communities where the majority of people are religious. Our
study reveals a new dimension of studying religious people
where they can be classified into multiple groups that have
totally different behaviors towards misinformation. This mo-
tivates inspecting the effects of religion that are studied be-
fore while considering that religious people can be classified
into multiple groups.
Although our study addresses the topic of Hadith fabri-
cation in a neutral way towards Sunni and Shia schools of
Hadith evaluation, it highlights that the available resources
to study Hadith from the Sunni perspective are much more
than those available for Shia. Studying Hadith from Shia’s
point of view requires consulting professional Islamic Shia
scholars who are not accessible to everyone in the research
community. We believe that there is a need for datasets that
evaluate Hadith from the Shia perspective. This will help
researchers to study the religious beliefs of Shia communi-
ties more smoothly. The research community already reports
many difficulties Shia Muslims are experiencing with their
religious expression (Alshehri and Su 2023)
Finally, our study sheds light on Hadith as a text in gen-
eral and the topic of the spread of fabricated Hadith in par-
ticular. This interesting complex phenomenon manifests a
lot of observations about the different cultural backgrounds
of social media users in the Middle East and the disputes
they have in a religious flavor. There are a lot of quantita-
tive works that addressed social discourse in areas of conflict
like Ukraine (Alieva and Carley 2024) and they did not find
a significant role for religion in such conflicts. However, in
understudied parts of the world like the Middle East as well
as India and Sri Lanka, religion has a significant role in con-
flicts (Koch 2019). Our study motivates exploring this effect
further through quantitative methods rather than the limited
existing qualitative ones.
Limitations & Future Work
Our analysis to Islamic religious misinformation is limited
to Hadith as the religious text. However, other religious texts
are also often used for misinformation as we showed in Fig-
ure 1. This includes users sharing quotes by scholars or
historic figures that are not true. However, the main chal-
lenge studying such type of misinformation is the absence
of datasets or algorithms to spot them. It can be an interest-
ing direction to create such resources. This analysis can be
applied to similar texts in different religions.
Secondly, our study only considers the Hadith in Ara-
bic text. However, there are hundreds of millions of Mus-
lims who report Hadith in other languages such as Turk-
ish, Farsi, Urdu, and Malay (Sulistio et al. 2023). Explor-
ing how fabricated Hadith spread among these non-Arabic
communities would be an interesting future direction, espe-
cially when compared to the findings of this study on the
Arab world. Additionally, while our study only investigates
disputes about fabricated hadith, it is interesting to charac-
terize users who attempt to debunk Hadith that is actually
authentic and whether this should be classified as a form of
misinformation or intended disinformation.
We acknowledge that our strict data collection methodol-
ogy can potentially result in missing many circulators and
debunkers. Overlooked circulators include the users who
circulated fabricated hadiths that are not included in the
datasets used as a reference as well as the users who made up
hadiths themselves or by prompting LLMs. Overlooked de-
bunkers include the users who argue against the authenticity
of a hadith in a conversational or indirect way. Nevertheless,
our data collection method still retrieves an unbiased rep-
resentative sample of both behaviors with a high precision
which is more necessary for characterizing such behaviors
than recall to avoid potential noise in the data.
Another important limitation is that our study only inves-
tigates Hadith on Twitter (currently X). Hadith exchanges
is also very popular on other platforms such as Telegram
and Whatsapp (Sauda 2020). Finally, we believe that setting
up surveys and interviews with Muslim users can provide
good qualitative insights about the awareness and motives
behind circulating or debunking fabricated Hadith. They can
also provide more context about the possible consequences
of this type of misinformation.
Conclusion
In this work, we introduced the topic of Hadith fabrication
as a form of religious misinformation. We identified tens
of thousands of threads on social media that include fabri-
cated Hadith and we collected multiple sets of users who
interact with it. We attempted to gain more insights about
the differences between users who circulate fabricated Ha-
dith and those who debunk it. Both classes were found to be
tied with a lot of religious accounts but the accounts tied
to each class have a different nature. Circulators are tied
with Shia accounts, non-professional Sunni pages, and pro-
fessional Sunni Islamic scholars from gulf countries while
debunkers are tied with more professional pages and profes-
sional Islamic scholars from a diverse set of countries. The
non-religious interests that identify circulators are limited to
entertainment while debunkers are identified by interests re-
lated to charity, politics, and activism.
References
Abdelaal,
H.
M.;
Ahmed,
A.
M.;
Ghribi,
W.;
and
Youness Alansary, H. A. 2019. Knowledge Discovery in the
Hadith According to the Reliability and Memory of the Re-
porters Using Machine Learning Techniques. IEEE Access,
7: 157741–157755.
Abokhodair, N.; Elmadany, A.; and Magdy, W. 2020. Holy
tweets: Exploring the sharing of the Quran on Twitter.
Proceedings of the ACM on Human-Computer Interaction,
4(CSCW2): 1–32.
Al-Zaman, M. S. 2024.
Social Media Users’ Engage-
ment with Religious Misinformation: An Exploratory Se-
quential Mixed-Methods Analysis.
Emerging Media,
27523543241257715.
Albadi, N.; Kurdi, M.; and Mishra, S. 2022. Deradicalizing
youtube: Characterization, detection, and personalization of
religiously intolerant arabic videos. Proceedings of the ACM
on Human-Computer Interaction, 6(CSCW2): 1–25.
Alieva, I.; and Carley, K. 2024. Exploring Russian Anti-War
Discourse on Twitter during Russia’s full-scale invasion of

--- Page 10 ---

Ukraine: Dynamics, Influence, and Narratives. Proceedings
of the International AAAI Conference on Web and Social
Media.
Alimardani, M.; and Elswah, M. 2020. Online Temptations:
COVID-19 and Religious Misinformation in the MENA Re-
gion. Social Media+ Society, 6(3): 2056305120948251.
Alshehri, M.; and Su, N. M. 2023. Comfort Activism: On-
line Photography for Social Change in a Minority Group.
Proceedings of the ACM on Human-Computer Interaction,
7(CSCW1): 1–33.
Altammami, S.; Atwell, E.; and Alsalka, A. 2020.
The
Arabic-English parallel corpus of authentic hadith. Interna-
tional Journal on Islamic Applications in Computer Science
And Technology, 8(2).
Ashkinaze, J.; Gilbert, E.; and Budak, C. 2024. The Dy-
namics of (Not) Unfollowing Misinformation Spreaders. In
Proceedings of the ACM on Web Conference 2024, 1115–
1125.
Azami, M. M. 2002. Studies in Hadith methodology and
literature. The Other Press.
Azmi, A. M.; Al-Qabbany, A. O.; and Hussain, A. 2019.
Computational and natural language processing based stud-
ies of hadith literature: a survey. Artificial Intelligence Re-
view, 52: 1369–1414.
Benkler, Y.; Tilton, C.; Etling, B.; Roberts, H.; Clark, J.;
Faris, R.; Kaiser, J.; and Schmitt, C. 2020. Mail-In Voter
Fraud: Anatomy of a Disinformation Campaign. SSRN Elec-
tronic Journal.
Bennett, C. 2015. The Bloomsbury companion to Islamic
studies. Bloomsbury Publishing.
Bhimdiwala, A.; Adavi, K. A. K.; and Arif, A. 2024. Fight-
ing for Their Voice: Understanding Indian Muslim Women’s
Responses to Networked Harassment. Proceedings of the
ACM on Human-Computer Interaction, 8(CSCW1): 1–24.
Binbeshr, F.; Kamsin, A.; and Mohammed, M. 2021. A sys-
tematic review on hadith authentication and classification
methods.
Transactions on Asian and Low-Resource Lan-
guage Information Processing, 20(2): 1–17.
Boutz, J.; Benninger, H.; and Lancaster, A. 2019. Exploiting
the prophet’s authority: How Islamic State propaganda uses
hadith quotation to assert legitimacy. Studies in Conflict &
Terrorism, 42(11): 972–996.
Boutz, J.; Brugman, C.; and Lancaster, A. 2017. Quoting
the Prophet online: Communicative functions of hadith quo-
tations in webbased Arabic discourse. Journal of Arab &
Muslim Media Research, 10(1): 3–23.
Bronstein, M. V.; Pennycook, G.; Bear, A.; Rand, D. G.; and
Cannon, T. D. 2019. Belief in fake news is associated with
delusionality, dogmatism, religious fundamentalism, and re-
duced analytic thinking.
Journal of applied research in
memory and cognition, 8(1): 108–117.
Buie, E.; and Blythe, M. 2013. Spirituality: there’s an app
for that!(but not a lot of research). In CHI’13 extended ab-
stracts on human factors in computing systems, 2315–2324.
Caldarelli, G.; De Nicola, R.; Petrocchi, M.; Pratelli, M.; and
Saracco, F. 2021. Flow of online misinformation during the
peak of the COVID-19 pandemic in Italy. EPJ Data Science,
10: 34.
Chandra, M.; Reddy, M.; Sehgal, S.; Gupta, S.; Buduru,
A. B.; and Kumaraguru, P. 2021.
” A Virus Has No
Religion”: Analyzing Islamophobia on Twitter During the
COVID-19 Outbreak. In Proceedings of the 32nd ACM con-
ference on hypertext and social media, 67–77.
Claisse, C.; and Durrant, A. C. 2023. ‘Keeping our Faith
Alive’: Investigating Buddhism Practice during COVID-19
to Inform Design for the Online Community Practice of
Faith. In Proceedings of the 2023 CHI Conference on Hu-
man Factors in Computing Systems, 1–19.
Darwish, K. 2022. News consumption in time of conflict:
2021 Palestinian-Israel War as an example. In Proceedings
of the 14th ACM Web Science Conference 2022, 260–268.
Darwish, K.; Magdy, W.; and Mourad, A. 2012. Language
processing for arabic microblog retrieval. In Proceedings of
the 21st ACM international conference on Information and
knowledge management, 2427–2430.
Darwish, K.; Magdy, W.; et al. 2014. Arabic information re-
trieval. Foundations and Trends® in Information Retrieval,
7(4): 239–342.
Fakhruroji, M. 2021. Muslims Learning Islam on the Inter-
net 41. Handbook of contemporary Islam and Muslim lives,
845.
Fawzi, M.; and Magdy, W. 2024.
” Pinocchio had a
Nose, You have a Network!”: On Characterizing Fake News
Spreaders on Arabic Social Media. Proceedings of the ACM
on Human-Computer Interaction, 8(CSCW1): 1–20.
Fawzi, M.; Magdy, W.; and Ross, B. 2025. ’The Prophet said
so!’: On Exploring Hadith Presence on Arabic Social Media.
Proceedings of the ACM on Human-Computer Interaction,
9(CSCW2): 1–23.
FORCE11. 2020. The FAIR Data principles. https://force11.
org/info/the-fair-data-principles/.
Gaanoun, K.; and Alsuhaibani, M. 2022.
Fabricated Ha-
dith Detection: A Novel Matn-Based Approach With Trans-
former Language Models.
IEEE Access, 10: 113330–
113342.
Gebru, T.; Morgenstern, J.; Vecchione, B.; Vaughan, J. W.;
Wallach, H.; Iii, H. D.; and Crawford, K. 2021. Datasheets
for datasets. Communications of the ACM, 64(12): 86–92.
Ghazizadeh, M.; Zahedi, M. H.; Kahani, M.; and Bidgoli,
B. M. 2008. Fuzzy expert system in determining hadith1
validity. In advances in computer and information sciences
and engineering, 354–359. Springer.
Hakak, S.; Kamsin, A.; Zada Khan, W.; Zakari, A.; Imran,
M.; bin Ahmad, K.; and Amin Gilkar, G. 2022. Digital Ha-
dith authentication: Recent advances, open challenges, and
future directions. Transactions on Emerging Telecommuni-
cations Technologies, 33(6): e3977.
Hassaine, A.; Safi, Z.; and Jaoua, A. 2016.
Authenticity
detection as a binary text categorization problem: Applica-
tion to Hadith authentication. In 2016 IEEE/ACS 13th Inter-
national Conference of Computer Systems and Applications
(AICCSA), 1–7. IEEE.

--- Page 11 ---

Hu, Y.; Farnham, S.; and Talamadupula, K. 2015. Predicting
user engagement on twitter with real-world events. In Pro-
ceedings of the International AAAI Conference on Web and
Social Media, volume 9, 168–177.
Hutchings, T. 2017a. Creating church online: Ritual, com-
munity and new media. Taylor & Francis.
Hutchings, T. 2017b. Design and the digital Bible: Persua-
sive technology and religious reading. Journal of Contem-
porary Religion, 32(2): 205–219.
Ibrahim, N. K.; Samsuri, S.; Seman, M. S. A.; Ali, A. E. B.;
and Kartiwi, M. 2016. Frameworks for a computational is-
nad authentication and mechanism development. In 2016
6th International Conference on Information and Commu-
nication Technology for The Muslim World (ICT4M), 154–
159. IEEE.
Ibrahim, Z.; Nurain, N.; and Clawson, J. 2024. Tracking
During Ramadan: Examining the Intersection of Menstrual
and Religious Tracking Practices Among Muslim Women in
the United States. In Proceedings of the CHI Conference on
Human Factors in Computing Systems, 1–19.
Ibtasam, S.; Razaq, L.; Ayub, M.; Webster, J. R.; Ahmed,
S. I.; and Anderson, R. 2019.
” My cousin bought the
phone for me. I never go to mobile shops.” The Role of Fam-
ily in Women’s Technological Inclusion in Islamic Culture.
Proceedings of the ACM on Human-Computer Interaction,
3(CSCW): 1–33.
Introne, J.; Yildirim, I.; Iandoli, L.; DeCook, J.; and
Elzeini, S. 2018.
How People Weave Online Informa-
tion Into Pseudoknowledge.
Social Media + Society, 4:
205630511878563.
Jalli, N. 2025.
Viral Justice: TikTok Activism, Misinfor-
mation, and the Fight for Social Change in Southeast Asia.
Social Media+ Society, 11(1): 20563051251318122.
Jurgens, D.; Finethy, T.; McCorriston, J.; Xu, Y.; and Ruths,
D. 2015. Geolocation prediction in twitter using social net-
works: A critical analysis and review of current practice. In
Proceedings of the international AAAI conference on web
and social media, volume 9, 188–197.
Kabir, M. N.; Hasan, M. M.; Rahman, M. A.; and Tao, H.
2018. Development of a web-extension for authentication
of online Hadith texts. International Journal of Engineering
& Technology, 7(2.5): 19–22.
Kabir, M. N.; Tayan, O.; Alginahi, Y.; Hasan, M. M.; and
Rahman, M. A. 2019. On the development of a web ex-
tension for text authentication on Google Chrome. In 2019
International Conference on Electrical, Computer and Com-
munication Engineering (ECCE), 1–5. IEEE.
Kapantai, E.; Christopoulou, A.; Berberidis, C.; and Peris-
teras, V. 2021. A systematic literature review on disinforma-
tion: Toward a unified taxonomical framework. New media
& society, 23(5): 1301–1326.
Khan, M. M.; et al. 1983. The translation of the meanings
of Sahih AL-Bukhari: Arabic-English, volume 5. Kazi Pub-
lications.
Kim, I.; Ko, M.; Park, J.; Moon, S. W.; Jung, G.; Lim, Y.-k.;
and Lee, U. 2022. Social-Spiritual Face: Designing Social
Reading Support for Spiritual Well-being. Proceedings of
the ACM on Human-Computer Interaction, 6(CSCW2): 1–
22.
Koch, B. 2019. Unmasking ‘religious’ conflicts and reli-
gious radicalisation in the Middle East.
Kursuncu,
U.;
Gaur,
M.;
Castillo,
C.;
Alambo,
A.;
Thirunarayan, K.; Shalin, V.; Achilov, D.; Arpinar, I. B.; and
Sheth, A. 2019. Modeling islamist extremist communica-
tions on social media using contextual dimensions: religion,
ideology, and hate.
Proceedings of the ACM on Human-
Computer Interaction, 3(CSCW): 1–22.
Lee Rogers, R.; and Powe, N. 2022. COVID-19 information
sources and misinformation by faith community. INQUIRY:
The Journal of Health Care Organization, Provision, and
Financing, 59: 00469580221081388.
Leonardi, S.; and Rizzo, G. 2021. Automated Classification
of Fake News Spreaders to Break the Misinformation Chain.
Information, 12: 248.
Magdy, W.; Darwish, K.; Abokhodair, N.; Rahimi, A.; and
Baldwin, T. 2016. # isisisnotislam or# deportallmuslims?
Predicting unspoken views. In Proceedings of the 8th ACM
Conference on Web Science, 95–106.
Markum, R. B.; Wolf, S.; Hoefer, M.; and Maas, F. 2023.
Designing Tangible Interactive Artifacts for Religious and
Spiritual Purposes. In Companion Publication of the 2023
ACM Designing Interactive Systems Conference, 117–120.
McMahon, R. 2023. The Sunni-Shia Divide. Council on
Foreign Relations.
Miyazaki, K.; Uchiba, T.; Tanaka, K.; An, J.; Kwak, H.; and
Sasahara, K. 2023. ” This is Fake News”: Characterizing the
Spontaneous Debunking from Twitter Users to COVID-19
False Information. In Proceedings of the International AAAI
Conference on Web and Social Media, volume 17, 650–661.
Molina, M. D.; Sundar, S. S.; Le, T.; and Lee, D. 2021. “Fake
news” is not simply false information: A concept explication
and taxonomy of online content. American behavioral sci-
entist, 65(2): 180–212.
Morales, P. R.; Berriche, M.; and Cointet, J.-P. 2023. The
geometry of misinformation: embedding twitter networks of
users who spread fake news in geometrical opinion spaces.
In Proceedings of the International AAAI Conference on
Web and Social Media, volume 17, 730–741.
Mosleh, M.; and Rand, D. G. 2022. Measuring exposure
to misinformation from political elites on Twitter. Nature
Communications, 13(1): 7144.
Mu, Y.; Niu, P.; and Aletras, N. 2022. Identifying and char-
acterizing active citizens who refute misinformation in so-
cial media. Proceedings of the 14th ACM Web Science Con-
ference 2022, 401–410.
Najiyah, I.; Susanti, S.; Riana, D.; and Wahyudi, M. 2017.
Hadith degree classification for Shahih Hadith identification
web based. In 2017 5th International Conference on Cyber
and IT Service Management (CITSM), 1–6. IEEE.
Pennycook, G.; Ross, R. M.; Koehler, D. J.; and Fugel-
sang, J. A. 2016. Atheists and agnostics are more reflective
than religious believers: Four empirical studies and a meta-
analysis. PloS one, 11(4): e0153039.

--- Page 12 ---

Prochaska, S.; Duskin, K.; Kharazian, Z.; Minow, C.;
Blucker, S.; Venuto, S.; West, J.; and Starbird, K. 2023. Mo-
bilizing Manufactured Reality: How Participatory Disinfor-
mation Shaped Deep Stories to Catalyze Action during the
2020 U.S. Presidential Election. Proceedings of the ACM on
Human-Computer Interaction, 7: 1–39.
Rath, B.; Salecha, A.; and Srivastava, J. 2020. Detecting
Fake News Spreaders in Social Networks Using Inductive
Representation Learning, 182–189.
IEEE Press.
ISBN
9781728110561.
Rifat, M. R.; Toriq, T.; and Ahmed, S. I. 2020. Religion
and sustainability: Lessons of sustainable computing from
Islamic religious communities. Proceedings of the ACM on
Human-Computer Interaction, 4(CSCW2): 1–32.
Saloot, M. A.; Idris, N.; Mahmud, R.; Ja’afar, S.; Thor-
leuchter, D.; and Gani, A. 2016. Hadith data mining and
classification: a comparative analysis. Artificial Intelligence
Review, 46: 113–128.
Sauda, L. 2020. One Day One Hadith with Online Media:
Challenges and Opportunities. In Proceedings of the 2nd
International Conference on Quran and Hadith Studies In-
formation Technology and Media in Conjunction with the
1st International Conference on Islam, Science and Tech-
nology, ICONQUHAS & ICONIST, Bandung, October 2-4,
2018, Indonesia.
Sinpeng, A.; Tapsell, R.; et al. 2021. From grassroots ac-
tivism to disinformation: Social media trends in Southeast
Asia. From grassroots activism to disinformation, 1–18.
Southwell, B. G.; Brennen, J. S. B.; Paquin, R.; Boudewyns,
V.; and Zeng, J. 2022. Defining and measuring scientific
misinformation. The ANNALS of the American Academy of
Political and Social Science, 700(1): 98–111.
Sulistio, B.; Ramadhan, A.; Abdurachman, E.; Zarlis, M.;
and Trisetyarso, A. 2023. The utilization of machine learn-
ing on studying Hadith in Islam: A systematic literature re-
view. Education and Information Technologies, 1–39.
Teplinsky, E.; Ponce, S. B.; Drake, E. K.; Garcia, A. M.;
Loeb, S.; Van Londen, G.; Teoh, D.; Thompson, M.;
Schapira, L.; and for Outcomes using Social Media in On-
cology (COSMO), C. 2022. Online medical misinformation
in cancer: distinguishing fact from fiction. JCO oncology
practice, 18(8): 584–589.
Tsuria, R. 2020.
Discourse of Practice: The Negotiation
of Sexual Norms Via Online Religious Discourse. Interna-
tional Journal of Communication, 14: 19.
Twitter. 2012. Twitter Transparency Center.
Usman, A. H.; and Wazir, R. 2018. The fabricated hadith:
Islamic ethics and guidelines of hadith dispersion in social
media. Turkish Online Journal Of Design Art And Commu-
nication, 8: 804–808.
Vaezi, A. 2004. Shia political thought. Islamic Centre of
England London.
Vl˘adut¸escu, S. 2014.
Communicational Types of Propa-
ganda. International Letters of Social and Humanistic Sci-
ences, 33: 41–49.
Vogel, I.; and Meghana, M. 2020.
Detecting Fake News
Spreaders on Twitter from a Multilingual Perspective. 599–
606.
Weinzierl, M.; Hopfer, S.; and Harabagiu, S. M. 2021. Mis-
information adoption or rejection in the era of covid-19. Pro-
ceedings of the International AAAI Conference on Web and
Social Media, 15: 787–795.
Wolf, S.; Friedrich, P.; and Hurtienne, J. 2024. Still Not a Lot
of Research? Re-Examining HCI Research on Religion and
Spirituality. In Extended Abstracts of the CHI Conference
on Human Factors in Computing Systems, 1–15.
Wolf, S.; Moerike, F.; Luthe, S.; Nord, I.; and Hurtienne,
J. 2022. Spirituality at the breakfast table: Experiences of
Christian online worship services. In CHI Conference on
Human Factors in Computing Systems Extended Abstracts,
1–7.
Zannettou, S.; Sirivianos, M.; Blackburn, J.; and Kourtellis,
N. 2019. The web of false information: Rumors, fake news,
hoaxes, clickbait, and various other shenanigans. Journal of
Data and Information Quality (JDIQ), 11(3): 1–37.
Zhou, K.; ˇS´cepanovi´c, S.; and Quercia, D. 2024. Character-
izing Fake News Targeting Corporations. In Proceedings of
the International AAAI Conference on Web and Social Me-
dia, volume 18, 1818–1832.

--- Page 13 ---

A Ethics Checklist
1. For most authors...
(a) Would answering this research question advance sci-
ence without violating social contracts, such as violat-
ing privacy norms, perpetuating unfair profiling, exac-
erbating the socio-economic divide, or implying dis-
respect to societies or cultures? Yes, In our study, we
ensure using the term misinformation and not disin-
formation as we don’t claim any assumptions about
the intentions of users sharing fabricated Hadith or
their prior knowledge about it. This means that our
labels for accounts are just meant to frame the ob-
served social behaviors to enable further analysis for
their causes. The strict classification of users accounts
is not among the objectives of our study. We also re-
frain from exposing any details that can help reveal the
identity of the users whose accounts are being studied.
Finally, we obtained an ethical approval from our host
institution to conduct this study.
(b) Do your main claims in the abstract and introduction
accurately reflect the paper’s contributions and scope?
Yes
(c) Do you clarify how the proposed methodological ap-
proach is appropriate for the claims made? Yes
(d) Do you clarify what are possible artifacts in the data
used, given population-specific distributions? Yes, in
section 3 entitled Data & Methods
(e) Did you describe the limitations of your work? Yes
(f) Did you discuss any potential negative societal im-
pacts of your work? NA, the study describes character-
izes two social behaviors without claiming that misin-
formation is intentional.
(g) Did you discuss any potential misuse of your work?
Yes, we highlight that the easy identification of the re-
ligious preferences of users can be misused.
(h) Did you describe steps taken to prevent or mitigate po-
tential negative outcomes of the research, such as data
and model documentation, data anonymization, re-
sponsible release, access control, and the reproducibil-
ity of findings? Yes, and we obtained an ethical ap-
proval from our host institution to conduct the study.
(i) Have you read the ethics review guidelines and en-
sured that your paper conforms to them? Yes
2. Additionally, if your study involves hypotheses testing...
(a) Did you clearly state the assumptions underlying all
theoretical results? NA
(b) Have you provided justifications for all theoretical re-
sults? NA
(c) Did you discuss competing hypotheses or theories that
might challenge or complement your theoretical re-
sults? NA
(d) Have you considered alternative mechanisms or expla-
nations that might account for the same outcomes ob-
served in your study? NA
(e) Did you address potential biases or limitations in your
theoretical framework? NA
(f) Have you related your theoretical results to the existing
literature in social science? NA
(g) Did you discuss the implications of your theoretical
results for policy, practice, or further research in the
social science domain? NA
3. Additionally, if you are including theoretical proofs...
(a) Did you state the full set of assumptions of all theoret-
ical results? NA
(b) Did you include complete proofs of all theoretical re-
sults? NA
4. Additionally, if you ran machine learning experiments...
(a) Did you include the code, data, and instructions
needed to reproduce the main experimental results (ei-
ther in the supplemental material or as a URL)? NA,
Only simple statistical models are used
(b) Did you specify all the training details (e.g., data splits,
hyperparameters, how they were chosen)? NA, Only
simple statistical models are used
(c) Did you report error bars (e.g., with respect to the ran-
dom seed after running experiments multiple times)?
NA, Only simple statistical models are used
(d) Did you include the total amount of compute and the
type of resources used (e.g., type of GPUs, internal
cluster, or cloud provider)? NA, Only simple statistical
models are used
(e) Do you justify how the proposed evaluation is suffi-
cient and appropriate to the claims made? NA, Only
simple statistical models are used
(f) Do you discuss what is “the cost“ of misclassifica-
tion and fault (in)tolerance? NA, Only simple statis-
tical models are used
5. Additionally, if you are using existing assets (e.g., code,
data, models) or curating/releasing new assets...
(a) If your work uses existing assets, did you cite the cre-
ators? Yes, we cite the datasets and adopted mecha-
nisms
(b) Did you mention the license of the assets? NA
(c) Did you include any new assets in the supplemental
material or as a URL? NA
(d) Did you discuss whether and how consent was ob-
tained from people whose data you’re using/curating?
NA
(e) Did you discuss whether the data you are using/cu-
rating contains personally identifiable information or
offensive content? NA
(f) If you are curating or releasing new datasets, did you
discuss how you intend to make your datasets FAIR
(see FORCE11 (2020))? NA, we do not intend to re-
lease a dataset
(g) If you are curating or releasing new datasets, did you
create a Datasheet for the Dataset (see Gebru et al.
(2021))? NA, we do not intend to release a dataset
6. Additionally, if you used crowdsourcing or conducted re-
search with human subjects...

--- Page 14 ---

(a) Did you include the full text of instructions given
to participants and screenshots? NA, we neither used
crowdsourcing nor conducted research with human
subjects.
(b) Did you describe any potential participant risks, with
mentions of Institutional Review Board (IRB) ap-
provals? NA, we neither used crowdsourcing nor con-
ducted research with human subjects.
(c) Did you include the estimated hourly wage paid to
participants and the total amount spent on participant
compensation? NA, we neither used crowdsourcing
nor conducted research with human subjects.
(d) Did you discuss how data is stored, shared, and deiden-
tified? NA, we neither used crowdsourcing nor con-
ducted research with human subjects.

--- Page 15 ---

Figure 5: The steps of collecting the dataset. Yellow blocks represent the initial seeds used as a starting point. Green blocks
represent data collected using Twitter API that are related to the circulators and debunkers of fabricated Hadith.

--- Page 16 ---

Count
Users
Top Fabricated Hadith
233
142
I. ËA£ úG.
@ 	áK. ú
Î« I. k úÎ« A	KXBð@
	Qª	K 	à@ ÕÎð éJ
Ê« é<Ë@ úÎ é<Ë@ ÈñP A	KQÓ@
247
89
éJ.	K	X 	áÓ ÐY®K AÓ éË Q	®	« éÊJ
Ë ú
	¯ 	àA 	gYË@ èPñ @Q¯ 	áÓ
120
89
éK
ðAªÓ úÍ@ éª	¯Y	¯ ú
Î« YK
 	áÓ ÕÎ®Ë@ 	Y 	g@ ÕÎð éË@ð éJ
Ê« é<Ë@ úÎ é	K@
141
88
éÊg. Q	® éK
ðAªÓ úÍ@ ©	¯X ÕÎð éË@ð éJ
Ê« é<Ë@ úÎ é	K@
69
65
é ¢. ú
	¯ úæñÓð èYë	P ú
	¯ úæ
m'
ð éÒºk ú
	¯ Õæ
ë@QK.@ð éÒê	¯ ú
	¯ hñ	Kð éÒÊ« ú
	¯ ÐX@ úÍ@ Q 	¢	JK
 	à@ X@P@ 	áÓ
ú
Î« úÍ@ Q 	¢	JJ
Ê	¯
77
62
I. ¢mÌ'@ PA	JË@ É¿AK AÒ» HAJ
Ë@ É¿AK
 ú
Î« I. k
65
51
éJ
K. Éë@ ÕÎð éË@ð éJ
Ê« é<Ë@ úÎ ÈA®	¯ ÕËAªË@ ú
	¯ A	JË@ Yë	P@ 	áÓ
371
47
ZAJ
.	KB@ H. @ñK éJJ
¢«@ èC É¿ QK.X ú
	¯ ú
æQºË@ éK
@ @Q¯ 	áÓ úæñÖÏ é<Ë@ ÈA¯
342
43
AK
 ½ÊÖÏ@ ½Ë	X ú
Í ÈA¯ ú
æÓ@ 	áÓ Ég. P ú
Î« úÎ @	XA	¯ ø
 Q.¯ Y	J« A¾ÊÓ ú
G. É¿ð é<Ë@ 	àA	¯ ú
Î« èCË@ @ðQ»@
é«AË@ ½J
Ê« úÎ 	àC	¯ 	áK. 	àC	¯ 	à@ YÒm×
51
41
éK.AK. 	áÓ éKAJ
Ê	¯ ÕÎªË@ X@P@ 	áÔ	¯ AîE.AK. ú
Î«ð ÕÎªË@ é	JK
YÓ A	K@
Table 4: The most shared fabricated hadiths in the timelines of the users in our dataset along with the number of unique users
sharing them and their total number of occurrences.

```
