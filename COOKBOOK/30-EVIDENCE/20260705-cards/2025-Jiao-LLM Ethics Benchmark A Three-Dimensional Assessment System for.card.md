---
stem: "2025-Jiao-LLM Ethics Benchmark A Three-Dimensional Assessment System for"
reader_model: "opus"
confidence: "high"
is_benchmark: true
theme_tags: [moral-psychology, normative-ethics, validity-psychometrics, cultural-linguistic]
task_format: "mixed"
scoring_type: "mixed"
dataset_size: 50
dataset_construction: "survey-derived"
languages: [en]
models_tested: ["GPT-4o", "Claude 3.7 Sonnet", "Deepseek-V3", "LLaMA 3.1 (70B)", "Gemini 2.5 Pro"]
headline_numbers: ["Claude composite 90.9±0.9, GPT-4o 90.0±1.0, LLaMA 3.1 70B 75.8±1.0 (p.6)", "Inter-rater reliability Cohen's kappa 0.89 (p.7)", "Human baseline reasoning depth 74% at levels 4-5 vs GPT-4o 62%, Claude 56%, LLaMA 28% (p.8)", "Value consistency CV: Claude 0.54%, LLaMA 3.60% (p.9)"]
---
## 1. Gist
This is the peer-reviewed Scientific Reports (2025, 15:34642) publication of the "LLM Ethics Benchmark" — the same three-dimensional moral-reasoning framework as the arXiv preprint, but with substantially more rigorous statistics (ANOVA, effect sizes, inter-rater reliability, coefficient of variation, correlation significance). It adapts MFQ-30, WVS, and Moral Dilemmas into LLM prompts to measure Moral Foundation Alignment (MFA), Reasoning Quality Index (RQI), and Value Consistency. It matters for values-alignment benchmarking as a psychometrically anchored, statistically validated template with explicit human baselines (Rest et al. 1999, N=200) and dual-method (expert + benchmark) validation.

## 2. Benchmark/eval design features
Three dimensions: MFA (Eq.1, alignment of 0-5 ratings to human ground truth per foundation), RQI (Eq.2, α=0.4·semantic-similarity + β=0.4·expected-reasoning-elements + γ=0.2·coherence), and Ethical Consistency Metric (Eq.3) over related item pairs (p.4-6). Explicit weight justification: content accuracy and reasoning thoroughness weighted equally, coherence down-weighted so fluency does not dominate (p.5). n=50 scenarios per model per dimension. Foundations: Care, Fairness, Loyalty, Authority, Sanctity. Reasoning components: principle identification, perspective-taking, consequence analysis, principle application (p.6-7).

## 3. Task format & example item
No fully verbatim item printed. MFQ items reworded to 0-5 scale + required justification; WVS items scored against population distributions; moral dilemmas (Trolley, Moral Machine) scored on rubric (p.3-5). Reasoning depth on validated 5-point scale: (1) basic issue ID, (2) limited stakeholder, (3) moderate consequence analysis, (4) advanced framework integration, (5) expert-level synthesis (p.7). "n/a" for verbatim item.

## 4. Scoring / grading methodology
Dual-method validation: (1) a philosophical-ethics expert reviewed all instrument modifications; (2) automated scoring aligned to established moral-psychology benchmarks (MFQ means/SDs, WVS population distributions, philosophical dilemma criteria) (p.3). Reasoning components scored by two trained evaluators, Cohen's kappa 0.89 (p.7). Numeric alignment via MAE/RMSE; reasoning via sentence-embedding similarity + expected-element detection + coherence. ANOVA across models with Tukey HSD, Dunn's test with Bonferroni for post-hoc (p.6-8).

## 5. Dataset construction & provenance
Survey-derived from MFQ-30, WVS, and canonical dilemmas (p.3-5). n=50 standardized scenarios per model per assessment. 3-5 archetypal justification patterns per foundation extracted from moral-psychology literature as ground truth (p.4). Human baseline from Rest et al. (1999), N=200 university students, age 18-25 (p.8). Data/code: github.com/The-Responsible-AI-Initiative/LLM_Ethics_Benchmark; CC BY-NC-ND 4.0 license (p.13). Received 30 May 2025, accepted 2 Sept 2025.

## 6. Validity evidence
Expert (philosophical ethics) review of all adaptations (p.3). Human baseline anchoring (Rest et al., N=200) (p.8). Inter-rater reliability Cohen's kappa 0.89 (p.7). ANOVA: all dimensions F(4,245), p<0.001, effect sizes η²=0.32-0.51 (Tables 1-3). Reasoning-depth Cohen's d effect sizes 1.8-2.4 between top models and LLaMA (p.7). Inter-foundation correlations mirror human baseline pattern (Care-Fairness r=0.78 Claude vs 0.81 human; Care-Sanctity 0.25 vs 0.19 human) (p.9). χ²(20)=45.7, p<0.001 for reasoning-depth distributions (p.8).

