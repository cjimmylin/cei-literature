---
stem: "2025-Wei-MedEthicsQA"
reader_model: "opus"
confidence: "high"
is_benchmark: true
theme_tags: [normative-ethics, saturation-discrimination, llm-judges-scoring, best-practices]
task_format: "mixed"
scoring_type: "mixed"
dataset_size: 10974
dataset_construction: "mixed"
languages: [en]
models_tested: [GPT-4o, GPT-4o-mini, o1-mini, Qwen-plus, Llama2-7b, Llama2-13b, Llama2-70b, Llama3-8b, Llama3-70b, Llama3.1-8b, Llama3.1-70b, Aloe-8b-alpha, Aloe-8b-beta, Aloe-70b, Med42-8b, Med42-70b, Meditron3-8b, Meditron3-70b, Huatuo-o1-8b, Huatuo-o1-70b]
headline_numbers: ["5,623 MCQ + 5,351 open-ended = 10,974 total questions (p.1)", "Expert-validated error rate 2.72% (p.4)", "Average Ethics Score 55.5 across models (p.4)", "MedLLMs degrade ~4.4% RS / 4.0% MCQ vs foundation models (p.4)", "GPT-4o best ES = 64.5 (p.4)", "<2% ethics-related samples in existing medical benchmarks (p.2)"]
---
## 1. Gist
MedEthicsQA is a large medical-ethics QA benchmark (10,974 items: 5,623 MCQs + 5,351 open-ended) built to test whether medical LLMs (MedLLMs) actually behave ethically under the four Beauchamp pillar principles (beneficence, non-maleficence, autonomy, justice). Its headline finding for values-alignment is a "fine-tuning tax": domain-adapting a base model on medical knowledge *reduces* medical-ethics performance (~4.4% relative on open-ended, ~4% MCQ accuracy) even though it improves medical-knowledge scores. This directly demonstrates that capability alignment and values alignment can trade off, and that ethics evaluation must be a separate axis from knowledge evaluation. It also documents that existing medical benchmarks contain <2% ethics-relevant items, motivating a dedicated ethics eval.

## 2. Benchmark/eval design features
Constructs: the four pillar principles of biomedical ethics, operationalized through a hierarchical taxonomy 4P-26C-256G (4 Pillars → 26 categories → 256 detailed guidelines) built from authoritative codes of conduct across six continents (p.2, p.7). Two answer spaces: (1) closed MCQ (A–E, accuracy), (2) open-ended free-text scored against a reference-answer checklist. Overall metric Ethics Score ES = (Acc + RS)/2 (p.4). Categories split patient-centered vs physician-centered vs others; distribution is long-tailed toward patient-centered items (p.3).

## 3. Task format & example item
MCQ (contextualized medical-ethics questions collected/filtered from medical QA banks) and open-ended questions synthesized from PubMed ethics literature. Verbatim example items are referenced in Figure 9 (question examples) and Figure 8 (synthesis example) but the figure text is not transcribed in the extract; a full verbatim item is not available. (See p.3, Figure 9.) Answer-index distribution randomized to avoid position bias: A 25.1%, B 25.3%, C 24.4%, D 23.4%, E 1.8% (p.9).

## 4. Scoring / grading methodology
MCQ: accuracy vs gold answer. Open-ended: checklist-based LLM-as-Judge (following HelloBench/Que et al.). Each key point in the reference answer is a checklist item; one point awarded if the model addresses it; Relative Score RS(%) = points obtained / total points (p.4). Rater = GPT-4o-mini. LLM-judge reliability was itself validated by humans assessing "Reasonable Rate" over 200 sampled <question, reference, response, rating> tuples (100 MedLLM + 100 else) (p.9).

## 5. Dataset construction & provenance
MCQs: 29k candidates gathered via ethics-keyword search from MedMCQA, MedQA, PubMedQA, MMLU, CAREQA and online banks (Medbullets, Amboss, Quizlet, Lecturio, ProProfs), then (a) 3-model consensus classification (GPT-4o-mini, Deepseek-v3, Qwen-plus) to keep ethics items, (b) dedup via text-embedding-3 cosine >0.85, (c) drop items all small models answer correctly → 5,623 MCQs (p.2-3). Open-ended: 2.1k PubMed ethics papers → 14k pages → GPT-4o-1120 extracts reference paragraph, breaks into key-point reference answer, and generates a question; filtered for reference existence, length ≥330 words, answer-reference similarity ≥0.80 → 5,351 items (p.3). License CC BY-NC 4.0 (p.1). Human validation on 1,200 (22.4%) items; error rate 2.72% (p.3-4). English only.

