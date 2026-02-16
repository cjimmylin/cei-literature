---



Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0010
type: preprint
short_title: PluriHarms
year: 2025
first_author: "[[Li, Jing-Jing]]"
last_author: "[[Levine, Sydney]]"
authors: "[[Li, Jing-Jing]]; [[Mire, Joel]]; [[Fleisig, Eve]]; [[Pyatkin, Valentina]]; [[Collins, Anne]]; [[Sap, Maarten]]; [[Levine, Sydney]]"
authors_incomplete: false
url: "https://arxiv.org/abs/2601.08951"
external_pdf: "https://arxiv.org/pdf/2601.08951.pdf"
pdf_extract: "PDF Extracts/0000/2026-Li-PluriHarms.md"
local_pdf: "[[PDFs/2026/2026-Li-PluriHarms.pdf]]"
publication: "arXiv preprint"
DATE_ADDED: 20260207
ethics_overall: "No"
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
is_eval: "No"
is_dataset: "No"
tags: 
abstract: "Current AI safety frameworks, which often treat harmfulness as binary, lack the flexibility to handle borderline cases where humans meaningfully disagree. To build more pluralistic systems, it is essential to move beyond consensus and instead understand where and why disagreements arise. We introduce PLURIHARMS, a benchmark designed to systematically study human harm judgments across two key dimensions—the harm axis (benign to harmful) and the agreement axis (agreement to disagreement)."
ethics_perspective: "AI Safety & Alignment"
data_description: "N/A"
data_metrics: "Not specified"
LLM_assessed: "GPT-4, Claude, Qwen, DeepSeek"
DATA_URL: "https://jl3676.github.io/PluriHarms"
research_topic: "Other"
---
# PluriHarms

## Authors

[[Li, Jing-Jing]], [[Mire, Joel]], [[Eve Fleisig|Fleisig, Eve]], [[Valentina Pyatkin|Pyatkin, Valentina]], [[Collins, Anne]], [[Maarten Sap|Sap, Maarten]], [[Sydney Levine|Levine, Sydney]]

## Metadata

**Authors:** Li, Jing-Jing; Mire, Joel; Fleisig, Eve; Pyatkin, Valentina; Collins, Anne; Sap, Maarten; Levine, Sydney

**Year:** 2026

**Type:** preprint

**Venue:** arXiv preprint

## Links

- **arXiv:** https://arxiv.org/abs/2601.08951

## Abstract

Current AI safety frameworks, which often treat harmfulness as binary, lack the flexibility to handle borderline cases where humans meaningfully disagree. To build more pluralistic systems, it is essential to move beyond consensus and instead understand where and why disagreements arise. We introduce PLURIHARMS, a benchmark designed to systematically study human harm judgments across two key dimensions—the harm axis (benign to harmful) and the agreement axis (agreement to disagreement). Our scalable framework generates prompts that capture diverse AI harms and human values while targeting cases with high disagreement rates, validated by human data. The benchmark includes 150 prompts with 15,000 ratings from 100 human annotators, enriched with demographic and psychological traits and prompt-level features of harmful actions, effects, and values. Our analyses show that prompts that relate to imminent risks and tangible harms amplify perceived harmfulness, while annotator traits (e.g., toxicity experience, education) and their interactions with prompt content explain systematic disagreement. We benchmark AI safety models and alignment methods on PLURIHARMS, finding that while personalization significantly improves prediction of human harm judgments, considerable room remains for future progress. By explicitly targeting value diversity and disagreement, our work provides a principled benchmark for moving beyond “one-size-fits-all” safety toward pluralistically safe AI.

## Dataset Information

150 prompts calibrated across full harmfulness spectrum

## Data Description

PLURIHARMS is a benchmark of 150 prompts calibrated across a harm spectrum, each annotated with 100 human ratings (15,000 total ratings from 100 annotators). The dataset includes comprehensive demographic and psychological traits of annotators, prompt-level features of harmful actions/effects/values, and was curated from 62,612 synthesized prompts using a genetic algorithm. AI safety models including GPT-4.1, Claude, Qwen3, WildGuard, and SafetyAnalyst were evaluated on the benchmark.

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 16, Agent 1
**Implementation Readiness:** MEDIUM

## Tags

