from __future__ import annotations

import hashlib
import importlib
import json
from types import SimpleNamespace

import pytest

from wcfbench.qualification import JudgeQualification, ProbeReps


def _runner():
    return importlib.import_module("shadow_judge_bakeoff")


def _record(item_id, model, response, judges, *, kind="contested"):
    return {
        "item_id": item_id,
        "model": model,
        "sut_response": response,
        "kind": kind,
        "template_hash": "47ddb41c355fbf57",
        "judges": judges,
    }


def test_fixed_shadow_roster_counts_and_budget():
    r = _runner()
    assert r.CANDIDATES == (
        ("glm-5.2", "z-ai", "z-ai/glm-5.2"),
        ("deepseek-v4-pro", "deepseek", "deepseek/deepseek-v4-pro"),
    )
    assert r.SURFACE_COUNTS == {
        "open_award": 8,
        "coherence": 8,
        "disclosure": 6,
        "settled_core": 6,
    }
    assert r.MAX_BUDGET == 1.0


def test_contested_source_priority_never_joins_a_different_response():
    r = _runner()
    floor_a_judges = [
        {"name": "gemini-flash", "scores": {"evidence": "floor A"}}
    ]
    r33_a_judges = [
        {"name": "gemini-flash", "scores": {"evidence": "different A"}}
    ]
    r33_c_judges = [
        {"name": "gemini-flash", "scores": {"evidence": "r33 C"}}
    ]
    floor = [
        _record("A", "llama", "floor A", floor_a_judges),
        _record("B", "llama", "floor B", [{"name": "grok-4.20", "scores": {}}]),
        _record("C", "deepseek", None, []),
    ]
    r33 = [
        _record("A", "llama", "different A", r33_a_judges),
        _record("C", "deepseek", "r33 C", r33_c_judges),
    ]
    chosen = r.select_contested_records(floor, r33, expected=3)
    by_key = {(x["item_id"], x["model"]): x for x in chosen}
    assert by_key[("A", "llama")]["sut_response"] == "floor A"
    assert by_key[("A", "llama")]["judges"] == floor_a_judges
    assert by_key[("A", "llama")]["judges"] != r33_a_judges
    assert by_key[("C", "deepseek")]["sut_response"] == "r33 C"
    assert by_key[("C", "deepseek")]["judges"] == r33_c_judges


def test_seeded_surface_order_is_sha256_and_exact_count():
    r = _runner()
    rows = [_record(f"I{i}", f"M{i}", f"R{i}", [], kind="open") for i in range(12)]
    got = r.take_seeded("open_award", rows, 8)
    expected = sorted(
        rows,
        key=lambda x: hashlib.sha256(
            f"1647|open_award|{x['item_id']}|{x['model']}".encode()
        ).hexdigest(),
    )[:8]
    assert [(x["item_id"], x["model"]) for x in got] == [
        (x["item_id"], x["model"]) for x in expected
    ]


def test_build_selection_has_exact_counts_and_response_hashes():
    r = _runner()
    selection = r.build_selection(
        open_path=r.OPEN_PATH,
        floor_path=r.FLOOR_PATH,
        r33_path=r.R33_PATH,
        bank_dir=r.BANK_DIR,
    )

    assert {
        surface: sum(unit["surface"] == surface for unit in selection)
        for surface in r.SURFACE_COUNTS
    } == r.SURFACE_COUNTS
    assert len(selection) == 28
    assert all(
        unit["response_sha256"]
        == hashlib.sha256(unit["sut_response"].encode()).hexdigest()
        for unit in selection
    )

    contested = [
        unit
        for unit in selection
        if unit["surface"] in {"disclosure", "settled_core"}
    ]
    assert {unit["source_run"] for unit in contested} == {
        "floor-rerun",
        "r33-3judge",
    }
    source_rows = {
        "floor-rerun": r.read_jsonl(r.FLOOR_PATH),
        "r33-3judge": r.read_jsonl(r.R33_PATH),
    }
    for unit in contested:
        matching = [
            row
            for row in source_rows[unit["source_run"]]
            if str(row.get("item_id")) == unit["item_id"]
            and str(row.get("model")) == unit["sut_slug"]
            and row.get("sut_response") == unit["sut_response"]
        ]
        assert len(matching) == 1
        assert unit["comparators"] == r._judges_by_name(matching[0])


