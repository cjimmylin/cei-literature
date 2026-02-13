---


Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: ID6PYJ9M
type: conferencePaper
short_title: "Inducing Human-like Biases in Moral Reasoning"
year: 2025
first_author: "[[Artem Karpov]]"
last_author: "[[Bogdan-Ionut Cirstea]]"
authors: "Artem Karpov; Seong Hah Cho; Austin Meek; Raymond Koopmanschap; Lucy Farnik; Bogdan-Ionut Cirstea"
doi: 10.48550/arXiv.2411.15386
url: "http://arxiv.org/abs/2411.15386"
external_pdf: "http://arxiv.org/pdf/2411.15386.pdf"
publication: arXiv.org
national_ethnic_cultural: N/A
religious_values: "Christianity"
religious_values_list: "Christianity"
moral_psychology: N/A
newtags: "Moral Reasoning & Psychology"
key_contribution: "Fine-tuned LLMs on human behavioral (ETHICS) and fMRI brain data to see if models become more 'human-like' in moral reasoning. Result: Accuracy improved, but 'BrainScore' (alignment with fMRI signals) did not."
significance: "A fascinating negative result suggesting that behavioral alignment (outputting the right answer) does not imply mechanistic alignment (thinking like a human brain)."
tags: 
pdf_extract: "PDF Extracts/2024/2024-Karpov-Inducing Human-like Biases in Moral Reasoning.md"
abstract: "In this work, we study the alignment (BrainScore) of large language models (LLMs) fine-tuned for moral reasoning on behavioral data and/or brain data of humans performing the same task. We also explore if fine-tuning several LLMs on the fMRI data of humans performing moral reasoning can improve the BrainScore. We fine-tune several LLMs (BERT, RoBERTa, DeBERTa) on moral reasoning behavioral data from the ETHICS benchmark [Hendrycks et al., 2020], on the moral reasoning fMRI data from Koster-Hale"
paper_summary: "Abstract: In this work, we study the alignment (BrainScore) of large language models (LLMs) fine-tuned for moral reasoning on behavioral data and/or brain data of humans performing the same task. We also explor | Overview: Inducing Human-like Biases in Moral Reasoning Language Models Artem Karpov ∗ Independent Seong Hah Cho ∗ Independent Austin Meek ∗ University of Delaware Raymond Koopmanschap Independent Lucy Farnik U | Methodology: 3.1 Benchmark and Dataset To quantitatively measure the moral reasoning performance of the fine-tuned LLMs, we used the common sense category of the E"
local_pdf: "[[PDFs/2024/2024-Karpov-Inducing Human-like Biases in Moral Reasoning.pdf]]"
ethics_overall: No
virtue_ethics: No
deontological_ethics: No
utilitarian_ethics: No
ethics_perspective: "Moral Reasoning & Psychology"
is_benchmark: Yes
is_eval: Yes
is_dataset: No
data_description: "Benchmark for moral/ethical reasoning"
data_metrics: "Not specified"
LLM_assessed: "BERT, RoBERTa, DeBERTa"
DATA_URL: "https://github.com/ajmeek/Inducing-human-like-biases-in-moral-reasoning-LLMs"
---
# Inducing Human-like Biases in Moral Reasoning Language Models

## Metadata

**Authors:** Karpov, Artem; Cho, Seong Hah; Meek, Austin; Koopmanschap, Raymond; Farnik, Lucy; Cirstea, Bogdan-Ionut

**Year:** 2024

**Type:** preprint

**DOI:** [10.48550/arXiv.2411.15386](https://doi.org/10.48550/arXiv.2411.15386)

**Publisher:** arXiv

## Links

- **Local PDF:** [[PDFs/2024/2024-Karpov-Inducing Human-like Biases in Moral Reasoning.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2411.15386
- **DOI:** https://doi.org/10.48550/arXiv.2411.15386

## Abstract

In this work, we study the alignment (BrainScore) of large language models (LLMs) fine-tuned for moral reasoning on behavioral data and/or brain data of humans performing the same task. We also explore if fine-tuning several LLMs on the fMRI data of humans performing moral reasoning can improve the BrainScore. We fine-tune several LLMs (BERT, RoBERTa, DeBERTa) on moral reasoning behavioral data from the ETHICS benchmark [Hendrycks et al., 2020], on the moral reasoning fMRI data from Koster-Hale et al. [2013], or on both. We study both the accuracy on the ETHICS benchmark and the BrainScores between model activations and fMRI data. While larger models generally performed better on both metrics, BrainScores did not significantly improve after fine-tuning.

## Authors

[[Artem Karpov]], [[Seong Hah Cho]], [[Austin Meek]], [[Raymond Koopmanschap]], [[Lucy Farnik]], [[Bogdan-Ionut Cirstea]]

## Data Description

The study uses the common sense category of the ETHICS benchmark for moral reasoning evaluation and fMRI data from Koster-Hale et al. (2013) on moral judgments of intentional and accidental moral violations. Four encoder models (BERT-base-cased, BERT-large-cased, RoBERTa-large, DeBERTa-v2-xlarge) were fine-tuned across 450 runs totaling 292 hours of training, producing 1,082 different models. Brain-model alignment (BrainScore) was measured using Pearson's correlation between predicted and actual brain activity across 1,024 regions of interest.


## Notes


## Tags

#Computer-Science---Artificial-Intelligence #Computer-Science---Computers-and-Society #Computer-Science---Machine-Learning

## Citation Info

31 citations (Semantic Scholar/arXiv) [2025-08-27] 53 citations (Semantic Scholar/DOI) [2025-08-27] 0 citations (Semantic Scholar/DOI) [2025-08-23]
