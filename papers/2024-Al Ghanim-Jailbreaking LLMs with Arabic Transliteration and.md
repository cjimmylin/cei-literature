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
authors: "[[Al Ghanim, Mansour]]; [[Almohaimeed, Saleh]]; [[Zheng, Mengxin]]; [[Solihin, Yan]]; [[Lou, Qian]]"
url: "https://aclanthology.org/2024.emnlp-main.1034/"
external_pdf: "file:///Users/jimmylin/Zotero/storage/KHCWIX2B/2024 - Jailbreaking LLMs with Arabic Transliteration and Arabizi.pdf"
national_ethnic_cultural: "Arabic"
cultures_nationalities_list: "Arabic"
languages_list: "Arabic"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: "Arabic, AI Safety & Alignment"
key_contribution: "Showed that LLMs are vulnerable to jailbreaking via Arabic transliteration ('Arabizi'), bypassing safety filters optimized for English or standard Arabic."
significance: "Highlights a specific 'low-resource language attack vector', where using a dialect/script mix (Arabizi) allows evasion of safety controls that work on the dominant language."
tags: 
abstract: "This study identifies the potential vulnerabilities of Large Language Models (LLMs) to ’jailbreak’ attacks, specifically focusing on the Arabic language and its various forms. While most research has concentrated on English-based prompt manipulation, our investigation broadens the scope to investigate the Arabic language. We initially tested the AdvBench benchmark in Standardized Arabic, finding that even with prompt manipulation techniques like prefix injection, it was insufficient to provoke..."
CONF-CC: "N/A"
DATE_ADDED: 20260208
LLM_assessed: "GPT-4, Claude"
DATA_URL: "https://github.com/SecureDL/arabic_jailbreak"
pdf_extract: "PDF Extracts/2024/2024-Al Ghanim-Jailbreaking LLMs with Arabic Transliteration and.md"
local_pdf: "[[PDFs/2024/2024-Al Ghanim-Jailbreaking LLMs with Arabic Transliteration and.pdf]]"
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "AI Safety & Alignment"
is_benchmark: "Yes"
is_eval: "No"
is_dataset: "No"
data_description: "Benchmark for ai safety"
data_metrics: "Not specified"
CONFERENCE: "EMNLP 2024"
---
# Jailbreaking LLMs with Arabic Transliteration and Arabizi

## Authors

[[Mansour Al Ghanim|Al Ghanim, Mansour]], [[Saleh Almohaimeed|Almohaimeed, Saleh]], [[Mengxin Zheng|Zheng, Mengxin]], [[Yan Solihin|Solihin, Yan]], [[Qian Lou|Lou, Qian]]

## Links

- **ACL Anthology:** https://aclanthology.org/2024.emnlp-main.1034/

## Abstract

This study identifies the potential vulnerabilities of Large Language Models (LLMs) to ‘jailbreak’ attacks, specifically focusing on the Arabic language and its various forms. While most research has concentrated on English-based prompt manipulation, our investigation broadens the scope to investigate the Arabic language. We initially tested the AdvBench benchmark in Standardized Arabic, finding that even with prompt manipulation techniques like prefix injection, it was insufficient to provoke LLMs into generating unsafe content. However, when using Arabic transliteration and chatspeak (or arabizi), we found that unsafe content could be produced on platforms like OpenAI GPT-4 and Anthropic Claude 3 Sonnet. Our findings suggest that using Arabic and its various forms could expose information that might remain hidden, potentially increasing the risk of jailbreak attacks. We hypothesize that this exposure could be due to the model’s learned connection to specific words, highlighting the need for more comprehensive safety training across all language forms.

## Data Description

The study uses the AdvBench benchmark containing 520 harmful prompts, which are translated into Arabic and converted into Arabic transliteration and chatspeak (Arabizi) forms. The prompts are tested against OpenAI GPT-4-0613 and Anthropic Claude-3-Sonnet-20240229 to evaluate jailbreak vulnerability through Arabic language variants. Manual evaluation categorizes LLM outputs into refusal and non-refusal categories including unsafe content generation.


## Notes

