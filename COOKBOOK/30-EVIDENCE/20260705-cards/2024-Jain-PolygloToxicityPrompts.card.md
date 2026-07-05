---
stem: "2024-Jain-PolygloToxicityPrompts"
reader_model: "opus"
confidence: "high"
is_benchmark: true
theme_tags: [cultural-linguistic, contamination-robustness, best-practices]
task_format: "generative"
scoring_type: "classifier"
dataset_size: 425000
dataset_construction: "scraped"
languages: [ar, zh, cs, nl, en, fr, de, hi, id, it, ja, ko, pl, pt, ru, es, sv]
models_tested: ["GPT-3.5-Turbo", "Aya101", "Bloomz (560m-7b1)", "Llama-2-chat (7/13/70b)", "Tulu-2-DPO", "Pythia suite (70m-12b)", "TinyLlama", "Archangel Llama suite", "Gemma-7b-it", "Zephyr-7b-gemma", "Qwen-7B-Chat", "Mistral-Instruct"]
headline_numbers: ["425K naturally occurring prompts across 17 languages (p.1)", "62 LLMs benchmarked (p.4)", "Pearson r=0.49 between prompt toxicity and continuation toxicity (p.9)", "Perspective API vs Llama Guard correlation r=0.78 (p.8)", "base models AT=0.281, Cohen's d=0.40 vs instruct (p.7)"]
---
## 1. Gist
PolygloToxicityPrompts (PTP) is the first large-scale multilingual toxicity-degeneration benchmark: 425K naturally occurring prompts scraped from web-text across the 17 languages supported by Perspective API. It measures "neural toxic degeneration" — the propensity of an LLM to continue a prompt with toxic text. Unlike prior work that translates English RealToxicityPrompts (introducing translation artifacts and losing cultural nuance), PTP uses natively-occurring toxic web-text, surfacing substantially more toxicity from LLMs. For values-alignment benchmarking it is a strong exemplar of (a) cross-lingual safety evaluation, (b) using an industry classifier as a scalable scorer, and (c) studying how model size and alignment method (SFT/PPO/DPO/KTO/IPO) affect an alignment-relevant behavioral outcome.

## 2. Benchmark/eval design features
Construct: toxicity of model continuations given naturally occurring prompts. Answer space is open generative text; toxicity is a scalar in [0,1] from Perspective API's TOXICITY score. Three aggregate metrics: Expected Maximum Toxicity (EMT, worst-case over K completions), Empirical Probability (EP, prob. of at least one completion scoring ≥0.5 in K), and Average Toxicity (AT, mean over completions). Prompts are stratified across 4 equal-width toxicity bins so difficulty spans non-toxic to highly-toxic. 25K prompts/language; PTPSMALL is a 5K/language stratified subset for compute-limited benchmarking. Research questions probe language resource level, model size (within-family via Pythia), base vs instruct vs preference tuning, alignment-method choice, and human vs AI feedback.

## 3. Task format & example item
Sentence/document-completion: a scraped web-text document is split in half; the first half is the prompt, the model generates a continuation which is scored. No verbatim example prompt appears in the extract pages read (prompts are potentially toxic web text and not reproduced inline). "n/a" for an exact quoted item.

## 4. Scoring / grading methodology
Automated classifier scoring via Perspective API TOXICITY score (UTC framework: Charformer-based Seq2Seq pretrained on mC4 + Perspective Pretraining Corpus; plus a distilled CNN for German/Portuguese). K=10 completions per prompt, temperature 0.7, top_p 1, max 512 tokens. Metrics EMT/EP/AT computed per model per language. Also compared against Llama Guard (safety classifier, English only) to distinguish toxicity vs safety.

## 5. Dataset construction & provenance
Scraped 100M+ documents from mC4 and The Pile; English split additionally uses Pile Curse (bad-words-scored subset). All docs scored with Perspective API; sampled 6250 docs from each of 4 toxicity bins. Because mC4 filters bad-words (yielding <0.01% toxicity for 9 languages), ~70K synthetic high-toxicity prompts (16.8% of data) were made by translating toxic mC4/Pile samples via NLLB-3.3B; original-vs-translated toxicity correlated r=0.725 (p.4). Final: 25K/language × 17 = 425K. Prompts average ~400 GPT-4 tokens (much longer than RTP). Planned release under AI2 ImpAct license to mitigate dual use.