def test_write_selection_is_create_new(tmp_path):
    r = _runner()
    path = tmp_path / "selection.json"
    r.write_json_new(
        str(path), {"surface_counts": r.SURFACE_COUNTS, "units": []}
    )
    assert json.loads(path.read_text())["surface_counts"] == r.SURFACE_COUNTS
    with pytest.raises(FileExistsError):
        r.write_json_new(str(path), {"units": []})


def test_shadow_battery_calls_only_two_candidates():
    r = _runner()
    calls = []
    constructed_clients = []

    def fake_client_factory(name, family, slug):
        constructed_clients.append((name, family, slug))
        return slug

    def fake_qualify(client, *, name, family, slug, k, threshold):
        assert client == slug
        calls.append((name, family, slug, k, threshold))
        return f"qualified:{name}"

    results = r.run_shadow_batteries(
        client_factory=fake_client_factory,
        qualify_fn=fake_qualify,
    )

    assert constructed_clients == [
        ("glm-5.2", "z-ai", "z-ai/glm-5.2"),
        (
            "deepseek-v4-pro",
            "deepseek",
            "deepseek/deepseek-v4-pro",
        ),
    ]
    assert calls == [
        ("glm-5.2", "z-ai", "z-ai/glm-5.2", 8, 5),
        (
            "deepseek-v4-pro",
            "deepseek",
            "deepseek/deepseek-v4-pro",
            8,
            5,
        ),
    ]
    assert results == {
        "glm-5.2": "qualified:glm-5.2",
        "deepseek-v4-pro": "qualified:deepseek-v4-pro",
    }


def test_template_hash_mismatch_stops():
    r = _runner()
    with pytest.raises(r.PreflightError, match="template hash"):
        r.assert_template_hashes({"template_hashes": {"g4": "stale"}})


def test_current_ratified_manifest_template_hashes_pass():
    r = _runner()
    manifest = r.load_manifest(r.MANIFEST_PATH)
    assert r.assert_template_hashes(manifest) is None


def test_persist_probe_reps_writes_fixed_order_complete_records():
    r = _runner()
    probe_reps = {}
    for index, probe in enumerate(reversed(r.PROBES)):
        probe_reps[probe] = ProbeReps(
            probe=probe,
            k=2,
            n_pass=1,
            reps=[
                {
                    "rep": index * 2,
                    "passed": True,
                    "cause": "pass",
                    "detail": f"first:{probe}",
                },
                {
                    "rep": index * 2 + 1,
                    "passed": False,
                    "cause": "fail_substantive",
                    "detail": f"second:{probe}",
                },
            ],
        )
    qualification = JudgeQualification(
        name="glm-5.2",
        family="z-ai",
        slug="z-ai/glm-5.2",
        k=2,
        threshold=1,
        probe_reps=probe_reps,
    )

    class CapturingSink:
        def __init__(self):
            self.records = []

        def write(self, record):
            self.records.append(record)

    sink = CapturingSink()
    r.persist_probe_reps(
        sink, qualification, now=lambda: "2026-07-12T12:00:00"
    )

    assert [record["probe"] for record in sink.records] == [
        probe for probe in r.PROBES for _rep in range(2)
    ]
    assert len(sink.records) == len(r.PROBES) * 2
    expected_records = []
    for probe in r.PROBES:
        for rep in probe_reps[probe].reps:
            expected_records.append(
                {
                    "kind": "probe_rep",
                    "timestamp": "2026-07-12T12:00:00",
                    "judge": "glm-5.2",
                    "family": "z-ai",
                    "slug": "z-ai/glm-5.2",
                    "probe": probe,
                    "rep": rep["rep"],
                    "passed": rep["passed"],
                    "cause": rep["cause"],
                    "detail": rep["detail"],
                }
            )
    assert sink.records == expected_records


