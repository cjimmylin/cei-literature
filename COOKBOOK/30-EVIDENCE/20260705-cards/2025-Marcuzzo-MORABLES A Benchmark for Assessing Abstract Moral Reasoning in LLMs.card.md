---
stem: "2025-Marcuzzo-MORABLES A Benchmark for Assessing Abstract Moral Reasoning in LLMs"
reader_model: "opus"
confidence: "high"
is_benchmark: true
theme_tags: [moral-psychology, saturation-discrimination, contamination-robustness, cultural-linguistic]
task_format: "MCQ"
scoring_type: "mixed"
dataset_size: 709
dataset_construction: "mixed"
languages: [en]
models_tested: ["Mistral 7B", "Llama 3.1 8B", "Qwen 2.5 7B", "Mixtral 8x22B", "Llama 3.3 70B", "DeepSeek V3", "Gemini 2.0 Flash", "GPT-4o", "Claude 3.5 Sonnet", "GPT-o3-mini", "DeepSeek R1"]
headline_numbers: ["Claude 3.5 Sonnet best on core MCQA at 84.8% (p.6)", "Best models self-refute own answers in ~20% of cases under TF/NOTO reframing (p.1,8)", "40+ percentage-point gap between worst small (Mistral 7B 28.4%) and best large (Llama 3.3 70B 73.6%) (p.6)", "Combined adversarial modifications drop accuracy up to 12.3% for GPT-4o, 10.5% for Llama 3.3 (p.7)", "709 fable/moral pairs, avg fable 133.4 words, avg moral 11.6 words (p.3)"]
---
## 1. Gist
MORABLES is a human-verified benchmark of 709 historical fables/short stories (primarily Western, Aesop-centric) each paired with an author-attributed moral, framed as a 5-option multiple-choice moral-inference task. It targets abstract moral reasoning rather than extractive reading comprehension, using carefully engineered distractors and adversarial variants to separate genuine moral inference from thematic pattern-matching and memorization. It matters for values-alignment benchmarking because it operationalizes "does the model grasp the moral lesson of a narrative" as a discriminating, contamination-aware task and shows that even top models are brittle — self-contradicting under reframing and swayed by superficial cues.

## 2. Benchmark/eval design features
Construct: abstract moral inference from narrative. Item structure: a fable + 5 candidate morals (1 ground-truth + 4 typed distractors). Four distractor types (p.3-4): (1) similar-character moral (moral from another story with similar entities), (2) trait-injected moral (incorrect moral with character traits inserted), (3) feature-based moral (LLM-generated from character traits only, detached from plot), (4) partial-story moral (LLM-generated from first 10% of sentences). Four variants (p.5, Table 2): Core (709), NOTO (correct answer replaced by "None of the other options", 709), TF (binary True/False per choice, 3,545 = 709×5), ADV (adversarial modifications, 709). Adversarial modifications: character swap, trait injection, tautology prepend/append.

## 3. Task format & example item
MCQA, predict answer-ID token. Verbatim (p.2, Fig.1): "The Wolf and the Crane... (A) There is nothing more valuable than liberty. (B) Expect no reward for serving the wicked. (C) Gratitude can turn pain into promise. (D) Unity is mankind's greatest good... (E) Desperation can turn foes into allies." Correct: (B).

## 4. Scoring / grading methodology
MCQA: first generated token (stripped) matched against correct option ID; temperature 0; options shuffled to balance token position; one-shot prompt reported as upper bound (zero-shot drops 4-6%) (p.6). TF: precision/recall/F1 on binary True/False (p.7, Table 6). NOTO: accuracy plus a novel "Consistency" metric — % of incorrect NOTO picks the model had previously labeled True in the TF task (p.7). Free-text morals: human 1-5 Likert alignment rubric by 5 annotators + BERTScore F1 (p.8).

## 5. Dataset construction & provenance
Sourced from open-domain historical fable collections (Aesop primary, also La Fontaine); requires fable+moral, historical/official translation, public domain (p.3). Duplicate removal via word IoU, BERTScore, and Perry Index. Distractor generation used GPT-4o with human verification. 709 final pairs. Human validation: 5 graduate English-native annotators (Computer Science, Neuroscience, Theology, Literature), Cohen's Kappa 0.6-0.75, each fable double-annotated; 152 fables needed a moral/distractor replaced; outdated-value morals updated (p.4). Publicly on HuggingFace (cardiffnlp/Morables). English only, Western-biased (admitted limitation).

