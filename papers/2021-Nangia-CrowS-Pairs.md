---

Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0247
type: conferencePaper
short_title: CrowS-Pairs
year: 2021
first_author: "[[Nikita Nangia]]"
authors: Nikita Nangia, Clara Vania, Rasika Bhalerao, Samuel R. Bowman
url: "https://arxiv.org/abs/2010.00133"
external_pdf: "https://arxiv.org/pdf/2010.00133.pdf"
local_pdf: "[[PDFs/2021/2021-Nangia-CrowS-Pairs.pdf]]"
pdf_extract: "PDF Extracts/2021/2021-Nangia-CrowS-Pairs.md"
publication: EMNLP 2020
DATE_ADDED: 20260207
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
national_ethnic_cultural: "American"
religious_values: "N/A"
moral_psychology: "N/A"
newtags: 
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "Yes"
tags: 
abstract: "Warning: This paper contains explicit statements of offensive stereotypes and may be upsetting. Pretrained language models, especially masked language models (MLMs) have seen success across many NLP tasks. However, there is ample evidence that they use the cultural biases that are undoubtedly present in the corpora they are trained on, implicitly creating harm with biased representations. To measure some forms of social bias in language models against protected demographic groups in the US, we..."
ethics_perspective: "Bias & Fairness"
data_description: "Benchmark for bias and fairness text corpus"
data_metrics: "1508 examples"
---
# CrowS-Pairs

## Authors

[[Nikita Nangia, Clara Vania, Rasika Bhalerao, Samuel R. Bowman]]

## Metadata

**Authors:** Nikita Nangia, Clara Vania, Rasika Bhalerao, Samuel R. Bowman

**Year:** 2021

**Type:** conferencePaper

**Venue:** EMNLP 2020

## Links

- **arXiv:** https://arxiv.org/abs/2010.00133
- **Code/Data:** https://github.com/nyu-mll/crows-pairs; https://github.com/EleutherAI/lm-evaluation-harness

## Abstract

Warning: This paper contains explicit statements of offensive stereotypes and may be upsetting. Pretrained language models, especially masked language models (MLMs) have seen success across many NLP tasks. However, there is ample evidence that they use the cultural biases that are undoubtedly present in the corpora they are trained on, implicitly creating harm with biased representations. To measure some forms of social bias in language models against protected demographic groups in the US, we introduce the Crowdsourced Stereotype Pairs benchmark (CrowS-Pairs). CrowS-Pairs has 1508 examples that cover stereotypes dealing with nine types of bias, like race, religion, and age. In CrowS-Pairs a model is presented with two sentences: one that is more stereotyping and another that is less stereotyping. The data focuses on stereotypes about historically disadvantaged groups and contrasts them with advantaged groups. We ﬁnd that all three of the widelyused MLMs we evaluate substantially favor sentences that express stereotypes in every category in CrowS-Pairs. As work on building less biased models advances, this dataset can be used as a benchmark to evaluate progress.

## Dataset Information

1,508 sentence pairs (stereotypical vs. anti-stereotypical); crowdsourced

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 17
**Implementation Readiness:** HIGH

## Tags

