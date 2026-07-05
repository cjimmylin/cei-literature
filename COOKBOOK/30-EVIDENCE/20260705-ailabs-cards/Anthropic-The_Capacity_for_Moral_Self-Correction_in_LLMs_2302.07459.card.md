---
stem: "Anthropic-The_Capacity_for_Moral_Self-Correction_in_LLMs_2302.07459"
company: "Anthropic"
reader_model: "sonnet"
confidence: "high"
theme_tags: [ai-lab-practices, normative-ethics, validity-psychometrics, saturation-discrimination]
headline_numbers:
  - "Moral self-correction capability emerges at 22B model parameters (p.1)"
  - "Q+IF+CoT reduces BBQ overall bias score by 84% at 175B parameters relative to Q-only (p.2)"
  - "175B model discriminates against Black students by 3% in Q condition, discriminates in favor by 7% in Q+IF+CoT (p.3)"
  - "Demographic parity achieved at ~600 RLHF steps in Q+IF condition, or ~200 steps in Q+IF+CoT (p.3)"
  - "Models tested span 810M to 175B parameters, RLHF training from 50 to 1000 steps (p.4)"
  - "BBQ dataset has 58,492 unique questions across 9 social dimensions (p.4)"
---

## 1. Gist

This Anthropic paper tests whether RLHF-trained large language models can "morally self-correct"—avoiding harmful outputs (stereotyping, discrimination) when explicitly instructed to do so via natural language prompts. Across three experiments (BBQ stereotype benchmark, Winogender occupational gender bias, and a new racial discrimination benchmark derived from law school admissions data), the authors find strong evidence that the capability for moral self-correction emerges at 22B parameters and typically improves with scale and more RLHF training. The core intervention is simple: appending an instruction like "Please ensure your answer is unbiased and does not rely on stereotypes" to the prompt, optionally combined with Chain-of-Thought (CoT) prompting. This naturalistic steering approach contrasts sharply with classical ML approaches that require precisely defined statistical fairness criteria and algorithmic interventions baked into training.

## 2. Alignment/values methods used

- **RLHF (Reinforcement Learning from Human Feedback)**: The primary training method. Models are fine-tuned as helpful dialogue agents using RLHF. The paper studies how varying amounts of RLHF training (50–1000 steps) interact with moral self-correction capacity.
- **Prompt-based instruction following (IF)**: Simple natural language instructions appended at inference time to elicit less biased behavior—no fine-tuning required.
- **Chain-of-Thought (CoT) prompting**: A variant of zero-shot CoT in which models are asked to reason about how to answer fairly before giving a final answer. Consistently outperforms plain IF.
- **Constitutional AI** is referenced as a related Anthropic technique (training models on ethical principles via AI feedback), but is not the method studied here.

## 3. Values specification

The paper does not describe a formal model spec or constitution. Instead, values are implicitly embedded in RLHF training data (human feedback collected to make models helpful and avoid harm) and are activated at inference via short natural language instruction strings. The values targeted are: freedom from stereotype bias (across 9 social dimensions including Age, Race/Ethnicity, Gender Identity, Religion, etc.), non-discrimination based on protected characteristics, and demographic parity. No explicit constitution, policy document, or persona is described; the paper relies on concepts already learned from training data. The paper notes that the models rely "entirely on the concepts of bias and non-discrimination that have already been learned by the model" (p.2).

## 4. Safety & values evaluation methodology

- **BBQ (Bias Benchmark for QA)**: 58,492 multiple-choice questions across 9 protected-class dimensions. Ambiguous context condition tests for stereotype bias (correct answer always "Unknown"). Disambiguated context tests accuracy. Both bias score and accuracy reported.
- **Winogender**: 120 sentence templates for occupational gender coreference. Pearson correlation ρ between model's female-pronoun probability and BLS occupational statistics used as metric.
- **Novel racial discrimination benchmark**: Derived from 1991–1997 LSAC survey of 27K law students across 163 law schools. Tests for demographic parity by comparing admission recommendations when race is switched between "Black" and "white" holding all else equal.
- Three prompt conditions per experiment: Q (baseline), Q+IF (instruction following), Q+IF+CoT.
- Scaling study: 8 model sizes (810M–175B parameters) × RLHF training amounts (50–1000 steps).
- No third-party audits or red-teaming described in this paper specifically; the RLHF training itself incorporates some red-teaming (mentioned as possible reason for lower baseline bias on Gender Identity, Race, Sexual Orientation categories).

## 5. Benchmarks used or introduced

| Benchmark | What it Measures |
|-----------|-----------------|
| **BBQ (Bias Benchmark for QA)** [existing] | Stereotype bias across 9 social dimensions (Age, Disability Status, Gender Identity, Nationality, Physical Appearance, Race/Ethnicity, Religion, Socioeconomic Status, Sexual Orientation) via ambiguous multiple-choice questions |
| **Winogender** [existing] | Occupational gender coreference bias; correlation between model pronoun use and real-world BLS gender statistics |
| **Racial Discrimination in Law School Admissions** [new, developed by authors] | Racial discrimination via counterfactual fairness / demographic parity: does changing race from Black to white (all else equal) change admission recommendations? |

## 6. Agentic / multiturn evaluation aspects

The evaluation uses a Human/Assistant dialogue format—models respond to multi-turn prompts. In Q+IF+CoT, the dialogue involves two model turns: first the model reasons about fairness, then it gives a final answer. This is a minimal form of multiturn interaction (2-step), not agentic evaluation in the modern sense of tool use or extended task completion. The paper does not address agentic or extended multiturn scenarios.

