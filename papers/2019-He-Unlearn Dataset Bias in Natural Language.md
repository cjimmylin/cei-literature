---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: 6EJBF544
type: document
short_title: "Unlearn Dataset Bias in Natural Language"
year: 2025
first_author: "[[He He]]"
authors: "[[He, He]]; [[Zha, Sheng]]; [[Wang, Haohan]]"
url: "https://aclanthology.org/D19-6115/"
external_pdf: "https://aclanthology.org/D19-6115.pdf"
national_ethnic_cultural: N/A
religious_values: N/A
moral_psychology: N/A
newtags: "Bias & Fairness"
key_contribution: "Proposed DRiFt (Debiased Residual Fitting), a learning algorithm that removes known dataset biases (superficial cues) by fitting the residual of a 'biased' model."
significance: "Addresses the 'Clever Hans' effect in NLP, ensuring models learn robust semantic features rather than just memorizing spurious correlations (e.g., negation = contradiction) in training data."
tags: 
abstract: "Statistical natural language inference (NLI) models are susceptible to learning dataset bias: superficial cues that happen to associate with the label on a particular dataset, but are not useful in general, e.g., negation words indicate contradiction. As exposed by several recent challenge datasets, these models perform poorly when such association is absent, e.g., predicting that “I love dogs.” contradicts “I don’t love cats.”. Our goal is to design learning algorithms that guard against known dataset bias. We formalize the concept of dataset bias under the framework of distribution shift and present a simple debiasing algorithm based on residual fitting, which we call DRiFt. We first learn a biased model that only uses features that are known to relate to dataset bias. Then, we train a debiased model that fits to the residual of the biased model, focusing on examples that cannot be predicted well by biased features only. We use DRiFt to train three high-performing NLI models on two benchmark datasets, SNLI and MNLI. Our debiased models achieve significant gains over baseline models on two challenge test sets, while maintaining reasonable performance on the original test sets."
local_pdf: "[[PDFs/2019-He-Unlearn Dataset Bias in Natural Language.pdf]]"
pdf_extract: "PDF Extracts/2019-He-Unlearn Dataset Bias in Natural Language.md"
ethics_overall: No
virtue_ethics: No
deontological_ethics: No
utilitarian_ethics: No
ethics_perspective: "Bias & Fairness"
is_benchmark: Yes
is_eval: No
is_dataset: Yes
data_description: "Benchmark for bias and fairness dataset"
data_metrics: "Not specified"
---
# Unlearn Dataset Bias in Natural Language Inference by Fitting the Residual

## Authors

[[He He]], [[Sheng Zha]], [[Haohan Wang]]
## Metadata

**Year:** 2019

**Type:** document

## Links

- **ACL Anthology:** https://aclanthology.org/D19-6115/

## Abstract

Statistical natural language inference (NLI) models are susceptible to learning dataset bias: superficial cues that happen to associate with the label on a particular dataset, but are not useful in general, e.g., negation words indicate contradiction. As exposed by several recent challenge datasets, these models perform poorly when such association is absent, e.g., predicting that “I love dogs.” contradicts “I don’t love cats.”. Our goal is to design learning algorithms that guard against known dataset bias. We formalize the concept of dataset bias under the framework of distribution shift and present a simple debiasing algorithm based on residual fitting, which we call DRiFt. We first learn a biased model that only uses features that are known to relate to dataset bias. Then, we train a debiased model that fits to the residual of the biased model, focusing on examples that cannot be predicted well by biased features only. We use DRiFt to train three high-performing NLI models on two benchmark datasets, SNLI and MNLI. Our debiased models achieve significant gains over baseline models on two challenge test sets, while maintaining reasonable performance on the original test sets.

## Notes

