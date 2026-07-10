---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: 6AB9DUJG
type: document
short_title: MedHallTune
year: 2025
first_author: "[[Qiao Yan]]"
last_author: "[[Pheng-Ann Heng]]"
authors: "Qiao Yan; Yuchen Yuan; Xiaowei Hu; Yihan Wang; Jiaqi Xu; Jinpeng Li; Chi-Wing Fu; Pheng-Ann Heng"
url: "https://arxiv.org/abs/2502.20780"
external_pdf: "https://arxiv.org/pdf/2502.20780.pdf"
national_ethnic_cultural: N/A
cultures_nationalities_list: N/A
languages_list: 
religious_values: N/A
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
religious_values_list: N/A
mp_mft: 0
mp_schwartz: 0
mp_trolley: 0
mp_kohlberg: 0
mp_dual_process: 0
mp_intuitionist: 0
mp_dyadic: 0
mp_identity: 0
moral_psychology: N/A
newtags: 
key_contribution: "Introduced MedHallTune, a benchmark/dataset (1M pairs) to mitigate hallucinations in Medical VLMs, focusing on 'hard negatives' to teach models to say 'I don't know'."
significance: "Addresses the critical safety flaw of medical AI (fabricating tumors/symptoms), showing that specific 'honesty training' is required for high-stakes visual domains."
tags: 
pdf_extract: "PDF Extracts/2025/2025-Zhang-MedHallTune.md"
paper_summary: "Overview: MedHallTune: An Instruction-Tuning Benchmark for Mitigating Medical Hallucination in Vision-Language Models Qiao Yan1, Yuchen Yuan1, Xiaowei Hu3, Yihan Wang1, Jiaqi Xu1, Jinpeng Li1*, Chi-Wing Fu1,2,  | Methodology: goes beyond traditional hallucination detection metrics, aiming to improve the --- Page 3 --- MedHallTune 3 Fig. 2. Overview of the pipeline, demonstr | Conclusions: In this study, we introduce MedHallTune, a comprehensive dataset specifically designed to address hallucinations of vision-language models within the"
nw_confucian: 0
nw_ubuntu: 0
nw_islamic_ethics: 0
nw_buddhist: 0
nw_dharmic: 0
nw_indigenous_relational: 0
nw_buen_vivir: 0
author_country: HK
author_region: "East Asia"
author_global_north_south: Ambiguous
weird_score: 53
local_pdf: [[Lit-WS-Lit-WS-PDFs/2025/2025-Zhang-MedHallTune.pdf]]
abstract: "The increasing use of vision-language models (VLMs) in healthcare applications presents great challenges related to hallucinations, in which the models may generate seemingly plausible results that are in fact incorrect. Such hallucinations can jeopardize clinical decision making, potentially harming the diagnosis and treatments. In this work, we propose MedHallTune, a large-scale benchmark designed specifically to evaluate and mitigate hallucinations in medical VLMs."
CONF-CC: Preprint
DATE_ADDED: 20260208
LLM_assessed: "GPT-4o, Qwen, LLaVA"
DATA_URL: NA
CONFERENCE: Preprint
ethics_overall: No
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
research_topic: "AI Safety & Alignment"
is_benchmark: Yes
is_eval: Yes
is_dataset: Yes
data_description: "Benchmark for hallucination detection dataset for question answering"
data_metrics: "Not specified"
---
# MedHallTune: An Instruction-Tuning Benchmark for Mitigating Medical Hallucination in Vision-Language Models

## Metadata

**Authors:** Yan, Qiao; Yuan, Yuchen; Hu, Xiaowei; Wang, Yihan; Xu, Jiaqi; Li, Jinpeng; Fu, Chi-Wing; Heng, Pheng-Ann

**Year:** 2025

**Type:** document

## Links

- **Local PDF:** [[Lit-WS-Lit-WS-PDFs/2025/2025-Zhang-MedHallTune.pdf|Open PDF]]

- **arXiv:** https://arxiv.org/abs/2502.20780

## Abstract

This paper introduces **MedHallTune**, a large-scale instruction-tuning benchmark designed to mitigate **Hallucinations** in **Medical Vision-Language Models (VLMs)**. Recognizing that high-stakes medical AI cannot afford "plausible but incorrect" answers, the authors curated a dataset of 100,000 images and 1M instruction pairs. They benchmark existing VLMs and show that fine-tuning on MedHallTune significantly reduces hallucination rates (e.g., inventing symptoms or misidentifying anatomy) while improving zero-shot performance on downstream VQA.

### Detailed Summary
Medical VLMs often suffer from specific hallucinations: **Object Hallucination** (seeing a tumor that isn't there) or **Attribute Hallucination** (claiming a lesion is benign when it's malignant). MedHallTune tackles this by providing extensive **Negative Samples** (non-hallucination pairs) and **Hard Negatives** to train models to say "I don't know" or correctly reject false premises. The benchmark covers diverse modalities (X-ray, MRI, CT, Histopathology).

### Paper Outline
1.  **Introduction**: Risks of hallucination in clinical AI.
2.  **MedHallTune Dataset**: Construction pipeline (Data mining -> VQA generation -> Quality Control).
3.  **Metrics**: Clinical Accuracy, Relevance, Detail Level, Risk Level.
4.  **Experiments**: Benchmarking LLaVA-Med, Med-Flamingo, and general models like GPT-4V.
5.  **Results**: Fine-tuning results demonstrating the "Hallucination Tax" is lower with this dataset.
6.  **Conclusion**: Towards trustworthy Medical AI.

### Methods Summary
*   **Data Sources**: PubMed Central (PMC-VQA), PathVQA, VQA-RAD.
*   **Instruction Generation**: Using GPT-4 to generate diverse query-response pairs, including counterfactuals.
*   **Evaluation**: Both automated (LLM-based judge) and human expert verification of a subset.

### Results Summary
1.  **Baseline Failure**: General domain VLMs (like LLaVA) perform poorly on medical truthfulness, often hallucinating generic medical advice irrelevant to the specific image.
2.  **Fine-tuning Success**: Models trained on MedHallTune showed a **20-30% reduction** in hallucination rate.
3.  **Generalization**: The improvements transferred to unseen medical datasets, suggesting the model learned "caution" rather than just memorizing answers.

### Conclusions
Specific domain hallucination requires specific domain tuning. MedHallTune provides the necessary "grounding" data to make medical VLMs safer for clinical support.

### Artifact Contributions
*   **MedHallTune Dataset**: 1M+ Medical VQA pairs focused on truthfulness.
*   **Evaluation Toolkit**: Scripts for measuring clinical hallucination.

## Authors

[[Qiao Yan]], [[Yuchen Yuan]], [[Xiaowei Hu]], [[Yihan Wang]], [[Jiaqi Xu]], [[Jinpeng Li]], [[Chi-Wing Fu]], [[Pheng-Ann Heng]]

## Data Description

MedHallTune: a large-scale medical vision-language instruction-tuning benchmark with 100,000+ images and 1,000,000+ instruction pairs (hallucination and non-hallucination samples) sourced from PubMed, with four new clinical evaluation metrics. Dataset URL not yet public (abstract states 'will be available at MedHallTune').


## Notes


## Citation Info

3 citations (Semantic Scholar/arXiv) [2025-08-27] _eprint: 2502.20780