## 6. Validity evidence
Content validity from continent-spanning authoritative medical codes (p.7). Human expert validation on 22.4% of data across three aspects (reference quality, Q-A relevance, answer correctness); cross-validated error rate 2.72% (p.4). Results on validated subset match whole-set results (Figure 15), supporting reliability (p.4). LLM-as-Judge validated against human "Reasonable Rate" on 200 samples (p.9). Random baseline ~24.2% MCQ accuracy establishes chance floor (p.4).

## 7. Saturation / discrimination
Not saturated overall: average ES = 55.5 (p.4). But MCQ subset is near-ceiling for strong models — GPT-4o 91.1% accuracy (p.4), most large models 80-88%; discrimination comes mainly from open-ended RS (GPT-4o only 37.0%, average 30.9%) (p.4). Deliberate difficulty control: items all small models answered correctly were removed to avoid inflation (p.3). Weak Llama2 models near random on MCQ (49-54%) (p.4).

## 8. Multiturn / agentic aspects
n/a — single-turn QA, no tool use or interactive environment.

## 9. Key numbers
- 5,623 MCQ + 5,351 open-ended = 10,974 items (p.1, p.9)
- 4P-26C-256G taxonomy: 256 detailed principles → 26 categories → 4 pillars (p.2)
- Expert validation on 1,200 items (22.4%); error rate 2.72% (p.4)
- Ethics-related samples <2% in existing benchmarks (187/12500 = 1.49% at 1-vote) (p.2)
- Average ES 55.5; average MCQ acc 80.2/80.1; average open-ended RS 30.9 (p.4, p.10)
- GPT-4o best ES 64.5 (Acc 91.1, RS 37.0) (p.4)
- MedLLMs vs foundation: overall ↓4.0 MCQ acc, ↓4.4 RS (p.4, p.9); few-shot ↓3.3 (p.9)
- Pillar proportions: Beneficence 44.3%, Non-maleficence 32.4%, Autonomy 12.0%, Justice 11.3% (p.9)
- Answer index distribution A/B/C/D/E = 25.1/25.3/24.4/23.4/1.8% (p.9)

## 10. Pitfalls & limitations
Author-admitted: text-only (no multimodal medical VLM ethics), single language (English), and no remediation/training method offered (p.5). Reviewer-noted: MCQ subset is near-ceiling for frontier models, so most discrimination rests on the LLM-judged open-ended RS, which inherits GPT-4o-mini judge biases; open-ended items are LLM-synthesized (GPT-4o) from PubMed, risking style/circularity and contamination with model priors; "ethics" is filtered by LLM consensus classification, so the label boundary is model-defined; unequal pillar coverage (Justice/Autonomy underrepresented ~11-12%). ES = (Acc+RS)/2 mixes two very differently-scaled metrics.

## 11. Novel ideas worth stealing
- Hierarchical values taxonomy grounded in *cross-national authoritative codes* (4P-26C-256G) — a reusable pattern for building any values benchmark from real institutional documents across continents rather than a single-country source (p.2, p.7).
- "Fine-tuning tax" as a headline eval axis: always test the fine-tuned model *against its own base model* to expose values regressions hidden by capability gains (p.4). Ship a base-vs-tuned delta column.
- Difficulty calibration by removing items all weak models get right — prevents ceiling inflation and preserves discrimination (p.3).
- Dual-format (MCQ + open-ended) for the same constructs, showing that MCQ and free-text rank models differently — argues any single format is inadequate for values (p.9).
- Checklist-based LLM-judge where each reference key-point is a binary rubric item, plus human validation via "Reasonable Rate" (judging the judge's reasoning, not re-doing the task) to cut task-understanding gap (p.4, p.9).
- Answer-index randomization to defeat position bias (p.9).
- Extraction-constrained synthesis (force model to quote a real reference paragraph, filter fabricated answers by similarity) to reduce hallucination in generated items (p.3).

## 12. Notable quotes
- "medical-domain adaptation does not guarantee consistent performance superiority in medical ethics questions... it still induces an overall performance degradation (↓4.4% overall) to their foundation models." (p.4)
- "our systematic analysis reveals a critical scarcity (less than 2%, Table1) of ethics-related samples in widely-used medical benchmarks, exposing fundamental gaps in medical ethics evaluation." (p.2)
- "assessing model performance in medical ethics through a single data format (e.g., MCQs) may be inadequate, demonstrating the necessity of a multidimensional dataset." (p.9)
- "This finding suggests an asymmetry of ethical prioritization in healthcare contexts." (p.3)

## 13. UNKNOWN / not in extract
- Verbatim full text of a specific MCQ or open-ended item (only referenced as Figures 8/9, not transcribed).
- Exact inter-rater reliability statistics among human validators (only aggregate 2.72% error rate given).
- Train/test split details (benchmark is evaluation-only; no splits described).
- Precise prompt wording (in Appendix G, not in extract).
