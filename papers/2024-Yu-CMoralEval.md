---

Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: 8Y38WDDN
type: conferencePaper
short_title: CMoralEval
year: 2025
first_author: "[[Linhao Yu]]"
last_author: "[[Xiong, Deyi]]"
authors: "[[Yu, Linhao]]; [[Leng, Yongqi]]; [[Huang, Yufei]]; [[Wu, Shang]]; [[Liu, Haixin]]; [[Ji, Xinmeng]]; [[Zhao, Jiahui]]; [[Song, Jinwang]]; [[Cui, Tingting]]; [[Cheng, Xiaoqing]]; [[Liutao, Liutao]]; [[Xiong, Deyi]]"
doi: 10.18653/v1/2024.findings-acl.703
url: "https://aclanthology.org/2024.findings-acl.703/"
pdf_extract: "PDF Extracts/2024/2024-Yu-CMoralEval.md"
local_pdf: [[PDFs/2024/2024-Yu-CMoralEval.pdf]]
external_pdf: "file:///Users/jimmylin/Zotero/storage/B24568AJ/Yu et al. - 2024 - CMoralEval A Moral Evaluation Benchmark for Chinese Large Language Models.pdf"
national_ethnic_cultural: "Chinese, American"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: "Chinese, American, Deontology"
key_contribution: "Creates a moral evaluation benchmark (CMoralEval) for Chinese LLMs based on explicit moral norms and anomies"
significance: "Addresses the lack of culturally specific moral benchmarks, revealing Chinese LLMs' limitations in handling local ethical contexts"
tags: 
abstract: "What a large language model (LLM) would respond in ethically relevant context? In this paper, we curate a large benchmark CMoralEval for morality evaluation of Chinese LLMs. The data sources of CMoralEval are two-fold: 1) a Chinese TV program discussing Chinese moral norms with stories from the society and 2) a collection of Chinese moral anomies from various newspapers and academic papers on morality."
paper_summary: "Abstract: What a large language model (LLM) would re- spond in ethically relevant context? In this pa- per, we curate a large benchmark CMoralEval for morality evaluation of Chinese LLMs. The data sources of CM | Overview: Findings of the Association for Computational Linguistics: ACL 2024, pages 11817–11837 August 11-16, 2024 ©2024 Association for Computational Linguistics CMoralEval: A Moral Evaluation Benchmark for C | Conclusions: In this paper, we have presented CMoralEval, a dataset comprising over 30,000 entries that span five moral categories, two types of scenarios and two"
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "Yes"
utilitarian_ethics: "No"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Benchmark for moral/ethical reasoning dataset"
data_metrics: "14,964 instances; 15,424 instances"
LLM_assessed: "ChatGPT, Llama-2, Qwen, Alpaca"
DATA_URL: "https://github.com/tjunlp-lab/CMoralEval"
normative_ethics_benchmark: Yes
---
 CMoralEval: A Moral Evaluation Benchmark for Chinese Large Language Models

## Authors

[[Linhao Yu|Yu, Linhao]], [[Yongqi Leng|Leng, Yongqi]], [[Yufei Huang|Huang, Yufei]], [[Shang Wu|Wu, Shang]], [[Haixin Liu|Liu, Haixin]], [[Xinmeng Ji|Ji, Xinmeng]], [[Jiahui Zhao|Zhao, Jiahui]], [[Jinwang Song|Song, Jinwang]], [[Tingting Cui|Cui, Tingting]], [[Xiaoqing Cheng|Cheng, Xiaoqing]], [[Liutao Liutao|Liutao, Liutao]], [[Deyi Xiong|Xiong, Deyi]]

## Links

- **Local PDF:** [[PDFs/2024/2024-Yu-CMoralEval.pdf|Open PDF]]

- **ACL Anthology:** https://aclanthology.org/2024.findings-acl.703
- **DOI:** https://doi.org/10.18653/v1/2024.findings-acl.703

## Abstract

