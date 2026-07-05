---
stem: "2025-Dickerson-Who Gets the Kidney"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [moral-psychology, normative-ethics, validity-psychometrics, pluralism-aggregation]
task_format: "forced-choice"
scoring_type: "behavioral"
dataset_size: 40
dataset_construction: "survey-derived"
languages: ["en"]
models_tested: ["GPT-4o", "Claude-3.5-Haiku", "Gemini-1.5-Pro", "Gemini-2.0-Flash", "DeepSeek-V3", "DeepSeek-R1", "Gemma3-27B", "Llama-3.3-70B"]
headline_numbers:
  - "LLMs exhibit near-zero indecision (~0–6%) versus humans (~17%) when coin-flip option is offered (p.6)"
  - "Fine-tuning on 3,960 examples improves alignment accuracy by up to 19% (Qwen-3-14B, Strict) and 20% (Indecisive) (p.7)"
  - "LLMs deviate from humans specifically on 'number of dependents' attribute while aligning on age and drinking habits (p.4)"
  - "After fine-tuning, >60% of LLM indecision responses correspond to instances where humans are decisive (p.8)"
  - "Human non-majority-choice rate across all scenarios: 17.31%; GPT-4o: 2.98%; DeepSeek-V3: 0.83% (p.4)"
---
## 1. Gist
This paper systematically evaluates eight prominent LLMs against human moral preferences in kidney allocation decisions—a canonical high-stakes scarce-resource scenario. The central findings are two-fold: (1) LLMs deviate from human moral values in attribute prioritization, especially regarding family dependents, exhibiting near-lexicographic dominance by a single attribute rather than nuanced trade-offs; and (2) LLMs almost never express indecision even when explicitly offered a coin-flip option, in stark contrast to humans who express substantial heterogeneity. Low-rank supervised fine-tuning on small human samples improves alignment but fails to capture the true structure of human indecision. For values-alignment benchmarking, this paper demonstrates that distributional alignment (matching the full distribution of human choices, including uncertainty) is a richer target than mere majority-preference alignment, and that LLM determinism is itself a form of misalignment.

## 2. Benchmark/eval design features
The study adapts two pre-existing human-subject datasets from McElfresh et al. and Freedman et al. on kidney allocation. Two experimental designs are used:

**Experiment 1 (Single-attribute and multi-attribute alignment):** 14 pairwise scenarios with triplet patient profiles (age, drinking habits, family dependents). 9 scenarios vary one attribute; 5 involve multi-attribute trade-offs. Human data: ~289 respondents, 28 pairwise comparisons each. LLM: 30 agents per model.

**Experiment 2 (Indecision modeling):** Same 14 scenarios with an added coin-flip option. Four additional indecision framings are tested: "Both deserve," "Neither deserves," "Too similar," "Need more information."

**Experiment 3 (Fine-tuning):** 132 human subjects × 40 instances; first 30 used for training, last 10 for testing. Four open-source LLMs fine-tuned with LoRA. Performance measured as accuracy of predicting individual human decisions.

## 3. Task format & example item
Forced-choice pairwise comparison with optional indecision. Patient profiles are triplets: age ∈ {18, 32, 55, 90}, drinks/day ∈ {0, 1, 2}, family dependents ∈ {0, 1, 2} (Experiment 1). Multi-attribute version (Experiment 2) uses binary attributes: Age (Young/Old), Drinking (Rare/Frequent), Health (Healthy/Cancer).

Example item (paraphrased from p.3): "Patient A is 32 years old, drinks 1 unit/day, has 2 dependents. Patient B is 55 years old, drinks 0 units/day, has 0 dependents. Who should receive the kidney? (A / B / Flip a coin)"

## 4. Scoring / grading methodology
Two metrics are used:
- **Win-rate**: percentage of LLM (or human) agents choosing each patient per scenario.
- **Alignment accuracy** (fine-tuning): fraction of LLM responses matching individual human decisions on held-out test items.
- **Clarity** (Table 1, p.4): percentage of responses that deviate from the majority choice — used as an inverse measure of determinism.
Statistical comparison of indecision rates uses Welch's T-test. Fisher's exact test and chi-square tests are referenced in appendix analyses.

## 5. Dataset construction & provenance
Primary datasets adapted from McElfresh et al. [42] (132 subjects, 40 instances each = 5,280 human responses for fine-tuning) and Freedman et al. [17] (289 subjects, 28 pairwise comparisons). Both datasets originate from academic human-subject studies on kidney allocation. The scenarios are synthetic (not real clinical cases). Fine-tuning uses a 30/10 split per subject. No explicit licensing or public release of LLM response data is described, but the original human data sources are cited.

## 6. Validity evidence
Face validity is strong: kidney allocation is a recognized ethical decision domain from the computational social choice literature. Human baseline data from prior published studies provides an external standard. Sensitivity analyses test memory-less prompting, shuffled orders, and position swapping (Appendix A). Temperature sensitivity is also analyzed (Appendix A.2). The Welch's T-test confirms that LLMs' lower indecision rates are statistically significant versus humans at p < 0.05 for every model (p.6). Social-choice-theoretic Kemeny-Young analysis is used to derive preference orderings (Appendix G).

