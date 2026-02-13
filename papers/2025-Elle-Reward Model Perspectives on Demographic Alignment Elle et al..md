---



Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0294
type: preprint
short_title: Reward Model Perspectives on Demographic Alignment (Elle et al.)
year: 2025
first_author: "[[Yang, Elle Michelle]]"
last_author: "[[Yang, Elle Michelle]]"
authors: "[[Yang, Elle Michelle]]"
authors_incomplete: false
url: "https://arxiv.org/abs/2510.06391"
external_pdf: "https://arxiv.org/pdf/2510.06391.pdf"
local_pdf: "[[PDFs/2025/2025-Elle-Reward Model Perspectives on Demographic Alignment Elle et al..pdf]]"
pdf_extract: "PDF Extracts/2025/2025-Elle-Reward Model Perspectives on Demographic Alignment Elle et al..md"
publication: arXiv
DATE_ADDED: 20260207
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
national_ethnic_cultural: "American"
religious_values: "Christianity"
religious_values_list: "Christianity"
moral_psychology: "N/A"
newtags: 
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "No"
tags: 
abstract: "Reward models (RMs) are central to the alignment of language models (LMs). An RM often serves as a proxy for human preferences to guide downstream LM behavior. However, our understanding of RM behavior is limited. Our work (i) formalizes a framework for measuring the alignment of opinions captured by RMs, (ii) investigates the extent to which RMs demonstrate sociodemographic biases, and (iii) explores the effects of prompting to steer rewards towards the preferences of a target group."
ethics_perspective: "AI Safety & Alignment"
data_description: "Evaluation framework"
data_metrics: "Not specified"
LLM_assessed: "DeBERTa"
DATA_URL: "https://github.com/socialnlp/rmp"
---
# Reward Model Perspectives on Demographic Alignment (Elle et al.)

## Authors

[[S. Elle]]

## Metadata

**Authors:** Elle, S. et al.

**Year:** 2025

**Type:** preprint

**Venue:** arXiv

## Links

- **arXiv:** https://arxiv.org/abs/2510.06391

## Abstract

Reward models (RMs) are central to the alignment of language models (LMs). An RM often serves as a proxy for human preferences to guide downstream LM behavior. However, our understanding of RM behavior is limited. Our work (i) formalizes a framework for measuring the alignment of opinions captured by RMs, (ii) investigates the extent to which RMs demonstrate sociodemographic biases, and (iii) explores the effects of prompting to steer rewards towards the preferences of a target group. We study the subjective and diverse perspectives on controversial topics, which allows us to quantify RM perspectives in terms of their opinions, attitudes, and values. We show that RMs are poorly aligned with several demographic groups and can systematically reward harmful stereotypes, and steering alone is not enough to overcome these limitations. Our findings underscore the need for more careful consideration of RM behavior in model alignment during preference learning to prevent the propagation of unwanted social biases in the language technologies that we use. Code: github.com/socialnlp/rmp

## Dataset Information

Framework for demographic alignment of reward models

## Data Description

The study evaluates seven open-source reward models (Beaver RM, LLM-Blender RM, Starling RM, Ultra RM, and OpenAssistant's DeBERTa RM, Pythia1B RM, Pythia7B RM) for sociodemographic biases using four datasets with demographic labels: BBQ, OpinionQA, PRISM, and StereoSet. The authors formalize a framework for measuring alignment of reward model opinions across demographic groups, finding that reward models can systematically reward harmful stereotypes and are poorly aligned with several demographic groups.

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 1 (Citation Graph)
**Implementation Readiness:** LOW

## Tags

