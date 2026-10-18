---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: YZ3ILWKS
type: conferencePaper
short_title: KorNAT
year: 2024
first_author: "[[Jiyoung Lee]]"
last_author: "[[Edward Choi]]"
authors: "Jiyoung Lee; Minwoo Kim; Seungho Kim; Junghwan Kim; Seunghyun Won; Hwaran Lee; Edward Choi"
doi: 10.18653/v1/2024.findings-acl.666
url: "https://aclanthology.org/2024.findings-acl.666/"
external_pdf: "file:///Users/jimmylin/Zotero/storage/K6EDWHWM/Lee et al. - 2024 - KorNAT LLM Alignment Benchmark for Korean Social Values and Common Knowledge.pdf"
national_ethnic_cultural: Korean
cultures_nationalities_list: Korean
languages_list: Korean
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
newtags: "Korean, AI Safety & Alignment"
key_contribution: "Created KorNAT, a benchmark for 'national alignment' with South Korea, comprising social values (survey-based) and common knowledge (textbook-based)."
significance: "Defines 'National Alignment' as a distinct goal from 'Human Alignment', showing that general models often fail on specific cultural norms (Korean values) even if they are generally 'helpful'."
tags: 
abstract: "For Large Language Models (LLMs) to be effectively deployed in a specific country, they must possess an understanding of the nation’s culture and basic knowledge. To this end, we introduce National Alignment, which measures an alignment between an LLM and a targeted country from two aspects: social value alignment and common knowledge alignment. Social value alignment evaluates how well the model understands nation-specific social values, while common knowledge alignment examines how well the..."
LLM_assessed: "Claude, GPT-3.5, GPT-4, Gemini, Llama-2, PaLM-2"
DATA_URL: "https://huggingface.co/datasets/datumo/KorNAT"
pdf_extract: "PDF Extracts/2024/2024-Lee-KorNAT.md"
local_pdf: "[[Lit-WS-PDFs/2024/2024-Lee-KorNAT.pdf]]"
publication: "arXiv / ACL Anthology"
CONF-CC: N/A
DATE_ADDED: 20260215
CONFERENCE: "ACL 2024"
ethics_overall: 100
virtue_ethics: 0
deontological_ethics: 5
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
ethics_perspective: "AI Safety & Alignment"
nw_confucian: 0
nw_ubuntu: 0
nw_islamic_ethics: 0
nw_buddhist: 0
nw_dharmic: 0
nw_indigenous_relational: 0
nw_buen_vivir: 0
author_country: KR
author_region: "East Asia"
author_global_north_south: "Global North"
weird_score: 63
is_benchmark: Yes
is_eval: Yes
is_dataset: Yes
data_description: "Benchmark dataset"
data_metrics: "Not specified"
---
# KorNAT: LLM Alignment Benchmark for Korean Social Values and Common Knowledge

## Metadata

**Authors:** Lee, Jiyoung; Kim, Minwoo; Kim, Seungho; Kim, Junghwan; Won, Seunghyun; Lee, Hwaran; Choi, Edward

**Year:** 2024

**Publication:** Findings of the Association for Computational Linguistics ACL 2024

**Type:** conferencePaper

**DOI:** [10.18653/v1/2024.findings-acl.666](https://doi.org/10.18653/v1/2024.findings-acl.666)

**Pages:** 11177-11213

**Publisher:** Association for Computational Linguistics

## Links

- **ACL Anthology:** https://aclanthology.org/2024.findings-acl.666
- **DOI:** https://doi.org/10.18653/v1/2024.findings-acl.666

## Abstract

To reliably deploy Large Language Models (LLMs) in a specific country, they must possess an understanding of the nation’s culture and basic knowledge. To this end, we introduce National Alignment, which measures the alignment between an LLM and a targeted country from two aspects: social value alignment and common knowledge alignment. We constructed KorNAT, the first benchmark that measures national alignment between LLMs and South Korea. KorNat contains 4K and 6K multiple-choice questions for social value and common knowledge, respectively. To attain an appropriately aligned ground truth in the social value dataset, we conducted a large-scale public survey with 6,174 South Koreans. For common knowledge, we created the data based on the South Korea text books and GED exams. Our dataset creation process is meticulously designed based on statistical sampling theory, and we also introduce metrics to measure national alignment, including three variations of social value alignment. We tested seven LLMs and found that only few models passed our reference score, indicating there exists room for improvement. Our dataset has received government approval following an assessment by a government-affiliated organization dedicated to evaluating dataset quality.

## Authors

[[Jiyoung Lee]], [[Minwoo Kim]], [[Seungho Kim]], [[Junghwan Kim]], [[Seunghyun Won]], [[Hwaran Lee]], [[Edward Choi]]

## Data Description

KorNAT: 10,000 multiple-choice questions (4K social value, 6K common knowledge) measuring national alignment between LLMs and South Korea; social value ground truth derived from a survey of 6,174 Korean participants; common knowledge based on Korean GED curriculum.


## Notes


## Citation Info

4 citations (Semantic Scholar/DOI) [2025-08-27] 4 citations (Crossref/DOI) [2025-08-23]
