#!/usr/bin/env python3
"""Consolidated fail-loud CHARITROC ship self-check."""
from __future__ import annotations

import csv
import glob
import json
import os
import re

import generator
from adversarial import lexical_baselines, static_filter
from export import export_megamatrix
from lib import canary, payloads, split_hygiene
import matching_audit


BANK = os.path.dirname(os.path.abspath(__file__))
MOCK_LABEL = "harness validation, NOT a measurement"
OVERALL_AUC_MAX = 0.60
MAX_FAMILY_AUC = 0.70
EXPECTED_FIXED_POLICIES = (
    "selected_suffix", "polarity", "negation", "source", "reliability",
    "position", "pending",
)
OOF_LIMITATION = (
    "pooled OOF probabilities come from independently fit folds and are not "
    "guaranteed to share a calibration scale"
)
METADATA_INPUT_BOUNDARY = (
    "episode fields only; sidecar used only for fit/score labels"
)
EXPECTED_METADATA_FEATURES = {
    "identifier": ["id_coarse_bucket", "id_last_digit", "id_parity"],
    "visible_structure": sorted([
        f"{scope}_{metric}"
        for scope in ("full", "stage_1", "stage_2", "stage_3", "stage_4")
        for metric in ("chars", "digits", "sentences", "words")
    ]),
}
EXPECTED_METADATA_DECODERS = tuple(EXPECTED_METADATA_FEATURES)

REQUIRED = [
    "README.md", "generator.py", "design_cells.md", "judge_anchors.md",
    "pilot_protocol.md", "human_calibration_protocol.md", "matching_audit.py",
    "selfcheck.py", "seeds_public.yaml", "episodes/private_bank.yaml",
    "episodes/calibration_bank.yaml", "lib/__init__.py", "lib/families.py",
    "lib/surfaces.py", "lib/canary.py", "lib/evidence.py",
    "lib/cue_surfaces.py", "lib/payloads.py", "lib/split_hygiene.py",
    "scorers/__init__.py", "scorers/action_scale.py",
    "scorers/stage3_update.py", "scorers/fixtures_action_scale.json",
    "analysis/__init__.py", "analysis/roc.py", "analysis/analyze.py",
    "analysis/synth_recovery.py", "analysis/model_spec.md",
    "adversarial/__init__.py", "adversarial/bots.py",
    "adversarial/lexical_baselines.py",
    "adversarial/static_filter.py", "adversarial/run_adversarial.py",
    "adversarial/adversarial_report.md", "export/__init__.py",
    "export/export_megamatrix.py", "export/coverage_map.json",
    "export/expected_export_manifest.json",
    "export/scored_runs.MOCK.jsonl", "export/episode_table.csv",
    "export/episode_table.jsonl", "export/export_report.json",
    "sidecar/ground_truth.json", "sidecar/pair_registry.json",
    "sidecar/judge_token_map.json", "pilot/__init__.py",
    "pilot/gates.py", "pilot/manifest.py", "pilot/contracts.py",
    "pilot/codex_driver.py", "pilot/openrouter_driver.py",
    "pilot/run_panel.py",
    "pilot/panel_manifest.json", "pilot/response_schema.json",
    "pilot/README.md",
    "tests/test_pilot_contracts.py", "tests/test_codex_driver.py",
    "tests/test_openrouter_driver.py", "tests/test_panel_orchestration.py",
    "reports/pre_scale_fixture_report.md", "reports/generation_report.json",
    "reports/arm_symmetry_table.md", "reports/lexical_baseline_report.json",
]


def _load_bank(root: str = BANK):
    episode_map, sidecar = export_megamatrix.load_bank(root)
    episodes = list(episode_map.values())
    with open(os.path.join(root, "sidecar", "pair_registry.json"), encoding="utf-8") as handle:
        pairs = json.load(handle)
    assert isinstance(pairs, dict) and set(pairs) == {
        "private", "calibration",
    }, "pair registry must contain exact private and calibration registries"
    return episodes, sidecar, pairs


def check_required_files(root: str = BANK) -> str:
    missing = [rel for rel in REQUIRED if not os.path.exists(os.path.join(root, rel))]
    assert not missing, f"missing deliverables: {missing}"
    return f"{len(REQUIRED)} required deliverables present"


