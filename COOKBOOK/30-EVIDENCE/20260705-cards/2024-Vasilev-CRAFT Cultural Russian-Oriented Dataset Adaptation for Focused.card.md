---
stem: "2024-Vasilev-CRAFT Cultural Russian-Oriented Dataset Adaptation for Focused"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [cultural-linguistic, design-space, best-practices]
task_format: "n/a"
scoring_type: "human-rating"
dataset_size: 200000
dataset_construction: "mixed"
languages: ["ru", "en"]
models_tested: ["Kandinsky 3.1", "Kandinsky 2.2", "DALL-E 3", "Midjourney V5.2", "Stable Diffusion XL", "YandexART"]
headline_numbers:
  - "Dataset: ~200,000 text-image pairs with human-written captions across ~8,000 entities in 17 categories (p.6–8)"
  - "Human evaluation on 120 prompts by 12 evaluators; Kandinsky 3.1 outperforms Kandinsky 2.2, Midjourney 5.2, SDXL, YaART; competitive with DALL-E 3 (p.9)"
  - "Finetuning: 500K steps on 416 A100 GPUs; data duplicated 50x for rare entities (p.8)"
---
## 1. Gist
CRAFT (Cultural Russian-Oriented Dataset Adaptation for Focused Text-to-Image Generation) is a methodology and dataset for improving text-to-image generative models' understanding of Russian cultural concepts — collectively called the "cultural code." Popular models like DALL-E 3, Midjourney, and Stable Diffusion XL, trained predominantly on Western-oriented internet data, fail to correctly generate culturally specific Russian entities (e.g., Soviet cartoon characters, traditional cuisine, historical figures in proper context). The paper proposes a systematic pipeline: (1) define 17 cultural categories and enumerate entities; (2) collect and filter images from the web; (3) create detailed human-written captions rather than relying on LLaVA-based auto-captioning (which makes factual errors on culturally specific content); (4) fine-tune Kandinsky 3.1. Human evaluation demonstrates significant improvement. This work is relevant for values-alignment benchmarking because it provides a concrete methodology for how culturally specific knowledge can be operationalized — applied to moral/values benchmarks, the same pipeline could systematically identify and fill cultural blind spots in LLM evaluations.

## 2. Benchmark/eval design features
Not a benchmark paper; it is a dataset + fine-tuning methodology paper. However, the paper does create and use a 120-prompt human evaluation set for measuring cultural awareness in text-to-image models. The evaluation compares models on: (a) text alignment — does the generated image match the prompt's cultural content? (b) visual quality. 12 human evaluators perform pairwise comparisons (side-by-side). The paper acknowledges "there are no benchmarks and automatic metrics for the task of Russian cultural adaptation of text-to-image generation" (p.9), motivating their human-only evaluation. A follow-on benchmark (RusCode) is referenced (p.10, ref [49]).

## 3. Task format & example item
Human side-by-side preference evaluation. Example entity from Table 1 (p.7): "Yuri Gagarin" with web queries including "cosmonaut Gagarin, Gagarin in a helmet with the inscription USSR, Gagarin in an orange spacesuit." The model is prompted to generate an image; human evaluators choose which model's output better represents the cultural entity.

## 4. Scoring / grading methodology
Human preference evaluation: 12 evaluators, 120 prompts reflecting Russian cultural code, pairwise choice between models on text alignment and visual quality. Results shown as preference distributions (Figure 6, p.9). No inter-rater reliability reported; no statistical significance tests mentioned in the extract.

## 5. Dataset construction & provenance
- ~8,000 entities across 17 categories (e.g., famous personalities, literature, art, national cuisine, religious holidays, trees and plants, Soviet/Russian movies/TV, utensils, technology)
- ~200,000 text-image pairs with human-written captions (2–10 sentences each)
- Captions: auto-captioning (LLaVA-NeXT 34B) was tested but rejected due to factual errors on culturally specific content (Table 2, p.7); human captions took ~4.52 min/image vs. 5.23 min for editing synthetic captions
- Quality filtering criteria: aesthetic quality, cultural authenticity, no watermarks, entities not distorted (p.6)
- Data duplication: 50x duplication to balance rare entities
- Fine-tuning: stage 1 at 768×768, stage 2 at mixed 768²–1024² resolution; 500K steps, 416 A100 GPUs (p.8)

