---
title: "2023-Dione-MasakhaPOS Part-of-Speech Tagging for Typologically Diverse African - PDF Extract"
source_pdf: "2023-Dione-MasakhaPOS Part-of-Speech Tagging for Typologically Diverse African.pdf"
pages: 16
extracted_at: "2026-02-13T09:50:29.811428"
---

# PDF Extract: 2023-Dione-MasakhaPOS Part-of-Speech Tagging for Typologically Diverse African

**Source PDF:** 2023-Dione-MasakhaPOS Part-of-Speech Tagging for Typologically Diverse African.pdf
**Total Pages:** 16

---

## Content

```
--- Page 1 ---

MasakhaPOS: Part-of-Speech Tagging for Typologically Diverse African
Languages
Cheikh M. Bamba Dione1,†,∗, David Ifeoluwa Adelani2,†,∗, Peter Nabende3,†, Jesujoba O. Alabi4,†,
Thapelo Sindane5, Happy Buzaaba6†, Shamsuddeen Hassan Muhammad7,8†,
Chris Chinenye Emezue9,10†, Perez Ogayo11†, Anuoluwapo Aremu†, Catherine Gitau†,
Derguene Mbaye12†, Jonathan Mukiibi3†, Blessing Sibanda†, Bonaventure F. P. Dossou10,13,14†,
Andiswa Bukula15, Rooweither Mabuya15, Allahsera Auguste Tapo16†, Edwin Munkoh-Buabeng17†,
Victoire Memdjokam Koagne†, Fatoumata Ouoba Kabore18†, Amelia Taylor19, Godson Kalipe†,
Tebogo Macucwa5, Vukosi Marivate5,13†, Tajuddeen Gwadabe†, Elvis Tchiaze Mboning†,
Ikechukwu Onyenwe20, Gratien Atindogbe21, Tolulope Anu Adelani†, Idris Akinade22,
Olanrewaju Samuel†, Marien Nahimana, Théogène Musabeyezu, Emile Niyomutabazi,
Ester Chimhenga, Kudzai Gotosa, Patrick Mizha, Apelete Agbolo23, Seydou Traore24,
Chinedu Uchechukwu20, Aliyu Yusuf8, Muhammad Abdullahi8, Dietrich Klakow4
†Masakhane NLP, 1Université Gaston Berger, Senegal, 2University College London, UK, 3Makerere University, Uganda,
4Saarland University, Germany, 5University of Pretoria, South Africa, 6 RIKEN Center for AIP, Japan,
7Bayero University Kano, Nigeria. 8University of Porto, Portugal, 9Technical University of Munich, Germany, 10Lanfrica,
11Carnegie Mellon University, USA, 12Baamtu, Senegal, 13Lelapa AI, 14Mila Quebec AI Institute, Canada,
15SADiLaR, South Africa, 16Rochester Institute of Technology, USA, 17TU Clausthal, Germany, 18Uppsala University, Sweden,
19Malawi University of Business and Applied Science, Malawi, 20Nnamdi Azikiwe University, Nigeria,
21University of Buea, Cameroon, 22University of Ibadan, Nigeria, 23Ewegbe Akademi, Togo, 24AMALAN, Mali.
Abstract
In this paper, we present MasakhaPOS, the
largest part-of-speech (POS) dataset for 20 ty-
pologically diverse African languages.
We
discuss the challenges in annotating POS for
these languages using the UD (universal de-
pendencies) guidelines. We conducted exten-
sive POS baseline experiments using condi-
tional random field and several multilingual pre-
trained language models. We applied various
cross-lingual transfer models trained with data
available in UD. Evaluating on the Masakha-
POS dataset, we show that choosing the best
transfer language(s) in both single-source and
multi-source setups greatly improves the POS
tagging performance of the target languages, in
particular when combined with cross-lingual
parameter-efficient fine-tuning methods. Cru-
cially, transferring knowledge from a language
that matches the language family and mor-
phosyntactic properties seems more effective
for POS tagging in unseen languages.
1
Introduction
Part-of-Speech (POS) tagging is a process of as-
signing the most probable grammatical category
∗Equal contribution.
(or tag) to each word (or token) in a given sen-
tence of a particular natural language. POS tagging
is one of the fundamental steps for many natural
language processing (NLP) applications, including
machine translation, parsing, text chunking, spell
and grammar checking. While great strides have
been made for (major) Indo-European languages
such as English, French and German, work on the
African languages is quite scarce. The vast major-
ity of African languages lack annotated datasets for
training and evaluating basic NLP systems.
There have been recent works on the develop-
ment of benchmark datasets for training and eval-
uating models in African languages for various
NLP tasks, including machine translation (NLLB-
Team et al., 2022; Adelani et al., 2022a), text-to-
speech (Ogayo et al., 2022; Meyer et al., 2022),
speech recognition (Ritchie et al., 2022), senti-
ment analysis (Muhammad et al., 2022, 2023),
news topic classification (Adelani et al., 2023),
and named entity recognition (Adelani et al., 2021,
2022b). However, there is no large-scale dataset
for POS covering several African languages.
To tackle the data bottleneck issue for low-
resource languages, recent work applied cross-
lingual transfer (Artetxe et al., 2020; Pfeiffer et al.,
arXiv:2305.13989v1  [cs.CL]  23 May 2023

--- Page 2 ---

2020; Ponti et al., 2020) using multilingual pre-
trained language models (PLMs) (Conneau et al.,
2020) to model specific phenomena in low-resource
target languages. While such a cross-lingual trans-
fer is often evaluated by fine-tuning multilingual
models on English data, more recent work has
shown that English is not often the best transfer
language (Lin et al., 2019; de Vries et al., 2022;
Adelani et al., 2022b).
Contributions
In
this
paper,
we
develop
MasakhaPOS — the largest POS dataset for 20
typologically diverse African languages. We high-
light the challenges of annotating POS for these
diverse languages using the universal dependencies
(UD) (Nivre et al., 2016) guidelines such as tok-
enization issues, and POS tags ambiguities. We
provide extensive POS baselines using conditional
random field (CRF) and several multilingual pre-
trained language models (PLMs). Furthermore,
we experimented with different parameter-efficient
cross-lingual transfer methods (Pfeiffer et al., 2021;
Ansell et al., 2022), and transfer languages with
available training data in the UD. Our evaluation
demonstrates that choosing the best transfer lan-
guage(s) in both single-source and multi-source
setups leads to large improvements in POS tag-
ging performance, especially when combined with
parameter-fine-tuning methods. Finally, we show
that a transfer language that belongs to the same
language family and shares similar morphologi-
cal characteristics (e.g. Non-Bantu Niger-Congo)
seems to be more effective for tagging POS in un-
seen languages. For reproducibility, we release our
code, data and models on GitHub1
2
Related Work
In the past, efforts have been made to build a
POS tagger for several African languages, includ-
ing Hausa (Tukur et al., 2020), Igbo (Onyenwe
et al., 2014), Kinyarwanda (Cardenas et al., 2019),
Luo (De Pauw et al., 2010), Setswana (Malema
et al., 2017, 2020), isiXhosa (Delman, 2016),
Wolof (Dione et al., 2010), Yorùbá (Sèmiyou et al.,
2012; Ishola and Zeman, 2020), and isiZulu (Kol-
eva, 2013). While POS tagging has been investi-
gated for the aforementioned languages, annotated
datasets exist only in a few African languages. In
the Universal dependencies dataset (Nivre et al.,
1https://github.com/masakhane-io/
masakhane-pos
2016), nine African languages2 are represented.
Still, only four of the nine languages have training
data, i.e. Afrikaans, Coptic, Nigerian-Pidgin, and
Wolof. In this work, we create the largest POS
dataset for 20 African languages following the UD
annotation guidelines.
3
Languages and their characteristics
We focus on 20 Sub-Saharan African languages,
spoken in circa 27 countries in the Western, East-
ern, Central and Southern regions of Africa. An
overview of the focus languages is provided in
Table 1. The selected languages represent four lan-
guage families: Niger-Congo (17), Afro-Asiatic
(Hausa), Nilo-Saharan (Luo), and English Creole
(Naija). Among the Niger-Congo languages, eight
belong to the Bantu languages.
The writing system of our focus languages is
mostly based on Latin script (sometimes with
additional letters and diacritics). Besides Naija,
Kiswahili, and Wolof, the remaining languages are
all tonal. As far as morphosyntax is concerned,
noun classification is a prominent grammatical fea-
ture for an important part of our focus languages.
12 of the languages actively make use of between
6–20 noun classes. This includes all Bantu lan-
guages, Ghomálá’, Mossi, Akan and Wolof (Nurse
and Philippson, 2006; Payne et al., 2017; Bodomo
and Marfo, 2002; Babou and Loporcaro, 2016).
Noun classes can play a central role in POS anno-
tation. For instance, in isiXhosa, adding the class
prefix can change the grammatical category of the
word (Delman, 2016). All languages use the SVO
word order, while Bambara additionally uses the
SOV word order. Appendix A provides the details
about the language characteristics.
4
Data and Annotation for MasakhaPOS
4.1
Data collection
Table 1 provides the data source used for POS an-
notation — collected from online newspapers. The
choice of the news domain is threefold. First, it is
the second most available resource after the reli-
gious domain for most African languages. Second,
it covers a diverse range of topics. Third, the news
domain is one of the dominant domains in the UD.
We collected monolingual news corpus with an
open license for about eight African languages,
mostly from local newspapers. For the remaining
2including Amharic, Bambara, Beja, Yorùbá, and Zaar
with no training data in UD.

--- Page 3 ---

African
No. of
#
Average sentence
Language
Family
Region
Speakers
Source
Train / dev / test
Tokens
Length (# Tokens)
Bambara (bam)
NC / Mande
West
14M
MAFAND-MT (Adelani et al., 2022a)
793/ 158/ 634
40,137
25.9
Ghomálá’ (bbj)
NC / Grassfields
Central
1M
MAFAND-MT
750/ 149/ 599
23,111
15.4
Éwé (ewe)
NC / Kwa
West
7M
MAFAND-MT
728/ 145/ 582
28,159
19.4
Fon (fon)
NC / Volta-Niger
West
2M
MAFAND-MT
798/ 159/ 637
49,460
30.6
Hausa (hau)
Afro-Asiatic / Chadic
West
63M
Kano Focus and Freedom Radio
753/ 150/ 601
41,346
27.5
Igbo (ibo)
NC / Volta-Niger
West
27M
IgboRadio and Ka O. dI. Taa
803/ 160/ 642
52,195
32.5
Kinyarwanda (kin)
NC / Bantu
East
10M
IGIHE, Rwanda
757/ 151/ 604
40,558
26.8
Luganda (lug)
NC / Bantu
East
7M
MAFAND-MT
733/ 146/ 586
24,658
16.8
Luo (luo)
Nilo-Saharan
East
4M
MAFAND-MT
757/ 151/ 604
45,734
30.2
Mossi (mos)
NC / Gur
West
8M
MAFAND-MT
757/ 151/ 604
33,791
22.3
Chichewa (nya)
NC / Bantu
South-East
14M
Nation Online Malawi
728/ 145/ 582
24,163
16.6
Naija (pcm)
English-Creole
West
75M
MAFAND-MT
752/ 150/ 600
38,570
25.7
chiShona (sna)
NC / Bantu
South
12M
VOA Shona
747/ 149/ 596
39,785
26.7
Kiswahili (swa)
NC / Bantu
East & Central
98M
VOA Swahili
675/ 134/ 539
40,789
29.5
Setswana (tsn)
NC / Bantu
South
14M
MAFAND-MT
753/ 150/ 602
41,811
27.9
Akan/Twi (twi)
NC / Kwa
West
9M
MAFAND-MT
775/ 154/ 618
41,203
26.2
Wolof (wol)
NC / Senegambia
West
5M
MAFAND-MT
770/ 154/ 616
44,002
28.2
isiXhosa (xho)
NC / Bantu
South
9M
Isolezwe Newspaper
752/ 150/ 601
25,313
16.8
Yorùbá (yor)
NC / Volta-Niger
West
42M
Voice of Nigeria and Asejere
875/ 174/ 698
43,601
24.4
isiZulu (zul)
NC / Bantu
South
27M
Isolezwe Newspaper
753/ 150/ 601
24,028
16.0
Table 1: Languages and Data Splits for MasakhaPOS Corpus. Language, family (NC: Niger-Congo), number of
speakers, news source, and data split in number of sentences.
12 languages, we make use of MAFAND-MT (Ade-
lani et al., 2022a) translation corpus that is based
on the news domain. While there are a few is-
sues with translation corpus such as translationese
effect, we did not observe serious issues in anno-
tation. The only issue we experienced was a few
misspellings of words, which led to annotators la-
beling a few words with the "X" tag. However, as a
post-processing step, we corrected the misspellings
and assigned the correct POS tags.
4.2
POS Annotation Methodology
For the POS annotation task, we collected 1,500
sentences per language. As manual POS annota-
tion is very tedious, we agreed to manually anno-
tate 100 sentences per language in the first instance.
This data is then used as training data for automatic
POS tagging (i.e., fine-tuning RemBERT (Chung
et al., 2021) PLM) of the remaining unannotated
sentences. Annotators proceeded to fix the mis-
takes of the predictions (i.e. 1,400 sentences). This
drastically reduced the manual annotation efforts
since a few tags are predicted with almost 100%
accuracy like punctuation marks, numbers and sym-
bols. Proper nouns were also predicted with high
accuracy due to the casing feature.
To support work on manual corrections of an-
notations, most of the languages used the IO An-
notator3 tool, a collaborative annotation platform
for text and images. The tool provides support for
multi-user annotations simultaneously on datasets.
For each language, we hired three native speakers
with linguistics backgrounds to perform POS an-
3https://ioannotator.com/
notation.4 To ensure high-quality annotation, we
recruited a language coordinator to supervise anno-
tation in each language. In addition, we provided
online support (documentation and video tutori-
als) to train annotators on POS annotation. We
made use of the Universal POS tagset (Petrov et al.,
2012), which contains 17 tags.5 To avoid the use of
spurious tags, for each word to be annotated, anno-
tators have to choose one of the possible tags made
available on the IO Annotator tool through a drop-
down menu. For each language, annotation was
done independently by each annotator. At the end
of annotation, language coordinators worked with
their team to resolve disagreements using IOAnno-
tator or Google Spreadsheet. We refer to our newly
annotated POS dataset as MasakhaPOS.
4.3
Quality Control
Computation of automatic inter-agreement metrics
scores like Fleiss Kappa was a bit challenging due
to tokenization issues, e.g. many compound family
names are split. Instead, we adopted the tokeniza-
tion defined by annotators since they are annotating
all words in the sentence. Due to several annota-
tion challenges as described in section 5, seven
language teams (Ghomálá’, Fon, Igbo, Chichewa
chiShona, Kiswahili, and Wolof) decided to en-
gage annotators on online calls (or in person dis-
cussions) to agree on the correct annotation for
each word in the sentence. The other language
teams allowed their annotators to work individu-
ally, and only discuss sentences on which they did
not agree. Seven of the 13 languages achieved a
4Each annotator was paid $750 for 1,500 sentences.
5https://universaldependencies.org/u/pos/

--- Page 4 ---

sentence-level annotation agreement of over 75%.
Two more languages (Luganda and isiZulu) have
sentence-level agreement scores of between 64.0%
to 67.0%. The remaining four languages (Ewe,
Luo, Mossi, and Setswana) only agreed on less
than 50% of the annotated sentences. This con-
firms the difficulty of the annotation task for many
language teams. Despite this challenge, we ensured
that all teams resolved all disagreements to produce
high-quality POS corpus. Appendix B provides de-
tails of the number of agreed annotation by each
language team.
After quality control, we divided the annotated
sentences into training, development and test splits
consisting of 50%, 10%, 40% of the data respec-
tively. We chose a larger test set proportion that is
similar to the size of test sets in the UD, usually
larger than 500 sentences. Table 1 provides the de-
tails of the data split. We split very long sentences
into two to fit the maximum sequence length of 200
for PLM fine-tuning. We further performed manual
checks to correct sentences split at arbitrary parts.
5
Annotation challenges
When annotating our focus languages, we faced
two main challenges: tokenization and POS ambi-
guities.
5.1
Tokenization and word segmentation
In UD, the basic annotation units are syntactic
words (rather than phonological or orthographical
words) (Nivre et al., 2016). Accordingly, clitics
need to be split off and contraction must be un-
done where necessary. Applying the UD annotation
scheme to our focus languages was not straightfor-
ward due to the nature of those languages, espe-
cially with respect to the notion of word, the use of
clitics and multiword units.
5.1.1
Definition of word
For many of our focus languages (e.g. Chichewa,
Luo, chiShona, Wolof and isiXhosa), it was dif-
ficult to establish a dividing line between a word
and a phrase. For instance, the chiShona word
ndakazomuona translates into English as a whole
sentence (‘I eventually saw him’).
This word
consists of several morphemes that convey dis-
tinct morphosyntactic information (Chabata, 2000):
Nda- (subject concord), -ka- (aspect), -zo- (aux-
iliary), -mu- (object concord), -ona- (verb stem).
This illustrates pronoun incorporation (Bresnan and
Mchombo, 1987), i.e. subject and/or object pro-
nouns appear as bits of morphology on a verb or
other head, functioning as agreement markers. Nat-
urally, one may want to split this word into several
tokens reflecting the different grammatical func-
tions. For UD, however, morphological features
such as agreement are encoded as properties of
words and there is no attempt at segmenting words
into morphemes, implying that items like ndaka-
zomuona should be treated as a single unit.
5.1.2
Clitics
In languages like Hausa, Igbo, IsiZulu, Kin-
yarwanda, Wolof and Yorùbá, we observed an ex-
tensive use of cliticization. Function words such
as prepositions, conjunctions, auxiliaries and de-
terminers can attach to other function or content
words. For example, the Igbo contracted form yana
consists of a pronoun (PRON) ya and a coordi-
nating conjunction (CCONJ) na. Following UD,
we segmented such contracted forms, as they cor-
respond to multiple (syntactic) words. However,
there were many cases of fusion where a word
has morphemes that are not necessarily easily seg-
mentable. For instance, the chiShona word vave
translates into English as ‘who (PRON) are (AUX)
now (ADV)’. Here, the morpheme -ve, which func-
tions both as auxiliary and adverb, cannot be further
segmented, even though it corresponds to multiple
syntactic words. Ultimately, we treated the word
vave as a unit, which received the AUX POS tag.
In addition, there were word contractions with
phonological changes, posing serious challenges,
as proper segmentation may require to recover the
underlying form first. For instance, the Wolof con-
tracted form “cib" (Dione, 2019) consists of the
preposition ci ‘in’ and the indefinite article ab ‘a’.
However, as a result of phonological change, the
initial vowel of the article is deleted. Accordingly,
to properly segment the contracted form, it won’t
be sufficient to just extract the preposition ci be-
cause the remaining form b will not have meaning.
Also, some word contractions are ambiguous. For
instance, in Wolof, a form like geek can be split
into gi ‘the’ and ak where ak can function as a
conjunction ‘and’ or as a preposition ‘with’.
5.1.3
One unit or multitoken words?
Unlike the issue just described in 5.1.2, it was some-
times necessary to go in the other direction, and
combine several orthographic tokens into a sin-
gle syntactic word. Examples of such multitoken

--- Page 5 ---

words are found e.g. in Setswana (Malema et al.,
2017). For instance, in the relative structure ng-
wana yo o ratang (the child who likes ...), the rela-
tive marker yo o is a multitoken word that matches
the noun class (class 1) of the relativized noun ng-
wana (‘child’), which is subject of the verb ratang
(‘to like’). In UD, multitoken words are allowed for
a restricted class of phenomena, such as numerical
expressions like 20 000 and abbreviations (e. g.).
We advocate that this restricted class be expanded
to phenomena like Setswana relative markers.
5.2
POS ambiguities
There were cases where a word form lies on the
boundary between two (or more) POS categories.
5.2.1
Verb or conjunction?
In quite a few of our focus languages (e.g. Yorùbá,
Wolof), a form of the verb ‘say’ is also used as a
subordinate conjunction (to mark out clause bound-
aries) with verbs of speaking. For example, in the
Yorùbá sentence Olú gbàgbé pé Bolá tí jàde (lit.
‘Olu forgot that Bola has gone’) (Lawal, 1991), the
item pé seems to behave both like a verb and a sub-
ordinate conjunction. On the one hand, because of
the presence of another verb gbàgbé ‘to forget’, the
pattern may be analyzed as a serial verb construc-
tion (SVC) (Oyelaran, 1982; Güldemann, 2008),
i.e. a construction that contains sequences of two
or more verbs without any syntactic marker of sub-
ordination. This would mean that pé is a verb. On
the other hand, however, this item shows properties
of a complementizer (Lawal, 1991). For instance,
pé can occur in sentence initial position, which
in Yorùbá is typically occupied by subordinating
conjunctions. Also, unlike verbs, pé cannot un-
dergo reduplication for nominalization (an ability
that all Yorùbá verbs have). This seems to pro-
vide evidence for treating this item as a subordinate
conjunction rather than a verb.
5.2.2
Adjective or Verb?
In some of our focus languages, the category of ad-
jectives is not entirely distinct morpho-syntactically
from verbs. In Wolof and Yorùbá, the notions that
would be expressed by adjectives in English are en-
coded through verbs (McLaughlin, 2004). Igbo
(Welmers, 2018) and Éwé (McLaughlin, 2004)
have a very limited set of underived adjectives (8
and 5, respectively). For instance, in Wolof, unlike
in English, an ‘adjective’ like gaaw ‘be quick’ does
not need a copula (e.g. ‘be’ in English) to function
as a predicate. Likewise, the Bambara item téli
‘quick’ as in the sentence Sò ka téli ‘The horse is
quick’ (Aplonova and Tyers, 2017) has adjectival
properties, as it is typically used to modify nouns
and specify their properties or attributes. It also
has verbal properties, as it can be used in the main
predicative position functioning as a verb. This is
signaled by the presence of the auxiliary ka, which
is a special predicative marker ka that typically
accompanies qualitative verbs (Vydrin, 2018).
5.2.3
Adverbs or particles?
The distinction between adverbs and particles was
not always straightforward. For instance, many of
our focus languages have ideophones, i.e. words
that convey an idea by means of a sound (often
reduplicated) that expresses an action, quality, man-
ner, etc. Ideophones may behave like adverbs by
modifying verbs for such categories as time, place,
direction or manner. However, they can also func-
tion as verbal particles. For instance, in Wolof, an
ideophone like jërr as in tàng jërr “very hot” (tàng
means “to be hot”) is an intensifier that only co-
occurs as a particle of that verb. Thus, it would
not be motivated to treat it as another POS other
than PART. Whether such ideophones are PART or
ADV or the like varies depending on the language.
6
Baseline Experiments
6.1
Baseline models
We provide POS tagging baselines using both CRF
and multilingual PLMs. For the PLMs, we fine-
tune three massively multilingual PLMs pre-trained
on at least 100 languages (mBERT (Devlin et al.,
2019), XLM-R (Conneau et al., 2020), and Rem-
BERT (Chung et al., 2021)), and three Africa-
centric PLMs like AfriBERTa (Ogueji et al., 2021),
AfroXLMR (Alabi et al., 2022), and AfroLM (Dos-
sou et al., 2022) pre-trained on several African
languages. The baseline models are:
CRF
is one of the most successful sequence la-
beling approach prior to PLMs. CRF models the
sequence labeling task as an undirected graphical
model, using both labelled observations and contex-
tual information as features. We implemented the
CRF model using sklearn-crfsuite,6 using
the following features: the word to be tagged, two
consecutive previous and next words, the word in
lowercase, prefixes and suffixes of words, length
6https://sklearn-crfsuite.readthedocs.io/

--- Page 6 ---

Model
bam
bbj
ewe
fon
hau
ibo
kin
lug
luo
mos
nya
pcm
sna
swa
tsn
twi
wol
xho
yor
zul
AVG
CRF
89.1
78.9
88.0
88.1
89.8
75.2
95.3
88.3
84.6
86.0
77.7
85.6
85.9
89.3
81.4
81.5
91.0
81.8
92.0
84.2
85.7
Massively-multilingual PLMs
mBERT (172M)
89.9
75.2
86.0
87.6
90.7
76.5
96.9
89.6
87.0
86.5
79.9
90.4
87.5
92.0
81.9
83.9
92.5
85.9
93.4
86.8
87.0
XLM-R-base (270M)
90.1
83.6
88.5
90.1
92.5
77.2
96.7
89.1
87.2
90.7
79.9
90.5
87.9
92.9
81.3
84.1
92.4
87.4
93.7
88.0
88.2
XLM-R-large (550M)
90.2
85.4
88.8
90.2
92.8
78.1
97.3
90.0
88.0
91.1
80.5
90.8
88.1
93.2
82.2
84.9
92.9
88.1
94.2
89.4
88.8
RemBERT (575M)
90.6
82.6
88.9
90.8
93.0
79.3
98.0
90.3
87.5
90.4
82.4
90.9
89.1
93.1
83.6
86.0
92.1
89.3
94.7
90.2
89.1
Africa-centric PLMs
AfroLM (270M)
89.2
77.8
87.5
82.4
92.7
77.8
97.4
90.8
86.8
89.6
81.1
89.5
88.7
92.8
83.8
83.9
92.1
87.5
91.1
88.8
87.6
AfriBERTa-large (126M)
89.4
79.6
87.4
88.4
93.0
79.3
97.8
89.8
86.5
89.9
79.7
89.8
87.8
93.0
82.5
83.7
91.7
86.1
94.5
86.9
87.8
AfroXLMR-base (270M)
90.2
83.5
88.5
90.1
93.0
79.1
98.2
90.9
86.9
90.9
82.7
90.8
89.2
92.9
82.7
84.3
92.4
88.5
94.5
89.4
88.9
AfroXLMR-large (550M)
90.5
85.3
88.7
90.4
93.0
78.9
98.4
91.6
88.1
91.2
83.2
91.2
89.5
93.2
83.0
84.9
92.9
88.7
95.0
90.1
89.4
Table 2: Accuracy of baseline models on MasakhaPOS dataset . We compare several multilingual PLMs
including the ones trained on African languages. Average is over 5 runs.
ADJ
ADP
ADV
AUX
CCONJ
DET
INTJ
NOUN
NUM
PART
PRON
PROPN
PUNCT
SCONJ
SYM
VERB
X
ACC
bam
41.0
77.0
72.0
82.0
91.0
0.0
91.0
90.0
95.0
97.0
82.0
100.0
71.0
25.0
83.0
0.0
90.7
bbj
71.0
80.0
67.0
89.0
84.0
85.0
0.0
82.0
86.0
78.0
91.0
92.0
100.0
88.0
86.0
85.6
ewe
72.0
83.0
57.0
94.0
89.0
100.0
91.0
91.0
87.0
90.0
93.0
100.0
84.0
13.0
82.0
88.7
fon
91.0
88.0
69.0
75.0
94.0
96.0
91.0
90.0
89.0
95.0
91.0
100.0
51.0
89.0
90.4
hau
86.0
80.0
71.0
96.0
89.0
84.0
0.0
94.0
98.0
95.0
76.0
98.0
99.0
86.0
96.0
62.0
92.9
ibo
95.0
89.0
56.0
98.0
76.0
79.0
0.0
70.0
95.0
0.0
98.0
95.0
100.0
6.0
0.0
81.0
79.2
kin
86.0
99.0
91.0
0.0
100.0
99.0
99.0
100.0
84.0
98.0
97.0
100.0
97.0
0.0
99.0
0.0
98.4
lug
71.0
96.0
72.0
90.0
90.0
76.0
94.0
93.0
94.0
15.0
94.0
100.0
89.0
92.0
91.6
luo
73.0
88.0
69.0
87.0
69.0
82.0
89.0
96.0
86.0
42.0
89.0
100.0
94.0
100.0
86.0
0.0
88.2
mos
64.0
83.0
72.0
91.0
93.0
84.0
91.0
93.0
94.0
83.0
90.0
100.0
95.0
92.0
91.2
nya
74.0
79.0
56.0
25.0
77.0
81.0
20.0
92.0
86.0
12.0
73.0
86.0
99.0
6.0
89.0
83.1
pcm
78.0
97.0
74.0
86.0
98.0
92.0
95.0
98.0
90.0
86.0
91.0
98.0
86.0
45.0
91.0
91.1
sna
51.0
94.0
44.0
87.0
89.0
83.0
95.0
96.0
0.0
78.0
92.0
99.0
58.0
60.0
94.0
89.4
swa
95.0
86.0
65.0
82.0
95.0
56.0
97.0
98.0
86.0
51.0
97.0
100.0
91.0
95.0
0.0
93.1
tsn
57.0
80.0
82.0
42.0
53.0
78.0
17.0
94.0
97.0
62.0
76.0
91.0
99.0
18.0
0.0
95.0
0.0
82.4
twi
55.0
82.0
68.0
52.0
87.0
93.0
0.0
86.0
77.0
21.0
82.0
92.0
100.0
9.0
0.0
87.0
84.8
wol
0.0
94.0
81.0
94.0
96.0
90.0
22.0
91.0
90.0
98.0
92.0
96.0
100.0
85.0
62.0
94.0
92.9
xho
73.0
69.0
47.0
17.0
88.0
54.0
0.0
87.0
100.0
80.0
95.0
100.0
57.0
0.0
90.0
88.3
yor
84.0
92.0
82.0
99.0
97.0
97.0
95.0
94.0
83.0
95.0
96.0
100.0
98.0
95.0
0.0
95.1
zul
68.0
26.0
72.0
21.0
67.0
82.0
0.0
91.0
99.0
81.0
99.0
100.0
91.0
100.0
91.0
96.0
90.0
AVE
69.2
83.1
68.4
69.1
86.4
79.0
15.9
90.8
93.4
69.7
79.0
92.8
99.7
68.0
33.8
90.4
19.8
89.4
Table 3: Tag distribution of the “AfroXLMR-large” -based POS tagger (reporting results from the first run).
The tags with high average accuracy (> 90.0% ) across all languages are highlighted in gray .
of the word, and other boolean features like is the
word a digit, a punctuation mark, the beginning of
a sentence or end of a sentence.
Massively multilingual PLM
We fine-tune
mBERT, XLM-R (base & large), and RemBERT
pre-trained on 100-110 languages, but only few
African languages. mBERT, XLM-R, and Rem-
BERT were pre-trained on two (swa & yor), three
(hau, swa, & xho), and eight (hau, ibo, nya,
sna, swa, xho, yor, & zul) of our focus lan-
guages respectively. The three models were all
pre-trained using masked language model (MLM),
mBERT and RemBERT additionally use the next-
sentence prediction objective.
Africa-centric PLMs
We fine-tune AfriBERTa,
AfroLM and AfroXLMR (base & large). The first
two PLMs were pre-trained using XLM-R style pre-
training, AfroLM additionally make use of active
learning during pre-training to address data scarcity
of many African languages. On the other hand,
AfroXLMR was created through language adapta-
tion (Pfeiffer et al., 2020) of XLM-R on 17 African
languages, “eng”, “fra”, and “ara”. AfroLM was
pre-trained on all our focus languages, while AfriB-
ERTa and AfroXLMR were pre-trained on 6 (hau,
ibo, kin, pcm, swa, & yor) and 10 (hau, ibo,
kin, nya, pcm, sna, swa, xho, yor, & zul)
respectively. We fine-tune all PLMs using the Hug-
gingFace Transformers library (Wolf et al., 2020).
For PLM fine-tuning, we make use of a max-
imum sequence length of 200, batch size of 16,
gradient accumulation of 2, learning rate of 5e −5,
and number of epochs 50. The experiments were
performed on using Nvidia V100 GPU.
6.2
Baseline results
Table 2 shows the results of training POS tag-
gers for each focus language using the CRF and
PLMs. Suprinsingly, the CRF model gave a very
impressive result for all languages with only a few
points below the best PLM (−3.7). In general, fine-
tuning PLMs gave a better result for all languages.
The mBERT performance is (+1.3) better in accu-
racy than CRF. AfroLM and AfriBERTa are only
slightly better than mBERT with (< 1 point). One
of the reasons for AfriBERTa’s poor performance
is that most of the languages are unseen during

--- Page 7 ---

pre-training.7 On the other hand, AfroLM was pre-
trained on all our focus languages but on a small
dataset (0.73GB) which makes it difficult to train
a good representation for each of the languages
covered during pre-training. Furthermore, XLM-
R-base gave slightly better accuracy on average
than both AfroLM (+0.6) and AfriBERTa (+0.4)
despite seeing fewer African languages. However,
the performance of the AfroXLMR-base exceeds
that of XLM-R-base because it has been further
adapted to 17 typologically diverse African lan-
guages, and the performance (±0.1) is similar to
the larger PLMs i.e RemBERT and XLM-R-large.
Impressive performance was achieved by large
versions of massively multilingual PLMs like
XLM-R-large and RemBERT, and AfroXLMR
(base & large) i.e better than mBERT (+1.8 to
+2.4) and better than CRF (+3.1 to +3.7). The
performance of the large PLMs (e.g. AfroXLMR-
large) is larger for some languages when compared
to mBERT like bbj (+10.1), mos (+4.7), nya
(+3.3), and zul (+3.3). Overall, AfroXLMR-
large achieves the best accuracy on average over
all languages (89.4) because it has been pre-trained
on more African languages with larger monolin-
gual data and it’s large size. Interestingly, 11 out
of 20 languages reach an impressive accuracy of
(> 90%) with the best PLM which is an indication
of consistent and high quality POS annotation.
Accuracy by tag distribution
Table 3 shows the
POS tagging results by tag distribution using our
best model “AfroXLMR-large”. The tags that are
easiest (with accuracy over > 90%) to detect across
all languages are PUNCT, NUM, PROPN, NOUN,
and VERB, while the most difficult are SYM, INTJ,
and X tags. The difficult tags are often infrequent,
which does not affect the overall accuracy. Sur-
prisingly, a few languages like Yorùbá and Kin-
yarwanda, have very good accuracy on almost all
tags except for the infrequent tags in the language.
7
Cross-lingual Transfer
7.1
Experimental setup for effective transfer
The effectiveness of zero-shot cross-lingual trans-
fer depends on several factors including the choice
of the best performing PLM, choice of an effective
cross-lingual transfer method, and the choice of the
best source language for transfer. Oftentimes, the
source language chosen for cross-lingual transfer
714 out of 20 languages are unseen
is English due to the availability of training data
which may not be ideal for distant languages espe-
cially for POS tagging (de Vries et al., 2022). To
further improve performance, parameter-efficient
fine-tuning approaches (Pfeiffer et al., 2020; Ansell
et al., 2022) can be leveraged with additional mono-
lingual data for both source and target languages.
We highlight how we combine these different fac-
tors for effective transfer below:
Choice of source languages
Prior work on the
choice of source language for POS tagging shows
that the most important features are geographi-
cal similarity, genetic similarity (or closeness in
language family tree) and word overlap between
source and target language (Lin et al., 2019). We
choose seven source languages for zero-shot trans-
fer based on the following criteria (1) availability
of POS training data in UD,8. Only three African
languages satisfies this criteria (Wolof, Nigerian-
Pidgin, and Afrikaans) (2) geographical prox-
imity to African languages – this includes non-
indigeneous languages that have official status in
Africa like English, French, Afrikaans, and Arabic.
(3) language family similarity to target languages.
The languages chosen are: Afrikaans (afr), Ara-
bic (ara), English (eng), French (fra), Nigerian-
Pidgin (pcm), Wolof (wol), and Romanian (ron).
While Romanian does not satisfy the last two cri-
teria - it was selected based on the findings of
de Vries et al. (2022) — Romanian achieves the
best transfer performance to the most number of
languages in UD. Appendix C shows the data split
for the source languages.
Parameter-efficient cross-lingual transfer
The
standard way of zero-shot cross-lingual transfer
involves fine-tuning a multilingual PLM on the
source language labelled data (e.g.
on a POS
task), and evaluate it on a target language. We
refer to it as FT-Eval (or Fine-tune & evaluate).
However, the performance is often poor for un-
seen languages in PLM and distant languages.
One way to address this is to perform language
adaptation using monolingual corpus in the tar-
get language before fine-tuning on the downstream
task (Pfeiffer et al., 2020), but this setup does not
scale to many languages since it requires modify-
ing all the parameters of the PLM and requires
large disk space (Alabi et al., 2022).
Several
parameter-efficient approaches have been proposed
8https://universaldependencies.org/

--- Page 8 ---

afr
ara
eng
fra
pcm
ron
wol
eng-ron-wol
Source Languages
30
35
40
45
50
55
60
65
70
Accuracy
48.9
36.9
52.6
45.6
32.8
53.1
48.1
56.7
60.5
48.4
63.4
61.7
49.6
63.5
64.8
66.8
61.4
50
66
64.9
52.5
67
65.7
68.8
FT-Eval
LT-SFT
MAD-X
Figure 1: Zero-shot cross-lingual transfer results using FT-Eval, LT-SFT and MAD-X. Average over 20
languages. Experiments performed using AfroXLMR-base. Evaluation metric is Accuracy.
like Adapters (Houlsby et al., 2019) and Lottery-
Ticketing Sparse Fine-tunings (LT-SFT) (Ansell
et al., 2022) —they are also modular and compos-
able making them ideal for cross-lingual transfer.
Here, we make use of MAD-X 2.09 adapter
based approach (Pfeiffer et al., 2020, 2021) and
LT-SFT approach. The setup is as follows: (1)
We train language adapters/SFTs using monolin-
gual news corpora of our focus languages. We
perform language adaptation on the news corpus
to match the POS task domain, similar to (Alabi
et al., 2022). We provide details of the monolin-
gual corpus in Appendix E. (2) We train a task
adapter/SFT on the source language labelled data
using source language adapter/SFT. (3) We sub-
stitute the source language adapter/SFT with the
target language/SFT to run prediction on the target
language test set, while retaining the task adapter.
Choice of PLM
We make use of AfroXLMR-
base as the backbone PLM for all experiments be-
cause it gave an impressive performance in Table 2,
and the availability of language adapters/SFTs
for some of the languages by prior works (Pfeif-
fer et al., 2021; Ansell et al., 2022; Alabi et al.,
2022). When a target language adapter/SFT of
AfroXLMR-base is absent, XLM-R-base language
adapter/SFT can be used instead since they share
the same architecture and number of parameters, as
demonstrated in Alabi et al. (2022). We did not find
XLM-R-large based adapters and SFTs online,10
and they are time-consuming to train especially for
high-resource languages like English.
7.2
Experimental Results
Parameter-efficient fine-tuning are more effec-
tive
Figure 1 shows the result of cross-lingual
9an extension of MAD-X where the last adapter layers are
dropped, which has been shown to improve performance
10https://adapterhub.ml/
transfer from seven source languages with POS
training data in UD, and their average accuracy on
20 African languages. We report the performance
of the standard zero-shot cross-lingual transfer with
AfroXLMR-base (i.e. FT-Eval), and parameter-
efficient fine-tuning approaches i.e MAD-X and
LT-SFT. Our result shows that MAD-X and LT-
SFT gives significantly better results than FT-Eval,
the performance difference is over 10% accuracy
on all languages. This shows the effectiveness
of parameter-efficient fine-tuning approaches on
cross-lingual transfer for low-resource languages
despite only using small monolingual data (433KB
- 50.2MB, as shown in Appendix E) for training tar-
get language adapters and SFTs. Furthermore, we
find MAD-X to be slightly better than LT-SFT espe-
cially when ron (+3.5), fra (+3.2), pcm (+2.9),
and eng (+2.6) are used as source languages.
The best source language
In general, we find
eng, ron, and wol to be better as source lan-
guages to the 20 African languages. For the FT-
Eval, eng and ron have similar performance.
However, for LT-SFT, wol was slightly better than
the other two, probably because we are transfering
from an African language that shares the same fam-
ily or geographical location to the target languages.
For MAD-X, eng was surprisingly the best choice.
Multi-source fine-tuning leads to further gains
Table 4 shows that co-training the best three source
languages (eng, ron, and wol) leads to improved
performance, reaching an impressive accuracy of
68.8% with MAD-X. For the FT-Eval, we per-
formed multi-task training on the combined train-
ing set of the three languages. LT-SFT supports
multi-source fine-tuning — where a task SFT can
be trained on data from several languages jointly.
However, MAD-X implementation does not sup-
port multi-source fine-tuning. We created our ver-

--- Page 9 ---

Method
bam
bbj
ewe
fon
hau
ibo
kin
lug
luo
mos
nya
pcm
sna
swa
tsn
twi
wol
xho
yor
zul
AVG
AVG*
eng as a source language
FT-Eval
52.1
31.9
47.8
32.5
67.1
74.5
63.9
57.8
38.4
45.3
59.0
82.1
63.7
56.9
49.4
35.9
35.9
45.9
63.3
48.8
52.6
51.9
LT-SFT
67.9
57.6
67.9
55.5
69.0
76.3
64.2
61.0
74.5
70.3
59.4
82.4
64.6
56.9
49.5
52.1
78.2
45.9
65.3
49.8
63.4
61.5
MAD-X
62.9
58.5
68.7
55.8
67.0
77.8
70.9
65.7
73.0
71.8
70.1
83.2
69.8
61.2
49.8
53.0
75.2
57.1
66.9
60.9
66.0
64.5
ron as a source language
FT-Eval
46.5
30.5
37.6
30.9
67.3
77.7
73.3
56.9
36.7
40.6
62.2
78.9
66.3
61.0
55.8
35.7
33.8
49.6
63.5
56.3
53.1
52.7
LT-SFT
60.6
57.0
64.9
60.4
67.5
77.4
68.2
58.5
70.2
67.9
58.2
78.1
64.6
59.7
57.4
55.7
81.9
46.3
64.8
51.2
63.5
61.7
MAD-X
63.5
62.2
66.6
61.8
66.5
80.0
73.5
62.7
76.5
71.8
66.0
83.7
71.1
64.5
61.2
53.5
79.5
48.6
69.5
57.8
67.0
65.4
wol as a source language
FT-Eval
40.8
36.5
39.8
37.4
55.1
58.6
49.2
51.8
35.1
44.9
49.0
51.6
53.8
42.9
45.0
38.4
88.6
46.0
52.5
45.5
48.1
45.7
LT-SFT (N)
64.4
64.3
69.8
63.0
67.0
79.7
63.7
64.0
74.1
72.2
56.5
72.7
67.7
53.0
51.3
56.2
92.5
46.0
69.8
47.7
64.8
62.8
MAD-X (N)
46.6
41.8
47.2
37.8
53.9
51.8
41.0
39.0
46.5
44.0
38.3
40.2
44.3
38.8
44.6
40.1
85.6
39.2
46.4
36.0
45.2
43.2
MAD-X (N+W)
61.7
63.6
68.9
63.1
66.8
77.0
67.8
69.1
73.7
71.3
63.2
75.1
68.9
55.8
50.7
54.9
90.4
49.6
70.0
51.7
65.7
63.8
multi-source:
eng-ron-wol
FT-Eval
44.2
36.3
39.3
39.3
69.4
78.5
70.6
59.2
35.5
46.8
60.9
81.4
65.8
58.5
53.8
38.8
89.1
48.8
65.2
53.5
56.7
53.6
LT-SFT
67.4
64.6
70.0
64.2
70.4
81.1
68.7
63.9
76.4
73.9
58.8
83.0
69.6
57.3
52.7
57.2
93.1
45.8
69.8
48.3
66.8
64.4
MAD-X
66.2
65.5
70.3
64.9
69.1
82.3
73.1
68.0
75.1
74.2
69.2
83.9
69.4
62.6
53.6
55.2
90.1
52.3
70.8
59.4
68.8
66.7
Table 4: Cross-lingual transfer to MasakhaPOS . Zero-shot Evaluation using FT-Eval, LT-SFT, and MAD-X, with
ron, eng, and wol as source languages. Experiments are based on AfroXLMR-base. Non-Bantu Niger-Congo
languages highlighted with gray . AVG* excludes pcm and wol from the average since they are source languages.
sion of multi-source fine-tuning following these
steps: (1) We combine all the training data of the
three languages (2) We train a task adapter using
the combined data and one of the best source lan-
guages’ adapter. We experiment using eng, ron,
and wol as source language adapter for the com-
bined data. Our experiment shows that eng or
wol achieves similar performance when used as
language adapter for multi-source fine-tuning. We
only added the result using wol as source adapter
on Table 4. Appendix Appendix F provides more
details on MAD-X multi-source fine-tuning.
Performance difference by language family
Ta-
ble 4 shows the transfer result per language for
the three best source languages. wol has a better
transfer performance to non-Bantu Niger-Congo
languages in West Africa than eng and ron, es-
pecially for bbj, ewe, fon, ibo, mos, twi, and
yor despite having a smaller POS training data
(1.2k sentences) compared to ron (8k sentences)
and eng (12.5k sentences). Also, wol adapter was
trained on a small monolingual corpus (5.2MB).
This result aligns with prior studies that choosing
a source language from the same family leads to
more effective transfer (Lin et al., 2019; de Vries
et al., 2022). However, we find MAD-X to be more
sensitive to the size of monolingual corpus. We
obtained a very terrible transfer accuracy when we
only train language adapter for wol on the news do-
main (2.5MB) i.e MAD-X (N), lower than FT-Eval.
By additionally combining the news corpus with
Wikipedia corpus (2.7MB) i.e MAD-X (N+W), we
were able to obtain an impressive result comparable
to LT-SFT. This highlight the importance of using
larger monolingual corpus to train source language
adapter. wol was not the best source language for
Bantu languages probably because of the difference
in language characteristics. For example, Bantu lan-
guages are very morphologically-rich while non-
Bantu Niger-Congo languages (like wol) are not.
Our further analysis shows that sna was better
in transferring to Bantu languages. Appendix G
provides result for the other source languages.
8
Conclusion
In this paper, we created MasakhaPOS, the largest
POS dataset for 20 typologically-diverse African
languages. We showed that POS annotation of
these languages based on the UD scheme can be
quite challenging, especially with regard to word
segmentation and POS ambiguities. We provide
POS baseline models using CRF and by fine-tuning
multilingual PLMs. We analyze cross-lingual trans-
fer on MasakhaPOS dataset in single-source and
multi-source settings. An important finding that
emerged from this study is that choosing the appro-
priate transfer languages substantially improves
POS tagging for unseen languages.
The trans-
fer performance is particularly effective when pre-
training includes a language that shares typological
features with the target languages.
9
Limitations
Some Language families in Africa not covered
For example, Khoisan and Austronesian (like Mala-
gasy). We performed extensive analysis and exper-
iments on Niger-Congo languages but we only cov-
ered one language each in the Afro-asiatic (Hausa)
and Nilo-Saharan (Dholuo) families.
News domain
Our annotated dataset belong to
the news domain, which is a popular domain in
UD. However, the POS dataset and models may not

--- Page 10 ---

generalize to other domains like speech transcript,
conversation data etc.
Transfer results may not generalize to all NLP
tasks
We have only experimented with POS task,
the best transfer language e.g for non-Bantu Niger-
Congo languages i.e Wolof, may not be the same
for other NLP tasks.
10
Ethics Statement or Broader Impact
Our work aims to understand linguistic character-
istics of African languages, we do not see any po-
tential harms when using our POS datasets and
models to train ML models, the annotated dataset
is based on the news domain, and the articles are
publicly available, and we believe the dataset and
POS annotation is unlikely to cause unintended
harm.
Also, we do not see any privacy risks in using
our dataset and models because it is based on news
domain.
Acknowledgements
This work was carried out with support from La-
cuna Fund, an initiative co-founded by The Rock-
efeller Foundation, Google.org, and Canada’s In-
ternational Development Research Centre. We are
grateful to Sascha Heyer, for extending the ioAn-
notator tool to meet our requirements for POS an-
notation. We appreciate the early advice from Gra-
ham Neubig, Kim Gerdes, and Sylvain Kahane
on this project. David Adelani acknowledges the
support of DeepMind Academic Fellowship pro-
gramme. We appreciate all the POS annotators that
contributed to this dataset. Finally, we thank the
Masakhane leadership, Melissa Omino, Davor Or-
lic and Knowledge4All for their administrative ˇ
support throughout the project.
References
David Adelani, Jesujoba Alabi, Angela Fan, Julia
Kreutzer, Xiaoyu Shen, Machel Reid, Dana Ruiter,
Dietrich Klakow, Peter Nabende, Ernie Chang, Tajud-
deen Gwadabe, Freshia Sackey, Bonaventure F. P.
Dossou, Chris Emezue, Colin Leong, Michael Beuk-
man, Shamsuddeen Muhammad, Guyo Jarso, Oreen
Yousuf, Andre Niyongabo Rubungo, Gilles Hacheme,
Eric Peter Wairagala, Muhammad Umair Nasir, Ben-
jamin Ajibade, Tunde Ajayi, Yvonne Gitau, Jade
Abbott, Mohamed Ahmed, Millicent Ochieng, An-
uoluwapo Aremu, Perez Ogayo, Jonathan Mukiibi,
Fatoumata Ouoba Kabore, Godson Kalipe, Derguene
Mbaye, Allahsera Auguste Tapo, Victoire Memd-
jokam Koagne, Edwin Munkoh-Buabeng, Valen-
cia Wagner, Idris Abdulmumin, Ayodele Awokoya,
Happy Buzaaba, Blessing Sibanda, Andiswa Bukula,
and Sam Manthalu. 2022a. A few thousand trans-
lations go a long way! leveraging pre-trained mod-
els for African news translation. In Proceedings of
the 2022 Conference of the North American Chap-
ter of the Association for Computational Linguistics:
Human Language Technologies, pages 3053–3070,
Seattle, United States. Association for Computational
Linguistics.
David Adelani, Graham Neubig, Sebastian Ruder,
Shruti Rijhwani, Michael Beukman, Chester Palen-
Michel, Constantine Lignos, Jesujoba Alabi, Sham-
suddeen Muhammad,
Peter Nabende,
Cheikh
M. Bamba Dione, Andiswa Bukula, Rooweither
Mabuya, Bonaventure F. P. Dossou, Blessing Sibanda,
Happy Buzaaba, Jonathan Mukiibi, Godson Kalipe,
Derguene Mbaye, Amelia Taylor, Fatoumata Ka-
bore, Chris Chinenye Emezue, Anuoluwapo Aremu,
Perez Ogayo, Catherine Gitau, Edwin Munkoh-
Buabeng, Victoire Memdjokam Koagne, Allah-
sera Auguste Tapo, Tebogo Macucwa, Vukosi Mari-
vate, Mboning Tchiaze Elvis, Tajuddeen Gwad-
abe, Tosin Adewumi, Orevaoghene Ahia, Joyce
Nakatumba-Nabende, Neo Lerato Mokono, Ig-
natius Ezeani, Chiamaka Chukwuneke, Mofetoluwa
Oluwaseun Adeyemi, Gilles Quentin Hacheme,
Idris Abdulmumin, Odunayo Ogundepo, Oreen
Yousuf, Tatiana Moteu, and Dietrich Klakow. 2022b.
MasakhaNER 2.0: Africa-centric transfer learning
for named entity recognition.
In Proceedings of
the 2022 Conference on Empirical Methods in Nat-
ural Language Processing, pages 4488–4508, Abu
Dhabi, United Arab Emirates. Association for Com-
putational Linguistics.
David Ifeoluwa Adelani, Jade Abbott, Graham Neu-
big, Daniel D’souza, Julia Kreutzer, Constantine Lig-
nos, Chester Palen-Michel, Happy Buzaaba, Shruti
Rijhwani, Sebastian Ruder, Stephen Mayhew, Is-
rael Abebe Azime, Shamsuddeen H. Muhammad,
Chris Chinenye Emezue, Joyce Nakatumba-Nabende,
Perez Ogayo, Aremu Anuoluwapo, Catherine Gitau,
Derguene Mbaye, Jesujoba Alabi, Seid Muhie Yi-
mam, Tajuddeen Rabiu Gwadabe, Ignatius Ezeani,
Rubungo Andre Niyongabo, Jonathan Mukiibi, Ver-
rah Otiende, Iroro Orife, Davis David, Samba Ngom,
Tosin Adewumi, Paul Rayson, Mofetoluwa Adeyemi,
Gerald Muriuki, Emmanuel Anebi, Chiamaka Chuk-
wuneke, Nkiruka Odu, Eric Peter Wairagala, Samuel
Oyerinde, Clemencia Siro, Tobius Saul Bateesa,
Temilola Oloyede, Yvonne Wambui, Victor Akin-
ode, Deborah Nabagereka, Maurice Katusiime, Ayo-
dele Awokoya, Mouhamadane MBOUP, Dibora Ge-
breyohannes, Henok Tilaye, Kelechi Nwaike, De-
gaga Wolde, Abdoulaye Faye, Blessing Sibanda, Ore-
vaoghene Ahia, Bonaventure F. P. Dossou, Kelechi
Ogueji, Thierno Ibrahima DIOP, Abdoulaye Diallo,
Adewale Akinfaderin, Tendai Marengereke, and Sa-
lomey Osei. 2021.
MasakhaNER: Named entity
recognition for African languages.
Transactions

--- Page 11 ---

of the Association for Computational Linguistics,
9:1116–1131.
David Ifeoluwa Adelani, Marek Masiak, Israel Abebe
Azime, Jesujoba Oluwadara Alabi, Atnafu Lam-
bebo Tonja, Christine Mwase, Odunayo Ogun-
depo,
Bonaventure
F.
P.
Dossou,
Akintunde
Oladipo, Doreen Nixdorf, Chris Chinenye Emezue,
Sana Sabah al azzawi,
Blessing K. Sibanda,
Davis David, Lolwethu Ndolela, Jonathan Mukiibi,
Tunde Oluwaseyi Ajayi, Tatiana Moteu Ngoli, Brian
Odhiambo, Abraham Toluwase Owodunni, Nnae-
meka C. Obiefuna, Shamsuddeen Hassan Muham-
mad, Saheed Salahudeen Abdullahi, Mesay Gemeda
Yigezu, Tajuddeen Gwadabe, Idris Abdulmumin,
Mahlet Taye Bame, Oluwabusayo Olufunke Awoy-
omi, Iyanuoluwa Shode, Tolulope Anu Adelani,
Habiba Abdulganiy Kailani, Abdul-Hakeem Omo-
tayo, Adetola Adeeko, Afolabi Abeeb, Anuoluwapo
Aremu, Olanrewaju Samuel, Clemencia Siro, Wan-
gari Kimotho, Onyekachi Raphael Ogbu, Chinedu E.
Mbonu, Chiamaka I. Chukwuneke, Samuel Fanijo,
Jessica Ojo, Oyinkansola F. Awosan, Tadesse Kebede
Guge, Sakayo Toadoum Sari, Pamela Nyatsine,
Freedmore Sidume, Oreen Yousuf, Mardiyyah Odu-
wole, Ussen Kimanuka, Kanda Patrick Tshinu, Thina
Diko, Siyanda Nxakama, Abdulmejid Tuni Johar,
Sinodos Gebre, Muhidin Mohamed, Shafie Abdi
Mohamed, Fuad Mire Hassan, Moges Ahmed
Mehamed, Evrard Ngabire, and Pontus Stenetorp.
2023. Masakhanews: News topic classification for
african languages.
Jesujoba O. Alabi, David Ifeoluwa Adelani, Marius
Mosbach, and Dietrich Klakow. 2022. Adapting pre-
trained language models to African languages via
multilingual adaptive fine-tuning. In Proceedings of
the 29th International Conference on Computational
Linguistics, pages 4336–4349, Gyeongju, Republic
of Korea. International Committee on Computational
Linguistics.
Alan Ansell, Edoardo Ponti, Anna Korhonen, and Ivan
Vuli´c. 2022. Composable sparse fine-tuning for cross-
lingual transfer. In Proceedings of the 60th Annual
Meeting of the Association for Computational Lin-
guistics (Volume 1: Long Papers), pages 1778–1796,
Dublin, Ireland. Association for Computational Lin-
guistics.
Ekaterina Aplonova and Francis Tyers. 2017. Towards
a dependency-annotated treebank for bambara. In
Proceedings of the 16th International Workshop on
Treebanks and Linguistic Theories, pages 138–145.
Mikel Artetxe, Sebastian Ruder, and Dani Yogatama.
2020. On the cross-lingual transferability of mono-
lingual representations. In Proceedings of the 58th
Annual Meeting of the Association for Computational
Linguistics, pages 4623–4637, Online. Association
for Computational Linguistics.
Cheikh Anta Babou and Michele Loporcaro. 2016.
Noun classes and grammatical gender in wolof. Jour-
nal of African Languages and Linguistics, 37(1):1–
57.
Adams Bodomo and Charles Marfo. 2002. The mor-
phophonology of noun classes in dagaare and akan.
Joan Bresnan and Sam A Mchombo. 1987. Topic, pro-
noun, and agreement in chiche ˆwa. Language, pages
741–782.
Ronald Cardenas, Ying Lin, Heng Ji, and Jonathan May.
2019. A grounded unsupervised universal part-of-
speech tagger for low-resource languages.
arXiv
preprint arXiv:1904.05426.
Emmanuel Chabata. 2000. The shona corpus and the
problem of tagging. Lexikos, 10(10):76–85.
Hyung Won Chung, Thibault Fevry, Henry Tsai, Melvin
Johnson, and Sebastian Ruder. 2021. Rethinking em-
bedding coupling in pre-trained language models. In
International Conference on Learning Representa-
tions.
Alexis Conneau, Kartikay Khandelwal, Naman Goyal,
Vishrav Chaudhary, Guillaume Wenzek, Francisco
Guzmán, Edouard Grave, Myle Ott, Luke Zettle-
moyer, and Veselin Stoyanov. 2020. Unsupervised
cross-lingual representation learning at scale. In Pro-
ceedings of the 58th Annual Meeting of the Asso-
ciation for Computational Linguistics, pages 8440–
8451, Online. Association for Computational Lin-
guistics.
Guy De Pauw, Naomi Maajabu, and Peter Waiganjo
Wagacha. 2010.
A knowledge-light approach to
luo machine translation and part-of-speech tagging.
In Proceedings of the Second Workshop on African
Language Technology (AfLaT 2010). Valletta, Malta:
European Language Resources Association (ELRA),
pages 15–20.
Wietse de Vries, Martijn Wieling, and Malvina Nissim.
2022. Make the best of cross-lingual transfer: Ev-
idence from POS tagging with over 100 languages.
In Proceedings of the 60th Annual Meeting of the
Association for Computational Linguistics (Volume
1: Long Papers), pages 7676–7685, Dublin, Ireland.
Association for Computational Linguistics.
Xolani Delman. 2016. Development of Part-of-speech
Tagger for Xhosa. Ph.D. thesis, University of Fort
Hare.
Jacob Devlin, Ming-Wei Chang, Kenton Lee, and
Kristina Toutanova. 2019. BERT: Pre-training of
deep bidirectional transformers for language under-
standing. In Proceedings of the 2019 Conference of
the North American Chapter of the Association for
Computational Linguistics: Human Language Tech-
nologies, Volume 1 (Long and Short Papers), pages
4171–4186, Minneapolis, Minnesota. Association for
Computational Linguistics.
Cheikh M Bamba Dione. 2019. Developing universal
dependencies for wolof. In Proceedings of the Third
Workshop on Universal Dependencies (UDW, Syn-
taxFest 2019), pages 12–23.

--- Page 12 ---

Cheikh M Bamba Dione, Jonas Kuhn, and Sina Zarrieß.
2010. Design and development of part-of-speech-
tagging resources for wolof (niger-congo, spoken in
senegal). In Proceedings of the Seventh International
Conference on Language Resources and Evaluation
(LREC’10).
Bonaventure F. P. Dossou, Atnafu Lambebo Tonja,
Oreen Yousuf, Salomey Osei, Abigail Oppong, Iyan-
uoluwa Shode, Oluwabusayo Olufunke Awoyomi,
and Chris C. Emezue. 2022.
Afrolm:
A self-
active learning-based multilingual pretrained lan-
guage model for 23 african languages.
ArXiv,
abs/2211.03263.
Tom Güldemann. 2008. Quotative Indexes in African
Languages. A Synchronic and Diachronic Survey. De
Gruyter Mouton, Berlin, New York.
Neil Houlsby, Andrei Giurgiu, Stanislaw Jastrzebski,
Bruna Morrone, Quentin De Laroussilhe, Andrea
Gesmundo, Mona Attariyan, and Sylvain Gelly. 2019.
Parameter-efficient transfer learning for NLP.
In
Proceedings of the 36th International Conference
on Machine Learning, volume 97 of Proceedings
of Machine Learning Research, pages 2790–2799.
PMLR.
Olájídé Ishola and Daniel Zeman. 2020. Yorùbá de-
pendency treebank (YTB). In Proceedings of the
12th Language Resources and Evaluation Confer-
ence, pages 5178–5186, Marseille, France. European
Language Resources Association.
Mariya Koleva. 2013. Towards adaptation of nlp tools
for closely-related bantu languages: Building a part-
of-speech tagger for zulu. Master’s thesis, Saarland
University, Germany.
Adenike Lawal. 1991.
Yoruba pe and ki verbs or
complementizers.
Studies in African Linguistics,
22(1):74–84.
Yu-Hsiang Lin, Chian-Yu Chen, Jean Lee, Zirui Li,
Yuyan Zhang, Mengzhou Xia, Shruti Rijhwani, Junx-
ian He, Zhisong Zhang, Xuezhe Ma, Antonios Anas-
tasopoulos, Patrick Littell, and Graham Neubig. 2019.
Choosing transfer languages for cross-lingual learn-
ing. In Proceedings of the 57th Annual Meeting of
the Association for Computational Linguistics, pages
3125–3135, Florence, Italy. Association for Compu-
tational Linguistics.
Gabofetswe Malema, Boago Okgetheng, and Moffat
Motlhanka. 2017. Setswana part of speech tagging.
International Journal on Natural Language Comput-
ing, 6(6):15–20.
Gabofetswe Malema, Boago Okgetheng, Bopaki Tebalo,
Moffat Motlhanka, and Goaletsa Rammidi. 2020.
Complex setswana parts of speech tagging. In Pro-
ceedings of the first workshop on Resources for
African Indigenous Languages, pages 21–24.
Fiona McLaughlin. 2004. Is there an adjective class in
wolof. Adjective classes: A cross-linguistic typology,
1:242–262.
Josh Meyer, David Adelani, Edresson Casanova, Alp
Öktem, Daniel Whitenack, Julian Weber, Salomon
KABONGO KABENAMUALU, Elizabeth Salesky,
Iroro Orife, Colin Leong, Perez Ogayo, Chris Chi-
nenye Emezue, Jonathan Mukiibi, Salomey Osei,
Apelete AGBOLO, Victor Akinode, Bernard Opoku,
Olanrewaju Samuel, Jesujoba Alabi, and Shamsud-
deen Hassan Muhammad. 2022. BibleTTS: a large,
high-fidelity, multilingual, and uniquely African
speech corpus. In Proc. Interspeech 2022, pages
2383–2387.
Shamsuddeen Hassan Muhammad, Idris Abdulmumin,
Abinew Ali Ayele, Nedjma Ousidhoum, David Ife-
oluwa Adelani, Seid Muhie Yimam, Ibrahim Sa’id
Ahmad, Meriem Beloucif, Saif Mohammad, Sebas-
tian Ruder, et al. 2023. Afrisenti: A twitter sentiment
analysis benchmark for african languages.
arXiv
preprint arXiv:2302.08956.
Shamsuddeen Hassan Muhammad, David Ifeoluwa Ade-
lani, Sebastian Ruder, Ibrahim Sa’id Ahmad, Idris
Abdulmumin, Bello Shehu Bello, Monojit Choud-
hury, Chris Chinenye Emezue, Saheed Salahudeen
Abdullahi, Anuoluwapo Aremu, Alípio Jorge, and
Pavel Brazdil. 2022. NaijaSenti: A Nigerian Twitter
sentiment corpus for multilingual sentiment analy-
sis. In Proceedings of the Thirteenth Language Re-
sources and Evaluation Conference, pages 590–602,
Marseille, France. European Language Resources
Association.
Joakim Nivre, Marie-Catherine De Marneffe, Filip Gin-
ter, Yoav Goldberg, Jan Hajic, Christopher D Man-
ning, Ryan McDonald, Slav Petrov, Sampo Pyysalo,
Natalia Silveira, et al. 2016. Universal dependencies
v1: A multilingual treebank collection. In Proceed-
ings of the Tenth International Conference on Lan-
guage Resources and Evaluation (LREC’16), pages
1659–1666.
Rubungo Andre Niyongabo, Qu Hong, Julia Kreutzer,
and Li Huang. 2020. KINNEWS and KIRNEWS:
Benchmarking cross-lingual text classification for
Kinyarwanda and Kirundi. In Proceedings of the
28th International Conference on Computational Lin-
guistics, pages 5507–5521, Barcelona, Spain (On-
line). International Committee on Computational Lin-
guistics.
NLLB-Team, Marta Ruiz Costa-jussà, James Cross,
Onur cCelebi, Maha Elbayad, Kenneth Heafield,
Kevin Heffernan, Elahe Kalbassi, Janice Lam,
Daniel Licht, Jean Maillard, Anna Sun, Skyler
Wang, Guillaume Wenzek, Alison Youngblood,
Bapi Akula, Loïc Barrault, Gabriel Mejia Gonza-
lez, Prangthip Hansanti, John Hoffman, Semarley
Jarrett, Kaushik Ram Sadagopan, Dirk Rowe, Shan-
non L. Spruit, C. Tran, Pierre Andrews, Necip Fazil
Ayan, Shruti Bhosale, Sergey Edunov, Angela Fan,
Cynthia Gao, Vedanuj Goswami, Francisco Guzm’an,
Philipp Koehn, Alexandre Mourachko, Christophe
Ropers, Safiyyah Saleem, Holger Schwenk, and

--- Page 13 ---

Jeff Wang. 2022. No language left behind: Scal-
ing human-centered machine translation.
ArXiv,
abs/2207.04672.
Derek Nurse and Gerard Philippson, editors. 2006. The
Bantu Languages. Routledge Language Family Se-
ries. Routledge, London, England.
Perez Ogayo, Graham Neubig, and Alan W Black. 2022.
Building African Voices. In Proc. Interspeech 2022,
pages 1263–1267.
Kelechi Ogueji, Yuxin Zhu, and Jimmy Lin. 2021.
Small data? no problem! exploring the viability
of pretrained multilingual language models for low-
resourced languages. In Proceedings of the 1st Work-
shop on Multilingual Representation Learning, pages
116–126, Punta Cana, Dominican Republic. Associa-
tion for Computational Linguistics.
Ikechukwu E Onyenwe, Chinedu Uchechukwu, and
Mark Hepple. 2014. Part-of-speech tagset and cor-
pus development for igbo, an african. In Proceedings
of LAW VIII-The 8th Linguistic Annotation Workshop,
pages 93–98. Association for Computational Linguis-
tics and Dublin City University.
Olasope O Oyelaran. 1982. On the scope of the se-
rial verb construction in yoruba. Studies in African
Linguistics, 13(2):109.
Chester Palen-Michel, June Kim, and Constantine Lig-
nos. 2022. Multilingual open text release 1: Public
domain news in 44 languages. In Proceedings of
the Thirteenth Language Resources and Evaluation
Conference, pages 2080–2089, Marseille, France. Eu-
ropean Language Resources Association.
Doris L. Payne, Sara Pacchiarotti, and Mokaya Bosire,
editors. 2017. Diversity in African languages. Num-
ber 1 in Contemporary African Linguistics. Language
Science Press, Berlin.
Slav Petrov, Dipanjan Das, and Ryan McDonald. 2012.
A universal part-of-speech tagset. In Proceedings
of the Eighth International Conference on Language
Resources and Evaluation (LREC’12), pages 2089–
2096, Istanbul, Turkey. European Language Re-
sources Association (ELRA).
Jonas Pfeiffer, Ivan Vuli´c, Iryna Gurevych, and Se-
bastian Ruder. 2020. MAD-X: An Adapter-Based
Framework for Multi-Task Cross-Lingual Transfer.
In Proceedings of the 2020 Conference on Empirical
Methods in Natural Language Processing (EMNLP),
pages 7654–7673, Online. Association for Computa-
tional Linguistics.
Jonas Pfeiffer, Ivan Vuli´c, Iryna Gurevych, and Sebas-
tian Ruder. 2021. UNKs everywhere: Adapting mul-
tilingual language models to new scripts. In Proceed-
ings of the 2021 Conference on Empirical Methods in
Natural Language Processing, pages 10186–10203,
Online and Punta Cana, Dominican Republic. Asso-
ciation for Computational Linguistics.
Edoardo Maria Ponti, Goran Glavaš, Olga Majewska,
Qianchu Liu, Ivan Vuli´c, and Anna Korhonen. 2020.
XCOPA: A multilingual dataset for causal common-
sense reasoning. In Proceedings of the 2020 Con-
ference on Empirical Methods in Natural Language
Processing (EMNLP), pages 2362–2376, Online. As-
sociation for Computational Linguistics.
Sandy Ritchie, You-Chi Cheng, Mingqing Chen, Ra-
jiv Mathews, Daan van Esch, Bo Li, and Khe Chai
Sim. 2022. Large vocabulary speech recognition
for languages of africa: multilingual modeling and
self-supervised learning. ArXiv, abs/2208.03067.
Adedjouma A. Sèmiyou,
John OR Aoga,
and
Mamoud A Igue. 2012. Part-of-speech tagging of
yoruba standard, language of niger-congo family. Re-
search Journal of Computer and Information Tech-
nology Sciences, 1:2–5.
Kathleen Siminyu, Godson Kalipe, Davor Orlic, Jade Z.
Abbott, Vukosi Marivate, Sackey Freshia, Prateek
Sibal, Bhanu Bhakta Neupane, David Ifeoluwa
Adelani, Amelia Taylor, Jamiil Toure Ali, Kevin
Degila, Momboladji Balogoun, Thierno Ibrahima
Diop, Davis David, Chayma Fourati, Hatem Had-
dad, and Malek Naski. 2021. Ai4d - african language
program. ArXiv, abs/2104.02516.
Aminu Tukur, Kabir Umar, and SAS Muhammad. 2020.
Parts-of-speech tagging of hausa-based texts using
hidden markov model. vol, 6:303–313.
Valentin Vydrin. 2018. Where corpus methods hit their
limits: the case of separable adjectives in bambara.
Rhema, (4):34–48.
Wm E Welmers. 2018. African language structures.
University of California Press.
Thomas Wolf, Lysandre Debut, Victor Sanh, Julien
Chaumond, Clement Delangue, Anthony Moi, Pier-
ric Cistac, Tim Rault, Remi Louf, Morgan Funtow-
icz, Joe Davison, Sam Shleifer, Patrick von Platen,
Clara Ma, Yacine Jernite, Julien Plu, Canwen Xu,
Teven Le Scao, Sylvain Gugger, Mariama Drame,
Quentin Lhoest, and Alexander Rush. 2020. Trans-
formers: State-of-the-art natural language processing.
In Proceedings of the 2020 Conference on Empirical
Methods in Natural Language Processing: System
Demonstrations, pages 38–45, Online. Association
for Computational Linguistics.
A
Language Characteristics
Table 5 provides the details about the language
characteristics.
B
Annotation Agreement
Table 6 provides POS annotation agreements at the
sentence level for 13 out of the 20 focus languages.

--- Page 14 ---

No. of
Latin Letters
Morphological
Inflectional
Noun
Language
Letters
Omitted
Letters added
Tonality
diacritics
Word Order
typology
Morphology (WALS)
Classes
Bambara (bam)
27
q,v,x
E, O, ñ, N
yes, 2 tones
yes
SVO & SOV
isolating
strong suffixing
absent
Ghomálá’ (bbj)
40
q, w, x, y
bv, dz, @, a@, E, gh, ny, nt, N, Nk, O, pf,
mpf, sh, ts, 0, zh, ’
yes, 5 tones
yes
SVO
agglutinative
strong prefixing
active, 6
Éwé (ewe)
35
c, j, q
ã, dz, E, ƒ, gb, G, kp, ny, N, O, ts, V
yes, 3 tones
yes
SVO
isolating
equal prefixing and suffixing
vestigial
Fon (fon)
33
q
ã, E,gb, hw, kp, ny, O, xw
yes, 3 tones
yes
SVO
isolating
little affixation
vestigial
Hausa (hau)
44
p,q,v,x
á, â, Î, ¯, kw, Îw, gw, ky, Îy, gy, sh, ts
yes, 2 tones
no
SVO
agglutinative
little affixation
absent
Igbo (ibo)
34
c, q, x
ch, gb, gh, gw, kp, kw, nw, ny, o., ˙o, sh, u.
yes, 2 tones
yes
SVO
agglutinative
little affixation
vestigial
Kinyarwanda (kin)
30
q, x
cy, jy, nk, nt, ny, sh
yes, 2 tones
no
SVO
agglutinative
strong prefixing
active, 16
Luganda (lug)
25
h, q, x
N, ny
yes, 3 tones
no
SVO
agglutinative
strong prefixing
active, 20
Luo (luo)
31
c, q, x, v, z
ch, dh, mb, nd, ng’, ng, ny, nj, th, sh
yes, 4 tones
no
SVO
agglutinative
equal prefixing and suffixing
absent
Mossi (mos)
26
c, j, q, x
’, E, Ì, V
yes, 2 tones
yes
SVO
isolating
strongly suffixing
active, 11
Chichewa (nya)
31
q, x, y
ch, kh, ng, N, ph, tch, th, ˆw
yes, 2 tones
no
SVO
agglutinative
strong prefixing
active, 17
Naija (pcm)
26
–
–
no
no
SVO
mostly analytic
strongly suffixing
absent
chiShona (sna)
29
c, l, q, x
bh, ch, dh, nh, sh, vh, zh
yes, 2 tones
no
SVO
agglutinative
strong prefixing
active, 20
Swahili (swa)
33
x, q
ch, dh, gh, kh, ng’, ny, sh, th, ts
no
yes
SVO
agglutinative
strong suffixing
active, 18
Setswana (tsn)
36
c, q, v, x, z
ê, kg, kh, ng, ny, ô, ph, š, th, tl, tlh, ts,
tsh, tš, tšh
yes, 2 tones
no
SVO
agglutinative
strong prefixing
active, 18
Akan/Twi (twi)
22
c,j,q,v,x,z
E, O
yes, 5 tones
no
SVO
isolating
strong prefixing
active, 6
Wolof (wol)
29
h,v,z
N, à, é, ë, ó, ñ
no
yes
SVO
agglutinative
strong suffixing
active, 10
isiXhosa (xho)
68
–
bh, ch, dl, dy, dz, gc, gq, gr, gx, hh, hl,
kh, kr, lh, mh, ng, ngc, ngh, ngq, ngx,
nkq, nkx, nh, nkc, nx, ny, nyh, ph, qh,
rh, sh, th, ths, thsh, ts, tsh, ty, tyh, wh,
xh, yh, zh
yes, 2 tones
no
SVO
agglutinative
strong prefixing
active, 17
Yorùbá (yor)
25
c, q, v, x, z
e., gb, s. , o.
yes, 3 tones
yes
SVO
isolating
little affixation
vestigial, 2
isiZulu (zul)
55
–
nx, ts, nq, ph, hh, ny, gq, hl, bh, nj, ch,
ngc, ngq, th, ngx, kl, ntsh, sh, kh, tsh,
ng, nk, gx, xh, gc, mb, dl, nc, qh
yes, 3 tones
no
SVO
agglutinative
strong prefixing
active, 17
Table 5: Linguistic Characteristics of the Languages
No. agreed
agreed
No. agreed
agreed
Lang.
annotation
annotation (%)
Lang.
annotation
annotation (%)
bam
1,091
77.9
pcm
1,073
76.6
ewe
616
44.0
tsn
1,058
24.4
hau
1,079
77.1
twi
1,306
93.2
kin
1,127
80.5
xho
1,378
98.4
lug
937
66.9
yor
1,059
75.6
luo
564
40.3
zul
905
64.6
mos
829
49.2
Table 6: Number of sentences with agreed annotations and their percentages
Language
Data Source
# Train/# dev/ # test
Afrikaans (afr)
UD_Afrikaans-AfriBooms
1,315/ 194/ 425
Arabic (ara)
UD_Arabic-PADT
6,075/ 909/ 680
English (eng)
UD_English-EWT
12,544/ 2001/ 2077
French (fra)
UD_French-GSD
14,450/ 1,476/ 416
Naija (pcm)
UD_Naija-NSC
7,279/ 991/ 972
Romanian (ron)
UD_Romanian-RRT
8,043/ 752/ 729
Wolof (wol)
UD_Wolof-WTB
1,188/ 449/ 470
Table 7: Data Splits for UD POS datasets used as
source languages for cross-lingual transfer.
C
UD POS data split
Table 7 provides the UD POS corpus found online
that we make use for determining the best transfer
languages
D
Hyper-parameters for Experiments
Hyper-parameters for Baseline Models
The
PLMs were trained for 20 epochs with a learning
rate of 5e-5 using huggingface transformers (Wolf
et al., 2020). We make use of a batch size of 16
Hyper-parameters for adapters
We train the
task adapter using the following hyper-parameters:
batch size of 8, 20 epochs, “pfeiffer” adapter con-
fig, adapter reduction factor of 4 (except for Wolof,
where we make use of adapter reduction factor of
1), and learning rate of 5e-5. For the language
adapters, we make use of 100 epochs or maxi-
mum steps of 100K, minimum number of steps
is 30K, batch size of 8, “pfeiffer+inv” adapter con-
fig, adapter reduction factor of 2, learning rate of
5e-5, and maximum sequence length of 256.
Hyper-parameters for LT-SFT
We make use of
the default setting used by the Ansell et al. (2022)
paper.
E
Monolingual data for Adapter/SFTs
language adaptation
Table 8 provides the UD POS corpus found online
that we make use for determining the best transfer
languages
F
MAD-X multi-source fine-tuning
Figure 2 provides the result of MAD-X with dif-
ferent source languages, and multi-source fine-
tuning using either eng, ron or wol as language
adapter for task adaptation prior to zero-shot trans-
fer. Our result shows that making of wol as lan-

--- Page 15 ---

Language
Source
Size (MB)
Bambara (bam)
MAFAND-MT (Adelani et al., 2022a)
0.8MB
Ghomálá’ (bbj)
MAFAND-MT (Adelani et al., 2022a)
0.4MB
Éwé (ewe)
MAFAND-MT (Adelani et al., 2022a)
0.5MB
Fon (fon)
MAFAND-MT (Adelani et al., 2022a)
1.0MB
Hausa (hau)
VOA (Palen-Michel et al., 2022)
46.1MB
Igbo (ibo)
BBC Igbo (Ogueji et al., 2021)
16.6MB
Kinyarwanda (kin)
KINNEWS (Niyongabo et al., 2020)
35.8MB
Luganda (lug)
Bukedde (Alabi et al., 2022)
7.9MB
Luo (luo)
Ramogi FM news (Adelani et al., 2021) and MAFAND-MT (Adelani et al., 2022a)
1.4MB
Mossi (mos)
MAFAND-MT (Adelani et al., 2022a)
0.7MB
Naija (pcm)
BBC (Alabi et al., 2022)
50.2MB
Chichewa (nya)
Nation Online Malawi (Siminyu et al., 2021)
4.5MB
chiShona (sna)
VOA (Palen-Michel et al., 2022)
28.5MB
Kiswahili (swa)
VOA (Palen-Michel et al., 2022)
17.1MB
Setswana (tsn)
Daily News (Adelani et al., 2021), MAFAND-MT (Adelani et al., 2022a)
1.9MB
Twi (twi)
MAFAND-MT (Adelani et al., 2022a)
0.8KB
Wolof (wol)
Lu Defu Waxu, Saabal, Wolof Online, and MAFAND-MT (Adelani et al., 2022a)
2.3MB
isiXhosa (xho)
Isolezwe Newspaper
17.3MB
Yorùbá (yor)
BBC Yorùbá (Alabi et al., 2022)
15.0MB
isiZulu (zul)
Isolezwe Newspaper
34.3MB
Romanian (ron)
Wikipedia
500MB
French (fra)
Wikipedia (a subset)
500MB
Table 8: Monolingual News Corpora used for language adapter and SFT training, and their sources and size (MB)
bam
bbj
ewe
fon
hau
ibo
kin
lug
luo
mos
nya
pcm
sna
swa
tsn
twi
wol
xho
yor
zul
ave
ave*
TARGET LANGUAGE
afr
ara
eng
fra
pcm
ron
wol
eng-ron-wol (wo)
eng-ron-wol (en)
eng-ron-wol (ro)
wol_news
SOURCE LANGUAGE
61
55
64
52
64
74
63
56
68
66
61
80
60
58
53
52
76
40
66
41
60
58
41
32
46
43
48
53
53
50
58
46
51
67
54
62
39
35
52
39
50
43
48
47
66
58
67
54
67
77
71
68
76
72
69
83
71
63
54
52
75
58
66
62
66
65
63
56
66
58
68
79
71
66
73
68
71
83
72
66
52
48
78
47
69
51
65
64
46
44
52
37
58
68
54
60
60
54
59
76
60
54
44
35
58
33
53
40
52
51
64
62
68
59
65
78
72
61
75
68
65
83
70
64
62
54
78
47
70
56
66
64
62
63
70
66
67
78
63
65
73
72
62
77
70
54
52
56
91
43
70
45
65
63
66
65
70
62
69
82
71
68
74
72
69
84
72
62
52
58
90
52
70
56
68
66
62
61
69
61
70
82
72
70
75
72
68
84
71
63
58
58
87
53
72
58
68
66
65
63
71
62
70
81
70
62
75
73
65
85
69
63
60
58
88
46
72
51
67
65
47
42
47
38
54
52
41
39
46
44
38
40
44
39
45
40
86
39
46
36
45
43
Heat Map of MAD-X Transfer Accuracy
40
50
60
70
80
90
Figure 2: MAD-X: Cross-lingual Experiments on MasakhaPOS . Zero-shot Evaluation using afr, ara, eng,
fra, ron, pcm and wol as source languages. Experiments based on AfroXLMR-base. ave* excludes pcm and
wol from the average since they are also source languages.
guage adapters leads to slightly better accuracy
(69.1%) over eng (68.7%) and ron (67.8%). But
in general, either one can be used, and they all give
an impressive performance over LT-SFT, as shown
in Table 9.
G
Cross-lingual transfer from all source
languages
Table 9 shows the result of cross-lingual transfer
from each source language (afr, ara, eng, fra,
pcm, ron, and wol) to each of the African lan-
guages. We extended the evaluation to include
sna (since it was recommended as the best transfer
language for a related task – named entity recogni-
tion by (Adelani et al., 2022b)) by using the newly
created POS corpus. We also tried other Bantu lan-
guages like kin and swa, but their performance
was worse than sna. Our evaluation shows that
sna results in better transfer to Bantu languages be-
cause of it’s rich morphology. We achieved the best
result for all languages using multi-source transfer
from (eng, ron, wol, sna) languages.

--- Page 16 ---

Method
bam
bbj
ewe
fon
hau
ibo
kin
lug
luo
mos
nya
pcm
sna
swa
tsn
twi
wol
xho
yor
zul
AVG
AVG*
ara as a source language
FT-Eval
26.4
10.0
16.0
14.2
47.7
62.5
57.1
35.4
15.3
17.0
53.7
66.4
56.0
58.4
42.9
14.1
13.5
39.0
46.9
44.8
36.9
37.1
LT-SFT
41.0
30.7
41.2
45.0
47.3
62.9
54.0
48.7
56.2
43.2
54.4
63.3
53.6
59.4
44.8
39.9
51.0
36.8
50.6
44.8
48.4
48.0
MAD-X
44.5
36.5
50.9
45.9
48.5
59.5
55.5
51.1
60.5
46.7
53.4
66.8
53.8
59.1
40.4
37.9
52.3
40.3
52.3
44.6
50.0
49.7
pcm as a source language
FT-Eval
16.0
8.6
14.3
4.9
58.0
64.9
48.9
35.9
13.0
11.0
47.5
74.6
51.9
50.9
32.8
5.3
7.3
25.9
46.9
30.9
32.8
33.2
LT-SFT
44.4
39.4
51.1
38.1
59.2
66.6
47.9
53.5
61.3
52.3
49.3
75.3
48.9
50.6
40.8
35.3
63.9
25.1
58.3
30.6
49.6
48.8
MAD-X
42.1
43.6
53.5
39.4
57.3
68.2
55.7
58.1
60.1
51.9
59.6
75.8
57.5
55.7
44.8
36.9
58.9
32.9
57.1
40.6
52.5
51.8
afr as a source language
FT-Eval
54.8
25.4
38.3
31.3
61.4
73.6
67.1
48.6
29.4
35.2
56.1
77.3
56.0
57.5
49.0
32.9
32.5
43.8
63.8
44.3
48.9
49.4
LT-SFT
69.2
55.6
64.0
52.5
62.8
74.7
66.1
59.0
69.4
63.4
54.4
79.7
58.4
57.1
48.5
49.0
79.3
41.0
64.3
41.5
60.5
59.6
MAD-X
61.9
56.1
63.9
53.0
63.0
75.2
68.2
60.2
68.1
63.4
62.0
80.8
61.1
60.6
50.4
48.6
75.7
43.8
65.2
46.0
61.4
60.6
fra as a source language
FT-Eval
41.0
15.2
27.5
16.1
64.1
73.0
67.7
53.4
21.9
21.3
65.2
77.9
64.4
62.2
51.8
16.8
17.7
45.8
61.6
46.5
45.6
46.1
LT-SFT
60.6
52.2
63.3
60.2
63.9
75.6
63.4
57.6
69.0
65.2
66.4
79.7
63.0
61.2
52.4
48.6
78.3
43.9
64.7
44.3
61.7
60.7
MAD-X
62.0
57.9
64.2
59.4
66.9
78.7
71.3
64.1
74.0
67.7
70.2
83.4
68.6
65.4
53.0
48.1
78.3
46.0
67.8
50.2
64.9
63.9
eng as a source language
FT-Eval
52.1
31.9
47.8
32.5
67.1
74.5
63.9
57.8
38.4
45.3
59.0
82.1
63.7
56.9
52.6
35.9
35.9
45.9
63.3
48.8
52.6
52.9
LT-SFT
67.9
57.6
67.9
55.5
69.0
76.3
64.2
61.0
74.5
70.3
59.4
82.4
64.6
56.9
49.5
52.1
78.2
45.9
65.3
49.8
63.4
62.5
MAD-X
62.9
58.5
68.7
55.8
67.0
77.8
70.9
65.7
73.0
71.8
70.1
83.2
69.8
61.2
49.8
53.0
75.2
57.1
66.9
60.9
66.0
65.2
ron as a source language
FT-Eval
46.5
30.5
37.6
30.9
67.3
77.7
73.3
56.9
36.7
40.6
62.2
78.9
66.3
61.0
55.8
35.7
33.8
49.6
63.5
56.3
53.1
53.4
LT-SFT
60.6
57.0
64.9
60.4
67.5
77.4
68.2
58.5
70.2
67.9
58.2
78.1
64.6
59.7
57.4
55.7
81.9
46.3
64.8
51.2
63.5
62.4
MAD-X
63.5
62.2
66.6
61.8
66.5
80.0
73.5
62.7
76.5
71.8
66.0
83.7
71.1
64.5
61.2
53.5
79.5
48.6
69.5
57.8
67.0
66.1
wol as a source language
FT-Eval
40.8
36.5
39.8
37.4
55.1
58.6
49.2
51.8
35.1
44.9
49.0
51.6
53.8
42.9
45.0
38.4
88.6
46.0
52.5
45.5
48.1
45.6
LT-SFT (N)
64.4
64.3
69.8
63.0
67.0
79.7
63.7
64.0
74.1
72.2
56.5
72.7
67.7
53.0
51.3
56.2
92.5
46.0
69.8
47.7
64.8
63.1
MAD-X (N)
46.6
41.8
47.2
37.8
53.9
51.8
41.0
39.0
46.5
44.0
38.3
40.2
44.3
38.8
44.6
40.1
85.6
39.2
46.4
45.2
43.0
43.3
MAD-X (N+W)
61.7
63.6
68.9
63.1
66.8
77.0
67.8
69.1
73.7
71.3
63.2
75.1
68.9
55.8
50.7
54.9
90.4
49.6
70.0
51.7
65.7
64.1
sna as a source language
FT-Eval
42.6
26.2
41.7
29.5
60.5
68.2
73.7
75.0
42.2
34.9
69.3
65.7
89.2
63.4
48.9
33.3
35.8
59.5
59.2
67.9
54.3
53.4
LT-SFT
52.2
57.5
66.0
55.4
60.5
71.9
69.0
80.1
75.7
58.1
70.4
60.2
89.9
63.5
50.6
65.8
71.6
62.7
62.2
72.9
65.8
64.2
MAD-X
50.3
57.0
65.3
56.3
64.1
71.9
75.0
79.2
75.9
59.8
70.6
68.6
89.7
63.2
52.7
61.0
75.3
61.8
57.8
69.8
66.3
64.5
multi-source:
eng-ron-wol
FT-Eval
44.2
36.3
39.3
39.3
69.4
78.5
70.6
59.2
35.5
46.8
60.9
81.4
65.8
58.5
53.8
38.8
89.1
48.8
65.2
53.5
56.7
54.4
LT-SFT
67.4
64.6
70.0
64.2
70.4
81.1
68.7
63.9
76.4
73.9
58.8
83.0
69.6
57.3
52.7
57.2
93.1
45.8
69.8
48.3
66.8
65.2
MAD-X
66.2
65.5
70.3
64.9
69.1
82.3
73.1
68.0
75.1
74.2
69.2
83.9
69.4
62.6
53.6
55.2
90.1
52.3
70.8
59.4
68.8
67.5
multi-source:
eng-ron-wol-sna
FT-Eval
45.1
35.9
39.6
41.0
69.5
78.7
76.9
71.7
37.4
46.8
71.9
82.4
88.9
63.8
51.7
38.8
89.2
59.6
65.6
67.3
61.1
58.0
LT-SFT
66.7
64.7
68.5
65.1
71.0
81.2
75.3
80.2
79.3
73.5
73.6
83.6
89.1
64.3
51.1
60.9
93.2
61.8
69.1
70.2
72.1
70.0
MAD-X
59.0
64.3
70.9
64.3
69.8
82.5
76.9
80.9
78.8
70.1
74.2
85.1
89.1
65.7
55.0
60.7
86.5
60.7
71.0
69.6
71.8
70.0
Table 9: Cross-lingual transfer to MasakhaPOS . Zero-shot Evaluation using FT-Eval, LT-SFT, and MAD-X,
with ron, eng, wol and sna as source languages. Experiments are based on AfroXLMR-base. Non-Bantu
Niger-Congo languages highlighted with gray (except for Bambara that is often disputed as a different language
family — Mande) while those of Bantu Niger-Congo languages are highlighted with cyan . AVG* excludes sna
and wol from the average since they are source languages.

```
