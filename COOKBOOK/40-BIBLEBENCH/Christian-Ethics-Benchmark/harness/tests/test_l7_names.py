"""R-J13 deterministic L7 name-rotation contract (PUBLIC designs only)."""
import re
from importlib.util import find_spec
from pathlib import Path

import pytest

from walkworthy.l7_names import (
    NameEntry,
    RoleName,
    allocate_replacements,
    apply_name_swaps,
    load_inventory,
    select_replacement,
)
from walkworthy.loader import DESIGN_CODES


def test_l7_rotation_module_and_inventory_are_machine_readable():
    assert find_spec("walkworthy.l7_names") is not None
    data_path = Path(__file__).parents[1] / "walkworthy" / "l7_name_inventory.json"
    assert data_path.is_file()


def test_inventory_has_public_provenance_and_gender_capacity(benchmark_root):
    version, entries = load_inventory()
    assert version == "2026-07-12-rj13-v1"
    assert {entry.source_design for entry in entries} == set(DESIGN_CODES)
    for design in DESIGN_CODES:
        by_gender = [entry.apparent_gender for entry in entries
                     if entry.source_design == design]
        assert by_gender.count("female") >= 4
        assert by_gender.count("male") >= 4
        public_text = (Path(benchmark_root) / "DESIGNS" /
                       f"{design}-seeds.md").read_text(encoding="utf-8")
        for entry in (e for e in entries if e.source_design == design):
            assert re.search(rf"\b{re.escape(entry.name)}\b", public_text)


def test_selector_excludes_target_design_target_names_and_wrong_gender():
    inventory = (
        NameEntry("Abena", "female", "07-seventyseven"),
        NameEntry("Marta", "female", "05-ordoamoris"),
        NameEntry("Owen", "male", "05-ordoamoris"),
    )
    with pytest.raises(ValueError, match="no eligible L7 name"):
        select_replacement(
            "07-seventyseven", "WW-07-A01", 0, "female",
            target_names={"Marta"}, inventory=inventory,
        )


def test_selector_is_deterministic_for_the_registered_tuple():
    inventory = (
        NameEntry("Marta", "female", "05-ordoamoris"),
        NameEntry("Priyanka", "female", "01-goodsamaritan"),
        NameEntry("Colette", "female", "09-doubleedge"),
    )
    kwargs = dict(
        target_design="07-seventyseven",
        item_id="WW-07-C01",
        role_index=2,
        apparent_gender="female",
        target_names={"Abena"},
        inventory=inventory,
    )
    assert select_replacement(**kwargs) == select_replacement(**kwargs)


def test_allocator_never_reuses_a_name_within_the_target_design():
    inventory = tuple(
        NameEntry(name, "female", source)
        for name, source in (
            ("Marta", "05-ordoamoris"),
            ("Priyanka", "01-goodsamaritan"),
            ("Colette", "09-doubleedge"),
            ("Halima", "06-crookedpath"),
        )
    )
    roles = [RoleName("Alice", "female"), RoleName("Bea", "female"),
             RoleName("Cara", "female")]
    swaps = allocate_replacements(
        "07-seventyseven", "WW-07-C01", roles,
        target_names={role.original for role in roles}, inventory=inventory,
    )
    assert len({swap.replacement for swap in swaps}) == len(roles)
    assert swaps == allocate_replacements(
        "07-seventyseven", "WW-07-C01", roles,
        target_names={role.original for role in roles}, inventory=inventory,
    )


def test_name_swap_changes_exact_names_but_preserves_titles_and_pronouns():
    roles = [
        RoleName("Alice", "female", title="Dr."),
        RoleName("Bob", "male", title="Mr."),
    ]
    swaps = [
        # Title metadata is audited but the operation changes name tokens only.
        (roles[0], "Marta"),
        (roles[1], "Owen"),
    ]
    text = "Dr. Alice told Mr. Bob that she would call him. Anna heard Alice."
    changed = apply_name_swaps(text, swaps)
    assert changed == "Dr. Marta told Mr. Owen that she would call him. Anna heard Marta."
