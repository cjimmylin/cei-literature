---
stem: "2018-Kiritchenko-Examining Gender and Race Bias in Two Hundred"
reader_model: "opus"
confidence: "high"
is_benchmark: true
theme_tags: [validity-psychometrics, best-practices, design-space]
task_format: "generative"
scoring_type: "behavioral"
dataset_size: 8640
dataset_construction: "template"
languages: [English]
models_tested: ["219 SemEval-2018 Task 1 submissions (50 teams)", "SVM-Unigrams baseline"]
headline_numbers: ["EEC = 8,640 English sentences from 11 templates (p.1)", "75%-86% of submissions consistently scored one gender higher (p.6)", "Average score differences <0.03 = 3% of 0-1 range (p.6)", "Maximal score difference (delta) as high as 0.34 (p.6)"]
---
## 1. Gist
This paper introduces the Equity Evaluation Corpus (EEC), described as "for the first time" a benchmark dataset for examining inappropriate gender and race biases in NLP systems (p.1). It consists of 8,640 English sentences constructed from 11 templates, engineered so that minimal pairs differ only in a single gender- or race-associated word (e.g., "This man made me feel angry" vs. "This woman made me feel angry"). The authors use the EEC as a supplementary hidden test set to audit 219 sentiment/emotion-intensity systems from SemEval-2018 Task 1. The core contribution matters for values-alignment benchmarking because it establishes the paired-minimal-pair (counterfactual substitution) methodology for measuring bias as a consistent, statistically-testable score differential rather than an accuracy differential — a template that recurs across fairness and values benchmarks. It demonstrates that bias is pervasive (75%+ of systems show statistically significant differences) even when average magnitudes are small.

## 2. Benchmark/eval design features
Construct measured: systematic (statistically significant) difference in predicted emotion/sentiment intensity attributable solely to the gender or race of a named/referenced person, holding all other content fixed. Item structure: template-generated sentences with two slots, <person> and <emotion word>. 11 templates: 7 contain emotion words (1,200 sentences each), 4 are neutral (60 sentences each), totaling 8,640 (p.3). <person> is filled by 10 African American + 10 European American first names (balanced M/F) plus 20 gendered noun phrases (e.g., "my daughter"/"my son") (Tables 2-3, p.3). <emotion word> covers 4 emotions (anger, fear, joy, sadness) x 5 intensity-varied words, drawn from Roget's Thesaurus categories (Table 4, p.4). Answer space is a real-valued intensity score in [0,1]. The design deliberately supports deriving minimal pairs differing in exactly one bias-relevant token.

## 3. Task format & example item
The systems perform intensity regression: "Given a tweet and an affective dimension A (anger, fear, joy, sadness, or valence), determine the intensity of A ... a real-valued score between 0 (least A) and 1 (most A)" (p.4). Example EEC minimal pair: "My daughter feels devastated" vs. "My son feels devastated" (p.4). Template example: "The conversation with my mom was heartbreaking" vs. "The conversation with my dad was heartbreaking" (p.5).

## 4. Scoring / grading methodology
Behavioral/statistical: for each system, predicted intensity scores on female-slot vs male-slot (and AA-slot vs EA-slot) sentence sets are compared. Delta = score(female) - score(male) per pair. A paired two-sample t-test per system tests whether the mean paired difference is zero; significance level 0.05, with Bonferroni correction over 438 assessments (219 submissions x 2 bias types), so the effective threshold is 0.05/438 (p.5). Systems are partitioned into three groups: no significant difference, significantly female-higher, significantly female-lower. 1,584 gender pairs and 144 race pairs were compared (p.5).

## 5. Dataset construction & provenance
Hand-authored templates (11, developed by the two authors "after several rounds of discussion and consensus building," p.3), populated by names from Caliskan et al. (2017) and emotion words from Roget's Thesaurus categories #900/#860/#836/#837 (p.4). Sentences manually checked for grammaticality (article/pronoun fixes, p.4 fn5). Total 8,640. No gold intensity labels exist for EEC — it functions purely as a probe set (p.5). Contamination control: EEC was administered as a hidden second test set of "unknown origin"; participants were told only after competition (p.5). Freely released (p.1).

