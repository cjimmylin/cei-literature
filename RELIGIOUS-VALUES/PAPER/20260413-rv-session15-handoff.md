# RV Session 15 Handoff — Dashboard v7 + Paper v3

**Date:** 2026-04-13
**Session scope:** Two parallel deliverables built via meta-critique council pattern (12 planners -> 12 critics -> execute -> 5 correctness gates).

## Summary

Session 15 produced two independent artifacts from a shared data contract:

1. **Dashboard v7** (deployed) — rewrites the public story around the 8-claim canonical set, foregrounds the Claim 8 values-relevance failure (d = -1.23, p < 0.001), and re-frames Tab 6 as a "Simulated Scorer Study" with an opening simulation disclosure. Cold-reader comprehension gate: 5.0 / 5.0 (hard-gate Q3 on simulation awareness MET).
2. **Paper v3** (built) — applies the two residual S14 edits (Opus `values_paired` footnote + NormEval citation tidy) in an immutable `PAPER-V3/` fork. Delta gate confirms only two markdown files differ from v2 and all 18 figure hashes match.

Both deliverables use a single `claims_canonical.json` source to prevent the number-drift issues seen in Sessions 11-13.

## Live URLs

- **Dashboard v7 (latest):** https://cjimmylin.github.io/cei-rv-dashboard/v7/
- **Dashboard v6 (archived):** https://cjimmylin.github.io/cei-rv-dashboard/v6/
- **Repo root (redirects to v7):** https://cjimmylin.github.io/cei-rv-dashboard/
- **Repo:** `cjimmylin/cei-rv-dashboard`, commit `4ed083b` on `main` (single repo, `/v6/` and `/v7/` subdirectories; Critic 4 corrected the original "new-repo-per-version" plan to avoid repo sprawl)

## Sub-handoffs

- Dashboard detail: `PAPER/20260413a-rv-session15-dashboard-v7-handoff.md`
- Paper detail: `PAPER/20260413b-rv-session15-paper-v3-handoff.md`

## Meta-critique council pattern

Unlike Session 13 (12 writing experts, no critic pass), Session 15 followed the `feedback_meta_critique_council_pattern` memory:

1. **Phase A0 Scout** — one-agent data contract build (`data-contract.md`, `claims_canonical.json`, `dom-skeleton.html`).
2. **Phase A1 Plan (8 experts):** narrative, dataviz, statistics, religion, vendor-framing, ux-a11y, transparency, cold-reader.
3. **Phase A2 Critique (3 critics + 1 cold-reader persona = 4):** plain-reader, overclaim, contract-drift, cold-reader.
4. **Phase A3 Synthesis** — 28 numbered resolutions (`synthesis-v7.md`, R-01 through R-28).
5. **Phase B Execute** — generator fork, figure rebuild, HTML emit.
6. **Phase C 5 Gates** — numeric / stale-blocklist / overclaim / non-ascii / cold-reader.
7. **Phase D Deploy** — same-repo `/v7/` subdir, v6 preserved.
8. **Phase E-F** — this handoff and MEMORY updates.

The scope was trimmed from an original "12 plan + 6 critic" plan because Critic 1 (plain-reader) flagged 9 CRITICAL comprehension issues that needed to drive the plan structure directly; the shorter council focused reviewer attention on the most load-bearing concerns.

## Phase C gates (all PASS)

| Gate | Check | Result |
|---|---|---|
| 1 | Numeric correctness (6 canonical patterns) | 6 / 6 found (t = -4.93, p < 0.001, d = -1.23, 6.7%, 93.3, 30/100) |
| 2 | Stale-number blocklist ("4 claims supported", "4/8", etc.) | 0 hits |
| 3 | Overclaim / bare vendor names (200-char qualifier window) | 0 residuals |
| 4 | Non-ASCII / non-Latin-1 characters | 0 |
| 5 | Cold-reader comprehension (5 questions, hard-gate Q3) | 5.0 / 5.0, Q3 MET |

Paper v3 additional gates:

- **Delta gate:** only `03-discussion.md` and `05-supp-methods.md` differ from v2; all 18 figure hashes match exactly.
- **Non-Latin-1 grep:** zero non-ASCII in `PAPER-V3/*.md`.

## Critic findings that shaped the deliverables

- **Critic 1 (plain-reader) — 9C / 15M / 6m:** glossary panel, replace all "A3" with "values relevance score (0-100)", C8 hero card on Overview, reading-path numbered badges (1-6) on tab labels, static all-8-claims index table.
- **Critic 2 (overclaim) — 2C / 9M / 6m:** Tab 6 must open with explicit simulation disclosure; C8 needs CAV-2 (caveat-2) badge on every mention.
- **Critic 3 (contract-drift) — 5C / 8M / 6m:** generator must read `claims_canonical.json` keys (not the human-readable contract keys); C4 null p-value must render as "n.s." with a diamond at y = 1.0 on the -log10(p) strip chart and a pseudo-R^2 tooltip; preserve v6 tab order so returning readers are not disoriented.

## Residuals (non-blocking)

1. **Paper v3 — mean values-relevance clarification.** The cold-reader transcript noted the paper reports two slightly different values-relevance figures: 30 / 100 (top-16 tier, used for the t-test) and 33.6 / 100 (all 50 gate-passers). Both are currently contextualized in the paragraph they appear in, but a parenthetical clarification on first mention would help a plain reader. Synthesis doc R-22 accepted this as non-blocking for v3; address in v3.1 or v4.
2. **Gate 3 accepted edge case.** One sentence in the simulated-scorer-study caveat ribbon names "Gemini" within a 240-char qualifier window (slightly over the 200-char gate window), but the qualifier "Claude-roleplaying" appears in the same sentence. Synthesis R-18 documented this as an accepted over-run because splitting the sentence degraded readability more than the qualifier distance gained.

## Next-session suggestions

- **Paper v3.1** — apply the 30/100 vs 33.6/100 parenthetical clarification. 15-minute edit; no rebuild of figures needed.
- **Cross-vendor re-run (if API access changes)** — per the critical memory `feedback_no_non_anthropic_models`, all cross-vendor numbers in v7 are Claude-roleplaying simulations. If real OpenAI/Google APIs become available, a "real-vendor v8" dashboard could replace the simulated layer; the data-contract pattern would carry over.
- **Tab 6 telemetry** — add a tiny analytics beacon on Tab 6 only to measure whether readers actually read the simulation disclosure before scrolling. (Opt-in.)
- **Data-contract skill** — extract the `claims_canonical.json` scout pattern into a reusable `/rv-data-contract` skill so the next major revision can start from Phase A0 scout in under an hour.

## File index

- Dashboard generator: `scripts/20260413-generate-dashboard-v7.py`
- Dashboard HTML: `dashboard/20260413-religious-values-dashboard-v7.html`
- Dashboard council: `dashboard/review-council-v7/`
- Paper v3 folder: `PAPER-V3/`
- Paper v3 PDF: `PAPER-V3/20260413-religious-values-paper-v3.pdf`
- Paper v3 build script: `PAPER-V3/generate_combined_pdf_v3.py`
- Session handoffs: `PAPER/20260413-rv-session15-handoff.md` (this file), `PAPER/20260413a-...`, `PAPER/20260413b-...`
