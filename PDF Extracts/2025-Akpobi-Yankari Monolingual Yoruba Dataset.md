---
title: "Yankari Monolingual Yoruba Dataset - PDF Extract"
source_pdf: "2025-Akpobi-Yankari Monolingual Yoruba Dataset.pdf"
pages: 6
extracted_at: "2026-01-24T19:37:58.429501"
---

# PDF Extract: Yankari Monolingual Yoruba Dataset

**Source PDF:** 2025-Akpobi-Yankari Monolingual Yoruba Dataset.pdf
**Total Pages:** 6

---

## Content

```
--- Page 1 ---

Proceedings of the Sixth Workshop on African Natural Language Processing (AfricaNLP 2025), pages 1–6
July 31, 2025 ©2025 Association for Computational Linguistics
Yankari: Monolingual Yoruba Dataset
Maro Akpobi
African Center for Language Preservation
maro@acflp.org
Abstract
This paper presents Yankari, a large-scale
monolingual dataset for the Yoruba language,
aimed at addressing the critical gap in Natural
Language Processing (NLP) resources for this
important West African language. Despite be-
ing spoken by over 30 million people, Yoruba
has been severely underrepresented in NLP re-
search and applications. We detail our method-
ology for creating this dataset, which includes
careful source selection, automated quality con-
trol, and rigorous data cleaning processes. The
Yankari dataset comprises 51,407 documents
from 13 diverse sources, totaling over 30 mil-
lion tokens. Our approach focuses on ethical
data collection practices, avoiding problem-
atic sources and addressing issues prevalent
in existing datasets. We provide thorough au-
tomated evaluations of the dataset, demonstrat-
ing its quality compared to existing resources.
The Yankari dataset represents a significant ad-
vancement in Yoruba language resources, pro-
viding a foundation for developing more accu-
rate NLP models, supporting comparative lin-
guistic studies, and contributing to the digital
accessibility of the Yoruba language.
1
Introduction
Natural Language Processing (NLP) has made
tremendous strides in recent years, yet these ad-
vancements have primarily benefited high-resource
languages, leaving many African languages, in-
cluding Yoruba, underrepresented in NLP research
and applications. This paper introduces Yankari, a
large-scale, high-quality monolingual dataset for
Yoruba, a language spoken by over 30 million peo-
ple in West Africa. Despite its significant speaker
population, Yoruba has long suffered from a lack
of comprehensive, ethically-sourced language re-
sources suitable for modern NLP tasks.
Yankari addresses this critical gap by providing a
carefully curated corpus of 51,407 documents from
13 diverse sources, totaling over 30 million tokens.
Our methodology prioritizes ethical data collec-
tion, rigorous quality control, and the preservation
of linguistic authenticity. By avoiding problem-
atic sources such as religious texts and machine-
translated content, Yankari offers a more balanced
and representative sample of contemporary Yoruba
language use.
This paper details our data collection and pro-
cessing pipeline, discusses the challenges encoun-
tered in creating resources for low-resource lan-
guages, and provides a thorough analysis of the
dataset’s composition and potential biases. We also
offer insights into the ethical considerations sur-
rounding the creation and use of such resources.
Through Yankari, we aim to facilitate the develop-
ment of more accurate and culturally appropriate
NLP models for Yoruba, contribute to the preser-
vation of linguistic diversity in the digital age, and
provide a replicable approach for creating high-
quality datasets for other low-resource languages.
To our knowledge, Yankari represents the first
large-scale, non-religious domain monolingual re-
source created specifically for Yoruba. This work
not only provides a valuable asset for Yoruba NLP
but also offers a replicable approach for developing
similar datasets for other low-resource languages.
1

--- Page 2 ---

Source
Docs
Type
Domain
yo.wikipedia.org
16 809
Encyclopedia
General
alaroye.org
10 535
News
Current Affairs
www.bbc.com
8 252
News
Current Affairs
www.awikonko.com.ng
5 438
Blog
Culture
yoruba.von.gov.ng
2 542
News
Current Affairs
sportsinyoruba.
wordpress.com
2 328
Blog
Sports
www.asejere.net
2 079
Blog
Entertainment
asa.ooduarere.com
1 744
Blog
Culture
radionigeriaibadan.
gov.ng
824
News
Current Affairs
iroyinowuro.com.ng
603
News
Current Affairs
oroyoruba.blogspot.
com
139
Blog
Culture
yo.globalvoices.org
81
News
Current Affairs
edeyorubarewa.com
33
Blog
Fashion
Total
51 407
Table 1: Data sources for the Yankari dataset.
2
Related Works
This section examines existing resources for
Yoruba NLP, highlighting their limitations and
the need for a comprehensive, ethically-sourced
Yoruba dataset.
2.1
Monolingual Yoruba Datasets
2.1.1
Yorùbá Text C3
Alabi et al. (2020) introduced Yorùbá Text C3, com-
piled from various web sources including the Bible,
JW300 (Agi´c and Vuli´c, 2019), books, news arti-
cles, and Wikipedia. While broad in scope, this
dataset is heavily skewed towards religious con-
tent, particularly Christianity. This bias signifi-
cantly limits its utility for NLG tasks requiring
balanced and diverse text. Moreover, the inclu-
sion of JW300 data raises serious ethical and legal
concerns. Hutchinson (2024) points out that the
Jehovah’s Witnesses have explicitly prohibited the
use of their data in NLP research, making the con-
tinued use of JW300 not just ethically questionable
but potentially illegal.
2.1.2
MENYO-20k
Adelani et al. (2021) developed MENYO-20k, a
multi-domain English-Yoruba corpus primarily for
machine translation tasks. While it offers more di-
verse content, its relatively small size of 20,100 sen-
tences and focus on translation rather than mono-
lingual text generation limit its applicability for
large-scale NLG tasks.
2.2
Multilingual Datasets Including Yoruba
2.2.1
Wura Dataset
The Wura dataset, developed by Oladipo et al.
(2023), is a multilingual dataset containing approxi-
mately 68,000 Yoruba documents. It integrates con-
tent from JW300 and Wikipedia, inheriting similar
biases and ethical issues as Yorùbá Text C3. Our
manual inspection of the Wura dataset revealed crit-
ical quality issues not previously reported, includ-
ing formatting errors and inappropriate content.
2.2.2
Large-Scale Web-Crawled Corpora
Multilingual datasets such as mC4, OSCAR, and
the Afriberta-Corpus also include Yoruba con-
tent. However, these datasets often suffer from
noise, poor formatting, and limited source diver-
sity. Ogueji et al. (2021) used the Afriberta-Corpus,
which primarily sources data from the BBC News
and Common Crawl, resulting in a dataset lacking
the domain diversity necessary for robust NLG.
Nguyen et al. (2023) introduced CulturaX, cov-
ering 167 languages. However, its Yoruba sub-
set showed an alarmingly high duplication rate of
24.48% and contained machine-translated pages,
false positives in language detection, and a signifi-
cant amount of religious text.
2.3
Large-Scale Multilingual Efforts for
African Languages
The Cheetah project by Adebara et al. (2024)
focuses on natural language generation for 517
African languages, including Yoruba. This ambi-
tious project utilizes existing corpora from various
sources, including OSCAR (Ortiz Suárez et al.,
2

--- Page 3 ---

2020), CC-100 (Conneau et al., 2020), Afriberta-
Corpus (Ogueji et al., 2021), and mC4 (Xue et al.,
2021).
While Cheetah represents a significant step to-
wards improving NLP capabilities for African lan-
guages, it faces challenges common to large-scale
multilingual efforts. These include potential issues
with data quality, bias towards certain domains or
text types, and the inclusion of machine-translated
content.
2.4
Ethical Considerations in Using Religious
Texts
The ethical implications of using religious texts in
NLP, particularly for low-resource languages, are
profound and often overlooked. Hutchinson (2024)
challenges the NLP community’s casual approach
to sacred texts, arguing that the prevalence of Chris-
tian texts in datasets for low-resource languages re-
flects a legacy of colonialism and missionary work.
This creates an ethical dilemma where NLP tech-
nologies risk becoming unwitting agents of cultural
imperialism and religious proselytism.
3
Motivation for Yankari
Given these severe limitations and ethical concerns
in existing resources, there is an urgent need for a
high-quality, diverse, and extensive monolingual
Yoruba dataset that does not rely on restricted or
problematic sources. This is where Yankari comes
in, directly addressing the gaps and ethical issues
left by previous datasets.
Yankari aims to provide a large-scale, ethically
sourced corpus that represents a wide range of
Yoruba language use. By avoiding the pitfalls of
previous datasets, such as over-reliance on religious
texts or machine-translated content, Yankari seeks
to offer a more balanced and authentic representa-
tion of the Yoruba language. This approach aligns
with recent calls in the NLP community for more
thoughtful and ethical dataset creation, particularly
for low-resource languages.
4
Methodology
This section details our approach to creating the
Yankari dataset, including data collection, process-
ing, quality assurance steps, and corpus analysis.
4.1
Data Collection
Our data collection process focused on gather-
ing content from diverse, high-quality sources to
ensure a representative sample of contemporary
Yoruba language use. We carefully selected 13
sources, including news outlets, blogs, educational
websites, and Wikipedia.
Table 1 provides an
overview of these sources and their contributions
to the dataset.
4.2
Analysis of Existing Datasets
To inform our data collection and curation pro-
cess, we conducted a detailed analysis of the Wura
dataset (Oladipo et al., 2023). Our investigation
revealed several critical issues:
• High repetition: 18.01% of the dataset con-
tains the word ’asteroidi’ (asteroid), indicating
a significant bias towards astronomical con-
tent.
• Duplication: After removing duplicates and
cleaning, only 17,103 unique entries re-
mained, representing just 45% of the original
dataset.
• Quality issues: We found formatting errors, in-
appropriate content, and entries in non-Yoruba
languages.
These findings highlight the pressing need for
more stringent data curation practices in low-
resource language datasets. The recent study by
Hernandez et al. (2022) on scaling laws and the in-
terpretability of learning from repeated data offers
valuable insights that influenced our methodology.
Their extensive research reveals that data repetition
can severely hinder model performance, particu-
larly by disrupting the balance between memoriza-
tion and generalization. Additionally, repeated data
can obstruct the development of "induction heads,"
which are vital for in-context learning in large lan-
guage models. Most importantly, their work un-
derscores the pivotal role that high-quality training
data plays in the effectiveness of language mod-
els. These insights significantly shaped our careful
approach to developing Yankari, underscoring the
critical need for rigorous data curation, quality con-
trol, and the preservation of diversity in our dataset.
4.3
Data Processing Pipeline
Our data processing pipeline consisted of several
key steps:
3

--- Page 4 ---

4.3.1
HTML Parsing and Text Extraction
We implemented a robust HTML parsing system
using BeautifulSoup to extract clean text from web
pages. This process involved:
• Removing all script and style elements
• Extracting text from relevant HTML tags (e.g.,
<p>, <h1>, <h2>, etc.)
• Preserving the document structure by main-
taining paragraph boundaries
It is important to note that, beyond basic structural
parsing, no specific sentence-level filtering based
on the presence or absence of terminal punctuation
was applied at this stage, as the primary goal was
to capture full textual content from the identified
relevant HTML elements.
4.3.2
Deduplication
We employed a two-step deduplication process:
1. Exact matching at the document level to re-
move duplicate web pages
2. Near-duplicate detection at the paragraph
level using MinHash and Locality-Sensitive
Hashing (LSH) techniques
4.4
Corpus Statistics
Our final Yankari dataset consists of:
• Total number of documents: 51,407
• Total number of tokens: 30,438,702
• Average tokens per document: 592.11
4.5
Domain Analysis
The distribution of web domains in our corpus re-
flects the diverse sources we targeted. The top 5
domains by number of documents are:
1. yo.wikipedia.org: 32.70%
2. alaroye.org: 20.49%
3. www.bbc.com: 16.05%
4. www.awikonko.com.ng: 10.58%
5. yoruba.von.gov.ng: 4.94%
This distribution ensures a balance between en-
cyclopedic content, news, and cultural discussions,
providing a comprehensive representation of writ-
ten Yoruba across various domains.
4.6
Ethical Considerations and Excluded
Content
Throughout our data collection and processing, we
prioritized ethical considerations:
• We explicitly removed data from restricted
sources, such as those with terms prohibiting
use in NLP research.
• We filtered out suspected machine-translated
content to maintain linguistic authenticity.
This was primarily a manual process con-
ducted by the author, a native Yoruba speaker,
during data spot-checking and review. Docu-
ments exhibiting unnatural phrasing, common
translation artifacts, or content inconsistent
with known source characteristics were ex-
cluded.
• We removed inappropriate or offensive ma-
terial to ensure the dataset’s suitability for a
wide range of applications. This was also a
manual review process performed by the au-
thor. The guidelines focused on excluding
hate speech, explicit adult content, and other
materials generally considered unsuitable for
a public research dataset.
• We respected copyright and intellectual prop-
erty rights.
Content was sourced primar-
ily from publicly accessible websites. For
sources like Wikipedia, explicit open licenses
(e.g., CC-BY-SA) were followed. For other
public news and blog content without explicit
licenses for redistribution, we operated under
the principles of fair use for non-commercial
research, providing clear attribution via source
URLs. Direct contact for explicit redistribu-
tion permission was not feasible for every
source due to the scale of collection; this is a
recognized challenge in web-scale data gath-
ering and is noted as a limitation.
In line with our commitment to transparency, we
acknowledge that our content filtering process may
have introduced certain biases:
• The removal of very short texts may have dis-
proportionately affected certain types of con-
tent.
• Our focus on standard Yoruba may have led
to the underrepresentation of regional dialects
or colloquial expressions.
4

--- Page 5 ---

• Excluding content with non-Yoruba charac-
ters might have removed some culturally rele-
vant content involving code-switching or bor-
rowings.
4.7
Output Format
The final dataset is stored in JSONL format, with
each line containing a separate JSON document
with the following fields:
• text: The main content of the document in
Yoruba.
• url: The original URL from which the content
was sourced.
• source: A code indicating the source of the
document.
Here is a sample entry:
{
" t e x t " :
"O ma se o !
Ijamba oko
o f u r u f u
gba emi eeyan marun−
un . . . " ,
" u r l " :
" h t t p s : / /www. awikonko .
com . ng / 2 0 2 4 / 0 3 / o−ma−se −o−
ijamba −oko−ofurufu −gba −emi .
html " ,
" source " :
"ACFLP"
}
4.8
Quality Assurance
To ensure the highest quality of our dataset:
• We involved native Yoruba speakers in the
data cleaning and validation process.
• We conducted regular spot checks throughout
the data processing pipeline.
• We performed a final manual review of a ran-
domly selected subset of the data to verify its
quality and authenticity.
4.9
Limitations and Potential Biases
We acknowledge the following limitations and po-
tential biases in our dataset:
• Internet Bias
• Written Language Bias
• Source Bias
• Temporal Bias
• Standardization Bias
These limitations highlight areas for future work
and expansion of the Yankari dataset.
5
Limitations and Ethical Considerations
While the Yankari dataset represents a significant
contribution to Yoruba language resources for NLP,
it is important to acknowledge its limitations and
the ethical considerations that arise from its cre-
ation and potential use.
5.1
Representation Bias
• Spoken Language: The dataset does not in-
clude samples of spoken Yoruba.
• Informal Variants: Internet sources may favor
more formal language use.
• Demographic Skew: Internet access and con-
tent creation are not uniformly distributed
across all Yoruba-speaking demographics.
5.2
Diacritization Challenges
• Tonal Ambiguity: Incorrect or missing diacrit-
ical marks can cause ambiguity.
• Standardization Issues: The lack of a univer-
sally adopted standard for Yoruba orthography
may result in inconsistencies.
6
Conclusion
The Yankari dataset represents a significant step
forward in addressing the resource gap for Yoruba
in Natural Language Processing. By providing
a large-scale, high-quality, and ethically sourced
corpus, we have laid a foundation for advancing
NLP research and applications in this important
West African language. Our rigorous methodology,
which prioritizes data quality, diversity, and ethi-
cal considerations, sets a new standard for the de-
velopment of language resources for low-resource
languages.
The creation of Yankari highlights several crit-
ical challenges in developing NLP resources for
languages like Yoruba, including the scarcity of di-
verse, high-quality online content, the complexities
of automated processing for languages with limited
existing NLP tools, and the ethical considerations
surrounding data collection and potential misuse.
By transparently discussing these challenges and
our approaches to addressing them, we hope to con-
tribute to the broader conversation on responsible
5

--- Page 6 ---

AI development for diverse languages and cultures.
Future work will focus on rigorously evaluating
Yankari’s utility in various downstream NLP tasks,
such as language modeling, machine translation,
and text classification, including comparative per-
formance analyses against other available Yoruba
corpora. Such evaluations will further quantify the
benefits of Yankari’s curated nature and diverse
domain coverage.
The dataset is available on Hugging Face:
https://huggingface.co/datasets/acflp/YANKARI
Acknowledgments
This work was performed independently.
The
author received no specific grant from any fund-
ing agency in the public, commercial, or not-for-
profit sectors for the research described in this
manuscript.
References
Ife Adebara, AbdelRahim Elmadany, and Muhammad
Abdul-Mageed. 2024. Cheetah: Natural language
generation for 517 african languages.
Preprint,
arXiv:2401.01053.
David Adelani et al. 2021. Menyo-20k: A multi-domain
english - yoruba corpus for machine translation and
domain adaptation. In Proceedings of the Fourth
Workshop on Technologies for MT of Low Resource
Languages.
Željko Agi´c and Ivan Vuli´c. 2019. JW300: A wide-
coverage parallel corpus for low-resource languages.
In Proceedings of the 57th Annual Meeting of the As-
sociation for Computational Linguistics, pages 3204–
3210, Florence, Italy. Association for Computational
Linguistics.
Jesujoba Alabi et al. 2020. Massive vs. curated em-
beddings for low-resourced languages: The case of
yorùbá and twi. In Proceedings of the 12th Language
Resources and Evaluation Conference.
Alexis Conneau, Kartikay Khandelwal, Naman Goyal,
Vishrav Chaudhary, Guillaume Wenzek, Francisco
Guzmán, Edouard Grave, Myle Ott, Luke Zettle-
moyer, and Veselin Stoyanov. 2020. Unsupervised
cross-lingual representation learning at scale. In Pro-
ceedings of the 58th Annual Meeting of the Asso-
ciation for Computational Linguistics, pages 8440–
8451.
Danny Hernandez, Tom Brown, Tom Conerly, Nova
DasSarma, Dawn Drain, Sheer El-Showk, Nelson
Elhage, Zac Hatfield-Dodds, Tom Henighan, Tris-
tan Hume, Scott Johnston, Ben Mann, Chris Olah,
Catherine Olsson, Dario Amodei, Nicholas Joseph,
Jared Kaplan, and Sam McCandlish. 2022. Scaling
laws and interpretability of learning from repeated
data. Preprint, arXiv:2205.10487.
Ben Hutchinson. 2024. Modeling the sacred: Consider-
ations when using religious texts in natural language
processing. arXiv preprint arXiv:2404.14740.
Duc Minh Nguyen et al. 2023. Culturax: A cleaned,
enormous, and multilingual dataset for large lan-
guage models in 167 languages.
arXiv preprint
arXiv:2309.09400.
Kelechi Ogueji et al. 2021. Small data? no problem!
exploring the viability of pretrained multilingual lan-
guage models for low-resourced languages. arXiv
preprint arXiv:2011.03823.
Adewale Oladipo et al. 2023. Wura: A multilingual
dataset of african languages. In Proceedings of the
61st Annual Meeting of the Association for Computa-
tional Linguistics.
Pedro Javier Ortiz Suárez, Laurent Romary, and Benoît
Sagot. 2020. A monolingual approach to contextual-
ized word embeddings for mid-resource languages.
Proceedings of the 58th Annual Meeting of the Asso-
ciation for Computational Linguistics, pages 1703–
1714.
Linting Xue, Noah Constant, Adam Roberts, Mihir Kale,
Rami Al-Rfou, Aditya Siddhant, Aditya Barua, and
Colin Raffel. 2021. mt5: A massively multilingual
pre-trained text-to-text transformer. arXiv preprint
arXiv:2010.11934.
6

```
