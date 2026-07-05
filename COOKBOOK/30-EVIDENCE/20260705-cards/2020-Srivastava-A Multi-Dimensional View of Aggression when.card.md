---
stem: "2020-Srivastava-A Multi-Dimensional View of Aggression when"
reader_model: "sonnet"
confidence: "high"
is_benchmark: true
theme_tags: [cultural-linguistic, validity-psychometrics, design-space, moral-psychology]
task_format: "mixed"
scoring_type: "classifier"
dataset_size: 1001
dataset_construction: "crowdsourced"
languages: ["hi", "en"]
models_tested: []
headline_numbers:
  - "Fleiss's kappa for stance annotation: 0.84 (p.5)"
  - "Fleiss's kappa for aggression annotation: 0.62 (p.5)"
  - "Fleiss's kappa for hate speech annotation: 0.47 (p.5)"
  - "Spearman correlation for emotion arousal across annotator pairs: average 0.65 (p.5)"
  - "1001 Hindi-English code-mixed tweets annotated across 6 dimensions (p.2)"
---
## 1. Gist
This paper presents a multi-dimensional annotated dataset of 1,001 Hindi-English code-mixed tweets on the 2016 Indian banknote demonetisation, annotated across six dimensions: stance (favourable/against/neutral), aggression (overt/covert/non-aggressive), hate speech, figurative language (sarcasm/irony/rhetorical questions, puns/word-play, metaphors/similes), and emotion arousal (1-5 scale). It is the first attempt to analyze social media opinion across aggression and figurative language dimensions simultaneously on a single corpus. For values-alignment benchmarking, the work demonstrates how multi-label annotation of a single text across correlated ethical dimensions (aggression, hate, stance) reveals interaction effects invisible to single-task datasets — and demonstrates design patterns for capturing culturally situated political discourse in non-English/code-mixed contexts.

## 2. Benchmark/eval design features
The dataset enables multi-task classification across six binary or multi-class dimensions on the same 1,001 tweets:
- Stance: 3-class (favourable/against/neutral), re-annotated to capture indirect stance
- Aggression: 3-class (overt/covert/non-aggressive) following Kumar et al. (2018) guidelines
- Hate speech: binary
- Sarcasm/irony/rhetorical questions: binary
- Puns/word-play: binary
- Metaphors/similes: binary
- Emotion arousal: 5-point ordinal scale (1=very low to 5=very high)

The paper's core finding is that these dimensions are correlated: minority-stance speakers use more covert aggression and figurative language (especially sarcasm), while majority-stance speakers show more overt aggression and higher emotion arousal.

## 3. Task format & example item
Multi-label annotation task on tweets. Three domain expert annotators per dimension.

Example items (p.1-2):
- Tweet 1 (overt aggression, hate speech, word-play, favourable stance): "ye AAPtards aise behave kar rahe hain jaise Modi ji ne Notebandi nahi inki Nassbandi kara di ho" — "These AAPtards are behaving as if its not demonetisation but castration for them." [Uses the slur "AAPtards" and rhymes "Notebandi"/"Nassbandi"]
- Tweet 4 (sarcasm, neutral stance, non-aggressive): "what if .. Modi Ji says Mitron ,,, kal raat ko zyada ho gayi thi ,,. Kuch nahi badla he.. #NoteBandi" — "What if Modi says that he had too much to drink last night and nothing has really changed."

## 4. Scoring / grading methodology
Final label per binary dimension = majority vote of 3 annotators. For 3-class aggression, adjudication was provided for non-majority cases. Emotion arousal = average of 3 annotator scores. Inter-annotator agreement measured by Fleiss's kappa for categorical tasks and Spearman's rank correlation for ordinal emotion arousal.

## 5. Dataset construction & provenance
Base dataset: 3,500 Hindi-English tweets collected by Swami et al. (2018b) using Twitter Scraper API with keywords "notebandi" and "demonetisation" over 6 months after the November 2016 announcement. 1,001 tweets randomly sampled from this pool and re-annotated by 3 domain expert annotators (Indian socio-political context experts). Originally annotated for stance only; this paper adds 5 additional annotation dimensions. Dataset is publicly available at github.com/arjitsrivastava/MultidimensionalViewOpinionMining. The paper plans to extend to all 3,500 tweets.

## 6. Validity evidence
Fleiss's kappa scores (Table 3, p.5):
- Stance: κ=0.84 (high, due to clear political polarisation)
- Aggression: κ=0.62 (moderate-substantial)
- Hate Speech: κ=0.47 (moderate; hardest dimension, reflecting definitional ambiguity)
- Sarcasm/Irony/Rhetorical Questions: κ=0.61
- Puns/Word-play: κ=0.72
- Metaphors/Similes: κ=0.65

