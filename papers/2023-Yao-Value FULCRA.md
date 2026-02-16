---




Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: 2ZM69H7H
type: conferencePaper
short_title: "Value FULCRA"
year: 2025
first_author: "[[Jing Yao]]"
last_author: "[[Xing Xie]]"
authors: "Jing Yao; Xiaoyuan Yi; Xiting Wang; Yifan Gong; Xing Xie"
doi: 10.48550/arXiv.2311.10766
url: "http://arxiv.org/abs/2311.10766"
external_pdf: "http://arxiv.org/pdf/2311.10766.pdf"
publication: "North American Chapter of the Association for Computational Linguistics"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: ""
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "Value Pluralism / Schwartz"
newtags: "Value Pluralism / Schwartz, AI Safety & Alignment"
key_contribution: "Mapped LLM behaviors to Schwartz's Theory of Basic Values and released FULCRA, a dataset of 5k value-vector pairs for continuous value alignment."
significance: "Integrates established social psychology theory into alignment, enabling a more structured and continuous measurement of 'human values' rather than relying on binary safety labels."
tags: 
pdf_extract: "PDF Extracts/2023/2023-Yao-Value FULCRA.md"
abstract: "The rapid advancement of Large Language Models (LLMs) has attracted much attention to value alignment for their responsible development. However, how to define values in this context remains a largely unexplored question. Existing work mainly follows the Helpful, Honest, Harmless principle and specifies values as risk criteria formulated in the AI community, e.g., fairness and privacy protection, suffering from poor clarity, adaptability and transparency."
paper_summary: "Abstract: The rapid advancement of Large Language Models (LLMs) has attracted much attention to value alignment for their responsible de- velopment. However, how to define values in this context remains a large | Overview: Value FULCRA: Mapping Large Language Models to the Multidimensional Spectrum of Basic Human Values Jing Yao1, Xiaoyuan Yi1, Xiting Wang2,3, Yifan Gong1 and Xing Xie1 1Microsoft Research Asia, Beijing, | Key Findings: and alignment, showing promising results. 2 Related Work Value Alignment of LLMs With the growing popularity of LLMs, researchers strive to align LLMs | Conclusions: on more comprehensive human values. Social Value Orientation (Murphy et al., 2011; Zhang et al., 2023) addresses this gap, measuring the bal- ance bet"
local_pdf: "[[PDFs/2023/2023-Yao-Value FULCRA.pdf]]"
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "AI Safety & Alignment"
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Evaluation approach dataset"
data_metrics: "Not specified"
LLM_assessed: "GPT-4, GPT-3.5, BERT, DeBERTa, BART, OPT, Llama-2, Vicuna"
DATA_URL: "https://ValueCompass.github.io"
DATE_ADDED: 20260207
---
# Value FULCRA: Mapping Large Language Models to the Multidimensional Spectrum of Basic Human Values

## Metadata

**Authors:** Yao, Jing; Yi, Xiaoyuan; Wang, Xiting; Gong, Yifan; Xie, Xing

**Year:** 2023

**Type:** preprint

**DOI:** [10.48550/arXiv.2311.10766](https://doi.org/10.48550/arXiv.2311.10766)

**Publisher:** arXiv

## Links

- **Local PDF:** [[PDFs/2023/2023-Yao-Value FULCRA.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2311.10766
- **DOI:** https://doi.org/10.48550/arXiv.2311.10766

## Abstract

The rapid advancement of Large Language Models (LLMs) has attracted much attention to value alignment for their responsible development. However, how to define values in this context remains a largely unexplored question. Existing work mainly follows the Helpful, Honest, Harmless principle and specifies values as risk criteria formulated in the AI community, e.g., fairness and privacy protection, suffering from poor clarity, adaptability and transparency. Inspired by basic values in humanity and social science across cultures, this work proposes a novel basic value alignment paradigm and introduces a value space spanned by basic value dimensions. All LLMs’ behaviors can be mapped into the space by identifying the underlying values, possessing the potential to address the three challenges. To foster future research, we apply the representative Schwartz’s Theory of Basic Values as an initialized example and construct FULCRA, a dataset consisting of 5k (LLM output, value vector) pairs. Our extensive analysis of FULCRA reveals the underlying relation between basic values and LLMs’ behaviors, demonstrating that our approach not only covers existing mainstream risks but also anticipates possibly unidentified ones. Additionally, we present an initial implementation of the basic value evaluation and alignment, paving the way for future research in this line.

## Authors

[[Jing Yao]], [[Xiaoyuan Yi]], [[Xiting Wang]], [[Yifan Gong]], [[Xing Xie]]

## Data Description

FULCRA is a dataset of 5,000 (LLM output, value vector) pairs mapping LLM behaviors to Schwartz's Theory of Basic Values across 10 dimensions. It was constructed using a Human-GPT-4 collaborative annotation process on adversarial prompts from red teaming datasets. The paper trains basic value evaluators using BERT-large, DeBERTa-large, BART-large, OPT-1.3B, and Llama2-7B, and evaluates real-time LLM responses from GPT-3.5-Turbo, GPT-4, Llama2-7B, Llama2-13B, and Vicuna-13B.


## Notes


## Tags

#Computer-Science---Artificial-Intelligence #Computer-Science---Computation-and-Language

## Citation Info

31 citations (Semantic Scholar/DOI) [2025-08-27] 2 citations (Semantic Scholar/arXiv) [2025-08-27] 31 citations (Semantic Scholar/DOI) [2025-08-23]
