# CORINTHLOVE Consolidated Core Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build an offline-only consolidated core that inventories DIMGLASS, CHARITROC, and CROSSROADS through read-only adapters, freezes source evidence, emits the registered ten-field export, and validates synthetic L1/L2 analysis without running models.

**Architecture:** A new `CORINTHLOVE-CONSOLIDATED` root owns strict contracts, source adapters, immutable snapshots, and portfolio analysis while treating every bank as an immutable upstream module. Native C1–C16 evidence and crosswalk-mapped family evidence remain separate; cheap screening and formal panels are distinct registries.

**Tech Stack:** Python 3.9, standard-library JSON/hash/path tooling, NumPy 1.26, SciPy 1.13, pytest 8, JSON/JSONL/CSV, Markdown reports.

**Execution rule:** Do not commit, call OpenRouter, generate a new bank, alter an upstream bank, or create measurement claims. The user must separately authorize any commit or live phase.

---

## File structure

Create this bounded first slice:

```text
COOKBOOK/40-BIBLEBENCH/CORINTHLOVE-CONSOLIDATED/
├── AGENTS.md
├── README.md
├── STATUS.md
├── DECISIONS.md
├── pyproject.toml
├── registry/
│   ├── clauses.json
│   ├── methods.json
│   ├── panels.json
│   └── sources.lock.json
├── src/corinthlove_suite/
│   ├── __init__.py
│   ├── contracts.py
│   ├── provenance.py
│   ├── inventory.py
│   ├── evidence.py
│   ├── export.py
│   ├── profiles.py
│   ├── qualification.py
│   ├── concordance.py
│   ├── clause_structure.py
│   ├── report.py
│   ├── cli.py
│   └── adapters/
│       ├── __init__.py
│       ├── base.py
│       ├── dimglass.py
│       ├── charitroc.py
│       └── crossroads.py
├── tests/
├── fixtures/
├── snapshots/
├── reports/
└── selfcheck.py
```

## Task 1: Scaffold and freeze registry identities

**Files:**
- Create: `CORINTHLOVE-CONSOLIDATED/pyproject.toml`
- Create: `CORINTHLOVE-CONSOLIDATED/registry/clauses.json`
- Create: `CORINTHLOVE-CONSOLIDATED/registry/methods.json`
- Create: `CORINTHLOVE-CONSOLIDATED/registry/panels.json`
- Create: `CORINTHLOVE-CONSOLIDATED/tests/test_registry.py`

- [ ] **Step 1: Write failing registry tests**

```python
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def load(name):
    return json.loads((ROOT / "registry" / name).read_text())

def test_clause_registry_is_exact_and_family_complete():
    value = load("clauses.json")
    assert value["registry_source"] == "../CORINTHLOVE-v3/00-corinthlove-v3-portfolio.md#3"
    assert value["clauses"] == [f"C{i}" for i in range(1, 17)]
    assert sorted(sum(value["families"].values(), [])) == sorted(value["clauses"])

def test_initial_methods_keep_native_and_crosswalk_boundaries():
    rows = {row["method_id"]: row for row in load("methods.json")["methods"]}
    assert rows["01-crossroads"]["method_class"] == "native_first_order"
    assert rows["01-crossroads"]["coverage"] == [f"C{i}" for i in range(1, 17)]
    assert rows["dimglass"]["method_class"] == "crosswalk_mapped"
    assert rows["charitroc"]["method_class"] == "crosswalk_mapped"
    assert all(not row.get("crosswalk_targets") for row in rows.values())

def test_cheap_and_formal_panels_are_distinct():
    panels = load("panels.json")["panels"]
    assert panels["cheap-screen"]["formal_inference"] is False
    assert panels["formal-shared"]["formal_inference"] is True
    assert panels["formal-shared"]["minimum_models"] == 8
    assert panels["formal-shared"]["models"] == []
```

- [ ] **Step 2: Run the tests and verify RED**

Run:

```sh
cd COOKBOOK/40-BIBLEBENCH/CORINTHLOVE-CONSOLIDATED
/Users/jimmy.lin/Documents/CEI-Literature-Vault/.venv/bin/python -m pytest tests/test_registry.py -q
```

Expected: FAIL because registry files do not exist.

- [ ] **Step 3: Add the package configuration**

