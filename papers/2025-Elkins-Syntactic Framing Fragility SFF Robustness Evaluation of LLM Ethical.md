---






















Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0262
type: preprint
short_title: "Syntactic Framing Fragility (SFF): Robustness Evaluation of LLM Ethical Decisions"
year: 2025
first_author: "[[K. Elkins]]"
last_author: "[[J. Chun]]"
authors: "K. Elkins; J. Chun"
url: "https://arxiv.org/abs/2601.09724"
external_pdf: "https://arxiv.org/pdf/2601.09724.pdf"
pdf_extract: "PDF Extracts/2025/2025-Elkins-Syntactic Framing Fragility SFF Robustness Evaluation of LLM Ethical.md"
local_pdf: "[[PDFs/2025/2025-Elkins-Syntactic Framing Fragility SFF Robustness Evaluation of LLM Ethical.pdf]]"
publication: arXiv
CONF-CC: "Preprint"
DATE_ADDED: 20260207
national_ethnic_cultural: "Chinese, American"
cultures_nationalities_list: "Chinese, American"
languages_list: ""
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
tags: 
abstract: "Large language models (LLMs) are increasingly deployed in consequential decision-making settings, yet their robustness to benign prompt variation remains underexplored. In this work, we study whether LLMs maintain consistent ethical judgments across logically equivalent but syntactically different prompts, focusing on variations involving negation and conditional structure. We introduce Syntactic Framing Fragility (SFF), a robustness evaluation framework that isolates purely syntactic effects..."
LLM_assessed: "Claude, Grok, DeepSeek, Llama-3, Phi, Gemma, Qwen"
DATA_URL: "NA"
CONFERENCE: "Preprint"
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "Yes"
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "No"
data_description: "Evaluation framework"
data_metrics: "Not specified"
---
# Syntactic Framing Fragility (SFF): Robustness Evaluation of LLM Ethical Decisions

## Authors

[[Elkins]], [[K. & Chun]], [[Johnstun, J.|J.]]

## Metadata

**Authors:** Elkins, K. & Chun, J.

**Year:** 2025

**Type:** preprint

**Venue:** arXiv

## Links

- **arXiv:** https://arxiv.org/abs/2601.09724

## Abstract

Large language models (LLMs) are increasingly deployed in consequential decision-making settings, yet their robustness to benign prompt variation remains underexplored. In this work, we study whether LLMs maintain consistent ethical judgments across logically equivalent but syntactically different prompts, focusing on variations involving negation and conditional structure. We introduce Syntactic Framing Fragility (SFF), a robustness evaluation framework that isolates purely syntactic effects via Logical Polarity Normalization (LPN), enabling direct comparison of decisions across positive and negative framings without semantic drift. Auditing 23 state-of-the-art models spanning the U.S. and China as well as small U.S. open-source software models over 14 ethical scenarios and four controlled framings (39,975 decisions), we find widespread and statistically significant inconsistency: many models reverse ethical endorsements solely due to syntactic polarity, with open-source models exhibiting over twice the fragility of commercial counterparts. We further uncover extreme negation sensitivity, where some models endorse actions in 80–97% of cases when explicitly prompted with “should not.” We show that eliciting chain-of-thought reasoning substantially reduces fragility, identifying a practical mitigation lever, and we map fragility across scenarios, finding higher risk in financial and business contexts than in medical scenarios. Our results demonstrate that syntactic consistency constitutes a distinct and critical dimension of ethical robustness, and we argue that SFF-style audits should be a standard component of safety evaluation for deployed LLMs. Our code and results will be available on github.com.

## Dataset Information

39,975 ethical decisions from 23 models across 14 scenarios using Logical Polarity Normalization

## Data Description

The paper introduces the Syntactic Framing Fragility (SFF) audit framework, evaluating 23 LLMs across three origin categories (US commercial, Chinese commercial, and US open-source) on 14 ethical scenarios spanning 7 domains with four controlled syntactic framings, yielding 39,975 decisions. Models tested include Claude (Haiku-4-5, Sonnet-4-5), Gemini-3-flash, Grok-4-1, DeepSeek-v3p2, Llama-3.2, Phi-4-mini, Gemma-3, Qwen-3, and others, assessed for consistency of ethical judgments under logically equivalent syntactic transformations.

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 1 (Citation Graph)
**Implementation Readiness:** MEDIUM

## Tags

