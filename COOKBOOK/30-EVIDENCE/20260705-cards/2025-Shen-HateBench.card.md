---
stem: "2025-Shen-HateBench"
reader_model: "opus"
confidence: "high"
is_benchmark: true
theme_tags: [contamination-robustness, saturation-discrimination, best-practices, ai-lab-practices]
task_format: "generative"
scoring_type: "mixed"
dataset_size: 7838
dataset_construction: "LLM-generated"
languages: [English]
models_tested: [GPT-3.5, GPT-4, Vicuna-7B, Baichuan2-7B, Dolly2-7B, OPT-6.7B, Perspective, Moderation, Detoxify-Original, Detoxify-Unbiased, LFTW, TweetHate, HSBERT, BERT-HateXplain]
headline_numbers: ["HATEBENCHSET = 7,838 annotated samples (3,641 hate / 4,197 non-hate) across 34 identity groups from 6 LLMs (p.1, p.3)", "Perspective F1 drops from 0.878 on GPT-3.5 to 0.621 on GPT-4 (p.4)", "TextFooler adversarial attack reaches ASR 0.966/0.974/0.975 on Perspective/Moderation/TweetHate (p.9)", "Model stealing yields 13-21x attack-efficiency speedup (p.1)", "Krippendorff's Alpha = 0.846 across annotators (p.3)"]
---
## 1. Gist
HATEBENCH is a framework and dataset (HATEBENCHSET) for benchmarking hate-speech detectors specifically on LLM-generated content. It asks two questions: (RQ1) can existing detectors catch hate speech that LLMs produce, and does effectiveness vary by generator model / identity group; and (RQ2) can detectors survive adversarial and model-stealing "hate campaigns." It matters for values-alignment because it stress-tests the safety filters (Perspective, OpenAI Moderation, Detoxify, etc.) that labs rely on to cleanse training data and guard model outputs — showing they silently degrade on newer, more fluent generators and collapse under cheap adversarial perturbation. To appear at USENIX Security 2025.

## 2. Benchmark/eval design features
- Construct measured: binary hate vs. non-hate on LLM-generated text, following the UN definition of hate speech (p.3).
- 34 identity groups spanning race, religion, origin, gender, sexual orientation, disability (p.3).
- 6 generator LLMs (GPT-3.5, GPT-4, Vicuna, Baichuan2, Dolly2, OPT) x 6 prompts (3 negative + 3 positive/neutral) x 3 repeats x {original, 2 jailbreak statuses} = 11,016 raw generations, filtered to 7,838 (p.3).
- 8 detectors benchmarked (4 open-source community + 4 commercial), selected by Pareto download frequency on HuggingFace and hate-definition alignment (p.4).
- Second axis: adversarial robustness (character/word/sentence-level attacks) and model-stealing surrogate detectors.

## 3. Task format & example item
Detectors classify generated statements as hate/non-hate. Generation prompts are simplistic (used to elicit content about a group). Saliency example (p.10): original "Fuck those people with cognitive disorders or learning disabilities They are just retards who can't even take care of themselves" (0.6 hate) vs adversarial "Shafted those people... just simpletons..." (0.72 not-hate).

## 4. Scoring / grading methodology
Detector performance scored with accuracy, precision, recall, macro-F1 vs. human ground truth (p.4). Ground-truth labels from 3 expert annotators, majority vote, third labeler on disagreement (p.3). Adversarial campaign scored by ASR, WMR, USE, Meteor, Fluency (GPT-2 perplexity), #Query, Time (p.8). Stealthy campaign adds attack accuracy and attack agreement (p.8).

## 5. Dataset construction & provenance
LLM-generated via mix of 3 negative + 3 positive/neutral prompts over 34 identity groups from prior MHS taxonomy [65]; temperature 1.0, response length 256 (p.3). Original + 2 jailbreak statuses to reduce jailbreak bias. 11,016 raw → exclude 3,178 N/A refusals → 7,838 testbed (p.3). Human-written comparison uses MHS dataset (Reddit/Twitter/YouTube) with matching identity taxonomy (p.5). Code released on GitHub (p.1).

