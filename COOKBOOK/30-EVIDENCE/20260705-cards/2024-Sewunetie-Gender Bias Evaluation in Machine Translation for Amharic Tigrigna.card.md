---
stem: "2024-Sewunetie-Gender Bias Evaluation in Machine Translation for Amharic Tigrigna"
reader_model: "opus"
confidence: "high"
is_benchmark: true
theme_tags: [cultural-linguistic, best-practices, validity-psychometrics]
task_format: "free-text"
scoring_type: "human-rating"
dataset_size: 2400
dataset_construction: "mixed"
languages: [en, am, ti, om]
models_tested: [Google Translate, NLLB]
headline_numbers: ["2400 gender-balanced English sentences translated into 3 languages = 7200 pairs (p.5)", "92.96% Afaan Oromoo, 80.96% Tigrinya, 72.50% Amharic translations show gender bias (p.8)", "108 unique professional names collected (p.5)", "Eng-Amh Google MT SacreBleu 16.13 vs NLLB 3.48 (p.7)"]
---
## 1. Gist
This paper constructs the Gold Gender Bias Test Dataset (GGBTD), a benchmark for evaluating occupational gender bias in machine translation into three low-resource Ethiopian languages: Amharic (Semitic, grammatical gender), Tigrinya (Semitic, grammatical gender), and Afaan Oromoo (Cushitic, minimal grammatical gender). 2,400 gender-balanced English sentences pairing pronouns with 108 professions are translated by human experts, then Google Translate outputs are human-annotated for gender bias. It matters for values-alignment benchmarking as a template for community-rooted, native-speaker-authored fairness benchmarks in low-resource, morphologically rich languages — a setting where automatic bias metrics fail and Anglo-centric benchmarks do not transfer.

## 2. Benchmark/eval design features
Construct measured: representational harm via occupational gender stereotyping in MT (defaulting professions to masculine forms). Uses the Blodgett et al. (2020) bias taxonomy, focusing on representational harms from stereotyping (p.2). Item structure: each item is an English sentence pairing a pronoun (he/his/him or she/her) with an occupation, gender-balanced so every masculine sentence has a feminine counterpart (p.4). 1,200 masculine + 1,200 feminine per language pair (p.6). Answer space: the MT output translation, judged Yes/No biased by human annotators. Also runs automatic translation-quality evaluation (SacreBleu, Chrf++) on NLLB and Google MT as a complementary axis (p.6-7).

## 3. Task format & example item
Verbatim illustrative example (p.3-4): English "The nurse helped the doctor" -> Google Translate Amharic "ነርሷ ሐኪሙን ረድታለች።" (nerswa hakimun redtalech), where the nurse is rendered female and the doctor male by default. The paper enumerates 8 valid gendered Amharic translations of this single sentence (p.4), demonstrating the multiplicity of correct gendered forms that a biased system collapses. Test items pair each of 108 professions with masculine and feminine pronoun sentences (Figure 3, p.5).

## 4. Scoring / grading methodology
Human evaluation only for bias (automatic metrics only for translation quality). Each sentence evaluated by 3 annotators across 3 groups/phases; the Potato annotation tool takes the majority vote to label a sentence biased or not (p.6). Annotators judge two factors: whether translated gender matches source gender, and whether professional terms carry the correct gender (p.9-10, guideline). Each evaluator assessed 400 sentences (p.10). Translation quality scored automatically with SacreBleu and Chrf++ (higher = better) (p.7).

## 5. Dataset construction & provenance
Mixed construction. English source: SimpleGEN (n=130) + winomt (n=192) + crowd-sourced (n=2078) = 2,400 sentences (p.5). 108 professions drawn from the Ethiopian Civil Service Commission job-title list plus GPT-3.5 queries for recent tech professions (p.5). Ten paid freelancers built gender-balanced pairs. Translation: 18 paid linguistic experts (6 per language pair), 600 pairs each, plus 2 professional linguist editors per pair for QC (p.5). Total 7,200 sentence pairs (2,400 x 3 languages). Publicly released under CC-BY-ND on HuggingFace (EthioNLP/Gender-Bias-Evaluation-Dataset) (p.1). Only Google Translate was human-evaluated for bias due to cost (p.6).

## 6. Validity evidence
Reliability: triple annotation with majority vote per sentence controls subjectivity (p.6). Native-speaker experts + professional-linguist QC support content validity for morphologically rich target languages. Gender balance (1,200/1,200) is a design control against label imbalance (p.6). No inter-rater agreement statistic (e.g., kappa) is reported. Automatic quality metrics (SacreBleu/Chrf++) are standard and cross-comparable (p.6-7) but the authors note they capture only overall accuracy, not bias.

