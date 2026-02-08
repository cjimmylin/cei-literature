---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: YXZ79HSK
type: document
short_title: "Benchmarking Ethics in Text-to-Image Models"
year: 2025
first_author: "[[Lijun Li]]"
authors: "Lijun Li; Zhelun Shi; Xuhao Hu; Bowen Dong; Yiran Qin; Xihui Liu; Lu Sheng; Jing Shao"
url: "https://openreview.net/forum?id=kIboeK0Wzs"
external_pdf: "file:///Users/jimmylin/Zotero/storage/BU3GIQZ6/1558_Benchmarking_Ethics_in_Te.pdf"
national_ethnic_cultural: N/A
religious_values: N/A
moral_psychology: N/A
newtags: "Bias & Fairness"
key_contribution: "Benchmarks ethics in T2I models (fairness, toxicity, privacy)."
significance: "Addresses the specific ethical modalities of image generation (e.g., visual bias, deepfakes) which differ from text-only harms."
tags: 
abstract: "Text-to-image (T2I) models have rapidly advanced, enabling the generation of high-quality images from text prompts across various domains. However, these models raise significant ethical concerns, including the risk of generating harmful, biased, or private content. Existing safety benchmarks are limited in scope, lacking comprehensive coverage of critical ethical aspects such as detailed categories of toxicity, privacy, and fairness, and often rely on inadequate evaluation techniques. To address these gaps, we introduced T2IEthics, a comprehensive benchmark that rigorously evaluates T2I models across three key ethical dimensions: fairness, toxicity, and privacy."
ethics_overall: No
virtue_ethics: No
deontological_ethics: No
utilitarian_ethics: No
ethics_perspective: "Bias & Fairness"
is_benchmark: Yes
is_eval: Yes
is_dataset: Yes
data_description: "Benchmark for moral/ethical reasoning dataset for toxicity detection"
data_metrics: "Not specified"
pdf_extract: "PDF Extracts/2024/2024-Li-Benchmarking Ethics in Text-to-Image Models.md"
local_pdf: "[[PDFs/2024/2024-Li-Benchmarking Ethics in Text-to-Image Models.pdf]]"
---
# Benchmarking Ethics in Text-to-Image Models: A Holistic Dataset and Evaluator for Fairness, Toxicity, and Privacy

## Metadata

**Authors:** Li, Lijun; Shi, Zhelun; Hu, Xuhao; Dong, Bowen; Qin, Yiran; Liu, Xihui; Sheng, Lu; Shao, Jing

**Year:** 2024

**Type:** document

## Links

- **URL:** https://openreview.net/forum?id=kIboeK0Wzs

## Abstract

Text-to-image (T2I) models have rapidly advanced, enabling the generation of high-quality images from text prompts across various domains. However, these models raise significant ethical concerns, including the risk of generating harmful, biased, or private content. Existing safety benchmarks are limited in scope, lacking comprehensive coverage of critical ethical aspects such as detailed categories of toxicity, privacy, and fairness, and often rely on inadequate evaluation techniques. To address these gaps, we introduced T2IEthics, a comprehensive benchmark that rigorously evaluates T2I models across three key ethical dimensions: fairness, toxicity, and privacy.

## Authors

[[Lijun Li]], [[Zhelun Shi]], [[Xuhao Hu]], [[Bowen Dong]], [[Yiran Qin]], [[Xihui Liu]], [[Lu Sheng]], [[Jing Shao]]

## Detailed Summary

This paper introduces T2IEthics, a comprehensive benchmark for evaluating the ethical dimensions of text-to-image (T2I) models across three critical areas: fairness, toxicity, and privacy. The authors argue that existing safety benchmarks for T2I models are limited in scope, often focusing narrowly on specific ethical aspects without providing comprehensive coverage of detailed toxicity categories, privacy concerns, or nuanced fairness dimensions. T2IEthics addresses these gaps through a hierarchical taxonomy that includes subcategories such as violence, hate, sexual content, and humiliation under toxicity; public figures, intellectual property, and personal identification documents under privacy; and race, age, and gender under fairness.

A key contribution of the paper is ImageGuard, a multimodal large language model-based evaluator designed for accurate ethical assessment of generated images. The authors demonstrate that ImageGuard significantly outperforms existing evaluation approaches including GPT-4o and CLIP-based classifiers across all ethical dimensions. The development of ImageGuard involved large-scale data collection, a cross-attention module architecture, and integration of contrastive loss during training. For fairness evaluation, the paper proposes using normalized Kullback-Leibler (KL) divergence as a metric, which provides better interpretability and allows for cross-task comparisons compared to traditional distance-based methods.

The benchmark was used to evaluate 12 diffusion models including popular models from the Stable Diffusion series. The results reveal persistent issues with racial fairness, a tendency to generate toxic content, and significant variation in privacy protection among models even when defense methods like concept erasing are employed. The evaluation also assessed the effectiveness of various concept erasing methods aimed at removing unethical content from T2I models, providing insights into their limitations and areas for improvement.

## Paper Outline

1. Introduction - Establishes the need for comprehensive ethical evaluation of T2I models
2. Related Works - Reviews existing ethical datasets and image content moderation approaches
3. Dataset - Describes T2IEthics benchmark construction across fairness, toxicity, and privacy
4. ImageGuard - Presents the MLLM-based ethical evaluator architecture and training
5. Experiments - Reports evaluation of 12 T2I models and concept erasing methods
6. Conclusion - Summarizes contributions and implications for T2I model development

## Methods Summary

The T2IEthics benchmark was constructed with high-quality, human-written prompts across diverse sources, with quality control procedures to ensure relevance and variety. The dataset covers three ethical dimensions with detailed subcategories. ImageGuard was trained using collected image-label pairs with a cross-attention module that integrates text and image features. Training incorporated contrastive loss to improve discrimination between safe and unsafe content. Evaluation metrics include safety rate for toxicity and privacy, and normalized KL divergence for fairness assessment.

## Results Summary

ImageGuard outperformed GPT-4o and CLIP-based evaluators across all ethical dimensions. Among the 12 T2I models evaluated, persistent racial fairness issues were identified across most models. Toxicity generation tendencies varied significantly between models, with some generating harmful content even from benign prompts. Privacy protection showed high variability, with intellectual property violations being particularly common. Concept erasing methods showed limited effectiveness in completely removing unethical content generation capabilities.

## Conclusions

T2IEthics provides a much-needed comprehensive ethical evaluation framework for T2I models with hierarchical taxonomy and rigorous methodology. ImageGuard offers a more accurate evaluation tool than existing approaches. The benchmark reveals that current T2I models continue to face significant challenges across fairness, toxicity, and privacy dimensions, highlighting the need for improved safety measures and alignment techniques.

## Artifact Contributions

- T2IEthics benchmark dataset with prompts for fairness, toxicity, and privacy evaluation
- ImageGuard MLLM-based ethical content evaluator
- Evaluation results for 12 T2I models
- Normalized KL divergence fairness metric

## Notes

