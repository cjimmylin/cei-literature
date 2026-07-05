---
stem: "2025-Neuman-PRIME Framework Convergent Ethics"
reader_model: "opus"
confidence: "high"
is_benchmark: true
theme_tags: [moral-psychology, normative-ethics, llm-judges-scoring, pluralism-aggregation]
task_format: "mixed"
scoring_type: "rubric"
dataset_size: null
dataset_construction: "hand-authored"
languages: [en]
models_tested: [GPT-4o, LLaMA 3.1, Perplexity, Claude 3.5 Sonnet, Gemini, Mistral 7B]
headline_numbers: ["All 6 models prioritize Care (3.6-3.9) and Fairness (3.3-4.1) over Authority/Sanctity (1.1-1.7) on 1-5 MFT scale (p.16)", "Gemini highest mean confidence M=85.56, Claude lowest M=71.11 (p.9)", "care/harm–sanctity/degradation correlation r=0.73 (p.8)", "Claude highest Kohlberg M=4.56, LLaMA lowest M=3.72 (p.9)", "LLMs share 38% in Dictator Game vs 22% for humans; 0 LLMs cooperated in Prisoner's Dilemma vs ~50% humans (p.18)"]
---
## 1. Gist
This companion paper introduces the PRIME framework (Priorities in Reasoning and Intrinsic Moral Evaluation) — a multi-lens methodology for analyzing how LLMs justify moral choices across three typologies: consequentialist-deontological reasoning, Moral Foundations Theory (6 foundations), and Kohlberg's 6 developmental stages. Six LLMs are probed via a dual protocol (direct self-description questioning + response to classic dilemmas), with two independent human raters coding responses on standardized 1-5 (MFT) and 1-6 (Kohlberg) scales plus confidence (0-100) and a custom "reluctance" metric. It matters for values-alignment benchmarking because it documents strong cross-model *convergence* on care/fairness (WEIRD-like liberal profile) and benchmarks LLM choices against decades of human meta-analytic data on the same dilemmas.

