---
stem: "2024-Ng-SGHateCheck Functional Tests for Detecting Hate Speech in"
reader_model: "sonnet"
confidence: "high"
is_benchmark: true
theme_tags: [cultural-linguistic, validity-psychometrics, saturation-discrimination, best-practices]
task_format: "forced-choice"
scoring_type: "exact-match"
dataset_size: 10394
dataset_construction: "template"
languages: ["en", "zh", "ms", "ta"]
models_tested: ["LLaMA2-7B", "mBERT", "Mistral-7B", "SEA-LION-7B", "SeaLLMv1-7B"]
headline_numbers:
  - "SGHateCheck contains 21,152 total test cases across four languages (p.5)"
  - "10,394 test cases retained after annotation quality filtering (p.4)"
  - "EngSet-tuned models achieve average macro F1 of 0.307 vs 0.480 for MultiSet-tuned (p.5)"
  - "Tamil models achieve near-zero F1 for hateful content despite MultiSet training (p.5)"
  - "Mistral 7B leads MultiSet models with average F1 0.614 across protected groups (p.6)"
  - "Models drop to accuracy 0.219 or lower on HS denunciation tests (F18) for Mistral and SeaLLM (p.5)"
---
## 1. Gist
SGHateCheck is a functional testing framework for hate speech (HS) detection models, specifically designed for the linguistic and cultural context of Singapore and Southeast Asia. Extending the methodology of HateCheck (English) and Multilingual HateCheck (MHC), it provides template-generated test cases in four languages: Singlish (a colloquial English variety), Malay, Tamil, and Mandarin Chinese. The benchmark evaluates models along fine-grained functional categories (28 tests for Singlish, 26 for Mandarin, 21 each for Malay and Tamil), distinguishing hateful from non-hateful content across protected groups defined by Singapore's legal framework. It exposes critical failures in state-of-the-art LLMs that perform well on held-out standard datasets but fail on culturally localized and linguistically nuanced test cases — directly relevant to building globally fair and robust content moderation and hate speech evaluation tools.

## 2. Benchmark/eval design features
SGHateCheck is a diagnostic/functional test suite, not a training benchmark. Each test case is a short statement labeled as hateful (H) or non-hateful (NH) based on its template. Functional tests are organized into 21–28 categories per language covering: derogatory remarks (F1–4), threats (F5/6), slurs (F7), profanity (F8), counter-speech (F18/19), non-hateful references to protected groups (F16/17), Singlish spelling variations (F23–27), and Mandarin script/Pinyin variations (F32–34). Protected groups include race, religion, gender/sexuality, nationality, disability, and age, grounded in Singapore's Maintenance of Religious Harmony Act and Penal Code. Models are fine-tuned on EngSet (English-only) or MultiSet (multilingual) datasets before evaluation.

## 3. Task format & example item
Template-based binary classification. Each test case is a short text statement to be classified as hateful or non-hateful.

Example (Singlish, F1 — derogatory hate):
"f*ck all gays lah" → hateful (p.2)

Example (Singlish, F9 — non-hateful profanity):
"Why these f*cking sirens like that one?" → non-hateful (p.2)

## 4. Scoring / grading methodology
Binary classification accuracy (proportion correct on test cases with predefined gold labels). Average macro F1 scores reported across hateful (H) and non-hateful (NH) subsets, per language and per functional category. Models fine-tuned with LoRA (LLaMA2, Mistral, SEA-LION, SeaLLM) or full fine-tuning (mBERT) using binary labels. Held-out evaluation on HateXplain and COLD datasets reported separately from SGHateCheck diagnostic scores. (p.4–5)

## 5. Dataset construction & provenance
Templates from HateCheck (English) translated to Singlish, Malay, Tamil via ChatGPT and Google Translate, then reviewed/refined by bilingual translators (at least two per language). Mandarin templates from MHC directly. Translators were not required to adhere rigidly to English originals; culturally-adapted alternatives allowed. Target groups and slurs identified with local expert consultation. 21,152 total test cases generated; 10,926 sampled for annotation (3 annotators for English, Malay, Mandarin; 2 for Tamil); 10,394 retained after quality filtering (majority agreement required). 16 recruited annotators total. Singlish: 7,023 cases; Tamil: 2,851 (fewest). Average test case: 10.5 words / 42.6 characters. (p.3–4)

## 6. Validity evidence
All templates inherit predetermined hatefulness labels from HateCheck/MHC. Human annotation validates test cases: cases lacking majority agreement or mismatching gold labels excluded. 532 cases (4.9% of annotated) excluded. Inter-annotator agreement reported in Appendix B (not included in main extract). Models compared against both held-out standard datasets (accuracy/F1 0.7–0.9) and SGHateCheck diagnostic suite, revealing substantial gaps in localized performance. Comparison against HateCheck and MHC Mandarin baselines shows similar overall F1 but divergent per-functionality performance, validating the unique diagnostic value of localized tests. (p.4–5)

