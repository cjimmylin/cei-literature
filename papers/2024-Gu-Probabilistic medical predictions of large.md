---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: NA333TMH
type: journalArticle
short_title: "Probabilistic medical predictions of large"
year: 2024
first_author: "[[Bowen Gu]]"
last_author: "[[Jie Yang]]"
authors: "Bowen Gu; Rishi J. Desai; Kueiyu Joshua Lin; Jie Yang"
doi: 10.1038/s41746-024-01366-4
url: "https://www.nature.com/articles/s41746-024-01366-4"
external_pdf: "file:///Users/jimmylin/Zotero/storage/MQMSE9SR/Gu et al. - 2024 - Probabilistic medical predictions of large language models.pdf"
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
newtags: 
tags: 
research_topic: Other
abstract: "Large Language Models (LLMs) have shown promise in clinical applications through prompt engineering, allowing flexible clinical predictions. However, they struggle to produce reliable prediction probabilities, which are crucial for transparency and decision-making. While explicit prompts can lead LLMs to generate probability estimates, their numerical reasoning limitations raise concerns about reliability."
CONF-CC: "npj Digital Medicine"
DATE_ADDED: 20260208
LLM_assessed: "Gemma-2, Llama-3, Mistral, Phi-3, Qwen-2, Yi-1.5"
DATA_URL: "https://github.com/gubowen2/Probabilistic-Medical-Predictions-of-Large-Language-Models"
pdf_extract: "PDF Extracts/2024/2024-Gu-Probabilistic medical predictions of large.md"
local_pdf: "[[Lit-WS-PDFs/2024/2024-Gu-Probabilistic medical predictions of large.pdf]]"
CONFERENCE: Journal
ethics_overall: 30
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
ethics_perspective: "Applied Ethics"
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
weird_score: 78
is_benchmark: No
is_eval: No
is_dataset: Yes
data_description: Dataset
data_metrics: "Not specified"
---
# Probabilistic medical predictions of large language models

## Metadata

**Authors:** Gu, Bowen; Desai, Rishi J.; Lin, Kueiyu Joshua; Yang, Jie

**Year:** 2024

**Publication:** npj Digital Medicine

**Type:** journalArticle

**DOI:** [10.1038/s41746-024-01366-4](https://doi.org/10.1038/s41746-024-01366-4)

**Pages:** 367

**Volume/Issue:** Vol. 7, Issue 1

## Links

- **URL:** https://www.nature.com/articles/s41746-024-01366-4
- **DOI:** https://doi.org/10.1038/s41746-024-01366-4

## Abstract

Large Language Models (LLMs) have shown promise in clinical applications through prompt engineering, allowing flexible clinical predictions. However, they struggle to produce reliable prediction probabilities, which are crucial for transparency and decision-making. While explicit prompts can lead LLMs to generate probability estimates, their numerical reasoning limitations raise concerns about reliability. We compared explicit probabilities from text generation to implicit probabilities derived from the likelihood of predicting the correct label token. Across six advanced open-source LLMs and five medical datasets, explicit probabilities consistently underperformed implicit probabilities in discrimination, precision, and recall. This discrepancy is more pronounced with smaller LLMs and imbalanced datasets, highlighting the need for cautious interpretation, improved probability estimation methods, and further research for clinical use of LLMs.

## Authors

[[Bowen Gu]], [[Rishi J. Desai]], [[Kueiyu Joshua Lin]], [[Jie Yang]]

## Detailed Summary

This paper investigates a critical but often overlooked aspect of LLM deployment in healthcare: the reliability of probability estimates that accompany predictions. In clinical settings, probabilistic outputs are essential for informed decision-making, patient stratification, and allowing clinicians to set appropriate thresholds based on their preferred trade-offs between recall and precision. The authors distinguish between two types of probability outputs: "explicit" probabilities obtained by directly prompting LLMs to state their confidence (e.g., "Please provide the probability along with your prediction"), and "implicit" probabilities derived from the likelihood scores assigned to label tokens during generation.

The study evaluated six advanced open-source LLMs (Qwen2-72B, Llama-3.1-70B, Gemma-2-27b, Mistral-Large, Yi-1.5-34B, and Phi-3-medium) across five medical datasets including MMLU Clinical Knowledge, MMLU College Medicine, USMLE, MCMLE (Chinese), and MGB-SDoH (real-world EHR data). The researchers converted multi-choice questions to binary format to enable proper AUROC and AUPRC evaluation. A key finding is that explicit probabilities consistently underperform implicit probabilities across all LLMs and datasets in terms of discrimination, precision, and recall metrics.

The performance gap between explicit and implicit probabilities is particularly pronounced with smaller LLMs and when dealing with imbalanced datasets, a common scenario in clinical contexts where rare diseases or adverse outcomes are of interest. The authors also observed that explicit probabilities tend to cluster around round numbers (e.g., 90%, 80%), creating coarse-grained ROC curves, while implicit probabilities provide finer granularity. Notably, some models produced contradictory outputs where the stated explicit probability was below 50% despite selecting a particular answer, fundamentally undermining reliability. These findings have important implications for the responsible deployment of LLMs in healthcare applications.

## Paper Outline

1. Introduction - Establishes importance of probabilistic predictions in clinical AI
2. Results - Presents LLM performance, comparison of large vs. small models, imbalanced dataset analysis
3. Discussion - Interprets findings and discusses implications for clinical use
4. Methods - Describes data sources, experiment settings, probability extraction, and evaluation metrics

## Methods Summary

The study used five medical datasets: four public benchmarks (MMLU-CK, MMLU-CM, USMLE, MCMLE) and one private EHR dataset (MGB-SDoH). Questions were converted to binary format, with correct and incorrect options randomly assigned as A or B to avoid position bias. LLMs were prompted to output predictions with explicit probability estimates. Implicit probabilities were extracted from token transition scores. Experiments were run at three temperature settings (0, 0.3, 0.7) to calculate standard deviations. Statistical significance was assessed using one-sided paired t-tests.

## Results Summary

All LLMs achieved at least 80% average accuracy across datasets. However, AUROC and AUPRC for implicit probabilities were consistently and significantly higher than for explicit probabilities. The Llama-3.1-70B model achieved the highest average accuracy. Smaller models showed larger discrepancies between explicit and implicit probability metrics. On imbalanced datasets, the AUPRC difference increased as imbalance grew more severe. Explicit probability distributions were highly polarized regardless of prediction correctness, suggesting overconfidence.

## Conclusions

The study demonstrates that explicit probabilities from LLMs are less reliable than implicit probabilities, particularly for smaller models and imbalanced datasets common in clinical settings. This unreliability can amplify biases and lead to misinformed clinical decisions. The authors recommend caution when using explicit probability estimates in healthcare and suggest future work on fine-tuning explicit outputs using implicit probability supervision.

## Artifact Contributions

- Code repository: https://github.com/gubowen2/Probabilistic-Medical-Predictions-of-Large-Language-Models
- Framework for evaluating probabilistic reliability of LLMs in medical contexts

## Data Description

Evaluation framework comparing explicit vs implicit probability estimation methods across 6 open-source LLMs and 5 medical datasets for clinical prediction tasks.


## Notes


## Citation Info

21 citations (Semantic Scholar/DOI) [2025-08-27] 13 citations (Semantic Scholar/DOI) [2025-08-23] 4 citations (Crossref/DOI) [2025-08-23]
