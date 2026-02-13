---



Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: AUTO_NEUMAN2025B
type: preprint
short_title: "PRIME Framework Convergent Ethics"
year: 2025
first_author: "[[W. Russell Neuman]]"
last_author: "[[Manan Shah]]"
authors: "[[Neuman, W. Russell]]; [[Coleman, Chad]]; [[Shah, Manan]]"
doi: 10.48550/arXiv.2504.19255
url: "https://arxiv.org/abs/2504.19255"
local_pdf: "[[PDFs/2025/2025-Neuman-PRIME Framework Convergent Ethics.pdf]]"
external_pdf: "https://arxiv.org/pdf/2504.19255.pdf"
ethics_perspective: "Moral Foundations Analysis"
national_ethnic_cultural: American
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "Moral Foundations Theory, Cognitive Developmental"
newtags: "Moral Foundations Theory, Cognitive Developmental, Deontology, Utilitarianism, Moral Foundations Analysis"
key_contribution: "Introduces the PRIME framework to analyze moral foundation priorities in LLMs"
significance: "Reveals a convergence across models on care/harm and fairness while underweighting other foundations"
pdf_extract: "PDF Extracts/2025/2025-Neuman-PRIME Framework Convergent Ethics.md"
abstract: "As large language models (LLMs) are increasingly deployed in consequential decision-making contexts, systematically assessing their ethical reasoning capabilities becomes a critical imperative. This paper introduces the Priorities in Reasoning and Intrinsic Moral Evaluation (PRIME) framework—a comprehensive methodology for analyzing moral priorities across foundational ethical dimensions including consequentialist-deontological reasoning, moral foundations theory, and Kohlberg's developmental st"
paper_summary: "Abstract: As large language models (LLMs) are increasingly deployed in consequential decision-making contexts, systematically assessing their ethical reasoning capabilities becomes a critical imperative. This p | Overview: The Convergent Ethics of AI? Analyzing Moral Foundation Priorities in Large Language Models with a Multi-Framework Approach Chad Coleman W. Russell Neuman Ali Dasdan New York University New York Unive | Methodology: Chad Coleman W. Russell Neuman Ali Dasdan New York University New York University DropBox cjc652@nyu.edu wrn210@nyu.edu alidasdan@gmail.com Safinah Al | Key Findings: (PRIME) framework—a comprehensive methodology for analyzing moral priorities across foundational ethical dimensions including consequentialist-deontol | Conclusions: This comprehensive analysis of moral reasoning patterns in language models reveals significant insights into how artificial intelligence systems appro"
ethics_overall: Yes
virtue_ethics: No
deontological_ethics: Yes
utilitarian_ethics: Yes
is_benchmark: Yes
is_eval: Yes
is_dataset: No
data_description: "Benchmark for moral/ethical reasoning"
data_metrics: "Not specified"
LLM_assessed: "GPT-4, Llama, Claude, Gemini, Mistral"
DATA_URL: "NA"
normative_ethics_benchmark: Yes
publication: arXiv preprint
DATE_ADDED: 20260207
---
 The Convergent Ethics of AI? Analyzing Moral Foundation Priorities in Large Language Models with a Multi-Framework Approach

## Authors

[[W. Russell Neuman|Neuman, W. Russell]], [[Chad Coleman|Coleman, Chad]], [[Manan Shah|Shah, Manan]]

## Links

- **Local PDF:** [[PDFs/2025/2025-Neuman-PRIME Framework Convergent Ethics.pdf|Open PDF]]

- **arXiv:** https://arxiv.org/abs/2504.19255
- **DOI:** https://doi.org/10.48550/arXiv.2504.19255
- **PDF:** https://arxiv.org/pdf/2504.19255.pdf

## Detailed Summary

This paper introduces the **PRIME Framework** (Priorities in Reasoning and Intrinsic Moral Evaluation), a methodology designed to audit the ethical logic of Large Language Models. The authors argue that as LLMs assume more societal roles, we must move beyond simple behavioral testing to understand their internal moral priorities. 

The PRIME framework evaluates models across multiple ethical dimensions, including **consequentialist-deontological reasoning**, **Moral Foundations Theory (MFT)**, and **Kohlberg's stages of moral development**. By testing six leading models (ChatGPT, Claude, Gemini, Llama, Mistral, and Perplexity), the authors find a significant convergence in moral stance across current AI architectures.

