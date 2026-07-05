---
stem: "2024-Wasi-Exploring Bengali Religious Dialect Biases in Large Language Models"
reader_model: "sonnet"
confidence: "medium"
is_benchmark: false
theme_tags: [religious-values, cultural-linguistic, validity-psychometrics]
task_format: "forced-choice"
scoring_type: "exact-match"
dataset_size: 20
dataset_construction: "expert"
languages: ["bn"]
models_tested: ["ChatGPT 3.5", "Gemini", "Microsoft Copilot"]
headline_numbers:
  - "LLMs show systematic bias toward Muslim Bengali dialect (higher accuracy ~55-60% vs. ~40-45% for Hindu dialect) without explicit religious specification (p.7)"
  - "Explicit Muslim specification boosts accuracy to 80-85%; explicit Hindu specification achieves 60-70% (p.8)"
  - "Dataset: 20 sentences contrasting Hindu vs. Muslim Bengali dialect; 4 experimental conditions per model (p.4-5)"
---
## 1. Gist
This exploratory study investigates whether major LLMs exhibit religious dialect bias in Bengali — specifically, whether they perform better on Muslim Bengali (Musholmani Bangla) than Hindu Bengali (Tatsama Bangla). The two dialect variants differ in vocabulary, loanword sources (Arabic/Persian vs. Sanskrit), and cultural context, reflecting the religious identity divide between Muslim-majority Bangladesh and Hindu Bengali communities in India. Twenty sentences were constructed, each having a Hindu dialect form and a Muslim dialect form of the same meaning. Three LLMs (ChatGPT 3.5, Gemini, Microsoft Copilot) were tested in four conditions: without religious specification, with "Muslim" specification, with "Hindu" specification, and with explicit translations of individual terms. Results show a systematic bias toward Muslim Bengali dialect without specification, and that explicit religious context improves accuracy for both dialects — but Muslim dialect accuracy is always higher. This work matters for values-alignment benchmarking because it demonstrates religious bias operating through the linguistic layer, not just through topic-level content, and provides a minimal viable methodology for detecting such biases.

## 2. Benchmark/eval design features
Small-n exploratory design with four conditions:
1. No specification: "Translate/interpret this Bengali sentence" (no religious context)
2. Muslim specification: "This is a Muslim Bengali sentence; interpret it"
3. Hindu specification: "This is a Hindu Bengali sentence; interpret it"
4. Term-explicit: individual dialect terms translated/glossed before the sentence
Twenty sentences × 3 models × 4 conditions = 240 evaluations. Accuracy defined as whether the model correctly understands/translates the dialect-specific vocabulary in context.

## 3. Task format & example item
Translation/interpretation forced evaluation. Example contrast pair (from paper context, p.4): A sentence using the Sanskrit-origin term "জল" (jal = water, Hindu dialect) vs. the Arabic-origin term "পানি" (pani = water, Muslim dialect). The model is shown one version and asked to interpret; the correct interpretation is judged by whether the model handles the dialect-specific vocabulary accurately. No verbatim example items are quoted with full prompt text in the extract.

## 4. Scoring / grading methodology
Binary human-coded accuracy per sentence (correct/incorrect interpretation of dialect-specific vocabulary). No formal rubric or inter-rater reliability reported. Accuracy rates reported as percentages across the 20-sentence set per condition per model. Results presented as bar charts or descriptive statistics (figures referenced p.7–8).

## 5. Dataset construction & provenance
20 sentences constructed by the authors, drawing on knowledge of Hindu and Muslim Bengali dialect vocabulary differences. No external dataset; expert-constructed minimal contrast pairs. Sentence topics not described in the extract (general everyday language assumed). The dataset is novel and small; no published vocabulary lists or corpus were used as a basis.

## 6. Validity evidence
Minimal formal validity. The dialect distinction (Tatsama/Hindu vs. Musholmani/Muslim Bengali) is linguistically documented and culturally well-established — the basic construct is valid. However, 20 sentences is too small for reliable estimation of bias magnitude. No inter-rater reliability for the accuracy coding. The four-condition design provides internal replication (same sentences, different context) rather than external generalizability.

