# Session Handoff — CLI-OAuth Bring-Up (Fable, 2026-07-09 night)

**Session:** Fable main loop + 2 Opus execution agents. Boot prompt: `20260709c-cli-oauth-fable-session-boot-prompt.md` — all 4 tasks completed.

## What was done

1. **Provisional ruling (Fable):** `20260709d-cli-oauth-provisional-ruling.md` — vault-wide GREEN/YELLOW/RED lanes for CLI-OAuth model access; new provenance class `cli-oauth-provisional`; pilot-scale volume caps; standing project rulings (THORNS D-37, SERMONMOUNT MF-1…8, DUPLEX P0 roster, v1.x scope locks) explicitly NOT overridden. Jimmy-tier residue queued as **PR-02** in `PENDING-RULINGS.md`.
2. **T1 provisional shim (Opus agent, verified):** `40-BUILDS/t1-runner-provisional/` — vendor-agnostic runner, 3 CLI backends, JSONL transcripts, backoff, provenance stamping. 34 unit + 3 real-token integration tests green. Exact CLI flags in `20260709-cli-bringup-log.md`. **Anthropic + OpenAI WORKING; Google BROKEN** (tier retired server-side — `IneligibleTierError`, Antigravity migration; backend drop-in ready but disabled).
3. **GREEN smoke (Opus agent):** 10 items × 2 working families, clean; report `40-BUILDS/t1-runner-provisional/20260709-smoke-report.md`.
4. **RP-04 S1 machinery pilot (Opus agent, verified):** `40-BUILDS/rp04-corpus/20260709-s1-pilot/20260709-s1-machinery-validation-report.md` — 80 stratified synthetic-mock records × 2 judge families (claude-haiku-4-5, gpt-5.5), END/REC/GEN reconstructed (ACT + controls excluded, documented), 100%/100% injected-label recovery, κ=1.00 (floor check), 0 label leakage (independently re-verified by Fable grep of all 250 sent prompts). NOT a judge-bias measurement — machinery only.
5. **Fable adjudication:** `20260709e-cli-oauth-adjudication.md` — shim **GO** (conditions C1–C5); machinery **PASS**, YELLOW judge-pilot design green-lit contingent on 3rd family + real S3; surprises routed (Gemini → Jimmy action; codex shared-config drift → standing per-call-pinning mitigation).
6. **Living docs updated:** `07-opus-handoff.md` (2.1-provisional entry), `00-CHARTER/04-decision-log.md` (DL-15…17), `~/.claude/../.claude/FABLE-WEEK.md` (vault root), `PENDING-RULINGS.md` (PR-02).

## What remains

- **Jimmy:** PR-02 ruling; Gemini re-provision or API key; API keys (unchanged gate #1 — RED lane stays shut without them).
- **Next Fable session:** Governance Symphony (`CEI-AI-Statements/GENERATION3/20260709-fable-session-boot-prompt.md`), then queued gate reviews if window allows.
- **Post-window Opus:** may use the shim for GREEN/YELLOW work under the ruling (may narrow, never widen lanes). Cycle-2 real runs still key-gated. F1/F2 corpus gaps (ACT renderer, control renderings) are upstream WITNESS work if S1-lane reuse is wanted.

## Known issues

- codex: no model pinning on ChatGPT accounts; slow tails (≥240 s timeouts mandatory); shared `~/.codex/config.toml` is a cross-session hazard — pin config per-call (C2), never edit shared dotfiles silently.
- claude backend without explicit `--model` inherits the calling session's model (observed `claude-fable-5`) — always pass `--model` (C3).
- Shim refusal classifier provisional (C4); hand-audit where refusal counts are load-bearing.
- First codex pilot arm (57/80 instant failures) retained as immutable transcript evidence of the config-drift incident; the clean rerun is the reported arm.

## File inventory (this session, all under CEI-Lit-WS/INNOVATION/ unless noted)

- `20260709d-cli-oauth-provisional-ruling.md` (NEW)
- `20260709e-cli-oauth-adjudication.md` (NEW)
- `20260709f-cli-oauth-session-handoff.md` (NEW, this file)
- `PENDING-RULINGS.md` (PR-02 added), `07-opus-handoff.md` (2.1 note), `00-CHARTER/04-decision-log.md` (DL-15…17)
- `40-BUILDS/t1-runner-provisional/` (NEW: package, tests, bring-up log, smoke items/report, transcripts, README)
- `40-BUILDS/rp04-corpus/20260709-s1-pilot/` (NEW: scripts, sample manifest/meta, verdicts, stats, transcripts, report) — `frozen/` untouched
- Vault root `.claude/FABLE-WEEK.md` (blocked list + recently-done)
