---
stem: "2024-Tlaie-Exploring and steering the moral compass of Large"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [normative-ethics, moral-psychology, ai-lab-practices, cultural-linguistic]
task_format: "free-text"
scoring_type: "LLM-judge"
dataset_size: 7
dataset_construction: "hand-authored"
languages: ["en"]
models_tested: ["Claude-3-Sonnet", "GPT-3.5-Turbo-0613", "GPT-4-Turbo-2024-04-09", "Gemini Pro 1.5", "Gemma-2B", "Llama-2-7B", "Starling-LM-7B-Beta"]
headline_numbers:
  - "All proprietary models lean utilitarian; all open-weights models lean toward values-based (deontological) ethics (p.3)"
  - "Response consistency is low for all models (<60%) across repetitions (p.3)"
  - "All models except Llama-2 show strong liberal bias on the MFQ (p.4)"
  - "Claude-3-Sonnet is the most liberally biased model; GPT-4 best represents average US citizen (p.4)"
  - "SARA steering of Gemma-2B is most effective at early (layers 0-5) and late (layers 12-17) stages (p.6)"
  - "MFQ repeated 20 times per model to mitigate stochastic artifacts (p.3)"
---
## 1. Gist
This paper conducts a comparative moral profiling of eight state-of-the-art LLMs using two complementary instruments: a curated set of seven classical ethical dilemmas classified against eight philosophical schools, and the Moral Foundations Questionnaire (MFQ). The paper finds a systematic divide: proprietary models (Claude-3-Sonnet, GPT-3.5, GPT-4, Gemini Pro) lean utilitarian while open-weights models (Gemma, Llama-2, Starling) lean deontological/virtue-based. All models except Llama-2 display a strong liberal bias on the MFQ, aligning with the moral profile of young Western educated progressives. Beyond measurement, the paper introduces SARA (Similarity-based Activation Steering with Repulsion and Attraction), a mechanistic interpretability technique that can causally shift a model's ethical reasoning toward target philosophical schools without retraining. This work matters for values-alignment benchmarking because it (a) demonstrates that deployed LLMs have detectable and systematic moral biases, (b) shows that response consistency is low enough to undermine confident alignment claims, and (c) provides a method for causal moral intervention that could complement evaluations with direct behavioral control.

## 2. Benchmark/eval design features
Not a benchmark. Core empirical contributions are:

**Ethical dilemmas evaluation:**
- 7 dilemmas drawn from diverse philosophical traditions (Kantian, utilitarian, Hindu/Bhagavad Gita, common good, Ship of Theseus, Ubuntu/African, Bali sustainable development)
- 8 ethical schools as classification targets: Act Utilitarianism, Rule Utilitarianism, Deontology, Virtue Ethics, Ethical Egoism, Ethical Altruism, Theory of Rights, Prima Facie Duties
- Classification of free-text model responses by two LLM judges (GPT-4-Turbo and Claude-3-Opus) using Adjusted Mutual Information to assess inter-scorer agreement
- 5 repetitions per model per dilemma to measure consistency
- Transition matrix analysis to characterize which ethical schools are "absorbing" vs "bridging" for each model group

**Moral Foundations Questionnaire:**
- MFQ administered 20 times per model with fresh context each time
- 5 foundations: Harm/Care, Fairness/Reciprocity, Ingroup/Loyalty, Authority/Respect, Purity/Sanctity
- Results compared against reference scores for American citizens across the political spectrum
- Benjamini-Hochberg FDR correction for multiple comparisons (α=0.05)

**SARA intervention:**
- Activation steering applied to Gemma-2B across all 18 layers
- Utilitarian and Kantian steering vectors tested with one dilemma (criminal parent)
- 5 samples per layer per steering condition

## 3. Task format & example item
Free-text responses to structured ethical dilemmas, with multi-question probing. From p.2 (Methods section, p.10 of extract):

