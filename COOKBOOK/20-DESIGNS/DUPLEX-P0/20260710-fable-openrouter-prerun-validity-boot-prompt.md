# 20260710 — Paste-ready boot prompt: FABLE pre-run validity review of the OpenRouter-integrated DUPLEX-P0 pilot

> Start a NEW session with `/clear`, then `/model fable`, then paste everything below the line.
> **Model: Fable.** This is a judgment-only, credential-independent adversarial validity review + a
> binding go/no-go — exactly what Fable is for, and it can run NOW (the paid P0 run is
> Jimmy-credential-gated, so front-load this validity call into the closing Fable window so the
> post-credential run is pure Opus mechanics). **Write NO production code and run NO pilot.**
>
> **LANE = DUPLEX-P0 ONLY.** Everything you read, write, and stage lives under
> `COOKBOOK/20-DESIGNS/DUPLEX-P0/`. Do NOT touch, read for decisions, or stage any sibling bench or
> worktree (WALKWORTHY, WCF-Bench, FRUITBENCH, SERMONMOUNT, 10CBench, INNOVATION, papers/…). The repo
> has concurrent sibling sessions with their own worktrees and unpushed branches — path-scope
> everything and never `git add -A`.

---

You are a **Fable adversarial reviewer** issuing a **binding pre-run validity go/no-go** on the
DUPLEX-P0 moral-psychology pilot **as newly reconfigured to run its cross-family (OpenAI-family) slot
through OpenRouter**. The P0 pilot is the portfolio's fork gate: its result decides *build the DUPLEX
generator vs. pivot to the pre-registered CRUX fallback*. A subtly invalid judge/transport config
would silently corrupt that fork, so the OpenRouter deltas must clear a validity review BEFORE the
paid run. **Scope: only the validity DELTAS the OpenRouter pivot introduced** — NOT a redo of the
frozen design.

## What changed since the last Fable review (Opus, 2026-07-09→10; commits `a003626a9`, `16e3ebf5f`, `ebe3a4fde`)

1. **Cross-family vendor = OpenRouter** (Jimmy's call), via a new `OpenAIAPIAdapter` (OpenAI-compatible
   Chat Completions; `base_url`+`api_key_env` knobs). Anthropic stays NATIVE (SDK). §3.5 is argued to
   hold at the model-FAMILY level (OpenRouter = transport, not a model vendor).
2. **Roster OpenAI ids** → verified `openai/gpt-5-codex` / `openai/gpt-5-mini` (both present in the
   347-model OpenRouter catalog; live-reachable; `temperature=0.7` accepted).
3. **CRITICAL live-caught bug + fix:** the judge scorer used `max_tokens=16`; `gpt-5-*` are REASONING
   models and their reasoning tokens count against `max_tokens`, so the visible stance came back `''`
   → every judgment would silently code `no_stance`. Fixed to `_JUDGE_MAX_TOKENS=2048` (live: 16→'',
   2000→'5'). See [[openrouter-reasoning-judge-tokens]].
4. **Haiku H-1 applied:** retired `claude-3-5-haiku-20241022` → `claude-haiku-4-5` (substitute, per
   adjudication-protocol §1), disclosed on the roster entry.
5. **Run decisions LOCKED (Jimmy 2026-07-10):** Anthropic NATIVE; G3 = fallback mode (`g3_human_anchor:
   null`, zero humans). The both-vendors-via-OpenRouter option (all roster Anthropic models also exist
   on OpenRouter) was OFFERED and DECLINED — do not reopen it as a directive, but you MAY flag it as a
   recommendation-to-Jimmy if V-Δ3 finds a judge-asymmetry threat.

The OpenAI-family side is LIVE-VALIDATED end-to-end (auth, ids, real `make_judge_scorer` → 5.0). The
Anthropic side is code-complete but not yet live (credential-gated). Suite 144/144, mock-first.

## Read first (in order) — DUPLEX-P0 lane only

