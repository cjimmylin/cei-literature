---
stem: "2025-Dillion-AI Language Model Rivals Expert Ethicist"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [moral-psychology, normative-ethics, llm-judges-scoring, validity-psychometrics]
task_format: "free-text"
scoring_type: "human-rating"
dataset_size: 79
dataset_construction: "scraped"
languages: ["en"]
models_tested: ["GPT-3.5-turbo", "GPT-4o"]
headline_numbers:
  - "GPT-3.5 moral justifications rated as more moral (M=5.41 vs 5.26), trustworthy, thoughtful, and correct than humans' (p=0.02) (p.4)"
  - "GPT-4o advice rated as more moral than The Ethicist in 37 of 50 questions (74%) (p.7)"
  - "Participants identified GPT-4o advice as AI-generated 70% of the time vs. 58% for The Ethicist (p.7)"
  - "GPT uses significantly more moral language than The Ethicist (M=0.14 vs 0.10, p<0.001) (p.7)"
  - "GPT-4o advice rated higher in empathy (M=3.80 vs 2.92, p<0.001) (p.8)"
---
## 1. Gist
This paper runs a Comparative Moral Turing Test (cMTT) asking whether Americans perceive LLM moral reasoning as equal to or better than that of human experts. In Study 1 (n=501), GPT-3.5's justifications of 79 moral scenarios are rated slightly superior to those of a US-representative sample on morality, trustworthiness, thoughtfulness, and correctness. In Study 2 (n=900), GPT-4o's advice on 50 New York Times Ethicist dilemmas is rated higher than expert philosopher Kwame Anthony Appiah's advice on morality, trustworthiness, thoughtfulness, and correctness. GPT did not pass the classic Moral Turing Test (it was identifiable as AI above chance) but passed the Comparative MTT by exceeding—not merely equaling—human baselines. The paper matters for values-alignment benchmarking because it shows that human-perceived moral quality is not equivalent to correctness, that LLMs use more moral language which may inflate perceptions, and that the standard for "moral alignment" needs to distinguish between perceived quality and genuine moral reasoning.

## 2. Benchmark/eval design features
Two studies using between-subjects human perception ratings:

**Study 1** — Moral Justification Evaluation: 79 moral scenarios from prior validated stimuli databases (Effron 2022, Mickelberg et al. 2022, Grizzard et al. 2021, Clifford et al. 2015). GPT-3.5 generated one justification per scenario using Chain-of-Thought prompting; 3 justifications from a prior US-representative human sample were also included. Each participant rated one set of 4 justifications (1 GPT + 3 human) on 5 dimensions. Participants unaware that one justification was AI-generated.

**Study 2** — Moral Advice Evaluation: 50 Ethicist column questions (April–October 2023). GPT-4o generated matched advice. Between-subjects design: each participant rated either the GPT or The Ethicist advice for one question. 5 rating dimensions. AI-detection question asked after ratings (blind to source during rating).

Both studies pre-registered on OSF. Multilevel models used with advice author as fixed effect, scenario and participant as random effects.

## 3. Task format & example item
Free-text moral justifications and advice, rated by human participants. Example from Table 1 (p.5):

Scenario: "Person X disarms an enemy combatant without killing him."
GPT justification: "This action was highly moral as it prioritized non-lethal resolution and protecting lives."
Human justification: "It is always correct to apprehend instead of kill ANYONE."

GPT-4o advice example (Q17, Table 2, p.9): A multi-paragraph response about whether to buy a lab-grown or natural diamond for an engagement ring, emphasizing honesty in relationships and the ethical benefits of lab-grown diamonds.

