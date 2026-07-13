from __future__ import annotations

from collections import Counter
import hashlib
import json
from pathlib import Path

from jsonschema import Draft202012Validator
import yaml

from biblebench_pilot.contracts import canonical_sha256
from biblebench_pilot.schedule import (
    CueVariant,
    DevelopmentEpisode,
    DevelopmentPack,
    compile_schedule,
)


PACKAGE_ROOT = Path(__file__).parents[1]
BIBLEBENCH_ROOT = PACKAGE_ROOT.parent
SCHEMA_PATH = PACKAGE_ROOT / "schemas" / "authored-episode-bank.schema.json"
SELECTION_PATH = (
    BIBLEBENCH_ROOT
    / "output"
    / "docs"
    / "superpowers"
    / "specs"
    / "2026-07-11-biblebench-42-core-selection.md"
)
SELECTION_SHA256 = (
    "c0de28c064fdb87ae9ac4d38d53190856912b88f645492cc087ff2d0cee346e2"
)
MODULE_PATHS = {
    module: PACKAGE_ROOT / "modules" / module / "episodes.yaml"
    for module in (
        "fruitbench",
        "corinthlove",
        "tencommandments",
        "sermonmount",
    )
}
EXPECTED_CORES = {
    "fruitbench": {f"F{index:02d}" for index in range(1, 13)},
    "corinthlove": {f"L{index:02d}" for index in range(1, 9)},
    "tencommandments": {f"T{index:02d}" for index in range(1, 13)},
    "sermonmount": {f"S{index:02d}" for index in range(1, 11)},
}
EXPECTED_STRATA = {
    "fruitbench": Counter(common_life=9, christian_facing=3),
    "corinthlove": Counter(common_life=8, christian_facing=4),
    "tencommandments": Counter(common_life=8, christian_facing=4),
    "sermonmount": Counter(common_life=9, christian_facing=3),
}
ACTOR_IDS = ("A", "B", "C", "D")


def _load_banks() -> dict[str, dict]:
    assert SCHEMA_PATH.is_file(), f"missing schema: {SCHEMA_PATH}"
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema)
    banks: dict[str, dict] = {}
    for module, path in MODULE_PATHS.items():
        assert path.is_file(), f"missing episode bank: {path}"
        bank = yaml.safe_load(path.read_text(encoding="utf-8"))
        errors = sorted(validator.iter_errors(bank), key=lambda row: list(row.path))
        assert not errors, "\n".join(error.message for error in errors)
        assert bank["module"] == module
        banks[module] = bank
    return banks


def _to_development_pack(module: str, bank: dict) -> DevelopmentPack:
    episodes = []
    for row in bank["episodes"]:
        variants = tuple(
            CueVariant(
                cue=cue,
                cue_surface=row["cue_surfaces"][cue],
                shared_body=row["shared_body"],
                task_semantics_sha256=canonical_sha256(row["task_semantics"]),
                answer_semantics_sha256=canonical_sha256(row["answer_semantics"]),
                tool_schema_sha256=canonical_sha256(row["tool_schema"]),
                response_schema_sha256=canonical_sha256(row["response_schema"]),
                decoding=row["decoding"],
                semantic_response_tokens=tuple(row["semantic_response_tokens"]),
            )
            for cue in ("C0", "C1", "C2")
        )
        episodes.append(
            DevelopmentEpisode(
                episode_id=row["episode_id"],
                role=row["role"],
                forecast_payload=row["forecast_payload"],
                probe_payload=row["probe_payload"],
                variants=variants,
            )
        )
    return DevelopmentPack(module=module, episodes=tuple(episodes))


def test_approved_selection_bytes_are_unchanged() -> None:
    assert hashlib.sha256(SELECTION_PATH.read_bytes()).hexdigest() == SELECTION_SHA256


def test_all_four_authored_episode_banks_exist_and_validate() -> None:
    banks = _load_banks()
    assert set(banks) == set(MODULE_PATHS)


def test_episode_banks_have_registered_geometry_and_core_coverage() -> None:
    banks = _load_banks()
    observed_cores: set[str] = set()
    observed_episode_ids: set[str] = set()
    observed_strata: Counter[str] = Counter()
    for module, bank in banks.items():
        episodes = bank["episodes"]
        assert len(episodes) == 12
        assert Counter(row["role"] for row in episodes) == Counter(
            target=4, null=4, restraint=4
        )
        assert Counter(row["stratum"] for row in episodes) == EXPECTED_STRATA[module]
        module_cores = {row["core_id"] for row in episodes}
        assert module_cores == EXPECTED_CORES[module]
        observed_cores.update(module_cores)
        module_episode_ids = {row["episode_id"] for row in episodes}
        assert len(module_episode_ids) == 12
        assert observed_episode_ids.isdisjoint(module_episode_ids)
        observed_episode_ids.update(module_episode_ids)
        observed_strata.update(row["stratum"] for row in episodes)
    assert len(observed_cores) == 42
    assert len(observed_episode_ids) == 48
    assert observed_strata == Counter(common_life=34, christian_facing=14)


def test_each_episode_has_three_distinct_registered_cue_surfaces() -> None:
    for bank in _load_banks().values():
        for episode in bank["episodes"]:
            cue_surfaces = episode["cue_surfaces"]
            assert set(cue_surfaces) == {"C0", "C1", "C2"}
            assert len(set(cue_surfaces.values())) == 3


def test_source_hashes_and_capability_controls_are_real() -> None:
    for bank in _load_banks().values():
        for episode in bank["episodes"]:
            for source in episode["source_artifacts"]:
                path = BIBLEBENCH_ROOT / source["path"]
                assert path.is_file(), path
                assert hashlib.sha256(path.read_bytes()).hexdigest() == source["sha256"]
                source_headings = {
                    line.strip()
                    for line in path.read_text(encoding="utf-8").splitlines()
                    if line.lstrip().startswith("#")
                }
                assert source["heading"] in source_headings, (
                    episode["episode_id"],
                    source["heading"],
                )
            assert episode["capability_twin"] is not None
            if episode["mode"] == "action":
                assert episode["execution_contract"]["kind"] == "sandbox"


def test_answer_contracts_are_closed_and_tokens_are_consistent() -> None:
    for bank in _load_banks().values():
        for episode in bank["episodes"]:
            response_schema = episode["response_schema"]
            required = response_schema["required"]
            assert response_schema["type"] == "object"
            assert response_schema["additionalProperties"] is False
            assert set(required) == set(response_schema["properties"])
            assert episode["answer_semantics"]["required_fields"] == required
            assert episode["semantic_response_tokens"] == required


def test_real_episode_banks_compile_through_task7() -> None:
    for index, (module, bank) in enumerate(_load_banks().items(), start=1):
        pack = _to_development_pack(module, bank)
        schedule = compile_schedule(pack, actor_ids=ACTOR_IDS, seed=713 + index)
        assert len(schedule.logical_calls) == 336
        assert len(schedule.forecast_rows) == 48
        assert len(schedule.primary_rows) == 144
        assert len(schedule.probe_rows) == 144
