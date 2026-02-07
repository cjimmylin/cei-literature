---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: ZSG87J24
type: conferencePaper
short_title: IndoPref
year: 2025
first_author: "[[Vanessa Rebecca Wiyono]]"
authors: "Vanessa Rebecca Wiyono; David Anugraha; Ayu Purwarianti; Genta Indra Winata"
doi: 10.48550/arXiv.2507.22159
url: "http://arxiv.org/abs/2507.22159"
external_pdf: "http://arxiv.org/pdf/2507.22159.pdf"
publication: arXiv.org
research_topic: "Machine Learning"
national_ethnic_cultural: Indonesian
religious_values: N/A
moral_psychology: N/A
newtags: Indonesian
tags: 
pdf_extract: "PDF Extracts/2025-Wiyono-IndoPref.md"
abstract: "Over 200 million people speak Indonesian, yet the language remains significantly underrepre- sented in preference-based research for large language models (LLMs). Most existing multi- lingual datasets are derived from English trans- lations, often resulting in content that lacks cul- tural and linguistic authenticity. To address this gap, we introduce INDOPREF, the first fully human-authored and multi-domain Indonesian preference dataset designed to evaluate the nat- uralness and quality of LLM-"
paper_summary: "Abstract: Over 200 million people speak Indonesian, yet the language remains significantly underrepre- sented in preference-based research for large language models (LLMs). Most existing multi- lingual datasets | Overview: INDOPREF: A Multi-Domain Pairwise Preference Dataset for Indonesian Vanessa Rebecca Wiyono1*, David Anugraha2∗, Ayu Purwarianti1, Genta Indra Winata3 1Institut Teknologi Bandung 2Stanford University 3 | Key Findings: A.2 Indonesian Template Pairwise evaluation prompt template Evaluasi respons berdasarkan tugas, ma- sukan, respons, dan rubrik evaluasi yang diberikan | Conclusions: This paper introduces INDOPREF, a new bench- mark for evaluating LLMs on Indonesian-language preference tasks using fully human-authored data. By focu"
local_pdf: [[PDFs/2025-Wiyono-IndoPref.pdf]]
key_contribution: "Introduces IndoPref, the first fully human-authored, multi-domain pairwise preference dataset for the Indonesian language, containing 522 prompts and 4,099 human-annotated preferences."
significance: "Addresses the 'Translation-ese' problem in multilingual LLM evaluation by providing a native-authored gold standard that captures Indonesian cultural and linguistic authenticity, revealing critical performance gaps in English-centric models."
ethics_overall: No
virtue_ethics: No
deontological_ethics: No
utilitarian_ethics: No
ethics_perspective: "Social & Cultural Values"
is_benchmark: Yes
is_eval: Yes
is_dataset: Yes
data_description: "Multilingual benchmark annotated dataset"
data_metrics: "522 prompts; 10 categories"
---
# IndoPref: A Multi-Domain Pairwise Preference Dataset for Indonesian

## Metadata

**Authors:** Wiyono, Vanessa Rebecca; Anugraha, David; Purwarianti, Ayu; Winata, Genta Indra

**Year:** 2025

**Type:** preprint

**DOI:** [10.48550/arXiv.2507.22159](https://doi.org/10.48550/arXiv.2507.22159)

**Publisher:** arXiv

## Links

- **Local PDF:** [[PDFs/2025-Wiyono-IndoPref.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2507.22159
- **DOI:** https://doi.org/10.48550/arXiv.2507.22159

## Abstract

This paper introduces **IndoPref**, the first fully human-authored, multi-domain preference dataset for the **Indonesian language**. Addressing the underrepresentation of Indonesian in LLM research (despite 200M+ speakers), the authors created a dataset of 522 prompts and 4,099 pairwise preferences annotated by native speakers. The study benchmarks five instruction-tuned LLMs, revealing that while English-centric models often fail to capture cultural nuances, models fine-tuned on IndoPref show improved "naturalness" and alignment with Indonesian cultural values.

### Detailed Summary
Most multilingual datasets are "Translation-ese"—direct translations from English that miss local idioms and cultural context. IndoPref bridges this gap by employing native Indonesian annotators to write prompts from scratch across 10 domains (e.g., creative writing, STEM, humanities). The authors then generated responses using various LLMs and had humans rank them. The resulting dataset provides a high-quality "Gold Standard" for evaluating how well AI models understand not just the Indonesian language, but the Indonesian *user*.

### Paper Outline
1.  **Introduction**: The scarcity of non-English preference data and the "Translation-ese" problem.
2.  **Related Work**: Existing multilingual benchmarks (often translated) vs. native datasets.
3.  **IndoPref Construction**: Methodology for prompt creation, response generation, and human annotation (max-diff scaling).
4.  **Experiments**: Benchmarking 5 LLMs (proprietary and open) on the dataset.
5.  **Analysis**: Error analysis showing common failure modes (e.g., formal vs. informal register mismatch).
6.  **Conclusion**: The importance of culturally grounded evaluation.

### Methods Summary
*   **Dataset Creation**: 522 native Prompts across 10 categories.
*   **Response Generation**: Responses generated by 5 models (e.g., GPT-4, Llama 2, local Indonesian finetunes).
*   **Annotation**: Native speakers ranked pairs. High Inter-Annotator Agreement (Krippendorff's alpha > 0.4, considered good for preference data).
*   **Metrics**: Win-rate against 'text-davinci-003' and pairwise accuracy.

### Results Summary
1.  **Native vs. Translated**: Models trained on translated data performed significantly worse on IndoPref than on translated benchmarks, proving that translation hides competence gaps.
2.  **Model Rankings**: GPT-4 generally led, but "local" models fine-tuned on Indonesian instruction data punched above their weight in specific cultural domains.
3.  **Cultural Sensitivity**: The dataset revealed that generic models often used "Formal" Indonesian in inappropriate casual contexts (like writing a text message), which native speakers penalized heavily.

### Conclusions
Linguistic competence does not equal cultural competence. IndoPref demonstrates that to truly align AI with a specific population (Indonesians), we need alignment data rooted in their native context, not just translated instructions.

### Artifact Contributions
*   **IndoPref Dataset**: 4,099 human-annotated preferences for Indonesian text.
*   **Benchmarking Leaderboard**: Initial rankings of major LLMs on Indonesian cultural nuances.

## Authors

[[Vanessa Rebecca Wiyono]], [[David Anugraha]], [[Ayu Purwarianti]], [[Genta Indra Winata]]

## Notes


## Tags

#Computer-Science---Artificial-Intelligence #Computer-Science---Computation-and-Language

## Citation Info

18 citations (Semantic Scholar/DOI) [2025-08-27] 1 citations (Semantic Scholar/arXiv) [2025-08-27] 0 citations (Semantic Scholar/arXiv) [2025-08-23]
