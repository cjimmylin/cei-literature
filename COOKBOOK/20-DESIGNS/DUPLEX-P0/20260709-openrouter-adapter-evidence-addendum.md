# DUPLEX-P0 — OpenRouter cross-family adapter: evidence addendum (2026-07-09, Opus builder)

> **New dated addendum — does NOT edit the F-1…F-5 or Session-A tables (report-immutability).**
> Prior addendum: `20260709-f1-f5-checklist-evidence-addendum.md`. This one covers ONLY the
> clean OpenAI-compatible Chat Completions adapter added this session.

## What this session closed

The 2026-07-09 CLI-OAuth smoke (`20260709-cli-oauth-smoke-report.md`) proved the pipeline runs
end-to-end over CLI-OAuth but confirmed the **OpenAI subjects for a VALID run cannot use `codex
exec`** (ChatGPT-subscription Codex refuses the roster's API-only models; it is also an agentic
runner, not a clean single-turn chat). §3.5 requires cross-family judging, so a valid run needs a
clean OpenAI-family backend as BOTH the OpenAI subject AND the judge for the Anthropic subjects.

**Decision (Jimmy, this session): the cross-family vendor is OpenRouter**, not OpenAI-direct and not
the deferred Gemini vendor. OpenRouter exposes an **OpenAI-compatible Chat Completions** surface, so
one adapter — parameterized by `base_url` + key-env — targets OpenRouter now and OpenAI-direct later
with no code fork. Anthropic stays native (SDK / `ant auth login` OAuth); only the cross-family slot
routes through OpenRouter. §3.5 holds at the **model-family** level (OpenRouter is transport, not a
model vendor): Anthropic subjects → judged by an OpenAI-family model (via OpenRouter); OpenAI-family
subjects → judged by a native Anthropic model.

## Build (mock-first TDD — no live calls, no `openai` install needed to build or test)

| Unit | Change | File |
|------|--------|------|
| `OpenAIAPIAdapter` | NEW. OpenAI-compatible **Chat Completions** adapter, mirrors `AnthropicAdapter`'s F-1 shape: deferred `openai` import, bare-client credential resolution (no hard-required key in our code), F-1 bounded exponential-backoff `_retry`, `refusal_flag=False` always, `omit_sampling_params` (F-2). `base_url` + `api_key_env` are construction knobs (OpenAI-direct vs OpenRouter). | `runner/adapters.py` |
| `_TRANSIENT_OPENAI_ERROR_NAMES` + `_is_transient_openai_error` | NEW. Class-NAME match set (`RateLimitError`/`InternalServerError`/`APIConnectionError`/`APITimeoutError`) — same trick + fail-OPEN posture as the anthropic set; auth/bad-request raise immediately, unretried. OpenRouter surfaces upstream failures through these same OpenAI SDK types. | `runner/adapters.py` |
| `resolve_openai_auth_mode` | NEW. Reports `api_key`/`unset` for run metadata (OpenAI SDK is key-only — no OAuth profile fallback). | `runner/adapters.py` |
| `build_adapter("openai", backend=…)` | **DEFAULT FLIPPED**: `backend="api"` (default) → `OpenAIAPIAdapter`; `backend="openrouter"` → presets OpenRouter base_url + `OPENROUTER_API_KEY`; `backend="codex"` → `OpenAICodexAdapter` (SMOKE path **kept**, not deleted). | `runner/adapters.py` |
| `adapter_kwargs_for(roster, vendor)` | NEW. Roster is the single source of truth for the OpenAI backend; pulls `backend`/`auth.base_url`/`auth.env`; `{}` for non-OpenAI vendors (frozen Anthropic path untouched). | `runner/roster.py` |
| `build_orchestrator` + `main` | Now build per-vendor adapters via `build_adapter(v, **adapter_kwargs_for(roster, v))` → OpenAI vendor gets the OpenRouter clean adapter. | `run_p0.py` |
| `config/p0-roster.yaml` | OpenAI vendor → `adapter: openai_api_adapter`, `backend: openrouter`, `auth: {api_key, OPENROUTER_API_KEY, base_url}`. Model ids **kept** `gpt-5-codex`/`gpt-5-mini` (unverified on OpenRouter + keeps `runner.judges` routing) with a loud `TODO(live)` for the `openai/`-prefixed form. | `config/p0-roster.yaml` |
| `make_fake_openai` (+`vary`) | NEW test fixture: fake Chat Completions client recording `last_kwargs`. | `tests/fixtures_p0.py` |

## Test evidence — full suite **144 passed** (was 129; +15 new, +1 intentional flip), 0 warnings

New / changed tests (all mock-first, NO live calls):

- **Adapter (10)** — `test_openai_api_adapter_*`: params+content read; system-message prepend; F-2
  `omit_sampling_params`; `refusal_flag` always False (content refusal → scorer→no_stance);
  bounded-retry-then-succeed; persistent-transient → `AdministrationError`; auth error unretried
  (call count == 1); bad-request (400 unknown model) unretried; injected-client auth mode;
  **OpenRouter construction** (`base_url` + `OPENROUTER_API_KEY` handed to `openai.OpenAI()`).
- **Factory (2)** — `test_build_adapter_factory` (flipped default → `OpenAIAPIAdapter`);
  `test_build_adapter_openai_backend_selector` (api/openrouter/codex; codex still reachable).
- **Wiring (3)** — `test_adapter_kwargs_for_openai_reads_backend_from_roster`;
  `test_build_orchestrator_wires_openrouter_clean_adapter_for_openai_vendor` (openai →
  `OpenAIAPIAdapter` @ OpenRouter; anthropic stays native);
  `test_make_judge_scorer_routes_anthropic_subject_to_openai_api_judge` (§3.5 judge runnable — 1-5
  stance extracted from the OpenAI judge served through the new adapter).
- **End-to-end (1)** — `test_smoke_run_both_vendors_on_api_path_end_to_end`: the REAL
  `OpenAIAPIAdapter` (fake client) + mock Anthropic → records → all three gates (both vendors on the
  API path).

```
$ .venv/bin/python -m pytest tests/ -q
144 passed in ~6s
```

## Design choices logged (for the reviewer / live operator)

1. **`seed` is NOT sent to the API** — retained for checkpoint identity only, matching the Anthropic
   adapter. Symmetric non-determinism at fixed temperature is cleaner for cross-vendor comparability
   (Anthropic has no seed param; the design uses temperature>0 + reps for a distribution by design).
2. **`refusal_flag=False` always** — Chat Completions has no universal structured refusal signal;
   content refusals flow through the scorer→`no_stance` path (WS-1 D10), parity with Codex.
3. **Model ids left design-named** (`gpt-5-codex`/`gpt-5-mini`) — a conscious logged choice, not
   silent drift (same discipline as the Haiku-retirement note). OpenRouter needs `openai/`-prefixed
   ids **verified against its catalog** before the run.

## Not in scope this session (live-run chain — see the handoff)

`OPENROUTER_API_KEY` provisioning; `pip install openai`; OpenRouter provider-pinning
(`allow_fallbacks:false`) to prevent silent provider/quantization swaps mid-benchmark;
`openai/`-prefixed model-id verification; `max_completion_tokens` calibration for reasoning SKUs;
live calibration of the judge 1-5 stance extraction. None of these block the mock-first build.
