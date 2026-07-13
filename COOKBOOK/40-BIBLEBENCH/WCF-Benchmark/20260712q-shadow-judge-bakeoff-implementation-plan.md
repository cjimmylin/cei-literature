# Shadow Judge Bakeoff Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build and execute the approved $1-NTE shadow comparison of GLM 5.2 and DeepSeek
V4 Pro against immutable Gemini/Grok evidence without changing the qualification manifest,
candidate ladder, T4, or any score of record.

**Architecture:** Add one harness-root runner that composes the existing qualification
battery, parsers, scorer functions, OpenRouter client, retry/budget guard, and append-only
JSONL sink. Pure selection/report functions stay network-free; the live boundary is one
`execute_live()` function gated by exact-slug, key-credit, template-hash, output-path, and
$1-budget checks.

**Tech Stack:** Python 3.9, pytest, stdlib JSON/hashlib/argparse/time, existing `wcfbench`
modules, and the existing OpenRouter stdlib client.

---

## Execution context and fixed references

Project rules require the shared `main` worktree; do not create a separate worktree. Before
every commit run `git log -1`, stage only named WCF-Benchmark paths, and leave sibling
benchmark changes untouched.

Read before implementation:

- `AGENTS.md`
- `20260712n-shadow-judge-bakeoff-design.md`
- `20260712p-shadow-judge-bakeoff-design-amendment.md`
- `07-PILOTS/20260712-artifact-corrected-requal/20260712-artifact-corrected-requal-manifest.json`

## File map

- Create `04-HARNESS/shadow_judge_bakeoff.py`: configuration, pure selection, shadow
  scoring, qualification, live safety/accounting, report, and CLI.
- Create `04-HARNESS/tests/test_shadow_judge_bakeoff.py`: hermetic TDD coverage for every
  approved boundary and output.
- Create only during live execution `07-PILOTS/20260712-shadow-judge-bakeoff/` with
  `selection.json`, `shadow-run-metadata.json`, `raw_verdicts.jsonl`, and the report.
- Update after execution only `PENDING-QUESTIONS.md`, `project-dashboard.html`, and
  `20260712s-codex-session31-handoff.md`. Do not edit execution-plan checkboxes.

### Task 1: Freeze configuration and deterministic sample selection

**Files:**
- Create: `04-HARNESS/tests/test_shadow_judge_bakeoff.py`
- Create: `04-HARNESS/shadow_judge_bakeoff.py`

- [ ] **Step 1: Write failing tests for roster, counts, source priority, and hash order**

```python
from __future__ import annotations

import hashlib
import importlib
import json


def _runner():
    return importlib.import_module("shadow_judge_bakeoff")


def _record(item_id, model, response, judges, *, kind="contested"):
    return {"item_id": item_id, "model": model, "sut_response": response,
            "kind": kind, "template_hash": "47ddb41c355fbf57", "judges": judges}


def test_fixed_shadow_roster_counts_and_budget():
    r = _runner()
    assert r.CANDIDATES == (
        ("glm-5.2", "z-ai", "z-ai/glm-5.2"),
        ("deepseek-v4-pro", "deepseek", "deepseek/deepseek-v4-pro"),
    )
    assert r.SURFACE_COUNTS == {
        "open_award": 8, "coherence": 8, "disclosure": 6, "settled_core": 6}
    assert r.MAX_BUDGET == 1.0


def test_contested_source_priority_never_joins_a_different_response():
    r = _runner()
    floor = [
        _record("A", "llama", "floor A", [{"name": "gemini-flash", "scores": {}}]),
        _record("B", "llama", "floor B", [{"name": "grok-4.20", "scores": {}}]),
        _record("C", "deepseek", None, []),
    ]
    r33 = [
        _record("A", "llama", "different A", [{"name": "gemini-flash", "scores": {}}]),
        _record("C", "deepseek", "r33 C", [{"name": "gemini-flash", "scores": {}}]),
    ]
    chosen = r.select_contested_records(floor, r33, expected=3)
    by_key = {(x["item_id"], x["model"]): x for x in chosen}
    assert by_key[("A", "llama")]["sut_response"] == "floor A"
    assert by_key[("C", "deepseek")]["sut_response"] == "r33 C"


def test_seeded_surface_order_is_sha256_and_exact_count():
    r = _runner()
    rows = [_record(f"I{i}", f"M{i}", f"R{i}", [], kind="open") for i in range(12)]
    got = r.take_seeded("open_award", rows, 8)
    expected = sorted(rows, key=lambda x: hashlib.sha256(
        f"1647|open_award|{x['item_id']}|{x['model']}".encode()).hexdigest())[:8]
    assert [(x["item_id"], x["model"]) for x in got] == [
        (x["item_id"], x["model"]) for x in expected]
```

- [ ] **Step 2: Run tests and verify RED**

```bash
cd /Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/WCF-Benchmark/04-HARNESS
/Users/jimmy.lin/Documents/CEI-Literature-Vault/.venv/bin/python -m pytest tests/test_shadow_judge_bakeoff.py -q
```

Expected: import failure because `shadow_judge_bakeoff.py` does not exist.

- [ ] **Step 3: Implement constants and pure selection helpers**

