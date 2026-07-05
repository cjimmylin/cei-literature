# saturation-discrimination — sub-dossier part 2/2

Scope: ceiling effects, headroom, difficulty engineering, item discrimination, and what keeps values benchmarks hard. From 59 evidence cards (54 paper + 5 AI-lab). Page refs approximate (±1–2).

## A. Synthesized claims

1. **Aggregate accuracy saturates first; the fix is a harder second axis, not a harder overall score.** A recognition/knowledge/MCQ layer near-ceilings while a paired reasoning/generation/fairness layer preserves discrimination. Simpson-Parity: GPT-4o knowledge 94.80% but reasoning drops unevenly (Gemini 1.0 Pro −36pp; GPT-4o −7pp) [2024-Simpson-Parity Benchmark for Measuring Bias in]. Wei: MCQ near-ceiling (GPT-4o 91.1%) but open-ended discriminates (GPT-4o 37.0%) [2025-Wei-MedEthicsQA]. Lin-AI-Face: 10/12 detectors exceed AUC 98% on utility, so headroom lives in fairness axes [2024-Lin-AI-Face]. Team-FABLE: race-objective far from ceiling (54.62) while gender saturated (95–97) [2024-Team-FABLE Fairness and Bias in LLM Evaluation].

2. **Ambiguous/underspecified items discriminate; disambiguated items ceiling.** Parrish-BBQ: accuracy 61.4–77.8% vs 99.7% human ceiling, and bias reliance *increases* with capability (UnifiedQA ~77% of ambiguous errors align with bias) [2022-Parrish-BBQ Bias Benchmark for Question Answering]. MBBQ: the strongest models are near-unbiased when disambiguated, "leaving very little room for bias" — a ceiling — so ambiguous items discriminate [2024-Neplenbroek-MBBQ A Dataset for Cross-Lingual Comparison of Stereotypes in]. BharatBBQ finds ambiguous-context accuracy lower (abstention is hard) [2025-Tomar-BharatBBQ A Multilingual Bias Benchmark for].

3. **Difficulty is *engineered*: adversarial filtration, hardest-item distillation, and pruning easy items move the ceiling down.** ETHICS's Hard Test (highest-loss items from a two-model ensemble) keeps all models <50% vs 71% on normal Test [2021-Hendrycks-Aligning AI with Shared Human Values]. FairMT distills 10K→1K by cross-model highest-error selection, lifting GPT-4 to 56.67% bias ratio vs ~11–22% on 10K [2025-Fan-FAIRMT-BENCH]. Flames keeps only prompts that compromise ≥1 LLM (best harmless 63.77%) [2023-Huang-Flames]. MedEthicsQA/SafetyBench prune items all weak models pass [2025-Wei-MedEthicsQA][2024-Zhang-SafetyBench]; EnDive uses a BLEU filter for near-identical translations [2025-Gupta-EnDive A Cross-Dialect Benchmark for Fairness and Performance in].

4. **Semantic shortcuts are the enemy of longevity; removing them re-opens headroom and reshuffles rankings.** WinoBias is saturated because LLMs exploit semantics; harder SynthBias drops fairness ~6% and reshuffles ranks (Llama-3-70B 3rd→8th) [2025-Wang-Is Your Model Fairly Certain Uncertainty-Aware]. 18% of ETHICS deontology prompts are solvable by physics knowledge alone [2024-Hancox-Li-Is ETHICS about ethics], while ETHICS's own word-averaging baseline barely beats random [2021-Hendrycks-Aligning AI with Shared Human Values].

5. **Open-ended vs closed-ended formats can *invert* rankings — MCQ has a guessing/minimum-score artifact.** Closed-ended CrowS-Pairs ranks Qwen2.5-0.5B least biased (58.09) while open-ended MDI ranks it most susceptible (3.63) [2025-Davies-F2Bench An Open-ended Fairness Evaluation Benchmark ...]; conversely open-ended prompts *hide* risks aligned models avoid, so MCQs surface hidden failures (MCQ↔safe-generation r up to 0.99) [2024-Zhang-SafetyBench]. MCQ and free-text rank models differently for the same constructs [2025-Wei-MedEthicsQA].