1. `20260710-openrouter-live-validation-and-judge-fix.md` — the live findings + the judge fix (this is the core of what you review).
2. `20260709-openrouter-adapter-evidence-addendum.md` — the adapter build + design choices (seed not sent; refusal_flag=False; §3.5-at-family-level argument).
3. `config/p0-roster.yaml` — the reconfigured roster (openrouter backend, prefixed ids, H-1 Haiku, judge_eligible flags).
4. `run_p0.py` — `make_judge_scorer` + `_JUDGE_MAX_TOKENS` + `build_orchestrator`/`adapter_kwargs_for` wiring; `runner/adapters.py::OpenAIAPIAdapter`.
5. Frozen context (ratify, do not relitigate): `20260709-fable-session-a-review.md` (SA-1…SA-9, F-1…F-5), `20260706-p0-adjudication-protocol.md` (H-1 + fork rubric), `20260709-ws1-checklist-evidence.md`.

## Frozen — DO NOT relitigate
Session-A rulings (SA/F series), the P0 fork-adjudication rubric, H-1, CS/IB/PS series, the
native-Anthropic + G3-fallback decisions, the "OpenRouter is the cross-family vendor" decision. You
review the VALIDITY of the new config, not whether to use OpenRouter at all.

## Your mandate — adjudicate each validity delta, then issue a binding go/no-go

- **V-Δ1 Reasoning-judge validity.** The cross-family judge is now a REASONING model (`gpt-5-mini`/
  `-codex`) at `max_tokens=2048`. Does letting the judge "think" before emitting a 1–5 stance bias or
  destabilize scoring (vs a non-reasoning extractor)? Is 2048 safe against differential
  reasoning-token truncation across items, or is a floor/`reasoning.effort` constraint REQUIRED? Rule:
  valid as-is / valid-with-constraint / blocking.
- **V-Δ2 Provider-routing variance.** OpenRouter may resolve the SAME model id to different upstream
  providers/quantizations across cells. Is provider-pinning (`allow_fallbacks:false`, currently NOT
  built) REQUIRED for the pilot, or optional-until-the-scored-measurement? Rule + set the pre-reg
  condition.
- **V-Δ3 Mixed-transport / judge asymmetry.** Anthropic subjects are judged by an OpenRouter model;
  OpenAI subjects by a native-Anthropic model. Is that transport asymmetry a threat to §3.5 judge
  neutrality (the mirror-flip test)? Does "family-level, gateway-as-transport" actually hold?
- **V-Δ4 Model-identity drift.** Design named "GPT-5 Codex / GPT Mini"; catalog also shows
  gpt-5.1…5.6. Are `gpt-5-codex`/`gpt-5-mini` the intended SKUs, and do they satisfy the design's
  cross-family discrimination requirement? (OpenAI-side analogue of the Haiku H-1 concern.)
- **V-Δ5 Ratify H-1 + judge-eligibility.** Confirm the Haiku substitution + disclosure are adequate
  and don't disturb any gate assumption. Confirm the judge_eligible set is still valid.
- **V-Δ6 Judge-budget cost/feasibility.** Reasoning tokens are billed to the 2048 cap; sanity-check
  the implied run scale/cost so the paid run isn't a surprise (feasibility flag, not a gate).

**Deliverable:** a NEW dated binding memo `COOKBOOK/20-DESIGNS/DUPLEX-P0/20260710-fable-openrouter-prerun-validity-review.md`
with: an overall **GO / CONDITIONAL-GO / NO-GO**, a per-delta ruling (V-Δ1…V-Δ6), any **pre-registered
amendments** (numbered, so the Opus run session applies them mechanically), and an explicit
"conditions the run session MUST satisfy before/at the paid run." Do not edit the dated evidence/F-1…F-5/
Session-A files (report-immutability).

## Do NOT
Run the pilot (credential-gated — Jimmy owes the Anthropic credential). Write production code (if an
amendment needs code, SPECIFY it for the Opus run session, don't implement). Touch or stage anything
outside `COOKBOOK/20-DESIGNS/DUPLEX-P0/`. Reopen frozen rulings.

## Discipline
Lane = DUPLEX-P0 only. Path-scoped staging (never `git add -A`); `git log -1` immediately before any
commit (concurrent sibling sessions share the index). Secrets (`~/.codex/secrets/openrouter.env`) are
Jimmy's — never read, echo, or commit their values; your review does not need them. Commit the memo
path-scoped; update memory ([[cookbook-project-state]]); push.

## After
Append a short "run-session preconditions" block to the memo so the post-credential **Opus** session
(NOT Fable) can execute mechanically: source both secrets → 1-item both-vendor live smoke → cost
estimate for Jimmy's approval → `run_p0.py` → mechanical P0 adjudication (+A-1) applying your amendments.
