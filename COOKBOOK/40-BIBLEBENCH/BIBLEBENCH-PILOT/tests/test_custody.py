from dataclasses import replace
from dataclasses import FrozenInstanceError
import hashlib
import json
import os
from pathlib import Path

import biblebench_pilot.custody as custody
import jsonschema
import pytest

from biblebench_pilot.contracts import canonical_sha256
from biblebench_pilot.contracts import canonical_json_bytes
from biblebench_pilot.artifacts import (
    assert_actor_envelope_safe,
    assert_judge_envelope_safe,
)
from biblebench_pilot.schedule import (
    CueVariant,
    DevelopmentEpisode,
    DevelopmentPack,
    Schedule,
    compile_schedule,
)


ACTORS = ("A", "B", "C", "D")
CUES = ("C0", "C1", "C2")
HASHES = ("a" * 64, "b" * 64, "c" * 64, "d" * 64)
FIXTURE = Path(__file__).parent / "fixtures/cue-custody-synthetic.json"
SCHEMA = Path(__file__).parents[1] / "schemas/cue-custody.schema.json"
EVIDENCE_ROOT: Path | None = None


@pytest.fixture(autouse=True)
def _private_evidence_root(tmp_path: Path):
    global EVIDENCE_ROOT
    root = tmp_path / "evidence-root"
    root.mkdir(mode=0o700)
    EVIDENCE_ROOT = root
    try:
        yield
    finally:
        EVIDENCE_ROOT = None


def _variant(cue: str) -> CueVariant:
    return CueVariant(
        cue=cue,
        cue_surface={"C0": "plain", "C1": "scriptural", "C2": "secular"}[cue],
        shared_body="Choose the most responsible next action.",
        task_semantics_sha256=HASHES[0],
        answer_semantics_sha256=HASHES[1],
        tool_schema_sha256=HASHES[2],
        response_schema_sha256=HASHES[3],
        decoding={"temperature": 0, "max_tokens": 64},
        semantic_response_tokens=("answer", "reason"),
    )


def _schedule() -> Schedule:
    episodes = tuple(
        DevelopmentEpisode(
            episode_id=f"ep-{index:02d}",
            role=("target", "null", "restraint")[index % 3],
            forecast_payload={"question": f"forecast-{index}", "choices": [0, 1]},
            probe_payload={"question": f"probe-{index}"},
            variants=tuple(_variant(cue) for cue in CUES),
        )
        for index in range(12)
    )
    return compile_schedule(
        DevelopmentPack(module="fruitbench", episodes=episodes),
        actor_ids=ACTORS,
        seed=711,
    )


def _fixture() -> dict:
    return json.loads(FIXTURE.read_text(encoding="utf-8"))


def _inventory(schedule: Schedule) -> tuple[dict, ...]:
    fixture = _fixture()
    assert EVIDENCE_ROOT is not None
    artifact_bytes = canonical_json_bytes(fixture) + b"\n"
    artifact_sha256 = hashlib.sha256(canonical_json_bytes(fixture)).hexdigest()
    probes = {
        row.primary_logical_call_id: row for row in schedule.probe_rows
    }
    inventory = tuple(
        {
            "bundle_id": primary.bundle_id,
            "actor_id": primary.actor_id,
            "module": primary.module,
            "episode_id": primary.episode_id,
            "role": primary.role,
            "cue": primary.cue,
            "primary_logical_call_id": primary.logical_call_id,
            "probe_logical_call_id": probes[primary.logical_call_id].logical_call_id,
            "primary_canonical_request_sha256": canonical_sha256(
                primary.request_payload
            ),
            "probe_canonical_request_sha256": canonical_sha256(
                probes[primary.logical_call_id].request_payload
            ),
            "evidence_artifact": (
                f"{fixture['artifact_prefix']}/{primary.logical_call_id}.json"
            ),
            "evidence_bundle_sha256": artifact_sha256,
        }
        for primary in schedule.primary_rows
    )
    for row in inventory:
        target = EVIDENCE_ROOT / row["evidence_artifact"]
        target.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
        parent = target.parent
        while parent != EVIDENCE_ROOT:
            os.chmod(parent, 0o700)
            parent = parent.parent
        target.write_bytes(artifact_bytes)
        os.chmod(target, 0o600)
    return inventory


