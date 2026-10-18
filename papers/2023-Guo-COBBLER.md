---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: TSQJ734D
type: journalArticle
short_title: COBBLER
year: 2023
first_author: "[[Ryan Koo]]"
last_author: "[[Dongyeop Kang]]"
authors: "Ryan Koo; Minhwa Lee; Vipul Raheja; Jong Inn Park; Zae Myung Kim; Dongyeop Kang"
url: "https://arxiv.org/abs/2309.17012"
external_pdf: "https://arxiv.org/pdf/2309.17012.pdf"
national_ethnic_cultural: N/A
cultures_nationalities_list: N/A
languages_list: 
religious_values: N/A
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
religious_values_list: N/A
mp_mft: 0
mp_schwartz: 0
mp_trolley: 0
mp_kohlberg: 0
mp_dual_process: 0
mp_intuitionist: 0
mp_dyadic: 0
mp_identity: 0
moral_psychology: N/A
newtags: "Bias & Fairness"
key_contribution: "Introduced COBBLER to benchmark cognitive biases in LLM-as-a-judge (e.g., egocentric bias, order bias), finding machine preferences misaligned with humans (49% RBO)."
significance: "Critically evaluates the trend of using LLMs to evaluate other LLMs, showing that 'AI judges' have their own distinct cognitive biases that differ from human judges."
tags: 
pdf_extract: "PDF Extracts/2023/2023-Guo-COBBLER.md"
abstract: "Large Language Models (LLMs) have recently been shown to be effective as automatic evaluators with simple prompting and in-context learning. In this work, we assemble 16 LLMs encompassing four different size ranges and evaluate their output responses by preference ranking from the other LLMs as evaluators, such as System Star is better than System Square. We then evaluate the quality of ranking outputs introducing the COgnitive Bias Benchmark for LLMs as EvaluatoRs (COBBLER)1, a benchmark to..."
paper_summary: "Abstract: Large Language Models (LLMs) have recently been shown to be effective as automatic eval- uators with simple prompting and in-context learning. In this work, we assemble 16 LLMs encompassing four diffe | Overview: Benchmarking Cognitive Biases in Large Language Models as Evaluators Ryan Koo1 Minhwa Lee1 Vipul Raheja2 Jonginn Park1, Zae Myung Kim1 Dongyeop Kang1 1University of Minnesota, 2Grammarly {koo00017,lee | Key Findings: suites such as Fan et al. (2019) and Wang et al. (2020). With the increased usage of language mod- els as general-purpose assistants and their artifi- | Conclusions: For each bias, we analyze the performance of each of the 16 models as evaluators. We provide a vi- sual breakdown of the proportional impact of the av"
local_pdf: "[[Lit-WS-Lit-WS-PDFs/2023/2023-Guo-COBBLER.pdf]]"
CONF-CC: "ACL 2023"
DATE_ADDED: 20260208
LLM_assessed: "Alpaca, ChatGPT, Falcon, GPT-4, LLaMA, Llama-2, Mistral, MPT, Vicuna, WizardLM"
DATA_URL: "https://github.com/minnesotanlp/cobbler"
CONFERENCE: Journal
ethics_overall: 0
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 5
contractarian_ethics: 0
care_ethics: 15
ethics_perspective: "Bias & Fairness"
nw_confucian: 0
nw_ubuntu: 0
nw_islamic_ethics: 0
nw_buddhist: 0
nw_dharmic: 0
nw_indigenous_relational: 0
nw_buen_vivir: 0
author_country: US
author_region: "North America"
author_global_north_south: "Global North"
weird_score: 83
is_benchmark: Yes
is_eval: Yes
is_dataset: Yes
data_description: "Benchmark for bias and fairness dataset"
data_metrics: "Not specified"
---
# COBBLER: A Scrutinizing Benchmark for Assessing the Cognitive Bias of Large Language Models as Evaluators

## Metadata

**Authors:** Guo, X.; Zhang, B.; Wang, J.; Wang, H.; Zhang, Y.; Zhang, C.

**Year:** 2023

**Type:** journalArticle

## Links

- **Local PDF:** [[Lit-WS-Lit-WS-PDFs/2023/2023-Guo-COBBLER.pdf|Open PDF]]

- **arXiv:** https://arxiv.org/abs/2309.17012

## Abstract

Large Language Models are cognitively biased judges. Large Language Models (LLMs) have recently been shown to be effective as automatic evaluators with simple prompting and in-context learning. In this work, we assemble 15 LLMs of four different size ranges and evaluate their output responses by preference ranking from the other LLMs as evaluators, such as System Star is better than System Square. We then evaluate the quality of ranking outputs introducing the Cognitive Bias Benchmark for LLMs as Evaluators (CoBBLEr), a benchmark to measure six different cognitive biases in LLM evaluation outputs, such as the Egocentric bias where a model prefers to rank its own outputs highly in evaluation. We find that LLMs are biased text quality evaluators, exhibiting strong indications on our bias benchmark (average of 40% of comparisons across all models) within each of their evaluations that question their robustness as evaluators. Furthermore, we examine the correlation between human and machine preferences and calculate the average Rank-Biased Overlap (RBO) score to be 49.6%, indicating that machine preferences are misaligned with humans. According to our findings, LLMs may still be unable to be utilized for automatic annotation aligned with human preferences. Our project page is at: https://minnesotanlp.github.io/cobbler.

## Authors

[[Ryan Koo]], [[Minhwa Lee]], [[Vipul Raheja]], [[Jong Inn Park]], [[Zae Myung Kim]], [[Dongyeop Kang]]

## Data Description

COBBLER: a cognitive bias benchmark for evaluating LLMs as automatic evaluators, measuring six cognitive biases across 630K+ pairwise comparisons from 16 models.


## Notes


## Citation Info

98 citations (Semantic Scholar/arXiv) [2025-08-27]
