# Normative Ethics Eval-of-Evals — Session Handoff

**Date:** 2026-04-02 to 2026-04-03
**Status:** Paper draft complete (6,094 words + supplement); 2 minor editorial items remain
**Plan file:** `.claude/plans/glowing-meandering-plum.md`
**Project directory:** `CEI-Lit-WS/NORM-ETHICS/` (all session outputs relocated here)

---

## Executive Summary

Built a comprehensive meta-evaluation of normative ethics benchmarks for LLM values alignment — from initial literature audit through feature matrix construction, gap analysis, implementation trials, and academic paper draft. The project produced:

- **37 benchmarks** characterized across **26 features** in 4 axes (Normative Depth, Practical Ease, Citation Impact, Metadata)
- **Top 15 ranked selection** with composite scoring (ND×0.40 + PE×0.35 + CI×0.25)
- **5 implementation trials** (150 items) revealing ceiling effect in ETHICS, consequentialist bias in LLMs, care ethics research void
- **8-page paper draft** targeting NeurIPS 2026 Datasets & Benchmarks track, with 84 references and 5 appendices
- **6 new papers ingested** into the vault from external search

---

## Work Completed

### Sessions 1-3: Feature Matrix Construction

**What:** Extracted 26 features for 31 normative ethics benchmark papers from the vault.

- **S1:** YAML frontmatter extraction (ethics scores, DATA_URL, benchmark flags) for all 31 papers. Script: `/tmp/extract_benchmark_features.py`
- **S2:** Full-text feature extraction from PDF extracts (format, dataset size, scorer type, model compatibility, cultural provenance, annotator type, etc.). Script: `/tmp/extract_fulltext_features.py`. Manual corrections applied for cultural provenance (regex overcounted) and domain (healthcare overcounted).
- **S3:** Normative depth assessment (A2-A6) via 3 parallel agents reading PDF extract abstracts. Calibration anchors: MoReBench (A6=5, high), ETHICS (A6=3, moderate), Hui (A6=1, low).
- **Citation data:** Semantic Scholar API queries for all 31 papers (citation count, age-normalized rate, venue, influential citations).
- **Dashboard scores:** Extracted per-paper implementability scores across 6 harnesses from eval framework dashboard v4.

**Output:** `NORM-ETHICS/STATISTICS/20260402-normative-benchmark-feature-matrix.json` (110 KB, 37 papers after Session 5 additions)

### Sessions 4-5: Gap Analysis + External Search

**What:** Systematic search for normative ethics benchmarks not in the vault. PRISMA-compliant protocol across 7 databases with 10 query sets.

- **20 candidates found** (18 searches + 8 page fetches)
- **6 ingested** into vault: DailyDilemmas, PrinciplismQA, Pluralistic Moral Gap (already in vault as Russo — enriched), UniMoral (name collision fixed — BengaliMoralBench mislabel corrected), MedEthicsQA, ProMoral-Bench
- **Key finding:** No pure care ethics (Gilligan/Noddings) or contractarian (Rawls) LLM benchmark exists anywhere in the literature
- **Data re-check:** 8 high-ND papers with DATA_URL=NA re-checked; all correctly marked unavailable. Chakraborty's GitHub repo returns 404; Hilliard plans open-source but hasn't released.

**Output:** `/tmp/external_search_results.json`, `/tmp/data_recheck_results.json`

### Sessions 6-7: Scoring + Top 15 Selection

**What:** Computed composite scores, applied hard gates (ND ≥ 40, data available), applied diversity constraints.

- **15 papers pass both gates** (exactly the target)
- **Diversity verified:** V=8, D=12, U=11, C=3 (via PrinciplismQA, Pluralistic Moral Gap, MedEthicsQA), Co=1 (MoReBench). Non-Western: JETHICS (Japanese), UniMoral (6 languages). Domain-specific: PrinciplismQA + MedEthicsQA (healthcare).

**Output:** `NORM-ETHICS/STATISTICS/20260403-normative-ethics-top15-benchmark-selection.md`

### Sessions 9-11: Implementation Trials

**What:** 5 parallel agents each downloaded benchmark data, sampled 20-50 items, evaluated them (Claude as LLM-under-test), scored results, and wrote trial reports.

