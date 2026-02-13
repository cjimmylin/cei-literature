---
title: "2020-Kurpicz-Briki-Cultural Differences in Bias Origin and Gender Bias in Pre-Trained - PDF Extract"
source_pdf: "2020-Kurpicz-Briki-Cultural Differences in Bias Origin and Gender Bias in Pre-Trained.pdf"
pages: 11
extracted_at: "2026-02-13T13:24:16.854285"
---

# PDF Extract: 2020-Kurpicz-Briki-Cultural Differences in Bias Origin and Gender Bias in Pre-Trained

**Source PDF:** 2020-Kurpicz-Briki-Cultural Differences in Bias Origin and Gender Bias in Pre-Trained.pdf
**Total Pages:** 11

---

## Content

```
--- Page 1 ---

Cultural Differences in Bias? Origin and Gender Bias in Pre-Trained
German and French Word Embeddings
Mascha Kurpicz-Briki
Bern University of Applied Sciences
Biel/Bienne, Switzerland
mascha.kurpicz@bfh.ch
Abstract
Smart applications often rely on training
data in form of text.
If there is a bias
in that training data, the decision of the
applications might not be fair. Common
training data has been shown to be bi-
ased towards different groups of minori-
ties. However, there is no generic algo-
rithm to determine the fairness of training
data. One existing approach is to mea-
sure gender bias using word embeddings.
Most research in this ﬁeld has been ded-
icated to the English language.
In this
work, we identiﬁed that there is a bias
towards gender and origin in both Ger-
man and French word embeddings.
In
particular, we found that real-world bias
and stereotypes from the 18th century are
still included in today’s word embeddings.
Furthermore, we show that the gender bias
in German has a different form from En-
glish and there is indication that bias has
cultural differences that need to be consid-
ered when analyzing texts and word em-
beddings in different languages.
1
Introduction
Bias is an important topic in machine learning ap-
plications, and in particular in natural language
processing. For example, it can be easily shown in
automatic translation. As shown in Figure 1, when
translating ”She is an engineer. He is a nurse.” to
Turkish and then back to English, we obtain ”He’s
an engineer. She is a nurse.”. Due to the fact
that in Turkish there is no difference between he
and she, when translating back to English, a guess
Copyright c⃝2020 for this paper by its authors. Use permit-
ted under Creative Commons License Attribution 4.0 Interna-
tional (CC BY 4.0)
about the gender has to be made. It is therefore
highly relevant to identify and mitigate gender bias
in natural language processing (Sun et al., 2019).
Word embeddings are applied in several types
of applications and enhance the development of
machine learning and natural language processing.
However, they also amplify existing social stereo-
types in the human-generated training data.
Different approaches to identify and mitigate
bias in word embeddings have been developed. A
word embedding is a vectorial representation of
a word (or phrase), trained on co-occurences in
a text corpora. Each word w is represented as a
d-dimensional word vector ⃗w ∈Rd (Bolukbasi
et al., 2016), where often d = 300 (Caliskan et al.,
2017). In such a vector space, words with similar
meaning have vectors that are close (i.e. they have
a small vector distance). It has been conﬁrmed that
the vector distance can be used to represent the
relationship between two words (Mikolov et al.,
2013c). Using this method, problems like the fol-
lowing can be solved: man is to king as woman is
to x. With simple arithmetic on vectors this prob-
lem can be solved by proposing x=queen (Boluk-
basi et al., 2016), because
−−→
man −−−−−−→
woman ≈−−→
king −−−−→
queen.
Even if not perfectly equal to any vector in the
vocabulary, the closest vector to the resultant will
often be the answer to the question (Hapke et al.,
2019). This is useful for different types of appli-
cations, for example word embeddings are an im-
portant source of evidence for document ranking
(Nalisnick et al., 2016) (Mitra et al., 2016). How-
ever, this relationship between words can also con-
tain problematic associations. Research demon-
strated that words like he or man are associated
to jobs like programmer or doctor, whereas words

--- Page 2 ---

Figure 1: Example of bias in Google Translate.
like she or woman are associated to jobs like
homemaker or nurse (Bolukbasi et al., 2016) (Lu
et al., 2018).
For example, it has been shown
(Bolukbasi et al., 2016) that
−−→
man −−−−−−→
woman ≈
−−−−−−−−−−−−−−−−→
computerprogrammer −−−−−−−−−→
homemaker.
Human bias in psychology is often measured
using Implicit Association Test (IAT) (Greenwald
et al., 1998). The IAT measures differences in the
response time of the human subjects, when they
are asked to pair two concepts. Whenever they
ﬁnd these concepts similar, the response time is
shorter than when they ﬁnd the concepts different.
Based on these results, a corresponding measure
based on word embeddings instead of human sub-
jects has been developed, called Word Embedding
Association Test (WEAT) (Caliskan et al., 2017).
The WEAT allows to demonstrate different types
of bias in word embeddings, replacing the reac-
tion time from IAT with word similarity (i.e. dis-
tance between word vectors).
The method has
been further developed and applied (e.g. (Karve
et al., 2019) (May et al., 2019)), but mostly for
the English language and gender bias.
We ap-
ply this method to pre-trained word embeddings
in German and French, and address the following
research questions:
• Can known gender and origin bias found in
pre-trained English word embeddings be con-
ﬁrmed for German and French?
• Can we identify different forms of gender
bias in German word embeddings?
The paper will ﬁrst discuss the related work and
provide more details about the used methods. We
will then describe the experimental setup. In the
end, the results will be presented and discussed.
2
Related Work
2.1
Word Embeddings
Unless a domain-speciﬁc word model is required,
pre-trained word vector representations are suf-
ﬁcient, and are easily available online as open-
source (Hapke et al., 2019). In the following para-
graphs we shortly describe the most common word
embedding training techniques:
word2vec
was ﬁrst presented in 2013 (Mikolov
et al., 2013b) (Mikolov et al., 2013a) (Mikolov
et al., 2013c). These word embeddings provided a
surprising accuracy improvement on several NLP
tasks, and can be trained in two different ways
(Hapke et al., 2019): with the skip-gram approach
using a word of interest as an input, or with the
continuous bag-of-words approach using nearby
words as input.
GloVe
provides another technology for generat-
ing word embeddings (Pennington et al., 2014).
Whereas word2vec relies on a neural network with
backpropagation, GloVe uses direct optimization.
fastText
provides an improvement to word2vec
(Bojanowski et al., 2017). Instead of predicting
the surrounding words, it predicts the surrounding
n-character grams. This results in the advantage
to handle rare words much better than the original
approach (Hapke et al., 2019). Pre-trained models
are available in 157 languages (Grave et al., 2018).
2.2
Bias Identiﬁcation in Training Data
There is a concern that artiﬁcial intelligence
and smart decision making will amplify cultural
stereotypes (Barocas and Selbst, 2016). Due to
historical unfairness, which is represented in the
training data, unfair decisions can be made in the
future.
Research has shown that such bias can

--- Page 3 ---

be identiﬁed, for example by using bayesian net-
works (Mancuhan and Clifton, 2014). Commonly
used datasets such as Wikipedia have been proven
to be biased (Wagner et al., 2015) (Wagner et al.,
2016). In particular, it was also shown how dialect
can lead to racial bias in common training data for
hate speech detection (Sap et al., 2019).
Recent research concentrates on bias identiﬁca-
tion in word embeddings. The state-of-the-art will
be presented in the next subsection.
2.3
Bias Identiﬁcation in Word Embeddings
In the original WEAT paper (Caliskan et al.,
2017), several different IAT results have been con-
ﬁrmed on pre-trained GloVe and word2vec word
embeddings for the English language.
Due to
their experiments on off-the-shelf machine learn-
ing components, they demonstrate that cultural
stereotypes have already propagated to state-of-
the-art artiﬁcial intelligence applications.
The
WEAT has become a common method to mea-
sure bias in word embeddings, being used as a
metric when developing methods to reduce bias in
word embeddings (Karve et al., 2019). The au-
thors identiﬁed different biases, in particular the
following categories of gender bias: career vs.
family activities, Maths vs. Arts and Science vs.
Arts. Furthermore, they detected racial bias con-
cerning African-Americans by comparing Euro-
pean American and African American names.
Other research proposed a framework for tem-
poral analysis of word embeddings and observed
bias changing over time and relating it to historical
events (Garg et al., 2018). The approach helped to
quantify stereotypes and attitudes towards women
and ethnic minorities in the United States in the
20th and 21st century.
The WEAT has also been applied to word
embeddings that were trained for different spe-
ciﬁc domains (Twitter,Wikipedia-based gender-
balanced corpus GAP, PubMed and Google News)
(Chaloner and Maldonado, 2019).
The authors
conﬁrmed a statistically signiﬁcant gender bias for
all experiments on the Google News corpus (and
for some of the experiments on the other corpora).
It has been shown that current bias mitiga-
tion methods cannot directly be applied to lan-
guages with grammatical gender such as French
or Spanish (Zhou et al., 2019). However, the au-
thors show that different types of bias can still be
identiﬁed for those languages. They also present
the Modiﬁed Word Embedding Association Test
(MWEAT), which is then used to evaluate the bias
in the Spanish language.
The WEAT was extended to measure bias in
state-of-the-art sentence encoders (May et al.,
2019).
The Sentence Encoder Association test
(SEAT) enters the words from the WEAT exper-
iments into sentence templates such as ”This is
a[n] <word>”.
The results suggest that recent
sentence encoders exhibit less bias than previous
models, but future research to further clarify this
is suggested. The research focusses on English
sentences only. As WEAT, SEAT can only detect
presence of bias, but not its absence.
Other research (Friedman et al., 2019) identiﬁes
gender bias in word embeddings trained on Twitter
data from 99 countries and 51 U.S. regions. The
results are then validated against statistical gender
gaps in 18 international and 5 U.S. based statis-
tics. In this research only tweets in English were
considered.
It has been explored (McCurdy and Serbetci,
2017) whether word embeddings in languages
with grammatical gender show the same topical
semantic bias as in English.
In particular, the
authors show that for German there is a positive
differential association, but the WEAT shows re-
liable effects only for the evaluated natural gen-
der languages English and Dutch.
The training
data was prepared from the OpenSubtitles corpus
(Lison and Tiedemann, 2016) with translations in
German, Spanish, Dutch and English.
3
Method
3.1
WEAT method
The terminology of WEAT (Caliskan et al., 2017)
is borrowed from the Implicit Association Test
(IAT) (Greenwald et al., 1998) from psychology.
The IAT measures a person’s subconscious as-
sociation between concepts and therefore gives a
measure for implicit bias. It is a computer-based
measure, where users are asked to rapidly cate-
gorize two target concepts with an attribute. The
IAT questions are based on combining possible an-
swers to parallel non-biased questions, and there-
fore implicit stereotypes can be assessed. Easier
pairing (i.e., shorter reaction time) is interpreted
as as stronger association between the concepts.
In the background, the experiment consists
of two sets of target words,
as for exam-
ple (math, algebra, ...) and (art, poetry, ...).

--- Page 4 ---

Furthermore, two sets of attribute words are
deﬁned, as for example (man, male, ...) and
(woman, female, ...)
In WEAT, the distance between vectors corre-
sponds to the reaction time in IAT. As a measure
of distance between the vectors, the cosine simi-
larity between the vectors is used.
The null hypothesis is that there is no difference
between the two sets of target words with regard
to relative similarity to the two sets of attribute
words. In other words, there is no bias between
the genders regarding the target word groups.
The WEAT test can be formalized as follows
(Caliskan et al., 2017): X and Y are the two sets
of target words of equal size. A and B are the two
sets of attribute words. s(X, Y, A, B) is the test
statistics.
s(X, Y, A, B) =
X
x∈X
s(x, A, B)−
X
y∈Y
s(y, A, B)
(1)
where
s(w, A, B) =
meana∈Acos(⃗w,⃗a) −meanb∈Bcos(⃗w,⃗b)
s(w, A, B) measures the association of w with
the attribute. s(X, Y, A, B) measures the differen-
tial association of the two sets of target words with
the attribute. In the equation, cos(⃗a,⃗b) deﬁnes the
cosine of the angle between the vectors ⃗a and ⃗b,
which we use to measure the distance between the
two vectors.
In WEAT, a permutation test is used to measure
the (un)likelihood of the null hypothesis, i.e. they
compute the probability that a random permuta-
tion of the attribute words would produce the ob-
served (or greater) difference in sample means.
{(Xi, Yi)} denotes all the partitions of X ∪Y
into two sets of equal size. The one-sided p-value
is then deﬁned as (Caliskan et al., 2017):
Pri[s(Xi, Yi, A, B) > s(X, Y, A, B)]
(2)
In our implementation, instead of the full per-
mutation test we implemented a randomization
test with 100’000 iterations, following (Chaloner
and Maldonado, 2019).
The effect size is computed as Cohen’s d (as for
the original IAT). The effect size d is computed as
(Caliskan et al., 2017)
meanx∈Xs(x, A, B) −meany∈Y s(y, A, B)
stddevw∈X∪Y s(w, A, B)
(3)
3.2
Experimental Setup
This section describes the different experiments
we executed in our implementation of the WEAT
and pre-trained word embeddings in different lan-
guages.
3.2.1
Validation: WEAT experiments
To validate our implementation, we executed se-
lected experiments in English (WEAT 5 for origin
bias and WEAT 6-8 for gender bias) from the orig-
inal WEAT paper (Caliskan et al., 2017).
In a ﬁrst experiment, European American and
African American names are used, along with
pleasant and unpleasant attributes (WEAT5-ori,
detailed setup in Table 1).
We then deﬁned the targets as male and female
names and the attributes as words regarding career
and family (WEAT6-ori, detailed setup in Table
2).
Another experiment considers words from
maths and arts as targets, and female and male
terms as attributes. Table 4 shows the exact terms
of the experiment. We ﬁrst executed this experi-
ments in its original form (WEAT7-ori). We then
also executed it in a reduced form (words in italic
were skipped), in order to match what the German
and French experiments explained in the next sec-
tions (WEAT7-mod).
We then executed an experiment that considers
words from science and arts as targets, and male
and female attributes.
Table 4 shows the exact
terms of the experiment. We ﬁrst executed this ex-
periments in its original form (WEAT8-ori). We
then also executed it in a reduced form (words in
italic were skipped), in order to match what the
German and French experiments explained in the
next sections (WEAT8-mod).
WEAT 5-7 are based on an existing Implicit As-
sociation Test (IAT) from literature (Nosek et al.,
2002a), as well as WEAT 8 (Nosek et al., 2002b).

--- Page 5 ---

Group
WEAT5-ori
WEAT5-ger
WEAT5-fr
Group 1
Brad, Brendan, Geoffrey, Greg,
Brett, Jay, Matthew, Neil, Todd,
Allison, Anne, Carrie, Emily, Jill,
Laurie, Kristen, Meredith, Sarah
Peter, Daniel, Hans, Thomas, An-
dreas, Martin, Markus, Michael,
Maria,
Anna,
Ursula,
Ruth,
Monika, Elisabeth, Verena, Sandra
Jean,
Daniel,
Michel,
Pierre,
David, Philippe, Nicolas, Jos´e,
Maria, Marie, Anne, Catherine,
Nathalie, Ana, Isabelle, Christine
Group 2
Darnell, Hakim, Jermaine, Ka-
reem,
Jamal,
Leroy,
Rasheed,
Tremayne, Tyrone, Aisha, Ebony,
Keisha, Kenya, Latonya, Lakisha,
Latoya, Tamika, Tanisha
Ladina,
Fatima,
Fatma,
Alma,
Soraya,
Svetlana,
Elif,
Vesna,
Mehmet,
Mustafa,
Aleksandar,
Mohamed,
Ibrahim,
Dragan,
Hasan, Mohammad
Ladina,
Fatima,
Fatma,
Alma,
Soraya,
Svetlana,
Elif,
Vesna,
Mehmet,
Mustafa,
Aleksandar,
Mohamed,
Ibrahim,
Dragan,
Hasan, Mohammad
Pleasant
joy, love, peace, wonderful, plea-
sure, friend, laughter, happy
Spass, Liebe, Frieden, wunderbar,
Freude, Lachen, gl¨ucklich
joie,
amour,
paix,
magniﬁque,
plaisir, ami, rire, enthousiaste
Unpleasant
agony,
terrible,
horrible,
nasty,
evil, war, awful, failure
Qual, furchtbar, schrecklich, ¨ubel,
b¨ose, Krieg, scheusslich, Versagen
souffrance,
terrible,
horrible,
d´esagr´eable, mal, guerre, abom-
inable, d´efaillance
Table 1: The terms from the original WEAT 5 experiment (Caliskan et al., 2017) and our adaptations/translations
to German and French.
Group
WEAT6-ori
WEAT6-ger1
WEAT6-fr1
Male names
John, Paul, Mike, Kevin, Steve,
Greg, Jeff, Bill
Peter, Daniel, Hans, Thomas, An-
dreas, Martin, Markus, Michael
Jean,
Daniel,
Michel,
Pierre,
David, Philippe, Nicolas, Jos´e
Female
names
Amy, Joan, Lisa, Sarah, Diana,
Kate, Ann, Donna
Maria,
Anna,
Ursula,
Ruth,
Monika, Elisabeth, Verena, Sandra
Maria, Marie, Anne, Catherine,
Nathalie, Ana, Isabelle, Christine
Career
executive,
management,
profes-
sional, corporation, salary, ofﬁce,
business, career
F¨uhrungskraft, Verwaltung, beru-
ﬂich,
Konzern,
Gehalt,
B¨uro,
Gesch¨aft, Werdegang
´equipe,
gestion,
profession,
soci´et´e, salaire, bureau, affaires,
carri`ere
Family
home, parents, children, family,
cousins, marriage, weddings, rela-
tives
Zuhause, Eltern, Kinder, Fami-
lie, Cousinen, Ehe, Hochzeit, Ver-
wandtschaft
maison, parents, enfants, famille,
cousins, mariage, noces, proches
Table 2: The terms from the original WEAT 6 experiment (Caliskan et al., 2017) and our adaptations/translations
to German and French for names in Switzerland.
3.2.2
Reproduction of WEAT 5-8 for German
We translated and/or adapted the experiments to
execute them on German pre-trained word embed-
dings as described in the next paragraphs.
WEAT5-ger
We reproduced the origin experi-
ment that connected names of speciﬁc origins to
pleasant or unpleasant words for German.
We
selected originally Swiss German names by us-
ing the 8 most common names of the German
part of Switzerland for women and men respec-
tively1. We then selected manually a list of com-
monly used names in Switzerland that are of dif-
ferent origin from the same source. These names
were chosen as representatives of names of for-
eign origin. A German study has shown that the
origin of the name has a major impact on the suc-
cess of job applications (Schneider et al., 2014).
Instead of focussing on the percentage of different
minorities of the population, which is complicated
due to regional differences, we selected commonly
1Bundesamt f¨ur Statistik - Vornamen der Bev¨olkerung
nach Jahrgang, Schweiz und Sprachgebiete, 2018
used names of different origins, based on the list
of the most common names in Switzerland men-
tioned before. The pleasant and unpleasant terms
were translated to German. Table 1 shows the ex-
act terms of the experiment.
WEAT6-ger1 and WEAT6-ger2
We repro-
duced the gender experiment regarding career vs.
family attributes for German.
In a ﬁrst experi-
ment (WEAT6-ger1), we used the 8 most com-
mon names of the German part of Switzerland for
women and men respectively2. In a second exper-
iment (WEAT6-ger2), we used the most common
names of adults living in Germany3. The career
and family terms were translated to German. Ta-
bles 2 and 3 show the exact terms used in the ex-
periments.
WEAT7-ger and WEAT8-ger
We reproduced
the gender experiment regarding Math vs. Arts
2Bundesamt f¨ur Statistik - Vornamen der Bev¨olkerung
nach Jahrgang, Schweiz und Sprachgebiete, 2018
3https://www.beliebte-vornamen.de/49519-
erwachsene.htm

