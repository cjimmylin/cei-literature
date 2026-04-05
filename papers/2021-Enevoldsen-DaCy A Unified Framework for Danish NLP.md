---



































Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0491
type: preprint
short_title: "DaCy: A Unified Framework for Danish NLP"
year: 2021
first_author: "[[Kenneth C. Enevoldsen]]"
last_author: "[[Kristoffer Nielbo]]"
authors: Kenneth C. Enevoldsen; Lasse Hansen; Kristoffer Nielbo
url: "https://arxiv.org/abs/2107.05295"
external_pdf: "https://arxiv.org/pdf/2107.05295.pdf"
publication: arXiv
CONF-CC: "Preprint"
pdf_extract: "PDF Extracts/2021/2021-Enevoldsen-DaCy A Unified Framework for Danish NLP.md"
local_pdf: "[[Lit-WS-Lit-WS-PDFs/2021/2021-Enevoldsen-DaCy A Unified Framework for Danish NLP.pdf]]"
DATE_ADDED: 20260213
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: "Danish"
religious_values: "Islam"
rv_islam: 60
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
religious_values_list: "Islam"
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
LLM_assessed: "BERT, XLM-R"
DATA_URL: "https://github.com/centre-for-humanities-computing/DaCy"
tags: 
abstract: "Danish natural language processing (NLP) has in recent years obtained considerable improvements with the addition of multiple new datasets and models. However, at present, there is no coherent framework for applying state-of-the-art models for Danish. We present DaCy: a uniﬁed framework for Danish NLP built on SpaCy. DaCy uses efﬁcient multitask models which obtain state-of-the-art performance on named entity recognition, part-of-speech tagging, and dependency parsing."
CONFERENCE: "Preprint"
ethics_overall: 0
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
author_country: "DK"
author_region: "Western Europe"
author_global_north_south: "Global North"
weird_score: 84
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "No"
data_description: "Evaluation framework"
data_metrics: "Not specified"
---
# DaCy: A Unified Framework for Danish NLP

## Authors

[[Kenneth C. Enevoldsen]], [[Lasse Hansen]], [[Kristoffer Nielbo]]

## Metadata

**Authors:** Kenneth C. Enevoldsen, Lasse Hansen, Kristoffer Nielbo

**Year:** 2021

**Type:** preprint

**Venue:** arXiv

**Languages:** Danish

**Benchmark:** DaCy

## Links

- **arXiv:** https://arxiv.org/abs/2107.05295
- **Code/Data:** https://github.com/alexandrainst/danlp

## Abstract

Unified Danish NLP framework with bias and robustness testing. Found all models except DaCy large display significant ethnicity biases; only Polyglot shows significant gender bias. Uses data augmentation for more realistic performance estimates.

## Summary

This paper presents DaCy, a unified SpaCy-based framework for Danish NLP providing three multitask models (DaCy small based on Danish ELECTRA, DaCy medium based on Danish BERT, and DaCy large based on XLM-RoBERTa) achieving state-of-the-art performance on POS tagging, named entity recognition, and dependency parsing. The authors conduct comprehensive bias and robustness testing using data augmentation on the DaNE dataset, revealing that all models except DaCy large display significant ethnicity biases, while only Polyglot shows significant gender bias. The framework emphasizes that data augmentation can provide more realistic performance estimates for low-resource languages and includes tools for easy integration of existing models for sentiment, emotion, and subjectivity detection.

## Data Description

DaCy: unified Danish NLP framework with augmented evaluation suite testing bias and robustness of Danish language models on NER, POS, and dependency parsing.


## Detailed Summary

This paper presents DaCy, a unified SpaCy-based framework for Danish NLP that provides state-of-the-art multitask models for named entity recognition, part-of-speech tagging, and dependency parsing. DaCy includes three fine-tuned models of varying size: DaCy small (based on Danish ELECTRA, 14M parameters), DaCy medium (based on Danish BERT, 110M parameters), and DaCy large (based on multilingual XLM-RoBERTa, 550M parameters). All models perform POS tagging, NER, and dependency parsing in a single forward pass for efficiency. Beyond core NLP tasks, DaCy provides convenient wrappers for integrating other models for polarity, emotion, and subjectivity detection, and supports any HuggingFace Transformers model for sentence classification.

A significant contribution is the systematic evaluation of bias and robustness using data augmentation on the DaNE benchmark dataset. The authors argue that for languages with limited benchmark sets like Danish, standard test set evaluation provides unrealistic performance estimates, as the DaNE data was collected from 1983-1992 text and may not represent contemporary language use. Through augmentation-based testing (including name substitution with ethnically diverse names, spelling error injection, and casing variations), the authors find that all models except DaCy large display significant biases related to ethnicity in NER performance, while only the Polyglot model shows significant gender bias. DaCy large is especially robust to long input lengths and spelling variations, suggesting that larger multilingual models generalize better than smaller monolingual ones for bias robustness.

## Paper Outline

1. Introduction - Motivation for unified Danish NLP framework
2. Methods - Model training, data augmentation for bias and robustness testing
3. Results - Performance on DaNE, augmented evaluations, bias analysis
4. Discussion - Implications for low-resource language model development
5. Conclusion

## Methods Summary

All publicly available Danish language models are fine-tuned on the DaNE corpus using SpaCy 3.0.3 for joint POS tagging, NER, and dependency parsing. Models evaluated include two Danish ELECTRAs, Danish ConvBERT, Danish BERT, and multilingual XLM-RoBERTa Large. For bias and robustness testing, the DaNE test set is augmented using: (1) name substitution with Danish first and last names stratified by gender and Muslim/non-Muslim origin; (2) character-level perturbations simulating spelling errors; (3) casing variations; and (4) keystroke error simulation. Statistical significance of bias is assessed by comparing model performance across augmented demographic groups using bootstrapped confidence intervals.

## Results Summary

DaCy large achieves the best overall performance on standard DaNE evaluation, with the highest NER average F1, best UAS/LAS for dependency parsing, and competitive POS accuracy. Under augmented evaluation, DaCy large is the most robust model, maintaining performance under spelling errors, casing variations, and long input lengths. All models except DaCy large show statistically significant ethnicity bias in NER, with lower performance on Muslim-origin names compared to Danish-origin names. Only Polyglot shows significant gender bias. Smaller models (DaCy small, DaCy medium) are more sensitive to input perturbations than the larger multilingual model, suggesting that model scale and multilingual pre-training contribute to robustness.

## Conclusions

The authors conclude that data augmentation is particularly valuable for evaluating language models in low-resource settings where limited benchmarks may provide misleading performance estimates. They recommend that model developers routinely test for demographic biases through name augmentation and provide a series of augmenters as a starting point for more thorough evaluation. Future work includes developing additional augmenters, expanding the DaCy framework with more tasks, and investigating bias mitigation strategies for Danish NLP models.

## Artifact Contributions

- **DaCy Framework**: Unified Danish NLP framework built on SpaCy with three multitask models (https://github.com/centre-for-humanities-computing/DaCy)
- **Data Augmenters**: Bias and robustness testing tools for Danish NLP evaluation

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B7
**Relevance:** Danish NLP framework with explicit bias testing revealing ethnicity and gender biases in Danish models.

## Tags

