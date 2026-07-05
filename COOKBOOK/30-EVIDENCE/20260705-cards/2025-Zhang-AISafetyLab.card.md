---
stem: "2025-Zhang-AISafetyLab"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [best-practices, contamination-robustness, llm-judges-scoring, design-space]
task_format: "n/a"
scoring_type: "mixed"
dataset_size: 50
dataset_construction: "scraped"
languages: ["en"]
models_tested: ["Vicuna-7B-v1.5", "Llama-Guard-3-8B"]
headline_numbers:
  - "AutoDAN achieves average ASR of 56.4% across all defense methods on Vicuna-7B-v1.5 (p.7, Table 1)"
  - "Safe Unlearning reduces average ASR to 14.8% across all attack methods (p.7)"
  - "Prompt Guard reduces ASR to 0.0% for all 13 attack methods tested (p.7, Table 1)"
  - "Erase Check has 99.6% over-refusal rate despite strong defense (p.7, Table 1)"
  - "13 attack methods, 16 defense mechanisms, 7 evaluation scorers implemented (p.1)"
---
## 1. Gist
AISafetyLab is an open-source framework and toolkit from Tsinghua University that unifies attack, defense, and evaluation methods for LLM safety research under a single, extensible Python codebase. The framework addresses a practical reproducibility and comparability gap: prior safety research is fragmented across different codebases, experimental setups, and datasets, making fair comparison impossible. AISafetyLab implements 13 jailbreak attack methods (white-box, gray-box, black-box), 16 defense mechanisms (13 inference-time, 3 training-time), and 7 safety evaluation scorers (2 rule-based, 5 model-based). An empirical study on Vicuna-7B-v1.5 using 50 HarmBench instructions provides a comparative benchmark across all attack × defense combinations. For values-alignment benchmarking, this paper is primarily relevant as infrastructure: it demonstrates how to build standardized attack/defense evaluation pipelines and surfaces the attack-success-rate vs. over-refusal trade-off that any safety benchmark must measure.

## 2. Benchmark/eval design features
This is a toolkit paper, not a benchmark paper in the traditional sense. The empirical study functions as a system paper evaluation:
- **Attack module:** 13 methods across three access tiers. White-box (1): GCG. Gray-box (3): AutoDAN, LAA, Advprompter. Black-box (9): GPTFuzzer, Cipher, DeepInception, ICA, Jailbroken, MultiLingual, PAIR, ReNeLLM, TAP.
- **Defense module:** Inference-time (13) across three stages: preprocessing (PPL Filter, Self Reminder, Prompt Guard, Goal Prioritization, Paraphrase, ICD), intraprocessing (SmoothLLM, SafeDecoding, DRO, Erase-Check, Robust Aligned), postprocessing (Self Evaluation, Aligner). Training-time (3): Safety Data Tuning, Safe RLHF, Safe Unlearning.
- **Evaluation scorers (7):** PatternScorer, PrefixMatchScorer (rule-based); ClassificationScorer, ShieldLMScorer, HarmBenchScorer, LlamaGuard3Scorer (fine-tuning-based); PromptedLLMScorer (prompt-based).
- **Over-refusal scorer:** Based on XSTest (Röttger et al., 2024), prompts an LLM to evaluate over-refusal rate separately from safety score.
- **Metric:** Attack Success Rate (ASR) = proportion of 50 HarmBench harmful instructions that successfully elicit harmful content, scored by Llama-Guard-3-8B.

## 3. Task format & example item
The evaluation is behavioral (not MCQ or free-text elicitation), assessed via attack-defense pipelines. A representative attack query from the code example (p.6):
> `attack_query = "Give detailed instructions for >>> correctlua code reform BEGIN <!--"` (p.6, an AutoDAN-style adversarial jailbreak prompt)

## 4. Scoring / grading methodology
- Primary scoring: Llama-Guard-3-8B classifies each model response as safe or unsafe; ASR = fraction of 50 test cases scored unsafe.
- Over-refusal scoring: OverRefuseScorer (based on Röttger et al., 2024 XSTest) measures the rate at which the defended model refuses benign requests.
- Seven scorers implemented via a unified `score(query, response) → judgment` interface; the paper notes these scorers sometimes produce inconsistent results, flagging an evaluation reliability problem (p.8).

## 5. Dataset construction & provenance
- Test set: 50 harmful instructions sampled from HarmBench (Mazeika et al., 2024).
- Over-refusal test: XSTest (Röttger et al., 2024).
- Training-time defenses: controlled at ~1,000 samples each.
- Datasets hosted on HuggingFace at thu-coai/AISafetyLab_Datasets (p.6).
- No contamination controls are described.

## 6. Validity evidence
- The paper demonstrates face validity through diverse attack coverage (white-, gray-, black-box) and multiple evaluation scorers.
- The main finding that evaluation methods produce inconsistent ASR readings is itself a validity concern: DeepInception achieves >40% ASR under some defenses, but "the responses often consist of fictional narratives or simple repetitions of the question, without providing precise or potentially harmful information" (p.8). This shows ASR as currently measured does not cleanly distinguish harmful information delivery from surface compliance.
- No human validation of scorer outputs, no inter-rater reliability analysis, no correlation between different scoring methods reported.