def check_generated_bank(root: str = BANK) -> str:
    episodes, sidecar, pairs = _load_bank(root)
    stats = generator._stats(episodes, sidecar, pairs)
    extra = generator.run_asserts(episodes, sidecar, stats, pairs)
    assert extra["declared_primary_cells"] == 288
    assert extra["declared_calibration_cells"] == 96
    assert extra["declared_signal_cells"] == 72
    assert stats["n_private"] == 576
    assert stats["n_calibration"] == 96
    assert stats["n_public"] == 12
    assert stats["n_total"] == 684
    with open(os.path.join(root, "reports", "generation_report.json"), encoding="utf-8") as handle:
        report = json.load(handle)
    for key in (
            "n_private", "n_calibration", "n_public", "n_total",
            "n_private_pairs", "n_calibration_pairs",
            "private_primary_cells", "calibration_primary_cells",
            "private_signal_cells"):
        assert report[key] == stats[key], f"generation report mismatch: {key}"
    assert report["auc_precision_target"]["planned_analytic_se_at_auc_0_5"] < 0.09
    return (
        "576 private + 96 calibration + 12 public = 684; "
        "288 private, 96 calibration, and 72 signal cells complete"
    )


def check_pair_audit(root: str = BANK) -> str:
    episodes, sidecar, pairs = _load_bank(root)
    result = matching_audit.audit_pairs(episodes, sidecar, pairs, assert_ok=True)
    assert result["n_pairs"] == 288
    assert result["n_declared_ambiguity_groups"] == 12
    assert result["n_undeclared_opposite_label_groups"] == 0
    assert result["n_declared_normalized_core_groups"] == 12
    assert result["n_undeclared_normalized_core_groups"] == 0
    return (
        "288/288 private pairs pass defeat-class matching; "
        "12 declared ambiguity controls and 0 undeclared twins"
    )


def check_static_filter(root: str = BANK) -> str:
    episodes, _, _ = _load_bank(root)
    kept, removed = static_filter.filter_bank(episodes)
    static_filter.assert_clean_filter(episodes, kept, removed)
    return f"{len(episodes)} -> {len(kept)}; 0 removed"


def check_sidecar_boundary(root: str = BANK) -> str:
    episodes, sidecar, _ = _load_bank(root)
    secret_names = (
        "true_type", "cue_variant", "pair_id", "defeat_class",
        "expected_stage3", "rubric_emphases", "failure_modes",
    )
    for episode in episodes:
        visible = payloads.model_visible_text(episode)
        assert episode["canary"] not in visible
        for name in secret_names:
            assert name not in visible, f"{episode['id']}: sidecar field name leaked: {name}"
        assert sidecar[episode["id"]]["pair_id"] not in visible
    return f"{len(episodes)} model payloads exclude sidecar truth and canaries"


def check_canary_registry(root: str = BANK) -> str:
    episodes, sidecar, _ = _load_bank(root)
    registry_path = os.path.join(os.path.dirname(root), "canary_registry.txt")
    assert os.path.exists(registry_path), "canary registry missing"
    with open(registry_path, encoding="utf-8") as handle:
        rows = [line.split() for line in handle if line.strip() and not line.startswith("#")]
    assert all(len(row) == 3 for row in rows), "malformed canary registry row"
    registry = {
        marker: (item_id, design) for marker, item_id, design in rows
    }
    assert len(registry) == len(rows), "duplicate registry canary"
    bank_values = [episode["canary"] for episode in episodes]
    assert len(bank_values) == len(set(bank_values))
    assert all(canary.is_wellformed(value) for value in bank_values)
    wrong_mappings = {
        episode["canary"]: {
            "registered": registry.get(episode["canary"]),
            "expected": (episode["id"], generator.DESIGN),
        }
        for episode in episodes
        if registry.get(episode["canary"])
        != (episode["id"], generator.DESIGN)
    }
    assert not wrong_mappings, f"canary registry mapping mismatch: {wrong_mappings}"
    assert all(sidecar[episode["id"]]["canary"] == episode["canary"] for episode in episodes)
    return f"{len(bank_values)} bank canaries unique, well-formed, and registered"


def check_judge_token_map(root: str = BANK) -> str:
    episodes, _, _ = _load_bank(root)
    path = os.path.join(root, "sidecar", "judge_token_map.json")
    with open(path, encoding="utf-8") as handle:
        token_map = json.load(handle)
    generator.validate_judge_token_map(episodes, token_map)
    assert len(token_map) == 684, "judge token count must be 684"
    return "684 opaque judge IDs exactly cover the three-way bank"


