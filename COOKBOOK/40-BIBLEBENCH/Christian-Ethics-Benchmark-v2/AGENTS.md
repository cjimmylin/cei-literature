# AGENTS.md — Christian-Ethics-Benchmark-v2 operational rules

Carried forward from v1 (`../Christian-Ethics-Benchmark/AGENTS.md`) — these bit the
project before. Read before any live run.

1. **OpenRouter 402 token-reservation trap.** OpenRouter reserves
   `max_tokens × output-price` against the balance per request, up front. A missing cap
   reserves the model's full default (up to 65536) and calls 402 "requires more
   credits" even with cents of real cost. ALWAYS pass an explicit max-tokens cap
   (`--max-tokens 4096`–`8192` or `GenerateConfig(max_tokens=…)`) on every model,
   including the judge.
2. **No sampling params to Opus 4.7+/Fable models.** `temperature`/`top_p`/`top_k`
   → HTTP 400 (adaptive thinking only). Pin decoding via prompt, not sampling params.
3. **Subscription CLIs are smoke-only** (ToS). The sanctioned measurement path is the
   OpenRouter developer API (key file: `~/.codex/secrets/openrouter.env`).
4. **Spend gates.** PF-003 $5 ceiling per unauthorized run; anything larger needs an
   explicit owner (Jimmy) authorization. The 2026-07-15 live smoke (< $1) is authorized.
5. **v1 folder is read-only.** Copies and imports only. Fixes land on v2 `banks/`
   copies; never delete an item — mark `runnable: false` with a reason.
6. **Holdout discipline.** `banks-holdout/`, `datasets/holdout/` and
   `datasets/v4/holdout/` are gitignored (the v4 dir was added 2026-08-06 after a
   session briefly tracked it — untracked in `31dc22c42`; it remains in pushed
   history `2c67334cb..`, purge is an owner decision). The loader raises unless
   `WALKWORTHY_ALLOW_HOLDOUT=1` is set (v1 HoldoutAccessError convention); wire the
   same guard into any v4 loader. Never include holdout items in committed reports
   or prompts.
7. **No file deletions anywhere in the vault** — `mv` to `RECYCLE-BIN/` instead.
8. **Reports are immutable.** New reports get new `YYYYMMDD-` prefixes.
