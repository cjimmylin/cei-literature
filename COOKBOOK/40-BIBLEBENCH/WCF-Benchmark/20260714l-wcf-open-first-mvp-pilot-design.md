# WCF-Bench Open-First MVP Pilot — Frozen Design

**Date:** 2026-07-14  
**Owner authority:** Jimmy's written “PLEASE IMPLEMENT THIS PLAN” direction  
**Status:** OFFLINE IMPLEMENTATION + ZERO-PAID PUBLIC PREFLIGHT ONLY; empirical execution remains gated

> **EXPLORATORY WCF-BENCH OPEN-FIRST MVP · ONE RUN PER SUT · SINGLE UNQUALIFIED CODEX-OAUTH GPT-5.6 SOL JUDGE · NON-QUOTABLE**

## Paper-facing purpose

Produce a standalone exploratory supplement showing one response per model over the full frozen bank while keeping the four `dev_set_only` items outside every judged or numeric surface. The supplement does not replace, amend, or reopen the accepted PPP-1 manuscript packet.

## Frozen model and request contract

The exact OpenRouter SUT roster is:

1. `minimax/minimax-m3`
2. `z-ai/glm-5.2`
3. `deepseek/deepseek-v4-pro`
4. `qwen/qwen3.7-max`
5. `google/gemma-4-31b-it`
6. `meta-llama/llama-4-maverick`

SUT requests use `temperature=0`, `max_tokens=2048`, no tools, no web, no perturbations, no model substitutions, and no model fallbacks. A reasoning-capable model must accept `reasoning.effort="none"`; a non-reasoning model omits the reasoning field. Provider routing uses `sort="price"`, `require_parameters=true`, `data_collection="deny"`, and a prompt/completion `max_price` pair frozen from the zero-paid catalog refresh. Three model shards may run concurrently; calls within each shard remain sequential.

Qwen3.7 Max is API-only. The study is therefore an **open-first family roster**, not a uniformly open-source roster.

## Geometry and reporting boundary

| Surface | Frozen count |
|---|---:|
| SUT responses | 230 × 6 = 1,380 |
| Runnable/scorable cells | 226 × 6 = 1,356 |
| Diagnostic-only development cells | 4 × 6 = 24 |
| Scalar-eligible cells | 222 × 6 = 1,332 |
| Contested position outputs | 4 × 6 = 24 |
| Logical judge decisions | 348 × 6 = 2,088 |
| OAuth tasks at batch size 8 | 44 × 6 = 264 |

The four development items receive SUT responses only. They are never sent to the judge and never enter a mean, interval, ranking, or coverage denominator. Contested outputs remain separate. Errors remain missing, never zero. A SUT receives a descriptive scalar aggregate only at 200 or more numeric results among its 222 scalar-eligible cells.

## Sole judge contract

The sole judge model is exact `gpt-5.6-sol` at medium reasoning, invoked through the installed Codex CLI's saved ChatGPT authentication only after a separate OAuth-quota authorization. Each `codex exec` task is ephemeral, runs in an empty directory under a read-only sandbox, ignores user configuration and rules, uses a strict JSON schema, receives no more than eight same-SUT/same-route records, and is rejected if its JSONL event stream contains any tool call. Valid unique records persist immediately; only missing or malformed records may be retried, at most twice. OAuth judging is concurrency one.

This is an agent-mediated, unqualified single-judge interface, not a direct OpenAI API endpoint and not a qualified cross-family panel.

## Fail-closed gates

No executable manifest or inference may follow if an exact slug is missing; required context, capability, or price metadata is absent; `reasoning.effort="none"` cannot be verified for a reasoning-capable model; no eligible data-policy endpoint can be verified; or an endpoint exceeds its frozen price ceiling. The first paid response from each SUT belongs to the immutable run and must stop the run if usage shows reasoning tokens or an ignored parameter.

The present implementation direction authorizes no credential access, OAuth task, OpenRouter inference, top-up, manuscript replacement, perturbation, ranking, gate, or rerun.

## Expected deliverables after all later gates pass

A new immutable run directory will hold the frozen manifest, checkpoints, raw evidence, usage ledger, report, and traceability. A separate Markdown/HTML/PDF supplement will report per-SUT, design, route, axis, refusal, contested, coverage, error, and diagnostic surfaces without rankings, release claims, a universal final score, or quotation permission.

## Official interface sources

- OpenRouter public catalog: <https://openrouter.ai/api/v1/models>
- OpenRouter provider routing: <https://openrouter.ai/docs/guides/routing/provider-selection>
- OpenRouter reasoning controls and billing: <https://openrouter.ai/docs/guides/best-practices/reasoning-tokens>
- GPT-5.6 Sol model: <https://developers.openai.com/api/docs/models/gpt-5.6-sol>
- Codex non-interactive mode: <https://learn.chatgpt.com/docs/non-interactive-mode>
- Codex authentication: <https://learn.chatgpt.com/docs/auth>