## 6. Validity evidence
Human evaluation by 12 evaluators on 120 culturally specific prompts. Results show Kandinsky 3.1 outperforms previous models. LLaVA auto-captioning comparison (Table 2) directly demonstrates the factual failure mode and motivates human captioning — a validation of the methodology choice. The paper acknowledges its evaluation set is relatively small and lacks statistical rigor.

## 7. Saturation / discrimination
Remaining problems identified: (a) entities with very few high-quality training examples (old cartoons, films) remain poorly generated; (b) translation difficulties (e.g., "cosmonaut" → "astronaut" in English, adding American flags) degrade culturally specific generation (Figure 7, p.10). The competitive performance against DALL-E 3 on a Russian cultural test set shows headroom for improvement.

## 8. Multiturn / agentic aspects
n/a

## 9. Key numbers
- 17 cultural categories; ~8,000 entities (p.5)
- ~200,000 text-image pairs with human captions (p.8)
- Average captioning time: human 4.52 min, human-editing-synthetic 5.23 min (p.8)
- Fine-tuning: 500K steps, 416 A100 GPUs, batch size 4 (768²) and 1 (mixed) (p.8)
- Human evaluation: 120 prompts, 12 evaluators (p.9)
- Kandinsky 3.1 wins on text alignment against Kandinsky 2.2, Midjourney 5.2, SDXL, YaART; competitive with DALL-E 3 (p.9)

## 10. Pitfalls & limitations
- Scope limited to Russian/Soviet/post-Soviet cultural code; methodology is general but results are culture-specific.
- Evaluation set (120 prompts, 12 evaluators) is small; no inter-rater reliability or statistical tests reported.
- Human captioning is expensive and may introduce annotator subjectivity/inconsistency.
- 50x data duplication for rare entities is a workaround rather than a solution; generation quality for rare entities remains poor.
- Translation issues (p.10) reveal a systematic pipeline flaw for non-English entities.
- No automatic metrics; entirely dependent on human evaluation which is hard to reproduce.
- The follow-on RusCode benchmark is only referenced, not described in this paper.

## 11. Novel ideas worth stealing
- **17-category cultural taxonomy as a template**: the CRAFT category taxonomy (famous personalities, literature, art, religion, cuisine, geography, cinema, folk traditions, etc.) is a transferable framework for constructing culturally specific benchmark item sets — any culture could be mapped to this template.
- **Entity-level granularity for cultural evaluation**: rather than asking "does the model understand Russian culture" abstractly, evaluating on specific named entities (Yuri Gagarin, specific Soviet cartoons, specific dishes) provides measurable and reproducible ground truth.
- **LLaVA auto-captioning failure as a lesson**: the systematic factual errors in LLaVA's captions on culturally specific content (Table 2) demonstrate that LLM-generated labels for non-Western cultural content cannot be trusted without human validation — a critical warning for benchmark construction using LLM-generated items.
- **Filtering criteria for cultural authenticity**: the explicit rules for accepting/rejecting images based on cultural authenticity (p.6) provide a transferable annotation protocol for any culturally-grounded evaluation dataset.
- **50x duplication to handle rare entity underrepresentation**: a simple but effective data augmentation strategy applicable to benchmark construction when certain cultural subcategories are underrepresented.

## 12. Notable quotes
- "Despite the fact that popular text-to-image generation models cope well with international and general cultural queries, they have a significant knowledge gap regarding individual cultures." (p.1)
- "Erroneous and incorrect generations in this case can lead to, at a minimum, an unsatisfactory result, limited applicability of the model and partial loss of interest among users, and, at a maximum, to unintentional insult, and the spread of stereotypes and social biases." (p.2)
- "We found that training the model on data collected from the Internet according to our entity lists produces unsatisfactory results." (p.5)
- "Since there are no benchmarks and automatic metrics for the task of Russian cultural adaptation of text-to-image generation, we focused on conducting side-by-side human evaluation." (p.9)

## 13. UNKNOWN / not in extract
- RusCode benchmark details (referenced as [49] but not described in this paper).
- Licensing of the collected dataset.
- Inter-rater reliability among the 12 human evaluators.
- Exact distribution of prompts across the 17 categories in the 120-prompt evaluation set.
- Whether the fine-tuned model degrades on non-Russian prompts (cultural forgetting).
