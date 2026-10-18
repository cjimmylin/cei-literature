---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0006
type: preprint
short_title: JMedEthicBench
year: 2026
first_author: "[[Liu, Junyu]]"
last_author: "[[Hatakeyama-Sato, Kan]]"
authors: "Liu, Junyu; Li, Zirui; Niu, Qian; Zhang, Zequn; Xun, Yue; Hou, Wenlong; Wang, Shujun; Iwasawa, Yusuke; Matsuo, Yutaka; Hatakeyama-Sato, Kan"
authors_incomplete: false
url: "https://arxiv.org/abs/2601.01627"
external_pdf: "https://arxiv.org/pdf/2601.01627.pdf"
pdf_extract: "PDF Extracts/2026/2026-Liu-JMedEthicBench.md"
local_pdf: [[Lit-WS-Lit-WS-PDFs/2026/2026-Liu-JMedEthicBench.pdf]]
publication: "arXiv preprint"
CONF-CC: Preprint
DATE_ADDED: 20260207
national_ethnic_cultural: Japanese
cultures_nationalities_list: Japanese
languages_list: "English, Japanese"
religious_values: N/A
rv_islam: 0
rv_christianity: 0
rv_buddhism: 0
rv_judaism: 0
rv_hinduism: 0
rv_sikhism: 0
rv_confucianism: 0
rv_taoism: 0
rv_shinto: 0
rv_jainism: 0
rv_bahai: 0
rv_zoroastrianism: 0
rv_ubuntu: 0
rv_indigenous: 0
religious_values_list: N/A
mp_mft: 0
mp_schwartz: 0
mp_trolley: 0
mp_kohlberg: 0
mp_dual_process: 0
mp_intuitionist: 0
mp_dyadic: 0
mp_identity: 0
moral_psychology: N/A
newtags: 
tags: 
abstract: "As Large Language Models (LLMs) are increasingly deployed in healthcare field, it becomes essential to carefully evaluate their medical safety before clinical use. However, existing safety benchmarks remain predominantly English-centric, and test with only single-turn prompts despite multi-turn clinical consultations. To address these gaps, we introduce JMedEthicBench, the first multi-turn conversational benchmark for evaluating medical safety of LLMs for Japanese healthcare."
LLM_assessed: "Claude, DeepSeek, GPT-4, Gemini, Grok, Llama-3, Qwen"
DATA_URL: NA
normative_ethics_benchmark: Borderline
research_topic: Other
CONFERENCE: Preprint
ethics_overall: 0
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
ethics_perspective: "AI Safety & Alignment"
nw_confucian: 0
nw_ubuntu: 0
nw_islamic_ethics: 0
nw_buddhist: 0
nw_dharmic: 0
nw_indigenous_relational: 0
nw_buen_vivir: 0
author_country: CN
author_region: "East Asia"
author_global_north_south: Ambiguous
weird_score: 36
is_benchmark: Yes
is_eval: Yes
is_dataset: No
data_description: "Benchmark for ai safety"
data_metrics: "Not specified"
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

JMedEthicBench is a multi-turn Japanese medical safety benchmark comprising 54,180 adversarial conversations grounded in 67 Japan Medical Association guidelines, with a test set of 2,345 instances. No public data URL found in the extract.


## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 14
**Implementation Readiness:** HIGH

## Tags

