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
tests/            86 pytest tests (TDD throughout)
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
cd harness && python -m pytest tests/ -q      # 86 passing
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

## O3 wiring (next session, needs a credential — key OR OAuth)

1. Implement the SDK call in `clients.AnthropicAdapter` / `OpenAIAdapter` / `GoogleAdapter`
   `.complete()` (they currently raise until wired). For Anthropic, a bare
   `anthropic.Anthropic()` picks up either a key or the `ant` OAuth profile.
2. Add real judge subclasses of `judges.Judge` that call a model and parse the JSON verdict
   (the rubric prompt is already assembled by `assemble_rubric_prompt`).
3. Replace `executors.default_state_classifier` with a judge-backed branch classifier for
   02/07.
4. Provide `.env` with keys, or run the OAuth login (both gitignored/local). Keep the
   PUBLIC-only + IDs-only + no-average rules.
```
