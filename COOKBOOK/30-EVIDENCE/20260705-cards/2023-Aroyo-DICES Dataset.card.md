---
stem: "2023-Aroyo-DICES Dataset"
reader_model: "opus"
confidence: "high"
is_benchmark: true
theme_tags: [pluralism-aggregation, cultural-linguistic, validity-psychometrics, agentic-multiturn]
task_format: "interactive"
scoring_type: "human-rating"
dataset_size: 1340
dataset_construction: "mixed"
languages: [en]
models_tested: [LaMDA]
headline_numbers: ["Over 2.5 million total safety ratings across DICES-990 (1,802,600) and DICES-350 (731,850) (p.10)", "DICES-350: 350 conversations rated by up to 123 raters each (104 reliable) along 16 safety criteria (p.4,8)", "34% gold-vs-crowd-majority disagreement; 30% unsafe-by-gold-safe-by-crowd (p.8)", "Just over 60% of 36,400 ratings safe, 33% unsafe, 6% unsure (p.9)"]
---
## 1. Gist
DICES (Diversity In Conversational AI Evaluation for Safety) is a benchmark dataset that preserves — rather than collapses — rater disagreement about the safety of AI chatbot conversations. Instead of a single "ground truth" safety label, it collects an exceptionally high number of ratings per item (up to ~120) from a demographically balanced rater pool, encoding votes as distributions across gender, age, and race/ethnicity so that different aggregation strategies can be studied. Two subsets (DICES-990 across US+India, DICES-350 within a balanced US demographic grid) yield over 2.5 million ratings on adversarial multi-turn LaMDA conversations. It matters for values-alignment benchmarking as a flagship "perspectivist" safety resource: it operationalizes the claim that safety is socially and culturally situated and provides the statistical power to measure how demographic subgroups diverge on what counts as harmful.

## 2. Benchmark/eval design features
Construct: multi-dimensional conversational safety over five categories — harmful content (Q2, 8-9 sub-questions), unfair bias (Q3, 5 sub-questions), misinformation (Q4), political affiliation (Q5), and safety policy violations (Q6, 3 sub-questions) — plus a legibility check (Q1) (p.5). Answer space per sub-question: Yes (unsafe) / No (safe) / Unsure, with an "other" free option. Aggregation rule: a rater judges a conversation unsafe if any sub-question is "Yes" (p.9). Two annotation layers: "platinum" (diverse crowd) on all items and "gold" (trust-and-safety experts) on DICES-350. Ratings deliberately encoded as demographic distributions to support multiple aggregation strategies.

## 3. Task format & example item
Interactive/rating over a multi-turn conversation. Raters see prior turns as "context" and rate the last chatbot response (highlighted) (p.6). No single verbatim conversation is reproduced in the extract (adversarial content). The task structure: Q1 legibility (English? comprehensible? familiar topic?), then Q2-Q6 safety sub-questions each answered Yes/No/Unsure (p.5). Example structure only (p.5-6); actual conversation text n/a in extract.

## 4. Scoring / grading methodology
Human rating, no model scoring. Overall safety derived by OR-aggregation over sub-questions (any "Yes" → unsafe; no Yes but some Unsure → unsure; all No → safe) (p.9). Gold labels: one expert rater then verified by a pool of five experts (p.8). Diversity/agreement metrics include inter-rater reliability (IRR), negentropy, and plurality size computed within demographic groups (p.2,8). Rater quality filtered via response-time thresholds (below 1/2, 1/3, 1/4 of the 120s median) and constant-labeling detection (p.7).

## 5. Dataset construction & provenance
Source: sampled from an 8K multi-turn conversation corpus (48K turns) of human agents adversarially provoking a generative chatbot (LaMDA, Thoppilan et al.), max 5 turns (p.3-4). DICES-990 (990 convs, stratified across 3 adversariality levels, US+India, 173 raters, 60-70 ratings/item, 24 criteria) and DICES-350 (350 convs, balanced US 3x4 age×race grid targeting 120 raters, all raters rate all items, 16 criteria) (p.4). 13/19 low-quality raters removed respectively; DICES-350 analyses use 104 reliable raters. Total 1,340 conversations. Released on GitHub under CC BY 4.0 (p.22). Self-reported, consented demographics.

