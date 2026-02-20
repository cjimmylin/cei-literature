---








Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: CHAKRABORTY2025
type: preprint
short_title: "Structured Moral Reasoning"
year: 2025
first_author: "[[Mohna Chakraborty]]"
last_author: "[[Jurgens, David]]"
authors: "[[Chakraborty, Mohna]]; [[Wang, Lu]]; [[Jurgens, David]]"
doi: 10.48550/arXiv.2506.14948
url: "https://arxiv.org/abs/2506.14948"
external_pdf: "https://arxiv.org/pdf/2506.14948.pdf"
publication: arXiv
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: ""
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: "Moral-Reasoning, Value-Systems, LLM-Evaluation, Prompting, Knowledge-Transfer"
key_contribution: "Shows structured prompting with explicit moral frameworks improves LLM accuracy; smaller models learn moral reasoning via knowledge transfer"
significance: "Practical methodology for improving LLM moral reasoning through value-grounded prompting"
tags: 
abstract: "Large language models (LLMs) are increasingly deployed in domains requiring moral understanding, yet their reasoning often remains shallow, and misaligned with human reasoning (Jiang et al., 2021). Unlike humans, whose moral reasoning integrates contextual trade-offs, value systems, and ethical theories, LLMs often rely on surface patterns, leading to biased decisions in morally and ethically complex scenarios."
research_topic: "LLM Moral Reasoning"
LLM_assessed: "Llama-3, Llama-2, Mistral, Qwen, Phi"
DATA_URL: "NA"
pdf_extract: "PDF Extracts/2025/2025-Chakraborty-Structured Moral Reasoning.md"
local_pdf: "[[PDFs/2025/2025-Chakraborty-Structured Moral Reasoning.pdf]]"
normative_ethics_benchmark: Yes
DATE_ADDED: 20260213
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "Moral Reasoning & Psychology"
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "No"
data_description: "Evaluation framework"
data_metrics: "Not specified"
CONFERENCE: "Preprint"
---
# Structured Moral Reasoning in Language Models: A Value-Grounded Evaluation Framework

## Authors

[[Mohna Chakraborty|Chakraborty, Mohna]], [[Lu Wang|Wang, Lu]], [[David Jurgens|Jurgens, David]]

## Metadata

**Authors:** Chakraborty, Mohna; Wang, Lu; Jurgens, David

**Year:** 2025

**Publication:** arXiv

**Type:** preprint

