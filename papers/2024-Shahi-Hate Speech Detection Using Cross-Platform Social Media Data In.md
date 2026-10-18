---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0475
type: preprint
short_title: "Hate Speech Detection Using Cross-Platform Social Media Data In English and German Language"
year: 2024
first_author: "[[Gautam Kishore Shahi]]"
last_author: "[[Tim A. Majchrzak]]"
authors: "Gautam Kishore Shahi; Tim A. Majchrzak"
url: "https://arxiv.org/abs/2410.05287"
external_pdf: "https://arxiv.org/pdf/2410.05287.pdf"
publication: arXiv
CONF-CC: Preprint
pdf_extract: "PDF Extracts/2024/2024-Shahi-Hate Speech Detection Using Cross-Platform Social Media Data In.md"
local_pdf: "[[Lit-WS-PDFs/2024/2024-Shahi-Hate Speech Detection Using Cross-Platform Social Media Data In.pdf]]"
DATE_ADDED: 20260213
national_ethnic_cultural: German
cultures_nationalities_list: German
languages_list: "English, German"
religious_values: N/A
rv_islam: 5
rv_christianity: 5
rv_buddhism: 0
rv_judaism: 0
rv_hinduism: 5
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
LLM_assessed: "BERT, RoBERTa"
DATA_URL: "https://github.com/Gautamshahi/BilingualYouTubeHateSpeech"
tags: 
abstract: "Hate speech has grown into a pervasive phenomenon, intensifying during times of crisis, elections, and social unrest. Multiple approaches have been developed to detect hate speech using artificial intelligence, but a generalized model is yet unaccomplished. The challenge for hate speech detection as text classification is the cost of obtaining high-quality training data. This study focuses on detecting bilingual hate speech in YouTube comments and measuring the impact of using additional data..."
CONFERENCE: Preprint
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
author_country: DE
author_region: "Western Europe"
author_global_north_south: "Global North"
weird_score: 84
is_benchmark: No
is_eval: No
is_dataset: No
data_description: N/A
data_metrics: "Not specified"
---
# Hate Speech Detection Using Cross-Platform Social Media Data In English and German Language

## Authors

[[Gautam Kishore Shahi]], [[Tim A. Majchrzak]]

## Metadata

**Authors:** Gautam Kishore Shahi, Tim A. Majchrzak

**Year:** 2024

**Type:** preprint

**Venue:** arXiv

**Languages:** English, German

## Links

- **arXiv:** https://arxiv.org/abs/2410.05287

## Abstract

Detects bilingual hate speech in YouTube comments in English and German covering politics, LGBT rights, and immigration. Examines cross-platform data augmentation for improving classification model performance.

## Summary

This study addresses the challenge of obtaining high-quality training data for bilingual hate speech detection by investigating cross-platform data augmentation strategies. The authors collect and annotate 1,892 English and 6,060 German YouTube comments from 190 videos covering topics including politics, LGBT rights, and immigration, then systematically evaluate how adding external datasets from other platforms (Twitter, Reddit, Gab) improves classifier performance. They measure dataset similarity based on content, hate words, and definitional overlap, finding that combining YouTube comments with Twitter and Gab data achieves the best performance with F1-scores of 0.74 for English and 0.68 for German. The findings demonstrate that strategically selecting similar cross-platform datasets based on content and definitional alignment can significantly enhance hate speech detection models.

## Data Description

A bilingual (English and German) hate speech dataset collected from YouTube comments covering political, LGBT rights, and immigration topics, used to study cross-platform data augmentation for improving hate speech classification performance.


## Detailed Summary

This study investigates the challenge of obtaining high-quality training data for bilingual hate speech detection by examining the value of cross-platform data augmentation. The authors collect and annotate YouTube comments in English (1,892) and German (6,060) from 190 videos covering social topics including politics, LGBT rights, and immigration. They then systematically evaluate how augmenting this YouTube training data with existing datasets from other platforms (Twitter, Reddit, Gab) affects classifier performance. The study measures three types of dataset similarity -- content similarity, definition similarity, and common hate words -- to predict which cross-platform combinations will yield the best improvements. The work addresses the fundamental problem that hate speech datasets vary considerably by platform, annotation goals, collection period, and linguistic style.

## Paper Outline

1. Introduction - Problem of obtaining high-quality hate speech training data
2. Related Work and Background - Machine learning for hate speech, cross-platform studies
3. Research Method - Data collection, annotation, similarity measures
4. Experiments and Results - Cross-dataset and cross-platform training
5. Discussion - Impact of dataset similarity on performance
6. Future Work

## Methods Summary

YouTube comments are collected from 190 videos across social topics and annotated for hate speech by human annotators. Eight existing datasets from Twitter, Reddit, and Gab in English and German are used for cross-platform augmentation. Dataset similarity is measured using three metrics: content similarity (text overlap), definition similarity (alignment of hate speech definitions), and common hate words (shared offensive vocabulary). Two augmentation strategies are tested: cross-dataset training (same platform, same language) and cross-platform training (different platforms). BERT and RoBERTa classifiers are fine-tuned with various data combinations, evaluated using precision, recall, and F1 score.

## Results Summary

The best performance is achieved by combining YouTube comments with Twitter and Gab data, yielding F1-scores of 0.74 for English and 0.68 for German YouTube comments. Adding more datasets that are similar in content, hate words, and definitions consistently improves classifier performance. Content similarity and hate word overlap are stronger predictors of successful augmentation than definition similarity alone. Cross-platform training (combining data from multiple platforms) generally outperforms using data from a single platform, provided the datasets share sufficient linguistic and topical overlap.

## Conclusions

Strategically selecting cross-platform datasets based on content and definitional similarity can significantly enhance hate speech detection models, partially alleviating the bottleneck of expensive annotation. The bilingual English-German approach reveals that cross-platform augmentation benefits vary by language, with different platform combinations optimal for each language. The study provides practical guidelines for researchers seeking to leverage existing datasets to improve hate speech classifiers in new domains or platforms.

## Artifact Contributions

- **Bilingual YouTube hate speech dataset**: 1,892 English and 6,060 German annotated YouTube comments from 190 videos
- **Cross-platform evaluation framework**: Systematic methodology for measuring dataset similarity and predicting augmentation effectiveness
- **Empirical guidelines**: Evidence-based recommendations for cross-platform data augmentation in hate speech detection

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B7
**Relevance:** Cross-platform, bilingual German-English hate speech detection study covering social topics.

## Tags

