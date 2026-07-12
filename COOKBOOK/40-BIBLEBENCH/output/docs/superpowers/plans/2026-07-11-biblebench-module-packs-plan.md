# BibleBench Four Passage-Module Packs Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Encode the exact 42 selected core families as four provenance-bound adapters and author a balanced 12-episode shared-evidence development pack for each module.

**Architecture:** FruitBench, CORINTHLOVE, 10CBench, and SermonMount own their constructs, theological boundaries, item lineage, native scorer adapters, and interpretation. The shared engine owns identity, custody, cue geometry, sandbox execution, and evidence. Each module has 12 development episodes: four target opportunities, four null/foil cases, and four restraint/counterfeit/overreach cases. All 42 core families appear at least once; six families receive a second episode so every module has the same 12-episode diagnostic geometry.

**Fixed development matrix:** 48 episodes total; 34 common-life and 14 Christian-facing. Per module: FruitBench 9/3, CORINTHLOVE 8/4, 10CBench 8/4, SermonMount 9/3. Per model/module: 12 blind forecasts + 36 C0/C1/C2 primaries + 36 matched probes = 84 logical calls. Optional interventions are separately registered and excluded from the qualification schedule unless explicitly approved.

**CORINTHLOVE dependency:** First execute the separately approved offline-only
Tier-0 plan at `COOKBOOK/20260711e-corinthlove-consolidated-core-implementation-plan.md`.
This plan consumes its verified snapshot through a read-only adapter. It does
not recreate DIMGLASS, CHARITROC, or CROSSROADS, invent a crosswalk, or treat
the eight BibleBench Love scenario cores as native C1-C16 measurements.

---

### Task 1: Freeze machine-readable module inventories

**Files:**
- Create: `BIBLEBENCH-PILOT/schemas/module.schema.json`
- Create: `BIBLEBENCH-PILOT/modules/fruitbench/module.yaml`
- Create: `BIBLEBENCH-PILOT/modules/corinthlove/module.yaml`
- Create: `BIBLEBENCH-PILOT/modules/tencommandments/module.yaml`
- Create: `BIBLEBENCH-PILOT/modules/sermonmount/module.yaml`
- Create: `BIBLEBENCH-PILOT/tests/test_module_inventory.py`

- [ ] **Step 1: Write failing inventory tests**

```python
from biblebench_pilot.registry import load_module_inventory

def test_all_module_inventories_declare_native_boundaries(module_paths):
    rows = [load_module_inventory(path) for path in module_paths]
    assert {r.module for r in rows} == {
        "fruitbench", "corinthlove", "tencommandments", "sermonmount"
    }
    assert all(r.construct and r.intended_claims and r.explicit_non_claims for r in rows)
    assert all(r.native_scorer and r.binding_handoffs for r in rows)
```

- [ ] **Step 2: Verify failure**

```bash
python3 -m pytest BIBLEBENCH-PILOT/tests/test_module_inventory.py -q
```

- [ ] **Step 3: Define the closed inventory schema**

Require benchmark/version/owner/state, binding handoffs, frozen surfaces,
construct, unit, modality, scoring outputs, intended claims, explicit
non-claims, lineage, use split, privacy class, leakage/canary policy, license,
harness/schema/test/evidence entry points, inference roles, calibration state,
provider/secret/spend history, shared-core gaps, and owner-only decisions.
Unknown fields fail closed.

- [ ] **Step 4: Record lane authority honestly**

Mark SermonMount `PARKED_CONSOLIDATED`, its M2-M4 as not started, and its paid
calls/spend as 0/$0.00. Mark the 10CBench legacy sequential plan parked; cite
the frozen TABLETS 4,452-response fixture bundle as `FIXTURE_ONLY`, not
empirical evidence. Mark FruitBench shared-episode design as a design
precedent. No inventory record grants network, spend, Git, or publication
authority.

