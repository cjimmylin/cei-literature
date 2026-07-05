---
stem: "2025-Kumar-UniMoral ACL 2025 Best Resource Paper"
reader_model: "opus"
confidence: "medium"
is_benchmark: true
theme_tags: [moral-psychology, cultural-linguistic, religious-values, normative-ethics]
task_format: "forced-choice"
scoring_type: "exact-match"
dataset_size: 3000
dataset_construction: "hand-authored"
languages: [Bengali, English]
models_tested: [Gemma 3 1B, Gemma 2 2B, Gemma 2 9B, Llama 3.2 1B, Llama 3.2 3B, Llama 3.1 8B, Llama 3.3 70B, Qwen2.5 14B, DeepSeek-R1-Distill-Llama 70B]
headline_numbers: ["3,000 handcrafted Bengali moral scenarios across 5 domains x 50 subtopics (p.4)", "Zero-shot accuracy spans 50-91% across models (p.3)", "Gemma 2 9B best Commonsense Acc 91.20% (MCC 0.8242) (p.4)", "Inter-annotator kappa improved 0.61 -> 0.87 after pilot calibration (p.5)"]
---
## 1. Gist
NOTE: the extract content is BengaliMoralBench (Ridoy, Wasi, Tonmoy), not "UniMoral" — the filename/stem and the paper it points to diverge (see section 13). BengaliMoralBench is the first large-scale, culturally grounded ethics benchmark for Bengali, built entirely from scratch by native annotators to test LLM moral reasoning within Bangladeshi socio-cultural contexts. It matters for values-alignment benchmarking because it operationalizes a non-Western, triadic moral framework (Virtue / Commonsense / Justice ethics) grounded in local practices (zakat, load-shedding etiquette, dowry, hijab-in-labs), and demonstrates that model scale alone does not buy culturally-competent moral judgment — pretraining coverage and alignment strategy matter more than parameter count.

## 2. Benchmark/eval design features
3,000 single-sentence scenarios, each a binary ethical(1)/unethical(0) judgment, evenly split across three ethical lenses (1,000 each): Virtue (character traits — satyata, daya, shraddha), Commonsense (samajik gyan — social norms), Justice (nyay, samata, adhikar — fairness/rights). Structured as 5 domains (Daily Activities, Habits, Parenting, Family Relationships, Religious Activities) x 10 subtopics x 20 instances (10 ethical + 10 unethical). Metrics: Accuracy, F1, Matthews Correlation Coefficient, Cohen's kappa. Evaluated zero-shot in both Bengali and English with temperature-variance and persona/context sub-studies.

## 3. Task format & example item
Binary moral classification: LLM labels a behavior scenario as Ethical or Unethical under a specified ethics type. Example subtopics: "digital payments, right vs left hand use, madrasa vs general schooling, dowry negotiations, and hijab in labs" (p.5); culturally-specific dilemmas like "load-shedding etiquette, rickshaw fare disputes, and zakat vs voluntary charity" (p.4). No full verbatim scenario sentence appears in the extract.

## 4. Scoring / grading methodology
Exact-match accuracy against human consensus labels, plus F1, MCC, and Cohen's kappa for chance-adjusted agreement (p.7). Unified zero-shot prompting protocol; models classify into the binary label space (p.3).

## 5. Dataset construction & provenance
Built from scratch to avoid train–test leakage (p.4). 30 native Bengali speakers recruited with strict residency/proficiency criteria; pilot phase of 500 cross-reviewed statements; each annotator wrote 10 ethical + 10 unethical single-sentence statements per subtopic (100/annotator, 1,000/framework, 3,000 pre-QC). Constraints: 12–25 words / <140 chars, lexically neutral (no explicit moral cues). Two-stage QC: peer review + senior adjudication on 20% sample; 94 items (3.1%) removed. 52% marked country-specific. Released on HuggingFace (ciol-research) (p.1).

