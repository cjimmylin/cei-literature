from __future__ import annotations

import hashlib
import importlib
import json
from types import SimpleNamespace

import pytest

from wcfbench import OpenRouterError
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


def _exact_selection(r):
    units = []
    settled_ids = ("AGG-C3-W302", "AGG-C5-W304", "AGG-C8-W305")
    for surface, count in r.SURFACE_COUNTS.items():
        for index in range(count):
            item_id = (
                settled_ids[index % len(settled_ids)]
                if surface == "settled_core"
                else f"{surface}-{index}"
            )
            response = f"response:{item_id}"
            units.append(
                {
                    "surface": surface,
                    "item_id": item_id,
                    "sut_slug": f"synthetic/sut-{index}",
                    "sut_response": response,
                    "response_sha256": hashlib.sha256(
                        response.encode()
                    ).hexdigest(),
                    "axis": "end" if surface == "coherence" else None,
                    "comparators": {},
                }
            )
    return units


def _complete_qualification(r, name, family, slug):
    probe_reps = {
        probe: ProbeReps(
            probe=probe,
            k=r.K,
            n_pass=r.K,
            reps=[
                {
                    "rep": rep,
                    "passed": True,
                    "cause": "pass",
                    "detail": "synthetic",
                }
                for rep in range(r.K)
            ],
        )
        for probe in r.PROBES
    }
    return JudgeQualification(
        name=name,
        family=family,
        slug=slug,
        k=r.K,
        threshold=r.THRESHOLD,
        probe_reps=probe_reps,
    )


def _complete_qualifications(r):
    return {
        name: _complete_qualification(r, name, family, slug)
        for name, family, slug in r.CANDIDATES
    }


def _complete_raw_evidence(r, selection):
    records = []
    for sequence, (name, family, slug) in enumerate(r.CANDIDATES, 1):
        records.extend(
            [
                {
                    "kind": "call_timing",
                    "judge": name,
                    "slug": slug,
                    "item_id": "QUALIFICATION",
                    "phase": "qualification",
                    "timing_sequence": sequence,
                },
                {
                    "kind": "raw_call",
                    "judge": name,
                    "family": family,
                    "slug": slug,
                    "item_id": "QUALIFICATION",
                    "phase": "qualification",
                    "timing_sequence": sequence,
                    "invocation": 1,
                    "attempt": 0,
                },
            ]
        )
        for probe in r.PROBES:
            for rep in range(r.K):
                records.append(
                    {
                        "kind": "probe_rep",
                        "judge": name,
                        "family": family,
                        "slug": slug,
                        "probe": probe,
                        "rep": rep,
                        "passed": True,
                        "cause": "pass",
                        "detail": "synthetic substantive evidence",
                    }
                )
        for unit in selection:
            records.append(
                {
                    "kind": "shadow_verdict",
                    "judge": name,
                    "surface": unit["surface"],
                    "item_id": unit["item_id"],
                    "sut_slug": unit["sut_slug"],
                    "response_sha256": unit["response_sha256"],
                    "result": None,
                    "error": "synthetic attempted evidence",
                }
            )
    return records


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


@pytest.mark.parametrize(
    "field,value",
    [
        ("prompt", float("nan")),
        ("completion", float("inf")),
        ("prompt", -0.000001),
    ],
)
def test_nonfinite_or_negative_catalog_price_stops_before_output_or_client(
    field, value, tmp_path
):
    r = _runner()
    out_dir = tmp_path / "shadow"
    catalog = _live_catalog(r)
    catalog[r.CANDIDATES[0][2]]["pricing"][field] = value
    client_calls = []

    class ForbiddenClient:
        def __init__(self, *args, **kwargs):
            client_calls.append((args, kwargs))

    with pytest.raises(r.PreflightError, match="finite and nonnegative"):
        r.execute_live(
            "secret",
            out_dir=str(out_dir),
            key_fetch=lambda _key: {
                "usage": 1.0,
                "limit": 10.0,
                "limit_remaining": 9.0,
            },
            catalog_fetch=lambda _key: catalog,
            client_builder=ForbiddenClient,
        )
    assert not out_dir.exists()
    assert client_calls == []


@pytest.mark.parametrize(
    "budget",
    [0, -0.01, 1.01, float("nan"), float("inf"), float("-inf")],
)
def test_shadow_budget_is_strictly_bounded(budget):
    r = _runner()
    with pytest.raises(r.PreflightError, match=r">\$0 and <=\$1\.00"):
        r.validate_options(budget)


def test_one_dollar_shadow_budget_is_accepted():
    assert _runner().validate_options(1.0) is None


def test_nonnumeric_budget_raises_preflight_with_repr():
    with pytest.raises(_runner().PreflightError, match="received 'one'"):
        _runner().validate_options("one")


@pytest.mark.parametrize(
    "field,value",
    [
        ("usage", float("nan")),
        ("limit_remaining", float("inf")),
        ("limit", -1.0),
    ],
)
def test_invalid_key_snapshot_stops_before_output_or_client(
    field, value, tmp_path
):
    r = _runner()
    out_dir = tmp_path / "shadow"
    snapshot = {"usage": 1.0, "limit": 10.0, "limit_remaining": 9.0}
    snapshot[field] = value
    later_calls = []

    def forbidden(*args, **kwargs):
        later_calls.append((args, kwargs))
        raise AssertionError("must not be called")

    with pytest.raises(r.PreflightError, match="key-before.*finite.*nonnegative"):
        r.execute_live(
            "secret",
            out_dir=str(out_dir),
            key_fetch=lambda _key: snapshot,
            catalog_fetch=forbidden,
            client_builder=forbidden,
        )
    assert not out_dir.exists()
    assert later_calls == []


def test_metadata_cannot_claim_complete_above_budget():
    r = _runner()
    metadata = r.build_metadata(
        catalog=_live_catalog(r),
        budget=1.0,
        internal_total=1.01,
        partial_reason=None,
        qualifications={name: {} for name, _family, _slug in r.CANDIDATES},
        verdicts=[],
        analysis={
            "qualification": {},
            "agreement": [],
            "operations": {},
            "pareto_names": [],
        },
        key_before={"usage": 1.0, "limit_remaining": 9.0},
        key_after={"usage": 2.01, "limit_remaining": 7.99},
    )

    assert metadata["run_status"] == "PARTIAL"
    assert "exceeded budget" in metadata["partial_reason"]


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
            "phase": "qualification",
            "elapsed_seconds": 0.25,
            "error": None,
        },
        {
            "kind": "call_timing",
            "timestamp": "2026-07-12T12:00:00",
            "judge": "glm-5.2",
            "slug": "z-ai/glm-5.2",
            "item_id": "I2",
            "phase": "qualification",
            "elapsed_seconds": 0.0,
            "error": "RuntimeError: failed I2",
        },
    ]


