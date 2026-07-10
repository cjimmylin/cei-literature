# WCF-Bench — Session Handoff (2026-07-10, session 7 — Opus build: contested scorer + judges + live pilot)

**Date:** 2026-07-10 · **Executor:** Opus (main loop; 1 Sonnet subagent for the README update)
· **Governing doc:** `20260709h-next-session-prompt.md` · **Predecessor:** `20260709g-wcf-session-handoff.md` (session 6, Phase-3 chain + first live mechanical pilot).
**Project root:** `CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/WCF-Benchmark/`

> Build handoff. Session 7 executed the boot prompt's five work items mock-first/TDD, then
> ran the first live OPEN + CONTESTED judge pilot. No relitigation of rulings R1–R23 or the
> contested-scoring ruling; scope stayed locked to WCF-Bench. **187 → 240 pytest green, 0
> network in the suite.** Two atomic commits: `feec515b1` (scorer split + panel) and
> `674a9ad1c` (client robustness + disagreement + live pilot).

---

## 1. What session 7 built (all mock-first, TDD; 187 → 240 pytest)

**Work item 1 — Contested-item scorer split (binding ruling `20260709-contested-item-scoring-ruling.md`):**
- `routing.CONTESTED` — a new **flag-driven** scorer kind (`item.extra['contested'] is True`),
  precedence **EPISODE > CONTESTED > ORDINAL > ANCHOR > OPEN**. An aggravate item that still
  carries a `gold_order` routes to CONTESTED once flagged and is **NEVER τ-scored**. The switch
  is the flag, not `design=="aggravate"` (ruling explicit). (+6 routing tests)
- `contested.py` (NEW, +14 tests) — `score_contested_position()` grades **adherence**:
  disclosure · which legitimate Reformed position + defensibility · coherence-from-the-right-heads,
  plus a **settled_core** (Q152 floor + engagement "no collapse") kept **right/wrong** (the only
  correct/incorrect quantity). `ContestedScore.collapsed()` **raises** — no single gold-match
  scalar (mirrors TriaxialScore). Pure reducers `position_invariance` (flags **sycophantic flip**
  under P4) + `steerability_check` for the multi-response legs. `settled_core_keypoints(item)`
  extracts the floor by Q152-anchor / marker.
- `promptbuilder` — CONTESTED gets the **same** ranking-or-decline ask as ORDINAL: the examinee
  is **blind** to contestedness (a divergent prompt would betray the item). (+3 tests)
- `runner.run(items, clients, *, judge=None, panel=None)` — CONTESTED branch (position scorer via
  panel; `fraction` stays **None → NOT in the accuracy tensor**). New `PerItemResult` fields
  `triaxial` / `contested_score` / `judge_raw` / `contested`. (+8 tests)
- **Bank:** `05-BANK-YAML/aggravate-expansion2.yaml` — `AGG-C3-W302` / `AGG-C5-W304` / `AGG-C8-W305`
  marked `contested: true`; **`positions:` map deferred to G6** (not minted). Verified: exactly
  those 3 route CONTESTED; the other 5 aggravate items stay ORDINAL; bank loads 0 errors.

**Work item 2 — OPEN triaxial judge panel (§4.3, unlocks the 48 OPEN items):**
- `judge_panel.JudgePanel` (NEW, +10 tests) — **calibrate-and-discard** on construction (runs the
  G4 polish-confound battery; drops any judge scoring B≥A); per-item **cross-family assignment with
  the item's generating family excluded**; OPEN → triaxial Matter/Manner/End (never collapsed),
  CONTESTED → the position scorer. **Retains every judge's raw scores** (`OpenVerdict.per_judge` /
  `ContestedVerdict.per_judge`) — the cross-judge disagreement. Per-judge call errors survived.
- Triaxial parse HARDENED (a live-pilot lesson, see §3): `build_judge_prompt` now requests an
  explicit `SCORE: <0.0-1.0>` line; `score_triaxial` extracts it via a trailing-prose-tolerant
  `SCORE:` token (the old `label:number$` parse missed nearly every real judge output). (+2 tests)

**Work item 3 — Client robustness:** `openrouter_client` surfaces `finish_reason`
(`last_finish_reason` / `last_truncated` / `truncated_item_ids`); default `max_tokens` 1024 → 2048.
(+4 tests)

**Work item 4 — Live OPEN/contested pilot + disagreement clusters:**
- `disagreement.py` (NEW, +6 tests) — `summarize_disagreement(RunReport)` → per-cell spread +
  split-defensibility, sorted worst-first (the Fable input).
