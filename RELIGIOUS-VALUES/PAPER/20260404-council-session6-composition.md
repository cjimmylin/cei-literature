# Expert Council Composition: Session 6 — Scoring Framework Critique & Revision

**Date:** 2026-04-04
**Project:** Religious Values Benchmark Paper — "Do AI Systems Understand Religious Values?"
**Mandate:** Comprehensive critique of the existing 3-axis scoring framework, the 22-feature matrix, the `build_religious_feature_matrix.py` implementation, and the Top 15 ranking. Produce actionable revision recommendations.
**Scope:** This council is SEPARATE from the 14-member background literature council (Session 3, D-01/D-02) and the 6-member paper review council (Session 5, D-03). This is a dedicated scoring and methodology review council.

---

## Council Structure

### Composition Rationale

The 12-member council is organized in three tiers reflecting the interdisciplinary demands of critiquing a religious values benchmark scoring framework:

- **Tier 1 — Tradition-Specific Depth Auditors (4 members):** Domain experts who can evaluate whether the scoring framework captures genuine theological substance or rewards surface-level religious vocabulary. Each covers a tradition family where ground-truth problems have been identified.
- **Tier 2 — Measurement & Methods Specialists (4 members):** Psychometric, bibliometric, statistical, and implementation experts who evaluate the technical rigor of the 3-axis framework, the composite formula, and the feature matrix design.
- **Tier 3 — Infrastructure & Quality Assurance (4 members):** Experts in data discovery, sociological framing, East Asian coverage gaps, and overall paper methodology who ensure the framework is complete, reproducible, and fairly framed.

---

## Tier 1 — Tradition-Specific Depth Auditors

### Member 1: Dr. Nadia al-Rashidi

| Field | Detail |
|-------|--------|
| **Affiliation** | Associate Professor, Department of Information Systems, King Saud University |
| **Expertise** | Maqasid al-Shariah, computational fiqh, Islamic legal informatics, Arabic ontology engineering |
| **Council Role** | Islamic Depth Auditor |
| **Mandate** | Validate whether the 9/15 Islamic benchmarks in the Top 15 test jurisprudential reasoning (ijtihad, qiyas, istihsan) or merely test rule retrieval and factual recall. Assess whether the R2 (theological depth) scoring distinguishes between fiqh-as-calculation and fiqh-as-reasoning. Evaluate whether the Maqasid al-Shariah framework is appropriately operationalized in the feature matrix or reduced to a checklist. |
| **Key question** | Does the scoring framework reward Islamic benchmarks for genuine engagement with usul al-fiqh, or does it reward the availability of structured Islamic legal data that happens to be easy to format as MCQ items? |
| **Ground-truth assignments** | Review ELQV (Rank 1), Islamic Inheritance (Rank 2), QIAS 2025 (Rank 4), and the remaining 6 Islamic entries for knowledge-vs-reasoning classification. |

### Member 2: Dr. Sarah Goldberg

| Field | Detail |
|-------|--------|
| **Affiliation** | Associate Professor, Department of Computer Science, Bar-Ilan University |
| **Expertise** | Bar-Ilan Responsa Project, halakhic reasoning systems, Hebrew NLP, Sefaria digital library, Talmudic logic formalization |
| **Council Role** | Judaism Gap Specialist |
| **Mandate** | Investigate why Judaism --- the world's oldest computational humanities tradition, with the Responsa Project (1960s), Sefaria, and Talmudic logic formalization --- has zero values-alignment benchmarks in the corpus. Determine whether the hard gates (RD >= 30, public data) structurally exclude Jewish computational resources or whether the gap is a community coordination problem. Assess whether the scoring framework could accommodate halakhic reasoning formats (multi-voice argumentation, precedent chains, dissent structures) that do not map to standard MCQ/SCN/MIX formats. |
| **Key question** | Is the zero-benchmark finding for Judaism an artifact of the search strategy, the format taxonomy, or a genuine gap in the LLM evaluation community's engagement with Jewish computational scholarship? |
| **Ground-truth assignments** | Evaluate whether existing Jewish NLP resources (Sefaria API, Responsa corpus, Talmudic logic datasets) could pass the hard gates if reformulated as evaluation instruments. |

### Member 3: Dr. Venkatesh Raghavan

