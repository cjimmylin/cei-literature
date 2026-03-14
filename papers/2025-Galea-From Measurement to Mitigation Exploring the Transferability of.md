---




































Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0547
type: preprint
short_title: "From Measurement to Mitigation: Exploring the Transferability of Debiasing Approaches to Gender Bias in Maltese Language Models"
year: 2025
first_author: "[[Melanie Galea]]"
last_author: "[[Claudia Borg]]"
authors: Melanie Galea; Claudia Borg
url: "https://arxiv.org/abs/2507.03142"
external_pdf: "https://arxiv.org/pdf/2507.03142.pdf"
publication: arXiv
CONF-CC: "Preprint"
pdf_extract: "PDF Extracts/2025/2025-Galea-From Measurement to Mitigation Exploring the Transferability of.md"
local_pdf: "[[PDFs/2025/2025-Galea-From Measurement to Mitigation Exploring the Transferability of.pdf]]"
DATE_ADDED: 20260213
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: "Maltese"
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
LLM_assessed: "BERT"
DATA_URL: "https://github.com/MLRS/Malti-Bias"
tags: 
abstract: "The advancement of Large Language Models (LLMs) has transformed Natural Language Processing (NLP), enabling performance across diverse tasks with little task-specific training. However, LLMs remain susceptible to social biases, particularly reflecting harmful stereotypes from training data, which can disproportionately affect marginalised communities. We measure gender bias in Maltese LMs, arguing that such bias is harmful as it reinforces societal stereotypes and fails to account for gender..."
CONFERENCE: "Preprint"
ethics_overall: 100
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "No"
data_description: "Benchmark for bias and fairness"
data_metrics: "Not specified"
ethics_perspective: "Bias & Fairness"
---
# From Measurement to Mitigation: Exploring the Transferability of Debiasing Approaches to Gender Bias in Maltese Language Models

## Authors

[[Melanie Galea]], [[Claudia Borg]]

## Metadata

**Authors:** Melanie Galea, Claudia Borg

**Year:** 2025

**Type:** preprint

**Venue:** arXiv

**Languages:** Maltese

## Links

- **arXiv:** https://arxiv.org/abs/2507.03142

## Abstract

Measures gender bias in Maltese language models (BERTu and mBERTu) and evaluates transferability of debiasing methods from English. Adapts CrowS-Pairs and SEAT benchmarks to Maltese. Tests Counterfactual Data Augmentation, Dropout Regularization, Auto-Debias, and GuiDebias. Finds mBERTu shows less biased representation than BERTu.

## Summary

This paper investigates gender bias in Maltese language models by adapting English bias measurement benchmarks (CrowS-Pairs and SEAT) to Maltese, a low-resource gendered language with complex morphology. The authors evaluate BERTu (monolingual) and mBERTu (multilingual) and test four debiasing methods: Counterfactual Data Augmentation, Dropout Regularization, Auto-Debias, and GuiDebias. Results show mBERTu exhibits less biased representations than BERTu, while highlighting challenges in transferring English-centric bias mitigation techniques to morphologically complex languages.

## Data Description

The Malti-Bias repository contains code and datasets used for measuring and mitigating gender bias in Maltese language models (BERTu and mBERTu), including adapted versions of CrowS-Pairs and SEAT benchmarks for Maltese.


## Detailed Summary

This paper investigates gender bias in Maltese language models, focusing on BERTu (monolingual) and mBERTu (multilingual mBERT further pre-trained on Maltese). The work is motivated by the observation that most bias research focuses on English, while methods developed for English may not generalize to morphologically rich, low-resource languages. Maltese presents unique challenges as a Semitic-core language with Romance influences, complex gendered grammar, and written in Latin script. The authors adapt English bias measurement benchmarks (CrowS-Pairs and SEAT) to Maltese and implement four debiasing methods: Counterfactual Data Augmentation, Dropout Regularization, Auto-Debias, and GuiDebias.

The study contributes new Maltese evaluation datasets for gender bias research and provides a systematic analysis of the transferability of English-centric debiasing approaches to a linguistically complex low-resource language. The authors argue that gender bias in language models is harmful because it reinforces limiting societal stereotypes and excludes gender diversity, which is especially problematic in gendered languages. Results show that mBERTu exhibits less biased representations than BERTu, while highlighting significant challenges in applying existing English-centric bias mitigation techniques to morphologically complex languages, underscoring the need for more inclusive approaches in multilingual NLP development.

## Paper Outline

1. Introduction - Motivation for bias research in low-resource gendered languages
2. Related Work - Bias evaluation and mitigation for English and non-English models
3. Methodology - Bias measurement and mitigation approaches adapted to Maltese
4. Experiments - Evaluation setup and debiasing implementations
5. Results - Bias measurement and mitigation effectiveness
6. Discussion - Transferability challenges and implications
7. Conclusion

## Methods Summary

Gender bias is measured using CrowS-Pairs (adapted to Maltese) and SEAT (Sentence Encoder Association Test) benchmarks. Four debiasing methods are implemented: Counterfactual Data Augmentation (augmenting training data with gender-swapped examples), Dropout Regularization (applying dropout during fine-tuning to reduce bias), Auto-Debias (automated debiasing without manual attribute selection), and GuiDebias (guided debiasing using external knowledge). Both BERTu (monolingual Maltese BERT) and mBERTu (multilingual mBERT further pre-trained on Maltese) are evaluated before and after debiasing. The evaluation accounts for Maltese-specific challenges including gendered noun forms and complex morphology.

## Results Summary

The multilingual model mBERTu shows less biased representations than the monolingual BERTu model, suggesting that exposure to multiple languages during pre-training may help mitigate some forms of gender bias. However, the effectiveness of debiasing methods varies significantly when transferred from English to Maltese. The complex morphology and gendered grammar of Maltese present challenges for methods designed for English's relatively simple gender system. Some methods that work well for English show limited effectiveness for Maltese, while others introduce unintended side effects on downstream task performance.

## Conclusions

The paper highlights that applying English-centric bias mitigation methods to morphologically complex, low-resource languages requires significant adaptation and may not always yield the expected improvements. Limitations include the focus on binary gender bias only, excluding non-binary gender identities. Future work includes developing bias evaluation and mitigation methods specifically designed for gendered and morphologically rich languages, expanding to other forms of social bias beyond gender, and creating larger Maltese evaluation datasets.

## Artifact Contributions

- **Maltese CrowS-Pairs**: Adapted CrowS-Pairs evaluation dataset for Maltese gender bias measurement
- **Maltese SEAT**: Adapted SEAT benchmark for Maltese sentence encoder bias evaluation

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B9
**Relevance:** Directly evaluates gender bias in Maltese language models. Tests debiasing transferability to low-resource gendered language. Highly relevant to fairness, bias, and values evaluation in Maltese NLP.

## Tags