--- Page 6 ---

Group
WEAT6-ori
WEAT6-ger2
WEAT6-fr2
Male names
John, Paul, Mike, Kevin, Steve,
Greg, Jeff, Bill
Michael, Thomas, Andreas, Peter,
Stefan, Christian, Hans, Klaus
Jean,
Pierre,
Michel,
Andr´e,
Philippe, Ren´e, Louis, Alain
Female
names
Amy, Joan, Lisa, Sarah, Diana,
Kate, Ann, Donna
Sabine, Susanne, Petra, Monika,
Claudia, Birgit, Andrea, Stefanie
Marie,
Jeanne,
Franc¸oise,
Monique,
Catherine,
Nathalie,
Isabelle, Jacqueline
Career
executive,
management,
profes-
sional, corporation, salary, ofﬁce,
business, career
F¨uhrungskraft, Verwaltung, beru-
ﬂich,
Konzern,
Gehalt,
B¨uro,
Gesch¨aft, Werdegang
´equipe,
gestion,
profession,
soci´et´e, salaire, bureau, affaires,
carri`ere
Family
home, parents, children, family,
cousins, marriage, weddings, rela-
tives
Zuhause, Eltern, Kinder, Fami-
lie, Cousinen, Ehe, Hochzeit, Ver-
wandtschaft
maison, parents, enfants, famille,
cousins, mariage, noces, proches
Table 3: The terms from the original WEAT 6 experiment (Caliskan et al., 2017) and our adaptations/translations
to German and French for names in Germany and France.
Group
WEAT7-ori/mod
WEAT7-ger
WEAT7-fr
Math
math, algebra, geometry, calculus,
equations, computation, numbers,
addition
Mathematik, Algebra, Geometrie,
Calculus,
Gleichungen,
Berech-
nung, Zahlen, Addition
math´ematiques,
alg`ebre,
g´eom´etrie,
calcul,
´equations,
calcul, nombres, addition
Arts
poetry, art, dance, literature, novel,
symphony, drama, sculpture
Poesie, Kunst, Tanz, Literatur, Ro-
man, Symphonie, Drama, Skulptur
po´esie, art, danse, litt´erature, ro-
man, symphonie, drame, sculpture
Male terms
male, man, boy, brother, he, him,
his, son
m¨annlich, Mann, Junge, Bruder,
Sohn
masculin, homme, copain, fr`ere,
ﬁls
Female
terms
female, woman, girl, sister, she,
her, hers, daughter
weiblich,
Frau,
M¨adchen,
Schwester, Tochter
f´eminine, femme, copine, soeur,
ﬁlle
Table 4: The terms from the original WEAT 7 experiment (Caliskan et al., 2017) and our adaptations/translations
to German and French.
and Science vs. Arts for German. The pronouns in
the attribute terms were skipped, because of con-
ﬂicts with other terms. For example, sie can he
she, but also they; or sein could be his but also
refer to the verb to be. We considered NASA, Ein-
stein and Shakespeare as internationally known
and kept these words for the German experiments.
Tables 4 and 5 show the exact terms of the experi-
ment.
3.2.3
Reproduction of WEAT 6-8 for French
We translated and/or adapted the experiments to
execute them on French pre-trained word embed-
dings as described in the next paragraphs.
WEAT5-fr
We reproduced the experiment that
connects names of speciﬁc origins to pleasant or
unpleasant words in French.
We selected orig-
inally Swiss French names by using the 8 most
common names of the French part of Switzerland
for women and men respectively4. We then se-
lected manually a list of commonly used names
in Switzerland that are of different origin from
the same source (as described in the experiment
WEAT5-ger). The pleasant and unpleasant terms
4Bundesamt f¨ur Statistik - Vornamen der Bev¨olkerung
nach Jahrgang, Schweiz und Sprachgebiete, 2018
were translated to French.
In the translation,
words that have the same form for male and female
(e.g. magniﬁque instead of merveilleux) were pre-
ferred, in order to provide consistency in the num-
ber of terms used in English and German. Table 1
shows the exact terms of the experiment.
WEAT6-fr1 and WEAT6-fr2
We reproduced
the gender experiment regarding career vs. family
attributes for French. To translate the female and
male names, in a ﬁrst experiment (WEAT6-fr1),
we used the 8 most common names of the French
part of Switzerland for women and men5. In a sec-
ond experiment (WEAT6-fr2) we used the most
common names in metropolitan France given be-
tween 1943 and 2019 6. The word executive leads
to a French word with a male and a female form.
It was therefore replaced by the business related
word ´equipe. Tables 2 and 3 show the exact terms
of the experiments.
WEAT7-fr and WEAT8-fr
As in German,
pronouns were skipped.
Additionally, we re-
placed girl/boy with copain/copine (in english:
5Bundesamt f¨ur Statistik - Vornamen der Bev¨olkerung
nach Jahrgang, Schweiz und Sprachgebiete, 2018
6https://tinyurl.com/tkgubf5

--- Page 7 ---

Group
WEAT8-ori/mod
WEAT8-ger
WEAT8-fr
Science
science,
technology,
physics,
chemistry,
Einstein,
NASA,
experiment, astronomy
Wissenschaft,
Technologie,
Physik, Chemie, Einstein, NASA,
Experiment, Astronomie
science,
technologie,
physique,
chimie,
Einstein,
NASA,
exp´erience, astronomie
Arts
poetry, art, Shakespeare, dance, lit-
erature, novel, symphony, drama
Poesie, Kunst, Shakespeare, Tanz,
Literatur,
Roman,
Symphonie,
Drama
po´esie, art, Shakespeare, danse,
litt´erature,
roman,
symphonie,
drame
Male terms
brother, father, uncle, grandfather,
son, he, his, him
Bruder, Vater, Onkel, Grossvater,
Sohn
fr`ere, p`ere, oncle, grand-p`ere, ﬁls
Female
terms
sister, mother, aunt, grandmother,
daughter, she, hers, her
Schwester, Mutter, Tante, Gross-
mutter, Tochter
soeur, m`ere, tante, grande-m`ere,
ﬁlle
Table 5: The terms from the original WEAT 8 experiment (Caliskan et al., 2017) and our adaptations/translations
to German and French.
boyfriend/girlfriend), because the French word
ﬁlle can be both girl and daughter. For the gender-
speciﬁc adjectives we picked the male version
for masculin and the female version for f´eminine,
since we expect these words to appear more fre-
quently.
We considered NASA, Einstein and
Shakespeare as internationally known and kept
these words for the French experiments. Tables
4 and 5 show the exact terms of the experiments.
3.2.4
Additional Gender Stereotypes in
German Word Embeddings
Based on real-world bias we deﬁned the following
two additional experiments for German:
GER-1
Study choice in Switzerland is often a
matter of gender. A report about equal opportuni-
ties in Switzerland (Dubach et al., 2017) indicates
that at least four out of ﬁve students are female
in subjects such as special pedagogy, veterinary
medicine, ethnology, educational science and psy-
chology. On the other side, in technical studies
such as mechanical engineering or computer sci-
ence, only around 10-20% of the students are fe-
male. In this experiment we examine whether this
bias is reﬂected in the word embeddings. We se-
lected the ﬁve subjects with the highest percentage
of women in 2015 (Dubach et al., 2017) (special
pedagogy, veterinary medicine, ethnology, educa-
tional science, psychology). We then picked the
ﬁve subjects with the lowest percentage of women
in 2015 (Dubach et al., 2017) (electrical engineer-
ing, mechanical engineering, computer science,
microtechnology and physics).
The same male
and female terms as for the WEAT7 experiment
which considers the different interest of men and
women in arts and maths were used for this exper-
iment. We therefore deﬁned target and attribute
word sets as shown in Table 6.
GER-2
Studies have shown the perception of
the roles of men and women in the 18th cen-
tury based on dictionary entries from that time
(Hausen, 1981).
Based on these results, a list
of words describing men and women was de-
duced7.
The list is separated in different cat-
egories describing the role of women and men
in the society: Bestimmung f¨ur (engl. intended
for), Aktivit¨at/Passivit¨at (engl. activity/passivity),
Tun/Sein (engl.
doing/being), and their charac-
ters: Rationalit¨at/Emotionalit¨at (engl.
rational-
ity/emotionality), Tugenden (engl.
virtues).
In
this study we focussed on the words indicating the
characters of men and women to verify whether
these stereotypes are still reﬂected in today’s word
embeddings.
We therefore selected the words
from the category Rationalit¨at/Emotionalit¨at for
our experiment.
The category Tugenden was
skipped due to the different number of male and
female words. We therefore deﬁned the experi-
ment as shown in Table 7.
3.3
Data Sets: Pre-trained Word
Embeddings
The validation experiments in English were exe-
cuted on the same pre-trained word embeddings as
in the original experiments (Caliskan et al., 2017):
• GloVe pre-trained word embeddings using
the ”Common Crawl” corpus (300 dimen-
sions) with 840 billion tokens8
• word2vec pre-trained word embeddings us-
ing Google News (300 dimensions)9
The German and the French experiments were
7https://de.wikipedia.org/wiki/Geschlechterrolle - Abbil-
dung Polarisierung der Geschlechterrolle im 18. Jahrhundert
8https://nlp.stanford.edu/projects/glove/
9https://code.google.com/archive/p/word2vec/

