---
stem: "2025-Prasannan-Counter-Speech Generation for Homophobic and Transphobic"
reader_model: "sonnet"
confidence: "high"
is_benchmark: true
theme_tags: [cultural-linguistic, best-practices, llm-judges-scoring]
task_format: "generative"
scoring_type: "mixed"
dataset_size: 5100
dataset_construction: "mixed"
languages: ["ml"]
models_tested: ["ChatGPT-4o", "Gemini 2.0", "KunoRZN-Llama-3-3B", "XLM-RoBERTa", "mT5", "LaBSE"]
headline_numbers: ["5100 hate-counter speech pairs in Malayalam (p.1)", "HITL V5 imbalance degree 0.294 vs. one-shot 0.831 (p.17)", "HITL V5 CS repetition rate 13.61 vs. one-shot 1.000 (p.17)", "RAG chatbot stance confidence 0.99999 (p.18)", "RAG chatbot fluency PPL 1.78 (p.18)", "RAG chatbot toxicity 0.031 (p.18)", "Welch t-test for CS length increase V2 to V5: t=9.72, p<0.00001 (p.13)"]
---
## 1. Gist
This paper presents the first Malayalam counter-speech dataset targeting homophobic and transphobic hate speech, comprising 5,100 hate–counter speech pairs built via a human-in-the-loop (HITL) iterative pipeline using ChatGPT-4o. It then proposes a RAG (Retrieval-Augmented Generation) framework enhanced by REFINE (Retrieval Evaluation via Fluency, Inversion, and NEarness) filtering to generate contextually appropriate, stance-opposing, non-toxic counter-speech for novel inputs. The paper matters for values-alignment benchmarking because it: (1) demonstrates a replicable methodology for building inclusive, pluralism-sensitive datasets in low-resource languages; (2) shows that one-shot LLM generation without human oversight produces severely degraded diversity (repetition rate 100%); and (3) establishes a multi-metric evaluation framework for the hard problem of generating counter-values responses aligned with specific ethical commitments (dignity, LGBTQIA+ inclusion).

## 2. Benchmark/eval design features
Semi-benchmark: the dataset and evaluation framework are designed for generative counter-speech quality, not model ranking on fixed items.
- **Constructs measured**: dataset quality (diversity, balance, fluency) and chatbot performance (relevance, novelty, stance, toxicity).
- **Item structure**: hate speech input (homophobic or transphobic, in Malayalam script or Latin script) → counter-speech response.
- **Answer space**: free-text Malayalam counter-speech.
- **Key evaluation metrics for dataset quality**: Imbalance Degree, Acceptance Rate (untouched/modified), HTER, Repetition Rate, Novelty (Jaccard), Vocabulary Size/Growth.
- **Key evaluation metrics for chatbot**: Relevance (semantic alignment), Novelty (lexical originality), Stance (must be COUNTER), Stance Confidence, Fluency (PPL via mT5), Toxicity (classifier score).

## 3. Task format & example item
The task is counter-speech generation. A sample interaction shown in Fig. 1 (p.1) and Fig. 17 (p.18):

Input (hate speech in Malayalam, translated): Homophobic statement targeting LGBTQIA+ identity.
Bot output: Calm, empathetic, factually grounded counter-narrative affirming dignity and constitutional rights.

The HITL-generated response example (p.17): "delivers a direct and principled rebuttal rooted in constitutional values. It upholds individual dignity and strongly counters the hateful premise." — contrasted with one-shot response: "vague and moralistic, offering no factual contradiction… merely appeals to generic ideas of peace and diversity."

Annotation guidelines required: Empathy First, Direct Relevance, Script Consistency (Malayalam vs. Latin), Non-aggression, Tone and Cultural Sensitivity, Clarity, Inclusiveness, Ambiguity Resolution, Ethical Compliance.