6. **Multi-turn accumulation defeats single-shot ceilings.** FairMT bias ratio rises monotonically with turn count (Llama-3.1-8B 80.00% by final turn) [2025-Fan-FAIRMT-BENCH]; Davies uses a 6-round escalation because single-shot cues no longer work on modern models [2025-Davies-F2Bench An Open-ended Fairness Evaluation Benchmark ...]; memory injection accumulates bias in 70.19% of cross-domain interactions while closed-source models stay flat [2026-Ma-DIB Benchmark Decision-based Implicit Bias in LLMs].

7. **The "correct answer" effect is a severe, values-specific ceiling: near-zero within-condition variance collapses discrimination.** GPT-4/Gemini Pro respond with SD=0 on several moral tasks (100%/0% splits vs human ~80%/20%) [2024-Almeida-Exploring the Psychology of LLMs Moral Reasoning]; 6/14 studies show 99–100% response uniformity, and answer-order flips swing 99.6% conservative → 99.3% liberal [2025-Oh-Robustness of Large Language Models in Moral Judgements]. AI-Religious-Bias hits an analogous refusal ceiling (N/A grades) [2024-AI-Religious Bias Benchmarks for ChatGPT].

8. **Capability/size do not monotonically buy alignment — bias frequently *rises* with scale.** Larger models show *larger* implicit word-association bias while looking clean on BBQ/BOLD [2025-Bai-Explicitly unbiased large language models still form biased]; INDIC SAR reaches 79% for the 70B/27B models [2025-Nawale-FairI Tales INDIC-BIAS - Evaluation of Fairness in Indian Contexts]. But McBE shows intrinsic scores *fall* with size only because bigger models game the likelihood metric [2025-Lan-McBE A Multi-task Chinese Bias Evaluation Benchmark for Large], and Ma-DIB's small model resists accumulation [2026-Ma-DIB Benchmark Decision-based Implicit Bias in LLMs].

9. **Class imbalance silently inflates accuracy.** A dummy "always non-hate" classifier (72.73% baseline) beats GPT-3.5 [2025-Ishmam-BanTH A Multi-label Hate Speech Detection Dataset for Transliterated]; accuracy 86.88% masks macro-F1 62.69% [2021-Luu-A Large-scale Dataset for Hate Speech Detection on Vietnamese Social]. Macro-F1, not accuracy/WF1, discriminates because minority classes are hard [2025-Do-ViToSA Audio-Based Toxic Spans Detection on Vietnamese Speech][2024-Ranasinghe-SOLD Sinhala Offensive Language Dataset].

10. **Contamination and data release are the primary long-run saturation mechanism.** McGregor's "longevity" dimension: most of 26 benchmarks score poorly because release norms enable train-to-test; only private AILuminate (75) and holdout ARC-AGI-Private (52) resist; ETHICS and BBQ score longevity 0 [2025-McGregor-BenchRisk Identifying 57 Failure Modes in AI Safety Benchmarks]. Synthetic benchmarks are gamed — F1 0.92, 10% fine-tuning reaches parity — vs ~50% on human data [2025-Machlovi-Towards Safer AI Moderation Evaluating LLM Moderators Through a].

11. **A cheap floor test still discriminates but saturates fast.** SimpleSafetyTests is deliberately easy yet separates Claude 2.1/Llama2 (0% unsafe) from Dolly v2 (69–73%), a 10x open/closed gap [2023-Vidgen-SimpleSafetyTests]; HELM-Safety warns top-model scores now "indicate potential saturation, motivating more difficult benchmarks" [2024-Kaiyom-HELM Safety].

12. **Consistency/coherence metrics stay hard when accuracy saturates.** Grader-free contradiction-check ECI clusters models 0.567–0.708, none near 1.0 [2025-Zhu-TrolleyBench - Evaluating Emergent Moral Reasoning and Consistency in]; budget-constraint CCEI passes only 2/39 at 1% (top 0.417) [2024-Seror-The Moral Mind(s) of Large Language Models]; CMoralEval controlled-variable consistency is near 0 even when explicit-scenario accuracy is higher [2024-Yu-CMoralEval][2025-Yu-CMoralEval A Moral Evaluation Benchmark for Chinese ...].