```python
from __future__ import annotations

import argparse
import datetime
import hashlib
import json
import os
import sys
import time
from dataclasses import dataclass
from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple

from format_bridge_requal import (
    BudgetGuard, CapturingClient, JsonlSink, OutputPathError, PreflightError,
    fetch_with_two_retries, require_preflight,
)
from wcfbench import load_items
from wcfbench import mvp
from wcfbench.contested import _score_disclosure, score_settled_core
from wcfbench.judge import (
    award_emission_count, build_award_prompt, complete_with_retry,
    parse_award_verdict, willingness_to_grade,
)
from wcfbench.openrouter_client import OpenRouterModelClient
from wcfbench.qualification import (
    DEFAULT_K, DEFAULT_THRESHOLD, PROBES, JudgeQualification,
    current_template_hashes, load_manifest, qualify_judge,
)
from wcfbench.triaxial import AXES, TriaxialScore, _score_numeric_axis

HERE = os.path.dirname(os.path.abspath(__file__))
PROJECT = os.path.normpath(os.path.join(HERE, ".."))
RUN_DIR = os.path.join(PROJECT, "07-PILOTS", "20260712-shadow-judge-bakeoff")
MANIFEST_PATH = os.path.join(PROJECT, "07-PILOTS", "20260712-artifact-corrected-requal",
                             "20260712-artifact-corrected-requal-manifest.json")
OPEN_PATH = os.path.join(PROJECT, "07-PILOTS", "20260712-mvp-open-reparse",
                         "corrected-open-transcripts.jsonl")
FLOOR_PATH = os.path.join(PROJECT, "07-PILOTS", "20260710-floor-rerun", "transcripts.jsonl")
R33_PATH = os.path.join(PROJECT, "07-PILOTS", "20260710-r33-3judge", "transcripts.jsonl")
BANK_DIR = os.path.join(PROJECT, "05-BANK-YAML")

CANDIDATES = (
    ("glm-5.2", "z-ai", "z-ai/glm-5.2"),
    ("deepseek-v4-pro", "deepseek", "deepseek/deepseek-v4-pro"),
)
SURFACE_COUNTS = {"open_award": 8, "coherence": 8, "disclosure": 6, "settled_core": 6}
K = DEFAULT_K
THRESHOLD = DEFAULT_THRESHOLD
MAX_BUDGET = 1.0
JUDGE_MAX_TOKENS = 2048
SEED = 1647


def read_jsonl(path: str) -> List[Dict[str, Any]]:
    with open(path, encoding="utf-8") as fh:
        return [json.loads(line) for line in fh if line.strip()]


def _usable(record: Dict[str, Any]) -> bool:
    return bool(record.get("sut_response")) and bool(record.get("judges"))


def select_contested_records(floor, r33, *, expected=6):
    chosen = {}
    for source_name, records in (("floor-rerun", floor), ("r33-3judge", r33)):
        for record in records:
            if record.get("kind") != "contested" or not _usable(record):
                continue
            key = (str(record["item_id"]), str(record["model"]))
            if key not in chosen:
                copied = dict(record)
                copied["source_run"] = source_name
                chosen[key] = copied
    if len(chosen) != expected:
        raise PreflightError(f"expected {expected} unique contested units, found {len(chosen)}")
    return [chosen[key] for key in sorted(chosen)]


def take_seeded(surface, rows, count):
    ordered = sorted(rows, key=lambda row: hashlib.sha256(
        f"{SEED}|{surface}|{row['item_id']}|{row['model']}".encode()).hexdigest())
    if len(ordered) < count:
        raise PreflightError(f"{surface}: need {count} units, found {len(ordered)}")
    return ordered[:count]
```

- [ ] **Step 4: Run Task-1 tests and verify GREEN**

- [ ] **Step 5: Commit Task 1**

```bash
git log -1 --oneline
git add -- 04-HARNESS/shadow_judge_bakeoff.py 04-HARNESS/tests/test_shadow_judge_bakeoff.py
git commit -m "WCF-Bench: add shadow bakeoff selection"
```

### Task 2: Materialize and persist the exact 8/8/6/6 selection

**Files:**
- Modify: `04-HARNESS/tests/test_shadow_judge_bakeoff.py`
- Modify: `04-HARNESS/shadow_judge_bakeoff.py`

- [ ] **Step 1: Add failing selection-materialization tests**

```python
def test_build_selection_has_exact_counts_and_response_hashes():
    r = _runner()
    selection = r.build_selection(open_path=r.OPEN_PATH, floor_path=r.FLOOR_PATH,
                                  r33_path=r.R33_PATH, bank_dir=r.BANK_DIR)
    assert {s: sum(x["surface"] == s for x in selection) for s in r.SURFACE_COUNTS} == r.SURFACE_COUNTS
    assert len(selection) == 28
    assert all(x["response_sha256"] == hashlib.sha256(
        x["sut_response"].encode()).hexdigest() for x in selection)


def test_write_selection_is_create_new(tmp_path):
    r = _runner()
    path = tmp_path / "selection.json"
    r.write_json_new(str(path), {"surface_counts": r.SURFACE_COUNTS, "units": []})
    assert json.loads(path.read_text())["surface_counts"] == r.SURFACE_COUNTS
    import pytest
    with pytest.raises(FileExistsError):
        r.write_json_new(str(path), {"units": []})
```

- [ ] **Step 2: Run and verify RED for missing functions**

- [ ] **Step 3: Implement selection materialization**

```python
def _judges_by_name(record):
    return {str(j["name"]): j for j in record.get("judges", [])}


def _unit(surface, record, *, axis=None):
    response = str(record["sut_response"])
    return {"surface": surface, "item_id": str(record["item_id"]),
            "sut_slug": str(record["model"]), "sut_response": response,
            "response_sha256": hashlib.sha256(response.encode()).hexdigest(),
            "source_run": record.get("source_run", "corrected-mvp-open-reparse"),
            "axis": axis, "comparators": _judges_by_name(record)}


def build_selection(*, open_path, floor_path, r33_path, bank_dir):
    items = {item.id: item for item in load_items(bank_dir)}
    open_rows = [row for row in read_jsonl(open_path) if row.get("kind") == "open"]
    award_rows, coherence_rows = [], []
    for row in open_rows:
        judges = _judges_by_name(row)
        if not {"gemini-flash", "grok-4.20"}.issubset(judges):
            continue
        if all(judges[n].get("scores", {}).get("awards") for n in ("gemini-flash", "grok-4.20")):
            award_rows.append(row)
        item = items[row["item_id"]]
        untagged = [a for a in AXES if not any(getattr(kp, "axis", None) == a for kp in item.rubric)]
        if len(untagged) == 1 and all(judges[n].get("scores", {}).get(untagged[0]) is not None
                                      for n in ("gemini-flash", "grok-4.20")):
            copied = dict(row)
            copied["numeric_axis"] = untagged[0]
            coherence_rows.append(copied)
    selected = [_unit("open_award", row) for row in take_seeded("open_award", award_rows, 8)]
    selected += [_unit("coherence", row, axis=row["numeric_axis"])
                 for row in take_seeded("coherence", coherence_rows, 8)]
    contested = select_contested_records(read_jsonl(floor_path), read_jsonl(r33_path))
    selected += [_unit("disclosure", row) for row in contested]
    selected += [_unit("settled_core", row) for row in contested]
    return selected


def write_json_new(path, value):
    with open(path, "x", encoding="utf-8") as fh:
        json.dump(value, fh, indent=2, sort_keys=True)
```

