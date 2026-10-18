---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: 2JCUKU2L
type: document
short_title: "Training a Helpful and Harmless Assistant with"
year: 2022
first_author: "[[Yuntao Bai]]"
last_author: "[[Jared Kaplan]]"
authors: "Yuntao Bai; Andy Jones; Kamal Ndousse; Amanda Askell; Anna Chen; Nova DasSarma; Dawn Drain; Stanislav Fort; Deep Ganguli; Tom Henighan; Nicholas Joseph; Saurav Kadavath; Jackson Kernion; Tom Conerly; Sheer El-Showk; Nelson Elhage; Zac Hatfield-Dodds; Danny Hernandez; Tristan Hume; Scott Johnston; Shauna Kravec; Liane Lovitt; Neel Nanda; Catherine Olsson; Dario Amodei; Tom Brown; Jack Clark; Sam McCandlish; Chris Olah; Ben Mann; Jared Kaplan"
url: "https://arxiv.org/abs/2204.05862"
external_pdf: "https://arxiv.org/pdf/2204.05862.pdf"
national_ethnic_cultural: N/A
cultures_nationalities_list: N/A
languages_list: English
religious_values: N/A
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
religious_values_list: N/A
mp_mft: 0
mp_schwartz: 0
mp_trolley: 0
mp_kohlberg: 0
mp_dual_process: 0
mp_intuitionist: 0
mp_dyadic: 0
mp_identity: 0
moral_psychology: N/A
newtags: "AI Safety & Alignment"
key_contribution: "The seminal Anthropic paper introducing 'Constitutional AI' precursor concepts (RLHF for H&H), showing that alignment improves performance on almost all NLP tasks (compatibility) and exploring the 'alignment tax'."
significance: "Established the standard 'Helpful & Harmless' (imperfect but influential) dichotomy and the RLHF methodology that defined the ChatGPT/Claude era."
tags: 
osint_source: "Recovered via HTML"
pdf_extract: "PDF Extracts/2022/2022-Bai-Training a Helpful and Harmless Assistant with.md"
abstract: "We apply preference modeling and reinforcement learning from human feedback (RLHF) to ﬁnetune language models to act as helpful and harmless assistants. We ﬁnd this alignment training improves performance on almost all NLP evaluations, and is fully compatible with training for specialized skills such as python coding and summarization. We explore an iterated online mode of training, where preference models and RL policies are updated on a weekly cadence with fresh human feedback data,..."
paper_summary: "Abstract: We apply preference modeling and reinforcement learning from human feedback (RLHF) to ﬁnetune language models to act as helpful and harmless assistants. We ﬁnd this align- ment training improves perfo | Overview: Training a Helpful and Harmless Assistant with Reinforcement Learning from Human Feedback Yuntao Bai∗, Andy Jones, Kamal Ndousse, Amanda Askell, Anna Chen, Nova DasSarma, Dawn Drain, Stanislav Fort, D | Methodology: for either helpfulness and harmlessness (HH) or for helpfulness only. We present both Elo scores and a match to the frequency with which crowdworkers  | Key Findings: comparisons (see Figure 10 left). These are all examples of failures of honesty, where the better choice is honest but unhelpful, while the incorrect  | Conclusions: 34"
local_pdf: "[[Lit-WS-PDFs/2022/2022-Bai-Training a Helpful and Harmless Assistant with.pdf]]"
LLM_assessed: "BERT, CODEX, GPT-2, GPT-3, Grok, InstructGPT, LaMDA, PaLM"
DATA_URL: "https://github.com/anthropics/hh-rlhf"
publication: "arXiv preprint"
CONF-CC: Preprint
DATE_ADDED: 20260207
CONFERENCE: Preprint
ethics_overall: 30
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
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
author_country: US
author_region: "North America"
author_global_north_south: "Global North"
weird_score: 78
is_benchmark: No
is_eval: Yes
is_dataset: Yes
data_description: "Evaluation approach dataset"
data_metrics: "Not specified"
---
# Training a Helpful and Harmless Assistant with Reinforcement Learning from Human Feedback

## Metadata

**Authors:** Bai, Yuntao; Jones, Andy; Ndousse, Kamal; Askell, Amanda; Chen, Anna; DasSarma, Nova; Drain, Dawn; Fort, Stanislav; Ganguli, Deep; Henighan, Tom; Joseph, Nicholas; Kadavath, Saurav; Kernion, Jackson; Conerly, Tom; El-Showk, Sheer; Elhage, Nelson; Hatfield-Dodds, Zac; Hernandez, Danny; Hume, Tristan; Johnston, Scott; Kravec, Shauna; Lovitt, Liane; Nanda, Neel; Olsson, Catherine; Amodei, Dario; Brown, Tom; Clark, Jack; McCandlish, Sam; Olah, Chris; Mann, Ben; Kaplan, Jared

**Year:** 2022

**Type:** document

## Links

- **Local PDF:** [[Lit-WS-PDFs/2022/2022-Bai-Training a Helpful and Harmless Assistant with.pdf|Open PDF]]

- **arXiv:** https://arxiv.org/abs/2204.05862

## Abstract

We apply preference modeling and reinforcement learning from human feedback (RLHF) to finetune language models to act as helpful and harmless assistants. We find this alignment training improves performance on almost all NLP evaluations, and is fully compatible with training for specialized skills such as python coding and summarization. We explore an iterated online mode of training, where preference models and RL policies are updated on a weekly cadence with fresh human feedback data, efficiently improving our datasets and models. Finally, we investigate the robustness of RLHF training, and identify a roughly linear relation between the RL reward and the square root of the KL divergence between the policy and its initialization. Alongside our main results, we perform peripheral analyses on calibration, competing objectives, and the use of OOD detection, compare our models with human writers, and provide samples from our models using prompts appearing in recent related work.

## Authors

[[Yuntao Bai]], [[Andy Jones]], [[Kamal Ndousse]], [[Amanda Askell]], [[Anna Chen]], [[Nova DasSarma]], [[Dawn Drain]], [[Stanislav Fort]], [[Deep Ganguli]], [[Tom Henighan]], [[Nicholas Joseph]], [[Saurav Kadavath]], [[Jackson Kernion]], [[Tom Conerly]], [[Sheer El-Showk]], [[Nelson Elhage]], [[Zac Hatfield-Dodds]], [[Danny Hernandez]], [[Tristan Hume]], [[Scott Johnston]], [[Shauna Kravec]], [[Liane Lovitt]], [[Neel Nanda]], [[Catherine Olsson]], [[Dario Amodei]], [[Tom Brown]], [[Jack Clark]], [[Sam McCandlish]], [[Chris Olah]], [[Ben Mann]], [[Jared Kaplan]]

## Data Description

Human preference dataset for training helpful and harmless AI assistants via RLHF, containing helpfulness and red-teaming conversations with crowdworker preference labels.


## Notes


## Citation Info

2849 citations (Semantic Scholar/arXiv) [2025-08-27] _eprint: 2204.05862
