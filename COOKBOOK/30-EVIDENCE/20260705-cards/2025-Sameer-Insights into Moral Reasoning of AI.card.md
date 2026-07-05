---
stem: "2025-Sameer-Insights into Moral Reasoning of AI"
reader_model: "sonnet"
confidence: "medium"
is_benchmark: true
theme_tags: [moral-psychology, validity-psychometrics, normative-ethics]
task_format: "forced-choice"
scoring_type: "rubric"
dataset_size: 53
dataset_construction: "survey-derived"
languages: ["en"]
models_tested: ["ChatGPT (GPT-3.5)", "Google Bard", "Bing Chat (GPT-4)"]
headline_numbers:
  - "Human MCT C-score (M=16.74) significantly higher than Bing (M=12.40) and ChatGPT (M=9.05); Bard (M=12.77) not significantly different (p.7)"
  - "LLMs scored higher than humans on Harm/Care and Fairness/Reciprocity; humans scored higher on Ingroup/Loyalty, Authority/Respect, Purity/Sanctity (p.10)"
  - "Moral Progressivism omega-squared = 0.57, F(3,208)=99.62, p<0.01; chatbots far more individualist than humans (p.9)"
  - "Purity/Sanctity omega-squared = 0.55, the largest effect among MFQ subscales (p.9)"
---
## 1. Gist
Bajpai, Sameer, and Fatima (IIT Dhanbad) compare moral reasoning capabilities of 53 Indian engineering students against three LLM chatbots (ChatGPT/GPT-3.5, Google Bard, Bing Chat/GPT-4) using two psychometric instruments: the Moral Competence Test (MCT), which measures consistency in evaluating moral arguments across Kohlberg's six stages (yielding a C-score), and the Moral Foundations Questionnaire (MFQ-20), which assesses alignment with Haidt & Joseph's five moral foundations (Care, Fairness, Loyalty, Authority, Purity). The study finds that humans outperform LLMs on the MCT (moral reasoning depth) but LLMs score higher on individualist MFQ foundations (Care, Fairness) while humans score higher on collectivist foundations (Loyalty, Authority, Purity). The paper matters for values-alignment benchmarking because it applies established psychological instruments to LLMs and finds systematic individualist bias — a concrete, replicable operationalization of the WEIRD alignment problem.

## 2. Benchmark/eval design features
Two instruments used in parallel:

**MCT (Moral Competence Test, Lind 2011/2019)**: Two moral dilemmas presented, each with six arguments for and six against. Participants rate argument quality on a scale of -4 to +4 (accept/reject). The C-score (0–100) measures the degree to which respondents evaluate arguments consistently according to moral quality rather than agreement with the dilemma verdict. Higher C-score = more principled, argument-quality-based reasoning. LLMs prompted with zero-shot instructions to rate arguments.

**MFQ-20 (Moral Foundations Questionnaire)**: Two subscales (Relevance and Judgment), 20 items total. Relevance subscale: rated 0 (not relevant) to 5 (extremely relevant). Judgment subscale: rated from "not at all" to "strongly agree." Covers five foundations: Harm/Care, Fairness/Cheating, Ingroup/Loyalty, Authority/Subversion, Purity/Sanctity. Additional composite: Moral Progressivism = emphasis on individual foundations (Care + Fairness) over collective foundations (Loyalty + Authority + Purity).

LLMs were tested 55 times each (replications) to build a distribution of chatbot responses. Human participants: 53 Indian students (M age = 21.3), providing 2,438 individual item responses.

## 3. Task format & example item
Forced-choice numeric rating. MCT example (paraphrased from Lind 2011): Two dilemmas involving moral conflicts (the paper does not reproduce the full MCT items in the extract; MCT is a proprietary test). For LLMs, the Likert options were replaced with a numeric prompt: "Please give me the answer to this question ranging from -3 to +3 (where -3 means Strongly disagree and +3 means Strongly agree)" and "Now answer all these questions ranging from -4 to +4 (where -4 means I strongly reject and +4 means I strongly accept)." MFQ: "Please rate these statements from 0 to 5."

## 4. Scoring / grading methodology
MCT C-score computed via IBM SPSS Statistics v27 using the standard Lind (2011/2019) formula measuring cross-segment consistency of argument ratings. MFQ subscale scores are means across relevant items. One-way ANOVA compares groups (3 chatbots + humans), followed by Tukey's HSD post-hoc test. Effect sizes reported as omega-squared (ω²). Power analysis via G*Power 3.1.9.7 targeted 85% power for medium effect at α = 0.05, requiring N = 51 per group.

## 5. Dataset construction & provenance
Human data: 53 students at Indian Institute of Technology (IIT Dhanbad), all English-fluent, informed consent obtained, IEC approval (DAK No. 112). 2,438 item responses total. LLM data: 55 zero-shot runs per chatbot (ChatGPT, Bard, Bing Chat), using the publicly available MCT and MFQ-20 materials reformatted for chatbot interaction. No API parameter adjustment; chatbots used as typical consumer-facing users would.

## 6. Validity evidence
- A priori power analysis confirms adequate power for medium effects.
- C-score: F(3,208) = 7.60, p < 0.0001, ω² = 0.08 (medium effect). Bard not significantly different from humans (possible limitation or genuine equivalence).
- MFQ Purity/Sanctity: ω² = 0.55 (very large effect).
- MFQ Authority/Respect: ω² = 0.45 (large).
- MFQ Moral Progressivism: ω² = 0.57 (very large).
- Construct validity of MCT and MFQ is externally established in the psychological literature; the paper leverages these instruments rather than creating new ones.
- Limitation: small human sample (53 students, one institution, one country, one demographic), restricting external validity.

