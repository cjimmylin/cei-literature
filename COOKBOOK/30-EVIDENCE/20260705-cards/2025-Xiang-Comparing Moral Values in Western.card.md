---
stem: "2025-Xiang-Comparing Moral Values in Western"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [moral-psychology, cultural-linguistic, validity-psychometrics, contamination-robustness]
task_format: "n/a"
scoring_type: "n/a"
dataset_size: 12000
dataset_construction: "LLM-generated"
languages: ["en"]
models_tested: ["Llama-3.1-8B-Instruct"]
headline_numbers:
  - "GMN-H (human) and GMN-L (Llama) show comparable overall Spearman correlation with eMFD: 0.28 vs 0.29 (p.6)"
  - "Largest cross-graph divergence in sanctity and authority dimensions (p.6)"
  - "Human associations: 66% emotional responses vs. Llama 55%; humans more concrete across all dimensions (p.8)"
  - "Llama optimal temperature: 2.1, yielding ~80% precision at top-10 moral cues relative to human data (p.5)"
  - "GMN-L weighted degree centrality 2x higher than GMN-H for abstract dimensions (loyalty, authority) (p.9)"
---
## 1. Gist
This paper (arXiv May 2025, University of Melbourne) proposes a novel indirect method to compare the moral values encoded in LLMs with those of western English-speaking humans. Instead of asking LLMs moral questions directly (which is brittle and contamination-prone), the authors use word association tests — a well-established psychological paradigm — to extract LLM "mental lexicons" and then propagate moral information through these association graphs using a random-walk algorithm. The key finding is that LLMs broadly mirror human moral associations for positive moral concepts, but diverge systematically for negative ones: LLM associations are more abstract and emotionally sterile, while human associations are more sensory, emotional, and experience-grounded. This has implications for values-alignment benchmarking because it shows that surface-level alignment in moral questionnaires may mask deeper structural misalignment in how LLMs represent moral concepts.

## 2. Benchmark/eval design features
This is a methodology and measurement paper, not a benchmark deployment. Core claims:
1. Word association tests are more robust measures of LLM moral values than direct moral questionnaires because they probe implicit conceptual organization rather than surface pattern-matching.
2. A global graph propagation algorithm (random walk) outperforms local subgraph methods (Moral Association Graph, MAG) for predicting moral concept scores.
3. LLMs and English-speaking humans align more closely for virtue concepts than vice concepts.
4. LLMs produce more abstract, less emotionally grounded associations for morally charged words, particularly in the sanctity dimension.

The evaluation framework has two phases: (1) collecting word association graphs from humans (WA-H: Small World of Words, 90k participants, 12k cues) and from Llama (WA-L: same 12k cues, 100 responses each at temperature=2.1); (2) propagating moral values from 626 MFT seed words through each graph to produce Global Moral Networks (GMN-H, GMN-L). Alignment is then measured against the extended Moral Foundations Dictionary (eMFD).

## 3. Task format & example item
Word association task: "Given the cue word [cue], generate up to three associated words." Administered to Llama with the same instructions used in the human WA-H data collection (Appendix A). Not a moral questionnaire format. Example: cue "abortion" → human responses: "pregnancy, choice, right, baby, death, sad..."; Llama responses differ. (p.2, Figure 1)

## 4. Scoring / grading methodology
Moral values propagated via: F_{t+1} = αSF_t + (1−α)F_0, where S is the normalized adjacency matrix, F_0 contains MFD seed moral scores {-1, 0, +1}, and α controls propagation depth. Optimal α=0.75 for GMN-H, 0.90 for GMN-L. Final moral scores compared to eMFD (continuous moral scores) via Spearman correlation, evaluated on 2,186 overlapping concepts. Emotionality measured using VAD-norms arousal scores; concreteness using Brysbaert et al. (2014) lexicon.

## 5. Dataset construction & provenance
**Human data (WA-H)**: English Small World of Words (De Deyne et al., 2019), 90k native English speakers (50% US, plus UK, Canada, Australia), 12k cues, up to 3 responses per participant per cue. Publicly available.
**LLM data (WA-L)**: Llama-3.1-8B-Instruct queried 100 times for each of 12k cues (1.2M total requests), temperature=2.1, using same instructions as WA-H. Code and data released at GitHub.
**Moral seed words**: Intersection of MFD 2.0 (2,041 words) with 12k cues = 626 seed words.
**Evaluation set**: Intersection of eMFD (3,270 words) with 12k cues = 2,186 words.

## 6. Validity evidence
The global propagation (GMN) outperforms the previous state-of-the-art local approach (MAG) on Spearman correlation with eMFD across all five dimensions (Table 1): MAG All=0.20 vs. GMN-H=0.28 vs. GMN-L=0.29. Split-half reliability of WA-L assessed via Spearman-Brown formula (Appendix B). Temperature calibrated on 400-cue subset. Robustness of propagation to alpha variation reported in Appendix D. Statistical significance: all reported correlations p ≤ 0.01 (p.6).

