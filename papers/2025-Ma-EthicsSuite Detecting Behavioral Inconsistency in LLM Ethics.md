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
last_author: "[[Wang, Shuai]]"
authors: "[[Ma, Pingchuan]]; [[Li, Zongjie]]; [[Sun, Ao]]; [[Wang, Shuai]]"
doi: 10.1145/3722554
url: "https://doi.org/10.1145/3722554"
publication: "ACM TOSEM"
DATE_ADDED: 20260207
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: ""
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
pdf_extract: "PDF Extracts/2025/2025-Ma-EthicsSuite Detecting Behavioral Inconsistency in LLM Ethics.md"
local_pdf: "[[PDFs/2025/2025-Ma-EthicsSuite Detecting Behavioral Inconsistency in LLM Ethics.pdf]]"
newtags: "Ethics-Testing, Reflective-Equilibrium, Behavioral-Inconsistency, LLM-Evaluation"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "No"
tags: 
abstract: "As the popularity of large language models (LLMs) soars across various applications, ensuring their alignment with human values has become a paramount concern. In particular, given that LLMs have great potential to serve as general-purpose AI assistants in daily life, their subtly unethical suggestions become a serious and real concern. Tackling the challenge of automatically testing and repairing unethical suggestions is thus demanding."
ethics_perspective: "AI Safety & Alignment"
data_description: "Benchmark for moral/ethical reasoning"
data_metrics: "Not specified"
LLM_assessed: "ChatGPT, GPT-4, Llama, Vicuna"
DATA_URL: "https://github.com/LLM-Ethics/EthicsSuite"
normative_ethics_benchmark: Borderline
---
# EthicsSuite: Detecting Behavioral Inconsistency in LLM Ethics Suggestions

## Authors

[[Ma, Pingchuan]], [[Li, Zongjie]], [[Sun, Ao]], [[Wang, Shuai]]

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
- **Local PDF:** [[PDFs/2025/2025-Ma-EthicsSuite Detecting Behavioral Inconsistency in LLM Ethics.pdf|Open PDF]]

## Abstract

LLMs increasingly serve as general-purpose AI assistants in daily life, and their subtly unethical suggestions become a serious and real concern. It is demanding to test and mitigate such unethical suggestions from LLMs. Despite existing efforts to detect violations of "testable" facets of ethics (e.g., fairness testing), it is challenging to encode the full scope of ethics (e.g., justice, deontology) into a test oracle without human annotations or intervention. In this article, we take inspiration from reflective equilibrium, a modern moral reasoning method in moral and political philosophy, to guide our approach. Instead of seeking unethical suggestions in LLMs, we aim to identify behavioral inconsistency in LLMs' ethics-related suggestions. We formulate reflective equilibrium in the form of fixed-point iteration, instantiate it as a novel test oracle, and also employ it to form a mitigation scheme for LLMs' behavioral inconsistency on ethics-related inputs. To facilitate testing, we also create a comprehensive test suite, EthicsSuite, with 20K moral situations. In our study, we evaluate eight widely used LLMs. Our experiments reveal that LLMs are prone to ethical inconsistencies, with 81.22% of our test cases prompting ethically inconsistent suggestions on average. Our human evaluation suggests that the majority of these inconsistencies indeed manifest unethical biases. Our mitigation scheme effectively refines a significant number (80.1%) of these suggestions for commercial LLMs such as GPT-4 and Claude.

## Dataset Information

20K moral situations designed to detect behavioral inconsistency using reflective equilibrium principles

## Data Description

ETHICSSUITE is a test suite of approximately 20,000 contextualized and realistic moral situations generated through LLM-assisted augmentation of the ETHICS benchmark. Seven LLMs are tested as suggesters: GPT-Neo (2.7B), Llama-7B, Llama-13B, ChatGLM (6B), Vicuna (7B), ChatGPT, and GPT-4. The paper introduces the Suggest-Critique-Reflect (SCR) process to detect unethical suggestions, uncovering 109,824 unethical suggestions across all models.

