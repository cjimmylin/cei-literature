---
stem: "2025-Lee-KOTOX A Korean Toxic Dataset for Deobfuscation and Detoxification"
reader_model: "sonnet"
confidence: "high"
is_benchmark: true
theme_tags: [cultural-linguistic, contamination-robustness, design-space]
task_format: "mixed"
scoring_type: "classifier"
dataset_size: 6882
dataset_construction: "mixed"
languages: ["ko"]
models_tested: ["GPT-4.1", "Qwen2.5-7B-Instruct", "EXAONE-3.5-7.8B-Instruct", "Llama-3-Korean-Bllossom-8B", "HateBERT", "RoBERTa", "XLM-R"]
headline_numbers:
  - "XLM-R trained only on non-obfuscated toxic data: F1 drops from 95.06 (non-obfuscated) to 53.66 (obfuscated), a gap of 41.40pp (p.6)"
  - "Fine-tuning on KOTOX reduces robustness gap by up to 34.67pp (p.7)"
  - "Human deobfuscation BERTScore ~95.6 vs. fine-tuned Qwen2.5 77.9 — 17.75pp gap (p.8)"
  - "Inter-annotator agreement (Gwet's AC1) = 0.7408, p < 0.001 for source dataset filtering (p.5)"
---
## 1. Gist
KOTOX is the first Korean dataset that jointly supports obfuscated toxic text detection, deobfuscation, and detoxification. The paper introduces a linguistically-grounded taxonomy of 17 Korean obfuscation rules across five categories (phonological, iconological, transliteration, syntactic, pragmatic), exploiting unique properties of Korean (agglutinative morphology, Hangeul decomposability, multiscript fluency). The dataset provides 6,882 instances of (neutral, toxic, obfuscated-neutral, obfuscated-toxic) quadruples, enabling three evaluation tasks. The core finding is that current LLMs—including GPT-4.1—are substantially degraded by Korean obfuscation, but fine-tuning on KOTOX improves robustness. For values-alignment benchmarking, KOTOX matters as an example of how content-safety benchmarks must account for language-specific evasion tactics, and as a methodological template for building obfuscation-robust evaluation resources in other languages.

## 2. Benchmark/eval design features
Three tasks are defined and benchmarked:
1. **Obfuscated Toxic Text Classification**: Binary toxicity detection on obfuscated Korean text. Tests model robustness to surface-form evasion.
2. **Neutral Text Deobfuscation**: Given obfuscated neutral text, recover the original. A constrained text-generation task.
3. **Obfuscated Toxic Text Sanitization**: Given obfuscated toxic text, produce deobfuscated neutral text. Combines both steps; the hardest task.

The key design innovation is the taxonomy of 17 transformation rules grounded in Korean linguistic properties, applied algorithmically to produce controlled, systematic obfuscations rather than random perturbations. The dataset provides parallel quadruples allowing fine-grained ablation of rule difficulty.

## 3. Task format & example item
Phonological obfuscation example (p.12):
- Original: 한국인들만 알아볼 수 (Koreans can only see)
- Obfuscated: 한꾹인뜰만 알아뽈쑤 (lenis→tense consonant substitution)

Iconological example (p.13):
- Original: 쭈꾸미 (webfoot octopus)
- Obfuscated: 卒꾸미 (CJK character substitution)

For the classification task, models receive obfuscated text and must output toxic/non-toxic. For deobfuscation/sanitization, models generate a target string.

## 4. Scoring / grading methodology
- Classification: F1-score on binary toxic/non-toxic labels
- Deobfuscation and Sanitization: BERTScore (semantic similarity) and chrF (character n-gram F-score)
- Sanitization additionally: Google Jigsaw Perspective API toxicity score (lower = less toxic)
- Human baseline: 3 Korean native speakers deobfuscated 500 test samples; their BERTScore and chrF compared against models

