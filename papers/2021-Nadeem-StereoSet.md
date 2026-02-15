---


Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXA5Y72K
type: conferencePaper
short_title: StereoSet
year: 2025
first_author: "[[Moin Nadeem]]"
last_author: "[[Siva Reddy]]"
authors: "Moin Nadeem; Anna Bethke; Siva Reddy"
doi: 10.48550/arXiv.2004.09456
url: "http://arxiv.org/abs/2004.09456"
external_pdf: "http://arxiv.org/pdf/2004.09456.pdf"
publication: "Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics (ACL 2021)"
national_ethnic_cultural: "N/A"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: "Bias & Fairness"
key_contribution: "Released StereoSet, a large-scale dataset to measure stereotypical bias in PLMs across gender, profession, race, and religion."
significance: "One of the pivotal benchmarks that proved widely used models (BERT, GPT-2) exhibit strong stereotypical biases, spurring the development of de-biasing techniques."
tags: 
pdf_extract: "PDF Extracts/2021/2021-Nadeem-StereoSet.md"
abstract: "A stereotype is an over-generalized belief about a particular group of people, e.g., Asians are good at math or Asians are bad drivers. Such beliefs (biases) are known to hurt target groups. Since pretrained language models are trained on large real world data, they are known to capture stereotypical biases. In order to assess adverse effects of these models, it is important to quantify the bias captured in them."
paper_summary: "Abstract: A stereotype is an over-generalized belief about a particular group of people, e.g., Asians are good at math or Asians are bad drivers. Such beliefs (biases) are known to hurt tar- get groups. Since p | Overview: StereoSet: Measuring stereotypical bias in pretrained language models Moin Nadeem§∗and Anna Bethke† and Siva Reddy‡ §Massachusetts Institute of Technology, Cambridge MA, USA †Intel AI, Santa Clara CA, | Conclusions: Table 4 shows the overall results of baselines and models on StereoSet. Baselines vs. Models As seen in Table 4, all pretrained models have higher lms"
local_pdf: [[PDFs/2021/2021-Nadeem-StereoSet.pdf]]
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "Bias & Fairness"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Benchmark for bias and fairness dataset"
data_metrics: "Not specified"
LLM_assessed: "BERT, GPT-2, RoBERTa, XLNet"
DATA_URL: "https://stereoset.mit.edu"
---
# StereoSet: Measuring stereotypical bias in pretrained language models

## Metadata

**Authors:** Nadeem, Moin; Bethke, Anna; Reddy, Siva

**Year:** 2020

**Type:** preprint

**DOI:** [10.48550/arXiv.2004.09456](https://doi.org/10.48550/arXiv.2004.09456)

**Publisher:** arXiv

## Links

- **Local PDF:** [[PDFs/2021/2021-Nadeem-StereoSet.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2004.09456
- **DOI:** https://doi.org/10.48550/arXiv.2004.09456

## Abstract

A stereotype is an over-generalized belief about a particular group of people, e.g., Asians are good at math or Asians are bad drivers. Such beliefs (biases) are known to hurt target groups. Since pretrained language models are trained on large real world data, they are known to capture stereotypical biases. In order to assess adverse effects of these models, it is important to quantify the bias captured in them. Existing literature on quantifying bias evaluates pretrained language models on a small set of artiﬁcially constructed bias-assessing sentences. We present StereoSet, a large-scale natural dataset in English to measure stereotypical biases in four domains: gender, profession, race, and religion. We evaluate popular models like BERT, GPT2, ROBERTA, and XLNET on our dataset and show that these models exhibit strong stereotypical biases. We also present a leaderboard with a hidden test set to track the bias of future language models at https://stereoset. mit.edu.

## Authors

[[Moin Nadeem]], [[Anna Bethke]], [[Siva Reddy]]

## Data Description

StereoSet is a large-scale English-language dataset containing 16,995 crowdsourced test instances (triplets) designed to measure stereotypical biases in pretrained language models across four domains: gender, profession, race, and religion. The dataset uses Context Association Tests (CATs) at both intrasentence and intersentence levels, with 321 target terms and options labeled as stereotype, anti-stereotype, or unrelated. BERT, GPT-2, RoBERTa, and XLNet (each in base and large variants) were evaluated on the dataset.


## Notes


## Tags

#Computer-Science---Artificial-Intelligence #Computer-Science---Computers-and-Society #Computer-Science---Computation-and-Language

## Citation Info

1078 citations (Semantic Scholar/arXiv) [2025-08-27] 1071 citations (Semantic Scholar/arXiv) [2025-08-23]
