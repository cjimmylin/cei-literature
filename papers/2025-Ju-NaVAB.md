---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: JDUIJ4P2
type: document
short_title: NaVAB
year: 2025
first_author: "[[Chengyi Ju]]"
last_author: "[[Guo, Yike]]"
authors: "Ju, Chengyi; Shi, Weijie; Liu, Chengzhong; Ji, Jiaming; Zhang, Jipeng; Zhang, Ruiyuan; Xu, Jiajie; Yang, Yaodong; Han, Sirui; Guo, Yike"
url: "https://aclanthology.org/2025.findings-acl.1028/"
external_pdf: "file:///Users/jimmylin/Zotero/storage/5RMIU8JW/2025 - NaVAB Benchmarking Multi-National Value Alignment for Large Language Models.pdf"
national_ethnic_cultural: "Chinese, French, German, American"
cultures_nationalities_list: "Chinese, French, German, American"
languages_list: "Chinese, English, French, German"
religious_values: Jainism
rv_islam: 0
rv_christianity: 0
rv_buddhism: 0
rv_judaism: 0
rv_hinduism: 0
rv_sikhism: 0
rv_confucianism: 0
rv_taoism: 0
rv_shinto: 0
rv_jainism: 50
rv_bahai: 0
rv_zoroastrianism: 0
rv_ubuntu: 0
rv_indigenous: 0
religious_values_list: Jainism
mp_mft: 0
mp_schwartz: 0
mp_trolley: 0
mp_kohlberg: 0
mp_dual_process: 0
mp_intuitionist: 0
mp_dyadic: 0
mp_identity: 0
moral_psychology: N/A
newtags: "Chinese, French, German, American, AI Safety & Alignment"
key_contribution: "Introduced NaVAB, a benchmark for multi-national value alignment across 5 nations (CN, US, UK, FR, DE), extracting values from policy/legal documents."
significance: "Moves beyond 'Western vs non-Western' to fine-grained national distinctions (e.g., French vs German values), providing a scalable pipeline for national value alignment."
tags: 
abstract: "Do Large Language Models (LLMs) hold positions that conflict with your country’s values? Occasionally they do! However, existing works primarily focus on ethical reviews, failing to capture the diversity of national values, which encompass broader policy, legal, and moral considerations. Furthermore, current benchmarks that rely on spectrum tests using manually designed questionnaires are not easily scalable."
CONF-CC: N/A
DATE_ADDED: 20260208
LLM_assessed: "Claude-3 Sonnet, DeepSeek, GPT-4, Llama-3, Mixtral, Qwen"
DATA_URL: "https://huggingface.co/datasets/JadenGGGeee/NaVAB"
pdf_extract: "PDF Extracts/2025/2025-Ju-NaVAB.md"
local_pdf: "[[Lit-WS-PDFs/2025/2025-Ju-NaVAB.pdf]]"
CONFERENCE: "ACL 2025"
ethics_overall: 60
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
ethics_perspective: "General Ethics"
nw_confucian: 0
nw_ubuntu: 0
nw_islamic_ethics: 0
nw_buddhist: 0
nw_dharmic: 0
nw_indigenous_relational: 0
nw_buen_vivir: 0
author_country: HK
author_region: "East Asia"
author_global_north_south: Ambiguous
weird_score: 53
is_benchmark: Yes
is_eval: Yes
is_dataset: Yes
data_description: "Benchmark for moral/ethical reasoning dataset"
data_metrics: "Not specified"
---
# NaVAB: Benchmarking Multi-National Value Alignment for Large Language Models

## Authors

[[Chengyi Ju|Ju, Chengyi]], [[Weijie Shi|Shi, Weijie]], [[Chengzhong Liu|Liu, Chengzhong]], [[Jiaming Ji|Ji, Jiaming]], [[Jipeng Zhang|Zhang, Jipeng]], [[Ruiyuan Zhang|Zhang, Ruiyuan]], [[Jiajie Xu|Xu, Jiajie]], [[Yaodong Yang|Yang, Yaodong]], [[Sirui Han|Han, Sirui]], [[Yike Guo|Guo, Yike]]

## Links

- **ACL Anthology:** https://aclanthology.org/2025.findings-acl.1028/

## Abstract

Do Large Language Models (LLMs) hold positions that conflict with your country’s values? Occasionally they do! However, existing works primarily focus on ethical reviews, failing to capture the diversity of national values, which encompass broader policy, legal, and moral considerations. Furthermore, current benchmarks that rely on spectrum tests using manually designed questionnaires are not easily scalable. To address these limitations, we introduce NaVAB, a comprehensive benchmark to evaluate the alignment of LLMs with the values of five major nations: China, the United States, the United Kingdom, France, and Germany. NaVAB implements a national value extraction pipeline to efficiently construct value assessment datasets. Specifically, we propose a modeling procedure with instruction tagging to process raw data sources, a screening process to filter value-related topics and a generation process with a Conflict Reduction mechanism to filter non-conflicting values. We conduct extensive experiments on various LLMs across countries, and the results provide insights into assisting in the identification of misaligned scenarios. Moreover, we demonstrate that NaVAB can be combined with alignment techniques to effectively reduce value concerns by aligning LLMs’ values with the target country.

## Data Description

NaVAB (National Values Alignment Benchmark): value assessment datasets derived from official media outlets across 5 nations (China, US, UK, France, Germany), with quoted and official statement evaluation sets totaling ~60,000+ value statement triples.


## Notes

