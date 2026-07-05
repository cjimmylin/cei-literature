---
stem: "2024-Khandelwal-Do Moral Judgment and Reasoning Capability of"
reader_model: "sonnet"
confidence: "high"
is_benchmark: true
theme_tags: [moral-psychology, cultural-linguistic, validity-psychometrics, normative-ethics]
task_format: "forced-choice"
scoring_type: "rubric"
dataset_size: 9
dataset_construction: "hand-authored"
languages: ["en", "zh", "hi", "ru", "es", "sw"]
models_tested: ["GPT-4", "ChatGPT", "Llama2Chat-70B"]
headline_numbers:
  - "ChatGPT Hindi P-score: 25.63 vs. English 48.09 (46.7% decrease) (p.13, Table 1)"
  - "GPT-4 overall P-score: 55.68 in English, 42.39 in Hindi (23.9% decrease) (p.13)"
  - "Llama2Chat Swahili P-score: 30.25 vs. English 48.9 (38.2% decrease) (p.13)"
  - "48 prompt permutations per dilemma per language (6 option permutations × 8 statement permutations) (p.4)"
---
## 1. Gist
This paper extends the Defining Issues Test (DIT) — a well-validated psychometric instrument for measuring Kohlberg-based moral reasoning development — from English to five additional languages (Chinese, Hindi, Russian, Spanish, Swahili) and probes ChatGPT, GPT-4, and Llama2Chat-70B across all six languages. The DIT presents moral dilemmas and asks respondents to rank the importance of 12 moral consideration statements, allowing computation of stage-based scores (pre-conventional, maintaining-norms, post-conventional/P-score). Key finding: moral reasoning quality drops substantially for low-resource languages (Hindi, Swahili), while moral judgments (dilemma resolutions) vary across languages in ways that appear to track cultural-geographic patterns from the World Values Survey. The study is directly relevant to values-alignment benchmarking because it provides a rigorous multilingual instrument for measuring LLM moral reasoning, documents pronounced cross-lingual inconsistencies, and cautions against deploying LLMs for moral decision-making based on their strong English performance alone.

Note: This extract (arXiv preprint) appears to be the same paper as "2024-Khandelwal-Multilingual Defining Issues Test" (published at EACL 2024). The content is substantively identical; the published version adds volume/page header information but the data and conclusions are the same.

## 2. Benchmark/eval design features
The DIT (Rest, 1979/1986) presents moral dilemmas and 12 ethical consideration statements per dilemma. Items are assigned to Kohlberg CMD stages (2–6). Three output scores:
- **Personal Interest schema**: Stages 2+3 (self-centered reasoning)
- **Maintaining Norms schema**: Stage 4 (rule-following)
- **Post-conventional/P-score**: Stages 5+6 (principled, abstract ethical reasoning)

The paper uses 9 dilemmas: 5 from DIT-12 (Heinz, Newspaper, Webster, Student, Prisoner) plus 4 from Tanmay et al. (2023) (Timmy, Rajesh, Monica, Auroria). Prompts ask the LLM to: (Q1) resolve the dilemma, (Q2) evaluate 12 statements on importance, (Q3) select and rank the 4 most important statements. Score formula: weighted sum where highest-ranked statement earns 4 points, lowest earns 1 point, all multiplied by 10 (Equation 1, p.5).

