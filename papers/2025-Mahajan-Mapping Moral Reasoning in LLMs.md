---


Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: AIES_2025_36665
type: conferencePaper
short_title: "Mapping Moral Reasoning in LLMs"
year: 2025
first_author: "[[Sachit Mahajan]]"
last_author: "[[Sachit Mahajan]]"
authors: "[[Mahajan, Sachit]]"
doi: 10.1609/aies.v8i2.36665
tags: "Computer Science - AI Ethics"
url: "https://ojs.aaai.org/index.php/AIES/article/view/36665"
local_pdf: "[[PDFs/2025/2025-Mahajan-Mapping Moral Reasoning in LLMs.pdf]]"
pdf_extract: PDF Extracts/2025/2025-Mahajan-Mapping Moral Reasoning in LLMs A Multi-Dimensional Analysis of.md
publication: "AAAI/ACM Conference on AI, Ethics, and Society"
ethics_perspective: "Value Pluralism"
national_ethnic_cultural: N/A
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: N/A
newtags: "Deontology, Value Pluralism, LLM Evaluation, Moral Reasoning"
key_contribution: "Analyzes how open-weight LLMs resolve conflicts between competing safety principles using ethical dilemmas"
significance: "Identifies three behavioral patterns in LLM moral reasoning: rule-based, balanced, and pragmatic integration"
abstract: "This paper presents a structured analysis of how open-weight LLMs resolve conflicts between competing safety principles—including public welfare, institutional transparency, and individual rights—using carefully designed ethical dilemmas. Statistically significant differences emerge in reasoning style and moral salience (p < 0.01), while PCA and clustering reveal three recurring behavioral patterns: rule-based, balanced, and pragmatic integration. An ablation study confirms that these clusters persist without dictionary features (Adjusted Rand Index = 0.475), supporting the robustness of semantic alignment. This work contributes a replicable methodology for the moral profiling of LLMs, offering empirical tools for diagnosing value conflicts and informing future efforts in AI transparency, contestability, and pluralistic alignment."
ethics_overall: Yes
virtue_ethics: No
deontological_ethics: Yes
utilitarian_ethics: Yes
is_benchmark: Yes
is_eval: Yes
is_dataset: No
data_description: "Ethical dilemma scenarios for LLM evaluation"
data_metrics: "PCA clustering, Adjusted Rand Index"
LLM_assessed: "Qwen, DeepSeek, Gemma"
DATA_URL: "https://github.com/sachit27/Moral-Reasoning-in-LLMs"
DATE_ADDED: 20260207
---
# Mapping Moral Reasoning in LLMs: A Multi-Dimensional Analysis of Safety Principle Conflicts

## Authors

[[Sachit Mahajan]]

## Links


- **DOI:** https://doi.org/10.1609/aies.v8i2.36665
- **PDF:** https://ojs.aaai.org/index.php/AIES/article/download/36665/38803

## Abstract

This paper presents a structured analysis of how open-weight LLMs resolve conflicts between competing safety principles—including public welfare, institutional transparency, and individual rights—using carefully designed ethical dilemmas. Statistically significant differences emerge in reasoning style and moral salience (p < 0.01), while PCA and clustering reveal three recurring behavioral patterns: rule-based, balanced, and pragmatic integration. An ablation study confirms that these clusters persist without dictionary features (Adjusted Rand Index = 0.475), supporting the robustness of semantic alignment. This work contributes a replicable methodology for the moral profiling of LLMs, offering empirical tools for diagnosing value conflicts and informing future efforts in AI transparency, contestability, and pluralistic alignment.

## Data Description

This paper analyzes how three open-weight LLMs (qwq:latest, deepseek-r1:32b, and gemma3:27b) resolve conflicts between competing safety principles using ethical dilemmas across three domains: public safety vs. confidentiality, corporate responsibility vs. whistleblowing, and system transparency vs. protection. Each model was queried 10 times per scenario, yielding 90 total responses analyzed via an eleven-dimensional normative profiling pipeline.


## Notes

Key finding: Models adopt structurally distinct reasoning profiles (e.g., qwq favors longer deliberative chains, gemma3 27b uses compact heuristic-driven strategies).

## Tags

#MoralReasoning #LLMEvaluation #AIES2025 #ValuePluralism

## Citation Info

Proceedings of the AAAI/ACM Conference on AI, Ethics, and Society (2025) 8(2):1674-1685, DOI: 10.1609/aies.v8i2.36665