For CORINTHLOVE, bind the approved modular-suite/tiered-funnel design, the
ten-field export, the frozen C1-C16 and six-family registries, and the separate
cheap/formal panels. Record DIMGLASS and CHARITROC as `crosswalk_mapped`,
CROSSROADS as `native_first_order`, and WEIGHBRIDGE/AGAPEGAME as required but
unbuilt members of the eventual minimum native core.

- [ ] **Step 5: Run and commit**

```bash
python3 -m pytest BIBLEBENCH-PILOT/tests/test_module_inventory.py -q
git log -1 --oneline
git add BIBLEBENCH-PILOT/schemas/module.schema.json BIBLEBENCH-PILOT/modules/fruitbench/module.yaml BIBLEBENCH-PILOT/modules/corinthlove/module.yaml BIBLEBENCH-PILOT/modules/tencommandments/module.yaml BIBLEBENCH-PILOT/modules/sermonmount/module.yaml BIBLEBENCH-PILOT/tests/test_module_inventory.py
git commit -m "BibleBench: freeze four module inventories"
```

### Task 2: Encode the exact 42 core manifests

**Files:**
- Create: `BIBLEBENCH-PILOT/modules/fruitbench/cores.yaml`
- Create: `BIBLEBENCH-PILOT/modules/corinthlove/cores.yaml`
- Create: `BIBLEBENCH-PILOT/modules/tencommandments/cores.yaml`
- Create: `BIBLEBENCH-PILOT/modules/sermonmount/cores.yaml`
- Create: `BIBLEBENCH-PILOT/tests/test_module_packs.py`

- [ ] **Step 1: Write the failing exact-ID test**

```python
EXPECTED = {
    "fruitbench": {f"F{i:02d}" for i in range(1, 13)},
    "corinthlove": {f"L{i:02d}" for i in range(1, 9)},
    "tencommandments": {f"T{i:02d}" for i in range(1, 13)},
    "sermonmount": {f"S{i:02d}" for i in range(1, 11)},
}

def test_core_ids_match_approved_selection(loaded_modules):
    assert {name: {c.core_id for c in cores} for name, cores in loaded_modules.items()} == EXPECTED
```

- [ ] **Step 2: Author records from the approved selection package**

Transcribe IDs, selected source paths, pilot use, primary evidence, and boundary
from `output/docs/superpowers/specs/2026-07-11-biblebench-42-core-selection.md`.
Add passage anchors, explicit non-claims, deficient/counterfeit poles, shared and
module red lines, eligible modes/transforms, and behavioral-attribution status.
Do not invent source claims or edit legacy source files.

L01-L08 use a distinct `biblebench_pilot_construct` namespace. They may cite
native or legacy sources, but cannot emit C1-C16 clause observations without an
approved coverage map. Store mapping status explicitly as `native_first_order`,
`crosswalk_mapped`, or `unmapped_pilot_construct`; missing mapping status fails.

- [ ] **Step 3: Reconcile interpretive-only cores**

T01 and any Godward, worship, covenantal, or Spirit-wrought core must be
`not_behaviorally_attributable` and routed to interpretation/pastoral fidelity.
The parked SOVEREIGN executable-bank program remains deferred; T01 uses only
the approved delimited interpretive counsel construct and cannot schedule a
latent-objective or worship-behavior experiment. S10 remains non-aggregable as
ethical action evidence.

- [ ] **Step 4: Validate source provenance and counts**

Resolve every path inside the workspace, hash the exact bytes once, and save
the hash in the generated freeze input. Assert 12/8/12/10 counts, unique IDs,
no traversal, and no missing sources.

- [ ] **Step 5: Run and commit**

```bash
python3 -m pytest BIBLEBENCH-PILOT/tests/test_module_packs.py -q
git log -1 --oneline
git add BIBLEBENCH-PILOT/modules/fruitbench/cores.yaml BIBLEBENCH-PILOT/modules/corinthlove/cores.yaml BIBLEBENCH-PILOT/modules/tencommandments/cores.yaml BIBLEBENCH-PILOT/modules/sermonmount/cores.yaml BIBLEBENCH-PILOT/tests/test_module_packs.py
git commit -m "BibleBench: encode approved 42 core families"
```

