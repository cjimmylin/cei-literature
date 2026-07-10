# WCF-Bench — Session Handoff (2026-07-10, session 9 — Opus build tail: R24–R28)

**Date:** 2026-07-10 · **Executor:** Opus (main loop; 7 Sonnet agents for axis-tagging, 1 Opus agent for adversarial review)
· **Governing doc:** `20260710b-opus-build-boot-prompt.md` · **Spec:** `20260710-fable-judge-calibration-adjudication-memo.md` (BINDING, R24–R28)
· **Predecessor:** `20260710-wcf-session-handoff.md` (session 7) + the session-8 Fable memo.
**Project root:** `CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/WCF-Benchmark/`

> Pure execution from the binding memo. No relitigation of R1–R28, the contested-scoring
> ruling, or the OpenRouter path. Mock-first/TDD; scope locked to WCF-Bench. **240 → 285
> pytest green, 0 network in the suite.** The post-fix pilot re-ran live GREEN.

---

## 1. What this session built (memo work-queue items 1–5; TDD, 240 → 285 pytest)

**R24 — F-1 fix: triaxial → per-keypoint AWARD scoring (items 1 of the queue).**
- `loader.RubricKeypoint.axis` field (`matter|manner|end`) + validation (loader rejects any
  other value — the bank lint doubles as the tag review gate). (+3 tests)
- `judge.build_award_prompt` / `parse_award_verdict` / `AwardVerdict` — one award call per
  judge per item; keypoints numbered `KP1..KPn` (rubric order) + axis-grouped; judge emits
  `KP<n>: award|deny` + optional `OFFMAP:`; NO point weights shown (kills the salience defect).
  (+8 tests)
- `triaxial.score_triaxial` **rewritten**: award path when the rubric is axis-tagged (axis
  fraction = Σ awarded pts / Σ **graded** pts; an unparseable KP is excluded from the
  denominator, never denied; an axis with no graded keypoints → `None` surfaced). Untagged
  axes fall back to the **hardened numeric** prompt (pinned levels; a value outside [0,1] is
  kept RAW + flagged `scale_defect`, EXCLUDED at aggregation, never clamped). `TriaxialScore`
  gained `scale_defect / awards / award_axis / offmap / raw_verdicts`. Untagged rubrics use
  the numeric path for all three axes (backward compat — the pre-existing tests still pass).
  (+7 tests)
- `contested._numeric_axis` raw-preservation (returns raw + scale_defect flag + text; clamp
  only at aggregation). `judge_panel._aggregate_triaxial` + `_aggregate_contested` **exclude**
  scale-defected per-judge values (raw survives on `per_judge`). (+2 panel tests, +2 contested)
- **Bank: all 48 transcribed OPEN items axis-tagged** (7 Sonnet agents, one per OPEN design;
  Opus-reviewed via the whole-bank loader lint: 273 keypoints, matter 186 / manner 41 / end 46,
  0 untagged). Genuine axis-bundling keypoints were assigned a dominant axis (agent-flagged);
  no criterion text changed. **Splits deferred** — see §3.

**R28 — leveled disclosure (queue item 3).** `contested.build_disclosure_prompt` +
`_score_disclosure`: frozen 3-level anchor via a **2-binary award form** (KP1 avoided-settled,
KP2 located-the-within-tradition-divide) → 1.0 / 0.5 / 0.0 mechanically. `ContestedScore`
gained `disclosure_awards`. (+5 tests)

**R25 — judge-acceptance probes (queue item 3).** `judge.run_award_consistency_probe` (a
pre-registered award pattern on a fixture, tolerance 1) + `contested.run_disclosure_inversion_probe`
(matched A/B pair; passes iff disclosure(A) > disclosure(B) AND disclosure(B) ≤ 0.3).
`JudgePanel.__init__` now runs **G4 + both probes** at construction and discards on any failure.
(+7 probe tests, +2 panel discard tests)

