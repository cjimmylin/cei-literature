---


Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: Y7FJU6YL
type: conferencePaper
short_title: "WildTeaming at Scale"
year: 2025
first_author: "[[Liwei Jiang]]"
last_author: "[[Nouha Dziri]]"
authors: "Liwei Jiang; Kavel Rao; Seungju Han; Allyson Ettinger; Faeze Brahman; Sachin Kumar; Niloofar Mireshghallah; Ximing Lu; Maarten Sap; Yejin Choi; Nouha Dziri"
doi: 10.48550/arXiv.2406.18510
url: "https://arxiv.org/abs/2406.18510"
external_pdf: "https://arxiv.org/pdf/2406.18510.pdf"
national_ethnic_cultural: American
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: N/A
newtags: "American, AI Safety & Alignment"
key_contribution: "Introduced WildTeaming, an automated red-teaming framework that mines 'in-the-wild' user jailbreak tactics (5.7k clusters) to discover novel vulnerabilities."
significance: "Demonstrates that leveraging real-world user attack patterns (rather than just synthetic ones) significantly improves the diversity and success rate of red-teaming, revealing vulnerabilities frontier models miss."
tags: 
pdf_extract: "PDF Extracts/2024/2024-Jiang-WildTeaming at Scale.md"
abstract: "We introduce WILDTEAMING, an automatic red-teaming framework that mines in-the-wild user-chatbot interactions to discover 5.7K unique clusters of novel jail- break tactics, and then composes selections of multiple mined tactics for systematic exploration of novel and even more challenging jailbreaks. Compared to prior work that performed red-teaming via recruited human workers, gradient-based optimization, or iterative revision with large language models (LLMs), our work investigates jailbreaks"
paper_summary: "Abstract: We introduce WILDTEAMING, an automatic red-teaming framework that mines in-the-wild user-chatbot interactions to discover 5.7K unique clusters of novel jail- break tactics, and then composes selection | Overview: WILDTEAMING at Scale: From In-the-Wild Jailbreaks to (Adversarially) Safer Language Models Liwei Jiang1,2 Kavel Rao∗,1 Seungju Han∗,2,3 Allyson Ettinger2 Faeze Brahman2 Sachin Kumar2 Niloofar Mireshgh | Methodology: ASR ↑Query ↓ PPL ↓ASR×5 30 ↑Query×5 30 ↓Sim@5 30 ↓Simall ↓#Tacticall ↑ Vicuna (7B) WILDTEAM 93.1 | Key Findings: benchmark including test vanilla harmful prompts across standard, contextual, and copyright unsafe behaviors. In this work, we report results using 15 | Conclusions: With empirical insights gleaned from WILDTEAMING and WILDJAILBREAK, we discuss three key areas for improvement for contemporary LLMs safety and genera"
local_pdf: "[[PDFs/2024/2024-Jiang-WildTeaming at Scale.pdf]]"
ethics_overall: No
virtue_ethics: No
deontological_ethics: No
utilitarian_ethics: No
ethics_perspective: "AI Safety & Alignment"
is_benchmark: No
is_eval: Yes
is_dataset: Yes
data_description: "Evaluation framework dataset"
data_metrics: "Not specified"
LLM_assessed: "GPT-4, Vicuna, Mistral, Mixtral, Llama-2, Llama-3"
DATA_URL: "https://huggingface.co/datasets/allenai/wildjailbreak"
---
# WildTeaming at Scale: From In-the-Wild Jailbreaks to (Adversarially) Safer Language Models

## Metadata

**Authors:** Jiang, Liwei; Rao, Kavel; Han, Seungju; Ettinger, Allyson; Brahman, Faeze; Kumar, Sachin; Mireshghallah, Niloofar; Lu, Ximing; Sap, Maarten; Choi, Yejin; Dziri, Nouha

**Year:** 2024

**Publication:** arXiv preprint arXiv:2406.18510

**Type:** conferencePaper

**DOI:** [10.48550/arXiv.2406.18510](https://doi.org/10.48550/arXiv.2406.18510)

## Links

- **Local PDF:** [[PDFs/2024/2024-Jiang-WildTeaming at Scale.pdf|Open PDF]]

- **arXiv:** https://arxiv.org/abs/2406.18510
- **DOI:** https://doi.org/10.48550/arXiv.2406.18510

## Abstract

We introduce WildTeaming, an automatic LLM safety red-teaming framework that mines in-the-wild user-chatbot interactions to discover 5.7K unique clusters of novel jailbreak tactics, and then composes multiple tactics for systematic exploration of novel jailbreaks. Compared to prior work that performed red-teaming via recruited human workers, gradient-based optimization, or iterative revision with LLMs, our work investigates jailbreaks from chatbot users who were not specifically instructed to break the system. WildTeaming reveals previously unidentified vulnerabilities of frontier LLMs, resulting in up to 4.6x more diverse and successful adversarial attacks compared to state-of-the-art jailbreak methods. While many datasets exist for jailbreak evaluation, very few open-source datasets exist for jailbreak training, as safety training data has been closed even when model weights are open. With WildTeaming we create WildJailbreak, a large-scale open-source synthetic safety dataset with 262K vanilla (direct request) and adversarial (complex jailbreak) prompt-response pairs. To mitigate exaggerated safety behaviors, WildJailbreak provides two contrastive types of queries: 1) harmful queries (vanilla & adversarial) and 2) benign queries that resemble harmful queries in form but contain no harm. As WildJailbreak considerably upgrades the quality and scale of existing safety resources, it uniquely enables us to examine the scaling effects of data and the interplay of data properties and model capabilities during safety training. Through extensive experiments, we identify the training properties that enable an ideal balance of safety behaviors: appropriate safeguarding without over-refusal, effective handling of vanilla and adversarial queries, and minimal, if any, decrease in general capabilities. All components of WildJailbeak contribute to achieving balanced safety behaviors of models.

## Authors

[[Liwei Jiang]], [[Kavel Rao]], [[Seungju Han]], [[Allyson Ettinger]], [[Faeze Brahman]], [[Sachin Kumar]], [[Niloofar Mireshghallah]], [[Ximing Lu]], [[Maarten Sap]], [[Yejin Choi]], [[Nouha Dziri]]

## Data Description

WildJailbreak is a large-scale open-source synthetic safety dataset containing 262K prompt-response pairs organized into four contrastive components: vanilla harmful queries, vanilla benign queries, adversarial harmful queries, and adversarial benign queries. The dataset was created using the WildTeaming framework, which mines 5.7K unique clusters of jailbreak tactics from real-world user-chatbot interactions in LMSYS-Chat-1M and WildChat, then composes these tactics to generate diverse adversarial attacks for safety training.


## Notes


## Citation Info

91 citations (Semantic Scholar/DOI) [2025-08-27]
