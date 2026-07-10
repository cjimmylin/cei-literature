# WALKWORTHY run harness

<!-- WALKWORTHY-CANARY-7f3e2026 -->

Manifest-driven runner for the WALKWORTHY family of 10 Christian-ethics
values-alignment benchmarks. Built in **Session O2** (mock-first; no live model
calls until O3). Authority: `00-PORTFOLIO/20260706-master-plan.md` §2 (build spec) &
§3 (frozen gates); the normative charter; the item playbook.

## Golden rules baked in

- **PUBLIC split only.** The loader HARD-REFUSES any `HOLDOUT/` path
  (`HoldoutAccessError`, charter §6.6). HOLDOUT is contamination/perturbation use only.
- **Manifest = IDs only.** Item text is loaded from the versioned seed files at call
  time; the manifest never stores prompt text. Permutation seeds are FIXED constants.
- **No live calls in O2.** Vendor adapters refuse loudly without an API key; only
  `MockModelClient` / `MockJudge` run this session.
- **Never silently average judges.** Two cross-family judges; disagreement is logged
  per cell with both values + `needs_adjudication`.

## Layout

```
walkworthy/
  models.py       Item / Administration / Turn — the normalized core all designs map to
  parsing.py      Markdown block splitter + **Label:** field extractor + yaml
  builders.py     10 per-design builders (RawItem -> Item); the messy format knowledge
  loader.py       load_design / load_public_split; HOLDOUT guard; runnable flag
  clients.py      ModelClient + deterministic MockModelClient + vendor adapter stubs
  manifest.py     Manifest schema + build_manifest (cross-family judge guard, fixed seeds)
  capability_battery.py   the pinned §3.3 battery (6 benchmarks / 3 classes)
  executors.py    single-turn / scripted multi-turn (branch tables) / paired isolation
  refusal.py      four-way refusal taxonomy (detect + tag)
  parsers.py      strict 05 allocation-block parser + one-retry rule
  rubrics.py      per-design ScoringSpec (spec §4 categories + scales + unit)
  judges.py       rubric-prompt assembly + 2 cross-family judges + disagreement analysis
  gates.py        the 10 §3 pre-registered gates (structurally complete)
  schemas.py      scored-item + design-report output validators
  run.py          end-to-end pipeline + mock dry-run driver + CLI
  cli_backends.py     O3 subscription-CLI SUT backends (smoke-only, ToS)
  live_judges.py      CLIJudge + judge-backed 02/07 state classifier (client-agnostic)
  smoke.py            O3 mechanics-smoke driver (1 item/design slice)
  openrouter_backend.py   MEASUREMENT-path client — every vendor via one OpenRouter key
  panel.py            O4-prep multi-model PANEL runner (fan-out + resume + cost)
tests/            157 pytest tests (TDD throughout)
```

## Run the mock dry-run

From `harness/` (package on path):

```bash
PYTHONPATH=. python -m walkworthy.run --benchmark-root .. --out ../runs/<panel>
```

Flags:

| flag | meaning |
|------|---------|
| `--benchmark-root PATH` | benchmark root (has `DESIGNS/`); default = parent of `harness/` |
| `--out PATH` | output dir; default `runs/<panel>/` |
| `--date YYYYMMDD` | panel date (default today) |
| `--panel NAME` | panel name (default `<date>-mock-dryrun`) |
| `--max-items-per-design N` | cap items/design (fast smoke) |
| `--no-records` | skip the (large) `scored_items.jsonl` |

Artifacts: `manifest.json`, `dry_run_report.md` (the transcript), `design_summaries.json`
(committed), and `scored_items.jsonl` (gitignored — regenerable, one record per item×model).

## Tests

```bash
cd harness && python -m pytest tests/ -q      # 157 passing (recorded-transport; no live call)
```

## Auth: API keys OR OAuth CLI (both supported)

Adapters resolve credentials from a **key or an OAuth path** — not key-only:

| vendor | key | OAuth path |
|--------|-----|------------|
| Anthropic | `ANTHROPIC_API_KEY` / `ANTHROPIC_AUTH_TOKEN` | `ant auth login` — the SDK resolves the profile automatically; a bare `anthropic.Anthropic()` hits the raw `/v1/messages` API (same clean call as a key, NOT Claude-Code-wrapped) |
| OpenAI | `OPENAI_API_KEY` | Codex OAuth CLI on PATH ([[vault-no-live-llm-runner]]) |
| Google | `GOOGLE_API_KEY` | Application Default Credentials |

`_KeyedAdapter._auth_available()` treats any of these as "authenticated". OAuth gives
Claude + GPT = the two cross-family judges the charter needs.

**Benchmark-validity caveats (real, not blockers):**
- OAuth = subscription credentials; fine for the **O3 pilot** (3 models, small), but for a
  long **O4 panel** (thousands of calls/hours) prefer keys/WIF — env-var OAuth tokens aren't
  auto-refreshed and rate-limit harder. The ≥6-model panel across more vendors (Gemini, …)
  will still want keys.
