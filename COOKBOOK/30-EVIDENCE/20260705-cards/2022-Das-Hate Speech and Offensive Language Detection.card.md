---
stem: "2022-Das-Hate Speech and Offensive Language Detection"
reader_model: "sonnet"
confidence: "high"
is_benchmark: true
theme_tags: [cultural-linguistic, validity-psychometrics, best-practices]
task_format: "classifier"
scoring_type: "classifier"
dataset_size: 10178
dataset_construction: "scraped"
languages: ["bn", "bn-en"]
models_tested: ["m-BERT", "XLM-RoBERTa", "IndicBERT", "MuRIL"]
headline_numbers:
  - "Dataset: 10,178 tweets (5,071 actual Bengali + 5,107 Roman Bengali), 3 classes: hate/offensive/normal (p.4)"
  - "XLM-RoBERTa achieves Macro-F1=0.803 on actual Bengali (ELFI setting) (p.6)"
  - "MuRIL best for joint training: actual Bengali Macro-F1=0.808 (p.6)"
  - "Zero-shot transfer actual→Roman: best Macro-F1=0.390 (m-BERT) (p.7)"
  - "Krippendorff alpha: 0.696 (p.4)"
---
## 1. Gist
Das et al. introduce a 10K Bengali hate speech dataset covering both actual Bengali (Unicode script) and Romanized Bengali (Latin script) — a code-mixed form prevalent on social media. Each tweet is annotated with a ternary label (hate/offensive/normal) and a target community label (gender, linguistic community, national origin, religion, miscellaneous). The paper systematically evaluates four multilingual transformer models across five interlingual transfer settings (monolingual, joint training, zero-shot/few-shot transfer, language translation transfer). For values-alignment benchmarking, this paper demonstrates the significant challenges of hate speech evaluation in low-resource, code-mixed languages, and shows that cross-script transfer of moral judgement classifiers degrades severely in zero-shot settings even for semantically similar content.

## 2. Benchmark/eval design features
Three-class classification (hate speech / offensive / normal) with optional target community annotation:
- **Hate speech**: Language targeting individuals/groups based on protected attributes (race, religion, ethnicity, sexual orientation, disability, caste, geographic location, gender).
- **Offensive**: Profanity, rude/vulgar language targeting individuals/groups — not necessarily hate speech.
- **Normal**: Everything else.
- **Target groups** (Table 3, p.3): Gender (Men/Women/Trans), Linguistic Community (Bengali/Bihari), National Origin (Indian/Bangladeshi/Pakistani), Religion (Hindu/Islam), Miscellaneous (Individual/Political/Disabled/Dalit/Others).

Five interlingual transfer settings evaluated: ELFI (monolingual), Joint training, Model transfer (zero-shot and few-shot), Language transfer (translated to English), Joint training with language transfer.

## 3. Task format & example item
Given a tweet in actual or Roman Bengali, predict hate/offensive/normal. Example annotations (Table 2, p.4):

Actual Bengali, translated: "Do you understand today that this race is barbaric, stupid, mean, fanatical? But the British understood more than 300 years ago! The word 'civilized' should not be associated with the Bengali those who have been enslaved all their lives" → Hate (target: Bengali community)

Roman Bengali: "@user I fuck you in dream, daughter of a bitch, this is why I get nightmare" → Offensive (target: Individual, Woman)

## 4. Scoring / grading methodology
Accuracy, Macro-F1, class-specific F1 for Hate (H) and Offensive (O), and AUROC score (p.6). 70:10:20 train/validation/test stratified split. For zero/few-shot settings: Macro-F1 only. Results averaged over 3 random sets for few-shot experiments (p.6).

## 5. Dataset construction & provenance
Twitter data collected using a lexicon of 74 abusive terms in Bengali (both actual and Romanized). 500K actual Bengali tweets and 150K Roman Bengali tweets initially retrieved. Filtered: max 75 tweets/user, max 500 tweets/month to avoid event bias. Final annotation: 5,071 actual + 5,107 Roman Bengali tweets.

Annotation: 4 undergraduate CS native Bengali speaker annotators + 2 expert PhD student annotators. Pilot annotation (30 tweets from gold-label set per annotator), then main annotation via Doccano platform. Two-annotator annotation per tweet; expert tie-breaking for mismatches; triplet disagreements excluded. Mental health precautions: periodic breaks, weekly meetings (p.4). Inter-annotator agreement: Krippendorff α=0.696 (p.4).

