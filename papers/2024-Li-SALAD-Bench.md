---







Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: YKYNNAQX
type: document
short_title: SALAD-Bench
year: 2024
first_author: "[[Lijun Li]]"
last_author: "[[Shao, Jing]]"
authors: "[[Li, Lijun]]; [[Dong, Bowen]]; [[Wang, Ruohui]]; [[Hu, Xuhao]]; [[Zuo, Wangmeng]]; [[Lin, Dahua]]; [[Qiao, Yu]]; [[Shao, Jing]]"
url: "https://aclanthology.org/2024.findings-acl.235/"
external_pdf: "file:///Users/jimmylin/Zotero/storage/6WRTXGCW/2024 - SALAD-Bench A Hierarchical and Comprehensive Safety Benchmark for Large Language Models.pdf"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: ""
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: Utilitarianism
key_contribution: "Proposes SALAD-Bench, a hierarchical safety benchmark evaluating LLMs, attacks, and defenses, featuring an LLM-based 'MD-Judge'"
significance: "Provides a comprehensive ecosystem for testing the 'attack-defense' dynamic, moving beyond static safety benchmarks to evaluating resilience against evolving threats"
tags: 
abstract: "In the rapidly evolving landscape of Large Language Models (LLMs), ensuring robust safety measures is paramount. To meet this crucial need, we propose SALAD-Bench, a safety benchmark specifically designed for evaluating LLMs, attack, and defense methods. Distinguished by its breadth, SALAD-Bench transcends conventional benchmarks through its large scale, rich diversity, intricate taxonomy spanning three levels, and versatile functionalities."
DATE_ADDED: 20260208
LLM_assessed: "GPT-4, GPT-3.5, Claude, Gemini, Llama-2, Llama-3, Mistral, Mixtral, Qwen, Gemma, Vicuna"
DATA_URL: "https://github.com/OpenSafetyLab/SALAD-BENCH"
pdf_extract: "PDF Extracts/2024/2024-Li-SALAD-Bench.md"
local_pdf: "[[PDFs/2024/2024-Li-SALAD-Bench.pdf]]"
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "Yes"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "No"
data_description: "Benchmark for ai safety"
data_metrics: "Not specified"
CONFERENCE: "ACL 2024"
---
# SALAD-Bench: A Hierarchical and Comprehensive Safety Benchmark for Large Language Models

## Authors

[[Lijun Li|Li, Lijun]], [[Bowen Dong|Dong, Bowen]], [[Ruohui Wang|Wang, Ruohui]], [[Xuhao Hu|Hu, Xuhao]], [[Wangmeng Zuo|Zuo, Wangmeng]], [[Dahua Lin|Lin, Dahua]], [[Yu Qiao|Qiao, Yu]], [[Jing Shao|Shao, Jing]]

## Links

- **ACL Anthology:** https://aclanthology.org/2024.findings-acl.235/

## Abstract

In the rapidly evolving landscape of Large Language Models (LLMs), ensuring robust safety measures is paramount. To meet this crucial need, we propose SALAD-Bench, a safety benchmark specifically designed for evaluating LLMs, attack, and defense methods. Distinguished by its breadth, SALAD-Bench transcends conventional benchmarks through its large scale, rich diversity, intricate taxonomy spanning three levels, and versatile functionalities.SALAD-Bench is crafted with a meticulous array of questions, from standard queries to complex ones enriched with attack, defense modifications and multiple-choice. To effectively manage the inherent complexity, we introduce an innovative evaluators: the LLM-based MD-Judge for QA pairs with a particular focus on attack-enhanced queries, ensuring a seamless, and reliable evaluation. Above components extend SALAD-Bench from standard LLM safety evaluation to both LLM attack and defense methods evaluation, ensuring the joint-purpose utility. Our extensive experiments shed light on the resilience of LLMs against emerging threats and the efficacy of contemporary defense tactics. Data and evaluator are released under https://github.com/OpenSafetyLab/SALAD-BENCH

## Data Description

SALAD-Bench is a hierarchical safety benchmark for LLMs comprising approximately 30,000 questions organized into a three-level taxonomy of 6 domains, 16 tasks, and 66 categories. The benchmark includes a base set of 21K questions, 5K attack-enhanced questions, 200 defense-enhanced questions, and 4K multiple-choice questions. Data sources include public safety datasets and self-instructed data generated via fine-tuned GPT-3.5-turbo, with automated labeling achieving 94.3% consistency with human annotations.


## Notes

