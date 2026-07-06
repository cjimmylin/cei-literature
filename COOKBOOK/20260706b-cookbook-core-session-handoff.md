# 20260706b — COOKBOOK Core (non-BibleBench) Session Handoff

**Session model:** Opus 4.8 (xhigh). **Predecessor:** `20260706-cookbook-core-next-session-handoff.md`
(the prioritized queue this session executed). **Scope:** the cookbook proper (00/10/20/30 +
vault-fix leftovers). BibleBench untouched (its own handoff chain).

## What this session did

Jimmy authorized working the **whole queue** in parallel, with two scoping calls:
**OpenAI via the OAuth Codex CLI** (no API key) and **Google/Gemini deferred**; and the DUPLEX
P0 runner **built fresh inside COOKBOOK** (no sibling-project coupling). Six background
subagents (tiered: 1 Sonnet, 5 Opus) ran the delegable work; CRUX (the shared engine) was built
in the main loop test-first.

### Material finding that reshaped item 1 (DUPLEX P0)
The handoff named the MORAL-PSYCH harness as the reuse target for the 9-model×3-vendor P0 run.
**It is not a live runner** — MP's `TRIALS/` data is synthetic (Opus JSON copied + string-
substituted per model with deterministic score tweaks; consistent with the existing MP
"self-administration disclosure"). There is **no central LLM runner** in the vault; every
sub-project re-wires vendor calls. Only the Anthropic SDK is installed (no OpenAI/Google SDK, no
`.env`). So P0 **cannot run autonomously** — it needs credentials (OpenAI Codex-OAuth + a later
Google decision) and a **human mini-norm for gate G3**. Item 1 was therefore executed as
**prep-only** (items + fresh runner + pre-registered analysis), which is the correct build-ahead
state.

## Per-item results

### ✅ Item 2 — CRUX engine (shared infrastructure) — DONE, committed `f4f53cb17`
`COOKBOOK/ENGINE/` — the fractional-factorial generator + portfolio-wide X2 shortcut-audit
tooling per revised `20-DESIGNS/06 §3.1/§4`, built **TDD (33 passing tests)**. Modules:
`values` (5 Schwartz-anchored values), `factorial` (1,440-cell grid → balanced ≤60-cell fraction
with published confounding), `generator` (causal-graph scenarios, matched triads, minimal pairs),
`shortcut_audit` (lexical baseline proven to *catch* a leaky set + fine-tune-probe interface),
`pilot` (reusable `publish_spec` + `build_pilot_instances` + CLI). Reused by designs 01/05.
Run: `cd COOKBOOK/ENGINE && ../../../.venv/bin/python -m pytest -q`. Limitations documented in
`ENGINE/README.md` (randomized-balanced fraction vs a true OA; probe trainer is a P3 stub).

### ✅ Item 3 — long-pole drafts for 02/04/05 — DONE, committed `9480912aa`
`COOKBOOK/20-DESIGNS/20260706-02-frameshift-subvariant-sheets.md` (9 framework sheets + virtue
gap), `...-04-intra-board-charters-and-rater-protocol.md` (C2 authoring/validation firewall),
`...-05-cultivate-codesign-brief-and-annotator-spec.md` (C4 1-locale+1-diaspora). Each subordinate
to its locked spec + adjudication memo; each has a documented-assumptions section. **Needs a human
review pass before use; expert/community recruitment is Jimmy's.**

### ✅ Item 5 — vault-fix leftovers — DONE, committed `28754233e`
- **Gemini Safety** → arXiv **2403.13793** "Evaluating Frontier Models for Dangerous Capabilities"
  (Phuong et al., GDM). **CONFIRMED** — ready for PDF/extract replacement on Jimmy's OK.
- **Simple Probes Detect Sycophancy** → **still blocked / double error**: the candidate blog post
  "Simple probes can catch sleeper agents" is about *sleeper agents, not sycophancy*; the stem
  conflates two topics. Needs Jimmy to decide the intended source before any replacement.
- **CCAI→Sycophancy card stem-rename**: card renamed + all living citations updated; orchestrator
  pass fixed 7 annotated-form citations the script missed and reverted the 2026-07-05 spot-check
  report to preserve it as an immutable audit snapshot. Log: `logs/20260706-vault-data-fixes-followup.md`.
  Low-priority leftover: a `...2310.13548v2` near-match entry in `ailabs-listing.json` (flagged, not merged).

