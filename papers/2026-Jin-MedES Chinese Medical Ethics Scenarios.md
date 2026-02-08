---


Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0008
type: preprint
short_title: MedES (Chinese Medical Ethics Scenarios)
year: 2026
first_author: "[[Haoan Jin]]"
authors: Haoan Jin, Han Ying, Jiacheng Ji, Hanhui Xu, and Mengyue Wu
url: "https://arxiv.org/abs/2601.07954"
external_pdf: "https://arxiv.org/pdf/2601.07954.pdf"
local_pdf: "[[PDFs/2026/2026-Jin-MedES Chinese Medical Ethics Scenarios.pdf]]"
pdf_extract: "PDF Extracts/2026/2026-Jin-MedES Chinese Medical Ethics Scenarios.md"
publication: arXiv preprint
DATE_ADDED: 20260207
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
national_ethnic_cultural: "Chinese"
religious_values: "N/A"
moral_psychology: "N/A"
newtags: 
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "Yes"
tags: 
abstract: "Recent advances in large language models (LLMs) have enabled their application to a range of healthcare tasks. However, aligning LLMs with the nuanced demands of medical ethics, especially under complex real-world scenarios, remains underexplored. In this work, we present MedES, a dynamic, scenario-centric benchmark specifically constructed from 260 authoritative Chinese medical, ethical, and legal sources to reflect the challenges in clinical decision-making."
ethics_perspective: "Applied Ethics"
data_description: "Benchmark for moral/ethical reasoning text corpus"
data_metrics: "Not specified"
normative_ethics_benchmark: Borderline
---
# MedES (Chinese Medical Ethics Scenarios)

## Authors

[[Haoan Jin, Han Ying, Jiacheng Ji, Hanhui Xu, and Mengyue Wu]]

## Metadata

**Authors:** Haoan Jin, Han Ying, Jiacheng Ji, Hanhui Xu, and Mengyue Wu

**Year:** 2026

**Type:** preprint

**Venue:** arXiv preprint

## Links

- **arXiv:** https://arxiv.org/abs/2601.07954

## Abstract

Recent advances in large language models (LLMs) have enabled their application to a range of healthcare tasks. However, aligning LLMs with the nuanced demands of medical ethics, especially under complex real-world scenarios, remains underexplored. In this work, we present MedES, a dynamic, scenario-centric benchmark specifically constructed from 260 authoritative Chinese medical, ethical, and legal sources to reflect the challenges in clinical decision-making. To facilitate model alignment, we introduce a guardian-inthe-loop framework that leverages a dedicated automated evaluator—trained on expert-labeled data and achieving over 97% accuracy within our domain—to generate targeted prompts and provide structured ethical feedback. Using this pipeline, we align a 7B-parameter LLM through supervised fine-tuning and domain-specific preference optimization. Experimental results, conducted entirely within the Chinese medical ethics context, demonstrate that our aligned model outperforms notably larger baselines on core ethical tasks, with observed improvements in both quality and composite evaluation metrics. Our work offers a practical and adaptable framework for aligning LLMs with medical ethics in the Chinese healthcare domain, and suggests that similar alignment pipelines may be instantiated in other legal and cultural environments through modular replacement of the underlying normative corpus. Code — https://github.com/X-LANCE/MedEthicAlign Datasets — https://github.com/X-LANCE/MedEthicAlign

## Dataset Information

12 real-world high-risk clinical scenarios

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 14
**Implementation Readiness:** MEDIUM

## Tags

