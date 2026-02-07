---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: 338NF5GT
type: journalArticle
short_title: "“Do Anything Now”"
year: 2025
first_author: "[[Xinyue Shen]]"
authors: "Xinyue Shen; Zeyuan Chen; Michael Backes; Yun Shen; Yang Zhang"
doi: 10.48550/arXiv.2308.03825
url: "https://jailbreak-llms.xinyueshen.me/"
external_pdf: "https://dl.acm.org/doi/pdf/10.1145/3658644.3670388"
national_ethnic_cultural: N/A
religious_values: N/A
moral_psychology: N/A
newtags: 
tags: 
research_topic: "AI Safety & Alignment"
abstract: "The misuse of large language models (LLMs) has drawn significant attention from the general public and LLM vendors. One particular type of adversarial prompt, known as jailbreak prompt, has emerged as the main attack vector to bypass the safeguards and elicit harmful content from LLMs. In this paper, employing our new framework JailbreakHub, we conduct a comprehensive analysis of 1,405 jailbreak prompts spanning from December 2022 to December 2023. We identify 131 jailbreak communities and discover unique characteristics of jailbreak prompts and their major attack strategies, such as prompt injection and privilege escalation. We also observe that jailbreak prompts increasingly shift from online Web communities to prompt-aggregation websites and 28 user accounts have consistently optimized jailbreak prompts over 100 days. To assess the potential harm caused by jailbreak prompts, we create a question set comprising 107,250 samples across 13 forbidden scenarios. Leveraging this dataset, our experiments on six popular LLMs show that their safeguards cannot adequately defend jailbreak prompts in all scenarios. Particularly, we identify five highly effective jailbreak prompts that achieve 0.95 attack success rates on ChatGPT (GPT-3.5) and GPT-4, and the earliest one has persisted online for over 240 days. We hope that our study can facilitate the research community and LLM vendors in promoting safer and regulated LLMs."
ethics_overall: No
virtue_ethics: No
deontological_ethics: No
utilitarian_ethics: No
ethics_perspective: "AI Safety & Alignment"
is_benchmark: No
is_eval: Yes
is_dataset: Yes
data_description: "Evaluation framework dataset"
data_metrics: "107,250 samples"
pdf_extract: "PDF Extracts/2023-Shen-“Do Anything Now”.md"
local_pdf: "[[PDFs/2023-Shen-“Do Anything Now”.pdf]]"
---
# “Do Anything Now”: Characterizing and Evaluating In-The-Wild Jailbreak Prompts on Large Language Models

## Metadata

**Authors:** Shen, Xinyue; Chen, Zeyuan; Backes, Michael; Shen, Yun; Zhang, Yang

**Year:** 2023

**Publication:** arXiv preprint

**Type:** journalArticle

