---
stem: "2025-Hendra-Decoding Moral Responses in AI"
reader_model: "sonnet"
confidence: "low"
is_benchmark: false
theme_tags: [moral-psychology, normative-ethics, llm-judges-scoring]
task_format: "forced-choice"
scoring_type: "behavioral"
dataset_size: null
dataset_construction: "hand-authored"
languages: ["en"]
models_tested: ["GPT-3", "GPT-3.5", "GPT-4", "GPT-4.1", "Claude 3.7", "Grok 3", "Gemini 2.5 Pro"]
headline_numbers: []
---
## 1. Gist
Hendra et al. (2025) present a quantitative comparison of 7 major LLMs on moral dilemmas, finding that LLMs tend toward utilitarian responses in impersonal dilemmas — consistent with dual-process theory predictions. The paper advocates for "AI Psychology" as a new field of inquiry. For values-alignment benchmarking, the work matters because it establishes empirical patterns of LLM moral reasoning using classical moral psychology instruments, revealing that fast (intuitive) thinking is a blind spot for current models.

## 2. Benchmark/eval design features
The study compares 7 LLMs (GPT-3, GPT-3.5, GPT-4, GPT-4.1, Claude 3.7, Grok 3, Gemini 2.5 Pro) on moral dilemmas. Key design features: (1) utilitarian vs. deontological response classification on trolley-problem-style dilemmas; (2) distinction between personal and impersonal dilemmas; (3) few-shot prompting used to simulate "slow thinking" (System 2), with zero-shot representing "fast thinking" (System 1); (4) quantitative analysis of response distributions across models. Core theoretical claim: LLMs are more utilitarian in impersonal dilemmas, matching dual-process theory predictions.

## 3. Task format & example item
Full text unavailable — specific example items cannot be confirmed. Based on the abstract, tasks are moral dilemmas (trolley-problem variants) presented as forced-choice scenarios between utilitarian and deontological responses.

## 4. Scoring / grading methodology
Behavioral scoring: LLM responses classified as utilitarian or deontological. Likely involves response parsing to extract choice, with quantitative tabulation of response distributions across models and conditions. Specific scoring rubric details unknown without full text.

## 5. Dataset construction & provenance
Likely uses established moral dilemma stimuli from the moral psychology literature (trolley problems, footbridge dilemmas, etc.). Exact dataset source, size, and item list unknown without full text.

## 6. Validity evidence
The dual-process framework provides theoretical grounding. Alignment with dual-process predictions (LLMs more utilitarian in impersonal dilemmas) provides convergent validity. Specific inter-rater reliability or psychometric validity evidence unknown without full text.

## 7. Saturation / discrimination
Unknown — full text unavailable.

## 8. Multiturn / agentic aspects
Few-shot prompting used to simulate slow/deliberate thinking (System 2 processes). Single-turn prompts with few-shot context rather than multiturn dialogue.

## 9. Key numbers
- 7 LLMs compared: GPT-3, GPT-3.5, GPT-4, GPT-4.1, Claude 3.7, Grok 3, Gemini 2.5 Pro.
- LLMs more utilitarian in impersonal dilemmas (consistent with dual-process theory).
- Few-shot = slow thinking; fast thinking is a blind spot.

## 10. Pitfalls & limitations
- Moral dilemma paradigms (trolley problems) are criticized for poor ecological validity — they probe edge cases that rarely arise in practice.
- "Utilitarian vs. deontological" binary oversimplifies actual moral reasoning.
- LLM responses to moral dilemmas may reflect training data patterns rather than anything analogous to moral cognition.
- Fast vs. slow thinking distinction in LLMs is debated — few-shot prompting may not map cleanly onto human System 1/2 processes.

## 11. Novel ideas worth stealing
- Using few-shot prompting as an operationalization of "slow/deliberate thinking" vs. zero-shot as "fast/intuitive thinking" is a reusable design move for probing depth of moral reasoning in LLMs.
- The AI Psychology framing — treating LLMs as subjects for psychological investigation using established instruments — is a productive paradigm for values benchmarking.
- Comparing personal vs. impersonal dilemma responses as a discriminator of reasoning style is a design feature worth replicating.

## 12. Notable quotes
Full text unavailable — no quotes recoverable.

## 13. UNKNOWN / not in extract
- Full text unavailable; all quantitative results, specific dilemma stimuli, and detailed methodology are unknown.
- Exact dataset size and item list.
- Statistical analysis methods and effect sizes.
- Whether results held across all 7 models or varied substantially.
- How "utilitarian" vs. "deontological" was operationalized for response coding.
