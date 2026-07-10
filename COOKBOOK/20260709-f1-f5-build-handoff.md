# 20260709 — Handoff: DUPLEX-P0 F-1…F-5 Opus build session

**Session:** Opus 4.8 (1M context) main loop, 2026-07-09. **Scope:** mechanical execution of the
five blocking fix packages F-1…F-5 from the binding Fable Session-A review
(`DUPLEX-P0/20260709-fable-session-a-review.md`, verdict CONDITIONAL-GO). No judgment calls were
open; the memo pre-specified every fix. All work path-scoped to `20-DESIGNS/DUPLEX-P0/`.

## What was done

Each fix landed **red→green** with a test that quotes the governing memo sentence (A1/A2
discipline). Baseline **95/95** → **122/122 green** (+27 new/replaced spec-quoting tests, incl. the
audit-resolution lock test). Commits (each committed with an explicit pathspec — the index is shared
with concurrent WALKWORTHY / WCF-Bench sessions, [[parallel-sessions-share-git-index]]):

| Fix | Memo | Commit | Summary |
|---|---|---|---|
| **F-1** | SA-5 + SA-5.4 + OAuth addendum | `da9737c3d` | Codex `returncode!=0` = administration error → bounded exp-backoff retry → RAISE `AdministrationError` fail-loud (never a refusal, never a record, never checkpointed); Codex `refusal_flag` always False. AnthropicAdapter gains the same retry for transient API errors (auth/bad-request NOT retried → raise at once); `stop_reason=='refusal'` unchanged. `refusal_report()` splits refusal counts (by vendor/category) from a separate admin-error bucket + discloses the vendor signal asymmetry. AnthropicAdapter no longer hard-requires `ANTHROPIC_API_KEY` — bare `anthropic.Anthropic()` + `resolve_auth_mode()`. |
| **F-2** | SA-6 + sampling-param addendum | `1aba9668f` | Implements the V-4 drop itself (no drop path existed upstream — the run would have 400'd on the first `extended_thinking` call). `effective_temperature()` decides omit + `v4_temp_drop` per (model,condition); records carry `requested_temperature`/`effective_temperature`/`v4_temp_drop`/`temp_drop_reason`; `AnthropicAdapter` omits `temperature` when flagged. `gates._cell_state` keys UNMEASURABLE on per-record `v4_temp_drop` (all records in the cell) OR a `(model_id,condition)`-scoped override — bare condition names removed. Model-capability gate (`model_rejects_sampling_params`) omits sampling params for Opus 4.7/4.8/Fable with `v4_temp_drop=False` (distinct from the thinking drop). |
| **F-3** | SA-7 | `2f046cba3` | `is_pole_collapsed()` = exact-suffix (`endswith("-M030")`) / exact-ID match, not substring; real-bank test asserts exactly one match (`DPX-P0-M030`). |
| **F-4** | SA-8 + env addendum | `26d008577` | `run_p0.py` entrypoint: pins `frames`, `administer_greene_fallback`, `strict_prompts`, `g1_high/low_condition` (SA-1.1), `g3_min_effect=0.02` (SA-4.b), `g1_unmeasurable_overrides` (tuple set); enforces obfuscation-QA **before** scoring; `check_anthropic_env()` fails loud on the empty-key and both-key+token footguns; cross-vendor judge scorer + recognition-QA pass wired for `main()`. |
| **F-5** | A-1 / SA-2 | `15486d4a3` | `process_beats_content` also computes `process_cv_item_grain` + `content_cv_item_grain` (per-item cross-model CVs, ε-guarded, skipped counted), a `sensitivity_reversed` flag, and per-axis skipped counts; a numeric PASS with reversed sensitivity → PROVISIONAL (3rd trigger); a FAIL is never softened. |
| — | evidence addendum | `e53842f40` | `DUPLEX-P0/20260709-f1-f5-checklist-evidence-addendum.md` — one row per fix, Session-A columns (the dated Session-A table itself is NOT edited; report-immutability). |

## Superseded tests (the two overturns)

Per the boot prompt, the tests certifying the OVERTURNED behavior were REPLACED with memo-quoting
ones, not weakened:
- `test_codex_adapter_refusal_flag_from_returncode_not_substring` (asserted `returncode!=0` →
  `refusal_flag=True`) → replaced by the SA-5 admin-error / always-False-refusal tests.
- `test_g1_unmeasurable_cell_excluded_from_both_num_and_denom` (condition-name keying via
  `unmeasurable_conditions={"extended_thinking"}`) → replaced by the SA-6 per-record `v4_temp_drop`
  keying tests, incl. the required "SD≈0 Codex cell in the same condition codes DEAD" test.

## Non-building A1/A2 audit (WS-1 §3)

A fresh Opus auditor that did NOT build the code ran the A1/A2 code-vs-spec grammar over the **F-1
and F-2 diffs only** (commits `da9737c3d` + `1aba9668f`), grading each implementation and test
against the memo's SA-5/SA-6 sentences. **Verdict: FINDINGS — all MINOR/NIT, no BLOCKING.** All 9
checklist items graded FAITHFUL: both overturns solid, the anti-revert guards real (an SA-5 revert
fails `test_codex_returncode_nonzero_is_admin_error_not_refusal`; an SA-6 revert fails the
per-record keying tests), the `cell_v4drop` `all()`-semantics correct (a missing/None flag → DEAD),
the capability gate matches Opus 4.7/4.8/Fable but not the roster, and the shared `_retry` bound is
N+1 attempts consistently across both adapters (no off-by-one, no divergence).

Three findings, all in F-1's Anthropic transient-error set — **resolved in commit `14917c84a`**
after verifying the auditor's empirical claims against the installed anthropic 0.84.0:
- **F-1.a (MINOR):** `"APIConnectionTimeoutError"` was a dead entry (absent from 0.84.0) — removed;
  `APITimeoutError` already covers timeouts.
- **F-1.b (MINOR):** the set omitted `ServiceUnavailableError` (503) and `DeadlineExceededError`
  (504) — real transient service conditions that were raising unretried on a live run. Added, with
  a +1 lock test.
- **F-1.c (NIT):** comment now pins the SDK version whose `_exceptions` names these are and notes
  the by-name match fails OPEN on a future rename (re-verify on a version bump).
- Out-of-scope doc-drift the auditor flagged (stale "Haiku 3.5" / "key from env" in the module
  docstring) also fixed in the same commit.

Suite re-greened **122/122** after the resolution. No BLOCKING divergence was found; the two
overturns are validity-clean.

## What remains (unchanged chain — all Jimmy-gated)

Nothing in the code is open. The DUPLEX-P0 chain is now:
1. **Credentials (Jimmy).** Anthropic side: `ant auth login` (platform OAuth, org-billed — the
   AnthropicAdapter now resolves the profile without a static key) **and** make sure
   `ANTHROPIC_API_KEY` is fully UNSET (an empty `""` still outranks the profile; `run_p0.py`'s
   `check_anthropic_env` fails loud on that and on key+token both-set). OpenAI side: the Codex-OAuth
   login (`codex login`). This is now self-serviceable — no key minting required.
2. **Real P0 run** via `run_p0.py` (`main()` wires the roster adapters, the recognition-QA pass, and
   the cross-vendor judge scorer). `claude -p` administration is PROHIBITED (SDK adapter only).
3. **Mechanical adjudication** per `DUPLEX-P0/20260706-p0-adjudication-protocol.md` as amended by
   A-1 (the third PROVISIONAL trigger).

Also still Jimmy's (unchanged): the G3 human mini-norm launch, and the design-named Haiku 3.5 →
`claude-haiku-4-5` substitution call (roster note; the substitute accepts `temperature`).

## Known issues / notes

- **Sampling-param gate is inert for the current roster.** Opus 4.6 / Sonnet 4.6 / claude-haiku-4-5
  all accept `temperature`; the capability gate is future-proofing for a 4.7+/Fable subject. The
  only omit path that fires on the real run is the V-4 Anthropic-`extended_thinking` thinking drop.
- **Live judge scorer / recognition-QA pass are not unit-tested** (they require live calls). They
  are exercised structurally via the mock-first seams; `run_p0`/`build_orchestrator`/`gate_config`/
  `check_anthropic_env` are the tested surfaces. If the judge's 1–5 stance extraction or the
  recognition markers need tuning, that is a live-run calibration step, not an F-1…F-5 gap.
- Facts for F-2 (which roster models reject sampling params; extended-thinking × temperature) were
  verified against the claude-api reference at build time, not memory.

## Re-entry

Everything is on `main`, pushed, no branches. There is no further Opus build work on DUPLEX-P0
until a Jimmy input lands (credentials). Memory anchor: [[cookbook-project-state]].
