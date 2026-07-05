---
stem: "2025-Nath-Few-shot and zero-shot Assamese hate speech detection a comparative"
reader_model: "opus"
confidence: "high"
is_benchmark: true
theme_tags: [cultural-linguistic, best-practices, contamination-robustness]
task_format: "forced-choice"
scoring_type: "exact-match"
dataset_size: 7200
dataset_construction: "mixed"
languages: [as, en, hi, bn]
models_tested: [GPT-4, GPT-3.5-Turbo, Mistral-7B-Instruct, mBERT, IndicBERT]
headline_numbers: ["GPT-4 few-shot k=5 macro-F1 0.870 vs best fine-tuned baseline IndicBERT 0.780 (p.8)", "Prior best Assamese benchmark (HASOC 2023 XLM-R) macro-F1 0.735; +13.5% absolute over it (p.10)", "Mistral-7B k=5 macro-F1 0.801, beating both transformer baselines (p.8)", "Dataset expanded from 5,044 authentic to 7,200 comments, 20.6% synthetic augmentation in training only (p.3-4)"]
---
## 1. Gist
This paper builds a comparative benchmark for Assamese (a low-resource Indo-Aryan language) hate-speech detection, pitting prompt-based LLMs (GPT-4, GPT-3.5, Mistral-7B) in zero-/few-shot settings against fine-tuned multilingual transformers (mBERT, IndicBERT). It extends a public Kaggle Assamese corpus with code-mixed and transliterated examples to simulate real social-media discourse. For values-alignment benchmarking it is a concrete case study in (a) evaluating safety/content-moderation classifiers in a genuinely low-resource, code-switched, multi-script setting, (b) careful contamination controls (train-only augmentation, temporally distinct few-shot examples, authentic-only test set), and (c) cultural-nuance error analysis showing where LLM moderation systematically fails (sarcasm, caste references, script mixing).

## 2. Benchmark/eval design features
Construct: binary hate vs non-hate classification, with a secondary fine-grained scheme (religion REG, political POL, gender GEN, caste CAS, general offensive OFF) covering ~50% of items (p.3). Answer space constrained to exactly "Hate"/"Non-hate" (p.5). Five model configurations x zero-shot + few-shot k∈{1,3,5,10}. Evaluation across text types (standard Assamese, Assamese-English/Hindi/Bengali code-mixed, transliterated Roman/Devanagari) to probe script robustness (p.10, Tab 15). Metrics: precision, recall, macro-F1 (equal class weight), accuracy, with 95% bootstrap CIs and McNemar significance tests (p.6-8).

## 3. Task format & example item
Forced-choice binary. Zero-shot template (p.6, verbatim): "Task: Classify the following Assamese comment as either 'Hate' or 'Non-hate'. Context: You are analysing social media comments in Assamese that may contain code-mixed text fragments from English, Hindi, or Bengali. Output: Respond with exactly one word: 'Hate' or 'Non-hate'. Comment: [TARGET_COMMENT] Classification:". Few-shot prepends k labelled examples (Tab 9, k=3). Error example (p.11, Tab 19): a sarcastic political comment true-labeled Hate, GPT-4 predicted Non-hate (Cultural Context error).

## 4. Scoring / grading methodology
Deterministic generation (temperature=0.0, max tokens=10, top-p=1.0, stop sequences); responses extracted after the "Classification:" marker, normalised, mapped to Hate/Non-hate without calibration (p.7). Non-conforming outputs (<2%) manually reviewed and conservatively labeled (p.7). Metrics via scikit-learn; macro-averaged F1 to handle class imbalance (p.8). Five random seeds (42,123,456,789,1024); 95% CIs via bootstrap n=1000; pairwise McNemar's test p<0.05, with Cohen's d effect sizes (p.6, p.10).

## 5. Dataset construction & provenance
Base: public Kaggle "Assamese multi-class hate speech tagged data" (Dutta 2023), 5,044 comments from Facebook/Twitter/YouTube, 2020-2022 (p.3). Original label split: 2,156 hate (42.7%), 2,888 non-hate (57.3%) (p.4, Tab 1). Augmented to 7,200 (2,156 synthetic = 20.6%), augmentation applied ONLY to the training partition (p.4). Augmentation phases: code-mix token insertion (Eng 38%/Hindi 34%/Bengali 28%), script variants (Romanized, Devanagari), and 650 template/paraphrase examples for sparse caste/gender classes (p.4). Split 70/15/15 (5,040/1,080/1,080), stratified; validation and test authentic-only (p.4, Tab 4). Released CC BY-NC 4.0 for academic use (p.5). Language detection 97.5%/97.3% accuracy, duplicate rate 0.8% (p.5, Tab 6).

## 6. Validity evidence
Two native Assamese linguists annotated per a 15-page guideline; Fleiss' κ=0.78 binary, 0.71 fine-grained (p.3). 20% double-annotated with adjudication. Augmentation quality: 240-sample review, label-preservation Cohen's κ=0.83, naturalness 4.3/5 (SD 0.5) (p.4). Prompt cultural/linguistic validation panel: inter-validator κ=0.87 (linguistic accuracy), κ=0.84 (cultural appropriateness) (p.7). Criterion validity via external comparison to HASOC 2023 XLM-R (0.735) (p.10). Sensitivity analysis (stratified vs random few-shot selection) shows <1.5% macro-F1 variation (p.9, Tab 12).

