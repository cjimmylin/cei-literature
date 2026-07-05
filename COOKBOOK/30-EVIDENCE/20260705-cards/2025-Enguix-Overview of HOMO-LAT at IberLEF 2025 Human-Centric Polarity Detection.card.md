---
stem: "2025-Enguix-Overview of HOMO-LAT at IberLEF 2025 Human-Centric Polarity Detection"
reader_model: "sonnet"
confidence: "high"
is_benchmark: true
theme_tags: [cultural-linguistic, validity-psychometrics, saturation-discrimination, design-space]
task_format: "forced-choice"
scoring_type: "classifier"
dataset_size: 16273
dataset_construction: "scraped"
languages: ["es"]
models_tested: ["RoBERTa", "BETO", "GPT-4o-mini", "RoBERTuito", "MarIA", "BIMALAT", "Mistral-7B", "Falcon-7B"]
headline_numbers:
  - "Best macro F1 Track 1: 0.5296 (PLD team) (p.8)"
  - "Best macro F1 Track 2: 0.5086 (PLD team) (p.8)"
  - "BETO baseline F1 Track 1: 0.3800 (p.8)"
  - "BETO baseline F1 Track 2: 0.3412 (p.8)"
  - "Maximum Possible Accuracy all teams: 0.939 (p.9)"
  - "Fleiss kappa inter-annotator agreement: 0.124 (train), 0.158 (test) (p.6)"
  - "Hateful content (NEG label) in training: 34% (p.6)"
---
## 1. Gist
HOMO-LAT 2025 is a shared task at IberLEF/SEPLN on polarity detection for Spanish-language Reddit posts mentioning LGBTQ+ identity terms, covering 19 Latin American countries. It extends HOMO-MEX 2023/2024 by including posts from all Spanish-speaking countries in the Americas. The task has two tracks: Track 1 (multi-dialect, same countries in train and test) and Track 2 (cross-dialect, test on unseen countries/dialects). The 16,273-post corpus is annotated for positive/negative/neutral polarity toward LGBTQ+ keywords. Six teams participated. Best results peaked at macro F1 ≈ 0.53, with a notable performance drop in cross-dialect Track 2. The work highlights inter-annotator disagreement (Fleiss κ ≈ 0.13–0.16) as a fundamental challenge driven by the subjectivity of polarity toward sensitive social identity terms. For values-alignment benchmarking this paper is relevant as a case study in culturally and linguistically diverse hate/sentiment annotation, with explicit documentation of cross-dialectal generalization failures and annotation subjectivity.

## 2. Benchmark/eval design features
Three-class polarity classification (POS/NEG/NEU) per Reddit post with respect to a highlighted LGBTQ+ keyword. Two evaluation tracks test in-domain vs. cross-domain/dialect generalization. Evaluation metric: macro F1, chosen to handle class imbalance. Corpus construction used neutral identity terms (homosexual, lesbiana, bisexual, etc.) to reduce country-specific lexical variation. Annotation deliberately balanced by LGBTQ+ identity membership, gender, and nationality to capture within-community and cross-community perspectives. Maximum Possible Accuracy (MPA) and Coincident Failure Diversity (CFD) metrics used to assess ensemble complementarity. Statistical significance tested with CompStats library.

## 3. Task format & example item
Each item is a Reddit post paired with a highlighted keyword (one of 12 LGBTQ+ identity terms). Annotators (and models) must assign a single label: POS, NEG, or NEU. The polarity is assessed relative to the keyword, not the post as a whole.

No verbatim example post given in the extract. Example keywords include: asexual, bisexual, gay, intersexual, lesbiana, LGBT, pansexual, queer, trans, transexual, transgénero, travesti (p.3).

## 4. Scoring / grading methodology
Macro F1-score (mean F1 across POS/NEG/NEU classes). This penalizes poor performance on minority classes (POS is only 9–12% of test data). MPA = proportion of instances where at least one system was correct (upper bound for ensemble). CFD = diversity of error patterns across systems (0–1; higher = more independent errors). Statistical significance via CompStats with confidence intervals.

## 5. Dataset construction & provenance
20,215 Reddit posts extracted via Reddit API from country-specific subreddits of 19 Latin American countries. After cleaning (duplicates, bot posts, URL-only posts, irrelevant "trans" uses): 16,273 posts. Argentina (3,724), Mexico (2,824), Chile (2,343), Colombia (1,907) are largest contributors. Train/dev/test split from the top-4 countries for Track 1; Track 2 test from remaining 15 countries. Training: 5,767 posts; Dev: 1,443; Test Track 1: 3,588; Test Track 2: 5,475 (p.4). No explicit license reported.

