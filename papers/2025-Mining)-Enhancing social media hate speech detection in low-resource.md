---


























Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0544
type: conferencePaper
short_title: "Enhancing social media hate speech detection in low-resource languages using transformers and explainable AI"
year: 2025
first_author: "[[Fetahi, Endrit]]"
last_author: "[[Misini, Arta]]"
authors: "Fetahi, Endrit; Susuri, Arsim; Hamiti, Mentor; Kastrati, Zenun; Canhasi, Ercan; Misini, Arta"
authors_incomplete: false
doi: 10.1007/s13278-025-01497-w
url: "https://link.springer.com/article/10.1007/s13278-025-01497-w"
external_pdf: "https://link.springer.com/content/pdf/10.1007/s13278-025-01497-w.pdf"
publication: "Springer Social Network Analysis and Mining"
CONF-CC: "Social Network Analysis and Mining"
pdf_extract: "PDF Extracts/2025/2025-Mining)-Enhancing social media hate speech detection in low-resource.md"
local_pdf: "[[PDFs/2025/2025-Mining)-Enhancing social media hate speech detection in low-resource.pdf]]"
DATE_ADDED: 20260213
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "Albanian"
languages_list: Albanian
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
LLM_assessed: XLM-RoBERTa
DATA_URL: "NA"
tags: 
abstract: "Hate speech (HS) on social media exposes public discourse and community well-being. Despite its prevalence, majority of the research and technological advances have focused on rich-resourced languages. In contrast, Albanian, a language marked by dialects, limited NLP tools, and scarcity of annotated data, remains underexplored. To address this gap, this paper explores the enhancement of automatic hate speech detection in Albanian social media using advanced deep neural techniques."
CONFERENCE: "Other Conference"
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "Toxicity & Hate Speech"
is_benchmark: "No"
is_eval: "No"
is_dataset: "Yes"
data_description: "Dataset for hate speech detection"
data_metrics: "Not specified"
---
# Enhancing social media hate speech detection in low-resource languages using transformers and explainable AI

## Authors

[[Fetahi, Endrit]], [[Susuri, Arsim]], [[Hamiti, Mentor]], [[Kastrati, Zenun]], [[Canhasi, Ercan]], [[Misini, Arta]]

## Metadata

**Authors:** Fetahi, Endrit; Susuri, Arsim; Hamiti, Mentor; Kastrati, Zenun; Canhasi, Ercan; Misini, Arta

**Year:** 2025

**Type:** conferencePaper

**Venue:** Springer Social Network Analysis and Mining

