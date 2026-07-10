# 20260709 — Paste-ready boot prompt: OPUS build of the clean OpenAI API subject/judge adapter (DUPLEX-P0)

> Start the session with `/clear`, then `/model opus`, then paste everything below the line.
> **Model: Opus 4.8.** This is a mechanical, mock-first build — one new adapter mirroring an existing
> one — with no judgment/design calls open, so it is Opus-tier execution, not Fable. (Fable is for
> design / adjudication / adversarial review; nothing of that kind is open on DUPLEX-P0.)

---

You are an Opus builder session adding the **clean OpenAI Messages-API adapter** to the DUPLEX-P0
runner — the one code gap the 2026-07-09 CLI-OAuth smoke identified. The smoke proved the pipeline
runs end-to-end over CLI-OAuth, but confirmed the **OpenAI subjects for a VALID run cannot use
`codex exec`**: the ChatGPT-subscription Codex CLI refuses the roster models (`gpt-5-codex` /
`gpt-5-mini` → 400 "not supported when using Codex with a ChatGPT account", API-only) and is an
agentic runner, not a clean single-turn chat. A valid DUPLEX-P0 run needs the OpenAI vendor via the
OpenAI API — both as the OpenAI **subject** backend AND as the cross-family **judge** for the
Anthropic subjects (§3.5: a judge must not share a vendor with its subject; roster = anthropic +
openai). This session builds that adapter, **mock-first (no live calls, no API key needed to
build)**. Running it later needs `OPENAI_API_KEY`; building and testing it does not.

**Staleness guard first:** `git log -1 -- COOKBOOK/20-DESIGNS/DUPLEX-P0/` — confirm the latest
DUPLEX-P0 commit is `be8faf0df` (CLI-OAuth smoke) or later; if a later session moved things, read
its handoff before touching code.

**Read first (in order):**
1. `COOKBOOK/20260709-f1-f5-build-handoff.md` — the F-1…F-5 build state (now 129/129 green) + the
   remaining Jimmy-gated chain.
2. `COOKBOOK/20-DESIGNS/DUPLEX-P0/20260709-cli-oauth-smoke-report.md` — the smoke findings, the
   OpenAI boundary (why this adapter is needed), and the recommendation.
3. `COOKBOOK/20-DESIGNS/DUPLEX-P0/runner/adapters.py` — the vendor-neutral adapter interface;
   **mirror `AnthropicAdapter`'s F-1 shape exactly** (bounded `_retry` + `AdministrationError`,
   class-name-matched transient set, `resolve_auth_mode`, bare-client credential chain,
   `omit_sampling_params`). `OpenAICodexAdapter` stays (smoke path). Also `runner/roster.py`,
   `config/p0-roster.yaml`, and `run_p0.py` (`build_adapter` factory + `make_judge_scorer` +
   `build_orchestrator`).

**Working dir:** `COOKBOOK/20-DESIGNS/DUPLEX-P0/`. Suite is **129/129 green**
(`../../../../.venv/bin/python -m pytest tests/` — adjust the venv path). Every behavior lands
**red→green**, mock-first: inject a fake OpenAI client (a `SimpleNamespace` with
`chat.completions.create`) — **NO live calls in the suite**, exactly like the AnthropicAdapter tests.

**Build `OpenAIAPIAdapter` (new class in `runner/adapters.py`):**
- **Interface** identical to `AnthropicAdapter.administer(prompt, model_id, temperature, seed,
  max_tokens=1024, system=None, omit_sampling_params=False, **_) -> AdapterResult`.
- **Backend:** OpenAI Python SDK, single-turn **Chat Completions**
  (`client.chat.completions.create(model=model_id, messages=[{"role":"system",...}?,
  {"role":"user","content":prompt}], temperature=…, max_tokens=…)`). Chat Completions is the
  simplest stable single-turn surface; the Responses API is an acceptable alternative — pick one and
  note the choice. **Defer-import `openai`** inside the client property (like AnthropicAdapter
  defer-imports anthropic) so building/tests need no install.
- **Credentials (mirror F-1 spirit):** construct a bare `openai.OpenAI()` and let the SDK resolve
  `OPENAI_API_KEY`; do NOT hard-require a key at construction; fail loud only when the first call
  errors with an authentication error; record the auth mode in run metadata.
