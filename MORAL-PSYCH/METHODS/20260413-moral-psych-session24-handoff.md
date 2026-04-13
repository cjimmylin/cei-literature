# Moral Psychology Benchmarks — Session 24 Handoff

**Date:** 2026-04-13
**Session:** 24 — Dashboard v5 + Paper v5 Combined PDF
**Project:** `CEI-Lit-WS/MORAL-PSYCH/`
**Previous handoff:** `METHODS/20260412-moral-psych-session23-handoff.md`

---

## What Was Done This Session

### Planning Phase — 12-Expert Alternate Critic Council

Assembled 12 alternate critic experts (not plan-phase, but critique-of-plan) in parallel:
1. Version control archaeologist — `git clone` vs `cp -R`, tag discipline
2. First-time reader cognitive psychologist — triad label renaming, glossary, prerequisite knowledge
3. Web security / SRI / CSP — Bootstrap SRI, Google Fonts, CSP
4. Reproducibility engineer — canonical_metrics.json, cross-check scripts, build determinism
5. Agent orchestration skeptic — voice bible, integrator, P0 abort gate
6. Moral psychology domain expert — triple-bind framing, Claim 7 causation, MFT operationalized caveat
7. Pandoc / Typst failure-mode expert — **P0: hardcoded filename literals would silently produce empty PDF**
8. WCAG 2.2 AA accessibility — axe-core gates, semantic HTML, contrast targets
9. GitHub Pages deploy skeptic — `.nojekyll`, Pages API, poll-until-built, cache-bust
10. YAGNI / scope auditor — recommended cutting 60→10 agents, dropped help drawer
11. Long-term maintainer — sprawl veto, handoff requirements, MEMORY.md discipline
12. Adversarial red-team — `20260405-` prefix laundering, aiDisclosure under-disclosure, `.git` copy bug

### Key P0 Findings Integrated

- **C7-F1:** Parameterized `build_combined_pdf.py` with `VERSION`/`DATE` constants (prevented empty PDF)
- **C12-F1:** Section files renamed to `20260413-*-v5.md` (date integrity)
- **C12-F2:** New ~40-word aiDisclosure covering triad content
- **C12-F4:** Used `cp -R` + `rm -rf .git` + `git init` (prevents v4 history leaking into v5)
- **C2-F1:** Renamed "Background/Method/Interpretation" → "What is this about? / How did we measure it? / What does it mean?"
- **C5-F2:** Voice bible authored before execution wave (single canonical voice)
- **C6 guardrails:** "most operationalized" (C1), "measurement gap" (C4), "correlation not causation" (C7)

### Deliverable 1: Dashboard v5 — COMPLETE

**Repo:** https://github.com/cjimmylin/cei-moral-psych-dashboard-v5
**URL:** https://cjimmylin.github.io/cei-moral-psych-dashboard-v5/
**Tag:** `v5.0-s24` (commit `946eff6`)

New features:
- **Start Here tab** as default landing — 3-paragraph orientation for first-time readers
- **Contextual triads** on all 7 claim cards (collapsed, expand on hover/focus)
- **Study-level triads** in executive summary
- **Narrative tour triads** on all 4 steps
- **Updated aiDisclosure** (~40 words, covers triad content)
- **Content guardrails** verified: all 3 mandatory phrases present
- **WCAG AA:** semantic `<section role="region" aria-labelledby>`, `aria-pressed` on theme toggle, `:focus-visible` ring
- **Cache-bust** `?v=v5.0-s24` on all local assets
- **`.nojekyll`** for Pages deploy

### Deliverable 2: Paper v5 Combined PDF — COMPLETE

**Output:** `PAPER-v5/20260413-mpbench-v5-combined.pdf` — **5.29 MB**

- 9 main sections + 3 supplementary + 15-figure plate
- Build script parameterized: `VERSION = "v5"`, `DATE = "20260413"` (C7-F1 fix)
- Unicode NFC normalization + C0/C1 control strip (C7-F5)
- `--resource-path` added to pandoc (C7-F4 belt-and-suspenders)
- Section-count assertion: aborts if any main section missing
- Figure-count warning if < 15
- Combined-content guard: aborts if < 100K characters
- `MANIFEST.sha256` for 15 figure PNGs
- `canonical_metrics.json` — single source of truth for both paper and dashboard
- `DASHBOARD_PIN.txt` — pins dashboard commit `946eff6`

