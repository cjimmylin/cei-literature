# Paper Spine v2 — Shared Contract for All Writing Agents

## Title
**Three Ethical Profiles, One Knowledge Ceiling: A Meta-Evaluation of 54 Normative Ethics Benchmarks Across Nine LLMs and Three Vendors**

## Authors
Jimmy Lin, Center for Ethical Intelligence

## Venue Target
General academic journal format (no length constraints)

---

## 12-Member Expert Council

| # | Perspective | Primary Sections | Role |
|---|------------|-----------------|------|
| 1 | RLHF / Alignment Training | 5.3 (Three Profiles), 5.5 (Persuasion) | How training intensity maps to moral posture |
| 2 | Moral Psychology / Dual-Process | 5.2 (Consequentialist Bias), 5.4 (K-J Divergence) | System 1/2 interpretation of IB-IH gap |
| 3 | NLP Evaluation / Psychometrics | 3 (Methods), 6 (Limitations) | Statistical rigor, effective battery size |
| 4 | ML Systems / Distributed Inference | 5.6 (Gemini Identity) | Routing/infrastructure hypothesis |
| 5 | Normative Ethics / Kantian | 5.2 (Bias Discussion), 5.3 (Profiles) | Philosophical precision on duty-based reasoning |
| 6 | Consequentialist Ethics | 5.2 (Bias Discussion), 5.3 (Profiles) | Counterpoint: permissive profile isn't wrong |
| 7 | AI Policy / Deployment Safety | 5.7 (Policy), 7 (Conclusion) | Governance recommendations |
| 8 | Benchmark Security / Data Contamination | 5.1 (Ceiling), 6 (Limitations) | Contamination vs. capability distinction |
| 9 | Cross-Cultural Moral Psychology | 4.1 (Landscape), 5.9 (Western Bias) | Non-Western gaps, cultural contingency |
| 10 | Biostatistics / Agreement Analysis | 3.5 (Stats), 4.6 (Cross-Vendor) | CIs, effect sizes, chance-corrected metrics |
| 11 | Educational Measurement / IRT | 4.3 (Trials), 5.4 (K-J Construct) | Item difficulty, discriminative power |
| 12 | Science Communication | All figures, 5.6 (Gemini Disclosure) | Responsible disclosure framing, narrative clarity |

---

## Narrative Arc (Four Movements)

1. **The Landscape** (Sec 3-4.2): Establish the problem, describe methodology, reveal 54-benchmark atlas. Tradition voids, ND-PE tradeoffs, reasoning deficit, data bottleneck.
2. **The Empirical Validation** (Sec 4.3-4.4): Single-model trials transform the static landscape into dynamic findings. Ceiling confirmed, consequentialist bias measured, discriminative power inverted vs. composite rank.
3. **The Revelation** (Sec 4.5-4.6): Cross-vendor analysis produces the central surprise — models cluster by ethical profile (Conservative/Moderate/Permissive), not vendor. Knowledge converges; judgment diverges. Gemini models identical. Question shifts: "how many benchmarks?" to "how many ethical voices?"
4. **The Implications** (Sec 5-7): 12 council perspectives unpack what this means for benchmark design, AI governance, and the field's future.

---

## Five Core Claims (Updated for n=54)

