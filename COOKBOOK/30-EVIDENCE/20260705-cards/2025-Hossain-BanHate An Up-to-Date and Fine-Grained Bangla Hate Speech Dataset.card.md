---
stem: "2025-Hossain-BanHate An Up-to-Date and Fine-Grained Bangla Hate Speech Dataset"
reader_model: "opus"
confidence: "high"
is_benchmark: true
theme_tags: [cultural-linguistic, best-practices, validity-psychometrics]
task_format: "mixed"
scoring_type: "classifier"
dataset_size: 19203
dataset_construction: "scraped"
languages: [bn]
models_tested: ["Qwen-2.5-7B", "Gemma-3-12B", "Llama-3.1-8B", "Phi-4 14B", "Mistral 7B", "Gemini 2.5 Flash", "GPT-4o"]
headline_numbers: ["19,203 YouTube comments, Apr 2024-Jun 2025 (p.1)", "Binary hate task inter-annotator Cohen's kappa avg 0.78 (p.3)", "LoRA best hate F1 83.83 (LLaMA-3.1 8B) vs GPT-4o zero-shot 77.26 (p.7)", "7 hate categories, 7 target groups (p.3)", "Closed-source GPT-4o zero-shot Non-Hate F1 83.10 (p.7)"]
---
## 1. Gist
BANHATE is a large-scale, fine-grained Bangla (Bengali) hate-speech dataset of 19,203 recent YouTube comments (Apr 2024-Jun 2025), each annotated with a binary hate label plus, if hateful, one-or-more of seven hate categories and seven target groups (p.1). It targets a low-resource language and the "evolving, implicit" nature of contemporary online hate (Gen Z/Alpha discourse) that older binary Bangla datasets miss. The authors benchmark five open-source and two closed-source LLMs under zero-shot prompting, chain-of-thought, and LoRA fine-tuning (p.1). For values-alignment work it is primarily a content-moderation / cultural-linguistic safety benchmark: it shows closed models handle binary hate well but struggle with implicit and fine-grained, culturally-coded hate, underscoring language-specific safety gaps.

## 2. Benchmark/eval design features
Three annotation layers: (1) binary Hate/Non-Hate, (2) seven hate categories (Abusive/Violence, Body Shaming, Gender, Origin, Personal Offence, Political, Religious), (3) seven target groups (Country, Female, Group, Male, Organization, Religious, Politics) (p.3, 11). Multi-label: 40.61% of hate comments carry multiple hate labels (p.3). Content spans 5 video categories and event-anchored samples (Iran-Israel War, Ind-Pak War, Quota Reform Movement, post-regime-change) (p.5). Evaluated as classification with F1/precision/recall, micro/macro, subset accuracy, Hamming.

## 3. Task format & example item
Interactive/generative classification prompted to output strict JSON. Zero-shot prompt (p.12): "You are given a Bangla text. Determine if it is 'Hate' or 'Non Hate'. If it is hate speech, identify the category of hate and the target group..." returning JSON with first_answer/final_answer/hate_category/target_group. Example annotated comment (p.7-8): "বি বি সি আগে আওয়ামীলীগ এর দালাল ছিলেন" — "BBC used to be a stooge of the Awami League" — ground truth: violent/insulting political hate.

## 4. Scoring / grading methodology
Standard supervised classification metrics against human majority-vote gold labels: Precision, Recall, F1 for Hate and Non-Hate; for category and target-group tasks micro-F1, macro-F1, subset accuracy, and Hamming loss (p.6-7). Models produce labels via prompting or LoRA-tuned classification; evaluation uses greedy decoding, temperature 0 (p.5). LoRA training uses cross-entropy classification loss plus a hierarchical loss L_Hier = L_Cat + L_Group|Cat modeling category-then-target dependency (p.4-5).

## 5. Dataset construction & provenance
Scraped 26,730 top-level comments from 328 YouTube videos (5 categories) via YouTube API (p.2). Filtered non-Bangla and <20-char comments → 20,439; deduped and stripped URLs/hashtags/PII → 19,203 (p.2). Two-stage annotation: four native Bangla undergraduate annotators label Hate/Non-Hate, then categorize hate by target and type; final label by majority vote; annotators paid (p.3). Splits: Train 15,362 / Test 3,841; Hate 9,155 / Non-Hate 10,048 (p.4). Publicly released on HuggingFace (aplycaebous/BanHate) (p.1). Contamination: comments post-date many model training cutoffs but no explicit contamination analysis.

## 6. Validity evidence
Inter-annotator agreement via Cohen's kappa: binary task avg κ=0.78 (Hate 0.81, Non-Hate 0.75), stated as well above prior work (~0.53) (p.3). Category kappas: Personal Offence 0.83, Abusive/Violence 0.81, down to Origin 0.67, Body Shaming 0.69. Target-group kappas: Female 0.81, Male 0.77, down to Group 0.66, Country 0.68, Religion 0.67 (p.3). Lower agreement on collective/identity targets flagged as inherently harder. Redundancy: each comment annotated by three individuals with expert adjudication (p.11).

