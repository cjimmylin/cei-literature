---








Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: WQ9NJRNZ
type: conferencePaper
short_title: "Improving Model Evaluation using SMART Filtering"
year: 2024
first_author: "[[Vipul Gupta]]"
last_author: "[[Adina Williams]]"
authors: "Vipul Gupta; Candace Ross; David Pantoja; Rebecca J. Passonneau; Megan Ung; Adina Williams"
doi: 10.48550/arXiv.2410.20245
url: "http://arxiv.org/abs/2410.20245"
external_pdf: "http://arxiv.org/pdf/2410.20245.pdf"
publication: "North American Chapter of the Association for Computational Linguistics"
CONF-CC: "NAACL 2024"
national_ethnic_cultural: "American"
cultures_nationalities_list: "N/A"
languages_list: "English"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: American
tags: 
pdf_extract: "PDF Extracts/2024/2024-Gupta-Improving Model Evaluation using SMART Filtering.md"
abstract: "One of the most challenging problems facing NLP today is evaluation. Some of the most pressing issues pertain to benchmark saturation, data contamination, and diversity in the quality of test examples. To address these concerns, we propose Selection Methodology for Accurate, Reduced, and Targeted (SMART) filtering, a novel approach to select a high-quality subset of examples from existing benchmark datasets by systematically removing less informative and less challenging examples."
paper_summary: "Abstract: One of the most challenging problems facing NLP today is evaluation. Some of the most pressing issues pertain to benchmark satura- tion, data contamination, and diversity in the quality of test exampl | Overview: Improving Model Evaluation using SMART Filtering of Benchmark Datasets Vipul Gupta1, 2, † Candace Ross1 David Pantoja3 Rebecca J. Passonneau2 Megan Ung1 Adina Williams1 1 FAIR, Meta AI 2 Pennsylvania  | Methodology: increases efficiency without hits to leaderboard util- ity. For example, on the ARC dataset, we shrink the dataset by 68.9%, increasing computational  | Key Findings: datasets, preserving the high-quality examples that are most informative and reliable as our basis for benchmarking. Our methodology applies three fil | Conclusions: Dataset Quality. Our approach removes the easy, data contaminated, and similar examples, thus im- proving the quality of the resulting dataset. Our me"
local_pdf: "[[PDFs/2024/2024-Gupta-Improving Model Evaluation using SMART Filtering.pdf]]"
DATE_ADDED: 20260208
LLM_assessed: "Qwen, Llama-3, Gemma, Phi, Mixtral"
DATA_URL: "NA"
ethics_overall: "No"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
research_topic: "Machine Learning"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Benchmark dataset for question answering"
data_metrics: "Not specified"
CONFERENCE: "NAACL 2024"
---
# Improving Model Evaluation using SMART Filtering of Benchmark Datasets

## Metadata

**Authors:** Gupta, Vipul; Ross, Candace; Pantoja, David; Passonneau, Rebecca J.; Ung, Megan; Williams, Adina

**Year:** 2025

**Type:** preprint

**DOI:** [10.48550/arXiv.2410.20245](https://doi.org/10.48550/arXiv.2410.20245)

**Publisher:** arXiv

## Links

- **Local PDF:** [[PDFs/2024/2024-Gupta-Improving Model Evaluation using SMART Filtering.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2410.20245
- **DOI:** https://doi.org/10.48550/arXiv.2410.20245

## Abstract

One of the most challenging problems facing NLP today is evaluation. Some of the most pressing issues pertain to benchmark saturation, data contamination, and diversity in the quality of test examples. To address these concerns, we propose Selection Methodology for Accurate, Reduced, and Targeted (SMART) filtering, a novel approach to select a high-quality subset of examples from existing benchmark datasets by systematically removing less informative and less challenging examples. Our approach applies three filtering criteria, removing (i) easy examples, (ii) data-contaminated examples, and (iii) examples that are similar to each other based on distance in an embedding space. We demonstrate the effectiveness of SMART filtering on three multiple choice QA datasets, where our methodology increases efficiency by reducing dataset size by 48% on average, while increasing Pearson correlation with rankings from ChatBot Arena, a more open-ended human evaluation setting. Our method enables us to be more efficient, whether using SMART filtering to make new benchmarks more challenging or to revitalize older datasets, while still preserving the relative model rankings.

## Authors

[[Vipul Gupta]], [[Candace Ross]], [[David Pantoja]], [[Rebecca J. Passonneau]], [[Megan Ung]], [[Adina Williams]]

## Data Description

The paper applies SMART (Selection Methodology for Accurate, Reduced, and Targeted) filtering to three multiple-choice QA benchmark datasets: ARC (3,530 examples, filtered to 1,097), MMLU (14,042 examples, filtered to 8,000), and CommonsenseQA (1,221 examples, filtered to 802). Eleven LLMs including Qwen2-72B, Llama-3.1-70B, Gemma-2-27b, Phi-3.5-MoE, and Mixtral-8x22B are evaluated on both original and SMART-filtered versions to demonstrate that filtering increases efficiency while preserving model rankings.


## Notes


## Tags

#Computer-Science---Artificial-Intelligence #Computer-Science---Machine-Learning #Computer-Science---Computation-and-Language

## Citation Info

4 citations (Semantic Scholar/DOI) [2025-08-27] 4 citations (Semantic Scholar/DOI) [2025-08-23]
