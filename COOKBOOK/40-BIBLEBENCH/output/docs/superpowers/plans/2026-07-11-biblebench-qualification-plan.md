# BibleBench Cheap Qualification and Freeze Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Qualify the consolidated harness with offline fixtures and four cheap general-purpose models across at least three providers, under a USD 25 hard cap, then permit at most one evidence-supported design revision before freezing the held-out bank.

**Architecture:** Evidence advances through explicit levels: offline contract, authenticated catalog GET, non-bank live smoke, complete cheap diagnostic tranche, human calibration, sealed C3 confirmation, and formal evidence. Each level preserves lower-level engineering evidence but cannot borrow a higher-level claim. The cheap tranche tests transport, mechanical resolution, non-saturation, discrimination, and feasibility; it does not rank models, run formal CORINTHLOVE concordance, or emit the 70/30 composite.

**Exact cheap schedule:** The 12-episode geometry produces 84 calls per model/module; across four modules this is 336 logical calls per model and 1,344 across four models: 192 blind forecasts, 576 C0/C1/C2 primaries, and 576 matched probes. No optional intervention, model judge, C3, private held-out confirmation, provider retry, or frontier call is included. Before authority, the compiled exact token ceilings and fresh catalog prices must prove a worst-case cost no greater than USD 25.

---

### Task 1: Build the complete credential-free Tier-0 vertical slice

**Files:**
- Create: `BIBLEBENCH-PILOT/fixtures/nonbank-smoke.yaml`
- Create: `BIBLEBENCH-PILOT/src/biblebench_pilot/qualification.py`
- Create: `BIBLEBENCH-PILOT/tests/test_tier0.py`

- [ ] **Step 1: Write failing end-to-end fixture tests**

```python
def test_tier0_covers_all_modules_and_failure_states(tier0_result):
    assert set(tier0_result.modules) == {
        "fruitbench", "corinthlove", "tencommandments", "sermonmount"
    }
    assert {"accepted", "refused", "malformed", "truncated", "delivery_unknown"} <= set(tier0_result.states)
    assert tier0_result.evidence_basis == "FIXTURE_ONLY"
    assert tier0_result.authorizes_live_calls is False
```

- [ ] **Step 2: Implement one reusable fixture bundle per module**

Run exact rendering, fake transport, sandbox, response/probe retention,
observable-event coding, lens ballots, native scoring, journal, manifest-last
publication, verification, replay, and report generation. Include all inference
roles even if deterministic in the pilot.

- [ ] **Step 3: Add synthetic recovery organisms**

Create stable, cue-fragile, target-blind, null-overreaching, restraint-failing,
capability-limited, monitoring-aware, mode-discordant, and red-line profiles.
Assert the diagnostic engine recovers the planted signature. Every artifact is
`harness validation, NOT a measurement` and ineligible for empirical, ranking,
composite, or publication claims.

- [ ] **Step 4: Run and commit**

```bash
python3 -m pytest BIBLEBENCH-PILOT/tests/test_tier0.py -q
git log -1 --oneline
git add BIBLEBENCH-PILOT/fixtures/nonbank-smoke.yaml BIBLEBENCH-PILOT/src/biblebench_pilot/qualification.py BIBLEBENCH-PILOT/tests/test_tier0.py
git commit -m "BibleBench: add credential free Tier 0 slice"
```

### Task 2: Freeze separate cheap-screen and formal-panel registries

**Files:**
- Create: `BIBLEBENCH-PILOT/config/panels.yaml`
- Create: `BIBLEBENCH-PILOT/tests/test_panels.py`

- [ ] **Step 1: Test cheap roster requirements**

The cheap screen contains exactly four general-purpose LLMs across at least
three pinned providers. Each row includes alias, allowed returned aliases,
vendor, provider, capability tier, snapshot/version, prompt/config hashes,
numeric cheap ceiling, and `formal_inference:false`. Select exact models only
from a fresh launch-day catalog; example names never authorize dispatch.

- [ ] **Step 2: Test formal panel separation**

The formal CORINTHLOVE panel is a distinct empty registry object requiring at
least eight models, three vendors, and three tiers. It remains
`authorization:not_authorized` in this plan. Cheap models may later be members
only if the separately frozen formal design includes them; cheap-screen data
cannot be relabeled formal.

- [ ] **Step 3: Test general-purpose-only eligibility**

Reject safety classifiers, embedding models, reward models, domain-specific
Christian models, proprietary judge-only systems, unavailable endpoints, and
routes that cannot preserve exact identity, provider pinning, fallback denial,
and privacy controls.

- [ ] **Step 4: Run and commit**

```bash
python3 -m pytest BIBLEBENCH-PILOT/tests/test_panels.py -q
git log -1 --oneline
git add BIBLEBENCH-PILOT/config/panels.yaml BIBLEBENCH-PILOT/tests/test_panels.py
git commit -m "BibleBench: separate cheap and formal panels"
```