| Field | Detail |
|-------|--------|
| **Affiliation** | Professor, Department of Computer Science and Engineering, IIT Bombay |
| **Expertise** | Sanskrit NLP, Dharmic text processing, Indic language technology, Digital Corpus of Sanskrit, Pali/Hindi computational linguistics |
| **Council Role** | Dharmic Traditions Analyst |
| **Mandate** | Evaluate the repurposability of existing Sanskrit, Pali, and Hindi computational corpora for religious values benchmarking. Audit the Bhagavad Gita Sentiment Analysis benchmark (Rank 6) for source language fidelity --- whether it processes Sanskrit text, Hindi translations, or English translations, and whether the feature matrix's R3 (scriptural grounding) score reflects this distinction. Assess whether the scoring framework's text-centric assumptions disadvantage Dharmic traditions whose ethical reasoning is embedded in commentarial traditions (bhashya) rather than isolated proof-texts. |
| **Key question** | Does the scoring framework's emphasis on scriptural grounding (R3) and denominational awareness (R4) capture the Dharmic model of ethics, where moral reasoning flows through layered commentary traditions (Shankara, Ramanuja, Madhva on the Gita) rather than through direct scriptural citation? |
| **Ground-truth assignments** | Review the Bhagavad Gita benchmark for language fidelity; assess BuddhismEval (Rank 13) and GurbaniDB (Rank 14) for construct validity. |

### Member 4: Dr. Amina Diallo

| Field | Detail |
|-------|--------|
| **Affiliation** | Senior Lecturer, Department of Philosophy, University of Cape Town |
| **Expertise** | Ubuntu communitarian ethics, oral knowledge systems, decolonial AI, CARE Principles for Indigenous Data Governance, participatory design |
| **Council Role** | Epistemic Sovereignty Advisor |
| **Mandate** | Address whether the scoring framework's assumptions --- textual corpora, public data availability, individual-item evaluation --- are epistemically appropriate for traditions whose knowledge is transmitted orally, communally, and through embodied practice. Evaluate whether the 8-tradition void should be treated as a "gap to be filled" or as evidence that the benchmarking paradigm itself is structurally exclusionary. Assess whether the CARE Principles are adequately integrated into the framework's design and whether the hard gate on public data availability functions as a structural exclusion mechanism. |
| **Key question** | Should the paper recommend building benchmarks for oral/communal traditions, or should it argue that the benchmarking paradigm is fundamentally inappropriate for these traditions and propose alternative evaluation architectures? |
| **Ground-truth assignments** | Review Ubuntu Philosophy (4 candidates, 0 gate-passers) and Indigenous Spirituality (16 candidates, 0 gate-passers) for whether the zero-benchmark finding is a pipeline artifact or a genuine epistemic boundary. |

---

## Tier 2 — Measurement & Methods Specialists

### Member 5: Dr. James Chen

| Field | Detail |
|-------|--------|
| **Affiliation** | Associate Professor, Educational Testing Service (ETS), Princeton |
| **Expertise** | Item Response Theory (IRT), construct validity, measurement invariance, Differential Item Functioning (DIF), Classical Test Theory, computerized adaptive testing |
| **Council Role** | Psychometric Rigor Lead |
| **Mandate** | Provide formal psychometric critique of the 3-axis scoring framework. Evaluate whether the 22 features constitute a coherent measurement instrument with defensible construct validity, or whether they are an ad hoc collection of indicators without psychometric grounding. Assess the composite formula's weighting scheme (40/35/25) for theoretical justification, sensitivity to perturbation, and potential for rank instability. Evaluate whether the R2 (theological depth) 1-5 ordinal scale has adequate discrimination and whether the calibration anchors are psychometrically sound. |
| **Key question** | If this scoring framework were submitted to a psychometric review panel, would it pass construct validity scrutiny, or would it be returned for fundamental redesign? |
| **Ground-truth assignments** | Formal analysis of the composite formula's sensitivity to weight perturbation; evaluation of R2 distribution collapse (85% scoring depth=1); assessment of measurement invariance across tradition families. |

### Member 6: Dr. Priya Mehta

