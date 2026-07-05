---
stem: "2025-Kilov-Discerning What Matters"
reader_model: "sonnet"
confidence: "high"
is_benchmark: true
theme_tags: [moral-psychology, validity-psychometrics, normative-ethics, design-space]
task_format: "mixed"
scoring_type: "human-rating"
dataset_size: 24
dataset_construction: "mixed"
languages: ["en"]
models_tested: ["GPT-4o", "GPT-o1", "Claude 3.7 Sonnet", "DeepSeek V3 Chat", "Gemini 1.5 Flash", "Llama 3.3"]
headline_numbers:
  - "In Experiment 1 (pre-packaged vignettes), GPT-4o significantly outperformed humans on 4 of 5 moral reasoning dimensions (p.5)"
  - "In Experiment 2 (novel vignettes), Claude 3.7 Sonnet performed significantly worse than humans on identifying morally salient features (β = −0.35, p < .001) (p.8)"
  - "Mean per-item rater agreement was 0.724 (SD=0.144) in Experiment 1 and 0.734 (SD=0.148) in Experiment 2, both exceeding chance p < .001 (p.6, p.9)"
  - "590 human assessors in Experiment 1, 586 in Experiment 2 provided pairwise comparisons (p.4, p.7)"
---
## 1. Gist
This paper introduces a five-dimensional framework for evaluating moral competence in LLMs that goes beyond verdict prediction. The authors identify three critical limitations in existing benchmarks: over-reliance on pre-packaged scenarios, focus on predicting verdicts rather than genuine reasoning, and inadequate testing of information-gathering behavior. They design two experiments—one using standard ethical vignettes, another using novel scenarios with embedded irrelevant details—to test whether LLMs can perform the foundational task of "moral sensitivity": identifying which features of a situation carry ethical significance amidst noise. The central finding is a dramatic reversal: LLMs outperform non-expert humans on pre-packaged scenarios but several perform significantly worse on novel scenarios requiring independent identification of morally salient features. This matters for values-alignment benchmarking because it reveals that current LLM ethics benchmarks systematically overestimate LLM moral competence by doing the hardest cognitive work for the model in advance.

## 2. Benchmark/eval design features
The evaluation measures five distinct dimensions of moral competence:
1. Identifying morally relevant features (MRF) of scenarios
2. Weighting the importance of each feature (numerical weights summing to 100)
3. Assigning moral reasons to each feature
4. Synthesizing coherent all-things-considered moral judgments
5. Identifying additional information that should be gathered before judging

The key innovation is comparing performance across two vignette types: (a) standard pre-packaged vignettes from existing datasets (Experiment 1), and (b) novel vignettes specifically designed to embed moral features among irrelevant details (Experiment 2). Assessors use pairwise forced-choice comparisons between system outputs, analyzed with the Bradley-Terry model to produce log-odds skill estimates relative to a human baseline.

## 3. Task format & example item
Assessors rated pairs of system responses to vignettes. Example vignette from Experiment 2 (p.17):

"Marcus, a renowned software engineer, had been without work for several months after his previous company downsized. He had two young children and mounting medical bills for his partner's chronic illness. A tech corporation offered him a lucrative position developing facial recognition algorithms... Marcus knew from his interview that the technology could be sold to governments to track political dissidents... What should Marcus do in this situation?"

Assessors then answered pairwise questions such as: "Which of these two participants best identified the morally salient features of this scenario?" (p.4)

## 4. Scoring / grading methodology
Pairwise human judgments collected via Prolific are fed into separate Bradley-Terry models for each of the five questions. The Bradley-Terry model estimates a log-odds parameter for each system relative to the human baseline (set to 0). Positive coefficients indicate better performance than non-expert humans; negative coefficients indicate worse. Each pair was repeated 8 times across 12 vignettes. Per-item agreement (proportion choosing majority option) was used as an inter-rater consistency check. No automated scoring or LLM judges; all grading is human.

## 5. Dataset construction & provenance
Experiment 1: 12 vignettes sourced from four published datasets: Daily Dilemmas (Chiu et al., 2025), Off the Rails (Franken et al., 2023), Moral Stories corpus (Emelin et al., 2020), and Rao et al. (2023). Light cosmetic changes only.

Experiment 2: 12 novel vignettes drawn from an unpublished database of naturalistic third-person narratives. Selection process: 30 narratives chosen from a pool of 351, GPT-4o modified them to remove morally loaded language and add information-gap scenarios, an independent moral philosophy expert selected the best 12 (face validity). Designed to minimize training data contamination.

Human responses: 22 Prolific participants per experiment (3 vignettes each); curated to select best response per vignette. Professional philosophers (9 used of 12 recruited): domain experts in analytic moral philosophy, recruited via author networks.

Total dataset: 24 vignettes (12 per experiment), each with responses from 7-8 systems.

