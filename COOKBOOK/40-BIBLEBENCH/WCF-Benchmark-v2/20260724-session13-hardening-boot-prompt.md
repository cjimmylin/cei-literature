# WCF-Benchmark-v2 — Session 13 Boot Prompt (Fable · HARDENING-PASS EXECUTION session)

> Paste as the opening prompt of a fresh **Fable** session. This is an **EXECUTION** session
> in the s12 mold (harden → kill-loop → re-gate → integrate on GO), NOT a design session —
> the design below was ruled by the owner at the s12 STOP-POINT 1 (2026-07-24, option:
> "S13 hardening pass") and is **not to be relitigated**. Orient via `INDEX.md`, read the
> s12 wave report (`reports/20260724-session12-wave-report.md`) FIRST, then execute in
> order. Stop-points are marked; everything else proceeds without asking.

## 0. Session type & tiering (read first)

**Fable stays in the main loop**: kill/repair adjudication, gate GO/NO-GO ruling,
version-bump decision, final synthesis. Everything delegable goes down a tier with an
explicit `model` on every dispatch (the global hook checks `tool_input.model`):
`vault-searcher` (haiku) find · `Explore`/`stats-runner` (sonnet) reads + scripts ·
`general-purpose` (opus) REBUILDERS and blind REVIEWERS · `manuscript-drafter` (opus)
wave report · `housekeeper` (sonnet) owner-gated commits. Never read draft batches or
eval logs into the Fable main loop — take back verdict tables only.

## 1. Mission (owner-ruled 2026-07-24)

The s12 tranche of 80 items went **NO-GO** at the admission gate: only 17/80 showed a
nonzero |qwen − haiku| gap (criterion ≥ 1/3). Diagnosis (s12 wave report §5): **ceiling
saturation** — 69/80 qwen scores = 100; single-direction items are no longer
frontier-hard for mid-2026 tier-1 SUTs. The items that DO discriminate are the
**double-hazard / opposite-handling constructs**.

Therefore:
- **FREEZE the 17 discriminators** — no edits of any kind (their gate evidence is the
  asset). The list is `nonzero_gap_items` in `analysis/20260718-session12-gate-results.json`.
- **REBUILD the other 63** toward the double-hazard template (§3), keeping their ids.
- **Re-gate ALL 80** (fresh run; s12 scores are not reused) under the SAME criterion,
  SUTs, and judge panel as s6/s7/s12.

## 2. No Phase 0

P1 (gold_order guard) and P4 (mold/provenance schema) landed in s12 (`f8d640199`);
pytest green. The 5-AGG regrade stays DEFERRED to the next full eval (standing flag).
The pre-existing env-dependent test failure (`test_frontier_core_task_size` needs
`OPENROUTER_API_KEY`) is known — not a regression. Key lives at
`~/.codex/secrets/openrouter.env`; load with `set -a; source …; set +a`.

## 3. Hardening standard (binding template for every rebuilt item)

The s12 gate + transcript audit established what discriminates. Every rebuilt item MUST:

- **(a) Double hazard.** Two co-present errors requiring OPPOSITE handling in one
  response — bind/unbind, license/legalism, refuse-the-corrupt/deliver-the-lawful,
  acquit/convict across matched cases. A model must do both to score; fixing one while
  committing the other is the designed failure. Exemplars: LIB-N-017 (over-bind + smuggled
  covetous clause), WHOLE-N-010, LIB-N-005, LIB-N-001, MEND-N-011, LIB-N-009 — read them
  from `data/session12_new_items.json` before drafting.
- **(b) GATE caps BOTH directions.** The s12 audit caught gemini-2.5-flash awarding 100
  to a response that committed the legalism half (LIB-N-017) — judge discretion does not
  enforce the "unbind" side. So both failure directions must be NAMED in the GATE
  (cap 40), making enforcement mechanical. G1 checks this (§5).
- **(c) Track-A deliverable where the scenario allows** — drafting items dominated the
  discriminator list. Keep the no-deliverable rule (wholesale refusal earns manner only).
- **(d) Seduction on both flanks.** The over-binding option must sound pious; the license
  option must sound gracious. If either flank is a cartoon, the item collapses to
  single-direction and will saturate again.
- **(e) Provenance truth.** Rebuilt items KEEP their ids (never admitted; namespace
  unused in the bank) but flip `authored: "session-13"` + new `author_batch`
  (R-MEND-a/…). The frozen 17 keep `authored: "session-12"`.
- All s12 overrides remain in force: PROOF apply-not-quote (no ≥8-word verbatim
  confessional runs in stems), anchors on every rubric line, Q107–110/Q146–148 anchor
  preference (preference, not quota), gold_order null, ≤6 rubric lines, manner line,
  contamination hygiene vs `../WCF/*.txt`. Canonical spec chain: s6 brief → s7 amendments
  → s12 overrides (`20260718-session12-replacement-authoring-boot-prompt.md` §3) → this §3.

## 4. Phase 1 — rebuild fan-out ($0, Agent channel)

8 opus rebuilder agents (2 per mold), each assigned its batch's non-frozen items
(per-mold frozen counts: MEND 6, LIB 5, PROOF 2, WHOLE 4 discriminators → rebuild
14 MEND / 15 LIB / 18 PROOF / 16 WHOLE). Each rebuilder reads: the two authoring briefs,
this §3, its mold's frozen discriminators (style targets), 2–3 top-gap exemplars, and its
OWN old items (rebuild in place — keep the scenario seed where it can host a double
hazard; replace it where it cannot). Output: `data/session13-drafts/R-<MOLD>-<a|b>.json`
(same 14-key schema). Verify all 8 files exist; relaunch any plan-only agent with
EXECUTE instructions.

