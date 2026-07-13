# WCF-Bench PPP-1 Zero-Paid Preflight Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Freeze an exact, reproducible PPP-1 roster/call/cost/runtime packet from two authorized OpenRouter metadata GETs, without inference or spend.

**Architecture:** Add one PPP-1-specific controller that reuses the already-tested T4 metadata, pricing, call-weight, cap, runtime, canary, and secret-detection helpers without reading or changing the immutable T4 packet. The controller fixes the ratified three-SUT/one-judge roster, computes only 226 base-item calls, emits five new immutable artifacts, and stops for owner ratification if the conservative minimum cap exceeds the proposed $5 ceiling.

**Tech Stack:** Python 3.9, pytest, existing `wcfbench` loaders and `t4_preflight` pure helpers, OpenRouter `/api/v1/auth/key` and `/api/v1/models` GET metadata.

---

## Task 1: RED — PPP-1 contract tests

**Files:**
- Create: `04-HARNESS/tests/test_ppp1_preflight.py`

- [x] Add a dry-mode test proving no metadata or artifact seam is touched.
- [x] Add a call-geometry test asserting 226 runnable items, 226 SUT calls per model,
  348 single-judge calls per model, 678 SUT calls, 1,044 judge calls, and 1,722 total.
- [x] Add an injected-metadata test asserting the exact ratified roster, five artifact
  names, current-price calculation, runtime fields, secret exclusion, and no completion URL.
- [x] Add a budget-branch test asserting monotonically cheaper judge caps
  `2048 → 1024 → 512 → 256 → 0`, with the zero-completion row marked non-executable.
- [x] Add an exclusive-write test asserting an existing output directory fails before any
  artifact changes and a credential string cannot be persisted.
- [x] Run:
  `/Users/jimmy.lin/Documents/CEI-Literature-Vault/.venv/bin/python -m pytest tests/test_ppp1_preflight.py -q`
  and verify failure because `ppp1_preflight` does not exist.

**Required test-facing API:** constants `PPP1_SUTS` and `PPP1_JUDGE`; pure functions
`build_call_plan(items)`, `build_budget_branches(classes, catalog, token_profiles)`, and
`build_preflight_payloads(token_profiles, metadata)`; exclusive writer
`write_new_artifacts(output_dir, payloads, forbidden_values=())`; and injected-seam CLI
`main(argv, metadata_fetch, artifact_writer)`.

**Done when:** the focused suite fails for the missing PPP-1 module, not for a malformed test.

## Task 2: GREEN — minimal metadata-only controller

**Files:**
- Create: `04-HARNESS/ppp1_preflight.py`
- Read only: `04-HARNESS/t4_preflight.py`
- Read only: `20260713h-t4-preflight-source-inputs.json`

- [x] Define the exact frozen roster, sole judge, validity label, five artifact names, and
  proposed `$5.00` strategy ceiling.
- [x] Reuse `t4_preflight.fetch_openrouter_metadata`; do not define any POST or completion
  endpoint.
- [x] Load all frozen bank items, exclude only `dev_set_only`, fail unless there are 226,
  and derive the single-judge weight with `t4_preflight._per_judge_call_weight`.
- [x] Build exactly these six request rows:

```python
for sut in PPP1_SUTS:
    classes.append({"role": "sut", "model": sut, "sut_context": sut,
                    "request_class": "base_sut", "count": 226})
    classes.append({"role": "judge", "model": PPP1_JUDGE, "sut_context": sut,
                    "request_class": "base_judge", "count": 348})
```

- [x] Reuse `t4_preflight.estimate_cost`, `minimum_ratifiable_cap`,
  `required_top_up`, and `forecast_runtime` with only the frozen `base_sut` and
  `base_judge` profiles.
- [x] Produce executable judge-cap branches for 2048, 1024, 512, and 256 completion
  tokens plus a non-executable zero-completion price floor. Do not select a branch.
