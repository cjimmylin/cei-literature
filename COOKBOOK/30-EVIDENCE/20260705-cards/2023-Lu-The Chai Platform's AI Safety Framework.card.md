---
stem: "2023-Lu-The Chai Platform's AI Safety Framework"
reader_model: "sonnet"
confidence: "medium"
is_benchmark: false
theme_tags: [ai-lab-practices, best-practices, normative-ethics]
task_format: "n/a"
scoring_type: "behavioral"
dataset_size: null
dataset_construction: "n/a"
languages: ["en"]
models_tested: ["GPT-J 6B"]
headline_numbers:
  - "~2 million user-chatbot conversations per day with average length of ~500 words (p.4)"
  - "Three major model/platform updates (June 2022, October 2022, March 2023) reduced NSFW word ratio (p.4)"
---
## 1. Gist
This short paper describes the AI safety framework developed by Chai Research for its conversational chatbot platform. Chai allows users to create and interact with custom chatbot personas. The paper articulates three safety pillars—content safeguarding, stability and robustness, and operational transparency and traceability—and describes how they are operationalized in the deployed system. The paper is relevant to values-alignment benchmarking as a case study of AI lab safety practices: it shows how a consumer-facing chatbot platform translates abstract alignment principles into production-level mechanisms, and introduces a simple proxy safety metric (NSFW word ratio) used to track safety over time.

## 2. Benchmark/eval design features
This is not a benchmark paper. The core contribution is a framework description and system paper:

- **Three safety pillars** (adapted from DeepMind, Meta, and OpenAI frameworks): (1) Content Safeguarding — automated moderation of generated content against categories from OpenAI's moderation API (hate speech, self-harm, sexual content, violence); (2) Stability and Robustness — continuous retraining on diverse user conversations, user feedback loop for reward model updates; (3) Operational Transparency and Traceability — full logging of all conversations, periodic quality/safety audits, early detection of unsafe behaviors.

- **Safety proxy metric**: NSFW word ratio per day. Defined as the fraction of all words in real user conversations classified as appearing in a NSFW dictionary. Formula: s̄ = (1/N) Σ 1(wn ∈ V), where V is the NSFW word dictionary and N is total words on a given day. Tracks improvement across platform updates.

- **Pre-deployment moderation pipeline**: New chatbot personas are stress-tested by running thousands of logged conversational histories through each persona, sampling outputs, and applying an automatic safety classifier. Personas failing the classifier are rejected.

- **Image moderation**: Uploaded avatar images are filtered through an image moderation classification system.

## 3. Task format & example item
n/a. No items or tasks presented. The paper describes a deployed system, not an evaluation benchmark.

## 4. Scoring / grading methodology
The paper reports a single proxy safety metric: NSFW word ratio per day. This is a behavioral measure on real user conversations. No benchmark-style evaluation protocol is described. Qualitative analysis of randomly sampled conversations is mentioned as a supplementary quality check.

## 5. Dataset construction & provenance
The base LLM is GPT-J 6B fine-tuned on novels and literature (HuggingFace: hakurei/lit-6B). The conversational data is proprietary user-chatbot interaction logs on the Chai platform. Platform launched May 5, 2022. No public dataset is released. The paper references ~2 million user-chatbot conversations per day.

## 6. Validity evidence
Validity evidence is limited. The NSFW word ratio is described as a proxy metric inspired by OpenAI's moderation tool, with no validation against human judgments of safety or broader measures of harm. Qualitative analysis of randomly sampled conversations is mentioned but not described in detail. No inter-rater reliability or construct validity analysis is reported.

## 7. Saturation / discrimination
Not applicable as this is a system/practice paper. The NSFW word ratio metric showed improvement following three major platform updates (June 2022, October 2022, March 2023), suggesting the metric is sensitive to system changes, but baseline and improved values are shown only in a figure (Figure 2) without numerical values in the text.

## 8. Multiturn / agentic aspects
The platform is inherently multiturn: users engage in extended conversations with chatbot personas over multiple turns. The safety mechanisms (pre-deployment stress testing with "thousands of logged conversational histories") are specifically designed to catch unsafe behaviors that emerge over conversation sequences rather than single turns. This is a notable design feature relevant to multiturn evaluation design.

## 9. Key numbers
- ~2 million user-chatbot conversations per day (p.4)
- Average conversation length ~500 words (p.4)
- Three major model/safety updates: June 2022, October 2022, March 2023 (p.4)
- Platform launched May 5, 2022 (p.4)
- Base model: GPT-J 6B (p.4)
- NSFW categories: hate speech, self-harm, sexual content, violence (p.4)

## 10. Pitfalls & limitations
- NSFW word ratio is a crude proxy: it cannot distinguish context (quoting hate speech vs. generating it), and is limited to surface-level lexical matching
- No external validation of the safety pipeline against human raters or standardized harm taxonomies
- No ablation studies showing which safety components contribute most to improvement
- Self-reported framework from the platform developer; no independent audit
- The paper is short (6 pages) and primarily promotional in nature
- The three pillars are adapted from other labs' frameworks without critical evaluation of their suitability for a consumer chatbot context
- No discussion of false positive rates in moderation (legitimate personas rejected)

## 11. Novel ideas worth stealing
1. **Pre-deployment stress testing via diverse conversational histories**: Before releasing a new model or persona, run it through a large corpus of prior user conversations (thousands of logs) and apply automated safety classifiers. This is a form of behavioral red-teaming at scale that could be formalized into a benchmark.
2. **Temporal safety tracking via proxy metrics**: The NSFW word ratio as a running daily metric enables longitudinal evaluation of model safety across deployments—a design worth adopting in values-alignment evaluation frameworks.
3. **Multiturn safety assessment by default**: The paper's practical experience suggests single-turn safety evaluation is insufficient; stress-testing via conversation histories is operationally necessary.
4. **User feedback loop for reward model calibration**: Integrating user ratings and correction suggestions to update the reward function provides a live human preference signal that could supplement static benchmarks.

## 12. Notable quotes
- "Despite the exciting prospects, the work recognizes the inherent challenges of a commitment to modern safety standards." (p.1)
- "Content safeguarding aims to encourage chat AI systems to generate responses (content) that are aligned with human values such that they do not cause any risk to users." (p.2)
- "By periodically reviewing the exchanges for quality and safety, we can better understand how the AI chatbot interacts with users, identify potential risks, and monitor the chat AI's compliance with our content guidelines and policies." (p.3)
- "We emphasise the significance of conscientious application of AI safety principles and robust safety measures." (p.1)

## 13. UNKNOWN / not in extract
- Numerical values for the NSFW word ratio before and after each update (Figure 2 is referenced but values not given in text)
- Details of the automatic safety classifier used in pre-deployment testing (architecture, training data, performance)
- Details of the image moderation classification system
- Size and composition of the NSFW word dictionary V
- Whether the reward model update frequency or scale is reported
- User demographic information or geographic distribution
- Any IRB/ethics approval for the study
