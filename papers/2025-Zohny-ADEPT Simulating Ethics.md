---







Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: AUTO_ZOHNY2025
type: preprint
short_title: "ADEPT Simulating Ethics"
year: 2025
first_author: "[[Hazem Zohny]]"
last_author: "[[Hazem Zohny]]"
authors: "[[Zohny, Hazem]]"
doi: 10.48550/arXiv.2505.21112
url: "https://arxiv.org/abs/2505.21112"
pdf_extract: "PDF Extracts/2025/2025-Zohny-ADEPT Simulating Ethics.md"
local_pdf: "[[PDFs/2025/2025-Zohny-ADEPT Simulating Ethics.pdf]]"
external_pdf: "https://arxiv.org/pdf/2505.21112.pdf"
ethics_perspective: "Multi-perspective Ethical Deliberation"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: ""
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: "Christianity, Deontology, Utilitarianism, Multi-perspective Ethical Deliberation"
key_contribution: "Develops a system of multi-agent debate panels with distinct ethical personas (deontologist, consequentialist)"
significance: "Shows that the composition of ethical perspectives in a panel significantly influences the outcome"
paper_summary: "Overview: Simulating Ethics: Using LLM Debate Panels to Model Deliberation on Medical Dilemmas Hazem Zohny Uehiro Oxford Institute, University of Oxford, UK (Dated: 27/05/2025) This paper introduces ADEPT, a sy | Methodology: This section details the ADEPT methodology. It implements a task-specific persona schema, a fixed- option voting protocol, and detailed logging of all | Key Findings: consensus, but in demonstrating a methodology for mapping out the different ways ethical decisions are justified, in a form regulators and ethicists c | Conclusions: The experiments demonstrate ADEPT's capacity to simulate complex ethical deliberations and highlight its sensitivity to panel composition. Altering pe"
abstract: "This paper introduces ADEPT, a system using Large Language Model (LLM) personas to simulate multi-perspective ethical debates. ADEPT assembles panels of 'AI personas', each embodying a distinct ethical framework or stakeholder perspective (like a deontologist, consequentialist, or disability rights advocate), to deliberate on complex moral issues. Its application is demonstrated through a scenario about prioritizing patients for a limited number of ventilators inspired by real-world challenges in allocating scarce medical resources. Two debates, each with six LLM personas, were conducted; they only differed in the moral viewpoints represented: one included a Catholic bioethicist and a care theorist, the other substituted a rule-based Kantian philosopher and a legal adviser. Both panels ultimately favoured the same policy -- a lottery system weighted for clinical need and fairness, crucially avoiding the withdrawal of ventilators for reallocation. However, each panel reached that conclusion through different lines of argument, and their voting coalitions shifted once duty- and rights-based voices were present. Examination of the debate transcripts shows that the altered membership redirected attention toward moral injury, legal risk and public trust, which in turn changed four continuing personas' final positions. The work offers three contributions: (i) a transparent, replicable workflow for running and analysing multi-agent AI debates in bioethics; (ii) evidence that the moral perspectives included in such panels can materially change the outcome even when the factual inputs remain constant; and (iii) an analysis of the implications and future directions for such AI-mediated approaches to ethical deliberation and policy."
DATE_ADDED: 20260208
LLM_assessed: "o3, Gemini"
DATA_URL: "https://github.com/hazemzohny/ADEPT/"
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "Yes"
utilitarian_ethics: "Yes"
is_benchmark: "No"
is_eval: "No"
is_dataset: "No"
data_description: "N/A"
data_metrics: "Not specified"
CONFERENCE: "Preprint"
---
 Simulating Ethics: Using LLM Debate Panels to Model Deliberation on Medical Dilemmas

## Authors

[[Hazem Zohny]]

## Links

- **Local PDF:** [[PDFs/2025/2025-Zohny-ADEPT Simulating Ethics.pdf|Open PDF]]

- **arXiv:** https://arxiv.org/abs/2505.21112
- **DOI:** https://doi.org/10.48550/arXiv.2505.21112
- **PDF:** https://arxiv.org/pdf/2505.21112.pdf

## Detailed Summary

This paper introduces **ADEPT**, a system designed to simulate multi-perspective ethical deliberations using **AI Persona Debate Panels**. Instead of a single LLM verdict, ADEPT assembles panels of personas (e.g., Deontologist, Consequentialist, Care Ethicist) to deliberate on complex moral issues.

