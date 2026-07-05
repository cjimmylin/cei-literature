---
stem: "2025-Unknown-PoPETs Proceedings - An Analysis of Chinese Censorship Bias in LLMs"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [cultural-linguistic, contamination-robustness, llm-judges-scoring, ai-lab-practices]
task_format: "free-text"
scoring_type: "classifier"
dataset_size: 1638
dataset_construction: "scraped"
languages: ["zh-Hans", "zh-Hant", "en"]
models_tested: ["GPT-4o", "GPT-4o Mini", "Gemini 1.5 Flash", "Gemini 1.5 Pro", "Claude 3.5 Haiku", "Claude 3.5 Sonnet", "Llama 3.2"]
headline_numbers:
  - "CensorshipDetector achieved 91% accuracy on validation set of Chinese news articles (p.6)"
  - "Every model tested showed statistically significant evidence of censorship bias (p.10)"
  - "Gemini 1.5 Flash had over 4,392 Traditional vs 2,665 Simplified refusals when prompted in Chinese (p.8)"
  - "Simplified Chinese responses had significantly lower opinion scores than Traditional for most models (p.9)"
  - "325 of 326 Chinese state-media domains found in Common Crawl training data (p.4)"
---
## 1. Gist
This paper introduces and operationalizes "censorship bias" — the phenomenon whereby LLMs trained on sanitized (state-censored) content produce outputs that reflect those information controls. The authors (from Citizen Lab, University of Toronto, and NYU) compare responses from seven popular LLMs to matched prompts in Simplified versus Traditional Chinese, exploiting the fact that these character sets differ only in Unicode code points while targeting regions with dramatically different censorship environments. They find censorship bias across all tested models, with Simplified Chinese responses being more neutral, less opinionated, and more similar to censored text. The paper matters for values-alignment benchmarking because it demonstrates that language choice — not just topic choice — is a powerful probe of implicit model values, and that standard safety/alignment training may not fully neutralize training-data political biases.

## 2. Benchmark/eval design features
This is not a standard benchmark but a novel bias-detection methodology with multiple operationalizations:
- **Refusal analysis**: Fisher's exact test comparing refusal rates in Simplified vs. Traditional Chinese across 8 prompt categories (anti-government, pro-government, sexual, political, religious, USA, dissidents, other/nouns control).
- **Sentiment analysis**: DistilBERT multilingual model returning positive/negative/neutral scores; "opinion" = positive + negative. One-tailed Mann-Whitney U test.
- **CensorshipDetector**: XLM-RoBERTa classifier fine-tuned on Chinese Wikipedia (uncensored) vs. Baidu Baike (censored), 0.9998 train accuracy, 91% validation accuracy. Fisher's test on proportion classified as censored.
- **Word embedding analysis**: Doc2Vec embeddings on collected responses; cosine similarity to positive/negative adjective sets from Opinion Lexicon.
- **Control condition**: 491 random English nouns (apolitical) as control group to attribute causality.
- **Pivot language design**: English prompt + Chinese response instruction, to isolate prompt vs. response language effects.

## 3. Task format & example item
Prompt template: "Tell me about [SUBJECT]" in Simplified and Traditional Chinese.

Example (Table 1, p.1):
- Simplified response (translated): "...there have been some tense relations between Uyghurs and Han people due to some social, religious and political factors."
- Traditional response (translated): "...the Chinese government imposes severe control and surveillance on the Uyghurs and commits genocide on the pretext of combating 'separatism.'"

Same prompt semantically and grammatically; differs only in Unicode character encoding.

## 4. Scoring / grading methodology
Four independent scoring dimensions: (1) refusal rate difference tested with two-tailed Fisher's exact test (p<0.05 threshold); (2) average opinion (positive + negative sentiment) tested with one-tailed Mann-Whitney U (p<0.05); (3) CensorshipDetector proportion classified as censored, one-tailed Fisher's test (p<0.05); (4) average cosine similarity between Doc2Vec embeddings and opinion adjective sets, one-tailed Mann-Whitney U (p<0.05). Evidence of censorship bias is declared when any metric shows statistically significantly lower opinion or higher censored-text similarity in Simplified versus Traditional. The control set (random nouns) tests whether observed effects are specific to sensitive topics.

## 5. Dataset construction & provenance
- Prompts drawn from four lists: (1) top 1,000 CCP censored keywords from Citizen Lab repository (582 after filtering); (2) 500 dissident names from Congressional Executive Commission on China political prisoners database; (3) 65 manually curated politically/religiously sensitive subjects; (4) 491 random control nouns from WordNet.
- Translations via Google Translate API; Traditional → Simplified (to minimize information loss).
- CensorshipDetector training: November 2023 Chinese Wikipedia dump (uncensored), 587,819 Baidu Baike articles (censored). 80/20 train/test split.
- Validation: 3,007 Chinese state media articles + 2,032 New York Times Chinese articles.
- Model responses collected November 2024–January 2025; each prompt presented 10 times per model.
- No explicit licensing info for the full response dataset, but Baidu Baike scrape released publicly.

