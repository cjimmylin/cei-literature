"""MF-6 binding execution-order, session-isolation, and safe-run gates."""
from __future__ import annotations

import json
import copy
import inspect
import random
import stat
import sys
from pathlib import Path

import pytest


PKG = Path(__file__).resolve().parents[1]
for path in (PKG, PKG / "harness", PKG / "scoring"):
    sys.path.insert(0, str(path))

import harness.run_p1 as run_p1  # noqa: E402
from harness.model_client import ModelClient, MockModelClient  # noqa: E402


def _api(name):
    value = getattr(run_p1, name, None)
    assert callable(value), f"missing callable run_p1.{name}"
    return value


def _config(tmp_path: Path, *, run_id="mf6-smoke", models=("mock-alpha",), repeats=1):
    cls = getattr(run_p1, "RunConfig", None)
    assert cls is not None, "missing run_p1.RunConfig"
    return cls(
        run_date="20260710",
        run_id=run_id,
        output_dir=tmp_path / f"20260710-{run_id}",
        models=models,
        repeats=repeats,
    )


def _read_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def test_run_config_validates_date_run_id_output_path_models_and_repeats(tmp_path):
    cls = getattr(run_p1, "RunConfig", None)
    error = getattr(run_p1, "RunConfigError", ValueError)
    assert cls is not None
    valid = _config(tmp_path)
    assert valid.output_dir.is_absolute()

    for bad_date in ("2026-07-10", "20260230", ""):
        with pytest.raises(error):
            cls(bad_date, "mf6", tmp_path / f"{bad_date}-mf6", ("mock-alpha",), 1)
    for bad_id in ("", "../escape", "bad/name", "."):
        with pytest.raises(error):
            cls("20260710", bad_id, tmp_path / "invalid", ("mock-alpha",), 1)
    with pytest.raises(error, match="absolute"):
        cls("20260710", "mf6", Path("relative/20260710-mf6"), ("mock-alpha",), 1)
    with pytest.raises(error, match="date.*run ID|name"):
        cls("20260710", "mf6", tmp_path / "wrong-name", ("mock-alpha",), 1)
    with pytest.raises(error):
        cls("20260710", "mf6", tmp_path / "20260710-mf6", (), 1)
    with pytest.raises(error):
        cls("20260710", "mf6", tmp_path / "20260710-mf6", ("mock-alpha", "mock-alpha"), 1)
    with pytest.raises(error):
        cls("20260710", "mf6", tmp_path / "20260710-mf6", ("mock-alpha",), 0)


def test_stable_session_ids_are_unique_and_input_order_independent(tmp_path):
    config = _config(tmp_path)
    session_id = _api("stable_session_id")
    calls = [
        ("mock-alpha", "item-a", 0, True),
        ("mock-alpha", "item-a", 0, False),
        ("mock-alpha", "item-a", 1, True),
        ("mock-alpha", "item-b", 0, True),
    ]
    first = [session_id(config, *call) for call in calls]
    second = [session_id(config, *call) for call in reversed(calls)]
    assert first == list(reversed(second))
    assert len(first) == len(set(first))
    assert all(value.startswith("witness-session-") and len(value) == 80 for value in first)


def test_canonical_plan_is_shuffle_independent_and_covers_all_items():
    items = run_p1.load_p1_items()
    shuffled = list(items)
    random.Random(8612).shuffle(shuffled)
    build = _api("build_execution_plan")
    original = build(items)
    reordered = build(shuffled)
    assert original == reordered
    assert len(original) == 45
    planned_items = [item for core in original for _, group in core.items_by_modality
                     for item in group]
    assert len(planned_items) == 300
    assert sum(bool(item.get("is_control")) for item in planned_items) == 60
    assert len({item["item_id"] for item in planned_items}) == 300
    for core in original:
        assert list(core.expected_modality_order) == run_p1._perm(core.core_id)
        assert [modality for modality, _ in core.items_by_modality] == run_p1._perm(
            core.core_id
        )
        for _, group in core.items_by_modality:
            assert list(group) == sorted(
                group, key=lambda item: (item.get("skin", 0), item["item_id"])
            )


def test_forced_modality_swap_aborts_without_provider_or_outputs(tmp_path):
    config = _config(tmp_path)
    calls = {"provider": 0}

    def provider(_name):
        calls["provider"] += 1
        raise AssertionError("provider must not be created after a plan-order fault")

    def swapped(core_id):
        order = run_p1._perm(core_id)
        order[0], order[1] = order[1], order[0]
        return order

    error = getattr(run_p1, "RunOrderError", AssertionError)
    with pytest.raises(error, match="expected.*actual|modality order"):
        _api("execute_run")(
            config,
            items_loader=run_p1.load_p1_items,
            client_factory=provider,
            actual_order_fn=swapped,
        )
    assert calls["provider"] == 0
    assert not config.output_dir.exists()


