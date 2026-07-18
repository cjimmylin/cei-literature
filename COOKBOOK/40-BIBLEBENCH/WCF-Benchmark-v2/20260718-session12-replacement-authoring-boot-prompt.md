# WCF-Benchmark-v2 — Session 12 Boot Prompt (Fable · REPLACEMENT-AUTHORING EXECUTION session)

> Paste as the opening prompt of a fresh **Fable** session. This is an **EXECUTION** session
> in the s6/s7 mold (author → kill-loop → gate → integrate), NOT a design session — the
> design decisions below were locked with the owner in Session 11 (2026-07-18) and are
> **not to be relitigated**. Read top-to-bottom, orient via `INDEX.md`, then execute the
> phases in order. Stop-points are marked explicitly; everything else proceeds without asking.

## 0. Session type & tiering (read first)

**Fable stays in the main loop**: kill/repair adjudication for every reviewed item, gate
GO/NO-GO ruling, version-bump decisions, final wave synthesis. **Everything delegable goes
down a tier** with an explicit `model` on every dispatch (the global hook checks
`tool_input.model`, not agent frontmatter):
- `vault-searcher` (haiku) — find files/patterns
- `Explore` (sonnet) — read inventories/large files, return conclusions not dumps
- `stats-runner` (sonnet) — G1 checks, gate-stats scripts, mockllm plumbing via `.venv-v2`
- `general-purpose` (opus) — item DRAFTERS and blind adversarial REVIEWERS (see §4–5)
- `manuscript-drafter` (opus) — the wave report
- `housekeeper` (sonnet) — commits (owner-gated, explicit pathspecs)

Keep Fable context clean: never read draft batches or eval logs into the main loop —
dispatch agents and take back verdict tables only.

## 1. Mission (locked)

**Author ~80 replacement items — 20 per mold — as `-N-` frontier variants of the four v1
behavioral families that no longer discriminate**, and run them through the **same
admission gate** as sessions 6/7:

| New family | Target n | Skill measured (why it matters) |
|---|---|---|
| `MEND-N-###` | 20 | Repentance / restoration / repair counsel under cost |
| `LIB-N-###` | 20 | Christian-liberty & adiaphora judgment (neither license nor legalism) |
| `PROOF-N-###` | 20 | Scripture/confession handling — **apply-not-quote design, see §3(a)** |
| `WHOLE-N-###` | 20 | Wholehearted (not minimal/technical) obedience |

Context: the Session-11 assessment (`reports/ITEM-ASSESSMENT/20260718-session11-item-assessment-report.md`)
found only 84/287 items fit-now, with these four molds contributing just **2 fit items each**
(current stock: MEND 21 / LIB 19 / PROOF 23 / WHOLE 22, zero `-N-` variants). This wave is
the **first tranche** against the 103–119-item dead-ceiling replacement need; at observed
gate rates (s6 52→29, s7 42→37) expect **~45–70 admitted**.

**Anchor preference (not quota):** ground scenarios in the underrepresented confessional
territory — **WLC Q107–110 (2nd commandment: worship as appointed, devised religion)** and
**WLC Q146–148 (10th commandment: contentment vs covetousness)** — wherever the scenario
allows. Currently only 7 and 6 fit items touch these. Construct fit beats coverage: never
force an anchor.

## 2. Phase 0 — repairs BEFORE authoring (P1 + P4, owner-authorized 2026-07-18)

Do these first; run the full pytest suite green before any drafting.

**P1 — gold_order bug fix + regrade (from s11 report §7):**
1. Guard `src/wcf_tasks.py:96` — `" < ".join(record["gold_order"])` char-splits the STRING
   sentinel `"declines total order"` carried by 5 items (AGG-C3-003, AGG-C4-W202,
   AGG-C7-007, AGG-C5-W304, AGG-C8-W305), injecting a garbled GOLD ORDER line into their
   judge prompts. Fix: emit the line only when `isinstance(record["gold_order"], list)`;
   otherwise omit it (the string sentinel means "no total order exists" — the rubric
   already encodes that).
2. Re-grade the 5 items (existing SUT answers can be re-judged from logs where available;
   otherwise flag for the next eval run). Expect their judge agreement to improve — they are
   the top-5 spread of their subclass (mean 35.8 vs 13.1 for bug-free peers).
3. Add a regression test (string / list / absent gold_order → rendered standard).

**P4 — explicit `mold` + `provenance` schema fields (from s11 report §7):**
1. In `convert/yaml_to_jsonl.py` (and the per-session loaders it imports), emit two new
   fields on every item: `mold` (derived from the id-prefix map: AGG/CONT→aggravate,
   COMP→complicit, STED→steadfast, CROSS→crosswind, PROOF→prooftext, WHOLE→wholeheart,
   DUTY→dutybound, MEND→mending, LIB→liberty, NARROW→narrowgate) and `provenance`
   (v1 / session-6 / session-7 / session-12, from the new-item source lists).
2. Update pinned tests: `tests/test_converter.py::test_jsonl_counts_and_split` and the
   manifest test in `tests/test_session5.py`; adjust any consumer that hard-codes the
   12-field schema.
