---







































Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0472
type: conferencePaper
short_title: "A novel German TikTok hate speech dataset: far-right comments against politicians, women, and others"
year: 2025
first_author: "[[Jan Fillies]]"
last_author: "[[Adrian Paschke]]"
authors: Jan Fillies; Esther Theisen; Michael Hoffmann; Robert Jung; Elena Jung; Nele Fischer; Adrian Paschke
doi: 10.1007/s44248-025-00020-y
url: "https://link.springer.com/article/10.1007/s44248-025-00020-y"
external_pdf: "https://link.springer.com/content/pdf/10.1007/s44248-025-00020-y.pdf"
publication: "Springer (Discover Data)"
CONF-CC: "Discover Data"
pdf_extract: "PDF Extracts/2025/2025-Fillies-A novel German TikTok hate speech dataset far-right comments against.md"
local_pdf: "[[Lit-WS-Lit-WS-PDFs/2025/2025-Fillies-A novel German TikTok hate speech dataset far-right comments against.pdf]]"
DATE_ADDED: 20260213
national_ethnic_cultural: "German"
cultures_nationalities_list: "German"
languages_list: "German"
religious_values: "N/A"
rv_islam: 10
rv_christianity: 0
rv_buddhism: 0
rv_judaism: 0
rv_hinduism: 0
rv_sikhism: 0
rv_confucianism: 0
rv_taoism: 0
rv_shinto: 0
rv_jainism: 0
rv_bahai: 0
rv_zoroastrianism: 0
rv_ubuntu: 0
rv_indigenous: 0
religious_values_list: "N/A"
mp_mft: 0
mp_schwartz: 0
mp_trolley: 0
mp_kohlberg: 0
mp_dual_process: 0
mp_intuitionist: 0
mp_dyadic: 0
mp_identity: 0
moral_psychology: "N/A"
newtags: 
LLM_assessed: "BERT"
DATA_URL: "https://zenodo.org/records/14677171"
tags: 
abstract: "With the rise of new social media platforms designed for teenagers and adolescents, the importance of content moderation supported by algorithms is more necessary than ever. State-of-the-art hate speech detection algorithms are increasingly challenged by the rapid and creative evolution of modern language. To better understand the online discourse and phenomena of German far-right extremism on contemporary platforms, this research presents the first German TikTok dataset, consisting of 10,586..."
authors_incomplete: false
CONFERENCE: "Other Conference"
ethics_overall: 100
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
ethics_perspective: "Toxicity & Hate Speech"
nw_confucian: 0
nw_ubuntu: 0
nw_islamic_ethics: 0
nw_buddhist: 0
nw_dharmic: 0
nw_indigenous_relational: 0
nw_buen_vivir: 0
author_country: "FR"
author_region: "Western Europe"
author_global_north_south: "Global North"
weird_score: 77
is_benchmark: "No"
is_eval: "No"
is_dataset: "Yes"
data_description: "Annotated dataset for hate speech detection"
data_metrics: "Not specified"
---
# A novel German TikTok hate speech dataset: far-right comments against politicians, women, and others

## Authors

[[Jan Fillies]], [[Esther Theisen]], [[Michael Hoffmann]], [[Robert Jung]], [[Elena Jung]], [[Nele Fischer]], [[Adrian Paschke]]

## Metadata

**Authors:** Jan Fillies, Esther Theisen, Michael Hoffmann, Robert Jung, Elena Jung, Nele Fischer, Adrian Paschke

**Year:** 2025

**Type:** conferencePaper

**Venue:** Springer (Discover Data)

