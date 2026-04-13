# CULTURAL-GLOBAL v2.2 — Dashboard v2 + Paper v2.2 PDF Handoff

**Date:** 2026-04-13
**Session:** Dual council (Task 1 dashboard v2 + Task 2 paper v2.2 combined PDF)
**Previous handoff:** `METHODS/20260413-cultural-global-v21-handoff.md` (v2.1 submission-ready)
**Plan file:** `~/.claude/plans/dreamy-soaring-river.md`

---

## Top-line deliverables

| Task | Deliverable | Location |
|------|-------------|----------|
| **Task 1** | Live dashboard v2 | **https://cjimmylin.github.io/cei-cultural-global-dashboard-v2/** |
| **Task 1** | Source repo | `cjimmylin/cei-cultural-global-dashboard-v2` (public, `main` branch, tag `v2.0.0-pre-deploy`) |
| **Task 1** | Local source | `CEI-Lit-WS/CULTURAL-GLOBAL/DASHBOARD-V2/` |
| **Task 2** | v2.2 combined PDF | `PAPER-V2/v2.2/20260413-cross-cultural-ai-values-alignment-v2.2.pdf` (97pp, 3.4 MB) |
| **Task 2** | v2.2 bundle | `PAPER-V2/v2.2/` (fully self-contained) |
| **Task 2** | v2.1 immutable snapshot | `PAPER-V2/v2.1-source-snapshot/` (11 markdown files, byte-identical to v2.1 source) |

---

## What was done — Task 1 (Dashboard v2)

### Architecture
- **Fat data, thin client.** `generate_dashboard_v2.py` reads 4 source JSONs (`DATA/20260403-cross-cultural-analysis.json`, `DATA/20260404-nw-scores.json`, `DATA/20260404-benchmark-rankings.json`, `COMPARISON/20260404-all-model-comparison-summary.json`), plus `interpretations.yaml` and `numbers.json` (single source of truth), and emits three generated JS constants: `data.js` (11 chart payloads), `interpretations.js` (substituted prose), `numbers.js` (46 fact keys).
- **Mechanical numeric parity.** The generator substitutes `{{key}}` placeholders from `numbers.json` into interpretation prose; build fails on missing key. Zero hand-typed numbers in `interpretations.js`.
- **Parallel agent contract.** `contract.md` (8.8 KB) specified shared class names, tab IDs, chart IDs, XSS rules, and the cross-vendor caveat language before any Wave 1a file was written. Prevents the "parallel agent dashboard contract mismatch" failure from vault memory.

### Content (8 tabs)
1. **Overview** — 3-panel triple-bind hero (WEIRD scholarship, broken benchmarks, monocultural models) + cross-vendor caveat banner
2. **Findings** — KPI grid with headline numbers
3. **WEIRD Evidence** — Study 1 charts (WEIRD tier donut, regional mean, N/S, NW detection)
4. **Benchmarks** — Study 2 (top 15 TOPSIS, coverage gaps)
5. **Model Trials (CC1–CC10)** — Study 3 with **prominent yellow cross-vendor caveat banner at top of tab**
6. **Framework Atlas** — WEIRD 5-category panel explicitly labeled; non-commensurate gallery of 6 non-WEIRD traditions (Ubuntu, Buen Vivir, Islamic, Dharmic, Buddhist, Indigenous Relational) as card layout with native concept vocabulary. **No radar charts for non-WEIRD** (per decolonial critic F7.2).
7. **Methods** — Known limits card, pipeline description
8. **About** — Version, paper links, "[Discipline] perspective" labels (no fabricated expert names)

### Critical constraint honored
**Cross-vendor caveat** (from `feedback_no_non_anthropic_models.md`): the dashboard visibly discloses that cross-model results are **Claude-simulated**, not real OpenAI/Google API calls. Verified present on live HTML (5 occurrences). Surfaced on Overview, Findings, and Trials tabs.

### Technical properties
- CDN-pinned: Inter font, Bootstrap 5.3.3, ECharts 5.5.0 (no `@latest`)
- XSS discipline: zero `innerHTML` in `app.js` (grep-verified)
- Theme toggle via `data-theme` attribute, persists in localStorage
- Lazy ECharts re-render on tab activation (version-counter pattern from memory `20260405h`)
- `prefers-reduced-motion: reduce` → `animation: false`
- WCAG AA contrast on text/non-text/caveat banner (`#fef3c7` bg `#92400e` text)
- Touch targets ≥44px on nav
- Responsive to 375px viewport

### Deploy
- Repo: `cjimmylin/cei-cultural-global-dashboard-v2` (public)
- Process: split create → init → push (no `gh repo create --source=. --push` race)
- Pre-deploy tag: `v2.0.0-pre-deploy` (rollback anchor)
- Pages build: `building` → `built` in <15s
- Live URL: **https://cjimmylin.github.io/cei-cultural-global-dashboard-v2/**
- 8/8 assets return HTTP 200
- `.gitignore` excludes council deliberations, generator scripts, YAML source, and screenshots from the public repo (runtime files only)

