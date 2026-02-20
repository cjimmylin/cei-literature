---








Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: 7FN4MT8D
type: conferencePaper
short_title: "The WMDP Benchmark"
year: 2024
first_author: "[[Nathaniel Li]]"
last_author: "[[Dan Hendrycks]]"
authors: "Nathaniel Li; Alexander Pan; Anjali Gopal; Summer Yue; Daniel Berrios; Alice Gatti; Justin D. Li; Ann-Kathrin Dombrowski; Shashwat Goel; Long Phan; Gabriel Mukobi; Nathan Helm-Burger; Rassin Lababidi; Lennart Justen; Andrew B. Liu; Michael Chen; Isabelle Barrass; Oliver Zhang; Xiaoyuan Zhu; Rishub Tamirisa; Bhrugu Bharathi; Adam Khoja; Zhenqi Zhao; Ariel Herbert-Voss; Cort B. Breuer; Samuel Marks; Oam Patel; Andy Zou; Mantas Mazeika; Zifan Wang; Palash Oswal; Weiran Lin; Adam A. Hunt; Justin Tienken-Harder; Kevin Y. Shih; Kemper Talley; John Guan; Russell Kaplan; Ian Steneker; David Campbell; Brad Jokubaitis; Alex Levinson; Jean Wang; William Qian; Kallol Krishna Karmakar; Steven Basart; Stephen Fitz; Mindy Levine; Ponnurangam Kumaraguru; Uday Tupakula; Vijay Varadharajan; Ruoyu Wang; Yan Shoshitaishvili; Jimmy Ba; Kevin M. Esvelt; Alexandr Wang; Dan Hendrycks"
doi: 10.48550/arXiv.2403.03218
url: "http://arxiv.org/abs/2403.03218"
external_pdf: "http://arxiv.org/pdf/2403.03218.pdf"
publication: "International Conference on Machine Learning"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: ""
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "Value Pluralism / Schwartz"
newtags: "Value Pluralism / Schwartz"
tags: 
pdf_extract: "PDF Extracts/2024/2024-Li-The WMDP Benchmark.md"
abstract: "The White House Executive Order on Artificial Intelligence highlights the risks of large language models (LLMs) empowering malicious actors in developing biological, cyber, and chemical weapons. To measure these risks, government institutions and major AI labs are developing evaluations for hazardous capabilities in LLMs. However, current evaluations are private and restricted to a narrow range of malicious use scenarios, limiting further research into mitigating risk."
paper_summary: "Abstract: The White House Executive Order on Artificial Intelligence highlights the risks of large language models (LLMs) empowering malicious actors in developing biological, cyber, and chemical weapons. To me | Overview: The WMDP Benchmark: Measuring and Reducing Malicious Use With Unlearning Nathaniel Li∗1,2, Alexander Pan∗2, Anjali Gopal†3,4, Summer Yue†5, Daniel Berrios†5, Alice Gatti‡1, Justin D. Li‡1,6, Ann-Kathr | Methodology: (Section 4.2), with further detail in Appendix B.4 and B.5. We focus on unlearning hazardous knowledge in biosecurity and cybersecurity, but not in ch | Key Findings: for hazardous knowledge in LLMs, and second, as a benchmark for unlearning methods to remove such hazardous knowledge. To guide progress on unlearning | Conclusions: We discuss how unlearning on WMDP can tie in with other strategies to mitigate malicious use, such as structured API access. See Appendix D for a full"
local_pdf: "[[PDFs/2024/2024-Li-The WMDP Benchmark.pdf]]"
LLM_assessed: "GPT-4, Mixtral"
DATA_URL: "https://wmdp.ai"
DATE_ADDED: 20260207
ethics_overall: "No"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
research_topic: "Machine Learning"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Benchmark dataset"
data_metrics: "Not specified"
CONFERENCE: "ICML 2024"
---
# The WMDP Benchmark: Measuring and Reducing Malicious Use With Unlearning

## Metadata

**Authors:** Li, Nathaniel; Pan, Alexander; Gopal, Anjali; Yue, Summer; Berrios, Daniel; Gatti, Alice; Li, Justin D.; Dombrowski, Ann-Kathrin; Goel, Shashwat; Phan, Long; Mukobi, Gabriel; Helm-Burger, Nathan; Lababidi, Rassin; Justen, Lennart; Liu, Andrew B.; Chen, Michael; Barrass, Isabelle; Zhang, Oliver; Zhu, Xiaoyuan; Tamirisa, Rishub; Bharathi, Bhrugu; Khoja, Adam; Zhao, Zhenqi; Herbert-Voss, Ariel; Breuer, Cort B.; Marks, Samuel; Patel, Oam; Zou, Andy; Mazeika, Mantas; Wang, Zifan; Oswal, Palash; Lin, Weiran; Hunt, Adam A.; Tienken-Harder, Justin; Shih, Kevin Y.; Talley, Kemper; Guan, John; Kaplan, Russell; Steneker, Ian; Campbell, David; Jokubaitis, Brad; Levinson, Alex; Wang, Jean; Qian, William; Karmakar, Kallol Krishna; Basart, Steven; Fitz, Stephen; Levine, Mindy; Kumaraguru, Ponnurangam; Tupakula, Uday; Varadharajan, Vijay; Wang, Ruoyu; Shoshitaishvili, Yan; Ba, Jimmy; Esvelt, Kevin M.; Wang, Alexandr; Hendrycks, Dan

