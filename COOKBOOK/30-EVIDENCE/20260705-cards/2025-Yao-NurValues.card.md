---
stem: "2025-Yao-NurValues"
reader_model: "opus"
confidence: "high"
is_benchmark: true
theme_tags: [normative-ethics, cultural-linguistic, saturation-discrimination, contamination-robustness]
task_format: "free-text"
scoring_type: "classifier"
dataset_size: 4400
dataset_construction: "mixed"
languages: [zh, en]
models_tested: [Claude 3.5 Sonnet, Claude 3.7 Sonnet, Claude 3.5 Haiku, GPT-4o, o1, Gemini-2.5-Pro-Preview, Gemini-2.0-Flash, DeepSeek-V3, DeepSeek-R1, Qwen-QwQ-Plus, Qwen 2.5-Omni-7B, Qwen 2.5-72B-Instruct, Llama-4-Maverick-17B-128E, Llama-4-Scout-17B-16E, Llama-3.3-70B-Instruct, Llama-3.1-70B-Instruct, Llama-3-70B-Instruct, Llama-3-8B-Instruct, HuatuoGPT-o1-72B, HuatuoGPT-o1-70B, Llama3-Med42-70B, Llama3-Med42-8B, OpenBioLLM-70B]
headline_numbers: ["1,100 real-world nursing instances → 2,200 Easy + 2,200 Hard = 4,400 (p.1)", "DeepSeek-V3 best Easy-Level Ma-F1 94.55 (p.1)", "Claude 3.5 Sonnet best Hard-Level Ma-F1 89.43 (p.1)", "Fleiss kappa = 0.73 among 5 nurse annotators (p.4)", "Justice hardest dimension; Hard-Level avg drops 56.16 pts to 32.29 (p.7)"]
---
## 1. Gist
NurValues is the first benchmark for nursing value alignment of LLMs in clinical context, built from a five-month ethnographic field study across three hospital tiers in China. It distills five nursing value dimensions from international nursing codes (Altruism, Human Dignity, Integrity, Justice, Professionalism) and collects 1,100 real-world nurse behavior instances, each annotated by clinical nurses and paired with an o1-generated counterfactual of reversed ethical polarity (Easy-Level, 2,200 instances). Each instance is further rewritten into an adversarial persuasive dialogue with misleading cues (Hard-Level, 2,200). It matters for values-alignment benchmarking as a rare ecologically-valid, domain-grounded, two-difficulty benchmark that sharply discriminates 23 LLMs and shows domain fine-tuning does not improve moral reasoning.

## 2. Benchmark/eval design features
Constructs: alignment with five nursing values. Task per item: given a case (Easy) or dialogue (Hard) plus an instruction, decide whether the nurse's action conforms to the annotated value (binary judgment against gold alignment label). Balanced by construction: every original case has a value-aligned and a value-violating counterfactual. Two difficulty tiers stress-test robustness under adversarial framing (persuasion, traps, deception). Bilingual (Chinese default; English translation for models weak in Chinese). Hierarchical structure (five dimensions × positive/negative polarity × difficulty).

## 3. Task format & example item
Binary alignment judgment. Instruction: "we feed the case text and an instruction to the LLM and ask it to decide whether the nurse's action conforms to the annotated value" (Easy); Hard feeds the entire dialogue (p.17, Fig.7 p.18). Counterfactual example (p.2, p.5): "administering two different vaccines to a child in two separate arms" (value-aligned) is flipped into "injecting both vaccines into the same arm" (value-violating), preserving context/length/factual integrity. Full verbatim prompt text is in Fig. 7 (image, not transcribed in extract).

## 4. Scoring / grading methodology
Accuracy, F1, and Macro-F1 (Ma-F1) against gold alignment labels (p.6-7). Reported per model, per difficulty level, and per value dimension (Table 4, 5, 8). McNemar tests for pairwise model significance (p.8). Zero-shot standard I/O prompting by default; ICL variants (CoT, Self-Consistency, K-Shot) evaluated separately (Table 6). Classification-style scoring of the model's conform/not-conform output.

## 5. Dataset construction & provenance
Five-month (Dec 2024–Apr 2025) observer-as-witness field study, 300+ hours across a tertiary, secondary, and primary hospital in Zhejiang, 11 departments (p.3-4). 976 raw instances collected under a saturation-based termination rule (<3 non-duplicative instances/day) (p.4). Five clinical nurses annotate (4 annotators + 1 reviewer); 124 dual-value instances duplicated → 1,100 labeled samples; Fleiss kappa 0.73 (p.4). o1 generates counterfactuals (Easy, 2,200) and jailbreak-style adversarial dialogues (Hard, 2,200), all manually reviewed. PII removed, verbal consent obtained. Public on HuggingFace (Ben012345/NurValues) (p.1).