- [ ] **Step 4: Run focused tests and verify GREEN**

- [ ] **Step 5: Commit Task 2**

```bash
git log -1 --oneline
git add -- 04-HARNESS/shadow_judge_bakeoff.py 04-HARNESS/tests/test_shadow_judge_bakeoff.py
git commit -m "WCF-Bench: freeze shadow comparison sample"
```

### Task 3: Add full six-probe qualification with no incumbent calls

**Files:**
- Modify: `04-HARNESS/tests/test_shadow_judge_bakeoff.py`
- Modify: `04-HARNESS/shadow_judge_bakeoff.py`

- [ ] **Step 1: Add failing full-battery and hash tests**

```python
def test_shadow_battery_calls_only_two_candidates():
    r = _runner()
    calls = []
    def fake(client, *, name, family, slug, k, threshold):
        calls.append((name, family, slug, k, threshold, client))
        return {"name": name}
    got = r.run_shadow_batteries(client_factory=lambda n, f, s: s, qualify_fn=fake)
    assert [x[:5] for x in calls] == [
        ("glm-5.2", "z-ai", "z-ai/glm-5.2", 8, 5),
        ("deepseek-v4-pro", "deepseek", "deepseek/deepseek-v4-pro", 8, 5)]
    assert set(got) == {"glm-5.2", "deepseek-v4-pro"}


def test_template_hash_mismatch_stops():
    r = _runner()
    import pytest
    with pytest.raises(r.PreflightError, match="template hash"):
        r.assert_template_hashes({"template_hashes": {"g4": "stale"}})
```

- [ ] **Step 2: Run and verify RED**

- [ ] **Step 3: Implement battery and probe persistence**

```python
def persist_probe_reps(sink, qualification, now):
    for probe in PROBES:
        for rep in qualification.probe_reps[probe].reps:
            sink.write({"kind": "probe_rep", "timestamp": now(),
                        "judge": qualification.name, "family": qualification.family,
                        "slug": qualification.slug, "probe": probe, **rep})


def run_shadow_batteries(*, client_factory, qualify_fn=qualify_judge,
                         sink=None, now=lambda: datetime.datetime.now().isoformat(timespec="seconds")):
    results = {}
    for name, family, slug in CANDIDATES:
        result = qualify_fn(client_factory(name, family, slug), name=name, family=family,
                            slug=slug, k=K, threshold=THRESHOLD)
        results[name] = result
        if sink is not None and isinstance(result, JudgeQualification):
            persist_probe_reps(sink, result, now)
    return results


def assert_template_hashes(manifest):
    if manifest.get("template_hashes") != current_template_hashes():
        raise PreflightError("qualification template hash mismatch; stop before spending")
```

- [ ] **Step 4: Run focused tests and verify GREEN**

- [ ] **Step 5: Commit Task 3**

```bash
git log -1 --oneline
git add -- 04-HARNESS/shadow_judge_bakeoff.py 04-HARNESS/tests/test_shadow_judge_bakeoff.py
git commit -m "WCF-Bench: add shadow judge qualification"
```

### Task 4: Score all 56 amended surface verdicts through existing contracts

**Files:**
- Modify: `04-HARNESS/tests/test_shadow_judge_bakeoff.py`
- Modify: `04-HARNESS/shadow_judge_bakeoff.py`

- [ ] **Step 1: Add failing surface-dispatch tests**

```python
def test_coherence_result_uses_exact_numeric_axis(monkeypatch):
    r = _runner()
    item = type("Item", (), {"id": "X", "stem": "stem", "rubric": []})()
    unit = {"surface": "coherence", "item_id": "X", "sut_response": "response", "axis": "end"}
    def fake(score, axis, **kwargs):
        setattr(score, axis, 0.75)
        score.graded[axis] = True
    monkeypatch.setattr(r, "_score_numeric_axis", fake)
    assert r.score_shadow_unit(unit, item, object()) == {
        "graded": True, "value": 0.75, "axis": "end", "scale_defect": False}


def test_all_four_surface_result_shapes(monkeypatch):
    r = _runner()
    item = type("Item", (), {"id": "X", "stem": "stem", "rubric": []})()
    monkeypatch.setattr(r, "complete_with_retry", lambda *a, **k: type(
        "Call", (), {"text": "KP1: award — reason", "discarded": False})())
    monkeypatch.setattr(r, "parse_award_verdict", lambda *a, **k: type(
        "Verdict", (), {"awards": {1: True}, "compliance_defects": {}})())
    open_result = r.score_shadow_unit(
        {"surface": "open_award", "sut_response": "r"}, item, object())
    assert set(open_result) == {"graded", "awards", "compliance_defects", "discarded"}

    monkeypatch.setattr(r, "_score_disclosure", lambda *a, **k: type(
        "Disc", (), {"graded": True, "value": 0.5, "awards": {},
                     "defects": {}, "discarded": False})())
    disc_result = r.score_shadow_unit(
        {"surface": "disclosure", "sut_response": "r"}, item, object())
    assert set(disc_result) == {"graded", "value", "awards", "defects", "discarded"}

    monkeypatch.setattr(r, "score_settled_core", lambda *a, **k: ({"kp": True}, [], "raw"))
    settled_result = r.score_shadow_unit(
        {"surface": "settled_core", "sut_response": "r"}, item, object())
    assert settled_result == {"graded": True, "keypoints": {"kp": True}, "reasonless": []}
```

