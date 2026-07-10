# CLI-OAuth Bring-Up Log — T1 Provisional Runner

**Date:** 2026-07-09 (probes run 2026-07-10 UTC per timestamps) · **Machine:** this one
**Provenance of everything below:** `cli-oauth-provisional`. Nothing here is an API measurement.
**Authorization:** `INNOVATION/20260709d-cli-oauth-provisional-ruling.md` (GREEN lane §3, §7).

This file documents the EXACT headless invocation each backend uses and why, established empirically with trivial probes.

---

## Summary

| Family | CLI | Version | Status | Headless invocation (final) |
|---|---|---|---|---|
| Anthropic | `claude` | 2.1.183 | **WORKING** | `claude -p PROMPT --model <alias> --output-format json </dev/null` |
| OpenAI | `codex` | 0.134.0 | **WORKING** | `codex exec --json --skip-git-repo-check --sandbox read-only -C <dir> -o <lastfile> PROMPT </dev/null` |
| Google | `gemini` | 0.41.2 | **BROKEN** | headless mode reachable but account tier server-side deprecated (`IneligibleTierError`) — no flag fixes it |

Two of three families usable. Smoke runs on Anthropic + OpenAI.

---

## Anthropic — `claude` 2.1.183 — WORKING

### Probe 1: JSON output
```
claude -p "Reply with exactly the word OK" --output-format json </dev/null
```
- Exit 0. Output is a **JSON array of event objects**; the last object has `"type":"result"`.
- Final `result` object fields used: `.result` (completion text), `.is_error` (bool), `.duration_ms`, `.session_id`, `.total_cost_usd`, `.modelUsage` (dict keyed by resolved model id).
- **Model id self-report:** the *authoritative* resolved model id is the **key of `.modelUsage`** (e.g. `claude-opus-4-8`), NOT anything the model says in prose. With no `--model`, it inherited the *calling session's* model (`claude-fable-5`) — so we always pass an explicit `--model`.

### Probe 2: model pinning
```
claude -p "Reply with exactly the word OK" --model opus --output-format json </dev/null
```
- Exit 0, `.result == "OK"`, `.modelUsage` key == `claude-opus-4-8`. **`--model <alias>` works** and the modelUsage key reflects the real resolved id.

### Probe 3: env isolation (NEGATIVE result — important)
```
env -i HOME=$HOME PATH=$PATH claude -p "..." --model opus --output-format json </dev/null
```
- Returned `result == "Not logged in · Please run /login"`. **Stripping the environment breaks subscription auth.**
- **Decision:** the backend runs `claude` with the **inherited environment** (no `env -i`). No session-env interference was observed in practice (probes from inside a Claude Code session succeeded).

### Final decisions (anthropic)
- Invocation: `claude -p PROMPT --model <alias> --output-format json </dev/null`, inherited env, hard timeout (subprocess `timeout=`).
- `</dev/null` on stdin so a piped/closed stdin never hangs it.
- Parse: load JSON array, take the `type==result` object. `text=.result`, `is_error=.is_error`, model id = sole key of `.modelUsage`.
- Errors surface as `.is_error==true` and/or a `.result` string like "Not logged in…". Non-zero exit also possible. We classify error/refusal from both.

---

## OpenAI — `codex` 0.134.0 — WORKING

### Probe 1: first attempt hung on stdin
```
codex exec --json --skip-git-repo-check --sandbox read-only -C /tmp -o LAST "Reply OK"
```
- Emitted `Reading additional input from stdin...` — codex **appends piped stdin to the prompt** and will block on an open stdin. Completion still returned (`agent_message.text == "OK"`), but risk of hang.
- **Fix:** always pass `</dev/null`.

### Probe 2: stdin closed
```
codex exec --json --skip-git-repo-check --sandbox read-only -C /tmp -o LAST "..." </dev/null
```
- Exit 0. JSONL event stream on stdout. Final answer available two ways:
  1. `--output-last-message LAST` writes the clean final text to a file (we use this).
  2. the `{"type":"item.completed","item":{"type":"agent_message","text":...}}` event.