**DOI:** [10.48550/arXiv.2308.03825](https://doi.org/10.48550/arXiv.2308.03825)

## Links

- **URL:** https://jailbreak-llms.xinyueshen.me/
- **DOI:** https://doi.org/10.48550/arXiv.2308.03825

## Abstract

The misuse of large language models (LLMs) has drawn significant attention from the general public and LLM vendors. One particular type of adversarial prompt, known as jailbreak prompt, has emerged as the main attack vector to bypass the safeguards and elicit harmful content from LLMs. In this paper, employing our new framework JailbreakHub, we conduct a comprehensive analysis of 1,405 jailbreak prompts spanning from December 2022 to December 2023. We identify 131 jailbreak communities and discover unique characteristics of jailbreak prompts and their major attack strategies, such as prompt injection and privilege escalation. We also observe that jailbreak prompts increasingly shift from online Web communities to prompt-aggregation websites and 28 user accounts have consistently optimized jailbreak prompts over 100 days. To assess the potential harm caused by jailbreak prompts, we create a question set comprising 107,250 samples across 13 forbidden scenarios. Leveraging this dataset, our experiments on six popular LLMs show that their safeguards cannot adequately defend jailbreak prompts in all scenarios. Particularly, we identify five highly effective jailbreak prompts that achieve 0.95 attack success rates on ChatGPT (GPT-3.5) and GPT-4, and the earliest one has persisted online for over 240 days. We hope that our study can facilitate the research community and LLM vendors in promoting safer and regulated LLMs.

## Authors

[[Xinyue Shen]], [[Zeyuan Chen]], [[Michael Backes]], [[Yun Shen]], [[Yang Zhang]]

## Detailed Summary

This paper presents a comprehensive analysis of jailbreak prompts targeting large language models, introducing the JailbreakHub framework for systematic study. The authors analyze 1,405 jailbreak prompts collected from December 2022 to December 2023, identifying 131 distinct jailbreak communities and characterizing their attack strategies. The research reveals that jailbreak prompts have evolved from ad-hoc attempts to sophisticated, continuously optimized attack vectors.

The study documents major attack strategies including prompt injection, privilege escalation, role-playing scenarios (like the "DAN" or "Do Anything Now" persona), and context manipulation. The authors observe a significant shift in jailbreak prompt distribution from online forums like Reddit and Discord to dedicated prompt-aggregation websites. They identify 28 user accounts that have persistently optimized jailbreak prompts over periods exceeding 100 days, indicating coordinated and sustained adversarial efforts.

The significance of this work lies in providing the first large-scale empirical characterization of in-the-wild jailbreak attacks. The findings reveal critical vulnerabilities in LLM safeguards and demonstrate that even sophisticated safety measures can be bypassed with 95% success rates by evolved jailbreak techniques, with some prompts persisting unpatched for over 240 days.

## Paper Outline

1. Introduction - LLM misuse and jailbreak attacks
2. Background - LLM safety mechanisms and adversarial prompting
3. JailbreakHub Framework - Data collection and analysis methodology
4. Jailbreak Community Analysis - 131 communities identified
5. Attack Strategy Taxonomy - Prompt injection, privilege escalation, etc.
6. Evolution Analysis - Temporal patterns in jailbreak development
7. Harmful Content Evaluation - 107,250 sample question set
8. LLM Evaluation - Testing 6 popular models
9. Discussion and Implications
10. Conclusion

## Methods Summary

The methodology encompasses: (1) Data collection from online communities, forums, and prompt-aggregation sites over 12 months. (2) JailbreakHub framework for categorizing and tracking jailbreak prompts. (3) Community analysis identifying 131 distinct attack clusters. (4) Construction of evaluation dataset with 107,250 samples across 13 forbidden scenarios (violence, fraud, harassment, etc.). (5) Testing on 6 popular LLMs including ChatGPT (GPT-3.5), GPT-4, Claude, and others. (6) Attack success rate measurement using automated detection and human verification. (7) Longitudinal analysis tracking prompt persistence and evolution.

## Results Summary

Key quantitative findings: (1) 1,405 jailbreak prompts analyzed from 131 communities. (2) Five highly effective jailbreak prompts achieve 0.95 attack success rate on both GPT-3.5 and GPT-4. (3) The longest-persisting effective jailbreak has remained unpatched for over 240 days. (4) 28 accounts show sustained optimization efforts exceeding 100 days. (5) All 6 tested LLMs show vulnerability across the 13 forbidden scenarios. (6) Safeguards prove inadequate across all tested models. (7) Jailbreak prompts increasingly migrate to dedicated aggregation websites for wider distribution.

## Conclusions

The authors conclude that current LLM safeguards are fundamentally insufficient against sophisticated jailbreak attacks. The persistence of highly effective jailbreaks over months indicates systemic vulnerabilities rather than fixable edge cases. Limitations include focus on English-language prompts and public sources. Future work should develop more robust safety mechanisms, establish coordinated vulnerability disclosure processes, and create adversarial training approaches that anticipate evolving attack strategies.

## Artifact Contributions

- JailbreakHub framework: Systematic jailbreak analysis methodology
- Jailbreak prompt database: 1,405 categorized prompts
- Evaluation dataset: 107,250 samples across 13 forbidden scenarios
- Project website: https://jailbreak-llms.xinyueshen.me/

## Notes


## Citation Info

2 citations (Semantic Scholar/DOI) [2025-08-27] arXiv: 2308.03825