### Task 3: Compile and prove the exact cheap qualification freeze

**Files:**
- Create: `BIBLEBENCH-PILOT/config/qualification-gates.yaml`
- Create: `BIBLEBENCH-PILOT/status/freeze.example.json`
- Create: `BIBLEBENCH-PILOT/tests/test_qualification_freeze.py`

- [ ] **Step 1: Test exact schedule counts**

Assert 48 episodes, 1,344 logical calls, correct forecast/primary/probe counts,
four models, four modules, balanced target/null/restraint per module, 34/14
strata, C0/C1/C2 only, no C3, and no optional calls. Assert every call has a
unique logical ID and exact request/token ceiling.

- [ ] **Step 2: Prove worst-case cost before network authority**

From fresh catalog prices and exact byte/token ceilings, compute Decimal cost
per call, route, model, module, and total. Require total <= USD 25 and record a
hard cap of exactly the approved value, never an inferred sum of historical
caps. Cost uncertainty blocks freeze.

- [ ] **Step 3: Freeze sources, schedules, policies, and expected gates**

Hash exact module inventories, cores, episodes, gold lock, cue geometry,
response/tool schemas, sandbox reducers, lens/rubric versions, runner/runtime,
route catalog, panel, budget, diagnostics, and report schema. C3 stores only an
external commitment hash; its content is absent.

- [ ] **Step 4: Keep freeze separate from authority**

The freeze receipt sets all live/ranking/composite/publication booleans false.
A separate owner-signed/no-replace authority receipt must bind the freeze hash,
exact four-model roster, routes, expiry, and cap before POST dispatch.

- [ ] **Step 5: Run and commit**

```bash
python3 -m pytest BIBLEBENCH-PILOT/tests/test_qualification_freeze.py -q
git log -1 --oneline
git add BIBLEBENCH-PILOT/config/qualification-gates.yaml BIBLEBENCH-PILOT/status/freeze.example.json BIBLEBENCH-PILOT/tests/test_qualification_freeze.py
git commit -m "BibleBench: freeze cheap qualification matrix"
```

### Task 4: Run authenticated preflight and non-bank live smoke

**Files:**
- Create: `BIBLEBENCH-PILOT/tests/test_live_guards.py`
- Generate after approval: `BIBLEBENCH-PILOT/runs/<run-id>/preflight/`

- [ ] **Step 1: Pass the complete offline gate**

Run all tests, whole-root source and leakage audits, route/budget simulations,
restart/tamper cases, import safety, and credential-pattern scans. The approved
CORINTHLOVE Tier-0 snapshot must verify read-only; no source bank may change.

- [ ] **Step 2: Perform authenticated GET only**

With owner authority, read the key at call time, fetch catalog/route data, and
freeze sanitized identity/price/privacy evidence. If exact pinned routes,
returned aliases, cheap ceiling, ZDR/data policy, schema/tool support, or token
limits differ, stop before POST and generate a new freeze proposal.

- [ ] **Step 3: Execute non-bank smoke only**

After a separate authority receipt, send one synthetic, non-bank request per
model/route using the real response contract. Zero retries. Require exact
identity, complete response, schema resolution, usage/cost receipt, and terminal
manifest. Any drift, fallback, unknown delivery, budget uncertainty, or private
leak stops the tranche.

- [ ] **Step 4: Review smoke evidence**

The report is infrastructure evidence only. A failed model/route is replaced
only through a new catalog, roster, budget, freeze, and authority receipt; it is
not silently rerouted.

### Task 5: Execute the tightly capped cheap diagnostic tranche

**Files:**
- Generate after approval: `BIBLEBENCH-PILOT/runs/<run-id>/`
- Create: `BIBLEBENCH-PILOT/tests/test_live_result_validation.py`

- [ ] **Step 1: Obtain exact owner authority**

Jimmy approves the frozen roster and cap after reviewing the preflight and
non-bank smoke. This authority covers only 1,344 registered logical calls,
their pinned routes, the stated expiry, and the hard cap. It does not authorize
frontier, C3, formal concordance, calibration, ranking, or publication.

- [ ] **Step 2: Execute in balanced tranches**

Interleave model/module/cue/order so an interruption cannot confound a model or
cue with time. Reserve cost before each call, seal the dispatch fence, send once,
retain exact evidence, and close terminally. On process restart continue only
unattempted calls. A provider/rate-limit failure parks affected unattempted rows
without creating retries.

- [ ] **Step 3: Close and verify**

Publish complete or invalid restricted-partial manifest last. Replay every
request, event, lens packet, native score, diagnostic, and report. Reconcile
logical calls, physical attempts, successes, failures, unattempted rows,
reservations, paid equivalents, usage, and Decimal cost exactly.

- [ ] **Step 4: Keep the interpretation diagnostic-only**

Report completion, mechanical validity, schema access, route integrity,
missingness, non-saturation, discrimination, cue effects, capability twins,
cost, and module vectors. No leaderboard, qualified composite, L1/L2 formal
Love concordance, or “best ethical model” claim is permitted.