```toml
[build-system]
requires = ["setuptools>=61"]
build-backend = "setuptools.build_meta"

[project]
name = "corinthlove-suite"
version = "0.1.0"
requires-python = ">=3.9"
dependencies = ["numpy==1.26.4", "scipy==1.13.1"]

[tool.setuptools]
package-dir = {"" = "src"}

[tool.pytest.ini_options]
pythonpath = ["src"]
```

- [ ] **Step 4: Add exact registry JSON**

`clauses.json`:

```json
{
  "registry_version": "corinthlove-c1-c16-v1",
  "registry_source": "../CORINTHLOVE-v3/00-corinthlove-v3-portfolio.md#3",
  "clauses": ["C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9", "C10", "C11", "C12", "C13", "C14", "C15", "C16"],
  "families": {
    "capability-vs-love": ["C1"],
    "patience-kindness": ["C2", "C3"],
    "status": ["C4", "C5", "C7"],
    "truth-dignity": ["C6", "C10", "C11"],
    "protective-trust": ["C12", "C13", "C14"],
    "endurance-humility": ["C15", "C16"]
  }
}
```

`methods.json`:

```json
{
  "registry_version": "corinthlove-methods-v1",
  "methods": [
    {
      "method_id": "dimglass",
      "method_class": "crosswalk_mapped",
      "source_root": "../CORINTHLOVE-v2/BANKS/09-dimglass",
      "coverage_map": "export/coverage_map.json",
      "episode_export": "export/episode_table.jsonl",
      "coverage": ["DIMGLASS:EPISTEMIC_HUMILITY"]
    },
    {
      "method_id": "charitroc",
      "method_class": "crosswalk_mapped",
      "source_root": "../CORINTHLOVE/BANKS/07-charitroc",
      "coverage_map": "export/coverage_map.json",
      "episode_export": "export/episode_table.jsonl",
      "coverage": ["CHARITROC:CALIBRATED_CHARITY"]
    },
    {
      "method_id": "01-crossroads",
      "method_class": "native_first_order",
      "source_root": "../CORINTHLOVE-v3/BANKS/01-crossroads",
      "coverage_map": "export/coverage_map.json",
      "episode_export": "export/episode_table.jsonl",
      "coverage": ["C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9", "C10", "C11", "C12", "C13", "C14", "C15", "C16"]
    }
  ]
}
```

`panels.json`:

```json
{
  "registry_version": "corinthlove-panels-v1",
  "panels": {
    "cheap-screen": {
      "formal_inference": false,
      "authorization": "cheap-public-qualification-only",
      "models": [
        {"alias": "openai/gpt-5-nano", "vendor": "OpenAI", "tier": "nano"},
        {"alias": "openai/gpt-5.4-nano", "vendor": "OpenAI", "tier": "nano"},
        {"alias": "openai/gpt-5-mini", "vendor": "OpenAI", "tier": "mini"},
        {"alias": "openai/gpt-5.4-mini", "vendor": "OpenAI", "tier": "mini"}
      ]
    },
    "formal-shared": {
      "formal_inference": true,
      "authorization": "not-authorized",
      "minimum_models": 8,
      "minimum_vendors": 3,
      "minimum_tiers": 3,
      "models": []
    }
  }
}
```

`crosswalk_targets` is absent from every method entry.

- [ ] **Step 5: Run tests and verify GREEN**

Expected: `3 passed`.

- [ ] **Step 6: Checkpoint without committing**

Run `git diff --check`; record the passing output in the task log. Do not stage
or commit.

## Task 2: Strict contracts and provenance boundaries

**Files:**
- Create: `src/corinthlove_suite/contracts.py`
- Create: `src/corinthlove_suite/provenance.py`
- Create: `tests/test_contracts.py`

- [ ] **Step 1: Write failing contract tests**

