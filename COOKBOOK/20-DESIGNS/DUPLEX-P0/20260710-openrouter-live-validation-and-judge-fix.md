# DUPLEX-P0 — OpenRouter live validation + judge-budget fix (2026-07-10, Opus)

> New dated evidence file (does NOT edit the 2026-07-09 addendum or the F-1…F-5 / Session-A tables —
> report-immutability). First LIVE calls on the DUPLEX-P0 OpenAI-family path, using the OpenRouter
> key Jimmy provided at `~/.codex/secrets/openrouter.env` (`OPENROUTER_API_KEY`, 0600).

## What was validated LIVE (real OpenRouter calls through the real `OpenAIAPIAdapter`)

| Check | Result |
|-------|--------|
| Auth via `OPENROUTER_API_KEY` | ✅ `auth_mode=api_key`, calls succeed |
| Model ids exist on OpenRouter | ✅ catalog fetch (347 models): **`openai/gpt-5-codex`** and **`openai/gpt-5-mini`** both present |
| `openai/gpt-5-mini` subject call, `temperature=0.7` | ✅ substantive utilitarian answer; temperature ACCEPTED (no `omit_sampling_params` needed) |
| `openai/gpt-5-codex` reachability | ✅ returned "OK" |
| Real `make_judge_scorer` path (anthropic subject → OpenRouter/OpenAI judge, §3.5) | ✅ returns **`5.0`** (config-driven `backend=openrouter` → prefixed id → extraction) |

## CRITICAL bug caught live — judge budget starved by reasoning tokens

`make_judge_scorer` called the judge with **`max_tokens=16`**. The roster's OpenAI-family judges
(`gpt-5-*`) are **reasoning models**, and on OpenRouter reasoning tokens count against `max_tokens`.
Live result:

- `max_tokens=16`  → completion **`''` (len 0)** → `\b([1-5])\b` finds nothing → `None` →
  **EVERY judgment silently coded `no_stance`** (would have destroyed the entire cross-family score).
- `max_tokens=2000` → clean **`'5'`**.

**Fix (TDD, red→green):** `run_p0.py` now uses `_JUDGE_MAX_TOKENS = 2048` (was 16); the existing
judge-routing test asserts the reasoning-safe budget so it can't silently regress. It is a cap
(billed on actual output; the Anthropic judge stops after the integer), so it is safe for both
vendors. TODO(cost-opt): pass OpenRouter `reasoning.effort=low` via per-call `extra_body` to cut
judge reasoning spend once the adapter supports it (not required for correctness).

## Config change

`config/p0-roster.yaml` OpenAI model ids → the **verified** OpenRouter form `openai/gpt-5-codex` /
`openai/gpt-5-mini` (were the bare design-named ids). `runner.judges` + two tests updated in lockstep.

## Suite

`144/144 green` (unchanged count; the judge-budget + id-prefix changes landed red→green in existing
tests). `openai` SDK 2.45.0 installed into the vault venv.

## Still gated for a FULL P0 run (Jimmy-side)

- **Anthropic credential** — `claude setup-token` → `ANTHROPIC_AUTH_TOKEN`, or an `ANTHROPIC_API_KEY`
  (the OpenAI-family side is now fully live-validated; Anthropic is the remaining vendor).
- **G3 decision** — fallback mode (zero humans, already wired) vs the human mini-norm.
- **Haiku** — roster still names the RETIRED `claude-3-5-haiku-20241022`; apply the ruled
  `claude-haiku-4-5` substitution at run time (Anthropic-side, per the P0 adjudication protocol).
- Provider-pinning (`allow_fallbacks:false`) — recommended before the scored run.

**Secrets hygiene:** the key was sourced from the 0600 env file only at call time and never echoed,
committed, or written into any artifact. The `/tmp` smoke scripts are throwaway (not committed).
