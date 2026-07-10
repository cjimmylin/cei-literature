#!/usr/bin/env python3
"""Matched benign/malicious arm audit (rubric C3; propagation P-2)."""
from __future__ import annotations

from collections import Counter, defaultdict
from functools import lru_cache
import json
import os
import re

from lib import families, surfaces


BANK = os.path.dirname(os.path.abspath(__file__))
CHAR_TOLERANCE = 40


def _core_replacements() -> tuple:
    values = []
    for pool in surfaces.ENTITY_POOLS.values():
        values.extend(pool["actors"])
        values.extend(pool["orgs"])
        values.extend(pool["windows"])
    for spec in families.all_families():
        for split in ("public", "calibration", "private"):
            values.extend(spec[f"{split}_resources"])
    return tuple(sorted({value.lower() for value in values}, key=len, reverse=True))


_CORE_ENTITY_PATTERN = re.compile(
    r"\b(?:" + "|".join(re.escape(value) for value in _core_replacements()) + r")\b"
)


@lru_cache(maxsize=4096)
def _normalized_core(text: str) -> str:
    """Cached stricter equivalent of ``surfaces.normalized_skeleton``.

    It normalizes the complete serialized transcript in one pass and keeps
    alphanumeric opaque keys intact because only standalone numbers change.
    """
    out = text.lower()
    out = re.sub(r"\b[a-z]{2}-\d{4}\b", "<case>", out)
    out = re.sub(r"\b\d+%?\b", "<number>", out)
    out = _CORE_ENTITY_PATTERN.sub("<entity>", out)
    return re.sub(r"\s+", " ", out).strip()


def _features(text: str) -> dict:
    return {
        "words": len(text.split()),
        "chars": len(text),
        "digits": sum(character.isdigit() for character in text),
        "sentences": len(re.findall(r"[.!?]", text)),
        "format_lines": len(re.findall(r"INTENT:|DECISION:", text)),
    }


def exact_transcript_groups(episodes: list) -> list:
    """Return duplicate groups using the complete four-turn transcript."""
    grouped = defaultdict(list)
    for episode in episodes:
        fingerprint = json.dumps(
            episode["multiturn_script"], sort_keys=True,
            ensure_ascii=False, separators=(",", ":"),
        )
        grouped[fingerprint].append(episode)
    return [tuple(group) for group in grouped.values() if len(group) > 1]


def normalized_core_transcript_groups(episodes: list) -> list:
    """Group full transcripts after entity/value normalization.

    ``surfaces.normalized_skeleton`` replaces case IDs, numbers, entities, and
    resources, but deliberately leaves the alphanumeric pointer keys intact.
    Thus the audit catches name-only duplicates without erasing the binding
    manipulation itself.
    """
    grouped = defaultdict(list)
    for episode in episodes:
        serialized = json.dumps(
            episode["multiturn_script"], sort_keys=True,
            ensure_ascii=False, separators=(",", ":"),
        )
        fingerprint = _normalized_core(serialized)
        grouped[fingerprint].append(episode)
    return [tuple(group) for group in grouped.values() if len(group) > 1]


def opposite_label_transcript_groups(groups: list, sidecar: dict) -> list:
    """Select duplicate groups containing both hidden type labels."""
    return [
        tuple(group) for group in groups
        if {
            sidecar[episode["id"]]["true_type"] for episode in group
        } == {"benign", "malicious"}
    ]


def _classify_opposite_groups(groups: list, sidecar: dict) -> tuple:
    declared, undeclared = [], []
    for group in opposite_label_transcript_groups(groups, sidecar):
        valid = (
            len(group) == 2
            and all(
                sidecar[episode["id"]].get(
                    "indistinguishable_control", False
                )
                for episode in group
            )
            and {episode["split"] for episode in group} == {"calibration"}
            and {
                sidecar[episode["id"]]["cue_variant"] for episode in group
            } == {"absent"}
        )
        (declared if valid else undeclared).append(group)
    return declared, undeclared


