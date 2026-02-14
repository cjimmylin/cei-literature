---
title: "2021-Plaza-del-Arco-Overview of MeOffendEs at IberLEF 2021 Offensive Language Detection - PDF Extract"
source_pdf: "2021-Plaza-del-Arco-Overview of MeOffendEs at IberLEF 2021 Offensive Language Detection.pdf"
pages: 12
extracted_at: "2026-02-14T01:17:58.261639"
---

# PDF Extract: 2021-Plaza-del-Arco-Overview of MeOffendEs at IberLEF 2021 Offensive Language Detection

**Source PDF:** 2021-Plaza-del-Arco-Overview of MeOffendEs at IberLEF 2021 Offensive Language Detection.pdf
**Total Pages:** 12

---

## Content

```
--- Page 1 ---

Overview of MeOﬀendEs at IberLEF 2021: Oﬀensive
Language Detection in Spanish Variants
Resumen de la tarea MeOﬀendEs en IberLEF 2021: Detecci´on
de lenguaje ofensivo en las variantes del espa˜nol
Flor Miriam Plaza-del-Arco1, Marco Casavantes2, Hugo Jair Escalante2,
M. Teresa Mart´ın-Valdivia1, Arturo Montejo-R´aez1, Manuel Montes-y-G´omez2,
Horacio Jarqu´ın-V´asquez2, Luis Villase˜nor-Pineda2,3
1Universidad de Ja´en, Campus Las Lagunillas, 23071, Ja´en, Spain
2Laboratorio de Tecnolog´ıas del Lenguaje (INAOE), Mexico
3Centre de Recherche GRAMMATICA (EA 4521), Universit´e d’Artois, France
{fmplaza, maite, amontejo}@ujaen.es
{hugojair, mmontesg, villasen}@inaoep.mx
Abstract: This paper is an overview of MeOﬀendES 2021, organized at IberLEF
2021 and co-located with the 37th International Conference of the Spanish Society
for Natural Language Processing (SEPLN 2021). The main purpose of MeOﬀendEs
is to promote research on the detection of oﬀensive language in Spanish variants.
The shared task involve four subtasks, the ﬁrst two correspond to the identiﬁcation
of oﬀensive language categories in generic Spanish texts from diﬀerent social media
platforms, while subtasks 3 and 4 are related to the identiﬁcation of oﬀensive langua-
ge targeting the Mexican variant of Spanish. Two annotated datasets on oﬀensive
language have been released to the Natural Language Processing community. MeOf-
fendes attracted a large number of participants: a total of 69 signed up to participate
in the task, 12 submitted oﬃcial runs on the test data, and 10 submitted system
description papers. Corpora and results are available at the shared task website at
https://competitions.codalab.org/competitions/28679.
Keywords: MeOﬀendEs, detecci´on de lenguaje ofensivo, procesamiento del lenguaje
natural, clasiﬁcaci´on de textos.
Resumen: Este art´ıculo presenta la tarea MeOﬀendES 2021, organizada en iber-
LEF 2021 junto a la 37ª Conferencia Internacional de la Sociedad Espa˜nola para el
Procesamiento del Lenguaje Natural (SEPLN 2021). El objetivo principal de MeOf-
fendEs es promover la detecci´on del lenguaje ofensivo en las variantes del espa˜nol. La
tarea compartida implica cuatro subtareas, las dos primeras corresponden a la iden-
tiﬁcaci´on de categor´ıas de lenguaje ofensivo en textos gen´ericos en espa˜nol extra´ıdos
de diferentes redes sociales, mientras que las subtareas 3 y 4 est´an relacionadas con
la identiﬁcaci´on de lenguaje ofensivo dirigido a la variante mexicana del espa˜nol.
Para la competencia se han puesto a disposici´on de la comunidad del Procesamiento
del Lenguaje Natural dos conjuntos de datos anotados con lenguaje ofensivo. MeOf-
fendes ha atrav´ıdo a un gran n´umero de participantes: un total de 69 se inscribieron
para participar en la tarea, 12 presentaron resultados oﬁciales sobre los datos de
evaluaci´on y 10 presentaron art´ıculos describiendo su sistema. Los conjuntos de da-
tos y los resultados oﬁciales est´an disponibles en el sitio web de la tarea compartida:
https://competitions.codalab.org/competitions/28679.
Palabras clave: MeOﬀendEs, oﬀensive language detection, natural language pro-
cessing, text classiﬁcation.
1
Introduction
Oﬀensive language detection is part of the
broader domain of text classiﬁcation, and
closely related to the plethora of subjective
language classiﬁcation tasks (Wiebe et al.,
2004), including sentiment analysis (Medhat,
Procesamiento del Lenguaje Natural, Revista nº 67, septiembre de 2021, pp. 183-194
recibido 05-07-2021 revisado 12-07-2021 aceptado 16-07-2021
ISSN 1135-5948. DOI 10.26342/2021-67-16
© 2021 Sociedad Española para el Procesamiento del Lenguaje Natural

--- Page 2 ---

Hassan, and Korashy, 2014), emotion detec-
tion (Canales and Mart´ınez-Barco, 2014) and
hate speech detection (MacAvaney et al.,
2019). Oﬀensive language is more individual-
oriented, as oﬀenses are intended to upset or
to embarrass someone by means of insults or
impolite expressions. The growing participa-
tion of people in social media has raised the
problem of a frequent use of these communi-
cation channels as an uncontrollable means
to publish rude messages against others. It
is not diﬃcult to realize the large number of
works regarding this topic and focusing on
diﬀerent languages or targeted communities.
This interest, which extends through more
than a decade so far, has motivated several
evaluation campaigns, being the more recent
the MEX-A3T task at IberLEF 2020 (Arag´on
et al., 2020b), Oﬀenseval at SemEval 2020
(Zampieri et al., 2020), or OSACT4 shared
task at AOSCT 2020 (Mubarak et al., 2020).
Regarding the approaches applied to tac-
kle the challenge of detecting oﬀensive texts,
they share many common methods and al-
gorithms usually explored in text classiﬁca-
tion tasks, from early lexical based approa-
ches (Razavi et al., 2010) to current deep lear-
ning based ones (Plaza-del Arco et al., 2021).
With the aim of promoting research in the
detection of oﬀensive language for Spanish
and its Mexican variant, we introduced the
MeOﬀendEs task at IberLEF 2021 (Montes
et al., 2021) with four subtasks. The ﬁrst two
subtasks involve a novel dataset for oﬀensive
language research in general Spanish (Oﬀen-
dEs). The dataset contains users comments
in response to posts from well-known inﬂuen-
cers in diﬀerent social media platforms (Twit-
ter, YouTube and Instagram). Comments are
annotated on four diﬀerent classes that invol-
ve non-oﬀensive and oﬀensive categories. Par-
ticipants had to develop solutions for identif-
ying those categories from comments. Addi-
tional information is provided in the dataset,
including the inﬂuencer ID and the social me-
dia source of the post. Systems have to face
with diﬀerent challenges in these subtasks: (i)
diﬀerent language registers from three diﬀe-
rent social media platforms (ii) multi-class
classiﬁcation on non-oﬀensive and oﬀensive
categories, and (iii) multi-output prediction
based on annotators agreement. A total of
ﬁve teams submitted their prediction sys-
tems for subtask 1, and two teams for sub-
task 2. Finally, we have received four des-
cription papers from the participants in the-
se subtasks. Overall, the systems used by
the participants explore state-of-the-art clas-
siﬁcation models including traditional neural
networks and Transformer architectures. The
results obtained by the participants motiva-
tes to further research on the oﬀensive lan-
guage detection in diﬀerent social media plat-
forms and on the identiﬁcation of diﬀerent
oﬀensive language categories.
In addition to the previous subtasks,
MeOﬀendEs involves two subtasks on oﬀensi-
ve language detection targeting the Mexican
variant of Spanish (subtasks 3 and 4). These
are a continuation of previous eﬀorts in trying
to detect aggressiveness and oﬀensiveness in
tweets in the context of the IberLEF (Arag´on
et al., 2020a; Arag´on et al., 2019) and Ibe-
rEval forums (´Alvarez-Carmona et al., 2018)
for the same variant of Spanish. As in pre-
vious editions, participants had to develop
solutions to recognize oﬀensiveness in tweets.
This time, however, we released additional in-
formation accompanying tweets, with the ho-
pe that such information could be beneﬁcial
for improving the recognition performance.
Also, these subtasks consider a new dataset
build upon those used in past editions. The
main diﬀerence being the annotation process:
for the IberLEF2021 campaign tweets were
carefully analyzed and labeled by a commit-
tee of annotators (see Section 3.2). Our goal
was to provide a curated dataset that could
result in more reliable conclusions.
As in previous editions, the aim of sub-
tasks 3 and 4 were to motivate research on
the analysis of oﬀensive language in Mexi-
can Spanish. A language whose characteris-
tics and variations make it unique in its kind
and diﬀerent to other languages, making it
necessary to have tailored techniques for this
language. Likewise, cultural aspects like the
use of language with sexual connotation for
non oﬀensive communications make it parti-
cularly challenging in terms of disambigua-
tion. This phenomenon is not present in the
languages considered in other evaluation fo-
rums and therefore it has not been studied
elsewhere.
Subtasks 3 and 4 attracted a considera-
ble number of participants, most of them im-
plementing solutions based on cutting edge
language modeling tools available. In gene-
ral terms, performance of solutions was lo-
wer than that achieved in previous years (see,
Flor Miriam Plaza-del-Arco, Marco Casavantes, Hugo Jair Escalante, M. Teresa Martín-Valdivia,  
Arturo Montejo-Ráez, Manuel Montes-y-Gómez, Horacio Jarquín-Vásquez, Luis Villaseñor-Pineda
184

--- Page 3 ---

e.g., (Arag´on et al., 2020a)), this could be due
to the more careful annotation process. For
subtask 3, which does not consider any ad-
ditional metadata, most participants outper-
formed the baseline, whereas for subtask 4,
no team outperformed1 it. Contrary to what
we were expecting, subtask 3 received more
submissions even when additional data was
provided for subtask 4. Overall, results are
encouraging and motivate further research.
As with the other subtasks, we will keep the
leaderboard of the competition open, so that
users can keep making submissions despite
the competition is over.
The remainder of this paper is organized
as follows. Section 2 introduces the four sub-
tasks that are part of MeOﬀendEs. Then,
Section 3 describes the corpora considered
for the diﬀerent subtasks. Next, the solu-
tions proposed to approach the posed pro-
blems and their results are reviewed in Sec-
tion 4. Finally, conclusions are presented in
Section 5.
2
Task description
This section describes in detail the four sub-
tasks that are part of the MeOﬀendEs com-
petition at IberLEF 2021.
The whole shared task was implemented
in the CodaLab platform2 and every sub-
task comprised two phases: (1) a develop-
ment phase in which participants had access
to labeled trial and training data, and whe-
re they could make submissions to test the
platform; and (2) a ﬁnal phase in which unla-
beled test data was released and participants
uploaded the predictions of their systems to
the platform. The evaluation and raking for
the oﬃcial results used the performance sco-
re measured in the test phase. The diﬀerent
subtasks on diﬀerent corpora (see Section 3),
and their evaluation measures, are described
below:
• Subtask 1: Non-contextual multi-
class classiﬁcation for generic Spa-
nish. Participants had to classify com-
ments into the four diﬀerent categories
associated with the OﬀendEs corpus (see
subsection 3.1). No information about
the comment (source or inﬂuencer ID)
1Please note that baselines were very competitive
as described in Section 3.2.1
2https://competitions.codalab.org/
competitions/28679
is provided. Participants can optionally
submit conﬁdence values to predictions
(as a probability for each class, so they
all sum 1.0) for the four considered ca-
tegories, in order to evaluate the agree-
ment of predictions with conﬁdence of
ten human annotators. For evaluation
we considered the micro-averaged pre-
cision, recall and f1 measures. In ca-
ses where participants submit conﬁdence
values (between 0 and 1) to their out-
puts, Mean Squared Error (MSE) is ap-
plied (with error value equal to one for
wrongly predicted classes).
• Subtask 2: Contextual multiclass
classiﬁcation for generic Spanish.
Same problem as subtask 1, but meta-
data (information about targeted users
and the related social media) is provided
to participants. Participants had access
to information associated with posts: so-
cial media source, inﬂuencer genre and
inﬂuencer name. The same evaluation
measures as subtask 1 were taking into
account for this subtask.
• Subtask 3: Non-contextual binary
classiﬁcation for Mexican Spanish.
Participants must classify tweets as of-
fensive or non-oﬀensive in the Oﬀend-
MEX corpus, this is, a binary text classi-
ﬁcation problem. For evaluation we con-
sidered the precision, recall and f1 mea-
sure with respect to the oﬀensive class.
• Subtask 4: Contextual binary clas-
siﬁcation for Mexican Spanish. Sa-
me problem as subtask 3, but metada-
ta about each tweet was provided to
participants. For this subtask, partici-
pants had access to information associa-
ted with the tweets and their authors li-
ke: date, retweet count, followers count,
etc. The aim of including this informa-
tion was to determine to what extent
contextual information of tweets and
users is useful for improving the detec-
tion performance. The same evaluation
measures as subtask 3 were used for this
one.
3
Datasets and baselines
3.1
OﬀendES
For subtasks 1 and 2 we have released a no-
vel dataset for oﬀensive language research
Overview of MeOffendEs at IberLEF 2021: Offensive Language Detection in Spanish Variants
185

--- Page 4 ---

in general Spanish (OﬀendEs). Focusing on
young inﬂuencers from the well-known social
platforms of Twitter, Instagram, and YouTu-
be, we have collected a corpus composed of
47,128 Spanish comments manually labeled
on oﬀensive pre-deﬁned categories. A subset
of the corpus is labeled with three annotators
while another subset is labeled with ten an-
notators. The latter attaches a degree of con-
ﬁdence to each label computed as the ratio of
annotators that agreed on the majority label
over the total number of annotators, so both
multiclass classiﬁcation and multioutput re-
gression studies can be carried out. For the
competition, we have selected 30,416 posts
from the total. The posts are labeled with
the following categories:
- Oﬀensive, target is a person (OFP).
Oﬀensive text targeting a speciﬁc individual.
- Oﬀensive, target is a group of peo-
ple or collective (OFG).
Oﬀensive text
targeting a group of people belonging to the
same ethnic group, gender or sexual orien-
tation, political ideology, religious belief or
other common characteristic.
- Oﬀensive, target is diﬀerent from a
person or a group (OFO).
Oﬀensive text
where the target does not belong to any of the
previous categories, e.g., an organization, an
event, a place, an issue.
- Non-oﬀensive, but with expletive lan-
guage (NOE).
A text that contains ru-
de words, blasphemes or swearwords but
without the aim of oﬀending, and usually
with a positive connotation.
-
Non-oﬀensive
(NO).
Text
that
is
neither oﬀensive nor contains expletive lan-
guage.
We consider a post as oﬀensive when lan-
guage is used to commit an explicit or im-
plicitly directed oﬀense that may include in-
sults, threats, profanity or swearing.
Additional to the text of the comment,
two features were also provided as “contex-
tual” information: the name of the social
platform where that comment was posted to,
and the gender addressee of the comment, i.e.
the targeted user.
Finally, diﬀerent sets have been relea-
sed for the competition. During the pre-
evaluation phase training and development
(Dev) sets were provided to the participants
and for the evaluation phase the test set was
release, Table 1 shows the number and per-
centage of posts corresponding to each set by
the above categories.
Label
Training
Development
Test
NO
13,212
64
9651
NOE
1,235
22
2340
OFP
2,051
10
1404
OFG
212
4
211
Total
16,710
100
13,606
Tabla 1: Distribution of the OﬀendES catego-
ries by subset (Training, Dev, Test) in MeOf-
fendES subtasks 1 and 2.
3.1.1
Baseline
To evaluate the non-contextual multiclass
classiﬁcation task on the OﬀendEs dataset,
we implemented a straightforward baseline
system based on a bag-of-words of unigrams,
bigrams and trigrams and an linear SVM
classiﬁer. For the multiouput regression task
we use a multiouput regressor along with the
Epsilon-Support Vector Regression. No pre-
processing has been applied to the text, nor
has a hyperparameter search been performed.
We refer to these baselines as baseline-svm.
3.2
OﬀendMEX
For subtasks 3 and 4 we have released a
novel dataset in Mexican Spanish collected
from Twitter and manually labeled for oﬀen-
siveness. The resource is formed by tweets
labeled with binary and multiclass catego-
ries with the following types of oﬀensiveness
according to a recent categorization (D´ıaz-
Torres et al., 2020): oﬀensive, aggressive and
vulgar (but not oﬀensive). Although the inhe-
rent problem is a multi label classiﬁcation
one (e.g., a tweet can be oﬀensive but not
vulgar), we are approaching the underlying
binary-classiﬁcation task of interest: distin-
guishing oﬀensive from non-oﬀensive tweets.
Nevertheless, we released all of the labels for
the training data as additional information
that participants can exploit when develo-
ping their solutions. Such information was
not provided in the test set partition.
Additionally, for subtask 4, we distributed
metadata information associated with tweets
in the corpus, these include: date, retweet
count, favourite count, reply status, quote
status; and metadata derived from users, in-
cluding: veriﬁcation status, followers count,
listed count, favourites count, status count,
Flor Miriam Plaza-del-Arco, Marco Casavantes, Hugo Jair Escalante, M. Teresa Martín-Valdivia,  
Arturo Montejo-Ráez, Manuel Montes-y-Gómez, Horacio Jarquín-Vásquez, Luis Villaseñor-Pineda
186

--- Page 5 ---

date the account was created, among a few
others associated to the user proﬁle and ima-
ge. Detailed information on the considered
metadata can be found in the corresponding
API documentation (Twitter, 2021).
Partition
Tweets
Oﬀ.
No Oﬀ.
Trial
76
41
35
Training
5,060
1,381
3,679
Test
2,183
600
1,583
Total
7,319
2,022
5,287
Tabla 2: Number of tweets in the OﬀendMex
corpus.
Table 2 summarizes the OﬀendMex data
set used for subtasks 3 and 4. The Trial par-
tition was rather small, as the idea was to use
such partition for testing the submission sys-
tem. Training and test partitions are larger
and present an approximate class imbalance
ratio of 2,6 favoring the non-oﬀensive class.
3.2.1
Baselines
In order to approach the Contextual and
Non-contextual binary classiﬁcation for Me-
xican Spanish, we implemented two popular
approaches that have shown to be hard to
beat in both subtasks: i) a Bidirectional Ga-
ted Recurrent Unit (Bi-GRU) neural network
for the Non-Contextual binary classiﬁcation,
and ii) a XGBoost + BETO ensemble for the
Contextual binary classiﬁcation.
For the Bi-GRU neural network baseline,
all text was pre-processed by removing spe-
cial characters and stopwords (with the ex-
ception of personal pronouns); in order to
enrich the vocabulary, all hashtags were seg-
mented by words (e.g. #EsDeLesbianas - es
de lesbianas), and all emojis were conver-
ted into words (e.g. , - ‘cara sonriente’). As
input features pre-trained Spanish FastText
(Grave et al., 2018) embeddings were used,
and a fully-connected softmax layer handle
the class probabilities. Alternatively, for the
XGBoost + BETO ensemble baseline the da-
ta pre-processing steps consisted of conver-
ting the text to lowercase and stripping it
of emojis. This ensemble involves two stages.
In the ﬁrst stage the messages were classiﬁed
considering only their textual content using
BETO (Ca˜nete et al., 2020). Subsequently,
in the second stage BETO predictions were
concatenated to the three most discriminati-
ve metadata features (Tweet favorite count,
User listed count and Default proﬁle) to form
new vectors, handled at the end by a XG-
Boost classiﬁer (Chen and Guestrin, 2016).
We refer to these two baselines as baseline-dl
below.
In addition to the previous baselines
we evaluated the performance of a rather
straightforward baseline based on a bag-
of-unigrams-bigrams-trigrams and an linear
SVM classiﬁer, where a similar preprocessing
as above was applied. The goal of this baseli-
ne was to evaluate the added value metadata
when using a linear model, and to assess the
margin of beneﬁts of approaches over a di-
rect baseline method. We will refer to these
baselines as baseline-bow.
4
Participant approaches and
results
4.1
Subtask 1
This subtask, as introduced previously, pro-
poses a pure multi-class text classiﬁcation
problem or a multi-output one. Here, a brief
description of participants’ systems is provi-
ded.
NLP-CIC team (Aroyehun and Gel-
bukh, 2021) used the multilingual model
XLM-RoBERTa pre-trained on Twitter texts
and Sentiment Analysis data. They show that
Sentiment Analysis and the social domain
adaption is beneﬁcial for the problem of of-
fensive language detection. The system ran-
ked the ﬁrst position in the competition.
UMUTeam
(Garc´a-D´ıaz,
Jim´enez-
Zafra, and Valencia-Garc´ıa, 2021) explo-
red a wide range of features and how to com-
bine them in a ﬁnal multi-layer perceptron
(MLP) with several tentative conﬁgurations.
The features considered were lexical features,
negation features, word and sentence embed-
dings from diﬀerent embedding algorithms
(fastText , word2vec, gloVe and a Spanish
version of BERT). Word embeddings were
evaluated isolated from the rest of features
using convolutional networks and two well-
known recurrent architectures like LSTM and
Bi-GRU, although MLP was the one showing
the best behavior. In general, these featu-
res were further pre-processed, with MinMax
scaler for linguistic ones and Robust scaler for
negation features. All these features as ﬁlte-
red using mutual information. Also, several
approaches to combine the total number of
features generated were evaluated, including
Overview of MeOffendEs at IberLEF 2021: Offensive Language Detection in Spanish Variants
187

--- Page 6 ---

majority voting, weighted voting and logis-
tic regression. Diﬀerent kinds of shape and
diﬀerent number of layers, number of neu-
rons, dropout probabilities, batch sizes and
activation functions deﬁned a varied num-
ber of experiments in order to identify the
best conﬁguration for system hyperparame-
ters. From oﬃcial results it can be drawn
that a combination of BERT-based encodings
(pre-trained and ﬁne-tuned), with sentences
embeddings and lexical and negation featu-
res became the best solution. When linguistic
features were removed, the system obtained
the second position in the competition.
The GDUFS DM team applied se-
quence classiﬁcation system ﬁne-tuned on a
pre-trained BERT model and composing the
ﬁnal encodings for the text from a max poo-
ling of the sentence encondings from all layers
and token encondings from last layer. Two
additional techniques were integrated in the
ﬁnal system: pseudo-labeling and focal loss.
The former technique consists of a two-stage
training, were test labels are predicted and
re-entered into the learning process to produ-
ce a larger training set. Focal loss was used as
a way to correct class imbalance. The system
ranked in the third position in the competi-
tion.
Marta Navarr´on and Isabel Segura
(Garc´ıa and Bedmar, 2021) explored dif-
ferent deep learning models including Long-
Short Term Memory (LSTM) and Bidirectio-
nal Encoder Representations from Transfor-
mers (BERT). The best results was archived
by the BERT model. The system ranked in
the fourth position in the competition.
4.2
Subtask 2
UMUTeam was the only team in submit-
ting results to this subtask. They applied the
same system to add to the set of features
applied one-hot encodings of contextual co-
lumns (gender and media). Robust scaler was
also applied to these two features, as done
with negation ones. Compared to what was
obtained in subtask 1, the integration of con-
textual information contributed to a small,
but consistent improvement in ﬁnal scores.
4.3
Analysis of subtasks 1 and 2
Table 3 and Table 4 provides a summary
of the oﬃcial results for subtasks 1 and 2
in terms of micro-average and macro-average
of Precision, Recall and F1 scores, respecti-
vely. Regarding the multiclass classiﬁcation
setting, it can be notice that all the teams
outperformed our baseline-svm which shows
the success of the neural network models em-
ployed by the participants compared to clas-
sical machine learning algorithms. However,
for the multioutput regression setting, two of
the four teams outperformed the SVM regres-
sor baseline, which shows the success of the
classical learning algorithm in this setting.
For the non-contextual multiclass classiﬁca-
tion, it can be seen that the scores of the
ﬁrst three teams are very close. This close-
ness in performance could be due to the fact
that most of these top ranked participants
relied on similar pretrained models in their
solutions (Spanish BERT model, except for
NLP-CIC, who ﬁne-tuned a multilingual Ro-
BERTa model). But greater diﬀerences can
be observed when looking at the MSE error.
The lower MSE value is, the closer is the sys-
tem to the behaviour of human annotators.
In that case, XML-RoBERTa almost reduces
to a half the error of the second system in
the ranking. Finally, both F1 scores and MSE
errors are consistent in terms of ranking or-
der.
For the second subtask, only one team eva-
luate their system. We can observe that the
contextual information did not improve per-
formance, in terms of F1 score, to that obtai-
ned by their system in subtask1. But regar-
ding MSE, including those additional featu-
res (social media platform and gender of the
targeted user) do led to a system closer to
human annotator behaviour.
Subtask 1: Non-contextual classiﬁcation
Team
P
R
F1
MSE
NLP-CIC
0.8815
0.8815
0.8815
0.0231
UMUTeam
0.8782
0.8782
0.8782
0.0411
GDUFS DM
0.8732
0.8732
0.8732
0.0672
Marta Isabel
0.8416
0.8417
0.8416
0.0697
baseline-svm
0.8285
0.8285
0.8285
0.0615
Subtask 2: Contextual classiﬁcation
Team
P
R
F1
MSE
UMUTeam
0.8782
0.8782
0.8782
0.0409
Tabla 3: Subtasks 1 and 2 oﬃcial ranking. Re-
sults are in terms of Micro-precision, Micro-
Recall and Micro-F1 scores.
Flor Miriam Plaza-del-Arco, Marco Casavantes, Hugo Jair Escalante, M. Teresa Martín-Valdivia,  
Arturo Montejo-Ráez, Manuel Montes-y-Gómez, Horacio Jarquín-Vásquez, Luis Villaseñor-Pineda
188

--- Page 7 ---

Subtask 1: Non-contextual classiﬁcation
Team
P
R
F1
MSE
NLP-CIC
0.7679
0.7093
0.7324
0.0231
UMUTeam
0.7861
0.6919
0.7301
0.0411
GDUFS DM
0.7565
0.7002
0.7239
0.0672
Marta Isabel
0.5781
0.5451
0.5595
0.0697
baseline-svm
0.6278
0.4831
0.5236
0.0615
Subtask 2: Contextual classiﬁcation
Team
P
R
F1
MSE
UMUTeam
0.7879
0.6921
0.7308
0.0409
Tabla 4: Subtasks 1 and 2 oﬃcial ranking. Re-
sults are in terms of Macro-precision, Macro-
Recall and Macro-F1 scores.
4.4
Subtasks 3 and 4: Oﬀensive
language identiﬁcation in
Mexican Spanish
We now analyze the results obtained by parti-
cipants of subtasks 3 and 4. For the former, a
total of 10 teams submitted runs for the ﬁnal
phase and were considered for the oﬃcial lea-
derboard. In addition, two other teams sub-
mitted runs but these did not qualify for the
oﬃcial ranking. For subtask 4 we received the
submissions from three diﬀerent teams. This
was somewhat disappointing as we were ex-
pecting participants to exploit the metadata
provided with the dataset.
Subtask 3: Non-contextual classiﬁcation
Team
P
R
F1
CIMAT-MTY-GTO
0.7600
0.6533
0.7026
NLP-CIC
0.7550
0.6407
0.6932
DCCD-INFOTEC
0.6733
0.6966
0.6847
CIMAT-GTO
0.6633
0.6958
0.6792
UMUTeam
0.6650
0.6763
0.6706
Timen
0.6000
0.6081
0.6040
CIC-IPN
0.5350
0.6874
0.6017
Baseline-bow
0.6040
0.5517
0.5767
Baseline-dl
0.7192
0.4100
0.5222
xjywing
0.8883
0.3417
0.4935
aomar
0.8750
0.3239
0.4728
CEN-Amrita
0.9183
0.3143
0.4683
Subtask 4: Contextual classiﬁcation
Team
P
R
F1
Baseline-dl
0.6629
0.6983
0.6801
UMUTeam
0.6683
0.6705
0.6694
CIC-IPN
0.5383
0.6843
0.6026
Baseline-bow
0.6062
0.5517
0.5777
Timen
0.4233
0.4456
0.4341
Tabla 5: Final results for the Contextual and
Non-contextual binary classiﬁcation for Me-
xican Spanish
Table 5 provide a summary of the oﬃcial
results for subtasks 3 and 4. For the former,
i.e., non-contextual binary classiﬁcation, it
can be seen that there were only 3 teams that
did not beat the baselines associated with the
task. The best performance was obtained by
the CIMAT-MTY-GTO team with a relative
improvement over the bow and dl baselines
of 21% and 34%, respectively. Followed clo-
sely by the next 4 teams in the ranking. This
closeness in performance could be due to the
fact that most of these top ranked partici-
pants relied on similar pretrained models in
their solutions, see Table 6.
Interestingly, baseline-bow outperformed
the one based on the Bi-GRU. This could be
due to the fact that the latter model was trai-
ned only on the available data, which may be
of limited size given the complexity of GRU
models. Other participants outperformed the
baselines because they used external resour-
ces and pretrained models (see Table 6).
Regarding task 4, from Table 5 it can be
seen that no team outperformed baseline-dl.
This is due in part to the competitiveness of
the baseline model, but also, to the fact that
participants did not do any special processing
for the provided metadata (see below). Still,
two out of the three teams were close to the
baseline. On the other hand, only one team
did not outperformed the baseline-bow. The
improvement of baseline-dl over baseline-bow
could be due to the fact that the former used
a representation based on a transformer, op-
posed to the Bi-GRU baseline considered for
subtask 3.
Finally, when comparing the results of
baseline-bow in both tasks, it is observed that
the added value of metadata in subtask 4 only
yield a negligible improvement. This conﬁrms
that the sole inclusion the features is not
enough to improve performance.
4.4.1
Systems descriptions
Table 6 summarizes the contributions from
teams that participated in subtasks 3 and 4,
it shows the adopted models and highlights
any novel aspect of the diﬀerent approaches.
In the following, we outline the main ﬁn-
dings from the methodologies proposed to ap-
proach subtasks 3 and 4.
• Transformer-based solutions were
common. Most teams relied on pretrai-
ned transformers for Spanish in the mo-
deling process, we assume this was with
the purpose of alleviating the small sam-
ple problem. This is in line with trends in
Overview of MeOffendEs at IberLEF 2021: Offensive Language Detection in Spanish Variants
189

--- Page 8 ---

general NLP, and in general it was very
helpful: most of top ranked participants
used transformers. Despite these results,
we think that more specialized mecha-
nisms could help to boost performance
when using transformers.
• Advanced linguistic features were
not considered in most approaches.
Only a couple of teams (UMUTeam and
CIC-IPN teams) proposed solutions that
included linguistic analyses, and another
team relied on a genetic programming
formulation (DCCD-INFOTEC). It is
interesting that their performance was
competitive, even when no transformer
was used. It may be expected that an
adequate combination of linguistic and
data-driven features could result in bet-
ter performance.
• External
data.
External
data
for
further ﬁne tuning transformer models
was adopted by top ranked participants.
Suggesting this is a promising way for
further improving the performance of
transformers.
• No special treatment for processing
metadata for subtask 4.
It was so-
mewhat disappointing that participants
of subtask 4, did not took full advantage
of metadata. These features were conca-
tenated to the other input spaces and
feed to classiﬁcation models. We are still
conﬁdent that recognition performance
can be improved when these features are
used eﬀectively.
4.4.2
Analysis
In order to further analyze the participants’
results, we performed an analysis on the com-
plimentariness and diversity of the predic-
tions from the diﬀerent teams. For this analy-
sis we used the last run from every team in
the diﬀerent subtasks. We measured the di-
versity of predictions by using the Coincident
Failure Diversity (CFD) measure (Tang, Su-
ganthan, and Yao, 2006). This measure ex-
presses with a number in [0,1] the extend to
which the errors made by diﬀerent classiﬁca-
tion system overlap (the higher the value the
less correlated the errors are). On the other
hand, to measure the complimentariness of
predictions, we calculated the Maximum Pos-
sible Accuracy (MPA), this is the accuracy
that can be obtained if we consider a tweet
correctly classiﬁed when at least one of the
considered systems classiﬁed it correctly.
Table 7 shows the CFD and MPA values
obtained for the considered runs from sub-
tasks 3 and 4, for completion we also report
the best accuracy (BA) obtained by any of
the considered systems. From these results, it
is possible to observe that the MPA in both
subtasks is considerably greater than the BA
in both subtasks, suggesting that the partici-
pants systems and approaches are somewhat
complementary to each other: performance
could improve by ≈16% and ≈11% if the pre-
dictions from the available systems were com-
bined optimally for subtasks 3 and 4, respec-
tively. The values of the CFD measure show
that there is a high diversity among errors in
the predictions of both subtasks. Most no-
tably for subtask 3. Results are consistent
with the number of participating teams in
both subtasks.
As a result of applying the MPA metric, it
was possible to identify those common errors
across all systems3. In fact, there are only 34
tweets that no system could classify correctly.
Nine of them are oﬀensive tweets that were
classiﬁed as non-oﬀensive. Below we present
some of these tweets (a rough translation to
English is provided), where we can identify
oﬀenses with no vulgar or profane words (e.g.
“gata”), the use of out of the training voca-
bulary words (e.g. “whore”), the masking of
potentially oﬀensive words (e.g. “pen....”), as
well as some ironic comments.
• Nada peor que whore y gorda #sorrynotsorry.
(ENG:
Nothing
worse
than
whore
and
fat
#sorrynotsorry)
• Yo no te quise decir gata, pero bueno. Eres una
gata (ENG: I did not mean to say gata. But well.
You are a gata.)
• Soy yo o @USUARIO est´a bien pen.... hace dra-
mas se pone loca y pierde jajaja @ExatlonMx.
(ENG: It is me or @USER is pen... she gets
crazy and loses hahah @ExatlonMx.)
• B´asicamente, el feminismo se trata de feas pe-
leando por los derechos de las guapas. (ENG:
Basically, feminism is about the ugly girls ﬁgh-
ting for the rights of the pretty ones. )
A couple of mistakenly classiﬁed non-
oﬀensive tweets are the following:
• @USUARIO Vas en micro, camina, se suben
unos HDP y les quitan todo a todos En un taxi,
te pueden secuestrar... En el metro hay n car-
teristas. (ENG: @USER you are going in bus,
it moves, some HPD get in, they steal everyo-
ne. In a can you can be kipnaped.... in the subay
there are n pinpockets.)
3NOTE: In this section we include examples of
language that may be oﬀensive to some readers, these
do not represent the perspectives of the authors.
Flor Miriam Plaza-del-Arco, Marco Casavantes, Hugo Jair Escalante, M. Teresa Martín-Valdivia,  
Arturo Montejo-Ráez, Manuel Montes-y-Gómez, Horacio Jarquín-Vásquez, Luis Villaseñor-Pineda
190

--- Page 9 ---

Systems considered in the oﬃcial ranking.
Team
Novel elements
Transformer / Model
Reference
CIMAT-MTY-GTO
External
data
was
from
hate-
speecha detection and sentiment
analysis was used to augment the
training set.
Ensemble of BERT
models
for
Spanish
(BETO)
(G´omez-Espinosa,
Mu˜niz-Sanchez,
and
L´opez-Monroy, 2021)
NLP-CIC
The model was trained with both
tweets and sentiment analysis data
in Spanish.
XLM-RoBERTa
(Aroyehun and Gelbukh,
2021)
DCCD-INFOTEC
A combination of diﬀerent models
trained for humor, aggressiveness
and misogyny detection, in addition
to models trained on the provided
training set and a reverse version of
it.
EvoMSA
(genetic
programming
based
model)
(Calder´on,
Tellez,
and
Graﬀ, 2021)
CIMAT-GTO
The models were trained taking ad-
vantage of the auxiliary sentence for
the transformer. Two methods for
obtaining auxuliary sentences were
proposed.
Ensemble of BERT
models
for
Spanish
(BETO)
(S´anchez-Vega
and
L´opez-Monroy, 2021)
UMUTeam∗
A variety of linguistic features, in-
cluding negation were considered
and combined with learned repre-
sentations.
Ensembles of models
based
on
linguistic
and learned features
(embeedings).
(Garc´a-D´ıaz,
Jim´enez-
Zafra,
and
Valencia-
Garc´ıa, 2021)
CIC-IPN∗
A diversity of conﬁgurations we-
re tested, a model pretrained on
tweets and sentiment analysis data
obtained the best performance.
XLM-RoBERTa
(Huerta-Velasco
and
Calvo, 2021)
CEN-Amrita
Better results were obtained withe
the Bi-LSTM model
Bidirectional
LSTM
and
BERT
(bert-
base-multilingual-
cased)
(Sreelakshmi, Premjith,
and Soman, 2021)
Additional models
QuSwe1d0n
The representation obtained from
the transformer was feed to a CNN
based model.
XLM and CNN
(Qu, Que, and Shuang-
jun, 2021)
YNU qyc
The output of the transformer was
feed to an LSTM model, a K-folding
ensemble scheme was adopted.
XLM-RoBERTa and
LSTM
(Qu, Yang, and Wang,
2021)
Tabla 6: Summary of system descriptions that participated in subtasks 3 and 4. ∗Indicates this
team participated in both tasks. We separate systems that qualiﬁed for the oﬃcial results and
additional systems.
Subtask
BA
MPA
CFD
NoT
3
0.8277
0.9844
0.6073
10
4
0.8185
0.9271
0.2685
3
Tabla 7: Comparison of MPA and CFD
results between the Contextual and Non-
contextual binary classiﬁcation. The Best Ac-
curacy (BA) obtained by the participating
teams in each subtask, was used to compare
the complementarity obtained with the MPA
metric; NoT stands for Number of Teams.
• Sus pinches relaciones empiezan con un Invita
a tus amigas las m´as putas y piden ﬁdelidad,
malditos ilusos. (ENG: Your damn relationships
start with an invite to your friends, the most
promiscuous and you ask ﬁdelity, fkng dreamer.)
This analysis suggests the most diﬃcult
instances are those that require further lin-
guistic analysis. This evidences the inherent
challenges of this variation of language and
the detection of oﬀensiveness in text. Moti-
vating further research on this subject.
Another important aspect to mention is
that the corpus used this year took a sub-
set of last year’s data and was relabeled with
the guide proposed by (D´ıaz-Torres et al.,
2020). For this task, a group of labelers of
diﬀerent ages was selected (3 adults, 6 youth)
and balancing the number of males and fema-
les (4 females, 5 males). This new relabeling
was the main decrease in the reported results
(baseline decreased by 0.19 points compared
Overview of MeOffendEs at IberLEF 2021: Offensive Language Detection in Spanish Variants
191

--- Page 10 ---

to last year). Diversity in the group of labe-
lers (generational change as well as gender)
increased the variations present in both the
training set and the test set. The creation
of robust systems for this task must consider
these scenarios both during the training pha-
se and to provide a conﬁdence rating of the
prediction made by the automatic method.
5
Conclusion
The MeOﬀendEs shared task at IberLEF at-
tempts to continue to the research in oﬀensive
language detection in Spanish. A new data-
set on generic Spanish has been prepared for
this edition, as a companion collection to the
existing one on Mexican Spanish, enabling in-
tensive experimentation over a large number
of messages from diﬀerent social media plat-
forms. This evaluation campaign allowed par-
ticipants to test their systems on this classi-
ﬁcation task. Diﬀerent algorithms, features,
techniques and conﬁgurations were explored,
reporting the eﬀectiveness of the approaches
and contributing to the advance of oﬀensive
language detection systems.
A total of 69 participants registered to
the MeOﬀendEs shared task. However, only
12 teams participated in the ﬁnal phase of
the challenge. Interesting ﬁndings and con-
clusions have been drawn and very competi-
tive approaches are now available to approach
the 4 proposed subtasks. Given the interest
from the community we are keeping the cha-
llenge website open so that anyone interested
in trying their own methods can do it at any
time.
Acknowledgements
We would like to thank CONACyT for par-
tially supporting this work under grants CB-
2015-01-257383 and the Thematic Networks
program (Language Technologies Thematic
Network). Hugo Jair Escalante is suppor-
ted by CONACyT under project grant CO-
NACYT CB-S-26314.
This work is also partially supported by
the grant P20 00956 (PAIDI 2020) from An-
dalusian Regional Government, a grant from
European Regional Development Fund (FE-
DER), the LIVING-LANG project [RTI2018-
094653-B-C21], and the Ministry of Scien-
ce, Innovation and Universities (scholarship
[FPI-PRE2019-089310]) from the Spanish
Government.
References
´Alvarez-Carmona, M. ´A., E. Guzm´an-Falc´on,
M. Montes-y-G´omez, H. J. Escalante,
L. Villase˜nor-Pineda, V. Reyes-Meza, and
A. Rico-Sulayes. 2018. Overview of MEX-
A3T at ibereval 2018: Authorship and
aggressiveness analysis in mexican spa-
nish tweets.
In P. Rosso, J. Gonzalo,
R. Mart´ınez, S. Montalvo, and J. C. de Al-
bornoz, editors, Proceedings of the Third
Workshop on Evaluation of Human Lan-
guage Technologies for Iberian Languages
(IberEval 2018) co-located with 34th Con-
ference of the Spanish Society for Natural
Language Processing (SEPLN 2018), Se-
villa, Spain, September 18th, 2018, volu-
me 2150 of CEUR Workshop Proceedings,
pages 74–96. CEUR-WS.org.
Arag´on, M. E., M.
´A.
´Alvarez-Carmona,
M. Montes-y-G´omez, H. J. Escalante,
L. Villase˜nor-Pineda, and D. Moctezuma.
2019.
Overview of MEX-A3T at iber-
lef 2019: Authorship and aggressiveness
analysis in mexican spanish tweets.
In
M. ´A. G. Cumbreras, J. Gonzalo, E. M.
C´amara, R. Mart´ınez-Unanue, P. Ros-
so, J. Carrillo-de-Albornoz, S. Montal-
vo, L. Chiruzzo, S. Collovini, Y. Gu-
ti´errez, S. M. J. Zafra, M. Krallinger,
M. Montes-y-G´omez, R. Ortega-Bueno,
and A. Ros´a, editors, Proceedings of the
Iberian Languages Evaluation Forum co-
located with 35th Conference of the Spa-
nish Society for Natural Language Pro-
cessing, IberLEF-SEPLN 2019, Bilbao,
Spain, September 24th, 2019, volume 2421
of CEUR Workshop Proceedings, pages
478–494. CEUR-WS.org.
Arag´on,
M.
E.,
H.
J.
Jarqu´ın-V´asquez,
M. Montes-y-G´omez, H. J. Escalante,
L. Villase˜nor-Pineda, H. G´omez-Adorno,
J. P. Posadas-Dur´an, and G. Bel-Enguix.
2020a.
Overview of MEX-A3T at iber-
lef 2020: Fake news and aggressiveness
analysis in mexican spanish. In M. ´A. G.
Cumbreras, J. Gonzalo, E. M. C´amara,
R. Mart´ınez-Unanue, P. Rosso, S. M. J.
Zafra, J. A. O. Zambrano, A. Miranda,
J. P. Zamorano, Y. Guti´errez, A. Ros´a,
M. Montes-y-G´omez, and M. G. Vega, edi-
tors, Proceedings of the Iberian Langua-
ges Evaluation Forum (IberLEF 2020) co-
located with 36th Conference of the Spa-
nish Society for Natural Language Pro-
Flor Miriam Plaza-del-Arco, Marco Casavantes, Hugo Jair Escalante, M. Teresa Martín-Valdivia,  
Arturo Montejo-Ráez, Manuel Montes-y-Gómez, Horacio Jarquín-Vásquez, Luis Villaseñor-Pineda
192

--- Page 11 ---

cessing (SEPLN 2020), M´alaga, Spain,
September 23th, 2020, volume 2664 of
CEUR Workshop Proceedings, pages 222–
235. CEUR-WS.org.
Arag´on, M., H. Jarqu´ın, M. M.-y. G´omez,
H.
Escalante,
L.
Villase˜nor-Pineda,
H. G´omez-Adorno, G. Bel-Enguix, and
J. Posadas-Dur´an.
2020b.
Overview
of mex-a3t at iberlef 2020: Fake news
and aggressiveness analysis in mexican
spanish.
In Notebook Papers of 2nd
SEPLN Workshop on Iberian Languages
Evaluation
Forum
(IberLEF),
Malaga,
Spain.
Aroyehun, S. T. and A. Gelbukh. 2021. Eva-
luation of intermediate pre-training for
the detection of oﬀensive language.
In
Proceedings of the Iberian Languages Eva-
luation Forum (IberLEF 2021), CEUR
Workshop Proceedings. CEUR-WS.org.
Calder´on, J. J., E. S. Tellez, and M. Graﬀ.
2021.
Dccd-infotec
at
meoﬀen-
des@iberlef21
subtask
3:
A
transfer
learning
approach
based
on
evomsa’s
stacked generalization.
In Proceedings
of
the
Iberian
Languages
Evaluation
Forum (IberLEF 2021), CEUR Workshop
Proceedings. CEUR-WS.org.
Canales, L. and P. Mart´ınez-Barco.
2014.
Emotion detection from text: A survey.
In Proceedings of the workshop on natu-
ral language processing in the 5th infor-
mation systems research working days (JI-
SIC), pages 37–43.
Ca˜nete, J., G. Chaperon, R. Fuentes, J.-H.
Ho, H. Kang, and J. P´erez. 2020. Spanish
pre-trained bert model and evaluation da-
ta. In PML4DC at ICLR 2020.
Chen, T. and C. Guestrin. 2016. XGBoost:
A scalable tree boosting system. In Pro-
ceedings of the 22nd ACM SIGKDD In-
ternational Conference on Knowledge Dis-
covery and Data Mining, KDD ’16, page
785–794, New York, NY, USA. Associa-
tion for Computing Machinery.
D´ıaz-Torres, M. J., P. A. Mor´an-M´endez,
L.
Villasenor-Pineda,
M.
Montes-y
G´omez, J. Aguilera, and L. Meneses-
Ler´ın.
2020.
Automatic detection of
oﬀensive language in social media: Deﬁ-
ning linguistic criteria to build a Mexican
Spanish dataset.
In Proceedings of the
Second Workshop on Trolling, Aggression
and Cyberbullying, pages 132–136, Mar-
seille, France, May. European Language
Resources Association (ELRA).
Garc´a-D´ıaz, J. A., S. M. Jim´enez-Zafra, and
R. Valencia-Garc´ıa.
2021.
Umuteam at
meoﬀendes 2021: Ensemble learning for of-
fensive language identiﬁcation using lin-
guistic features, ﬁne-grained negation and
transformers.
In Proceedings of the Ibe-
rian Languages Evaluation Forum (Iber-
LEF 2021), CEUR Workshop Procee-
dings. CEUR-WS.org.
Garc´ıa, M. N. and I. S. Bedmar. 2021. Detec-
ting oﬀensiveness in social network com-
ments. In Proceedings of the Iberian Lan-
guages Evaluation Forum (IberLEF 2021),
CEUR Workshop Proceedings. CEUR-
WS.org.
G´omez-Espinosa, V., V. Mu˜niz-Sanchez, and
A. P. L´opez-Monroy. 2021. Transformers
pipeline for oﬀensiveness detection in me-
xican spanish social media.
In Procee-
dings of the Iberian Languages Evaluation
Forum (IberLEF 2021), CEUR Workshop
Proceedings. CEUR-WS.org.
Grave, E., P. Bojanowski, P. Gupta, A. Jou-
lin, and T. Mikolov. 2018. Learning word
vectors for 157 languages. In Proceedings
of the International Conference on Lan-
guage Resources and Evaluation (LREC
2018), page .
Huerta-Velasco, D. A. and H. Calvo. 2021.
Using lexical resources for detecting of-
fensiveness in mexican spanish tweets. In
Proceedings of the Iberian Languages Eva-
luation Forum (IberLEF 2021), CEUR
Workshop Proceedings. CEUR-WS.org.
MacAvaney, S., H.-R. Yao, E. Yang, K. Rus-
sell, N. Goharian, and O. Frieder. 2019.
Hate speech detection: Challenges and so-
lutions. PloS one, 14(8):e0221152.
Medhat, W., A. Hassan, and H. Korashy.
2014. Sentiment analysis algorithms and
applications: A survey. Ain Shams engi-
neering journal, 5(4):1093–1113.
Montes, M., P. Rosso, J. Gonzalo, E. Arag´on,
R.
Agerri,
M.
´Alvarez
Carmona,
E.
´Alvarez
Mellado,
J.
Carrillo-de
Albornoz,
L.
Chiruzzo,
L.
Freitas,
H. G´omez Adorno, Y. Guti´errez, S. Lima,
Overview of MeOffendEs at IberLEF 2021: Offensive Language Detection in Spanish Variants
193

--- Page 12 ---

S. M. Jim´enez-Zafra, F. M. Plaza-del-
Arco, and M. Taul´e, editors.
2021.
Proceedings
of
the
Iberian
Languages
Evaluation Forum (IberLEF 2021).
Mubarak, H., K. Darwish, W. Magdy, T. El-
sayed, and H. Al-Khalifa.
2020.
Over-
view of osact4 arabic oﬀensive language
detection shared task. In Proceedings of
the 4th Workshop on Open-Source Arabic
Corpora and Processing Tools, with a Sha-
red Task on Oﬀensive Language Detection,
pages 48–52.
Plaza-del
Arco,
F.
M.,
M.
D.
Molina-
Gonz´alez, L. A. Ure˜na-L´opez, and M. T.
Mart´ın-Valdivia.
2021.
Comparing pre-
trained language models for spanish ha-
te speech detection. Expert Systems with
Applications, 166:114120.
Qu, S., Q. Que, and Shuangjun. 2021. Non-
contextual binary classiﬁcation for mexi-
can spanish with xlm and cnn. In Procee-
dings of the Iberian Languages Evaluation
Forum (IberLEF 2021), CEUR Workshop
Proceedings. CEUR-WS.org.
Qu, Y., Y. Yang, and G. Wang.
2021.
Ynu qyc at meoﬀendes@iberlef 2021:the
xlm-roberra and lstm for identifying of-
fensive tweets. In Proceedings of the Ibe-
rian Languages Evaluation Forum (Iber-
LEF 2021), CEUR Workshop Procee-
dings. CEUR-WS.org.
Razavi, A. H., D. Inkpen, S. Uritsky, and
S. Matwin.
2010.
Oﬀensive language
detection using multi-level classiﬁcation.
In A. Farzindar and V. Keˇselj, editors,
Advances in Artiﬁcial Intelligence, pages
16–27, Berlin, Heidelberg. Springer Berlin
Heidelberg.
S´anchez-Vega, F. and A. P. L´opez-Monroy.
2021.
Cimat-gto at meoﬀendes 2021:
Bert’s
auxiliary
sentence
focused
on
word’s information for oﬀensiveness detec-
tion. In Proceedings of the Iberian Lan-
guages Evaluation Forum (IberLEF 2021),
CEUR Workshop Proceedings. CEUR-
WS.org.
Sreelakshmi, K., B. Premjith, and K. P. So-
man.
2021.
Transformer based oﬀensi-
ve language identiﬁcation in spanish. In
Proceedings of the Iberian Languages Eva-
luation Forum (IberLEF 2021), CEUR
Workshop Proceedings. CEUR-WS.org.
Tang, E. K., P. N. Suganthan, and X. Yao.
2006. An analysis of diversity measures.
Mach. Learn., 65(1):247–271.
Twitter. 2021. Tweets – twitter developers.
https://developer.twitter.com/. Ac-
cessed: 2021-06-30.
Wiebe, J., T. Wilson, R. Bruce, M. Bell,
and M. Martin. 2004. Learning subjec-
tive language. Computational linguistics,
30(3):277–308.
Zampieri,
M.,
P.
Nakov,
S.
Rosenthal,
P. Atanasova, G. Karadzhov, H. Mubarak,
L. Derczynski, Z. Pitenis, and C¸. C¸¨oltekin.
2020. Semeval-2020 task 12: Multilingual
oﬀensive language identiﬁcation in social
media (oﬀenseval 2020).
arXiv preprint
arXiv:2006.07235.
Flor Miriam Plaza-del-Arco, Marco Casavantes, Hugo Jair Escalante, M. Teresa Martín-Valdivia,  
Arturo Montejo-Ráez, Manuel Montes-y-Gómez, Horacio Jarquín-Vásquez, Luis Villaseñor-Pineda
194

```
