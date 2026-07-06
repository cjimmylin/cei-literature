"""Load-compliance coding (R-2): FINAL LIST presence + left-rotation of [6,3,8,2,5].

Covers the four cases the review calls out (compliant / non-compliant / missing / malformed),
every left-rotation, format tolerance, and the orchestrator wiring that records `load_compliance`
for load_injected cells (and None elsewhere).
Applied per REVIEWS/20260706-fable-rulings-post-execution.md R-2.
"""
from types import SimpleNamespace

import fixtures_p0 as fx
from runner.adapters import AdapterResult, BaseAdapter
from runner.orchestrator import (
    Orchestrator,
    code_load_compliance,
    LOAD_TARGET_LIST,
    _left_rotations,
)


# --------------------------------------------------------------------------- pure function

def test_compliant_exact_target():
    r = code_load_compliance("...reasoning...\nFINAL LIST: [6, 3, 8, 2, 5]")
    assert r == {"final_list_present": True, "is_rotation": True, "compliant": True}


def test_compliant_rotated():
    # one left-rotation of [6,3,8,2,5]
    r = code_load_compliance("FINAL LIST: [8, 2, 5, 6, 3]")
    assert r["final_list_present"] and r["is_rotation"] and r["compliant"]


def test_all_left_rotations_are_compliant():
    for rot in _left_rotations(LOAD_TARGET_LIST):
        text = "FINAL LIST: " + ", ".join(str(n) for n in rot)
        r = code_load_compliance(text)
        assert r["compliant"] is True, rot


def test_non_compliant_valid_length_but_not_a_rotation():
    # present + 5 numbers, but not any cyclic shift of the target
    r = code_load_compliance("FINAL LIST: [1, 2, 3, 4, 5]")
    assert r["final_list_present"] is True
    assert r["is_rotation"] is False
    assert r["compliant"] is False


def test_non_compliant_reversed_is_not_a_left_rotation():
    # reverse of the target is not a rotation of it
    r = code_load_compliance("FINAL LIST: [5, 2, 8, 3, 6]")
    assert r["final_list_present"] is True
    assert r["compliant"] is False


def test_missing_marker():
    r = code_load_compliance("I decided to intervene. The verdict is yes, with these reasons...")
    assert r == {"final_list_present": False, "is_rotation": False, "compliant": False}


def test_missing_on_empty_and_none():
    for bad in ("", None):
        r = code_load_compliance(bad)
        assert r == {"final_list_present": False, "is_rotation": False, "compliant": False}


def test_malformed_marker_present_but_unparseable():
    r = code_load_compliance("FINAL LIST: eight, two, five, six, three")
    assert r["final_list_present"] is True
    assert r["is_rotation"] is False
    assert r["compliant"] is False


def test_malformed_wrong_count():
    r = code_load_compliance("FINAL LIST: 8, 2, 5")  # only 3 numbers
    assert r["final_list_present"] is True
    assert r["compliant"] is False


def test_format_tolerance_no_brackets_and_trailing_prose():
    r = code_load_compliance("final list 8 2 5 6 3 — done, thanks!")
    assert r["compliant"] is True


def test_format_tolerance_marker_then_newline():
    r = code_load_compliance("...\nFINAL LIST\n2 5 6 3 8")
    assert r["compliant"] is True


# --------------------------------------------------------------------------- orchestrator wiring

class _LoadAwareAdapter(BaseAdapter):
    """Returns a compliant FINAL LIST only under the load_injected prompt; else a plain verdict."""

    def __init__(self, vendor="anthropic"):
        self.vendor = vendor
        self.calls = []

    def administer(self, prompt, model_id, temperature, seed, **gen):
        self.calls.append({"prompt": prompt, "model_id": model_id, "seed": seed})
        if "Concurrent task" in prompt or "keep a running count" in prompt:
            text = f"Verdict for {model_id} seed={seed}. FINAL LIST: [8, 2, 5, 6, 3]"
        else:
            text = f"Verdict for {model_id} seed={seed}"
        return AdapterResult(text=text, raw={}, refusal_flag=False, latency=0.0)


def _bank():
    return [fx.FIXTURE_ITEM_BANK[0]]


def test_orchestrator_records_load_compliance_for_load_injected_only():
    adapters = {"anthropic": _LoadAwareAdapter("anthropic")}
    orch = Orchestrator(
        adapters=adapters,
        models=[{"id": "claude-opus-4-6", "vendor": "anthropic"}],
        item_bank=_bank(),
        conditions=["standard", "load_injected"],
        scorer=fx.fake_scorer,
        reps=3,
        temperature=0.7,
    )
    records = orch.run()

    load_recs = [r for r in records if r["resource_condition"] == "load_injected"]
    std_recs = [r for r in records if r["resource_condition"] == "standard"]
    assert load_recs and std_recs

    # load_injected cells carry a coded dict; the fake adapter returns a compliant list
    assert all(isinstance(r["load_compliance"], dict) for r in load_recs)
    assert all(r["load_compliance"]["compliant"] is True for r in load_recs)

    # non-load conditions record None (present key, filterable downstream)
    assert all("load_compliance" in r for r in std_recs)
    assert all(r["load_compliance"] is None for r in std_recs)


def test_orchestrator_flags_non_compliant_load_rep():
    class _IgnoresLoad(BaseAdapter):
        vendor = "anthropic"

        def administer(self, prompt, model_id, temperature, seed, **gen):
            return AdapterResult(
                text=f"Verdict for {model_id} seed={seed}",  # never emits FINAL LIST
                raw={}, refusal_flag=False, latency=0.0,
            )

    orch = Orchestrator(
        adapters={"anthropic": _IgnoresLoad()},
        models=[{"id": "claude-opus-4-6", "vendor": "anthropic"}],
        item_bank=_bank(),
        conditions=["load_injected"],
        scorer=fx.fake_scorer,
        reps=2,
        temperature=0.7,
    )
    records = orch.run()
    assert records
    assert all(r["load_compliance"]["final_list_present"] is False for r in records)
    assert all(r["load_compliance"]["compliant"] is False for r in records)
