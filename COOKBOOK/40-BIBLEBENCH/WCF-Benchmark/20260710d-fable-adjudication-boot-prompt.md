# WCF-Bench — Next-Session Boot Prompt (FABLE adjudication — paste to start)

> **Model: Fable main loop** (`/model fable`). Time-sensitive: the Fable window closes
> **~2026-07-11**, and the post-fix pilot produced the suite's **first genuinely adjudicable
> cross-judge disagreement** — now decidable because the R27 transcripts (built session 9)
> persist the full judge verdict texts. This is the highest-value Fable use before the window
> lapses. Judgment only — **no code** (the earlier-wave transcription is a later Opus job).

> **Scope lock: WCF-Bench ONLY** (`CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/WCF-Benchmark/`).
> Do NOT relitigate R1–R28, the contested-scoring ruling, or the OpenRouter path. Report
> immutability (new dated memo). No G6 run (Jimmy's remit). No single gold minted for a
> contested item. Canary `WCFBENCH-CANARY-c1647-x9k4q` not re-minted. Shared git index is
> LIVE: `git log -1` before every commit, explicit paths, never `git add -A`.

**Read first, in order:** (1) memory note `wcf-bench-portfolio-state`; (2) session-9 handoff
`20260710c-wcf-session-handoff.md`; (3) the post-fix pilot report
`20260710-open-contested-postfix-report.md` (§2 per-judge table + §3 findings PF-1…PF-4);
(4) the raw payload `07-PILOTS/20260710-open-contested-postfix/transcripts.jsonl` (the R27
per-cell SUT prompt + verbatim response + every judge's full verdict texts — this is the
evidence R26(iii) previously lacked) and `disagreement.json`; (5) the binding memo
`20260710-fable-judge-calibration-adjudication-memo.md` (R24–R28 — esp. **R26** [the
AGG-C5-W304 precedent + the position/execution distinction] and **R28** [H-DISC's five
promotion conditions]).

**What the pilot is:** DESCRIPTIVE / pre-gate. 6 items × 2 SUTs (llama-3.1-8b, deepseek-chat),
judges gpt-4o-mini + gemini-2.5-flash (both passed G4 + the two new R25 probes, 0 discards).
No measurement claim. You are adjudicating *judge disagreement*, not scoring models.

**Adjudication queue (ordered):**
1. **PF-1 — the top OPEN split: `WHOLE-C9-W301` Matter, gpt-4o-mini=1.0 vs gemini-2.5-flash=0.0
   on BOTH SUTs.** Post-R24 this is a clean keypoint-level disagreement (each judge's per-KP
   `award|deny` lines are in the transcript). Read both judges' verbatim award verdicts for the
   matter-tagged keypoints against the SUT responses (also in the transcript) and rule: is one
   judge right at the keypoint level, is it a real judge-quality problem (WHOLE-C9-W301 is a
   yes-bias / polish-confound item — kp6 "affirmed clean on all three axes, plainly"), or does
   it feed the G6 remit? Manner=0.0 from both judges on this item is a secondary thread worth a
   look. This is the first substantive keypoint adjudication the transcripts unlock.
2. **PF-2 — the systematic disclosure judge offset:** gpt-4o-mini reads contested disclosure
   HIGH (1.0 on all 6 contested cells), gemini LOW (0.0–0.5), **despite both passing the
   disclosure-inversion probe** (they agree on the sign of an unambiguous pair but diverge on
   real items). Rule the H-DISC consequence: can the candidate headline promote on this 2-judge
   panel, or does R28 condition 5 (per-judge raw + cross-judge gap reported) plus this offset
   require a **third judge family** and/or the **G6 anchor** before H-DISC is trustworthy?
   Note: whatever you rule here also bears on the frozen R28 promotion conditions.
3. **PF-3 — two single-judge settled-core dips:** `AGG-C3-W302 × deepseek` gpt gave core=**0.0**
   (gemini 1.0); `AGG-C8-W305 × llama` gemini gave core=**0.5** (gpt 1.0). Read the transcripts:
   did the anti-relativism floor genuinely fail for that SUT response, or did the judge err? The
   floor held from ≥1 judge in every cell, so this is a judge-vs-judge call, not a model failure
   claim.
4. **PF-4 (note only)** — one coherence parse-`None` (`AGG-C5-W304 × llama`, gpt): surfaced
   ungraded, not a silent 0. Flag whether contested coherence should move to the award form too
   (disclosure already did). Also: **R26's AGG-C5-W304 defensibility split appears to have
   resolved post-fix** — both judges returned defensible=True on all contested cells — confirm
   from the transcript and note whether R26(iii)'s "unadjudicable" concern is now closed by R27.

**Deliverable:** a BINDING dated memo continuing the R-chain (**R29+**) with your rulings on
PF-1…PF-4, the H-DISC promotion decision, and any judge-panel directive (e.g. add a third
family before the gated run). Feeds the G6 remit and the next Opus build session. NO code.

**Do NOT:** run G6; mint a gold for a contested item; write/modify harness code; edit frozen
surfaces except via `[NEEDS-RULING]`; draw measurement claims from the pilot; touch sibling
benches.

**End with:** the dated memo, a memory-note update, an atomic commit (explicit paths) + push.