def test_timing_and_raw_retry_attempts_share_stable_identity(tmp_path):
    r = _runner()
    raw_path = tmp_path / "raw.jsonl"
    sink = r.TimingLinkedSink(str(raw_path))
    sink.touch()

    class RetryOnceClient:
        def __init__(self):
            self.max_tokens = 16
            self.usage_log = []
            self.last_finish_reason = "stop"
            self.last_truncated = False
            self.attempt = 0

        def complete(self, prompt, item_id=None):
            self.attempt += 1
            if self.attempt == 1:
                raise OpenRouterError("transient")
            self.usage_log.append(
                {
                    "usage": {
                        "prompt_tokens": 1,
                        "completion_tokens": 1,
                        "total_tokens": 2,
                        "cost": 0.001,
                    }
                }
            )
            return "ok"

    inner = RetryOnceClient()
    guard = r.BudgetGuard(1.0, _live_catalog(r))
    guard.register(r.CANDIDATES[0][2], inner)
    timed = r.TimingClient(
        inner,
        name=r.CANDIDATES[0][0],
        slug=r.CANDIDATES[0][2],
        sink=sink,
        now=lambda: "2026-07-12T00:00:00",
    )
    client = r.StrictCapturingClient(
        timed,
        name=r.CANDIDATES[0][0],
        family=r.CANDIDATES[0][1],
        slug=r.CANDIDATES[0][2],
        guard=guard,
        sink=sink,
        now=lambda: "2026-07-12T00:00:00",
        sleeper=lambda _seconds: None,
    )

    assert client.complete("prompt", item_id="ITEM") == "ok"
    records = [json.loads(line) for line in raw_path.read_text().splitlines()]
    timings = [record for record in records if record["kind"] == "call_timing"]
    raw_calls = [record for record in records if record["kind"] == "raw_call"]
    assert len(timings) == len(raw_calls) == 2
    assert {(x["judge"], x["timing_sequence"]) for x in timings} == {
        (x["judge"], x["timing_sequence"]) for x in raw_calls
    }
    assert [(x["invocation"], x["attempt"]) for x in raw_calls] == [
        (1, 0),
        (1, 1),
    ]
    assert len({x["timing_sequence"] for x in timings}) == 2
    assert {x["phase"] for x in timings} == {"qualification"}
    assert [x["phase"] for x in timings] == [x["phase"] for x in raw_calls]


@pytest.mark.parametrize(
    "usage",
    [
        {
            "prompt_tokens": 1,
            "completion_tokens": 1,
            "total_tokens": 2,
            "cost": float("nan"),
        },
        {
            "prompt_tokens": 1,
            "completion_tokens": 1,
            "total_tokens": 2,
            "cost": float("inf"),
        },
        {
            "prompt_tokens": 1,
            "completion_tokens": 1,
            "total_tokens": 2,
            "cost": -0.01,
        },
        {"prompt_tokens": float("nan"), "completion_tokens": 1},
        {"prompt_tokens": 1, "completion_tokens": float("inf")},
        {"prompt_tokens": 1, "completion_tokens": -1},
        {"prompt_tokens": 1, "completion_tokens": 1, "total_tokens": -1},
    ],
)
def test_invalid_response_usage_latches_accounting_and_persists_partial(
    usage, tmp_path
):
    r = _runner()
    out_dir = tmp_path / "shadow"

    class InvalidUsageClient:
        def __init__(self, model, **kwargs):
            self.model = model
            self.max_tokens = kwargs["max_tokens"]
            self.usage_log = []
            self.last_finish_reason = "stop"
            self.last_truncated = False

        def complete(self, prompt, item_id=None):
            self.usage_log.append({"usage": dict(usage)})
            return "response"

    def fake_qualify(client, **_kwargs):
        client.complete("probe", item_id="PROBE")
        return {}

    snapshots = iter(
        [
            {"usage": 1.0, "limit_remaining": 9.0},
            {"usage": 1.0, "limit_remaining": 9.0},
        ]
    )
    outcome = r.execute_live(
        "secret",
        out_dir=str(out_dir),
        key_fetch=lambda _key: next(snapshots),
        catalog_fetch=lambda _key: _live_catalog(r),
        client_builder=InvalidUsageClient,
        qualify_fn=fake_qualify,
        selection_fn=lambda **_kwargs: _live_selection(),
        score_fn=lambda *_args, **_kwargs: [],
        now=lambda: "2026-07-12T00:00:00",
    )

    metadata = json.loads((out_dir / "shadow-run-metadata.json").read_text())
    raw = [
        json.loads(line)
        for line in (out_dir / "raw_verdicts.jsonl").read_text().splitlines()
    ]
    raw_calls = [record for record in raw if record["kind"] == "raw_call"]
    assert outcome.partial_reason
    assert "accounting" in outcome.partial_reason
    assert metadata["run_status"] == "PARTIAL"
    assert metadata["internal_total_usd"] is None
    assert metadata["reconciliation"]["status"] == "UNRECONCILED"
    assert len(raw_calls) == 1
    assert raw_calls[0]["error"]
    assert raw_calls[0]["usage"]


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
    assert metadata["run_status"] == "PARTIAL"
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
    assert metadata["qualification_complete"] is False
    assert metadata["shadow_verdicts_recorded"] == 0
    assert metadata["key_before"] == {"usage": 1.0, "limit_remaining": 9.0}
    assert metadata["key_after"] == {
        "usage": 1.002,
        "limit_remaining": 8.998,
    }
    assert "evidence incomplete" in metadata["partial_reason"]
    assert metadata["analysis"]["pareto_names"] == []
    assert metadata["reconciliation"] == {
        "status": "RECONCILED",
        "internal_total_usd": 0.002,
        "key_usage_delta_usd": pytest.approx(0.002),
        "within_20_percent": True,
        "unavailable_reason": None,
    }
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
    assert {
        (x["judge"], x["timing_sequence"])
        for x in raw
        if x["kind"] == "call_timing"
    } == {
        (x["judge"], x["timing_sequence"])
        for x in raw
        if x["kind"] == "raw_call"
    }


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
            budget=1.01,
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