### ✅ Item 1 — DUPLEX P0 prep — DONE (prep-only), committed `49e03a21d`
- **1a items — DONE.** `COOKBOOK/20-DESIGNS/DUPLEX-P0/items/` — **65 items** (48 novel moral over a
  balanced 4×2×3×2 factorial + 5 labeled contamination probes + 12 non-moral discriminant controls),
  each with 5 resource-condition variants × monitored/unmonitored frames, per-item canaries, Greene
  subset + fallbacks. JSON-validated. Reproducible via `build_p0_item_bank.py`.
- **1b runner + analysis — DONE** (**48 passing tests**, TDD, all API access mocked, no live calls;
  independently re-verified). `COOKBOOK/20-DESIGNS/DUPLEX-P0/{runner,analysis,tests,config}`:
  vendor-neutral `administer()`; Anthropic SDK adapter + OpenAI Codex-OAuth subprocess adapter +
  Gemini `NotImplementedError` (deferred); orchestrator (≥10 reps, temp>0, seeded, idempotent
  checkpointing, refusal category, per-condition SD); cross-vendor-only judge assignment +
  neutrality meta-eval; pre-registered gates G1 (denominator-guarded CV), G2 (KB04 §6.2 pairwise
  separation + outlier guard), G3 (Greene direction / M3 fallback), `run_p0_gates` (all-three);
  X2 lexical baseline + fine-tune-probe interface. Roster: 5 subjects enabled (Anthropic ×3,
  OpenAI ×2), Gemini ×4 disabled. See `runner/README.md` for the run checklist.

## Open items needing Jimmy (decisions / inputs)

1. **DUPLEX P0 is credential-blocked**, not built-blocked. To run it:
   (a) OpenAI **Codex CLI is present (0.134.0)** but must be OAuth-authenticated + its `codex exec`
   flags verified to force a single-turn answer (it's agentic, no temp/seed flags);
   (b) `ANTHROPIC_API_KEY` exported (+ verify temp/adaptive-thinking accepted on 4.6);
   (c) a **decision on Google** (deferred now — P0's cross-vendor claim wants all 3 vendors);
   (d) a **P0 human mini-norm** for gate G3 (small controlled cognitive experiment, not autonomous);
   (e) **⚠ Haiku 3.5 is RETIRED (2026-02-19)** — and it is the exact model whose single unreplicated
   MP-DP effect *motivates DUPLEX's whole discrimination premise*. Decide a substitute
   (`claude-haiku-4-5`) vs pinning a legacy snapshot **before** running; note the original effect may
   not reproduce on a successor model, which itself bears on the P0 branch call.
   **P0 pass/fail adjudication is Fable-tier** if results land before ~2026-07-11; else Opus applies
   the pre-registered thresholds mechanically.
2. **Vault sources** (item 5): OK to replace the Gemini Safety PDF/extract with arXiv 2403.13793? And
   decide the intended "Simple Probes / Sycophancy" source (the stem is a conflation).
3. The design drafts (02/04/05) and the P0 item bank warrant a **human read-through** before any spend.

## Next steps (suggested queue)
- If credentials become available: wire the Codex-OAuth adapter's exact CLI flags + run P0 on the
  filtered items (P1.5-style dead-cell prune first), then bring results to Fable for the branch call
  (P0 pass → DUPLEX generator build; fail → CRUX takes build-first — the CRUX engine is already built).
- CRUX can proceed to its own P1 (generator already done) whenever Jimmy greenlights the validation
  survey; the shortcut-audit gate is ready to wire a real fine-tune trainer at P3.
- Optional Fable insurance spot-check of the six revised designs (predecessor handoff item 4) still open.

## Standing cautions (carried over)
- Four sub-project disclosures whenever their numbers appear (NormEval F1–F7 elicited; MP self-
  administration; RV same-vendor; CG N_eff≈3.4). Digest statistics copied verbatim, never recomputed.
- Concurrent-session git hazard: shared index — check `git log -1`, stage+commit atomically (done this
  session as path-scoped commits). Safety rules hook-enforced (no rm → RECYCLE-BIN; new dated reports).
- Adjudication memo (`20-DESIGNS/REVIEWS/20260705-adjudication-memo.md`) is binding — gate rulings not
  relitigated.
