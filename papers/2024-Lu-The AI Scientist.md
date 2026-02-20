---








Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: R3D4BBTX
type: conferencePaper
short_title: "The AI Scientist"
year: 2024
first_author: "[[Chris Lu]]"
last_author: "[[David Ha]]"
authors: "Chris Lu; Cong Lu; Robert Tjarko Lange; Jakob Foerster; Jeff Clune; David Ha"
doi: 10.48550/ARXIV.2408.06292
url: "https://arxiv.org/abs/2408.06292"
external_pdf: "https://arxiv.org/pdf/2408.06292.pdf"
publication: arXiv.org
CONF-CC: "Preprint"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: ""
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: American
tags: 
pdf_extract: "PDF Extracts/2024/2024-Lu-The AI Scientist.md"
paper_summary: "Overview: 2024-9-4 The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery Chris Lu1,2,*, Cong Lu3,4,*, Robert Tjarko Lange1,*, Jakob Foerster2,, Jeff Clune3,4,5, and David Ha1, *Equal Cont | Methodology: for low-dimensional diffusion models, aiming to balance global structure and local details in generated samples. The novel architecture incorporates t | Conclusions: In this paper, we introduced The AI Scientist, the first framework designed to fully automate the scientific discovery process, and, as a first demons"
local_pdf: "[[PDFs/2024/2024-Lu-The AI Scientist.pdf]]"
abstract: "One of the grand challenges of artificial general intelligence is developing agents capable of conducting scientific research and discovering new knowledge. While frontier models have already been used as aides to human scientists, e.g. for brainstorming ideas, writing code, or prediction tasks, they still conduct only a small part of the scientific process. This paper presents the first comprehensive framework for fully automatic scientific discovery, enabling frontier large language models to"
DATE_ADDED: 20260208
LLM_assessed: "Claude, GPT-4, DeepSeek, Llama-3"
DATA_URL: "https://github.com/SakanaAI/AI-Scientist"
ethics_overall: "No"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
research_topic: "Machine Learning"
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "No"
data_description: "Evaluation framework"
data_metrics: "Not specified"
CONFERENCE: "Other Conference"
---
# The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery

## Metadata

**Authors:** Lu, Chris; Lu, Cong; Lange, Robert Tjarko; Foerster, Jakob; Clune, Jeff; Ha, David

**Year:** 2024

**Type:** preprint

**DOI:** [10.48550/ARXIV.2408.06292](https://doi.org/10.48550/ARXIV.2408.06292)

**Publisher:** arXiv

## Links

- **Local PDF:** [[PDFs/2024/2024-Lu-The AI Scientist.pdf|Open PDF]]

- **arXiv:** https://arxiv.org/abs/2408.06292
- **DOI:** https://doi.org/10.48550/ARXIV.2408.06292

## Abstract

One of the grand challenges of artificial general intelligence is developing agents capable of conducting scientific research and discovering new knowledge. While frontier models have already been used as aides to human scientists, e.g. for brainstorming ideas, writing code, or prediction tasks, they still conduct only a small part of the scientific process. This paper presents the first comprehensive framework for fully automatic scientific discovery, enabling frontier large language models to perform research independently and communicate their findings. We introduce The AI Scientist, which generates novel research ideas, writes code, executes experiments, visualizes results, describes its findings by writing a full scientific paper, and then runs a simulated review process for evaluation. In principle, this process can be repeated to iteratively develop ideas in an open-ended fashion, acting like the human scientific community. We demonstrate its versatility by applying it to three distinct subfields of machine learning: diffusion modeling, transformer-based language modeling, and learning dynamics. Each idea is implemented and developed into a full paper at a cost of less than $15 per paper. To evaluate the generated papers, we design and validate an automated reviewer, which we show achieves near-human performance in evaluating paper scores. The AI Scientist can produce papers that exceed the acceptance threshold at a top machine learning conference as judged by our automated reviewer. This approach signifies the beginning of a new era in scientific discovery in machine learning: bringing the transformative benefits of AI agents to the entire research process of AI itself, and taking us closer to a world where endless affordable creativity and innovation can be unleashed on the world's most challenging problems. Our code is open-sourced at https://github.com/SakanaAI/AI-Scientist

## Authors

[[Chris Lu]], [[Cong Lu]], [[Robert Tjarko Lange]], [[Jakob Foerster]], [[Jeff Clune]], [[David Ha]]

## Data Description

The paper presents The AI Scientist, a framework for fully automated scientific discovery using LLMs. It evaluates four LLMs (Claude Sonnet 3.5, GPT-4o, DeepSeek Coder, and Llama-3.1 405B) as the backbone for end-to-end paper generation across three ML subfields: diffusion modeling, transformer-based language modeling, and learning dynamics. The automated reviewer component is validated on 500 ICLR 2022 papers from the OpenReview dataset, comparing GPT-4o, Claude Sonnet 3.5, GPT-4o-mini, and Llama 3.1 405B reviewer performance.


## Notes


## Tags

#Artificial-Intelligence-(cs.AI) #FOS--Computer-and-information-sciences #Machine-Learning-(cs.LG) #Computation-and-Language-(cs.CL)
