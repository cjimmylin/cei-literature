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
authors: "Li, Lijun; Dong, Bowen; Wang, Ruohui; Hu, Xuhao; Zuo, Wangmeng; Lin, Dahua; Qiao, Yu; Shao, Jing"
url: "https://aclanthology.org/2024.findings-acl.235/"
external_pdf: "file:///Users/jimmylin/Zotero/storage/6WRTXGCW/2024 - SALAD-Bench A Hierarchical and Comprehensive Safety Benchmark for Large Language Models.pdf"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: ""
religious_values: "N/A"
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
religious_values_list: "N/A"
mp_mft: 0
mp_schwartz: 0
mp_trolley: 0
mp_kohlberg: 0
mp_dual_process: 0
mp_intuitionist: 0
mp_dyadic: 0
mp_identity: 0
moral_psychology: "N/A"
newtags: Utilitarianism
key_contribution: "Proposes SALAD-Bench, a hierarchical safety benchmark evaluating LLMs, attacks, and defenses, featuring an LLM-based 'MD-Judge'"
significance: "Provides a comprehensive ecosystem for testing the 'attack-defense' dynamic, moving beyond static safety benchmarks to evaluating resilience against evolving threats"
tags: 
abstract: "In the rapidly evolving landscape of Large Language Models (LLMs), ensuring robust safety measures is paramount. To meet this crucial need, we propose SALAD-Bench, a safety benchmark specifically designed for evaluating LLMs, attack, and defense methods. Distinguished by its breadth, SALAD-Bench transcends conventional benchmarks through its large scale, rich diversity, intricate taxonomy spanning three levels, and versatile functionalities."
CONF-CC: "N/A"
DATE_ADDED: 20260208
LLM_assessed: "GPT-4, GPT-3.5, Claude, Llama-2, Llama-3, Mistral, Mixtral, Qwen, Qwen-1.5, Gemma, Vicuna, ChatGLM"
DATA_URL: "https://github.com/OpenSafetyLab/SALAD-BENCH"
pdf_extract: "PDF Extracts/2024/2024-Li-SALAD-Bench.md"
local_pdf: "[[PDFs/2024/2024-Li-SALAD-Bench.pdf]]"
CONFERENCE: "ACL 2024"
ethics_overall: 0
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 5
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: Yes
data_description: "Benchmark for ai safety"
data_metrics: "Not specified"
---
# SALAD-Bench: A Hierarchical and Comprehensive Safety Benchmark for Large Language Models

## Authors

[[Lijun Li|Li, Lijun]], [[Bowen Dong|Dong, Bowen]], [[Ruohui Wang|Wang, Ruohui]], [[Xuhao Hu|Hu, Xuhao]], [[Wangmeng Zuo|Zuo, Wangmeng]], [[Dahua Lin|Lin, Dahua]], [[Yu Qiao|Qiao, Yu]], [[Jing Shao|Shao, Jing]]

## Links

- **ACL Anthology:** https://aclanthology.org/2024.findings-acl.235/

## Abstract

In the rapidly evolving landscape of Large Language Models (LLMs), ensuring robust safety measures is paramount. To meet this crucial need, we propose SALAD-Bench, a safety benchmark specifically designed for evaluating LLMs, attack, and defense methods. Distinguished by its breadth, SALAD-Bench transcends conventional benchmarks through its large scale, rich diversity, intricate taxonomy spanning three levels, and versatile functionalities.SALAD-Bench is crafted with a meticulous array of questions, from standard queries to complex ones enriched with attack, defense modifications and multiple-choice. To effectively manage the inherent complexity, we introduce an innovative evaluators: the LLM-based MD-Judge for QA pairs with a particular focus on attack-enhanced queries, ensuring a seamless, and reliable evaluation. Above components extend SALAD-Bench from standard LLM safety evaluation to both LLM attack and defense methods evaluation, ensuring the joint-purpose utility. Our extensive experiments shed light on the resilience of LLMs against emerging threats and the efficacy of contemporary defense tactics. Data and evaluator are released under https://github.com/OpenSafetyLab/SALAD-BENCH

## Data Description

SALAD-Bench: a hierarchical safety benchmark with 30,000 questions spanning 6 domains, 16 tasks, and 66 categories for evaluating LLM safety, attack methods, and defense methods; includes standard QA, multiple-choice, attack-enhanced, and defense-enhanced question variants.


## Notes

