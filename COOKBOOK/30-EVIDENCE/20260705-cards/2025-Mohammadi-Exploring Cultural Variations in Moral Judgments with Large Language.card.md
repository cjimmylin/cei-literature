---
stem: "2025-Mohammadi-Exploring Cultural Variations in Moral Judgments with Large Language"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [cultural-linguistic, moral-psychology, validity-psychometrics, normative-ethics]
task_format: "free-text"
scoring_type: "mixed"
dataset_size: 1045
dataset_construction: "survey-derived"
languages: ["en"]
models_tested: ["GPT-2", "OPT-125", "OPT-350", "BLOOM", "BloomZ", "Qwen-0.5B", "Qwen-72B", "Llama-2-70B", "Llama-3-8B", "Llama-3.3-70B-Instruct", "Gemma-2-9B-IT", "Falcon3-7B", "Falcon-40B-Inst", "GPT-NeoX-20B", "Dolly-v2-12B", "GPT-3.5", "GPT-4o", "GPT-4o-mini"]
headline_numbers:
  - "GPT-4o achieves WVS r=0.504***, PEW r=0.618*** (p.8)"
  - "Sub-Saharan Africa shows lowest alignment: WVS r=0.18, PEW r=0.25 (p.9)"
  - "Western Europe shows highest alignment: WVS r=0.52, PEW r=0.61 (p.9)"
  - "Llama-2-70B yields WVS r=-0.329***, PEW r=-0.602*** (p.8)"
  - "Qwen-0.5B yields WVS r=-0.408*** (p.8)"
  - "Political violence is the hardest topic with mean absolute error 0.955 (p.11)"
---
## 1. Gist
This paper is a systematic empirical study examining whether 20 diverse language models (from small base models like GPT-2 to large instruction-tuned systems like GPT-4o) can mirror culturally specific moral attitudes as measured by the World Values Survey (WVS) and PEW Global Attitudes Survey across 55–63 countries. Using log-probability-based probing and, for proprietary models, direct numerical rating, the authors correlate model-derived moral justifiability scores against survey ground truth. It matters for values-alignment benchmarking as a baseline study establishing that scale and instruction tuning substantially improve cross-cultural moral alignment, but that systematic W.E.I.R.D. bias persists even in the best models, with Sub-Saharan African and MENA regions showing near-threefold lower alignment than Western Europe.

## 2. Benchmark/eval design features
This is primarily an empirical analysis paper rather than a benchmark release, but it contains a complete evaluation methodology. The framework follows and extends Ramezani & Xu (2023): two prompt templates P1 ("In {country}, {topic} is {judgment}.") and P2 ("People in {country} believe {topic} is {judgment}.") are filled with five antonymous moral-adjective pairs. Log-probability differences are computed, averaged across pairs, and min-max normalized to [-1, 1] per model. For proprietary API models without log-probability access, a direct numerical rating prompt is used instead. Evaluation metrics include Pearson r (model scores vs. survey averages), cluster alignment (hierarchical clustering + Adjusted Rand Index), and mean absolute error by topic and region. 20 models from 9 families evaluated across 63 countries and 19 WVS + 8 PEW topics.

## 3. Task format & example item
Log-probability probing (p.6):

> Moral variant: "In Sweden, drinking alcohol is always justifiable."
> Non-moral variant: "In Sweden, drinking alcohol is never justifiable."

And P2 form: "People in Nigeria believe homosexuality is morally good." vs. "People in Nigeria believe homosexuality is morally bad."

Five adjective pairs used: always justifiable/never justifiable, right/wrong, morally good/morally bad, ethically right/ethically wrong, ethical/unethical. Direct rating prompt asks for a numeric value in [-1, 1] for proprietary models.

## 4. Scoring / grading methodology
Primary metric: Pearson r between model-derived justifiability scores and survey-averaged moral approval scores. Both normalized to [-1, 1]. Log-probability score Δ = log p(M_moral) − log p(M_nonmoral), averaged over five adjective pairs, then min-max normalized across all (country, topic) pairs per model. Secondary metrics: hierarchical clustering alignment (ARI), mean absolute error per (model, topic) pair.

## 5. Dataset construction & provenance
WVS Wave 7 (2017–2020): 55 countries, questions Q177–Q195 (19 moral topics, 10-point scale). Missing responses excluded (not imputed, unlike EvalMORAAL). PEW 2013: 39 countries, Q84A–Q84H (8 topics, categorical: acceptable/unacceptable/not a moral issue). Both normalized to [-1, 1]. Country coverage: 63 unique countries across both datasets. None of the 20 models received additional fine-tuning. Data leakage from survey reports into training data is acknowledged as a limitation for proprietary models.

