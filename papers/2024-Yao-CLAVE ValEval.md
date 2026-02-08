---



Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0147
type: preprint
short_title: CLAVE / ValEval
year: 2024
first_author: "[[J. Yao]]"
authors: "Yao, J., Yi, X., & Xie, X"
url: "https://arxiv.org/abs/2407.10725"
external_pdf: "https://arxiv.org/pdf/2407.10725.pdf"
local_pdf: "[[PDFs/2024/2024-Yao-CLAVE ValEval.pdf]]"
pdf_extract: "PDF Extracts/2024/2024-Yao-CLAVE ValEval.md"
publication: arXiv
DATE_ADDED: 20260207
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
national_ethnic_cultural: "N/A"
religious_values: "N/A"
moral_psychology: "N/A"
newtags: 
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "Yes"
tags: 
abstract: "The rapid progress in Large Language Models (LLMs) poses potential risks such as generating unethical content. Assessing LLMs’ values helps expose their misalignment, but relies on reference-free evaluators, e.g., fine-tuned LLMs or close-source ones like GPT-4, to identify values reflected in generated responses. Nevertheless, these evaluators face two challenges in open-ended value evaluation: they should align with changing human value definitions with minimal annotation, against their own..."
ethics_perspective: "AI Safety & Alignment"
data_description: "Benchmark for moral/ethical reasoning dataset"
data_metrics: "Not specified"
normative_ethics_benchmark: Borderline
---
# CLAVE / ValEval

## Authors

[[Yao, J., Yi, X., & Xie, X]]

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

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 5
**Implementation Readiness:** MEDIUM

## Tags

