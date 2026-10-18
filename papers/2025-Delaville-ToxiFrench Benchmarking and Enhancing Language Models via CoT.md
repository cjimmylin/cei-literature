---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0429
type: preprint
short_title: "ToxiFrench: Benchmarking and Enhancing Language Models via CoT Fine-Tuning for French Toxicity Detection"
year: 2025
first_author: "[[Axel Delaville]]"
last_author: "[[Axel Delaville]]"
authors: "Axel Delaville"
authors_incomplete: false
url: "https://arxiv.org/abs/2508.11281"
external_pdf: "https://arxiv.org/pdf/2508.11281.pdf"
publication: arXiv
CONF-CC: Preprint
pdf_extract: "PDF Extracts/2025/2025-Delaville-ToxiFrench Benchmarking and Enhancing Language Models via CoT.md"
local_pdf: "[[Lit-WS-PDFs/2025/2025-Delaville-ToxiFrench Benchmarking and Enhancing Language Models via CoT.pdf]]"
DATE_ADDED: 20260213
national_ethnic_cultural: French
cultures_nationalities_list: French
languages_list: French
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
LLM_assessed: "BERT, DeepSeek, GPT-4o, GPT-4o mini, Gemini, Mistral, Qwen, Qwen-2"
DATA_URL: "https://huggingface.co/datasets/AxelDlv00/ToxiFrench"
tags: 
abstract: "Detecting toxic content using language models is crucial yet challenging. While substantial progress has been made in English, toxicity detection in French remains underdeveloped, primarily due to the lack of culturally relevant, human-annotated, large-scale datasets. In this work, we release TOXIFRENCH, a dataset of 53,622 French online comments together with a balanced benchmark split for systematic evaluation."
CONFERENCE: Preprint
ethics_overall: 100
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
research_topic: "Machine Learning"
ethics_perspective: "Toxicity & Hate Speech"
nw_confucian: 0
nw_ubuntu: 0
nw_islamic_ethics: 0
nw_buddhist: 0
nw_dharmic: 0
nw_indigenous_relational: 0
nw_buen_vivir: 0
author_country: US
author_region: "North America"
author_global_north_south: "Global North"
weird_score: 78
is_benchmark: Yes
is_eval: Yes
is_dataset: Yes
data_description: "Benchmark dataset for toxicity detection"
data_metrics: "Not specified"
---
# ToxiFrench: Benchmarking and Enhancing Language Models via CoT Fine-Tuning for French Toxicity Detection

## Authors

[[Delaville]], [[Axel]]

## Metadata

**Authors:** Axel Delaville, et al.

**Year:** 2025

**Type:** preprint

**Venue:** arXiv

**Languages:** French

**Benchmark:** ToxiFrench

## Links

- **arXiv:** https://arxiv.org/abs/2508.11281
- **Code/Data:** https://huggingface.co/datasets/AxelDlv00/ToxiFrench

## Abstract

Dataset of 53,622 native French online comments with a balanced benchmark split for systematic evaluation of toxicity detection. Constructed via semi-automated annotation pipeline reducing manual labeling to 10%. Largest high-quality public French toxicity dataset with Chain-of-Thought explanations for every label.

## Summary

This paper releases ToxiFrench, a dataset of 53,622 native French online comments for toxicity detection, constructed via a semi-automated annotation pipeline that reduces manual labeling to only 10% while maintaining statistical alignment with human-only annotation. The authors benchmark SLMs, BERT-style models, commercial APIs, and LLMs, revealing that small language models often surpass larger ones in robustness. They propose a novel Chain-of-Thought fine-tuning strategy with Dynamic Weighted Loss, achieving state-of-the-art performance with a fine-tuned Qwen3-4B model that outperforms GPT-4o and DeepSeek-R1 on their benchmark.

## Data Description

Releases ToxiFrench, a dataset of 53,622 native French online comments with binary toxicity labels and Chain-of-Thought explanations, constructed via a semi-automated pipeline combining GPT-4o-mini pre-annotation and human verification, making it the largest high-quality public French toxicity dataset.


