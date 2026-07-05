---
stem: "2023-Hämmerl-Speaking Multiple Languages Affects the Moral Bias of Language Models"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [cultural-linguistic, moral-psychology, validity-psychometrics, contamination-robustness]
task_format: "n/a"
scoring_type: "behavioral"
dataset_size: null
dataset_construction: "scraped"
languages: ["Arabic", "Czech", "German", "English", "Chinese"]
models_tested: ["XLM-R", "mBERT", "AraBERT", "RobeCzech", "gBERT", "monolingual BERT (en/zh)"]
headline_numbers:
  - "XLM-R S-BERT achieves correlations of .74-.86 with English user study data across Arabic, Czech, German, English, and Chinese (p.5, Table 2)"
  - "Mean-pooled multilingual models fail: mBERT achieves 0.65 (en) but -0.10 (ar), 0.12 (cs), -0.18 (de), 0.62 (zh) with user study (p.5, Table 1)"
  - "Training with parallel data produces inter-language correlations >0.95, essentially removing cultural differences (p.9)"
  - "None of the models' MFQ scores map directly onto average human responses from any country tested (p.9)"
---
## 1. Gist
This paper investigates whether pre-trained multilingual language models (PMLMs) capture culturally differentiated moral norms across five languages: Arabic, Czech, German, English, and Mandarin Chinese. The authors apply the MORALDIRECTION framework (Schramowski et al., 2022), which induces a "good vs. bad" direction in sentence embedding space, to multilingual and monolingual BERT-based models. They also probe models with translated Moral Foundations Questionnaire (MFQ) items and compare results to human survey data from corresponding countries. The central finding is that while PMLMs do encode some moral dimension (correlating with English user study data), the moral differences between languages/models do not reliably correspond to human cultural differences — raising a significant warning for using multilingual LLMs as proxies for culturally diverse moral judgments. This is directly relevant to cultural-linguistic validity in values-alignment benchmarks.

## 2. Benchmark/eval design features
Three experiments:

**Experiment 1 — MORALDIRECTION framework**: Encodes positively/negatively connotated action verbs into sentence embeddings using 10 question templates (e.g., "Should I [verb]?", "Is it exemplary to [verb]?"). PCA extracts a "moral direction" axis from this space. Scores for subsequent statements are projected onto this axis and read as moral evaluations in [-1, 1]. Evaluated against English human user study (Schramowski et al., 2022) for correlation.

**Experiment 2 — Parallel subtitles analysis**: Applies MORALDIRECTION to Czech-English and German-English OpenSubtitles parallel sentence pairs. Manually inspects 500 pairs with highest score discrepancies to identify model failure modes (lexical reliance, polysemy, negation failures).

**Experiment 3 — Moral Foundations Questionnaire**: Applies MFQ questions (translated into 5 languages from the MFQ website) to models. Compares resulting aspect scores (Care, Fairness, Loyalty, Authority, Purity) to published human survey data from Germany (Joeckel 2012), Czech Republic (Beneš 2021), US (Graham 2011), and China (Wang 2019).

## 3. Task format & example item
No direct benchmark items — the paper probes models with existing instruments. Examples of MORALDIRECTION score contrasts from German-English parallel data (p.7, Table 4):

- German "Pures Gift." / English "Pure poison.": German XLM-R gives +0.65 (incorrect positive), English XLM-R gives -0.69. Likely error: German "Gift" = poison, but looks like English "gift."
- "Verräter ... wie Sie!" / "Traitors ... like you!": German scores negative; English model gives +0.19 (confusing "like you" as positive sentiment)
- "Ich erwürg dich!" / "I'll strangle you!": German models score correctly negative; XLM-R German gives +0.90 for unknown reasons

## 4. Scoring / grading methodology
- **Primary**: Pearson correlation of MORALDIRECTION scores with human user study data (Schramowski et al., 2022) from Amazon MTurk
- **Secondary**: Pearson correlations between models queried in different languages (intra-model cross-lingual consistency)
- **MFQ analysis**: Mean-pooled aspect scores from MFQ questions, compared visually to published human survey data
- Sentence-BERT fine-tuning (on MNLI data in 5 languages) is required before MORALDIRECTION yields coherent results

## 5. Dataset construction & provenance
- **MORALDIRECTION seed verbs**: From Schramowski et al. (2022) — machine-translated into 5 languages using MT systems (see Appendix B)
- **User study comparison data**: English Amazon MTurk ratings from Schramowski et al. (2022)
- **Parallel data**: OpenSubtitles (Lison & Tiedemann, 2016), Czech-English and German-English
- **MFQ translations**: From official MFQ website (moralfoundations.org); rephrased for machine scoring
- **Human MFQ comparison data**: Existing published studies from Germany, Czech Republic, US, China (not specifically collected for this paper)
- **Models released**: S-BERT models for 5 languages released on HuggingFace

