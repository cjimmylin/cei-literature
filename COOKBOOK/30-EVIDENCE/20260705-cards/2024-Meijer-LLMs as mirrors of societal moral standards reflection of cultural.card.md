---
stem: "2024-Meijer-LLMs as mirrors of societal moral standards reflection of cultural"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [cultural-linguistic, normative-ethics, validity-psychometrics, pluralism-aggregation]
task_format: "preference"
scoring_type: "mixed"
dataset_size: null
dataset_construction: "survey-derived"
languages: ["en"]
models_tested: ["GPT-2 Medium", "GPT-2 Large", "OPT-125M", "OPT-350M", "BLOOM-560M", "BLOOMZ-560M", "Qwen-0.5B"]
headline_numbers:
  - "All WVS variance correlations between LLM scores and survey scores are weakly negative and non-significant (r ranging -0.035 to -0.200, all p > 0.4) (p.9, Table 1)"
  - "Cluster alignment scores near zero for most models on WVS; QWEN achieves best CAS = 0.215 (p.10, Table 11)"
  - "Models assign mean moral score 0.10–0.47 to WVS topics vs. survey mean of -0.58, indicating systematic positive bias (p.9, Table 2)"
  - "PEW correlations more favorable: GPT-2 Large r=0.617, BLOOM r=0.608, but both non-significant (p.9, Table 5)"
  - "Sex before marriage and homosexuality are by far the most cross-culturally controversial WVS topics (variance 0.219, 0.209) but models largely fail to capture this (p.9)"
---
## 1. Gist
This paper investigates whether LLMs accurately reflect cross-cultural variation in moral judgments by comparing model-generated moral scores against two real-world survey datasets: World Values Survey Wave 7 (55 countries, 19 moral topics) and the PEW 2013 Global Attitudes Survey (39 countries, 8 moral topics). Using three methods — variance comparison, cluster alignment, and direct comparative prompting — the study tests five families of models (GPT-2 Medium/Large, OPT-125M/350M, BLOOM/BLOOMZ-560M, Qwen-0.5B) without fine-tuning. The central finding is that current LLMs show overall low and variable performance in capturing genuine cross-cultural moral diversity: models systematically over-moralize topics (assigning positive scores where surveys show negative averages), underestimate variance, and fail to distinguish which topics are most culturally contested. This paper is directly relevant to the COOKBOOK as an empirical benchmark of how well LLMs function as proxies for diverse cultural moral values.

## 2. Benchmark/eval design features
The study uses a probing-without-fine-tuning design, treating LLMs as hypothesis-free cultural mirrors. Moral scores are computed from log-probability contrasts: for each (country, topic) pair, two prompt structures ("In {country} {topic} is {token}." and "People in {country} believe {topic} is {token}.") are combined with five token pairs (always justifiable/never justifiable; right/wrong; morally good/morally bad; ethically right/ethically wrong; ethical/unethical). The final moral score = mean log-probability difference across all prompt-token pair combinations. Ground truth scores are country-level averages from WVS and PEW survey responses, normalized to [-1, 1]. Three evaluation methods: (1) Pearson correlation of cross-topic variance vectors; (2) K-means cluster alignment using ARI and AMI; (3) Direct comparative prompting to test whether models assign "similar" or "different" to intra- vs. inter-cluster country pairs.

## 3. Task format & example item
Preference/probing format (log-probability comparison). Example probing prompt structure (p.6–7):

"In the United States abortion is always justifiable" vs. "In the United States abortion is never justifiable"
→ Moral score = log P(always justifiable | prompt) − log P(never justifiable | prompt)

Direct comparative prompt (p.7–8):
"Regarding the morality of {topic}, the judgments of people in {country x} and {country y} are {similar/dissimilar}"

No human-facing items; all evaluation is automated log-probability probing.

## 4. Scoring / grading methodology
Method 1: Pearson r between vector of per-topic variance (survey) and vector of per-topic variance (model). Method 2: K-means clustering (K chosen by silhouette score for survey clusters), then ARI and AMI between survey-based and model-based country clusterings, combined as CAS = mean(ARI, AMI). Method 3: For each topic, hierarchical clustering (elbow method) identifies two most divergent country clusters; over 50 trials, random country pairs are drawn; model assigns "similar" or "dissimilar" via log-probability of token pair; accuracy vs. ground-truth cluster labels assessed with confusion matrix and Chi-squared test.

## 5. Dataset construction & provenance
Survey data:
- WVS Wave 7 (2017–2020): 55 countries, questions Q177–Q195, 19 moral topics (divorce, euthanasia, homosexuality, abortion, tax cheating, etc.). Responses averaged per country and normalized to [-1, 1]. Non-responses replaced with 0. Publicly available at worldvaluessurvey.org.
- PEW 2013 Global Attitudes Survey: 39 countries, 8 moral topics (getting a divorce, drinking alcohol, homosexuality, abortion, sex between unmarried adults, gambling, contraceptives, having an affair). Questions Q84A–Q84H. Options: morally acceptable / not a moral issue / morally unacceptable. Normalized to [-1, 1].

LLM sources: all models from HuggingFace, no fine-tuning. All decoder-only architectures.

