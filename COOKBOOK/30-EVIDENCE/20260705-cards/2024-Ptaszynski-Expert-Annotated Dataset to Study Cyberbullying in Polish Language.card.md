---
stem: "2024-Ptaszynski-Expert-Annotated Dataset to Study Cyberbullying in Polish Language"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [validity-psychometrics, cultural-linguistic, design-space, normative-ethics]
task_format: "free-text"
scoring_type: "classifier"
dataset_size: 11041
dataset_construction: "scraped"
languages: ["pl"]
models_tested: ["Polbert (bert-base-polish-uncased-v1)", "distilHerBERT", "bert-base-pl-cased", "distilbert-base-pl-cased", "HerBERT", "PolBERTa", "TrelBERT", "ULMFiT/fast.ai", "Przetak", "SVM", "fasttext", "GRU", "Flair"]
headline_numbers:
  - "11,041 Polish tweets collected from Twitter; 10,041 training / 1,000 test split (p.4)"
  - "Layperson inter-annotator agreement: Kappa ≈ 0.325–0.378 (fair) (p.12)"
  - "Expert inter-annotator agreement: Kappa 0.451–0.517 (moderate), nearly doubling harmful label counts vs. laypeople (p.20)"
  - "Best Task 1 F1 (binary): 58.58% by n-waves ULMFiT (p.18)"
  - "Best Task 2 micro-F (3-class): 87.60% by SVM on re-annotated data (p.19)"
  - "Expert re-annotation found twice as many harmful labels as layperson annotations (p.20)"
---
## 1. Gist
This data descriptor introduces the first publicly released expert-annotated dataset of cyberbullying and hate speech in Polish, based on 11,041 tweets collected from major Polish Twitter accounts in 2018. The dataset exists in two versions: an original version annotated by trained laypersons under expert oversight, and an improved v2 re-annotated by a team of experienced cyberbullying annotation specialists. The paper documents data collection, preprocessing, annotation protocols, inter-annotator agreement, and baseline classification results. It matters for values-alignment benchmarking because it exemplifies the methodological gap between layperson and expert annotation for subtle harms, demonstrates class imbalance challenges for low-prevalence harmful content, and provides a rare non-English (Polish-language) resource for studying online harm detection in a morphologically complex Slavic language with politically polarized content.

## 2. Benchmark/eval design features
Two classification tasks are defined on the same dataset:
- **Task 1 (binary):** harmful vs. non-harmful; evaluation metrics: Precision, Recall, F1, Accuracy.
- **Task 2 (3-class):** non-harmful (0), cyberbullying (1), hate speech (2); evaluation: micro-F and macro-F.

The key distinction between cyberbullying and hate speech is operational: cyberbullying targets a private individual or small group; hate speech targets public figures or broad communities. This is a decade-long definitional framework from the lead author's prior research.

Annotation categories include: phishing/private-info disclosure, personal attack, threats, blackmail, mocking/ridiculing, gossip/insinuations, accumulation of profanity, and combinations thereof (Tables 1 and 2, pp.7–8). Each tweet also carries a "specific phrase" annotation identifying harmful text spans.

## 3. Task format & example item
Annotators classify individual tweets (provided as plain text without conversation context) into: 0 = non-harmful, 1 = cyberbullying, 2 = hate speech. Example from Table 3 (p.9):

> Polish: "Ty si˛e oszu´scie i kłamco od nas odpierdol. My sobie damy rad˛e bez twoich kłamstw"
> English: "Fuck off you cheat and liar. We can do without your lies"
> Score: 2 (hate speech); Specific tags: atk, wul, atk; Harmful phrases: "oszu´scie", "kłamco", "odpierdol si˛e"

Non-harmful control example (p.9):
> Polish: "WISŁA KRAKÓW !! brawo za dzisiejszy mecz :)"
> English: "WISLA KRAKOW [soccer team name] !! Bravo for today's match :)"
> Score: 0