- Harmless stderr noise: `ERROR codex_models_manager::cache: failed to load models cache: unknown variant 'max'…` and `Reading additional input from stdin...` — ignore.

### Probe 3: model pinning (NEGATIVE — important)
```
codex exec ... -m gpt-5 "Reply OK" </dev/null
```
- **400 invalid_request**: `The 'gpt-5' model is not supported when using Codex with a ChatGPT account.`
- Surfaces as `{"type":"error",...}` + `{"type":"turn.failed",...}` events; the `-o` file is NOT written.
- **Decision:** do NOT pass `-m`. Let codex use the ChatGPT-account default. `~/.codex/config.toml` has `model = "gpt-5.5"`, `model_reasoning_effort = "xhigh"`. We record `gpt-5.5` (config default) as the authoritative `model_id_reported`; the model's prose self-report ("Codex, based on GPT-5.") is captured separately and treated as unreliable.

### Final decisions (openai)
- Invocation: `codex exec --json --skip-git-repo-check --sandbox read-only -C <workdir> -o <lastfile> PROMPT </dev/null`, hard timeout.
- `--sandbox read-only` so model-generated shell can't touch disk; `--skip-git-repo-check` so it runs anywhere; `-C <isolated tmp dir>` as working root.
- Parse: prefer the `-o` last-message file; fall back to the last `agent_message` event. Detect failure via `turn.failed`/`error` events → classify as error.
- Model id = config default `gpt-5.5` (stamped); do not pass `-m`.

---

## Google — `gemini` 0.41.2 — BROKEN

### Probe 1: json, default dir
```
gemini -o json -p "Reply with exactly the word OK" </dev/null
```
- Exit 55: `Gemini CLI is not running in a trusted directory. To proceed, either use --skip-trust …`

### Probe 2: add --skip-trust
```
gemini --skip-trust -o json -p "Reply with exactly the word OK" </dev/null
```
- Exit 1: **`IneligibleTierError: This client is no longer supported for Gemini Code Assist for individuals. To continue using Gemini, please migrate to the Antigravity suite of products: https://antigravity.google`**

### Probe 3: text output + explicit model
```
gemini --skip-trust -p "Reply with exactly the word OK" </dev/null
gemini --skip-trust -m gemini-2.5-flash -p "Reply OK" </dev/null
```
- Both fail with the same `IneligibleTierError` / OAuth `requestPost` failure.
- Auth artifact `~/.gemini/oauth_creds.json` **is present** (1801 bytes, dated Jul 9). The failure is **server-side account-tier deprecation**, not a missing credential or a flag problem.

### Conclusion (google)
- **BROKEN for headless use on this account.** The Gemini Code Assist "for individuals" tier that this OAuth cred belongs to has been retired server-side; the CLI directs migration to Antigravity. No CLI flag recovers it.
- The `google_cli` backend is implemented (drop-in ready) but **disabled by default**; it will start working if/when the account is re-provisioned or an API key lands (at which point a proper `google_api` backend supersedes it anyway).
- Smoke and integration tests therefore run on **Anthropic + OpenAI only**; Google is recorded as BROKEN with the exact evidence above.

---

## Cross-cutting decisions baked into the backends

- **Hard timeout:** every subprocess call wrapped with `subprocess.run(..., timeout=T)`; a `TimeoutExpired` → `ResponseStatus.TIMEOUT` (never hangs the runner).
- **stdin:** always `stdin=DEVNULL` (both working CLIs otherwise read/append stdin).
- **env:** inherited (NOT `env -i`) — stripping breaks claude subscription auth.
- **CLI version** captured once per run via `<cli> --version` and stamped on every record.
- **Refusals are data:** classified (`refusal`) and logged, never raised.
- **Full transcript:** every call's exact `argv`, prompt, params, raw stdout/stderr, parsed text, and classification appended to `transcripts/20260709-<runid>.jsonl`.