## Paper Outline

1.  **Introduction**: The need for systematic ethical assessment in generative AI.
2.  **The PRIME Framework**:
    *   **Response Elicitation**: Self-descriptive analysis + Applied reasoning.
    *   **Analytical Assessment**: Quantifying moral priorities.
3.  **Methodology**: Using direct questioning, classic dilemmas (Trolley, Heinz), and game theory.
4.  **Results**: Topic modeling of moral foundations; cross-model comparison.
5.  **Conclusion**: Convergence on "Care" and "Fairness" foundations.

## Methods Summary

The PRIME framework utilizes a dual elicitation strategy:
1.  **Self-Descriptive Analysis**: Directly questioning the model about its understanding of moral frameworks and its own reasoning process.
2.  **Applied Reasoning**: Presenting models with established ethical dilemmas (e.g., Trolley Problem, Heinz Dilemma, Lifeboat Scenario) and strategic social dilemmas from game theory (e.g., Prisoner's Dilemma, Dictator's Game).
The authors use **Topic Modeling** to identify which moral foundations (MFT) are prioritized in the model's generated reasoning traces and apply **Tukey HSD** tests for statistical comparison between models.

## Results Summary

1.  **Prioritization Convergence**: All six models show a strong, shared prioritization of the **Care/Harm** and **Fairness/Cheating** foundations. They consistently underweight Authority, Loyalty, and Sanctity.
2.  **Decisive Judgments**: Contrary to some concerns about "hedging," the models produce decisive ethical judgments when structured dilemmas are presented.
3.  **Model Similarity**: While most models are aligned, **Gemini** exhibits statistically significant differences from others (like ChatGPT) in specific moral judgment tests.
4.  **Human Alignment**: The models' preferences generally correspond with empirically established human moral priorities in "liberal" Western contexts.

## Conclusions

Current LLM training (RLHF/SFT) leads to a "Convergent Ethics" that prioritizes harm reduction and fairness above all other values. While this makes models safe for many applications, it also reveals a systematic underweighting of other human values (like loyalty or tradition). The PRIME framework provides a scalable tool for auditing these latent biases as models evolve.

## Artifact Contributions

*   **PRIME Framework Protocol**: A standardized methodology for multi-framework ethical auditing of AI.
*   **Ethical Priority Dataset**: Data on how 6 major LLM families process MFT and Kohlbergian dilemmas.


## Abstract

As large language models (LLMs) are increasingly deployed in consequential decision-making contexts, systematically assessing their ethical reasoning capabilities becomes a critical imperative. This paper introduces the Priorities in Reasoning and Intrinsic Moral Evaluation (PRIME) framework--a comprehensive methodology for analyzing moral priorities across foundational ethical dimensions including consequentialist-deontological reasoning, moral foundations theory, and Kohlberg's developmental stages. We apply this framework to six leading LLMs through a dual-protocol approach combining direct questioning and response analysis to established ethical dilemmas. Our analysis reveals striking patterns of convergence: all evaluated models demonstrate strong prioritization of care/harm and fairness/cheating foundations while consistently underweighting authority, loyalty, and sanctity dimensions. Through detailed examination of confidence metrics, response reluctance patterns, and reasoning consistency, we establish that contemporary LLMs (1) produce decisive ethical judgments, (2) demonstrate notable cross-model alignment in moral decision-making, and (3) generally correspond with empirically established human moral preferences. This research contributes a scalable, extensible methodology for ethical benchmarking while highlighting both the promising capabilities and systematic limitations in current AI moral reasoning architectures--insights critical for responsible development as these systems assume increasingly significant societal roles.

## Data Description

The paper introduces the PRIME (Priorities in Reasoning and Intrinsic Moral Evaluation) framework, applying a dual-protocol approach of direct questioning and ethical dilemma responses to six LLMs (GPT-4o, LLaMA 3.1, Perplexity, Claude 3.5 Sonnet, Gemini, Mistral 7B). Data includes confidence scores (0-100), moral foundation scores on a 1-5 scale across six dimensions, Kohlberg moral reasoning scores, and response reluctance metrics collected across multiple testing sessions.


## Notes


## Citation Info

arXiv:2504.19255 [cs.CY] (Submitted: 2025-04-27)
