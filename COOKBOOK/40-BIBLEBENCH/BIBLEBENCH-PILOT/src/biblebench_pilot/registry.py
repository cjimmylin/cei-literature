from __future__ import annotations

from dataclasses import dataclass
from importlib.resources import files
import json
from pathlib import Path, PurePosixPath, PureWindowsPath
from typing import Any

from jsonschema import Draft202012Validator, SchemaError, ValidationError
import yaml


_ARRAY_FIELDS = (
    "source_paths",
    "passage_anchors",
    "explicit_non_claims",
    "eligible_modes",
    "eligible_transforms",
    "shared_red_lines",
    "module_red_lines",
)
_MANIFEST_FIELDS = {"manifest_version", "cores"}
_YAML_MERGE_TAG = "tag:yaml.org,2002:merge"


class _DuplicateKeyError(yaml.YAMLError):
    pass


class _UniqueKeySafeLoader(yaml.SafeLoader):
    pass


def _check_duplicate_mapping_keys(
    loader: _UniqueKeySafeLoader,
    node: yaml.MappingNode,
    *,
    deep: bool,
    active_node_ids: set[int],
    seen_node_ids: set[int],
) -> None:
    node_id = id(node)
    if node_id in active_node_ids or node_id in seen_node_ids:
        return
    active_node_ids.add(node_id)

    explicit_keys: set[Any] = set()
    merge_sources: list[yaml.MappingNode] = []
    for key_node, value_node in node.value:
        if key_node.tag == _YAML_MERGE_TAG:
            if isinstance(value_node, yaml.MappingNode):
                merge_sources.append(value_node)
            elif isinstance(value_node, yaml.SequenceNode):
                merge_sources.extend(
                    source
                    for source in value_node.value
                    if isinstance(source, yaml.MappingNode)
                )
            continue
        key = loader.construct_object(key_node, deep=deep)
        try:
            duplicate = key in explicit_keys
        except TypeError:
            raise yaml.constructor.ConstructorError(
                "while constructing a mapping",
                node.start_mark,
                "found an unhashable key",
                key_node.start_mark,
            ) from None
        if duplicate:
            raise _DuplicateKeyError
        explicit_keys.add(key)

    for source in merge_sources:
        _check_duplicate_mapping_keys(
            loader,
            source,
            deep=deep,
            active_node_ids=active_node_ids,
            seen_node_ids=seen_node_ids,
        )

    active_node_ids.remove(node_id)
    seen_node_ids.add(node_id)


def _construct_unique_mapping(
    loader: _UniqueKeySafeLoader,
    node: yaml.MappingNode,
    deep: bool = False,
) -> dict[Any, Any]:
    _check_duplicate_mapping_keys(
        loader,
        node,
        deep=deep,
        active_node_ids=set(),
        seen_node_ids=set(),
    )
    loader.flatten_mapping(node)
    return yaml.constructor.SafeConstructor.construct_mapping(
        loader,
        node,
        deep=deep,
    )


_UniqueKeySafeLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
    _construct_unique_mapping,
)


@dataclass(frozen=True)
class CoreRecord:
    core_id: str
    module: str
    source_paths: tuple[str, ...]
    passage_anchors: tuple[str, ...]
    construct: str
    explicit_non_claims: tuple[str, ...]
    evidence_type: str
    behavioral_attribution: str
    eligible_modes: tuple[str, ...]
    eligible_transforms: tuple[str, ...]
    deficient_pole: str
    counterfeit_pole: str
    shared_red_lines: tuple[str, ...]
    module_red_lines: tuple[str, ...]


def _validation_field(error: ValidationError) -> str:
    if error.path:
        return ".".join(str(part) for part in error.path)
    if error.validator == "required" and isinstance(error.instance, dict):
        for field in error.validator_value:
            if field not in error.instance:
                return field
    return "<root>"


def _to_core_record(row: dict[str, Any]) -> CoreRecord:
    values = dict(row)
    for field in _ARRAY_FIELDS:
        values[field] = tuple(values[field])
    return CoreRecord(**values)


def _load_authoritative_schema() -> dict[str, Any]:
    try:
        schema_text = (
            files("biblebench_pilot.schemas")
            .joinpath("core.schema.json")
            .read_text(encoding="utf-8")
        )
    except OSError:
        raise ValueError("authoritative core schema could not be read") from None
    try:
        schema = json.loads(schema_text)
    except json.JSONDecodeError:
        raise ValueError("authoritative core schema is not valid JSON") from None
    try:
        Draft202012Validator.check_schema(schema)
    except SchemaError:
        raise ValueError(
            "authoritative core schema is not a valid Draft 2020-12 schema"
        ) from None
    return schema