## 5. Dataset construction & provenance
Source: K/DA dataset (Jeon et al., 2025) — 7,555 Korean neutral-toxic pairs. Three Korean natives manually filtered to 2,294 high-quality pairs (Gwet's AC1=0.7408) using a 10-item rubric for label fidelity, linguistic validity, and ethical concerns (PII removal). Obfuscated counterparts generated algorithmically using 17 transformation rules with k ∈ {2,3,4} rule applications per pair, yielding 3 obfuscated variants per pair → total ~6,882 instances. Split: 8:1:1 train/val/test (5,505/687/690). Wild dataset for generalization: 144 real-world obfuscated reviews from Agoda, Google Maps, Booking.com.

## 6. Validity evidence
Human deobfuscation evaluation on 500 test samples showed BERTScore ~95.6 and chrF ~82.1, validating that transformation rules preserve semantic content while introducing surface-form variation (p.8). Rules have very low inter-rule correlation (Figure 11, referenced), enabling independent interpretation. Wild dataset evaluation showed similar performance trends to KOTOX, confirming real-world representativeness.

## 7. Saturation / discrimination
Strong discrimination observed: XLM-R drops from F1=95.06 to 53.66 under obfuscation without KOTOX training (41.40pp gap). Rule-level analysis shows spacing perturbation (Rule 15) and emoji insertion (Rule 17) cause highest error rates, while systematic phonological rules cause lower rates. GPT-4.1 base shows smaller gaps (~11pp) than encoder models (~21-41pp), but still substantially degraded. Fine-tuning on KOTOX reduces gaps across models.

## 8. Multiturn / agentic aspects
n/a. All tasks are single-turn text classification or generation.

## 9. Key numbers
- Total dataset size: ~6,882 instances (6.9K in Table 1) (p.2)
- Source pairs after filtering: 2,294 (p.5)
- Train/val/test: 5,505/687/690 (p.5)
- Gwet's AC1 inter-annotator agreement: 0.7408, p < 0.001 (p.5)
- XLM-R robustness gap: 41.40pp (Toxic F1=95.06, Obfus F1=53.66) (p.6)
- RoBERTa robustness gap: 21.88pp (p.6)
- Fine-tuning reduces gap by up to 34.67pp (p.7)
- Human deobfuscation BERTScore: ~95.6 avg vs. Qwen2.5 fine-tuned 77.9 (17.75pp gap) (p.8)
- Human chrF: ~82.1 vs. Qwen2.5 36.32 (45.81pp gap) (p.8)
- Wild dataset (144 reviews): slightly lower performance than KOTOX but consistent trends (p.8)
- 17 transformation rules across 5 categories (p.4)
- 144 real-world obfuscated instances analyzed by 2 Korean experts to define taxonomy (p.4)

## 10. Pitfalls & limitations
Author-admitted:
- Korean-only; rules may not generalize to other languages (p.9)
- Transformation rules are manually defined and may not cover all real-world evasion patterns
- Perspective API used for toxicity evaluation may not accurately handle Korean text

Additional observations:
- Algorithmic rule application may produce less naturalistic obfuscations than real user-generated content, even with wild dataset validation
- The 10-item filtering rubric details are in Appendix (Table 17) but not reproduced; rubric quality not independently verified
- No evaluation of model behavior on multi-rule compositions beyond k=4
- Classification LMs (HateBERT, RoBERTa) were not trained on Korean data, making them poor baselines; XLM-R is the more relevant encoder comparison

## 11. Novel ideas worth stealing
1. **Linguistically-grounded obfuscation taxonomy**: Deriving transformation rules from systematic linguistic analysis (phonology, orthography, morphology) rather than ad hoc perturbations produces more principled and comprehensive coverage. This approach could be applied to build evasion-robustness benchmarks for values-alignment in non-English languages.
2. **Quadruple structure**: (neutral, toxic, obfuscated-neutral, obfuscated-toxic) enables multiple tasks from a single dataset and allows controlled ablation of obfuscation effects independent of toxicity.
3. **Wild data validation**: Comparing benchmark performance to real-world collected examples (144 Agoda/Google Maps reviews) is a lightweight ecological validity check that more benchmark papers should include.
4. **Rule-level error analysis**: Measuring per-rule classification error rates reveals which evasion strategies are hardest for models, directly informing where to invest robustness improvements.
5. **Human vs. LLM deobfuscation baseline**: The 17.75pp BERTScore gap between native speakers and fine-tuned LLMs is a principled target for model improvement, analogous to human-LLM gaps in other benchmark domains.

## 12. Notable quotes
"Models trained exclusively on Ours set achieve higher performance on the Toxic evaluation set than models trained only on the Toxic set. Moreover, the performance gap between the Ours and Toxic evaluations decrease by up to 34.67%p." (p.7)

"Rule 15 corresponds to the spacing perturbation rule and shows the highest error ratio. Although spacing changes do not significantly affect human understanding of the original meaning, they severely impact LMs because the models process text at the token level." (p.7-8)

"These findings indicate that current LLMs still have limited understanding of obfuscated Korean text, making them highly vulnerable to obfuscated toxic content." (p.8)

"KOTOX is the first high-quality paired dataset of obfuscated Korean toxic text." (p.2)

## 13. UNKNOWN / not in extract
- Full 10-item annotation rubric (Table 17 referenced but in Appendix, not extracted)
- Complete Appendix B (examples for all 17 rules beyond the first few categories)
- Appendix C (detailed dataset statistics and split methodology)
- Appendix D (LoRA fine-tuning configurations)
- Figure 11 (rule correlation matrix)
- Figure 5 (sanitization results visualization referenced but not shown in extract)
- License terms for KOTOX dataset release
- Exact number of parameters for all models used