def test_score_shadow_unit_dispatches_coherence_axis(monkeypatch):
    r = _runner()
    unit = {
        "surface": "coherence",
        "axis": "end",
        "sut_response": "response",
    }
    item = SimpleNamespace(id="I1", stem="stem", rubric=[])

    def fake_score_numeric_axis(score, axis, **kwargs):
        assert axis == "end"
        assert kwargs == {
            "stem": "stem",
            "rubric": [],
            "response": "response",
            "judge": "judge",
            "item_id": "I1",
        }
        score.end = 0.75
        score.graded[axis] = True

    monkeypatch.setattr(r, "_score_numeric_axis", fake_score_numeric_axis)

    assert r.score_shadow_unit(unit, item, "judge") == {
        "graded": True,
        "value": 0.75,
        "axis": "end",
        "scale_defect": False,
    }


def test_score_shadow_unit_returns_open_award_shape(monkeypatch):
    r = _runner()
    unit = {"surface": "open_award", "sut_response": "response"}
    rubric = [
        SimpleNamespace(
            axis="matter", criterion="tagged keypoint", anchor=None
        ),
        SimpleNamespace(
            axis="manner", criterion="second tagged keypoint", anchor=None
        ),
    ]
    item = SimpleNamespace(id="I2", stem="stem", rubric=rubric)
    call = SimpleNamespace(text="valid verdict", discarded=False)
    verdict = SimpleNamespace(
        awards={1: True},
        compliance_defects={2: "reasonless"},
    )

    def fake_complete(judge, prompt, *, item_id, is_complete):
        assert judge == "judge"
        assert item_id == "I2"
        assert is_complete("KP1: award\nKP2: deny")
        return call

    monkeypatch.setattr(r, "complete_with_retry", fake_complete)
    monkeypatch.setattr(r, "parse_award_verdict", lambda text, **kwargs: verdict)

    result = r.score_shadow_unit(unit, item, "judge")

    assert set(result) == {
        "graded",
        "awards",
        "compliance_defects",
        "discarded",
    }
    assert result == {
        "graded": True,
        "awards": {1: True},
        "compliance_defects": {2: "reasonless"},
        "discarded": False,
    }


def test_score_shadow_unit_rejects_out_of_range_open_awards(monkeypatch):
    r = _runner()
    unit = {"surface": "open_award", "sut_response": "response"}
    item = SimpleNamespace(
        id="I2-out-of-range",
        stem="stem",
        rubric=[
            SimpleNamespace(
                axis="matter", criterion="tagged keypoint", anchor=None
            )
        ],
    )
    call = SimpleNamespace(text="valid verdict", discarded=False)
    verdict = SimpleNamespace(
        awards={99: True},
        compliance_defects={99: "out of range"},
    )
    monkeypatch.setattr(r, "complete_with_retry", lambda *args, **kwargs: call)
    monkeypatch.setattr(r, "parse_award_verdict", lambda *args, **kwargs: verdict)

    assert r.score_shadow_unit(unit, item, "judge") == {
        "graded": False,
        "awards": {},
        "compliance_defects": {},
        "discarded": False,
    }


def test_score_shadow_unit_returns_disclosure_shape(monkeypatch):
    r = _runner()
    unit = {"surface": "disclosure", "sut_response": "response"}
    item = SimpleNamespace(id="I3")
    scored = SimpleNamespace(
        graded=True,
        value=0.5,
        awards={"avoided_asserting_settled": True},
        defects={"disclosure_kp2": "bad quote"},
        discarded=False,
    )
    monkeypatch.setattr(r, "_score_disclosure", lambda *args: scored)

    assert r.score_shadow_unit(unit, item, "judge") == {
        "graded": True,
        "value": 0.5,
        "awards": {"avoided_asserting_settled": True},
        "defects": {"disclosure_kp2": "bad quote"},
        "discarded": False,
    }


