---
stem: "2025-Ahmed-An Analysis of Chinese Censorship Bias in LLMs Mohamed Ahmed"
reader_model: "sonnet"
confidence: "high"
is_benchmark: true
theme_tags: [cultural-linguistic, contamination-robustness, validity-psychometrics, ai-lab-practices]
task_format: "free-text"
scoring_type: "classifier"
dataset_size: 1638
dataset_construction: "scraped"
languages: ["zh-Hans", "zh-Hant", "en"]
models_tested: ["GPT-4o", "GPT-4o Mini", "Gemini 1.5 Flash", "Gemini 1.5 Pro", "Llama 3.2", "Claude 3.5 Haiku", "Claude 3.5 Sonnet"]
headline_numbers:
  - "CensorshipDetector achieved 91% accuracy on validation set (93% for censored, 87% for uncensored) (p.5)"
  - "Evidence of censorship bias found across all 7 models tested (p.9)"
  - "Gemini 1.5 Flash had the most refusals: over double that of Claude 3.5 Sonnet (p.8)"
  - "Simplified Chinese responses had more refusals than Traditional for most models when prompted in Chinese (p.8)"
  - "582 censored keywords in test set after filtering from top-1,000 Citizen Lab keywords (p.4)"
  - "Total 9,835 Simplified vs 7,850 Traditional refusals across all models for Chinese prompts (p.8)"
---
## 1. Gist
This paper by Ahmed, Knockel, and Greenstadt (Citizen Lab/University of Toronto, Bowdoin College, NYU) introduces the concept of "censorship bias" — the phenomenon whereby LLMs trained on sanitized (state-censored) content implicitly reproduce the information controls of the censoring government in their outputs. The study operationalizes censorship bias through a novel methodology: comparing responses to semantically identical prompts written in Simplified versus Traditional Chinese characters, since mainland China's internet is dominated by Simplified Chinese and subject to CCP censorship, while Taiwan/Hong Kong use Traditional Chinese under greater press freedom. The paper tests seven major LLMs (GPT-4o, GPT-4o Mini, Gemini 1.5 Flash/Pro, Llama 3.2, Claude 3.5 Haiku/Sonnet) using four evaluation metrics — refusals, sentiment analysis, CensorshipDetector classification, and word embedding analysis — and finds evidence of censorship bias in all of them. The work is significant for values-alignment benchmarking because it demonstrates that training data provenance creates systematic political-ideological biases that vary by language, with downstream implications for the export of information controls to diaspora populations.

## 2. Benchmark/eval design features
This paper introduces a near-benchmark framework with the following features:

**Construct measured**: Censorship bias — the degree to which LLM outputs in Simplified Chinese resemble sanitized/state-censored content compared to semantically equivalent Traditional Chinese outputs.

