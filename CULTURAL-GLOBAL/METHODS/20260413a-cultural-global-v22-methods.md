# Methods: Cross-Cultural AI Values Alignment — Dashboard v2 and Paper v2.2

**Date:** 2026-04-13
**Project:** `CEI-Lit-WS/CULTURAL-GLOBAL/`

## Data and Materials

The session processed four machine-readable source datasets derived from prior cultural-global analyses, all accessed in read-only mode:

- `DATA/20260403-cross-cultural-analysis.json` (55 KB): regional profiles for 2,315 AI ethics papers across ten macro-regions (South Asia, North America, East Asia, Western Europe, Sub-Saharan Africa, Latin America and Caribbean, Oceania, Middle East and North Africa, Eastern Europe and Central Asia, Southeast Asia), with 34 measurement dimensions including five WEIRD normative frameworks, seven non-Western frameworks (nw_*), fourteen religious-values framings (rv_*), and eight moral-psychology operationalizations (mp_*). The dataset also includes a WEIRD tier comparison across four score bins, a North/South/Ambiguous comparison, and summary statistics (mean WEIRD score 63.4; high-WEIRD percentage 56.0%).
- `DATA/20260404-nw-scores.json` (824 KB): paper-level non-Western framework scores for 2,368 papers, with per-field detection counts at a ≥50 score threshold (nw_indigenous_relational: 51; nw_confucian: 39; nw_islamic_ethics: 31; nw_ubuntu: 24; nw_buddhist: 22; nw_dharmic: 19; nw_buen_vivir: 8).
- `DATA/20260404-benchmark-rankings.json` (162 KB): TOPSIS-ranked list of 218 benchmarks under an ELECTRE-III veto rule, with an eight-dimensional weight scheme, five sensitivity schemes, and a Kendall's W of 0.9242 indicating high rank stability.
- `COMPARISON/20260404-all-model-comparison-summary.json`: per-model aggregate statistics across ten model identifiers (Anthropic Claude Haiku 4.5, Opus 4.6, Sonnet 4.6; Google Gemini 2.5 Flash, Flash-Lite, Pro; Gemini 3.1 Flash-Lite Preview, Pro; OpenAI GPT-5.4, GPT-5.4-mini). Per an environmental constraint, non-Anthropic model values in this file are Claude-simulated self-reports, not measurements from live OpenAI or Google APIs.

The eleven paper v2.1 section markdowns (`00-abstract.md` through `10-endmatter.md`), ten main figures (PNG + PDF pairs), seven supplementary figures, and five supplementary text sections (S1-S5) were also consumed as byte-identical copies.

## Procedure

### Dashboard generation pipeline

A "fat data, thin client" architecture was adopted: all computation occurred in a Python generator (`generate_dashboard_v2.py`), and the browser was restricted to rendering pre-computed JavaScript constants. The generator pipeline proceeded in three stages. First, the four source JSONs were parsed and flattened into eleven pre-aggregated chart payloads keyed by chart identifier (e.g., `chart-weird-tiers`, `chart-regional-weird`, `chart-nw-detection`, `chart-benchmark-ranks`, `chart-framework-atlas`). Second, a single-source-of-truth fact table (`numbers.json`, 46 keys) was derived from the source data. Third, human-authored interpretation prose (`interpretations.yaml`) was read and its `{{key}}` placeholder syntax was substituted against the fact table; any unresolved placeholder raised a build-time error. The generator emitted three JavaScript constant files (`data.js`, `interpretations.js`, `numbers.js`), each assigning to `window.*` globals rather than top-level `const` declarations to ensure browser accessibility.

### Parallel-agent contract

Before any parallel authoring work began, a written interface contract (`contract.md`, 8,980 bytes) was committed to the `DASHBOARD-V2/` directory. The contract specified: shared CSS class names (prefixed `dash-`), eight canonical tab identifiers, eleven chart identifiers, the XSS discipline (textContent-only, no innerHTML), pinned CDN versions (Inter font, Bootstrap 5.3.3, ECharts 5.5.0), the seven-field interpretation schema with per-field word caps, and the mandatory cross-vendor disclaimer language for Study 3 content. This contract served as the coordination mechanism to prevent class-name and identifier drift across subsequently dispatched parallel authoring agents.

