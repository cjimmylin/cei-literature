---



Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0275
type: preprint
short_title: "Fair-PP: Synthetic Dataset for Aligning LLM with Personalized Preferences of Social Equity"
year: 2025
first_author: "[[Zhou, Qi]]"
last_author: "[[Guo, Qing]]"
authors: "[[Zhou, Qi]]; [[Zhang, Jie]]; [[Wang, Dongxia]]; [[Liu, Qiang]]; [[Li, Tianlin]]; [[Dong, Jin Song]]; [[Wang, Wenhai]]; [[Guo, Qing]]"
authors_incomplete: false
url: "https://arxiv.org/abs/2505.11861"
external_pdf: "https://arxiv.org/pdf/2505.11861.pdf"
pdf_extract: "PDF Extracts/2025/2025-Zhou-Fair-PP Synthetic Dataset for Aligning LLM with Personalized.md"
local_pdf: "[[PDFs/2025/2025-Zhou-Fair-PP Synthetic Dataset for Aligning LLM with Personalized.pdf]]"
publication: arXiv
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
is_eval: "No"
is_dataset: "Yes"
tags: 
abstract: "Human preference plays a crucial role in the refinement of large language models (LLMs). However, collecting human preference feedback is costly and most existing datasets neglect the correlation between personalization and preferences. To address this issue, we introduce FAIR-PP, a synthetic dataset of personalized preferences targeting social equity, derived from real-world social survey data, which includes 28 social groups, 98 equity topics, and 5 personal preference dimensions."
ethics_perspective: "Bias & Fairness"
data_description: "Dataset"
data_metrics: "Not specified"
LLM_assessed: "Falcon, Llama-3, Mistral, Qwen"
DATA_URL: "https://github.com/tools-only/FairPP, https://huggingface.co/datasets/tools-o/Fair-PP"
---
# Fair-PP: Synthetic Dataset for Aligning LLM with Personalized Preferences of Social Equity

## Authors

[[Zhou, Qi]], [[Jie Zhang|Zhang, Jie]], [[Wang, Dongxia]], [[Liu, Qiang]], [[Li, Tianlin]], [[Dawn Song|Dong, Jin Song]], [[Wang, Wenhai]], [[Guo, Qing]]

## Metadata

**Authors:** Zhou, Qi; Zhang, Jie; Wang, Dongxia; Liu, Qiang; Li, Tianlin; Dong, Jin Song; Wang, Wenhai; Guo, Qing

**Year:** 2025

**Type:** preprint

**Venue:** arXiv

## Links

- **arXiv:** https://arxiv.org/abs/2505.11861

## Abstract

Human preference plays a crucial role in the refinement of large language models (LLMs). However, collecting human preference feedback is costly and most existing datasets neglect the correlation between personalization and preferences. To address this issue, we introduce FAIR-PP, a synthetic dataset of personalized preferences targeting social equity, derived from real-world social survey data, which includes 28 social groups, 98 equity topics, and 5 personal preference dimensions. Leveraging GPT-4o-mini, we engage in role-playing based on seven representative persona portrayals guided by existing social survey data, yielding a total of 238,623 preference records. Through FAIR-PP, we also contribute (i) An automated framework for generating preference data, along with a more fine-grained dataset of personalized preferences; (ii) analysis of the positioning of the existing mainstream LLMs across five major global regions within the personalized preference space; and (iii) a sample reweighting method for personalized preference alignment, enabling alignment with a target persona while maximizing the divergence from other personas. Empirical experiments show our method outperforms the baselines. Code: github.com/tools-only/FairPP Dataset: huggingface.co/datasets/tools-o/Fair-PP

## Dataset Information

238,623 preference records across 28 social groups and 98 equity topics

## Data Description

FAIR-PP is a synthetic dataset of personalized preferences targeting social equity, derived from real-world social survey data. It contains 34,089 survey questions and 238,623 personalized preference records covering 28 social groups, 98 equity topics, and 5 personal preference dimensions across 7 representative persona portrayals. The dataset was generated using GPT-4o-mini for LLM personalization based on value-based segments from the UK public as defined in the 'More in Common' and YouGov's 2020 Britain's Choice report.

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 1 (Citation Graph)
**Implementation Readiness:** HIGH

## Tags