## 6. Validity evidence
Criterion-style comparison: PTP elicits higher AT than RTP-LX and WildChat across multilingual models (Fig 9, p.9), supporting that naturally occurring longer prompts surface more toxicity. Perspective vs Llama Guard correlation r=0.78 shows convergent but non-identical constructs. Translation validity: original/translated toxicity r=0.725 (p.4). No human validation of toxicity labels was performed (author-admitted limitation, p.10).

## 7. Saturation / discrimination
Wide score spread across languages (AT ranges roughly 0.078 to 0.328 across models, Table 1, p.4) and clear stratification by language resource level (Table 2, p.6). Meaningful headroom remains: even highly capable GPT-3.5-Turbo shows high non-English toxicity, indicating the benchmark is far from saturated for multilingual safety.

## 8. Multiturn / agentic aspects
n/a — single-turn prompt-continuation, no tools or interaction.

## 9. Key numbers
- 425K prompts, 17 languages, 25K/language (p.1, p.4).
- 62 LLMs benchmarked (p.4); paper text also says "over 60" (p.1).
- ~70K translated prompts = 16.8% of dataset; original/translated toxicity r=0.725, p≤0.001 (p.4).
- Base-model size vs toxicity r=0.015, p<0.001 (weak) (p.6); Pythia plateaus near 2.8b, 2.8b-vs-12b Cohen's d≤0.1 (p.7).
- base AT=0.281; base vs instruct d=0.40, base vs preference d=0.43; instruct vs preference d=0.02 (p.7).
- Alignment-method choice difference Cohen's d<0.1 (p.8).
- Prompt vs continuation toxicity r=0.49 overall; base r=0.65, preference r=0.49, instruct r=0.44 (p.9).
- Perspective vs Llama Guard r=0.78, p≤0.001 (p.8).

## 10. Pitfalls & limitations
Author-admitted (p.10): toxicity is subjective and Perspective may not cover all facets; no human validation at scale; naturally occurring web-text may not represent user-LLM interactions or conversational/social-media toxicity; excludes low-resource languages lacking detection tools; Perspective known to over-flag minority-identity mentions (p.9). Observed by reader: reliance on a single proprietary classifier as ground truth couples the benchmark to Perspective's biases; the 16.8% translated data partly reintroduces the translation-artifact problem the paper critiques; benchmarking uses safety-disabled API and raw models, so numbers do not reflect deployed guardrails.

## 11. Novel ideas worth stealing
- Stratified sampling across equal-width toxicity/target bins to guarantee difficulty spread and avoid a benchmark saturated at "easy" items — directly transferable to values benchmarks (sample across a values-conflict severity axis).
- Use naturally occurring, long-context prompts rather than templated or translated ones to surface more realistic behavior; longer prompts elicited more toxicity, suggesting values benchmarks should test long realistic contexts, not short templates.
- Triangulating two scorers (Perspective toxicity vs Llama Guard safety) to show "related but distinct" constructs — a cheap validity move: run two independent judges and analyze disagreement cases.
- Small stratified subset (PTPSMALL) shipped alongside full set for compute-limited replication — good benchmark-engineering practice.
- Controlled within-family scaling (Pythia suite) and matched-data/different-alignment (Archangel, TinyLlama) designs to isolate causal factors on an alignment outcome.
- Multi-metric reporting (expected-max / empirical-probability / average) to capture worst-case vs typical behavior.

## 12. Notable quotes
- "We introduce POLYGLOTOXICITYPROMPTS (PTP), the first large-scale multilingual bench-mark for evaluating neural toxic degeneration" (p.1).
- "toxicity increases as language resources decrease or model size increases" (p.1).
- "while instruction- and preference-tuning reduce toxicity, the choice of preference-tuning method does not have any significant impact" (p.1).
- "Our findings suggest that LLM safety detectors may not be equipped to capture the full spectrum of toxicity." (p.8).

## 13. UNKNOWN / not in extract
- Exact per-language AT/EP/EMT tables (Table 5) and appendices not fully read.
- No verbatim example prompt available in read pages.
- Full list of all 62 models not enumerated in the read pages.
- Licensing final terms and leaderboard details beyond ImpAct mention.
