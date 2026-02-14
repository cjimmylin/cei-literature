---
title: "2021-Bareket-Neural Modeling for Named Entities and Morphology NEMO2 - PDF Extract"
source_pdf: "2021-Bareket-Neural Modeling for Named Entities and Morphology NEMO2.pdf"
pages: 19
extracted_at: "2026-02-13T22:00:45.233498"
---

# PDF Extract: 2021-Bareket-Neural Modeling for Named Entities and Morphology NEMO2

**Source PDF:** 2021-Bareket-Neural Modeling for Named Entities and Morphology NEMO2.pdf
**Total Pages:** 19

---

## Content

```
--- Page 1 ---

Neural Modeling for Named Entities and Morphology (NEMO2)
Dan Bareket1,2 and Reut Tsarfaty1
1Bar Ilan University, Ramat-Gan, Israel
2Open Media and Information Lab (OMILab), The Open University of Israel, Israel
dbareket@gmail.com, reut.tsarfaty@biu.ac.il
Abstract
Named Entity Recognition (NER) is a fun-
damental NLP task, commonly formulated
as classiﬁcation over a sequence of tokens.
Morphologically-Rich Languages (MRLs)
pose a challenge to this basic formulation,
as the boundaries of Named Entities do not
necessarily coincide with token boundaries,
rather, they respect morphological bound-
aries. To address NER in MRLs we then
need to answer two fundamental questions,
namely, what are the basic units to be la-
beled, and how can these units be detected
and classiﬁed in realistic settings, i.e., where
no gold morphology is available. We em-
pirically investigate these questions on a
novel NER benchmark, with parallel token-
level and morpheme-level NER annotations,
which we develop for Modern Hebrew,
a morphologically rich-and-ambiguous lan-
guage. Our results show that explicitly mod-
eling morphological boundaries leads to im-
proved NER performance, and that a novel
hybrid architecture, in which NER precedes
and prunes morphological decomposition,
greatly outperforms the standard pipeline,
where morphological decomposition strictly
precedes NER, setting a new performance
bar for both Hebrew NER and Hebrew mor-
phological decomposition tasks.
1
Introduction
Named Entity Recognition (NER) is a fundamen-
tal task in the area of Information Extraction (IE),
in which mentions of Named Entities (NE) are ex-
tracted and classiﬁed in naturally-occurring texts.
This task is most commonly formulated as a se-
quence labeling task, where extraction takes the
form of assigning each input token with a label
that marks the boundaries of the NE (e.g., B,I,O),
and classiﬁcation takes the form of assigning la-
bels to indicate entity type (PER, ORG, LOC, etc.).
Despite a common initial impression from lat-
est NER performance, brought about by neural
models on the main English NER benchmarks
— CoNLL 2003 (Tjong Kim Sang, 2003) and
OntoNotes (Weischedel et al., 2013) — the NER
task in real-world settings is far from solved.
Speciﬁcally, NER performance is shown to greatly
diminish when moving to other domains (Luan
et al., 2018; Song et al., 2018), when address-
ing the long tail of rare, unseen, and new user-
generated entities (Derczynski et al., 2017), and
when handling languages with fundamentally dif-
ferent structure than English. In particular, there is
no readily available and empirically veriﬁed neu-
ral modeling strategy for Neural NER in those lan-
guages with complex word-internal structure, also
known as morphologically-rich languages.
Morphologically-rich languages (MRL) (Tsar-
faty et al., 2010; Seddah et al., 2013; Tsarfaty
et al., 2020) are languages in which substantial in-
formation concerning the arrangement of words
into phrases and the relations between them is
expressed at word level, rather than in a ﬁxed
word-order or a rigid structure.
The extended
amount of information expressed at word-level
and the morpho-phonological processes creating
these words result in high token-internal com-
plexity, which poses serious challenges to the ba-
sic formulation of NER as classiﬁcation of raw,
space-delimited, tokens. Speciﬁcally, while NER
in English is formulated as the sequence labeling
of space-delimited tokens, in MRLs a single to-
ken may include multiple meaning-bearing units,
henceforth morphemes, only some of which are
relevant for the entity mention at hand.
In this paper we formulate two questions con-
cerning neural modelling strategies for NER in
MRLs, namely: (i) what should be the granularity
of the units to be labeled? Space-delimited tokens
or ﬁner-grain morphological segments? and, (ii)
how can we effectively encode, and accurately de-
arXiv:2007.15620v2  [cs.CL]  10 May 2021

--- Page 2 ---

tect, the morphological segments that are relevant
to NER, and speciﬁcally in realistic settings, when
gold morphological boundaries are not available?
To empirically investigate these questions we
develop a novel parallel benchmark, containing
parallel token-level and morpheme-level NER an-
notations for texts in Modern Hebrew — a mor-
phologically rich and morphologically ambiguous
language, which is known to be notoriously hard
to parse (More et al., 2019; Tsarfaty et al., 2019).
Our results show that morpheme-based NER is
superior to token-based NER, which encourages
a segmentation-ﬁrst pipeline. At the same time,
we demonstrate that token-based NER improves
morphological segmentation in realistic scenarios,
encouraging a NER-ﬁrst pipeline.
While these
two ﬁndings may appear contradictory, we aim
here to offer a climax; a hybrid architecture where
the token-based NER predictions precede and
prune the space of morphological decomposition
options, while the actual morpheme-based NER
takes place only after the morphological decom-
position. We empirically show that the hybrid ar-
chitecture we propose outperforms all token-based
and morpheme-based model variants of Hebrew
NER on our benchmark, and it further outper-
forms all previously reported results on Hebrew
NER and morphological decomposition. Our er-
ror analysis further demonstrates that morpheme-
based models better generalize, that is, they con-
tribute to recognizing the long tail of entities un-
seen during training (out-of-vocabulary, OOV), in
particular those unseen entities that turn out to be
composed of previously seen morphemes.
The contribution of this paper is thus mani-
fold.
First, we deﬁne key architectural ques-
tions for Neural NER modeling in MRLs and
chart the space of modeling options.
Second,
we deliver a new and novel parallel benchmark
that allows one to empirically compare and con-
trast the morpheme vs. token modeling strate-
gies. Third, we show consistent advantages for
morpheme-based NER, demonstrating the impor-
tance of morphologically-aware modeling. Next
we present a novel hybrid architecture which
demonstrates an even further improved perfor-
mance on both NER and morphological decom-
position tasks. Our results for Hebrew present a
new bar on these tasks, outperforming the reported
state-of-the-art results on various benchmarks.1
1Data & code: https://github.com/OnlpLab/NEMO
2
Research Questions: NER for MRLs
In MRLs, words are internally complex, and word
boundaries do not generally coincide with the
boundaries of more basic meaning-bearing units.
This fact has critical ramiﬁcations for sequence
labeling tasks in MRLs in general, and for NER
in MRLs in particular. Consider, for instance, the
three-token Hebrew phrase in (1):2
(1) !Nטסנו מתאילנד לסי
tasnu
mithailand
lesin
ﬂew.1PL
from-Thailand
to-China
‘we ﬂew from Thailand to China’
It is clear that !/תאילנדthailand (Thailand) and
!N/סיsin (China) are NEs, and in English, each NE
is its own token. In the Hebrew phrase though,
neither NE constitutes a single token. In either
case, the NE occupies only one of two morphemes
in the token, the other being a case-assigning
preposition.
This simple example demonstrates
an extremely frequent phenomenon in MRLs such
as Hebrew, Arabic or Turkish, that the adequate
boundaries for NEs do not coincide with token
boundaries, and tokens must be segmented in or-
der to obtain accurate NE boundaries.3
The segmentation of tokens and the identiﬁca-
tion of adequate NE boundaries is however far
from trivial, due to complex morpho-phonological
and orthographic processes in some MRLs (Vania
et al., 2018; Klein and Tsarfaty, 2020). This means
that the morphemes that compose NEs are not nec-
essarily transparent in the character sequence of
the raw tokens. Consider for example phrase (2):
(2) !NהמרוZ לבית הלב
hamerotz
labayit
halavan
the-race
to-house.DEF
the-white
‘the race to the White House’
Here, the full form of the NE !N/ הבית הלבhabayit
halavan (the White House), is not present in the ut-
terances, only the sub-string !N/ בית הלבbayit hala-
van ((the) White House) is present in (2) — due to
2Glossing conventions are in accord with the Leipzig
Glossing Rules (Comrie et al., 2008).
3We use the term morphological segmentation (or seg-
mentation) to refer to splitting raw tokens into morphological
segments, each carrying a single Part-Of-Speech tag. That
is, we segment away prepositions, determiners, subordination
markers and multiple kinds of pronominal clitics, that attach
to their hosts via complex morpho-phonological processes.
Throughout this work, we use the terms morphological seg-
ment, morpheme, or segment interchangeably.

--- Page 3 ---

phonetic and orthographic processes suppressing
the deﬁnite article !/הha in certain environments.
In this and many other cases, it is not only that
NE boundaries do not coincide with token bound-
aries, they do not coincide with characters or sub-
strings of the token either. This calls for accessing
the more basic meaning-bearing units of the token,
that is, to decompose the tokens into morphemes.
Unfortunately though, the morphological de-
composition of surface tokens may be very chal-
lenging due to extreme morphological ambiguity.
The sequence of morphemes composing a token
is not always directly recoverable from its char-
acter sequence, and is not known in advance.4
This means that for every raw space-delimited to-
ken, there are many conceivable readings which
impose different segmentations, yielding different
sets of potential NE boundaries. Consider for ex-
ample the token !( לבניlbny) in different contexts:
(3) (a) !השרה לבני
hasara
livni
the-minister
[Livni]P ER
‘Minister [Livni]PER’
(b) !Zלבני גנ
le-beny
gantz
for-[Benny
Gantz]P ER
‘for [Benny Gantz]PER’
(c) !לבני היקר
li-bni
hayakar
for-son.POSS.1SG
the-dear
‘for my dear son’
(d) !לבני חימר
livney
kheymar
brick.CS
clay
‘clay bricks’
In (3a) the token !לבניis completely consumed
as a labeled NE. In (3b) !לבניis only partly con-
sumed by an NE, and in (3c) and (3d) the token
is entirely out of an NE context. In (3c) the to-
ken is composed of several morphemes, and in
(3d) it consists of a single morpheme. These are
only some of the possible decompositions of this
surface token, other alternatives may still be avail-
able. As shown by Goldberg and Tsarfaty (2008);
Green and Manning (2010); Seeker and Çetino˘glu
(2015); Habash and Rambow (2005); More et al.
(2019), and others, the correct morphological de-
composition becomes apparent only in the larger
4This ambiguity gets magniﬁed by the fact that Semitic
languages that use abjads, like Hebrew and Arabic, lack cap-
italization altogether and suppress all vowels (diacritics).
(syntactic or semantic) context. The challenge, in
a nutshell, is as follows: in order to detect accu-
rately NE boundaries, we need to segment the raw
token ﬁrst, however, in order to segment tokens
correctly, we need to know the greater semantic
content, including, e.g., the participating entities.
How can we break out of this apparent loop?
Finally, MRLs are often characterized by an ex-
tremely sparse lexicon, consisting of a long-tail of
out-of-vocabulary (OOV) entities unseen during
training (Czarnowska et al., 2019). Even in cases
where all morphemes are present in the training
data, morphological compositions of seen mor-
phemes may yield tokens and entities which were
unseen during training. Take for example the ut-
terance in (4), which the reader may inspect as fa-
miliar:
(4) !טסנו מסיN לתאילנד
tasnu
misin
lethailand
ﬂew.1PL
from-China
to-Thailand
’we ﬂew from China to Thailand’
Example (4) is in fact example (1) with a switched
ﬂight direction. This subtle change creates two
new surface tokens !Nלתאילנד! ,מסיwhich might
not have been seen during training, even if ex-
ample (1) had been observed.
Morphological
compositions of an entity with prepositions, con-
junctions, deﬁnite markers, possessive clitics and
more, cause mentions of seen entities to have un-
familiar surface forms, which often fail to be ac-
curately detected and analyzed.
Given the aforementioned complexities, in or-
der to solve NER for MRLs we ought to answer
the following fundamental modeling questions:
Q1. Units: What are the discrete units upon which
we need to set NE boundaries in MRLs? Are they
tokens? characters? morphemes? a representation
containing multiple levels of granularity?
Q2. Architecture: When employing morphemes
in NER, the classical approach is “segmentation-
ﬁrst".
However, segmentation errors are detri-
mental and downstream NER cannot recover from
them. How is it best to set up the pipeline so that
segmentation and NER could interact?
Q3. Generalization: How do the different mod-
eling choices affect NER generalization in MRLs?
How can we address the long tail of OOV NEs
in MRLs? Which modeling strategy best handles
pseudo-OOV entities that result from a previously
unseen composition of already seen morphemes?

--- Page 4 ---

3
Formalizing NER for MRLs
To answer the aforementioned questions, we chart
and formalize the space of modeling options for
neural NER in MRLs. We cast NER as a Sequence
Labelling task and formalize it as f : X →Y,
where x ∈X is a sequence x1, ..., xn of n dis-
crete strings from some vocabulary xi ∈Σ, and
y ∈Y is a sequence y1, .., yn of the same length,
where yi ∈Labels, and Labels is a ﬁnite set of la-
bels composed of the BIOSE tags (a.k.a., BIOLU
as described in Ratinov and Roth (2009)). Every
non-O label is also enriched with an entity type
label. Our list of types is presented in Table 2.
3.1
Token-Based or Morpheme-Based?
Our ﬁrst modeling question concerns the discrete
units upon which to set the NE boundaries. That
is, what is the formal deﬁnition of the input vocab-
ulary Σ for the sequence labeling task?
The simplest scenario, adopted in most NER
studies, assumes token-based input, where each
token admits a single label — hence token-single:
NERtoken-single : W →L
Here, W = {w∗|w ∈Σ} is the set of all possible
token sequences in the language and L = {l∗|l ∈
Labels} is the set of all possible label sequences
over the label set deﬁned above. Each token gets
assigned a single label, so the input and output se-
quences are of the same length. The drawback of
this scenario is that since the input for token-single
incorporates no morphological boundaries, the ex-
act boundaries of the NEs remain underspeciﬁed.
This case is exempliﬁed at the top row of Table 1.
There is another conceivable scenario, where
the input is again the sequence of space-delimited
tokens, and the output consists of complex la-
bels (henceforth multi-labels) reﬂecting, for each
token, the labels of its constituent morphemes;
henceforth, a token-multi scenario:
NERtoken-multi : W →L∗
Here, W = {w∗|w ∈Σ} is the set of sequences of
tokens as in token-single. Each token is assigned a
multi-label, i.e., a sequence (l∗∈L) which indi-
cates the labels of the token’s morphemes in order.
The output is a sequence of such multi-labels, one
multi-label per token. This variant incorporates
morphological information concerning the num-
ber and order of labeled morphemes, but lacks the
Nickname
Input
Lit
Output
token-single
!Zהמרוthe-race
O
!לביתto-house.DEF
B_ORG
!Nהלבthe-white
E_ORG
token-multi
!Zהמרוthe-race
O + O
!לביתto-house.DEF
O + B_ORG + I_ORG
!Nהלבthe-white
I_ORG + E_ORG
morpheme
!הthe
O
!Zמרוrace
O
!לto
O
!הthe
B_ORG
!ביתhouse
I_ORG
!הthe
I_ORG
!Nלבwhite
E-ORG
Table 1: Input/output for token-single, token-multi and
morpheme models for example (2) in Sec. 2.
precise morphological boundaries. This is illus-
trated at the middle of Table 1. A downstream ap-
plication may require (possibly noisy) heuristics to
determine the precise NE boundaries of each indi-
vidual label in the multi-label for an input token.
Another possible scenario is a morpheme-based
scenario, assigning a label l ∈L for each segment:
NERmorph : M →L
Here, M = {m∗|m ∈Morphemes} is the set of
sequences of morphological segments in the lan-
guage, and L = {l∗|l ∈Labels} is the set of label
sequences as deﬁned above. The upshot of this
scenario is that NE boundaries are precise. An ex-
ample is given in the bottom row of Table 1. But,
since each token may contain many meaningful
morphological segments, the length of the token
sequence is not the same as the length of morpho-
logical segments to be labeled, and the model as-
sumes prior morphological segmentation — which
in realistic scenarios is not necessarily available.
3.2
Realistic Morphological Decomposition
A major caveat with morpheme-based modeling
strategies is that they often assume an ideal sce-
nario of gold morphological decomposition of the
space-delimited tokens into morphological seg-
ments (cf. Nivre et al. (2007); Pradhan et al.
(2012)). But in reality, gold morphological de-
composition is not known in advance, it has to be
predicted automatically, and prediction errors may
propagate to contaminate the downstream task.
Our second modeling question therefore con-
cerns the interaction between the morphological
decomposition and the NER tasks: how would it
be best to set up the pipeline so that the prediction
of the two tasks can interact?

--- Page 5 ---

Figure 1: Lattice for a partial list of analyses of the He-
brew tokens !Nלבית הלבcorresponding to Table 1. Bold
nodes are token boundaries. Light nodes are segment
boundaries. Every path through the lattice is a single
morphological analysis. The bold path is a single NE.
To answer this, we deﬁne morphological de-
composition as consisting of two subtasks: mor-
phological analysis (MA) and morphological dis-
ambiguation (MD). We view sentence-based MA
as:
MA : W →P(M)
Here W = {w∗|w ∈Σ} is the set of possi-
ble token sequences as before, M = {m∗|m ∈
Morphemes} is the set of possible morpheme se-
quences, and P(M) is the set of subsets of M.
The role of MA is then to assign a token sequence
w ∈W with all of its possible morphological de-
composition options. We represent this set of al-
ternatives in a dense structure that we call a lattice
(exempliﬁed in Figure 1). MD is the task of pick-
ing the single correct morphological path M ∈M
through the MA lattice of a given sentence:
MD : P(M) →M
Now, assume x ∈W is a surface sentence in
the language, with its morphological decomposi-
tion initially unknown and underspeciﬁed. In a
Standard pipeline, MA strictly precedes MD:
MDStandard : M = MD(MA(x))
The main problem here is that MD errors may
propagate to contaminate the NER output.
We propose a novel Hybrid alternative, in which
we inject a task-speciﬁc signal, in this case NER,5
to constrain the search for M through the lattice:
MDHybrid : M = MD(MA(x) ↾NERtoken(x))
Here, the restriction MA(x) ↾NER(x) indi-
cates pruning the lattice structure MA(x) to con-
tain only MD options that are compatible with the
token-based NER predictions, and only then apply
MD to the pruned lattice.
5We can do this for any sequence labeling task in MRLs.
Both MDStandard and MDHybrid are disam-
biguation architectures that result in a morpheme
sequence M ∈M. The latter beneﬁts from the
NER signal, while the former doesn’t. The se-
quence M ∈M can be used in one of two ways.
We can use M as input to a morpheme model to
output morpheme labels. Or, we can rely on the
output of the token-multi model and align the to-
ken’s multi-label with the segments in M.
In what follows, we want to empirically assess
the effect of different modeling choices (token-
single, token-multi, morpheme) and disambigua-
tion architectures (Standard, Hybrid) on the per-
formance of NER in MRLs. To this end, we need
a corpus that allows training and evaluating NER
at both token and morpheme-level granularity.
4
The Data: A Novel NER Corpus
This work empirically investigates NER modeling
strategies in Hebrew, a Semitic language known
for its complex and highly ambiguous morphol-
ogy.
Ben-Mordecai (2005), the only previous
work on Hebrew NER to date, annotated space-
delimited tokens, basing their guidelines on the
CoNLL 2003 shared task (Chinchor et al., 1999).
Popular Arabic NER corpora also label space-
delimited tokens (ANERcorp (Benajiba et al.,
2007), AQMAR (Mohit et al., 2012), TWEETS
(Darwish, 2013)), with the exception of the Ara-
bic portion of OntoNotes (Weischedel et al., 2013)
and ACE (LDC, 2008) which annotate NER la-
bels on gold morphologically pre-segmented texts.
However, these works do not provide a compre-
hensive analysis on the performance gaps between
morpheme-based and token-based scenarios.
In agglutinative languages as Turkish, token
segmentation is always performed before NER
(Tür et al. (2003); Küçük and Can (2019), re-
enforcing the need to contrast the token-based sce-
nario, widely adopted for Semitic languages, with
the morpheme-based scenarios in other MRLs.
Our ﬁrst contribution is thus a parallel corpus
for Hebrew NER, one version consists of gold-
labeled tokens and the other consists of gold-
labeled morphemes, for the same text. For this,
we performed gold NE annotation of the Hebrew
Treebank (Sima’an et al., 2001), based on the
6,143 morpho-syntactically analyzed sentences of
the HAARETZ corpus, to create both token-level
and morpheme-level variants, as illustrated at the
topmost and lowest rows of Table 1, respectively.

--- Page 6 ---

Annotation Scheme
We started off with the
guidelines of Ben-Mordecai (2005), from which
we deviate in three main ways. First, we label NE
boundaries and their types on sequences of mor-
phemes, in addition to the space-delimited token
annotations.6 Secondly, we use the ﬁner-grained
entity categories list of ACE (LDC, 2008).7 Fi-
nally, we allow nested entity mentions, as in Finkel
and Manning (2009); Benikova et al. (2014).8
Annotation Cycle
As Fort et al. (2009) put it,
examples and rules would never cover all possible
cases because of the speciﬁcity of natural language
and the ambiguity of formulation. To address this
we employed the cyclic approach of agile annota-
tion as offered by Alex et al. (2010). Every cycle
consisted of: annotation, evaluation and curation,
clariﬁcation and reﬁnements. We used WebAnno
(Yimam et al., 2013) as our annotation interface.
The Initial Annotation Cycle was a two-stage pi-
lot with 12 participants, divided into 2 teams of
6. The teams received the same guidelines, with
the exception of the speciﬁcations of entity bound-
aries. One team was guided to annotate the mini-
mal string that designates the entity. The other was
guided to tag the maximal string which can still be
considered as the entity. Our agreement analysis
showed that the minimal guideline generally led to
more consistent annotations. Based on this result
(as well as low-level reﬁnements) from the pilot,
we devised the full version of the guidelines.9
Annotation, Evaluation and Curation: Every
annotation cycle was performed by two annotators
(A, B) and an annotation manager/curator (C). We
annotated the full corpus in 7 cycles. We eval-
uated the annotation in two ways, manual cura-
tion and automatic evaluation. After each anno-
tation step, the curator manually reviewed every
sentence in which disagreements arose, as well
as speciﬁc points of difﬁculty pointed out by the
annotators.
The inter-annotator agreement met-
ric described below was also used to quantitatively
gauge the progress and quality of the annotation.
6A single NE is always continuous. Token-morpheme dis-
crepancies do not lead to discontinuous NEs.
7Entity categories are listed in Table 2. We dropped the
NORP category, since it introduced complexity concerning
the distinction between adjectives and group names. LAW
did not appear in our corpus.
8Nested labels are are not modeled in this paper, but they
are published with the corpus, to allow for further research.
9The complete annotation guide is publicly available at
https://github.com/OnlpLab/NEMO-Corpus.
train
dev
test
Sentences
4, 937
500
706
Tokens
93, 504
8, 531
12, 619
Morphemes
127, 031
11, 301
16, 828
All mentions
6, 282
499
932
Type: Person (PER)
2, 128
193
267
Type: Organization (ORG)
2, 043
119
408
Type: Geo-Political (GPE)
1, 377
121
195
Type: Location (LOC)
331
28
41
Type: Facility (FAC)
163
12
11
Type: Work-of-Art (WOA)
114
9
6
Type: Event (EVE)
57
12
0
Type: Product (DUC)
36
2
3
Type: Language (ANG)
33
3
1
Table 2: Basic Corpus Statistics. Standard HTB Splits.
Clariﬁcations and Reﬁnements: In the end of
each cycle we held a clariﬁcation talk between A,
B and C, in which issues that came up during the
cycle were discussed. Following that talk we re-
ﬁned the guidelines and updated the annotators,
which went on to the next cycle. In the end we per-
formed a ﬁnal curation run to make sentences from
earlier cycles comply with later reﬁnements.10
Inter-Annotator Agreement (IAA) IAA is
commonly measured using κ-statistic. However,
Pyysalo et al. (2007) show that it is not suitable
for evaluating inter-annotator agreement in NER.
Instead, an F1 metric on entity mentions has in re-
cent years been adopted for this purpose (Zhang,
2013). This metric allows for computing pair-wise
IAA using standard F1 score by treating one anno-
tator as gold and the other as the prediction.
Our full corpus pair-wise F1
scores are:
IAA(A,B)=89, IAA(B,C)=92, IAA(A,C)=96. Ta-
ble 2 presents ﬁnal corpus statistics.
Annotation Costs The annotation took on av-
erage about 35 seconds per sentence, and thus a
total of 60 hours for all sentences in the corpus for
each annotator. Six clariﬁcation talks were held
between the cycles, which lasted from thirty min-
utes to an hour. Giving a total of about 130 work
hours of expert annotators.11
5
Experimental Settings
Goal
We set out to empirically evaluate the rep-
resentation alternatives for the input/output se-
quences (token-single, token-multi, morpheme)
and the effect of different architectures (Standard,
Hybrid) on the performance of NER for Hebrew.
10A, B and C annotations are published to enable research
on learning with disagreements (Plank et al., 2014).
11The corpus is available at https://github.com/
OnlpLab/NEMO-Corpus.

--- Page 7 ---

Figure 2:
The token-single and token-multi Models.
The input and output correspond to rows 1,2 in Tab. 1.
Triangles indicate string embeddings. Circles indicate
char-based encoding.
Modeling Variants
All experiments use the cor-
pus we just described and employ a standard
Bi-LSTM-CRF architecture for implementing the
neural sequence labeling task (Huang et al., 2015).
Our basic architecture12 is composed of an embed-
ding layer for the input and a 2-layer Bi-LSTM
followed by a CRF inference layer — for which
we test three modeling variants.
Figures 2–3 present the variants we employ.
Figure 2 shows the token-based variants, token-
single and token-multi. The former outputs a sin-
gle BIOSE label per token, and the latter outputs a
multi-label per token — a concatenation of BIOSE
labels of the morphemes composing the token.
Figure 3 shows the morpheme-based variant for
the same input phrase. It has the same basic archi-
tecture, but now the input consists of morphologi-
cal segments instead of tokens. The model outputs
a single BIOSE label for each morphological seg-
ment in the input.
In all modeling variants, the input may be en-
coded in two ways: (a) String-level embeddings
(token-based or morpheme-based) optionally ini-
tialized with pre-trained embeddings. (b) Char-
level embeddings, trained simultaneously with the
main task (cf. Ma and Hovy (2016); Chiu and
Nichols (2015); Lample et al. (2016)). For char-
based encoding (of either tokens or morphemes)
12Using the NCRF++ suite of Yang and Zhang (2018).
Figure 3: The morpheme Model. The input and output
correspond to row 3 in Tab. 1. Triangles indicate string
embeddings. Circles indicate char-based encoding.
we experiment with CharLSTM, CharCNN or
NoChar, that is, no character embedding at all.
We pre-trained all token-based or morpheme-
based embeddings on the Hebrew Wikipedia
dump of Goldberg (2014). For morpheme-based
embeddings, we decompose the input using More
et al. (2019), and use the morphological seg-
ments as the embedding units.13
We compare
GloVe (Pennington et al., 2014) and fastText (Bo-
janowski et al., 2017). We hypothesize that since
FastText uses sub-string information, it will be
more useful for analyzing OOVs.
Hyper
parameters
Following
Reimers
and
Gurevych (2017); Yang et al. (2018), we per-
formed hyper-parameter tuning for each of our
model variants.
We performed hyper-parameter
tuning on the dev set in a number of rounds of ran-
dom search, independently on every input/output
and char-embedding architecture. Table 3 shows
our selected hyper-parameters.14 The Char CNN
window size is particularly interesting as it was
13Embeddings and Wikipedia corpus also available in:
https://github.com/OnlpLab/NEMO
14A few interesting empirical observations diverging from
those of Reimers and Gurevych (2017); Yang et al. (2018) are
worth mentioning. We found that a lower Learning Rate than
the one recommended by Yang et al. (2018) (0.015), led to
better results and less occurrences of divergence. We further
found that raising the number of Epochs from 100 to 200 did
not result in over-ﬁtting, and signiﬁcantly improved NER re-
sults. We used for evaluation the weights from the best epoch.

--- Page 8 ---

Parameter
Value
Parameter
Value
Optimizer
SGD
*LR (token-single)
0.01
*Batch Size
8
*LR (token-multi)
0.005
LR decay
0.05
*LR (morpheme)
0.01
Epochs
200
Dropout
0.5
Bi-LSTM layers
2
*CharCNN window
7
*Word Emb Dim
300
Char Emb dim
30
Word Hidden Dim
200
*Char Hidden Dim
70
Table 3: Summary of Hyper-Parameter Tuning. The *
indicates divergence from the NCRF++ proposed setup
and empirical ﬁndings (Yang and Zhang, 2018).
not treated as a hyper-parameter in Reimers and
Gurevych (2017), Yang et al. (2018). However,
given the token-internal complexity in MRLs we
conjecture that the window size over characters
might make a crucial effect. In our experiments
we found that a larger window (7) increased the
performance. For MRLs, further research into this
hyper-parameter might be of interest.
Evaluation
Standard NER studies typically in-
voke the CoNLL evaluation script that anchors
NEs in token positions (Tjong Kim Sang, 2003).
However, it is inadequate for our purposes because
we want to compare entities across token-based vs.
morpheme-based settings. To this end, we use a
revised evaluation procedure, which anchors the
entity in its form rather than its index. Speciﬁ-
cally, we report F1 scores on strict, exact-match of
the surface forms of the entity mentions. I.e., the
gold and predicted NE spans must exactly match
in their form, boundaries, and entity type. In all
experiments, we report both token-level F-scores
and morpheme-level F-scores, for all models.
• Token-Level evaluation.
For the sake of
backwards compatibility with previous work
on Hebrew NER, we ﬁrst deﬁne token-level
evaluation. For token-single this is a straight-
forward calculation of F1 against gold spans.
For token-multi and morpheme, we need to
map the predicted label sequence of that to-
ken to a single label, and we do so using
linguistically-informed rules we devise (as
elaborated in Appendix A).15
• Morpheme-Level evaluation. Our ultimate
goal is to obtain precise boundaries of the
NEs. Thus, our main metric evaluates NEs
15In the morpheme case we might encounter “illegal” label
sequences in case of a prediction error. We employ similar
linguistically-informed heuristics to recover from that (See
Appendix A).
against the gold morphological boundaries.
For morpheme and token-single models, this
is a straightforward F1 calculation against
gold spans. Note for token-single we are ex-
pected to pay a price for boundary mismatch.
For token-multi, we know the number and or-
der of labels, so we align the labels in the
multi-label of the token with the morphemes
in its morphological decomposition.16
For all experiments and metrics, we report mean
and conﬁdence interval (0.95) over ten runs.
Input-Output Scenarios
We experiment with
two kinds of input settings: token-based, where the
input consists of the sequence of space-delimited
tokens, and morpheme-based, where the input
consists of morphological segments. For the mor-
pheme input, there are three input variants:
(i) Morph-gold: where the morphological se-
quence is produced by an expert (idealistic).
(ii) Morph-standard:
where the morpho-
logical sequence is produced by a standard
segmentation-ﬁrst pipeline (realistic).
(iii) Morph-hybrid: where the morphological
sequence is produced by the hybrid architec-
ture we propose (realistic).
In
the
token-multi
case
we
can
perform
morpheme-based evaluation by aligning individ-
ual labels in the multi-label with the morpheme
sequence of the respective token. Again we have
three options as to which morphemes to use:
(i) Tok-multi-gold: The multi-label is aligned
with morphemes produced by an expert (ide-
alistic).
(ii) Tok-multi-standard: The multi-label is
aligned with morphemes produced by a stan-
dard pipeline (realistic).
(iii) Tok-multi-hybrid:
The multi-label is
aligned with morphemes produced by the hy-
brid architecture we propose (realistic).
Pipeline Scenarios
Assume an input sentence x.
In the Standard pipeline we use YAP,17 the cur-
rent state-of-the-art morpho-syntactic parser for
Hebrew (More et al., 2019), for the predicted seg-
mentation M = MD(MA(x)). In the Hybrid
16In case of a misalignment (in the number of morphemes
and labels) we match the label-morpheme pairs from the ﬁnal
one backwards, and pad unpaired morphemes with O labels.
17For other languages this may be done using models for
canonical segmentation as in (Kann et al., 2016).

--- Page 9 ---

Figure 4: Token-level Eval. on Dev w/ Gold Segmen-
tation. CharCNN for morph, CharLSTM for tok.
Figure 5: Morph-Level Eval. on Dev w/ Gold Segmen-
tation. CharCNN for morph, CharLSTM for tok.
pipeline, we use YAP to ﬁrst generate complete
morphological lattices MA(x). Then, to obtain
MA(x) ↾NER(x) we omit lattice paths where
the number of morphemes in the token decompo-
sition does not conform with the number of labels
in the multi-label of NERtoken-multi(x). Then, we
apply YAP to obtain MD(MA(x) ↾NER(x))
on the constrained lattice. In predicted morphol-
ogy scenarios (either Standard or Hybrid), we use
the same model weights as trained on the gold seg-
ments, but feed predicted morphemes as input.18
6
Results
6.1
The Units: Tokens vs. Morphemes
Figure 4 shows the token-level evaluation for the
different model variants we deﬁned.
We see
that morpheme models perform signiﬁcantly better
than the token-single and token-multi variants. In-
18We do not re-train the morpheme models with predicted
segmentation, which might achieve better performance (e.g..
jackkniﬁng). We leave this for future work.
Figure 6:
Token-Level Evaluation in Realistic Sce-
narios on Dev, comparing Gold, Standard and Hybrid
Morphology.
CharCNN for morph, CharLSTM for
tok. Results for Gold, token-single and token-multi are
taken from Fig 4.
Figure 7:
Morph-Level Evaluation in Realistic Sce-
narios on Dev, comparing Gold, Standard and Hybrid
Morphology.
CharCNN for morph, CharLSTM for
tok. Results for Gold, token-single and token-multi are
taken from Fig 5.
terestingly, explicit modeling of morphemes leads
to better NER performance even when evaluated
against token-level boundaries. As expected, the
performance gaps between variants are smaller
with fastText than they are with embeddings that
are unaware of characters (GloVe) or with no pre-
training at all. We further pursue this in Sec. 6.3.
Figure 5 shows the morpheme-level evaluation
for the same model variants as in Table 4. The
most obvious trend here is the drop in the per-
formance of the token-single model. This is ex-
pected, reﬂecting the inadequacy of token bound-
aries for identifying accurate boundaries for NER.
Interestingly, morpheme and token-multi models
keep a similar level of performance as in token-
level evaluation, only slightly lower. Their per-

--- Page 10 ---

Figure 8:
Entity Mention Counts and Ratio by Cate-
gory and OOTV Category, for Dev Set.
formance gap is also maintained, with morpheme
performing better than token-multi. An obvious
caveat is that these results are obtained with gold
morphology. What happens in realistic scenarios?
6.2
The Architecture: Pipeline vs. Hybrid
Figure 6 shows the token-level evaluation results
in realistic scenarios. We ﬁrst observe a signiﬁcant
drop for morpheme models when Standard pre-
dicted segmentation is introduced instead of gold.
This means that MD errors are indeed detrimen-
tal for the downstream task, in a non-negligible
rate. Second, we observe that much of this perfor-
mance gap is recovered with the Hybrid pipeline.
It is noteworthy that while morph hybrid lags be-
hind morph gold, it is still consistently better than
token-based models, token-single and token-multi.
Figure 7 shows morpheme-level evaluation re-
sults for the same scenarios as in Table 6.
All
trends from the token-level evaluation persist, in-
cluding a drop for all models with predicted seg-
mentation relative to gold, with the hybrid variant
recovering much of the gap. Again morph gold
outperforms token-multi, but morph hybrid shows
great advantages over all tok-multi variants. This
performance gap between morph (gold or hybrid)
and tok-multi indicates that explicit morphological
modeling is indeed crucial for accurate NER.
6.3
Morphologically-Aware OOV Evaluation
As discussed in Section 2, morphological compo-
sition introduces an extremely sparse word-level
“long-tail” in MRLs. In order to gauge this phe-
nomenon and its effects on NER performance,
we categorize unseen, out-of-training-vocabulary
(OOTV) mentions into 3 categories:
Figure 9:
Token-Level Eval on Dev by OOTV Cate-
gory. Using fastText and CharLSTM.
• Lexical: Unknown mentions caused by an
unknown token which consists of a single
morpheme. This is a strictly lexical unknown
with no morphological composition (most
English unknowns are in this category).
• Compositional: Unknown mentions caused
by an unknown token which consists of mul-
tiple known morphemes.
These are un-
knowns introduced strictly by morphological
composition, with no lexical unknowns.
• LexComp: Unknown mentions caused by an
unknown token consisting of multiple mor-
phemes, of which (at least) one morpheme
was not seen during training. In such cases,
both unknown morphological composition
and lexical unknowns are involved.
We group NEs based on these categories, and
evaluate each group separately. We consider men-
tions that do not fall into any category as Known.
Figure 8 shows the distributions of entity men-
tions in the dev set by entity type and OOTV cat-
egory. OOTV categories that involve composition
(Comp and LexComp) are spread across all cate-
gories but one, and in some they even make up
more than half of all mentions.
Figure 9 shows token-level evaluation19 with
fastText embeddings, grouped by OOTV type. We
ﬁrst observe that indeed unknown NEs that are due
to morphological composition (Comp and Lex-
Comp) proved the most challenging for all models.
We also ﬁnd that in strictly Compositional OOTV
19This section focuses on token-level evaluation, which is
a permissive evaluation metric, allowing us to compare the
models on a more level playing ﬁeld, where all models (in-
cluding token-single) have an equal opportunity to perform.

--- Page 11 ---

mentions, morpheme-based models exhibit their
most signiﬁcant performance advantage, support-
ing the hypothesis that explicit morphology helps
to generalize. We ﬁnally observe that token-multi
models perform better than token-single models
for these NEs (in contrast with the trend for non-
compositional NEs).
This corroborates the hy-
pothesis that even partial modeling of morphology
(as in token-multi compared to token-single) is bet-
ter than none, leading to better generalization.
String-level vs. Character-level Embeddings
To further understand the generalization capacity
of different modeling alternatives in MRLs, we
probe into the interplay of string-based and char-
based embeddings in treating OOTV NEs.
Figure 10 presents 12 plots, each of which
presents the level of performance (y-axes) for all
models (x-axes). Token-based models are on the
left of each x-axes, morpheme-based are on the
right. We plot results with and without charac-
ter embeddings,20 in orange and blue respectively.
The plots are organized in a large grid, with the
type of NE on the y-axes (Known, Lex, Comp, Lex-
Comp), and the type of pre-training on the x-axes
(No pre-training, GloVe, fastText) .
At the top-most row, plotting the accuracy for
Known NEs, we see a high level of performance
for all pre-training methods, with not much dif-
ferences between the type of pre-training, with
or without the character embeddings.
Moving
further down to the row of Lexical unseen NEs,
char-based representations lead to signiﬁcant ad-
vantages when we assume no pre-training, but
with GloVe pre-training the performance substan-
tially increases, and with fastText the differences
in performance with/without char-embeddings al-
most entirely diminish, indicating the char-based
embeddings are somewhat redundant in this case.
The two lower rows in the large grid show the
performance for Comp and LexComp unseen NEs,
which are ubiquitous in MRLs. For Compositional
NEs, pre-training closes only part of the gap be-
tween token-based and morpheme-based models.
Adding char-based representations indeed helps
the token-based models, but crucially does not
close the gap with the morpheme-based variants.
Finally, for LexComp NEs at the lowest row, we
again see that adding GloVe pre-training and char-
based embeddings does not close the gap with
20For brevity we only show char LSTM (vs. no char repre-
sentation), there was no signiﬁcant difference with CNN.
Eval
Model
dev
test
Morph-
morph gold
80.03 ± 0.4
79.10 ± 0.6
Level
morph hybrid
78.51 ± 0.5
77.11 ± 0.7
morph standard
72.79 ± 0.5
69.52 ± 0.6
token-multi hybrid
75.70 ± 0.5
74.64 ± 0.3
Token-
morph gold
80.30 ± 0.5
79.28 ± 0.6
Level
morph hybrid
79.04 ± 0.5
77.64 ± 0.7
morph standard
74.52 ± 0.7
73.53 ± 0.8
token-multi
77.59 ± 0.4
77.75 ± 0.3
token-single
78.15 ± 0.3
77.15 ± 0.6
Table 4:
Test vs. Dev: Results with fastText for all
Models. morph-gold presents an ideal upper-bound.
morpheme-based models, indicating that not all
morphological information is captured by these
vectors.
For fastText with char-based embed-
dings the gap between token-multi and morpheme
greatly diminishes, but is still well above token-
single. This suggests biasing the model to learn
about morphology (either via multi-labels or by
incorporating morphological boundaries) has ad-
vantages for analysing OOTV entities, beyond the
contribution of char-based embeddings alone.
All in all, the biggest advantage of morpheme-
based models over token-based models is their
ability
to
generalize
from
observed
tokens
to composition-related OOTV (Comp/LexComp).
While character-based embeddings do help token-
based models generalize, the contribution of mod-
eling morphology is indispensable, above and be-
yond the contribution of char-based embeddings.
6.4
Setting in the Greater Context
Test Set Results
Table 4 conﬁrms our best re-
sults on the Test set. The trends are kept, though
results on Test are lower than on Dev. The morph
gold scenario still provides an upperbound of the
performance, but it is not realistic. For the realistic
scenarios, morph hybrid generally outperforms all
other alternatives. The only divergence is that in
token-level evaluation, token-multi performs on a
par with morph hybrid on the Test set.
Results
on
MD
Tasks.
While
the
Hybrid
pipeline achieves superior performance on NER,
it also improves the state-of-the-art on other tasks
in the pipeline. Table 5 shows the Seg+POS results
of our Hybrid pipeline scenario, compared with
the Standard pipeline which replicates the pipeline
of More et al. (2019). We use the metrics deﬁned
by More et al. (2019). We show substantial im-
provements for the Hybrid pipeline over the results
of More et al. (2019), and also outperforming the
Test results of Seker and Tsarfaty (2020).

--- Page 12 ---

Figure 10: Token-Level Eval. on Dev for Different OOTV Types, Char- and Word-Embeddings.
Seg+POS
dev
Standard (More et al., 2019)
92.36
Ptr-Network (Seker and Tsarfaty, 2020)
93.90
Hybrid (This work)
93.12
test
Standard (More et al., 2019)
89.08
Ptr-Network (Seker and Tsarfaty, 2020)
90.49
Hybrid (This work)
90.89
Table 5: Morphological Segmentation & POS scores.
Comparison with Prior Art.
Table 6 presents
our results on the Hebrew NER corpus of Ben-
Mordecai (2005) compared to their model, which
uses a hand-crafted feature-engineered MEMM
with regular-expression rule-based enhancements
and an entity lexicon. Like Ben-Mordecai (2005)
Precision
Recall
F1
Ben-Mordecai (2005)
84.54
74.31
79.10
MEMM+HMM+REGEX
This work
86.84
82.6
84.71
token-single +FT+CharLSTM
±0.5
±0.9
±0.5
This work
86.93
83.59
85.22
morph-Hybrid +FT+CharLSTM
±0.6
±0.8
±0.5
Table 6: NER Comparison with Ben-Mordecai (2005).
we performed three 75%-25% random train/test
splits, and used the same seven NE categories
(PER,LOC,ORG,TIME,DATE,PERCENT,MONEY).
We trained a token-single model on the original
space-delimited tokens and a morpheme model on
automatically segmented morphemes we obtained

--- Page 13 ---

using our best segmentation model (Hybrid MD
on our trained token-multi model, as in Table 5).
Since their annotation includes only token-level
boundaries, all of the results we report conform
with token-level evaluation.
Table 6 presents the results of these experi-
ments. Both models signiﬁcantly outperform the
previous state-of-the-art by Ben-Mordecai (2005),
setting a new performance bar on this earlier
benchmark. Moreover, we again observe an em-
pirical advantage when explicitly modeling mor-
phemes, even with the automatic noisy segmenta-
tion that is used for the morpheme-based training.
7
Discussion: Joint Modeling
Alternatives and Future Work
The present study provides the motivation and the
necessary foundations for comparing morpheme-
based and token-based modeling for NER. While
our ﬁndings clearly demonstrate the advantages of
morpheme-based modeling for NER in a morpho-
logically rich language, it is clear that our pro-
posed Hybrid architecture is not the only modeling
alternative for linking NER and morphology.
For example, a previous study by Güngör
et al. (2018) addresses joint neural modeling of
morphological segmentation and NER labeling,
proposing a multi-task learning (MTL) approach
for joint MD and NER in Turkish. They employ
separate Bi-LSTM networks for the MD and NER
tasks, with a shared loss to allow for joint learning.
Their results indicate improved NER performance,
with no improvement in the MD results. Contrary
to our proposal, they view MD and NER as dis-
tinct tasks, assuming a single NER label per token,
and not providing disambiguated morpheme-level
boundaries for the NER task. More generally, they
test only token-based NER labeling and do not at-
tend to the question of input/output granularity in
their models.
A different approach for joint NER and mor-
phology is jointly predicting the segmentation
and labels for each token in the input stream.
This is the approach taken, for instance, by the
lattice-based Pointer-Network of Seker and Tsar-
faty (2020). As shown in Table 5, their results for
morphological segmentation and POS tagging are
on a par with our reported results and, at least in
principle, it should be possible to extend the Seker
and Tsarfaty (2020) approach to yield also NER
predictions.
However, our preliminary experiments with a
lattice-based Pointer-network for token segmen-
tation and NER labeling shows that this is not a
straightforward task. Contrary to POS tags, which
are constrained by the MA, every NER label can
potentially go with any segment, and this leads to
a combinatorial explosion of the search space rep-
resented by the lattice. As a result, the NER pre-
dictions are brittle to learn, and the complexity of
the resulting model is computationally prohibitive.
A different approach to joint sequence segmen-
tation and labeling can be applying the neural
model directly on the character-sequence of the
input stream.
Such an approach is for instance
the char-based labeling as segmentation setup pro-
posed by Shao et al. (2017).
Shao et al. use a
character-based Bi-RNN-CRF to output a single
label-per-char which indicates both word bound-
ary (using BIES sequence labels) and the POS
tags. This method is also used in their universal
segmentation paper, (Shao et al., 2018). However,
as seen in the results of Shao et al. (2018), char-
based labeling for segmenting Semitic languages
lags far behind all other languages, precisely be-
cause morphological boundaries are not explicit in
the character sequences.
Additional proposals are those of Kong et al.
(2015); Kemos et al. (2019). First, Kong et al.
(2015) proposed to solve e.g. Chinese segmen-
tation and POS tagging using dynamic program-
ming with neural encoding, by using a Bi-LSTM
to encode the character input, and then feed it
to a semi-markov CRF to obtain probabilities for
the different segmentation options. Kemos et al.
(2019) propose an approach similar to Kong et al.
(2015) for joint segmentation and tagging but add
convolution layers on top of the Bi-LSTM encod-
ings to obtain segment features hierarchically and
then feed them to the semi-markov CRF.
Preliminary experiments we conducted conﬁrm
that char-based joint segmentation and NER label-
ing for Hebrew, either using char-based labeling
or a seq2seq architecture, still lags behind our re-
ported results. We conjecture that this is due to the
complex morpho-phonological and orthographic
processed in Semitic languages. Going into char-
based modeling nuances and offering a sound joint
solution for a language like Hebrew is an impor-
tant matter that merits its own investigation. Such
work is feasible now given the new corpus, how-
ever, it is out of the scope of the current study.

--- Page 14 ---

All in all, the design of sophisticated joint mod-
eling strategies for morpheme-based NER poses
fascinating questions — for which our work pro-
vides a solid foundation (data, protocols, metrics,
strong baselines). More work is needed for inves-
tigating joint modeling of NER and morphology,
in the directions portrayed in this Section, yet it is
beyond the scope of this paper, and we leave this
investigation for future work.
Finally, while the joint approach is appealing,
we argue that the elegance of our Hybrid solution
is precisely in providing a clear and well-deﬁned
interface between MD and NER through which the
two tasks can interact, while still keeping the dis-
tinct models simple, robust, and efﬁciently train-
able. It also has the advantage of allowing us to
seamlessly integrate sequence labelling with any
lattice-based MA, in a plug-and-play language-
agnostic fashion, towards obtaining further advan-
tages on both of these tasks.
8
Conclusion
This work addresses the modeling challenges of
Neural NER in MRLs. We deliver a parallel token-
vs-morpheme NER corpus for Modern Hebrew,
that allows one to assess NER modeling strate-
gies in morphologically rich-and-ambiguous en-
vironments.
Our experiments show that while
NER beneﬁts from morphological decomposition,
downstream results are sensitive to segmentation
errors. We thus propose a Hybrid architecture in
which NER precedes and prunes the morpholog-
ical decomposition.
This approach greatly out-
performs a Standard
pipeline in realistic (non-
gold) scenarios. Our analysis further shows that
morpheme-based models better recognize OOVs
that result from morphological composition. All
in all we deliver new state-of-the-art results for
Hebrew NER and MD, along with a novel bench-
mark, to encourage further investigation into the
interaction between NER and morphology.
Acknowledgments
We are grateful to the BIU-NLP lab members as
well as 6 anonymous reviewers for their insight-
ful remarks. We further thank Daphna Amit and
Zef Segal for their meticulous annotation and pro-
found discussions. This research is funded by an
ISF Individual Grant (1739/26) and an ERC Start-
ing Grant (677352), for which we are grateful.
References
Bea Alex, Claire Grover, Rongzhou Shen, and Mi-
jail Kabadjov. 2010. Agile corpus annotation
in practice: An overview of manual and auto-
matic annotation of CVs. In Proceedings of the
Fourth Linguistic Annotation Workshop, pages
29–37, Uppsala, Sweden. Association for Com-
putational Linguistics.
Naama Ben-Mordecai. 2005. Hebrew named en-
tity recognition. Master’s thesis, Department of
Computer Science, Ben-Gurion University.
Yassine Benajiba, Paolo Rosso, and José Miguel
BenedíRuiz. 2007. Anersys: An arabic named
entity recognition system based on maximum
entropy.
In Computational Linguistics and
Intelligent Text Processing, pages 143–153,
Berlin, Heidelberg. Springer Berlin Heidelberg.
Darina Benikova,
Chris Biemann,
and Marc
Reznicek. 2014.
NoSta-D named entity an-
notation for German: Guidelines and dataset.
In Proceedings of the Ninth International Con-
ference on Language Resources and Evalua-
tion (LREC-2014), pages 2524–2531, Reyk-
javik, Iceland. European Languages Resources
Association (ELRA).
Piotr Bojanowski, Edouard Grave, Armand Joulin,
and Tomas Mikolov. 2017. Enriching word vec-
tors with subword information. Transactions of
the Association for Computational Linguistics,
5:135–146.
N. Chinchor, E. Brown, L. Ferro, and P. Robinson.
1999. Named entity recognition task deﬁnition.
Technical Report Version 1.4, The MITRE Cor-
poration and SAIC.
Jason P. C. Chiu and Eric Nichols. 2015. Named
entity recognition with bidirectional lstm-cnns.
CoRR, abs/1511.08308.
Bernard
Comrie,
Martin
Haspelmath,
and
Balthasar Bickel. 2008.
The leipzig glossing
rules: Conventions for interlinear morpheme-
by-morpheme glosses. Department of Linguis-
tics of the Max Planck Institute for Evolutionary
Anthropology & the Department of Linguistics
of the University of Leipzig.
Paula Czarnowska, Sebastian Ruder, Edouard
Grave, Ryan Cotterell, and Ann Copestake.

--- Page 15 ---

2019. Don’t forget the long tail! a comprehen-
sive analysis of morphological generalization in
bilingual lexicon induction. In Proceedings of
the 2019 Conference on Empirical Methods in
Natural Language Processing and the 9th Inter-
national Joint Conference on Natural Language
Processing (EMNLP-IJCNLP), pages 974–983,
Hong Kong, China. Association for Computa-
tional Linguistics.
Kareem Darwish. 2013. Named entity recognition
using cross-lingual resources: Arabic as an ex-
ample. In Proceedings of the 51st Annual Meet-
ing of the Association for Computational Lin-
guistics (Volume 1: Long Papers), pages 1558–
1567, Soﬁa, Bulgaria. Association for Compu-
tational Linguistics.
Leon Derczynski, Eric Nichols, Marieke van Erp,
and Nut Limsopatham. 2017.
Results of the
WNUT2017 shared task on novel and emerging
entity recognition.
In Proceedings of the 3rd
Workshop on Noisy User-generated Text, pages
140–147, Copenhagen, Denmark. Association
for Computational Linguistics.
Jenny Rose Finkel and Christopher D. Manning.
2009. Nested named entity recognition. In Pro-
ceedings of the 2009 Conference on Empirical
Methods in Natural Language Processing: Vol-
ume 1 - Volume 1, EMNLP ’09, pages 141–150,
Stroudsburg, PA, USA. Association for Compu-
tational Linguistics.
Karën
Fort,
Maud
Ehrmann,
and
Adeline
Nazarenko. 2009. Towards a methodology for
named entities annotation.
In Proceedings of
the Third Linguistic Annotation Workshop (LAW
III), pages 142–145, Suntec, Singapore. Associ-
ation for Computational Linguistics.
Yoav Goldberg. 2014. Hebrew wikipedia depen-
dency parsed corpus, v.1.0. Technical Report
V.1.0.
Yoav Goldberg and Reut Tsarfaty. 2008. A single
generative model for joint morphological seg-
mentation and syntactic parsing.
In Proceed-
ings of ACL-08: HLT, pages 371–379, Colum-
bus, Ohio. Association for Computational Lin-
guistics.
Spence Green and Christopher D. Manning. 2010.
Better Arabic parsing: Baselines, evaluations,
and analysis.
In Proceedings of the 23rd In-
ternational Conference on Computational Lin-
guistics (Coling 2010), pages 394–402, Beijing,
China. Coling 2010 Organizing Committee.
Onur Güngör,
Suzan Üsküdarli,
and Tunga
Güngör. 2018. Improving named entity recog-
nition by jointly learning to disambiguate mor-
phological tags. CoRR, abs/1807.06683.
Nizar Habash and Owen Rambow. 2005. Arabic
tokenization, part-of-speech tagging and mor-
phological disambiguation in one fell swoop.
In Proceedings of the 43rd Annual Meeting of
the Association for Computational Linguistics
(ACL’05), pages 573–580, Ann Arbor, Michi-
gan. Association for Computational Linguistics.
Zhiheng Huang, Wei Xu, and Kai Yu. 2015. Bidi-
rectional LSTM-CRF models for sequence tag-
ging. CoRR, abs/1508.01991.
Katharina Kann, Ryan Cotterell, and Hinrich
Schütze. 2016.
Neural morphological analy-
sis: Encoding-decoding canonical segments. In
Proceedings of the 2016 Conference on Empir-
ical Methods in Natural Language Processing,
pages 961–967, Austin, Texas. Association for
Computational Linguistics.
Apostolos Kemos,
Heike Adel,
and Hinrich
Schütze. 2019.
Neural semi-Markov condi-
tional random ﬁelds for robust character-based
part-of-speech tagging. In Proceedings of the
2019 Conference of the North American Chap-
ter of the Association for Computational Lin-
guistics: Human Language Technologies, Vol-
ume 1 (Long and Short Papers), pages 2736–
2743, Minneapolis, Minnesota. Association for
Computational Linguistics.
Stav Klein and Reut Tsarfaty. 2020. Getting the
##life out of living: How adequate are word-
pieces for modelling complex morphology? In
Proceedings of the 17th SIGMORPHON Work-
shop on Computational Research in Phonetics,
Phonology, and Morphology, pages 204–209,
Online. Association for Computational Linguis-
tics.
Lingpeng Kong, Chris Dyer, and Noah A Smith.
2015.
Segmental recurrent neural networks.
arXiv preprint arXiv:1511.06018.

--- Page 16 ---

Dilek Küçük and Fazli Can. 2019.
A tweet
dataset annotated for named entity recognition
and stance detection. CoRR, abs/1901.04787.
Guillaume Lample, Miguel Ballesteros, Sandeep
Subramanian, Kazuya Kawakami, and Chris
Dyer. 2016. Neural architectures for named en-
tity recognition. CoRR, abs/1603.01360.
LDC. 2008. ACE (automatic content extraction)
english annotation guidelines for entities ver-
sion 6.6.
Yi Luan, Luheng He, Mari Ostendorf, and Han-
naneh Hajishirzi. 2018. Multi-task identiﬁca-
tion of entities, relations, and coreference for
scientiﬁc knowledge graph construction.
In
Proceedings of the 2018 Conference on Empir-
ical Methods in Natural Language Processing,
pages 3219–3232, Brussels, Belgium. Associa-
tion for Computational Linguistics.
Xuezhe Ma and Eduard H. Hovy. 2016. End-to-
end sequence labeling via bi-directional lstm-
cnns-crf. CoRR, abs/1603.01354.
Behrang
Mohit,
Nathan
Schneider,
Rishav
Bhowmick, Kemal Oﬂazer, and Noah A. Smith.
2012. Recall-oriented learning of named enti-
ties in Arabic Wikipedia. In Proceedings of the
13th Conference of the European Chapter of
the Association for Computational Linguistics,
pages 162–173, Avignon, France. Association
for Computational Linguistics.
Amir More, Amit Seker, Victoria Basmova, and
Reut Tsarfaty. 2019.
Joint transition-based
models for morpho-syntactic parsing: Parsing
strategies for MRLs and a case study from mod-
ern Hebrew. Transactions of the Association for
Computational Linguistics, 7:33–48.
Joakim Nivre, Johan Hall, Sandra Kübler, Ryan
McDonald, Jens Nilsson, Sebastian Riedel, and
Deniz Yuret. 2007. The CoNLL 2007 shared
task on dependency parsing.
In Proceed-
ings of the 2007 Joint Conference on Empiri-
cal Methods in Natural Language Processing
and Computational Natural Language Learn-
ing (EMNLP-CoNLL), pages 915–932, Prague,
Czech Republic. Association for Computational
Linguistics.
Jeffrey Pennington, Richard Socher, and Christo-
pher Manning. 2014.
Glove: Global vectors
for word representation.
In Proceedings of
the 2014 Conference on Empirical Methods in
Natural Language Processing (EMNLP), pages
1532–1543, Doha, Qatar. Association for Com-
putational Linguistics.
Barbara Plank, Dirk Hovy, and Anders Søgaard.
2014.
Learning part-of-speech taggers with
inter-annotator agreement loss. In Proceedings
of the 14th Conference of the European Chap-
ter of the Association for Computational Lin-
guistics, pages 742–751, Gothenburg, Sweden.
Association for Computational Linguistics.
Sameer Pradhan, Alessandro Moschitti, Nianwen
Xue, Olga Uryupina, and Yuchen Zhang. 2012.
CoNLL-2012 shared task: Modeling multilin-
gual unrestricted coreference in OntoNotes. In
Joint Conference on EMNLP and CoNLL -
Shared Task, pages 1–40, Jeju Island, Korea.
Association for Computational Linguistics.
Sampo Pyysalo, Filip Ginter, Juho Heimonen,
Jari Björne, Jorma Boberg, Jouni Järvinen, and
Tapio Salakoski. 2007. Bioinfer: a corpus for
information extraction in the biomedical do-
main. BMC bioinformatics, 8(1):50.
Lev Ratinov and Dan Roth. 2009.
Design
challenges and misconceptions in named en-
tity recognition.
In Proceedings of the Thir-
teenth Conference on Computational Natural
Language Learning (CoNLL-2009), pages 147–
155, Boulder, Colorado. Association for Com-
putational Linguistics.
Nils Reimers and Iryna Gurevych. 2017. Optimal
hyperparameters for deep lstm-networks for se-
quence labeling tasks. CoRR, abs/1707.06799.
Djamé Seddah, Reut Tsarfaty, Sandra Kübler,
Marie Candito, Jinho D. Choi, Richárd Farkas,
Jennifer Foster, Iakes Goenaga, Koldo Go-
jenola Galletebeitia, Yoav Goldberg, Spence
Green,
Nizar
Habash,
Marco
Kuhlmann,
Wolfgang
Maier,
Joakim
Nivre,
Adam
Przepiórkowski, Ryan Roth, Wolfgang Seeker,
Yannick Versley,
Veronika Vincze,
Marcin
Woli´nski, Alina Wróblewska, and Eric Ville-
monte de la Clergerie. 2013. Overview of the
SPMRL 2013 shared task: A cross-framework
evaluation of parsing morphologically rich lan-
guages. In Proceedings of the Fourth Workshop
on Statistical Parsing of Morphologically-Rich

--- Page 17 ---

Languages, pages 146–182, Seattle, Wash-
ington, USA. Association for Computational
Linguistics.
Wolfgang Seeker and Özlem Çetino˘glu. 2015. A
graph-based lattice dependency parser for joint
morphological segmentation and syntactic anal-
ysis. Transactions of the Association for Com-
putational Linguistics, 3:359–373.
Amit Seker and Reut Tsarfaty. 2020. A pointer
network architecture for joint morphological
segmentation and tagging.
In Findings of
the Association for Computational Linguistics:
EMNLP 2020, pages 4368–4378, Online. Asso-
ciation for Computational Linguistics.
Yan Shao, Christian Hardmeier, and Joakim Nivre.
2018.
Universal word segmentation: Imple-
mentation and interpretation.
Transactions of
the Association for Computational Linguistics,
6:421–435.
Yan Shao, Christian Hardmeier, Jörg Tiedemann,
and Joakim Nivre. 2017. Character-based joint
segmentation and POS tagging for Chinese us-
ing bidirectional RNN-CRF.
In Proceedings
of the Eighth International Joint Conference on
Natural Language Processing (Volume 1: Long
Papers), pages 173–183, Taipei, Taiwan. Asian
Federation of Natural Language Processing.
Khalil Sima’an, Alon Itai, Yoad Winter, Alon Alt-
man, and Noa Nativ. 2001. Building a tree-bank
of modern hebrew text.
Hye-Jeong Song, Byeong-Cheol Jo, Chan-Young
Park,
Jong-Dae Kim,
and Yu-Seop Kim.
2018.
Comparison of named entity recogni-
tion methodologies in biomedical documents.
Biomedical engineering online, 17(2):158.
Erik F. Tjong Kim Sang. 2003. Introduction to the
conll-2003 shared task: Language-independent
named entity recognition.
In Proceedings of
the Seventh Conference on Natural Language
Learning at HLT-NAACL 2003 - Volume 4,
CONLL ’03, pages 142–147, Stroudsburg, PA,
USA. Association for Computational Linguis-
tics.
Reut Tsarfaty, Dan Bareket, Stav Klein, and Amit
Seker. 2020.
From SPMRL to NMRL: What
did we learn (and unlearn) in a decade of pars-
ing morphologically-rich languages (MRLs)?
In Proceedings of the 58th Annual Meeting
of the Association for Computational Linguis-
tics, pages 7396–7408, Online. Association for
Computational Linguistics.
Reut Tsarfaty, Shoval Sadde, Stav Klein, and Amit
Seker. 2019. What’s wrong with Hebrew NLP?
and how to make it right.
In Proceedings of
the 2019 Conference on Empirical Methods in
Natural Language Processing and the 9th Inter-
national Joint Conference on Natural Language
Processing (EMNLP-IJCNLP): System Demon-
strations, pages 259–264, Hong Kong, China.
Association for Computational Linguistics.
Reut Tsarfaty, Djamé Seddah, Yoav Goldberg,
Sandra Kuebler, Yannick Versley, Marie Can-
dito, Jennifer Foster, Ines Rehbein, and Lamia
Tounsi. 2010. Statistical parsing of morpholog-
ically rich languages (SPMRL) what, how and
whither.
In Proceedings of the NAACL HLT
2010 First Workshop on Statistical Parsing of
Morphologically-Rich Languages, pages 1–12,
Los Angeles, CA, USA. Association for Com-
putational Linguistics.
Gökhan Tür,
Dilek Hakkani-tür,
and Kemal
Oﬂazer. 2003.
A statistical information ex-
traction system for turkish.
Nat. Lang. Eng.,
9(2):181–210.
Clara Vania, Andreas Grivas, and Adam Lopez.
2018.
What do character-level models learn
about morphology?
the case of dependency
parsing.
In Proceedings of the 2018 Confer-
ence on Empirical Methods in Natural Lan-
guage Processing, pages 2573–2583, Brussels,
Belgium. Association for Computational Lin-
guistics.
Ralph Weischedel, Martha Palmer, Mitchell Mar-
cus, Eduard Hovy, Sameer Pradhan, Lance
Ramshaw, Nianwen Xue, Ann Taylor, Jeff
Kaufman, Michelle Franchini, Mohammed El-
Bachouti, Robert Belvin, and Ann Houston.
2013. Ontonotes release 5.0. Linguistic Data
Consortium, Philadelphia, PA.
Jie Yang, Shuailong Liang, and Yue Zhang. 2018.
Design challenges and misconceptions in neu-
ral sequence labeling.
In Proceedings of the
27th International Conference on Computa-
tional Linguistics (COLING).

--- Page 18 ---

Jie Yang and Yue Zhang. 2018.
NCRF++: An
open-source neural sequence labeling toolkit.
In Proceedings of the 56th Annual Meeting of
the Association for Computational Linguistics.
Seid Muhie Yimam, Iryna Gurevych, Richard
Eckart de Castilho, and Chris Biemann. 2013.
WebAnno: A ﬂexible, web-based and visually
supported system for distributed annotations.
In Proceedings of the 51st Annual Meeting of
the Association for Computational Linguistics:
System Demonstrations, pages 1–6, Soﬁa, Bul-
garia. Association for Computational Linguis-
tics.
Ziqi Zhang. 2013.
Named entity recognition:
challenges in document annotation, gazetteer
construction and disambiguation. Ph.D. thesis,
University of Shefﬁeld.
A
Alignment Heuristics
Aligning Multi-labels to Single Labels. In order
to evaluate morpheme-based labels (morph or
token-multi) in token-based settings, we introduce
a deterministic procedure to extend the morpho-
logical labels to token boundaries. Speciﬁcally,
we use regular expressions to map the multiple
sequence labels to a single label by choosing the
ﬁrst non-O entity category (BIES) as the single
category.
In case the sequence of labels is not
valid (e.g., B comes after E, or there is an O
between two I labels), we use a relaxed mapping
that does not take the order of the labels into
consideration: if there is an S or both B and E in
the sequence, return an S. Otherwise, if there is an
E, return an E; if there is a B, return a B; if there
is an I return an I (Figure 11).
Aligning Multi-labels to Morphemes. In order
to obtain morpheme boundary labels from token-
multi, we introduce a deterministic procedure to
align the token’s predicted multi-label with the list
of morphemes predicted for it by the MD. Specif-
ically, we align the multi-labels to morphemes in
the order that they are both provided. In case of a
mismatch between the number of labels and mor-
phemes predicted for the token, we match label-
morpheme pairs from the ﬁnal one backwards. If
the number of morphemes exceeds the number of
labels, we pad unpaired morphemes with O labels.
If the number of labels exceeds the morphemes,
we drop unmatched labels (Figure 12).
def extend_morph_to_tok(token_labels):
# gets list of morpheme NER labels for a token
# returns single NER label
biose_labels = ”
categories = list()
for label in token_labels:
if label==’O’:
biose_labels += ’O’
categories += None
else:
bio, cat = label.split(’-’)
biose_labels += bio
categories += cat
single_biose = get_single_biose(biose_labels)
single_cat = get_single_token_categ(categories)
if single_biose == ’O’:
return ’O’
else: return single_biose + ’-’ +single_cat
def get_single_token_categ(categ_labels):
# gets list of NER categories for a token
# returns the ﬁrst category which is not None
[...]
def get_single_biose(biose_labels):
# gets string of ’BIOSE’ for a token
# returns single character from ’BIOSE’
# regex matches valid labels for:
O|B|S|I|E|S
valid_seq = ’O+|O*BI*|O*BI*EO*|I+|I*EO*|O*SO*’
if valid_seq.match(biose_labels):
# split valid_seq by ’|’ and return
# label based on the corresponding re match
[...]
else: # treat as set
if ’S’ in biose_labels:
return ’S’
elif ’B’ and ’E’ in biose_labels:
return ’S’
elif ’E’ in biose_labels:
return ’E’
elif ’B’ in biose_labels:
return ’B’
elif ’I’ in biose_labels:
return ’I’
return ’O’
Figure 11: Multi-Label to Single Label Alignment

--- Page 19 ---

def align_multi_to_morph(labels, forms):
# gets list of labels and list of morph forms
# returns aligned list of tuples (morph, label)
if len(labels)==len(forms):
# if same length, return zipped by order
return zip(forms, labels)
elif len(labels)>len(forms):
# if extra labels, trim labels from the beginning
# return zipped by order
[ ... ]
elif len(labels)<len(forms):
# if extra forms, pad beginning with ’O’
# return zipped by order
[ ... ]
Figure 12: Multi-Label to Morpheme Alignment

```
