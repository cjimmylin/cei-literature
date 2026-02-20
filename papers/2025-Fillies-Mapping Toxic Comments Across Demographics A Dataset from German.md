---








Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0470
type: preprint
short_title: "Mapping Toxic Comments Across Demographics: A Dataset from German Public Broadcasting"
year: 2025
first_author: "[[Jan Fillies]]"
last_author: "[[Adrian Paschke]]"
authors: "[[Jan Fillies]]; [[Michael Peter Hoffmann]]; [[Rebecca Reichel]]; [[Roman Salzwedel]]; [[Sven Bodemer]]; [[Adrian Paschke]]"
url: "https://arxiv.org/abs/2508.21084"
external_pdf: "https://arxiv.org/pdf/2508.21084.pdf"
publication: arXiv
CONF-CC: "Preprint"
pdf_extract: "PDF Extracts/2025/2025-Fillies-Mapping Toxic Comments Across Demographics A Dataset from German.md"
local_pdf: "[[PDFs/2025/2025-Fillies-Mapping Toxic Comments Across Demographics A Dataset from German.pdf]]"
DATE_ADDED: 20260213
national_ethnic_cultural: "German"
cultures_nationalities_list: "German"
languages_list: German
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
LLM_assessed: "GPT-3, GPT-3.5, GPT-4o, GPT-4o-mini, Llama-3"
DATA_URL: "https://github.com/Behiwzad/swearify"
tags: 
abstract: "A lack of demographic context in existing toxic speech datasets limits our understanding of how different age groups communicate online. In collaboration with funk, a German public service content network, this research introduces the first large-scale German dataset annotated for toxicity and enriched with platform-provided age estimates. The dataset includes 3,024 human-annotated and 30,024 LLM-annotated anonymized comments from Instagram, TikTok, and YouTube."
authors_incomplete: false
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "Toxicity & Hate Speech"
is_benchmark: "No"
is_eval: "No"
is_dataset: "Yes"
data_description: "Annotated dataset for toxicity detection"
data_metrics: "Not specified"
CONFERENCE: "Preprint"
---
# Mapping Toxic Comments Across Demographics: A Dataset from German Public Broadcasting

## Authors

[[Jan Fillies]], [[Michael Hoffmann|Michael Peter Hoffmann]], [[Rebecca Reichel]], [[Roman Salzwedel]], [[Sven Bodemer]], [[Adrian Paschke]]

## Metadata

**Authors:** Jan Fillies, Michael Peter Hoffmann, Rebecca Reichel, Roman Salzwedel, Sven Bodemer, Adrian Paschke

**Year:** 2025

**Type:** preprint

**Venue:** arXiv

**Languages:** German

## Links

- **arXiv:** https://arxiv.org/abs/2508.21084

## Abstract

First large-scale German dataset annotated for toxicity enriched with age demographics from German public broadcasting (funk). 3,024 human-annotated and 30,024 LLM-annotated comments from Instagram, TikTok, and YouTube. Reveals age-based differences in toxic speech patterns.

## Summary

This paper presents the first large-scale German toxicity dataset enriched with platform-provided age demographics, developed in partnership with funk (ARD/ZDF public broadcasting network). The dataset comprises 3,024 human-annotated comments and 30,024 LLM-annotated comments from Instagram, TikTok, and YouTube, with comments consolidated using predefined toxic keywords resulting in 16.7% labeled as problematic. The analysis reveals significant age-based differences in toxic speech patterns, with younger users favoring expressive language and users aged 31-35 more likely to produce disinformation and devaluation, while Instagram shows the highest proportion of toxic content across platforms.

## Data Description

Presents the first large-scale German toxicity dataset enriched with age demographics from public broadcasting (funk), comprising 3,024 human-annotated and 30,024 LLM-annotated comments from Instagram, TikTok, and YouTube, revealing age-based differences in toxic speech patterns. Uses LLMs for annotation but does not evaluate specific models.


## Detailed Summary

This paper introduces the first large-scale multi-platform German-language dataset of social media comments annotated for toxicity and enriched with estimated user age ranges. Developed in partnership with funk (a digital content network operated by German public broadcasters ARD and ZDF targeting users aged 14-29), the dataset leverages a novel opportunity: platform-provided anonymized age distribution data from Instagram, TikTok, and YouTube. The dataset comprises 3,024 human-annotated comments and an additional 30,024 comments annotated via LLMs (GPT-3.5, GPT-4o, GPT-4o-mini, and Llama-3-8B). Comments were consolidated using predefined toxic keywords, resulting in 16.7% labeled as problematic. The annotation pipeline identified key categories including insults, disinformation, and criticism of broadcasting fees. Analysis reveals significant age-related differences in toxic speech patterns, with younger users favoring expressive or sarcastic language and users aged 31-35 more likely to produce disinformation and devaluation. Toxicity patterns also vary across platforms, with Instagram showing the highest proportion of toxic content.

## Paper Outline

1. Introduction - Gap in demographic context for toxic speech datasets
2. Related Work - Survey of English and German hate speech datasets; LLM annotation studies
3. Dataset Collection - Collaboration with funk; data sources and filtering
4. Annotation Schema - Human annotation categories and guidelines
5. LLM Annotation Pipeline - Comparative evaluation of four LLMs for toxicity annotation
6. Quantitative Analysis - Age-based differences and platform-specific patterns
7. Results and Discussion
8. Conclusion

## Methods Summary

Comments were collected from funk's subsidiary accounts across Instagram, TikTok, and YouTube, with platform-provided age distribution data attached. A predefined set of toxic keywords was used to consolidate relevant comments. The human annotation involved 3,024 comments with categories including insults, disinformation, criticism of broadcasting fees, and others. Four LLMs (GPT-3.5, GPT-4o, GPT-4o-mini, Llama-3-8B) were comparatively evaluated for annotation quality, and the best-performing model was used to extrapolate annotations to the remaining 30,024 comments. Statistical analysis examined age group differences, platform variations, and toxicity category distributions.

## Results Summary

The dataset reveals 16.7% of comments labeled as problematic. Age-based analysis shows distinct toxic speech patterns: younger users tend toward expressive or sarcastic language, while users aged 31-35 are more likely to engage in disinformation and devaluation. Instagram shows the highest proportion of toxic content across the three platforms examined. The comparative evaluation of LLMs for annotation demonstrates the viability of LLM-assisted annotation pipelines for scaling toxicity detection.

## Conclusions

The research contributes the first multi-platform, age-enriched German toxicity dataset, enabling novel fine-grained demographic analysis of online toxicity. The findings highlight the importance of age-aware content moderation systems and provide a foundation for developing more equitable moderation approaches that account for demographic differences in communication styles.

## Artifact Contributions

- **Dataset:** 33,048 German social media comments (3,024 human-annotated + 30,024 LLM-annotated) with toxicity labels and age demographics, from Instagram, TikTok, and YouTube, available via Zenodo to verified researchers

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B7
**Relevance:** Novel German toxicity dataset with demographic (age) annotations, combining human and LLM annotation.

## Tags