1. **Ceiling Effect:** ETHICS produces 100% accuracy on frontier LLMs across all 9 models tested (p < 1e-15, binomial). Saturated benchmarks should be retired.
2. **Consequentialist Bias:** LLMs achieve 77% utilitarian vs. 50% deontological accuracy (z=2.17, p=0.015, Cohen's h=0.57). Confirmed across vendors.
3. **Care/Contractarian Void:** Only 2/54 care ethics and 4/54 contractarian benchmarks reach substantive engagement. Genuine research void.
4. **Reasoning Deficit:** Only 10/54 (19%) test moral reasoning; 44 (81%) test judgment only (p < 0.001, binomial).
5. **Data Bottleneck:** No significant ND difference between available and unavailable benchmarks (Mann-Whitney p=0.605). The gate reflects sociology, not quality.

## Seven Cross-Vendor Findings (NEW)

- **F1:** Three ethical profiles: Conservative (GPT-5, Opus; IH~3.0), Moderate (Sonnet, GPT-5-mini; IH~3.2), Permissive (Haiku, all Gemini; IH~4.47)
- **F2:** All 4 Gemini models = 100% identical on 114 items (p ~ 10^-103)
- **F3:** Universal knowledge ceiling: 8/8 models at 100% on 4 benchmarks (44/114 items = 38.6%)
- **F4:** Knowledge-judgment divergence: 0% variance on knowledge vs. up to 33/55 items disagreement on judgment (12/12 council unanimous)
- **F5:** GPT-5 most conservative: IH=2.93, IB=5.13, gap=2.20 (largest), persuasion change=0%
- **F6:** Cross-vendor clustering by profile, not vendor: Sonnet-GPT5 90.4% > Sonnet-Haiku 74.6%
- **F7:** Persuasion resistance non-monotonic: Opus 66.7% > Haiku 33.3% > Sonnet 0%

---

## Terminology Glossary

| Term | Definition |
|------|-----------|
| **Normative Depth (ND)** | 0-100 score measuring philosophical rigor. Weighted 40% in composite. |
| **Practical Ease (PE)** | 0-100 score measuring implementability. Weighted 35%. |
| **Citation Impact (CI)** | 0-100 score measuring community influence. Weighted 25%. |
| **Composite Score** | ND x 0.40 + PE x 0.35 + CI x 0.25. Range 0-100. |
| **Hard Gate** | ND >= 40 AND publicly available data. 24/54 pass both. |
| **Discriminative Power** | Whether a benchmark produces meaningful variance across models. |
| **Ceiling Effect** | Benchmark too easy for current models; near-perfect scores, no variance. |
| **Procedural Reasoning** | Evaluating *how* a model reasons morally, not just *what* it concludes. |
| **Framework Difficulty Hierarchy** | U=77% > V=63% > D=50% accuracy pattern. |
| **Tradition** | Five normative frameworks: Virtue (V), Deontological (D), Utilitarian (U), Care (C), Contractarian (Co). |
| **Ethical Profile** | NEW: Conservative/Moderate/Permissive classification based on IH, CBR, and persuasion metrics. |
| **IH (Instrumental Harm)** | NEW: OUS subscale measuring willingness to accept harm for greater good (1-7 scale). |
| **IB (Impartial Beneficence)** | NEW: OUS subscale measuring endorsement of equal moral concern (1-7 scale). |
| **CBR (Cognitive Bias Rate)** | NEW: Percentage of PNAS moral dilemmas where model exhibits cognitive biases. |
| **Knowledge-Judgment Divergence** | NEW: Pattern where models converge on knowledge items but diverge on judgment items. |

---

## Section Structure and File Assignment

| File | Sections | Council Perspectives |
|------|----------|---------------------|
| `abstract-normeval-v2.md` | Abstract (~450 words) | All 12 (synthesis) |
| *(Introduction not rewritten)* | Sec 1-2 preserved from v1 | — |
| `methods-normeval-v2.md` | Sec 3.1-3.7 (~3,500 words) | 3 (Psychometrics), 10 (Biostatistics) |
| `results-landscape-normeval-v2.md` | Sec 4.1-4.2 (~2,000 words) | 9 (Cross-Cultural), 11 (IRT) |
| `results-trials-normeval-v2.md` | Sec 4.3-4.4 (~1,500 words) | 11 (IRT), 8 (Contamination) |
| `results-crossvendor-normeval-v2.md` | Sec 4.5-4.6 (~3,000 words) | 1 (RLHF), 2 (MoralPsych), 4 (ML Systems), 10 (Biostats) |
| `discussion-normeval-v2.md` | Sec 5.1-5.9 (~6,000 words) | All 12 |
| `limitations-normeval-v2.md` | Sec 6.1-6.2 (~1,000 words) | 3 (Psychometrics), 8 (Security) |
| `conclusion-normeval-v2.md` | Sec 7.1-7.3 (~1,000 words) | 7 (Policy), 12 (SciComm) |
| `references-normeval-v2.md` | Bibliography (~200+ entries) | — |

---

## Figure & Table Assignments

### Main Body

| ID | Type | Section | Description |
|----|------|---------|-------------|
| **Figure 1** | Heatmap (54x5) | 4.1 | Tradition coverage: 54 benchmarks x 5 traditions. Gate-pass separator line. |
| **Figure 2** | Grouped bar | 4.3 | Framework difficulty: U=77%, V=63%, D=50% |
| **Figure 3** | Bubble scatter | 4.1 | ND vs PE, bubble=log(citations), color=gate status |
| **Figure 4** | Stacked bar | 4.1 | Data availability by host type |
| **Figure 5** | Paired bar | 4.3 | Accuracy vs discriminative power, 15 trials |
| **Figure 6** | Grouped bar | 4.6 | IH/IB scaling across 9 models + reference lines |
| **Figure 7** | Heatmap (8x8) | 4.6 | Cross-vendor pairwise agreement matrix |
| **Figure 8** | Dumbbell | 4.6 | Knowledge vs judgment agreement ranges by trial |
| **Table 1** | Table | 3.2 | Feature matrix: 4 axes, 26 features, example values |
| **Table 2** | Table | 4.2 | Top 24 gate-passing benchmarks ranked by composite |
| **Table 3** | Table | 4.3 | 15 trial results: accuracy, discriminative power, key finding |
| **Table 4** | Table | 4.6 | Seven cross-vendor findings: evidence and significance |

### Supplement

| ID | Appendix | Description |
|----|----------|-------------|
| **Table S1** | A | Complete 54x26 feature matrix |
| **Table S2** | B | Scoring formulas and calibration anchors |
| **Tables S3-S7** | C | Per-trial item-level results (T1-T5) |
| **Tables S8-S17** | D | Per-trial item-level results (T6-T15, all 9 models) |
| **Table S18** | E | Benchmarks 25-54: below-cutoff with gate failure reasons |
| **Table S19** | F | Cross-harness implementability (54x6) |
| **Tables S20-S21** | G | Hypothesis tests (C1-C5) + pairwise CIs |
| **Table S22** | H | Care ethics prototype: 10 scenarios, Tronto 4-dimension scores |
| **Figures S1-S2** | I | v2 feature distributions + non-Western engagement heatmap |

---

## Core Citation Keys

### Top 15 Benchmarks
- [Hendrycks2021] ETHICS — ICLR 2021
- [Chiu2025] MoReBench — 2025
- [Hong2025] PrinciplismQA — 2025
- [Huang2024] Moral Persuasion — 2024
- [An2025] MoralReason-QA — AAAI 2025
- [Samway2025] Moral Lens — EMNLP 2025
- [Galatolo2025] Beyond Ethical Alignment — 2025
- [Takeshita2025] JETHICS — 2025
- [Russo2025] Pluralistic Moral Gap — 2025
- [ChiuDD2024] DailyDilemmas — ICLR 2025
- [Wei2025] MedEthicsQA — 2025
- [Kumar2025] UniMoral — ACL 2025
- [Marraffini2024] Greatest Good — 2024
- [Cheung2025] PNAS Cognitive Biases — 2025
- [Thomas2026] ProMoral-Bench — 2026

### Foundational Works
- [Rawls1971] A Theory of Justice
- [Gilligan1982] In a Different Voice
- [MacIntyre1981] After Virtue
- [Scanlon1998] What We Owe to Each Other
- [Kahane2012] Kahane et al. — Utilitarian philosophers (OUS reference population)

### Meta-Analyses & Meta-Benchmarks
- [Snoswell2025] 69-paper LLM ethics evaluation survey
- [Rismani2025] 791 AI ethics evaluation measures
- [Liang2022] HELM
- [Wang2023] DecodingTrust
- [Sun2024] TrustLLM

---

## Writing Guidelines

1. **No length constraints.** Capture all information, data, and analysis.
2. **Use discipline-based council labels** (e.g., "the RLHF perspective"), not fabricated expert names.
3. **All statistics must include:** test type, statistic value, p-value, effect size, sample size.
4. **n=54 throughout.** Never reference "37 benchmarks" — that was the v1 corpus.
5. **24 gate-passing benchmarks** (not 15 — that was v1).
6. **Cross-references:** Use `Figure N`, `Table N`, `Section N.N`, `Table SN` consistently.
7. **Citation format:** `[AuthorYear]` for inline references.
8. **Markdown format:** Standard academic markdown. Use `>` for block quotes of formulas. Use `**bold**` for terms on first definition. Use `---` for section breaks.