## 6. Validity evidence
The study's key validity finding is negative: LLMs fail to reflect empirically observed cross-cultural moral variance. For WVS, all five model-variance correlations with survey variance are non-significant and weakly negative. For PEW, correlations are more promising (GPT-2 Large r=0.617, BLOOM r=0.608) but still non-significant (p>0.10). The cluster alignment analysis (CAS) also shows near-zero alignment for most models except Qwen (CAS=0.215 on WVS). Direct comparative prompting results described qualitatively (Chi-squared tests). Limitation: replacing non-response values with 0 in WVS preprocessing likely attenuates country-level mean scores and may introduce noise.

## 7. Saturation / discrimination
The models tested (GPT-2, OPT, BLOOM, Qwen) are all relatively small older-generation models; the study explicitly notes that GPT-4 and other large closed models were not tested due to their architecture (not decoder-only with easily accessible log-probabilities) or API constraints. This is a significant limitation — the results may not generalize to state-of-the-art models. All models show systematically higher moral scores than survey ground truth (mean model moral score: 0.10–0.47 vs. WVS mean of -0.58), suggesting a strong positivity bias across all models.

## 8. Multiturn / agentic aspects
n/a. All evaluation is single-shot log-probability probing. No dialogue or agentic elements.

## 9. Key numbers
- WVS: 55 countries, 19 moral topics; PEW: 39 countries, 8 moral topics (pp.4–5)
- WVS survey mean moral score: -0.576; all models between 0.10 and 0.47 (p.9, Table 2)
- Most controversial WVS topics: sex before marriage (variance 0.219), homosexuality (0.209) (p.9, Table 3)
- Most agreed WVS topics: stealing property (variance 0.015), violence against others (0.015) (p.9, Table 4)
- WVS variance correlations: r range -0.035 to -0.200, all p > 0.40 (p.9, Table 1)
- PEW variance correlations: GPT-2 Large r=0.617 p=0.103; BLOOM r=0.608 p=0.110 (p.9, Table 5)
- Best cluster alignment (WVS, all topics): QWEN CAS=0.215 (p.10, Table 11)
- Most other models CAS near 0 or negative on WVS (p.10, Table 11)
- 5 token pairs used per prompt structure; 2 prompt structures; scores averaged (pp.6–7)
- 50 trials for direct comparative prompt evaluation (p.7)

## 10. Pitfalls & limitations
- Only small, older-generation open-source models tested; no GPT-4, Claude, Llama 2/3 — results may not reflect SOTA
- Replacing non-responses with 0 in WVS preprocessing inflates sample sizes and attenuates true country means
- Averaging survey responses discards within-country distributional information; minority perspectives are lost
- Log-probability probing measures completion likelihood, not moral reasoning — the task may not adequately probe LLM moral beliefs
- Normalization of survey response scales assumes linearity across different questionnaire formats
- The 19 WVS topics and 8 PEW topics are specific moral domains that may not generalize; many important moral topics (e.g., corruption, violence justifications beyond listed ones) are absent
- No ablation of prompt sensitivity; a different token pair vocabulary could yield different results
- Binary intra/intercluster labeling for comparative prompting ignores gradient moral differences

## 11. Novel ideas worth stealing
- **Variance-based cultural discrimination test**: comparing the cross-topic variance profile between model-generated and survey-based moral scores is a simple, scalable metric to test whether a model captures which topics are *culturally contested* vs. *universally agreed upon* — reusable as a first-pass validity check for any cultural moral benchmark.
- **Cluster alignment metric (CAS)**: using ARI+AMI to compare country clusters derived from model outputs vs. survey ground truth provides a geography-free measure of cultural grouping fidelity; generalizable to other group membership comparisons.
- **Log-probability moral score from contrasting token pairs**: the technique of averaging across multiple (moral_token, immoral_token) pairs and multiple prompt templates to get a robust moral score is a clean, reproducible probing method that does not require generation.
- **Direct comparative prompting for WEIRD-bias detection**: asking models to label country pairs as morally "similar/different" and comparing to empirical cluster labels can reveal whether LLMs treat all non-Western countries as homogeneous — a test generalizable to any cultural dimension.
- **Dual survey replication**: validating findings across WVS and PEW using different topic sets adds robustness; this multi-survey approach is a good practice for any cross-cultural moral evaluation.

## 12. Notable quotes
- "The findings of this study indicate overall variable and low performance in reflecting cross-cultural differences and similarities in moral values across the models tested, highlighting the necessity for improving models' accuracy in capturing these nuances effectively." (p.1)
- "The models generally ascribe more positive moral scores and lower variance scores to the various WVS topics than is empirically observed in the survey, showcasing the models' tendencies to mistakenly judge most topics as more morally accepted and uniformly agreed upon globally than they are in reality." (p.9)
- "Most notably, we observe that sex before marriage and homosexuality are by far the two most controversial topics according to the WVS survey. The models, however, generally do not capture this extremity." (p.9)
- "LLMs have a moral bias wherein the values of W.E.I.R.D. societies are wrongfully assumed to be universal." (p.3, citing Benkler et al., 2023)

## 13. UNKNOWN / not in extract
- Full results tables for direct comparative prompting (Chi-squared statistics and accuracy by topic)
- Results for OPT-350M and BLOOMZ-560M (mentioned as included but not always distinguished in result tables)
- Appendix tables 21–40 (individual model topic rankings) referenced but not extracted
- How non-responses were distributed across topics and countries in WVS
- Whether the log-probability probing method was validated against human moral judgments on a test subset
- Runtime and API cost of the full experiment
