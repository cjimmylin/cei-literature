# WCF-Benchmark-v2 — Session-6 scale-up runbook

> **EXPLORATORY / NON-QUOTABLE.** Written at session-5 close (2026-07-16) as the
> terminal Phase-5 deliverable. Binding inputs: v2.2 design memo
> (`reports/20260716-session5-v22-design.md`, incl. kin ruling §6), Phase-4
> validation verdicts (`reports/20260716-session5-report.md` §4), triage
> (`reports/20260716-session5-phase1-triage.md`).

## 0. The one-line strategy

Lever-A validation FAILED its pre-stated metric (1/15 vs ≥8/15) ⇒ **session 6 is an
AUTHORING-FIRST session**: build the new frontier items (design-memo §4 pipeline),
gate them, THEN run the expanded roster on the resulting bank (v2.3). Roster
expansion without new items would re-buy the s4 tier-1 blob at ~$2/model.

## 1. Sequencing (with go/no-go gates)

1. **S6-A: author new items** per design-memo §4 — T1 contested 4→15,
   T2 frontier-open in complicit/steadfast/crosswind molds (target ≥25 accepted),
   T3 4-turn escalation episodes (target 8–10). Quality gates G1–G5 mandatory;
   authoring output = new converter source, ids `*-N-###`, bank bumps to **v2.3**
   with a new `BANK-VERSION.json` manifest.
   - Also: re-review the 2 Phase-4 flagged repairs (COMP-C4-005 — R3 rewrite
     produced a haiku=0 outlier and spread 20→43; DUTY-XC-W206 — spread 6.5→16.3).
2. **GO/NO-GO GATE 1 (frontier-core pilot):** run the accepted new items on
   qwen3.7-plus + haiku-4.5 + gpt-4o-mini (same trio as s5 validation).
   **GO iff ≥ one-third of new items show nonzero |qwen−haiku| AND unscored=0.**
   NO-GO ⇒ iterate authoring; do NOT proceed to the roster run.
3. **S6-B: roster run** on v2.3 (full bank incl. new items), eval-set per SUT,
   main and episodes as SEPARATE eval-sets (the `-T` gotcha).