### Task 3: Author balanced shared-episode development packs

**Files:**
- Create: `BIBLEBENCH-PILOT/modules/fruitbench/episodes.yaml`
- Create: `BIBLEBENCH-PILOT/modules/corinthlove/episodes.yaml`
- Create: `BIBLEBENCH-PILOT/modules/tencommandments/episodes.yaml`
- Create: `BIBLEBENCH-PILOT/modules/sermonmount/episodes.yaml`
- Create: `BIBLEBENCH-PILOT/tests/test_episode_packs.py`

- [ ] **Step 1: Write failing balance and coverage tests**

```python
def test_each_module_has_twelve_balanced_development_episodes(packs):
    for pack in packs.values():
        assert len(pack.episodes) == 12
        assert pack.role_counts() == {"target": 4, "null": 4, "restraint": 4}

def test_all_42_cores_are_represented_and_strata_are_34_14(packs):
    assert len({e.core_id for p in packs.values() for e in p.episodes}) == 42
    assert sum(e.stratum == "common_life" for p in packs.values() for e in p.episodes) == 34
    assert sum(e.stratum == "christian_facing" for p in packs.values() for e in p.episodes) == 14
```

- [ ] **Step 2: Author episode seeds and capability twins**

Each record declares core ID, role, stratum, mode, shared body, C0/C1/C2 cue
surfaces, semantic response tokens, tools, sandbox reducer, capability twin,
probe, transform eligibility, source lineage, and private template version. All
action-primary episodes require a certified nonmoral capability twin.

- [ ] **Step 3: Prove semantic and moral invariance**

Generate a review sheet comparing C0/C1/C2 and every pressure/monitoring skin.
Tests reject changed right action, changed affected parties, easier tools,
different answer contract, cue/order collinearity, or a C3 string in any
development artifact. Null and restraint cases must expose false-positive,
overreach, coercion, passivity, or counterfeit-style failure poles.

- [ ] **Step 4: Compile exact call geometry**

Assert 84 logical calls per model/module and 336 per model across the battery:
48 forecasts, 144 primaries, and 144 probes. Lens counts do not alter this
geometry. Write a coverage proof listing the six repeated core families and why
their second episode is needed.

- [ ] **Step 5: Run and commit**

```bash
python3 -m pytest BIBLEBENCH-PILOT/tests/test_episode_packs.py BIBLEBENCH-PILOT/tests/test_schedule.py -q
git log -1 --oneline
git add BIBLEBENCH-PILOT/modules/fruitbench/episodes.yaml BIBLEBENCH-PILOT/modules/corinthlove/episodes.yaml BIBLEBENCH-PILOT/modules/tencommandments/episodes.yaml BIBLEBENCH-PILOT/modules/sermonmount/episodes.yaml BIBLEBENCH-PILOT/tests/test_episode_packs.py
git commit -m "BibleBench: add balanced shared episode packs"
```

### Task 4: Build the owner provisional-gold workbench

**Files:**
- Create: `BIBLEBENCH-PILOT/schemas/gold.schema.json`
- Create: `BIBLEBENCH-PILOT/src/biblebench_pilot/adjudication.py`
- Create: `BIBLEBENCH-PILOT/config/adjudication.yaml`
- Create: `BIBLEBENCH-PILOT/tests/test_adjudication.py`

- [ ] **Step 1: Test the gold lock and authority labels**

Require `single_expert_provisional_gold`, theologian/technical owner role,
acceptable action band, prohibited actions, deficient and counterfeit poles,
red lines, consequence/repair expectations, confidence, and exactly one of
`clear`, `contested`, or `outside_competence`. Reject gold authored after an
actor response hash enters the store.

- [ ] **Step 2: Implement blinded 20% repeat adjudication**

