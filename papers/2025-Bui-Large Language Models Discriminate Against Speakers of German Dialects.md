---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0473
type: preprint
short_title: "Large Language Models Discriminate Against Speakers of German Dialects"
year: 2025
first_author: "[[Minh Duc Bui]]"
last_author: "[[Katharina von der Wense]]"
authors: "Minh Duc Bui; Carolin Holtermann; Valentin Hofmann; Anne Lauscher; Katharina von der Wense"
url: "https://arxiv.org/abs/2509.13835"
external_pdf: "https://arxiv.org/pdf/2509.13835.pdf"
publication: "arXiv / EMNLP 2025"
CONF-CC: "EMNLP 2025"
pdf_extract: "PDF Extracts/2025/2025-Bui-Large Language Models Discriminate Against Speakers of German Dialects.md"
local_pdf: "[[Lit-WS-PDFs/2025/2025-Bui-Large Language Models Discriminate Against Speakers of German Dialects.pdf]]"
DATE_ADDED: 20260213
national_ethnic_cultural: German
cultures_nationalities_list: German
languages_list: German
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
newtags: 
LLM_assessed: "Aya, GPT-4o, Llama-3, Qwen-2"
DATA_URL: "https://github.com/UhhDS/German-Dialect-Bias"
tags: 
abstract: "Dialects represent a significant component of human culture and are found across all regions of the world. In Germany, more than 40% of the population speaks a regional dialect (Adler and Hansen, 2022). However, despite cultural importance, individuals speaking dialects often face negative societal stereotypes. We examine whether such stereotypes are mirrored by large language models (LLMs). We draw on the sociolinguistic literature on dialect perception to analyze traits commonly associated..."
CONFERENCE: "EMNLP 2025"
ethics_overall: 65
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
ethics_perspective: "Social & Cultural Values"
nw_confucian: 0
nw_ubuntu: 0
nw_islamic_ethics: 0
nw_buddhist: 0
nw_dharmic: 0
nw_indigenous_relational: 0
nw_buen_vivir: 0
author_country: DE
author_region: "Western Europe"
author_global_north_south: "Global North"
weird_score: 84
is_benchmark: No
is_eval: Yes
is_dataset: No
data_description: "Evaluation approach"
data_metrics: "Not specified"
---
# Large Language Models Discriminate Against Speakers of German Dialects

## Authors

[[Minh Duc Bui]], [[Carolin Holtermann]], [[Valentin Hofmann]], [[Anne Lauscher]], [[Katharina von der Wense]]

## Metadata

**Authors:** Minh Duc Bui, Carolin Holtermann, Valentin Hofmann, Anne Lauscher, Katharina von der Wense

**Year:** 2025

**Type:** preprint

**Venue:** arXiv / EMNLP 2025

**Languages:** German

## Links

- **arXiv:** https://arxiv.org/abs/2509.13835

## Abstract

Examines whether LLMs exhibit stereotypes against German dialect speakers. Evaluates 7 German dialects and finds all LLMs show significant dialect naming and usage bias against dialect speakers, reflected in negative adjective associations and biased decision-making.

## Summary

This paper investigates dialect bias in LLMs by examining seven German dialects (Low German, North Frisian, Saterfrisian, Ripuarian, Rhine Franconian, Alemannic, Bavarian) using association and decision tasks. The authors construct a novel evaluation corpus pairing dialect sentences with standard German counterparts and evaluate nine LLMs including Llama-3.1, GPT-4o, and Claude-3.5-Sonnet. Findings reveal that all models exhibit significant dialect naming and usage bias, associating dialect speakers with negative traits like 'uneducated' and making biased decisions in job assignment tasks, with explicit demographic labeling amplifying bias more than implicit dialect usage.

## Data Description

