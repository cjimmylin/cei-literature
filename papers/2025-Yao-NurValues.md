---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: D8YG9EGA
type: conferencePaper
short_title: NurValues
year: 2025
first_author: "[[Ben Yao]]"
last_author: "[[Jing Qin]]"
authors: "Ben Yao; Qiuchi Li; Yazhou Zhang; Siyu Yang; Bohan Zhang; Prayag Tiwari; Jing Qin"
doi: 10.48550/arXiv.2505.08734
tags: 
url: "http://arxiv.org/abs/2505.08734"
external_pdf: "http://arxiv.org/pdf/2505.08734.pdf"
publication: arXiv.org
national_ethnic_cultural: N/A
religious_values: N/A
religious_values_list: N/A
moral_psychology: N/A
newtags: "Applied Ethics"
key_contribution: "Created NurValues, a benchmark for *nursing* value alignment with 1,100 clinical cases annotated for specialized values (Altruism, Dignity, Justice)."
significance: "Shows that general 'medical LLMs' often fail on professional ethics (e.g., patient dignity), underscoring the need for domain-specific value alignment beyond generic 'helpfulness'."
pdf_extract: "PDF Extracts/2025/2025-Yao-NurValues.md"
abstract: "This work introduces the first benchmark for nursing value alignment, consisting of five core value dimensions distilled from international nursing codes: Altruism, Human Dignity, Integrity, Justice, and Professionalism. The benchmark com- prises 1,100 real-world nursing behavior instances collected through a five-month longitudinal field study across three hospitals of varying tiers. These instances are annotated by five clinical nurses and then augmented with LLM-generated counterfactuals with"
paper_summary: "Abstract: This work introduces the first benchmark for nursing value alignment, consisting of five core value dimensions distilled from international nursing codes: Altruism, Human Dignity, Integrity, Justice,  | Overview: arXiv:2505.08734v1 [cs.CL] 13 May 2025 NurValues: Real-World Nursing Values Evaluation for Large Language Models in Clinical Context Ben Yao1, Qiuchi Li2, Yazhou Zhang3∗, Siyu Yang4, Bohan Zhang1, Pra | Methodology: in 15, while the underline font indicates the second-best result. Dataset Model 0-Shot 2-Shot 6-Shot 10-Shot Acc. Ma-F1 Acc. Ma-F1 Acc. Ma-F1 Acc. Ma- | Key Findings: confirms that the rewritten dialogues retain high topical consistency with the original instances. Using three SoTA LLMs to score semantic similarity, | Conclusions: In this paper, we introduce NurValues, the first real-world healthcare benchmark for evaluating LLMs’ nursing values. Built from 1,100 real-world nurs"
local_pdf: [[PDFs/2025/2025-Yao-NurValues.pdf]]
ethics_overall: No
virtue_ethics: No
deontological_ethics: No
utilitarian_ethics: No
ethics_perspective: "Applied Ethics"
is_benchmark: Yes
is_eval: Yes
is_dataset: Yes
data_description: "Benchmark annotated dataset for conversational ai"
data_metrics: "Not specified"
LLM_assessed: "GPT-4o, o1, Claude, Gemini, DeepSeek, Llama-3, Llama, Qwen"
DATA_URL: "https://huggingface.co/datasets/Ben012345/NurValues"
---
# NurValues: Real-World Nursing Values Evaluation for Large Language Models in Clinical Context

## Metadata

**Authors:** Yao, Ben; Li, Qiuchi; Zhang, Yazhou; Yang, Siyu; Zhang, Bohan; Tiwari, Prayag; Qin, Jing

**Year:** 2025

**Type:** preprint

**DOI:** [10.48550/arXiv.2505.08734](https://doi.org/10.48550/arXiv.2505.08734)

**Publisher:** arXiv

## Links

- **Local PDF:** [[PDFs/2025/2025-Yao-NurValues.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2505.08734
- **DOI:** https://doi.org/10.48550/arXiv.2505.08734

## Abstract

This work introduces the first benchmark for nursing value alignment, consisting of five core value dimensions distilled from international nursing codes: Altruism, Human Dignity, Integrity, Justice, and Professionalism. The benchmark comprises 1,100 real-world nursing behavior instances collected through a five-month longitudinal field study across three hospitals of varying tiers. These instances are annotated by five clinical nurses and then augmented with LLM-generated counterfactuals with reversed ethic polarity. Each original case is paired with a value-aligned and a value-violating version, resulting in 2,200 labeled instances that constitute the Easy-Level dataset. To increase adversarial complexity, each instance is further transformed into a dialogue-based format that embeds contextual cues and subtle misleading signals, yielding a Hard-Level dataset. We evaluate 23 state-of-the-art (SoTA) LLMs on their alignment with nursing values. Our findings reveal three key insights: (1) DeepSeek-V3 achieves the highest performance on the Easy-Level dataset (94.55), where Claude 3.5 Sonnet outperforms other models on the Hard-Level dataset (89.43), significantly surpassing the medical LLMs; (2) Justice is consistently the most difficult nursing value dimension to evaluate; and (3) in-context learning significantly improves alignment. This work aims to provide a foundation for value-sensitive LLMs development in clinical settings2.

## Authors

[[Ben Yao]], [[Qiuchi Li]], [[Yazhou Zhang]], [[Siyu Yang]], [[Bohan Zhang]], [[Prayag Tiwari]], [[Jing Qin]]

## Data Description

NurValues is the first real-world nursing value alignment benchmark consisting of 4,400 instances across five core nursing value dimensions (Altruism, Human Dignity, Integrity, Justice, Professionalism). It includes 2,200 Easy-Level instances from a five-month longitudinal field study across three hospitals, paired with counterfactual augmented samples, and 2,200 Hard-Level dialogue-based instances with adversarial complexity. Twenty-three state-of-the-art LLMs were evaluated including 18 general LLMs (Claude 3.5/3.7 Sonnet, GPT-4o, o1, DeepSeek-V3/R1, Gemini-2.5-Pro, Llama-3/3.1/3.3/4 variants, Qwen 2.5 variants) and 5 medical LLMs.


## Notes


## Tags

#Computer-Science---Computation-and-Language

## Citation Info

9 citations (Semantic Scholar/DOI) [2025-08-27] 0 citations (Semantic Scholar/DOI) [2025-08-23]
