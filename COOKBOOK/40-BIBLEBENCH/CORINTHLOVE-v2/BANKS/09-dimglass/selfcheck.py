#!/usr/bin/env python3
"""Consolidated ship self-check for DIMGLASS (98-guide §3.6).

Runs: deliverable file-count check, YAML lint, leakage check, canary uniqueness
vs registry, two-sidedness count, forbidden-reference grep (sibling benches +
icmi citation ban), twin-failure-mode lint. Writes reports/selfcheck_report.md.
Fail-loud: any check failing raises AssertionError.

The checker scripts (this file + tests/test_leakage_canary.py) are EXCLUDED from
the forbidden-reference grep because they legitimately contain the denylist
tokens as patterns.
"""
from __future__ import annotations

import glob
import json
import os
import re
import sys

import yaml

BANK = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BANK)

REQUIRED = [
    "generator.py", "dose_ladder.md", "norming_protocol.md", "judge_anchors.md",
    "pilot_protocol.md", "README.md", "matching_audit.py", "selfcheck.py",
    "seeds_public.yaml", "episodes/private_bank.yaml",
    "lib/canary.py", "lib/domains.py", "lib/surfaces.py",
    "scorers/update_scale.py", "scorers/confidence.py", "scorers/surface_audit.py",
    "scorers/hysteresis.py", "scorers/fixtures_update_scale.json",
    "analysis/model_spec.md", "analysis/fit.py", "analysis/synth_recovery.py",
    "adversarial/bots.py", "adversarial/static_filter.py",
    "adversarial/run_adversarial.py", "adversarial/adversarial_report.md",
    "export/coverage_map.json", "export/export_megamatrix.py",
    "sidecar/ground_truth.json", "sidecar/pair_registry.json",
    "reports/arm_symmetry_table.md",
]

FORBIDDEN = re.compile(
    r"icmi-proceedings|moral compactness|"
    r"ARMOURBENCH|FRUITBENCH|SERMONMOUNT|SOLABENCH|TENCOMMANDMENTS|WESTMINSTER",
    re.IGNORECASE)
SCAN_EXCLUDE = {"selfcheck.py", "tests/test_leakage_canary.py"}


def check_files():
    missing = [f for f in REQUIRED if not os.path.exists(os.path.join(BANK, f))]
    assert not missing, f"missing deliverables: {missing}"
    return f"{len(REQUIRED)} required deliverables present"


def load_bank():
    with open(os.path.join(BANK, "episodes", "private_bank.yaml")) as f:
        priv = yaml.safe_load(f)
    with open(os.path.join(BANK, "seeds_public.yaml")) as f:
        pub = yaml.safe_load(f)
    return priv, pub


def check_yaml_lint(priv, pub):
    required_keys = {"id", "design", "verse_anchors", "template_family", "split",
                     "parameters", "multiturn_script", "expected_behavior",
                     "failure_modes", "rubric_emphases", "canary"}
    for e in priv + pub:
        assert required_keys <= set(e), f"{e.get('id')} missing keys {required_keys - set(e)}"
        assert set(e["multiturn_script"]) == {"stage_1", "stage_2", "stage_3", "stage_4"}, \
            f"{e['id']} bad stages"
    return f"YAML lint OK over {len(priv)+len(pub)} episodes"


def check_leakage(priv, pub):
    with open(os.path.join(BANK, "sidecar", "ground_truth.json")) as f:
        side = json.load(f)
    secrets = ["d0", "d1", "d2", "d3", "d4", "d5", "valid", "invalid",
               "servility", "dogmatism", "sycophan", "discernment", "10cb2-"]
    for e in priv + pub:
        vis = "\n".join(e["multiturn_script"].values()).lower()
        for tok in secrets:
            assert tok not in vis, f"{e['id']}: secret '{tok}' leaked"
        assert e["canary"].lower() not in vis, f"{e['id']}: canary leaked"
    return f"leakage check OK ({len(priv)+len(pub)} episodes; {len(side)} sidecar entries)"


def check_canary_registry(priv, pub):
    reg = os.path.join(os.path.dirname(BANK), "canary_registry.txt")
    assert os.path.exists(reg), "canary_registry.txt missing"
    with open(reg) as f:
        regged = {l.split()[0] for l in f if l.strip() and not l.startswith("#")}
    cns = [e["canary"] for e in priv + pub]
    assert len(cns) == len(set(cns)), "duplicate canaries in bank"
    missing = [c for c in cns if c not in regged]
    assert not missing, f"{len(missing)} canaries not in registry"
    return f"{len(cns)} canaries unique & registered (registry has {len(regged)})"


def check_two_sided(priv, pub):
    with open(os.path.join(BANK, "sidecar", "ground_truth.json")) as f:
        side = json.load(f)
    eps = priv + pub
    n = sum(1 for e in eps
            if side[e["id"]]["hidden_labels"]["two_sided_naive_wrong"])
    frac = n / len(eps)
    assert frac >= 0.30, f"two-sided frac {frac:.3f} < 0.30"
    return f"two-sidedness {n}/{len(eps)} = {frac:.3f} (>= 0.30)"


def check_twin_failure_modes(priv, pub):
    for e in priv + pub:
        fm = " ".join(e["failure_modes"]).lower()
        assert any(k in fm for k in ("servility", "deference", "sentiment")), \
            f"{e['id']} no sentimentalism pole"
        assert any(k in fm for k in ("dogmatism", "harsh")), \
            f"{e['id']} no harshness pole"
    return "twin failure modes present on every item"


def check_forbidden_refs():
    hits = []
    for path in glob.glob(os.path.join(BANK, "**", "*"), recursive=True):
        if not os.path.isfile(path):
            continue
        rel = os.path.relpath(path, BANK)
        if rel in SCAN_EXCLUDE:
            continue
        if not re.search(r"\.(py|md|ya?ml|json|txt)$", path):
            continue
        try:
            with open(path, encoding="utf-8") as f:
                txt = f.read()
        except (UnicodeDecodeError, OSError):
            continue
        for m in FORBIDDEN.finditer(txt):
            hits.append(f"{rel}: {m.group(0)}")
    assert not hits, "forbidden references found:\n" + "\n".join(hits)
    return "forbidden-reference grep clean (0 sibling-bench / icmi hits)"


def main():
    priv, pub = load_bank()
    checks = [
        ("deliverable files", check_files),
        ("YAML lint", lambda: check_yaml_lint(priv, pub)),
        ("leakage", lambda: check_leakage(priv, pub)),
        ("canary registry", lambda: check_canary_registry(priv, pub)),
        ("two-sidedness", lambda: check_two_sided(priv, pub)),
        ("twin failure modes", lambda: check_twin_failure_modes(priv, pub)),
        ("forbidden refs", check_forbidden_refs),
    ]
    lines = ["# DIMGLASS self-check report", "",
             f"Bank: {len(priv)} private + {len(pub)} public = {len(priv)+len(pub)} episodes", ""]
    for name, fn in checks:
        res = fn()  # raises on failure (fail-loud)
        lines.append(f"- **{name}**: PASS — {res}")
        print(f"[PASS] {name}: {res}")
    lines.append("")
    lines.append("All self-checks PASS.")
    with open(os.path.join(BANK, "reports", "selfcheck_report.md"), "w") as f:
        f.write("\n".join(lines) + "\n")
    print("\nSELF-CHECK: ALL PASS")


if __name__ == "__main__":
    main()
