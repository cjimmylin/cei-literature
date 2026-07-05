---
stem: "2025-Seker-HATECAT-TR A Hate Speech Span Detection"
reader_model: "sonnet"
confidence: "high"
is_benchmark: true
theme_tags: [cultural-linguistic, validity-psychometrics, design-space, saturation-discrimination]
task_format: "free-text"
scoring_type: "classifier"
dataset_size: 2981
dataset_construction: "mixed"
languages: ["tr"]
models_tested: ["BERTurk", "TurkishBERTweet", "Llama-3.3-70B", "Llama-3.1-8B", "Gemma-2-9B", "GPT-4o"]
headline_numbers:
  - "2981 tweets and 4465 hateful spans across 8 minority target groups (p.3)"
  - "BERTurk best detection F1=0.59; categorization F1=0.31 (p.4)"
  - "Llama-3.3-70B few-shot detection F1=0.53; zero-shot F1=0.48 (p.4)"
  - "Inter-annotator detection F1=0.77; categorization F1=0.50 (p.3)"
  - "Symbolization category hardest for annotators: F1=0.29 (Appendix F)"
  - "Best category for models: Threat of Enmity (BERTurk F1=0.44) (p.4)"
---
## 1. Gist
HATECAT-TR is the first Turkish dataset for hate speech span detection and categorization at the span level, covering 2,981 tweets and 4,465 annotated hateful spans targeting eight minority groups (Armenian, Greek, Jewish, Arab, Immigrant/Refugee, LGBTI+, Alevi, Kurdish). Spans are classified into five discourse-type categories (Exclusive/Discriminatory Discourse; Exaggeration/Generalization/Attribution/Distortion; Threat of Enmity/War; Symbolization; Swearing/Insult/Dehumanization). The dataset was created via a semi-automated pipeline: GPT-4o generated initial span annotations, which were then reviewed and corrected by expert human annotators. Baseline models include fine-tuned Turkish BERT variants and zero/few-shot LLaMA. The paper is relevant to values-alignment benchmarking as a resource for Turkish-language hate speech evaluation and as a methodology case study for semi-automated, span-level, multi-category annotation of harmful discourse.

## 2. Benchmark/eval design features
- **Span-level annotation**: Unlike post-level classification, HATECAT-TR identifies the precise character-level spans within tweets responsible for hate speech, enabling fine-grained analysis.
- **Five discourse categories** drawn from the Hrant Dink Foundation's expert taxonomy: Exclusive/Discriminatory Discourse, Exaggeration/Generalization/Attribution/Distortion, Threat of Enmity/War/Attack/Murder/Harm, Symbolization, Swearing/Insult/Defamation/Dehumanization.
- **Eight minority target groups** spanning ethnic, religious, and identity communities.
- **BIO/IO tagging** for encoder models; natural language prompt format for decoder LLMs.
- **Semi-automated annotation**: GPT-4o (gpt-4o-2024-08-06) generates initial spans; two human annotators revise; IoU < 0.5 disagreements resolved by a third annotator.
- **Evaluation**: span-level F1 scores via SeqEval; evaluated on a test set of 300 randomly selected tweets from the agreed-annotation pool.

## 3. Task format & example item
Span annotation / token classification. Example from p.1:

Tweet (Turkish): "@username Bak Yunan tohumu, Feodalite denen bir şey vardı. Korkudan surların arkasına saklanmıştınız."
(English: "@username Look, Greek seed. There was something called feudalism. You hid behind the walls out of fear.")

Hateful spans identified: "Yunan tohumu" (Greek seed) → Symbolization; "Korkudan surların arkasına saklanmıştınız" (You hid behind the walls out of fear) → Threat of Enmity/War.

GPT-4o annotation prompt format (Appendix B, p.8): System message instructs model to identify hate speech spans targeting a given group and classify them into the five categories; returns JSON with text_span and hate_speech_category.

## 4. Scoring / grading methodology
Span-level precision, recall, and F1 computed via SeqEval library. For detection: BIO tagging (O / B-HATE / I-HATE). For categorization: IO tagging (O / I-{Category}). Test set: 300 tweets selected from the first-round agreed annotations. 5-fold cross-validation used for training; mean ± standard deviation reported. Inter-annotator agreement: character-level Cohen's Kappa (excluding negatives biases assessment) and character-level micro-averaged F1 excluding negative labels. Relaxed Kappa computed at IoU thresholds (0.50, 0.90).

## 5. Dataset construction & provenance
- Source tweets collected 2022–2024 by the Hrant Dink Foundation (HDF), focusing on current events and specific hashtags targeting the eight minority groups; includes tweets from the Israel-Palestine conflict period and Turkish election period.
- Previously used in HSD-2Lang shared task (Uludoğan et al., 2024).
- GPT-4o annotation: 2,981 tweets processed; 1,530 accepted without modification, 1,451 revised by human annotators (span boundaries, category labels, or hallucination removal).
- Edit-distance correction: GPT-4o spans differing by <4 characters from original tweet text were snapped to closest match.
- Six annotators: two from linguistics, three from cultural studies, one from political science; all HDF-trained.
- Dataset available by contacting authors (complying with X/Twitter terms); code: github.com/boun-tabi/hatecat-tr.

