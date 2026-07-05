---
stem: "2025-Hu-LLMs on Trial Evaluating Judicial Fairness for Large Language Models"
reader_model: "sonnet"
confidence: "high"
is_benchmark: true
theme_tags: [validity-psychometrics, saturation-discrimination, normative-ethics, cultural-linguistic]
task_format: "free-text"
scoring_type: "behavioral"
dataset_size: 177100
dataset_construction: "mixed"
languages: ["zh"]
models_tested: ["GLM-4", "Gemini Flash 1.5", "Mistral Nemo", "Llama 3.1 8B Instruct", "GLM-4 Flash", "Qwen2.5 72B Instruct", "LFM 40B MoE", "Gemini Flash 1.5 8B", "Qwen2.5 7B Instruct", "Nova Lite 1.0", "Nova Micro 1.0", "DeepSeek V3", "Phi 4", "DeepSeek R1-32B Qwen", "LFM 7B", "Mistral Small 3"]
headline_numbers:
  - "Average inconsistency across 15 models at temperature=0 exceeds 15% (p.8)"
  - "14 out of 15 models show significant bias at temperature=0 via Bernoulli test (p.9)"
  - "14 out of 15 models show significant imbalanced inaccuracy at temperature=0 (p.9)"
  - "Mean Weighted Average MAE across all models is 64.871 months (~5 years deviation) (p.9)"
  - "Mean Weighted Average MAPE of all models is 219%, meaning LLMs are on average multiple times harsher than real sentences (p.9)"
  - "Bernoulli test across all LLMs yields p-value < 0.01 for both bias and imbalanced inaccuracy (p.9)"
  - "Demographic labels show significantly more pronounced biases than non-demographic labels (p.9)"
---

## 1. Gist

This paper introduces JudiFair, a large-scale benchmark for evaluating the judicial fairness of LLMs when used as decision-makers in criminal sentencing tasks. The authors construct a systematic framework grounded in legal and philosophical theories of judicial fairness, distinguishing between substance factors (crime-related) and procedure factors (process-related), and between demographic and non-demographic attributes. The benchmark comprises 177,100 unique counterfactually generated case facts drawn from 1,100 Chinese judicial documents, annotated with 65 extra-legal factor labels and 161 distinct values. Experiments on 16 LLMs using three novel metrics — inconsistency, bias, and imbalanced inaccuracy — reveal pervasive judicial unfairness across all models. The work matters for values-alignment benchmarking because it demonstrates that LLMs absorb and reproduce real-world judicial biases, that demographic factors drive more pronounced unfairness than non-demographic factors, and that higher accuracy paradoxically correlates with greater bias — a fundamental alignment challenge for high-stakes decision-making.

## 2. Benchmark/eval design features

**Framework:** A two-layer taxonomy covering (1) substance vs. procedure factors and (2) demographic vs. non-demographic attributes. This produces four quadrants: substance-demographic (e.g., defendant gender, ethnicity, age, sexual orientation), substance-non-demographic (e.g., crime date, time, location), procedure-demographic (e.g., judge gender/age, defender gender), and procedure-non-demographic (e.g., court level, whether trial is public, whether broadcast online).

**Label system:** 65 labels across the four categories, 161 distinct label values. Built on the LEEC dataset (Xue et al., 2024) and extended with labels typically absent from Chinese judicial documents (e.g., sexual orientation, judge demographics).

**Counterfactual design:** For each case and each label, the trigger sentence is identified and replaced with each alternative value, generating a separate query per counterfactual. LLMs are asked to predict a criminal sentence (months of imprisonment in JSON format) independently for each variant, so contextual contamination between alternatives is minimized.

**Three evaluation metrics:**
- *Inconsistency*: proportion of documents where LLM output changes when a label value changes (weighted average across labels).
- *Bias*: fixed-effect regression of log(sentence) on label values with document ID fixed effects; Bernoulli test across all labels to assess whether biases are systematic.
- *Imbalanced inaccuracy*: same regression but using absolute deviation from real human sentences as the dependent variable.

**Statistical rigor:** High-dimensional fixed-effect linear regression via REGHDFE in Stata; cluster-robust standard errors at document level; Bernoulli tests to guard against false discoveries from multiple comparisons; multiple robustness checks.

## 3. Task format & example item

LLMs are prompted with a role-play instruction ("You are now a judge proficient in Chinese law"), a task definition, sentencing rules, case facts, and parties. The model outputs a JSON structure with a sentencing prediction.

Example (p.20, Figure A2/A3 described): For the label "Court Level," the same crime facts are presented three times with the trigger sentence varying — primary, intermediate, and higher people's court. The model predicts a sentence length for each. For "Defendant Gender," the same case facts are presented with defendant identified as male, female, or non-binary.

The prompt ends with: "Please output the json structure of the sentencing result of the defendant according to the format given above." (p.20)

## 4. Scoring / grading methodology

Sentencing predictions (months of imprisonment) are extracted from LLM JSON outputs. Scores are computed at three levels:

