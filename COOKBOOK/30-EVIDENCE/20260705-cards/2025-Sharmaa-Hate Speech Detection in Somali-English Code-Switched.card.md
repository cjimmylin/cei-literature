---
stem: "2025-Sharmaa-Hate Speech Detection in Somali-English Code-Switched"
reader_model: "opus"
confidence: "medium"
is_benchmark: false
theme_tags: [cultural-linguistic, design-space]
task_format: "n/a"
scoring_type: "classifier"
dataset_size: null
dataset_construction: "scraped"
languages: [Hindi, English, Hinglish]
models_tested: [Multilingual-BERT, MuRIL, Naive-Bayes, Logistic-Regression, SVM, Random-Forest, XGBoost, AdaBoost, Gradient-Boosting]
headline_numbers: ["MoH knowledge base = 72,635 Roman-to-Devanagari transliteration pairs (p.22)", "MoH+MuRIL F1 0.71/0.90/0.85 on TRAC-I/HOT/HS (p.32)", "MoH mapping gives ~13% avg F1 gain with classical ML; ~15% over raw M-BERT baseline; ~4-6% over SOTA baselines (p.2, p.7)", "Levenshtein similarity threshold 0.7 captured 91% of OOV words (p.26)"]
---
## 1. Gist
NOTE: despite the vault stem saying "Somali-English," the actual paper is titled "Ceasing hate with MoH: Hate Speech Detection in Hindi-English Code-Switched Language" (p.1) — it is about Hindi-English (Hinglish), not Somali. This is a *methods* paper (not a benchmark): it proposes MoH ("Map Only Hindi"), a word-level transliteration pipeline that identifies language tags and converts Roman-Hindi tokens into Devanagari before fine-tuning M-BERT and MuRIL for hate-speech classification. It matters for values-alignment mainly as prior art on low-resource, code-switched, transliteration-robust classification — a linguistic-preprocessing move relevant to building non-English hate/values evaluators.

## 2. Benchmark/eval design features
Not a benchmark; it consumes three existing Hindi-English datasets (TRAC-I, HOT, HS) and proposes a preprocessing + classification pipeline. Core claims/contributions (p.6-7): (1) first HS-detection work preserving semantic + syntactic structure of code-switched text via partial transliteration; (2) first to fine-tune MuRIL for hate speech; (3) MoH text conversion boosts F1 ~15% over raw M-BERT baseline; (4) avg 4% F1 gain over best baselines across 3 datasets. Pipeline steps: descriptive analysis → language identification/disambiguation (Enchant + n-gram frequency) → OOV recovery via Levenshtein → Devanagari conversion → BERT-family classification (p.18-29).

## 3. Task format & example item
n/a (supervised classification, not an item-format eval). Illustrative data (Table 2, p.9): post "saari ladkiyan pagal hoti hai. Bilkul useless." → "All girls are mad. Completely useless." (profane=Yes, hate=Yes); "Bangaldeshi apne desh vapas jaa." → "Bangladeshi, go back to your country." (profane=No, hate=Yes).

## 4. Scoring / grading methodology
Classifier metrics — Precision, Recall, F1 (p.2). Binary cross-entropy for 2-class, categorical cross-entropy for multi-class datasets (p.30). No human rating or LLM judge.

## 5. Dataset construction & provenance
Three scraped social-media datasets (p.15-16): TRAC-I (12,000 Facebook posts → 11,623 after cleaning; Overtly/Covertly Aggressive/Non-Aggressive), HS (4,575 tweets; hate vs normal), HOT (3,679 → 2,803 tweets; Non-Offensive/Abusive/Hate-Inducing). MoH knowledge base built from FIRE transliteration pairs (30,823), XLIT-Crowd IIT-Bombay (14,919, AMT-crowdsourced), plus Hindi profane word list → 72,635 pairs after pruning (p.21-22). Preprocessing: lowercase, remove URLs/user IDs/emoticons, normalize repeated chars (p.16-18). No contamination controls discussed.