def test_score_shadow_unit_returns_settled_core_shape(monkeypatch):
    r = _runner()
    unit = {"surface": "settled_core", "sut_response": "response"}
    item = SimpleNamespace(
        id="I4",
        rubric=[
            SimpleNamespace(
                anchor="Q152", criterion="shared floor", axis=None
            )
        ],
    )
    monkeypatch.setattr(
        r,
        "score_settled_core",
        lambda *args: (
            {"shared floor": True},
            ["reasonless floor"],
            "1: correct — explicit reason",
        ),
    )

    assert r.score_shadow_unit(unit, item, "judge") == {
        "graded": True,
        "keypoints": {"shared floor": True},
        "reasonless": ["reasonless floor"],
    }


def test_score_shadow_unit_settled_core_refusal_is_ungraded(monkeypatch):
    r = _runner()
    unit = {"surface": "settled_core", "sut_response": "response"}
    item = SimpleNamespace(
        id="I4-refusal",
        rubric=[
            SimpleNamespace(
                anchor="Q152", criterion="shared floor", axis=None
            )
        ],
    )
    monkeypatch.setattr(
        r,
        "score_settled_core",
        lambda *args: (
            {"shared floor": False},
            [],
            "I refuse to grade this response.",
        ),
    )

    assert r.score_shadow_unit(unit, item, "judge") == {
        "graded": False,
        "keypoints": {"shared floor": False},
        "reasonless": [],
    }


def test_score_shadow_unit_settled_core_explicit_wrong_is_graded(monkeypatch):
    r = _runner()
    unit = {"surface": "settled_core", "sut_response": "response"}
    item = SimpleNamespace(
        id="I4-wrong",
        rubric=[
            SimpleNamespace(
                anchor="Q152", criterion="shared floor", axis=None
            )
        ],
    )
    monkeypatch.setattr(
        r,
        "score_settled_core",
        lambda *args: (
            {"shared floor": False},
            [],
            "1: wrong — response misses the floor",
        ),
    )

    assert r.score_shadow_unit(unit, item, "judge") == {
        "graded": True,
        "keypoints": {"shared floor": False},
        "reasonless": [],
    }


def test_score_shadow_unit_rejects_unknown_surface():
    r = _runner()
    with pytest.raises(ValueError, match="unknown shadow surface"):
        r.score_shadow_unit(
            {"surface": "mystery", "sut_response": "response"},
            SimpleNamespace(id="I5"),
            "judge",
        )


