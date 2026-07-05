---
stem: "2025-Usmana-A Large Language Model-Based Approach for Multilingual Hate Speech"
reader_model: "opus"
confidence: "high"
is_benchmark: true
theme_tags: [cultural-linguistic, saturation-discrimination, best-practices]
task_format: "mixed"
scoring_type: "exact-match"
dataset_size: 10193
dataset_construction: "scraped"
languages: [en, es, ur]
models_tested: ["GPT-3.5 Turbo", "Qwen 2.5 72B", "LLaMA 3.3 70B", "DeepSeek 67B", "BERT", "RoBERTa", "ELECTRA", "XLM-RoBERTa", "SVM", "XGBoost", "Random Forest", "Decision Tree", "CNN", "BiLSTM"]
headline_numbers: ["Trilingual dataset of 10,193 tweets: 3,834 English, 3,197 Urdu, 3,162 Spanish (p.1)", "Fleiss' Kappa = 0.821 inter-annotator agreement (p.1)", "GPT-3.5 Turbo macro F1 0.87 English, 0.85 Spanish; Qwen 2.5 72B 0.81 Urdu, 0.88 Joint (p.1)", "SVM baselines: 0.80 En, 0.78 Es, 0.77 Ur, 0.82 Joint (p.8)"]
---
## 1. Gist
This paper introduces a trilingual (English, Urdu, Spanish) hate-speech detection dataset of 10,193 tweets and benchmarks a broad model ensemble — traditional ML (SVM, XGBoost), deep learning (CNN, BiLSTM), transformers (BERT, RoBERTa, ELECTRA, XLM-RoBERTa), and LLMs (GPT-3.5 Turbo, Qwen 2.5 72B, LLaMA 3.3 70B, DeepSeek 67B) — using a translation-based standardization pipeline (Google Translate API) plus an attention-augmentation layer. Its relevance to values-alignment benchmarking is as a content-moderation / harmful-content safety benchmark that foregrounds low-resource-language equity: Urdu, with its Perso-Arabic script and code-mixing, is markedly harder (F1 0.81 vs 0.87 English), exposing a fairness gap in multilingual safety classification. It is a classification benchmark rather than a values-elicitation benchmark, but the annotation protocol (culturally-specific guidelines, cross-language pivot validation) and the low-resource discrimination findings are transferable.

## 2. Benchmark/eval design features
Construct: binary "Hateful" vs "Not-Hateful" classification of individual tweets. Answer space is binary per item. Four evaluation datasets: English, Spanish, Urdu, and a Joint Multilingual set. Label distribution across the combined corpus: 4,849 "Hateful" / 5,344 "Not-Hateful" (p.3). Primary metric is macro F1 (also precision, recall, accuracy). Feature extraction varies by model family: TF-IDF for ML, GloVe/FastText for DL, contextual embeddings + a prepended multi-head + Linformer-style sparse attention layer for transformers/LLMs (p.7). Keywords for collection deliberately span hateful and neutral/positive terms (e.g., "support," "gracias," "hope") to avoid negativity bias (p.3).

## 3. Task format & example item
MCQ/binary classification. Example items (Table 1, p.4): English Hateful — "Fuck these assholes—they deserve to die for screwing everything up!"; English Not-Hateful — "Life's a mess right now, no clue how we'll fix it." Spanish Hateful — "¡Estos hijos de puta no valen nada, que se mueran ya!"; Spanish Not-Hateful — "Todo está mal, no sé cómo vamos a salir de esto." (p.4).

## 4. Scoring / grading methodology
Exact-match against gold binary labels; macro-averaged precision/recall/F1/accuracy on a 2,039-tweet test set (20% split for ML/DL/transformers; LLMs evaluated few-shot on the whole dataset) (p.8). Confusion matrices reported per best model (Tables 10–13, p.11–12).

## 5. Dataset construction & provenance
Collected via Tweepy API from X between Jan 2024 and Feb 2025; 58,000 initial tweets filtered by keyword to a stratified 10,193 (p.3). Three native-speaking postgraduate CS annotators per language, majority-vote labels, standardized translated guidelines, joint training, and a 510-tweet (5%) cross-language pivot-validation subset annotated by all groups (p.4). Anonymized; shared only with ethical researchers ("Data will be made upon request," p.14). Translation-based pipeline standardizes all three languages via Google Translate API (p.6).

