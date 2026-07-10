---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0819
type: conferencePaper
short_title: "AmericasNLI: Evaluating Zero-shot Natural Language Understanding of Pretrained Multilingual Models in Truly Low-resource Languages"
year: 2025
first_author: "[[Ebrahimi, Abteen]]"
last_author: "[[Kann, Katharina]]"
authors: "Ebrahimi, Abteen; Mager, Manuel; Oncevay, Arturo; Chaudhary, Vishrav; Chiruzzo, Luis; Fan, Angela; Ortega, John; Ramos, Ricardo; Rios, Annette; Meza-Ruiz, Ivan; Gustavo A. Giménez-Lugo; Mager, Elisabeth; Neubig, Graham; Palmer, Alexis; Coto-Solano, Rolando; Vu, Ngoc Thang; Kann, Katharina"
authors_incomplete: false
url: "https://aclanthology.org/2022.acl-long.435/"
external_pdf: "https://arxiv.org/pdf/2104.08726v2.pdf"
publication: "ACL Anthology"
CONF-CC: N/A
pdf_extract: "PDF Extracts/2025/2025-Ebrahimi-AmericasNLI Evaluating Zero-shot Natural Language Understanding of.md"
local_pdf: "[[Lit-WS-Lit-WS-PDFs/2025/2025-Ebrahimi-AmericasNLI Evaluating Zero-shot Natural Language Understanding of.pdf]]"
DATE_ADDED: 20260213
national_ethnic_cultural: "Latin American"
cultures_nationalities_list: "Latin American"
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
LLM_assessed: RoBERTa
DATA_URL: "https://github.com/abteen/americasnli"
tags: 
abstract: "Pretrained multilingual models are able to perform cross-lingual transfer in a zero-shot setting, even for languages unseen during pretraining. However, prior work evaluating performance on unseen languages has largely been limited to low-level, syntactic tasks, and it remains unclear if zero-shot learning of high-level, semantic tasks is possible for unseen languages. To explore this question, we present AmericasNLI, an extension of XNLI (Conneau et al."
CONFERENCE: "ACL 2025"
ethics_overall: No
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
research_topic: "Machine Translation"
nw_confucian: 0
nw_ubuntu: 0
nw_islamic_ethics: 0
nw_buddhist: 0
nw_dharmic: 0
nw_indigenous_relational: 0
nw_buen_vivir: 0
author_country: UY
author_region: "Latin America & Caribbean"
author_global_north_south: "Global South"
weird_score: 42
is_benchmark: No
is_eval: Yes
is_dataset: Yes
data_description: "Evaluation methodology dataset"
data_metrics: "10 languages"
---
# AmericasNLI: Evaluating Zero-shot Natural Language Understanding of Pretrained Multilingual Models in Truly Low-resource Languages

## Authors

[[Ebrahimi, Abteen]], [[Mager, Manuel]], [[Oncevay, Arturo]], [[Vishrav Chaudhary|Chaudhary, Vishrav]], [[Chiruzzo, Luis]], [[Angela Fan|Fan, Angela]], [[Ortega, John]], [[Ricardo Ramos|Ramos, Ricardo]], [[Annette Rios|Rios, Annette]], [[Meza-Ruiz, Ivan]], [[Giménez-Lugo, Gustavo A]], [[Elisabeth Mager|Mager, Elisabeth]], [[Graham Neubig|Neubig, Graham]], [[Alexis Palmer|Palmer, Alexis]], [[Coto-Solano, Rolando]], [[Ngoc Thang Vu|Vu, Ngoc Thang]], [[Kann, Katharina]]

## Metadata

**Authors:** Abteen Ebrahimi; Manuel Mager; Arturo Oncevay; Vishrav Chaudhary; Luis Chiruzzo; Angela Fan; John Ortega; Ricardo Ramos; Annette Rios; Ivan Meza-Ruiz; Gustavo A. Giménez-Lugo; Elisabeth Mager; Graham Neubig; Alexis Palmer; Rolando Coto-Solano; Ngoc Thang Vu; Katharina Kann

**Year:** 2025

**Type:** conferencePaper

**Venue:** ACL Anthology

**Languages:** Guarani, Multilingual, Quechua

**Benchmark:** AmericasNLI

## Links

- **URL:** https://aclanthology.org/2022.acl-long.435/

## Abstract


Pretrained multilingual models are able to perform cross-lingual transfer in a zero-shot setting, even for languages unseen during pretraining. However, prior work evaluating performance on unseen languages has largely been limited to low-level, syntactic tasks, and it remains unclear if zero-shot learning of high-level, semantic tasks is possible for unseen languages. To explore this question, we present AmericasNLI, an extension of XNLI (Conneau et al., 2018) to 10 Indigenous languages of the Americas. We conduct experiments with XLM-R, testing multiple zero-shot and translation-based approaches. Additionally, we explore model adaptation via continued pretraining and provide an analysis of the dataset by considering hypothesis-only models. We ﬁnd that XLM-R’s zero-shot performance is poor for all 10 languages, with an average performance of 38.48%. Continued pretraining offers improvements, with an average accuracy of 43.85%. Surprisingly, training on poorly translated data by far outperforms all other methods with an accuracy of 49.12%.

## Data Description

AmericasNLI extends XNLI to 10 Indigenous languages of the Americas (Asháninka, Aymara, Bribri, Guaraní, Nahuatl, Otomí, Quechua, Rarámuri, Shipibo-Konibo, Wixarika), providing dev and test NLI sets; intended as a benchmark for zero-shot multilingual evaluation.


## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent D2
**Relevance:** AmericasNLI benchmark for Multilingual, Quechua, Guarani

## Tags

