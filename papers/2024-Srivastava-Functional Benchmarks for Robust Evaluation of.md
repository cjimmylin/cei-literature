---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: G5IILKTJ
type: conferencePaper
short_title: "Functional Benchmarks for Robust Evaluation of"
year: 2024
first_author: "[[Saurabh Srivastava]]"
last_author: "[[Sooraj Thomas]]"
authors: "Saurabh Srivastava; Annarose M B; Anto P; Shashank Menon; Ajay Sukumar; Adwaith Samod T; Alan Philipose; Stevin Prince; Sooraj Thomas"
doi: 10.48550/arXiv.2402.19450
url: "http://arxiv.org/abs/2402.19450"
external_pdf: "http://arxiv.org/pdf/2402.19450.pdf"
publication: arXiv.org
CONF-CC: Preprint
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
tags: 
pdf_extract: "PDF Extracts/2024/2024-Srivastava-Functional Benchmarks for Robust Evaluation of.md"
abstract: "We propose a framework for robust evaluation of reasoning capabilities of language models, using functional variants of benchmarks. Models that solve a reasoning test should exhibit no difference in performance over the static version of a problem compared to a snapshot of the functional variant. We have rewritten the relevant fragment of the MATH benchmark into its functional variant MATH(), with functionalization of other benchmarks to follow."
paper_summary: "Abstract: We propose a framework for robust evaluation of reasoning capabilities of language models, using functional variants of benchmarks. Models that solve a reasoning test should exhibit no difference in p | Overview: Functional Benchmarks for Robust Evaluation of Reasoning Performance, and the Reasoning Gap Saurabh Srivastava∗, Annarose M B, Anto P V, Shashank Menon, Ajay Sukumar, Adwaith Samod T, Alan Philipose,  | Methodology: Given a benchmark test written as a 'question, answer' pair, we convert it to three functions 'problem(inputs), solution(inputs), inputs(rngs, seed)'. | Key Findings: Compute the product of the number $5+\\sqrt{3}$ and its radical conjugate. • counting and probability/64.json: Expected value of independent trials is | Conclusions: 5.1 Functionalizing MATH to MATH() We have functionalized 41.2% (2060/5000) of the MATH benchmark. This subset was chosen based on the portion of the"
local_pdf: "[[Lit-WS-PDFs/2024/2024-Srivastava-Functional Benchmarks for Robust Evaluation of.pdf]]"
DATE_ADDED: 20260208
LLM_assessed: "GPT-3.5, GPT-4, Claude-2, Mixtral, Llama-2, Qwen"
DATA_URL: "https://github.com/consequentai/fneval/"
CONFERENCE: "Other Conference"
ethics_overall: 0
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
research_topic: "Machine Learning"
nw_confucian: 0
nw_ubuntu: 0
nw_islamic_ethics: 0
nw_buddhist: 0
nw_dharmic: 0
nw_indigenous_relational: 0
nw_buen_vivir: 0
author_country: CH
author_region: "Western Europe"
author_global_north_south: "Global North"
weird_score: 84
is_benchmark: Yes
is_eval: Yes
is_dataset: Yes
data_description: "Benchmark dataset"
data_metrics: "Not specified"
---
# Functional Benchmarks for Robust Evaluation of Reasoning Performance, and the Reasoning Gap

## Metadata

**Authors:** Srivastava, Saurabh; B, Annarose M.; V, Anto P.; Menon, Shashank; Sukumar, Ajay; T, Adwaith Samod; Philipose, Alan; Prince, Stevin; Thomas, Sooraj

**Year:** 2024

**Type:** preprint

**DOI:** [10.48550/arXiv.2402.19450](https://doi.org/10.48550/arXiv.2402.19450)

**Publisher:** arXiv

## Links

- **Local PDF:** [[Lit-WS-PDFs/2024/2024-Srivastava-Functional Benchmarks for Robust Evaluation of.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2402.19450
- **DOI:** https://doi.org/10.48550/arXiv.2402.19450

## Abstract

We propose a framework for robust evaluation of reasoning capabilities of language models, using functional variants of benchmarks. Models that solve a reasoning test should exhibit no difference in performance over the static version of a problem compared to a snapshot of the functional variant. We have rewritten the relevant fragment of the MATH benchmark into its functional variant MATH(), with functionalization of other benchmarks to follow. When evaluating current state-of-the-art models over snapshots of MATH(), we find a reasoning gap -- the percentage difference between the static and functional accuracies. We find reasoning gaps from 58.35% to 80.31% among the state-of-the-art closed and open weights models that perform well on static benchmarks, with the caveat that the gaps are likely to be smaller with more sophisticated prompting strategies. Here we show that models which anecdotally have good reasoning performance over real-world tasks, have quantifiable lower gaps, motivating the open problem of building "gap 0" models. Code for evaluation and new evaluation datasets, three MATH() snapshots, are publicly available at https://github.com/consequentai/fneval/.

## Authors

[[Saurabh Srivastava]], [[Annarose M B]], [[Anto P]], [[Shashank Menon]], [[Ajay Sukumar]], [[Adwaith Samod T]], [[Alan Philipose]], [[Stevin Prince]], [[Sooraj Thomas]]

## Data Description

MATH() is a functional variant of the MATH benchmark where problem parameters are randomized, allowing infinite snapshot instantiation to test true reasoning versus memorization. Three quarterly snapshots (Oct/Nov/Dec 2023) are released publicly.


## Notes


## Tags

#Computer-Science---Artificial-Intelligence #Computer-Science---Computation-and-Language

## Citation Info

60 citations (Semantic Scholar/arXiv) [2025-08-27] 60 citations (Semantic Scholar/DOI) [2025-08-27] 60 citations (Semantic Scholar/DOI) [2025-08-23]
