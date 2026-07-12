from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, ValidationError
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


def load_core_manifest(
    path: Path,
    schema_path: Path | None = None,
) -> tuple[CoreRecord, ...]:
    manifest = yaml.safe_load(Path(path).read_text(encoding="utf-8"))
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

    resolved_schema_path = schema_path or (
        Path(__file__).parents[2] / "schemas/core.schema.json"
    )
    schema = json.loads(Path(resolved_schema_path).read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema)

    records: list[CoreRecord] = []
    core_ids: set[str] = set()
    for index, row in enumerate(cores):
        try:
            validator.validate(row)
        except ValidationError as error:
            field = _validation_field(error)
            raise ValueError(
                f"core {index} invalid at {field}: {error.message}"
            ) from None

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
            if relative_path.is_absolute():
                raise ValueError(f"{prefix} must be relative")
            if ".." in relative_path.parts:
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
