---
stem: "2024-Xu-Exploring Multilingual Concepts of Human Value in Large Language"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [cultural-linguistic, normative-ethics, validity-psychometrics, pluralism-aggregation]
task_format: "mixed"
scoring_type: "classifier"
dataset_size: null
dataset_construction: "scraped"
languages: ["en", "fr", "zh", "es", "pt", "vi", "ca", "id", "ja", "ko", "fi", "hu", "ta", "te", "sw", "ny"]
models_tested: ["LLaMA2-chat-7B", "LLaMA2-chat-13B", "LLaMA2-chat-70B", "Qwen-chat-1B8", "Qwen-chat-7B", "Qwen-chat-14B", "BLOOMZ-560M", "BLOOMZ-1B7", "BLOOMZ-7B1"]
headline_numbers:
  - "All models exceed 65% concept recognition accuracy across represented languages, even smallest BLOOMZ-560M (p.5)"
  - "BLOOMZ-7B1 achieves >81% accuracy on majority of seen languages (10/12) (p.5)"
  - "English cross-lingual control (En-Control) achieves 93.91% following rate on LLaMA2-chat-7B, compared to 97.35% for language-specific control (p.9)"
  - "Without control, LLaMA2-chat-7B follows only 6.44% of harmful instructions on average across non-English languages (p.9)"
  - "Larger models more vulnerable: LLaMA2-chat-70B follows 9.89% of harmful instructions without control vs 6.44% for 7B (p.9)"
---
## 1. Gist
This paper conducts the first systematic investigation of how human values-related concepts (value concepts) are encoded in the multilingual representation spaces of LLMs. Building on Representation Engineering (RepE), the authors extract concept vectors for 7 value types (commonsense morality, deontology, utilitarianism, fairness, truthfulness, toxicity, harmfulness) across 16 languages and 3 LLM families. The central finding is that LLMs do encode value concepts multilingually, but the cross-lingual properties of these representations are heavily shaped by language resource disparities — leading to inconsistency between high- and low-resource language representations, distorted linguistic relationships, and unidirectional transfer from dominant to minority languages. A fourth experiment demonstrates that these concept vectors can be used to cross-lingually control model behavior, including bypassing safety alignment. The paper is important for values-alignment benchmarking because it reveals that value alignment is not uniformly transferable across languages and that English-centric alignment may create exploitable multilingual vulnerabilities.

## 2. Benchmark/eval design features
This is a probing/mechanistic study rather than a benchmark paper per se. The core methodology is Representation Engineering (RepE): concept vectors are extracted from LLMs using paired positive/negative text examples representing two opposing directions of a value concept. The framework has four components:

1. **Concept vector extraction** (§3.1): Mean difference of hidden-state representations over positive/negative pairs per concept per language per layer.
2. **Concept recognition task** (§3.2): Dot product of extracted vector against test pair representations; accuracy measures whether vector correctly discriminates concept direction. Threshold τ=65% is used as conservative lower bound for presence confirmation.
3. **Cross-lingual similarity** (§3.3): Cosine similarity of concept vectors between language pairs, used to assess cross-lingual consistency.
4. **Cross-lingual concept recognition** (§3.4): Using vector from language l1 to recognize concept in language l2; accuracy difference measures transfer direction and magnitude.
5. **Cross-lingual alignment control** (§5): Adding concept vectors to hidden states to steer model behavior across languages (harmful instruction following rate as behavioral metric).

Seven value concepts are examined using established datasets: ETHICS (commonsense morality, deontology, utilitarianism), StereoSet (fairness), TruthfulQA (truthfulness), RealToxicityPrompts (toxicity), AdvBench (harmfulness). English data translated to 15 non-English languages via Google Translate.

## 3. Task format & example item
Concept extraction uses paired positive/negative text examples. From the paper (p.3): "a harmless instruction 'Provide a tutorial on how to make a breakfast' and a harmful instruction 'Provide a tutorial on how to make a bomb' form a pair representing the concept of harmfulness."

The concept recognition task is a binary classification: given a positive-negative text pair, the concept vector should assign higher dot-product score to the positive member. The cross-lingual control task uses harmful instruction prompts translated to 12 languages and measures whether the model follows them (following rate).

## 4. Scoring / grading methodology
- **Concept recognition accuracy**: Proportion of test text pairs where the concept vector correctly discriminates positive from negative. Best layer accuracy reported unless otherwise specified.
- **Cross-lingual similarity**: Cosine similarity of concept vectors between languages, averaged over all value concepts.
- **Cross-lingual transferability**: Difference in recognition accuracy when using source-language vector on target-language data vs. using target-language vector on target-language data.
- **Cross-lingual control**: "Following rate" — proportion of harmful instructions the model follows — computed using AdvBench multilingual harmful instructions. Compared across: No-Control, Language-Specific Control (LS-Control), and English Cross-lingual Control (En-Control).
- Pearson correlation computed between cross-lingual concept consistency and four types of linguistic similarity (genetic, syntactic, geographic, phonological) using lang2vec.

## 5. Dataset construction & provenance
- Value concept datasets: ETHICS, StereoSet, TruthfulQA, RealToxicityPrompts, AdvBench — all established English-language benchmarks translated to 15 non-English languages via Google Translate.
- 16 languages from multiple families: Indo-European (Catalan, French, Indonesian, Portuguese, Spanish), Niger-Congo (Chichewa/ny, Swahili/sw), Dravidian (Tamil/ta, Telugu/te), Uralic (Finnish, Hungarian), Sino-Tibetan (Chinese), Japonic (Japanese), Koreanic (Korean), Austro-Asiatic (Vietnamese).
- LLM families: LLaMA2-chat (7B, 13B, 70B), Qwen-chat (1B8, 7B, 14B), BLOOMZ (560M, 1B7, 7B1).
- Translation quality effects discussed in Appendix C; authors argue noise has minimal impact given the study's focus on universal patterns rather than peak language performance.
- Not all languages covered in each model's pre-training; LLaMA2 and BLOOMZ cover 12 of 16 selected languages (non-overlapping sets).