--- Page 8 ---

Group
GER-1
English
Study
Elektroingenieurwesen,
Maschineningenieurwesen,
Informatik, Mikrotechnik, Physik
Electrical
Engineering,
Mechanical
Engineering,
Computer Science, Microtechnology, Physics
Study
Sonderp¨adagogik,
Veterin¨armedizin,
Ethnologie,
Erziehungswissenschaften, Psychologie
Special Pedagogy, Veterinary Medicine, Ethnology,
Educational Science, Psychology
Male terms
m¨annlich, Mann, Junge, Bruder, Sohn
male, man, boy, brother, son
Female
terms
weiblich, Frau, M¨adchen, Schwester, Tochter
female, woman, girl, sister, daughter
Table 6: Experiment GER-1 veriﬁes if existing bias in study selection appears also in German word embeddings
(with English translations for better readability).
Group
GER-2
English
Character
Geist, Vernunft, Verstand, Denken, Wissen, Urteilen
Mind, Rationality, Realisation, Thinking, Knowing,
Judging
Character
Gef¨uhl, Empﬁnden, Empf¨anglichkeit, Rezeptivit¨at,
Religiosit¨at, Verstehen
Feeling, Sentiment, Receptiveness, Religiousness, Un-
derstanding
Male terms
m¨annlich, Mann, Junge, Bruder, Sohn
male, man, boy, brother, son
Female
terms
weiblich, Frau, M¨adchen, Schwester, Tochter
female, woman, girl, sister, daughter
Table 7: Experiment GER-2 veriﬁes if existing historical bias appears also in German word embeddings (with
English translations for better readability).
Experiment
p-value
Effect
size d
Bias
detected?
GloVe
WEAT5-ori
< 10−3
1.36
✓
WEAT6-ori
< 10−3
1.8
✓
WEAT7-ori
0.058
0.94
(✓)
WEAT8-ori
0.0097
1.24
✓
WEAT7-mod
0.026
1.09
✓
WEAT8-mod
0.01
1.2
✓
word2vec
WEAT5-ori
0.02937
0.72
✓
WEAT6-ori
< 10−3
1.88
✓
WEAT7-ori
0.039
0.99
✓
WEAT8-ori
0.008
1.24
✓
WEAT7-mod
0.04
0.99
✓
WEAT8-mod
0.008
1.24
✓
Table 8: Results of the validation: conﬁrming the re-
sults of the original WEAT paper (Caliskan et al., 2017)
for the English language on the GloVe and word2vec
dataset. We report p-values (p) and absolute value of
effect size (d).
executed using pre-trained fastText10 word em-
beddings with 300 dimensions trained on Com-
monCrawl and Wikipedia (Grave et al., 2018).
Other word embeddings were considered, but they
had either less dimensions (e.g. (Kutuzov et al.,
2017)) or missing words in the vocabulary which
were relevant for our experiments.
Experiment
p-value
Effect
size d
Bias
detected?
German
WEAT5-ger
< 10−3
1.134
✓
WEAT6-ger1
< 10−3
1.62
✓
WEAT6-ger2
0.003
1.44
✓
WEAT7-ger
0.65
0.23
×
WEAT8-ger
0.83
0.11
×
GER-1
< 10−3
1.74
✓
GER-2
0.002
1.43
✓
French
WEAT5-fr
< 10−3
1.29
✓
WEAT6-fr1
0.14
0.75
×
WEAT6-fr2
0.03
1.03
✓
WEAT7-fr
0.2
0.62
×
WEAT8-fr
0.53
0.32
×
Table 9: Results of the German and French experi-
ments: translated and adapted WEAT experiments and
new deﬁned experiments. We report p-values (p) and
absolute value of effect size (d).
4
Results
In this work, we consider a statistically signiﬁ-
cant bias if the p-value is below 0.05, following
(Chaloner and Maldonado, 2019) and (Caliskan
et al., 2017).
We conﬁrmed the bias detected by (Caliskan
et al., 2017) in the WEAT 5-8 experiments for
the English language (both GloVe and word2vec
datasets). Table 8 lists the detailed results.
Whereas the original WEAT5 experiment con-
10https://fasttext.cc/docs/en/crawl-vectors.html