def test_existing_run_directory_is_refused_before_item_or_provider_work(tmp_path):
    config = _config(tmp_path)
    config.output_dir.mkdir()
    sentinel = config.output_dir / "sentinel.txt"
    sentinel.write_text("frozen\n")
    calls = {"items": 0, "provider": 0}

    def items_loader():
        calls["items"] += 1
        raise AssertionError("items must not load for an existing run directory")

    def provider(_name):
        calls["provider"] += 1
        raise AssertionError("provider must not initialize for an existing run directory")

    error = getattr(run_p1, "RunRefusedError", RuntimeError)
    with pytest.raises(error, match="exists|refus"):
        _api("execute_run")(config, items_loader=items_loader, client_factory=provider)
    assert calls == {"items": 0, "provider": 0}
    assert sentinel.read_text() == "frozen\n"


def test_full_mock_run_binds_order_sessions_manifest_audit_and_coverage(tmp_path):
    config = _config(tmp_path)
    provider_calls = []

    class RecordingMock(MockModelClient):
        def respond(self, item, monitored=True, rep=0, session_id=None):
            provider_calls.append({
                "core_id": item["core_id"], "item_id": item["item_id"],
                "modality": item["modality"], "skin": item.get("skin", 0),
                "rep": rep, "monitored": monitored, "session_id": session_id,
            })
            return super().respond(
                item, monitored=monitored, rep=rep, session_id=session_id
            )

    manifest = _api("execute_run")(
        config, client_factory=lambda name: RecordingMock(name)
    )
    assert manifest["schema_version"] == "witness-run-manifest-v1"
    assert manifest["run_date"] == config.run_date
    assert manifest["run_id"] == config.run_id
    assert manifest["execution_type"] == "SIMULATED"
    assert manifest["evidence"] == "SIMULATED"
    assert manifest["models"] == [
        {
            "name": "mock-alpha", "execution_type": "SIMULATED",
            "evidence": "SIMULATED", "family": "mock-simulator",
        }
    ]
    assert manifest["repeats"] == 1
    assert manifest["n_items"] == 300
    assert manifest["n_control_items"] == 60
    assert manifest["n_cores"] == 45
    assert manifest["n_sessions"] == 345
    assert manifest["completed"] is True

    assert sorted(path.name for path in config.output_dir.iterdir()) == [
        "audit_log.jsonl", "qc.json", "run_manifest.json", "scored.jsonl",
    ]
    assert json.loads((config.output_dir / "run_manifest.json").read_text()) == manifest
    audit = _read_jsonl(config.output_dir / "audit_log.jsonl")
    scored = _read_jsonl(config.output_dir / "scored.jsonl")
    assert len(audit) == 45
    assert len(scored) == 345
    assert sum(row["is_control"] for row in scored if row["monitored"]) == 60
    assert all(row["execution_type"] == "SIMULATED" for row in scored)
    assert all(row["evidence"] == "SIMULATED" for row in scored)
    assert all(row["run_id"] == config.run_id for row in scored)

    session_ids = []
    logged_items = []
    for record in audit:
        assert record["schema_version"] == "witness-session-audit-v1"
        assert record["run_id"] == config.run_id
        assert record["model"] == "mock-alpha"
        assert record["execution_type"] == "SIMULATED"
        assert record["evidence"] == "SIMULATED"
        assert record["family"] == "mock-simulator"
        assert record["expected_modality_order"] == run_p1._perm(record["core_id"])
        assert record["actual_modality_order"] == record["expected_modality_order"]
        assert record["assertions"] == {
            "modality_order_matches": True,
            "item_coverage_complete": True,
            "sessions_complete": True,
            "fresh_client_per_session": True,
        }
        assert record["completed"] is True
        logged_items.extend(record["item_ids"])
        session_ids.extend(call["session_id"] for call in record["sessions"])
    assert len(logged_items) == len(set(logged_items)) == 300
    assert len(session_ids) == len(set(session_ids)) == 345
    assert {row["session_id"] for row in scored} == set(session_ids)

    plan = {core.core_id: core for core in run_p1.build_execution_plan(
        run_p1.load_p1_items()
    )}
    for core_id, core in plan.items():
        calls = [call for call in provider_calls if call["core_id"] == core_id]
        observed_modalities = []
        for call in calls:
            if call["modality"] not in observed_modalities:
                observed_modalities.append(call["modality"])
        assert observed_modalities == run_p1._perm(core_id)
        observed_items = [
            call["item_id"] for call in calls
            if call["monitored"] and call["rep"] == 0
        ]
        expected_items = [
            item["item_id"] for _, group in core.items_by_modality for item in group
        ]
        assert observed_items == expected_items


