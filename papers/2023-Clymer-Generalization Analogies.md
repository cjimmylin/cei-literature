---


Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: 6455Y4UP
type: conferencePaper
short_title: "Generalization Analogies"
year: 2025
first_author: "[[Joshua Clymer]]"
last_author: "[[Sam Wang]]"
authors: "Joshua Clymer; Garrett Baker; Rohan Subramani; Sam Wang"
doi: 10.48550/arXiv.2311.07723
url: "http://arxiv.org/abs/2311.07723"
external_pdf: "http://arxiv.org/pdf/2311.07723.pdf"
publication: arXiv.org
national_ethnic_cultural: N/A
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: N/A
newtags: 
tags: 
pdf_extract: "PDF Extracts/2023/2023-Clymer-Generalization Analogies.md"
abstract: "As AI systems become more intelligent and their behavior becomes more challenging to assess, they may learn to game the flaws of human feed- back instead of genuinely striving to follow in- structions; however, this risk can be mitigated by controlling how LLMs generalize human feed- back to situations where it is unreliable. To better understand how reward models generalize, we craft 69 distribution shifts spanning 8 categories. We find that reward models do not learn to evalu- ate ‘instruction"
paper_summary: "Abstract: As AI systems become more intelligent and their behavior becomes more challenging to assess, they may learn to game the flaws of human feed- back instead of genuinely striving to follow in- structions | Overview: Generalization Analogies (GENIES): A Testbed for Generalizing AI Oversight to Hard-To-Measure Domains Joshua Clymer 1 Garrett Baker 2 Rohan Subramani 1 Sam Wang 1 Abstract As AI systems become more in"
local_pdf: "[[PDFs/2023/2023-Clymer-Generalization Analogies.pdf]]"
ethics_overall: No
virtue_ethics: No
deontological_ethics: No
utilitarian_ethics: No
research_topic: "Machine Learning"
is_benchmark: Yes
is_eval: Yes
is_dataset: No
data_description: Benchmark
data_metrics: "8 categories"
LLM_assessed: "Llama"
DATA_URL: "https://github.com/Joshuaclymer/GENIES"
---
# Generalization Analogies: A Testbed for Generalizing AI Oversight to Hard-To-Measure Domains

## Metadata

**Authors:** Clymer, Joshua; Baker, Garrett; Subramani, Rohan; Wang, Sam

**Year:** 2023

**Type:** preprint

**DOI:** [10.48550/arXiv.2311.07723](https://doi.org/10.48550/arXiv.2311.07723)

**Publisher:** arXiv

## Links

- **Local PDF:** [[PDFs/2023/2023-Clymer-Generalization Analogies.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2311.07723
- **DOI:** https://doi.org/10.48550/arXiv.2311.07723

## Abstract

As AI systems become more intelligent and their behavior becomes more challenging to assess, they may learn to game the flaws of human feedback instead of genuinely striving to follow instructions; however, this risk can be mitigated by controlling how LLMs generalize human feedback to situations where it is unreliable. To better understand how reward models generalize, we craft 69 distribution shifts spanning 8 categories. We find that reward models do not learn to evaluate ‘instruction-following’ by default and instead favor personas that resemble internet text. Techniques for interpreting reward models’ internal representations achieve better generalization than standard fine-tuning, but still frequently fail to distinguish instruction-following from conflated behaviors. We consolidate the 15 most challenging distribution shifts into the GENeralization analogIES (GENIES) benchmark, which we hope will enable progress toward controlling reward model generalization.

## Authors

[[Joshua Clymer]], [[Garrett Baker]], [[Rohan Subramani]], [[Sam Wang]]

## Data Description

GENIES (GENeralization analogIES) is a benchmark consisting of 69 distribution shifts spanning 8 categories, consolidated into 15 curated challenging distribution shifts for evaluating reward model generalization. The datasets include a mix of fully generated data (24 using ChatGPT, filtered with GPT-4), repurposed existing datasets (11), and hybrid datasets (33). LLaMA-30B reward models are the primary models evaluated for instruction-following generalization.


## Notes


## Tags

#Computer-Science---Artificial-Intelligence #Computer-Science---Machine-Learning #Computer-Science---Computation-and-Language

## Citation Info

29 citations (Semantic Scholar/DOI) [2025-08-27] 7 citations (Semantic Scholar/arXiv) [2025-08-27] 7 citations (Semantic Scholar/DOI) [2025-08-23]