| Field | Detail |
|-------|--------|
| **Affiliation** | Assistant Professor, School of Information, University of Michigan |
| **Expertise** | Bibliometrics, network science, systematic review methodology, meta-analysis, research synthesis |
| **Council Role** | Computational Analysis Lead |
| **Mandate** | Evaluate the systematic review methodology (PRISMA compliance, search strategy completeness, inclusion/exclusion criteria). Assess the Citation Impact axis for bibliometric rigor: whether age-normalized citations (C2) adequately correct for field recency, whether venue classification (C3) is defensible, and whether C4 (downstream adoption) and C5 (leaderboard presence) are measurable or aspirational. Flag any systematic review methodology gaps that would be caught by peer review at NeurIPS D&B. |
| **Key question** | Does the CI axis measure actual scholarly influence, or does it primarily measure the age and venue prestige of the benchmark, rewarding incumbency over innovation? |
| **Ground-truth assignments** | Audit C4/C5 data completeness (suspected always-zero); evaluate search strategy coverage (missing Google Scholar, PapersWithCode); assess PRISMA flow diagram compliance. |

### Member 7: Dr. Marcus Rivera

| Field | Detail |
|-------|--------|
| **Affiliation** | Research Scientist, Allen Institute for AI (AI2), Seattle |
| **Expertise** | lm-eval-harness architecture, Inspect AI, HELM, evaluation harness design, benchmark implementation, reproducibility engineering |
| **Council Role** | Benchmark Implementation Expert |
| **Mandate** | Evaluate the Practical Ease axis from the perspective of someone who would actually implement these benchmarks. Assess whether P7 (implementability composite, weight 30% of PE) captures real-world harness integration difficulty or is a proxy that conflates format compatibility with implementation effort. Evaluate the format taxonomy's 12 codes for completeness and mutual exclusivity. Assess whether the PE axis rewards benchmarks that are easy to plug into existing harnesses over benchmarks that require novel evaluation approaches but produce more meaningful measurements. |
| **Key question** | Does the PE axis measure genuine practical ease of implementation, or does it measure conformity to existing harness architectures --- thereby penalizing innovative evaluation designs that may better capture religious values? |
| **Ground-truth assignments** | Review PE computation bug (P7 * 10 vs. 6-feature formula); evaluate harness compatibility ratings for the Top 15; assess whether GurbaniDB (Rank 14, a database) should have a PE score at all. |

### Member 8: Dr. Fatima Zahra

| Field | Detail |
|-------|--------|
| **Affiliation** | Assistant Professor, Department of the Study of Religions, SOAS University of London |
| **Expertise** | Sociology of religion, World Values Survey, cross-cultural measurement, WEIRD critique, religion-as-lived-practice |
| **Council Role** | Tradition Coverage Analyst |
| **Mandate** | Evaluate the 14-tradition taxonomy for sociological adequacy. Assess whether the tradition categories are mutually exclusive and collectively exhaustive, or whether they reflect Western academic categories that may not map onto practitioners' self-understanding. Evaluate the "tradition family" groupings (Abrahamic, Dharmic, East Asian, African/Indigenous, Other) for sociological defensibility. Flag traditions that are absent from the taxonomy entirely (e.g., Sikhism is included but not as a family; new religious movements are absent; folk/syncretic traditions are invisible). Assess the WEIRD critique for empirical grounding. |
| **Key question** | Does the 14-tradition taxonomy reflect the actual diversity of religious engagement with AI, or does it reflect the categories that Western religious studies departments use to organize their curricula? |
| **Ground-truth assignments** | Evaluate Break the Checkbox (Rank 5) for whether it tests religious values or secular cultural dimensions; review the tradition assignment methodology for external search papers. |

---

## Tier 3 — Infrastructure & Quality Assurance

### Member 9: Dr. Kenji Tanaka

| Field | Detail |
|-------|--------|
| **Affiliation** | Associate Professor, Graduate School of Letters, Kyoto University |
| **Expertise** | Shinto studies, Japanese NLP, East Asian philosophy of technology, CValues benchmark, Confucian ethics |
| **Council Role** | East Asian Gap Specialist |
| **Mandate** | Investigate the near-total absence of East Asian traditions from the benchmark corpus (Confucianism: 1 gate-passer at the lowest composite score; Taoism: 0; Shinto: 0). Evaluate whether the search strategy's English-language bias missed Japanese, Chinese, and Korean religious values evaluation work. Assess the Confucian Analects benchmark (Rank 15) for whether it is an implemented evaluation instrument or a theoretical proposal. Evaluate whether CValues and similar Chinese-language benchmarks contain religious values dimensions that the tradition assignment methodology failed to capture. |
| **Key question** | Is the East Asian void a genuine gap in the field, or is it an artifact of an English-centric search strategy that missed substantial work in Japanese, Chinese, and Korean NLP communities? |
| **Ground-truth assignments** | Review the Confucian Analects benchmark (Rank 15) for implementation status; assess whether CValues (Tao et al. 2024) contains religious or philosophical values dimensions. |