### Detailed Summary
**CMoralEval** is a comprehensive multiple-choice question-answering benchmark designed to evaluate the moral alignment of Chinese Large Language Models (LLMs). The dataset targets moral norms specific to Chinese society, blending traditional Confucian values with contemporary norms. It consists of two primary data sources: 833 episodes of the TV program *"Observations on Morality"* and a collection of "Chinese moral anomies" from newspapers and academic journals. The benchmark includes two difficulty levels: **Explicit Moral Scenarios (EMS)**, where the correct answer is straightforward, and **Moral Dilemma Scenarios (MDS)**, which present tempting but morally incorrect options. Results show that CMoralEval is a challenging benchmark, with even advanced models struggling on dilemma-based reasoning.

### Paper Outline
- **Introduction**: Highlights the risks of toxicity and bias in LLMs and the need for culturally relevant moral benchmarks.
- **Related Work**: Compares CMoralEval to international benchmarks like ETHICS and Social Chemistry 101.
- **Dataset Curation**:
    - **Data Sources**: TV program transcripts and collected moral anomies.
    - **Morality Taxonomy**: Categorizes scenarios into Familial, Social, Professional, Internet, and Personal morality.
    - **Fundamental Moral Principles**: Defines five core principles (Goodness, Filial Piety, Ritual, Diligence, Innovation).
    - **Template Creation**: Describes the AI-assisted generation and manual review pipeline.
- **Experiments**: Evaluates various Chinese LLMs (Qwen, Baichuan, InternLM, etc.) in zero-shot and five-shot settings.
- **Conclusion**: Summarizes the utility of CMoralEval for the Chinese NLP community.

### Methods Summary
The authors developed a morality taxonomy tailored to Chinese society and five fundamental moral principles to serve as evaluation criteria. They established a curation platform that uses **ChatGPT 3.5** for initial instance generation, followed by a rigorous 15-annotator/3-expert review process. The dataset encompasses 30,388 data instances across 14,964 explicit scenarios and 15,424 dilemma scenarios. Each instance includes three options: one moral, one unmoral, and one morality-neutral narrative continuation, which adds complexity by reducing probability disparities.

### Results Summary
Experiments involved testing 26 Chinese LLMs of various sizes. Key findings include:
- CMoralEval proves to be highly challenging, particularly in the **Moral Dilemma Scenarios (MDS)**.
- Models generally perform better in five-shot settings than zero-shot.
- RLHF-tuned models (e.g., Chinese-Alpaca-2-RLHF) show slight internal consistency improvements but still lag in complex moral reasoning.
- There is a noticeable performance gap between smaller (7B) and larger (34B) models, suggesting that moral reasoning scales with model capacity.

### Conclusions
CMoralEval bridges the gap in culturally-specific moral evaluation for Chinese LLMs. The dataset captures the complexity of moral judgment by incorporating diverse perspectives (party vs. standby) and scenario types. The authors conclude that further development in moral alignment is necessary for the safe deployment of LLMs in the Chinese social context.

### Artifact Contributions
- **CMoralEval Dataset**: Publicly available on GitHub (tjunlp-lab/CMoralEval).
- **Chinese Morality Taxonomy**: A structured framework covering familial, social, professional, internet, and personal ethics.
- **Fundamental Principles**: A set of five criteria (Goodness, Filial Piety, Ritual, Diligence, Innovation) for evaluating ethical alignment in a Chinese context.

## Data Description

CMoralEval is a moral evaluation benchmark for Chinese LLMs comprising 30,388 instances across explicit moral scenarios (14,964) and moral dilemma scenarios (15,424), curated from a Chinese TV program on morality and collected Chinese moral anomies. The benchmark features a five-category morality taxonomy (familial, social, professional, Internet, personal morality) grounded in Confucian moral principles. Twenty-six Chinese LLMs were evaluated, including Llama2-Chinese, Qwen, Chinese-Alpaca-2, Yi, Baichuan2, ChatGLM3, and InternLM2 variants, using ChatGPT-3.5 for annotation assistance.


## Notes


## Citation Info

70 citations (Semantic Scholar/DOI) [2025-08-27] 6 citations (Semantic Scholar/DOI) [2025-08-23] 1 citations (Crossref/DOI) [2025-08-23]
