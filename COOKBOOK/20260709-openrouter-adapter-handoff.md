# DUPLEX-P0 — OpenRouter cross-family adapter: session handoff (2026-07-09, Opus builder)

**Commit(s) this session:** see `git log` for the `DUPLEX-P0: OpenRouter cross-family adapter` commit.
**Suite:** 144/144 green (was 129) — mock-first, NO live calls.
**Scope:** DUPLEX-P0 only. Path-scoped staging; no sibling-session files touched.

---

## What was built (why)

The remaining code gap the 2026-07-09 CLI-OAuth smoke exposed: a **clean OpenAI-compatible Chat
Completions adapter** for the cross-family (§3.5) slot. Jimmy chose **OpenRouter** as that vendor
(not OpenAI-direct, not the deferred Gemini vendor). Because OpenRouter is OpenAI-compatible, one
`OpenAIAPIAdapter` (parameterized `base_url` + `api_key_env`) serves OpenRouter now and OpenAI-direct
later with no code fork. Anthropic stays native (SDK / `ant auth login` OAuth).

Details + full test evidence: `COOKBOOK/20-DESIGNS/DUPLEX-P0/20260709-openrouter-adapter-evidence-addendum.md`.

**Nothing is open on the DUPLEX-P0 code for the mock build.** What remains is the live-run chain,
which needs credentials + a few live-only confirmations (below). This session does NOT run it.

---

## Remaining live-run chain (Jimmy-gated)

1. **Credentials**
   - **Anthropic:** `ant auth login` OAuth (or a key). `check_anthropic_env()` already guards the two
     footguns (empty `ANTHROPIC_API_KEY=""`; both key+token set).
   - **OpenAI-family via OpenRouter:** export `OPENROUTER_API_KEY`. (There is no OAuth/profile
     fallback for the OpenAI SDK — a missing key fails loud at client construction on the first call,
     which happens during the recognition-QA pass. Consider adding a pre-flight guard symmetric to
     `check_anthropic_env` if you want it to fail before QA; left out here as untested live code.)

2. **Install the OpenAI SDK** (only needed to RUN; the build/tests defer-import it and inject fakes):
   ```
   /Users/jimmy.lin/Documents/CEI-Literature-Vault/.venv/bin/python -m pip install openai
   ```
   (macOS arm64: `python -m pip`, never bare `pip`.)

3. **Verify OpenRouter model ids** — `config/p0-roster.yaml` keeps the design-named `gpt-5-codex` /
   `gpt-5-mini`. OpenRouter addresses models as `<vendor>/<model>` (e.g. `openai/gpt-5-mini`).
   Check each against <https://openrouter.ai/models>; update the `id` to the accepted prefixed form
   (a wrong id is a 400 bad-request → unretried fail-loud). `gpt-5-codex` is a Codex-tuned SKU — if
   OpenRouter lacks it, pin an available OpenAI SKU and LOG the substitution (Haiku-note discipline).
   **Note:** `runner.judges` routes on these ids and `test_p0_roster_judges.py:17` asserts the two
   bare ids — update that test in lockstep if you change them.

4. **Pin the OpenRouter provider (validity)** — OpenRouter may silently route to different upstream
   providers / quantizations. For a rigorous benchmark, pin routing (`provider: {allow_fallbacks:
   false, order: [...]}`) so the underlying provider can't swap mid-run. This is a real validity
   concern; wire it as a `default_headers`/extra-body option on the OpenRouter call before the run.

5. **Reasoning-SKU sampling params** — some reasoning models reject `temperature` and require
   `max_completion_tokens` instead of `max_tokens`. A 400 there is a bad-request (unretried,
   fail-loud), so calibrate per judge/subject model at first live call (`omit_sampling_params` already
   handles the temperature drop; `max_completion_tokens` would be a small adapter tweak if needed).

6. **Live-calibrate the cross-vendor judge scorer** — `make_judge_scorer` extracts a 1-5 stance via
   `\b([1-5])\b` from a `max_tokens=16` completion. Confirm this holds on REAL OpenRouter responses
   (models sometimes prepend prose); add a repair (e.g. tighter prompt / last-integer rule) if not.

7. **G3** — run in fallback mode (no human anchor needed) or run the G3 mini-norm
   (`20260706-g3-mininorm-preregistration.md`).

Then: `run_p0.py::main()` (or `run_p0(...)`) → recognition-QA (before scoring) → 5×2 factorial →
all three gates.

---

## Frozen — do not relitigate

2026-07-05 memo; CS/IB/PS series; Fable Session-A review; F-1…F-5 fixes; the V-2 `claude -p`
prohibition; the CLI-OAuth smoke = smoke-pilot only. The `OpenAICodexAdapter` is retained SMOKE-ONLY
(`build_adapter("openai", backend="codex")`) — do not delete it.

---

## Re-enter

Open a session at `COOKBOOK/20-DESIGNS/DUPLEX-P0/`, read this handoff + the evidence addendum, and —
once Jimmy provides `OPENROUTER_API_KEY` (+ Anthropic OAuth) — work the live-run chain top-down. The
code is done; the next session is credential-gated live execution + the live-only confirmations above.