This paper constructs a novel evaluation corpus pairing sentences from seven regional German dialects (Low German, North Frisian, Saterfrisian, Ripuarian, Rhine Franconian, Alemannic, Bavarian) with their standard German counterparts. It evaluates dialect naming bias and dialect usage bias through association tasks and decision-making tasks, finding all LLMs exhibit significant bias against German dialect speakers.


## Detailed Summary

This paper investigates whether LLMs replicate societal stereotypes against German dialect speakers, drawing on sociolinguistic literature on dialect perception to analyze traits commonly associated with dialect speakers. The authors examine seven German dialects -- Low German, North Frisian, Saterfrisian, Ripuarian, Rhine Franconian, Alemannic, and Bavarian -- across two bias dimensions: dialect naming bias (explicitly labeling someone as a dialect speaker) and dialect usage bias (providing text written in dialect). Two experimental tasks are used: an association task measuring implicit adjective associations with dialect versus standard German speakers, and a decision task probing biased decision-making such as job assignments.

The analysis of nine open-source models of varying sizes and one proprietary model (including Llama-3.1-70B, Llama-3.1-8B, Mistral-7B, Gemma-7B, and GPT-4o-mini) reveals that all evaluated LLMs exhibit significant dialect naming and dialect usage bias. In the association task, models link negative traits (e.g., "uneducated," "unfriendly") to dialect speakers, even reversing the sociolinguistic finding that dialect speakers are viewed as friendly. In the decision task, models consistently assign dialect speakers to occupations requiring lower educational levels. Critically, the study finds that explicitly labeling linguistic demographics amplifies bias more than implicit cues like dialect usage, contradicting prior work showing minimal bias with explicit demographic mentions for other categories.

## Paper Outline

1. Introduction - Historical context of German dialect stereotypes and research questions
2. Related Work - Dialect perception in sociolinguistics and bias in NLP
3. Experimental Setup - Trait selection, dialect corpus construction, association and decision tasks
4. Results - Association task findings, decision task findings, dialect naming vs. usage bias comparison
5. Discussion - Implications for real-world deployment and comparison with prior bias research
6. Conclusion

## Methods Summary

The authors construct a novel evaluation corpus pairing sentences from seven German dialects with standard German counterparts. Two experimental paradigms are used: (1) an association task presenting LLMs with two writers (standard German vs. dialect) and asking them to assign adjectives describing stereotypical traits, and (2) a decision task requiring models to generate profiles and make job recommendations for standard German vs. dialect writers. Both tasks test dialect naming bias (explicit labels like "writes Alemannic dialect") and dialect usage bias (actual dialect text samples without labels). Nine open-source models (Llama-3.1-70B/8B, Llama-3-70B/8B, Mistral-7B, Gemma-7B, and others) and one proprietary model are evaluated.

## Results Summary

All evaluated LLMs exhibit significant dialect naming and dialect usage bias in both tasks. In the association task, Llama-3.1-70B significantly associates adjectives related to the "uneducated" trait with dialect speakers. Even the sole positive trait from sociolinguistic studies (friendliness) is reversed by LLMs, which associate dialect speakers with "unfriendly" instead. In the decision task, models show more consistent alignment with human dialect perceptions, systematically assigning dialect speakers to lower-status occupations. Explicitly labeling individuals as dialect speakers amplifies bias more than implicit dialect usage cues, contradicting findings from prior work on other demographic categories. This highlights the pressing need to address dialect bias in LLMs deployed in real-world applications.

## Conclusions

The study demonstrates that current LLMs display explicit discriminatory behavior toward German dialect speakers, with potential real-world consequences in applications such as hiring tools and educational platforms. Limitations include the focus on German dialects only, and the study does not explore mitigation strategies. Future work directions include extending the analysis to other languages with dialect variation, developing debiasing techniques for dialect bias, and investigating the impact of training data composition on dialect-related stereotypes.

## Artifact Contributions

No publicly released artifacts identified.

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B7
**Relevance:** Directly evaluates bias and discrimination in LLMs against German dialect speakers across 7 dialects.

## Tags

