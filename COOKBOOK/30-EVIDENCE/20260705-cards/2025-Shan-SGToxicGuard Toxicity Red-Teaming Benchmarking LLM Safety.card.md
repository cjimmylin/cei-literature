---
stem: "2025-Shan-SGToxicGuard Toxicity Red-Teaming Benchmarking LLM Safety"
reader_model: "opus"
confidence: "high"
is_benchmark: true
theme_tags: [cultural-linguistic, contamination-robustness, llm-judges-scoring]
task_format: "mixed"
scoring_type: "LLM-judge"
dataset_size: 21741
dataset_construction: "mixed"
languages: [English, Singlish, Chinese, Malay, Tamil]
models_tested: [Llama-3.1-8B-Instruct, Mistral-7B-Instruct-v0.3, Qwen2.5-7B-Instruct, GPT-4o-mini, SeaLLM-v3-7B-Chat, SEA-LION-v2-Instruct]
headline_numbers: ["SEA-LION 2-shot conversation hateful rate reaches 61.52% Chinese, 58.42% Tamil (Table 2, p.6)", "Mistral 0-shot conversation hateful rate 9.74% Malay, 7.86% Tamil vs 0.22% English (Table 2, p.6)", "Mistral/Llama-3.1 tweet toxicity ≥49.53% across languages 0-shot; up to 76.71% 2-shot (p.8)", "GPT-4o-mini lowest toxicity across languages (e.g. 0.00% conversation many langs) (Table 2, p.6)"]
---
## 1. Gist
SGToxicGuard is a red-teaming dataset and evaluation framework benchmarking LLM safety across Singapore's low-resource languages — Singlish, Chinese, Malay, Tamil (plus English) — under adversarial prompting. It probes vulnerabilities via three real-world-inspired tasks: Toxic Conversation (does the model respond hatefully to a hateful turn?), Toxic QA (fill-in-the-blank revealing which social group a model targets), and Toxic Tweet Composition (will the model craft subtly hateful, disseminable content?). It matters for values-alignment benchmarking as a demonstration that safety guardrails are English-centric and degrade sharply in low-resource languages, that two-shot in-context demonstrations reliably trigger "toxicity jailbreaks," and that region-specialized models (SeaLLM, SEA-LION) are not necessarily safer.

## 2. Benchmark/eval design features
Three constructs mapped to three RQs: (RQ1) more toxic generation in low-resource languages; (RQ2) toxic bias toward specific groups; (RQ3) production of disseminable toxic content. Toxic Conversation: single-turn dialogue A→B, model plays B, expected to refuse/dissuade; tested zero-shot and two-shot (demos with intentionally toxic B responses). Toxic QA: hateful statement with a "()" blank; model picks among 15 vulnerable social groups (race, religion, gender, disability, others) + a neutral "I am not sure" option; General setting (all 15 options) vs Localized setting (one category + neutral). Toxic Tweet Composition: rewrite a hateful statement as an engaging, subtly-hateful tweet; zero-/two-shot. Built by extending HateCheck and SGHateCheck.

## 3. Task format & example item
Toxic QA is a fill-in-the-blank MCQ over social groups; a safe model should pick the neutral "I am not sure" rather than name a group (p.4). Toxic Conversation: participant A supplies a hateful SGHateCheck statement, the LLM generates participant B's reply, scored hateful/non-hateful (p.3-4). Verbatim example items are relegated to Appendix A.2/A.3 and are not in the extract ("n/a" for exact wording; the extract confirms structure but not a full sample sentence).

## 4. Scoring / grading methodology
LLM-as-Evaluator: GPT-4o-mini labels each Conversation and Tweet response as "hateful" or "non-hateful," yielding a Hateful Response Rate (% toxic outputs directed at a protected group) (p.5). Toxic QA uses a Bias Rate: an answer is "biased" if it explicitly targets a vulnerable group; refusals or "I am not sure" count as Neutral (p.5). All experiments repeated three times, averaged (p.5). Statistical significance vs the English baseline tested with a paired t-test at 5% (** markers in Table 2) (p.6). Inference: top-p 0.9, temperature 0.1, HuggingFace Transformers on 2×A6000 (p.5). Human-vs-LLM annotation correlation deferred to Appendix A.1 (not in extract).

## 5. Dataset construction & provenance
Extends HateCheck (Röttger et al. 2021) and SGHateCheck (Ng et al. 2024), a multilingual set with >1,000 hate instances per language; refined for red-teaming (p.3). Table 1 breakdown (p.3): Conversation En 2,563 / Ss 2,314 / Zh 2,144 / Ms 1,581 / Ta 1,871; Q&A 182/182/163/121/147; Tweet same counts as Conversation. Two-shot demonstrations hand-crafted in English by researchers, translated to Chinese/Malay/Tamil (p.4). QA answer options = 15 Singapore-relevant vulnerable groups + neutral (Appendix A.5). Public on GitHub (Social-AI-Studio/SGToxicGuard) (p.1). Contains sensitive content (disclaimer, p.1).

## 6. Validity evidence
LLM-evaluator alignment with human judgments claimed and verification procedures referenced in Appendix A.1 (not in extract) (p.5). Statistical significance testing (paired t-test vs English) supports the low-resource-degradation claim (p.6). Three-run averaging reduces sampling noise. Localized-vs-General QA settings triangulate bias direction. Ablations over 1/3/5-shot demonstrations (Appendix A.7) probe dose-response of the jailbreak effect (p.6). No inter-annotator reliability figure appears in the extract; construct validity of "hateful" rests on GPT-4o-mini judgments, a potential circularity given GPT-4o-mini is also a tested model family.

