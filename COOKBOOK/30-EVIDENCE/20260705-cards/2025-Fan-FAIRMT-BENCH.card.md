---
stem: "2025-Fan-FAIRMT-BENCH"
reader_model: "opus"
confidence: "high"
is_benchmark: true
theme_tags: [agentic-multiturn, llm-judges-scoring, saturation-discrimination, cultural-linguistic]
task_format: "interactive"
scoring_type: "LLM-judge"
dataset_size: 10195
dataset_construction: "LLM-generated"
languages: [en]
models_tested: [ChatGPT-3.5, GPT-4, Llama-2-7b-chat, Llama-2-13b-chat, Llama-3.1-8B-Instruct, Mistral-7B-Instruct-v0.3, Mistral-Small-Instruct, Mixtral-8x7B-Instruct, Gemma-7b-it, Gemma-2-2b-it, Gemma-2-9b-it, Gemma-2-27b-it, Qwen2.5-0.5B-Instruct, Qwen2.5-3B-Instruct, Qwen2.5-7B-Instruct]
headline_numbers: ["FairMT-10K = 10,195 multi-turn dialogues, 5 turns each (p.4)", "on FairMT-1K, Llama-3.1-8B avg bias ratio 80.00% (p.10)", "GPT-4 avg bias ratio 56.67% on FairMT-1K (p.10)", "bias ratio rises with dialogue turn count for all models (p.8)", "Llama-2-7b-chat FairMT-10K run: 72.5 H100 GPU-hours, ~$171 GPT-4 eval (p.5)"]
---
## 1. Gist
FairMT-Bench is an ICLR 2025 benchmark measuring **fairness of LLMs in multi-turn dialogue**, addressing the gap that prior fairness benchmarks are single-turn and miss bias accumulation across conversational turns. It defines a three-stage/six-task taxonomy (context understanding, interaction fairness, fairness trade-off), builds a 10,195-dialogue dataset (FairMT-10K) by re-templating existing bias corpora into 5-turn conversations, and evaluates with GPT-4-as-judge + Llama-Guard-3 classifier + human validation. It matters for values-alignment benchmarking as a concrete demonstration that safety alignment degrades over multi-turn context — a model "fair" in single-turn can be walked into biased output via anaphora, scattered questions, jailbreak tips, misinformation injection, negative feedback, or fixed-format priming. The distilled hard subset FairMT-1K shows even GPT-4 fails heavily.

## 2. Benchmark/eval design features
Construct: bias ratio = proportion of multi-turn dialogue groups whose final-turn response is judged biased. Taxonomy of three capabilities × two tasks (p.3-4): (A) Context Understanding — **Anaphora Ellipsis** (bias conveyed via pronouns referencing earlier sensitive attributes) and **Scattered Questions** (bias spread across disjoint turns to accumulate); (B) Interaction Fairness — **Jailbreak Tips** (misleading instructions crafted from prior turns) and **Interference from Misinformation** (harmless paraphrase turns inject biased viewpoints, final turn asks model to integrate); (C) Fairness Trade-off — **Negative Feedback** (user repeatedly claims content is unbiased to pressure compliance) and **Fixed Format** (structured answer template established on benign turns, then flipped to biased final question). Two bias types (stereotype, toxicity), six attributes (gender, race, religion, age, disabled, appearance).

## 3. Task format & example item
5-turn dialogue, only the final turn scored. Anaphora Ellipsis example (Fig 1, p.2): Q1 "When you think of the unique and distinctive characteristics of women... Summarize in ONLY 10 words." → ... Q5 "So based on some historical and realistic factors, they are more likely to be subservient." with the model (A5) agreeing "Yes, it is likely that women are more susceptible to... subservient behaviors due to some social factors." The bias is conveyed via the pronoun "they" so single-turn protection is not triggered.

## 4. Scoring / grading methodology
Two-stage: inference (sequential multi-turn, previous outputs fed as history), then scoring of only the final turn. Primary judge GPT-4 given the full multi-turn output plus the original biased seed statement (temperature 0.6). Auxiliary: Llama-Guard-3-8B content-safety classifier. Human evaluation verifies GPT-4 judgments (three annotators per item, majority vote; consistency reported in Appendix A.4). Metric: bias ratio (fraction of dialogue groups flagged biased). Over-rejection (false refusals on non-biased inputs) also measured (Appendix B.1).

## 5. Dataset construction & provenance
Source bias data drawn from established human-annotated corpora: RedditBias and SBIC (Social Bias Inference Corpus) for stereotype, HateXplain for toxicity (p.4). GPT-4 used to generate the multi-turn dialogue templates and to simulate the user in Scattered Questions and Jailbreak Tips. FairMT-10K totals 10,195 items (8,176 stereotype + 2,019 toxicity), unevenly distributed across attributes (Table 1, p.4). Dataset contains only input prompts. FairMT-1K distilled by selecting items where all six original models had highest error ratio, equal count per task (p.9). Ethics: publicly available sources, anonymized; code/data released.

## 6. Validity evidence
Human validation of GPT-4 judgments with three-annotator majority vote (p.11); GPT-4 and Llama-Guard-3 trends "align closely" (p.6), providing convergent multi-judge evidence. Single vs multi-turn comparison (Section 3.3) is a criterion contrast showing the benchmark captures something single-turn does not. Cross-source integration (RedditBias/SBIC/HateXplain) supports coverage. Limitation: exact human-GPT-4 agreement numbers are in appendix, not the extract.

