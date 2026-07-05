---
stem: "2019-Jikeli-Annotating Antisemitic Online Content Towards an"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [validity-psychometrics, cultural-linguistic, normative-ethics, best-practices]
task_format: "n/a"
scoring_type: "human-rating"
dataset_size: 419
dataset_construction: "scraped"
languages: ["en"]
models_tested: []
headline_numbers:
  - "12–18% of 'Jew*' tweets classified antisemitic/probably antisemitic depending on annotator (p.12)"
  - "11–14% of 'Israel' tweets classified antisemitic/probably antisemitic (p.12)"
  - "15–19% of 'Jew*' tweets calling out antisemitism (p.12)"
  - "Raw dataset: 11,300,747,876 tweets in 2018 10% random sample (p.5)"
  - "3,427,731 tweets with 'Jew*' from 1,460,075 distinct users in 2018 (p.5)"
---
## 1. Gist
This paper describes a methodology for annotating antisemitic content in Twitter data using the International Holocaust Remembrance Alliance (IHRA) Working Definition of Antisemitism. The authors draw on a 10% random sample of all public tweets from 2018, extract keyword-filtered subsets ("Jew*" and "Israel"), and manually annotate two random samples of 400 tweets each using a trained team of graduate students. The paper is primarily a methodology paper arguing that antisemitic content requires a domain-specific annotation scheme that goes beyond generic hate-speech frameworks, and that the IHRA definition, when carefully elaborated with explicit inferences, is workable for this purpose. It is important for values-alignment benchmarking because it documents the practical challenges of building high-quality labeled corpora for targeted, subtle hate speech: inter-annotator disagreement, the need for deep domain knowledge, the difficulty of distinguishing antisemitic content from calls against antisemitism, and the limits of keyword-based data collection.

## 2. Benchmark/eval design features
Not a benchmark. The paper's core contribution is an annotation process and schema for labeling antisemitic tweets. Key design elements:
- Uses the IHRA Working Definition with added inferences spelled out in Annex II.
- Five-point antisemitism scale: -2 (confident antisemitic), -1 (probably antisemitic), 0 (incomprehensible), +1 (probably not), +2 (confident not antisemitic).
- Separate five-point sentiment scale toward Jews/Israel/Judaism (-2 to +2).
- Additional flags: deleted tweet, foreign language, annotator disagrees with IHRA definition.
- Focus on impact of message rather than intent of sender.
- Annotators inspect embedded links, images, user profiles, and prior tweet context.
- Two annotators per sample, each working independently before cross-comparison.
- Average annotation time approximately 2 minutes per tweet (p.9).

Core claims: (1) Generic hate-speech definitions under-capture nuanced antisemitism; (2) the IHRA definition, with elaborations, is applicable to social media if inferences are explicit; (3) highly trained expert annotators are superior to many less-qualified annotators for this task; (4) context (threading, user profile, embedded media) is essential for correct classification.

## 3. Task format & example item
Not an LLM benchmark; no standardized item format is presented. The annotation task was: human coders read tweets in context, then assigned scores on antisemitism and sentiment scales.

Example of an ambiguous tweet discussed (p.13): "@realMatMolina @GothamGirlBlue There is a large Jewish population in the neighborhood and school" — classified differently by the two annotators due to difficulty reading the thread context.

