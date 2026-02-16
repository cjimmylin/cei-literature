---







Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0474
type: conferencePaper
short_title: "Comparative Survey of German Hate Speech Datasets: Background, Characteristics and Biases"
year: 2025
first_author: "[[Bertram, Markus]]"
last_author: "[[Mandl, Thomas]]"
authors: Markus Bertram; Johannes Schafer; Thomas Mandl
url: "https://www.researchgate.net/publication/378070468_Comparative_Survey_of_German_Hate_Speech_Datasets_Background_Characteristics_and_Biases"
external_pdf: "https://ceur-ws.org/Vol-3630/LWDA2023-paper19.pdf"
publication: ResearchGate
pdf_extract: "PDF Extracts/2024/2024-Bertram-Comparative Survey of German Hate Speech Datasets Background.md"
local_pdf: "[[PDFs/2024/2024-Bertram-Comparative Survey of German Hate Speech Datasets Background.pdf]]"
DATE_ADDED: 20260213
national_ethnic_cultural: "German"
cultures_nationalities_list: "German"
languages_list: German
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
LLM_assessed: "BERT"
DATA_URL: "https://github.com/MarkusBertram/Cross-Dataset-Generalization-of-German-Hate-Speech-Datasets"
tags: 
abstract: "The large fraction of hate speech and other offensive and objectionable content online poses a vast challenge to societies. Offensive language such as insulting, hurtful, derogatory, or obscene content directed from one person to another and open to others undermines objective discussions. Hate speech detection quality depends on the datasets available for training. Potential bias needs to be identified in order to increase the generalization performance of the trained classifiers."
authors_incomplete: false
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "Bias & Fairness"
is_benchmark: "No"
is_eval: "No"
is_dataset: "Yes"
data_description: "Dataset for hate speech detection"
data_metrics: "Not specified"
---
# Comparative Survey of German Hate Speech Datasets: Background, Characteristics and Biases

## Authors

[[Markus Bertram]], [[Johannes Schafer]], [[Thomas Mandl]]

## Metadata

**Authors:** Markus Bertram; Johannes Schafer; Thomas Mandl

**Year:** 2024

**Type:** conferencePaper

**Venue:** ResearchGate

**Languages:** German

## Links

- **URL:** https://www.researchgate.net/publication/378070468_Comparative_Survey_of_German_Hate_Speech_Datasets_Background_Characteristics_and_Biases

## Abstract

Overview of nine German hate speech datasets applying a bias analysis framework. Identifies topical biases across datasets and notes that German datasets predominantly focus on Twitter with limited exploration of other platforms.

## Summary

This survey paper provides a systematic analysis of nine German hate speech datasets (Covid2021, De-reddit-corpus, Germeval2018, Germeval2019, Hasoc2019, Hasoc2020, and others) using a comprehensive bias analysis framework adapted from literature. The authors apply multiple methods to identify potential biases including Latent Semantic Indexing (LSI), topic models, Mutual Information, and Shapley values to analyze topical distribution and intra/inter-dataset similarity. Results reveal significant topical biases across datasets and highlight that German hate speech datasets predominantly focus on Twitter with limited platform diversity. The analysis provides crucial insights for understanding the limitations and potential generalization issues of hate speech classifiers trained on these datasets.

## Data Description

Overview of nine German hate speech datasets applying a bias analysis framework. Identifies topical biases across datasets and notes that German datasets predominantly focus on Twitter with limited exploration of other platforms. This is a survey paper, not a benchmark or model evaluation.


## Detailed Summary

This survey paper provides a systematic comparative analysis of nine major German hate speech datasets using a comprehensive bias analysis framework adapted from the literature. The datasets examined include Covid2021, De-reddit-corpus, Germeval2018, Germeval2019, Hasoc2019, Hasoc2020, and others. The authors apply multiple analytical methods to identify potential biases including Latent Semantic Indexing (LSI) for topic discovery, topic models for thematic distribution analysis, Mutual Information for identifying discriminative features, and Shapley values for understanding feature importance in classification decisions. The work addresses the critical question of whether biases in hate speech training data limit the generalizability of classifiers trained on these datasets.

## Paper Outline

1. Introduction - Importance of understanding dataset biases in hate speech detection
2. Related Work - Bias frameworks, German hate speech datasets
3. Methodology - Bias analysis framework, analytical methods
4. Dataset Overview - Nine German hate speech datasets described
5. Results - Topical biases, intra/inter-dataset similarity
6. Discussion - Implications for classifier generalization
7. Conclusion

## Methods Summary

The bias analysis framework examines datasets across multiple dimensions using four complementary methods: (1) Latent Semantic Indexing (LSI) identifies latent topical structures within each dataset; (2) topic models reveal the thematic distribution and concentration of topics; (3) Mutual Information measures how strongly specific terms associate with hate vs. non-hate labels, revealing lexical biases; and (4) Shapley values quantify the contribution of individual features to classification decisions, identifying which terms most influence model predictions. Both intra-dataset (within a single dataset) and inter-dataset (across datasets) similarity analyses are performed to assess consistency and generalization potential.

## Results Summary

The analysis reveals significant topical biases across all nine German hate speech datasets. German hate speech datasets predominantly focus on Twitter as a data source, with limited exploration of other platforms, creating platform-specific biases. Topical distributions vary substantially across datasets, with some focused on specific events (COVID-19, elections) while others cover broader phenomena. The inter-dataset similarity analysis shows relatively low overlap between datasets, suggesting that classifiers trained on one dataset may not generalize well to others. Certain keywords are disproportionately associated with hate speech labels, indicating lexical overfitting risks.

## Conclusions

The survey demonstrates that all major German hate speech datasets contain systematic biases that limit the generalizability of classifiers trained on them. The predominant reliance on Twitter data creates platform-specific artifacts, and topical concentration means models may learn event-specific patterns rather than generalizable hate speech characteristics. The findings highlight the need for more diverse data collection strategies and careful bias-aware evaluation when developing German hate speech detection systems.

## Artifact Contributions

- **Bias analysis framework**: Comprehensive multi-method framework for analyzing hate speech dataset biases
- **Comparative analysis**: Systematic comparison of nine German hate speech datasets along multiple bias dimensions
- **Generalization insights**: Evidence-based assessment of cross-dataset classifier transferability for German hate speech

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B7
**Relevance:** Systematic analysis of biases across all major German hate speech datasets.

## Tags

