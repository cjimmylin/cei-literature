---




































Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0045
type: preprint
short_title: "ELEPHANT (Social Sycophancy)"
year: 2025
first_author: "[[Myra Cheng]]"
last_author: "[[Dan Jurafsky]]"
authors: Myra Cheng; Sunny Yu; Cinoo Lee; Pranav Khadpe; Lujain Ibrahim; Dan Jurafsky
url: "https://arxiv.org/abs/2505.13995"
external_pdf: "https://arxiv.org/pdf/2505.13995.pdf"
pdf_extract: "PDF Extracts/2025/2025-Cheng-ELEPHANT Social Sycophancy.md"
local_pdf: "[[PDFs/2025/2025-Cheng-ELEPHANT Social Sycophancy.pdf]]"
publication: "arXiv preprint"
CONF-CC: "Preprint"
DATE_ADDED: 20260207
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: ""
religious_values: "N/A"
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
religious_values_list: "N/A"
mp_mft: 0
mp_schwartz: 0
mp_trolley: 0
mp_kohlberg: 0
mp_dual_process: 0
mp_intuitionist: 0
mp_dyadic: 0
mp_identity: 0
moral_psychology: "N/A"
newtags: 
tags: 
abstract: "LLMs are known to exhibit sycophancy: agreeing with and flattering users, even at the cost of correctness. Prior work measures sycophancy only as direct agreement with users’ explicitly stated beliefs that can be compared to a ground truth. This fails to capture broader forms of sycophancy such as affirming a user’s self-image or other implicit beliefs. To address this gap, we introduce social sycophancy, characterizing sycophancy as excessive preservation of a user’s face (their desired..."
LLM_assessed: "Claude, DeepSeek, GPT-4o, GPT-5, Llama-3, Mistral, Qwen"
DATA_URL: "https://github.com/myracheng/elephant"
CONFERENCE: "Preprint"
eleutherai: incorporated
ethics_overall: 15
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
research_topic: "Computer Vision & Multimodal"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "No"
data_description: "Benchmark"
data_metrics: "Not specified"
---
# ELEPHANT (Social Sycophancy)

## Authors

[[Myra Cheng]], [[Sunny Yu]], [[Cinoo Lee]], [[Pranav Khadpe]], [[Lujain Ibrahim]], [[Dan Jurafsky]]

## Metadata

**Authors:** Myra Cheng, Sunny Yu, Cinoo Lee, Pranav Khadpe, Lujain Ibrahim, Dan Jurafsky

**Year:** 2025

**Type:** preprint

**Venue:** arXiv preprint

## Links

- **arXiv:** https://arxiv.org/abs/2505.13995
- **Code/Data:** https://github.com/myracheng/elephant

## Abstract

LLMs are known to exhibit sycophancy: agreeing with and flattering users, even at the cost of correctness. Prior work measures sycophancy only as direct agreement with users’ explicitly stated beliefs that can be compared to a ground truth. This fails to capture broader forms of sycophancy such as affirming a user’s self-image or other implicit beliefs. To address this gap, we introduce social sycophancy, characterizing sycophancy as excessive preservation of a user’s face (their desired self-image), and present ELEPHANT, a benchmark for measuring social sycophancy in an LLM. Applying our benchmark to

## Dataset Information

Two evaluation datasets: open-ended questions (OEQ) and Reddit r/AmITheAsshole (AITA) posts; measures across 5 dimensions; comparison to human baselines

## Data Description

ELEPHANT is a benchmark for measuring social sycophancy in LLMs, grounded in Goffman's face theory, evaluating four dimensions (validation, indirectness, framing, moral sycophancy) across four datasets including Reddit r/AmITheAsshole posts and open-ended advice queries. The benchmark tests 11 production models including GPT-5, GPT-4o, Claude Sonnet 3.7, Gemini-1.5-Flash, Llama-3 variants (8B, 17B, 70B), Mistral (7B, 24B), DeepSeek-V3, and Qwen2.5-7B, finding that LLMs preserve user face 45 percentage points more than humans on average.

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 17
**Implementation Readiness:** HIGH

## Tags

