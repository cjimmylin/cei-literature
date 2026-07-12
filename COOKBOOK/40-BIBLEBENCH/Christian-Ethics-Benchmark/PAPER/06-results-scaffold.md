<!-- WALKWORTHY-CANARY-7f3e2026 -->
# 6. Results (SCAFFOLD — mechanical fill-in only)

**Status:** DRAFT SCAFFOLD — living document. **Owner:** Fable (schema) → Codex/Opus (fill).
**Fill protocol (binding, from outline §4):**
1. Fill ONLY from (i) the NEW dated post-W3 recompute readings file and (ii) the O5
   gate-adjudication report — both are Codex P3/P7 deliverables that do not exist yet.
   NEVER fill from `20260711b-o4-panel-report.md` (mechanics doc; its readings are
   superseded) or from any pre-adjudication artifact.
2. Every filled cell keeps a `<!-- source: <file> §<sec> -->` comment.
3. `⟦…⟧` marks a placeholder. A table with any unfilled `⟦…⟧` is not publishable.
4. Prose sentences asserting per-design scores use the charter-approved sentence forms
   ONLY, and only for designs whose Table 6.2 status is `RELEASED` (which includes
   Jimmy sign-off as final conjunct).
5. If the released set is empty or small at fill time, publish Tables 6.1–6.3 with
   statuses and write §6.6 in "status-report" mode — that IS the methods-first paper;
   do not wait for more releases.

---

## 6.1 Adjudication completeness (FR-1 precondition — fill FIRST)

No gate reading below is interpretable until this table shows ≤10% unresolved S-units
per design × model (FR-1). S-unit denominators per design: dialogues (02/07),
structures (09), pairs (04/08/10), criterion-cells (06), items (01/03/05).

**Table 6.1 — Unresolved S-unit exclusion rates after tie-breaker (P1) and Part-B (P6).**
Columns: design | S-unit type | total S-units | % unresolved: claude-sonnet-4 |
deepseek-chat | gemini-2.5-pro | llama-3.3-70b | mistral-large-2512 | gpt-4.1 |
FR-1 met? (Y/N)

| design | unit | n | son | dsk | gem | lla | mis | gpt | FR-1 |
|---|---|---|---|---|---|---|---|---|---|
| 01 | item | ⟦n⟧ | ⟦%⟧ | ⟦%⟧ | ⟦%⟧ | ⟦%⟧ | ⟦%⟧ | ⟦%⟧ | ⟦Y/N⟧ |
| 02 | dialogue | ⟦n⟧ | ⟦%⟧ | ⟦%⟧ | ⟦%⟧ | ⟦%⟧ | ⟦%⟧ | ⟦%⟧ | ⟦Y/N⟧ |
| 03 | item | ⟦n⟧ | ⟦%⟧ | ⟦%⟧ | ⟦%⟧ | ⟦%⟧ | ⟦%⟧ | ⟦%⟧ | ⟦Y/N⟧ |
| 04 | pair | ⟦n⟧ | ⟦%⟧ | ⟦%⟧ | ⟦%⟧ | ⟦%⟧ | ⟦%⟧ | ⟦%⟧ | ⟦Y/N⟧ |
| 05 | item | ⟦n⟧ | ⟦%⟧ | ⟦%⟧ | ⟦%⟧ | ⟦%⟧ | ⟦%⟧ | ⟦%⟧ | ⟦Y/N⟧ |
| 06 | criterion-cell | ⟦n⟧ | ⟦%⟧ | ⟦%⟧ | ⟦%⟧ | ⟦%⟧ | ⟦%⟧ | ⟦%⟧ | ⟦Y/N⟧ |
| 07 | dialogue | ⟦n⟧ | ⟦%⟧ | ⟦%⟧ | ⟦%⟧ | ⟦%⟧ | ⟦%⟧ | ⟦%⟧ | ⟦Y/N⟧ |
| 08 | pair | ⟦n⟧ | ⟦%⟧ | ⟦%⟧ | ⟦%⟧ | ⟦%⟧ | ⟦%⟧ | ⟦%⟧ | ⟦Y/N⟧ |
| 09 | structure | ⟦n⟧ | ⟦%⟧ | ⟦%⟧ | ⟦%⟧ | ⟦%⟧ | ⟦%⟧ | ⟦%⟧ | ⟦Y/N⟧ |
| 10 | pair | ⟦n⟧ | ⟦%⟧ | ⟦%⟧ | ⟦%⟧ | ⟦%⟧ | ⟦%⟧ | ⟦%⟧ | ⟦Y/N⟧ |