## 7. Saturation / discrimination
Strong discrimination: composite 75.8 (LLaMA) to 90.9 (Claude), F=28.6***, η²=0.32 (p.6). Very large model gaps in reasoning depth (Cohen's d 1.8-2.4). Ceiling among frontier models: GPT-4o/Claude statistically indistinguishable in reasoning depth (p=0.23, p.8). All LLMs significantly below human baseline (all p<0.001) — meaningful headroom remains. Binding foundations and dilemma resolution show most spread.

## 8. Multiturn / agentic aspects
n/a — single-turn. Consistency/stability tested via 5 independent rounds × 3 question-modification types (rewording, contextual variation, format switching), 15 evaluations per model, 24h apart to avoid carryover (p.8-9). Not interactive/agentic.

## 9. Key numbers
- Composite: GPT-4o 90.0±1.0, Claude 90.9±0.9, Deepseek-V3 86.1±1.0, LLaMA 75.8±1.0, Gemini 86.1±1.1; F=28.6***, η²=0.32 (p.6).
- Foundations F-stats 38.9-61.4***, η² 0.40-0.51 (p.7).
- Reasoning components: Cohen's kappa 0.89; F 39.8-52.1***, η² 0.39-0.46 (p.7).
- Reasoning depth 4-5: human 74%, GPT-4o 62%, Claude 56%, LLaMA 28% (p.8).
- Consistency CV: Claude 0.54%, GPT-4o 1.10%, Gemini 1.99%, Deepseek 2.24%, LLaMA 3.60%; F(4,20)=18.7*** (p.9).
- Human moral alignment: Claude 91.2%, GPT-4o 87.8%, LLaMA 76.3% (p.10).
- RQI weights α=0.4, β=0.4, γ=0.2 (p.5).

## 10. Pitfalls & limitations
Author-admitted (p.6): moral subjectivity blocks universal standards; predefined scenarios miss real-world ambiguity; LLMs generate plausible-but-flawed reasoning; biased training data; WVS-based cultural assessments may reflect Western bias and miss nuanced cultural values; ignores evolving norms; text-only. Reviewer-visible: n=50 scenarios per dimension is small; "ground truth" = human population means penalizes valid pluralistic responses; human baseline is a re-used external study (Rest 1999) with different scenarios, not a matched re-collection; embedding-similarity "reasoning quality" is a weak proxy; WEIRD-skewed baselines undermine binding-foundation and cross-cultural conclusions.

## 11. Novel ideas worth stealing
- Dual-method validation: expert (philosopher) review of item adaptations PLUS anchoring automated scoring to decades of validated psychometric benchmarks — a strong construct-validity playbook for values benchmarks.
- Report full inferential statistics (ANOVA, η², Cohen's d, Tukey HSD, χ²) and inter-rater kappa — raises the evidentiary bar for values-eval papers.
- Coefficient-of-variation stability testing across systematic prompt-perturbation types (rewording / context / format) as a framing-robustness metric.
- Down-weighting coherence (γ=0.2) so linguistic fluency does not inflate ethical-reasoning scores — a deliberate anti-glibness scoring choice.
- Inter-foundation correlation matrix compared to a human-baseline matrix as a "moral structure coherence" indicator (Care-Sanctity as the diagnostic cross-category pair).
- 5-level reasoning-depth rubric distribution vs human distribution — captures headroom that mean scores hide.

## 12. Notable quotes
- "This methodology successfully tackles inter-rater reliability issues by connecting automated evaluations to validated psychological and philosophical benchmarks, instead of relying on subjective human assessments." (p.3)
- "The equal weighting of semantic similarity (α) and fundamental reasoning components (β)... Simultaneously, the reduced coherence weight (γ) ensures that linguistic fluency does not overshadow meaningful ethical reasoning." (p.5)
- "Human participants exhibited a significant inclination towards advanced reasoning (scores 4–5), with 74% of their responses reaching these elevated levels... GPT-4o... 62%... LLaMA 3.1 (70B)... only 28%." (p.8)
- "This trend points to the possibility that existing language models may reveal a consistent bias towards individualistic ethical frameworks, which could impede their effectiveness in collectivist cultural contexts." (p.10)

## 13. UNKNOWN / not in extract
- Total item pool size beyond the n=50-per-model figure and any train/test split.
- Full verbatim example items.
- Whether the human baseline (Rest 1999) used exactly the same scenarios as the LLM eval.
- Exact per-model MAE/RMSE values.
- How the two evaluators were trained and how disagreements were resolved beyond kappa.