def test_mock_clients_are_explicitly_simulated():
    client = MockModelClient("mock-alpha")
    assert client.execution_type == "SIMULATED"
    assert client.family == "mock-simulator"


def test_gen_vote_ties_use_a_fixed_hash_seed_independent_pole_order():
    resolve = _api("resolve_judge_votes")
    assert resolve(["counterfeit", "gold"]) == "gold"
    assert resolve(["gold", "counterfeit"]) == "gold"
    assert resolve(["neutral", "deficient"]) == "deficient"


def test_provider_without_recognized_execution_type_is_refused_without_outputs(tmp_path):
    config = _config(tmp_path)

    class UndeclaredProvider(ModelClient):
        def respond(self, *_args, **_kwargs):
            raise AssertionError("undeclared provider must not receive a session")

    error = getattr(run_p1, "RunProviderError", RuntimeError)
    with pytest.raises(error, match="execution_type|SIMULATED|LIVE"):
        _api("execute_run")(config, client_factory=lambda _name: UndeclaredProvider())
    assert not config.output_dir.exists()


def test_every_session_uses_a_distinct_one_call_client_with_no_retained_state(tmp_path):
    config = _config(tmp_path)
    instances = []

    class StatefulMock(MockModelClient):
        def __init__(self, name):
            super().__init__(name)
            self.calls = 0
            instances.append(self)

        def respond(self, item, monitored=True, rep=0, session_id=None):
            self.calls += 1
            assert self.calls == 1, "session client retained context across calls"
            return super().respond(
                item, monitored=monitored, rep=rep, session_id=session_id
            )

    manifest = _api("execute_run")(
        config, client_factory=lambda name: StatefulMock(name)
    )
    assert manifest["n_sessions"] == 345
    assert len(instances) == 346  # one metadata probe plus one instance per session
    assert instances[0].calls == 0
    assert all(instance.calls == 1 for instance in instances[1:])
    assert len({id(instance) for instance in instances}) == len(instances)
    audit = _read_jsonl(config.output_dir / "audit_log.jsonl")
    assert all(row["assertions"]["fresh_client_per_session"] for row in audit)


def test_reused_session_client_is_rejected_before_a_second_response(tmp_path):
    config = _config(tmp_path)
    shared = MockModelClient("mock-alpha")
    responses = 0

    original = shared.respond

    def counted(*args, **kwargs):
        nonlocal responses
        responses += 1
        return original(*args, **kwargs)

    shared.respond = counted
    with pytest.raises(run_p1.RunProviderError, match="reus|fresh|distinct"):
        _api("execute_run")(config, client_factory=lambda _name: shared)
    assert responses <= 1
    assert not config.output_dir.exists()


@pytest.mark.parametrize("mutation", [
    "moral_skin", "moral_holdout", "moral_item_id", "control_base", "control_skin",
])
def test_exact_moral_and_control_structure_is_enforced(mutation):
    items = copy.deepcopy(run_p1.load_p1_items())
    if mutation.startswith("moral"):
        row = next(item for item in items if not item["is_control"] and item["skin"] == 1)
        if mutation == "moral_skin":
            row["skin"] = 0
        elif mutation == "moral_holdout":
            row["holdout"] = not row["holdout"]
        else:
            row["item_id"] = row["item_id"] + "-forged"
    else:
        row = next(item for item in items if item["is_control"])
        if mutation == "control_base":
            row["control_base_id"] = "CTRL-forged"
        else:
            row["skin"] = 1
    with pytest.raises(run_p1.RunCoverageError):
        run_p1.build_execution_plan(items)


