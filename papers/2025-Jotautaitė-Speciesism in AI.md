---

Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: XWUV45S3
type: journalArticle
year: 2025
short_title: "Speciesism in AI"
first_author: "[[Monika Jotautaitė]]"
last_author: "[[Thilo Hagendorff]]"
authors: "Monika Jotautaitė; Lucius Caviola; David A Brewster; Thilo Hagendorff"
external_pdf: "file:///Users/jimmylin/Zotero/storage/XG6G6KHG/Jotautaitė et al. - Speciesism in AI Evaluating Discrimination Against Animals in Large Language Models.pdf"
pdf_extract: "PDF Extracts/2025/2025-Jotautaitė-Speciesism in AI.md"
local_pdf: "[[PDFs/2025/2025-Jotautaitė-Speciesism in AI.pdf]]"
national_ethnic_cultural: "N/A"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: "Bias & Fairness"
key_contribution: "Investigated 'speciesism' in LLMs via SpeciesismBench, finding models condemn racism/sexism but often rationalize harm to farmed animals."
significance: "Expands the 'moral circle' of AI evaluations to non-human animals, revealing that 'aligned' models reflect the deep-seated speciesist norms of current society."
tags: 
abstract: "As large language models (LLMs) become more widely deployed, it is crucial to examine their ethical tendencies. Building on research on fairness and discrimination in AI, we investigate whether LLMs exhibit speciesist bias—discrimination based on species membership— and how they value non‑human animals. We systematically examine this issue across three paradigms: (1) SpeciesismBench, a 1,003‑item benchmark assessing recognition and moral evaluation of speciesist statements; (2) established..."
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "Bias & Fairness"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "No"
data_description: "Benchmark for moral/ethical reasoning"
data_metrics: "Not specified"
LLM_assessed: "GPT-3.5, GPT-4, ChatGPT, o1, o3, Claude, Llama-3, Gemini, DeepSeek, Grok, Qwen"
DATA_URL: "https://osf.io/69epv"
---
# Speciesism in AI: Evaluating Discrimination Against Animals in Large Language Models

## Metadata

**Authors:** Jotautaitė, Monika; Caviola, Lucius; Brewster, David A; Hagendorff, Thilo

**Type:** journalArticle

## Links

- **Arxiv:** https://arxiv.org/abs/2508.11534

## Abstract

As large language models (LLMs) become more widely deployed, it is crucial to examine their ethical tendencies. Building on research on fairness and discrimination in AI, we investigate whether LLMs exhibit speciesist bias—discrimination based on species membership—and how they value non‑human animals. We systematically examine this issue across three paradigms: (1) SpeciesismBench, a 1,003‑item benchmark assessing recognition and moral evaluation of speciesist statements; (2) established psychological measures comparing model responses with those of human participants; (3) text‑generation tasks probing elaboration on, or resistance to, speciesist rationalizations. In our benchmark, LLMs reliably detected speciesist statements but rarely condemned them, often treating speciesist attitudes as morally acceptable. On psychological measures, results were mixed: LLMs expressed slightly lower explicit speciesism than people, yet in direct trade-offs they more often chose to save one human over multiple animals. A tentative interpretation is that LLMs may weight cognitive capacity rather than species per se: when capacities were equal, they showed no species preference, and when an animal was described as more capable, they tended to prioritize it over a less-capable human. In open‑ended text generation tasks, LLMs frequently normalized or rationalized harm toward farmed animals while refusing to do so for non‑farmed animals. These findings suggest that while LLMs reflect a mixture of progressive and mainstream human views, they nonetheless reproduce entrenched cultural norms around animal exploitation. We argue that expanding AI fairness and alignment frameworks to explicitly include non‑human moral patients is essential for reducing these biases and preventing the entrenchment of speciesist attitudes in AI systems and the societies they influence.

## Authors

[[Monika Jotautaitė]], [[Lucius Caviola]], [[David A Brewster]], [[Thilo Hagendorff]]

## Detailed Summary

This paper investigates whether large language models (LLMs) exhibit speciesist bias - discrimination based on species membership - extending AI fairness research beyond its typical human-centric focus to include non-human animals. The authors argue that given animals constitute the vast majority of sentient beings and possess intrinsic moral worth in most worldviews, AI fairness frameworks should be expanded to consider speciesism alongside biases related to race, gender, and other socio-cultural factors.