## 6. Validity evidence
- XLM-R S-BERT achieves correlations of .74-.86 with English user study — comparable to monolingual English S-BERT (.86) (p.5, Table 2)
- Cross-language consistency (monolingual models): all pairwise correlations .78-.92, suggesting models share a common moral dimension (p.6, Table 3)
- But: No model MFQ scores match average human response patterns from any corresponding country — the direction of cultural differences is not captured (p.8-9)
- Parallel data analysis confirms models are lexically driven, not semantically driven — "like you" triggers positive scores regardless of context
- Sanity check confirms mean-pooled representations produce near-random MFQ scores (Figure 3), validating the need for sentence-BERT tuning

## 7. Saturation / discrimination
- All five languages show similar high correlation with English user study (.74-.86) — little discrimination between cultural contexts
- Pre-existing parallel-data S-BERT shows inter-language correlations >.95 — cultural signal essentially eliminated
- Key problem: moral encoding exists but is not culturally differentiated — models discriminate good/bad in English terms regardless of language used
- Arabic and Czech portions of XLM-R show slightly lower correlations (.77-.74), likely due to smaller training data (5.4 GB Arabic, 4.4 GB Czech vs. larger English corpus)

## 8. Multiturn / agentic aspects
n/a — single-turn embedding-based probing, no interactive dialogue.

## 9. Key numbers
- 5 target languages: Arabic (ar), Czech (cs), German (de), English (en), Mandarin Chinese (zh) (p.3)
- XLM-R S-BERT correlations with user study: en=.86, ar=.77, cs=.74, de=.81, zh=.86 (p.5, Table 2)
- Monolingual S-BERT correlations: en=.86, ar=.76, cs=.81, de=.84, zh=.80 (p.5, Table 2)
- Mean-pooled XLM-R correlations: mostly near zero except en=-.30 (p.5, Table 1)
- Monolingual model inter-correlation range: .78-.92 (p.6, Table 3)
- Parallel-data S-BERT inter-language correlations: >.95 (p.9, Appendix Table 8)
- 500 parallel sentence pairs manually inspected per condition (p.6)
- 4 human survey datasets compared in MFQ analysis: Germany, Czech, US, China (p.9)

## 10. Pitfalls & limitations
- **Language ≠ culture**: The assumption that language = cultural context does not hold — Arabic is spoken across many culturally distinct communities (p.8)
- **MORALDIRECTION limitation**: Single-axis (good/bad) representation is reductive; morality is not unidimensional (p.8)
- **Lexical shortcut problem**: Models rely on surface lexical cues rather than compositional semantics, failing with negation and polysemy across languages (p.7-9)
- **No Arabic/Czech human MFQ data**: No corresponding human baselines for comparison (noted p.5)
- **Translation confound**: Machine-translated verbs and MFQ items introduce translation errors that may drive some "cultural" differences
- **Models incomparable**: Monolingual models differ in training data size and domain, complicating direct comparisons (p.10)
- **Qualitative, exploratory scope**: Authors explicitly note this is primarily exploratory; most analyses qualitative (p.10)

## 11. Novel ideas worth stealing
- **Cross-lingual moral consistency as a benchmark dimension**: Test whether an LLM gives morally consistent evaluations of semantically equivalent statements across languages — inconsistency is a form of cultural bias
- **Parallel corpus moral scoring test**: Use parallel translation pairs as benchmark items where the model should ideally give similar moral scores to semantically identical content — deviations reveal cultural imposition or lexical shortcuts
- **Sanity check protocol for moral probing**: Compare model behavior with vs. without sentence-level representation fine-tuning as a baseline validation — mean-pooled representations are near-random, which should be reported as a baseline in any moral probing benchmark
- **Negation and polysemy as moral evaluation test cases**: Include items specifically designed to test whether models handle negation ("It is NOT okay to...") and cross-lingual false friends ("Gift" = present in English, poison in German) — systematic failures here would reveal lexical rather than semantic moral encoding
- **MFQ as a cross-cultural alignment probe**: Administering the MFQ to models and comparing to country-level human data is a low-cost method to test whether models encode culturally differentiated moral profiles — but this paper shows it is insufficient alone

## 12. Notable quotes
- "Can a PMLM capture cultural differences, or does it impose a Western-centric view regardless of context? This is a broad question which we cannot answer definitively." (p.2)
- "training with parallel data leads to more similar behaviour in this dimension, more or less removing cultural differences" (p.9)
- "None of our models' scores map directly onto average human responses. The model scores do not use the full range of possible values, but even the patterns of relative importance do not match the average human patterns." (p.9)
- "language models should not decide moral questions in the real world, but research in that direction might suggest that this is in fact possible." (p.10)

## 13. UNKNOWN / not in extract
- The specific verb list and question templates used for MORALDIRECTION induction (referenced in source paper Schramowski et al. 2022)
- Full MFQ question rephrasing and multiplier table (available in appendix/supplementary CSV, not in extract)
- Specific MT systems used for translation (referenced in Appendix B, not in extract)
- Statistical tests for MFQ comparison (visual comparison only reported in extract)
- How well the method generalizes to low-resource languages
