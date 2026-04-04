# Paper Spine — Shared Contract for All Writing Agents

## Title
**What Do Normative Ethics Benchmarks Actually Test? A Meta-Evaluation of 37 LLM Moral Reasoning Assessments**

## Authors
Jimmy Lin, Center for Ethical Intelligence

## Venue Target
NeurIPS 2026 Datasets & Benchmarks Track (8pp main + unlimited appendix)

---

## Five Key Claims

1. **Ceiling Effect:** The field's most-cited normative ethics benchmark (ETHICS, Hendrycks et al. 2021; 843 citations) produces 100% accuracy on frontier LLMs, rendering it unable to discriminate between models. Saturated benchmarks should be retired from active evaluation or replaced by their hard-test variants.

2. **Consequentialist Bias:** LLMs are measurably more consequentialist than deontological — achieving 77% accuracy on utilitarian reasoning vs. 50% on deontological reasoning in our implementation trials (MoralReason-QA). Virtue ethics is consistently the hardest tradition to operationalize across all benchmarks tested.

3. **Care/Contractarian Lacuna:** No dedicated care ethics (Gilligan/Noddings) or contractarian (Rawls/Scanlon) LLM benchmark exists anywhere in the published literature. This is not a data gap in our survey — it is a genuine research void in the field. The closest approximation is PrinciplismQA (Beauchamp-Childress medical ethics), which engages beneficence but not relational ethics.

4. **Judgment vs. Reasoning:** Only 10 of 37 benchmarks (27%) make any attempt to evaluate moral *reasoning* (how a model arrives at its conclusion); the remaining 27 (73%) test moral *judgment* — what the model concludes — either exclusively (22 benchmarks) or alongside limited reasoning assessment (5 benchmarks) (p = 0.004, binomial test). MoReBench is the sole benchmark achieving a 5/5 philosophical grounding score by testing procedural reasoning with expert rubric criteria — and it is genuinely difficult (10% rubric coverage for frontier models).

5. **Data Bottleneck:** 12 of 37 benchmarks (32%) have no publicly available data, including several with the highest normative depth scores (Chakraborty ND=83, Rao ND=80, Zhou ND=72). Data availability, not benchmark quality, is the field's primary practical bottleneck.

---

## Terminology Glossary

| Term | Definition | First Use |
|------|-----------|-----------|
| **Normative Depth (ND)** | Composite score (0-100) measuring how rigorously a benchmark engages normative ethical philosophy. Weighted 40% in composite. | Section 3.1 |
| **Practical Ease (PE)** | Composite score (0-100) measuring how readily a benchmark can be implemented today (data availability, harness compatibility, code access). Weighted 35%. | Section 3.1 |
| **Citation Impact (CI)** | Composite score (0-100) measuring a benchmark's influence in the research community (age-normalized citations, downstream adoption, venue tier). Weighted 25%. | Section 3.1 |
| **Composite Score** | ND×0.40 + PE×0.35 + CI×0.25. Range 0-100. | Section 3.2 |
| **Hard Gate** | Binary inclusion criterion: ND ≥ 40 AND data publicly available. Benchmarks failing either gate are excluded regardless of composite score. | Section 3.2 |
| **Discriminative Power** | Whether a benchmark produces meaningful variance across models/items — a benchmark where all models score 100% has zero discriminative power. | Section 4.3 |
| **Ceiling Effect** | When a benchmark is too easy for current models, producing near-perfect scores with no variance. Identified in ETHICS (Hendrycks 2021). | Section 4.3 |
| **Procedural Reasoning** | Evaluating *how* a model reasons morally (identifying principles, weighing tradeoffs, articulating justifications) rather than *what* it concludes. Tested by MoReBench. | Section 4.3 |
| **Framework Difficulty Hierarchy** | The empirical finding that LLMs handle utilitarian reasoning (77%) better than virtue (63%) and deontological (50%). | Section 4.3 |
| **Tradition** | One of the 5 normative ethical frameworks scored: Virtue (V), Deontological (D), Utilitarian (U), Care (C), Contractarian (Co). | Throughout |

---

## Figure & Table Assignments

### Main Body

| ID | Type | Section | Description |
|----|------|---------|-------------|
| **Table 1** | Table | 3.1 | Feature matrix axes: 4 tiers (A/B/C/D), 26 features, example values |
| **Figure 1** | Heatmap | 4.1 | 37 benchmarks × 5 traditions. Color = score 0-100. Shows care/contractarian void. |
| **Figure 2** | Grouped bar | 4.3 | Framework difficulty: U=77%, V=63%, D=50% (from MoralReason-QA trial) |
| **Figure 3** | Scatter+bubble | 4.1 | ND (x) vs PE (y), bubble size = log(citations+1). Labels for Top 5. |
| **Table 2** | Table | 4.2 | Top 15 ranking: Rank, Name, Year, ND, PE, CI, COMP, Traditions, Size |
| **Table 3** | Table | 4.3 | Trial results: 5 rows (benchmark, items, accuracy, disc. power, verdict) |
| **Figure 4** | Stacked bar | 4.1 | Data availability: GitHub/HF/Public vs Unavailable, broken by reason |

