# Implementation Trial: BuddhismEval — Bilingual Benchmark for Buddhist LLM Evaluation

**Generated:** 20260404
**Trial ID:** RV-T3
**Benchmark:** BuddhismEval: A Bilingual Benchmark for Buddhist Ethical and Philosophical Reasoning
**Paper:** `2025-Xiong-BuddhismEval A Bilingual Benchmark for Buddhist.md`
**Rank in Top 15:** 13 (Composite 41.2)

---

## 1. Benchmark Summary

| Field | Value |
|-------|-------|
| **Tradition** | Buddhism (Dharmic) |
| **Format** | MIX (multiple question types) |
| **Dataset Size** | Unknown (paper under review, dataset gated) |
| **Data Source** | HuggingFace (gated/private) |
| **Data URL** | https://huggingface.co/datasets/Nethmi14/BuddhismEval |
| **Languages** | English, Pali, Sinhala |
| **LLMs Previously Tested** | NA (dataset released without published results) |
| **Composite Score** | 41.2 (RD=42.3, PE=55.0, CI=20.0) |

## 2. Data Acquisition Report

### 2.1 Access Attempts

| Attempt | Method | Result |
|---------|--------|--------|
| 1 | Direct HuggingFace dataset page | HTTP 401 (authentication required) |
| 2 | HuggingFace `datasets-server` API (`/info`) | Error: "dataset does not exist, or is not accessible without authentication" |
| 3 | HuggingFace `datasets-server` API (`/rows`) | Same error |
| 4 | HuggingFace REST API (`/api/datasets/`) | Error: "Invalid username or password" |
| 5 | PDF extract from vault | **CORRUPTED** — contains education encyclopedia pages, not the BuddhismEval paper |

### 2.2 Data Accessibility

- **Status: INACCESSIBLE** — Dataset is gated or private on HuggingFace
- The paper is described as "under review, likely NeurIPS 2025"
- No alternative data source found (no GitHub mirror, no arXiv supplementary)
- The PDF in the vault (`2025-Xiong-BuddhismEval Bilingual Evaluation Benchmark for Buddhist.pdf`) is a **wrong document** — its extract shows an education encyclopedia, not the BuddhismEval paper

### 2.3 Information Available from Vault Abstract

From the Top 15 JSON abstract (truncated):
> "BuddhismEval is the first bilingual evaluation benchmark specifically designed to assess LLMs on Buddhist ethical reasoning and philosophical understanding. It includes factual, ethical, philosophical, and applied reasoning questions drawn from the Dhammapada, Abhidharma texts, Sri Lankan government..."

### 2.4 Inferred Dataset Characteristics (from abstract + metadata)

| Feature | Inferred Value | Confidence |
|---------|---------------|------------|
| **Question categories** | Factual, Ethical, Philosophical, Applied reasoning | HIGH (from abstract) |
| **Source texts** | Dhammapada, Abhidharma, Sri Lankan government sources | HIGH (from abstract) |
| **Languages** | English + Pali + Sinhala | MEDIUM (metadata says so) |
| **Format** | Mixed (MCQ + open-ended likely) | LOW (inferred from MIX code) |
| **Denominations** | Likely Theravada-focused (Sri Lankan context) | MEDIUM |
| **Size** | Unknown | — |

## 3. Item Analysis

### 3.1 No Direct Item Inspection Possible

Without data access, item analysis relies entirely on the abstract description and genre expectations.

### 3.2 Likely Item Types (Based on "MIX" Format and Abstract)

| Category | Likely Format | Example Domain |
|----------|--------------|----------------|
| **Factual** | MCQ | "What is the first Noble Truth?" |
| **Ethical** | Scenario-based | "A monk encounters X situation. According to the Vinaya..." |
| **Philosophical** | Open-ended | "Explain the relationship between sunyata and pratityasamutpada" |
| **Applied reasoning** | Case study | "How would Buddhist ethics evaluate the use of AI in..." |

### 3.3 Language Complexity

The inclusion of Pali items is notable:
- Pali is a classical liturgical language with very limited LLM training data
- Performance on Pali items would likely show extreme floor effects
- Sinhala adds another low-resource dimension
- The bilingual design enables cross-lingual analysis of religious knowledge

## 4. Implementability Assessment

### 4.1 Current Status