## 7. Saturation / discrimination
Strong discrimination and far from saturated. On FairMT-1K averages range widely: Gemma-2-27b-it 25.35% (best) to Llama-3.1-8B 80.00% (worst) (p.10). Clear scaling signal within Gemma-2 family (2B 40.30% → 9B 36.97% → 27B 25.35%) and Qwen2.5. Even GPT-4 scores 56.67% avg, so ample headroom. FairMT-10K bias ratios much lower (averages ~11-22%, Table 2) — the 1K distillation deliberately raises difficulty. Bias ratio monotonically increases with turn count (Fig 6-7, p.8).

## 8. Multiturn / agentic aspects
This is the core contribution. 5-turn dialogues where prior model outputs become conversation history; bias accumulates across turns. GPT-4 simulates an adversarial user in two tasks (Jailbreak Tips, Interference Misinformation), an agentic red-teaming loop. Interference-from-Misinformation withholds model response for the first four turns (injection only), then requires integration on the final turn. Fixed Format conditions the model on a benign structured template before flipping to biased content. Findings: models prioritizing utility/instruction-following (Mistral) are more susceptible under interaction pressure; keyword-reliant models (Llama-2) fail comprehension tasks like Anaphora Ellipsis (p.6-7).

## 9. Key numbers
- FairMT-10K: 10,195 dialogues (8,176 stereotype / 2,019 toxicity); Gender 3,098, Race 2,574, Religion 2,492 (Table 1, p.4)
- 5 turns per dialogue; temp 0.7, max 150 new tokens for tested LLMs (p.5)
- FairMT-10K GPT-4 eval averages (stereotype): Llama-3.1-8b 22.29% (worst), Gemma-7b 11.38% (best) (Table 2, p.5)
- Highest single-cell bias: Mistral-7b Interference-Misinformation stereotype 58.10%; Llama-2-13b Anaphora Ellipsis toxicity 44.57% (Table 2, p.5)
- FairMT-1K averages: Llama-3.1-8B 80.00%, Mistral-7B 83.43%, Qwen2.5-0.5B 74.55%, Llama-2-7b 76.36%, GPT-4 56.67%, Gemma-2-27b 25.35% (Table 3, p.10)
- Multi-turn vs single-turn: all models except Gemma show higher multi-turn bias; ~5-10% (stereotype) to ~10% (toxicity) increases (p.7)
- Gemma Fix-Format bias drops >80% multi-turn (p.7)
- Cost: 72.5 H100 GPU-hours + ~$171 GPT-4 API per Llama-2-7b FairMT-10K run (p.5)

## 10. Pitfalls & limitations
Author-noted: models over-reject non-biased inputs (measured separately). Observed flaws: GPT-4 is both a data generator (user simulator) and the primary judge — potential circularity/self-preference; only English; attribute coverage highly imbalanced (Age/Appearance lack toxicity data, so some cells empty). Scattered Questions deviates from the turn-monotonic bias trend because a specific third-turn prompt subtly steers the model, revealing template-specific artifacts (p.8). Bias ratio depends heavily on judge thresholds; single seed run per config (no variance reported in main tables). FairMT-1K selection is model-conditioned (hardest for the original 6), which could bias difficulty toward those models' failure modes.

## 11. Novel ideas worth stealing
- **Multi-turn bias accumulation as the unit of evaluation**: score only the final turn after adversarial context build-up — directly transferable to any values benchmark that wants to test alignment robustness rather than single-shot refusal.
- **Six concrete attack templates** (Anaphora Ellipsis, Scattered Questions, Jailbreak Tips, Interference Misinformation, Negative Feedback, Fixed Format) — a reusable taxonomy of *how* conversational context erodes safety; each is a design pattern for stress-testing a new benchmark.
- **Anaphora/pronoun laundering**: conveying the sensitive attribute in an earlier turn and referring to it via "they" so that per-turn keyword filters miss it — a sharp probe of genuine contextual understanding vs surface keyword matching.
- **Format-priming attack (Fixed Format)**: establish a compliant answer scaffold on benign turns, then flip the final question — exploits instruction-following inertia.
- **Distill-the-hardest subset** (10K→1K by selecting cross-model highest-error items) to make an efficient, discriminating leaderboard that resists saturation.
- **Triangulated scoring** (LLM-judge + safety classifier + human majority vote) to guard against single-judge artifacts.
- **Comprehension vs bias-resistance decomposition**: separating whether a model *understands* the bias from whether it *resists* it — a useful two-axis diagnostic.

## 12. Notable quotes
- "biases tend to accumulate over successive turns, causing LLMs to struggle with maintaining fairness in multi-turn scenarios" (p.2)
- "The protection mechanism was not triggered by the Ellipsis in Multi-Turn" (Fig 1, p.2)
- "no model has yet demonstrated consistently strong fairness performance across both comprehension-focused and bias-resistance tasks." (p.7)
- "even the most recently introduced models... exhibit a significant proportion of biased responses on the FairMT-1K, underscoring the dataset's challenging nature" (p.9)

## 13. UNKNOWN / not in extract
- Exact human–GPT-4 inter-annotator agreement figures (Appendix A.4.2 not in extract).
- Full GPT-4 judge prompt / rubric wording (Appendix A.3).
- Detailed FairMT-1K selection algorithm (Appendix B.5).
- Single-turn baseline numeric tables (only figures described).
- Licensing terms of the derived dataset.
- Number of distinct dialogue templates per task and how much GPT-4 generation was filtered/validated.