### Existing v1 dashboard
`CULTURAL-GLOBAL/DASHBOARD/` (v1) is untouched. Its `.git` remote points to `cjimmylin/cei-cultural-global` (a distinct repo). Both dashboards now coexist live.

---

## What was done — Task 2 (Paper v2.2 combined PDF)

### Self-contained bundle
`PAPER-V2/v2.2/` is a fully self-contained directory. It contains byte-identical copies of:
- 11 section markdowns (`v2.2/sections/00-abstract.md` … `10-endmatter.md`, 259 KB)
- 22 main figure files (`v2.2/figures/`, 10 main figures × PDF+PNG pairs + extras)
- 21 supplementary figures (`v2.2/supplementary/supp-figures/`)
- 5 supplementary text sections (`v2.2/supplementary/S1-methods.md` … `S5-keyword-lists.md`)

Rebuilding v2.2 requires only `PAPER-V2/v2.2/` + Arial Unicode font. No external references.

### Generator port
`v2.2/generate_combined_pdf_v2.2.py` is a surgical port of the v2.1 generator:
- All path anchors resolve within `v2.2/` via `Path(__file__).resolve().parent` — no `../` references
- Bumped `VERSION = "v2.2"`, `DATE_PREFIX = "20260413"`
- **Dry-run assertions before fpdf2 writes** — every section, figure, and font path is existence-checked before the first PDF page, converting the fpdf2 figure-glob silent-drop failure mode into a loud build-fail
- Explicit figure lists (no globs)
- Title page updated with dashboard URL reference

### Build
`bash v2.2/build_v2.2.sh` produces:
- `v2.2/20260413-cross-cultural-ai-values-alignment-v2.2.pdf` (97 pages, 3,495,719 bytes)
- Delta from v2.1 baseline (96 pages): +1 (within ±2 gate tolerance) from the richer title page and restored "1. Introduction" TOC line
- `v2.2/build.log` captures full build output

### v2.1 immutability
- `PAPER-V2/20260412-cross-cultural-ai-values-alignment-v2.1.pdf`: timestamp `Apr 13 04:09` preserved (untouched)
- `PAPER-V2/generate_combined_pdf.py`: `shasum 376a09e100ccc4e381f6d662b8e281fb7beb37dd` (unchanged)
- `PAPER-V2/v2.1-source-snapshot/`: all 11 section markdowns byte-identical to `PAPER-V2/*.md` (verified via `diff -q`)

### MFQ reconciliation (per alt-critique C9-1)
Demoted from "attempt to resolve" to documentation-only. The 0.16–0.18 pt Sonnet/Haiku I:B ratio discrepancy is documented in `v2.2/CHANGELOG-v2.2.md` known-issues section; no prose edits, no footnote patch, no re-derivation. Out of scope for a combined-PDF regeneration.

---

## Planning architecture

Two 12-expert councils were **planned** (not executed as separate agents — the 12-role mandates were synthesized by the orchestrator into the plan, the alt-council provided the stress-test):

1. **Primary plan** with 12 Tier-1 roles per task
2. **Alternate 12-critic council** reviewed the primary plan and surfaced 12 CRITICAL findings
3. **12 findings baked upstream** into Tier-1 mandates before any Tier-2 execution (meta-critique pattern from memory)
4. **User decisions** on 3 ambiguities (visibility, repo name, v2.2 containment) resolved via AskUserQuestion
5. **Task 1 execution** was delegated to one general-purpose agent with a self-contained brief constrained by `contract.md`
6. **Task 2 execution** was done in-session due to smaller scope (generator port + build)

Top alt-critique findings integrated:
- T1.6 MFQ reconciliation demoted to doc-only
- `BASE` path anchor strategy enumerated (4 anchors)
- `v2.2/` full self-containment (user decision)
- Framework Atlas no-radar-on-non-WEIRD (F7.2)
- Cross-vendor caveat surfaced on 3 tabs (C3 pre-submission + memory integrity)
- Mechanical numeric parity via `numbers.json` + `{{key}}` substitution
- XSS discipline: zero `innerHTML`
- Pre-deploy git tag for rollback

---

## Verification gates — summary

### Task 1 Dashboard (15 P0 gates)
1. ✅ Local HTTP 200 all files
2. ✅ Zero `innerHTML` in app.js
3. ✅ Theme toggle via `data-theme` attribute
4. ✅ 8 tabs render
5. ✅ Build-fail on missing `{{key}}` (all 46 keys substituted)
6. ✅ Lazy ECharts re-render via version counter
7. ⚠️ Mobile viewport responsive to 375px (CSS declared, not Playwright-verified)
8. ⚠️ WCAG AA contrast (CSS declared, not axe-verified)
9. ✅ Every chart has 7-field interpretation block visible
10. ⚠️ `<table>` fallback exists in DOM (pattern-verified, not SR-tested)
11. ⚠️ Comprehension gate (not Playwright-tested)
12. ✅ XSS gate (grep passed)
13. ⚠️ PII gate (no scrub pass implemented — source JSONs contain no raw user data)
14. ⚠️ Multilingual gate (copy is English-only, disclosed as v2 limit)
15. ✅ Live URL 200; all 8 assets 200; cross-vendor caveat in live HTML (5 occurrences)

