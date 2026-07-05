---
stem: "2025-Fayaz-BIDWESH A Bangla Regional Based Hate Speech Detection Dataset"
reader_model: "opus"
confidence: "high"
is_benchmark: true
theme_tags: [cultural-linguistic, saturation-discrimination]
task_format: "mixed"
scoring_type: "exact-match"
dataset_size: 9183
dataset_construction: "mixed"
languages: [bn]
models_tested: []
headline_numbers: ["9,183 dialectal instances across 3 dialects (p.1)", "3,061 base samples: 1,513 hate / 1,548 non-hate (p.8)", "13 hate-type categories, 7 target categories (p.12)"]
---
## 1. Gist
BIDWESH is presented as the first multi-dialectal Bangla hate speech detection dataset, built by manually translating and annotating a 3,061-sample subset of the BD-SHS corpus into three regional Bangla dialects (Barishal, Noakhali, Chittagong), yielding 9,183 dialectal instances. Each sentence is labeled for hate presence (binary), hate type (slander, gender, religion, callToViolence, including multi-label combinations), and target group (individual, male, female, group). Its relevance to values-alignment benchmarking is as a low-resource, culturally-grounded safety/content-moderation resource that foregrounds dialectal and regional linguistic variation—a dimension usually ignored by standard-language safety benchmarks. It is a dataset/resource paper rather than an LLM evaluation: no models are actually trained or scored on BIDWESH in this extract.

## 2. Benchmark/eval design features
Constructs measured: (1) binary hate vs. non-hate; (2) hate-type taxonomy of 4 primitive types (Slander, Gender, Religion, callToViolence) with observed 13 single- and multi-label combinations; (3) target taxonomy of 4 primitives (Individual, Male, Female, Group) with 7 observed categories. Item structure: parallel corpus—each standard-Bangla source sentence has aligned Barishal, Noakhali, and Chittagong dialectal versions (Table 3, p.11). Answer space for the primary task is binary (1=hate, 0=non-hate); type/target labels apply only to hate instances. Perfect regional balance (33.3% each dialect, p.11) and near-balanced hate/non-hate (49.24%/50.76%, p.11).

## 3. Task format & example item
Classification labels on dialectal sentences. Example from Table 3 (p.11): standard Bangla "grur ba£ca kukuerr ba£ca" (transliterated) with Chittagong/Noakhali/Barishal parallel forms, Target=ind, Type=slander, hate label=1. A second row shows a non-hate sentence with target/type "-" and label 0.

## 4. Scoring / grading methodology
No model scoring performed in this paper. Labels are gold human annotations intended for supervised training/evaluation; downstream use implies exact-match against these categorical labels (binary, multi-label type, target). Related-work models are reported by F1/accuracy but not on BIDWESH itself.

## 5. Dataset construction & provenance
Source: BD-SHS (Romim et al. 2022), the largest public Bangla hate speech corpus (>50,000 comments); a subset of 3,061 samples (1,513 hate / 1,548 non-hate) was selected (p.8). Six native-speaker translators (two per dialect; four male, two female; ages 22–25; students/researchers, all 18+) manually translated into the three dialects (Table 2, p.8), producing 9,183 instances (p.8). Five-stage validation: re-evaluation, unrelated-text removal, sentence verification, emoji removal, data balancing (pp.8–10). Annotation done by the same dialect experts. Licensing: publicly available via Mendeley Data (p.14). Ethics statement notes data is from a public dataset with no private/sensitive info (p.14). No train/test splits are specified in the extract.

## 6. Validity evidence
Validity rests on manual translation and multi-stage review by native speakers; no quantitative inter-annotator agreement, kappa, or reliability statistics are reported. No human baseline or model criterion validity is established (no models are run on the dataset here). Preservation of "semantic integrity and offensive characteristics" is asserted qualitatively (p.8).

## 7. Saturation / discrimination
No model results on BIDWESH, so no ceiling/headroom analysis exists here. Class imbalance in fine-grained labels is severe: type distribution ranges from Slander (822, 53.65%) down to Gender_religion_slander (3, 0.20%) (p.12); target from Individual (520, 34.37%) to Male_group/Female_group (3 each, 0.20%) (p.12), which will make rare-class discrimination hard.

## 8. Multiturn / agentic aspects
n/a — single-sentence classification dataset, no interaction or agentic protocol.

## 9. Key numbers
- 9,183 total dialectal instances across three dialects (p.1, p.8)
- Base subset 3,061 samples: 1,513 hate (49.24%), 1,548 non-hate (50.76%) (p.11)
- Regional split perfectly balanced at 33.3% each (Barishal/Noakhali/Chittagong) (p.11)
- 13 hate-type categories; Slander largest at 822 / 53.65% of hate (p.12)
- 7 target categories; Individual largest at 520 / 34.37% (p.12)
- 6 translators, 2 per dialect, ages 22–25 (Table 2, p.8)
- BD-SHS source: >50,281 comments, 24,156 hate (p.3)

## 10. Pitfalls & limitations
Author-admitted: high risk of inconsistency from subjective translation and lack of standardized dialectal orthography (p.8–9). Observed flaws: no inter-annotator agreement statistics; no baseline model results despite calling itself a "benchmark," so discrimination/validity are unproven; extreme class imbalance in fine-grained type/target labels; only 3,061 unique semantic items (dialects are translations, not independent samples), so effective diversity is limited; annotators and translators are the same people, risking circular validation; transliteration artifacts in the extract complicate verification.

## 11. Novel ideas worth stealing
- Parallel dialectal construction: hold semantic content fixed while varying regional dialect, enabling controlled measurement of a model's robustness to sub-national linguistic variation—directly transferable to building "same value, different vernacular" alignment probes.
- Multi-level layered annotation (presence → type → target) that only applies deeper layers to positive cases, reducing annotation cost while preserving fine granularity.
- Explicit translator-demographic disclosure (region, age, gender, background) as a provenance/representativeness artifact worth emulating for culturally sensitive alignment datasets.
- Dedicated emoji-removal and orthography-normalization stages as documented, auditable pipeline steps for low-resource text.
- Framing regional dialect coverage as a fairness requirement: a values-alignment benchmark could similarly treat sub-language dialect coverage as a first-class equity axis.

## 12. Notable quotes
- "we introduce BIDWESH (Hatred), the first benchmark corpus designed for hate speech detection in Bangla regional dialects." (p.6)
- "if models focus only on standard language, they will miss regional slurs." (p.3)
- "The absence of dialect-aware models results in systematic under-detection of harmful content, particularly when hate speech is deliberately obfuscated through culturally specific language patterns" (p.3)
- "hate speech detection models struggle when applied to data from unfamiliar regions, highlighting the necessity of designing systems that embrace cultural diversity and fairness." (p.5)

## 13. UNKNOWN / not in extract
- No inter-annotator agreement / reliability metrics reported.
- No baseline model performance on BIDWESH (no models tested).
- No train/validation/test split sizes.
- Specific license terms beyond "publicly available for research."
- Exact dialect-level label distributions (only aggregate given).
