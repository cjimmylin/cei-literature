---
title: "2023-Schwarting-The eBible Corpus Data and Model - PDF Extract"
source_pdf: "2023-Schwarting-The eBible Corpus Data and Model.pdf"
pages: 20
extracted_at: "2026-02-13T09:15:43.819121"
---

# PDF Extract: 2023-Schwarting-The eBible Corpus Data and Model

**Source PDF:** 2023-Schwarting-The eBible Corpus Data and Model.pdf
**Total Pages:** 20

---

## Content

```
--- Page 1 ---

The eBible Corpus: Data and Model Benchmarks for Bible Translation
for Low-Resource Languages
Vesa Åkerman
SIL International
7500 W. Camp Wisdom Rd.
Dallas, TX
David Baines
SIL International
7500 W. Camp Wisdom Rd.
Dallas, TX
Damien Daspit
SIL International
7500 W. Camp Wisdom Rd.
Dallas, TX
Ulf Hermjakob
University of Southern California
Information Sciences Institute
4676 Admiralty Way #1001
Marina del Rey, CA
Taeho Jang
Payap University Linguistics Department
Super-highway Chiang Mai – Lumpang Road
Amphur Muang, Chiang Mai, 50000 Thailand
Colin Leong
University of Dayton
300 College Park
Dayton, OH
Michael Martin
SIL International
7500 W. Camp Wisdom Rd.
Dallas, TX
michael_martin@sil.org
Joel Mathew
University of Southern California
Information Sciences Institute
4676 Admiralty Way #1001
Marina del Rey, CA
Jonathan Robie
Clear Bible
2990 Franklin Ave SW #8
Grandville, MI
Marcus Schwarting
University of Chicago
Department of Computer Science
5801 South Ellis Avenue
Chicago, IL
Abstract
Efﬁciently and accurately translating a corpus
into a low-resource language remains a chal-
lenge, regardless of the strategies employed,
whether manual, automated, or a combina-
tion of the two.
Many Christian organiza-
tions are dedicated to the task of translat-
ing the Holy Bible into languages that lack
a modern translation. Bible translation (BT)
work is currently underway for over 3000 ex-
tremely low resource languages.
We intro-
duce the eBible corpus: a dataset containing
1009 translations of portions of the Bible with
data in 833 different languages across 75 lan-
guage families.
In addition to a BT bench-
marking dataset, we introduce model perfor-
mance benchmarks built on the No Language
Left Behind (NLLB) neural machine transla-
tion (NMT) models. Finally, we describe sev-
eral problems speciﬁc to the domain of BT and
consider how the established data and model
benchmarks might be used for future transla-
tion efforts. For a BT task trained with NLLB,
Austronesian and Trans-New Guinea language
families achieve 35.1 and 31.6 BLEU scores
respectively, which spurs future innovations
for NMT for low-resource languages in Papua
New Guinea.
1
Introduction
There has been signiﬁcant progress recently to-
wards solving multiple problems in the ﬁeld of
natural language processing (NLP). Most of these
advances, however, are skewed towards languages
of wider communication (LWCs). Though there
is ongoing work in low resource languages, the
scarcity of training data and benchmarks for mean-
ingful comparison of proposed techniques in such
languages slow down the pace of research.
The Holy Bible has been translated to a very
large number of languages of the world with contin-
ued work to modernize multiple translations. His-
torically, BTs have been foundational to the stan-
dardizing and revitalization of language for various
communities. Therefore, this data has the potential
to be the starting point for NLP research in many
extremely low resource languages. It would espe-
cially be useful for benchmarking model perfor-
mance for NLP researchers working in the Biblical
domain against modern techniques. Though not
all translations are published under a permissive
license for reuse, eBible.org has curated more than
1000 translations in various formats that are unen-
cumbered. Yet there are domain speciﬁc nuances
and issues in the data format (Klassen, 2022), struc-
arXiv:2304.09919v1  [cs.CL]  19 Apr 2023

--- Page 2 ---

ture (versiﬁcation) and encoding that need careful
handling and have been observed by the authors as
an impedance to use the data efﬁciently for NLP.
In this work we tackle the problem of scarcity
of data and a model benchmark (for machine trans-
lation) in low resource languages by: Collect-
ing, parsing and cleaning 1009 translations from
eBible.org which have been automatically veriﬁed
to be under a permissive license. These are made
available as a verse(footnote on deﬁnition of verse)-
wise parallel corpus across 833 languages. Design-
ing domain relevant benchmarking tasks that take
into consideration the textual and stylistic varia-
tions in the content, having multiple related lan-
guages to a target language and the realities of the
progress of a BT project on the ground.
To our knowledge, this is the ﬁrst time such a
large unencumbered multilingual corpus and care-
fully designed benchmark has been released to the
NLP community. This work draws heavily from
our own experience and work with multiple recog-
nized BT teams, organizations and languages.
The following sections are organized so that we
ﬁrst brieﬂy review existing relevant work on de-
veloping large Bible corpora and low resource ma-
chine translation. We then detail the eBible corpus
and its statistics along with the steps we took to
parse and clean the data. We share our experimen-
tal setup for the benchmark and the models we used.
We then share the experiment results and discuss
ﬁndings to attract researchers to the issues faced in
BT. Finally, we propose multiple research direc-
tions for future work using this dataset and provide
concluding remarks.
2
Background
In this section we brieﬂy review previous efforts to
aggregate Biblical corpora. We then consider pre-
vious NLP-driven strategies for multilingual trans-
lation to such low-resource languages, including
those speciﬁc to BT tasks.
2.1
Previously Aggregated Data
The number of languages represented in Biblical
corpora has been rising steadily over the last few
decades. Resnik et. al. produced a parallel corpus
with 13 languages in 1999 (Resnik et al., 1999),
and by 2015 the corpus of Christodouloupoulos
et. al. contained Bibles spanning 100 languages
(Christodouloupoulos and Steedman, 2015). In
2020, McCarthy et. al. reported on an effort to
scrape and align Scriptures from various sources.
With over 1600 languages and 4000 unique transla-
tions represented it is most likely the largest Bibli-
cal corpus ever compiled, unfortunately this corpus
is not publicly available (McCarthy et al., 2020).
Other online archives of open-license partial and
full BTs exist, but have not been made available in
a format amenable to statistical or deep learning
driven translation tasks.
Outside of BT, the general problem of trans-
lating text into extremely low resource languages
remains a challenge, primarily due to a lack of
high-quality open-source data. Datasets such as
FLORES-101 (Goyal et al., 2022), SALT (Akera
et al., 2022) and AmericasNLI (Kann et al., 2022)
previously provided a starting point for model train-
ing.
With the release of NLLB also came the
FLORES-200 dataset (Costa-jussà et al., 2022),
which contains 3001 sentences sampled across 204
total languages. FLORES-200 provides a many-
to-many multilingual data benchmark which is the
largest to date.
2.2
Previous Translation Models
We deﬁne a translation task as follows. Suppose
we are given a passage which is readily available
in one or multiple source languages. Suppose we
also have a target language for which the passage
has not been previously translated. We deﬁne the
translation task for this passage as the creation
of a mapping between the source(s) and the tar-
get. In the case of BT, a mapping between pas-
sages is carried out by verse, but in the general
case this can be performed by sentence. The ﬁrst
non-classical machine translation models relied on
statistical machine translation (SMT), and include
alignment-based strategies (Dyer et al., 2013),
Markovian methods (Deng and Byrne, 2008), and
many other frequentist and Bayesian approaches
(Koehn, 2009). Of particular interest is the work
of (Wu et al., 2018), which employs an SMT ap-
proach on the Bible corpus compiled by (McCarthy
et al., 2020). NMT is a natural extension of SMT,
and utilizes a neural network architecture to train di-
rectly on source and target texts. Basic NMT imple-
mentations use an encoder and a decoder structure,
and may forgo the recurrence and attention mech-
anism characteristic of transformers. The Open-
NMT package provides a turnkey implementation
for ﬁne-tuning NMT models for speciﬁc translation
tasks (Klein et al., 2017).

--- Page 3 ---

Transformers designed for translation tasks can
be considered an extension of earlier NMT models
through the inclusion of recurrent layers and an
attention mechanism. Many transformer architec-
tures have been modiﬁed for translation, including
fairseq (Ott et al., 2019) and BERT (Zhu et al.,
2020). Of particular interest is the work of Lei-
des, which uses a fairseq architecture trained on
BTs across 50 different languages and available
for general-purpose BT tasks (Liedes, 2018). Fi-
nally, Meta’s NLLB model represents the current
state-of-the-art NMT transformer, trained on the
FLORES-200 dataset representing over 200 differ-
ent languages (Costa-jussà et al., 2022).
3
Methods
In this section we describe the content of the eBible
corpus and our pipeline for aggregating and prepro-
cessing BTs. We also present summary statistics
describing the contents of the eBible corpus. We
then detail several benchmark translation tasks we
performed across eight language families within
the corpus. Finally, we describe the model archi-
tectures and scoring methods by which we will
evaluate model translation performance.
3.1
The eBible Corpus
We gathered and aligned 1,009 Scripture transla-
tions in 833 languages from eBible.org which are
provided under a Creative Commons or similarly
permissive licenses. This includes 113 ﬁles un-
der Attribution ShareAlike (CC BY-SA), two ﬁles
under Attribution Non-Commercial (CC BY-NC),
106 ﬁles under Attribution No Derivs (CC BY-ND),
699 ﬁles under Attribution Non-Commercial No
Derivs (CC BY-NC-ND), and 84 ﬁles under Pub-
lic Domain. After downloading these Bibles, the
versiﬁcation scheme (Original, English, Russian
Orthodox, Russian Protestant, Septuagint, or Vul-
gate) for each Bible was inferred based on its con-
tent. The text of each verse was extracted and all
formatting, cross-references, footnotes, and other
markup was removed. The verse text was placed
into an extract ﬁle with a verse-per-line format with
41,899 lines per ﬁle; the placement of each verse
in the extract ﬁle was normalized to the Original
versiﬁcation scheme, allowing ready comparison
of verses across translations. A separate index ﬁle
(vref.txt) records the verse reference for each
line of all verse extract ﬁles. Verse ranges were
preserved by placing the verse range text on the
ﬁrst line of the range, and tagging subsequent lines
from the verse range with the <range> indicator in
the verse extract ﬁle. The corpus and code is openly
available (Baines et al., 2023a). Additional tools
used in this process include the SIL-NLP package
(Daspit, 2023) and the Wildebeest package (Herm-
jakob, 2023). Figure 1 shows the general format of
several extract ﬁles, designed to be easily ingested
for NLP analysis and machine translation tasks.
In order to reduce data fragmentation for NLP
tasks, we performed character-level cleaning on the
eBible corpus using the Wildebeest tool, making
3.3 million changes to 220 out of the 1,009 BTs, the
vast majority of which are not or barely perceptible
to the human reader.
Changes include bringing complex character se-
quences into conventional order (e.g. Devanagari
primary character, nukta, vowel sign), preferring
composed characters per Unicode standard; cor-
recting some look-alike characters, e.g. mapping
Latin A to Cyrillic
in Cyrillic-script text, or
mapping Latin l to Devanagari danda where ap-
propriate; character normalization, e.g. reversed
c to open o (
→); for one translation, map-
ping the replacement character
to open/close
double/single quotes; correcting some comma er-
rors (deleting spaces before a comma, adding a
space after a comma, removing duplicate com-
mas); decomposing some ligatures (e.g.
→ﬁ);
and more1. Slightly over half of these changes
were done fully automatically, using the Wilde-
beest Normalization script wb_normalize.py; the
remaining changes were made with an eBible spe-
ciﬁc script wb_bible_plus.py based on a man-
ual review using the Wildebeest Analysis script
wb_analysis.py.
Some issues raised by the
Wildebeest Analysis script have not been addressed,
such as private-use characters in two BTs (dwr-
dwrENT, gof-gofENT), and some residual wrong-
script characters that can’t readily be corrected au-
tomatically or semi-automatically.
The eBible corpus exhibits a wide diversity of
languages, as shown in Figure 2 and Figure 3.
Roughly a quarter of the translations are in lan-
guages spoken primarily in Papua New Guinea,
which is widely known as the most linguistically
diverse country in the world. Many translations are
1Wildebeest complex character order normalization gen-
erally matches the dominant forms of most original BTs and
other corpora; it is closest to Unicode’s NFC, but unlike NFC
follows conventional order. E.g., NFC order of the above
pattern is: Devanagari primary character, vowel sign, nukta.

--- Page 4 ---

Figure 1: Sample verse extract ﬁles (vref, English, French, German).
Figure 2: Count of BTs by language family.
in languages considered ultra-low-resource, and ad-
ditional texts in some languages may not be readily
available. A large portion of the BTs are partially
complete, as shown in Figure 4. Experts often start
with translating the New Testament (NT) before
proceeding to the Old Testament (OT), which is
reﬂected in the availability of full NT translations
versus full OT translations. A small number of
translations also include the Deuterocanon. These
are often translated last or not at all. While they
are included in the eBible corpus, we exclude them
from further analysis based on their overall spar-
sity.
Figure 3: Count of BTs by country.
Figure 4: Sorted count of available verses per transla-
tion, separated by OT, NT, and Deuterocanon (DT).

--- Page 5 ---

3.2
Benchmark Translation Tasks
In
addition
to
a
standard
benchmark
train/test/validation splitting of our paired-verse
corpora, we also benchmark model performance
based on more realistic translation approaches.
We chose several additional tasks motivated by
plausible trajectories taken by those seeking to
translate the Bible into a low-resource language.
For example, the progression of a translation
may begin with the Gospels, then certain epistles,
followed by portions of the Pentateuch, and so on.
In this fashion, we can train a model on content
obtained earlier in the translation progression,
then measure performance on content typically
translated later. Our translation tasks include:
• Randomized
cross-validation
(CV)
task.
Translation pairs are delimited by Bible
verses available in both source and target cor-
pora. Due to the small size of the transla-
tion corpora (relative to those normally em-
ployed for NMT), we do not use a standard
80%/10%/10% split. We instead set aside 250
randomly selected verses for testing and vali-
dation sets respectively, with the training set
being the remaining verses, and running a ﬁve-
fold CV for scoring. This task will represent
an upper bound for possible model transla-
tion performance, with other tasks likely to
perform worse overall.
• Gospel Translation task. Train a model on the
Gospel of Mark (MRK), test the model on the
Gospel of Matthew (MAT). We selected this
task because Mark is often the ﬁrst book to
be translated, with Matthew to follow. Some
sections of Mark are also found in Matthew,
however Mark is also a shorter book. For
three-letter Biblical book codes, readers are
directed to Appendix C.
• Epistles Translation task. Train a model on
the Gospels (MAT, MRK, LUK, JHN) and
Acts of the Apostles (ACT), test the model
on the ﬁve epistles (1TH, 2TH, 1TI, 2TI, TIT,
collectively abbreviated as 5T).
• NT Completion task. Train a model on the
entire NT except Romans (ROM) and Reve-
lation (REV), test the model on the books of
Romans (ROM) and Revelation (REV). Due
to their translation difﬁculty, these books are
often among the last books of the NT to be
translated.
• Early OT translation task.
Train a model
on the entire NT, test the model on selected
books of the OT (GEN, EXO, LEV, NUM,
DEU, RUT, PSA, JON, collectively abbrevi-
ated as Early OT). These books are often the
ﬁrst from the OT to be translated.
• Late OT translation task. Train a model on
the entire Bible excluding minor prophets, test
the model on OT minor prophets (HOS, JOL,
AMO, OBA, MIC, NAH, HAB, ZEP, HAG,
ZEC, MAL). These books were chosen as
books that are typically among the last to be
translated.
• Related Language task.
Train a model to
translate from the source language into the
target language and into a related language
using the same train/test splits used for the
Gospel Translation, Epistles Translation, and
NT Completion tasks. This task is intended to
explore the potential for improving translation
accuracy through the use of other completed
translations.
We focus on eight speciﬁc translation pairings
with a translation source and target, spanning
unique language families, as described in Table 1.
These translation pairings are selected to represent
countries and language families with a signiﬁcant
number of active BT projects and with reasonable
representation in the eBible corpus. Within each se-
lected language family, source and target language
translations were selected to simulate the work of
a BT team using a reference translation from a
national or gateway language as a guide for trans-
lating into their target language, with access to a
related language translation for further guidance. In
creating these source/target/related language trans-
lation pairings, the target language translation was
selected by identifying a language family branch
with multiple translations in the corpus, prefer-
ably from the same country or in close geographic
proximity (Collin, 2010). Preference was given to
branches containing more total languages, some
with translations and some without. Within this
branch, preference was given to languages with a
full BT, or with a NT and partial OT content. The
next step was identifying a translation from the
corpus in a national or gateway language to act as

--- Page 6 ---

the source language translation, with priority given
to more recent translations from these languages.
Symmetric hidden Markov model (HMM) word
alignment models were trained between each can-
didate national/gateway language translation and
a small group of candidate target language trans-
lations; the source/target translation pairing with
the highest overall word alignment score was then
chosen. Finally, symmetric HMM word alignment
models were trained between the target language
translation and the available related language trans-
lations from the language family branch. Generally,
the translation with the highest overall alignment
score was selected for the related language. How-
ever, in some cases a related language translation
with a particularly high alignment score was ex-
cluded, based on the assumption that it may have
been translated as an adaptation or using some
other less generalized translation methodology. De-
tailed information on each translation pairing is
available in Appendix C.
Our benchmarking tasks will be approached us-
ing four different models. First, we use a SMT
technique; namely, the “fast_align” package from
(Dyer et al., 2013) which uses a fast implementa-
tion IBM2 word alignment strategy. Second, we
perform training on the OpenNMT Transformer-
Base architecture from (Klein et al., 2017) with a
SentencePiece unigram tokenization. Next, we per-
form ﬁne-tuning on the “No Language Left Behind”
(NLLB) model architecture from Meta (Costa-jussà
et al., 2022), both the small version consisting
of 600 million tunable parameters (NLLB-600M)
and the medium distilled version consisting of 1.3
billion tunable parameters (NLLB-1.3B-distilled),
which have pre-trained weights available from Hug-
gingFace.
We scored models across translation tasks us-
ing three different metrics: BLEU (Papineni et al.,
2002), Sentence Piece BLEU (spBLEU) (Goyal
et al., 2022), character 3-gram F-score (chrF3)
(Popovi´c, 2015). While BLEU and spBLEU scores
are correlated to some extent, spBLEU more read-
ily accounts for language variations in scripting
and agglutination. Models were trained with an
early stopping criteria of +0.1 BLEU over four
checkpoints (1000 steps per checkpoint). Mod-
els used a batch size of 16 with four gradient ac-
cumulation steps, 4000 warm-up steps, and label
smoothing of 0.2. For languages unknown to the
NLLB tokenizer, we added a new language code
as a special token to the tokenizer. All models
were trained and evaluated on an NVIDIA A-100
with 40 GB of available VRAM. This hardware
is sufﬁcient for ﬁne-tuning the small and medium
size NLLB architectures. For the random cross-
validation task, we train ﬁve distinct models on
different train/test/validation verse pair splits. For
all other tasks, only a single model of each type is
trained with the identiﬁed splits.
4
Results
We divide our results into four sections according
to tasks. We ﬁrst present results for a random cross-
validation task, then results for tasks speciﬁc to
translating NT books, then results for tasks spe-
ciﬁc to translating OT books, and ﬁnally results
for tasks speciﬁc to the use of a related language
translation. Further results are available for anal-
ysis in the ebible-experiments repository (Baines
et al., 2023b).
4.1
Cross-Validation Translation Task
We ﬁrst consider the benchmark task for CV by
verse. This effectively provides an upper bound
on possible model performance on later transla-
tion tasks. We run our ﬁve-fold CV across various
models and present the results in Figure 5. For
the three language families shown in Table 2, we
see a clear increase in performance from SMT to
OpenNMT in nearly all tests, with NLLB-600M
out-performing both techniques across all metrics.
Likewise, the ﬁne-tuned NLLB-1.3B-distilled ar-
chitecture out-performs its smaller counterpart in
all instances.
We also present the test set results across all
language families for the CV task using NLLB-
600M. Figure 6 shows a bar chart of the median
BLEU, spBLEU, and chrF3 scores for all eight
translation pairings. Interestingly, we ﬁnd no clear
correlation between the scope (NT-only, NT with
partial OT, or full Bible) of the translation pair-
ing and our selected scoring metrics. The wide
differences between word-level and subword-level
metrics (BLEU and spBLEU) for some translation
pairings such as Dravidian (+18.1), Sino-Tibetan
(+18.0), and Trans-New Guinea (+17.4), compared
to other translation pairings such as Austronesian
(+4.3), highlight the value of examining a range
of translation accuracy metrics when evaluating
results on these benchmarks.

--- Page 7 ---

Lang. Family(ISO-639-5)
Branch(es)
Purpose
Language(ISO-639-3)
Country
Afro-Asiatic
(afa)
Chadic
(afa : cdc)
Source
Hausa (hau)
Nigeria
Target
Dangaléat (daa)
Chad
Related
Fulfulde, Western Niger (fuh)
Niger
Austronesian
(map)
Malayo-Polynesian,
Central Eastern Malayo-Poly.,
Eastern Malayo-Polynesian
(map : poz : pqe)
Source
Kuanua (ksd)
Papua New Guinea
Target
Kandas (kqw)
Papua New Guinea
Related
Ramoaaina (rai)
Papua New Guinea
Dravidian
(dra)
N/A
Source
Tamil (tam)
India
Target
Malayalam (mal)
India
Related
Kannada (kan)
India
Indo-European
(ine)
Indo-Iranian,
Indo-Aryan
(ine : iir : inc)
Source
Hindi (hin)
India
Target
Eastern Panjabi (pan)
India
Related
Gujarati (guj)
India
Niger-Congo
(nic)
Atlantic-Congo
(nic : alv)
Source
Swahili (swh)
Tanzania
Target
Kwere (cwe)
Tanzania
Related
Vidunda (vid)
Tanzania
Otomanguean
(cai : omq)
Eastern Otomanguean
Source
Spanish (spa)
Spain
Target
Zapotec, Tabaa (zat)
Mexico
Related
Tapotec, Cajonos (zad)
Mexico
Sino-Tibetan
(sit)
N/A
Source
Nepali (npi)
Nepal
Target
Tamang, Eastern (taj)
Nepal
Related
Limbu (lif)
Nepal
Trans-New Guinea
(paa : ngf)
N/A
Source
Tok Pisin (tpi)
Papua New Guinea
Target
Yopno (yut)
Papua New Guinea
Related
Iyo (nca)
Papua New Guinea
Table 1: Language pairings for machine translation benchmarks.
Figure 5: Bar chart of median BLEU, spBLEU, and chrF3 scores from SMT, NMT, and ﬁne-tuned NLLB-600M
models for the Dravidian, Niger-Congo, and Sino-Tibetan translation pairings. Note that ﬁve-fold CV is not
performed on the NLLB-1.3B-distilled model due to training overheads.

--- Page 8 ---

Figure 6: Bar chart of median BLEU, spBLEU, and
chrF3 scores from a ﬁne-tuned NLLB-600M model
across eight language families for the CV task.
4.2
New Testament Benchmark Tasks
We ﬁrst consider the Gospel Translation task of
ﬁne-tuning an NLLB-600M model using MRK as
the training set and MAT as the test set. Figure
7 shows the BLEU scores for this task across our
eight language families, including a comparison to
the CV task results. We see that in general, there
is a drop-off in performance compared to the CV
task for six of the eight translation pairings. This is
attributed to the increased data heterogeneity and
larger corpus used for training during the CV task.
These factors outweigh the beneﬁts of the subject
matter overlap between MRK and MAT. However,
results from these models for MAT are signiﬁcantly
better than their results for Epistles (see Table 2,
Gospel Translation portion).
Next, we consider the Epistle Translation task
where NLLB-600M models are either trained with
MRK, or trained with the Gospels plus Acts of
the Apostles, and then used to translate a selec-
tion of the Epistles (1TH, 2TH, 1TI, 2TI, and TIT).
These results are summarized in Table 2, which
demonstrates that models perform signiﬁcantly bet-
ter when translating the selected Epistles when their
training sets include these four additional books
(MAT, LUK, JHN, ACT).
Finally, we consider the NT Completion task us-
ing a ﬁne-tuned NLLB-600M model. We ﬁne-tune
models ﬁrst on MRK only, then on the Gospels plus
ACT, then on the entire NT except Romans (ROM)
and Revelation (REV). In this fashion we form
training sets with corpora of increasing size and lit-
erary breadth. For each translation pairing, BLEU
Figure 7: Bar chart of median BLEU, spBLEU, and
chrF3 scores from a ﬁne-tuned NLLB-600M model
across eight language families for the Gospel Transla-
tion task, as compared to the CV task.
scores for both ROM and REV increase across
these three tasks, indicating that the increased size
and literary breadth of the training set is beneﬁcial
for the translation of these challenging NT books.
4.3
Old Testament Benchmark Tasks
For the Early OT translation task, the entire NT
is used as the training set; the ﬁne-tuned model is
then evaluated on various books that are typically
translated early in an OT translation project (GEN-
DEU, RUT, PSA, JON). Figure 8 shows the BLEU
scores of NLLB-600M models trained across ﬁve
translation pairs on the NT, with translations per-
formed across books in the Early OT as the test
set. Empty cells indicate a lack of an available
translation for a particular book in the target lan-
guage. For the tested Early OT books, the highest
BLEU scores within a translation pair are observed
for GEN, while the lowest scores are observed for
LEV, NUM, or DEU.
Next, we assess the performance of NLLB-
600M on the Late OT translation task. The books in
this test set (the minor prophets) tend to be among
the last books of the Bible to be translated. Figure
9 shows the BLEU scores for OT minor prophet
books across Dravidian and Indo-European lan-
guage families, both in the case of models trained
on the entire NT and models trained on the entire
Bible (excluding the minor prophets). As before,
a larger corpus of training data led to a large im-
provement in BLEU scores.

--- Page 9 ---

Translation Pairing
Gospel Translation
Epistle Translation
1TH
2TH
1TI
2TI
TIT
1TH
2TH
1TI
2TI
TIT
Afro-Asiatic
6.3
5.5
4.8
6.9
2.9
14.8(+6.5)
17.3(+11.8)
11.3(+6.5)
14.3(+7.4)
9.3(+6.4)
Austronesian
12.7
15.4
13.3
13.3
13.9
20.1(+7.4)
21.5(+6.1)
19.9(+6.6)
23.5(+10.2)
19.8(+5.9)
Dravidian
10.1
12.0
4.2
7.4
2.0
11.4(+1.3)
13.4(+1.4)
7.0(+2.8)
8.1(+0.7)
5.2(+3.2)
Indo-European
24.1
22.5
17.1
22.3
15.5
28.7(+4.6)
26.2(+3.7)
21.3(+4.2)
26.7(+4.4)
21.6(+6.1)
Niger-Congo
9.4
13.4
10.7
10.8
7.3
14.9(+5.5)
16.7(+3.3)
15.1(+4.4)
14.5(+3.7)
13.6(+6.3)
Otomanguean
6.5
7.4
8.4
8.4
6.9
16.2(+9.7)
14.0(+6.6)
15.5(+7.1)
13.1(+4.7)
15.6(+8.7)
Sino-Tibetan
13.2
10.6
9.4
10.3
8.7
18.8(+5.6)
17.2(+6.6)
16.2(+6.8)
18.2(+7.9)
18.3(+9.6)
Trans-New Guinea
6.9
8.4
7.2
7.6
6.5
18.7(+11.8)
20.5(+12.1)
16.9(+9.7)
17.6(+10.0)
15.0(+8.5)
Table 2: BLEU scores for NLLB-600M ﬁne-tuned models: Gospel Translation and Epistle Translation tasks.
Translation
Pairing
Gospel
Translation
Epistle Translation
(vs Gospel Translation)
NT Completion
(vs Epistle Translation)
ROM
REV
ROM
REV
ROM
REV
Afro-Asiatic
7.0
7.6
14.1 (+7.1)
15.1 (+7.5)
18.9 (+4.8)
16.0 (+0.9)
Austronesian
11.5
15.3
18.1 (+6.6)
26.2 (+10.9)
23.2 (+5.1)
28.6 (+2.4)
Dravidian
8.2
9.7
10.9 (+2.7)
13.0 (+3.3)
12.8 (+1.9)
13.7 (+0.7)
Indo-European
23.2
21.7
26.5 (+3.3)
26.5 (+4.8)
30.0 (+3.5)
29.2 (2.7)
Niger-Congo
11.4
11.4
16.9 (+5.5)
20.3 (+8.9)
20.1 (+3.2)
23.5 (+3.2)
Otomanguean
7.6
9.8
15.2 (+7.6)
19.0 (+10.2)
22.1 (+6.9)
20.6 (+1.6)
Sino-Tibetan
12.0
13.5
19.5 (+7.5)
21.2 (+7.7)
23.3 (+3.8)
23.3 (+2.1)
Trans-New Guinea
8.8
7.4
18.5 (+9.7)
18.3 (+10.9)
24.9 (+6.4)
22.1 (+3.8)
Table 3:
BLEU scores for NLLB-600M ﬁne-tuned
models: Gospel Translation, Epistle Translation, NT
Completion tasks.
Figure 8: Radar plot of NLLB-600M BLEU scores for
four language families for the Early OT task. Miss-
ing points for Niger-Congo and Otomanguean indicate
that these books are not included in the target language
translation.
Figure 9: Radar plot of NLLB-600M BLEU scores for
Dravidian and Indo-European for Early and Late OT
tasks.
4.4
Related Language Benchmark Tasks
For the Related Language task, an additional trans-
lation is selected from the eBible corpus for each of
the eight language families. HMM word alignment
models are trained between the target language and
each related language translation in the eBible cor-
pus from the same branch of the language family;
the translation with the best alignment to the tar-
get language is selected as the related language
translation. Then, the Gospel Translation, Epistle
Translation, and NT Completion tasks are repeated
using both the target language and the related lan-
guage on the target side of the model. For each
task, the related language training data included
the same verse pairs used for the target language
training data; additionally, the related language
training data included the verse pairs from the tar-
get language test set.
Figure 10 compares the BLEU score deltas for
the Related Language version of each task com-
pared to the original version of the task. BLEU
score deltas across the eight language families
are widely divergent, ranging from -2.9 to +3.2
BLEU (Gospel Translation task), -4.0 to +10.6
BLEU (Epistle Translation task), and -2.7 to +11.5
BLEU (NT Completion task). Results for the Aus-
tronesian and Niger-Congo language families are
strongest, while results for the Afro-Asiatic, Indo-
European, Sino-Tibetan and Trans-New Guinea
language families are the weakest. These BLEU
score deltas correlate well with the HMM align-
ment scores between the target language and re-
lated language, with the Austronesian (0.68) and
Niger-Congo (0.49) translation pairings exhibit-
ing the highest alignment, and the Afro-Asiatic
(0.21), Indo-European (0.30), Sino-Tibetan (0.27)
and Trans-New Guinea (0.27) exhibiting the lowest
alignment among the selected translation pairings.

--- Page 10 ---

Figure 10: Impact of a Related Language Translation on the Gospel Translation, Epistle Translation, and NT
Completion tasks.
5
Discussion
On the CV benchmark task, median accuracy met-
rics across the eight selected language families var-
ied widely, ranging from 21.7 - 35.1 (BLEU), 37.9
- 49.5 (spBLEU), and 52.5 - 60.4 (chrF3). No in-
dividual characteristic of the selected languages
and translations correlated closely with the distri-
bution of these results for any of these three accu-
racy metrics. For instance, the scope of the source
/ target translation pairings varied from NT-only,
to NT with OT portions, to full BTs; while the
highest BLEU score was seen for an NT-only pair-
ing (Austronesian (35.1)) and the lowest BLEU
score was seen for a full Bible pairing (Dravid-
ian (21.7)), other NT-only pairings (Afro-Asiatic
(29.9); Sino-Tibetan (31.5)) and full Bible pairings
(Indo-European (30.5)) scored comparably. Sim-
ilar diversity was seen when comparing spBLEU
and chrF3 scores to the scope of the translation
pairings. HMM word alignment scores for the
source/target translation pairings also do not cor-
relate closely with the accuracy metrics on this
benchmark; translation pairings with the highest
(Niger-Congo (0.44)) and lowest (Otomanguean
(0.19)) word alignment scores resulted in compara-
ble BLEU scores (28.8 and 28.3, respectively).
NLLB characterized the resource level of each
supported language as either high or low, with low
resource languages being trained on less than 1M
bitexts. In our CV benchmark, the source lan-
guages were a mix of high resource (Hindi, Swahili,
Spanish), low resource (Hausa, Tamil, Nepali, Tok
Pisin), and unsupported (Kuanua). However, there
was no clear correlation between the NLLB re-
source level of the source language and the result-
ing metrics for the translation pairing. Similarly,
while the best chrF3 results were seen for transla-
tion pairings with languages using the Latin script
(Niger-Congo (60.4); Trans-New Guinea (60.1)),
which is well-represented in the NLLB vocabulary,
other Latin script translation pairings performed
relatively poorly (Afro-Asiatic (52.5); Austrone-
sian (54.2)).
While BLEU is a widely used, language agnostic
metric for assessing machine translation accuracy,
the fact that it is a word-level metric means that it
can be difﬁcult to interpret the metric across lan-
guages, particularly when attempting to judge the
usefulness of a translation model for a less well
known language. Combining a word-level metric
(e.g., BLEU) with a subword-level metric (e.g., sp-
BLEU) and a character-level metric (e.g., chrF3)
provides a more nuanced view.
Table 3 presents several sample predictions from
the CV task with median BLEU, spBLEU, and
chrF3 scores for their respective model2. The pre-
dictions are color-coded at the word level to give
a general sense of the accuracy of each predic-
tion, and suggest that, although the NLLB models
represent a strong improvement over earlier NMT
approaches, further improvement is needed.
Evaluating median verse accuracy across a range
of word, subword and character-level metrics can
help to establish a broad intuition about the useful-
ness of a translation model, but it is also important
to evaluate the distribution of these metrics. Gener-
ally, the distribution can be quite broad, as shown in
2For the sake of simplicity, we are comparing predictions
to existing translations. This has obvious limitations. For
instance, translations may use different translation strategies,
or there may even be mistakes in a translation. Reading each
of these texts in the target languages and creating a corrected
text in order to compute a BLEU score is, however, beyond
the scope of this paper.

--- Page 11 ---

Figure 11: Sample predictions with median verse accu-
racy, CV task models. Green indicates correct words,
yellow indicates partially correct words, purple indi-
cates moved words, and red indicates incorrect words.
Figure 12: Cumulative per-verse BLEU score distri-
bution for Afro-Asiatic, Niger-Congo, Otomanguean
models on CV task.
Figure 12 for the Afro-Asiatic, Niger-Congo, and
Otomanguean CV models. When the same or simi-
lar verse text occurs in multiple passages (e.g., the
parables in the Gospels), or when the verse text fol-
lows a repeating pattern (“from the tribe of Joseph,
...”; “from the tribe of Dan, ...”), accuracy can be
relatively higher. Translations for longer, more
complex verses tend to be relatively lower. In the
context of BT, presenting the model’s conﬁdence
level to the translator may be as helpful as present-
ing the suggested verse text, helping the translator
know where to focus. Augmenting the model’s pre-
dictions with external evaluation metrics may also
be helpful for focusing the translator’s attention on
low-conﬁdence verse drafts. Empirically collected
data on challenging verses could also provide a
valuable means of focusing the translator’s efforts.
6
Future Work
We envision a number of opportunities to expand
and improve on this current work. From a linguis-
tic point of view, our results open up questions
about how spBLEU scoring might capture aggluti-
nation and scripting more effectively than a BLEU
score, as well as broader questions about how the
viability of scoring methods might change based
on language morphology. Furthermore, it is not
usually clear why certain language families seem
more amenable to ﬁne-tuning than others using
NLLB (as measured by BLEU scores). It is also
unclear whether larger NLLB models (such as the
next largest architecture with 3.3B tunable parame-
ters) will lead to continued improvements, or yield
diminishing returns.
Our work also highlights potential beneﬁts from
incorporating multiple BTs during model training,
although the mixed results indicate that more so-
phisticated strategies should be investigated, while
considering factors such as language and transla-
tion characteristics (e.g. translation age, reading
level, style) and other metrics (e.g. word alignment
scores, subword evenness). Automated methods
for selecting the best source and related language
translations may improve performance over the
heuristics used in this work.
In this work, changes to the NLLB tokenizer
were limited to the introduction of special tokens
for new language codes. Some of the translations,
such as the Yopno (yut-yut) and Zapotec Tabaa (zat-
zatNTps) translations, included a number of char-
acters that were not known to the NLLB tokenizer,
slightly reducing the accuracy of the ﬁne-tuned
model. Other translations, such as the Limbu trans-
lation in Limbu script (lif-lifNT) included many
unknown characters, and prevented their use in
this work. We would like to explore translation
from the original texts in ancient Greek, Hebrew,
and Aramaic, which requires careful attention to
a variety of issues involving character encoding,
segmentation, and other issues. Effective methods
for augmenting NLLB and the NLLB tokenizer
for new scripts and characters will be necessary to
achieve the full beneﬁts of the eBible corpus. We
would also like to explore using this parallel corpus
to infer characteristics of translation languages for
the purpose of language documentation.
Moreover, given the limitations of available data
and compute resources for target communities
there is a gap in developing techniques that over-

--- Page 12 ---

come the "low-resource double bind" (Ahia et al.,
2021). Towards this end, implementing and study-
ing efﬁcient ﬁne-tuning methods (Pfeiffer et al.,
2020) would provide signiﬁcant support for the
more advanced neural models to be useful for trans-
lators on the ground.
The wide distribution of per-verse translation
accuracy indicates the need for effective human-in-
the-loop strategies to support the Bible translator,
ensuring that these differences are accurately and
intuitively presented to guide their work.
7
Conclusions
In this work we present the eBible corpus: an open-
source NMT-ready dataset of over a thousand par-
tial and full BTs spanning more than 800 languages.
With the aim of leveraging machine translation to
aid expert Bible translators, we introduce a num-
ber of benchmark tasks based on the translation
ordering often used by these experts. These tasks
include a randomized CV along with NT- and OT-
speciﬁc objectives. In addition to benchmark tasks,
we provide benchmark model results for selected
language families, with models ranging from SMT
methods to a ﬁne-tuned NLLB architecture.
8
Limitations
Ethics Statement
Contributions
J.M. cast the vision and along with M.M. organized
the work on the eBible corpus within the Partner-
ship for Applied Biblical NLP. V.A. wrote the ini-
tial scripts to download the corpus from eBible.org
while D.B. improved upon these. U.H. provided
signiﬁcant support for pre-processing through man-
ual and automatic data checks and cleanup. M.M,
J.M, T.J, D.B and M.S. designed the benchmark
experiments. M.M., D.B and D.D. ran experiments
and reported results. M.S. M.M., U.H. and J.M.
wrote and edited the manuscript.
Acknowledgements
The authors would like to thank their respective
organizations for encouraging their participation in
this cross-organization collaboration. They would
also like to acknowledge the foundational and on-
going work of Michael Johnson in creating and
maintaining the eBible.org site. Finally, we thank
the ETEN Innovation Lab (EIL) for sponsoring the
computing resources used in this project.
References
Orevaoghene Ahia, Julia Kreutzer, and Sara Hooker.
2021. The low-resource double bind: An empirical
study of pruning for low-resource machine transla-
tion. arXiv preprint arXiv:2110.03036.
Benjamin Akera, Jonathan Mukiibi, Lydia Sanyu Nag-
gayi, Claire Babirye, Isaac Owomugisha, Solomon
Nsumba,
Joyce Nakatumba-Nabende,
Engineer
Bainomugisha, Ernest Mwebaze, and John Quinn.
2022.
Machine translation for African languages:
Community creation of datasets and models in
Uganda.
David Baines, Joel Mathew, and Michael Martin.
2023a. The eBible corpus. https://github.com/
BibleNLP/ebible.
David Baines, Joel Mathew, and Michael Martin.
2023b. eBible corpus NMT experiments. https:
//github.com/BibleNLP/ebible-experiments.
Christos Christodouloupoulos and Mark Steedman.
2015.
A massively parallel corpus: the Bible in
100 languages. Language resources and evaluation,
49:375–395.
Richard Oliver Collin. 2010. Ethnologue. Ethnopoli-
tics, 9(3-4):425–432.
Marta R Costa-jussà, James Cross, Onur Çelebi, Maha
Elbayad, Kenneth Heaﬁeld, Kevin Heffernan, Elahe
Kalbassi, Janice Lam, Daniel Licht, Jean Maillard,
et al. 2022.
No language left behind:
Scaling
human-centered machine translation. arXiv preprint
arXiv:2207.04672.
Damien Daspit. 2023.
SIL-NLP.
https://github.
com/sillsdev/silnlp.
Yonggang Deng and William Byrne. 2008. HMM word
and phrase alignment for statistical machine transla-
tion. IEEE Transactions on Audio, Speech, and Lan-
guage Processing, 16(3):494–507.
Chris Dyer, Victor Chahuneau, and Noah A Smith.
2013. A simple, fast, and effective reparameteriza-
tion of IBM model 2. In Proceedings of the 2013
Conference of the North American Chapter of the
Association for Computational Linguistics: Human
Language Technologies, pages 644–648.
Naman Goyal, Cynthia Gao, Vishrav Chaudhary, Peng-
Jen Chen, Guillaume Wenzek, Da Ju, Sanjana Kr-
ishnan, Marc’Aurelio Ranzato, Francisco Guzmán,
and Angela Fan. 2022.
The ﬂores-101 evaluation
benchmark for low-resource and multilingual ma-
chine translation.
Transactions of the Association
for Computational Linguistics, 10:522–538.
Ulf Hermjakob. 2023. Wildebeest. https://github.
com/uhermjakob/wildebeest.

--- Page 13 ---

Katharina Kann, Abteen Ebrahimi, Manuel Mager, Ar-
turo Oncevay, John E Ortega, Annette Rios, An-
gela Fan, Ximena Gutierrez-Vasques, Luis Chiruzzo,
Gustavo A Giménez-Lugo, et al. 2022. Americasnli:
Machine translation and natural language inference
systems for Indigenous languages of the Americas.
Frontiers in Artiﬁcial Intelligence, 5:266.
Jeff Klassen. 2022. Uniﬁed standard format markers.
https://github.com/ubsicap/usfm.
Guillaume Klein, Yoon Kim, Yuntian Deng, Jean Senel-
lart, and Alexander M Rush. 2017. Opennmt: Open-
source toolkit for neural machine translation. arXiv
preprint arXiv:1701.02810.
Philipp Koehn. 2009. Statistical machine translation.
Cambridge University Press.
Sami Liedes. 2018. Machine translating the Bible into
new languages.
https://github.com/sliedes/
fairseq-py.
Arya D McCarthy, Rachel Wicks, Dylan Lewis, Aaron
Mueller, Winston Wu, Oliver Adams, Garrett Nico-
lai, Matt Post, and David Yarowsky. 2020.
The
Johns Hopkins University Bible corpus:
1600+
tongues for typological exploration. In Proceedings
of the Twelfth Language Resources and Evaluation
Conference, pages 2884–2892.
Myle Ott, Sergey Edunov, Alexei Baevski, Angela
Fan, Sam Gross, Nathan Ng, David Grangier, and
Michael Auli. 2019.
fairseq:
A fast, extensi-
ble toolkit for sequence modeling. arXiv preprint
arXiv:1904.01038.
Kishore Papineni, Salim Roukos, Todd Ward, and Wei-
Jing Zhu. 2002. Bleu: a method for automatic eval-
uation of machine translation. In Proceedings of the
40th annual meeting of the Association for Compu-
tational Linguistics, pages 311–318.
Jonas Pfeiffer, Andreas Rücklé, Clifton Poth, Aish-
warya
Kamath,
Ivan
Vuli´c,
Sebastian
Ruder,
Kyunghyun
Cho,
and
Iryna
Gurevych.
2020.
Adapterhub: A framework for adapting transform-
ers. In Proceedings of the 2020 Conference on Em-
pirical Methods in Natural Language Processing:
System Demonstrations, pages 46–54.
Maja Popovi´c. 2015. chrf: character n-gram F-score
for automatic MT evaluation. In Proceedings of the
tenth workshop on statistical machine translation,
pages 392–395.
Philip Resnik, Mari Broman Olsen, and Mona Diab.
1999. The Bible as a parallel corpus: Annotating
the ‘Book of 2000 Tongues’.
Computers and the
Humanities, 33:129–153.
Winston Wu, Nidhi Vyas, and David Yarowsky. 2018.
Creating a translation matrix of the Bible’s names
across 591 languages.
In Proceedings of the
Eleventh International Conference on Language Re-
sources and Evaluation (LREC 2018).
Jinhua Zhu, Yingce Xia, Lijun Wu, Di He, Tao Qin,
Wengang Zhou, Houqiang Li, and Tie-Yan Liu.
2020. Incorporating bert into neural machine trans-
lation. arXiv preprint arXiv:2002.06823.
A
Characteristics of Selected Bible
Translations
Table 4 goes into greater depth on the characteris-
tics of selected BTs.
B
NLLB Language Codes
Table 5 lists the language codes speciﬁc to Meta’s
NLLB.
C
Source / Target / Related Language
Alignment Scores (HMM)
We report on initial HMM scores which led to our
decisions around speciﬁc source and target lan-
guage decisions within selected language families.
C.1
Afro-Asiatic
For the Afro-Asiatic language family, the Chadic >
Biu-Mandara branch contains 79 languages (four
translations in the corpus) and the Chadic > East
branch contains 36 languages (one translation in
the corpus). These ﬁve translations only contain the
NT portion of the Bible, and are languages spoken
in either Cameroon or Chad. English and French
are national languages for Cameroon. French and
Arabic are national languages for Chad. Table 6
shows that the best alignment results were achieved
using a Hausa translation (hau-hausa) with the Dan-
galéat translation (daa-daaNT). The Western Niger
Fulfulde translation (ful-fuhbkf) aligned best with
the Dangaléat translation.
C.2
Austronesian
For the Austronesian language family, the Malayo-
Polynesian > Central-Eastern Malayo-Polynesian
> Eastern Malayo-Polynesian > Oceanic branch
contains 513 languages. Of these 513 languages,
the eBible corpus contains four translations from
the Western Oceanic sub-branch. All four of these
are for languages spoken in Papua New Guinea
(PNG). Three of these translations contain the NT
only, and one contains the NT and a portion of
the OT (four translations in the corpus) and the
Chadic > East branch contains 36 languages (one
translation in the corpus). English and Tok Pisin
(tpi) are national languages in PNG, while Dobu
(dob), Kuanua (ksd), Suau (swp) and Tawala (tbo)

--- Page 14 ---

Language
Family
Purpose
Language
ISO-
639-3
eBible
Translation
Scope
Verses
Script
Typology
Country
Afro-Asiatic
Source
Hausa
hau
hau-hausa.txt
Bible
31,082
Latn
SVO
Nigeria
Target
Dangaléat
daa
daa-daaNT.txt
NT
7,957
Latn
Unk
Chad
Related
Fulfulde,
Western Niger
fuh
fuh-fuhbkf.txt
NT
7,57
Latn
SVO
Niger
Austronesian
Source
Kuanua
ksd
ksd-ksd.txt
Bible
31,098
Latn
Unk
PNG*
Target
Kandas
kqw
kqw-kqw.txt
NT
7,957
Latn
Unk
PNG
Related
Ramoaaina
rai
rai-rai.txt
NT
7,957
Latn
SVO
PNG
Dravidian
Source
Tamil
tam
tam-tam2017.txt
Bible
31,099
Taml
SOV
India
Target
Malayalam
mal
mal-mal.txt
Bible
31,089
Mlym
SOV
India
Related
Kannada
kan
kan-kan2017.txt
Bible
31,099
Knda
SOV
India
Indo-European
Source
Hindi
hin
hin-hin2017.txt
Bible
31,099
Deva
SOV
India
Target
Eastern
Panjabi
pan
pan-pan.txt
Bible
31,099
Gurm
SOV
India
Related
Gujarati
guj
guj-guj2017.txt
Bible
31,099
Gujr
SOV
India
Niger-Congo
Source
Swahili
swh
swh-swhonen.txt
Bible
31,098
Latn
SVO
Tanzania
Target
Kwere
cwe
cwe-cwe.txt
GEN-DEU,
NT
13,806
Latn
Unk
Tanzania
Related
Vidunda
vid
vid-vid.txt
GEN-DEU,
NT
13,809
Latn
Unk
Tanzania
Otomanguean
Source
Spanish
spa
spa-sparvg.txt
Bible
31,097
Latn
SVO
Spain
Target
Zapotec,
Tabaa
zat
zat-zatNTps.txt
PSA, NT
10,416
Latn
VSO
Mexico
Related
Tapotec,
Cajonos
zad
zad-zadNT.txt
NT
7,957
Latn
VSO
Mexico
Sino-Tibetan
Source
Nepali
npi
npi-npiulb.txt
Bible
31,099
Deva
SOV
Nepal
Target
Tamang,
Eastern
taj
taj-taj.txt
NT
7,957
Deva
SOV
Nepal
Related
Limbu
lif
lif-lifNT2.txt
NT
7,957
Deva
SOV
Nepal
Trans-New Guinea
Source
Tok Pisin
tpi
tpi-tpiOTNT.txt
Bible
31,099
Latn
SOV
PNG
Target
Yopno
yut
yut-yut.txt
PSA, NT
10,417
Latn
SOV
PNG
Related
Iyo
nca
nca-nca.txt
NT
7,957
Latn
SOV
PNG
Table 4: BT characteristics.

--- Page 15 ---

Language Family
Language
ISO-639-3
NLLB
Language Code
Afro-Asiatic
Hausa
hau
hau_Latn
Dangaléat
daa
(!) daa_Latn
Fulfulde, Western Niger
fuh
(!) fuh_Latn
Austronesian
Kuanua
ksd
(!) ksd_Latn
Kandas
kqw
(!) kqw_Latn
Ramoaaina
rai
(!) rai_Latn
Dravidian
Tamil
tam
tam_Taml
Malayalam
mal
mal_Mlym
Kannada
kan
kan_Knda
Indo-European
Hindi
hin
hin_Deva
Eastern Panjabi
pan
pan_Gurm
Gujarati
guj
guj_Gujr
Niger-Congo
Swahili
swh
swh_Latn
Kwere
cwe
(!) cwe_Latn
Vidunda
vid
(!) vid_Latn
Otomanguean
Spanish
spa
spa_Latn
Zapotec, Tabaa
zat
(!) zat_Latn
Tapotec, Cajonos
zad
(!) zad_Latn
Sino-Tibetan
Nepali
npi
npi_Deva
Tamang, Eastern
taj
(!) taj_Deva
Limbu
lif
(!) lif_Deva
Trans-New Guinea
Tok Pisin
tpi
tpi_Latn
Yopno
yut
(!) yut_Latn
Iyo
nca
(!) nca_Latn
Table 5: NLLB language codes.

--- Page 16 ---

Target
Language(s)
National/Gateway
Language(s)
Related
Language(s)
Language
Translation
eng-engULB
fra-frasbl
hau-hausa
hau-hauulb
ffm-ffm
fuh-fhubkf
Hdi
xed-xed
0.1792
0.1691
0.1860
0.1736
0.1915
0.1982
Mbuko
mqb-mqbNT
0.1366
0.1291
0.1465
0.1298
0.1560
0.1613
Merey
meq-meq
0.1422
0.1368
0.1546
0.1376
0.1598
0.1640
Muyang
muy-muy
0.1513
0.1451
0.1537
0.1403
0.1818
0.1862
Dangaléat
daa-daaNT
0.1912
0.1760
0.1929
0.1705
0.2044
0.2148
Table 6: Source / Target / Related Language Alignment
Scores (Afro-Asiatic).
Target
Language(s)
National/Gateway
Language(s)
Related
Language(s)
Language
Translation
tpi-tpiOTNT
dob-dob
swp-swp
tbo-tbo
ksd-ksd
kqw-kqw
lbb-lbb
gfk-gfk
rai-rai
sgq-sgq
Fanamarket
bjp-bjp
0.2581
0.1761
0.2068
0.1990
0.2701
0.3994
0.4134
0.3025
0.3974
0.2576
Kandas
kqw-kqw
0.2213
0.1629
0.2003
0.1897
0.3303
N/A
0.6847
0.2910
0.6849
0.2516
Label
lbb-lbb
0.2152
0.1657
0.2127
0.1979
0.3229
N/A
N/A
0.2789
0.6583
0.2538
Patpatar
gfk-gfk
0.1966
0.1462
01662
0.1567
0.2707
N/A
N/A
N/A
0.2938
0.1919
Ramoaaina
rai-rai
0.2120
0.1613
0.2069
0.1874
0.3916
N/A
N/A
N/A
N/A
0.2475
Sursurunga
sgq-sgq
0.1775
0.1353
0.1440
0.1498
0.1692
N/A
N/A
N/A
N/A
N/A
Table 7: Source / Target / Related Language Alignment
Scores (Austronesian).
are gateway languages from the Malayo-Polynesian
branch with translations in the corpus.
Among these translations, the Kuanua transla-
tion (ksd-ksd) was selected as the source and the
Kandas translation (kqw-kqw) was selected as the
target due to their strong alignment score. The
Label (lbb-lbb) and Ramoaaina (rai-rai) transla-
tions both aligned well with the Kandas translation
(kqw-kqw); Ramoaaina was selected as the related
language translation. Results are summarized in
Table 7.
C.3
Dravidian
For the Dravidian language family (85 total lan-
guages), the Southern > Tamil-Kannada branch
contains 31 languages. Of these 31 languages, the
eBible corpus contains ﬁve translations, one from
the Kannada sub-branch and four from the Tamil-
Kodagu sub-branch. All ﬁve of these are for lan-
guages spoken in India, and each translation is a
full BT. Each of these translations is for a national
language of India (Kannada, Malayalam, Tamil,
and Telugu). There are no translations for low-
resource languages from this language family and
geography available in the corpus. As a result, the
Tamil (tam-tam2017) and Malayalam (mal-mal)
translations were chosen for the source and target
translation pairing, with the Kannada translation
(kan-kan2017) as the related language translation.
Results are summarized in Table 8.
Target
Language(s)
National/Gateway
Language(s)
Related
Language(s)
Language
Translation
hin-hin2017
kan-kan2017
mal-mal
mal-malc
Tamil
tam-tam2017
0.2063
0.3466
0.4295
0.3396
Telugu
tel-tel2017
0.2097
0.3423
0.3229
0.3068
Table 8: Source / Target / Related Language Alignment
Scores (Dravidian).
Target
Language(s)
National/Gateway
Language(s)
Related
Language(s)
Language
Translation
hin-hin2017
npi-npiulb
pan-pan
ben-ben2017
Gujarati
guj-guj2017
0.3012
0.3200
0.2973
0.3041
E. Panjabi
pan-pan
0.4240
0.2623
N/A
0.3665
Assamese
asm-asmfb
0.2796
0.3172
0.2616
0.3666
Bengali
ben-ben2017
0.2904
0.3242
0.2774
N/A
Marathi
mar-mar
0.2521
0.2989
0.2461
0.2767
Orya
ory-ory
0.3036
0.3098
0.2942
0.4031
Urdu
urd-urd
0.4622
0.2576
0.4415
0.2765
Urdu
urd-urdgvh
0.3123
0.2346
0.2949
0.2270
Urdu
urd-urdgvr
0.3092
0.2293
0.3012
0.2238
Urdu
urd-urdgvu
0.3041
0.2253
0.2964
0.2205
Table 9: Source / Target / Related Language Alignment
Scores (Indo-European).
C.4
Indo-European
For the Indo-European language family, the Indo-
Iranian > Indo-Aryan branch contains 220 lan-
guages, with 92 languages in the Intermediate >
Western sub-branch, 94 languages in the Outer sub-
branch, and 11 languages in the Western Hindi sub-
branch. The eBible corpus contains two transla-
tions from the Intermediate > Western sub-branch,
four from the Outer sub-branch and ﬁve from the
Western Hindi sub-branch (representing two lan-
guages). Each of these translations is for a lan-
guage spoken in Bangladesh, India, Nepal, and/or
Pakistan, and each is a full BT. There are no trans-
lations for low-resource languages from this lan-
guage family and geography available in the corpus.
As a result, the Hindi (hin-hin2017) and Eastern
Panjabi (pan-pan) translations were chosen for the
source and target translation pairing, with the Gu-
jarati translation (guj-gju2017) as the related lan-
guage translation. Results are summarized in Table
9.
C.5
Niger-Congo
For the Niger-Congo language family, the Volta-
Congo > Benue-Congo > Bantoid > Southern >
Narrow-Bantu > Central branch contains 354 lan-
guages. Of these 354 languages, the eBible corpus
contains 19 translations for languages spoken in
Tanzania, including three Swahili full BTs, two
NT+ translations (Kwere (cwe-cwe) and Vidunda
(vid-vid)), and 14 NT-only translations. Among
these translations, the Swahili translation (swh-
swhonen) was selected as the source and the Kwere
translation (cwe-cwe) was selected as the target,
and the Vidunda translation (vid-vid) was selected
as the related language translation. Preference was
given to the Kwere and Vidunda translations due to
their partial OT content. Results are summarized
in Table 10.

--- Page 17 ---

Target
Language(s)
National/Gateway
Language(s)
Related
Language(s)
Language
Translation
swh-swhonen
swh-swhulb
cwe-cwe
vid-vid
Kwere*
cwe-cwe
0.4382
0.3758
N/A
0.4912
Isanzu
isn-isn
0.3245
0.5625
0.2638
0.2424
Kutu
kdc-kdc
0.4326
0.3685
0.5347
0.4760
Makonda
kde-kde
0.4509
0.3672
0.4451
0.4315
Kisi
kiz-kiz
0.4320
0.7855
0.3446
0.3304
Mwera
mwe-mwe
0.4216
0.3560
0.4287
0.4382
Ndamba
ndj-ndj
0.4098
0.3544
0.4609
0.4808
Ngulu
ngp-ngp
0.3891
0.3383
0.4459
0.4112
Ngindo
nnq-nnq
0.4118
0.3517
0.4602
0.4754
Pogolo
poy-poy
0.4235
0.3608
0.4745
0.4781
Kara
reg-reg
0.3732
0.5998
0.3143
0.2850
Luguru
ruf-ruf
0.4457
0.3807
0.5570
0.4701
Vidunda*
vid-vid
0.4045
0.3462
0.4913
N/A
Vwanji
wbi-wbi
0.3477
0.4811
0.3169
0.2933
Zaramo
zaj-zaj
0.4652
0.3965
0.4784
0.4331
Zigula
ziw-ziw
0.4149
0.3624
0.4748
0.4451
Table 10:
Source / Target / Related Language Align-
ment Scores (Niger-Congo).
C.6
Otomanguean
For the Otomanguean language family with 179
total languages, the Eastern-Otomanguean >
Popolocan-Zapotecan > Zapotecan branch con-
tains 64 languages. Of these 64 languages, the
eBible corpus contains 28 translations for lan-
guages spoken in Mexico, including three acNT+
translations3, and 25 NT-only translations; there
are no full BTs from this branch. Among these
translations, a Spanish translation (spa-sparvg)
translation was selected as the source and the Za-
potec Tabaa translation (zat-zatNTps) was selected
as the target; preference was given to the Zaopotec
Tabaa translation due to its partial OT content. The
Zapotec Cajonos translation (zad-zadNT) was se-
lected as the related language translation. Results
are summarized in Table 11.
C.7
Sino-Tibetan
For the Sino-Tibetan language family (458 total
languages), the Tibeto-Burman > Western Tibeto-
Burman branch contains 442 languages. Of these
442 languages, the eBible corpus contains 15
translations spread across the Kuki-Chin (eight),
Ngwi-Burmese (three), and Western Tibeto-Burman
(four) sub-branches. Translations from these sub-
branches are for languages spoken in China, India,
Myanmar, and Nepal, with eight full Bible, one
NT+, and ﬁx NT-only translations. The best align-
ment results were seen with a Nepali translation
(npi-npiulb) as the source and the Eastern Tamang
translation (taj-taj) as the target. The Limbu transla-
tion in Devanagari script (lif-lifNT2) was selected
3Zapotec Rincón (zar-zarNT), Zapotec Tabaa (zat-
zatNTps), and Zapotec Yatee (zty-ztyNTps).
Target
Language(s)
National/Gateway
Language(s)
Related
Language(s)
Language
Translation
spa-sparvg
zar-zarNT
zat-zatNTps
Chatino, Tataltepec
cta-ctaNT
0.1029
0.1229
0.1214
Chatino, Western Highland
ctp-ctpNT
0.0947
0.1165
0.1157
Chatino, Nopala
cya-cya
0.1718
0.1718
0.1667
Zapotec, Sierra de Juárez
zaa-zaaNT
0.1662
0.1663
0.1653
Zapotec, Western Tlacolula Valley
zab-zabNT
0.2092
0.2281
0.2456
Zapotec, Ocotlán
zac-zacNT
0.1733
0.1896
0.2022
Zapotec, Cajonos
zad-zadNT
0.1877
0.2485
0.2757
Zapotec, Isthmus
zai-zaiNT
0.1835
0.2000
0.1957
Zapotec, Miahuatlán
zam-zamNT
0.1161
0.1362
0.1369
Zapotec, Ozolotepec
zao-zaoNT
0.1810
0.2056
0.2119
Zapotec, Rincón
zar-zarNT*
0.1901
N/A
N/A
Zapotec, Santo Domingo Albarradas
zas-zasNT
0.1858
0.2301
02420
Zapotec, Tabaa
zat-zatNTps*
0.1869
N/A
N/A
Zapotec, Yatzachi
zav-zavNT
0.1536
0.1960
0.2049
Zapotec, Mitla
zaw-zawNT
0.2094
0.2202
0.2263
Zapotec, Coatecas Altas
zca-zcaNT
0.1567
0.1855
0.1825
Zapotec, Choapan
zpc-zpcNT
0.1439
0.2057
0.2097
Zapotec, Mixtepec
zpm-zpmNT
0.1215
0.1387
0.1370
Zapotec, Amatlán
zpo-zpoNT
0.1718
0.1985
0.2027
Zapotec, Zoogocho
zpq-zpqNT
0.1549
0.2162
0.2371
Zapotec, Yalálag
zpu-zpuNT
0.1557
0.2148
0.2440
Zapotec, Chichicapan
zpv-zpvNT
0.1642
0.1836
0.1948
Zapotec, Texmelucan
zpz-zpzNTpp
0.1438
0.1727
0.1745
Zapotec, Southern Rincon
zsr-zsrNT
0.1988
0.9000
0.3517
Zapotec, Quioquitani-Quierí
ztq-ztqNT
0.1676
0.1944
0.2111
Zapotec, Yatee
zty-ztyNTps*
0.1782
0.5623
0.4381
Table 11:
Source / Target / Related Language Align-
ment Scores (Otomanguean).
Target
Language(s)
National/Gateway
Language(s)
Related
Language(s)
Language
Translation
hin-hin2017
npi-npiulb
mya-mya
mya-myajvb
taj-taj
Zaiwa
atb-atbNT
0.1827
0.1640
0.1621
0.1703
0.1545
Chin, Eastern Khumi
cek-cekak
0.2112
0.2074
0.1259
0.2237
0.1655
Chin, Thaiphum
cth-cth
0.1821
0.1806
0.1237
0.2478
0.1463
Chin, Siyin
csy-csy
0.2078
0.1843
0.1423
0.1854
0.1590
Chin, Matu
hlt-hlt
0.2281
0.2170
0.1229
0.2208
0.1620
Chin, Matu
hlt-hltmcsb
0.2296
0.2191
0.1237
0.2216
0.1642
Chin, Matu
hlt-hltthb
0.1678
0.1698
0.1195
0.1559
0.1449
Limbu (Limbu*)
lif-lifNT
0.2108
0.2665
0.1142
0.1513
0.2664
Limbu (Deva)
lif-lifNT2
0.2093
0.2660
0.1131
0.1509
0.2650
Sunwar
suz-suzBl
0.2008
0.2065
0.1107
0.1563
0.1805
Tamang, Eastern
taj-taj
0.1959
0.2657
0.1204
0.1344
N/A
Chin, Thado
tcz-tczchongthu
0.1271
0.1303
0.0976
0.1207
0.1487
Chin, Zyphe
zyp-zypNT
0.1765
0.1824
0.1399
0.1583
0.1662
Table 12:
Source / Target / Related Language Align-
ment Scores (Sino-Tibetan).
for the related language translation. Results are
summarized in Table 12.
C.8
Trans-New Guinea
For the Trans-New Guinea language family (481
total languages), the Finisterre-Huon > Finisterre
branch contains 40 languages and the Madang
> Croisilles branch contains 57 languages. The
eBible corpus contains 10 translations from the
Finisterre-Huon > Finisterre branch; ﬁve of these
are NT-only translations and ﬁve are NT+ trans-
lations. For the Madang > Croisilles branch, the
eBible corpus contains eight translations; six of
these are NT-only translations and two are NT+
translations. These translations are for languages
spoken in Papua New Guinea, where national lan-
guages are English and Tok Pisin (tpi). The best
alignment results were observed with a Tok Pisin
translation (tpi-tpiOTNT) as the source and the
Yopno translation (yut-yut) as the target, while the
Iyo translation (nca-nca) was selected for the re-
lated language translation. Results are summarized
in Table 13.

--- Page 18 ---

Target
Language(s)
National/Gateway
Language(s)
Related
Language(s)
Language
Translation
tpi-tpi
tpi-tpiOTNT
yut-yut
aey-aey
Finisterre-Huon > Finisterre Sub-branch
Gwahatike
dah-dah
0.1354
0.1354
0.1545
N/A
Tuma-Irumu
iou-iou*
0.1573
0.1573
0.1902
N/A
Iyo
nca-nca
0.2034
0.2034
0.2677
N/A
Numanggang
nop-nop*
0.1790
0.1790
0.2261
N/A
Rawa
rwo-rwo-karo
0.1913
0.1913
0.1859
N/A
Rawa
rwo-rwo-rawa
0.1917
0.1917
0.1854
N/A
Uri
uvh-uvh
0.1307
0.1307
0.1296
N/A
Wantoat
wnc-wnc*
0.1840
0.1840
0.1831
N/A
Yau
yuw-yuw
0.1774
0.1774
0.2161
N/A
Yopno
yut-yut*
0.2252
0.2252
N/A
N/A
Madang > Croisilles Sub-branch
Amele
aey-aey*
0.2089
0.2089
N/A
N/A
Girawa
bbr-bbr
0.1948
0.1948
N/A
0.2298
Nobonob
gaw-gaw
0.1875
0.1875
N/A
0.2432
Kein
bmh-bmh
0.1934
0.1934
N/A
0.2171
Mauwake
mhl-mhl
0.1659
0.1659
N/A
0.1809
Bargam
mlp-mlp
0.1868
0.1868
N/A
0.1971
Usan
wnu-wnu
0.1592
0.1592
N/A
0.1765
Waskia
wsk-wsk*
0.1866
0.1866
N/A
0.2353
Table 13:
Source / Target / Related Language Align-
ment Scores (Trans-New Guinea).
D
Biblical Book Identiﬁers
Table 14 lists the standard three-character book
identiﬁers utilized as part of the uniﬁed standard
format markers (USFM) format.
E
Extended Results
In this section, we include additional results of in-
terest, represented in tabular form. Several of these
tables have ﬁgure analogs in the main body of the
paper. First, we consider the effect of increasing
model size for Meta’s NLLB model, which is avail-
able in ﬁve different conﬁgurations, ranging from
600M to 54.5B parameters. To evaluate the po-
tential beneﬁts of working with the larger models,
the NLLB-1.3B (distilled) model was ﬁne-tuned
on one of the same train/test/validation splits from
the previous tests. This was done for the Dravidian,
Niger-Congo, and Sino-Tibetan translation pair-
ings. Translation accuracy metrics with the NLLB-
1.3B-distilled models were consistently better for
each translation pairing than with the NLLB-600M
model, as shown in 15.
Next, we consider how model complexity im-
proves performance across all ﬁve scoring metrics,
as shown in Table 16.
We also reiterate the median performance across
scoring metrics, along with counts for the total
number of available verses per each target transla-
tion, as shown in Table 17.
Table 18 shows BLEU, spBLEU, and chrF3
scores for the CV task as well as the Gospel Trans-
lation task.
Book Name
Identiﬁer
Genesis
GEN
Exodus
EXO
Leviticus
LEV
Numbers
NUM
Deuteronomy
DEU
Joshua
JOS
Judges
JDG
Ruth
RUT
1 Samuel
1SA
2 Samuel
2SA
1 Kings
1KI
2 Kings
2KI
1 Chronicles
1CH
2 Chronicles
2CH
Ezra
EZR
Nehemiah
NEH
Esther
EST
Job
JOB
Psalms
PSA
Proverbs
PRO
Ecclesiastes
ECC
Song of Songs
SNG
Isaiah
ISA
Jeremiah
JER
Lamentations
LAM
Ezekiel
EZK
Daniel
DAN
Hosea
HOS
Joel
JOL
Amos
AMO
Obadiah
OBA
Jonah
JON
Micah
MIC
Nahum
NAH
Habakkuk
HAB
Zephaniah
ZEP
Haggai
HAG
Zechariah
ZEC
Malachi
MAL
Matthew
MAT
Mark
MRK
Luke
LUK
John
JHN
Acts of the Apostles
ACT
Romans
ROM
1 Corinthians
1CO
2 Corinthians
2CO
Galatians
GAL
Ephesians
EPH
Philippians
PHP
Colossians
COL
1 Thessalonians
1TH
2 Thessalonians
2TH
1 Timothy
1TI
2 Timothy
2TI
Titus
TIT
Philemon
PHM
Hebrews
HEB
James
JAS
1 Peter
1PE
2 Peter
2PE
1 John
1JN
2 John
2JN
3 John
3JN
Jude
JUD
Revelation
REV
Table 14:
Three-letter identiﬁers for Biblical books
(excluding those not used in this work).

--- Page 19 ---

TranslationPairing
Model
BLEU
spBLEU
chrF3
WER
TER
Dravidian
NLLB-600M
21.7
40.0
59.5
46.6
69.7
NLLB-1.3B-distilled
24.9
(+3.2)
44.2
(+4.2)
62.7
(+3.2)
43.9
(-2.7)
65.6
(-4.1)
Niger-Congo
NLLB-600M
28.3
37.9
60.5
43.6
65.2
NLLB-1.3B-distilled
29.9
(+1.6)
40.0
(+2.1)
62.2
(+1.7)
41.7
(-1.9)
63.1
(-2.1)
Sino-Tibetan
NLLB-600M
31.5
49.5
57.9
52.0
64.0
NLLB-1.3B-distilled
33.1
(+1.6)
51.0
(+1.5)
59.9
(+2.0)
52.1
(+0.1)
62.3
(-1.7)
Table 15:
Model size impact, NLLB-600M versus
NLLB-1.3B (distilled).
TranslationPairing
MT Technology
BLEU
spBLEU
chrF3
WER
TER
Dravidian
SMT
9.8
20.1
36.9
98.6
84.4
OpenNMT
13.3
28.0
46.9
56.3
79.0
NLLB-600M
21.7
39.8
58.2
47.0
68.6
NLLB-1.3B-distilled*
24.9
44.2
62.7
43.9
65.6
Niger-Congo
SMT
19.3
27.6
49.2
81.6
73.8
OpenNMT
16.6
24.3
45.2
55.2
77.9
NLLB-600M
28.8
37.9
60.4
43.9
65.2
NLLB-1.3B-distilled*
29.9
40.0
62.2
41.7
63.1
Sino-Tibetan
SMT
9.9
30.8
42.1
60.2
84.4
OpenNMT
10.2
26.5
37.4
66.9
86.8
NLLB-600M
31.5
49.5
57.9
52.0
64.0
NLLB-1.3B-distilled*
33.1
51.0
59.9
52.1
62.3
Table 16:
Machine translation across model types
(SMT, OpenNMT, and NLLB-600M). *Five-fold CV
is not performed on NLLB-1.3B-distilled due to train-
ing overheads.
TranslationPairing
Training Verses
BLEU
spBLEU
chrF3
WER
TER
Afro-Asiatic
7,394
29.9±1.4
38.4±1.5
52.5±1.2
51.6±1.3
67.2±1.6
Austronesian
7,404
35.1±1.1
39.4±1.1
54.2±0.6
49.1±1.6
62.0±1.4
Dravidian
30,589
21.7±0.8
39.8±0.8
58.2±0.6
47.0±0.9
68.6±0.9
Indo-European
30,599
30.5±1.0
40.4±1.1
55.7±0.7
42.5±1.1
55.8±1.4
Niger-Congo
13,304
28.8±1.0
37.9±0.7
60.4±0.6
43.9±0.7
65.2±1.1
Otomanguean
9,901
28.3±0.9
44.3±0.8
56.4±1.2
50.9±0.6
68.1±0.7
Sino-Tibetan
7,419
31.5±1.6
49.5±1.5
58.9±0.7
50.5±1.3
63.9±1.7
Trans-New Guinea
9,775
31.6±0.7
49.0±0.5
60.1±0.9
48.0±0.8
61.6±0.4
Table 17: Median translation accuracy scores by trans-
lation pairing.
CV Task
Gospel Translation Task
TranslationPairing
BLEU
spBLEU
chrF3
BLEU
spBLEU
chrF3
Afro-Asiatic
29.9
38.4
52.1
30.2 (+0.3)
35.8 (-2.6)
49.7 (-2.4)
Austronesian
35.1
39.4
53.8
33.7 (-1.4)
36.2 (-3.2)
52.6 (-1.2)
Dravidian
21.7
39.8
58.5
18.2 (-3.5)
35.1 (-4.7)
58.1 (-0.4)
Indo-European
30.5
40.4
55.5
36.5 (+6.0)
44.5 (+4.1)
59.9 (+4.4)
Niger-Congo
28.8
37.9
60.1
21.7 (-7.1)
29.7 (-10.2)
53.7 (-6.4)
Otomanguean
28.3
44.3
56.7
20.4 (-7.9)
34.5 (-9.8)
48.7 (-8.0)
Sino-Tibetan
31.5
49.5
58.8
30.6 (-0.9)
45.9 (-3.6)
56.1 (-2.7)
Trans-New Guinea
31.6
49.0
59.8
28.5 (-3.1)
41.7 (-7.3)
51.7 (-8.1)
Table 18: Scores for NLLB-600M ﬁne-tuned models
for the CV task and the Gospel Translation task.
Dravidian (BLEU)
Indo-European (BLEU)
Minor Prophet
Early OT Task
Late OT Task
Early OT Task
Late OT Task
HOS
10.4
16.6 (+6.2)
16.6
22.6 (+6.0)
JOL
10.2
19.2 (+9.0)
19.2
28.5 (+9.3)
AMO
7.2
17.9 (+10.7)
19.0
26.0 (+7.0)
OBA
5.4
16.7 (+11.3)
16.9
26.3 (+9.4)
MIC
7.0
14.7 (+7.7)
20.8
25.8 (+5.0)
NAH
4.5
10.9 (+6.4)
13.8
21.4 (+7.6)
HAB
5.9
9.8 (+3.9)
18.9
22.2 (+3.3)
ZEP
8.1
15.1 (+7.0)
19.1
29.2 (+10.1)
HAG
6.9
21.3 (+14.4)
17.9
34.3 (+16.4)
ZEC
8.3
16.6 (+8.3)
17.1
27.1 (+10.0)
MAL
8.2
11.9 (+3.7)
15.4
22.8 (+7.4)
Table 19:
BLEU scores for NLLB-600M ﬁne-tuned
models on Early OT and Late OT tasks.
TranslationPairing
GEN
EXO
LEV
NUM
DEU
RUT
PSA
JON
Dravidian
11.8
8.9
6.4
6.5
6.4
8.1
10.9
9.2
Indo-European
23.6
17.0
19.3
16.7
17.9
18.6
20.3
20.9
Niger-Congo
18.9
16.0
12.7
14.7
12.8
N/A
N/A
N/A
Otomanguean
N/A
N/A
N/A
N/A
N/A
N/A
16.2
N/A
Trans-New Guinea
N/A
N/A
N/A
N/A
N/A
N/A
19.0
N/A
Table 20:
BLEU scores for NLLB-600M ﬁne-tuned
models on the Early OT task.
Table 19 shows BLEU scores for various minor-
prophet books with both the Early OT task (training
set includes the full NT) and the Late OT task (train-
ing set includes the full NT and OT books except
the minor prophets in the test set, shown below).
Table 20 shows BLEU scores for the NLLB
model on the Early OT task.
Table 21 shows various scoring metrics for the
Gospel Translation task, both with and without
related languages supplied.
Table 22 shows the performance of ﬁne-tuned
NLLB on the Epistle Translation task.
Table 23 shows the ﬁne-tuned NLLB model per-
formance on the NT Completion task.
Translation
Pairing
Gospel Translation (MAT)
(Without Related Language)
Gospel Translation (MAT)
(With Related Language)
BLEU
spBLEU
chrF3
BLEU
spBLEU
chrF3
Afro-Asiatic
30.2
35.8
49.7
28.5
33.8
48.0
Austronesian
33.7
36.2
52.6
36.2
39.0
54.2
Dravidian
18.2
35.1
58.1
19.4
36.5
58.7
Indo-European
36.5
44.5
59.9
36.0
44.2
60.1
Niger-Congo
21.7
29.7
53.7
21.1
28.7
52.2
Otomanguean
20.4
34.5
48.7
18.1
31.2
47.9
Sino-Tibetan
30.6
45.9
56.1
27.3
41.6
53.9
Trans-New Guinea
28.5
41.7
51.7
27.8
40.5
51.3
Table 21:
BLEU, spBLEU, and chrF3 scores for
NLLB-600M ﬁne-tuned models on Gospel Translation
(without Related Language) task and the Gospel Trans-
lation (with Related Language) task.

--- Page 20 ---

Translation
Pairing
Epistle Translation
(Without Related Language)
Epistle Translation
(With Related Language)
1TH
2TH
1TI
2TI
TIT
1TH
2TH
1TI
2TI
TIT
Afro-Asiatic
14.8
17.3
11.3
14.3
9.3
14.2
14.6
11.2
12.3
8.1
Austronesian
20.1
21.5
19.9
23.5
19.8
30.0
31.3
30.5
33.4
28.3
Dravidian
11.4
13.4
7.0
8.1
5.2
13.2
13.1
7.5
9.4
4.8
Indo-European
28.7
26.2
21.3
26.7
21.6
26.0
24.0
18.8
24.2
20.2
Niger-Congo
14.9
16.7
15.1
14.5
13.6
15.5
18.4
17.1
18.6
16.0
Otomanguean
16.2
14.0
15.5
13.1
15.6
14.2
13.1
15.4
13.4
14.0
Sino-Tibetan
18.8
17.2
16.2
18.2
18.3
18.3
18.9
15.7
16.6
14.4
Trans-New Guinea
18.7
20.5
16.9
17.6
15.0
16.8
20.4
13.7
13.6
14.8
Table 22:
BLEU scores for NLLB-600M ﬁne-tuned
models on Epistle Translation (without Related Lan-
guage) task and the Epistle Translation (with Related
Language) task.
Translation
Pairing
NT Completion
(Without Related Language)
NT Completion
(With Related Language)
ROM
REV
ROM
REV
BLEU
spBLEU
chrF3
BLEU
spBLEU
chrF3
BLEU
spBLEU
chrF3
BLEU
spBLEU
chrF3
Afro-Asiatic
18.9
28.2
43.7
16.0
25.6
43.3
19.4
29.1
44.3
16.2
25.1
43.7
Austronesian
23.2
27.3
44.9
28.6
33.3
50.3
31.5
35.0
50.7
40.1
44.0
58.0
Dravidian
12.8
29.3
53.1
13.7
31.9
54.6
12.6
29.5
53.1
14.6
32.6
55.7
Indo-European
30.0
38.2
56.1
29.2
38.1
54.3
29.1
37.9
55.5
28.4
37.7
54.2
Niger-Congo
20.1
29.9
54.6
23.5
32.3
55.3
22.3
32.1
57.1
23.4
31.1
56.2
Otomanguean
22.1
38.8
53.1
20.6
35.5
51.1
22.1
38.6
53.5
21.2
36.0
52.3
Sino-Tibetan
23.3
41.4
51.6
23.3
42.5
53.2
23.9
41.5
52.9
23.4
42.3
54.0
Trans-New Guinea
24.9
42.3
56.2
22.1
42.1
53.5
22.2
40.0
53.2
20.9
41.2
52.7
Table 23:
BLEU, spBLEU, and chrF3 scores for
NLLB-600M ﬁne-tuned models on NT Completion
(without Related Language) task and the NT Comple-
tion (with Related Language) task.

```
