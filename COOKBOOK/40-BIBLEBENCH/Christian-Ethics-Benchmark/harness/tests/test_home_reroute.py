"""PR-16 FR-7 replacement-pair materialization."""
import json
from copy import deepcopy
from pathlib import Path
from types import SimpleNamespace

import pytest

from walkworthy.home_reroute import (DISQUALIFIED_JUDGE, MISTRAL_MODEL,
                                     SURVIVING_JUDGE, apply_replacement_pair, main,
                                     plan_home_reroute, run_home_reroute,
                                     validate_nonselected_invariance)


ROOT = Path(__file__).resolve().parents[2]
W1 = ROOT / "runs" / "20260712-o5-tiebreak"


def _jsonl(path):
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()
            if line.strip()]


def _record(item_id="WW-05-X", design="05-ordoamoris"):
    categories = (["rationale_honesty"] if design == "05-ordoamoris" else
                  ["frame", "facts", "principles", "alternatives", "resolution",
                   "remainder", "pastoral"])
    openai_scores = {name: (2 if design == "05-ordoamoris" else 1)
                     for name in categories}
    google_scores = {name: 0 for name in categories}
    return {
        "item_id": item_id,
        "design": design,
        "model": "google/gemini-2.5-pro",
        "administrations": [{"label": "main", "response": "answer"}],
        "judge_report": {
            "verdicts": [
                {"judge": "or:openai/gpt-4.1-mini", "family": "openai",
                 "unit": "item", "scores": openai_scores},
                {"judge": "or:google/gemini-2.5-flash", "family": "google",
                 "unit": "item", "scores": google_scores},
            ],
            "disagreements": [],
            "adjudicated_verdict": {
                "judge": "derived:pair-plus-tiebreak", "family": "derived",
                "unit": "item", "scores": deepcopy(google_scores),
                "per_unit": [], "refused": False,
            },
        },
    }


def test_production_plan_is_exact_63_units_249_cells_11_reused_52_missing():
    if not (W1 / "scored_items.jsonl").exists():
        pytest.skip("gitignored production run is not present in this checkout")
    records = _jsonl(W1 / "scored_items.jsonl")
    events = _jsonl(W1 / "tiebreak_events.jsonl")

    plan = plan_home_reroute(records, events)

    assert len(plan) == 63
    assert sum(len(unit["categories"]) for unit in plan) == 249
    assert sum(unit["source"] == "reused_w1" for unit in plan) == 11
    assert sum(unit["source"] == "new_call" for unit in plan) == 52
    assert sum(unit["superseded_pr15_cells"] for unit in plan) == 11
    assert {unit["model"] for unit in plan} == {"google/gemini-2.5-pro"}
    assert {unit["unit_key"] for unit in plan} == {"item"}


def test_replacement_pair_strikes_google_uses_mean_and_routes_disagreement():
    rec = _record()

    resolved = apply_replacement_pair(rec, {"rationale_honesty": 1})
    contested = apply_replacement_pair(rec, {"rationale_honesty": 0})

    assert resolved["judge_report"]["adjudicated_verdict"]["scores"][
        "rationale_honesty"] == 1.5
    assert resolved["judge_report"]["disagreements"][0][
        "adjudication_status"] == "home_reroute_resolved"
    assert resolved["judge_report"]["disagreements"][0]["values"] == [2, 1]
    assert contested["judge_report"]["adjudicated_verdict"]["scores"][
        "rationale_honesty"] is None
    assert contested["judge_report"]["disagreements"][0][
        "adjudication_status"] == "part_b_home_reroute_disagreement"
    assert contested["judge_report"]["disagreements"][0][
        "needs_adjudication"] is True
    provenance = resolved["judge_report"]["home_reroute"]
    assert provenance["disqualified_judge"] == "google/gemini-2.5-flash"
    assert provenance["replacement_judges"] == [
        "openai/gpt-4.1-mini", MISTRAL_MODEL]


