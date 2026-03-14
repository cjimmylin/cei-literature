---


































Human View: true
Human View Date: 2026-01-24
Human View note: "Chinese Role Playing Personas"
Not AI: 
key: 22DDETPV
type: journalArticle
short_title: CharacterEval
year: 2024
first_author: "[[Quan Tu]]"
last_author: "[[Rui Yan]]"
authors: "Quan Tu; Shilong Fan; Zihang Tian; Rui Yan"
url: "https://arxiv.org/abs/2401.01275"
pdf_extract: "PDF Extracts/2024/2024-Tu-CharacterEval.md"
local_pdf: "[[PDFs/2024/2024-Tu-CharacterEval.pdf]]"
external_pdf: "https://arxiv.org/pdf/2401.01275.pdf"
national_ethnic_cultural: "Chinese"
cultures_nationalities_list: "Chinese"
languages_list: "Chinese"
religious_values: "Confucianism"
rv_islam: 0
rv_christianity: 0
rv_buddhism: 0
rv_judaism: 0
rv_hinduism: 0
rv_sikhism: 0
rv_confucianism: 50
rv_taoism: 0
rv_shinto: 0
rv_jainism: 0
rv_bahai: 0
rv_zoroastrianism: 0
rv_ubuntu: 0
rv_indigenous: 0
religious_values_list: "Confucianism"
mp_mft: 0
mp_schwartz: 0
mp_trolley: 0
mp_kohlberg: 0
mp_dual_process: 0
mp_intuitionist: 0
mp_dyadic: 0
mp_identity: 0
moral_psychology: "N/A"
newtags: "Chinese, Virtue Ethics"
key_contribution: "Introduces CharacterEval, a comprehensive Chinese benchmark for evaluating Role-Playing Conversational Agents across four dimensions"
significance: "Addresses the lack of benchmarks for role-playing agents (RPCAs) and evaluates the ability of LLMs to maintain consistent character personas, a prerequisite for simulacra-based virtue modeling"
tags: 
abstract: "Recently, the advent of large language models (LLMs) has revolutionized generative agents. Among them, Role-Playing Conversational Agents (RPCAs) attract considerable attention due to their ability to emotionally engage users. However, the absence of a comprehensive benchmark impedes progress in this field. To bridge this gap, we introduce CharacterEval, a Chinese benchmark for comprehensive RPCA assessment, complemented by a tailored high-quality dataset. The dataset contains 1,785 multi-turn dialogues with approximately 23,000 examples featuring 77 characters sourced from Chinese literary works. We employ a multifaceted evaluation approach, encompassing thirteen targeted metrics across four dimensions."
paper_summary: "Introduces CharacterEval, a Chinese benchmark for evaluating Role-Playing Conversational Agents (RPCAs). Dataset contains 1,785 multi-turn dialogues with 23,000 examples featuring 77 characters from Chinese literary works. Employs 13 metrics across 4 dimensions; Chinese LLMs outperformed GPT-4 in role-playing tasks."
CONF-CC: "ACL 2024"
DATE_ADDED: 20260208
LLM_assessed: "Baichuan, ChatGLM, GPT-3.5, GPT-4, InternLM, Qwen"
DATA_URL: "https://github.com/morecry/CharacterEval"
CONFERENCE: "Journal"
ethics_overall: 0
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
research_topic: "AI Safety & Alignment"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Benchmark dataset for conversational ai"
data_metrics: "23,020 examples"
---
 CharacterEval: A Chinese Benchmark for Role-Playing Conversational Agent Evaluation

## Authors

[[Quan Tu]], [[Shilong Fan]], [[Zihang Tian]], [[Rui Yan]]

## Metadata

**Authors:** Tu, Quan; Fan, Shilong; Tian, Zihang; Yan, Rui

**Year:** 2024

**Type:** journalArticle

## Links

- **Local PDF:** [[PDFs/2024/2024-Tu-CharacterEval.pdf|Open PDF]]

- **arXiv:** https://arxiv.org/abs/2401.01275

## Abstract

