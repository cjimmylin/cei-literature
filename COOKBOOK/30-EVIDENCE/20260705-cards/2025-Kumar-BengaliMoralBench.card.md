---
stem: "2025-Kumar-BengaliMoralBench"
reader_model: "opus"
confidence: "high"
is_benchmark: true
theme_tags: [cultural-linguistic, normative-ethics, contamination-robustness, validity-psychometrics]
task_format: "forced-choice"
scoring_type: "exact-match"
dataset_size: 3000
dataset_construction: "hand-authored"
languages: [bn, en]
models_tested: ["Gemma 3 (1B)", "Gemma 2 (2B)", "Gemma 2 (9B)", "Llama 3.2 (1B)", "Llama 3.2 (3B)", "Llama 3.1 (8B)", "Llama 3.3 (70B)", "Qwen2.5 (14B)", "DeepSeek-R1-Distill-Llama (70B)"]
headline_numbers: ["3,000 hand-authored Bengali moral scenarios (p.5)", "Zero-shot accuracy spans 50-91% across models (p.3)", "Gemma 2 (9B) 91.20% Commonsense acc, MCC 0.8242 (p.4)", "Inter-annotator agreement improved κ=0.61 → κ=0.87 after calibration (p.5)", "94 items (3.1%) removed in adjudication (p.6)"]
---
## 1. Gist
BengaliMoralBench is the first large-scale, culturally grounded ethics benchmark for the Bengali language (285M+ speakers), built entirely from scratch by native annotators to audit whether multilingual LLMs' moral reasoning aligns with Bangladeshi socio-cultural norms rather than Western-centric defaults. It contains 3,000 single-sentence scenarios, each labeled ethical/unethical, organized under three culturally adapted ethical lenses (Virtue, Commonsense, Justice) and spanning 5 life domains × 50 subtopics rooted in everyday Bangladeshi life (load-shedding etiquette, rickshaw fare disputes, zakat vs voluntary charity, dowry, hijab in labs). It matters for values-alignment benchmarking as a template for non-Western, contamination-resistant, hand-authored moral evaluation with proper psychometric rigor (dual metrics, IAA, temperature-variance, prompt-language ablations), and it empirically documents cultural blind spots: models score 50-91% with Justice consistently the hardest lens.

## 2. Benchmark/eval design features
Construct: binary moral classification (ethical=1 / unethical=0) of single-sentence behaviors, stratified by three ethical frameworks and five domains (Daily Activities, Habits, Parenting, Family Relationships, Religious Activities), 10 subtopics each = 50 subtopics; 20 instances/subtopic (10 ethical + 10 unethical) → 3,000 (Figure 1, p.2). Triadic framework (p.4): Virtue (character traits — satyata, daya, shraddha), Commonsense (samajik gyan — social-intuitive norms), Justice (nyay, samata, adhikar — fairness/rights). Answer space: binary label. Balanced by label and topic; 52% of items marked "country-specific" (distinctly Bangladeshi) (p.6). Lexical neutrality enforced (no explicit moral cues) to prevent shortcut solving.

## 3. Task format & example item
Forced-choice binary classification: given a Bengali scenario, model outputs Ethical or Unethical under the specified ethics type (Figure 2, p.3). Full verbatim item text not reproduced in extract (examples shown in Figure 1 as paired Bengali-English ethical/unethical scenarios). Item spec (p.6): 12-25 words / under 140 characters, lexically neutral, culturally grounded. Example subtopics/dilemmas cited: "load-shedding etiquette, rickshaw fare disputes, and zakat vs voluntary charity" (p.4).

## 4. Scoring / grading methodology
Exact-match against native-consensus gold labels using four classification metrics: Accuracy (%), F1 (×100), Matthews Correlation Coefficient (MCC), and Cohen's Kappa (p.6-7). MCC/κ emphasized to expose class-imbalance sensitivity and chance-adjusted agreement. Unified zero-shot prompting protocol in both Bengali and English, one prompt tailored per ethical lens (p.6). Human ceiling = 100%, random baseline = 50% (Table 1, p.4).

## 5. Dataset construction & provenance
Built from scratch to avoid train-test leakage in web-scraped data (p.5). 30 native Bengali speakers recruited under strict proficiency/residency/cultural-familiarity criteria. Pilot: annotators generated & cross-reviewed 500 statements, surfacing disagreements (unethical vs merely socially undesirable; lexical leakage), resolved via workshops; IAA rose κ=0.61→0.87 (p.5). Each annotator assigned 5 subtopics within one ethics framework, writing 10 ethical + 10 unethical statements per subtopic (100/annotator, 1,000/framework, 3,000 pre-QC) (p.6). Two-stage QC: Stage 1 peer review; Stage 2 senior adjudication sampling 20%, removing 94 ambiguous items (3.1%) (p.6). Final 3,000 evenly split across the three lenses; mean 18.4 words / 103 chars; 52% country-specific (p.6). Released on HuggingFace (ciol-research/BengaliMoralBench) + GitHub (p.1).

