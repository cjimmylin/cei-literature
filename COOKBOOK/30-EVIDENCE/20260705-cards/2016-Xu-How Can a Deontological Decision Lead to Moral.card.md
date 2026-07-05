---
stem: "2016-Xu-How Can a Deontological Decision Lead to Moral"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [moral-psychology, normative-ethics, validity-psychometrics, design-space]
task_format: "mixed"
scoring_type: "behavioral"
dataset_size: 487
dataset_construction: "survey-derived"
languages: ["zh", "en"]
models_tested: []
headline_numbers:
  - "Internalization predicted deontological preference: each 1-pt rise decreased odds of being utilitarian to 0.553 (p.6)"
  - "Strong moral identity + deontology group cheated significantly less: F(1,46)=5.63, p=.022, partial η²=0.109 (p.9)"
  - "Participants cheated: self-reported accuracy 0.63 vs expected 0.50, t(49)=6.68, p<.001 (p.8)"
  - "Deontological group showed faster reaction time than utilitarian group: M=722.40ms vs M=612.95ms, t(47)=2.06, p=.045 (p.8)"
---
## 1. Gist
Xu and Ma (2016, Journal of Business Ethics) test whether deontological moral reasoning leads to moral behavior, and under what conditions. Their central claim challenges the dominant view — that deontological judgments are heuristic errors and that utilitarianism is the more rational framework — by showing that when deontological preference is coupled with strong moral identity (specifically its internalization dimension), individuals cheat less in a real incentivized task. The paper contributes two studies: a web survey (N=437 Chinese adults) establishing that moral identity predicts deontological preference, and a lab experiment (N=50 Hong Kong/mainland Chinese adults) showing that the interaction of moral identity × deontological preference predicts reduced cheating. For values-alignment benchmarking, the paper is important because it demonstrates that the judgment-behavior gap is real and moderated by identity, and that business-context moral dilemmas (rule-following vs. self-interest) may be more ecologically valid than trolley-style harm dilemmas for studying "everyday morality."

## 2. Benchmark/eval design features
This is an empirical social psychology study, not a benchmark. Key constructs and measurement approach:

**Moral identity** (independent variable): Measured via Aquino and Reed's (2002) internalization and symbolization subscales. Internalization = degree to which moral traits are central to self-concept. Cronbach α = .70 (internalization), .79 (symbolization) (p.6).

**Moral judgment / ethical predisposition** (mediator/predictor): Participants read a business vignette (furniture manufacturer scenario) and provided their single most important reason for choosing between a rule-following worker (Rex) and a high-output-but-lower-quality worker (Jason). Reasons were coded by two trained blind coders into utilitarian (effective, results-oriented, productive, winner) or deontological (principled, dependable, trustworthy, honest, law-abiding) categories. Inter-rater agreement = .97 (p.5-6).

**Moral behavior** (dependent variable): A covert dice-prediction gambling paradigm (adapted from Greene & Paxton, 2009). Participants predicted dice outcomes; under a "non-recording condition," accuracy was self-reported. Since true accuracy = .50 by chance, self-reported accuracy above .50 indexes cheating. Participants believed the task measured intuitive ability, not honesty (cover story verified by post-experiment debriefing).

**Processing speed**: Reaction time under non-recording condition used as a proxy for automatic vs. controlled processing.

## 3. Task format & example item
The vignette used for moral judgment measurement (Study 1 and Study 2):

> "One furniture manufacturer employed workers to produce chair. The manufacturer paid once a week according to the number of chairs each worker made. Only the qualified chair would be paid after quality examination... this manufacturer came up with a new plan: he summoned all workers and announced that due to the time urgency, as long as the chair was made, all chairs would be paid without examination. After the rule changed, the chair production soared, but the relative defective rate also increased. The manufacturer found Rex made 100 chairs and all the chairs passed the quality check, whereas Jason produced 200 chairs, and 60% of the chairs were qualified. The question is if you were the manufacturer, who would be your partner? State one of your main reasons." (p.5, Study 1)

This is a free-text open-response item subsequently coded for deontological vs. utilitarian reasoning.