## 6. Validity evidence
Inter-annotator agreement is very low: Fleiss κ = 0.124 (train), 0.158 (test) (p.6). The authors attribute this to task subjectivity and the large number of annotators (20+) fragmented across sub-corpora. Geographic bias in annotation: Argentina/Mexico/Chile/Colombia used country-matched annotators; remaining 15 countries used Mexican annotators by default. This likely injects cultural annotation bias for the Track 2 test set. The cross-dialect performance drop (PLD: F1 0.5296 → 0.5086) further validates the cultural generalization challenge. No external validity evidence (no comparison to human performance ceilings).

## 7. Saturation / discrimination
All systems cluster in a narrow macro F1 band (0.26–0.53 in Track 1; 0.26–0.51 in Track 2). Best system (PLD) scores only 0.53; all systems significantly underperform the theoretical MPA ceiling of 0.939. Imbalanced class distribution (NEU dominant at 55–64%) systematically disadvantages minority-class detection. The task appears far from saturated.

## 8. Multiturn / agentic aspects
n/a. Single-turn classification of individual Reddit posts.

## 9. Key numbers
- Total corpus after cleaning: 16,273 posts from 19 countries (p.3)
- Training set: 5,767 posts (11% POS, 34% NEG, 55% NEU) (p.6)
- Test Track 1: 3,588 posts; Track 2: 5,475 posts (p.6)
- Best Track 1 macro F1: 0.5296 (PLD) (p.8)
- Best Track 2 macro F1: 0.5086 (PLD) (p.8)
- BETO baseline F1: 0.3800 (Track 1), 0.3412 (Track 2) (p.8)
- MPA all teams: 0.939; Transformers only: 0.928; Traditional ML: 0.732 (p.9)
- CFD all teams: 0.924; Transformers: 0.905; Traditional ML: 0.491 (p.9)
- Fleiss kappa: 0.124 (train), 0.158 (test) (p.6)
- 6 participating teams, 30 registered participants (p.3)
- 12 LGBTQ+ keyword terms (p.3)

## 10. Pitfalls & limitations
- Very low inter-annotator agreement (κ ≈ 0.13–0.16) undermines dataset reliability; the authors attribute this partly to annotator fragmentation across 20+ persons (p.6).
- Track 2 annotation used Mexican annotators for 15 of 19 countries, introducing systematic cultural bias into the test set (p.5).
- Neutral-term focus avoids country-specific slurs but may underrepresent the most harmful content.
- Class imbalance (NEU dominant) makes macro F1 sensitive to minority-class performance.
- Reddit-specific discourse may not generalize to other platforms or text types.
- Only Spanish-language data; findings may not transfer across languages.

## 11. Novel ideas worth stealing
1. **Cross-dialect generalization track**: Explicitly partitioning train vs. test by dialect/region (Track 2) is a clean design for testing robustness to linguistic variety — reusable for any benchmark spanning regional language variants.
2. **Keyword-anchored polarity annotation**: Assigning polarity relative to a highlighted target term (not the whole text) is a precise framing that reduces ambiguity in multi-topic posts. Useful for designing fine-grained values/attitude benchmarks.
3. **Demographic-balanced annotation panels**: Deliberately recruiting annotators who match the community being studied (LGBTQ+ members and non-members; multiple national backgrounds) is a methodologically stronger approach to annotation validity for sensitive topics.
4. **MPA + CFD ensemble analysis**: These two metrics quantify how much more performance is achievable via system combination (MPA) and whether combining systems is likely to help (CFD > 0 = independent errors). Both are cheap to compute and reveal ensemble complementarity.
5. **Senior adjudicator role for disagreements**: Using a dedicated senior annotator to resolve conflicts without exposure to prior annotations is a clean disagreement-resolution protocol applicable to any high-subjectivity annotation task.

## 12. Notable quotes
- "An analysis of inter-annotator agreement yields very poor results... There are two reasons for this. The first is the intrinsic subjectivity of the task... The second is that the corpus was segmented into many fragments for labeling." (p.6)
- "The decline in scores across all teams in Track 2 highlights the increased challenge posed by domain and dialect shift, as the evaluation data included dialects unseen during training." (p.7)
- "One of the volunteers decided to no longer participate in the activity because he felt personally attacked and couldn't continue." (p.5)
- "F1-scores peaking at 0.53 in Track 1 and 0.51 in Track 2... demonstrate the difficulty of transferring sentiment knowledge across dialects." (p.10)

## 13. UNKNOWN / not in extract
- Full per-class F1 breakdown (POS/NEG/NEU) for each team.
- Details of data augmentation size used by the SINAI-UGPLN team (400 synthetic examples mentioned but method details sparse).
- Whether the corpus is released under a public license.
- Exact count of unique annotators per country group.
- Whether any error analysis was done on the cross-dialect failures.
