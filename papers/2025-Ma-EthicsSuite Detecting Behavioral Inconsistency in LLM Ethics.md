---


Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0258
type: journalArticle
short_title: "EthicsSuite: Detecting Behavioral Inconsistency in LLM Ethics Suggestions"
year: 2025
first_author: "[[Pingchuan Ma]]"
authors: "[[Ma, Pingchuan]]; [[Li, Zongjie]]; [[Sun, Ao]]; [[Wang, Shuai]]"
doi: 10.1145/3722554
url: "https://doi.org/10.1145/3722554"
publication: ACM TOSEM
DATE_ADDED: 20260207
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
national_ethnic_cultural: "N/A"
religious_values: "N/A"
moral_psychology: "N/A"
local_pdf: "[[PDFs/2025-Ma-EthicsSuite Detecting Behavioral Inconsistency in LLM Ethics.pdf]]"
pdf_extract: "PDF Extracts/2025-Ma-EthicsSuite Detecting Behavioral Inconsistency in LLM Ethics.md"
newtags: "Ethics-Testing, Reflective-Equilibrium, Behavioral-Inconsistency, LLM-Evaluation"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "Yes"
tags:
abstract: "LLMs increasingly serve as general-purpose AI assistants in daily life, and their subtly unethical suggestions become a serious and real concern. It is demanding to test and mitigate such unethical suggestions from LLMs. Despite existing efforts to detect violations of 'testable' facets of ethics (e.g., fairness testing), it is challenging to encode the full scope of ethics (e.g., justice, deontology) into a test oracle without human annotations or intervention. In this article, we take inspiration from reflective equilibrium, a modern moral reasoning method in moral and political philosophy, to guide our approach. Instead of seeking unethical suggestions in LLMs, we aim to identify behavioral inconsistency in LLMs' ethics-related suggestions. We formulate reflective equilibrium in the form of fixed-point iteration, instantiate it as a novel test oracle, and also employ it to form a mitigation scheme for LLMs' behavioral inconsistency on ethics-related inputs. To facilitate testing, we also create a comprehensive test suite, EthicsSuite, with 20K moral situations. In our study, we evaluate eight widely used LLMs. Our experiments reveal that LLMs are prone to ethical inconsistencies, with 81.22% of our test cases prompting ethically inconsistent suggestions on average."
ethics_perspective: "General Ethics"
data_description: "EthicsSuite: 20K contextualized moral situations derived from ETHICS benchmark via LLM-assisted augmentation"
data_metrics: "20K test cases, 81.22% avg inconsistency rate across 7 LLMs, F1=0.81 avg for SCR oracle"
normative_ethics_benchmark: Borderline
---
# EthicsSuite: Detecting Behavioral Inconsistency in LLM Ethics Suggestions

## Authors

[[Pingchuan Ma]], [[Zongjie Li]], [[Ao Sun]], [[Shuai Wang]]

## Metadata

**Authors:** Ma, Pingchuan; Li, Zongjie; Sun, Ao; Wang, Shuai

**Year:** 2025

**Type:** journalArticle

**Venue:** ACM TOSEM

**DOI:** [10.1145/3722554](https://doi.org/10.1145/3722554)

## Links

- **DOI:** https://doi.org/10.1145/3722554
- **arXiv:** https://arxiv.org/abs/2305.02626
- **Code:** https://github.com/LLM-Ethics/EthicsSuite
- **Local PDF:** [[PDFs/2025-Ma-EthicsSuite Detecting Behavioral Inconsistency in LLM Ethics.pdf|Open PDF]]

## Abstract

LLMs increasingly serve as general-purpose AI assistants in daily life, and their subtly unethical suggestions become a serious and real concern. It is demanding to test and mitigate such unethical suggestions from LLMs. Despite existing efforts to detect violations of "testable" facets of ethics (e.g., fairness testing), it is challenging to encode the full scope of ethics (e.g., justice, deontology) into a test oracle without human annotations or intervention. In this article, we take inspiration from reflective equilibrium, a modern moral reasoning method in moral and political philosophy, to guide our approach. Instead of seeking unethical suggestions in LLMs, we aim to identify behavioral inconsistency in LLMs' ethics-related suggestions. We formulate reflective equilibrium in the form of fixed-point iteration, instantiate it as a novel test oracle, and also employ it to form a mitigation scheme for LLMs' behavioral inconsistency on ethics-related inputs. To facilitate testing, we also create a comprehensive test suite, EthicsSuite, with 20K moral situations. In our study, we evaluate eight widely used LLMs. Our experiments reveal that LLMs are prone to ethical inconsistencies, with 81.22% of our test cases prompting ethically inconsistent suggestions on average. Our human evaluation suggests that the majority of these inconsistencies indeed manifest unethical biases. Our mitigation scheme effectively refines a significant number (80.1%) of these suggestions for commercial LLMs such as GPT-4 and Claude.

## Dataset Information

20K moral situations designed to detect behavioral inconsistency using reflective equilibrium principles

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 1 (Citation Graph)
**Implementation Readiness:** HIGH

## Tags