def test_final_actual_overrun_is_partial_without_a_following_call(tmp_path):
    r = _runner()
    out_dir = tmp_path / "shadow"
    attempts = []

    class FinalOverrunClient:
        def __init__(self, model, **kwargs):
            self.model = model
            self.max_tokens = kwargs["max_tokens"]
            self.usage_log = []
            self.last_finish_reason = "stop"
            self.last_truncated = False

        def complete(self, prompt, item_id=None):
            attempts.append((self.model, item_id))
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
        if name == r.CANDIDATES[-1][0]:
            client.complete("final paid attempt", item_id="FINAL")
        return {"name": name}

    snapshots = iter(
        [
            {"usage": 1.0, "limit_remaining": 9.0},
            {"usage": 3.0, "limit_remaining": 7.0},
        ]
    )
    outcome = r.execute_live(
        "secret",
        out_dir=str(out_dir),
        budget=1.0,
        key_fetch=lambda _key: next(snapshots),
        catalog_fetch=lambda _key: _live_catalog(r),
        client_builder=FinalOverrunClient,
        qualify_fn=fake_qualify,
        selection_fn=lambda **_kwargs: _live_selection(),
        score_fn=lambda *_args, **_kwargs: [],
        now=lambda: "2026-07-12T00:00:00",
    )

    assert attempts == [(r.CANDIDATES[-1][2], "FINAL")]
    assert outcome.internal_total_usd == 2.0
    assert outcome.partial_reason
    metadata = json.loads((out_dir / "shadow-run-metadata.json").read_text())
    report = (out_dir / "20260712-shadow-judge-bakeoff-report.md").read_text()
    assert metadata["internal_total_usd"] == 2.0
    assert metadata["run_status"] == "PARTIAL"
    assert metadata["partial_reason"] == outcome.partial_reason
    assert "PARTIAL" in report
    assert not any("manifest" in path.name.lower() for path in out_dir.iterdir())


@pytest.mark.parametrize("failure_stage", ["selection", "sink"])
def test_post_directory_setup_failure_persists_partial_artifacts(
    monkeypatch, failure_stage, tmp_path
):
    r = _runner()
    out_dir = tmp_path / "shadow"
    client_calls = []
    original_write_json_new = r.write_json_new

    if failure_stage == "selection":
        def fail_selection_only(path, value):
            if path.endswith("selection.json"):
                raise RuntimeError("selection setup failed")
            original_write_json_new(path, value)

        monkeypatch.setattr(r, "write_json_new", fail_selection_only)
    else:
        def fail_sink_touch(self):
            raise RuntimeError("raw sink setup failed")

        monkeypatch.setattr(r.JsonlSink, "touch", fail_sink_touch)

    class ForbiddenClient:
        def __init__(self, *args, **kwargs):
            client_calls.append((args, kwargs))

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
        client_builder=ForbiddenClient,
        selection_fn=lambda **_kwargs: _live_selection(),
        now=lambda: "2026-07-12T00:00:00",
    )

    metadata_path = out_dir / "shadow-run-metadata.json"
    report_path = out_dir / "20260712-shadow-judge-bakeoff-report.md"
    assert out_dir.exists()
    assert metadata_path.exists()
    assert report_path.exists()
    assert client_calls == []
    metadata = json.loads(metadata_path.read_text())
    assert metadata["run_status"] == "PARTIAL"
    assert failure_stage in metadata["partial_reason"]
    assert outcome.partial_reason == metadata["partial_reason"]
    assert "PARTIAL" in report_path.read_text()


def test_final_accounting_failure_persists_partial_artifacts(
    monkeypatch, tmp_path
):
    r = _runner()
    out_dir = tmp_path / "shadow"

    class ExplodingGuard(r.BudgetGuard):
        def total_usd(self):
            raise RuntimeError("accounting unavailable")

    class NoCallClient:
        def __init__(self, model, **kwargs):
            self.model = model
            self.max_tokens = kwargs["max_tokens"]
            self.usage_log = []
            self.last_finish_reason = "stop"
            self.last_truncated = False

    monkeypatch.setattr(r, "BudgetGuard", ExplodingGuard)
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
        client_builder=NoCallClient,
        qualify_fn=lambda _client, **kwargs: {"name": kwargs["name"]},
        selection_fn=lambda **_kwargs: _live_selection(),
        score_fn=lambda *_args, **_kwargs: [],
        now=lambda: "2026-07-12T00:00:00",
    )

    metadata = json.loads((out_dir / "shadow-run-metadata.json").read_text())
    report = (out_dir / "20260712-shadow-judge-bakeoff-report.md").read_text()
    assert outcome.internal_total_usd is None
    assert outcome.partial_reason
    assert "accounting" in outcome.partial_reason
    assert "RuntimeError: accounting unavailable" in outcome.partial_reason
    assert metadata["internal_total_usd"] is None
    assert metadata["reconciliation"]["status"] == "UNRECONCILED"
    assert metadata["run_status"] == "PARTIAL"
    assert metadata["partial_reason"] == outcome.partial_reason
    assert "PARTIAL" in report


def test_exact_persisted_evidence_is_complete():
    r = _runner()
    selection = _exact_selection(r)
    qualifications = _complete_qualifications(r)
    raw_records = _complete_raw_evidence(r, selection)

    evidence = r.assess_evidence(selection, qualifications, raw_records)

    assert evidence == {
        "complete": True,
        "selection_complete": True,
        "qualification_complete": True,
        "probe_coverage_complete": True,
        "probe_reps_recorded": 96,
        "verdict_coverage_complete": True,
        "shadow_verdicts_recorded": 56,
        "timing_pairs_complete": True,
        "issues": [],
    }


@pytest.mark.parametrize(
    "defect,issue",
    [
        ("threshold", "qualification substance"),
        ("probe_detail", "probe substance"),
        ("probe_n_pass", "probe substance"),
        ("hollow_verdict", "verdict substance"),
        ("duplicate_selection", "selection substance"),
        ("bad_hash", "selection substance"),
        ("missing_timing", "timing substance"),
        ("timing_mismatch", "timing substance"),
    ],
)
def test_evidence_counts_require_substantive_records(defect, issue):
    r = _runner()
    selection = _exact_selection(r)
    qualifications = _complete_qualifications(r)
    raw_records = _complete_raw_evidence(r, selection)

    if defect == "threshold":
        qualifications[r.CANDIDATES[0][0]].threshold += 1
    elif defect == "probe_detail":
        next(x for x in raw_records if x["kind"] == "probe_rep")["detail"] = ""
    elif defect == "probe_n_pass":
        next(x for x in raw_records if x["kind"] == "probe_rep")["passed"] = False
    elif defect == "hollow_verdict":
        verdict = next(x for x in raw_records if x["kind"] == "shadow_verdict")
        verdict["result"] = None
        verdict["error"] = ""
    elif defect == "duplicate_selection":
        for field in ("surface", "item_id", "sut_slug"):
            selection[0][field] = selection[1][field]
    elif defect == "bad_hash":
        selection[0]["response_sha256"] = "not-the-response-hash"
    elif defect == "missing_timing":
        raw_records = [
            x
            for x in raw_records
            if x["kind"] not in {"call_timing", "raw_call"}
        ]
    elif defect == "timing_mismatch":
        next(x for x in raw_records if x["kind"] == "call_timing")[
            "item_id"
        ] = "DIFFERENT"

    evidence = r.assess_evidence(selection, qualifications, raw_records)

    assert evidence["complete"] is False
    assert any(issue in value for value in evidence["issues"])


