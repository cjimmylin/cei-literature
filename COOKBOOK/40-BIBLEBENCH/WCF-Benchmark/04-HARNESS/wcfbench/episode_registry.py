"""Human-review loader for the inert EPISODE specification draft.

This module is deliberately not wired into a runner. The default loader refuses
an unapproved registry; allow_unapproved=True exists only so tests and human
review tooling can inspect the draft.
"""

from __future__ import annotations

import json
import os
from typing import Any, Dict

from .loader import ItemRecord
from .narrowgate import DEFAULT_DIALS, EpisodeSpec


DRAFT_REGISTRY_PATH = os.path.normpath(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        "config",
        "episode-spec-registry.draft.json",
    )
)


class EpisodeRegistryError(ValueError):
    """Raised when an EPISODE registry is invalid or not approved."""


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise EpisodeRegistryError(message)


def _episode_spec_from_entry(entry: Dict[str, Any]) -> EpisodeSpec:
    item_id = entry.get("item_id")
    _require(isinstance(item_id, str) and bool(item_id.strip()), "episode entry needs a non-empty item_id")
    raw = entry.get("episode_spec")
    _require(isinstance(raw, dict), f"[{item_id}] episode_spec must be an object")
    metric = raw.get("success_metric")
    tools = raw.get("tools")
    _require(
        isinstance(metric, str) and bool(metric.strip()),
        f"[{item_id}] success_metric must be a non-empty string",
    )
    _require(
        isinstance(tools, list) and bool(tools)
        and all(isinstance(tool, str) and tool.strip() for tool in tools),
        f"[{item_id}] tools must be a non-empty list of names",
    )
    _require(
        raw.get("dials") == list(DEFAULT_DIALS),
        f"[{item_id}] dials must be {list(DEFAULT_DIALS)!r}",
    )
    try:
        return EpisodeSpec(item_id=item_id, **raw)
    except (TypeError, ValueError) as exc:
        raise EpisodeRegistryError(f"[{item_id}] invalid EpisodeSpec: {exc}") from exc


def _validate_registry(raw: Any) -> Dict[str, Any]:
    _require(isinstance(raw, dict), "episode registry must be a JSON object")
    _require(raw.get("schema_version") == 1, "episode registry schema_version must be 1")
    status = raw.get("status")
    _require(status in {"DRAFT_UNAPPROVED", "APPROVED"}, f"invalid registry status: {status!r}")
    approval = raw.get("approval")
    _require(isinstance(approval, dict), "episode registry needs an approval object")
    approved = approval.get("approved")
    _require(isinstance(approved, bool), "approval.approved must be boolean")
    _require(
        approved == (status == "APPROVED"),
        "registry status and approval.approved disagree",
    )

    entries = raw.get("entries")
    _require(isinstance(entries, list) and bool(entries), "episode registry entries must be a non-empty list")
    ids = []
    for entry in entries:
        _require(isinstance(entry, dict), "each episode registry entry must be an object")
        item_id = entry.get("item_id")
        _require(isinstance(item_id, str) and bool(item_id.strip()), "episode entry needs a non-empty item_id")
        ids.append(item_id)
        _require(
            entry.get("prompt_source") == "bank.stem",
            f"[{item_id}] prompt_source must be bank.stem",
        )
        review = entry.get("human_review")
        _require(isinstance(review, dict), f"[{item_id}] human_review must be an object")
        _require(
            isinstance(review.get("status"), str) and bool(review["status"].strip()),
            f"[{item_id}] human_review.status is required",
        )
        _require(
            isinstance(review.get("mapping_basis"), str) and bool(review["mapping_basis"].strip()),
            f"[{item_id}] human_review.mapping_basis is required",
        )
        limitations = review.get("known_limitations")
        _require(
            isinstance(limitations, list) and bool(limitations)
            and all(isinstance(note, str) and note.strip() for note in limitations),
            f"[{item_id}] human_review.known_limitations must be a non-empty list",
        )
        _episode_spec_from_entry(entry)
    _require(len(ids) == len(set(ids)), "episode registry contains duplicate item_id values")
    return raw


def load_episode_registry(
    path: str = DRAFT_REGISTRY_PATH,
    *,
    allow_unapproved: bool = False,
) -> Dict[str, Any]:
    """Load and validate a registry, refusing unapproved data by default.

    allow_unapproved is an explicit review-only escape hatch. Live or
    production callers must not set it.
    """
    try:
        with open(path, "r", encoding="utf-8") as handle:
            registry = _validate_registry(json.load(handle))
    except (OSError, json.JSONDecodeError) as exc:
        raise EpisodeRegistryError(f"cannot load episode registry {path}: {exc}") from exc
    if registry["status"] != "APPROVED" and not allow_unapproved:
        raise EpisodeRegistryError(
            f"episode registry is {registry['status']}; human approval is required"
        )
    return registry


def episode_specs_from_registry(
    registry: Dict[str, Any],
    *,
    allow_unapproved: bool = False,
) -> Dict[str, EpisodeSpec]:
    """Construct specs, requiring an explicit override for review-only drafts."""
    _validate_registry(registry)
    if registry["status"] != "APPROVED" and not allow_unapproved:
        raise EpisodeRegistryError(
            f"episode registry is {registry['status']}; human approval is required"
        )
    return {
        entry["item_id"]: _episode_spec_from_entry(entry)
        for entry in registry["entries"]
    }


def build_blind_episode_prompt(entry: Dict[str, Any], item: ItemRecord) -> str:
    """Return only the examinee-facing bank stem for a matching episode item."""
    item_id = entry.get("item_id")
    _require(
        entry.get("prompt_source") == "bank.stem",
        f"[{item_id}] blind episode prompts may only use bank.stem",
    )
    _require(item.id == item_id, f"[{item_id}] prompt item mismatch: got {item.id}")
    return item.stem