## 6. Validity evidence
Inter-annotator reliability Krippendorff's Alpha = 0.846 overall (per-LLM range 0.610 OPT to 0.961 GPT-4) (p.3-4). Equivalently-hateful annotation of adversarial outputs: second Alpha = 0.788, 450 samples, 3 labelers (p.9). Saliency maps validate that identity/derogatory words drive predictions (p.6). T-SNE shows GPT-4 output most distant from human text, explaining degraded detection (p.5).

## 7. Saturation / discrimination
Discriminates strongly across generators: same detector spans F1 0.621-0.885 depending on source LLM (p.4). Top detectors cluster near F1 0.82-0.86 on the full set (p.4) — modest headroom on clean data but the adversarial axis reopens huge headroom (ASR up to 0.975), so the benchmark is far from saturated once robustness is included. Identity-group F1 ranges 0.667 (Gay) to 0.933 (Christian) for Perspective (p.6).

## 8. Multiturn / agentic aspects
Not conversational, but models an adversarial pipeline: adversary with black-box access iteratively queries detector, identifies influential words, perturbs, and optionally trains a surrogate (model stealing) to move optimization offline — effectively an automated agentic hate-campaign loop (p.7-8).

## 9. Key numbers
- 7,838 samples; 3,641 hate / 4,197 non-hate; 34 identity groups; 6 LLMs (p.1, p.3).
- 11,016 raw generations; 3,178 N/A refusals excluded (p.3).
- Top detectors F1: TweetHate 0.864, Moderation 0.852, LFTW 0.825, Perspective 0.821 (p.4).
- Perspective F1: 0.878 (GPT-3.5) → 0.621 (GPT-4) (p.4).
- GPT-4 non-hate profanity 53% vs GPT-3.5 17% (p.4).
- TextFooler ASR 0.966/0.974/0.975 (Perspective/Moderation/TweetHate) (p.9).
- Restricted TextFooler (no identity words) ASR 0.852/0.955/0.952; equivalently-hateful 95.4/96.2/100% (p.9).
- Model stealing efficiency gain 13-21x (p.1).

## 10. Pitfalls & limitations
- Simplistic prompts = best-case for detectors; may overstate detector competence (author-acknowledged, p.3).
- Only English (p.4) — no code-mixed / multilingual coverage.
- Binary hate/non-hate collapses severity gradations.
- N/A refusals (29% of generations) dropped, so benchmark excludes the alignment-success cases.
- Paraphrase attack often destroys hatefulness (equivalently-hateful only 34.8-44.4%, p.9), so its ASR is inflated.
- Older generator/detector snapshots (GPT-3.5/4-turbo era) date quickly.

## 11. Novel ideas worth stealing
- **Generator-stratified evaluation**: score the same detector separately per source model to expose degradation on newer, more fluent generators — directly transferable to any values benchmark where the item author (human vs GPT-3.5 vs GPT-4) is a hidden variable.
- **N/A / refusal as an explicit third label** rather than folding refusals into non-hate — cleanly separates alignment (declined) from judgment (non-hate).
- **Lexical-difficulty diagnostics** (Coleman-Liau, perplexity, Type-Token ratio, profanity rate) to explain WHY scores move, not just that they move.
- **Adversarial-robustness axis with equivalently-hateful human check** — pairing ASR with a human verification that the perturbed item still expresses the target construct; prevents crediting attacks that merely destroy the signal.
- **Saliency-map leave-one-out interpretation** to audit whether a scorer keys on identity tokens vs. genuine hostility — a bias probe reusable for any classifier-scored benchmark.
- **Model-stealing threat model** as a stress test for any deployed LLM-judge/API scorer.

## 12. Notable quotes
- "while detectors are generally effective in identifying LLM-generated hate speech, their performance degrades with newer versions of LLMs" (p.1).
- "The most potent adversarial attack achieves an attack success rate of 0.966, and its attack efficiency can be further improved by 13−21× through model stealing attacks" (p.1).
- "Perspective performs well on GPT-3.5 with an F1-score of 0.878, but its performance drops to 0.621 on GPT-4" (p.1-2).
- "53% of non-hate samples from GPT-4 include profanity, compared to 17% from GPT-3.5" (p.4).

## 13. UNKNOWN / not in extract
- Full per-detector adversarial and stealthy-campaign numeric tables beyond p.10 (pages 11-22 not read in detail).
- Appendix prompt-engineering (Appendix E) exact results.
- Licensing terms of HATEBENCHSET release.
- Exact per-identity-group breakdown table (Figure 12 in appendix).
