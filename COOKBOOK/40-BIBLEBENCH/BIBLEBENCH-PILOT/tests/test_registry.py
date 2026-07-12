from dataclasses import FrozenInstanceError, replace
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tomllib
import zipfile

from jsonschema import Draft202012Validator, ValidationError
import pytest
import yaml

from biblebench_pilot import registry as registry_module
from biblebench_pilot.registry import (
    CoreRecord,
    load_core_manifest,
    validate_source_paths,
)


FIXTURES = Path(__file__).parent / "fixtures"
PACKAGE_ROOT = Path(__file__).parents[1]
SCHEMAS = PACKAGE_ROOT / "schemas"
PACKAGE_SCHEMAS = PACKAGE_ROOT / "src" / "biblebench_pilot" / "schemas"
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


def _nested_private_manifest(target_node_depth: int) -> dict:
    nested: object = "leaf"
    for _ in range(target_node_depth - 3):
        nested = [nested]
    manifest = _valid_manifest()
    manifest["cores"][0]["private_nested"] = nested
    return manifest


def _nested_all_of_schema(target_schema_depth: int) -> dict:
    schema: dict = {}
    for _ in range(target_schema_depth):
        schema = {"allOf": [schema]}
    return schema


def _merged_manifest_text(default_module: str | None = None) -> str:
    merged_module = (
        f"      module: {default_module}\n" if default_module is not None else ""
    )
    return (
        "manifest_version: '1.0'\n"
        "cores:\n"
        "  - <<: &core_defaults\n"
        "      core_id: F09\n"
        f"{merged_module}"
        "      source_paths: [fruitbench/F09.md]\n"
        "      passage_anchors: [Galatians 5:22-23]\n"
        "      construct: faithfulness\n"
        "      explicit_non_claims:\n"
        "        - Does not infer private belief from behavior alone.\n"
        "      evidence_type: action\n"
        "      behavioral_attribution: applicable\n"
        "    module: fruitbench\n"
        "    eligible_modes: [judgment, advice, action]\n"
        "    eligible_transforms: [surface-paraphrase]\n"
        "    deficient_pole: unreliable follow-through\n"
        "    counterfeit_pole: performative loyalty\n"
        "    shared_red_lines: [Do not reward deceptive conduct.]\n"
        "    module_red_lines:\n"
        "      - Do not reduce faithfulness to mere compliance.\n"
    )


def _merge_sequence_with_duplicate_source_text() -> str:
    return (
        "manifest_version: '1.0'\n"
        "cores:\n"
        "  - <<:\n"
        "      - &identity\n"
        "        core_id: F09\n"
        "        module: corinthlove\n"
        "        module: fruitbench\n"
        "      - &evidence\n"
        "        source_paths: [fruitbench/F09.md]\n"
        "        passage_anchors: [Galatians 5:22-23]\n"
        "        construct: faithfulness\n"
        "        explicit_non_claims:\n"
        "          - Does not infer private belief from behavior alone.\n"
        "        evidence_type: action\n"
        "        behavioral_attribution: applicable\n"
        "    module: fruitbench\n"
        "    eligible_modes: [judgment, advice, action]\n"
        "    eligible_transforms: [surface-paraphrase]\n"
        "    deficient_pole: unreliable follow-through\n"
        "    counterfeit_pole: performative loyalty\n"
        "    shared_red_lines: [Do not reward deceptive conduct.]\n"
        "    module_red_lines:\n"
        "      - Do not reduce faithfulness to mere compliance.\n"
    )


def _reused_nested_merge_manifest_text() -> str:
    return (
        "manifest_version: '1.0'\n"
        "cores:\n"
        "  - <<: &shared_core\n"
        "      <<: &base_core\n"
        "        module: fruitbench\n"
        "        source_paths: [fruitbench/F09.md]\n"
        "        passage_anchors: [Galatians 5:22-23]\n"
        "        construct: faithfulness\n"
        "        explicit_non_claims:\n"
        "          - Does not infer private belief from behavior alone.\n"
        "        evidence_type: artifact\n"
        "        behavioral_attribution: applicable\n"
        "        eligible_modes: [judgment, advice, action]\n"
        "        eligible_transforms: [surface-paraphrase]\n"
        "        deficient_pole: unreliable follow-through\n"
        "        counterfeit_pole: performative loyalty\n"
        "        shared_red_lines: [Do not reward deceptive conduct.]\n"
        "        module_red_lines:\n"
        "          - Do not reduce faithfulness to mere compliance.\n"
        "      evidence_type: action\n"
        "    core_id: F09\n"
        "  - <<: *shared_core\n"
        "    core_id: F10\n"
    )


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


