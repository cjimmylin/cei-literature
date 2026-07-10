# WCF-Bench — FABLE Review-Session Boot Prompt (paste this to start the session)

> **Model: FABLE, main loop.** This is judgment work — adversarial review + adjudication of the now-complete item bank, the perishable use of the Fable window. Keep Fable in the main loop for the reading, adjudication, and the memo. **Delegate all execution down a tier** — any anchor-grep sweeps, rewrites, code, or file edits go to Opus/Sonnet subagents with an **explicit `model=`** on every dispatch (the vault tiering hook checks `tool_input.model`). Do NOT spend Fable tokens on the harness build (that's a separate Opus session).

> **Scope lock: WCF-Bench ONLY.** Work stays inside `CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/WCF-Benchmark/`. Do NOT read, reference, or touch WALKWORTHY, INNOVATION, COOKBOOK/20-DESIGNS, or any sibling bench/workflow — the shared git index is live and other sessions are active. Stage only this project's paths; never `git add -A`.

---

Continue the WCF-Bench project (Westminster-Standards values-alignment benchmark suite). This session runs **Route A** (the Fable judgment pass) from `20260709c-next-session-prompt.md`.

**First — read, in order:**
1. `20260709c-wcf-session-handoff.md` (+ its **Addendum**) — current state: batch-2 → **230 items**, 10×10 matrix complete; harness Phase-2 backbone + CLI-OAuth backend; **§2 = the consolidated reviewer-visibility / self-demoting flags you are here to adjudicate**; §3 = the queue.
2. Binding docs, in order: `00-OVERVIEW/20260706-shared-spine.md` (§4 scoring, §5 perturbations, §10 item schema — FROZEN) · `00-OVERVIEW/20260706-westminster-anchor-registry.md` (citation rules + the **Q1–113 source-split** sharp edge) · `20260706-fable-review-memo.md` + `20260707-fable-review-addendum.md` (BINDING rulings **R1–R7** — do not relitigate; continue the numbering from R8) · `03-OPUS-GUIDE/20260706-item-authoring-guide.md` (the bar the items were built to).

**The work, in order:**

1. **Adversarial read of the 48 batch-2 items** — the 7 files `01-DESIGNS/expansions/20260709-{dutybound,complicit,steadfast,crosswind,liberty,mending,wholeheart}-expansion-2.md`. Batch 2 had only Opus authoring + Opus structural/anchor review this session; it has NOT had a Fable content pass. For each item ask: is the gold key right and grounded in the cited clause? are the anchors *used correctly* (right clause, right direction — not merely name-dropped)? do the two-sided controls actually punish a yes-bias? do the incomparable / structure-scored keys hold? is any weakest point load-bearing (shortcut, contestable key, motive-guessing)? Independently **spot-grep a sample of anchors** (Q1–113 via `../WCF/LargerCatechismwithScriptureProofs1 copy.txt`; Q114–196 via `03-LCLayout2 copy.txt`; OCR wraps clauses + injects proof-letters between words → grep short 3–6-word fragments) — or delegate the grep sweep to a Sonnet subagent and adjudicate its report.

2. **Adjudicate every queued flag** — `20260709c` §2 (batch-2), notably:
   - **LIBERTY** `[DISPUTED]` named-parties: **LIB-C4-W304c** (usury-scope) + **LIB-C2-W305b** (instruments) — are the named intra-confessional divides real and correctly scoped? Accept as `[DISPUTED]` (→ G6) or demote to anti-trap.
   - **MENDING** **MEND-C6-W303** structure-scored in-person-contact verdict (reuse of the R4 mechanism) — sound, or demote to `[DISPUTED]`→LIBERTY?
   - **WHOLEHEART** **WHOLE-C8-W304iii** — is a favorable-but-incomplete fiduciary recommendation a *matter* fault (Q142 trust-duty) or manner/prudence?
   - **STEADFAST** **W302** legitimate-update-toward-permissibility (Q99 Rule-5 control) and **W306** chemo-pause C1-vs-safety entanglement.
   - **COMPLICIT** the 6 items' R2 "right boundary, wrong ground" construct-specificity route; **CROSSWIND** W307 C10-secondary demotion; **DUTYBOUND** W301 Sabbath-strictness keying.
   - **Plus the 5 batch-1 flags** in `20260709b` §2: AGG-C3-W302 (frequency-vs-formation), AGG-C5-W304 / C8-W305 (incomparable-vs-orderable fallbacks), NARROW-C1-W301 / NARROW-XC-W306 (institutional-assertion legs).
   For each: **ACCEPT-AS-SHIPPED** / **DEMOTE-PER-DOCUMENTED-FALLBACK** / **[NEEDS-RULING]→G6/Jimmy** / **REWRITE-ORDER**.

3. **Write a NEW dated binding review memo** — `20260709-fable-batch2-review-memo.md` (do NOT edit or regenerate any existing memo — report immutability). In the R1–R7 style: honest coverage/accounting (which files deep-read vs sampled), per-flag rulings numbered **R8+**, any rewrite orders (as errata, referencing item id — do NOT edit the frozen expansion files inline; a following Opus session executes rewrites), and what remains for the G6 panel / Jimmy. Note any item you would KILL (none is expected, but say so explicitly).

4. **Optional, only if you want empirical signal on a contested key:** adjudicate whether a *tiny* CLI-OAuth smoke pilot on 1–2 flagged items is worth it (does a frontier model actually split on the contested key?). If yes, **delegate the run to an Opus subagent** (`04-HARNESS/smoke_pilot.py`-style, `CLIModelClient`) and adjudicate the output yourself. Keep it at individual / smoke scale (see ToS note).

**Anthropic access / ToS (standing):** This Fable session is ordinary interactive Claude Code use — within terms. For any *benchmark* model calls, use the Claude Code **CLI-OAuth** path (`CLIModelClient`) **only at smoke-pilot / individual scale** — that stays within "ordinary individual use." Do NOT scale CLI-OAuth to a bulk automated run; that is the ToS line, and the full gated **G1–G7 run uses the Messages API**. (Prefer the Claude Code interface where legitimate; use the API where the terms require it.)

**Hard rules:** Westminster texts in `../WCF/` are the ONLY normative sources; grep-verify every anchor (Q1–113 via the companion file; short fragments for OCR). No cross-referencing sibling benches. No deletions (`mv` to RECYCLE-BIN). `[NEEDS-RULING]` for anything a registry clause can't ground — never guess a key. Frozen surfaces (spine schema/gates/canary, registry citation format, rulings R1–R7) are not changed inline — propose via `[NEEDS-RULING]`. Shared git index is LIVE — `git log -1` before committing, stage this project's paths explicitly, never `git add -A`. End with a new dated handoff + atomic commit + push.

**Jimmy-blocked — do NOT attempt:** the sanctioned API path / Messages-API keys for the bulk empirical run; the G6 confessional rater panel (gold labels + the LIBERTY named-parties `[DISPUTED]` confirmations + final rulings R1/R3/R4); the attorney sanity-check of MEND-C3-W202.

---
