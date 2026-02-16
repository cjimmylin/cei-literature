---



Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0160
type: conferencePaper
short_title: "Does Cross-Cultural Alignment Change the Commonsense Morality of Language Models?"
year: 2025
first_author: "[[Y Jinnai]]"
last_author: "[[Y]]"
authors: "Jinnai, Y"
publication: "ACL 2024"
external_pdf: "https://arxiv.org/pdf/2406.16316v1.pdf"
pdf_extract: "PDF Extracts/2024/2024-Jinnai-Does Cross-Cultural Alignment Change the Commonsense Morality of.md"
local_pdf: "[[PDFs/2024/2024-Jinnai-Does Cross-Cultural Alignment Change the Commonsense Morality of.pdf]]"
DATE_ADDED: 20260207
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
national_ethnic_cultural: "Japanese, Multicultural/Cross-cultural"
cultures_nationalities_list: "Japanese, Cross-cultural"
languages_list: "English, Japanese"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "Yes"
tags: 
abstract: "Alignment of the language model with human preferences is a common approach to making a language model useful to end users. However, most alignment work is done in English, and human preference datasets are dominated by English, reflecting only the preferences of Englishspeaking annotators. Nevertheless, it is common practice to use the English preference data, either directly or by translating it into the target language, when aligning a multilingual language model."
ethics_perspective: "AI Safety & Alignment"
data_description: "Evaluation approach dataset"
data_metrics: "Not specified"
LLM_assessed: "GPT-3.5, GPT-4, Llama-2"
DATA_URL: "https://huggingface.co/datasets/cyberagent/chatbot-arena-ja-calm2-7b-chat-experimental"
---
# Does Cross-Cultural Alignment Change the Commonsense Morality of Language Models?

## Authors

[[Jinnai]], [[Y]]

## Metadata

**Authors:** Jinnai, Y

**Year:** 2024

**Type:** conferencePaper

**Venue:** ACL 2024

## Links


## Abstract

Alignment of the language model with human preferences is a common approach to making a language model useful to end users. However, most alignment work is done in English, and human preference datasets are dominated by English, reflecting only the preferences of Englishspeaking annotators. Nevertheless, it is common practice to use the English preference data, either directly or by translating it into the target language, when aligning a multilingual language model. The question is whether such an alignment strategy marginalizes the preference of non-English speaking users. To this end, we investigate the effect of aligning Japanese language models with (mostly) English resources. In particular, we focus on evaluating whether the commonsense morality of the resulting finetuned models is aligned with Japanese culture using the JCommonsenseMorality (JCM) and ETHICS datasets. The experimental results show that the fine-tuned model outperforms the SFT model. However, it does not demonstrate the same level of improvement as a model finetuned using the JCM, suggesting that while some aspects of commonsense morality are transferable, others may not be.

## Dataset Information

Datasets used: JCommonsenseMorality (Japanese), ETHICS (English)

## Data Description

This study uses two commonsense morality datasets: the JCommonsenseMorality (JCM) dataset, which contains short sentences about moral judgments collected from Japanese-speaking crowd workers, and the commonsense morality subset of the ETHICS dataset collected from English speakers in the US, Canada, and Great Britain. Both datasets were cross-translated (JCM to English and ETHICS to Japanese) to isolate cultural versus linguistic effects when fine-tuning three Japanese LLMs (CALM2-7B, llm-jp-13B, Swallow-7B) using DPO alignment.

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 12-13
**Implementation Readiness:** MEDIUM

## Tags