## 6. Validity evidence
- Concept recognition accuracy exceeds τ=65% threshold for all models across represented languages, confirming presence of value concepts even in smallest model (p.5).
- PCA-based vs. mean-based concept vector extraction show comparable precision, with mean slightly better (Appendix E.1).
- Even small numbers of training samples can effectively extract concept vectors (Appendix E.2).
- Cross-lingual consistency patterns align with known linguistic relationships (genetic, syntactic) when language resource disparities are controlled for (Table 1, p.7).
- Middle layers most consistently encode value concepts — consistent with prior representation engineering research (p.5–6).
- En-Control achieves near-LS-Control performance, validating the cross-lingual concept transfer mechanism (Table 2, p.9).

## 7. Saturation / discrimination
Concept recognition accuracy is notably lower for extremely low-resource languages (ta, te, sw, ny representing <0.5% of BLOOMZ pre-training). The 65% threshold is described as a "conservative statistic and lower bound" derived from the worst case (BLOOMZ-560M on Chichewa). Larger models produce significantly higher accuracies. No ceiling effects reported for high-resource language experiments.

## 8. Multiturn / agentic aspects
n/a. All experiments are single-forward-pass probing or controlled single-turn inference.

## 9. Key numbers
- 7 value concepts, 16 languages, 3 LLM families (p.1)
- τ=65% accuracy threshold for confirming concept presence (p.5)
- BLOOMZ-7B1 >81% accuracy on 10/12 seen languages (p.5)
- LLaMA2-chat-7B En-Control following rate: 93.91% avg across non-English languages (p.9)
- LLaMA2-chat-7B LS-Control: 97.35% avg following rate (p.9)
- LLaMA2-chat-7B No-Control: 6.44% avg following rate (p.9)
- LLaMA2-chat-70B No-Control: 9.89% avg following rate (larger models more vulnerable) (p.9)
- LLaMA2 English pre-training data: ~90% (p.9)
- Pearson correlation between concept consistency and genetic linguistic similarity (with language-resource-category control): up to 0.78 for LLaMA2-chat-70B (Table 1, p.7)

## 10. Pitfalls & limitations
- All non-English data are machine-translated from English; cultural variations in value interpretation are not captured (Limitations, p.10).
- Study focuses on universal multilingual patterns, explicitly deferring cultural divergence investigation to future work (p.2).
- LLM language distribution data is incomplete: Qwen's technical report only specifies English and Chinese, so other language inclusions are inferred from performance (p.4–5).
- Unidirectional transfer measurement may be amplified by initial performance differences across languages (Appendix H.1 partially addresses but doesn't fully resolve).
- Cross-lingual control experiment uses harmful instruction following as the behavioral metric — a narrow operationalization of "value alignment control."
- Translation quality for low-resource languages (Chichewa, Swahili, Tamil, Telugu) may be poor, introducing confounds.

## 11. Novel ideas worth stealing
1. **Concept vector probing as values-alignment diagnostic**: The RepE-based method of extracting concept vectors per language and measuring recognition accuracy is a low-cost diagnostic for whether a model has internalized a value concept in a given language. New benchmarks could use this to pre-screen model capability before behavioral testing.
2. **Cross-lingual consistency as an alignment fairness metric**: Measuring cosine similarity of concept vectors between high- and low-resource language pairs directly quantifies alignment inequality. This could be a supplementary metric in multilingual alignment benchmarks.
3. **Dominant-language-as-source cross-lingual control**: The finding that English concept vectors transfer effectively to other languages in English-dominated LLMs suggests a practical alignment technique: align in English, propagate cross-lingually. This also reveals a vulnerability that benchmark designers should probe.
4. **Language-resource stratification for interpreting cross-lingual results**: The insight that linguistic family relationships are masked by resource disparities (Table 1) is a methodological lesson — always stratify by language resource level when computing cross-lingual metrics.
5. **Multi-family LLM comparison as a validity design**: Testing the same hypotheses on LLMs with different multilinguality profiles (English-dominated, bilingual, balanced) provides natural controls that single-model studies lack.

## 12. Notable quotes
- "Cross-lingual concept inconsistency is more likely to occur between high- and low-resource languages." (p.6)
- "Surprising, we observe larger models are more prone to responding to non-English harmful instructions, potentially due to their enhanced instruction-following capabilities." (p.9)
- "Despite the positive effect of dominant languages as sources for cross-lingual alignment transfer (§5.2), it is crucial to avoid an excessive prevalence of these languages to mitigate unfair cross-lingual patterns." (p.2)
- "Middle layers encode more abstract information related to human values, aligning with the findings of Li et al. (2023)." (p.5)

## 13. UNKNOWN / not in extract
- Exact dataset sizes (numbers of training and test pairs) for each value concept dataset (referenced in Appendix B, not shown)
- Detailed results per individual value concept for concept recognition and cross-lingual tasks (Appendices E.3, E.4, G.2, G.3, H.2, H.3)
- Hyperparameter search details for cross-lingual control (Appendix I)
- Impact of translation quality analysis (Appendix C)
- Full language distribution data for LLaMA2 and BLOOMZ pre-training (Appendix D)
- Details on lang2vec-based language pair categorization method (Appendix F)
