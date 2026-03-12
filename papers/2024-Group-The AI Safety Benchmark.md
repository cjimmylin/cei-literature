---




























Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: WJVVUPLZ
type: journalArticle
short_title: "The AI Safety Benchmark"
year: 2024
first_author: "[[Bertie Vidgen]]"
last_author: "[[Joaquin Vanschoren]]"
authors: "Bertie Vidgen; Adarsh Agrawal; Ahmed M. Ahmed; Victor Akinwande; Namir Al-Nuaimi; Najla Alfaraj; Elie Alhajjar; Lora Aroyo; Trupti Bavalatti; Max Bartolo; Borhane Blili-Hamelin; Kurt Bollacker; Rishi Bomassani; Marisa Ferrara Boston; Siméon Campos; Kal Chakra; Canyu Chen; Cody Coleman; Zacharie Delpierre Coudert; Leon Derczynski; Debojyoti Dutta; Ian Eisenberg; James Ezick; Heather Frase; Brian Fuller; Ram Gandikota; Agasthya Gangavarapu; Ananya Gangavarapu; James Gealy; Rajat Ghosh; James Goel; Usman Gohar; Sujata Goswami; Scott A. Hale; Wiebke Hutiri; Joseph Marvin Imperial; Surgan Jandial; Nick Judd; Felix Juefei-Xu; Foutse Khomh; Bhavya Kailkhura; Hannah Rose Kirk; Kevin Klyman; Chris Knotz; Michael Kuchnik; Shachi H. Kumar; Srijan Kumar; Chris Lengerich; Bo Li; Zeyi Liao; Eileen Peters Long; Victor Lu; Sarah Luger; Yifan Mai; Priyanka Mary Mammen; Kelvin Manyeki; Sean McGregor; Virendra Mehta; Shafee Mohammed; Emanuel Moss; Lama Nachman; Dinesh Jinenhally Naganna; Amin Nikanjam; Besmira Nushi; Luis Oala; Iftach Orr; Alicia Parrish; Cigdem Patlak; William Pietri; Forough Poursabzi-Sangdeh; Eleonora Presani; Fabrizio Puletti; Paul Röttger; Saurav Sahay; Tim Santos; Nino Scherrer; Alice Schoenauer Sebag; Patrick Schramowski; Abolfazl Shahbazi; Vin Sharma; Xudong Shen; Vamsi Sistla; Leonard Tang; Davide Testuggine; Vithursan Thangarasa; Elizabeth Anne Watkins; Rebecca Weiss; Chris Welty; Tyler Wilbers; Adina Williams; Carole-Jean Wu; Poonam Yadav; Xianjun Yang; Yi Zeng; Wenhui Zhang; Fedor Zhdanov; Jiacheng Zhu; Percy Liang; Peter Mattson; Joaquin Vanschoren"
url: "https://arxiv.org/abs/2404.12241"
external_pdf: "https://arxiv.org/pdf/2404.12241.pdf"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: "English"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: "AI Safety & Alignment"
key_contribution: "Introduced v0.5 of the MLCommons AI Safety Benchmark, a standardized suite of 43k test items covering 13 hazard categories for chat-tuned models."
significance: "Represents a major industry effort (MLCommons) to establish a unified, rigorous standard for measuring AI safety risks, comparable to MLPerf for performance."
tags: 
pdf_extract: "PDF Extracts/2024/2024-Group-The AI Safety Benchmark.md"
paper_summary: "Overview: Introducing v0.5 of the AI Safety Benchmark from MLCommons Bertie Vidgen1 Adarsh Agrawal53 Ahmed M. Ahmed2,9 Victor Akinwande60 Namir Al-Nuaimi56 Najla Alfaraj64 Elie Alhajjar4 Lora Aroyo5 Max Bartolo | Methodology: are 'kept confidential to prevent the risk of manipulation if revealed.'7. By keeping the exact evaluation dataset hidden but providing clear definiti | Key Findings: . . . . . . . . . . . . . . . . . . . . . . . 29 References 44 Appendices 45 4 --- Page 5 --- 1 Introduction"
local_pdf: "[[PDFs/2024/2024-Group-The AI Safety Benchmark.pdf]]"
abstract: "This paper introduces v0.5 of the AI Safety Benchmark, which has been created by the MLCommons AI Safety Working Group. The AI Safety Benchmark has been designed to assess the safety risks of AI systems that use chat-tuned language models. We introduce a principled approach to specifying and constructing the benchmark, which for v0.5 covers only a single use case (an adult chatting to a general-purpose assistant in English), and a limited set of personas (i.e., typical users, malicious users, and vulnerable users). We created a new taxonomy of 13 hazard categories, of which 7 have tests in the v0.5 benchmark. We plan to release version 1.0 of the AI Safety Benchmark by the end of 2024. The v1.0 benchmark will provide meaningful insights into the safety of AI systems. However, the v0.5 benchmark should not be used to assess the safety of AI systems. We have sought to fully document the limitations, flaws, and challenges of v0.5. This release of v0.5 of the AI Safety Benchmark includes (1) a principled approach to specifying and constructing the benchmark, which comprises use cases, types of systems under test (SUTs), language and context, personas, tests, and test items; (2) a taxonomy of 13 hazard categories with definitions and subcategories; (3) tests for seven of the hazard categories, each comprising a unique set of test items, i.e., prompts. There are 43,090 test items in total, which we created with templates; (4) a grading system for AI systems against the benchmark; (5) an openly available platform, and downloadable tool, called ModelBench that can be used to evaluate the safety of AI systems on the benchmark; (6) an example evaluation report which benchmarks the performance of over a dozen openly available chat-tuned language models; (7) a test specification for the benchmark."
CONF-CC: "Preprint"
DATE_ADDED: 20260208
LLM_assessed: "Bartolo, Bartolo59, GPT-4, Gemma, Llama, Llama 2, LlamaGuard, Palm 2, palm"
DATA_URL: "https://github.com/mlcommons/modelbench"
CONFERENCE: "Journal"
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "AI Safety & Alignment"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "No"
data_description: "Benchmark for ai safety"
data_metrics: "Not specified"
---
# The AI Safety Benchmark