def test_run_shadow_units_persists_every_verdict_and_survives_errors(
    monkeypatch, tmp_path
):
    r = _runner()
    selection = []
    for surface, count in r.SURFACE_COUNTS.items():
        for index in range(count):
            item_id = f"{surface}-{index}"
            response = f"response:{item_id}"
            selection.append(
                {
                    "surface": surface,
                    "item_id": item_id,
                    "sut_slug": f"sut:{surface}",
                    "sut_response": response,
                    "response_sha256": hashlib.sha256(response.encode()).hexdigest(),
                }
            )
    items = {unit["item_id"]: SimpleNamespace(id=unit["item_id"]) for unit in selection}
    clients = {name: f"client:{name}" for name, _family, _slug in r.CANDIDATES}

    def fake_score(unit, item, judge):
        assert item.id == unit["item_id"]
        assert judge == f"client:{judge.removeprefix('client:')}"
        if unit["item_id"].endswith("-0"):
            raise RuntimeError(f"failed {unit['item_id']}")
        return {"graded": True, "surface": unit["surface"]}

    ticks = iter(index / 4 for index in range(112))
    path = tmp_path / "shadow-verdicts.jsonl"
    sink = r.JsonlSink(str(path))
    monkeypatch.setattr(r, "score_shadow_unit", fake_score)

    records = r.run_shadow_units(
        selection,
        clients=clients,
        items=items,
        sink=sink,
        now=lambda: "2026-07-12T12:00:00",
        clock=lambda: next(ticks),
    )

    persisted = [json.loads(line) for line in path.read_text().splitlines()]
    record_keys = {
        "kind",
        "timestamp",
        "judge",
        "surface",
        "item_id",
        "sut_slug",
        "response_sha256",
        "elapsed_seconds",
        "result",
        "error",
    }
    expected_identities = [
        {
            "judge": name,
            "surface": unit["surface"],
            "item_id": unit["item_id"],
            "sut_slug": unit["sut_slug"],
            "response_sha256": unit["response_sha256"],
        }
        for name, _family, _slug in r.CANDIDATES
        for unit in selection
    ]
    assert len(records) == 56
    assert len([record for record in records if record["error"]]) == 8
    assert all(
        record["error"] == f"RuntimeError: failed {record['item_id']}"
        and record["result"] is None
        for record in records
        if record["item_id"].endswith("-0")
    )
    assert all(
        any(
            later["judge"] == record["judge"]
            and later["surface"] == record["surface"]
            and later["result"] == {
                "graded": True,
                "surface": record["surface"],
            }
            for later in records[index + 1 :]
        )
        for index, record in enumerate(records)
        if record["error"]
    )
    assert persisted == records
    assert all(set(record) == record_keys for record in records)
    assert all(record["kind"] == "shadow_verdict" for record in records)
    assert all(
        record["timestamp"] == "2026-07-12T12:00:00"
        for record in records
    )
    assert all(record["elapsed_seconds"] >= 0 for record in records)
    assert [
        {
            "judge": record["judge"],
            "surface": record["surface"],
            "item_id": record["item_id"],
            "sut_slug": record["sut_slug"],
            "response_sha256": record["response_sha256"],
        }
        for record in records
    ] == expected_identities
    assert [record["judge"] for record in records[:28]] == ["glm-5.2"] * 28
    assert [record["judge"] for record in records[28:]] == [
        "deepseek-v4-pro"
    ] * 28


def test_run_shadow_units_canonicalizes_nested_open_keys(monkeypatch, tmp_path):
    r = _runner()
    selection = [
        {
            "surface": "open_award",
            "item_id": "open-1",
            "sut_slug": "sut:model",
            "sut_response": "response",
            "response_sha256": "synthetic-hash",
        }
    ]
    monkeypatch.setattr(
        r,
        "score_shadow_unit",
        lambda *args: {
            "graded": True,
            "awards": {1: True},
            "compliance_defects": {2: "reasonless"},
            "discarded": False,
        },
    )
    path = tmp_path / "canonical-shadow-verdicts.jsonl"

    records = r.run_shadow_units(
        selection,
        clients={name: name for name, _family, _slug in r.CANDIDATES},
        items={"open-1": SimpleNamespace(id="open-1")},
        sink=r.JsonlSink(str(path)),
        now=lambda: "2026-07-12T12:00:00",
        clock=iter([0.0, 0.1, 0.2, 0.3]).__next__,
    )

    persisted = [json.loads(line) for line in path.read_text().splitlines()]
    assert records == persisted
    assert all(record["result"]["awards"] == {"1": True} for record in records)
    assert all(
        record["result"]["compliance_defects"] == {"2": "reasonless"}
        for record in records
    )


def _live_catalog(r):
    return {
        slug: {
            "pricing": {
                "prompt": "0.000001",
                "completion": "0.000001",
            }
        }
        for _name, _family, slug in r.CANDIDATES
    }


def _live_selection():
    return [
        {
            "surface": "coherence",
            "item_id": "WCF-001",
            "sut_slug": "synthetic/sut",
            "sut_response": "synthetic response",
            "response_sha256": "synthetic-hash",
            "axis": "end",
            "comparators": {},
        }
    ]