## 7. Saturation / discrimination
WA-L precision vs. WA-H degrades as k increases: near-perfect at k=1 (most frequent response), declining to ~80% at k=10 (p.5). Largest human-LLM divergence in sanctity and authority moral dimensions. Care shows smallest divergence. The abstract dimensions (loyalty, authority) show 2x higher weighted degree centrality in GMN-L vs. GMN-H, suggesting LLM over-represents abstract moral connections while under-representing sensory/emotional ones.

## 8. Multiturn / agentic aspects
n/a — single-turn word association queries only.

## 9. Key numbers
- 12,000 cue words in both WA-H and WA-L (p.3)
- 90,000 human participants in WA-H (p.3)
- 626 MFD seed words after intersection with cues (p.4)
- 2,186 eMFD words used for evaluation (p.4)
- GMN-L optimal temperature: 2.1 (p.5)
- Overall Spearman correlation with eMFD: MAG=0.20, GMN-H=0.28, GMN-L=0.29 (p.6)
- Care correlation: MAG=0.29, GMN-H=0.47, GMN-L=0.46 (p.6)
- Authority correlation: MAG=0.21, GMN-H=0.19, GMN-L=0.25 (p.6)
- Human emotional response rate: 66%; Llama: 55% across all dimensions (p.8)
- Human concrete response rate: 42%; Llama: 36% (p.8)

## 10. Pitfalls & limitations
- **Single LLM tested**: only Llama-3.1-8B-Instruct; results may not generalize to larger or differently trained models (p.10).
- **Western cultural specificity**: both WA-H and Llama's training data are predominantly Western Anglo-centric; findings cannot be generalized to other cultural contexts (p.10).
- **Concept-level only**: the framework measures word-level moral scores; it cannot directly assess morality in sentences, documents, or behavioral contexts (p.10).
- **Training data contamination risk**: LLMs trained on text containing the MFD/eMFD itself could exhibit spurious alignment; the paper partially addresses this by avoiding direct moral prompting, but the underlying word co-occurrence statistics in Llama's training may still encode questionnaire patterns.
- **Temperature selection**: using temperature=2.1 is unusual and may produce qualitatively different responses than typical deployment settings (temperature 0–1).
- **Correlation metric**: Spearman correlation with eMFD is itself a human-generated crowdsourced dictionary with its own coverage gaps.

## 11. Novel ideas worth stealing
- **Indirect moral probing via word associations**: instead of asking LLMs "is X ethical?", elicit free word associations for morally loaded cues. This is contamination-resistant and captures implicit conceptual organization. Directly applicable to values-alignment benchmarks as a validity check against direct-prompting results.
- **Global moral network propagation**: seed a word association graph with a few hundred ground-truth moral anchor words and propagate scores globally. This enables moral scoring of any vocabulary item without explicit labeling. Can be used to pre-compute moral "neighborhoods" for scenario generation.
- **Emotionality and concreteness as LLM calibration metrics**: measuring the proportion of emotional and concrete associations (using VAD-norms and concreteness lexicons) provides a diagnostic for experiential grounding. LLMs may be systematically miscalibrated on negative/vice moral concepts due to abstract training data.
- **Temperature calibration for association diversity**: the paper's approach of tuning temperature to match human association diversity and reliability is reusable whenever LLM outputs need to approximate human variability distributions.
- **Divergence analysis by moral dimension**: systematically comparing human vs. LLM association topology for each MFT dimension (care, fairness, loyalty, authority, sanctity) can pinpoint which dimensions are most unreliable for benchmark purposes.

## 12. Notable quotes
- "The leakage of moral questionnaires into the LLMs' training data raises questions about the genuineness of their responses." (p.1)
- "An LLM lacking the experiential, affective grounding for negative concepts might misjudge the severity of harm or respond inappropriately in critical situations, even if capable of superficially correct answers to direct queries." (p.9)
- "LLMs and humans align more closely for positive moral values compared to negative ones. Humans show greater emotional diversity and concreteness in their responses, while LLMs are less varied and more abstract." (p.2)
- "GMN-H's top negative concepts often relate to physically or emotionally charged words in the sanctity dimension (e.g., 'disgusting', 'gross'), whereas GMN-L focuses predominantly on social vices in the fairness dimension (e.g., 'betrayal', 'racism')." (p.7)

## 13. UNKNOWN / not in extract
- Results for models other than Llama-3.1-8B
- Cross-cultural replication (non-English word association datasets)
- Whether temperature=2.1 affects semantic coherence of associations beyond diversity
- Appendix B (split-half reliability), D (alpha sensitivity), E–G (detailed subgraph statistics)
- How the framework handles polysemous words with both moral and non-moral senses
