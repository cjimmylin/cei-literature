WALKWORTHY-CANARY-7f3e2026

# REPORTS/20260717-briefing/figures — Figure README

Generated 2026-07-17 offline from stored analysis artifacts. Zero model calls.
Generation script: `make_figures.py` (same directory). Run from $V2 root with `.venv/bin/python REPORTS/20260717-briefing/figures/make_figures.py`.

---

## fig1-concordance-heatmap.png

Shows raw agreement rates (proportion of items where the referee verdict matches the judge verdict) for five rater pairs — Opus↔A, Opus↔B, Sol↔A, Sol↔B, Sol↔Opus — across four row strata: design-02 control (n=80), design-02 disagreement (n=200), design-07 control (n=150), design-07 disagreement (n=392). Green cells indicate high agreement; red cells indicate low agreement. The disagreement strata drive the headline finding: both referees agree poorly with either judge on design-02 disagreement items (Opus↔A=0.250, Opus↔B=0.255, Sol↔A=0.230, Sol↔B=0.270) but strongly with each other (Sol↔Opus=0.735). Design-07 disagreement shows the same pattern (Sol↔Opus=0.857 vs judge-pair agreement of 0.14–0.60). Control strata are high across the board for d07 (0.86–0.92), confirming referees and judges agree when items are not contested. Title contains "disagreement-enriched sample — per-stratum only" per specification.

Data sources:
- Rater pairs Opus↔A, Opus↔B: `logs/jr-referee-20260716/referee-agreement.json` keys `designs_02_07_per_stratum.[02|07].[control|disagreement].overall.raw_agreement_opus_[A|B]`
- Rater pairs Sol↔A, Sol↔B, Sol↔Opus: `logs/jr-referee-20260716/referee-agreement-sol.json` keys `designs_02_07_sol_vs_ABO_per_stratum.[02|07].[control|disagreement].overall.raw_agreement_sol_[A|B|opus]`

No hand-typed values. All cell values read programmatically from JSON.

---

## fig2-sidewith-bars.png

Stacked horizontal bar chart showing the proportion of disagreement-stratum items where the referee sides with judge-A, sides with judge-B, or sides with neither. Six groups: Opus d02 (n=200), Sol d02 (n=200), Opus d07 (n=392), Opus d07 after defect-exclusion (n=274), Sol d07 (n=392), Sol d07 after defect-exclusion (n=274). The defect-exclusion rows remove the 5 design-07 items where Opus was ever unscorable (WW-07-A02, D03, F02, I04, L02), isolating the cleaner rubric items. The key pattern: on design-07 disagreement items, both referees side strongly with judge-B (~59–76%), not judge-A; exclusion of defect items pushes B-side rates further to 76–84%. On design-02 disagreement items, both referees are roughly balanced between A (~23–25%), B (~25–27%), and neither (~50%), confirming d02 is genuinely three-way ambiguous.

Data sources:
- Opus side-with (J1): `referee-agreement.json` keys `disagreement_side_with.[02|07].overall` and `design07_unscorable_sensitivity.side_with_after`
- Sol side-with (J2): `referee-agreement-sol.json` keys `disagreement_sol_joint.[02|07].sol_side_with.overall` and `design07_sol_sensitivity.sol_side_with_after_primary`

No hand-typed values.

---

## fig3-joint-referee-cells.png

Horizontal bar chart (two panels: d02 n=200, d07 n=392) of the 7 mutually exclusive joint-referee outcome cells: both→A, both→B, Opus→A/Sol→B (disagreement), Opus→B/Sol→A (disagreement), Opus sides/Sol neither, Sol sides/Opus neither, both neither. The cells partition every disagreement-stratum item exactly. On design-02, "both neither" dominates (83/200 = 41.5%), reflecting genuine ambiguity the 4-state taxonomy cannot resolve. On design-07, "both→B" dominates (225/392 = 57.4%), confirming strong consensus that judge-B is correct on the pastoral-care arc construct. "Both→A" (48/392 = 12.2%) and the inter-referee disagreement cells (opus_A_sol_B=9, opus_B_sol_A=4) are small, confirming referee consensus on d07 is not driven by one referee.

Data sources: `referee-agreement-sol.json` keys `disagreement_sol_joint.[02|07].joint_referee_table.cells` and `.n`.

No hand-typed values.

---

## fig4-design06-category-deltas.png

