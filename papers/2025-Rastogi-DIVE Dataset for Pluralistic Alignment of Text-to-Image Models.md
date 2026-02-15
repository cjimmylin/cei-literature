---

Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0288
type: preprint
short_title: "DIVE: Dataset for Pluralistic Alignment of Text-to-Image Models"
year: 2025
first_author: "[[Rastogi, Charvi]]"
last_author: "[[Aroyo, Lora]]"
authors: "[[Rastogi, Charvi]]; [[Teh, Tian Huey]]; [[Mishra, Pushkar]]; [[Patel, Roma]]; [[Wang, Ding]]; [[Díaz, Mark]]; [[Parrish, Alicia]]; [[Davani, Aida Mostafazadeh]]; [[Ashwood, Zoe]]; [[Paganini, Michela]]; [[Prabhakaran, Vinodkumar]]; [[Rieser, Verena]]; [[Aroyo, Lora]]"
authors_incomplete: false
url: "https://arxiv.org/abs/2507.13383"
external_pdf: "https://arxiv.org/pdf/2507.13383.pdf"
pdf_extract: "PDF Extracts/2025/2025-Rastogi-DIVE Dataset for Pluralistic Alignment of Text-to-Image Models.md"
local_pdf: "[[PDFs/2025/2025-Rastogi-DIVE Dataset for Pluralistic Alignment of Text-to-Image Models.pdf]]"
publication: arXiv
DATE_ADDED: 20260207
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
national_ethnic_cultural: "N/A"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "Yes"
tags: 
abstract: "Current text-to-image (T2I) models often fail to account for diverse human experiences, leading to misaligned systems. We advocate for pluralistic alignment, where an AI understands and is steerable towards diverse, and often conflicting, human values. Our work provides three core contributions to achieve this in T2I models. First, we introduce a novel dataset for Diverse Intersectional Visual Evaluation (DIVE) – the first multimodal dataset for pluralistic alignment."
ethics_perspective: "AI Safety & Alignment"
data_description: "Evaluation approach dataset"
data_metrics: "1000 prompts"
LLM_assessed: Gemma
DATA_URL: "https://huggingface.co/datasets/neurips-dataset-1211/DIVE"
---
# DIVE: Dataset for Pluralistic Alignment of Text-to-Image Models

## Authors

[[Rastogi, Charvi]], [[Teh, Tian Huey]], [[Mishra, Pushkar]], [[Patel, Roma]], [[Wang, Ding]], [[Díaz, Mark]], [[Parrish, Alicia]], [[Davani, Aida Mostafazadeh]], [[Ashwood, Zoe]], [[Paganini, Michela]], [[Prabhakaran, Vinodkumar]], [[Rieser, Verena]], [[Aroyo, Lora]]

## Metadata

**Authors:** Rastogi, Charvi; Teh, Tian Huey; Mishra, Pushkar; Patel, Roma; Wang, Ding; Díaz, Mark; Parrish, Alicia; Davani, Aida Mostafazadeh; Ashwood, Zoe; Paganini, Michela; Prabhakaran, Vinodkumar; Rieser, Verena; Aroyo, Lora

**Year:** 2025

**Type:** preprint

**Venue:** arXiv

## Links

- **arXiv:** https://arxiv.org/abs/2507.13383

## Abstract

Current text-to-image (T2I) models often fail to account for diverse human experiences, leading to misaligned systems. We advocate for pluralistic alignment, where an AI understands and is steerable towards diverse, and often conflicting, human values. Our work provides three core contributions to achieve this in T2I models. First, we introduce a novel dataset for Diverse Intersectional Visual Evaluation (DIVE) – the first multimodal dataset for pluralistic alignment. It enables deep alignment to diverse safety perspectives through a large pool of demographically intersectional human raters who provided extensive feedback across 1000 prompts, with high replication, capturing nuanced safety perceptions. Second, we empirically confirm demographics as a crucial proxy for diverse viewpoints in this domain, revealing significant, context-dependent differences in harm perception that diverge from conventional evaluations. Finally, we discuss implications for building aligned T2I models, including efficient data collection strategies, LLM judgment capabilities, and model steerability towards diverse perspectives. This research offers foundational tools for more equitable and aligned T2I systems. Content Warning: The paper includes sensitive content that may be harmful.

## Dataset Information

1,000 prompts with safety perspectives from demographically intersectional raters for text-to-image alignment

## Data Description

DIVE is a multimodal dataset for pluralistic alignment in text-to-image safety evaluation, containing 1,000 adversarial prompt-image pairs with 35,164 harm evaluations from 637 demographically diverse raters across 30 intersectional groups (gender, age, ethnicity). Raters provide 5-point Likert scale harmfulness ratings, harm-to-self vs. harm-to-others assessments, violation type labels, and 5,372 free-form text comments.

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 1 (Citation Graph)
**Implementation Readiness:** MEDIUM

## Tags

