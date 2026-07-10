# Expert Council & Search Strategy — NormEval Background Literature

**Date:** 2026-04-03
**Paper:** "What Do Normative Ethics Benchmarks Actually Test? A Meta-Evaluation of 37 LLM Moral Reasoning Assessments"
**Target:** NeurIPS 2026 Datasets & Benchmarks Track

---

## Directory Structure

```
BACKGROUND/
├── 00-council-and-search-strategy.md   # This file
├── 03-bibliography.md                   # Master bibliography (122 entries)
├── .gitignore                           # Excludes ORIG/ from git
├── EXTRACT/                             # ★ USE THIS — 123 markdown text extracts
│   ├── 1993-Tronto-Moral Boundaries Ethics of Care.md
│   ├── 2001-Greene-fMRI Emotional Engagement Moral Judgment.md
│   └── ... (123 files)
├── ORIG/                                # Original PDFs (~170MB, gitignored)
│   └── *.pdf
├── 01-vault-papers/                     # (emptied — originals moved to ORIG/)
└── 02-external-papers/                  # (emptied — originals moved to ORIG/)
```

> **IMPORTANT:** For all future analysis, reading, and citation work, use **EXTRACT/** only.
> The **ORIG/** folder contains original PDFs (~170MB) and is gitignored.
> Do NOT reference or read from `01-vault-papers/` or `02-external-papers/` — they are empty.

---

## Expert Council (14 Members)

### 1. Dr. Psychometrics — Construct Validity Specialist
**Expertise:** Psychometric theory, construct validity, measurement in NLP
**Perspective:** The paper claims benchmarks test the wrong thing (judgment not reasoning). This expert grounds that claim in construct validity theory from educational testing (Messick 1989) and recent NLP-specific treatments.
**Search Block:** A (Construct Validity + Benchmark Lifecycle)

### 2. Dr. Lifecycle — Benchmark Saturation Expert
**Expertise:** NLP benchmark history, dataset artifacts, evaluation methodology
**Perspective:** The ETHICS ceiling effect (Claim 1) needs context in the broader NLP history of benchmark saturation — GLUE/SuperGLUE, SQuAD, dataset artifacts in SNLI. When do benchmarks "expire"?
**Search Block:** A

### 3. Dr. Machine Ethics — Computational Ethics Pioneer
**Expertise:** Machine ethics, computational morality, ethical AI foundations
**Perspective:** The paper's intellectual lineage extends to pre-LLM computational ethics. Wallach & Allen (2009), Anderson & Anderson (2011), and Moor (2006) are seminal works any reviewer in AI ethics will expect.
**Search Block:** B (Computational Ethics Foundations)

### 4. Dr. Dual-Process — Moral Cognition Researcher
**Expertise:** Moral psychology, dual-process theory, neuroscience of ethics
**Perspective:** The consequentialist bias finding (Claim 2: 77% utilitarian vs 50% deontological) maps directly onto Greene's dual-process theory. Utilitarian reasoning is "algorithmically transparent" (computationally explicit), while deontological reasoning is more intuitive/emotional — explaining why LLMs trained on text find the former easier.
**Search Block:** C (Dual-Process Moral Cognition)

### 5. Dr. Care Ethics — Feminist Ethics Scholar
**Expertise:** Care ethics, relational ethics, feminist moral philosophy
**Perspective:** Claim 3 (no care ethics benchmark exists) is a major finding. This expert explains *why* care ethics resists formalization: it is fundamentally relational, dialogic, and longitudinal — properties incompatible with MCQ or classification formats.
**Search Block:** D (Care Ethics Operationalization)

### 6. Dr. Contamination — Data Leakage Expert
**Expertise:** Training data contamination, benchmark security, evaluation integrity
**Perspective:** The ETHICS ceiling effect (Claim 1) may partly result from data contamination rather than genuine capability. ETHICS was released in 2021, and its training items are likely in most frontier LLM training sets.
**Search Block:** E (Data Contamination)

### 7. Dr. Harness — Evaluation Infrastructure Expert
**Expertise:** Evaluation harnesses, reproducible evaluation, benchmark engineering
**Perspective:** The paper's Appendix F (harness compatibility matrix) and PE axis rely on understanding evaluation infrastructure. This expert contextualizes lm-eval-harness, Inspect, HELM, and their role in benchmark adoption.
**Search Block:** I (LLM-as-Judge Methodology)

### 8. Dr. RLHF — Alignment Training Specialist
**Expertise:** RLHF, constitutional AI, reward modeling, preference learning
**Perspective:** Section 5.2 hypothesizes that RLHF systematically favors consequentialist reasoning. This expert finds literature connecting RLHF/preference-based training to outcome-oriented moral reasoning.
**Search Block:** F (RLHF & Consequentialist Bias)

### 9. Dr. Datasheets — Benchmark Documentation Expert
**Expertise:** Dataset documentation standards, NeurIPS D&B track norms
**Perspective:** As a D&B track submission, the paper should cite foundational documentation papers: Gebru et al. (2021) Datasheets, Bender & Friedman (2018) Data Statements, Mitchell et al. (2019) Model Cards.
**Search Block:** G (Benchmark Documentation Standards)

### 10. Dr. Cross-Cultural — Cultural Psychology Expert
**Expertise:** Cross-cultural moral psychology, WEIRD critique, moral universals
**Perspective:** Most benchmarks are WEIRD-centric. Henrich et al. (2010) is essentially mandatory for any paper discussing moral evaluation across populations.
**Search Block:** H (Cross-Cultural Moral Psychology)

### 11. Dr. AI Ethics Survey — Normative AI Ethics Reviewer
**Expertise:** AI ethics surveys, normative frameworks for AI, philosophical AI safety
**Perspective:** The paper needs comprehensive surveys of normative frameworks applied to AI beyond the specific benchmark papers. Floridi & Cowls (2019), Jobin et al. (2019) are key references.
**Search Block:** K (Philosophical AI Ethics Surveys)

### 12. Dr. Moral Philosophy — Reasoning vs. Judgment Philosopher
**Expertise:** Moral philosophy, moral epistemology, the reasoning/judgment distinction
**Perspective:** Claim 4 (28/37 test judgment not reasoning) has a rich philosophical history. Rest's Four Component Model (1986) is the canonical distinction. Haidt (2001) social intuitionist model challenges the primacy of reasoning.
**Search Block:** J (Moral Reasoning vs. Judgment)

### 13. Dr. Meta-Science — Benchmark Meta-Analysis Methodologist
**Expertise:** Systematic reviews, meta-analysis methodology, evidence synthesis
**Perspective:** The paper is itself a meta-evaluation. This expert finds methodological precedents for systematic reviews of benchmarks and PRISMA adaptations for computational venues.
**Search Block:** A (combined with Dr. Psychometrics)

### 14. Dr. Pluralism — Value Pluralism and Disagreement Specialist
**Expertise:** Moral pluralism, value alignment under disagreement, democratic AI
**Perspective:** How to handle genuine moral disagreement in evaluation design. MacAskill et al. (2020) on moral uncertainty provides the theoretical framework.
**Search Block:** L (Value Pluralism / Moral Uncertainty)

---

## Search Execution Log

### Tier 1 — CRITICAL (Blocks A, B, C)
_Status: COMPLETE — 37 papers (16+13+8)_

### Tier 2 — HIGH (Blocks D, E, F, G)
_Status: COMPLETE — 33 papers (11+8+8+6)_

### Tier 3 — MEDIUM (Blocks H, I, J, K)
_Status: COMPLETE — 15 papers (4+3+4+4)_

### Tier 4 — LOW (Blocks L, M)
_Status: COMPLETE — 7 papers (3+4)_

---

## Paper Count Tracking

| Category | Target | Found | Downloaded |
|----------|--------|-------|------------|
| Vault papers | ~25 | 25 | 25 |
| Block A: Construct Validity + Lifecycle | 8-14 | 16 | 16 |
| Block B: Computational Ethics | 5-6 | 13 | 13 |
| Block C: Dual-Process Cognition | 4-6 | 8 | 8 |
| Block D: Care Ethics | 4-7 | 11 | 11 |
| Block E: Data Contamination | 4-7 | 8 | 8 |
| Block F: RLHF Bias | 5-8 | 8 | 8 |
| Block G: Documentation Standards | 4-5 | 6 | 6 |
| Block H: Cross-Cultural | 3-4 | 4 | 4 |
| Block I: LLM-as-Judge | 1-2 | 3 | 3 |
| Block J: Reasoning vs. Judgment | 3-4 | 4 | 4 |
| Block K: AI Ethics Surveys | 3-4 | 4 | 4 |
| Block L: Value Pluralism | 2-4 | 3 | 3 |
| Block M: Recent Benchmarks | 2-4 | 4 | 4 |
| **TOTAL** | **~60-80** | **120** | **120** |