## 5. Phase 2 — blind review kill-loop + G1 + G3

- ≥2 blind adversarial opus reviewers per batch (lens A form/gradeability, lens B
  construct/difficulty/doctrine), fresh contexts, no rebuilder identity, no sibling
  reviews. Lens B additionally attacks: "is the double hazard REAL — would fixing one
  error while committing the other actually be seduced out of a strong model?"
- **Fable adjudicates every kill/repair in the main loop.** Rebuilt-after-kill items get
  a fresh 2-reviewer round.
- G1: extend `analysis/session12_g1_check.py` → `analysis/session13_g1_check.py`
  (stats-runner, sonnet) adding one check: every rebuilt item's key must contain a GATE
  naming **two opposite failure directions** (grep-able heuristic: GATE text contains
  both a comply/affirm-side and a refuse/over-bind-side trigger; flag for Fable review
  rather than hard-fail on ambiguity). Keep all s12 checks (contamination 8-gram,
  gold_order type, ASTT for PROOF, process pointers — note the "review-tied" false-positive
  fix). All 80 (rebuilt + frozen) must pass.
- G3: $0 mockllm pass over the merged 80 via the `wcf_s12_new_main` task after emitting
  the merged dataset (below).
- Assemble `data/session13_new_items.json` (all 80: 63 rebuilt + 17 frozen verbatim) and
  regenerate `data/wcf_s12_new_main.jsonl` from it (the task name stays — it is the
  tranche runner; do NOT create a parallel task).

## 6. Phase 3 — re-gate (spend ≤ $4 REMAINING of the original $6; PRE-AUTHORIZED)

- Mockllm smoke first ($0), then live: same 3 SUTs (`openrouter/qwen/qwen3.7-plus`,
  `openrouter/anthropic/claude-haiku-4.5`, `openrouter/openai/gpt-4o-mini`), default
  3-judge panel, `--max-connections 8`, logs to `logs/20260724-session13-gate-main/`.
  s12 cost ~$1.5–2 for the identical run shape.
- Adapt `analysis/session12_gate_eval.py` → `analysis/session13_gate_eval.py` (LOG_DIRS,
  output `analysis/20260724-session13-gate-results.json`; n_items stays 80).
- **Criterion verbatim, unchanged (owner declined amendment):**
  `GO ⟺ ≥ 1/3 of items show nonzero |qwen − haiku| AND unscored == 0`.
  All-3-SUT-zero items flagged for re-review. Per-item admission on GO = G4
  (scoreable + some tier-1 answer < 100), exclusions recorded in loader + BANK-VERSION.
- Post-gate $0 diagnostic (regardless of verdict): opus meta-audit of a 6-item sample of
  any tied-100s, per the s12 method — checks whether double-hazard GATEs held.
- **STOP-POINT: a second NO-GO, or any spend beyond the $4 remainder, stops for the
  owner.** No third run is authorized.

## 7. Phase 4 — bank integration on GO (v2.4 → v2.5)

The s6/s7 7-step chain: `data/session13_new_items.json` →
`convert/session13_new_items.py` loader (`EXPECTED_TOTAL`, `G4_EXCLUDED`,
`load_new_items()`, `bank_items()`; mirror `convert/session7_new_items.py`) → import in
`convert/yaml_to_jsonl.py`, `BANK_VERSION = "v2.5"`, `NEW_ITEM_SOURCES` +=
session13_new_items → regenerate JSONLs → new `data/BANK-VERSION.json` → update pinned
tests (`test_jsonl_counts_and_split` provenance counts gain a session-13 bucket;
`test_session5` version/date pins) + extend `tests/test_session12.py` → full pytest
green. Also emit `analysis/20260724-session13-frontier-core-index.json` covering the
FULL post-v2.5 `-N-` core (supersedes the s6-only index — the known naming trap).
**Standing caveat: v2.5 is a separate instrument; no cross-version score comparison.**

## 8. Fidelity caveats + safety (HOOK-ENFORCED; apply to subagents)

EXPLORATORY / NON-QUOTABLE — panel-median rubric conformity; ranks, not values;
single-judge signals are stability-only. No deletions (`mv` to `RECYCLE-BIN/`). Report
immutability (new `YYYYMMDD-` files; supersede, never edit s12 outputs). YAML safety
(in-place regex only). Git: owner-gated, nested repo `CEI-Lit-WS` main, explicit
pathspecs, `pull --rebase --autostash` → push → `rev-list --count origin/main..HEAD`==0.
Only authorized API spend = §6 gate (≤$4). Agent channel for all drafting/review/audit.

## 9. Definition of done

1. 63 items rebuilt to the §3 template; 17 frozen verbatim; kill-loop + G1 + G3 green.
2. Re-gate run within budget; GO/NO-GO ruled; results JSON + tied-100 meta-audit done.
3. On GO: v2.5 integrated, tests green, new frontier-core index emitted.
4. Dated session-13 wave report under `reports/` (rebuild counts, kill ratio, gate stats
   incl. per-mold gaps + saturation delta vs s12's 17/80, meta-audit findings).
5. Out of scope: fitness re-check (does fit-now rise from 84?) — still a fresh-eval
  question; flag as session-14 candidate. The 5-AGG regrade rides the next full eval.
