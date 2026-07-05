---
stem: "2025-Singh-Rethinking Hate Speech Detection on Social Media Can LLMs Replace"
reader_model: "opus"
confidence: "high"
is_benchmark: true
theme_tags: [cultural-linguistic, design-space, best-practices, contamination-robustness]
task_format: "free-text"
scoring_type: "classifier"
dataset_size: 11725
dataset_construction: "mixed"
languages: [Hindi, English, Hinglish]
models_tested: [mBERT, XLM-RoBERTa, Perspective, Mistral-7B, LLaMA3.1-8B, InternLM2.5-7B, Qwen2.5-7B, GPT-4o-mini]
headline_numbers: ["IndoHateMix = 11,725 samples (4,457 hate / 7,268 non-hate), Fleiss' Kappa 0.685 (p.4, p.7)", "LLaMA3.1-8B beats mBERT by ~4/8/14% accuracy on HateXplain/ImplicitHate/IndoHateMix (p.10)", "LLaMA3.1-8B fine-tuned on 10% data (~4M LoRA params) beats mBERT on full data (179M params) (p.11)", "LLaMA3.1-8B IndoHateMix F1 0.82 vs mBERT 0.77 vs Perspective 0.59 (p.10)"]
---
## 1. Gist
This paper argues that modern LLMs (LLaMA-3.1, Mistral, Qwen, InternLM) not only surpass fine-tuned BERT-based detectors on hate-speech classification but should redefine the task — and introduces IndoHateMix, a Hindi-English code-mixed / transliterated benchmark scraped from the Indian microblogging platform Koo. It matters for values-alignment because it (a) supplies a culturally-grounded, code-mixed benchmark where WEIRD/English-centric detectors fail, and (b) empirically challenges the "build specialized detectors" paradigm in favor of curating diverse datasets to fine-tune general LLMs. The framing directly bears on pluralistic, non-English values coverage.

## 2. Benchmark/eval design features
- Construct: binary hate vs. non-hate classification across three datasets — HateXplain, ImplicitHate, and the new IndoHateMix (p.2).
- IndoHateMix uniquely captures code-mixing + transliteration and *both* community-directed (religious/caste) and individual-directed (political-leader) hate (p.7).
- Target-of-hate analysis: religious groups (Hindus/Muslims/Sikhs/Jews), racial/ethnic (African Americans/Mexicans), political figures (Modi/Gandhi/Kejriwal) color-coded across datasets (p.7).
- Benchmarks 3 model families: multilingual BERT, off-the-shelf API (Perspective), and 5 LLMs.
- Transfer-learning axis: cross-dataset train/test heatmaps + 10%-data low-resource regime.

## 3. Task format & example item
Free-text social-media post → binary label. Prompt (p.9): Instruction "Review the provided statement and classify it as 'Hate' or 'Non-Hate.' Return '1' for Hate and '0' for Non-Hate." Example hate item (p.6): "a clever enemy is much better than a stupid friend. despite knowing fact, party leaders hug & felicitate him." Example non-hate (p.6): "yes, they must condemn this dastardly act in a loud and clear voice."

## 4. Scoring / grading methodology
Standard classification metrics — accuracy, precision, recall, F1 — against human gold labels (Table 2, p.10). No LLM-judge; LLM outputs are the classification decision compared to ground truth (exact label match → treated as classifier scoring). Perspective proxied by max of 6 toxicity subscores > 0.5 threshold (p.8).

## 5. Dataset construction & provenance
IndoHateMix scraped from Koo ("India's Twitter"), Dec 2023-Jan 2024, via keyword-seeded account discovery (Israel, Palestine, Khalistan, Pakistan, Election, etc.) then follower expansion (p.5). 300 posts per account (spaced for high-activity accounts); 50% candidate Koos sampled, posts + comments (p.5-6). Preprocessing: remove URLs/emojis, lowercase, dedupe by cosine similarity, keep 5-55 word posts, strip '#' (p.6). Manual annotation by 3 expert annotators, binary scheme, consensus on ambiguous cases (p.6-7). Final: 11,725 samples, 38.01% hate. HateXplain (12,375) and ImplicitHate (21,480) restructured to binary (p.4-5).

