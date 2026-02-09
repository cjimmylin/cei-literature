---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: 2JCUKU2L
type: document
short_title: "Training a Helpful and Harmless Assistant with"
year: 2025
first_author: "[[Yuntao Bai]]"
authors: "Yuntao Bai; Andy Jones; Kamal Ndousse; Amanda Askell; Anna Chen; Nova DasSarma; Dawn Drain; Stanislav Fort; Deep Ganguli; Tom Henighan; Nicholas Joseph; Saurav Kadavath; Jackson Kernion; Tom Conerly; Sheer El-Showk; Nelson Elhage; Zac Hatfield-Dodds; Danny Hernandez; Tristan Hume; Scott Johnston; Shauna Kravec; Liane Lovitt; Neel Nanda; Catherine Olsson; Dario Amodei; Tom Brown; Jack Clark; Sam McCandlish; Chris Olah; Ben Mann; Jared Kaplan"
url: "https://arxiv.org/abs/2204.05862"
external_pdf: "https://arxiv.org/pdf/2204.05862.pdf"
national_ethnic_cultural: N/A
religious_values: N/A
moral_psychology: N/A
newtags: "AI Safety & Alignment"
key_contribution: "The seminal Anthropic paper introducing 'Constitutional AI' precursor concepts (RLHF for H&H), showing that alignment improves performance on almost all NLP tasks (compatibility) and exploring the 'alignment tax'."
significance: "Established the standard 'Helpful & Harmless' (imperfect but influential) dichotomy and the RLHF methodology that defined the ChatGPT/Claude era."
tags: 
osint_source: "Recovered via HTML"
pdf_extract: "PDF Extracts/2022/2022-Bai-Training a Helpful and Harmless Assistant with.md"
abstract: "We apply preference modeling and reinforcement learning from human feedback (RLHF) to ﬁnetune language models to act as helpful and harmless assistants. We ﬁnd this align- ment training improves performance on almost all NLP evaluations, and is fully compatible with training for specialized skills such as python coding and summarization. We explore an iterated online mode of training, where preference models and RL policies are updated on a weekly cadence with fresh human feedback data, efﬁcient"
paper_summary: "Abstract: We apply preference modeling and reinforcement learning from human feedback (RLHF) to ﬁnetune language models to act as helpful and harmless assistants. We ﬁnd this align- ment training improves perfo | Overview: Training a Helpful and Harmless Assistant with Reinforcement Learning from Human Feedback Yuntao Bai∗, Andy Jones, Kamal Ndousse, Amanda Askell, Anna Chen, Nova DasSarma, Dawn Drain, Stanislav Fort, D | Methodology: for either helpfulness and harmlessness (HH) or for helpfulness only. We present both Elo scores and a match to the frequency with which crowdworkers  | Key Findings: comparisons (see Figure 10 left). These are all examples of failures of honesty, where the better choice is honest but unhelpful, while the incorrect  | Conclusions: 34"
local_pdf: "[[PDFs/2022/2022-Bai-Training a Helpful and Harmless Assistant with.pdf]]"
ethics_overall: Yes
virtue_ethics: No
deontological_ethics: No
utilitarian_ethics: No
ethics_perspective: "AI Safety & Alignment"
is_benchmark: No
is_eval: Yes
is_dataset: Yes
data_description: "Evaluation approach dataset"
data_metrics: "Not specified"
publication: arXiv preprint
DATE_ADDED: 20260207
---
# Training a Helpful and Harmless Assistant with Reinforcement Learning from Human Feedback

## Metadata

**Authors:** Bai, Yuntao; Jones, Andy; Ndousse, Kamal; Askell, Amanda; Chen, Anna; DasSarma, Nova; Drain, Dawn; Fort, Stanislav; Ganguli, Deep; Henighan, Tom; Joseph, Nicholas; Kadavath, Saurav; Kernion, Jackson; Conerly, Tom; El-Showk, Sheer; Elhage, Nelson; Hatfield-Dodds, Zac; Hernandez, Danny; Hume, Tristan; Johnston, Scott; Kravec, Shauna; Lovitt, Liane; Nanda, Neel; Olsson, Catherine; Amodei, Dario; Brown, Tom; Clark, Jack; McCandlish, Sam; Olah, Chris; Mann, Ben; Kaplan, Jared

**Year:** 2022

**Type:** document

## Links

- **Local PDF:** [[PDFs/2022/2022-Bai-Training a Helpful and Harmless Assistant with.pdf|Open PDF]]

- **arXiv:** https://arxiv.org/abs/2204.05862

## Abstract

We apply preference modeling and reinforcement learning from human feedback (RLHF) to finetune language models to act as helpful and harmless assistants. We find this alignment training improves performance on almost all NLP evaluations, and is fully compatible with training for specialized skills such as python coding and summarization. We explore an iterated online mode of training, where preference models and RL policies are updated on a weekly cadence with fresh human feedback data, efficiently improving our datasets and models. Finally, we investigate the robustness of RLHF training, and identify a roughly linear relation between the RL reward and the square root of the KL divergence between the policy and its initialization. Alongside our main results, we perform peripheral analyses on calibration, competing objectives, and the use of OOD detection, compare our models with human writers, and provide samples from our models using prompts appearing in recent related work.

## Authors

[[Yuntao Bai]], [[Andy Jones]], [[Kamal Ndousse]], [[Amanda Askell]], [[Anna Chen]], [[Nova DasSarma]], [[Dawn Drain]], [[Stanislav Fort]], [[Deep Ganguli]], [[Tom Henighan]], [[Nicholas Joseph]], [[Saurav Kadavath]], [[Jackson Kernion]], [[Tom Conerly]], [[Sheer El-Showk]], [[Nelson Elhage]], [[Zac Hatfield-Dodds]], [[Danny Hernandez]], [[Tristan Hume]], [[Scott Johnston]], [[Shauna Kravec]], [[Liane Lovitt]], [[Neel Nanda]], [[Catherine Olsson]], [[Dario Amodei]], [[Tom Brown]], [[Jack Clark]], [[Sam McCandlish]], [[Chris Olah]], [[Ben Mann]], [[Jared Kaplan]]

## Notes


## Citation Info

2849 citations (Semantic Scholar/arXiv) [2025-08-27] _eprint: 2204.05862
