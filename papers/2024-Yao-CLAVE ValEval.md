---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0147
type: preprint
short_title: "CLAVE / ValEval"
year: 2024
first_author: "[[Jing Yao]]"
last_author: "[[X & Xie]]"
authors: "Jing Yao; Xu, Tianyi; X & Xie"
url: "https://arxiv.org/abs/2407.10725"
external_pdf: "https://arxiv.org/pdf/2407.10725.pdf"
pdf_extract: "PDF Extracts/2024/2024-Yao-CLAVE ValEval.md"
local_pdf: "[[Lit-WS-Lit-WS-PDFs/2024/2024-Yao-CLAVE ValEval.pdf]]"
publication: arXiv
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
mp_mft: 100
mp_schwartz: 50
mp_trolley: 0
mp_kohlberg: 0
mp_dual_process: 0
mp_intuitionist: 0
mp_dyadic: 0
mp_identity: 0
moral_psychology: "Moral Foundations Theory, Value Pluralism / Schwartz"
newtags: 
tags: 
abstract: "The rapid progress in Large Language Models (LLMs) poses potential risks such as generating unethical content. Assessing LLMs’ values helps expose their misalignment, but relies on reference-free evaluators, e.g., fine-tuned LLMs or close-source ones like GPT-4, to identify values reflected in generated responses. Nevertheless, these evaluators face two challenges in open-ended value evaluation: they should align with changing human value definitions with minimal annotation, against their own..."
LLM_assessed: "GPT-4, GPT-2, Mistral, Phi-3, Llama-2, Alpaca"
DATA_URL: "NA"
normative_ethics_benchmark: Borderline
CONFERENCE: "Preprint"
ethics_overall: 15
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
ethics_perspective: "AI Safety & Alignment"
nw_confucian: 5
nw_ubuntu: 0
nw_islamic_ethics: 0
nw_buddhist: 0
nw_dharmic: 0
nw_indigenous_relational: 0
nw_buen_vivir: 0
author_country: "US"
author_region: "North America"
author_global_north_south: "Global North"
weird_score: 78
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Benchmark for moral/ethical reasoning dataset"
data_metrics: "Not specified"
---
# CLAVE / ValEval

## Authors

[[Jing Yao]], [[Xu, Tianyi]], [[X & Xie]]

## Metadata

**Authors:** Yao, J., Yi, X., & Xie, X

**Year:** 2024

**Type:** preprint

**Venue:** arXiv

## Links

- **arXiv:** https://arxiv.org/abs/2407.10725

## Abstract

The rapid progress in Large Language Models (LLMs) poses potential risks such as generating unethical content. Assessing LLMs’ values helps expose their misalignment, but relies on reference-free evaluators, e.g., fine-tuned LLMs or close-source ones like GPT-4, to identify values reflected in generated responses. Nevertheless, these evaluators face two challenges in open-ended value evaluation: they should align with changing human value definitions with minimal annotation, against their own bias (adaptability), and detect varying value expressions and scenarios robustly (generalizability). To handle these challenges, we introduce CLAVE, a novel framework which integrates two complementary LLMs, a large one to extract high-level value concepts from a few human labels, leveraging its extensive knowledge and generalizability, and a smaller one fine-tuned on such concepts to better align with human value understanding. This dual-model approach enables calibration with any value systems using <100 human-labeled samples per value. Then we present ValEval, a comprehensive dataset comprising 13k+ (text,value,label) tuples across diverse domains, covering three major value systems. We benchmark the capabilities of 12+ popular LLM evaluators and analyze their strengths and weaknesses. Our findings reveal that combining fine-tuned small models and prompt-based large ones serves as a superior balance in value evaluation.

## Dataset Information

Size: 13,000+ (text, value, label) tuples

## Data Description

ValEval is a comprehensive value evaluation benchmark comprising 13,000+ annotated (text, value, label) tuples across 3 value systems (Social Risks, Schwartz Theory, Moral Foundation Theory), with original, perturbation, and generalization splits for benchmarking 12+ LLM evaluators.


## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 5
**Implementation Readiness:** MEDIUM

## Tags

