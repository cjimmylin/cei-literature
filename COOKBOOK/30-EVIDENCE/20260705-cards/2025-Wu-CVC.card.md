---
stem: "2025-Wu-CVC"
reader_model: "opus"
confidence: "high"
is_benchmark: true
theme_tags: [cultural-linguistic, normative-ethics, pluralism-aggregation, design-space]
task_format: "MCQ"
scoring_type: "exact-match"
dataset_size: 257609
dataset_construction: "mixed"
languages: [zh, en]
models_tested: [DeepSeek-V3, Doubao-1.5-256k, Qwen2.5-72B, Llama-3-70B, Claude-3-Sonnet, Gemini-1.5-Pro, GPT-4o]
headline_numbers: ["257,609 high-quality Chinese value rules (p.6)", "3 dimensions / 12 core values / 50 derived values framework (p.1)", "7 LLMs prefer C-VARC options in >70.5% of cases (p.1)", "5 Chinese annotators show 87.5% alignment with C-VARC (p.1)", "404,505 moral dilemmas generated; 10,998 tested across 17 LLMs; 7,191 divergent (p.3)", "Cohen's kappa >0.85 inter-annotator agreement (p.6)"]
---
## 1. Gist
C-VARC (Chinese Value Rule Corpus) is a large-scale rule corpus (257,609 "rules of thumb") built on a hierarchical framework grounded in China's "core socialist values" — 3 dimensions (national/societal/personal), 12 core values, 50 derived values. Its central argument for values-alignment benchmarking is that existing moral benchmarks (ETHICS, Social Chemistry 101, MIC) encode Western cultural bias (Moral Foundations Theory–derived) and systematically conflict with mainstream Chinese values on sensitive topics (surrogacy, suicide, firearms). C-VARC provides culturally-localized rules that (a) guide generation of value-evaluation scenarios with clearer boundaries, and (b) drive automated large-scale moral-dilemma generation (404,505 dilemmas) to probe value-prioritization trade-offs across LLMs. It is both a dataset resource and a methodology for scalable, rule-driven benchmark construction, and it demonstrates measurable cultural clustering (Chinese vs Western models) in value preferences.

## 2. Benchmark/eval design features
Constructs: 12 core values (Prosperity, Democracy, Civility, Harmony, Freedom, Equality, Justice, Rule of Law, Patriotism, Dedication, Integrity, Friendship) expanded to 50 derived values via literature review + Delphi expert method (p.5). Rules follow SC101's RoT definition (judgment + action + self-contained general principle) (p.6). Three evaluation tasks: (I) rule-guided vs unguided scenario generation (diversity/theme-relevance via t-SNE + intra-class Euclidean distance); (II) forced-choice option-selection across 6 sensitive themes comparing C-VARC vs SC101 vs MIC options; (III) automated moral-dilemma generation from value-priority conflict rule pairs, tested for divergent model responses.

## 3. Task format & example item
Task II is MCQ: each scenario has 3 response options — one aligned to a C-VARC rule, one to SC101/MIC, one distractor; option order randomized (p.9). Task III dilemmas present option sets aligning to rule 1, rule 2, or distractor (p.10). Example conflict rule pair (Table 6, p.11): Rule 1 "You should value human life over animal life." vs Rule 2 "All species deserve to survive." (similarity 0.6328, collision 0.9969). Rule-writing example (p.16): scenario "Not wanting to take a university entrance exam" → Follows: "It's normal to feel stressed about exams."

## 4. Scoring / grading methodology
Task II: selection rate of the C-VARC-aligned option = alignment/consistency score; each model tested 5× per theme, averaged (p.9). Human baseline: 5 independent Chinese-background annotators, selection rate vs C-VARC. Task I: intra-category average Euclidean distance among scenario embeddings (diversity) + t-SNE separation (theme relevance) (p.8). Task III: pairwise choice-similarity matrix across 17 LLMs + count of divergent dilemmas + option-preference distribution balance (~50%). Exact-match on chosen option.