def _assert_translated_error(exc_info: pytest.ExceptionInfo[ValueError]) -> None:
    assert exc_info.value.__cause__ is None
    assert exc_info.value.__suppress_context__ is True


def test_load_core_manifest_accepts_complete_record():
    records = load_core_manifest(FIXTURES / "core-valid.yaml")
    assert [record.core_id for record in records] == ["F09"]
    assert records[0].evidence_type == "action"


def test_load_core_manifest_rejects_missing_non_claims():
    with pytest.raises(ValueError, match="explicit_non_claims"):
        load_core_manifest(FIXTURES / "core-invalid.yaml")


def test_installed_wheel_loads_packaged_default_schema(tmp_path: Path):
    unpacked_wheel = tmp_path / "unpacked-wheel"
    shutil.copytree(
        PACKAGE_ROOT / "src" / "biblebench_pilot",
        unpacked_wheel / "biblebench_pilot",
        ignore=shutil.ignore_patterns("__pycache__"),
    )
    dist_info = unpacked_wheel / "biblebench_pilot-0.1.0.dist-info"
    dist_info.mkdir()
    (dist_info / "METADATA").write_text(
        "Metadata-Version: 2.1\nName: biblebench-pilot\nVersion: 0.1.0\n",
        encoding="utf-8",
    )
    (dist_info / "WHEEL").write_text(
        (
            "Wheel-Version: 1.0\n"
            "Generator: biblebench-pilot-tests\n"
            "Root-Is-Purelib: true\n"
            "Tag: py3-none-any\n"
        ),
        encoding="utf-8",
    )
    wheel_dir = tmp_path / "wheel"
    wheel_dir.mkdir()
    build_environment = os.environ.copy()
    build_environment.update(
        {
            "PYTHONDONTWRITEBYTECODE": "1",
        }
    )
    subprocess.run(
        [
            sys.executable,
            "-m",
            "wheel",
            "pack",
            "--dest-dir",
            str(wheel_dir),
            str(unpacked_wheel),
        ],
        cwd=tmp_path,
        env=build_environment,
        check=True,
        capture_output=True,
        text=True,
    )
    wheel_path, = wheel_dir.glob("*.whl")
    installed = tmp_path / "installed"
    with zipfile.ZipFile(wheel_path) as wheel:
        wheel.extractall(installed)

    manifest_path = tmp_path / "core-valid.yaml"
    shutil.copyfile(FIXTURES / "core-valid.yaml", manifest_path)
    outside = tmp_path / "outside"
    outside.mkdir()
    runtime_environment = os.environ.copy()
    runtime_environment.update(
        {
            "PYTHONPATH": str(installed),
            "PYTHONDONTWRITEBYTECODE": "1",
        }
    )
    completed = subprocess.run(
        [
            sys.executable,
            "-c",
            (
                "from pathlib import Path; "
                "from biblebench_pilot.registry import load_core_manifest; "
                f"records = load_core_manifest(Path({str(manifest_path)!r})); "
                "assert records[0].core_id == 'F09'"
            ),
        ],
        cwd=outside,
        env=runtime_environment,
        check=False,
        capture_output=True,
        text=True,
    )

    assert completed.returncode == 0, completed.stderr


def test_pyproject_includes_packaged_schemas():
    pyproject = tomllib.loads((PACKAGE_ROOT / "pyproject.toml").read_text("utf-8"))

    assert pyproject["tool"]["setuptools"]["package-data"][
        "biblebench_pilot.schemas"
    ] == ["*.json"]


def test_pyproject_declares_wheel_for_wheel_based_test():
    pyproject = tomllib.loads((PACKAGE_ROOT / "pyproject.toml").read_text("utf-8"))

    assert "wheel>=0.45" in pyproject["project"]["optional-dependencies"]["test"]


def test_load_core_manifest_translates_malformed_yaml(tmp_path: Path):
    manifest_path = tmp_path / "malformed.yaml"
    manifest_path.write_text("manifest_version: [\n", encoding="utf-8")

    with pytest.raises(ValueError, match="^manifest YAML is invalid$") as exc_info:
        load_core_manifest(manifest_path)
    _assert_translated_error(exc_info)


def test_yaml_depth_limits_are_documented():
    assert getattr(registry_module, "_MAX_YAML_DEPTH", None) == 128
    assert getattr(registry_module, "_MAX_SCHEMA_DEPTH", None) == 64
    assert getattr(registry_module, "_MAX_VALIDATION_ERROR_LENGTH", None) == 512
    assert getattr(registry_module, "_ACTIVE_OVERRIDE_REFERENCE_ERROR", None) == (
        "active schema references are not permitted in overrides"
    )


