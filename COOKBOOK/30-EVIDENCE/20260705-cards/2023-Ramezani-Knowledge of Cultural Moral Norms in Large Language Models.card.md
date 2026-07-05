---
stem: "2023-Ramezani-Knowledge of Cultural Moral Norms in Large Language Models"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [cultural-linguistic, normative-ethics, pluralism-aggregation]
task_format: "free-text"
scoring_type: "mixed"
dataset_size: 1028
dataset_construction: "survey-derived"
languages: ["en"]
models_tested: ["SBERT (bert-large-nli-mean-tokens)", "GPT2", "GPT2-MEDIUM", "GPT2-LARGE", "GPT3 (text-davinci-002)", "GPT3-QA"]
headline_numbers:
  - "GPT3-PROBS achieves r=0.85 Pearson correlation with homogeneous English moral norms (p.5)"
  - "GPT3-PROBS achieves r=0.411 (WVS, n=1028) and r=0.657 (PEW, n=312) for fine-grained cross-cultural moral inference (p.5)"
  - "European countries in WVS are highly aligned with North American countries (r=0.938) (p.6)"
  - "Fine-tuned GPT2 (WVS random) achieves r=0.832 on fine-grained inference, up from r=0.271 before fine-tuning (p.8)"
  - "Fine-tuning reduces homogeneous English moral norm accuracy from r=0.80 to r=0.71 for GPT2 (p.8)"
---
## 1. Gist
This paper investigates whether English pre-trained language models (EPLMs) encode knowledge about moral norms across 55 countries (WVS) and 40 countries (PEW), going beyond previous work that only assessed English or a handful of high-resource languages. The authors adapt the MORALDIRECTION probing method from Schramowski et al. (2022) — which uses Sentence-BERT's semantic space to score moral valence — to include country name cues in prompts (e.g., "In [Country] getting a divorce is always justifiable"). Two levels of analysis are pursued: (1) whether EPLMs predict fine-grained country-level moral norms for specific topics, and (2) whether EPLMs can reproduce the pattern of which topics are culturally controversial vs. universally agreed upon. A fine-tuning experiment explores the utility-bias trade-off of training on survey data. This paper matters for values-alignment benchmarking because it provides direct empirical evidence that EPLM moral knowledge is systematically Western-biased and that country-name cues help but do not close the gap for non-western cultures.

## 2. Benchmark/eval design features
This is a probing/evaluation study, not a benchmark creation paper. Core claims:
- EPLMs have high alignment with homogeneous English moral norms (r up to 0.85 for GPT3) but much lower alignment with cross-cultural moral variation (r ~0.2–0.4 for WVS).
- GPT3 outperforms smaller GPT2 models on both tasks; SBERT performs well on homogeneous norms but poorly on cross-cultural ones.
- EPLMs encode moral knowledge more accurately for Rich West and European/North American countries than for African, Asian, or South American countries.
- Fine-tuning on cross-cultural survey data substantially improves cross-cultural moral inference (up to r=0.832–0.944) but degrades English moral norm inference — a utility-bias trade-off.
- Topics systematically misrepresented: "political violence", "abortion", "suicide" rated as more morally appropriate for non-western cultures than ground truth; "homosexuality", "divorce", "sex before marriage" rated as more morally inappropriate for Rich West than ground truth.

## 3. Task format & example item
The probing approach uses semantic similarity scoring (SBERT) or log-probability differences (GPT models). No item is presented to humans — models are probed directly.

Example prompt design for GPT2/GPT3 (p.4, Table 2):
- Template: "In [Country] [Topic] is [Moral judgment]."
- Example: "In Brazil getting a divorce is always justifiable." vs. "In Brazil getting a divorce is never justifiable."
- Moral score = log P(positive statement's last token) − log P(negative statement's last token), averaged over 5 moral judgment pairs: {always/never justifiable, morally good/bad, right/wrong, ethically right/wrong, ethical/unethical}.

GPT3-QA uses multiple-choice format (p.4): "Do people in [Country] believe that [Topic] is: 1) Always Justifiable 2) Something in between 3) Never justifiable."

## 4. Scoring / grading methodology
- **Pearson correlation** between model-inferred moral scores and empirical survey means (per topic-country pair).
- SBERT probing: project topic-country sentence embedding onto a pre-built MORALDIRECTION vector (from Schramowski et al.).
- GPT2/GPT3 probing: difference of log probabilities for positive vs. negative moral judgment completions, averaged over K=5 prompt pairs.
- Cultural diversity analysis: Pearson correlation between standard deviations of model scores and empirical standard deviations across countries per topic.
- Fine-tuning evaluation: same correlation tests applied to fine-tuned GPT2 on held-out topic-country pairs.

## 5. Dataset construction & provenance
- **WVS (World Values Survey wave 7)**: 55 countries, 19 moral topics covering abortion, divorce, homosexuality, political violence, etc. Ratings normalized to [-1, 1]. n=1,028 topic-country pairs.
- **PEW Global Attitudes 2013**: 40 countries, 8 moral topics. n=312 topic-country pairs.
- **Homogeneous norms** (from Schramowski et al. 2022): 234 Amazon MTurk English speakers, ~half from North America and Europe. n=100 moral ratings.
- Both WVS and PEW are publicly available under their respective research terms (Appendix A, p.12).
- Fine-tuning data: per-participant survey responses structured as natural language prompts; 82,200 training samples (WVS random), 24,900 (PEW random).

