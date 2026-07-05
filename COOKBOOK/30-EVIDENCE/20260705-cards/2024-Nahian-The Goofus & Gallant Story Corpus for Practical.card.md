---
stem: "2024-Nahian-The Goofus & Gallant Story Corpus for Practical"
reader_model: "sonnet"
confidence: "high"
is_benchmark: true
theme_tags: [normative-ethics, moral-psychology, best-practices, design-space]
task_format: "MCQ"
scoring_type: "exact-match"
dataset_size: 1387
dataset_construction: "scraped"
languages: ["en"]
models_tested: ["GPT-4o", "BERT", "DistilBERT", "ViT"]
headline_numbers:
  - "Dual encoder (image+text) achieves 76.77% accuracy on normativity classification (p.6)"
  - "BERT text-only achieves 94.05% accuracy on full GnG text-only normative dataset (p.6)"
  - "GPT-4o annotation agreed with human judgment at 91% for at least one principle in initial review (p.5)"
  - "Fleiss-Kappa of 0.54 for crowdsourced principle annotations, indicating moderate agreement (p.4)"
  - "GnG Normative dataset: 1387 texts, 819 images; GnG Principles dataset: 819 items (p.5)"
---
## 1. Gist
This paper introduces the Goofus & Gallant (GnG) story corpus — a multi-modal dataset drawn from 20+ years of a children's magazine comic strip that contrasts normative and non-normative behavior. Each comic panel pairs a short text description with an image depicting either Goofus (socially unacceptable behavior) or Gallant (socially acceptable behavior). The dataset is augmented with a taxonomy of 27 social principles derived from Kiesel et al.'s 54-value taxonomy, annotated via both crowdworkers and GPT-4o. The paper matters for values-alignment benchmarking because it demonstrates that a small, targeted, expert-curated dataset specifically designed to teach social norms to children can achieve higher-quality training signal than large, noisy web-scraped corpora — and that the labeling of normative vs. non-normative behavior is tractable for current ML models.

## 2. Benchmark/eval design features
Two classification tasks are evaluated: (1) normativity classification — a binary task distinguishing normative from non-normative actions; and (2) principles classification — a multi-class task identifying which of 27 social principles is upheld or violated. The corpus contains an auto-labeled component (Gallant = normative, Goofus = non-normative) and a principles layer added via crowdsourcing and GPT-4o annotation with human verification. Items are short text statements drawn from comic panels (action descriptions), with optional visual context (images). The principles classification uses a relaxed evaluation metric: a prediction is correct if it matches either of two ground-truth principles per item.

## 3. Task format & example item
Text-only normativity classification example:
"Gallant does his studying before watching TV." → Label: normative (p.5)

Principles classification example:
Input: scene description + action description + compliance information (followed/violated) → predict the primary principle from a set of 27, e.g., "be responsible." (p.5-6)

## 4. Scoring / grading methodology
Normativity task: binary exact-match classification evaluated with accuracy, precision, recall, F1, and MCC. Principles task: both strict (predicted == Principle 1) and relaxed (predicted matches either Principle 1 or Principle 2) metrics are reported. Human-LLM agreement for GPT-4o annotations measured as proportion agreeing with at least one predicted principle (91% initial, 93% extended; 61% both principles). (p.5, p.6-7)

## 5. Dataset construction & provenance
Comics from Highlights Magazine (1995–2017) form the base corpus. Text extracted from panels: 1387 text descriptions, 819 images (2001–2017 only, due to image quality). Names "Goofus" and "Gallant" replaced with pronouns to avoid surface-level shortcuts. Principles annotation: (1) crowdsourced — 150 workers annotated 400 items (3 principles each, top-frequency wins); (2) GPT-4o zero-shot with 5 query iterations per item to pick the most frequent prediction for Principle 1 and 2, followed by human verification of 50 initial items and 100 from extended set. Splits: GnG text-only 832/555 train/test; GnG multi-modal 655/164. No explicit contamination controls described. (p.3–5)

## 6. Validity evidence
Fleiss-Kappa = 0.54 for crowdsourced principle annotation (moderate agreement). Human-GPT agreement: 91–93% on at least one principle, 61% on both. Ablation shows multi-modal model (76.77% acc) outperforms both image-only (72.26%) and text-only (72.90%) models, validating the utility of the multi-modal design. Sentiment analysis baseline (62.46%) trails BERT (94.05%), confirming that normativity is not reducible to sentiment. (p.4–6)

