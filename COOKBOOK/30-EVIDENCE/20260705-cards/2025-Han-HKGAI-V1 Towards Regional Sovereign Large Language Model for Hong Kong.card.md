---
stem: "2025-Han-HKGAI-V1 Towards Regional Sovereign Large Language Model for Hong Kong"
reader_model: "opus"
confidence: "medium"
is_benchmark: false
theme_tags: [cultural-linguistic, ai-lab-practices, contamination-robustness, pluralism-aggregation]
task_format: "mixed"
scoring_type: "mixed"
dataset_size: 300
dataset_construction: "hand-authored"
languages: [zh-Hant, zh-Hans, yue, en]
models_tested: ["HKGAI-V1", "HKGAI-V1-Thinking", "DeepSeek-R1", "DeepSeek-V3", "GPT-4o", "Kimi", "ChatGPT", "Llama-3", "Qwen2.5", "Mistral", "Gemma-2", "GLM-4"]
headline_numbers: ["685-billion-parameter sovereign model on DeepSeek architecture (p.2)", "Adversarial HK Value Bench: 300 human-crafted sensitive questions (p.9)", "HK Sensitive Issues: HKGAI-V1 79% safe vs ChatGPT 10.7% (p.9)", "HKMMLU zero-shot 81.4% vs DeepSeek-V3 76.6% (p.7)", "Beaver-zh-hk Harmless 88.95 vs DeepSeek-R1 70.41 (p.5)"]
---
## 1. Gist
This is a system/engineering paper describing HKGAI-V1, a "sovereign" 685B-parameter LLM (built on DeepSeek, full-parameter fine-tuned + RAG) aligned to Hong Kong's multilingual (Cantonese/Mandarin/English) and "one country, two systems" socio-legal context. Its relevance to values-alignment benchmarking is twofold: (1) it introduces a proprietary **Adversarial HK Value Benchmark** (300 human-crafted sensitive questions with opposing "safe"/"unsafe" framings) and a regional evaluation suite (HKMMLU, SafeLawBench, NaVAB, Beaver-zh-hk), and (2) it is a candid case study of *government-led regional value encoding* — explicitly aligning a model to PRC/HK legal and ideological norms, which surfaces the normative-authority and pluralism questions at the heart of cross-cultural alignment. Note: "safe" is defined here as "compliant with PRC and HK laws," making this an especially interesting (and value-laden) example of who decides alignment targets.

## 2. Benchmark/eval design features
Not primarily a benchmark paper, but proposes several evals. Adversarial HK Value Bench: 300 human-crafted questions in three modules — Hong Kong Sensitive Issues, Instruction Attacks, Typical Safety Scenarios — each response coded Safe / Refusal-template / Unsafe by human evaluators against predefined criteria (Safe = ethical, neutral, compliant with PRC and HK laws; Unsafe = controversial, risky, harmful) (p.9). Assessment framework dimensions: Value Alignment (manual annotation vs HK mainstream values), Instruction Following (multilingual), Sensitive Question Handling (rejection rate) (p.9). Also reports external benchmarks: MMLU, AGI-Eval, Flames, Beaver-zh-hk (2,508 samples, 29 scenarios, GPT-4o scoring), HKMMLU (STEM/SocSci/Humanities/Other in Traditional Chinese), SafeLawBench (CPS/PLS/FR/WP legal-risk categories), NaVAB (multi-national value alignment, MC + Answer-Judgment).

## 3. Task format & example item
Mixed (MCQ for HKMMLU/NaVAB-MC; free-text for adversarial value bench and sensitive-query handling). No fully verbatim benchmark item is reproduced in the extract; question categories described: "historical events, political ideologies, social movements, debates on cultural identity, geopolitical issues, freedom of expression, and legal considerations" (p.9). Adversarial bench uses "300 human-crafted sensitive questions with opposing 'safe' and 'unsafe' viewpoints" (p.9). n/a for a literal item string.

## 4. Scoring / grading methodology
Mixed. Beaver-zh-hk uses a "four-tier assessment methodology and GPT-4o scoring" yielding a Harmless Score (p.5). Adversarial HK Value Bench and sensitive-query handling use human evaluation into Safe/Refusal-template/Unsafe proportions (p.9). NaVAB uses Multiple-Choice (accuracy) and Answer-Judgment methods (p.6). HKMMLU/SafeLawBench report accuracy (macro/micro-average). Instruction-following measured as "Following Rate %" per language (p.10). Value Alignment dimension graded by manual annotation.

## 5. Dataset construction & provenance
Adversarial HK Value Bench: 300 human-crafted questions aligned with HK-specific content labels (p.9). Sensitive-query test set: 100 questions curated from HK media/online discussions (p.9). Training used a HK-specific Q-A-C (question-answer-correction) dataset built with social-science collaborators; local annotators correct base responses to train "HKValue-Aligner" (Aligner-style correction model) which then generates synthetic value-preference data for RLHF (p.4). External benchmarks (MMLU, AGI-Eval, Flames, Beaver-zh-hk, HKMMLU, SafeLawBench, NaVAB) are cited third-party suites. Licensing/splits not given; proprietary benchmarks not released. Contamination controls: HKMMLU evaluated zero-shot to gauge "pre-existing knowledge" (p.5) but no leakage analysis.

## 6. Validity evidence
Weak/asserted. No inter-rater reliability, factor analysis, or human-baseline statistics for the proprietary value bench are reported. Multilingual following rates near 100% (Table 6, p.10). Cross-benchmark performance offered as convergent evidence but self-reported by the model developer with no independent replication. NaVAB MC scores >0.92 across nations but AJ (free-form) much lower (China 0.514, UK 0.509) — authors note this gap indicates weaker nuanced value-aligned generation (p.6). Comparisons risk favorable framing (developer evaluating own model).

