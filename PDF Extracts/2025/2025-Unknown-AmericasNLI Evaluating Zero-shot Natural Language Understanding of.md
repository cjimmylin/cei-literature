---
title: "2025-Unknown-AmericasNLI Evaluating Zero-shot Natural Language Understanding of - PDF Extract"
source_pdf: "2025-Unknown-AmericasNLI Evaluating Zero-shot Natural Language Understanding of.pdf"
pages: 21
extracted_at: "2026-02-13T14:50:55.939007"
---

# PDF Extract: 2025-Unknown-AmericasNLI Evaluating Zero-shot Natural Language Understanding of

**Source PDF:** 2025-Unknown-AmericasNLI Evaluating Zero-shot Natural Language Understanding of.pdf
**Total Pages:** 21

---

## Content

```
--- Page 1 ---

AmericasNLI: Evaluating Zero-shot Natural Language Understanding
of Pretrained Multilingual Models in Truly Low-resource Languages
Abteen Ebrahimi♦
Manuel Mager♠
Arturo Oncevay♥
Vishrav Chaudhary§
Luis Chiruzzo△Angela Fan∇John E. OrtegaΩRicardo Ramosη
Annette Riosψ
Ivan Meza-Ruiz♯Gustavo A. Giménez-Lugo♣Elisabeth Mager♯Graham Neubig▷◁
Alexis Palmer♦Rolando Coto-Solano℧Ngoc Thang Vu♠Katharina Kann♦
▷◁Carnegie Mellon University
℧Dartmouth College
§Microsoft Turing
∇Facebook AI Research
ΩNew York University
△Universidad de la República, Uruguay
ηUniversidad Tecnológica de Tlaxcala
♯Universidad Nacional Autónoma de México
♣Universidade Tecnológica Federal do Paraná
♦University of Colorado Boulder
♥University of Edinburgh
♠University of Stuttgart
ψUniversity of Zurich
Abstract
Pretrained multilingual models are able to per-
form cross-lingual transfer in a zero-shot set-
ting, even for languages unseen during pre-
training. However, prior work evaluating per-
formance on unseen languages has largely
been limited to low-level, syntactic tasks, and
it remains unclear if zero-shot learning of
high-level, semantic tasks is possible for un-
seen languages. To explore this question, we
present AmericasNLI, an extension of XNLI
(Conneau et al., 2018) to 10 Indigenous lan-
guages of the Americas. We conduct experi-
ments with XLM-R, testing multiple zero-shot
and translation-based approaches.
Addition-
ally, we explore model adaptation via contin-
ued pretraining and provide an analysis of the
dataset by considering hypothesis-only mod-
els. We ﬁnd that XLM-R’s zero-shot perfor-
mance is poor for all 10 languages, with an av-
erage performance of 38.48%. Continued pre-
training offers improvements, with an average
accuracy of 43.85%. Surprisingly, training on
poorly translated data by far outperforms all
other methods with an accuracy of 49.12%.
1
Introduction
Pretrained multilingual models such as XLM
(Lample and Conneau, 2019), multilingual BERT
(mBERT; Devlin et al., 2019), and XLM-R (Con-
neau et al., 2020) achieve strong cross-lingual trans-
fer results for many languages and natural language
processing (NLP) tasks. However, there exists a
discrepancy in terms of zero-shot performance be-
tween languages present in the pretraining data and
those that are not: performance is generally highest
for well-represented languages and decreases with
less representation. Yet, even for unseen languages,
performance is generally above chance, and model
adaptation approaches have been shown to yield
Language
ISO
Family
Dev
Test
Aymara
aym
Aymaran
743
750
Asháninka
cni
Arawak
658
750
Bribri
bzd
Chibchan
743
750
Guaraní
gn
Tupi-Guaraní
743
750
Nahuatl
nah
Uto-Aztecan
376
738
Otomí
oto
Oto-Manguean
222
748
Quechua
quy
Quechuan
743
750
Rarámuri
tar
Uto-Aztecan
743
750
Shipibo-Konibo
shp
Panoan
743
750
Wixarika
hch
Uto-Aztecan
743
750
Table 1: The languages in AmericasNLI, along with
their ISO codes, language families, and dataset sizes.
further improvements (Muller et al., 2020; Pfeiffer
et al., 2020a,b; Wang et al., 2020).
Importantly, however, there are currently no
datasets for high-level, semantic tasks which fo-
cus solely on low-resource languages. As these
languages are most likely to be unseen to com-
monly used pretrained models, practically all work
evaluating unseen language performance and lan-
guage adaptation methods has been limited to low-
level, syntactic tasks such as part-of-speech tag-
ging, dependency parsing, and named-entity recog-
nition (Muller et al., 2020; Wang et al., 2020). This
largely limits our ability to draw more general con-
clusions with regards to the zero-shot learning abil-
ities of pretrained multilingual models for unseen
languages.
In this work, we introduce AmericasNLI, an ex-
tension of XNLI (Conneau et al., 2018) – a natural
language inference (NLI; cf. §2.3) dataset cover-
ing 15 high-resource languages – to 10 Indigenous
languages spoken in the Americas: Asháninka, Ay-
mara, Bribri, Guaraní, Nahuatl, Otomí, Quechua,
Rarámuri, Shipibo-Konibo, and Wixarika. All of
them are truly low-resource languages: they have
little to no digitally available labeled or unlabeled
arXiv:2104.08726v2  [cs.CL]  16 Mar 2022

--- Page 2 ---

data, and they are not typically studied by the main-
stream NLP community. The goal of this work
is two-fold: First, we hope to increase the visibil-
ity of these languages by providing a portion of
the resources necessary for NLP research. Sec-
ond, we aim to allow for a more comprehensive
study of multilingual model performance on un-
seen languages, where improvements will help ex-
tend the reach of NLP techniques to a larger set
of languages. We are speciﬁcally interested in the
following research questions: (1) Do pretrained
multilingual models still perform above random
chance for a high-level, semantic task in an un-
seen language? (2) Do methods aimed at adapting
models to unseen languages – previously exclu-
sively evaluated on low-level, syntactic tasks – also
increase performance on NLI? (3) Are translation-
based approaches effective for truly low-resource
languages, where translation quality is typically
very poor?1
We experiment with XLM-R, both with and with-
out model adaptation via continued pretraining on
monolingual corpora in the target language. Our
results show that the performance of XLM-R out-
of-the-box is moderately above chance, and model
adaptation leads to improvements of up to 5.86
percentage points. Training on machine-translated
training data, however, results in an even larger per-
formance gain of 11.13 percentage points over the
corresponding XLM-R model without adaptation.
We further perform an analysis via experiments
with hypothesis-only models, to examine poten-
tial artifacts which may have been inherited from
XNLI and ﬁnd that performance is above chance
for most models, but still below that for using the
full example.
AmericasNLI is publicly available2 and we hope
that it will serve as a benchmark for measuring the
zero-shot natural language understanding abilities
of multilingual models for unseen languages. Ad-
ditionally, we hope that our dataset will motivate
the development of novel pretraining and model
adaptation techniques which are suitable for truly
low-resource languages.
2
Background and Related Work
2.1
Pretrained Multilingual Models
Prior to the widespread use of pretrained trans-
former models, cross-lingual transfer was mainly
1We provide a sample of sentence pairs in Table D.3.
2https://github.com/abteen/americasnli
achieved through word embeddings (Mikolov et al.,
2013; Pennington et al., 2014; Bojanowski et al.,
2017), either by aligning monolingual embeddings
into the same embedding space (Lample et al.,
2018b,a; Grave et al., 2018) or by training multilin-
gual embeddings (Ammar et al., 2016; Artetxe and
Schwenk, 2019). Pretrained multilingual models
represent the extension of multilingual embeddings
to pretrained transformer models.
These models follow the standard pretraining–
ﬁnetuning paradigm: they are ﬁrst trained on unla-
beled monolingual corpora from various languages
(the pretraining languages) and later ﬁnetuned
on target-task data in a – usually high-resource
– source language.
Having been exposed to a
variety of languages through this training setup,
cross-lingual transfer results for these models are
competitive with the state of the art for many lan-
guages and tasks. Commonly used models are
mBERT (Devlin et al., 2019), which is pretrained
on the Wikipedias of 104 languages with masked
language modeling (MLM) and next sentence pre-
diction (NSP), and XLM, which is trained on 15
languages and introduces the translation language
modeling objective, which is based on MLM, but
uses pairs of parallel sentences. XLM-R has im-
proved performance over XLM, and trains on data
from 100 different languages with only the MLM
objective. Common to all models is a large shared
subword vocabulary created using either BPE (Sen-
nrich et al., 2016) or SentencePiece (Kudo and
Richardson, 2018) tokenization.
2.2
Evaluating Pretrained Multilingual
Models
Just as in the monolingual setting, where bench-
marks such as GLUE (Wang et al., 2018) and Su-
perGLUE (Wang et al., 2019) provide a look into
the performance of models across various tasks,
multilingual benchmarks (Hu et al., 2020; Liang
et al., 2020) cover a wide variety of tasks involv-
ing sentence structure, classiﬁcation, retrieval, and
question answering.
Additional work has been done examining what
mechanisms allow multilingual models to trans-
fer across languages (Pires et al., 2019; Wu and
Dredze, 2019). Wu and Dredze (2020) examine
transfer performance dependent on a language’s
representation in the pretraining data.
For lan-
guages with low representation, multiple methods
have been proposed to improve performance, in-

--- Page 3 ---

cluding extending the vocabulary, transliterating
the target text, and continuing pretraining before
ﬁnetuning (Lauscher et al., 2020; Chau et al., 2020;
Muller et al., 2020; Pfeiffer et al., 2020a,b; Wang
et al., 2020). In this work, we focus on continued
pretraining to analyze the performance of model
adaptation for a high-level, semantic task.
2.3
Natural Language Inference
Given two sentences, the premise and the hypothe-
sis, the task of NLI consists of determining whether
the hypothesis logically entails, contradicts, or is
neutral to the premise.
The most widely used
datasets for NLI in English are SNLI (Bowman
et al., 2015) and MNLI (Williams et al., 2018).
XNLI (Conneau et al., 2018) is the multilingual
expansion of MNLI to 15 languages, providing
manually translated evaluation sets and machine-
translated training sets. While datasets for NLI or
the similar task of recognizing textual entailment
exist for other languages (Bos et al., 2009; Alab-
bas, 2013; Eichler et al., 2014; Amirkhani et al.,
2020), their lack of similarity prevents a general-
ized study of cross-lingual zero-shot performance.
This is in contrast to XNLI, where examples for all
15 languages are parallel. To preserve this property
of XNLI, when creating AmericasNLI, we choose
to translate Spanish XNLI as opposed to creating
examples directly in the target language.
However, NLI datasets are not without issue:
Gururangan et al. (2018) show that artifacts from
the creation of MNLI allow for models to classify
examples depending on only the hypothesis, show-
ing that models may not be reasoning as expected.
Motivated by this, we provide further analysis of
AmericasNLI in Section 6 by comparing the perfor-
mance of hypothesis-only models to models trained
on full examples.
3
AmericasNLI
3.1
Data Collection Setup
AmericasNLI is the translation of a subset of XNLI
(Conneau et al., 2018). As translators between
Spanish and the target languages are more fre-
quently available than those for English, we trans-
late from the Spanish version. Additionally, some
translators reported that code-switching is often
used to describe certain topics, and, while many
words without an exact equivalence in the target
language are worked in through translation or inter-
pretation, others are kept in Spanish. To minimize
the amount of Spanish vocabulary in the translated
examples, we choose sentences from genres that
we judged to be relatively easy to translate into
the target languages: “face-to-face,” “letters,” and
“telephone.” We choose up to 750 examples from
each of the development and test set, with exact
counts for each language in Table 1.
3.2
Languages
We now discuss the languages in AmericasNLI. For
additional background on previous NLP research
on Indigenous languages of the Americas, we refer
the reader to Mager et al. (2018). A summary of
this information can be found in Table C.1.
Aymara
Aymara is a polysynthetic Amerindian
language spoken in Bolivia, Chile, and Peru by over
two million people (Homola, 2012). Aymara fol-
lows an SOV word order and has multiple dialects,
including Northern and Southern Aymara, spoken
on the southern Peruvian shore of Lake Titicaca as
well as around La Paz and, respectively, in the east-
ern half of the Iquique province in northern Chile,
the Bolivian department of Oruro, in northern Po-
tosi, and southwest Cochabamba. AmericasNLI
examples are translated into the Central Aymara
variant, speciﬁcally Aymara La Paz.
Asháninka
Asháninka is an Amazonian lan-
guage from the Arawak family, spoken by 73,567
people3 in Central and Eastern Peru, in a geograph-
ical region located between the eastern foothills of
the Andes and the western fringe of the Amazon
basin (Mihas, 2017). Asháninka is an agglutinat-
ing and polysynthetic language with a VSO word
order.
Bribri
Bribri is a Chibchan language spoken by
7,000 people in Southern Costa Rica (INEC, 2011).
It has three dialects, and while it is still spoken
by children, it is currently a vulnerable language
(Moseley, 2010; Sánchez Avendaño, 2013). Bribri
is a tonal language with SOV word order. There
are several orthographies which use different dia-
critics for the same phenomena, however even for
researchers who use the same orthography, the Uni-
code encoding of similar diacritics differs amongst
authors. Furthermore, the dialects of Bribri differ in
their exact vocabularies, and there are phonological
processes, like the deletion of unstressed vowels,
which also change the tokens found in texts. As
3https://bdpi.cultura.gob.pe/pueblos/
ashaninka

--- Page 4 ---

Language Premise
Hypothesis
en
And he said, Mama, I’m home.
He told his mom he had gotten home.
es
Y él dijo: Mamá, estoy en casa.
Le dijo a su madre que había llegado a casa.
aym
Jupax sanwa: Mamita, utankastwa.
Utar purinxtwa sasaw mamaparux sanxa
bzd
Ena ie’ iche: ãm`˜ı, ye’ tso’ ù a.
I ãm`˜ı a iché irir tö ye’ démine ù a.
cni
Iriori ikantiro: Ina, nosaiki pankotsiki.
Ikantiro iriniro yaretaja pankotsiki.
gn
Ha ha’e he’i: Mama, aime ógape.
He’íkuri isýpe oˆguahêhague hógape.
hch
metá mik+ petay+: ne mama kitá nepa yéka.
yu mama m+pa+ p+ra h+awe kai kename yu kitá he nuakai.
nah
huan yehhua quiihtoh: Nonantzin, niyetoc nochan quiilih inantzin niehcoquia
oto
xi nydi biênâ: maMe dimi an ngû
bimâbi o ini maMe guê o ngû
quy
Hinaptinmi pay nirqa: Mamay wasipim kachkani. Wasinman chayasqanmanta mamanta willarqa.
shp
Jara neskata iki: tita, xobonkoriki ea.
Jawen tita yoiaia iki moa xobon nokota.
tar
A’lí je aníli échiko: ku bitichí ne atíki Nana
Iyéla ku ruyéli, mapu bitichí ku nawáli.
Table 2: A parallel example in AmericasNLI with the entailment label.
Bribri has only been a written language for about
40 years, existing materials have a large degree of
idiosyncratic variation. These variations are stan-
dardized in AmericasNLI, which is written in the
Amubri variant.
Guaraní
Guaraní is spoken by between 6 to 10
million people in South America and roughly 3 mil-
lion people use it as their main language, including
more than 10 native nations in Paraguay, Brazil,
Argentina, and Bolivia, along with Paraguayan, Ar-
gentinian, and Brazilian peoples. According to
the Paraguayan Census, in 2002 there were around
1.35 million monolingual speakers, which has since
increased to around 1.5 million people (Dos Santos,
2017; Melià, 1992).4 Although the use of Guaraní
as spoken language is much older, the ﬁrst writ-
ten record dates to 1591 (Catechism) followed by
the ﬁrst dictionary in 1639 and linguistic descrip-
tions in 1640. The ofﬁcial grammar of Guaraní
was approved in 2018. Guaraní is an agglutinative
language, with ample use of preﬁxes and sufﬁxes.
Nahuatl
Nahuatl belongs to the Nahuan subdivi-
sion of the Uto-Aztecan language family. There are
30 recognized variants of Nahuatl spoken by over
1.5 million speakers across Mexico, where Nahu-
atl is recognized as an ofﬁcial language (SEGOB,
2020b). Nahuatl is polysynthetic and agglutina-
tive, and many sentences have an SVO word order
or, for contrast and focus, a VSO order, and for
emphasis, an SOV order (MacSwan, 1998). The
4https://www.ine.gov.py/news/
25-de-agosto-dia-del-Idioma-Guarani.php
translations in AmericasNLI belong to the Central
Nahuatl (Náhuatl de la Huasteca) dialect. As there
is a lack of consensus regarding the orthographic
standard, the orthography is normalized to a ver-
sion similar to Classical Nahuatl.
Otomí
Otomí belongs to the Oto-Pamean lan-
guage family and has nine linguistic variants with
different regional self-denominations. Otomí is a
tonal language following an SVO order, and there
are around 307,928 speakers spread across 7 Mex-
ican states. In the state of Tlaxcala, the yuhmu or
ñuhmu variant is spoken by fewer than 100 speak-
ers, and we use this variant for the Otomí examples
in AmericasNLI.
Quechua
Quechua, or Runasimi, is an Indige-
nous language family spoken primarily in the Pe-
ruvian Andes. It is the most widely spoken pre-
Columbian language family of the Americas, with
around 8-10 million speakers.
Approximately
25% (7.7 million) of Peruvians speak a Quechuan
language, and it is the co-ofﬁcial language in
many regions of Peru. There are multiple subdi-
visions of Quechua , and AmericasNLI examples
are translated into the standard version of South-
ern Quechua, Quechua Chanka, also known as
Quechua Ayacucho, which is spoken in different
regions of Peru and can be understood in differ-
ent areas of other countries, such as Bolivia or
Argentina. In AmericasNLI, the apostrophe and
pentavocalism from other regions are not used.
Rarámuri
Rarámuri, also known as Tarahumara,
which means light foot (INALI, 2017), belongs

--- Page 5 ---

aym
bzd
cni
gn
hch
nah
oto
quy
shp
tar
ChrF
es→XX
0.19
0.08
0.10
0.22
0.13
0.18
0.06
0.33
0.14
0.05
XX→es
0.09
0.06
0.09
0.14
0.07
0.10
0.06
0.14
0.09
0.08
BLEU
es→XX
0.30
0.54
0.03
3.26
3.18
0.33
0.01
1.58
0.34
0.01
XX→es
0.04
0.01
0.01
0.18
0.01
0.02
0.02
0.05
0.01
0.01
Table 3: Translation performance for all target languages. es→XX represents translating into the target language,
which is used for translate-train, and XX→es represents translating into Spanish, used for translate-test.
to the Taracahitan subgroup of the Uto-Aztecan
language family (Goddard, 1996), and is polysyn-
thetic and agglutinative. Rarámuri is an ofﬁcial
language of Mexico, spoken mainly in the Sierra
Madre Occidental region by a total of 89,503
speakers (SEGOB, 2020c). AmericasNLI exam-
ples are translated into the Highlands variant (IN-
ALI, 2009), and translation orthography and word
boundaries are similar to Caballero (2008).
Shipibo-Konibo
Shipibo-Konibo is a Panoan
language spoken by around 35,000 native speakers
in the Amazon region of Peru. Shipibo-Konibo
uses an SOV word order (Faust, 1973) and post-
positions (Vasquez et al., 2018). The translations
in AmericasNLI make use of the ofﬁcial alphabet
and standard writing supported by the Ministry of
Education in Peru.
Wixarika
The Wixarika, or Huichol, language,
meaning the language of the doctors and heal-
ers (Lumholtz, 2011), is a language in the Cora-
chol subgroup of the Uto-Aztecan language fam-
ily (Campbell, 2000). Wixarika is a national lan-
guage of Mexico with four variants , spoken by a
total of around 47,625 speakers (SEGOB, 2020a).
Wixarika is a polysynthetic language and follows
an SOV word order. Translations in Americas-
NLI are in Northern Wixarika and use an orthogra-
phy common among native speakers (Mager-Hois,
2017).
4
Experiments
In this section, we detail the experimental setup
we use to evaluate the performance of various ap-
proaches on AmericasNLI.
4.1
Zero-Shot Learning
Pretrained Model
We use XLM-R (Conneau
et al., 2020) as the pretrained multilingual model
in our experiments. The architecture of XLM-R
is based on RoBERTa (Liu et al., 2019), and it is
trained using MLM on web-crawled data in 100
languages. It uses a shared vocabulary consisting
of 250k subwords, created using SentencePiece
(Kudo and Richardson, 2018) tokenization. We use
the Base version of XLM-R for our experiments.
Adaptation Methods
To adapt XLM-R to the
various target languages, we continue training with
the MLM objective on monolingual text in the tar-
get language before ﬁnetuning. To keep a fair com-
parison with other approaches, we only use target
data which was also used to train the translation
models, which we describe in Section 4.2. How-
ever, we note that one beneﬁt of continued pretrain-
ing for adaptation is that it does not require parallel
text, and could therefore beneﬁt from text which
could not be used for a translation-based approach.
For continued pretraining, we use a batch size of
32 and a learning rate of 2e-5. We train for a to-
tal of 40 epochs. Each adapted model starts from
the same version of XLM-R, and is adapted indi-
vidually to each target language, which leads to a
different model for each language. We denote mod-
els adapted with continued pretraining as +MLM.
Finetuning
To ﬁnetune XLM-R, we follow the
approach of Devlin et al. (2019) and use an ad-
ditional linear layer. We train on either the En-
glish MNLI data or the machine-translated Spanish
data, and we call the ﬁnal models XLM-R (en)
and XLM-R (es), respectively. Following Hu et al.
(2020), we use a batch size of 32 and a learning
rate of 2e-5. We train for a maximum of 5 epochs,
and evaluate performance every 2500 steps on the
XNLI development set. We employ early stopping
with a patience of 15 evaluation steps and use the
best performing checkpoint for the ﬁnal evalua-
tion. All ﬁnetuning is done using the Huggingface
Transformers library (Wolf et al., 2020) with up
to two Nvidia V100 GPUs. Using Lacoste et al.
(2019), we estimate total carbon emissions to be
75.6 kgCO2eq.

--- Page 6 ---

aym
bzd
cni
gn
hch
nah
oto
quy
shp
tar
Avg.
Majority baseline
33.33
33.33
33.33
33.33
33.33
33.47
33.42
33.33
33.33
33.33
-
Zero-shot
XLM-R (en)
36.13±0.88 39.65±0.89 37.91±0.82 39.47±1.14 37.20±1.32 42.59±0.34 37.79±0.78 37.24±1.78 40.45±0.89 36.36±1.07 38.48±1.05
XLM-R (es)
37.25±2.33 39.38±1.96 37.29±1.12 39.25±1.55 35.82±1.01 38.98±1.38 38.32±1.47 39.51±1.92 38.40±0.87 35.73±0.69 37.99±1.51
Zero-shot w/ adaptation
XLM-R +MLM (en)
43.51±1.69 38.13±1.75 39.47±1.19 52.44±0.93 37.25±2.60 46.21±0.72 37.03±3.28 61.78±2.42 41.34±0.61 39.82±0.95 43.70±1.83
XLM-R +MLM (es)
43.87±0.14 40.05±2.20 38.76±0.08 52.27±1.20 37.82±1.59 44.17±1.76 40.55±1.07 62.40±1.44 40.18±0.95 38.45±0.86 43.85±1.30
Translate-train
XLM-R
50.00±1.51 51.42±1.24 42.45±1.63 58.89±2.70 43.20±2.07 55.33±1.12 36.01±0.74 59.91±0.20 52.00±0.27 42.04±1.81 49.12±1.52
Translate-test
XLM-R
39.73±0.27 40.40±0.13 34.71±0.73 46.62±2.29 38.00±0.48 41.37±0.16 35.29±1.15 51.38±1.24 39.51±0.47 35.16±0.97 40.22±1.01
Table 4: Results for zero-shot, translate-train, and translate-test averaged over 3 runs with different seeds. The
majority baseline represents expected performance when predicting only the majority class of the test set. Random
guessing would result in an accuracy of 33.33%. Standard deviations in the Avg. column are calculated by taking
the square root of the average variance of the languages in that row.
4.2
Translation-based Approaches
We also experiment with two translation-based ap-
proaches, translate-train and translate-test, detailed
below along with the translation model used.
Translation Models
For our translation-based
approaches, we train two sets of translation mod-
els: one to translate from Spanish into the tar-
get language, and one in the opposite direction.
We use transformer sequence-to-sequence models
(Vaswani et al., 2017) with the hyperparameters
proposed by Guzmán et al. (2019). Parallel data
used to train the translation models can be found
in Table B.1. We employ the same model archi-
tecture for both translation directions, and we mea-
sure translation quality in terms of BLEU (Papineni
et al., 2002) and ChrF (Popovi´c, 2015), cf. Table 3.
We use fairseq (Ott et al., 2019) to implement all
translation models.5
Translate-train
For the translate-train approach,
the Spanish training data provided by XNLI is
translated into each target language. It is then used
to ﬁnetune XLM-R for each language individually.
Along with the training data, we also translate the
Spanish development data, which is used for vali-
dation and early stopping. We discuss the effects of
using a translated development set in Section F.1.
Notably, we ﬁnd that the ﬁnetuning hyperparame-
ters deﬁned above do not reliably allow the model
to converge for many of the target languages. To
5The code for translation models can be found at https:
//github.com/AmericasNLP/americasnlp2021
ﬁnd suitable hyperparameters, we tune the batch
size and learning rate by conducting a grid search
over {5e-6, 2e-5, 1e-4} for the learning rate and
{32, 64, 128} for the batch size. In order to select
hyperparameters which work well across all lan-
guages, we evaluate each run using the average per-
formance on the machine-translated Aymara and
Guaraní development sets, as these languages have
moderate and high ChrF scores, respectively. We
ﬁnd that decreasing the learning rate to 5e-6 and
keeping the batch size at 32 yields the best perfor-
mance. Other than the learning rate, we use the
same approach as for zero-shot ﬁnetuning.
Translate-test
For the translate-test approach,
we translate the test sets of each target language
into Spanish. This allows us to apply the model
ﬁnetuned on Spanish, XLM-R (es), to each test
set. Additionally, a beneﬁt of translate-test over
translate-train and the adapted XLM-R models is
that we only need to ﬁnetune once overall, as op-
posed to once per language. For evaluation, we use
the checkpoint with the highest performance on the
Spanish XNLI development set.
5
Results and Discussion
Zero-shot Models
We present our results in Ta-
ble 4. Results for the development set are presented
in Table E.1. Zero-shot performance is low for all
10 languages, with an average accuracy of 38.48%
and 37.99% for the English and Spanish model,
respectively. However, in all cases the performance
is higher than the majority baseline. As shown in

--- Page 7 ---

FT
aym
bzd
cni
gn
hch
nah
oto
quy
shp
tar
Avg.
Avg.+P
Majority baseline
-
33.33 33.33 33.33 33.33 33.33 33.47 33.42 33.33 33.33 33.33
-
-
Zero-shot
XLM-R (en)
62.34 33.60 33.47 32.40 33.47 34.13 33.06 32.35 33.33 33.60 34.27 33.37
38.48
XLM-R (es)
62.26 34.13 34.80 35.33 35.33 34.53 33.60 33.16 33.07 36.80 35.73 34.65
37.99
Zero-shot w/ adaptation
XLM-R +MLM (en)
-
37.07 32.80 33.07 42.40 33.73 34.55 33.96 44.40 35.33 34.80 36.21
43.70
XLM-R +MLM (es)
-
36.27 34.80 33.73 41.73 34.00 35.37 32.89 47.87 35.60 34.67 36.69
43.85
Translate-train
XLM-R
-
44.93 43.73 43.47 47.60 43.07 45.80 35.83 52.13 46.27 39.47 44.23
49.12
Translate-test
XLM-R
-
36.53 42.67 37.33 43.60 38.53 43.22 34.22 48.13 42.67 34.67 40.16
40.22
Table 5: Hypothesis-only results. The Avg. column represents the average of the hypothesis-only results, while
the Avg.+P column, taken from Table 4, represents the average of the languages when using both the premise and
hypothesis.
Table E.3 in the appendix, the same models achieve
an average of 74.20% and 75.35% accuracy respec-
tively, when evaluated on the 15 XNLI languages.
Interestingly, even though code-switching with
Spanish is encountered in many target languages,
ﬁnetuning on Spanish labeled data on average
slightly underperforms the model trained on En-
glish, however performance is better for 3 of the
languages. The English model achieves a highest
accuracy of 42.59%, when evaluated on Nahuatl,
while the Spanish model achieves a highest accu-
racy of 39.51%, when evaluated on Quechua. The
lowest performance is achieved when evaluating on
Aymara and Rarámuri, for the English and Spanish
model, respectively.
We ﬁnd that model adaptation via continued pre-
training improves both models, with an average
gain of 5.22 percentage points for English and 5.86
percentage points for Spanish. Notably, continued
pretraining increases performance for Quechua by
24.53 percentage points when ﬁnetuning on En-
glish, and 22.89 points when ﬁnetuning on Spanish.
Performance decreases for Bribri and Otomí when
ﬁnetuning on English, however performance for all
languages improves when using Spanish.
Translate-test
Performance of the translate-test
model improves over both zero-shot baselines. We
see the largest increase in performance for Guaraní
and Quechua, with gains of 7.16 and, respectively,
11.87 points over the best performing zero-shot
model without adaptation. Considering the trans-
lation metrics in Table 3, models for Guaraní and
Quechua achieve the two highest scores for both
metrics.
On average, translate-test does worse
when compared to the adapted zero-shot models,
and in all but two cases, both adapted models per-
form better than translate-test. We hypothesize that
translate-test is more sensitive to noise in the trans-
lated data; sentences may lose too much of their
original content, preventing correct classiﬁcation.
Translate-train
The most surprising result is
that of translate-train, which considerably outper-
forms the performance of translate-test for all lan-
guages, and outperforms the zero-shot models for
all but two languages. Compared to the best non-
adapted zero-shot model, the largest performance
gain is 20.40 points for Quechua. For the language
with the lowest performance, Otomí, translate-train
performs 2.32 points worse than zero-shot; how-
ever, it still outperforms translate-test. When av-
eraged across all languages, translate-train outper-
forms the English zero-shot model by 10.64 points,
and translate-test by 8.9 points. It is important to
note that the translation performance from Span-
ish to each target language is not particularly high:
when considering ChrF scores, the highest is 0.33,
and the highest BLEU score is 3.26. Performance
of both translation-based models is correlated with
ChrF scores, with a Pearson correlation coefﬁcient
of 0.82 and 0.83 for translate-train and translate-
test. Correlations are not as strong for BLEU, with
coefﬁcients of 0.37 and 0.59.
The sizable difference in performance between
translate-train and the other methods suggests that
translation-based approaches may be a valuable
asset for cross-lingual transfer, especially for low-

--- Page 8 ---

resource languages. While the largest downsides
to this approach are the requirement for parallel
data and the need for multiple models, the poten-
tial performance gain over other approaches may
prove worthwhile. Additionally, we believe that the
performance of both translation-based approaches
would improve given a stronger translation system,
and future work detailing the necessary level of
translation quality for the best performance would
offer great practical usefulness for NLP applica-
tions for low-resource languages.
6
Analysis
6.1
Hypothesis-only Models
As shown by Gururangan et al. (2018), SNLI and
MNLI – the datasets AmericasNLI is based on
– contain artifacts created during the annotation
process which models exploit to artiﬁcially inﬂate
performance. To analyze whether similar artifacts
exist in AmericasNLI and if they can also be ex-
ploited, we train and evaluate models using only
the hypothesis, and present results in Table 5. We
can see that the average performance across lan-
guages is better than chance for all models except
for XLM-R without adaptation. Translate-train
obtains the highest result with 44.23% accuracy,
and as shown in Table E.2, hypothesis-only per-
formance of translate-test is higher than standard
performance for 5 languages. Thus, as with SNLI
and MNLI, artifacts in the hypotheses can be used
to predict, to some extent, the correct labels. How-
ever all but 1 zero-shot and translate-train models
perform better in the standard setting, indicating
that the models are learning something beyond just
exploiting artifacts in the hypotheses, even with the
additional challenge of unseen languages.
6.2
Case Study: Human Evaluation
Following Conneau et al. (2018), AmericasNLI
was created by translating sentences individually,
in order to prevent additional context being added
into the hypotheses. However, this strategy may
break the original semantic relationship between
the premise and the hypothesis. Furthermore, for
some examples the logical relationship may be de-
pendent on context or subtext which can be lost
through translation, or simply not make sense in
the target language. To verify the validity of the
labels of AmericasNLI, we conduct a human evalu-
ation experiment, focusing on examples translated
to Bribri. We create a balanced, random sample
of 450 examples taken from the Bribri develop-
ment set. An annotator familiar with the task was
then asked to classify the pairs of sentences. For
comparison, we also annotate parallel examples
taken from the English and Spanish development
sets. For Bribri, we recover the original XNLI label
for 76.44% of examples. For English and Spanish,
we achieve 81.78% and 71.56% accuracy, respec-
tively. Due to the relatively small differences in
performance across languages, we conclude that
translation to Bribri has a minimal effect on the
semantic relationship between the premise and the
hypothesis.
7
Limitations and Future Work
While the case study above provides strong evi-
dence for the validity of our Bribri examples, we
cannot currently generalize this claim to the re-
maining languages. For future work, we plan on
extending our human evaluation to more languages
and provide a more detailed analysis.
Additionally, due to the limited availability of
annotators and the difﬁculties of translation for lan-
guages that are less frequently studied, the size of
the AmericasNLI test set is relatively small. As
such, care must be taken to carefully evaluate con-
clusions drawn using the dataset; following Card
et al. (2020) we present a power analysis of our
results in Section D.1. Future work expanding the
dataset size will help create a stronger baseline.
Furthermore, while we do not make any model-
speciﬁc assumptions in our experiments, our re-
sults are based on only one pretrained model and
adaptation method. Methods using vocabulary ex-
tension or adapters may offer additional improve-
ments. Similarly, other pretrained models could
perform differently, depending on, e.g., the model
size or the set of languages in their pretraining
data. In Table F.3, we present results using XLM-
R Large, and ﬁnd that, while the relationship be-
tween the approaches differs from the main experi-
ments, the overall highest average performance is
still achieved by the translate-train approach with
XLM-R Base. We provide a longer discussion in
Section F.3.
8
Conclusion
To better understand the zero-shot abilities of pre-
trained multilingual models for semantic tasks in
unseen languages, we present AmericasNLI, a par-
allel NLI dataset covering 10 low-resource lan-

--- Page 9 ---

guages indigenous to the Americas. We conduct
experiments with XLM-R, and ﬁnd that the model’s
zero-shot performance, while better than a majority
baseline, is poor. However, it can be improved by
model adaptation via continued pretraining. Addi-
tionally, we ﬁnd that translation-based approaches
outperform a zero-shot approach, which is surpris-
ing given the low quality of the employed trans-
lation systems. We hope that this work will not
only spur further research into improving model
adaptation to unseen languages, but also motivate
the creation of more resources for languages not
frequently studied by the NLP community.
Ethics Statement
In this work, we present a new dataset created
through the translation of an existing resource,
XNLI (Conneau et al., 2018). While this allows for
results that are directly comparable, it also means
that this dataset inherits any biases and ﬂaws which
are contained in the previous dataset. Furthermore,
research involving languages spoken by Indigenous
communities raises ethical concerns regarding the
exploitation of these languages and communities:
it is crucial that members of the community are
able to directly beneﬁt from the research. Trans-
lation for AmericasNLI was done by either paper
authors or translators who were compensated at a
rate based on the average rate for translation and
the minimum wage in their country of residence.
Additionally, many authors are members of, and/or
have a record of close work with communities who
speak a language contained in AmericasNLI.
Acknowledgments
We thank the following people for their work on
the translations: Francisco Morales for Bribri, Fe-
liciano Torres Ríos for Asháninka, Perla Alvarez
Britez for Guaraní, Silvino González de la Crúz
for Wixarika, Giovany Martínez Sebastián, Pedro
Kapoltitan, and José Antonio for Nahuatl, José Ma-
teo Lino Cajero Velázquez for Otomí, Liz Chávez
for Shipibo-Konibo, and María del Cármen Sotelo
Holguín for Rarámuri. We would also like to thank
Dallas Card for his help with power analysis. This
work would not have been possible without the
ﬁnancial support of Facebook AI Research, Mi-
crosoft Research, Google Research, the Institute
of Computational Linguistics at the University of
Zurich, the NAACL Emerging Regions Fund, Co-
munidad Elotl, and Snorkel AI.
References
Željko Agi´c and Ivan Vuli´c. 2019. JW300: A wide-
coverage parallel corpus for low-resource languages.
In Proceedings of the 57th Annual Meeting of the
Association for Computational Linguistics, pages
3204–3210, Florence, Italy. Association for Compu-
tational Linguistics.
Maytham Alabbas. 2013. A dataset for Arabic textual
entailment. In Proceedings of the Student Research
Workshop associated with RANLP 2013, pages 7–
13, Hissar, Bulgaria. INCOMA Ltd. Shoumen, BUL-
GARIA.
Hossein Amirkhani, Mohammad AzariJafari, Azadeh
Amirak,
Zohreh
Pourjafari,
Soroush
Faridan
Jahromi, and Zeinab Kouhkan. 2020.
Farstail: A
persian natural language inference dataset. ArXiv,
abs/2009.08820.
Waleed Ammar, George Mulcaire, Yulia Tsvetkov,
Guillaume Lample, Chris Dyer, and Noah A. Smith.
2016.
Massively multilingual word embeddings.
ArXiv, abs/1602.01925.
M. Artetxe and Holger Schwenk. 2019. Massively mul-
tilingual sentence embeddings for zero-shot cross-
lingual transfer and beyond. Transactions of the As-
sociation for Computational Linguistics, 7:597–610.
Piotr Bojanowski, Edouard Grave, Armand Joulin, and
Tomas Mikolov. 2017. Enriching word vectors with
subword information. Transactions of the Associa-
tion for Computational Linguistics, 5:135–146.
Johan Bos, Fabio Massimo Zanzotto, and M. Pennac-
chiotti. 2009. Textual entailment at evalita 2009.
Samuel R. Bowman, Gabor Angeli, Christopher Potts,
and Christopher D. Manning. 2015. A large anno-
tated corpus for learning natural language inference.
In Proceedings of the 2015 Conference on Empirical
Methods in Natural Language Processing (EMNLP).
Association for Computational Linguistics.
David Brambila. 1976. Diccionario raramuri - castel-
lano: Tarahumar.
Gabriela Caballero. 2008. Choguita rarámuri (tarahu-
mara) phonology and morphology.
M. Cajero. 1998. Raíces del Otomí: diccionario. Gob-
ierno del Estado de Tlaxcala.
Mateo Cajero. 2009.
Historia de los Otomíes en Ix-
tenco, volume 1. Instituto Tlaxcalteca de la Cultura,
Tlaxcala, México.
Lyle Campbell. 2000. American Indian languages: the
historical linguistics of Native America.
Oxford
University Press.
D. Card, Peter Henderson, Urvashi Khandelwal, Robin
Jia, Kyle Mahowald, and Dan Jurafsky. 2020. With
little power comes great responsibility. In EMNLP.

--- Page 10 ---

Ethan C. Chau, Lucy H. Lin, and Noah A. Smith. 2020.
Parsing with multilingual BERT, a small corpus, and
a small treebank.
In Findings of the Association
for Computational Linguistics: EMNLP 2020, pages
1324–1334, Online. Association for Computational
Linguistics.
Luis Chiruzzo, Pedro Amarilla, Adolfo Ríos, and Gus-
tavo Giménez Lugo. 2020.
Development of a
Guarani - Spanish parallel corpus. In Proceedings of
the 12th Language Resources and Evaluation Con-
ference, pages 2629–2633, Marseille, France. Euro-
pean Language Resources Association.
Alexis Conneau, Kartikay Khandelwal, Naman Goyal,
Vishrav Chaudhary, Guillaume Wenzek, Francisco
Guzmán, E. Grave, Myle Ott, Luke Zettlemoyer, and
Veselin Stoyanov. 2020. Unsupervised cross-lingual
representation learning at scale. In ACL.
Alexis Conneau, Ruty Rinott, Guillaume Lample, Ad-
ina Williams, Samuel R. Bowman, Holger Schwenk,
and Veselin Stoyanov. 2018. Xnli: Evaluating cross-
lingual sentence representations. In Proceedings of
the 2018 Conference on Empirical Methods in Natu-
ral Language Processing. Association for Computa-
tional Linguistics.
Adolfo Constenla, Feliciano Elizondo, and Francisco
Pereira. 2004. Curso Básico de Bribri. Editorial de
la Universidad de Costa Rica.
Rubén Cushimariano Romano and Richer C. Se-
bastián Q. 2008.
Ñaantsipeta asháninkaki bi-
rakochaki. diccionario asháninka-castellano. versión
preliminar.
http://www.lengamer.org/
publicaciones/diccionarios/.
Visitado:
01/03/2013.
Jacob Devlin, Ming-Wei Chang, Kenton Lee, and
Kristina Toutanova. 2019.
BERT: Pre-training of
deep bidirectional transformers for language under-
standing.
In Proceedings of the 2019 Conference
of the North American Chapter of the Association
for Computational Linguistics: Human Language
Technologies, Volume 1 (Long and Short Papers),
pages 4171–4186, Minneapolis, Minnesota. Associ-
ation for Computational Linguistics.
Rafaela Alves Dos Santos. 2017.
DIGLOSSIA
NO PARAGUAI: A restrição dos monolíngues em
guarani no acesso à informação.
Trabalho de
Conclusão de Curso, Bacharelado em Línguas Es-
trangeiras. Universidade de Brasília, Brasilia.
Kathrin Eichler, Aleksandra Gabryszak, and Günter
Neumann. 2014. An analysis of textual inference
in German customer emails.
In Proceedings of
the Third Joint Conference on Lexical and Com-
putational Semantics (*SEM 2014), pages 69–74,
Dublin, Ireland. Association for Computational Lin-
guistics and Dublin City University.
Norma Faust. 1973. Lecciones para el aprendizaje del
idioma shipibo-conibo, volume 1 of Documento de
Trabajo.
Instituto Lingüístico de Verano, Yarina-
cocha.
Isaac Feldman and Rolando Coto-Solano. 2020. Neu-
ral machine translation models with back-translation
for the extremely low-resource indigenous language
Bribri.
In Proceedings of the 28th International
Conference on Computational Linguistics, pages
3965–3976, Barcelona, Spain (Online). Interna-
tional Committee on Computational Linguistics.
Sofía Flores Solórzano. 2017. Corpus oral pandialectal
de la lengua bribri. http://bribri.net.
Ana-Paula Galarreta, Andrés Melgar, and Arturo On-
cevay. 2017. Corpus creation and initial SMT ex-
periments between Spanish and Shipibo-konibo. In
Proceedings of the International Conference Recent
Advances in Natural Language Processing, RANLP
2017, pages 238–244, Varna, Bulgaria. INCOMA
Ltd.
Ives Goddard. 1996.
Introduccion.
In William C.
Sturtevant, editor, Handbook of North American In-
dians (vol. 17), chapter 1, pages 1–6. University of
Texas.
Héctor Erasmo Gómez Montoya, Kervy Dante Rivas
Rojas, and Arturo Oncevay. 2019.
A continuous
improvement framework of machine translation for
Shipibo-konibo.
In Proceedings of the 2nd Work-
shop on Technologies for MT of Low Resource Lan-
guages, pages 17–23, Dublin, Ireland. European As-
sociation for Machine Translation.
Edouard Grave, Piotr Bojanowski, Prakhar Gupta, Ar-
mand Joulin, and Tomas Mikolov. 2018. Learning
word vectors for 157 languages.
In Proceedings
of the International Conference on Language Re-
sources and Evaluation (LREC 2018).
Joseph Harold Greenberg. 1963.
Universals of lan-
guage.
Suchin Gururangan,
Swabha Swayamdipta,
Omer
Levy, Roy Schwartz, Samuel Bowman, and Noah A.
Smith. 2018.
Annotation artifacts in natural lan-
guage inference data. In Proceedings of the 2018
Conference of the North American Chapter of the
Association for Computational Linguistics: Human
Language Technologies, Volume 2 (Short Papers),
pages 107–112, New Orleans, Louisiana. Associa-
tion for Computational Linguistics.
Ximena
Gutierrez-Vasques,
Gerardo
Sierra,
and
Isaac Hernandez Pompa. 2016.
Axolotl: a web
accessible parallel corpus for Spanish-Nahuatl. In
Proceedings of the Tenth International Conference
on Language Resources and Evaluation (LREC’16),
pages 4210–4214, Portorož, Slovenia. European
Language Resources Association (ELRA).
Francisco Guzmán, Peng-Jen Chen, Myle Ott, Juan
Pino, Guillaume Lample, Philipp Koehn, Vishrav
Chaudhary, and Marc’Aurelio Ranzato. 2019. The
ﬂores evaluation datasets for low-resource machine

--- Page 11 ---

translation: Nepali–english and sinhala–english. In
Proceedings of the 2019 Conference on Empirical
Methods in Natural Language Processing and the
9th International Joint Conference on Natural Lan-
guage Processing (EMNLP-IJCNLP), pages 6100–
6113.
Petr Homola. 2012. Building a formal grammar for a
polysynthetic language. In Formal Grammar, pages
228–242, Berlin, Heidelberg. Springer Berlin Hei-
delberg.
Junjie Hu, Sebastian Ruder, Aditya Siddhant, Gra-
ham Neubig, Orhan Firat, and Melvin Johnson.
2020. Xtreme: A massively multilingual multi-task
benchmark for evaluating cross-lingual generaliza-
tion. CoRR, abs/2003.11080.
INALI. 2009. Catálogo de las lenguas indígenas na-
cionales: Variantes lingüísticas de méxico con sus
autodenominaciones y referencias geoestadísticas.
INALI.
INALI. 2014.
Norma de escritura de la Lengua
Hñähñu (Otomí), 1st edition. Secretaria de culatura.
INALI. 2017. Etnografía del pueblo tarahumara (rará-
muri).
INEC. 2011. Población total en territorios indígenas
por autoidentiﬁcación a la etnia indígena y habla de
alguna lengua indígena, según pueblo y territorio in-
dígena. In Instituto Nacional de Estadística y Cen-
sos, editor, Censo 2011.
INEGI. 2008. Catálogo de las lenguas indígenas na-
cionales: Variantes lingüísticas de méxico con sus
autodenominaciones y referencias geoestadísticas.
Diario Oﬁcial, pages 31–108.
José L. Iturrioz and Paula Gómez-López. 2008. Gra-
matica wixarika i.
Carla Victoria Jara Murillo. 2018a. Gramática de la
Lengua Bribri. EDigital.
Carla Victoria Jara Murillo. 2018b.
I Ttè Historias
Bribris, second edition. Editorial de la Universidad
de Costa Rica.
Carla Victoria Jara Murillo and Alí García Segura.
2013. Se’ ttö’ bribri ie Hablemos en bribri. EDigi-
tal.
Katharina Kann, Kyunghyun Cho, and Samuel R. Bow-
man. 2019.
Towards realistic practices in low-
resource natural language processing: The develop-
ment set. In Proceedings of the 2019 Conference on
Empirical Methods in Natural Language Processing
and the 9th International Joint Conference on Natu-
ral Language Processing (EMNLP-IJCNLP), pages
3342–3349, Hong Kong, China. Association for
Computational Linguistics.
Taku Kudo and John Richardson. 2018. SentencePiece:
A simple and language independent subword tok-
enizer and detokenizer for neural text processing. In
Proceedings of the 2018 Conference on Empirical
Methods in Natural Language Processing: System
Demonstrations, pages 66–71, Brussels, Belgium.
Association for Computational Linguistics.
Alexandre
Lacoste,
Alexandra
Luccioni,
Victor
Schmidt, and Thomas Dandres. 2019. Quantifying
the carbon emissions of machine learning.
arXiv
preprint arXiv:1910.09700.
Guillaume Lample and Alexis Conneau. 2019. Cross-
lingual language model pretraining. In NeurIPS.
Guillaume Lample, Alexis Conneau, Ludovic Denoyer,
and Marc’Aurelio Ranzato. 2018a.
Unsupervised
machine translation using monolingual corpora only.
In International Conference on Learning Represen-
tations (ICLR).
Guillaume Lample, Alexis Conneau, Marc’Aurelio
Ranzato, Ludovic Denoyer, and Hervé Jégou. 2018b.
Word translation without parallel data. In 6th Inter-
national Conference on Learning Representations,
ICLR 2018, Vancouver, BC, Canada, April 30 - May
3, 2018, Conference Track Proceedings. OpenRe-
view.net.
Anne Lauscher, Vinit Ravishankar, Ivan Vuli´c, and
Goran Glavaš. 2020. From zero to hero: On the lim-
itations of zero-shot language transfer with multilin-
gual Transformers. pages 4483–4499.
Yaobo Liang, Nan Duan, Yeyun Gong, Ning Wu, Fen-
fei Guo, Weizhen Qi, Ming Gong, Linjun Shou,
Daxin Jiang, Guihong Cao, Xiaodong Fan, Ruofei
Zhang, Rahul Agrawal, Edward Cui, Sining Wei,
Taroon Bharti, Ying Qiao, Jiun-Hung Chen, Winnie
Wu, Shuguang Liu, Fan Yang, Daniel Campos, Ran-
gan Majumder, and Ming Zhou. 2020. XGLUE: A
new benchmark datasetfor cross-lingual pre-training,
understanding and generation. In Proceedings of the
2020 Conference on Empirical Methods in Natural
Language Processing (EMNLP), pages 6008–6018,
Online. Association for Computational Linguistics.
Y. Liu, Myle Ott, Naman Goyal, Jingfei Du, Mandar
Joshi, Danqi Chen, Omer Levy, M. Lewis, Luke
Zettlemoyer, and Veselin Stoyanov. 2019. Roberta:
A robustly optimized bert pretraining approach.
ArXiv, abs/1907.11692.
James Loriot, Erwin Lauriout, and Dwight Day. 1993.
Diccionario Shipibo-Castellano. Instituto Lingüís-
tico de Verano.
Carl Lumholtz. 2011.
Unknown Mexico: A Record
of Five Years’ Exploration Among the Tribes of the
Western Sierra Madre, volume 2. Cambridge Uni-
versity Press.
Jeff MacSwan. 1998. The argument status of nps in
southeast puebla nahuatl: Comments on the polysyn-
thesis parameter. Southwest Journal of Linguistics,
17(2):101–114.

--- Page 12 ---

Manuel Mager, Dionico Gonzalez, and Ivan Meza.
2017.
Probabilistic ﬁnite-state morphological seg-
menter for wixarika (huichol).
Manuel Mager, Ximena Gutierrez-Vasques, Gerardo
Sierra, and Ivan Meza-Ruiz. 2018. Challenges of
language technologies for the indigenous languages
of the Americas. In Proceedings of the 27th Inter-
national Conference on Computational Linguistics,
pages 55–69, Santa Fe, New Mexico, USA. Associ-
ation for Computational Linguistics.
Jesus
Manuel
Mager-Hois.
2017.
Traductor
hıbrido wixárika-espanol con escasos recursos
bilingües. Ph.D. thesis, Master’s thesis, Universidad
Autónoma Metropolitana.
Enrique Margery. 2005.
Diccionario Fraseológico
Bribri-Español Español-Bribri, second edition. Edi-
torial de la Universidad de Costa Rica.
Bartomeu Melià. 1992.
La lengua Guaraní del
Paraguay: Historia, sociedad y literatura. Editorial
MAPFRE, Madrid.
Elena Mihas. 2017. The kampa subgroup of the arawak
language family. The Cambridge Handbook of Lin-
guistic Typology, page 782–814.
Tomas Mikolov, Ilya Sutskever, Kai Chen, Greg S Cor-
rado, and Jeff Dean. 2013. Distributed representa-
tions of words and phrases and their compositional-
ity. In Advances in Neural Information Processing
Systems, volume 26, pages 3111–3119. Curran As-
sociates, Inc.
Christopher Moseley. 2010. Atlas of the World’s Lan-
guages in Danger. Unesco.
B. Muller, Antonis Anastasopoulos, Benoît Sagot, and
Djamé Seddah. 2020.
When being unseen from
mbert is just the beginning:
Handling new lan-
guages with multilingual language models. ArXiv,
abs/2010.12858.
Johanna Nichols. 1986. Head-marking and dependent-
marking grammar. Language, 62(1):56–119.
Myle Ott, Sergey Edunov, Alexei Baevski, Angela
Fan, Sam Gross, Nathan Ng, David Grangier, and
Michael Auli. 2019.
fairseq: A fast, extensible
toolkit for sequence modeling.
In Proceedings of
NAACL-HLT 2019: Demonstrations.
Kishore Papineni, Salim Roukos, Todd Ward, and Wei-
Jing Zhu. 2002. Bleu: a method for automatic eval-
uation of machine translation.
In Proceedings of
the 40th Annual Meeting of the Association for Com-
putational Linguistics, pages 311–318, Philadelphia,
Pennsylvania, USA. Association for Computational
Linguistics.
Jeffrey Pennington, Richard Socher, and Christopher
Manning. 2014.
GloVe: Global vectors for word
representation. In Proceedings of the 2014 Confer-
ence on Empirical Methods in Natural Language
Processing (EMNLP), pages 1532–1543,
Doha,
Qatar. Association for Computational Linguistics.
Jonas Pfeiffer, Ivan Vuli´c, Iryna Gurevych, and Se-
bastian Ruder. 2020a. MAD-X: An Adapter-Based
Framework for Multi-Task Cross-Lingual Transfer.
In Proceedings of the 2020 Conference on Empirical
Methods in Natural Language Processing (EMNLP),
pages 7654–7673, Online. Association for Computa-
tional Linguistics.
Jonas Pfeiffer, Ivan Vuli´c, Iryna Gurevych, and Sebas-
tian Ruder. 2020b. Unks everywhere: Adapting mul-
tilingual language models to new scripts.
Telmo Pires, Eva Schlinger, and Dan Garrette. 2019.
How multilingual is multilingual BERT?
In Pro-
ceedings of the 57th Annual Meeting of the Asso-
ciation for Computational Linguistics, pages 4996–
5001, Florence, Italy. Association for Computa-
tional Linguistics.
Maja Popovi´c. 2015. chrF: character n-gram F-score
for automatic MT evaluation. In Proceedings of the
Tenth Workshop on Statistical Machine Translation,
pages 392–395, Lisbon, Portugal. Association for
Computational Linguistics.
Carlos Sánchez Avendaño. 2013. Lenguas en peligro
en Costa Rica: vitalidad, documentación y descrip-
ción. Revista Káñina, 37(1):219–250.
SEGOB. 2020a.
Sistema de Información Cultural -
Lenguas indígenas: Huichol
.
https://sic.gob.mx/ficha.php?
table=inali_li.
SEGOB.
2020b.
Sistema
de
Información
Cultural
-
Lenguas
indígenas:
Nnahuatl.
https://sic.gob.mx/ficha.php?
table=inali_li&amp;table_id=5.
SEGOB. 2020c.
Sistema de Información Cul-
tural
-
Lenguas
indígenas:
Tarahumara.
http://sic.gob.mx/ficha.php?table=
inali_li&amp;table_id=15.
Rico Sennrich, Barry Haddow, and Alexandra Birch.
2016.
Neural machine translation of rare words
with subword units. In Proceedings of the 54th An-
nual Meeting of the Association for Computational
Linguistics (Volume 1: Long Papers), pages 1715–
1725, Berlin, Germany. Association for Computa-
tional Linguistics.
Rémi Siméon. 1977. Diccionario de la lengua náhuatl
o mexicana, volume 1. Siglo XXI.
Thelma D Sullivan and Miguel León-Portilla. 1976.
Compendio de la gramática náhuatl, volume 18.
Universidad nacional autónoma de México, Instituto
de investigaciones históricas.
Jörg Tiedemann. 2012. Parallel data, tools and inter-
faces in OPUS.
In Proceedings of the Eighth In-
ternational Conference on Language Resources and

--- Page 13 ---

Evaluation (LREC’12), pages 2214–2218, Istanbul,
Turkey. European Language Resources Association
(ELRA).
Pilar Valenzuela. 2003. Transitivity in Shipibo-Konibo
grammar. Ph.D. thesis, University of Oregon.
Alonso Vasquez, Renzo Ego Aguirre, Candy An-
gulo, John Miller, Claudia Villanueva, Željko Agi´c,
Roberto Zariquiey, and Arturo Oncevay. 2018. To-
ward Universal Dependencies for Shipibo-konibo.
In Proceedings of the Second Workshop on Uni-
versal Dependencies (UDW 2018), pages 151–161,
Brussels, Belgium. Association for Computational
Linguistics.
Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob
Uszkoreit, Llion Jones, Aidan N Gomez, Ł ukasz
Kaiser, and Illia Polosukhin. 2017. Attention is all
you need. In Advances in Neural Information Pro-
cessing Systems, volume 30. Curran Associates, Inc.
Alex Wang,
Yada Pruksachatkun,
Nikita Nangia,
Amanpreet Singh, Julian Michael, Felix Hill, Omer
Levy, and Samuel Bowman. 2019.
Superglue: A
stickier benchmark for general-purpose language un-
derstanding systems. In Advances in Neural Infor-
mation Processing Systems, volume 32. Curran As-
sociates, Inc.
Alex Wang, Amanpreet Singh, Julian Michael, Fe-
lix Hill, Omer Levy, and Samuel Bowman. 2018.
GLUE: A multi-task benchmark and analysis plat-
form for natural language understanding.
In Pro-
ceedings of the 2018 EMNLP Workshop Black-
boxNLP: Analyzing and Interpreting Neural Net-
works for NLP, pages 353–355, Brussels, Belgium.
Association for Computational Linguistics.
Zihan Wang, Karthikeyan K, Stephen Mayhew, and
Dan Roth. 2020. Extending multilingual BERT to
low-resource languages. In Findings of the Associ-
ation for Computational Linguistics: EMNLP 2020,
pages 2649–2656, Online. Association for Computa-
tional Linguistics.
Adina Williams, Nikita Nangia, and Samuel Bowman.
2018. A broad-coverage challenge corpus for sen-
tence understanding through inference. In Proceed-
ings of the 2018 Conference of the North American
Chapter of the Association for Computational Lin-
guistics: Human Language Technologies, Volume
1 (Long Papers), pages 1112–1122. Association for
Computational Linguistics.
Thomas Wolf, Lysandre Debut, Victor Sanh, Julien
Chaumond, Clement Delangue, Anthony Moi, Pier-
ric Cistac, Tim Rault, Rémi Louf, Morgan Funtow-
icz, Joe Davison, Sam Shleifer, Patrick von Platen,
Clara Ma, Yacine Jernite, Julien Plu, Canwen Xu,
Teven Le Scao, Sylvain Gugger, Mariama Drame,
Quentin Lhoest, and Alexander M. Rush. 2020.
Transformers: State-of-the-art natural language pro-
cessing. In Proceedings of the 2020 Conference on
Empirical Methods in Natural Language Processing:
System Demonstrations, pages 38–45, Online. Asso-
ciation for Computational Linguistics.
Shijie Wu and Mark Dredze. 2019. Beto, bentz, be-
cas: The surprising cross-lingual effectiveness of
BERT. In Proceedings of the 2019 Conference on
Empirical Methods in Natural Language Processing
and the 9th International Joint Conference on Natu-
ral Language Processing (EMNLP-IJCNLP), pages
833–844, Hong Kong, China. Association for Com-
putational Linguistics.
Shijie Wu and Mark Dredze. 2020. Are all languages
created equal in multilingual BERT? In Proceedings
of the 5th Workshop on Representation Learning for
NLP, pages 120–130, Online. Association for Com-
putational Linguistics.

--- Page 14 ---

A
Geographic Distribution of the
AmericasNLI Languages
Bribri
Guaraní
Wixarika
Náhuatl
Rarámuri
Otomí
Figure A.1: Maps of Central and South America presenting an approximate distribution of where each Indigenous
language contained in AmericasNLI is spoken. Please note that this map is hand-drawn and largely an estimate:
some regions may not be included, and borders of included regions may not be completely accurate.
B
Sources of Parallel Data
Lang.
Source(s)
Sent.
aym Tiedemann (2012)
6,531
bzd
Feldman and Coto-Solano (2020); Margery (2005);
7,508
Jara Murillo (2018a); Constenla et al. (2004);
Jara Murillo and García Segura (2013);
Jara Murillo (2018b); Flores Solórzano (2017)
cni
Cushimariano Romano and Sebastián Q. (2008)
3,883
gn
Chiruzzo et al. (2020)
26,032
hch Mager et al. (2017)
8,966
nah Gutierrez-Vasques et al. (2016)
16,145
oto
https://tsunkua.elotl.mx
4,889
quy Agi´c and Vuli´c (2019)
125,008
shp Galarreta et al. (2017); Loriot et al. (1993);
14,592
Gómez Montoya et al. (2019)
tar
Brambila (1976);
14,720
github.com/pywirrarika/tar_par
Table B.1: Parallel data used for our translation models.

--- Page 15 ---

C
Additional Information for
AmericasNLI Languages
C.1
Aymara
A rare linguistic phenomenon found in Aymara is
vowel elision, a deletion of certain vowel sounds
triggered by complex phonological, morphological,
and syntactic factors.
C.2
Asháninka
While Asháninka in a strict sense refers to the lin-
guistic varieties spoken in Ene, Tambo and Bajo
Perené rivers, the name is also used to talk about
the following nearby and closely-related Asheninka
varieties: Alto Perené, Pichis, Pajonal, Ucayali-
Yurua, and Apurucayali. Although Asháninka is
the most widely spoken Amazonian language in
Peru, certain varieties, such as Alto Perené, are
highly endangered.
The verb is the most morphologically complex
word class, with a rich repertoire of aspectual and
modal categories. The language lacks case, except
for one locative sufﬁx, so the grammatical rela-
tions of subject and object are indexed as afﬁxes
on the verb itself. Other notable linguistic features
of the language include obligatory marking of a
realis/irrealis distinction on the verb, a rich system
of applicative sufﬁxes, serial verb constructions,
and a pragmatically conditioned split intransitivity.
C.3
Bribri
As previously noted, Bribri is a vulnerable lan-
guage, and there are few settings where the lan-
guage is written or used in ofﬁcial functions. The
language does not have ofﬁcial status and it is not
the main medium of instruction of Bribri children,
but it is offered as a class in primary and secondary
schools. Bribri features fusional morphology and
an ergative-absolutive case system. Bribri grammar
also includes phenomena like head-internal relative
clauses, directional verbs and numerical classiﬁers
(Jara Murillo, 2018a).
C.4
Guaraní
While the ﬁrst written record dates to 1591,
Guaraní usage in text continued until the Paraguay-
Triple Alliance War (1864-1870) and declined
thereafter. From the 1920s on, Guaraní has slowly
re-emerged and received renewed focus. In 1992,
Guaraní was the ﬁrst American language declared
an ofﬁcial language of a country, followed by a
surge of local, national, and international recogni-
tion in the early 21st century.6
C.5
Nahuatl
Nahuatl is spoken in 17 different states of Mexico.
In Nahuatl, different roots with or without afﬁxes
are combined to form new words. The sufﬁxes that
are added to a word modify the meaning of the orig-
inal word (Sullivan and León-Portilla, 1976), and
18 prepositions stand out based on postpositions of
names and adjectives (Siméon, 1977).
C.6
Otomí
The various regional self-denominations of Otomí
include ñähñu or ñähño, hñähñu, ñuju, ñoju, yühu,
hnähño, ñühú, ñanhú, ñöthó, ñható and hñothó
(INALI, 2014). Many words are homophonous
to Spanish (Cajero, 1998, 2009). When speaking
ñuhmu, pronunciation is elongated, especially on
the last syllable. The alphabet is composed of 19
consonants, 12 vowel phonemes.
C.7
Rarámuri
Rarámuri is mainly spoken in the state of Chi-
huahua. There are ﬁve variants of Rarámuri.
C.8
Shipibo-Konibo
Shipibo-Konibo is a language with agglutinative
processes, a majority of which are sufﬁxes. How-
ever, clitics are also used, and are a widespread
element in Panoan literature (Valenzuela, 2003).
C.9
Wixarika
The four variants of Wixarika are the Northern,
Southern, Eastern, and Western variants (INEGI,
2008). It is spoken mainly in the three Mexican
states of Jalisco, Nayari, and Durango. Features
of Wixarika include head-marking (Nichols, 1986),
a head-ﬁnal structure (Greenberg, 1963), nominal
incorporation, argumentative marks, inﬂected adpo-
sitions, possession marks, as well as instrumental
and directional afﬁxes (Iturrioz and Gómez-López,
2008).
6https://es.wikipedia.org/wiki/Idioma_
guarani

--- Page 16 ---

C.10
Summary of Language Information
Language
Language Family
Countries Spoken
Number of Speakers
Word Order
aym
Aymaran
Bolivia, Chile, Peru
2m
SOV
bzd
Chibchan
Costa Rica
7k
SOV
cni
Arawak
Peru
73k
VSO
gn
Tupi-Guarani
Paraguay, Brazil, Argentina, Bolivia
6-10m
SVO
hch
Uto-Aztecan
Mexico
47k
SOV
nah
Uto-Aztecan
Mexico
1.5m
SVO/VSO/SOV
oto
Oto-Manguean
Mexico
307k
SVO
quy
Quechuan
Peru
8-10m
SOV
shp
Panoan
Peru
35k
SOV
tar
Uto-Aztecan
Mexico
89k
SOV
Table C.1: Summary of the 10 languages in AmericasNLI.
D
Dataset Information
D.1
Power Analysis
p1 Model
p1
p2
Lower Bound Power
Upper Bound Power
p2 Model
Random Baseline
33.33
38.48
40.33
100
Zero-shot (en)
37.99
35.80
100
Zero-shot (es)
43.70
91.38
100
Zero-shot +MLM (en)
43.85
91.52
100
Zero-shot +MLM (es)
49.12
99.82
100
Translate-train
40.22
61.85
100
Translate-test
Zero-shot Baseline
38.48
43.70
33.66
100
Zero-shot +MLM (en)
43.85
35.33
100
Zero-shot +MLM (es)
49.12
87.10
100
Translate-train
40.22
7.13
99.07
Translate-test
Adaptation Baseline
43.85
49.12
31.29
100
Translate-train
Table D.1: Here, we use the simulation approach of Card et al. (2020) to calculate upper and lower bounds for
the power of our experiments. We use the average accuracies for each approach, and set n = 750, α = 0.05, r =
10, 000, and bold experiments with well-powered lower bounds.

--- Page 17 ---

D.2
Dataset Statistics
Language
Split
Entailment
Contradiction
Neutral
Majority Baseline
aym
Test
250
250
250
0.333
Dev
248
248
247
0.334
bzd
Test
250
250
250
0.333
Dev
248
248
247
0.334
cni
Test
250
250
250
0.333
Dev
220
220
218
0.334
gn
Test
250
250
250
0.333
Dev
248
248
247
0.334
hch
Test
250
250
250
0.333
Dev
248
248
247
0.334
nah
Test
246
245
247
0.335
Dev
193
195
197
0.337
oto
Test
249
249
250
0.334
Dev
78
75
69
0.351
quy
Test
250
250
250
0.333
Dev
248
248
247
0.334
shp
Test
250
250
250
0.333
Dev
248
248
247
0.334
tar
Test
250
250
250
0.333
Dev
248
248
247
0.334
Table D.2: Distribution of labels in the test and development sets, per language.
E
Detailed Results
FT
aym
bzd
cni
gn
hch
nah
oto
quy
shp
tar
Avg.
Majority baseline
-
33.40
33.40
33.40
33.40
33.40
33.70
35.10
33.40
33.40
33.40
-
Zero-shot
XLM-R (en)
84.55
38.45
41.59
40.07
40.74
37.82
39.50
43.84
38.67
43.56
36.03
40.03
XLM-R (es)
80.77
37.73
39.70
37.59
40.06
36.74
37.88
39.94
38.54
38.18
35.89
38.23
Zero-shot w/ adaptation
XLM-R +MLM (en)
-
41.77
39.57
40.93
52.40
41.01
43.25
37.24
62.27
44.86
39.30
44.26
XLM-R +MLM (es)
-
45.26
42.22
40.53
53.52
38.40
42.41
40.24
55.00
40.11
45.89
44.36
Translate-train
XLM-R
-
53.61
49.98
45.49
61.28
42.22
53.80
41.44
58.62
53.10
43.01
50.25
Translate-test
XLM-R
-
37.73
39.70
37.59
40.06
36.74
37.88
39.94
38.54
38.18
35.89
38.23
Table E.1: Development set results for zero-shot, translate-train, and translate-test. FT represents the XNLI de-
velopment set performance for the ﬁnetuning language and is not included in the average. The majority baseline
represents expected performance when predicting only the majority class of the development set. Random guessing
would result in an accuracy of 33.33%.

--- Page 18 ---

FT
aym
bzd
cni
gn
hch
nah
oto
quy
shp
tar
Avg.
Zero-shot
XLM-R (en)
-22.21
-2.53
-6.18
-5.51
-6.00
-3.07
-9.53
-5.44
-3.91
-6.85
-2.09
-5.11
XLM-R (es)
-18.51
-3.12
-4.58
-1.96
-3.92
-1.29
-5.38
-5.16
-6.44
-1.60
0.00
-3.35
Zero-shot w/ adaptation
XLM-R +MLM (en)
-
-6.44
-5.33
-6.40
-10.04
-3.52
-11.66
-3.07
-17.38
-6.01
-5.02
-7.49
XLM-R +MLM (es)
-
-7.60
-5.25
-5.03
-10.54
-3.82
-8.80
-7.66
-14.53
-4.58
-3.78
-7.16
Translate-train
XLM-R
-
-5.07
-7.69
1.02
-11.29
-0.13
-9.52
-0.18
-7.78
-5.73
-2.57
-4.89
Translate-test
XLM-R
-
-3.20
2.27
2.62
-3.02
0.53
1.85
-1.07
-3.25
3.16
-0.49
-0.06
Table E.2: Differences between hypothesis-only and standard results on the test set of AmericasNLI.
Source
ar
bg
de
el
en
es
fr
hi
ru
sw
th
tr
ur
vi
zh
Avg.
en
71.96 77.65 76.62 75.84 84.55 78.74 78.00 70.02 76.04 64.41 72.04 72.54 66.28 74.38 73.97 74.20
es
73.49 78.71 77.59 77.05 83.36 80.77 78.83 72.25 77.10 64.60 73.32 73.78 68.44 75.82 75.16 75.35
Table E.3: Results of zero-shot models on the test set of XNLI. Scores are underlined when the same language
used for training is used for evaluation as well.
F
Additional Results
Source
Model
aym
bzd
cni
gn
hch
nah
oto
quy
shp
tar
Avg.
en
Zero-Shot
36.00
39.20
37.20
40.67
36.80
42.28
36.90
35.73
40.67
36.27
38.17
Z-S +MLM
41.60
36.53
40.80
51.47
39.87
46.48
37.83
64.53
40.67
40.67
44.05
Z-S +MLMAUG
45.07
38.67
41.47
52.93
38.53
46.48
33.42
62.00
39.73
40.27
43.86
es
Zero-Shot
37.87
41.60
37.87
39.47
36.27
39.57
39.04
40.93
38.27
35.33
38.62
Z-S +MLM
43.87
37.60
38.80
52.27
36.00
45.12
41.58
60.80
41.20
38.80
43.60
Z-S +MLMAUG
45.20
38.67
39.33
54.27
37.07
44.99
42.65
62.67
37.20
38.67
44.07
−
Translate-Train
49.33
52.00
42.80
55.87
41.07
54.07
36.50
59.87
52.00
43.73
48.72
T-T +MLM
50.93
51.20
42.27
61.60
44.93
56.10
35.16
63.47
50.00
44.13
49.98
T-T +MLMAUG
51.07
51.87
44.53
61.07
46.27
53.39
35.96
61.07
52.67
40.67
49.86
Table F.1: Results from models adapted with augmented data before ﬁnetuning. Zero-shot, zero-shot +MLM, and
translate-train results are taken from the main experiments, however we only take results from the run correspond-
ing to the same random seed as the newly trained models.

--- Page 19 ---

F.1
Early Stopping
While early stopping is vital for machine learn-
ing, in the case of zero-shot learning hand-labeled
development sets in the target language are often as-
sumed to be unavailable (Kann et al., 2019). Thus,
in our main experiments we use either a machine-
translated development set or one from a high-
resource language. In both cases, performance on
the development set is an imperfect signal for how
the model will ultimately perform. To explore how
this affects ﬁnal performance, we present the dif-
ference in results for translate-train models when
an oracle translation is used for early stopping in
Table F.2. We ﬁnd that performance is 2.34 points
higher on average, with a maximum difference of
7.28 points for Asháninka, suggesting that creating
ways to better approximate a development set may
lead to higher performance.
aym bzd cni
gn hch nah oto quy shp tar Avg.
2.13 0.98 7.28 0.58 0.53 2.12 3.03 1.42 0.93 4.36 2.34
Table F.2: Difference between translate-train results ob-
tained using the oracle development set and the trans-
lated development set for early stopping.
F.2
Data Augmentation with Translated Data
Due to the success of translate-train, we also in-
vestigate if we can improve performance further
by creating data for language adaptation (+MLM)
through translation. To do so, we create a random
sample of sentences taken from Spanish Wikipedia,
and translate them into each target language. The
sample is sized to contain the same number of sub-
word tokens as the original pretraining data. We
combine the original pretraining data and trans-
lated data to create a new set of sentences for con-
tinued pretraining, doubling the size of the origi-
nal. We also ﬁnetune the original adapted models
using translate-train. We present results in Table
F.1. When ﬁnetuning on English and translate-train
data, the average performance is highest when us-
ing the models adapted on the original data. When
ﬁnetuning on Spanish, the models adapted on aug-
mented data are best on average. While on av-
erage performance increases are not drastic, for
some languages the performance increase is no-
table, and these mixed and/or augmented models
may be worth looking into when interested in a
particular language.
F.3
XLM-R Large
In this section we provide results for XLM-R Large.
Due to computational restrictions, we slightly mod-
ify the experimental setup from the main experi-
ments: we use mixed precision training and a more
aggressive early stopping patience of 3 evaluation
steps. Additionally, we use a learning rate of 5e-6
for all ﬁnetuning experiments, as we found that the
original learning rate of 2e-5 failed to converge.
However, even when using the modiﬁed hyperpa-
rameters, we experience some instability during
training. The zero-shot model trained on Spanish
data did not converge with the original random
seed, but successfully trained after changing the
seed. For translate-train, the models trained on
Asháninka and Otomí failed to converge, regard-
less of the seed used, and further hyperparameter
tuning will be required, which we leave for future
work.
In this experiment, we can see that the results
are more varied in comparison to the main results.
Translate-train achieves the highest performance
for ﬁve languages, with the adapted models achiev-
ing a combined highest performance for the remain-
ing ﬁve. On average, the adapted model ﬁnetuned
on English labeled data achieved the highest per-
formance, followed closely by the other adapted
model, and the translate-train model. This indi-
cates that translate-train may be a viable approach
when faced with limited compute, but might also
have a restrictive upper limit on performance; in
contrast, adaptation may allow for more potential
performance gain, especially when larger models
and datasets are available. Interestingly, when con-
sidering average performances across only the lan-
guages for which all models converged (i.e. remov-
ing Asháninka and Otomí from the calculation),
we ﬁnd that translate-train offers an average per-
formance of 51.91%, while adaptation approaches
achieve 49.39% and 49.83% accuracy on average.
Comparing XLM-R Large to XLM-R Base in
Table F.4, we see that for all but one language
the Large model outperforms the Base model in
all adaptation and zero-shot runs. Notably, the
Base model trained on translated data outperforms
the Large model, and retains the highest overall
performance across all languages and models.

--- Page 20 ---

FT
aym
bzd
cni
gn
hch
nah
oto
quy
shp
tar
Avg.
Zero-shot
XLM-R Large (en)
89.04 40.67 41.33 43.07 42.93 39.20 45.39 42.25 42.13 48.27 40.53 42.58
XLM-R Large (es)
89.84 38.67 41.60 41.20 42.00 37.20 41.46 42.38 41.33 43.47 36.00 40.53
Zero-shot w/ adaptation
XLM-R Large +MLM (en)
-
54.80 43.87 46.67 59.87 43.60 43.36 44.79 64.80 43.07 41.73 48.66
XLM-R Large +MLM (es)
-
54.93 40.40 42.93 61.07 44.67 45.53 42.51 68.00 43.60 40.40 48.40
Translate-train
XLM-R Large
-
51.47 50.13 33.33 61.20 42.00 55.28 33.42 61.47 49.87 43.87 48.20
Translate-test
XLM-R Large
-
38.67 40.93 35.73 50.80 38.93 39.97 32.62 47.87 39.33 35.60 40.05
Table F.3: Results when using XLM-R Large. Underlined results indicate runs which did not converge on the
training data.
FT
aym
bzd
cni
gn
hch
nah
oto
quy
shp
tar
Avg.
Zero-shot
English
4.49
4.54
1.68
5.16
3.46
2.00
2.80
4.46
4.89
7.82
4.17
4.10
Spanish
9.07
1.42
2.22
3.91
2.75
1.38
2.48
4.06
1.82
5.07
0.27
2.54
Zero-shot w/ adaptation
+MLM (en)
-
11.29
5.74
7.20
7.43
6.35
-2.85
7.76
3.02
1.73
1.91
4.96
+MLM (es)
-
11.06
0.35
4.17
8.80
6.85
1.36
1.96
5.60
3.42
1.95
4.55
Translate-train
-
1.47
-1.29 -9.12 2.31 -1.20 -0.05 -2.59
1.56
-2.13 1.83 -0.92
Translate-test
-
-1.06
0.53
1.02
4.18
0.93
-1.40 -2.67 -3.51 -0.18 0.44 -0.17
Table F.4: Difference in performance between XLM-R Large and Base.

--- Page 21 ---

Language
Example
aym
P: Mä jan walt ’ awinakax utjkaniti?
H: Iglesia JI JI ukax XIFlo XICI ukax XIIII ukan mä jach ’a pacha.
P: Aka qillqatax Crownwn Squareareareare ukax iwayi, ‘ Ñalacio ‘ ‘ ‘ ñoquis ukch ’ añataki.
H: Plaza de Plaza de palacio palacio palacio äwipat uñt ’ayi.
bzd
P: Ye’r ye’ alà alà dör ye’ alà tã’ alàshshshshshshöö ?
H: Káxkkk e’ tã káx batà batà ã káx batà ã .
P: Káx i’r i’ i’ ã káx i’ ulàshshshshshshshshshshshshshshshshsh .
H: Kéqéqwöwöwöwöwöwöwö ulà ulà ulà ulà wa .
cni
P:APAPAPAPAPAPAPAPAPAPAPAPAPAPAPAPAPAPAPAPAPAPAPAPAPAPAPAPAPAPAPAP
APAPAPAPAPAPAPAPAPAPAPA)))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))
))))))))))))))))))))))))))))))))))))))))))) O O O O O O O ObibibibibibibiIIIIIIIIIIIIIIIIIII
H: Ibibibibiti obibiti obibi. Ababababa
P: b. Akobiro ayiro ayiro ayiro nija Jebabentirori Anampiki.
H: Itititititititititititi.
gn
P: Peteî paseo corto imbarete caminata norte gotyo ha’e pueblo j? Sus , peteî tupão particularmente siglo XIX .
H: Tupão tavaguasu Jesús omopu’ã siglo XIX .
P: Péicha Crown Square oime palacio real , kuimba’e preciado tetãme , joy Escocia .
H: Plaza de la corona cuenta palacio real .
hch
P: xewit+ta m+k+ wa+ka xewit+ x+ka xewit+ x+ka mu’at+a.
H: ’aix+ ’aix+ ti’at+ x+t+ x+a mu’at+ x+a.
P: wa+ka m+k+ ’aix+ pureh+k+t+a de oro.
H: ’ik+ p+h+k+ palacio palacio palacio palacio.
nah
P: See tosaasaanil , see tosaasaanil , see tosaasaanil . See tosaasaanil , see tosaasaanil , see tosaasaanil .
H: Yn ipan ciudad de Jesús la Yglesia de Jesús yn ipan in omoteneuh xihuitl de Jesús .
P: Auh ynic patlahuac cenpohualmatl ypan in yn oncan tecpan quiyahuac yn oncan tecpan quiyahuac yn tecpan
quiyahuac yn oncan tecpan quiyahuac .
H: In tlapoalli ica tlapoalli ica tecpan palacio .
oto
P: Ra nge’a mi b’et¯’em¯ ’i ha ra thuhu ra thuhu ra thuhu ra thuhu ra ñ’ot¯’et¯’et¯’a ra thuhu ra thuhu ra thuhu ra thuhu ra
thuhu ra thuhu ra thuhu ra hnini .
H: Nu’u xki tsoh¯o nuni M’onda .
P: Ra nge’a ra thuhu ra b’ui¯ ha ra thuhu ra thuhu ra thuhu ra thuhu ra thuhu ra thuhu ra thuhu ra thuhu ra thuhu ra
thuhu ra thuhu ra thuhu ra thuhu ra thuhu ,
H: Ra nge’a ra b’em¯ ’em¯ ’em¯ ’i .
quy
P: Asiria nacionpa norte lawninpim, Sus X00 watapa norte lawninpi kaq Sus X00 watakunapi religionniyoq punta
apaqkunawan hukllawakurqaku.
H: Jesuspa tiemponpi iglesia
P: Crown Squarepa hichpanpim tarikunku palaciopi, chayqa Escocia nacionpa chawpinpim kachkan
H: Alemania nacionpa Plaza sutiyoq runam qollqepaq apuestaspa palaciopi cuentallikun
shp
P: Westiora yoxan yoxanya riki ea, jainxon westiora westiora westiora westiora westioraya iki.
H: Iririririririririririririririririricancancancancancancan.
P: Nato yobinbinki jawe ati iki, jainxon min keni raometi iki, jainxon westiora westiora westiora raomeomeai,
jainxon min kenkin.
H:Chomomomomomomomomomomomomomomomomomomomomomomomomomomomomomomo
momomomomomomomomomomomomomomomomomomomomomomomomomomomomomo-
momomomomomomomom omomomomomomomomomomomomomomomomomomomomomomomomomomo-
momomomomomomomomomomomomomomomomomomomomomomomomomomomomomomomomomomin
tar
P: ( 2 ) ¿ chí mu ´re’pá ? ¿ chí mu ´re’pá ? ¿ atza be’pá ? ¿ chí mu ´re’pá ?
H: a’rí ko’rí ko’rí ko’rí ko’rí ko’rí ko’rí ko’rí ko’rí ko’rí ko’rí ko’rí ko’rí ko’rí ko’rí ko’rí ko’rí ko ba’rí ko’rí ko pe pe
pe pe pe pe pe pe pe pe pe pe pe pe pe pe pe pe pe a’rí mi mi mi mi mi mi mi mi mi mi mi mi mi mi mi mi’rí ko’rí
ko’rí ko ´re’rí ko’rí ko’rí ko’rí ko’rí ko’rí ko’rí ko’rí ko’rí ko’rí ko mapu mapu mapu mapu ´re’rí ko’rí ko’rí ko’rí ko’rí
ko’rí ko’rí ko ´re’rí ko ´re’rí ko ´re’rí ko’rí ko ´re’rí ko ´re’rí ko ´re’rí ko’rí ko ´re’rí ko ba’rí
P: ( 2 ) a ) pe ´re’pá ´re’pá ´re’pá ´re’pá ´re’pá ´re’pá ´re’pá ´re’pá ´re’pá ´re’pá ´re’pá ´re’pá ´re’pá ´re’rí ko , pe pe pe ´re’pá
´re’pá ´re’pá ´re’pá ´re’pá ´re’pá ´re’pá ´re’pá ´re’pá ´re’pá ´re’pá ´re’pá ´re’pá ´re’pá ´re’pá ´re’pá ´re’pá ´re’pá ´re’pá ´re’pá ´re’pá
´re’pá ´re’pá ´re’pá ´re’pá ´re’pá ´re’pá bo’pá bo’pá ´re’pá ´re’pá ´re’pá ´re’pápápá ´re’pá ´re’pá ´re’pá ´re’pá ´re’pá ´re’pá ´re’pá
´re’pá ´re’pá ´re’pá ´re’pá ´re’rí ko ba’pá ´re’pá ´re’pá
H: ( 2 ) ( b ) pe ´re’chí na’chí na’chí
Table D.3: Two randomly selected translate-train examples.

```