def audit_pairs(episodes: list, sidecar: dict, pairs: dict,
                assert_ok: bool = True) -> dict:
    by_id = {episode["id"]: episode for episode in episodes}
    failures = []
    class_counts = Counter()
    group_diffs = defaultdict(list)
    private_char_budget_delta_max = 0

    for pair_id, arms in pairs["private"].items():
        if set(arms) != {"benign", "malicious"}:
            failures.append(f"{pair_id}: incomplete arms")
            continue
        benign = by_id[arms["benign"]]
        malicious = by_id[arms["malicious"]]
        hb = sidecar[benign["id"]]
        hm = sidecar[malicious["id"]]

        same_fields = (
            ("family", benign["template_family"], malicious["template_family"]),
            ("split", benign["split"], malicious["split"]),
            ("pair", hb["pair_id"], hm["pair_id"]),
            ("world", hb["world_id"], hm["world_id"]),
            ("cue", hb["cue_variant"], hm["cue_variant"]),
            ("prior", hb["base_rate_benign"], hm["base_rate_benign"]),
            ("template", hb["surface_template_id"], hm["surface_template_id"]),
            ("semantic bank", hb["semantic_bank_id"], hm["semantic_bank_id"]),
        )
        for field, left, right in same_fields:
            if left != right:
                failures.append(f"{pair_id}: {field} mismatch {left!r} != {right!r}")

        if hb["defeat_class"] != hm["defeat_class"]:
            failures.append(
                f"{pair_id}: defeat class mismatch "
                f"{hb['defeat_class']} != {hm['defeat_class']}"
            )
        defeat_class = hb["defeat_class"]
        compact = defeat_class.replace("_", "").replace("-", "").lower()
        if "nonsequitur" in compact:
            failures.append(f"{pair_id}: defeat class uses a non-sequitur")
        class_counts[defeat_class] += 1

        script_b = benign["multiturn_script"]
        script_m = malicious["multiturn_script"]
        for unchanged_stage in ("stage_2", "stage_4"):
            if script_b[unchanged_stage] != script_m[unchanged_stage]:
                failures.append(f"{pair_id}: {unchanged_stage} differs outside manipulation")

        for stage in ("stage_1", "stage_3"):
            fb = _features(script_b[stage])
            fm = _features(script_m[stage])
            diffs = {name: fb[name] - fm[name] for name in fb}
            group_diffs[(benign["template_family"], stage)].append(diffs)
            if diffs["words"] != 0:
                failures.append(f"{pair_id}: {stage} word budget differs by {diffs['words']}")
            char_tolerance = 0 if stage == "stage_3" else CHAR_TOLERANCE
            if abs(diffs["chars"]) > char_tolerance:
                failures.append(f"{pair_id}: {stage} char budget differs by {diffs['chars']}")
            if stage == "stage_3":
                private_char_budget_delta_max = max(
                    private_char_budget_delta_max, abs(diffs["chars"])
                )
            if diffs["digits"] != 0:
                failures.append(f"{pair_id}: {stage} digit budget differs by {diffs['digits']}")
            if diffs["sentences"] != 0 or diffs["format_lines"] != 0:
                failures.append(f"{pair_id}: {stage} structure differs {diffs}")

    exact_declared, exact_undeclared = _classify_opposite_groups(
        exact_transcript_groups(episodes), sidecar
    )
    core_declared, core_undeclared = _classify_opposite_groups(
        normalized_core_transcript_groups(episodes), sidecar
    )
    if len(exact_declared) != 12:
        failures.append(
            f"declared exact ambiguity groups {len(exact_declared)} != 12"
        )
    if exact_undeclared:
        failures.append(
            f"undeclared exact opposite-label groups: {len(exact_undeclared)}"
        )
    if len(core_declared) != 12:
        failures.append(
            f"declared normalized-core groups {len(core_declared)} != 12"
        )
    if core_undeclared:
        failures.append(
            "undeclared normalized-core opposite-label groups: "
            f"{len(core_undeclared)}"
        )

    result = {
        "n_pairs": len(pairs["private"]),
        "failures": failures,
        "defeat_class_counts": dict(sorted(class_counts.items())),
        "n_family_stage_groups": len(group_diffs),
        "private_char_budget_delta_max": private_char_budget_delta_max,
        "n_declared_ambiguity_groups": len(exact_declared),
        "n_undeclared_opposite_label_groups": len(exact_undeclared),
        "n_declared_normalized_core_groups": len(core_declared),
        "n_undeclared_normalized_core_groups": len(core_undeclared),
    }
    if assert_ok:
        assert not failures, "matched-pair/defeat class audit failed:\n" + "\n".join(failures)
    return result


def _load(bank_dir: str):
    import yaml
    episodes = []
    for rel in (
        "episodes/private_bank.yaml", "episodes/calibration_bank.yaml",
        "seeds_public.yaml",
    ):
        path = os.path.join(bank_dir, rel)
        if not os.path.exists(path):
            continue
        with open(path, encoding="utf-8") as handle:
            episodes.extend(yaml.safe_load(handle))
    with open(os.path.join(bank_dir, "sidecar", "ground_truth.json"), encoding="utf-8") as handle:
        sidecar = json.load(handle)
    with open(os.path.join(bank_dir, "sidecar", "pair_registry.json"), encoding="utf-8") as handle:
        pairs = json.load(handle)
    return episodes, sidecar, pairs


def _write_report(result: dict, bank_dir: str):
    lines = [
        "# CHARITROC matched-arm symmetry and defeat-class audit",
        "",
        "All private twins share family, world, prior, pressure, gate, and surface wrapper. "
        "Only the initial signal and new-information premise may differ.",
        "",
        f"- matched pairs audited: {result['n_pairs']}",
        f"- family × manipulated-stage groups: {result['n_family_stage_groups']}",
        f"- stage-1 character tolerance: {CHAR_TOLERANCE}",
        "- stage-3 character difference allowed: 0",
        "- word, digit, sentence, and response-format differences allowed: 0",
        f"- private stage-3 maximum character delta: {result['private_char_budget_delta_max']}",
        f"- declared exact ambiguity groups: {result['n_declared_ambiguity_groups']}",
        f"- undeclared exact opposite-label groups: {result['n_undeclared_opposite_label_groups']}",
        f"- declared normalized-core ambiguity groups: {result['n_declared_normalized_core_groups']}",
        f"- undeclared normalized-core opposite-label groups: {result['n_undeclared_normalized_core_groups']}",
        "",
        "## Defeat classes",
        "",
    ]
    for label, count in result["defeat_class_counts"].items():
        lines.append(f"- `{label}`: {count} pairs")
    lines.extend(["", "## Result", ""])
    if result["failures"]:
        lines.append("FAIL")
        lines.extend(f"- {failure}" for failure in result["failures"])
    else:
        lines.append("PASS — all matched arms satisfy structural and semantic matching.")
    with open(os.path.join(bank_dir, "reports", "arm_symmetry_table.md"), "w", encoding="utf-8") as handle:
        handle.write("\n".join(lines) + "\n")


def run(bank_dir: str = BANK, assert_ok: bool = True) -> dict:
    episodes, sidecar, pairs = _load(bank_dir)
    result = audit_pairs(episodes, sidecar, pairs, assert_ok=assert_ok)
    _write_report(result, bank_dir)
    return result


if __name__ == "__main__":
    print(json.dumps(run(assert_ok=True), indent=2))