def _load_override_schema(schema_path: Path) -> dict[str, Any]:
    try:
        schema_text = Path(schema_path).read_text(encoding="utf-8")
    except OSError:
        raise ValueError("schema override could not be read") from None
    try:
        schema = json.loads(schema_text)
    except json.JSONDecodeError:
        raise ValueError("schema override is not valid JSON") from None
    try:
        Draft202012Validator.check_schema(schema)
    except SchemaError:
        raise ValueError(
            "schema override is not a valid Draft 2020-12 schema"
        ) from None
    return schema


def _validate_core(
    validator: Draft202012Validator,
    row: Any,
    index: int,
) -> None:
    try:
        validator.validate(row)
    except ValidationError as error:
        field = _validation_field(error)
        raise ValueError(
            f"core {index} invalid at {field}: {error.message}"
        ) from None


def load_core_manifest(
    path: Path,
    schema_path: Path | None = None,
) -> tuple[CoreRecord, ...]:
    manifest_text = Path(path).read_text(encoding="utf-8")
    try:
        manifest = yaml.load(manifest_text, Loader=_UniqueKeySafeLoader)
    except _DuplicateKeyError:
        raise ValueError(
            "manifest YAML contains a duplicate mapping key"
        ) from None
    except yaml.YAMLError:
        raise ValueError("manifest YAML is invalid") from None
    if not isinstance(manifest, dict) or set(manifest) != _MANIFEST_FIELDS:
        raise ValueError(
            "manifest top-level must contain exactly manifest_version and cores"
        )

    manifest_version = manifest["manifest_version"]
    if not isinstance(manifest_version, str) or not manifest_version:
        raise ValueError("manifest_version must be a nonempty string")

    cores = manifest["cores"]
    if not isinstance(cores, list) or not cores:
        raise ValueError("cores must be a nonempty list")

    authoritative_validator = Draft202012Validator(_load_authoritative_schema())
    override_validator = None
    if schema_path is not None:
        override_validator = Draft202012Validator(
            _load_override_schema(schema_path)
        )

    records: list[CoreRecord] = []
    core_ids: set[str] = set()
    for index, row in enumerate(cores):
        _validate_core(authoritative_validator, row, index)
        if override_validator is not None:
            _validate_core(override_validator, row, index)

        core_id = row["core_id"]
        if core_id in core_ids:
            raise ValueError(f"duplicate core_id {core_id}")
        core_ids.add(core_id)
        records.append(_to_core_record(row))

    return tuple(records)


def validate_source_paths(
    records: tuple[CoreRecord, ...],
    workspace_root: Path,
) -> None:
    try:
        root = Path(workspace_root).resolve()
    except (OSError, RuntimeError):
        raise ValueError("workspace_root must be an existing directory") from None
    if not root.is_dir():
        raise ValueError("workspace_root must be an existing directory")

    for record in records:
        for source_path in record.source_paths:
            prefix = f"core {record.core_id} source path {source_path!r}"
            relative_path = Path(source_path)
            posix_path = PurePosixPath(source_path)
            windows_path = PureWindowsPath(source_path)
            if (
                relative_path.is_absolute()
                or posix_path.is_absolute()
                or bool(windows_path.drive)
                or bool(windows_path.root)
            ):
                raise ValueError(f"{prefix} must be relative")
            if ".." in posix_path.parts or ".." in windows_path.parts:
                raise ValueError(
                    f"{prefix} contains '..' traversal "
                    "(rejected whether or not it escapes workspace root)"
                )
            if not source_path.endswith(".md"):
                raise ValueError(f"{prefix} must end in .md")

            try:
                resolved_path = (root / relative_path).resolve()
                resolved_path.relative_to(root)
            except ValueError:
                raise ValueError(f"{prefix} escapes workspace root") from None
            except (OSError, RuntimeError):
                raise ValueError(f"{prefix} cannot be resolved") from None

            if not resolved_path.exists():
                raise ValueError(f"{prefix} does not exist")
            if not resolved_path.is_file():
                raise ValueError(f"{prefix} is not a regular file")