## 6. Validity evidence
Content validity via native-speaker consensus and focus-group subtopic selection (nine annotators, rural+urban) (p.5). Reliability: inter-annotator κ=0.87 post-calibration (p.5). Human baseline = 100% accuracy (Table 1, p.4). Convergent signal: culturally coherent difficulty patterns (Justice hardest; Daily/Religious most country-specific) (p.6, p.8). Temperature-variance study (3 runs, temps 0.3/0.7) demonstrates measurement stability for top models (std dev <0.5) (Table 2, p.5). Prompt-language ablation isolates language-alignment effects (Table 3, p.5).

## 7. Saturation / discrimination
Strong discrimination and clear headroom. Zero-shot accuracy spans 50-91% (p.3). Best: Gemma 2 (9B) 91.20% Commonsense / 89.70% Virtue; Qwen2.5 (14B) best on Justice (86.29%). Weakest: Llama 3.2 (1B) near chance (49.70-51.30%, negative MCC on Justice) (Table 1, p.4). Justice is the hardest lens across models (lower MCC/κ), attributed to fairness-sensitivity and label skew (p.8). Scaling helps but is non-monotonic and family/task dependent (DeepSeek-R1-70B underperforms at 53.99% Justice) (p.8-9), giving good spread across model tiers.

## 8. Multiturn / agentic aspects
n/a. Single-turn zero-shot classification; no tools, no multi-turn interaction.

## 9. Key numbers
- 3,000 instances, evenly split across Justice/Virtue/Commonsense (p.5-6).
- 5 domains × 10 subtopics = 50; 20 instances/subtopic (p.2, p.6).
- 30 annotators; pilot 500 statements; IAA κ=0.61→0.87 (p.5).
- 94 items (3.1%) removed in adjudication (p.6); mean 18.4 words, 103 chars; 52% country-specific (p.6).
- Gemma 2 (9B): Commonsense 91.20% acc / MCC 0.8242; Virtue 89.70% / 0.7947; Justice 80.36% / 0.6513 (Table 1, p.4).
- Qwen2.5 (14B): Justice 86.29% acc, F1 86.15, MCC 0.7391 (Table 1, p.4).
- Llama 3.2 (1B): Justice 49.70% acc, MCC −0.0366 (Table 1, p.4).
- Bengali prompts: Gemma 3 (1B) +8.6 F1 on Virtue; Gemma 2 (2B) −11.97 F1 on Justice (p.9).

## 10. Pitfalls & limitations
Reviewer-observed: binary ethical/unethical labels compress genuine moral pluralism into a two-way call, and "human = 100%" ceiling implies items were selected for consensus, possibly excluding genuinely contested dilemmas (reducing ecological validity of hard moral disagreement). Single-sentence, 140-char format limits scenario richness. 52% country-specific means ~48% may be globally shared (less discriminative for cultural grounding). Benchmark not yet public at submission ("upon acceptance," p.6) — reproducibility deferred. Prompt-language effects are inconsistent across model sizes, complicating fair comparison. No author "Limitations" section captured in the extract pages read.

## 11. Novel ideas worth stealing
- **From-scratch native authorship as a contamination control**: explicitly building items to avoid web-scrape train-test leakage, with lexical-neutrality constraints to block shortcut solving (p.5-6) — directly reusable for contamination-robust value benchmarks.
- **Culturally-adapted triadic ethics lenses** (Virtue/Commonsense/Justice with indigenous vocabulary satyata/samajik gyan/nyay) as an alternative to Western MFT taxonomies (p.4).
- **Country-specific vs globally-shared item tagging** (52% CS) enabling analysis of *where* cultural grounding specifically matters (p.6).
- **Psychometric package as standard**: report MCC + Cohen's κ alongside accuracy/F1 to expose class-imbalance and shallow agreement, plus a temperature-variance table (±std over 3 runs) as a reliability check (Tables 1-2, p.4-5).
- **Prompt-language ablation** (native Bengali vs English prompts) revealing that prompt engineering cannot substitute for culturally representative pretraining (p.9).
- **Calibration pilot with documented IAA jump** (0.61→0.87) as a template for annotator alignment on contested moral categories (p.5).
- **Domain × ethics-lens matrix** to localize failures (e.g., Justice dips in relationally complex Family domain) (p.8).

## 12. Notable quotes
- "Existing ethics benchmarks are largely English-centric and shaped by Western frameworks, overlooking cultural nuances critical for real-world deployment." (p.1)
- "Performance varies widely (50-91% accuracy), with qualitative analysis revealing consistent weaknesses in cultural grounding, commonsense reasoning, and moral fairness." (p.1)
- "translation alone cannot ensure cultural or ethical alignment, emphasizing the need for benchmarks rooted in cultural context." (p.2)
- "parameter count is beneficial but insufficient: Bangla pretraining coverage, instruction tuning quality, and alignment choices materially affect ethical reasoning." (p.9)

## 13. UNKNOWN / not in extract
Verbatim Bengali/English example items, exact prompt text (Appendix F), full domain-wise tables beyond partial Table 4, licensing terms, whether the benchmark was public at time of extract, and an explicit author-written limitations section.
