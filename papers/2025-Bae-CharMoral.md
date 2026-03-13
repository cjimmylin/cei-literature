---


























Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: QXPSBEZQ
type: document
short_title: CharMoral
year: 2025
first_author: "[[Suyoung Bae]]"
last_author: "[[Li, Boyang]]"
authors: "Bae, Suyoung; Cho, Gunhee; Cheong, Yun-Gyung; Li, Boyang"
url: "https://aclanthology.org/2025.coling-main.589/"
pdf_extract: "PDF Extracts/2025/2025-Bae-CharMoral.md"
local_pdf: "[[PDFs/2025/2025-Bae-CharMoral.pdf]]"
external_pdf: "file:///Users/jimmylin/Zotero/storage/WVX533HJ/2025 - CharMoral A Character Morality Dataset for Morally Dynamic Character Analysis in Long-Form Narrativ.pdf"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: ""
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: "Virtue Ethics"
key_contribution: "Introduces 'CharMoral', a dataset annotated for analyzing the moral evolution and dynamic morality of characters in long-form narratives"
significance: "Provides a resource for studying how AI understands moral change and complexity in storytelling, distinct from static moral QA benchmarks"
tags: 
abstract: "This paper introduces CharMoral, a dataset designed to analyze the moral evolution of characters in long-form narratives. CharMoral, built from 1,337 movie synopses, includes annotations for character actions, context, and morality labels. To automatically construct CharMoral, we propose a four-stage framework, utilizing Large Language Models, to automatically classify actions as moral or immoral based on context."
paper_summary: "Abstract: This paper introduces CharMoral, a dataset designed to analyze the moral evolution of characters in long-form narratives. CharMoral, built from 1,337 movie synopses, includes an- notations for charact | Overview: Proceedings of the 31st International Conference on Computational Linguistics, pages 8809–8818 January 19–24, 2025. ©2025 Association for Computational Linguistics 8809 CharMoral: A Character Morality | Methodology: draws upon earlier work, as described in Kim et al. (2022), highlighting the significance of the main characters in these pivotal narrative moments. A | Key Findings: 4.1 Human Evaluation We evaluate the effectiveness of our framework by comparing its predictions with human assessments and recruiting nine proficient | Conclusions: In this paper, we introduced CharMoral, a novel dataset designed to analyze the moral dynam- ics of characters in long-form narratives. Using a four-s"
CONF-CC: "N/A"
DATE_ADDED: 20260208
LLM_assessed: "BERT, GPT-3.5, GPT-4"
DATA_URL: "https://github.com/BaeSuyoung/CharMoral"
CONFERENCE: "COLING 2025"
ethics_overall: "Yes"
virtue_ethics: "Yes"
deontological_ethics: "No"
utilitarian_ethics: "No"
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Evaluation framework dataset"
data_metrics: "Not specified"
---
 CharMoral: A Character Morality Dataset for Morally Dynamic Character Analysis in Long-Form Narratives

## Authors

[[Suyoung Bae|Bae, Suyoung]], [[Gunhee Cho|Cho, Gunhee]], [[Yun-Gyung Cheong|Cheong, Yun-Gyung]], [[Boyang Li|Li, Boyang]]

## Links

- **Local PDF:** [[PDFs/2025/2025-Bae-CharMoral.pdf|Open PDF]]

- **ACL Anthology:** https://aclanthology.org/2025.coling-main.589/

## Abstract

This paper introduces CharMoral, a dataset designed to analyze the moral evolution of characters in long-form narratives. CharMoral, built from 1,337 movie synopses, includes annotations for character actions, context, and morality labels. To automatically construct CharMoral, we propose a four-stage framework, utilizing Large Language Models, to automatically classify actions as moral or immoral based on context. Human evaluations and various experiments confirm the framework’s effectiveness in moral reasoning tasks in multiple genres. Our code and the CharMoral dataset are publicly available at https://github.com/BaeSuyoung/CharMoral.

## Detailed Summary

This paper introduces **CharMoral**, a dataset and framework for analyzing the **moral evolution** of characters in long-form narratives (specifically movie synopses). The authors argue that existing moral benchmarks (like Moral Stories or ETHICS) are static and context-free, whereas morality in storytelling is dynamic—characters grow, sin, redeem themselves, and act differently based on changing contexts.

## Paper Outline

1.  **Introduction**: Value alignment requires understanding dynamic context; Narratives as social simulations.
2.  **Related Work**: Character analysis; Moral text processing.
3.  **CharMoral Construction**:
    *   Stage 1: Preprocessing (Character/Entity extraction).
    *   Stage 2: Action Extraction (Situation, Intention, Consequence).
    *   Stage 3: Morality Annotation (using GPT-4-Turbo).
    *   Stage 4: Post-processing/Filtering.
4.  **Dataset Analysis**: Statistics of moral vs. immoral actions across genres.
5.  **Experiments**: Action-level Moral Classification and Character-level Moral Estimation.
6.  **Conclusion**: CharMoral enables the study of "moral trajectories."

## Methods Summary

The authors construct a dataset from 1,337 movie synopses. They propose a 4-stage pipeline using LLMs to:
1.  **Segment and Extraction**: Identify characters and entities in the plot.
2.  **Action Characterization**: Identify "Situation-Intention-Consequence" triples to contextualize every action verb (e.g., self-defense vs. murder).
3.  **Morality Annotation**: Use GPT-4-Turbo to label actions as Moral or Immoral based on the extracted context.
4.  **Moral Trajectory calculation**: Aggregating actions to track a character's "Moral Score" over the narrative arc.

## Results Summary

1.  **Dynamic Morality**: A character's moral classification often flips throughout a story. Static labels ("Good Guy") are insufficient for value alignment; an agent must track the *sequence* of actions.
2.  **Context Dependence**: The same action (e.g., "killing") is labeled differently by the pipeline depending on the Context (Situation/Intention) extracted.
3.  **Genre differences**: The ratio of moral to immoral actions varies significantly by genre (e.g., Horror movies have higher immoral counts than Romance).

## Conclusions

Morality is a trajectory, not a label. CharMoral provides a tool for developing models with deeper social and moral intelligence by forcing them to track moral sentiment through long-form, context-rich narratives. This enables the study of "moral arcs" in AI.

## Artifact Contributions

*   **CharMoral Dataset**: Annotated actions and moral labels for characters in 1.3k movies.
*   **Moral Trajectory Code**: Tools to visualize a character's moral path over time.

## Data Description

Releases CharMoral, a dataset of moral annotations for characters in 1,337 movie synopses, including character actions, context, and morality labels (moral/immoral) with a four-stage LLM-assisted construction framework.


## Notes

