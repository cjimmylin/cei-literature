---
stem: "2025-Sachdeva-Normative Evaluation of LLMs with Everyday Moral Dilemmas"
reader_model: "sonnet"
confidence: "high"
is_benchmark: true
theme_tags: [moral-psychology, normative-ethics, cultural-linguistic, validity-psychometrics]
task_format: "free-text"
scoring_type: "classifier"
dataset_size: 10826
dataset_construction: "scraped"
languages: ["en"]
models_tested: ["GPT-3.5", "GPT-4", "Claude Haiku", "PaLM 2 Bison", "Llama 2 7B", "Mistral 7B", "Gemma 7B"]
headline_numbers:
  - "GPT-4 had the highest agreement with Redditors (Krippendorff's alpha = 0.34) (p.8)"
  - "LLMs show low inter-model agreement overall; Mistral and Llama 2 show negative alpha with all others (p.8)"
  - "GPT-4 and Claude Haiku had high self-consistency (alpha = 0.85 and 0.89); Llama 2 and Gemma lowest (0.37 and 0.41) (p.8)"
  - "LLM cosine similarity with Redditor reasoning: 0.13-0.15, far below inter-LLM range of 0.25-0.40 (p.9)"
  - "Redditors: 76.4% NTA verdicts; Llama 2: 79.2% YTA; Mistral: 39.4% NAH (p.8)"
---
## 1. Gist
Sachdeva & van Nuenen (UC Berkeley, published at FAccT 2025) conduct a large-scale normative evaluation of seven LLMs on 10,826 real-world moral dilemmas from Reddit's "Am I the Asshole" (AITA) community. The study moves beyond survey-style moral questionnaires by using naturally occurring, complex social scenarios where Reddit users have already produced a distributional human baseline of verdicts (NTA/YTA/NAH/ESH/INFO). The paper evaluates inter-model agreement, self-consistency, moral theme invocation, and ensemble behavior. Key findings: LLMs exhibit strikingly distinct verdict distributions from each other and from Redditors; self-consistency is moderate-to-high within models but inter-model agreement is low to negative; an ensemble of LLMs collectively approximates Reddit consensus even when individuals diverge. The paper matters for values-alignment benchmarking by demonstrating that real-world, ecologically valid moral dilemmas reveal alignment failures that structured questionnaires miss, and by providing a large-scale comparison infrastructure with human baselines.

## 2. Benchmark/eval design features
**Stimulus set**: 10,826 AITA posts from Oct 2022–Mar 2023, selected to fall outside model training data, with post score ≥ 25th percentile (score ≥ 25), non-deleted, and minimum 300-character length.

**Task**: Assign one of five verdicts — NTA, YTA, NAH, ESH, INFO — and provide one-paragraph reasoning. System prompt provides verdict definitions taken verbatim from AITA community rules.

**Models evaluated**: GPT-3.5, GPT-4, Claude Haiku, PaLM 2 Bison (API-accessed); Llama 2 7B, Mistral 7B, Gemma 7B (local GPU, HuggingFace weights). All run with default hyperparameters (low but non-zero temperature).

**Replications**: 3 runs per model per post (GPT-4: 2 runs due to cost), enabling self-consistency measurement.

**Moral theme classification**: Six themes from Yudkin et al.'s AITA moral framework — Fairness & Proportionality, Feelings, Harm & Offense, Honesty, Relational Obligation, Social Norms — predicted by fine-tuned RoBERTa-Large classifiers applied to both posts and LLM reasonings.

**Human baseline**: Top-level AITA comments from 476,183 comments across 10,826 posts, providing distributional verdict data per dilemma.

## 3. Task format & example item
Free-text verdict assignment with required explanation. Example from Table 1 (p.4):

"My sister (18f) has social anxiety, and she's just a very awkward person overall. Yesterday, she asked me to go in the store and buy her a plan b because she was too embarrassed. [...] I told her she had to go in and get it herself. [...] AITA?"

Seven different model verdicts are shown: Reddit → YTA; GPT-3.5 → YTA; GPT-4 → NAH; Claude Haiku → NTA; PaLM 2 Bison → NTA; Llama 2 7B → YTA; Mistral 7B → NAH; Gemma 7B → ESH. Full reasoning provided for each.

## 4. Scoring / grading methodology
- **Inter-rater agreement**: Krippendorff's alpha across all model pairs and against Redditors (diagonal = self-consistency from 3 replicated runs).
- **Verdict distribution comparison**: Bar plots of fraction of 10,826 posts assigned each verdict.
- **Ensemble consistency**: For each dilemma, fraction of models voting for each label vs. fraction of Redditor comments using that label (label rate), analyzing sigmoid-shaped relationship.
- **Textual similarity**: TF-IDF cosine similarity between reasoning outputs (3,000 features); word embedding similarity via RoBERTa-Large + UMAP.
- **Moral theme prevalence difference**: For each model and moral theme, the percentage increase in NTA or YTA verdict usage when the model invokes that theme.
- **Cochran-Armitage trend test** for association between number of moral themes and YTA assignment.

## 5. Dataset construction & provenance
Reddit posts via Pushshift.io and PRAW. Filtering: score ≥ 25, non-deleted, non-removed, minimum length. Date range: Oct 2022–Mar 2023. Final dataset: 10,826 posts, 476,183 top-level comments. RoBERTa moral theme classifiers fine-tuned on Yudkin et al.'s 300,000+ labeled AITA corpus (no overlap with evaluation set). Refusal rate in LLM queries: <0.1%.

