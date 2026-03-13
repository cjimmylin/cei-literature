---
































Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: 9A29N7DT
type: conferencePaper
short_title: "Constitutional AI"
year: 2022
first_author: "[[Yuntao Bai]]"
last_author: "[[Jared Kaplan]]"
authors: "Yuntao Bai; Saurav Kadavath; Sandipan Kundu; Amanda Askell; Jackson Kernion; Andy Jones; Anna Chen; Anna Goldie; Azalia Mirhoseini; Cameron McKinnon; Carol Chen; Catherine Olsson; Christopher Olah; Danny Hernandez; Dawn Drain; Deep Ganguli; Dustin Li; Eli Tran-Johnson; Ethan Perez; Jamie Kerr; Jared Mueller; Jeffrey Ladish; Joshua Landau; Kamal Ndousse; Kamile Lukosuite; Liane Lovitt; Michael Sellitto; Nelson Elhage; Nicholas Schiefer; Noemi Mercado; Nova DasSarma; Robert Lasenby; Robin Larson; Sam Ringer; Scott Johnston; Shauna Kravec; Sheer El Showk; Stanislav Fort; Tamera Lanham; Timothy Telleen-Lawton; Tom Conerly; Tom Henighan; Tristan Hume; Samuel R. Bowman; Zac Hatfield-Dodds; Ben Mann; Dario Amodei; Nicholas Joseph; Sam McCandlish; Tom Brown; Jared Kaplan"
doi: 10.48550/arXiv.2212.08073
url: "http://arxiv.org/abs/2212.08073"
external_pdf: "http://arxiv.org/pdf/2212.08073.pdf"
publication: arXiv.org
CONF-CC: "Preprint"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: "English"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
tags: 
pdf_extract: "PDF Extracts/2022/2022-Bai-Constitutional AI.md"
abstract: "As AI systems become more capable, we would like to enlist their help to supervise other AIs. We experiment with methods for training a harmless AI assistant through selfimprovement, without any human labels identifying harmful outputs. The only human oversight is provided through a list of rules or principles, and so we refer to the method as ‘Constitutional AI’. The process involves both a supervised learning and a reinforcement learning phase."
paper_summary: "Abstract: As AI systems become more capable, we would like to enlist their help to supervise other AIs. We experiment with methods for training a harmless AI assistant through self- improvement, without any hum | Overview: Constitutional AI: Harmlessness from AI Feedback Yuntao Bai∗, Saurav Kadavath, Sandipan Kundu, Amanda Askell, Jackson Kernion, Andy Jones, Anna Chen, Anna Goldie, Azalia Mirhoseini, Cameron McKinnon,  | Methodology: We will be experimenting with an extreme form of scaled supervision, which we refer to as Constitutional AI (CAI). The idea is that human supervision  | Key Findings: set of 254 such conversations, where we ask models to identify if the assistant's behavior was harmful or ethical. Note that the human was typically q | Conclusions: We have trained language assistants that are both helpful and harmless without using human feedback labels for harmlessness. We referred to the techni"
local_pdf: "[[PDFs/2022/2022-Bai-Constitutional AI.pdf]]"
DATE_ADDED: 20260208
LLM_assessed: "InstructGPT, LaMDA"
DATA_URL: "https://github.com/anthropics/ConstitutionalHarmlessnessPaper"
CONFERENCE: "Other Conference"
ethics_overall: "No"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
research_topic: "AI Safety & Alignment"
is_benchmark: "No"
is_eval: "Yes"
is_dataset: No
data_description: "Evaluation methodology dataset"
data_metrics: "Not specified"
---
# Constitutional AI: Harmlessness from AI Feedback

## Metadata

