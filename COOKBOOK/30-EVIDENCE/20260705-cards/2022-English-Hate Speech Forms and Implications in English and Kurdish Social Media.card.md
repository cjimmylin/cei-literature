---
stem: "2022-English-Hate Speech Forms and Implications in English and Kurdish Social Media"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [cultural-linguistic, normative-ethics]
task_format: "n/a"
scoring_type: "n/a"
dataset_size: 30
dataset_construction: "scraped"
languages: ["en", "ku"]
models_tested: []
headline_numbers:
  - "15 English comments: 11/15 used negative character, 2 disagreement, 1 dehumanization, 1 negative action (p.4)"
  - "15 Kurdish comments: 8 dehumanization/demonization, 5 negative character, 3 disagreement, 1 negative action — total 17 hate speech acts (p.4)"
  - "3 paired political Facebook posts analyzed (G7 summit, Afghan refugee crisis, UK Queen's guard incident) (p.4)"
---
## 1. Gist
Faiq and Noori present a small qualitative study comparing hate speech forms used by English-language and Kurdish-language Facebook commenters on three matched political posts. Using Bahador's (2020) Hate Speech Intensity Scale (6 categories across 3 typologies), the paper finds that English commenters predominantly use "negative character" (name-calling: "fools, idiots, terrorists"), while Kurdish commenters predominantly use "dehumanization and demonization" (calling people "donkeys," "animals," "Satan") — a higher-intensity form on Bahador's scale. For values-alignment benchmarking, this paper is relevant as a cross-cultural, cross-linguistic case study showing that hate speech forms and intensities are not culturally uniform, and provides a concrete typological framework (Bahador's scale) for categorizing harm intensity.

## 2. Benchmark/eval design features
Not a benchmark. This is a qualitative discourse analysis study with a very small sample. The core analytical framework is Bahador's (2020) Hate Speech Intensity Scale:
- **Typology 1 (Early Warning)**: (1) Disagreement, (2) Negative nonviolent actions, (3) Negative character/insults
- **Typology 2 (Dehumanization/Demonization)**: (4) Dehumanization (treating as animals/vermin) or Demonization (treating as superhuman threat/monster)
- **Typology 3 (Incitement)**: (5) Non-lethal violence, (6) Lethal violence/incitement to murder

The study categorizes 15 English and 15 Kurdish Facebook comments (5 per post × 3 posts × 2 languages) using this scale.

## 3. Task format & example item
Manual annotation of Facebook comments into Bahador's 6 categories. Kurdish examples translated to English in appendices (pp.6-8):

Post 1 (G7 summit) Kurdish comments:
- "Satan groups" → Demonization (category 4)
- "Sons of Anti-Christ" → Demonization (category 4)
- "Acting like donkey starts again" → Dehumanization (category 4)
- "All those dirty Satan" → Demonization (category 4)
- "The world's politics is under the control of these stupid" → Negative character (category 3)

Post 3 Kurdish comments:
- "Two donkeys" → Dehumanization
- "donkey is walking" → Dehumanization
- "They are animals" → Dehumanization
- "English stupid donkey" → Dehumanization + Negative character
- "Donkey is a donkey even if you take it to London" → Dehumanization

## 4. Scoring / grading methodology
Qualitative categorization — no quantitative scoring beyond frequency counts. Counts of comments per category per language group reported in the results section (p.4). No inter-rater reliability reported.

## 5. Dataset construction & provenance
Three matched political posts selected from English (Sky News, Fox News, The Raz Man Facebook pages) and Kurdish (Rudaw, Politic Press Facebook pages) on the same topics: G7 summit, Afghan refugee crisis, UK Queen's guard knocking a child. 5 comments per post per language = 15 comments per language = 30 total. Collected from public Facebook pages; no dates specified (p.4).

## 6. Validity evidence
No inter-rater reliability reported. Single-analyst qualitative coding. No validation of the coding scheme beyond citation of Bahador (2020). The extremely small sample (15 comments per language) severely limits generalizability. The paper notes the same comment can be assigned multiple categories (some Kurdish comments include both dehumanization and negative character + disagreement, resulting in 17 hate speech acts across 15 comments) (p.4).

## 7. Saturation / discrimination
Not applicable — this is a qualitative study. The 30-comment sample has no statistical power and cannot support quantitative claims about language-level differences in hate speech intensity.

## 8. Multiturn / agentic aspects
n/a

## 9. Key numbers
- 30 total comments analyzed (15 English, 15 Kurdish) (p.4)
- 3 political posts per language (p.4)
- English: 11/15 negative character, 2/15 disagreement, 1/15 dehumanization, 1/15 negative action (p.4)
- Kurdish: 8 dehumanization/demonization, 5 negative character, 3 disagreement, 1 negative action = 17 acts in 15 comments (p.4)
- Dehumanization found in Kurdish: 8 instances; in English: 1 instance (p.4-5)

## 10. Pitfalls & limitations
- Extremely small sample (n=30): no statistical validity for any cross-cultural claims
- No inter-rater reliability: one analyst applying one coding scheme
- Posts selected from different media outlets (Fox News vs. Rudaw) — confounds platform/audience differences with language/culture differences
- Translation of Kurdish comments into English by the authors — translation validity not addressed
- No control for post topic within language comparisons
- The Bahador scale itself is not empirically validated (cited as a single SSRC blog post, 2020)
- Kurdish is a language family with multiple dialects; which Kurdish variety not specified
- Study published in Journal of University of Human Development — limited peer review rigor

## 11. Novel ideas worth stealing
1. **Bahador's 6-category intensity scale**: A typological framework organizing hate speech from early-warning (disagreement) through dehumanization to incitement-to-kill provides a fine-grained alternative to binary hate/not-hate annotation. For values benchmarks, this scale could operationalize graduated harm severity in a cross-culturally motivated way.
2. **Matched cross-language post design**: Selecting matched political posts (same topics, same time period) in two languages and comparing comment patterns is a clean quasi-experimental design for isolating linguistic/cultural factors in values expression. Could be adapted for larger-scale multilingual values evaluation.
3. **Dehumanization as a distinct category**: The finding that Kurdish commenters prefer dehumanization (animal metaphors: donkey, Satan) while English commenters prefer name-calling (idiot, terrorist) illustrates that the *form* of harm expression varies cross-culturally even when intensity is similar. Benchmarks should measure form variety, not just intensity level.

## 12. Notable quotes
- "The majority of the English commentators used negative character, while the majority of the Kurdish commentators used Dehumanization and Demonization, in which it was only found in one comment on the English posts." (p.1, abstract)
- "Dehumanization is the act of treating people like pigs, rats, monkeys, or even trash or diseases." (p.3)
- "On the other side, demonization is the representation of a group as superhuman, such as a monster, robot, or even fatal diseases like cancer, which pose a serious threat to the in-group." (p.3)
- "Hate speech incites abuse, degrades society and often leads to social punishment." (p.2)

## 13. UNKNOWN / not in extract
- The actual English comments (the appendix images are not OCR-readable in the extract, pp.6-8)
- Dates of data collection
- Which specific Kurdish dialect the posts are in
- Whether the authors are native speakers of both languages
- Statistical significance of any cross-language difference claims
- Bahador (2020) scale's original validation methodology