## 6. Validity evidence
- Inter-annotator detection F1=0.77; overall categorization F1=0.50 (Table 5, Appendix F); moderate Kappa=0.57 (p.3).
- Category-specific IAA: Threat of Enmity highest (F1=0.66); Symbolization lowest (F1=0.29).
- Relaxed Kappa (IoU≥0.50): 0.76 — annotators often agree on approximate span region even when exact boundaries differ (p.3).
- Annotators had prior HDF training on hate speech identification; domain expertise validated by project membership.

## 7. Saturation / discrimination
- Best model (BERTurk) achieves F1=0.59 on detection and F1=0.31 on categorization — well below human annotator agreement (0.77 / 0.50), leaving substantial headroom.
- Strong discrimination by category: Threat of Enmity scores 0.44 (BERTurk) vs. Exclusive/Discriminatory Discourse 0.08 — 5× difference showing genuine discrimination challenge.
- LLMs (LLaMA-3.3-70B few-shot: F1=0.53 detection, F1=0.22 categorization) underperform Turkish-specific models, showing that language-specific pretraining matters.
- Symbolization category: LLaMA-3.3-70B scores F1=0.00 in both zero- and few-shot settings — complete failure on implicit hate.

## 8. Multiturn / agentic aspects
n/a — single-turn annotation task.

## 9. Key numbers
- 2,981 tweets; 4,465 hateful spans (p.3)
- Average span length: 30.30 characters (SD=21.69) (p.3)
- Average spans per tweet: 1.50 (p.3)
- 1,530 tweets accepted without modification; 1,451 revised (p.3)
- Test set: 300 tweets (Appendix G)
- IAA overall detection F1=0.77; categorization F1=0.50 (Appendix F)
- IAA Symbolization F1=0.29; Threat F1=0.66 (Appendix F)
- BERTurk detection: F1=0.59; categorization F1=0.31 (p.4)
- LLaMA-3.3-70B few-shot detection F1=0.53; zero-shot F1=0.48 (p.4)
- Gemma-2-9B detection F1=0.46 (p.4); unable to report categorization due to hallucinated outputs
- Target groups: Jewish 925, Greek 1015, Armenian 534, Arab 301, Alevi 108, Kurdish 52, LGBTI+ 46 tweets (Table 4, Appendix E)

## 10. Pitfalls & limitations
- Annotator subjectivity, especially for implicit and context-dependent hate speech; IAA for categorization is only 0.50 (p.5).
- Limited to Twitter/X; may not generalize to other platforms or registers.
- Some categories underrepresented (LGBTI+: 46 tweets, Kurdish: 52) — insufficient data for robust category-level evaluation.
- Symbolization category: relies on culturally specific negative stereotypes; hardest for both models and annotators.
- Turkish agglutinative morphology creates tokenization-span alignment issues for multilingual models (p.5).
- GPT-4o hallucination problem: hallucinated spans required edit-distance correction; pipeline error rate not fully quantified.
- Gemma categorization failure — model consistently produced unparsable outputs for categorization (Appendix G).

## 11. Novel ideas worth stealing
1. **Semi-automated annotation pipeline**: Using an LLM (GPT-4o) for initial span annotation + human expert review is more efficient than pure annotation from scratch while maintaining quality — the 51% acceptance-without-modification rate shows the approach is not rubber-stamping but genuinely complementary.
2. **Span-level discourse typology**: The five discourse categories (discriminatory, exaggeration, threat, symbolization, dehumanization) provide a reusable taxonomic vocabulary for fine-grained harmful content classification that goes beyond binary hate/non-hate. This taxonomy could be adapted for values-alignment scenarios involving harmful discourse toward AI-adjacent groups.
3. **Relaxed inter-annotator agreement via IoU threshold**: Using IoU-based relaxed Kappa for span tasks (Kappa 0.57 → 0.76 at IoU≥0.50) gives a more realistic picture of annotation quality when exact boundary consensus is unrealistic — useful for any span-annotation benchmark design.
4. **Target group as conditioning variable**: Pre-assigning a single target group per tweet during annotation simplifies the task and enables stratified analysis of model performance across groups — a scalable approach for benchmarks covering multiple protected attributes.

## 12. Notable quotes
- "Identifying and categorizing these spans allows moderators to distinguish the nature of hate speech, prioritize severe cases, ensure consistency in content moderation, and improve overall transparency in enforcing platform guidelines." (p.1)
- "All models scored lower on the categorization task, indicating that this task is more difficult." (p.4)
- "These results indicate that more implicit and context-dependent hate speech categories are difficult to detect and categorize." (p.4)
- "Turkish's agglutinative morphology presents specific challenges for span-level detection. Words often contain multiple morphemes, and subword tokenization may not align well with morpheme boundaries." (p.5)

## 13. UNKNOWN / not in extract
- The specific tweets in the dataset (privacy-protected; access via HDF contact).
- Full confusion matrix details beyond Figure 1 description.
- Exact GPT-4o system message (listed as Appendix B, Listing 1 — included in extract at p.8).
- Compensation details for annotators (described as "aligned with HDF's standard policies").
- Whether the dataset covers hate speech collected after 2024.
- Breakdown of inter-annotator agreement by target group.