Spearman correlation for emotion arousal: average 0.65, all pairs statistically significant (p<<0.005; Table 4, p.5). The authors note that hate speech has the worst agreement because of ambiguity between targeted personal attacks and group-directed hate speech.

## 7. Saturation / discrimination
Dataset is skewed toward favourable stance (583/1001 tweets), which limits analysis for minority stance categories. Hate speech instances are very sparse (29 total; Table 2, p.5), constraining analysis. Covert aggression (264) exceeds overt (140), suggesting the dataset has richer signal for subtle phenomena. Figurative language is moderately represented: 163 sarcasm, 140 word-play, 189 metaphor. No classifier performance numbers are reported (dataset paper only, no models trained).

## 8. Multiturn / agentic aspects
n/a — single-tweet classification task.

## 9. Key numbers
- Total annotated tweets: 1,001 (p.2)
- Favourable stance: 583; Against: 180; Neutral: 238 (Table 2, p.5)
- Overt aggression: 140; Covert: 264; Non-aggressive: 597 (Table 2, p.5)
- Hate speech (true): 29 (Table 2, p.5)
- Sarcasm/Irony/Rhetorical Q: 163 (Table 2, p.5)
- Puns/Word-play: 140; Metaphors/Similes: 189 (Table 2, p.5)
- Fleiss's kappa ranges: 0.47 (hate speech) to 0.84 (stance; Table 3, p.5)
- Emotion arousal Spearman r average: 0.65 (Table 4, p.5)
- Average tokens per tweet: 21.1 (Table 1, p.5)
- Average Hindi tokens: 16.9; average English tokens: 1.0 (Table 1, p.5)
- Tweets with discernible code-mixing (3+ English words): 119 (p.5)

## 10. Pitfalls & limitations
- Strong topic specificity: the dataset covers only a single political issue (Indian demonetisation 2016), limiting generalisability to other topics or cultures.
- Class imbalance: hate speech is very sparse (29 instances), making it difficult to train or evaluate models on this dimension.
- Code-mixing makes the data challenging for standard NLP pipelines; most tweets are predominantly Hindi in Roman script, not true bilingual mixing.
- Annotator familiarity with the political issue may bias annotations — what counts as covert aggression depends on in-group knowledge.
- No baseline model performance is reported; the paper is purely a corpus introduction.
- Re-annotation of the original stance dataset may introduce disagreements with the original labels, which are not systematically analysed.

## 11. Novel ideas worth stealing
- **Multi-dimensional joint annotation on a single corpus**: Annotating the same tweet for stance, aggression (overt/covert), hate speech, multiple figurative language types, and emotion arousal simultaneously enables discovery of cross-dimension interactions that single-task datasets miss. Values-alignment benchmarks could adopt this paradigm.
- **Overt vs. covert aggression as a difficulty gradient**: The overt/covert distinction (direct insult vs. sarcasm/rhetorical question) creates a natural difficulty gradient for detecting social harm that is relevant to evaluating LLM moral sensitivity.
- **Majority-stance vs. minority-stance analysis**: The finding that minority-stance speakers use more covert aggression and figurative language (Tables 5–8) is a sociolinguistic insight worth incorporating into benchmark design — social position predicts rhetorical strategy.
- **Code-mixed text as a stress test for values evaluation**: Using Hindi-English code-mixed social media data tests whether moral/offense detection systems work outside clean English, which is important for global deployment of values-aligned AI.
- **Expert annotators with domain knowledge**: Using annotators who are experts in the socio-political context (rather than generic crowdworkers) is appropriate for politically sensitive or culturally specific content; relevant for designing culturally grounded values benchmarks.
- **Emotion arousal as a continuous moral signal**: Separate measurement of emotion arousal (intensity) from valence is a useful design principle for benchmarks that aim to distinguish distress from mere displeasure.

## 12. Notable quotes
- "While research has been focused largely on analyzing aggression and stance in isolation from each other, this work is the first attempt to gain an extensive and fine-grained understanding of patterns of aggression and figurative language use when voicing opinion." (p.1)
- "It is not difficult to hypothesise that holding a majority stance on issues will lead to open bullying in a lot of cases. Users in minority tend to be more covert to possibly avoid being bullied by the majority group." (p.6)
- "Covert aggression is expressed through figurative language like sarcasm and puns." (p.6)
- "The higher percentage of lowest arousal state tweets when against the issue must also be noted. These lowest arousal tweets correspond to emotions like depression and sadness." (p.7)

## 13. UNKNOWN / not in extract
- Whether baseline classifiers were trained and evaluated; the paper explicitly defers this to future work.
- The specific annotation guidelines used for each of the six dimensions (only aggression guidelines are described in detail, referencing Kumar et al. 2018).
- Demographic information about the 3 annotators.
- Whether the original stance labels from Swami et al. (2018b) were retained or fully replaced.
- License for the dataset.
- Whether the extension to 3,500 tweets and named entity/emotion annotation has been completed.
