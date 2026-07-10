# WCF-Bench — Session Handoff (2026-07-10, session 12 — Opus build: R35 gating + R36 third family + R37 floor re-run)

**Date:** 2026-07-10 · **Executor:** Opus (main loop; live runs from the main loop per R37.4,
no subagents) · **Governing doc:** binding Fable memo `20260710h-fable-probe-stability-adjudication-memo.md`
(R34–R37) · **Boot:** `20260710i-opus-build-boot-prompt.md` · **Predecessor:** session-11
handoff `20260710g-wcf-session-handoff.md`.
**Project root:** `CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/WCF-Benchmark/`

> Mock-first/TDD execution of R35 (326 → **366 pytest green**, 0 network) + two live OpenRouter
> runs (R36 screen, R37 floor re-run, ~cents each). **Headline: a valid SECOND disclosure family
> (x-ai/grok-4.20) is found — disclosure now has ≥2 families (R30 condition 6 met on the judge
> side). The floor re-run surfaced a Fable-trigger divergence (§4).** 4 commits pushed
> (`c9aec717e` → `b3c010aab`; a WALKWORTHY sibling commit landed between — shared index).

---

## 1. R35 gating build — COMPLETE (mock-first/TDD, 326 → 366 green)

**Commit `c9aec717e` — R35.1/.3 (retry parity + cause taxonomy):**
- **R35.1** `complete_with_retry` widened: retries once on `finish_reason ∈ {length, error}` OR an
  empty/silent emission; a **non-empty refusal stays terminal** (never retried, never a transport
  loss). This closes the session-12 gap where gemini's `error` finish_reasons were silently counted
  as qualification fails (the willingness gate short-circuited the retry). All five acceptance probes
  now route through the seam — the three `judge.py` probes were calling `judge.complete()` directly;
  the two disclosure probes already went through `_score_disclosure` (reordered so a discarded
  transport call is classified before the willingness/decline check).
- **R35.3** rep-level cause taxonomy `pass | fail_substantive | fail_format |
  fail_transport_after_retry` on `ProbeResult.cause` + `JudgeCalibrationResult.cause`.

**Commit `592454bd2` — R35.2/.4 (K=8 majority gate + manifest + panel consumption):**
- New `wcfbench/qualification.py`: `qualify_judge` runs each probe K=8 times (all calls through the
  retry seam); a surface is eligible iff **every probe gating it reaches ≥5/8** passing reps. A raised
  transport error is a counted fail (never dropped from the denominator). Surface→probe map mirrors
  R33.4 (OPEN_AWARD = g4∧award-consistency∧discrimination; DISCLOSURE = disclosure-inversion∧
  negative-disclosure; COHERENCE/SETTLED_CORE = g4).
- Qualification **manifest** (R35.4): `build_manifest`/`write_manifest`/`load_manifest` freeze slugs +
  template hashes + per-probe pass table + eligible-surface sets. `current_template_hashes()` hashes
  the **rendered canonical probe prompts** (`build_award_prompt`/`build_disclosure_prompt`/extracted
  `build_g4_prompt`) → a template drift makes the manifest stale. `manifest_from_pass_table` rebuilds
  a manifest from recorded K=8 counts.
- **`JudgePanel(judges, manifest=…)`** consumes the manifest: reads eligibility by slug, runs **NO
  probes at construction** (the run-to-run gate flip is structurally impossible), discards a judge
  absent from the manifest, refuses a stale manifest. Legacy `calibrate=` path kept for mock tests.

**Commit `6a550a0e4` — R36 scaffolding + R37.2 renderer + provisional manifest:**
- **R37.2** fixed `probe_stability.py`'s `???` renderer (root cause: `json.loads` stringifies the int
  KP keys on the `raw_verdicts.jsonl` round-trip, so `pat.get(1)` missed every cell). New runs only;
  the frozen report is untouched. Verified on real records: `???` → `AAA`.
- **R35.6 provisional manifest of record**: `build_provisional_manifest.py` →
  `07-PILOTS/20260710-probe-stability/20260710-qualification-manifest.json`, reproducing the frozen
  eligibility from the sweep's §0 pass table via the same ≥5/8 gate (gemini all-4, gpt
  coherence+settled-core, both mistrals discarded).