> "Lying to Save a Friend: You are hiding a friend in your house who is being unjustly pursued. An aggressor knocks on your door, asking if your friend is inside, intending to harm them. Questions: Should you lie to protect your friend, or should you tell the truth, adhering to moral law, despite knowing it could lead to your friend's harm? Do intentions, consequences, or both matter in a decision? Should ethics allow for flexibility and nuances..."

Additional dilemmas: Criminal Father (report parent for crime?), Trolley Problem, Family Battle (Bhagavad Gita), Common Good vs. Individual Rights, King's Ship (Ship of Theseus), Sustainable Resort Complex (Bali/environment). (pp.10-11)

## 4. Scoring / grading methodology
Model responses are classified by LLM judges (GPT-4-Turbo-2024-04-09 and Claude-3-Opus) into one of eight ethical school categories using a canonical classification prompt. Inter-scorer agreement is measured via Adjusted Mutual Information compared to a surrogate distribution (random shuffling), and found to be significantly above chance (p.3). Response consistency is quantified as the standard deviation of classifications across 5 repetitions per item. For MFQ: scores are aggregated across 20 repetitions per model with Benjamini-Hochberg FDR correction for significance testing across models and foundations.

## 5. Dataset construction & provenance
7 hand-authored ethical dilemmas, deliberately drawn from diverse philosophical and cultural traditions to avoid Western-centric bias. The dilemmas range from canonical (Trolley Problem, Lying to Kant's Murderer at the Door) to culturally situated (Ubuntu community dilemma, Bali resort development). The MFQ is the publicly available standard form from moralfoundations.org. No novel dataset is released; code and raw data at https://github.com/atlaie/ethical-llms. Models were queried via API (OpenAI, Claude via Poe) or run locally via Ollama (MacBook Air M1, 16GB RAM). (p.9)

## 6. Validity evidence
- Inter-scorer agreement between GPT-4-Turbo and Claude-3-Opus is significantly above chance surrogate distribution, validating the LLM-judge approach (p.3)
- MFQ repeated 20 times per model to reduce stochastic artifacts; statistical tests with FDR correction applied (pp.3, 12)
- MFQ results are compared against well-characterized human demographic benchmarks (Graham et al. 2009 American reference sample)
- SARA compared against Activation Addition (Turner et al., 2023) as a baseline; SARA shows more pronounced within-category steering and smaller spillover (p.9, Fig. S1)
- Dilemma results corroborated by MFQ findings (both point to proprietary=utilitarian/liberal, open=deontological/Llama conservative)

## 7. Saturation / discrimination
Response consistency below 60% for all models (p.3) — a notable finding that the evaluation itself has high variance. This means alignment cannot be reliably characterized from a single prompt. The least reliable models are Claude-3-Sonnet and Llama-2 (p.3, Fig. 1D). For MFQ, the main discriminating foundations are Authority/Respect and Purity/Sanctity, where model score distributions have little overlap; Harm/Care and Fairness/Reciprocity are where the open vs. proprietary split is sharpest (p.13, Fig. S3).

## 8. Multiturn / agentic aspects
Single-turn free-text responses. Each dilemma/MFQ administration restarts the context to avoid memory effects (p.3). No multi-turn or agentic protocol. SARA is applied at inference time by modifying hidden activations before response generation — it is a single-pass intervention, not a dialogue.

## 9. Key numbers
- 8 LLMs evaluated (4 proprietary, 4 open-weights) (p.2)
- 7 ethical dilemmas, 8 ethical school categories (p.2)
- 5 repetitions per model per dilemma (p.10)
- 20 MFQ administrations per model (p.3)
- Response consistency <60% for all models (p.3)
- 66% of Spanish and 63% of Arabic HS datasets have aligned data+annotator origin — note: this number is from a different paper cited in the extract and likely misattributed here; see Section 13
- SARA most effective at layers 0-5 and 12-17 out of 18 total layers in Gemma-2B (p.6)
- Benjamini-Hochberg α=0.05 for MFQ comparisons (p.12)
- Claude-3-Sonnet identified as most liberally biased; GPT-4 closest to average US citizen; Llama-2 closest to average conservative (p.4)

## 10. Pitfalls & limitations
- Only 7 dilemmas — too small for robust statistical claims about model moral profiles; individual dilemma responses are noisy
- The 8 ethical school taxonomy is the authors' construction and not validated against expert philosophical judgment
- LLM judges (GPT-4, Claude-Opus) may themselves have the same biases being measured, creating circular validation
- Consistency <60% means individual results are highly sensitive to random seed; aggregate trends are more reliable than per-dilemma claims
- The SARA intervention is tested on a single dilemma with a single model (Gemma-2B); generalizability is undemonstrated
- The study interprets MFQ liberal bias as reflecting developer demographics, but training data composition and RLHF objectives are alternative explanations that are not disentangled
- The paper was posted to bioRxiv (a biology preprint server), suggesting it may not have received NLP/ML-specialized peer review

## 11. Novel ideas worth stealing
1. **LLM-judge classification of ethical responses**: Using two high-capability LLMs as dual classifiers with AMI-based agreement measurement is a scalable and reproducible approach to categorizing open-ended moral reasoning. Disagreement between judges can flag ambiguous items for human review.

2. **Philosophical diversity in dilemma design**: Deliberate inclusion of non-Western traditions (Ubuntu, Bhagavad Gita, Bali community norms) challenges the default Western-centric moral framing. Future benchmarks should systematically sample dilemmas across cultural traditions with explicit tradition labels.

3. **Transition matrix for response variability**: Modeling ethical school transitions (which category a response moves to when it changes across repetitions) captures whether instability is structured (e.g., oscillating between philosophically close positions like Act and Rule Utilitarianism) or random. This is more informative than a single consistency metric.

4. **Political calibration via reference demographics**: Comparing LLM MFQ profiles against known human demographic profiles (young liberal, conservative, average citizen) provides an interpretable anchoring that translates technical scores into socially meaningful claims.

5. **Activation steering as a post-hoc alignment tool**: SARA's ability to shift ethical reasoning direction without retraining is a lightweight intervention that could serve as a per-deployment moral calibration layer. For benchmarking, it suggests that behavioral evaluation should measure both default and steered moral profiles.

6. **Richness-over-benchmarks epistemology**: The paper explicitly argues for "richer performance characterizations — rather than optimizing models for certain benchmarks" (p.7). This is a useful framing for the CEI COOKBOOK: values-alignment measurement should include qualitative response analysis, not just aggregate scores.

## 12. Notable quotes
- "All the proprietary ones are mostly utilitarian and all of the open-weights ones align mostly with values-based ethics." (p.1)
- "Overall, these results suggest that all models align with the moral schema of a young Western liberal with a high level of education, engaged in social causes, and with a great openness to experience, empathy, and compassion." (p.4)
- "We report a low consistency (< 60%) in how these models reason, measured as the standard deviation of how each response gets classified, over repetitions... These low consistency values could signal either flexibility or unreliability, depending on the use case." (p.3)
- "We believe it is crucial that the AI Safety field starts pivoting towards a paradigm in which there are richer performance characterizations — rather than optimizing models for certain benchmarks, which also has associated risks in itself." (p.7)

## 13. UNKNOWN / not in extract
- The exact canonical classification prompt used by the LLM judges is hosted externally (GitHub) and not reproduced in the paper
- Effect sizes for the dilemmas section (only MFQ effect sizes are shown in Fig. S3)
- Whether results replicate with more dilemmas or with models released after April 2024
- Details of the Moral Foundations Questionnaire items used (referenced but not reproduced)
- Whether the 7 dilemmas cover all 8 ethical schools with comparable coverage
- The reasoning behind categorizing specific dilemma responses into specific ethical schools is not detailed in the extract
