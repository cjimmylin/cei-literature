---
stem: "2021-Wang-MedAI at SemEval-2021 Task 5"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [best-practices, validity-psychometrics]
task_format: "free-text"
scoring_type: "exact-match"
dataset_size: 9629
dataset_construction: "crowdsourced"
languages: ["en"]
models_tested: ["RoBERTa-base-squad2", "twitter-RoBERTa-base-sentiment", "DistillRoBERTa-base"]
headline_numbers:
  - "Final ensemble F1=69.03%, placing top-10 among ~100 teams (p.4)"
  - "Top 1 system F1=70.83%, top 2 F1=70.77% (p.1)"
  - "Training set: 7,939 posts (7,454 with spans, 485 without); test set: 2,000 posts (p.3)"
  - "Custom distance loss + cross-entropy ensemble: F1=0.6754 (vs. cross-entropy alone 0.6662) (p.4)"
---
## 1. Gist
This is a system description paper from SemEval-2021 Task 5: Toxic Spans Detection, where the goal is to identify the specific character-offset spans within a post that make it toxic — rather than merely classifying the whole post. The MedAI team developed a start-to-end tagging framework on top of RoBERTa, combined with a custom distance loss that penalizes predictions far from the true span boundary, and a voting ensemble of three RoBERTa variants. For values-alignment benchmarking, this paper is relevant because span-level toxicity localization is a step toward explainable harm detection: it forces operationalizing not just "is this harmful?" but "which words cause the harm?"

## 2. Benchmark/eval design features
The paper describes a system rather than a benchmark. The task (SemEval 2021 Task 5) targets:
- **Construct measured**: Toxic spans — character offsets of the words/phrases that make a post toxic.
- **Item structure**: Each post has a list of character-offset indices marking toxic spans (possibly empty if no spans detectable).
- **Answer space**: Sets of character offsets for each post.

The evaluation metric is character-offset F1, averaged across all posts. Posts with no gold spans score F1=1 only if the system predicts no spans, F1=0 otherwise (p.3).

## 3. Task format & example item
Given a post, predict the set of character offset indices corresponding to toxic spans (p.4):

```
Text: "good side of trump? are you kidding me? trump has no good side all bad, he is 
divisive, a racist and bigot, pathological liar, scammer, tax cheat, sexual pervert,"

Golden Spans: ['pathological liar', 'scammer', 'sexual pervert']
RoBERTa-base-squad2: ['racist', 'scammer', 'sexual pervert']
```

## 4. Scoring / grading methodology
Character-offset F1 per post, then averaged across all posts (p.3). The formula computes intersection of predicted and gold span character sets divided by their sizes. Posts with empty gold spans: F1=1 if system also predicts empty, F1=0 otherwise. This is token-overlap F1 operating at character level.

## 5. Dataset construction & provenance
SemEval 2021 Task 5 dataset (Pavlopoulos et al., 2021) — not constructed by this paper. Statistics as used (p.3, Table 1):
- Trial: 690 posts (647 with spans, 43 without)
- Train: 7,939 posts (7,454 with spans, 485 without)
- Test: 2,000 posts (1,606 with spans, 394 without)

5-fold cross-validation on official training data only (p.3). Source of posts not specified in this extract; the task description paper indicates they are from online forums/social media (Pavlopoulos et al., 2021).

## 6. Validity evidence
The paper does not discuss construct validity, human baselines, or inter-rater reliability — it is a system paper, not a dataset paper. Model comparison provides implicit evidence: span detection performance varies by encoder (DistillRoBERTa-base 0.6754, RoBERTa-base-squad2 0.6793, twitter-RoBERTa-base-sentiment 0.6742), suggesting the task is sensitive to training domain (squad-based reading comprehension helps).

## 7. Saturation / discrimination
Best submitted system F1=70.83%, MedAI achieves 69.03% — gap to ceiling is small (~1.8%). The field appears to be converging near 70% F1. It is unclear whether higher is achievable or whether inter-annotator disagreement on what counts as "toxic spans" limits the ceiling. The paper notes its final F1 is "slight lower" than top-2, ranking in top-10 of ~100 teams (p.1).

## 8. Multiturn / agentic aspects
n/a — single-post, single-pass span extraction.

## 9. Key numbers
- Training set: 7,939 posts (p.3)
- Test set: 2,000 posts (p.3)
- Final system F1: 69.03% (p.1, p.4)
- Top-1 F1: 70.83%, Top-2 F1: 70.77% (p.1)
- Cross-entropy baseline (variant 1): 0.6662 (p.4)
- Label smoothing loss (variant 2): 0.6347 (p.4)
- KL divergence loss (variant 3): 0.6618 (p.4)
- Custom distance + cross-entropy model: 0.6754 (p.4)
- RoBERTa-base-squad2 best single encoder: 0.6793 (p.4)
- Approximately 100 participating teams (p.4)

## 10. Pitfalls & limitations
- Distance loss target assigned manually; may have low generalization to other datasets (p.5)
- The ensemble voting threshold (majority among 3 encoders) is heuristic
- No analysis of where the model fails (span boundaries? highly implicit toxic language?)
- The paper is a short system description; no ablations beyond loss function variants and encoder choice
- Character-offset F1 is sensitive to tokenization artifacts and off-by-one boundary predictions

## 11. Novel ideas worth stealing
1. **Start-to-end tagging for span boundary detection**: Rather than BIOES tagging (which multiplies classes), predict start probability and end probability for each token independently. This is simpler and handles multi-span cases without class explosion — reusable for value-harm localization tasks.
2. **Custom distance loss for span boundaries**: A loss that penalizes predictions proportional to distance from the true boundary position, not just binary hit/miss — could be adapted for any task where partial credit for "close" predictions is desirable.
3. **Domain-matched encoder selection**: Using RoBERTa-base-squad2 (reading comprehension-trained) outperforms twitter-sentiment RoBERTa on this span extraction task — evidence that task-type domain matching matters more than topic domain matching. Useful heuristic for benchmark practitioners choosing base models.

## 12. Notable quotes
- "Highlighting such toxic spans can assist human moderators (e.g., news portals moderators) who often deal with lengthy comments, and who prefer attribution instead of just a system-generated unexplained toxicity score per post." (p.1)
- "The distance loss target is assigned manually, which may have low generalization ability to different data set and task." (p.5)
- "Complementing and correcting each other may improve the overall performance due to the difference." (p.4)

## 13. UNKNOWN / not in extract
- Source platform and annotation methodology for the SemEval 2021 Task 5 dataset
- Inter-annotator agreement on toxic span boundaries
- Human baseline performance on this task
- Whether span annotations distinguish explicit vs. implicit toxicity
- Number of spans per post in the dataset
- What "negative" indicator appended to posts does mechanically (mention in p.1 but not analyzed in ablation)