**DOI:** [10.1007/s44248-025-00020-y](https://doi.org/10.1007/s44248-025-00020-y)

**Languages:** German

## Links

- **DOI:** https://doi.org/10.1007/s44248-025-00020-y
- **URL:** https://link.springer.com/article/10.1007/s44248-025-00020-y

## Abstract

First German TikTok dataset with 10,586 comments annotated for far-right extremism and hate speech using a 32-aspect fine-grained annotation schema. 13.76% annotated as hateful. Addresses gap in TikTok hate speech research for German.

## Summary

This paper introduces the first German TikTok hate speech dataset comprising 10,586 comments collected from far-right accounts and annotated using a novel fine-grained schema of 32 labels developed with extremism experts. Using an ensemble of six hate speech classifiers for initial filtering followed by manual annotation by three trained annotators, the dataset identifies 13.76% of comments as hateful. The analysis reveals extensive hate directed toward German politicians (particularly Green Party members), women, and immigrants, with the comprehensive annotation schema enabling nuanced capture of hate speech types, targets, and intensity levels.

## Data Description

First German TikTok hate speech dataset: 10,586 comments annotated for far-right extremism and hate speech using a 32-label annotation schema, with 13.76% labeled hateful. Covers targets including politicians, women, and immigrants.


## Detailed Summary

This paper presents the first German TikTok hate speech dataset, consisting of 10,586 comments collected from comment sections of TikTok videos associated with the German far-right scene. The dataset was developed as part of the European Research Project RECO_DAR in collaboration with domain experts in online extremism and deradicalization. An extensive novel annotation schema comprising 32 labels was designed to capture various dimensions of hate speech including targets, types, and intensity levels, specifically tailored to the TikTok platform. Three trained annotators meticulously annotated the dataset, identifying 13.76% of comments as hateful. The quantitative analysis reveals extensive hate directed toward German politicians (particularly Green Party members), women, and immigrants. The research addresses the critical gap in German-language hate speech research on TikTok, a platform with 47.4% of users under 30 and 25% between ages 10-19, making content moderation particularly important given EU Digital Services Act and AI Act requirements.

## Paper Outline

1. Introduction - Motivation for TikTok hate speech research in German
2. Background - Definitions of far-right ideology and hate speech; survey of existing datasets
3. Dataset - Sources, collection process, privacy measures, and data statement
4. Methodology - Taxonomy development and annotation procedure
5. Analysis - Label distribution, inter-annotator agreement, sentiment, and keyword analysis
6. Qualitative Findings - In-depth examination of hate speech patterns
7. Discussion - Interpretation of results
8. Conclusion and Future Outlook

## Methods Summary

The dataset was constructed through a multi-step process. First, 323 accounts relevant to the German far-right ecosystem were identified through expert interviews, keywords, and snowball sampling (142 ultimately included). Approximately 815,000 comments were collected in November 2023. An ensemble of six hate speech classifiers (five open models plus Google Jigsaw) performed initial binary classification on a 150,000-comment subset. Videos with the highest average hate levels were selected until reaching 10,586 comments. The 32-label annotation schema was developed with extremism prevention experts, and three trained annotators performed the final annotation.

## Results Summary

Of the 10,586 comments, 13.76% were annotated as hateful. The dataset reveals hate speech predominantly targeting German politicians (especially Green Party members), women, and immigrants. The analysis identifies primary keywords within hate speech classes, label combinations and distributions, and sentiment patterns. Inter-annotator agreement metrics confirm annotation reliability. The fine-grained 32-label schema enables nuanced capture of subtle variations in hate speech expression beyond simple binary classification.

## Conclusions

The research contributes the first German TikTok hate speech dataset with a novel fine-grained annotation schema, addressing an important gap as existing German hate speech datasets focus primarily on Twitter. The comprehensive annotation approach enables more consistent and nuanced analysis compared to binary classification, and the dataset provides research institutions with a resource for developing platform-specific hate speech detection tools for German-language TikTok content.

## Artifact Contributions

- **Dataset:** 10,586 annotated German TikTok comments with 32-label hate speech schema
- **Annotation Schema:** Novel 32-class fine-grained taxonomy for hate speech annotation, developed with domain experts in online extremism
- **Code:** Scripts for data collection and classification available on GitHub

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B7
**Relevance:** First German-language TikTok hate speech dataset with fine-grained annotation for far-right content.

## Tags