### Adversarial alternate-council review

The initial implementation plan was stress-tested by an alternate council of twelve adversarial critic personas, organized into three parallel Plan-agent dispatches of four critics each. Personas spanned software architecture, release/DevOps, red-team security, reproducibility, UX for first-time visitors, accessibility, cross-cultural decolonial methods, science communication, statistical methodology, fpdf2 PDF production, process management, and scope compliance. Each critic returned structured findings with severity tags (CRITICAL / MAJOR / MINOR) and specific recommended plan edits. Convergent findings (items flagged by three or more independent critics) were treated as must-fix. The top convergent findings were: (1) scope creep in Task 2 MFQ reconciliation; (2) fpdf2 path anchor fragility in the copied v2.2 generator; (3) ambiguity in "working files in subfolder" user requirement; (4) WEIRD-coding in the Framework Synthesis matrix layout. All twelve findings were integrated upstream into Tier-1 role mandates before any Tier-2 execution dispatch.

### Paper v2.2 combined PDF build

The v2.1 PDF generator (`generate_combined_pdf.py`) was copied verbatim to a new subfolder (`PAPER-V2/v2.2/generate_combined_pdf_v2.2.py`) and four modifications were applied: (1) the `BASE` path anchor was redefined as `Path(__file__).resolve().parent` with four explicit sub-anchors (SECTIONS_DIR, FIGURES_DIR, SUPP_DIR, SUPP_FIG_DIR) resolving within the v2.2 bundle; (2) the version and date constants were bumped to `v2.2` and `20260413`; (3) explicit figure lists replaced implicit globs for both main and supplementary figures; (4) a dry-run assertion loop was added that verified every required path, section file, and figure existed before any PDF page was written. The generator was invoked via a single authorized wrapper script (`build_v2.2.sh`) that resolved its own directory to prevent working-directory-dependent failure modes.

### v2.1 immutability enforcement

Prior to any v2.2 operations, all eleven v2.1 section markdown files were copied to an immutable snapshot directory (`PAPER-V2/v2.1-source-snapshot/`). At the end of the session, shasum and byte-level diff were used to verify that the v2.1 PDF (`20260412-cross-cultural-ai-values-alignment-v2.1.pdf`) and v2.1 generator (`generate_combined_pdf.py`) remained unmodified, and that the parent section markdowns were identical to their snapshot counterparts.

### Deployment

The dashboard was deployed to GitHub Pages at a dedicated public repository (`cjimmylin/cei-cultural-global-dashboard-v2`), created by splitting the `gh repo create` and `git push` operations into distinct steps to avoid the backend replication race described in the vault's deployment memory. A pre-deploy git tag (`v2.0.0-pre-deploy`) was created as a rollback anchor. The repository was initialized with a `.nojekyll` marker to bypass Jekyll preprocessing, and a `.gitignore` excluded council deliberations, generator scripts, YAML source, SHA256 lock, and screenshots from the public artifact. After the first push, Pages was enabled via the GitHub REST API (`POST /repos/{owner}/{repo}/pages`) with `source.branch=main` and `source.path=/`. Build status was polled at 15-second intervals until the `built` state was reached, after which the live URL was verified via HTTP 200 checks on all eight deployed assets.

## Analysis

No new inferential statistical analyses were conducted in this session. The methodological discipline distinguished between deterministic re-scans (permitted; used for citation audit re-run) and inferential re-runs (forbidden; classifier scores, council adjudications, and effect-size derivations were treated as frozen). The 0.16–0.18 point MFQ individualizing-to-binding ratio discrepancy flagged by v2.1's `verify_mfq.py` script was documented as a known-issue carryover in `CHANGELOG-v2.2.md` without any attempt at resolution; resolution was explicitly deferred to a future session with its own council.