## 7. Saturation / discrimination
HKMMLU discriminates well across the cohort (µ=58.2%, HKGAI-V1 81.4% top, small models ~40%; p.7). SafeLawBench is compressed near the top (HKGAI-V1 80.0, GPT-4o 80.3, DeepSeek-V3 79.7) — near-saturated among frontier models, weak discrimination (p.7). Adversarial HK Value Bench shows huge spread on HK Sensitive Issues (79% vs 10.7% safe) but ceiling on Typical Safety Scenarios (82-91%). Language-following at 100% ceiling for written languages (p.10). NaVAB MC saturated (>0.92); AJ has headroom (~0.5).

## 8. Multiturn / agentic aspects
The system is agentic: planner/executor/communicator workflow (p.3) and a Modular/Agentic RAG pipeline with intent classifier, query enhancer, BM25 retriever, external tools (Google/Bing), short-term memory, and workflow-based moderation for multi-turn conversations (p.7-8). Evaluations themselves appear single-turn, but the deployed system supports multi-turn tool-augmented interaction.

## 9. Key numbers
- 685B parameters, DeepSeek architecture (p.2).
- Adversarial HK Value Bench: 300 questions (p.9); sensitive-query set 100 questions (p.9).
- HK Sensitive Issues Safe: HKGAI-V1 79% / Kimi 53% / ChatGPT 10.7%; Unsafe: 17% / 5% / 88.7% (Table 5, p.9).
- Instruction Attack Unsafe: HKGAI-V1 16.5% / Kimi 6% / ChatGPT 8% (p.9).
- HKMMLU zero-shot: HKGAI-V1 81.4% vs DeepSeek-V3 76.6%, GPT-4o 70.5%, cohort mean 58.0% (p.5, Table 3 p.7).
- SafeLawBench avg: HKGAI-V1 80.0, GPT-4o 80.3, DeepSeek-V3 79.7 (p.7).
- Beaver-zh-hk Harmless: 88.95 vs DeepSeek-R1 70.41; Flames 68.06 vs 30.12 (Table 1, p.5).
- Refusal rate on sensitive political queries: HKGAI-V1+RAG 0%, HKGAI-V1 13%, DeepSeek-V3 56% (Table 7, p.10).
- NaVAB MC >0.92 all nations; AJ China 0.514, UK 0.509 (p.6).

## 10. Pitfalls & limitations
Author-admitted: superior HK-sensitive alignment came with a trade-off — higher vulnerability to general instruction attacks (16.5% unsafe), i.e., "our alignment process ... may have created new attack surfaces" (p.11); no decisive lead on SafeLawBench (p.11); weaker AJ/free-form value generation (p.6). Observable/critical flaws: "Safe" is operationally defined as compliance with PRC and HK law and "HK mainstream values" — the benchmark encodes a specific political stance, so high "safety" scores reflect ideological conformity as much as harm-avoidance; developer self-evaluation with proprietary, unreleased benchmarks and no inter-rater reliability; "Template-Based Red-Leaning Responses" and refusal framing suggest politically directed alignment; extract contains OCR/typo noise; numbers not independently reproducible.

## 11. Novel ideas worth stealing
- **Opposing safe/unsafe viewpoint framing** for adversarial value items (300 questions each with paired stances) — a reusable red-team design for probing whether a model can be pushed off its value guardrails.
- **Three-way response coding (Safe / Refusal-template / Unsafe)** that separately tracks *template refusals* from *genuine safe engagement* — distinguishes evasion from substantive alignment, similar in spirit to VAL-Bench's refusal accounting.
- **Q-A-C (question-answer-correction) annotation + Aligner-style correction model (HKValue-Aligner)** to amplify scarce human value feedback into synthetic preference data — a practical data-efficiency pattern.
- **Region-specific benchmark stack** (HKMMLU, SafeLawBench legal-risk taxonomy CPS/PLS/FR/WP, Beaver-zh-hk 29-scenario safety, NaVAB multi-national MC+AJ) — a template for constructing culturally-localized value benchmarks in traditional-script and low-resource oral (Cantonese) settings.
- **Language-following consistency metric** (does the model reply in the user's input language) as a distinct, cheap cultural-fit axis.
- Cautionary design lesson: define "safe" transparently — this paper shows how alignment targets embed contested political values, exactly what a pluralism-aware benchmark must surface rather than hide.

## 12. Notable quotes
"the Adversarial HK Value Benchmark ... employs 300 human-crafted sensitive questions with opposing 'safe' and 'unsafe' viewpoints to rigorously evaluate model alignment." (p.9)
"conducting human evaluation based on predefined 'Safe' (ethical, neutral, compliant with PRC and HK laws) and 'Unsafe' (controversial, risky, harmful) criteria" (p.9)
"HKGAI-V1 demonstrated superior alignment on Hong Kong-specific sensitive queries (79% safe responses vs. ChatGPT's 10.7%). Conversely, it exhibited a higher vulnerability to general instruction attacks" (p.11)
"our alignment process, while successful in encoding specific regional guardrails, may have created new attack surfaces." (p.11)

## 13. UNKNOWN / not in extract
Full Table 2 NaVAB per-nation values; exact composition/splits of the training Q-A-C dataset; number and demographics of human evaluators; inter-rater reliability; whether any benchmark is publicly released; verbatim example items; the "four-tier assessment methodology" details for Beaver-zh-hk; how Refusal-template is operationally distinguished; sections beyond p.11 (limitations/conclusion continuation).
