<!-- WCFBENCH-CANARY-c1647-x9k4q -->
# 6. Results

> ⚠️ **SCAFFOLD — contains no data; populated only from the T4 gate report.**
> Every cell below is a `{{PREREG:...}}` placeholder or a blank slot. No numbers are
> written here by hand and no conclusions are drawn. The gate report (produced by the
> executor as "GATE-COMPUTATION REPORT — adjudication pending") drops into these
> placeholders mechanically; PASS/FAIL adjudication is a separate human step, and the
> release rules of §5.8 govern what may be quoted. All field names below are taken
> verbatim from the pre-registration's gate computations (§5.7 / R60–R66) so that the
> substitution is purely mechanical.

## 6.1 Gate report table

Each gate row carries its frozen threshold, its computed field(s), and a PASS/FAIL slot
that is filled only by adjudication (not by the executor).

| Gate | Frozen threshold | Computed value(s) | PASS / FAIL |
|---|---|---|---|
| G1 — Capability correlation | r² < 0.40 | r² = `{{PREREG:G1.r_squared}}`; r = `{{PREREG:G1.pearson_r}}`; ρ = `{{PREREG:G1.spearman_rho}}`; n = `{{PREREG:G1.n}}`; bootstrap CI = `{{PREREG:G1.bootstrap_ci}}` | `{{PREREG:G1.verdict}}` |
| G2 — Headroom | best frontier-set mean ≤ 0.70 | best frontier mean = `{{PREREG:G2.best_frontier_mean}}`; frontier vector = `{{PREREG:G2.frontier_vector}}` | `{{PREREG:G2.verdict}}` |
| G3 — Separation | ≥ 9 of 10 pairs p < 0.01 | pairs significant = `{{PREREG:G3.pairs_significant}}` / 10 | `{{PREREG:G3.verdict}}` |
| G4 — Judge validity | κ ≥ 0.60 AND κ ≥ 0.75 × human ceiling | per surface (see §6.5) | per surface (see §6.5) |
| G5 — Shortcut | G5a ≤ 0.10; G5b ≤ 0.20; G5c below | G5a = `{{PREREG:G5.g5a_max_gap}}`; G5b = `{{PREREG:G5.g5b_open_fraction}}`; G5c Δ = `{{PREREG:G5.g5c_delta}}`, mean_B = `{{PREREG:G5.g5c_mean_b}}` | `{{PREREG:G5.verdict}}` |
| G6 — Human consensus | ≥ 85% per item; 100% coverage for quoted golds | coverage % = `{{PREREG:G6.coverage_pct}}`; confirmed golds = `{{PREREG:G6.confirmed_count}}` | `{{PREREG:G6.verdict}}` |
| G7 — Reliability | α > 0.99 → REDUNDANCY flag (no veto) | per design (see §6.6) | flag only (see §6.6) |

Scope-disclosure line (filled if EPISODE items are excluded or the roster is < 10):
`{{PREREG:G1.scope_disclosure}}` — applies to every gate row whose scope was shrunk.

## 6.2 League table — per-SUT composite

Composite score by SUT over gold-scored base cells in scope. The worst-cell scalar is the
only sanctioned scalar (§5.8).

| SUT (slug) | Composite | Worst-cell scalar |
|---|---|---|
| `{{PREREG:league.per_sut_slug}}` | `{{PREREG:league.per_sut_composite}}` | `{{PREREG:league.per_sut_worst_cell}}` |

> **Validity footnotes (part of this template):**
> † OPEN-track columns are a **single-judge-family label** — the OPEN surface is scored by
> one judge family (google) only; see §5.3 and §5.7 (G4). Not quotable unless G4 passes on
> open_award.
> ‡ PROOF columns use **mechanical citation scoring with a known-artifact disclosure**; see
> §5.1 and §5.7 (PROOF).

## 6.3 League table — per-design breakdown

Per-design mean score for each SUT (frontier-set columns marked); headline cells require G6
coverage per §5.8.

| Design | SUT | Mean score | Track | Coverage % |
|---|---|---|---|---|
| `{{PREREG:league.per_design_id}}` | `{{PREREG:league.per_design_sut}}` | `{{PREREG:league.per_design_mean}}` | `{{PREREG:league.per_design_track}}` | `{{PREREG:G6.per_design_coverage_pct}}` |

Headline matrix (per-commandment × per-tier × per-track), quotable only under §5.8:
`{{PREREG:league.headline_matrix}}`.

> **Validity footnotes (part of this template):**
> † single-judge-family label on every OPEN-scored cell (§5.7 G4).
> ‡ PROOF cells carry the mechanical-citation known-artifact disclosure (§5.1).
> § cells with coverage < 100% carry the `author-gold (G6-pending)` mark and are excluded
> from any quoted headline aggregate.

## 6.4 Perturbation flip-rate table

Base cells feed no gate here; this is a reported metric only. Flip rates are computed on
the frontier-set SUTs (5) for axes P3, P4, P6.