- [ ] **Step 2: Run and verify RED**

- [ ] **Step 3: Implement scorer dispatch without new prompts or parsers**

```python
def score_shadow_unit(unit, item, judge):
    surface, response = unit["surface"], unit["sut_response"]
    if surface == "open_award":
        tagged = [kp for kp in item.rubric if getattr(kp, "axis", None) in AXES]
        prompt = build_award_prompt(stem=item.stem, rubric=item.rubric, response=response)
        call = complete_with_retry(judge, prompt, item_id=item.id,
            is_complete=lambda text: award_emission_count(text) >= len(tagged))
        if call.discarded or not willingness_to_grade(call.text):
            return {"graded": False, "awards": {}, "compliance_defects": {},
                    "discarded": call.discarded}
        verdict = parse_award_verdict(call.text, require_reason=True)
        return {"graded": bool(verdict.awards), "awards": verdict.awards,
                "compliance_defects": verdict.compliance_defects, "discarded": False}
    if surface == "coherence":
        axis = unit["axis"]
        score = TriaxialScore()
        _score_numeric_axis(score, axis, stem=item.stem, rubric=item.rubric,
                            response=response, judge=judge, item_id=item.id)
        return {"graded": bool(score.graded.get(axis)), "value": getattr(score, axis),
                "axis": axis, "scale_defect": bool(score.scale_defect.get(axis))}
    if surface == "disclosure":
        result = _score_disclosure(judge, item, response, item.id)
        return {"graded": result.graded, "value": result.value,
                "awards": result.awards, "defects": result.defects,
                "discarded": result.discarded}
    if surface == "settled_core":
        values, reasonless, _text = score_settled_core(judge, item, response, item.id)
        return {"graded": bool(values), "keypoints": values, "reasonless": reasonless}
    raise ValueError(f"unknown shadow surface {surface!r}")
```

- [ ] **Step 4: Implement error-surviving, latency-bearing verdict persistence**

```python
def run_shadow_units(selection, *, clients, items, sink, now, clock=time.perf_counter):
    results = []
    for name, _family, _slug in CANDIDATES:
        for unit in selection:
            started, result, error = clock(), None, None
            try:
                result = score_shadow_unit(unit, items[unit["item_id"]], clients[name])
            except Exception as exc:
                error = f"{type(exc).__name__}: {exc}"
            record = {"kind": "shadow_verdict", "timestamp": now(), "judge": name,
                      "surface": unit["surface"], "item_id": unit["item_id"],
                      "sut_slug": unit["sut_slug"],
                      "response_sha256": unit["response_sha256"],
                      "elapsed_seconds": max(0.0, clock() - started),
                      "result": result, "error": error}
            sink.write(record)
            results.append(record)
    return results
```

- [ ] **Step 5: Add exact-count/error-survival test and verify GREEN**

```python
def test_shadow_loop_records_exactly_56_results_and_survives_errors(monkeypatch, tmp_path):
    r = _runner()
    selection = [{"surface": s, "item_id": f"{s}-{i}", "sut_slug": "sut",
                  "sut_response": "r", "response_sha256": "h", "axis": "end"}
                 for s, n in r.SURFACE_COUNTS.items() for i in range(n)]
    items = {u["item_id"]: object() for u in selection}
    monkeypatch.setattr(r, "score_shadow_unit", lambda unit, item, judge:
                        (_ for _ in ()).throw(ValueError("bad")) if unit["item_id"].endswith("-0")
                        else {"graded": True})
    sink = r.JsonlSink(str(tmp_path / "raw.jsonl"))
    sink.touch()
    got = r.run_shadow_units(selection, clients={"glm-5.2": object(),
        "deepseek-v4-pro": object()}, items=items, sink=sink,
        now=lambda: "2026-07-12T00:00:00", clock=lambda: 1.0)
    assert len(got) == 56
    assert sum(x["error"] is not None for x in got) == 8
```

- [ ] **Step 6: Commit Task 4**

```bash
git log -1 --oneline
git add -- 04-HARNESS/shadow_judge_bakeoff.py 04-HARNESS/tests/test_shadow_judge_bakeoff.py
git commit -m "WCF-Bench: add shadow surface scoring"
```

### Task 5: Add strict live safety and append-only artifacts

**Files:**
- Modify: `04-HARNESS/tests/test_shadow_judge_bakeoff.py`
- Modify: `04-HARNESS/shadow_judge_bakeoff.py`

- [ ] **Step 1: Add failing exact-slug and budget tests**

```python
def test_exact_candidates_have_no_alias_or_fallback():
    r = _runner()
    catalog = {slug: {"pricing": {"prompt": "0", "completion": "0"}}
               for _name, _family, slug in r.CANDIDATES}
    assert r.resolve_candidates(catalog) == r.CANDIDATES
    import pytest
    with pytest.raises(r.mvp.SlugValidationError):
        r.resolve_candidates({"z-ai/glm-4.5-air": {}, "deepseek/deepseek-chat": {}})


def test_budget_above_one_dollar_is_rejected():
    r = _runner()
    import pytest
    with pytest.raises(r.PreflightError):
        r.validate_options(1.01)
    r.validate_options(1.0)
```

- [ ] **Step 2: Implement exact resolution and bounds**

```python
def resolve_candidates(catalog):
    slugs = [slug for _name, _family, slug in CANDIDATES]
    mvp.validate_slugs(slugs, catalog)
    for slug in slugs:
        mvp.price_for(slug, catalog)
    return CANDIDATES


def validate_options(budget):
    if budget <= 0 or budget > MAX_BUDGET:
        raise PreflightError(
            f"shadow budget must be >$0 and <=${MAX_BUDGET:.2f}; received ${budget:.2f}")


def write_text_new(path, text):
    with open(path, "x", encoding="utf-8") as fh:
        fh.write(text)
```