**R27 — transcript persistence (queue item 2).** `transcripts.py` (NEW): `template_hash()`
(16-hex over the award + numeric + disclosure templates), `build_transcript_records`,
`write_run_transcripts` (JSONL, one per item×SUT cell: SUT prompt + verbatim response + every
judge's full verdict texts + template hash + slugs + timestamp). `runner.PerItemResult` now
captures `prompt_user / response_full`; `judge_panel` per_judge carries `verdict_texts`. (+4 tests)

**Item 5 — perturbation materialization.** `perturbation.materialize_perturbations` +
`materialize_pushback` (P4) / `materialize_monitoring` (P6) / `materialize_persona` (P3) →
`MaterializedPerturbations` (base + declared mechanical variants; P1/P5 surfaced as `needs_llm`,
P2 as `deferred`). `.prompts()` feeds `run_perturbations`; the variants feed `position_invariance`
(P4 sycophantic flip) + `steerability_check` (P3 persona). (+7 tests)

## 2. The post-fix pilot re-run (memo item 4) — GREEN

`openrouter_pilot_open.py --go` ran live (new dated dir `07-PILOTS/20260710-open-contested-postfix/`,
report `20260710-open-contested-postfix-report.md`). Judges `gpt-4o-mini`+`gemini-2.5-flash`
(**both passed G4 + the two new probes, 0 discarded**); SUTs `llama-3.1-8b`+`deepseek-chat`; 6
items × 2; ~10.5k tokens, 0 errors, 0 truncation; 12 transcript cells persisted.
- **F-1 fixed, confirmed live:** every OPEN axis value is a clean mechanical fraction in [0,1]
  (0.556, 0.778, 0.75, …) — the pre-fix off-scale `matter=2.0`/`1.5` are gone.
- **Findings (descriptive, for a later Fable pass — NOT ruled here):** PF-1 top OPEN split now
  crisp = `WHOLE-C9-W301` Matter gpt=1.0 vs gemini=0.0 (both SUTs); PF-2 disclosure has a
  systematic judge offset (gpt reads HIGH ~1.0, gemini LOW 0.0–0.5) even though both pass the
  inversion probe → H-DISC must carry the per-judge gap (R28 condition 5); PF-3 two single-judge
  settled-core dips (`AGG-C3-W302×deepseek` core 0.0; `AGG-C8-W305×llama` core 0.5); PF-4 one
  coherence parse-`None` (surfaced, not 0).

## 3. What remains (ordered; NOT done this session)

1. **Earlier-wave transcription ~161 → 230 (memo queue item 6) — DEFERRED.** The 69 expansion-2
   items are transcribed + axis-tagged; the **~161 earlier-wave items** (exemplars wave-1/wave-2
   in `01-DESIGNS/exemplars*/`, expansion-1 in `01-DESIGNS/expansions/*expansion-2.md`? no —
   expansion-1 files + `02-EXPANSION`/wave dirs) are NOT yet in `05-BANK-YAML`. This is a large,
   independent data task (10-agent-scale, like session 5's 69-item transcription) and was
   deliberately deferred rather than rushed at session end (anchor grep-verification is
   fabrication-sensitive — CLAUDE.md data-integrity). **At transcription:** axis-tag the OPEN
   rubrics (same protocol as §1), mark `AGG-C7-007` `contested: true` (the 4th aggravation
   contested item / R1), and `LIB-C7-008` + `LIB-C3-W202` `dev_set_only: true`. Grep-verify
   every anchor (OCR wraps clauses + injects proof-letters — grep short fragments).
2. **Axis-tag SPLITS.** The 4 tagging agents flagged genuinely-bundled keypoints (e.g. MEND
   "anti-merit + manner (no groveling)"); each got a dominant-axis tag, no split. If a later
   pass wants true splits (memo R24 bullet 1 allows splitting a spanning keypoint, preserving
   total points), the flagged ones are in the agent summaries. Low priority — dominant-axis
   tagging is faithful and the award scorer works on it.
3. **Coherence → award form (PF-4).** Contested coherence is still a numeric prompt; a later
   pass could move it to award keypoints too (disclosure already is).
4. **Gated G1–G7 run (memo queue item 7) — G6-BLOCKED (Jimmy).** Unchanged.

## 4. Jimmy-blocked (unchanged + the memo's additions)

- **G6 confessional panel** — instrument (`06-G6-PANEL/g6-panel.html`) + aggregation done; Jimmy
  recruits raters. G6 now also gates: H-DISC promotion (compute only over G6-confirmed contested
  items), the W304/W305 position-map confirmation (ratified as *proposed* maps in R26), and the 4
  LIB `[DISPUTED]` legs.
- The gated G1–G7 run stays blocked on G6.

## 5. Re-entry

- Next Opus build session: execute §3.1 (earlier-wave transcription + the 3 flags + axis-tags),
  then §3.3. Read order: this handoff → the Fable memo R24–R28 → `05-BANK-YAML/TRANSCRIPTION-SPEC.md`.
- Best Fable use (if a window opens): adjudicate the **post-fix** disagreement clusters —
  PF-1 (`WHOLE-C9-W301` Matter split, now keypoint-adjudicable via the persisted transcripts)
  and PF-2 (the disclosure judge offset → third-judge / G6 dependency for H-DISC).

## 6. Sharp edges honored

Report immutability (new dated files; the pre-fix pilot dir untouched). Shared git index LIVE
(HEAD moved under WALKWORTHY mid-session; explicit-path staging, `git log -1` before commit,
never `git add -A`; the pre-existing `06-G6-PANEL/screenshots/g6-aggregate-jl.png` is Jimmy's, NOT
staged). Secrets sourced at runtime (`~/.codex/secrets/openrouter.env`), never committed. Canary
`WCFBENCH-CANARY-c1647-x9k4q` not re-minted. No frozen surface edited (R1–R28, spine, registry,
contested-scoring + OpenRouter rulings all stand). No deletions.

## 7. Verify

`../.venv/bin/python -m pytest COOKBOOK/40-BIBLEBENCH/WCF-Benchmark/04-HARNESS/tests/ -q` → **285 passed**.
Post-fix pilot: `cd 04-HARNESS && source ~/.codex/secrets/openrouter.env && python openrouter_pilot_open.py --go`.