- `openrouter_pilot_open.py` (NEW, opt-in `--go`) — **RAN GREEN LIVE 2026-07-10.** See §2.

**Work item 5 (stretch) — NOT done:** perturbation-variant materialization + earlier-wave
transcription were not reached this session (deliberately — items 1–4 + the pilot fix filled it).

## 2. The live pilot (2026-07-10, `openrouter_pilot_open.py --go`) — report is the Fable input

Full report: **`20260710-open-contested-pilot-report.md`**; raw: `07-PILOTS/20260710-open-contested/disagreement.json`.
- Judges `gpt-4o-mini` + `gemini-2.5-flash` (cross-family, both non-Anthropic so the opus-authored
  items' generator-exclusion doesn't shrink the panel). SUTs `llama-3.1-8b` + `deepseek-chat`.
  6 items (3 OPEN across designs + the 3 contested) × 2 SUTs. 0 errors, no truncation.
- **G4 calibration: both judges PASSED, 0 discards → calibration GO** (provisional; F-1 caveat).
- **Contested** items position-scored live (never τ). **Disclosure systematically LOW** (mostly
  0.0–0.5): models rarely surface the contestedness (**F-2**). Settled-core held at 1.0 everywhere
  (the anti-relativism guardrail works). **One real defensibility split** — `AGG-C5-W304 · llama`
  (gemini: misapplication of Q151, coh 0.2, defensible=✗; gpt-4o-mini: defensible familial-honor
  reading, coh 0.8). **Top Fable adjudication item.**
- **OPEN** triaxial now parses on nearly every axis (vs all-`None` before the fix).

## 3. Findings surfaced by the live pilot (for the Fable design call)

- **F-1 (judge axis-scale inconsistency):** some judges score triaxial axes **0..2 (rubric points)**
  despite the explicit `0.0–1.0` instruction (gemini M=2.0; gpt-4o-mini 1.5). So a raw OPEN
  cross-judge spread ~1.0 **conflates scale-disagreement with substance-disagreement**. Options for
  the next build: pin the scale harder, switch triaxial to per-keypoint award scoring (compute the
  axis fraction mechanically, like the contested settled-core), or accept 0..1-clamped headlines +
  report per-judge raw. **This is the judge-calibration design decision the Fable session owns.**
- **F-2 (disclosure-low):** confirm whether "models rarely disclose contestedness" is a scale-worthy
  headline before committing measurement design to it.

## 4. Next session = FABLE adjudication (before the window closes ~2026-07-11)

Re-enter via **`20260710-fable-adjudication-boot-prompt.md`**. Fable's uniquely-owned tasks:
1. **Judge-calibration go/no-go** — rule on F-1 (the axis-scale fix path) + confirm G4-GO.
2. **The disagreement clusters** — adjudicate `AGG-C5-W304 · llama` (defensibility split) and the
   OPEN spreads (net of F-1); decide which feed the G6 `positions:` remit vs a judge-quality fix.
3. **F-2** — rule whether the disclosure-low signal is measurement-headline material.

Then a later Opus build session: F-1 scale fix, perturbation-variant materialization (feeds the
position scorer's invariance leg + the flip-rate engine), earlier-wave transcription (~161 → 230,
marking `AGG-C7-007`/R1 `contested: true` and `LIB-C7-008`/`LIB-C3-W202` `dev_set_only`), anchor
grep-verification, then scale toward the gated G1–G7 run.

## 5. Jimmy-blocked (unchanged)

- **G6 confessional panel** — the instrument (`06-G6-PANEL/g6-panel.html`) + aggregation are DONE;
  Jimmy recruits raters. The four contested items' `positions:` map is deferred to G6.
- The gated G1–G7 run stays blocked on G6.

## 6. Sharp edges honored

Report immutability (new dated files only). Shared git index LIVE — both commits used `git log -1`
+ explicit paths, never `git add -A` (WALKWORTHY moved HEAD mid-session). No deletions. Frozen
surfaces (spine, registry, R1–R23, contested-scoring ruling) untouched. Secrets sourced at runtime
(`source ~/.codex/secrets/openrouter.env`), never committed. Canary `WCFBENCH-CANARY-c1647-x9k4q`
not re-minted (appears once in the pilot JSON, carried from the bank).

## 7. Verify

`../.venv/bin/python -m pytest COOKBOOK/40-BIBLEBENCH/WCF-Benchmark/04-HARNESS/tests/ -q` → **240 passed**.
Live pilot: `cd 04-HARNESS && source ~/.codex/secrets/openrouter.env && python openrouter_pilot_open.py --go`.