## 6. Validity evidence
Inter-annotator agreement Cohen's Kappa 0.6-0.75 (substantial) (p.4). Similarity thresholds (>0.5 IoU, >0.4 BERTScore F1) trigger manual review (~15% feature-based, ~25% partial-story morals) to keep distractors plausible-but-wrong (p.4). Self-preferential-bias check for GPT-4o (used to generate distractors): found no clear outlier advantage (p.10). Free-text: BERTScore-vs-human Pearson correlation only 0.28-0.35, weak — automated metrics fail to capture the construct (p.8-9).

## 7. Saturation / discrimination
Strong discrimination: 40+ point spread across model scales (p.6). Core range 28.4% (Mistral 7B) to 84.8% (Claude 3.5) — not saturated; best models leave ~15% headroom and are far from human ceiling. Reframing (TF/NOTO) and adversarial variants further expose brittleness, indicating remaining headroom in "genuine" reasoning even where raw accuracy is high.

## 8. Multiturn / agentic aspects
n/a — single-turn MCQA / binary classification / one-shot generation. No tools or environment.

## 9. Key numbers
- Core accuracy: Mistral 7B 28.4%, Llama 3.1 8B 34.0%, Qwen 2.5 7B 46.8%, Mixtral 8x22B 56.9%, DeepSeek V3 70.6%, Llama 3.3 70B 73.6%, Gemini 2.0 Flash 80.7%, GPT-4o 84.0%, Claude 3.5 Sonnet 84.8%, GPT-o3-mini 66.3%, DeepSeek R1 77.0% (p.6, Table 3).
- "Partial-story" is most frequent wrong choice across models; feature-based distractor: Llama 3.3 70B 8.8% vs GPT-4o 4.9% vs Claude 3.5 3.7% (p.6).
- NOTO consistency: Claude 3.5 changes stance ~38% of cases; ~20% self-refutation gap remains for stable models (p.8).
- ADV: tautology-append most impactful; combined mods drop GPT-4o to 71.7%, Llama 3.3 to 63.1% (p.7, Table 7).
- Free-text ratings: GPT-4o 3.83, Claude 3.5 3.76, Llama 3.3 3.66 (1-5); BERTScore F1 0.22-0.29 (p.8-9).

## 10. Pitfalls & limitations
Author-admitted: high memorization risk — models likely saw fables and morals in pretraining, limiting definitive claims about reasoning (p.10). Western/English-only, restricting cultural-bias study (p.10). GPT-4o generated distractors → potential self-preferential bias (mitigated but noted). Distractors partly GPT-4o-generated → benchmark inherits generator idiosyncrasies. My read: TF class imbalance (20/80) inflates accuracy and confounds precision/recall interpretation (p.7); free-text human ratings have huge SD (~1.29) reflecting subjectivity; only 2 models run on full ADV grid; reasoning models tested once (no variance).

## 11. Novel ideas worth stealing
- **Typed distractors mapped to specific failure modes** (similar-character, trait-injected, feature-based, partial-story) — the answer-choice distribution becomes a diagnostic of *how* a model fails, not just whether (p.3-4,6). Reusable for any values benchmark: engineer each wrong option to test one shortcut.
- **NOTO variant + Consistency metric**: replace the correct answer with "None of the others" and cross-check against the model's own TF judgments to distinguish stable-but-wrong interpretation from sycophantic answer-picking (p.7). A cheap self-contradiction probe.
- **TF reframing** of a single MCQA item into N True/False statements to surface over-acceptance / low precision (p.5,7).
- **Tautology injection** as adversarial noise (semantically empty sentences at start/end) to expose positional attention-sink biases (p.5,7).
- **Contamination-aware framing**: treat memorization as inevitable and build adversarial perturbations + plan for entirely-new unseen stories (p.10).
- **Semi-automatic similarity gating** (IoU/BERTScore thresholds) to route only borderline distractors to expensive human review (p.4).

## 12. Notable quotes
- "even the best models contradict their own judgments in roughly 20% of cases when the moral inference task is reframed" (p.2).
- "scale – not reasoning ability – is the primary driver of performance" (p.1).
- "models would rather select a wrong answer than none" (p.8).
- "our dataset is unfortunately more than likely biased toward moral lessons that reflect Western values" (p.10).

## 13. UNKNOWN / not in extract
Exact prompt templates (Appendix E), full Appendix A textual/readability analysis, per-language expansion plans specifics, licensing details of each source collection, and the answer-ID/token-bias experiment numbers (Appendix D) are referenced but not in the read portion.
