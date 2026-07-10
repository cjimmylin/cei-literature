# WCF-Bench — Next-Session Boot Prompt (Opus build; paste after /model opus + /clear)

Continue WCF-Bench (scope-locked to `COOKBOOK/40-BIBLEBENCH/WCF-Benchmark/`). You are
the Opus build session executing the binding Fable memo
`20260710h-fable-probe-stability-adjudication-memo.md` (R34–R37). Read, in order:
(1) that memo; (2) session-11 handoff `20260710g-wcf-session-handoff.md`;
(3) `04-HARNESS/README.md` if present. Mock-first/TDD; suite currently 326 green
(`../.venv/bin/python -m pytest COOKBOOK/40-BIBLEBENCH/WCF-Benchmark/04-HARNESS/tests/ -q`
from `CEI-Lit-WS/`). 0 network in tests.

## Ordered queue

1. **R35 gating build (mock-first):**
   - Route all five acceptance probes through the R33.3 retry semantics
     (retry once on `finish_reason ∈ {length, error}` or short-emission; post-retry
     failure = failed rep with recorded cause `pass|fail_substantive|fail_format|
     fail_transport_after_retry`).
   - K=8 reps per probe; surface gate = ≥5/8 reps pass; tolerance stays 1;
     `patterns_differ` stays per-rep.
   - **Qualification manifest**: probes write a dated manifest (run dir, template
     hashes, slugs, pass table, eligible-surface sets); `JudgePanel` CONSUMES a
     manifest instead of re-running probes at construction; re-qualification only on
     slug change / relevant template-hash change / memo order. The provisional
     manifest of record is `07-PILOTS/20260710-probe-stability/` (gemini → all four
     surfaces; gpt → coherence+settled-core only; both mistral slugs discarded).
2. **R36 third-family screen (live, cheap):** extend/reuse
   `04-HARNESS/probe_stability.py` (fix its `???` report renderer first — R37.2,
   new runs only, do NOT regenerate the existing report); screen `cohere/command-r`
   class, then `x-ai/grok` fast tier, then `amazon/nova` class (validate slugs live
   against `/api/v1/models`; family ∉ {openai, google, anthropic}). Wire the first
   candidate reaching ≥5/8 on disclosure (ideally also OPEN award). Do NOT wire a
   non-qualifier. Mistral fast-mid tier is exhausted (R36.2) — don't retry it.
3. **Floor re-run:** re-run the 6-item slice (post settled-core prompt fix) with the
   manifest-driven panel → NEW dated dir under `07-PILOTS/` + NEW dated report.
   Confirm the R31 12/12 settled-core floor holds; report whether disclosure/OPEN
   award gained a second family. Numbers stay DESCRIPTIVE; if still single-family on
   a surface, label it single-family (R34.4).
4. **Earlier-wave transcription ~161→230** (unchanged protocol — session-11 handoff
   §3 + `05-BANK-YAML/TRANSCRIPTION-SPEC.md`): 10-agent Sonnet fan-out, axis-tag OPEN
   rubrics at transcription, `AGG-C7-007` contested:true, `LIB-C7-008` +
   `LIB-C3-W202` dev_set_only:true, grep-verify EVERY anchor (OCR wraps + injected
   proof-letters — grep short fragments; WLC Q1–113 against
   `LargerCatechismwithScriptureProofs1 copy.txt`, NOT `03-LCLayout2 copy.txt`).
   Fidelity spot-check after. Do not rush this at session end — it is
   fabrication-sensitive; defer again rather than truncate it.
5. End with a dated handoff + update the `wcf-bench-portfolio-state` memory note.

## Guardrails (hook-enforced)

Report immutability (new dated files; pilot dirs append-only, never re-scored — incl.
the `???` report, which stays as-is). NEVER rm/delete — `mv` to `RECYCLE-BIN/`.
Canary `WCFBENCH-CANARY-c1647-x9k4q` not re-minted. No G6 run (Jimmy recruits raters).
Shared git index LIVE: `git log -1` before every commit, stage explicit paths only,
never `git add -A`. Secrets: `source ~/.codex/secrets/openrouter.env` at runtime,
never committed. Live calls: OpenRouter is the sanctioned path (Jimmy ruling);
subagents get an explicit `model=` per Fable-week protocol (moot after ~2026-07-11).

## Still Jimmy-blocked (unchanged)

G6 confessional panel (gates the gated G1–G7 run, H-DISC promotion, W304/W305
position maps, 4 LIB `[DISPUTED]` legs). H-DISC additionally needs R30 condition 6 +
R34.4 (≥2 valid families per scored surface) — item 2 above is the unblocking path.