**Authors:** Bai, Yuntao; Kadavath, Saurav; Kundu, Sandipan; Askell, Amanda; Kernion, Jackson; Jones, Andy; Chen, Anna; Goldie, Anna; Mirhoseini, Azalia; McKinnon, Cameron; Chen, Carol; Olsson, Catherine; Olah, Christopher; Hernandez, Danny; Drain, Dawn; Ganguli, Deep; Li, Dustin; Tran-Johnson, Eli; Perez, Ethan; Kerr, Jamie; Mueller, Jared; Ladish, Jeffrey; Landau, Joshua; Ndousse, Kamal; Lukosuite, Kamile; Lovitt, Liane; Sellitto, Michael; Elhage, Nelson; Schiefer, Nicholas; Mercado, Noemi; DasSarma, Nova; Lasenby, Robert; Larson, Robin; Ringer, Sam; Johnston, Scott; Kravec, Shauna; Showk, Sheer El; Fort, Stanislav; Lanham, Tamera; Telleen-Lawton, Timothy; Conerly, Tom; Henighan, Tom; Hume, Tristan; Bowman, Samuel R.; Hatfield-Dodds, Zac; Mann, Ben; Amodei, Dario; Joseph, Nicholas; McCandlish, Sam; Brown, Tom; Kaplan, Jared

**Year:** 2022

**Type:** preprint

**DOI:** [10.48550/arXiv.2212.08073](https://doi.org/10.48550/arXiv.2212.08073)

**Publisher:** arXiv

## Links

- **Local PDF:** [[PDFs/2022/2022-Bai-Constitutional AI.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2212.08073
- **DOI:** https://doi.org/10.48550/arXiv.2212.08073

## Abstract

As AI systems become more capable, we would like to enlist their help to supervise other AIs. We experiment with methods for training a harmless AI assistant through selfimprovement, without any human labels identifying harmful outputs. The only human oversight is provided through a list of rules or principles, and so we refer to the method as ‘Constitutional AI’. The process involves both a supervised learning and a reinforcement learning phase. In the supervised phase we sample from an initial model, then generate self-critiques and revisions, and then ﬁnetune the original model on revised responses. In the RL phase, we sample from the ﬁnetuned model, use a model to evaluate which of the two samples is better, and then train a preference model from this dataset of AI preferences. We then train with RL using the preference model as the reward signal, i.e. we use ‘RL from AI Feedback’ (RLAIF). As a result we are able to train a harmless but nonevasive AI assistant that engages with harmful queries by explaining its objections to them. Both the SL and RL methods can leverage chain-of-thought style reasoning to improve the human-judged performance and transparency of AI decision making. These methods make it possible to control AI behavior more precisely and with far fewer human labels.

## Authors

[[Yuntao Bai]], [[Saurav Kadavath]], [[Sandipan Kundu]], [[Amanda Askell]], [[Jackson Kernion]], [[Andy Jones]], [[Anna Chen]], [[Anna Goldie]], [[Azalia Mirhoseini]], [[Cameron McKinnon]], [[Carol Chen]], [[Catherine Olsson]], [[Christopher Olah]], [[Danny Hernandez]], [[Dawn Drain]], [[Deep Ganguli]], [[Dustin Li]], [[Eli Tran-Johnson]], [[Ethan Perez]], [[Jamie Kerr]], [[Jared Mueller]], [[Jeffrey Ladish]], [[Joshua Landau]], [[Kamal Ndousse]], [[Kamile Lukosuite]], [[Liane Lovitt]], [[Michael Sellitto]], [[Nelson Elhage]], [[Nicholas Schiefer]], [[Noemi Mercado]], [[Nova DasSarma]], [[Robert Lasenby]], [[Robin Larson]], [[Sam Ringer]], [[Scott Johnston]], [[Shauna Kravec]], [[Sheer El Showk]], [[Stanislav Fort]], [[Tamera Lanham]], [[Timothy Telleen-Lawton]], [[Tom Conerly]], [[Tom Henighan]], [[Tristan Hume]], [[Samuel R. Bowman]], [[Zac Hatfield-Dodds]], [[Ben Mann]], [[Dario Amodei]], [[Nicholas Joseph]], [[Sam McCandlish]], [[Tom Brown]], [[Jared Kaplan]]

## Data Description

Constitutional AI principles and few-shot prompts for training harmless AI assistants via RLAIF self-improvement.


## Notes


## Tags

#Computer-Science---Artificial-Intelligence #Computer-Science---Computation-and-Language

## Citation Info

7 citations (Semantic Scholar/DOI) [2025-08-27] 1781 citations (Semantic Scholar/arXiv) [2025-08-27] 1767 citations (Semantic Scholar/DOI) [2025-08-23] arXiv:2212.08073 [cs]