### Pre-Flight Artifacts

| File | Purpose |
|------|---------|
| `DASHBOARDS/contract.md` | DOM/data contract for parallel agents |
| `DASHBOARDS/voice_bible.md` | Canonical triad strings for 7 claims |
| `DASHBOARDS/DEPLOY.md` | Deploy registry (v4 + v5 URLs) |

---

## Triad-Key Schema Diff vs v4

### data.js new keys (v5 only)
```
DATA.executiveSummary.startHere         → { title, paragraphs[] }
DATA.executiveSummary.contextAbout      → string
DATA.executiveSummary.contextMeasure    → string
DATA.executiveSummary.contextMeaning    → string
DATA.claimCards[N].contextAbout         → string
DATA.claimCards[N].contextMeasure       → string
DATA.claimCards[N].contextMeaning       → string
DATA.narrativeTour[N].contextAbout      → string
DATA.narrativeTour[N].contextMeasure    → string
DATA.narrativeTour[N].contextMeaning    → string
```

### New CSS classes
`.ctx-block`, `.ctx-about`, `.ctx-measure`, `.ctx-meaning`, `.ctx-label`, `.ctx-text`, `.start-here-panel`

### New DOM
`#tab-start-here`, `#pane-start-here`, `#start-here-content`

---

## Critic Findings — Accepted / Deferred

### Accepted (implemented)
- C7-F1: Parameterized build script (P0)
- C12-F1: Date prefix consistency
- C12-F2: New aiDisclosure
- C12-F4: .git directory isolation
- C1-F1: git clone lineage
- C2-F1: Reader-facing triad labels
- C5-F2: Voice bible pattern
- C5-F3: Integrator QA step
- C6-F1/F2/F4: Content guardrails
- C8-F3: Semantic HTML sections
- C9-F1: Pages API enable
- C9-F2: .nojekyll
- C9-F5: Cache-bust query strings
- C4-F1: canonical_metrics.json

### Deferred (out of scope for S24)
- C3-F1: Self-hosted fonts (privacy, offline resilience)
- C3-F4: Content Security Policy meta tag
- C11-F1: Extract `moral-psych-benchmarks-common/` shared code
- C2-F3/F5: Forced first-visit modal + wizard + glossary tooltip lib
- C4-F3: Byte-reproducible PDFs
- C8-F1: axe-core automated run (manual a11y check done instead)

---

## File-Partition Map (Execution Agents)

| Agent | File(s) | Status |
|-------|---------|--------|
| generate_dashboard.py | `generate_dashboard.py` only | COMPLETE |
| app.js renderer | `app.js` only | COMPLETE |
| style.css + index.html | `style.css`, `index.html` | COMPLETE |
| Integrator QA | Read-only verification | COMPLETE |

---

## Known Issues for v6

1. **N ≥ 5 parallel dashboards** — consolidation trigger reached. Next session's FIRST task should be extracting `moral-psych-benchmarks-common/` before creating v6 (C11-F1, C11-F5).
2. **S16–S19 supplementary PNGs** still not generated (UMAP, Treemap, Feature Importance, Pre/Post RLHF).
3. **N=1 per model** — no inferential statistics (carried from S21).
4. **axe-core automated audit** not run — recommend as v6 pre-deploy gate.
5. **Google Fonts privacy** — still loading from Google CDN (C3-F3 deferred).
6. **No CSP header** — GitHub Pages has no CSP; meta tag deferred (C3-F4).

---

## Verification Results

| Test | Result |
|------|--------|
| data.js: 49 keys, 7 claim cards, 4 tour steps | PASS |
| Start Here tab default active | PASS |
| 36 triad blocks in DOM | PASS |
| 3 guardrail phrases in data.js | PASS |
| Hash routing (#tab=pane-methodology) | PASS (on reload) |
| Theme toggle light ↔ dark | PASS |
| aria-pressed updates on toggle | PASS |
| 1440px layout | PASS |
| 768px responsive | PASS |
| Console errors | favicon 404 only |
| Pages build status | built |
| Live URL title | "MPBench v5 — The Triple Bind" |
| Paper v5 PDF size | 5.29 MB (matches v4) |
| Paper v5 section count | 9/9 |
| Paper v5 figure count | 15/15 |

---

*Filed: 2026-04-13 | CEI-Lit-WS/MORAL-PSYCH/METHODS/*