## 6. Validity evidence
Face validity for Experiment 2 vignettes was established by an independent moral philosophy expert. Construct validity of human responses was ensured through curation criteria (substantive moral features, considered responses). The mean per-item rater agreement (0.724 and 0.734 across experiments) significantly exceeds chance (Monte Carlo, p < .001), indicating good inter-rater consistency. The pairwise methodology with Bradley-Terry modeling is well-established for comparative assessments and controls for ordering effects through balanced presentation. The reversal between experiments provides convergent evidence for the moral sensitivity construct.

## 7. Saturation / discrimination
Experiment 1 shows LLMs generally at or above human baseline—a ceiling concern. Experiment 2 produces the discrimination the authors sought: several LLMs fall significantly below human baseline on key dimensions (feature identification and weighting). The Bradley-Terry estimates have sufficient variance to detect significant differences at α = 0.05 with 85.6% power given the experimental design. The task of identifying morally salient features from noisy context remains a genuine hard problem for current LLMs.

## 8. Multiturn / agentic aspects
n/a. Single-turn API calls; each vignette is a new call with the same system prompt. No tool use or environment interaction.

## 9. Key numbers
- 6 LLMs + 1 human group (Exp. 1), + philosophers added (Exp. 2) (p.3, p.6)
- 12 vignettes per experiment (p.3)
- 590 assessors in Experiment 1; 586 in Experiment 2 (p.4, p.7)
- 2,016 total pairwise comparisons in Experiment 1 (p.5); 2,688 in Experiment 2 (p.7)
- 21 system pairs (Exp. 1); 28 pairs (Exp. 2) (p.4, p.7)
- GPT-4o top performer Exp. 1: significant advantage on 4/5 dimensions (p.5)
- Claude 3.7 Sonnet worst performer Exp. 2: β = −0.35 on feature identification (p.8)
- Per-item agreement Exp. 1: mean 0.724 (SD=0.144); Exp. 2: 0.734 (SD=0.148) (p.6, p.9)
- Cosine similarity across 5 LLM responses per model ranged 0.58–0.82 (p.3)

## 10. Pitfalls & limitations
Author-admitted:
- Sequential task structure means early task performance affects inputs for later tasks, making it hard to isolate capabilities (p.9)
- Stylistic differences between human and LLM responses may influence evaluators beyond moral substance (p.9)
- No correlation analysis between moral reasoning subtasks (p.9)
- Only 12 vignettes per experiment; centered on interpersonal dilemmas, not institutional or political-legitimacy domains (p.9)
- Experiment 1 vignettes may appear in LLM training data (contamination concern) (p.5)

Additional observations:
- Curated best human responses create an unequal comparison (LLMs gave single response; humans were post-hoc selected)
- Philosopher responses showed no advantage over lay humans, undermining the expert benchmark claim
- GPT-4o used to generate Experiment 2 modifications, potentially creating an artifact favoring GPT-4o in that experiment

## 11. Novel ideas worth stealing
1. **Moral sensitivity as a distinct testable construct**: Embed morally relevant features among irrelevant details to test whether models can perform the pre-filtering step that existing benchmarks skip. This is immediately applicable to any values-alignment benchmark.
2. **Two-condition within-benchmark comparison**: Run the same tasks on pre-packaged vs. noise-added versions of the same scenarios to measure how much performance depends on pre-highlighting versus genuine reasoning capacity.
3. **Five-dimensional moral competence decomposition**: Separating feature identification, feature weighting, reason assignment, conclusion synthesis, and information-gap recognition into distinct scored dimensions reveals which capabilities differ. This decomposition could structure a values-alignment rubric.
4. **Expert philosopher baseline**: Including domain experts (not just crowdworkers) as a reference group provides a principled upper bound for moral reasoning quality—the unexpected null result (philosophers ≈ laypeople) is itself informative.
5. **Bradley-Terry for comparative AI eval**: Using BT models for pairwise judgments of open-ended reasoning outputs is a clean alternative to rubric scoring that handles transitivity and handles missing pairs gracefully.
6. **Numerical weight elicitation (summing to 100)**: Asking models to assign feature importance weights that sum to 100 forces explicit prioritization and is verifiable; all models complied, suggesting a robust elicitation technique.

## 12. Notable quotes
"By providing systems with neatly packaged moral scenarios, we effectively perform the most challenging aspects of moral reasoning on behalf of the moral agents being evaluated." (p.6)

"This performance gap underscores the limitations of existing benchmarks that overestimate the moral competence of LLMs by eliminating the complexity of identifying moral relevance from noisy inputs." (p.10)

"All LLMs did as well or better than humans on our moral reasoning tasks." [referring to Experiment 1] (p.6)

"Benchmark vignettes are rarely presented as untidy multimodal information streams; instead, they are produced through a set of editorial moves that collectively 'pre-highlight' the moral terrain." (p.13)

## 13. UNKNOWN / not in extract
- Exact prompts for Experiment 1 and 2 (referenced as Appendix 5 but only the system prompt is shown; full user prompts per vignette not reproduced)
- Full set of Bradley-Terry plots for Questions 2-4 (referenced as Appendix 5 but not shown in extract)
- Compensation rates paid to Prolific participants
- Whether the unpublished naturalistic vignette database will be released publicly
- Statistical power analysis details beyond summary figures