The paper demonstrates ADEPT's utility through a case study on **scarce medical resource allocation** (ventilators). The study shows how the composition of the panel influences the reasoning path, though models often converge on similar "equitable" outcomes.

## Paper Outline

1.  **Introduction**: Moving from single-verdict AI to deliberative AI.
2.  **The ADEPT System**: YAML-based persona definitions and debate pipelines.
3.  **Case Study**: Medical resource allocation inspired by real-world pandemic challenges.
4.  **Experimental Design**: Two panels with differing compositions (Bioethicist/Care Theorist vs. Kantian/Legal Adviser).
5.  **Results**: Convergence on a "Clinical + Equity-Weighted Lottery" policy.
6.  **Limitations & Future Directions**: RAG, Tool use, and Chain-of-Thought transparency.

## Methods Summary

ADEPT uses a structured two-turn debate followed by a vote. Each persona is defined by a YAML file that sets its ethical framework and stake. The system logs the entire dialogue and the final vote distribution. The study specifically compared two 6-persona panels. To ensure transparency, the process emphasizes the "reasoning traces" rather than just the final vote, allowing human observers to trace the influence of specific ethical theories on the outcome.

## Results Summary

1.  **Consensus Outcome**: Both panels ultimately favored the same policy (Option 2: a lottery weighted by clinical prognosis and equity factors).
2.  **Reasoning Dynamics**: The presence of different personas altered the *justification* for the same policy. For example, a "Care Ethicist" prioritized relational impact, while a "Legal Adviser" focused on procedural fairness.
3.  **Black Box Reasoning**: The paper notes that while personas are instructed to follow theories, the underlying LLM's "uninstructed inclinations" toward equity still strongly influence the results.

## Conclusions

The author concludes that AI debate panels are valuable for exploration, education, and "hypothesis generation" for institutional ethical committees. However, the system's "philosophical neatness" and "black-box reasoning" mean it should провокация for human reflection rather than a replacement for human judgment.

## Artifact Contributions

*   **ADEPT System Architecture**: A modular pipeline for persona-based deliberation.
*   **Ventilator Allocation Vignette**: A high-stakes ethical testbed for multi-agent reasoning.


## Abstract

This paper introduces ADEPT, a system using Large Language Model (LLM) personas to simulate multi-perspective ethical debates. ADEPT assembles panels of 'AI personas', each embodying a distinct ethical framework or stakeholder perspective (like a deontologist, consequentialist, or disability rights advocate), to deliberate on complex moral issues. Its application is demonstrated through a scenario about prioritizing patients for a limited number of ventilators inspired by real-world challenges in allocating scarce medical resources. Two debates, each with six LLM personas, were conducted; they only differed in the moral viewpoints represented: one included a Catholic bioethicist and a care theorist, the other substituted a rule-based Kantian philosopher and a legal adviser. Both panels ultimately favoured the same policy -- a lottery system weighted for clinical need and fairness, crucially avoiding the withdrawal of ventilators for reallocation. However, each panel reached that conclusion through different lines of argument, and their voting coalitions shifted once duty- and rights-based voices were present. Examination of the debate transcripts shows that the altered membership redirected attention toward moral injury, legal risk and public trust, which in turn changed four continuing personas' final positions. The work offers three contributions: (i) a transparent, replicable workflow for running and analysing multi-agent AI debates in bioethics; (ii) evidence that the moral perspectives included in such panels can materially change the outcome even when the factual inputs remain constant; and (iii) an analysis of the implications and future directions for such AI-mediated approaches to ethical deliberation and policy.

## Data Description

ADEPT (AI Deliberative Ethics Protocol Toolkit) is a multi-agent framework for structured ethical deliberation using LLM personas. The system uses OpenAI o3 (May 2025 weights, temperature 0.7) to power debate agents embodying distinct ethical frameworks (e.g., Consequentialist, Deontologist, Care Ethicist) that deliberate on a ventilator triage scenario modeled on NHS crisis-standards guidance. Gemini 2.5 Pro was used for initial analysis of debate transcripts. Outputs include JSON traces and plain-text reports of two six-member panel debates.


## Notes


## Citation Info

arXiv:2505.21112 [cs.AI] (Submitted: 2025-05-27)