def check_split_hygiene(episodes: list = None,
                        root: str = BANK) -> str:
    if episodes is None:
        episodes, _, _ = _load_bank(root)
    result = split_hygiene.audit_cross_split_shingles(
        episodes, threshold=0.25
    )
    assert result["threshold"] == 0.25
    assert result["width"] == 4
    assert result["comparisons"] == 21120, (
        "cross-split shingle comparison inventory changed"
    )
    assert set(result["max_overlap"]) == {
        "public|calibration", "public|private", "calibration|private",
    }
    assert not result["violations"], (
        "cross-split shingle hygiene violations: "
        f"{result['violations'][:4]}"
    )
    assert all(
        overlap < result["threshold"]
        for overlap in result["max_overlap"].values()
    ), f"cross-split shingle overlap reached threshold: {result['max_overlap']}"
    maxima = ", ".join(
        f"{name}={value:.3f}"
        for name, value in sorted(result["max_overlap"].items())
    )
    return f"21120 cross-split comparisons pass 4-token <0.25 gate ({maxima})"


def _validate_auc_block(name: str, block: dict,
                        learned: bool = False) -> None:
    assert isinstance(block, dict), f"lexical {name} block missing"
    assert block.get("provenance") == MOCK_LABEL, (
        f"lexical {name} mock provenance mismatch"
    )
    auc = block.get("auc")
    assert (not isinstance(auc, bool) and isinstance(auc, (int, float))
            and 0.0 <= float(auc) <= OVERALL_AUC_MAX), (
        f"lexical {name} AUC {auc!r} exceeds {OVERALL_AUC_MAX}"
    )
    family_auc = block.get("family_auc")
    assert isinstance(family_auc, dict) and set(family_auc) == set(
        generator.FAMILY_CODES
    ), f"lexical {name} family AUC inventory mismatch"
    assert all(
        not isinstance(value, bool)
        and isinstance(value, (int, float))
        and 0.0 <= float(value) <= 1.0
        for value in family_auc.values()
    ), f"lexical {name} has invalid family AUC"
    observed_max = max(float(value) for value in family_auc.values())
    reported_max = block.get("max_family_auc")
    assert (not isinstance(reported_max, bool)
            and isinstance(reported_max, (int, float))
            and abs(float(reported_max) - observed_max) <= 1e-12), (
        f"lexical {name} max family AUC mismatch"
    )
    assert observed_max <= MAX_FAMILY_AUC, (
        f"lexical {name} max family AUC {observed_max} exceeds "
        f"{MAX_FAMILY_AUC}"
    )
    if learned:
        observed_macro = sum(
            float(value) for value in family_auc.values()
        ) / len(family_auc)
        reported_macro = block.get("macro_family_auc")
        assert (not isinstance(reported_macro, bool)
                and isinstance(reported_macro, (int, float))
                and abs(float(reported_macro) - observed_macro) <= 1e-12), (
            f"lexical {name} macro family AUC mismatch"
        )
        assert block.get("pooled_oof_probability_limitation") == (
            OOF_LIMITATION
        ), f"lexical {name} pooled OOF limitation changed"
    assert block.get("passed") is True, f"lexical {name} passed is not true"


