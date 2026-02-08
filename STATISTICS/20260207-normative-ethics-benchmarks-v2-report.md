# Normative Ethics Benchmark Classification — V2 Full Deep-Read Report

**Date:** 2026-02-07
**Scope:** 266 EXSR papers (exhaustive search import batch)
**Method:** 10-agent full deep-read (no keyword pre-screening)

---

## Methodology

### V1 (Previous Round)
- Keyword screening filtered 266 papers → 63 candidates (2+ of 3 keyword legs)
- 5 agents deep-read 63 candidates
- Result: 14 tagged (5 Yes + 9 Borderline)

### V2 (This Round)
- **No keyword screening** — all 266 papers deep-read directly
- 10 agents, each reading 26-27 papers with full PDF extracts (where available)
- 3-part rubric: (1) Normative ethics frameworks, (2) Benchmark/dataset, (3) LLM testing
- 2 waves of 5 agents for reliability
- Result: **45 tagged (7 Yes + 38 Borderline)**

---

## Results Summary

| Decision | V1 | V2 | Change |
|----------|---:|---:|--------|
| Yes | 5 | 7 | +2 |
| Borderline | 9 | 38 | +29 |
| Exclude | 252 | 221 | -31 |
| **Total** | **266** | **266** | — |

### Yes Papers (7)
1. 2024-Agarwal — Multilingual Ethical Reasoning (Deontology, Virtue Ethics, Consequentialism)
2. 2024-Moore — Utilitarianism vs. Contractualism
3. 2024-retrieved — Cross-Linguistic Moral Preferences (Rawlsian/egalitarian)
4. 2025-Hong — PrinciplismQA (Beauchamp & Childress bioethics principles)
5. 2025-Huang — BehaviorBench (Kagan's Normative Ethics)
6. 2025-Takeshita — JETHICS (D/U/V/Justice in Japanese)
7. 2025-Unknown — Moral Alignment for LLM Agents (Deontological/utilitarian intrinsic rewards)

### Borderline Papers (38)
Papers meeting 2 of 3 conditions strongly, or all 3 weakly. Includes:
- Bioethics/medical ethics benchmarks (PrinciplismQA adjacent, MedEthicsQA, MedES, JMedEthicBench, etc.)
- Trolley problem / moral dilemma benchmarks (TrolleyBench, MULTITP, CLASH)
- Value frameworks with normative overlap (ValEval, ValuePrism, COMETH)
- Implicit normative framing without formal operationalization

---

## Reconciliation with V1

### Overlap (63 papers reviewed in both rounds)
- **Consistent:** 49 papers (78%)
- **Upgraded (Exclude→Borderline/Yes):** 11 papers
- **Downgraded (Yes→Borderline):** 3 papers

### Upgraded Papers (11)
| Paper | V1 | V2 |
|-------|----|----|
| Varshney — Decolonial AI Alignment | Exclude | Borderline |
| ALI-Agent — Zheng | Exclude | Borderline |
| PoliCon — Authors | Exclude | Borderline |
| TRIAL — Chua | Exclude | Borderline |
| EMNLP — Jiang | Exclude | Borderline |
| LLM Ethics Benchmark — Jiao | Exclude | Borderline |
| ConflictScope — Unknown | Exclude | Borderline |
| Measuring Moral LLM Responses — Unknown | Exclude | Borderline |
| Moral Alignment Intrinsic Rewards — Unknown | Exclude | **Yes** |
| Ethics and Payoffs Diverge — Unknown | Exclude | Borderline |
| JMedEthicBench — Liu | Exclude | Borderline |

### Downgraded Papers (3)
| Paper | V1 | V2 | Reason |
|-------|----|----|--------|
| Franken — OffTheRails | Yes | Borderline | V2 agent found implicit rather than formal operationalization |
| Ashkinaze — Deep Value Benchmark | Yes | Borderline | Ross's duties used but less systematically than initially assessed |
| Unknown — Moral Reasoning Across Languages | Yes | Borderline | ETHICSMAX normative branches present but not formally ground-truth normative |

### New Discoveries (18 papers)
Papers NOT in the previous 63 candidates that scored Yes/Borderline:

| Paper | Decision | Frameworks |
|-------|----------|------------|
| Cross-Linguistic Moral Preferences | **Yes** | Rawlsian/egalitarian distributive justice |
| PrinciplismQA — Hong | **Yes** | Beauchamp & Childress principlism |
| Confucian Analects — So | Borderline | Confucian virtue ethics |
| Conscience Conflict — results | Borderline | Competing normative principles |
| TrolleyBench — Authors | Borderline | Utilitarian/deontological trolley framing |
| Healthcare Ethics China — Bian | Borderline | Bioethics principles |
| Cognitive Biases in Moral — Capraro | Borderline | Personal/impersonal dilemmas |
| Corpus-Based Medical Ethics — Ebara | Borderline | Medical ethics principles |
| MoralBench — Gai | Borderline | Moral benchmarking with ethical annotations |
| Delphi Experiment — Jiang | Borderline | Gert's 10 moral principles |
| EthicsSuite — Ma | Borderline | Reflective equilibrium |
| COMETH — Morlat | Borderline | Gert's common morality rules |
| Moral Judgements Robustness — Oh | Borderline | Implicit consequentialist/deontological |
| Mapping Moral Reasoning — Unknown | Borderline | Safety principles from normative frameworks |
| TrolleyBench — Zhu | Borderline | Trolley-problem dilemmas |
| Decoding Moral Responses — extracted | Borderline | Personal/impersonal dilemmas |
| MedES — Jin | Borderline | Chinese medical ethics |
| PsychEthicsBench — Shen | Borderline | Australian psychology ethics codes |

---

## Key Takeaways

1. **Keyword screening missed 29% of tagged papers.** The v1 keyword filter passed only 63 of 266 papers, but 18 papers outside that 63 turned out to be Yes/Borderline — a recall gap of 18/45 = 40%.

2. **V2 is more inclusive overall.** 45 papers tagged vs 14, largely because the full deep-read catches papers with implicit or domain-specific normative framing (bioethics, Confucian ethics, Gert's common morality) that keyword patterns miss.

3. **V2 is slightly stricter on Yes.** 3 papers downgraded from Yes to Borderline, suggesting the 10-agent approach applies the "all 3 conditions met" test more conservatively.

4. **Medical/bioethics is the biggest new category.** 6+ new discoveries involve bioethics principles (autonomy, beneficence, non-maleficence, justice) — these derive from normative philosophy but occupy a grey zone.

---

## Files Generated

| File | Contents |
|------|----------|
| `logs/normative_v2_batches/batch_01.json` — `batch_10.json` | Input batches (266 papers) |
| `logs/normative_v2_batches/results_agent_01.json` — `results_agent_10.json` | Per-agent classifications |
| `logs/20260207-normative_v2_all_classifications.json` | All 266 classifications |
| `logs/20260207-normative_v2_decisions.json` | 45 Yes/Borderline decisions |
| `STATISTICS/20260207-normative-ethics-benchmarks-v2-report.md` | This report |

## Scripts Created

| Script | Purpose |
|--------|---------|
| `PYTHON/generate_normative_v2_batches.py` | Split 266 EXSR papers into 10 batches |
| `PYTHON/consolidate_normative_v2.py` | Merge, validate, reconcile 10 agent results |
| `PYTHON/add_normative_v2_field.py` | Write `normative_ethics_benchmark` to YAML |

## Validation

- 923/923 papers pass YAML validation
- 45/45 decisions written to paper files
- 266/266 unique papers classified (no duplicates, no missing)
- Spot-checked 3 papers: field values match decisions file