```python
import pytest
from corinthlove_suite.contracts import EpisodeRow, validate_episode_row
from corinthlove_suite.provenance import validate_provenance

VALID = {
    "model_id": "mock-model-A", "method_id": "01-crossroads",
    "item_family": "family", "item_id": "ITEM-1", "clause": "C1",
    "score": 1.0, "rung": "choice", "judge_ids": "mechanical",
    "mechanical_flag": 0, "canary_id": "10CB3-01-example"
}

def test_episode_row_has_exact_ten_fields():
    assert validate_episode_row(VALID) == EpisodeRow(**VALID)
    with pytest.raises(ValueError, match="fields"):
        validate_episode_row({**VALID, "hidden_truth": True})

def test_native_and_crosswalk_clause_namespaces_are_disjoint():
    validate_episode_row(VALID)
    validate_episode_row({**VALID, "method_id": "charitroc",
                          "clause": "CHARITROC:CALIBRATED_CHARITY"})
    with pytest.raises(ValueError, match="native clause"):
        validate_episode_row({**VALID, "method_id": "charitroc", "clause": "C16"})

def test_mock_cannot_be_promoted_to_measurement():
    with pytest.raises(ValueError, match="mock"):
        validate_provenance("harness validation, NOT a measurement", "measurement")
```

- [ ] **Step 2: Verify RED**

Run `python -m pytest tests/test_contracts.py -q`; expect import failure.

- [ ] **Step 3: Implement immutable row validation**

```python
from dataclasses import dataclass
from numbers import Real

FIELDS = {"model_id", "method_id", "item_family", "item_id", "clause",
          "score", "rung", "judge_ids", "mechanical_flag", "canary_id"}

@dataclass(frozen=True)
class EpisodeRow:
    model_id: str
    method_id: str
    item_family: str
    item_id: str
    clause: str
    score: float
    rung: str
    judge_ids: str
    mechanical_flag: int
    canary_id: str

def validate_episode_row(value):
    if not isinstance(value, dict) or set(value) != FIELDS:
        raise ValueError("episode row fields differ")
    for field in FIELDS - {"score", "mechanical_flag"}:
        if not isinstance(value[field], str) or not value[field]:
            raise ValueError(f"episode row {field} is invalid")
    if isinstance(value["score"], bool) or not isinstance(value["score"], Real):
        raise ValueError("episode row score is invalid")
    if value["mechanical_flag"] not in {0, 1}:
        raise ValueError("episode row mechanical_flag is invalid")
    native_clauses = {f"C{i}" for i in range(1, 17)}
    if value["method_id"] in {"dimglass", "charitroc"} and value["clause"] in native_clauses:
        raise ValueError("crosswalk method cannot assert native clause")
    return EpisodeRow(**{**value, "score": float(value["score"])})
```

Implement provenance as a frozen allowed-state table. Only identical source
and requested phases pass; mock and protocol diagnostics can never promote.

- [ ] **Step 4: Verify GREEN and run registry tests**

Expected: all contract and registry tests pass.

- [ ] **Step 5: Checkpoint without committing**

Run `git diff --check` and scan the new root for unresolved marker strings.

## Task 3: Read-only adapter and source inventory

**Files:**
- Create: `src/corinthlove_suite/adapters/base.py`
- Create: `src/corinthlove_suite/inventory.py`
- Create: `tests/test_adapter_base.py`

- [ ] **Step 1: Write failing read-only tests**

```python
from pathlib import Path
from corinthlove_suite.adapters.base import JsonlAdapter

def test_adapter_reads_canonical_jsonl_without_writing(tmp_path):
    source = tmp_path / "rows.jsonl"
    source.write_text('{"model_id":"m","method_id":"01-crossroads","item_family":"f","item_id":"i","clause":"C1","score":1,"rung":"choice","judge_ids":"mechanical","mechanical_flag":0,"canary_id":"c"}\n')
    before = source.read_bytes()
    rows = list(JsonlAdapter("01-crossroads", source).iter_rows())
    assert len(rows) == 1
    assert source.read_bytes() == before

def test_duplicate_json_keys_fail(tmp_path):
    source = tmp_path / "rows.jsonl"
    source.write_text('{"model_id":"a","model_id":"b"}\n')
    adapter = JsonlAdapter("01-crossroads", source)
    try:
        list(adapter.iter_rows())
    except ValueError as error:
        assert "duplicate" in str(error)
    else:
        raise AssertionError("duplicate key was accepted")
```

- [ ] **Step 2: Verify RED**

Expected: import failure.

- [ ] **Step 3: Implement strict JSONL and inventory hashing**

