---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0471
type: preprint
short_title: "taz2024full: Analysing German Newspapers for Gender Bias and Discrimination across Decades"
year: 2025
first_author: "[[Urchs, Stefanie]]"
last_author: "[[Thiemichen, Stephanie]]"
authors: "Urchs, Stefanie; Thurner, Veronika; Aßenmacher, Matthias; Heumann, Christian; Thiemichen, Stephanie"
authors_incomplete: false
url: "https://arxiv.org/abs/2506.05388"
external_pdf: "https://arxiv.org/pdf/2506.05388.pdf"
publication: "arXiv / ACL 2025"
CONF-CC: "ACL 2025"
pdf_extract: "PDF Extracts/2025/2025-Urchs-taz2024full Analysing German Newspapers for Gender Bias and.md"
local_pdf: "[[Lit-WS-Lit-WS-PDFs/2025/2025-Urchs-taz2024full Analysing German Newspapers for Gender Bias and.pdf]]"
DATE_ADDED: 20260213
national_ethnic_cultural: German
cultures_nationalities_list: German
languages_list: German
religious_values: N/A
rv_islam: 0
rv_christianity: 5
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
religious_values_list: N/A
mp_mft: 0
mp_schwartz: 0
mp_trolley: 0
mp_kohlberg: 0
mp_dual_process: 0
mp_intuitionist: 0
mp_dyadic: 0
mp_identity: 0
moral_psychology: N/A
newtags: 
LLM_assessed: NA
DATA_URL: "https://doi.org/10.5281/zenodo.15480855"
tags: 
abstract: "Open-access corpora are essential for advancing natural language processing (NLP) and computational social science (CSS). However, large-scale resources for German remain limited, restricting research on linguistic trends and societal issues such as gender bias. We present taz2024full, the largest publicly available corpus of German newspaper articles to date, comprising over 1.8 million texts from taz, spanning 1980 to 2024."
CONFERENCE: "ACL 2025"
ethics_overall: 100
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 5
contractarian_ethics: 0
care_ethics: 0
ethics_perspective: "Bias & Fairness"
nw_confucian: 0
nw_ubuntu: 0
nw_islamic_ethics: 0
nw_buddhist: 0
nw_dharmic: 0
nw_indigenous_relational: 0
nw_buen_vivir: 0
author_country: US
author_region: "North America"
author_global_north_south: "Global North"
weird_score: 78
is_benchmark: No
is_eval: No
is_dataset: Yes
data_description: "Text corpus"
data_metrics: "Not specified"
---
# taz2024full: Analysing German Newspapers for Gender Bias and Discrimination across Decades

## Authors

[[Urchs, Stefanie]], [[Thurner, Veronika]], [[Aßenmacher, Matthias]], [[Heumann, Christian]], [[Thiemichen, Stephanie]]

## Metadata

**Authors:** Urchs, Stefanie; Thurner, Veronika; Aßenmacher, Matthias; Heumann, Christian; Thiemichen, Stephanie

**Year:** 2025

**Type:** preprint

**Venue:** arXiv / ACL 2025

**Languages:** German

**Benchmark:** taz2024full

## Links

- **arXiv:** https://arxiv.org/abs/2506.05388

## Abstract

Largest publicly available German newspaper corpus (1.8M+ texts from taz, 1980-2024). Analyzes gender representation finding consistent overrepresentation of men but gradual shift toward balanced coverage. Provides resource for studying gender bias in German texts.

## Summary

This paper presents taz2024full, the largest publicly available German newspaper corpus comprising over 1.8 million articles from the taz newspaper spanning 1980 to 2024. Using a scalable structured analysis pipeline that employs pronoun-based gender identification, the study demonstrates the corpus's utility for bias research by analyzing four decades of gender representation in German journalism. Key findings reveal a consistent overrepresentation of men in news coverage, though recent years show a gradual shift toward more balanced gender representation, providing a valuable resource for diachronic language analysis and critical media studies.

## Data Description

taz2024full is the largest publicly available German newspaper corpus, comprising over 1.8 million texts from the taz newspaper spanning 1980 to 2024. It is released for academic research on NLP and bias/discrimination analysis in German media.


## Detailed Summary

This paper introduces taz2024full, the largest publicly available corpus of German newspaper articles, comprising over 1.8 million texts from the German daily newspaper taz (die tageszeitung) spanning the period from 1980 to 2024. The corpus is presented as a dual contribution: first as a large-scale open-access resource for German NLP and computational social science, and second as a demonstration of its utility for studying gender bias and discrimination in journalistic language over more than four decades. The authors analyze gender representation using a pronoun-based identification approach within a scalable, structured pipeline, finding a consistent overrepresentation of men in news coverage alongside a gradual shift toward more balanced reporting in recent years. The corpus fills a critical gap in German-language resources, where existing datasets are often limited to keyword searches, sentence-level results, or restricted access.

## Paper Outline

1. Introduction - Motivation for large-scale German corpora and gender bias research
2. Related Work - Survey of English and German news corpora and bias detection methods
3. Data Collection and Preprocessing - Web scraping and cleaning of taz articles (1980-2024)
4. Corpus Statistics - Distribution analysis across decades, sections, and article lengths
5. Gender Bias Analysis - Pronoun-based actor identification and sentiment analysis pipeline
6. Results - Temporal trends in gender representation and linguistic framing
7. Conclusion - Summary of contributions and future research directions

## Methods Summary

The authors constructed the corpus by systematically scraping and preprocessing articles from the taz newspaper website. For the gender bias demonstration, they employed a structured analysis pipeline using pronoun-based gender identification (limited to binary categories due to German linguistic constraints lacking widely used non-binary pronouns). The pipeline combines information extraction and linguistic discourse analysis to examine actor mentions, frequency of gender references, sentiment associated with different genders, and linguistic framing patterns across four decades of reporting. Statistical analysis tracks temporal trends in gender representation.

## Results Summary

The analysis reveals a consistent overrepresentation of men in German newspaper coverage across all four decades examined (1980-2024). However, the data also shows a gradual shift toward more balanced gender coverage in recent years, suggesting evolving journalistic practices. The corpus contains over 1.8 million articles providing sufficient volume for statistically robust diachronic analysis. The pronoun-based approach effectively captures gender representation patterns at scale, though the authors acknowledge limitations in capturing non-binary gender identities.

## Conclusions

The authors conclude that taz2024full provides a valuable open-access resource for German NLP research and computational social science, addressing a significant gap in available large-scale German corpora. The gender bias analysis demonstrates the corpus's utility for studying societal trends reflected in media language, while the scalable analysis pipeline can be adapted for investigating other phenomena. The corpus is freely available to support inclusive and reproducible research in German-language NLP.

## Artifact Contributions

- **Dataset:** taz2024full corpus - 1.8M+ German newspaper articles spanning 1980-2024, publicly available via Zenodo (https://doi.org/10.5281/zenodo.15480855)
- **Analysis Pipeline:** Scalable structured pipeline for pronoun-based gender identification and bias analysis in German texts

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B7
**Relevance:** Massive German-language corpus for studying gender bias and discrimination in media across four decades.

## Tags