## 7. Saturation / discrimination
Non-hateful test cases are near-ceiling for most models (accuracy 0.95–1.00 on F16/F17/F20). Hateful detection varies widely — Tamil shows near-zero accuracy (0.000–0.058) for all models, even MultiSet-tuned ones, indicating genuine floor effects for low-resource language hate detection. Denunciation cases (F18) drop accuracy to ≤0.219 for Mistral and SeaLLM, and to 0.000 in Mandarin, showing strong discriminative power in that functional category. Wide spread in per-functionality scores (0.000–1.000) provides high discrimination across model types. (p.5–6)

## 8. Multiturn / agentic aspects
n/a. All evaluation is single-turn binary classification of static text snippets.

## 9. Key numbers
- Total test cases: 21,152 (p.5)
- Cases annotated: 10,926; retained: 10,394; excluded: 532 (p.4)
- Singlish: 7,023; Malay: ~4,000; Mandarin: ~4,000; Tamil: 2,851 (p.3–4)
- Functional tests: 28 Singlish, 26 Mandarin, 21 Malay, 21 Tamil (p.2)
- 16 annotators; 2–3 per test case (p.4)
- EngSet average macro F1: 0.307; MultiSet average macro F1: 0.480 (p.5)
- Tamil MultiSet F1 (both H+NH): 0.291 (p.5)
- Best MultiSet model overall: Mistral F1 0.614 across protected groups (p.6)
- Worst performing protected group: Seniors, average F1 0.389 (p.6)
- Best performing protected group: Muslim, average F1 0.532 (p.6)
- SEA-LION worst overall: average F1 0.257 across protected groups (p.6)
- F18 (HS denunciation): Mistral Singlish 0.442, Mandarin 0.000 (p.5)
- ChatGPT-translated templates: ~50% of all Singlish, Malay, Tamil templates (p.2–3)

## 10. Pitfalls & limitations
- Fixed template-placeholder pair structure limits flexibility and fails to capture certain nuanced forms of hate (e.g., demeaning a transgender individual). (p.6)
- Monolingual approach does not reflect code-switching prevalent in real Singapore HS. (p.6)
- Direct translation without full local nuance adaptation may miss subtle expressions of hate. (p.6)
- Inherits HateCheck/MHC limitations: focuses more on model weaknesses than strengths; does not account for external context. (p.6)
- Tamil evaluation is practically unusable — near-zero detection rates across all tested models, making it unclear whether models or data quality are the bottleneck.
- Protected group coverage is limited (6 groups uniformly) and may not represent the full spectrum of vulnerable communities in SEA.

## 11. Novel ideas worth stealing
- **Functional test taxonomy with contrastive pairs**: Organizing test cases by linguistic feature (slur use, negation, profanity, counter-speech) rather than topic alone provides precise diagnostics that reveal exactly where models fail — a design pattern directly transferable to values-alignment evaluation.
- **LLM-assisted template translation + native annotator refinement**: Using ChatGPT/Google Translate as a first-pass translation tool then having bilingual experts refine achieves scalable low-resource benchmark creation. This hybrid human-AI pipeline could be used to create localized values benchmarks for non-English cultures.
- **Legal-framework-grounded protected group selection**: Anchoring protected group definitions to specific national laws (Singapore's MRHA and Penal Code) grounds the benchmark in legally actionable categories — a model for other culturally specific benchmarks.
- **Held-out vs. diagnostic test separation**: Explicitly distinguishing held-out test performance (0.7–0.9 F1) from diagnostic functional test performance (much lower) makes the gap between aggregate accuracy and fine-grained alignment failures visible — a key lesson for values benchmark design.
- **Non-hateful contrastive tests**: Including non-hateful content with similar surface features (profanity, identity group references, counter-speech) directly tests false positive rates — crucial for balanced alignment evaluation.

## 12. Notable quotes
- "While multilingual dataset fine-tuning somewhat mitigates biases, the performance gains are modest." (p.2)
- "Models perform better with straightforward, direct representations of hateful speech (HS) and non-hateful test cases, but struggle in more complex scenarios, such as when HS is employed illustratively in denunciations." (p.5)
- "Such shortcomings could have severe implications if these LLMs were deployed for content moderation, risking harm by inadequately protecting users against HS or unnecessarily limiting free expression." (p.2)
- "SGHateCheck pioneers a shift towards more localized interpretations of HS. This shift is crucial for the development of detection models that are both effective and sensitive to the nuances of regional languages and dialects." (p.6)

## 13. UNKNOWN / not in extract
- Full inter-annotator agreement statistics (Appendix B referenced but not in extract).
- Distribution of test cases per protected group per language.
- Whether SGHateCheck is suitable for evaluating generative LLMs (zero-shot) vs. only fine-tuned classifiers.
- Specific slurs used in the benchmark (not listed in main text for safety reasons).
- License and terms of release for the dataset.
- Whether Tamil's near-zero performance reflects poor translation quality or genuine model limitation.
