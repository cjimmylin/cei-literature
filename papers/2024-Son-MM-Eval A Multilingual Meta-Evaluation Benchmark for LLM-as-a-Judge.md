---


Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0444
type: preprint
short_title: "MM-Eval: A Multilingual Meta-Evaluation Benchmark for LLM-as-a-Judge and Reward Models"
year: 2024
first_author: "[[Guijin Son]]"
last_author: "[[Guijin Son]]"
authors: Guijin Son, et al.
url: "https://arxiv.org/abs/2410.17578"
external_pdf: "https://arxiv.org/pdf/2410.17578.pdf"
publication: arXiv
local_pdf: "[[PDFs/2024/2024-Son-MM-Eval A Multilingual Meta-Evaluation Benchmark for LLM-as-a-Judge.pdf]]"
pdf_extract: "PDF Extracts/2024/2024-Son-MM-Eval A Multilingual Meta-Evaluation Benchmark for LLM-as-a-Judge.md"
DATE_ADDED: 20260213
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "Yes"
utilitarian_ethics: "No"
national_ethnic_cultural: "N/A"
languages_list: "122 languages for consistency, 18 languages including French"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "No"
data_description: "Multilingual benchmark for bias and fairness"
data_metrics: "18 languages; 122 languages"
LLM_assessed: "GPT-4, GPT-4o, Claude models, various LLM-as-a-Judge and reward models"
DATA_URL: "https://github.com/guijinSON/MM-Eval"
tags: 
abstract: "As Large Language Models (LLMs) are now capable of producing fluent and coherent content in languages other than English, it is not imperative to precisely evaluate these non-English outputs. However, when assessing the outputs from mutlilingual LLMs, prior works often employed LLM based evaluators that excel at assessing English outputs, without a thorough examination of whether these evaluators could effectively assess non-English text as well."
---
# MM-Eval: A Multilingual Meta-Evaluation Benchmark for LLM-as-a-Judge and Reward Models

## Authors

[[Guijin Son, et al.]]

## Metadata

**Authors:** Guijin Son, et al.

**Year:** 2024

**Type:** preprint

**Venue:** arXiv

**Languages:** 122 languages for consistency, 18 languages including French

**Benchmark:** MM-Eval

## Links

- **arXiv:** https://arxiv.org/abs/2410.17578
- **Code/Data:** https://github.com/guijinSON/MM-Eval

## Abstract

Multilingual meta-evaluation benchmark with five core subsets (Chat, Reasoning, Safety, Language Hallucination, Linguistics) spanning 18 languages. Models achieve only 68.9% average accuracy (50% = random). Safety subset performance in low-resource languages is 18.4% lower than English.

## Data Description

MM-Eval is a multilingual meta-evaluation benchmark with five core subsets (Chat, Reasoning, Safety, Language Hallucination, Linguistics) spanning 18 languages. Models achieve only 68.9% average accuracy (50% = random). Safety subset performance in low-resource languages is 18.4% lower than English, revealing significant degradation in non-English safety evaluation.


## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B6
**Relevance:** Evaluates LLM-as-a-Judge reliability for safety assessment in French. Shows significant degradation in non-English safety evaluation accuracy.

## Tags

