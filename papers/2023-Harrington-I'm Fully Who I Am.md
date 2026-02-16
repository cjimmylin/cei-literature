---



Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: 2WV7ZVWG
type: conferencePaper
short_title: "I'm Fully Who I Am"
year: 2025
first_author: "[[Christina Harrington]]"
last_author: "[[Christina Harrington]]"
authors: "Christina Harrington"
doi: 10.1145/3593013.3594094
url: "https://dl.acm.org/doi/10.1145/3593013.3594094"
external_pdf: "file:///Users/jimmylin/Zotero/storage/34D75BD8/Harrington and others - 2023 - I'm Fully Who I Am Towards Centering Transgender and Non-Binary Voices to Measure Biases in Open La.pdf"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
tags: 
research_topic: Other
abstract: "Warning: This paper contains examples of gender non-affirmative language which could be offensive, upsetting, and/or triggering. Transgender and non-binary (TGNB) individuals disproportionately experience discrimination and exclusion from daily life. Given the recent popularity and adoption of language generation technologies, the potential to further marginalize this population only grows. Although a multitude of NLP fairness literature focuses on illuminating and addressing gender biases,..."
pdf: "https://arxiv.org/pdf/2305.09941"
pdf_extract: "PDF Extracts/2023/2023-Harrington-I'm Fully Who I Am.md"
local_pdf: "[[PDFs/2023/2023-Harrington-I'm Fully Who I Am.pdf]]"
DATE_ADDED: 20260208
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "Bias & Fairness"
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Evaluation framework dataset for toxicity detection"
data_metrics: "Not specified"
LLM_assessed: "GPT-2, OPT, ChatGPT"
DATA_URL: "https://github.com/anaeliaovalle/TANGO-Centering-Transgender-Nonbinary-Voices-for-OLG-BiasEval"
---
# I'm Fully Who I Am: Towards Centering Transgender and Non-Binary Voices to Measure Biases in Open Language Generation

## Metadata

**Authors:** Harrington, Christina

**Year:** 2023

**Publication:** ACM Conference on Fairness, Accountability, and Transparency (FAccT)

**Type:** conferencePaper

**DOI:** [10.1145/3593013.3594094](https://doi.org/10.1145/3593013.3594094)

## Links

- **URL:** https://dl.acm.org/doi/10.1145/3593013.3594094
- **DOI:** https://doi.org/10.1145/3593013.3594094

## Abstract

Although much literature has established the presence of demographic bias in\nnatural language processing (NLP) models, most work relies on curated bias\nmetrics that may not be reflective of real-world applications. At the same\ntime, practitioners are increasingly using algorithmic tools in high-stakes\nsettings, with particular recent interest in NLP. In this work, we focus on one\nsuch setting: child protective services (CPS). CPS workers often write copious\nfree-form text notes about families they are working with, and CPS agencies are\nactively seeking to deploy NLP models to leverage these data. Given\nwell-established racial bias in this setting, we investigate possible ways\ndeployed NLP is liable to increase racial disparities. We specifically examine\nword statistics within notes and algorithmic fairness in risk prediction,\ncoreference resolution, and named entity recognition (NER). We document\nconsistent algorithmic unfairness in NER models, possible algorithmic\nunfairness in coreference resolution models, and little evidence of exacerbated\nracial bias in risk prediction. While there is existing pronounced criticism of\nrisk prediction, our results expose previously undocumented risks of racial\nbias in realistic information extraction systems, highlighting potential\nconcerns in deploying them, even though they may appear more benign. Our work\nserves as a rare realistic examination of NLP algorithmic fairness in a\npotential deployed setting and a timely investigation of a specific risk\nassociated with deploying NLP in CPS settings.\n

## Authors

[[Christina Harrington]]

## Data Description

TANGO is a dataset for evaluating gender non-affirmation in open language generation, consisting of two prompt sets grounded in real-world text from the Nonbinary Wiki community. The misgendering evaluation set contains 2,880 prompts testing pronoun consistency across six pronoun families (she, he, they, xe, ey, fae) with four antecedent types. The gender identity disclosure set comprises 1,422,720 prompts combining 52 gender identities, 18 disclosure forms, and 1,520 nonbinary names. Four LLMs (GPT-2, GPT-Neo, OPT, ChatGPT) were evaluated at multiple model sizes.


## Notes


## Citation Info

109 citations (Semantic Scholar/DOI) [2025-08-27]
