"""Qualification manifest — the frozen R35.4 artifact JudgePanel consumes.

Qualification is an artifact, not a side effect: the K=8 run's slugs + template hashes +
per-probe pass table + eligible-surface sets are frozen to a dated manifest. Surface
eligibility is FROZEN to that manifest; re-qualification is required only on a slug change, a
relevant template-hash change, or a binding-memo order — so the run-to-run gate flip session
11 observed cannot recur. This module tests the manifest's build / round-trip / freshness.

NO network; the judges are canned fakes.
"""

from __future__ import annotations

import json
import os
import sys

HARNESS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if HARNESS not in sys.path:
    sys.path.insert(0, HARNESS)

from wcfbench.qualification import (  # noqa: E402
    qualify_judge,
    build_manifest,
    manifest_from_pass_table,
    write_manifest,
    load_manifest,
    current_template_hashes,
    manifest_is_fresh,
    eligible_surfaces_for,
    OPEN_AWARD,
    DISCLOSURE,
    COHERENCE,
    SETTLED_CORE,
)
from test_qualification import BatteryJudge  # noqa: E402


def _quals():
    return [
        qualify_judge(BatteryJudge(), name="gemini", family="google", slug="google/gemini-2.5-flash"),
        qualify_judge(BatteryJudge(disc_reps_fail=8, neg=True), name="gpt", family="openai",
                      slug="openai/gpt-4o-mini"),   # discrimination 0/8 -> OPEN_AWARD out
    ]


def _manifest(**kw):
    return build_manifest(_quals(), run_dir="07-PILOTS/20260710-probe-stability-k8",
                          timestamp="2026-07-10T12:00:00", memo="R34-R37", **kw)


def test_manifest_records_slugs_and_eligible_surfaces():
    m = _manifest()
    by_slug = {j["slug"]: j for j in m["judges"]}
    assert set(by_slug["google/gemini-2.5-flash"]["eligible_surfaces"]) == {
        OPEN_AWARD, DISCLOSURE, COHERENCE, SETTLED_CORE}
    assert OPEN_AWARD not in by_slug["openai/gpt-4o-mini"]["eligible_surfaces"]
    assert {COHERENCE, SETTLED_CORE, DISCLOSURE} <= set(by_slug["openai/gpt-4o-mini"]["eligible_surfaces"])


def test_manifest_records_per_probe_pass_table():
    m = _manifest()
    gpt = next(j for j in m["judges"] if j["slug"] == "openai/gpt-4o-mini")
    assert gpt["probe_pass"]["discrimination"] == {"n_pass": 0, "k": 8}
    assert gpt["probe_pass"]["g4"] == {"n_pass": 8, "k": 8}


def test_manifest_carries_current_template_hashes():
    m = _manifest()
    assert m["template_hashes"] == current_template_hashes()
    assert m["k"] == 8 and m["threshold"] == 5
    assert m["memo"] == "R34-R37"
    assert m["canary"] == "WCFBENCH-CANARY-c1647-x9k4q"


def test_manifest_round_trip(tmp_path):
    m = _manifest()
    path = os.path.join(tmp_path, "manifest.json")
    write_manifest(path, m)
    loaded = load_manifest(path)
    assert loaded == m
    # and it is valid JSON on disk
    with open(path) as fh:
        assert json.load(fh) == m


def test_manifest_is_fresh_when_template_hashes_match():
    assert manifest_is_fresh(_manifest()) is True


def test_manifest_is_stale_when_a_template_hash_differs():
    m = _manifest()
    m["template_hashes"]["disclosure"] = "deadbeefdeadbeef"     # simulate a prompt-template change
    assert manifest_is_fresh(m) is False


def test_manifest_from_pass_table_reproduces_memo_r356_eligibility():
    # The memo sec0 K=8 pass table -> R35.6 frozen eligibility, via the same >=5/8 gate.
    rows = [
        {"name": "gemini-flash", "family": "google", "slug": "google/gemini-2.5-flash",
         "pass_counts": {"g4": 8, "award_consistency": 5, "discrimination": 6,
                         "disclosure_inversion": 8, "negative_disclosure": 8}},
        {"name": "gpt4omini", "family": "openai", "slug": "openai/gpt-4o-mini",
         "pass_counts": {"g4": 8, "award_consistency": 2, "discrimination": 0,
                         "disclosure_inversion": 8, "negative_disclosure": 0}},
        {"name": "mistral-small", "family": "mistral", "slug": "mistralai/mistral-small-3.2-24b-instruct",
         "pass_counts": {"g4": 0, "award_consistency": 2, "discrimination": 0,
                         "disclosure_inversion": 0, "negative_disclosure": 0}},
    ]
    m = manifest_from_pass_table(rows, run_dir="07-PILOTS/20260710-probe-stability",
                                 timestamp="2026-07-10T08:32:00", memo="R34-R37", k=8, threshold=5)
    by_slug = {j["slug"]: set(j["eligible_surfaces"]) for j in m["judges"]}
    assert by_slug["google/gemini-2.5-flash"] == {OPEN_AWARD, DISCLOSURE, COHERENCE, SETTLED_CORE}
    assert by_slug["openai/gpt-4o-mini"] == {COHERENCE, SETTLED_CORE}
    assert by_slug["mistralai/mistral-small-3.2-24b-instruct"] == set()      # discarded
    assert manifest_is_fresh(m) is True


def test_eligible_surfaces_for_reads_a_slug():
    m = _manifest()
    assert eligible_surfaces_for(m, "google/gemini-2.5-flash") == {
        OPEN_AWARD, DISCLOSURE, COHERENCE, SETTLED_CORE}
    # an unknown slug is not in the manifest -> None (caller must re-qualify / discard)
    assert eligible_surfaces_for(m, "cohere/command-r") is None
