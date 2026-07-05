---
stem: "Meta AI-Llama_Guard_2312.06674"
company: "Meta AI"
reader_model: "sonnet"
confidence: "high"
theme_tags: [ai-lab-practices, llm-judges-scoring, best-practices, validity-psychometrics]
headline_numbers:
  - "Llama Guard achieves AUPRC 0.945 on own test set (prompt classification), vs. OpenAI API 0.764 (p.7)"
  - "Llama Guard achieves AUPRC 0.626 on ToxicChat in zero-shot, outperforming all baselines (p.7)"
  - "Few-shot Llama Guard (AUPRC 0.872) outperforms OpenAI Mod API (0.856) on OpenAI's own dataset (p.8)"
  - "Training dataset: 13,997 labeled prompt-response pairs across 6 harm categories (p.4)"
  - "Llama Guard needs only 20% of ToxicChat data to match Llama2-7b trained on 100% (p.9)"
  - "Fine-tuning: 500 steps (~1 epoch) on 8xA100 80GB GPUs (p.4)"
---

## 1. Gist

Llama Guard is an LLM-based input-output safeguard model from Meta AI for classifying safety risks in human-AI conversations. Built on Llama2-7B and instruction-tuned on a custom 6-category safety taxonomy, it performs both prompt classification (user inputs) and response classification (model outputs) as separate tasks using the same model via instruction following. Unlike fixed-taxonomy content moderation APIs, Llama Guard accepts the taxonomy as model input, enabling zero-shot and few-shot adaptation to novel policies without fine-tuning. The paper introduces a reusable evaluation framework for comparing moderation systems under policy mismatch conditions.

## 2. Alignment/values methods used

- **Supervised fine-tuning (SFT) on safety classification**: Llama2-7B is instruction-tuned to perform binary safe/unsafe classification with multi-label category identification (p.3–4).
- **Instruction-following framework**: Safety assessment is framed as an instruction-following task; the guidelines, classification type (prompt vs. response), conversation, and output format are all passed as input (p.3).
- **Data augmentation for policy generalization**: (1) Random dropping of non-violated categories from prompt; (2) dropping all violated categories while changing label to "safe" — teaches category-level independence (p.4).
- **Zero-shot and few-shot prompting for policy adaptation**: Novel taxonomies can be injected at inference time via 2–4 in-context examples per category, achieving adaptation without retraining (p.3, p.8).

## 3. Values specification

Llama Guard operationalizes values through an explicit, customizable **safety risk taxonomy** rather than a broad policy document:
- **Violence & Hate**: Statements encouraging violence or discrimination based on protected characteristics (p.2)
- **Sexual Content**: Statements encouraging sex acts (including potentially with minors), or sexually explicit content (p.3)
- **Guns & Illegal Weapons**: Acquisition, creation, or use of illegal weapons including biological/chemical agents (p.3)
- **Regulated or Controlled Substances**: Illegal production, transfer, or consumption of drugs, tobacco, alcohol, cannabis (p.3)
- **Suicide & Self Harm**: Instructions for self-harm; any response to self-harm intent that doesn't link to health resources (p.3)
- **Criminal Planning**: Miscellaneous criminal activities not covered by other categories (p.3)

The taxonomy is explicitly described as a **sample taxonomy** intended to be broadly applicable, not a comprehensive measure of all risks (p.2). The instruction-tuning approach allows users to supply their own taxonomy at inference time.

## 4. Safety & values evaluation methodology

- **AUPRC (Area Under Precision-Recall Curve)** as primary metric; selected because it focuses on performance on the positive ("unsafe") class and is useful for threshold selection (p.7).
- **In-domain vs. off-policy evaluation**: Evaluates on own test set (in-policy) and on external benchmarks with different taxonomies (off-policy) (p.5–6).
- **Three off-policy evaluation strategies**: (1) Overall binary classification using max score across all categories; (2) per-category 1-vs-all (includes cross-category misclassifications as errors); (3) per-category 1-vs-benign (drops hard negatives from other categories, producing optimistic estimates for fixed-output APIs) (p.5–6).
- **Expert in-house red team annotation**: 13,997 prompt-response pairs labeled by in-house red teamers for 4 labels: prompt-category, response-category, prompt-label, response-label. 3:1 train/eval split (p.4).
- **Baselines**: OpenAI Moderation API, Perspective API, Azure AI Content Safety API, GPT-4 zero-shot (p.7).
- **External benchmarks**: ToxicChat (10K samples from real user-AI interactions) and OpenAI Moderation Evaluation Dataset (1,680 prompts) (p.6–7).

## 5. Benchmarks used or introduced

- **ToxicChat (Lin et al., 2023)**: 10K samples for content moderation in real-world user-AI interactions; labels determined by strict majority vote (≥3 annotators) (p.6)
- **OpenAI Moderation Evaluation Dataset (Markov et al., 2023)**: 1,680 prompts labeled across OpenAI moderation API taxonomy (p.7)
- **Llama Guard internal test set**: 3,499 labeled examples (25% of the 13,997 total); in-policy evaluation; not publicly released as a standalone benchmark (p.4)

## 6. Agentic / multiturn evaluation aspects

