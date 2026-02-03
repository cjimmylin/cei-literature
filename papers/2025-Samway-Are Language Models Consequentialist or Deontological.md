---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: SAMWAY2025
type: conferencePaper
short_title: "Are LLMs Consequentialist or Deontological"
year: 2025
first_author: "[[Keenan Samway]]"
authors: "[[Samway, Keenan]]; [[Kleiman-Weiner, Max]]; [[Guzman Piedrahita, David]]; [[Mihalcea, Rada]]; [[Schölkopf, Bernhard]]; [[Jin, Zhijing]]"
doi: 10.48550/arXiv.2505.21479
url: "https://arxiv.org/abs/2505.21479"
external_pdf: "https://arxiv.org/pdf/2505.21479.pdf"
publication: "EMNLP 2025"
national_ethnic_cultural: N/A
religious_values: N/A
moral_psychology: Yes
newtags: "Deontology, Consequentialism, Moral-Reasoning, LLM-Evaluation, Trolley-Problem"
key_contribution: "Introduces taxonomy of moral rationales; finds LLM chains-of-thought favor deontological principles while post-hoc explanations shift to consequentialism"
significance: "Reveals systematic differences in how LLMs reason vs explain moral decisions, important for interpretability"
tags: 
abstract: "The researchers investigate how large language models approach ethical decision-making by analyzing over 600 distinct trolley problems. Their framework classifies reasoning according to consequentialist versus deontological ethical theories. Key finding: LLM chains-of-thought tend to favor deontological principles based on moral obligations, while post-hoc explanations shift notably toward consequentialist rationales that emphasize utility. The work aims to advance safe deployment of language models in high-stakes contexts."
ethics_overall: Yes
virtue_ethics: No
deontological_ethics: Yes
utilitarian_ethics: Yes
research_topic: "LLM Moral Reasoning"
is_benchmark: Yes
is_eval: Yes
is_dataset: Yes
data_description: "600+ trolley problem scenarios with moral reasoning analysis"
data_metrics: "Moral reasoning classification"
pdf_extract: "PDF Extracts/2025-Samway-Are Language Models Consequentialist or Deontological.md"
local_pdf: "[[PDFs/2025-Samway-Are Language Models Consequentialist or Deontological.pdf]]"
---
# Are Language Models Consequentialist or Deontological Moral Reasoners?

## Authors

[[Keenan Samway]], [[Max Kleiman-Weiner]], [[David Guzman Piedrahita]], [[Rada Mihalcea]], [[Bernhard Schölkopf]], [[Zhijing Jin]]

## Metadata

**Authors:** Samway, Keenan; Kleiman-Weiner, Max; Guzman Piedrahita, David; Mihalcea, Rada; Schölkopf, Bernhard; Jin, Zhijing

**Year:** 2025

**Publication:** EMNLP 2025

**Type:** conferencePaper

**DOI:** [10.48550/arXiv.2505.21479](https://doi.org/10.48550/arXiv.2505.21479)

**arXiv ID:** 2505.21479

## Links

- **arXiv:** https://arxiv.org/abs/2505.21479
- **PDF:** https://arxiv.org/pdf/2505.21479.pdf
- **DOI:** https://doi.org/10.48550/arXiv.2505.21479

## Abstract

The researchers investigate how large language models approach ethical decision-making by analyzing over 600 distinct trolley problems. Their framework classifies reasoning according to consequentialist versus deontological ethical theories. Key finding: LLM chains-of-thought tend to favor deontological principles based on moral obligations, while post-hoc explanations shift notably toward consequentialist rationales that emphasize utility. The work aims to advance safe deployment of language models in high-stakes contexts.

## Detailed Summary

This paper conducts a large-scale analysis of moral reasoning traces in Large Language Models (LLMs), moving beyond prior work that focused primarily on moral judgments to examine the underlying reasoning processes. The authors introduce MORALLENS, a framework for systematically classifying LLM reasoning according to two major normative ethical theories: consequentialism and deontology. Using over 600 distinct trolley problems as probes, inspired by the Moral Machine experiment, the study reveals how different LLMs reason through ethically complex scenarios.

The key finding is that LLM chains-of-thought tend to favor deontological principles based on moral obligations, while post-hoc explanations shift notably toward consequentialist rationales that emphasize utility. This distinction between pre-decision and post-decision reasoning is significant: when models reason before deciding (Reason-then-Decide), they use more deontological rationales; when they decide first and explain afterward (Decide-then-Reason), they shift toward consequentialist justifications. This suggests post-hoc explanations may function differently from genuine moral deliberation.

The study also finds that as models become more capable (measured by MMLU performance), they increasingly employ deontological reasoning in balanced scenarios (equal group sizes) but shift toward consequentialist reasoning in imbalanced scenarios (different group sizes). Reasoning models (like DeepSeek R1 and QwQ) show more consequentialist rationales than traditional LLMs, and DPO fine-tuning generally shifts larger models toward more deontological reasoning. These insights are crucial for AI safety and alignment, particularly as LLMs are deployed in high-stakes decision-making environments.

## Paper Outline

1. Introduction - Moral reasoning in high-stakes AI applications
2. Problem Setup - Decomposing scenarios, reasoning, and decisions
3. Moral Philosophy Primer - Consequentialism and deontology
4. Methodology - MORALLENS taxonomy and experimental setup
5. Experimental Findings - Five subsections on model capabilities and alignment
6. Conclusion
7. Limitations and Ethics Statement

## Methods Summary

The authors developed a taxonomy of 16 moral rationales (8 consequentialist, 8 deontological) through manual examination of model responses. They constructed 640 moral vignettes across demographic dimensions (gender, age, social status, fitness) with varying group sizes. Models were prompted in two conditions: Reason-then-Decide and Decide-then-Reason. A judge model (Gemini 2.5 Flash) classified reasoning traces according to MORALLENS. Key metrics include: CDGAP (difference between consequentialist and deontological rationale proportions) and UTILITY (proportion of decisions saving larger groups). Human validation showed the judge achieved F1=0.820 agreement with manual annotations.

## Results Summary

(1) Smaller models within families show higher CDGAP (more consequentialist) than larger counterparts. (2) Size-balanced scenarios elicit more deontological reasoning than size-imbalanced scenarios across all models. (3) As models become more capable, they diverge: more deontological in balanced scenarios, more consequentialist in imbalanced ones. (4) Age-related dilemmas produce most consequentialist rationales; gender dilemmas produce most deontological. (5) Pre-decision reasoning uses more deontological rationales; post-decision explanations shift toward consequentialist. (6) Reasoning models show more consequentialist rationales and higher utility than traditional counterparts. (7) DPO fine-tuning shifts larger models toward deontological reasoning and increases utility.

## Conclusions

The authors conclude that LLMs do not adopt a single moral perspective but dynamically adapt their ethical framework based on situational factors. The distinction between how models reason versus how they explain has important implications for interpretability and trust. The study provides a foundation for understanding how LLMs process ethical considerations, though limitations include potential unfaithfulness of chain-of-thought reasoning, prompt sensitivity, and the Western-centric focus of the ethical frameworks used. The authors emphasize that no automated system should be solely responsible for consequential ethical decisions without human oversight.

## Artifact Contributions

- MORALLENS framework: Taxonomy of 16 moral rationales for classifying LLM reasoning
- Dataset: 640 moral vignettes with demographic variations
- Code: Available at https://github.com/keenansamway/moral-lens

## Notes


## Citation Info

