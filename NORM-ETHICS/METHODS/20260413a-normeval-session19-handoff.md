# NormEval -- Session 19 Handoff

**Date:** 2026-04-13
**Session:** Dashboard v4 + Paper v2.2-preliminary via 12-expert councils (plan, critique, execute)
**Project:** `CEI-Lit-WS/NORM-ETHICS/`
**Previous handoff:** `METHODS/20260413-normeval-session18-handoff.md`

---

## What Was Done This Session

### 1. Plan + 12-Expert Meta-Critique Council

Wrote a comprehensive implementation plan for two deliverables (Dashboard v4 + Paper v2.2-preliminary). Submitted the plan to a 12-expert alternate council (release engineering, TPM, QA, architecture, data engineering, security, legal, UX, academic publishing, red team, resource economics, research ethics) for critique. 12 concrete improvements were accepted into the revised plan, including:

- **Research integrity labeling** (Critic 12): all v2.2 artifacts labeled "preliminary" with "DRAFT -- NOT FOR CITATION" watermark and inline `[simulated]` flags
- **True sequencing** (Critic 2): Parts A and B are NOT parallel -- Paper v2.2 depends on Dashboard v4's URL
- **Git checkpoints** (Critic 10): A0 and B0 snapshots before execution phases
- **Agent budget reduction** (Critic 11): cut Part B 6-critic meta-phase, down from 42+ to 24 agents

### 2. Dashboard v4 (12-Expert Council + Execution)

**Phase A:** 12 expert agents dispatched in 3 batches (SciComm, InfoDesign, ML Benchmarks, Ethics, Psychometrics, Statistics, Accessibility, Frontend, Integrity, Hostile Reviewer, A11y Reviewer, Historian). All 12 produced plan files.

**Key findings from dashboard council:**
- 20 glossary terms needed for Tab 0 (Expert 1)
- `<details>` collapse pattern for B/M/I text blocks (Expert 2)
- 260-word Five Ethical Traditions glossary drafted (Expert 4)
- 21 WCAG 2.2 AA violations identified (Expert 7)
- v2 has ZERO theme toggle infrastructure (Expert 8)
- 7 unqualified factual claims about simulated data (Expert 9)
- Anthropic-only default toggle recommended for v5 (Expert 10, deferred)
- All 5 CLAUDE.md safety checks pass (Expert 12)