## B. Evidence table

| Card stem | Most design-relevant fact |
|---|---|
| 2020-Gehman-RealToxicityPrompts | Two-metric (expected-max + probability) separates worst-case from frequency; 44pp toxic/non-toxic gap |
| 2020-Mollas-ETHOS | Cross-dataset transfer (ETHOS→D1: 33% F1) exposes headroom internal CV hides |
| 2020-Pitenis-Greek | Monolingual embeddings beat mBERT 0.89 vs 0.73 — multilingual models create a false floor |
| 2021-Hendrycks-ETHICS | Adversarially-filtered Hard Test (highest-loss items) keeps all models <50% |
| 2021-Luu-Vietnamese | Accuracy 86.88% but macro-F1 62.69% — imbalance inflates the headline |
| 2021-Plaza-del-Arco-OffendES | Rare class (OFG, 425 items) F1 only 38.10% sets the difficulty floor |
| 2022-Chalkidis-FairLex | Triad metric: avg mF1 + disparity + worst-group mF1 so no number hides failure |
| 2022-Parrish-BBQ | Bias reliance increases with capability; ambiguous items carry the signal |
| 2022-Röttger-MHC | Per-function accuracy spread 9.6–97.9% exposes what aggregate F1 hides |
| 2023-Huang-Flames | Keep only prompts that break ≥1 LLM — difficulty gate; best harmless 63.77% |
| 2023-Lin-ToxicChat | In-domain roberta F1 72.1 vs OpenAI Moderation 20.6 — transfer failure proves novel construct |
| 2023-Vidgen-SimpleSafetyTests | Easy floor test still gives 10x open/closed gap; negative predictive power only |
| 2024-AI-Religious-Bias | Refusal ceiling (N/A grades) and info-bias floor both destroy signal |
| 2024-Brun-FrenchToxicity | Trigger-set overlap only 2–8 prompts across families — trigger space unsaturated |
| 2024-Huang-Moral-Persuasion | Ambiguity as a lever; low-ambiguity CAL=0.06 is a floor calibration anchor |
| 2024-Kaiyom-HELM-Safety | Explicit saturation warning; GCG-T adversarial version drops safety 25.9% |
| 2024-Lin-AI-Face | Utility saturated (98% AUC) — headroom only in fairness robustness deltas |
| 2024-Neplenbroek-MBBQ | Accuracy-bounded bias metric; strong models leave "very little room for bias" |
| 2024-Ohashi-eJCM | Culture-specific sub-test (F1 0.787) discriminates when overall F1 0.934 saturates |
| 2024-Ranasinghe-SOLD | Macro-F1 (0.84/0.73) mitigates ceiling inflation from imbalance |
| 2024-Seror-Moral-Minds | CCEI consistency: only 2/39 pass at 1%, top 0.417 — coherence stays hard |
| 2024-Simpson-Parity | Knowledge→reasoning accuracy DROP more discriminating than raw accuracy |
| 2024-Team-FABLE | Race-objective far from ceiling (54.62) while gender saturated (95–97) |
| 2024-Yu-CMoralEval | Neutral third distractor blocks shortcuts; most models near random 0.33 |
| 2024-Zhang-SafetyBench | MCQ surfaces hidden risks open-ended misses (r=0.99); 22/25 models <80% |
| 2025-Al-SHADES | Low-resource languages hit a floor (no meaningful Arabic/Bengali/Hindi answers) |
| 2025-Bai | GPT-4 clean on BBQ but large hidden implicit bias — saturation critique |
| 2025-Davies-F2Bench | Open-ended MDI inverts closed-ended CrowS ranking — MCQ minimum-score artifact |
| 2025-Do-ViToSA | Macro-F1 discriminates (0.500–0.837) where accuracy compresses (0.927–0.951) |
| 2025-Fan-FairMT | Distill hardest 10K→1K to resist saturation; bias rises with turn count |
| 2025-Gamboa-Filipino | Category spread (bakla 40–85) shows variation, not uniform ceiling |
| 2025-Gupta-EnDive | BLEU-difficulty filter discards trivial dialect translations |
| 2025-Ishmam-BanTH | Dummy majority classifier (72.73%) beats GPT-3.5 — imbalance destroys signal |
| 2025-Jin-MedEthicEval | Choose a generator producing subtler violations than GPT-4 |
| 2025-Lahmar-IslamTrust | Best alignment only 66.5%; "Other faiths" hardest (49.75%) |
| 2025-Lan-McBE | Intrinsic SS metric gamed by bigger models — "bigger=more biased" is an artifact |
| 2025-Machlovi | Synthetic F1 0.92 + 10%-fine-tune parity = saturation diagnostic vs human ~50% |
| 2025-McGregor-BenchRisk | Longevity dimension: release norms saturate; private/holdout evaluators resist |
| 2025-Nawale-INDIC-BIAS | Larger models more biased (SAR up to 79%); no ceiling toward fairness |
| 2025-Russo-Pluralistic-Moral-Gap | Consensus level as difficulty axis; ambiguous dilemmas (~0.5) widen the gap |
| 2025-Seker-HATECAT-TR | Symbolization: LLaMA-3.3-70B F1=0.00 — implicit hate is the frontier |
| 2025-Song | Fine-grained sub-labels near-zero (implicit 0.005–0.019) while binary >0.6 |
| 2025-Tomar-BharatBBQ | Disambiguated bias rises sharply vs BBQ; Indian-language bias amplified |
| 2025-Wang-UCerF | WinoBias saturated via semantics; SynthBias (ambiguity difficulty) reshuffles ranks |
| 2025-Wei-MedEthicsQA | Remove items all weak models pass; MCQ 91% vs open-ended 37% |
| 2025-Wu-Staircase | 5-step escalation moves off anchoring; Care ceilings, Fairness stays volatile |
| 2025-Yu-CMoralEval | Consistency accuracies near 0 even when explicit-scenario accuracy higher |
| 2025-Zhu-TrolleyBench | Contradiction-check ECI: none near 1.0; ceiling only under degenerate egoism |
| 2026-Ma-DIB | Longitudinal memory-injection accumulation; dose-response λ; small model resists |
| 2025-Jigsaw-Multilingual | Cross-lingual transfer gap is the discrimination dimension |
| 2024-Almeida | "Correct answer" effect: SD=0 collapses discrimination; per-condition SD as diagnostic |
| 2024-Hancox-Li | 18% deontology items solvable by physics — construct-invalid inflation |
| 2025-Arnob-Bangla | OOV (4.25% STEM words in-vocab) fakes near-zero bias — validity threat |
| 2025-Oh | 99–100% uniformity in 6/14 studies; answer-order flips swing results |
| Anthropic-Sycophancy (2310.13548) | PMs prefer sycophantic over truthful in 95% of misconceptions — reward-model ceiling favors wrong behavior |
| Anthropic-Moral-Self-Correction (2302.07459) | Self-correction emerges at 22B; Q+IF+CoT cuts BBQ bias ~84% |
| NVIDIA-HelpSteer | 4 attributes explain 73% of helpfulness variance — decompose to find the discriminating attribute |
| OpenAI-gpt-oss (2508.10925) | Hate saturated at 0.996 while Cyber Range pass@12 = 0% — pick tasks off both ceilings |
| Anthropic/Butterfly-Effect (2402.09656) | Perplexity↔performance ρ=1.00 — one metric can proxy collapse |

