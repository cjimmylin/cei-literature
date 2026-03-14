---




































Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: Y644CHBP
type: conferencePaper
short_title: CASE-Bench
year: 2025
first_author: "[[Guangzhi Sun]]"
last_author: "[[Jose Such]]"
authors: "Guangzhi Sun; Xiao Zhan; Shutong Feng; Philip C. Woodland; Jose Such"
doi: 10.48550/arXiv.2501.14940
url: "http://arxiv.org/abs/2501.14940"
external_pdf: "http://arxiv.org/pdf/2501.14940.pdf"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: "English"
religious_values: "N/A"
rv_islam: 0
rv_christianity: 5
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
religious_values_list: "N/A"
mp_mft: 0
mp_schwartz: 0
mp_trolley: 0
mp_kohlberg: 0
mp_dual_process: 0
mp_intuitionist: 0
mp_dyadic: 0
mp_identity: 0
moral_psychology: "N/A"
newtags: "Value Pluralism / Schwartz, AI Safety & Alignment"
key_contribution: "Introduced CASE-Bench, a benchmark for evaluating LLM safety that explicitly incorporates context into safety assessments using Contextual Integrity theory."
significance: "Highlights that current benchmarks fail to capture context-dependent safety nuances and demonstrates that LLMs struggle with safe contexts where refusal is unnecessary, often misaligning with human judgment."
tags: 
pdf_extract: "PDF Extracts/2025/2025-Sun-CASE-Bench.md"
abstract: "Aligning large language models (LLMs) with human values is essential for their safe deployment and widespread adoption. Current LLM safety benchmarks often focus solely on the refusal of individual problematic queries, which overlooks the importance of the context where the query occurs and may cause undesired refusal of queries under safe contexts that diminish user experience. Addressing this gap, we introduce CASE-Bench, a Context-Aware SafEty Benchmark that integrates context into safety ass"
paper_summary: "Abstract: Aligning large language models (LLMs) with human values is essential for their safe deployment and widespread adoption. Current LLM safety benchmarks often focus solely on the refusal of individual pr | Overview: Preprint CASE-BENCH: CONTEXT-AWARE SAFETY BENCH- MARK FOR LARGE LANGUAGE MODELS Guangzhi Sun1∗, Xiao Zhan2∗, Shutong Feng3, Philip C. Woodland1, Jose Such2,4 Department of Engineering, University of C | Methodology: Accuracy↑ R (Safe / Unsafe) ↑ PCC ↑ BCE ↓ GPT-4o-2024-08-06 OpenAI Team (2024) Binary 77.0% 54.6% / 94.8% – – Score 78.6% 58.1% / 94.8% 67.77 | Conclusions: 6.1 CONTEXT RELIABILITY The context in CASE-Bench is assumed to be derived from verified practical mechanisms. We used various techniques to formalize"
local_pdf: "[[PDFs/2025/2025-Sun-CASE-Bench.pdf]]"
LLM_assessed: "Claude-3, GPT-4o, GPT-4o mini, Llama-3, Mixtral, Qwen-2"
DATA_URL: "https://github.com/BriansIDP/CASEBench"
publication: "ICML 2025"
CONF-CC: "ICML 2025"
DATE_ADDED: 20260207
CONFERENCE: "ICML 2025"
ethics_overall: 15
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
ethics_perspective: "AI Safety & Alignment"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: Yes
data_description: "Benchmark for ai safety"
data_metrics: "Not specified"
---
# CASE-Bench: Context-Aware SafEty Benchmark for Large Language Models

## Metadata

**Authors:** Sun, Guangzhi; Zhan, Xiao; Feng, Shutong; Woodland, Philip C.; Such, Jose

**Year:** 2025

**Type:** conferencePaper

**DOI:** [10.48550/arXiv.2501.14940](https://doi.org/10.48550/arXiv.2501.14940)

**Publisher:** arXiv

## Links

- **Local PDF:** [[PDFs/2025/2025-Sun-CASE-Bench.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2501.14940
- **DOI:** https://doi.org/10.48550/arXiv.2501.14940

## Abstract

Aligning large language models (LLMs) with human values is essential for their safe deployment and widespread adoption. Current LLM safety benchmarks often focus solely on the refusal of individual problematic queries, which overlooks the importance of the context where the query occurs and may cause undesired refusal of queries under safe contexts that diminish user experience. Addressing this gap, we introduce CASE-Bench, a Context-Aware Safety Evaluation Benchmark that integrates context into safety assessments of LLMs. CASE-Bench assigns distinct, formally described contexts to categorized queries based on Contextual Integrity theory. Additionally, in contrast to previous studies which mainly rely on majority voting from just a few annotators, we recruited a sufficient number of annotators necessary to ensure the detection of statistically significant differences among the experimental conditions based on power analysis. Our extensive analysis using CASE-Bench on various open-source and commercial LLMs reveals a substantial and significant influence of context on human judgments (p <0.0001 from a z-test), underscoring the necessity of context in safety evaluations. We also identify notable mismatches between human judgments and LLM responses, particularly in commercial models within safe contexts.1 Code and data used in the paper are available at https://github.com/BriansIDP/CASEBench.git.

## Authors

[[Guangzhi Sun]], [[Xiao Zhan]], [[Shutong Feng]], [[Philip C. Woodland]], [[Jose Such]]

## Data Description

CASE-Bench: a context-aware safety benchmark with 900 query-context pairs (450 queries x 2 contexts each), 47,000+ human annotations from 2,000+ annotators, covering 45 safety categories with CI-theory-based formalized context descriptions.


## Notes


## Tags

#Computer-Science---Artificial-Intelligence #Computer-Science---Computation-and-Language

## Citation Info

16 citations (Semantic Scholar/DOI) [2025-08-27]
