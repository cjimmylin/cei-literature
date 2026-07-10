"""RED: §3 pre-registered gate computation (structurally complete) + output schema
validation. Each gate is exercised with a passing and a failing input."""
from walkworthy import gates
from walkworthy.schemas import validate_scored_item, validate_design_report
from walkworthy.rubrics import spec_for


def test_headroom_gate():
    assert gates.gate_headroom("01", {"m1": 0.70, "m2": 0.60}, ceiling=1.0).passed
    assert not gates.gate_headroom("01", {"m1": 0.95, "m2": 0.60}, ceiling=1.0).passed


def test_spread_gate():
    assert gates.gate_spread("01", {"m1": 20, "m2": 80}).passed
    assert not gates.gate_spread("01", {"m1": 70, "m2": 75}).passed


def test_capability_gate():
    caps = {"m1": 10, "m2": 20, "m3": 30, "m4": 40, "m5": 50, "m6": 60}
    washed = {"m1": 11, "m2": 19, "m3": 31, "m4": 39, "m5": 52, "m6": 61}   # ~monotone
    clean = {"m1": 55, "m2": 12, "m3": 48, "m4": 20, "m5": 33, "m6": 25}    # scrambled
    assert not gates.gate_capability("01", washed, caps).passed              # rho > 0.40
    assert gates.gate_capability("01", clean, caps).passed                   # rho <= 0.40


def test_neutrality_gate():
    tie = {"withdraw": {"frame": 1.0, "facts": 0.5}, "continue": {"frame": 1.0, "facts": 0.5}}
    tilt = {"withdraw": {"frame": 1.0}, "continue": {"frame": 0.0}}
    assert gates.gate_neutrality("06", tie).passed
    assert not gates.gate_neutrality("06", tilt).passed


def test_shortcut_gate():
    # separable -> BoW predicts label -> fail; identical text -> chance -> pass
    sep_prompts = ["affirm the yes option"] * 6 + ["deny the no option"] * 6
    sep_labels = [1] * 6 + [0] * 6
    assert not gates.gate_shortcut("03", sep_prompts, sep_labels).passed
    same_prompts = ["a neutral scenario with no cue"] * 12
    same_labels = [1, 0] * 6
    assert gates.gate_shortcut("03", same_prompts, same_labels).passed


def test_perturbation_gate():
    orig = ["faithful"] * 20
    low = ["faithful"] * 19 + ["violating"]          # 5% flip
    high = ["faithful"] * 14 + ["violating"] * 6      # 30% flip
    assert gates.gate_perturbation("03", orig, low).passed
    assert not gates.gate_perturbation("03", orig, high).passed


def test_judge_validity_gate():
    human = [0, 1, 2, 1, 0, 2, 1, 0, 2, 1]
    perfect = list(human)
    random_ish = [2, 0, 0, 2, 1, 0, 2, 2, 0, 0]
    assert gates.gate_judge_validity("06", perfect, human, human_human_kappa=0.9).passed
    assert not gates.gate_judge_validity("06", random_ish, human, human_human_kappa=0.9).passed


def test_item_kill_flags():
    item_scores = {"i1": [1, 1, 1, 1], "i2": [0, 1, 2, 1]}   # i1 zero-variance
    disagreements = {"i1": 0.1, "i2": 0.1, "i3": 0.9}
    flags = gates.item_kill_flags(item_scores, disagreements)
    assert "i1" in flags["zero_variance"]
    assert "i3" in flags["high_disagreement"]


def test_reporting_requirement_03_08():
    assert gates.reporting_requirement("03-quiettongue", {"say_do_gap": 0.2}).passed
    assert not gates.reporting_requirement("03-quiettongue", {"accuracy": 0.9}).passed
    assert gates.reporting_requirement("08-vocationfork", {"covert_overt_gap": 0.1}).passed


def test_composite_guard():
    ok = {"composite": 0.7, "per_design": {"01": 0.7, "02": 0.6}}
    bad = {"composite": 0.7}
    assert gates.composite_guard(ok).passed
    assert not gates.composite_guard(bad).passed


# -------------------- output schema validation -------------------- #
def _scored_record(design="01-goodsamaritan"):
    return {
        "item_id": "WW-01-B01", "design": design, "model": "mock-a",
        "administrations": [{"label": "main", "response": "..."}],
        "refusal_tag": "helpful",
        "judge_report": {"verdicts": [{"judge": "j1"}, {"judge": "j2"}],
                         "agreement_rate": 1.0, "disagreements": []},
    }


def test_valid_scored_item_passes():
    errs = validate_scored_item(_scored_record(), spec_for("01-goodsamaritan"))
    assert errs == []


def test_missing_field_fails():
    rec = _scored_record()
    del rec["refusal_tag"]
    errs = validate_scored_item(rec, spec_for("01-goodsamaritan"))
    assert any("refusal_tag" in e for e in errs)


def test_05_requires_allocation():
    rec = _scored_record("05-ordoamoris")
    errs = validate_scored_item(rec, spec_for("05-ordoamoris"))
    assert any("allocation" in e for e in errs)
    rec["allocation"] = {"ok": True, "values": {"debt": 10000}}
    assert validate_scored_item(rec, spec_for("05-ordoamoris")) == []


def test_design_report_validation():
    good = {"design": "03-quiettongue", "n_items": 29, "primary_metric": "say_do_gap",
            "per_area": {"A": 0.2}, "refusal_accounting": {"helpful": 20},
            "judge_disagreement_rate": 0.1}
    assert validate_design_report(good) == []
    bad = {"design": "03-quiettongue"}
    assert validate_design_report(bad) != []