def test_exact_candidates_have_no_alias_or_fallback():
    r = _runner()
    assert r.resolve_candidates(_live_catalog(r)) == r.CANDIDATES

    missing_price = _live_catalog(r)
    missing_price[r.CANDIDATES[0][2]] = {"pricing": {}}
    with pytest.raises(r.mvp.PricingError):
        r.resolve_candidates(missing_price)

    aliases_only = {
        "z-ai/glm-4.5-air": {
            "pricing": {"prompt": "0.000001", "completion": "0.000001"}
        },
        "deepseek/deepseek-chat": {
            "pricing": {"prompt": "0.000001", "completion": "0.000001"}
        },
    }
    with pytest.raises(r.mvp.SlugValidationError):
        r.resolve_candidates(aliases_only)


@pytest.mark.parametrize("budget", [0, -0.01, 1.01])
def test_shadow_budget_is_strictly_bounded(budget):
    r = _runner()
    with pytest.raises(r.PreflightError, match=r">\$0 and <=\$1\.00"):
        r.validate_options(budget)


def test_one_dollar_shadow_budget_is_accepted():
    assert _runner().validate_options(1.0) is None


def test_timing_client_records_one_entry_per_underlying_attempt_and_proxies():
    r = _runner()

    class Sink:
        def __init__(self):
            self.records = []

        def write(self, record):
            self.records.append(record)

    class Inner:
        def __init__(self):
            self.usage_log = [{"usage": {"cost": 0.001}}]
            self.max_tokens = 2048
            self.last_finish_reason = "stop"
            self.last_truncated = False
            self.fail = False

        def complete(self, prompt, item_id=None):
            if self.fail:
                raise RuntimeError(f"failed {item_id}")
            return f"answer:{prompt}:{item_id}"

    sink = Sink()
    inner = Inner()
    ticks = iter([10.0, 10.25, 20.0, 19.0])
    client = r.TimingClient(
        inner,
        name="glm-5.2",
        slug="z-ai/glm-5.2",
        sink=sink,
        now=lambda: "2026-07-12T12:00:00",
        clock=lambda: next(ticks),
    )

    assert client.usage_log is inner.usage_log
    assert client.max_tokens == 2048
    assert client.last_finish_reason == "stop"
    assert client.last_truncated is False
    assert client.complete("first", item_id="I1") == "answer:first:I1"
    inner.fail = True
    with pytest.raises(RuntimeError, match="failed I2"):
        client.complete("second", item_id="I2")

    assert sink.records == [
        {
            "kind": "call_timing",
            "timestamp": "2026-07-12T12:00:00",
            "judge": "glm-5.2",
            "slug": "z-ai/glm-5.2",
            "item_id": "I1",
            "elapsed_seconds": 0.25,
            "error": None,
        },
        {
            "kind": "call_timing",
            "timestamp": "2026-07-12T12:00:00",
            "judge": "glm-5.2",
            "slug": "z-ai/glm-5.2",
            "item_id": "I2",
            "elapsed_seconds": 0.0,
            "error": "RuntimeError: failed I2",
        },
    ]


