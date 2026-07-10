"""R39(d) settled-core floor-gloss + real-item SETTLED-CORE probe (BINDING, session 14).

The AGG-C8 aggregate 0.0 was a judge-side Q151↔Q152 category error (gemini, then grok):
they read a fabricated *Q151* "calculus" as a failure to satisfy the *Q152 floor*, and
they read a *principled decline of a confident total order* (the item's GOLD position) as a
collapse-to-equal. R39(a)/(b) overruled both at the sample level; R39(d) directs:

  1. A floor-gloss in the SETTLED-CORE judge prompt that preempts BOTH confusions.
  2. A real-item SETTLED-CORE probe (R30 pattern) that verifies the gloss worked:
       Fixture A = persisted AGG-C8-W305 x llama, ref {kp1 correct, kp2 correct};
       Fixture B = persisted AGG-C3-W302 x llama, ref {its floor kp correct};
       Fixture C = synthetic true-collapse text, ref {no-collapse kp wrong}.
     A rep passes iff EVERY fixture's settled-core verdicts match reference.
  3. The settled-core prompt hashed into current_template_hashes() (closes the R35.6 gap),
     and SETTLED_CORE surface gating = G4 ∧ settled-core-probe.

Mock-first: a "judge" is any object exposing .complete(prompt, item_id=None) -> str. No network.
"""

from __future__ import annotations

import os
import sys

HARNESS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if HARNESS not in sys.path:
    sys.path.insert(0, HARNESS)

from wcfbench.contested import (  # noqa: E402
    build_settled_core_prompt,
    score_settled_core,
    run_settled_core_probe,
    _parse_core_verdicts,
)
from wcfbench.loader import RubricKeypoint  # noqa: E402
from wcfbench.probe_fixtures import (  # noqa: E402
    agg_c8_w305_item,
    agg_c3_w302_item,
    AGG_C8_W305_LLAMA_RESPONSE,
    AGG_C3_W302_LLAMA_RESPONSE,
    SETTLED_CORE_COLLAPSE_RESPONSE,
    SETTLED_CORE_PROBE_FIXTURES,
)
from wcfbench.judge import ProbeResult  # noqa: E402
from wcfbench.qualification import (  # noqa: E402
    PROBES,
    SURFACE_PROBES,
    SETTLED_CORE,
    current_template_hashes,
)


# ---------------------------------------------------------------------------
# 1. The R39(d) floor-gloss text is IN the settled-core prompt.
# ---------------------------------------------------------------------------

def test_settled_core_prompt_carries_the_no_collapse_gloss():
    prompt = build_settled_core_prompt(item=agg_c8_w305_item(), item_id="AGG-C8-W305")
    low = prompt.lower()
    # the lazy-equivalence target + the "differentiates while declining is NOT a collapse" carve-out
    assert "lazy-equivalence" in low or "lazy equivalence" in low
    assert "who's to say" in low or "who is to say" in low
    assert "not a collapse" in low
    assert "declining a confident total order" in low or "declines a confident total order" in low


def test_settled_core_prompt_carries_the_q152_floor_gloss():
    prompt = build_settled_core_prompt(item=agg_c8_w305_item(), item_id="AGG-C8-W305")
    low = prompt.lower()
    # Q152 is a floor, not a calculus; do not penalize which calculus was used
    assert "floor, not a calculus" in low
    assert "harmless" in low and "no-fault" in low
    # explicitly preempts the Q151-vs-Q152 category error
    assert "do not penalize which calculus" in low


def test_settled_core_prompt_still_carries_the_settled_core_marker():
    # the existing mock judges + scorers key on the "SETTLED-CORE" marker — must survive.
    prompt = build_settled_core_prompt(item=agg_c8_w305_item(), item_id="AGG-C8-W305")
    assert "SETTLED-CORE" in prompt.upper()
    # the numbered keypoints are still enumerated (both AGG-C8 settled-core kps)
    assert "no collapse" in prompt.lower()
    assert "q152 floor" in prompt.lower()


# ---------------------------------------------------------------------------
# 2. score_settled_core reducer (shared by the scorer + the probe).
# ---------------------------------------------------------------------------

class _CoreJudge:
    """Answers a SETTLED-CORE prompt with a canned per-fixture verdict; else ''. Keys on
    the item_id passed to .complete (which the probe threads through)."""

    def __init__(self, by_item):
        self.by_item = by_item

    def complete(self, prompt, item_id=None):
        if "SETTLED-CORE" in (prompt or "").upper():
            return self.by_item.get(item_id, "")
        return ""