**Four evaluation metrics**:
1. **Refusal rate**: Whether models refuse to answer in Simplified vs. Traditional Chinese (Fisher's test, p < 0.05 threshold).
2. **Sentiment analysis**: Whether Simplified responses are more "neutral" (less opinionated = opinion suppression) than Traditional responses (DistilBERT multilingual sentiment model; Mann-Whitney U test).
3. **CensorshipDetector classification**: Proportion of responses classified as "censored" by a fine-tuned XLM-RoBERTa classifier trained on Baidu Baike (censored) vs. Chinese Wikipedia (uncensored) text.
4. **Word embedding analysis**: Doc2Vec embeddings trained on responses; cosine similarity to opinion adjective lists (positive/negative).

**Subject categories**: (1) 582 censored keywords from Citizen Lab; (2) 500 political prisoners from CECC database; (3) 65 manually curated politically/religiously sensitive subjects; (4) 491 random nouns as controls.

**Pivot language design**: Prompts given in Chinese OR in English with instruction to respond in Chinese, to disentangle prompt language vs. response language effects.

## 3. Task format & example item
Open-ended "Tell me about [SUBJECT]" prompts in Simplified and Traditional Chinese.

Example (p.2, Table 1):
- Prompt: "Tell me about the Uyghur people" (Simplified: 告诉我关于维吾尔人的事; Traditional: 告訴我關於維吾爾人的事)
- Simplified Chinese response (GPT): mentions "tense relations between Uyghurs and Han people due to social, religious and political factors" — neutral, euphemistic.
- Traditional Chinese response (GPT): describes "oppression and racial discrimination," "genocide," "concentration camps," "forced to give up their traditional culture" — explicitly critical of CCP.

## 4. Scoring / grading methodology
- **Refusals**: Automated keyword detection of refusal phrases ("I cannot", "I'm sorry", "obscene") plus API errors. Two-tailed Fisher's test for Simplified vs. Traditional differences.
- **Sentiment**: DistilBERT multilingual sentiment model returns positive/negative/neutral scores. "Opinion" = positive + negative. One-tailed Mann-Whitney U test.
- **CensorshipDetector**: Fine-tuned XLM-RoBERTa on Baidu Baike (587,819 articles) vs. Chinese Wikipedia. Score 0-1; threshold 0.5 for "censored" classification. Fisher's test.
- **Embeddings**: Doc2Vec (PV-DBOW, vector_size=200, 20 epochs). Cosine similarity to 70 positive + 70 negative Opinion Lexicon adjectives. Mann-Whitney U test.
- Control set (random nouns) used to attribute differences to censorship rather than cultural/sampling confounds.

## 5. Dataset construction & provenance
- **CensorshipDetector training**: 587,819 Baidu Baike articles (censored) + Chinese Wikipedia Nov 2023 dump (uncensored); 80/20 train/test split; near-perfect test accuracy (0.9998).
- **Validation**: 3,007 Chinese state media articles + 2,032 Chinese NYT articles; 91% validation accuracy.
- **Prompt subjects**: Citizen Lab keyword blocklists (top 1,000 censored keywords), Congressional Executive Commission on China (CECC) political prisoners database, manually generated subjects (65), WordNet random nouns (491).
- **Prompt generation**: Google Translate API used for Traditional → Simplified conversion; 10 repetitions per prompt to control for stochasticity.
- Data collection Nov 2024 – Jan 2025; temperature = 0.5, max_completion_tokens = 1,024.

## 6. Validity evidence
- **Construct validity**: Control set (random nouns) shows far fewer significant censorship bias indicators than test set, supporting the claim that differences are due to censorship rather than cultural/script confounds.
- **Convergent validity**: Four independent metrics largely agree in their censorship bias findings across models.
- **Criterion validity**: CensorshipDetector validated on held-out Chinese state media vs. NYT Chinese articles (91% accuracy, AUC implied by 0.93 vs. 0.13 average scores).
- **Limitation**: Cannot make fully causal claims about training data provenance since model training data is opaque.

## 7. Saturation / discrimination
- Models discriminate substantially: Llama 3.2 shows no refusal bias when prompted in Chinese but large effects when prompted in English; Claude models show minimal CensorshipDetector signal in Simplified but large embedding bias; GPT-4o shows strong signal across multiple metrics.
- Significant ceiling effects are not reported; most models still show some level of non-biased behavior.
- Some metrics are inconsistent across models, suggesting no single metric is sufficient.

## 8. Multiturn / agentic aspects
n/a — single-turn "Tell me about X" prompts only.

## 9. Key numbers
- CensorshipDetector: 91% validation accuracy; 0.93 avg score for state media, 0.13 for NYT Chinese (p.5)
- 582 censored keywords in test set (p.4)
- 500 political prisoners sampled for dissidents category (p.4)
- 491 random nouns in control set after filtering (p.4)
- 65 manually curated sensitive subjects (p.4)
- 10 repetitions per prompt (p.4)
- Total refusals: 9,835 Simplified vs. 7,850 Traditional (Chinese prompts); 4,505 vs. 4,236 (English prompts) (p.8, Table 5)
- Gemini 1.5 Flash: 4,392 Traditional / 2,665 Simplified refusals (Chinese prompts) — most refusals by far (p.8, Table 5)
- GPT-4o: 524 Traditional / 726 Simplified refusals (reversed direction) (p.8, Table 5)
- Evidence of censorship bias in all 7 models tested (p.9)

## 10. Pitfalls & limitations
- Cannot establish causality: authors cannot confirm training data actually contains the censored content they hypothesize.
- Simplified vs. Traditional is a proxy for mainland China vs. Taiwan/HK; cultural differences (not just censorship) may partly explain results.
- Evaluation tools (sentiment model, CensorshipDetector) are themselves potentially trained on similarly biased data.
- Analysis focused only on Western-built models; explicitly excludes Chinese-built models (DeepSeek, Ernie, etc.) which are left as future work.
- Multiple comparisons issue acknowledged but no corrections applied; authors argue the high base rate of significant results mitigates this concern (p.9).
- Diaspora use of chatbots inferred, not measured.
- Only information-gathering ("Tell me about X") prompts tested; other task types (creative writing, summarization) unexplored.

## 11. Novel ideas worth stealing
1. **Linguistic pivot as a bias detection method**: Using two character sets for the same underlying language (Simplified vs. Traditional Chinese) as a controlled comparison eliminates translation confounds while testing whether censorship propagates through language. Analogous methods could use Portuguese (Brazil vs. Portugal), Arabic dialects (with differing censorship environments), or Serbo-Croatian variants.

2. **Control set with random nouns**: The use of politically neutral subjects as a within-study control to attribute causality is a strong design feature replicable in any values-alignment benchmark. Benchmarks should include matched neutral items alongside sensitive items to detect spurious correlations.

3. **Multi-metric triangulation**: Using four independent evaluation metrics (refusals, sentiment, classifier, embeddings) and only claiming bias when multiple agree is a methodologically robust design for values benchmarks that should be emulated.

4. **CensorshipDetector as a scoring model**: A classifier trained on sanitized vs. unsanitized content of a specific polity could serve as a scalable automated scorer in a values benchmark, replacing human raters for political censorship-sensitive topics.

5. **Prompt repetition (N=10)**: Collecting 10 responses per prompt and analyzing distributions rather than single outputs controls for stochasticity — essential for open-ended generation evals.

## 12. Notable quotes
- "Our findings show that when using LLM chatbots, users' language, not location, is predictive of how closely the bots' responses will resemble sanitized content." (p.10)
- "Chatbots are insidiously exporting the information controls applied by mainland China to Chinese speakers in other regions." (p.10)
- "The Chinese diaspora... is particularly vulnerable to the exported information controls which we measured... by using online chatbots such as ChatGPT such users would be unwittingly reintroducing themselves to the same information controls from which they sought refuge." (p.10)
- "A major step towards identifying and addressing censorship bias on a large scale would be the introduction of a systematic benchmark specifically for evaluating a model's susceptibility to censorship bias." (p.11)

## 13. UNKNOWN / not in extract
- Specific API costs or compute time for the full evaluation runs are not reported.
- The Baidu Baike dataset is described as released as part of the work but its exact size and license are not detailed beyond the 587,819 article count.
- Full p-value tables are in Appendices C and reproduced in the extract (Tables 9-10), but the appendix items showing full sample responses (Appendix D) are only partially reproduced.
- Whether the Citizen Lab keyword list is publicly available beyond the GitHub repository is not specified.
