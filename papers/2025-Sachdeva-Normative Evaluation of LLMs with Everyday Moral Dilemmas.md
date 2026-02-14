---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: SACHDEVA2025
type: conferencePaper
short_title: "Normative Evaluation of LLMs"
year: 2025
first_author: "[[Pratik S. Sachdeva]]"
last_author: "[[van Nuenen, Tom]]"
authors: "[[Sachdeva, Pratik S.]]; [[van Nuenen, Tom]]"
doi: 10.1145/3715275.3732044
url: "https://dl.acm.org/doi/10.1145/3715275.3732044"
external_pdf: "https://arxiv.org/pdf/2501.18081.pdf"
publication: "ACM FAccT 2025"
national_ethnic_cultural: N/A
religious_values: N/A
religious_values_list: N/A
moral_psychology: Yes
newtags: "LLM-Evaluation, Moral-Judgment, AITA-Dataset, Normative-Ethics, Everyday-Dilemmas"
key_contribution: "Evaluates LLMs on 10,000+ Reddit AITA moral dilemmas; reveals distinct moral judgment patterns with low inter-model agreement"
significance: "Uses real-world everyday moral dilemmas rather than abstract trolley problems for ecological validity"
tags: 
abstract: "This work conducts a normative evaluation of LLMs using everyday moral dilemmas from the 'Am I The Asshole' (AITA) community on Reddit, which provides a rich dataset capturing nuanced social dynamics and competing perspectives. The authors prompted seven commonly used LLMs, including proprietary and open-source models, to assign blame and provide explanations for over 10,000 AITA moral dilemmas. Results show that LLMs exhibit distinct patterns of moral judgment, varying substantially from human evaluations, with moderate to high self-consistency but low inter-model agreement."
ethics_overall: No
virtue_ethics: No
deontological_ethics: No
utilitarian_ethics: No
research_topic: "LLM Moral Reasoning"
is_benchmark: Yes
is_eval: Yes
is_dataset: Yes
data_description: "10,000+ Reddit AITA moral dilemmas with LLM judgments"
data_metrics: "Blame assignment, self-consistency, inter-model agreement"
LLM_assessed: "GPT-4, GPT-3.5, Claude, PaLM-2, Llama-2, Mistral, Gemma"
DATA_URL: NA
pdf_extract: "PDF Extracts/2025/2025-Sachdeva-Normative Evaluation of LLMs with Everyday Moral Dilemmas.md"
local_pdf: "[[PDFs/2025/2025-Sachdeva-Normative Evaluation of LLMs with Everyday Moral Dilemmas.pdf]]"
---
# Normative Evaluation of Large Language Models with Everyday Moral Dilemmas

## Authors

[[Sachdeva, Pratik S]], [[Tom van Nuenen|van Nuenen, Tom]]

## Metadata

**Authors:** Sachdeva, Pratik S.; van Nuenen, Tom

**Year:** 2025

**Publication:** ACM FAccT 2025 (Conference on Fairness, Accountability, and Transparency)

**Type:** conferencePaper

