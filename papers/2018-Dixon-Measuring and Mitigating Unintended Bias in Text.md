---





































Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: UA6KI2C8
type: conferencePaper
short_title: "Measuring and Mitigating Unintended Bias in Text"
year: 2018
first_author: "[[Lucas Dixon]]"
last_author: "[[Lucy Vasserman]]"
authors: "Lucas Dixon; John Li; Jeffrey Sorensen; Nithum Thain; Lucy Vasserman"
doi: 10.1145/3278721.3278729
url: "https://dl.acm.org/doi/10.1145/3278721.3278729"
external_pdf: "file:///Users/jimmylin/Zotero/storage/7UNGXMSM/Dixon et al. - 2018 - Measuring and Mitigating Unintended Bias in Text Classification.pdf"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: "English"
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
newtags: "Bias & Fairness"
key_contribution: "One of the first papers to define 'unintended bias' in text classification (e.g., toxicity detectors flagging 'I am a gay man' as toxic) and proposed a 'balancing' mitigation strategy."
significance: "A seminal work in fairness for NLP, addressing the 'identity term bias' where models learn that mention of a minority group = toxicity, leading to censorship of those groups."
tags: 
abstract: "We introduce and illustrate a new approach to measuring and mitigating unintended bias in machine learning models. Our definition of unintended bias is parameterized by a test set and a subset of input features. We illustrate how this can be used to evaluate text classifiers using a synthetic test set and a public corpus of comments annotated for toxicity from Wikipedia Talk pages. We also demonstrate how imbalances in training data can lead to unintended bias in the resulting models, and..."
pdf: "https://dl.acm.org/doi/pdf/10.1145/3278721.3278729"
CONF-CC: "AIES 2018"
DATE_ADDED: 20260208
LLM_assessed: "NA"
DATA_URL: "https://github.com/conversationai/unintended-ml-bias-analysis"
pdf_extract: "PDF Extracts/2018/2018-Dixon-Measuring and Mitigating Unintended Bias in Text.md"
local_pdf: "[[PDFs/2018/2018-Dixon-Measuring and Mitigating Unintended Bias in Text.pdf]]"
CONFERENCE: "Other Conference"
ethics_overall: 100
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Evaluation methodology annotated dataset for toxicity detection"
data_metrics: "Not specified"
ethics_perspective: "Bias & Fairness"
---
# Measuring and Mitigating Unintended Bias in Text Classification

## Metadata

**Authors:** Dixon, Lucas; Li, John; Sorensen, Jeffrey; Thain, Nithum; Vasserman, Lucy

**Year:** 2018

**Publication:** Proceedings of the 2018 AAAI/ACM Conference on AI, Ethics, and Society

**Type:** conferencePaper