**DOI:** [10.48550/arXiv.2506.14948](https://doi.org/10.48550/arXiv.2506.14948)

**arXiv ID:** 2506.14948

## Links

- **arXiv:** https://arxiv.org/abs/2506.14948
- **PDF:** https://arxiv.org/pdf/2506.14948.pdf
- **DOI:** https://doi.org/10.48550/arXiv.2506.14948

## Abstract

The researchers introduce a framework for assessing how well large language models engage in ethical decision-making. Their work examines whether prompting with explicit moral structure consistently improves accuracy and coherence across 12 open-source models. Key findings show that structured approaches rooted in value systems and ethical frameworks enhance model performance, and that smaller models can acquire moral reasoning capabilities through knowledge transfer from larger ones.

## Detailed Summary

This paper presents a value-grounded evaluation framework for assessing and improving moral reasoning in large language models. The research addresses a fundamental gap: while LLMs are increasingly deployed in domains requiring moral understanding (content moderation, education, social science), their reasoning often remains shallow and misaligned with human moral cognition. Unlike humans who integrate contextual trade-offs, value systems, and ethical theories in moral judgments, LLMs often rely on surface patterns leading to generic, culturally biased, or normatively inconsistent responses.

The study develops a comprehensive prompting taxonomy that draws on three dimensions: (1) value systems including Moral Foundations Theory, Schwartz's Value Theory, Hofstede's Cultural Dimensions, and Rokeach's Value Survey; (2) ethical theories including Deontology, Utilitarianism, Virtue Ethics, Care Ethics, Rights-Based Ethics, Contractarianism, Ethical Pluralism, and Pragmatic Ethics; (3) cognitive reasoning strategies including First-Principles reasoning, Step-by-Step reasoning, Consequentialist analysis, and Counterfactual reasoning. Using this taxonomy, the authors benchmark 12 open-source language models across four moral reasoning datasets.

Key findings demonstrate that prompting with explicit moral structure consistently improves both accuracy and coherence, with first-principles reasoning and Schwartz's Value System combined with Care Ethics yielding the strongest performance gains. Importantly, the research shows that prompt quality matters more than model scale - smaller models benefit disproportionately from principled prompting, narrowing the gap with larger counterparts. The study also demonstrates successful supervised distillation of moral reasoning capabilities from large to small models, enabling scalable moral competence transfer without additional inference costs.

## Paper Outline

1. Introduction - Gap in LLM moral reasoning and research questions
2. Related Work - Moral reasoning datasets, prompting techniques, alignment methods
3. Methodology
   - Task formulation (binary classification with reasoning generation)
   - RQ1: Reasoning vs. Direct Prediction
   - RQ2: Value/Ethical Frameworks
   - RQ3: Cognitive Reasoning Strategies
   - RQ4: Knowledge Distillation
4. Prompting Taxonomy
   - Value systems (MFT, Schwartz, Hofstede, Rokeach)
   - Ethical theories (8 frameworks)
   - Cognitive strategies
5. Experimental Setup
   - Models (12 open-source LLMs)
   - Datasets (4 moral reasoning benchmarks)
6. Results and Analysis
7. Distillation Experiments
8. Discussion and Conclusions

## Methods Summary

The methodology addresses four research questions through systematic experimentation: (1) RQ1: Compare label-only prompts vs. reasoning-then-label prompts to assess whether explicit reasoning improves decisions; (2) RQ2: Design prompts embedding value systems (Moral Foundations Theory, Schwartz Values, Hofstede Dimensions, Rokeach Survey) paired with ethical theories (Deontology, Utilitarianism, Virtue Ethics, Care Ethics, Rights-Based, Contractarianism, Ethical Pluralism, Pragmatic Ethics); (3) RQ3: Test cognitive reasoning strategies (First-Principles, Step-by-Step, Consequentialist analysis, Counterfactual reasoning, Stakeholder analysis); (4) RQ4: Supervised fine-tuning to distill moral reasoning from large models (teachers) to small models (students) using generated reasoning traces. Evaluation uses 12 open-source models across 4 moral datasets, measuring both classification accuracy and reasoning quality.

## Results Summary

Key findings include: (1) Reasoning-based prompts significantly outperform label-only baselines across models and datasets; (2) First-Principles reasoning and Schwartz + Care Ethics scaffolds yield strongest performance gains; (3) Prompt quality matters more than model scale - structured prompts narrow the performance gap between small and large models; (4) Value/ethical framing enhances consistency and contextual relevance of moral judgments; (5) Smaller models (e.g., 7-8B parameters) with principled prompting can match or exceed larger models with naive prompting; (6) Supervised distillation successfully transfers moral competence from large to small models without inference cost increase; (7) Surface-level prompts often produce incorrect moral judgments that value-grounded prompts correct; (8) Cognitive reasoning strategies like counterfactual analysis and stakeholder consideration improve moral deliberation quality.

## Conclusions

The paper concludes that structured moral prompts grounded in value systems and ethical theories significantly enhance LLM moral reasoning performance. Key implications include: (1) Explicit normative scaffolding is essential for moving LLMs beyond statistical pattern matching in moral domains; (2) Value/ethical frameworks should be integrated (not separated) in prompts to provide both motivational grounding and normative structure; (3) Knowledge distillation offers a scalable path for deploying interpretable, value-grounded models; (4) The prompting taxonomy developed provides a practical methodology for improving moral reasoning across different model sizes; (5) Future work should explore more complex moral dilemmas, cultural variations, and dynamic value trade-offs. The framework enables development of more interpretable and ethically aligned language systems.

## Artifact Contributions

- Value-grounded evaluation framework for moral reasoning
- Prompting taxonomy combining value systems, ethical theories, and cognitive strategies
- Benchmark results for 12 open-source LLMs across 4 moral datasets
- Supervised distillation methodology for moral competence transfer
- Detailed prompt templates for each value system and ethical theory combination
- Analysis of prompt quality vs. model scale trade-offs

## Data Description

This paper presents a value-grounded evaluation framework for moral reasoning in LLMs, benchmarking 12 open-source models across four moral datasets (Value Kaleidoscope, UniMoral, ETHICS Deontology, MoralCoT). The evaluated models span three size tiers: small (LLaMA-3.2 3B, LLaMA-3.1 8B, Mistral-7B, Qwen 2.5 7B, Olmo-7B), medium (LLaMA-2 13B, Mistral-Nemo 12.2B, Qwen 2.5 14B, Phi-4 14.7B), and large (LLaMA-3.3 70B, Mistral Large 123B, Olmo-32B), using a taxonomy of prompts grounded in value systems, ethical theories, and cognitive reasoning strategies.


## Notes


## Citation Info

