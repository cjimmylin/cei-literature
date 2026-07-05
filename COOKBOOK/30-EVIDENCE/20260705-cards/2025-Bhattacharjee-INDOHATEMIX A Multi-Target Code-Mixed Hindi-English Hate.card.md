---
stem: "2025-Bhattacharjee-INDOHATEMIX A Multi-Target Code-Mixed Hindi-English Hate"
reader_model: "sonnet"
confidence: "high"
is_benchmark: true
theme_tags: [cultural-linguistic, llm-judges-scoring, validity-psychometrics, best-practices]
task_format: "MCQ"
scoring_type: "classifier"
dataset_size: 11725
dataset_construction: "crowdsourced"
languages: ["hi", "en"]
models_tested: ["mBERT", "XLM-RoBERTa", "Mistral-7B", "LLaMA3.1-8B", "InternLM2.5-7B", "Qwen2.5-7B", "GPT-4o-mini", "Perspective API"]
headline_numbers:
  - "LLaMA3.1-8B achieves 0.91 F1 on HATEXPLAIN vs mBERT 0.87 (p.7)"
  - "LLaMA3.1-8B achieves 0.82 F1 on INDOHATEMIX vs mBERT 0.77 (p.7)"
  - "LLaMA3.1-8B fine-tuned on 10% data still outperforms mBERT trained on full dataset (p.7-8)"
  - "LLaMA3.1-8B trained on HATEXPLAIN and tested on all three datasets shows average 12.15% relative accuracy gain over mBERT (p.6)"
  - "INDOHATEMIX: 11,725 samples, 4,457 hate (38.01%), 7,268 non-hate (61.99%) (p.4)"
  - "Inter-annotator agreement Fleiss' Kappa = 0.685 on INDOHATEMIX (p.4)"
