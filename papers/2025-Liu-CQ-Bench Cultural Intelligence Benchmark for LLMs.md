---

Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0272
type: preprint
short_title: "CQ-Bench: Cultural Intelligence Benchmark for LLMs"
year: 2025
first_author: "[[Z. Liu]]"
authors: Liu, Z. et al.
url: "https://arxiv.org/abs/2504.01127"
external_pdf: "https://arxiv.org/pdf/2504.01127.pdf"
local_pdf: "[[PDFs/2025/2025-Liu-CQ-Bench Cultural Intelligence Benchmark for LLMs.pdf]]"
pdf_extract: "PDF Extracts/2025/2025-Liu-CQ-Bench Cultural Intelligence Benchmark for LLMs.md"
publication: arXiv
DATE_ADDED: 20260207
ethics_overall: "Yes"
virtue_ethics: "Yes"
deontological_ethics: "No"
utilitarian_ethics: "No"
national_ethnic_cultural: "Multicultural/Cross-cultural"
religious_values: "N/A"
moral_psychology: "N/A"
newtags: 
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "Yes"
tags: 
abstract: "Cultural Intelligence (CQ) refers to the ability to understand unfamiliar cultural contexts—a crucial skill for large language models (LLMs) to effectively engage with globally diverse users. Existing studies often focus on explicitly stated cultural norms, but fail to capture the subtle, implicit values that are common in daily conversation. To address this gap, we introduce CQ-Bench, a benchmark specifically designed to assess LLMs’ capability to infer implicit cultural values from natural..."
data_description: "Benchmark for moral/ethical reasoning text corpus for conversational ai"
data_metrics: "Not specified"
---
# CQ-Bench: Cultural Intelligence Benchmark for LLMs

## Authors

[[Liu, Z. et al.]]

## Metadata

**Authors:** Liu, Z. et al.

**Year:** 2025

**Type:** preprint

**Venue:** arXiv

## Links

- **arXiv:** https://arxiv.org/abs/2504.01127

## Abstract

Cultural Intelligence (CQ) refers to the ability to understand unfamiliar cultural contexts—a crucial skill for large language models (LLMs) to effectively engage with globally diverse users. Existing studies often focus on explicitly stated cultural norms, but fail to capture the subtle, implicit values that are common in daily conversation. To address this gap, we introduce CQ-Bench, a benchmark specifically designed to assess LLMs’ capability to infer implicit cultural values from natural conversational contexts. CQ-Bench consists of multi-character conversation-based stories using values from the World Value Survey and the GlobalOpinions, with topics including ethical, religious, social, etc. Our automatic dataset construction pipeline integrates rigorous validation procedures (incorporation, consistency, and implicitness checks), achieving a 94.5% human–model agreement in the final validation. To leverage CQ-Bench data, we design three tasks of increasing complexity: attitude detection, value selection, and value extraction. These tasks evaluate whether models can detect attitude and recognize values embedded within natural dialogues rather than relying on explicit cultural knowledge. We find that while frontier models like o1 reach human-level performance in value selection (0.809 F1), they still fall short in nuanced attitude detection (0.622 F1). Notably, fine-tuning a smaller LLaMA-3.2-3B on only 500 culturally-rich examples improves performance by over 10%, even outperforming o3-mini in some cases. Using CQ-Bench, we provide insights into the current challenges in LLMs’ CQ research and suggest practical pathways for enhancing LLMs’ cross-cultural reasoning abilities.

## Dataset Information

Benchmarks LLMs' metacognitive cultural intelligence for implicit cultural values across diverse contexts

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 1 (Citation Graph)
**Implementation Readiness:** MEDIUM

## Tags

