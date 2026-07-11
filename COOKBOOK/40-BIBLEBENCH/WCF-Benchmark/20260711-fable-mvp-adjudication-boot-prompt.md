# WCF-Bench — Next-Session Boot Prompt (Fable adjudication of the MVP run; paste after /model fable + /clear)

Continue WCF-Bench (scope-locked to `COOKBOOK/40-BIBLEBENCH/WCF-Benchmark/`). You are a
**Fable adjudication session** (judgment only — NO code, NO live runs; like sessions 8/10/12/14).
Session 15 (Fable-orchestrated multi-agent build-out, handoff `20260710m` incl. §6b addendum)
completed the ENTIRE MVP critical path: bank 230/230 (audited GO), R40 + R39(d) executed,
`run_mvp.py` built, and the **first full-bank descriptive run finished 816/816 cells, 0 errors**
(`07-PILOTS/20260710-mvp-run/`). This session is the payoff read + two pending rulings. Read, in order:

1. `20260710m-wcf-session-handoff.md` — §6b (run completion, readings, disclosures) + §6 queue.
2. `07-PILOTS/20260710-mvp-run/20260710-mvp-run-report.md` — the full descriptive report.
3. `20260710-fable-grok-ratification-floor-divergence-memo.md` (R38–R41) — governing memo;
   R39(e) floor semantics apply to everything you read.
4. Evidence: `07-PILOTS/20260710-mvp-run/disagreement.json` (worst-first cell spreads; covers the
   **309 transcript-backed cells** — session-1 judge texts were lost to a since-fixed clobber,
   disclosed in-report) + `transcripts.jsonl` (full SUT responses + verbatim judge verdicts for
   those cells). Adjudicate at the sample level from persisted text; do NOT re-run models.

## The questions to rule (write a BINDING memo `20260711-fable-<slug>-memo.md`, R42+)

**Q1 — First cross-SUT disagreement read.** From `disagreement.json`, take the worst-spread
cells (suggest: top ~10 by max_spread + every `split_defensible` cell). For each, read the SUT
response + all verdict texts and rule in the R29/R31 mode: judge error (overrule, with evidence),
defensible strict/lenient split (record, no overrule), or genuine model-behavior finding. The
meta-question: is the panel's disagreement profile HEALTHY post-requal, or is there a new
systematic bias (like the gemini decline-penalty R39(d) caught)? Any systematic finding →
directive for a probe/gloss in the R30/R39(d) pattern.

**Q2 — gpt-4o-mini: drop or keep?** After the R39(d) requal it is coherence-only (OPEN award
suspended R34; disclosure suspended R30; settled-core lost 0/8). Its MVP-run raw verdicts include
the known deterministic harmless-error (seen fenced-out on the re-sampled AGG-C3 cell). Rule:
keep as a third coherence reader (redundancy value?), or drop to a clean gemini+grok panel and
name coherence's second/third family need. Consider judge cost/complexity vs information added.

**Q3 — OPEN-award second family: authorize the format-bridge?** R36.4's candidate ladder is
EXHAUSTED (mistral fast-mid tier out R36; cohere/command-a + amazon/nova-pro failed the K=8
OPEN-award gate in `07-PILOTS/20260710-settled-requal/`). The remaining path is the R36.4
format-bridge: few-shot exemplar in the award prompt — a template change ⇒ new hashes ⇒ **full
re-qualification of ALL judges on ALL surfaces** (R35.4). Rule: authorize (with conditions —
e.g. exemplar must be from a non-bank item; re-qual battery scope; which candidates to re-screen)
or defer and ship single-family-labeled OPEN numbers until after G6. Cost context: ~$30 remains
on the key; a full re-qual + 2-candidate re-screen ≈ $3–8.

**Q4 — Directives for the next Opus build (direct, don't build):** (a) PROOFTEXT scorer upgrade
to the judge-assisted correct-use path (`judge_score_anchor_use` exists) — the citation-token
scorer floors PROOF at 0.03–0.34 across all SUTs, an artifact not a finding; set acceptance
criteria. (b) EPISODE live runs for the 22 NARROWGATE items via `episode_live.py`. (c) Cost
estimator fix (known ≈10× undercount vs key-side accounting — pricing lookup gaps; the --budget
cap currently guards the estimate, not true spend).

## Guardrails

Adjudication only — no code, no live calls, no gold minted, no item edited, no G6 activity.
Report immutability (new dated memo; all `07-PILOTS/` dirs append-only, never re-scored; the two
PARTIAL reports in the mvp-run dir are preserved history). Canary `WCFBENCH-CANARY-c1647-x9k4q`
not re-minted. Shared git index LIVE (`git log -1` before every commit; explicit paths; never
`git add -A`). Secrets not needed (no live calls).

## After the ruling

Update the `wcf-bench-portfolio-state` memory note + write the next re-entry pointer (Opus build:
Q4 directives + any Q3-authorized re-qual). After this session, WCF-Bench's remaining queue is
entirely Opus-executable or Jimmy-blocked (G6 raters) — the Fable window can close with nothing
stranded.

> Fallback: if the Fable window has lapsed, run this same boot on Opus but DOWNGRADE Q1–Q3 to
> descriptive cataloging + recommendations (no binding rulings, no overrules) — flag them for a
> future judgment pass.