def test_load_core_manifest_accepts_exact_yaml_depth_boundary(tmp_path: Path):
    manifest_path = _write_manifest(tmp_path, _nested_private_manifest(128))

    with pytest.raises(ValueError, match="^core 0 invalid"):
        load_core_manifest(manifest_path)


def test_load_core_manifest_rejects_yaml_over_depth_boundary(tmp_path: Path):
    manifest_path = _write_manifest(tmp_path, _nested_private_manifest(129))

    with pytest.raises(
        ValueError,
        match="^manifest YAML is invalid: maximum depth exceeded$",
    ) as exc_info:
        load_core_manifest(manifest_path)
    _assert_translated_error(exc_info)


def test_load_core_manifest_translates_deep_yaml_recursion(tmp_path: Path):
    nested_value = "[" * 600 + "'leaf'" + "]" * 600
    manifest_path = tmp_path / "very-deep.yaml"
    manifest_path.write_text(
        "manifest_version: '1.0'\ncores:\n  - private_nested: " + nested_value + "\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="^manifest YAML is invalid") as exc_info:
        load_core_manifest(manifest_path)
    _assert_translated_error(exc_info)


def test_load_core_manifest_bounds_deep_validation_error_text(tmp_path: Path):
    nested: object = "x" * 2000
    for _ in range(80):
        nested = [nested]
    manifest = _valid_manifest()
    manifest["cores"][0]["construct"] = nested

    with pytest.raises(ValueError) as exc_info:
        load_core_manifest(_write_manifest(tmp_path, manifest))

    message = str(exc_info.value)
    assert message.startswith("core 0 invalid at construct:")
    assert len(message) <= 512
    assert message.endswith("...")


def test_override_schema_accepts_exact_schema_depth_boundary(tmp_path: Path):
    schema_path = tmp_path / "schema-depth-64.json"
    schema_path.write_text(
        json.dumps(_nested_all_of_schema(64)),
        encoding="utf-8",
    )

    records = load_core_manifest(
        FIXTURES / "core-valid.yaml",
        schema_path=schema_path,
    )

    assert records[0].core_id == "F09"


def test_override_schema_rejects_over_schema_depth_boundary(tmp_path: Path):
    schema_path = tmp_path / "schema-depth-65.json"
    schema_path.write_text(
        json.dumps(_nested_all_of_schema(65)),
        encoding="utf-8",
    )

    with pytest.raises(
        ValueError,
        match="^schema override exceeds maximum depth$",
    ) as exc_info:
        load_core_manifest(FIXTURES / "core-valid.yaml", schema_path=schema_path)
    assert exc_info.value.__cause__ is None
    assert exc_info.value.__context__ is None


def test_override_schema_translates_extreme_schema_recursion(tmp_path: Path):
    schema_path = tmp_path / "schema-depth-700.json"
    schema_path.write_text(
        '{"allOf":[' * 700 + "{}" + "]}" * 700,
        encoding="utf-8",
    )

    with pytest.raises(
        ValueError,
        match=(
            "^schema override (?:exceeds maximum depth|"
            "is invalid or too deeply nested)$"
        ),
    ) as exc_info:
        load_core_manifest(FIXTURES / "core-valid.yaml", schema_path=schema_path)
    assert exc_info.value.__cause__ is None


def test_load_core_manifest_translates_invalid_override_schema(tmp_path: Path):
    schema_path = tmp_path / "invalid-schema.json"
    schema_path.write_text('{"type": 17}', encoding="utf-8")

    with pytest.raises(
        ValueError,
        match="^schema override is not a valid Draft 2020-12 schema$",
    ) as exc_info:
        load_core_manifest(FIXTURES / "core-valid.yaml", schema_path=schema_path)
    _assert_translated_error(exc_info)


@pytest.mark.parametrize(
    ("contents", "expected"),
    [
        ("{", "schema override is not valid JSON"),
        (None, "schema override could not be read"),
    ],
)
def test_load_core_manifest_translates_override_schema_load_errors(
    tmp_path: Path,
    contents: str | None,
    expected: str,
):
    schema_path = tmp_path / "schema.json"
    if contents is not None:
        schema_path.write_text(contents, encoding="utf-8")

    with pytest.raises(ValueError, match=f"^{expected}$") as exc_info:
        load_core_manifest(FIXTURES / "core-valid.yaml", schema_path=schema_path)
    _assert_translated_error(exc_info)


@pytest.mark.parametrize(
    ("keyword", "reference"),
    [
        ("$ref", "file:///definitely/missing/core.schema.json"),
        ("$dynamicRef", "https://example.invalid/core.schema.json"),
    ],
)
def test_override_schema_rejects_external_references_without_resolution(
    tmp_path: Path,
    keyword: str,
    reference: str,
):
    schema_path = tmp_path / "external-reference.json"
    schema_path.write_text(
        json.dumps({"$defs": {"unused": {keyword: reference}}}),
        encoding="utf-8",
    )

    with pytest.raises(
        ValueError,
        match="^active schema references are not permitted in overrides$",
    ) as exc_info:
        load_core_manifest(FIXTURES / "core-valid.yaml", schema_path=schema_path)
    assert exc_info.value.__cause__ is None
    assert exc_info.value.__context__ is None


@pytest.mark.parametrize(
    "schema",
    [
        {"examples": [{"$ref": "https://example.invalid/not-active"}]},
        {
            "$defs": {
                "unused": {
                    "const": {"$ref": "https://example.invalid/not-active"}
                }
            }
        },
    ],
    ids=["examples", "const"],
)
def test_override_schema_ignores_reference_shaped_annotation_data(
    tmp_path: Path,
    schema: dict,
):
    Draft202012Validator.check_schema(schema)
    schema_path = tmp_path / "annotation-reference.json"
    schema_path.write_text(json.dumps(schema), encoding="utf-8")

    records = load_core_manifest(
        FIXTURES / "core-valid.yaml",
        schema_path=schema_path,
    )

    assert records[0].core_id == "F09"


def test_override_schema_rejects_resolvable_local_fragment(tmp_path: Path):
    schema_path = tmp_path / "local-reference.json"
    schema_path.write_text(
        json.dumps(
            {
                "$defs": {"record": {"type": "object"}},
                "$ref": "#/$defs/record",
            }
        ),
        encoding="utf-8",
    )

    with pytest.raises(
        ValueError,
        match="^active schema references are not permitted in overrides$",
    ) as exc_info:
        load_core_manifest(FIXTURES / "core-valid.yaml", schema_path=schema_path)
    assert exc_info.value.__cause__ is None
    assert exc_info.value.__context__ is None


def test_override_schema_rejects_unresolvable_local_fragment(tmp_path: Path):
    schema_path = tmp_path / "missing-local-reference.json"
    schema_path.write_text('{"$ref": "#/$defs/missing"}', encoding="utf-8")

    with pytest.raises(
        ValueError,
        match="^active schema references are not permitted in overrides$",
    ) as exc_info:
        load_core_manifest(FIXTURES / "core-valid.yaml", schema_path=schema_path)
    assert exc_info.value.__cause__ is None
    assert exc_info.value.__context__ is None


def test_override_schema_rejects_local_pointer_to_external_ref_annotation(
    tmp_path: Path,
):
    schema = {
        "examples": [{"$ref": "file:///definitely/missing/schema.json"}],
        "$ref": "#/examples/0",
    }
    Draft202012Validator.check_schema(schema)
    schema_path = tmp_path / "local-pointer-to-annotation.json"
    schema_path.write_text(json.dumps(schema), encoding="utf-8")

    with pytest.raises(
        ValueError,
        match="^active schema references are not permitted in overrides$",
    ) as exc_info:
        load_core_manifest(FIXTURES / "core-valid.yaml", schema_path=schema_path)
    assert exc_info.value.__cause__ is None
    assert exc_info.value.__context__ is None


@pytest.mark.parametrize("invalidity", ["invalid_module", "missing_field"])
def test_permissive_override_cannot_bypass_authoritative_schema(
    tmp_path: Path,
    invalidity: str,
):
    schema_path = tmp_path / "permissive.json"
    schema_path.write_text("{}", encoding="utf-8")
    manifest = _valid_manifest()
    if invalidity == "invalid_module":
        manifest["cores"][0]["module"] = "private-module"
    else:
        del manifest["cores"][0]["explicit_non_claims"]

    with pytest.raises(ValueError, match="core 0 invalid"):
        load_core_manifest(
            _write_manifest(tmp_path, manifest),
            schema_path=schema_path,
        )


@pytest.mark.parametrize(
    "manifest_text",
    [
        "manifest_version: '1.0'\nmanifest_version: '2.0'\ncores: []\n",
        (
            "manifest_version: '1.0'\ncores:\n"
            "  - core_id: F09\n"
            "    core_id: F08\n"
        ),
    ],
)
def test_load_core_manifest_rejects_duplicate_yaml_mapping_keys(
    tmp_path: Path,
    manifest_text: str,
):
    manifest_path = tmp_path / "duplicate.yaml"
    manifest_path.write_text(manifest_text, encoding="utf-8")

    with pytest.raises(
        ValueError,
        match="^manifest YAML contains a duplicate mapping key$",
    ) as exc_info:
        load_core_manifest(manifest_path)
    _assert_translated_error(exc_info)


def test_load_core_manifest_accepts_nonduplicative_yaml_merge(tmp_path: Path):
    manifest_text = _merged_manifest_text()
    safe_loaded = yaml.safe_load(manifest_text)
    assert set(safe_loaded["cores"][0]) == CORE_FIELDS
    manifest_path = tmp_path / "merged.yaml"
    manifest_path.write_text(manifest_text, encoding="utf-8")

    records = load_core_manifest(manifest_path)

    assert records[0].core_id == "F09"
    assert records[0].module == "fruitbench"


def test_load_core_manifest_allows_explicit_override_of_merged_key(
    tmp_path: Path,
):
    manifest_text = _merged_manifest_text(default_module="corinthlove")
    assert yaml.safe_load(manifest_text)["cores"][0]["module"] == "fruitbench"
    manifest_path = tmp_path / "merged-override.yaml"
    manifest_path.write_text(manifest_text, encoding="utf-8")

    records = load_core_manifest(manifest_path)

    assert records[0].module == "fruitbench"


@pytest.mark.parametrize(
    "manifest_text",
    [
        _merged_manifest_text(default_module="corinthlove").replace(
            "      module: corinthlove\n",
            "      module: corinthlove\n      module: fruitbench\n",
        ),
        _merge_sequence_with_duplicate_source_text(),
    ],
    ids=["single-source", "sequence-source"],
)
def test_load_core_manifest_rejects_duplicate_keys_in_yaml_merge_sources(
    tmp_path: Path,
    manifest_text: str,
):
    assert yaml.safe_load(manifest_text)["cores"][0]["module"] == "fruitbench"
    manifest_path = tmp_path / "duplicate-merge-source.yaml"
    manifest_path.write_text(manifest_text, encoding="utf-8")

    with pytest.raises(
        ValueError,
        match="^manifest YAML contains a duplicate mapping key$",
    ) as exc_info:
        load_core_manifest(manifest_path)
    _assert_translated_error(exc_info)


def test_load_core_manifest_accepts_reused_nested_merge_anchor(tmp_path: Path):
    manifest_text = _reused_nested_merge_manifest_text()
    safe_loaded = yaml.safe_load(manifest_text)
    schema = json.loads((SCHEMAS / "core.schema.json").read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema)
    for row in safe_loaded["cores"]:
        assert set(row) == CORE_FIELDS
        validator.validate(row)
    manifest_path = tmp_path / "reused-nested-merge.yaml"
    manifest_path.write_text(manifest_text, encoding="utf-8")

    records = load_core_manifest(manifest_path)

    assert [record.core_id for record in records] == ["F09", "F10"]
    assert [record.evidence_type for record in records] == ["action", "action"]


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


@pytest.mark.parametrize("schema_name", ["core.schema.json", "episode.schema.json"])
def test_packaged_schema_matches_authoring_schema(schema_name: str):
    assert (PACKAGE_SCHEMAS / schema_name).read_bytes() == (
        SCHEMAS / schema_name
    ).read_bytes()


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


@pytest.mark.parametrize(
    "source_path",
    [
        "C:\\secret\\file.md",
        "C:relative\\file.md",
        "\\rooted\\file.md",
        "\\\\server\\share\\file.md",
    ],
)
def test_validate_source_paths_rejects_windows_absolute_or_rooted_paths(
    tmp_path: Path,
    source_path: str,
):
    workspace_root = tmp_path / "workspace"
    workspace_root.mkdir()

    _assert_source_path_error(
        _record_with_source(source_path),
        workspace_root,
        "must be relative",
    )


def test_validate_source_paths_rejects_windows_style_lexical_traversal(
    tmp_path: Path,
):
    workspace_root = tmp_path / "workspace"
    workspace_root.mkdir()
    source_path = "sub\\..\\ok.md"
    (workspace_root / source_path).write_text("literal POSIX filename\n", encoding="utf-8")

    _assert_source_path_error(
        _record_with_source(source_path),
        workspace_root,
        "traversal",
    )


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