def test_runner_is_append_only_resumable_and_preserves_nonselected_records(tmp_path):
    selected = _record()
    untouched = deepcopy(selected)
    untouched.update({"item_id": "WW-01-X", "design": "01-goodsamaritan"})
    source_events = [{
        "item_id": selected["item_id"], "design": selected["design"],
        "model": selected["model"], "unit_key": "item",
        "route": "tie_breaker",
        "tiebreaker_model": MISTRAL_MODEL,
        "scores": {"rationale_honesty": 1}, "defects": [],
        "cost": {"usd": 0.1, "calls": 1, "prompt_tokens": 10,
                 "completion_tokens": 2},
    }]

    class NoCallClient:
        def complete(self, *args, **kwargs):
            raise AssertionError("reused W1 score must not trigger a new call")

    checkpoint = tmp_path / "events.jsonl"
    out, summary = run_home_reroute(
        [selected, untouched], {}, NoCallClient(), source_events, checkpoint)
    resumed, summary2 = run_home_reroute(
        [selected, untouched], {}, NoCallClient(), source_events, checkpoint)

    assert out[1] == untouched
    assert resumed == out
    assert summary["selected_units"] == 1
    assert summary["selected_cells"] == 1
    assert summary["reused_w1_units"] == 1
    assert summary["new_call_units"] == 0
    assert summary["resolved_cells"] == 1
    assert summary["complete"] is True
    assert summary2["checkpointed_units"] == 1
    assert len(checkpoint.read_text(encoding="utf-8").splitlines()) == 1

    corrupted = deepcopy(out)
    corrupted[1]["unexpected"] = True
    try:
        validate_nonselected_invariance([selected, untouched], corrupted,
                                        plan_home_reroute([selected, untouched], source_events))
    except ValueError as exc:
        assert "nonselected" in str(exc)
    else:
        raise AssertionError("nonselected mutation was accepted")


def test_resume_rejects_wrong_model_checkpoint(tmp_path):
    selected = _record()
    checkpoint = tmp_path / "events.jsonl"
    checkpoint.write_text(json.dumps({
        "item_id": selected["item_id"], "design": selected["design"],
        "model": selected["model"], "unit_key": "item", "route": "home_reroute",
        "source": "reused_w1", "tiebreaker_model": "wrong/model",
        "scores": {"rationale_honesty": 1}, "defects": [], "cost": {},
    }) + "\n", encoding="utf-8")
    source_events = [{
        "item_id": selected["item_id"], "design": selected["design"],
        "model": selected["model"], "unit_key": "item",
        "route": "tie_breaker",
        "tiebreaker_model": MISTRAL_MODEL,
        "scores": {"rationale_honesty": 1}, "defects": [],
    }]

    try:
        run_home_reroute([selected], {}, object(), source_events, checkpoint)
    except ValueError as exc:
        assert "checkpoint provenance" in str(exc)
    else:
        raise AssertionError("wrong-model checkpoint was accepted")


def test_resume_rejects_unexpected_checkpoint_key(tmp_path):
    selected = _record()
    checkpoint = tmp_path / "events.jsonl"
    checkpoint.write_text(json.dumps({
        "item_id": "WW-EXTRA", "design": selected["design"],
        "model": selected["model"], "unit_key": "item", "route": "home_reroute",
        "source": "new_call", "tiebreaker_model": MISTRAL_MODEL,
        "scores": {"rationale_honesty": 1}, "defects": [], "cost": {},
    }) + "\n", encoding="utf-8")

    with pytest.raises(ValueError, match="unexpected checkpoint"):
        run_home_reroute([selected], {}, object(), [], checkpoint)


def test_cli_refuses_to_overwrite_completed_derived_run(tmp_path):
    root = tmp_path / "bench"
    source = root / "runs" / "20260712-o5-tiebreak"
    out = root / "runs" / "derived"
    source.mkdir(parents=True)
    out.mkdir(parents=True)
    (out / "home_reroute_summary.json").write_text(
        json.dumps({"complete": True}), encoding="utf-8")

    try:
        main(["--benchmark-root", str(root), "--source-run", "20260712-o5-tiebreak",
              "--out-run", "derived", "--surviving-judge", SURVIVING_JUDGE,
              "--disqualified-judge", DISQUALIFIED_JUDGE,
              "--tiebreaker-model", MISTRAL_MODEL])
    except SystemExit as exc:
        assert "immutable" in str(exc)
    else:
        raise AssertionError("completed derived run was not immutable")


def test_cli_rejects_run_path_traversal_before_io(tmp_path):
    for field, value in (("--source-run", "../escape"),
                         ("--out-run", "../escape")):
        args = ["--benchmark-root", str(tmp_path), "--source-run",
                "20260712-o5-tiebreak", "--out-run", "derived",
                "--surviving-judge", SURVIVING_JUDGE,
                "--disqualified-judge", DISQUALIFIED_JUDGE,
                "--tiebreaker-model", MISTRAL_MODEL]
        args[args.index(field) + 1] = value
        with pytest.raises(SystemExit, match="PUBLIC runs"):
            main(args)