**DOI:** [10.1145/3278721.3278729](https://doi.org/10.1145/3278721.3278729)

**Pages:** 67-73

**Publisher:** ACM

## Links

- **URL:** https://dl.acm.org/doi/10.1145/3278721.3278729
- **DOI:** https://doi.org/10.1145/3278721.3278729

## Abstract

We introduce and illustrate a new approach to measuring and mitigating unintended bias in machine learning models. Our definition of unintended bias is parameterized by a test set and a subset of input features. We illustrate how this can be used to evaluate text classifiers using a synthetic test set and a public corpus of comments annotated for toxicity from Wikipedia Talk pages. We also demonstrate how imbalances in training data can lead to unintended bias in the resulting models, and therefore potentially unfair applications. We use a set of common demographic identity terms as the subset of input features on which we measure bias. This technique permits analysis in the common scenario where demographic information on authors and readers is unavailable, so that bias mitigation must focus on the content of the text itself. The mitigation method we introduce is an unsupervised approach based on balancing the training dataset. We demonstrate that this approach reduces the unintended bias without compromising overall model quality.

## Authors

[[Lucas Dixon]], [[John Li]], [[Jeffrey Sorensen]], [[Nithum Thain]], [[Lucy Vasserman]]

## Detailed Summary

This paper from Jigsaw (a Google subsidiary) introduces foundational methods for measuring and mitigating unintended bias in text classification models, specifically applied to toxicity detection. The authors define "unintended bias" as a model performing better for comments containing some identity terms than others - for example, giving unreasonably high toxicity scores to clearly non-toxic statements like "I am a gay man" because the word "gay" frequently appeared in toxic training examples. This work distinguishes between unintended model bias and fairness in application, noting that the same bias can lead to different fairness outcomes depending on how the model is deployed.

The paper demonstrates that the root cause of identity term bias is disproportionate representation in training data. Analysis of the Wikipedia Talk Pages dataset revealed that words like "gay" appeared in 3% of toxic comments but only 0.5% of comments overall, leading models to overgeneralize and associate these terms with toxicity regardless of context. To address this, the authors propose a novel mitigation strategy: strategically adding non-toxic examples containing the affected identity terms to balance the training data, sourcing this additional data from Wikipedia articles (assumed non-toxic) rather than requiring expensive additional human labeling.

The paper introduces several evaluation metrics for measuring unintended bias, including Error Rate Equality Difference (measuring variation in false positive and false negative rates across identity groups) and a novel "Pinned AUC" metric that compares each identity subgroup's performance against the overall population distribution, providing a threshold-agnostic measure of bias.

## Paper Outline

1. Abstract
2. Introduction - Motivation and overview of the unintended bias problem
3. Related Work - Prior research on fairness in ML and NLP
4. Methodology
   - Model Task and Data - Wikipedia Talk Pages toxicity classification
   - Definitions of Unintended Bias and Fairness
   - Quantifying bias in dataset
   - Bias Mitigation - Data balancing approach
5. Unintended Bias Evaluation Metrics
   - General Test Set
   - Identity Phrase Templates Test Set
   - AUC, Error Rate Equality Difference, Pinned AUC
6. Results - Experimental evaluation
7. Conclusion

## Methods Summary

The authors trained convolutional neural network models using Keras/TensorFlow on the Wikipedia Talk Pages dataset (127,820 comments labeled as toxic or non-toxic). They manually created a set of 51 common demographic identity terms and analyzed their distribution across toxic and non-toxic examples. For bias mitigation, they mined additional non-toxic examples from Wikipedia articles, adding enough examples per identity term to balance the toxic/non-toxic ratio at each text length bucket. A synthetic test set of 77,000 phrase templates was created for controlled bias evaluation.

## Results Summary

The initial toxicity model showed significant false positive bias for identity terms like "gay" (appearing in toxic comments at 6x the overall rate). The data balancing mitigation approach reduced unintended bias substantially: False Positive Equality Difference dropped from 0.21 to 0.07, False Negative Equality Difference from 0.17 to 0.08, and Pinned AUC Equality Difference from 0.40 to 0.15. Overall model quality was maintained - AUC on the general test set remained at 0.96 after mitigation.

## Conclusions

The paper establishes that unintended bias in text classification stems from data imbalances and can be measured and mitigated without compromising model performance. The proposed Pinned AUC metric provides a more nuanced measure of bias than standard approaches. The unsupervised mitigation approach - balancing training data with assumed non-toxic examples from a related domain - offers a practical solution when additional supervised data is expensive or impossible to obtain.

## Artifact Contributions

- Identity phrase template test set with 77,000 synthetic examples for bias evaluation
- Pinned AUC metric for measuring unintended bias in text classifiers
- Publicly released toxicity dataset on Wikipedia Talk pages

## Data Description

A synthetic test set and augmented training corpus for measuring and mitigating unintended demographic bias in text classifiers, applied to Wikipedia Talk page toxicity annotations.


## Notes


## Citation Info

792 citations (Semantic Scholar/DOI) [2025-08-27] 791 citations (Semantic Scholar/DOI) [2025-08-23] 271 citations (Crossref/DOI) [2025-08-23]
