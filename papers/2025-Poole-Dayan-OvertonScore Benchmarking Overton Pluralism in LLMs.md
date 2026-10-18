---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0273
type: preprint
short_title: "OvertonScore: Benchmarking Overton Pluralism in LLMs"
year: 2025
first_author: "[[Elinor Poole-Dayan]]"
last_author: "[[Michiel A. Bakker]]"
authors: "Elinor Poole-Dayan; Jiayi Wu; Taylor Sorensen; Jiaxin Pei; Michiel A. Bakker"
url: "https://arxiv.org/abs/2512.01351"
external_pdf: "https://arxiv.org/pdf/2512.01351.pdf"
pdf_extract: "PDF Extracts/2025/2025-Poole-Dayan-OvertonScore Benchmarking Overton Pluralism in LLMs.md"
local_pdf: "[[Lit-WS-Lit-WS-PDFs/2025/2025-Poole-Dayan-OvertonScore Benchmarking Overton Pluralism in LLMs.pdf]]"
publication: arXiv
CONF-CC: Preprint
DATE_ADDED: 20260207
national_ethnic_cultural: American
cultures_nationalities_list: American
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
abstract: "We introduce a novel framework for measuring Overton pluralism in LLMs—the extent to which diverse viewpoints are represented in model outputs. We (i) formalize Overton pluralism as a set coverage metric (OVERTONSCORE), (ii) conduct a large-scale U.S.-representative human study (N = 1209; 60 questions; 8 LLMs), and (iii) develop an automated benchmark that closely reproduces human judgments. On average, models achieve OVERTONSCOREs of 0.35–0."
LLM_assessed: "Claude-3, DeepSeek, GPT-4, Gemma, Llama-3, o1"
DATA_URL: NA
CONFERENCE: Preprint
ethics_overall: 0
virtue_ethics: 0
deontological_ethics: 0
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
author_country: US
author_region: "North America"
author_global_north_south: "Global North"
weird_score: 78
is_benchmark: Yes
is_eval: Yes
is_dataset: No
data_description: Benchmark
data_metrics: "60 questions"
---
# OvertonScore: Benchmarking Overton Pluralism in LLMs

## Authors

[[Elinor Poole-Dayan]], [[Jiayi Wu]], [[Taylor Sorensen]], [[Jiaxin Pei]], [[Michiel A. Bakker]]

## Metadata

**Authors:** Poole-Dayan, E. et al.

**Year:** 2025

**Type:** preprint

**Venue:** arXiv

## Links

- **arXiv:** https://arxiv.org/abs/2512.01351

## Abstract

We introduce a novel framework for measuring Overton pluralism in LLMs—the extent to which diverse viewpoints are represented in model outputs. We (i) formalize Overton pluralism as a set coverage metric (OVERTONSCORE), (ii) conduct a large-scale U.S.-representative human study (N = 1209; 60 questions; 8 LLMs), and (iii) develop an automated benchmark that closely reproduces human judgments. On average, models achieve OVERTONSCOREs of 0.35–0.41, with DeepSeek V3 performing best; yet all models remain far below the theoretical maximum of 1.0, revealing substantial headroom for improvement. Because repeated large-scale human studies are costly and slow, scalable evaluation tools are essential for model development. Hence, we propose an automated benchmark that achieves high rank correlation with human judgments (ρ = 0.88), providing a practical proxy without replacing human assessment. By turning pluralistic alignment from a normative aim into a measurable benchmark, our work establishes a foundation for systematic progress toward more pluralistic LLMs.

## Dataset Information

OvertonScore metric validated against 1,209 human respondents across 60 questions and 8 models

## Data Description

The benchmark comprises 60 subjective questions (15 from Model Slant and 45 from PRISM) evaluated by 1,209 U.S.-representative participants who rated outputs from 8 LLMs on a 1-5 Likert scale for perceived representation. The resulting dataset contains 29,016 data points (1,209 participants x 3 questions x 8 LLMs) with free-form written responses, representation ratings, and agree/disagree votes used to cluster participants into distinct viewpoints for computing the OvertonScore metric.

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 1 (Citation Graph)
**Implementation Readiness:** HIGH

## Tags

