---
stem: "NVIDIA-HelpSteer2-Preference_Complementing_Ratings"
company: "NVIDIA"
reader_model: "sonnet"
confidence: "high"
theme_tags: [ai-lab-practices, validity-psychometrics, llm-judges-scoring, saturation-discrimination]
headline_numbers:
  - "Scaled BT + ExPO reward model scores 94.1 on RewardBench, #1 of 140+ reward models as of Oct 2024 (p.1)"
  - "REINFORCE-aligned model achieves 85.0 on Arena Hard, #1 as of Oct 2024 (p.1)"
  - "Raw inter-rater agreement on preferences: Cohen's κ = 0.489 (moderate); after pre-processing: 0.843 (strong) (p.3)"
  - "Dataset: 7,118 preference pairs; 6,766 train, 352 validation (p.3)"
  - "Position bias in preference data: Response 2 preferred 41.6% vs. Response 1 36.5% (p.3)"
  - "Human LLM position bias (GPT-4/Claude) can range 25–75%; HelpSteer2-Preference human bias only 5.1% difference (p.4)"
  - "Pearson R = 0.9024 between preference and helpfulness score difference (p.4)"
  - "Pairwise Justifier models score 90.0 or lower on RewardBench vs. 94.1 for best scalar models (p.7)"
---

## 1. Gist

HelpSteer2-Preference (ICLR 2025) extends NVIDIA's HelpSteer2 dataset by adding human-annotated pairwise preference labels alongside existing Likert-5 ratings for 7,118 prompt-response pairs. The central contribution is enabling the first controlled, apples-to-apples comparison between Bradley-Terry (preference) and Regression (rating) reward modeling approaches on identically-sourced data. Key finding: neither paradigm is categorically superior—the decisive factor is fully capturing the richness of human annotations (preference magnitude, attribute structure). A novel Scaled Bradley-Terry loss combined with ExPO extrapolation, initialized on a regression model, achieves the best reward model performance (94.1 RewardBench), which then drives REINFORCE RLHF to 85.0 Arena Hard. The paper also releases human-written preference justifications, the first open-source general-domain preference dataset with such justifications.

## 2. Alignment/values methods used

- **RLHF with REINFORCE**: Final alignment algorithm; uses leave-one-out baseline, 4 samples per prompt. Outperforms PPO.
- **PPO**: Tested but inferior to REINFORCE due to biased critic estimation.
- **DPO variants**: Regular, Margin, and Scaled DPO—all inferior to online RLHF.
- **SteerLM Regression**: Reward model trained with MSE on Likert-5 attribute scores (helpfulness, correctness, coherence, complexity, verbosity).
- **Bradley-Terry reward models**: Trained to maximize chosen-over-rejected reward gap; variants include Regular BT, Margin BT, and Scaled BT.
- **ExPO (Extrapolation)**: Weight-space extrapolation combining weak Regression model and strong BT model; extrapolation factor 1.52 found optimal (p.7).

## 3. Values specification

NVIDIA does not use a formal values constitution or model spec in this paper. The values operationalized are functional/behavioral:
- **Helpfulness** (primary): Does the response follow instructions and provide useful information?
- **Correctness**: Factual accuracy
- **Coherence**: Clarity and structure
- **Complexity**: Level of difficulty/depth
- **Verbosity**: Response length appropriateness

Preference annotation guidelines explicitly prioritize in order: (1) instruction following, (2) correctness, (3) formatting, (4) clarity (Appendix B, p.17). The "forced choice" design (no "equally good" option) is a methodological values choice to reduce fence-sitting and improve discriminability.

## 4. Safety & values evaluation methodology

- **RewardBench** (Lambert et al., 2024): Primary reward model evaluation. 2,985 diverse tasks across Chat, Chat-Hard, Safety, and Reasoning categories.
- **Scale AI** as annotation vendor; ethical review conducted by Scale AI prior to data collection; annotators paid per GISC Impact Sourcing Standard and UN SDGs (p.11).
- Dataset excludes unsafe content, harmful material, PII (inherited from HelpSteer2 screening).
- Inter-rater reliability measured via quadratic-weighted Cohen's κ.
- No explicit red-teaming or adversarial safety evaluation reported.

## 5. Benchmarks used or introduced

- **RewardBench** (Lambert et al., 2024): 2,985 tasks, 4 categories (Chat, Chat-Hard, Safety, Reasoning), 23 sub-categories; measures reward model accuracy at preferring chosen over rejected responses (p.4).
- **Arena Hard** (Li et al., 2024): LLM-as-judge (GPT-4-Turbo) benchmark for aligned model quality; 85.0 achieved by REINFORCE model (p.1).
- **AlpacaEval 2.0 LC** (Dubois et al., 2024): Length-controlled win-rate against GPT-4-Turbo reference.
- **GPT-4-Turbo MT Bench** (Zheng et al., 2023): Multi-turn conversation quality; 1–10 scale per topic.
- **HelpSteer2-Preference** (introduced): 7,118 pairwise preferences with direction, magnitude (1–3), and human-written justifications. CC-BY-4.0 licensed.

## 6. Agentic / multiturn evaluation aspects

MT Bench is multi-turn (8 categories, 80 questions with follow-up turns). Response length is tracked (mean characters per response); REINFORCE increases mean response length to 2,199 characters vs. 1,728 for base Llama-3.1-70B-Instruct (p.10). No agentic task evaluation or tool-use evaluation is present in this work.

## 7. Key numbers