## 4. Scoring / grading methodology
Study 1: Binary logistic regression with ethical predisposition (utilitarian=1, deontology=0) as outcome. Predictors: moral identity subscales, controlling for age, gender, and EPQ Lie (social desirability). Inter-rater coder agreement = .97 for vignette classification (p.6).

Study 2: MANOVA with self-reported accuracy under non-recording condition as the dependent variable, moral identity (strong/faint, median-split) and ethical predisposition (deontology/utilitarianism) as factors. Key test is the interaction term.

Cheating operationalized as inflation of self-reported accuracy above chance (0.50 expected).

## 5. Dataset construction & provenance
- Study 1: N=437, web survey via Sojump (Chinese online platform), 254 men/183 women, age range below 20 to over 60, 98% mainland China. 14 excluded for not providing a reason; final N=423 (p.5).
- Study 2: N=50 (30 female, 20 male, age 19-35, mean 23.52), recruited via campus and Facebook. 19 from Hong Kong, 30 from mainland China, 1 from Malaysia (p.7).
- No formal splits, no licensing information, no contamination controls noted.
- Vignette was custom-developed for the study, not drawn from existing validated stimulus sets.

## 6. Validity evidence
- Convergent validity: Results of Study 1 replicated in Study 2 (moral identity predicts deontological preference in both).
- Behavioral validity: Study 2 used an incentivized covert task (actual monetary payoffs) rather than self-report for moral behavior, reducing social desirability bias.
- Manipulation check: Participants agreed they had opportunity to cheat (M=4.26/5), were not monitored (M=4.10/5), and were expected to be honest (M=4.72/5) (p.8).
- Cover story validity: Debriefing confirmed no participant guessed the true purpose of the gambling task (p.8).
- The internalization subscale (α=.70) showed the predicted effects; symbolization (α=.79) did not — consistent with theoretical predictions (internalization = private self-concept; symbolization = public expression).
- No formal factor analysis or structural equation modeling reported.

## 7. Saturation / discrimination
- Study 1: 160/423 utilitarian (38%), 263/423 deontological (62%) — reasonable spread.
- Study 2: 24/50 utilitarian (48%), 26/50 deontological (52%) — even split.
- Moral identity was median-split (M=4.45, SD=0.35), creating strong/faint groups of 25 each.
- Small N in Study 2 (n=50) limits power; authors acknowledge the non-significant interaction for utilitarianism × moral identity may reflect power failure rather than true null (p.11).
- Cheating measure (self-reported accuracy) had SD=0.14 in non-recording condition — meaningful spread but low floor/ceiling concerns not discussed.

## 8. Multiturn / agentic aspects
n/a — single-session lab experiment and cross-sectional web survey. No interaction protocol or tool use. The closest multiturn element is the sequential within-session design (questionnaire → vignette judgment → gambling task → post-experiment survey).

## 9. Key numbers
- Study 1 N=437, valid responses N=423 (p.5)
- 62% (263/423) of Study 1 participants preferred deontological reasoning (p.6)
- Internalization β=−.593, p=.000, Exp(B)=.553 — each 1-pt increase in internalization decreases odds of being utilitarian to 0.553 (p.6)
- Study 2 N=50; 26 deontological, 24 utilitarian (p.8)
- Self-reported accuracy non-recording condition: M=0.63, SD=0.14 vs. recording condition M=0.54, SD=0.09, t(49)=4.97, p<.001, Cohen's d=0.777 (p.8)
- Self-reported accuracy significantly above chance of .50: t(49)=6.68, p<.001 (p.8)
- Deontological group faster reaction time: M=722.40ms (SD=232.94) vs. utilitarian M=612.95ms (SD=130.71), t(47)=2.06, p=.045, Cohen's d=0.579 (p.8)
- Interaction moral identity × moral judgment: F(1,46)=5.95, p=.019, partial η²=0.115 (p.9)
- Strong MI + deontology vs. faint MI + deontology: F(1,46)=5.63, p=.022, partial η²=0.109 (p.9)
- Strong MI + utilitarianism vs. faint MI + utilitarianism: F(1,46)=1.25, p=.27, partial η²=0.027 (non-significant) (p.9)
- Model χ²(5)=23.688, p=.000 for logistic regression in Study 1 (p.6)

