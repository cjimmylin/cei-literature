# NormEval Trial Prompt Sourcing Report

**Date:** 2026-04-13 (Day 1 of submission sprint)
**Action Item:** A7 (Prompt Release Supplement) — Anthropic-only scope
**Status:** READ-ONLY investigation complete
**Scope note:** Cross-vendor (GPT-5 / Gemini) sourcing is PAUSED per the 2026-04-12 environment constraint; only Anthropic-administered trials (Opus / Sonnet / Haiku) are audited here.

---

## Summary

**Anthropic prompt-archive completeness: PARTIAL — sufficient for an honest, caveated Appendix K release, but not sufficient for bit-exact replication.**

The NormEval trial archive preserves **items verbatim** for 10 of 15 trials (T6–T15) and **partially** for T1–T5 (5–10 representative items each in the paper's Appendix C; full per-trial narratives also survive in `STATISTICS/20260403-trial-T*.md`). All 70+ per-trial JSON outputs record model IDs, administration dates, response schemas, and item-level responses.

However, three categories of prompt material were **never archived in machine-readable form**:

1. **System prompt text.** Opus trials inherited the "full CEI project system prompt" active at administration time (recoverable via `git log` on root `CLAUDE.md`). Sonnet/Haiku trials ran under a separate "standardized assessment-only prompt" whose exact wording was never saved.
2. **Per-trial assessment prompt text.** Every trial JSON records `"administration_method": "Claude Code agent, standardized prompt"` but none stores the prompt string. The closest surviving artifact is a three-sentence prose description at `20260404c-normeval-session8-methods.md:24-26`.
3. **Decoding parameters.** No temperature, top-p, or seed is recorded per trial. The `seed=42` mentioned in Appendix C is a Python `random.sample()` seed used for T1 item selection — **not** a decoder seed. Sub-agent spawning via Claude Code's `model=` parameter override does not expose temperature controls to the caller, so temperature is implicitly the Claude Code sub-agent default (effectively 0 / greedy for most tool-using agents, but not confirmed in writing).

**Verdict:** Appendix K can be assembled for Anthropic-only trials using (a) a `git`-recovered Opus system prompt, (b) a clearly labelled post-hoc reconstruction of the Sonnet/Haiku standardized prompt, and (c) an explicit gaps disclosure. Bit-exact replication is **not possible** and the paper must say so.

---

## Per-Trial Inventory (T1–T15)

Legend:
- **System Prompt** / **Assessment Prompt**: NOT ARCHIVED unless otherwise noted.
- **Items Preserved**: VERBATIM (full list in STATISTICS/), PARTIAL (subset in appendix-C), or NONE.
- **Recoverable?**: what can be reconstructed from on-disk artifacts alone.

| Trial | Benchmark | Model(s) Administered | System Prompt | Assessment Prompt | Items Preserved | Recoverable? | Source File(s) |
|-------|-----------|------------------------|---------------|-------------------|-----------------|--------------|----------------|
| T1 | ETHICS (Hendrycks 2021) | Opus | NOT ARCHIVED (inherited full CEI project CLAUDE.md) | NOT ARCHIVED | PARTIAL (10 of 50 in appendix-C, Table S3; full narrative in `20260403-trial-T1-ethics.md`) | System prompt via `git log` on root CLAUDE.md; assessment prompt: reconstruction only | `STATISTICS/20260403-trial-T1-ethics.md`, `PAPER-v2/supplement/appendix-C-trials-T1-T5.md` |
| T2 | MoReBench-Theory (Chiu 2025) | Opus | NOT ARCHIVED | NOT ARCHIVED | PARTIAL (6–10 of 30 in appendix-C, Table S4) | As above | `STATISTICS/20260403-trial-T2-morebench.md`, `PAPER-v2/supplement/appendix-C-trials-T1-T5.md` |
| T3 | MoralReason-QA | Opus | NOT ARCHIVED | NOT ARCHIVED | PARTIAL (appendix-C Table S5) | As above | `STATISTICS/20260403-trial-T3-moralreason.md` |
| T4 | MoralLens | Opus | NOT ARCHIVED | NOT ARCHIVED | PARTIAL (appendix-C Table S6) | As above | `STATISTICS/20260403-trial-T4-morallens.md` |
| T5 | DailyDilemmas | Opus | NOT ARCHIVED | NOT ARCHIVED | PARTIAL (appendix-C Table S7) | As above | `STATISTICS/20260403-trial-T5-dailydilemmas.md` |
| T6 | PrinciplismQA | Opus, Sonnet, Haiku | NOT ARCHIVED | NOT ARCHIVED | PARTIAL items in trial narrative (12 of 30 individually documented; Sonnet/Haiku replication limited to those 12 per `20260404c-normeval-session8-methods.md:8`) | Items: partial; prompts: reconstruction only | `STATISTICS/20260404-trial-T6-principlismqa.md`, per-model JSONs |
| T7 | Moral Persuasion | Opus, Sonnet, Haiku | NOT ARCHIVED | NOT ARCHIVED | VERBATIM (items in trial narrative + JSONs) | Prompts: reconstruction only | `STATISTICS/20260404-trial-T7-moralpersuasion.md` |
| T8 | AMAeval | Opus, Sonnet, Haiku | NOT ARCHIVED | NOT ARCHIVED | VERBATIM | Prompts: reconstruction only | `STATISTICS/20260404-trial-T8-amaeval.md` |
| T9 | JETHICS (Japanese) | Opus, Sonnet, Haiku | NOT ARCHIVED | NOT ARCHIVED | VERBATIM (Japanese text preserved) | Prompts: reconstruction only | `STATISTICS/20260404-trial-T9-jethics.md` |
| T10 | Pluralistic Moral Gap | Opus, Sonnet, Haiku | NOT ARCHIVED | NOT ARCHIVED | VERBATIM | Prompts: reconstruction only | `STATISTICS/20260404-trial-T10-pluralisticmoralgap.md` |
| T11 | MedEthicsQA | Opus, Sonnet, Haiku | NOT ARCHIVED | NOT ARCHIVED | VERBATIM | Prompts: reconstruction only | `STATISTICS/20260404-trial-T11-medethicsqa.md` |
| T12 | UniMoral | Opus, Sonnet, Haiku | NOT ARCHIVED | NOT ARCHIVED | VERBATIM | Prompts: reconstruction only | `STATISTICS/20260404-trial-T12-unimoral.md` |
| T13 | Greatest Good Benchmark (OUS) | Opus, Sonnet, Haiku | NOT ARCHIVED | NOT ARCHIVED | VERBATIM (Likert item text) | Prompts: reconstruction only | `STATISTICS/20260404-trial-T13-greatestgood.md` |
| T14 | PNAS Cognitive Biases | Opus, Sonnet, Haiku | NOT ARCHIVED | NOT ARCHIVED | VERBATIM (22 of 22 items individually documented) | Prompts: reconstruction only | `STATISTICS/20260404-trial-T14-cognitivebiases.md` |
| T15 | ProMoralBench | Opus, Sonnet, Haiku | NOT ARCHIVED | NOT ARCHIVED | VERBATIM | Prompts: reconstruction only | `STATISTICS/20260404-trial-T15-promoralbench.md` |

**Coverage pattern (from `20260404c-normeval-session8-methods.md:8`):**
- T14: 100% individually documented (22/22)
- T6: ~40% individually documented (12/30) — worst case among replicated trials
- T1–T5: not cross-model replicated because each had fewer than 8 individually documented items

---

## Anthropic-Only Recovery Plan

For Opus / Sonnet / Haiku trials only (cross-vendor paused per 2026-04-12 constraint):

### 1. Opus system prompt (recoverable via git)

Run at vault root:

```bash
git log --all --follow -- CLAUDE.md
git log --all --follow -- CEI-Lit-WS/CLAUDE.md
```

Identify the commit(s) that bracket the 2026-04-03 / 2026-04-04 trial window and `git show COMMIT:CLAUDE.md`. Archive the exact text as `Appendix K / K.1 / system_prompt_opus_v1.md` and label with: (a) commit SHA, (b) effective-date range, (c) note that Opus agents inherited this as the enclosing project prompt and that no trial-specific system prompt was set on top of it.

### 2. Sonnet / Haiku standardized assessment prompt (post-hoc reconstruction)

The only surviving description is three sentences at `20260404c-normeval-session8-methods.md:24-26`:

> Each agent received: (1) a standardized assessment prompt specifying the benchmark context, response format requirements (letter selection for MCQ, 1–7 integer for Likert, binary "Right/Wrong" for moral dilemma items), and an instruction to return all responses as a single JSON object. (2) The full item set for that trial, verbatim from the original trial documentation (including Japanese text for T9, Likert item text for T13, scenario descriptions for T14).

Action: draft a *post-hoc reconstruction* of the prompt matching those constraints, clearly label it **"RECONSTRUCTION, not archived original"** in both the appendix header and a standing footnote, and publish it alongside the trial JSONs. Do NOT present it as the administered text.

### 3. Decoder parameters

Document in Appendix K preamble:
- **Temperature / top-p:** Not set at the caller level. Sub-agents were spawned via Claude Code's `model=` override (`model="opus"`, `model="sonnet"`, `model="haiku"`), which does not expose decoder parameters to the parent. Effective temperature is the Claude Code sub-agent default, which is not formally documented; the paper should describe sampling as "Claude Code default sub-agent decoding" and note that this is not deterministic in the bit-exact sense.
- **Seed:** No decoder seed. The `seed=42` in Appendix C refers to `random.sample()` item selection for T1, not sampling.
- **Max tokens / stop sequences:** Not set.

### 4. Item-level data

- T6–T15: rely on `STATISTICS/20260404-trial-T*.md` (verbatim items) plus the per-model JSONs (verbatim responses).
- T1–T5: rely on the representative items tabulated in `PAPER-v2/supplement/appendix-C-trials-T1-T5.md` plus full narratives in `STATISTICS/20260403-trial-T*.md`. The non-tabulated items are described only in aggregate ranges and are not individually recoverable.

---

## Gaps & Honest Disclosure Required

The paper (Appendix K and §6.1 limitations) must acknowledge the following gaps:

1. **No archived system prompt.** Opus ran under the project-level CLAUDE.md (git-recoverable but not captured at administration time); Sonnet/Haiku ran under an unarchived standardized prompt.
2. **No archived assessment prompt.** All published assessment prompts are post-hoc reconstructions consistent with the prose methodology, not the literal strings served to the models.
3. **No decoder parameters logged.** Temperature, top-p, seed, and max-token settings are inherited from Claude Code sub-agent defaults; bit-exact replication is not possible.
4. **T1–T5 items only partially preserved.** 5–10 representative items per trial are individually recoverable; the remainder survive only as aggregated narrative ranges.
5. **T6 items partially preserved.** Only 12 of 30 items were individually documented; Sonnet/Haiku replication was limited to those 12.
6. **No per-call request/response logs.** Only the per-trial summary JSONs and the aggregate trial narratives exist; raw API traces were not retained.
7. **Administration was not blinded or order-randomized beyond single-pass agent spawning.** Documented in session methods files but bears repeating in the sourcing appendix.

These gaps are fundamental to the environment in which the trials were run (Claude Code sub-agents, not an instrumented replication harness) and cannot be closed retroactively for Opus/Sonnet/Haiku. They can, however, be **avoided prospectively** for any future runs by (a) logging the full system+user prompt strings to JSON, (b) capturing per-call metadata, and (c) using a deterministic harness.

---

## Cross-Vendor Items (PAUSED)

Per the 2026-04-12 environment constraint (no non-Anthropic API access in this environment), the GPT-5 / Gemini prompt-sourcing question is paused. Current state:

- `Codex/README.md` and `Codex/prompts/protocol.md` explicitly document that GPT-5 outputs are **"direct agent reasoning in-session, SDK/API usage: none"** — i.e., Claude acting as a Codex agent generating outputs in-context, not real OpenAI API calls. Same pattern for `Codex/mini/` (GPT-5-mini) and any Gemini-labelled artifacts.
- When non-Anthropic runs happen externally:
  - Real prompts will be archived at administration time (both system and assessment, plus decoder parameters).
  - The current Codex outputs should be relabelled in the paper as **"elicited (Claude in-context)"** rather than "administered", matching the elicitation disclosure already present in §6.1.
  - Appendix K will gain a **"Real cross-vendor prompts"** sub-section after external runs land.
- Until then, Appendix K should ship **Anthropic-only** with a standing note that cross-vendor prompt material is pending external runs tracked by sprint items A2 / A8 / A10.

---

## Verdict for A7 Sprint Action

**CAN A7 PROCEED FOR ANTHROPIC-ONLY SCOPE? → YES, with caveats.**

Reasoning:
1. All machine-level outputs (model IDs, responses, per-item scoring) are archived for T6–T15 and partially for T1–T5 — sufficient to publish an item-level appendix.
2. The Opus system prompt is git-recoverable; the Sonnet/Haiku assessment prompt can be honestly published as a post-hoc reconstruction.
3. The missing decoder parameters and unrecoverable raw prompt strings are disclosures the paper already partially makes in §6.1; A7 formalizes them in an appendix rather than introducing new problems.
4. The Anthropic scope is independent of the paused cross-vendor work, so A7 does not block and is not blocked by A2 / A8 / A10.

**Blocker risk for A7 (Anthropic scope): LOW.** The only work required is git recovery, a careful reconstruction draft, and honest gap-disclosure prose. No new experiments, no new data collection.

---

## Recommended Next Step

**Day 4 of sprint — Appendix K skeleton.** Concrete actions:

1. Run `git log --all -- CLAUDE.md` at vault root; capture the commit SHA(s) active during 2026-04-03 / 2026-04-04 and export the `CLAUDE.md` content as `PAPER-v2/supplement/appendix-K/system_prompt_opus_v1.md`.
2. Draft a minimal **reconstructed** Sonnet/Haiku standardized prompt consistent with `20260404c-normeval-session8-methods.md:24-26`, labelled "RECONSTRUCTION — NOT THE ADMINISTERED STRING" in both the header and a standing footnote.
3. Write a preamble documenting (a) decoder parameters gap, (b) item-level coverage by trial, (c) item-preservation status by trial, (d) cross-vendor pending-note.
4. Cross-link Appendix K from §6.1 limitations and from the new Appendix C (T1–T5) header.
5. Leave placeholders for the future cross-vendor sub-section so that the structure is already present when external runs land.

---

## Addendum: Git Recovery Results (2026-04-13)

**Attempted:** `git log --all -- CLAUDE.md` in `CEI-Lit-WS/` repo.

**Result:** The `CEI-Lit-WS/CLAUDE.md` file (last committed `d23eb2463` on 2026-02-21) is a **thin reference file** — it points to the root `CLAUDE.md` for safety rules and vault structure, and covers only sub-project-specific configuration (validation commands, skill references, docs links). It does NOT contain the actual system prompt text that would have been loaded into sub-agent context.

**Root `CLAUDE.md`:** Located at `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CLAUDE.md`. This is the real system prompt with safety rules, API conventions, file operations, and environment constraints. However, the vault root is **NOT a git repository** — there is no version history for the root CLAUDE.md. The current version (loaded in this session's context) is available but we cannot confirm it was identical to the version active during the 2026-04-03/04 trial sessions.

**Conclusion for Appendix K:**
- CEI-Lit-WS/CLAUDE.md: recoverable from git commit `d23eb2463`, but contains only configuration metadata, not the safety rules or project context that shaped sub-agent behavior
- Root CLAUDE.md: current version available but **no git history** — must be published as "current version, believed consistent with trial-period version but not version-controlled at that time"
- Combined, these two files would have been the Opus system context. The actual trial behavior was also shaped by Claude Code's built-in system prompt and any session-specific instructions, neither of which was archived.

**Updated recovery plan:** Save current root CLAUDE.md as `appendix-K/root_claude_md_current.md` with an honest header noting it is the current version, not a confirmed trial-period snapshot.

---

## Source Files Audited

- `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/NORM-ETHICS/METHODS/20260404c-normeval-session8-methods.md` (prose description of standardized prompt; lines 24–26 are the closest surviving artifact)
- `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/NORM-ETHICS/METHODS/20260412-normeval-sprint-tracker.md` (sprint pivot context and A7 scoping)
- `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/NORM-ETHICS/STATISTICS/20260403-trial-T1-ethics.md` (T1 narrative)
- `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/NORM-ETHICS/STATISTICS/20260403-trial-T2-morebench.md` (T2 narrative)
- `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/NORM-ETHICS/STATISTICS/20260403-trial-T3-moralreason.md` (T3 narrative)
- `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/NORM-ETHICS/STATISTICS/20260403-trial-T4-morallens.md` (T4 narrative)
- `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/NORM-ETHICS/STATISTICS/20260403-trial-T5-dailydilemmas.md` (T5 narrative)
- `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/NORM-ETHICS/STATISTICS/20260404-trial-T6-principlismqa.md` through `20260404-trial-T15-promoralbench.md` (T6–T15 verbatim items)
- `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/NORM-ETHICS/PAPER-v2/supplement/appendix-C-trials-T1-T5.md` (T1–T5 representative-item tables S3–S7; seed=42 note)
- `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/NORM-ETHICS/Codex/README.md` (GPT-5 elicitation disclosure — "direct agent reasoning in-session, SDK/API usage: none")
- `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/NORM-ETHICS/Codex/prompts/protocol.md` (Codex protocol)
- `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/NORM-ETHICS/Codex/mini/README.md` (GPT-5-mini, same pattern)
- `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CLAUDE.md` (root project prompt — current version; historical versions recoverable via git log)

---

**Report author:** Claude Code sub-agent, A7 sourcing pass (Day 1)
**Read-only:** no paper files were modified by this investigation.