Use `json.loads(..., object_pairs_hook=unique_pairs, parse_constant=reject)`;
require canonical JSON objects and `validate_episode_row` for every line.
`inventory.py` returns absolute source path, SHA-256, byte count, row count,
method IDs, model IDs, clauses, and no mutation timestamp comparison.

- [ ] **Step 4: Add a write tripwire**

Hash every source file before and after adapter iteration; raise
`ValueError("source bank changed during read")` on any difference.

- [ ] **Step 5: Verify GREEN**

Expected: adapter tests pass.

- [ ] **Step 6: Checkpoint without committing**

Run focused tests and `git diff --check`.

## Task 4: Implement three source-specific adapters

**Files:**
- Create: `src/corinthlove_suite/adapters/dimglass.py`
- Create: `src/corinthlove_suite/adapters/charitroc.py`
- Create: `src/corinthlove_suite/adapters/crossroads.py`
- Create: `tests/test_existing_adapters.py`

- [ ] **Step 1: Write failing exact-source tests**

```python
from corinthlove_suite.adapters.dimglass import DimGlassAdapter
from corinthlove_suite.adapters.charitroc import CharitrocAdapter
from corinthlove_suite.adapters.crossroads import CrossroadsAdapter

def test_existing_coverage_boundaries():
    dim = DimGlassAdapter().coverage()
    char = CharitrocAdapter().coverage()
    cross = CrossroadsAdapter().coverage()
    assert dim.mapping_status == "crosswalk-mapped"
    assert dim.clauses == ("DIMGLASS:EPISTEMIC_HUMILITY",)
    assert char.mapping_status == "crosswalk-mapped only"
    assert char.clauses == ("CHARITROC:CALIBRATED_CHARITY",)
    assert cross.mapping_status == "native frozen registry"
    assert cross.clauses == tuple(f"C{i}" for i in range(1, 17))

def test_existing_mock_exports_validate_without_rescoring():
    for adapter in (DimGlassAdapter(), CharitrocAdapter(), CrossroadsAdapter()):
        rows = list(adapter.iter_rows())
        assert rows
        assert {row.method_id for row in rows} == {adapter.method_id}
```

- [ ] **Step 2: Verify RED**

Expected: source-specific modules are absent.

- [ ] **Step 3: Implement coverage dataclass and adapters**

Each adapter hardcodes only its source paths and expected method ID. Coverage
is loaded from the source bank's `export/coverage_map.json`; exact mapping
status and clauses are asserted. Rows are passed through unchanged except for
numeric normalization performed by `EpisodeRow`.

- [ ] **Step 4: Assert source immutability**

Record SHA-256 for coverage and export files before and after the complete test.
The test must compare bytes, not modification time.

- [ ] **Step 5: Verify GREEN**

Expected: all three real mock exports load and source hashes remain identical.

- [ ] **Step 6: Checkpoint without committing**

Do not modify any upstream bank to make an adapter pass.

## Task 5: Create-only source lock and evidence snapshot

**Files:**
- Create: `src/corinthlove_suite/evidence.py`
- Create: `src/corinthlove_suite/cli.py`
- Create: `tests/test_evidence_snapshot.py`
- Generate: `registry/sources.lock.json`

- [ ] **Step 1: Write failing evidence tests**

```python
import json
from pathlib import Path
import pytest
from corinthlove_suite.evidence import create_snapshot, verify_snapshot

def test_snapshot_is_create_only_and_whole_root_closed(tmp_path):
    root = tmp_path / "snapshot"
    create_snapshot(root, provenance="harness validation, NOT a measurement")
    assert verify_snapshot(root)["valid"] is True
    with pytest.raises(FileExistsError):
        create_snapshot(root, provenance="harness validation, NOT a measurement")
    (root / "extra.json").write_text("{}")
    with pytest.raises(ValueError, match="extra"):
        verify_snapshot(root)

def test_source_drift_invalidates_snapshot(tmp_path):
    root = tmp_path / "snapshot"
    create_snapshot(root, provenance="harness validation, NOT a measurement")
    manifest = json.loads((root / "manifest.json").read_text())
    manifest["sources"][0]["sha256"] = "0" * 64
    (root / "manifest.json").write_text(json.dumps(manifest, sort_keys=True) + "\n")
    with pytest.raises(ValueError):
        verify_snapshot(root)
```

- [ ] **Step 2: Verify RED**