## 6. Validity evidence
Inter-annotator agreement Fleiss' Kappa = 0.685 (substantial), with collaborative review of ambiguous cases (p.7). Cross-dataset transfer heatmaps test generalization (p.11-12). Detailed error analysis (Table 3) shows mBERT fails on short/indirect/code-mixed hate and over-flags sarcasm, while LLaMA-3.1 handles them (p.12-13). Limited-data results averaged over 5 runs to reduce variance (p.11).

## 7. Saturation / discrimination
IndoHateMix is the hardest: mBERT accuracy 0.73 and XLM-R F1 collapses to 0.33 (p.10), vs. HateXplain where mBERT reaches 0.87 — so the new benchmark reopens substantial headroom. LLM ceiling on IndoHateMix ~0.82-0.83 accuracy leaves room. Discrimination across model families is clear (LLMs 0.79-0.82 vs Perspective 0.59 F1) (p.10).

## 8. Multiturn / agentic aspects
n/a — single-turn zero/fine-tuned classification only.

## 9. Key numbers
- IndoHateMix: 11,725 total, 4,457 (38.01%) hate, 7,268 (61.99%) non-hate, avg 22.20 words (p.5, p.7).
- HateXplain 12,375 (43.17% hate); ImplicitHate 21,480 (38.12% hate) (p.5).
- Fleiss' Kappa 0.685 (p.7).
- LLaMA3.1-8B accuracy: HateXplain 0.91, ImplicitHate 0.82, IndoHateMix 0.83 (p.10).
- mBERT: HateXplain 0.87, ImplicitHate 0.76, IndoHateMix 0.73 (p.10).
- GPT-4o-mini (zero-shot, not fine-tuned): 0.72 / 0.70 / 0.76 accuracy (p.10).
- Transfer-learning gain of LLaMA3.1-8B over mBERT averaged 12.15% when trained on HateXplain (p.11).
- LoRA rank-8 ≈ 4M trainable params vs mBERT 179M (p.11).

## 10. Pitfalls & limitations
- Author-admitted: single platform (Koo) with intrinsic bias; only Hindi-English; classification-only bias analysis; no CoT/advanced prompting; single A100 constrains model scale (p.14-15).
- GPT-4o-mini run zero-shot while open LLMs fine-tuned — unfair comparison (authors acknowledge, p.11).
- XLM-RoBERTa IndoHateMix F1 = 0.33 with accuracy 0.74 signals a degenerate/collapsed classifier, undermining that row (p.10).
- Two illustrative code-mixed examples in text are missing/blanked in the extract (p.6).
- Binary relabeling merges offensive vs hate (HateXplain excludes "offensive"; ImplicitHate merges implicit+explicit).

## 11. Novel ideas worth stealing
- **Code-mixed + transliterated benchmark construction** from a regional platform (Koo) — a template for building non-WEIRD, culturally-grounded values datasets where English detectors fail.
- **Target-of-hate taxonomy contrast across datasets** (community-directed vs individual/political-leader-directed; religious vs racial vs political) — a reusable lens for characterizing *what a dataset actually measures* rather than just its label balance.
- **Low-resource stress test**: fine-tune on 10% with a 4M-param LoRA adapter and still beat full-data specialist models — a cheap way to probe whether a benchmark rewards data diversity over model specialization.
- **Cross-dataset transfer heatmaps** to measure generalization vs overfitting to one corpus's idiosyncrasies.
- **Conservative-prompt policy** (deliberately simple prompt as a lower bound) so any measured LLM advantage is a floor, not a tuned ceiling.
- Reframing the research question: "curate richer datasets vs. build specialized models" — a design-space prior for values benchmarking.

## 12. Notable quotes
- "recent large language models (LLMs) not only surpass them but also redefine the landscape of hate speech detection more broadly" (p.1).
- "LLaMA-3.1, even when fine-tuned on just 10% of the available data, outperform fine-tuned BERT-based models trained on the full dataset" (p.2).
- "it may be more effective to invest in powerful, general-purpose LLMs trained on diverse, culturally grounded datasets to combat online hate more reliably" (p.14).
- "hate speech in India is as much about blaming individuals in authority as it is about targeting religious or caste groups" (p.7).

## 13. UNKNOWN / not in extract
- Exact numeric contents of the transfer-learning heatmaps (Figures 1-2) — only textual summaries given.
- The two blanked code-mixed example posts on p.6.
- IndoHateMix licensing / public-release terms.
- Full Table 3 error-analysis example set.
- Annotator demographics / guidelines detail.