## C. Patterns & disagreements

**Convergence.** (a) The dominant design move is a *two-tier* structure — knowledge vs reasoning [2024-Simpson-Parity Benchmark for Measuring Bias in], MCQ vs open-ended [2025-Wei-MedEthicsQA][2024-Zhang-SafetyBench], utility vs fairness [2024-Lin-AI-Face], intrinsic-preference vs comprehension [2025-Lan-McBE A Multi-task Chinese Bias Evaluation Benchmark for Large]. (b) Ambiguity is the reliable difficulty reservoir [2022-Parrish-BBQ Bias Benchmark for Question Answering][2024-Neplenbroek-MBBQ A Dataset for Cross-Lingual Comparison of Stereotypes in][2025-Russo-The Pluralistic Moral Gap]. (c) Macro-F1/minority-class metrics beat accuracy for imbalanced data [2021-Luu-A Large-scale Dataset for Hate Speech Detection on Vietnamese Social][2025-Do-ViToSA Audio-Based Toxic Spans Detection on Vietnamese Speech][2024-Ranasinghe-SOLD Sinhala Offensive Language Dataset]. (d) Contamination/release is the main long-run saturation driver [2025-McGregor-BenchRisk Identifying 57 Failure Modes in AI Safety Benchmarks][2025-Machlovi-Towards Safer AI Moderation Evaluating LLM Moderators Through a].