Numeric parity between the dashboard and paper v2.1 was enforced mechanically rather than by human review. Each interpretation prose field in `interpretations.yaml` referenced numeric values via `{{key}}` placeholders resolved against `numbers.json`. The generator's substitution step raised a build error on any missing or unused key, converting numeric consistency from a review gate (susceptible to reviewer fatigue with forty-six separate values) into a build gate with zero false-negative rate.

## Computational Environment

- Python 3.9 (vault `.venv`, `/Users/jimmy.lin/Documents/CEI-Literature-Vault/.venv/bin/python`)
- `fpdf2` for PDF generation; `/Library/Fonts/Arial Unicode.ttf` for multilingual glyph support
- Frontend: ECharts 5.5.0, Bootstrap 5.3.3 CSS, Inter font family, all loaded via jsdelivr CDN at pinned versions
- GitHub CLI (`gh`) for repository creation and Pages API enablement
- GitHub Pages with legacy (non-Actions) build type, serving from `main` branch root directory

Environmental constraint: per vault memory `feedback_no_non_anthropic_models.md`, no live calls to OpenAI, Google, or other non-Anthropic model APIs were made; all cross-vendor model values in the source comparison JSON are Claude-simulated self-reports, not independently measured behaviors.

## Limitations and Decisions

**Scope containment.** The Task 2 MFQ foundation-means reconciliation was demoted from "attempt to resolve" to documentation-only, on the grounds that re-reading raw comparison data and re-deriving individualizing-to-binding ratios would constitute a statistical analytical act requiring its own review process, and therefore exceeded the scope of a combined-PDF regeneration. This decision was made after convergent alt-council findings from critics C9, C4, and C1.

**Working-files self-containment.** Upon user decision, the v2.2 subfolder was populated with byte-identical copies of all eleven section markdowns, twenty-two main figure files, twenty-one supplementary figures, and five supplementary text sections, rather than reading them via relative paths from the parent `PAPER-V2/` directory. This cost approximately 250 KB of storage duplication but produced a genuinely portable and independently rebuildable bundle.

**Framework Atlas rendering.** The Framework Synthesis tab was explicitly restructured from a matrix comparing five WEIRD ethical frameworks against seven non-Western traditions (which would have re-enacted the flattening that the paper critiques) into a two-panel side-by-side layout: a labeled "WEIRD 5-category" panel on the left and a non-commensurate gallery of six non-WEIRD tradition cards on the right, each rendered in its native concept vocabulary without radar or polar plots. This decision followed the decolonial critic's F7.1 and F7.2 findings.

**Accessibility verification scope.** WCAG 2.2 AA compliance was enforced by CSS design (named contrast ratios, touch-target sizes, reduced-motion support, visually-hidden data table fallbacks for charts) but was not independently verified with axe-core or NVDA/VoiceOver walkthroughs. Live-URL accessibility verification remains a follow-up task.

**Dashboard language scope.** All dashboard copy is English-only. Multilingual rendering with `lang` attributes and right-to-left support for Arabic passages is declared as a v2 limitation in the Methods tab's Known Limits card.

**Figures at legacy DPI.** Six main and supplementary figures (Figures 1-4, S-Figures 1 and 7) remain at their v2.1 legacy DPI because their source generator scripts are unidentified (likely Plotly or manual exports). These are acceptable for specialist venues such as FAccT, JAIR, or Big Data and Society, but would block a Nature-family submission without a figure provenance audit.

**Citation orphans.** Sixty-eight of the one hundred thirty-three references in v2.1 remained un-cited in prose as of v2.2 build time. Five of these are narrative-form false positives for "Norenzayan (2010)" that should be consolidated as "Henrich et al. (2010)" in a future cleanup session; the current session did not perform this rewrite.

**Playwright visual verification.** Post-deploy visual correctness was verified via curl HTTP 200 checks on all eight asset endpoints and by grep-verification that the cross-vendor caveat appeared at five locations in the live HTML. Screenshot-based per-tab visual verification was not conducted in this session.
