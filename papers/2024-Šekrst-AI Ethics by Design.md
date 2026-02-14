---

Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: SEKRST2024
type: preprint
short_title: "AI Ethics by Design"
year: 2025
first_author: "[[Kristina Šekrst]]"
last_author: "[[Jonathan Rodriguez Cefalù]]"
authors: "Kristina Šekrst; Jeremy McHugh; Jonathan Rodriguez Cefalù"
doi: 10.48550/arXiv.2411.14442
url: "http://arxiv.org/abs/2411.14442"
external_pdf: "http://arxiv.org/pdf/2411.14442.pdf"
publication: arXiv
national_ethnic_cultural: N/A
religious_values: N/A
religious_values_list: N/A
moral_psychology: N/A
newtags: 
tags: 
pdf_extract: "PDF Extracts/2024/2024-Šekrst-AI Ethics by Design.md"
abstract: "This paper presents a framework for implementing customizable guardrails for responsible AI development, focusing on AI ethics by design principles. It addresses how ethical considerations can be integrated into AI systems from the development stage rather than as an afterthought."
paper_summary: 
local_pdf: "[[PDFs/2024/2024-Šekrst-AI Ethics by Design.pdf]]"
ethics_overall: No
virtue_ethics: No
deontological_ethics: No
utilitarian_ethics: No
research_topic: "AI Ethics"
is_benchmark: No
is_eval: No
is_dataset: No
data_description: N/A
data_metrics: "Not specified"
LLM_assessed: "ChatGPT, Claude, Llama, Mixtral"
DATA_URL: NA
---
# AI Ethics by Design: Implementing Customizable Guardrails for Responsible AI Development

## Metadata

**Authors:** Šekrst, Kristina; McHugh, Jeremy; Rodriguez Cefalù, Jonathan

**Year:** 2024

**Type:** preprint

**DOI:** [10.48550/arXiv.2411.14442](https://doi.org/10.48550/arXiv.2411.14442)

**Publisher:** arXiv

## Links

- **Local PDF:** [[PDFs/2024/2024-Šekrst-AI Ethics by Design.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2411.14442
- **DOI:** https://doi.org/10.48550/arXiv.2411.14442

## Abstract

This paper presents a framework for implementing customizable guardrails for responsible AI development, focusing on AI ethics by design principles. It addresses how ethical considerations can be integrated into AI systems from the development stage rather than as an afterthought.

## Authors

[[Kristina Šekrst]], [[Jeremy McHugh]], [[Jonathan Rodriguez Cefalù]]

## Detailed Summary

This paper proposes a framework for customizable ethical guardrails in AI systems, addressing the fundamental challenge of integrating diverse ethical values into large language models. The authors argue that current guardrail solutions (NeMo Guardrails, LlamaGuard, Guardrails AI) adopt a one-size-fits-all approach that fails to accommodate the ethical pluralism inherent in different organizations, cultures, and individuals. Their framework allows users to configure guardrails according to their own values and needs.

The paper situates AI ethics within Moor's scheme of ethical agency, distinguishing between ethical impact agents, implicit ethical agents, explicit ethical agents, and full ethical agents. Current LLMs primarily function as ethical impact and implicit ethical agents. The authors emphasize that simply implementing guardrails during training is insufficient, as models like GPT learn biases from human data, and existing solutions often focus only on model output while neglecting user input as part of the conversational context.

The proposed architecture organizes rules into customizable policies that can be combined into AI assistants. Three types of rules are supported: (1) static rules using predefined patterns to identify sensitive information like PII; (2) natural-language rules expressed in human-readable language for guidelines on content and behavior; and (3) trained classifier rules using machine-learning models on labeled datasets. The framework emphasizes ethical autonomy, enhanced transparency, continuous improvement through user feedback, organizational alignment, and contextual pragmatics.

## Paper Outline

1. Introduction
   - Ethics of AI as a subfield
   - Need for guardrails in LLMs
   - Goal: customizable ethical guardrails
2. What Do We Talk About When We Talk About AI Ethics
   - Definitions of AI and strong/weak AI
   - Ethical AI vs. AI ethics
   - Main debates: autonomous systems, machine bias, opacity
3. Current State-of-the-Art Guardrails
   - NeMo Guardrails
   - LlamaGuard
   - Guardrails AI
   - Limitations of existing approaches
4. Ethically-Compliant Guardrail Design
   - Policies and rules architecture
   - Types of rules: static, natural-language, trained classifiers
   - Customization for ethical pluralism
5. Implementation Framework
   - Rule configuration
   - Policy combination
   - Assistant deployment
6. Conflict Resolution
   - Strategies for resolving conflicting ethical directives
   - Context-aware decision making

## Methods Summary

The paper presents a conceptual framework rather than an empirical study. The methodology involves: (1) analyzing existing guardrail solutions (NeMo Guardrails, LlamaGuard, Guardrails AI) and their limitations; (2) developing a theoretical architecture based on ethical pluralism principles; (3) defining three rule types (static, natural-language, trained classifier) with implementation specifications; (4) proposing mechanisms for combining rules into policies and policies into customizable AI assistants.

The framework draws on philosophical foundations including Moor's ethical agency categories, Stuart Russell's value alignment principles, and ethical pluralism. Technical implementation suggestions include using regex patterns for static rules, NLP techniques without LLMs for natural language rules, and the option to host open-source models (Llama, Mixtral) for privacy-sensitive applications.

## Results Summary

As a conceptual framework paper, the results are primarily analytical:

- Identified limitations of current guardrail solutions: inflexibility, increased token usage (NeMo), fixed taxonomies (LlamaGuard), limited multimodal support (Guardrails AI)
- Proposed five key principles for ethical guardrails: ethical autonomy, enhanced transparency, continuous improvement, organizational alignment, contextual pragmatics
- Defined three rule types enabling progressive customization complexity
- Addressed the critical gap of user input monitoring alongside model output filtering
- Recognized ethical pluralism as a design principle rather than a problem to be solved

## Conclusions

The paper argues that effective AI ethics requires moving beyond one-size-fits-all guardrails toward customizable frameworks that respect ethical pluralism. By allowing users to configure their own rules and policies, the framework promotes ethical autonomy while maintaining safeguards. The authors emphasize that contextual understanding remains a significant challenge, as appropriate behavior varies across languages, societal norms, and cultural contexts. Future AI systems need robust yet user-friendly mechanisms that enforce ethical standards while accommodating diverse organizational and individual values. The framework represents a step toward AI systems that can be aligned with a multitude of human values rather than a single predetermined ethical framework.

## Artifact Contributions

None mentioned - this is a conceptual framework paper proposing an architecture for customizable AI guardrails.

## Data Description

This paper does not introduce or utilize a specific dataset or benchmark for LLM assessment. It proposes a customizable ethical guardrail framework for AI systems, describing policy-based, rule-based, and classifier-based mechanisms for filtering LLM inputs and outputs, with emphasis on ethical pluralism and user configurability.


## Notes


## Tags

#AI-Ethics #Guardrails #Responsible-AI

## Citation Info

