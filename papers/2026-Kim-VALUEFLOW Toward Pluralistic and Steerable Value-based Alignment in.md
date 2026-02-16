---




Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0014
type: preprint
short_title: "VALUEFLOW: Toward Pluralistic and Steerable Value-based Alignment in Large Language Models"
year: 2025
first_author: "[[Woojin Kim]]"
last_author: "[[Jaeyoung Do]]"
authors: "Woojin Kim; Sieun Hyeon; Jusang Oh; Jaeyoung Do"
url: "https://arxiv.org/abs/2602.03160"
external_pdf: "https://arxiv.org/pdf/2602.03160.pdf"
pdf_extract: "PDF Extracts/2026/2026-Kim-VALUEFLOW Toward Pluralistic and Steerable Value-based Alignment in.md"
local_pdf: "[[PDFs/2026/2026-Kim-VALUEFLOW Toward Pluralistic and Steerable Value-based Alignment in.pdf]]"
publication: "arXiv preprint"
DATE_ADDED: 20260207
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "Yes"
tags: 
abstract: "Aligning Large Language Models (LLMs) with the diverse spectrum of human values remains a central challenge: preference-based methods often fail to capture deeper motivational principles. Value-based approaches offer a more principled path, yet three gaps persist– extraction often ignores hierarchical structure, evaluation detects presence but not calibrated intensity, and therefore, the steerability of LLMs at controlled intensities remains insufficiently understood."
ethics_perspective: "AI Safety & Alignment"
data_description: "Evaluation framework dataset"
data_metrics: "Not specified"
LLM_assessed: "GPT-4, Claude, Grok, Qwen, Mistral, Phi, Gemma"
DATA_URL: NA
---
# VALUEFLOW: Toward Pluralistic and Steerable Value-based Alignment in Large Language Models

## Authors

[[Woojin Kim]], [[Sieun Hyeon]], [[Jusang Oh]], [[Jaeyoung Do]]

## Metadata

**Authors:** Woojin Kim; Sieun Hyeon; Jusang Oh; Jaeyoung Do

**Year:** 2026

**Type:** preprint

**Venue:** arXiv preprint

## Links

- **arXiv:** https://arxiv.org/abs/2602.03160

## Abstract

Aligning Large Language Models (LLMs) with the diverse spectrum of human values remains a central challenge: preference-based methods often fail to capture deeper motivational principles. Value-based approaches offer a more principled path, yet three gaps persist– extraction often ignores hierarchical structure, evaluation detects presence but not calibrated intensity, and therefore, the steerability of LLMs at controlled intensities remains insufficiently understood. To address these limitations, we introduce VALUEFLOW, the first unified framework that spans extraction, evaluation, and steering with calibrated intensity control. The framework integrates three components: (i) HIVES, a hierarchical value embedding space that captures intra- and crosstheory value structure; (ii) the Value Intensity DataBase (VIDB), a large-scale resource of valuelabeled texts with intensity estimates derived from ranking-based aggregation; and (iii) an anchorbased evaluator that produces consistent intensity scores for model outputs by ranking them against VIDB panels. Using VALUEFLOW, we conduct a comprehensive large-scale study across ten models and four value theories, identifying asymmetries in steerability and composition laws for multi-value control. This paper establishes a scalable infrastructure for evaluating and controlling value intensity, advancing pluralistic alignment of LLMs.

## Dataset Information

See report

## Data Description

VALUEFLOW introduces a unified framework for value-based alignment in LLMs comprising HIVES (a hierarchical value embedding space), VIDB (a large-scale Value Intensity Database with 10K texts per value scored via Plackett-Luce aggregation), and a ranking-based evaluator. The study evaluates steerability across ten models (Qwen3-32B, Mistral-3.1-Small-24B, Phi-4, GLM-4-32B, gpt-oss-20b, Gemma-3-27B-it, GPT-4.1, Claude-4-Sonnet, Grok-4, Gemini-2.5-Flash) on 500 prompts spanning four value theories (SVT, MFT, Rights, Duties) with 32 values.

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 7-8, Agent 1
**Implementation Readiness:** MEDIUM

## Tags

