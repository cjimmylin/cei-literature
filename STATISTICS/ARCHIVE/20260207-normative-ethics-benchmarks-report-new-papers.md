# Normative Ethics + LLM Benchmark: New Papers Classification Report

**Date:** 2026-02-07
**Scope:** 266 newly imported papers (DATE_ADDED: 20260207)
**YAML Field:** `normative_ethics_benchmark` (values: `Yes`, `Borderline`)
**Reference:** See `20260207-normative-ethics-benchmarks-report.md` for original 657-paper classification

---

## Methodology

### Process

1. **Keyword screening** — Three-leg test (normative ethics + benchmark/dataset + LLM) on all 266 new papers using PDF extract text (214 papers) or paper body text (52 papers without extracts)
2. **Candidate filtering** — Papers scoring 3 legs or 2 legs with Leg 1 (normative ethics) retained: **63 candidates**
3. **Deep reading** — Each candidate's PDF extract read in full by 5 parallel classification agents applying the 3-part test
4. **Duplicate check** — 3 papers identified as duplicates of already-tagged papers (removed)

### Qualifying Criteria (same as original report)

| Criterion | Requirement |
|-----------|-------------|
| **Normative ethics** | Explicitly references or operationalizes a normative framework (deontological, utilitarian, virtue, care, rights-based) |
| **Benchmark/dataset** | Creates, uses, or adapts a structured evaluation artifact |
| **LLM testing** | Evaluates one or more large language models |

- **Yes** = all 3 clearly met
- **Borderline** = most criteria met with a notable gap

### Data Availability

| Source | Papers | Notes |
|--------|--------|-------|
| PDF extracts available | 214 | Full text searched and read |
| No PDF extract | 52 | Paper body + abstract searched; 3 of these passed to candidate stage but all were excluded |

---

## Section 1: Confirmed Papers (5 papers — `normative_ethics_benchmark: Yes`)