Expected: evidence functions are absent.

- [ ] **Step 3: Implement create-only canonical artifacts**

Use `open(path, "xb")`, canonical sorted JSON plus newline, SHA-256 journal
entries, normalized relative paths, symlink rejection, exact file closure, and
source-hash replay. Copy no source rows into the manifest; store inventories and
hashes only.

- [ ] **Step 4: Add `freeze-sources` and `verify-snapshot` CLI commands**

```sh
python -m corinthlove_suite.cli freeze-sources --out registry/sources.lock.json
python -m corinthlove_suite.cli verify-snapshot --root snapshots/tier0-v1
```

`freeze-sources` must refuse to overwrite an existing lock. Generate it once,
review every path/hash, and bind it in the snapshot manifest.

- [ ] **Step 5: Verify GREEN**

Expected: evidence tests pass and no upstream file changes.

- [ ] **Step 6: Checkpoint without committing**

Run `git status --short` and confirm all changes are confined to the new root.

## Task 6: Consolidated export and profile builder

**Files:**
- Create: `src/corinthlove_suite/export.py`
- Create: `src/corinthlove_suite/profiles.py`
- Create: `tests/test_consolidated_export.py`

- [ ] **Step 1: Write failing export tests**

```python
from corinthlove_suite.export import build_tier0_export
from corinthlove_suite.profiles import build_profiles

def test_tier0_export_preserves_method_namespaces(tmp_path):
    result = build_tier0_export(tmp_path / "rows.jsonl")
    assert result["methods"] == ["01-crossroads", "charitroc", "dimglass"]
    assert result["provenance"] == "harness validation, NOT a measurement"
    assert result["duplicate_key_count"] == 0
    profiles = build_profiles(tmp_path / "rows.jsonl")
    assert set(profiles["native"]) == {"01-crossroads"}
    assert set(profiles["crosswalk_mapped"]) == {"charitroc", "dimglass"}
```

- [ ] **Step 2: Verify RED**

Expected: export/profile modules are absent.

- [ ] **Step 3: Implement deterministic merge**

Sort rows by `(method_id, model_id, item_id, clause, rung, judge_ids)`. Reject
exact duplicates and conflicting rows sharing `(method_id, model_id, item_id,
clause, rung)`. Write canonical JSONL create-only and return counts by method,
model, clause, and provenance.

- [ ] **Step 4: Implement separate profile namespaces**

Aggregate native rows only into C1–C16 profiles. Aggregate crosswalk rows under
their family codes. Each cell carries mean score, `n_items`, and `ci: null` for
mock Tier-0 data. Never emit an overall scalar.

- [ ] **Step 5: Verify GREEN**

Expected: export tests pass; source banks remain byte-identical.

- [ ] **Step 6: Checkpoint without committing**

Run focused tests and inspect the first and last 20 emitted rows.

## Task 7: Panel and qualification diagnostics

**Files:**
- Create: `src/corinthlove_suite/qualification.py`
- Create: `tests/test_qualification.py`

- [ ] **Step 1: Write failing panel/provenance tests**

```python
import pytest
from corinthlove_suite.qualification import validate_panel, score_support

def test_formal_panel_requires_eight_models_three_vendors_three_tiers():
    with pytest.raises(ValueError, match="eight"):
        validate_panel({"formal_inference": True, "models": []})

def test_cheap_panel_cannot_authorize_formal_analysis():
    panel = {"formal_inference": False, "models": ["a", "b", "c", "d"]}
    with pytest.raises(ValueError, match="formal"):
        validate_panel(panel, require_formal=True)

def test_score_support_reports_floor_ceiling_without_ranking():
    report = score_support([0.0, 0.0, 1.0, 2.0])
    assert report == {"n": 4, "minimum": 0.0, "maximum": 2.0,
                      "floor_rate": 0.5, "ceiling_rate": 0.25}
```

- [ ] **Step 2: Verify RED**

- [ ] **Step 3: Implement strict panel validation**

Formal panels require explicit model alias, vendor, tier, snapshot, prompt hash,
configuration hash, and authorization. Cheap panels reject `require_formal`.
Do not populate the formal registry in this task.

- [ ] **Step 4: Implement method-local diagnostics**