- **F-1 retry/refusal semantics (mirror exactly):** bounded exponential-backoff retry for TRANSIENT
  OpenAI errors (rate-limit / 5xx / APIConnection / timeout — match by `type(exc).__name__` against
  a name set, so tests need no SDK, same trick as `_TRANSIENT_ANTHROPIC_ERROR_NAMES`); auth /
  bad-request errors raise immediately, unretried; a persistent transient failure raises
  `AdministrationError` (never a refusal, never a checkpointed record). `refusal_flag` = **False**
  (Chat Completions has no universal structured refusal signal — a content refusal is the
  scorer→None→`no_stance` path, same as Codex). Extract text from
  `resp.choices[0].message.content`; `raw` = the response dict (`.model_dump()` when available).
- **F-2:** honor `omit_sampling_params` (omit `temperature` when set). The roster's OpenAI models
  accept `temperature`, so this is inert for the real roster, but wire it for symmetry with F-2.

**Wire it in:**
- `build_adapter("openai", ...)` returns `OpenAIAPIAdapter` by default (the real run). Keep
  `OpenAICodexAdapter` constructible for the smoke (e.g. `build_adapter("openai", backend="codex")`
  or leave the smoke to construct it directly — do NOT delete it).
- Confirm `run_p0.py`'s `make_judge_scorer` + `build_orchestrator` now hand the OpenAI vendor a clean
  single-turn adapter (the judge for Anthropic subjects is OpenAI — this makes cross-family judging
  actually runnable).

**Tests (mock-first; quote the governing rule where one applies — §3.5 cross-family, F-1 SA-5):**
- constructs the right Chat Completions call (model, messages incl. system when given,
  temperature/max_tokens); reads `choices[0].message.content`.
- bounded retry: a transient error retried then succeeds; a persistent transient raises
  `AdministrationError`; an auth error raises immediately, unretried (assert call count == 1).
- `refusal_flag` always False; a scoreless completion → `no_stance` via the orchestrator.
- `omit_sampling_params=True` omits `temperature` from the call.
- `build_adapter("openai")` returns the API adapter; the codex adapter is still reachable for the smoke.
- (recommended) extend the F-4 smoke test: a mock-adapter `run_p0.py` run with the API adapter for
  OpenAI + a mock Anthropic → records → all three gates end-to-end (both vendors on the API path).

**After:** full suite green; write a NEW dated evidence addendum (do NOT edit the dated F-1…F-5 or
Session-A tables — report-immutability); dated handoff (`COOKBOOK/2026MMDD-openai-adapter-handoff.md`);
memory update ([[cookbook-project-state]]); **push**. In the handoff, spell out the remaining
live-run chain (this session does NOT run it): Anthropic via `ant auth login` (or key) → SDK
adapter; OpenAI via `OPENAI_API_KEY` → this new adapter; **cross-vendor judge scorer live-calibrated**
(does `make_judge_scorer`'s 1–5 stance extraction hold on real responses? add a repair if not); G3 in
fallback mode (no human anchor needed) or the G3 mini-norm. For the live run, install the OpenAI SDK:
`/Users/jimmy.lin/Documents/CEI-Literature-Vault/.venv/bin/python -m pip install openai` (macOS
arm64: `python -m pip`, never bare `pip`).

**Discipline:** parallel sessions share the git index — **path-scoped staging only** (never
`git add -A`), `git log -1` immediately before every commit, commit per coherent unit. No `rm` ever —
`mv` to the nearest `RECYCLE-BIN/`. **Keep this thread DUPLEX-P0-only**; the WALKWORTHY / WCF-Bench
commits interleaved in `git log` are sibling sessions, not this thread — path-scope so their staged
files never ride along. Do not relitigate frozen rulings (the 2026-07-05 memo, CS/IB/PS series, the
Fable Session-A review, the F-1…F-5 fixes, the V-2 `claude -p` prohibition).

**Alternative direction (only if Jimmy says so):** if you want to stay subscription-only and NOT use
an OpenAI API key, a valid cross-family run is not achievable via `codex exec` (roster models
unavailable + agentic). The fallback would be to enable the deferred **Gemini** vendor (google-genai
SDK) as the cross-family subject/judge instead — a larger build. Absent that instruction, build the
OpenAI API adapter above.

---