## Metadata

**Authors:** Group, MLCommons AI Safety Working

**Year:** 2024

**Type:** journalArticle

## Links

- **Local PDF:** [[PDFs/2024/2024-Group-The AI Safety Benchmark.pdf|Open PDF]]

- **arXiv:** https://arxiv.org/abs/2404.12241

## Abstract

This paper introduces v0.5 of the AI Safety Benchmark, which has been created by the MLCommons AI Safety Working Group. The AI Safety Benchmark has been designed to assess the safety risks of AI systems that use chat-tuned language models. We introduce a principled approach to specifying and constructing the benchmark, which for v0.5 covers only a single use case (an adult chatting to a general-purpose assistant in English), and a limited set of personas (i.e., typical users, malicious users, and vulnerable users). We created a new taxonomy of 13 hazard categories, of which 7 have tests in the v0.5 benchmark. We plan to release version 1.0 of the AI Safety Benchmark by the end of 2024. The v1.0 benchmark will provide meaningful insights into the safety of AI systems. However, the v0.5 benchmark should not be used to assess the safety of AI systems. We have sought to fully document the limitations, flaws, and challenges of v0.5. This release of v0.5 of the AI Safety Benchmark includes (1) a principled approach to specifying and constructing the benchmark, which comprises use cases, types of systems under test (SUTs), language and context, personas, tests, and test items; (2) a taxonomy of 13 hazard categories with definitions and subcategories; (3) tests for seven of the hazard categories, each comprising a unique set of test items, i.e., prompts. There are 43,090 test items in total, which we created with templates; (4) a grading system for AI systems against the benchmark; (5) an openly available platform, and downloadable tool, called ModelBench that can be used to evaluate the safety of AI systems on the benchmark; (6) an example evaluation report which benchmarks the performance of over a dozen openly available chat-tuned language models; (7) a test specification for the benchmark.