1. **Inconsistency**: For each label, the proportion of documents where the LLM prediction changes across label values; weighted average across all labels using effective sample size as weight (Equation 1, p.7).

2. **Bias**: High-dimensional fixed-effect OLS regression of log(sentence+1) on indicator variables for each label value (reference group = baseline value) and document ID fixed effects (Equation 2, p.7). Significance per label value tested with cluster-robust t-tests. Bernoulli test (Equation 3, p.8) aggregates across labels and across models.

3. **Imbalanced inaccuracy**: Same regression as bias but dependent variable = absolute deviation between LLM prediction and actual human sentence (Equation 4, p.8). MAE and MAPE also computed.

Temperature is fixed at 0 for main analysis; temperature=1 experiments are run for comparison.

## 5. Dataset construction & provenance

- **Source**: 1,100 judicial documents sampled from the LEEC dataset (Xue et al., 2024), which draws from Chinese criminal court records.
- **Annotation**: 3 legal experts (Master of Law degree holders, paid $10/hour) annotated extra-legal labels and trigger sentences. Automated exact-match extraction; LLM-assisted semantic retrieval for cases without exact matches, reviewed by experts (p.8).
- **Counterfactual generation**: Trigger sentences replaced with each alternative label value to generate counterfactual cases. Cases where the label is legally relevant (e.g., occupation in bribery cases) are excluded to avoid confounds (p.8).
- **Size**: 177,100 unique case facts across 65 labels (p.2).
- **Splits**: No train/test splits — this is an evaluation-only benchmark.
- **Language**: Simplified Chinese; scoped to Chinese criminal law (p.1).
- **Licensing**: Built on LEEC (publicly available); dataset and toolkit publicly released.
- **Contamination controls**: Separate query per counterfactual value (no side-by-side comparison within single context) to prevent contextual shortcuts (p.5).

## 6. Validity evidence

- **Construct validity**: Framework grounded in legal and philosophical theories of judicial fairness (Rawls 1971, Waldron 2011); labels derived from empirical legal studies of real judicial bias (p.3-4).
- **Criterion validity**: LLM biases are shown to align directionally with known real-world judicial biases — e.g., female defendants treated more leniently, rural Hukou defendants treated more harshly — mirroring prior empirical legal research (p.9).
- **Human baseline**: Real sentencing data from judicial documents used as ground truth for imbalanced inaccuracy metric (p.5).
- **Statistical rigor**: Fixed-effect regression with cluster-robust standard errors; Bernoulli tests to control for false discovery across 65 labels; multiple robustness checks in Appendix E.4 (p.8).
- **Prompt evaluation**: Pre-experiment prompt testing across 420 queries, run 3 times each, to assess format adherence and variation (p.20).

## 7. Saturation / discrimination

- **No ceiling effects**: All 16 models fail — average inconsistency exceeds 15% and 14/15 models show systematic bias and imbalanced inaccuracy at temperature=0 (p.8-9). There is substantial remaining headroom.
- **Discrimination within models**: The benchmark differentiates between model behaviors — some models show bias concentrated on specific labels (e.g., defendant wealth significant in 10/13 models; victim age biased in only 1 model) (p.9, footnote 6).
- **Accuracy-bias trade-off**: More accurate models show *more* bias, not less — a discrimination-relevant finding that flips the usual expectation (p.9).
- **Temperature effect on discrimination**: Higher temperature increases inconsistency but decreases the number of significantly biased labels, suggesting temperature is a lever that trades one type of unfairness for another (p.9-10).

## 8. Multiturn / agentic aspects

n/a. All evaluations are single-turn: each counterfactual case fact is presented to the LLM in a single prompt, and the LLM produces a sentencing JSON. No multi-turn dialogue, tool use, or agentic environment.

## 9. Key numbers

- 177,100 unique case facts in JudiFair (p.2)
- 1,100 source judicial documents (p.5)
- 65 labels, 161 label values (p.2)
- 16 LLMs evaluated (p.1)
- Average inconsistency > 15% across 15 models at temperature=0 (p.8)
- 14/15 models show significant bias at temperature=0; Bernoulli test p < 0.01 across all LLMs (p.9)
- 14/15 models show significant imbalanced inaccuracy at temperature=0 (p.9)
- Mean Weighted Average MAE = 64.871 months (~5+ year deviation from real sentences) (p.9)
- Mean Weighted Average MAPE = 219% (LLMs sentence roughly 3x harsher than real judges on average) (p.9)
- 3 legal expert annotators, paid $10/hour (p.19)
- Demographic labels show "notably more pronounced biases" than non-demographic labels (p.9)
- Procedure factors slightly more biased than substance factors; judge characteristics especially biased (p.9)
- No significant effect of model size, release date, or country of origin on fairness (p.10)
- Positive correlation between accuracy and bias (p.9-10)
- Negative correlation between inconsistency and bias — greater randomness masks underlying bias (p.9)
- Defendant wealth: significant bias in 10/13 models; victim age: biased in only 1 model (p.9, fn.6)

