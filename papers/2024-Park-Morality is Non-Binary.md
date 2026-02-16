---



Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: 373IZL7R
type: conferencePaper
short_title: "Morality is Non-Binary"
year: 2025
first_author: "[[Jeongwoo Park]]"
last_author: "[[Murukannaiah, Pradeep K]]"
authors: "[[Park, Jeongwoo]]; [[Liscio, Enrico]]; [[Murukannaiah, Pradeep K.]]"
doi: 10.48550/arXiv.2401.17228
url: "http://arxiv.org/abs/2401.17228"
pdf_extract: "PDF Extracts/2024/2024-Park-Morality is Non-Binary.md"
local_pdf: "[[PDFs/2024/2024-Park-Morality is Non-Binary.pdf]]"
external_pdf: "http://arxiv.org/pdf/2401.17228.pdf"
publication: Findings
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: Deontology
key_contribution: "Builds a 'pluralist moral sentence embedding space' using contrastive learning to capture multiple moral elements rather than binary right/wrong"
significance: "Shows that moral pluralism (including deontology) can be mathematically represented in embedding space, enabling more nuanced value alignment"
tags: 
abstract: "Recent advances in NLP show that language models retain a discernible level of knowledge in deontological ethics and moral norms. However, existing works often treat morality as binary, ranging from right to wrong. This simplistic view does not capture the nuances of moral judgment. Pluralist moral philosophers argue that human morality can be deconstructed into a finite number of elements, respecting individual differences in moral judgment."
paper_summary: "Abstract: Recent advances in NLP show that language models retain a discernible level of knowledge in deontological ethics and moral norms. How- ever, existing works often treat morality as bi- nary, ranging fr | Overview: Morality is Non-Binary: Building a Pluralist Moral Sentence Embedding Space using Contrastive Learning Jeongwoo Park∗, Enrico Liscio∗, and Pradeep K. Murukannaiah Delft University of Technology, the N | Methodology: to morality can be captured in a sentence embed- ding space, but also that human labels are necessary to successfully train the embeddings. Our work r | Key Findings: We investigate the embedding space by (1) show- ing a visualization of the training set data in the embedding space to gain an intuitive understand- i | Conclusions: We report the results of the intrinsic evaluations to judge the effect of supervised training, and the re- sults of the extrinsic evaluation to assess"
DATE_ADDED: 20260208
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "Yes"
utilitarian_ethics: "No"
is_benchmark: "No"
is_eval: "No"
is_dataset: "No"
data_description: "N/A"
data_metrics: "Not specified"
LLM_assessed: BERT
DATA_URL: "https://github.com/jeongwoopark0514/morality-is-non-binary"
---
 Morality is Non-Binary: Building a Pluralist Moral Sentence Embedding Space using Contrastive Learning

## Authors

[[Jeongwoo Park|Park, Jeongwoo]], [[Enrico Liscio|Liscio, Enrico]], [[Murukannaiah, Pradeep K]]

## Links

- **Local PDF:** [[PDFs/2024/2024-Park-Morality is Non-Binary.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2401.17228
- **DOI:** https://doi.org/10.48550/arXiv.2401.17228

## Detailed Summary

This paper investigates whether a pluralist approach to morality, specifically **Moral Foundations Theory (MFT)**, can be captured in a sentence embedding space. The authors argue that existing work often treats morality as binary (right vs. wrong), which fails to capture the nuanced differences in human moral judgment. 

To address this, the authors propose a method for mapping MFT elements to a sentence embedding space using **SimCSE** (Simple Contrastive Learning of Sentence Embeddings). They test both supervised and unsupervised approaches and evaluate how well the resulting space disentangles the 10 moral elements (5 foundations with virtue/vice dualities).

## Paper Outline

1.  **Introduction**: Moving from binary morality to pluralist moral elements in NLP.
2.  **Background**: Moral Foundations Theory (MFT) and Contrastive Learning (SimCSE).
3.  **Methodology**:
    *   Mapping MFT to sentence embedding space.
    *   Supervised vs. Unsupervised Contrastive Learning.
4.  **Evaluation**:
    *   Intrinsic Evaluation: Relationship among moral elements.
    *   Extrinsic Evaluation: Generalization to novel test sets and moral dictionaries.
5.  **Conclusion**: Pluralist morality is captureable but requires human-labeled supervision.

## Methods Summary

The authors use **SimCSE**, a text-based Contrastive Learning (CL) framework built on BERT. 
1.  **Supervised Approach**: Minimizes the distance between sentences with the same MFT label and maximizes the distance between those with different labels. 
2.  **Unsupervised Approach**: Uses a slight variation of a sentence (via dropout) as a positive instance and a random sentence as a negative instance.
The model is trained on the **Moral Foundations Twitter Corpus (MFTC)** and evaluated on its ability to distinguish between 10 moral elements (e.g., Care vs. Harm, Fairness vs. Cheating).

## Results Summary

1.  **Representation Quality**: A pluralist approach to morality can be captured in a sentence embedding space, but the unsupervised (self-supervised) approach alone is insufficient to capture the complexity and disentangle the foundations.
2.  **Supervision Necessity**: Human labels are necessary to successfully train the embeddings to differentiate between subtle moral nuances (e.g., distinguishing between different virtues).
3.  **Element Difficulty**: Some elements, like "Purity," remain difficult for all models to classify correctly, likely due to their relative rarity in training datasets.

## Conclusions

Self-supervision alone is not enough to capture the richness and complexity of human morality in AI systems. The authors conclude that incorporating a pluralist approach requires fine-grained, human-annotated data. This work provides a foundation for more sophisticated "Moral Embeddings" that can be used for nuanced value alignment.

## Artifact Contributions

*   **Pluralist Moral Embedding Space**: A methodology for training sentence embeddings that reflect Moral Foundations Theory.
*   **MFTC-based Simulation Results**: Comparative data on BERT vs. SimCSE for moral element classification.


## Tags

#Computer-Science---Artificial-Intelligence #Computer-Science---Computation-and-Language

## Data Description

The paper builds a pluralist moral sentence embedding space using contrastive learning (SimCSE) on BERT sentence embeddings, trained and evaluated on the Moral Foundations Twitter Corpus (MFTC) containing 35,108 tweets annotated with Moral Foundations Theory elements. The dataset is split 90/10 for training/testing, with intrinsic evaluation via UMAP visualization and moral similarity tables, and extrinsic evaluation against the Moral Foundation Dictionary 2.0.


## Citation Info

5 citations (Semantic Scholar/DOI) [2025-08-27] 5 citations (Semantic Scholar/DOI) [2025-08-23]
## Abstract

Recent advances in NLP show that language models retain a discernible level of knowledge in deontological ethics and moral norms. However, existing works often treat morality as binary, ranging from right to wrong. This simplistic view does not capture the nuances of moral judgment. Pluralist moral philosophers argue that human morality can be deconstructed into a finite number of elements, respecting individual differences in moral judgment. In line with this view, we build a pluralist moral sentence embedding space via a state-of-the-art contrastive learning approach. We systematically investigate the embedding space by studying the emergence of relationships among moral elements, both quantitatively and qualitatively. Our results show that a pluralist approach to morality can be captured in an embedding space. However, moral pluralism is challenging to deduce via self-supervision alone and requires a supervised approach with human labels.
