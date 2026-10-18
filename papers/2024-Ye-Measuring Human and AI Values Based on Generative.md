---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: E9AQ47CN
type: conferencePaper
short_title: "Measuring Human and AI Values Based on Generative"
year: 2024
first_author: "[[Haoran Ye]]"
last_author: "[[Guojie Song]]"
authors: "Haoran Ye; Yuhang Xie; Yuanyi Ren; Hanjun Fang; Xin Zhang; Guojie Song"
doi: 10.48550/arXiv.2409.12106
url: "http://arxiv.org/abs/2409.12106"
external_pdf: "http://arxiv.org/pdf/2409.12106.pdf"
publication: "AAAI Conference on Artificial Intelligence"
CONF-CC: "AAAI 2024"
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
mp_schwartz: 50
mp_trolley: 0
mp_kohlberg: 0
mp_dual_process: 0
mp_intuitionist: 0
mp_dyadic: 0
mp_identity: 0
moral_psychology: "Value Pluralism / Schwartz"
newtags: "Value Pluralism / Schwartz, AI Safety & Alignment"
key_contribution: "Introduced Generative Psychometrics for Values (GPV), a paradigm using LLMs to dynamically parse unstructured text into value-laden perceptions, akin to psychometric testing."
significance: "Demonstrates that LLM values can be measured from their free-form outputs rather than just fixed surveys, revealing how different value systems (e.g., Schwartz) predict model safety behaviors."
tags: 
pdf_extract: "PDF Extracts/2024/2024-Ye-Measuring Human and AI Values Based on Generative.md"
abstract: "Human values and their measurement are long-standing interdisciplinary inquiry. Recent advances in AI have sparked renewed interest in this area, with large language models (LLMs) emerging as both tools and subjects of value measurement. This work introduces Generative Psychometrics for Values (GPV), an LLM-based, data-driven value measurement paradigm, theoretically grounded in text-revealed selective perceptions."
paper_summary: "Abstract: Human values and their measurement are long-standing interdisciplinary inquiry. Recent advances in AI have sparked renewed interest in this area, with large lan- guage models (LLMs) emerging as both t | Overview: Measuring Human and AI Values Based on Generative Psychometrics with Large Language Models Haoran Ye∗,1, Yuhang Xie∗,2, Yuanyi Ren∗,1, Hanjun Fang3, Xin Zhang4, Guojie Song†,1,5 1State Key Laboratory  | Methodology: studies. Journal of personality and social psychology, 89(6):1010, 2005. [82] S. H. Schwartz, G. Melech, A. Lehmann, S. Burgess, M. Harris, and V. Owe | Key Findings: methods [43, 69, 100], which this work aims to address. 3 --- Page 4 --- 3 Generative Psychometrics for Values (GPV) | Conclusions: Relation to Self-Reports. The items organized in self-report inventories are essentially perceptions that support or oppose specific values [78]. Comp"
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
weird_score: 80
local_pdf: "[[Lit-WS-Lit-WS-PDFs/2024/2024-Ye-Measuring Human and AI Values Based on Generative.pdf]]"
DATE_ADDED: 20260208
LLM_assessed: "GPT-3.5, GPT-4, Gemma, InternLM, Llama-2, Mistral, Qwen-1.5, Vicuna, Yi"
DATA_URL: "https://github.com/Value4AI/gpv"
CONFERENCE: "AAAI 2024"
ethics_overall: 0
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 5
contractarian_ethics: 0
care_ethics: 0
ethics_perspective: "AI Safety & Alignment"
is_benchmark: No
is_eval: Yes
is_dataset: No
data_description: "Evaluation methodology"
data_metrics: "Not specified"
---
# Measuring Human and AI Values Based on Generative Psychometrics with Large Language Models

## Metadata

**Authors:** Ye, Haoran; Xie, Yuhang; Ren, Yuanyi; Fang, Hanjun; Zhang, Xin; Song, Guojie

**Year:** 2025

**Type:** preprint

**DOI:** [10.48550/arXiv.2409.12106](https://doi.org/10.48550/arXiv.2409.12106)

**Publisher:** arXiv

## Links

- **Local PDF:** [[Lit-WS-Lit-WS-PDFs/2024/2024-Ye-Measuring Human and AI Values Based on Generative.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2409.12106
- **DOI:** https://doi.org/10.48550/arXiv.2409.12106

## Abstract

Human values and their measurement are long-standing interdisciplinary inquiry. Recent advances in AI have sparked renewed interest in this area, with large language models (LLMs) emerging as both tools and subjects of value measurement. This work introduces Generative Psychometrics for Values (GPV), an LLM-based, data-driven value measurement paradigm, theoretically grounded in text-revealed selective perceptions. The core idea is to dynamically parse unstructured texts into perceptions akin to static stimuli in traditional psychometrics, measure the value orientations they reveal, and aggregate the results. Applying GPV to human-authored blogs, we demonstrate its stability, validity, and superiority over prior psychological tools. Then, extending GPV to LLM value measurement, we advance the current art with 1) a psychometric methodology that measures LLM values based on their scalable and free-form outputs, enabling context-specific measurement; 2) a comparative analysis of measurement paradigms, indicating response biases of prior methods; and 3) an attempt to bridge LLM values and their safety, revealing the predictive power of different value systems and the impacts of various values on LLM safety. Through interdisciplinary efforts, we aim to leverage AI for next-generation psychometrics and psychometrics for value-aligned AI.

## Authors

[[Haoran Ye]], [[Yuhang Xie]], [[Yuanyi Ren]], [[Hanjun Fang]], [[Xin Zhang]], [[Guojie Song]]

## Data Description

This paper introduces Generative Psychometrics for Values (GPV), an LLM-based value measurement paradigm that dynamically extracts perceptions from unstructured texts to measure value orientations across arbitrary value systems. The core model, ValueLlama, is a fine-tuned Llama-3-8B for perception-level and open-vocabulary value measurement. GPV was evaluated across 17 LLMs and 4 value theories, using GPT-3.5 Turbo for text parsing and GPT-4 Turbo for comparison, demonstrating superior construct validity and predictive power for LLM safety compared to self-report questionnaires and dictionary-based methods.


## Notes


## Tags

#Computer-Science---Artificial-Intelligence #Computer-Science---Computation-and-Language

## Citation Info

3 citations (Semantic Scholar/DOI) [2025-08-27] 98 citations (Semantic Scholar/arXiv) [2025-08-27] 3 citations (Semantic Scholar/DOI) [2025-08-23]