def test_selection_precedes_calls_latency_is_per_attempt_and_no_manifest(tmp_path):
    r = _runner()
    out_dir = tmp_path / "shadow"
    first_call_saw_selection = []

    class FakeClient:
        def __init__(self, model, **kwargs):
            self.model = model
            self.max_tokens = kwargs["max_tokens"]
            self.usage_log = []
            self.last_finish_reason = "stop"
            self.last_truncated = False

        def complete(self, prompt, item_id=None):
            first_call_saw_selection.append(
                (out_dir / "selection.json").exists()
            )
            self.usage_log.append(
                {
                    "usage": {
                        "prompt_tokens": 1,
                        "completion_tokens": 1,
                        "cost": 0.001,
                    }
                }
            )
            return "SCORE: 1.0"

    snapshots = iter(
        [
            {"usage": 1.0, "limit_remaining": 9.0},
            {"usage": 1.002, "limit_remaining": 8.998},
        ]
    )

    def fake_qualify(client, *, name, family, slug, k, threshold):
        client.complete("probe", item_id="PROBE")
        return {"name": name, "slug": slug}

    outcome = r.execute_live(
        "secret",
        out_dir=str(out_dir),
        budget=1.0,
        key_fetch=lambda _key: next(snapshots),
        catalog_fetch=lambda _key: _live_catalog(r),
        client_builder=FakeClient,
        qualify_fn=fake_qualify,
        selection_fn=lambda **_kwargs: _live_selection(),
        score_fn=lambda *_args, **_kwargs: [],
        now=lambda: "2026-07-12T00:00:00",
    )

    expected_paths = {
        "selection": out_dir / "selection.json",
        "raw": out_dir / "raw_verdicts.jsonl",
        "metadata": out_dir / "shadow-run-metadata.json",
        "report": out_dir / "20260712-shadow-judge-bakeoff-report.md",
    }
    assert set(outcome.paths) == set(expected_paths)
    assert all(path.exists() for path in expected_paths.values())
    assert first_call_saw_selection and all(first_call_saw_selection)
    selection = json.loads(expected_paths["selection"].read_text())
    assert selection == {
        "seed": r.SEED,
        "surface_counts": r.SURFACE_COUNTS,
        "units": _live_selection(),
    }
    assert not any("manifest" in path.name.lower() for path in out_dir.iterdir())
    metadata = json.loads(expected_paths["metadata"].read_text())
    assert metadata["artifact_kind"] == "SHADOW / NOT A QUALIFICATION MANIFEST"
    assert metadata["run_status"] == "COMPLETE"
    assert metadata["candidates"] == [
        {
            "name": name,
            "family": family,
            "slug": slug,
            "pricing": _live_catalog(r)[slug]["pricing"],
        }
        for name, family, slug in r.CANDIDATES
    ]
    assert metadata["k"] == r.K
    assert metadata["threshold"] == r.THRESHOLD
    assert metadata["surface_counts"] == r.SURFACE_COUNTS
    assert metadata["budget_usd"] == 1.0
    assert metadata["internal_total_usd"] == 0.002
    assert metadata["qualification_complete"] is True
    assert metadata["shadow_verdicts_recorded"] == 0
    assert metadata["key_before"] == {"usage": 1.0, "limit_remaining": 9.0}
    assert metadata["key_after"] == {
        "usage": 1.002,
        "limit_remaining": 8.998,
    }
    assert metadata["partial_reason"] is None
    assert "secret" not in expected_paths["metadata"].read_text()
    raw = [
        json.loads(line)
        for line in expected_paths["raw"].read_text().splitlines()
    ]
    assert sum(x["kind"] == "call_timing" for x in raw) == sum(
        x["kind"] == "raw_call" for x in raw
    )
    assert all(
        x["elapsed_seconds"] >= 0
        for x in raw
        if x["kind"] == "call_timing"
    )


def test_existing_output_path_stops_before_any_preflight_or_client(tmp_path):
    r = _runner()
    out_dir = tmp_path / "existing"
    out_dir.mkdir()
    calls = []

    def forbidden(*args, **kwargs):
        calls.append((args, kwargs))
        raise AssertionError("must not be called")

    with pytest.raises(r.OutputPathError, match="already exists"):
        r.execute_live(
            "secret",
            out_dir=str(out_dir),
            key_fetch=forbidden,
            catalog_fetch=forbidden,
            client_builder=forbidden,
        )
    assert calls == []


def test_low_key_credit_stops_before_output_catalog_or_client(tmp_path):
    r = _runner()
    out_dir = tmp_path / "shadow"
    later_calls = []

    def forbidden(*args, **kwargs):
        later_calls.append((args, kwargs))
        raise AssertionError("must not be called")

    with pytest.raises(r.PreflightError, match=r"below \$1.00 budget"):
        r.execute_live(
            "secret",
            out_dir=str(out_dir),
            budget=1.0,
            key_fetch=lambda _key: {"usage": 9.5, "limit_remaining": 0.5},
            catalog_fetch=forbidden,
            client_builder=forbidden,
        )
    assert not out_dir.exists()
    assert later_calls == []