## 10. Pitfalls & limitations

**Author-admitted:**
- Dataset, label system, and experiments are scoped to the Chinese legal system; judicial fairness is highly context-specific and may not generalize cross-jurisdictionally (p.10).
- Most experiments run on small/mid-scale non-reasoning models; reasoning models (DeepSeek R1) were included but did not show substantially fewer fairness issues (p.10).
- More advanced prompting strategies (CoT, RAG) not systematically tested and may reduce bias or improve interpretability (p.10).

**Additional flaws visible:**
- Chinese-only cases means all models are evaluated in a non-English context; models may perform differently in their primary training language.
- Counterfactual prompting assumes the trigger sentence is the sole carrier of label information; if labels leak through other parts of the case text, the counterfactual manipulation is incomplete.
- The JudiFair dataset conflates "LLM fairness" with "deviation from human judicial decisions" — but human judges themselves exhibit documented biases (the paper partially acknowledges this by noting LLM biases mirror real-world judicial biases).
- Proprietary API models (GLM-4, Gemini, Nova) have unknown parameter counts and training data, making it hard to interpret cross-model comparisons.
- The imbalanced inaccuracy metric requires ground-truth human sentences, limiting the benchmark's applicability to cases where real outcomes are available.

## 11. Novel ideas worth stealing

1. **Substance × Procedure × Demographic × Non-demographic 2×2 taxonomy**: Most fairness benchmarks focus only on demographic bias. Extending to procedural factors (court level, trial publicity, whether broadcast) reveals underexplored bias vectors — directly relevant to values-alignment benchmarks that examine AI behavior in institutional/bureaucratic contexts.

2. **Counterfactual-per-query (not counterfactual-in-context)**: Presenting each counterfactual as a completely separate prompt rather than showing alternatives side-by-side eliminates order effects, comparison shortcuts, and anchoring. This design principle transfers directly to MCQ-format values benchmarks wanting to test consistency across demographic variants.

3. **Bernoulli test for multiple-label multiple-model evaluation**: When testing bias across tens of labels and many models, naive significance testing inflates false discovery. The Bernoulli test approach (treating each label test as a Bernoulli trial and asking whether the count of significant results exceeds what pure randomness would produce) is a principled correction that can be adopted in any benchmark reporting aggregate bias statistics.

4. **Three-metric framework (inconsistency + bias + imbalanced inaccuracy)**: Consistency/reliability and accuracy-gap fairness are distinct from directional bias — measuring all three simultaneously and then computing their correlations reveals structural trade-offs (e.g., accuracy-bias trade-off) that single-metric benchmarks miss.

5. **Excluding legally relevant cases from fairness analysis**: When a label value is legally material for a specific crime type (e.g., occupation in bribery), including it contaminates fairness measurement. Building explicit exclusion logic based on legal relevance is a domain-grounded validity control transferable to any domain where some attributes are legitimately decision-relevant.

6. **Fixed-effect regression with document ID controls for within-document variance**: Using the same document as its own control across counterfactuals (via ID fixed effects) eliminates between-document confounds and isolates the causal effect of label manipulation — a strong within-subject design that could be replicated in other LLM behavioral evaluations.

7. **Temperature as a fairness lever**: The finding that higher temperature reduces bias but increases inconsistency frames temperature not just as an accuracy/creativity trade-off but as a fairness dial — a design insight for evaluators who want to characterize model behavior across the fairness-consistency space.

## 12. Notable quotes

"LLMs display notably more pronounced biases on demographic labels, with slightly less bias on substance labels compared to procedure ones." (p.1)

"Notably, as an LLM's accuracy increases, its bias also increases substantially. This suggests that when LLMs learn the patterns from real-world judicial data, the improvement in their predictive accuracy generally comes at the expense of biases." (p.9)

"Fairness is a broader concept than bias, and our comprehensive evaluations highlight systematic issues that call for mitigation approaches beyond mere prompting techniques." (p.11)

"Model size, release date, and country of origin show no correlation with improved fairness." (p.10)

## 13. UNKNOWN / not in extract

- Full detailed results tables (Table A17, Table A18) listing per-model scores for all three metrics are referenced but the extract does not render the table contents clearly enough to extract individual model scores.
- Exact figure content for Figure A9 (temperature vs. metrics), Figure A10 (release date), Figure A11 (parameter size), Figure A12 (country of origin comparisons) — described but not fully readable from extract.
- Detailed heatmap data from Appendix E.1 showing per-label per-model bias significance.
- Whether the JudiFair dataset and toolkit are available under an open license (extract mentions public release but does not specify a license).
- Whether non-Chinese LLMs were tested with Chinese-language inputs or translated prompts; language handling not specified.
- Exact inter-rater reliability statistics for the 3 legal annotators (voting procedure mentioned but kappa or other IRR metrics not reported in available extract).
