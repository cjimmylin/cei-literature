---


Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: 3JVW2NQF
type: document
short_title: HackAPrompt
year: 2025
first_author: "[[Sander Schulhoff]]"
last_author: "[[Boyd-Graber, Jordan]]"
authors: "[[Schulhoff, Sander]]; [[Pinto, Jeremy]]; [[Khan, Anaum]]; [[Bouchard, Louis-François]]; [[Si, Chenglei]]; [[Anati, Svetlina]]; [[Tagliabue, Valen]]; [[Kost, Anson]]; [[Carnahan, Christopher]]; [[Boyd-Graber, Jordan]]"
url: "https://aclanthology.org/2023.emnlp-main.302/"
external_pdf: "https://aclanthology.org/2023.emnlp-main.302.pdf"
national_ethnic_cultural: N/A
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "Value Pluralism / Schwartz"
newtags: "Value Pluralism / Schwartz"
tags: 
local_pdf: "[[PDFs/2023/2023-Schulhoff-HackAPrompt.pdf]]"
pdf_extract: "PDF Extracts/2023/2023-Schulhoff-HackAPrompt.md"
abstract: "Large Language Models (LLMs) are deployed in interactive contexts with direct user engage- ment, such as chatbots and writing assistants. These deployments are vulnerable to prompt injection and jailbreaking (collectively, prompt hacking), in which models are manipulated to ignore their original instructions and follow potentially malicious ones. Although widely acknowledged as a significant security threat, there is a dearth of large-scale resources and quantitative studies on prompt hacking. T"
ethics_overall: No
virtue_ethics: No
deontological_ethics: No
utilitarian_ethics: No
research_topic: "AI Safety & Alignment"
is_benchmark: No
is_eval: No
is_dataset: Yes
data_description: Dataset
data_metrics: "Not specified"
LLM_assessed: "GPT-3, ChatGPT, Flan-T5"
DATA_URL: "NA"
---
# HackAPrompt: Automated Prompt Engineering for Attacking and Defending LLMs

## Authors

[[Sander Schulhoff|Schulhoff, Sander]], [[Jeremy Pinto|Pinto, Jeremy]], [[Anaum Khan|Khan, Anaum]], [[Louis-François Bouchard|Bouchard, Louis-François]], [[Chenglei Si|Si, Chenglei]], [[Svetlina Anati|Anati, Svetlina]], [[Valen Tagliabue|Tagliabue, Valen]], [[Anson Kost|Kost, Anson]], [[Christopher Carnahan|Carnahan, Christopher]], [[Jordan Boyd-Graber|Boyd-Graber, Jordan]]

## Links

- **Local PDF:** [[PDFs/2023/2023-Schulhoff-HackAPrompt.pdf|Open PDF]]

- **ACL Anthology:** https://aclanthology.org/2023.emnlp-main.302/

## Abstract

Large Language Models (LLMs) are increasingly being deployed in interactive contexts that involve direct user engagement, such as chatbots and writing assistants. These deployments are increasingly plagued by prompt injection and jailbreaking (collectively, prompt hacking), in which models are manipulated to ignore their original instructions and instead follow potentially malicious ones. Although widely acknowledged as a significant security threat, there is a dearth of a large-scale resource and quantitative study on prompt hacking. To address this lacuna, we launch a global prompt hacking competition, which allows for free-form human input attacks. We elicit 600K+ adversarial prompts against three state-of-the-art LLMs. We describe the dataset, which empirically verifies that current LLMs can indeed be manipulated via prompt hacking. We also present a comprehensive ontology of the types of adversarial prompts.

## Data Description

The paper introduces HackAPrompt, a global prompt hacking competition dataset containing over 600,000 adversarial prompts from 2,800+ participants across 50+ countries. The dataset is divided into Submissions and Playground datasets, testing prompt injection and jailbreaking attacks against GPT-3 (text-davinci-003), ChatGPT (GPT-3.5-turbo), and FlanT5-XXL across ten challenges of varying difficulty. The dataset is available on HuggingFace.


## Notes