## 4. Scoring / grading methodology
**Dataset quality metrics** (applied per version V2–V5):
- Imbalance Degree (class distribution skew; ideal <1.0)
- Acceptance Rate untouched (2–6% typical) and modified (30–50%)
- HTER (0.30–0.45 moderate edit effort; lower is better)
- Repetition Rate H/T and CS (lower is better; <60 standard)
- Novelty vs. V1, cumulative, Vi-1 (Jaccard dissimilarity; ≥0.7 desired)
- Vocabulary Size and Growth

**RAG chatbot metrics**:
- Relevance: cosine similarity (LaBSE embeddings)
- Novelty: lexical originality
- Stance: XLM-RoBERTa classifier → COUNTER / other
- Stance Confidence: probability score
- Fluency: mT5 perplexity (lower = better)
- Toxicity: classifier (value <0.2 = non-toxic)

Statistical testing: Welch's t-tests for instance-level metric comparisons (e.g., t=9.72, p<0.00001 for CS length V2 to V5).

## 5. Dataset construction & provenance
- **Seed**: 100 manually matched hate-counter speech pairs from Kumaresan et al. (2023) dataset sourced from social media.
- **Annotation**: Two voluntary native Malayalam speakers (LGBTQIA+ advocacy experience) matched counter-speech; reviewed by two additional native speakers.
- **Expansion**: HITL with ChatGPT-4o iteratively: V2 (+500→600), V3 (+500→1100), V4 (+500→1600), V5 (+3500→5100). Duration: 2 months.
- **Validation per iteration**: Two native speaker reviewers assessed naturalness, clarity, thematic consistency; second layer by two more reviewers.
- **Gemini 2.0 tested but rejected** due to template-like phrasing, poor cultural sensitivity, incomplete outputs, verbatim repetition.
- **Final dataset**: 5,100 unique hate-counter speech pairs (HITL V5: all 5,100 unique; one-shot: only 228 unique hate, 159 unique CS).
- **GitHub**: https://github.com/Bharathi-AI-for-Social-Good/CN-Malayalam
- Language: Malayalam (native script and Latin/Roman script — dual-script challenge).

## 6. Validity evidence
- HITL V5 significantly outperforms one-shot on all metrics (Table 5, p.17).
- Welch's t-test confirms significantly longer, more elaborative CS outputs in V5 vs. V2 (t=9.72, p<0.00001).
- Sentiment polarity analysis confirms H/T content skews negative, CS content skews positive (Fig. 13).
- Character length distributions confirm CS is more deliberate and longer than H/T (Fig. 12, 15).
- RAG chatbot achieves stance confidence 0.99999 and toxicity 0.031 — strong on safety properties.
- Moderate relevance (0.535) and novelty (0.443) acknowledged as limitations for low-resource language setting.

## 7. Saturation / discrimination
- One-shot generation shows complete saturation/failure: repetition rate 1.000, novelty 0.000, HTER 1.357.
- HITL V5 achieves imbalance degree 0.294 (well below 1.5 threshold), repetition rate 13.61 (well below 60), novelty H/T 0.799, CS 0.837.
- Vocabulary expansion: V5 adds 3,533 new tokens; CS vocab grows from 1,674 to 5,207 tokens.
- Homophobic content significantly outnumbers transphobic (~3,000 vs. ~2,000 instances), reflecting real distribution but creating class imbalance that persists across versions.

## 8. Multiturn / agentic aspects
The paper proposes deploying the dataset as a chatbot interface (Fig. 17, p.18). However, the primary evaluation is single-turn (hate speech → counter-speech). The DIALOCONAN precedent (multi-turn dialogue between hater and NGO operator) is cited as a future direction. Current system is effectively single-turn RAG.

Romanized Malayalam (Latin script) poses a cross-script retrieval challenge: "semantically similar phrases like 'entha cheyya' and 'entha cheyyendathu' not being matched" (p.18) and "hybrid syntax examples... being misclassified."