- [ ] **Step 3: Add mock-live tests proving selection precedes calls and every call has latency**

```python
def test_selection_precedes_calls_latency_is_per_attempt_and_no_manifest(tmp_path):
    r = _runner()
    out_dir = tmp_path / "shadow"
    first_call_saw_selection = []

    class FakeClient:
        def __init__(self, model, **kwargs):
            self.model, self.max_tokens = model, kwargs["max_tokens"]
            self.usage_log = []
            self.last_finish_reason, self.last_truncated = "stop", False
        def complete(self, prompt, item_id=None):
            first_call_saw_selection.append((out_dir / "selection.json").exists())
            self.usage_log.append({"usage": {"prompt_tokens": 1,
                "completion_tokens": 1, "cost": 0.001}})
            return "SCORE: 1.0"

    snapshots = iter([{"usage": 1.0, "limit_remaining": 9.0},
                      {"usage": 1.002, "limit_remaining": 8.998}])
    catalog = {slug: {"pricing": {"prompt": "0.000001", "completion": "0.000001"}}
               for _name, _family, slug in r.CANDIDATES}
    selection = [{"surface": "coherence", "item_id": "X", "sut_slug": "sut",
                  "sut_response": "r", "response_sha256": "h", "axis": "end",
                  "comparators": {}}]
    def fake_qualify(client, *, name, family, slug, k, threshold):
        client.complete("probe", item_id="PROBE")
        return {"name": name}

    r.execute_live("secret", out_dir=str(out_dir), budget=1.0,
        key_fetch=lambda _key: next(snapshots), catalog_fetch=lambda _key: catalog,
        client_builder=FakeClient, qualify_fn=fake_qualify,
        selection_fn=lambda **_kwargs: selection,
        score_fn=lambda *_args, **_kwargs: [],
        now=lambda: "2026-07-12T00:00:00")
    assert first_call_saw_selection and all(first_call_saw_selection)
    assert not any("manifest" in path.name.lower() for path in out_dir.iterdir())
    assert json.loads((out_dir / "shadow-run-metadata.json").read_text())[
        "artifact_kind"] == "SHADOW / NOT A QUALIFICATION MANIFEST"
    raw = [json.loads(line) for line in (out_dir / "raw_verdicts.jsonl").read_text().splitlines()]
    assert sum(x["kind"] == "call_timing" for x in raw) == sum(
        x["kind"] == "raw_call" for x in raw)
    assert all(x["elapsed_seconds"] >= 0 for x in raw if x["kind"] == "call_timing")
```

The test injects qualification and scoring seams only; production defaults remain the full
battery and 56-verdict loop.

- [ ] **Step 4: Implement the per-call timing adapter**

```python
class TimingClient:
    def __init__(self, inner, *, name, slug, sink, now, clock=time.perf_counter):
        self.inner, self.name, self.slug = inner, name, slug
        self.sink, self.now, self.clock = sink, now, clock

    def __getattr__(self, name):
        return getattr(self.inner, name)

    def complete(self, prompt, item_id=None):
        started, error = self.clock(), None
        try:
            return self.inner.complete(prompt, item_id=item_id)
        except Exception as exc:
            error = f"{type(exc).__name__}: {exc}"
            raise
        finally:
            self.sink.write({"kind": "call_timing", "timestamp": self.now(),
                             "judge": self.name, "slug": self.slug,
                             "item_id": item_id,
                             "elapsed_seconds": max(0.0, self.clock() - started),
                             "error": error})
```

- [ ] **Step 5: Implement metadata and the live boundary**

```python
@dataclass
class ShadowOutcome:
    paths: Dict[str, str]
    qualifications: Dict[str, Any]
    verdicts: List[Dict[str, Any]]
    internal_total_usd: float
    partial_reason: Optional[str]


def build_metadata(*, catalog, budget, internal_total, partial_reason,
                   qualifications, verdicts, key_before, key_after):
    return {"artifact_kind": "SHADOW / NOT A QUALIFICATION MANIFEST",
            "candidates": [{"name": n, "family": f, "slug": s,
                            "pricing": catalog[s].get("pricing", {})}
                           for n, f, s in CANDIDATES],
            "k": K, "threshold": THRESHOLD, "surface_counts": SURFACE_COUNTS,
            "budget_usd": budget, "internal_total_usd": internal_total,
            "partial_reason": partial_reason,
            "qualification_complete": len(qualifications) == 2,
            "shadow_verdicts_recorded": len(verdicts),
            "key_before": key_before, "key_after": key_after}


def build_report(metadata, qualifications, verdicts, selection):
    return "\n".join([
        "# WCF-Bench — Shadow Judge Bakeoff", "",
        "**SHADOW / NOT A QUALIFICATION MANIFEST**", "",
        f"partial_reason: {metadata.get('partial_reason')}", "",
    ])


def execute_live(api_key, *, out_dir=RUN_DIR, budget=MAX_BUDGET,
                 key_fetch=mvp.fetch_key_snapshot, catalog_fetch=mvp.fetch_model_catalog,
                 client_builder=OpenRouterModelClient, qualify_fn=qualify_judge,
                 selection_fn=build_selection, score_fn=run_shadow_units,
                 now=lambda: datetime.datetime.now().isoformat(timespec="seconds")):
    validate_options(budget)
    if os.path.exists(out_dir):
        raise OutputPathError(f"append-only output path already exists: {out_dir}")
    key_before = fetch_with_two_retries(key_fetch, api_key)
    require_preflight(key_before, budget)
    catalog = fetch_with_two_retries(catalog_fetch, api_key)
    resolve_candidates(catalog)
    assert_template_hashes(load_manifest(MANIFEST_PATH))
    selection = selection_fn(open_path=OPEN_PATH, floor_path=FLOOR_PATH,
                             r33_path=R33_PATH, bank_dir=BANK_DIR)
    os.makedirs(out_dir, exist_ok=False)
    selection_path = os.path.join(out_dir, "selection.json")
    raw_path = os.path.join(out_dir, "raw_verdicts.jsonl")
    write_json_new(selection_path, {"seed": SEED, "surface_counts": SURFACE_COUNTS,
                                    "units": selection})
    sink = JsonlSink(raw_path)
    sink.touch()
    guard, clients = BudgetGuard(budget, catalog), {}
    for name, family, slug in CANDIDATES:
        inner = client_builder(model=slug, api_key=api_key, temperature=0.0,
                               max_tokens=JUDGE_MAX_TOKENS)
        guard.register(slug, inner)
        timed = TimingClient(inner, name=name, slug=slug, sink=sink, now=now)
        captured = CapturingClient(timed, name=name, family=family, slug=slug,
                                   guard=guard, sink=sink, now=now)
        clients[name] = captured
    qualifications, verdicts, partial_reason = {}, [], None
    try:
        qualifications = run_shadow_batteries(
            client_factory=lambda name, _family, _slug: clients[name],
            qualify_fn=qualify_fn, sink=sink, now=now)
        items = {item.id: item for item in load_items(BANK_DIR)}
        verdicts = score_fn(selection, clients=clients, items=items, sink=sink, now=now)
    except Exception as exc:
        partial_reason = f"{type(exc).__name__}: {exc}"
    internal = guard.total_usd()
    try:
        key_after = fetch_with_two_retries(key_fetch, api_key)
    except Exception:
        key_after = None
    metadata = build_metadata(catalog=catalog, budget=budget, internal_total=internal,
        partial_reason=partial_reason, qualifications=qualifications, verdicts=verdicts,
        key_before=key_before, key_after=key_after)
    metadata_path = os.path.join(out_dir, "shadow-run-metadata.json")
    report_path = os.path.join(out_dir, "20260712-shadow-judge-bakeoff-report.md")
    write_json_new(metadata_path, metadata)
    write_text_new(report_path, build_report(metadata, qualifications, verdicts, selection))
    paths = {"selection": selection_path, "raw": raw_path,
             "metadata": metadata_path, "report": report_path}
    return ShadowOutcome(paths, qualifications, verdicts, internal, partial_reason)
```