| Trial | Benchmark | Items | Key Finding |
|-------|-----------|-------|-------------|
| T1 | ETHICS (Hendrycks) | 50 | **100% accuracy — ceiling effect.** Cannot discriminate frontier LLMs. |
| T2 | MoReBench-Theory | 30 | **10% rubric coverage.** Tests procedural reasoning; genuinely hard. Contractualist best (18.3%), virtue worst (4.0%). |
| T3 | MoralReason-QA | 30 | **Framework hierarchy:** Utilitarian 77% > Virtue 63% > Deontological 50%. Joint accuracy 37%. |
| T4 | Moral Lens | 20 | **40% refusal rate** on gender/fitness/status items. 60% deontological, 40% consequentialist tendency. |
| T5 | DailyDilemmas | 20 | **No ground truth.** Value profiling tool, not accuracy benchmark. 57% virtue match rate. |

**Revised priority (by discriminative power, not composite):**
1. MoralReason-QA (best balance of difficulty + ease)
2. MoReBench-Theory (gold standard but needs LLM-as-judge)
3. Moral Lens (good for bias detection)
4. ETHICS (baseline/sanity check only)
5. DailyDilemmas (profiling tool only)

**Output:** `NORM-ETHICS/STATISTICS/20260403-trial-T{1-5}-*.md` (5 reports), `NORM-ETHICS/STATISTICS/20260403-implementation-trials-summary.md`, `/tmp/trial_T{1-5}_{items,scored}.json`

### Sessions 12-14: Academic Paper Draft

**What:** 3-phase parallel architecture — spine → 5 parallel writers → 2 sequential writers → integrator.

**Title:** "What Do Normative Ethics Benchmarks Actually Test? A Meta-Evaluation of 37 LLM Moral Reasoning Assessments"

**5 Key Claims:**
1. Ceiling effect in ETHICS (most-cited benchmark, 100% accuracy)
2. LLMs are more consequentialist (77%) than deontological (50%)
3. No care ethics or contractarian benchmark exists (research void)
4. Most benchmarks (28/37) test judgment, not reasoning
5. Data unavailability blocks 32% of benchmarks

**Integration report:** All checks passed. 2 citation keys fixed (Liang2023→2022, Snoswell2026→2025). Total: 6,094 words main body + 5,510 words supplement + 84 references.

---

## Files Created

### NORM-ETHICS/STATISTICS/
| File | Size | Purpose |
|------|------|---------|
| `20260402-normative-benchmark-feature-matrix.json` | 110 KB | Master feature matrix (37 papers × 26 features + composites) |
| `20260403-normative-ethics-top15-benchmark-selection.md` | 8 KB | Top 15 ranking with methodology and diversity checks |
| `20260403-implementation-trials-summary.md` | 9 KB | Consolidated cross-benchmark trial comparison |
| `20260403-trial-T1-ethics.md` | 10 KB | ETHICS trial (ceiling effect finding) |
| `20260403-trial-T2-morebench.md` | 11 KB | MoReBench trial (procedural reasoning) |
| `20260403-trial-T3-moralreason.md` | 10 KB | MoralReason-QA trial (framework hierarchy) |
| `20260403-trial-T4-morallens.md` | 13 KB | Moral Lens trial (refusal patterns) |
| `20260403-trial-T5-dailydilemmas.md` | 13 KB | DailyDilemmas trial (no ground truth) |

### NORM-ETHICS/PAPER/
| File | Words | Section |
|------|-------|---------|
| `spine-normeval.md` | — | Shared contract (title, claims, glossary, figure assignments) |
| `introduction-normeval.md` | 1,442 | Abstract + Sec 1 (Introduction) + Sec 2 (Related Work) |
| `methods-normeval.md` | 1,049 | Sec 3 (Methods) |
| `results-landscape-normeval.md` | 931 | Sec 4.1 (Landscape) + 4.2 (Top 15) |
| `results-trials-normeval.md` | 919 | Sec 4.3 (Trials) + 4.4 (Cross-benchmark) |
| `discussion-normeval.md` | 1,753 | Sec 5 (Discussion) + Sec 6 (Conclusion) |
| `references-normeval.md` | 2,476 | Bibliography (84 references) |
| `supplement-normeval.md` | 5,510 | Appendices A-E (matrix, scoring, trials, excluded, search) |
| `integration-report-normeval.md` | — | QA report from integration agent |

