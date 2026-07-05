---
stem: "2024-Wijanarko-Monitoring Hate Speech in Indonesia An NLP-based Classification of"
reader_model: "sonnet"
confidence: "high"
is_benchmark: true
theme_tags: [cultural-linguistic, llm-judges-scoring, best-practices, design-space]
task_format: "classifier"
scoring_type: "classifier"
dataset_size: 27228
dataset_construction: "crowdsourced"
languages: ["id"]
models_tested: ["IndoBERTweet", "gpt-3.5-turbo", "SeaLLM-7B-v2.5"]
headline_numbers:
  - "IndoBERTweet fine-tuned on IndoToxic2024 achieves macro-F1 0.78 for hate speech detection (p.4)"
  - "gpt-3.5-turbo zero-shot achieves macro-F1 0.627 vs IndoBERTweet's 0.718 overall (p.3)"
  - "gpt-3.5-turbo few-shot drops to macro-F1 0.429, worse than zero-shot (p.4)"
  - "Hate speech ratio spiked from 7.78% to 20.21% after October 2023 Israel-Hamas war (p.5)"
  - "Dashboard processed over 1.45 million online texts from Sep 2023 to Mar 2024 (p.4)"
---
## 1. Gist
This paper presents an NLP-based hate speech monitoring system for Indonesian social media, developed to track hate speech against seven vulnerable minority groups during the 2024 Indonesian presidential election. The core contribution is the IndoToxic2024 dataset — annotated by members of the targeted minority groups via focus group discussions — and a fine-tuned IndoBERTweet classifier deployed in a live Power BI dashboard. The work demonstrates that minority-community involvement in keyword discovery and annotation yields a smaller but higher-performing classifier than LLM zero-shot or few-shot approaches. The paper is directly relevant to values-alignment benchmarking because it operationalizes culturally embedded toxicity categories, shows that community participation substantially improves annotation quality, and reveals that English-centric LLMs fail on Indonesian hate speech even in few-shot settings.

## 2. Benchmark/eval design features
The evaluation benchmark is the IndoToxic2024 dataset, which covers five toxic text types: profanity/obscenity, insult, incitement to violence, identity attack, and sexual explicit content. Target groups are Shia, Ahmadiyyah, Christians, LGBTQ+ individuals, Chinese Indonesians (Tionghoa), people with disabilities, and Jews. The classification task is multi-label (a single text can bear multiple toxicity type labels). Annotation was performed by 19 annotators from diverse backgrounds, including members of the six minority groups; conflicting annotations are preserved to reflect real-world subjectivity. The evaluation metric is macro-F1, enabling comparison across imbalanced classes.

## 3. Task format & example item
The classification task asks models to determine whether a text targeting a vulnerable group constitutes hate speech (binary), then assigns one or more toxicity type labels. An example of group-specific slang used as keywords: "lesbong" (derogatory for lesbian), "cokin" (slur for Chinese Indonesian), "setanyahu" (portmanteau insult for Netanyahu/Satan) (p.1). No verbatim annotation example item is reproduced in the extract; item examples appear as keywords in Appendix A rather than full annotated instances.

## 4. Scoring / grading methodology
Models are evaluated via stratified 10-fold cross-validation for IndoBERTweet (preventing data leakage) and zero-shot or 15-shot few-shot prompting for LLMs. The primary metric is macro-F1 across all classes, supplemented by accuracy. For the classification subtasks displayed in the dashboard (e.g., "Related to Election", "Identity Attack"), each subtask has its own IndoBERTweet model evaluated separately (Table 3, p.4).

## 5. Dataset construction & provenance
Keywords were elicited through focus group discussions with Indonesian minority group representatives, yielding group-specific slang and derogatory terms (Appendix A). Using these keywords, 1.45 million posts were scraped from X (23% sampling rate), Facebook, Instagram, and Cekfakta news articles between September 2023 and March 2024. From this pool, texts were randomly sampled, then annotated by 19 annotators. For model training, the dataset was down-sampled to 6,807 positive (hate speech) and 20,421 negative examples (3:1 ratio), totaling 27,228 samples. The dataset is released as IndoToxic2024 under CC BY-SA 4.0.

## 6. Validity evidence
Annotation was performed by community members of targeted groups, providing face validity for cultural relevance. Inter-annotator agreement details are not fully reported in the extract, but the paper explicitly notes that conflicting annotations are retained to reflect "real-life complexity of hate speech messages in social media" (p.3). The achieved macro-F1 of 0.78 for hate speech detection substantially outperforms all LLM baselines (gpt-3.5 zero-shot: 0.63, SeaLLM: 0.52). External validity is supported by real-world deployment: the dashboard was used by BAWASLU (Indonesian election oversight body) and covered by 32 national media outlets.

