from dataclasses import FrozenInstanceError, replace
import json
from pathlib import Path

from jsonschema import Draft202012Validator, ValidationError
import pytest
import yaml

from biblebench_pilot.registry import (
    CoreRecord,
    load_core_manifest,
    validate_source_paths,
)


FIXTURES = Path(__file__).parent / "fixtures"
SCHEMAS = Path(__file__).parents[1] / "schemas"
CORE_FIELDS = {
    "core_id",
    "module",
    "source_paths",
    "passage_anchors",
    "construct",
    "explicit_non_claims",
    "evidence_type",
    "behavioral_attribution",
    "eligible_modes",
    "eligible_transforms",
    "deficient_pole",
    "counterfeit_pole",
    "shared_red_lines",
    "module_red_lines",
}
EPISODE_FIELDS = {
    "episode_id",
    "core_id",
    "split",
    "stratum",
    "mode",
    "transform_ids",
    "capability_twin_id",
    "actor_payload_sha256",
}
ARRAY_FIELDS = {
    "source_paths",
    "passage_anchors",
    "explicit_non_claims",
    "eligible_modes",
    "eligible_transforms",
    "shared_red_lines",
    "module_red_lines",
}


def _valid_manifest() -> dict:
    return yaml.safe_load((FIXTURES / "core-valid.yaml").read_text(encoding="utf-8"))


def _write_manifest(tmp_path: Path, manifest: object) -> Path:
    path = tmp_path / "manifest.yaml"
    path.write_text(yaml.safe_dump(manifest, sort_keys=False), encoding="utf-8")
    return path


def _record_with_source(source_path: str) -> CoreRecord:
    record = load_core_manifest(FIXTURES / "core-valid.yaml")[0]
    return replace(record, source_paths=(source_path,))


def _assert_source_path_error(
    record: CoreRecord,
    workspace_root: Path,
    category: str,
) -> None:
    with pytest.raises(ValueError) as exc_info:
        validate_source_paths((record,), workspace_root)
    assert f"core {record.core_id} source path {record.source_paths[0]!r}" in str(
        exc_info.value
    )
    assert category in str(exc_info.value)


def test_load_core_manifest_accepts_complete_record():
    records = load_core_manifest(FIXTURES / "core-valid.yaml")
    assert [record.core_id for record in records] == ["F09"]
    assert records[0].evidence_type == "action"


def test_load_core_manifest_rejects_missing_non_claims():
    with pytest.raises(ValueError, match="explicit_non_claims"):
        load_core_manifest(FIXTURES / "core-invalid.yaml")


def test_load_core_manifest_rejects_duplicate_core_id(tmp_path: Path):
    manifest = _valid_manifest()
    manifest["cores"].append(dict(manifest["cores"][0]))

    with pytest.raises(ValueError, match="duplicate core_id F09"):
        load_core_manifest(_write_manifest(tmp_path, manifest))


@pytest.mark.parametrize(
    "manifest",
    [
        {"manifest_version": "1.0", "cores": [], "private": True},
        {"cores": []},
        {"manifest_version": "1.0"},
        [],
    ],
)
def test_load_core_manifest_rejects_wrong_top_level_fields(
    tmp_path: Path,
    manifest: object,
):
    with pytest.raises(ValueError, match="top-level"):
        load_core_manifest(_write_manifest(tmp_path, manifest))


def test_load_core_manifest_rejects_empty_cores(tmp_path: Path):
    manifest = {"manifest_version": "1.0", "cores": []}

    with pytest.raises(ValueError, match="cores must be a nonempty list"):
        load_core_manifest(_write_manifest(tmp_path, manifest))


@pytest.mark.parametrize("manifest_version", ["", 1, None])
def test_load_core_manifest_rejects_invalid_manifest_version(
    tmp_path: Path,
    manifest_version: object,
):
    manifest = _valid_manifest()
    manifest["manifest_version"] = manifest_version

    with pytest.raises(ValueError, match="manifest_version must be a nonempty string"):
        load_core_manifest(_write_manifest(tmp_path, manifest))


def test_load_core_manifest_rejects_unknown_row_field(tmp_path: Path):
    manifest = _valid_manifest()
    manifest["cores"][0]["private_note"] = "must not cross the boundary"

    with pytest.raises(ValueError, match="private_note"):
        load_core_manifest(_write_manifest(tmp_path, manifest))


def test_load_core_manifest_rejects_invalid_core_id(tmp_path: Path):
    manifest = _valid_manifest()
    manifest["cores"][0]["core_id"] = "F13"

    with pytest.raises(ValueError, match="core_id"):
        load_core_manifest(_write_manifest(tmp_path, manifest))


def test_load_core_manifest_converts_every_array_to_tuple():
    record = load_core_manifest(FIXTURES / "core-valid.yaml")[0]

    for field in ARRAY_FIELDS:
        assert isinstance(getattr(record, field), tuple), field