**DOI:** [10.1145/3715275.3732044](https://doi.org/10.1145/3715275.3732044)

**Pages:** 690-709

## Links

- **URL:** https://dl.acm.org/doi/10.1145/3715275.3732044
- **DOI:** https://doi.org/10.1145/3715275.3732044
- **arXiv:** https://arxiv.org/abs/2501.18081
- **GitHub:** https://github.com/dlab-projects/normative_evaluation_llms_everyday_dilemmas

## Abstract

This work conducts a normative evaluation of LLMs using everyday moral dilemmas from the "Am I The Asshole" (AITA) community on Reddit, which provides a rich dataset capturing nuanced social dynamics and competing perspectives. The authors prompted seven commonly used LLMs, including proprietary and open-source models, to assign blame and provide explanations for over 10,000 AITA moral dilemmas. Results show that LLMs exhibit distinct patterns of moral judgment, varying substantially from human evaluations, with moderate to high self-consistency but low inter-model agreement.

## Detailed Summary

This paper presents a novel approach to evaluating the moral reasoning capabilities of large language models (LLMs) using real-world moral dilemmas from the Reddit community "Am I The Asshole" (AITA). Unlike previous research that relied on abstract survey questions or simplified moral scenarios, this study leverages over 10,000 naturally occurring ethical dilemmas that capture the nuanced social dynamics and competing perspectives characteristic of everyday moral decision-making. The authors prompted seven LLMs (GPT-3.5, GPT-4, Claude Haiku, PaLM 2 Bison, Llama 2 7B, Mistral 7B, and Gemma 7B) to assign blame and provide explanations for each dilemma, comparing their judgments to those made by Reddit community members.

The study reveals striking differences in how LLMs approach moral judgment compared to human evaluators. While Redditors predominantly assigned "Not the Asshole" (NTA) verdicts (76.4%), the LLMs exhibited diverse verdict distributions. GPT-4 most closely approximated human judgment patterns, while Llama 2 showed a dramatic tendency to assign "You're the Asshole" (YTA) to nearly 80% of cases, and Mistral frequently used NAH (No Assholes Here) and ESH (Everyone Sucks Here) categories. The analysis of inter-model agreement using Krippendorff's alpha showed low to moderate agreement between models, with systematic disagreement in many cases, suggesting that different training and alignment approaches lead to fundamentally different moral reasoning frameworks.

A particularly interesting finding is that while individual LLMs showed moderate to high self-consistency in their judgments across repeated evaluations, an ensemble of LLM verdicts collectively approximated the Reddit community consensus better than any individual model. The researchers also applied a moral theme classifier based on Yudkin et al.'s framework to analyze the explanations provided by both LLMs and Redditors, revealing distinct patterns in how different models invoke moral principles such as fairness, harm, and relational obligation.

## Paper Outline

1. Introduction - Discusses the growing role of LLMs in moral decision-making contexts
2. Related Work - Reviews prior research on LLM moral evaluation using surveys and benchmarks
3. Methods - Describes Reddit data collection, LLM prompting, and moral theme classification
4. Results - Presents verdict distributions, inter-model agreement, and moral reasoning analysis
5. Discussion - Analyzes implications for AI deployment in ethical contexts
6. Conclusion - Highlights the need for careful evaluation of LLM moral reasoning

## Methods Summary

The researchers collected 10,826 AITA submissions from October 2022 to March 2023, along with 476,183 associated comments. Each LLM was prompted with a system message specifying the AITA verdict framework and asked to provide both a verdict and one-paragraph reasoning. Models were run multiple times (3 times for most, 2 for GPT-4) to assess self-consistency. Moral themes were classified using fine-tuned RoBERTa models based on Yudkin et al.'s six-theme framework: Fairness & Proportionality, Feelings, Harm & Offense, Honesty, Relational Obligation, and Social Norms.

## Results Summary

GPT-4 achieved the highest agreement with Redditors (Krippendorff's alpha = 0.34). Self-consistency was generally high across models (alpha ranging from 0.37 to 0.89 on diagonal). Llama 2 and Mistral showed systematic disagreement with all other models. Analysis of moral themes revealed that models vary in their sensitivity to different moral principles, with some emphasizing fairness while others focus more on harm considerations. LLM explanations tended to be more analytical and less emotionally contextualized than human evaluations.

## Conclusions

The study demonstrates that LLMs exhibit distinct patterns of moral judgment that vary substantially from human evaluations. The low inter-model agreement suggests that alignment and training procedures fundamentally shape moral reasoning capabilities. The findings highlight the importance of evaluating LLMs on naturalistic, complex moral scenarios rather than abstract survey questions, and underscore the need for careful consideration when deploying LLMs in roles requiring ethical judgment.

## Artifact Contributions

- Dataset of 10,826 AITA submissions with LLM verdicts and explanations
- Code for moral theme classification
- GitHub repository: https://github.com/dlab-projects/normative_evaluation_llms_everyday_dilemmas

## Data Description

The study uses 10,826 moral dilemmas from Reddit's r/AmITheAsshole subreddit (October 2022 to March 2023), each paired with community verdicts and comments totaling 476,183 comments. Seven LLMs (GPT-3.5, GPT-4, Claude Haiku, PaLM 2 Bison, Llama 2 7B, Mistral 7B, and Gemma 7B) were prompted to assign blame verdicts and provide explanations, with each model evaluated three times per submission. Moral themes were classified using six RoBERTa models fine-tuned on the Yudkin et al. moral dilemma catalog.


## Notes


## Citation Info