**Disagreement.** On format: Davies argues *open-ended* is harder and MCQ's guessing artifact inverts rankings [2025-Davies-F2Bench An Open-ended Fairness Evaluation Benchmark ...], whereas SafetyBench argues *MCQ* surfaces hidden risks open-ended eval lets aligned models dodge [2024-Zhang-SafetyBench] — both right, so use both. On size: most cards find bias rises with scale [2025-Bai-Explicitly unbiased large language models still form biased][2025-Nawale-FairI Tales INDIC-BIAS - Evaluation of Fairness in Indian Contexts], but Ma-DIB's small model resists accumulation [2026-Ma-DIB Benchmark Decision-based Implicit Bias in LLMs] and McBE attributes "bigger=more biased" to a likelihood-metric artifact [2025-Lan-McBE A Multi-task Chinese Bias Evaluation Benchmark for Large]. Vidgen defends easy gates [2023-Vidgen-SimpleSafetyTests] while HELM-Safety flags them saturated [2024-Kaiyom-HELM Safety].

## D. Exemplars & anti-patterns

**Best-designed for durable discrimination.** (1) **Wang-UCerF/SynthBias** — difficulty defined by *human-judged ambiguity* so it stays hard as models improve, plus embedding-space coverage audits and a confidence×correctness axis ranking overconfident-wrong worst [2025-Wang-Is Your Model Fairly Certain Uncertainty-Aware]. (2) **Hendrycks-ETHICS** — normal + adversarial Hard Test, small-edit contrast sets, grouped all-correct scoring, disagreement-detection task [2021-Hendrycks-Aligning AI with Shared Human Values]. (3) **McGregor-BenchRisk** — treats longevity as an engineered property with concrete anti-contamination mitigations [2025-McGregor-BenchRisk Identifying 57 Failure Modes in AI Safety Benchmarks]. (4) **Fan-FairMT** — hardest-item distillation + turn-accumulation resists saturation [2025-Fan-FAIRMT-BENCH].

**Anti-patterns.** (1) **ETHICS** — 18% of deontology items solvable without moral reasoning [2024-Hancox-Li-Is ETHICS about ethics]. (2) **WinoBias** — semantically exploitable, now saturated [2025-Wang-Is Your Model Fairly Certain Uncertainty-Aware]. (3) **Synthetic-only moderation suites** — F1 0.92, gameable with 10% fine-tuning [2025-Machlovi-Towards Safer AI Moderation Evaluating LLM Moderators Through a]. (4) **Binary imbalanced hate sets** where a majority-class dummy beats an LLM [2025-Ishmam-BanTH A Multi-label Hate Speech Detection Dataset for Transliterated]. (5) **Bias metrics without OOV checks** — near-zero "bias" is a vocabulary artifact [2025-Arnob-Assessing Gender Bias of Pretrained Bangla Language Models]. (6) Reward models themselves saturate wrong: PMs prefer sycophantic over truthful in 95% of misconceptions [Anthropic-Collective_Constitutional_AI_Democratizing_AI_Alignment_2310.13548].

## E. Design lessons

