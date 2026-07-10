# WCF-Bench — Next-Session Boot Prompt (Fable adjudication; paste after /model fable + /clear)

Continue WCF-Bench (scope-locked to `COOKBOOK/40-BIBLEBENCH/WCF-Benchmark/`). You are a
**Fable adjudication session** (judgment only — NO code, like sessions 8/10/12). The
session-13 Opus build (handoff `20260710j-wcf-session-handoff.md`) executed R35–R37 and
its live runs surfaced a Fable-trigger divergence — the exact contingency the session-12
memo reserved a Fable pass for. Read, in order:

1. `20260710j-wcf-session-handoff.md` — **§2 (R36 screen), §3 (floor re-run), §4 (the three
   questions Q1–Q3)** are the whole agenda.
2. The binding predecessor memo `20260710h-fable-probe-stability-adjudication-memo.md`
   (R34–R37) — the governing prior adjudication (R34.4 = ≥2 valid families per scored
   surface; R30 condition 6 = ≥2 disclosure-valid families for H-DISC).
3. Evidence on disk (the R27 transcript payoff — adjudicate at the sample level from
   persisted text, as session 10 did; do NOT re-run models):
   - `07-PILOTS/20260710-third-family-screen/20260710-third-family-screen-report.md` +
     `20260710-third-family-manifest.json` — grok-4.20's K=8 pass table (disclosure 8/8).
   - `07-PILOTS/20260710-floor-rerun/disagreement.json` (per-judge settled-core verdicts) +
     `transcripts.jsonl` (full SUT responses + every judge's verdict texts) +
     `20260710-floor-rerun-report.md`. The load-bearing cell is **`AGG-C8-W305 × llama`**.
   - For context on grok's disclosure qualification: the negative-disclosure probe fixture is
     the real AGG-C5-W304 item (`04-HARNESS/wcfbench/probe_fixtures.py`).

## The three questions to rule (write a BINDING memo `20260710-fable-<slug>-memo.md`, R38+)

**Q1 — Ratify `x-ai/grok-4.20` as the valid SECOND disclosure family?** It passed the K=8
gate cleanly (G4 8/8, disclosure-inversion 8/8, negative-disclosure 8/8 — incl. the
real-item negative probe; zero variance) and is correctly excluded from OPEN award
(award-consistency + discrimination fail). Caveat: one live `JSONDecodeError` drop on
AGG-C8-W305×llama (occasional, not systematic — it graded AGG-C3/C5 cleanly). If ratified,
**R30 condition 6 is met on the judge side** and H-DISC's only remaining block is G6 (Jimmy).
Rule whether the probe evidence suffices, or whether a robustness condition (parse-retry /
a second live confirmation) attaches.

**Q2 — Does the settled-core floor "hold" post-fix?** The session-11 prompt fix works (no
uniform 0.0 collapse: AGG-C3=1.0, AGG-C5=0.5, gpt credits AGG-C8 1.0). But the AGG-C8-W305×
llama aggregate is 0.0 because of a **substantive gpt(1.0)-vs-gemini(0.0) divergence** with
grok (the tie-breaker) dropped. Read llama's actual response + both verdict texts and rule:
is **gemini's reading correct** — llama's *"the Q151 calculus does not yield a confident
ordering … both involve significant moral wrongness"* is a collapse-to-'both equal' + wrong
calculus (Q151 not Q152) → **core genuinely FAILED, 0.0 is right, floor = credit-when-earned**
— or **gpt's** (declining a confident order = the settled core → 1.0)? This defines what the
"R31 12/12 floor" criterion means going forward (aggregate vs per-judge; whether a weak-SUT
genuine miss counts against the floor). This is the headline validity call.

**Q3 — Direct the operational re-run.** deepseek's entire contested arm 403'd (transient
provider issue; WHOLE-C9-W301 also hit transport errors). Direct a PR-5-style provider-pin +
empty-retry clean re-run of the 6-item slice (with the combined manifest) so the deepseek
contested arm and grok's AGG-C8 parse are not transport-starved, before any gated reading.

## Guardrails

Adjudication only — no code, no gold minted, no item edited, no G6 run. Report immutability
(new dated memo; the `20260710-third-family-screen/` + `20260710-floor-rerun/` dirs are
append-only, never re-scored). Canary `WCFBENCH-CANARY-c1647-x9k4q` not re-minted. Shared git
index LIVE (`git log -1` before every commit; explicit paths; never `git add -A`). Secrets
sourced at runtime, never committed. If a re-run is directed (Q3), it is the NEXT Opus
session's job, not this one's.

## After the ruling

Update the `wcf-bench-portfolio-state` memory note + write the next re-entry pointer. If Q1/Q2
rule clean, WCF-Bench has **nothing model-blocked left** — the remainder (G6 raters, the gated
G1–G7 run, earlier-wave transcription ~161→230) is Jimmy-blocked or deferred, not Fable-tier.