## 6. Validity evidence
Inter-annotator agreement improved from kappa=0.61 to kappa=0.87 after pilot calibration and guideline refinement (p.5). Human ceiling set at 100% by construction (p.4, Table 1). Multi-annotator consensus + adjudication used to control subjectivity. Temperature-variance study (3 runs, temp 0.3/0.7) shows top models stable (std <0.5) while smaller models fluctuate up to 1.7 F1 (p.5, p.8).

## 7. Saturation / discrimination
Wide model spread (50–91% accuracy) gives strong discrimination (p.3). Justice is consistently the hardest lens (lowest MCC/kappa), Virtue the most unstable; Commonsense handled most robustly (p.8). Smaller models (Gemma 3 1B, Llama 3.2 1B) sit near chance (MCC ~0.03), so the benchmark is far from saturated for the low-capacity tier while larger models approach ceiling on Commonsense.

## 8. Multiturn / agentic aspects
n/a — single-turn zero-shot classification; no tools or multiturn interaction. Persona/context effects studied via prompt framing only (p.9).

## 9. Key numbers
- 3,000 instances, 1,000 per ethics lens, 50 subtopics, avg 18.4 words / 103 chars (p.5)
- Gemma 2 9B: Commonsense Acc 91.20 / MCC 0.8242; Justice 80.36 / 0.6513; Virtue 89.70 / 0.7947 (p.4)
- Qwen2.5 14B best on Justice: Acc 86.29, F1 86.15, MCC 0.7391 (p.7-8)
- Llama 3.2 1B near/below chance on Justice: MCC -0.0366 (p.4)
- DeepSeek-R1-Distill-Llama 70B underperforms: Justice Acc 53.99% (p.8)
- 94 items (3.1%) removed in adjudication (p.5)

## 10. Pitfalls & limitations
Author-admitted: Bangladesh-centric (may not generalize to West Bengal); binary label schema oversimplifies moral nuance; annotator/guideline framing biases; no human–model feedback loops (p.11). Observable: benchmark availability gated ("upon acceptance", p.6); 100% human ceiling is asserted, not empirically re-measured on held-out annotators; risk that majority norms are encoded at expense of marginalized voices (p.12); MCC/kappa gaps vs accuracy reveal class-imbalance sensitivity.

## 11. Novel ideas worth stealing
- Triadic culturally-situated ethics framing (Virtue/Commonsense/Justice) rather than a single normative theory — lets one benchmark surface which moral lens a model fails on (p.4).
- Balanced 10-ethical/10-unethical-per-subtopic design with lexical-neutrality constraint (no explicit moral cues) to force reasoning over surface pattern-matching (p.5) — a strong anti-shortcut control.
- "Country-specific" (CS) tagging of items (52%) enabling separation of culturally-local vs globally-shared moral content (p.5) — useful for measuring cultural-grounding gaps directly.
- Build-from-scratch provenance explicitly framed as a contamination control against web-scraped leakage (p.4).
- Prompt-language A/B (Bengali vs English) revealing that smaller models benefit from native-language prompts while larger models regress — a reusable diagnostic for English-centric representational dominance (p.9).
- Pilot-calibration-then-scale annotation pipeline with quantified kappa lift (0.61->0.87) as a reproducible quality-control template (p.5).

## 12. Notable quotes
- "even large models like Gemma-9B, while achieving high surface-level accuracy, struggle with Virtue and Justice tasks requiring deep contextual or persona-based reasoning." (p.10)
- "scaling model size alone is insufficient without rich, localized pretraining data and alignment strategies." (p.11)
- "The binary label schema (ethical/unethical) oversimplifies moral nuance, yet in practice many scenarios involve clear right-or-wrong decisions." (p.11)

## 13. UNKNOWN / not in extract
Why the stem says "UniMoral / Kumar / ACL 2025 Best Resource Paper" while the extracted PDF is "BengaliMoralBench" by Ridoy/Wasi/Tonmoy — likely a mislabeled extract/file. Full verbatim scenario examples; exact prompt templates (Appendix F); appendix subtopic-level tables (D); annotator compensation rate; final public-release license.
