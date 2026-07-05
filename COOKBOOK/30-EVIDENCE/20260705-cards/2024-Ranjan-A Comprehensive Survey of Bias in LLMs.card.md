---
stem: "2024-Ranjan-A Comprehensive Survey of Bias in LLMs"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [normative-ethics, cultural-linguistic, ai-lab-practices, validity-psychometrics]
task_format: "n/a"
scoring_type: "n/a"
dataset_size: null
dataset_construction: "n/a"
languages: ["en"]
models_tested: ["GPT-3", "GPT-4", "LLaMA 2", "Tulu", "NousHermes", "LLaMA 3"]
headline_numbers:
  - "20.29% to 44.93% of LLM-generated code functions exhibit bias in sensitive tasks (p.9)"
  - "One-shot and few-shot learning removed up to 90% of bias in GPT-4 code generation (p.9)"
  - "SCD (Social Contact Debiasing) reduced biases in LLaMA 2 by up to 40% after one epoch of tuning (p.9)"
  - "SCD dataset created 108,000 entries measuring 13 types of social bias across 3 models (p.9)"
---
## 1. Gist
This survey by Ranjan, Gupta, and Singh (Carnegie Mellon University / BIT Sindri, 2024) provides a comprehensive taxonomy and synthesis of biases in Large Language Models, covering types, sources, social impacts, and mitigation strategies. The survey systematically categorizes bias along multiple dimensions — demographic (gender, race, age, socioeconomic), contextual (domain-specific, cultural), and structural (data, algorithmic, systemic) — and reviews recent empirical work on bias detection and debiasing techniques. It concludes by identifying key research gaps: lack of standardized intersectional metrics, Western-centric and English-centric focus, opacity of model training pipelines, and absence of scalable post-training mitigation. For values-alignment benchmarking this survey is useful as a structured taxonomy of bias types that doubles as a checklist of normative concerns to evaluate in benchmark items, and as a synthesis of empirical debiasing results that inform what mitigation approaches actually work.

## 2. Benchmark/eval design features
This is a survey paper; it does not present a new benchmark. Core claims and taxonomy:

**Bias type taxonomy (Table 1):**
- Application-specific: Task Bias
- Cognitive: Confirmation Bias
- Data-Driven: Data Bias, Content Bias, Label Bias
- Model Architecture: Algorithmic Bias
- Social: Gender Bias, Racial Bias, Age Bias
- Societal: Social Bias, Cultural Bias
- Systemic: Feedback Loop Bias

**Source taxonomy (Table 2):**
Training Data, Model Architecture, Human Annotation, User Interactions, Societal Influences, Prompt Design, Evaluation Metrics, Cultural Context, Selection Bias.

**Key reviewed debiasing techniques:**
- Prompt engineering and fine-tuning for political bias (Lin et al. 2024)
- "Deceiving to Enlighten" — multi-role debate loop with impartial referee (Cheng et al. 2024)
- BiasAlert — external human knowledge + LLM reasoning for social bias detection
- Few-shot / one-shot learning removing up to 90% of code generation bias in GPT-4
- Social Contact Debiasing (SCD) — 108,000-entry dataset, reduces LLaMA 2 bias by 40% in one epoch
- PoliTune — PEFT for targeted ideological alignment of Llama3-70B
- LangBiTe — automated bias testing platform using developer-defined ethical requirements
- Chain-of-Thought prompting — reduces social bias in arithmetic/symbolic reasoning tasks

**Composite metric reviewed:** LLM Bias Index (LLMBI) — multi-dimensional composite scoring system for age, gender, racial biases.

## 3. Task format & example item
n/a — survey paper; no original task items. Reviewed tasks include analogy completion (word embeddings), text generation continuation, fill-in-the-blank probing, and code generation analysis.

## 4. Scoring / grading methodology
n/a — synthesizes others' methodologies. Common metrics reviewed: disparity metrics (false positive/negative rates by demographic group), statistical parity, equalized odds, equal opportunity, LLMBI composite scores.

## 5. Dataset construction & provenance
n/a — survey, no original dataset. SCD dataset created by Raj et al. (2024) with 108,000 entries measuring 13 types of social bias (noted as significant).

## 6. Validity evidence
n/a — synthesizes existing empirical findings. Notes that BiasAlert outperforms GPT-4-as-A-Judge on social bias detection (p.9), providing implicit criterion validity for a particular detection approach.

