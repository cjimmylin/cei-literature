---



Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: TSQJ734D
type: journalArticle
short_title: COBBLER
year: 2025
first_author: "[[Ryan Koo]]"
last_author: "[[Dongyeop Kang]]"
authors: "Ryan Koo; Minhwa Lee; Vipul Raheja; Jong Inn Park; Zae Myung Kim; Dongyeop Kang"
url: "https://arxiv.org/abs/2309.17012"
external_pdf: "https://arxiv.org/pdf/2309.17012.pdf"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: "Bias & Fairness"
key_contribution: "Introduced COBBLER to benchmark cognitive biases in LLM-as-a-judge (e.g., egocentric bias, order bias), finding machine preferences misaligned with humans (49% RBO)."
significance: "Critically evaluates the trend of using LLMs to evaluate other LLMs, showing that 'AI judges' have their own distinct cognitive biases that differ from human judges."
tags: 
pdf_extract: "PDF Extracts/2023/2023-Guo-COBBLER.md"
abstract: "Large Language Models (LLMs) have recently been shown to be effective as automatic evaluators with simple prompting and in-context learning. In this work, we assemble 16 LLMs encompassing four different size ranges and evaluate their output responses by preference ranking from the other LLMs as evaluators, such as System Star is better than System Square. We then evaluate the quality of ranking outputs introducing the COgnitive Bias Benchmark for LLMs as EvaluatoRs (COBBLER)1, a benchmark to..."
paper_summary: "Abstract: Large Language Models (LLMs) have recently been shown to be effective as automatic eval- uators with simple prompting and in-context learning. In this work, we assemble 16 LLMs encompassing four diffe | Overview: Benchmarking Cognitive Biases in Large Language Models as Evaluators Ryan Koo1 Minhwa Lee1 Vipul Raheja2 Jonginn Park1, Zae Myung Kim1 Dongyeop Kang1 1University of Minnesota, 2Grammarly {koo00017,lee | Key Findings: suites such as Fan et al. (2019) and Wang et al. (2020). With the increased usage of language mod- els as general-purpose assistants and their artifi- | Conclusions: For each bias, we analyze the performance of each of the 16 models as evaluators. We provide a vi- sual breakdown of the proportional impact of the av"
local_pdf: [[PDFs/2023/2023-Guo-COBBLER.pdf]]
DATE_ADDED: 20260208
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
LLM_assessed: "GPT-4, ChatGPT, InstructGPT, Llama, Llama-2, Alpaca, Falcon, Vicuna, Mistral"
DATA_URL: "https://github.com/minnesotanlp/cobbler"
---
# COBBLER: A Scrutinizing Benchmark for Assessing the Cognitive Bias of Large Language Models as Evaluators

## Metadata

**Authors:** Guo, X.; Zhang, B.; Wang, J.; Wang, H.; Zhang, Y.; Zhang, C.

**Year:** 2023

**Type:** journalArticle

## Links

- **Local PDF:** [[PDFs/2023/2023-Guo-COBBLER.pdf|Open PDF]]

- **arXiv:** https://arxiv.org/abs/2309.17012

## Abstract

Large Language Models are cognitively biased judges. Large Language Models (LLMs) have recently been shown to be effective as automatic evaluators with simple prompting and in-context learning. In this work, we assemble 15 LLMs of four different size ranges and evaluate their output responses by preference ranking from the other LLMs as evaluators, such as System Star is better than System Square. We then evaluate the quality of ranking outputs introducing the Cognitive Bias Benchmark for LLMs as Evaluators (CoBBLEr), a benchmark to measure six different cognitive biases in LLM evaluation outputs, such as the Egocentric bias where a model prefers to rank its own outputs highly in evaluation. We find that LLMs are biased text quality evaluators, exhibiting strong indications on our bias benchmark (average of 40% of comparisons across all models) within each of their evaluations that question their robustness as evaluators. Furthermore, we examine the correlation between human and machine preferences and calculate the average Rank-Biased Overlap (RBO) score to be 49.6%, indicating that machine preferences are misaligned with humans. According to our findings, LLMs may still be unable to be utilized for automatic annotation aligned with human preferences. Our project page is at: https://minnesotanlp.github.io/cobbler.

## Authors

[[Ryan Koo]], [[Minhwa Lee]], [[Vipul Raheja]], [[Jong Inn Park]], [[Zae Myung Kim]], [[Dongyeop Kang]]

## Data Description

COBBLER (COgnitive Bias Benchmark for LLMs as EvaluatoRs) benchmarks 16 LLMs for six cognitive biases when used as automatic text quality evaluators. The benchmark uses 50 question-answering instructions from BigBench and ELI5 datasets, generating over 630,000 pairwise comparisons across all models. The six biases measured include order bias, compassion fade, egocentric bias, salience bias, bandwagon effect, and attentional bias, categorized into implicit and induced types.


## Notes


## Citation Info

98 citations (Semantic Scholar/arXiv) [2025-08-27]
