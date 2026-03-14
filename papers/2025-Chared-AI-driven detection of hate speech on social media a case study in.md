---





































Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0453
type: conferencePaper
short_title: "AI-driven detection of hate speech on social media: a case study in the French language"
year: 2025
first_author: "[[Chared, Zahim]]"
last_author: "[[YILDIRIM, Sule YAYILGAN]]"
authors: "Chared, Zahim; Jantet, Clément; Ravix, Calliste; Salmi, Robin; Hashmi, Ehtesham; YILDIRIM, Sule YAYILGAN"
authors_incomplete: false
doi: 10.1007/s10586-025-05553-0
url: "https://link.springer.com/article/10.1007/s10586-025-05553-0"
external_pdf: "https://link.springer.com/content/pdf/10.1007/s10586-025-05553-0.pdf"
publication: Springer
CONF-CC: "Cluster Computing"
pdf_extract: "PDF Extracts/2025/2025-Chared-AI-driven detection of hate speech on social media a case study in.md"
local_pdf: "[[PDFs/2025/2025-Chared-AI-driven detection of hate speech on social media a case study in.pdf]]"
DATE_ADDED: 20260213
national_ethnic_cultural: "French"
cultures_nationalities_list: "French"
languages_list: "French"
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
LLM_assessed: "BART"
DATA_URL: "NA"
tags: 
abstract: "In today’s digital age, the rise of online hate speech–fueled by user anonymity and widespread use of platforms like X– has become a serious issue. It is a challenge for both social media companies and authorities in their efforts to maintain a safe and respectful online environment. Hate speech (HS) is mostly seen as an intentional act of aggressive behavior towards anyone based on their personal traits."
CONFERENCE: "Other Conference"
ethics_overall: 100
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
is_benchmark: "No"
is_eval: Yes
is_dataset: "Yes"
data_description: "Text corpus for hate speech detection"
data_metrics: "Not specified"
ethics_perspective: "Toxicity & Hate Speech"
---
# AI-driven detection of hate speech on social media: a case study in the French language

## Authors

[[Chared, Zahim]], [[Jantet, Clément]], [[Ravix, Calliste]], [[Salmi, Robin]], [[Hashmi, Ehtesham]], [[YILDIRIM, Sule YAYILGAN]]

## Metadata

**Authors:** Zahim Chared; Clément Jantet; Calliste Ravix; Robin Salmi; Ehtesham Hashmi; Sule YAYILGAN YILDIRIM

**Year:** 2025

**Type:** conferencePaper

**Venue:** Springer

**DOI:** [10.1007/s10586-025-05553-0](https://doi.org/10.1007/s10586-025-05553-0)

**Languages:** French

## Links

- **DOI:** https://doi.org/10.1007/s10586-025-05553-0
- **URL:** https://link.springer.com/article/10.1007/s10586-025-05553-0

## Abstract

Compiles and preprocesses a custom French hate speech dataset by merging and cleaning existing corpora. Develops binary-class ML (SVM, RF, NB, LR), DL (LSTM, Bi-LSTM, GRU), and Transformer models (CamemBERT, DistilCamemBERT, DeHateBert). Published in Cluster Computing 2025.

## Summary

This paper addresses hate speech detection in French social media by compiling and preprocessing a custom dataset from merged existing French corpora. The authors develop and benchmark multiple approaches including traditional machine learning (SVM, Random Forest, Naive Bayes, Logistic Regression), deep learning (LSTM, Bi-LSTM, GRU), and Transformer models (CamemBERT, DistilCamemBERT, DeHateBERT). Experimental results show DistilCamemBERT achieves the best performance with an F1-score of 80%, and the study includes interpretability analysis using explainable AI and bias mitigation techniques.

## Data Description

Custom French hate speech dataset of 12,397 tweets (merged and preprocessed from existing corpora plus AI-generated phrases), annotated with hate/non-hate labels and target group categories.


## Detailed Summary

This paper addresses the challenge of hate speech detection in French social media, a language that remains under-resourced compared to English, Arabic, or Hindi for this task. The authors compile and preprocess a custom French-language dataset by merging and cleaning existing French hate speech corpora, then develop and evaluate a comprehensive range of models: traditional machine learning classifiers (SVM, Random Forest, Naive Bayes, Logistic Regression), deep learning architectures (LSTM, Bi-LSTM, GRU), and Transformer models (CamemBERT, DistilCamemBERT, DeHateBERT).

Experimental results demonstrate that DistilCamemBERT significantly outperforms all other models, achieving an F1-score of 80% on the binary hate speech classification task. The paper also goes beyond standard classification by implementing interpretability studies using explainable AI methods and bias mitigation techniques to ensure transparency in AI-driven content moderation decisions. The authors discuss the legal framework for hate speech in France, the social impact of online hate speech, and the privacy concerns raised by AI-driven detection systems, emphasizing the importance of fair and unbiased automated decisions.

## Paper Outline

1. Introduction - Expansion of hate speech online, legal aspects, work contributions
2. Related Work - Prior approaches to hate speech detection
3. Dataset - Compilation, preprocessing, and analysis of French hate speech corpora
4. Methodology - ML, DL, and Transformer model architectures
5. Experimental Results - Performance comparison across all models
6. Explainable AI and Bias Analysis - SHAP/LIME interpretability studies
7. Conclusion

## Methods Summary

The authors create a custom French hate speech dataset by merging and cleaning existing French corpora for binary classification (hate vs. non-hate). Three categories of models are developed: traditional ML classifiers (SVM, Random Forest, Naive Bayes, Logistic Regression) with various text representations, deep learning models (LSTM, Bi-LSTM, GRU) for sequential text processing, and Transformer-based models including CamemBERT, DistilCamemBERT, and DeHateBERT. Models are evaluated using standard classification metrics including F1-score. The study includes explainability analysis using SHAP and LIME to interpret model decisions and bias mitigation techniques.

## Results Summary

DistilCamemBERT achieves the best overall performance with an F1-score of 80%, significantly outperforming other approaches on French hate speech detection. Transformer-based models consistently outperform traditional ML and deep learning approaches. The explainable AI analysis reveals how models make classification decisions and identifies potential biases in the detection process. Comparison with existing state-of-the-art results confirms the competitive performance of the proposed approach for French-language hate speech detection.

## Conclusions

The paper highlights that French hate speech detection resources lag behind those available for English. Limitations include the reliance on binary classification (hate vs. non-hate) without fine-grained categories, and the potential biases in merged datasets from different sources. Future work includes expanding to multi-class hate speech categorization, improving bias mitigation, and developing more robust interpretability frameworks for content moderation in French.

## Artifact Contributions

No publicly released artifacts identified.

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B6
**Relevance:** Comprehensive benchmarking of French hate speech detection models including CamemBERT variants. Provides state-of-the-art results for French HS detection.

## Tags

