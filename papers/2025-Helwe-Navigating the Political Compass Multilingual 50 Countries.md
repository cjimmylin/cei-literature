---







Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0094
type: conferencePaper
short_title: "Navigating the Political Compass (Multilingual, 50 Countries)"
year: 2025
first_author: "[[Chadi Helwe]]"
last_author: "[[Davide Ceolin]]"
authors: "Chadi Helwe, Oana Balalau, Davide Ceolin"
publication: "ACL 2025"
external_pdf: "https://arxiv.org/pdf/2506.22493.pdf"
pdf_extract: "PDF Extracts/2025/2025-Helwe-Navigating the Political Compass Multilingual 50 Countries.md"
local_pdf: "[[PDFs/2025/2025-Helwe-Navigating the Political Compass Multilingual 50 Countries.pdf]]"
DATE_ADDED: 20260207
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: ""
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
tags: 
abstract: "The Political Compass Test (PCT) and similar surveys are commonly used to assess political bias in auto-regressive LLMs. Our rigorous statistical experiments show that while changes to standard generation parameters have minimal effect on PCT scores, prompt phrasing and fine-tuning individually and together can significantly influence results. Interestingly, finetuning on politically rich vs. neutral datasets does not lead to different shifts in scores."
research_topic: "Machine Translation"
LLM_assessed: "Llama-3, Mistral, Falcon, Gemma"
DATA_URL: "https://github.com/sadiakamal/Detailed-factor-analysis-PCT"
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "Bias & Fairness"
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Evaluation approach dataset"
data_metrics: "Not specified"
---
# Navigating the Political Compass (Multilingual, 50 Countries)

## Authors

[[Chadi Helwe]], [[Oana Balalau]], [[Davide Ceolin]]

## Metadata

**Authors:** Chadi Helwe, Oana Balalau, Davide Ceolin

**Year:** 2025

**Type:** conferencePaper

**Venue:** ACL 2025

## Links

- **Code/Data:** https://github.com/ChadiHelwe/navigating_the_political_compass

## Abstract

The Political Compass Test (PCT) and similar surveys are commonly used to assess political bias in auto-regressive LLMs. Our rigorous statistical experiments show that while changes to standard generation parameters have minimal effect on PCT scores, prompt phrasing and fine-tuning individually and together can significantly influence results. Interestingly, finetuning on politically rich vs. neutral datasets does not lead to different shifts in scores. We also generalize these findings to a similar popular test called 8 Values. Humans do not change their responses to questions when prompted differently (“answer this question” vs “state your opinion”), or after exposure to politically neutral text, such as mathematical formulae. But the fact that the models do so raises concerns about the validity of these tests for measuring model bias, and paves the way for deeper exploration into how political and social views are encoded in LLMs. The source code is publicly available here1.

## Dataset Information

Political Compass Test administered across 50 most populous countries, their official languages; 15 multilingual LLMs evaluated

## Data Description

This study performs a rigorous statistical factor analysis of the Political Compass Test (PCT) and 8 Values Test applied to LLMs. Four open-source models were tested: Llama3-8B-Instruct, Mistral-7B-Instruct-v0.3, Falcon3-7B-Instruct, and Gemma-3-4b-it, each fine-tuned on eight datasets (politically neutral and politically charged). A total of approximately 2,700 PCT tests were generated, analyzing the effects of decoding parameters, prompt variation, and fine-tuning on political compass scores using ANOVA statistical tests.

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 17
**Implementation Readiness:** HIGH

## Tags

