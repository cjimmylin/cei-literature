# WCF-Bench — Next-Session Prompt (paste this to start the session)

> **Model choice — read first.** The item bank is now COMPLETE (230 items, 10×10 matrix), but **batch 2 (48 items) has had only Opus review, never a Fable adversarial content pass**, and it ships with a set of self-demoting / `[DISPUTED]` flags queued for higher-tier adjudication.
> - **If you have a Fable session and the window is still open (~2026-07-11): use FABLE, and do the judgment pass — it is the perishable work.** Adversarially review the 48 batch-2 items + adjudicate the queued flags (see Route A). Delegate any code/build down to Opus subagents with an explicit `model=`. Do NOT spend Fable tokens on the harness build.
> - **Otherwise (default): use OPUS** and do the harness build-out (Route B). Opus authored and reviewed batch 2 this session — it's sufficient to keep building; the bank would just ship without an independent Fable adjudication of the flags.
> Recommended sequence if both are available: **Fable (Route A) first, then Opus (Route B).**

---

Continue the WCF-Bench project (Westminster-Standards values-alignment benchmark suite).

**First action — read this, it governs everything and chains to the rest:**
1. `CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/WCF-Benchmark/20260709c-wcf-session-handoff.md` (latest state: batch-2 done → 230 items; harness Phase-2 backbone + CLI-OAuth real backend; the **Addendum** covers the CLI-OAuth adapter; §2 = the consolidated reviewer-visibility flags; §3 = the queue). It sits on `20260709b-` and `20260709-next-session-handoff.md` (standing orientation) — read those next if you need the deeper context.

Then, before writing anything, load in this order:
1. `00-OVERVIEW/20260706-shared-spine.md` (BINDING — tiers, scoring §4, perturbations §5, item schema §10)
2. `00-OVERVIEW/20260706-westminster-anchor-registry.md` (citation rules + the Q1–113 source-split sharp edge)
3. `20260706-fable-review-memo.md` + `20260707-fable-review-addendum.md` (BINDING rulings R1–R7 — do not relitigate)
4. `03-OPUS-GUIDE/20260706-item-authoring-guide.md` (BINDING authoring protocol — only if you touch items)

## Route A — FABLE judgment pass (if window open; the perishable work)
1. **Adversarially review the 48 batch-2 items** in `01-DESIGNS/expansions/20260709-{dutybound,complicit,steadfast,crosswind,liberty,mending,wholeheart}-expansion-2.md`: are the gold keys right, the two-sided controls real, the incomparable/structure-scored keys defensible, the anchors used correctly (not just cited)? Independently spot-grep anchors (Q1–113 via `LargerCatechismwithScriptureProofs1 copy.txt`).
2. **Adjudicate the queued flags** — the consolidated reviewer-visibility / self-demoting list in `20260709c` §2 (notably: LIBERTY `[DISPUTED]` named-parties **LIB-C4-W304c** usury + **LIB-C2-W305b** instruments; MENDING structure-scoring **MEND-C6-W303**; WHOLEHEART matter-vs-manner **WHOLE-C8-W304iii**; the AGGRAVATE-seam MENDING relapse ladder; STEADFAST W302 legitimate-update-toward-permissibility) **plus the 5 batch-1 flags** in `20260709b` §2 (AGG-C3-W302 frequency-vs-formation; AGG-C5-W304/C8-W305 incomparable fallbacks; NARROW-C1-W301 / NARROW-XC-W306 legs).
3. **Issue a new dated review memo** (`20260709-fable-batch2-review-memo.md` or similar) with BINDING rulings, in the R1–R7 style — accept / demote-per-fallback / `[NEEDS-RULING]` / rewrite-order. Do NOT edit the frozen expansion files inline; record rulings + errata in the new memo (report immutability).
4. Push execution (any rewrites the memo orders) to a following Opus session.

## Route B — OPUS harness build-out (default, or after Route A)
Extend `04-HARNESS/` (keep `tests/` green — currently **44 passed**; mock-first stays default), per `20260709c` §3 + `00-OVERVIEW/20260706-build-plan.md`:
1. **Full YAML transcription** of the 10×10 prose banks into spine-§10 records (only 3 fixtures exist — until this lands the tensor's worst-cell / A–B gap aren't meaningful; the tensor input is all Track B). Lint-load with zero schema failures.
2. **NARROWGATE episode state machines** + defect-instructed baseline runner (prove the harness *detects* defection before trusting any null).
3. **Judge-prompt templates** (cross-family, generator-family exclusion, length-corrected, neutrality meta-check) — retire the PROOFTEXT **and** refusal heuristic stubs.
4. **Triaxial Matter/Manner/End** sub-scoring + remaining mechanical scorers (DUTYBOUND Track-A artifact / signal-detection d′; NARROWGATE sent-message).
5. **Cross-family OAuth CLI adapters** (Codex / Gemini) behind the existing `CLIModelClient` seam — needed for the spine's ≥2-judge-family requirement; then a small real cross-family smoke pilot. (A Messages-API client is still needed for the sanctioned bulk run.)

**Hard rules (both routes):** Westminster texts in `../WCF/` are the ONLY normative sources; grep-verify every anchor (Q1–113 via the companion file; OCR wraps clauses + inserts proof-letters between words — grep short 3–6-word fragments). No cross-referencing sibling benches (WALKWORTHY etc.). No deletions (`mv` to RECYCLE-BIN). `[NEEDS-RULING]` for anything a registry clause can't ground — never guess a key. **Shared git index is LIVE** — `git log -1` before committing, stage this project's paths explicitly, never `git add -A`. **CLI-OAuth is smoke-pilot only** — the gated G1–G7 run needs the Messages API (ToS + reproducible params).

**Jimmy-blocked — do NOT attempt:** the sanctioned API path (or Messages-API keys) for the bulk empirical run; the G6 confessional rater panel (gold labels + the LIBERTY named-parties `[DISPUTED]` confirmations + rulings R1/R3/R4); the attorney sanity-check of MEND-C3-W202.

---
