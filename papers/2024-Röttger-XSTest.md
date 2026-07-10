---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: 8X95VAH8
type: document
short_title: XSTest
year: 2025
first_author: "[[Paul Röttger]]"
last_author: "[[Hovy, Dirk]]"
authors: "Röttger, Paul; Kirk, Hannah; Vidgen, Bertie; Attanasio, Giuseppe; Bianchi, Federico; Hovy, Dirk"
url: "https://aclanthology.org/2024.naacl-long.301/"
external_pdf: "file:///Users/jimmylin/Zotero/storage/W25TJPES/2024 - XSTest A Test Suite for Identifying Exaggerated Safety Behaviours in Large Language Models.pdf"
national_ethnic_cultural: N/A
cultures_nationalities_list: N/A
languages_list: English
religious_values: N/A
rv_islam: 0
rv_christianity: 0
rv_buddhism: 0
rv_judaism: 5
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
newtags: "AI Safety & Alignment"
key_contribution: "Introduced XSTest, a test suite designed to identify 'exaggerated safety behaviors' (over-refusals) where models incorrectly refuse safe prompts (e.g., historical facts) due to safety filters."
significance: "Highlights the 'safety-helpfulness trade-off', showing that current alignment methods often result in models that are too cautious, reducing their utility for legitimate user queries."
tags: 
abstract: "Without proper safeguards, large language models will readily follow malicious instructions and generate toxic content. This risk motivates safety efforts such as red-teaming and large-scale feedback learning, which aim to make models both helpful and harmless. However, there is a tension between these two objectives, since harmlessness requires models to refuse to comply with unsafe prompts, and thus not be helpful."
CONF-CC: N/A
DATE_ADDED: 20260208
LLM_assessed: "GPT-4, Llama-2, Mistral"
DATA_URL: "https://github.com/paul-rottger/exaggerated-safety"
pdf_extract: "PDF Extracts/2024/2024-Röttger-XSTest.md"
local_pdf: [[Lit-WS-Lit-WS-PDFs/2024/2024-Röttger-XSTest.pdf]]
CONFERENCE: "NAACL 2024"
helm: incorporated
ethics_overall: No
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
author_country: US
author_region: "North America"
author_global_north_south: "Global North"
weird_score: 78
is_benchmark: Yes
is_eval: No
is_dataset: No
data_description: "Benchmark for ai safety"
data_metrics: "Not specified"
---
# XSTest: A Test Suite for Identifying Exaggerated Safety Behaviours in Large Language Models

## Authors

[[Röttger, Paul]], [[Hannah Kirk|Kirk, Hannah]], [[Bertie Vidgen|Vidgen, Bertie]], [[Giuseppe Attanasio|Attanasio, Giuseppe]], [[Federico Bianchi|Bianchi, Federico]], [[Dirk Hovy|Hovy, Dirk]]

## Links

- **ACL Anthology:** https://aclanthology.org/2024.naacl-long.301/

## Abstract

Without proper safeguards, large language models will readily follow malicious instructions and generate toxic content. This risk motivates safety efforts such as red-teaming and large-scale feedback learning, which aim to make models both helpful and harmless. However, there is a tension between these two objectives, since harmlessness requires models to refuse to comply with unsafe prompts, and thus not be helpful. Recent anecdotal evidence suggests that some models may have struck a poor balance, so that even clearly safe prompts are refused if they use similar language to unsafe prompts or mention sensitive topics. In this paper, we introduce a new test suite called XSTest to identify such eXaggerated Safety behaviours in a systematic way. XSTest comprises 250 safe prompts across ten prompt types that well-calibrated models should not refuse to comply with, and 200 unsafe prompts as contrasts that models, for most applications, should refuse. We describe XSTest’s creation and composition, and then use the test suite to highlight systematic failure modes in state-of-the-art language models as well as more general challenges in building safer language models.

## Data Description

XSTEST is a hand-crafted test suite of 250 safe prompts across 10 prompt types plus 200 unsafe contrast prompts, designed to identify exaggerated safety behaviours in LLMs.


## Notes

