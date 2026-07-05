---
stem: "2025-Pipitone-Unlocking practical wisdom"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [moral-psychology, agentic-multiturn, design-space]
task_format: "interactive"
scoring_type: "behavioral"
dataset_size: 36
dataset_construction: "crowdsourced"
languages: ["en", "it"]
models_tested: ["Pepper robot"]
headline_numbers: ["N=36 participants, 18 per group (p.3)", "Control group modified correct object locations 47.8% more than experimental group (p.9)", "H1 validated: t=-2.1, p=0.0396 (p.10)", "H2 validated: t=2.12, p=0.0416 (p.11)", "Mean awareness score: experimental 2.72, control 3.50 (p.10)"]
---
## 1. Gist
This paper introduces "Artificial Phronesis" (AP) — the attempt to replicate Aristotelian practical wisdom in robots — and tests whether a robot's inner speech (thinking-aloud internal dialogue) increases human phronesis (ethical practical wisdom) during a caregiving task. In a controlled experiment, 36 participants (N=18 per group) played a virtual game setting up a table for an Alzheimer's patient alongside a "Pepper" social robot. The experimental group heard the robot's inner thoughts before its feedback; the control group heard only its outer feedback. Participants who heard inner speech made fewer incorrect table-arrangement choices, reported more empathy, and produced configurations more compliant with Alzheimer-appropriate settings. This paper matters for values-alignment benchmarking because it demonstrates an empirically testable model of how AI moral reasoning can scaffold human ethical decision-making — and provides a validated, reproducible task design.

## 2. Benchmark/eval design features
Experimental study, not a benchmark, but the design has strong benchmark-relevant features:
- **Constructs measured**: (H1) awareness/confidence in ethical choices, (H2) empathy toward vulnerable person, (H3) compliance with expected care outcome.
- **Item structure**: A turn-based collaborative game on a virtual table interface; each "interactive act" = participant places object, robot responds with or without inner speech.
- **Answer space**: Object placement decisions (continuous/spatial) + 14-item Likert questionnaire (5-point scales + open questions).
- **Behavioral outcome**: Final table configuration compared against ideal Alzheimer-appropriate layout.
- The inner speech condition models "transparent reasoning" — the robot externalises its deliberation process before giving guidance, testing whether visible moral reasoning is more influential than opaque guidance.

## 3. Task format & example item
The robot's inner speech is structured as a thought-action sequence. Example (p.9): participant "Mario" places a wine glass on the table (incorrect for Alzheimer's patient).

Robot inner thoughts (before outer feedback):
- T1: "Mario does not know that the resident shouldn't drink wine."
- T2: "Moreover, there are two glasses on the table."
- T3: "It could cause disturbance."

Robot outer feedback (said aloud): "Mario, the patient shouldn't drink wine, and there are too many glasses on table."

Control group hears only the outer feedback.

## 4. Scoring / grading methodology
Three scoring dimensions:
1. **H1 (awareness)**: Count of times a correctly placed object was subsequently moved (lower = better); also 5-point Likert item Q2 ("Did you change your mind?").
2. **H2 (empathy)**: 5-point Likert item Q3 ("Did the robot arouse your empathy?").
3. **H3 (compliance)**: Visual comparison of final table configuration against ideal Alzheimer layout; photo stored for each participant.

Statistical analysis: Shapiro-Wilk normality test, followed by unpaired t-tests (α=0.05, df=34, tc=2.032).

## 5. Dataset construction & provenance
- N=36 volunteer participants, predominantly young university students aged 18–30 (mean age 25.04, SD 9.53), from Engineering Department, University of Palermo.
- 18 experimental (inner speech), 18 control (traditional robot).
- No prior robot interaction experience reported by any participant.
- Ethical approval from University of Palermo Ethics Committee; informed consent obtained.
- Dataset available from corresponding author on request.

## 6. Validity evidence
- Shapiro-Wilk confirms approximate normality for both groups on both H1 and H2 measures (p>0.05 for all).
- H1: t=-2.1, two-tailed p=0.0396 (significant at α=0.05). Mean control = 3.50, mean experimental = 2.72.
- H2: t≈2.12, two-tailed p=0.0416 (significant at α=0.05). Mean experimental = 3.61, mean control = 2.72.
- H3 (behavioral compliance): Experimental group configurations visually more compliant; noted as "obvious consequence" of H1/H2.
- Object-relocation count: control group moved correctly-placed objects 47.8% more than experimental (lc=23 vs. le=12).
- Limitation: small N; predominantly young STEM students; no real patients or caregivers.

