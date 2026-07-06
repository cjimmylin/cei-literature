"""Leakage (B1/B2), canary (B3), scope & citation (D4) checks over the SHIPPED bank."""
import json
import os
import re

import yaml

import generator as gen
from lib import canary as canary_mod

BANK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _visible_text(episode):
    """Everything the evaluated model can see = the rendered multiturn_script."""
    return "\n".join(episode["multiturn_script"].values())


def test_hidden_labels_not_leaked():
    """B2: dose codes, validity words, cell labels, and canary never appear in
    candidate-visible text."""
    eps, side, _, _, _ = gen.generate(20260706)
    secret_tokens = ["d0", "d1", "d2", "d3", "d4", "d5",
                     "valid", "invalid", "servility", "dogmatism", "sycophan",
                     "discernment", "10CB2-"]
    for e in eps:
        vis = _visible_text(e).lower()
        for tok in secret_tokens:
            assert tok.lower() not in vis, f"{e['id']}: secret '{tok}' leaked into prompt"
        # canary must not appear
        assert e["canary"].lower() not in vis, f"{e['id']}: canary leaked"


def test_no_telegraphing_expected_behavior():
    """B1: item-visible text must not narrate the expected behaviour or name the
    vice. expected_behavior is identical/generic across items (not per-item)."""
    eps, _, _, _, _ = gen.generate(20260706)
    exp = {e["expected_behavior"] for e in eps}
    assert len(exp) == 1, "expected_behavior must be generic (identical) across items"
    banned = ["should resist", "should update", "should flip", "correct answer is",
              "the vice", "sycophan", "dogmatis", "you are being tested"]
    for e in eps:
        vis = _visible_text(e).lower()
        for b in banned:
            assert b not in vis, f"{e['id']}: telegraph '{b}'"


def test_canary_wellformed_unique():
    eps, side, _, _, _ = gen.generate(20260706)
    cns = [e["canary"] for e in eps]
    assert all(canary_mod.is_wellformed(c) for c in cns)
    assert len(cns) == len(set(cns))
    # sidecar canary matches item canary
    for e in eps:
        assert side[e["id"]]["canary"] == e["canary"]


def test_canary_registry_present():
    reg = os.path.join(BANK, "canary_registry.txt")
    # registry is written one level up (BANKS/canary_registry.txt)
    reg = os.path.join(os.path.dirname(BANK), "canary_registry.txt")
    assert os.path.exists(reg), "canary_registry.txt missing"
    with open(reg) as f:
        lines = [l for l in f if l.strip() and not l.startswith("#")]
    regged = {l.split()[0] for l in lines}
    # every shipped canary from the current seed must be registered
    with open(os.path.join(BANK, "seeds_public.yaml")) as f:
        pub = yaml.safe_load(f)
    with open(os.path.join(BANK, "episodes", "private_bank.yaml")) as f:
        priv = yaml.safe_load(f)
    for e in pub + priv:
        assert e["canary"] in regged, f"{e['id']} canary not in registry"
    # format check
    for c in regged:
        assert canary_mod.is_wellformed(c), f"malformed registry canary {c}"


def test_scope_and_citation_bans():
    """D4: no sibling-bench references, no icmi 'moral compactness' citation."""
    # sibling BENCHES under 40-BIBLEBENCH (NOT CORINTHLOVE*) + the citation ban.
    # CROSSROADS/MANYMIRRORS/AGAPEGAME/WITNESS/CHARITROC are CORINTHLOVE designs
    # (in-scope) and are deliberately NOT forbidden.
    forbidden = re.compile(
        r"icmi-proceedings|moral compactness|"
        r"ARMOURBENCH|FRUITBENCH|SERMONMOUNT|SOLABENCH|TENCOMMANDMENTS|WESTMINSTER",
        re.IGNORECASE)
    # scan shipped artifacts (data files only; prose docs scanned separately in CI)
    for rel in ("seeds_public.yaml", "episodes/private_bank.yaml"):
        with open(os.path.join(BANK, rel)) as f:
            txt = f.read()
        m = forbidden.search(txt)
        assert not m, f"forbidden reference in {rel}: {m.group(0)}"


def test_sidecar_leakcheck_block():
    """The generator-declared hidden_labels values (short label tokens) are
    absent from visible text — belt-and-suspenders over test_hidden_labels."""
    eps, side, _, _, _ = gen.generate(20260706)
    for e in eps[:300]:
        vis = _visible_text(e).lower()
        hl = side[e["id"]]["hidden_labels"]
        for r in ("round_1", "round_2"):
            rr = hl.get(r)
            if rr:
                assert rr["dose"] not in vis
                assert rr["validity"] not in vis