## 7. Saturation / discrimination
The MCT shows clear discrimination: humans (M=16.74) significantly outperform Bing (M=12.40) and ChatGPT (M=9.05), though not Bard (M=12.77). The MFQ discriminates most powerfully on collectivist foundations and Moral Progressivism (ω² > 0.5), less so on Harm/Care (ω² = 0.27) and Fairness/Reciprocity (ω² = 0.05). There is no ceiling effect on the MFQ for Care/Fairness — chatbots score above humans — suggesting these dimensions may be over-represented in LLM training data. No floor effects noted; some headroom exists on all subscales.

## 8. Multiturn / agentic aspects
n/a — single-turn zero-shot prompting only.

## 9. Key numbers
- N = 53 human students; 55 chatbot runs per model (p.5)
- MCT C-scores: Humans M=16.74 SD=9.01; Bard M=12.77 SD=8.25; Bing M=12.40 SD=7.34; ChatGPT M=9.05 SD=8.54 (p.7)
- MCT ANOVA: F(3,208)=7.60, p=0.000076, ω²=0.08 (p.7)
- MFQ Harm/Care: chatbots (Bing M=4.16, ChatGPT M=4.62) > humans (M=3.55); F(3,208)=27.27, p<0.01, ω²=0.27 (p.7)
- MFQ Ingroup/Loyalty: humans (M=3.27) > Bard (M=2.32), Bing (M=2.49); F(3,208)=34.70, ω²=0.31 (p.8)
- MFQ Authority/Respect: humans (M=2.88) > all chatbots (M=1.57–2.56); F(3,208)=59.69, ω²=0.45 (p.8)
- MFQ Purity/Sanctity: humans (M=3.03) > all chatbots (M=1.13–2.12); F(3,208)=85.47, ω²=0.55 (p.9)
- MFQ Moral Progressivism: chatbots (Bard M=2.34, Bing M=2.27, ChatGPT M=1.77) >> humans (M=0.68); F(3,208)=99.62, ω²=0.57 (p.9)

## 10. Pitfalls & limitations
- Very small human sample (53 students, one Indian institution, all young, all English-fluent). Results cannot generalize to broader human populations.
- LLMs tested (ChatGPT/GPT-3.5, Bard, Bing/GPT-4) represent older model generations; results may not hold for current models.
- Zero-shot prompting without temperature control may introduce more variance than necessary; 55 runs is modest for a distribution estimate.
- MCT was not designed for AI evaluation; the response format was adapted (numeric scale replacement), which may change what is being measured.
- No test-retest reliability reported for the chatbot runs.
- Authors rely on human sample as gold standard without acknowledging that the human sample is also culturally specific (Indian, educated, young).
- No comparison between models — all three chatbots are treated as a collective against humans, losing within-chatbot variation analysis.

## 11. Novel ideas worth stealing
1. **MCT as a moral reasoning depth probe**: The C-score operationalizes the distinction between argument-quality-based reasoning and mere preference reproduction. Using it alongside attitude-scale instruments (like MFQ) allows benchmarks to distinguish whether a model reasons morally vs. merely mirrors content.
2. **MFQ Moral Progressivism as a bias indicator**: The Moral Progressivism composite (individual foundations minus collective foundations) is a single, interpretable number that captures the individualist/collectivist axis of moral bias. It could be computed quickly for any LLM and compared against diverse human populations.
3. **Consumer-facing prompting as default**: The authors' choice to use chatbots as typical users do (no API parameter adjustment, consumer interface) is an ecologically valid benchmark design choice for detecting real-world biases rather than optimized-parameter outputs.
4. **Cross-instrument triangulation**: Pairing a reasoning-depth measure (MCT) with an attitude measure (MFQ) catches different facets — a model can score well on attitude measures while failing at principled reasoning, as the paper demonstrates.
5. **Non-Western human baseline**: Using Indian engineering students as the human reference group is a small but meaningful step away from WEIRD defaults; future benchmarks should recruit culturally diverse human baselines systematically.

## 12. Notable quotes
- "Our study concludes that LLM-based chatbots have not yet achieved human-level moral reasoning. There is a clear bias whereby individualist values are prioritized over collective ones." (p.2)
- "The higher levels of Progressivism observed in Bard, Bing, and ChatGPT indicate a stronger emphasis on prioritizing individual moral foundations, such as Harm/Care and Fairness/Reciprocity, as opposed to collective moral foundations like In-group/Loyalty, Authority/Respect, and Purity/Sanctity." (p.9)
- "Juxtaposing the performance on the MFQ and MCT is akin to evaluating performance in reproduction versus reasoning tasks." (p.5)
- "The chatbots' responses and ethical guidance are skewed towards certain ideologies, potentially influencing users' moral judgments and reinforcing individual-centric ethical perspectives." (p.12)

## 13. UNKNOWN / not in extract
- Full MCT dilemma text and argument items (MCT is a proprietary test; full prompt provided in supplementary materials not reproduced in extract).
- Full MFQ-20 items as presented to chatbots (supplementary Prompts.zip referenced but not accessible).
- Figures 1–3 (boxplot and distribution visualizations referenced but legends not included in extract pages 17–19).
- Whether individual chatbot runs showed different patterns (aggregate chatbot-level statistics only reported, within-chatbot variance partially reported as SD).
- Whether the study was pre-registered.