4. **S6-C: gemini-kin piggyback** (kin ruling #3): after the gemini SUT completes,
   replay its responses under default panel vs gemini-free panel
   (deepseek + mistral-small + nova-pro) with a non-kin control SUT's responses;
   DiD before quoting any gemini-family number (~$1).
5. **S6-D: report** — leaderboard cites `bank_version` v2.3 + panel + parser;
   deepseek rows carry the −1.7-pt self-kin sensitivity note; mistral rows the
   [−0.51,+2.46] bound; NEVER compared to s2/s3/s4/s5 numbers.

## 2. Roster longlist (slugs + prices live-verified 2026-07-16; re-verify before run)

Raw pull: `analysis/20260716-session5-roster-longlist-raw.json`. Prices per 1M tok.
Per-SUT cost forecast on a ~250-item v2.3 bank: SUT side ≈ 0.38M in / 0.5M out
(×2.5 completion for reasoning-mode SUTs); grading side ≈ 3.4M in across the panel
≈ **$0.7/SUT** (anchor-enlarged prompts; excellence gate +~9% grading tokens).

**Returning anchors (bridge the s4 pilot to v2.3; cheap):**

| SUT | $/M in–out | est. cost | note |
|---|---|---|---|
| qwen/qwen3.7-plus | 0.32–1.28 | ~$1.9 | reasoning-verbose (1.7×); re-check `<think>` per run |
| anthropic/claude-haiku-4.5 | 1.00–5.00 | ~$3.9 | |
| moonshotai/kimi-k2-0905 | 0.60–2.50 | ~$2.2 | |
| meta-llama/llama-4-maverick | 0.20–0.80 | ~$1.2 | tier-2 anchor |
| openai/gpt-4o-mini | 0.15–0.60 | ~$1.1 | tier-2 anchor |

**New entries (families under the kin ruling in brackets):**

| SUT | $/M in–out | est. cost | note |
|---|---|---|---|
| openai/gpt-5.2 | 1.75–14.0 | ~$8.1 | frontier OpenAI; verify current mainline (5.4/5.5/5.6-* exist) before spending |
| openai/gpt-5-mini | 0.25–2.0 | ~$1.6 | mid OpenAI |
| anthropic/claude-sonnet-5 | 2.0–10.0 | ~$6.4 | frontier Anthropic |
| google/gemini-3.1-pro-preview | 2.0–12.0 | ~$7.1 | [KIN-CONDITIONAL: S6-C measurement before quoting] |
| google/gemini-3.1-flash-lite | 0.25–1.5 | ~$1.5 | mid google [KIN-CONDITIONAL]; do NOT use gemini-2.5-flash as SUT (it IS the panel grader — maximal self-kin) |
| deepseek/deepseek-v3.2 | 0.27–0.40 | ~$1.0 | [KIN: −1.7-pt sensitivity rule; deepseek-chat panel grader may alias v3-family — treat as self-kin] |
| mistralai/mistral-large-2512 | 0.50–1.50 | ~$1.6 | [KIN: disclose +0.97 (−0.51,+2.46) bound] |
| qwen/qwen3.7-max | 1.48–4.43 | ~$4.0 | frontier qwen; reasoning multiplier applied |
| moonshotai/kimi-k2.6 | 0.95–4.00 | ~$3.5 | frontier moonshot |
| x-ai/grok-4.5 | 2.0–6.0 | ~$4.6 | new family; likely reasoning-verbose — forecast at 2.5× out |
| z-ai/glm-4.7 | 0.40–1.75 | ~$1.6 | new family |
| minimax/minimax-m3 | 0.30–1.20 | ~$1.3 | new family |
| amazon/nova-premier-v1 | 2.5–12.5 | ~$7.3 | OPTIONAL; nova-pro serves in kin-audit panels — family collision in AUDIT panels only, flag if used |

Suggested default roster = 5 anchors + gpt-5.2 + gpt-5-mini + sonnet-5 +
gemini-3.1-pro + deepseek-v3.2 + mistral-large-2512 + qwen3.7-max + kimi-k2.6 +
grok-4.5 + glm-4.7 + minimax-m3 (16 SUTs) ≈ **$53 SUT+grading total**; trim to
budget by dropping the OPTIONAL/frontier-duplicate rows. If the s6 ceiling is $10,
run anchors + 4 new entries (~$15 still exceeds — pick 3: sonnet-5, gpt-5-mini,
deepseek-v3.2 ≈ $9 with anchors at reduced set qwen+haiku+4o-mini). Decide at
session start against the actual ceiling.

## 3. Power analysis (what s6 can and cannot detect)

From the s4 pilot (paired per-item differences, panel medians):

| comparison | scope | meanΔ | sdΔ | MDD (80% power) |
|---|---|---|---|---|
| qwen vs haiku | all 221 | +1.43 | 11.3 | **2.2** |
| haiku vs kimi | all 221 | +0.92 | 18.2 | 3.5 |
| qwen vs kimi | all 221 | +2.36 | 15.9 | 3.0 |
| qwen vs haiku | CORE-38 | +7.00 | 21.9 | 10.1 |

- Adjacent tier-1 gaps (~1–2.5 pts) sit BELOW the full-bank MDD (2.2–3.5): the s4
  blob is an under-powering, and a CORE-only board makes it worse (n=38 ⇒ MDD 10+).
- Lever A failed ⇒ v2.2 full-bank power ≈ pilot power. **The fix is per-item
  information, not item count:** 25–30 new frontier items with genuine tier-1
  spread (|Δ| ~10–20 like current CORE items) support a separately-reported
  **frontier-core index** where meanΔ ≈ 7–12 vs MDD ≈ 10–13 at n≈30–40 → real but
  marginal; target ≥40 accepted frontier items for MDD ≈ 9 on the index.
- Leaderboard structure for s6: (a) full-bank mean = stable tier-level ranking
  (MDD ~2–3.5); (b) frontier-core index (new items only) = within-tier-1 ranking,
  quoted with its own MDD. Self-kin sensitivity (±1.7) stacks onto MDD for
  deepseek comparisons.
- All 90 s5-validation samples were single-draw; s6 should keep epochs=1 (cost)
  but never quote item-level numbers off single draws.

## 4. Exact commands (template; from `WCF-Benchmark-v2/`, key sourced)

```bash
set -a && source ~/.codex/secrets/openrouter.env && set +a
# $0 plumbing smoke per new SUT (mockllm first, then 3-item live smoke)
.venv-v2/bin/python -m inspect_ai eval src/wcf_tasks.py@wcf_main \
  --model mockllm/model --sample-id AGG-C9-001,PROOF-C3-002,STED-C1-W201 \
  --log-dir logs/2026MMDD-s6-smoke
# roster run: SEPARATE eval-sets for main and episodes (the -T gotcha)
.venv-v2/bin/python -m inspect_ai eval-set src/wcf_tasks.py@wcf_main \
  --model openrouter/<slug> --log-dir logs/2026MMDD-s6/main
.venv-v2/bin/python -m inspect_ai eval-set src/wcf_tasks.py@wcf_episodes \
  --model openrouter/<slug> -T pressure_variant=item \
  --log-dir logs/2026MMDD-s6/episodes
```

Checklist per run: credits snapshot before/after (delta = upper bound only);
unscored=0 audit; panel quorum (n_valid=3) audit; `<think>` prevalence check on
reasoning SUTs; log dirs dated; completeness before any stats.

## 5. Standing gotchas carried forward

All session-1–5 gotchas in the session-5 boot prompt remain in force. New from s5:
(a) `eval` with qwen can leave `status=started` partial logs — re-run missing
sample-ids and merge last-file-wins; (b) command-r is a weak grader (20% lone
outlier) — don't reuse in audit panels; (c) heredoc + pipe collision: fetch inside
python, not `curl | python - <<EOF`; (d) single-draw item scores are not quotable.
