---



































Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: BH9GAFPJ
type: document
short_title: "Jailbreaking LLMs with Arabic Transliteration and"
year: 2024
first_author: "[[Mansour Al Ghanim]]"
last_author: "[[Lou, Qian]]"
authors: "Al Ghanim, Mansour; Almohaimeed, Saleh; Zheng, Mengxin; Solihin, Yan; Lou, Qian"
url: "https://aclanthology.org/2024.emnlp-main.1034/"
external_pdf: "file:///Users/jimmylin/Zotero/storage/KHCWIX2B/2024 - Jailbreaking LLMs with Arabic Transliteration and Arabizi.pdf"
national_ethnic_cultural: "Arabic"
cultures_nationalities_list: "Arabic"
languages_list: "Arabic"
religious_values: "Christianity"
rv_islam: 0
rv_christianity: 50
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
religious_values_list: "Christianity"
mp_mft: 0
mp_schwartz: 0
mp_trolley: 0
mp_kohlberg: 0
mp_dual_process: 0
mp_intuitionist: 0
mp_dyadic: 0
mp_identity: 0
moral_psychology: "N/A"
newtags: "Arabic, AI Safety & Alignment"
key_contribution: "Showed that LLMs are vulnerable to jailbreaking via Arabic transliteration ('Arabizi'), bypassing safety filters optimized for English or standard Arabic."
significance: "Highlights a specific 'low-resource language attack vector', where using a dialect/script mix (Arabizi) allows evasion of safety controls that work on the dominant language."
tags: 
abstract: "This study identifies the potential vulnerabilities of Large Language Models (LLMs) to ’jailbreak’ attacks, specifically focusing on the Arabic language and its various forms. While most research has concentrated on English-based prompt manipulation, our investigation broadens the scope to investigate the Arabic language. We initially tested the AdvBench benchmark in Standardized Arabic, finding that even with prompt manipulation techniques like prefix injection, it was insufficient to provoke..."
CONF-CC: "N/A"
DATE_ADDED: 20260208
LLM_assessed: "Claude-3, GPT-4"
DATA_URL: "https://github.com/SecureDL/arabic_jailbreak"
pdf_extract: "PDF Extracts/2024/2024-Al Ghanim-Jailbreaking LLMs with Arabic Transliteration and.md"
local_pdf: "[[PDFs/2024/2024-Al Ghanim-Jailbreaking LLMs with Arabic Transliteration and.pdf]]"
CONFERENCE: "EMNLP 2024"
ethics_overall: 0
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
ethics_perspective: "AI Safety & Alignment"
is_benchmark: No
is_eval: Yes
is_dataset: "No"
data_description: "Benchmark for ai safety"
data_metrics: "Not specified"
---
# Jailbreaking LLMs with Arabic Transliteration and Arabizi

## Authors

[[Mansour Al Ghanim|Al Ghanim, Mansour]], [[Saleh Almohaimeed|Almohaimeed, Saleh]], [[Mengxin Zheng|Zheng, Mengxin]], [[Yan Solihin|Solihin, Yan]], [[Qian Lou|Lou, Qian]]

## Links

- **ACL Anthology:** https://aclanthology.org/2024.emnlp-main.1034/

## Abstract

This study identifies the potential vulnerabilities of Large Language Models (LLMs) to ‘jailbreak’ attacks, specifically focusing on the Arabic language and its various forms. While most research has concentrated on English-based prompt manipulation, our investigation broadens the scope to investigate the Arabic language. We initially tested the AdvBench benchmark in Standardized Arabic, finding that even with prompt manipulation techniques like prefix injection, it was insufficient to provoke LLMs into generating unsafe content. However, when using Arabic transliteration and chatspeak (or arabizi), we found that unsafe content could be produced on platforms like OpenAI GPT-4 and Anthropic Claude 3 Sonnet. Our findings suggest that using Arabic and its various forms could expose information that might remain hidden, potentially increasing the risk of jailbreak attacks. We hypothesize that this exposure could be due to the model’s learned connection to specific words, highlighting the need for more comprehensive safety training across all language forms.

## Data Description

Code and evaluation framework for testing jailbreak attacks on LLMs using Arabic transliteration and chatspeak (Arabizi) forms.


## Notes

