---
title: "2024-Liebeskind-From Linguistics to Practice a Case Study of Offensive Language - PDF Extract"
source_pdf: "2024-Liebeskind-From Linguistics to Practice a Case Study of Offensive Language.pdf"
pages: 8
extracted_at: "2026-02-13T10:43:51.832724"
---

# PDF Extract: 2024-Liebeskind-From Linguistics to Practice a Case Study of Offensive Language

**Source PDF:** 2024-Liebeskind-From Linguistics to Practice a Case Study of Offensive Language.pdf
**Total Pages:** 8

---

## Content

```
--- Page 1 ---

Proceedings of the The 8th Workshop on Online Abuse and Harms (WOAH), pages 110–117
June 20, 2024 ©2024 Association for Computational Linguistics
From Linguistics to Practice: a Case Study of Offensive Language
Taxonomy in Hebrew
Chaya Liebeskind
Department of Computer Science
Jerusalem College of Technology
Jerusalem, Israel
liebchaya@gmail.com
Natalia Vanetik and Marina Litvak
Department of Software Engineering
Shamoon College of Engineering
Beer-Sheva
{natalyav,marinal}@sce.ac.il
Abstract
The perception of offensive language varies
based on cultural, social, and individual per-
spectives.
With the spread of social media,
there has been an increase in offensive con-
tent online, necessitating advanced solutions
for its identiﬁcation and moderation. This pa-
per addresses the practical application of an of-
fensive language taxonomy, speciﬁcally target-
ing Hebrew social media texts. By introduc-
ing a newly annotated dataset, modeled after
the taxonomy of explicit offensive language
of (Lewandowska-Tomaszczyk et al., 2023),
we provide a comprehensive examination of
various degrees and aspects of offensive lan-
guage. Our ﬁndings indicate the complexities
involved in the classiﬁcation of such content.
We also outline the implications of relying on
ﬁxed taxonomies for Hebrew.
1
Introduction
The deﬁnition of offensive language can vary de-
pending on cultural, social, and personal view-
points.
In a general sense,
offensive lan-
guage encompasses any form of communica-
tion that may upset or discomfort individu-
als or groups (Haugh and Sinkeviciute, 2019;
Lewandowska-Tomaszczyk, 2023).
It can be
broadly categorized into explicit forms (Kogila-
vani et al., 2021; Lewandowska-Tomaszczyk,
2023), including insults and hate speech, and im-
plicit forms which use subtle insinuations or coded
language to convey bias. Social media platforms
have become signiﬁcant sources of offensive lan-
guage, with surveys revealing a rise in hate speech
instances (Alsagheer et al., 2022; Costello and
Hawdon, 2020). Numerous countries have laws
against hate speech and false information. Failure
to properly regulate such content can result in le-
gal consequences and harm to a platform’s reputa-
tion. While content ﬁlters on platforms can help
reduce offensive language, their effectiveness is
diminishing due to the growth of user-generated
content. Consequently, Natural Language Process-
ing (NLP) techniques are gaining importance in
identifying offensive language. However, detect-
ing offensive language in low-resource languages,
like Hebrew, remains a challenge (Zampieri et al.,
2019b) due to the lack of available resources.
The taxonomy of offensive language is crucial
as it establishes a structured framework for vari-
ous inappropriate content, assisting automated sys-
tems in moderating and responding to such con-
tent.
This classiﬁcation creates a foundational
structure that not only streamlines the intricate
landscape of online communication but also acts
as an instrument to enhance the safety and func-
tionality of digital platforms. The practicality of
offensive language taxonomies often raises con-
cerns, especially in the ever-evolving digital land-
scape.
Creating a comprehensive taxonomy is
challenging given the vast and nuanced spectrum
of offensive content. Relying solely on a static tax-
onomy may not capture the dynamic nature of lan-
guage, especially as slang, idioms, and colloqui-
alisms evolve. There’s also a risk of misinterpreta-
tion or misclassiﬁcation, which can inadvertently
lead to stiﬂing genuine discussions or failing to
catch genuinely harmful content.
This study distinguishes itself from prior stud-
ies on identifying offensive texts by deviating from
the approach of just focusing on a certain form of
offensive language or relying on an intuitive def-
inition that encompasses various kinds of offen-
sive language, without being grounded in a system-
atic linguistic taxonomy. In this paper, we study
the practical implications of applying an offensive
language taxonomy to the collection and analysis
of Hebrew social media texts. For this purpose,
we present here a new annotated dataset follow-
ing a simpliﬁed taxonomy of explicit offensive lan-
guage introduced in (Lewandowska-Tomaszczyk
et al., 2023). The data represents all the levels
110

--- Page 2 ---

of this taxonomy, which allowed us to examine
the practical consequences of collecting and ana-
lyzing offensive texts. We were able to determine
what types and aspects of offensive language pose
a signiﬁcant challenge for binary and multi-class
classiﬁcation of offensive language.
This paper is organized as follows. Section 2
covers the related work.
Section 3.2 describes
the collection and annotation of the offensive lan-
guage dataset in Hebrew, and Section 3.3 reports
on the dataset analysis.
Finally, Section 4 con-
cludes our work and describes potential future
tasks.
2
Related Work
Multiple works on automated offensive language
detection exist,
including early unsupervised
lexicon-based approaches (Tulkens et al., 2016),
traditional supervised approaches (Davidson et al.,
2017), and recent approaches based on deep neu-
ral networks (Zampieri et al., 2019b) and trans-
former models (Liu et al., 2019; Ranasinghe et al.,
2019). However, the clear majority of the offen-
sive detection studies deal with English. Recently,
many researchers started to develop multilingual
methodologies and annotated corpora in multiple
languages. For example, such languages as Ara-
bic (Mohaouchane et al., 2019), Dutch (Tulkens
et al., 2016), French (Chiril et al., 2019), Turk-
ish (Çöltekin, 2020), Danish (Sigurbergsson and
Derczynski, 2019), Greek (Pitenis et al., 2020),
Italian (Poletto et al., 2017), Portuguese (Fortuna
et al., 2019), Slovene (Fišer et al., 2017), and Dra-
vidian (Yasaswini et al., 2021) were explored for
the task of offensive content identiﬁcation.
Despite the great international effort, many low-
resource languages got much less attention than
others. For example, only a few works proposed
solutions for Hebrew: a Hebrew corpus of user
comments annotated for abusive language was in-
troduced in (Liebeskind and Liebeskind, 2018);
an annotated Facebook comments dataset and a
system for offensive text detection was suggested
in (Litvak et al., 2021), and a union of these
two datasets and together with monolingual, cross-
lingual, and multilingual experiments for the task
of offensive language detection was presented in
(Litvak et al., 2022).
Hebrew and Arabic are
both members of the same family of languages
known as the Semitic languages, and some authors
made use of the wealth of resources available in
Arabic.
For example, the most recent work in-
troduced a new offensive language corpus in He-
brew containing 15,881 Twitter labeled by Arabic-
Hebrew bilingual speakers into one or more of
the ﬁve available classes, namely abuse, hate, vi-
olence, pornography, or non-offensive (Hamad
et al., 2023). Fine-tuning of pre-trained Hebrew
LLMs showed that the proposed dataset is beneﬁ-
cial for the detection of offensive language in He-
brew (Litvak et al., 2022).
The ﬁrst offensive language taxonomy suitable
for social media content appeared in (Zampieri
et al., 2019a,b). This three-level hierarchy for of-
fensive language classiﬁcation was created to of-
fer a methodical technique to distinguish between
various forms and degrees of offensive language.
In (Lewandowska-Tomaszczyk et al., 2022), the
combined schema for explicit and implicit of-
fensive language was tested on English datasets,
and difﬁculties with agreement among annota-
tors about the distinction of particular categories
emerged. Based on linguistic ideas like Grice’s
implicitness categories, the work (Lewandowska-
Tomaszczyk, 2023) established a holistic method
that targets both explicit and implied types of abu-
sive language. However, to this day, no applica-
tions or evaluation of similar taxonomy in Hebrew
exists.
3
Hebrew Offensive Language
Taxonomy and Dataset
3.1
Taxonomy
We derive the aspects of offensive language
for Hebrew from the taxonomy proposed by
(Lewandowska-Tomaszczyk et al., 2023) that in its
turn extends a taxonomy proposed in (Zampieri
et al., 2019a,b).
We have translated this taxon-
omy to Hebrew and focused on the ﬁrst six lay-
ers that represent explicit offensive language. In
this taxonomy (depicted in Figure 1), after decid-
ing of whether or not the text is offensive, one has
to determine the presence or absence of the tar-
get of an offense, then decide on the type of tar-
get, and rule whether or not the expression is vul-
gar. The next step is to state what is the severity
of the offense (discrediting, insulting, hate speech,
threat) and what are the offense aspects (racism,
homophobia, xenophobia, religious profanity, sex-
ism, ageism, ableism, ideologism, classism, unde-
termined).
111

--- Page 3 ---

Figure 1: Explicit offensive language taxonomy
3.2
Dataset Collection and Annotation
As a starting point for data collection, we created a
list of offensive terms in Hebrew using the method
of (Liebeskind and Liebeskind, 2018), as follows.
Initially, 67 offensive terms were chosen, and then
they were supplemented using a statistical mea-
sure of word co-occurrence. We obtained the 100
most similar words for each offending term in
the ﬁrst list using the Dice coefﬁcient (Smadja
et al., 1996) and a sizable unannotated corpus of
Facebook comments (Liebeskind and Liebeskind,
2018), supposing that words that often occur to-
gether are thematically relevant (Schütze and Ped-
ersen, 1997).
Then, from these candidate lists,
683 offensive terms were manually chosen and as-
signed to one or more offensive aspects. Note that
we could not ﬁnd any example of xenophobia that
is not racist, so this aspect is excluded from the
analysis. We adopted a classiﬁcation method that
requires only a context-based connection between
the offensive term and the aspect. For instance,
the word !( עלוקהleech) has been categorized as
profanity because it is frequently directed at a par-
ticular religious group of the population. Or, for
instance, the word !( גנבthief) has been labeled as
classism because criminals frequently belong to a
particular social class. This strategy aims to ob-
tain a diverse dataset that cannot be separated by
the search terms alone, necessitating the annota-
tion and analysis presented in this work. Finally,
we extracted offensive tweets from Twitter using
the offensive terms. In this manner, we ensured
that our data encompasses all aspects of offensive
language, not just the most prevalent types. Conse-
quently, we were able to evaluate the applicability
of offensive taxonomy for dataset creation.
To demonstrate the efﬁcacy of our extraction
method, we trained the 100-dimensional fastText
word embeddings (Bojanowski et al., 2017) on
the constructed dataset that is suitable for morpho-
logically rich languages, such as Hebrew. Using
t-Distributed Stochastic Neighbor Embedding (t-
SNE) (Belkina et al., 2019), we retrieved 30 neigh-
boring words for each aspect and visualized the
results. We prefer the t-SNE method over the Prin-
cipal Component Analysis (PCA) (Shlens, 2014)
method because it captures nonlinear structures
and clusters in high-dimensional data more effec-
tively. Figure 2 shows that there is a clear separa-
tion between the neighboring words that occur in
the different offensive aspects, indicating that they
are readily identiﬁed.
However, owing to their
close association in reality, certain categories virtu-
ally overlap, such as racial and ideological (mak-
ing racism an ideology) or ableism and classism
(identifying a person in a different socioeconomic
position as handicapped).
Figure 2: t-SNE-based visualization of the 30 neighbor-
ing fastText vectors
We used the INCEpTION platform (Klie et al.,
2018) to produce annotations. The data was di-
vided into 9 ﬁles, one ﬁle per offensive aspect,
with 50 comments in every ﬁle, making it 450
texts in total.
Our annotators were unaware of
this division. The texts were given to two native
Hebrew speakers who were requested to annotate
them independently.
Given that the texts came
from social networks frequented by young individ-
uals who use slang and modern language, we se-
lected annotators between the ages of 20 and 30.
The annotators were ﬁrst asked to decide whether
or not a text is offensive and then to proceed ac-
112

--- Page 4 ---

cording to taxonomy levels of Section 3.1; we
have computed Cohen’s Kappa agreement coefﬁ-
cient (Cohen, 1960) for every level/parameter sep-
arately. First, the annotators determined whether
or not the target of the offense is present in the
text (agreement 0.49), then they identiﬁed the tar-
get’s type (agreement 0.84) and the severity of the
offense (agreement 0.73 for hate speech and insult,
0.66 for discrediting, and 0.97 for threat), and they
determined whether or not the expression is vulgar
(agreement 0.63). As the last step, the annotators
were instructed to list (in alphabetical order) each
aspect of explicit offensive language that applies
to the text, achieving an agreement of 0.68. Cal-
culating the inter-annotator agreement not only al-
lows us to evaluate the clarity of the annotation
guidelines but also the inherent difﬁculty of the
classiﬁcation and how well humans comprehend
the task. In order to create the ﬁnal dataset, we re-
solved instances where the labels did not align by
involving a third annotator for disambiguation.
3.3
Dataset Analysis
Table 1 describes the three tokens with the high-
est tf-idf values for every ﬁle. We can see that
some words appear across ﬁles, for example, the
word !K( לgo), which is not a vulgar word but may
be considered impolite if it is used as “get out”
in the sentence. The categories where words are
related (although these words are not necessarily
vulgar or insults) are “homophobia” and “ideolo-
gism” where, for example, the last name of a for-
mer prime minister is mentioned (Bennet).
Table 2 shows the three words with the highest
normalized count for every ﬁle. Again, we see that
words appear across ﬁles.
To tokenize the texts, we cleaned the data from
punctuation, numbers, and non-Hebrew charac-
ters, and applied the AlephBERT tokenizer (Seker
et al., 2021).
We see the words that have high tf-idf values or
high unigram count are not necessarily the words
related to their respective offensive aspect, ex-
cept for “sexism" and “profanity" ﬁles. Moreover,
these words often represent the most prominent to-
kens in more than one ﬁle. For instance, an un-
related offensive word such as !N( עברייa criminal)
is among the most common words in the ﬁle “sex-
ism". Therefore, straightforward word-based clas-
siﬁcation does not seem very helpful in this case.
To evaluate the creation process’ validity and
to better comprehend the practical applicability of
the annotated dataset we extracted the data for spe-
ciﬁc offensive language categorization tasks using
the various taxonomy levels.
Table 4 reports the results of the binary classi-
ﬁcation for every offensive category with at least
10 sentences. We treat the category sentences as
positive samples, and the rest of the sentences as
negative samples. This table also reports the ﬁ-
nal dataset statistics, i.e., the number of sentences
in the dataset that were annotated as containing
a speciﬁc offensive aspect.
Note that there are
sentences that were not annotated as offensive at
all, and therefore the total number of sentences
is smaller than 450.
We have applied eXtreme
Gradient Boost (XGB) (Chen et al., 2015) (we
have also applied Random Forest (RF) (Pal, 2005)
and Logistic Regression (LR) (Wright, 1995), but
XGB provided slightly better results). to texts rep-
resented as BERT sentence embeddings encoded
with AlephBERT (Seker et al., 2021). We split
the data into training and test sets (80%/20%) and
classiﬁed offensive types/aspects with at least 10
sentences. For example, in offensive aspects, this
pruning left us with 7 categories out of 10. We
see that upper taxonomy levels such as target pres-
ence accuracy exceed the majority values signif-
icantly; however, lower taxonomy levels pose a
more serious challenge - vulgarity and severity of
the offense are especially difﬁcult. On the lowest
taxonomy level for most of the offensive aspects,
the accuracy does not exceed the majority values,
except for the “other” aspect which is the largest
class. However, “homophobia" has signiﬁcantly
higher precision than other classes.
As baselines we applied two ﬁne-tuned trans-
formers – a multilingual BERT model or (Hug-
gingFace, 2024) which we denote by mlbert, and
the Hebrew BERT model of (Chriqui and Yahav,
2021) denoted by hebert, to the task of binary clas-
siﬁcation for different levels of our taxonomy. We
have ﬁne-tuned every model for 10 epochs with
batch size 16, Adam optimizer, and standard learn-
ing rate of 0.00002. All texts were padded to the
maximal length, and the attention mask was set to
ignore the padded tokens. Comparative results of
these transformer models appear in Table 5. We
can see that the hebert model has an obvious ad-
vantage over the mlbert for all the categories, but
both models perform worse that traditional classi-
ﬁers.
In Table 3 we report the results of the multi-
class classiﬁcation of offensive parameters per tax-
113

--- Page 5 ---

ﬁle
words with top tf-idf
transcription
translation
racism
!פאשיסט! , נבלה! ,נבלותphashist, navela, navelot
fascist, scavenger, scavengers
homophobia
!לסביות! , קוקסינליM! ,התחתlesbiot, koksinelim, hatachat
lesbians, shemales , the a**
sexism
!לK! ,בוגדיM! ,תעופיlekh, bogdim, ta’oﬁ
go , traitors, get out
profanity
!Kהזה! ,שלו! ,לhaze, she’lo, lekh
this , that is not, go
ageism
!הולני! , הזויה! ,דיcholani, hazuya, day
sick, delusional, enough
ableism
!קרימינל! ,קשקשN! ,זבלkriminal, kashkashan, zevel
criminal, rascal, garbage
classism
!Nעלובה! , מסית! ,עבריייaluva, matsit, avaryan
wretched, agitator, offender
ideologism
!בנט! ,בשלטוN! ,מושהטBennett, b’shelton, moshachat
Bennet, in power, corrupt
other
!לK!, כבר! ,פהpach, kvar, lekh
trash can , already , go
all ﬁles
!Kשלא! ,עלובה! ,לlekh, aluva, she’lo
go, wretched, that is not
Table 1: Tokens with highest tf-idf values per ﬁle.
ﬁle
unigrams
transcription
translation
racism
!כלוM! ,הוZ! ,עכשיוklum, utz, akhshav
now, except, nothing
homophobia
!ילדה! ,לK! ,ראיתיyalda, lekh, ra’iti
I saw, go, girl
sexism
!עברייN! ,עלובה! ,מסיתavariyan, aluva, mesit
agitator, wretched, criminal
profanity
!כמה! ,לסביות! ,התחתkama, lesbiyot, taat
the a**, lesbians, how much
ageism
!דיקטטורי! ,הכל! ,בנטdiktatory, hakol, Bennett
Bennet, all, dictatorial
ableism
!בכל! ,עוד! ,כברbekol, od, kvar
already, more, in every
classism
!בN! ,עוד! ,נבלהben, od, neveilah
scavanger, more, son
ideoligism
!לK! ,הזה! ,שלאlekh, hazeh, she’lo
that not, this, go
other
!ולא! ,ערב! ,עכשיוve lo, erev, akhshav
now, evening, and not
all ﬁles
!Kכמה! ,עוד! ,לkama, od, lekh
go, more, how much
Table 2: Unigrams with top counts per ﬁle.
parameter
classes
F1
acc
maj
presence
2
0.699
0.699
0.518
target type
4
0.232
0.615
0.641
severity
4
0.201
0.354
0.616
vulgarity
2
0.589
0.616
0.565
aspects
7
0.125
0.488
0.545
Table 3: Multiclass classiﬁcation of offense types and
aspects.
onomy level. We can see that accuracy decreases
as we descend through taxonomy levels, with one
notable exception - offense severity is the hardest
category to classify.
4
Conclusions and Limitations
This paper explores the use of an offensive lan-
guage taxonomy for Hebrew social media content.
Using a new dataset annotated following the taxon-
omy of (Lewandowska-Tomaszczyk et al., 2023),
we highlight the challenges of classiﬁcation and
the limitations of static taxonomies for Hebrew.
The difﬁculty in classifying categories like vulgar-
ity and offense severity shows the complexities of
interpreting linguistic nuances. The results from
the multi-class classiﬁcation further reinforced the
notion that as we venture deeper into the taxon-
omy levels, the task of classiﬁcation becomes pro-
gressively challenging. In sum, this paper under-
lines the paramount importance of a multifaceted
approach to offensive language detection. Rely-
ing solely on individual words or ﬁxed taxonomies
may not capture the multifarious nature of lan-
guage, especially when dealing with nuanced top-
ics like offensive content. Future efforts should
consider incorporating advanced linguistic models
and domain-speciﬁc knowledge to enhance classi-
ﬁcation performance, especially at more granular
taxonomy levels.
Acknowledgments
This work was supported by the Israel Innovation
Authority. The subject of the program is the de-
velopment of a dataset and a language model for
identifying offensive language in Hebrew and Ara-
bic.
A
Appendix
114

--- Page 6 ---

parameter
category
sentences
P
R
F1
acc
majority
presence
present
175
0.695
0.693
0.693
0.694
0.513
presence
absent
184
0.676
0.669
0.664
0.667
0.513
target
group
86
0.502
0.501
0.492
0.718
0.777
target
non-targeted
39
0.448
0.493
0.469
0.885
0.899
target
individual
247
0.542
0.527
0.511
0.615
0.640
target
ind. wrt. gr./gr. wrt. ind.
14
0.480
0.487
0.483
0.936
0.964
severity
discredit
103
0.370
0.380
0.375
0.600
0.794
severity
insult
303
0.420
0.427
0.421
0.470
0.607
severity
hate speech
89
0.493
0.497
0.479
0.780
0.822
vulgatiry
vulgar
157
0.507
0.507
0.503
0.528
0.563
vulgarity
not vulgar
202
0.583
0.564
0.551
0.597
0.563
aspect
homophobia
32
0.726
0.654
0.681
0.930
0.925
aspect
sexism
12
0.488
0.500
0.494
0.977
0.972
aspect
racism
26
0.470
0.481
0.476
0.907
0.939
aspect
classism
10
0.488
0.494
0.491
0.965
0.977
aspect
other
229
0.602
0.599
0.599
0.605
0.534
aspect
ideologism
100
0.589
0.527
0.509
0.756
0.767
aspect
profanity
11
0.488
0.494
0.491
0.965
0.974
Table 4: Binary classiﬁcation of offensive categories.
parameter
category
mlbert acc
hebert acc
presence
absent
0.377
0.494
presence
present
0.558
0.494
target
non-targeted
0.610
0.909
target
individual
0.558
0.662
target
ind. wrt. gr./gr. wrt. ind.
0.610
0.974
target
group
0.675
0.636
severity
insult
0.377
0.234
severity
hate speech
0.558
0.234
severity
discredit
0.584
0.299
severity
threat
0.623
0.013
vulgarity
not vulgar
0.351
0.571
vulgarity
vulgar
0.584
0.571
aspect
racism
0.766
0.416
aspect
homophobia
0.636
0.909
aspect
sexism
0.623
0.013
aspect
other
0.325
0.455
aspect
profanity
0.584
0.987
aspect
ideologism
0.507
0.351
aspect
classism
0.571
0.013
aspect
ageism
0.675
0.987
Table 5:
Binary classiﬁcation of offensive categories
with ﬁne-tuned transformers.
115

--- Page 7 ---

References
Dana Alsagheer, Hadi Mansourifar, and Weidong Shi.
2022. Counter hate speech in social media: A sur-
vey. arXiv preprint arXiv:2203.03584.
Anna C Belkina, Christopher O Ciccolella, Rina Anno,
Richard Halpert, Josef Spidlen, and Jennifer E
Snyder-Cappione. 2019. Automated optimized pa-
rameters for t-distributed stochastic neighbor em-
bedding improve visualization and analysis of large
datasets. Nature communications, 10(1):5415.
Piotr Bojanowski, Edouard Grave, Armand Joulin, and
Tomas Mikolov. 2017. Enriching word vectors with
subword information. Transactions of the associa-
tion for computational linguistics, 5:135–146.
Ça˘grı Çöltekin. 2020. A corpus of turkish offensive
language on social media.
In Proceedings of the
Twelfth Language Resources and Evaluation Confer-
ence, pages 6174–6184.
Tianqi Chen, Tong He, Michael Benesty, Vadim
Khotilovich, Yuan Tang, Hyunsu Cho, Kailong
Chen, et al. 2015. Xgboost: extreme gradient boost-
ing. R package version 0.4-2, 1(4):1–4.
Patricia Chiril, Farah Benamara, Véronique Moriceau,
Marlene Coulomb-Gully,
and Abhishek Kumar.
2019. Multilingual and multitarget hate speech de-
tection in tweets. In Conférence sur le Traitement
Automatique des Langues Naturelles (TALN-PFIA
2019), pages 351–360. ATALA.
Avihay Chriqui and Inbal Yahav. 2021.
Hebert and
hebemo: a hebrew bert model and a tool for polar-
ity analysis and emotion recognition. arXiv preprint
arXiv:2102.01909.
Jacob Cohen. 1960.
A coefﬁcient of agreement for
nominal scales.
Educational and Psychological
Measurement, 20(1):37–46.
Matthew Costello and James Hawdon. 2020.
Hate
speech in online spaces. The Palgrave handbook of
international cybercrime and cyberdeviance, pages
1397–1416.
Thomas Davidson, Dana Warmsley, Michael Macy,
and Ingmar Weber. 2017. Automated hate speech
detection and the problem of offensive language. In
Proceedings of the international AAAI conference on
web and social media, volume 11, pages 512–515.
Darja Fišer, Tomaž Erjavec, and Nikola Ljubeši´c. 2017.
Legal framework, dataset and annotation schema for
socially unacceptable online discourse practices in
Slovene.
In Proceedings of the ﬁrst workshop on
abusive language online, pages 46–51.
Paula Fortuna, Joao Rocha da Silva, Leo Wanner, Sér-
gio Nunes, et al. 2019. A hierarchically-labeled Por-
tuguese hate speech dataset. In Proceedings of the
third workshop on abusive language online, pages
94–104.
Nagham Hamad, Mustafa Jarrar, Mohammad Khalilia,
and Nadim Nashif. 2023.
Offensive hebrew cor-
pus and detection using bert.
arXiv preprint
arXiv:2309.02724.
Michael Haugh and Valeria Sinkeviciute. 2019.
Of-
fence and conﬂict talk. The Routledge handbook of
language in conﬂict, pages 196–214.
HuggingFace. 2024.
XLM-RoBERTa-Multilingual-
Hate-Speech-Detection-New:
A
Pretrained
Model for Multilingual Hate Speech Detection.
https://huggingface.co/christinacdl/XLM_
RoBERTa-Multilingual-Hate-Speech-Detection-New.
Accessed: April 23, 2024.
Jan-Christoph Klie, Michael Bugert, Beto Boullosa,
Richard Eckart de Castilho, and Iryna Gurevych.
2018.
The inception platform: Machine-assisted
and knowledge-oriented interactive annotation. In
proceedings of the 27th international conference on
computational linguistics: system demonstrations,
pages 5–9.
SV Kogilavani, S Malliga, KR Jaiabinaya, M Malini,
and M Manisha Kokila. 2021. Characterization and
mechanical properties of offensive language taxon-
omy and detection techniques.
Materials Today:
Proceedings.
Barbara Lewandowska-Tomaszczyk. 2023. A simpli-
ﬁed taxonomy of offensive language (sol) for com-
putational applications.
Konin Language Studies,
10(3):213–227.
Barbara
Lewandowska-Tomaszczyk,
Anna
B ˛aczkowska,
Chaya
Liebeskind,
Giedre
Valu-
naite Oleskeviciene, and Slavko Žitnik. 2023. An
integrated explicit and implicit offensive language
taxonomy. Lodz Papers in Pragmatics, 19(1):7–48.
Barbara Lewandowska-Tomaszczyk, Slavko Žitnik,
Chaya Liebeskind, Giedr˙e Val¯unait˙e-Oleškeviˇcien˙e,
Anna B ˛aczkowska, Paul A Wilson, Marcin Tro-
jszczak,
Ivana Braˇc,
Lobel Filipi´c,
Ana Os-
troški Ani´c, et al. 2022.
Annotation scheme
and evaluation:
The case of offensive language.
Rasprave.
Chaya Liebeskind and Shmuel Liebeskind. 2018. Iden-
tifying abusive comments in Hebrew Facebook. In
2018 IEEE International Conference on the Science
of Electrical Engineering in Israel (ICSEE), pages
1–5. IEEE.
Marina Litvak, Natalia Vanetik, Chaya Liebeskind,
Omar Hmdia, and Rizek Abu Madeghem. 2022. Of-
fensive language detection in hebrew: can other lan-
guages help? In Proceedings of the Thirteenth Lan-
guage Resources and Evaluation Conference, pages
3715–3723.
Marina Litvak, Natalia Vanetik, Yaser Nimer, Abdul-
rhman Skout, and Israel Beer-Sheba. 2021. Offen-
sive language detection in semitic languages.
In
Multimodal Hate Speech Workshop, volume 2021,
pages 7–12.
116

--- Page 8 ---

Ping Liu, Wen Li, and Liang Zou. 2019.
NULI at
SemEval-2019 task 6: Transfer learning for offen-
sive language detection using bidirectional trans-
formers. In Proceedings of the 13th international
workshop on semantic evaluation, pages 87–91.
Hanane Mohaouchane, Asmaa Mourhir, and Nikola S
Nikolov. 2019.
Detecting offensive language on
Arabic social media using deep learning. In 2019
Sixth International Conference on Social Networks
Analysis, Management and Security (SNAMS), pages
466–471. IEEE.
Mahesh Pal. 2005. Random forest classiﬁer for remote
sensing classiﬁcation.
International journal of re-
mote sensing, 26(1):217–222.
Zeses Pitenis, Marcos Zampieri, and Tharindu Ranas-
inghe. 2020.
Offensive language identiﬁcation in
Greek. arXiv preprint arXiv:2003.07459.
Fabio Poletto, Marco Stranisci, Manuela Sanguinetti,
Viviana Patti, Cristina Bosco, et al. 2017.
Hate
speech annotation: Analysis of an Italian Twitter cor-
pus. In Ceur workshop proceedings, volume 2006,
pages 1–6. CEUR-WS.
Tharindu Ranasinghe, Marcos Zampieri, and Hansi
Hettiarachchi. 2019. Brums at hasoc 2019: Deep
learning models for multilingual hate speech and of-
fensive language identiﬁcation. In FIRE (working
notes), pages 199–207.
Hinrich Schütze and Jan O Pedersen. 1997.
A
cooccurrence-based thesaurus and two applications
to information retrieval. Information Processing &
Management, 33(3):307–318.
Amit
Seker,
Elron
Bandel,
Dan
Bareket,
Idan
Brusilovsky, Refael Shaked Greenfeld, and Reut
Tsarfaty. 2021.
Alephbert: A hebrew large pre-
trained language model to start-off your hebrew nlp
application with. arXiv preprint arXiv:2104.04052.
Jonathon Shlens. 2014. A tutorial on principal compo-
nent analysis. arXiv preprint arXiv:1404.1100.
Gudbjartur Ingi Sigurbergsson and Leon Derczynski.
2019. Offensive language and hate speech detection
for Danish. arXiv preprint arXiv:1908.04531.
Frank Smadja, Kathleen R McKeown, and Vasileios
Hatzivassiloglou. 1996. Translating collocations for
bilingual lexicons: A statistical approach. Computa-
tional linguistics, 22(1):1–38.
Stéphan
Tulkens,
Lisa
Hilte,
Elise
Lodewyckx,
Ben Verhoeven,
and Walter Daelemans. 2016.
A
dictionary-based
approach
to
racism
detec-
tion in dutch social media.
arXiv preprint
arXiv:1608.08738.
Raymond E Wright. 1995. Logistic regression.
Konthala Yasaswini, Karthik Puranik, Adeep Hande,
Ruba Priyadharshini, Sajeetha Thavareesan, and
Bharathi
Raja
Chakravarthi.
2021.
IIITT@
DravidianLangTech-EACL2021: Transfer learning
for offensive language detection in Dravidian lan-
guages.
In Proceedings of the First Workshop on
Speech and Language Technologies for Dravidian
Languages, pages 187–194.
Marcos Zampieri, Shervin Malmasi, Preslav Nakov,
Sara Rosenthal, Noura Farra, and Ritesh Kumar.
2019a.
Predicting the type and target of of-
fensive posts in social media.
arXiv preprint
arXiv:1902.09666.
Marcos Zampieri, Shervin Malmasi, Preslav Nakov,
Sara Rosenthal, Noura Farra, and Ritesh Kumar.
2019b. Semeval-2019 task 6: Identifying and cat-
egorizing offensive language in social media (offen-
seval). arXiv preprint arXiv:1903.08983.
117

```