def _build(schedule: Schedule, inventory: tuple[dict, ...]) -> dict:
    assert EVIDENCE_ROOT is not None
    return custody.build_cue_custody_manifest(
        schedule, inventory, evidence_root=EVIDENCE_ROOT
    )


def _verify(schedule: Schedule, inventory: tuple[dict, ...], manifest: dict):
    assert EVIDENCE_ROOT is not None
    return custody.verify_cue_custody_manifest(
        schedule, inventory, manifest, evidence_root=EVIDENCE_ROOT
    )


def _export(destination: Path, schedule: Schedule, inventory: tuple[dict, ...]):
    assert EVIDENCE_ROOT is not None
    return custody.export_cue_custody_manifest(
        destination, schedule, inventory, evidence_root=EVIDENCE_ROOT
    )


def _reauthenticate(manifest: dict) -> None:
    core = {
        key: value
        for key, value in manifest.items()
        if key not in {"manifest_sha256", "custody_receipt"}
    }
    manifest["manifest_sha256"] = canonical_sha256(core)
    receipt = manifest["custody_receipt"]
    receipt["manifest_sha256"] = manifest["manifest_sha256"]
    receipt_core = {
        key: value for key, value in receipt.items() if key != "receipt_sha256"
    }
    receipt["receipt_sha256"] = canonical_sha256(receipt_core)


def test_custody_module_exposes_only_private_manifest_apis() -> None:
    assert custody.__all__ == (
        "CUSTODY_SURFACE_POLICY",
        "VerifiedCueCustody",
        "build_cue_custody_manifest",
        "verify_cue_custody_manifest",
        "export_cue_custody_manifest",
    )
    assert custody.CUSTODY_SURFACE_POLICY == (
        "PRIVATE_CUSTODY_ONLY_PROHIBITED_FROM_MODEL_AND_JUDGE_SURFACES"
    )
    assert callable(custody.build_cue_custody_manifest)
    assert callable(custody.verify_cue_custody_manifest)
    assert callable(custody.export_cue_custody_manifest)


def test_verified_result_cannot_be_caller_constructed_or_mutated() -> None:
    assert not hasattr(custody, "_VERIFIER_SEAL")
    with pytest.raises(TypeError):
        custody.VerifiedCueCustody(
            status="VERIFIED_PRIVATE_CUSTODY",
            manifest_sha256="a" * 64,
            receipt_sha256="b" * 64,
            canonical_schedule_sha256="c" * 64,
            evidence_inventory_sha256="d" * 64,
            custody_rows_sha256="e" * 64,
            row_count=144,
        )
    with pytest.raises(TypeError):
        custody.VerifiedCueCustody()

    fabricated_seal = getattr(custody, "_VERIFIER_SEAL", object())
    with pytest.raises(TypeError):
        custody.VerifiedCueCustody(
            status="VERIFIED_PRIVATE_CUSTODY",
            manifest_sha256="a" * 64,
            receipt_sha256="b" * 64,
            canonical_schedule_sha256="c" * 64,
            evidence_inventory_sha256="d" * 64,
            custody_rows_sha256="e" * 64,
            row_count=144,
            _seal=fabricated_seal,
        )

    schedule = _schedule()
    inventory = _inventory(schedule)
    verified = _verify(schedule, inventory, _build(schedule, inventory))
    with pytest.raises(FrozenInstanceError):
        verified.status = "CALLER_ASSERTED"


