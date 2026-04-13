# Methods: NormEval v2.2-preliminary Dashboard and Paper Assembly via Multi-Expert Council

**Date:** 2026-04-13
**Project:** `CEI-Lit-WS/NORM-ETHICS/`

## Data and Materials

The session operated on existing NormEval artifacts: a 54-benchmark x 41-feature dataset (`data.js`, 200KB), a cross-vendor extension (`data_cross_vendor.js`, 17KB), 12 paper section files totaling approximately 37,700 words, and 12 figure PNGs (8 main + 4 supplementary). Data integrity was verified via SHA-256 checksums stored in `.corpus-manifest` and `FIGURE-MANIFEST.txt`.

The dashboard source comprised 6 files from DASHBOARD-v2/ (index.html 84KB, app.js 49KB, charts.js 38KB, style.css 26KB, and two data files). The PDF builder was forked from a prior project's fpdf2-based generator (`CEI-AI-Statements/children/paper/generate_v3_combined_pdf.py`).

## Procedure

### Phase 0: Pre-Council Infrastructure

Directory structures were created for `PAPER-v2.2/` (source, figures, build, blind-review, council subdirectories) and `DASHBOARD-v4/` (council, deploy, screenshots). A pre-council briefing document (`briefing-session19.md`, ~500 words) was written as a single-read context document for all council agents, replacing the alternative of each agent independently reading 8+ source files. An implementation contract (`CONTRACT.md`) was written pinning CSS class names, script load order, theme toggle specification, CDN versions, tab structure, and banner wording before any parallel agent dispatch.

### Phase 1: Plan + Meta-Critique

An initial implementation plan was written and then submitted to a 12-expert alternate council for critique. The 12 critic perspectives were deliberately orthogonal to the domain-correctness councils that would review the actual artifacts: release engineering, technical program management, QA, software architecture, data engineering, security, legal/licensing, UX research, academic publishing, risk management, resource economics, and research ethics. Each critic read the full plan and produced a structured analysis (top 3 concerns, specific edits, missing element). The plan was revised to incorporate 12 accepted changes.

### Phase 2: Parallel Council Dispatch (24 Agents)

Two 12-expert councils were dispatched in parallel across 3 batches of 4 agents each (8 agents per batch, 3 batches = 24 total). The dashboard council assessed science communication, information design, ML benchmarking methodology, normative ethics, psychometrics, statistics, WCAG accessibility, frontend/ECharts, research integrity, hostile review, accessibility heuristics, and project-history compliance. The paper council assessed normative ethics, ML methods, psychometrics, statistics, scientific writing, reproducibility/FAIR, research integrity, bibliometrics, figure/table design, hostile review, first-time reader comprehension, and sprint-history alignment.

All 24 agents wrote markdown plan files to their respective `council/plan-phase/` directories. File existence was verified after each batch. Agents were instructed to read the pre-council briefing document first, then their per-expert scope, reducing redundant file I/O by an estimated 180K tokens.

### Phase 3: Synthesis and Execution

Dashboard synthesis consolidated 12 expert plans into a single `SYNTHESIS.md` with per-tab edit lists, CSS changes, JS changes, and deferred items. Execution was performed in the main session (not sub-agents) to avoid a known plan-mode propagation bug (Session 18 Issue #3).

Dashboard changes: CSS contrast fixes (2 hex values for WCAG AA compliance), light theme CSS variable block, preliminary banner styles, simulated-data tag styles, focus-visible indicators, reduced-motion media query, mobile breakpoints. HTML: new Tab 0 (Guide) with 7 content sections, compact preliminary banner on Cross-Vendor tab, language softening on 3 tabs, 8 inline simulated tags, theme toggle button, footer. A NOTICE file was created for third-party attributions (Bootstrap, ECharts, jsDelivr, Inter, JetBrains Mono).

Paper changes: abstract disclosure paragraph, v4 dashboard URL in 3 locations (abstract, data availability, conclusion), 9 missing reference entries added, Wei2025b citation key corrected to Galatolo2025, new Appendix K (prompt provenance and system configuration), REVISION-PROTOCOL.md documenting the v2.2 -> v2.3 upgrade path.

### Phase 4: PDF Assembly

The combined PDF was built using fpdf2 2.8.4 (Python 3.9). The builder script was forked from the children paper generator and adapted for NormEval's section structure (11 main sections + 1 appendix). Unicode sanitization was applied to handle en-dashes, em-dashes, curly quotes, Greek letters, and mathematical symbols. The title page includes an orange "DRAFT -- NOT FOR CITATION" disclosure. Every page footer carries a gray watermark: "DRAFT -- NOT FOR CITATION -- NormEval v2.2-preliminary -- Page N". A license page lists the dual MIT/CC-BY-4.0 license and all 4 dashboard URLs. The figures section embeds 12 PNGs with `[simulated -- awaits external validation]` caption flags on the 5 figures containing cross-vendor data (fig6, fig7, fig8, figS5, figS6).

### Phase 5: Deployment and Verification

The dashboard was deployed to GitHub Pages via a split-step pattern: `gh repo create` (separate from push), 3-second wait, `git push`, `git ls-remote` verification, `gh api` Pages enablement, 30-second polling until HTTP 200 (achieved on attempt 3, ~60 seconds). All 4 dashboard versions (v1-v4) were verified returning HTTP 200. A 17-point verification checklist was executed covering deploy file count, Tab 0 content, banner presence, simulated tags, URL liveness, PDF size/page count, source file count, v4 URL placement, reference fixes, Appendix K existence, revision protocol, manifests, and checkpoint integrity.

## Computational Environment

- Python 3.9 (`.venv/bin/python`)
- fpdf2 2.8.4
- Playwright MCP (Chrome) for dashboard verification
- GitHub CLI (`gh`) for deployment
- macOS Darwin 25.3.0

## Limitations and Decisions

1. **The 6-critic meta-phase for Part B (paper) was cut** based on resource economics analysis (Critic 11). The paper's edits are mechanical (known fixes, URL swaps, 1 new appendix), making creative meta-critique redundant. This saved ~6 agents and ~90K tokens.
2. **The Anthropic-only default toggle was deferred to v5** despite being the hostile reviewer's #1 recommendation (Expert 10). It would require dual-mode rendering throughout charts.js -- high complexity for a preliminary release.
3. **ECharts theme adaptation is incomplete.** The CSS chrome switches correctly on theme toggle, but ~30 hardcoded hex values in charts.js keep chart canvases dark-themed. A `getThemeColors()` helper was specified but not implemented. The visual impact is acceptable (dark charts on light page chrome are readable) but not ideal.
4. **The blind-review PDF variant was not built** due to time constraints. The build script supports it architecturally (anonymize flag) but the flag is not yet implemented. This is needed before TMLR submission.
5. **Inline `[simulated]` flags were applied to the abstract but not yet systematically to results-crossvendor and discussion sections** (~38 locations identified by Expert 1). This is the highest-priority remaining edit for paper polish.