### Member 10: Dr. Elena Volkov

| Field | Detail |
|-------|--------|
| **Affiliation** | Senior Data Scientist, HuggingFace, Paris |
| **Expertise** | Dataset curation, open science infrastructure, HuggingFace Hub dataset discovery, dataset documentation (datasheets), licensing |
| **Council Role** | Data Discovery Specialist |
| **Mandate** | Evaluate the data availability assessment methodology. Determine whether the "publicly available data" hard gate was assessed using systematic methods (HuggingFace API search, GitHub repository verification) or ad hoc checks. Assess whether the 77% data unavailability rate is an accurate measurement or an artifact of incomplete search. Evaluate the licensing dimension (P5) for whether it captures the actual reusability of datasets or merely records the stated license. Identify datasets on HuggingFace that may have been missed by the search strategy. |
| **Key question** | Is the data availability bottleneck as severe as the paper claims (77% eliminated), or has the search methodology underestimated the true availability of religious benchmark data? |
| **Ground-truth assignments** | Verify data availability claims for the Top 15; assess whether HuggingFace API rate limiting (acknowledged in Section 3.6) systematically biased the data availability assessment. |

### Member 11: Dr. Robert Okafor

| Field | Detail |
|-------|--------|
| **Affiliation** | Professor, Department of Statistics, University of Ibadan |
| **Expertise** | Multi-criteria decision analysis (MCDA), sensitivity analysis, bootstrap methods, rank stability, decision theory under uncertainty |
| **Council Role** | Scoring Framework Critic |
| **Mandate** | Provide a formal decision-analytic critique of the composite scoring framework. Evaluate the 40/35/25 weighting scheme using sensitivity analysis: how much do the weights need to change before the Top 15 ranking changes? Assess whether the hard gates (RD >= 30, data available) are appropriately calibrated or whether they are arbitrary thresholds that create discontinuities. Evaluate the normalization methodology (all axes to 0-100) for whether it preserves ordinal relationships. Assess the diversity constraints for formal defensibility. |
| **Key question** | Is the composite ranking robust to reasonable perturbation of the weighting scheme, or do small weight changes produce substantial rank instability --- suggesting that the specific ranking is an artifact of the chosen weights rather than a stable ordering? |
| **Ground-truth assignments** | Sensitivity analysis of the 40/35/25 weights; evaluation of the RD >= 30 threshold; assessment of the CI dead weight problem (C4/C5 always zero). |

### Member 12: Dr. Maria Theresa Santos

| Field | Detail |
|-------|--------|
| **Affiliation** | Associate Professor, Department of English and Comparative Literature, University of the Philippines Diliman |
| **Expertise** | Scientific writing, PRISMA methodology, academic argumentation, systematic review reporting standards, NeurIPS D&B submission guidelines |
| **Council Role** | Methodology & Paper Critic |
| **Mandate** | Evaluate the paper's overall methodological coherence, argumentation structure, and compliance with NeurIPS D&B reporting standards. Assess whether the seven claims are adequately supported by evidence, whether the limitations section is honest and complete, and whether the paper's framing fairly represents the field. Flag any gaps between what the paper claims and what the evidence supports. Evaluate the relationship between the 3-axis framework and the 7 meta-evaluation criteria for redundancy and complementarity. |
| **Key question** | If submitted to NeurIPS D&B as-is, what would the most likely reviewer objections be, and which are addressable within the current framework? |
| **Ground-truth assignments** | Evaluate claim-evidence alignment for all 7 claims; assess PRISMA compliance; review the limitations section for completeness. |

---

## Operating Protocol

### Anti-Essentialization Guardrails

All council members are bound by the following anti-essentialization rules, carried forward from the background literature council (Session 3) and the paper review council (Session 5):

1. **No tradition-as-agent constructions.** Never write "Islam believes X" or "Judaism requires Y." Always attribute to scholars, frameworks, or communities: "Islamic ethics scholarship argues X," "the Maqasid framework holds X," "the Jewish computational scholarship community has produced Y."

2. **No monolithic tradition claims.** Always acknowledge intra-tradition diversity. Islam includes Sunni, Shia, Ibadi, and Sufi perspectives; Christianity includes Catholic, Orthodox, Protestant, and Restorationist; Hinduism includes Advaita, Vishishtadvaita, Dvaita, and other darshana. Scoring critiques must not imply that a tradition has a single "correct" view that a benchmark should capture.