def test_default_qualification_cannot_swallow_missing_usage_into_complete(
    tmp_path,
):
    r = _runner()
    out_dir = tmp_path / "shadow"

    class MissingUsageScriptedClient:
        underlying_calls = 0

        def __init__(self, model, **kwargs):
            self.model = model
            self.max_tokens = kwargs["max_tokens"]
            self.usage_log = []
            self.last_finish_reason = "stop"
            self.last_truncated = False

        def complete(self, prompt, item_id=None):
            type(self).underlying_calls += 1
            return "scripted response without usage"

    snapshots = iter(
        [
            {"usage": 1.0, "limit_remaining": 9.0},
            {"usage": 1.0, "limit_remaining": 9.0},
        ]
    )
    outcome = r.execute_live(
        "secret",
        out_dir=str(out_dir),
        key_fetch=lambda _key: next(snapshots),
        catalog_fetch=lambda _key: _live_catalog(r),
        client_builder=MissingUsageScriptedClient,
        selection_fn=lambda **_kwargs: _live_selection(),
        score_fn=lambda *_args, **_kwargs: [],
        now=lambda: "2026-07-12T00:00:00",
    )

    metadata = json.loads((out_dir / "shadow-run-metadata.json").read_text())
    assert MissingUsageScriptedClient.underlying_calls == 1
    assert outcome.partial_reason
    assert "accounting" in outcome.partial_reason
    assert outcome.internal_total_usd is None
    assert metadata["run_status"] == "PARTIAL"
    assert metadata["probe_reps_recorded"] == 96
    assert metadata["reconciliation"]["status"] == "UNRECONCILED"
    assert metadata["partial_reason"] == outcome.partial_reason


def test_guard_fatal_error_makes_internal_accounting_unavailable(tmp_path):
    r = _runner()
    out_dir = tmp_path / "shadow"

    class NoCallClient:
        def __init__(self, model, **kwargs):
            self.model = model
            self.max_tokens = kwargs["max_tokens"]
            self.usage_log = []

    def fatal_qualification(client, *, name, family, slug, **_kwargs):
        client.guard.block_fatal("synthetic fatal evidence error")
        return _complete_qualification(r, name, family, slug)

    snapshots = iter(
        [
            {"usage": 1.0, "limit_remaining": 9.0},
            {"usage": 1.0, "limit_remaining": 9.0},
        ]
    )
    outcome = r.execute_live(
        "secret",
        out_dir=str(out_dir),
        key_fetch=lambda _key: next(snapshots),
        catalog_fetch=lambda _key: _live_catalog(r),
        client_builder=NoCallClient,
        qualify_fn=fatal_qualification,
        selection_fn=lambda **_kwargs: _live_selection(),
        score_fn=lambda *_args, **_kwargs: [],
    )

    metadata = json.loads((out_dir / "shadow-run-metadata.json").read_text())
    assert outcome.internal_total_usd is None
    assert "fatal evidence" in outcome.partial_reason
    assert metadata["reconciliation"]["status"] == "UNRECONCILED"


def test_late_sink_failure_preserves_persisted_verdict_progress(
    monkeypatch, tmp_path
):
    r = _runner()
    out_dir = tmp_path / "shadow"
    original_write = r.JsonlSink.write
    shadow_writes = {"count": 0}

    def fail_fourth_shadow_write(self, record):
        if record.get("kind") == "shadow_verdict":
            shadow_writes["count"] += 1
            if shadow_writes["count"] == 4:
                raise RuntimeError("late shadow sink failure")
        original_write(self, record)

    monkeypatch.setattr(r.JsonlSink, "write", fail_fourth_shadow_write)

    class NoCallClient:
        def __init__(self, model, **kwargs):
            self.model = model
            self.max_tokens = kwargs["max_tokens"]
            self.usage_log = []
            self.last_finish_reason = "stop"
            self.last_truncated = False

    def fake_qualify(_client, *, name, family, slug, **_kwargs):
        return _complete_qualification(r, name, family, slug)

    def late_failing_score(selection, *, sink, **_kwargs):
        for unit in selection[:4]:
            sink.write(
                {
                    "kind": "shadow_verdict",
                    "judge": r.CANDIDATES[0][0],
                    "surface": unit["surface"],
                    "item_id": unit["item_id"],
                    "sut_slug": unit["sut_slug"],
                    "response_sha256": unit["response_sha256"],
                    "result": None,
                    "error": "synthetic",
                }
            )
        return []

    snapshots = iter(
        [
            {"usage": 1.0, "limit_remaining": 9.0},
            {"usage": 1.0, "limit_remaining": 9.0},
        ]
    )
    outcome = r.execute_live(
        "secret",
        out_dir=str(out_dir),
        key_fetch=lambda _key: next(snapshots),
        catalog_fetch=lambda _key: _live_catalog(r),
        client_builder=NoCallClient,
        qualify_fn=fake_qualify,
        selection_fn=lambda **_kwargs: _exact_selection(r),
        score_fn=late_failing_score,
        now=lambda: "2026-07-12T00:00:00",
    )

    metadata = json.loads((out_dir / "shadow-run-metadata.json").read_text())
    assert outcome.partial_reason
    assert "late shadow sink failure" in outcome.partial_reason
    assert len(outcome.verdicts) == 3
    assert metadata["shadow_verdicts_recorded"] == 3
    assert metadata["probe_reps_recorded"] == 96
    assert metadata["run_status"] == "PARTIAL"


def test_candidate_one_qualification_is_recovered_when_candidate_two_fails(
    tmp_path,
):
    r = _runner()
    out_dir = tmp_path / "shadow"

    class NoCallClient:
        def __init__(self, model, **kwargs):
            self.model = model
            self.max_tokens = kwargs["max_tokens"]
            self.usage_log = []

    def second_candidate_fails(_client, *, name, family, slug, **_kwargs):
        if name == r.CANDIDATES[1][0]:
            raise RuntimeError("candidate two failed")
        return _complete_qualification(r, name, family, slug)

    snapshots = iter(
        [
            {"usage": 1.0, "limit_remaining": 9.0},
            {"usage": 1.0, "limit_remaining": 9.0},
        ]
    )
    outcome = r.execute_live(
        "secret",
        out_dir=str(out_dir),
        key_fetch=lambda _key: next(snapshots),
        catalog_fetch=lambda _key: _live_catalog(r),
        client_builder=NoCallClient,
        qualify_fn=second_candidate_fails,
        selection_fn=lambda **_kwargs: _live_selection(),
        score_fn=lambda *_args, **_kwargs: [],
    )

    metadata = json.loads((out_dir / "shadow-run-metadata.json").read_text())
    first_name = r.CANDIDATES[0][0]
    assert set(outcome.qualifications) == {first_name}
    recovered = outcome.qualifications[first_name]
    assert isinstance(recovered, JudgeQualification)
    assert all(recovered.probe_reps[probe].n_pass == r.K for probe in r.PROBES)
    assert metadata["probe_reps_recorded"] == 48
    assert metadata["qualification_complete"] is False
    assert metadata["run_status"] == "PARTIAL"