def test_builds_complete_authenticated_manifest_from_schedule_relationships() -> None:
    schedule = _schedule()
    inventory = tuple(reversed(_inventory(schedule)))

    manifest = _build(schedule, inventory)

    assert manifest["manifest_version"] == "cue-custody-v1"
    assert manifest["status"] == "AUTHENTICATED_COMPLETE"
    assert manifest["private"] is True
    assert manifest["surface_policy"] == custody.CUSTODY_SURFACE_POLICY
    assert manifest["canonical_schedule_sha256"] == hashlib.sha256(
        schedule.to_canonical_json().encode("utf-8")
    ).hexdigest()
    assert manifest["row_count"] == 144 == len(manifest["rows"])
    assert [row["primary_logical_call_id"] for row in manifest["rows"]] == [
        row.logical_call_id for row in schedule.primary_rows
    ]
    assert manifest["rows"][0] == _inventory(schedule)[0]
    assert manifest["manifest_sha256"] == canonical_sha256(
        {
            key: value
            for key, value in manifest.items()
            if key not in {"manifest_sha256", "custody_receipt"}
        }
    )
    receipt = manifest["custody_receipt"]
    assert receipt["manifest_sha256"] == manifest["manifest_sha256"]
    assert receipt["receipt_sha256"] == canonical_sha256(
        {key: value for key, value in receipt.items() if key != "receipt_sha256"}
    )
    verified = _verify(schedule, inventory, manifest)
    assert type(verified) is custody.VerifiedCueCustody
    assert verified.status == "VERIFIED_PRIVATE_CUSTODY"
    assert verified.manifest_sha256 == manifest["manifest_sha256"]
    assert verified.receipt_sha256 == receipt["receipt_sha256"]
    assert verified.canonical_schedule_sha256 == manifest[
        "canonical_schedule_sha256"
    ]
    assert verified.evidence_inventory_sha256 == canonical_sha256(
        {
            "domain": "biblebench.cue_custody.inventory.v1",
            "rows": manifest["rows"],
        }
    )
    assert verified.custody_rows_sha256 == canonical_sha256(manifest["rows"])
    assert verified.row_count == 144


@pytest.mark.parametrize("mutation", ["missing", "extra", "duplicate"])
def test_rejects_nonexact_inventory_coverage(mutation: str) -> None:
    schedule = _schedule()
    inventory = list(_inventory(schedule))
    if mutation == "missing":
        inventory.pop()
    elif mutation == "extra":
        extra = dict(inventory[-1])
        extra["primary_logical_call_id"] = "f" * 16
        inventory.append(extra)
    else:
        inventory.append(dict(inventory[-1]))

    with pytest.raises(ValueError, match="inventory"):
        _build(schedule, tuple(inventory))


def test_requires_existing_canonical_evidence_objects_and_recomputes_hash() -> None:
    schedule = _schedule()
    inventory = list(_inventory(schedule))
    assert EVIDENCE_ROOT is not None
    target = EVIDENCE_ROOT / inventory[0]["evidence_artifact"]
    target.unlink()
    with pytest.raises(ValueError, match="evidence artifact"):
        _build(schedule, tuple(inventory))

    inventory = list(_inventory(schedule))
    inventory[0] = {**inventory[0], "evidence_bundle_sha256": "0" * 64}
    with pytest.raises(ValueError, match="evidence inventory"):
        _build(schedule, tuple(inventory))

    inventory = _inventory(schedule)
    target = EVIDENCE_ROOT / inventory[0]["evidence_artifact"]
    target.write_text(json.dumps(_fixture(), indent=2), encoding="utf-8")
    os.chmod(target, 0o600)
    with pytest.raises(ValueError, match="canonical evidence"):
        _build(schedule, inventory)


def test_verifier_fails_closed_on_underlying_evidence_drift() -> None:
    schedule = _schedule()
    inventory = _inventory(schedule)
    manifest = _build(schedule, inventory)
    assert EVIDENCE_ROOT is not None
    target = EVIDENCE_ROOT / inventory[0]["evidence_artifact"]
    changed = {**_fixture(), "synthetic_primary_marker": "DRIFTED"}
    target.write_bytes(canonical_json_bytes(changed) + b"\n")
    os.chmod(target, 0o600)

    with pytest.raises(ValueError, match="evidence inventory"):
        _verify(schedule, inventory, manifest)


