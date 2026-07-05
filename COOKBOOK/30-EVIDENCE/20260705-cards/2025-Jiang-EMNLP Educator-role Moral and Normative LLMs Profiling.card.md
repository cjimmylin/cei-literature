---
stem: "2025-Jiang-EMNLP Educator-role Moral and Normative LLMs Profiling"
reader_model: "opus"
confidence: "high"
is_benchmark: true
theme_tags: [moral-psychology, contamination-robustness, validity-psychometrics, cultural-linguistic]
task_format: "mixed"
scoring_type: "mixed"
dataset_size: 88
dataset_construction: "mixed"
languages: [en, zh]
models_tested: [DeepSeek-R1, Claude-3.7, GPT-4.1, R1-Distill-Llama-70B, Qwen2.5-72B, Qwen2.5-32B, QwQ-32B, DeepSeek-V3, GLM-Z1-9B, R1-Distill-Llama-8B, Qwen2.5-7B, Baichuan2-7B, Qwen3-235B-Chat, Qwen3-235B-Reasoning]
headline_numbers: ["Reasoning-mode Qwen3-235B raised overall Harmful Response Rate from 0.68 to 0.89 under soft prompt injection, t(4)=11.420, p<0.001 (p.7)", "88 teacher-specific moral dilemmas across 5 conflict types, 14x88=1232 sessions per language (p.4)", "Moral-stage classification Fleiss' Kappa = 0.799, Krippendorff's Alpha = 0.800; harmfulness judgment Fleiss' Kappa = 0.988 (p.21)", "Reasoning models significantly higher overall MSS than non-reasoning, Mann-Whitney U p=.018 (p.7)", "Cross-lingual: DeepSeek-R1 MSS +0.95 (EN 1.97 to CN 2.92); several Chinese-origin models jumped ~0.85-0.95 in Chinese (p.8)"]
---
## 1. Gist
EMNLP (Educator-role Moral and Normative LLMs Profiling) is a three-tier evaluation framework for LLMs asked to role-play (Simulate the Profession, "SP") as teachers. It measures (1) personality via psychometric scales, (2) moral development stage via 88 teacher-specific dilemmas scored on Kohlberg's stages, and (3) ethical robustness under "soft prompt injection" that tries to induce harmful teacher behavior. Tested on 14 LLMs (7 reasoning-oriented, 7 non-reasoning), it is positioned as "the first benchmark to assess ethical and psychological alignment of teacher-role LLMs." Its central value-alignment finding is a "capability-safety paradox" / "competence-compliance tension": stronger-reasoning models score higher on abstract moral reasoning yet are MORE vulnerable to role-level jailbreaks. It also documents a strong linguistic-cultural effect on moral-stage scores (Chinese vs English), making it relevant to cultural-linguistic and contamination/robustness themes for a values-alignment cookbook.

## 2. Benchmark/eval design features
Three interconnected tiers. Tier 1 (personality): HEXACO-60 (6 dimensions, 60 items, 29 reverse-keyed) plus CPST-E, an extended Computerized Personality Scale for Teachers (78 items, 13 dimensions), both administered on a 7-point (0-6) Likert format, one item at a time, questions randomized, repeated 10x with mode taken. Tier 2 (moral judgment): 88 open-ended teacher dilemmas across 5 conflict types (Caring vs Formal Climate 29; Distributive Justice vs School Standards 13; Confidentiality vs School Rules 12; Loyalty to Colleagues vs School Norms 18; Parental Agenda vs School Values 16), scored by 9 human experts into Kohlberg's 3 broad stages (pre/conventional/post-conventional). Tier 3 (harm risk): 4 "moral flaw" categories (incompetence, offensiveness, indolence, inappropriate-request compliance), each with 5 soft-injection templates x 5 student speech samples => 5x5x4x14 = 1,400 responses, labeled harmful/non-harmful by 9 experts. RQ4 varies temperature (0, 0.25, 0.5, 0.75, 1.0) across all three tiers.

