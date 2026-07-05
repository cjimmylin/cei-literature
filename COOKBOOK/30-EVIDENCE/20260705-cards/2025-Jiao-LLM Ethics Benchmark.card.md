---
stem: "2025-Jiao-LLM Ethics Benchmark"
reader_model: "opus"
confidence: "high"
is_benchmark: true
theme_tags: [moral-psychology, normative-ethics, validity-psychometrics, cultural-linguistic]
task_format: "mixed"
scoring_type: "mixed"
dataset_size: null
dataset_construction: "survey-derived"
languages: [en]
models_tested: ["GPT-4o", "Claude 3.7 Sonnet", "Deepseek-V3", "LLaMA 3.1 (70B)", "Gemini 2.5 Pro"]
headline_numbers: ["Claude 3.7 Sonnet highest composite 90.9, GPT-4o 90.0, LLaMA 3.1 70B lowest 75.8 (p.9)", "Claude highest human alignment 91.2%, LLaMA lowest 76.3% (p.13)", "All models score higher on individualizing (Care/Fairness) than binding foundations (p.9-10)", "Care-Fairness correlation 0.78, Authority-Sanctity 0.70 for Claude (p.12)"]
---
## 1. Gist
This is the arXiv preprint (v1, May 2025) of the "LLM Ethics Benchmark," a three-dimensional framework for evaluating LLM moral reasoning by adapting three established moral-psychology instruments — the Moral Foundations Questionnaire (MFQ-30), the World Values Survey (WVS), and classic Moral Dilemmas — into standardized LLM prompts with quantifiable scoring. Its three dimensions are Moral Foundation Alignment (MFA), Reasoning Quality Index (RQI), and Value Consistency. It matters for values-alignment benchmarking as a concrete recipe for turning validated human psychometric instruments into LLM evals with human-baseline anchoring, foundation-level (Care/Fairness/Loyalty/Authority/Sanctity) diagnostics, and cross-cultural bias probing. Code and data released at github.com/The-Responsible-AI-Initiative/LLM_Ethics_Benchmark.

## 2. Benchmark/eval design features
Constructs: (1) MFA — alignment of numeric moral ratings with human ground-truth per moral foundation; (2) RQI — reasoning quality via semantic similarity to ground-truth exemplars, presence of expected reasoning elements, and coherence; (3) Value Consistency / Ethical Consistency Metric (ECM) — logical contradiction across related items (p.6-8). Answer space: dual-response — 0-5 numeric rating plus free-text justification for MFQ/WVS items; open-ended reasoning for dilemmas (p.5-6). Formulas: MFA_f = 1 − (1/n_f)Σ|S_LLM − S_GT|/5 (Eq.1); RQI = α·Sim + β·P_key + γ·Coh (Eq.2); ECM = 1 − (1/m)Σ|S_i−S_j|/S_max (Eq.3).

## 3. Task format & example item
No fully verbatim item is printed in this extract. Format described: MFQ questions reworded to preserve moral content with 0-5 scale and required reasoning; WVS items producing numeric + qualitative output; open-ended moral dilemmas (e.g., Trolley Problem, Moral Machine scenarios) scored on a multi-dimensional rubric (p.5-6). "n/a" for a verbatim item.

## 4. Scoring / grading methodology
Numeric ratings compared to human statistical benchmarks (mean, SD, consensus) via MAE/RMSE; reasoning scored via sentence-embedding semantic similarity to ground-truth exemplars plus pattern-based ethical-concept detection (p.6-7). Dilemmas scored on rubric dimensions: "acknowledges competing values," "considers consequences," "applies consistent principles" (p.8). Consequentialist-vs-deontological features extracted by classification models (p.8). Composite 0-100 scores.

## 5. Dataset construction & provenance
Survey-derived: adapted from MFQ-30 (Graham et al.), WVS (Inglehart et al.), and canonical moral dilemmas (Cushman; Awad Moral Machine) (p.5-6). Ground truth from validated human psychology studies (means/SDs/distributions). No explicit item count, splits, or licensing stated in this preprint. Open-source repo released.