## 4. Scoring / grading methodology
Binary classification (Task 1): standard P, R, F1, Accuracy. Winner = highest F1; ties broken by accuracy, then proximity to precision-recall break-even point.

Multi-class (Task 2): micro-F (weighted by instance count) and macro-F (equal class weighting). Winner = highest micro-F; ties resolved by macro-F. Non-standard calculation: macro-F and micro-F are computed via separately averaged precision and recall rather than averaging class-level F-scores, to reveal P-R balance at each level (pp.15–16).

Inter-annotator reliability uses a modified weighted Cohen's Kappa with quadratic weights where 0-1 and 0-2 disagreements are penalized more severely than 1-2 disagreements, reflecting the greater conceptual distance between harmful and non-harmful than between the two harm types (p.12, Table 6).

## 5. Dataset construction & provenance
Tweets were collected via the Twitter API in late 2018 from 19 prominent Polish public accounts plus responses, yielding 23,223 tweets. After preprocessing (removing URLs, exact duplicates, @/# only tweets, tweets < 5 words, non-Polish tweets), 11,041 tweets remained: 10,041 training, 1,000 test. Tweets are from private reply accounts (not the prominent accounts themselves) to focus on cyberbullying of private individuals. Two versions are released: v1 (layperson-annotated) and v2 (expert re-annotated). Anonymized versions are provided for both. The dataset also includes the best-performing Polish BERT classification model (bert-base-polish-cyberbullying). Available on HuggingFace and described in the MDPI Data journal.

## 6. Validity evidence
Two annotation rounds provide a natural validity comparison. Layperson Kappa ≈ 0.325–0.378 (fair agreement), driven largely by high agreement on the dominant non-harmful class (89.76% of tweets). Experts achieved 0.451–0.517 (moderate agreement), with all three experts agreeing on 80.58% of cases and no case of full three-way disagreement (p.20). The expert v2 re-annotation found twice as many harmful labels, suggesting layperson annotation systematically misses approximately half of harmful cases. The authors explicitly frame this as validating the need for domain-expert annotators for cyberbullying-class tasks (p.20). TF-IDF feature analysis confirms that top harmful-class tokens are slurs, vulgarities, and politically-coded insults — not generic content (p.11, Table 5).

## 7. Saturation / discrimination
Heavy class imbalance: non-harmful = ~83–87% of samples in both versions; cyberbullying = 2.5–14% depending on version and split; hate speech = 5–11%. This means all-zero baselines achieve 86.6% accuracy on Task 1 but F1 = 0 for the harmful class — demonstrating that accuracy is a misleading metric for this domain (p.17, Table 8). The best Task 1 result is F1 = 58.58%, indicating the task remains far from saturated. Expert re-annotation shifts class balance meaningfully (CB from 2.5% to ~13.9% in test set), showing annotation quality substantially affects benchmark difficulty.

## 8. Multiturn / agentic aspects
n/a — single-tweet classification with no conversational context. Authors explicitly identify the lack of conversation threading as a limitation and flag it as future work (p.12–13).

## 9. Key numbers
- 23,223 tweets initially collected; 11,041 retained after preprocessing (p.4)
- Training: 10,041; Test: 1,000 (p.4)
- Overall layperson annotator agreement rate: 91.38% (predominantly from non-harmful majority) (p.9)
- Layperson Kappa: 0.325 (standard), 0.329 (weighted), 0.378 (modified quadratic) (p.12)
- Expert Kappa: 0.451 (standard), 0.517 (weighted), 0.495 (modified quadratic) (p.20)
- Expert re-annotation: harmful increased from 8.92% (v1) to 16.04% (v2) (p.20, Table 13)
- Best Task 1 F1: 58.58% (n-waves ULMFiT), P = 66.67%, R = 52.24%, A = 90.10% (p.18)
- Best Task 2 micro-F: 87.60% (SVM with LEMSNERS features) (p.19)
- 14 teams submitted to Task 1; 8 to Task 2 (p.16)
- Baseline always-predict-0 Task 1 F1 = 0 despite 86.60% accuracy (p.17)

## 10. Pitfalls & limitations
- **Context missing**: Each tweet treated in isolation due to Twitter API limitations; conversation threading would substantially improve annotation quality and model performance (p.12–13).
- **Temporal snapshot**: Data collection ended November 2018; does not capture more recent linguistic patterns or political events.
- **Class imbalance**: Strong non-harmful majority inflates accuracy metrics and suppresses F1 for rare harmful classes. Researchers must use macro-F over accuracy.
- **Private-account scope only**: Public figures' tweets excluded by design, limiting generalizability to public discourse.
- **Annotation subjectivity**: Even expert annotators only reached moderate agreement (Kappa ≈ 0.5), indicating inherent ambiguity, especially for contextually dependent cases (p.12–13).
- **Polish-only, European political context**: The dataset reflects specific Polish political polarization dynamics (left/right framing, named political figures); generalization to other languages or political systems requires caution.
- **Feature engineering gap**: All participating Task 2 teams used primarily lexical features; POS, named entities, and semantic features remained unexplored (p.18).

## 11. Novel ideas worth stealing
1. **Two-round annotation design (layperson + expert re-annotation)**: Running a full expert re-annotation pass on top of layperson annotations and publishing both versions as v1/v2 is a powerful quality ladder that lets researchers study the effect of annotation expertise on label quality and model performance. This design is directly transferable to values-alignment datasets where "harmful" or "misaligned" is a matter of expert judgment.
2. **Modified quadratic Kappa for ordered multi-class harm**: The custom inter-annotator agreement weighting (treating non-harmful as categorically different from both harm types, but treating the two harm types as closer to each other) is a principled move for any ordered multi-class annotation schema. Directly applicable to values-alignment annotations with tiered severity.
3. **Explicit harmful-phrase span annotation alongside class label**: Requiring annotators to mark specific harmful phrases (not just tweet-level labels) provides span-level training signal and interpretability data. For values-alignment benchmarks, requiring annotators to mark the specific sentence or phrase that triggered a judgment would improve downstream model analysis.
4. **Dual-metric reporting with break-even analysis**: The custom micro-F/macro-F derivation (separately averaging P and R before combining) provides more diagnostic information than standard F-scoring when class imbalance is severe. For low-frequency value violations in a larger evaluation set, macro-F with explicit P-R reporting is essential.
5. **TF-IDF feature audit as a validity check**: Reporting top-scoring tokens per class via TF-IDF as a sanity check (harmful class should have slurs, non-harmful class should have sports terms) is cheap and communicative. A values-alignment dataset could run the same check to verify that annotated examples reflect intended constructs rather than spurious correlates.

## 12. Notable quotes
- "Expert annotation is required [for cyberbullying tasks]... when the annotation is entrusted to laypeople, half of the cyberbullying cases will be lost due to annotator mistakes or insufficient training." (p.20)
- "The annotators often identified that the semantic nuances of the majority of tweets were contextually dependent. When contextual clarity was lacking, the assessment of these tweets within the designated categories—particularly the harmful category—proved challenging." (p.13)
- "Although the utilization of explicit language ('kurwa') might suggest a robustly offensive tone, the phrase inherently lacks any indication of harmful conduct." (p.13)
- "The dataset exhibits an imbalance in class distribution... Baseline A (constant value of 0) yielded an F1 score of 0, a foreseeable outcome, confirming that it is not possible to consider the problem as too simple." (p.17)

## 13. UNKNOWN / not in extract
- Full classification results for all transformer models (Polbert, HerBERT, PolBERTa, TrelBERT, etc.) on the re-annotated v2 dataset are in Table 16 and beyond (pages beyond p.21 not fully read in extract).
- Detailed demographic breakdown of re-annotation team's annotation disagreement patterns.
- Specific release license for the dataset and model weights.
- Whether any data augmentation was applied for class balancing in the transformer experiments.
- Whether the expert annotators annotated completely independently or had access to v1 labels during re-annotation.
