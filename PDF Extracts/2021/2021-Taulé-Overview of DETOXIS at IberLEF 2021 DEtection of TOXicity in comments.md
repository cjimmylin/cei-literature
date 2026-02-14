---
title: "2021-Taulé-Overview of DETOXIS at IberLEF 2021 DEtection of TOXicity in comments - PDF Extract"
source_pdf: "2021-Taulé-Overview of DETOXIS at IberLEF 2021 DEtection of TOXicity in comments.pdf"
pages: 13
extracted_at: "2026-02-14T01:17:58.315960"
---

# PDF Extract: 2021-Taulé-Overview of DETOXIS at IberLEF 2021 DEtection of TOXicity in comments

**Source PDF:** 2021-Taulé-Overview of DETOXIS at IberLEF 2021 DEtection of TOXicity in comments.pdf
**Total Pages:** 13

---

## Content

```
--- Page 1 ---

Overview of DETOXIS at IberLEF 2021:
DEtection of TOXicity in comments In Spanish
Visi´on general de DETOXIS en IberLEF 2021:
DEtecci´on de TOXicidad en comentarios En Espa˜nol
Mariona Taul´e1, Alejandro Ariza1, Montserrat Nofre1, Enrique Amig´o2, Paolo Rosso3
1CLiC, Universitat de Barcelona, Spain
2Research Group in NLP and IR, Universidad Nacional de Educaci´on a Distancia, Spain
3PRHLT Research Center, Universitat Polit`ecnica de Val`encia, Spain
{mtaule, alejandro.ariza14, montsenofre}@ub.edu, enrique@lsi.uned.es, prosso@dsic.upv.es
Abstract: In this paper we present the DETOXIS task, DEtection of TOxicity in
comments In Spanish, which took place as part of the IberLEF 2021 Workshop on
Iberian Languages Evaluation Forum at the SEPLN 2021 Conference. We describe
the NewsCom-TOX dataset used for training and testing the systems, the metrics
applied for their evaluation and the results obtained by the submitted approaches.
We also provide an error analysis of the results of these systems.
Keywords: Toxicity detection, Rank Biased Precision, Closeness Evaluation Mea-
sure, NewsCom-TOX corpus.
Resumen: En este art´ıculo se presenta la tarea DETOXIS, DEtecci´on de TOxici-
dad en comentarios en espa˜nol, que tuvo lugar en el Iberian Languages Evaluation
Forum workshop (IberLEF 2021) en el congreso de la SEPLN 2021. Se describe el
corpus NewsCom-TOX utilizado para entrenar y evaluar los sistemas, las m´etricas
para evaluarlos y los resultados obtenidos por las distintas aproximaciones utilizadas.
Se proporciona tambi´en un an´alisis de los resultados obtenidos por estos sistemas.
Palabras clave: Detecci´on de toxicidad, Rank Biased Precision, Closeness Evalu-
ation Measure, NewsCom-TOX corpus.
1
Introduction
The aim of the DETOXIS task is the detec-
tion of toxicity in comments posted in Span-
ish in response to diﬀerent online news arti-
cles related to immigration. The DETOXIS
task is divided into two related classiﬁcation
subtasks: Toxicity detection task and Toxic-
ity level detection task, which are described
in Section 2. The presence of toxic messages
on social media and the need to identify and
mitigate them leads to the development of
systems for their automatic detection. The
automatic detection of toxic language, espe-
cially in tweets and comments, is a task that
has attracted growing interest from the Nat-
ural Language Processing (NLP) community
in recent years.
This interest is reﬂected
in the diversity of the shared tasks that
have been organized recently, among which
we highlight those held over the last two
years: HateEval-20191 (Basile et al., 2019) on
1https://competitions.codalab.org/competitions/19935
hate speech against immigrants and women
in English and Spanish tweets;
TRAC-2
task on Aggression Identiﬁcation2 (Kumar
et al., 2020) for English, Bengali and Hindi
in comments extracted from YouTube; the
OﬀensEval-20203 on oﬀensive language iden-
tiﬁcation (Zampieri et al., 2020) in Arabic,
Danish, English, Greek and Turkish tweets;
GermEval-2019 shared task4 on the Identi-
ﬁcation of Oﬀensive Language for German
on Twitter (Struß et al., 2019); and the Jig-
saw Multilingual Toxic Comment Classiﬁca-
tion Challenge 5, in which the task is focused
on building multilingual models (English,
French, German, Italian, Portuguese, Rus-
sian and Spanish) with English-only training
data from Wikipedia comments.
DETOXIS is the ﬁrst task that focuses
2https://sites.google.com/view/trac2/shared-task
3https://sites.google.com/site/oﬀensevalsharedtask/
4https://projects.fzai.h-da.de/iggsa/the
5https://www.kaggle.com/c/jigsaw-multilingual-
toxic-comment-classiﬁcation
Procesamiento del Lenguaje Natural, Revista nº 67, septiembre de 2021, pp. 209-221
recibido 03-07-2021 revisado 10-07-2021 aceptado 14-07-2021
ISSN 1135-5948. DOI 10.26342/2021-67-18
© 2021 Sociedad Española para el Procesamiento del Lenguaje Natural

--- Page 2 ---

on the detection of diﬀerent levels of toxic-
ity in comments posted in response to news
articles written in Spanish. The main nov-
elty of the present task is, on the one hand,
the methodology applied to the annotation
of the dataset that will be used for training
and testing the participant models and, on
the other hand, the evaluation metrics that
will be applied to evaluating the participant
models in terms of their system use proﬁle
applying four diﬀerent metrics (F-measure,
Rank Biased Precision (Moﬀat and Zobel,
2008), Closeness Evaluation Measure (Amig´o
et al., 2020) and Pearson’s correlation co-
eﬃcient).
The methodology proposed aims
to reduce the subjectivity of the annotation
of toxicity by taking into account the con-
textual information, i.e. the conversational
thread, and by annotating diﬀerent linguis-
tic features, such as argumentation, construc-
tiveness, stance, target, stereotype, sarcasm,
mockery, insult, improper language, aggres-
siveness and intolerance, which allowed us to
discriminate the diﬀerent levels of toxicity.
The rest of the overview is structured as
follows. In Section 2 we present the two sub-
tasks of DETOXIS. In Section 3 the corpus
NewsCom-TOX used as dataset is described
together with the way it was gathered and
annotated. In Section 4 the diﬀerent metrics
used for the evaluation of the systems and
the results they obtained are presented, as
well as a description of the techniques and
models used by systems. Finally, in Section
5 the conclusions are drawn.
2
Task Description
The aim of the DETOXIS task is the detec-
tion of toxicity in comments posted in Span-
ish in response to diﬀerent online news arti-
cles related to immigration. The DETOXIS
task is divided into two related classiﬁcation
subtasks:
• Subtask 1:
Toxicity detection task is
a binary classiﬁcation task that con-
sists of classifying the content of a com-
ment as toxic (toxic=yes) or not toxic
(toxic=no).
• Subtask 2: Toxicity level detection task
is a more ﬁne-grained classiﬁcation task
in which the aim is to identify the level
of toxicity of a comment (0=not toxic;
1=mildly toxic;
2=toxic and 3=very
toxic).
Although we recommended to participate
in both subtasks, participants were also al-
lowed to participate just in one of them.
Teams were also encouraged to submit mul-
tiple runs (maximum 5).
3
Dataset: The NewsCom-TOX
corpus
We used as dataset the NewsCom-TOX cor-
pus, which consists of 4,359 comments posted
in response to diﬀerent 21 articles extracted
from Spanish online newspapers (ABC, el-
Diario.es, El Mundo, NIUS, etc.)
and dis-
cussion forums (such as Men´eame6 and Foro-
Coches7) from August 2017 to July 2020.
These articles were manually selected tak-
ing into account their controversial subject
matter, their potential toxicity, and the num-
ber of comments posted (minimum 50 com-
ments). We used a keyword-based approach
to search for articles related mainly to immi-
gration. The comments were selected in the
same order in which they appear in the time
thread in the web. The author (anonymized),
the date and the time when the comment was
posted were also retrieved. The number of
comments ranges from 65 to 359 comments
per article. On average, 31.16% of the com-
ments are toxic.
3.1
Annotation Scheme
We considered that a comment is toxic when
it attacks, threatens, insults, oﬀends, deni-
grates or disqualiﬁes a person or group of
people on the basis of characteristics such
as race, ethnicity, nationality, political ideol-
ogy, religion, gender and sexual orientation,
among others. This attack can be expressed
in diﬀerent ways –explicitly (through insult,
mockery and inappropriate humor) or implic-
itly (for instance through sarcasm)– and at
diﬀerent levels of intensity, that is at dif-
ferent levels of toxicity (from impolite and
oﬀensive comments to the most aggressive,
the latter being those comments that incite
hate or even physical violence). We use tox-
icity as an umbrella term under which we
include diﬀerent deﬁnitions used in the lit-
erature to describe hate speech ((Nockleby,
2000), (Waseem and Hovy, 2016), (Schmidt
and Wiegand, 2017), (Davidson et al., 2017))
and abusive (Nobata et al., 2016), aggres-
sive (Kumar et al., 2018), toxic (Kolhatkar et
6https://www.meneame.net/
7https://www.forocoches.com/
Mariona Taulé, Alejandro Ariza, Montserrat Nofre,
Enrique amigó, Paolo Rosso
210

--- Page 3 ---

al., 2020) or oﬀensive (?) language. In fact,
these diﬀerent terms address diﬀerent aspects
of toxic language (Poletto et al., 2020).
We
annotated
each
comment
in
two
categories
‘toxic’
and
‘not
toxic’,
and
then we assigned diﬀerent levels of tox-
icity:
‘toxicity level 0=not
toxic’
(1),
‘toxicity level 1=mildly
toxic’
(2),
‘toxi-
city level 2=toxic’(example
3)
or
‘toxic-
ity level 3=very toxic’ (4) to those that were
annotated ﬁrst as toxic 8.
(1a) Contra la desinformaci´on datos. En el
INE ten´eis los datos de los inmigrantes.
Delitos, cotizaciones, prestaciones, etc.
<toxicity=not> <toxicity level=0>
(1b) Against
misleading
data.
In
the
INE you have data for immigrants.
Crimes,
contributions,
subsidies,
etc.
<toxicity=not> <toxicity level=0>
(2a) Esta gentuza se carga al pa´ıs en dos tele-
diarios
<toxicity=yes> <toxicity level=1>
(2b) This rabble could destroy the coun-
try
with
two
TV
news
programs
<toxicity=yes> <toxicity level=1>
(3a) Lo que importa en realidad es sentirse
mejor con uno mismo. Sumar karma. A
los putos negros les pueden joder bien.
<toxicity=yes> <toxicity level=2>
(3b) What really matters is feeling better
about yourself.
Accumulating karma.
Fucking blacks can get fucked up pretty
good.
<toxicity=yes> <toxicity level=2>
(4a) A
estos
putos
animales
sarnosos
que
los
encierren
y
tiren
la
llave.
<toxicity=yes> <toxicity level=3>
(4b) With these mangy fucking animals, lock
them up and throw away the key.
<toxicity=yes> <toxicity level=3>
In addition to annotating whether or not
a comment was toxic and its level of toxic-
ity, we also annotated the following features:
argumentation, constructiveness, stance, tar-
get, stereotype, sarcasm, mockery, insult, im-
proper language, aggressiveness and intoler-
ance.
All these features have binary val-
ues except the toxicity level (the value ‘0’
8The examples contain text that may be consid-
ered oﬀensive.
is assigned for indicating the absence of the
corresponding feature in the comment, and
the value ‘1’ is assigned when the feature
is present).
We ﬁrst annotated these fea-
tures and we then used them to establish the
toxicity of comments and to determine their
level of toxicity. It is worth noting that the
level of toxicity is especially determined by
the type of features combined. All this in-
formation was included only in the training
dataset that was used for the task.
In or-
der to assign each of these features and be
able to interpret the global meaning of com-
ments, it was crucial to take the context into
account, that is, the conversational thread.
For instance, the conversational threat was
very useful for interpreting and annotating
sarcasm, mockery and stance. The identiﬁer
of each conversation thread (‘thread id’ fea-
ture) was also provided for the participants,
as well as the identiﬁer of the previous com-
ment in the thread (‘reply to’ feature) and
the ‘comment level’ feature. The latter is a
categorical attribute with two possible val-
ues: ‘1’ for indicating that the comment is
a direct comment to an article and ‘2’ for
indicating that the comment is a reply to
another comment.
The ‘topic’ feature was
also provided in the training dataset. This
feature has three possible values (CR=crime,
MI=migration, SO=social) to distinguish the
topic of the news article.
3.2
Annotation Process
Each comment was annotated in parallel
by three annotators and an inter-annotator
agreement test was carried out once all the
comments on each article had been anno-
tated.
Then, disagreements were discussed
by the annotators and a senior annotator
until agreement was reached.
The team of
annotators involved in the task consisted of
two expert linguists and two trained anno-
tators, who were students of linguistics. Ta-
ble 1 shows the results obtained in the inter-
annotator agreement test, the average ob-
served percentage of agreement between the
three annotators, 81.99% for toxicity and
73.95% for toxicity level, and Krippenddorfs’
alpha (0.59 and 0.62 respectively), which en-
sures annotation reliability. The results ob-
tained are quite acceptable considering the
diﬃculty of both tasks.
Overview of DETOXIS at IberLEF 2021: DEtection of TOXicity in comments In Spanish
211

--- Page 4 ---

Feature
Average observed agreement
Krippendorﬀ’s α
Toxicity
81.99%
0.59
Toxicity level
73.95%
0.62
Table 1: Inter-Annotator Agreement Test.
3.3
Training and Test Dataset
We provided participants with 80% of the
NewsCom-TOX corpus for training their
models (3,463 comments), and the remain-
ing 20% of the corpus (896 comments) was
used for testing their models.9
Both train-
ing and test ﬁles were provided in csv for-
mat.
The training dataset contains all the
features included in the annotation of the
NewsCom-TOX corpus (see Subsection 3.1),
whereas the test dataset only contains the
following features: ‘thread id’, ‘comment id’,
‘reply to’, ‘comment level’ and ‘comment’.
Table 2 shows the distribution of toxic
comments by toxicity level. The dataset con-
sists of 4,359 comments, of which 1,385 are
toxic (31.16%): 996 mildly toxic (21.90%),
310 toxic (7.36%) and 79 very toxic (1.81% ).
4
Systems and Results
This section contains a brief description of
the baselines provided as a benchmark, fol-
lowed by an overview of both subtasks (tox-
icity detection and toxicity level detection)
mentioning the reasons behind the selection
of the evaluation metrics and their implica-
tion when models are compared.
Finally,
some interesting systems insights and a brief
error analysis of the submitted approaches
are presented.
4.1
Baselines
A benchmark was set with the introduction of
three diﬀerent baselines: RandomClassiﬁer,
BOWClassiﬁer and ChainBOW. First, Ran-
domClassiﬁer assigns a random of toxicity
from four possible values {0, 1, 2, 3} to each
comment in the test set without any kind
of weighting strategy.
Second, the BOW-
Classiﬁer consists of a simple Support Vector
Classiﬁer (SVC) that receives the features ex-
tracted by a TF-IDF Vectorizer (an advanced
version of the classical Bag-Of-Words tech-
nique).
In particular, the SVC model uses
9In order to avoid any conﬂict with the sources
of comments regarding their Intellectual Property
Rights (IPR), the data was privately sent to each par-
ticipant that was interested in the task. The corpus
will be only available for research purposes.
a linear kernel with a regularization param-
eter equal to 1.0 and a “one-versus-rest” de-
cision function strategy for the toxicity level
detection subtask. Furthermore, the TF-IDF
Vectorizer, which is responsible for feature
extraction, constructs a vocabulary of 5,000
entries including unigrams and bigrams af-
ter performing a simple preprocessing stage
(lowercasing and removal of accents).
Fi-
nally, due to the fact of having an unbalanced
dataset, we decided to include a baseline that
processes both subtasks sequentially. There-
fore, ChainBOW contains two BOWClassi-
ﬁers, one for each subtask (toxicity detection
and toxicity level detection), connected in a
hierarchical fashion with the same conﬁgura-
tion as mentioned before. It is worth men-
tioning that, given their baseline nature, no
hyperparameter optimization was performed
on any of the models. In addition, all base-
lines were implemented using the Python
scikit-learn library.
4.2
Subtask 1: Toxicity Detection
Task
Subtask 1 consists of a binary classiﬁcation
(toxic vs.
non-toxic).
In this subtask, the
metrics precision, recall and their combina-
tion by means of the F-measure were used.
Table 5 ranks the best run of each of the par-
ticipating teams according to F-measure. In
general, the SINAI system outperforms the
rest of systems. SINAI is outperformed by
some of the other approaches in terms of
recall, although at the cost of a signiﬁcant
precision loss.
In relation to the baselines,
RandomClassiﬁer achieves a mid-ranking po-
sition in the ranking, with low precision but
medium high recall.
In a similar position
is ChainBOW, with low recall and medium
high precision. In general, there is signiﬁcant
room for improvement between participants
runs and the Gold Standard.
Figure 1 illustrates the precision and recall
scores achieved by the systems. The precision
of all systems is between 0.25 and 0.75.
Mariona Taulé, Alejandro Ariza, Montserrat Nofre,
Enrique amigó, Paolo Rosso
212

--- Page 5 ---

Feature
Comments
Percentage
mildly toxic (level 1)
996
21.90%
toxic (level 2)
310
7.36%
very toxic (level 3)
79
1.81%
Total
1,385
31.16%
Table 2: Distribution of toxic comments.
Figure 1: Precision and Recall for the best
run of each team in Subtask 1.
4.3
Subtask 2: Toxicity Level
Detection Task
Regarding Subtask 2, the toxicity level detec-
tion task is a more ﬁne grained classiﬁcation
task in which the aim is to identify the level
of toxicity of a comment (0= not toxic; 1=
mildly toxic; 2= toxic and 3: very toxic). For
this task we considered four evaluation met-
rics.
Closseness Evaluation Metric (CEM):
The metric CEM (Amig´o et al., 2020)
considers the proximity between pre-
dicted and real categories.
Unlike
measures based on absolute error, CEM
has two particularities. First, it assumes
no
equidistance
between
categories.
That is, an error between category 0
and 2 is not necessarily twice as serious
as an error between categories 0 and
1.
In addition, it assigns more weight
to infrequent categories.
This avoids
over-weighting systems that tend to
classify items in majority classes. CEM
is appropriate for unbalanced data sets,
and when the relative distance between
categories beyond the way they are
ordered is unknown.
Rank Biased Precision (RBP): RBP
is
a ranking metric (Moﬀat and Zobel,
2008). We rank the output of the sys-
tem and the Gold Standard on the basis
of toxicity levels (from highest to lowest)
and compare the two rankings.
Basi-
cally, RBP is computed as the sum of the
actual values (Gold Standard) along the
ranking generated by the system with a
weight function that decreases as we de-
cay in the ranking of the system output.
d corresponds to the categorized items in
the system output s, with pos(d) being
the ranking position of d in the system
output s and g(d) being the real cate-
gory value in the Gold Standard for this
item. RBP is computed as:
RBP = (1 −p)
X
d
f(d)g(d)
where
f
is
a
decay
function
that
decreases with position i,
concretely
f(d) = ppos(i)−1. The value p is a param-
eter which is typically ﬁxed at X. Origi-
nally, RBP applies to rankings with one
item in each ranking position. However,
in our scenario, the items are ordered
in four levels in the ranking generated
by the system (level 4= not toxic; level
3= mildly toxic; level 2= toxic and level
1:
very toxic).
Therefore, we modify
RBP by considering the average i posi-
tion that each item would occupy in the
system output if we were to randomly
order the ties:
f(d) =
1
ns(d)
MaxPos(d)
X
i=MinPos(d)
pi−1
where ns(d) represents the number of
items at level s(d) in the system out-
put. MinPos(d) and MaxPos(d) repre-
sent the minimum and maximum posi-
tion that item d could occupy in the sys-
tem output s according to its level. This
metric is appropriate when sorting items
according to their toxicity. For instance,
the scenario in which the user needs to
Overview of DETOXIS at IberLEF 2021: DEtection of TOXicity in comments In Spanish
213

--- Page 6 ---

ﬁnd the most toxic comments ﬁts in this
metric.
Accuracy: Accuracy is the most popular
classiﬁcation metric.
This metric does
not consider the order between cate-
gories.
That is, an error is penalised
regardless of the distance to the actual
category. Furthermore, it does not com-
pensate for the eﬀect of imbalance in the
data set. This metric is not appropriate
for most possible scenarios, although it
has the advantage of being very easy to
interpret in terms of the percentage of
hits.
Mean Average Error (MAE): MAE av-
erages the absolute diﬀerence between
predicted and actual categories.
This
metric assumes equidistance between
categories and does not compensate for
the eﬀect of imbalance between cate-
gories in the data set. MAE is appro-
priate, for example, when predicting the
average toxicity value in a comment set.
Note this requires assuming numerical
intervals between categories.
Pearson Coeﬃcient: Like
MAE,
using
Pearson coeﬃcient requires assuming
equidistance between categories.
The
diﬀerence with respect to MAE is that
it does not require the system to predict
the category of each item, but gener-
ates a scale that is linearly correlated
with the actual scale.
In addition, it
compensates for the eﬀect of imbalance
between
categories
by
giving
more
weight to those categories that are more
infrequent.
Obtaining a high Pearson
value is interesting, for example, when
predicting the evolution of toxicity over
time in a comment stream or compare
the average toxicity of two streams.
Table 6 shows the results obtained by the
best run of each team in terms of CEM. The
baselines are in the middle positions of the
systems ranking.
In this case, the BOW-
Classiﬁer approach performs better than the
other baselines developed by the task organ-
isers.
Figure 2 illustrates the CEM results vs.
other evaluation metrics.
In this subtask,
the systems SINAI and Team Sabari outper-
form most of the other approaches for all
metrics. There is only one exception. The
system output DCG outperforms SINAI and
Sabari by a wide margin in terms of ranking
(RBP metric). This means that, in a scenario
where the objective is to prioritise particu-
larly toxic comments, DCG is more eﬀective
than SINAI.
In Figure 2, we ﬁnd a high correspondence
between CEM and the Pearson correlation
coeﬃcient. CEM does not consider numeric
intervals.
The Pearson coeﬃcient does not
take into account the proximity of the esti-
mated categories to the actual ones but the
correlation between the values (numeric cat-
egory labels) in the system output and the
gold standard.
This means that the eﬀect
of ’scale shifts’ and the eﬀect of assuming
numeric intervals between categories is not
particularly relevant in this evaluation bench-
mark.
However, we did not ﬁnd as much corre-
spondence between the CEM metric and the
MAE and Accuracy metrics. The main dif-
ference is that CEM, like Pearson, compen-
sates for the imbalance between categories in
the data set, giving more weight to errors
or hits in infrequent categories. As Figure 2
shows, there is a set of runs that obtain simi-
lar Accuracy and MAE values, but neverthe-
less present important diﬀerences in terms of
CEM. From a usage scenario perspective, this
result indicates that these runs are compara-
ble if we are interested in predicting or ap-
proximating the actual category in as many
cases as possible. For example, this would be
the case if we wanted to calculate the average
toxicity of a set of comments. However, if we
are interested in detecting particular cases of
toxicity (low, medium or high) then we can
assert that some of these runs will be more
eﬀective than others.
4.4
Systems Insights
A total of 31 teams (Subtask 1) and 24
teams (Subtask 2) sent a maximum of
ﬁve submissions per subtask to be evalu-
ated.
Not surprisingly, and based on the
recent success of transfer learning with pre-
trained Transformer-like language models,
the top ﬁve teams in both subtasks achieved
their best scores using BETO10 (the Span-
ish version of the BERT model).
The dif-
ference in performance between their re-
spective submissions thus lies in the ﬁne-
tuning techniques, data augmentation strat-
10https://github.com/dccuchile/beto
Mariona Taulé, Alejandro Ariza, Montserrat Nofre,
Enrique amigó, Paolo Rosso
214

--- Page 7 ---

Figure 2: Correspondence between CEM and other metrics in Subtask 2.
egy and/or preprocessing steps.
Although
the performance of classical machine learn-
ing models such as TF-IDF with Random
Forests/Support Vector Machines/Logistic
Regression Classiﬁers were not as high as
those achieved by BETO, they were also used
as part of ensemble architectures and ana-
lyzed by multiple participants. In fact, sev-
eral teams provided valuable insights and
comparisons of models for a task that is in-
credibly challenging, even for trained expert
annotators. The most interesting conclusions
are summed up below.
This competition introduced several chal-
lenges in addition to the toxicity detection
problem. First, the language of the dataset
(comments in Spanish) diﬀers from the usual
English language present in most of the gen-
eral benchmark NLP datasets.
Therefore,
the models needed to account for the diﬀerent
directionality of the text, as well as for the
selection of other pre-processing steps. For
instance, the GTH-UPM team performed an
analysis of the multiple pre-processing steps
applied prior to a pre-trained Transformer-
like model (BETO). Apparently, a basic
text normalization (the replacement of spe-
cial Named Entities such as MAIL, DATE,
URL...
with their respective shared token)
improves BETO’s performance as opposed
to other steps e.g.
the removal of stop-
words and punctuation or lemmatization.
GTH-UPM also validated the extension of
pre-trained models’ vocabulary with domain-
speciﬁc terms as a useful technique to im-
prove task-oriented results.
Another analysis that is worth paying
attention to regarding the language of the
texts is a performance comparison among
pretrained multilingual models, English mod-
els with a proper Spanish-to-English transla-
tor and Spanish models. Alejandro Mosquera
built a stacked model composed of at least
one model for each variant in conjunction
with additional features and extracted the
feature importance of the individual models
via cross-validation on the training dataset.
The results show that pretrained multilin-
gual models such as XLM do not provide as
much predictive power in this toxicity context
as a neural network with a capsule network
architecture using SBWC i25 GloVe Span-
ish embeddings.
However, the diﬀerence is
not so pronounced when we compare it with
the translator followed by the model trained
on English embeddings. A similar compari-
son was performed by the AI-UPV team task
in which classical machine learning models
(both generative and discriminative), multi-
lingual BERT and BETO performed cross-
validation with a hyperparameter setup. Not
only did they conclude that transformer-like
architectures outperform classical statistical
models in this complex task, but they also
Overview of DETOXIS at IberLEF 2021: DEtection of TOXicity in comments In Spanish
215

--- Page 8 ---

found that BETO achieved substantially bet-
ter results than multilingual BERT for all of
their top ﬁve best conﬁgurations and in both
subtasks.
Furthermore, Alejandro Mosquera’s was
the only team to introduce side informa-
tion related to the topic of the articles each
comment refers to and the thread to which
they belong.
As a preliminary analysis
using cross-validation, the use of informa-
tion related to the comments present in the
thread/conversation seems to enrich overall
model performance. Further research on how
to better exploit thread and topic informa-
tion may be an interesting and promising di-
rection.
Last but not least, the winners of both
DETOXIS subtasks (SINAI team proved the
importance of enriching the model by ﬁne-
tuning it on similar tasks related to senti-
ment and emotion analysis, thus increasing
the available training data and making more
precise predictions thanks to this Multi-Task
Learning strategy.
In fact, SINAI was the
only team in the competition that took the
provided extra features (see Section 3.1) into
account, thereby giving their systems an im-
portant boost in comparison to the other par-
ticipants. However, a study of the inﬂuence
of each extra feature on the model’s predic-
tive power is yet to be performed.
4.5
Error Analysis
The tasks of toxicity and toxicity level de-
tection are particularly diﬃcult for machine
learning models. In fact, even the most re-
cent transformer models struggle with lin-
guistic devices users sometimes use such as
sarcasm or irony.
However, thanks to the
fact that the dataset includes 13 additional
features that classify the text according to
other helpful semantic dimensions from the
raw text, we can easily identify the most chal-
lenging comments and the possible reasons
behind the diﬃculty of their detection. Ta-
ble 3 contains the average performance of the
top ﬁve best submissions per task (based on
the F1-score and CEM metrics respectively)
considering the subset of samples where each
feature is present and a single (best) run per
team.
Regarding the ﬁrst task (toxicity detec-
tion), the oﬃcial metric focuses on the abil-
ity of the models to detect all toxic com-
ments and pays zero attention to the neg-
ative class.
Therefore, comments with ar-
gumentative cues (generally linked to non-
toxic comments) that are marked as toxic
are usually the most diﬃcult ones to detect
(see examples 5, 8, 10, 13 and 14 in Table
4). A similar situation appears in comments
with a positive stance that are actually toxic.
Other dimensions that clearly increase the
diﬃculty of this task are sarcasm and stereo-
type. The existence of a greater number of
implicit stereotypes rather than explicit ones
in hate speech posts which ultimately require
models to learn related world knowledge be-
forehand is well known.
Furthermore, this
dataset contains comments that are replies
to other users’ comment.
Consequently, a
broader context than just the current text
is sometimes required to make an informed
decision on whether the comment is toxic or
not.
On the other hand, the diﬃculty of lin-
guistic cues related to aggressiveness, mock-
ery, sarcasm and stereotype is even clearer in
the task of toxicity level detection when CEM
scores are considered. Even though a com-
ment may not apparently be very toxic ac-
cording to the explicit words in the text, im-
plicit messages and emitter intention can be
really harmful for the receiver. Consequently,
an eﬀort to build automatic systems able to
capture toxicity levels in comments in which
such subtle hidden messages are included is
of utmost importance. For instance, example
12 is usually marked as non-toxic by the top
performing submitted systems although the
actual toxicity is at its maximum level due
to the implicit aggressiveness within the mes-
sage. This diﬀerence between the predicted
and ground truth labels is highly penalized
by the oﬃcial CEM metric.
5
Conclusions and Future Work
This paper has described the DETOXIS chal-
lenge at IberLEF 2021 and summarized the
participation of several teams in both sub-
tasks which evidenced interesting approaches
and conclusions.
Although all of the top-
performing systems made use of the Spanish
version of the BERT model (a Transformer
encoder), a variety of insights into the impor-
tance of diﬀerent strategies become clearer
for researchers to build upon or explore fur-
ther in their respective studies on hate speech
and toxicity detection. As opposed to pre-
vious challenges on hate speech, we have
Mariona Taulé, Alejandro Ariza, Montserrat Nofre,
Enrique amigó, Paolo Rosso
216

--- Page 9 ---

Feature
Size (Toxic)
Subtask 1
Subtask 2
1. argumentation
459 (113)
0.6006
0.7591
2. constructiveness
282 (0)
-
0.8929
3. positive stance
22 (7)
0.6545
0.8465
4. negative stance
252 (125)
0.6919
0.6764
5. target person
108 (90)
0.7243
0.5672
6. target group
67 (62)
0.7945
0.5444
7. stereotype
41 (38)
0.6938
0.5110
8. sarcasm
52 (42)
0.6653
0.5497
9. mockery
80 (77)
0.7443
0.4824
10. insult
85 (83)
0.8541
0.5202
11. improper language
74 (51)
0.7985
0.6542
12. aggressiveness
15 (15)
0.7091
0.3892
13. intolerance
15 (13)
0.8516
0.5655
Table 3: Average score (F1-score and CEM respectively) of the ﬁve best performing teams in
each task for the subset of comments where the corresponding feature is positive together with
the size of each subset and the number of toxic instances in them.
provided 13 additional features and a ﬁne-
grained toxicity degree target with four pos-
sible labels that go beyond the classical bi-
nary toxicity classiﬁcation. Furthermore, the
collection of comments includes the thread to
which they belong and the topic of the article
they are posted in, thus, allowing a broader
context to be used by innovative solutions.
Unsurprisingly, multilingual models are
outperformed by the Spanish counterparts
in this challenge most probably due to the
speciﬁc embedding space fully optimized in
the given language and the use of a more
language-oriented token vocabulary.
Tech-
niques
such
as
data
augmentation
with
Masked Language Modeling and the addition
of Multi-Task Learning with datasets belong-
ing to similar tasks in order to increase the
available data used at the ﬁnetuning step has
turned out to be beneﬁcial in a scenario in
which the number of comments is small and
classes were unbalanced. Moreover, despite
the fact that further analysis and more elab-
orate ways to extract information from the
conversation and the topic are needed, the
only team that took advantage of such infor-
mation achieved positive results in the ﬁnal
outcome by combining them with other com-
mon strategies.
Finally, it is important to mention that,
depending on the ﬁnal application and its
speciﬁc requirements, the selection of the
model may require a diﬀerent evaluation met-
ric. Thanks to our selection of metrics, we
were able to provide a simple visualization of
diﬀerent trade-oﬀs when opting for a certain
system and how models perfectly suitable for
a particular goal may not perform at the
same level when those requisites change. A
clear example we have presented is the com-
parison between the SINAI and DCG sys-
tems, in which the former was better at de-
tecting all toxicity levels according to an or-
dinal classiﬁcation metric such as CEM but
was outperformed by the latter in scenarios in
which prioritizing the most toxic comments is
the priority (according to the RBP ranking
metric).
Regarding future work, systems are as yet
far from the Gold Standard and this is mainly
due to the diﬃculty these models encounter
when detecting implicit features such as ag-
gressiveness, mockery and sarcasm.
More-
over, the lack of examples corresponding to
each individual feature makes this an even
more challenging task.
Additional research
on the inﬂuence of these implicit features on
the ﬁnal toxicity of the comment and the cre-
ation of systems able to detect and mitigate
such subtle cues is highly necessary in a so-
ciety in which messages and ideas are spread
faster than ever. Some of the paths that were
not explored by participants and could be
worth looking into are: larger language mod-
els or possible distillations of them, improve-
ments to the semantic contextualization of
language models by the use of techniques that
reduce their anisotropicity problem and the
incorporation of sentence encoders or compo-
sitional representations to the ensemble ar-
chitectures.
Overview of DETOXIS at IberLEF 2021: DEtection of TOXicity in comments In Spanish
217

--- Page 10 ---

ID
Features
FN Ratio
Toxicity
Comment
1
8
1.0000
1
Como se echa de menos la opini´on de los guardianes de la moral
en la noticia de la ejecuci´on en Portland. Bueno, en muchos casos
est´an sus negativos pero no sus siempre dignos comentarios.
2
10, 11
1.0000
1
Directamente :peineta:
3
4
1.0000
1
Los andaluces, no los espa˜noles
4
-
0.9677
1
Y 600000 votos m´as, para el pandemias.
5
1, 4, 12
0.9677
1
No intentaba poner ni a favor ni en contra. Ni intentaba realizar
una cr´ıtica en el origen de los EEUU. Mi comentario solo trataba
de dar perspectiva del problema en USA. En mi opini´on personal
todos los usanos con armas podr´ıan salir a la calle hasta matarse
los unos a los otros que el mundo en un plazo m´as corto que largo
ir´ıa a mejor. Pero es mi opini´on.
6
3, 4, 5, 10
0.9677
1
Que f´acil es hablar bocachancla
7
5
0.9677
1
Expulsion de echenique de espa˜na ya1
8
1, 4, 6, 9, 10
0.9355
1
En Madrid no hay campo, no hablo de la p´urria de ciudad. Hablo
de la gente que todo los a˜nos entra en Espa˜na para hacer estos
trabajos estacionales + los que est´an siempre aqu´ı y que se han
ido
9
4, 11
0.9355
1
Como conseguir 600.000 votos. Vomitivo
10
1, 5
0.9355
1
El segundo es el que le tira al suelo, pero mira el primero tambi´en,
ﬁgura. youtu.be/neUnhYO2Ehc
11
6, 7
0.9355
1
Pues m´as raz´on para hacer como ellos contra ellos. La diferencia es
que nosotros sabemos que esta mal, ellos creen que es lo correcto.
Nosotros podemos parar cuando lo estimemos, ellos no.
12
12
0.9355
3
Tengo esperanzas en que legalicen la noche de ’La Purga’. La peli
cuenta como las clases acomodadas impulsan esta celebraci´on para
que el lumpen se autorregule. Es sencilla, pero a mi me entretuvo
mucho : )
13
1, 4, 5, 9
0.9355
1
Echenique miente mas que corre....aun regularizando estos irreg-
ulares, no serian de hecho ”ciudadanos espa˜noles” y por lo tanto
SIN derecho a voto. Pura propaganda bolchevique.
14
1, 4, 5
0.9355
1
ss.
29.304 simplemente exige que tengas licencia de caza (que
no se sabe publicamente si el implicado la tiene o no) [...] Ergo,
podemos deducir que el acusado no estaba violando la 948.60(2)(a)
al usar un arma larga con 17 a˜nos. Hay que hacer los deberes
antes de soltar aﬁrmaciones tan categ´oricas. O sea que necesita
una licencia de caza y como no sabemos si la tiene o no vamos
a suponer que SI la tiene pero el que tiene que hacer los deberas
antes de hacer aﬁrmaciones categ´oricas soy yo. Pos fueno, pos fale,
pos malegro, campe´on. al parecer al ﬁnal no va a haber acusaci´on
por la tenencia de armas, ¿Fuente?
15
5, 8
0.9355
2
Si le hacen tantas pregunta a ”NUMERO 3”, es posible que se
cortocircuite?
16
4, 13
0.8710
1
Deportaciones masivas ya!
Table 4: List of the top 16 comments in the test set that are misclassiﬁed as non-toxic by the
majority of the systems. The Features column shows the feature identiﬁers from Table 3 marked
as positive for the given comment, FN Rate is the ratio of systems that marked the comment
as non-toxic and Toxicity refers to the four-levels annotation for that speciﬁc comment.
Acknowledgments
The work has been carried out in the
framework
of
the
following
projects:
MISMIS
project
(PGC2018-096212-B),
funded
by
Ministerio
de
Ciencia,
Inno-
vaci´on y Universidades (Spain), CLiC SGR
(2027SGR341), funded by AGAUR (Gener-
alitat de Catalunya) and STERHEOTYPES
project (Challenges for Europe), funded by
Fondazione Compangia di San Paolo.
References
Amig´o, E., J. Gonzalo, S. Mizzaro, and
J. Carrillo-de Albornoz.
2020.
Eﬀec-
tiveness metric for ordinal classiﬁcation:
Formal properties and experimental re-
sults. In Proceedings of the 58th Annual
Meeting of the Association for Computa-
tional Linguistics. Association for Compu-
tational Linguistics.
Basile, V., C. Bosco, E. Fersini, N. Deb-
ora, V. Patti, F. M. R. Pardo, P. Rosso,
Mariona Taulé, Alejandro Ariza, Montserrat Nofre,
Enrique amigó, Paolo Rosso
218

--- Page 11 ---

M. Sanguinetti, et al.
2019.
Semeval-
2019 task 5: Multilingual detection of hate
speech against immigrants and women in
twitter. In 13th International Workshop
on Semantic Evaluation, pages 54–63. As-
sociation for Computational Linguistics.
Davidson, T., D. Warmsley, M. Macy, and
I. Weber. 2017. Automated hate speech
detection and the problem of oﬀensive lan-
guage. In Proceedings of the International
AAAI Conference on Web and Social Me-
dia, volume 11.
Kolhatkar, V., H. Wu, L. Cavasso, E. Fran-
cis, K. Shukla, and M. Taboada.
2020.
The sfu opinion and comments corpus: A
corpus for the analysis of online news com-
ments. Corpus Pragmatics, 4(2):155–190.
Kumar, R., A. K. Ojha, S. Malmasi, and
M. Zampieri.
2018.
Benchmarking ag-
gression identiﬁcation in social media.
In Proceedings of the First Workshop
on Trolling, Aggression and Cyberbullying
(TRAC-2018), pages 1–11.
Kumar, R., A. K. Ojha, S. Malmasi, and
M. Zampieri. 2020. Evaluating aggression
identiﬁcation in social media. In Proceed-
ings of the Second Workshop on Trolling,
Aggression and Cyberbullying, pages 1–5.
Moﬀat, A. and J. Zobel. 2008. Rank-biased
precision for measurement of retrieval ef-
fectiveness. ACM Transactions on Infor-
mation Systems (TOIS), 27(1):1–27.
Nobata,
C.,
J.
Tetreault,
A.
Thomas,
Y. Mehdad, and Y. Chang. 2016. Abu-
sive language detection in online user con-
tent. In Proceedings of the 25th interna-
tional conference on world wide web, pages
145–153.
Nockleby, J. T.
2000.
Hate speech.
En-
cyclopedia of the American constitution,
3(2):1277–1279.
Poletto,
F.,
V.
Basile,
M.
Sanguinetti,
C. Bosco, and V. Patti. 2020. Resources
and benchmark corpora for hate speech
detection: a systematic review. Language
Resources and Evaluation, pages 1–47.
Schmidt, A. and M. Wiegand. 2017. A sur-
vey on hate speech detection using nat-
ural language processing. In Proceedings
of the ﬁfth international workshop on nat-
ural language processing for social media,
pages 1–10.
Struß, J. M., M. Siegel, J. Ruppenhofer,
M. Wiegand, M. Klenner, et al.
2019.
Overview of germeval task 2, 2019 shared
task on the identiﬁcation of oﬀensive lan-
guage.
In Preliminary proceedings of
the 15th Conference on Natural Language
Processing (KONVENS 2019).
Waseem, Z. and D. Hovy.
2016.
Hateful
symbols or hateful people? predictive fea-
tures for hate speech detection on twitter.
In Proceedings of the NAACL student re-
search workshop, pages 88–93.
Zampieri,
M.,
P.
Nakov,
S.
Rosenthal,
P. Atanasova, G. Karadzhov, H. Mubarak,
L. Derczynski, Z. Pitenis, and C¸. C¸¨oltekin.
2020. SemEval-2020 task 12: Multilingual
oﬀensive language identiﬁcation in social
media (OﬀensEval 2020). In Proceedings
of the Fourteenth Workshop on Seman-
tic Evaluation, pages 1425–1447. Interna-
tional Committee for Computational Lin-
guistics.
A
Appendix: Results for both
Subtasks
This appendix provides the results obtained
by each team, selecting their best scoring out-
put, for both DETOXIS subtasks. Table 5
ranks the best run of each of the participat-
ing teams according to F-measure. Table 6
shows the results obtained by the best run of
each team in terms of CEM (column 3). The
rest of columns show the results in terms of
MAE, RBP, Pearson and Accuracy metrics.
The baselines are in the middle positions of
the systems ranking.
Overview of DETOXIS at IberLEF 2021: DEtection of TOXicity in comments In Spanish
219

--- Page 12 ---

Ranking
Team
F-measure
Precision
Recall
1
SINAI
0.6461
0.6356
0.6569
2
GuillemGSubies
0.6000
0.5234
0.7029
3
AI-UPV
0.5996
0.5672
0.6360
4
DCG
0.5734
0.6225
0.5314
5
GTH-UPM
0.5726
0.5852
0.5607
6
alejandro mosquera
0.5691
0.4688
0.7238
7
Team Sabari
0.5646
0.5379
0.5941
8
maia
0.5570
0.4904
0.6444
9
address
0.4930
0.4697
0.5188
10
Javier Garc´ıa Gilabert
0.4911
0.3644
0.7531
11
Dembo
0.4632
0.4798
0.4477
12
ToxicityAnalizers
0.4562
0.4444
0.4686
13
DetoxisLuciaYNora
0.4529
0.4346
0.4728
14
YaizaMi˜nana
0.4449
0.4077
0.4895
15
VG UPV
0.4377
0.3348
0.6318
16
Datacism
0.4235
0.4839
0.3766
17
Calabacines c´osmicos
0.4065
0.4603
0.364
18
Ivan i Jaume
0.3991
0.4194
0.3808
19
CarlesyJorge
0.3844
0.3973
0.3724
20
NEON2
0.3798
0.4463
0.3305
RandomClassiﬁer
0.3761
0.2540
0.7238
ChainBOW
0.3747
0.5071
0.2971
21
JOSAND10
0.3636
0.5323
0.2762
22
GCP
0.3535
0.4459
0.2929
23
LlunaPerez-J´uliaGregori
0.3017
0.2806
0.3264
24
GalAgo
0.2982
0.2841
0.3138
25
Just Do It
0.2060
0.5000
0.1297
BOW Classiﬁer
0.1837
0.5909
0.1088
26
Benlloch
0.1828
0.2705
0.1381
27
LNR SaraSoto ClaraSalelles
0.1637
0.5476
0.0962
28
LNR I˜nigoPicasarri JoanCastillo
0.1637
0.5476
0.0962
29
ElenaLopez MartaGarcia LNR
0.1605
0.4000
0.1004
Word2VecSpacy
0.1523
0.3651
0.0962
30
Iker&Miguel
0.0405
0.6250
0.0209
31
JOREST
0.0246
0.6000
0.0126
Table 5: Results of Subtask 1.
Mariona Taulé, Alejandro Ariza, Montserrat Nofre,
Enrique amigó, Paolo Rosso
220

--- Page 13 ---

Ranking
Team
CEM
MAE
RBP
Pearson
Accuracy
Gold Standard
1
0
0.8213
1
1
1
SINAI
0.7495
0.2626
0.2612
0.4957
0.7654
2
Team Sabari
0.7428
0.2795
0.2670
0.5014
0.7464
3
DCG
0.7300
0.3019
0.3925
0.4544
0.7329
4
GTH-UPM
0.7256
0.3019
0.1545
0.4298
0.7318
5
GuillemGSubies
0.7189
0.349
0.2449
0.4451
0.6835
6
AI-UPV
0.7142
0.3143
0.2101
0.4734
0.7127
7
address
0.6915
0.3165
0.1136
0.3215
0.7228
8
Dembo
0.6703
0.3468
0.1037
0.2677
0.6936
ChainBOW
0.6535
0.3389
0.0787
0.2077
0.7127
9
Javier Garc´ıa Gilabert
0.6514
0.3345
0.2773
0.2158
0.7250
10
JOSAND10
0.6424
0.3367
0.1306
0.2046
0.7239
11
ToxicityAnalizers
0.6332
0.4871
0.0709
0.1805
0.6139
12
NEON2
0.6324
0.3434
0.1339
0.1632
0.7116
BOWClassiﬁer
0.6318
0.3266
0.1657
0.1688
0.7329
13
JOREST
0.6250
0.3389
0.0592
0.0972
0.7273
14
Iker&Miguel
0.6250
0.3389
0.0592
0.0972
0.7273
15
Ivan i Jaume
0.6201
0.4366
0.0844
0.1604
0.6251
16
DetoxisLuciaYNora
0.6200
0.3816
0.0903
0.1248
0.6869
Word2VecSpacy
0.6116
0.3928
0.0855
0.0566
0.7015
GloVeSBWC
0.6111
0.3356
0.1085
0.0623
0.7318
17
CarlesyJorge
0.6094
0.3367
0.0535
NaN
0.7318
18
ElenaLopez MartaGarcia LNR
0.6064
0.3490
0.0294
-0.0153
0.7217
19
VG UPV
0.6041
0.6498
0.1224
0.1896
0.5589
20
Just Do It
0.5928
0.4579
0.0320
0.0195
0.6207
21
Benlloch
0.5913
0.4545
0.0711
0.0237
0.633
22
GalAgo
0.5876
0.4759
0.0936
0.0372
0.6285
23
LlunaPerez-J´uliaGregori
0.5498
0.5724
0.0369
0.0004
0.5365
24
JosepCarles CandidogGarcia LNR
0.5376
0.6061
0.0705
0.0072
0.4949
RandomClassiﬁer
0.4382
1.4287
0.0390
-0.0455
0.2278
Table 6: Results of Subtask 2.
Overview of DETOXIS at IberLEF 2021: DEtection of TOXicity in comments In Spanish
221

```