def test_mid_stage_write_failure_aborts_early_and_leaves_no_final_or_claim(tmp_path):
    config = _config(tmp_path)
    writes = 0
    responses = 0
    real_write = _api("stage_write_text")

    class CountingMock(MockModelClient):
        def respond(self, *args, **kwargs):
            nonlocal responses
            responses += 1
            return super().respond(*args, **kwargs)

    def failing_write(path, payload, append):
        nonlocal writes
        writes += 1
        if writes == 8:
            raise OSError("injected staged write failure")
        real_write(path, payload, append)

    with pytest.raises(OSError, match="injected staged write"):
        _api("execute_run")(
            config,
            client_factory=lambda name: CountingMock(name),
            stage_write_fn=failing_write,
        )
    assert 0 < responses < 345
    assert not config.output_dir.exists()
    assert not _api("reservation_path")(config.output_dir).exists()
    assert not list(config.output_dir.parent.glob(f".{config.output_dir.name}.staging-*"))
    failed = list(config.output_dir.parent.glob(f".{config.output_dir.name}.failed-*"))
    assert len(failed) == 1
    assert {path.name for path in failed[0].iterdir()} == {
        "audit_log.jsonl", "scored.jsonl",
    }


def test_silent_stage_write_loss_is_detected_before_full_provider_spend(tmp_path):
    config = _config(tmp_path, run_id="silent-loss")
    writes = 0
    responses = 0
    real_write = _api("stage_write_text")

    class CountingMock(MockModelClient):
        def respond(self, *args, **kwargs):
            nonlocal responses
            responses += 1
            return super().respond(*args, **kwargs)

    def lossy_write(path, payload, append):
        nonlocal writes
        writes += 1
        if writes != 8:
            real_write(path, payload, append)

    with pytest.raises(run_p1.RunCoverageError, match="stage|write|payload"):
        run_p1.execute_run(
            config,
            client_factory=lambda name: CountingMock(name),
            stage_write_fn=lossy_write,
        )
    assert 0 < responses < 345
    assert not config.output_dir.exists()


def test_competitor_race_preserves_sentinel_and_avoids_full_provider_spend(tmp_path):
    config = _config(tmp_path)
    writes = 0
    responses = 0
    real_write = _api("stage_write_text")

    class CountingMock(MockModelClient):
        def respond(self, *args, **kwargs):
            nonlocal responses
            responses += 1
            return super().respond(*args, **kwargs)

    def racing_write(path, payload, append):
        nonlocal writes
        writes += 1
        real_write(path, payload, append)
        if writes == 5:
            config.output_dir.mkdir()
            (config.output_dir / "competitor.txt").write_text("sentinel\n")

    with pytest.raises(run_p1.RunRefusedError, match="race|appeared|reserved"):
        _api("execute_run")(
            config,
            client_factory=lambda name: CountingMock(name),
            stage_write_fn=racing_write,
        )
    assert 0 < responses < 345
    assert (config.output_dir / "competitor.txt").read_text() == "sentinel\n"
    assert sorted(path.name for path in config.output_dir.iterdir()) == ["competitor.txt"]
    assert not _api("reservation_path")(config.output_dir).exists()
    assert len(list(config.output_dir.parent.glob(
        f".{config.output_dir.name}.failed-*"
    ))) == 1


def test_runner_contains_no_deletion_api_and_failed_publications_are_preserved():
    source = inspect.getsource(run_p1)
    for forbidden in (".unlink(", ".rmdir(", "rmtree(", "os.remove("):
        assert forbidden not in source


def test_claim_directory_is_created_owner_only(tmp_path):
    config = _config(tmp_path, run_id="owner-only-claim")
    claim, token, stage = run_p1._claim_run_directory(config.output_dir)
    try:
        assert stage == claim
        assert stat.S_IMODE(claim.stat().st_mode) == 0o700
    finally:
        run_p1._preserve_failed_publication(config.output_dir, stage, claim, token)


def test_empty_competitor_at_publish_seam_is_never_replaced(tmp_path):
    config = _config(tmp_path, run_id="empty-publish-race")

    def create_empty_competitor():
        config.output_dir.mkdir()

    with pytest.raises(run_p1.RunRefusedError, match="no.?replace|exists|publish"):
        run_p1.execute_run(config, before_publish_fn=create_empty_competitor)
    assert config.output_dir.is_dir()
    assert list(config.output_dir.iterdir()) == []
    failed = list(config.output_dir.parent.glob(f".{config.output_dir.name}.failed-*"))
    assert len(failed) == 1
    assert {path.name for path in failed[0].iterdir()} == set(run_p1.RUN_OUTPUT_NAMES)