| SUT (frontier) | P3 flip rate | P4 flip rate | P6 flip rate |
|---|---|---|---|
| `{{PREREG:league.per_sut_slug}}` | `{{PREREG:P3.flip_rate}}` | `{{PREREG:P4.flip_rate}}` | `{{PREREG:P6.flip_rate}}` |

Variant-eligible item counts (from the bank, not results): P3 = 143, P4 = 132, P6 = 25.
A variant that changes a Westminster-relevant fact is a new item, not a flip (§5.4).

## 6.5 Judge-agreement table (G4)

One row per judge × surface. κ form is fixed by surface type (§5.7 G4). Human labels are
drawn after the panel runs; this table is populated at release, not at run time.

| Surface | Judge | κ (judge–human) | Human ceiling | 0.75 × ceiling | κ form | Verdict |
|---|---|---|---|---|---|---|
| open_award | gemini-flash | `{{PREREG:G4.open_award.kappa}}` | `{{PREREG:G4.open_award.human_ceiling}}` | `{{PREREG:G4.open_award.ceiling_threshold}}` | unweighted / weighted | `{{PREREG:G4.open_award.verdict}}` |
| disclosure | gemini-flash | `{{PREREG:G4.disclosure.gemini.kappa}}` | `{{PREREG:G4.disclosure.human_ceiling}}` | `{{PREREG:G4.disclosure.ceiling_threshold}}` | unweighted | `{{PREREG:G4.disclosure.gemini.verdict}}` |
| disclosure | grok | `{{PREREG:G4.disclosure.grok.kappa}}` | `{{PREREG:G4.disclosure.human_ceiling}}` | `{{PREREG:G4.disclosure.ceiling_threshold}}` | unweighted | `{{PREREG:G4.disclosure.grok.verdict}}` |
| settled_core | gemini-flash | `{{PREREG:G4.settled_core.gemini.kappa}}` | `{{PREREG:G4.settled_core.human_ceiling}}` | `{{PREREG:G4.settled_core.ceiling_threshold}}` | unweighted | `{{PREREG:G4.settled_core.gemini.verdict}}` |
| settled_core | grok | `{{PREREG:G4.settled_core.grok.kappa}}` | `{{PREREG:G4.settled_core.human_ceiling}}` | `{{PREREG:G4.settled_core.ceiling_threshold}}` | unweighted | `{{PREREG:G4.settled_core.grok.verdict}}` |
| coherence | gemini-flash | `{{PREREG:G4.coherence.gemini.kappa}}` | `{{PREREG:G4.coherence.human_ceiling}}` | `{{PREREG:G4.coherence.ceiling_threshold}}` | weighted | `{{PREREG:G4.coherence.gemini.verdict}}` |
| coherence | grok | `{{PREREG:G4.coherence.grok.kappa}}` | `{{PREREG:G4.coherence.human_ceiling}}` | `{{PREREG:G4.coherence.ceiling_threshold}}` | weighted | `{{PREREG:G4.coherence.grok.verdict}}` |
| EPISODE | gemini-flash | `{{PREREG:G4.episode.gemini.kappa}}` | `{{PREREG:G4.episode.human_ceiling}}` | `{{PREREG:G4.episode.ceiling_threshold}}` | weighted | `{{PREREG:G4.episode.gemini.verdict}}` |
| EPISODE | grok | `{{PREREG:G4.episode.grok.kappa}}` | `{{PREREG:G4.episode.human_ceiling}}` | `{{PREREG:G4.episode.ceiling_threshold}}` | weighted | `{{PREREG:G4.episode.grok.verdict}}` |

Supplementary (fraction-valued surfaces): ICC(2,1) = `{{PREREG:G4.icc_2_1}}`.

## 6.6 Reliability table (G7)

One row per design; α > 0.99 raises a REDUNDANCY flag and no release veto.

| Design | α | 95% bootstrap CI | Mean inter-item r | REDUNDANCY flag |
|---|---|---|---|---|
| `{{PREREG:G7.design_id}}` | `{{PREREG:G7.alpha}}` | `{{PREREG:G7.alpha_ci}}` | `{{PREREG:G7.mean_inter_item_r}}` | `{{PREREG:G7.redundancy_flag}}` |

## 6.7 Cost and compliance table

Records the run against the not-to-exceed cap and truncation ladder (§5.5).

| Item | Value |
|---|---|
| Total spend ($) | `{{PREREG:cost.total_spend}}` |
| Not-to-exceed cap ($) | `{{PREREG:cost.nte_cap}}` |
| Approved budget ($) | `{{PREREG:cost.approved_budget}}` |
| Pre-flight cost estimate ($) | `{{PREREG:cost.preflight_estimate}}` |
| Truncation-ladder events | `{{PREREG:cost.truncation_events}}` |
| Roster size at run (target 10; n ≥ 8) | `{{PREREG:cost.roster_size}}` |
| Voided / out-of-range cells | `{{PREREG:cost.voided_cells}}` |
| Transport failures after retry | `{{PREREG:cost.fail_transport_after_retry}}` |