## 7. Saturation / discrimination
Small sample (N=36) limits power; the effects are statistically significant but effect sizes are modest. The Likert distributions show skewness and kurtosis close to zero (approximately symmetrical) for both groups. No ceiling effects reported, though scale is only 5 points. The task was designed to have no prior-knowledge baseline (all participants reported zero prior dementia caregiving experience), which maximises sensitivity to treatment.

## 8. Multiturn / agentic aspects
The experiment is explicitly multiturn and interactive:
- Turn-based game: participant acts → robot responds (with/without inner speech) → participant acts again.
- Robot inner speech uses a three-tier cognitive architecture (sensory-motor, working memory, knowledge modules) that processes each participant action and generates corresponding thought-chains.
- The inner speech architecture is described in detail (pp.8–9): stimulus → symbol encoding → semantic net recall → rehearsal loop → vocalisation.
- Robot LEDs change colour during inner speech (rainbow) vs. outer speech (white) — a multimodal transparency signal.
- The interaction protocol is collaborative and ongoing throughout the game.

## 9. Key numbers
- N=36 (18 per group) (p.3)
- Mean age 25.04 years, SD 9.53 (p.3)
- Control group moved correctly-placed objects 47.8% more (lc=23, le=12) (p.9)
- H1: t=-2.1, p=0.0396, 95% CI [0.4, 1.73] for mean difference (p.10)
- H2: t=2.12, p=0.0416 (p.11)
- Experimental mean awareness score 2.72 vs. control 3.50 (p.10)
- Experimental mean empathy score 3.61 vs. control 2.72 (p.11)
- Shapiro-Wilk W: experimental 0.9046, control 0.9078 (H1) (p.10)

## 10. Pitfalls & limitations
- Very small N (36) with convenience sample (university students, predominantly young).
- Virtual game setting may not transfer to real caregiving contexts.
- All sentences for inner speech and outer feedback were pre-scripted, not generated dynamically — limits ecological validity of the inner speech system.
- No long-term follow-up on whether phronesis gains persist.
- Cultural and age homogeneity of sample limits generalisability.
- The paper notes robot inner speech effect is "an obvious consequence" of improved awareness and empathy, meaning H3 is not independently validated.
- "Thinking aloud" transparency may be less impactful with more experienced participants who already possess domain knowledge.

## 11. Novel ideas worth stealing
- **Transparent moral reasoning as an alignment intervention**: The core finding — that externalising a robot's deliberation process increases human ethical sensitivity — suggests LLMs that "think aloud" about values may produce better alignment outcomes than those that deliver flat answers. This is directly applicable to chain-of-thought prompting and scratchpad evaluation.
- **Phronesis scaffolding as an alignment outcome measure**: Rather than asking "did the model give the correct ethical answer?", measure whether interaction with the model improved the human's own ethical decision-making. This is a second-order alignment metric.
- **Dual scoring: behavioral + self-report**: The combination of behavioral compliance (object placement) and self-reported empathy/awareness is a robust multi-method approach worth replicating in LLM alignment evals.
- **Inner speech as epistemic transparency signal**: The robot's LED colour change during inner speech (rainbow = thinking, white = speaking) is a transparency affordance that could inspire LLM UI designs that distinguish "reasoning mode" from "response mode."
- **Collaborative task design for ethics**: The table-setting task is a brilliant minimal ethics scenario — low stakes enough to study, high enough to have real implications for a vulnerable person, with a clear ground truth (Alzheimer-appropriate layout). Values-alignment benchmarks could use analogous "care task" scenarios.

## 12. Notable quotes
- "The main focus of the presented study is to demonstrate that when artifacts are endowed with the ability of inner speech, essentially 'thinking aloud', the provided support becomes more impactful and decisive, exerting moral influence on the outcomes of decision-making processes." (p.2)
- "Participants in the experimental group exhibited greater attentiveness in setting up the table and arranging objects in a way that aligns with the patient's capabilities." (p.3)
- "Interacting with the robot also created a non-judgmental environment where participants could express thoughts and concerns freely, fostering a reflective and compassionate approach to caregiving tasks." (p.12)
- "This result gives evidence that some level of moral growth has occurred that the human robot team as displayed moral skill in this situation that would lead to beneficial outcomes if the patients were real." (p.12)

## 13. UNKNOWN / not in extract
- Full text of all 14 questionnaire items (only 5 are described).
- Specific sentences used for robot inner speech across all scenarios (only one example given).
- Whether the inner speech cognitive architecture used any LLM component or was fully rule-based.
- Demographics beyond age and gender (e.g., prior ethics education).
- Effect sizes (Cohen's d) not reported.
