---

Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0072
type: preprint
short_title: "LLMs on Trial: Evaluating Judicial Fairness for Large Language Models (JudiFair)"
year: 2025
first_author: "[[Hu]]"
authors: Hu et al.
url: "https://arxiv.org/abs/2507.10852"
external_pdf: "https://arxiv.org/pdf/2507.10852.pdf"
local_pdf: "[[PDFs/2025-Hu-LLMs on Trial Evaluating Judicial Fairness for Large Language Models.pdf]]"
pdf_extract: "PDF Extracts/2025-Hu-LLMs on Trial Evaluating Judicial Fairness for Large Language Models.md"
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
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "Yes"
tags: 
abstract: "Large Language Models (LLMs) are increasingly used in high-stakes fields where their decisions impact rights and equity. However, LLMs’ judicial fairness and implications for social justice remain underexplored. When LLMs act as judges, the ability to fairly resolve judicial issues is a prerequisite to ensure their trustworthiness. Based on theories of judicial fairness, we construct a comprehensive framework to measure LLM fairness, leading to a selection of 65 labels and 161 corresponding..."
ethics_perspective: "Bias & Fairness"
data_description: "Evaluation framework dataset"
data_metrics: "Not specified"
---
# LLMs on Trial: Evaluating Judicial Fairness for Large Language Models (JudiFair)

## Authors

[[Hu et al.]]

## Metadata

**Authors:** Hu et al.

**Year:** 2025

**Type:** preprint

**Venue:** arXiv

## Links

- **arXiv:** https://arxiv.org/abs/2507.10852

## Abstract

Large Language Models (LLMs) are increasingly used in high-stakes fields where their decisions impact rights and equity. However, LLMs’ judicial fairness and implications for social justice remain underexplored. When LLMs act as judges, the ability to fairly resolve judicial issues is a prerequisite to ensure their trustworthiness. Based on theories of judicial fairness, we construct a comprehensive framework to measure LLM fairness, leading to a selection of 65 labels and 161 corresponding values. Applying this framework to the judicial system, we compile an extensive dataset, JudiFair, comprising 177,100 unique case facts. To achieve robust statistical inference, we develop three evaluation metrics—inconsistency, bias, and imbalanced inaccuracy—and introduce a method to assess the overall fairness of multiple LLMs across various labels. Through experiments with 16 LLMs, we uncover pervasive inconsistency, bias, and imbalanced inaccuracy across models, underscoring severe LLM judicial unfairness. Particularly, LLMs display notably more pronounced biases on demographic labels, with slightly less bias on substance labels compared to procedure ones. Interestingly, increased inconsistency correlates with reduced biases, but more accurate predictions exacerbate biases. While we find that adjusting the temperature parameter can influence LLM fairness, model size, release date, and country of origin do not exhibit significant effects on judicial fairness. Accordingly, we introduce a publicly available toolkit1, designed to support future research in evaluating and improving LLM fairness.

## Dataset Information

JudiFair dataset: 177,100 unique case facts

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 6
**Implementation Readiness:** HIGH

## Tags

