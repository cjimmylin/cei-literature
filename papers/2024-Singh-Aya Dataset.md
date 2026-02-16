---


Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: PH662KCP
type: journalArticle
short_title: "Aya Dataset"
year: 2025
first_author: "[[Ahmet Üstün]]"
last_author: "[[Sara Hooker]]"
authors: "Ahmet Üstün; Viraat Aryabumi; Zheng-Xin Yong; Wei-Yin Ko; Daniel D'souza; Gbemileke Onilude; Neel Bhandari; Shivalika Singh; Hui-Lee Ooi; Amr Kayid; Freddie Vargus; Phil Blunsom; Shayne Longpre; Niklas Muennighoff; Marzieh Fadaee; Julia Kreutzer; Sara Hooker"
url: "https://arxiv.org/abs/2402.07827"
external_pdf: "https://arxiv.org/pdf/2402.07827.pdf"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "Cross-cultural"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: "AI Safety & Alignment"
key_contribution: "Released Aya, a massively multilingual generative model and dataset covering 101 languages (50% lower-resourced), significantly expanding access to instruction-tuned AI."
significance: "Challenges the 'data-rich' language hegemony by providing high-quality, open-source resources for low-resource languages, fostering more equitable global AI development."
tags: 
pdf_extract: "PDF Extracts/2024/2024-Singh-Aya Dataset.md"
abstract: "Recent breakthroughs in large language models (LLMs) have centered around a handful of data-rich languages. What does it take to broaden access to breakthroughs beyond first-class citizen languages? Our work introduces Aya, a massively multilingual generative language model that follows instructions in 101 languages of which over 50% are considered as lower-resourced. Aya outperforms mT0 and BLOOMZ on the majority of tasks while covering double the number of languages."
paper_summary: "Abstract: Recent breakthroughs in large language models (LLMs) have centered around a handful of data-rich languages. What does it take to broaden access to breakthroughs beyond first-class citizen languages? O | Overview: Aya Model: An Instruction Finetuned Open-Access Multilingual Language Model Ahmet Üstün♦1, Viraat Aryabumi♦1, Zheng-Xin Yong♦2,4, Wei-Yin Ko♦3, Daniel D'souza♦4, Gbemileke Onilude5, Neel Bhandari4, Sh | Methodology: also works in a multilingual setup. We take inspiration from the critique-and-revise approach proposed by Bai et al. [2022b] for a one-step classify-a | Key Findings: of performance across varied tasks. Aya is built by fine-tuning 13B parameter mT5 model [Xue et al., 2020] using an instruction mixture that includes  | Conclusions: What we know is a drop, what we don't know is an ocean. — Isaac Newton Model Choice: We selected mT5 [Xue et al., 2020] as our base model. This decisi"
local_pdf: "[[PDFs/2024/2024-Singh-Aya Dataset.pdf]]"
DATE_ADDED: 20260208
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "AI Safety & Alignment"
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Evaluation approach dataset for toxicity detection"
data_metrics: "101 languages; 99 languages"
LLM_assessed: BLOOM
DATA_URL: "https://hf.co/CohereForAI/aya-101"
---
# Aya Dataset: A Massively Multilingual Instruction-Tuned Dataset

## Metadata

**Authors:** Singh, A.

**Year:** 2024

**Type:** journalArticle

## Links

- **Local PDF:** [[PDFs/2024/2024-Singh-Aya Dataset.pdf|Open PDF]]

- **arXiv:** https://arxiv.org/abs/2402.07827

## Abstract

Recent breakthroughs in large language models (LLMs) have centered around a handful of data-rich languages. What does it take to broaden access to breakthroughs beyond first-class citizen languages? Our work introduces Aya, a massively multilingual generative language model that follows instructions in 101 languages of which over 50% are considered as lower-resourced. Aya outperforms mT0 and BLOOMZ on the majority of tasks while covering double the number of languages. We introduce extensive new evaluation suites that broaden the state-of-art for multilingual eval across 99 languages -- including discriminative and generative tasks, human evaluation, and simulated win rates that cover both held-out tasks and in-distribution performance. Furthermore, we conduct detailed investigations on the optimal finetuning mixture composition, data pruning, as well as the toxicity, bias, and safety of our models. We open-source our instruction datasets and our model at https://hf.co/CohereForAI/aya-101

## Authors

[[Ahmet Üstün]], [[Viraat Aryabumi]], [[Zheng-Xin Yong]], [[Wei-Yin Ko]], [[Daniel D'souza]], [[Gbemileke Onilude]], [[Neel Bhandari]], [[Shivalika Singh]], [[Hui-Lee Ooi]], [[Amr Kayid]], [[Freddie Vargus]], [[Phil Blunsom]], [[Shayne Longpre]], [[Niklas Muennighoff]], [[Marzieh Fadaee]], [[Julia Kreutzer]], [[Sara Hooker]]

## Data Description

The paper introduces the Aya model and associated multilingual instruction finetuning datasets covering 101 languages. The training mixture includes xP3x (168M examples), Aya Collection (templated, translated, and human-annotated data totaling 513M instances), Data Provenance Collection (1.65M examples), and ShareGPT-Command (6.8M synthetic examples). The Aya Dataset specifically contains 204K human-curated prompt-response pairs across 65 languages, and evaluation spans discriminative tasks, generative tasks, human evaluation, and safety assessments across 99 languages.


## Notes


## Citation Info

728 citations (Semantic Scholar/arXiv) [2025-08-27]