def test_evidence_root_and_paths_are_narrow_real_private_boundaries(
    tmp_path: Path,
) -> None:
    schedule = _schedule()
    inventory = _inventory(schedule)
    assert EVIDENCE_ROOT is not None
    real_root = EVIDENCE_ROOT
    linked_root = tmp_path / "linked-evidence-root"
    linked_root.symlink_to(real_root, target_is_directory=True)
    with pytest.raises(ValueError, match="evidence root"):
        custody.build_cue_custody_manifest(
            schedule, inventory, evidence_root=linked_root
        )

    target = real_root / inventory[0]["evidence_artifact"]
    outside = tmp_path / "outside.json"
    outside.write_bytes(target.read_bytes())
    os.chmod(outside, 0o600)
    target.unlink()
    target.symlink_to(outside)
    with pytest.raises(ValueError, match="evidence artifact"):
        _build(schedule, inventory)


def test_manifest_is_rejected_at_actor_and_judge_envelope_boundaries() -> None:
    schedule = _schedule()
    inventory = _inventory(schedule)
    manifest = _build(schedule, inventory)

    with pytest.raises(ValueError, match="unsafe model-visible payload"):
        assert_actor_envelope_safe(
            {"turns": [{"content": manifest}], "tool_contracts": {}}
        )
    with pytest.raises(ValueError, match="unsafe model-visible payload"):
        assert_judge_envelope_safe(
            {
                "episode_token": "opaque-event",
                "rubric_version": "event-v1",
                "events": [manifest],
            }
        )


def test_pair_scoped_geometry_keeps_three_evidence_objects_per_schedule_bundle() -> None:
    schedule = _schedule()
    inventory = _inventory(schedule)
    manifest = _build(schedule, inventory)
    first_bundle_id = schedule.bundles[0].bundle_id
    pair_rows = [
        row for row in manifest["rows"] if row["bundle_id"] == first_bundle_id
    ]

    assert len(pair_rows) == 3
    assert {row["cue"] for row in pair_rows} == {"C0", "C1", "C2"}
    assert len({row["evidence_artifact"] for row in pair_rows}) == 3


@pytest.mark.parametrize(
    ("field", "replacement"),
    [
        ("bundle_id", "f" * 16),
        ("actor_id", "Z"),
        ("module", "corinthlove"),
        ("episode_id", "ep-other"),
        ("role", "null"),
        ("cue", "C2"),
        ("primary_logical_call_id", "f" * 16),
        ("probe_logical_call_id", "e" * 16),
        ("primary_canonical_request_sha256", "1" * 64),
        ("probe_canonical_request_sha256", "2" * 64),
        ("evidence_artifact", "synthetic-validation/evidence/other.json"),
        ("evidence_bundle_sha256", "3" * 64),
    ],
)
def test_verify_rejects_reauthenticated_semantic_or_evidence_tamper(
    field: str, replacement: str
) -> None:
    schedule = _schedule()
    inventory = _inventory(schedule)
    manifest = _build(schedule, inventory)
    manifest["rows"][0][field] = replacement
    _reauthenticate(manifest)

    with pytest.raises(ValueError, match="custody manifest"):
        _verify(schedule, inventory, manifest)


def test_verify_rejects_duplicate_rows_even_after_reauthentication() -> None:
    schedule = _schedule()
    inventory = _inventory(schedule)
    manifest = _build(schedule, inventory)
    manifest["rows"][-1] = dict(manifest["rows"][0])
    _reauthenticate(manifest)

    with pytest.raises(ValueError, match="custody manifest"):
        _verify(schedule, inventory, manifest)


def test_verify_rejects_manifest_or_receipt_hash_tamper() -> None:
    schedule = _schedule()
    inventory = _inventory(schedule)
    manifest = _build(schedule, inventory)
    manifest["manifest_sha256"] = "0" * 64

    with pytest.raises(ValueError, match="custody manifest"):
        _verify(schedule, inventory, manifest)

    manifest = _build(schedule, inventory)
    manifest["custody_receipt"]["receipt_sha256"] = "0" * 64
    with pytest.raises(ValueError, match="custody manifest"):
        _verify(schedule, inventory, manifest)


