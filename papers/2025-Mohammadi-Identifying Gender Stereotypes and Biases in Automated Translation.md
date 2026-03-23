---







































Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0511
type: preprint
short_title: "Identifying Gender Stereotypes and Biases in Automated Translation from English to Italian using Similarity Networks"
year: 2025
first_author: "[[Fatemeh Mohammadi]]"
last_author: "[[Samira Maghool]]"
authors: Fatemeh Mohammadi; Marta Annamaria Tamborini; Paolo Ceravolo; Costanza Nardocci; Samira Maghool
url: "https://arxiv.org/abs/2502.11611"
external_pdf: "https://arxiv.org/pdf/2502.11611.pdf"
publication: arXiv
CONF-CC: "Preprint"
pdf_extract: "PDF Extracts/2025/2025-Mohammadi-Identifying Gender Stereotypes and Biases in Automated Translation.md"
local_pdf: "[[Lit-WS-Lit-WS-PDFs/2025/2025-Mohammadi-Identifying Gender Stereotypes and Biases in Automated Translation.pdf]]"
DATE_ADDED: 20260213
national_ethnic_cultural: "Italian"
cultures_nationalities_list: "Italian"
languages_list: "English, Italian"
religious_values: "N/A"
rv_islam: 0
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
LLM_assessed: NA
DATA_URL: "NA"
tags: 
abstract: "This paper is a collaborative effort between Linguistics, Law, and Computer Science to evaluate stereotypes and biases in automated translation systems. We advocate gender-neutral translation as a means to promote gender inclusion and improve the objectivity of machine translation. Our approach focuses on identifying gender bias in Englishto-Italian translations. First, we define gender bias following human rights law and linguistics literature."
authors_incomplete: false
CONFERENCE: "Preprint"
ethics_overall: 100
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "No"
data_description: "Evaluation approach"
data_metrics: "Not specified"
ethics_perspective: "Bias & Fairness"
---
# Identifying Gender Stereotypes and Biases in Automated Translation from English to Italian using Similarity Networks

## Authors

[[Fatemeh Mohammadi]], [[Marta Annamaria Tamborini]], [[Paolo Ceravolo]], [[Costanza Nardocci]], [[Samira Maghool]]

## Metadata

**Authors:** Fatemeh Mohammadi, Marta Annamaria Tamborini, Paolo Ceravolo, Costanza Nardocci, Samira Maghool

**Year:** 2025

**Type:** preprint

**Venue:** arXiv

**Languages:** English, Italian

## Links

- **arXiv:** https://arxiv.org/abs/2502.11611

## Abstract

Evaluates stereotypes and biases in automated English-to-Italian translation systems using similarity networks. Identifies gender-specific terms (she/lei, he/lui) as key elements and uses cosine similarity to reveal model bias. Advocates gender-neutral translation for gender inclusion.

## Summary

This interdisciplinary paper combines Linguistics, Law, and Computer Science perspectives to evaluate gender stereotypes and biases in English-to-Italian automated translation systems. Using similarity network analysis and cosine similarity measures, the study identifies gender-specific terms (she/lei, he/lui) as key elements revealing systematic bias patterns in machine translation models. Grounding their approach in human rights law and linguistics literature, the authors advocate for gender-neutral translation as a means to promote gender inclusion and improve the objectivity of machine translation systems.

## Data Description

Evaluates gender stereotypes and biases in automated English-to-Italian translation systems using similarity networks to identify gender-specific terms and cosine similarity to reveal model bias. Advocates gender-neutral translation for gender inclusion. Proposes evaluation methodology rather than introducing a dataset.


## Detailed Summary

This interdisciplinary paper, a collaboration between Linguistics, Law, and Computer Science at the University of Milan, evaluates gender stereotypes and biases in English-to-Italian automated translation systems using similarity network analysis. The study situates itself within the broader European legal framework for AI, including the EU AI Act (March 2024) and Council of Europe treaty on human rights in AI systems (May 2024). The methodology involves: (1) defining gender bias categories following human rights law and linguistics literature, (2) collecting word corpora containing gender-specific and gender-neutral terms, (3) representing these words in a feature space organized into a similarity network, (4) computing cosine similarity between target terms and gender-specific anchors (she/lei, he/lui). The paper addresses the specific challenge of translating between English (a notional gender language) and Italian (a grammatical gender language), where the "inclusive masculine" rule and lack of established feminine professional titles create systematic bias opportunities. A comparative analysis between FastText word embeddings and Google Translate reveals significant shifts in bias direction after translation, with the methodology effectively identifying terms susceptible to gender bias.

## Paper Outline

1. Introduction - Gender bias in machine translation and the English-Italian case
2. Background and Related Work - Gender bias in law and linguistics; MT bias studies; notional vs. grammatical gender
3. Methodology - Word corpora collection; similarity network construction; bias features
4. Results - FastText vs. Google Translate comparison; bias direction shifts
5. Conclusion - Implications for gender-neutral translation algorithms

## Methods Summary

The approach uses cosine similarity to measure semantic associations between gender-specific anchor terms (she/lei, he/lui) and other terms in the embedding space. Word corpora containing both gender-specific and gender-neutral terms are collected and represented using FastText word embeddings and Google Translate outputs. Similarity networks are constructed to visualize and quantify gender associations. Specially designed numerical features capture both the intensity and direction of bias for each term. A comparative analysis between the embedding model (FastText) and the MT system (Google Translate) reveals how translation shifts bias patterns.

## Results Summary

The study finds a significant shift in the direction of gender bias after translation from English to Italian via Google Translate. The methodology effectively identifies terms susceptible to gender bias, providing quantitative measures of bias intensity and direction. The analysis reveals that Italian's grammatical gender system, with its "inclusive masculine" rule and historically asymmetric professional terminology, creates systematic opportunities for bias amplification in machine translation. The comparative analysis demonstrates that both word embedding methods and MT systems exhibit gender bias, but with different patterns and intensities.

## Conclusions

The paper advocates for gender-neutral translation as both a manifestation of gender inclusion and an objective for MT model development. The methodology provides tangible insights for developing and training gender-neutral translation algorithms, contributing to fairer representation of gender in automated translation systems. The approach can be extended to other notional-grammatical language pairs beyond English-Italian.

## Artifact Contributions

- **Methodology:** Similarity network-based framework for identifying and quantifying gender bias in machine translation between notional and grammatical gender languages
- **Analysis:** Comparative bias assessment between FastText embeddings and Google Translate for English-to-Italian translation

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B8
**Relevance:** Directly addresses gender bias in machine translation for Italian, relevant to fairness evaluation of NLP systems.

## Tags