@pytest.mark.parametrize("invalid_total", [float("nan"), float("inf"), -0.01])
def test_invalid_internal_total_is_conservative_partial(
    monkeypatch, invalid_total, tmp_path
):
    r = _runner()
    out_dir = tmp_path / "shadow"

    class InvalidTotalGuard(r.BudgetGuard):
        def total_usd(self):
            return invalid_total

    class NoCallClient:
        def __init__(self, model, **kwargs):
            self.model = model
            self.max_tokens = kwargs["max_tokens"]
            self.usage_log = []

    monkeypatch.setattr(r, "BudgetGuard", InvalidTotalGuard)
    snapshots = iter(
        [
            {"usage": 1.0, "limit_remaining": 9.0},
            {"usage": 1.0, "limit_remaining": 9.0},
        ]
    )
    outcome = r.execute_live(
        "secret",
        out_dir=str(out_dir),
        key_fetch=lambda _key: next(snapshots),
        catalog_fetch=lambda _key: _live_catalog(r),
        client_builder=NoCallClient,
        qualify_fn=lambda _client, **kwargs: {"name": kwargs["name"]},
        selection_fn=lambda **_kwargs: _live_selection(),
        score_fn=lambda *_args, **_kwargs: [],
    )

    metadata = json.loads((out_dir / "shadow-run-metadata.json").read_text())
    assert outcome.internal_total_usd is None
    assert "internal total" in outcome.partial_reason
    assert metadata["internal_total_usd"] is None
    assert metadata["reconciliation"]["status"] == "UNRECONCILED"
    assert metadata["run_status"] == "PARTIAL"


@pytest.mark.parametrize(
    "internal,before,after,expected_status,reason",
    [
        (0.0, {"usage": 1.0}, None, "UNRECONCILED", "unavailable"),
        (
            0.0,
            {"usage": 1.0},
            {"usage": float("nan")},
            "UNRECONCILED",
            "finite",
        ),
        (
            0.0,
            {"usage": 1.0},
            {"usage": 0.5},
            "UNRECONCILED",
            "negative",
        ),
        (
            0.5,
            {"usage": 1.0},
            {"usage": 2.1},
            "UNRECONCILED",
            "budget",
        ),
        (
            0.001,
            {"usage": 1.0},
            {"usage": 1.01},
            "UNRECONCILED",
            "20%",
        ),
        (
            0.002,
            {"usage": 1.0},
            {"usage": 1.002},
            "RECONCILED",
            None,
        ),
        (0.0, {"usage": 1.0}, {"usage": 1.0}, "RECONCILED", None),
    ],
)
def test_key_reconciliation_status(
    internal, before, after, expected_status, reason
):
    r = _runner()
    result = r.build_reconciliation(
        internal_total=internal,
        key_before=before,
        key_after=after,
        budget=1.0,
    )

    assert result["status"] == expected_status
    if reason is None:
        assert result["within_20_percent"] is True
        assert result["unavailable_reason"] is None
    else:
        assert reason in result["unavailable_reason"]


def test_invalid_key_after_becomes_reconciliation_partial(tmp_path):
    r = _runner()
    out_dir = tmp_path / "shadow"

    class NoCallClient:
        def __init__(self, model, **kwargs):
            self.model = model
            self.max_tokens = kwargs["max_tokens"]
            self.usage_log = []

    snapshots = iter(
        [
            {"usage": 1.0, "limit_remaining": 9.0},
            {"usage": float("nan"), "limit_remaining": 9.0},
        ]
    )
    outcome = r.execute_live(
        "secret",
        out_dir=str(out_dir),
        key_fetch=lambda _key: next(snapshots),
        catalog_fetch=lambda _key: _live_catalog(r),
        client_builder=NoCallClient,
        qualify_fn=lambda _client, **kwargs: {"name": kwargs["name"]},
        selection_fn=lambda **_kwargs: _live_selection(),
        score_fn=lambda *_args, **_kwargs: [],
    )

    metadata = json.loads((out_dir / "shadow-run-metadata.json").read_text())
    assert outcome.partial_reason
    assert "key-after" in outcome.partial_reason
    assert metadata["run_status"] == "PARTIAL"
    assert metadata["reconciliation"]["status"] == "UNRECONCILED"


def test_comparator_and_candidate_values_are_surface_specific():
    r = _runner()
    unit = {"axis": "manner"}
    comparator = {
        "scores": {
            "awards": {"1": True, "2": False},
            "manner": 0.75,
            "disclosure": 0.5,
        }
    }

    assert r.comparator_value("open_award", comparator, unit) == {
        1: True,
        2: False,
    }
    assert r.comparator_value("coherence", comparator, unit) == 0.75
    assert r.comparator_value("disclosure", comparator, unit) == 0.5
    settled = {
        "scores": {"settled_core_fraction": 1.0},
        "verdict_texts": ["unused", "1: correct — explicit reason"],
    }
    item = SimpleNamespace(
        rubric=[SimpleNamespace(anchor="Q152", criterion="floor", axis=None)]
    )
    assert r.comparator_value("settled_core", settled, unit, item=item) == {
        "floor": True
    }
    assert r.candidate_value("open_award", {"awards": {"1": True}}) == {
        "1": True
    }
    assert r.candidate_value("coherence", {"value": 0.75}) == 0.75
    assert r.candidate_value("disclosure", {"value": 0.5}) == 0.5
    assert r.candidate_value(
        "settled_core", {"keypoints": {"floor": True}}
    ) == {"floor": True}


def test_agreement_is_componentwise_and_requires_shared_components():
    r = _runner()
    assert r.agreement({"1": True, "2": False}, {1: True, 2: True}) == {
        "exact": False,
        "component_agreement": 0.5,
        "n_components": 2,
    }
    assert r.agreement({}, {}) == {
        "exact": False,
        "component_agreement": None,
        "n_components": 0,
    }
    assert r.agreement({"1": True}, {1: True, 2: False}) == {
        "exact": False,
        "component_agreement": 0.5,
        "n_components": 2,
    }
    assert r.agreement(0.75, 0.75) == {
        "exact": True,
        "component_agreement": 1.0,
        "n_components": 1,
    }