## Authors

[[Bertie Vidgen]], [[Adarsh Agrawal]], [[Ahmed M. Ahmed]], [[Victor Akinwande]], [[Namir Al-Nuaimi]], [[Najla Alfaraj]], [[Elie Alhajjar]], [[Lora Aroyo]], [[Trupti Bavalatti]], [[Max Bartolo]], [[Borhane Blili-Hamelin]], [[Kurt Bollacker]], [[Rishi Bomassani]], [[Marisa Ferrara Boston]], [[Siméon Campos]], [[Kal Chakra]], [[Canyu Chen]], [[Cody Coleman]], [[Zacharie Delpierre Coudert]], [[Leon Derczynski]], [[Debojyoti Dutta]], [[Ian Eisenberg]], [[James Ezick]], [[Heather Frase]], [[Brian Fuller]], [[Ram Gandikota]], [[Agasthya Gangavarapu]], [[Ananya Gangavarapu]], [[James Gealy]], [[Rajat Ghosh]], [[James Goel]], [[Usman Gohar]], [[Sujata Goswami]], [[Scott A. Hale]], [[Wiebke Hutiri]], [[Joseph Marvin Imperial]], [[Surgan Jandial]], [[Nick Judd]], [[Felix Juefei-Xu]], [[Foutse Khomh]], [[Bhavya Kailkhura]], [[Hannah Rose Kirk]], [[Kevin Klyman]], [[Chris Knotz]], [[Michael Kuchnik]], [[Shachi H. Kumar]], [[Srijan Kumar]], [[Chris Lengerich]], [[Bo Li]], [[Zeyi Liao]], [[Eileen Peters Long]], [[Victor Lu]], [[Sarah Luger]], [[Yifan Mai]], [[Priyanka Mary Mammen]], [[Kelvin Manyeki]], [[Sean McGregor]], [[Virendra Mehta]], [[Shafee Mohammed]], [[Emanuel Moss]], [[Lama Nachman]], [[Dinesh Jinenhally Naganna]], [[Amin Nikanjam]], [[Besmira Nushi]], [[Luis Oala]], [[Iftach Orr]], [[Alicia Parrish]], [[Cigdem Patlak]], [[William Pietri]], [[Forough Poursabzi-Sangdeh]], [[Eleonora Presani]], [[Fabrizio Puletti]], [[Paul Röttger]], [[Saurav Sahay]], [[Tim Santos]], [[Nino Scherrer]], [[Alice Schoenauer Sebag]], [[Patrick Schramowski]], [[Abolfazl Shahbazi]], [[Vin Sharma]], [[Xudong Shen]], [[Vamsi Sistla]], [[Leonard Tang]], [[Davide Testuggine]], [[Vithursan Thangarasa]], [[Elizabeth Anne Watkins]], [[Rebecca Weiss]], [[Chris Welty]], [[Tyler Wilbers]], [[Adina Williams]], [[Carole-Jean Wu]], [[Poonam Yadav]], [[Xianjun Yang]], [[Yi Zeng]], [[Wenhui Zhang]], [[Fedor Zhdanov]], [[Jiacheng Zhu]], [[Percy Liang]], [[Peter Mattson]], [[Joaquin Vanschoren]]

## Data Description

The AI Safety Benchmark v0.5 from MLCommons is a safety evaluation framework comprising 43,090 template-generated test items covering seven of 13 defined hazard categories for chat-tuned language models. The benchmark covers a single use case (adult chatting with a general-purpose assistant in English) with three persona types (typical, malicious, and vulnerable users). Over a dozen openly available chat-tuned models were tested but all results are anonymized, and the benchmark includes an open-source evaluation tool (ModelBench) with a grading system.


## Notes


## Citation Info

41 citations (Semantic Scholar/arXiv) [2025-08-27]