**Phase C execution (main session):**
- Copied DASHBOARD-v2/ to DASHBOARD-v4/
- CSS: contrast fixes (--text-muted #8a8ea8 -> #9ea2bc, --text-secondary #9498b3 -> #a8acc4), light theme vars, preliminary banner styles, simulated tag, provenance badges, focus-visible, reduced-motion, mobile breakpoints, care ethics tradition dot
- HTML: Tab 0 (Guide) with preliminary banner, orientation, "Why show simulated data?" rationale, framework explainer (ND/PE/CI with colored cards), Five Ethical Traditions glossary, reading path, 15-term technical glossary, color legend
- HTML: Compact preliminary banner on Cross-Vendor tab
- HTML: Language fixes ("confirms" -> "suggests", "validated" -> explored) on tabs 1, 8, 10
- HTML: 8 `[simulated]` inline tags throughout
- HTML: Theme toggle button, footer with v4 label
- JS: Inline theme toggle script with localStorage, ECharts re-render
- NOTICE file with third-party attributions

**Phase D verification:**
- Playwright: Guide tab, Overview tab, Cross-Vendor tab, light theme all render correctly
- 0 JS errors (only favicon.ico 404)
- 4 screenshots in DASHBOARD-v4/screenshots/

**Deployment:**
- `cjimmylin/cei-normeval-dashboard-v4` created, pushed, Pages enabled
- **LIVE at https://cjimmylin.github.io/cei-normeval-dashboard-v4/**
- v1, v2, v3 all verified still returning 200

### 3. Paper v2.2-preliminary (12-Expert Council + Execution)

**Phase A:** 12 expert agents (Ethics, ML Methods, Psychometrics, Statistics, Writing/Style, Reproducibility, Integrity, References, Figures, Hostile Reviewer, First-time Reader, Sprint Historian). All 12 produced plan files.

**Key findings from paper council:**
- 38 cross-vendor data points need `[simulated]` flags (Expert 1)
- 2 arithmetic errors in gate count (Expert 2)
- "Exploratory" framing only in Section 6, not abstract (Expert 3)
- 19 statistical claims need flags, 11 are safe (Expert 4)
- Abstract has zero disclosure of simulated status (Experts 5, 7, 10, 11 all converge)
- `.zenodo.json` is broken -- missing `creators` and `version` (Expert 6)
- fig6 misclassified -- should be flagged as simulated (5 figs, not 4) (Expert 9)
- `[Wei2025b]` is a key mismatch -- should be `[Galatolo2025]` (Expert 8)
- 9 new bib entries needed + 26 orphans to prune (Expert 8)

**Phase C execution (main session):**
- Copied 12 PAPER-v2/*.md files to PAPER-v2.2/source/ with new names
- B0 checkpoint saved (12 files in council/checkpoints/B0-source-baseline/)
- Abstract: added "Important methodological note" paragraph, v4 URL
- Data availability: added v4 URL, fixed "in progress" -> "planned but not yet complete"
- Conclusion: added v4 URL
- References: added 9 missing entries (Du2025, IslamicLegalBench2026, IslamicMMLU2026, Kittay1999, Nunnally1994, Snarey1985, Xu2026, Zhang2026, Zheng2024)
- Fixed Wei2025b -> Galatolo2025 citation in methods
- Wrote Appendix K (prompt provenance + system prompt disclosure)
- Wrote REVISION-PROTOCOL.md (v2.2 -> v2.3 upgrade path)

**Phase D: PDF assembly:**
- Forked children paper `generate_v3_combined_pdf.py` -> `build_v22_combined_pdf.py`
- Built 83-page, 2.15MB combined PDF with watermark footer on every page
- Title page: orange "DRAFT -- NOT FOR CITATION" disclosure
- License page: MIT + CC-BY-4.0, all 4 dashboard URLs
- Figures section: 12 PNGs embedded, 5 with `[simulated]` caption flags

### 4. Infrastructure Artifacts

- `.corpus-manifest`: sha256 of data.js + data_cross_vendor.js
- `FIGURE-MANIFEST.txt`: sha256 of all 12 figure PNGs
- `briefing-session19.md`: pre-council briefing doc read by all 24 agents
- `CONTRACT.md`: dashboard implementation contract (CSS classes, script order, theme toggle, banner wording)
- A0 checkpoint: contract snapshot
- B0 checkpoint: 12 source baseline files
- Council synthesis: `DASHBOARD-v4/council/SYNTHESIS.md`
- 24 expert plan files across two councils

---

## Remaining Work

### Priority 1: External Model Runs (USER-DRIVEN, outside Claude Code)

All model administrations deferred per `feedback_no_non_anthropic_models.md`. When real API results land, follow `PAPER-v2.2/REVISION-PROTOCOL.md` for the v2.3 upgrade path.

### Priority 2: Dashboard v4 Polish (can continue)

- B/M/I text blocks on remaining 8 tabs (Overview done, Cross-Vendor done, 8 others need them)
- Chart-level `[simulated]` tags on individual ECharts chart titles (tabs 8-10)
- Provenance badges on Trial Details table (Empirical vs. Simulated per Expert 5)
- `getThemeColors()` helper in charts.js to replace 30 hardcoded hex values
- ECharts dispose/re-init on theme toggle (currently charts stay dark-themed in light mode)
- Hidden data tables for screen reader accessibility (P2, large effort)
- ARIA labels on chart containers, filter controls, sort headers

### Priority 3: Paper v2.2 Polish (can continue)

- Apply `[simulated]` inline flags to results-crossvendor and discussion section text (~38 locations per Expert 1)
- Fix 2 arithmetic errors in methods (gate count sum, PE+CI share per Expert 2)
- Add exploratory framing to abstract and introduction (not just Section 6)
- Blind-review PDF variant (strip author metadata, GitHub URLs, Zenodo DOI)
- Fix `.zenodo.json` (add `creators`, `version` fields per Expert 6)
- Prune 26 orphaned references (Expert 8 recommendations)

### Priority 4: LaTeX / TMLR Template

Set up TMLR `.cls` template and build pipeline. Content insertion waits for Priority 1.

---

## File Locations

| File | Location | Purpose |
|------|----------|---------|
| Dashboard v4 (live) | https://cjimmylin.github.io/cei-normeval-dashboard-v4/ | Cold-readable dashboard with Guide tab |
| Dashboard v4 source | `NORM-ETHICS/DASHBOARD-v4/` | Full source including council artifacts |
| Dashboard v4 deploy | `NORM-ETHICS/DASHBOARD-v4/deploy/` | Allowlisted files for GitHub Pages |
| Paper v2.2 PDF | `NORM-ETHICS/PAPER-v2.2/build/20260413-normeval-paper-v2.2-preliminary.pdf` | 83-page combined PDF |
| Paper v2.2 source | `NORM-ETHICS/PAPER-v2.2/source/` | 13 markdown section files |
| Appendix K | `NORM-ETHICS/PAPER-v2.2/source/appendix-k-prompt-provenance-v2.2-preliminary.md` | System prompt disclosure |
| Revision protocol | `NORM-ETHICS/PAPER-v2.2/REVISION-PROTOCOL.md` | v2.2 -> v2.3 upgrade plan |
| Corpus manifest | `NORM-ETHICS/PAPER-v2.2/.corpus-manifest` | sha256 of data.js for versioning |
| Figure manifest | `NORM-ETHICS/PAPER-v2.2/FIGURE-MANIFEST.txt` | sha256 of all 12 figure PNGs |
| Dashboard synthesis | `NORM-ETHICS/DASHBOARD-v4/council/SYNTHESIS.md` | Consolidated council decisions |
| Dashboard contract | `NORM-ETHICS/DASHBOARD-v4/CONTRACT.md` | Implementation conventions |
| Briefing doc | `NORM-ETHICS/PAPER-v2.2/briefing-session19.md` | Pre-council context for all 24 agents |
| Plan file | `~/.claude/plans/prancy-giggling-truffle.md` | Critique-informed implementation plan |
| Previous handoff | `NORM-ETHICS/METHODS/20260413-normeval-session18-handoff.md` | Session 18 state |

## Known Issues

1. **ECharts charts stay dark-themed in light mode.** The theme toggle switches CSS variables but ~30 hardcoded hex values in `charts.js` don't update. Need `getThemeColors()` helper. Low priority -- the CSS chrome switches correctly.
2. **fig6 (IH/IB scaling) was misclassified in briefing doc** as Anthropic-only. Expert 9 caught it -- all 9 models are plotted. Fixed in PDF caption flags but briefing doc has stale info.
3. **figS3 and figS4 do not exist** -- supplementary numbering jumps S2 to S5. Should be resolved before submission.
4. **`.zenodo.json` still a skeleton** -- missing mandatory `creators` and `version` fields. Must be fixed before Zenodo deposit.
5. **62 orphaned references** -- 20 keep, 16 keep for Paper B, 26 to prune. Pruning deferred to next session.
6. **Abstract is unusually long** (double typical length per Expert 11). May need compression for TMLR submission.

---

*Filed: 2026-04-13 | CEI-Lit-WS/NORM-ETHICS/METHODS/*
