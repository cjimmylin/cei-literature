---


Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0006
type: preprint
short_title: JMedEthicBench
year: 2026
first_author: "[[Junyu Liu]]"
last_author: "[[Junyu Liu]]"
authors: Junyu Liu et al
authors_incomplete: true
url: "https://arxiv.org/abs/2601.01627"
external_pdf: "https://arxiv.org/pdf/2601.01627.pdf"
local_pdf: "[[PDFs/2026/2026-Liu-JMedEthicBench.pdf]]"
pdf_extract: "PDF Extracts/2026/2026-Liu-JMedEthicBench.md"
publication: arXiv preprint
DATE_ADDED: 20260207
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
national_ethnic_cultural: "Japanese"
religious_values: "N/A"
moral_psychology: "N/A"
newtags: 
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "No"
tags: 
abstract: "As Large Language Models (LLMs) are increasingly deployed in healthcare field, it becomes essential to carefully evaluate their medical safety before clinical use. However, existing safety benchmarks remain predominantly English-centric, and test with only single-turn prompts despite multi-turn clinical consultations. To address these gaps, we introduce JMedEthicBench, the first multi-turn conversational benchmark for evaluating medical safety of LLMs for Japanese healthcare."
ethics_perspective: "AI Safety & Alignment"
data_description: "Benchmark for ai safety"
data_metrics: "Not specified"
normative_ethics_benchmark: Borderline
---
# JMedEthicBench

## Authors

[[Junyu Liu]]

## Metadata

**Authors:** Junyu Liu et al

**Year:** 2026

**Type:** preprint

**Venue:** arXiv preprint

## Links

- **arXiv:** https://arxiv.org/abs/2601.01627

## Abstract

As Large Language Models (LLMs) are increasingly deployed in healthcare field, it becomes essential to carefully evaluate their medical safety before clinical use. However, existing safety benchmarks remain predominantly English-centric, and test with only single-turn prompts despite multi-turn clinical consultations. To address these gaps, we introduce JMedEthicBench, the first multi-turn conversational benchmark for evaluating medical safety of LLMs for Japanese healthcare. Our benchmark is based on 67 guidelines from the Japan Medical Association and contains over 50,000 adversarial conversations generated using seven automatically discovered jailbreak strategies. Using a dual-LLM scoring protocol, we evaluate 27 models and find that commercial models maintain robust safety while medical-specialized models exhibit increased vulnerability. Furthermore, safety scores decline significantly across conversation turns (median: 9.5 to 5.0, p < 0.001). Cross-lingual evaluation on both Japanese and English versions of our benchmark reveals that medical model vulnerabilities persist across languages, indicating inherent alignment limitations rather than language-specific factors. These findings suggest that domain-specific fine-tuning may accidentally weaken safety mechanisms and that multi-turn interactions represent a distinct threat surface requiring dedicated alignment strategies.

## Dataset Information

50,000+ adversarial conversations

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 14
**Implementation Readiness:** HIGH

## Tags