3. **No deficit framing for absent traditions.** The 8-tradition void is a finding about infrastructure, not about the traditions themselves. Never imply that absent traditions lack ethical sophistication. Always distinguish between "no benchmark exists" and "the tradition's ethical framework is underdeveloped."

4. **No implied hierarchy of traditions.** Islam's benchmark dominance reflects infrastructure investment and fiqh formalizability, not theological superiority. The scoring framework critique must not imply that traditions with high composite scores are more important than those with zero benchmarks.

5. **Source language sensitivity.** When discussing sacred texts (Quran, Torah, Vedas, Pali Canon, Analects), always specify the source language and note whether benchmarks process original-language text or translations. Never assume English is the default.

### Decision Protocol

| Decision Type | Threshold | Process |
|---------------|-----------|---------|
| **Consensus findings** | Unanimous or near-unanimous (11/12+) | Preferred for all cross-cutting themes and major recommendations |
| **Domain deference** | Tier 1 experts have authority on tradition-specific claims | When a Tier 1 expert's assessment conflicts with a Tier 2/3 expert on a tradition-specific matter, the Tier 1 expert's view prevails unless overridden by empirical evidence |
| **Formal votes** | 7/12 majority (simple majority + 1) | Used only when consensus cannot be reached after deliberation |
| **Recorded dissent** | Any member may file | Dissenting views are recorded in the deliberation document with full reasoning; they are not suppressed or minimized |
| **Veto** | Tier 1 experts on their tradition | A Tier 1 tradition expert may veto any claim about their tradition that they judge to be factually incorrect or essentializing |
| **Bug confirmations** | Empirical verification | Code-level bugs in `build_religious_feature_matrix.py` are confirmed or rejected based on code review, not by vote |

### Deliberation Sequence

| Deliberation | Topic | Status |
|--------------|-------|--------|
| **D-01** | Critique of existing methods and scoring framework | THIS SESSION |
| **D-02** | 109-feature taxonomy evaluation and feature selection | Future |
| **D-03** | Revised scoring framework design | Future |
| **D-04** | Re-ranking with revised framework | Future |

---

## Cross-References

| Document | File | Relationship |
|----------|------|-------------|
| Background Literature Council | `BACKGROUND/20260403-background-handoff.md` | Session 3; 14-member council, different composition |
| Paper Review Council (D-02) | `council-deliberation-intro-review.md` | Session 4; 12-member council (same numbering, different members) |
| Paper Review Council (D-03) | `20260404-council-deliberation-full-review.md` | Session 5; 6-member subset |
| Paper Spine | `spine-religious-values.md` | Shared contract for all writing agents |
| Session 5 Handoff | `20260404-paper-session5-handoff.md` | Prior session state |
| Full Paper | `full-paper-religious-values.md` | Canonical paper file under critique |
| Feature Matrix Script | `scripts/build_religious_feature_matrix.py` | Implementation under audit |

---

## Council Member Quick Reference

| # | Name | Role | Tier | Tradition/Domain |
|---|------|------|------|-----------------|
| 1 | Dr. Nadia al-Rashidi | Islamic Depth Auditor | 1 | Islam |
| 2 | Dr. Sarah Goldberg | Judaism Gap Specialist | 1 | Judaism |
| 3 | Dr. Venkatesh Raghavan | Dharmic Traditions Analyst | 1 | Dharmic |
| 4 | Dr. Amina Diallo | Epistemic Sovereignty Advisor | 1 | African/Indigenous |
| 5 | Dr. James Chen | Psychometric Rigor Lead | 2 | Measurement |
| 6 | Dr. Priya Mehta | Computational Analysis Lead | 2 | Bibliometrics |
| 7 | Dr. Marcus Rivera | Benchmark Implementation Expert | 2 | Implementation |
| 8 | Dr. Fatima Zahra | Tradition Coverage Analyst | 2 | Sociology |
| 9 | Dr. Kenji Tanaka | East Asian Gap Specialist | 3 | East Asian |
| 10 | Dr. Elena Volkov | Data Discovery Specialist | 3 | Infrastructure |
| 11 | Dr. Robert Okafor | Scoring Framework Critic | 3 | Statistics |
| 12 | Dr. Maria Theresa Santos | Methodology & Paper Critic | 3 | Writing/Methods |
