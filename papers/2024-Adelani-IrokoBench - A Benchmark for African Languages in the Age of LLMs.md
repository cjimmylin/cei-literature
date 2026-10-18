---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0187
type: conferencePaper
short_title: "IrokoBench -- A Benchmark for African Languages in the Age of LLMs"
year: 2024
first_author: "[[Adelani, David Ifeoluwa]]"
last_author: "[[Stenetorp, Pontus]]"
authors: "Adelani, David Ifeoluwa; Ojo, Jessica; Azime, Israel Abebe; Zhuang, Jian Yun; Jesujoba O. Alabi; He, Xuanli; Ochieng, Millicent; Hooker, Sara; Bukula, Andiswa; Lee, En-Shiun Annie; Chukwuneke, Chiamaka; Buzaaba, Happy; Sibanda, Blessing; Kalipe, Godson; Mukiibi, Jonathan; Kabongo, Salomon; Yuehgoh, Foutse; Setaka, Mmasibidi; Ndolela, Lolwethu; Odu, Nkiruka; Mabuya, Rooweither; Muhammad, Shamsuddeen Hassan; Osei, Salomey; Samb, Sokhar; Guge, Tadesse Kebede; Sherman, Tombekai Vangoni; Stenetorp, Pontus"
authors_incomplete: false
url: "https://arxiv.org/abs/2406.03368"
external_pdf: "https://arxiv.org/pdf/2406.03368.pdf"
pdf_extract: "PDF Extracts/2024/2024-Adelani-IrokoBench - A Benchmark for African Languages in the Age of LLMs.md"
local_pdf: "[[Lit-WS-PDFs/2024/2024-Adelani-IrokoBench - A Benchmark for African Languages in the Age of LLMs.pdf]]"
publication: "ACL 2025"
CONF-CC: "ACL 2025"
DATE_ADDED: 20260207
national_ethnic_cultural: African/Ubuntu
cultures_nationalities_list: African/Ubuntu
languages_list: Multilingual
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
abstract: "Despite the widespread adoption of Large language models (LLMs), their remarkable capabilities remain limited to a few high-resource languages. Additionally, many low-resource languages (e.g., African languages) are often evaluated only on basic text classification tasks due to the lack of appropriate or comprehensive benchmarks outside of highresource languages. In this paper, we introduce IrokoBench—a human-translated benchmark dataset for 17 typologically-diverse lowresource African..."
LLM_assessed: "BLOOM, Claude, Command-R, Gemma-2, GPT-3.5, GPT-4, GPT-4o, GPT-4o mini, Llama-3, Aya, Alpaca, T5"
DATA_URL: NA
CONFERENCE: "ACL 2025"
ethics_overall: 0
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
research_topic: "Machine Learning"
nw_confucian: 0
nw_ubuntu: 0
nw_islamic_ethics: 0
nw_buddhist: 0
nw_dharmic: 0
nw_indigenous_relational: 0
nw_buen_vivir: 0
author_country: IL
author_region: MENA
author_global_north_south: "Global North"
weird_score: 57
is_benchmark: Yes
is_eval: Yes
is_dataset: Yes
data_description: "Benchmark dataset for question answering"
data_metrics: "Not specified"
---
# IrokoBench -- A Benchmark for African Languages in the Age of LLMs

## Authors

[[David Ifeoluwa Adelani|Adelani, David Ifeoluwa]], [[Ojo, Jessica]], [[Azime, Israel Abebe]], [[Zhuang, Jian Yun]], [[Alabi, Jesujoba O]], [[He, Xuanli]], [[Ochieng, Millicent]], [[Hooker, Sara]], [[Bukula, Andiswa]], [[Lee, En-Shiun Annie]], [[Chukwuneke, Chiamaka]], [[Buzaaba, Happy]], [[Sibanda, Blessing]], [[Kalipe, Godson]], [[Mukiibi, Jonathan]], [[Kabongo, Salomon]], [[Yuehgoh, Foutse]], [[Setaka, Mmasibidi]], [[Ndolela, Lolwethu]], [[Odu, Nkiruka]], [[Mabuya, Rooweither]], [[Shamsuddeen Hassan Muhammad|Muhammad, Shamsuddeen Hassan]], [[Salomey Osei|Osei, Salomey]], [[Samb, Sokhar]], [[Guge, Tadesse Kebede]], [[Sherman, Tombekai Vangoni]], [[Stenetorp, Pontus]]

## Metadata

**Authors:** Adelani, David Ifeoluwa; Ojo, Jessica; Azime, Israel Abebe; Zhuang, Jian Yun; Alabi, Jesujoba O.; He, Xuanli; Ochieng, Millicent; Hooker, Sara; Bukula, Andiswa; Lee, En-Shiun Annie; Chukwuneke, Chiamaka; Buzaaba, Happy; Sibanda, Blessing; Kalipe, Godson; Mukiibi, Jonathan; Kabongo, Salomon; Yuehgoh, Foutse; Setaka, Mmasibidi; Ndolela, Lolwethu; Odu, Nkiruka; Mabuya, Rooweither; Muhammad, Shamsuddeen Hassan; Osei, Salomey; Samb, Sokhar; Guge, Tadesse Kebede; Sherman, Tombekai Vangoni; Stenetorp, Pontus

**Year:** 2024

**Type:** conferencePaper

**Venue:** ACL 2025

## Links

- **arXiv:** https://arxiv.org/abs/2406.03368

## Abstract

Despite the widespread adoption of Large language models (LLMs), their remarkable capabilities remain limited to a few high-resource languages. Additionally, many low-resource languages (e.g., African languages) are often evaluated only on basic text classification tasks due to the lack of appropriate or comprehensive benchmarks outside of highresource languages. In this paper, we introduce IrokoBench—a human-translated benchmark dataset for 17 typologically-diverse lowresource African languages covering three tasks: natural language inference (AfriXNLI), mathematical reasoning (AfriMGSM), and multi-choice knowledge-based question answering (AfriMMLU). We use IrokoBench to evaluate zero-shot, few-shot, and translate-test settings (where test sets are translated into English) across 10 open and six proprietary LLMs. Our evaluation reveals a significant performance gap between high-resource languages (such as English and French) and lowresource African languages. We observe a significant performance gap between open and proprietary models, with the highest performing open model, Gemma 2 27B only at 63% of the best-performing proprietary model GPT4o performance. In addition, machine translating the test set to English before evaluation helped to close the gap for larger models that are English-centric, such as Gemma 2 27B and LLaMa 3.1 70B. These findings suggest that more efforts are needed to develop and adapt LLMs for African languages.

## Dataset Information

17 typologically-diverse low-resource African languages

## Data Description

IrokoBench: human-translated benchmark for 17 African languages covering NLI (AfriXNLI), math reasoning (AfriMGSM), and knowledge QA (AfriMMLU).


## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 9-11
**Implementation Readiness:** HIGH

## Tags