| Aspect | Rating (1-5) | Notes |
|--------|-------------|-------|
| **Data access** | 1 | BLOCKED — dataset is gated/private, no alternative source |
| **Format adaptation** | 2 | MIX format requires multiple scoring methods |
| **Scoring setup** | 2 | Unknown scoring method; open-ended questions need judge model |
| **Prompt engineering** | 3 | English items straightforward; Pali/Sinhala items challenging |
| **Overall difficulty** | 2 (hard) | Cannot proceed without data access |

### 4.2 Blockers

1. **Primary blocker:** Dataset is not publicly accessible
2. **Secondary blocker:** No published paper with methodology details
3. **Tertiary blocker:** PDF in vault is wrong document — no way to inspect item format

### 4.3 Possible Remediation

| Action | Likelihood of Success |
|--------|----------------------|
| Contact authors (Nethmi Muthugala, Deyi Xiong) for access | MEDIUM — common for pre-publication datasets |
| Wait for NeurIPS 2025 publication (if accepted) | HIGH but delayed (~6 months) |
| Request HuggingFace gated access (if gated, not private) | MEDIUM — may require justification |
| Construct proxy items from Dhammapada/Abhidharma sources | LOW — would not be the actual benchmark |

## 5. Preliminary Findings: Structural Analysis

### 5.1 What BuddhismEval Likely Tests

Based on the abstract and benchmark design:

| Construct | Estimated Weight | Rationale |
|-----------|-----------------|-----------|
| **Factual knowledge** | 30% | Dhammapada/Abhidharma factual questions |
| **Ethical reasoning** | 25% | Buddhist ethics application to scenarios |
| **Philosophical understanding** | 25% | Conceptual relationships in Buddhist thought |
| **Applied reasoning** | 10% | Real-world application of Buddhist principles |
| **Linguistic competence** | 10% | Pali/Sinhala comprehension |

### 5.2 Unique Value Proposition

- **Only Buddhism-specific benchmark** in the Top 15
- **Trilingual** (English/Pali/Sinhala) — tests low-resource language handling
- **Theravada focus** — complements any Mahayana/Zen-oriented benchmarks
- **Ethics + philosophy** — goes beyond factual knowledge to test reasoning about Buddhist values

### 5.3 Potential Concerns

1. **Theravada bias** — Sri Lankan context may underrepresent Mahayana, Vajrayana, Zen traditions
2. **Pali floor effect** — LLMs likely have minimal Pali training data; scores may be uninformatively low
3. **MIX format** — different question types make aggregate scoring non-trivial
4. **No published baselines** — cannot compare our results to any reference

## 6. Meta-Evaluation Ratings

| Criterion | Score | Justification |
|-----------|-------|---------------|
| **Content Validity** | MEDIUM | Abstract suggests appropriate Buddhist sources, but cannot verify item quality without data access |
| **Discriminative Power** | MEDIUM | Multi-category design should discriminate, but Pali items may create uninformative floor |
| **Cultural Authenticity** | NATIVE (inferred) | First author appears to be Sri Lankan Buddhist scholar; sources from canonical texts |
| **Reproducibility** | 2/5 | Data currently inaccessible; no published methodology; no baselines |
| **Complementarity** | 5/5 | Only Buddhism benchmark — fills critical gap in tradition coverage |
| **Construct Coverage** | Knowledge + Reasoning + Values (inferred) | Multi-category design covers broader range than pure MCQ |
| **Annotation Quality** | Unknown | Cannot assess without data access |

## 7. Verdict

**[x] MODIFY** — Viable but needs adaptation (data access required)

### Justification

BuddhismEval fills the most critical gap in the Top 15 — it is the only Buddhism-specific benchmark. Its trilingual design and multi-category structure are exactly what the paper needs to demonstrate tradition diversity. However, the dataset is currently inaccessible, making implementation impossible without author cooperation.

### Recommended Actions

1. **Immediate:** Contact authors (Nethmi Muthugala at Tianjin University, Deyi Xiong) requesting research access
2. **Parallel:** Correct the vault PDF — the current extract is from a wrong document (education encyclopedia)
3. **Fallback:** If access is denied, document the inaccessibility as a finding for Section 4.4 (reproducibility barrier in religious benchmarks)
4. **Paper framing:** Use the inaccessibility itself as evidence for the "reproducibility crisis" argument — a Top 13 benchmark whose data cannot be independently verified

### Data Quality Issue Noted

The PDF extract at `PDF Extracts/2025/2025-Xiong-BuddhismEval Bilingual Evaluation Benchmark for Buddhist.md` contains pages from what appears to be an education encyclopedia (entries for "Abacus", "Buddhist education", "Catholic school", etc.) — this is NOT the BuddhismEval paper. The local PDF should be re-acquired.