### Supplement

| ID | Type | Appendix | Description |
|----|------|----------|-------------|
| **Table S1** | Full table | A | Complete 37×26 feature matrix |
| **Table S2** | Table | B | Scoring formula coefficients and calibration anchors |
| **Tables S3-S7** | Tables | C | Per-trial item-level results |
| **Table S8** | Table | D | Benchmarks 16-37 with gate failure reasons |
| **Table S9** | Table | F | Cross-harness implementability (37×6 matrix) |

---

## Section Assignment Map

| File | Sections | Written By |
|------|----------|------------|
| `introduction-normeval.md` | Abstract + Sec 1 (Intro) + Sec 2 (Related Work) | Agent F (Phase 2a) |
| `methods-normeval.md` | Sec 3 (Methods) | Agent A (Phase 1) |
| `results-normeval.md` | Sec 4.1-4.2 (Landscape + Top 15) by Agent B; Sec 4.3-4.4 (Trials + Cross-bench) by Agent C | Agents B+C (Phase 1) |
| `discussion-normeval.md` | Sec 5 (Discussion) + Sec 6 (Conclusion) | Agent G (Phase 2b) |
| `references-normeval.md` | Bibliography | Agent E (Phase 1) |
| `supplement-normeval.md` | Appendices A-F | Agent D (Phase 1) |

---

## Core Citation Keys

### Benchmark Papers (Top 15, cite by rank)
- [Hendrycks2021] Hendrycks et al. "Aligning AI with Shared Human Values" ICLR 2021
- [Chiu2025] Chiu et al. "MoReBench: Evaluating Procedural and Pluralistic Moral Reasoning" 2025
- [Hong2025] Hong et al. "PrinciplismQA" 2025
- [Huang2024] Huang et al. "Moral Persuasion in Large Language Models" 2024
- [An2025] An et al. "MoralReason" 2025
- [Samway2025] Samway et al. "Are Language Models Consequentialist or Deontological" 2025
- [Galatolo2025] Galatolo et al. "Beyond Ethical Alignment" 2025
- [Takeshita2025] Takeshita et al. "JETHICS" 2025
- [Russo2025] Russo et al. "The Pluralistic Moral Gap" 2025
- [ChiuDD2024] Chiu et al. "DailyDilemmas" ICLR 2025
- [Wei2025] Wei et al. "MedEthicsQA" 2025
- [Kumar2025] Kumar et al. "UniMoral" ACL 2025
- [Marraffini2024] Marraffini et al. "The Greatest Good Benchmark" 2024
- [Cheung2025] Cheung et al. "LLMs Amplified Cognitive Biases" PNAS 2025
- [Thomas2026] Thomas et al. "ProMoral-Bench" 2026

### Meta-Analyses & Surveys
- [Ray2023] Ray "Benchmarking ethical alignment" 2023
- [Snoswell2025] Snoswell et al. "69-paper LLM ethics evaluation survey" 2025
- [Rismani2025] Rismani et al. "791 AI ethics evaluation measures" 2025
- [Rauh2024] Rauh et al. (DeepMind) "Gaps in safety evaluation" 2024

### Meta-Benchmarks
- [Liang2022] Liang et al. "HELM" 2022
- [Srivastava2022] Srivastava et al. "BIG-Bench" 2022
- [Wang2023] Wang et al. "DecodingTrust" 2023
- [Sun2024] Sun et al. "TrustLLM" 2024

### Foundational Ethics
- [BeauchampChildress] Beauchamp & Childress "Principles of Biomedical Ethics"
- [Gilligan1982] Gilligan "In a Different Voice" 1982
- [Rawls1971] Rawls "A Theory of Justice" 1971
- [Scanlon1998] Scanlon "What We Owe to Each Other" 1998
- [MacIntyre1981] MacIntyre "After Virtue" 1981

### Methodology
- [Ethayarajh2020] Ethayarajh & Jurafsky "Utility is not sufficient" 2020
- [Rottger2025] Rottger et al. "SafetyPrompts: Systematic review of open safety evaluation datasets" 2025

---

## Word Budget

| Section | Target | Max |
|---------|--------|-----|
| Abstract | 200 | 250 |
| 1. Introduction | 800 | 900 |
| 2. Related Work | 500 | 600 |
| 3. Methods | 1,000 | 1,200 |
| 4. Results | 1,800 | 2,000 |
| 5. Discussion | 1,200 | 1,400 |
| 6. Conclusion | 400 | 500 |
| **TOTAL** | **5,900** | **6,850** |