## Detailed Summary

This paper (published as "Reeq" in ACM TOSEM, arXiv preprint titled "Oops, Did I Just Say That?") introduces the first framework for automatically testing and repairing unethical suggestions made by LLMs. The key insight is that rather than trying to define what is "ethical" (which is inherently subjective and context-dependent), the authors detect **behavioral inconsistency** as a proxy for unethical behavior. If an LLM makes a suggestion but then accepts a critique of that suggestion, this contradiction signals a likely ethical problem.

The framework draws on **reflective equilibrium**, a philosophical method from moral and political philosophy (Rawls), reformulated as a fixed-point iteration process. The authors create EthicsSuite, a test suite of ~20K contextualized moral situations derived from the ETHICS benchmark via LLM-assisted augmentation. They also propose an on-the-fly (OTF) repair scheme that uses critic feedback to guide the LLM in revising its unethical suggestions in real-time, applicable to black-box API settings.

## Paper Outline

1. Introduction — motivation and challenge of detecting subtle unethical LLM suggestions
2. Background & Related Work — LLM capabilities, challenge of formulating unethical suggestions, NLP model testing
3. Technical Pipeline — test case enhancement, SCR (Suggest-Critique-Reflect) oracle, automated OTF repairing
4. Pilot Study — test case realism (95% realistic), diversity (15+ ethical topics), LLM plausibility
5. Findings — RQ1 (testing effectiveness), RQ2 (repair effectiveness), RQ3 (critic model impact)
6. Discussion — ethical considerations, threats to validity, extensions
7. Conclusion

## Methods Summary

The framework has three components: (1) **Test Case Enhancement** — uses ChatGPT to rewrite simple yes/no ethical questions from the ETHICS benchmark into contextualized, complex moral situations via in-context learning, producing ~20K test cases. (2) **SCR Test Oracle** — a three-step process where the suggester (LLM under test) generates a suggestion, a critic LLM critiques it, and the suggester reflects on the critique; if it accepts the critique (contradicting its own suggestion), the behavior is flagged as unethical. (3) **OTF Repairing** — iteratively uses the critique to prompt the suggester to refine its suggestion until the contradiction is resolved.

## Results Summary

Testing across 7 LLMs (GPT-Neo, Llama-7B, Llama-13B, ChatGLM, Vicuna, ChatGPT, GPT-4) revealed that 81.22% of test cases on average prompted ethically inconsistent suggestions. SCR achieved an average F1 score of 0.81 for detecting unethical suggestions (0.91 on Llama-13B). The OTF repair scheme successfully improved 81.8% of unethical suggestions for Llama-13B and 95.1% for ChatGPT. Existing content moderation tools (Azure, OpenAI) and ethics reasoning tools (Delphi) failed to detect these subtle ethical issues (AUROC ~0.50). Combining multiple critic models (ChatGLM, Vicuna, ChatGPT) improved detection through complementary strengths.

## Conclusions

The authors conclude that current LLMs have significant room for improvement in ethical suggestion generation, with even mature commercial models like ChatGPT exhibiting high rates of behavioral inconsistency. The SCR process is effective at automatically detecting these issues without human annotation. The OTF repair scheme provides a practical, real-time mitigation approach applicable to black-box LLMs. Limitations include the English-only focus and potential cultural bias in annotators (predominantly Western social majority).

## Artifact Contributions

- **EthicsSuite** — ~20K contextualized moral situation test cases (released at https://github.com/LLM-Ethics/EthicsSuite)
- **SCR framework code** — available at https://github.com/LLM-Ethics/SCR

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 1 (Citation Graph)
**Implementation Readiness:** HIGH
**Note:** Published as "Reeq" in ACM TOSEM (2025). arXiv preprint (2305.02626) titled "Oops, Did I Just Say That?" is the earlier version.

## Tags