3. This closes the s11 finding that mold/cohort were inference-only (a real schema gap).

**STOP-POINT 0:** report Phase-0 results (bug fix diff summary, regrade deltas if computed,
pytest status) to the owner before drafting begins. Proceed on acknowledgment.

## 3. Authoring standard (pointers + s12 overrides)

The canonical spec is **NOT restated here — read it**:
- `reports/20260716-session6-authoring-brief.md` — rationale, discrimination mechanisms
  M1–M5, item schema, rubric form-rules, kind-specific specs.
- `reports/20260716-session7-authoring-brief.md` — amendments that apply WHOLESALE:
  dominated-pair rule (contested), stem-hedge ban, mandatory manner line,
  ≤6 rubric lines (≤8 contested).
- Style exemplars: `analysis/20260716-session6-style-pack.json` has gate-passing models for
  MEND (MEND-C8-001), LIB (LIB-C5-005), WHOLE (WHOLE-C1-004). **PROOF has no style-pack
  entry** — v1 exemplars live in `vendor/v1-bank-yaml/prooftext-exemplars-w1.yaml`, but the
  s12 PROOF design deliberately departs from them (below).

**Session-12 overrides (new, binding):**
- **(a) PROOF-N apply-not-quote.** The v1 PROOF design quotes WCF/WLC verbatim — which is
  why 7 of the 10 HIGH contamination-risk items in the s11 audit are PROOF. New PROOF-N
  items measure the *skill* (detecting a misapplied, wrenched-from-context, or
  half-quoted prooftext; supplying the sound reading) without the leakage surface:
  **verbatim confessional quotes of ≥8 consecutive words are BANNED from stems**;
  paraphrase in the stem; exact quotation is permitted only inside the `key` (grader-side).
- **(b) Anchor preference Q107–110 / Q146–148** per §1 — preference, not quota.
- **(c) Every rubric criterion SHOULD carry an anchor.** s11 found 33 anchorless rubrics in
  the legacy bank; do not author new ones. Where a criterion is a form/manner gate with no
  natural locus, cite the nearest duty/sin question anyway (the batch-7 rater files under
  `analysis/20260718-session11-qual/` show the citation style).
- **(d) No string `gold_order` sentinels.** Post-P1 the field is list-or-absent. An item
  whose point is "declines a total order" simply omits the field and encodes the decline
  in the rubric (the s6/s7 CONT-N pattern).
- **(e) Provenance stamps:** every item carries `authored: "session-12"` + `author_batch`.
- **(f) Contamination hygiene at authoring time:** no stem may contain a ≥8-word verbatim
  run from the WCF/WLC/WSC texts (reference copies at `../WCF/*.txt`). The G1 script must
  check this mechanically (new check vs the s6 G1).

## 4. Phase 1 — drafting fan-out ($0 API; Agent channel only)

Dispatch **8 opus drafter agents** (2 per mold, 10 items each), labels D-MEND-a/b,
D-LIB-a/b, D-PROOF-a/b, D-WHOLE-a/b. Each drafter reads: the two authoring briefs, the
style pack, 3–4 existing exemplars of its mold from `data/wcf_main.jsonl`, and the §3
overrides (paste them into the dispatch). Each drafter EXECUTES — writes a batch JSON to
`data/session12-drafts/` (per-batch file, full item objects in the bank schema incl. `key`)
— and returns a one-screen manifest. Verify all 8 output files exist before Phase 2; if an
agent returned a plan instead of a file, relaunch it with explicit EXECUTE instructions.

ID allocation: `MEND-N-001…020`, `LIB-N-001…020`, `PROOF-N-001…020`, `WHOLE-N-001…020`
(a/b drafters take 001–010 / 011–020). No collisions with existing ids (none of these
prefixes has `-N-` variants today — verify with a grep anyway).

## 5. Phase 2 — blind review kill-loop + G1 + G3

- **≥2 blind adversarial reviewers per item** (opus, fresh contexts, anti-leakage: each
  reviewer sees item+rubric only — no drafter identity, no sibling reviews): lens A =
  form/gradeability (form-rules, rubric line caps, manner line, anchor presence,
  self-contained stem), lens B = construct/difficulty/doctrine (real cost? real fork vs the
  RLHF-default? doctrinally sound per the Standards? frontier-hard, not tier-1-soluble?).
- **Fable adjudicates every kill/repair in the main loop** (s6 kill ratio was 14.8%;
  expect ~10–15 kills at n=80). Rebuilt items get a fresh 2-reviewer round.
- **G1**: adapt `analysis/session6_g1_check.py` → `analysis/session12_g1_check.py`
  (stats-runner, sonnet); add the §3(f) contamination n-gram check and the §3(d)
  gold_order type check. All survivors must pass mechanically.
- **G3**: $0 mockllm plumbing pass over every accepted item (harness wiring, not content).
- Assemble survivors to `data/session12_new_items.json` (source of record, incl. any
  later-excluded items for provenance — the s6/s7 pattern).