Return row counts, missingness, unique score support, floor/ceiling occupancy,
model dispersion, judge/mechanical channels, and provenance. Do not compute an
overall ranking or combine method scales.

- [ ] **Step 5: Verify GREEN and checkpoint**

Expected: qualification tests pass; no live client exists in the package.

## Task 8: L1 concordance with reliability and exact inference

**Files:**
- Create: `src/corinthlove_suite/concordance.py`
- Create: `fixtures/l1_known_profiles.json`
- Create: `tests/test_concordance.py`

- [ ] **Step 1: Add hand-computable failing tests**

```python
import numpy as np
from corinthlove_suite.concordance import (
    spearman_brown, kendalls_w, pairwise_spearman, exact_label_permutation
)

def test_spearman_brown():
    assert spearman_brown(0.5) == 2 * 0.5 / 1.5

def test_kendalls_w_perfect_agreement():
    ranks = np.array([[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]])
    assert kendalls_w(ranks) == 1.0

def test_pairwise_spearman_reverses_sign():
    assert pairwise_spearman([1, 2, 3, 4], [4, 3, 2, 1]) == -1.0

def test_exact_permutation_is_deterministic():
    result = exact_label_permutation([1, 2, 3], [1, 2, 3])
    assert result["permutations"] == 6
    assert 0.0 < result["p_one_sided"] <= 1.0
```

- [ ] **Step 2: Verify RED**

- [ ] **Step 3: Implement statistics without latent modeling**

Use SciPy rank functions with explicit tie handling. Kendall's W accepts a
method × model rank matrix and applies the standard tie correction. Exact
permutation enumerates all permutations when `n! <= 10000`; otherwise use a
fixed-seed 10,000-permutation Monte Carlo path and record the seed.

- [ ] **Step 4: Add reliability and disattenuation**

Split items deterministically by stable item hash, compute half correlations,
apply Spearman–Brown, and report raw plus `raw / sqrt(rel_a * rel_b)` capped to
[-1, 1]. Never replace raw results with corrected results.

- [ ] **Step 5: Add the known-profile fixture**

Create three native mock methods × eight mock models × four clauses with two
perfectly concordant clauses, one moderate clause, and one reversed clause.
Label the fixture `harness validation, NOT a measurement` and assert exact
expected bands.

- [ ] **Step 6: Verify GREEN and checkpoint**

Expected: all L1 tests pass deterministically on repeated runs.

## Task 9: L2 clause structure and fallback decision

**Files:**
- Create: `src/corinthlove_suite/clause_structure.py`
- Create: `fixtures/l2_clause.jsonl`
- Create: `fixtures/l2_family.jsonl`
- Create: `fixtures/l2_factor.jsonl`
- Create: `tests/test_clause_structure.py`

- [ ] **Step 1: Write failing fallback tests**

```python
from corinthlove_suite.clause_structure import choose_reporting_level

def test_clause_structure_stands_when_registered_rules_pass():
    assert choose_reporting_level(clause_p=0.01, discriminant_rows=14,
                                  family_p=0.01) == "clause"

def test_family_fallback_when_clause_rule_fails():
    assert choose_reporting_level(clause_p=0.20, discriminant_rows=8,
                                  family_p=0.01) == "family"

def test_factor_fallback_when_both_structures_fail():
    assert choose_reporting_level(clause_p=0.20, discriminant_rows=8,
                                  family_p=0.30) == "factor-plus-c1"
```

- [ ] **Step 2: Verify RED**

- [ ] **Step 3: Implement residual and contrast functions**

For measurement rows only, subtract model × method cell means, rank-transform
ordinal values, compute the residual clause correlation matrix, and calculate
mean within-block minus mean between-block correlation for both registered
blockings. Reject cells with insufficient observations rather than imputing.

- [ ] **Step 4: Implement fixed-seed within-cell permutation inference**

Permute episode residuals within model × method cells, use 10,000 permutations,
record the seed and valid-permutation count, and require exact source-row hashes.

- [ ] **Step 5: Add three synthetic fixtures**

The clause fixture must pass the 16-clause and 12-of-16 rules. The family
fixture must fail clause but pass family. The factor fixture must fail both.
All carry the exact mock label.

- [ ] **Step 6: Verify GREEN and checkpoint**

Expected: all three fallback outcomes are recovered.

