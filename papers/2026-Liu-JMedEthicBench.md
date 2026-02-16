---




Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0006
type: preprint
short_title: JMedEthicBench
year: 2025
first_author: "[[Liu, Junyu]]"
last_author: "[[Hatakeyama-Sato, Kan]]"
authors: "[[Liu, Junyu]]; [[Li, Zirui]]; [[Niu, Qian]]; [[Zhang, Zequn]]; [[Xun, Yue]]; [[Hou, Wenlong]]; [[Wang, Shujun]]; [[Iwasawa, Yusuke]]; [[Matsuo, Yutaka]]; [[Hatakeyama-Sato, Kan]]"
authors_incomplete: false
url: "https://arxiv.org/abs/2601.01627"
external_pdf: "https://arxiv.org/pdf/2601.01627.pdf"
pdf_extract: "PDF Extracts/0000/2026-Liu-JMedEthicBench.md"
local_pdf: "[[PDFs/2026/2026-Liu-JMedEthicBench.pdf]]"
publication: "arXiv preprint"
DATE_ADDED: 20260207
ethics_overall: "No"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "Japanese"
languages_list: "English, Japanese"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
is_benchmark: "No"
is_eval: "No"
is_dataset: "No"
tags: 
abstract: "As Large Language Models (LLMs) are increasingly deployed in healthcare field, it becomes essential to carefully evaluate their medical safety before clinical use. However, existing safety benchmarks remain predominantly English-centric, and test with only single-turn prompts despite multi-turn clinical consultations. To address these gaps, we introduce JMedEthicBench, the first multi-turn conversational benchmark for evaluating medical safety of LLMs for Japanese healthcare."
ethics_perspective: "AI Safety & Alignment"
data_description: "N/A"
data_metrics: "Not specified"
LLM_assessed: "GPT-4, Claude, DeepSeek, Qwen, Llama-3, Grok"
DATA_URL: "NA"
normative_ethics_benchmark: Borderline
research_topic: "Other"
---
# JMedEthicBench

## Authors

[[Liu, Junyu]], [[Li, Zirui]], [[Niu, Qian]], [[Zhang, Zequn]], [[Xun, Yue]], [[Hou, Wenlong]], [[Wang, Shujun]], [[Iwasawa, Yusuke]], [[Matsuo, Yutaka]], [[Hatakeyama-Sato, Kan]]

## Metadata

**Authors:** Liu, Junyu; Li, Zirui; Niu, Qian; Zhang, Zequn; Xun, Yue; Hou, Wenlong; Wang, Shujun; Iwasawa, Yusuke; Matsuo, Yutaka; Hatakeyama-Sato, Kan

**Year:** 2026

**Type:** preprint

**Venue:** arXiv preprint

## Links

- **arXiv:** https://arxiv.org/abs/2601.01627

## Abstract

As Large Language Models (LLMs) are increasingly deployed in healthcare field, it becomes essential to carefully evaluate their medical safety before clinical use. However, existing safety benchmarks remain predominantly English-centric, and test with only single-turn prompts despite multi-turn clinical consultations. To address these gaps, we introduce JMedEthicBench, the first multi-turn conversational benchmark for evaluating medical safety of LLMs for Japanese healthcare. Our benchmark is based on 67 guidelines from the Japan Medical Association and contains over 50,000 adversarial conversations generated using seven automatically discovered jailbreak strategies. Using a dual-LLM scoring protocol, we evaluate 27 models and find that commercial models maintain robust safety while medical-specialized models exhibit increased vulnerability. Furthermore, safety scores decline significantly across conversation turns (median: 9.5 to 5.0, p < 0.001). Cross-lingual evaluation on both Japanese and English versions of our benchmark reveals that medical model vulnerabilities persist across languages, indicating inherent alignment limitations rather than language-specific factors. These findings suggest that domain-specific fine-tuning may accidentally weaken safety mechanisms and that multi-turn interactions represent a distinct threat surface requiring dedicated alignment strategies.

## Dataset Information

50,000+ adversarial conversations

## Data Description

JMedEthicBench is the first multi-turn conversational benchmark for evaluating medical safety of LLMs in Japanese healthcare, comprising over 50,000 adversarial conversations generated from 1,935 validated harmful questions using seven jailbreak strategies. The benchmark is grounded in 67 guidelines from the Japan Medical Association (JMA). A total of 27 models were evaluated across three categories (commercial, general open-source, and medical-specialized), with a test set of 2,345 instances.

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 14
**Implementation Readiness:** HIGH

## Tags