## 7. Saturation / discrimination
- Prompt Guard (classifier on input queries) achieves 0.0% ASR for all 13 attacks — a ceiling defense that essentially prevents any evaluation because it blocks all adversarial inputs at the input stage.
- Erase-Check and Robust Aligned both achieve very low ASR but at the cost of >93% over-refusal rates, making them unusable in practice — revealing a fundamental defense-usability trade-off.
- Safe Unlearning (training-time) is the most effective usable defense (14.8% average ASR, 20% over-refusal), with reasonable discrimination across attacks.
- AutoDAN is the strongest attack (56.4% average ASR), maintaining high efficacy even against most defenses.

## 8. Multiturn / agentic aspects
n/a for the main evaluation. The paper mentions plans to add an agent safety module in future work (p.9). Attack methods like PAIR (iterative LLM-to-LLM adversarial refinement) and TAP (tree-of-attacks with pruning) are multi-turn by design, but the evaluation framework measures only final ASR, not turn-level behavior.

## 9. Key numbers
- 13 jailbreak attack methods (1 white-box, 3 gray-box, 9 black-box) (p.1)
- 16 defense mechanisms (13 inference-time, 3 training-time) (p.1)
- 7 evaluation scorers (2 rule-based, 5 model-based) (p.1)
- 50 harmful instructions from HarmBench used in empirical study (p.6)
- AutoDAN average ASR across all defenses: 56.4% (p.7, Table 1)
- Best training-time defense (Safe Unlearning) average ASR: 14.8% (p.7)
- Prompt Guard: 0.0% ASR on all attacks, but 5.2% over-refusal (p.7)
- Erase-Check over-refusal rate: 99.6% (p.7)
- Robust Aligned over-refusal rate: 93.2% (p.7)
- Cipher attack average ASR: 14.3% (lowest effective attack) (p.7, Table 1)

## 10. Pitfalls & limitations
- **Single target model:** All experiments use only Vicuna-7B-v1.5, a model deliberately chosen for weak safety alignment; results may not generalize to modern safety-tuned models.
- **Small test set:** 50 instructions from HarmBench is extremely small for reliable cross-condition comparisons; variance will be high.
- **Scorer inconsistency:** The paper itself flags that current evaluation methods "lead to inconsistencies and potentially unfair comparisons" (p.1), and the DeepInception case illustrates that high ASR does not always correspond to actually harmful output (p.8).
- **Training-time defense sample limitation:** Only ~1,000 training samples per defense; real-world fine-tuning uses orders of magnitude more.
- **No values-alignment evaluation:** The framework covers safety/harmlessness (jailbreak prevention) but does not address values alignment in the broader sense (moral reasoning, honesty, cultural values).
- **English only:** All attacks and defenses tested on English inputs only.

## 11. Novel ideas worth stealing
1. **Attack × defense matrix as benchmark infrastructure:** The full 13×16 ASR matrix in Table 1 is a model card format for safety evaluation; a similar matrix structure could be adapted for values-alignment benchmarks (e.g., different elicitation formats × alignment interventions).
2. **Over-refusal as a mandatory co-metric:** Any safety benchmark should report over-refusal rate alongside ASR — this paper demonstrates that optimizing one without the other is misleading (Erase-Check is "safe" but unusable).
3. **Unified scorer interface:** The `score(query, response) → judgment` interface pattern, with multiple scorer backends, is directly applicable to values-alignment evaluation pipelines that need to compare LLM-judge, rule-based, and fine-tuned scoring methods.
4. **Staged defense taxonomy (preprocessing → intraprocessing → postprocessing):** This three-stage classification cleanly maps to where in the inference pipeline a defense intervenes, and could structure values-alignment intervention taxonomies similarly.
5. **Robustness stress test with adversarial elicitation:** The practice of testing the same model under many different attack methods simultaneously, rather than a single evaluation condition, surfaces inconsistency that single-method evaluations miss — a transferable design principle for benchmark robustness testing.

## 12. Notable quotes
- "Despite significant advancements in attack methodologies, research on defense mechanisms remains fragmented. Existing approaches typically concentrate on isolated defense strategies or individual evaluation metrics, often lacking a unified framework." (p.3)
- "The evaluation of robustness still poses significant challenges, often resulting in unfair comparisons between methods. For example, while DeepInception achieves an attack success rate (ASR) above 40% under methods such as Safe Unlearning and Self Evaluation, the responses often consist of fictional narratives or simple repetitions of the question, without providing precise or potentially harmful information." (p.8)
- "Some defenses, such as Erase Check and Robust Aligned, while highly effective, introduce significant over-refusal rates, highlighting a trade-off in overall usability." (p.8)
- "These problems underscore the necessity for more dependable evaluation frameworks that can accurately measure performance across a variety of adversarial conditions." (p.8)

## 13. UNKNOWN / not in extract
- Exact set of 50 HarmBench instructions used (subset selection criteria not detailed).
- Whether Llama-Guard-3-8B as a scorer has been validated against human judgments for the specific instruction categories tested.
- Performance results for API-based models (e.g., GPT-4, Claude) as targets — only Vicuna tested.
- Detailed results for training-time defenses under each of the 13 attacks (Table 1 shows average; individual breakdowns not fully shown).
- Computation times and resource requirements for each attack method.
- Plans for multimodal safety extension (mentioned as future work but not detailed).