## 7. Saturation / discrimination
The task discriminates well at the distributional level: humans show 17.31% non-majority choices while most LLMs are below 5%, revealing a clear gap. For multi-attribute trade-offs, LLMs and humans diverge on priority ordering (drinking habits vs. age), demonstrating item-level discrimination. The coin-flip indecision option effectively surfaces the determinism gap. The small number of scenarios (14–28) limits breadth but is sufficient for the authors' analytical goals.

## 8. Multiturn / agentic aspects
Chat history (memory) is maintained across the sequence of 14 allocation prompts within a session to mirror the human study protocol. This is a minimal multiturn design—not agentic. Each instance is a separate prompt in a running conversation. The authors test memory-less alternatives in Appendix A and find it affects results, though the memory condition is primary.

## 9. Key numbers
- 8 LLMs evaluated in main alignment experiment (p.3)
- 14 pairwise scenarios in Experiment 1; 28 in Experiment 2 (pp.3–5)
- ~289 human respondents for Experiment 2 multi-attribute (p.5)
- 132 human subjects for fine-tuning; 3,960 training examples (pp.7–8)
- Human non-majority response rate: 17.31%; GPT-4o: 2.98%; DeepSeek-V3: 0.83%; Gemma3-27B: 1.19% (p.4)
- Fine-tuning accuracy gains: Gemma-3-4B +15%, Llama-3.1-8B +17%, Qwen-3-14B +19% (Strict); Qwen-3-14B +20% (Indecisive) (p.8)
- >60% of post-fine-tuning LLM indecision responses occur where humans were decisive (p.8)
- >75% of human indecision instances are not matched by LLM indecision post-fine-tuning (p.8)
- Claude-3.5-H expressed the most LLM indecision among pretrained models, still substantially below humans (p.6)

## 10. Pitfalls & limitations
- Synthetic scenarios do not map directly to real clinical kidney allocation decisions (p.9).
- Only a narrow slice of moral attributes (age, drinking, dependents, health) is tested; real-world allocation involves many more factors.
- Fine-tuning uses small open-source models (up to 27B); results may not hold for larger frontier models.
- Indecision training overshoots: LLMs learn to express indecision on decisive cases and remain decisive on genuinely ambiguous cases.
- Human data comes from prior studies with specific demographic profiles (Western, English-speaking); cultural generalizability is not tested.
- Memory across scenarios introduces potential order effects; while sensitivity analyses are conducted, this is an acknowledged complexity.
- The study focuses on binary forced-choice allocation; real decisions involve continuous preference gradients.

## 11. Novel ideas worth stealing
- **Indecision as an alignment target**: explicitly including a "flip a coin" option and measuring whether AI matches human uncertainty rates is a powerful diagnostic. Values benchmarks should measure distributional alignment, not just mode/majority alignment.
- **Multiple indecision framings**: testing four different wordings of the indecision option ("Both deserve," "Neither deserves," "Too similar," "Need more information") reveals how sensitive LLM behavior is to prompt framing. New benchmarks could include parallel-framing reliability checks.
- **Social-choice-theoretic preference recovery**: using pairwise comparison win rates to reconstruct a full preference ordering (via Kemeny-Young) is a rigorous way to characterize implicit value functions from behavioral data.
- **Determinism as a diagnostic**: measuring the variance or entropy of LLM responses across repeated trials on identical moral dilemmas reveals whether a model is lexicographically dominated by one attribute — a form of misalignment distinct from wrong average preference.
- **Fine-tuning alignment ceiling**: comparing fine-tuned LLMs to MLP/decision-tree baselines (which achieve similar or better performance) reveals how much of human decision-making is captured by simple feature functions vs. richer reasoning.
- **Attribute dominance detection**: the method of holding two attributes constant while varying a third cleanly isolates single-attribute preferences. This could be used in any multi-dimensional values-alignment benchmark to diagnose lexicographic AI reasoning.

## 12. Notable quotes
- "LLMs more often resolve moral queries with a single, deterministic choice. This determinism in responses can lead to systematic misalignment of AI models with human judgment and fail to capture the plurality inherent in moral values." (p.4)
- "While humans generally prioritize age over drinking habits, they may still choose an older patient if the younger alternative is a frequent drinker with a severe health condition." (p.5)
- "Human judgments on moral dilemmas are inherently variable—a desirable feature in ethical questions that rarely admit objectively 'correct' answers." (p.6)
- "Can we develop or fine-tune models that accurately reflect the cultural norms and ethical judgments of their intended users? Moreover, should these systems be calibrated to emphasize the individualistic ideals prevalent in many Western societies, or should they instead adopt a more collectivist perspective?" (p.9)

## 13. UNKNOWN / not in extract
- Full prompt text for kidney allocation scenarios (Appendix F mentioned but not reproduced in extract)
- Complete Kemeny-Young pairwise election results (Appendix G)
- Full fine-tuning hyperparameter details (Appendix D)
- Memory-less vs. memory sensitivity analysis results (Appendix A)
- Position-swap and order-shuffle sensitivity results (Appendix A)
- Temperature sensitivity analysis results (Appendix A.2)
- Demographic details of the 132/289 human respondents
- Licensing and public availability of the LLM response dataset