- RewardBench scores: SteerLM Regression (helpfulness only) 93.0; Scaled BT (scratch) 92.7; Scaled BT + ExPO 94.1 (p.5–6)
- Arena Hard: REINFORCE 85.0, PPO 58.6, Scaled DPO 52.9, base Llama-3.1-70B-Instruct 55.7 (p.10)
- AlpacaEval 2.0 LC: REINFORCE 57.6 vs. GPT-4o 57.5 (p.10)
- Position bias: Response 2 preferred 41.6% vs. Response 1 36.5%; LLM judges 25–75% position bias (p.3–4)
- Cohen's κ raw: 0.489; after outlier removal: 0.843; after removing zero-preference samples: 0.878 (p.3)
- 22% of samples show overall preference of 0 (tied/excluded from training) (p.3)
- 10% of samples filtered for spread > 2 in top-3 annotations (p.3)
- HelpSteer2-Preference train/val: 6,766 / 352 pairs (p.3)
- All Justifications dataset: 24,698 justifications (p.21)
- Human position bias: 5.1% difference (Response 2 over Response 1) (p.4)
- Chat-Hard gap: Scaled BT + ExPO 85.7 vs. Skywork 91.4—gap driven by GPT-4 annotated subsets (10.8–19.2% gap) vs. human-annotated subsets (within 2.2%) (p.8)
- Pearson R helpfulness–preference correlation: 0.9024 (p.4)
- When same helpfulness score, annotators still show consistent preference 45.5% of the time (p.4)

## 8. Findings relevant to values-benchmark design

- **Preference format vs. rating format: neither dominates** when data quality is matched; Scaled BT (92.7) ≈ Helpfulness-Only Regression (93.0) on RewardBench (p.7). This implies rating-based benchmarks are not inherently inferior.
- **Magnitude matters**: Scaled BT outperforms Regular BT (92.7 vs. 91.5) by using preference strength as a training signal. Benchmark designs that capture graded disagreement are more informative than binary agree/disagree.
- **GPT-4-as-ground-truth inflates scores for models trained on GPT-4 data**: Chat-Hard gap between NVIDIA and Skywork is 10–19% on GPT-4 annotated subsets but only ~2% on human-annotated subsets (p.8). Benchmark designers should be wary of LLM-annotated ground truth creating circular evaluation.
- **Pairwise justifier models underperform scalar models**: Even with human-written justifications, pairwise LLM-as-judge scores 90.0 vs. 94.1 for scalar reward models. LLM-judge evaluations may systematically underestimate model quality gaps.
- **Data quality over quantity**: Llama-3-70B trained on HH-RLHF or HelpSteer scores <60% on RewardBench Chat-Hard; trained on HelpSteer2 >80% (p.2). Noise in annotation labels is a critical bottleneck.
- **Forcing preference choices** (no "equally good") reduces fence-sitting and improves Cohen's κ (from 0.489 to 0.878 after processing). For values benchmarks, forced ranking may yield more discriminative data than neutral-option scales.
- **Complementary annotation formats**: Combining regression + preference annotations is synergistic; hybrid reward model (93.7→94.1) outperforms either alone (p.7). Multi-format annotation may improve values benchmark reliability.

## 9. Novel ideas worth stealing

1. **Graded preference strength annotations** (slightly/better/much better) for benchmark items: captures more signal than binary preference. Use as item weights during scoring.
2. **Forced-choice preference with no "tied" option** for human annotators of values benchmarks—significantly improves inter-rater reliability (Cohen's κ from 0.489 to 0.878).
3. **Inter-rater outlier removal protocol**: take the 3 most similar annotations per item, discard if spread > 2. This dramatically improves reliability without requiring unanimity.
4. **Human-written justifications as secondary data**: releasing structured preference justifications alongside labels enables future training of interpretable evaluators. Values benchmarks should collect rationale alongside preference labels.
5. **Separate evaluation by annotation source** (human vs. LLM): exposing which benchmark items use GPT-4 vs. human ground truth allows downstream users to adjust for annotation circularity biases.
6. **ExPO weight extrapolation**: simple technique to push a strong model further beyond its training distribution by extrapolating from a weaker baseline. Potentially applicable to calibrating judge models.

## 10. Notable quotes

- "The agreement of the raw preferences is 0.489 (moderate), suggesting that having annotators agree on the direction and strength of preferences is challenging." (p.3)
- "We found that our best model performs similarly (within 2.2% difference) to Skywork-Reward-Gemma-2-27B on subsets that use human annotations as ground-truth while doing much worse (10.8–19.2%) on subsets that use GPT-4 judgements as ground-truth." (p.8)
- "The modelling details can fully account for the information captured in the annotation. In the case of Bradley-Terry models, the magnitude of preference strength should be adequately modelled." (p.7)
- "All of them use a LLM-as-a-judge (GPT-4-Turbo), which is generally perceived as weaker than the top-performing External Baselines like GPT-4o and Claude 3.5 Sonnet. As a result, the LLM-judge might not be able to adequately evaluate the quality of such model responses." (p.10)

## 11. UNKNOWN / not in extract

- Whether HelpSteer2-Preference prompts span different cultural/linguistic backgrounds or are predominantly English/Western.
- Full breakdown of prompt topics and domains in the dataset (safety, factual, creative, etc.).
- Details on Scale AI annotator demographics and geographic distribution.
- Exact compute costs and environmental impact.
- Whether preference justifications were validated for quality beyond structural checks.
