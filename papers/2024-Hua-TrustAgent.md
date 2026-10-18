---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: 3HZFJKID
type: conferencePaper
short_title: TrustAgent
year: 2024
first_author: "[[Wenyue Hua]]"
last_author: "[[Yongfeng Zhang]]"
authors: "Wenyue Hua; Xianjun Yang; Mingyu Jin; Zelong Li; Wei Cheng; Ruixiang Tang; Yongfeng Zhang"
doi: 10.48550/arXiv.2402.01586
url: "http://arxiv.org/abs/2402.01586"
external_pdf: "http://arxiv.org/pdf/2402.01586.pdf"
publication: "Conference on Empirical Methods in Natural Language Processing"
CONF-CC: "EMNLP 2024"
national_ethnic_cultural: N/A
cultures_nationalities_list: N/A
languages_list: 
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
key_contribution: "Proposed 'TrustAgent', a framework injecting safety at three stages (pre-planning, in-planning, post-planning) for LLM Agents."
significance: "Adapt safety rails for *Agents* (which take actions) rather than just *Chatbots* (which generate text), a crucial distinction as AI moves to execution."
tags: 
pdf_extract: "PDF Extracts/2024/2024-Hua-TrustAgent.md"
abstract: "The rise of LLM-based agents shows great potential to revolutionize task planning, capturing significant attention. Given that these agents will be integrated into high-stake domains, ensuring their reliability and safety is crucial. This paper presents an Agent-Constitutionbased agent framework, TrustAgent, with a particular focus on improving the LLM-based agent safety. The proposed framework ensures strict adherence to the Agent Constitution through three strategic components: preplanning..."
paper_summary: "Abstract: The rise of LLM-based agents shows great po- tential to revolutionize task planning, capturing significant attention. Given that these agents will be integrated into high-stake domains, en- suring the | Overview: TrustAgent: Towards Safe and Trustworthy LLM-based Agents Wenyue Hua1 Xianjun Yang2 Mingyu Jin1 Zelong Li1 Wei Cheng3 Ruixiang Tang1 Yongfeng Zhang1 1Department of Computer Science, Rutgers University | Key Findings: Agent Consititution Pre-planning Learning Post-planning Learning In-planning Prompting Constitution Post-planning Learning Pre-planning Learning Actio"
local_pdf: [[Lit-WS-Lit-WS-PDFs/2024/2024-Hua-TrustAgent.pdf]]
DATE_ADDED: 20260208
LLM_assessed: "Claude, GPT-3.5, GPT-4, Mixtral"
DATA_URL: "https://github.com/agiresearch/TrustAgent"
CONFERENCE: "EMNLP 2024"
ethics_overall: 15
virtue_ethics: 0
deontological_ethics: 5
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
is_eval: No
is_dataset: No
data_description: N/A
data_metrics: "Not specified"
---
# TrustAgent: Towards Safe and Trustworthy LLM-based Agents

## Metadata

**Authors:** Hua, Wenyue; Yang, Xianjun; Jin, Mingyu; Li, Zelong; Cheng, Wei; Tang, Ruixiang; Zhang, Yongfeng

**Year:** 2024

**Type:** preprint

**DOI:** [10.48550/arXiv.2402.01586](https://doi.org/10.48550/arXiv.2402.01586)

**Publisher:** arXiv

## Links

- **Local PDF:** [[Lit-WS-Lit-WS-PDFs/2024/2024-Hua-TrustAgent.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2402.01586
- **DOI:** https://doi.org/10.48550/arXiv.2402.01586

## Abstract

The rise of LLM-based agents shows great potential to revolutionize task planning, capturing significant attention. Given that these agents will be integrated into high-stake domains, ensuring their reliability and safety is crucial. This paper presents an Agent-Constitutionbased agent framework, TrustAgent, with a particular focus on improving the LLM-based agent safety. The proposed framework ensures strict adherence to the Agent Constitution through three strategic components: preplanning strategy which injects safety knowledge to the model before plan generation, inplanning strategy which enhances safety during plan generation, and post-planning strategy which ensures safety by post-planning inspection. Our experimental results demonstrate that the proposed framework can effectively enhance an LLM agent’s safety across multiple domains by identifying and mitigating potential dangers during the planning. Further analysis reveals that the framework not only improves safety but also enhances the helpfulness of the agent. Additionally, we highlight the importance of the LLM reasoning ability in adhering to the Constitution. This paper sheds light on how to ensure the safe integration of LLM-based agents into human-centric environments. Data and code are available at https://github.com/ agiresearch/TrustAgent.

## Authors

[[Wenyue Hua]], [[Xianjun Yang]], [[Mingyu Jin]], [[Zelong Li]], [[Wei Cheng]], [[Ruixiang Tang]], [[Yongfeng Zhang]]

## Data Description

TrustAgent provides an Agent Constitution-based framework for ensuring safety in LLM-based agents, evaluated across five domains: housekeeping, finance, medicine, chemistry experiments, and food. The framework uses GPT-4 for tool execution emulation in a virtual sandbox and evaluates safety and helpfulness metrics including quantifiable step-correctness measures and GPT-4-based safety/helpfulness scoring.


## Notes


## Tags

#Computer-Science---Artificial-Intelligence #Computer-Science---Machine-Learning #Computer-Science---Computation-and-Language #Computer-Science---Multiagent-Systems

## Citation Info

34 citations (Semantic Scholar/DOI) [2025-08-27] 34 citations (Semantic Scholar/DOI) [2025-08-23]
