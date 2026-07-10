# 20260709 — Paste-ready boot prompt: FABLE adversarial review of the DUPLEX-P0 Session-A rebuild

> Start the session with the Fable model (`/model fable`), then paste everything below the line.
> This is a **judgment session** (validity audit of the fork-deciding P0 gate implementation) — the
> highest-value Fable use before the ~2026-07-11 window closes. After 07-11 this review drops to Opus.

---

You are Fable, reviewing the **DUPLEX-P0 runner/analysis rebuild** completed by an Opus session on
2026-07-09 (roadmap Session A). The rebuild fixed all 10 WS-1 §1 code↔spec divergences; a
non-building Opus auditor already ran an A1/A2 pass and caught one relocated-D10 bug (now fixed).
Your job is the **higher-tier validity sign-off before the first real P0 run**: ratify or overturn
the interpretation choices the builder made (they gate the P0 pass/fail), and confirm the gate
estimands are faithful. **Do NOT re-do the mechanical A1/A2 line-audit** (Opus did it) — spend your
tokens on the judgment calls a wrong answer would silently corrupt.

**Staleness guard first:** run `git log -1` and confirm the latest `COOKBOOK/2026*handoff*.md` is the
`20260709-duplex-p0-session-a-*` one; a later session may have moved `main`.

**Read yourself (small, load-bearing):** `DUPLEX-P0/20260709-ws1-checklist-evidence.md` (the
per-item table + the "interpretation choices ratified" and "run flags" sections),
`DUPLEX-P0/20260706-p0-adjudication-protocol.md` (rulings G1-a/G1-b/G3-a/V-4/§5.x), and
`REVIEWS/20260706-p0-item-bank-adversarial-read.md` (IB-1a/IB-2/IB-3a/IB-5). Do NOT read the ~1,500
lines of runner/analysis code into your context — **dispatch Opus subagents** (explicit
`model: "opus"`) to verify specific fidelity claims against the code and return only verdicts +
short quotes. Keep the adjudication in your main loop.

**Adjudicate these (each gates the fork — issue a BINDING ratify / overturn+fix ruling per item):**

1. **G1 aggregation choice.** The builder implemented G1-a's "cross-model CV of per-item condition-
   deltas" as: per-model signature = mean over items of |per-item delta|, then CV across models
   (preserving the pre-existing per-model→CV architecture). The alternative is per-item CV-across-
   models, then average over items. Does the chosen aggregation faithfully realize "content
   disagreement between models" / "resource-driven shift", or can it wash out per-item signal? Rule.
2. **G1 content baseline** = per-model mean of standard-condition stance over items, then cross-model
   CV. Same aggregation question: does averaging standard stance over items before the CV lose
   per-item content disagreement? Rule (this is the denominator of the fork-deciding ratio).
3. **Frame rendering (D8/X3).** The builder re-applies the bank builder's monitored-prepend /
   unmonitored-embed wrappers to EACH resource-condition prompt at runtime (5×2), since the bank
   pre-rendered them on the base only. Is this faithful to the design's factorial intent, and does
   the unmonitored naturalistic embed clash with e.g. forced_immediate's "16 tokens" instruction
   (README/IB flagged a register clash)? Rule on whether the runtime wrapper is acceptable or needs
   per-condition hand-tuning before the real run.
4. **G3 fallback contrast.** Fallback direction = sign(mean(extended_thinking) − mean(greene_fallback
   arm)) per item, within each frame, ≥4/5 both frames. The prereg defines Δ = deliberation −
   speeded+load; the builder substitutes the greene_fallback (agent-patient+time-pressure) arm for
   the speeded pole. Ratify that greene_fallback is the correct "intuitive/speeded" pole for the
   contrast, or correct it.
5. **D10 fix.** Refusal_flag now = structured signal only (Anthropic `stop_reason=='refusal'`, Codex
   `returncode!=0`); content refusal = scorer-returns-None. Is Codex `returncode!=0` the right
   structured signal (does it conflate administration errors with refusals — should errored calls
   raise/retry instead of scoring as refusals)? Rule.
6. **UNMEASURABLE detection (V-4).** A cell is coded UNMEASURABLE iff SD≈0 AND its condition is in a
   caller-supplied `unmeasurable_conditions` set. Is a condition-name flag the right mechanism, or
   should it key on the per-record temperature actually used? Rule.
7. **M030 pole-collapse** is detected by the substring `"M030"` in `item_id`. Confirm the run bank's
   Greene item IDs literally contain `M030`, or specify a robust key.

Also: spot-check (via an Opus subagent) that no NEW test asserts the code's behavior rather than the
spec's sentence, and confirm the operator run-flags gap (no run entrypoint wires
`frames`/`administer_greene_fallback`/`strict_prompts`) — decide whether wiring+testing that
entrypoint is a run precondition you make binding.

**Deliverable:** a dated binding memo `DUPLEX-P0/20260709-fable-session-a-review.md` — per-item
rulings (ratify / overturn+fix), a verdict on each interpretation choice, confirmation of the D10
fix, and an overall **GO / CONDITIONAL-GO (with the specific fixes) / FIXES-REQUIRED** call on
whether the runner is validity-cleared for a real P0 run. Anything you overturn becomes an Opus fix
task (PR-NN memo style). If credentials have landed and you'd rather spend the window on the live P0
branch call instead, say so and pivot (exit memo §2.4: P0 branch call is the top discretionary use).

**Discipline:** model tiering per `~/.claude/CLAUDE.md` — delegate all code-reading/verification to
Opus subagents with explicit `model`, keep judgment in the main loop, `/clear` afterward. Git:
parallel sessions share the index — path-scoped staging, commit promptly, never `git add -A`,
`git log -1` before committing. Do NOT relitigate frozen rulings (2026-07-05 memo, CS-1…5, IB-1…5,
PS-1…6) — scrutinize the builder's NEW implementation choices only. End with a dated handoff +
memory update ([[cookbook-project-state]]).