## 6. Validity evidence
Inter-rater reliability Fleiss kappa = 0.73 ("high agreement", p.4). Ecological validity from real-world field observation. Topic-consistency check: 3 SoTA LLMs score semantic similarity of Hard vs original, >82% score ≥8, all averages >8 (p.5). Linguistic-feature analysis confirms Hard-Level has longer, more complex text (Table 3, p.6). Discriminant evidence: McNemar tests show Hard-Level separates 91.7% of model pairs at p<0.001 while agreeing for near-identical models (p.8). No separate human performance ceiling reported.

## 7. Saturation / discrimination
Easy-Level shows ceiling effects: 16/23 models exceed 90% accuracy, top cluster within 0.15% (p.6) — near-saturated. Hard-Level opens large headroom: sharp degradation (DeepSeek-V3 drops 51.6 points to 42.95% acc; Llama-3-8B falls 77.32 points to 6.73%) (p.6). Justice is consistently hardest (Easy avg Ma-F1 83.31 lowest; Hard 27.26) (p.7). Hard-Level average falls 56.16 points to 32.29 (p.7), leaving substantial discrimination and headroom.

## 8. Multiturn / agentic aspects
Hard-Level items are two-speaker dialogues embedding persuasion/traps/deception, but evaluation is single-shot (the full dialogue is fed once and a judgment requested) — a scripted adversarial-context format rather than interactive multiturn. No tool use or live environment.

## 9. Key numbers
- 4,400 total: 2,200 Easy + 2,200 Hard; from 1,100 labeled instances (p.1, p.9)
- 976 raw field instances; 124 dual-value; saturation <3/day (p.4)
- Fleiss kappa 0.73 (p.4)
- Value distribution: PRO 594, HD 532, INT 522, ALT 478, JUS 74 (p.5)
- Behavior types: Operational 38.1%, Communicative 36.7%, Emergency 7.5% (p.5)
- Easy best DeepSeek-V3 94.55 Ma-F1; Hard best Claude 3.5 Sonnet 89.43 (p.1, Table 4 p.7)
- Gen LLMs avg Hard 43.12% acc vs Medical LLMs 23.25% (p.6)
- ICL: DeepSeek-V3 CoT lifts Hard Ma-F1 34.29→57.32 (+23.03) (p.8); Llama-3.1-70B K-Shot Easy +18.60 (p.8)
- Hard-Level McNemar: 232/253 pairs (91.7%) significant at p<0.001 (p.8)

## 10. Pitfalls & limitations
Author-admitted: limited coverage of value dimensions; regional/cultural bias (single Chinese province); Hard-Level adversarial instances LLM-generated hence limited realism and stylistic homogeneity ("Easy-Level dataset currently remains the most rigorous and reliable component"); possible translation semantic shift; narrow methodological scope (ICL only) (p.9). Visible flaws: Justice severely underrepresented (74 samples, 3.36%) undermines that dimension's estimates; counterfactuals and adversarial dialogues both generated by o1 (a tested-adjacent model) risk generator artifacts and contamination; binary conform/not-conform simplifies moral judgment; Fig.7 prompt not transcribed.

## 11. Novel ideas worth stealing
- Counterfactual polarity-flipping: pair each real instance with a minimally-edited value-violating twin (same context/length/facts, reversed ethics) to build a perfectly balanced dataset and isolate the value signal from surface content.
- Two-difficulty design where the Hard tier is the same content re-embedded in a persuasive adversarial dialogue — a clean way to add contamination/robustness stress without changing ground truth.
- Ecological grounding via longitudinal field observation with a saturation-based stopping rule — a reusable recipe for authentic, non-scraped values items.
- Topic-consistency verification (LLM-scored semantic similarity ≥8) to prove the hard transform preserves the underlying construct.
- Domain-vs-general contrast: including medical fine-tunes and their base models to test whether capability fine-tuning transfers to value alignment (it did not).
- Per-dimension reporting exposing that one construct (Justice) is systematically hardest — informs targeted item collection.

## 12. Notable quotes
- "DeepSeek-V3 achieves the highest performance on the Easy-Level dataset (94.55), where Claude 3.5 Sonnet outperforms other models on the Hard-Level dataset (89.43), significantly surpassing the medical LLMs." (p.1)
- "This suggests that domain-specific fine-tuning improves clinical Q&A but not ethical reasoning, where general LLMs trained with broader human feedback perform more reliably." (p.6)
- "adversarial instances in Hard-Level subset are generated using LLMs, causing their limited realism... Therefore, the Easy-Level dataset currently remains the most rigorous and reliable component of NurValues." (p.9)
- "Justice is notably underrepresented, with only 74 samples in total (3.36%). This imbalance reflects the relative rarity of justice-related behaviors in the observed real-world nursing scenarios." (p.5)

## 13. UNKNOWN / not in extract
- Verbatim evaluation prompt wording (Fig. 7 is an image).
- Licensing terms of the HuggingFace dataset.
- Exact train/test/dev splits (appears to be full-set evaluation, no split stated).
- Human accuracy baseline on the tasks.
- Full per-model per-dimension numbers (Tables 8+ partially in appendix, not fully read).
- Details of the jailbreak techniques used for Hard-Level generation.