## 6. Validity evidence
Explicit inter-rater reliability analysis: Latine raters show significantly higher IRR; White raters higher negentropy/plurality; Multiracial significantly lower agreement (p.8, Fig.4). Expert (gold) vs crowd-majority disagreement quantified at 34%, mostly the crowd finding expert-flagged-unsafe content acceptable (p.8). High replication (~104-123 ratings/item vs typical 3-5) gives strong statistical power and enables resampling to estimate variability (p.2). Bayesian multilevel modeling of demographics used to study disagreement (p.10).

## 7. Saturation / discrimination
Not a model-scoring leaderboard, so no ceiling in the usual sense; the "signal" is disagreement itself. Rating distribution: ~60% safe, 33% unsafe, 6% unsure (p.9), showing a non-degenerate spread. Authors note diverse pools produce much higher disagreement, challenging the notion of a stable "gold" label (p.9). Headroom framed as needing more conversations and finer demographic disaggregation to reveal content-dependent disagreement patterns (p.10).

## 8. Multiturn / agentic aspects
Core to the design: all items are adversarial multi-turn human-chatbot conversations (max 5 turns) generated by human agents deliberately trying to provoke unsafe responses; raters evaluate the final chatbot turn in context (p.3-4,6). This is a red-teaming-derived corpus, though the rating task itself is static annotation of pre-generated conversations rather than live agentic interaction.

## 9. Key numbers
- DICES-990: 990 convs, 173 raters, 60-70 ratings/item, 24 criteria, 1,802,600 ratings (p.8).
- DICES-350: 350 convs, 123 raters (104 reliable), 16 criteria, 731,850 ratings (p.8).
- Total >2.5M ratings, ~300 raters, 1,340 conversations (p.9-10).
- DICES-350 reliable pool: 57 women/47 men; 27 GenX+/28 Millennial/49 GenZ; 21 Asian/23 Black/22 Latine/13 Multiracial/25 White (p.4).
- Gold-vs-crowd disagreement 34% (30% unsafe-gold/safe-crowd; 4% reverse) (p.8).
- Rating split: ~60% safe, 33% unsafe, 6% unsure of 36,400 (p.9).
- Topics: ~22% racial, 14% political, 10% gendered, 7% misinfo/medical each; >40% benign (p.7).
- Median annotation time 120s/conversation (p.7).

## 10. Pitfalls & limitations
Author-admitted: only 1,340 conversations total — small item count may hide content-dependent disagreement patterns (p.10); demographic axes simplified to 4 categories with few sub-groups (2 locales, 5 ethnicities, 3 ages, 2 genders) (p.10); cannot yet distinguish sincere-belief disagreement from noise/error/poor items (p.10); unclear how disagreement translates to decision-making (p.10). My additions: OR-aggregation over many sub-questions inflates "unsafe" base rate and conflates severities; single-vendor (Google/LaMDA) source and consent form permitting broad internal reuse; DICES-350 US-only limits cross-cultural claims despite the diversity framing.

## 11. Novel ideas worth stealing
- Radically high rating replication (100+ per item) turning annotator disagreement into a measurable, statistically powered signal rather than noise to be averaged away.
- Encode votes as distributions over demographics and ship annotator-level labels, enabling downstream users to test alternative aggregation/pluralism strategies without recollecting data.
- Dual gold (expert) + platinum (crowd) labeling on the same items, quantifying expert-crowd divergence (34%) as a first-class finding.
- Within-group agreement metrics (IRR + negentropy + plurality size) to characterize which subgroups agree internally — a reusable diagnostic for value benchmarks.
- Response-time-based quality control (fractions of median time) plus constant-label detection as scalable rater-quality signals.
- "Balanced-cell" recruitment (fully crossed age×ethnicity grid) to guarantee statistical power for intersectional analysis.
- Adversarial multi-turn red-team corpus as the item source, ensuring value-laden edge cases.

## 12. Notable quotes
"Machine learning approaches often require training and evaluation datasets with a clear separation between positive and negative examples. This risks simplifying and even obscuring the inherent subjectivity present in many tasks." (p.1)
"we approach differences between raters opinions of safety in terms of diversity ... We avoid assuming bias should, by default, be mitigated or removed" (p.2)
"we observed disagreements between the gold label and crowd majority vote label in 34% examples." (p.8)
"diverse rater pool presents much higher rate of disagreement among raters, which poses a challenge to the traditional definition of 'gold' labels" (p.9)

## 13. UNKNOWN / not in extract
- Verbatim example conversation text (withheld as adversarial).
- Exact per-category safety rates (only overall reported here).
- Estimated hourly wage / total compensation (referenced but not in read text).
- Full appendix metrics repository contents.
- Model performance evaluation (dataset is annotation-only; no model tested against it here).