- [x] Fail loudly if any exact slug is absent, any price is absent/nonpositive, or any
  model lacks text input/output or `response_format` support. Record, but do not
  reinterpret, each catalog row's declared `max_tokens` support.
- [x] Build exactly:
  `auth-snapshot.json`, `openrouter-catalog-snapshot.json`,
  `ppp1-run-manifest.json`, `ppp1-cost-plan.csv`, and
  `ppp1-preflight-report.md`.
- [x] Write exclusively into a nonexistent output directory; include the provenance
  canary; reject API-key fields, authorization fields, `sk-or-v1-`, or the runtime key.
- [x] Run the focused suite and verify all tests pass.

**Done when:** the pure controller passes its focused tests and has no inference endpoint.

## Task 3: Authorized two-GET metadata freeze

**Files:**
- Create directory exclusively: `07-PILOTS/20260713-ppp1-zero-paid-preflight/`
- Create through controller only: the five artifacts listed above

- [x] Confirm the output directory does not exist.
- [x] Source `~/.codex/secrets/openrouter.env` without echoing the key.
- [x] Execute the controller once with `--metadata-preflight`, the frozen T4 source-input
  file for its reviewed base token profiles, and the new output directory.
- [x] Verify the only network boundary was one GET to `/api/v1/auth/key` and one GET to
  `/api/v1/models`; no inference endpoint exists in the controller.
- [x] Verify the four exact slugs, current per-token prices, catalog timestamp/hash,
  balance, 1,722 calls, forecast, minimum cap, top-up, runtime, and all truncation rows.
- [x] If the minimum cap exceeds `$5.00`, mark `strategy_cap_feasible: false`, append one
  owner question to `PENDING-QUESTIONS.md`, and stop before paid execution.

**Done when:** a new immutable metadata packet exists and exposes the exact owner decision.

## Task 4: Verification and close

**Files:**
- Create: `20260713m-codex-session38-ppp1-zero-paid-preflight-handoff.md`
- Modify: `project-dashboard.html` live surfaces and append-only S38/log rows
- Modify: `../ACTIVE-CRITICAL-PATHS.md` WCF section only if the exact cap changes its blocker
- Modify: `../project-dashboard.html` WCF card only
- Modify: `PENDING-QUESTIONS.md` only if the `$5` cap is infeasible

- [x] Run focused tests, then the full offline harness.
- [x] Verify artifact count, JSON/CSV readability, manifest arithmetic, secret absence,
  no completion URL, and `$0` spend.
- [x] Record exact models, calls, prices, forecast, cap, balance/top-up, runtime, and branch
  feasibility in the handoff and dashboards.
- [x] Rewrite the local next-session block to stop for paid-run ratification or budget
  adjudication; include the mandatory dashboard open/close lines.
- [x] Source-verify the dashboard under the established local-file browser exception.
- [x] Run `git log -1`, stage only isolated PPP-1 paths/hunks, commit, and fast-forward push.

**Done when:** the zero-paid packet is reproducible, the owner decision is explicit, all
tests pass, no inference/spend occurred, and unrelated concurrent changes remain untouched.

## Post-verification correction — actual retry geometry

- [x] Preserve the original five-artifact metadata packet unchanged.
- [x] Reproduce the review failure showing the blanket 3,444-attempt reserve does not
  match the production runner/scorer retry seams.
- [x] Derive 1,722 initial and 3,624 maximum API attempts from the frozen item geometry
  and existing normal, EPISODE, OPEN, and CONTESTED paths.
- [x] Add the zero-network offline correction mode and two focused regression tests.
- [x] Freeze the three-file append-only correction packet at
  `07-PILOTS/20260713-ppp1-zero-paid-preflight-retry-correction/`.
- [x] Freeze the three-file zero-network branch addendum at
  `07-PILOTS/20260713-ppp1-zero-paid-preflight-branch-addendum/`, labeling original
  branch figures logical-call-only and recording each maximum-retry envelope.
- [x] Propagate the distinct logical forecast and maximum-retry NTE cap through the owner
  question, dashboards, handoff, final verification, and commit.