Select a deterministic stratified 20% of episode-lens ballots, assign fresh
opaque packet IDs, randomize order, and hide original ratings. Keep the original
and repeat ballots separate until agreement analysis. `outside_competence`
routes to referral and cannot be numerically imputed.

- [ ] **Step 3: Export a no-network owner workbench**

The CLI exports packets containing exact source excerpts, frozen observable
events, opaque evidence IDs, and the registered rubric—but no actor/model/cue
identity. Import validates packet hash, rubric version, evidence IDs, and gold
lock. It never calls a model judge.

- [ ] **Step 4: Run and commit**

```bash
python3 -m pytest BIBLEBENCH-PILOT/tests/test_adjudication.py -q
git log -1 --oneline
git add BIBLEBENCH-PILOT/schemas/gold.schema.json BIBLEBENCH-PILOT/src/biblebench_pilot/adjudication.py BIBLEBENCH-PILOT/config/adjudication.yaml BIBLEBENCH-PILOT/tests/test_adjudication.py
git commit -m "BibleBench: add provisional gold workbench"
```

### Task 5: Implement thin module adapters and fixture slices

**Files:**
- Create: `BIBLEBENCH-PILOT/src/biblebench_pilot/module_adapters.py`
- Create: `BIBLEBENCH-PILOT/fixtures/modules/fruitbench.json`
- Create: `BIBLEBENCH-PILOT/fixtures/modules/corinthlove.json`
- Create: `BIBLEBENCH-PILOT/fixtures/modules/tencommandments.json`
- Create: `BIBLEBENCH-PILOT/fixtures/modules/sermonmount.json`
- Create: `BIBLEBENCH-PILOT/tests/test_module_adapters.py`

- [ ] **Step 1: Define the native adapter protocol**

An adapter supplies rendering, parsing/normalization, observable-event mapping,
lens applicability, native mechanical outcomes, native estimands, abstention
policy, and explicit missingness. It cannot change shared identity, custody,
route, budget, evidence-basis, or authority fields.

- [ ] **Step 2: Add one complete no-network slice per module**

Each fixture covers forecast, primary action or consequential artifact, matched
probe, sandbox/event record, applicable native lenses, malformed response,
refusal, and unknown-delivery terminal input. Mark every output exactly
`harness validation, NOT a measurement` and `FIXTURE_ONLY`.

- [ ] **Step 3: Test legacy preservation**

Adapters may cite frozen legacy artifacts by absolute source hash, but must not
copy private bank bytes, mutate legacy files, or infer empirical eligibility
from fixture results. Add tests that reject a changed legacy hash or any attempt
to promote TABLETS synthetic recovery to empirical evidence.

The CORINTHLOVE adapter additionally verifies the approved Tier-0 snapshot,
preserves the exact ten-field upstream rows, and exports native and crosswalk
profiles in separate namespaces. The cheap shared-episode screen may report
only infrastructure, non-saturation, missingness, and construct-local vectors;
it cannot run registered L1/L2 concordance. Formal concordance requires at
least CROSSROADS, WEIGHBRIDGE, and AGAPEGAME on one frozen panel of at least
eight models, three vendors, and three capability tiers.

- [ ] **Step 4: Run the module suite and commit**

```bash
python3 -m pytest BIBLEBENCH-PILOT/tests/test_module_inventory.py BIBLEBENCH-PILOT/tests/test_module_packs.py BIBLEBENCH-PILOT/tests/test_episode_packs.py BIBLEBENCH-PILOT/tests/test_adjudication.py BIBLEBENCH-PILOT/tests/test_module_adapters.py -q
git log -1 --oneline
git add BIBLEBENCH-PILOT/src/biblebench_pilot/module_adapters.py BIBLEBENCH-PILOT/fixtures/modules BIBLEBENCH-PILOT/tests/test_module_adapters.py
git commit -m "BibleBench: add four native module adapters"
```

Expected: the exact 42-core registry and all four 12-episode fixture slices pass without network access.