Line plot showing per-category mean deltas (referee score minus judge score) for seven rubric categories (frame, facts, principles, alternatives, resolution, remainder, pastoral) across five comparison pairs (Opus−A, Opus−B from J1; Sol−A, Sol−B, Sol−Opus from J2) separately for the control stratum (n=60) and gap stratum (n=60). The `principles` category is highlighted with a shaded vertical band: in both strata and across all referee-minus-judge pairs involving Opus (Opus−A, Opus−B), `principles` is a strong outlier (control: −0.508/−0.517; gap: −0.283/−0.533), meaning Opus scores `principles` substantially lower than either judge. Sol−Opus in contrast shows `principles` positive (+0.408 control, +0.400 gap), confirming Opus is the outlier — not judge-A or judge-B. This is the F6 "principles = Opus-specific bias" finding.

Data sources:
- J1 (Opus): `referee-agreement.json` keys `design06_per_stratum.[control|gap].per_category_mean_delta_opus_minus_[A|B].[category].mean_delta`
- J2 (Sol): `referee-agreement-sol.json` keys `design06_sol_per_stratum.[control|gap].per_category_mean_delta_sol_minus_[A|B|opus].[category].mean_delta`

No hand-typed values.

---

## fig5-defect-items.png

Grouped bar chart of unscorable counts by item (WW-07-L02, WW-07-I04, WW-07-F02, WW-07-A02, WW-07-D03) for Opus referee (blue, J1) and Sol referee (green, J2). An annotation box reports: Opus total unscorable=50, Sol total unscorable=87, Opus∩Sol overlap=48. The three named defect items (L02, I04, F02) ship "(no keyed text)" rubric anchors and account for nearly all unscorables: Opus L02=19, I04=18, F02=11; Sol L02=35, I04=23, F02=29. WW-07-A02 and WW-07-D03 contribute 1 each for Opus and 0 for Sol (not in J2 audit). Sol produces more unscorables on all three named items than Opus — likely because Sol applies the "unscorable" label more liberally when anchors are absent. The overlap-48 figure means nearly all Opus unscorables are a subset of Sol unscorables.

Data sources:
- Opus counts: `referee-agreement.json` key `opus_unscorable_audit.by_item_id.[item].n` and `n_opus_unscorable_units`
- Sol counts: `referee-agreement-sol.json` key `sol_unscorable_audit.by_item_id.[item].n`, `n_sol_unscorable_units`, and `opus_and_sol_unscorable_overlap`

No hand-typed values.

---

## fig6-pilot-judge-swap.png

Dumbbell chart (2-row x 5-column panel grid, one panel per design) showing per-design headline metric values under judge-A (circle) and judge-B (square) for all 5 SUTs (ds=deepseek, gem=gemini, gpt=gpt-4.1-mini, llama=llama, mist=mistral). Each panel also annotates the judge A/B agreement range across SUTs. Title includes required disclaimer: "no SUT-vs-SUT ordering claims (R4)". The chart is intended to show that ordering is judge-sensitive on every design — connecting lines between A and B dots cross for most SUTs. Design-07 is floor-saturated (all SUTs 0.00 under judge-A; judge-B shows 0.00–0.04). Design-05 shows judge-A dots only (CSR is judge-free; no judge-B csr_mean available).

Data sources:
- Judge-A and judge-B headline values for designs 01–04, 06–10: computed live by `tools/audit/pilot_judge_swap.py --pilot-dir logs/pilot-20260716` on 2026-07-17, reading stored `.eval` logs and `judgeB-verdicts.jsonl`. All values are embedded in `make_figures.py` and flagged as programmatically derived.
- Design-05 judge-A csr_mean: HAND-TRANSCRIBED from `20260716-pilot-report.md` §3 (values from `tools/audit/recompute_design05_csr.py`). These values are: deepseek 0.9028, gemini 0.9226, gpt-4.1-mini 0.8869, llama 0.8436, mistral 0.9444. Flagged in the figure title and in `make_figures.py` source.
- A/B agreement range strings: HAND-TRANSCRIBED from pilot-report §2 table. Flagged in the figure title.

CAVEAT: Design-05 judge-A values and all A/B agreement range strings in fig6 are hand-transcribed from the pilot report (not programmatically extracted from JSON), because csr_mean recovery was done via an offline audit tool whose output is stored in the report markdown, not in a JSON artifact. These are clearly flagged in the figure title ("HAND-TRANSCRIBED") and in the make_figures.py source comments.