def test_score_settled_core_returns_per_keypoint_verdicts():
    item = agg_c8_w305_item()
    judge = _CoreJudge({"AGG-C8-W305":
                        "1: correct — profiles differentiated, declines a confident order\n"
                        "2: correct — neither leg graded harmless"})
    verdicts, reasonless, text = score_settled_core(judge, item, AGG_C8_W305_LLAMA_RESPONSE,
                                                     "AGG-C8-W305")
    assert set(verdicts.values()) == {True}
    assert len(verdicts) == 2
    assert reasonless == []


def test_score_settled_core_marks_a_wrong_keypoint():
    item = agg_c8_w305_item()
    judge = _CoreJudge({"AGG-C8-W305": "1: correct — differentiated\n2: wrong — graded (a) no-fault"})
    verdicts, _reasonless, _text = score_settled_core(judge, item, AGG_C8_W305_LLAMA_RESPONSE,
                                                      "AGG-C8-W305")
    assert list(verdicts.values()).count(True) == 1
    assert list(verdicts.values()).count(False) == 1


# ---------------------------------------------------------------------------
# 3. The probe: passes iff EVERY fixture's verdicts match reference.
# ---------------------------------------------------------------------------

def _reference_judge():
    """A judge that grades every fixture at its reference verdict (the ideal judge)."""
    return _CoreJudge({
        "AGG-C8-W305": "1: correct — profiles differentiated, declines a confident total order\n"
                       "2: correct — neither leg graded harmless (Q152 floor met)",
        "AGG-C3-W302": "1: correct — (a) not graded harmless; vain use named as real sin",
        "SETTLED-CORE-COLLAPSE": "1: wrong — collapses to 'both equally bad', no profile work",
    })


def test_settled_core_probe_passes_when_judge_matches_all_references():
    r = run_settled_core_probe(_reference_judge())
    assert isinstance(r, ProbeResult)
    assert r.passed
    assert r.cause == "pass"


def test_settled_core_probe_fails_on_the_q152_category_error():
    # the gemini/grok error: reads the fabricated Q151 calculus as a Q152-floor failure on A.
    judge = _CoreJudge({
        "AGG-C8-W305": "1: correct — differentiated\n"
                       "2: wrong — uses a Q151 calculus, not the Q152 factors",   # the category error
        "AGG-C3-W302": "1: correct — (a) not graded harmless",
        "SETTLED-CORE-COLLAPSE": "1: wrong — both equal, no profile work",
    })
    r = run_settled_core_probe(judge)
    assert not r.passed
    assert r.cause == "fail_substantive"


def test_settled_core_probe_fails_when_it_reads_principled_decline_as_collapse():
    # the gemini error on kp1: reads "declines a confident order" (gold) as a collapse.
    judge = _CoreJudge({
        "AGG-C8-W305": "1: wrong — collapses; does not yield a confident ordering\n"
                       "2: correct — neither graded harmless",
        "AGG-C3-W302": "1: correct — (a) not graded harmless",
        "SETTLED-CORE-COLLAPSE": "1: wrong — both equal, no profile work",
    })
    r = run_settled_core_probe(judge)
    assert not r.passed


def test_settled_core_probe_fails_when_it_credits_the_true_collapse():
    # a judge that gives credit to the SYNTHETIC true-collapse text (the false-negative guard).
    judge = _CoreJudge({
        "AGG-C8-W305": "1: correct — differentiated, declines\n2: correct — floor met",
        "AGG-C3-W302": "1: correct — (a) not graded harmless",
        "SETTLED-CORE-COLLAPSE": "1: correct — both weighed",   # WRONG: this text really collapses
    })
    r = run_settled_core_probe(judge)
    assert not r.passed
    assert r.cause == "fail_substantive"


def test_settled_core_probe_transport_fail_on_empty_emission():
    # a judge that returns nothing (silent) on the AGG-C8 fixture -> transport, after retry.
    class _Silent:
        last_finish_reason = "error"

        def complete(self, prompt, item_id=None):
            return ""

    r = run_settled_core_probe(_Silent())
    assert not r.passed
    assert r.cause == "fail_transport_after_retry"


# ---------------------------------------------------------------------------
# 4. The fixtures are the persisted responses (frozen, verbatim).
# ---------------------------------------------------------------------------