- [ ] **Step 6: Run focused tests and commit Task 5**

```bash
git log -1 --oneline
git add -- 04-HARNESS/shadow_judge_bakeoff.py 04-HARNESS/tests/test_shadow_judge_bakeoff.py
git commit -m "WCF-Bench: enforce shadow run safety"
```

### Task 6: Add descriptive agreement, Pareto reporting, and CLI

**Files:**
- Modify: `04-HARNESS/tests/test_shadow_judge_bakeoff.py`
- Modify: `04-HARNESS/shadow_judge_bakeoff.py`

- [ ] **Step 1: Add failing report and dry-run tests**

```python
def test_report_forbids_accuracy_and_production_effect():
    r = _runner()
    report = r.build_report(
        {"artifact_kind": "SHADOW / NOT A QUALIFICATION MANIFEST",
         "internal_total_usd": 0.2, "partial_reason": None,
         "analysis": {"qualification": {}, "agreement": [], "operations": {},
                      "pareto_names": []}}, {}, [], [])
    assert "SHADOW / NOT A QUALIFICATION MANIFEST" in report
    assert "PARETO" in report
    assert "more accurate" not in report.lower()
    assert "production judge" not in report.lower()


def test_dry_run_has_zero_network_and_creates_no_directory(tmp_path, monkeypatch):
    r = _runner()
    monkeypatch.setattr(r, "RUN_DIR", str(tmp_path / "shadow"))
    monkeypatch.setattr(r.mvp, "fetch_key_snapshot", lambda *_a, **_k: 1 / 0)
    assert r.main([]) == 0
    assert not (tmp_path / "shadow").exists()
```

- [ ] **Step 2: Implement comparator normalization and agreement**

```python
def comparator_value(surface, comparator, unit):
    scores = comparator.get("scores", {})
    if surface == "open_award":
        return {int(k): bool(v) for k, v in scores.get("awards", {}).items()}
    if surface == "coherence":
        return scores.get(unit["axis"])
    if surface == "disclosure":
        return scores.get("disclosure")
    if surface == "settled_core":
        return scores.get("settled_core")
    raise ValueError(surface)


def agreement(candidate, comparator):
    if isinstance(candidate, dict) and isinstance(comparator, dict):
        keys = sorted(set(candidate) & set(comparator), key=str)
        return {"exact": bool(keys) and all(candidate[k] == comparator[k] for k in keys),
                "component_agreement": (sum(candidate[k] == comparator[k] for k in keys) /
                                        len(keys) if keys else None),
                "n_components": len(keys)}
    return {"exact": candidate == comparator,
            "component_agreement": float(candidate == comparator), "n_components": 1}
```

- [ ] **Step 3: Implement mechanical agreement and operational summaries**