## Task 10: CLI, report bundle, adversarial checks, and Tier-0 integration

**Files:**
- Create: `src/corinthlove_suite/report.py`
- Modify: `src/corinthlove_suite/cli.py`
- Create: `selfcheck.py`
- Create: `tests/test_cli.py`
- Create: `tests/test_integration_tier0.py`
- Create: `README.md`
- Create: `AGENTS.md`
- Create: `STATUS.md`
- Create: `DECISIONS.md`

- [ ] **Step 1: Write failing end-to-end tests**

```python
import json
from corinthlove_suite.cli import main

def test_tier0_build_and_verify(tmp_path):
    root = tmp_path / "tier0"
    assert main(["build-tier0", "--root", str(root)]) == 0
    assert main(["verify", "--root", str(root)]) == 0
    report = json.loads((root / "tier0_report.json").read_text())
    assert report["provenance"] == "harness validation, NOT a measurement"
    assert report["authorizes_live_calls"] is False
    assert report["authorizes_model_ranking"] is False
    assert set(report["methods"]) == {"dimglass", "charitroc", "01-crossroads"}

def test_cli_exposes_no_live_command():
    try:
        main(["run-live"])
    except SystemExit as error:
        assert error.code != 0
    else:
        raise AssertionError("live command unexpectedly exists")
```

- [ ] **Step 2: Verify RED**

- [ ] **Step 3: Implement only offline CLI commands**

Commands:

- `inventory`;
- `freeze-sources`;
- `build-tier0`;
- `verify`;
- `analyze-synthetic-l1`;
- `analyze-synthetic-l2`;
- `selfcheck`.

Every command emits canonical JSON. No module imports an HTTP client or reads an
API key.

- [ ] **Step 4: Build the report bundle**

The Tier-0 report contains source inventories, coverage classes, row counts,
profile namespaces, synthetic recovery results, exclusions, limitations, and
all authorization flags false. It contains no model leaderboard.

- [ ] **Step 5: Implement self-check and adversarial mutations**

Self-check must reject:

- source hash drift;
- an extra hidden field;
- a crosswalk row relabeled C1–C16;
- a mock row relabeled measurement;
- a cheap panel relabeled formal;
- a missing declared source;
- duplicate/conflicting rows;
- an unreferenced snapshot artifact;
- any credential-shaped key or value.

- [ ] **Step 6: Run focused and full verification**

Run:

```sh
PY=/Users/jimmy.lin/Documents/CEI-Literature-Vault/.venv/bin/python
$PY -m pytest tests/test_cli.py tests/test_integration_tier0.py -q
$PY -m pytest tests -q
$PY selfcheck.py
$PY -m corinthlove_suite.cli build-tier0 --root snapshots/20260711-tier0-v1
$PY -m corinthlove_suite.cli verify --root snapshots/20260711-tier0-v1
git diff --check
```

Expected: all tests pass; self-check reports every check PASS; the snapshot
verifies; no upstream file hash changes.

- [ ] **Step 7: Manual artifact audit**

Read all three coverage maps, the snapshot manifest, the first/last 20 rows per
method, native and crosswalk profile outputs, and the complete Tier-0 report.
Confirm labels, grammar, IDs, provenance, and authorization flags.

- [ ] **Step 8: Independent review and handoff**

Request a fresh adversarial review against the approved design. Apply only
safe conditional fixes, rerun the affected focused tests and one final full
suite, then write a dated handoff and update authoritative status/memory.

- [ ] **Step 9: Final checkpoint without committing**

Run `git status --short`, `git diff --check`, and a credential-pattern scan.
Do not stage, commit, push, or begin Tier 1.

## Plan self-review

- Spec coverage: Tasks 1–10 cover registry, adapters, evidence, export,
  profiles, panel separation, qualification, L1, L2, CLI, reporting, testing,
  and handoff.
- Placeholder scan: no unresolved markers, deferred work phrases, or
  unspecified error handling remains.
- Type consistency: `EpisodeRow`, method IDs, method classes, provenance
  strings, panel IDs, and file paths are consistent throughout.
- Scope: this plan produces a working offline Tier-0 suite. New native banks,
  formal panel selection, live execution, and property studies remain separate
  plans.
- Authorization: every checkpoint is no-commit and no-live, matching current
  user constraints.
