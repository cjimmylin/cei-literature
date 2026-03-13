---





























Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: RTSV27JH
type: preprint
short_title: ValueDCG
year: 2024
first_author: "[[Zhaowei Zhang]]"
last_author: "[[Yaodong Yang]]"
authors: "Zhaowei Zhang; Fengshuo Bai; Jun Gao; Yaodong Yang"
doi: 10.48550/arXiv.2310.00378
url: "http://arxiv.org/abs/2310.00378"
external_pdf: "http://arxiv.org/pdf/2310.00378.pdf"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: ""
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: "Moral Reasoning & Psychology"
key_contribution: "Developed ValueDCG, a metric to distinguish between an LLM's 'know what' (superficial knowledge) and 'know why' (deep understanding) of human values."
significance: "Shows that while larger models improve at 'knowing what', their ability to 'understand why' often stagnates or declines, suggesting they may act as 'stochastic parrots' of values without true alignment."
tags: 
pdf_extract: "PDF Extracts/2024/2024-Zhang-ValueDCG.md"
abstract: "Personal values are a crucial factor behind human decision-making. Considering that Large Language Models (LLMs) have been shown to impact human decisions significantly, it is essential to make sure they accurately understand human values to ensure their safety. However, evaluating their grasp of these values is complex due to the value’s intricate and adaptable nature. We argue that truly understanding values in LLMs requires considering both “know what” and “know why”."
paper_summary: "Abstract: Personal values are a crucial factor behind hu- man decision-making. Considering that Large Language Models (LLMs) have been shown to impact human decisions significantly, it is essential to make sure | Overview: ValueDCG: Measuring Comprehensive Human Value Understanding Ability of Language Models Zhaowei Zhang1,2, Fengshuo Bai1,2*, Jun Gao3, Yaodong Yang1, 1Institute for Artificial Intelligence, Peking Unive | Methodology: Our method proposes a measurement ValueDCG with an engineering implementation framework that can effectively quantify the DCG (Saunders et al., 2022)  | Key Findings: framework quantifies both 'know what' and 'know why' and computes ValueDCG based on their dis- crepancy. For the input requirements, we input the data"
local_pdf: "[[PDFs/2024/2024-Zhang-ValueDCG.pdf]]"
CONF-CC: "Preprint"
DATE_ADDED: 20260208
LLM_assessed: "Llama-2, Llama-3"
DATA_URL: "https://github.com/zowiezhang/ValueDCG"
CONFERENCE: "Preprint"
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "Moral Reasoning & Psychology"
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "No"
data_description: "Evaluation approach"
data_metrics: "Not specified"
---
# ValueDCG: Measuring Comprehensive Human Value Understanding Ability of Language Models

## Metadata

**Authors:** Zhang, Zhaowei; Bai, Fengshuo; Gao, Jun; Yang, Yaodong

**Year:** 2024

**Type:** preprint

**DOI:** [10.48550/arXiv.2310.00378](https://doi.org/10.48550/arXiv.2310.00378)

**Publisher:** arXiv

## Links

- **Local PDF:** [[PDFs/2024/2024-Zhang-ValueDCG.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2310.00378
- **DOI:** https://doi.org/10.48550/arXiv.2310.00378

## Abstract

Personal values are a crucial factor behind human decision-making. Considering that Large Language Models (LLMs) have been shown to impact human decisions significantly, it is essential to make sure they accurately understand human values to ensure their safety. However, evaluating their grasp of these values is complex due to the value’s intricate and adaptable nature. We argue that truly understanding values in LLMs requires considering both “know what” and “know why”. To this end, we present a comprehensive evaluation metric, ValueDCG (Value Discriminator-Critique Gap), to quantitatively assess the two aspects with an engineering implementation. We assess four representative LLMs and provide compelling evidence that the growth rates of LLM’s “know what” and “know why” capabilities do not align with increases in parameter numbers, resulting in a decline in the models’ capacity to understand human values as larger amounts of parameters. This may further suggest that LLMs might craft plausible explanations based on the provided context without truly understanding their inherent value, indicating potential risks. Our code has been released at https: //github.com/zowiezhang/ValueDCG.

## Authors

[[Zhaowei Zhang]], [[Fengshuo Bai]], [[Jun Gao]], [[Yaodong Yang]]

## Data Description

ValueDCG proposes a comprehensive evaluation metric measuring the discrepancy between LLMs' 'know what' (discriminator) and 'know why' (critique) capabilities regarding human values understanding. Four open-source LLMs (Llama-2 7B/13B/70B and Llama-3 8B) are evaluated across 13 human value types from the ETHICS and ValueNet datasets, using attribution analysis, counterfactual analysis, and rebuttal argument dimensions, with GPT-4o serving as the automated evaluator.


## Notes


## Tags

#Computer-Science---Artificial-Intelligence #Computer-Science---Computers-and-Society #Computer-Science---Computation-and-Language

## Citation Info

3 citations (Semantic Scholar/arXiv) [2025-08-27] 0 citations (Semantic Scholar/DOI) [2025-08-27] 3 citations (Semantic Scholar/arXiv) [2025-08-23]