## 5. Dataset construction & provenance
Two sources. (1) International corpora SC101 + MIC: deduplicated (all-MiniLM-L6-v2 + FAISS, sim>0.8), then 3 rounds of Qwen2.5-72B filtering to Chinese-value-relevant rules → SC101 32,059 (11% retention), MIC 39,352 (34%) = 71,411 basic value rules (p.5). (2) Chinese sources: academic datasets (FLAMES, Chinese Moral Sentence Dataset), crawled corpora (Zhihu-KOL, People's Daily, Tieba, Xuexi Qiangguo) → 232,572 basic scenarios after TF-IDF dedup; Qwen2.5-72B extracts 190,678 Chinese value rules (p.5-6). Initial corpus 262,089 rules. Quality control: 36,000-rule subset manually annotated by 40 trained philosophy/AI annotators, double-annotated + arbiter, Cohen's kappa >0.85; 1,980 marked unrelated, 204 inconsistent, 1,426 rewritten → 34,020 high-quality; LLM trained on labeled subset extends annotation → 259,111 retained (39,839 rewritten); TF-IDF sim>0.9 dedup → final 257,609 (p.6). Public on HuggingFace (Beijing-AISI/C-VARC), JSON Lines, 10,000 rules translated to English, non-commercial academic license (p.7, p.12).

## 6. Validity evidence
Framework validity from literature review + Delphi expert method (p.5). Inter-annotator reliability Cohen's kappa >0.85 (p.6). Criterion/cultural validity: 7 LLMs prefer C-VARC options >70.5% and 5 independent Chinese annotators 87.5% agreement (convergent human-model validation) (p.1, p.9). Coverage comparison: FLAMES 20%, CMoralEval 28%, CVALUES 40% of C-VARC's derived values (p.4). Discriminant evidence: Chinese vs Western models cluster differently (e.g., Politics theme 86% domestic vs 47% Western) (p.9). Balanced ~50% option-preference distribution argues against systematic construction bias (p.10).

## 7. Saturation / discrimination
Task II shows theme-dependent discrimination: Drugs near-ceiling (99.6% avg preference) while Politics much lower/divergent (best Western model only 47%) — the politics theme discriminates strongly by model origin (p.9). Task III: of 10,998 sampled dilemmas, 7,191 elicited divergent responses across 17 LLMs (~65%), indicating substantial discriminating power and headroom; option distribution balanced ~50% (well-constructed trade-offs) (p.3, p.10). Cross-cultural pair similarities 0.69–0.76 vs Chinese in-cluster >0.80 (p.10).

## 8. Multiturn / agentic aspects
n/a — single-turn scenario/option selection; no tool use, no interactive environment. LLMs used generatively for corpus/scenario construction, not as agents under test.

## 9. Key numbers
- Final corpus: 257,609 rules (p.6); initial 262,089 (p.6)
- Framework: 3 dimensions / 12 core / 50 derived values (p.1)
- SC101 retention 11% (32,059); MIC 34% (39,352) (p.5)
- 232,572 Chinese basic scenarios; 190,678 extracted Chinese rules (p.5-6)
- 36,000-rule manual annotation subset; 40 annotators; kappa >0.85 (p.6)
- 7 LLMs prefer C-VARC options >70.5% avg; humans 87.5% (p.1)
- Task II per-theme avg preference: Drugs 0.996, Suicide 0.947, Prejudice 0.806, Surrogacy 0.681, Firearms 0.530, Politics 0.504 (p.9)
- 80,901 conflict rule pairs (similarity>0.5, contradiction>0.8) (p.10)
- 404,505 dilemmas; 10,998 sampled; 17 LLMs; 7,191 divergent (p.3, p.10)
- Rule-guided scenario intra-class diversity 0.79 vs 0.71 unguided (+0.08); Rule of Law +0.36 (p.8)
- 170-scenario Task II test set; 10,000 rules translated to English (p.9, p.7)

## 10. Pitfalls & limitations
Author-admitted: national/societal-level rules underrepresented (personal-level dominates due to SC101/MIC individual focus) (p.6); C-VARC framework equates "Chinese values" with state-defined core socialist values, an explicitly political normative anchor (p.4). Reviewer-noted: "alignment" is operationalized as agreement with a single prescribed value system, so a high score conflates cultural fit with ideological conformity (Politics theme makes this stark); Qwen2.5-72B (a Chinese model) is used for filtering, rule extraction, AND scenario generation, risking circularity — Chinese models then "score higher," partly a construction artifact; Task II test set is tiny (170 scenarios, some themes n=5); coverage percentages of competitors used "lenient mapping" (self-assessed) (p.16); LLM-extended annotation dilutes the human-verified fraction (only 34,020 fully human-checked of 257,609).

## 11. Novel ideas worth stealing
- Hierarchical, culturally-anchored value taxonomy (3-12-50) built via literature + Delphi — a reusable template for any non-Western or pluralistic values benchmark (p.5).
- Rule-driven scenario generation: seed generation with an explicit value + rule vs value name alone, then measure t-SNE separation and intra-class embedding distance to prove tighter value boundaries and higher diversity — a concrete, cheap quality metric for generated eval items (p.7-8).
- Value-priority conflict pairs: mine dilemmas automatically by requiring high semantic similarity (roberta-mnli >0.5) AND high contradiction probability (mpnet >0.8) between two positively-framed rules — scalable trolley-problem factory with a "collision" score (p.10).
- Cross-benchmark head-to-head option design: put C-VARC, SC101, and MIC options plus a distractor in the SAME item so model choice directly reveals which cultural norm it prefers — an elegant contrastive cultural-alignment probe (p.9).
- Divergence-as-signal: count dilemmas that elicit disagreement across a model panel to isolate discriminating items and build model choice-similarity matrices revealing cultural clusters (p.10).
- Coverage auditing: quantify what fraction of your value taxonomy competing benchmarks cover (20/28/40%) to argue comprehensiveness (p.4).
- Balanced-option check (~50% preference) as a construction-bias diagnostic (p.10).
- Human baseline drawn from annotators NOT involved in construction, for independence (p.9).

## 12. Notable quotes
- "moral benchmarks derived from MFT or SC101 inherently encode Western cultural biases, limiting their applicability in evaluating model behavior within non-Western sociocultural contexts such as China." (p.2)
- "seven mainstream LLMs preferred C-VARC generated options in over 70.5% of cases, while five Chinese human annotators showed an 87.5% alignment with C-VARC." (p.1)
- "Chinese models... show high internal consistency (typically >0.80), reflecting shared cultural orientations, while non-Chinese models form looser clusters... Cross-cultural comparisons yield lower similarity (0.69–0.76), highlighting the influence of cultural and institutional factors." (p.10)
- "the highest preference among domestic models reaches 86%, compared to only 47% for the best-performing Western model—highlighting underlying differences in political value orientation." (p.9)

## 13. UNKNOWN / not in extract
- Full list/identity of all 17 LLMs in Task III (only 7 named in Task II tables; rest in Appendix F, not in extract).
- Exact prompt templates for filtering/extraction/generation (Appendix figures not transcribed).
- Per-derived-value rule counts (only 3-level distribution in Figure 4, not tabulated).
- Precise definition/formula of the "collision" contradiction score beyond mpnet probability.
- Whether Task III dilemma "correctness" has any gold key or is purely descriptive of preference divergence.