Recently, the advent of large language models (LLMs) has revolutionized generative agents. Among them, Role-Playing Conversational Agents (RPCAs) attract considerable attention due to their ability to emotionally engage users. However, the absence of a comprehensive benchmark impedes progress in this field. To bridge this gap, we introduce CharacterEval, a Chinese benchmark for comprehensive RPCA assessment, complemented by a tailored high-quality dataset. The dataset comprises 1,785 multi-turn role-playing dialogues, encompassing 23,020 examples and featuring 77 characters derived from Chinese novels and scripts. It was carefully constructed, beginning with initial dialogue extraction via GPT-4, followed by rigorous human-led quality control, and enhanced with in-depth character profiles sourced from Baidu Baike. CharacterEval employs a multifaceted evaluation approach, encompassing thirteen targeted metrics on four dimensions. Comprehensive experiments on CharacterEval demonstrate that Chinese LLMs exhibit more promising capabilities than GPT-4 in Chinese role-playing conversation. Source code, data source and reward model will be publicly accessible at https://github.com/morecry/CharacterEval.

## Detailed Summary

Introduces **CharacterEval**, the first comprehensive Chinese benchmark for **Role-Playing Conversational Agents (RPCAs)**. As LLMs are increasingly used as "simulacra" of fictional or historical characters, evaluating their subjective performance (personality, tone, idioms) has become a major challenge. CharacterEval provides a high-quality dataset of Chinese characters and a multifaceted evaluation framework to measure how well AI agents maintain these complex personae.

## Paper Outline

1.  **Introduction**: The rise of RPCAs and the need for Chinese-specific benchmarks.
2.  **Related Work**: Role-playing benchmarks and subjective evaluation.
3.  **CharacterEval Benchmark**:
    *   **Dataset**: 1,785 dialogues for 77 characters.
    *   **Evaluation Dimensions**: Consistency, Engagement, Empathy, etc.
4.  **CharacterRM**: A tailored reward model for RPCA assessment.
5.  **Experiments**: Comparing GPT-4 and Chinese LLMs.
6.  **Conclusion**: The state of Chinese role-playing AI.

## Methods Summary

The authors create a benchmark with two main components:
1.  **Dataset Construction**: They extract dialogue and profiles for 77 characters from Chinese novels and scripts (via GPT-4 extraction followed by human verification). This includes detailed character "baike" (wikis) to ground the knowledge.
2.  **Multifaceted Evaluation**: They use 13 metrics across 4 dimensions: **Character Persona**, **Dialogue Quality**, **Immersion**, and **User Engagement**.
3.  **CharacterRM**: To automate this subjective evaluation, they train a **Role-Playing Reward Model (RM)** based on human preference annotations. This model is shown to correlate more highly with human judgment than GPT-4 prompting.

## Results Summary

1.  **Chinese LLM Performance**: Domestic models like Baichuan and Qwen often outperform GPT-4 on this benchmark. This is attributed to their deeper training on Chinese literature and cultural idioms.
2.  **Dimension Trade-offs**: Models that are highly "consistent" with character history sometimes struggle with "engagement," showing that role-playing is a delicate balance of accuracy and conversational flow.
3.  **Reward Model Efficacy**: CharacterRM successfully identifies subtle out-of-character behaviors that generic safety or helpfulness models miss.

## Conclusions

RPCAs require culturally and linguistically grounded evaluation. CharacterEval provides the necessary infrastructure to measure the "soul" of Chinese AI characters. The CharacterRM serves as a powerful automated proxy for human judgment in role-playing.

## Artifact Contributions

*   **CharacterEval Dataset**: 11,376 dialogue examples across 77 characters.
*   **CharacterRM**: A role-playing reward model for automated evaluation.
*   **Evaluation Pipeline**: A standardized suite for testing Chinese generative agents.

## Data Description

Introduces CharacterEval, a Chinese benchmark for role-playing conversational agent evaluation with 1,785 multi-turn dialogues, 11,376 examples, and 77 characters from Chinese novels and scripts, evaluated across 13 metrics on 4 dimensions.


## Notes


## Citation Info

61 citations (Semantic Scholar/arXiv) [2025-08-27] _eprint: 2401.01275 Published: arXiv preprint arXiv:2401.01275