def test_core_record_is_frozen():
    record = load_core_manifest(FIXTURES / "core-valid.yaml")[0]

    with pytest.raises(FrozenInstanceError):
        record.core_id = "F08"


def test_core_schema_is_valid_and_declares_closed_required_boundary():
    schema = json.loads((SCHEMAS / "core.schema.json").read_text(encoding="utf-8"))

    Draft202012Validator.check_schema(schema)
    assert schema["additionalProperties"] is False
    assert set(schema["required"]) == CORE_FIELDS
    assert set(schema["properties"]) == CORE_FIELDS


def test_episode_schema_is_valid_and_enforces_private_field_boundary():
    schema = json.loads((SCHEMAS / "episode.schema.json").read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema)
    record = {
        "episode_id": "episode-001",
        "core_id": "F09",
        "split": "public_calibration",
        "stratum": "common_life",
        "mode": "action",
        "transform_ids": ["surface-paraphrase"],
        "capability_twin_id": None,
        "actor_payload_sha256": "a" * 64,
    }

    Draft202012Validator.check_schema(schema)
    validator.validate(record)
    with pytest.raises(ValidationError, match="private_note"):
        validator.validate({**record, "private_note": "hidden"})
    assert schema["additionalProperties"] is False
    assert set(schema["required"]) == EPISODE_FIELDS
    assert set(schema["properties"]) == EPISODE_FIELDS


def test_validate_source_paths_accepts_existing_markdown_file(tmp_path: Path):
    workspace_root = tmp_path / "workspace"
    source = workspace_root / "sources" / "F09.md"
    source.parent.mkdir(parents=True)
    source.write_text("# F09\n", encoding="utf-8")

    assert validate_source_paths(
        (_record_with_source("sources/F09.md"),), workspace_root
    ) is None


def test_validate_source_paths_rejects_absolute_path(tmp_path: Path):
    workspace_root = tmp_path / "workspace"
    workspace_root.mkdir()
    record = _record_with_source(str(tmp_path / "absolute.md"))

    _assert_source_path_error(record, workspace_root, "must be relative")


def test_validate_source_paths_rejects_traversal(tmp_path: Path):
    workspace_root = tmp_path / "workspace"
    workspace_root.mkdir()
    record = _record_with_source("../../secret.md")

    _assert_source_path_error(record, workspace_root, "escapes workspace root")


def test_validate_source_paths_rejects_lexical_traversal_inside_root(tmp_path: Path):
    workspace_root = tmp_path / "workspace"
    workspace_root.mkdir()
    (workspace_root / "ok.md").write_text("# Safe target\n", encoding="utf-8")
    (workspace_root / "sub").mkdir()
    record = _record_with_source("sub/../ok.md")

    _assert_source_path_error(record, workspace_root, "traversal")


def test_validate_source_paths_rejects_missing_path(tmp_path: Path):
    workspace_root = tmp_path / "workspace"
    workspace_root.mkdir()
    record = _record_with_source("missing.md")

    _assert_source_path_error(record, workspace_root, "does not exist")


def test_validate_source_paths_rejects_wrong_extension(tmp_path: Path):
    workspace_root = tmp_path / "workspace"
    workspace_root.mkdir()
    record = _record_with_source("notes.txt")

    _assert_source_path_error(record, workspace_root, "must end in .md")


def test_validate_source_paths_rejects_directory(tmp_path: Path):
    workspace_root = tmp_path / "workspace"
    directory = workspace_root / "directory.md"
    directory.mkdir(parents=True)
    record = _record_with_source("directory.md")

    _assert_source_path_error(record, workspace_root, "is not a regular file")


def test_validate_source_paths_rejects_outside_resolving_symlink(tmp_path: Path):
    workspace_root = tmp_path / "workspace"
    workspace_root.mkdir()
    outside = tmp_path / "outside.md"
    outside.write_text("outside\n", encoding="utf-8")
    symlink = workspace_root / "link.md"
    try:
        symlink.symlink_to(outside)
    except (NotImplementedError, OSError) as error:
        pytest.skip(f"platform cannot create symlinks: {error}")
    record = _record_with_source("link.md")

    _assert_source_path_error(record, workspace_root, "escapes workspace root")


@pytest.mark.parametrize("kind", ["missing", "file"])
def test_validate_source_paths_rejects_invalid_workspace_root(
    tmp_path: Path,
    kind: str,
):
    workspace_root = tmp_path / "workspace"
    if kind == "file":
        workspace_root.write_text("not a directory\n", encoding="utf-8")

    with pytest.raises(ValueError, match="workspace_root must be an existing directory"):
        validate_source_paths((_record_with_source("F09.md"),), workspace_root)