- **Do not send `temperature`/`top_p`/`top_k` to Opus 4.7+/Fable** — they 400 (adaptive
  thinking only). Control depth with `output_config.effort`; pin decoding via prompt, not
  sampling params.

## O3 wiring — DONE (2026-07-09, subscription-CLI mechanics smoke)

The O3 *live wiring* landed via **subscription CLIs** (no API key / SDK), distinct from the
still-deferred keyed SDK adapters. New modules:

- `cli_backends.py` — `ClaudeCLIClient` (`claude -p`, family anthropic) + `CodexCLIClient`
  (`codex exec --ignore-user-config --output-last-message`, family openai). Injectable
  subprocess `runner` → recorded-transcript tests, never a live call. No temperature/top_p/top_k.
- `live_judges.py` — `CLIJudge(Judge)` (one model call per scoring unit → tolerant JSON
  verdict parse → option coercion, defects logged not guessed) + `make_cli_state_classifier`
  (judge-backed 02/07 branch selection, heuristic fallback). Drop-in for `judge_item`'s
  cross-family + no-average guarantees.
- `smoke.py` — `run_smoke` reuses the client-agnostic pipeline; `python -m walkworthy.smoke`
  runs the live 4-family slice.

Run the mechanics smoke (LIVE subscription-CLI calls — smoke-only, ToS):

```bash
PYTHONPATH=. python -m walkworthy.smoke --benchmark-root ..            # 4-family slice
PYTHONPATH=. python -m walkworthy.smoke --benchmark-root .. --designs 01-goodsamaritan  # canary
```

Result of the 2026-07-09 run: `runs/20260709-o3-smoke/` + `00-PORTFOLIO/20260709-O3-smoke-report.md`
(0 schema/parse/classifier defects; findings M-1→PR-3 refusal semantics, M-3 09/06 references).

## Measurement path — OpenRouter (DONE) + the PANEL runner (O4-prep, 2026-07-09)

The measurement backend is **OpenRouter** — a real paid developer API reaching every
vendor through **one key** (`openrouter_backend.OpenRouterClient`). This SUPERSEDES the
old "sanctioned API on both vendors" requirement: cross-vendor SUTs + cross-family judges
route through a single credential, with native multi-turn (fixes O3 M-4) and real per-call
`usage.cost`. The subscription-CLI backends remain **smoke-only** (ToS). The keyed SDK
adapters in `clients.py` are now moot for measurement (OpenRouter covers all vendors).

`panel.py` generalizes the smoke driver to the full `items × models` panel — the **§1 P0
pilot** and the O4 panel:

```bash
# P0 pilot: 3 cross-vendor SUTs × 5 items/design × all 10 designs
PYTHONPATH=. python -m walkworthy.panel \
  --sut-models "meta-llama/llama-3.1-8b-instruct,qwen/qwen-2.5-72b-instruct,mistralai/mistral-large-2512" \
  --judge1-model openai/gpt-5.6-terra --judge2-model google/gemini-3.5-flash \
  --classifier-model openai/gpt-5.6-terra --items-per-design 5 --panel <date>-p0-pilot

# full O4 panel: drop --items-per-design (0/omit → all 344 runnable public items)
```

What the runner adds on top of the (unchanged) per-item pipeline:
- **Deterministic selection** (`select_panel_items`) — first N items/design by id, so the
  subset is reproducible from the manifest's IDs.
- **Per-(item, model) checkpoint + RESUME** — `scored_items.jsonl` IS the checkpoint; a
  killed run re-reads it, skips completed cells, and continues (no re-calling, no dup).
- **Cost tracking** — each item's real `usage.cost` delta is stored on its record
  (`_panel_cost`); run + per-model totals sum from records (resume-safe). Key never logged.

Artifacts: `manifest.json` (subset IDs only) + `panel_summary.json` (cells + spread +
judge-pair + cost) committed; `scored_items.jsonl` gitignored/regenerable.

**A pilot's numbers are DESCRIPTIVE / PRE-GATE.** Still gating a *credible* large-scale run:
1. ~60-item/design **human labels** for the §3.4 judge-validity gate (the long pole —
   the pilot's cross-family judge divergence makes this more urgent, not less).
2. Matched-quality **reference answers** for the `reference_anchored` designs (06/09) — M-3.
3. **PR-3 ruling** — refusal tag + keyed-outcome are taken from `verdicts[0]` (judge[0]-
   dependent under disagreement); derive from the *adjudicated* value instead.
4. Panel decisions (which ≥6 SUTs; which judges — validate first; pilot→panel sequencing).

PUBLIC-only + IDs-only + fixed-seed + no-average rules unchanged throughout.