## 4. Scoring / grading methodology
Human annotation on two independent five-point scales (antisemitism, sentiment toward Jews/Judaism/Israel). Majority voting was not used — only two annotators per sample; disagreements are presented and discussed qualitatively. No formal inter-annotator reliability metric (e.g., Cohen's kappa) is reported in the main text, though the authors note that different interpretations of context and the IHRA definition drove most disagreements. Resolution relied on discussion and clarification of inferences in Annex II.

## 5. Dataset construction & provenance
- Raw source: 10% random sample of all public tweets via Twitter Streaming API (Indiana University OSoMe).
- Year: 2018.
- Full raw set: ~11.3 billion tweets; filtered to those containing "Jew*" (3.4M) or "Israel" (2.98M).
- Annotated samples: 400 tweets each for "Jew*" and "Israel" queries, drawn via DMI-TCAT randomization.
- After removing deleted tweets, foreign-language tweets, and jewelry-related tweets: 172 "Jew*" and 247 "Israel" tweets annotated in the reported samples (p.12).
- Corpus not released as gold standard; paper treats it as preliminary.
- No formal licensing or contamination-control discussion.

## 6. Validity evidence
No formal validity analysis. The authors discuss face validity of the IHRA definition for social-media contexts and describe qualitative case studies of ambiguous tweets to demonstrate how their elaborated inferences function. No human baseline beyond the two annotators per sample. No IRR coefficients reported.

## 7. Saturation / discrimination
Not applicable — this is not a benchmark with items calibrated for difficulty. The annotation results suggest that antisemitism is unevenly distributed: 12–18% of "Jew*" tweets and 11–14% of "Israel" tweets were scored as (probably) antisemitic, leaving substantial headroom. A comparably large fraction (15–19%) of "Jew*" tweets was classified as calling out antisemitism, showing the dataset contains a mix of very different content types that require fine discrimination.

## 8. Multiturn / agentic aspects
n/a

## 9. Key numbers
- Raw tweet corpus 2018: 11,300,747,876 tweets in 10% random sample (p.5)
- "Jew*" tweets: 3,427,731 from 1,460,075 users (p.5)
- "Israel" tweets: 2,980,327 from 1,101,373 users (p.5)
- Annotated "Jew*" sample (live tweets only): 172 (p.12)
- Annotated "Israel" sample (live tweets only): 247 (p.12)
- "Jew*" antisemitic/probably antisemitic: Annotator B 18%, Annotator G 12.2% (p.12)
- "Israel" antisemitic/probably antisemitic: Annotator D 14.3%, Annotator J 10.5% (p.12)
- Calling out antisemitism in "Jew*" sample: 14.5–18.5% (p.12)
- Calling out antisemitism in "Israel" sample: 2.1–6.2% (p.12)
- Mean annotation time: ~2 minutes per tweet (p.9)
- Margin of error for n=172: ±6%; for n=247: ±5% (p.12)

## 10. Pitfalls & limitations
- Very small annotated samples (172 and 247 live tweets) with only two annotators each — no statistical reliability.
- No inter-annotator reliability metric computed or reported.
- Deleted tweets excluded even though they may be disproportionately antisemitic (p.12).
- Sampling gap in July 2018 (only 1% of tweets) required special handling and introduced bias.
- Only English-language tweets analyzed, yet Twitter antisemitism is multilingual.
- Keyword-based sampling misses antisemitism not containing "Jew" or "Israel" and over-samples certain topics.
- Annotators' different levels of contextual knowledge (e.g., MEMRI tweets) drove disagreements, suggesting results depend heavily on annotator expertise.
- No gold standard released; methodological paper only.

## 11. Novel ideas worth stealing
- **Intent-vs-impact distinction**: scoring a message on its likely interpretation by readers, not on inferred sender intent — directly applicable to LLM output evaluation where model "intent" is opaque.
- **Explicit inference annex**: appending a detailed elaboration of definitional grey zones to annotation guidelines substantially reduced inter-annotator disagreement in pilot rounds; benchmark designers should write similar inference documents for contested moral constructs.
- **Dual-scale coding**: separate scales for the target construct (antisemitism) and a correlated but distinct dimension (sentiment) allow cross-validation and help annotators avoid conflating different phenomena. Analogously, values-alignment benchmarks could separate "model endorses X" from "model tone is hostile about X."
- **Annotator disagreement log as design input**: qualitative documentation of every disagreement case drove refinement of the definition — a useful practice for iterative benchmark development.
- **Calls-against as a distinct category**: flagging tweets that *denounce* the harmful content (rather than only content that expresses it) enables measuring false-positive rates from context-free keyword matching. Values benchmarks could similarly code refusals or meta-commentary as a separate label.
- **Expert vs. crowd annotators**: the paper argues for small teams of highly trained annotators over large crowds for subtle, culturally-dependent content; relevant for benchmarks evaluating subtle moral distinctions.

## 12. Notable quotes
- "We argue that antisemitic content has distinct features that are not captured adequately in generic approaches of annotation, such as hate speech, abusive language, or toxic language." (p.1)
- "We look at the message itself and what viewers are likely to take away from it. However, it is still necessary to look at the overall context to understand the meaning and likely interpretations of it." (p.7)
- "Discussion between qualified annotators in which they explain the rationale for their classification is likely to result in better classification than using statistical measures across a larger number of (less qualified) annotators." (p.18)
- "The lack of details of the annotation process and annotation guidelines that are provided in publications in the field have been identified as one of the major obstacles for the development of new and more efficient methods by the abusive content detection community." (p.3)

## 13. UNKNOWN / not in extract
- Full text of IHRA definition inferences (Annex II) — referenced but located in an appendix not fully captured.
- Inter-annotator agreement statistics (kappa or alpha) — not computed or not reported.
- Comparison results between 2017 and 2018 samples — mentioned as collected but not detailed.
- Whether the annotated dataset was ever released publicly.
- Languages other than English in the corpus (tweets in foreign languages were discarded).
