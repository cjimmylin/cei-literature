---



Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0040
type: conferencePaper
short_title: Deep Value Benchmark
year: 2025
first_author: "[[Joshua Ashkinaze]]"
authors: Joshua Ashkinaze, Hua Shen, Saipranav Avula, Eric Gilbert, Ceren Budak
url: "https://arxiv.org/abs/2511.02109"
external_pdf: "https://arxiv.org/pdf/2511.02109.pdf"
local_pdf: "[[PDFs/2025-Ashkinaze-Deep Value Benchmark.pdf]]"
pdf_extract: "PDF Extracts/2025-Ashkinaze-Deep Value Benchmark.md"
publication: NeurIPS 2025
DATE_ADDED: 20260207
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "Yes"
utilitarian_ethics: "No"
national_ethnic_cultural: "American"
religious_values: "N/A"
moral_psychology: "N/A"
newtags: 
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "Yes"
tags: 
abstract: "We introduce the Deep Value Benchmark (DVB), an evaluation framework that directly tests whether large language models (LLMs) learn fundamental human values or merely surface-level preferences. This distinction is critical for AI alignment: Systems that capture deeper values are likely to generalize human intentions robustly, while those that capture only superficial patterns in preference data risk producing misaligned behavior."
data_description: "Benchmark for moral/ethical reasoning dataset"
data_metrics: "Not specified"
normative_ethics_benchmark: Borderline
---
# Deep Value Benchmark

## Authors

[[Joshua Ashkinaze, Hua Shen, Saipranav Avula, Eric Gilbert, Ceren Budak]]

## Metadata

**Authors:** Joshua Ashkinaze, Hua Shen, Saipranav Avula, Eric Gilbert, Ceren Budak

**Year:** 2025

**Type:** conferencePaper

**Venue:** NeurIPS 2025

## Links

- **arXiv:** https://arxiv.org/abs/2511.02109

## Abstract

We introduce the Deep Value Benchmark (DVB), an evaluation framework that directly tests whether large language models (LLMs) learn fundamental human values or merely surface-level preferences. This distinction is critical for AI alignment: Systems that capture deeper values are likely to generalize human intentions robustly, while those that capture only superficial patterns in preference data risk producing misaligned behavior. The DVB uses a novel experimental design with controlled confounding between deep values (e.g., moral principles) and shallow features (e.g., superficial attributes). In the training phase, we expose LLMs to human preference data with deliberately correlated deep and shallow features—for instance, where a user consistently prefers (non-maleficence, formal language) options over (justice, informal language) alternatives. The testing phase then breaks these correlations, presenting choices between (justice, formal language) and (non-maleficence, informal language) options. This design allows us to precisely measure a model’s Deep Value Generalization Rate (DVGR)—the probability of generalizing based on the underlying value rather than the shallow feature. Across 9 different models, the average DVGR is just 0.30. All models generalize deep values less than chance. Larger models have a (slightly) lower DVGR than smaller models. We are releasing our dataset, which was subject to three separate human validation experiments. DVB provides an interpretable measure of a core feature of alignment.

## Dataset Information

Dataset with controlled confounds between deep values and shallow features; three separate human validation experiments

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 19, Agent 1
**Implementation Readiness:** HIGH

## Tags

