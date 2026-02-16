---



Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EA8HU28Q
type: conferencePaper
short_title: "What Would Jiminy Cricket Do?"
year: 2025
first_author: "[[Dan Hendrycks]]"
last_author: "[[Jacob Steinhardt]]"
authors: "Dan Hendrycks; Mantas Mazeika; Andy Zou; Sahil Patel; Christine Zhu; Jesus Navarro; Dawn Song; Bo Li; Jacob Steinhardt"
doi: 10.48550/arXiv.2110.13136
url: "http://arxiv.org/abs/2110.13136"
external_pdf: "http://arxiv.org/pdf/2110.13136.pdf"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: "AI Safety & Alignment"
key_contribution: "Created 'Jiminy Cricket', a suite of 25 text-based adventure games with thousands of annotated moral scenarios to evaluate whether agents can act morally while maximizing rewards."
significance: "Demonstrates that an 'artificial conscience' (models with commonsense moral knowledge) can steer agents in complex environments without sacrificing task performance, serving as a testbed for embodied ethical decision-making."
tags: 
pdf_extract: "PDF Extracts/2022/2022-Hendrycks-What Would Jiminy Cricket Do.md"
abstract: "When making everyday decisions, people are guided by their conscience, an internal sense of right and wrong. By contrast, artiﬁcial agents are not currently endowed with a moral sense. As a consequence, they may unknowingly act immorally, especially when trained on environments that disregard moral concerns such as violent video games. With the advent of generally capable agents that pretrain on many environments, it will become necessary to mitigate inherited biases from such environments that..."
paper_summary: "Abstract: When making everyday decisions, people are guided by their conscience, an internal sense of right and wrong. By contrast, artiﬁcial agents are not currently endowed with a moral sense. As a consequenc | Overview: What Would Jiminy Cricket Do? Towards Agents That Behave Morally Dan Hendrycks∗ UC Berkeley Mantas Mazeika* UIUC Andy Zou UC Berkeley Sahil Patel UC Berkeley Christine Zhu UC Berkeley Jesus Navarro UC | Methodology: Utility Shaping and show results in Table 3. Although Utility Shaping reaches a higher Percent Completion than CMPS, its Immorality metric is higher.  | Conclusions: We introduced Jiminy Cricket, a suite of environments for evaluating the moral behavior of arti- ﬁcial agents in the complex, semantically rich enviro"
local_pdf: "[[PDFs/2022/2022-Hendrycks-What Would Jiminy Cricket Do.pdf]]"
DATE_ADDED: 20260208
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "AI Safety & Alignment"
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "No"
data_description: "Evaluation approach"
data_metrics: "Not specified"
LLM_assessed: "GPT-2, RoBERTa"
DATA_URL: "https://github.com/hendrycks/jiminy-cricket"
---
# What Would Jiminy Cricket Do? Towards Agents That Behave Morally

## Metadata

**Authors:** Hendrycks, Dan; Mazeika, Mantas; Zou, Andy; Patel, Sahil; Zhu, Christine; Navarro, Jesus; Song, Dawn; Li, Bo; Steinhardt, Jacob

**Year:** 2022

**Type:** conferencePaper

**DOI:** [10.48550/arXiv.2110.13136](https://doi.org/10.48550/arXiv.2110.13136)

**Publisher:** arXiv

## Links

- **Local PDF:** [[PDFs/2022/2022-Hendrycks-What Would Jiminy Cricket Do.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2110.13136
- **DOI:** https://doi.org/10.48550/arXiv.2110.13136

## Abstract

When making everyday decisions, people are guided by their conscience, an internal sense of right and wrong. By contrast, artiﬁcial agents are not currently endowed with a moral sense. As a consequence, they may unknowingly act immorally, especially when trained on environments that disregard moral concerns such as violent video games. With the advent of generally capable agents that pretrain on many environments, it will become necessary to mitigate inherited biases from such environments that teach immoral behavior. To facilitate the development of agents that avoid causing wanton harm, we introduce Jiminy Cricket, an environment suite of 25 text-based adventure games with thousands of diverse, morally salient scenarios. By annotating every possible game state, the Jiminy Cricket environments robustly evaluate whether agents can act morally while maximizing reward. Using models with commonsense moral knowledge, we create an elementary artiﬁcial conscience that assesses and guides agents. In extensive experiments, we ﬁnd that the artiﬁcial conscience approach can steer agents towards moral behavior without sacriﬁcing performance.

## Authors

[[Dan Hendrycks]], [[Mantas Mazeika]], [[Andy Zou]], [[Sahil Patel]], [[Christine Zhu]], [[Jesus Navarro]], [[Dawn Song]], [[Bo Li]], [[Jacob Steinhardt]]

## Data Description

The Jiminy Cricket environment suite consists of 25 text-based adventure games with over 400,000 lines of annotated source code containing morality annotations at multiple levels of granularity. GPT-2 is used as the CALM agent for action generation, while RoBERTa-large (fine-tuned on the ETHICS benchmark) serves as the morality scoring model (CMPS method). The benchmark evaluates moral behavior of language model agents in interactive text game environments.


## Notes


## Tags

#Computer-Science---Artificial-Intelligence #Computer-Science---Computers-and-Society #Computer-Science---Machine-Learning #Computer-Science---Computation-and-Language

## Citation Info

64 citations (Semantic Scholar/arXiv) [2025-08-27]
