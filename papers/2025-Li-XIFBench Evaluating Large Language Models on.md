---
































Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0754
type: conferencePaper
short_title: "XIFBench: Evaluating Large Language Models on"
year: 2025
first_author: "[[Li, Zhenyu]]"
last_author: "[[Zhang, Min]]"
authors: "Li, Zhenyu; Chen, Kehai; Long, Yunfei; Bai, Xuefeng; Zhang, Yaoyin; Wei, Xuchen; Li, Juntao; Zhang, Min"
authors_incomplete: false
url: "https://openreview.net/pdf/da14c5ecc0ecf18bfb2f9ccbd84f45422a3077fb.pdf"
external_pdf: "https://arxiv.org/pdf/2503.07539v2.pdf"
publication: OpenReview
CONF-CC: "Preprint"
pdf_extract: "PDF Extracts/2025/2025-Li-XIFBench Evaluating Large Language Models on.md"
local_pdf: "[[PDFs/2025/2025-Li-XIFBench Evaluating Large Language Models on.pdf]]"
DATE_ADDED: 20260213
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: "Multilingual"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
LLM_assessed: "ChatGLM, Claude-3, GPT-4o, Gemini, Llama-3, Qwen-2"
DATA_URL: "https://github.com/zhenyyli801/XIFBench"
tags: 
abstract: "Large Language Models (LLMs) have demonstrated remarkable instructionfollowing capabilities across various applications. However, their performance in multilingual settings lacks systematic investigation, with existing evaluations lacking fine-grained constraint analysis across diverse linguistic contexts. We introduce XIFBench, a comprehensive constraint-based benchmark for evaluating multilingual instruction-following abilities of LLMs, comprising 558 instructions with 0-5 additional..."
CONFERENCE: "Other Conference"
ethics_overall: "No"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
research_topic: "Machine Translation"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Multilingual benchmark dataset"
data_metrics: "Not specified"
---
# XIFBench: Evaluating Large Language Models on

## Authors

[[Li, Zhenyu]], [[Chen, Kehai]], [[Long, Yunfei]], [[Bai, Xuefeng]], [[Zhang, Yaoyin]], [[Wei, Xuchen]], [[Li, Juntao]], [[Zhang, Min]]

## Metadata

**Authors:** Zhenyu Li; Kehai Chen; Yunfei Long; Xuefeng Bai; Yaoyin Zhang; Xuchen Wei; Juntao Li; Min Zhang

**Year:** 2025

**Type:** conferencePaper

**Venue:** OpenReview

**Languages:** Multilingual

**Benchmark:** XIFBench

## Links

- **URL:** https://openreview.net/pdf/da14c5ecc0ecf18bfb2f9ccbd84f45422a3077fb.pdf

## Abstract


Large Language Models (LLMs) have demonstrated remarkable instructionfollowing capabilities across various applications. However, their performance in multilingual settings lacks systematic investigation, with existing evaluations lacking fine-grained constraint analysis across diverse linguistic contexts. We introduce XIFBench, a comprehensive constraint-based benchmark for evaluating multilingual instruction-following abilities of LLMs, comprising 558 instructions with 0-5 additional constraints across five categories (Content, Style, Situation, Format, and Numerical) in six languages spanning different resource levels. To support reliable and consistent cross-lingual evaluation, we implement three methodological innovations: cultural accessibility annotation, constraint-level translation validation, and requirement-based evaluation using English requirements as semantic anchors across languages. Extensive experiments with various LLMs not only quantify performance disparities across resource levels but also provide detailed insights into how language resources, constraint categories, instruction complexity, and cultural specificity influence multilingual instruction-following. Our code and data are available at https://github.com/zhenyuli801/XIFBench.

## Data Description

XIFBench: 558 multilingual instructions (Easy + Hard sets) augmented with 0-5 constraints across 5 categories and 21 dimensions, translated into 6 languages (English, Chinese, Russian, Arabic, Hindi, Swahili), yielding 3,348 evaluation instances with structured binary-question evaluation requirements.


## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent D1
**Relevance:** XIFBench benchmark for Multilingual

## Tags