## 7. Saturation / discrimination
n/a — no new evaluation. Notes that existing bias metrics are often isolated (gender or race separately) and fail to capture intersectional biases (p.11), implying current benchmarks have discriminability gaps.

## 8. Multiturn / agentic aspects
n/a — the survey does not specifically address multiturn or agentic settings. Notes that feedback loop bias (user interactions reinforcing model biases) is a systemic bias type, which implicates deployment-time dynamics.

## 9. Key numbers
- 20.29%–44.93% of LLM-generated code functions exhibit bias in sensitive tasks (p.9)
- One-shot/few-shot learning removed up to 90% of bias in GPT-4 code generation (p.9)
- SCD reduced LLaMA 2 biases by up to 40% after one epoch of tuning (p.9)
- SCD dataset: 108,000 entries, 13 bias types, 3 models (p.9)
- Gradient-based prompts (AutoPrompt, OptiPrompt) inflate benchmark accuracy by overfitting to imbalanced datasets — representation-based approach gave up to 10% absolute performance gain on prompt retrieval (p.10)

## 10. Pitfalls & limitations
- **Limited depth per topic:** As a survey, individual claims are briefly summarized from cited papers rather than critically verified; some statistics (e.g., 90% bias removal) are taken at face value.
- **Coverage biases of the survey itself:** The survey skews toward English-language and Western-context papers — the gap it identifies in LLM research (Western-centric, English-centric) arguably applies to its own selection.
- **No meta-analysis:** Results across different mitigation papers are not standardized onto a common scale; it is impossible to compare the relative effectiveness of techniques.
- **Rapidly outdated:** The survey is from 2024 and the field is moving extremely fast; several cited "state-of-the-art" models (GPT-3, early LLaMA variants) are already superseded.
- **Lacks operationalization of "fairness":** Multiple fairness definitions are noted as in tension (demographic parity vs. equal opportunity vs. individual fairness) but the survey does not resolve these tensions or recommend a preferred framework.

## 11. Novel ideas worth stealing
1. **Bias taxonomy as benchmark item checklist:** The 12-type bias taxonomy (Table 1) plus 9-source taxonomy (Table 2) can serve directly as a systematic coverage checklist for values-alignment benchmark design — ensuring items test across all bias categories rather than only the most obvious ones (gender, race).

2. **Prompt bias as benchmark contamination type:** The "prompt bias" finding — where AutoPrompt-style gradient-based prompts inflate accuracy by overfitting to imbalanced datasets — is directly relevant to benchmark contamination. Benchmark designers should test whether their prompts systematically advantage certain response patterns independent of actual model values.

3. **Intersectional bias as discriminability target:** The identified gap in intersectional metrics (race × gender × socioeconomic) points to a dimension where new benchmarks could add value — testing model behavior at the intersection of multiple protected attributes rather than each independently.

4. **Lifecycle bias tracking:** The proposal for "comprehensive lifecycle bias evaluation" (pre-training → fine-tuning → deployment → feedback loops) suggests benchmark suites should include multiple test points rather than only static post-training evaluations.

5. **Social Contact Hypothesis for debiasing:** The SCD approach — generating synthetic social interactions via prompts to simulate contact between groups — could be adapted as a data augmentation strategy for creating balanced values-annotation training sets.

## 12. Notable quotes
- "Bias in AI models can lead to harmful consequences, such as reinforcing stereotypes, perpetuating existing inequalities, and impacting marginalized communities disproportionately." (p.3)
- "Current bias research is heavily skewed towards high-resource languages and Western-centric cultural contexts, with limited focus on low-resource languages and non-Western cultures." (p.11)
- "Existing bias mitigation techniques are often focused on pre-training solutions (e.g., data curation), but these approaches are computationally expensive and lack scalability." (p.12)
- "There is a lack of comprehensive, standardized metrics that can evaluate multiple intersecting biases, such as those involving race, gender, and socio-economic status simultaneously." (p.11)

## 13. UNKNOWN / not in extract
- Specific models tested and results for each bias type (results are from cited papers, not this paper's own experiments).
- Whether any novel empirical contributions were made beyond synthesis (seems to be purely a survey based on the extract).
- Publication venue / peer review status.
- Whether the authors have access to a systematic literature search protocol or if selection of cited papers is opportunistic.