def test_agreement_rows_require_exact_response_identity_and_known_comparator():
    r = _runner()
    selection = [
        {
            "surface": "disclosure",
            "item_id": "I1",
            "sut_slug": "sut",
            "response_sha256": "same-response",
            "comparators": {
                "gemini-flash": {"scores": {"disclosure": 0.5}},
                "grok-4.20": {"scores": {"disclosure": None}},
                "gpt4omini": {"scores": {"disclosure": 0.5}},
            },
        }
    ]
    verdicts = [
        {
            "judge": "glm-5.2",
            "surface": "disclosure",
            "item_id": "I1",
            "sut_slug": "sut",
            "response_sha256": "same-response",
            "result": {"graded": True, "value": 0.5},
            "error": None,
        },
        {
            "judge": "deepseek-v4-pro",
            "surface": "disclosure",
            "item_id": "I1",
            "sut_slug": "sut",
            "response_sha256": "different-response",
            "result": {"graded": True, "value": 0.5},
            "error": None,
        },
    ]

    assert r.build_agreement_rows(selection, verdicts) == [
        {
            "judge": "glm-5.2",
            "surface": "disclosure",
            "item_id": "I1",
            "sut_slug": "sut",
            "response_sha256": "same-response",
            "comparator": "gemini-flash",
            "exact": True,
            "component_agreement": 1.0,
            "n_components": 1,
        }
    ]


def test_actual_selection_has_reparsed_settled_comparator_coverage():
    r = _runner()
    selection = r.build_selection(
        open_path=r.OPEN_PATH,
        floor_path=r.FLOOR_PATH,
        r33_path=r.R33_PATH,
        bank_dir=r.BANK_DIR,
    )
    evidence = r.build_comparator_evidence(selection)
    counts = {
        (surface, comparator): sum(
            row["surface"] == surface
            and row["comparator"] == comparator
            and row["available"]
            for row in evidence
        )
        for surface in r.SURFACE_COUNTS
        for comparator in ("gemini-flash", "grok-4.20")
    }
    assert counts == {
        ("open_award", "gemini-flash"): 8,
        ("open_award", "grok-4.20"): 8,
        ("coherence", "gemini-flash"): 8,
        ("coherence", "grok-4.20"): 8,
        ("disclosure", "gemini-flash"): 6,
        ("disclosure", "grok-4.20"): 2,
        ("settled_core", "gemini-flash"): 6,
        ("settled_core", "grok-4.20"): 2,
    }
    settled = [row for row in evidence if row["surface"] == "settled_core"]
    assert all(isinstance(row["value"], dict) and row["value"] for row in settled)
    assert len(
        {
            (
                row["item_id"],
                row["sut_slug"],
                row["response_sha256"],
                row["source_run"],
                row["comparator"],
            )
            for row in settled
        }
    ) == len(settled)


def test_agreement_summary_retains_failures_in_fixed_denominators():
    r = _runner()
    selection = []
    verdicts = []
    for index in range(6):
        unit = {
            "surface": "disclosure",
            "item_id": f"I{index}",
            "sut_slug": "sut",
            "response_sha256": f"hash-{index}",
            "source_run": "synthetic",
            "comparators": (
                {"gemini-flash": {"scores": {"disclosure": 0.5}}}
                if index < 2
                else {}
            ),
        }
        selection.append(unit)
        verdicts.append(
            {
                "judge": "glm-5.2",
                "surface": "disclosure",
                "item_id": unit["item_id"],
                "sut_slug": "sut",
                "response_sha256": unit["response_sha256"],
                "result": (
                    {"graded": True, "value": 0.5}
                    if index != 1
                    else None
                ),
                "error": "failed" if index == 1 else None,
            }
        )
    evidence = r.build_comparator_evidence(selection)
    rows = r.build_agreement_rows(selection, verdicts, evidence=evidence)
    summary = r.summarize_agreement(selection, verdicts, evidence, rows)
    row = next(
        value
        for value in summary
        if value["judge"] == "glm-5.2"
        and value["surface"] == "disclosure"
        and value["comparator"] == "gemini-flash"
    )
    assert row["planned"] == 6
    assert row["comparator_available_count"] == 2
    assert row["graded_count"] == 5
    assert row["parseable_fraction"] == pytest.approx(5 / 6)
    assert row["exact_agreement_n"] == 1
    assert row["exact_agreement_fraction"] == 1.0
    assert row["disagreement_count"] == 0
    assert row["disagreement_identifiers"] == []
    assert row["component_agreement_numerator"] == 1.0
    assert row["component_agreement_denominator"] == 1
    assert row["component_agreement_fraction"] == 1.0
    no_evidence = next(
        value
        for value in summary
        if value["judge"] == "deepseek-v4-pro"
        and value["surface"] == "disclosure"
        and value["comparator"] == "gemini-flash"
    )
    assert no_evidence["comparator_available_count"] == 2
    assert no_evidence["graded_count"] == 0
    assert no_evidence["exact_agreement_n"] == 0
    assert no_evidence["exact_agreement_fraction"] is None
    assert no_evidence["disagreement_count"] == 0
    assert no_evidence["disagreement_identifiers"] == []
    assert no_evidence["component_agreement_numerator"] == 0.0
    assert no_evidence["component_agreement_denominator"] == 0
    assert no_evidence["component_agreement_fraction"] is None


def test_component_summary_aggregates_open_and_settled_components():
    r = _runner()
    selection = [
        {
            "surface": surface,
            "item_id": item_id,
            "sut_slug": "sut",
            "response_sha256": f"hash-{item_id}",
        }
        for surface, item_id in (
            ("open_award", "O1"),
            ("open_award", "O2"),
            ("settled_core", "S1"),
        )
    ]
    verdicts = [
        {
            "judge": "glm-5.2",
            **{key: unit[key] for key in (
                "surface", "item_id", "sut_slug", "response_sha256"
            )},
            "result": {"graded": True},
            "error": None,
        }
        for unit in selection
    ]
    evidence = [
        {
            **{key: unit[key] for key in (
                "surface", "item_id", "sut_slug", "response_sha256"
            )},
            "source_run": "synthetic",
            "comparator": "gemini-flash",
            "available": True,
        }
        for unit in selection
    ]
    agreement_rows = [
        {
            "judge": "glm-5.2",
            **{key: unit[key] for key in (
                "surface", "item_id", "sut_slug", "response_sha256"
            )},
            "comparator": "gemini-flash",
            "exact": exact,
            "component_agreement": component_fraction,
            "n_components": 2,
        }
        for unit, exact, component_fraction in zip(
            selection,
            (False, True, False),
            (0.5, 1.0, 0.5),
        )
    ]
    summary = r.summarize_agreement(
        selection, verdicts, evidence, agreement_rows
    )
    open_row = next(
        row for row in summary
        if row["judge"] == "glm-5.2"
        and row["surface"] == "open_award"
        and row["comparator"] == "gemini-flash"
    )
    settled_row = next(
        row for row in summary
        if row["judge"] == "glm-5.2"
        and row["surface"] == "settled_core"
        and row["comparator"] == "gemini-flash"
    )
    assert open_row["component_agreement_numerator"] == 3.0
    assert open_row["component_agreement_denominator"] == 4
    assert open_row["component_agreement_fraction"] == 0.75
    assert settled_row["component_agreement_numerator"] == 1.0
    assert settled_row["component_agreement_denominator"] == 2
    assert settled_row["component_agreement_fraction"] == 0.5


