---
































Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: ER38ZQNK
type: preprint
short_title: "Can LLMs Grasp Implicit Cultural Values?"
year: 2025
first_author: "[[Ziyi Liu]]"
last_author: "[[Zhao, Jieyu]]"
authors: "Liu, Ziyi; Dey, Priyanka; Zhao, Zhenyu; Huang, Jen-tse; Gupta, Rahul; Liu, Yang; Zhao, Jieyu"
doi: 10.48550/arXiv.2504.01127
tags: 
url: "http://arxiv.org/abs/2504.01127"
pdf_extract: "PDF Extracts/2025/2025-Liu-Can LLMs Grasp Implicit Cultural Values.md"
local_pdf: "[[Lit-WS-Lit-WS-PDFs/2025/2025-Liu-Can LLMs Grasp Implicit Cultural Values.pdf]]"
external_pdf: "http://arxiv.org/pdf/2504.01127.pdf"
national_ethnic_cultural: "Multicultural/Cross-cultural"
cultures_nationalities_list: "Multicultural/Cross-cultural"
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
newtags: "Multicultural/Cross-cultural, Virtue Ethics"
key_contribution: "Introduces CQ-Bench, a benchmark for evaluating LLMs' metacognitive cultural intelligence and ability to infer implicit values"
significance: "Demonstrates that while LLMs can select explicit values, they struggle with granular attitude detection and open-ended cultural reasoning"
abstract: "Cultural Intelligence (CQ) refers to the ability to understand unfamiliar cultural contexts—a crucial skill for large language models (LLMs) to effectively engage with globally diverse users. Existing studies often focus on explicitly stated cultural norms, but fail to capture the subtle, implicit values that are common in daily conversation. To address this gap, we introduce CQ-Bench, a benchmark specifically designed to assess LLMs’ capability to infer implicit cultural values from natural..."
paper_summary: "Abstract: Cultural Intelligence (CQ) refers to the ability to understand unfamiliar cultural contexts—a crucial skill for large language models (LLMs) to effectively engage with globally diverse users. Existing | Overview: Can LLMs Grasp Implicit Cultural Values? Benchmarking LLMs' Cultural Intelligence with CQ-Bench Ziyi Liu1 Priyanka Dey1 Jen-tse Huang3 Zhenyu Zhao1 Bowen Jiang4 Rahul Gupta2 Yang Liu2 Yao Du1 Jieyu Zh | Methodology: for extracting social norms from conversations, em- phasizing norm mining rather than cultural value identification. In contrast, our work focuses on  | Key Findings: We construct three escalating tasks—attitude detection, value selection, and value extraction—to systemati- cally evaluate open-sourced and close-sour | Conclusions: We introduce CQ-Bench, a benchmark for evaluat- ing LLMs' ability to infer implicit cultural values in conversations. CQ-Bench assesses model's cul- t"
LLM_assessed: "DeepSeek, GPT-4o, Llama-3, Qwen, Qwen-2, o1"
DATA_URL: "https://github.com/uscnlp-lime/CQ-Bench"
publication: arXiv
CONF-CC: "Preprint"
DATE_ADDED: 20260207
CONFERENCE: "Preprint"
ethics_overall: 0
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
nw_confucian: 0
nw_ubuntu: 0
nw_islamic_ethics: 0
nw_buddhist: 0
nw_dharmic: 0
nw_indigenous_relational: 0
nw_buen_vivir: 0
author_country: "US"
author_region: "North America"
author_global_north_south: "Global North"
weird_score: 78
is_benchmark: "Yes"
is_eval: "No"
is_dataset: "Yes"
data_description: "Benchmark for moral/ethical reasoning text corpus for conversational ai"
data_metrics: "Not specified"
---
 Can LLMs Grasp Implicit Cultural Values? Benchmarking LLMs' Metacognitive Cultural Intelligence with CQ-Bench

## Authors

[[Ziyi Liu|Liu, Ziyi]], [[Priyanka Dey|Dey, Priyanka]], [[Zhenyu Zhao|Zhao, Zhenyu]], [[Jen-tse Huang|Huang, Jen-tse]], [[Rahul Gupta|Gupta, Rahul]], [[Yang Liu|Liu, Yang]], [[Jieyu Zhao|Zhao, Jieyu]]

## Links

