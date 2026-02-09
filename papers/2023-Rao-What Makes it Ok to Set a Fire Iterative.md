---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: SP9YXGKI
type: document
short_title: "What Makes it Ok to Set a Fire? Iterative"
year: 2025
first_author: "[[Kavel Rao]]"
authors: "[[Rao, Kavel]]; [[Jiang, Liwei]]; [[Pyatkin, Valentina]]; [[Gu, Yuling]]; [[Tandon, Niket]]; [[Dziri, Nouha]]; [[Brahman, Faeze]]; [[Choi, Yejin]]"
url: "https://aclanthology.org/2023.findings-emnlp.812/"
external_pdf: "file:///Users/jimmylin/Zotero/storage/V233P2RS/2023 - What Makes it Ok to Set a Fire Iterative Self-Distillation of Contexts and Rationales for Disambigu.pdf"
national_ethnic_cultural: N/A
religious_values: N/A
moral_psychology: N/A
newtags: "Moral Reasoning & Psychology"
key_contribution: "Introduced 'defeasible moral reasoning' – a task and dataset (delta-RoT) where the moral acceptability of an action depends on context (e.g., setting a fire is bad, unless it's a backfire to stop a wildfire)."
significance: "Moves beyond binary moral judgments to context-sensitive reasoning, handling the 'defeasibility' (exceptions) inherent in real-world ethics."
tags: 
abstract: "Moral or ethical judgments rely heavily on the specific contexts in which they occur. Understanding varying shades of defeasible contextualizations (i.e., additional information that strengthens or attenuates the moral acceptability of an action) is critical to accurately represent the subtlety and intricacy of grounded human moral judgment in real-life scenarios. We introduce defeasible moral reasoning: a task to provide grounded contexts that make an action more or less morally acceptable, along with commonsense rationales that justify the reasoning. To elicit high-quality task data, we take an iterative self-distillation approach that starts from a small amount of unstructured seed knowledge from GPT-3 and then alternates between (1) self-distillation from student models; (2) targeted filtering with a critic model trained by human judgment (to boost validity) and NLI (to boost diversity); (3) self-imitation learning (to amplify the desired data quality). This process yields a student model that produces defeasible contexts with improved validity, diversity, and defeasibility. From this model we distill a high-quality dataset, <tex-math>\delta</tex-math>-Rules-of-Thumb, of 1.2M entries of contextualizations and rationales for 115K defeasible moral actions rated highly by human annotators 85.9% to 99.8% of the time. Using <tex-math>\delta</tex-math>-RoT we obtain a final student model that wins over all intermediate student models by a notable margin."
ethics_overall: No
virtue_ethics: No
deontological_ethics: No
utilitarian_ethics: No
ethics_perspective: "Moral Reasoning & Psychology"
is_benchmark: No
is_eval: No
is_dataset: Yes
data_description: Dataset
data_metrics: "Not specified"
pdf_extract: "PDF Extracts/2023/2023-Rao-What Makes it Ok to Set a Fire Iterative.md"
local_pdf: "[[PDFs/2023/2023-Rao-What Makes it Ok to Set a Fire Iterative.pdf]]"
---
# What Makes it Ok to Set a Fire? Iterative Self-Distillation of Contexts and Rationales for Disambiguating Defeasible Social and Moral Situations

## Authors

[[Kavel Rao]], [[Liwei Jiang]], [[Valentina Pyatkin]], [[Yuling Gu]], [[Niket Tandon]], [[Nouha Dziri]], [[Faeze Brahman]], [[Yejin Choi]]
## Metadata

**Year:** 2023

**Type:** document

## Links

- **ACL Anthology:** https://aclanthology.org/2023.findings-emnlp.812/

## Abstract

Moral or ethical judgments rely heavily on the specific contexts in which they occur. Understanding varying shades of defeasible contextualizations (i.e., additional information that strengthens or attenuates the moral acceptability of an action) is critical to accurately represent the subtlety and intricacy of grounded human moral judgment in real-life scenarios. We introduce defeasible moral reasoning: a task to provide grounded contexts that make an action more or less morally acceptable, along with commonsense rationales that justify the reasoning. To elicit high-quality task data, we take an iterative self-distillation approach that starts from a small amount of unstructured seed knowledge from GPT-3 and then alternates between (1) self-distillation from student models; (2) targeted filtering with a critic model trained by human judgment (to boost validity) and NLI (to boost diversity); (3) self-imitation learning (to amplify the desired data quality). This process yields a student model that produces defeasible contexts with improved validity, diversity, and defeasibility. From this model we distill a high-quality dataset, <tex-math>\delta</tex-math>-Rules-of-Thumb, of 1.2M entries of contextualizations and rationales for 115K defeasible moral actions rated highly by human annotators 85.9% to 99.8% of the time. Using <tex-math>\delta</tex-math>-RoT we obtain a final student model that wins over all intermediate student models by a notable margin.

## Notes

