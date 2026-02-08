---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: NZ2X7KAI
type: conferencePaper
short_title: CVC
year: 2025
first_author: "[[Ping Wu]]"
authors: "[[Wu, Ping]]; [[Shen, Guobin]]; [[Zhao, Dongcheng]]; [[Wang, Yuwei]]; [[Dong, Yiting]]; [[Shi, Yu]]; [[Lu, Enmeng]]; [[Zhao, Feifei]]; [[Zeng, Yi]]"
doi: 10.48550/arXiv.2506.01495
tags: 
url: "http://arxiv.org/abs/2506.01495"
local_pdf: [[PDFs/2025/2025-Wu-CVC.pdf]]
external_pdf: "http://arxiv.org/pdf/2506.01495.pdf"
publication: arXiv.org
national_ethnic_cultural: Chinese
religious_values: N/A
moral_psychology: N/A
newtags: "Chinese, Deontology"
key_contribution: "Constructs the 'Chinese Values Corpus' (CVC) with 250k value rules based on a hierarchical framework of core Chinese values"
significance: "Addresses western cultural bias by providing a large-scale, culturally adaptive benchmark for Chinese value alignment"
pdf_extract: "PDF Extracts/2025/2025-Wu-CVC.md"
abstract: "Ensuring that Large Language Models (LLMs) align with mainstream human val- ues and ethical norms is crucial for the safe and sustainable development of AI. Current value evaluation and alignment are constrained by Western cultural bias and incomplete domestic frameworks reliant on non-native rules; furthermore, the lack of scalable, rule-driven scenario generation methods makes evaluations costly and inadequate across diverse cultural contexts. To address these challenges, we propose a hierarch"
paper_summary: "Abstract: Ensuring that Large Language Models (LLMs) align with mainstream human val- ues and ethical norms is crucial for the safe and sustainable development of AI. Current value evaluation and alignment are  | Overview: C-VARC: A Large-Scale Chinese Value Rule Corpus for Value Alignment of Large Language Models Ping Wu1,4,†, Guobin Shen1,4,†, Dongcheng Zhao2,3,5,†, Yuwei Wang5,† Yiting Dong1,4, Yu Shi4, Enmeng Lu2,3, | Key Findings: In ethics and moral psychology, moral dilemmas entail decisions between competing obligations, each involving the compromise of certain values[46]. Th"
ethics_overall: No
virtue_ethics: No
deontological_ethics: Yes
utilitarian_ethics: No
is_benchmark: Yes
is_eval: Yes
is_dataset: Yes
data_description: "Benchmark for moral/ethical reasoning text corpus"
data_metrics: "Not specified"
---
 CVC: A Large-Scale Chinese Value Rule Corpus for Value Alignment of Large Language Models

## Authors

[[Ping Wu]], [[Guobin Shen]], [[Dongcheng Zhao]], [[Yuwei Wang]], [[Yiting Dong]], [[Yu Shi]], [[Enmeng Lu]], [[Feifei Zhao]], [[Yi Zeng]]
## Metadata

**Authors:** Wu, Ping; Shen, Guobin; Zhao, Dongcheng; Wang, Yuwei; Dong, Yiting; Shi, Yu; Lu, Enmeng; Zhao, Feifei; Zeng, Yi

**Year:** 2025

**Type:** preprint