## 6. Validity evidence
Krippendorff α=0.696 — the paper notes this is "better than the agreement score on other related hate speech tasks (Ousidhoum et al., 2019; Guest et al., 2021)" (p.4). Comparison with existing Bengali dataset (Romim et al., 2021) shows cross-dataset generalization: XLM-RoBERTa trained on this dataset achieves Macro-F1=0.754 on their test set; their model achieves 0.646 on this dataset (p.7, Table 9) — suggesting this dataset is harder/more discriminating.

Error analysis (p.8-9, Table 10) identifies 5 failure types: sarcasm with emojis, sequences of obscene words (no individual target), political/religious viewpoints, code-mixed linguistic structure, tentatively wrong ground truths. These categories reveal where model and human judgment diverge.

## 7. Saturation / discrimination
Best monolingual performance: Macro-F1 0.803 (actual Bengali XLM-RoBERTa), 0.805 (Roman Bengali XLM-RoBERTa). Joint training improves to 0.808. Zero-shot cross-script transfer drops to 0.390 (actual→Roman) — a severe 50% relative drop, showing the benchmark is not close to saturation and has strong discrimination between near-human and sub-human systems.

## 8. Multiturn / agentic aspects
n/a — single tweet classification. No thread context used.

## 9. Key numbers
- Dataset: 10,178 tweets (5,071 actual + 5,107 Roman Bengali) (p.4)
- Lexicon: 74 abusive terms (p.3)
- Hate class: 825 actual + 510 Roman = 1,335 total (p.3)
- Offensive: 1,341 actual + 2,063 Roman = 3,404 total (p.3)
- Normal: 2,905 actual + 2,534 Roman = 5,439 total (p.3)
- Krippendorff alpha: 0.696 (p.4)
- Best monolingual Macro-F1: 0.803 actual Bengali (XLM-R), 0.805 Roman Bengali (XLM-R) (p.6)
- Joint training best: MuRIL 0.808 actual, XLM-R 0.810 Roman (p.6)
- Zero-shot transfer best: 0.390 (m-BERT, actual→Roman) (p.7)
- Few-shot MTx128 best: MuRIL 0.751 (actual→Roman) (p.7)
- Language transfer (translated to English) best: XLM-R 0.764 — lower than monolingual 0.803 (p.7)

## 10. Pitfalls & limitations
- No external context (user profile, posting history, gender) — limits detection of contextual hate speech (p.9)
- Not tested against adversarial examples (p.9)
- 74-keyword lexicon may bias toward explicit hate speech, underrepresenting implicit forms
- Annotators are undergraduate CS students, not cultural/linguistic hate speech experts
- Target community annotation is secondary and not systematically evaluated
- Code-mixed linguistic structure causes systematic mis-classification (p.9)
- Dataset from single platform (Twitter); Facebook and WhatsApp are dominant in Bengali-speaking regions

## 11. Novel ideas worth stealing
1. **Parallel actual + Romanized script dataset construction**: Creating matched datasets in both Unicode and Latin-script versions of the same language enables systematic measurement of orthographic transfer — highly relevant for low-resource language benchmarks where code-mixing is prevalent.
2. **5-way interlingual transfer evaluation design**: ELFI (monolingual), joint training, zero-shot transfer, few-shot transfer (32/64/128 shots), and language translation transfer — a comprehensive transfer evaluation framework directly reusable for multilingual values benchmarks.
3. **Target community annotation with data statement**: Including who is targeted (gender, national origin, religion) alongside harm type, plus a full data statement (p.11) documenting annotator demographics and data collection — raises the standard for benchmark transparency.
4. **Annotator mental health protocols**: Documenting that annotators had weekly meetings and were advised to take breaks when annotating harmful content — an ethics-of-research design feature worth standardizing.

## 12. Notable quotes
- "XLM-Roberta performs best while trained with standalone data, it performs very poorly for unseen data with similar semantic content but a different orthography." (p.8-9)
- "MuRIL shows an increase in performance at a rate higher than the other models [in few-shot settings]. Observing these results it may be safe to say that when there is a data scarcity for a particular language, it is better to reuse existing fine-tuned models in the same domain." (p.9)
- "Hate speech is complex in nature, sometimes annotators make mistake while labelling them due to differing viewpoints." (p.9)
- "With more than 210 million speakers, Bengali is the seventh most widely spoken language, with around 100 million Bengali speakers in Bangladesh and 85 million in India." (p.2)

## 13. UNKNOWN / not in extract
- Breakdown of target community annotation performance
- Whether the dataset is balanced across target groups
- Distribution of hate speech by religion (Hindu vs. Islam) in the dataset
- Any cross-platform comparison (Twitter vs. Facebook/WhatsApp)
- Detailed annotation guidelines/codebook content
- Whether expert annotator vs. student annotator agreement was measured separately
