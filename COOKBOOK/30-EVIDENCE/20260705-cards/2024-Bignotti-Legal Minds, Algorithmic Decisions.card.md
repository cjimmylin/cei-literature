---
stem: "2024-Bignotti-Legal Minds, Algorithmic Decisions"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [normative-ethics, pluralism-aggregation, design-space, validity-psychometrics]
task_format: "generative"
scoring_type: "mixed"
dataset_size: 17
dataset_construction: "scraped"
languages: ["it"]
models_tested: ["GPT-4-turbo"]
headline_numbers:
  - "GPT-4 cosine distance from Applicant (progressive): 0.154–0.273; from State (conservative): 0.646–0.685 across verdict types (p.6, Table 2)"
  - "ALL-MPNET-BASE-V2 embedding model achieved 91% average precision on held-out argument pairs after finetuning (p.5)"
  - "GPT-4 argument extraction completeness and consistency rated mostly 3–5 out of 5 across 17 rulings (p.3)"
  - "GPT-4 alignment with Applicant remains consistent across 5 repeated sampling iterations (p.7, Table 3)"
---
## 1. Gist
This paper evaluates GPT-4's value alignment by comparing its legal arguments on 17 Italian Constitutional Court bioethics rulings against the positions of three legal parties: the Applicant (typically progressive), the State (conservative), and the Constitutional Court (moderate). Using a custom contrastive-learning embedding model fine-tuned to recognize concordant vs. opposing legal interpretations, the authors compute cosine distances between GPT-4's generated arguments and the existing party positions. The main finding is that GPT-4 consistently aligns with progressive interpretations of constitutional principles (e.g., same-sex parenthood, surrogate motherhood, end-of-life care), mirroring the Applicant's stance and diverging from the State's. This is a methodologically creative study using real-world legal adjudication as a "natural benchmark" for testing LLM values in genuinely complex, pluralistic scenarios.

## 2. Benchmark/eval design features
- **Construct measured:** LLM value alignment in real-world complex scenarios where competing constitutional values must be balanced.
- **Dataset:** 17 rulings from the Italian Constitutional Court (1975–2023) on bioethics: assisted procreation, homosexual parenthood, best interests of the child, end-of-life care.
- **Three-party comparison:** Each ruling contains arguments from Applicant (challenging law = typically progressive), State (defending law = typically conservative), and Court (the moderate adjudicator).
- **Embedding-based alignment scoring:** Custom embedding model fine-tuned with contrastive loss to push opposing legal arguments apart in vector space. Cosine distance used to quantify how close GPT-4's arguments are to each party.
- **Argument extraction evaluation:** GPT-4 also evaluated on completeness (identifying all constitutional articles), consistency (accurate summarization), and hallucination (fabricated arguments) — scored 1–5 with a rubric.
- **Robustness check:** Two prompting conditions (FATTO: full case description; FATTO-CLEAN: shortened human-written version without opinion leakage), and 5 repeated sampling iterations per ruling.

## 3. Task format & example item
Generative. GPT-4 is prompted with a description of a legal case and asked to state its own position and arguments. Example (p.7, discussion):

> For a case on embryo research: GPT-4 generates arguments supporting scientific research on embryos without adequately weighing the competing value of embryo protection.

The prompt instructs the model to structure its argument around relevant constitutional articles, mirroring the dataset format. The exact prompt text is in Appendix B.1 (not fully reproduced in the extract).

## 4. Scoring / grading methodology
**Two methods in parallel:**
1. **Embedding cosine distance:** The custom ALL-MPNET-BASE-V2 model (fine-tuned with contrastive loss on manually labeled concordant/opposing argument pairs) embeds GPT-4's arguments and each party's arguments; cosine distance is computed pairwise. Lower distance = greater alignment.
2. **Human rubric scoring (1–5)** for argument extraction quality: completeness, consistency, and hallucination. Applied to GPT-4's extraction of each party's arguments from the 17 rulings.

The embedding model achieved 91% average precision on a test set of labeled argument pairs (p.5).

## 5. Dataset construction & provenance
- **Source:** 17 publicly available rulings from the Italian Constitutional Court (cortecostituzionale.it), covering 1975–2023.
- **Cases selected** to demonstrate value trade-offs: assisted procreation (151/09, 96/15, 221/19, 162/14, 161/23, 229/15, 84/16), child's best interest (272/17, 230/20, 225/16, 32/21, 33/21, 237/19, 79/22), end-of-life care (242/19, 334/08), and abortion (27/75).
- **Argument pairs for embedding fine-tuning:** Created by pairing arguments made by different parties on the same case, then manually labeled as concordant (1) or opposing (0).
- **Fine-tuning:** 25 epochs, learning rate 2e-5, AdamW optimizer.
- Dataset is small and novel; not publicly released.