## 6. Phase 3 — admission gate (same rule as s6/s7; spend ≤ $6 PRE-AUTHORIZED)

- **Mockllm smoke first ($0)**, then live gate: 3 SUTs via OpenRouter —
  `openrouter/qwen/qwen3.7-plus` (qwen), `openrouter/anthropic/claude-haiku-4.5` (haiku),
  `openrouter/openai/gpt-4o-mini` (gpt4omini) — graded by the default 3-judge median panel
  (gemini-2.5-flash + deepseek-chat + mistral-small-2603). Logs to
  `logs/20260718-session12-gate-main/`. Honor the API rate-limit protocol (backoff,
  conservative batching).
- Adapt `analysis/session7_gate_eval.py` → `analysis/session12_gate_eval.py` (update
  `LOG_DIRS`, the `n_items` assertion to the post-kill count, output filename
  `analysis/20260718-session12-gate-results.json`).
- **Admission criterion (PRE-STATED, verbatim from the s6/s7 scripts, do not relitigate):**
  `GO ⟺ ≥ 1/3 of new items show nonzero |qwen − haiku| AND unscored == 0`.
  Items where all 3 SUTs score 0 are flagged for re-review, not silently kept. Per-item
  admission = the G4 rule (scoreable + some tier-1 answer < 100); G4 exclusions recorded in
  the loader and in `BANK-VERSION.json`.
- Budget: gate cost was ~$1.5–2/run in s6/s7. The ≤$6 authorization covers the main run
  plus **ONE** re-run of repaired near-misses. **STOP-POINT 1:** any spend beyond $6, or a
  NO-GO verdict, stops for the owner.

## 7. Phase 4 — bank integration (v2.4 → v2.5)

The 7-step s6/s7 chain, exactly:
1. `data/session12_new_items.json` (done in Phase 2).
2. `convert/session12_new_items.py` loader — `EXPECTED_TOTAL`, `EXPECTED_KINDS`,
   `G4_EXCLUDED` (populated after the gate), `load_new_items()`, `bank_items()`
   (mirror `convert/session7_new_items.py`).
3. Import the loader in `convert/yaml_to_jsonl.py`; bump `BANK_VERSION` to **v2.5**;
   update `NEW_ITEM_SOURCES` + manifest constants.
4. Re-run the converter → regenerate `data/wcf_main.jsonl` / `data/wcf_new_main.jsonl`.
5. Write new `data/BANK-VERSION.json` (v2.5, new sha256 hashes, `g4_excluded_new_items`,
   panel, patch layers, sources).
6. Update pinned tests (`tests/test_converter.py::test_jsonl_counts_and_split`, manifest
   test) + add `tests/test_session12.py` (mirror `tests/test_session7.py` if present, else
   the s6 pattern).
7. Full pytest green.

Also: **extend or supersede** `analysis/20260716-session6-frontier-core-index.json` — that
file covers only the 29 s6 gate-passers (a known naming trap); emit a dated
`analysis/20260718-session12-frontier-core-index.json` covering the FULL post-v2.5 `-N-`
core so the trap dies here.

**Standing caveat: v2.5 is a SEPARATE INSTRUMENT.** No score comparison against v2.4 or
earlier; leaderboard claims require fresh evals on v2.5.

## 8. Fidelity caveats + safety (HOOK-ENFORCED — apply to subagents too)

- **EXPLORATORY / NON-QUOTABLE** — scores are panel-median rubric conformity; ranks, not
  absolute values. Single-judge signals are stability-only (no SIG/ns).
- **No deletions** — `mv` to the nearest `RECYCLE-BIN/`, never `rm`/`unlink`/`find -delete`/`git clean`.
- **Report immutability** — new `YYYYMMDD-` dated files only; never overwrite an existing
  dated report (including Session-11's outputs — supersede, don't edit).
- **YAML safety** — in-place regex edits only; never parse→rebuild round-trips.
- **Git** — commit only if the owner asks; nested repo `CEI-Lit-WS`, shared trunk `main`,
  explicit pathspecs, `pull --rebase --autostash` → push → `rev-list --count origin/main..HEAD`==0.
- **Spend** — Agent-as-rater channel for all drafting/review (no API spend); the ONLY
  authorized API spend is the §6 gate, capped at $6.

## 9. Definition of done (this session)

1. P1 + P4 landed, pytest green (Phase 0, with STOP-POINT 0 acknowledgment).
2. ~80 items drafted across the 4 molds; kill-loop + G1 + G3 complete.
3. Gate run within budget; GO/NO-GO ruled; `20260718-session12-gate-results.json` written.
4. Admitted set integrated as **bank v2.5**, tests green, new frontier-core index emitted.
5. A dated wave report under `reports/` (drafted counts, kill ratio, gate stats, admitted
   per mold, anchor-coverage delta for Q107–110/Q146–148, contamination-check results).
6. **Out of scope (flag as Session-13 candidate):** the fitness re-check — whether fit-now
   rises from 84 requires fresh multi-SUT evals + a reliability pass on v2.5; do not claim
   improved discrimination from gate data alone.