## 7. Saturation / discrimination
Strong discrimination across languages: bias rates span 72.50% (Amharic) to 92.96% (Afaan Oromoo), far from ceiling/floor and revealing large cross-language spread (p.6, p.8). Translation-quality scores also separate systems clearly (Google MT >> NLLB on Eng->target; e.g., Eng-Amh SacreBleu 16.13 vs 3.48) (p.7). Bias is pervasive (all languages majority-biased), so as a discrimination benchmark for future improvement there is ample headroom.

## 8. Multiturn / agentic aspects
n/a — single-sentence translation task, no interaction, tools, or multiturn protocol.

## 9. Key numbers
- 2,400 gender-balanced English sentences; 7,200 total pairs across 3 languages (p.5)
- 1,200 masculine + 1,200 feminine per language pair (p.6)
- 108 unique professional names (p.5); English sources SimpleGEN n=130, winomt n=192, crowd n=2078 (p.5)
- Bias observed: Afaan Oromoo 92.96%, Tigrinya 80.96%, Amharic 72.50% (p.6, p.8)
- Table 1 sentence-translation issues: Amharic 1429, Tigrinya 936, Afaan Oromoo 918 (p.7)
- Profession-translation issues: Afaan Oromoo 612, Tigrinya 475, Amharic 258 (p.7)
- Automatic (SacreBleu / Chrf++): Eng-Amh NLLB 3.48/23.73, Google 16.13/47.97; Eng-Orm NLLB 4.85/34.85, Google 22.96/56.71; Eng-Tir NLLB 3.89/18.52, Google 16.00/38.00 (p.7)
- 18 translators + 18 evaluators; 3 annotators per sentence, 400 sentences each (p.5, p.6, p.10)

## 10. Pitfalls & limitations
Author-admitted: (1) limited to 3 language pairs due to cost/time (p.8); (2) focuses only on unbalanced professional names, ignoring other bias sources like unbalanced pronouns and language-gender nature (p.8); (3) only Google Translate bias-evaluated, not NLLB, due to cost (p.6). Visible flaws: binary gender system assumed (men/women only, explicitly noted p.2-3); no inter-rater reliability statistic reported; bias "perception" survey conflates respondent perception with ground-truth bias in some framing (Table 1 headers mix "perception" and "issue" language); Afaan Oromoo lacks grammatical gender yet shows the highest bias rate, suggesting the annotation may capture translation errors beyond pure gender bias.

## 11. Novel ideas worth stealing
- **Community-rooted, native-speaker-authored benchmark construction** with layered QC (translators + separate professional-linguist editors) — a reusable protocol for building values/fairness benchmarks in any low-resource or culturally specific setting where scraped data and automatic metrics are inadequate.
- **Enumerate the full space of valid gendered outputs** for a single ambiguous sentence (the 8-way Amharic example, p.4) as ground-truth reference — captures that "correct" is a set, not a single string, a design move directly reusable for pluralism/ambiguity-aware alignment benchmarks.
- **Strict gender-balancing by construction** (every masculine item has a feminine twin) so bias is measured as asymmetry, not absolute error (p.4, p.6).
- **Pair a domain job-title registry (Civil Service list) with LLM-generated recent professions** (GPT-3.5) to build a culturally grounded yet up-to-date item pool (p.5).
- **Triple-annotate + majority vote via a browsable/mobile annotation tool (Potato)** as a low-cost, reproducible human-rating pipeline (p.6).
- **Contrast open-source (NLLB) vs. commercial (Google) systems** on the same benchmark to expose that publicly available models struggle most on English-as-source into low-resource languages (p.7).

## 12. Notable quotes
- "we found that about 93% of Afaan Oromoo, 80% of Tigrinya, and 72% of Amharic sentences exhibited gender bias." (p.1)
- "Machine Translation services often default to masculine forms for professions like 'doctor' and 'nurse'... potentially reflecting and reinforcing gender stereotypes." (p.1)
- "Such contexts require community-rooted efforts that thoroughly investigate how the culture and language are structured." (p.3)
- "for low-resource languages, publicly available MT models like NLLB are struggling to predict the correct translation when using English as the source language." (p.7-8)

## 13. UNKNOWN / not in extract
- Inter-rater reliability / agreement coefficients (not reported).
- Exact per-profession bias breakdowns (only aggregate rates given).
- The precise wording of the perception-survey question distinct from the annotation task.
- Whether the "perception" percentages (Table 1 discussion) come from the annotators or a separate respondent survey — framing is ambiguous in the extract.
- NLLB bias-annotation results (only quality metrics reported for NLLB).
