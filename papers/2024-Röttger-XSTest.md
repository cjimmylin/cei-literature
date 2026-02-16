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
authors: "[[Röttger, Paul]]; [[Kirk, Hannah]]; [[Vidgen, Bertie]]; [[Attanasio, Giuseppe]]; [[Bianchi, Federico]]; [[Hovy, Dirk]]"
url: "https://aclanthology.org/2024.naacl-long.301/"
external_pdf: "file:///Users/jimmylin/Zotero/storage/W25TJPES/2024 - XSTest A Test Suite for Identifying Exaggerated Safety Behaviours in Large Language Models.pdf"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: "AI Safety & Alignment"
key_contribution: "Introduced XSTest, a test suite designed to identify 'exaggerated safety behaviors' (over-refusals) where models incorrectly refuse safe prompts (e.g., historical facts) due to safety filters."
significance: "Highlights the 'safety-helpfulness trade-off', showing that current alignment methods often result in models that are too cautious, reducing their utility for legitimate user queries."
tags: 
abstract: "Without proper safeguards, large language models will readily follow malicious instructions and generate toxic content. This risk motivates safety efforts such as red-teaming and large-scale feedback learning, which aim to make models both helpful and harmless. However, there is a tension between these two objectives, since harmlessness requires models to refuse to comply with unsafe prompts, and thus not be helpful."
DATE_ADDED: 20260208
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
LLM_assessed: "GPT-4, Llama-2, Mistral"
DATA_URL: "https://github.com/paul-rottger/exaggerated-safety"
pdf_extract: "PDF Extracts/2024/2024-Röttger-XSTest.md"
local_pdf: [[PDFs/2024/2024-Röttger-XSTest.pdf]]
---
# XSTest: A Test Suite for Identifying Exaggerated Safety Behaviours in Large Language Models

## Authors

[[Paul Röttger|Röttger, Paul]], [[Hannah Kirk|Kirk, Hannah]], [[Bertie Vidgen|Vidgen, Bertie]], [[Giuseppe Attanasio|Attanasio, Giuseppe]], [[Federico Bianchi|Bianchi, Federico]], [[Dirk Hovy|Hovy, Dirk]]

## Links

- **ACL Anthology:** https://aclanthology.org/2024.naacl-long.301/

## Abstract

Without proper safeguards, large language models will readily follow malicious instructions and generate toxic content. This risk motivates safety efforts such as red-teaming and large-scale feedback learning, which aim to make models both helpful and harmless. However, there is a tension between these two objectives, since harmlessness requires models to refuse to comply with unsafe prompts, and thus not be helpful. Recent anecdotal evidence suggests that some models may have struck a poor balance, so that even clearly safe prompts are refused if they use similar language to unsafe prompts or mention sensitive topics. In this paper, we introduce a new test suite called XSTest to identify such eXaggerated Safety behaviours in a systematic way. XSTest comprises 250 safe prompts across ten prompt types that well-calibrated models should not refuse to comply with, and 200 unsafe prompts as contrasts that models, for most applications, should refuse. We describe XSTest’s creation and composition, and then use the test suite to highlight systematic failure modes in state-of-the-art language models as well as more general challenges in building safer language models.

## Data Description

XSTEST is a test suite comprising 250 safe prompts across ten prompt types and 200 unsafe contrast prompts designed to identify exaggerated safety behaviours in LLMs. The benchmark evaluates models on their propensity to refuse safe prompts that superficially resemble unsafe ones, covering categories including homonyms, figurative language, safe targets, safe contexts, definitions, discrimination, historical events, and privacy.


## Notes