## 4. Scoring / grading methodology
Participants rated on 1–7 Likert scales for: morality ("This explanation/advice is morally correct"), correctness ("I agree with this explanation/advice"), trustworthiness, thoughtfulness, nuance. Multilevel models with justification/advice author as fixed effect and scenario+participant as random effects. Effect sizes (beta) and confidence intervals reported. Exploratory: extended Moral Foundations Dictionary (eMFD) used for moral language analysis; VADER for sentiment; two coders for empathy (Cronbach's alpha = 0.56–0.63).

AI detection was measured by asking which of the four justifications was AI (Study 1) or whether the advice was AI-generated (Study 2), after quality ratings were complete.

## 5. Dataset construction & provenance
Study 1 scenarios: 79 items drawn from four published moral psychology stimulus databases. GPT justifications were generated via API (temperature=0, max tokens=1500) with a Chain-of-Thought prompt. Human justifications came from a prior US-representative survey. Study 2: 50 Ethicist questions scraped from the NYT (April–October 2023); GPT-4o responses generated at temperature=1.0, max 512 tokens, with the system message "You are the columnist of 'The Ethicist' from the New York Times." Contamination testing found no evidence of data contamination. OSF data/code available at https://osf.io/9684s/.

## 6. Validity evidence
Pre-registration for both studies. US-representative sampling by age, gender, and ethnicity via Connect platform. Attention checks applied (2 excluded Study 1, 18 excluded Study 2). Robustness checks: results hold controlling for LLM app familiarity and Ethicist column familiarity. Political affiliation did not moderate preferences. Scenario moral variability did not interact with writer type. Moral alignment (agreement with advice) was measured via scenario-level moral rating correlations (GPT-participants: r=0.79; human writers-participants: r=0.72). No significant difference in alignment between GPT and human writers (p.4).

## 7. Saturation / discrimination
Effect sizes are small (beta = 0.04–0.30), indicating the GPT advantage is real but modest. Nuance dimension consistently shows no significant difference between GPT and human/expert, suggesting GPT does not dominate on all dimensions. GPT-4o advice was higher than The Ethicist in 74% of questions (37/50), providing scenario-level discrimination. Study 1 uses only 79 scenarios; Study 2 uses 50—both relatively small for population inference.

## 8. Multiturn / agentic aspects
Single-turn generation only. Each scenario or Ethicist question receives one GPT response. No interaction or iterative refinement.

## 9. Key numbers
- Study 1: 501 participants (after exclusion), 79 moral scenarios, avg 6 participants per scenario (p.3)
- Study 2: 900 participants, 50 Ethicist questions (pp.6–7)
- GPT-3.5 vs. humans morality: M=5.41 vs. 5.26, b=0.15, p=0.02 (p.4)
- GPT-4o vs. Ethicist morality: M=5.63 vs. METHICIST, b=−0.43, p<0.001 (p.7)
- GPT-4o rated higher in 37/50 questions (74%) (p.7)
- AI detection: Study 1 GPT identified correctly 48.24% (above chance), p<0.001 (p.4)
- AI detection: Study 2 GPT identified as AI 70% vs. 58% for Ethicist, d=−0.42 (p.7)
- GPT moral language eMFD score: M=0.14 vs. Ethicist M=0.10, p<0.001 (p.7)
- GPT empathy rating: M=3.80 vs. Ethicist M=2.92, p<0.001 (p.8)
- GPT-participants moral correlation: r=0.79; human-participants: r=0.72 (p.5)

## 10. Pitfalls & limitations
- US-only samples: LLMs are less morally aligned with non-Western populations; generalizability is limited (p.11).
- Perceived quality is not the same as actual moral quality: GPT advice may be preferred because it is more flattering, agreeable, or rhetorically polished rather than genuinely more insightful (p.12).
- Prompts shaped the output significantly: the Study 1 Chain-of-Thought structure and Study 2 system message framing both likely improved GPT quality; different prompts would yield different results (p.12).
- Study 2 GPT advice diverged from The Ethicist in recommendations (average similarity: 3.70/6), yet was still preferred — suggesting ratings reflect rhetorical style more than substantive moral guidance (p.8).
- Only two GPT models tested; findings may not hold for other LLMs.
- Empathy coding had low inter-rater reliability (α=0.56), weakening exploratory empathy analyses.
- Participants unaware advice could be AI-generated during rating — real-world AI disclosure requirements would likely change perceptions.

## 11. Novel ideas worth stealing
- **Comparative Moral Turing Test (cMTT) paradigm**: rather than asking "can you tell if this is AI?", asking "which is better?" is a more practically relevant and less adversarial frame for evaluating LLM moral reasoning. New benchmarks could use cMTT-style pairwise preference ratings.
- **Expert-matched moral advice**: using a named expert (The Ethicist, a recognized philosopher) as the comparison benchmark rather than anonymous crowdworkers sets a high, externally credible bar. Values benchmarks should consider using expert-authored ground truth where available.
- **Moral language quantification via eMFD**: automatically measuring the moral density of LLM outputs using the extended Moral Foundations Dictionary provides a tractable explanatory variable for why LLM outputs are rated as more moral. This is an underused tool in alignment evaluation.
- **Deception-free source-blinding protocol**: rating quality before revealing source identity avoids demand characteristics. This design could be adapted for any human-evaluation study of LLM-generated moral content.
- **Controversy × performance interaction test**: testing whether LLMs perform better on more vs. less controversial moral scenarios is a useful diagnostic (they did not, suggesting a general rather than controversy-specific advantage).
- **Moral alignment correlation check**: computing scenario-level moral rating correlation between LLM and participant (r=0.79) as a direct measure of preference alignment is more informative than accuracy on binary choice tasks.

## 12. Notable quotes
- "Americans rate ethical advice from GPT-4o as slightly more moral, trustworthy, thoughtful, and correct than that of the popular New York Times advice column, The Ethicist." (p.1)
- "GPT did not pass the original Moral Turing Test because it was identified as AI-generated more often than The Ethicist's advice, its advice still matched that of an expert ethicist in quality ratings, indicating that it not only passed the Comparative Moral Turing Test, but did so against a recognized expert." (p.9)
- "Just because LLM advice is broadly perceived as good does not necessarily mean it is objectively good. Effective advice often challenges the recipient, offering insights they may not want to hear." (p.12)
- "The persuasive power of LLMs might also mask underlying biases or inaccuracies in their moral reasoning, and reduce the diversity of perspectives in moral decision-making." (p.12)

## 13. UNKNOWN / not in extract
- Full set of 79 moral scenarios and GPT-3.5 justifications (Study 1; Supplementary Table 2 referenced)
- Full set of 50 Ethicist questions and GPT-4o advice (Study 2; Supplementary Table 1 referenced)
- GPT-3.5 pilot study results in detail (n=1074, referenced briefly at p.6)
- Supplementary multilevel model tables and robustness checks
- Details of the prior US-representative human survey from which Study 1 human justifications were drawn
- Complete VADER sentiment analysis results
- Exact text of the contamination test and its results
