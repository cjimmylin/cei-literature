# RV Session 15 — Dashboard v7 Build Handoff

**Date:** 2026-04-13
**Deliverable:** `dashboard/20260413-religious-values-dashboard-v7.html` (164,617 bytes)
**Generator:** `scripts/20260413-generate-dashboard-v7.py` (forked from v4; 153 KB)
**Deployed:** https://cjimmylin.github.io/cei-rv-dashboard/v7/ (commit `4ed083b`)

## Why v7

v6 (Session 12) reports 8 claims but foregrounds the 4 supported ones; v6 Tab 6 reads as a cross-vendor study without making the simulated nature of the non-Claude scorers obvious to a plain reader. Session 15 rebuilds the public story around Claim 8 (values-relevance failure, t = -4.93, p < 0.001, d = -1.23) and explicitly re-frames Tab 6 as a Simulated Scorer Study.

## Council roster (12 members)

The scope was trimmed from the original 12-planner + 6-critic plan. Critic 1 (plain-reader) flagged 9 CRITICAL comprehension issues in the A1 plans, which required re-allocating reviewer headcount toward cold-reading rather than another critic tier.

**Phase A1 Plan (8 experts, by discipline perspective):**

1. Narrative perspective — story arc, hero stat, reading path
2. Dataviz perspective — chart selection and chart-to-claim mapping
3. Statistics perspective — test descriptions, effect sizes, p-value handling
4. Religion perspective — tradition labeling, Islam = 9/15 caveat
5. Vendor-framing perspective — simulated scorer language, CAV-2 badge placement
6. UX/a11y perspective — skip link, WCAG AA, theme toggle
7. Transparency perspective — caveat ribbon, footnotes, method pointers
8. Cold-reader perspective — hypothetical naive reader

**Phase A2 Critique (3 critics + 1 cold-reader persona = 4):**

9. Plain-reader critic — scored plans against hypothetical plain reader
10. Overclaim critic — scanned for unqualified vendor names
11. Contract-drift critic — verified plans match `claims_canonical.json` keys
12. Cold-reader transcript persona — ran a 5-question plain-reader test at Phase C gate 5

## Phase A0 — Data contract scout

Three deliverables (authored by a single scout agent, reviewed in Phase A2 by Critic 3):

1. **`dashboard/review-council-v7/data-contract.md`** — Human-readable contract: 8 claims, verdict colors, chart list, caveat wording, typology cards.
2. **`dashboard/review-council-v7/claims_canonical.json`** — Machine-readable source of truth: 8 claim objects with `id`, `short`, `test`, `statistic`, `p`, `effect`, `verdict`, `caveats[]`; T2 span object; rubric ceiling 9x4 heatmap; 3 caveats array; vendor typology (3 cards). C1 and C8 use a nested-schema adapter because their test rows originally lived inside sub-objects in the S14 results JSON; Critic 3's drift audit caught this and added the adapter function in the generator.
3. **`dashboard/review-council-v7/dom-skeleton.html`** — Static DOM mockup so dataviz and UX planners could plan against the same layout.

## Phase A1 — 8 plan files

Located in `dashboard/review-council-v7/`:

- `plan-narrative.md`
- `plan-dataviz.md`
- `plan-statistics.md`
- `plan-religion.md`
- `plan-vendor-framing.md`
- `plan-ux-a11y.md`
- `plan-transparency.md`
- `plan-cold-reader.md`

## Phase A2 — 3 critique files

Located in `dashboard/review-council-v7/`:

| File | Severity counts |
|---|---|
| `critique-plain-reader.md` | 9 CRITICAL / 15 MAJOR / 6 minor |
| `critique-overclaim.md` | 2 CRITICAL / 9 MAJOR / 6 minor |
| `critique-contract-drift.md` | 5 CRITICAL / 8 MAJOR / 6 minor |

Key critical findings:

