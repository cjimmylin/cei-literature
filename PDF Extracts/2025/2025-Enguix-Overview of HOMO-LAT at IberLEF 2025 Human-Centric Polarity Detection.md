---
title: "2025-Enguix-Overview of HOMO-LAT at IberLEF 2025 Human-Centric Polarity Detection - PDF Extract"
source_pdf: "2025-Enguix-Overview of HOMO-LAT at IberLEF 2025 Human-Centric Polarity Detection.pdf"
pages: 12
extracted_at: "2026-02-13T22:58:56.799201"
---

# PDF Extract: 2025-Enguix-Overview of HOMO-LAT at IberLEF 2025 Human-Centric Polarity Detection

**Source PDF:** 2025-Enguix-Overview of HOMO-LAT at IberLEF 2025 Human-Centric Polarity Detection.pdf
**Total Pages:** 12

---

## Content

```
--- Page 1 ---

Overview of HOMO-LAT at IberLEF 2025:
Human-centric polarity detection in Online Messages
Oriented to the Latin American-speaking LGBTQ+
populaTion
Sinopsis de HOMO-LAT en IberLEF 2025: Detecci´on de
polaridad centrada en lo humano en mensajes en l´ınea
orientados a la poblaci´on LGBTQ+ de habla latinoamericana
Gemma Bel-Enguix,1,3 Helena G´omez-Adorno,2 Sergio Ojeda-Trueba,1 
Gerardo Sierra,1,3 Jessica Barco,1 Edgar Lee-Romero,1
Jocelyn Dunstan,4 Ruben Manrique5
1Instituto de Ingenier´ıa, Universidad Nacional Aut´onoma de M´exico
2Instituto de Investigaciones en Matem´aticas Aplicadas y Sistemas, Universidad 
Nacional Aut´onoma de M´exico
3Insituto de Investigaciones Bibliogr´aficas, Universidad Nacional Aut´onoma de M´exico 
4Departamento de Ciencia de la Computaci´on e Instituto de Ingenier´ıa Matem´atica
y Computacional, Pontificia Universidad Cat´olica de Chile.
5Departamento de Ingenier´ıa de Sistemas y Computaci´on, Universidad de los Andes
{gbele, gsierram, sojedat}@iingen.unam.mx, helena.gomez@iimas.unam.mx,
{jessbarco13,edgar.lee133}@gmail.com, rf.manrique@uniandes.edu.co, jdunstan@uc.cl
Abstract: This paper presents the HOMO-LAT shared task organized at IberLEF
2025, as part of the 41st International Conference of the Spanish Society for Natural
Language Processing (SEPLN 2025). Our goal is to foster the design of algorithms
capable of capturing the polarity of Reddit comments on keywords referring to the
LGBTQ+ community. HOMO-LAT is a continuation of the past tasks HOMO-MEX
2023 and 2024, with the particularity of including posts from 19 Spanish-speaking
Latin American countries. The shared task consisted of two tracks. In Track 1,
the test data corresponded to the same subreddits as the training data. Track 2 is
cross-lingual, since the test data belonged to different countries from the training
data. Six teams participated in the evaluation phase. Regarding the approaches
chosen by the participants, all of them used models based on Transformers. Two of
them also worked with traditional ML, and two more used LLMs.
Keywords: Polarity analysis, Hate speech, LGBTQ+ community, Reddit corpus.
Resumen: En este art´ıculo presenta la tarea compartida HOMO-LAT organizada
en IberLEF 2025, como parte de la 41 International Conference of the Spanish So-
ciety for Natural Language Processing (SEPLN 2025). El objetivo de esta tarea es
fomentar el dise˜no de algoritmos capaces de capturar la polaridad de los comentarios
de Reddit sobre palabras clave referidas a la comunidad LGBTQ+. HOMO-LAT es
una continuaci´on de HOMO-MEX 2023 y 2024, con la particularidad de que incluye
mensajes de 19 pa´ıses latinoamericanos de habla hispana. La tarea compartida ha
constado de dos tracks. En el Track 1 los datos de test correspond´ıan a los mismos
subredits que los datos de entrenamiento. El Track 2 es multivariante, ya que los
datos de test pertenec´ıan a pa´ıses diferentes que los datos de entrenamiento. En
la fase de evaluaci´on participaron seis equipos, cuyos resultados se analizan en el
art´ıculo. Por lo que respecta a las aproximaciones elegidas por los participantes, to-
dos ellos usaron modelos basados en Transformers. Dos de ellos trabajaron tambi´en
con ML tradicional y dos m´as usaron LLMs.
Palabras clave: An´alisis de polaridad, Detecci´on e lenguaje de odio, Comunidad
LGBTQ+, Corpus de Reddit.
Procesamiento del Lenguaje Natural, Revista nº 75, septiembre de 2025, pp. 413-424 recibido 03-07-2025 revisado 18-07-2025 aceptado 01-08-2025
ISSN 1135-5948 DOI 10.26342/2025-75-30
©2025 Sociedad Española para el Procesamiento del Lenguaje Natural

--- Page 2 ---

1
Introduction
Monique Wittig Wittig (1980) asserted that
heterosexuality is a political system that per-
meates all aspects of Western societies.
It
divides the population into two binary and
opposing groups separated by gender. Each
of these groups has pre-established roles and
behaviours, which shape the personality of
an individual who has to comply with the
norms set by this ‘stright regime’ (Wittig,
1979) according to a network of ‘gender’ re-
lations (Butler, 2011).
This whole ideological package that con-
structs society has made the normalisation of
non-heteronormative sex-gender definitions
very difficult, even in societies with advanced
legislation. Social media, on the other hand,
have served as a loudspeaker for some po-
sitions that support heterornormative posi-
tions and spread hate speech towards the
LGBTQ+ community (Chakravarthi et al.,
2024), making this community one of the
most vulnerable to hate speech on social net-
works (D´ıaz-Torres et al., 2020).
Efforts have been made in the NLP com-
munity to automatically identify homopho-
bia.
To address the issue, some works use
deep learning and transformer-based mod-
els, such as Manikandan, Subramanian, y
Shanmugavadivel (2022), Li et al.
(2024),
Sosto y Barr´on-Cede˜no (2024), and Felkner
et al.
(2023).
Other authors have focused
on the development of annotated corpora
for the evaluation of detection models.
To
test the efficiency of the models and the re-
sources, several shared tasks have been or-
ganized in different forums. HODI (Nozza et
al., 2023) is an event that specializes in homo-
transphobia identification in Italian. A series
of shared tasks on multilingual homophobia
and transphobia detection in social networks
Chakravarthi et al. (2022; Chakravarthi et
al. (2023; Chakravarthi et al. (2024) have
been organized in the framework of the Work-
shop on Language Technology for Equality,
Diversity and Inclusion.
Some efforts have centered only in low-
resourced languages.
Kumaresan et al.
(2023) present a work on Homophobia and
transphobia for Malayan and Hindi. In this
sense, the shared tasks Homo-Mex 2023 (Bel-
Enguix et al., 2023) and HOMO-MEX 2024
(G´omez-Adorno et al., 2024) have focused on
automatic detection of LGBTphobia in Span-
ish on social networks.
The Homo-Mex tasks have been continued
with the HOMO-LAT initiative, a joint effort
by researchers from different Latin American
countries to study society’s perception of the
LGBTQ+ community.
The central idea is approaching LGBT-
phobia in its different ideological and linguis-
tic manifestations in countries that share the
same language on the same continent.
We have focused on exploring the use
of LGBTQ+ language in social networks,
specifically Reddit, considering subreddits
from all Spanish-speaking countries in Amer-
ica. In this way, the different social positions
towards the LGBTQ+ community can be ad-
dressed.
The HOMO-LAT 2025 shared task pro-
poses a polarity analysis with respect to a set
of generic terms used in all Latin American
countries. It targets a diverse community of
users and offers significant industrial applica-
tions. Academics and researchers in NLP and
computational linguistics benefit from these
tasks by advancing sentiment analysis meth-
ods while addressing cultural and linguistic
nuances specific to Spanish dialects in Latin
America. LGBTQ+ advocacy groups and or-
ganizations can use these tools to monitor
harmful language or sentiment in online dis-
course, promoting inclusivity and combating
discrimination.
Additionally, policymakers
and regulators can use such systems to iden-
tify and address hate speech, fostering safer
digital spaces.
Industrially, polarity detection has wide-
ranging applications.
Social media plat-
forms can integrate these models to enhance
content moderation, flagging and mitigating
LGBTQ+ phobic or harmful content.
The
marketing and advertising sectors can use
sentiment analysis to develop culturally sen-
sitive campaigns tailored to LGBTQ+ audi-
ences, ensuring positive engagement.
Fur-
thermore, public relations teams and media
organizations can use these tools for social
listening and sentiment monitoring around
LGBTQ+ issues, enabling more informed re-
sponses to public opinion and societal trends.
The task is addressed to the whole com-
munity of Latin American researchers and
industry practitioners who can additionally
study and adapt their applications to differ-
ent variants of Spanish on the continent.
The Homo-Lat corpus has been a chal-
lenge for data collection and labeling.
On
Gemma Bel-Enguix, H. Gómez-Adorno, Sergio Ojeda-Trueba, Gerardo Sierra, Jessica Barco, Edgar Lee-Romero, Jocelyn Dunstan, R. Manrique
414

--- Page 3 ---

this occasion, and in contrast to Homo-Mex
tasks, we have not focused on the detection
of LGBTphobia in general. In order to build
the corpus, we used the social network Red-
dit, especially the subreddits of each of the
19 countries taken into consideration.
The
diversity of specific vocabulary to refer to the
community among the different countries led
us to search for a basic set of neutral terms
(homosexual, lesbian, bisexual, etc.) and to
tag the entire messages considering the po-
larity regarding the target term.
The shared task consists of two tracks fo-
cused on polarity detection towards LGBT+
keywords in Reddit posts. In Track 1 (multi-
dialect polarity detection), participants are
required to assign a single polarity label (pos-
itive, negative, or neutral) to each post with
respect to a given keyword. Both the train-
ing and evaluation data come from the same
Spanish dialects: Argentina, Chile, Colom-
bia, and Mexico. In Track 2 (cross-dialect po-
larity detection), models are trained on data
from those four countries but evaluated on
posts from previously unseen dialects, includ-
ing countries such as Bolivia, Peru, Uruguay,
and the Dominican Republic.
The task involved a total of 30 registered
participants, who ended up in 7 groups that
submitted evaluable results, and six teams
that have written their papers to share their
methods with the scientific community.
Homo-Lat25 is part of the IberLEF forum
(Gonz´alez-Barba, Chiruzzo, y Jim´enez-Zafra,
2025; Jim´enez-Zafra et al., 2025), which will
be held in Zaragoza in September 2025.
The paper is structured as follows. Sec-
tion 2 explains the configuration and anno-
tation of the corpus.
Section 3 introduces
the different approaches used by the groups.
An experimental evaluation and analysis of
the results is presented in Section 4. Finally,
Section 5 is devoted to conclusions and the
future of HOMO-LAT.
2
Homo-LAT 2025 Corpus and
Evaluation Framework
2.1
Compilation of the Corpus
The construction of the HOMOLAT-25 cor-
pus involved selecting nouns that represent
general LGBTQ + terminology applicable to
all selected Latin American countries. Gram-
matical variations—such as plural forms and
accent marks—were also considered. The se-
lected terms comprised the following identity
terms, alphabetically ordered:
• Asexual/es
• Bisexual/es
• Gay/gays
• Intersexual/es
• Lesbiana/as
• LGBT
• Pansexual/es
• Queer/s
• Trans
• Transexual/les
• Transg´enero
• Travesti/is
Using Reddit’s API, posts from country-
specific subreddits were extracted, yielding
20,215 unique posts.
The
dataset
included
Spanish-written
posts from 19 Latin American countries. The
full list of countries is as follows:
• Argentina
• Bolivia
• Chile
• Colombia
• Costa Rica
• Cuba
• Dominican Re-
public
• Ecuador
• El Salvador
• Guatemala
• Honduras
• Mexico
• Nicaragua
• Panama
• Paraguay
• Peru
• Puerto Rico
• Uruguay
• Venezuela
A cleaning process ensured the data met
the task’s requirements.
The data cleaning requirements included
removing:
1. Duplicated posts
2. Posts containing only titles (no body
text)
3. Bot-generated posts
4. Posts consisting exclusively of URLs
Additionally, we included posts contain-
ing at the same time the terms trans and
grasas/graso in our removal criteria to elim-
inate unrelated content.
After the cleaning process, the total num-
ber of posts in the corpus is 16,273, as can be
seen in Table 1. From these posts, 7,210 be-
long to Argentina, Mexico, Chile, and Colom-
bia.
These represent 70% of the collected
data.
The training and development sets
were taken from that group of countries with
the highest number of messages. For Track
1, the test set belonged to the same group of
countries. For Track 2, the test set consisted
of the posts from the other countries. The
number of posts for each subset is shown in
Table 2.
Overview of HOMO-LAT at IberLEF 2025: Human-centric polarity detection in Online Messages Oriented to the Latin American-speaking 
LGBTQ+ populaTion
415

--- Page 4 ---

Country
Number of Posts
Argentina
3,724
Chile
2,343
Mexico
2,824
Colombia
1,907
Uruguay
1,770
Panama
1,058
Peru
580
Paraguay
541
Puerto Rico
378
Guatemala
376
Venezuela
232
Honduras
154
El Salvador
100
Dominican Republic
100
Nicaragua
69
Bolivia
49
Ecuador
46
Costa Rica
17
Cuba
5
Total
16,273
Table 1: Number of posts by country.
Phase
Number of Posts
Training (Train)
5,767
Development (Dev)
1,443
Test Track 1
3,588
Test Track 2
5,475
Table 2: Distribution of Posts.
2.2
Annotation and
Interannotator Agreement
The annotation of the corpus HOMOLAT is
a challenge due to the geographical diversity
of the posts.
The messages were annotated with three
polarity values: POS, NEG, NEU. We pre-
sented the posts with a selected keyword, e.g.
gay, although it could contain more words
from our lexicon. For example, given a post
with the words gay, lesbian, and asexual, only
one was highlighted as the keyword.
We
asked the annotators to focus on the polarity
of the post with respect to this word selected
as a keyword.
The work was carried out with volunteer
or social service students. As the corpus has
been built in Mexico, there were no issues in
recruiting Mexican annotators. In the cases
of Argentina, Chile, and Colombia, which
are the countries, besides Mexico, with the
largest number of messages, a recruitment
process was carried out to ensure the pres-
ence of students of these nationalities in the
labeling.
The recruitment process and assignment
to a dataset aimed to ensure representation of
LGBT identities, gender, sex, and nationality
in all labeling activities. Therefore, we main-
tained a balance between annotators who are
part of the LGBTQ+ community and those
who are not, as well as between male and fe-
male. All teams included representation from
each of these groups.
This approach is determined by the partic-
ularities of our subject, where variability in
language expression, ascription to the LGBT
community, as well as social and cultural
differences between countries plays a critical
role in understanding what a user means on
their Reddit publications.
To mitigate the possible problems in the
annotation, we selected only general words,
such as homosexual, which can usually be
found in neuter contexts. We avoided words
with different meanings in different countries,
as well as dialectal specificities (e.g. arepa)
The proportion of publications in each
subreddit leads to modularization in the la-
beling process, starting with the countries
where the subreddits contained the highest
number of publications.
In our case, these
were Argentina, Mexico, Chile, and Colom-
bia.
Due to the volume of posts in the sub-
reddits from Argentina, Chile, and Colombia,
efforts were made to recruit volunteers from
those countries who also matched a specific
demographic for labeling.
After contacting
a handful of volunteers who agreed to sup-
port our project, the remaining gaps in cer-
tain groups were filled with Mexican annota-
tors.
While the four countries with the great-
est number of publications were labeled af-
ter considering and recruiting native people
from each nation while prioritizing their de-
mographic profile, it was not practical to con-
tinue with the same approach for the rest of
the countries in Latin America. For example,
there were five publications in the Cuba sub-
reddit that contained keywords related to the
LGBT community. However, it was neither
practical nor easy to recruit someone from
Cuba who matched the country’s culture and
demographics for just a few publications. Be-
Gemma Bel-Enguix, H. Gómez-Adorno, Sergio Ojeda-Trueba, Gerardo Sierra, Jessica Barco, Edgar Lee-Romero, Jocelyn Dunstan, R. Manrique
416

--- Page 5 ---

cause of this, we decided to continue using
Mexican annotators instead.
We
continued
with
this
strategy
for
the following countries:
Panama,
Peru,
Paraguay,
Puerto
Rico,
Guatemala,
Venezuela,
Honduras,
El
Salvador,
the
Dominican Republic, Bolivia, Cuba, and
Uruguay. Instead of focusing on individual
nations—as we had done previously with
Argentina, Colombia, Chile, and Mexico, we
compiled all publications into a single corpus
for labeling, creating one unified dataset.
Lastly, if any inconsistency between labels
was detected, such as a dissent, we consulted
annotators who had not participated in prior
activities, ensuring they could label publica-
tions without influence from previous anal-
yses. These individuals were senior annota-
tors, already familiar with the task, and their
role was to resolve disagreements.
While
their task was not as extensive as the first an-
notators, it proved crucial for difficult cases.
Country
Neg.
Neu.
Pos.
Argentina
1544
1844
336
Uruguay
570
759
441
Mexico
927
1572
325
Chile
462
1707
174
Colombia
485
1221
201
Panama
239
762
57
Peru
126
424
30
Paraguay
124
391
26
Guatemala
74
281
21
Venezuela
73
141
18
Puerto Rico
72
281
25
Honduras
22
120
12
El Salvador
20
76
4
Nicaragua
10
50
9
Dom. Rep.
11
86
3
Ecuador
1
40
5
Bolivia
4
43
2
Costa Rica
1
15
1
Cuba
0
4
1
Table 3: Compact Sentiment Distribution by
Country.
During the labeling of the publications, we
faced a number of challenges that went be-
yond borders and cultural differences in Latin
America. For example, names. In Argentina,
we faced a number of extraordinary cases,
such as a politician named Alfonso Prat-Gay.
In the cleaning phase, these cases were never
addressed because they were written in dif-
ferent ways; sometimes they only referred to
him as Prat Gay, Gay, or Alfonso Gay. But
ultimately, these cases were dismissed for not
being related to our study.
Additionally, some words used by the au-
thors of the publications were classified as
keywords despite having no relation to our
study, such as “trans atlantico” and “grasas
trans”, this could be the result of grammat-
ical errors or syntactical mistakes in their
writing or an unnoticed case during the clean-
ing phase.
One observation made by the annotators
was that, in general, during the last labeling
activity focusing on the rest of Latin Amer-
ica countries, the messages contained more
aggressive statements while also having fewer
publications. At one point, one of the volun-
teers decided to no longer participate in the
activity because he felt personally attacked
and couldn’t continue. This contrasts with
the cases of Argentina, Mexico, Colombia,
and Chile, where, while there were comments
with LGBTQ+phobic rhetoric, they weren’t
at the same level of intensity, bigotry, or hate.
The difference was palpable.
After the annotation process, we achieved
the results that are shown in Table 3. The
most common label was NEU, while the num-
ber of positive instances was notably lower.
Table 4 shows the distribution in the train,
development, and test sets.
An analysis of inter-annotator agreement
yields very poor results (see table 5). There
are two reasons for this. The first is the in-
trinsic subjectivity of the task, which is also
reflected in the results obtained by the teams.
The second is that the corpus was segmented
into many fragments for labeling. Therefore,
more than 20 different annotators were in-
volved.
3
Overview of the Submitted
Approaches
Six teams participated in this shared task,
with most participants working in both
tracks. Table 6 shows the approaches of each
of the teams for the two tracks.
In
terms
of
the
approaches
utilized,
team PLD (Olivert-Iserte, Caballero-Garc´ıa-
Alcaide, y Guijarro-Mart´ınez, 2025) used the
pre-trained transformer model RoBERTa to
calculate embeddings that were then used as
inputs in four classification models: a base-
line using machine learning (random forest
Overview of HOMO-LAT at IberLEF 2025: Human-centric polarity detection in Online Messages Oriented to the Latin American-speaking 
LGBTQ+ populaTion
417

--- Page 6 ---

Set
Pos
Neg
Neu
Total
Train
633 (11%)
1960 (34%)
3174 (55%)
5767
Dev
80 (6%)
475 (33%)
888 (62%)
1443
Track 1
323 (9%)
983 (27%)
2282 (64%)
3588
Track 2
655 (12%)
1347 (25%)
3473 (63%)
5475
Table 4: Label Distribution.
Metric
Train
Test
Annotator 1/2
0.133
0.318
Annotator 1/3
0.088
0.182
Annotator 2/3
0.153
0.137
Fleiss’ κ
0.124
0.158
Table 5: Inter-annotator Agreement.
Team
Traditional ML
LLM Prompting
Single Transformer
PLD
X
X
HomoCIC
X
X
CogniCIC
X
X
INFOTEC-NLP
X
SINAI-UGPLN
X
X
UC-UCO-CICESE UT3
X
Table 6: General approach of each partici-
pating team for all tasks.
and support vector machines); LLM prompt-
ing (GPT-4o-mini), BERT Fine-Tuning with
Paraphrase Ensemble, and Context-Based
BERT with Multi-Head Attention. In addi-
tion, this team used GPT-4o-mini for data
augmentation.
For the pre-processing, the
team removed URLs, mentions, markdown,
and extra whitespace, and all the text was
translated into English.
The team led by Cardaso-Moreno (Homo-
CIC) (Cardoso-Moreno et al., 2025) tack-
led the polarity detection task by combin-
ing retrieval-augmented classification with
transformer-based embeddings and a vector
database, using as an embedding layer the
pre-trained transformer-based model BETO
and Amazon’s Titan Text Embeddings V2,
and for the classification strategy, k-nearest
neighbors (k-nn) enhanced by country and
keyword filtering to address regional lan-
guage variation.
For the pre-processing,
URLs, markdown, quote markers, list pre-
fixes, separator lines, and sarcasm tags were
removed.
A
similar
use
of
BETO
plus
k-nn
was adopted by CogniCIC (Macias et al.,
2025), where the embeddings were stored in
OpenSearch and classified via k-nn with co-
sine similarity, applying additional filters by
country and LGBTQ+ keyword to account
for dialectal and contextual variation.
An-
other characteristic of this plan was that in-
stead of using the [CLS] token embedding,
they applied mean pooling over the attention
layers.
A common scheme for classification is
used by the teams INFOTEC-NLP, SINAI-
UGPLN
and
UC-UCO-CICESE UT3-
Plenitas
(Ruiz
et
al.,
2025;
Toapanta-
Bernab´e et al., 2025;
Mart´ınez-L´opez et
al., 2025) was a classification head, which
means that the final part of the model
has a layer of the size of the number of
classes that takes internal feature represen-
tations of the network and converts them
into probabilities.
The differences among
the
teams
are
the
embedding
strategy,
with (Toapanta-Bernab´e et al., 2025) us-
ing pre-trained models (RoBERTuito and
MarIA)(Macias et al., 2025) BETO, and
(Ruiz et al., 2025) employing the pre-trained
model BIMALAT (an existing RoBERTa-
based language model trained on 600 million
Latin American Spanish tweets). Moreover,
(Toapanta-Bernab´e et al., 2025) addressed
class and dialect imbalance by generating
400 synthetic examples using Mistral-7B and
Falcon-7B, and a dynamic input encoding
strategy was applied based on metadata
availability.
4
Experimental Evaluation and
Analysis of the Results
This section presents an overview of the re-
sults obtained by participants in the shared
task. The analysis focuses on evaluating and
comparing the performance of the submit-
ted systems on the test set, using the macro
F1-score as the primary evaluation metric.
Gemma Bel-Enguix, H. Gómez-Adorno, Sergio Ojeda-Trueba, Gerardo Sierra, Jessica Barco, Edgar Lee-Romero, Jocelyn Dunstan, R. Manrique
418

--- Page 7 ---

This metric was chosen because it provides
a balanced assessment of precision and recall
across all classes, making it particularly ap-
propriate for multi-class classification tasks
involving highly imbalanced data, as is the
case in this shared task.
To simplify the management of the shared
task workflow and ensure consistent evalua-
tion of all submissions, we employed the Cod-
abench platform1. This platform facilitated
the automation of performance metric com-
putation and submission handling through-
out the competition.
As
a
baseline
for
our
shared
task,
we
implemented
a
BERT-based
model
pretrained
for
Spanish,
specifically
the
bert-base-spanish-wwm-cased
model
(BETO) (Ca˜nete et al., 2020).
The model
was fine-tuned on the training dataset of
track 1 using the HuggingFace Transformers
library. No text pre-processing was applied
beyond standard tokenization with a maxi-
mum padding strategy. We used a standard
training configuration with a batch size of 8,
and the model was trained for 3 epochs. We
used the same baseline model to perform the
predictions on the test dataset of track 1 and
track 2. This baseline serves as a reference
point to evaluate the performance of the
participating systems.
Table 7 provides a summary of the results
obtained by each team in track 1 ((multi-
dialect polarity detection).
It includes the
evaluation metrics in descending order of
F1-score.
In this edition of the HOMO-
LAT shared task, the PLD team (Olivert-
Iserte, Caballero-Garc´ıa-Alcaide, y Guijarro-
Mart´ınez, 2025) achieved the best overall per-
formance, outperforming all other participat-
ing systems. Most of the teams outperformed
the baseline, except for 1 team.
The results for track 2 of the HOMO-LAT
shared task are presented in Table 8, which
summarizes the performance of each partic-
ipating team alongside our baseline model.
This track aimed to identify the polarity cat-
egories of posts originating from countries
that were not represented in the training
data, thereby assessing the generalization ca-
pabilities of the models.
Once again, the
PLD team (Olivert-Iserte, Caballero-Garc´ıa-
Alcaide, y Guijarro-Mart´ınez, 2025) achieved
the highest performance, outperforming all
1https://www.codabench.org/competitions/
5613/
other participants.
The decline in scores across all teams in
Track 2 highlights the increased challenge
posed by domain and dialect shift, as the
evaluation data included dialects unseen dur-
ing training. These results emphasize the im-
portance of robust generalization across di-
alectal variation in sentiment analysis tasks
and confirm that systems still face limitations
when transferring polarity detection capabil-
ities to unseen linguistic varieties.
4.1
Statistical Analysis
For the evaluation of the results obtained by
the participating teams, we employed Comp-
Stats (Nava-Mu˜noz, Graff Guerrero, y Es-
calante, 2023), a Python library specifically
designed for the statistical comparison of sys-
tem performance in shared tasks. This tool
allows for robust estimation of performance
intervals and comparison against the top-
performing systems.
Figure 1 displays the macro F1-scores ob-
tained by each team in track 1.
The PLD
system achieved the highest score, followed
by SINAI-UGPLN and INFOTEC. Other
teams, including CogniCIC, HomoCIC, and
the baseline, obtained lower scores, while UC-
UCO-CICESE UT3 reported the lowest per-
formance in this track.
In track 2 (Figure 2), PLD once again
reached the highest macro F1-score. It was
closely followed by SINAI-UGPLN and IN-
FOTEC, which also demonstrated compet-
itive results.
HomoCIC and CogniCIC ob-
tained mid-range scores, and the baseline
and UC-UCO-CICESE UT3 remained at the
lower end of the rank.
The CompStats library also provides a vi-
sual representation of the performance gap
between each submitted approach and the
best-performing system, based on macro F1-
score. These plots include confidence inter-
vals and statistical significance indicators, al-
lowing us to distinguish between models with
similar performance and those with meaning-
ful performance gaps.
In track 1, the PLD system was the best-
performing approach.
As shown in Fig-
ure 3, systems from SINAI-UGPLN and IN-
FOTEC showed the smallest differences with
respect to PLD, and their confidence inter-
vals suggest that their performance was not
significantly worse. In contrast, other teams
such as HomoCIC, CogniCIC, and the base-
Overview of HOMO-LAT at IberLEF 2025: Human-centric polarity detection in Online Messages Oriented to the Latin American-speaking 
LGBTQ+ populaTion
419

--- Page 8 ---

Team name
F1-score
Precision
Recall
PLD
0.5296
0.5354
0.5697
SINAI-UGPLN
0.5261
0.5327
0.5232
INFOTEC
0.5137
0.5083
0.5242
HomoCIC
0.4661
0.4762
0.4642
CogniCIC
0.4301
0.5427
0.4360
Baseline
0.3800
0.4069
0.3627
UC-UCO-CICESE UT3-Plenitas
0.2592
0.2120
0.3333
Table 7: Result summary for the HOMO-LAT shared task on track 1 - multi-dialect polarity
detection.
Team name
F1-score
Precision
Recall
PLD
0.5086
0.5076
0.5155
SINAI-UGPLN
0.4803
0.4820
0.4867
Infotec
0.4639
0.4899
0.4655
CogniCIC
0.4054
0.4677
0.4337
HomoCIC
0.3622
0.3688
0.3738
Baseline
0.3412
0.3953
0.3359
UC-UCO-CICESE UT3-Plenitas
0.2588
0.2114
0.3333
Table 8: Result summary for the HOMO-LAT shared task on track 2 - cross-dialect polarity
detection.
Figure 1: Classification metrics obtained in
track 1.
Figure 2: Classification metrics obtained in
track 2.
line exhibited larger differences, while UC-
UCO-CICESE UT3 displayed the most pro-
nounced gap.
Similarly, Figure 4 presents the differences
in track 2, again taking PLD as the refer-
ence. As in track 1, SINAI-UGPLN and IN-
FOTEC showed only minor differences from
PLD, while HomoCIC and CogniCIC ranked
in the mid-range.
The baseline and UC-
UCO-CICESE UT3 once more appeared at
the bottom, with the largest performance dif-
ferences.
4.2
Maximum Possible Accuracy
and Coincident Failure
Diversity
To evaluate the complementarity and vari-
ability among the participants’ predictions,
we employ two metrics:
Maximum Possi-
ble Accuracy (MPA) and Coincident Failure
Diversity (CFD) (Tang, Suganthan, y Yao,
2006; Kuncheva y Whitaker, 2003).
MPA
quantifies the upper bound of classification
performance by computing the proportion of
instances for which at least one system pro-
duced the correct label.
This allows us to
identify how many instances were misclassi-
Gemma Bel-Enguix, H. Gómez-Adorno, Sergio Ojeda-Trueba, Gerardo Sierra, Jessica Barco, Edgar Lee-Romero, Jocelyn Dunstan, R. Manrique
420

--- Page 9 ---

Figure
3:
Difference
in
performance
for
track 1.
Figure
4:
Difference
in
performance
for
track 2.
Approach
Best
accuracy
MPA
CFD
Number
of systems
All teams
0.6415
0.939
0.924
6
Transformers
0.6415
0.928
0.905
4
Traditional ML
0.6154
0.732
0.491
2
Table 9: MPA and CFD comparison results among the different proposed approaches for track 1.
fied by all systems.
Meanwhile, CFD cap-
tures the diversity in prediction errors among
the systems.
It ranges from 0 to 1, where
a value of 0 indicates that all systems be-
have similarly—either always correct or al-
ways incorrect—while a value closer to 1 im-
plies that errors are distributed more inde-
pendently across systems, reflecting high fail-
ure diversity.
The results of the MPA and CFD met-
rics are summarized in Table 9, where the
systems are grouped according to the general
approach used by each team, as outlined in
Table 6. We define three groups: All Teams,
which includes all six participating systems;
Transformers, which includes four teams that
adopted a transformer-based architecture (ei-
ther through single models or prompting);
and Traditional ML, which includes the two
teams that used classical machine learning
models without transformers.
5
Conclusion
All groups achieved relatively high MPA val-
ues, with the All Teams ensemble reach-
ing a maximum possible accuracy of 0.939.
The Transformer-based group also showed
strong complementarity with an MPA of
0.928,
while
the
Traditional
ML
group
reached an MPA of 0.732.
This suggests
that transformer-based systems are generally
more effective at covering different portions
of the input space.
Regarding diversity, the CFD scores in-
dicate that transformer systems also exhib-
ited more varied error patterns (CFD =
0.905) than traditional ML systems (CFD
=
0.491),
reflecting
lower
error
overlap
among transformer-based models. The com-
bined group of all teams showed the high-
est CFD (0.924), indicating potential bene-
fits of system combination across modeling
paradigms. These findings support the no-
tion that transformer-based systems not only
achieve stronger individual performance but
also complement each other better when con-
sidered as an ensemble.
This shared task explored the challenges
of polarity detection toward LGBT+ con-
tent in Spanish Reddit posts, focusing on
the sociolinguistic diversity of Latin Amer-
ican dialects.
The task was divided into
two tracks: Track 1 assessed models under
dialect-matched conditions, while Track 2 in-
troduced a cross-dialect generalization sce-
nario.
Across both settings, models were
Overview of HOMO-LAT at IberLEF 2025: Human-centric polarity detection in Online Messages Oriented to the Latin American-speaking 
LGBTQ+ populaTion
421

--- Page 10 ---

evaluated on their ability to assign positive,
negative, or neutral polarity to posts contain-
ing a controlled set of LGBT+ keywords.
The results highlight two key findings.
First, the results reveal modest overall per-
formance across systems,
with F1-scores
peaking at 0.53 in Track 1 and 0.51 in Track
2.
Second, performance dropped notably
in the cross-dialect scenario (Track 2), with
all systems showing reduced F1-scores, pre-
cision, and recall. These results demonstrate
the difficulty of transferring sentiment knowl-
edge across dialects.
Overall, the task emphasizes the impor-
tance of dialect-aware modeling in sentiment
analysis and the need for methods that can
better generalize across underrepresented lin-
guistic varieties. The benchmark provides a
valuable foundation for future work on inclu-
sive and robust NLP systems for the Spanish-
speaking LGBT+ community.
Aknowledgments
This paper has been partially supported
by
CONAHCYT
CF-2023-G-64
and
by
DGAPA-UNAM PAPIIT projects IN104424
and IG400325.
References
Bel-Enguix, G., H. G´omez-Adorno, G. Sierra,
J. V´asquez, S. T. Andersen, y S. Ojeda-
Trueba.
2023.
Overview of homo-mex
at iberlef 2023:
Hate speech detection
in online messages directed towards the
mexican spanish speaking lgbtq+ popula-
tion. Procesamiento del Lenguaje Natural,
71(0):361–370.
Butler, J. 2011. Bodies that matter: On the
discursive limits of sex. routledge.
Cardoso-Moreno, M., L. Moreno-Mendieta,
D.
Jim´enez,
J.
A.
Torres-Le´on,
y
J. Valdez-Rodr´ıguez.
2025.
Homocic at
homolat25: Retrieval augmented classifi-
cation using transformer architectures and
vector knowledgebases. En Proceedings of
the Iberian Languages Evaluation Forum
(IberLEF 2025), co-located with the 41st
Conference of the Spanish Society for Nat-
ural Language Processing (SEPLN 2025),
CEUR-WS.org.
Ca˜nete, J., G. Chaperon, R. Fuentes, J.-H.
Ho, H. Kang, y J. P´erez.
2020.
Span-
ish pre-trained bert model and evaluation
data. En PML4DC at ICLR 2020.
Chakravarthi, B., P. Kumaresan, R. Priyad-
harshini,
P.
Buitelaar,
A.
Hegde,
H. Shashirekha, S. Rajiakodi, M. Garc´ıa-
Cumbreras, S. Jim´enez-Zafra, J. Garc´ıa-
D´ıaz, R. Valencia-Garc´ıa, K. Ponnusamy,
P. Shetty, y D. Garc´ıa-Baena.
2024.
Overview of third shared task on ho-
mophobia and transphobia detection in
social media comments. En Proceedings of
the Fourth Workshop on Language Tech-
nology for Equality, Diversity, Inclusion,
p´aginas 124–132.
Chakravarthi,
B.
R.,
R.
Ponnusamy,
P. Buitelaar, M. ´A. Garc´ıa-Cumbreras,
S. M. Jim´enez-Zafra, J. A. Garc´ıa-D´ıaz,
R. Valencia-Garc´ıa, N. Jindal, y others.
2023. Overview of second shared task on
homophobia and transphobia detection in
social media comments.
En Proceedings
of
the
Third
Workshop
on
Language
Technology for Equality, Diversity and
Inclusion, p´aginas 38–46.
Chakravarthi,
B.
R.,
R.
Priyadharshini,
T. Durairaj, J. McCrae, P. Buitelaar,
P. Kumaresan, y R. Ponnusamy.
2022.
Overview of the shared task on homopho-
bia and transphobia detection in social
media comments. En B. R. Chakravarthi
B. Bharathi J. P. McCrae M. Zarrouk
K. Bali, y P. Buitelaar, editores, Proceed-
ings of the Second Workshop on Language
Technology for Equality, Diversity and In-
clusion, p´aginas 369–377, Dublin, Ireland,
Mayo. Association for Computational Lin-
guistics.
D´ıaz-Torres, M. J., P. A. Mor´an-M´endez,
L.
Villasenor-Pineda,
M.
Montes-y
G´omez, J. Aguilera, y L. Meneses-Ler´ın.
2020.
Automatic detection of offen-
sive language in social media:
Defining
linguistic criteria to build a Mexican
Spanish dataset.
En R. Kumar A. K.
Ojha B. Lahiri M. Zampieri S. Malmasi
V.
Murdock,
y
D.
Kadar,
editores,
Proceedings of the Second Workshop on
Trolling, Aggression and Cyberbullying,
p´aginas
132–136,
Marseille,
France,
Mayo.
European
Language
Resources
Association (ELRA).
Felkner, V., H.-C. H. Chang, E. Jang, y
J. May. 2023. WinoQueer: A community-
in-the-loop benchmark for anti-LGBTQ+
bias
in
large
language
models.
En
Gemma Bel-Enguix, H. Gómez-Adorno, Sergio Ojeda-Trueba, Gerardo Sierra, Jessica Barco, Edgar Lee-Romero, Jocelyn Dunstan, R. Manrique
422

--- Page 11 ---

A. Rogers J. Boyd-Graber, y N. Okazaki,
editores, Proceedings of the 61st Annual
Meeting of the Association for Compu-
tational Linguistics (Volume 1:
Long
Papers),
p´aginas
9126–9140,
Toronto,
Canada, Julio. Association for Computa-
tional Linguistics.
Gonz´alez-Barba, J. ´A., L. Chiruzzo, y S. M.
Jim´enez-Zafra. 2025. Overview of Iber-
LEF 2025: Natural Language Processing
Challenges for Spanish and other Iberian
Languages. En Proceedings of the Iberian
Languages Evaluation Forum (IberLEF
2025), co-located with the 41st Conference
of the Spanish Society for Natural Lan-
guage Processing (SEPLN 2025), CEUR-
WS. org.
G´omez-Adorno, H., G. Bel-Enguix, H. Calvo,
S.
Ojeda-Trueba,
S.
T.
Andersen,
J. V´asquez, T. Alc´antara, M. Soto, y
C. Macias. 2024. Overview of homo-mex
at iberlef 2024:
Hate speech detection
towards the mexican spanish speaking
lgbt+ population.
Procesamiento del
Lenguaje Natural, 73(0):393–405.
Jim´enez-Zafra,
S.,
J.
G´onzalez-Barba,
L. Chiruzzo, T. Alc´antara, M. ´Alvarez
Carmona, E. ´Alvarez Mellado, G. Bel-
Enguix,
B.
Botella
Gil,
S.
Butt,
D.
Hern´andez-Far´ıas,
E.
Lopes,
A. M´armol-Romero, A. Montejo R´aez,
G. Mordecki, J. Os´es Grijalba,
´Alvaro
Rodrigo, y R. Valencia-Garc´ıa, editores.
2025. Proceedings of IberLEF 2025.
Kumaresan,
P.
K.,
R.
Ponnusamy,
R. Priyadharshini, P. Buitelaar, y B. R.
Chakravarthi.
2023.
Homophobia and
transphobia detection for low-resourced
languages
in
social
media
comments.
Natural
Language
Processing
Journal,
5:100041.
Kuncheva, L. y C. Whitaker.
2003.
Mea-
sures of diversity in classifier ensembles
and their relationship with the ensemble
accuracy. Machine Learning, 51:181–207,
05.
Li, L., L. Fan, S. Atreja, y L. Hemphill. 2024.
“hot” chatgpt: The promise of chatgpt in
detecting and discriminating hateful, of-
fensive, and toxic comments on social me-
dia. ACM Trans. Web, 18(2), Marzo.
Macias, C., M. Soto, T. Alc´antara, Garc´ıa,
J. E. Valdez-Rodr´ıguez,
y E. Felipe-
Riveron.
2025.
Cognicic at homo-lat
2025: Fine-tuning and semantic similarity
approaches for polarity detection in span-
ish texts.
En Proceedings of the Iberian
Languages Evaluation Forum (IberLEF
2025), co-located with the 41st Conference
of the Spanish Society for Natural Lan-
guage Processing (SEPLN 2025), CEUR-
WS.org.
Manikandan,
D.,
M.
Subramanian,
y
K. Shanmugavadivel.
2022.
A sys-
tem for detecting abusive contents against
LGBT community using deep learning
based transformer models. En K. Ghosh
T. Mandl P. Majumder, y M. Mitra, edi-
tores, Working Notes of FIRE 2022 - Fo-
rum for Information Retrieval Evaluation,
Kolkata, India, December 9-13, 2022, vol-
umen 3395 de CEUR Workshop Proceed-
ings, p´aginas 106–116. CEUR-WS.org.
Mart´ınez-L´opez, Y., J. C. Hern´andez Nieto,
A.
Rodr´ıguez-G´onzalez,
J.
Madera,
A.
O.
L´opez
Correoso,
C.
d.
C.
Lozano, J. M. Ram´ırez Uceda, y J. C.
Ar´evalo
Fern´andez.
2025.
Uc-uco-
cicese ut3-plenitas team: Exploring in the
homo-lat25 challenge. En Proceedings of
the Iberian Languages Evaluation Forum
(IberLEF 2025), co-located with the 41st
Conference of the Spanish Society for
Natural
Language
Processing
(SEPLN
2025), CEUR-WS.org.
Nava-Mu˜noz, S., M. Graff Guerrero, y H. J.
Escalante.
2023.
Comparison of Classi-
fiers in Challenge Scheme. Lecture Notes
in Computer Science (including subseries
Lecture Notes in Artificial Intelligence and
Lecture Notes in Bioinformatics), 13902
LNCS:89–98.
Nozza,
D.,
A. T. Cignarella,
G. Damo,
T. Caselli, y V. Patti.
2023.
HODI
at EVALITA 2023: Overview of the first
shared task on homotransphobia detection
in italian. En M. Lai S. Menini M. Polig-
nano V. Russo R. Sprugnoli, y G. Venturi,
editores, Proceedings of the Eighth Evalu-
ation Campaign of Natural Language Pro-
cessing and Speech Tools for Italian. Fi-
nal Workshop (EVALITA 2023), Parma,
Italy, September 7th-8th, 2023, volumen
3473 de CEUR Workshop Proceedings.
CEUR-WS.org.
Overview of HOMO-LAT at IberLEF 2025: Human-centric polarity detection in Online Messages Oriented to the Latin American-speaking 
LGBTQ+ populaTion
423

--- Page 12 ---

Olivert-Iserte,
J.,
D.
Caballero-Garc´ıa-
Alcaide, y L. Guijarro-Mart´ınez.
2025.
Enhancing dialectal sentiment analysis
through contextual retrieval and trans-
lation.
En Proceedings of the Iberian
Languages Evaluation Forum (IberLEF
2025), co-located with the 41st Confer-
ence of the Spanish Society for Natural
Language
Processing
(SEPLN
2025),
CEUR-WS.org.
Ruiz, G., R. Campos, T. Ramirez-delreal,
D. Moctezuma, M. Graff, y E. S. Tellez.
2025. Infotec-nlp at homolat: Testing a
novel multi-region spanish model to mon-
itor opinion in latin american lgbtqi+ so-
cial media. En Proceedings of the Iberian
Languages Evaluation Forum (IberLEF
2025), co-located with the 41st Conference
of the Spanish Society for Natural Lan-
guage Processing (SEPLN 2025), CEUR-
WS.org.
Sosto, M. y A. Barr´on-Cede˜no. 2024. Queer-
bench: Quantifying discrimination in lan-
guage models toward queer identities.
Tang, E., P. Suganthan, y X. Yao. 2006. An
analysis of diversity measures.
Machine
learning, 65(1):247–271.
Toapanta-Bernab´e, M. d. C., M.
Garc´ıa-
Cumbreras, L. A. Ure˜na-L´opez, y A. D.
Trivi˜no-Leon. 2025. Sinai-ugpln at homo-
lat iberlef 2025:
Enhancing robertuito
with synthetic data and slur–dialect fea-
tures for multidialectal zero-shot lgbtq po-
larity classification.
En Proceedings of
the Iberian Languages Evaluation Forum
(IberLEF 2025), co-located with the 41st
Conference of the Spanish Society for Nat-
ural Language Processing (SEPLN 2025),
CEUR-WS.org.
Wittig, M. 1979. The straight mind. The
Future of Difference (discours liminaire
en conf´erence universitaire), vol. 3, t. 3.
New York, Barnard Center for Research
on Women, coll. Scholar and Feminist /
VI.
Wittig, M. 1980. The straight mind. Femi-
nist Issues, 1(1):103–111.
Gemma Bel-Enguix, H. Gómez-Adorno, Sergio Ojeda-Trueba, Gerardo Sierra, Jessica Barco, Edgar Lee-Romero, Jocelyn Dunstan, R. Manrique
424

```