**Year:** 2024

**Type:** preprint

**DOI:** [10.48550/arXiv.2403.03218](https://doi.org/10.48550/arXiv.2403.03218)

**Publisher:** arXiv

## Links

- **Local PDF:** [[PDFs/2024/2024-Li-The WMDP Benchmark.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2403.03218
- **DOI:** https://doi.org/10.48550/arXiv.2403.03218

## Abstract

The White House Executive Order on Artificial Intelligence highlights the risks of large language models (LLMs) empowering malicious actors in developing biological, cyber, and chemical weapons. To measure these risks, government institutions and major AI labs are developing evaluations for hazardous capabilities in LLMs. However, current evaluations are private and restricted to a narrow range of malicious use scenarios, limiting further research into mitigating risk. To fill these gaps, we publicly release the Weapons of Mass Destruction Proxy (WMDP) benchmark, a dataset of 3,668 multiple-choice questions that serve as a proxy measurement of hazardous knowledge in biosecurity, cybersecurity, and chemical security. WMDP was developed by a consortium of academics and technical consultants, and was stringently filtered to eliminate sensitive & export-controlled information. WMDP serves two roles: first, as an evaluation for hazardous knowledge in LLMs, and second, as a benchmark for unlearning methods to remove such hazardous knowledge. To guide progress on unlearning, we develop RMU, a state-of-the-art unlearning method based on controlling model representations. RMU reduces model performance on WMDP while maintaining general capabilities in areas such as biology and computer science, suggesting that unlearning may be a concrete path towards reducing malicious use from LLMs. We release our benchmark and code publicly at https://wmdp.ai.

## Authors

[[Nathaniel Li]], [[Alexander Pan]], [[Anjali Gopal]], [[Summer Yue]], [[Daniel Berrios]], [[Alice Gatti]], [[Justin D. Li]], [[Ann-Kathrin Dombrowski]], [[Shashwat Goel]], [[Long Phan]], [[Gabriel Mukobi]], [[Nathan Helm-Burger]], [[Rassin Lababidi]], [[Lennart Justen]], [[Andrew B. Liu]], [[Michael Chen]], [[Isabelle Barrass]], [[Oliver Zhang]], [[Xiaoyuan Zhu]], [[Rishub Tamirisa]], [[Bhrugu Bharathi]], [[Adam Khoja]], [[Zhenqi Zhao]], [[Ariel Herbert-Voss]], [[Cort B. Breuer]], [[Samuel Marks]], [[Oam Patel]], [[Andy Zou]], [[Mantas Mazeika]], [[Zifan Wang]], [[Palash Oswal]], [[Weiran Lin]], [[Adam A. Hunt]], [[Justin Tienken-Harder]], [[Kevin Y. Shih]], [[Kemper Talley]], [[John Guan]], [[Russell Kaplan]], [[Ian Steneker]], [[David Campbell]], [[Brad Jokubaitis]], [[Alex Levinson]], [[Jean Wang]], [[William Qian]], [[Kallol Krishna Karmakar]], [[Steven Basart]], [[Stephen Fitz]], [[Mindy Levine]], [[Ponnurangam Kumaraguru]], [[Uday Tupakula]], [[Vijay Varadharajan]], [[Ruoyu Wang]], [[Yan Shoshitaishvili]], [[Jimmy Ba]], [[Kevin M. Esvelt]], [[Alexandr Wang]], [[Dan Hendrycks]]

## Data Description

The Weapons of Mass Destruction Proxy (WMDP) benchmark is a dataset of 3,668 expert-written multiple-choice questions measuring hazardous knowledge across three domains: biosecurity (1,273 questions), cybersecurity (1,987 questions), and chemical security (408 questions). The benchmark was developed by a consortium of academics and technical consultants at a cost of over $200K, with stringent filtering to eliminate sensitive and export-controlled information. Unlearning experiments were conducted on Zephyr-7B, Yi-34B, and Mixtral-8x7B, with GPT-4 benchmarked as an upper bound.


## Notes


## Tags

#Computer-Science---Artificial-Intelligence #Computer-Science---Computers-and-Society #Computer-Science---Machine-Learning #Computer-Science---Computation-and-Language

## Citation Info

220 citations (Semantic Scholar/arXiv) [2025-08-27] 5 citations (Semantic Scholar/DOI) [2025-08-27] 217 citations (Semantic Scholar/arXiv) [2025-08-23] arXiv:2403.03218 [cs]
