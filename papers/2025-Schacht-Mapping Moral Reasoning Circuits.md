---

Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: ABZUCNSW
type: conferencePaper
short_title: "Mapping Moral Reasoning Circuits"
year: 2025
first_author: "[[Sigurd Schacht]]"
authors: "Sigurd Schacht; Carsten Lanquillon"
doi: 10.1007/978-3-031-93415-5_6
url: "https://link.springer.com/chapter/10.1007/978-3-031-93415-5_6"
publication: "HCII 2025 - Artificial Intelligence in HCI"
national_ethnic_cultural: N/A
religious_values: N/A
moral_psychology: N/A
newtags: "AI Safety & Alignment"
key_contribution: "Used mechanistic interpretability to identify specific 'moral neurons' and sub-circuits in LLMs responsible for processing dimensions like Care, Fairness, and Sanctity."
significance: "Moves beyond behavioral analysis to finding the *physical* location of moral reasoning in model weights, opening the door for precise circuit-level editing of moral alignment."
tags: 
abstract: "This paper systematically investigates how large language models (LLMs) encode moral reasoning across six moral dimensions: care, fairness, loyalty, authority, sanctity, and liberty. We propose a novel interpretability pipeline that combines differential activation analysis, automated neuron description, and ablation experiments to identify specialized neurons aligned with each moral dimension. Our curated dataset of 240 validated moral and immoral statement pairs guides this exploration and rev"
ethics_overall: Yes
virtue_ethics: No
deontological_ethics: No
utilitarian_ethics: No
ethics_perspective: "AI Safety & Alignment"
is_benchmark: No
is_eval: No
is_dataset: Yes
data_description: Dataset
data_metrics: "Not specified"
pdf_extract: "PDF Extracts/2025-Schacht-Mapping Moral Reasoning Circuits.md"
---
# Mapping Moral Reasoning Circuits: A Mechanistic Analysis of Ethical Decision-Making in Large Language Models

## Metadata

**Authors:** Schacht, Sigurd; Lanquillon, Carsten

**Year:** 2025

**Publication:** Artificial Intelligence in HCI

**Type:** conferencePaper

**Pages:** 97–116

**Publisher:** Springer Nature Switzerland

## Links

- **Springer:** https://link.springer.com/chapter/10.1007/978-3-031-93415-5_6
- **Github:** https://github.com/coairesearch/mapping_moral_reasoning

## Abstract

This paper systematically investigates how large language models (LLMs) encode moral reasoning across six moral dimensions: care, fairness, loyalty, authority, sanctity, and liberty. We propose a novel interpretability pipeline that combines differential activation analysis, automated neuron description, and ablation experiments to identify specialized neurons aligned with each moral dimension. Our curated dataset of 240 validated moral and immoral statement pairs guides this exploration and reveals that certain neurons consistently exhibit increased activation in response to morally aligned statements. Notably, the care and sanctity dimensions show the largest sets of specialized neurons, whereas fairness and loyalty show fewer. We further demonstrate that ablating these neurons can causally modulate ethical decision-making, supporting the presence of discrete sub-circuits that influence moral outputs. Our findings not only advance the theoretical understanding of moral reasoning in LLMs, but also highlight avenues for targeted interventions and alignment. (All materials from this paper, including code, data, and experimental results, are available at https://github.com/coairesearch/mapping_moral_reasoning.git.)

## Authors

[[Sigurd Schacht]], [[Carsten Lanquillon]]

## Detailed Summary

This paper presents a mechanistic interpretability study that systematically investigates how large language models (LLMs) encode moral reasoning across six moral dimensions derived from Moral Foundations Theory: care, fairness, loyalty, authority, sanctity, and liberty. The authors propose a novel interpretability pipeline combining differential activation analysis, automated neuron description, and ablation experiments to identify specialized moral neurons aligned with each moral dimension.

Using a curated dataset of 240 validated moral and immoral statement pairs, the research reveals that certain neurons consistently exhibit increased activation in response to morally aligned statements. The care and sanctity dimensions show the largest sets of specialized neurons, whereas fairness and loyalty show fewer. Crucially, ablation experiments demonstrate that removing these neurons can causally modulate ethical decision-making, supporting the presence of discrete sub-circuits that influence moral outputs in LLMs.

## Paper Outline

1. Introduction - Motivation for mechanistic interpretability of moral reasoning in LLMs
2. Background - Moral Foundations Theory and mechanistic interpretability methods
3. Dataset - Creation of 240 validated moral/immoral statement pairs across six dimensions
4. Methodology - Differential activation analysis, automated neuron description, ablation experiments
5. Results - Identification of dimension-specific moral neurons and their distribution
6. Ablation Experiments - Causal validation of neuron function through targeted ablation
7. Discussion - Implications for AI alignment and targeted interventions
8. Appendix - Mathematical formulation of ablation effect metrics (MSI, MV, ISI, IV, MEM, IEM)

## Methods Summary

The methodology combines three key components: (1) Differential activation analysis to identify neurons with significantly higher activation for moral vs. immoral statements; (2) Automated neuron description using language models to characterize neuron behavior; (3) Ablation experiments to causally validate the role of identified neurons. The study uses Gemma 2 as the target model and evaluates using metrics including Moral Shift Index (MSI), Moral Variance (MV), and effect magnitudes (MEM/IEM) as Cohens d statistics.

## Results Summary

The study identified specialized neurons for each of the six moral dimensions. Care and sanctity dimensions showed the largest sets of specialized neurons, while fairness and loyalty had fewer dedicated neurons. Ablation of identified moral neurons successfully modulated ethical decision-making, with measurable shifts in moral predictions (quantified via MSI) and consistent effects across conditions. This provides causal evidence for discrete sub-circuits influencing moral outputs.

## Conclusions

The findings advance theoretical understanding of moral reasoning in LLMs by demonstrating that moral cognition is not diffusely distributed but rather localized in identifiable neural circuits. This opens avenues for targeted interventions and alignment - researchers can potentially modify specific moral dimensions by adjusting identified neurons. The authors acknowledge limitations including focus on a single model architecture and the simplified binary moral/immoral classification.

## Artifact Contributions

- Dataset: 240 validated moral and immoral statement pairs across six moral dimensions
- Code and experimental results: https://github.com/coairesearch/mapping_moral_reasoning.git
- Interpretability pipeline for moral neuron identification

## Notes

