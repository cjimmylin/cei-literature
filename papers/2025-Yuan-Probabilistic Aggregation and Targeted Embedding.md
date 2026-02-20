---






Human View: true
Human View Date: 2026-01-24
Human View note: "Fuse moral reasoning"
Not AI: 
key: ND9XA8P6
type: conferencePaper
short_title: "Probabilistic Aggregation and Targeted Embedding"
year: 2025
first_author: "[[Chenchen Yuan]]"
last_author: "[[Gjergji Kasneci]]"
authors: "Chenchen Yuan; Zheyu Zhang; Shuo Yang; Bardh Prenkaj; Gjergji Kasneci"
doi: 10.48550/arXiv.2506.14625
url: "http://arxiv.org/abs/2506.14625"
external_pdf: "http://arxiv.org/pdf/2506.14625.pdf"
publication: "Annual Meeting of the Association for Computational Linguistics"
CONF-CC: "ACL 2025"
ethics_perspective: "Moral Reasoning & Psychology"
national_ethnic_cultural: N/A
cultures_nationalities_list: "N/A"
languages_list: ""
religious_values: N/A
religious_values_list: N/A
moral_psychology: N/A
newtags: "Moral Reasoning & Psychology"
key_contribution: "Proposed a 'Probabilistic Aggregation' mechanism to fuse moral scores from multiple LLMs into a robust consensus, and 'Targeted Embedding Optimization' (TEO) to align deviants."
significance: "Offers a 'democratic' way to stabilize AI moral reasoning (Wisdom of Crowds) and a 'surgical' method to fix specific moral failures without expensive retraining."
tags: 
pdf_extract: "PDF Extracts/2025/2025-Yuan-Probabilistic Aggregation and Targeted Embedding.md"
abstract: "Large Language Models (LLMs) have shown impressive moral reasoning abilities. Yet they often diverge when confronted with complex, multi-factor moral dilemmas. To address these discrepancies, we propose a framework that synthesizes multiple LLMs' moral judgments into a collectively formulated moral judgment, realigning models that deviate significantly from this consensus. Our aggregation mech- anism fuses continuous moral acceptability scores (beyond binary labels) into a collective probability"
paper_summary: "Abstract: Large Language Models (LLMs) have shown impressive moral reasoning abilities. Yet they often diverge when confronted with complex, multi-factor moral dilemmas. To address these discrepancies, we propo | Overview: arXiv:2506.14625v2 [cs.CL] 18 Jun 2025 Probabilistic Aggregation and Targeted Embedding Optimization for Collective Moral Reasoning in Large Language Models Chenchen Yuan†, Zheyu Zhang†, Shuo Yang†, B | Methodology: that fuses continuous moral scores from multiple LLMs into a collective moral reference by model- ing annotator reliability. (2) We introduce a token- | Key Findings: Two key questions are examined: (1) Does the truncated-normal EM approach produce a coher- ent collective opinion across LLMs? (2) Can tar- geted embe | Conclusions: We propose a truncated-normal EM framework to synthesize moral judgments from multiple LLMs and introduce targeted embedding optimization to reduce mi"
local_pdf: "[[PDFs/2025/2025-Yuan-Probabilistic Aggregation and Targeted Embedding.pdf]]"
DATE_ADDED: 20260208
LLM_assessed: "GPT-3.5, GPT-4, Claude, Llama-2, Llama-3"
DATA_URL: "https://github.com/yuanchencn/Collective-Moral-Reasoning"
ethics_overall: "Yes"
virtue_ethics: "Yes"
deontological_ethics: "No"
utilitarian_ethics: "No"
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Evaluation framework dataset"
data_metrics: "Not specified"
CONFERENCE: "ACL 2025"
---
# Probabilistic Aggregation and Targeted Embedding Optimization for Collective Moral Reasoning in Large Language Models

## Metadata

**Authors:** Yuan, Chenchen; Zhang, Zheyu; Yang, Shuo; Prenkaj, Bardh; Kasneci, Gjergji

**Year:** 2025

**Type:** preprint