```python
def candidate_value(surface, result):
    if surface == "open_award":
        return result.get("awards")
    if surface in {"coherence", "disclosure"}:
        return result.get("value")
    if surface == "settled_core":
        return result.get("keypoints")
    raise ValueError(surface)


def build_agreement_rows(selection, verdicts):
    units = {(u["surface"], u["item_id"], u["sut_slug"], u["response_sha256"]): u
             for u in selection}
    rows = []
    for verdict in verdicts:
        key = (verdict["surface"], verdict["item_id"], verdict["sut_slug"],
               verdict["response_sha256"])
        unit = units[key]
        if verdict.get("error") or not verdict.get("result", {}).get("graded"):
            continue
        value = candidate_value(verdict["surface"], verdict["result"])
        for comparator_name, comparator in unit["comparators"].items():
            if comparator_name not in {"gemini-flash", "grok-4.20"}:
                continue
            incumbent = comparator_value(verdict["surface"], comparator, unit)
            if incumbent is None:
                continue
            rows.append({"judge": verdict["judge"], "surface": verdict["surface"],
                         "comparator": comparator_name,
                         **agreement(value, incumbent)})
    return rows


def _row_cost(row, catalog):
    total = 0.0
    for entry in row.get("usage", []):
        usage = entry.get("usage", {})
        if usage.get("cost") not in (None, ""):
            total += float(usage["cost"])
        else:
            total += mvp.cell_cost(
                int(usage.get("prompt_tokens") or 0),
                int(usage.get("completion_tokens") or 0),
                mvp.price_for(row["slug"], catalog))
    return total


def operational_summary(raw_records, verdicts, catalog):
    by_judge = {}
    for name, _family, _slug in CANDIDATES:
        calls = [r for r in raw_records if r.get("kind") == "raw_call" and r.get("judge") == name]
        timings = [r["elapsed_seconds"] for r in raw_records
                   if r.get("kind") == "call_timing" and r.get("judge") == name]
        usage = [entry.get("usage", {}) for row in calls for entry in row.get("usage", [])]
        judged = [v for v in verdicts if v["judge"] == name]
        by_judge[name] = {
            "calls": len(calls),
            "retries": sum(int(row.get("attempt", 0)) > 0 for row in calls),
            "truncations": sum(bool(row.get("truncated")) for row in calls),
            "prompt_tokens": sum(int(u.get("prompt_tokens") or 0) for u in usage),
            "completion_tokens": sum(int(u.get("completion_tokens") or 0) for u in usage),
            "actual_cost_usd": sum(_row_cost(row, catalog) for row in calls),
            "mean_call_seconds": sum(timings) / len(timings) if timings else None,
            "parse_fraction": (sum(v.get("result", {}).get("graded") is True for v in judged) /
                               len(judged) if judged else 0.0),
            "errors": sum(v.get("error") is not None for v in judged),
        }
    return by_judge


def qualification_summary(qualifications):
    return {name: {
        "eligible_surfaces": sorted(q.surfaces),
        "probes": {probe: {"n_pass": reps.n_pass, "k": reps.k,
                            "cause_tally": reps.cause_tally()}
                   for probe, reps in q.probe_reps.items()}}
        for name, q in qualifications.items()}
```

- [ ] **Step 4: Implement labels, componentwise Pareto disclosure, and report**

```python
def candidate_labels(qualification, family, parse_fraction):
    labels = [(f"SHADOW-ELIGIBLE FOR {s}" if s in qualification.surfaces
               else f"SHADOW-INELIGIBLE FOR {s}") for s in SURFACE_COUNTS]
    if family in {"deepseek", "z-ai"}:
        labels.append("INDEPENDENCE-CONFLICTED")
    if parse_fraction == 0:
        labels.append("INSUFFICIENT EVIDENCE")
    return labels


def dominates(left, right):
    better_or_equal = (
        left["eligible_count"] >= right["eligible_count"] and
        left["parse_fraction"] >= right["parse_fraction"] and
        left["actual_cost_usd"] <= right["actual_cost_usd"] and
        left["independence_conflicts"] <= right["independence_conflicts"])
    strictly_better = (
        left["eligible_count"] > right["eligible_count"] or
        left["parse_fraction"] > right["parse_fraction"] or
        left["actual_cost_usd"] < right["actual_cost_usd"] or
        left["independence_conflicts"] < right["independence_conflicts"])
    return better_or_equal and strictly_better


def pareto_names(qualifications, operations):
    metrics = {}
    for name, family, _slug in CANDIDATES:
        q = qualifications[name]
        metrics[name] = {"eligible_count": len(q.surfaces),
                         "parse_fraction": operations[name]["parse_fraction"],
                         "actual_cost_usd": operations[name]["actual_cost_usd"],
                         "independence_conflicts": int(family in {"deepseek", "z-ai"})}
    return sorted(name for name in metrics
                  if not any(dominates(other, metrics[name])
                             for other_name, other in metrics.items() if other_name != name))


def build_report(metadata, qualifications, verdicts, selection):
    analysis = metadata["analysis"]
    lines = ["# WCF-Bench — Shadow Judge Bakeoff", "",
             "**SHADOW / NOT A QUALIFICATION MANIFEST**", "",
             "This descriptive report does not change T4, the panel, the manifest, "
             "the closed candidate ladder, or any score of record.", "",
             "## Scope", "", f"Surface denominators: `{SURFACE_COUNTS}`; seed {SEED}.", "",
             "## Qualification", "",
             "```json", json.dumps(analysis["qualification"], indent=2, sort_keys=True),
             "```", ""]
    for name, family, _slug in CANDIDATES:
        q = qualifications.get(name)
        if q is None:
            lines.append(f"- {name}: INSUFFICIENT EVIDENCE")
        else:
            lines.append(f"- {name}: surfaces={sorted(q.surfaces)}; "
                         f"labels={candidate_labels(q, family, 1.0)}")
    lines += ["", "## Real-response agreement", "",
              "Incumbent agreement is descriptive, not ground truth or accuracy.", "",
              "```json", json.dumps(analysis["agreement"], indent=2, sort_keys=True),
              "```", "", "## Operations", "",
              "```json", json.dumps(analysis["operations"], indent=2, sort_keys=True),
              "```", "",
              f"Internal actual/fallback cost: ${metadata.get('internal_total_usd', 0):.4f}.",
              "", "## PARETO recommendation", "",
              f"Non-dominated shadow candidates: {analysis['pareto_names']}.",
              "No weighted composite is used; no label authorizes production use.", ""]
    if metadata.get("partial_reason"):
        lines += [f"> PARTIAL / STOPPED: {metadata['partial_reason']}", ""]
    return "\n".join(lines)
```

- [ ] **Step 5: Wire analysis into metadata before writing artifacts**

Immediately after `internal = guard.total_usd()` in `execute_live()`:

```python
    raw_records = read_jsonl(raw_path)
    operations = operational_summary(raw_records, verdicts, catalog)
    analysis = {"qualification": qualification_summary(qualifications),
                "agreement": build_agreement_rows(selection, verdicts),
                "operations": operations,
                "pareto_names": (pareto_names(qualifications, operations)
                                 if len(qualifications) == 2 else [])}
