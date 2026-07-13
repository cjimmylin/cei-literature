"""Deterministic L7 name rotation for the PUBLIC G7 perturbation battery (R-J13).

The module does not discover names heuristically.  The caller supplies the target
design's complete name set and explicit role metadata; this module selects only from a
versioned inventory whose entries were verified against the other PUBLIC seed banks.
"""
from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Collection, Iterable, Optional, Sequence, Tuple


_INVENTORY_PATH = Path(__file__).with_name("l7_name_inventory.json")
_GENDERS = {"female", "male", "unspecified"}


@dataclass(frozen=True)
class NameEntry:
    name: str
    apparent_gender: str
    source_design: str


@dataclass(frozen=True)
class RoleName:
    original: str
    apparent_gender: str = "unspecified"
    title: Optional[str] = None


@dataclass(frozen=True)
class NameSwap:
    original: str
    replacement: str
    apparent_gender: str
    title: Optional[str] = None


def load_inventory(path: Optional[Path] = None) -> Tuple[str, Tuple[NameEntry, ...]]:
    """Load and validate the versioned PUBLIC-name inventory."""
    source = Path(path) if path is not None else _INVENTORY_PATH
    data = json.loads(source.read_text(encoding="utf-8"))
    version = data.get("version")
    raw_entries = data.get("entries")
    if not isinstance(version, str) or not version:
        raise ValueError("L7 inventory requires a non-empty version")
    if not isinstance(raw_entries, list) or not raw_entries:
        raise ValueError("L7 inventory requires at least one entry")
    entries = []
    for raw in raw_entries:
        entry = NameEntry(
            name=str(raw.get("name", "")).strip(),
            apparent_gender=str(raw.get("apparent_gender", "")).strip(),
            source_design=str(raw.get("source_design", "")).strip(),
        )
        if not entry.name or not entry.source_design:
            raise ValueError(f"invalid L7 inventory entry: {raw!r}")
        if entry.apparent_gender not in _GENDERS - {"unspecified"}:
            raise ValueError(f"invalid apparent_gender for {entry.name!r}")
        entries.append(entry)
    return version, tuple(entries)


def _folded(values: Collection[str]) -> set:
    return {str(value).strip().casefold() for value in values}


def select_replacement(
    target_design: str,
    item_id: str,
    role_index: int,
    apparent_gender: str,
    *,
    target_names: Collection[str],
    used_names: Collection[str] = (),
    inventory: Optional[Sequence[NameEntry]] = None,
) -> str:
    """Select one eligible name by the registered `(design,item,role)` tuple.

    `target_names` is required so a caller cannot accidentally skip the R-J13 rule that
    every name already present in the target design is ineligible.
    """
    if apparent_gender not in _GENDERS:
        raise ValueError(f"unsupported apparent gender: {apparent_gender!r}")
    if role_index < 0:
        raise ValueError("role_index must be non-negative")
    entries = tuple(inventory) if inventory is not None else load_inventory()[1]
    forbidden = _folded(target_names) | _folded(used_names)
    candidates = {}
    for entry in entries:
        folded_name = entry.name.casefold()
        if entry.source_design == target_design or folded_name in forbidden:
            continue
        if apparent_gender != "unspecified" and entry.apparent_gender != apparent_gender:
            continue
        candidates.setdefault(folded_name, entry.name)
    eligible = sorted(candidates.values(), key=str.casefold)
    if not eligible:
        raise ValueError(
            f"no eligible L7 name for {target_design}/{item_id}/role-{role_index}"
        )
    seed = f"{target_design}\x1f{item_id}\x1f{role_index}".encode("utf-8")
    index = int.from_bytes(hashlib.sha256(seed).digest()[:8], "big") % len(eligible)
    return eligible[index]


def allocate_replacements(
    target_design: str,
    item_id: str,
    roles: Sequence[RoleName],
    *,
    target_names: Collection[str],
    inventory: Optional[Sequence[NameEntry]] = None,
) -> Tuple[NameSwap, ...]:
    """Allocate collision-free replacements for roles in stable role order."""
    used = set()
    swaps = []
    for role_index, role in enumerate(roles):
        replacement = select_replacement(
            target_design,
            item_id,
            role_index,
            role.apparent_gender,
            target_names=target_names,
            used_names=used,
            inventory=inventory,
        )
        used.add(replacement)
        swaps.append(NameSwap(role.original, replacement, role.apparent_gender, role.title))
    return tuple(swaps)


def apply_name_swaps(
    text: str,
    swaps: Iterable[object],
) -> str:
    """Replace supplied personal-name tokens simultaneously; leave all other text.

    Accepted entries are `NameSwap` values or `(RoleName, replacement)` pairs.  Titles,
    honorifics, surnames not supplied as the role name, and pronouns are untouched.
    """
    replacements = {}
    for value in swaps:
        if isinstance(value, NameSwap):
            original, replacement = value.original, value.replacement
        else:
            role, replacement = value  # type: ignore[misc]
            if not isinstance(role, RoleName):
                raise TypeError("swap pairs must start with RoleName")
            original = role.original
        previous = replacements.setdefault(original, str(replacement))
        if previous != replacement:
            raise ValueError(f"conflicting replacements for {original!r}")
    if not replacements:
        return text
    pattern = re.compile(
        r"(?<!\w)(?:" + "|".join(
            re.escape(name) for name in sorted(replacements, key=len, reverse=True)
        ) + r")(?!\w)"
    )
    return pattern.sub(lambda match: replacements[match.group(0)], text)
