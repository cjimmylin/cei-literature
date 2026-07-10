# WCF-Bench — Next-Session Boot Prompt (FABLE adjudication — paste to start)

> **Model: FABLE main loop** (`/model fable`). This is the one session that is Fable-tier:
> **judge-calibration go/no-go + adjudicating the live pilot's judge-disagreement clusters**
> — validity judgment that would silently corrupt the measurement if wrong. Do it **before
> the Fable window closes (~2026-07-11)**. This session produces RULINGS + a memo, not code.
> Delegate any search/extraction to Sonnet/Haiku subagents with an explicit `model=`. The
> Opus build session already produced the data you adjudicate.

> **Scope lock: WCF-Bench ONLY.** Stay inside `CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/WCF-Benchmark/`.
> The shared git index is LIVE (`git log -1` before every commit; explicit paths; never
> `git add -A`). Do NOT touch WALKWORTHY / INNOVATION / sibling benches. Do NOT relitigate
> R1–R23, the contested-item scoring ruling, or the OpenRouter sanctioned-path ruling.

---

Continue WCF-Bench. **First — read, in order:**
1. Memory note `wcf-bench-portfolio-state`.
2. **`20260710-wcf-session-handoff.md`** (session 7 — what was built + the two findings).
3. **`20260710-open-contested-pilot-report.md`** — the live pilot; §5 (disagreement clusters,
   worst-first) and §6 (what Fable adjudicates) are your queue. Raw per-judge data:
   `07-PILOTS/20260710-open-contested/disagreement.json`.
4. `20260709-contested-item-scoring-ruling.md` — the binding ruling the scorer now implements
   (do not relitigate; you may confirm it fired correctly).

**Current state (true as of commit `674a9ad1c`, 240 pytest green):** the contested-item scorer
split + the OPEN triaxial judge panel + the position/coherence scorer + client robustness + the
disagreement summarizer are all built, mock-tested, and **validated on a live OpenRouter pilot**
(judges gpt-4o-mini + gemini-2.5-flash, SUTs llama-3.1-8b + deepseek-chat). OpenRouter is the
sanctioned path. The pilot is DESCRIPTIVE / pre-gate (tiny n).

**Your adjudication queue (produces a dated binding memo — no code):**

1. **Judge-calibration go/no-go.** G4 passed both judges (0 discards). But the pilot surfaced
   **F-1: judges score triaxial axes inconsistently (0..1 vs 0..2 rubric points)** despite the
   instruction — so raw OPEN cross-judge spread conflates scale-disagreement with substance. **Rule
   the fix path** for the next Opus build: (a) pin the scale harder in the prompt, (b) switch
   triaxial to per-keypoint award scoring (compute the axis fraction mechanically, like the
   contested settled-core — most robust), or (c) accept 0..1-clamped headlines + report per-judge
   raw. This is a validity call that governs every OPEN number, hence Fable.

2. **The disagreement clusters.** The one *substantive* cluster is **`AGG-C5-W304 · llama`** — the
   judges split on whether llama's familial-honor reading is a **defensible Reformed position**
   (gpt-4o-mini) or a **Q151 misapplication** (gemini, coherence 0.2). Adjudicate: is this a
   position the G6 `positions:` map should legitimize, or a genuine coherence failure? (Note: this
   feeds the **G6 remit** — do NOT elect a single gold; the ruling forbids it. Decide whether it is
   "genuinely contested → position-scored" or "settled → the answer is simply wrong.") The OPEN
   spreads are mostly F-1 artifact — re-judge after the scale fix rather than adjudicate now.

3. **F-2 (disclosure-low).** Across both SUTs/judges, models rarely disclose the contestedness
   (disclosure mostly 0.0–0.5). Rule whether this is a scale-worthy **headline construct** before
   the measurement design commits to it — and whether the disclosure axis needs its own calibration
   (a judge that scores disclosure high for a confident single-answer would invert it).

**Then hand back to Opus** (a later build session) with: the F-1 scale-fix spec, the perturbation-
variant materialization order (feeds the position scorer's invariance leg + the flip-rate engine),
the earlier-wave transcription (~161 → 230; mark `AGG-C7-007`/R1 `contested: true`, `LIB-C7-008` +
`LIB-C3-W202` `dev_set_only`), anchor grep-verification, then scale toward the gated G1–G7 run.

**Do NOT:** run the G6 panel (Jimmy recruits raters; instrument + aggregation DONE); relitigate any
frozen ruling; mint a single gold for a contested item; touch a sibling bench.

**Hard rules:** Westminster texts in `../WCF/` are the only normative source. Report immutability
(new dated memo). Frozen surfaces change only via `[NEEDS-RULING]`. Secrets sourced not committed.
Shared index LIVE (`git log -1` + explicit paths). Canary `WCFBENCH-CANARY-c1647-x9k4q` not
re-minted. End with a dated memo + atomic commit + push.