```

Add `analysis` as a required `build_metadata()` parameter and store it under
`"analysis": analysis`. This makes the JSON metadata—not report prose—the canonical
machine-readable table.

- [ ] **Step 6: Implement CLI**

```python
def print_plan(budget):
    print("WCF-Bench shadow judge bakeoff — DRY RUN (0 network calls)")
    print(f"candidates={CANDIDATES}; K={K}; surfaces={SURFACE_COUNTS}; budget=${budget:.2f}")
    print(f"live output (created only with --go): {RUN_DIR}")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--go", action="store_true")
    parser.add_argument("--budget", type=float, default=MAX_BUDGET)
    args = parser.parse_args(argv)
    try:
        validate_options(args.budget)
    except PreflightError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    if not args.go:
        print_plan(args.budget)
        return 0
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        print("ERROR: $OPENROUTER_API_KEY is required with --go", file=sys.stderr)
        return 2
    try:
        outcome = execute_live(api_key, budget=args.budget)
    except (PreflightError, OutputPathError, mvp.SlugValidationError, mvp.PricingError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    print(f"wrote {outcome.paths}")
    return 3 if outcome.partial_reason else 0


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 7: Run focused and full suites**

```bash
/Users/jimmy.lin/Documents/CEI-Literature-Vault/.venv/bin/python -m pytest tests/test_shadow_judge_bakeoff.py -q
/Users/jimmy.lin/Documents/CEI-Literature-Vault/.venv/bin/python -m pytest tests/ -q
```

Expected: new focused tests pass and full suite exceeds the current 520 tests with zero failures.

- [ ] **Step 8: Commit and push the offline build**

```bash
git log -1 --oneline
git add -- 04-HARNESS/shadow_judge_bakeoff.py 04-HARNESS/tests/test_shadow_judge_bakeoff.py
git commit -m "WCF-Bench: complete shadow bakeoff runner"
git push origin main
```

### Task 7: Execute the exact $1 study and close

**Files:**
- Create: `07-PILOTS/20260712-shadow-judge-bakeoff/selection.json`
- Create: `07-PILOTS/20260712-shadow-judge-bakeoff/raw_verdicts.jsonl`
- Create: `07-PILOTS/20260712-shadow-judge-bakeoff/shadow-run-metadata.json`
- Create: `07-PILOTS/20260712-shadow-judge-bakeoff/20260712-shadow-judge-bakeoff-report.md`
- Modify: `PENDING-QUESTIONS.md`
- Modify: `project-dashboard.html`
- Create: `20260712s-codex-session31-handoff.md`

- [ ] **Step 1: Reverify offline immediately before spending**

```bash
cd /Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/WCF-Benchmark/04-HARNESS
/Users/jimmy.lin/Documents/CEI-Literature-Vault/.venv/bin/python -m pytest tests/test_shadow_judge_bakeoff.py -q
/Users/jimmy.lin/Documents/CEI-Literature-Vault/.venv/bin/python shadow_judge_bakeoff.py --budget 1.00
test ! -e ../07-PILOTS/20260712-shadow-judge-bakeoff
```

- [ ] **Step 2: Execute once with the exact authorization**

```bash
set -a
source ~/.codex/secrets/openrouter.env
set +a
/Users/jimmy.lin/Documents/CEI-Literature-Vault/.venv/bin/python shadow_judge_bakeoff.py --go --budget 1.00
```

Never echo the environment/key. Apply the two-retry rule; never overwrite or manually
restart a completed/partial run directory.

- [ ] **Step 3: Verify output ceilings**

```bash
jq '.artifact_kind, .internal_total_usd, .shadow_verdicts_recorded, .partial_reason' \
  ../07-PILOTS/20260712-shadow-judge-bakeoff/shadow-run-metadata.json
jq '.surface_counts, (.units | length)' \
  ../07-PILOTS/20260712-shadow-judge-bakeoff/selection.json
test "$(find ../07-PILOTS/20260712-shadow-judge-bakeoff -maxdepth 1 -type f -iname '*manifest*' | wc -l | tr -d ' ')" = 0
```

Complete-run expectation: shadow label, cost `<=1.0`, 56 verdicts, null partial reason,
8/8/6/6 counts, 28 selection rows, and zero manifest-named files. A partial run remains
immutable evidence and is not resumed without a new ruling.

- [ ] **Step 4: Update durable state without changing T3/T4**

Update `PENDING-QUESTIONS.md` with execution status/report/actual spend and no automatic
panel effect. Update dashboard banner, Live status, S31 history, judge table with
`SHADOW / NO PANEL EFFECT`, budget actual, update log, and next-session instructions.
Write `20260712s-codex-session31-handoff.md`. Do not tick T3/T4.

- [ ] **Step 5: Run final verification**

```bash
/Users/jimmy.lin/Documents/CEI-Literature-Vault/.venv/bin/python -m pytest tests/ -q
git diff --check
```

- [ ] **Step 6: Commit and push only WCF paths**

```bash
git log -1 --oneline
git add -- 07-PILOTS/20260712-shadow-judge-bakeoff \
  PENDING-QUESTIONS.md project-dashboard.html 20260712s-codex-session31-handoff.md
git commit -m "WCF-Bench: record shadow judge bakeoff"
git push origin main
```

## Plan self-review

- Spec coverage: exact slugs, six probes, K=8, amended 8/8/6/6 sample, seeded selection,
  no incumbent calls, frozen hashes, raw persistence, actual-first accounting, $1 cap,
  latency, agreement, independence flags, Pareto reporting, no manifest, and immutable
  outputs each map to a task.
- Type consistency: candidate tuples remain `(name, family, slug)`; selection units use
  `surface/item_id/sut_slug/sut_response/response_sha256/source_run/axis/comparators`;
  live results use `ShadowOutcome`.
- Scope: one runner and one test file; no dependency, prompt, scorer, bank, manifest, or T4 edit.
