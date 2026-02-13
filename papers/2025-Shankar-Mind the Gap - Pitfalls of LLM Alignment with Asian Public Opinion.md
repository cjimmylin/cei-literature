---



Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0089
type: conferencePaper
short_title: Mind the Gap -- Pitfalls of LLM Alignment with Asian Public Opinion
year: 2025
first_author: "[[H. Shankar]]"
last_author: "[[D]]"
authors: "Shankar, H., S P, V., Margapuri, S., & Mazumder, D"
url: "https://precog.iiit.ac.in/pubs/mind_the_gap_LLM_Alignment_Steerability_Global_South.pdf"
external_pdf: "https://cdn.iiit.ac.in/cdn/precog.iiit.ac.in/pubs/mind_the_gap_LLM_Alignment_Steerability_Global_South.pdf"
local_pdf: "[[PDFs/2025/2025-Shankar-Mind the Gap - Pitfalls of LLM Alignment with Asian Public Opinion.pdf]]"
pdf_extract: "[[PDF Extracts/2025-Shankar-Mind the Gap - Pitfalls of LLM Alignment with Asian Public Opinion.md]]"
publication: "Proceedings of the National Academy of Sciences (PNAS)"
DATE_ADDED: 20260207
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
national_ethnic_cultural: "Asian (India, East Asia, Southeast Asia)"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "Yes"
tags: 
abstract: "Large Language Models (LLMs) are increasingly deployed in multilingual, multicultural settings, yet their reliance on predominantly English-centric training data risks misalignment with the diverse cultural values of different societies. In this paper, we present a comprehensive, multilingual audit of alignment of contemporary LLMs including GPT-4o-Mini, Gemini-2.5-Flash, Llama 3.2, Mistral and Gemma 3 across India, East Asia and Southeast Asia. Our study specifically focuses on the sensitive domain of religion as the prism for broader cultural alignment. To facilitate this, we conduct a multi-faceted analysis of every LLM's internal representations, using log-probs/logits, to compare the model's opinion distributions against ground-truth public attitudes. We find that while the popular models generally align with public opinion on broad social issues, they consistently fail to accurately represent religious viewpoints, especially those of minority groups, often amplifying negative stereotypes. Lightweight interventions, such as demographic priming and native language prompting, partially mitigate but do not eliminate these cultural gaps. We further show that downstream evaluations on bias benchmarks (such as CrowS-Pairs, IndiBias, ThaiCLI, KoBBQ) reveal persistent harms and under-representation in sensitive contexts. Our findings underscore the urgent need for systematic, regionally grounded audits to ensure equitable global deployment of LLMs."
ethics_perspective: "AI Safety & Alignment"
data_description: "Evaluation framework dataset for question answering"
data_metrics: "Not specified"
LLM_assessed: "GPT-4, Gemini, Llama-3, Mistral, Gemma"
DATA_URL: "https://github.com/HariShankar08/LLMOpinions/"
---
# Mind the Gap -- Pitfalls of LLM Alignment with Asian Public Opinion

## Authors

[[Shankar]], [[H.]], [[S P]], [[V.]], [[Margapuri]], [[S.]], [[& Mazumder]], [[D]]

## Metadata

**Authors:** Shankar, H., S P, V., Margapuri, S., & Mazumder, D

**Year:** 2025

**Type:** conferencePaper

**Venue:** Proceedings of the National Academy of Sciences (PNAS)

## Links

- **DOI:** https://www.pnas.org/doi/10.1073/pnas.2412015122
- **PDF:** https://cdn.iiit.ac.in/cdn/precog.iiit.ac.in/pubs/mind_the_gap_LLM_Alignment_Steerability_Global_South.pdf

## Abstract

Large Language Models (LLMs) are increasingly deployed in multilingual, multicultural settings, yet their reliance on predominantly English-centric training data risks misalignment with the diverse cultural values of different societies. In this paper, we present a comprehensive, multilingual audit of alignment of contemporary LLMs including GPT-4o-Mini, Gemini-2.5-Flash, Llama 3.2, Mistral and Gemma 3 across India, East Asia and Southeast Asia. Our study specifically focuses on the sensitive domain of religion as the prism for broader cultural alignment. To facilitate this, we conduct a multi-faceted analysis of every LLM's internal representations, using log-probs/logits, to compare the model's opinion distributions against ground-truth public attitudes. We find that while the popular models generally align with public opinion on broad social issues, they consistently fail to accurately represent religious viewpoints, especially those of minority groups, often amplifying negative stereotypes. Lightweight interventions, such as demographic priming and native language prompting, partially mitigate but do not eliminate these cultural gaps. We further show that downstream evaluations on bias benchmarks (such as CrowS-Pairs, IndiBias, ThaiCLI, KoBBQ) reveal persistent harms and under-representation in sensitive contexts. Our findings underscore the urgent need for systematic, regionally grounded audits to ensure equitable global deployment of LLMs.

## Data Description

The study audits LLM cultural alignment across 12 Asian countries using nationally representative Pew Research Center survey data on religious and social attitudes. Five LLMs (GPT-4o-Mini, Gemini-2.5-Flash, Llama 3.2, Mistral, and Gemma 3) are evaluated in both English and local languages across India, East Asia, and Southeast Asia. The evaluation also uses four bias benchmarks (CrowS-Pairs, IndiBias, ThaiCLI, KoBBQ) for downstream assessment of representational harms.


## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 12-13
**Implementation Readiness:** MEDIUM

## Tags

