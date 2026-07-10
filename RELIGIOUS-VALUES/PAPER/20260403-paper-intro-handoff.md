# Session Handoff: Religious Values Paper — Introduction & Literature Review

**Date:** 2026-04-03
**Project:** Religious Values Benchmark Paper — "What Do Religious Values Benchmarks Actually Test?"
**Location:** `CEI-Lit-WS/RELIGIOUS-VALUES/PAPER/`
**Status:** Introduction (Section 1) and Literature Review (Section 2) complete. Council-reviewed and revised.

---

## 1. What Was Accomplished

Wrote a comprehensive introduction and field review for the paper, following the NormEval sister-paper template. The process used a 6-agent parallel architecture with a 12-member expert council deliberation and revision cycle.

### Pipeline Summary

| Phase | Description | Output |
|-------|-------------|--------|
| **0** | Spine document — paper contract, 7 claims, glossary, 12-member council, citation keys | `spine-religious-values.md` |
| **1** | Introduction writing (Section 1) — paradox opening, three problems, threefold contributions | `section1-introduction.md` (intermediate) |
| **2a** | Literature Review Sections 2.1-2.3 — AI eval, religious/cultural values, bias/fairness | `section2-litreview-part1.md` (intermediate) |
| **2b** | Literature Review Sections 2.4-2.6 — sacred text NLP, Indigenous/marginalized, contribution positioning | `section2-litreview-part2.md` (intermediate) |
| **3** | Assembly + 12-member council deliberation — 52 recommendations, 2 minority reports | `council-deliberation-intro-review.md` |
| **4** | Final revision — all 3 critical, 7 important, 6 desirable revisions implemented | `introduction-religious-values.md` (canonical) |
| **5** | PDF generation via pandoc + typst | `introduction-religious-values.pdf` |

---

## 2. Key Numbers

| Metric | Value |
|--------|-------|
| Total word count (Sections 1+2) | ~5,036 |
| Citation blocks | ~24 (referencing 70+ papers) |
| Literature review subsections | 6 |
| Council members | 12 (6 tradition-specific + 6 methodological) |
| Council revision recommendations | 52 total (3 critical, 7 important, 6 desirable) |
| Minority reports | 2 (Bilimoria on word allocation; Mohamed on post-benchmark paradigms) |
| All critical revisions implemented | Yes |
| All important revisions implemented | Yes |
| Desirable revisions implemented | 6 of 6 |
| PDF pages | ~10 |

---

## 3. Document Structure

### Section 1: Introduction (~1,300 words, 5 paragraphs)

| Paragraph | Content | Key Citations |
|-----------|---------|---------------|
| P1 — Paradox Opening | 80%+ of humanity's moral reasoning is religious; no systematic framework for evaluating religious values benchmarks | Klingefjord 2024, Ji 2024, Gabriel 2020 |
| P2 — Consequential Stakes | LLMs in pastoral counseling, halal advisory, content moderation; HELM/BIG-Bench treat religion as demographic or knowledge domain; Ramadan/maslaha example | Liang 2023, Srivastava 2023, Bianchi 2024, Alharbi 2024 |
| P3 — Three Problems | (1) Tradition asymmetry: 8/14 at zero, Islam dominance; (2) Knowledge-reasoning conflation; (3) Structural epistemic injustice with Fricker grounding + CARE data sovereignty qualifier | Mohamed 2020, Fricker 2007, Bilimoria 2013, Henrich 2010, Carroll 2020 |
| P4 — Threefold Contributions | 3-axis RD/PE/CI framework; 401-candidate tradition coverage analysis; epistemic injustice diagnosis | Gupta 2025, Li 2025, Rao 2025 |
| P5 — Roadmap | Sections 2-6 preview | — |

### Section 2: Related Work (~3,700 words, 6 subsections)