## 7. Saturation / discrimination
The fine-tuned model achieves 0.78 macro-F1 for hate speech, but individual subtask performance varies considerably: incitement to violence reaches only 0.53 macro-F1 versus 0.85 for insult (p.4, Table 3). This indicates meaningful discrimination difficulty for subtle or legally ambiguous categories like "incitement to violence." The dataset is imbalanced (3:1 negative-to-positive ratio), and keyword-based filtering means the model was only tested on pre-filtered texts — generalization to general social media is untested (p.8).

## 8. Multiturn / agentic aspects
n/a — classification pipeline is single-turn inference. The dashboard architecture involves periodic scraping, batch inference, and Power BI visualization but no interactive multi-turn model engagement.

## 9. Key numbers
- Overall macro-F1: IndoBERTweet 0.718, gpt-3.5 zero-shot 0.627, SeaLLM-7B 0.517, gpt-3.5 few-shot 0.429 (p.3, Table 2)
- Hate speech detection subtask: accuracy 0.89, macro-F1 0.78 (p.4, Table 3)
- Identity attack subtask: macro-F1 0.80 (p.4)
- Incitement to violence subtask: macro-F1 0.53 (p.4)
- Total dataset scraped: 1.45 million texts (p.3)
- Training set size: 27,228 (6,807 positive + 20,421 negative) (p.3)
- Hate speech spike: 7.78% → 20.21% after October 7, 2023 (p.5)
- Dashboard page views peaked at 15,545 on February 13, 2024 (day before election) (p.8)
- Jews constituted two-thirds of all hate speech targets in November 2023 (p.5)

## 10. Pitfalls & limitations
- Model only tested on keyword-filtered texts, not general social media; performance on out-of-distribution text unknown (p.8)
- Dashboard launched Feb 2024 — may not reflect improvements in GPT-4o mini and newer LLMs (p.8)
- Limited to Indonesian; code-switching (regional dialects) not fully handled (p.8)
- 23% sampling rate on X means substantial data loss (p.3)
- Few-shot prompting severely degraded gpt-3.5 performance (0.627 → 0.429), possibly due to prompt complexity on non-English tasks — raises questions about prompt design validity (p.4)
- Conflicting annotations are retained without adjudication, which can lower model training signal quality

## 11. Novel ideas worth stealing
- **Community-in-the-loop keyword elicitation**: Using focus group discussions with targeted minority communities to derive domain-specific vocabulary before any annotation begins substantially improves data quality and ensures culturally embedded harm categories are captured — directly transferable to values-alignment benchmarks targeting non-WEIRD populations.
- **Multi-label toxicity taxonomy rooted in local legal definitions**: Defining toxic categories using Indonesia's National Human Rights Commission definition grounds annotation in local legal norms rather than imported US-centric frameworks — a model for culturally appropriate values benchmarks.
- **Annotator demographics matching targets**: Having annotators who are members of targeted groups (not just professional annotators) captures harm that outsiders miss — especially relevant for benchmarks on religious discrimination, racial microaggressions, or disability-related language.
- **Engagement metrics as external validity evidence**: Tracking dashboard page views and institutional partnerships (BAWASLU adoption) provides real-world impact evidence beyond F1 scores — a novel validity signal for applied benchmarks.

## 12. Notable quotes
- "Online hate speech propagation is a complex issue, deeply influenced by both the perpetrator and the target's cultural, historical, and societal contexts." (p.1)
- "This dataset therefore imitates the real-life complexity of hate speech messages in social media." (p.3)
- "Despite our constant sampling rate during data collection, the number of posts mentioning targeted vulnerable groups in Indonesia has increased in recent months." (p.5)
- "Correctly fighting hate speech is hard. Effective measures like stringent content filtering or social media bans should be reserved for extreme cases." (p.6)

## 13. UNKNOWN / not in extract
- Full inter-annotator agreement statistics (Cohen's kappa or similar) for IndoToxic2024 annotations
- Detailed demographic breakdown of the 19 annotators
- Whether the 27,228 training samples were used with standard train/validation/test splits or purely 10-fold CV
- License terms for IndoBERTweet base model
- Whether evaluation of Rohingya-related hate speech was included post-December 2023 addition
