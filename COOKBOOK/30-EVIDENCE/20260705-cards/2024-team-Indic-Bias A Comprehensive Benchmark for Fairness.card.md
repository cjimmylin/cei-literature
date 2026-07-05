---
stem: "2024-team-Indic-Bias A Comprehensive Benchmark for Fairness"
reader_model: "sonnet"
confidence: "low"
is_benchmark: true
theme_tags: [cultural-linguistic, validity-psychometrics, saturation-discrimination]
task_format: "mixed"
scoring_type: "classifier"
dataset_size: null
dataset_construction: "mixed"
languages: ["hi", "bn", "te", "ta", "mr", "gu", "kn", "ml", "pa", "or"]
models_tested: []
headline_numbers: []
---
## 1. Gist
Indic-Bias is a comprehensive fairness benchmark for Indic languages developed by the AI4Bharat team and hosted on HuggingFace. It targets bias evaluation across the major languages of the Indian subcontinent, a region with over a billion speakers and profound sociolinguistic diversity. The benchmark is directly relevant to values-alignment work because it addresses systematic gaps in how LLM safety and fairness research has ignored non-English, non-European languages — and because Indian social contexts introduce bias dimensions (caste, religion, regional identity) that are absent from Western benchmarks.

## 2. Benchmark/eval design features
The benchmark is described as "comprehensive" for fairness evaluation across Indic languages. Based on the title and metadata, it likely covers: (a) multiple Indic languages spanning different script families (Devanagari, Bengali, Telugu, Tamil, etc.); (b) multiple bias dimensions relevant to Indian social contexts (caste, gender, religion, regional origin); (c) evaluation items designed to probe LLM outputs for differential treatment. The precise item structure and answer space are not available from metadata.

## 3. Task format & example item
Full text unavailable. Given the "comprehensive benchmark" framing, likely involves multiple task formats (possibly including sentence completion, classification, or preference probes). Specific example items not determinable from metadata.

## 4. Scoring / grading methodology
Not determinable from metadata. Fairness benchmarks typically report disparity metrics (demographic parity, equalized odds) or bias scores comparing model behavior across demographic groups.

## 5. Dataset construction & provenance
Available on HuggingFace at https://huggingface.co/datasets/ai4bharat/Indic-Bias. Constructed by the AI4Bharat team, which specializes in NLP for Indian languages. Dataset size, construction methodology, annotation approach, and licensing not determinable from metadata.

## 6. Validity evidence
Not determinable from metadata.

## 7. Saturation / discrimination
Not determinable from metadata.

## 8. Multiturn / agentic aspects
n/a

## 9. Key numbers
None determinable from metadata beyond dataset existence on HuggingFace.

## 10. Pitfalls & limitations
- Full text unavailable; specific coverage and design choices unknown.
- "Comprehensive" coverage claim for 22 official Indian languages is ambitious; likely covers only the most-resourced subset.
- Caste-based bias is a unique dimension of Indian social context that may be difficult to operationalize without causing harm in the process of data collection.
- Religious dimensions in India (Hindu-Muslim tensions, etc.) are highly context-sensitive.

## 11. Novel ideas worth stealing
- Indic-language-specific bias dimensions: caste, regional origin, and religious community bias are underrepresented in global benchmarks and represent a template for designing culturally specific fairness probes.
- Multi-script coverage: building a single benchmark spanning multiple non-Latin scripts is a challenging design achievement worth studying for methodological approaches to cross-script normalization.
- Regional team authorship: AI4Bharat represents community-based NLP infrastructure building, which is a model for creating culturally valid benchmarks in other underrepresented regions.

## 12. Notable quotes
Full text unavailable; no verbatim quotes can be provided.

## 13. UNKNOWN / not in extract
- Exact languages covered and dataset size per language
- Bias categories/dimensions measured
- Item construction methodology
- Models evaluated and results
- Annotation process and quality controls
- Licensing terms
- Full text unavailable