## 6. Validity evidence
- **Two prompting conditions** (FATTO vs. FATTO-CLEAN) produce consistent results, suggesting findings are not artifacts of information leakage in the longer prompt (p.6).
- **5 repeated sampling iterations** show mostly stable cosine distances (p.7, Table 3), demonstrating that GPT-4's progressive bias is a systematic tendency rather than stochastic noise.
- **Embedding model precision** of 91% on held-out labeled pairs provides technical validation of the measurement instrument (p.5).
- **Limitation of human rubric:** Evaluation is acknowledged as complex and qualitative, with no inter-rater reliability reported for the 1–5 scoring of argument extraction quality.

## 7. Saturation / discrimination
Not directly applicable — no benchmark with multiple items designed for difficulty gradation. However, the study discriminates well: GPT-4's alignment with the Applicant (cosine ~0.15–0.27) is clearly and consistently different from alignment with the State (~0.65–0.71). The Court occupies a middle position (~0.27–0.54), showing meaningful within-dataset variation.

## 8. Multiturn / agentic aspects
n/a. Single-turn prompts; GPT-4 receives case description and generates legal arguments once.

## 9. Key numbers
- 17 rulings in dataset, covering 1975–2023 (p.3)
- GPT-4 cosine distance from Applicant: 0.154–0.273 (FATTO, across verdict types) (p.6, Table 2)
- GPT-4 cosine distance from State: 0.646–0.685 (p.6, Table 2)
- GPT-4 cosine distance from Court: 0.171–0.530 (p.6, Table 2)
- Embedding model ALL-MPNET-BASE-V2 test set average precision: 91% (p.5)
- Embedding model trained for 25 epochs, learning rate 2e-5, AdamW (p.5)
- 5 repeated sampling iterations per ruling for consistency testing (p.5)
- Consistency of progressive bias maintained across all 5 iterations (p.7, Table 3)

## 10. Pitfalls & limitations
- **Single model (GPT-4 only):** context length requirements at time of writing precluded other models; comparative analysis impossible.
- **Small dataset:** 17 rulings is insufficient to make strong statistical claims about GPT-4's global alignment tendencies.
- **Italian-language domain:** findings may not generalize across languages or legal systems; bioethics is a specific and potentially unrepresentative domain.
- **Prompt sensitivity:** the authors acknowledge (citing Röttger et al. 2024) that small prompt changes can shift model positions — this robustness was not systematically tested beyond two conditions.
- **Circular use of GPT-4:** GPT-4 both extracts arguments from rulings and is evaluated on those arguments — potential for the extraction to bias what the model then generates as its own position.
- **No non-LLM baseline** for comparison; no test of whether human legal experts would show similar patterns.
- **Progressive/conservative framing** relies on the paper's characterization of Italian Constitutional Court dynamics — contested in context.

## 11. Novel ideas worth stealing
1. **Real legal rulings as value benchmark items**: court cases encode genuine societal value trade-offs that are far richer than questionnaire items — using published rulings from courts as a values-evaluation corpus is immediately transferable to other jurisdictions and domains.
2. **Contrastive embedding fine-tuning for argument similarity**: training an embedding model to push opposing arguments apart (rather than just measuring raw semantic similarity) is a sophisticated method for measuring value alignment that could be adapted for moral philosophy texts, policy documents, or religious teachings.
3. **Three-party structure as scale**: comparing model output to a known-progressive party, a known-conservative party, and a moderate adjudicator provides a calibrated scale for value orientation without requiring explicit political labels — generalizable to any domain with multi-stakeholder debates.
4. **FATTO vs. FATTO-CLEAN robustness test**: the clean/unclean prompt comparison as a built-in validity check for information leakage is a reusable design pattern for any benchmark where context could contain hints about the "correct" answer.
5. **Repeated sampling for consistency**: measuring cosine distance variance across 5 completions reveals whether a model's value alignment is stable or stochastic — a simple but underused validity check applicable to any open-ended values evaluation.

## 12. Notable quotes
- "GPT-4 consistently aligns more closely with progressive interpretations of the Constitution, often overlooking competing values and mirroring the applicants' views rather than the more conservative perspectives of the State." (p.1)
- "The model exhibits a tendency to inadequately balance divergent interests and values, potentially leading to an underestimation of the adverse consequences associated with specific actions." (p.7)
- "Conducting unconstrained evaluations in realistic scenarios is preferable to constrained evaluation settings when it comes to investigating a model's values and opinions." (p.9, citing Röttger et al.)
- "Laws can be seen as a proxy of what a society values and protects." (p.8)

## 13. UNKNOWN / not in extract
- The exact prompts used (Appendix B.1, B.2) are referenced but not reproduced in the extract.
- The human rubric for argument extraction scoring (Appendix C) is referenced but not reproduced.
- Inter-rater reliability statistics for the human evaluation of argument quality are not reported.
- The full list of constitutional articles used in evaluation (Appendix D) is not in the extract.
- The number of argument pairs used for embedding model fine-tuning and the train/test split are not specified.
