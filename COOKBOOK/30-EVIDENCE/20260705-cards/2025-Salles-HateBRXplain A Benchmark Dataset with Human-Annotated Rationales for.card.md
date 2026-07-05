---
stem: "2025-Salles-HateBRXplain A Benchmark Dataset with Human-Annotated Rationales for"
reader_model: "opus"
confidence: "high"
is_benchmark: true
theme_tags: [cultural-linguistic, validity-psychometrics]
task_format: "mixed"
scoring_type: "mixed"
dataset_size: 7000
dataset_construction: "mixed"
languages: [Portuguese]
models_tested: [mBERT, BERTimbau, DistilBERTimbau, PTT5]
headline_numbers: ["BERTimbau best classifier: F1 0.91, AUC 0.97 (p.7)", "Human-annotation rationale agreement: Jaccard 0.6746, F1 0.7168 vs random 0.4855/0.5735 (p.4)", "3,500 offensive comments annotated with rationales, 7,000 total (p.2,p.8)", "PTT5[SHAP] top plausibility: IOU-F1 0.7400, Token-F1 0.7362 (p.8)"]
---
## 1. Gist
HateBRXplain is the first Brazilian-Portuguese hate-speech dataset with human-annotated rationales — text spans that justify the offensive label — built as an explainable extension of the HateBR corpus (7,000 Instagram comments, balanced 3,500 offensive / 3,500 non-offensive). Two annotators marked offending spans for every offensive comment. The authors fine-tune four transformers (mBERT, BERTimbau, DistilBERTimbau, PTT5) and then evaluate post-hoc explanation methods (LIME, SHAP) against the human rationales using ERASER-style plausibility and faithfulness metrics. It matters for values-alignment work as a low-resource-language template for pairing a moral/safety classification label with human-justified evidence spans, and for its finding that the best-performing classifier is not the most faithfully explainable.

## 2. Benchmark/eval design features
Constructs: (1) binary offensive/non-offensive classification; (2) rationale quality — plausibility (alignment with human spans) and faithfulness (whether spans reflect the model's actual decision). Item structure: a comment + binary label + one-or-more human rationale span sets (from two annotators). Answer space for the classifier is binary; the explanation "answer" is a set of important tokens. Inherits HateBR's three-layer annotation (offensive/not, offensiveness level, nine hate-target groups) but rationales added only for offensive class. Plausibility metrics: IOU-F1, token Precision/Recall/F1. Faithfulness metrics: comprehensiveness and sufficiency.

## 3. Task format & example item
Example annotation (p.4, rationale in the offensive span): "Criminal! Scoundrel and racist! May justice be served!" — highlighted spans are the rationale. Model-vs-human comparison example (p.6): "Who cares about what you think, corrupt communist? You should be in jail!" with green tokens marking human+model agreement and orange marking model-only importance.

## 4. Scoring / grading methodology
Classification: accuracy and macro-F1 on an 8:1:1 stratified train:val:test split (p.5). Rationale plausibility: IOU-F1 (a predicted rationale matches a human one if token IOU ≥ 0.5, Eq. 3) and token-level Precision/Recall/F1 (Eq. 4), computed at token level because LIME/SHAP output tokens not spans; the higher-agreement of the two human annotations is taken as ground truth (p.7). Faithfulness: comprehensiveness = drop in class probability when rationale tokens removed (Eq. 5); sufficiency = drop when only rationale tokens kept (Eq. 6, lower is better) (p.7). Inter-annotator agreement measured with span-level Jaccard and F1, partial overlaps (IOU≥0.5) counted as matches (p.4).

## 5. Dataset construction & provenance
Derived from HateBR (Vargas et al. 2022/2024a): 7,000 Instagram comments from Brazilian politicians' accounts, expert-annotated, balanced classes, 75% kappa (p.3). Rationales hand-authored by two independent annotators (Master's/PhD candidates, female, Black and White, from São Paulo and Minas Gerais) instructed to mark smallest spans conveying offensive meaning (p.4). Annotator 1 marked 6,601 spans / 27,038 tokens (avg 7.72 tokens/comment); Annotator 2 marked 5,922 spans / 17,992 tokens (avg 5.14) (p.5). Code and data public on GitHub (p.1). LIME/SHAP explanations generated on a random 350-comment (10%) subset (p.6). Licensing: open-source, anonymized (p.9).