### Task 6: Apply the registered promotion diagnostics

**Files:**
- Modify: `BIBLEBENCH-PILOT/src/biblebench_pilot/qualification.py`
- Create: `BIBLEBENCH-PILOT/tests/test_promotion_gates.py`

- [ ] **Step 1: Implement the mechanical and custody gates**

Require >=95% mechanically valid among delivered responses, complete route and
cost provenance, no leakage/canary/identity/fallback violation, exact schedule
geometry, exact source hashes, and no unresolved manifest or duplicate call.
Report delivery failures separately; do not miscode them as model behavior.

- [ ] **Step 2: Implement scientific diagnostic gates**

Require target/null/restraint discrimination, no wholesale floor or ceiling,
cue effect not dominating model/episode effects, capability twins sufficient to
interpret action failures, and no red-line ambiguity. Report mode discordance,
monitoring sensitivity, and module-specific saturation rather than forcing one
global pass.

- [ ] **Step 3: Implement human reliability gate**

After the owner completes blinded ballots and the stratified 20% repeat,
require weighted repeat agreement >=0.80. `contested` remains visible;
`outside_competence` is referred. This gate is necessary for promotion, but its
absence does not erase valid engineering evidence.

- [ ] **Step 4: Test formal-inference latches**

Even if cheap gates pass, keep composite, ranking, CORINTHLOVE L1/L2,
confirmatory C3, and formal ethical claims false. Those require separate panel,
calibration, held-out, and owner authority.

- [ ] **Step 5: Run and commit code-only changes**

```bash
python3 -m pytest BIBLEBENCH-PILOT/tests/test_promotion_gates.py -q
git log -1 --oneline
git add BIBLEBENCH-PILOT/src/biblebench_pilot/qualification.py BIBLEBENCH-PILOT/tests/test_promotion_gates.py
git commit -m "BibleBench: enforce cheap promotion diagnostics"
```

### Task 7: Permit one evidence-supported revision and freeze the bank

**Files:**
- Create: `BIBLEBENCH-PILOT/status/revision-ledger.schema.json`
- Generate after diagnostic review: `BIBLEBENCH-PILOT/status/<date>-revision-ledger.json`
- Create: `BIBLEBENCH-PILOT/tests/test_revision_policy.py`

- [ ] **Step 1: Localize every proposed change**

Each change cites a replicated cue/family/stage failure, affected frozen hashes,
unchanged comparison arm, expected diagnostic improvement, theological review,
and why the defect invalidates interpretation. Aggregate model preference or
one small cell is insufficient.

- [ ] **Step 2: Enforce exactly one revision cycle**

The ledger accepts cycle 1 only. Cycle 2 requires a new owner-approved design
version. Never overwrite the original bank, run, or report; create a new
versioned root and retain comparison lineage.

- [ ] **Step 3: Re-run offline and cheap gates under new authority if changed**

Any content, route, schema, rubric, scorer, or budget change invalidates the old
freeze and authority. Repeat Tier-0 and, only if approved, the cheap diagnostic
on the changed registered cells plus unchanged controls.

- [ ] **Step 4: Freeze public calibration and private held-out templates**

After gates pass, publish create-only source/bank/runtime manifests, canary and
leakage policies, exact split lineage, and C3 external commitment. Held-out
content stays absent from development code/config/prompts/reports.

- [ ] **Step 5: Stop for the next owner ruling**

Produce a scale-readiness package listing passed/failed gates, unresolved human
or formal-panel dependencies, exact future matrix, and cost proposal. Do not
execute frontier models, the >=8-model formal panel, C3, private confirmation,
or a qualified composite without new explicit authorization.

### Task 8: Final credential-free verification of the complete package

- [ ] **Step 1: Run all tests in a fresh process**

```bash
python3 -m pytest BIBLEBENCH-PILOT/tests -q
git diff --check
```

Expected: all tests pass and no whitespace errors.

- [ ] **Step 2: Audit plans against artifacts**

Verify exact 12/8/12/10 cores, 48 development episodes, 4/4/4 roles per module,
34/14 strata, 1,344-call cheap matrix, C3 absence, native/crosswalk separation,
zero hidden retries, no attempted-call retry, manifest-last closure, and all
authority latches.

- [ ] **Step 3: Manual evidence review**

Read the first and last records for each model/module/cue/status, every failed
or repaired response, the complete budget ledger, all red-line disagreements,
the owner repeat report, native module summaries, and the final limitations.
Confirm that cheap evidence is never described as formal measurement or rank.

- [ ] **Step 4: Request independent review before any promotion**

Have a fresh reviewer test specification coverage, custody, leakage, semantic
invariance, theological non-claims, native scorer boundaries, and report
honesty. Classify issues as current blockers, explicit deferred debt, or scope
changes; do not expand review indefinitely.