def test_operational_summary_prefers_actual_cost_then_catalog_fallback():
    r = _runner()
    name, family, slug = r.CANDIDATES[0]
    raw = [
        {
            "kind": "raw_call",
            "judge": name,
            "family": family,
            "slug": slug,
            "attempt": 0,
            "phase": "qualification",
            "truncated": False,
            "error": None,
            "usage": [
                {
                    "usage": {
                        "prompt_tokens": 10,
                        "completion_tokens": 5,
                        "cost": 0.002,
                    }
                }
            ],
        },
        {
            "kind": "raw_call",
            "judge": name,
            "family": family,
            "slug": slug,
            "attempt": 1,
            "phase": "real_response",
            "truncated": True,
            "error": "transient",
            "usage": [
                {"usage": {"prompt_tokens": 3, "completion_tokens": 2}}
            ],
        },
        {
            "kind": "call_timing",
            "judge": name,
            "phase": "qualification",
            "elapsed_seconds": 0.2,
        },
        {
            "kind": "call_timing",
            "judge": name,
            "phase": "real_response",
            "elapsed_seconds": 0.4,
        },
    ]
    verdicts = [
        {"judge": name, "result": {"graded": True}, "error": None},
        {"judge": name, "result": None, "error": "parse failed"},
    ]
    operations = r.operational_summary(raw, verdicts, _live_catalog(r))

    assert operations[name] == {
        "calls": 2,
        "retries": 1,
        "truncations": 1,
        "prompt_tokens": 13,
        "completion_tokens": 7,
        "actual_cost_usd": pytest.approx(0.002005),
        "mean_call_seconds": pytest.approx(0.3),
        "parse_fraction": 0.5,
        "errors": 1,
        "by_surface": {
            surface: {
                "planned": count,
                "graded": 0,
                "parseable_fraction": 0.0,
                "errors": 0,
            }
            for surface, count in r.SURFACE_COUNTS.items()
        },
        "by_phase": {
            "qualification": {
                "calls": 1,
                "retries": 0,
                "truncations": 0,
                "prompt_tokens": 10,
                "completion_tokens": 5,
                "actual_cost_usd": pytest.approx(0.002),
                "mean_call_seconds": pytest.approx(0.2),
                "errors": 0,
            },
            "real_response": {
                "calls": 1,
                "retries": 1,
                "truncations": 1,
                "prompt_tokens": 3,
                "completion_tokens": 2,
                "actual_cost_usd": pytest.approx(0.000005),
                "mean_call_seconds": pytest.approx(0.4),
                "errors": 1,
            },
        },
    }
    assert operations[r.CANDIDATES[1][0]]["calls"] == 0
    assert operations[r.CANDIDATES[1][0]]["actual_cost_usd"] == 0.0


def test_qualification_summary_labels_and_componentwise_pareto():
    r = _runner()
    qualifications = _complete_qualifications(r)
    qualifications[r.CANDIDATES[0][0]].surfaces = set(r.SURFACE_COUNTS)
    qualifications[r.CANDIDATES[1][0]].surfaces = {"coherence"}
    summary = r.qualification_summary(qualifications)
    assert summary[r.CANDIDATES[0][0]]["eligible_surfaces"] == sorted(
        r.SURFACE_COUNTS
    )
    assert summary[r.CANDIDATES[0][0]]["probes"]["g4"] == {
        "n_pass": r.K,
        "k": r.K,
        "cause_tally": {"pass": r.K},
    }
    labels = r.candidate_labels(
        qualifications[r.CANDIDATES[1][0]],
        "deepseek",
        0.0,
        insufficient=True,
    )
    assert "SHADOW-ELIGIBLE FOR coherence" in labels
    assert "SHADOW-INELIGIBLE FOR open_award" in labels
    assert "INDEPENDENCE-CONFLICTED" in labels
    assert "INSUFFICIENT EVIDENCE" in labels

    operations = {
        r.CANDIDATES[0][0]: {
            "parse_fraction": 1.0,
            "actual_cost_usd": 0.1,
        },
        r.CANDIDATES[1][0]: {
            "parse_fraction": 0.5,
            "actual_cost_usd": 0.2,
        },
    }
    assert r.pareto_names(qualifications, operations) == [r.CANDIDATES[0][0]]


def test_report_forbids_accuracy_and_production_effect():
    r = _runner()
    qualifications = _complete_qualifications(r)
    report = r.build_report(
        {
            "artifact_kind": "SHADOW / NOT A QUALIFICATION MANIFEST",
            "run_status": "COMPLETE",
            "internal_total_usd": 0.2,
            "partial_reason": None,
            "analysis": {
                "qualification": {},
                "agreement": [],
                "agreement_summary": [
                    {
                        "component_agreement_numerator": 3.0,
                        "component_agreement_denominator": 4,
                        "component_agreement_fraction": 0.75,
                    }
                ],
                "comparator_denominators": [],
                "comparator_coverage_complete": True,
                "operations": {},
                "pareto_names": [],
            },
        },
        qualifications,
        [],
        [],
    )
    assert "SHADOW / NOT A QUALIFICATION MANIFEST" in report
    assert "PARETO" in report
    assert "T4" in report
    assert "panel" in report
    assert "manifest" in report
    assert "closed candidate ladder" in report
    assert "score of record" in report
    assert "accuracy" not in report.lower()
    assert "more accurate" not in report.lower()
    assert "production judge" not in report.lower()
    assert "No label authorizes" in report
    assert "component_agreement_numerator" in report
    assert "component_agreement_denominator" in report
    assert "component_agreement_fraction" in report


def test_dry_run_has_zero_network_and_creates_no_directory(
    tmp_path, monkeypatch
):
    r = _runner()
    run_dir = tmp_path / "shadow"
    monkeypatch.setattr(r, "RUN_DIR", str(run_dir))
    monkeypatch.setattr(
        r.mvp, "fetch_key_snapshot", lambda *_a, **_k: 1 / 0
    )
    assert r.main([]) == 0
    assert not run_dir.exists()


def test_cli_requires_key_only_with_go(monkeypatch):
    r = _runner()
    monkeypatch.delenv("OPENROUTER_API_KEY", raising=False)
    assert r.main(["--budget", "1.00"]) == 0
    assert r.main(["--go", "--budget", "1.00"]) == 2
    assert r.main(["--budget", "1.01"]) == 2