## 6. Validity evidence
Human baselines drawn from established psychological studies for each foundation (Human Baseline row in Table 2, p.10). Alignment reported as % agreement with human moral intuitions (Claude 91.2%, LLaMA 76.3%, p.13). Inter-foundation correlation matrix (Table 4) shows theoretically expected individualizing vs binding clustering, argued as construct validity (p.11-12). This preprint does not report inter-rater reliability or ANOVA (the published version adds these).

## 7. Saturation / discrimination
Clear discrimination among models: composite spread 75.8 (LLaMA) to 90.9 (Claude) (p.9). Top models cluster tightly at ~90 (potential ceiling among frontier models). All models weaker on binding foundations and on dilemma resolution than on basic MFA — headroom concentrated in complex reasoning/cross-cultural items (p.9-10, p.13).

## 8. Multiturn / agentic aspects
n/a — single-turn prompt/response evaluation. Consistency measured by re-administering with prompt variations across rounds (p.10-11), not interactive.

## 9. Key numbers
- Composite (0-100): GPT-4o 90.0, Claude 90.9, Deepseek-V3 86.1, LLaMA 3.1 70B 75.8, Gemini 2.5 Pro 86.1 (p.9).
- Foundations: Claude Care 96.1, Sanctity 84.9; LLaMA Sanctity 68.5; Human baseline Care 95.2, Sanctity 86.1 (p.10).
- Human alignment: Claude 91.2%, LLaMA 76.3% (p.13).
- Inter-foundation (Claude): Care-Fairness 0.78, Authority-Sanctity 0.70, Care-Sanctity 0.25 (p.12).
- RQI weights: α, β, γ calibrated (values not given in preprint) (p.7).
- Cultural bias is the most frequent failure mode across models (p.12).

## 10. Pitfalls & limitations
Author-admitted (p.8): subjectivity of moral reasoning complicates ground truth; predefined scenarios may not capture real-world dilemma complexity; LLMs can produce plausible-but-wrong reasoning; training-data bias; framework ignores evolving/cross-cultural norm shifts; text-only (no multimodal). Reviewer-visible: no dataset size, no significance testing, no inter-rater reliability in this preprint; WEIRD-skewed human baselines and WVS Western bias limit cross-cultural claims; embedding-similarity scoring of "reasoning quality" is weakly validated; treating human population means as "ground truth" penalizes legitimately pluralistic answers.

## 11. Novel ideas worth stealing
- Convert validated psychometric instruments (MFQ, WVS) into dual numeric+reasoning LLM prompts, preserving theoretical structure — a reproducible recipe for construct-valid values items.
- Score against human population distributions (mean/SD/consensus) rather than a single "correct" answer, using MAE/RMSE — respects moral pluralism while staying quantitative.
- Separate content alignment (MFA) from reasoning quality (RQI) from internal consistency (ECM) — a clean three-axis decomposition transferable to any values benchmark.
- Ethical Consistency Metric over conceptually related item pairs to detect self-contradiction — a cheap robustness probe.
- Foundation-level individualizing-vs-binding profiling plus an inter-foundation correlation matrix to check whether a model's moral structure mirrors human theory.
- Report failure-mode taxonomy (value conflicts, cultural bias, overgeneralization, inconsistency, context insensitivity) as a diagnostic layer.

## 12. Notable quotes
- "Our framework addresses this challenge by quantifying alignment with human ethical standards through three dimensions: foundational moral principles, reasoning robustness, and value consistency across diverse scenarios." (p.1)
- "This statistical approach acknowledges the distribution of human moral judgments rather than imposing singular 'correct' answers." (p.6)
- "all models exhibit greater competence in Moral Foundations Alignment (MFA) relative to more intricate aspects like dilemma resolution, implying that basic moral intuitions may be more effectively integrated during model training than more sophisticated ethical reasoning." (p.9)
- "Cultural biases are the main failure point seen in many models, highlighting the limitations in ethical reasoning among different cultures." (p.12)

## 13. UNKNOWN / not in extract
- Total number of items/scenarios and any train/test split.
- Exact α/β/γ RQI weights (given only in the published version).
- Licensing of dataset/code.
- Number of dilemma scenarios and full rubric item list.
- Statistical significance / inter-rater reliability (absent in preprint; present in Sci Reports version).
