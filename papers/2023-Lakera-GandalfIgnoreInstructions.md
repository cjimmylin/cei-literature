---








Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: D8RT6724
type: document
short_title: GandalfIgnoreInstructions
year: 2025
first_author: "[[Lakera AI]]"
last_author: "[[Lakera AI]]"
authors: "Lakera AI"
url: "https://www.lakera.ai/blog/who-is-gandalf"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: "English"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
tags: 
abstract: "This is a dataset of prompt injections from Gandalf by Lakera. Gandalf is a challenge to find a hidden password in increasingly difficult levels of a prompted LLM, demonstrating how adversarial prompt engineering can be used to manipulate AI models into revealing sensitive information. The dataset was collected from prompts submitted to Gandalf in July 2023, filtered using OpenAI text embeddings to find prompts similar to 'Ignore all previous instructions' with similarity of at least 0.825, with PII removed and near-duplicates deduplicated."
DATE_ADDED: 20260129
LLM_assessed: "NA"
DATA_URL: "NA"
pdf_extract: 
no_pdf_applicable: true
local_pdf: N/A
ethics_overall: "No"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
research_topic: "AI Safety & Alignment"
is_benchmark: "No"
is_eval: "No"
is_dataset: "Yes"
data_description: "Dataset"
data_metrics: "Not specified"
---
# GandalfIgnoreInstructions

## Metadata

**Authors:** Lakera

**Year:** 2023

**Type:** document

## Links

- **URL:** https://www.lakera.ai/blog/who-is-gandalf

## Abstract

This is a dataset of prompt injections from Gandalf by Lakera. Gandalf is a challenge to find a hidden password in increasingly difficult levels of a prompted LLM, demonstrating how adversarial prompt engineering can be used to manipulate AI models into revealing sensitive information. The dataset was collected from prompts submitted to Gandalf in July 2023, filtered using OpenAI text embeddings to find prompts similar to 'Ignore all previous instructions' with similarity of at least 0.825, with PII removed and near-duplicates deduplicated.

## Authors

[[Lakera AI]]

## Detailed Summary

Gandalf is an interactive security challenge created by Lakera AI that tests users ability to manipulate language models into revealing hidden information through creative prompting techniques. The challenge emerged from an internal hackathon and demonstrates real-world vulnerabilities in LLMs handling sensitive information across healthcare, finance, and insurance sectors.

The challenge spans seven difficulty levels with progressively sophisticated defenses, combining system prompts, input guards, and output guards. Within approximately 20 days of launch, Gandalf generated nearly 9 million interactions from over 200,000 unique users, processing over 50 prompts per second at peak usage. Only 8% of users advanced past level seven, demonstrating the effectiveness of multi-layered defense mechanisms while also revealing that even sophisticated protections can be circumvented through encoding, linguistic workarounds, and indirect questioning.

## Paper Outline

1. Overview - Introduction to Gandalf as an LLM security challenge
2. Impact - Usage statistics (9M interactions, 200K users)
3. Purpose and Origin - Development from internal hackathon for attack/defense research
4. Game Structure - Seven levels with progressive difficulty
5. Defense Mechanisms - Detailed breakdown of each levels protections
6. Key Insights - Lessons about LLM security and prompt injection vulnerabilities
7. Related Resources - Links to additional AI security learning materials

## Methods Summary

The challenge implements a layered defense architecture across seven levels: Level 1 has no defenses; Level 2 uses system instruction prohibition without technical safeguards; Level 3 adds output filtering blocking responses containing the password; Level 4 introduces a secondary LLM analyzing transcripts for encoded password disclosures; Level 5 adds input filtering blocking prompts mentioning password or secret; Level 6 employs an LLM to evaluate whether user input relates to the password topic; Level 7 combines defenses from levels 3, 4, and 6 for maximum protection.

## Results Summary

The challenge revealed that language models struggle to maintain confidentiality despite explicit instructions. Users successfully bypassed defenses through various techniques including encoding schemes, linguistic workarounds, and indirect questioning strategies. The 8% pass rate for level 7 demonstrates that while multi-layered approaches significantly improve security, they remain vulnerable to determined attackers. The system processed over 50 prompts per second at peak usage, demonstrating the scale of interest in LLM security challenges.

## Conclusions

The Gandalf challenge provides empirical evidence that simple instruction-based protections are insufficient for LLM security. Advanced defenses incorporating input/output filtering and LLM-based evaluation prove more effective but not impenetrable. The educational value lies in demonstrating real-world prompt injection vulnerabilities that could affect production systems handling sensitive data in healthcare, finance, and insurance domains.

## Artifact Contributions

- Interactive challenge platform: Gandalf (publicly accessible via Lakera)
- Implicit dataset: User interaction logs from 9 million prompts demonstrating attack patterns
- Educational framework: Seven-level progression demonstrating defense mechanisms

## Data Description

This blog post describes Gandalf, an interactive security challenge by Lakera that tests users' ability to manipulate language models into revealing hidden information through prompt injection. The challenge spans seven difficulty levels with progressively sophisticated defenses (system prompts, input guards, output guards). It generated nearly 9 million interactions from over 200,000 users. No specific LLMs are identified as being tested; the underlying model is not named.


## Notes