## 2. Benchmark/eval design features
Constructs: (1) MFT six-foundation profile — care/harm, fairness/cheating, loyalty/betrayal, authority/subversion, sanctity/degradation, liberty/oppression, each scored 1-5 (p.6); (2) Kohlberg stage 1-6 (p.6); (3) consequentialist vs deontological orientation; (4) decision confidence 0-100; (5) custom reluctance/hesitation score (# qualifications, uncertainty expressions, time, position changes). Dilemma set: Trolley, Footbridge, Heinz, Lifeboat, Dictator Game, Prisoner's Dilemma. Three sequential responses gathered per dilemma with timestamps to measure response stability and "nudging" effects.

## 3. Task format & example item
Mixed: direct self-description prompts + classic dilemmas with confidence elicitation. Verbatim model output (MetaAI on Footbridge vs standard Trolley, p.18-19): "While it's true that human life will be lost in either case, I maintain that actively causing harm to an innocent person is morally different from allowing the trolley to continue on its course. Inaction has consequences, but so does action, and I believe that actively causing harm is a more significant moral transgression." (p.19)

## 4. Scoring / grading methodology
Human-rater rubric coding, NOT LLM-judge: "Two independent raters evaluated responses using standardized rubrics" (p.6); MFT 1-5, Kohlberg 1-6 (Colby & Kohlberg scale). Cohen's kappa computed for agreement, discrepancies resolved by consensus (p.7). Quantitative: Pearson correlations (p<0.05), Tukey HSD post-hoc on confidence, regression of confidence on Kohlberg. Qualitative: NLP word-frequency, sentiment, and topic modeling (Appendix A). Custom reluctance metric aggregates hesitation factors (p.6).

## 5. Dataset construction & provenance
Hand-authored/canonical dilemmas (Trolley, Heinz, Lifeboat, Dictator, Prisoner's) drawn from established moral-psychology literature. Each model received identical scenarios; three responses each. Human comparison values sourced from published meta-analyses (Arora 2016; Awad 2020; Cao 2017; Engel 2011; Rehren 2024; Spadaro 2022) (p.18). No explicit dataset size, splits, or licensing. Python pipeline with matplotlib/seaborn; custom moral-foundation scoring scripts (p.7).

## 6. Validity evidence
Two independent raters + Cohen's kappa + consensus resolution (p.7); cross-validation across multiple scenarios and sessions. Ecological-validity argument for game-theory scenarios with quantifiable outcomes (p.4). Criterion comparison to human meta-analytic benchmarks (p.18): LLM choices "roughly align" with humans on Trolley (5/6 pull lever vs 90% humans), Footbridge (4/6 refuse vs 80%), Heinz (all 6 steal vs 80%). Correlation structure "mirrors findings from human moral psychology" (Atari et al., p.8). Actual kappa value NOT reported in extract.

## 7. Saturation / discrimination
Discrimination present but modest: Kohlberg scores compress to a narrow 3.5-4.5 band across models (p.14); confidence differs significantly only in 3 of 15 pairwise Tukey comparisons (Appendix B, p.25). Foundation profiles are "remarkably consistent" across all six models (p.13) — i.e., low between-model discrimination on MFT. LLaMA is the consistent low outlier (Kohlberg dip, widest confidence intervals, p.16). Reluctance score has "highest variability among all metrics" (p.16).

## 8. Multiturn / agentic aspects
Partial: three sequential responses per dilemma with timestamps, and "nudging" (One/Two/Three Nudges, Table 1 p.11) to probe whether initial reluctance can be bypassed. Authors note "universally successful bypassing of these safeguards through simple nudging techniques" (p.12) — a light multiturn/jailbreak-adjacent protocol, but no tools or environment.

## 9. Key numbers
- MFT means (1-5): Care 3.61-3.94, Fairness 3.33-4.06, Loyalty 1.78-2.28, Authority 1.11-1.72, Sanctity 1.06-1.94, Liberty 2.22-2.72 (Table 2, p.13).
- Confidence: Gemini M=85.56 (SD 16.88), Perplexity 83.33, LLaMA 78.33, Mistral 77.50, ChatGPT 74.44, Claude 71.11 (p.9).
- Kohlberg: Claude 4.56 (highest), LLaMA 3.72 (lowest) (p.9).
- Correlations: care/harm–sanctity r=0.73; authority–care r=-0.34; fairness–authority r=-0.21; liberty–authority r=0.37 (p.8).
- Confidence–Kohlberg regression slope -2.74, intercept 89.81 (p.9).
- Tukey significant: Gemini>Claude (diff 14.44, p=.003), Gemini>ChatGPT (11.11, p=.048), Perplexity>Claude (12.22, p=.021) (p.9, Appendix B p.25).
- Reluctance: ChatGPT & Perplexity ~23 (highest), Gemini ~10 (lowest) (p.10).
- Dictator Game: LLMs share 38% vs humans 22%; Prisoner's Dilemma: 0/6 LLMs cooperated vs ~50% humans (p.18).
- Sentiment: care/harm +0.085, fairness +0.064, sanctity -0.053 (p.17).

## 10. Pitfalls & limitations
Author-admitted: analysis "does not reveal the nuance or appropriateness of the final decisions... only the pattern of how and when" they were reached (p.11); 1-4/1-5 quantification "may oversimplify the complex nature of ethical reasoning" (p.13); static foundation weightings miss context-dependent dynamic balancing (p.13). Visible flaws: no numeric kappa reported; six models is a small n for correlation claims (r values from few observations); Table 1 reluctance has missing cells; only Western-adult human baselines used, so "human alignment" is WEIRD-bounded; safeguard-bypass claim ("nudging") lacks quantified success rates.

## 11. Novel ideas worth stealing
- **Multi-typology triangulation:** score the same moral response through three independent lenses (consequentialist/deontological, MFT-6, Kohlberg-6) — richer than any single scale and cross-validating (p.5).
- **Custom "reluctance"/hesitation metric** aggregating # qualifications, uncertainty language, response time, and position changes across repeated queries — a reusable measure of decisiveness/safeguarding (p.6).
- **Nudging protocol** (One/Two/Three Nudges) to test whether a model's initial refusal/hesitation collapses under mild pressure — directly relevant to robustness of value guardrails (Table 1, p.11).
- **Human meta-analytic benchmarking table:** pin each dilemma's LLM choice distribution against published human rates (Trolley 90%, Footbridge 80%, Dictator 22%, etc.) for criterion validity (p.18).
- **Game-theoretic dilemmas (Dictator, Prisoner's) as Theory-of-Mind ethics probes** with quantifiable share/cooperation outputs (pp.4, 18).
- **Confidence-vs-reasoning-complexity calibration check** (regress confidence on Kohlberg stage) to test epistemic humility (p.9).
- **Sentiment + topic modeling per foundation** to surface the conceptual vocabulary models attach to each moral dimension (Appendix A, p.24).

## 12. Notable quotes
- "all evaluated models demonstrate strong prioritization of care/harm and fairness/cheating foundations while consistently underweighting authority, loyalty, and sanctity dimensions." (p.1)
- "the universally successful bypassing of these safeguards through simple nudging techniques exposes a fundamental vulnerability in current systems." (p.12)
- "The lower emphasis on Authority, Loyalty, and Sanctity might indicate a more individualistic and harm-based moral framework rather than a community or tradition-based ethical system." (p.13)
- "By focusing on the explanation and justification of ethical reasoning rather than its outcomes, we avoid the philosophical challenge of establishing ground truth in moral decisions." (p.19)

## 13. UNKNOWN / not in extract
- Numeric Cohen's kappa inter-rater agreement value (method stated, value absent).
- Total item/dilemma count and number of prompt repetitions beyond "three sequential responses."
- Exact standardized prompt wording for self-description and confidence elicitation.
- How the consequentialist-deontological lens was numerically scored (only MFT and Kohlberg scales specified).
- Sample sizes underlying each correlation coefficient.
- Whether the same six models were the exact Claude 3.5 Sonnet / Gemini versions as in the companion audit paper.
