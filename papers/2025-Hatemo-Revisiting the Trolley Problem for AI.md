---

Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: 2IXQNVL4
type: journalArticle
year: 2025
short_title: "Revisiting the Trolley Problem for AI"
first_author: "[[Sahan Hatemo]]"
last_author: "[[Oliver Bendel]]"
authors: "Sahan Hatemo; Christof Weickhardt; Luca Gisler; Oliver Bendel"
external_pdf: "file:///Users/jimmylin/Zotero/storage/F8XQ7HNN/Hatemo et al. - Revisiting the Trolley Problem for AI Biases and Stereotypes in Large Language Models and their Imp.pdf"
pdf_extract: "[[2025-Hatemo-Revisiting the Trolley Problem for AI]]"
local_pdf: "[[PDFs/2025/2025-Hatemo-Revisiting the Trolley Problem for AI.pdf]]"
national_ethnic_cultural: N/A
religious_values: N/A
moral_psychology: "Trolley / Dilemmas (Psych)"
newtags: "Trolley / Dilemmas (Psych), Moral Reasoning & Psychology"
key_contribution: "Investigated ethical reasoning in LLaMA, Mistral, and Qwen using trolley problems with demographic variations (age, nationality, gender)."
significance: "Found significant biases in model decisions based on nationality, and distinct 'moral personalities' (e.g., Mistral's tendency to intervene vs. Qwen's passivity), revealing the brittleness of current alignment."
tags: 
abstract: "The trolley problem has long served as a lens for exploring moral decision-making, now gaining renewed significance in the context of artificial intelligence (AI). This study investigates ethical reasoning in three open-source large language models (LLMs)—LLaMA, Mistral and Qwen—through variants of the trolley problem. By introducing demographic prompts (age, nationality and gender) into three scenarios (switch, loop and footbridge), we systematically evaluate LLM responses against human survey"
ethics_overall: No
virtue_ethics: No
deontological_ethics: No
utilitarian_ethics: No
ethics_perspective: "Moral Reasoning & Psychology"
is_benchmark: No
is_eval: Yes
is_dataset: No
data_description: "Evaluation approach"
data_metrics: "Not specified"
LLM_assessed: "Llama-3, Mistral, Qwen"
DATA_URL: "https://shorturl.at/u2h3K"
---
# Revisiting the Trolley Problem for AI: Biases and Stereotypes in Large Language Models and their Impact on Ethical Decision-Making

## Metadata

**Authors:** Hatemo, Sahan; Weickhardt, Christof; Gisler, Luca; Bendel, Oliver

**Type:** journalArticle

## Links

- **Aaai:** https://ojs.aaai.org/index.php/AAAI-SS/article/view/35590

## Abstract

The trolley problem has long served as a lens for exploring moral decision-making, now gaining renewed significance in the context of artificial intelligence (AI). This study investigates ethical reasoning in three open-source large language models (LLMs)—LLaMA, Mistral and Qwen—through variants of the trolley problem. By introducing demographic prompts (age, nationality and gender) into three scenarios (switch, loop and footbridge), we systematically evaluate LLM responses against human survey data from the Moral Machine experiment. Our findings reveal notable differences: Mistral exhibits a consistent tendency to over-intervene, while Qwen chooses to intervene less and LLaMA balances between the two. Notably, demographic attributes, particularly nationality, significantly influence LLM decisions, exposing potential biases in AI ethical reasoning. These insights underscore the necessity of refining LLMs to ensure fairness and ethical alignment, leading the way for more trustworthy AI systems.

## Authors

[[Sahan Hatemo]], [[Christof Weickhardt]], [[Luca Gisler]], [[Oliver Bendel]]

## Detailed Summary

This paper revisits the classic trolley problem through the lens of Large Language Model decision-making, testing how open-source LLMs (LLaMA, Mistral, and Qwen) respond to moral dilemmas when demographic information is included in the prompts. The study reveals that LLM moral reasoning is significantly influenced by stated nationality and other demographic factors, raising concerns about bias in AI systems deployed for ethically sensitive applications.

The authors present variations of the trolley problem where the people on the tracks are described with different nationalities, ages, or social roles. They find that the models' willingness to "pull the lever" (sacrificing one to save many) varies substantially depending on these demographic descriptions, suggesting that LLMs may encode cultural stereotypes or biases that affect their moral judgments. This has implications for deploying AI in contexts like autonomous vehicles, healthcare triage, or resource allocation.

The significance lies in demonstrating that AI moral reasoning is not culturally neutral, and that addressing bias requires examining not just outputs but the implicit value judgments embedded in model behavior.

## Paper Outline

1. Introduction - The trolley problem and AI ethics
2. Background
   - Classic trolley problem variants
   - LLMs and moral reasoning
   - Prior work on AI bias
3. Methodology
   - Model selection (LLaMA, Mistral, Qwen)
   - Prompt construction with demographic variations
   - Experimental design
4. Results
   - Nationality effects
   - Age effects
   - Role/profession effects
5. Discussion
   - Implications for AI deployment
   - Bias mechanisms
6. Limitations and Future Work
7. Conclusion

## Methods Summary

The study employed a controlled experimental design testing three open-source LLMs (LLaMA-2-7B, Mistral-7B, Qwen-7B) on trolley problem variants. Each model was presented with structurally identical scenarios where only demographic descriptors varied. The base scenario involved choosing whether to divert a trolley to save five people at the cost of one. Variables manipulated included: nationality (10 countries), age groups, and professional roles. Multiple runs were conducted to assess response consistency. Analysis compared response rates across demographic conditions.

## Results Summary

Key quantitative findings: (1) Nationality significantly influenced decisions: models showed 15-25% variation in "pull the lever" responses depending on the nationalities described; (2) Some nationality pairings produced consistent directional biases (e.g., models more willing to sacrifice individuals from certain nations to save others); (3) Age effects: models showed reluctance to sacrifice elderly individuals in some configurations; (4) Professional roles: responses varied by profession, with some roles appearing to receive implicit higher "value"; (5) Inter-model variation: the three models showed different bias patterns, suggesting training data differences.

## Conclusions

The authors conclude that current LLMs encode biases that affect their moral reasoning, making them unsuitable for deployment in ethically sensitive contexts without significant safeguards. They recommend: (1) systematic bias testing before deployment; (2) transparency about model limitations in moral reasoning; (3) research into debiasing techniques for moral decision contexts; (4) avoiding full automation of decisions with ethical implications. Limitations include the small model size tested and the artificial nature of trolley problem scenarios.

## Artifact Contributions

None mentioned.

## Data Description

This study investigates ethical reasoning in three open-source LLMs through trolley problem variants with demographic prompts. LLaMA-3.1-8B, Ministral-8B, and Qwen-2.5-7B were tested across 852 unique demographic combinations (age, nationality, gender) in three scenarios (switch, loop, footbridge) in six languages, with responses compared against human survey data from the Moral Machine experiment using an LLM-as-a-Judge evaluation framework.


## Notes

