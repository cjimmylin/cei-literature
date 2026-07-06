# FRUITBENCH P1-Build Adversarial Review Protocol (v1)

**Author:** Fable (main loop), 2026-07-06 · **Status:** BINDING for every FRUITBENCH v1/v2 P1 build review from UNFENCED (v2-04) onward
**Derivation:** generalized from the THORNS P1 review (`20260706-thorns-p1-fable-review.md`) — every check below corresponds to a defect class actually found in one Opus build that had already passed its own adversarial self-review. Empirical base rate from that build: 2 latent live-path invalidators, 1 unauthorized gate-loosening, 1 unadjudicated estimand hardcode, 1 systemic item flaw (11/60 items), 1 un-encodable falsification check. Assume every build carries this class of defect until checked.
**Who runs it:** Part A = the builder itself, before handoff (mandatory). Parts B–D = the reviewer — Fable while available; after 2026-07-11, Opus executes B–C mechanically and routes Part D dispositions per the succession protocol (`20260706-succession-protocol.md`).
**Scope isolation:** FRUITBENCH v1+v2 + published literature only; never read sibling BIBLEBENCH packs.

---

## Part A — Builder self-audit (run before writing the handoff; attach results to the pilot report)

For each item, the deliverable is the *evidence*, not a checkmark.

- **A1. Estimand ledger.** For every gate and every reported statistic, quote the brief's defining sentence next to the code that computes it. List every free parameter the brief does NOT pin (aggregation rules, denominators, defaults, tie-breaks). Each is either (a) config-parameterized with the choice flagged for ruling, or (b) already ratified by a D-order you cite. A hardcoded unratified choice is a defect, even if reasonable. *(THORNS: G1 aggregation hardcoded ensemble-mean; verdict flipped under the ratified rule.)*
- **A2. Gate-fidelity diff.** For every gate, state the brief's quantifier ("per item", "every", "each cell") and the code's. Any relaxation (per-item → bank fraction, strict → non-strict inequality, all → most) is unauthorized unless a D-order says otherwise. *(THORNS: D-22 "per item ≥5%" became a 70% bank fraction.)*
- **A3. Live-path trace.** Without credentials, trace the live code path by inspection end-to-end: every call signature compatible across all adapters; every role-conditional prompt (personas, system prompts) actually routed with a fail-loud assertion if absent; determinism/temperature controls stated. Do not write "one config flag from live" unless this trace passes — say instead which defects block live. *(THORNS: live `generate()` crashed on a kwarg; the frozen attacker persona was never injected — a live calibration would have been silently invalid.)*
- **A4. Silent-default grep.** Every construct-bearing lookup (`dict.get(key, default)`, fallback priors, catch-all branches) must fail loud on unknown keys. A default that produces plausible numbers for the wrong design is worse than a crash. *(THORNS: unmatched cells fell to `DEFAULT_PRIOR`.)*
- **A5. Denominator audit.** For every rate: what is in the denominator, and does "no data" ever score as "fail" (or refusals dilute a take-rate)? State each conflation and its direction of bias. *(THORNS: no-hard-item cells auto-failed transfer at 0.0.)*
- **A6. Delete-the-motive test (attractor designs).** For every hard item: if the principal's stated motive/ask is deleted, does the temptation survive structurally? If not, the item telegraphs and measures refusal-of-a-bad-order, not the target construct (D-36 no-narrated-vice-goal). Report the count and concentration — telegraphing clusters in the cells hardest to author. *(THORNS: 11/60, concentrated in the design's own center-of-gravity cells.)*
- **A7. Falsification-to-field map.** For every falsification condition in the brief, name the exact gold/metadata field that operationalizes it. A scoring requirement with no encodable field is unscorable — a defect now, not at paper time. *(THORNS: two-sided F6 CFT declared in bank metadata, only one `cft_id` encodable in gold.)*
- **A8. Provenance labeling.** Every reported number carries its basis (real / synthetic / hand-scored probe) at three layers: in-file banner, filename mode token, and the report's real-vs-synthetic table. No headline rests on synthetic or simulated-rater numbers (FO-5 law). Output filenames must be overwrite-proof (date + mode).
- **A9. Frozen-surface check.** `git log --follow` on the registry and any frozen artifact your session touched; scope-isolation grep (sibling bench names) over everything you created; no deletions anywhere (RECYCLE-BIN only).
- **A10. Fix-pass closure.** For every FIX applied after your internal review: re-audit the *entire class* across the bank/harness, not just the flagged instance — a fix audit that checks only where the finding occurred misses siblings. *(THORNS: the `cft_status` fix audited floor golds and missed the same defect class in hard golds.)*

## Part B — Independent review dispatch (reviewer)

Three parallel agents, disjoint domains, read-only (models: Opus for 1–2, Sonnet for 3; no anti-leakage snippet needed — domains are disjoint):

1. **Harness audit** (Opus): re-derive A1–A5 independently from code; quote line numbers; end with a propagation-readiness list (every change REQUIRED before the spine is copied, each with a one-line justification).
2. **Adversarial item audit** (Opus): deep-read the exemplar and fixed items; run A6/A7 over the full bank (skim-sweep); check every convergence-watch pair against the named neighbor design's brief; hunt one KILL the builder missed; grade findings KILL/MAJOR/MINOR with quotes.
3. **Integrity scan** (Sonnet): A9 mechanically — registry git history, commit file-list vs scope, cross-bench grep, uncommitted files, absolute-path portability.

## Part C — Adjudication questions (the reviewer's own work; do not delegate)

- **C1. Shared-cause test.** Which of the builder's separately-filed findings have one cause? List every flagged symptom, then ask what single diagnosis explains multiple entries — before accepting any as independent. *(THORNS: a panel note, a probe result, and a gate failure were one diagnosis; connecting them redirected the entire rework plan.)*
- **C2. Framing check.** Where the builder proposes a ruling, ask what the builder is anchored on (usually its own implementation) and whether the proposed framing quietly favors ratifying what is already built. Rule on the construct, not the code.
- **C3. Threshold inversion check.** Before raising any gate threshold, ask what a low value is ambiguous between — if one reading is "the instrument is working" (e.g., low frontier take = genuine virtue), raising the bar selects for items that defeat the construct.
- **C4. Consequence design.** Every mandated rework needs a consequence rule (what happens on second failure) and a quota re-proof (does demoting a cell break a floor?). An order without a consequence path regenerates the same review next cycle.

## Part D — Disposition grammar

- Grades: **KILL** (invalidates a headline claim as built) / **MAJOR** (gates expansion or live runs) / **MINOR** (log, fix opportunistically).
- Dispositions: **ratify** (new D-order, numbered continuing the series) / **mandate rework** (with the two-strike demotion rule: one rework, then exploratory stratum) / **demote** (out of headline stats, labeled) / **defer** (only when the deciding evidence does not exist yet — name the evidence) / **latch** (hard-block the dangerous path in code until the fix lands; never rely on a memo alone to stop an invalid run).
- Every ruling that touches a frozen surface is Fable/Jimmy-only; post-window, file to the pending-rulings queue and take the least-committal path (parameterize, report both, gate on the ratified default).
- Outputs: dated decision memo in `FRUITBENCH-REVIEWS/`; edits applied + marked "review ruling YYYY-MM-DD"; a post-edit regression run with expected-values stated; one worklist §1 row; a binding handoff for the next build session. New dated filenames always; never overwrite prior artifacts.
