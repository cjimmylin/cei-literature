---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: 4NE573JG
type: conferencePaper
short_title: MedSafetyBench
year: 2025
first_author: "[[Tessa Han]]"
last_author: "[[Lakkaraju, Himabindu]]"
authors: "Han, Tessa; Kumar, Aounon; Agarwal, Chirag; Lakkaraju, Himabindu"
doi: 10.48550/arXiv.2403.03744
tags: 
url: "http://arxiv.org/abs/2403.03744"
pdf_extract: "PDF Extracts/2024/2024-Han-MedSafetyBench.md"
local_pdf: [[Lit-WS-Lit-WS-PDFs/2024/2024-Han-MedSafetyBench.pdf]]
external_pdf: "http://arxiv.org/pdf/2403.03744.pdf"
publication: "Neural Information Processing Systems"
CONF-CC: "NeurIPS 2024"
national_ethnic_cultural: N/A
cultures_nationalities_list: N/A
languages_list: English
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
newtags: "American, Utilitarianism"
key_contribution: "Defines 'medical safety' for LLMs based on AMA ethics principles and introduces MedSafetyBench to evaluating it"
significance: "First benchmark to operationalize medical ethics for LLMs, showing current models fail safety standards but can be improved via targeted fine-tuning without losing capability"
abstract: "As large language models (LLMs) develop increasingly sophisticated capabilities and find applications in medical settings, it becomes important to assess their medical safety due to their far-reaching implications for personal and public health, patient safety, and human rights. However, there is little to no understanding of the notion of medical safety in the context of LLMs, let alone how to evaluate and improve it."
paper_summary: "Abstract: As large language models (LLMs) develop increasingly sophisticated capabil- ities and find applications in medical settings, it becomes important to assess their medical safety due to their far-reachi | Overview: MedSafetyBench: Evaluating and Improving the Medical Safety of Large Language Models Tessa Han Harvard University Cambridge, MA than@g.harvard.edu Aounon Kumar Harvard University Cambridge, MA aokumar | Methodology: did not work with Llama-2-7b-chat, which declined to generate harmful medical requests. To circumvent this, with Llama-2-7b-chat, we employed a jailbr | Key Findings: was abnormal. | Conclusions: In this work, we study the medical safety of LLMs. We define the notion of medical safety for LLMs and leverage this definition to develop MedSafetyBe"
DATE_ADDED: 20260208
LLM_assessed: "GPT-3.5, GPT-4, GPT-4o, Llama-2, Llama-3, Mistral, Mixtral, Vicuna"
DATA_URL: "https://github.com/AI4LIFE-GROUP/med-safety-bench"
CONFERENCE: "NeurIPS 2024"
ethics_overall: No
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 10
contractarian_ethics: 0
care_ethics: 0
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
is_benchmark: Yes
is_eval: Yes
is_dataset: Yes
data_description: "Benchmark for ai safety dataset"
data_metrics: "Not specified"
---
 MedSafetyBench: Evaluating and Improving the Medical Safety of Large Language Models

## Authors

[[Tessa Han|Han, Tessa]], [[Aounon Kumar|Kumar, Aounon]], [[Chirag Agarwal|Agarwal, Chirag]], [[Himabindu Lakkaraju|Lakkaraju, Himabindu]]

## Links

- **Local PDF:** [[Lit-WS-Lit-WS-PDFs/2024/2024-Han-MedSafetyBench.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2403.03744
- **DOI:** https://doi.org/10.48550/arXiv.2403.03744

## Abstract

As large language models (LLMs) develop increasingly sophisticated capabilities and find applications in medical settings, it becomes important to assess their medical safety due to their far-reaching implications for personal and public health, patient safety, and human rights. However, there is little to no understanding of the notion of medical safety in the context of LLMs, let alone how to evaluate and improve it. To address this gap, we first define the notion of medical safety in LLMs based on the Principles of Medical Ethics set forth by the American Medical Association. We then leverage this understanding to introduce MedSafetyBench, the first benchmark dataset designed to measure the medical safety of LLMs. We demonstrate the utility of MedSafetyBench by using it to evaluate and improve the medical safety of LLMs. Our results show that publicly-available medical LLMs do not meet standards of medical safety and that fine-tuning them using MedSafetyBench improves their medical safety while preserving their medical performance. By introducing this new benchmark dataset, our work enables a systematic study of the state of medical safety in LLMs and motivates future work in this area, paving the way to mitigate the safety risks of LLMs in medicine. The benchmark dataset and code are available at https://github.com/AI4LIFE-GROUP/med-safety-bench.

## Data Description

First medical safety benchmark with 1,800 harmful medical requests based on AMA Principles of Medical Ethics, used to evaluate and improve medical safety of general and medical LLMs.


## Notes


## Tags

#Computer-Science---Artificial-Intelligence

## Citation Info

17 citations (Semantic Scholar/arXiv) [2025-08-27] 70 citations (Semantic Scholar/DOI) [2025-08-27]
