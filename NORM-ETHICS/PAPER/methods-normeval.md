## 3. Methods

### 3.1 Benchmark Corpus Assembly

We assembled the evaluation corpus in two stages. First, we drew on the CEI Literature Vault, a curated collection of 2,043 AI ethics papers, in which 31 had been tagged as normative ethics benchmarks through prior manual review (20 confirmed, 11 borderline). Second, we conducted a PRISMA-compliant systematic search across seven databases — arXiv, Semantic Scholar, ACL Anthology, Google Scholar, PapersWithCode, OpenReview, and HuggingFace Hub — using ten query sets that combined terms for normative ethics, moral reasoning, and LLM evaluation (e.g., *"care ethics benchmark LLM"*, *"contractarian moral evaluation language model"*). We deliberately over-sampled queries targeting care ethics [Gilligan1982] and contractarian ethics [Rawls1971, Scanlon1998] to compensate for their anticipated under-representation.

The search returned 20 external candidates after deduplication against the vault. Of these, 6 met inclusion criteria (peer-reviewed or posted on a recognized preprint server; explicitly evaluating LLMs on normative ethical reasoning; published 2021–2026) and were ingested into the vault. The remaining 14 were excluded for lacking normative ethics content, duplicating existing entries, or evaluating only descriptive moral psychology without normative framing. The final corpus comprises 37 benchmarks spanning 2021–2026.

### 3.2 Feature Matrix Design

We characterized each benchmark along 26 features organized into four axes (Table 1): **Normative Depth** (A1–A8), measuring philosophical rigor; **Practical Ease** (B1–B9), measuring implementability; **Citation Impact** (C1–C5), measuring community influence; and **Metadata** (D1–D4), recording provenance.

Normative Depth features capture the number of ethical traditions tested (A1), the depth of ethical engagement from surface-level to framework-grounded scenarios (A2), whether the benchmark tests moral judgment or moral reasoning (A3), treatment of moral uncertainty (A4), pluralistic coverage of competing perspectives (A5), philosophical grounding on a 1–5 scale (A6), cultural framing (A7), and multilingual support (A8). Practical Ease features record task format (B1), dataset size (B2), data availability (B3), code availability (B4), license terms (B5), harness compatibility across six evaluation frameworks (B6), an overall implementability score (B7), scorer type (B8), and model compatibility (B9). Citation Impact features include raw citation count (C1), age-normalized citations per year (C2), venue tier (C3), downstream adoption count (C4), and leaderboard presence (C5).

To mitigate subjectivity in the most consequential feature — philosophical grounding (A6) — we calibrated against three anchors: MoReBench [Chiu2025] (A6 = 5, expert rubric criteria for procedural reasoning under five named traditions), ETHICS [Hendrycks2021] (A6 = 3, names traditions and creates sub-datasets but operationalizes them as classification tasks), and Hui *Decoding Moral* (A6 = 1, mentions ethics vocabulary without philosophical substance). All remaining benchmarks were scored relative to these anchors by the first author, with rationales recorded in the feature matrix.

### 3.3 Composite Scoring

We computed three axis scores. **Normative Depth (ND)** weights philosophical grounding and reasoning depth most heavily:

> ND = A2 × 25 + A6 × 20 + A1 × 15 + A3 × 15 + A5 × 15 + A4 × 10

**Practical Ease (PE)** prioritizes implementability and data access:

> PE = B7 × 30 + B3 × 20 + B4 × 15 + B6 × 15 + B9 × 10 + B5 × 10

**Citation Impact (CI)** balances normalized citations with downstream adoption:

> CI = C2 × 35 + C4 × 30 + C3 × 20 + C5 × 15

All axis scores are normalized to 0–100. The composite score combines the three axes:

> COMPOSITE = ND × 0.40 + PE × 0.35 + CI × 0.25

We weighted ND highest because this survey specifically evaluates *normative* depth — a benchmark that is easy to run but philosophically shallow serves our purpose less than one that is harder to implement but genuinely engages ethical theory. PE receives the second-highest weight because benchmarks without accessible data cannot be verified or extended. CI receives the lowest weight to avoid over-rewarding incumbency: the field's most-cited benchmark [Hendrycks2021] has 843 citations but produces ceiling effects on frontier models.

We applied two hard gates before ranking: (1) ND ≥ 40, ensuring minimum philosophical engagement, and (2) publicly available data (GitHub, HuggingFace, or equivalent repository). Of the 37 benchmarks, 12 failed the ND gate, 14 lacked public data, and 4 failed both, yielding exactly 15 benchmarks that passed both gates — including some high-ND benchmarks excluded solely for data unavailability (e.g., Chakraborty ND = 83, Rao ND = 80).

We verified tradition diversity in the final set: 8 of 15 test virtue ethics, 12 test deontological ethics, 11 test utilitarian ethics, 4 engage care ethics, and 1 includes contractarian ethics (Table 2). The set also includes two non-English or cross-cultural benchmarks (JETHICS [Takeshita2025] for Japanese, UniMoral [Kumar2025] across six languages) and two domain-specific benchmarks (PrinciplismQA [Hong2025] and MedEthicsQA [Wei2025], both in healthcare).

### 3.4 Implementation Trials

To move beyond feature-level characterization, we conducted implementation trials on five benchmarks spanning the composite-score spectrum: MoReBench [Chiu2025] (COMP = 70.2), ETHICS [Hendrycks2021] (COMP = 77.2), DailyDilemmas [ChiuDD2024] (COMP = 59.0), PrinciplismQA [Hong2025] (COMP = 67.9), and MoralReason-QA [An2025] (COMP = 65.5).

For each benchmark, we sampled 20–50 items and presented them directly to Claude Opus 4.6 via a chat-interface agent. We provided the benchmark's original instructions and response format, then scored model outputs against ground-truth labels or expert rubrics as specified by each benchmark's authors. We recorded accuracy, discriminative power (variance across items), and qualitative failure modes. For MoralReason-QA, we disaggregated accuracy by tradition to test whether LLMs exhibit systematic framework preferences — a hypothesis motivated by prior findings that models trained on web-scale corpora internalize consequentialist reasoning more readily than deontological or virtue-theoretic reasoning [Snoswell2025].

### 3.5 Limitations

Three methodological limitations warrant explicit acknowledgment. First, our implementation trials use Claude Opus 4.6 to evaluate benchmarks and to score its own responses, introducing self-evaluation bias. We report these results as directional evidence of discriminative power and framework difficulty, not as definitive model assessments. Second, the trial sample sizes (20–50 items per benchmark) are sufficient to identify ceiling effects and gross accuracy differences but insufficient for fine-grained statistical comparisons; full-scale evaluation across multiple model families is future work. Third, scoring heterogeneity across benchmarks — binary classification in ETHICS versus expert rubric criteria in MoReBench versus open-ended generation in DailyDilemmas — means that raw accuracy figures are not directly comparable across benchmarks. We mitigate this by reporting discriminative power alongside accuracy and by interpreting cross-benchmark patterns qualitatively rather than through formal statistical tests.
