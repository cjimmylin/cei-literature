---





























Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: QTHPTLW2
type: conferencePaper
short_title: "Are Large Language Models Consistent over"
year: 2024
first_author: "[[Jared Moore]]"
last_author: "[[Diyi Yang]]"
authors: "Jared Moore; Tanvi Deshpande; Diyi Yang"
doi: 10.48550/arXiv.2407.02996
url: "http://arxiv.org/abs/2407.02996"
external_pdf: "http://arxiv.org/pdf/2407.02996.pdf"
publication: "Conference on Empirical Methods in Natural Language Processing"
CONF-CC: "EMNLP 2024"
national_ethnic_cultural: "Multicultural/Cross-cultural"
cultures_nationalities_list: "Multicultural/Cross-cultural"
languages_list: "Chinese, English, German, Japanese"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: "Chinese, Japanese, German, American, Bias & Fairness"
key_contribution: "Investigated LLM value consistency across paraphrases, languages, and use-cases (open vs multiple choice), finding models are generally consistent but falter on controversial topics."
significance: "Challenges the 'stochastic parrot' view by showing robust value consistency, but highlights that 'controversial' topics (likely due to inconsistent RLHF) trigger more variability."
tags: 
pdf_extract: "PDF Extracts/2024/2024-Moore-Are Large Language Models Consistent over.md"
abstract: "Large language models (LLMs) appear to bias their survey answers toward certain values. Nonetheless, some argue that LLMs are too inconsistent to simulate particular values. Are they? To answer, we first define value consistency as the similarity of answers across (1) paraphrases of one question, (2) related questions under one topic, (3) multiple-choice and open-ended use-cases of one question, and (4) multilingual translations of a question to English, Chinese, German, and Japanese."
paper_summary: "Abstract: Large language models (LLMs) appear to bias their survey answers toward certain values. Nonetheless, some argue that LLMs are too inconsistent to simulate particular values. Are they? To answer, we fi | Overview: Are Large Language Models Consistent over Value-laden Questions? Jared Moore Stanford University jlcmoore@stanford.edu Tanvi Deshpande Stanford University tanvimd@stanford.edu Diyi Yang Stanford Unive | Conclusions: Prior work has argued that models either do (Dur- mus et al., 2024; Santurkar et al., 2023) or do not (Röttger et al., 2024; Shu et al., 2023) hold ce"
local_pdf: "[[PDFs/2024/2024-Moore-Are Large Language Models Consistent over.pdf]]"
DATE_ADDED: 20260208
LLM_assessed: "GPT-4o, Llama-2, Llama-3, Yi, Command-R"
DATA_URL: "https://huggingface.co/datasets/jlcmoore/ValueConsistency"
CONFERENCE: "EMNLP 2024"
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "Bias & Fairness"
is_benchmark: "No"
is_eval: "Yes"
is_dataset: Yes
data_description: "Evaluation approach"
data_metrics: "8,000 questions"
---
# Are Large Language Models Consistent over Value-laden Questions?

## Metadata

**Authors:** Moore, Jared; Deshpande, Tanvi; Yang, Diyi

**Year:** 2024

**Type:** preprint

**DOI:** [10.48550/arXiv.2407.02996](https://doi.org/10.48550/arXiv.2407.02996)

**Publisher:** arXiv

## Links

- **Local PDF:** [[PDFs/2024/2024-Moore-Are Large Language Models Consistent over.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2407.02996
- **DOI:** https://doi.org/10.48550/arXiv.2407.02996

## Abstract

Large language models (LLMs) appear to bias their survey answers toward certain values. Nonetheless, some argue that LLMs are too inconsistent to simulate particular values. Are they? To answer, we first define value consistency as the similarity of answers across (1) paraphrases of one question, (2) related questions under one topic, (3) multiple-choice and open-ended use-cases of one question, and (4) multilingual translations of a question to English, Chinese, German, and Japanese. We apply these measures to small and large, open LLMs including llama-3, as well as gpt-4o, using 8,000 questions spanning more than 300 topics. Unlike prior work, we find that models are relatively consistent across paraphrases, use-cases, translations, and within a topic. Still, some inconsistencies remain. Models are more consistent on uncontroversial topics (e.g., in the U.S., "Thanksgiving") than on controversial ones ("euthanasia"). Base models are both more consistent compared to fine-tuned models and are uniform in their consistency across topics, while fine-tuned models are more inconsistent about some topics ("euthanasia") than others ("women’s rights") like our human subjects (n=165).

## Authors

[[Jared Moore]], [[Tanvi Deshpande]], [[Diyi Yang]]

## Data Description

VALUECONSISTENCY: a dataset of 8,000+ questions spanning 300+ topics across four languages (English, Chinese, German, Japanese) for measuring LLM value consistency across paraphrases, use-cases, multilingual translations, and related questions.


## Notes


## Tags

#Computer-Science---Artificial-Intelligence #Computer-Science---Computation-and-Language

## Citation Info

43 citations (Semantic Scholar/DOI) [2025-08-27] 19 citations (Semantic Scholar/arXiv) [2025-08-27] 32 citations (Semantic Scholar/DOI) [2025-08-23]