--- Page 9 ---

sidered European American and African Amer-
ican names, in our experiment common Swiss
names (German and French speaking area respec-
tively) and common names in Switzerland of dif-
ferent origin were considered. We were able to
measure statistically signiﬁcant bias based on the
origin of the name, in relation to pleasant and un-
pleasant words, for both German and French.
In the WEAT6 experiments for German, we
were able to demonstrate that there is a statis-
tically signiﬁcant gender bias for the categories
family and career, for the most common names
from Germany and also Switzerland. For WEAT6
in French, we could not obtain statistically signiﬁ-
cant results for Switzerland. However, the WEAT
method can only detect presence of bias, but not
its absence. Therefore, future research is neces-
sary to further investigate this topic. For the most
common names in France, a signiﬁcant bias for the
WEAT6 experiment was shown.
We could not obtain statistically signiﬁcant
results for the word categories math vs.
arts
(WEAT7) and science vs. arts (WEAT8) for Ger-
man and French.
However, we identiﬁed two new sets of words in
German for which we could identify a statistically
signiﬁcant bias. On one side, we conﬁrmed that
there is a gender bias in the word categories for
different subjects of study (GER-1). On the other
side, historical gender bias from the 18th century
was found to be still present in today’s word em-
beddings (GER-2).
The detailed results for the German and French
experiments are listed in Table 9.
5
Discussion
We conﬁrmed existing results for gender and
origin bias in English word embeddings, and
examined selected word sets for German and
French word embeddings. Whereas we could par-
tially conﬁrm the translated (and where necessary
adapted) results of the English experiments for
German and French, we identiﬁed new word sets
for bias in German word embeddings. The iden-
tiﬁed word sets indicate that speciﬁc regional or
cultural stereotypes are included in word embed-
dings and therefore the bias detection may vary
among different languages. Future work needs to
further investigate the directions proposed in this
paper and extend the word sets our work has iden-
tiﬁed.
We identiﬁed a bias towards names from differ-
ent origin. We can therefore conﬁrm that stereo-
types based on names present in our society, e.g.
on the labour market (Schneider et al., 2014), are
also existing in word embeddings.
We worked
with a selection of names to get a ﬁrst indication,
future work must further study the differences be-
tween names encoded in word embeddings. Next
to the origin, it has been shown that different prej-
udices such as age, the attractiveness and the intel-
ligence of the person with the corresponding name
exist (Rudolph et al., 2007), or that teachers per-
ceive students differently, based on their names
(Kube, 2009). Our results indicate that there is po-
tential to further explore existing stereotypes and
prejudices in names also in word embeddings and
their implication in smart decision making.
Our results on word embeddings suggest an im-
pact on applications using machine learning or AI.
Previous studies have raised the concern that such
technologies may perpetuate cultural stereotypes
(Barocas and Selbst, 2016) and it has been dis-
cussed whether all implicit human biases are re-
ﬂected in the statistical properties of languages
(Caliskan et al., 2017). Therefore, whenever we
build a system that is capable of understanding or
producing natural languages (e.g. text generation,
machine translation), it risks to learn the stereo-
types and prejudices included in the language as
well. Further research to precisely measure the
different types of bias in such language models
and mitigate the bias is therefore required. Future
work should also identify how the observed bias in
word embeddings can be related to the exact text
from which they originate.
6
Conclusion
Although we partially conﬁrmed the existing gen-
der and origin bias also in German and French
word embeddings, we showed in this research that
known bias in pre-trained English word embed-
dings comes in a different form in German. We
demonstrated that real-world bias and stereotypes
from the 18th century are still included in today’s
word embeddings in German. Our results indicate
that there are cultural differences that need to be
considered in future work.
The results were obtained from publicly avail-
able pre-trained embeddings. Future work to iden-
tify and mitigate bias in word embeddings in dif-
ferent languages is therefore highly relevant.