## 9. Key numbers
- Seed dataset: 100 pairs (p.5)
- Final HITL dataset: 5,100 unique pairs (p.6)
- One-shot: 5,100 pairs but only 228 unique hate, 159 unique CS (p.10)
- HITL V5 imbalance degree: 0.294 (vs. one-shot 0.831) (p.17)
- HITL V5 repetition rate CS: 13.61% (vs. one-shot 100%) (p.17)
- HITL V5 novelty CS vs. V1: 0.837 (p.17)
- Vocabulary V5 CS: 5,207 tokens; new tokens V5: 3,533 (p.17)
- Welch t-test CS length V2→V5: t=9.72, p<0.00001 (p.13)
- RAG stance confidence: 0.99999; toxicity: 0.031; fluency PPL: 1.78 (p.18)
- RAG relevance: 0.535; novelty: 0.443 (p.18)
- Homophobic instances ~3,000; transphobic ~2,000 in dataset (p.9)

## 10. Pitfalls & limitations
- Romanized Malayalam retrieval and stance classification degrades significantly due to non-standardized transliteration.
- Moderate relevance (0.535) — chatbot is "on-topic but not deeply contextualized."
- Low novelty (0.443) — outputs tend toward safe, repetitive structures.
- English-derived evaluation metrics may underestimate novelty in agglutinative languages.
- Annotators are volunteers, not professional ethicists; training on homophobia/transphobia was provided but depth unclear.
- Dataset covers only Malayalam; limited generalizability to other Dravidian languages without adaptation.
- No real-world deployment or longitudinal effectiveness evaluation.

## 11. Novel ideas worth stealing
- **REFINE filter for stance-aware retrieval**: The Inversion-Nearness-Fluency triple filter is a reusable component for any benchmark requiring that retrieved examples oppose a given stance. Directly applicable to adversarial values-alignment evaluation.
- **Multi-metric dataset quality framework**: The 12-metric dashboard (imbalance, acceptance, HTER, repetition, novelty, vocabulary) provides a complete template for assessing LLM-generated alignment datasets — applicable to any human values domain, not just counter-speech.
- **HITL vs. one-shot as a benchmark validation methodology**: Comparing HITL to one-shot LLM generation (showing 100% repetition in one-shot) is a powerful quality signal. Any values-alignment dataset should run this comparison before deployment.
- **Dual-script challenge as a test of model robustness**: Evaluating counter-speech generation in both native script and informal romanized script captures real-world code-switching behavior relevant to multilingual values benchmarks.
- **Toxicity as an alignment property**: Using a low toxicity score (0.031) as a model evaluation metric alongside stance accuracy is a direct values-alignment evaluation approach.
- **Cultural sensitivity as annotation criterion**: The explicit annotation guideline "Tone and Cultural Sensitivity: maintain tone acceptable in Malayalam-speaking community, avoiding religious or political triggers" is a reusable annotation criterion for culturally grounded values benchmarks.

## 12. Notable quotes
- "Crafting effective counter speech requires linguistic sensitivity, cultural awareness, and strategic communication skills qualities that are hard to embed in automated systems without appropriate training data and feedback mechanisms." (p.3)
- "HITL-generated response delivers a direct and principled rebuttal rooted in constitutional values. It upholds individual dignity and strongly counters the hateful premise." (p.17)
- "These issues underscore the limitations of relying solely on static large language models for counter-speech generation and reinforce the need for human-in-the-loop (HITL) refinement to ensure diversity, contextual accuracy, and cultural relevance." (p.8)
- "Evaluation metrics developed for English, may underestimate novelty in agglutinative languages like Malayalam where small suffix or phrasing changes signal important meaning shifts." (p.18)

## 13. UNKNOWN / not in extract
- Inter-annotator agreement scores between the four voluntary reviewers.
- Full text of annotation guidelines provided to annotators beyond the summarised bullets.
- Whether the dataset distinguishes derogation-type vs. threatening-type within hate speech categories for counter-speech strategy differentiation.
- Specific demographic information about annotators (age, gender, LGBTQIA+ identity status).
- License terms for dataset distribution.