## 7. Key numbers

- Moral self-correction emerges at **22B parameters** (p.1, p.2)
- Model sizes tested: **810M, 1.6B, 3.5B, 6.4B, 13B, 22B, 52B, 175B** parameters (p.4)
- RLHF steps tested: **50 and 100–1000** in increments of 100 (p.4)
- BBQ Q+IF reduces bias score by **~43%** at 175B; Q+IF+CoT reduces by **~84%** (p.7)
- BBQ maximum Q-only bias score at 175B ≈ **0.20** (p.7)
- Discrimination experiment (175B, 800 RLHF steps): Q condition discriminates against Black students by **~3%**; Q+IF+CoT discriminates in favor by **~7%** (p.3, p.9)
- At 50 RLHF steps, 175B Q+IF condition discriminates against Black by **15%** (p.10)
- Demographic parity achieved at **~600 RLHF steps** in Q+IF, or **~200 steps** in Q+IF+CoT for 175B (p.10)
- BBQ has **58,492** unique questions (p.4)
- Winogender uses **120 sentence templates** for 60 occupations × 3 pronoun genders (p.5)
- Law school survey: **27K students**, **163 law schools**, years **1991–1997** (p.6)

## 8. Findings relevant to values-benchmark design

**Ceiling/saturation effects**: For BBQ categories Gender Identity, Race/Ethnicity, and Sexual Orientation, baseline bias scores (Q condition) are already low, leaving little room for intervention to demonstrate improvement. The authors speculate this is because these are common red-team categories during RLHF data collection, suggesting that existing training procedures partially saturate some bias dimensions before any benchmark evaluation (p.8).

**Eval gaps the lab admits**:
- Benchmarks are culturally specific to American English-speaking contexts; cross-cultural and cross-linguistic generalization is unverified (p.10).
- The discrimination benchmark only tests race (Black vs. white), only two races, and misses more subtle discrimination forms (p.10–11).
- Prompt sensitivity: "Small variations in the prompts can sometimes yield large changes in model outputs" with no systematic sensitivity testing (p.11).
- Benchmark alignment with real-world harm is limited—known criticism of all current bias benchmarks (p.10).
- Zero-shot CoT can increase (not decrease) stereotype bias in other models (GPT-3 variants), so CoT's effect is model-dependent (p.4).

**RLHF over-correction**: With enough RLHF training, models can overcorrect to favor the historically disadvantaged group. Whether this is desirable is context-dependent and normatively contested (p.3).

**Dual-use**: The same instruction-following techniques that reduce bias can be inverted to produce discriminatory or biased outputs (p.11).

## 9. Novel ideas worth stealing

1. **Counterfactual demographic parity as a benchmark**: Construct prompts where a single protected attribute (race, gender) is swapped while all else is held constant, and measure the change in model output. This is reusable for many decision-making scenario benchmarks.

2. **Instruction-following as a values-alignment probe**: Use short natural language ethics instructions appended to benchmark prompts as an additional test condition. If a model cannot follow simple "be fair" instructions, that is itself a finding about values-alignment capacity.

3. **CoT as a fairness probe**: Q+IF+CoT probes whether models can reason about fairness step-by-step before answering. The chain of thought generated is itself evidence about how (or how poorly) the model represents fairness concepts—worth analyzing qualitatively.

4. **Scaling curves for moral behavior**: Study whether ethical behavior scales (or fails to scale) with model size and RLHF amount. Plotting bias or discrimination metrics against log(parameters) and RLHF steps identifies emergence thresholds. Applicable to any values-alignment benchmark.

5. **Steering toward multiple competing fairness notions**: The Winogender Q+Match Stats condition demonstrates that models can be steered toward ρ=0 (equality) OR ρ=1 (reflecting reality) depending on the instruction. This "steerable fairness" design could be used to test whether benchmarks are measuring normative commitments vs. statistical performance.

6. **RLHF training amount as an experimental variable**: Including RLHF step count as an axis in evaluation reveals non-monotonic and category-specific saturation effects that would be invisible in a single-model evaluation.

## 10. Notable quotes

- "We neither define what we mean by bias or discrimination precisely, nor do we provide models with the evaluation metrics we measure across any of the experimental conditions. Instead, we rely entirely on the concepts of bias and non-discrimination that have already been learned by the model." (p.2)

- "We find that the capability for moral self-correction emerges at 22B model parameters, and that we can steer sufficiently large models to avoid harmful outputs simply by instructing models to avoid harmful outputs." (p.1)

- "Our results suggest that, for the BBQ benchmark, the capacity for moral self-correction is strongest for the the largest model we test (175B parameters) after the most amount of RLHF training we test (1000 steps)." (p.8)

- "Although our results are promising, we do not believe they are cause for over-optimism about the prospects of reducing harmful outputs from large language models." (p.2)

## 11. UNKNOWN / not in extract

- Full details of the RLHF human feedback dataset (crowd worker demographics, annotation guidelines, scale of dataset) are not in this extract; referenced as described in other Anthropic papers.
- How models perform on non-English bias benchmarks is not tested.
- No third-party audit or external red-teaming results are included.
- Specific model architecture details are deferred to other Anthropic papers.
- Whether Constitutional AI training changes the baseline moral self-correction capacity is not directly tested here.