**DOI:** [10.48550/arXiv.2506.01495](https://doi.org/10.48550/arXiv.2506.01495)

**Publisher:** arXiv

## Links

- **Local PDF:** [[PDFs/2025/2025-Wu-CVC.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2506.01495
- **DOI:** https://doi.org/10.48550/arXiv.2506.01495

## Detailed Summary

This paper introduces **C-VARC**, a large-scale **Chinese Value Rule Corpus** designed to evaluate and align Large Language Models with Chinese-specific ethical norms and cultural values. The authors argue that current alignment benchmarks are heavily biased toward Western cultural contexts and lack scalable, native frameworks.

C-VARC consists of over 1,200 unique value rules extracted from diverse Chinese sources. The paper presents a methodology for rule extraction and classification, followed by a benchmarking study of leading LLMs to assess their adherence to these rules.

## Paper Outline

1.  **Introduction**: Cultural bias in AI alignment; the need for native Chinese value frameworks.
2.  **Dataset Construction**:
    *   **Rule Extraction**: Using Qwen2.5-72B to extract rules from people's daily lives and online discussions.
    *   **Quality Control**: Manual annotation by experts in AI and philosophy.
3.  **Benchmark Study**: Evaluating 16 models on rule adherence.
4.  **Results**: Comparison of proprietary and open-source models.
5.  **Conclusion**: Importance of cultural context in safe AI development.

## Methods Summary

The authors collected a massive corpus of scenarios from sources like People Daily, Zhihu, and the Chinese Moral Sentence Dataset. They used **Qwen2.5-72B** to extract structured "Value Rules" (Action + Judgment) from these scenarios. A team of 45 annotators (AI/Philosophy backgrounds) then verified these rules for cultural accuracy and semantic completeness. The benchmark uses these rules as "ground truth" to evaluate LLM responses to ambiguous scenarios.

## Results Summary

1.  **Model Performance**: High-tier models like GPT-4o and Qwen2.5-72B show high agreement with human-annotated Chinese value rules, but significant gaps remain in handling complex, traditional Chinese moral dilemmas.
2.  **Extraction Efficiency**: Qwen2.5-72B was found to be more efficient than DeepSeek-V3 or GPT-4o at capturing subtle Chinese value nuances during the initial extraction phase.
3.  **Data Diversity**: The corpus covers a wide range of social, legal, and interpersonal values, from "respecting elders" to "combating transnational crime."

## Conclusions

Alignment is not a universally identical task; it requires culturally grounded datasets. **C-VARC** provides a critical resource for creating AI systems that are safe and effective within the Chinese linguistic and cultural sphere. The authors advocate for more "native" rule-driven alignment methods to replace generic, translated frameworks.

## Artifact Contributions

*   **C-VARC Dataset**: 1,200+ verified Chinese Value Rules.
*   **Rule Extraction Protocol**: A prompt-based methodology for extracting structured norms from unstructured text.


## Abstract

Ensuring that Large Language Models (LLMs) align with mainstream human values and ethical norms is crucial for the safe and sustainable development of AI. Current value evaluation and alignment are constrained by Western cultural bias and incomplete domestic frameworks reliant on non-native rules; furthermore, the lack of scalable, rule-driven scenario generation methods makes evaluations costly and inadequate across diverse cultural contexts. To address these challenges, we propose a hierarchical value framework grounded in core Chinese values, encompassing three main dimensions, 12 core values, and 50 derived values. Based on this framework, we construct a large-scale Chinese Value Rule Corpus (C-VARC) containing over 250,000 value rules enhanced and expanded through human annotation. Experimental results demonstrate that scenarios guided by C-VARC exhibit clearer value boundaries and greater content diversity compared to those produced through direct generation. In the evaluation across six sensitive themes (e.g., surrogacy, suicide), seven mainstream LLMs preferred C-VARC generated options in over 70.5% of cases, while five Chinese human annotators showed an 87.5% alignment with C-VARC, confirming its universality, cultural relevance, and strong alignment with Chinese values. Additionally, we construct 400,000 rule-based moral dilemma scenarios that objectively capture nuanced distinctions in conflicting value prioritization across 17 LLMs. Our work establishes a culturally-adaptive benchmarking framework for comprehensive value evaluation and alignment, representing Chinese characteristics.

## Notes


## Tags

#Computer-Science---Computation-and-Language

## Citation Info

1 citations (Semantic Scholar/DOI) [2025-08-27] 1 citations (Semantic Scholar/DOI) [2025-08-23]
