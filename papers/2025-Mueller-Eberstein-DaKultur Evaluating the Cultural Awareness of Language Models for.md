---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0486
type: preprint
short_title: "DaKultur: Evaluating the Cultural Awareness of Language Models for Danish with Native Speakers"
year: 2025
first_author: "[[Max Mueller-Eberstein]]"
last_author: "[[Max Mueller-Eberstein]]"
authors: "Max Mueller-Eberstein et al."
url: "https://arxiv.org/abs/2504.02403"
external_pdf: "https://arxiv.org/pdf/2504.02403.pdf"
publication: "arXiv / C3NLP 2025"
pdf_extract: "PDF Extracts/2025/2025-Mueller-Eberstein-DaKultur Evaluating the Cultural Awareness of Language Models for.md"
local_pdf: "[[PDFs/2025/2025-Mueller-Eberstein-DaKultur Evaluating the Cultural Awareness of Language Models for.pdf]]"
DATE_ADDED: 20260213
ethics_overall: No
virtue_ethics: No
deontological_ethics: No
utilitarian_ethics: No
national_ethnic_cultural: N/A
languages_list: Danish
religious_values: N/A
religious_values_list: N/A
moral_psychology: N/A
newtags: 
is_benchmark: No
is_eval: Yes
is_dataset: Yes
data_description: "Evaluation approach dataset"
data_metrics: "Not specified"
LLM_assessed: NA
DATA_URL: "https://mxij.me/x/dakultur"
tags: 
abstract: "Large Language Models (LLMs) have seen widespread societal adoption. However, while they are able to interact with users in languages beyond English, they have been shown to lack cultural awareness, providing anglocentric or inappropriate responses for underrepresented language communities. To investigate this gap and disentangle linguistic versus cultural proficiency, we conduct the first cultural evaluation study for the mid-resource language of Danish, in which native speakers prompt..."
research_topic: "Social & Cultural Analysis"
---
# DaKultur: Evaluating the Cultural Awareness of Language Models for Danish with Native Speakers

## Authors

[[Max Mueller-Eberstein et al.]]

## Metadata

**Authors:** Max Mueller-Eberstein et al.

**Year:** 2025

**Type:** preprint

**Venue:** arXiv / C3NLP 2025

**Languages:** Danish

**Benchmark:** DaKultur

## Links

- **arXiv:** https://arxiv.org/abs/2504.02403

## Abstract

First cultural evaluation study for Danish with 1,038 interactions from 63 native speakers. Training on native-speaker data doubles response acceptance rates. Maximum acceptance of 42% highlights need for further research in aligning LLMs to Danish culture.

## Summary

This paper presents DaKultur, the first cultural evaluation dataset for Danish with 1,038 interactions from 63 demographically diverse native speakers who prompt different LLMs to solve tasks requiring cultural awareness. The study disentangles linguistic versus cultural proficiency in mid-resource language contexts, revealing that training on native-speaker data can more than double response acceptance rates from 14% to 42%. The maximum acceptance rate of 42% demonstrates that cultural adaptation remains an open challenge, highlighting how automatically translated data are insufficient for measuring cultural alignment.

## Data Description

DaKultur is the first cultural evaluation dataset for Danish with 1,038 interactions from 63 native speakers. Native speakers prompt different models to solve tasks requiring cultural awareness. Training on native-speaker data doubles response acceptance rates (14% to 42%), with maximum acceptance of 42% highlighting the need for further research in aligning LLMs to Danish culture.


## Detailed Summary

This paper presents DaKultur, the first cultural evaluation study and dataset for the mid-resource language of Danish, in which native speakers prompt different LLMs to solve tasks requiring cultural awareness. The study collected 1,038 interactions from 63 demographically diverse participants through an online interface, where participants composed culturally-relevant prompts and rated model responses as accept or reject. The study involved three different language models to assess the impact of various adaptation strategies on cultural alignment, and participants provided optional demographic information (region, age, gender) to assess intra-cultural diversity.

The analysis reveals critical findings: automatically translated data commonly used to train or evaluate cultural adaptation are insufficient for measuring or achieving cultural alignment with Danish. Training on native-speaker data can more than double response acceptance rates (from 14% to 42%), but even the best-performing model achieves only 42% acceptance, demonstrating that cultural adaptation remains a major open challenge. The study also examines how demographic factors (region, age, gender) affect model alignment across different cultural topics, providing insights into the heterogeneity of cultural expectations. The resulting validated dataset constitutes the first native Danish instruction dataset with culturally-specific instructions and human preference annotations.

## Paper Outline

1. Introduction - Cultural misalignment in LLMs and study motivation
2. DaKultur - Study design, data collection setup, and statistics
3. Experimental Setup - Models and adaptation strategies
4. Results - Acceptance rates, demographic analysis, and cultural topic analysis
5. Related Work - Cultural evaluation and adaptation approaches
6. Conclusion

## Methods Summary

An online interface was built where 63 Danish native speakers composed prompts requiring cultural awareness and rated model responses. Three different LLMs were used with varied adaptation strategies to generate answers (answer order shuffled). Participants provided optional demographic data (region, age, gender identity) to assess intra-cultural diversity. Manual validation ensured response relevance and correctness, and topic annotations were added by a distinct set of five Danish speakers. The study was conducted over two months, mainly advertised across higher educational institutions in Denmark, and was approved by the IT University of Copenhagen ethics committee.

## Results Summary

Training on native Danish data dramatically improves cultural acceptance rates from 14% to 42%, demonstrating the importance of language-specific data for cultural adaptation. However, the maximum 42% acceptance rate highlights that cultural alignment remains an unsolved problem. Automatically translated data prove insufficient for both training and evaluating cultural adaptation. Demographic analysis reveals that cultural expectations vary across regions, age groups, and gender identities in Denmark, suggesting that "Danish culture" is not monolithic. The study covers participants from all five regions of Denmark, balanced gender distribution, and most age ranges (20-60+), though with a slight skew toward the Capital Region.

## Conclusions

The study demonstrates that current approaches to cultural adaptation are inadequate for mid-resource languages like Danish, with even the best models failing to satisfy cultural expectations more than half the time. Limitations include the relatively small participant pool (63), the skew toward higher education contexts in recruitment, and the limited coverage of older age groups. Future work includes scaling to larger participant pools, investigating more sophisticated cultural adaptation strategies beyond data augmentation, and extending the methodology to other mid-resource languages.

## Artifact Contributions

- **DaKultur Dataset**: First native Danish cultural awareness dataset with 1,038 interactions and human preference annotations (https://mxij.me/x/dakultur)

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B7
**Relevance:** First Danish cultural awareness evaluation using native speakers, directly assessing cultural alignment of LLMs.

## Tags