## 6. Validity evidence
- Self-consistency (diagonal Krippendorff's alpha): GPT-4 = 0.85, Claude Haiku = 0.89 (high); GPT-3.5 = 0.60, PaLM 2 Bison = 0.65 (moderate); Llama 2 = 0.37, Gemma = 0.41 (low).
- Human agreement proxy: GPT-4 best matches Redditors (α = 0.34); Mistral and Llama 2 show negative agreement (systematic disagreement).
- Ensemble NTA/YTA label rate increases monotonically with number of LLM votes, resembling a psychometric sigmoid, supporting construct validity of ensemble measure.
- Moral theme classifiers qualitatively validated on ~100 predictions by authors.
- UMAP visualization shows clear clustering by model identity, with Redditors visibly distinct from all LLMs.

## 7. Saturation / discrimination
The task discriminates strongly across models — verdict distributions span the full range from Llama 2 (79.2% YTA) to PaLM 2 Bison (88.1% NTA). The ensemble analysis shows that 3–5 model agreement is the most informative range (steepest label rate increase), meaning the dataset supports nuanced differentiation rather than ceiling/floor effects. Redditor verdicts (76.4% NTA) provide a human baseline that most models fail to match, preserving headroom for future improvement.

## 8. Multiturn / agentic aspects
n/a — single-turn prompting only. This paper serves as the methodological predecessor to the Sachdeva-Deliberative paper, which extends to multi-turn.

## 9. Key numbers
- Dataset: 10,826 posts; 476,183 comments; 7 models × 3 runs = ~227k verdict–reasoning pairs (p.3–4)
- Redditors: 76.4% NTA, 17% YTA, ~2% each NAH/ESH/INFO (p.8)
- GPT-4: 75% NTA, 12.7% YTA; GPT-3.5: 55.3% NTA, 31.3% YTA; Llama 2: 1% NTA, 79.2% YTA; Mistral: 7.6% NTA, 39.4% NAH (p.8)
- Best human agreement: GPT-4 α = 0.34 (p.8)
- Best self-consistency: Claude Haiku α = 0.89; worst: Llama 2 α = 0.37 (p.8)
- Inter-LLM cosine similarity: 0.25–0.40; LLM vs. Redditor: 0.13–0.15 (p.9)
- Fairness invocation: GPT-4 uses NTA 15% more often when Fairness is invoked (p.11)
- Feelings invocation: Claude uses NTA up to ~30% less when Feelings is invoked (p.11)

## 10. Pitfalls & limitations
- Redditors are demographically unrepresentative (young, male, liberal, English-speaking); human baseline may reflect WEIRD bias, not universal values (p.12).
- Agreement with Redditors does not necessarily mean correct or fair alignment.
- Smaller open-source models used at 7B parameter scale due to GPU constraints; larger versions might behave differently.
- Moral theme classifiers validated on only ~100 samples; no formal IRR reported.
- GPT-4 run only twice (cost); self-consistency estimate less reliable.
- No longitudinal tracking — model versions change; verdicts on same posts might differ with updated checkpoints.
- Study uses Reddit data from before the API restriction (April 2023); future data collection requires alternative methods.

## 11. Novel ideas worth stealing
1. **Distributional human baseline from social media**: Using Redditor comment distributions as a behavioral human baseline provides a richer signal than a single ground-truth label — it captures genuine human disagreement and allows calibration of ensemble LLM behavior.
2. **Ensemble sigmoid analysis**: Plotting average label rate vs. number of LLMs voting for a label reveals a sigmoid that mirrors psychometric item characteristic curves. This suggests LLM ensembles can be calibrated similarly to IRT models.
3. **Self-consistency as a benchmark quality gate**: Models with low self-consistency (α < 0.5) are unreliable benchmark subjects — their variance is dominated by stochasticity, not true value differences. Reporting self-consistency alongside inter-model comparisons should be standard practice.
4. **Moral theme prevalence difference**: Computing the difference in verdict rate when a specific moral theme is invoked vs. not is a simple, replicable way to map model moral sensitivity — analogous to item difficulty in IRT but for themes.
5. **RoBERTa-based moral theme labeling**: Fine-tuning a lightweight classifier on an existing human-annotated corpus to automatically tag moral themes in model outputs enables scalable content analysis of large reasoning corpora.
6. **Ecologically valid stimuli design**: Using real social media dilemmas (rather than constructed vignettes) ensures the benchmark captures the full ambiguity and complexity of everyday moral reasoning, including contextual cues that structured surveys suppress.

## 12. Notable quotes
- "LLMs demonstrate moderate to high self-consistency but low inter-model agreement, suggesting that differences in training and alignment lead to fundamentally different approaches to moral reasoning." (p.1)
- "Despite low inter-model agreement, an ensemble of LLMs can reproduce the consensus judgments of Redditors." (p.1)
- "Our findings that show agreement with the Redditors... do not necessarily suggest successful alignment. Instead, they may serve as further evidence of LLM alignment with Western, Educated, Industrialized, Rich, and Democratic (WEIRD) subpopulations." (p.12)
- "LLMs fundamentally use different language when rendering moral judgment compared to the Redditors." (p.9)

## 13. UNKNOWN / not in extract
- Full system prompt text (referenced in Appendix A but not reproduced in main extract).
- Full UMAP visualizations and details (Figure 4 described but not reproduced in extracted text).
- Appendix E (moral theme vs. verdict analysis by dilemma features).
- Appendix B ensemble voting distribution figures.
- Whether the 10,826-post dataset has been released publicly.
- Exact hyperparameters used for each model API call beyond "low but non-zero temperature."