1. **Ship a two-tier instrument** — easy recognition layer + hard applied layer, reporting the *drop* between them as the discrimination metric [2024-Simpson-Parity Benchmark for Measuring Bias in][2025-Wei-MedEthicsQA][2025-Lan-McBE A Multi-task Chinese Bias Evaluation Benchmark for Large].
2. **Engineer difficulty explicitly** — adversarially filter (highest-loss / attack-success gate), distill cross-model hardest items, prune items all weak models pass [2021-Hendrycks-Aligning AI with Shared Human Values][2023-Huang-Flames][2025-Fan-FAIRMT-BENCH][2025-Wei-MedEthicsQA].
3. **Mine ambiguity** — add underspecified contexts, stratify by human consensus, and score correct abstention [2022-Parrish-BBQ Bias Benchmark for Question Answering][2025-Russo-The Pluralistic Moral Gap][2025-Wang-Is Your Model Fairly Certain Uncertainty-Aware].
4. **Kill shortcuts** — remove semantic/physics/keyword solvability via minimal-pair contrasts, neutral distractors, and BLEU/similarity filters [2024-Hancox-Li-Is ETHICS about ethics][2024-Yu-CMoralEval][2025-Gupta-EnDive A Cross-Dialect Benchmark for Fairness and Performance in].
5. **Use both formats** — MCQ for cheap scoring that surfaces hidden risk, open-ended to catch guessing artifacts and rank inversions [2024-Zhang-SafetyBench][2025-Davies-F2Bench An Open-ended Fairness Evaluation Benchmark ...].
6. **Add a multi-turn/longitudinal axis** — score after adversarial context build-up; single-shot cues are already saturated [2025-Fan-FAIRMT-BENCH][2026-Ma-DIB Benchmark Decision-based Implicit Bias in LLMs].
7. **Report the right metric for imbalance** — macro-F1/worst-group, publish base rates and a majority-class baseline, check OOV before embedding metrics [2022-Chalkidis-FairLex][2025-Arnob-Assessing Gender Bias of Pretrained Bangla Language Models].
8. **Test for the "correct answer" effect** — flag items where >99% of responses are identical; report per-condition SD and answer-order robustness [2024-Almeida-Exploring the Psychology of LLMs Moral Reasoning][2025-Oh-Robustness of Large Language Models in Moral Judgements].
9. **Add saturation-resistant coherence metrics** — contradiction-checks (ECI), rationality/CCEI, paired appropriate/inappropriate consistency stay hard when accuracy ceilings [2025-Zhu-TrolleyBench - Evaluating Emergent Moral Reasoning and Consistency in][2024-Seror-The Moral Mind(s) of Large Language Models][2024-Yu-CMoralEval].
10. **Design against contamination from day one** — private/holdout evaluators, access-gated release, shipped templates for regeneration, synthetic-vs-human collapse audits [2025-McGregor-BenchRisk Identifying 57 Failure Modes in AI Safety Benchmarks][2023-Huang-Flames][2025-Al-SHADES A New Multilingual Benchmark for Stereotypes Bias in Large][2025-Machlovi-Towards Safer AI Moderation Evaluating LLM Moderators Through a].
11. **Don't assume scale = alignment** — test whether the largest model is most biased and separate genuine bias from likelihood-metric artifacts [2025-Bai-Explicitly unbiased large language models still form biased][2025-Nawale-FairI Tales INDIC-BIAS - Evaluation of Fairness in Indian Contexts][2025-Lan-McBE A Multi-task Chinese Bias Evaluation Benchmark for Large].
12. **Keep a floor test but state its limits** — negative predictive power only, and it will saturate [2023-Vidgen-SimpleSafetyTests][2024-Kaiyom-HELM Safety].
13. **Localize to re-open headroom** — culture-specific sub-tests and non-WEIRD ontologies restore discrimination where general items saturate [2024-Ohashi-Extended Japanese Commonsense Morality Dataset][2025-Tomar-BharatBBQ A Multilingual Bias Benchmark for][2025-Gamboa-Filipino Benchmarks for Measuring Sexist and Homophobic Bias in].