- **Local PDF:** [[Lit-WS-Lit-WS-PDFs/2025/2025-Liu-Can LLMs Grasp Implicit Cultural Values.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2504.01127
- **DOI:** https://doi.org/10.48550/arXiv.2504.01127

## Abstract

Cultural Intelligence (CQ) refers to the ability to understand unfamiliar cultural contexts—a crucial skill for large language models (LLMs) to effectively engage with globally diverse users. While existing research often focuses on explicitly stated cultural norms, such approaches fail to capture the subtle, implicit values that underlie real-world conversations. To address this gap, we introduce CQ-Bench, a benchmark specifically designed to assess LLMs’ capability to infer implicit cultural values from natural conversational contexts. We generate multi-character conversationbased stories dataset using values from the World Value Survey and GlobalOpinions datasets, with topics including ethical, religious, social, and political. Our dataset construction pipeline includes rigorous validation procedures—incorporation, consistency, and implicitness checks—using GPT-4o, with 98.2% human-model agreement in the final validation. Our benchmark consists of three tasks of increasing complexity: attitude detection, value selection, and value extraction. We find that while o1 and Deepseek-R1 models reach human-level performance in value selection (0.809 and 0.814), they still fall short in nuanced attitude detection, with F1 scores of 0.622 and 0.635, respectively. In the value extraction task, GPT4o-mini and o3-mini score 0.602 and 0.598, highlighting the difficulty of open-ended cultural reasoning. Notably, fine-tuning smaller models (e.g., LLaMA-3.2-3B) on only 500 culturally rich examples improves performance by over 10% overall, even outperforming stronger baselines (o3-mini) in some cases. Using CQ-Bench1, we provide insights into the current challenges in LLMs’ CQ research and suggest practical pathways for enhancing LLMs’ cross-cultural reasoning abilities.

## Detailed Summary

This paper introduces **CQ-Bench** (Cultural Intelligence Benchmark), designed to test whether Large Language Models (LLMs) can grasp **implicit cultural values**. While models are often tuned to recognize explicit cultural facts ("What is the harvest festival in Japan?"), they struggle with the subtle, unspoken values that drive real-world conversation and conflict.

## Paper Outline

1.  **Introduction**: Limits of explicit cultural knowledge; Need for implicit Cultural Intelligence (CQ).
2.  **CQ-Bench Construction**:
    *   **Data Source**: values from World Value Survey (WVS) & Global Opinions.
    *   **Generation**: Using LLMs to weave these values into "Show, Don't Tell" dialogue scenarios.
    *   **Validation**: Human verification of implicitness and consistency.
3.  **Experimental Tasks**: Attitude Detection, Value Selection, and Value Extraction.
4.  **Results**: Frontier models vs. Open weights; Effect of "Culturally-Rich" fine-tuning.
5.  **Conclusion**: Implicit CQ is a distinct capability frontier.

## Methods Summary

The authors construct a dataset of naturalistic conversations where characters express views grounded in data from the **World Value Survey (WVS)**. Evaluation involves three tasks of increasing complexity:
1.  **Attitude Detection**: Identifying if a speaker is positive/negative/neutral toward a topic.
2.  **Value Selection**: Choosing which cultural values are at play from a list.
3.  **Value Extraction**: Open-ended reasoning about the cultural background.
The construction pipeline includes rigorous validation procedures—incorporation, consistency, and implicitness checks—using GPT-4o, with 98.2% human-model agreement.

## Results Summary

1.  **Frontier Performance**: While o1 and Deepseek-R1 models reach human-level performance in value selection (0.809 and 0.814), they fall short in nuanced attitude detection, with F1 scores of 0.622 and 0.635, respectively.
2.  **Implicit Gap**: Models that score high on general benchmarks often fail to pick up on *implied* cultural judgment in conversation, especially when it contradicts Western norms.
3.  **Data Efficiency**: Notably, fine-tuning smaller models (e.g., LLaMA-3.2-3B) on only 500 culturally rich examples improves performance by over 10% overall, even outperforming stronger baselines like o3-mini in some cases.

## Conclusions

Implicit CQ is a distinct capability frontier that is not automatically captured by increasing model scale. Explicit "System Prompts" are often overwritten by the model's underlying training data bias. Deeper cultural alignment requires diverse, "culturally-rich" data and specialized evaluation like CQ-Bench.

## Artifact Contributions

*   **CQ-Bench Dataset**: A benchmark for implicit cultural reasoning with 500+ scenarios.
*   **Evaluation Scripts**: Code for the 3 tasks (Attitude, Selection, Extraction).
*   **Fine-tuned Models**: Weights for CQ-aligned LLaMA models.

## Data Description

CQ-Bench: synthetic multi-character conversation-based stories with implicit cultural values sourced from the World Values Survey and GlobalOpinions, evaluated on three tasks of increasing difficulty: attitude detection, value selection, and value extraction.


## Notes


## Tags

#Computer-Science---Computation-and-Language

## Citation Info

2 citations (Semantic Scholar/arXiv) [2025-08-27] 1 citations (Semantic Scholar/DOI) [2025-08-27] 2 citations (Semantic Scholar/DOI) [2025-08-23] arXiv:2504.01127 [cs]