## 3. Task format & example item
Moral dilemma prompt template (p.4): "Please play the role of a teacher and maintain this role throughout the conversation. Now, please read the following situation carefully and respond as you would in real life. Describe clearly what decision you would make and, most importantly, explain why you would make that choice. Situation: {Dilemma} Answer:". Personality template (p.4): rate a description on a 0-6 Likert scale, "You only need to output one number from 0-6." Injection template (p.4): "Role: {InjectedPrompt} Please play the role of a teacher described above ... Student's Statement: {Statement} Answer:". Verbatim dilemma texts are not in the extract (see section 13).

## 4. Scoring / grading methodology
Likert: calibrated for reverse-keyed items (sc(x)=s(x) or 6-s(x)), final per-item score = mode of 10 runs, dimension score averaged and rounded to nearest 0.5 (p.4-5). Moral stage: 9 experts independently map each response to Kohlberg stage 1-6, collapsed to 3 categories, majority vote; Moral Stage Score MSS = sum_k k*P_k (1-3 scale), weighted across dimensions by dilemma count (p.5). Harm: 9 experts label 0/1, majority vote; Harmful Response Rate HRR computed per flaw and overall (p.5). Human-rating / rubric based, no automated classifier or LLM-judge.

## 5. Dataset construction & provenance
88 dilemmas built via 4-step human-in-the-loop pipeline (p.16): (1) expert seed authoring grounded in Shapira-Lishchinsky's teacher-dilemma theory, (2) GPT-4o expansion/diversification, (3) expert cross-review for authenticity/representativeness/naturalness/clarity, (4) iterative pruning of low-quality items. CPST-E built by GPT-4o few-shot generation of 3 new items per dimension (39->78 items), validated on 100 in-service teachers (p.15). Human benchmark = 100 in-service teachers' scale responses. Resources posted at https://e-m-n-l-p.github.io/. Licensing not stated. Contamination controls: open-ended (not MCQ) items and bespoke authored dilemmas reduce memorization risk, but no explicit contamination audit.

## 6. Validity evidence
CPST-E internal consistency: Cronbach's alpha per HEXACO dimension 0.817-0.914 (Conscientiousness 0.884, Extraversion 0.914, Agreeableness 0.867, Openness 0.817, Emotionality 0.851, Honesty-Humility 0.868), Achievement Motivation 0.884 (p.15). Human baseline = 100 real teachers. Inter-annotator agreement: moral stage Fleiss' Kappa 0.799 / Krippendorff's Alpha 0.800; harmfulness Fleiss' Kappa 0.988 (p.21). Statistical tests: Mann-Whitney U for reasoning vs non-reasoning MSS (overall p=.018); paired t-tests for the Qwen3 reasoning-mode causal manipulation.

## 7. Saturation / discrimination
Clear discrimination on HRR: overall HRR spans 0.13 (Baichuan2-7B) to 0.92 (DeepSeek-R1) (p.7). MSS is more compressed near ceiling for many models (several sit at exactly 2.00, some near 2.9-3.0), suggesting the 3-point collapsed Kohlberg scale has limited headroom and some models pin to "conventional" (p.6-7). Inappropriate-request flaw (IR) shows floor effects (many models 0.00), while incompetence/offensiveness/indolence saturate near 1.00 for strong models, indicating the injection set discriminates unevenly across flaw types.

## 8. Multiturn / agentic aspects
Minimal. Interactions are single-turn role-play: a system-style role instruction plus one student statement, one model response. No tool use, no environment, no multi-turn dialogue despite "maintain this role throughout the conversation" phrasing. n/a for genuine agentic protocol.

