---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0108
type: preprint
short_title: "PrinciplismQA: Towards Assessing Medical Ethics from Knowledge to Practice"
year: 2025
first_author: "[[C. Hong]]"
last_author: [[Y]]
authors: "Hong, C., Wu, M., Xiao, Q., Wang, Y., Wan, X., Yu, G., Wang, B., & Hu, Y"
url: "https://arxiv.org/abs/2508.05132"
external_pdf: "https://arxiv.org/pdf/2508.05132.pdf"
local_pdf: "[[PDFs/2025/2025-Hong-PrinciplismQA Towards Assessing Medical Ethics from Knowledge to.pdf]]"
pdf_extract: "PDF Extracts/2025/2025-Hong-PrinciplismQA Towards Assessing Medical Ethics from Knowledge to.md"
publication: arXiv
DATE_ADDED: 20260207
ethics_overall: No
virtue_ethics: No
deontological_ethics: No
utilitarian_ethics: Yes
national_ethnic_cultural: N/A
religious_values: N/A
religious_values_list: N/A
moral_psychology: N/A
newtags: 
is_benchmark: Yes
is_eval: Yes
is_dataset: Yes
tags: 
abstract: "The integration of large language models into healthcare necessitates a rigorous evaluation of their ethical reasoning, an area current benchmarks often overlook. We introduce PrinciplismQA, a comprehensive benchmark with 3,648 questions designed to systematically assess LLMs’ alignment with core medical ethics. Grounded in Principlism, our benchmark features a high-quality dataset. This includes multiple-choice questions curated from authoritative textbooks and openended questions sourced from..."
data_description: "Benchmark for moral/ethical reasoning dataset for question answering"
data_metrics: "3,648 questions"
LLM_assessed: "GPT-4, o1, o3, Claude, Gemini, Gemma, Llama-3, Qwen, DeepSeek"
DATA_URL: NA
normative_ethics_benchmark: Yes
---
# PrinciplismQA: Towards Assessing Medical Ethics from Knowledge to Practice

## Authors

[[Hong]], [[C.]], [[Wenshan Wu|Wu]], [[M.]], [[Xiao]], [[Q.]], [[Wang]], [[Y.]], [[Wan]], [[X.]], [[Yu]], [[G.]], [[Wang]], [[B.]], [[& Hu]], [[Y]]

## Metadata

**Authors:** Hong, C., Wu, M., Xiao, Q., Wang, Y., Wan, X., Yu, G., Wang, B., & Hu, Y

**Year:** 2025

**Type:** preprint

**Venue:** arXiv

## Links

- **arXiv:** https://arxiv.org/abs/2508.05132

## Abstract

The integration of large language models into healthcare necessitates a rigorous evaluation of their ethical reasoning, an area current benchmarks often overlook. We introduce PrinciplismQA, a comprehensive benchmark with 3,648 questions designed to systematically assess LLMs’ alignment with core medical ethics. Grounded in Principlism, our benchmark features a high-quality dataset. This includes multiple-choice questions curated from authoritative textbooks and openended questions sourced from authoritative medical ethics case study literature, all validated by medical experts. Our experiments reveal a significant gap between models’ ethical knowledge and their practical application, especially in dynamically applying ethical principles to real-world scenarios. Most LLMs struggle with dilemmas concerning Beneficence, often over-emphasizing other principles. Frontier closed-source models, driven by strong general capabilities, currently lead the benchmark. Notably, medical domain fine-tuning can enhance models’ overall ethical competence, but further progress requires better alignment with medical ethical knowledge. PrinciplismQA offers a scalable framework to diagnose these specific ethical weaknesses, paving the way for more balanced and responsible medical AI.

## Dataset Information

PrinciplismQA benchmark: 3,648 questions total

## Data Description

PrinciplismQA is a comprehensive medical ethics benchmark with 3,648 questions (2,182 multiple-choice and 1,466 open-ended) designed to assess LLMs' alignment with the four core principles of medical ethics (Autonomy, Non-Maleficence, Beneficence, Justice). Over 20 models were evaluated including GPT-4.1, o3, o3-mini, Claude Sonnet 4, Gemini 2.5 Flash, DeepSeek-V3, DeepSeek-R1, Llama-3.1, Qwen2.5, Gemma3, and several medical LLMs (HuatuoGPT-o1, Med42, MedGemma).

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 6, Agent 14
**Implementation Readiness:** MEDIUM

## Tags