### Vault Papers (new/modified)
| File | Action |
|------|--------|
| `papers/2025-Hong-PrinciplismQA.md` | Created |
| `papers/2025-Kumar-UniMoral.md` | Created |
| `papers/2026-Thomas-ProMoral-Bench.md` | Created |
| `papers/2025-Kumar-BengaliMoralBench.md` | Renamed from `2025-Kumar-UniMoral ACL 2025 Best Resource Paper.md` |
| `papers/2025-Russo-The Pluralistic Moral Gap.md` | Updated (ethics scores, data_metrics, normative_ethics_benchmark) |
| `papers/2024-Chiu-DailyDilemmas.md` | Updated (data_metrics, normative_ethics_benchmark) |
| `papers/2025-Wei-MedEthicsQA.md` | Updated (data_metrics, normative_ethics_benchmark) |

### Temporary Files (/tmp/)
| File | Purpose |
|------|---------|
| `normative_benchmark_features.json` | Initial YAML extraction (31 papers) |
| `dashboard_scores.json` | Eval dashboard implementability data |
| `semantic_scholar_citations.json` | Citation data from S2 API |
| `fulltext_features.json` | PDF extract feature extraction |
| `external_search_results.json` | 20 external search candidates |
| `data_recheck_results.json` | Data availability re-check |
| `all_new_features.json` | Combined features for 6 new papers |
| `final_top15.json` | Top 15 selection (pre-matrix-update) |
| `ingest_{dailydilemmas,principlismqa,pluralistic_gap,unimoral,medethicsqa,promoral}.json` | Per-paper ingest feature data |
| `trial_T{1-5}_{items,scored}.json` | Raw trial data |
| `ethics_data/` | Downloaded ETHICS benchmark CSVs |

---

## Context for Next Session

### 2 Editorial Items to Resolve

1. **Missing Appendix F (Table S9):** The spine references a cross-harness implementability matrix (37 benchmarks × 6 harnesses) but the supplement only has Appendices A-E. Either write Appendix F from the eval dashboard data (`DASHBOARDS/20260329-eval-framework-dashboard-v4.html`) or remove the spine reference.

2. **Rottger2024 citation mismatch:** Introduction cites `[Rottger2024]` for "methodological standards for safety benchmarks" but the references entry points to the XSTest paper (exaggerated safety behaviors). Verify intended paper or substitute.

### Recommended Next Steps

1. **Author review of paper draft** — Read all sections in order (intro → methods → results → discussion → conclusion). Check that claims match your intended narrative.

2. **Generate figures** — Figures 1-4 are described in text but not yet generated as images. The feature matrix JSON has all data needed:
   - Fig 1 (heatmap): 37×5 tradition scores from `A1_traditions` field
   - Fig 2 (grouped bars): U=77%, V=63%, D=50% from Trial T3
   - Fig 3 (scatter): ND vs PE with citation bubble size
   - Fig 4 (stacked bar): `B3_data_availability` field counts

3. **LaTeX conversion** — Convert markdown sections to NeurIPS LaTeX template. The sectional structure maps cleanly to `\section{}` commands.

4. **Cross-model replication** — The trials used Claude self-evaluation (noted as limitation). Running the same 150 items through GPT-4o and Llama-3 via API would significantly strengthen the findings, especially Claim 2 (consequentialist bias).

5. **Full-scale implementation** — The trials sampled 20-50 items each. Full-scale runs on complete test sets (especially MoralReason-QA's 680 items and MoReBench-Theory's 150 items) would provide statistical significance.

### Key Architectural Decisions (for future sessions)

- **Composite weighting (40/35/25):** Chosen to prioritize normative depth over practical ease and citations. This can be adjusted — the feature matrix JSON supports any weighting.
- **Hard gate threshold (ND ≥ 40):** Eliminates benchmarks with only surface-level ethics engagement. Lowering to 30 would admit 5 more papers (including CMoralEval and Keshmirian).
- **Self-evaluation method:** Chosen because user specified "chat interface LLM agent." A harness-based approach (lm-eval, Inspect) would give more rigorous results but requires infrastructure setup.

### Dependencies

- **Python venv:** `.venv/bin/python` (Python 3.9) with `datasets` 4.5.0 installed
- **HuggingFace datasets:** MoReBench, MoralReason-QA, DailyDilemmas accessible
- **GitHub repos:** ETHICS (`hendrycks/ethics`), Moral Lens (`keenansamway/moral-lens`) accessible
- **Semantic Scholar API:** Used with 3s delay; may need API key for batch access
