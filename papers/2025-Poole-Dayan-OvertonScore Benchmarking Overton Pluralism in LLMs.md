---








Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0273
type: preprint
short_title: "OvertonScore: Benchmarking Overton Pluralism in LLMs"
year: 2025
first_author: "[[E. Poole-Dayan]]"
last_author: "[[Michiel A. Bakker]]"
authors: "Elinor Poole-Dayan; Jiayi Wu; Taylor Sorensen; Jiaxin Pei; Michiel A. Bakker"
url: "https://arxiv.org/abs/2512.01351"
external_pdf: "https://arxiv.org/pdf/2512.01351.pdf"
pdf_extract: "PDF Extracts/2025/2025-Poole-Dayan-OvertonScore Benchmarking Overton Pluralism in LLMs.md"
local_pdf: "[[PDFs/2025/2025-Poole-Dayan-OvertonScore Benchmarking Overton Pluralism in LLMs.pdf]]"
publication: arXiv
CONF-CC: "Preprint"
DATE_ADDED: 20260207
national_ethnic_cultural: "American"
cultures_nationalities_list: "American"
languages_list: ""
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
tags: 
abstract: "We introduce a novel framework for measuring Overton pluralism in LLMs—the extent to which diverse viewpoints are represented in model outputs. We (i) formalize Overton pluralism as a set coverage metric (OVERTONSCORE), (ii) conduct a large-scale U.S.-representative human study (N = 1209; 60 questions; 8 LLMs), and (iii) develop an automated benchmark that closely reproduces human judgments. On average, models achieve OVERTONSCOREs of 0.35–0."
LLM_assessed: "GPT-4, Gemma, DeepSeek, Llama-3, Claude"
DATA_URL: "NA"
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "AI Safety & Alignment"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "No"
data_description: "Benchmark"
data_metrics: "60 questions"
CONFERENCE: "Preprint"
---
# OvertonScore: Benchmarking Overton Pluralism in LLMs

## Authors

[[Elinor Poole-Dayan]], [[Jiayi Wu]], [[Taylor Sorensen]], [[Jian Pei|Jiaxin Pei]], [[Michiel Bakker|Michiel A. Bakker]]

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