## 6. Validity evidence
Face/content validity via the controlled minimal-pair design isolating a single causal variable. Criterion-style corroboration: bias directions align with documented human stereotypes — females rated more emotional, male-agent situations more fearful (Shields 2002, p.6); African American names associated with more negative emotions (Popp et al. 2003, p.8). A transparent SVM-Unigrams baseline (no external resources) also shows small bias, tracing bias to the training data itself (p.8). No inter-rater reliability or factor analysis (this is a behavioral audit, not a human-rated task).

## 7. Saturation / discrimination
Strong discrimination across systems: delta-spreads per system reach up to 0.57 on gender pairs and 0-0.15 on race pairs (p.6, p.8). Top-ranked and worst-ranked systems tend to have smaller delta-spreads; medium/low performers show greater sensitivity to bias-associated words (p.6). Most systems showing no significant difference performed poorly on the real tweets test set, implying that among well-performing systems the bias rate is even higher (p.6). Average magnitudes are small (<0.03) but individual pairs reach 0.34 (p.6), leaving headroom for finer discrimination.

## 8. Multiturn / agentic aspects
n/a — single-shot regression predictions, no interaction.

## 9. Key numbers
- EEC = 8,640 English sentences, 11 templates (p.1, p.3).
- 7 emotion templates x 1,200 + 4 neutral templates x 60 = 8,640 (p.3).
- 219 system submissions from 50 teams audited (p.4).
- 1,584 gender score-pair comparisons; 144 race comparisons (p.5).
- Bonferroni threshold 0.05/438 (p.5).
- Gender: only ~12/46 (25%) emotion submissions and 5/36 (14%) valence submissions showed no significant difference; so 75%-86% biased (p.6).
- Race: only 5-11 (11%-24%) emotion and 3 (8%) valence submissions showed no significant race difference (p.8).
- Average significant score differences <=0.03 (3% of range); max delta 0.34 (p.6).
- delta-spread up to 0.57 (gender), 0-0.15 (race) (p.6, p.8).
- SVM-Unigrams baseline delta-spread 0.09-0.2 gender, <0.002 race (p.8).

## 10. Pitfalls & limitations
Author-admitted: methodology "not meant to be comprehensive" (p.9); only binary gender and two US race categories; average biases are small (<3%) with unclear downstream impact (p.9); the paper does not identify the causes of bias, leaving it to future work (p.6, p.8). The neutral-sentence subset has only 44 comparisons, making its t-tests underpowered (p.7). Templates are short, syntactically simple, and synthetic — ecological validity to real text is limited (real sentences may contain multiple bias-associated words). Names encode race/gender jointly, so isolating "race" via first names conflates name-frequency/familiarity effects. No LLMs tested (2018-era feature systems).

## 11. Novel ideas worth stealing
- Minimal-pair counterfactual substitution: hold an entire sentence fixed and swap exactly one identity token, so any output difference is causally attributable to that token — directly reusable for probing values/identity bias in modern LLMs.
- Statistical framing of bias as a per-system paired t-test with multiple-comparison (Bonferroni) correction, rather than eyeballing means — gives calibrated significance claims.
- Hidden test set of "unknown origin" administered inside a shared task to prevent gaming/contamination — a clean contamination-control pattern.
- Template x fillers combinatorial generation for cheap, balanced, fully-controlled item construction with known structure.
- Reporting delta-spread (max-min within a system) as a discrimination/sensitivity metric alongside the mean effect — separates consistent-but-small bias from high-variance sensitivity.
- Including a transparent white-box baseline (SVM-Unigrams) to localize whether bias originates in the training data vs. the resources/architecture.
- Partitioning systems into direction-of-bias groups (higher/lower/none) rather than a single scalar — captures that bias direction can flip by affect dimension.

## 12. Notable quotes
- "Here for the first time, we present the Equity Evaluation Corpus (EEC), which consists of 8,640 English sentences carefully chosen to tease out biases towards certain races and genders." (p.1)
- "we cannot absolve ourselves of the ethical implications of the systems we build. Even if it is unclear how we should deal with the inappropriate biases in our systems, we should be measuring such biases." (p.2)
- "Thus 75% to 86% of the submissions consistently marked sentences of one gender higher than another." (p.6)
- "The SVM-Unigram bias results show that data collected by distant supervision can be a source of bias." (p.8)

## 13. UNKNOWN / not in extract
- Exact licensing terms of the EEC release (only "freely available" stated).
- Full lists of the specific significance p-values per system.
- Any human-subject validation that the templates read as natural to annotators.
- Individual system identities/architectures beyond aggregate feature descriptions.
- Numeric contents of Figures 1-4 (only described, not tabulated).
