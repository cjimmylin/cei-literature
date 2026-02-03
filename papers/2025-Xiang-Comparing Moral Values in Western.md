---



Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: YY7GGHXH
type: conferencePaper
short_title: "Comparing Moral Values in Western"
year: 2025
first_author: "[[Chaoyi Xiang]]"
authors: "Chaoyi Xiang; Chunhua Liu; Simon De Deyne; Lea Frermann"
doi: 10.48550/arXiv.2505.19674
tags: "Computer Science - Computation and Language"
url: "http://arxiv.org/abs/2505.19674"
external_pdf: "http://arxiv.org/pdf/2505.19674.pdf"
publication: "Annual Meeting of the Association for Computational Linguistics"
national_ethnic_cultural: N/A
religious_values: N/A
moral_psychology: N/A
newtags: "Moral Reasoning & Psychology"
key_contribution: "Used 'Word Associations' (projective testing) to probe implicit moral values in LLMs, finding they lack the 'visceral' associations of humans and are biased towards WEIRD values (Care/Fairness)."
significance: "Demonstrates a more robust method for moral auditing than direct questioning (which is easily rehearsed), revealing the deep semantic divergence between 'clean' LLM morality and 'messy' human morality."
pdf_extract: "PDF Extracts/2025-Xiang-Comparing Moral Values in Western.md"
abstract: "As the impact of large language models in- creases, understanding the moral values they reflect becomes ever more important. Assess- ing the nature of moral values as understood by these models via direct prompting is challeng- ing due to potential leakage of human norms into model training data, and their sensitivity to prompt formulation. Instead, we propose to use word associations, which have been shown to reflect moral reasoning in humans, as low- level underlying representations to obtain"
paper_summary: "Abstract: As the impact of large language models in- creases, understanding the moral values they reflect becomes ever more important. Assess- ing the nature of moral values as understood by these models via di | Overview: arXiv:2505.19674v2 [cs.CL] 28 May 2025 Comparing Moral Values in Western English-speaking societies and LLMs with Word Associations Chaoyi Xiang1 Chunhua Liu1 Simon De Deyne2 Lea Frermann1 1School of  | Methodology: to understanding moral alignment. • A framework to effectively extract multidi- mensional moral values from global word as- sociation networks, allowi | Key Findings: Following the propagation process, we obtain moral scores across five dimensions for each of the 12,000 cues in both GMN-L and GMN-H. To assess the al"
local_pdf: "[[PDFs/2025-Xiang-Comparing Moral Values in Western.pdf]]"
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "AI Safety & Alignment"
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Evaluation methodology dataset"
data_metrics: "Not specified"
---
# Comparing Moral Values in Western English-speaking societies and LLMs with Word Associations

## Metadata

**Authors:** Xiang, Chaoyi; Liu, Chunhua; Deyne, Simon De; Frermann, Lea

**Year:** 2025

**Type:** preprint

**DOI:** [10.48550/arXiv.2505.19674](https://doi.org/10.48550/arXiv.2505.19674)

**Publisher:** arXiv

## Links

- **Local PDF:** [[PDFs/2025-Xiang-Comparing Moral Values in Western.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2505.19674
- **DOI:** https://doi.org/10.48550/arXiv.2505.19674

## Abstract

This paper proposes using **Word Associations** as a robust method for probing the **Moral Values** of Large Language Models. Arguing that direct prompting is susceptible to "contamination" (leakage of human norms into training data) and prompt sensitivity, the authors use low-level word associations to reveal the "underlying representations" of moral concepts. They compare LLM-generated associations with those from Western English-speaking communities, finding systematic differences in how models conceptualize moral foundations (Care, Fairness, Authority, etc.).

### Detailed Summary
The study leverages the "Projective" nature of word associations—a technique long used in psychology to uncover implicit biases and conceptual structures. By propagating moral values from seed words (derived from Moral Foundations Theory) through the association graphs of both Humans and LLMs, the authors create a "moral map" of the latent space. They find that while LLMs generally align with Western liberal values (high Care/Fairness), their association graphs lack the "messiness" and emotional depth of human associations, often defaulting to dictionary-like definitions rather than lived experience.

### Paper Outline
1.  **Introduction**: Limits of direct moral questioning (surveys) for LLMs.
2.  **Methodology**:
    *   Dataset creation: LLM-generated word associations to match human norms (`SWOW` dataset).
    *   Value Propagation: Spreading "moral charge" from seed words through the graph.
3.  **Experiments**: Comparing the morality of associations in GPT-4, Llama, etc., vs. English speakers.
4.  **Results**: Systematic differences in moral conceptualization.
5.  **Discussion**: Implications for alignment—are we aligning to "stated" values or "implicit" structures?

### Methods Summary
*   **Word Association Task**: Prompting the model "What is the first word that comes to mind when you hear [STIMULUS]?"
*   **Graph Construction**: Building a weighted graph where edges represent association strength.
*   **Label Propagation**: Using a semi-supervised learning algorithm to propagate Moral Foundation labels (e.g., "Harm", "Purity") from known seed words to the rest of the vocabulary.
*   **Comparison**: Calculating the cosine similarity and structural alignment between the Human Moral Graph and the LLM Moral Graph.

### Results Summary
1.  **Sanitization**: LLMs produce "cleaner," more normative associations. For a word like "War," humans might associate "Death" or "Pain" (visceral), while LLMs might associate "Conflict" or "Strategy" (descriptive).
2.  **Moral Drift**: LLMs tend to over-emphasize the **Care** and **Fairness** foundations compared to **Loyalty** and **Sanctity**, reflecting a "WEIRD" (Western, Educated, Industrialized, Rich, Democratic) bias in their training data.
3.  **Robustness**: The word association method was more robust to prompt engineering than standard "Do you agree with X?" surveys, making it a better tool for audit.

### Conclusions
Directly asking an LLM "Are you moral?" yields rehearsed answers. probing its free associations reveals its true "subconscious" structures. This paper argues that true alignment requires synchronizing these low-level conceptual maps, not just high-level outputs.

### Artifact Contributions
*   **LLM Word Association Dataset**: A large-scale imitation of the Small World of Words (SWOW) dataset by LLMs.
*   **Moral Propagation Algorithm**: Code for mapping Moral Foundations onto semantic networks.

## Authors

[[Chaoyi Xiang]], [[Chunhua Liu]], [[Simon De Deyne]], [[Lea Frermann]]

## Notes


## Tags

#Computer-Science---Computation-and-Language

## Citation Info

13 citations (Semantic Scholar/arXiv) [2025-08-27] 2 citations (Semantic Scholar/DOI) [2025-08-27] 2 citations (Semantic Scholar/DOI) [2025-08-23] arXiv:2505.19674 [cs]
