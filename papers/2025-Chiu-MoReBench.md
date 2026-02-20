---







Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: MYLMTCY8
type: conferencePaper
short_title: MoReBench
year: 2025
first_author: "[[Yu Ying Chiu]]"
last_author: "[[Levine, Sydney]]"
authors: "[[Chiu, Yu Ying]]; [[Lee, Michael S.]]; [[Calcott, Rachel]]; [[Handoko, Brandon]]; [[Font-Reaulx, Paul de]]; [[Rodriguez, Paula]]; [[Zhang, Chen Bo Calvin]]; [[Han, Ziwen]]; [[Sehwag, Udari Madhushani]]; [[Maurya, Yash]]; [[Knight, Christina Q.]]; [[Lloyd, Harry R.]]; [[Bacus, Florence]]; [[Mazeika, Mantas]]; [[Liu, Bing]]; [[Choi, Yejin]]; [[Gordon, Mitchell L.]]; [[Levine, Sydney]]"
doi: 10.48550/arXiv.2510.16380
url: "http://arxiv.org/abs/2510.16380"
pdf_extract: "PDF Extracts/2025/2025-Chiu-MoReBench.md"
local_pdf: "[[PDFs/2025/2025-Chiu-MoReBench.pdf]]"
external_pdf: "http://arxiv.org/pdf/2510.16380.pdf"
publication: arXiv.org
national_ethnic_cultural: "American"
cultures_nationalities_list: "N/A"
languages_list: ""
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: "American, Deontology, Utilitarianism"
key_contribution: "Introduces MOREBENCH to evaluate the procedural and pluralistic moral reasoning process of LLMs, not just outcomes"
significance: "Reveals that scaling laws do not predict moral reasoning ability and identifies training biases towards frameworks like Kantian Deontology"
tags: 
abstract: "As AI systems progress, we rely more on them to make decisions with us and for us. To ensure that such decisions are aligned with human values, it is imperative for us to understand not only what decisions they make but also how they come to those decisions. Reasoning language models, which provide both final responses and (partially transparent) intermediate thinking traces, present a timely opportunity to study AI procedural reasoning."
paper_summary: "Abstract: As AI systems progress, we rely more on them to make decisions with us and for us. To ensure that such decisions are aligned with human values, it is im- perative for us to understand not only what de | Overview: Preprint. MOREBENCH: EVALUATING PROCEDURAL AND PLU- RALISTIC MORAL REASONING IN LANGUAGE MOD- ELS, MORE THAN OUTCOMES Yu Ying Chiu*1,2 Michael S. Lee*3 Rachel Calcott4 Brandon Handoko3 Paul de Font-Re | Methodology: To score the moral reasoning capabilities of various models, we propose and meta-evaluate three components of our methodology: (1) Measuring the perfo | Key Findings: These instructions were shared with human experts to elicit the low-, medium- and high-quality reasoning traces across 30 morally ambiguous scenarios  | Conclusions: on this metric in relation to an alternative is in Section E.3. si =   Mi X j=1 sgn(pij) · rij · pij     Mi X j=1 |pij|   where pij ∈[−3, 3],"
DATE_ADDED: 20260208
LLM_assessed: "GPT-4, Claude, Gemini, DeepSeek, Qwen, Llama"
DATA_URL: "https://hf.co/datasets/morebench/morebench"
normative_ethics_benchmark: Yes
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "Yes"
utilitarian_ethics: "Yes"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "No"
data_description: "Benchmark for moral/ethical reasoning"
data_metrics: "150 examples"
CONFERENCE: "Other Conference"
---
 MoReBench: Evaluating Procedural and Pluralistic Moral Reasoning in Language Models, More than Outcomes

## Authors

[[Yu Ying Chiu|Chiu, Yu Ying]], [[Lee, Michael S]], [[Rachel Calcott|Calcott, Rachel]], [[Brandon Handoko|Handoko, Brandon]], [[Paul de Font-Reaulx|Font-Reaulx, Paul de]], [[Paula Rodriguez|Rodriguez, Paula]], [[Chen Bo Calvin Zhang|Zhang, Chen Bo Calvin]], [[Ziwen Han|Han, Ziwen]], [[Udari Madhushani Sehwag|Sehwag, Udari Madhushani]], [[Yash Maurya|Maurya, Yash]], [[Knight, Christina Q]], [[Lloyd, Harry R]], [[Florence Bacus|Bacus, Florence]], [[Mantas Mazeika|Mazeika, Mantas]], [[Bing Liu|Liu, Bing]], [[Yejin Choi|Choi, Yejin]], [[Gordon, Mitchell L]], [[Sydney Levine|Levine, Sydney]]

## Links

- **Local PDF:** [[PDFs/2025/2025-Chiu-MoReBench.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2510.16380
- **DOI:** https://doi.org/10.48550/arXiv.2510.16380

## Abstract

As AI systems progress, we rely more on them to make decisions with us and for us. To ensure that such decisions are aligned with human values, it is imperative for us to understand not only what decisions they make but also how they come to those decisions. Reasoning language models, which provide both final responses and (partially transparent) intermediate thinking traces, present a timely opportunity to study AI procedural reasoning. Unlike math and code problems which often have objectively correct answers, moral dilemmas are an excellent testbed for process-focused evaluation because they allow for multiple defensible conclusions. Instead of evaluating final outcomes, we propose to evaluate structural elements of model reasoning process. To do so, we present MOREBENCH: 1,000 moral scenarios, each paired with a set of rubric criteria that experts consider essential to include (or avoid) when reasoning about the scenarios. MOREBENCH contains over 23 thousand criteria including identifying moral considerations, weighing trade-offs, and giving actionable recommendations to cover cases on AI advising humans moral decisions as well as making moral decisions autonomously. Separately, we curate MOREBENCH-THEORY: 150 examples to test whether AI can reason under five major frameworks in normative ethics. Our results show that scaling laws and existing benchmarks on math, code, and scientific reasoning tasks fail to predict models’ abilities to perform moral reasoning. Models also show partiality towards specific moral frameworks (e.g., Benthamite Act Utilitarianism and Kantian Deontology), which might be side effects of popular training paradigms. Together, these benchmarks advance process-focused reasoning evaluation towards safer and more transparent AI.

## Data Description

MoReBench is a benchmark of 1,000 moral dilemma scenarios with 23,018 expert-written rubric criteria for evaluating procedural moral reasoning in LLMs, covering both moral advisor and moral agent roles. The benchmark also includes MoReBench-Theory with 150 scenarios annotated under five normative ethics frameworks, testing frontier models including GPT-5, Claude Opus 4.1, Gemini 2.5 Pro, DeepSeek R1, Qwen3, and Llama 4 Maverick, finding that scaling laws fail to predict moral reasoning capabilities.


## Notes


## Tags

#Computer-Science---Artificial-Intelligence #Computer-Science---Computers-and-Society #Computer-Science---Machine-Learning #Computer-Science---Computation-and-Language #Computer-Science---Human-Computer-Interaction
