# 20260709 — DUPLEX-P0 CLI-OAuth SMOKE-PILOT report

> **SMOKE-PILOT — plumbing evidence only, NOT a valid P0 measurement.** Administered a handful of
> real calls over the operator's CLI-OAuth subscriptions (no API keys) purely to confirm the
> pipeline runs end-to-end. The Session-A memo's **V-2 addendum PROHIBITS `claude -p` for the real
> P0** (no param/`stop_reason` control, harness contamination); this smoke uses the SMOKE-ONLY
> `runner.cli_adapters` backend and is completely separate from `run_p0.py` (which stays
> SDK/Messages-API-only). Do NOT feed any number here to the P0 adjudication.

Runner: `smoke_cli_oauth.py` (`python smoke_cli_oauth.py --items 1 --openai-model gpt-5.5`).

## Result: both CLI-OAuth backends administer end-to-end ✅ (with one OpenAI boundary)

| Vendor | Backend | Auth | Roster models on the subscription | Smoke result |
|---|---|---|---|---|
| Anthropic | `claude -p` (Claude Code CLI) | subscription OAuth ✅ | claude-haiku-4-5, claude-sonnet-4-6 both resolve ✅ | **clean** — direct single-turn text answers |
| OpenAI | `codex exec` (Codex CLI) | ChatGPT-account OAuth ✅ | **gpt-5-codex / gpt-5-mini → 400 "not supported when using Codex with a ChatGPT account"** ❌ (API-only). Subscription default **gpt-5.5** resolves ✅ | works via gpt-5.5, but codex is an **agentic runner** (not a clean chat) |

### End-to-end pipeline evidence (9 records, 3 subjects × 1 item × 3 conditions)

- All 9 administrations succeeded (6 `claude -p` + 3 `codex exec`), all scored, `refusals_by_vendor={}`.
- **F-2 (V-4 temperature drop) verified on REAL cross-vendor calls:** the two Anthropic
  `extended_thinking` records carry `v4_temp_drop=True, effective_temperature=None`; every other
  Anthropic record and the OpenAI `extended_thinking` record carry `v4_temp_drop=False,
  effective_temperature=0.7`. The per-record `(vendor, condition)` keying is exactly right — the
  drop fires only for Anthropic thinking, never for the OpenAI subject.
- **F-1 (refusal handling)** in play — `refusal_report()` returns empty (no refusals); no
  administration errors on the successful path.
- **All three gates computed** (`run_p0_gates`) without crashing: `G1 verdict=FAIL`
  (`process_cv=None` — with `reps=1` every cell is `incomplete`, so the guards correctly return no
  signal rather than a bogus number), `G2 pass=False`, `G3 pass=False` (`no greene_subset records`
  fail-loud reason — the smoke bank has no Greene items). `overall_pass=False` — a SMOKE, not a
  decision. The degenerate verdicts are the guards working on 1-rep, crude-scorer data, not a bug.

**What this validates:** the adapters → records (with the F-1/F-2 fields) → gates flow works with
real CLI-OAuth calls, and the F-2 V-4 bookkeeping is correct across vendors. **What it does NOT
provide:** a valid measurement (V-2 contamination, subscription model limits, `reps=1`, and a crude
placeholder scorer instead of the cross-vendor judge).

## OpenAI boundary (the load-bearing finding)

The ChatGPT-account Codex CLI cannot administer the **roster** OpenAI models — `gpt-5-codex` and
`gpt-5-mini` both return `400 invalid_request_error: "... not supported when using Codex with a
ChatGPT account"`. Only the subscription default (`gpt-5.5`) resolves. And `codex exec` is
fundamentally an **agentic coder**, not a chat completion: even under `--sandbox read-only` it read
skill files and ran `sed` shell commands before answering (heavy harness contamination, worse than
`claude -p`). Conclusion, consistent with the "CLI-OAuth = smoke-only" rule: **the OpenAI subjects
for a valid DUPLEX-P0 run need the Messages/Responses API** (roster models + clean single-turn),
not the ChatGPT-subscription Codex CLI.

## Safety + config notes (surfaced during the smoke)

- **Codex is constrained** for the smoke: `--sandbox read-only -C /tmp` (subject cannot write; kept
  off the vault, which has a strict no-delete rule) + `--ignore-user-config`. `claude -p` is run
  from `cwd=/tmp` to reduce (not eliminate) project-context contamination. These are additive,
  backward-compatible options on `OpenAICodexAdapter` (`cwd`/`sandbox`/`extra_args`); `run_p0.py` is
  unaffected and still constructs the plain adapter.
- **Two local codex config issues** were surfaced and bypassed (user-side, not our code):
  (1) `~/.codex/config.toml` references a broken plugin — `failed to read skills dir …/plugins/
  cache/openai-curated-remote/documents-router/… No such file or directory`; (2) an invalid effort
  enum — `unknown variant 'max', expected one of none/minimal/low/medium/high/xhigh`.
  `--ignore-user-config` sidesteps both (auth still uses `CODEX_HOME`). If you want `codex exec` to
  work without that flag, repair or remove the `documents-router` plugin entry and the `max` effort
  value in `~/.codex/config.toml`.

## Guardrails (so this can never become the real run)

- `runner/cli_adapters.py` is marked `SMOKE_ONLY = True` and is kept OUT of
  `runner.adapters.build_adapter` and OUT of `run_p0.py`.
- `run_p0.py` administers Anthropic subjects through the SDK adapter only and its docstring keeps
  the `claude -p` prohibition; the validity path never touches this module.
- Every record this backend produces carries `raw.smoke_only=True` / `raw.backend="claude -p"`.

## Recommendation

The smoke has validated the pipeline plumbing over CLI-OAuth. For the **valid** P0 run:
- **Anthropic:** `ant auth login` (platform OAuth, no static key) or an API key → the SDK adapter
  (`run_p0.py`), which gives full `max_tokens`/thinking/temperature control and `stop_reason`.
- **OpenAI:** the Messages/Responses (or Chat Completions) API for the roster models — a
  clean single-turn adapter, not `codex exec`. (This is a small new adapter; the roster + judge
  wiring in `run_p0.py` already expects a vendor-neutral adapter interface.)