## 6. Validity evidence
Inter-annotator reliability: global Fleiss' Kappa 0.821 (English 0.83, Urdu 0.80, Spanish 0.82); cross-language Kappa 0.79 on the pivot subset (p.5). Human baseline = the annotation itself. No factor analysis (not applicable to a classification task). SVM+TF-IDF serves as the criterion baseline against which LLM gains are measured (p.12).

## 7. Saturation / discrimination
Clear discrimination across model families and languages. English/Spanish approach ceiling for LLMs (0.85–0.87) but Urdu remains well below (best 0.81; bert-base-uncased collapses to F1 0.50, XLM-RoBERTa 0.36 on Urdu, p.9). This language gap gives the benchmark strong remaining headroom specifically in low-resource and code-mixed settings. Joint multilingual training raises Qwen to 0.88, above any single-language score, showing cross-lingual transfer benefit (p.13).

## 9. Key numbers
- 10,193 tweets total; 3,834 En / 3,197 Ur / 3,162 Es (p.1)
- Fleiss' Kappa 0.821 global; cross-language 0.79 (p.5)
- Best LLM F1: En 0.87 (GPT-3.5), Es 0.85 (GPT-3.5), Ur 0.81 (Qwen), Joint 0.88 (Qwen) (p.9)
- SVM baselines: 0.80/0.78/0.77/0.82; improvements 8.75%/8.97%/5.19%/7.32% (p.12)
- Transformer Urdu collapse: BERT 0.50, XLM-R 0.36 (p.9)
- Test set = 2,039 tweets (20%) (p.8); English confusion: 920 TP, 854 TN, 166 FN, 99 FP (p.11)

## 8. Multiturn / agentic aspects
n/a — single-turn classification only.

## 10. Pitfalls & limitations
Author-admitted: Urdu low-resource performance limited by translation errors of slang/code-mixed text (e.g., "بھنچود" → "jerk" softens hostility), prompting sensitivity of LLMs, embedding limits for morphologically-rich Urdu, and LLM interpretability gaps (p.13). Observed flaws: LLMs were "trained on the entire dataset" (p.8) while ML/DL used an 80-20 split — an inconsistent, potentially contaminated evaluation protocol that makes cross-family comparison unfair. Confusing/contradictory table transcription (Tables 5/7 mislabeled). Translation-based standardization introduces artifacts that themselves cause misclassifications. "Data will be made upon request" (p.14) limits reproducibility.

## 11. Novel ideas worth stealing
- Cross-language pivot-validation subset: translate 5% of items into a shared pivot language (English) and have ALL language-group annotators label them, then report a cross-language Kappa — a cheap way to verify that separate monolingual annotation teams share a construct definition. Directly reusable for multilingual values benchmarks.
- Deliberately including neutral/positive seed keywords ("support," "gracias," "hope") to counter negativity sampling bias.
- Reporting per-language discrimination to surface fairness gaps rather than a single pooled score; the low-resource language becomes the discriminating "hard split."
- Culturally-specific annotation guidelines translated into each language with joint calibration meetings on culturally-weighted insults.

## 12. Notable quotes
- "we introduce a trilingual dataset of 10,193 tweets in English (3,834 samples), Urdu (3,197 samples), and Spanish (3,162 samples) ... achieving a Fleiss' Kappa of 0.821." (p.1)
- "LLMs were trained on the entire dataset to maximize their contextual understanding, particularly for low-resource Urdu." (p.8)
- "Urdu's lower F1 scores (0.78–0.81) reflect limited pre-training data and translation errors for slang and code-mixed texts." (p.13)

## 13. UNKNOWN / not in extract
- Exact few-shot prompt text and number of shots used for the LLMs.
- Licensing terms beyond "upon request."
- Whether the LLM "training on entire dataset" means fine-tuning or in-context; wording is ambiguous.
- Per-item difficulty statistics; only aggregate confusion matrices given.
- Whether Urdu tweets were originally in Perso-Arabic or Roman script at collection.