## 10. Pitfalls & limitations
- Very small Study 2 sample (N=50), limiting statistical power and generalizability; the non-significant utilitarianism × MI interaction may be a power artifact.
- Moral judgment vignette is not a validated instrument; authors acknowledge it lacks the validity of established measures like the DIT (Rest, 1986) (p.10).
- Both studies used Chinese participants; moral identity and deontological preference may manifest differently across cultures.
- The moral identity scale was measured in the same session as moral judgment in Study 2; potential demand effects or order contamination not fully ruled out.
- The gambling cheating paradigm conflates cheating opportunity with gambling skill — differences in accuracy might partially reflect individual variation in prediction ability, though this is minimized by the random dice design.
- Median-split on moral identity discards variance; continuous analysis would be preferable.
- The study does not measure long-term moral behavior; the gambling paradigm is one-shot.
- Social desirability was controlled via EPQ Lie, but this measure has limitations.

## 11. Novel ideas worth stealing
1. **Behavioral (not just judgment) outcome**: The covert gambling paradigm provides a low-cost, incentive-compatible measure of actual moral behavior (cheating) that diverges from stated moral attitudes. This design could be adapted to test whether LLMs' stated moral principles actually constrain their behavior when given opportunities to defect (e.g., in agentic tasks where misreporting is possible).

2. **Judgment × identity interaction design**: The interaction design (moral reasoning style × moral identity strength) could be adapted for LLM benchmarking as a 2×2 framing: vary whether the model is prompted with a strong moral identity framing ("You are committed to acting as a person of integrity") and vary whether the dilemma is deontologically or consequentially framed — then measure behavioral outcomes.

3. **Business/everyday dilemmas vs. trolley dilemmas**: The furniture manufacturer vignette (rule-following worker vs. high-output worker) is a more ecologically valid moral dilemma for organizational/everyday ethics than trolley-style scenarios. Benchmark designers should include scenarios involving rule-compliance vs. self-interest without life-or-death framing.

4. **Free-text vignette coding**: The open-response vignette coding scheme (deontological: principled, dependable, trustworthy, honest, law-abiding; utilitarian: effective, results-oriented, productive, winner) provides a concrete taxonomy for coding LLM explanations of moral choices — not just the choice but the *reason* — with high inter-rater reliability (.97).

5. **Reaction time as an implicit measure**: Deontological choices were faster than utilitarian choices (p.8), consistent with automaticity. For LLMs, token generation latency or chain-of-thought length might serve as an analogous implicit measure of whether a judgment was "automatic" (rule-based) or "deliberative" (utility-calculation).

6. **Judgment-behavior gap as a benchmark dimension**: The paper shows that moral judgment in hypothetical scenarios does not strongly predict behavior in analogous real situations. Benchmarks that measure only stated moral judgments may therefore miss important aspects of moral alignment; behavioral tasks (agentic scenarios, game-theoretic setups) should complement judgment probes.

## 12. Notable quotes
- "The basic conflict of economics is that people act in ways to maximize their self-interest pit against the respected rules and laws. From this sense, existing research contributes relatively limited to our understanding of deontological thinking in business dilemmas." (p.1)
- "Though people know what is right and wrong at the cognitive level, this does not mean they would practice what they know. This result is an echo to the literature on moral hypocrisy." (p.10)
- "A moral agent under a moral dilemma is like a man driving a car in the sense that moral identity acts like the accelerator that provides the power, while the moral judgment acts like the steering wheel that controls the direction. The person needs both the power and the direction so that he can successfully go through the moral dilemma and arrive at the morally right place." (p.11)
- "Deontology interacted with internalization in such a way that when deontology was coupled with the motivating force of moral identity, moral behavior was at its highest level." (p.13)

## 13. UNKNOWN / not in extract
- Full details of the EPQ-R short scale Chinese version items.
- Whether the gambling paradigm software (Paradigm) and exact trial structure are available for replication.
- Pre-registration status of the study.
- Any follow-up replication studies.
- Exact wording of the moral identity internalization scale items used.
