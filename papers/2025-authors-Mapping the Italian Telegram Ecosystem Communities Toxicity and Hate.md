---


Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0514
type: preprint
short_title: "Mapping the Italian Telegram Ecosystem: Communities, Toxicity, and Hate Speech"
year: 2025
first_author: "[[Multiple authors]]"
last_author: "[[Multiple authors]]"
authors: Multiple authors
url: "https://arxiv.org/abs/2504.19594"
external_pdf: "https://arxiv.org/pdf/2504.19594.pdf"
publication: arXiv
local_pdf: "[[PDFs/2025/2025-authors-Mapping the Italian Telegram Ecosystem Communities Toxicity and Hate.pdf]]"
pdf_extract: "PDF Extracts/2025/2025-authors-Mapping the Italian Telegram Ecosystem Communities Toxicity and Hate.md"
DATE_ADDED: 20260213
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
national_ethnic_cultural: "Italian"
languages_list: "Italian"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
is_benchmark: "No"
is_eval: "No"
is_dataset: "Yes"
data_description: "Dataset for toxicity detection"
data_metrics: "Not specified"
LLM_assessed: "LLMs for content annotation"
DATA_URL: "NA"
tags: 
abstract: "Telegram has become a major space for political discourse and alternative media. However, its lack of moderation allows misinformation, extremism, and toxicity to spread. While prior research focused on these particular phenomena or topics, these have mostly been examined separately, and a broader understanding of the Telegram ecosystem is still missing. In this work, we fill this gap by conducting a large-scale analysis of the Italian Telegram sphere, leveraging a dataset of 186 million..."
ethics_perspective: "Toxicity & Hate Speech"
---
# Mapping the Italian Telegram Ecosystem: Communities, Toxicity, and Hate Speech

## Authors

[[Multiple authors]]

## Metadata

**Authors:** Multiple authors

**Year:** 2025

**Type:** preprint

**Venue:** arXiv

**Languages:** Italian

## Links

- **arXiv:** https://arxiv.org/abs/2504.19594

## Abstract

Large-scale analysis of Italian Telegram using 186 million messages from 13,151 chats collected in 2023. Examines toxicity and hate speech distribution using Perspective API and LLMs. Primary hate targets: Black people, Jews, gay individuals. Finds toxicity widely normalized across communities.

## Summary

This paper presents a comprehensive large-scale analysis of the Italian Telegram ecosystem using 186 million messages from 13,151 chats collected in 2023, examining communities, toxicity, and hate speech patterns. Employing Perspective API and LLMs for content annotation, the study identifies Black people, Jews, and gay individuals as primary hate targets and reveals that toxicity is widely normalized across different communities rather than confined to extremist groups. The analysis fills a research gap by examining misinformation, extremism, and toxicity holistically rather than as separate phenomena within Telegram's largely unmoderated environment.

## Data Description

Large-scale analysis of Italian Telegram using 186 million messages from 13,151 chats collected in 2023, examining toxicity and hate speech distribution using Perspective API and LLMs. Finds primary hate targets are Black people, Jews, and gay individuals, with toxicity widely normalized. Uses LLMs for analysis but does not evaluate specific models.


## Detailed Summary

This paper presents the first comprehensive large-scale mapping of the Italian Telegram ecosystem, analyzing 186 million messages from 13,151 chats collected throughout 2023. The study addresses a significant research gap, as prior work on Telegram examined misinformation, extremism, and toxicity separately and focused primarily on right-wing spaces. Starting from 21,470 seed chats (from Telegram Italia and TGStat), the authors verified language (Italian majority), applied snowball sampling via the forwarding mechanism, and built a directed weighted forwarding network. Using LLMs for thematic characterization and political orientation classification, combined with the Perspective API for toxicity detection, the study addresses three research questions: how political orientations vary across communities, whether toxicity is concentrated or distributed, and who the primary hate speech targets are. Results reveal strong thematic and ideological homophily, a hybrid ideological group where far-left and far-right rhetoric coexists on geopolitical issues, widespread normalization of toxicity within highly toxic communities (not confined to fringe groups), and hate speech primarily targeting Black people, Jews, and LGBTQ+ individuals. A distinctive finding is intra-national hostility where Italians attack other Italian groups along old historical regional divisions.

## Paper Outline

1. Introduction - Research gap in comprehensive Telegram ecosystem analysis
2. Related Work - Prior Telegram research on extremism, conspiracy, and toxicity
3. Data Collection - Seed collection, snowball sampling, forwarding network
4. Network Analysis - Community detection and ideological clustering
5. Toxicity Analysis - Perspective API evaluation and distribution patterns
6. Hate Speech Target Analysis - Identity targets and ideological alignment
7. Discussion - Context-specific moderation strategies
8. Conclusion

## Methods Summary

Data collection begins with 21,470 seed chats from Telegram Italia and TGStat, filtered to 4,360 valid Italian-language seeds. Snowball sampling via Telegram's forwarding mechanism expands the dataset. A directed weighted forwarding network enables community detection. LLMs classify individual chats by most discussed topics and political orientation. The Perspective API assesses message toxicity levels. Hate speech targets are identified and analyzed across different community types and ideological alignments. The methodology combines network analysis with NLP tools to provide both structural and content-level insights.

## Results Summary

Key findings include: (1) strong thematic and ideological homophily across communities; (2) identification of mixed ideological communities where far-left and far-right rhetoric coexist on geopolitical issues; (3) toxicity is widely normalized within highly toxic communities rather than isolated in extreme fringe groups; (4) hate speech primarily targets Black people, Jews, and LGBTQ+ individuals, independently of the community topic; (5) a common pattern of intra-national hostility where Italians attack other Italians, reflecting regional and historical divisions traceable to old cultural conflicts. Only 18% of Telegram Italia seeds proved valid, while TGStat had 63% validity.

## Conclusions

The study provides the first large-scale mapping of the Italian Telegram sphere, revealing that toxicity is a pervasive and normalized feature rather than an extremist niche phenomenon. The findings suggest the need for context-specific moderation strategies that account for cultural, ideological, and linguistic specificities of the Italian digital ecosystem, and pave the way for cross-linguistic comparisons of toxicity patterns on Telegram.

## Artifact Contributions

- **Dataset:** 186 million Italian Telegram messages from 13,151 chats (2023), the most extensive Italian-focused Telegram dataset to date
- **Analysis Framework:** Combined network analysis, LLM-based topic/ideology classification, and Perspective API toxicity assessment pipeline

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B8
**Relevance:** Major Italian hate speech and toxicity analysis dataset and study using LLMs for content moderation evaluation.

## Tags

