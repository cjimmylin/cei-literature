# Stage-4 `research_topic` Vocabulary Inventory

**Generated:** 2026-07-10  
**Lane:** D1 (parallel session — read-only on papers/)  
**Purpose:** Fresh full inventory of live Stage-4 `research_topic` vocabulary vs. documented v1.5 codes

---

## Methodology

**Script:** Inline Python (run via `/Users/jimmy.lin/Documents/CEI-Literature-Vault/.venv/bin/python`)

**Parsing logic:**
- Opened every `.md` file in `papers/` (2,385 files total)
- Extracted YAML frontmatter (content between leading `---` delimiters)
- Parsed `research_topic:` with a two-pass line scanner:
  - Scalar form: `research_topic: "Value"` → strip quotes, collect single value
  - List form: `research_topic:` followed by `  - Item` lines → collect all items
  - Null/empty/N/A values: recorded as "field present but empty"
- Counted distinct values by number of *papers* using them (not total occurrences — no paper carried multiple values in this scan; all counts are paper counts = occurrence counts)
- Papers missing the field entirely: counted but not anomalies (field is only populated post-Stage-4 pipeline)

**Documented vocabulary sources:**
- `_OPERATING-SYSTEM/Standards/classification-logic.md` (v1.5, 2026-07-09)
  - Stage 4 codes: 12 documented categories (§ "Stage 4: Research Topic")
  - Stage 3 codes: 15 documented categories (§ "Stage 3: Ethics Perspective")
  - 5 new v1.5 codes are dual-homed in both stages: Specification & Compliance, Scalable Oversight, Preference Aggregation & Social Choice, Value Formation & Emergent Misalignment, Multi-Agent Value Dynamics

---

## Full Value Table (sorted by live count descending)

| research_topic value | Papers using it | Documented? (Stage3 / Stage4 / both / NO) |
|---|---|---|
| Machine Learning | 207 | Stage4-only |
| Other | 182 | NO |
| NLP & Representation Learning | 171 | Stage4-only |
| Machine Translation | 123 | Stage4-only |
| Social & Cultural Analysis | 89 | NO |
| Question Answering | 41 | Stage4-only |
| AI Safety & Alignment | 36 | both |
| Truthfulness & Factuality | 32 | Stage3-only |
| Computer Vision & Multimodal | 31 | NO |
| Bias & Fairness | 12 | Stage3-only |
| Dialogue Systems | 11 | NO |
| Interpretability & Explainability | 5 | NO |
| LLM Moral Reasoning | 5 | NO |
| Machine Ethics | 2 | Stage3-only |
| AI Ethics | 2 | NO |
| GAMA Moral Agent | 1 | NO |
| AI Alignment & Normative Ethics | 1 | NO |
| SPECTRA Ethical Framework | 1 | NO |
| AI Impact on Practical Wisdom | 1 | NO |
| LLM Moral Persuasion | 1 | NO |
| LLM Moral Foundations | 1 | NO |
| Socratic AI Ethics | 1 | NO |
| AI Alignment & Fairness | 1 | NO |
| AI Ethics Verification | 1 | NO |

**Total distinct live values:** 24  
**Undocumented live values:** 16  
**Stage3-only values used as Stage-4 labels (routing anomaly):** 4 (Truthfulness & Factuality, Bias & Fairness, Machine Ethics, and AI Safety & Alignment also appears in Stage 3)

---

## Documented-But-Unused Codes (count = 0)

These codes appear in the v1.5 documented vocabulary but have zero live occurrences in `research_topic`.

| Code | Where documented |
|---|---|
| Benchmarks & Datasets | Stage4-only |
| Computer Vision | Stage4-only (live variant is "Computer Vision & Multimodal") |
| Human Rights & Social Justice | Stage3-only |
| Moral Reasoning & Psychology | Stage3-only |
| Multi-Agent Value Dynamics | both (v1.5 new) |
| Preference Aggregation & Social Choice | both (v1.5 new) |
| Privacy & Surveillance | Stage3-only |
| Responsible AI | Stage3-only |
| Scalable Oversight | both (v1.5 new) |
| Specification & Compliance | both (v1.5 new) |
| Toxicity & Hate Speech | Stage3-only |
| Value Alignment | Stage3-only |
| Value Formation & Emergent Misalignment | both (v1.5 new) |

**Total documented-but-unused:** 13 (including all 5 new v1.5 codes)

---

## Summary Statistics

| Metric | Count |
|---|---|
| Total `.md` files scanned | 2,385 |
| Papers WITH `research_topic` field | 958 |
| Papers WITHOUT `research_topic` field | 1,427 |
| Distinct live `research_topic` values | 24 |
| Undocumented live values | 16 |
| Documented-but-unused codes | 13 |
| All-5 new v1.5 codes with live count > 0 | 0 (all five unused) |
| Stage3-only labels used as Stage-4 tags | 4 (routing anomaly) |