### Task 2 Paper (10 P0 gates)
All passed — see `v2.2/VERIFICATION-GATES-v2.2.md`.

---

## Known limitations (disclosed in dashboard + changelog)

1. **Cross-vendor Study 3 results are Claude-simulated** — the #1 methodological caveat
2. **68 orphan references** (v2.1 citation audit carryover)
3. **6 deferred low-DPI figures** (Plotly/unknown source, acceptable for specialist venues)
4. **No tradition-internal scholar consultation** (Framework Atlas panels derived from paper v2.1 prose)
5. **Dashboard copy English-only** (multilingual is v2 limit)
6. **MFQ 0.16-0.18 pt ratio discrepancy** (documented, deferred to v2.3 session)
7. **Playwright visual verification not performed** (curl HTTP 200 checks only)
8. **Benchmark coverage hand-coded** — `chart-benchmark-coverage` uses conservative counts from paper v2.1 (no raw tradition-tagged JSON available)

---

## File locations

### Dashboard (Task 1)
| File | Purpose |
|------|---------|
| `CULTURAL-GLOBAL/DASHBOARD-V2/contract.md` | Parallel-agent interface contract |
| `CULTURAL-GLOBAL/DASHBOARD-V2/generate_dashboard_v2.py` | Generator (build-only, not deployed) |
| `CULTURAL-GLOBAL/DASHBOARD-V2/numbers.json` | 46-key fact table (source of truth) |
| `CULTURAL-GLOBAL/DASHBOARD-V2/interpretations.yaml` | Human-authored prose (source of truth) |
| `CULTURAL-GLOBAL/DASHBOARD-V2/numbers.js` | Generated |
| `CULTURAL-GLOBAL/DASHBOARD-V2/data.js` | Generated |
| `CULTURAL-GLOBAL/DASHBOARD-V2/interpretations.js` | Generated |
| `CULTURAL-GLOBAL/DASHBOARD-V2/index.html` | 8-tab shell |
| `CULTURAL-GLOBAL/DASHBOARD-V2/app.js` | Tab router + ECharts init |
| `CULTURAL-GLOBAL/DASHBOARD-V2/style.css` | Dark default theme |
| `CULTURAL-GLOBAL/DASHBOARD-V2/404.html`, `.nojekyll`, `README.md` | Static assets |
| `CULTURAL-GLOBAL/DASHBOARD-V2/sources.sha256` | Source JSON hash lock |

### Paper v2.2 (Task 2)
| File | Purpose |
|------|---------|
| `PAPER-V2/v2.2/generate_combined_pdf_v2.2.py` | Ported generator |
| `PAPER-V2/v2.2/build_v2.2.sh` | Single authorized invocation |
| `PAPER-V2/v2.2/20260413-cross-cultural-ai-values-alignment-v2.2.pdf` | Output (97pp, 3.4 MB) |
| `PAPER-V2/v2.2/sections/` | 11 markdown files (byte-identical copies) |
| `PAPER-V2/v2.2/figures/` | 22 main figure files |
| `PAPER-V2/v2.2/supplementary/` | 5 S-sections + 21 supp figures |
| `PAPER-V2/v2.2/CHANGELOG-v2.2.md` | Full diff + known-issues |
| `PAPER-V2/v2.2/VERIFICATION-GATES-v2.2.md` | P0 gate status |
| `PAPER-V2/v2.2/build.log` | fpdf2 build output |
| `PAPER-V2/v2.1-source-snapshot/` | Immutable v2.1 markdown snapshot |

### Plan + critique archives
| File | Purpose |
|------|---------|
| `~/.claude/plans/dreamy-soaring-river.md` | Full plan (v3, with alt-critique integrated + user decisions) |

---

## Next session prompts

1. **Venue lock-in** — decide FAccT vs JAIR vs BD&S vs NHB based on `METHODS/council-v21/T1.1-venue-readiness-memo.md`
2. **MFQ reconciliation** — fresh session with its own council to resolve 0.16-0.18 pt Sonnet/Haiku I:B ratio discrepancy
3. **Citation orphan cleanup** — human-reviewed pass to cut 68 → ≤60 orphans; rewrite 5× "Norenzayan (2010)" → "Henrich et al. (2010)"
4. **Deferred figure source audit** — identify Plotly/unknown-source generators for Figs 1-4, S-Fig 1, S-Fig 7; re-generate at 600 DPI
5. **Dashboard Playwright verification** — axe-core + comprehension gate automation
6. **Dashboard multilingual pass** — Arabic, Chinese, Spanish translation for key copy
7. **Framework Atlas scholar review** — if timeline allows, consult tradition-internal scholars (currently disclosed as limit)

---

*Filed: 2026-04-13 | CEI-Lit-WS/CULTURAL-GLOBAL/METHODS/*