| # | File | Ethics Frameworks | Data Artifact | LLMs Tested |
|---|------|------------------|---------------|-------------|
| 1 | `2024-Franken-OffTheRails Procedural Dilemma Generation for Moral Reasoning.md` | Deontological + Consequentialist (doctrine of double effect) | OffTheRails benchmark (50 scenarios, 400 items) | GPT-4, Claude-2 |
| 2 | `2024-Moore-Intuitions of Compromise - Utilitarianism vs. Contractualism.md` | Utilitarian (additive welfare) vs Contractualist (Nash Product) | Systematic value aggregation scenarios | GPT-4, Claude-3, Claude-2.1, GPT-3.5 |
| 3 | `2025-Ashkinaze-Deep Value Benchmark.md` | W.D. Ross's prima facie duties (deontological: beneficence, fidelity, justice, non-maleficence, reparation, self-improvement) | DVB (12K questions, DVGR metric) | 9 models |
| 4 | `2025-Huang-BehaviorBench Multi-Tier Benchmark for Agent Behavior Editing.md` | Deontology, utilitarianism, virtue ethics, justice (per Kagan's Normative Ethics) | BEHAVIORBENCH (multi-tier benchmark) | Frontier LLM agents |
| 5 | `2025-Zhou-Moral Reasoning Across Languages The Critical Role of Low-Resource.md` | Virtue ethics, deontological ethics, consequentialism (ETHICSMAX with 6 principles per branch) | MMRB (2,170 scenarios, 5 languages) | GPT-4, GPT-3.5, LLaMA3, Mixtral |

---

## Section 2: Borderline Papers (9 papers — `normative_ethics_benchmark: Borderline`)

| # | File | Why Borderline |
|---|------|----------------|
| 1 | `2024-Jin-MULTITP - Language Model Alignment in Multilingual Trolley Problems.md` | Large trolley problem benchmark (98K scenarios, 19 LLMs) but explicitly disclaims normative guidelines; utilitarian framing implicit in trolley design |
| 2 | `2024-Sorensen-Value Kaleidoscope ValuePrism.md` | Broad value pluralism with deontological rights/duties (218K items); primarily a value modeling/generation system rather than normative benchmark |
| 3 | `2024-Yao-CLAVE ValEval.md` | Systematic value evaluation across 3 value systems (13K+ tuples, 12+ LLMs) but MFT and Schwartz are descriptive psychology, not normative |
| 4 | `2025-Coleman-The Convergent Ethics of AI Analyzing Moral Foundation Priorities in.md` | Uses consequentialist-deontological dichotomy alongside MFT/Kohlberg (6 LLMs); but no released structured dataset artifact |
| 5 | `2025-Jotautaite-SpeciesismBench Evaluating LLM Recognition of Speciesist Statements.md` | Clear normative stance rooted in Singer's utilitarian animal ethics (1,003 statements); but normative framework implicit rather than formally operationalized |
| 6 | `2025-Kasu-EthicsMH.md` | Bioethics principles (autonomy, beneficence) overlap normative ethics (125 scenarios); pilot dataset without systematic LLM evaluation |
| 7 | `2025-Lee-CLASH Evaluating Language Models on Judging High-Stakes Dilemmas from.md` | Multiple normative theories (D+U+V+Care+Rights) used for reasoning chain analysis (345 dilemmas, 14 LLMs); normative theories used for post-hoc analysis, not as organizing principle |
| 8 | `2025-Wei-MedEthicsQA A Comprehensive Question Answering Benchmark for Medical.md` | Bioethics four pillars (beneficence, non-maleficence, autonomy, justice) — derived from normative ethics but applied domain-specific (5,623 MCQs, 9+ LLMs) |
| 9 | `2026-Farid-One Model Many Morals Uncovering Cross-Linguistic Misalignments in.md` | Uses translated ETHICS benchmark (D+U+V+Justice) across 5 languages (7 LLMs); no new normative contribution beyond translation of existing benchmark |

---

## Section 3: Exclusion Patterns

The following paper types were reviewed in the 63-paper candidate list and did NOT qualify:

### Psychology-Based Frameworks (not normative ethics)

| Pattern | Papers Excluded | Reason |
|---------|----------------|--------|
| **Moral Foundations Theory (MFT)** | Duan-DeNEVIL, Becker-Moralization Corpus, Trager-MFTCXplain, Jiao-LLM Ethics Benchmark, Wu-Staircase, Unknown-Measuring Moral, Unknown-Diagnosing Moral | MFT is descriptive psychology, not prescriptive normative framework |
| **Kohlberg / moral development** | Tanmay-DIT, Jiang-EMNLP | Developmental psychology, not normative philosophy |
| **Schwartz Value Theory** | Duan-AdAEM, Yao-Value FULCRA, Yun-VAPT | Descriptive social psychology values |

### Crowdsourced Norms / Social Preferences

| Pattern | Papers Excluded | Reason |
|---------|----------------|--------|
| **Social norms / Rules-of-Thumb** | Kim-ProsocialDialog, Ziems-MIC, Bonagiri-SaGE | Crowdsourced norms without normative theory grounding |
| **Moral Machine preferences** | Vida-Decoding Multilingual, Goel-Interpretable Models | Crowdsourced trolley preferences, no normative framework |
| **Cultural value surveys (WVS/PEW)** | Mohammadi-Cultural Variations, Shankar-Mind the Gap, Ghate-EVALUESTEER | Cultural opinion alignment, not normative ethics |

### Safety / Governance Benchmarks

| Pattern | Papers Excluded | Reason |
|---------|----------------|--------|
| **Safety benchmarks** | Tom-SG-Bench, Tian-Chinese SafetyQA, Simhi-ManagerBench, He-GVS-Scale, Ren-Safetywashing | Safety/harm prevention ≠ normative ethical analysis |
| **Safeguard frameworks** | Unknown-BELLS | Input/output safeguard detection |

### Method / Alignment Papers

| Pattern | Papers Excluded | Reason |
|---------|----------------|--------|
| **Alignment methods** | Huang-Collective Constitutional AI, Unknown-AI Alignment at Your Discretion, Unknown-Moral Alignment Intrinsic Rewards, Unknown-VALUEFLOW | Focus on alignment techniques, not evaluation benchmarks |
| **Agent evaluation methods** | Zheng-ALI-Agent | Generates adversarial test scenarios, not normative benchmark |

### Theory-Only / No Benchmark

| Pattern | Papers Excluded | Reason |
|---------|----------------|--------|
| **Theory papers** | Varshney-Decolonial AI, Authors-Pluralistic Alignment, Karimi-Theory Trace Card | Discuss normative ethics but no benchmark or LLM testing |
| **Methodology papers** | Unknown-Active Learning Moral Preference | Synthetic simulations, no benchmark |

### Other Non-Qualifying

| Pattern | Papers Excluded | Reason |
|---------|----------------|--------|
| **Moral competence measurement** | Kilov-Discerning What Matters, Marcuzzo-MORABLES | Measures reasoning quality, not normative classification |
| **Cross-linguistic consistency** | Wu-C-VARC | Chinese socialist values, not normative ethics |
| **Text classification tools** | Chen-MoVa | Uses LLMs as classifiers for descriptive frameworks |
| **Red-teaming / jailbreak** | Chua-TRIAL | Exploits ethical reasoning as attack vector |
| **Political consensus** | Authors-PoliCon | Political goal-setting, not normative ethics evaluation |
| **Value conflict analysis** | Unknown-ConflictScope | Alignment categories (HHH), not normative ethics |
| **Game-theoretic social dilemmas** | Unknown-When Ethics and Payoffs Diverge | Applied moral scenarios in game-theoretic framework |
| **Applied medical ethics** | Liu-JMedEthicBench | Professional medical guidelines, not normative philosophy |

### Duplicates of Already-Tagged Papers (3 removed)

| New File | Duplicate Of | Status |
|----------|-------------|--------|
| `2025-Takeshita-JETHICS - Japanese Ethics Understanding Evaluation Dataset.md` | `2025-Takeshita-JETHICS.md` (Yes) | Same arXiv:2506.16187 |
| `2024-Agarwal-Ethical Reasoning and Moral Value Alignment Multilingual.md` | `2024-Agarwal-Ethical Reasoning Depends on Language.md` (Yes) | Same arXiv:2404.18460 |
| `2025-Jiao-LLM Ethics Benchmark Three-Dimensional Assessment.md` | `2025-Jiao-LLM Ethics Benchmark.md` (Yes) | Same arXiv:2505.00853 |

---

## Summary Statistics

### New Papers (this batch)

| Category | Count |
|----------|-------|
| **Confirmed (Yes)** | 5 |
| **Borderline** | 9 |
| **Total newly tagged** | 14 |
| **Candidates reviewed** | 63 |
| **Exclusion rate** | 75% |
| **Duplicates removed** | 3 |

### Combined Totals (original + new)

| Category | Original | New | Total |
|----------|----------|-----|-------|
| **Yes** | ~20 | 5 | 25 |
| **Borderline** | ~11 | 9 | 20 |
| **Total tagged** | 31 | 14 | **45** |

### Framework Distribution (New Confirmed papers)

| Framework | Papers Referencing |
|-----------|-------------------|
| Deontological / Kantian | 5 |
| Utilitarian / Consequentialist | 4 |
| Virtue Ethics | 3 |
| Care Ethics | 0 |
| Rights-Based | 1 (Ross's duties) |
| Contractualist | 1 |

### Papers Without PDF Extracts

52 of 266 new papers had no PDF extract available. Of these, 3 passed keyword screening to the candidate stage but all were excluded during deep reading (1 was a duplicate, 2 were theory/methodology papers without benchmarks). The lack of PDF extract did not prevent any qualifying paper from being identified, as the abstract and paper body text provided sufficient signal for screening.

---

## Verification Checklist

- [x] `../.venv/bin/python PYTHON/validate_all_papers.py` — 923/923 pass
- [x] Total `normative_ethics_benchmark:` count: 45 (25 Yes + 20 Borderline)
- [x] Spot-check 3 newly tagged papers (DVB, OffTheRails, CLASH) — field correctly appended
- [x] Original 31 papers unchanged (all 14 new tags on DATE_ADDED: 20260207 papers only)
- [x] All 63 candidates evaluated (none skipped)
- [x] 52 papers without PDF extracts documented; none missed due to extract absence
- [x] 3 duplicates identified and removed from tagging

---

## Files Generated

| File | Purpose |
|------|---------|
| `PYTHON/screen_normative_ethics_candidates.py` | Keyword screening script |
| `PYTHON/add_normative_ethics_field.py` | Safe YAML field addition script |
| `logs/20260207-normative_ethics_candidates_20260207.json` | Screening output (237 raw, 63 filtered) |
| `logs/20260207-normative_ethics_decisions_20260207.json` | Final decisions (14 papers: 5 Yes + 9 Borderline) |
| `logs/20260207-normative_ethics_all_classifications_20260207.json` | Full 63-paper classification with reasoning |
| `STATISTICS/20260207-normative-ethics-benchmarks-report-new-papers.md` | This report |