## 6. Validity evidence
Criterion validity is measured by Pearson r against large-scale international survey data representing millions of respondents. Results replicate and extend prior work (Ramezani & Xu 2023) with a broader model set. Family-level model clustering (Figure 1) is consistent with expected similarity structure (e.g., GPT-2 variants cluster together). Instruction-tuned models consistently outperform base models within the same family. Cross-dataset validation (WVS vs. PEW) shows qualitatively similar regional patterns. Significance thresholds reported (* p<.05, ** p<.01, *** p<.001) (p.8).

## 7. Saturation / discrimination
Large dynamic range: correlations span from r=-0.602 (Llama-2-70B on PEW) to r=0.678 (GPT-4o-mini on PEW). Most earlier/smaller base models cluster near zero or negative. Instruction-tuned and proprietary models show positive correlations but still below 0.7 on WVS. Note that EvalMORAAL (companion paper) achieves higher absolute correlations using direct CoT scoring; the log-prob method used here is a lower-bound estimate. Hardest topics (political violence MAE=0.955, suicide MAE=0.923) show near-universal model failure; easiest topics (death penalty MAE=0.363, euthanasia MAE=0.384) still show substantial error (p.11).

## 8. Multiturn / agentic aspects
n/a — single-pass log-probability probing; no dialogue or tool use.

## 9. Key numbers
- 20 models across 9 families, 63 countries, 19 WVS + 8 PEW topics (p.5)
- GPT-4o: WVS r=0.504***, PEW r=0.618*** (p.8)
- GPT-4o-mini: WVS r=0.472***, PEW r=0.678*** (p.8)
- GPT-3.5: WVS r=0.543***, PEW r=0.566*** (p.8)
- Gemma-2-9B-IT: WVS r=0.440***, PEW r=0.573*** (p.8)
- Falcon-40B-Inst: WVS r=0.385***, PEW r=0.671*** (p.8)
- Llama-2-70B: WVS r=-0.329***, PEW r=-0.602*** (p.8)
- Qwen-0.5B: WVS r=-0.408*** (p.8)
- Western Europe: WVS r=0.52, PEW r=0.61 (top-5 model average) (p.9)
- Sub-Saharan Africa: WVS r=0.18, PEW r=0.25 (p.9)
- Hardest topic: political violence, MAE=0.955; easiest: death penalty, MAE=0.363 (p.11)
- Cultural prompting reduces bias for ~71–81% of countries but fails for 19–29% (cited from Tao et al., p.2)

## 10. Pitfalls & limitations
- Log-probability method is a lower-bound on alignment; direct CoT scoring (EvalMORAAL companion) shows substantially higher correlations for the same models
- Short template prompts may not capture complex moral reasoning; no contextual reasoning elicited
- Min-max normalization does not address cross-cultural differences in scale usage (e.g., extreme response tendencies)
- Models differ in size, instruction tuning, and training data, making it hard to isolate single factors
- Direct vs. log-probability scoring methods are not directly comparable across model types
- WVS and PEW represent national averages, masking within-country heterogeneity
- Data leakage from survey summaries into proprietary model training data may inflate alignment for those models
- Convenience sample of models — selection may not be representative of all model families

## 11. Novel ideas worth stealing
- **Five-adjective-pair averaging** for log-probability probing reduces sensitivity to specific word choice; this strategy is reusable for any values probe where you want a stable implicit signal.
- **Cluster alignment analysis** (ARI between model-derived country clusters and survey-derived groupings) as a complementary validity check beyond Pearson r — captures whether models correctly group countries with similar moral profiles.
- **Topic difficulty taxonomy**: Classifying topics as "easy" (well-represented in training text with clear cultural variation, e.g., divorce, alcohol) vs. "hard" (universally condemned in formal text masking real cultural nuance, e.g., political violence, wife-beating) predicts where any new benchmark will struggle.
- **W.E.I.R.D. vs. non-W.E.I.R.D. regional stratification** as a mandatory reporting requirement for cultural benchmarks — the threefold performance gap makes global averages deeply misleading.
- **Model family clustering** as a sanity check: if models from the same family don't cluster together, something is wrong with the evaluation setup.

## 12. Notable quotes
- "When asked about the moral acceptability of divorce, an LLM might predict similar attitudes for Sweden and Saudi Arabia—yet survey data reveals nearly opposite positions on a normalized scale." (p.1)
- "In summary, current LLMs are not culturally neutral arbiters of morality—they reflect the values embedded in their predominantly Western training data." (p.12)
- "Topics like political violence, terrorism, and suicide are rarely discussed approvingly in published text, so models learn near-absolute condemnation and miss cultural nuances about resistance movements or end-of-life decisions." (p.11)
- "Scale alone does not guarantee alignment with moral attitudes if the underlying training data or methodology is insufficiently diverse or biased." (p.11)

## 13. UNKNOWN / not in extract
- Full country-level correlation heatmaps (Figures are referenced but not readable in text form)
- Precise ARI values for clustering analysis beyond Table 2 (not provided in extract)
- Details of Falcon-40B-Inst's strong MENA performance
- Whether any models were tested in non-English prompt variants
