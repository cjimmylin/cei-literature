---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0253
type: preprint
short_title: "VAL-Bench: Belief Consistency as a Measure for Value Alignment"
year: 2025
first_author: "[[Aman Gupta]]"
last_author: "[[Fazl Barez]]"
authors: "Aman Gupta; Denny O'Shea; Fazl Barez"
url: "https://arxiv.org/abs/2510.05465"
external_pdf: "https://arxiv.org/pdf/2510.05465.pdf"
pdf_extract: "PDF Extracts/2025/2025-Gupta-VAL-Bench Belief Consistency as a Measure for Value Alignment.md"
local_pdf: "[[Lit-WS-Lit-WS-PDFs/2025/2025-Gupta-VAL-Bench Belief Consistency as a Measure for Value Alignment.pdf]]"
publication: arXiv
CONF-CC: Preprint
DATE_ADDED: 20260207
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
abstract: "Large language models (LLMs) are increasingly being used for tasks where outputs shape human decisions, so it is critical to verify that their responses consistently reflect desired human values. Humans, as individuals or groups, don’t agree on a universal set of values, which makes evaluating value alignment difficult. Existing benchmarks often use hypothetical or commonsensical situations, which don’t capture the complexity and ambiguity of real-life debates."
LLM_assessed: "Claude, Claude-2, Claude-3, DeepSeek, GPT-3.5, GPT-4, GPT-4o, Llama-2, Llama-3, Mistral, Qwen"
DATA_URL: "https://github.com/val-bench/VAL-Bench"
CONFERENCE: Preprint
ethics_overall: 100
virtue_ethics: 5
deontological_ethics: 0
utilitarian_ethics: 5
contractarian_ethics: 5
care_ethics: 0
ethics_perspective: "Moral Reasoning & Psychology"
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
data_description: "Benchmark dataset"
data_metrics: "Not specified"
---
# VAL-Bench: Belief Consistency as a Measure for Value Alignment

## Authors

[[Aman Gupta]], [[Denny O'Shea]], [[Fazl Barez]]

## Metadata

**Authors:** Gupta, A. et al.

**Year:** 2025

**Type:** preprint

**Venue:** arXiv

## Links

- **arXiv:** https://arxiv.org/abs/2510.05465

## Abstract

Large language models (LLMs) are increasingly being used for tasks where outputs shape human decisions, so it is critical to verify that their responses consistently reflect desired human values. Humans, as individuals or groups, don’t agree on a universal set of values, which makes evaluating value alignment difficult. Existing benchmarks often use hypothetical or commonsensical situations, which don’t capture the complexity and ambiguity of real-life debates. We introduce the Value ALignment Benchmark (VAL-Bench1), which measures the consistency in language model belief expressions in response to real-life valueladen prompts. VAL-Bench consists of 115K pairs of prompts designed to elicit opposing stances on a controversial issue, extracted from Wikipedia. We use an LLM-as-a-judge, validated against human annotations, to evaluate if the pair of responses consistently expresses either a neutral or a specific stance on the issue. Applied across leading open- and closed-source models, the benchmark shows considerable variation in consistency rates (ranging from ∼10% to ∼80%), with Claude models the only ones to achieve high levels of consistency. Lack of consistency in this manner risks epistemic harm by making user beliefs dependent on how questions are framed rather than on underlying evidence, and undermines LLM reliability in trust-critical applications. Therefore, we stress the importance of research towards training belief consistency in modern LLMs. By providing a scalable, reproducible benchmark, VAL-Bench enables systematic measurement of necessary conditions for value alignment.

## Dataset Information

115K pairs of prompts from Wikipedia eliciting opposing stances on controversial issues

## Data Description

VAL-Bench: 115K paired prompts mined from Wikipedia controversial sections designed to elicit opposing stances on value-laden issues, used to measure LLM belief consistency as a necessary condition for value alignment.


## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 1 (Citation Graph)
**Implementation Readiness:** HIGH

## Tags