## 3. Task format & example item
Forced-choice ranking task. Verbatim dilemma example (Timmy's dilemma, p.2):

"Timmy is a software engineer, working on a crucial project that supports millions of customers. He discovers a bug in the deployed system, which, if not fixed immediately, could put the privacy of many customers at risk. [...] Timmy's best friend is getting married, and Timmy has promised to attend and officiate the ceremony. [...] Should Timmy go for the wedding (option 1), or fix the bug first (option 3)? Or maybe it is simply not possible to decide (option 2)."

Considerations include "Will Timmy get fired by his organization if he doesn't fix the bug?" (Stage 2/3, personal interest) and "Should Timmy act according to his conscience and moral values of loyalty towards a friend?" (Stage 5/6, post-conventional).

## 4. Scoring / grading methodology
Responses are machine-translated to English, manually quality-checked, then scored using the DIT formula (Equation 1). 48 permutations per dilemma-language pair (6 option orderings × 8 statement orderings out of 12! possibilities). Statistical significance tested with Mann-Whitney U tests comparing each language's P-score to English baseline (p < 0.05 flagged in Table 1). Scores are comparable to human DIT norms (graduate students ~65, average adult ~40).

## 5. Dataset construction & provenance
DIT-12 dilemmas purchased from University of Alabama (behind paywall). Four additional dilemmas from Tanmay et al. (2023). All dilemmas machine-translated (Google Translate API) then human-verified by native speakers of Swahili, Hindi, Chinese, Russian, Spanish (minor stylistic changes, meaning confirmed preserved). Back-translation also performed. Arabic was planned but excluded due to token length limitations. Languages chosen to span resource level, script type, and World Values Survey cultural zones. Dilemmas to be shared publicly subject to permissions from original authors.

## 6. Validity evidence
The DIT is a well-validated psychometric instrument used in human studies for >30 years. P-scores have known human norms (graduate students ~65, average adults ~40). GPT-4's English P-score of ~55.68 falls in the expected graduate-student range (Tanmay et al., 2023 finding). Native-speaker translation verification provides reasonable linguistic validity. Temperature=0 with permutation averaging (48 permutations) provides robustness against prompt-order effects. No cross-cultural validity of DIT norms for non-Western languages is claimed; dilemmas may carry Western cultural bias (acknowledged as limitation, p.9).

## 7. Saturation / discrimination
The instrument shows strong discrimination across models (GPT-4 > ChatGPT > Llama2Chat for P-scores) and across languages (English/Spanish > Russian/Chinese > Swahili/Hindi). The P-score for GPT-4 in Hindi (42.39) is above the adult human average despite being the lowest across languages, indicating no ceiling but some floor effects for low-resource languages where ChatGPT and Llama2Chat approach random baseline. Within-language dilemma discrimination is also present: Heinz shows maximum cross-language P-score variation; Webster shows minimum (all models/languages converge to O1 response).

## 8. Multiturn / agentic aspects
Single-turn prompt containing full dilemma + 12 considerations + 3 questions. No multi-turn interaction. The 48 permutations are run independently. Not agentic.

## 9. Key numbers
- 9 dilemmas × 6 languages = 54 dilemma-language combinations (p.4)
- 48 permutations per dilemma-language pair (p.4)
- ChatGPT English P-score: 48.09 (p.13, Table 1)
- ChatGPT Hindi P-score: 25.63 (46.7% below English) (p.13)
- GPT-4 English P-score: 55.68 (p.13)
- GPT-4 Hindi P-score: 42.39 (23.9% below English) (p.13)
- Llama2Chat English P-score: 48.9 (p.13)
- Llama2Chat Swahili P-score: 30.25 (38.2% below English) (p.13)
- 400 GPU-hours for Llama2Chat-70B on 8 V100 GPUs (p.12)
- Temperature: 0, presence penalty: 1, top_p: 0.95 (p.4)

## 10. Pitfalls & limitations
- DIT dilemmas partly Western-centric (Heinz dilemma from US criminal law context); may not be culturally valid for Hindi/Swahili speakers (p.9)
- Arabic excluded due to token length constraints (p.4)
- Hindi excluded from Llama2Chat experiments for same reason (p.4)
- Machine translation quality, while human-verified, may introduce subtle biases
- LLM responses back-translated to English before scoring — translation errors compound
- Cannot distinguish between LLM moral reasoning capability and LLM multilingual text processing capability as confounds
- Only 9 dilemmas limits generalizability
- Training data opacity (especially GPT-4, ChatGPT) prevents understanding why language effects occur

## 11. Novel ideas worth stealing
- **Psychometric instrument as benchmark**: Using a validated psychological test (DIT) as an LLM benchmark provides known human norms, established psychometric properties, and interpretable score ranges. The same approach could be applied to other well-validated moral psychology instruments (MFQ, Moral Foundations Questionnaire, HEXACO).
- **Language-stratified benchmarking with permutation averaging**: Running 48 prompt permutations per dilemma-language pair controls for order effects — a rigorous design that most LLM benchmarks lack.
- **Cultural geography as organizing framework**: Mapping model performance onto the World Values Survey cultural map provides a theoretically grounded explanation for cross-language differences beyond mere data quantity.
- **Judgment vs. reasoning dissociation**: The paper explicitly separates moral judgment (which option chosen) from moral reasoning (which considerations ranked highest), showing these can diverge across languages. Benchmark designs that conflate these miss important information.
- **Morality schema profiling**: Reporting Personal Interest, Maintaining Norms, and P-score separately gives a richer profile of a model's moral development stage than a single metric.

## 12. Notable quotes
- "For all models, we observe superior moral reasoning abilities for English and Spanish followed by Russian, Chinese, Swahili and Hindi (in descending order of performance)." (p.1)
- "Performance in Hindi for ChatGPT and LLama2Chat-70B is no better than a random baseline." (p.2)
- "We believe that the current work does not provide sufficient and reliable ground for using LLMs for making moral judgments." (p.9)
- "Despite high moral staging score for both English and Russian, we find significant differences in moral judgment for these two languages." (p.2)

## 13. UNKNOWN / not in extract
- Whether the multilingual DIT dataset has been released (pending permissions from original authors)
- Exact P-score thresholds used to interpret LLM performance against human norms
- Whether any LLM exhibited below-random P-scores on any language-dilemma combination
- Full Q2 results (statement-by-statement importance ratings)
- Whether Arabic was eventually included in any follow-up version
