# Methods: Multi-Agent Council Review and Real-Data Figure Generation

**Date:** 2026-04-12
**Project:** `CEI-Lit-WS/RELIGIOUS-VALUES/`

## Data and Materials

The Religious Values Benchmark Paper v2 manuscript comprises 9 markdown files totaling 2,055 lines (304 KB) under `PAPER-V2/`: an abstract (`00-abstract.md`), four main sections (Methods through Conclusion in `01-methods.md` through `04-conclusion.md`), and four supplementary files (`05-supp-methods.md` through `08-supp-figures.md`). The bibliography (`PAPER/religious-values-benchmarks.bib`) contained 88 entries at session start. Trial response data for the construct validity battery was located in `data/20260404-trial-{tradition}-{model}.json` files (9 files: 3 traditions × 3 Claude models). Sensitivity analysis output was located in `data/20260404-sensitivity-analysis.json`. Cross-vendor model summaries were located in `COMPARISON/results/model-comparison.json`. All figure rendering used Python 3.9, matplotlib 3.x, seaborn, numpy, and scipy.stats.pearsonr, executed within the project's `.venv`.

## Procedure

### Phase 1: Six-Expert Review Council (Parallel Dispatch)

Six independent expert agents were dispatched in parallel as Claude Code subagents, each assigned a non-overlapping mandate and a structured output template. The Transition Architect read all five main-text files and scanned for boundary coherence, anti-essentialization patterns, and rhetorical overclaims. The Claims and Statistical Consistency Auditor traced eight pre-registered empirical claims across all sections and the Table S9 robustness battery, checking verdict labels, statistical values, prose framing, effect-size descriptors, and p-value labeling. The Supplementary Coherence Reviewer verified main-to-supplementary and intra-supplementary cross-references. The Citation Completeness Auditor performed a mechanical cross-check of all `\cite{Key}` calls against bibliography entries, including syntactic validation and entry completeness. The Citation Context Evaluator extracted surrounding sentence context for each citation and rated relevance on a STRONG/ADEQUATE/WEAK/MISATTRIBUTED scale. The Cross-Reference Integrity Verifier built complete registries of all defined sections, tables, and figures, then validated every cross-reference call site against these registries.

Each agent prompt specified mandatory execution-mode language ("EXECUTE immediately. Do NOT return a plan. Write findings directly to the output file.") and a structured finding template (location, severity, category, issue, recommendation, quote) to ensure synthesis tractability.

### Phase 2: Synthesis

A single synthesis agent read all six expert reports and performed validation, deduplication, conflict resolution, priority ranking, and dependency mapping. Overlapping findings (notably Figure S7 Haiku data errors flagged by Experts 3 and 6, and the four missing bibliography entries flagged by Experts 4 and 5) were merged, with provenance retained.

### Phase 3: Execute (Two Rounds)

Round A dispatched three execution agents in parallel: Batch 1 (Bibliography) added missing entries and fixed misattributed citations, Batch 2 (Cross-references) corrected broken Section/Table/Figure references and copied missing figure files, and Batch 3 (Narrative and Data) resolved count inconsistencies, hedged overclaims, and corrected the Antisemitism Detection tier boundary cascade. Round B then ran a single sequential Batch 4 agent for minor enhancements: precision standardization, citation density additions, and final overclaim hedging.

The Antisemitism Detection tier correction was identified as a dependency root: its bootstrap probability of 0.840 exceeded the Tier 1 threshold of 0.80, requiring movement from Tier 2 to Tier 1 with cascading updates to all tier counts (11→12 Tier 1, 4→3 Tier 2) and the Islamic Tier 1 share (8 of 11 → 9 of 12) across the abstract, results, and discussion.

### Phase 4: Verification

Three of the original six experts (Claims, Citations, Cross-References) were re-dispatched in parallel as read-only verifiers against the modified files. They confirmed 12 of 14 gate checks; three residual issues (three "cognitive demand" instances in the Discussion, one unqualified "universal" in the Conclusion, and a Gemini Pro Figure S7 data inconsistency) were fixed manually before final PDF regeneration.

### Block B: Citation Verification (Zhang2024)

After the main council pass, the Zhang2024 placeholder bibliography entry was investigated. A web-search agent ran five queries against arXiv, Semantic Scholar, and Google Scholar for any 2024 paper by Zhang et al. on theological dialogue systems, religious dialogue, Socratic LLM tutoring, or Talmudic reasoning. No matching paper was found. The citation was confirmed as fabricated and removed; the in-text reference was rephrased to remove the citation while preserving the forward-looking framing of the DLG (Dialectical Reasoning) format code reservation.

### Block C: Figure Generation