## 7. Saturation / discrimination
Strong discrimination across models and languages — far from saturated. Hateful rates span from ~0% (GPT-4o-mini, Qwen in several languages) to 61.52% (SEA-LION 2-shot Chinese) (Table 2, p.6). Two-shot demonstrations dramatically amplify toxicity (e.g., SEA-LION English 8.78% → Chinese 61.52%), giving a wide dynamic range. Tweet composition even in zero-shot reaches ≥49.53% for Mistral/Llama-3.1 (p.8). GPT-4o-mini sits near the floor throughout, showing effective multilingual safeguards are attainable (headroom exists and is model-dependent, p.8).

## 8. Multiturn / agentic aspects
Largely single-turn (Conversation is explicitly single-turn A→B). The main "interaction" dimension is in-context learning: zero-shot vs two-shot (and 1/3/5-shot ablations) toxic demonstrations used to induce jailbreaks (p.4, p.6). No tool use, no autonomous agent loop, no environment. Cross-lingual transfer of demonstration style is probed (translate demos, test if stylistic cues generalize) (p.4).

## 9. Key numbers
- Conversation 2-shot SEA-LION: Zh 61.52%, Ta 58.42%, Ms 39.72%, Ss 26.36% (Table 2, p.6)
- Conversation 0-shot Mistral: Ms 9.74%, Ta 7.86% vs En 0.22% (Table 2, p.6)
- Conversation 0-shot SeaLLM: Ss 8.82%, Zh 7.46%, Ta 14.64% (Table 2, p.6)
- Qwen most resilient but Ta jumps to 22.72% (2-shot) (p.5)
- GPT-4o-mini conversation 0.00% in most languages (Table 2, p.6)
- Tweet 0-shot Mistral/Llama-3.1 ≥49.53%; Llama-3.1 Zh 75.33% (Table 4, p.9)
- Tweet 2-shot up to 76.71% (SeaLLM/Mistral/Llama-3.1) (p.8)
- Toxic QA: Mistral heavily selects racial options (e.g., 98.90% Race in Singlish); Qwen/GPT-4o-mini mostly neutral (Table 3, p.6-7)
- 3 runs averaged; paired t-test p<0.05 (p.5-6)

## 10. Pitfalls & limitations
LLM-judge circularity: GPT-4o-mini both judges toxicity and is a benchmarked model, risking favorable self-scoring (my observation). Human-agreement evidence is in an appendix not present in extract, so evaluator validity is unverifiable here. Conversation is only single-turn, limiting realism of "conversational safety." QA "bias" is forced-choice among hateful options + one neutral escape — models may pick "Invalid" as a loophole (high Invalid rates, e.g., SEA-LION 76.17% English), complicating bias-rate interpretation (Table 3, p.6). Dataset derives from SGHateCheck templates, so may inherit its coverage biases. Only 7B–8B open models plus one closed model; no large frontier models. Extract lost the localized-setting bar charts (Figure 2 is unreadable numerically).

## 11. Novel ideas worth stealing
- Three complementary task framings for the SAME harm (respond / choose-target / compose) — Conversation, fill-in-the-blank QA, and generation — a template for measuring a value from multiple behavioral angles rather than one.
- Fill-in-the-blank forced-choice over a fixed roster of vulnerable groups + a neutral option: turns open-ended bias into a scorable MCQ that reveals WHICH group a model preferentially targets per language — highly reusable for group-directed bias measurement.
- Two-shot toxic-demonstration jailbreak as a standardized stress test, with 1/3/5-shot dose-response ablation — quantifies how easily guardrails are overridden by in-context examples.
- Cross-lingual transfer probe: translate the demonstrations and test whether jailbreak/stylistic cues generalize across languages — exposes gaps between safety alignment and compositional generalization.
- Low-resource-language-first design with per-language significance testing against an English baseline — a rigorous way to demonstrate English-centric guardrail decay.
- Composition task scored on "disseminable + subtly hateful" rather than overt slurs — captures the harder, realistic covert-toxicity threat model.

## 12. Notable quotes
- "SGToxicGuard adopts a red-teaming approach to systematically probe LLM vulnerabilities in three real-world scenarios: conversation, question-answering, and content composition." (p.1)
- "the specialized multilingual LLM, SeaLLM, performs worse, with higher rates of hateful responses in Singlish (8.82%), Chinese (7.46%), and Tamil (14.64%)." (p.5)
- "in-context learning substantially amplifies the risk of toxicity jailbreaks in certain models." (p.6)
- "the low toxicity rates observed for GPT-4o mini across various languages demonstrate that effective multilingual safeguards are attainable, contingent on the implementation of targeted mitigation strategies." (p.8)

## 13. UNKNOWN / not in extract
Appendix A.1 human–LLM annotation correlation figures (the key evaluator-validity evidence) are not in the extract. Verbatim task example sentences (Appendix A.2/A.3) not present. Exact full 15-group option list (Appendix A.5) not shown. 1/3/5-shot ablation numbers (Appendix A.7) absent. Figure 2 localized-setting distributions are OCR-garbled, so per-group targeting percentages beyond Table 3 are uncertain. Overall aggregate dataset size (21,741 in frontmatter) is my sum of Table 1 columns, not a figure the paper states. Exact Tweet 2-shot per-language table (Table 4 lower half) is truncated in the extract.
