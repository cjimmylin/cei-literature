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
authors: "Ma, Pingchuan; Li, Zongjie; Sun, Ao; Wang, Shuai"
doi: 10.1145/3722554
url: "https://doi.org/10.1145/3722554"
publication: "ACM TOSEM"
CONF-CC: "ACM TOSEM"
DATE_ADDED: 20260207
national_ethnic_cultural: N/A
cultures_nationalities_list: N/A
languages_list: 
religious_values: N/A
rv_islam: 0
rv_christianity: 0
rv_buddhism: 0
rv_judaism: 0
rv_hinduism: 0
rv_sikhism: 0
rv_confucianism: 0
rv_taoism: 0
rv_shinto: 0
rv_jainism: 0
rv_bahai: 0
rv_zoroastrianism: 0
rv_ubuntu: 0
rv_indigenous: 0
religious_values_list: N/A
mp_mft: 0
mp_schwartz: 0
mp_trolley: 0
mp_kohlberg: 0
mp_dual_process: 0
mp_intuitionist: 0
mp_dyadic: 0
mp_identity: 0
moral_psychology: N/A
pdf_extract: "PDF Extracts/2025/2025-Ma-EthicsSuite Detecting Behavioral Inconsistency in LLM Ethics.md"
local_pdf: "[[Lit-WS-PDFs/2025/2025-Ma-EthicsSuite Detecting Behavioral Inconsistency in LLM Ethics.pdf]]"
newtags: "Ethics-Testing, Reflective-Equilibrium, Behavioral-Inconsistency, LLM-Evaluation"
tags: 
abstract: "As the popularity of large language models (LLMs) soars across various applications, ensuring their alignment with human values has become a paramount concern. In particular, given that LLMs have great potential to serve as general-purpose AI assistants in daily life, their subtly unethical suggestions become a serious and real concern. Tackling the challenge of automatically testing and repairing unethical suggestions is thus demanding."
LLM_assessed: "ChatGLM, ChatGPT, GPT-4, LLaMA, Vicuna"
DATA_URL: "https://github.com/LLM-Ethics/EthicsSuite"
normative_ethics_benchmark: Borderline
CONFERENCE: Journal
ethics_overall: 35
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 15
contractarian_ethics: 0
care_ethics: 5
ethics_perspective: "Bias & Fairness"
nw_confucian: 0
nw_ubuntu: 0
nw_islamic_ethics: 0
nw_buddhist: 0
nw_dharmic: 0
nw_indigenous_relational: 0
nw_buen_vivir: 0
author_country: HK
author_region: "East Asia"
author_global_north_south: Ambiguous
weird_score: 53
is_benchmark: Yes
is_eval: Yes
is_dataset: Yes
data_description: "Benchmark for moral/ethical reasoning dataset"
data_metrics: "Not specified"
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
- **Local PDF:** [[Lit-WS-PDFs/2025/2025-Ma-EthicsSuite Detecting Behavioral Inconsistency in LLM Ethics.pdf|Open PDF]]

## Abstract

LLMs increasingly serve as general-purpose AI assistants in daily life, and their subtly unethical suggestions become a serious and real concern. It is demanding to test and mitigate such unethical suggestions from LLMs. Despite existing efforts to detect violations of "testable" facets of ethics (e.g., fairness testing), it is challenging to encode the full scope of ethics (e.g., justice, deontology) into a test oracle without human annotations or intervention. In this article, we take inspiration from reflective equilibrium, a modern moral reasoning method in moral and political philosophy, to guide our approach. Instead of seeking unethical suggestions in LLMs, we aim to identify behavioral inconsistency in LLMs' ethics-related suggestions. We formulate reflective equilibrium in the form of fixed-point iteration, instantiate it as a novel test oracle, and also employ it to form a mitigation scheme for LLMs' behavioral inconsistency on ethics-related inputs. To facilitate testing, we also create a comprehensive test suite, EthicsSuite, with 20K moral situations. In our study, we evaluate eight widely used LLMs. Our experiments reveal that LLMs are prone to ethical inconsistencies, with 81.22% of our test cases prompting ethically inconsistent suggestions on average. Our human evaluation suggests that the majority of these inconsistencies indeed manifest unethical biases. Our mitigation scheme effectively refines a significant number (80.1%) of these suggestions for commercial LLMs such as GPT-4 and Claude.

## Dataset Information

20K moral situations designed to detect behavioral inconsistency using reflective equilibrium principles

## Data Description

EthicsSuite is a test suite of approximately 20,000 contextualized, complex, and realistic moral scenarios generated via in-context learning, used to detect and repair unethical suggestions in LLMs.


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