Tests added (all TDD, red→green): `test_retry_parity.py` (5), `test_probe_cause.py` (16),
`test_qualification.py` (8), `test_manifest.py` (8), `test_panel_manifest.py` (5).

## 2. R36 third-family screen (LIVE) — grok-4.20 QUALIFIES disclosure = SECOND family ✅

`probe_stability.py --screen --go` (K=8 gate, `07-PILOTS/20260710-third-family-screen/`):

| candidate | g4 | award-cons | discrim | disc-inv | neg-disc | eligible |
|---|---|---|---|---|---|---|
| `cohere/command-r-08-2024` | 0/8 | 0/8 | 0/8 | 4/8 | 0/8 | **[] — none** |
| `x-ai/grok-4.20` | **8/8** | 0/8 | 0/8 | **8/8** | **8/8** | **{coherence, disclosure, settled_core}** |

- x-ai/grok-4.20 is a **clean** (8/8, zero-variance) disclosure qualifier — correctly excluded from
  OPEN award (award-consistency fail_format + discrimination fail_substantive, the same form failure
  gpt has). **DISCLOSURE-valid families now {google, x-ai} = 2** → the judge-side R30 condition 6 is
  met. OPEN award stays single-family {google} (as the memo anticipated).
- Combined manifest written: `07-PILOTS/20260710-third-family-screen/20260710-third-family-manifest.json`
  (5 judges; gemini all-4, gpt coherence+settled, grok disclosure+coherence+settled, both mistrals
  discarded; fresh template hashes).
- Candidate order was cohere → x-ai/grok → amazon/nova; stopped at grok (first disclosure qualifier).
  grok-4.20 is frontier-tier (no fast grok in the live catalog) — R36.4 explicitly permits tier
  escalation within a new family for the starved surfaces.

## 3. R37.1 floor re-run (LIVE) — settled-core PROMPT FIX CONFIRMED

`floor_rerun.py --go --manifest <combined>` (manifest-driven panel, NO probes re-run — R35.4
live-validated; `07-PILOTS/20260710-floor-rerun/`). Panel = gpt (coherence+settled) + gemini (all-4) +
grok-4.20 (disclosure+coherence+settled); DISCLOSURE families {google, x-ai}, SETTLED-CORE families
{google, openai, x-ai}.

- **Settled-core prompt fix WORKS**: no longer the pre-fix uniform 0.0 collapse. llama contested cells
  AGG-C3=1.0, AGG-C5=0.5; gpt credits AGG-C8 at 1.0. The R33.1-mandate regression session 11 caught is
  fixed.
- **BUT the aggregate 12/12 floor does not cleanly reproduce** — see §4. Reported floor: 2/3 on the
  scoreable llama contested cells; deepseek's contested arm did not score.

## 4. ⚠ FABLE-TRIGGER divergence (the boot prompt's contingency — recommend a short `/model fable` pass)

The floor re-run surfaced the exact "would a wrong answer corrupt a conclusion" situation the boot
prompt reserved Fable for. Three coupled findings, all on `AGG-C8-W305 × llama` / the deepseek arm:

1. **Substantive gpt-vs-gemini divergence on the settled core** (a *fresh judge divergence*): gpt
   scores llama's response `settled_core=1.0`; gemini scores it `0.0`, reading llama's *"the Q151
   calculus does not yield a confident ordering… both involve significant moral wrongness"* as a
   **collapse-to-'both equal' + wrong calculus (Q151 not Q152)** — i.e. llama genuinely FAILED the
   settled core. gpt reads the same text charitably as *declining a confident order* (= the core). This
   is a real intra-panel reading disagreement with H-DISC-grade impact. **Opus did not adjudicate it —
   it is a Fable call.**
2. **grok-4.20 dropped on that one cell (JSONDecodeError)** → the tie-breaker was absent → a 1-1
   gpt/gemini tie resolves to False → aggregate 0.0. grok graded AGG-C3/C5 cleanly, so it is
   live-functional; the parse failure is occasional, not systematic (robustness note — the R35.1
   finish_reason retry does not catch a downstream JSON parse error).
3. **deepseek's entire contested arm 403'd** (`OpenRouter HTTP 403 Forbidden`; WHOLE-C9-W301 also hit
   transport errors across all 3 judges) — a transient provider/routing issue (contested cells ran
   after the OPEN cells), the WALKWORTHY PR-5 empty-retry/provider-routing territory. Operational, not
   a validity finding — but it starved the deepseek contested arm.

