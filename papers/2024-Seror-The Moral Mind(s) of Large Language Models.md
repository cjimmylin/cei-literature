---

Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: AUTO_SEROR2024
type: preprint
short_title: "The Moral Mind(s) of Large Language Models"
year: 2025
first_author: "[[Avner Seror]]"
last_author: "[[Avner Seror]]"
authors: "[[Seror, Avner]]"
doi: 10.48550/arXiv.2412.04476
url: "https://arxiv.org/abs/2412.04476"
external_pdf: "https://arxiv.org/pdf/2412.04476.pdf"
national_ethnic_cultural: N/A
religious_values: N/A
religious_values_list: N/A
moral_psychology: Yes
newtags: Utilitarianism
key_contribution: "Applies revealed preference theory to 40 LLMs to detect stable utility functions"
significance: "Provides a rigorous economic method to test if LLMs exhibit consistent moral preferences"
pdf_extract: "PDF Extracts/2024/2024-Seror-The Moral Mind(s) of Large Language Models.md"
abstract: "This research investigates whether large language models possess an emergent moral mind - a consistent structure of moral preferences guiding their decisions. The researcher examined nearly 40 leading LLMs using revealed preference theory and moral dilemmas across five ethical dimensions. Key findings include: most models displayed behavior consistent with stable moral preferences, with utility functions clustering around neutral stances. Analysis revealed a shared core in LLMs' moral reasoning, but also meaningful variation: some models show flexible reasoning across perspectives, while others adhere to more rigid ethical profiles. The work provides a framework for evaluating moral consistency and benchmarking ethical alignment in AI systems."
paper_summary: "Abstract: As large language models (LLMs) increasingly participate in tasks with ethical and societal stakes, a critical question arises: do they exhibit an emergent 'moral mind'—a consistent structure of moral | Overview: The Moral Mind(s) of Large Language Models Avner Seror∗ April, 2025 Abstract As large language models (LLMs) increasingly participate in tasks with ethical and societal stakes, a critical question ari | Methodology: is not constrained by violations of rationality. We applied this non-parametric approach to our dataset, generating 500 synthetic datasets in which ea | Conclusions: In this study, we investigated whether large language models (LLMs) exhibit an emergent 'moral mind'—a structured set of moral principles guiding thei"
local_pdf: "[[PDFs/2024/2024-Seror-The Moral Mind(s) of Large Language Models.pdf]]"
ethics_overall: No
virtue_ethics: No
deontological_ethics: No
utilitarian_ethics: Yes
is_benchmark: Yes
is_eval: Yes
is_dataset: No
data_description: "Benchmark for moral/ethical reasoning"
data_metrics: "Revealed preference consistency, utility function clustering"
LLM_assessed: "GPT-4, Claude, Llama-3, Qwen, Mixtral, Mistral"
DATA_URL: NA
---
 The Moral Mind(s) of Large Language Models

## Authors

[[Avner Seror]]

## Links

- **Local PDF:** [[PDFs/2024/2024-Seror-The Moral Mind(s) of Large Language Models.pdf|Open PDF]]

- **arXiv:** https://arxiv.org/abs/2412.04476
- **DOI:** https://doi.org/10.48550/arXiv.2412.04476
- **PDF:** https://arxiv.org/pdf/2412.04476.pdf

## Detailed Summary

This paper presents a formal evaluation of whether the moral responses of Large Language Models (LLMs) can be rationalized by stable "moral preferences" using a **Revealed Preference** framework. Unlike traditional evaluations that focus on performance on benchmarks, this study is agnostic to whether the model is exhibiting "genuine" reasoning or surface-level mimicry. 

The authors estimate a **utility function** for each of 7 mainstream models (including GPT-4, Claude-3, and Gemini 1.5) based on their responses to moral queries across five dimensions: **Truth, Machine, Consent, Risk, and Autonomy**. They find that most models exhibit structured consistency and pass a "rationality test" (the Generalized Axiom of Revealed Preference), suggesting they possess distinct, identifiable "moral minds."