Llama Guard explicitly supports multi-turn conversations: "A conversation may be single-turn, with a single user message followed by a single agent response, or multi-turn" (p.3). The same model handles both configurations via the instruction-following framework. The paper is notably the **first** to distinguish between prompt classification and response classification as separate content moderation tasks, rather than treating the full conversation as a single unit (p.3). In practice, the model receives the conversation history up to the relevant turn. No specific multi-turn jailbreak robustness evaluation is reported, however.

## 7. Key numbers

- Training set: 13,997 prompt-response pairs; 3:1 train/eval split (p.4)
- Training: 500 steps (~1 epoch), 8xA100 80GB GPUs, batch size 2, seq length 4096, lr 2×10^-6 (p.4)
- Category counts (training prompts): Criminal Planning 3,915; Safe 7,228; Violence & Hate 1,750; Substances 566; Sexual Content 283; Guns 166; Self-Harm 89 (p.4)
- AUPRC own test set: Llama Guard prompt 0.945, response 0.953; OpenAI API 0.764/0.769; Perspective 0.728/0.699 (p.7)
- AUPRC ToxicChat (zero-shot): Llama Guard 0.626; OpenAI API 0.588; Perspective 0.532 (p.7)
- AUPRC OpenAI Mod dataset: Llama Guard few-shot 0.872 vs. OpenAI API 0.856 (p.8)
- Fine-tuning efficiency: Llama Guard needs only 20% of ToxicChat data to match Llama2-7b at 100% (p.9)
- Llama2-7b zero-shot AUPRC on ToxicChat: 0.000 (produces malformed outputs) vs. Llama Guard 0.626 (p.9)
- F1 overall (prompt): Llama Guard 0.872; OpenAI API 0.389; Azure 0.623; Perspective 0.346; GPT-4 0.816 (p.14)
- F1 overall (response): Llama Guard 0.884; GPT-4 0.801; Azure 0.644; OpenAI API 0.478; Perspective 0.373 (p.15)

## 8. Findings relevant to values-benchmark design

1. **Taxonomy incompatibility is the primary challenge for cross-system evaluation**: Different systems use incompatible category structures (e.g., Perspective API has no self-harm category; Llama Guard has no Harassment subcategory). Benchmark designers must either adopt a canonical taxonomy or accept that cross-system comparison requires the 1-vs-benign approximation with optimistic bias (p.5–6).
2. **Recall vs. precision tradeoff by category**: Criminal Planning and Regulated Substances show very high AUPRC for Llama Guard; Sexual Content and Guns categories show lower scores even for Llama Guard itself — some harm categories are inherently harder to classify. Benchmark designers should not assume equal difficulty across categories.
3. **LLM-based judges are taxonomy-agnostic**: The ability to provide guidelines as model input at inference time means LLM-based judges can be rapidly adapted to benchmark-specific taxonomies, a design principle directly applicable to automated values-alignment evaluation pipelines.
4. **Human labels slightly better than LLM labels for borderline cases**: Referenced in Llama 3 paper (p.49) and implied by annotation design; borderline prompts are specifically harder for automated annotators.
5. **Prompt vs. response are distinct classification problems**: Treating them as the same task (as traditional tools do) inflates false negatives for response-level harms and underestimates prompt-level risks. A rigorous values benchmark should separate these.
6. **Few-shot prompting enables policy adaptation at near-zero cost**: 2–4 in-context examples per category can shift a moderation model to align with a novel taxonomy without fine-tuning, implying that values benchmarks using LLM judges should include policy specification in the judge prompt.

## 9. Novel ideas worth stealing

1. **Taxonomy-as-input judge design**: Pass the evaluation rubric (taxonomy + category descriptions) directly into the judge prompt. This decouples the judge model from any single fixed policy and enables rapid iteration on benchmark taxonomy without retraining.
2. **1-vs-all per-category evaluation**: Penalizes a model for predicting the right overall binary outcome but the wrong category. This is a stricter and more informative evaluation scheme for multi-label classification benchmarks.
3. **Separate prompt and response classification tasks**: For any values benchmark evaluating conversational AI, evaluating prompt-level appropriateness and response-level appropriateness as distinct dimensions (rather than a single verdict) reveals qualitatively different failure modes.
4. **Data augmentation via category subset dropping**: Training on prompts where random subsets of non-violated categories are omitted teaches category-independence — a principle applicable to multi-dimensional values benchmarks where annotators rate subsets of dimensions.
5. **Hard negative sampling ("few-shot as hard negatives")**: Including safe examples as hard negatives in the few-shot context prevents calibration artifacts where the model always predicts the provided categories as violated.

## 10. Notable quotes

- "We draw this distinction [prompt vs. response classification] simply by change of wording in the instruction tasks for the same model, which does not require significant added effort." (p.3)
- "The absence of standardized taxonomies makes comparing different models challenging, as they were trained against different taxonomies." (p.5)
- "We find that adapting to a new policy exclusively through prompting is effective while also being low cost compared to fine-tuning." (p.8)
- "Llama Guard needs only 20% of the ToxicChat dataset to perform comparably with Llama2-7b trained on 100% of the ToxicChat dataset." (p.9)

## 11. UNKNOWN / not in extract

- Whether the red-team annotation process involved inter-rater reliability measurement
- Details on the internal Llama checkpoint used to generate responses for the training set
- Whether the taxonomy guidelines themselves were iterated or remained fixed throughout training
- How prompt injection attacks against Llama Guard itself were tested
- Performance breakdown by language (all evaluations appear to be English-only)
- Latency or throughput benchmarks for deployment as an inference-time guardrail