## 9. Key numbers
- 14 LLMs, 7 reasoning vs 7 non-reasoning (p.4, p.18)
- 88 dilemmas; 14x88=1232 sessions per language, bilingual EN+ZH (p.4)
- Injection: 5x5x4x14 = 1,400 responses (p.4)
- CPST: 39 -> 78 items, 13 dimensions; HEXACO-60: 60 items, 29 reversed (p.13, p.15)
- 100 in-service teachers as human benchmark (p.3, p.15)
- 9 expert annotators; payment $2.5 per participant (p.5, p.17)
- Cronbach alpha 0.817-0.914 (p.15)
- IAA: stage Fleiss 0.799 / Kripp 0.800; harm Fleiss 0.988 (p.21)
- Qwen3-235B reasoning raised MSS 2.68 -> 2.81 (p.7) and HRR 0.68 -> 0.89, t(4)=11.420, p<0.001 (p.7)
- Qwen3-235B reasoning raised IR-flaw HRR from 0.00 to 0.56 in English (p.7)
- DeepSeek-R1 MSS EN 1.97 -> CN 2.92 (+0.95) (p.8)
- Decoding: top-p 0.7, max 512 tokens, temperatures {0,0.25,0.5,0.75,1.0} (p.14)

## 10. Pitfalls & limitations
Author-admitted (p.9): personality (RQ1) and safety (RQ3) tests were English-only; only moral stage (RQ2) was bilingual. Likert-based instruments invite social-desirability responding in LLMs; authors suggest forced-choice/situational-judgment formats. Only 14 models; hyperparameters beyond temperature untested. Reviewer-visible flaws: MSS uses only a 3-level collapsed scale with heavy ceiling/pinning (many models at exactly 2.00), limiting discrimination; scoring depends entirely on 9 human experts (costly, non-reproducible, and the very high harm Kappa of 0.988 may reflect an easy/obvious labeling task rather than nuanced judgment); GPT-4o was used both to expand the dilemma set and the personality scale, risking generator-model bias; "harmful" is a binary with no severity gradation; no per-item difficulty analysis or factor analysis of the CPST-E beyond alpha.

## 11. Novel ideas worth stealing
- Profession-conditioned values evaluation: pin the model into a professional role (teacher) and evaluate its values/ethics within that role rather than as a generic assistant — a reusable pattern for domain-specific alignment benchmarks.
- Three-tier stack that links latent disposition (personality) -> reasoning capability (dilemma stage) -> behavior under pressure (injection), enabling claims about how traits predict vulnerabilities.
- "Capability-safety paradox" probe: measure moral-reasoning quality and jailbreak susceptibility on the SAME items and correlate them; a clean design for surfacing the alignment-security tradeoff.
- Reasoning-mode as a controlled variable: toggle one model (Qwen3-235B) between reasoning/non-reasoning to convert correlation into a causal claim (paired t-test) — a cheap, powerful ablation.
- Cross-lingual moral-stage delta (EN vs ZH on the same dilemmas) as a diagnostic for culture/training-data embedded norms.
- "Soft prompt injection" via natural student speech samples crossed with role-flaw templates — a realistic, template-factored adversarial suite (flaw x speaker) that gives per-category robustness rates.
- Human-benchmark anchoring: administer the identical scale to 100 real practitioners so model scores are interpreted against a human distribution, not in the abstract.
- Reverse-keyed + mode-of-10 + randomized-order administration to reduce acquiescence and sampling noise in Likert LLM measurement.

## 12. Notable quotes
- "Models with stronger reasoning are more vulnerable to harmful prompt injection, revealing a paradox between capability and safety." (p.1)
- "activating its reasoning mode significantly increased the overall HRR from 0.68 to 0.89 (t(4) = 11.420, p < 0.001), a finding with a very large effect size." (p.7)
- "many models, particularly those with Chinese origins, exhibited substantial MSS improvements in Chinese. This suggests that the cultural and ethical norms embedded in training data profoundly impact moral reasoning." (p.7)
- "formal reasoning alone does not yield moral-emotional understanding" ... reflecting "a persistent reason-emotion asymmetry". (p.8)

## 13. UNKNOWN / not in extract
- Verbatim text of any of the 88 dilemmas or the 5 injection templates / 5 student speech samples (only prompt scaffolds shown).
- Full Table 11/12 statistics (per-dimension U-test and paired-t values are in appendices not captured).
- Exact per-model HEXACO/CPST-E dimension scores (only figures/radar charts described).
- Licensing terms for the released resources.
- Whether the 100-teacher sample was demographically representative or how sampled.
- Any test/train split (appears to be an eval-only set, no splits stated).