**DOI:** [10.1007/s13278-025-01497-w](https://doi.org/10.1007/s13278-025-01497-w)

**Languages:** Albanian

## Links

- **DOI:** https://doi.org/10.1007/s13278-025-01497-w
- **URL:** https://link.springer.com/article/10.1007/s13278-025-01497-w

## Abstract

Enhances hate speech detection in Albanian social media using transformers and explainable AI. Dataset of 20,860 Facebook comments with multi-annotator process. Fine-tuned XLM-RoBERTa achieves F1=86%, establishing new state-of-the-art for Albanian hate speech detection. Uses SHAP and LIME for explainability.

## Summary

This paper addresses hate speech detection in Albanian, a low-resource language with dialectal diversity and limited NLP tools, by creating a dataset of 20,860 manually annotated Facebook comments using rigorous multi-annotator processes. The authors compare machine learning, deep neural networks, and transformer models, finding that character-level 4-gram TF-IDF features strengthen ML classifiers while fine-tuned XLM-RoBERTa achieves the highest performance with F1=86%. Error analysis using SHAP and LIME reveals key challenges including dialectal writing, short sentences, and implicit insults, establishing a new state-of-the-art benchmark for Albanian hate speech detection.

## Data Description

This paper enhances hate speech detection in Albanian social media using transformers and explainable AI. Creates a dataset of 20,860 Facebook comments with multi-annotator process. Fine-tuned XLM-RoBERTa achieves F1=86%, establishing new state-of-the-art for Albanian hate speech detection. Uses SHAP and LIME for explainability, addressing dialectal writing, implicit insults, and cultural context challenges in Albanian.


## Detailed Summary

This paper addresses the challenge of automatic hate speech detection in Albanian, a low-resource language marked by dialectal diversity (Gheg and Tosk), limited NLP tools, and scarce annotated data. The authors collect a large-scale dataset of 20,860 Facebook comments manually annotated through a rigorous multi-annotator process using majority voting, making it the largest Albanian hate speech dataset to date. The study systematically compares machine learning classifiers (SVM, Random Forest, Logistic Regression, KNN, Naive Bayes), deep learning models (CNN, LSTM, BiLSTM, GRU), and transformer-based models (BERT, XLM-RoBERTa, mBERT) across various feature engineering strategies.

Results demonstrate that character-level 4-gram TF-IDF features consistently reinforce ML classifiers for handling informal spelling and slang, while the fine-tuned XLM-RoBERTa achieves the highest overall performance with an F1-score of 86%. The authors conduct thorough error analysis using both manual inspection and explainable AI approaches (SHAP and LIME), revealing key challenges including dialectal writing variations, short sentences with limited context, and implicit insults that lack explicit hate indicators. These insights highlight the importance of domain-aligned embedding resources and more extensive annotation for low-resource contexts.

## Paper Outline

1. Introduction - Problem statement and research questions
2. Related Work - High-resource and Albanian-specific hate speech detection
3. Dataset - Data collection, annotation process, and statistics
4. Methodology - Feature engineering, ML/DL/Transformer models
5. Experimental Results - Performance comparison across all models
6. Error Analysis - Manual inspection and XAI (SHAP/LIME) analysis
7. Discussion - Key findings and implications
8. Conclusion

## Methods Summary

The dataset comprises 20,860 Facebook comments in Albanian collected from public posts and annotated by multiple annotators using majority voting for binary classification (hate vs. non-hate). Feature engineering strategies include TF-IDF (word and character n-grams), word embeddings (Word2Vec, FastText), and contextual embeddings. Models evaluated span traditional ML classifiers (SVM, Random Forest, Logistic Regression, KNN, Naive Bayes), deep learning architectures (CNN, LSTM, BiLSTM, GRU), and transformer-based models (BERT, XLM-RoBERTa, mBERT). Explainable AI analysis uses SHAP and LIME to identify token-level contributions to classification decisions and reveal failure modes.

## Results Summary

Fine-tuned XLM-RoBERTa achieves the highest performance with an F1-score of 86%, establishing a new state-of-the-art for Albanian hate speech detection. Character-level 4-gram TF-IDF features prove most effective for ML classifiers, capturing informal spelling and dialectal variations. Among ML models, SVM with character 4-gram features performs best. Deep learning models show moderate improvement over ML baselines but are outperformed by transformers. Error analysis reveals persistent challenges: dialectal writing introduces spelling variations that confuse models, short sentences lack sufficient context for accurate classification, and implicit insults without explicit hate keywords remain difficult to detect across all architectures.

## Conclusions

The study establishes a new benchmark for Albanian hate speech detection and demonstrates the effectiveness of multilingual transformers for low-resource language tasks. Limitations include the binary classification scheme (hate vs. non-hate) without fine-grained categories, and the dataset is limited to Facebook comments. Future work includes extending to multi-class hate speech categorization, developing Albanian-specific pre-trained models, creating domain-aligned embedding resources, and expanding annotation to capture more diverse hate speech manifestations including implicit and coded language.

## Artifact Contributions

No publicly released artifacts identified.

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B9
**Relevance:** State-of-the-art Albanian hate speech detection with explainable AI. Largest Albanian hate speech dataset (20,860 comments). Addresses dialectal writing, implicit insults, and cultural context challenges in Albanian.

## Tags