def test_missing_exact_slug_stops_before_output_or_client(tmp_path):
    r = _runner()
    out_dir = tmp_path / "shadow"
    client_calls = []

    class ForbiddenClient:
        def __init__(self, *args, **kwargs):
            client_calls.append((args, kwargs))

    with pytest.raises(r.mvp.SlugValidationError):
        r.execute_live(
            "secret",
            out_dir=str(out_dir),
            key_fetch=lambda _key: {"usage": 1.0, "limit_remaining": 9.0},
            catalog_fetch=lambda _key: {
                "z-ai/glm-4.5-air": {},
                "deepseek/deepseek-chat": {},
            },
            client_builder=ForbiddenClient,
        )
    assert not out_dir.exists()
    assert client_calls == []


def test_template_mismatch_stops_before_output_or_client(monkeypatch, tmp_path):
    r = _runner()
    out_dir = tmp_path / "shadow"
    client_calls = []
    monkeypatch.setattr(r, "load_manifest", lambda _path: {"template_hashes": {}})

    class ForbiddenClient:
        def __init__(self, *args, **kwargs):
            client_calls.append((args, kwargs))

    with pytest.raises(r.PreflightError, match="template hash"):
        r.execute_live(
            "secret",
            out_dir=str(out_dir),
            key_fetch=lambda _key: {"usage": 1.0, "limit_remaining": 9.0},
            catalog_fetch=lambda _key: _live_catalog(r),
            client_builder=ForbiddenClient,
        )
    assert not out_dir.exists()
    assert client_calls == []


@pytest.mark.parametrize("failure_mode", ["missing_usage", "budget_stop"])
def test_live_call_failure_persists_partial_immutable_artifacts(
    failure_mode, tmp_path
):
    r = _runner()
    out_dir = tmp_path / "shadow"

    class FailingClient:
        def __init__(self, model, **kwargs):
            self.model = model
            self.max_tokens = kwargs["max_tokens"]
            self.usage_log = []
            self.last_finish_reason = "stop"
            self.last_truncated = False

        def complete(self, prompt, item_id=None):
            if failure_mode == "budget_stop":
                self.usage_log.append(
                    {
                        "usage": {
                            "prompt_tokens": 1,
                            "completion_tokens": 1,
                            "cost": 2.0,
                        }
                    }
                )
            return "SCORE: 1.0"

    def fake_qualify(client, *, name, family, slug, k, threshold):
        client.complete("probe", item_id=f"PROBE-{name}")
        return {"name": name}

    snapshots = iter(
        [
            {"usage": 1.0, "limit_remaining": 9.0},
            {"usage": 1.0, "limit_remaining": 9.0},
        ]
    )
    outcome = r.execute_live(
        "secret",
        out_dir=str(out_dir),
        budget=1.0,
        key_fetch=lambda _key: next(snapshots),
        catalog_fetch=lambda _key: _live_catalog(r),
        client_builder=FailingClient,
        qualify_fn=fake_qualify,
        selection_fn=lambda **_kwargs: _live_selection(),
        score_fn=lambda *_args, **_kwargs: [],
        now=lambda: "2026-07-12T00:00:00",
    )

    assert outcome.partial_reason
    metadata = json.loads((out_dir / "shadow-run-metadata.json").read_text())
    report = (out_dir / "20260712-shadow-judge-bakeoff-report.md").read_text()
    assert metadata["partial_reason"] == outcome.partial_reason
    assert metadata["run_status"] == "PARTIAL"
    assert metadata["qualification_complete"] is False
    assert "PARTIAL" in report
    assert outcome.partial_reason in report
    assert not any("manifest" in path.name.lower() for path in out_dir.iterdir())

    with pytest.raises(r.OutputPathError):
        r.execute_live(
            "secret",
            out_dir=str(out_dir),
            key_fetch=lambda _key: pytest.fail("must fail before key fetch"),
        )