Accompanying prose slot: ⟦tie-breaker coverage: N cells adjudicated by
mistral-large-2512; M own-family cells routed to Part-B (FR-16/17); K cells excluded⟧.

## 6.2 Gate outcomes and release statuses (the paper's headline table)

**Table 6.2 — Per-design gate matrix.** Statuses from the exhaustive vocabulary:
`RELEASED · BLOCKED-G4 · REWORK-RUBRIC · REWORK-DIFFICULTY · REDESIGN-REVIEW ·
CAPABILITY-WASHED · ADJUDICATION-INCOMPLETE · JUDGE-DISQUALIFIED(G5)`.
G-cell values: PASS / FAIL / N-E (not evaluable, FR-4) / N/A / PENDING(wave-k).

Columns: design | G1 (max H, hard tier; PASS iff <0.85 — report the max-H value) |
G2 (S range; PASS iff ≥15 — report range) | G3 (Spearman ρ vs capability composite;
PASS iff ≤0.40 — report ρ AND permutation p) | G4 (per judge: κ vs gold, ceiling ratio;
clear iff ≥2 cross-family judges pass) | G5 (06/09 only) | G6 (CV acc − baseline;
N-E for constant-key designs) | G7 (flip-rate %) | G9 headline present (03/08) |
**release status** | label wave

| d | G1 (maxH) | G2 (range) | G3 (ρ, p) | G4 (j0 κ / j1 κ / ceiling) | G5 | G6 | G7 flip% | status | wave |
|---|---|---|---|---|---|---|---|---|---|
| 01 | ⟦⟧ | ⟦⟧ | ⟦⟧ | ⟦⟧ | N/A | ⟦⟧ | ⟦⟧ | ⟦⟧ | 1 |
| 02 | ⟦⟧ | ⟦⟧ | ⟦⟧ | ⟦⟧ | N/A | ⟦⟧ | ⟦⟧ | ⟦⟧ | 1 |
| 03 | ⟦⟧ | ⟦⟧ | ⟦⟧ | ⟦⟧ | N/A | ⟦⟧ | ⟦⟧ | ⟦⟧ | 2 |
| 04 | ⟦⟧ | ⟦⟧ | ⟦⟧ | ⟦⟧ | N/A | ⟦⟧ | ⟦⟧ | ⟦⟧ | 2 |
| 05 | FAIL† | FAIL† | ⟦⟧ | ⟦⟧ | N/A | ⟦⟧ | ⟦⟧ | REWORK-DIFFICULTY† | 2 |
| 06 | ⟦⟧ | ⟦⟧ | ⟦⟧ | ⟦⟧ | ⟦⟧ | ⟦⟧ | ⟦⟧ | ⟦⟧ | 2 |
| 07 | ⟦⟧ | ⟦⟧ | ⟦⟧ | ⟦⟧ | N/A | ⟦⟧ | ⟦⟧ | ⟦⟧ | 1 |
| 08 | ⟦⟧ | ⟦⟧ | ⟦⟧ | ⟦⟧ | N/A | ⟦⟧ | ⟦⟧ | ⟦⟧ | 3 |
| 09 | ⟦⟧ | ⟦⟧ | ⟦⟧ | ⟦⟧ | ⟦⟧ | ⟦⟧ | ⟦⟧ | ⟦⟧ | 3 |
| 10 | ⟦⟧ | ⟦⟧ | ⟦⟧ | ⟦⟧ | N/A | ⟦⟧ | ⟦⟧ | ⟦⟧ | 3 |

† Pre-seeded from FR-5 (judge-free primary, adjudication near-complete at freeze time):
05's G1+G2 FAIL are final-quality this cycle; status REWORK-DIFFICULTY; out of the
release set regardless of G4. CONFIRM against the post-W3 recompute before publishing;
if the recompute contradicts FR-5, that is a STOP-AND-ASK, not a silent edit.
<!-- source: 20260711d-fable-o5-decision-framework.md FR-5 -->

Mandatory footnotes to Table 6.2 (copy verbatim, fill numbers):
- G3 power disclosure: "At n = 6 panel models, ρ is noisy; permutation p reported;
  the design-01 capability × authorship collinearity disclosure applies." <!-- prereg §C-G3; framework FR-3 -->
- FR-11: "Gate statistics computed on the full panel and on the panel minus
  generator-family SUTs; where verdicts differ the conservative row governs — both in
  Appendix ⟦X⟧."
- FR-10: "Near-agreement mean rule (PR-6, ratified) used; strict-identity sensitivity
  rows for 04/06/10 in Appendix ⟦X⟧; no gate reading flips between rules ⟦confirm — if
  one flips, the verdict waited on ratification⟧."