**DOI:** [10.48550/arXiv.2506.14625](https://doi.org/10.48550/arXiv.2506.14625)

**Publisher:** arXiv

## Links

- **Local PDF:** [[PDFs/2025/2025-Yuan-Probabilistic Aggregation and Targeted Embedding.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2506.14625
- **DOI:** https://doi.org/10.48550/arXiv.2506.14625

## Abstract

This paper proposes a framework for **Collective Moral Reasoning** in Large Language Models. Addressing the issue that individual LLMs often "hallucinate" unique (and sometimes dangerous) moral stances when faced with complex dilemmas, the authors introduce a **Probabilistic Aggregation** mechanism. This method fuses the "moral acceptability scores" of multiple models into a single, robust consensus. Furthermore, for models that deviate from this consensus, they propose a **Targeted Embedding Optimization** technique to "re-align" their internal representations without destroying their general semantic capabilities.

### Detailed Summary
The authors tackle the "Moral Disagreement" problem in AI ensembles. They treat moral judgment not as a binary classification (Right/Wrong) but as a continuous probability distribution. By aggregating these distributions from multiple models (weighted by reliability), they establish a "Collective Moral Norm." They then show that misaligned models can be corrected not by expensive full fine-tuning, but by optimizing specific token embeddings to minimize the **Jensen-Shannon (JS) divergence** between the model's output and the collective consensus. This serves as a "surgical" intervention for moral alignment.

### Paper Outline
1.  **Introduction**: The risk of idiosyncratic moral failures in single LLMs.
2.  **Methodology - Aggregation**: Developing a probabilistic fusion function for continuous moral scores.
3.  **Methodology - Alignment**: Targeted Embedding Optimization (TEO) identifying and shifting "moral vectors."
4.  **Experiments**: Testing on large-scale social dilemma datasets (e.g., ETHICS, Social Chemistry).
5.  **Results**: Improvements in consensus robustness and individual model fidelity.
6.  **Conclusion**: Data-driven ensemble alignment is safer than single-source alignment.

### Methods Summary
*   **Consensus Mechanism**: A weighted average of soft-probability outputs from $N$ models (e.g., Llama, GPT, Mistral).
*   **Targeted Embedding Optimization (TEO)**: instead of updating model weights (which is costly and risks catastrophic forgetting), they optimize the continuous embedding space of specific "concept tokens" (like "harm", "fairness") to align the model's output distribution with the target.
*   **Dataset**: Large-scale social moral dilemma dataset (likely derived from Social Chemistry 101 or similar).

### Results Summary
1.  **Robust Consensus**: The aggregated judgment was consistently more aligned with human labels than any single model's judgment (Wisdom of the Crowds).
2.  **TEO Efficacy**: The embedding optimization successfully "steered" deviant models back to the consensus with minimal computational overhead and negligible degradation on general language tasks.
3.  **Fidelity**: Post-optimization, models retained their ability to reason about the *structure* of the dilemma while correcting their *conclusion*.

### Conclusions
Moral alignment shouldn't rely on a single "oracle" model. A collective approach, combined with surgical embedding interventions, offers a scalable way to ensure consistent moral reasoning across diverse AI systems. The "Probabilistic Aggregation" method provides a mathematical foundation for democratic AI governance.

### Artifact Contributions
*   **Probabilistic Aggregation Framework**: A mathematical model for fusing soft moral judgments.
*   **Targeted Embedding Optimization Code**: A lightweight method for test-time alignment.

## Authors

[[Chenchen Yuan]], [[Zheyu Zhang]], [[Shuo Yang]], [[Bardh Prenkaj]], [[Gjergji Kasneci]]

## Data Description

The study uses 42,501 moral dilemmas from the AITA (Am I The Asshole) Reddit dataset, neutralized into 150-token summaries using GPT-4o-Mini. Each dilemma is annotated by multiple LLMs with continuous moral acceptability scores across five moral philosophical theories (justice, virtue, deontology, utilitarianism, and commonsense morality), enabling probabilistic aggregation of collective moral judgments.


## Notes


## Tags

#Computer-Science---Artificial-Intelligence #Computer-Science---Computation-and-Language

## Citation Info

0 citations (Semantic Scholar/DOI) [2025-08-27] 0 citations (Semantic Scholar/DOI) [2025-08-23]