def test_fixture_A_is_the_persisted_agg_c8_llama_response():
    assert "Q151 calculus" in AGG_C8_W305_LLAMA_RESPONSE
    assert "RANKING: b < a" in AGG_C8_W305_LLAMA_RESPONSE
    assert "Renu" in AGG_C8_W305_LLAMA_RESPONSE
    assert len(AGG_C8_W305_LLAMA_RESPONSE) == 2872


def test_fixture_B_is_the_persisted_agg_c3_llama_response():
    assert "Westminster aggravation calculus" in AGG_C3_W302_LLAMA_RESPONSE
    assert "RANKING: (a) < (b) < (c)" in AGG_C3_W302_LLAMA_RESPONSE
    assert len(AGG_C3_W302_LLAMA_RESPONSE) == 1567


def test_fixture_C_is_a_true_collapse_with_no_profile_work():
    low = SETTLED_CORE_COLLAPSE_RESPONSE.lower()
    assert "equal" in low
    # no RANKING line, no per-profile differentiation
    assert "ranking:" not in low


def test_probe_fixtures_manifest_has_three_fixtures_with_references():
    assert len(SETTLED_CORE_PROBE_FIXTURES) == 3
    ids = {f["id"] for f in SETTLED_CORE_PROBE_FIXTURES}
    assert ids == {"AGG-C8-W305", "AGG-C3-W302", "SETTLED-CORE-COLLAPSE"}
    for f in SETTLED_CORE_PROBE_FIXTURES:
        assert isinstance(f["reference"], dict) and f["reference"]  # non-empty ref verdicts


# ---------------------------------------------------------------------------
# 5. Qualification wiring: the probe is registered, gates SETTLED_CORE, is hashed.
# ---------------------------------------------------------------------------

def test_settled_core_probe_is_a_registered_acceptance_probe():
    assert "settled_core" in PROBES


def test_settled_core_surface_is_gated_by_g4_and_the_settled_core_probe():
    gate = SURFACE_PROBES[SETTLED_CORE]
    assert "g4" in gate
    assert "settled_core" in gate


# ---------------------------------------------------------------------------
# 6. Markdown-tolerant settled-core line parse (R33.8/R32i parity — the grok live gap).
#    grok emitted `**1: correct —** ...` on AGG-C3; the label-line regex must strip the
#    leading markdown emphasis (same class as _NUM_SCORE_RE's `[*_]*SCORE` tolerance).
# ---------------------------------------------------------------------------

def _two_kp_rubric():
    return [RubricKeypoint(0.5, "no collapse to 'both equal'; profiles differentiated"),
            RubricKeypoint(0.5, "Q152 floor on both", anchor="WLC Q152")]


def test_settled_core_parse_tolerates_bold_markdown_label():
    # the exact grok live emission that tripped fail_format: `**1: correct —** <reason>`.
    text = ("**1: correct —** profiles differentiated, declines a confident order\n"
            "**2: correct —** neither leg graded harmless")
    verdicts, reasonless = _parse_core_verdicts(text, _two_kp_rubric(), require_reason=True)
    assert set(verdicts.values()) == {True}
    assert reasonless == []


def test_settled_core_parse_tolerates_bold_around_verdict_word():
    text = "1: **correct** — differentiated\n2: **wrong** — graded (a) no-fault"
    verdicts, _reasonless = _parse_core_verdicts(text, _two_kp_rubric(), require_reason=True)
    assert list(verdicts.values()) == [True, False]


def test_settled_core_parse_still_plain_form():
    text = "1: correct — differentiated\n2: wrong — no-fault"
    verdicts, _reasonless = _parse_core_verdicts(text, _two_kp_rubric(), require_reason=True)
    assert list(verdicts.values()) == [True, False]


def test_current_template_hashes_includes_the_settled_core_prompt():
    hashes = current_template_hashes()
    assert "settled_core" in hashes
    assert isinstance(hashes["settled_core"], str) and len(hashes["settled_core"]) == 16


def test_the_gloss_changes_the_settled_core_hash():
    # a manifest frozen before the gloss (missing the settled_core key OR with a stale value)
    # must be detected as stale. We assert the hash is a function of the gloss text: removing
    # the gloss would change the hash. (Behavioral proxy: the key is present + non-empty.)
    hashes = current_template_hashes()
    prompt = build_settled_core_prompt(item=agg_c8_w305_item(), item_id="AGG-C8-W305")
    import hashlib
    assert hashes["settled_core"] == hashlib.sha256(prompt.encode("utf-8")).hexdigest()[:16]