## 6. Validity evidence
Inter-annotator reliability reported: rationale Jaccard 0.6746 and F1 0.7168, both well above random baselines (0.4855 / 0.5735), evidencing non-trivial human agreement (Table 5, p.4). Classification baseline exceeds prior Portuguese datasets (F1 0.91 vs HateBR's 0.85, Table 1, p.3). Human rationale serves as the criterion for plausibility. Faithfulness metrics provide construct separation between "looks like human reasoning" and "is the model's actual reasoning". Annotator profile diversity is an explicit reliability control (p.4).

## 7. Saturation / discrimination
Classification is near-saturated: all four models score 0.87–0.92 macro-F1, a narrow band (Table 9, p.7). Explanation metrics discriminate more: IOU-F1 spans 0.58–0.74, Token-F1 0.67–0.74 (Table 10, p.8); comprehensiveness ranges widely 0.565–0.948, showing substantial headroom and model separation on faithfulness. Key discriminating finding: the best classifier (BERTimbau) is mid-pack on explainability, so classification accuracy has saturated while faithful explanation remains an open, discriminating axis.

## 8. Multiturn / agentic aspects
n/a — static single-comment classification with post-hoc explanation; no interaction, tools, or agents.

## 9. Key numbers
- 7,000 comments; 3,500 offensive + 3,500 non-offensive (p.2, p.8)
- Offensive: 53,455 words, avg 15.27 words/comment; non-offensive: 42,891 words, avg 12.25 (p.5)
- BERTimbau accuracy 0.9157, macro-F1 0.9153, AUC 0.97 (Table 9, p.7)
- mBERT F1 0.8737; DistilBERTimbau 0.8994; PTT5 0.9035 (Table 9, p.7)
- Rationale IAA: Jaccard 0.6746, F1 0.7168 (Table 5, p.4)
- PTT5[SHAP] IOU-F1 0.7400, Token-F1 0.7362 (best plausibility) (Table 10, p.8)
- Best comprehensiveness DistilBERTimbau[SHAP] 0.9475; lowest sufficiency PTT5[LIME] 0.0016 (Table 10, p.8)
- Explanation subset: 350 comments (10%) (p.6)

## 10. Pitfalls & limitations
Author-admitted: inherits HateBR limitations — sourced only from Brazilian politicians' Instagram, so may not generalize to other platforms/domains (p.9); rationale annotation is subjective despite guidelines (p.9). Only two annotators; ground truth uses the higher-agreeing annotation per instance, which can inflate plausibility. LIME/SHAP token counts differ (SHAP returns more tokens, inflating recall-based plausibility, p.7), confounding cross-method comparison. Explanation evaluation on only 10% subset. Models are fine-tuned encoders/T5, not modern generative LLMs, limiting relevance to LLM alignment. Table 3/8 span highlighting lost in the text extract.

## 11. Novel ideas worth stealing
- Pair every moral/safety label with human-authored evidence spans, then score models on BOTH label accuracy AND rationale plausibility/faithfulness — directly portable to values benchmarks where "why" matters as much as "what".
- Use ERASER's faithfulness pair (comprehensiveness + sufficiency) to detect models that get the right answer for the wrong reasons — a saturation escape hatch when accuracy ceilings out.
- Random-rationale baseline (matched span-size distribution) to calibrate whether human agreement is meaningful — a cheap validity control any span-annotation benchmark should adopt.
- Diversified annotator profiles (education, race, region, membership in affected groups) as an explicit representativeness lever for subjective moral judgments (p.4, p.9).
- Extending an existing well-annotated corpus with a new explanatory layer rather than collecting from scratch — efficient low-resource-language benchmark construction.

## 12. Notable quotes
- "the inability of these technologies to provide reasons (rationales) for their decisions is the limiting factor to their adoption since they comprise bias, which may perpetuate social inequalities when propagated at scale." (p.1)
- "while some models excel in classification performance, they cannot always provide faithful rationales for their decisions." (p.2)
- "a rationale is defined as a set of text spans, with each span being the smallest text segment that conveys offensive meaning." (p.4)
- "the annotators selected for this task represent diverse cultural and demographic backgrounds, including members of affected groups, to ensure both fairness and representativeness." (p.9)

## 13. UNKNOWN / not in extract
Full Table 10 faithfulness figures for every model are partially readable but figure-based similarity plots (Figures 1-3) are not numerically in the extract. Exact test-set size (10% of 7,000 = 700) is implied but not stated. No modern LLM (GPT/Llama) is tested. Licensing name/version not specified beyond "open-source". Whether rationales exist for non-offensive comments is confirmed no (only offensive), but exact per-target-group rationale distribution is not given.
