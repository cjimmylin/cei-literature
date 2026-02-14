---
title: "2023-Bakrola-SAHAAYAK 2023 The Multi-Domain Bilingual Parallel - PDF Extract"
source_pdf: "2023-Bakrola-SAHAAYAK 2023 The Multi-Domain Bilingual Parallel.pdf"
pages: 3
extracted_at: "2026-02-13T09:15:43.731577"
---

# PDF Extract: 2023-Bakrola-SAHAAYAK 2023 The Multi-Domain Bilingual Parallel

**Source PDF:** 2023-Bakrola-SAHAAYAK 2023 The Multi-Domain Bilingual Parallel.pdf
**Total Pages:** 3

---

## Content

```
--- Page 1 ---

SAHAAYAK 2023 - the Multi Domain Bilingual Parallel Corpus of Sanskrit to
Hindi for Machine Translation
Vishvajitsinh Bakrola 1 Dr. Jitendra Nasariwala 2
Abstract
The data article presents the large bilingual
parallel corpus of low–resourced language pair
Sanskrit – Hindi, named SAHAAYAK 2023. The
corpus contains total of 1.5M sentence pairs be-
tween Sanskrit and Hindi. To make the universal
usability of the corpus and to make it balanced,
data from multiple domain has been incorporated
into the corpus that includes, News, Daily con-
versations, Politics, History, Sport, and Ancient
Indian Literature.
The multifaceted approach
has been adapted to make a sizable multi-domain
corpus of low-resourced languages like Sanskrit.
Our development approach is spanned from
creating a small hand-crafted dataset to applying
a wide range of mining, cleaning, and verification.
We have used the three-fold process of mining:
mining from machine-readable sources, mining
from non-machine readable sources, and collation
from existing corpora sources. Post mining, the
dedicated pipeline for normalization, alignment,
and corpus cleaning is developed and applied to
the corpus to make it ready to use on machine
translation algorithms.
1. Introduction
Parallel corpus is a crucial component in the field of ma-
chine translation. It refers to a collection of texts in two
or more languages, where each sentence in one language
has a corresponding sentence in the other language. Build-
ing parallel corpora can be a challenging task, especially
for low-resource languages. The effectiveness of machine
translation systems relies heavily on the quality and size
of the corpus used for training. Therefore, building high-
quality parallel corpus is essential for achieving accurate
1Assistant Professor, Department of Computer Science and
Engineering, Asha M. Tarsadia Institute of Computer Science
and Technology, Uka Tarsadia University 2Dean, Department of
Computer Sciences, Uka Tarsadia University. Correspondence to:
Vishvajitsinh Bakrola <vishvajit.bakrola@utu.ac.in>, Dr. Jitendra
Nasariwala <jvnasriwala@utu.ac.in>.
,
and human-like translation results. State-of-the-art Neural
machine translation systems are outperforming previous
translation approaches. (Singh et al., 2019) One of the sig-
nificant limitations of these systems is they are data-hungry.
NMT models require a large amount of data to offer good
translation accuracy, a particular hindrance from the begin-
ning of the neural machine translation journey.
2. Need of the Corpus
Both languages belong to 22 scheduled languages of India
under article 343 (1) of the Indian constitution. (Article-
343, 1) In addition, two of the Indian states, i.e., Himachal
Pradesh and Uttarakhand, have included Sanskrit as an addi-
tional official language, and nine states have Hindi as their
first official language. As per the last census of India, 528M
native speakers are using Hindi as their mother tongue, and
24.8K native speakers are using Sanskrit as their mother
tongue. (Census2011) Sanskrit fall under the category of
Low Resourced Language (LRL). It becomes a real problem
when it comes to the creation of LRLs corpus. These cate-
gories of languages are less studied, resource-scarce, less
computerized, and less privileged for the time being. (Singh,
2008) Most of today’s NLP research focuses on 20 of nearly
7000 spoken languages worldwide. This is because of their
significantly less digital availability. Sanskrit belongs to
the same category in multiple dimensions. Despite its rich
grammatical tradition in the linguistic community and being
one of the oldest living languages, there was an absolute
absence of a general-purpose bilingual corpus with San-
skrit as one of the languages. We cannot consider Sanskrit
a resource-scarce and less-studied language, but it is less
computerized. Though some good classical Sanskrit texts
from Vedas, Ramayana, Mahabharata, and Upanishads are
digitized chiefly, they have a monolingual form or are in
non-machine-readable formats.
We found that all the previous works contended against the
scarcity of sufficient parallel corpus with Sanskrit as one
of the languages in the translation pair. We observed that
developing a fully-aligned general-purpose parallel corpus
keeping Sanskrit as the source language is the first need to
establish a state-of-the-art machine translation system. To
our knowledge, SAHAAYAK 2023 is the most extensive
arXiv:2307.00021v1  [cs.CL]  27 Jun 2023

--- Page 2 ---

SAHAAYAK 2023 - the Multi Domain Bilingual Parallel Corpus of Sanskrit to Hindi for Machine Translation
dataset released in the public domain, with Sanskrit as one
of its languages.
3. General Architecture of Corpus Creation
The task of corpus creation of LRL required a 360-degree
approach for language coverage. To enhance the universal
usability the corpus should be balanced. (ATKINS et al.,
1992) We have applied our efforts to balance this corpus
by covering various domains. We initiated the parallel cor-
pus development of Sanskrit to Hindi with nearly 3.3K
sentences in 2018, and these translations included 2590
human-translated sentences of daily conversations in the
Indian context and 701 slokas from the Gita. Over a pe-
riod, we expanded this further with varieties of mining,
human expert verification, and translation by human experts.
Our mining approach is divided into three–fold, mining
from machine-readable sources, mining from non-machine-
readable sources, and Collation from other existing sources
of corpora. An overview of our pipeline is shown in Figure
– 1.
Figure 1. Pipeline of Sanskrit-Hindi Parallel Corpus Creation
We identified several web sources which publish content
in multiple Indic languages, including Sanskrit. Most of
these sources contain comparable texts rather than the direct
translation of each other. We have created a source-specific
standalone procedure for fetching text data.
For Sanskrit, a considerable amount of physical and scanned
documents are available which are not machine-readable.
We have developed separate procedures for fetching and
aligning text from these sources using OCR. In this min-
ing procedure, there are two varieties of seeds we have
worked with. One belongs to those sources which are pub-
licly available data, i.e., scanned copies of Sanskrit and its
Hindi translations and physical books, scriptures, and other
documents which are in public domains. The dedicated
OCR techniques are developed for extraction from such
public sources. In addition to these pipelines for parallel
text collection, samples were collected from the OPUS, and
NLLB. We have also applied parallel text extraction and
post-processing steps on these samples to remove the noise
and to make the text more clear. Text normalization, Text
alignment, and Corpus cleaning techniques are developed
and applied keeping in mind the Devanagari script.
4. Analysis of SAHAAYAK 2023
Table – 1 provides a glimpse on our bilingual parallel
Sanskrit-Hindi corpus.
Table 1. Analysis of SAHAAYAK 2023
PARAMETERS
SANSKRIT
HINDI
NUMBER OF SAMPLES
1580701
1580701
AVERAGE SENTENCE LENGTH
64
66
LONGEST SENTENCE LENGTH
2005
2069
5. Conclusion
SAHAAYAK 2023 is an attempt to contribute to the com-
munity of machine translation and computational linguistics.
We presented a bilingual parallel corpus of 1.5M parallelly
aligned sentence pairs from Sanskrit to Hindi. Tens of meth-
ods are applied to ensure the overall quality of the corpus
in the post–processing. We hope that SAHAAYAK 2023
will be proven helpful in developing state-of-the-art machine
translation systems for Indian languages. The improvements
in the translation quality of Sanskrit to other Indic languages
will also be proven beneficial for Education and different
societal needs.
6. Acknowledgment
We would like to thank the researchers of NLP and com-
putational linguistic community. We would also like to
acknowledge the authors of NLLB and OPUS. We would
like to take this opportunity to express our gratitude towards
our Sanskrit language experts Shri Harshad Joshi and Shri
Udit Sharma for their significant contributions for transla-
tion and verification. The acknowledgment is incomplete
without showing deep gratitude towards Maharshi Panini,
the complete source of inspiration to work in the direction
of Sanskrit based computational linguistics and Padmabhu-
san Shripad Damodar Satwalekar, whose books are proven
corner stone for creating interest in the Sanskrit language.
7. Dataset Source
The corpus can be accessed at https://rb.gy/hf6bp

--- Page 3 ---

SAHAAYAK 2023 - the Multi Domain Bilingual Parallel Corpus of Sanskrit to Hindi for Machine Translation
References
Article-343(1). Official languages of the union and eight
schedule, constitution of republic of india, government of
india. 24 June 2023. URL http://mha.gov.in.
ATKINS, S., CLEAR, J., and OSTLER, N. Corpus Design
Criteria. Literary and Linguistic Computing, 7(1):1–16,
01 1992. ISSN 0268-1145. doi: 10.1093/llc/7.1.1. URL
https://doi.org/10.1093/llc/7.1.1.
Census2011. Language – india, states, and union territories,
office of registrar general, government of india. 24 June
2023. URL https://censusindia.gov.in/.
Singh, A. K. Natural language processing for less privileged
languages: Where do we come from? where are we
going? In Proceedings of the IJCNLP-08 Workshop on
NLP for Less Privileged Languages, 2008. URL https:
//aclanthology.org/I08-3004.
Singh, M., Kumar, R., and Chana, I. Neural-based machine
translation system outperforming statistical phrase-based
machine translation for low-resource languages. In 2019
Twelfth International Conference on Contemporary Com-
puting (IC3), pp. 1–7, 2019. doi: 10.1109/IC3.2019.
8844915.

```