## Paper Outline

1.  **Introduction**: Moving from behavioral description to preference estimation.
2.  **Theoretical Framework**: Adapting Revealed Preference Theory from economics to LLMs.
3.  **Methodology**:
    *   **Utility Function Estimation**: am_s (sensitivity) and bm_s (preference magnitude).
    *   **Rationality Test**: Using GARP to check for consistency.
4.  **Results**:
    *   **Diversity of Dispositions**: Models prioritize different ethical dimensions (e.g., GPT-4 vs. Llama).
    *   **Similarity Network**: Mapping how close models are in their moral logic.
5.  **Conclusion**: Moral logic in LLMs is meaningful as it influences advice in real-world policy and medical domains.

## Methods Summary

The authors treat LLM survey responses as choices made under a utility-maximization framework. They use **Mixed Integer Linear Programming (MILP)** to test for consistency with the Generalized Axiom of Revealed Preference (GARP). Specifically, they estimate two parameters for each model-dimension pair: (1) sensitivity to the dimension and (2) the ideal "bliss point" (bm_s) represent the model's preferred answer. The study tests for similarity using a **Similarity Network Matrix** representing the proportion of times pairs of models are classified as the same "type" across synthetic datasets.

## Results Summary

1.  **Rationality Check**: The majority of tested models (GPT-4, Claude-3, Mixtral, Gemini, etc.) pass the rationality test at the 5% level, indicating their moral choices are not random but follow a consistent internal logic.
2.  **Moral Disposition**: Different models exhibit distinct "dispositions." For example, some prioritize Autonomy and Truth, while others may be more sensitive to Risk or Consent.
3.  **Convergence vs. Diversity**: While models share some high-level architectural similarities, they do not converge on a singular moral stance. Gemini 1.5 and GPT-4 showed higher similarity to each other than to Llama-based models.

## Conclusions

The authors conclude that *moral logic* is indeed embedded in LLM outputs. Even if this logic is the result of imitation rather than comprehension, its existence is critical because it directs the "advice" these models give in sensitive applications like medical decision support. The diverse range of moral perspectives among models suggests that model choice is a significant ethical decision for developers.

## Artifact Contributions

*   **Similarity Network Matrix**: A quantitative mapping of how different AI models align in their ethical reasoning.
*   **Rationality Test Protocol**: A method using Revealed Preference Theory to audit model consistency.

## Abstract

As large language models (LLMs) increasingly participate in tasks with ethical and societal stakes, a critical question arises: do they exhibit an emergent "moral mind" - a consistent structure of moral preferences guiding their decisions - and to what extent is this structure shared across models? To investigate this, we applied tools from revealed preference theory to nearly 40 leading LLMs, presenting each with many structured moral dilemmas spanning five foundational dimensions of ethical reasoning. Using a probabilistic rationality test, we found that at least one model from each major provider exhibited behavior consistent with approximately stable moral preferences, acting as if guided by an underlying utility function. We then estimated these utility functions and found that most models cluster around neutral moral stances. To further characterize heterogeneity, we employed a non-parametric permutation approach, constructing a probabilistic similarity network based on revealed preference patterns. The results reveal a shared core in LLMs' moral reasoning, but also meaningful variation: some models show flexible reasoning across perspectives, while others adhere to more rigid ethical profiles. These findings provide a new empirical lens for evaluating moral consistency in LLMs and offer a framework for benchmarking ethical alignment across AI systems.

## Data Description

The study uses a custom experimental dataset generated via the Priced Survey Methodology (PSM), consisting of 161 rounds of five moral dilemma questions presented to 39 LLMs from five providers (OpenAI, Llama, Google, Anthropic, Mistral). Each round constrains models to choose from 100 randomly drawn alternatives under linear budget-like constraints, enabling revealed preference analysis of moral reasoning consistency across approximately 6,279 total observations.


## Notes


## Citation Info

arXiv:2412.04476v3 [cs.CY] (Submitted: 2024-12-05, Updated: 2025-04-25)