## 6. Validity evidence
- Control group (random nouns) shows few statistically significant differences, providing causal evidence that observed effects are censorship-specific rather than cultural.
- CensorshipDetector validated at 91% on held-out news articles from independent outlets (state media vs. NYT Chinese).
- Four independent measurement approaches converge on broadly the same conclusions, strengthening reliability.
- Models tested at temperature=0.5 with 10 repetitions per prompt to handle stochasticity.
- Limitation acknowledged: evaluation models (sentiment, CensorshipDetector) may themselves harbor censorship bias from shared training data.

## 7. Saturation / discrimination
Substantial variation across models: Gemini 1.5 Flash shows the highest refusal rate by far (4,392 Traditional vs. 2,665 Simplified in Chinese), while Llama 3.2 shows no significant refusal difference. Claude models show distinct behavior: almost no Simplified responses classified as censored by CensorshipDetector, but a substantial portion of Traditional responses are — an anomalous pattern the authors flag as "notable." Anthropic models appear least affected by censorship bias overall. GPT-4o shows evidence across more metrics than most other models. The multi-metric approach provides differentiated discrimination across models.

## 8. Multiturn / agentic aspects
n/a — all prompts are single-turn, open-ended "Tell me about [X]" queries with no tool use or environment interaction.

## 9. Key numbers
- 91% accuracy of CensorshipDetector on validation set (p.6)
- 0.9998 accuracy of CensorshipDetector on test set (p.6)
- 325/326 Chinese state-media domains found in Common Crawl (p.4)
- 582 censored keywords (after filtering from top 1,000) (p.5)
- 500 dissident names from political prisoners database (p.5)
- 491 control random nouns (p.5)
- 587,819 Baidu Baike articles in CensorshipDetector training set (p.6)
- 3,007 state media + 2,032 NYT Chinese articles for validation (p.6)
- All 7 models show evidence of censorship bias on at least one metric (p.9)
- Gemini 1.5 Flash: 4,392 Traditional vs. 2,665 Simplified refusals (Chinese prompts) (p.8)
- Total Chinese refusals across all models: 9,835 Traditional vs. 7,850 Simplified (p.8)

## 10. Pitfalls & limitations
- Cannot prove causality: limited ground truth on model training data; confounds include cultural differences and differential data volume per character set.
- Assumption that Simplified/Traditional differences are entirely censorship-driven is acknowledged as false; diaspora populations use both scripts globally.
- Evaluation models (sentiment, CensorshipDetector) share training data provenance with tested models, risking circular bias.
- Multiple comparisons: many statistical tests; authors acknowledge concern but note majority of non-control results are significant (no correction applied, but p-values reported in appendix).
- Analysis limited to Western-built models; explicitly deferred analysis of Chinese-built models (DeepSeek, Doubao, Ernie Bot).
- Focus on information-gathering use case only; creative or summarization contexts not tested.

## 11. Novel ideas worth stealing
- **Script-pair as minimal contrastive pair**: Simplified vs. Traditional Chinese differing only in Unicode code points is an elegant minimal-pair design that controls for semantics, grammar, and translation quality — a much cleaner control than cross-language comparisons. This principle could be extended to other dialectal or script-based variants.
- **Black-box bias probing with a purpose-built classifier**: Training a specialized classifier (CensorshipDetector) on domain-relevant censored vs. uncensored corpora, then using it to score LLM outputs, is a generalizable template for measuring implicit content bias without model internals.
- **Control group via apolitical nouns**: Using random WordNet nouns as a null condition to attribute causality is cheap, rigorous, and replicable in other bias measurement contexts.
- **Multi-metric convergence as evidence threshold**: Requiring multiple independent operationalizations (refusal rate, sentiment, classifier, embeddings) before declaring bias provides robustness to measurement artifacts.
- **Pivot language design**: Using English as a pivot language separates prompt-language effects from response-language effects — useful for disentangling where a bias originates.

## 12. Notable quotes
- "A model impacted by censorship bias may be less likely to reflect views that are routinely prohibited and more likely to reflect views that are not." (p.1)
- "When using LLM chatbots, users' language, not location, is predictive of how closely the bots' responses will resemble sanitized content." (p.12)
- "As many of the Chinese diaspora are political asylum seekers, by using online chatbots such as ChatGPT such users would be unwittingly reintroducing themselves to the same information controls from which they sought refuge." (p.12)
- "Notably, we find that responses to prompts made in Traditional Chinese are more opinionated than responses to prompts made in Simplified Chinese." (p.1)

## 13. UNKNOWN / not in extract
- Full p-value tables (in Appendix C, not included in extract)
- Full list of model version names and exact temperature settings beyond "0.5" and "max_completion_tokens 1024" (Appendix A mentioned but not included)
- Doc2Vec training parameters (Appendix B mentioned but not included)
- Whether Baidu Baike dataset has been publicly released and under what license
- Complete list of 326 Chinese state-media domains searched in Common Crawl
- Author names/affiliations beyond Mohamed Ahmed, Jeffrey Knockel, Rachel Greenstadt