| Subsection | Words | Content | Key Papers |
|------------|-------|---------|------------|
| 2.1 AI Alignment Evaluation & Benchmark Science | ~650 | HELM/MMLU/BIG-Bench as monolithic; RLHF secular preference space; values alignment theory; psychometric critique | Liang, Hendrycks, Srivastava, Gabriel, Klingefjord, Ji, Gupta, Li, PATCH |
| 2.2 Religious and Cultural Values in AI | ~850 | Cultural values (WEIRD, Schwartz, Hofstede); Islamic AI ethics (Maqasid, IslamicMMLU, HAQA/QUQA); Other Abrahamic (doctrinal flattening, Talmudic Logic, Sefaria); Dharmic/East Asian (visesa-dharma, wu wei, Sikh/Jain) | Henrich, Schwartz, Kamali, Alharbi, Francis, Johnson, Abraham, Koppel, Chadha, Li |
| 2.3 Religious Bias and Fairness | ~450 | Anti-Muslim bias (Abid 66%); StereoSet, Divine LLaMAs; bias-vs-values orthogonality; Buyl bridging work | Abid, Bianchi, Hamid, Buyl, Nadeem |
| 2.4 Computational Approaches to Sacred Texts | ~500 | Modeling the Sacred (Hutchinson/Leavens); BERT on Upanishads; Al-Bayan QA; ground truth interpretation problem | Leavens, Roberts, Abdelnasser, Al-Azani |
| 2.5 Indigenous, African, and Marginalized | ~700 | Decolonial AI framework; CARE Principles vs. FAIR; Ubuntu relational ontology; structural epistemic injustice named explicitly; post-benchmark paradigms; Maori tikanga | Mohamed, Carroll, Birhane, Gwagwa, Mhlambi, Fricker |
| 2.6 Our Contribution in Context | ~450 | 4 extensions: cultural alignment → religious isolation; bias detection → benchmark quality; psychometric critique → contested constructs; comparative religious ethics "third wave" → meta-evaluation | Durmus, Abid, Gupta, Green, Twiss, Schweiker |

---

## 4. 12-Member Expert Council

### Tier 1 — Tradition-Specific (6)

| # | Name | Discipline | Rating |
|---|------|-----------|--------|
| 1 | Prof. Sachedina | Islamic Ethics | GOOD |
| 2 | Prof. Waters | Christian Theological Ethics | GOOD |
| 3 | Prof. Bilimoria | Dharmic & Comparative Philosophy | ADEQUATE (minority report) |
| 4 | Prof. Li | East Asian Philosophy | ADEQUATE |
| 5 | Dr. Osei-Mensah | African/Indigenous Philosophy | STRONG |
| 6 | Dr. Koppel | Jewish Ethics & Computational Talmudics | GOOD |

### Tier 2 — Methodological (6)

| # | Name | Discipline | Rating |
|---|------|-----------|--------|
| 7 | Dr. Liang | AI Evaluation & Benchmarking | STRONG |
| 8 | Dr. Pearce | Psychometrics & Construct Validity | STRONG |
| 9 | Dr. Cramer | Cultural Psychology & WEIRD Bias | STRONG |
| 10 | Dr. Birhane | Religious Bias & Fairness | GOOD |
| 11 | Dr. Mohamed | Decolonial & Critical Studies | GOOD (minority report) |
| 12 | Dr. Abid | Computational Sacred Texts & NLP | STRONG |

### Council Key Findings

1. **Draft substantively strong** — 9/12 experts rated GOOD or STRONG
2. **Anti-essentialization discipline well-maintained** — minor lapses corrected
3. **Section 2.5 (Indigenous/Marginalized) is strongest** — theoretical grounding praised
4. **Section 2.2d was underweight** — expanded by ~130 words in revision (critical fix)
5. **7 citation key mismatches in Section 2.4** — all fixed in revision
6. **Fricker (2007) missing** — added to ground "epistemic injustice" terminology
7. **Islam dominance framing confirmed respectful** — Expert 1 validated
8. **Two minority reports**: Bilimoria on word-allocation asymmetry; Mohamed on post-benchmark paradigms

---

## 5. Revisions Implemented

### Critical (3/3)
1. Fixed 7 citation key mismatches in Section 2.4 (Schmidhuber→ZhaoLiu, Awad→Abdelnasser, etc.)
2. Added Fricker (2007) citation when introducing "structural epistemic injustice"
3. Expanded Section 2.2d: visesa-dharma, wu wei correction, Sikh/Jain, Chinese-language literature, textual-vs-oral distinction

### Important (7/7)
4. Sharpened bias-vs-values orthogonality (debiased ≠ values-aligned)
5. Corrected Bar-Ilan "digitizing" → "computationally indexing"
6. Corrected maslaha "(public interest)" → "(public interest as constrained by objectives of Islamic law)"
7. Addressed Catholic-centrism: "Christian theologians" + denominational diversity note
8. Added data sovereignty qualifier in Intro P3 (CARE Principles, epistemic sovereignty)
9. Added Koppel (2011) + Sefaria in Jewish discussion
10. Attributed "cracked foundation" specifically to Gehrmann et al.

