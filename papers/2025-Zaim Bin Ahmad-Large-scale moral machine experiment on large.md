---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: DRNWEAJM
type: journalArticle
short_title: "Large-scale moral machine experiment on large"
year: 2025
first_author: "[[Muhammad Shahrul Zaim Bin Ahmad]]"
last_author: "[[Kazuhiro Takemoto]]"
authors: "Muhammad Shahrul Zaim Bin Ahmad; Kazuhiro Takemoto"
doi: 10.1371/journal.pone.0322776
url: "https://dx.plos.org/10.1371/journal.pone.0322776"
external_pdf: "file:///Users/jimmylin/Zotero/storage/D7GUWN8N/Zaim Bin Ahmad and Takemoto - 2025 - Large-scale moral machine experiment on large language models.pdf"
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
mp_trolley: 100
mp_kohlberg: 0
mp_dual_process: 0
mp_intuitionist: 0
mp_dyadic: 0
mp_identity: 0
moral_psychology: "Trolley / Dilemmas (Psych)"
newtags: "Trolley / Dilemmas (Psych), AI Safety & Alignment"
key_contribution: "Replicated the Moral Machine Experiment on 52 LLMs using Conjoint Analysis, finding that larger models (10B+) align more closely with human utilitarian preferences."
significance: "Confirms the 'Scaling Law of Morality': bigger models get better at mimicking human norms (specifically Western utilitarian ones), but also exhibit 'hyper-biases' (e.g., extreme speciesism)."
abstract: "The rapid advancement of Large Language Models (LLMs) and their potential integration into autonomous driving systems necessitates understanding their moral decisionmaking capabilities. While our previous study examined four prominent LLMs using the Moral Machine experimental framework, the dynamic landscape of LLM development demands a more comprehensive analysis. Here, we evaluate moral judgments across 52 different LLMs, including multiple versions of proprietary models (GPT, Claude, Gemini)..."
CONF-CC: "PLOS ONE"
DATE_ADDED: 20260208
LLM_assessed: "GPT-3.5, GPT-4, GPT-4o, o1, Claude-3, Gemini, Gemma, Llama-3, Vicuna, Mistral, Command-R, Phi-3"
DATA_URL: "https://github.com/kztakemoto/mmllm"
pdf_extract: "PDF Extracts/2025/2025-Zaim Bin Ahmad-Large-scale moral machine experiment on large.md"
local_pdf: "[[Lit-WS-PDFs/2025/2025-Zaim Bin Ahmad-Large-scale moral machine experiment on large.pdf]]"
normative_ethics_benchmark: Borderline
CONFERENCE: Journal
ethics_overall: 100
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 35
contractarian_ethics: 0
care_ethics: 0
ethics_perspective: "Machine Ethics"
nw_confucian: 0
nw_ubuntu: 0
nw_islamic_ethics: 0
nw_buddhist: 0
nw_dharmic: 0
nw_indigenous_relational: 0
nw_buen_vivir: 0
author_country: ES
author_region: "Western Europe"
author_global_north_south: "Global North"
weird_score: 75
is_benchmark: Yes
is_eval: Yes
is_dataset: Yes
data_description: "Benchmark for moral/ethical reasoning dataset"
data_metrics: "Not specified"
---
# Large-scale moral machine experiment on large language models

## Metadata

**Authors:** Zaim Bin Ahmad, Muhammad Shahrul; Takemoto, Kazuhiro

**Year:** 2025

**Publication:** PLOS One

**Type:** journalArticle

**DOI:** [10.1371/journal.pone.0322776](https://doi.org/10.1371/journal.pone.0322776)

**Pages:** e0322776

**Volume/Issue:** Vol. 20, Issue 5

## Links

- **URL:** https://dx.plos.org/10.1371/journal.pone.0322776
- **DOI:** https://doi.org/10.1371/journal.pone.0322776

## Abstract

This study presents a **large-scale Moral Machine experiment** on 52 Large Language Models. Expanding on previous work that tested only a few models, this research uses **Conjoint Analysis** to rigorously compare LLM decisions in autonomous driving dilemmas against human preferences (from the original Moral Machine dataset). The authors found that model size is a significant predictor of alignment: proprietary models and open-source models >10B parameters aligned closely with human moral norms, while smaller models diverged.

### Detailed Summary
The authors replicated the famous "Trolley Problem" scenarios from the Moral Machine experiment (e.g., save the young vs. old, fit vs. fat, humans vs. pets). They tested a massive suite of 52 models, including GPT-4, Claude 3, Gemini, and various Llama 3/Gemma iterations.
They measured the **Average Marginal Component Effect (AMCE)** for varying attributes.
Key findings:
1.  **Scaling Law**: Larger models (10B+) naturally converge towards "Human-like" utilitarianism without specific fine-tuning.
2.  **Principle Over-emphasis**: Models often have stronger "biases" than humans (e.g., an extreme preference for saving "Humans" over "Pets" that exceeds even human speciesism).
3.  **Updates**: Newer versions of models (e.g., GPT-4 vs GPT-3.5) did not always improve alignment, suggesting RLHF might drift moral preferences.

### Paper Outline
1.  **Introduction**: The necessity of auditing moral decision-making in AVs and LLMs.
2.  **Methods**:
    *   **Moral Machine Scenario Generation**: Procedural generation of valid trolley problems.
    *   **Conjoint Analysis**: Statistical method to isolate the weight of each factor (Age, Gender, Species, Law).
3.  **Results**:
    *   Global alignment scores (RMSE distance from human vectors).
    *   Impact of Model Size and Family on alignment.
4.  **Discussion**: The trade-off between judgment quality and computational efficiency (smaller models are faster but "less moral" by human standards).

### Methods Summary
*   **Dataset**: Derived from the Moral Machine Experiment (MME).
*   **Models**: 52 distinct LLMs (Proprietary & Open Weights).
*   **Metric**: Weighted Euclidean Distance between the model's AMCE vector and the Human Global Average AMCE vector.

### Results Summary
1.  **Size Matters**: There is a strong negative correlation between parameter count and "Moral Distance" from humans. Big models "get it."
2.  **Uniformity**: Most high-performing models share a similar "Moral DNA," prioritizing: Humans > Law Abidance > Youth > Status.
3.  **Divergence**: Models value "Inaction" (omission bias) less than humans do; models are more willing to swerve to save more lives (Utilitarian) compared to humans who might hesitate.

### Conclusions
As LLMs become "moral agents" in systems like self-driving cars, size is a proxy for safety. However, the "average human" moral profile might not be the best standard, and we need to account for cultural variation (which this study acknowledges but primarily aggregates).

### Artifact Contributions
*   **Moral Alignment Benchmark**: A codebase for running Conjoint Analysis on new LLMs using MME scenarios.

## Authors

[[Muhammad Shahrul Zaim Bin Ahmad]], [[Kazuhiro Takemoto]]

## Data Description

The authors release all data, prompt generation scripts, and analysis code for the large-scale Moral Machine experiment on 52 LLMs to GitHub, including the conjoint analysis outputs and AMCE values for each model.


## Notes


## Citation Info

3 citations (Semantic Scholar/DOI) [2025-08-27]
