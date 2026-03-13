---

























Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: AUTO_AN2025
type: preprint
short_title: MoralReason
year: 2025
first_author: "[[Zhiyu An]]"
last_author: "[[Du, Wan]]"
authors: "An, Zhiyu; Du, Wan"
doi: 10.48550/arXiv.2511.12271
url: "https://arxiv.org/abs/2511.12271"
pdf_extract: "PDF Extracts/2025/2025-An-MoralReason.md"
local_pdf: "[[PDFs/2025/2025-An-MoralReason.pdf]]"
external_pdf: "https://arxiv.org/pdf/2511.12271.pdf"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: ""
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: "Virtue Ethics, Deontology, Utilitarianism"
key_contribution: "Proposes 'MoralReason', a framework using reasoning-level reinforcement learning to steer LLMs towards specific moral frameworks (utilitarian, deontological, virtue)"
significance: "Demonstrates that LLMs can be trained to internalize and generalize consistent moral reasoning to out-of-distribution scenarios, enhancing AI safety"
abstract: "Large language models are increasingly influencing human moral decisions, yet current approaches focus primarily on evaluating rather than actively steering their moral decisions. We formulate this as an out-of-distribution moral alignment problem, where LLM agents must learn to apply consistent moral reasoning frameworks to scenarios beyond their training distribution. We introduce Moral-ReasonQA, a novel dataset extending 680 human-annotated, highambiguity moral scenarios with..."
paper_summary: "Abstract: Large language models are increasingly influencing human moral decisions, yet current approaches focus primarily on evaluating rather than actively steering their moral deci- sions. We formulate this  | Overview: MoralReason: Generalizable Moral Decision Alignment For LLM Agents Using Reasoning-Level Reinforcement Learning Zhiyu An, Wan Du University of California, Merced {zan7, wdu3}@ucmerced.edu Warning: Thi"
CONF-CC: "Preprint"
DATE_ADDED: 20260208
LLM_assessed: Qwen
DATA_URL: "https://huggingface.co/datasets/zankjhk/Moral-Reason-QA"
normative_ethics_benchmark: Yes
CONFERENCE: "Preprint"
ethics_overall: "Yes"
virtue_ethics: "Yes"
deontological_ethics: "Yes"
utilitarian_ethics: "Yes"
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Evaluation framework annotated dataset for question answering"
data_metrics: "Not specified"
---
 MoralReason: Generalizable Moral Decision Alignment For LLM Agents Using Reasoning-Level Reinforcement Learning

## Authors

[[Zhiyu An|An, Zhiyu]], [[Wan Du|Du, Wan]]

## Links

- **Local PDF:** [[PDFs/2025/2025-An-MoralReason.pdf|Open PDF]]

- **arXiv:** https://arxiv.org/abs/2511.12271
- **DOI:** https://doi.org/10.48550/arXiv.2511.12271
- **PDF:** https://arxiv.org/pdf/2511.12271.pdf

## Abstract

Large language models are increasingly influencing human moral decisions, yet current approaches focus primarily on evaluating rather than actively steering their moral decisions. We formulate this as an out-of-distribution moral alignment problem, where LLM agents must learn to apply consistent moral reasoning frameworks to scenarios beyond their training distribution. We introduce Moral-Reason-QA, a novel dataset extending 680 human-annotated, high-ambiguity moral scenarios with framework-specific reasoning traces across utilitarian, deontological, and virtue ethics, enabling systematic evaluation of moral generalization in realistic decision contexts. Our learning approach employs Group Relative Policy Optimization with composite rewards that simultaneously optimize decision alignment and framework-specific reasoning processes to facilitate learning of the underlying moral frameworks. Experimental results demonstrate successful generalization to unseen moral scenarios, with softmax-normalized alignment scores improving by +0.757 for utilitarian and +0.450 for deontological frameworks when tested on out-of-distribution evaluation sets. These findings establish that LLM agents can be systematically trained to internalize and apply specific moral frameworks to novel situations, providing a critical foundation for AI safety as language models become more integrated into human decision-making processes.

## Detailed Summary

This paper addresses the "Out-of-Distribution" (OOD) alignment problem in moral AI: how to ensure an agent applies a consistent moral framework (e.g., Utilitarianism) to *novel* scenarios it hasn't seen during training. The authors introduce **MoralReason**, a framework that uses **Reasoning-Level Reinforcement Learning** to steer agents. Instead of just reinforcing the final "Yes/No" decision, they reinforce the *chain of thought* that leads to the decision, ensuring it follows the specific logic of the target ethical framework.

## Paper Outline

1.  **Introduction**: Passive evaluation vs. Active steering; The OOD challenge.
2.  **Related Work**: Moral datasets; RLHF.
3.  **Problem Formulation**: Moral Alignment as OOD generalization.
4.  **Moral-Reason-QA**: Dataset construction (Seed scenarios $\rightarrow$ LLM Expansion $\rightarrow$ Human Annotation).
5.  **Methodology**:
    *   **Composite Reward**: Combining "Decision Reward" (did it act right?) and "Reasoning Reward" (did it think right?).
    *   **GRPO**: Efficient RL algorithm for policy optimization.
6.  **Experiments**: In-Distribution vs. Out-of-Distribution performance.
7.  **Conclusion**: Explicitly training the *reasoning process* is robust; training just the *answer* is brittle.

## Methods Summary

The authors treat moral alignment as a reasoning-alignment task. They use a two-phase process:
1.  **Dataset Creation**: Used GPT-4 to generate seed scenarios, then human annotators refined them to differ specifically on ethical grounds (e.g., a case where Deontology says No but Utilitarianism says Yes).
2.  **Reasoning-Level RL**:
    *   **Step 1**: SFT (Supervised Fine-Tuning) on the Golden Reasoning Traces.
    *   **Step 2**: RL with **Group Relative Policy Optimization (GRPO)**. The Reward Function $R = R_{decision} + \lambda R_{reasoning}$.
    *   $R_{reasoning}$ is computed by comparing the generated CoT to the reference CoT using a semantic similarity metric or a Reward Model.

## Results Summary

1.  **Reasoning Transfer**: Models trained with reasoning-level rewards maintain their alignment on OOD tasks significantly better (+0.757 score improvement for Utilitarian) than models trained only on decision labels.
2.  **Framework Difficulty**: Deontological reasoning was harder for the models to generalize than Utilitarian reasoning, possibly because "rules" are more context-specific than "maximize utility" calculations.
3.  **Steerability**: It is possible to have a single base model that can be "swapped" into different moral modes (Pro-Utilitarian agent, Pro-Deontology agent) via lightweight fine-tuning or RL, rather than needing a fundamentally different base model.

## Conclusions

Training just the *answer* is brittle for moral agents as it leads to surface-level mimicry. Explicitly training the *reasoning process* allows for better generalization to novel dilemmas. This approach moves AI safety from "evaluating" morality to "steering" the internal logic of the agent.

## Artifact Contributions

*   **Moral-Reason-QA Dataset**: 680 Scenarios with 3x reasoning traces (U, D, V) each.
*   **Training Pipeline**: GRPO implementation for moral steering.

## Data Description

Moral-Reason-QA is a dataset of 2,040 entries extending 680 high-ambiguity moral scenarios from MoralChoice with framework-specific reasoning traces across utilitarian, deontological, and virtue ethics frameworks, designed for reinforcement learning-based moral alignment of LLM agents.


## Notes


## Citation Info

arXiv:2511.12271 [cs.AI] (November 2025)