--- Page 10 ---

References
Solon Barocas and Andrew D Selbst. 2016. Big data’s
disparate impact. Calif. L. Rev., 104:671.
Piotr Bojanowski, Edouard Grave, Armand Joulin, and
Tomas Mikolov. 2017. Enriching word vectors with
subword information. Transactions of the Associa-
tion for Computational Linguistics, 5:135–146.
Tolga Bolukbasi, Kai-Wei Chang, James Y Zou,
Venkatesh Saligrama, and Adam T Kalai. 2016.
Man is to computer programmer as woman is to
homemaker? debiasing word embeddings. In Ad-
vances in neural information processing systems,
pages 4349–4357.
Aylin
Caliskan,
Joanna
J
Bryson,
and
Arvind
Narayanan. 2017. Semantics derived automatically
from language corpora contain human-like biases.
Science, 356(6334):183–186.
Kaytlin Chaloner and Alfredo Maldonado. 2019. Mea-
suring gender bias in word embeddings across do-
mains and discovering new gender bias word cat-
egories. In Proceedings of the First Workshop on
Gender Bias in Natural Language Processing, pages
25–32.
Philipp Dubach, Victor Legler, Mario Morger, and
Heidi Stutz. 2017.
Frauen und M¨anner an
Schweizer Hochschulen: Indikatoren zur Chancen-
gleichheit in Studium und wissenschaftlicher Lauf-
bahn. SBFI.
Scott Friedman, Sonja Schmer-Galunder, Anthony
Chen, and Jeffrey Rye. 2019. Relating word embed-
ding gender biases to gender gaps: A cross-cultural
analysis. In Proceedings of the First Workshop on
Gender Bias in Natural Language Processing, pages
18–24.
Nikhil Garg, Londa Schiebinger, Dan Jurafsky, and
James Zou. 2018.
Word embeddings quantify
100 years of gender and ethnic stereotypes.
Pro-
ceedings of the National Academy of Sciences,
115(16):E3635–E3644.
Edouard Grave, Piotr Bojanowski, Prakhar Gupta, Ar-
mand Joulin, and Tomas Mikolov. 2018.
Learn-
ing word vectors for 157 languages. arXiv preprint
arXiv:1802.06893.
Anthony G Greenwald, Debbie E McGhee, and Jor-
dan LK Schwartz. 1998. Measuring individual dif-
ferences in implicit cognition: the implicit associa-
tion test. Journal of personality and social psychol-
ogy, 74(6):1464.
Hannes Max Hapke, Hobson Lane, and Cole Howard.
2019. Natural language processing in action.
Karin Hausen. 1981. Family and role-division: the po-
larisation of sexual stereotypes in the nineteenth cen-
tury—an aspect of the dissociation of work and fam-
ily life. The German Family: Essays on the Social
History of the Family in Nineteenth-and Twentieth-
Century Germany, pages 51–83.
Saket Karve, Lyle Ungar, and Jo˜ao Sedoc. 2019. Con-
ceptor debiasing of word representations evaluated
on weat. arXiv preprint arXiv:1906.05993.
Julia Isabell Kube. 2009. Vornamensforschung: Frage-
bogenuntersuchung bei Lehrerinnen und Lehrern,
ob
Vorurteile
bez¨uglich
speziﬁscher
Vornamen
von Grundsch¨ulern und davon abgeleitete er-
wartete speziﬁsche Pers¨onlichkeitsmerkmale vor-
liegen. Ph.D. thesis.
Andrei Kutuzov, Murhaf Fares, Stephan Oepen, and
Erik Velldal. 2017. Word vectors, reuse, and repli-
cability: Towards a community repository of large-
text resources. In Proceedings of the 58th Confer-
ence on Simulation and Modelling, pages 271–276.
Link¨oping University Electronic Press.
Pierre Lison and J¨org Tiedemann. 2016.
Opensub-
titles2016: Extracting large parallel corpora from
movie and tv subtitles.
Kaiji Lu, Piotr Mardziel, Fangjing Wu, Preetam Aman-
charla, and Anupam Datta. 2018.
Gender bias in
neural natural language processing. arXiv preprint
arXiv:1807.11714.
Koray Mancuhan and Chris Clifton. 2014. Combating
discrimination using bayesian networks. Artiﬁcial
intelligence and law, 22(2):211–238.
Chandler May, Alex Wang, Shikha Bordia, Samuel R
Bowman, and Rachel Rudinger. 2019.
On mea-
suring social biases in sentence encoders.
arXiv
preprint arXiv:1903.10561.
Katherine McCurdy and Oguz Serbetci. 2017. Gram-
matical gender associations outweigh topical gender
bias in crosslinguistic word embeddings. Proceed-
ings of WiNLP.
Tomas Mikolov, Kai Chen, Greg Corrado, and Jef-
frey Dean. 2013a.
Efﬁcient estimation of word
representations in vector space.
arXiv preprint
arXiv:1301.3781.
Tomas Mikolov, Ilya Sutskever, Kai Chen, Greg S Cor-
rado, and Jeff Dean. 2013b. Distributed representa-
tions of words and phrases and their compositional-
ity. In Advances in neural information processing
systems, pages 3111–3119.
Tom´aˇs Mikolov, Wen-tau Yih, and Geoffrey Zweig.
2013c. Linguistic regularities in continuous space
word representations. In Proceedings of the 2013
conference of the north american chapter of the as-
sociation for computational linguistics: Human lan-
guage technologies, pages 746–751.
Bhaskar Mitra, Eric Nalisnick, Nick Craswell, and
Rich Caruana. 2016.
A dual embedding space
model for document ranking.
arXiv preprint
arXiv:1602.01137.

