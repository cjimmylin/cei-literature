---


Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0467
type: preprint
short_title: "GAHD: Improving Adversarial Data Collection by Supporting Annotators - Lessons from a German Hate Speech Dataset"
year: 2024
first_author: "[[Janis Goldzycher]]"
last_author: "[[Gerold Schneider]]"
authors: Janis Goldzycher, Paul Rottger, Gerold Schneider
url: "https://arxiv.org/abs/2403.19559"
external_pdf: "https://arxiv.org/pdf/2403.19559.pdf"
publication: arXiv / NAACL 2024
local_pdf: "[[PDFs/2024/2024-Goldzycher-GAHD Improving Adversarial Data Collection by Supporting Annotators -.pdf]]"
pdf_extract: "PDF Extracts/2024/2024-Goldzycher-GAHD Improving Adversarial Data Collection by Supporting Annotators -.md"
DATE_ADDED: 20260213
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
national_ethnic_cultural: "German"
languages_list: "German"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
is_benchmark: "No"
is_eval: "No"
is_dataset: "Yes"
data_description: "Dataset for hate speech detection"
data_metrics: "11k examples"
LLM_assessed: "GPT-3.5, GPT-4, LeoLM, gelectra-large"
DATA_URL: "https://github.com/jagol/gahd"
tags: 
abstract: "Hate speech detection models are only as good as the data they are trained on. Datasets sourced from social media suffer from systematic gaps and biases, leading to unreliable models with simplistic decision boundaries. Adversarial datasets, collected by exploiting model weaknesses, promise to fix this problem. However, adversarial data collection can be slow and costly, and individual annotators have limited creativity."
ethics_perspective: "AI Safety & Alignment"
---
# GAHD: Improving Adversarial Data Collection by Supporting Annotators - Lessons from a German Hate Speech Dataset

## Authors

[[Janis Goldzycher, Paul Rottger, Gerold Schneider]]

## Metadata

**Authors:** Janis Goldzycher, Paul Rottger, Gerold Schneider

**Year:** 2024

**Type:** preprint

**Venue:** arXiv / NAACL 2024

**Languages:** German

**Benchmark:** GAHD

## Links

- **arXiv:** https://arxiv.org/abs/2403.19559
- **Code/Data:** https://github.com/jagol/gahd

## Abstract

German Adversarial Hate speech Dataset with ~11,000 examples (42.4% hate speech). Uses adversarial data collection with annotator support strategies. Training on GAHD clearly improves model robustness.

## Summary

This paper introduces GAHD, a German Adversarial Hate speech Dataset with approximately 11,000 examples collected through four rounds of dynamic adversarial data collection (DADC). The authors explore multiple annotator support strategies across different rounds: free creation (R1), validating English-to-German translations (R2), validating newspaper sentences misclassified as hate speech (R3), and creating contrastive examples (R4). Experimental results show that training on GAHD improves model robustness substantially, with 18-20 percentage point increases in macro F1 scores on both in-domain and out-of-domain tests, and that mixing multiple support strategies yields the most consistent improvements.

## Data Description

GAHD (German Adversarial Hate speech Dataset) contains 11,000 German examples (42.4% hate speech) collected via dynamic adversarial data collection across 4 rounds. Training on GAHD improves model robustness, with 18-20 percentage point increases in macro F1 on in-domain and out-of-domain tests.


## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B7
**Relevance:** Adversarially-constructed German hate speech dataset designed to be challenging for state-of-the-art detection models.

## Tags