def _validate_lexical_result(result: dict) -> None:
    assert isinstance(result, dict), "lexical gate result must be an object"
    assert result.get("provenance") == MOCK_LABEL, (
        "lexical gate mock provenance mismatch"
    )
    assert result.get("thresholds") == {
        "overall_auc_max": OVERALL_AUC_MAX,
        "max_family_auc": MAX_FAMILY_AUC,
    }, "lexical gate thresholds changed"
    assert result.get("counts") == {
        "total": 684,
        "public": 12,
        "calibration": 96,
        "private": 576,
    }, "lexical gate split counts changed"

    fixed = result.get("fixed_policies")
    assert isinstance(fixed, dict) and set(fixed) == set(
        EXPECTED_FIXED_POLICIES
    ), "lexical fixed-policy inventory changed"
    for name in EXPECTED_FIXED_POLICIES:
        _validate_auc_block(f"fixed_policies.{name}", fixed[name])
    for name in ("word_1_2gram", "char_3_5gram"):
        _validate_auc_block(name, result.get(name), learned=True)

    metadata = result.get("metadata")
    assert isinstance(metadata, dict), "lexical metadata block missing"
    decoders = metadata.get("decoders")
    assert isinstance(decoders, dict) and set(decoders) == set(
        EXPECTED_METADATA_DECODERS
    ), "lexical metadata-decoder inventory changed"
    for name in EXPECTED_METADATA_DECODERS:
        block = decoders[name]
        _validate_auc_block(
            f"metadata.{name}", block, learned=True
        )
        assert block.get("input_boundary") == METADATA_INPUT_BOUNDARY, (
            f"lexical metadata.{name} input boundary changed"
        )
        assert block.get("feature_names") == EXPECTED_METADATA_FEATURES[name], (
            f"lexical metadata.{name} feature inventory changed"
        )
    expected_true_type_auc = max(
        float(decoders[name]["auc"])
        for name in EXPECTED_METADATA_DECODERS
    )
    true_type_auc = metadata.get("true_type_auc")
    assert (not isinstance(true_type_auc, bool)
            and isinstance(true_type_auc, (int, float))
            and abs(float(true_type_auc) - expected_true_type_auc) <= 1e-12
            and float(true_type_auc) <= OVERALL_AUC_MAX), (
        "lexical metadata true_type AUC is inconsistent or above cap"
    )
    assert metadata.get("passed") is True, (
        "lexical metadata passed is not true"
    )
    assert result.get("passed") is True, "lexical top-level passed is not true"


def _substantive_lexical_projection(result: dict) -> dict:
    def block(value, learned=False):
        projection = {
            key: value[key]
            for key in ("provenance", "auc", "family_auc",
                        "max_family_auc", "passed")
        }
        if learned:
            projection.update({
                "macro_family_auc": value["macro_family_auc"],
                "pooled_oof_probability_limitation": value[
                    "pooled_oof_probability_limitation"
                ],
            })
        return projection

    return {
        "provenance": result["provenance"],
        "thresholds": result["thresholds"],
        "counts": result["counts"],
        "fixed_policies": {
            name: block(result["fixed_policies"][name])
            for name in EXPECTED_FIXED_POLICIES
        },
        "word_1_2gram": block(result["word_1_2gram"], learned=True),
        "char_3_5gram": block(result["char_3_5gram"], learned=True),
        "metadata": {
            "decoders": {
                name: {
                    **block(
                        result["metadata"]["decoders"][name], learned=True
                    ),
                    "input_boundary": result["metadata"]["decoders"][name][
                        "input_boundary"
                    ],
                    "feature_names": result["metadata"]["decoders"][name][
                        "feature_names"
                    ],
                }
                for name in EXPECTED_METADATA_DECODERS
            },
            "true_type_auc": result["metadata"]["true_type_auc"],
            "passed": result["metadata"]["passed"],
        },
        "passed": result["passed"],
    }


def check_lexical_gate(episodes: list = None, sidecar: dict = None,
                       root: str = BANK,
                       compare_persisted: bool = None) -> str:
    supplied = episodes is not None or sidecar is not None
    assert (episodes is None) == (sidecar is None), (
        "lexical gate requires episodes and sidecar together"
    )
    if episodes is None:
        episodes, sidecar, _ = _load_bank(root)
    if compare_persisted is None:
        compare_persisted = not supplied

    # This is intentionally recomputed. A green persisted report cannot make a
    # changed bank pass without rerunning the actual static leakage baselines.
    current = lexical_baselines.run_all(episodes, sidecar)
    _validate_lexical_result(current)

    if compare_persisted:
        report_path = os.path.join(
            root, "reports", "lexical_baseline_report.json"
        )
        with open(report_path, encoding="utf-8") as handle:
            persisted = json.load(handle)
        _validate_lexical_result(persisted)
        assert _substantive_lexical_projection(persisted) == (
            _substantive_lexical_projection(current)
        ), "persisted lexical report differs from current substantive results"
    return (
        "7 fixed policies, 2 lexical models, and 2 metadata decoders "
        "pass AUC caps"
    )