def test_fully_mocked_exact_evidence_reaches_complete_with_analysis(tmp_path):
    r = _runner()
    out_dir = tmp_path / "shadow"
    selection = _exact_selection(r)
    bank_items = {item.id: item for item in r.load_items(r.BANK_DIR)}
    for unit in selection:
        if unit["surface"] == "open_award":
            scores = {"awards": {"1": True}}
        elif unit["surface"] == "coherence":
            scores = {unit["axis"]: 1.0}
        elif unit["surface"] == "disclosure":
            scores = {"disclosure": 1.0}
        else:
            scores = {"settled_core_fraction": 1.0}
            verdict = "\n".join(
                f"{index}: correct — explicit reason"
                for index, _keypoint in enumerate(
                    r.settled_core_keypoints(bank_items[unit["item_id"]]), 1
                )
            )
        unit["comparators"] = {"gemini-flash": {"scores": scores}}
        if unit["surface"] == "settled_core":
            unit["comparators"]["gemini-flash"]["verdict_texts"] = [
                "unused",
                verdict,
            ]
        if unit["surface"] in {"open_award", "coherence"} or int(
            unit["sut_slug"].rsplit("-", 1)[-1]
        ) < 2:
            unit["comparators"]["grok-4.20"] = {"scores": scores}
            if unit["surface"] == "settled_core":
                unit["comparators"]["grok-4.20"]["verdict_texts"] = [
                    "unused",
                    verdict,
                ]

    class FakeClient:
        def __init__(self, model, **kwargs):
            self.model = model
            self.max_tokens = kwargs["max_tokens"]
            self.usage_log = []
            self.last_finish_reason = "stop"
            self.last_truncated = False

        def complete(self, prompt, item_id=None):
            self.usage_log.append(
                {
                    "usage": {
                        "prompt_tokens": 1,
                        "completion_tokens": 1,
                        "total_tokens": 2,
                        "cost": 0.001,
                    }
                }
            )
            return "synthetic"

    def fake_qualify(client, *, name, family, slug, **_kwargs):
        client.complete("probe", item_id="QUALIFICATION")
        qualification = _complete_qualification(r, name, family, slug)
        qualification.surfaces = set(r.SURFACE_COUNTS)
        return qualification

    def fake_score(units, *, clients, sink, now, **_kwargs):
        records = []
        for name, client in clients.items():
            client.complete("real response", item_id=f"REAL-{name}")
        for name, _family, _slug in r.CANDIDATES:
            for unit in units:
                if unit["surface"] == "open_award":
                    result = {"graded": True, "awards": {"1": True}}
                elif unit["surface"] in {"coherence", "disclosure"}:
                    result = {"graded": True, "value": 1.0}
                else:
                    result = {
                        "graded": True,
                        "keypoints": {"floor": True},
                    }
                record = {
                    "kind": "shadow_verdict",
                    "timestamp": now(),
                    "judge": name,
                    "surface": unit["surface"],
                    "item_id": unit["item_id"],
                    "sut_slug": unit["sut_slug"],
                    "response_sha256": unit["response_sha256"],
                    "elapsed_seconds": 0.0,
                    "result": result,
                    "error": None,
                }
                sink.write(record)
                records.append(record)
        return records

    snapshots = iter(
        [
            {"usage": 1.0, "limit_remaining": 9.0},
            {"usage": 1.004, "limit_remaining": 8.996},
        ]
    )
    outcome = r.execute_live(
        "secret",
        out_dir=str(out_dir),
        key_fetch=lambda _key: next(snapshots),
        catalog_fetch=lambda _key: _live_catalog(r),
        client_builder=FakeClient,
        qualify_fn=fake_qualify,
        selection_fn=lambda **_kwargs: selection,
        score_fn=fake_score,
        now=lambda: "2026-07-12T00:00:00",
    )

    metadata = json.loads((out_dir / "shadow-run-metadata.json").read_text())
    report = (out_dir / "20260712-shadow-judge-bakeoff-report.md").read_text()
    assert outcome.partial_reason is None
    assert metadata["run_status"] == "COMPLETE"
    assert metadata["analysis"]["pareto_names"] == sorted(
        name for name, _family, _slug in r.CANDIDATES
    )
    assert len(metadata["analysis"]["agreement"]) == 96
    assert len(metadata["analysis"]["agreement_summary"]) == 16
    assert all(
        row["planned"] == r.SURFACE_COUNTS[row["surface"]]
        for row in metadata["analysis"]["agreement_summary"]
    )
    assert metadata["analysis"]["operations"]["glm-5.2"]["calls"] == 2
    assert metadata["analysis"]["operations"]["glm-5.2"]["by_phase"][
        "qualification"
    ]["calls"] == 1
    assert metadata["analysis"]["operations"]["glm-5.2"]["by_phase"][
        "real_response"
    ]["calls"] == 1
    assert "SHADOW / NOT A QUALIFICATION MANIFEST" in report
    assert "accuracy" not in report.lower()
    assert not any("manifest" in path.name.lower() for path in out_dir.iterdir())


def test_post_call_analysis_failure_preserves_partial_artifacts(
    monkeypatch, tmp_path
):
    r = _runner()
    out_dir = tmp_path / "shadow"

    class FakeClient:
        def __init__(self, model, **kwargs):
            self.model = model
            self.max_tokens = kwargs["max_tokens"]
            self.usage_log = []
            self.last_finish_reason = "stop"
            self.last_truncated = False

        def complete(self, prompt, item_id=None):
            self.usage_log.append(
                {
                    "usage": {
                        "prompt_tokens": 1,
                        "completion_tokens": 1,
                        "cost": 0.001,
                    }
                }
            )
            return "synthetic"

    def fake_qualify(client, **kwargs):
        client.complete("paid probe", item_id="PROBE")
        return {"name": kwargs["name"]}

    monkeypatch.setattr(
        r,
        "operational_summary",
        lambda *_args, **_kwargs: (_ for _ in ()).throw(
            RuntimeError("analysis normalization failed")
        ),
    )
    snapshots = iter(
        [
            {"usage": 1.0, "limit_remaining": 9.0},
            {"usage": 1.002, "limit_remaining": 8.998},
        ]
    )
    outcome = r.execute_live(
        "secret",
        out_dir=str(out_dir),
        key_fetch=lambda _key: next(snapshots),
        catalog_fetch=lambda _key: _live_catalog(r),
        client_builder=FakeClient,
        qualify_fn=fake_qualify,
        selection_fn=lambda **_kwargs: _live_selection(),
        score_fn=lambda *_args, **_kwargs: [],
    )

    metadata = json.loads((out_dir / "shadow-run-metadata.json").read_text())
    report = (out_dir / "20260712-shadow-judge-bakeoff-report.md").read_text()
    assert "analysis normalization failed" in outcome.partial_reason
    assert metadata["run_status"] == "PARTIAL"
    assert metadata["analysis"]["pareto_names"] == []
    assert "PARTIAL" in report
    assert (out_dir / "raw_verdicts.jsonl").stat().st_size > 0