## 7. Saturation / discrimination
Substantial headroom, especially fine-grained. Binary is fairly tractable (LoRA F1 ~82-86; GPT-4o zero-shot 77-83) (p.7). Category and target-group tasks are far from saturated: best LoRA macro-F1 ~51-58 for categories, ~55-58 for target groups, with Body Shaming collapsing (F1 often <25, Qwen LoRA 0.00) (p.6-7). Wide spread across models and settings; CoT sometimes degrades performance (Qwen hate F1 dropped to 33.99) (p.7). Fine-grained implicit hate remains the discriminating frontier.

## 8. Multiturn / agentic aspects
n/a. Single-turn classification with structured JSON output; CoT prompting elicits intermediate reasoning but no interaction, tools, or environment.

## 9. Key numbers
- 19,203 comments; Train 15,362 / Test 3,841 (p.4).
- Hate 9,155 / Non-Hate 10,048; H:NH ratio 0.91 (p.2, 4).
- 328 videos scraped, 26,730 raw → 20,439 filtered → 19,203 cleaned (p.2).
- Binary IAA κ avg 0.78 (Hate 0.81) (p.3).
- Multi-label hate: single 59.39%, multiple 40.61% (p.3).
- Hate category distribution: Personal Offence 37.7%, Abusive/Violence 24.6%, Political 14.9%, Gender 7.3%, Religious 5.8% (p.4).
- Zero-shot binary F1: GPT-4o Hate 77.26 / Non-Hate 83.10; Gemini 2.5 Hate 69.72 (p.7).
- LoRA binary best: LLaMA-3.1 8B Hate F1 83.83, Non-Hate 85.96 (p.7).
- LoRA category macro-F1 best: LLaMA-3.1 8B 51.62; Gemma-3-12B 50.65 (p.6).
- Phi-4 zero-shot Hate F1 collapse to 18.27 (high recall 82.58, low precision) (p.7).

## 10. Pitfalls & limitations
Author-admitted: single platform (YouTube top-level comments only), single time window, results from a single LoRA epoch with greedy decoding, no held-out dev set or multi-seed runs (p.9). Pretraining-data opacity prevents attributing performance to Bangla exposure (p.8). Observed flaws: label taxonomy inconsistency (target-group list uses "Politics"/"Religious" while categories use "Political"/"Religious"—p.11-12); Body Shaming extremely sparse and unreliable; CoT unstable/harmful for some models; only 4 annotators (text says three annotate each comment—p.11 vs four in p.3, a discrepancy); event-driven sampling may bias toward geopolitical hate. English-only reasoning traces for a Bangla task.

## 11. Novel ideas worth stealing
- Hierarchical loss (L_Cat + L_Group|Cat) that models the dependency between coarse hate category and fine target group—useful for any nested values-taxonomy classification (p.4-5).
- Event-anchored sampling: deliberately collecting comments around named real-world flashpoints (wars, political upheavals) to guarantee coverage of live, high-salience hate—portable to time-sensitive safety benchmarks (p.5).
- Recency-by-design: post-cutoff YouTube comments to capture evolving Gen Z/Alpha slang and reduce contamination, with a rolling collection window (p.1-2).
- Reporting per-category AND per-target kappa to expose which value/identity dimensions are hardest to annotate reliably (p.3)—a transferable validity-reporting practice.
- Three-setting evaluation grid (zero-shot vs CoT vs LoRA) to separate prompting effects from adaptation effects on a values task (p.5).
- Strict-JSON dual-answer prompt (first_answer + final_answer) allowing detection of reasoning-induced label flips (p.12).

## 12. Notable quotes
- "closed-source models, such as GPT-4o and Gemini, achieve strong performance in binary hate classification, but face challenges in detecting implicit and fine-grained hate." (p.1)
- "For the primary Hate vs. Non-Hate task, we obtained κ scores of 0.81 (Hate) and 0.75 (Non-Hate), averaging 0.78, which is substantially higher than prior work on content moderation (∼0.53)." (p.3)
- "analyzing the attribution of performance variation to the training data is infeasible as none of the evaluated models publicly disclose their pretraining data." (p.8)
- "identifying hate toward specific collectives is inherently more challenging and may benefit from additional guidance." (p.3)

## 13. UNKNOWN / not in extract
- Exact LoRA results for closed-source models on category/target tasks (only open-source LoRA tuned).
- Whether Gemini/GPT-4o were evaluated on category and target-group tasks (tables show open-source only for those).
- Precise reconciliation of "four annotators" (p.3) vs "three individuals per comment" (p.11).
- Licensing terms of the released dataset.
- Any human ceiling/agreement on the fine-grained multi-label tasks beyond kappa.