### Desirable (6/6)
11. Emerging pluralistic alignment (Sorensen 2024) with WEIRD-limitations caveat
12. Habib (2023) alongside Kamali in Maqasid discussion
13. Named Maori tikanga + First Nations data sovereignty in Section 2.5
14. Added Mhlambi (2020) in Section 2.5
15. Post-benchmark evaluation paradigms acknowledged (per Mohamed minority report)
16. Added Levy (2024) on Jewish robot perspectives

---

## 6. File Manifest

| File | Size | Status |
|------|------|--------|
| `spine-religious-values.md` | 16 KB | Canonical paper spine |
| `introduction-religious-values.md` | 39 KB | **CANONICAL** — final revised Section 1 + Section 2 |
| `introduction-religious-values.pdf` | 135 KB | PDF via pandoc + typst |
| `council-deliberation-intro-review.md` | 62 KB | Full 12-member deliberation (52 recommendations) |
| `section1-introduction.md` | 8 KB | Intermediate draft (pre-revision) |
| `section2-litreview-part1.md` | 15 KB | Intermediate draft (pre-revision) |
| `section2-litreview-part2.md` | 13 KB | Intermediate draft (pre-revision) |
| `build_pdf.py` | 2 KB | PDF build script (pandoc + typst) |

---

## 7. Writing Workflow Used

```
Step 0: Spine document (Agent A)
    ↓
Step 1-2: Parallel writing (Agents B, C, D)
    Agent B → Section 1 (Introduction)
    Agent C → Sections 2.1-2.3
    Agent D → Sections 2.4-2.6
    ↓
Step 3: Assembly + Council Deliberation (Agent E)
    12 experts × 5 criteria = 52 recommendations
    ↓
Step 4: Final Revision (Agent F)
    All critical + important + desirable revisions
    ↓
Step 5: PDF generation (build_pdf.py)
```

---

## 8. PDF Build Instructions

```bash
cd CEI-Lit-WS/RELIGIOUS-VALUES/PAPER

# Regenerate PDF from latest markdown
python3 build_pdf.py

# Requires: pandoc (3.9+) + typst
# Citations appear as [AuthorYear] — will resolve once .bib file is created
```

---

## 9. Known Issues & Limitations

### Citation Format
- Citations are LaTeX-style `\cite{Key}` in the markdown, converted to `[Key]` in PDF
- No `.bib` file yet — pandoc cannot resolve to proper author-year or numbered citations
- 7 citation keys in Section 2.4 were corrected but need bibliography entries added

### Content
- The `[PewResearch2017]` citation in the opening sentence needs a specific source (Pew Research Center 2017 report on global religious population)
- Some extract filenames in BACKGROUND don't match the citation keys used — a citation-key-to-extract mapping may be needed
- Two extracts flagged as content mismatches: `2019-Wong-Dao` (5MB physics content) and `2024-Mohanty-Indic` (atlas content) — should not affect the paper since citations are from other sources

### Scope
- Abstract not yet written (will be written after Methods and Results are drafted)
- Sections 3-6 (Methods, Results, Discussion, Conclusion) not yet started
- No figures or tables yet (Figure 1: tradition heatmap, Table 1: scoring axes, Table 2: Top 15)

---

## 10. Recommended Next Steps

### Immediate
1. **Write the Abstract** (~300 words) after Methods and Results sections exist
2. **Write Section 3 (Methods)** — corpus assembly, 3-axis scoring, meta-evaluation criteria, trial protocol
3. **Create `.bib` file** from spine citation keys + BACKGROUND-registry.json for proper citation resolution

### Short-Term
4. **Write Section 4 (Results)** — landscape analysis, Top 15 ranking, tradition gap analysis
5. **Write Section 5 (Discussion)** — implications, limitations, recommendations
6. **Generate figures** — tradition heatmap (Figure 1), RD-vs-PE scatter (Figure 3)
7. **Run implementation trials** on 2-3 benchmarks to populate Section 4.4

### Medium-Term
8. **LaTeX conversion** for NeurIPS D&B submission format
9. **Full bibliography** with proper BibTeX entries for all ~70 cited papers
10. **Supplement** with full 401-candidate feature matrix, format taxonomy, scoring formulas
