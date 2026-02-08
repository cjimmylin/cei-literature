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
authors: "Qiao Yan; Yuchen Yuan; Xiaowei Hu; Yihan Wang; Jiaqi Xu; Jinpeng Li; Chi-Wing Fu; Pheng-Ann Heng"
url: "https://arxiv.org/abs/2502.20780"
external_pdf: "https://arxiv.org/pdf/2502.20780.pdf"
national_ethnic_cultural: N/A
religious_values: N/A
moral_psychology: N/A
newtags: 
key_contribution: "Introduced MedHallTune, a benchmark/dataset (1M pairs) to mitigate hallucinations in Medical VLMs, focusing on 'hard negatives' to teach models to say 'I don't know'."
significance: "Addresses the critical safety flaw of medical AI (fabricating tumors/symptoms), showing that specific 'honesty training' is required for high-stakes visual domains."
tags: 
pdf_extract: "PDF Extracts/2025/2025-Zhang-MedHallTune.md"
paper_summary: "Overview: MedHallTune: An Instruction-Tuning Benchmark for Mitigating Medical Hallucination in Vision-Language Models Qiao Yan1, Yuchen Yuan1, Xiaowei Hu3, Yihan Wang1, Jiaqi Xu1, Jinpeng Li1*, Chi-Wing Fu1,2,  | Methodology: goes beyond traditional hallucination detection metrics, aiming to improve the --- Page 3 --- MedHallTune 3 Fig. 2. Overview of the pipeline, demonstr | Conclusions: In this study, we introduce MedHallTune, a comprehensive dataset specifically designed to address hallucinations of vision-language models within the"
local_pdf: [[PDFs/2025/2025-Zhang-MedHallTune.pdf]]
abstract: "The increasing use of vision-language models (VLMs) in healthcare applications presents great challenges related to hallucinations, in which the models may generate seemingly plausible results that are in fact incorrect. Such hallucinations can jeopardize clinical decision making, potentially harming the diagnosis and treatments. In this work, we propose MedHallTune, a large-scale benchmark designed specifically to evaluate and mitigate hallucinations in medical VLMs. Comprising over 100,000 images and 1,000,000 instruction pairs, MedHallTune includes both hallucination and non-hallucination samples, each with ground-truth annotations. We conduct a comprehensive evaluation of current medical and general VLMs using MedHallTune, assessing their performance across key metrics, including clinical accuracy, relevance, detail level, and risk level. The experimental results show that fine-tuning with MedHallTune successfully improves the ability of several existing models to manage hallucinations and boost their zero-shot performance on downstream visual-question-answering (VQA) tasks, making them more reliable for practical medical applications. Our work contributes to the development of more trustworthy VLMs. Codes and dataset will be available at \href{https://github.com/russellyq/MedHallTune}{MedHallTune}."
ethics_overall: No
virtue_ethics: No
deontological_ethics: No
utilitarian_ethics: No
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

- **Local PDF:** [[PDFs/2025/2025-Zhang-MedHallTune.pdf|Open PDF]]

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

## Notes


## Citation Info

3 citations (Semantic Scholar/arXiv) [2025-08-27] _eprint: 2502.20780
