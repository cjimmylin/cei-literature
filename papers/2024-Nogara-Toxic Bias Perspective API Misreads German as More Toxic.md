---


Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0460
type: preprint
short_title: "Toxic Bias: Perspective API Misreads German as More Toxic"
year: 2024
first_author: "[[Gianluca Nogara]]"
last_author: "[[Silvia Giordano]]"
authors: Gianluca Nogara, Francesco Pierri, Stefano Cresci, Luca Luceri, Petter Tornberg, Silvia Giordano
url: "https://arxiv.org/abs/2312.12651"
external_pdf: "https://arxiv.org/pdf/2312.12651.pdf"
publication: arXiv
local_pdf: "[[PDFs/2024/2024-Nogara-Toxic Bias Perspective API Misreads German as More Toxic.pdf]]"
pdf_extract: "PDF Extracts/2024/2024-Nogara-Toxic Bias Perspective API Misreads German as More Toxic.md"
DATE_ADDED: 20260213
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
national_ethnic_cultural: "German"
languages_list: "English, German"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Evaluation approach dataset for toxicity detection"
data_metrics: "Not specified"
LLM_assessed: "Perspective API"
DATA_URL: "NA"
tags: 
abstract: "Please check and cite the published version of this paper in the Proceedings of the 19th AAAI International Conference on Web and Social Media (ICWSM’25). Proprietary public APIs play a crucial and growing role as research tools among social scientists. Among such APIs, Google’s machine learning-based Perspective API is extensively utilized for assessing the toxicity of social media messages, providing both an important resource for researchers and automatic content moderation."
ethics_perspective: "Toxicity & Hate Speech"
---
# Toxic Bias: Perspective API Misreads German as More Toxic

## Authors

[[Gianluca Nogara, Francesco Pierri, Stefano Cresci, Luca Luceri, Petter Tornberg, Silvia Giordano]]

## Metadata

**Authors:** Gianluca Nogara, Francesco Pierri, Stefano Cresci, Luca Luceri, Petter Tornberg, Silvia Giordano

**Year:** 2024

**Type:** preprint

**Venue:** arXiv

**Languages:** English, German

## Links

- **arXiv:** https://arxiv.org/abs/2312.12651

## Abstract

Exposes intrinsic language biases in Perspective API's toxicity assessment, showing German content receives significantly higher toxicity scores than equivalent English content. Four times more tweets and users would be moderated when using the German language compared to English translations.

## Summary

This paper exposes significant intrinsic language bias in Google's widely-used Perspective API, which assesses toxicity in online content for both research and automated content moderation. Through analysis of multiple datasets including multilingual Twitter conversations and Wikipedia summaries, the authors demonstrate that German language text consistently receives significantly higher toxicity scores than equivalent content in other languages, regardless of the actual content. The bias is robust across various translations, topics, and data sources, with the practical consequence that approximately four times more tweets and users would be subject to moderation when using German compared to English translations. These findings raise concerns about the reliability of proprietary black-box APIs for both research and content moderation.

## Data Description

Exposes intrinsic language biases in Perspective API's toxicity assessment. Shows German content receives significantly higher toxicity scores than equivalent English content. Four times more tweets and users would be moderated when using German language compared to English translations. This is a bias evaluation study, not a benchmark dataset.


## Detailed Summary

This paper exposes a significant intrinsic language bias in Google's Perspective API, demonstrating that German-language text consistently receives substantially higher toxicity scores than equivalent content in other languages. Through systematic analysis of two large-scale datasets -- multilingual Twitter conversations and random Wikipedia summaries -- the authors show that this bias is robust across different translations, topics, and data sources. The practical consequence is severe: on average, four times more tweets and users would be moderated when using the German language compared to their English translations. The study examines existing research that has used Perspective API for German-language analysis, revealing that prior findings about German online discourse toxicity may have been artifacts of this tool bias rather than genuine phenomena.

## Paper Outline

1. Introduction - Research question about Perspective API bias toward German
2. Perspective API and Toxicity Research - Review of studies using the API for German content
3. Datasets - Multilingual Twitter conversations, Wikipedia summaries
4. Analysis and Results - Cross-language toxicity comparison, translation experiments
5. Discussion - Implications for research and content moderation
6. Conclusion and Limitations

## Methods Summary

The authors analyze toxicity scores from Perspective API across multiple languages using two complementary datasets: (1) multilingual Twitter conversations providing naturalistic social media content, and (2) random Wikipedia summaries serving as a neutral baseline expected to show minimal toxicity variation across languages. They perform systematic cross-language comparisons by translating content between languages and comparing resulting toxicity scores. The analysis covers multiple Perspective API attributes including overall toxicity, severe toxicity, insult, profanity, identity attack, and threat scores. Statistical tests are used to confirm that the toxicity score elevation for German is significantly higher than for other languages across all experimental conditions.

## Results Summary

German content consistently receives significantly higher toxicity scores than any other language, regardless of content type. The bias holds across: (1) original German text vs. other languages, (2) German translations of non-German content, (3) different topics and domains, and (4) both Twitter and Wikipedia data sources. At standard moderation thresholds (0.5-0.7), approximately four times more German tweets would be flagged compared to equivalent English content. This finding has critical implications for research studies that have used Perspective API to draw conclusions about German online discourse being more toxic, as these findings may reflect tool bias rather than genuine differences in toxicity.

## Conclusions

The paper demonstrates a systematic negative bias against German in Perspective API, likely stemming from artifacts or biases in the training data or the model itself. This raises fundamental concerns about the reliability of proprietary black-box APIs for academic research and automated content moderation. The findings suggest that prior cross-national toxicity studies using Perspective API may need to be revisited, and that researchers should exercise caution when using such tools for cross-linguistic analysis.

## Artifact Contributions

- **Empirical evidence**: Systematic documentation of German-language bias in Perspective API across multiple datasets and experimental conditions
- **Methodological framework**: Cross-language toxicity comparison methodology using both naturalistic and neutral baseline corpora
- **Published version**: ICWSM 2025 proceedings

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B7
**Relevance:** Reveals systematic bias in widely-used toxicity detection tool against German language, with implications for content moderation fairness.

## Tags

