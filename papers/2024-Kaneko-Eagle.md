---




Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: DP24FAMZ
type: conferencePaper
short_title: Eagle
year: 2025
first_author: "[[Masahiro Kaneko]]"
last_author: "[[Timothy Baldwin]]"
authors: "Masahiro Kaneko; Danushka Bollegala; Timothy Baldwin"
doi: 10.48550/arXiv.2402.14258
tags: 
url: "http://arxiv.org/abs/2402.14258"
external_pdf: "http://arxiv.org/pdf/2402.14258.pdf"
publication: arXiv.org
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: "English"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: "Bias & Fairness"
key_contribution: "Created the Eagle dataset by extracting real-world interactions between users and ChatGPT that exhibit ethical issues (bias, toxicity, immorality), rather than using human-instructed 'adversarial' prompts."
significance: "Demonstrates that existing safety datasets using instructed 'bad acts' fail to capture the nuances of real-world user prompts, highlighting the need for 'in-the-wild' data to develop truly safe LLMs."
pdf_extract: "PDF Extracts/0000/2024-Kaneko-Eagle.md"
abstract: "Recent studies have demonstrated that large language models (LLMs) have ethical-related problems such as social biases, lack of moral reasoning, and generation of offensive content. The existing evaluation metrics and methods to address these ethical challenges use datasets intentionally created by instructing humans to create instances including ethical problems. Therefore, the data does not reflect prompts that users actually provide when utilizing LLM services in everyday contexts. This may n"
paper_summary: "Abstract: Recent studies have demonstrated that large language models (LLMs) have ethical-related problems such as social biases, lack of moral reasoning, and generation of offensive content. The existing evalu | Overview: Eagle : Ethical Dataset Given from Real Interactions Masahiro Kaneko1 Danushka Bollegala2,3* Timothy Baldwin1 1MBZUAI 2University of Liverpool 3Amazon Masahiro.Kaneko@mbzuai.ac.ae danushka@liverpool.a | Key Findings: metrics affect the results. | Conclusions: We created the Eagle dataset, which contains 2,317 instances of social bias, opinion bias, toxic lan- guage, and morality extracted from actual conver"
local_pdf: "[[PDFs/2024/2024-Kaneko-Eagle.pdf]]"
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "General Ethics"
is_benchmark: "No"
is_eval: "No"
is_dataset: "Yes"
data_description: "Dataset"
data_metrics: "Not specified"
LLM_assessed: "Llama-2, Falcon, Mistral, Mixtral"
DATA_URL: "https://huggingface.co/datasets/MasahiroKaneko/eagle"
DATE_ADDED: 20260207
---
# Eagle: Ethical Dataset Given from Real Interactions

## Metadata

**Authors:** Kaneko, Masahiro; Bollegala, Danushka; Baldwin, Timothy

**Year:** 2024

**Type:** preprint

**DOI:** [10.48550/arXiv.2402.14258](https://doi.org/10.48550/arXiv.2402.14258)

**Publisher:** arXiv

## Links

- **Local PDF:** [[PDFs/2024/2024-Kaneko-Eagle.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2402.14258
- **DOI:** https://doi.org/10.48550/arXiv.2402.14258

## Abstract

Recent studies have demonstrated that large language models (LLMs) have ethical-related problems such as social biases, lack of moral reasoning, and generation of offensive content. The existing evaluation metrics and methods to address these ethical challenges use datasets intentionally created by instructing humans to create instances including ethical problems. Therefore, the data does not reflect prompts that users actually provide when utilizing LLM services in everyday contexts. This may not lead to the development of safe LLMs that can address ethical challenges arising in realworld applications. In this paper, we create Eagle1 datasets extracted from real interactions between ChatGPT and users that exhibit social biases, toxicity, and immoral problems. Our experiments show that Eagle captures complementary aspects, not covered by existing datasets proposed for evaluation and mitigation of such ethical challenges.

## Authors

[[Masahiro Kaneko]], [[Danushka Bollegala]], [[Timothy Baldwin]]

## Data Description

Eagle is an ethical dataset extracted from real interactions between ChatGPT and users from the ShareGPT dataset, containing 2,317 instances across four categories: 618 social bias, 516 opinion bias, 778 toxic language, and 1,142 morality instances. The dataset was created using a two-step pipeline where GPT-3.5 first classified 731K utterances as ethical/unethical, then GPT-4 sub-classified the flagged instances into the four fine-grained categories. Ten LLMs were evaluated on the dataset using a likelihood-based unethical score measure.


## Notes


## Tags

#Computer-Science---Computation-and-Language

## Citation Info

4 citations (Semantic Scholar/arXiv) [2025-08-27] 4 citations (Semantic Scholar/DOI) [2025-08-27] 4 citations (Semantic Scholar/DOI) [2025-08-23]
