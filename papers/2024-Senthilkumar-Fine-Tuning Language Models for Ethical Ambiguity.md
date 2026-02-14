---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: 5NT4RAZP
type: conferencePaper
short_title: "Fine-Tuning Language Models for Ethical Ambiguity"
year: 2025
first_author: "[[Pranav Senthilkumar]]"
last_author: "[[Kevin Zhu]]"
authors: "Pranav Senthilkumar; Visshwa Balasubramanian; Prisha Jain; Aneesa Maity; Jonathan Lu; Kevin Zhu"
doi: 10.48550/arXiv.2410.07826
tags: 
url: "http://arxiv.org/abs/2410.07826"
external_pdf: "http://arxiv.org/pdf/2410.07826.pdf"
publication: arXiv.org
national_ethnic_cultural: N/A
religious_values: Jainism
religious_values_list: Jainism
moral_psychology: N/A
newtags: "AI Safety & Alignment"
key_contribution: "Investigated LLM performance on *ambiguous* ethical scenarios (using Scruples/DILEMMAS datasets), finding that fine-tuning improves alignment but models still lag behind BERT baselines in identifying ambiguity."
significance: "Highlight that LLMs act 'too certain' in gray areas; true alignment requires recognizing when a situation is morally ambiguous rather than forcing a confident binary judgment."
pdf_extract: "PDF Extracts/2024/2024-Senthilkumar-Fine-Tuning Language Models for Ethical Ambiguity.md"
abstract: "Language models often misinterpret human intentions due to their handling of ambiguity, a limitation well-recognized in NLP research. While morally clear scenarios are more discernible to LLMs, greater difficulty is encountered in morally ambiguous contexts. In this investigation, we explored LLM calibration to show that human and LLM judgments are poorly aligned in such scenarios. We used two curated datasets from the Scruples project for evaluation: DILEMMAS, which involves pairs of distinct m"
paper_summary: "Abstract: Language models often misinterpret human intentions due to their handling of ambiguity, a limitation well-recognized in NLP research. While morally clear scenarios are more discernible to LLMs, greate | Overview: Fine-Tuning Language Models for Ethical Ambiguity: A Comparative Study of Alignment with Human Responses Pranav Senthilkumar Visshwa Balasubramanian Prisha Jain Aneesa Maity Jonathan Lu Kevin Zhu Algo | Methodology: 3.1 Model Calibration Approach To measure the calibration of LLM responses with respect to human ethical judgments, we extracted token probabilities f | Conclusions: In summary, fine-tuning led to different outcomes based on the datasets: notable progress on the Dilemmas dataset but stronger performance on Anecdote"
local_pdf: "[[PDFs/2024/2024-Senthilkumar-Fine-Tuning Language Models for Ethical Ambiguity.pdf]]"
ethics_overall: No
virtue_ethics: No
deontological_ethics: No
utilitarian_ethics: No
ethics_perspective: "AI Safety & Alignment"
is_benchmark: Yes
is_eval: Yes
is_dataset: Yes
data_description: "Benchmark for moral/ethical reasoning dataset"
data_metrics: "Not specified"
LLM_assessed: "GPT-4, Llama-3, Mistral"
DATA_URL: NA
---
# Fine-Tuning Language Models for Ethical Ambiguity: A Comparative Study of Alignment with Human Responses

## Metadata

**Authors:** Senthilkumar, Pranav; Balasubramanian, Visshwa; Jain, Prisha; Maity, Aneesa; Lu, Jonathan; Zhu, Kevin

**Year:** 2024

**Type:** preprint

**DOI:** [10.48550/arXiv.2410.07826](https://doi.org/10.48550/arXiv.2410.07826)

**Publisher:** arXiv

## Links

- **Local PDF:** [[PDFs/2024/2024-Senthilkumar-Fine-Tuning Language Models for Ethical Ambiguity.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2410.07826
- **DOI:** https://doi.org/10.48550/arXiv.2410.07826

## Abstract

Language models often misinterpret human intentions due to their handling of ambiguity, a limitation well-recognized in NLP research. While morally clear scenarios are more discernible to LLMs, greater difficulty is encountered in morally ambiguous contexts. In this investigation, we explored LLM calibration to show that human and LLM judgments are poorly aligned in such scenarios. We used two curated datasets from the Scruples project for evaluation: DILEMMAS, which involves pairs of distinct moral scenarios to assess the model’s ability to compare and contrast ethical situations, and ANECDOTES, which presents individual narratives to evaluate the model’s skill in drawing out details, interpreting, and analyzing distinct moral scenarios. Model answer probabilities were extracted for all possible choices and compared with human annotations to benchmark the alignment of three models— Llama-3.1-8b, Zephyr-7b-beta, and Mistral-7b. Significant improvements were observed after fine-tuning, with notable enhancements in both cross-entropy and Dirichlet scores, particularly in the latter. Notably, after fine-tuning, the performance of Mistral-7B-Instruct-v0.3 was on par with GPT-4o. However, the experimental models that were examined were all still outperformed by the BERT and RoBERTa models in terms of cross-entropy scores[Lourie et al., 2021]. Our fine-tuning approach, which improves the model’s understanding of text distributions in a text-to-text format, effectively enhances performance and alignment in complex decision-making contexts, underscoring the need for further research to refine ethical reasoning techniques and capture human judgment nuances.

## Authors

[[Pranav Senthilkumar]], [[Visshwa Balasubramanian]], [[Prisha Jain]], [[Aneesa Maity]], [[Jonathan Lu]], [[Kevin Zhu]]

## Data Description

This study uses two existing datasets from the Scruples project: the DILEMMAS dataset containing 10,000 ethical dilemmas annotated via Mechanical Turk, and the ANECDOTES dataset comprising 32,000 real-life scenarios from the r/AmItheAsshole subreddit. The models are evaluated on calibration to human moral judgments using cross-entropy and Dirichlet multinomial loss, with QLoRA fine-tuning applied to improve alignment.


## Notes


## Tags

#Computer-Science---Computation-and-Language

## Citation Info

2 citations (Semantic Scholar/DOI) [2025-08-27] 2 citations (Semantic Scholar/DOI) [2025-08-23]