---
## 1. Gist
This 11-page conference/preprint paper introduces INDOHATEMIX, a new 11,725-sample Hindi-English code-mixed hate speech benchmark curated from the Koo microblogging platform (India's Twitter alternative), and uses it alongside HATEXPLAIN and IMPLICITHATE to benchmark a range of models from fine-tuned mBERT to SOTA LLMs (LLaMA-3.1-8B, Mistral-7B, Qwen2.5-7B, InternLM2.5-7B, GPT-4o-mini). The central claim: modern LLMs consistently outperform task-specific transformer models on hate speech detection, even in code-mixed multilingual environments, and even when fine-tuned on only 10% of available training data. For values-alignment benchmarking, the paper is relevant as (1) a case study in constructing culturally grounded evaluation datasets for a non-Western, code-mixed linguistic context; and (2) empirical evidence that LLMs generalise across hate-detection scenarios better than specialised models.

## 2. Benchmark/eval design features
**INDOHATEMIX dataset:**
- Binary classification: Hate (1) vs. Non-Hate (0)
- Source: Koo platform posts, Dec 2023–Jan 2024
- Collection strategy: keyword-based seed accounts on politically and religiously charged topics (Israel, Palestine, Hamas, Khalistan, Pakistan, Elections, etc.), then follower expansion
- Filtering: 5-55 words per post; URL/emoji removal; near-duplicate removal (cosine similarity); hashtag retention (# symbol stripped)
- Annotation: 3 expert human annotators, manual, contextual; ambiguous cases resolved by consensus
- Fleiss' Kappa = 0.685 (substantial agreement)
- 70-20-10 train-test-validation split

**HATEXPLAIN (prior dataset, used as benchmark):**
- 12,375 samples; 3-way: hate speech, offensive, normal; includes target group and rationale annotations
- For this study, restricted to binary hate vs. normal; 594 hate + 782 normal from official test set

**IMPLICITHATE (prior dataset, used as benchmark):**
- 21,480 tweets; implicit hate, explicit hate, not hate → binarised (hate=1, not_hate=0)
- 80-20 train-test split (stratified)

**Models benchmarked:** mBERT, XLM-RoBERTa (BERT-based); Perspective API (Google); Mistral-7B, LLaMA3.1-8B, InternLM2.5-7B, Qwen2.5-7B (fine-tuned open-source LLMs); GPT-4o-mini (zero-shot only).

**Evaluation metrics:** Accuracy, Precision, Recall, F1-score (macro).

## 3. Task format & example item
Binary classification (Hate/Non-Hate). Verbatim annotated example of hate speech (p.4):
> "a clever enemy is much better than a stupid friend. despite knowing fact, party leaders hug & felicitate him."
Annotated as hate speech because "use of terms like 'enemy' and the context of criticizing political leaders indicated a negative sentiment directed at a specific group."

Non-hate example:
> "yes, they must condemn this dastardly act in a loud and clear voice."
Not hate because it "calls for condemnation rather than inciting hostility."

LLM prompt template used (p.6):
```
Instruction: "Review the provided statement and classify it as 'Hate' or 'Non-Hate.' Return '1' for Hate and '0' for Non-Hate."
Input: "{statement}"
Output: "{label}"
```

## 4. Scoring / grading methodology
- BERT models: fine-tuned with cross-entropy; evaluated by accuracy/precision/recall/F1
- LLMs: fine-tuned with LoRA (rank 8, alpha 16) on full dataset or 10% subset; same classification prompt across all models
- Perspective API: maximum of six scores (TOXICITY, SEVERE_TOXICITY, IDENTITY_ATTACK, INSULT, PROFANITY, THREAT) > 0.5 threshold → Hate
- GPT-4o-mini: zero-shot only (cannot be fine-tuned in this setup)
- Transfer learning: models fine-tuned on one dataset and evaluated on all three (cross-dataset generalisation)

## 5. Dataset construction & provenance
- INDOHATEMIX: 11,725 samples from Koo platform (Dec 2023–Jan 2024); keyword-seeded, follower-expanded; manually annotated by 3 experts; Fleiss' Kappa = 0.685
- Near-duplicate removal via cosine similarity
- Dataset is not released under a named open license in the extract; release status unclear
- HATEXPLAIN (Mathew et al., 2021): public benchmark from prior work
- IMPLICITHATE (ElSherief et al., 2021): public benchmark from prior work
- All experiments on single A100 40GB GPU

## 6. Validity evidence
- Inter-annotator agreement: Fleiss' Kappa = 0.685 (substantial, per standard interpretation) (p.4)
- Construct validity partially evidenced by target-group analysis: INDOHATEMIX shows mixed religious+political targeting (Hindus, Muslims, Sikhs plus Rahul Gandhi, Kejriwal, Modi), consistent with Indian online discourse patterns; HATEXPLAIN shows religious targeting (Muslims, Jews); IMPLICITHATE shows racial implicit bias (African Americans, Mexicans, Muslims) (p.4-5)
- Cross-dataset transfer experiments provide criterion validity: LLMs generalise better than BERT models
- No formal construct/factor analysis of hate speech dimensions

## 7. Saturation / discrimination
- BERT-based models hit a performance ceiling (~0.87 F1) on HATEXPLAIN and plateau around 0.73-0.77 on INDOHATEMIX
- LLMs push accuracy +4% on HATEXPLAIN, +8% on IMPLICITHATE, +14% on INDOHATEMIX vs. BERT (p.6)
- INDOHATEMIX is harder (lower BERT scores) due to code-mixing and cultural nuance; this is the intended discriminative contribution
- GPT-4o-mini in zero-shot underperforms fine-tuned open-source LLMs, suggesting fine-tuning on culturally grounded data matters even for capable proprietary models
- XLM-RoBERTa F1 on INDOHATEMIX collapses to 0.33 (despite 0.74 accuracy), revealing a recall problem — essentially predicts majority class (p.7 Table II)

## 8. Multiturn / agentic aspects
n/a — single-turn binary classification task.

## 9. Key numbers
- INDOHATEMIX: 11,725 samples; 4,457 hate (38.01%); 7,268 non-hate (61.99%); avg length 22.20 words (p.4)
- HATEXPLAIN: 12,375 samples; 5,342 hate (43.17%); avg 23.5 words (p.4)
- IMPLICITHATE: 21,480 samples; 8,189 hate (38.12%); avg 16.81 words (p.4)
- Fleiss' Kappa INDOHATEMIX: 0.685 (p.4)
- LLaMA3.1-8B on HATEXPLAIN: Accuracy=0.91, F1=0.91 (p.7)
- LLaMA3.1-8B on INDOHATEMIX: Accuracy=0.83, F1=0.82 (p.7)
- mBERT on INDOHATEMIX: Accuracy=0.73, F1=0.77 (p.7)
- Average accuracy gain of LLaMA over mBERT in transfer learning: 12.15% (p.6)
- LLaMA3.1-8B LoRA adapters add ~4 million trainable parameters vs mBERT's 179 million (p.7-8)
- All LLM fine-tuning: 3 epochs, AdamW, lr=5e-5, batch=1, LoRA r=8 α=16 (p.6)

## 10. Pitfalls & limitations
- INDOHATEMIX is limited to Koo platform; Koo was shut down in 2024, limiting reproducibility and platform generalisability
- Keyword-based seed strategy may over-represent certain types of political/religious hate and miss hate targeting other groups (caste, gender, sexuality)
- Only 3 annotators; cultural competency of annotators in both Hindi and English code-mixing context is not described
- Zero-shot GPT-4o-mini comparison is unfair (other LLMs fine-tuned); gaps may reflect scale/pretraining rather than architectural differences
- Simple direct prompting without CoT or few-shot; authors acknowledge this sets a conservative baseline but do not explore more powerful prompting
- Linguistic complexity: transliterated Hindi (Devanagari written in Roman script) is distinct from code-mixed Hinglish; the paper treats both together
- No analysis of intersectional hate (e.g., targeting women of a specific religion)

## 11. Novel ideas worth stealing
1. **Code-mixed benchmark as a stress test for LLM generalisation:** The INDOHATEMIX-style dataset — code-mixed, transliterated, culturally grounded, informal register — provides a template for stress-testing values-alignment benchmarks in non-English contexts. Building analogous datasets for other language pairs (Swahili-English, Arabic-French, etc.) would test whether alignment generalisations hold globally.

2. **Target-group distribution as a dataset validity metric:** Analysing which groups are targeted in a hate speech dataset (and comparing that distribution across datasets) reveals the social biases embedded in the benchmark. Values benchmarks should similarly report *whose* values are represented and which groups are centred.

3. **10% data regime as a robustness check:** Testing whether LLMs fine-tuned on only 10% of the data outperform classical models on 100% of data is a powerful efficiency argument for the LLM paradigm and a useful experimental design for future benchmark evaluations.

4. **Cross-dataset transfer as validation of benchmark generalisability:** Training on dataset A and evaluating on datasets B and C tests whether the benchmark captures generalizable constructs or merely dataset-specific artefacts. This cross-dataset transfer evaluation design should become standard in values-alignment benchmark validation.

5. **Fleiss' Kappa + consensus review for adversarial/subjective annotation:** The annotation protocol (three experts, Fleiss' Kappa measured, ambiguous cases reviewed collaboratively) provides a higher-validity baseline than crowdsourced majority-vote annotation — particularly important for cultural and religious hate speech where context is critical.

## 12. Notable quotes
- "Our extensive experiments show that cutting-edge LLMs (such as, LLaMA-3.1) consistently outperform task-specific BERT-based models, even when fine-tuned on significantly less data." (p.1)
- "This raises the question of whether future works should prioritize developing specialized models or focus on curating richer and more varied datasets to further enhance the effectiveness of LLMs." (p.1)
- "Each dataset brings its own style and focus, so models must be trained and tested with these differences in mind." (p.5)
- "Rather than relying on specialized dataset-specific solutions, our results suggest that leveraging general-purpose LLMs, especially when fine-tuned with culturally and linguistically diverse datasets like INDOHATEMIX, can lead to more reliable and context-sensitive hate speech detection frameworks." (p.9)

## 13. UNKNOWN / not in extract
- Whether INDOHATEMIX has been publicly released (URL/DOI for dataset not provided in extract)
- Full error analysis table (described as Figure 3 / Table 3 but not readable as text in this extract)
- Specific Koo API collection details or ethical approval
- Whether the code-mixed posts are tokenised differently from pure English/Hindi
- Demographic information about the three annotators
- Results broken down by hate target category (religious vs. political)