--- Page 11 ---

Eric Nalisnick, Bhaskar Mitra, Nick Craswell, and
Rich Caruana. 2016. Improving document ranking
with dual word embeddings. In Proceedings of the
25th International Conference Companion on World
Wide Web, pages 83–84.
Brian A Nosek, Mahzarin R Banaji, and Anthony G
Greenwald. 2002a.
Harvesting implicit group at-
titudes and beliefs from a demonstration web site.
Group Dynamics: Theory, Research, and Practice,
6(1):101.
Brian A Nosek, Mahzarin R Banaji, and Anthony G
Greenwald. 2002b. Math= male, me= female, there-
fore math̸= me. Journal of personality and social
psychology, 83(1):44.
Jeffrey Pennington, Richard Socher, and Christopher D
Manning. 2014.
Glove: Global vectors for word
representation. In Proceedings of the 2014 confer-
ence on empirical methods in natural language pro-
cessing (EMNLP), pages 1532–1543.
Udo Rudolph, Robert B¨ohm, and Michaela Lummer.
2007.
Ein vorname sagt mehr als 1000 worte.
Zeitschrift f¨ur Sozialpsychologie, 38(1):17–31.
Maarten Sap, Dallas Card, Saadia Gabriel, Yejin Choi,
and Noah A Smith. 2019. The risk of racial bias in
hate speech detection. In Proceedings of the 57th
Annual Meeting of the Association for Computa-
tional Linguistics, pages 1668–1678.
Jan Schneider,
Ruta Yemane,
and Martin Wein-
mann. 2014.
Diskriminierung am Ausbildungs-
markt: Ausmaß, Ursachen und Handlungsperspek-
tiven. Sachverst¨andigenrat deutscher Stiftungen f¨ur
Integration und Migration GmbH ....
Tony Sun, Andrew Gaut, Shirlyn Tang, Yuxin Huang,
Mai ElSherief, Jieyu Zhao, Diba Mirza, Eliza-
beth Belding, Kai-Wei Chang, and William Yang
Wang. 2019. Mitigating gender bias in natural lan-
guage processing: Literature review. arXiv preprint
arXiv:1906.08976.
Claudia Wagner, David Garcia, Mohsen Jadidi, and
Markus Strohmaier. 2015. It’s a man’s wikipedia?
assessing gender inequality in an online encyclope-
dia. In Ninth international AAAI conference on web
and social media.
Claudia Wagner, Eduardo Graells-Garrido, David Gar-
cia, and Filippo Menczer. 2016.
Women through
the glass ceiling: gender asymmetries in wikipedia.
EPJ Data Science, 5(1):5.
Pei
Zhou,
Weijia
Shi,
Jieyu
Zhao,
Kuan-Hao
Huang, Muhao Chen, Ryan Cotterell, and Kai-
Wei Chang. 2019. Examining gender bias in lan-
guages with grammatical gender.
arXiv preprint
arXiv:1909.02224.

```