def validate_export_artifacts(export_dir: str, episodes: dict,
                              sidecar: dict) -> str:
    """Validate both persisted table formats against the frozen expectation."""
    manifest_path = os.path.join(
        export_dir, export_megamatrix.MANIFEST_FILENAME
    )
    with open(manifest_path, encoding="utf-8") as handle:
        manifest = json.load(handle)
    summary = export_megamatrix.validate_expected_manifest(
        manifest, episodes, sidecar
    )

    with open(os.path.join(export_dir, "episode_table.csv"), newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != export_megamatrix.SCHEMA:
            raise ValueError("CSV export schema mismatch")
        csv_rows = list(reader)
    with open(os.path.join(export_dir, "episode_table.jsonl"), encoding="utf-8") as handle:
        json_rows = [json.loads(line) for line in handle if line.strip()]

    export_megamatrix.validate_export_rows(
        csv_rows, episodes, sidecar, manifest, row_format="csv"
    )
    export_megamatrix.validate_export_rows(
        json_rows, episodes, sidecar, manifest, row_format="json"
    )
    canonical_csv = {
        tuple(str(row[field]) for field in export_megamatrix.SCHEMA)
        for row in csv_rows
    }
    canonical_json = {
        tuple(str(row[field]) for field in export_megamatrix.SCHEMA)
        for row in json_rows
    }
    if canonical_csv != canonical_json:
        raise ValueError("CSV and JSONL export rows disagree")
    return (
        f"{summary['n_rows']} complete rows; "
        f"{summary['n_models']} models x {summary['n_episodes']} episodes; "
        f"{summary['n_cells']} cells; {summary['n_exclusions']} exclusions"
    )


def check_export_contract(root: str = BANK) -> str:
    coverage_path = os.path.join(root, "export", "coverage_map.json")
    with open(coverage_path, encoding="utf-8") as handle:
        coverage = json.load(handle)
    assert coverage["fixed_before_pilot"] is True
    assert coverage["version"] == "v1"
    assert coverage["declared_coverage"]["mapping_status"] == "crosswalk-mapped only"
    assert coverage["episode_table_schema"] == export_megamatrix.SCHEMA
    episode_list, sidecar, _ = _load_bank(root)
    episodes = {episode["id"]: episode for episode in episode_list}
    return validate_export_artifacts(
        os.path.join(root, "export"), episodes, sidecar
    ) + "; pinned 10-field stage-4 schema"


def _count_numbered_examples(text: str, heading_pattern: str) -> dict:
    headings = list(re.finditer(heading_pattern, text, flags=re.MULTILINE))
    counts = {}
    for index, match in enumerate(headings):
        next_heading = re.search(r"^### ", text[match.end():], flags=re.MULTILINE)
        end = (match.end() + next_heading.start()) if next_heading else len(text)
        section = text[match.end():end]
        counts[match.group(1)] = len(re.findall(r"^\d+\. ", section, flags=re.MULTILINE))
    return counts


def check_judge_anchors(root: str = BANK) -> str:
    with open(os.path.join(root, "judge_anchors.md"), encoding="utf-8") as handle:
        text = handle.read()
    action = _count_numbered_examples(text, r"^### (Level [0-4]) —.*$")
    safeguard = _count_numbered_examples(text, r"^### (Safeguard [0-2]) —.*$")
    assert len(action) == 5 and set(action.values()) == {5}, f"action anchors: {action}"
    assert len(safeguard) == 3 and set(safeguard.values()) == {5}, (
        f"safeguard anchors: {safeguard}"
    )
    return "5 action levels and 3 safeguard levels, 5 exemplars each"


def check_decision_log(root: str = BANK) -> str:
    with open(os.path.join(root, "design_cells.md"), encoding="utf-8") as handle:
        text = handle.read()
    missing = [f"P3-{index:02d}" for index in range(1, 28)
               if f"P3-{index:02d}" not in text]
    assert not missing, f"missing build-time decisions: {missing}"
    return "P3-01 through P3-27 documented before pilot"


def check_mock_honesty(root: str = BANK) -> str:
    text_files = (
        "reports/pre_scale_fixture_report.md",
        "adversarial/adversarial_report.md",
        "analysis/model_spec.md",
        "README.md",
    )
    for rel in text_files:
        with open(os.path.join(root, rel), encoding="utf-8") as handle:
            text = handle.read()
        assert MOCK_LABEL in text, f"{rel}: exact mock disclaimer missing"
    with open(os.path.join(root, "export", "export_report.json"), encoding="utf-8") as handle:
        export_report = json.load(handle)
    assert export_report["provenance"] == MOCK_LABEL
    assert export_report["artifact_role"] == "complete synthetic export"
    with open(os.path.join(root, "export", export_megamatrix.MANIFEST_FILENAME), encoding="utf-8") as handle:
        manifest = json.load(handle)
    assert export_report["n_rows"] == export_report["expected_row_count"]
    assert export_report["expected_row_count"] == manifest["expected_row_count"]
    with open(os.path.join(root, "export", "scored_runs.MOCK.jsonl"), encoding="utf-8") as handle:
        records = [json.loads(line) for line in handle if line.strip()]
    assert len(records) == manifest["expected_row_count"]
    assert all(record.get("provenance") == MOCK_LABEL for record in records)
    return f"all persisted mock/synthetic outputs labeled '{MOCK_LABEL}'"


def check_scope_and_citation(root: str = BANK) -> str:
    sibling_pattern = re.compile("40-" + r"BIBLEBENCH/(?!CORINTHLOVE(?:[-/]|$))", re.IGNORECASE)
    citation_fragments = (("icmi-" + "proceedings"), ("moral " + "compactness"))
    path_hits, citation_hits = [], []
    for path in glob.glob(os.path.join(root, "**", "*"), recursive=True):
        if not os.path.isfile(path) or not re.search(r"\.(py|md|ya?ml|json|jsonl|csv|txt)$", path):
            continue
        try:
            with open(path, encoding="utf-8") as handle:
                text = handle.read()
        except UnicodeDecodeError:
            continue
        if sibling_pattern.search(text):
            path_hits.append(os.path.relpath(path, root))
        lowered = text.lower()
        if any(fragment in lowered for fragment in citation_fragments):
            citation_hits.append(os.path.relpath(path, root))
    assert not path_hits, f"out-of-scope bench path found in: {path_hits}"
    assert not citation_hits, f"prohibited citation fragment found in: {citation_hits}"
    return "scope/citation scan clean"


def check_no_live_clients(root: str = BANK) -> str:
    patterns = (
        re.compile(r"^\s*(?:from|import)\s+openai\b", re.MULTILINE),
        re.compile(r"^\s*(?:from|import)\s+anthropic\b", re.MULTILINE),
    )
    hits = []
    for path in glob.glob(os.path.join(root, "**", "*.py"), recursive=True):
        with open(path, encoding="utf-8") as handle:
            text = handle.read()
        if any(pattern.search(text) for pattern in patterns):
            hits.append(os.path.relpath(path, root))
    assert not hits, f"live model client import found: {hits}"
    return "no live model client imports"


def run(write_report: bool = True, root: str = BANK) -> dict:
    checks = [
        ("required files", lambda: check_required_files(root)),
        ("generated bank", lambda: check_generated_bank(root)),
        ("pair audit", lambda: check_pair_audit(root)),
        ("static filter", lambda: check_static_filter(root)),
        ("split hygiene", lambda: check_split_hygiene(root=root)),
        ("lexical gate", lambda: check_lexical_gate(root=root)),
        ("sidecar boundary", lambda: check_sidecar_boundary(root)),
        ("judge token map", lambda: check_judge_token_map(root)),
        ("canary registry", lambda: check_canary_registry(root)),
        ("export contract", lambda: check_export_contract(root)),
        ("judge anchors", lambda: check_judge_anchors(root)),
        ("decision log", lambda: check_decision_log(root)),
        ("mock honesty", lambda: check_mock_honesty(root)),
        ("scope and citation", lambda: check_scope_and_citation(root)),
        ("live clients", lambda: check_no_live_clients(root)),
    ]
    results = {}
    for name, check in checks:
        detail = check()
        results[name] = {"status": "PASS", "detail": detail}
    if write_report:
        lines = [
            "# CHARITROC self-check report", "",
            "Bank: 576 private + 96 calibration + 12 public = 684 episodes", "",
        ]
        for name, result in results.items():
            lines.append(f"- **{name}:** PASS — {result['detail']}")
        lines.extend(["", "SELF-CHECK: ALL PASS"])
        with open(os.path.join(root, "reports", "selfcheck_report.md"), "w", encoding="utf-8") as handle:
            handle.write("\n".join(lines) + "\n")
    return results


def main():
    results = run(write_report=True)
    for name, result in results.items():
        print(f"[PASS] {name}: {result['detail']}")
    print("\nSELF-CHECK: ALL PASS")


if __name__ == "__main__":
    main()
