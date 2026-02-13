---
title: "2026-Smywinski-Pohl-Targum A Multilingual New Testament Translation - PDF Extract"
source_pdf: "2026-Smywinski-Pohl-Targum A Multilingual New Testament Translation.pdf"
pages: 8
extracted_at: "2026-02-13T09:15:45.857345"
---

# PDF Extract: 2026-Smywinski-Pohl-Targum A Multilingual New Testament Translation

**Source PDF:** 2026-Smywinski-Pohl-Targum A Multilingual New Testament Translation.pdf
**Total Pages:** 8

---

## Content

```
--- Page 1 ---

Targum – A Multilingual New Testament Translation Corpus
Maciej Rapacz, Aleksander Smywiński-Pohl
AGH University of Kraków
{mrapacz, apohllo}@agh.edu.pl
Abstract
Many European languages possess rich biblical translation histories, yet existing corpora—in prioritizing linguistic
breadth—often fail to capture this depth.
To address this gap, we introduce a multilingual corpus of 657 New
Testament translations, of which 352 are unique, with unprecedented depth in five languages: English (208 unique
versions from 396 total), French (41 from 78), Italian (18 from 33), Polish (30 from 48), and Spanish (55 from 102).
Aggregated from 12 online biblical libraries and one preexisting corpus, each translation is manually annotated with
metadata that maps the text to a standardized identifier for the work, its specific edition, and its year of revision. This
canonicalization empowers researchers to define ”uniqueness” for their own needs: they can perform micro-level
analyses on translation families, such as the KJV lineage, or conduct macro-level studies by deduplicating closely
related texts. By providing the first resource designed for such flexible, multilevel analysis, our corpus establishes a
new benchmark for the quantitative study of translation history.
Keywords: Corpus, Digital Humanities, Multilinguality, Translation Studies, Text Mining
1.
Introduction
In the data-scarce era of early Natural Language
Processing, the Bible was a widely used paral-
lel corpus. Its utility for methods such as statisti-
cal machine translation (SMT) was based on the
assumption that the verses between translations
were semantically equivalent (Mueller et al., 2020).
The current landscape of NLP, characterized by
terabyte-scale datasets and large language mod-
els, redefines this utility.
The Bible’s volume is
negligible for training modern foundation models,
and its specific thematic and stylistic registers are
not representative of general language use. This
shift reframes the main application of the corpus:
from being data for AI systems to be an object of
study by AI systems, enabling large-scale quanti-
tative analysis of textual choices that reflect its cul-
tural and theological history.
To facilitate this new analytical paradigm, we in-
troduce targum, a corpus designed to prioritize
vertical depth over linguistic breadth. targum pro-
vides coverage for five languages with extensive
translation histories. English, French, Italian, Pol-
ish, and Spanish.
This level of depth makes it
possible to computationally analyze a wide spec-
trum of historical periods and confessional tradi-
tions, treating translation variants that were previ-
ously discarded by heuristic methods as a primary
object of study.
The name of the corpus is a tribute to this
methodological focus on the full spectrum of trans-
lation styles. A “Targum” (Aramaic/Hebrew: ￿￿￿￿￿)
was an ancient Aramaic translation of the Hebrew
Bible (Alexander, 1992). The name itself means
”translation” with roots traced to the Hittite tarkum-
maj (”to proclaim, explain, or translate”). The Tar-
gumic method was defined by a unique duality: it
often combined passages of high literalness with
dynamic additions and expansions to make the
text accessible to its audience (Schühlein, 1912).
Our corpus is named for this principle, as it is de-
signed to contain a massive collection of transla-
tions that spans this same spectrum — from the
most formal, literal renderings to the most dynamic
paraphrases.
The main contributions of this paper are two-
fold. First, we introduce targum, a new multilin-
gual corpus of 657 New Testament translations
(352 unique) with deep coverage in English (208
unique from 396 total), French (41 from 78), Ital-
ian (18 from 33), Polish (30 from 48), and Spanish
(55 from 102). Second, we manually verify meta-
data for each translation, including its publication
history. The remainder of this paper is structured
as follows. We first position our work with respect
to existing corpora.
We then detail the method-
ology for corpus construction and annotation, fol-
lowed by a statistical analysis of the resulting re-
source. We conclude by discussing new research
directions and plans for future work.
2.
Related Work
The Bible is a frequently used text for creating mul-
tilingual corpora due to its verse structure, which
provides de facto parallel sentence-level align-
ment in a large number of languages (Mueller
et al., 2020). Research using these corpora has
followed two main paradigms.
The most com-
mon has been instrumental, using the text as
a convenient dataset to bootstrap NLP tools for
low-resource languages, such as training machine
arXiv:2602.09724v1  [cs.CL]  10 Feb 2026

--- Page 2 ---

translation systems (Guzmán et al., 2019) or cre-
ating part-of-speech taggers via annotation projec-
tion (Nicolai and Yarowsky, 2019; Nicolai et al.,
2020). In contrast, a more recent paradigm, of-
ten aligned with the digital humanities, treats the
biblical text as the primary object of study. This
line of research applies computational methods to
perform a diachronic analysis of language change
or to study stylistic variation between translations.
Our work is situated within this second paradigm.
A significant body of work has focused on
creating biblical corpora that maximize linguis-
tic breadth.
Over time, a series of progres-
sively larger collections were introduced, starting
with foundational resources such as those from
Christodouloupoulos and Steedman (2015) and
Mayer and Cysouw (2014).
This trend culmi-
nated in the Johns Hopkins University Bible Cor-
pus, which expanded coverage to over 1,600 lan-
guages to support tasks such as typological analy-
sis and low-resource NLP (McCarthy et al., 2020;
Asgari and Schütze, 2017). The state of these dig-
ital resources, however, is often dynamic; for in-
stance, while some corpora like that of Mayer and
Cysouw (2014) are actively maintained and have
grown since their initial publication, the Johns Hop-
kins corpus is no longer publicly available. A more
recent effort, the eBible Corpus, provides another
standardized and accessible resource (Akerman
et al., 2023). While these collections offer unparal-
leled breadth, their depth for any single language
remains limited in comparison to our work. We pro-
vide a detailed statistical comparison in Section 4,
which highlights this gap.
Although most work has focused on breadth,
some projects have curated collections with depth
for specific scholarly questions.
A prime exam-
ple is the EDGeS Diachronic Bible Corpus, a re-
source containing 36 translations across four Ger-
manic languages designed to enable the “longitu-
dinal and contrastive study of complex verb con-
structions” (Bouma et al., 2020). Similarly, Carl-
son et al. (2018) compiles 34 English versions for
the specific task of evaluating the transfer of prose
style. Our work seeks to extend and generalize
this depth-focused approach. Although these valu-
able prior corpora were built to answer a prede-
fined research question, targum is designed as
a general-purpose resource for comparative analy-
sis. Its aim is to allow researchers to dynamically
create a wide variety of bespoke subcorpora tai-
lored to their own specific inquiries across a di-
verse set of languages and traditions.
3.
Methodology
3.1.
Data Acquisition and Processing
The construction of the corpus began with the
aggregation of translations from a diverse set
of sources, including 12 online biblical libraries
and one preexisting digital corpus (eBible). Our
selection strategy was twofold:
we identified
well-known, large-scale aggregators (e.g., Bible
Gateway, Bible Hub) to ensure broad coverage,
and supplemented these with language-specific
repositories (e.g., bibliepolskie.pl for Polish,
laparola.net for Italian) to achieve deep cov-
erage in our target languages.
The acquisition
pipeline consists of three stages.
First, an indexer inventories all available transla-
tions on each source website, capturing metadata
such as source-specific identifiers and translation
names. This creates a stable, timestamped snap-
shot of each site’s collection, providing a clear ba-
sis for the subsequent steps.
Second, a scraper uses this index to download
the full text of each translation, caching the raw
source files (e.g., HTML or JSON) for each of the
New Testament’s 260 chapters without modifica-
tion.
This separation ensures that parsing logic
can be iteratively refined offline, which prevents re-
peated requests to the source websites and guar-
antees reproducibility.
Third, a parser processes the cached files to
extract verse-level text.
A key challenge at this
stage is the structural variation in verse notation.
While many translations align to a simple one-to-
one mapping, more dynamic versions often intro-
duce non-standard segments (e.g., 6a, 6b) or con-
solidated ranges (e.g., 6–8).
Our parser is de-
signed to handle this complexity. The final output
is stored in two formats: a simple TSV file for rapid
processing, and a structured JSON file that pre-
serves the detailed verse segmentation.
3.2.
Canonicalization and Metadata
Annotation
The
scraped
data
is
inconsistent
across
sources;
the same translation often appears
with slightly different names and inconsistent
metadata (e.g.
publication year).
To resolve
this,
we manually mapped each scraped in-
stance to a canonical entry.
This metadata is
stored in YAML files, where each translation
is
assigned
a
standardized
canonical_id
and
canonical_revision_year.
The
canonical_id
identifies
a
distinct
transla-
tion
work,
meaning
any
version
presented
under a new name (e.g., the American Stan-
dard Version relative to the King James Ver-
sion) receives its own unique identifier.
The

--- Page 3 ---

canonical_revision_year
specifies
the
exact edition. Determining these values required
extensive external research.
While we initially
explored using AI assistants for automated meta-
data extraction, this approach proved unreliable
under manual review, often failing to distinguish
between closely-related revisions or misidentify-
ing publication details.
Consequently, the final
canonicalization was performed entirely manually.
This manual process is supported by the lexical
and semantic similarity analysis described in the
following section, which acts as a safeguard to
verify that translations grouped under the same
identifier are indeed textually consistent.
The
rationale for each classification is documented
to ensure transparency and to allow for future
reassessment, making it possible to track the
original reasoning for a decision and re-evaluate
it in light of new evidence.
3.3.
Quality Control via Cross-Source
Validation
The aggregation process naturally yields multiple
copies of the same canonical text, particularly for
widely-distributed versions.
Instead of viewing
these as duplicates to be discarded, we treat their
presence as a central feature of our quality control
methodology.
Once a group of scraped translations are
assigned
the
same
canonical_id
and
canonical_revision_year,
we
conduct
a systematic, side-by-side comparison of their
texts using lexical similarity metrics.
These are
sensitive to the single-character variations that
distinguish editions or reflect transcription errors.
This process is highly effective at spotting discrep-
ancies, which reliably expose one of two issues: a
subtle error in our parsing logic, or a pre-existing
data error on the source website, such as a typo
or a missing verse. To resolve these differences
and identify the correct edition, we employ several
verification techniques, including comparing the
text against scanned historical documents and
using search engines to find quotations of a
specific divergent phrase, which can often be
traced back to a particular publication.
This
iterative process allows us to correct our parsers
and progressively enhance the textual accuracy
of the entire collection.
3.4.
Final Corpus Structure and
Philosophy
The final output of our methodology is not a single,
pre-filtered dataset where duplicates have been re-
moved. Instead, we deliver the complete archive of
all collected translations, accompanied by a com-
prehensive metadata index.
This index file con-
tains all the canonical information for every transla-
tion instance, allowing researchers to understand
the provenance and specific edition of each text.
This structure embodies the core philosophy of
the resource: to empower researchers, not to im-
pose a pre-defined notion of what constitutes a ”du-
plicate.” The rich metadata allows users to define
uniqueness on their own terms, tailored to their
specific research question. For example, a scholar
studying Polish translations might choose to pri-
oritize copies from the language-specific bibliepol-
skie.pl source. A researcher analyzing the evolu-
tion of the KJV family would treat each revision as
a distinct entity. Conversely, a user performing a
broad, cross-lingual study might choose to dedupli-
cate aggressively, keeping only one instance per
canonical_id. By providing the complete data
alongside the structured metadata to navigate it,
targum is designed as a flexible platform.
4.
Corpus Analysis
In this section, we present a statistical analysis
of the compiled corpus to demonstrate its scale
and analytical potential. We begin by quantifying
its comparative depth against existing resources,
then examine its diachronic and linguistic proper-
ties, and conclude by analyzing its internal struc-
ture through similarity clustering.
This analysis
showcases the new avenues for research that the
corpus enables.
4.1.
Corpus Scale and Comparative
Depth
The primary contribution of targum is the unprece-
dented depth it provides for its five core languages.
As detailed in Table 1, the corpus offers a sig-
nificant increase in the number of unique trans-
lations compared to the next largest resource for
each language (Mayer and Cysouw, 2014). For
English, targum contains 208 unique versions, a
more than five-fold increase (5.3x) over the 39 pre-
viously available. The depth is similarly expanded
for the other languages: the 30 Polish translations
represent a five-fold increase (5.0x), while the col-
lections for Spanish (55 versions, 2.5x), Italian (18
versions, 2.6x), and French (41 versions, 2.4x) are
all substantially larger than in any prior corpus.
This new scale of vertical depth is what enables
the fine-grained comparative and diachronic analy-
ses.
Table 2 details the provenance of the transla-
tions, illustrating the results of our acquisition strat-
egy. The data highlights how coverage is distrib-
uted across both large-scale international aggre-
gators and specialized, language-specific repos-
itories.
English is well-represented across nu-

--- Page 4 ---

Language
English
French
Italian
Polish
Spanish
Total
Corpus
Christodouloupoulos and Steedman (2015)
2
1
1
1
1
6
Akerman et al. (2023)
24
4
2
2
5
37
Mayer and Cysouw (2014)
39
17
7
6
22
91
Targum
396
78
33
48
102
657
Targum (no duplicates)
208
41
18
30
55
352
Table 1: The number of translations for each language in the Bible translation corpora.
merous sites, with bible.com, biblegateway.com,
and bibles.org being the most prolific sources.
bible.com also serves as the single largest source
for Spanish translations.
For other languages,
a combination of sources proved most effective;
French, for instance, drew heavily from bible.com,
bible.audio, and obohu.cz. In contrast, the collec-
tions for Polish and Italian are dominated by their
respective national sites, bibliepolskie.pl and la-
parola.net. This distribution underscores the im-
portance of a hybrid collection strategy to achieve
the level of depth present in the targum corpus.
4.2.
Diachronic Distribution
The depth of the corpus is not only numerical but
also historical.
Figure 1 illustrates the temporal
distribution of the unique translations based on
their revision year. Across all five languages, the
distribution is skewed to the right, with a signifi-
cant concentration of translations published in the
last 50 years.
The historical scope of the cor-
pus begins in the 16th-century Reformation and
Counter-Reformation period, with English showing
the most continuous and extensive history from
that point forward. The plot also reveals notable
historical gaps. For Polish and Spanish, there is
a long period of silence between a small cluster
of early 17th-century translations and a renewed
burst of activity in the second half of the 19th cen-
tury. Similarly, while our Italian collection includes
a few early 17th-century texts, this period remains
scarce, and the earliest French translation in the
corpus is from the latter half of the 17th century.
4.3.
Verse Length Distribution
To analyze the linguistic properties of the corpus,
we examined the distribution of verse lengths ag-
gregated at the chapter level. For each of the New
Testament’s 260 chapters, we calculated the me-
dian and interquartile range (IQR) of verse lengths
(in characters) across all unique translations. The
results, visualized in Figure 2, reveal structural
patterns in the biblical narrative.
The Gospels
and Acts, which constitute the first five books and
roughly 45% of the chapters, show similar char-
acteristics, with Acts generally exhibiting longer
verses. In contrast, the subsequent Epistles are
composed of fewer chapters each, and their me-
dian verse lengths are more variable than those in
the narrative books. The book of Revelation, the
final book, contains the longest verses on average.
Across the entire New Testament, the IQR remains
remarkably consistent, typically spanning around
80 characters, which suggests a stable level of styl-
istic disagreement among translations.
4.4.
Translation Similarity and
Clustering
Given that the corpus contains numerous transla-
tions for each language, many of which are near-
duplicates, we sought to quantify their similarity.
To do this effectively at scale, we limited our analy-
sis to the Gospel of Matthew and devised two com-
parison methods: semantic and lexical.
For the semantic comparison, we generated a
single vector embedding for each chapter using
the Qwen3-Embedding-0.6B model1, selected for
its state-of-the-art multilingual performance and
long-context capabilities (Zhang et al., 2025). We
then calculated the pairwise cosine similarity for
each shared chapter between two translations and
averaged the results to produce a final similarity
score.
While effective for capturing broad stylistic dif-
ferences, semantic similarity can fail to register
minor textual variations.
To capture these, we
also computed a lexical similarity score. This was
calculated in the same chapter-wise manner, but
using the Levenshtein similarity, defined as 1 −
LD(x1,x2)
max(len(x1),len(x2)), where LD(x1, x2) is the Lev-
enshtein distance.
The pairwise similarity matrices in Figure 3 re-
veal several key features of the corpus’s internal
structure. A primary observation, particularly from
the semantic matrices, is the high degree of over-
all similarity, with most translation pairs scoring
above 0.8 in cosine similarity. This reflects their
shared source text and narrative content. Against
1https://huggingface.co/Qwen/
Qwen3-Embedding-0.6B

--- Page 5 ---

Language
English
French
Italian
Polish
Spanish
Total
Source
bible.audio
3
15
0
0
1
19
bible.com
77
19
7
8
28
139
bible.is
18
8
1
2
15
44
biblegateway.com
64
4
5
3
19
95
biblehub.com
46
0
0
0
0
46
bibles.org
74
6
3
3
14
100
biblestudytools.com
37
0
0
0
0
37
bibliepolskie.pl
0
0
0
20
0
20
crossbible.com
14
1
0
0
1
16
ebible.org
24
4
2
2
5
37
jw.org
1
1
1
1
1
5
laparola.net
9
3
11
0
2
25
obohu.cz
29
17
3
9
16
74
Table 2: Number of translations sourced from each site for each language in the targum corpus.
English
French
Italian
Polish
1500
1600
1700
1800
1900
2000
Year of Publication
Spanish
Figure 1: Diachronic distribution of unique translations for each core language. We mark a single dot per
translation, regardless of the number of the exact copies we have obtained.
this cohesive backdrop, two types of clusters are
visible.
The most prominent are the tight, high-
similarity blocks along the diagonal, which repre-
sent near-identical editions or minor revisions of
the same translation work.
Additionally, we ob-
serve distinct clusters of translations that are in-
ternally cohesive but markedly dissimilar from the
main group. These often correspond to more dy-
namic or paraphrastic translations that employ a
different stylistic register. While these clusters ap-
pear in both matrices, their distinctiveness is far
more pronounced in the lexical view. This diver-
gence highlights how the lexical metric, with its
sensitivity to specific word choices and sentence
structures, is particularly effective at quantifying
the unique stylistic strategies of these more dy-
namic versions, revealing differences that are par-
tially smoothed over by the semantic embeddings.
5.
Discussion
5.1.
New Research Directions
The targum corpus enables computational analy-
sis of research questions that were previously dif-
ficult or impossible to address on a scale. These
new avenues can be broadly grouped into micro-
and macrolevel analyses.

--- Page 6 ---

MAT
MRK
LUK
JHN
ACT
ROM
1CO
2CO
GAL
EPH
PHP
COL
1TH
2TH
1TI
2TI
TIT
PHM
HEB
JAS
1PE
2PE
1JN
2JN
3JN
JUD
REV
Chapter of the New Testament
40
60
80
100
120
140
160
180
200
Verse Length (characters)
Distribution of Verse Lengths Across All Unique Translations
Interquartile Range (IQR)
Median Verse Length
Figure 2: Distribution of verse lengths (in characters) across all unique translations for each chapter of
the New Testament. The thick blue line represents the interquartile range (IQR), and the dark blue dot
marks the median length.
Lexical
English
French
Italian
Polish
Spanish
Semantic
Figure 3: Pairwise similarity (cosine for semantic, Levenshtein for lexical) matrices between translations
for each language, ordered by their year of publication.
5.1.1.
Micro-Level Analysis
First, targum facilitates micro-level analyses by al-
lowing researchers to select and compare focused
subsets of the corpus based on specific metadata
criteria. For example, scholars can:
• Conduct diachronic studies by tracing lin-
guistic changes across decades of revisions
within a single translation family (e.g., the King
James Version).
• Perform synchronic comparisons of con-
temporary versions to isolate the effects of
confessional tradition or individual translator
style.
• Track
translation
lineage
by
following
the propagation of theological and stylistic
choices through indirect translation chains,
such as those mediated by a Latin Vulgate
source or, in modern institutional cases (e.g.,
Jehovah’s Witnesses, Biblica), by an English
pivot translation.
Furthermore, the corpus can serve as a quanti-
tative complement to traditional qualitative evalua-
tion. While an expert might label a translation as
“controversial” or “overly literal” based on key pas-
sages, targum allows researchers to measure the
pervasiveness of these features across the entire
New Testament. This provides a more objective
and comprehensive context for such judgments,
framing them within the full scope of the text.
5.1.2.
Macro-Level Analysis
Second, on a macro-level, targum can function as
a comprehensive benchmark and analytical test-
bed for any new translation. By generating a vec-
tor embedding for a new version, whether pro-
duced by humans or machines, it can be situated
within the semantic space of the entire corpus.

--- Page 7 ---

This allows for its stylistic and theological profile
to be quantitatively compared against hundreds of
historical precedents. It makes it possible to an-
swer questions such as: “Is this new translation
stylistically closer to the KJV or the NIV family?”
or “Does its interpretation of key theological terms
align more with historical Catholic or Protestant tra-
ditions?”
5.2.
Future Work
The work presented in this paper establishes a
foundation that can be expanded in several key
directions. First, we plan to enrich the metadata
for the existing translations. This will involve an-
notating details such as the source text (e.g., Tex-
tus Receptus, Nestle-Aland), the confessional tra-
dition of the translators, and the known textual lin-
eage of each version. Second, the most direct ex-
tension is to broaden the linguistic scope of targum
to include other languages with rich translation tra-
ditions, such as German, Portuguese, or Welsh. A
third avenue is to expand the corpus textually be-
yond the New Testament to also include the Old
Testament.
Together, these enhancements will
enable an even more comprehensive analysis of
translation practices and provide a richer dataset
for the computational study of translation history.
6.
Conclusion
In this paper, we introduce targum, a multilingual
New Testament corpus focused on the depth of
translation within each language to address a key
gap in existing biblical resources. By providing ex-
tensive coverage for five European languages and
enriching 352 unique translations with manually-
verified metadata, targum offers the necessary
infrastructure for a new class of computational re-
search. This resource makes it feasible to address
long-standing questions about the interplay of the-
ology, style, and culture in translation using scal-
able quantitative methods.
7.
Limitations
We acknowledge several limitations in the current
version of the targum corpus.
First, the corpus is necessarily constrained by
the availability of digitized translations on public
websites. This introduces a potential “digitization
bias,”, which means that the corpus reflects the his-
tory of translations that have been made digitally
accessible, which may not perfectly align with the
complete publication history.
For instance, Ger-
man was initially considered for inclusion due to
its rich translation tradition but was ultimately ex-
cluded because of the relative scarcity of online
versions compared to the five languages that were
selected. Therefore, the distribution of translations
in targum should be understood as representa-
tive of the digital landscape, not the complete land-
scape.
Second, the manual annotation process has in-
herent limitations.
Although our methodology is
robust, the final classification is still subject to hu-
man error. A key challenge arose when trying to
pinpoint the exact revision year for certain transla-
tions. This diﬀiculty was most pronounced not with
historical texts, which often have well-documented
print editions, but with modern, digital-native trans-
lations distributed primarily online. Such versions
can be revised multiple times per year without for-
mal versioning, and their release history is often
undocumented. In these cases, we made a best-
effort judgment based on the available textual and
contextual evidence (e.g., copyright dates on the
webpage) to determine the edition.
8.
Ethics Statement
Data for the targum corpus was aggregated from
publicly accessible websites. The authors do not
claim copyright on any of the translated texts. Our
distribution plan is designed to respect the intellec-
tual property rights of the copyright holders. The
code for creating the corpus, along with the subset
of translations that are in the public domain, will be
made publicly available. For translations under ac-
tive copyright, the full text will not be publicly dis-
tributed but will be made available to researchers
upon reasonable request for noncommercial re-
search purposes. Furthermore, we are committed
to responsible data stewardship and will remove
any translation from the corpus upon a direct re-
quest from a verified copyright holder.
In the preparation of this work, AI assistants
were used as productivity tools.
Specifically,
Cursor with Gemini 2.5 Pro and standalone
Gemini 2.5 Pro were used for tasks such as
generating boilerplate code for web scraping and
helping with the editing and formatting of this arti-
cle.
9.
Acknowledgments
This research was supported by the National
Science Centre, Poland, under project number
2025/57/N/HS2/04961.
We gratefully acknowl-
edge the Polish high-performance computing in-
frastructure PLGrid (HPC Center: ACK Cyfronet
AGH) for providing computational facilities and
support under grant no. PLG/2026/019145.

--- Page 8 ---

10.
Bibliographical References
References
Vesa Akerman, David Baines, Damien Daspit, Ulf
Hermjakob, Taeho Jang, Colin Leong, Michael
Martin, Joel Mathew, Jonathan Robie, and Mar-
cus Schwarting. 2023.
The ebible corpus:
Data and model benchmarks for bible transla-
tion for low-resource languages. arXiv preprint
arXiv:2304.09919.
Philip S. Alexander. 1992. Targum, targumim. In
David Noel Freedman, editor, The Anchor Bible
Dictionary, volume 6, pages 320–331. Double-
day, New York.
Ehsaneddin Asgari and Hinrich Schütze. 2017.
Past, present, future: A computational investiga-
tion of the typology of tense in 1000 languages.
In Proceedings of the 2017 Conference on Em-
pirical Methods in Natural Language Processing,
pages 113–124, Copenhagen, Denmark. Asso-
ciation for Computational Linguistics.
Gerlof Bouma, Evie Coussé, Trude Dijkstra, and
Nicoline van der Sijs. 2020.
The edges di-
achronic bible corpus.
Keith Carlson, Allen Riddell, and Daniel Rock-
more. 2018.
Evaluating prose style transfer
with the bible.
Royal Society open science,
5(10):171920.
Christos Christodouloupoulos and Mark Steed-
man. 2015.
A massively parallel corpus: the
bible in 100 languages.
Language resources
and evaluation, 49(2):375–395.
Francisco Guzmán, Peng-Jen Chen, Myle Ott,
Juan Pino, Guillaume Lample, Philipp Koehn,
Vishrav Chaudhary, and Marc’Aurelio Ranzato.
2019.
The FLORES evaluation datasets
for low-resource machine translation: Nepali–
English and Sinhala–English.
In Proceedings
of the 2019 Conference on Empirical Meth-
ods in Natural Language Processing and the
9th International Joint Conference on Natural
Language Processing (EMNLP-IJCNLP), pages
6098–6111, Hong Kong, China. Association for
Computational Linguistics.
Thomas Mayer and Michael Cysouw. 2014. Creat-
ing a massively parallel bible corpus. Oceania,
135(273):40.
Arya D McCarthy, Rachel Wicks, Dylan Lewis,
Aaron Mueller, Winston Wu, Oliver Adams, Gar-
rett Nicolai, Matt Post, and David Yarowsky.
2020.
The johns hopkins university bible
corpus:
1600+ tongues for typological explo-
ration. In Proceedings of the Twelfth Language
Resources and Evaluation Conference, pages
2884–2892.
Aaron Mueller, Garrett Nicolai, Arya D. McCarthy,
Dylan Lewis, Winston Wu, and David Yarowsky.
2020.
An analysis of massively multilingual
neural machine translation for low-resource lan-
guages. In Proceedings of the Twelfth Language
Resources and Evaluation Conference, pages
3710–3718, Marseille, France. European Lan-
guage Resources Association.
Garrett Nicolai, Dylan Lewis, Arya D. McCarthy,
Aaron
Mueller,
Winston
Wu,
and
David
Yarowsky. 2020.
Fine-grained morphosyn-
tactic analysis and generation tools for more
than one thousand languages.
In Proceed-
ings of the Twelfth Language Resources and
Evaluation Conference, pages 3963–3972, Mar-
seille, France. European Language Resources
Association.
Garrett Nicolai and David Yarowsky. 2019. Learn-
ing morphosyntactic analyzers from the Bible
via iterative annotation projection across 26 lan-
guages. In Proceedings of the 57th Annual Meet-
ing of the Association for Computational Linguis-
tics, pages 1765–1774, Florence, Italy. Associ-
ation for Computational Linguistics.
Franz Schühlein. 1912.
Targum.
In Charles G.
Herbermann, Edward A. Pace, Condé B. Pallen,
Thomas J. Shahan, and John J. Wynne, editors,
The Catholic Encyclopedia, volume 14. Robert
Appleton Company, New York.
Yanzhao Zhang, Mingxin Li, Dingkun Long, Xin
Zhang, Huan Lin, Baosong Yang, Pengjun
Xie, An Yang, Dayiheng Liu, Junyang Lin, Fei
Huang, and Jingren Zhou. 2025.
Qwen3 em-
bedding: Advancing text embedding and rerank-
ing through foundation models. arXiv preprint
arXiv:2506.05176.

```
