# Methods: Dashboard v5 Contextual Triads and Paper v5 Combined PDF

**Date:** 2026-04-13
**Project:** `CEI-Lit-WS/MORAL-PSYCH/`

## Data and Materials

The primary input was the existing moral psychology benchmarks dashboard v4 (commit `afed1a0`, tag `v4.1-s23`) containing pre-computed analytics across 292 benchmark candidates, 9 models from 3 vendors, and 23 administered benchmarks. The dashboard's `data.js` (542 KB, 21,253 lines) served as the data layer, with `generate_dashboard.py` (2,442 lines) as the canonical data pipeline. The paper v4 manuscript (`PAPER-v4/`) comprised 9 main sections, 3 supplementary sections, and 15 main-text figures, built via `pandoc 3.9` with `typst 0.14.2` as PDF engine.

## Procedure

### Phase 1: Critic Council Assembly

A 12-expert alternate critic council was dispatched in parallel (one agent per persona, no shared state). Each critic read the initial implementation plan and the relevant source files, returning 3-5 targeted findings from their domain angle. Personas included: version control archaeologist, first-time reader cognitive psychologist, web security/SRI specialist, computational reproducibility engineer, agent orchestration skeptic, moral psychology domain expert, pandoc/typst failure-mode specialist, WCAG 2.2 AA accessibility auditor, GitHub Pages deploy engineer, YAGNI scope auditor, long-term maintainer, and adversarial red-team critic.

Critic findings were triaged by severity (P0 = would ship broken silently; P1 = would confuse users; P2 = nice-to-have). Three P0 findings were identified: (1) hardcoded section filenames in the build script would silently produce an empty PDF on rename; (2) the aiDisclosure string under-disclosed newly generated content; (3) `cp -R` of the v4 dashboard directory would copy its `.git` directory, leaking v4 history into the v5 repository.

### Phase 2: Pre-Flight Artifacts

Three coordination artifacts were authored before execution:

1. **DOM/Data Contract** (`contract.md`): Specified all new CSS classes, DOM IDs, data.js key names, semantic HTML structure, and content guardrail phrases. This served as the shared API contract preventing parallel agent drift.

2. **Voice Bible** (`voice_bible.md`): A single author produced canonical three-paragraph triads for all 7 claims plus the study-level summary and Start Here panel. Triads used reader-facing question labels ("What is this about?" / "How did we measure it?" / "What does it mean?") rather than IMRaD-derived terminology, following Critic 2's recommendation that the scaffolding itself needed to avoid academic jargon.

3. **Canonical Metrics JSON** (`canonical_metrics.json`): All quantitative claims were extracted verbatim from the paper v4 conclusion into a machine-readable single source of truth, preventing the dashboard-paper number-drift pattern observed in prior projects.

### Phase 3: Dashboard v5 Construction

Three file-partitioned execution agents worked in parallel, each editing exactly one file (or non-overlapping file pair):

- Agent A: `generate_dashboard.py` — added `VERSION`/`DASHBOARD_VERSION` constants, inserted triad keys (`contextAbout`, `contextMeasure`, `contextMeaning`) into all 7 claim card dicts, 4 narrative tour step dicts, and the executive summary dict. Replaced the 29-word aiDisclosure with a ~40-word version covering triad content.

- Agent B: `app.js` — added `renderStartHere()` function, extended `renderClaimCards()` and `renderExecutiveSummary()` with semantic `<section role="region" aria-labelledby>` triad blocks, updated `ThemeManager` with `aria-pressed` support, bumped localStorage key from `v4` to `v5`.

- Agent C: `style.css` + `index.html` — added triad block CSS (`.ctx-block`, `.ctx-about`, `.ctx-measure`, `.ctx-meaning`) with colored left borders, collapse/expand animation on claim cards, light/dark theme variants with WCAG AA contrast ratios. Added "Start Here" tab as default active, cache-bust query strings `?v=v5.0-s24`, `.nojekyll` file.

Data.js was regenerated via `python3 generate_dashboard.py`, producing 574 KB (49 top-level keys, up from ~542 KB in v4).

### Phase 4: Paper v5 Construction

Section files were copied from `PAPER-v4/sections/` to `PAPER-v5/sections/` with date prefix updated from `20260405` to `20260413` and version suffix from `-v4` to `-v5`. The build script (`build_combined_pdf.py`) was parameterized with `VERSION = "v5"` and `DATE = "20260413"` constants, with all section filename lists constructed via f-strings rather than hardcoded literals. Additional safety measures included: unicode NFC normalization + C0/C1 control stripping in the preprocessor, `--resource-path` argument to pandoc, section-count assertion (abort if any main section missing), figure-count warning (if < 15), and combined-content guard (abort if < 100K characters).

Figures were copied (not symlinked) with a SHA-256 manifest (`MANIFEST.sha256`) for provenance tracking. The dashboard commit SHA was pinned in `DASHBOARD_PIN.txt`.

### Phase 5: Deployment

The v4 repository was tagged `paper-v4-frozen` before v5 work began. The v5 dashboard was deployed to a new public repository (`cjimmylin/cei-moral-psych-dashboard-v5`) via discrete steps: `gh repo create` (separate from push), `git push -u origin main`, `gh api -X POST .../pages` to enable Pages, then polling `gh api .../pages/builds/latest` until `status=="built"` before URL verification.

## Analysis

### Integrator Verification

Post-generation verification used Node.js `vm.createContext` to parse `data.js` (which uses `const DATA = {...}` format incompatible with direct `eval` in Node's strict mode). Assertions checked: 49 top-level keys, 7 claim cards each with 3 triad keys, 4 narrative tour steps, Start Here panel with 3 paragraphs, and presence of all 3 mandatory guardrail phrases.

### Visual QA

Playwright MCP was used for browser-based verification at 1440px and 768px viewports. Tests included: Start Here tab renders as default, Overview tab shows claim cards with triad blocks, hash routing (`#tab=pane-methodology`) activates correct tab on reload, theme toggle updates `data-theme` attribute and `aria-pressed`, console errors limited to expected favicon 404.

## Computational Environment

- Python 3.14.3 (system), pandoc 3.9, typst 0.14.2
- Node.js v24.13.1 for JS verification
- Playwright MCP for browser automation
- GitHub CLI (`gh`) for repository creation and Pages deployment
- macOS Darwin 25.3.0

## Limitations and Decisions

1. **No axe-core automated audit** — manual accessibility verification was performed via Playwright snapshot inspection and contrast ratio specification, but no automated a11y tool was run. Deferred to v6.

2. **Content unchanged from v4** — Section text was carried forward verbatim from paper v4; the v5 bump reflects the new build infrastructure (parameterized constants, safety guards) and triad additions to the dashboard, not new analytical content.

3. **S16-S19 supplementary figures still missing** — Four supplementary figures (UMAP, Treemap, Feature Importance, Pre/Post RLHF) remain ungenerated. The build script's `--allow-missing` behavior (warn but continue) was retained.

4. **Dashboard code sprawl** — With 5 parallel dashboard directories (v1-v5), each a full code fork, maintenance debt is accumulating. The consolidation trigger (extract `moral-psych-benchmarks-common/`) was recorded but deferred.

5. **Voice bible authored by AI** — All triad text was generated by Claude without human expert review. The aiDisclosure string explicitly notes this. Content guardrails (mandatory phrases for Claims 1, 4, 7) were verified programmatically.