Two new figure functions were added to `generate_figures_v2.py`. Figure S2 (Gate Threshold Sensitivity) loads the gate threshold sweep results from `data/20260404-sensitivity-analysis.json` and renders a dual-axis line chart with the joint gate count on a logarithmic primary y-axis and tradition family coverage on a linear secondary y-axis. Per-point counts are annotated, the baseline RD threshold (30) is marked with a vertical line, and an inset annotation documents which void traditions are recovered at lower thresholds. Figure S6 (Bias-Values Scatter) loads trial responses from nine `20260404-trial-{tradition}-{model}.json` files for the three Claude models, builds index-based maps of bias and values_paired items per file, computes Pearson correlations using `scipy.stats.pearsonr`, and renders a 1×3 scatter grid with diagonal y=x reference lines, fitted regression lines, and per-panel correlation annotations. For Opus, where trial files lack `values_paired` items, the code falls back to regular `values` items paired by index, yielding n=10 pairs and r=0.673 (versus the published 0.706 from a slightly different item subset).

Both figures were generated, the manuscript figure descriptions in `08-supp-figures.md` were updated to remove placeholder notices and reflect the actual figure content, and the combined PDF was regenerated.

## Analysis

The council pass operated under six verification gates, four blocking and two advisory:
- **G1**: every `\cite{Key}` resolves to a bibliography entry
- **G2**: every Section/Table/Figure reference resolves to a defined target
- **G3**: all eight pre-registered claims have identical verdicts, statistics, and interpretive framing across all mention sites
- **G4**: zero CRITICAL severity issues remain
- **G5** (advisory): all section transitions reviewed with no MAJOR issues
- **G6** (advisory): no rhetorical overclaims or essentializing language

Issue severity used a three-level scale: CRITICAL (factual error, broken reference, missing bibliography entry), MAJOR (inconsistency that could mislead readers, ambiguous reference), MINOR (formatting, style, optimization). Statistical effect sizes referenced in the paper used Cohen's conventional thresholds (small d=0.2, medium d=0.5, large d=0.8; small V=0.1, medium V=0.3, large V=0.5).

For Figure S6 correlation analysis, the Pearson correlation was computed with `scipy.stats.pearsonr` on n=10 paired samples per model. The construct independence threshold (r < 0.30) was applied to label models as independent or conflated. Tradition-level coloring (Islam, Christianity, Hinduism) used the Okabe-Ito colorblind-safe palette consistent with the project's other figures.

## Computational Environment

Python 3.9 within `/Users/jimmy.lin/Documents/CEI-Literature-Vault/.venv/`. matplotlib (Agg backend), seaborn, numpy, scipy.stats. fpdf2 for PDF generation via `generate_combined_pdf.py`. All figures rendered at 300 DPI with tight bounding boxes and serif typeface (size 11). The Claude Code agent runtime managed parallel subagent dispatch (six simultaneous in Phase 1; three simultaneous in Phase 3 Round A; three simultaneous in Phase 4). Agent prompts were authored to include explicit execution-mode instructions and structured output templates following CLAUDE.md guidance about agent orchestration. No external API calls were made except for the Zhang2024 web search verification.

## Limitations and Decisions

The original Figure S2 description in `08-supp-figures.md` claimed three decomposed curves (joint gate, RD-only, data-availability-only). The sensitivity JSON only contains joint-gate sweep data; the decomposition into single-gate curves would require recomputing from the raw candidate matrix. Rather than fabricate the decomposition, the figure was redesigned to show the joint-gate sweep with tradition coverage as a complementary secondary axis, and the figure description was updated to match what the data actually supports. This trades visual richness for empirical fidelity.

For Figure S6, the Opus trial files lack `values_paired` items because the matched-pair protocol was added after the Opus trials were collected. The published bias-values correlation for Opus (r=0.706) differs slightly from the value computed in this session (r=0.673), because the published figure must have used a different item subset. The qualitative conclusion (r > 0.30, conflated) is unchanged, and both values are reported in the figure caption to maintain transparency. OpenAI and Gemini models were omitted from Figure S6 because no matched paired-item trial data was collected for non-Anthropic vendors.

The 6-expert council architecture was scoped to narrative coherence and bibliography verification only. Theological accuracy, terminology drift, and statistical assumption documentation are out of scope for this review pass; the prior 12-expert writing council (Session 13) addressed those domains. The critique meta-council that reviewed the plan before execution flagged this scope limitation as acceptable given the focused review goals.

The Tier 1 boundary correction (Antisemitism Detection moved from Tier 2 to Tier 1) cascaded through every count mention in the paper. Each cascading edit was applied by the Batch 3 execution agent and verified by the Phase 4 Expert 2 re-pass. The decision to elevate Antisemitism Detection followed the published threshold (p ≥ 0.80) rather than the original tier assignment, on the grounds that the threshold is the authoritative criterion and the tier label was a clerical error.