- **Plain-reader 9C:** add glossary panel (K/R/V, T1/T2, CI, pp, WEIRD, values relevance score); replace every "A3" with "values relevance score (0-100)"; add C8 hero stat card on Overview; add reading-path numbered badges 1-6 on tab labels; add Tab 5 static all-8-claims index table with verdict badges, C8 row first.
- **Overclaim 2C:** Tab 6 opening line must be "Simulated Scorer Study. All non-Claude scorers in this tab are Claude models roleplaying the persona and output style of other vendors; no real external API calls were made." C8 must carry a CAV-2 badge wherever it is cited.
- **Contract-drift 5C:** generator must read `claims_canonical.json` keys (not the contract doc's prose keys); C4 null p-value must render as "n.s." with a diamond at y = 1.0 on the -log10(p) strip chart and a pseudo-R^2 tooltip; keep v6 tab order (Overview, Claims, Constructs, Methods, Reader Guide, Simulated Scorer Study) so returning readers are not disoriented.

## Phase A3 — Synthesis

`dashboard/review-council-v7/synthesis-v7.md` contains 28 numbered resolutions **R-01 through R-28**. Each resolution is a one-line action plus the critic(s) that raised it plus the plan file(s) it patches.

## Phase B — Execution

Generator forked from v4 (not v6) because v6 had accumulated one-off patches that made the v7 diff hard to read. Fork steps:

1. Copy `scripts/20260405-generate-dashboard-v4.py` to `scripts/20260413-generate-dashboard-v7.py`.
2. Load `claims_canonical.json` as the single source of truth; wire all chart builders to read from it.
3. Add the C1/C8 nested-schema adapter.
4. Add R-01 through R-28 in order.
5. Rebuild all figures.
6. Emit HTML (164,617 bytes) to `dashboard/20260413-religious-values-dashboard-v7.html`.

Items added to v6:

1. C8 hero stat card in Overview tab (values relevance failure, d = -1.23, p < 0.001).
2. Hero subtitle: "A study of whether religious-values benchmarks actually measure what they claim."
3. Expanded-by-default caveat ribbon with 3 caveats (T2 blinding, scorer bias, Gemini provenance).
4. Reading-path numbered badges (1-6) on tab labels.
5. Tab 6 renamed "Simulated Scorer Study" with simulation disclosure in opening line.
6. Tab 5 glossary panel.
7. Tab 5 static all-8-claims index table with verdict badges (C8 row first).
8. New C8 forest plot with CAV-2 badge.
9. New -log10(p) strip chart for all 8 claims; C4 diamond at y = 1.0 with pseudo-R^2 tooltip; p = 0.05 reference line.
10. 3-card vendor typology on Tab 6.
11. T2 span horizontal bar chart (simulated; opacity 0.5 to signal the simulation layer).
12. Rubric ceiling 9x4 heatmap with "(sim)" suffix.
13. Every former "A3" reference replaced with "values relevance score (0-100)" (R-05).
14. Verdict colors: green supported, amber revised, blue not_significant (Okabe-Ito palette).
15. Skip-to-content link for a11y.
16. Theme toggle with version-counter pattern.

## Phase C — Correctness gates (all PASS)

| Gate | Check | Result |
|---|---|---|
| 1 | Numeric correctness | 6 / 6 canonical patterns found: `t=-4.93`, `p<0.001`, `d=-1.23`, `6.7%`, `93.3`, `30/100` |
| 2 | Stale-number blocklist | 0 hits on phrases "4 claims supported", "4/8", "five supported" |
| 3 | Overclaim / bare vendor names (200-char window) | 0 residuals (one accepted edge case at 240 chars; see session handoff) |
| 4 | Non-ASCII / non-Latin-1 | 0 |
| 5 | Cold-reader comprehension | 5.0 / 5.0; hard-gate Q3 (simulation awareness) MET |

`dashboard/review-council-v7/cold-reader-transcript.md` contains the full Q&A.

## Phase D — Deploy

- **Repo:** `cjimmylin/cei-rv-dashboard` (single repo, unchanged; the original plan proposed a new `cei-rv-dashboard-v7` repo, but Critic 4 on the contract-drift panel argued against repo sprawl because each new repo triples the GH Pages setup cost and fragments the archive story).
- **Layout:** `/v6/` subdirectory preserved verbatim; new `/v7/` subdirectory added; root `index.html` issues a `<meta http-equiv="refresh">` to `/v7/`.
- **Commit:** `4ed083b` on `main` (single commit containing the generator, the HTML, the figures, the council docs, and the root redirect).
- **Verification:** curl of the three URLs returned 200 after Pages build completed.

## Known caveats (user-facing)

These are the 3 caveats rendered in the expanded ribbon at the top of every tab:

1. **T2 blinding cannot be verified post-hoc.** The T2 admin transcripts include the scoring rubric, which may leak evaluative framing to the scorer; we present T2 results with an explicit caveat rather than blinding.
2. **Scorer bias.** The scorer is itself a Claude model; we cannot rule out in-vendor bias in the benchmark scoring step. Tab 6 exists specifically to explore this.
3. **Gemini provenance.** The "Gemini" column in Tab 6 is a Claude model roleplaying the Gemini output style; no real Google API was called (see `feedback_no_non_anthropic_models`).

## Files

- Generator: `scripts/20260413-generate-dashboard-v7.py`
- HTML output: `dashboard/20260413-religious-values-dashboard-v7.html`
- Council docs: `dashboard/review-council-v7/` (data-contract.md, claims_canonical.json, dom-skeleton.html, 8 plan files, 3 critique files, synthesis-v7.md, cold-reader-transcript.md)
- Live: https://cjimmylin.github.io/cei-rv-dashboard/v7/
- Archive: https://cjimmylin.github.io/cei-rv-dashboard/v6/
