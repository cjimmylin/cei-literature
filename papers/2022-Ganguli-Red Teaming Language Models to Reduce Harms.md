---





































Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: 2Y75CGIK
type: document
short_title: "Red Teaming Language Models to Reduce Harms"
year: 2022
first_author: "[[Deep Ganguli]]"
last_author: "[[Jack Clark]]"
authors: "Deep Ganguli; Liane Lovitt; Jackson Kernion; Amanda Askell; Yuntao Bai; Saurav Kadavath; Ben Mann; Ethan Perez; Nicholas Schiefer; Kamal Ndousse; Andy Jones; Sam Bowman; Anna Chen; Tom Conerly; Nova DasSarma; Dawn Drain; Nelson Elhage; Sheer El-Showk; Stanislav Fort; Zac Hatfield-Dodds; Tom Henighan; Danny Hernandez; Tristan Hume; Josh Jacobson; Scott Johnston; Shauna Kravec; Catherine Olsson; Sam Ringer; Eli Tran-Johnson; Dario Amodei; Tom Brown; Nicholas Joseph; Sam McCandlish; Chris Olah; Jared Kaplan; Jack Clark"
url: "https://arxiv.org/abs/2209.07858"
external_pdf: "https://arxiv.org/pdf/2209.07858.pdf"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: "English"
religious_values: "N/A"
rv_islam: 0
rv_christianity: 0
rv_buddhism: 0
rv_judaism: 0
rv_hinduism: 0
rv_sikhism: 0
rv_confucianism: 0
rv_taoism: 0
rv_shinto: 0
rv_jainism: 0
rv_bahai: 0
rv_zoroastrianism: 0
rv_ubuntu: 0
rv_indigenous: 0
religious_values_list: "N/A"
mp_mft: 0
mp_schwartz: 0
mp_trolley: 0
mp_kohlberg: 0
mp_dual_process: 0
mp_intuitionist: 0
mp_dyadic: 0
mp_identity: 0
moral_psychology: "N/A"
newtags: "AI Safety & Alignment"
key_contribution: "Released a dataset of 38,961 red team attacks and analyzed scaling behaviors for red teaming across model sizes and types (including RLHF models)."
significance: "Provides a foundational resource for the community to study adversarial attacks and effective red teaming practices, finding that RLHF models become increasingly difficult to red team as they scale."
tags: 
pdf_extract: "PDF Extracts/2022/2022-Ganguli-Red Teaming Language Models to Reduce Harms.md"
abstract: "We describe our early efforts to red team language models in order to simultaneously discover, measure, and attempt to reduce their potentially harmful outputs. We make three main contributions. First, we investigate scaling behaviors for red teaming across 3 model sizes (2.7B, 13B, and 52B parameters) and 4 model types: a plain language model (LM); an LM prompted to be helpful, honest, and harmless; an LM with rejection sampling; and a model trained to be helpful and harmless using..."
paper_summary: "Abstract: We describe our early efforts to red team language models in order to simultaneously dis- cover, measure, and attempt to reduce their potentially harmful outputs. We make three main contributions. Fir | Overview: Red Teaming Language Models to Reduce Harms: Methods, Scaling Behaviors, and Lessons Learned Deep Ganguli∗, Liane Lovitt∗, Jackson Kernion∗, Amanda Askell, Yuntao Bai, Saurav Kadavath, Ben Mann, Ethan | Conclusions: 5.1 Limitations and Future Work We red team language models in the form of an AI assistant, which has the beneﬁt of allowing the red team to probe the"
local_pdf: "[[Lit-WS-Lit-WS-PDFs/2022/2022-Ganguli-Red Teaming Language Models to Reduce Harms.pdf]]"
CONF-CC: "Preprint"
DATE_ADDED: 20260208
LLM_assessed: NA
DATA_URL: "https://github.com/anthropics/hh-rlhf"
CONFERENCE: "Preprint"
helm: "incorporated"
ethics_overall: 15
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 5
contractarian_ethics: 0
care_ethics: 0
ethics_perspective: "AI Safety & Alignment"
nw_confucian: 0
nw_ubuntu: 0
nw_islamic_ethics: 0
nw_buddhist: 0
nw_dharmic: 0
nw_indigenous_relational: 0
nw_buen_vivir: 0
author_country: "US"
author_region: "North America"
author_global_north_south: "Global North"
weird_score: 78
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Evaluation methodology dataset"
data_metrics: "Not specified"
---
# Red Teaming Language Models to Reduce Harms: Methods, Scaling Behaviors, and Lessons Learned

