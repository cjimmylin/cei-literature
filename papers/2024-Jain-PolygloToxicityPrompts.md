---






































Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: F8GJ6DLS
type: conferencePaper
short_title: PolygloToxicityPrompts
year: 2024
first_author: "[[Devansh Jain]]"
last_author: "[[Maarten Sap]]"
authors: "Devansh Jain; Priyanshu Kumar; Samuel Gehman; Xuhui Zhou; Thomas Hartvigsen; Maarten Sap"
doi: 10.48550/arXiv.2405.09373
tags: 
url: "http://arxiv.org/abs/2405.09373"
external_pdf: "http://arxiv.org/pdf/2405.09373.pdf"
publication: arXiv.org
CONF-CC: "Preprint"
national_ethnic_cultural: "Multicultural/Cross-cultural"
cultures_nationalities_list: "Multicultural/Cross-cultural"
languages_list: "Multilingual"
religious_values: "Multiple Religions"
rv_islam: 0
rv_christianity: 50
rv_buddhism: 0
rv_judaism: 0
rv_hinduism: 0
rv_sikhism: 0
rv_confucianism: 0
rv_taoism: 0
rv_shinto: 0
rv_jainism: 50
rv_bahai: 0
rv_zoroastrianism: 0
rv_ubuntu: 0
rv_indigenous: 0
religious_values_list: "Christianity, Jainism"
mp_mft: 0
mp_schwartz: 0
mp_trolley: 0
mp_kohlberg: 0
mp_dual_process: 0
mp_intuitionist: 0
mp_dyadic: 0
mp_identity: 0
moral_psychology: "N/A"
newtags: "Toxicity & Hate Speech"
key_contribution: "Released PTP, a dataset of 425k naturally occurring toxic prompts across 17 languages, derived from a 100M document crawl."
significance: "Addressing the 'English-centricity' of toxicity evaluation, finding that toxicity generation is worse in lower-resource languages and that standard safety tuning often fails to generalize multilingually."
pdf_extract: "PDF Extracts/2024/2024-Jain-PolygloToxicityPrompts.md"
abstract: "Recent advances in large language models (LLMs) have led to their extensive global deployment, and ensuring their safety calls for comprehensive and multilingual toxicity evaluations. However, existing toxicity benchmarks are overwhelmingly focused on English, posing serious risks to deploying LLMs in other languages. We address this by introducing POLYGLOTOXICITYPROMPTS (PTP), the first large-scale multilingual toxicity evaluation benchmark of 425K naturally occurring prompts spanning 17..."
paper_summary: "Abstract: Recent advances in large language models (LLMs) have led to their exten- sive global deployment, and ensuring their safety calls for comprehensive and multilingual toxicity evaluations. However, exist | Overview: Published as a conference paper at COLM 2024 PolygloToxicityPrompts : Multilingual Evaluation of Neural Toxic Degeneration in Large Language Models Warning: this paper discusses content that some may  | Methodology: does not have any significant impact. Our findings shed light on crucial shortcomings of LLM safeguarding and highlight areas for future research. Cod | Key Findings: framework for automated red teaming and robust refusal. arXiv preprint arXiv:2402.04249, 2024. Niklas Muennighoff, Thomas Wang, Lintang Sutawika, Adam | Conclusions: We present POLYGLOTOXICITYPROMPTS, the first large-scale multilingual benchmark of 425K naturally occurring prompts across 17 languages for evaluating"
local_pdf: "[[PDFs/2024/2024-Jain-PolygloToxicityPrompts.pdf]]"
DATE_ADDED: 20260208
LLM_assessed: "BLOOM, GPT-3.5, Llama-2, Mistral, Qwen"
DATA_URL: "https://huggingface.co/datasets/ToxicityPrompts/PolygloToxicityPrompts"
CONFERENCE: "Other Conference"
ethics_overall: 100
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: Yes
data_description: "Multilingual benchmark for ai safety"
data_metrics: "17 languages"
ethics_perspective: "Toxicity & Hate Speech"
---
# PolygloToxicityPrompts: Multilingual Evaluation of Neural Toxic Degeneration in Large Language Models

## Metadata

**Authors:** Jain, Devansh; Kumar, Priyanshu; Gehman, Samuel; Zhou, Xuhui; Hartvigsen, Thomas; Sap, Maarten

**Year:** 2024

**Type:** preprint

**DOI:** [10.48550/arXiv.2405.09373](https://doi.org/10.48550/arXiv.2405.09373)

**Publisher:** arXiv

## Links

- **Local PDF:** [[PDFs/2024/2024-Jain-PolygloToxicityPrompts.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2405.09373
- **DOI:** https://doi.org/10.48550/arXiv.2405.09373

## Abstract

Recent advances in large language models (LLMs) have led to their extensive global deployment, and ensuring their safety calls for comprehensive and multilingual toxicity evaluations. However, existing toxicity benchmarks are overwhelmingly focused on English, posing serious risks to deploying LLMs in other languages. We address this by introducing POLYGLOTOXICITYPROMPTS (PTP), the first large-scale multilingual toxicity evaluation benchmark of 425K naturally occurring prompts spanning 17 languages. We overcome the scarcity of naturally occurring toxicity in web-text and ensure coverage across languages with varying resources by automatically scraping over 100M web-text documents. Using PTP, we investigate research questions to study the impact of model size, prompt language, and instruction and preference-tuning methods on toxicity by benchmarking over 60 LLMs. Notably, we find that toxicity increases as language resources decrease or model size increases. Although instruction- and preference-tuning reduce toxicity, the choice of preference-tuning method does not have any significant impact. Our findings shed light on crucial shortcomings of LLM safeguarding and highlight areas for future research.

## Authors

[[Devansh Jain]], [[Priyanshu Kumar]], [[Samuel Gehman]], [[Xuhui Zhou]], [[Thomas Hartvigsen]], [[Maarten Sap]]

## Data Description

Large-scale multilingual toxicity evaluation benchmark of 425K naturally occurring prompts spanning 17 languages, with 62 LLMs benchmarked for toxic degeneration across model sizes and alignment methods.


## Notes


## Tags

#Computer-Science---Computation-and-Language

## Citation Info

11 citations (Semantic Scholar/DOI) [2025-08-27] 11 citations (Semantic Scholar/arXiv) [2025-08-27] arXiv:2405.09373 [cs]
