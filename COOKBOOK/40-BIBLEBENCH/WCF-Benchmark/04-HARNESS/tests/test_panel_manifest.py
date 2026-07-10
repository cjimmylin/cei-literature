"""JudgePanel consumes a qualification manifest — memo R35.4 (session 12).

Panel construction must NOT silently re-derive surface eligibility per run (the run-to-run
gate flip session 11 observed). When given a manifest, the panel reads each judge's
eligible-surface set FROM the frozen manifest (matched by slug), runs NO probes at
construction, discards a judge absent from the manifest, and refuses a manifest whose
template hashes have drifted (re-qualification required).

NO network; the "clients" here raise if asked to grade — proving the manifest path never
calls a probe at construction.
"""

from __future__ import annotations

import os
import sys

import pytest

HARNESS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if HARNESS not in sys.path:
    sys.path.insert(0, HARNESS)

from wcfbench.judge import JudgeError  # noqa: E402
from wcfbench.qualification import (  # noqa: E402
    qualify_judge, build_manifest, OPEN_AWARD, DISCLOSURE, COHERENCE, SETTLED_CORE,
)
from wcfbench.judge_panel import JudgePanel  # noqa: E402
from test_qualification import BatteryJudge  # noqa: E402


class RaisingClient:
    """A client that raises if ``.complete`` is ever called — proves the manifest path runs
    no probes at construction. (It is never asked to score in these tests.)"""

    def complete(self, prompt, item_id=None):
        raise AssertionError("manifest path must not call .complete at construction")


def _manifest(template_hashes=None):
    quals = [
        qualify_judge(BatteryJudge(), name="gemini", family="google", slug="google/gemini-2.5-flash"),
        qualify_judge(BatteryJudge(disc_reps_fail=8), name="gpt", family="openai",
                      slug="openai/gpt-4o-mini"),   # discrimination 0/8 -> OPEN_AWARD out
    ]
    return build_manifest(quals, run_dir="rundir", timestamp="2026-07-10T12:00:00",
                          memo="R34-R37", template_hashes=template_hashes)


def _judges():
    return [
        {"name": "gemini", "family": "google", "slug": "google/gemini-2.5-flash", "client": RaisingClient()},
        {"name": "gpt", "family": "openai", "slug": "openai/gpt-4o-mini", "client": RaisingClient()},
    ]


def test_panel_reads_eligibility_from_manifest_without_running_probes():
    panel = JudgePanel(_judges(), manifest=_manifest())
    assert panel.eligible["gemini"] == {OPEN_AWARD, DISCLOSURE, COHERENCE, SETTLED_CORE}
    assert OPEN_AWARD not in panel.eligible["gpt"]
    assert {COHERENCE, SETTLED_CORE, DISCLOSURE} <= panel.eligible["gpt"]


def test_panel_surfaces_a_manifest_suspension_in_discarded():
    panel = JudgePanel(_judges(), manifest=_manifest())
    assert any(n == "gpt" and OPEN_AWARD in reason for n, reason in panel.discarded)


def test_panel_discards_judge_absent_from_manifest():
    judges = _judges() + [
        {"name": "mystery", "family": "cohere", "slug": "cohere/command-r", "client": RaisingClient()}]
    panel = JudgePanel(judges, manifest=_manifest())
    assert "mystery" not in panel.eligible
    assert "mystery" not in {n for n, _, _ in panel.active}
    assert any(n == "mystery" and "manifest" in reason.lower() for n, reason in panel.discarded)


def test_panel_refuses_stale_manifest():
    stale = _manifest()
    stale["template_hashes"]["disclosure"] = "deadbeefdeadbeef"     # a prompt-template drift
    with pytest.raises(JudgeError):
        JudgePanel(_judges(), manifest=stale)


def test_panel_manifest_still_enforces_two_cross_family():
    # only one judge is in the manifest -> after discard, not two families -> unusable.
    one = [{"name": "gemini", "family": "google", "slug": "google/gemini-2.5-flash", "client": RaisingClient()},
           {"name": "solo", "family": "meta", "slug": "meta/llama", "client": RaisingClient()}]
    with pytest.raises(JudgeError):
        JudgePanel(one, manifest=_manifest())
