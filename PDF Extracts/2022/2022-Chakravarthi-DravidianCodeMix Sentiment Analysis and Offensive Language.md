---
title: "2022-Chakravarthi-DravidianCodeMix Sentiment Analysis and Offensive Language - PDF Extract"
source_pdf: "2022-Chakravarthi-DravidianCodeMix Sentiment Analysis and Offensive Language.pdf"
pages: 36
extracted_at: "2026-02-13T09:15:42.596008"
---

# PDF Extract: 2022-Chakravarthi-DravidianCodeMix Sentiment Analysis and Offensive Language

**Source PDF:** 2022-Chakravarthi-DravidianCodeMix Sentiment Analysis and Offensive Language.pdf
**Total Pages:** 36

---

## Content

```
--- Page 1 ---

Language Resources and Evaluation Journal manuscript No.
(will be inserted by the editor)
DravidianCodeMix: Sentiment Analysis and Offensive
Language Identiﬁcation Dataset for Dravidian Languages in
Code-Mixed Text
Bharathi Raja Chakravarthi1 ⋅Ruba
Priyadharshini2 ⋅Vigneshwaran Muralidaran3 ⋅
Navya Jose4 ⋅Shardul Suryawanshi1 ⋅
Elizabeth Sherly4 ⋅John P. McCrae1
Received: date / Accepted: date
Abstract This paper describes the development of a multilingual, manually anno-
tated dataset for three under-resourced Dravidian languages generated from social
media comments. The dataset was annotated for sentiment analysis and offensive lan-
guage identiﬁcation for a total of more than 60,000 YouTube comments. The dataset
consists of around 44,000 comments in Tamil-English, around 7,000 comments in
Kannada-English, and around 20,000 comments in Malayalam-English. The data was
manually annotated by volunteer annotators and has a high inter-annotator agreement
in Krippendorff’s alpha. The dataset contains all types of code-mixing phenomena
Bharathi Raja Chakravarthi*
E-mail: bharathi.raja@insight-centre.org
Ruba Priyadharshini
E-mail: rubapriyadharshini.a@gmail.com
Vigneshwaran Muralidaran
E-mail: MuralidaranV@cardiff.ac.uk
Navya Jose
E-mail: navya.mi3@iiitmk.ac.in
Shardul Suryawanshi
E-mail: shardul.suryawanshi@insight-centre.org
Elizabeth Sherly
E-mail: sherly@iiitmk.ac.in
John P. McCrae
E-mail: john.mccrae@insight-centre.org
1Insight SFI Research Centre for Data Analytics, Data Science Institute, National University of
Ireland Galway, Galway, Ireland
2ULTRA Arts and Science College, Madurai, Tamil Nadu, India
3School of Computer Science and Informatics, Cardiff University, Cardiff, United Kingdom
4Indian Institute of Information Technology and Management-Kerala, Kerala, India
arXiv:2106.09460v1  [cs.CL]  17 Jun 2021

--- Page 2 ---

2
Chakravarthi et al
since it comprises user-generated content from a multilingual country. We also present
baseline experiments to establish benchmarks on the dataset using machine learning
methods. The dataset is available on Github 1 and Zenodo 2.
Keywords Dravidian languages ⋅Sentiment Analysis ⋅Offensive Language
Identiﬁcation ⋅Tamil ⋅Kannada ⋅Malayalam ⋅Code-Mixed ⋅Corpora
1 Introduction
Sentiment analysis is the classiﬁcation task of mining sentiments from natural lan-
guage, which ﬁnds use in numerous applications such as reputation management,
customer support, and moderating content in social media (Wilson et al., 2005; Agar-
wal et al., 2011; Thavareesan and Mahesan, 2019, 2020a). Sentiment analysis has
helped industry to compile a summary of human perspectives and interests derived
from feedback or even just the polarity of comments (Pang and Lee, 2004; Thavareesan
and Mahesan, 2020b). Offensive language identiﬁcation is another classiﬁcation task
in natural language processing (NLP), where the aim is to moderate and minimise
offensive content in social media. In recent years, sentiment analysis and offensive
language identiﬁcation have gained signiﬁcant interest in the ﬁeld of NLP.
Social media websites and product review forums provide opportunities for users
to create content in informal settings. Moreover, to improve user experience, these
platforms ensure that the user communicates his/her opinion in such a way that he/she
feels comfortable either using native language or switching between one or more
languages in the same conversation (Vyas et al., 2014). However, most NLP systems
are trained on languages in formal settings with proper grammar, which creates issues
when it comes to the analysis phase of "user generated" comments (Chanda et al.,
2016; Pratapa et al., 2018). Further, most of the developments in sentiment analysis
and offensive language identiﬁcation systems are performed on monolingual data for
high-resource languages, while the user-generated content in under-resourced settings
are often mixed with English or other high-resource languages (Winata et al., 2019;
Jose et al., 2020).
Code-mixing or code-switching is the alternation between two or more languages at
the level of the document, paragraph, comments, sentence, phrase, word or morpheme.
It is a distinctive aspect of conversation or dialogue in bilingual and multilingual
societies (Barman et al., 2014). It is motivated by structural, discourse, pragmatic
and socio-linguistic reasons (Sridhar, 1978). Most of the social media comments are
code-mixed, while the resources created for sentiment analysis and offensive language
identiﬁcation are primarily available for monolingual texts. Code-mixing occurs in
daily life, such as in normal conversation or social media conversation in both audio
and text format. Code-mixing refers to the way a bilingual/ multilingual speaker
changes his or her utterance into another language. The vast majority of language
pairs are under-resourced with regards to code-mixing tasks (Bali et al., 2014; Jose
et al., 2020).
1 https://github.com/bharathichezhiyan/DravidianCodeMix-Dataset
2 https://zenodo.org/record/4750858#.YJtw0SYo_0M

--- Page 3 ---

DravidianCodeMix: Classiﬁcation Dataset for Dravidian Languages Code-Mixed Text
3
In this paper, we describe the creation of a corpus for Dravidian languages in
the context of sentiment analysis and offensive language detection tasks. Dravidian
languages are spoken mainly in the south of India (Chakravarthi et al., 2020c). The
four major literary languages belonging to the language family are Tamil (ISO 639-3:
tam), Telugu (ISO 639-3: tel), Malayalam (ISO 639-3: mal), and Kannada (ISO 639-3:
kan). Tamil, Malayalam and Kannada fall under the South Dravidian subgroup while
Telugu belongs to the South Central Dravidian subgroup (Vikram and Urs, 2007).
Each of the four languages has ofﬁcial status as one of the 22 scheduled languages
recognised by the Government of India. Tamil also has ofﬁcial status in Sri Lanka and
Singapore (Thamburaj and Rengganathan, 2015). Although the languages are widely
spoken by millions of people, the tools and resources available for building robust
NLP applications are under-developed for these languages.
Dravidian languages are highly agglutinating languages and each language uses its
own script (Krishnamurti, 2003; Sakuntharaj and Mahesan, 2016, 2017). The writing
system is a phonemic abugida written from left to right. The Tamil language was
written using Tamili, Vattezhuthu, Chola, Pallava and Chola-Pallava scripts at different
points in history. The modern Tamil script descended from the Chola-Pallava script that
was conceived around the 4th century CE (Sakuntharaj and Mahesan, 2018a,b). The
Malayalam script is based on the Vatteluttu script developed from old Vatteluttu with
additional letters from Grantha script to write loan words (Thottingal, 2019). Similarly,
the Kannada and Telugu scripts evolved from Bhattiprolu Brahmi. Nevertheless, social
media users often use the Latin script for typing in these languages due to its ease of
use and accessibility in handheld devices and computers (Thamburaj et al., 2015).
Monolingual datasets are available for Indian languages for various research aims
(Agrawal et al., 2018; Thenmozhi and Aravindan, 2018; Kumar et al., 2020). However,
there have been few attempts to make datasets for Tamil, Kannada and Malayalam
code-mixed text (Chakravarthi et al., 2020b,c; Chakravarthi, 2020; Chakravarthi and
Muralidaran, 2021). We believe it is essential to come up with approaches to tackle
this resource bottleneck so that these languages can be equipped with NLP support in
social media in a way that is both cost-effective and rapid. To create resources for a
Tamil-English, Kannada-English and Malayalam-English code-mixed scenario, we
collected comments on various Tamil, Kannada and Malayalam movie trailers from
YouTube.
The contributions of this paper are:
1. We present the dataset for three Dravidian languages, namely Tamil, Kannada, and
Malayalam, for sentiment analysis and offensive language identiﬁcation tasks.
2. The dataset contains all types3 of code-mixing. This is the ﬁrst Dravidian language
dataset to contain all types of code-mixing, including mixtures of these scripts and
the Latin script. The dataset consists of around 44,000 comments in Tamil-English,
around 7,000 comments in Kannada-English, and around 20,000 comments in
Malayalam-English.
3. We provide an experimental analysis of logistic regression, naive Bayes, decision
tree, random forest, and SVM on our code-mixed data for classiﬁcation tasks so as
to create a benchmark for further research.
3 different types of code-mixing are shown in Figure 2

--- Page 4 ---

4
Chakravarthi et al
2 Related Work
Sentiment analysis helps to understand the polarity (positive, negative or neutral) of
the audience towards a content (comment, tweet, image, video) or an event (Brexit,
presidential elections). This data on polarity can help in understanding public opinion.
Furthermore, the inclusion of sentiment analysis can improve the performance of tasks
such as recommendation system (Krishna et al., 2013; Musto et al., 2017), and hate
speech detection (Gitari et al., 2015). Over the last 20 years, social media networks
have become a rich data source for sentiment analysis (Clarke and Grieve, 2017; Tian
et al., 2017). Extensive research has been done for sentiment analysis of monolingual
corpora such as English (Hu and Liu, 2004; Wiebe et al., 2005; Jiang et al., 2019),
Russian (Rogers et al., 2018), German (Cieliebak et al., 2017), Norwegian (Mæhlum
et al., 2019) and Indian languages (Agrawal et al., 2018; Rani et al., 2020). In initial
research workds, n-gram features were used widely for classiﬁcation of sentiments
(Kouloumpis et al., 2011). However recently, due to readily available data on social
media, these traditional techniques have been replaced by deep neural network tech-
niques. Patwa et al. (2020) conducted sentiment analysis on code-mixed social media
text for Hindi-English and Spanish-English languages. However, sentiment analysis in
Dravidian languages is under-studied.
The anonymous and consequence-free nature of social media posts has prolif-
erated the use of aggressive, hateful or offensive language online. This downturn
has encouraged the development of automatic moderation systems. These systems
if trained on proper data can help detect aggressive speech thus moderating spiteful
content on a public platform. Collection of such data has become a crucial part of
social media analysis. To facilitate the researchers working on these problems, there
have been shared tasks conducted on aggression identiﬁcation in social media (Kumar
et al., 2018) and offensive language identiﬁcation (Zampieri et al., 2019) by provid-
ing necessary datasets. As English is a commonly used language on social media, a
signiﬁcant amount of research goes into the identiﬁcation of offensive English text.
However, many internet users prefer the use of their native languages. This has given
rise to the development of offensive language identiﬁcation dataset in Arabic, Danish,
Greek, and Turkish languages (Zampieri et al., 2020). Inspired by this we developed
resources for offensive language identiﬁcation for Dravidian languages.
In the past few years, cheaper internet and increased use of smartphones have signif-
icantly increased social media interaction in code-mixed native languages. Dravidian
language speakers (who are often bilingual with English as it is an ofﬁcial language
in India) with a population base of 215 million 4 contribute to large portion of such
interactions. Hence, there is an ever-increasing need for the analysis of code-mixed
text in Dravidian languages. However, the number of freely available code-mixed
dataset (Ranjan et al., 2016; Jose et al., 2020) are still limited in number, size, and
availability. Towards building language identiﬁcation (LID) systems in code-mixed
languages, Sowmya Lakshmi and Shambhavi (2017) developed a Kannada-English
dataset containing English and Kannada text with word-level code-mixing. Also, they
employed a stance detection system to detect stance in Kannada-English code-mixed
4 https://www.britannica.com/topic/Dravidian-languages

--- Page 5 ---

DravidianCodeMix: Classiﬁcation Dataset for Dravidian Languages Code-Mixed Text
5
Scrape 
YouTube 
comments
Unprocessed 
data
Preprocess
Preprocessed 
data
Send to Annotators
Annotation for 
sentiment 
classification
Code-mixed 
sentiment 
dataset
Annotation for 
offensive language 
classification
Code-mixed 
offensive language 
identification dataset  
Fig. 1 Data collection process.
text (on social media) using sentence embeddings. Shalini et al. (2018) have used
distributed representations for sentiment analysis of Kannada-English code-mixed
texts through neural networks, which had three tags: Positive, Negative and Neutral.
However, the dataset for Kannada was not readily available for research purposes. To
give motivation for further research we conducted (Chakravarthi et al., 2020a,d; Mandl
et al., 2020; Chakravarthi et al., 2021) a shared task that provided Tamil-English,
Kannada-English, and Malayalam-English code-mixed datasets using which partici-
pants trained models that identify the sentiments (task A) and offensive classes (task
B) in both the languages.
Most of the recent studies on sentiment analysis and offensive language identi-
ﬁcation have been conducted on high-resourced languages from social media plat-
forms. Models trained on such highly resourced monolingual data have succeeded
in predicting sentiment and offensiveness. However, with the increased social media
usage of bilingual users, a system trained on under-resourced code-mixed data is
needed. In spite of this need, no large datasets for Tamil-English, Kannada-English
and Malayalam-English are available. Hence, inspired by Severyn et al. (2014), we col-
lected and created a code-mixed dataset from YouTube. In this work, we describe the
process of corpora creation for under-resourced Dravidian languages from YouTube
comments. This is an extension of two workshop papers (Chakravarthi et al., 2020b,c)
and shared tasks (Chakravarthi et al., 2020d). We present DravidianCodeMix corpora
for Tamil-English (40,000+ comments), Kannada-English (7,000+ comments) and
Malayalam-English (nearly 20,000 comments) with manually annotated labels for
sentiment analysis and offensive language identiﬁcation. We used Krippendorff’s
alpha to calculate agreement amongst annotators. We made sure that each comment is
annotated by at least three annotators and made the labelled corpora freely available for
research purpose. For bench marking, we provided baseline experiments and results
on ’DravidianCodeMix’ corpora using machine learning models.
3 Raw Data
Online media, for example, Twitter, Facebook or YouTube, contain quickly changing
data produced by millions of users that can drastically alter the reputation of an
individual or an association. This raises the signiﬁcance of programmed extraction
of sentiments and offensive language used in online social media. YouTube is one
of social media which is getting popular in the Indian subcontinent because of the
wide range of content available from the platform such as songs, tutorials, product
reviews, trailers and so on. YouTube allows users to create content and other users to

--- Page 6 ---

6
Chakravarthi et al
 
Code-Switching Type 
Example 
Translation 
No Code-mixing 
Only Tamil (Written in Tamil 
script) 
இឝ மாதிரி ஒអ படញைத தாប இញதைன 
வអஷமா எதிណபாណញឝெகாឈផអដேதன 
ផெரឍலណ  பாណឃភឌேபாேத மனយឃភ 
அថவளឤ சដேதாசமா இអឃភ 
How long I have been waiting for this kind 
of movie! Feels joyful just watching this 
trailer. 
Inter-sentential code-mixing Mix 
of English and Tamil (Tamil 
written only in Tamil script) 
ெரជផயாណ சឲகឌ சாណபாக படឌ  ெவនறி 
ெபற வாទញឝឃகធ... Mohan  G all the 
very best we all behind you. 
On behalf of Reddiyar community, I am 
wishing the best for this movie. Mohan G, 
All the very best. We are all behind you. 
Only Tamil (Written in Latin 
script) 
inga niraya perukku illatha kedda 
palakkam enkidda irukku.  vasool 
mannan VIJAY anna 
‘I have a bad habit which is not found here 
in others’. Brother Vijay is the king of 
blockbusters.  
Code-switching at morphological 
level (Written in both Tamil and 
Latin script) 
ஓ விஜឍ படញឝឃភ இឋபផதாប viewers 
sekkuringala 
Oh. So this is how you gather more 
viewers for Vijay’s movie? 
Intra-sentential mix of English 
and Tamil (written in Latin script 
only) 
patti thotti engum pattaya kelaputha 
ne va thalaiva iam waiting 
Rocking performance that will be a hit 
among every type of audience. Come on, 
my star. I am waiting. 
Inter-sentential and 
intra-sentential mix (Tamil written 
in both Tamil script and Latin 
script) 
இដத படញத வர விட ឩடாឝ...இដத படញத 
திைரயரងகிត ஓட விட ឩடாឝឨ எவனாឝ 
தைட பបனா ...Theatre la vera endha 
padam odunaalum screen கிழிឡឌ 
If anybody imposes a ban that this movie 
should not be released, that it should not 
be allowed to run on theatres, then the 
screens will be torn if any other movie is 
released. 
Fig. 2 Examples of code mixing in Tamil dataset.
 
COMMENT TYPE 
EXAMPLE 
 TRANSLATION 
Only English 
Concentrate on hindi promotion.. sir 
Concentrate on Hindi promotion.. sir 
Only Kannada (written in Kannada 
Script only) 
ಎº ಗುರು ಎº æå§ ಎº ಮೂzë§ ನಮy 
ಮĀಯæ} ಈ ¤ಾ×ñ ಫĔÃ àೕದ ಆÏದć. 
 
Great lyrics and music mate, Everyone in my 
home are obsessed with this song. 
Mix of English and Kannada 
(Kannada written in Kannada 
script only) 
My favorite song in 2019 is Taaja 
samachara £ಾìತz ß{ಯćೕ ಒąy ಈ ¤ಾಡು 
ïೕçþ{ ïೕಾpĀ ಇăೕ^ಕು ಅನುüp .... Everybody 
watch this. 
 
My favourite song in 2019 is Taaja 
samachara. If it is heard by literary lovers, 
they would want to hear it again. 
Everybody watch this. 
Only Kannada (written in English) 
Neevu varshkke ondu cinema madru 
supper 1varshkke 3-4cinema 
madobadalige intha ondu cinema saku. 
 
If you make one movie a year it’s super, 
instead of doing 3-4 movies a year, one 
movie of this type is enough. 
Only Kannada (written in both 
Kannada and English script) 
Nanage ಅನುüp ಈ èೕ×ęೕ ವನುt ರéyಯ 
ಮಂದಣo ಾzº deslike ಾ×ರಬಹುದು. 
 
 I feel that this video has been disliked by 
the fans of Rashmika Mandana. 
Mix of English and Kannada 
(written in English only) 
Wonderful song daily 5/6 kelalill Andre 
eno miss madakodante. 
A wonderful song, if I don’t hear this song 
5-6 times a day, I feel like I am missing 
something. 
Mix of English and Kannada  
(Kannada written in both English 
and Kannada script) 
ñೂÚpಲ} ರĝ¶ ċಟು{ ನಟĀñ ಾನು àಾ .. 
ಾÈ waiting for ಮೂè .... ಚåü{ ಬćęೕ 
ಎಲ} ಲĚಣ ಇþ .. All The best your bright 
ಫĕzಚÁ. 
Don’t know why I am obsessed with Rakshit 
Shetty’s acting. waiting for your movie, 
expecting it to be a blockbuster. All the best 
for your bright future. 
Fig. 3 Examples of code mixing in Kannada dataset.
comment on the content. It allows for more user-generated content in under-resourced
languages. Hence, we chose YouTube to extract comments to create our dataset. We
chose movie trailers as the topic to collect data because movies are quite popular
among the Tamil, Malayalam, and Kannada speaking populace. This increases the
chance of getting varied views on one topic. Figure 1 shows the overview of the steps
involved in creating our dataset.

--- Page 7 ---

DravidianCodeMix: Classiﬁcation Dataset for Dravidian Languages Code-Mixed Text
7
Code-Switching Type 
Example 
Translation 
Only English 
Very good movie-making skills in your 
language.. keep up the good work 
Very good movie-making skills in your 
language.. keep up the good work. 
No-code-mixing: 
Only Malayalam (Written in Malayalam 
Script only) 
െപെ­ºു പറ¦ാൽ ശാപം 
എിൽ അനെ³ മന×് 
ഉÎവരുെട അÆമാർ പുരുഷ»ാർ 
ആേണാ? 
If women are a curse, are the mothers 
of such people men? 
Inter-sentential code-mixing: 
Mix of English and Malayalam 
(Malayalam written in Malayalam script 
only) 
 Highly promising trailer.  പഴയ മ¥ു 
േചിെയ തിരിá കി§ിയത് േപാെല 
േതാºുºു. 
 
Highly promising trailer. It feels like got 
that old Manju sister back. 
Only Malayalam (Written in Latin script) 
Ee onathinu nalloru 
kudumbhachithram 
pratheekshikkunnu. 
Expecting a good family entertainer for 
this Onam. 
Code-switching in morphological level 
(written in both Malayalam and Latin 
script) 
കുറá കാല³ിനു േശഷം സി·ിഖ് 
വീ®ും comedy യിൽ sajeevamayi. 
After some time Siddique became 
active again in comedy. 
Intra-sentential mix of English and 
Malayalam (written in Latin Script only) 
Video song kaanathe unlike 
adikkunath nallakaaryam alla 
It is not fair to unlike a video song 
without watching the same. 
Inter-sentential and Intra- sentential 
mix.  
(Malayalam written in both Latin and 
Malayalam script) 
പടം success ആവിÍ എºാണ് 
vichariche. ഇതിേ¿ാ nice ആണ്... 
Full comedy with െപാളി climax 
pratheekshikunnu..I am waiting. 
Thought this movie will not be a 
success. But it is nice now. Expecting 
full comedy and an awesome climax. I 
am waiting. 
Fig. 4 Examples of code mixing in Malayalam dataset.
We compiled the comments from different ﬁlm trailers of Tamil, Kannada, and
Malayalam languages from YouTube in the year 2019. The comments were gathered
using YouTube Comment Scraper tool5. We utilized these comments to make the
datasets for sentiment analysis and offensive language identiﬁcation with manual
annotations. We intended to collect comments that contain code-mixing at various
levels of the text, with enough representation for each sentiment and offensive language
classes in all three languages. It was a challenging task to extract the necessary text
that suited our intent from the comment section, which was further complicated by
the presence of remarks in other non-target languages. As a part of the preprocessing
steps to clean the data, we utilized langdetect library 6 to tell different languages
apart and eliminate the unintended languages. Examples of code-mixing in Tamil,
Kannada and Malayalam corpora are shown in Figure 2, Figure 3, and Figure 4 along
with their translations in English. By keeping data privacy in mind, we made sure
that all the user-related information is removed from the corpora. As a part of the
text-preprocessing, we removed redundant information such as URL.
Since we collected corpora from social media, our corpora contain different types
of real-world code-mixed data. Inter-sentential switching is characterised by change of
language between sentences where each sentence is written or spoken in one language.
Intra-sentential switching occurs within a single sentence, say one of the clause is in
one language and the other clause is in the second language. Our corpora contains all
forms of code-mixing ranging from purely monolingual texts in native languages to
mixing of scripts, words, morphology, inter-sentential and intra-sentential switches.
5 https://github.com/philbot9/youtube-remarkscraper
6 https://pypi.org/venture/langdetect/

--- Page 8 ---

8
Chakravarthi et al
We retained all the instances of code-mixing to faithfully preserve the real-world usage.
4 Methodology of Annotation
We create our corpora for two tasks, namely, sentiment analysis and offensive language
identiﬁcation. We anonymized the data gathered from Youtube in order to protect user
privacy.
4.1 Annotation Process
In order to ﬁnd volunteers for the annotation process, we contacted students in In-
dian Institute of Information Technology and Management-Kerala for Malayalam,
Indian Institute of Information Technology-Tiruchirapalli and Madurai Kamaraj Uni-
versity for Tamil. For Kannada, we contacted students in Visvesvaraya College of
Engineering, Bangalore University. The student volunteer annotators received the link
to a Google Form and did the annotations on their personal computers. The authors’
family members also volunteered to annotate the data. We created Google Forms to
gather annotations from annotators. Information on gender, education background
and medium of schooling were collected to know the diversity of the annotators. The
annotators were cautioned that the user remarks may have hostile language. They were
given a provision to discontinue with the annotation process in case the content is
too upsetting to deal with. They were asked not to be partial to a speciﬁc individual,
circumstance or occasion during the annotation process. Each Google form had been
set to contain up to 100 comments and each page was limited to contain 10 comments.
The annotators were instructed to agree that they understood the scheme before they
were allowed to proceed further. The annotation setup involved three stages. To begin
with, each sentence was annotated by two individuals. In the second step, the data was
included in the collection if both the annotations agreed. In the event of contention, a
third individual was asked to annotate the sentence. In the third step, in the uncommon
case that all the three of them disagreed, at that point, two additional annotators were
brought in to label the sentences. Each form was annotated by at least three annotators.
4.2 Sentiment Analysis
For sentiment analysis, we followed the methodology taken by Chakravarthi et al.
(2020c), and involved at least three annotators to label each sentence. The following
annotation schema was given to the annotators in English and Dravidian languages.
– Positive state: Comment contains an explicit or implicit clue in the content rec-
ommending that the speaker is in a positive state.
– Negative state: Comment contains an explicit or implicit clue in the content
recommending that the speaker is in a negative state.

--- Page 9 ---

DravidianCodeMix: Classiﬁcation Dataset for Dravidian Languages Code-Mixed Text
9
Fig. 5 Example Google Form with annotation instructions for sentiment analysis

--- Page 10 ---

10
Chakravarthi et al
– Mixed feelings: Comment contains an explicit or implicit clue in both positive
and negative feeling.
– Neutral state: Comment does not contain an explicit or implicit indicator of the
speaker’s emotional state.
– Not in intended language: If the comment is not in the intended language. For
example, for Tamil, if the sentence does not contain Tamil written in Tamil script
or Latin script, then it is not Tamil.
Figures 5 and 6 show the sample Google Forms for general instructions and sentiment
analysis respectively.
4.3 Offensive Language Identiﬁcation
We constructed offensive language identiﬁcation dataset for Dravidian languages at
different levels of complexity following the work of Zampieri et al. (2019). More
generally we expand this expand to a three-level hierarchical annotation schema. We
added a new category Not in intended language to account for comments written
in a language other than the intended language. Examples for this are the comments
written in other Dravidian languages using Roman script. To simplify the annotation
decisions, we split offensive language categories into six labels.
– Not Offensive: Comment does not contain offence or profanity.
– Offensive Untargeted: Comment contains offence or profanity not directed to-
wards any target. These are the comments which contain unacceptable language
without targeting anyone.
– Offensive Targeted Individual: Comment contains offence or profanity which
targets an individual.
– Offensive Targeted Group: Comment contains offence or profanity which targets
a group or a community.
– Offensive Targeted Other: Comment contains offence or profanity which does
not belong to any of the previous two categories (e.g. a situation, an issue, an
organization or an event).
– Not in indented language: If the comment is not in the intended language. For
example, in Tamil task, if the sentence does not contain Tamil written in Tamil
script or Latin script, then it is not Tamil.
Examples of the Google Forms in English and native language for offensive language
identiﬁcation task are given in Figure 7, Figure 8, and Figure 9. Once the Google Form
was ready, we sent it out to an equal number of males and females to enquire their
willingness to annotate. We got varied responses from them and so our distribution of
male and female annotators involved in the task are different. From Table 1, we can
see that only two female annotators volunteered to contribute for Tamil while there
were more female annotators for Malayalam and Kannada. For offensive language
identiﬁcation, we can see that there is a balance in gender from Table 2. The majority
of the annotators have received postgraduate level of education. We were not able to
ﬁnd volunteers of non-binary gender to annotate our dataset. All the annotators who
volunteered to annotate the Tamil-English, Kannada-English and Malayalam-English

--- Page 11 ---

DravidianCodeMix: Classiﬁcation Dataset for Dravidian Languages Code-Mixed Text
11
Fig. 6 Examples from the ﬁrst page of the Google form for sentiment analysis

--- Page 12 ---

12
Chakravarthi et al
Fig. 7 Example Google Form with annotation instructions for offensive language identiﬁcation
Language
Tamil
Malayalam
Kannada
Gender
Male
9
2
2
Female
2
4
3
Non-binary
0
0
0
Higher Education
Undegraduate
2
0
1
Graduate
2
0
2
Postgraduate
7
6
2
Medium of Schooling
English
6
5
4
Native language
5
1
1
Total
11
6
5
Table 1 Annotators Statistics for Sentiment Analysis
datasets had bilingual proﬁciency in the respective code-mixed pairs and they were
prepared to take up the task seriously. From Table 1 and 2, we can observe that the

--- Page 13 ---

DravidianCodeMix: Classiﬁcation Dataset for Dravidian Languages Code-Mixed Text
13
Fig. 8 Example Google Form with annotation instructions for offensive language identiﬁcation

--- Page 14 ---

14
Chakravarthi et al
Fig. 9 Examples from the ﬁrst page of the Google Form for offensive language identiﬁcation
majority of the annotators’ medium of schooling is English even though their mother
tongue is Tamil, Kannada or Malayalam. For Kannada and Malayalam languages only
one annotator from each language received their education through the medium of their
native language. Although the medium of education of the participants was skewed
towards the English language, we were careful it would not affect the annotation task
by ensuring that all of them are fully proﬁcient in using their native language.
A sample form (ﬁrst assignment) was annotated by experts and a gold standard
was created. We manually compared the gold standard annotations with the volunteer
submission form. To control the quality of annotation, we eliminated the annotators
whose label assignments in the ﬁrst form were not good. For instance, if the annotators

--- Page 15 ---

DravidianCodeMix: Classiﬁcation Dataset for Dravidian Languages Code-Mixed Text
15
Language
Tamil
Malayalam
Kannada
Gender
Male
6
2
3
Female
6
4
2
Non-binary
0
0
0
Higher Education
Undegraduate
2
0
0
Graduate
5
0
3
Postgraduate
5
6
2
Medium of Schooling
English
6
5
3
Native language
7
1
2
Total
12
6
5
Table 2 Annotators Statistics for Offensive Language Identiﬁcation
showed an unreasonable delay in responding or if they labelled all sentences with
the same label or if more than ﬁfty annotations in a form were wrong, we eliminated
those contributions. A total of 22 volunteers and 23 volunteers, for sentiment analysis
and offensive language identiﬁcation tasks respectively, were involved in the process.
Once they ﬁlled up the Google Form, 100 sentences were sent to them. If an annotator
offered to volunteer more, the next Google Form was sent to them with another set
of 100 sentences and in this way each volunteer chose to annotate as many sentences
from the corpus as they wanted.
Sentiment Analysis
Offensive Language Identiﬁcation
Nominal
Ordinal
Nominal
Ordinal
Tamil
0.6735
0.6534
0.7452
0.7634
Malayalam
0.8753
0.8463
0.8345
0.8374
Kannada
0.7356
0.7465
0.8456
0.8443
Table 3 Inter-annotator agreement in Krippendorff’s alpha
4.4 Inter-annotator agreement
Inter-annotator agreement is a measure of the extent to which the annotators agree in
their rating. This is necessary to ensure that the annotation scheme is consistent and
that different raters are able to assign the same sentiment label to a given comment.
There are two questions related to inter-annotator agreement: How do the annotators
agree or disagree in their annotation? How much of the observed agreement or dis-
agreement among the annotators might be due to chance? While the percentage of
agreement is fairly straightforward, answering the second question involves deﬁning
and modelling what chance is and how to measure the agreement due to chance. There
are different inter-annotator agreement measures that are intended to answer this in
order to measure the reliability of the annotation. We utilized Krippendorff’s alpha

--- Page 16 ---

16
Chakravarthi et al
(훼) (Krippendorff, 1970) to gauge the agreement between annotators because of the
nature of our annotation setup. Krippendorff’s alpha is a rigorous statistical measure
that accounts for incomplete data and, consequently, does not require every annotator
to annotate every sentence. It is also a measure that considers the level of disagree-
ment between the anticipated classes, which is critical in our annotation scheme. For
example, if the annotators differ among Positive and Negative class, this difference is
more genuine than when they differ between Mixed feelings and Neutral state. 훼is
sensitive to such disagreements. 훼is characterized by:
훼= 1−퐷표
퐷푒
(1)
퐷표is the observed disagreement between sentiment labels assigned by the annotators
and 퐷푒is the disagreement expected when the coding of sentiments can be attributed
to chance rather than due to the inherent property of the sentiment itself.
퐷표= 1
푛
∑
푐
∑
푘
표푐푘푚푒푡푟푖푐훿2
푐푘
(2)
퐷푒=
1
푛(푛−1)
∑
푐
∑
푘
푛푐. 푛푘푚푒푡푟푖푐훿2
푐푘
(3)
Here 표푐푘푛푐푛푘and 푛refer to the frequencies of values in the coincidence matrices
and 푚푒푡푟푖푐refers to any metric or level of measurement such as nominal, ordinal,
interval, ratio and others. Krippendorff’s alpha applies to all these metrics. We used
nominal and ordinal metric to calculate inter-annotator agreement. The range of 훼is
between ‘0’ and ‘1’, 1 ≥훼≥0. When 훼is ‘1’ there is perfect agreement between the
annotators and when ‘0’ the agreement is entirely due to chance. Care should be taken
in interpreting the reliability of the results shown by Krippendorf’s alpha because
reliability basically measures the amount of noise in the data. However, the location
of noise and the strength of the relationship measured will interfere with the reliability
of the estimate. It is customary to require 훼≥.800. A reasonable rule of thumb that
allows for tentative conclusions to be drawn requires 0.67 ≤훼≤0.8 while 훼≥.653
is the lowest conceivable limit. We used nltk7 for calculating Krippendorff’s alpha
(훼). The results of inter-annotator agreement between our annotators for different
languages on both sentiment analysis and offensive language identiﬁcation tasks are
shown in Table 3.
5 Corpus Statistics
Table 4 and Table 5 show the text statistics (number of words, vocabulary size, number
of comments, number of sentences, and average number of words per sentences) for
sentiment analysis and offensive language identiﬁcation for Tamil, Malayalam and
Kannada. The Tamil dataset had the highest number of samples while Kannada had
the least on both the tasks. On average, each comment contained only one sentence.
7 https://www.nltk.org/

--- Page 17 ---

DravidianCodeMix: Classiﬁcation Dataset for Dravidian Languages Code-Mixed Text
17
Fig. 10 Treemap for comparing sentiment classes across Tamil, Malayalam and Kannada
Fig. 11 Treemap for comparing offensive classes across Tamil, Malayalam and Kannada
Table 6 and Table 7 show the class distribution across Tamil, Malayalam and Kan-
nada in sentiment analysis and offensive language identiﬁcation tasks. Furthermore,
tree-maps in Figure 10 and Figure 11 depict the comparative analysis of distribution
of sentiment and offensive classes across languages. Figure 10 illustrates that there are
more number of samples labelled "Positive" than any other class in all the languages.
While the disparity between "Positive" and other classes is large in Tamil, it is not
the case with Malayalam and Kannada. In Malayalam, "Neutral state" is the second-
largest class in terms of distribution; 6,502 number of comments labelled "Neutral
state" could mean that most of the comments in Malayalam are vague remarks as the

--- Page 18 ---

18
Chakravarthi et al
Fig. 12 Treemap for comparing offensive classes (excluding Not Offensive class) across Tamil, Malayalam
and Kannada
sentiment behind them is unknown. On the other hand, Kannada has the least number
of "Neutral state" class. Figure 11 shows that all languages have not-offensive class
in the majority. In the case of Tamil, 71% of the total comments are not offensive,
while Malayalam has 85% non-offensive comments. But there is no consistent trend
observable amongst offensive classes across the languages shown in Figure 12. In
the case of Tamil, 60% of the offensive comments are targeted (group or individual).
Similar trends are seen in the case of Malayalam (66%) and Kannada (79%). Absence
(Malayalam) or least (Tamil, Kannada) number of targeted other category comments
points to the fact that most of the offensive comments are targeted towards either an
individual or a group. In the case of Kannada, it is interesting to see that 24% out of
total comments are in a language other than Kannada. This could mean that a Kannada
movie gets a signiﬁcant amount of audience who are not native Kannada speakers
or that Kannada speakers tend to use more languages other than English to generate
code-mixed content online.
Language
Tamil
Malayalam
Kannada
Number of words
513,311
224,207
65,002
Vocabulary Size
94,928
57,566
20,665
Number of comments
44,020
19,616
7,671
Number of sentences
52,750
24,014
8,472
Average number of words per sentence
11
11
8
Average number of sentences per comment
1
1
1
Table 4 Corpus statistics for Sentiment Analysis

--- Page 19 ---

DravidianCodeMix: Classiﬁcation Dataset for Dravidian Languages Code-Mixed Text
19
Language
Tamil
Malayalam
Kannada
Number of words
511,734
202,134
65,702
Vocabulary size
94,772
40,729
20,796
Number of comments
43,919
20,010
7,772
Number of sentences
52,617
23,652
8,586
Average number of words per sentence
11
10
8
Average number of sentences per comment
1
1
1
Table 5 Corpus statistics for Offensive Language Identiﬁcation
Class
Tamil
Malayalam
Kannada
Negative
5,228 (11.87 %)
2,600 (13.25 %)
1,484 (19.34 %)
Not in intended language
2,087 (4.74 %)
1,445 (736 %)
1,136 (14.80 %)
Neutral state
6,904 (15.68 %)
6,502 (33.14 %)
842 (10.97 %)
Mixed feelings
4,928 (1119 %)
1,162 (5.92 %)
691 (9.00 %)
Positive
24,873 (56.50 %)
7,907 (40.30 %)
3,518 (45.86 %)
Total
44,020
19,616
7,671
Table 6 Sentiment Analysis Dataset Distribution
Class
Tamil
Malayalam
Kannada
Not Offensive
31,808 (72.42 %)
17,697 (88.44 %)
4,336 (55.79 %)
O-Untargeted
3,630 (8.26 %)
240 (1.19 %)
278 (3.57 %)
O-Targeted Individual
2,965 (6.75 %)
290 (1.44 %)
628 (8.08 %)
O-Targeted Group
3,140 (7.14 %)
176 (0.87 %)
418 (5.37 %)
O-Targeted Others
590 (1.34 %)
-
153 (1.96 %)
Not in indented lang
1,786 (4.06 %)
1,607 (8.03 %)
1,898 (24.42 %)
Total
43,919
20,010
7,772
Table 7 Offensive language Identiﬁcation Dataset Distribution. O-Offensive. O-Untargeted: Offensive
Untargeted.
Our datasets are stored in tab separated ﬁles. The ﬁrst column of the tsv ﬁle
contains the comments from YouTube and the second column has the ﬁnal annotation.
6 Difﬁcult Examples
The social media comments that form our dataset are code-mixed showing a mixture of
Dravidian languages and English. This poses a few major difﬁculties while annotating
the sentiments and offensive language categories on our dataset. Dravidian languages
are under-resourced languages and the mixing of scripts makes the annotation task
difﬁcult since the annotators must have learned both the scripts, be familiar with how
English words are modiﬁed to native phonology and how the meaning of certain
English words have a different meaning in the given local language. Reading and

--- Page 20 ---

20
Chakravarthi et al
understanding the code mixed text often with non-standardised spelling is difﬁcult.
Moreover, we have created the annotation labels with the help of volunteer annotators
for three languages (not just one language). It is challenging and time consuming
to collect this much amount of data from bilingual, volunteer annotators from three
different language groups.
While annotating, it was found that some of the comments were ambiguous in con-
veying the right sentiment of the viewers. Hence the task of annotation for sentiment
analysis and offensive language identiﬁcation seemed difﬁcult. The problems include
the comparison of the movie with movies of same or other industries, expression
of opinion of different aspects of the movie in the same sentence. Below are a few
examples of such comments and details of how we resolved those issues are provided.
In this section, we talk about some examples from Tamil language that were difﬁcult
to annotate.
– Enakku iru mugan trailer gnabagam than varuthu - All it reminds me of is the
trailer of the movie Irumugan. Not sure whether the speaker enjoyed Irumugan
trailer or disliked it or simply observed the similarities between the two trailers.
The annotators found it difﬁcult to identify the sentiment behind the comment
consistently.
– Rajini ah vida akshay mass ah irukane - Akshay looks more amazing than
Rajini. Difﬁcult to decide if it is a disappointment that the villain looks better than
the hero or a positive appreciation for the villain actor. Some annotators interpreted
negative sentiment while some others took it as positive.
– Ada dei nama sambatha da dei - I wonder, Is this our sampath? Hey!. Conﬂict
between neutral and positive.
– Lokesh kanagaraj movie naalae.... English Rap....Song vandurum - If it is
a movie of Lokesh kanagaraj, it always has an English rap song. Ambiguous
sentiment.
– Ayayo bigil aprm release panratha idea iruka lokesh gaaru - Oh Dear! Are you
even considering releasing the movie Bigil, Mr.Lokesh?. This comment has a sinlge
word ‘garu’8 which is a non-Tamil , non-English word borrowed from Telugu
language which is a politeness marker. However, in this context the speaker uses
the word sarcastically to insult the director because of the undue delay in releasing
the movie. The annotators were inconsistent in interpreting this as offensive or
not-Tamil.
– No of dislikes la theriyudhu, idha yaru dislike panni irrupanga nu - It is
obvious from the number of dislikes as to who would have disliked this (trailer).
The comment below the trailer of a movie which talks about the caste issues
in contemporary Tamil society. Based on the content of the trailer, the speaker
offensively implies that the scheduled caste people are the ones who would have
disliked the movie and not other people. Recognising the offensive undercurrent
in a seemingly normal comment is difﬁcult and hence these examples complicate
the annotation process.
According to the instructions, questions about music director, movie release date and
comments containing speaker’s remarks about the date and time of watching the video
8 Telugu word for Mr

--- Page 21 ---

DravidianCodeMix: Classiﬁcation Dataset for Dravidian Languages Code-Mixed Text
21
should be treated as belonging to neutral class. However the above examples show
that some comments about the actors and movies can be ambiguously interpreted as
neutral or positive or negative. We found annotator disagreements in such sentences.
Below, we give similar examples from Malayalam.
– Realistic bhoothanghalil ninnu oru vimochanam pratheekshikkunnu -Hoping
for a deliverance from realistic demons. No category of audience can be pleased
simultaneously. The widespread opinion is that the Malayalam ﬁlm industry is
advancing with more realistic movies. Therefore a group of audience who is more
fond of action or non-realistic movies are not satisﬁed with this culture of realistic
movies. In this comment, the viewer is not insulting this growing culture, but
expecting that the upcoming ﬁlm is of his favourite genre. Hence we labelled it
non-offensive.
– Ithilum valiya jhimikki kammal vannatha - There was an even bigger ‘pendant
earring’. ‘Jhimikki kammal’ was a trending song from a movie of the same actor
mentioned here. The movie received huge publicity even before its release because
of the song but it turned out to be a disappointment after its release. Thus the
annotators got confused whether the comment is meant as an insult or not. But we
concluded that the viewer is not offending the present trailer but marks his opinion
as a warning for the audience to not judge the book by its cover.
– Ithu kandittu nalla tholinja comedyaayi thonniyathu enikku mathram aano?-
Am I the only person here who felt this a stupid comedy? The meaning of the
Malayalam word mentioned here corresponding to the word ‘stupid’ varies with
regions of Kerala. Hence the disparity in opinion between annotators who speaks
different dialects of Malayalam was evident. Though in few regions it is offensive,
generally it is considered as a byword for ‘bad’.
– aa cinemayude peru kollam. Ithu Dileep ne udheshichanu,ayale mathram ud-
heshichanu -The name of that movie is good. It is named after Dileep and intended
only for him. It is quite obvious that there is a chance of imagining several different
movie names based on the subjective predisposition of the annotator. As long as
the movie name is unknown here, apparently no insult can be proved and there is
no profane language used in the sentence either.
– Kanditt Amala Paul Aadai Tamil mattoru version aanu ennu thonnunu - It
looks like another version of Amala Paul’s Tamil movie Aadai. Here the viewer
doubts the Malayalam movie ‘Helen’ is similar to the Tamil movie ‘Aadai’. Though
the movie ‘Aadai’ was positively received by viewers and critics, we cannot
generalize and assume that this comment also as positive only because of this
comparison. Hence we add it to the category of ‘mixed feeling’.
– Evideo oru Hollywood story varunnilleee. Oru DBT. -Somewhere there is a Hol-
lywood storyline...one doubt. This is also a comparison comment of that same
movie ‘Helen’ mentioned above. Nevertheless, here the difference is that the movie
is compared with the Hollywood standard, which is well-known worldwide and is
generally considered positive. Hence it is marked as a positive comment.
– Trailer pole nalla story undayal mathiyarinu.-It was good enough to have a good
story like the trailer. Here viewer mentioned about two aspects of the movie viz:
‘trailer’ and ‘story’. He appreciates the trailer but doubts the quality of the story

--- Page 22 ---

22
Chakravarthi et al
at the same time. We considered this comment positive because it is clear that he
enjoyed the trailer and conveys strong optimism for the movie.
7 Benchmark Systems
In this section, we report the results obtained in three languages for both the tasks
in the corpora introduced above. Like many earlier studies, we approach the tasks
as text classiﬁcation tasks. In order to provide a simple baseline, we applied several
traditional machine learning algorithms such as Logistic Regression (LR), Support
Vector Machine (SVM), Multinomial Naive Bayes (MNB), K-Nearest Neigbours
(KNN), Decision Trees (DT) and Random Forests (RF) separately, for both sentiment
analysis and offensive language detection on the code-mixed datasets.
Tamil
Malayalam
Kannada
Training
35,220
15,694
6,136
Development
4,398
1,960
767
Test
4,402
1,962
768
Total
44,020
19,616
7,671
Table 8 Train-Development-Test Data Distribution with 90%-5%-5% train-dev-test split for Sentiment
Analysis
Tamil
Malayalam
Kannada
Training
35,139
16,010
6,217
Development
4,388
1,999
777
Test
4,392
2,001
778
Total
43,919
20,010
7,772
Table 9 Train-Development-Test Data Distribution with 90%-5%-5% train-dev-test for Offensive Language
Identiﬁcation
7.1 Experiments Setup
We used 90%-5%-5% randomly sampled data split for training, development and
test set for all the experimental setup. All the duplicated entries were removed from
the dataset before the split to make test and development data truly unseen. All the
experiments are tuned to the development set and tested on the test set.

--- Page 23 ---

DravidianCodeMix: Classiﬁcation Dataset for Dravidian Languages Code-Mixed Text
23
7.1.1 Logistic Regression (LR):
LR is one of the base-line machine learning algorithms, which is also a probabilistic
classiﬁer used for the task of classiﬁcation of data (Genkin et al. (2007)). This is
basically the transformed version of linear regression using the logistic function (Park
(2013)). Accordingly it takes the real-valued features as input which is later multiplied
by a weight and the sum is fed to the sigmoid function 휎(푧) also called the logistic
function to obtain the class probability (Shah et al. (2020)). The decision is made
based on the value set as threshold. Sigmoid function is as given below:
휎(푧) =
1
1+푒−푧
(4)
Logistic regression has a close relationship with neural networks as the latter can also
be viewed as a stack of several LR classiﬁers (de Gispert et al. (2015)). Unlike Naïve
Bayes which is a generative classiﬁer, LR is a discriminative classiﬁer (Ng and Jordan
(2002)). While Naïve Bayes holds strict conditional independence assumptions, LR is
evidently more robust to correlated features (Jin and Pedersen (2018)). It means that
when there are more than one features say F1,F2,F3 which are absolutely correlated,
it will divide the weight W among the features as W1,W2,W3 respectively.
We evaluated the Logistic Regression model with L2 regularization to reduce
overﬁtting. The input features are the Term Frequency Inverse Document Frequency
(TF-IDF) values of up to 3 grams. This approach results in the model being trained
only on this dataset without taking any pre-trained embeddings.
7.1.2 Support Vector Machine (SVM):
Support Vector Machine are a powerful supervised machine learning algorithm used
mainly for classiﬁcation tasks and for regression as well. The goal of an SVM is to
ﬁnd the hyperplane in an N-dimensional space which distinctly classiﬁes the data
points (Ekbal and Bandyopadhyay (2008)). It means, this algorithm clearly draws the
decision boundary line between the data points that belong to a particular category and
the ones that do not fall into the category. This is applicable to any kind of data that is
encoded as a vector. Therefore, if we could produce appropriate vector representations
of the data in our hand, we can use SVM to obtain the desired results (Ekbal and
Bandyopadhyay (2008)). Here the input features are the same as in LR that is the
Term Frequency Inverse Document Frequency (TF-IDF) values of up to 3 grams. We
evaluate the SVM model with L2 regularization.
7.1.3 Multinomial Naive Bayes (MNB):
This is a Bayesian classiﬁer that works on the naive assumption of conditional inde-
pendence of features. This means that each input is independent of the other and this
is absolutely unrealistic for real data. Nevertheless, it simpliﬁes several complex tasks
and hence validates the need.
We evaluate a Naive Bayes classiﬁer for multinomially distributed data, which
is derived from Bayes Theorem that ﬁnds the probability of a future event given an

--- Page 24 ---

24
Chakravarthi et al
observed event. MNB is a specialized version of Naive Bayes that is designed more
for text documents. Whereas simple naive Bayes would model a document as the
presence and absence of particular words, MNB explicitly models the word counts
and adjusts the underlying calculations to deal with in. Therefore, the input text data
is considered as the bag of words with the count of occurrence of words(frequency)
alone considered and the position of words are ignored.
Laplace smoothing is performed using 훼= 1 to solve the problem of zero proba-
bility and then evaluate the MNB model with TF-IDF vectors.
7.1.4 K-Nearest Neighbour (KNN):
KNN is used for the classiﬁcation and regression problems but mostly used for
classiﬁcation task.The KNN algorithm stores all available data and classiﬁes, on the
basis of similarities, a new data point. This implies that it can be conveniently grouped
into a well-suite group using the KNN algorithm as new data emerges. The KNN
algorithm assumes that the new upcoming data is related to the available cases and
places the new case into the column that is more similar to the categories available.
KNN is a non-parametric algorithm as it does not make any assumption on underlying
data (Nongmeikapam et al. (2017)). It is often referred to as a lazy learner algorithm
because it does not automatically learn from the training set, but instead stores the
dataset and performs an operation on the dataset at the time of classiﬁcation. At the
training point, the KNN algorithm only stores the dataset and then classiﬁes the data
into a group that is somewhat close to the current data as it encounters new data.
We use KNN for classiﬁcation with 3,4,5, and 9 neighbours by applying uniform
weights.
7.1.5 Decision Tree (DT):
The decision tree develops models of classiﬁcation or regression in the context of
a tree structure. A dataset is broken down into smaller and smaller subsets, while
an associated decision tree is gradually built at the same time. A tree with decision
nodes and leaf nodes is the ﬁnal product. Therefore, a decision tree classiﬁcation
works by generating a tree structure, where each node corresponds to a feature name,
and the branches correspond to the feature values. The leaves of the tree represent
the classiﬁcation labels. After sequentially choosing alternative decisions, each node
is recursively split again, and ﬁnally, the classiﬁer deﬁnes some rules to predict the
result. Decision trees can accommodate high dimensional data and perform classiﬁ-
cation without needing much computation. In general, a decision tree classiﬁer has
reasonable accuracy. While speaking about its cons, they are vulnerable to mistakes
in classiﬁcation problems having many classes and a comparatively limited number
of training examples. Moreover, it is computationally costly for preparation which
implies the method of growing a decision tree is expensive in terms of computation.
Each candidate splitting area must be organized at each node before it can ﬁnd the best
split. Combinations of ﬁelds are used in some algorithms and a search must be made
for optimum combination weights. Pruning algorithms can also be costly, because
it is important to shape and compare multiple candidate sub-trees. Here, maximum

--- Page 25 ---

DravidianCodeMix: Classiﬁcation Dataset for Dravidian Languages Code-Mixed Text
25
depth was 800, and minimum sample splits were 5 for DT. The criteria were Gini and
entropy.
7.1.6 Random Forest (RF):
Random forest is an ensemble classiﬁer that makes its prediction based on the com-
bination of different decision trees trained on datasets of the same size as training
set, called bootstraps, created from a random resampling on the training set itself
(Breiman, 2001). Once a tree is constructed, a set of bootstraps, which do not include
any particular record from the original dataset [out-of-bag (OOB) samples], is used as
test set. The error rate of the classiﬁcation of all the test sets is the OOB estimate of
the generalization error. RF showed important advantages over other methodologies
regarding the ability to handle highly non-linearly correlated data, robustness to noise,
tuning simplicity, and opportunity for efﬁcient parallel processing. Moreover, RF
presents another important characteristic: an intrinsic feature selection step, applied
prior to the classiﬁcation task, to reduce the variables space by giving an importance
value to each feature. RF follows speciﬁc rules for tree growing, tree combination,
self-testing and post-processing, it is robust to overﬁtting and it is considered more
stable in the presence of outliers and in very high dimensional parameter spaces than
other machine learning algorithms (Caruana and Niculescu-Mizil, 2006). We evaluate
the RF model with the same features as DT.
Classiﬁer Positive Negative Mixed feelings Neutral state Other language Macro Avg Weighted Avg
Support
2503
547
510
631
211
4402
4402
Precision
SVM
0.57
0.00
0.00
0.00
0.00
0.11
0.32
MNB
0.59
0.79
0.46
0.50
0.50
0.64
0.59
KNN
0.58
0.19
0.13
0.18
0.62
0.34
0.43
DT
0.65
0.32
0.23
0.36
0.52
0.42
0.51
LR
0.76
0.36
0.24
0.39
0.42
0.36
0.58
RF
0.62
0.59
0.71
0.56
0.80
0.66
0.63
Recall
SVM
1.00
0.00
0.00
0.00
0.00
0.20
0.57
MNB
1.00
0.06
0.00
0.04
0.04
0.28
0.59
KNN
0.70
0.04
0.06
0.29
0.07
0.23
0.46
DT
0.80
0.23
0.14
0.27
0.37
0.36
0.55
LR
0.64
0.43
0.28
0.44
0.64
0.40
0.54
RF
0.97
0.17
0.02
0.19
0.43
0.35
0.62
F-Score
SVM
0.72
0.00
0.00
0.00
0.00
0.14
0.41
MNB
0.74
0.11
0.01
0.08
0.08
0.28
0.47
KNN
0.63
0.07
0.08
0.23
0.13
0.23
0.42
DT
0.72
0.27
0.17
0.31
0.44
0.38
0.53
LR
0.69
0.39
0.26
0.41
0.51
0.38
0.56
RF
0.76
0.26
0.05
0.28
0.56
0.38
0.53
Table 10 Precision, Recall, and F-score for Tamil Sentiment Analysis

--- Page 26 ---

26
Chakravarthi et al
Classiﬁer Positive Negative Mixed feelings Neutral state Other language Macro Avg Weighted Avg
Support
755
285
131
645
146
1962
1962
Precision
SVM
0.38
0.00
0.00
0.00
0.00
0.08
0.15
MNB
0.49
0.88
0.00
0.60
0.88
0.57
0.58
KNN
0.43
0.32
0.41
0.37
0.59
0.42
0.41
DT
0.51
0.54
0.35
0.61
0.51
0.50
0.54
LR
0.73
0.57
0.34
0.52
0.50
0.53
0.59
RF
0.62
0.74
0.56
0.51
0.76
0.64
0.61
Recall
SVM
1.00
0.00
0.00
0.00
0.00
0.20
0.38
MNB
0.92
0.13
0.00
0.45
0.10
0.32
0.53
KNN
0.67
0.12
0.12
0.34
0.21
0.29
0.41
DT
0.79
0.32
0.21
0.40
0.42
0.43
0.53
LR
0.51
0.45
0.32
0.72
0.66
0.53
0.57
RF
0.63
0.31
0.14
0.77
0.41
0.45
0.58
F-Score
SVM
0.56
0.00
0.00
0.00
0.00
0.11
0.21
MNB
0.64
0.23
0.00
0.52
0.17
0.31
0.46
KNN
0.53
0.17
0.19
0.36
0.30
0.31
0.38
DT
0.62
0.40
0.26
0.49
0.46
0.44
0.51
LR
0.60
0.50
0.33
0.60
0.57
0.52
0.57
RF
0.62
0.44
0.22
0.62
0.53
0.49
0.56
Table 11 Precision, Recall, and F-score for Malayalam Sentiment Analysis
Classiﬁer Positive Negative Mixed feelings Neutral state Other language Macro Avg Weighted Avg
Support
363
162
57
83
103
768
768
Precision
RF
0.59
0.70
0.45
0.48
0.53
0.55
0.58
SVM
0.47
0.00
0.00
0.00
0.00
0.09
0.22
MNB
0.54
0.82
1.00
0.75
0.74
0.77
0.68
KNN
0.51
0.67
0.44
0.50
0.55
0.53
0.54
DT
0.59
0.61
0.21
0.39
0.45
0.45
0.53
LR
0.70
0.60
0.24
0.38
0.45
0.47
0.58
Recall
RF
0.87
0.48
0.06
0.18
0.50
0.42
0.59
SVM
1.00
0.00
0.00
0.00
0.00
0.20
0.47
MNB
0.99
0.36
0.02
0.04
0.14
0.31
0.57
KNN
0.91
0.10
0.07
0.05
0.41
0.31
0.52
DT
0.73
0.48
0.19
0.14
0.47
0.40
0.54
LR
0.69
0.51
0.26
0.36
0.55
0.48
0.57
F-Score
RF
0.7
0.57
0.11
0.27
0.52
0.43
0.55
SVM
0.64
0.00
0.00
0.00
0.00
0.13
0.30
MNB
0.70
0.50
0.03
0.07
0.23
0.31
0.48
KNN
0.65
0.17
0.12
0.09
0.47
0.30
0.43
DT
0.66
0.54
0.20
0.21
0.46
0.41
0.52
LR
0.70
0.55
0.25
0.37
0.50
0.47
0.57
Table 12 Precision, Recall, and F-score for Kannada Sentiment analysis

--- Page 27 ---

DravidianCodeMix: Classiﬁcation Dataset for Dravidian Languages Code-Mixed Text
27
Classiﬁer Not-O O-untargeted OTI OTG OT-Other Other language Macro Avg Weighted Avg
Support
3190
368
315
288
71
160
4392
4392
Precision
RF
0.77
0.48 0.65
0.43
1.00
0.88
0.70
0.72
SVM
0.73
0.67 0.25
0.12
0.00
0.91
0.45
0.65
MNB
0.74
0.79 1.00
1.00
0.00
0.96
0.75
0.78
KNN
0.73
0.67 0.25
0.12
0.00
0.91
0.45
0.65
DT
0.80
0.29 0.28
0.20
0.11
0.70
0.40
0.67
LR
0.87
0.29 0.27
0.14
0.03
0.68
0.38
0.71
Recall
RF
0.99
0.16 0.06
0.03
0.01
0.57
0.31
0.76
SVM
0.99
0.02 0.01
0.02
0.00
0.13
0.19
0.73
MNB
1.00
0.03 0.01
0.00
0.00
0.44
0.25
0.74
KNN
0.99
0.02 0.01
0.02
0.00
0.13
0.19
0.73
DT
0.92
0.20 0.15
0.12
0.03
0.56
0.33
0.72
LR
0.66
0.28 0.30
0.48
0.04
0.72
0.41
0.58
F-Score
RF
0.86
0.24 0.12
0.06
0.03
0.69
0.33
0.69
SVM
0.84
0.03 0.01
0.03
0.00
0.23
0.19
0.63
MNB
0.85
0.06 0.02
0.01
0.00
0.60
0.26
0.65
KNN
0.84
0.03 0.01
0.03
0.00
0.23
0.19
0.63
DT
0.85
0.24 0.20
0.15
0.04
0.62
0.35
0.69
LR
0.75
0.29 0.28
0.22
0.04
0.70
0.38
0.63
Table 13 Precision, Recall, and F-score for Tamil Offensive Language Identiﬁcation. O-Offensive, T-
Targeted, G-Group.
Classiﬁer Not-O O-untargeted OTI OTG OT-Other Other language Macro Avg Weighted Avg
Support
1765
29
27
23
-
157
2001
2001
Precision
RF
0.95
1.00 1.00
1.00
-
0.95
0.98
0.95
SVM
0.88
0.00 0.00
0.00
-
0.00
0.18
0.78
MNB
0.89
0.00 0.00
0.00
-
0.90
0.36
0.86
KNN
0.95
1.00 1.00
1.00
-
0.90
0.97
0.95
DT
0.95
0.67 0.79
0.65
-
0.82
0.78
0.93
LR
0.97
0.50 0.33
0.30
-
0.52
0.52
0.91
Recall
RF
1.00
0.45 0.37
0.39
-
0.69
0.58
0.95
SVM
1.00
0.00 0.00
0.00
-
0.00
0.20
0.88
MNB
1.00
0.00 0.00
0.00
-
0.11
0.22
0.89
KNN
0.99
0.48 0.44
0.43
-
0.68
0.61
0.95
DT
0.98
0.55 0.41
0.48
-
0.69
0.62
0.94
LR
0.89
0.72 0.56
0.52
-
0.85
0.71
0.88
F-Score
RF
0.97
0.62 0.54
0.56
-
0.80
0.70
0.94
SVM
0.94
0.00 0.00
0.00
-
0.00
0.19
0.83
MNB
0.94
0.00 0.00
0.00
-
0.20
0.23
0.85
KNN
0.97
0.65 0.62
0.61
-
0.78
0.72
0.94
DT
0.97
0.60 0.54
0.55
-
0.75
0.68
0.94
LR
0.93
0.59 0.42
0.38
-
0.64
0.59
0.89
Table 14 Precision, Recall, and F-score for Malayalam Offensive Language Identiﬁcation. O-Offensive,
T-Targeted, G-Group.

--- Page 28 ---

28
Chakravarthi et al
Classiﬁer Not-O O-untargeted OTI OTG OT-Other Other language Macro Avg Weighted Avg
Support
427
33
75
44
14
185
778
778
Precision
RF
0.65
0.00 0.71
0.43
1.00
0.67
0.58
0.63
SVM
0.55
0.00 0.00
0.00
0.00
0.00
0.09
0.30
MNB
0.60
0.00 0.86
0.00
0.00
0.78
0.37
0.60
KNN
0.61
0.00 0.78
0.67
0.00
0.66
0.45
0.60
DT
0.64
0.21 0.57
0.29
0.25
0.56
0.42
0.57
LR
0.77
0.04 0.63
0.25
0.22
0.64
0.43
0.66
Recall
RF
0.89
0.00 0.35
0.08
0.06
0.54
0.32
0.66
SVM
1.00
0.00 0.00
0.00
0.00
0.00
0.17
0.55
MNB
0.98
0.00 0.33
0.00
0.00
0.22
0.26
0.62
KNN
0.93
0.00 0.19
0.09
0.00
0.34
0.26
0.61
DT
0.78
0.09 0.51
0.18
0.07
0.45
0.35
0.60
LR
0.76
0.03 0.59
0.23
0.29
0.71
0.43
0.66
F-Score
RF
0.75
0.00 0.47
0.14
0.11
0.60
0.34
0.61
SVM
0.71
0.00 0.00
0.00
0.00
0.00
0.12
0.39
MNB
0.74
0.00 0.48
0.00
0.00
0.34
0.26
0.54
KNN
0.73
0.00 0.30
0.16
0.00
0.45
0.27
0.55
DT
0.70
0.13 0.54
0.22
0.11
0.50
0.37
0.58
LR
0.77
0.04 0.61
0.24
0.25
0.68
0.43
0.66
Table 15 Precision, Recall, and F-score for Kannada Offensive Language Identiﬁcation. O-Offensive,
T-Targeted, G-Group.
8 Results and Discussion
The results of the experiments with the classiﬁers described above for both sentiment
analysis and offensive language detection are shown in terms of precision, recall,
F1-score and support in Table 10, Table 11, Table 12, Table 13, Table 14, and Table
15.
We used sklearn9 to develop the models. A macro-average will compute the metrics
(precision, recall, F1-score) independently for each class and average them. Thus this
metric treats all classes equally, and it does not take the attribute of class imbalance
into account. A weighted average takes the metrics from each class just like a macro
average, but the contribution of each class to the average is weighted by the number
of examples available for it. The number of comments belonging to different classes
from both the tasks are listed as the support values in respective tables.
For sentiment analysis, the performance of the various classiﬁcation algorithms
range from being inadequate to average on the code-mixed dataset. Logistic regression,
random forest classiﬁers and decision trees were the ones that fared comparatively
better across all sentiment classes. To our surprise, we see that SVM performs poorly,
having a worse heterogeneity than the other methods. The precision, recall and F1-
score are higher for the “Positive" class followed by the “Negative" class. All the other
classes performed very poorly. One of the reasons is the nature of the dataset as the
9 https://scikit-learn.org/stable/

--- Page 29 ---

DravidianCodeMix: Classiﬁcation Dataset for Dravidian Languages Code-Mixed Text
29
classes “Mixed feelings" and “Neutral state" are challenging to label for the annotators
owing to the problematic examples described before.
For offensive language detection, all the classiﬁcation algorithms perform equally
poorly. We see that logistic regression and random forest are the ones that performed
relatively better than the others. The precision, recall and F1-score are higher for
the “Not Offensive" class followed by the “Offensive Targeted Individual" and “OL"
classes. The reasons for the poor performance of other classes are as same as sentiment
analysis. From the tables, we see that the classiﬁcation algorithms have performed
better on the task of sentiment analysis in comparison to that of offensive language
detection. One of the main reasons could be the differences in the distributions of the
classes among the two different tasks.
When it comes to sentiment analysis dataset in Kannada, out of the total of 7,671
sentences 46% and 19% belong to the “Positive" and the “Negative" classes respec-
tively while the other classes share 9%,11% and 15% respectively. This distribution is
better when compared to the Kannada dataset for offensive language detection task
where 56% belong to “Not Offensive", while the other class share a low distribution of
4%,8%,6%,2%,24%. Although the distribution of offensive and non-offensive classes
is skewed in all the languages, we were able to observe that overwhelmingly higher
percentage of comments belonged to non-offensive class in Tamil and Malayalam
datasets than Kannada. 72.4% of comments in Tamil and 88.44% comments in Malay-
alam datasets were non-offensive while in Kannada only 55.79% of the total comments
were non-offensive. This explains why the precision, recall and F-score values of iden-
tifying the non-offensive class are consistently higher for Tamil and Malayalam data
than Kannada. Next to non-offensive class, the number of comments that belonged to
"Not in intended language" class was more than the number of comments belonging
to one of the offensive classes in Kannada and Malayalam datasets. In other words,
it is easier to recognise the "Not offensive" and "Not in intended language" classes
because more comments belong to these two classes than other offensive classes. This
trend is shown by the tables 13, 14, and 15.
Since we collected the posts from movie trailers, we got more positive sentiment
than others as the people who watch trailers are more likely to be interested in movies
and this skews the overall distribution. However, as the code-mixing phenomenon is
not incorporated in the earlier models, this resource could be taken as a starting point
for further research. There is signiﬁcant room for improvement in code-mixed research
with our dataset. In our experiments, we only utilized the machine learning methods,
but more information such as linguistic information or hierarchical meta-embedding
can be utilized.
9 Conclusion
This work introduced code-mixed dataset of the under-resourced Dravidian languages.
This data set comprises more than 60,000 comments annotated for sentiment analysis
and offensive language identiﬁcation. To improve the research in the under-resourced
Dravidian languages, we created an annotation scheme and achieved a high inter-
annotator agreement in terms of Krippendorff 훼from voluntary annotators on contribu-

--- Page 30 ---

30
Chakravarthi et al
tions collected using Google Form. We created baselines with gold standard annotated
data and presented our results for each class in precision, recall, and F-Score. We
expect this resource will enable the researchers to address new and exciting problems
in code-mixed research. In future work, we intend to investigate whether we can apply
these corpora to build corpora for other under-resourced Dravidian languages.
Acknowledgements Authors Bharathi Raja Chakravarthi, Shardul Suryawanshi, and John Phillip McCrae
were supported in part by a research grant from Science Foundation Ireland (SFI) under Grant Number
SFI/12/RC/2289_P2 (Insight_2), co-funded by the European Regional Development Fund and Irish Research
Council grant IRCLA/2017/129 (CARDAMOM-Comparative Deep Models of Language for Minority and
Historical Languages).
References
Agarwal A, Xie B, Vovsha I, Rambow O, Passonneau R (2011) Sentiment analysis of
twitter data. In: Proceedings of the Workshop on Language in Social Media (LSM
2011), Association for Computational Linguistics, Portland, Oregon, pp 30–38,
URL https://www.aclweb.org/anthology/W11-0705
Agrawal R, Chenthil Kumar V, Muralidharan V, Sharma D (2018) No more beating
about the bush : A step towards idiom handling for Indian language NLP. In:
Proceedings of the Eleventh International Conference on Language Resources and
Evaluation (LREC-2018), European Languages Resources Association (ELRA),
Miyazaki, Japan, URL https://www.aclweb.org/anthology/L18-1048
Bali K, Sharma J, Choudhury M, Vyas Y (2014) “I am borrowing ya mixing ?”
an analysis of English-Hindi code mixing in Facebook. In: Proceedings of the
First Workshop on Computational Approaches to Code Switching, Association for
Computational Linguistics, Doha, Qatar, pp 116–126, DOI 10.3115/v1/W14-3914,
URL https://www.aclweb.org/anthology/W14-3914
Barman U, Das A, Wagner J, Foster J (2014) Code mixing: A challenge for language
identiﬁcation in the language of social media. In: Proceedings of the First Workshop
on Computational Approaches to Code Switching, Association for Computational
Linguistics, Doha, Qatar, pp 13–23, DOI 10.3115/v1/W14-3902, URL https:
//www.aclweb.org/anthology/W14-3902
Breiman L (2001) Random forests. Machine learning 45(1):5–32
Caruana R, Niculescu-Mizil A (2006) An empirical comparison of supervised learn-
ing algorithms. In: Proceedings of the 23rd international conference on Machine
learning, pp 161–168
Chakravarthi BR (2020) HopeEDI: A multilingual hope speech detection dataset
for equality, diversity, and inclusion. In: Proceedings of the Third Workshop on
Computational Modeling of People’s Opinions, Personality, and Emotion’s in Social
Media, Association for Computational Linguistics, Barcelona, Spain (Online), pp
41–53, URL https://www.aclweb.org/anthology/2020.peoples-1.5
Chakravarthi BR, Muralidaran V (2021) Findings of the shared task on hope speech
detection for equality, diversity, and inclusion. In: Proceedings of the First Workshop
on Language Technology for Equality, Diversity and Inclusion, Association for

--- Page 31 ---

DravidianCodeMix: Classiﬁcation Dataset for Dravidian Languages Code-Mixed Text
31
Computational Linguistics, Kyiv, pp 61–72, URL https://www.aclweb.org/
anthology/2021.ltedi-1.8
Chakravarthi BR, Anand Kumar M, McCrae JP, Premjith B, Soman K, Mandl T
(2020a) Overview of the track on HASOC-offensive Language Identiﬁcation-
DravidianCodeMix. In: Working Notes of the Forum for Information Retrieval
Evaluation (FIRE 2020). CEUR Workshop Proceedings, CEUR-WS. org
Chakravarthi BR, Jose N, Suryawanshi S, Sherly E, McCrae JP (2020b) A sentiment
analysis dataset for code-mixed Malayalam-English. In: Proceedings of the 1st
Joint Workshop of SLTU (Spoken Language Technologies for Under-resourced
languages) and CCURL (Collaboration and Computing for Under-Resourced Lan-
guages) (SLTU-CCURL 2020), European Language Resources Association (ELRA),
Marseille, France
Chakravarthi BR, Muralidaran V, Priyadharshini R, McCrae JP (2020c) Corpus cre-
ation for sentiment analysis in code-mixed Tamil-English text. In: Proceedings of the
1st Joint Workshop of SLTU (Spoken Language Technologies for Under-resourced
languages) and CCURL (Collaboration and Computing for Under-Resourced Lan-
guages) (SLTU-CCURL 2020), European Language Resources Association (ELRA),
Marseille, France
Chakravarthi BR, Priyadharshini R, Muralidaran V, Suryawanshi S, Jose N, Sherly
E, McCrae JP (2020d) Overview of the Track on Sentiment Analysis for Dravid-
ian Languages in Code-Mixed Text. In: Forum for Information Retrieval Evalu-
ation, Association for Computing Machinery, New York, NY, USA, FIRE 2020,
p 21–24, DOI 10.1145/3441501.3441515, URL https://doi.org/10.1145/
3441501.3441515
Chakravarthi BR, Priyadharshini R, Jose N, Kumar M A, Mandl T, Kumaresan PK,
Ponnusamy R, R L H, McCrae JP, Sherly E (2021) Findings of the shared task on
offensive language identiﬁcation in Tamil, Malayalam, and Kannada. In: Proceed-
ings of the First Workshop on Speech and Language Technologies for Dravidian
Languages, Association for Computational Linguistics, Kyiv, pp 133–145, URL
https://www.aclweb.org/anthology/2021.dravidianlangtech-1.17
Chanda A, Das D, Mazumdar C (2016) Unraveling the English-Bengali code-mixing
phenomenon. In: Proceedings of the Second Workshop on Computational Ap-
proaches to Code Switching, Association for Computational Linguistics, Austin,
Texas, pp 80–89, DOI 10.18653/v1/W16-5810, URL https://www.aclweb.org/
anthology/W16-5810
Cieliebak M, Deriu JM, Egger D, Uzdilli F (2017) A twitter corpus and benchmark
resources for German sentiment analysis. In: Proceedings of the Fifth International
Workshop on Natural Language Processing for Social Media, Association for Com-
putational Linguistics, Valencia, Spain, pp 45–51, DOI 10.18653/v1/W17-1106,
URL https://www.aclweb.org/anthology/W17-1106
Clarke I, Grieve J (2017) Dimensions of abusive language on twitter. In: Proceedings
of the First Workshop on Abusive Language Online, Association for Computational
Linguistics, Vancouver, BC, Canada, pp 1–10, DOI 10.18653/v1/W17-3001, URL
https://www.aclweb.org/anthology/W17-3001
Ekbal A, Bandyopadhyay S (2008) Bengali named entity recognition using support
vector machine. NER for South and South East Asian Languages p 51

--- Page 32 ---

32
Chakravarthi et al
Genkin A, Lewis D, Madigan D (2007) Large-Scale Bayesian Logistic Regression for
Text Categorization. Technometrics 49, DOI 10.1198/004017007000000245
de Gispert A, Iglesias G, Byrne B (2015) Fast and accurate preordering for SMT using
neural networks. In: Proceedings of the 2015 Conference of the North American
Chapter of the Association for Computational Linguistics: Human Language Tech-
nologies, Association for Computational Linguistics, Denver, Colorado, pp 1012–
1017, DOI 10.3115/v1/N15-1105, URL https://www.aclweb.org/anthology/
N15-1105
Gitari ND, Zuping Z, Damien H, Long J (2015) A lexicon-based approach for hate
speech detection. International Journal of Multimedia and Ubiquitous Engineering
10(4):215–230
Hu M, Liu B (2004) Mining and summarizing customer reviews. In: Proceedings
of the Tenth ACM SIGKDD International Conference on Knowledge Discovery
and Data Mining, Association for Computing Machinery, New York, NY, USA,
KDD ’04, p 168–177, DOI 10.1145/1014052.1014073, URL https://doi.org/
10.1145/1014052.1014073
Jiang Q, Chen L, Xu R, Ao X, Yang M (2019) A challenge dataset and effective
models for aspect-based sentiment analysis. In: Proceedings of the 2019 Conference
on Empirical Methods in Natural Language Processing and the 9th International
Joint Conference on Natural Language Processing (EMNLP-IJCNLP), Association
for Computational Linguistics, Hong Kong, China, pp 6279–6284, DOI 10.18653/
v1/D19-1654, URL https://www.aclweb.org/anthology/D19-1654
Jin S, Pedersen T (2018) Duluth UROP at SemEval-2018 task 2: Multilingual emoji
prediction with ensemble learning and oversampling. In: Proceedings of The 12th
International Workshop on Semantic Evaluation, Association for Computational
Linguistics, New Orleans, Louisiana, pp 482–485, DOI 10.18653/v1/S18-1077,
URL https://www.aclweb.org/anthology/S18-1077
Jose N, Chakravarthi BR, Suryawanshi S, Sherly E, McCrae JP (2020) A survey of
current datasets for code-switching research. In: 2020 6th International Conference
on Advanced Computing & Communication Systems (ICACCS)
Kouloumpis E, Wilson T, Moore J (2011) Twitter Sentiment Analysis: The Good the
Bad and the OMG! In: Fifth International AAAI conference on weblogs and social
media, Citeseer
Krippendorff K (1970) Estimating the reliability, systematic error and random
error of interval data. Educational and Psychological Measurement 30(1):61–
70, DOI 10.1177/001316447003000105, URL https://doi.org/10.1177/
001316447003000105, https://doi.org/10.1177/001316447003000105
Krishna PV, Misra S, Joshi D, Obaidat MS (2013) Learning automata based sentiment
analysis for recommender system on cloud. In: 2013 International Conference on
Computer, Information and Telecommunication Systems (CITS), IEEE, pp 1–5
Krishnamurti B (2003) The Dravidian languages. Cambridge University Press
Kumar BS, Thenmozhi D, Kayalvizhi S (2020) Tamil paraphrase detection using
encoder-decoder neural networks. In: International Conference on Computational
Intelligence in Data Science, Springer, pp 30–42
Kumar R, Ojha AK, Malmasi S, Zampieri M (2018) Benchmarking aggression iden-
tiﬁcation in social media. In: Proceedings of the First Workshop on Trolling, Ag-

--- Page 33 ---

DravidianCodeMix: Classiﬁcation Dataset for Dravidian Languages Code-Mixed Text
33
gression and Cyberbullying (TRAC-2018), Association for Computational Linguis-
tics, Santa Fe, New Mexico, USA, pp 1–11, URL https://www.aclweb.org/
anthology/W18-4401
Mæhlum P, Barnes J, Øvrelid L, Velldal E (2019) Annotating evaluative sentences
for sentiment analysis: a dataset for Norwegian. In: Proceedings of the 22nd
Nordic Conference on Computational Linguistics, Linköping University Elec-
tronic Press, Turku, Finland, pp 121–130, URL https://www.aclweb.org/
anthology/W19-6113
Mandl T, Modha S, Kumar M A, Chakravarthi BR (2020) Overview of the HASOC
Track at FIRE 2020: Hate Speech and Offensive Language Identiﬁcation in Tamil,
Malayalam, Hindi, English and German. In: Forum for Information Retrieval Eval-
uation, Association for Computing Machinery, New York, NY, USA, FIRE 2020,
p 29–32, DOI 10.1145/3441501.3441517, URL https://doi.org/10.1145/
3441501.3441517
Musto C, de Gemmis M, Semeraro G, Lops P (2017) A multi-criteria recommender
system exploiting aspect-based sentiment analysis of users’ reviews. In: Proceedings
of the eleventh ACM conference on recommender systems, pp 321–325
Ng AY, Jordan MI (2002) On discriminative vs. generative classiﬁers: A comparison of
logistic regression and naive bayes. In: Advances in neural information processing
systems, pp 841–848
Nongmeikapam K, Kumar W, Singh MP (2017) Exploring an efﬁcient handwritten
Manipuri meetei-mayek character recognition using gradient feature extractor and
cosine distance based multiclass k-nearest neighbor classiﬁer. In: Proceedings of the
14th International Conference on Natural Language Processing (ICON-2017), NLP
Association of India, Kolkata, India, pp 328–337, URL https://www.aclweb.
org/anthology/W17-7541
Pang B, Lee L (2004) A sentimental education: Sentiment analysis using subjectivity
summarization based on minimum cuts. In: Proceedings of the 42nd Annual Meeting
of the Association for Computational Linguistics (ACL-04), Barcelona, Spain,
pp 271–278, DOI 10.3115/1218955.1218990, URL https://www.aclweb.org/
anthology/P04-1035
Park H (2013) An introduction to logistic regression: from basic concepts to interpre-
tation with particular attention to nursing domain. Journal of Korean Academy of
Nursing 43(2):154–164
Patwa P, Aguilar G, Kar S, Pandey S, PYKL S, Gambäck B, Chakraborty T, Solorio T,
Das A (2020) Semeval-2020 task 9: Overview of sentiment analysis of code-mixed
tweets. In: Proceedings of the 14th International Workshop on Semantic Evaluation
(SemEval-2020), Association for Computational Linguistics, Barcelona, Spain
Pratapa A, Bhat G, Choudhury M, Sitaram S, Dandapat S, Bali K (2018) Language
modeling for code-mixing: The role of linguistic theory based synthetic data. In:
Proceedings of the 56th Annual Meeting of the Association for Computational
Linguistics (Volume 1: Long Papers), Association for Computational Linguistics,
Melbourne, Australia, pp 1543–1553, DOI 10.18653/v1/P18-1143, URL https:
//www.aclweb.org/anthology/P18-1143
Rani P, Suryawanshi S, Goswami K, Chakravarthi BR, Fransen T, McCrae JP (2020)
A comparative study of different state-of-the-art hate speech detection methods

--- Page 34 ---

34
Chakravarthi et al
for Hindi-English code-mixed data. In: Proceedings of the Second Workshop on
Trolling, Aggression and Cyberbullying, European Language Resources Association
(ELRA), Marseille, France
Ranjan P, Raja B, Priyadharshini R, Balabantaray RC (2016) A comparative study on
code-mixed data of Indian social media vs formal text. In: 2016 2nd International
Conference on Contemporary Computing and Informatics (IC3I), pp 608–611,
DOI 10.1109/IC3I.2016.7918035
Rogers A, Romanov A, Rumshisky A, Volkova S, Gronas M, Gribov A (2018) RuSen-
timent: An enriched sentiment analysis dataset for social media in Russian. In:
Proceedings of the 27th International Conference on Computational Linguistics, As-
sociation for Computational Linguistics, Santa Fe, New Mexico, USA, pp 755–763,
URL https://www.aclweb.org/anthology/C18-1064
Sakuntharaj R, Mahesan S (2016) A novel hybrid approach to detect and correct
spelling in Tamil text. In: 2016 IEEE International Conference on Information and
Automation for Sustainability (ICIAfS), IEEE, pp 1–6
Sakuntharaj R, Mahesan S (2017) Use of a novel hash-table for speeding-up sug-
gestions for misspelt Tamil words. In: 2017 IEEE International Conference on
Industrial and Information Systems (ICIIS), IEEE, pp 1–5
Sakuntharaj R, Mahesan S (2018a) Detecting and correcting real-word errors in Tamil
sentences. Ruhuna Journal of Science 9(2)
Sakuntharaj R, Mahesan S (2018b) A reﬁned pos tag sequence ﬁnder for Tamil
sentences. In: 2018 IEEE International Conference on Information and Automation
for Sustainability (ICIAfS), IEEE, pp 1–6
Severyn A, Moschitti A, Uryupina O, Plank B, Filippova K (2014) Opinion mining
on YouTube. In: Proceedings of the 52nd Annual Meeting of the Association for
Computational Linguistics (Volume 1: Long Papers), Association for Computational
Linguistics, Baltimore, Maryland, pp 1252–1261, DOI 10.3115/v1/P14-1118, URL
https://www.aclweb.org/anthology/P14-1118
Shah K, Patel H, Sanghvi D, Shah M (2020) A comparative analysis of logistic
regression, random forest and KNN models for the text classiﬁcation. Augmented
Human Research 5(1):1–16
Shalini K, Ganesh HB, Kumar MA, Soman KP (2018) Sentiment analysis for code-
mixed Indian social media text with distributed representation. In: 2018 Interna-
tional Conference on Advances in Computing, Communications and Informatics
(ICACCI), pp 1126–1131
Sowmya Lakshmi BS, Shambhavi BR (2017) An Automatic Language Identiﬁcation
System for Code-Mixed English-Kannada Social Media Text. In: 2017 2nd Inter-
national Conference on Computational Systems and Information Technology for
Sustainable Solution (CSITSS), pp 1–5, DOI 10.1109/CSITSS.2017.8447784
Sridhar SN (1978) On the functions of code-mixing in kannada. International Journal
of the Sociology of Language 1978(16):109–118
Thamburaj KP, Rengganathan V (2015) A critical study of spm tamil literature exam
paper. Asian Journal of Assessment in Teaching and Learning 5:13–24
Thamburaj KP, Arumugum L, Samuel SJ (2015) An analysis on keyboard writing skills
in online learning. In: 2015 International Symposium on Technology Management
and Emerging Technologies (ISTMET), IEEE, pp 373–377

--- Page 35 ---

DravidianCodeMix: Classiﬁcation Dataset for Dravidian Languages Code-Mixed Text
35
Thavareesan S, Mahesan S (2019) Sentiment Analysis in Tamil Texts: A Study
on Machine Learning Techniques and Feature Representation. In: 2019 14th
Conference on Industrial and Information Systems (ICIIS), pp 320–325, DOI
10.1109/ICIIS47346.2019.9063341
Thavareesan S, Mahesan S (2020a) Sentiment Lexicon Expansion using Word2vec and
fastText for Sentiment Prediction in Tamil texts. In: 2020 Moratuwa Engineering
Research Conference (MERCon), pp 272–276, DOI 10.1109/MERCon50084.2020.
9185369
Thavareesan S, Mahesan S (2020b) Word embedding-based Part of Speech tagging
in Tamil texts. In: 2020 IEEE 15th International Conference on Industrial and
Information Systems (ICIIS), pp 478–482, DOI 10.1109/ICIIS51140.2020.9342640
Thenmozhi D, Aravindan C (2018) Ontology-based Tamil–English cross-lingual
information retrieval system. S¯adhan¯a 43(10):1–14
Thottingal S (2019) Finite state transducer based morphology analysis for Malayalam
language. In: Proceedings of the 2nd Workshop on Technologies for MT of Low Re-
source Languages, European Association for Machine Translation, Dublin, Ireland,
pp 1–5, URL https://www.aclweb.org/anthology/W19-6801
Tian Y, Galery T, Dulcinati G, Molimpakis E, Sun C (2017) Facebook sentiment:
Reactions and emojis. In: Proceedings of the Fifth International Workshop on
Natural Language Processing for Social Media, Association for Computational
Linguistics, Valencia, Spain, pp 11–16, DOI 10.18653/v1/W17-1102, URL https:
//www.aclweb.org/anthology/W17-1102
Vikram TN, Urs SR (2007) Development of Prototype Morphological Analyzer for he
South Indian Language of Kannada, Springer Berlin Heidelberg, Berlin, Heidelberg,
pp 109–116
Vyas Y, Gella S, Sharma J, Bali K, Choudhury M (2014) POS tagging of English-
Hindi code-mixed social media content. In: Proceedings of the 2014 Conference
on Empirical Methods in Natural Language Processing (EMNLP), Association for
Computational Linguistics, Doha, Qatar, pp 974–979, DOI 10.3115/v1/D14-1105,
URL https://www.aclweb.org/anthology/D14-1105
Wiebe J, Wilson T, Cardie C (2005) Annotating expressions of opinions and emotions
in language. Language Resources and Evaluation 39(2):165–210, DOI 10.1007/
s10579-005-7880-9, URL https://doi.org/10.1007/s10579-005-7880-9
Wilson T, Wiebe J, Hoffmann P (2005) Recognizing contextual polarity in phrase-level
sentiment analysis. In: Proceedings of Human Language Technology Conference
and Conference on Empirical Methods in Natural Language Processing, Association
for Computational Linguistics, Vancouver, British Columbia, Canada, pp 347–354,
URL https://www.aclweb.org/anthology/H05-1044
Winata GI, Lin Z, Fung P (2019) Learning multilingual meta-embeddings for code-
switching named entity recognition. In: Proceedings of the 4th Workshop on
Representation Learning for NLP (RepL4NLP-2019), Association for Compu-
tational Linguistics, Florence, Italy, pp 181–186, DOI 10.18653/v1/W19-4320,
URL https://www.aclweb.org/anthology/W19-4320
Zampieri M, Malmasi S, Nakov P, Rosenthal S, Farra N, Kumar R (2019) Pre-
dicting the type and target of offensive posts in social media. In: Proceedings
of the 2019 Conference of the North American Chapter of the Association for

--- Page 36 ---

36
Chakravarthi et al
Computational Linguistics: Human Language Technologies, Volume 1 (Long and
Short Papers), Association for Computational Linguistics, Minneapolis, Minnesota,
pp 1415–1420, DOI 10.18653/v1/N19-1144, URL https://www.aclweb.org/
anthology/N19-1144
Zampieri M, Nakov P, Rosenthal S, Atanasova P, Karadzhov G, Mubarak H, Derczyn-
ski L, Pitenis Z, Çöltekin c (2020) SemEval-2020 Task 12: Multilingual Offensive
Language Identiﬁcation in Social Media (OffensEval 2020). In: Proceedings of
SemEval

```