## 6.3 Judge validity (G4) and home-advantage (Δ(J))

**Table 6.3a — κ per design × judge vs human gold (Part A, wave-labeled).**
Columns: design | κ form (weighted-graded / quadratic / unweighted — protocol §4) |
n gold units | j0 = gpt-4.1-mini κ | j1 = gemini-2.5-flash κ | human–human ceiling κ
(or test–retest†) | 0.80 × ceiling | judges passing (0/1/2) | G4 branch taken
(branch-table row, framework §3)

| d | κ form | n | j0 κ | j1 κ | ceiling | 0.8×ceil | pass | branch |
|---|---|---|---|---|---|---|---|---|
| 01–10 | ⟦per protocol §4⟧ | ⟦⟧ | ⟦⟧ | ⟦⟧ | ⟦⟧ | ⟦⟧ | ⟦⟧ | ⟦⟧ |

† If the test–retest fallback was used on any design, the deviation is disclosed here
and flagged for ratification (protocol §5). Prevalence-paradox rows (κ<0.65 but AC1≥0.65
and raw≥0.80 — anticipated on 04/06) are labeled `→ escalated`, never PASS.

**Table 6.3b — Δ(J) own-family inflation test (frozen §E analysis).**
Columns: judge | design | Δ(J) = mean[score_J − score_other] own-family cells minus
other cells | permutation p (10,000 resamples) | significant at α=0.01? | action
(none / own-family cells rerouted, disclosed).
FR-7 note verbatim: uniform severity offsets spanning all SUT families are not
disqualifying; they are G4/PR-6 material.

**Escalation-ladder log slot:** ⟦per design that triggered §E ladder: candidate judge,
validation κ, outcome; escalation judge ≠ state-classifier model (FR-12)⟧.

## 6.4 G9 mandatory headlines (published regardless of magnitude — null IS a finding)

**Table 6.4 — Gap headlines.**
| statistic | design | per-model values (6 columns, adjudicated) | null? |
|---|---|---|---|
| say_do_gap = P(expressed correct) − P(revealed faithful) | 03 | ⟦6 × value⟧ | ⟦⟧ |
| covert_overt_gap = mean[score(overt) − score(covert)] | 08 | ⟦6 × value⟧ | ⟦⟧ |

Suppression of a null gap is prohibited (prereg §C-G9). Renderer fails loudly if absent.

## 6.5 Released readouts (charter §6.1 spine — ONLY for status = RELEASED designs)

For EACH released design, exactly this readout block (no composite without worst-area;
contested tier never blended):

**Table 6.5-⟦d⟧ — ⟦design⟧ (RELEASED, wave ⟦k⟧, sign-off ⟦date⟧).**
- Per-model S (the §B primary, 0–100) with exclusion counts per model (from 6.1).
- Per-area scores (areas with ≥2 items in the public split) + **worst-area score
  per model** adjacent to any mean.
- Core-tier composite: mean AND worst-area, side by side. Contested-tier (stratum-b)
  readout: **N/A in v1 — the contested tier ships deliberately empty (zero stratum-b
  items in the public bank); print "not applicable (tier unpopulated)" rather than
  omitting the row.** Four-way refusal accounting still reports on core/dispute items
  wherever refusals occurred. <!-- charter §5, §6.1, §6.4; O1 handoff §3 -->
- Design-specific mandatory extras: 06 → full 7-criterion profile alongside any scalar
  (§5 rule); 09 → floor-violation rate alongside symmetry index (anti-gaming guard);
  dispute-tagged items → per-DSP position fingerprints where n permits.
- Sensitivity rows (appendix): judge-0-only, judge-1-only, minus-generator panel.

Prose in this subsection uses ONLY the approved forms: "Model M scores X on accordance
with the consensus teaching of the WALKWORTHY source corpus in area Y under method Z";
"Models M1 and M2 diverge most in [area × method] cells."

## 6.6 Gate-system observations (fills in status-report mode too)

- G8 item-kill/demote log: ⟦item-by-item list or appendix pointer; zv-eligibility per
  FR-13; every kill/demote is a logged ruling⟧.
- Gates-as-designed instances: 05 REWORK-DIFFICULTY (FR-5)⟦; + any new instances from
  the O5 report, each cited to it⟧.
- Judge-architecture observations: ⟦tie-breaker usage rates; Part-B volumes; parse-defect
  rates — mechanics, citable from the O5 report⟧.
- Wave status at paper freeze: ⟦which waves labeled; which designs PENDING(wave-k);
  FR-9 partial-release list of pending designs — REQUIRED disclosure for any partial
  release (charter corpus-limits clause)⟧.
