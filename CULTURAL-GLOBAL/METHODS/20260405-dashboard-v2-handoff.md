# Cross-Cultural Benchmarks Dashboard v2 -- Session Handoff

**Date:** 2026-04-05
**Session:** Multi-vendor expansion + 12-member UX council review + v2 implementation
**Project:** `CEI-Lit-WS/CULTURAL-GLOBAL/`
**Previous handoff:** `METHODS/20260404g-council-analysis-handoff.md`

---

## What Was Done This Session

### 1. Bug Fixes from Previous Session

- **Playwright Chrome instability**: Created `~/.claude/cleanup-playwright.sh` SessionStart hook to auto-remove stale `mcp-chrome-*` profiles. Verified it cleaned 1 actual stale profile.
- **Hard cases table CSS**: Unified 3 competing background-color layers (CSS rules, `:nth-child`, JS inline) to explicit hex values (`#1c2128` / `#21262d`). Added `!important` on stripe rule.

### 2. Multi-Vendor Dashboard Expansion (v1 update)

Expanded Tabs 2 and 3 from Claude-only to 10 models across 3 providers:

| Tab | Before | After |
|-----|--------|-------|
| Tab 2 (Trials) | Claude Opus only | 3-provider grouped (MFQ, RLHF radar, alignment, engagement) |
| Tab 3 (Comparison) | 3 Claude models | 6 representatives (3 Claude + Gemini ×5 + 2 GPT) |
| Tab 4 (Council) | Already 10 models | Provider colors aligned to tier scheme |

**New data constants:** `MODEL_COLORS_10`, `MODEL_SHORT`, `PROVIDER_COLORS`, `ALL_MODEL_RATIOS`, `COUNCIL_ALIGNMENT_PROVIDER`, `COUNCIL_RLHF_TOTALS`, `COUNCIL_PAIRWISE_MATRIX`

**New CSS:** `.prov-badge` (3 tier variants), `.prov-notice` provenance banner

3 commits deployed to GitHub Pages (`d9957fd`, `a7ebea2`).

### 3. 12-Member UX Council Review

Assembled expert panel and produced comprehensive critique (`METHODS/20260405-dashboard-ux-council-review.md`, ~4,500 words):

| # | Expert | Domain |
|---|--------|--------|
| 1-3 | Chen, Asante, Marchetti | Visualization, Accessibility, Dashboard Design |
| 4-6 | Patel, Tanaka, Silva | Scientific Communication, Typography, Color Theory |
| 7-9 | Okafor, Mahmoud, Eriksson | Cross-Cultural Design, Academic Writing, Frontend |
| 10-12 | Krishnamurthy, Müller, Wei | Psychometrics, HCI, Infographic Design |

**22 issues identified** across 9 domains, with priority matrix (P0-P4) and council vote counts.

### 4. Dashboard v2.0 Implementation

Implemented ALL 22 council recommendations in new `generate_benchmark_tab_v2.py` (preserving v1):

| Category | Key Changes |
|----------|-------------|
| **P0 Critical** | Tab 2/3 restructured to eliminate redundancy; Okabe-Ito colorblind-safe palette |
| **P1 High** | 22 collapsible `<details>` descriptions; glossary tooltips (MFQ, RLHF, WEIRD); radar→dot strip chart; hash-based tab routing |
| **P2 Medium** | Sticky tab bar; back-to-top button; 6 section dividers; ECharts decal patterns (solid/striped/dotted by provenance); text deduplication |
| **P3 Low** | Font size 0.82→0.88rem; "Subst."→"Substantive"; monocultural design acknowledgment; Pearson/Spearman footnote |

**Output:** `benchmarks-v2.html` (117KB) + `benchmark-data-v2.js` (66KB). Deployed as commit `69af812`.

### 5. Header Contrast Fix

Table `th` headers changed from `#8b949e` (4.2:1 contrast) to `#c9d1d9` (8:1 contrast) — WCAG AA compliant for small text.

---

## Remaining Work

### Priority 1: Console Error Investigation
1 console error persists across both v1 and v2. Non-critical (all 18 charts render), but should be investigated and fixed for quality.

### Priority 2: Real Gemini/GPT Trials
Council P2/P3: Replace template-derived Gemini and Codex-authored GPT data with real API responses. Scripts exist: `TRIALS/run_gemini_trials.py`.

### Priority 3: LaTeX Conversion
Both the cross-cultural paper and benchmark report need LaTeX for journal submission.

### Priority 4: EXSR0697 Key Collision
Still unresolved from Session 6a. `EXSR0697` collision between Islamic Ethics Trusteeship and Klingefjord Moral Graph.

### Priority 5: v2 → Default Deployment
The user may want `benchmarks-v2.html` to become the default `benchmarks.html`. Currently v1 and v2 coexist as separate files.

---

## File Locations

### Files Created This Session
| File | Location | Purpose |
|------|----------|---------|
| Playwright cleanup hook | `~/.claude/cleanup-playwright.sh` | SessionStart auto-cleanup |
| Dashboard v2 generator | `SCRIPTS/generate_benchmark_tab_v2.py` | v2 Python generator (2533→~2600 lines) |
| Dashboard v2 HTML | `DASHBOARD/benchmarks-v2.html` | 117KB self-contained dashboard |
| Dashboard v2 data | `DASHBOARD/benchmark-data-v2.js` | 66KB pre-computed analytics |
| UX council review | `METHODS/20260405-dashboard-ux-council-review.md` | 22-issue expert critique |
| Screenshots (8) | `screenshots/council-review-*.png`, `screenshots/v2-*.png` | Pre/post verification |

### Files Modified This Session
| File | Change |
|------|--------|
| `~/.claude/settings.json` | Added Playwright cleanup SessionStart hook |
| `SCRIPTS/generate_benchmark_tab.py` | v1 multi-vendor expansion (CSS fix + provider charts) |
| `DASHBOARD/benchmarks.html` | Regenerated v1 (99→114KB) |
| `DASHBOARD/benchmark-data.js` | Regenerated v1 (62→66KB) |

### Dashboards
| Version | URL | Generator |
|---------|-----|-----------|
| v1 (multi-vendor) | https://cjimmylin.github.io/cei-cultural-global/benchmarks.html | `generate_benchmark_tab.py` |
| v2 (council-reviewed) | https://cjimmylin.github.io/cei-cultural-global/benchmarks-v2.html | `generate_benchmark_tab_v2.py` |
| Main dashboard | https://cjimmylin.github.io/cei-cultural-global/ | `index.html` (14-tab, separate) |

---

## Known Issues

1. **1 console error** — non-critical, inherited from v1. All charts render. Likely a reference to an undefined variable in a fallback code path.
2. **Gemini data identical** — all 5 Gemini models produce identical metrics (template-derived). Communicated via provenance badges and Gemini ×5 collapse.
3. **GPT data Codex-authored** — GPT-5.4/Mini responses generated through Codex, not direct OpenAI API. Marked as Tier 2.
4. **v2 Tab 2 trial difficulty chart** — only shows CC3/CC4/CC5 because `COUNCIL_HARD_CASES` data is limited to those trials. A more complete version would compute variance from the full trial data.

---

*Filed: 2026-04-05 | CULTURAL-GLOBAL/METHODS/*