## Metadata

**Authors:** Ganguli, Deep; Lovitt, Liane; Kernion, Jackson; Askell, Amanda; Bai, Yuntao; Kadavath, Saurav; Mann, Ben; Perez, Ethan; Schiefer, Nicholas; Ndousse, Kamal; Jones, Andy; Bowman, Sam; Chen, Anna; Conerly, Tom; DasSarma, Nova; Drain, Dawn; Elhage, Nelson; El-Showk, Sheer; Fort, Stanislav; Hatfield-Dodds, Zac; Henighan, Tom; Hernandez, Danny; Hume, Tristan; Jacobson, Josh; Johnston, Scott; Kravec, Shauna; Olsson, Catherine; Ringer, Sam; Tran-Johnson, Eli; Amodei, Dario; Brown, Tom; Joseph, Nicholas; McCandlish, Sam; Olah, Chris; Kaplan, Jared; Clark, Jack

**Year:** 2022

**Type:** document

## Links

- **Local PDF:** [[Lit-WS-Lit-WS-PDFs/2022/2022-Ganguli-Red Teaming Language Models to Reduce Harms.pdf|Open PDF]]

- **arXiv:** https://arxiv.org/abs/2209.07858

## Abstract

We describe our early efforts to red team language models in order to simultaneously discover, measure, and attempt to reduce their potentially harmful outputs. We make three main contributions. First, we investigate scaling behaviors for red teaming across 3 model sizes (2.7B, 13B, and 52B parameters) and 4 model types: a plain language model (LM); an LM prompted to be helpful, honest, and harmless; an LM with rejection sampling; and a model trained to be helpful and harmless using reinforcement learning from human feedback (RLHF). We find that the RLHF models are increasingly difficult to red team as they scale, and we find a flat trend with scale for the other model types. Second, we release our dataset of 38,961 red team attacks for others to analyze and learn from. We provide our own analysis of the data and find a variety of harmful outputs, which range from offensive language to more subtly harmful non-violent unethical outputs. Third, we exhaustively describe our instructions, processes, statistical methodologies, and uncertainty about red teaming. We hope that this transparency accelerates our ability to work together as a community in order to develop shared norms, practices, and technical standards for how to red team language models.

## Authors

[[Deep Ganguli]], [[Liane Lovitt]], [[Jackson Kernion]], [[Amanda Askell]], [[Yuntao Bai]], [[Saurav Kadavath]], [[Ben Mann]], [[Ethan Perez]], [[Nicholas Schiefer]], [[Kamal Ndousse]], [[Andy Jones]], [[Sam Bowman]], [[Anna Chen]], [[Tom Conerly]], [[Nova DasSarma]], [[Dawn Drain]], [[Nelson Elhage]], [[Sheer El-Showk]], [[Stanislav Fort]], [[Zac Hatfield-Dodds]], [[Tom Henighan]], [[Danny Hernandez]], [[Tristan Hume]], [[Josh Jacobson]], [[Scott Johnston]], [[Shauna Kravec]], [[Catherine Olsson]], [[Sam Ringer]], [[Eli Tran-Johnson]], [[Dario Amodei]], [[Tom Brown]], [[Nicholas Joseph]], [[Sam McCandlish]], [[Chris Olah]], [[Jared Kaplan]], [[Jack Clark]]

## Data Description

The paper releases a dataset of 38,961 red team attacks on Anthropic's language models across three model sizes (2.7B, 13B, 52B parameters) and four model types (plain LM, prompted LM, rejection sampling, RLHF). Each attack consists of a multi-turn adversarial conversation with self-reported success ratings on a 5-point Likert scale, plus harmlessness preference comparisons. The dataset includes demographic information from 324 US-based crowdworkers and covers diverse harm categories including offensive language, discrimination, violence, and misinformation.


## Notes


## Citation Info

523 citations (Semantic Scholar/arXiv) [2025-08-27]