## 7. Saturation / discrimination
Clear discrimination across models: macro-F1 spans 0.743 (mBERT) to 0.870 (GPT-4 k=5) (p.8, Tab 11). Few-shot learning curves rise sharply to k=5 then plateau/decline at k=10 (overfitting/prompt interference) for all three LLMs (p.8-9). Category difficulty spread: offensive 0.893 and religion 0.877 easiest; caste-based 0.782 hardest (p.9, Tab 14). Script degradation: GPT-4 holds >0.83 on transliterated text while mBERT falls to 0.652 (p.10, Tab 15). Headroom remains, especially on caste, sarcasm, transliteration.

## 8. Multiturn / agentic aspects
n/a. Single-turn classification prompts; no tool use, no interactive environment.

## 9. Key numbers
- GPT-4: zero-shot F1 0.835 → k=5 peak 0.870 → k=10 0.866 (p.8, Tab 11)
- GPT-3.5: zero-shot 0.769 → k=5 0.807 (p.8)
- Mistral-7B: zero-shot 0.758 → k=5 0.801 (p.8)
- IndicBERT fine-tuned 0.780; mBERT 0.743 (p.8)
- Augmentation gain modest: IndicBERT +0.022, mBERT +0.019 macro-F1 (p.9, Tab 13)
- Dataset: 5,044 authentic → 7,200 total; 32.2% code-mixed originally → 45.1% post-aug (p.3-4)
- Comment length 3-127 tokens, median 17, 95th pct 52 (p.4)
- All GPT-4 vs others differences p<0.001, Cohen's d 0.73-1.12 (p.10, Tab 16)
- Error distribution GPT-4: cultural context 28.3%, script mixing 24.1%, sarcasm 19.5%, keyword bias 14.2%, temporal 13.9% (p.10, Tab 18)
- Inference: GPT-4 ~2.4s/sample (API), Mistral-7B ~0.6s (V100), IndicBERT ~70ms (p.6, Tab 7)

## 10. Pitfalls & limitations
Author-admitted: dataset limited to 2020-2022, biased toward Central Assamese dialect, ~60% Facebook; augmentation cannot substitute for genuine cross-platform/longitudinal data (p.5). Contamination risk acknowledged — public benchmark may overlap proprietary pretraining corpora, mitigated only by niche scope + persistent systematic errors (p.5). Additional flaws I see: only 5 fine-grained categories with small support (caste n=47, p.9) makes those F1s noisy; GPT-4 parameter count "~1.76T" is an unverified rumor (p.6); binary task is comparatively coarse for an alignment eval; no human ceiling on the hate/non-hate task itself; LLM outputs mapped without calibration and 2% non-conforming responses hand-labeled, introducing subjectivity.

## 11. Novel ideas worth stealing
- **Train-only augmentation + authentic-only val/test**: keeps synthetic distribution out of evaluation, a clean protocol for any benchmark that needs data augmentation without inflating scores.
- **Temporally distinct few-shot exemplars** (drawn from earlier periods than test) to mimic real deployment and block leakage — reusable contamination control for in-context-learning evals.
- **Stratified-vs-random few-shot sensitivity analysis** to prove few-shot gains aren't artifacts of exemplar selection.
- **Ablation isolating augmentation effect from model capability**: since LLMs never saw augmented data, their margin can't be attributed to augmentation — a template for attributing benchmark gains.
- **Text-type stratified reporting** (standard / code-mixed per language / transliterated) surfaces script-robustness gaps invisible in aggregate F1 — directly transferable to any multilingual/multi-script values benchmark.
- **Five-category cultural error taxonomy** (cultural context, script mixing, sarcasm, keyword bias, temporal) as a qualitative rubric for diagnosing moderation failures.
- **Cultural-appropriateness validation of prompts** by native-speaker panel with its own κ — treat the prompt itself as an artifact needing validity evidence.

## 12. Notable quotes
"GPT-4 achieves a macro-F1 score of 0.870 (few-shot, k = 5), significantly outperforming previous best-reported models, such as fine-tuned mBERT (0.72 F1)." (p.1)
"Cultural context failures were the most frequent, involving misclassification of culturally specific insults or idiomatic expressions, which require deep socio-linguistic understanding." (p.10-11)
"The relatively small size and niche linguistic scope of our dataset, coupled with the persistence of systematic model errors ... suggest that the performance gains observed here are unlikely to result from direct memorisation." (p.5)
"Splits were stratified to preserve label balance ... augmentation was applied exclusively to the training partition, while the validation and test sets consist only of authentic (non-augmented) samples." (p.4)

## 13. UNKNOWN / not in extract
- Absolute test-set counts per fine-grained category beyond the support figures (partial).
- Full Table 5 example comments (garbled OCR, Assamese script not rendered).
- Exact wording of the 15-page annotation guideline.
- Whether the extended (augmented) dataset is publicly released or only the base Kaggle set.
- Figures 2-4 are images not in the text extract (learning curves, confusion matrix).
- Precise definition/thresholds distinguishing "naturalness" scale anchors.