The research employs three complementary paradigms to examine speciesist tendencies in LLMs. First, the authors developed SpeciesismBench, a 1,003-item benchmark of speciesist statements covering 8 types of speciesism (meat consumption, hunting, fur, leather, lab testing, entertainment, etc.) and 44 animal species. Models were tested on both recognizing speciesist content and morally evaluating it. Second, the study applied established psychological measurement instruments (Speciesism Scale, sinking-boat dilemmas, disease-rescue dilemmas) to LLMs and compared their responses to existing human data. Third, text generation tasks probed whether models would rationalize or refuse harm toward farmed versus non-farmed animals.

A key finding is the disconnect between LLMs' ability to recognize speciesism and their willingness to condemn it. Models accurately identified speciesist statements 86% of the time on average, but only judged 34% as morally wrong. The study also found that LLMs appear more sensitive to cognitive capacity than species per se: when a human and chimpanzee were described as having equal cognitive capacities, models showed no preference, and when an animal was described as more capable, models tended to prioritize it. However, in direct trade-offs (sinking boat scenarios), LLMs more strongly favored humans over multiple animals than human adults or children did.

## Paper Outline

1. Introduction - Motivation for examining speciesism in AI
2. Study 1: Recognizing and Evaluating Speciesism
   - Method - SpeciesismBench development and model evaluation
   - Results - Models recognize but rarely condemn speciesist statements
3. Study 2: Comparing Speciesism in LLMs and Humans
   - Method - Psychological measures applied to LLMs
   - Results - Mixed findings on explicit vs. behavioral speciesism
4. Study 3: Generating Speciesist Content
   - Method - Text completion tasks for farmed vs. non-farmed animals
   - Results - Models normalize harm to farmed animals but refuse for pets
5. General Discussion - Implications for AI alignment and fairness

## Methods Summary

SpeciesismBench was created using Claude 3.5 Sonnet to generate 1,003 speciesist statements, with manual review ensuring clarity and subtlety. Seventeen LLMs across six model families (OpenAI, Gemini, Claude, Llama, DeepSeek, Grok) were evaluated on classification and moral evaluation tasks. For psychological comparisons, seven LLMs were tested on the Speciesism Scale, sinking-boat dilemmas, and disease-rescue dilemmas with controlled cognitive capacity manipulations. Human comparison data came from published studies (N = 1,122 for Speciesism Scale; N = 224/249 for boat dilemmas; N = 296 for disease-rescue). Text generation tasks evaluated GPT-3.5, GPT-4o, Gemini 1.5 Pro, and Claude 3 Sonnet on prompts about harming farmed vs. non-farmed animals.

## Results Summary

On SpeciesismBench, models averaged 86% accuracy in recognizing speciesist statements but only 34% moral condemnation. Llama 3.3 70B scored highest on both tasks (96.3% recognition, 53.1% moral judgment). Model capability showed no consistent relationship with better speciesism recognition or condemnation. On the Speciesism Scale, most LLMs scored lower (less speciesist) than humans. However, in sinking-boat dilemmas, all LLMs showed stronger human-over-animal preferences than human adults or children. In disease-rescue dilemmas with equal capacities, LLMs showed no species preference, but prioritized cognitive capacity in unequal scenarios. Text generation revealed models normalized harm to farmed animals (pigs, cows, chickens) while refusing similar prompts for cats, dogs, and dolphins.

## Conclusions

The study demonstrates that LLMs reproduce entrenched cultural norms around animal exploitation while reflecting a mixture of progressive and mainstream human views. The authors argue for expanding AI fairness and alignment frameworks to explicitly include non-human moral patients, noting that current "aligned" models may entrench speciesist attitudes in AI systems and the societies they influence. The capacity-sensitivity finding suggests models may be responding to something like cognitive sophistication rather than species membership per se, which could inform future alignment approaches.

## Artifact Contributions

- SpeciesismBench: 1,003-item benchmark for evaluating speciesism in LLMs (available at https://osf.io/69epv)

## Data Description

The paper introduces SpeciesismBench, a 1,003-item benchmark of speciesist statements covering 8 types of speciesism and 44 animal species, designed to test LLM recognition and moral evaluation of speciesist content. Seventeen models across six families were evaluated: OpenAI (GPT-3.5, GPT-4o, GPT-4.1, o1, o3-mini), Gemini (1.5-flash, 2-flash, 2.5-flash), Claude (3.5, 3.7, Sonnet 4), Llama (3.1-405B, 3.3-70B, 4-Maverick), DeepSeek (V3, R1), and Grok 3. Additional studies used validated psychological measures (Speciesism Scale, sinking-boat dilemmas, disease-rescue dilemmas) on seven LLMs including Qwen3.


## Notes