---

## Parsing Anomalies

No YAML read errors, missing frontmatter, or empty-field anomalies were detected. All 958 papers with the `research_topic` field parsed cleanly with valid scalar values. No paper carried multiple `research_topic` values (list form not used in live data).

---

## Notes on Undocumented Values

### High-count undocumented values (action likely needed)

**"Other" (182 papers)**  
Catch-all label not in the Stage-4 taxonomy. Largest undocumented bucket. Should be reviewed and redistributed into documented categories, or formally added as a documented escape-hatch code with a definition.

**"Social & Cultural Analysis" (89 papers)**  
Substantial category with no documented equivalent. Likely covers anthropology, sociology, cultural studies papers. Not clearly mappable to any existing Stage-4 code. Candidate for formal addition.

**"Computer Vision & Multimodal" (31 papers)**  
Variant of documented "Computer Vision" with "&Multimodal" suffix. The live label differs from the documented label. Either the documented label should be updated to "Computer Vision & Multimodal", or papers should be relabeled to "Computer Vision".

**"Dialogue Systems" (11 papers)**  
No documented equivalent. Likely covers conversational AI, chatbot systems papers. Not subsumed by "NLP & Representation Learning" in practice.

**"Interpretability & Explainability" (5 papers)**  
No documented equivalent. Meaningful technical sub-domain.

**"LLM Moral Reasoning" (5 papers)**  
Ethically-flavored label applied in Stage-4 context. May indicate routing errors (papers that scored `ethics_overall < 50` but have moral content). Papers:
- 2024-Agarwal-Ethical Reasoning Depends on Language.md
- 2024-Almeida-Exploring the Psychology of LLMs Moral Reasoning.md
- 2025-Chakraborty-Structured Moral Reasoning.md
- 2025-Sachdeva-Normative Evaluation of LLMs with Everyday Moral Dilemmas.md
- 2025-Samway-Are Language Models Consequentialist or Deontological.md

### Singleton undocumented values (likely manual overrides or classification errors)

| Value | Paper |
|---|---|
| GAMA Moral Agent | 2020-Akrout-Machine Ethics - Creation of a Virtuous Machine.md |
| AI Alignment & Normative Ethics | 2020-Gabriel-Artificial Intelligence Values and Alignment.md |
| SPECTRA Ethical Framework | 2024-Chhabra-Evaluating Computational Models of Ethics.md |
| AI Impact on Practical Wisdom | 2024-Eisikovits-AI and Phronesis.md |
| LLM Moral Persuasion | 2024-Huang-Moral Persuasion in Large Language Models.md |
| LLM Moral Foundations | 2024-Kirgis-Differences in Moral Foundations of LLMs.md |
| Socratic AI Ethics | 2024-Wilders-Socratic Dialogue for Virtue Ethics in AI.md |
| AI Alignment & Fairness | 2025-Gabriel-AI Alignment as Fair Treatment of Claims.md |
| AI Ethics Verification | 2025-Priya-Deontic Temporal Logic for AI Ethics.md |

These 9 singletons appear to be paper-specific manually-assigned labels (named after paper subject matter, not taxonomy codes). They likely represent ethics-adjacent papers that scored `ethics_overall < 50` and received ad-hoc labels.

### Stage-3 labels used in Stage-4 position (routing anomaly)

| Value | Live count | Documented in |
|---|---|---|
| Truthfulness & Factuality | 32 | Stage3-only |
| Bias & Fairness | 12 | Stage3-only |
| Machine Ethics | 2 | Stage3-only |
| AI Safety & Alignment | 36 | both (Stage3 + Stage4) |

"AI Safety & Alignment" is intentionally dual-homed. The other three ("Truthfulness & Factuality", "Bias & Fairness", "Machine Ethics") are Stage-3-only codes that appear in Stage-4 `research_topic` fields — either routing errors or deliberate manual overrides.

---

## Recommended Actions (for orchestrator)

1. **"Other" (182)** — highest-priority cleanup; redistribute or formally document.
2. **"Social & Cultural Analysis" (89)** — add to Stage-4 taxonomy or reclassify.
3. **"Computer Vision & Multimodal" (31)** — reconcile with documented "Computer Vision" label.
4. **"Dialogue Systems" (11)** — candidate for formal addition to Stage-4.
5. **5 new v1.5 codes (0 live)** — pipeline has not yet run Stage-4 classification with the v1.5 expanded vocabulary; next Stage-4 batch run will populate these.
6. **Stage-3 labels in Stage-4 position** — audit routing for Truthfulness & Factuality (32), Bias & Fairness (12), Machine Ethics (2) papers.