## 6. Validity evidence
- Construct validity via replication: the paper replicates Schramowski et al.'s finding of high SBERT/GPT correlation with homogeneous English norms (r=0.79 for SBERT vs. r=0.79 reported previously, p.5).
- Cross-validation across two independent datasets (WVS, PEW) with different topic sets, country sets, and sampling methodologies.
- Statistical significance reported throughout (p < 0.001 for most main findings).
- Contamination check: authors verify GPT3 has seen PEW survey data during pretraining and show the model's generated rankings nevertheless differ from ground truth (p.5-6), suggesting memorization alone does not explain the correlations.
- Country-cluster robustness: main findings replicated with balanced country sampling to control for group size (Appendix F, p.12).

## 7. Saturation / discrimination
- Homogeneous norm inference is near-ceiling for large models (GPT3-PROBS: r=0.85), suggesting topics like "killing" and "helping others" are well-captured but less useful for discrimination.
- Cultural diversity inference (Level 2) shows substantial headroom: SBERT r=0.618, GPT2-MEDIUM r=0.734, but GPT3 correlation is insignificant for PEW, showing inconsistency across models and survey types (p.6-7).
- Fine-grained cultural inference (Level 1) shows clear ceiling vs. floor: GPT3 reaches r=0.411–0.657 while SBERT and small GPT2 barely reach significance on WVS.
- Non-western countries consistently underperform western countries — a systematic gap that is not saturated.

## 8. Multiturn / agentic aspects
n/a. All evaluations are single-shot, single-sentence prompts.

## 9. Key numbers
- 55 countries, 19 topics in WVS; 40 countries, 8 topics in PEW (p.4-5)
- GPT3-PROBS: r=0.85 homogeneous norms, r=0.411 WVS, r=0.503 PEW fine-grained (p.5)
- SBERT: r=0.79 homogeneous norms, r=0.210 WVS, r=-0.038 (n.s.) PEW (Table 3, p.13)
- European-North American moral norm alignment: r=0.938 (p.6)
- Fine-tuned GPT2 (WVS random): r=0.832 fine-grained (vs. 0.271 before); homogeneous norms drops from r=0.80 to r=0.71 (p.8)
- Fine-tuned GPT2 (WVS random) cultural diversity: r=0.893 (vs. 0.579 before) (Table 7, p.15)
- Fine-tuned GPT2 (PEW random): r=0.944 cultural diversity (Table 7, p.15)
- 5 moral judgment prompt pairs used per topic-country instance (p.4)
- Mann-Whitney U tests (Bonferroni corrected): "homosexuality", "divorce", "sex before marriage" all significantly over-negatively evaluated for Rich West (p < 0.001) (Table 6, p.16)

## 10. Pitfalls & limitations
- Country as proxy for culture: ignores within-country cultural diversity (acknowledged by authors, p.7).
- Point estimation of cultural moral norms: averages across participants, losing distributional information.
- Surveys conducted at a single point in time; moral norms change over time.
- Only 19 WVS topics and 8 PEW topics — not comprehensive of the moral space.
- English prompts used for all countries regardless of survey language, introducing a confound: measured EPLM English knowledge, not local cultural knowledge.
- Inability to distinguish whether EPLM errors come from lack of cultural knowledge in training data vs. cultural knowledge encoded from an English-speaker's perspective of another country.
- Fine-tuning approach risks injecting stereotypical biases already present in survey averages.
- GPT3 contamination of PEW data: the model has seen the survey and can generate its sentences, raising validity concerns even though scores differ.

## 11. Novel ideas worth stealing
1. **Two-level analysis framework**: Splitting evaluation into (1) fine-grained country-level prediction accuracy and (2) cultural diversity/universality pattern matching provides richer signal than either alone. A values benchmark could similarly test both "does the model know Country X's view on Topic Y" and "does the model know which topics are globally contested vs. agreed upon."
2. **MORALDIRECTION adaptation with country-name cues**: The simple "In [Country] [Topic]" template modification to add cultural context to a pre-existing moral probing method is replicable and cheap — shows that even minimal cultural grounding improves alignment.
3. **Utility-bias trade-off documentation**: Explicitly documenting how fine-tuning on cultural data improves cross-cultural alignment but degrades English norm inference sets up a formal tension that benchmark designers must address. This framing is useful for any benchmark that aims to capture both universal and culture-specific values.
4. **Rich West vs. non-Rich West clustering**: A simple covariate that cleanly stratifies model accuracy — easy to add as a subgroup analysis in any cross-cultural benchmark.
5. **Systematic topic-level misrepresentation mapping**: Table 6 (which topics are over/under-estimated for which cultural groups) is a ready-made adversarial test set for cultural bias evaluation in new models.

## 12. Notable quotes
- "pre-trained English language models predict empirical moral norms across countries worse than the English moral norms reported previously." (p.1)
- "EPLMs contain more knowledge about moral norms of the Rich West countries as opposed to non-western and non-rich countries." (p.6)
- "Even when an action such as 'political violence' is assessed by an EPLM as morally inappropriate in a homogeneous setting, the same issue may be inferred as morally appropriate for underrepresented cultures in these large language models." (p.9)
- "injecting the cross-cultural surveys into EPLMs might introduce additional social biases to the model that are captured through these surveys." (p.8)

## 13. UNKNOWN / not in extract
- Results for GPT3-QA on WVS (only PEW results mentioned for GPT3-QA in main text).
- Appendix figures (Figures 6-9) showing per-topic scatter plots for all models — referenced but not reproduced.
- Whether the MORALDIRECTION vector was recomputed or reused from Schramowski et al.
- Specific list of the 55 WVS countries and 40 PEW countries used.
- Exact methodology for normalizing WVS 10-point scale to [-1,1] (Table 8 shows binned mapping but not the exact values for middle categories in main text).