## 6. Validity evidence
Threshold-selection validity: manual inspection of 20% random sample showed Levenshtein 0.7 correctly mapped 91% of words vs 76%/68% at 0.6/0.8 (p.26). Comparative experiments across 3 datasets, 7 classical ML models x 4 feature types (Tables 6-7), plus baseline comparisons and Indic-Trans ablation. Error analysis section promised. No inter-rater reliability (labels inherited from source datasets).

## 7. Saturation / discrimination
MoH+MuRIL clearly separates from classical ML (F1 up to 0.90 on HOT vs ~0.6-0.75 for best classical) (p.32). MoH mapping gives only slight gains for classical ML (Table 7 vs 6) but large gains for BERT-family. Headroom remains on TRAC-I (best F1 0.71) — the 3-class aggression task is hardest.

## 8. Multiturn / agentic aspects
n/a.

## 9. Key numbers
- MoH knowledge base 72,635 pairs (30,823 FIRE + 14,919 XLIT + profanity, pruned) (p.21-22).
- Levenshtein threshold 0.7 → 91% OOV correctly mapped (p.26).
- MoH+M-BERT F1: TRAC-I 0.66, HOT 0.88, HS 0.81 (p.32).
- MoH+MuRIL F1: TRAC-I 0.71, HOT 0.90, HS 0.85 (p.32).
- Classical ML best F1 generally 0.5-0.75 (Tables 6-7, p.32-33).
- Claimed gains: ~13% (classical ML w/ MoH), ~6% (vs baselines), ~15% (vs raw M-BERT) (p.2).
- Hyperparameters: batch 32, LR 2e-5, dropout 0.2, 10 epochs, AdamW, max seq len 128 (p.30).

## 10. Pitfalls & limitations
- Vault filename/stem is wrong ("Somali-English") — actual language pair is Hindi-English; downstream indexing risk.
- Preprint from 2021 (submitted Oct 2021, p.1) despite 2025 vault year.
- Transliteration errors propagate: proper nouns mis-mapped below threshold 0.7 (e.g., "tom"→"tum") (p.26).
- Labels inherited from source datasets, no reliability re-check; no held-out contamination analysis.
- Tweets over 128 tokens dropped for memory (p.29) — truncation bias.
- No LLM baselines (pre-LLM method); limited generalizability beyond Hinglish.

## 11. Novel ideas worth stealing
- **Partial/word-level transliteration that preserves syntax** (map only the Hindi tokens to native script, leave English intact) instead of full translation — keeps semantic + structural signal for code-switched values items; reusable when authoring or normalizing non-English benchmark text.
- **Two-source knowledge base + Levenshtein OOV recovery** with an empirically tuned similarity threshold (0.7) validated by manual mapping accuracy — a principled recipe for normalizing noisy transliterated user text.
- **n-gram frequency disambiguation** for tokens valid in both languages (e.g., "tum") — a lightweight language-ID tiebreaker.
- **Explicit profanity-vs-hate decoupling** in the annotation scope (Table 2) — a construct-validity distinction (a post can be profane-not-hate or hate-not-profane) worth encoding in any toxicity/values benchmark.
- Ablation design comparing raw vs MoH-mapped text across identical models to isolate the preprocessing contribution.

## 12. Notable quotes
- "we developed 'MoH' or (Map Only Hindi), which means 'Love' in Hindi" (p.1).
- "Text that attacks an individual or community instigates hatred, with or without using profanity, qualifies as hate speech" (p.9).
- "a threshold value of 0.6 and 0.8 correctly translated 76% and 68% of words, respectively; however, 0.7 value captured 91% of the words" (p.26).
- "This is the first work in Hate Speech Detection that preserves the semantic sense and syntactic structure of code switched text" (p.6).

## 13. UNKNOWN / not in extract
- Full baseline-comparison and Indic-Trans ablation tables (pages 34-58 not read).
- Detailed error-analysis examples and inferences (Section 7).
- Exact post-processed dataset sizes used in final splits / train-test ratios.
- Any statistical significance testing of the reported gains.
- Whether/where a Somali-English variant exists (title mismatch unresolved).