## 7. Saturation / discrimination
BERT on the text-only dataset achieves 94.05% accuracy, which is near-ceiling for normativity classification. This reflects the relatively simple binary signal in the corpus. Principles classification shows much lower performance (relaxed F1 ~32–36%), indicating substantial headroom for harder multi-label social value inference. (p.6–7)

## 8. Multiturn / agentic aspects
n/a. All tasks are single-turn classification on static text or image-text pairs.

## 9. Key numbers
- GnG text-only normative: 1387 items (832 train, 555 test) (p.5)
- GnG multi-modal normative: 819 items (655 train, 164 test) (p.5)
- GnG Principles: 819 items (655 train, 164 test) (p.5)
- Dual encoder (image+text): accuracy 76.77%, F1 79.78%, MCC 52.61% (p.6)
- BERT (text-only, full dataset): accuracy 94.05%, F1 94.03%, MCC 88.11% (p.6)
- Sentiment baseline: accuracy 62.46%, F1 58.44% (p.6)
- Principles classification (relaxed, action-only): F1 36.06%, accuracy 74.84% (p.7)
- Fleiss-Kappa for crowdsourced annotation: 0.54 (p.4)
- GPT-4o annotation agreement (at least one principle): 91% initial, 93% extended (p.5)
- 27 social principles used (p.3)
- 150 crowdworkers, 400 instances annotated (p.3-4)

## 10. Pitfalls & limitations
- Small dataset: ~1387 text instances from a monthly comic spanning 22 years; not scalable without more annotation effort.
- Binary normativity label is coarse; real-world moral situations are rarely so cleanly polarized.
- The corpus is Western/US-centric (Highlights Magazine) and targeted at children — cultural and developmental generalizability is uncertain.
- GPT-4o was used for annotation and the same family could be fine-tuned on this corpus, creating evaluation contamination concerns.
- Scene descriptions for the principles task were written by crowdworkers for images, introducing an indirect representation layer.
- Moderate inter-annotator agreement (κ=0.54) on principles suggests the taxonomy may be ambiguous or overlapping.
- The 27-value subset was selected by running a zero-shot model on the corpus, which could introduce circularity.

## 11. Novel ideas worth stealing
- **Automatically labeled contrasting pairs**: The Goofus/Gallant structure provides a natural auto-labeling scheme (one character always bad, one always good) without manual annotation for the base normativity label. A values benchmark designer could harvest similar naturally contrastive materials (e.g., advice columns that distinguish good/bad behavior, ethics textbooks with case studies).
- **Hybrid annotation pipeline**: Use LLM annotation (GPT-4o, 5 query iterations to reduce variance) then verify a sample via humans to calibrate trust. The 91–93% agreement makes this pipeline efficient.
- **Relaxed multi-label evaluation**: Allowing a predicted principle to match either of two valid ground-truth labels is a principled way to handle genuine ambiguity in value classification — reusable in any benchmark with overlapping value categories.
- **Children's educational materials as value training data**: Content deliberately designed to teach social norms is already curated, clear, and culturally accepted — a lower-noise alternative to Reddit/Twitter scraping.
- **Multimodal normativity corpus**: Pairing text with images that visually illustrate the social situation adds a separate test of whether models rely on visual or linguistic cues — relevant for future multimodal values benchmarks.

## 12. Notable quotes
- "While these methods are effective at generating a large amount of data, there are limitations that must be considered. When datasets are curated via web scraping, they are susceptible to biases present in online communities." (p.1)
- "The advantage of Goofus & Gallant comic is that it has both image and text for each strip demonstrating an action in a social scenario." (p.3)
- "The principle that appeared most frequently for a given instance was chosen as the final label, ensuring that the most commonly agreed-upon principle was used." (p.3–4)
- "The experiment shows that the pre-trained sentiment analysis model struggles to detect normative/non-normative behaviors from the texts. It indicates the two tasks are not analogous to one another." (p.7)

## 13. UNKNOWN / not in extract
- License terms for the Goofus & Gallant corpus (Highlights Magazine permission mentioned but no license specified).
- Whether the corpus is publicly released and under what access conditions.
- Full list of the 27 social principles used.
- Details of how crowdworkers were compensated and screened.
- Whether GPT-4o was tested in a held-out evaluation or only used as annotator.
- Inter-rater agreement for human verification step (only binary agree/disagree reported, not kappa).