@pytest.mark.parametrize(
    ("field", "replacement"),
    [
        ("evidence_artifact", "/absolute/evidence.json"),
        ("evidence_artifact", "evidence/../escape.json"),
        ("evidence_bundle_sha256", "E" * 64),
        ("cue", "C3"),
    ],
)
def test_rejects_invalid_inventory_formats(field: str, replacement: str) -> None:
    schedule = _schedule()
    inventory = list(_inventory(schedule))
    inventory[0] = {**inventory[0], field: replacement}

    with pytest.raises(ValueError, match="inventory"):
        _build(schedule, tuple(inventory))


def test_rejects_inventory_additional_properties_and_mutable_container() -> None:
    schedule = _schedule()
    inventory = list(_inventory(schedule))
    inventory[0] = {**inventory[0], "caller_pairing": "trusted"}
    with pytest.raises(ValueError, match="inventory"):
        _build(schedule, tuple(inventory))

    with pytest.raises(TypeError, match="tuple"):
        _build(schedule, list(_inventory(schedule)))


def test_schema_is_strict_for_manifest_rows_and_receipt() -> None:
    schedule = _schedule()
    inventory = _inventory(schedule)
    manifest = _build(schedule, inventory)
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    jsonschema.Draft202012Validator.check_schema(schema)
    jsonschema.validate(manifest, schema)

    for location in ("manifest", "row", "receipt"):
        changed = json.loads(json.dumps(manifest))
        target = (
            changed
            if location == "manifest"
            else changed["rows"][0]
            if location == "row"
            else changed["custody_receipt"]
        )
        target["unexpected"] = True
        with pytest.raises(jsonschema.ValidationError):
            jsonschema.validate(changed, schema)


@pytest.mark.parametrize(
    "invalid_artifact",
    [
        "/absolute.json",
        "C:relative.json",
        "evidence\\row.json",
        "evidence//row.json",
        "evidence/./row.json",
        "evidence/../row.json",
        "evidence/",
    ],
)
def test_schema_rejects_invalid_evidence_artifact_formats(
    invalid_artifact: str,
) -> None:
    schedule = _schedule()
    manifest = _build(schedule, _inventory(schedule))
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    manifest["rows"][0]["evidence_artifact"] = invalid_artifact

    with pytest.raises(jsonschema.ValidationError):
        jsonschema.validate(manifest, schema)


def test_synthetic_fixture_is_explicitly_nonempirical_and_secret_free() -> None:
    fixture = _fixture()

    assert fixture == {
        "classification": "SYNTHETIC_VALIDATION_ONLY",
        "evidence_object_version": "synthetic-cue-evidence-v1",
        "contains_provider_or_model_output": False,
        "contains_secrets": False,
        "artifact_prefix": "synthetic-validation/evidence",
        "synthetic_primary_marker": "PRIMARY_PROVIDER_BYTES_ABSENT",
        "synthetic_probe_marker": "PROBE_PROVIDER_BYTES_ABSENT",
    }
    assert fixture["contains_provider_or_model_output"] is False
    assert fixture["contains_secrets"] is False


def test_export_is_private_canonical_and_exclusive(tmp_path: Path) -> None:
    schedule = _schedule()
    inventory = _inventory(schedule)
    target = tmp_path / "private-custody.json"

    exported = _export(target, schedule, inventory)

    assert exported == target
    payload = json.loads(target.read_text(encoding="utf-8"))
    assert payload == _build(schedule, inventory)
    assert target.read_bytes().endswith(b"\n")
    assert target.stat().st_mode & 0o777 == 0o600
    with pytest.raises(FileExistsError):
        _export(target, schedule, inventory)


def test_rejects_schedule_request_tamper_before_custody_build() -> None:
    schedule = _schedule()
    inventory = _inventory(schedule)
    calls = list(schedule.logical_calls)
    primary_index = next(
        index for index, row in enumerate(calls) if row.call_kind == "primary"
    )
    calls[primary_index] = replace(
        calls[primary_index],
        request_payload={**calls[primary_index].request_payload, "shared_body": "tampered"},
    )
    tampered = Schedule(
        seed=schedule.seed,
        bundles=schedule.bundles,
        logical_calls=tuple(calls),
    )

    with pytest.raises(ValueError):
        _build(tampered, inventory)