**Recommended short Fable check-back (just these questions):**
- **(Q1)** Ratify `x-ai/grok-4.20` as the valid **second disclosure family**? (8/8 clean on both
  disclosure probes incl. the real-item negative-disclosure probe; 1 live JSONDecodeError = robustness
  caveat.) If ratified, the judge-side ≥2-disclosure-family requirement (R30 condition 6) is **met** —
  H-DISC's remaining block becomes G6 (Jimmy) only.
- **(Q2)** Does the settled-core floor "hold" post-fix given the AGG-C8×llama disagreement — i.e. is
  gemini's collapse-to-equal reading correct (→ 0.0 is a genuine weak-SUT failure, floor = credit-when-
  earned) or gpt's (→ 1.0)? This fixes what "12/12 floor" should mean.
- **(Q3)** Direct a clean re-run with provider-pin/empty-retry (PR-5) so the deepseek contested arm and
  grok's AGG-C8 parse are not transport-starved.

If Fable rules these clean, nothing model-blocked remains in WCF-Bench (the rest is G6/Jimmy).

## 5. DEFERRED (unchanged) — earlier-wave transcription ~161 → 230

**Not done — deliberately deferred** (boot prompt item 4: "defer rather than rush it";
fabrication-sensitive; G6-blocked from the gated run regardless). Protocol unchanged: session-11
handoff §3 + `05-BANK-YAML/TRANSCRIPTION-SPEC.md` (10-agent Sonnet fan-out, axis-tag OPEN rubrics,
`AGG-C7-007` contested / `LIB-C7-008` + `LIB-C3-W202` dev_set_only, grep-verify every anchor against
`LargerCatechismwithScriptureProofs1 copy.txt` for WLC Q1–113, fidelity spot-check after).

## 6. Jimmy-blocked (unchanged)

- **G6 confessional panel** — Jimmy recruits raters. Gates the gated G1–G7 run, H-DISC promotion (now
  needs ONLY G6 on the judge side if Fable ratifies grok per Q1 — R30 condition 6 is otherwise met),
  W304/W305 position maps, the 4 LIB `[DISPUTED]` legs.
- OPEN award still single-family {google} — needs a further third family reaching ≥5/8 on the OPEN
  award surface (grok failed it on the award form). cohere/nova/amazon-nova untried at OPEN-award depth;
  next candidate escalation per R36.4 if OPEN-award cross-family is wanted.

## 7. Verify

```
../.venv/bin/python -m pytest COOKBOOK/40-BIBLEBENCH/WCF-Benchmark/04-HARNESS/tests/ -q   # 366 passed
# live (spends ~cents; source ~/.codex/secrets/openrouter.env first):
cd 04-HARNESS && python probe_stability.py --screen          # dry: candidate resolution
python probe_stability.py --screen --go                      # R36 screen
python floor_rerun.py --manifest ../07-PILOTS/20260710-third-family-screen/20260710-third-family-manifest.json  # dry
python floor_rerun.py --go --manifest <combined>             # R37 floor re-run
```

## 8. Re-entry

1. **If the Fable window is open (~2026-07-11):** short `/model fable` pass on §4 Q1–Q3 (grok
   ratification + settled-core floor interpretation + PR-5 re-run direction). This is the one
   remaining model-blocked item.
2. After Fable: apply any re-run direction (PR-5 provider-pin), then §5 transcription (Sonnet fan-out).
3. Read order: this handoff → the R34–R37 memo → `05-BANK-YAML/TRANSCRIPTION-SPEC.md`.

## 9. Sharp edges honored

Report immutability (new dated dirs `20260710-third-family-screen/` + `20260710-floor-rerun/`; the
`???` report + `raw_verdicts.jsonl` + prior pilot dirs untouched; the provisional manifest is a NEW
file in the sweep dir). Shared git index LIVE (a WALKWORTHY sibling commit landed mid-session between
`6a550a0e4` and `b3c010aab`; explicit-path staging, `git log -1` before every commit, never
`git add -A`). Secrets sourced at runtime (`~/.codex/secrets/openrouter.env`), never committed. Canary
`WCFBENCH-CANARY-c1647-x9k4q` not re-minted. No gold minted; no item edited; no G6 run. No deletions.
Live runs from the session main loop (R37.4: not a subagent background shell).
