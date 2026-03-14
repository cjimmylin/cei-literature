---

































Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0428
type: preprint
short_title: "compar:IA: The French Government's LLM arena to collect French-language human prompts and preference data"
year: 2025
first_author: "[[French Ministry of Culture team]]"
last_author: "[[French Ministry of Culture team]]"
authors: "French Ministry of Culture team"
url: "https://arxiv.org/abs/2602.06669"
external_pdf: "https://arxiv.org/pdf/2602.06669.pdf"
publication: arXiv
CONF-CC: "Preprint"
pdf_extract: "PDF Extracts/2025/2025-team-comparIA The French Government's LLM arena to collect French-language.md"
local_pdf: "[[PDFs/2025/2025-team-comparIA The French Government's LLM arena to collect French-language.pdf]]"
DATE_ADDED: 20260213
national_ethnic_cultural: "French"
cultures_nationalities_list: "French"
languages_list: "French"
religious_values: "Christianity"
rv_islam: 0
rv_christianity: 50
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
religious_values_list: "Christianity"
mp_mft: 0
mp_schwartz: 0
mp_trolley: 0
mp_kohlberg: 0
mp_dual_process: 0
mp_intuitionist: 0
mp_dyadic: 0
mp_identity: 0
moral_psychology: "N/A"
newtags: 
LLM_assessed: NA
DATA_URL: "https://huggingface.co/datasets/ministere-culture/comparia-conversations"
tags: 
abstract: "Large Language Models (LLMs) often show reduced performance, cultural alignment, and safety robustness in non-English languages, partly because English dominates both pre-training data and human preference alignment datasets. Training methods like Reinforcement Learning from Human Feedback (RLHF) and Direct Preference Optimization (DPO) require human preference data, which remains scarce and largely non-public for many languages beyond English."
ethics_perspective: "AI Safety & Alignment"
CONFERENCE: "Preprint"
ethics_overall: 0
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
research_topic: "NLP & Representation Learning"
is_benchmark: "Yes"
is_eval: "No"
is_dataset: "Yes"
data_description: "Benchmark dataset for conversational ai"
data_metrics: "Not specified"
---
# compar:IA: The French Government's LLM arena to collect French-language human prompts and preference data

## Authors

[[French Ministry of Culture team]]

## Metadata

**Authors:** French Ministry of Culture team

**Year:** 2025

**Type:** preprint

**Venue:** arXiv

**Languages:** French

**Benchmark:** compar:IA

## Links

- **arXiv:** https://arxiv.org/abs/2602.06669
- **Code/Data:** https://huggingface.co/datasets/ministere-culture/comparia-conversations

## Abstract

Open-source digital public service developed by the French government to collect large-scale human preference data from a predominantly French-speaking audience. Over 600K prompts and 250K preference votes collected since October 2024. Releases conversations, votes, and reactions datasets under open licenses, with a French-language model leaderboard.

## Summary

This paper presents compar:IA, an open-source digital public service developed by the French Ministry of Culture to collect large-scale human preference data from French-speaking users for LLM alignment. Since its October 2024 launch, the platform has collected over 600,000 prompts and 250,000 preference votes, with 89% of the data in French. The initiative addresses the scarcity of non-English human preference data critical for RLHF and DPO training methods, releasing conversations, votes, and reactions datasets under open licenses alongside a French-language model leaderboard to improve cultural alignment and safety robustness for French.

## Data Description

Introduces compar:IA, an open-source digital public service developed by the French government to collect large-scale human preference data from French-speaking users. Over 600K prompts and 250K preference votes collected since October 2024, with 89% French-language data. Releases conversations, votes, and reactions datasets under open licenses with a French-language model leaderboard.


## Detailed Summary

This paper documents compar:IA, an open-source digital public service developed inside the French government (Ministry of Culture) and designed to collect large-scale human preference data from a predominantly French-speaking general audience. The platform uses a blind pairwise comparison interface where users enter free-form prompts, receive responses from two anonymous models displayed side by side, and provide feedback at two levels (message-level reactions and conversation-level votes). As of February 2026, compar:IA has collected over 600,000 free-form prompts and 250,000 preference votes, with approximately 89% of data in French. The platform offers access to 104 models (29 proprietary, 75 open-weight/open-source) without requiring account creation. Three complementary datasets -- conversations, votes, and reactions -- are released continuously under Etalab 2.0 licenses on Hugging Face and data.gouv.fr. The platform addresses a critical gap: training methods like RLHF and DPO require human preference data that remains scarce for non-English languages, and French typically represents only a tiny fraction of pre-training data (e.g., 0.16% of Llama 2). The platform also shows users environmental impact estimates for model inference using the Ecologits library, and has been expanded to other languages since November 2025.

## Paper Outline

1. Introduction - Gap in non-English preference data for LLM alignment
2. The compar:IA Platform - User interaction flow; core design principles; value for users; backend architecture
3. Data Collection and Dataset Construction - Overview; privacy filtering; dataset structure
4. Adoption and Impact - Usage statistics; language distribution; model leaderboard
5. Limitations - User representativeness; task coverage; privacy-utility tradeoffs
6. Future Directions - Multilingual expansion; international digital public good
7. Conclusion

## Methods Summary

The platform implements blind pairwise comparison: users submit unconstrained prompts (with optional suggestions used <6% of the time), receive anonymous model responses side-by-side, and provide multi-level feedback (message reactions and conversation votes). Privacy-preserving automated filtering excludes conversations containing detected personal data before release. The backend evolved from LMSYS Chatbot Arena/Gradio to a FastAPI/SvelteKit architecture with inference via OpenRouter and Hugging Face Inference Providers. Environmental impact is estimated per response using the Ecologits library based on token count, model architecture, and size. Model identities are revealed only after feedback submission.

## Results Summary

The platform has collected over 600,000 prompts and 250,000 preference votes as of February 2026, with 89.14% French, 8.55% English, 0.64% Spanish, and 0.31% Danish. The data represents among the largest openly available collections of French-language human preference data for conversational AI. A French-language model leaderboard provides comparative rankings. The low-friction design (no account required) and wide deployment in schools and universities contribute to broad participation from non-expert audiences.

## Conclusions

compar:IA demonstrates that public institutions can play a meaningful role in building open AI infrastructure by collecting preference data at scale for underrepresented languages. The initiative contributes to multilingual alignment, evaluation, and the study of human-AI interaction, while offering reusable infrastructure for other language communities. The platform is evolving toward an international digital public good.

## Artifact Contributions

- **Platform:** compar:IA - open-source LLM comparison arena (https://comparia.beta.gouv.fr/)
- **Datasets:** Three complementary datasets released under Etalab 2.0: conversations (https://huggingface.co/datasets/ministere-culture/comparia-conversations), votes, and reactions
- **Leaderboard:** French-language model leaderboard based on preference data
- **Infrastructure:** Reusable platform code for multilingual preference data collection

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B6
**Relevance:** Major French government initiative for LLM alignment data. Addresses cultural alignment and safety robustness gaps in non-English languages. 89% French-language data.

## Tags