def test_publish_seam_source_swap_is_refused_and_both_sources_are_preserved(tmp_path):
    config = _config(tmp_path, run_id="source-swap")
    claim = run_p1.reservation_path(config.output_dir)
    stolen_stage = config.output_dir.with_name(f".{config.output_dir.name}.stolen-valid")

    def replace_valid_stage_with_attacker():
        claim.rename(stolen_stage)
        claim.mkdir(mode=0o700)
        (claim / "attacker.txt").write_text("attacker\n", encoding="utf-8")

    with pytest.raises(
        (run_p1.RunCoverageError, run_p1.RunRefusedError),
        match="staged|output|reservation|ownership",
    ):
        run_p1.execute_run(config, before_publish_fn=replace_valid_stage_with_attacker)

    assert not config.output_dir.exists()
    assert stolen_stage.is_dir()
    assert {path.name for path in stolen_stage.iterdir()} == set(run_p1.RUN_OUTPUT_NAMES)
    preserved_replacements = [
        path
        for path in (
            claim,
            *config.output_dir.parent.glob(f".{config.output_dir.name}.failed-*"),
        )
        if (path / "attacker.txt").is_file()
    ]
    assert len(preserved_replacements) == 1
    assert (preserved_replacements[0] / "attacker.txt").read_text() == "attacker\n"


def test_publish_seam_in_place_payload_tampering_is_refused_and_preserved(tmp_path):
    config = _config(tmp_path, run_id="payload-tamper")
    claim = run_p1.reservation_path(config.output_dir)

    def tamper_with_valid_stage():
        (claim / "qc.json").write_text('{"attacker": true}\n', encoding="utf-8")

    with pytest.raises(run_p1.RunCoverageError, match="staged QC|completed QC"):
        run_p1.execute_run(config, before_publish_fn=tamper_with_valid_stage)

    assert not config.output_dir.exists()
    failed = list(config.output_dir.parent.glob(f".{config.output_dir.name}.failed-*"))
    assert len(failed) == 1
    assert json.loads((failed[0] / "qc.json").read_text()) == {"attacker": True}


def test_live_preflight_rejects_one_model_and_mixed_evidence_without_calls(tmp_path):
    calls = 0

    class FakeLive(ModelClient):
        execution_type = "LIVE"
        family = "family-a"

        def respond(self, *_args, **_kwargs):
            nonlocal calls
            calls += 1
            raise AssertionError("invalid LIVE metadata must fail before sessions")

    one = _config(tmp_path, run_id="one-live", models=("live-a",), repeats=3)
    with pytest.raises(run_p1.RunProviderError, match=">=4|four|model"):
        run_p1.execute_run(one, client_factory=lambda _name: FakeLive())

    mixed = _config(
        tmp_path, run_id="mixed", models=("live-a", "mock-alpha"), repeats=3
    )
    with pytest.raises(run_p1.RunProviderError, match="mixed|SIMULATED|LIVE"):
        run_p1.execute_run(
            mixed,
            client_factory=lambda name: FakeLive()
            if name == "live-a" else MockModelClient(name),
        )
    assert calls == 0
    assert not one.output_dir.exists() and not mixed.output_dir.exists()


def test_compliant_live_metadata_still_requires_authorized_real_judge_stack(tmp_path):
    config = _config(
        tmp_path,
        run_id="live-no-judge",
        models=("live-a1", "live-a2", "live-b1", "live-b2"),
        repeats=3,
    )
    calls = 0

    class FakeLive(ModelClient):
        execution_type = "LIVE"

        def __init__(self, family):
            self.family = family

        def respond(self, *_args, **_kwargs):
            nonlocal calls
            calls += 1
            raise AssertionError("LIVE sessions require a real judge stack first")

    with pytest.raises(run_p1.RunProviderError, match="judge|authoriz"):
        run_p1.execute_run(
            config,
            client_factory=lambda name: FakeLive(
                "family-a" if "-a" in name else "family-b"
            ),
        )
    assert calls == 0
    assert not config.output_dir.exists()


def test_cli_requires_explicit_run_identity_and_passes_typed_config(tmp_path, monkeypatch):
    captured = []

    def fake_execute(config, **_kwargs):
        captured.append(config)
        return {"run_id": config.run_id, "completed": True}

    monkeypatch.setattr(run_p1, "execute_run", fake_execute, raising=False)
    assert run_p1.main([]) == 2
    output = tmp_path / "20260710-cli-smoke"
    assert run_p1.main([
        "--run-date", "20260710",
        "--run-id", "cli-smoke",
        "--output-dir", str(output),
        "--models", "mock-alpha", "mock-beta",
        "--repeats", "2",
    ]) == 0
    assert len(captured) == 1
    config = captured[0]
    assert config.run_date == "20260710"
    assert config.run_id == "cli-smoke"
    assert config.output_dir == output
    assert config.models == ("mock-alpha", "mock-beta")
    assert config.repeats == 2