## 7. Saturation / discrimination
The 20-sentence dataset is small enough that individual sentence results are not stable. The Muslim-bias finding (higher accuracy without specification) is consistent across all three models, which provides convergent evidence. The explicit-specification condition shows the models can perform correctly when given context — showing the bias is not due to fundamental incompetence but to default assumptions about which dialect is standard.

## 8. Multiturn / agentic aspects
n/a — single-turn translation/interpretation tasks.

## 9. Key numbers
- Dataset: 20 sentences with Hindu/Muslim dialect contrast pairs (p.4)
- 4 experimental conditions per model; 3 models (p.5)
- No specification: Muslim dialect accuracy ~55-60%; Hindu dialect ~40-45% (approximate from figures, p.7)
- Muslim specification: accuracy ~80-85% (p.8)
- Hindu specification: accuracy ~60-70% (p.8)
- Term-explicit condition: highest accuracy for both dialects (p.8)
- All three models show consistent Muslim-dialect bias direction (p.9)

## 10. Pitfalls & limitations
- N=20 sentences is very small; confidence intervals on accuracy estimates are wide (±10-15% at minimum).
- No inter-rater reliability for the binary accuracy coding.
- "Accuracy" defined by authors without published rubric — replication impossible.
- Sentences constructed by study authors may over-represent their knowledge of dialect differences; not corpus-based.
- Only three models tested; no open-source or multilingual specialist models included.
- Results are descriptive percentages; no significance tests reported.
- The study does not distinguish between (a) the model lacking knowledge of Hindu dialect vocabulary and (b) the model having knowledge but defaulting to Muslim dialect — different problems with different remedies.
- Muslim Bengali is the dialect used in Bangladesh-language internet data (larger population, more online content), so the bias may reflect training data distribution rather than ideological preference.
- No control sentences (e.g., standard/neutral Bengali) to anchor the baseline.

## 11. Novel ideas worth stealing
- **Religious dialect as a bias dimension distinct from religious topic bias**: most religious bias studies test models' attitudes about religion; this paper tests whether models handle language that is indexed to religious identity — a distinct and underexplored dimension relevant to safe deployment in South Asia.
- **Explicit religious specification as a debiasing prompt**: the finding that adding "This is a Hindu Bengali sentence" substantially improves accuracy suggests a simple prompting intervention for dialect-indexed language — transferable to other dialect pairs indexed to ethnicity, region, or religion.
- **Minimal contrast pair methodology**: 20 well-chosen sentence pairs that isolate a single dialect variable can demonstrate systematic bias more cleanly than a large corpus with confounded variables — useful for quick bias audits.
- **Four-condition within-subjects design for isolation of context effects**: testing the same sentences with no context, religious context, and term-explicit context allows decomposing model failure into context-sensitivity vs. knowledge gaps — a simple but powerful design.
- **Convergent evidence across three model families**: showing the same bias direction in ChatGPT, Gemini, and Copilot strengthens the claim despite the small N — triangulation across model families is a useful reliability strategy for small-scale studies.

## 12. Notable quotes
- "The results indicate that LLMs are biased towards the Muslim Bengali dialect, showing higher accuracy without explicit specification." (p.7)
- "When explicitly mentioning the religious nature of the dialect, models perform better for both Hindu and Muslim Bengali, but Muslim dialect still maintains a slight advantage." (p.8)
- "This research reveals that linguistic biases in LLMs can be influenced by the training data's cultural and religious proportions, reflecting the dominant communities' linguistic norms." (p.9)
- "The study highlights the need for more inclusive training datasets that represent diverse religious dialects equitably." (p.10)

## 13. UNKNOWN / not in extract
- The 20 sentences used in the study (not provided in extract).
- Inter-rater reliability statistics.
- Exact prompts used for each of the four conditions.
- Model versions/dates for ChatGPT 3.5, Gemini, and Copilot.
- Whether results differed across sentence topics within the 20-sentence set.
- Training data proportions (Bangladeshi vs. Indian Bengali) for the three models tested.
- Whether standard/neutral Bengali was tested as a control condition.
