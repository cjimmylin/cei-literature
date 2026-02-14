---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0283
type: preprint
short_title: "CCD-Bench: Probing Cultural Conflict in LLM Decision-Making"
year: 2025
first_author: "[[Multiple authors]]"
last_author: "[[Multiple authors]]"
authors: "Multiple authors"
url: "https://arxiv.org/abs/2510.03553"
external_pdf: "https://arxiv.org/pdf/2510.03553.pdf"
pdf_extract: "PDF Extracts/2025/2025-authors-CCD-Bench Probing Cultural Conflict in LLM Decision-Making.md"
local_pdf: "[[PDFs/2025/2025-authors-CCD-Bench Probing Cultural Conflict in LLM Decision-Making.pdf]]"
publication: arXiv
DATE_ADDED: 20260207
ethics_overall: No
virtue_ethics: No
deontological_ethics: No
utilitarian_ethics: No
national_ethnic_cultural: "African/Ubuntu, Multicultural/Cross-cultural"
religious_values: N/A
religious_values_list: N/A
moral_psychology: N/A
newtags: 
is_benchmark: Yes
is_eval: Yes
is_dataset: No
tags: 
abstract: "Large language models (LLMs) increasingly shape interpersonal and societal decision-making, yet their ability to navigate explicit conflicts between legitimate cultural values remains underexplored. Existing benchmarks focus on cultural knowledge (CulturalBench), value inference (WorldValuesBench), or single-axis bias (CDEval), but none assess how LLMs adjudicate when multiple cultural frameworks directly clash."
ethics_perspective: "Social & Cultural Values"
data_description: "Benchmark for bias and fairness"
data_metrics: "Not specified"
LLM_assessed: "Claude, DeepSeek, Gemini, Llama, Llama-3, Phi, Mistral, ChatGPT, GPT-4, Qwen, Grok"
DATA_URL: "https://github.com/smartlab-nyu/CCD-Bench"
---
# CCD-Bench: Probing Cultural Conflict in LLM Decision-Making

## Authors

[[Multiple authors]]

## Metadata

**Authors:** Multiple authors

**Year:** 2025

**Type:** preprint

**Venue:** arXiv

## Links

- **arXiv:** https://arxiv.org/abs/2510.03553

## Abstract

Large language models (LLMs) increasingly shape interpersonal and societal decision-making, yet their ability to navigate explicit conflicts between legitimate cultural values remains underexplored. Existing benchmarks focus on cultural knowledge (CulturalBench), value inference (WorldValuesBench), or single-axis bias (CDEval), but none assess how LLMs adjudicate when multiple cultural frameworks directly clash. We introduce CCD-Bench, a benchmark for evaluating LLM decision-making under cross-cultural value conflict. CCD-Bench contains 2,182 open-ended dilemmas across seven domains, each with ten anonymized response options aligned with the ten GLOBE cultural clusters spanning 62 societies. Using a Stratified Latin Square design, we evaluate 17 leading LLMs and find clear biases: models favor Nordic Europe (20.2%) and Germanic Europe (12.4%), while Eastern Europe and Middle East & North Africa responses are least preferred (≈5–6%). Although 87.9% of model rationales reference multiple cultural dimensions, this pluralism is shallow-dominated by Future and Performance Orientation, with limited attention to Assertiveness or Gender Egalitarianism (<3%). Ordering effects are negligible, and model similarity clusters by developer lineage rather than geography. CCD-Bench shifts evaluation from bias detection to pluralistic reasoning, revealing that current LLMs express a Westerncentric, consensus-oriented worldview even when confronted with equally valid, culturally diverse alternatives. Code — https://github.com/smartlab-nyu/CCD-Bench

## Dataset Information

2,182 open-ended dilemmas spanning seven domains with ten response options from ten GLOBE cultural clusters

## Data Description

CCD-Bench (Culture-Conflict Decision Benchmark) contains 2,182 open-ended dilemmas across seven domains (Arts, Education, Family, Wellness, Work, Science, Lifestyle), each with ten anonymized response options aligned with the ten GLOBE cultural clusters spanning 62 societies. The benchmark evaluates 17 leading LLMs using a Stratified Latin Square design to assess how models navigate cross-cultural value conflicts. Responses were generated via multi-cluster prompting with OpenAI o3 and verified by human annotators.

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 1 (Citation Graph)
**Implementation Readiness:** HIGH

## Tags