## Detailed Summary

This paper addresses the underdevelopment of French toxicity detection by releasing ToxiFrench, a dataset of 53,622 native French online comments with a balanced benchmark split for systematic evaluation. Unlike prior French toxicity resources that translate English benchmarks or rely on automated annotation, ToxiFrench is culturally grounded in French discourse and validated against human annotation. The dataset is constructed via a semi-automated annotation pipeline combining LLM-based pre-annotation with human verification, reducing manual labeling effort to only 10% while achieving near-perfect statistical alignment with human-only annotation.

The authors conduct a comprehensive evaluation spanning open-source small language models (SLMs), BERT-style models, commercial moderation APIs, and large language models. A counterintuitive finding emerges: SLMs often surpass larger models in robustness and generalization on French toxicity detection. Motivated by this, the authors propose a novel Chain-of-Thought (CoT) fine-tuning strategy using a Dynamic Weighted Loss (DWL) that progressively emphasizes the model's final decision over intermediate reasoning, significantly improving faithfulness. The fine-tuned Qwen3-4B model achieves state-of-the-art performance with 87% balanced accuracy, improving 10% over its baseline and outperforming GPT-4o and DeepSeek-R1 on the benchmark while retaining cross-lingual capabilities.

## Paper Outline

1. Introduction - Motivation for French toxicity detection and SLM focus
2. Related Work - Existing French toxicity resources and benchmarks
3. ToxiFrench Dataset - Semi-automated annotation pipeline and dataset construction
4. Benchmark Evaluation - Comprehensive model comparison
5. Chain-of-Thought Fine-Tuning - DWL strategy and faithfulness improvement
6. Results and Analysis - Performance comparison and ablation studies
7. Conclusion

## Methods Summary

The dataset construction uses a semi-automated pipeline: high-confidence LLM-based pre-annotation filters the bulk of data, with human annotators verifying and labeling the remaining 10%. The benchmark evaluation covers SLMs, BERT-style models (CamemBERT), commercial moderation APIs, and LLMs (GPT-4o, Gemini-2.5, DeepSeek-R1). The CoT fine-tuning strategy employs a Dynamic Weighted Loss function that progressively shifts emphasis from reasoning chains to final classification decisions during training. The fine-tuned model (Qwen3-4B) is evaluated on both the ToxiFrench benchmark and external cross-lingual benchmarks. Performance saturates around 85% accuracy, consistent with the upper bound imposed by human inter-annotator agreement.

## Results Summary

The fine-tuned Qwen3-4B achieves 87% balanced accuracy, the best result on the benchmark, improving 10% over its baseline. It outperforms much larger models including GPT-4o (76% F1) and Gemini-2.5-flash on the ToxiFrench benchmark. SLMs demonstrate surprising competitiveness against larger models in French toxicity detection. The Dynamic Weighted Loss improves CoT faithfulness, ensuring reasoning chains better support final decisions. Cross-lingual evaluation confirms the fine-tuned model retains capabilities across languages. Performance saturation around 85% accuracy aligns with human inter-annotator agreement limits for this task.

## Conclusions

The study demonstrates that small, fine-tuned models can outperform large commercial models for French toxicity detection when trained on culturally appropriate data. Limitations include the focus on binary toxic/non-toxic classification and the fact that different benchmarks use different toxicity definitions, making cross-benchmark comparison challenging. Future work includes extending to multi-label toxicity categorization, exploring the methodology's applicability to other low-resource languages, and improving the ecological sustainability of model training.

## Artifact Contributions

- **ToxiFrench Dataset**: 53,622 native French online comments with balanced benchmark split (https://huggingface.co/datasets/AxelDlv00/ToxiFrench)
- **ToxiFrench Code**: Training and evaluation code (available on GitHub)
- **Fine-tuned Models**: CoT-finetuned Qwen3-4B models (available on HuggingFace)

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B6
**Relevance:** Largest French toxicity dataset. Benchmarks SLMs, BERT-style models, commercial moderation APIs, and LLMs. Finds small language models often surpass larger ones in robustness.

## Tags

