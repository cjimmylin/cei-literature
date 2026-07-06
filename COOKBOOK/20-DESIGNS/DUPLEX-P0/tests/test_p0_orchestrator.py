"""Orchestration: reps, temperature guard, idempotent checkpointing, resume, refusal, per-condition SD."""
import os

import pytest

import fixtures_p0 as fx
from runner.orchestrator import (
    Orchestrator,
    Checkpoint,
    condition_config,
    per_condition_sd,
    load_results,
    cell_key,
    seed_for,
)


CONDITIONS = ["forced_immediate", "extended_thinking"]


def _models():
    return [{"id": "claude-opus-4-6", "vendor": "anthropic"}]


def _bank():
    return [fx.FIXTURE_ITEM_BANK[0]]


def _orch(**kw):
    adapters = {"anthropic": fx.FakeAdapter("anthropic")}
    defaults = dict(
        adapters=adapters, models=_models(), item_bank=_bank(), conditions=CONDITIONS,
        scorer=fx.fake_scorer, reps=10, temperature=0.7,
    )
    defaults.update(kw)
    return Orchestrator(**defaults)


def test_condition_config_shapes():
    fi = condition_config("forced_immediate")
    assert fi["gen"]["max_tokens"] == 16 and fi["gen"]["thinking"] is None
    ext = condition_config("extended_thinking")
    assert ext["gen"]["thinking"] == {"type": "adaptive"}
    load = condition_config("load_injected")
    assert "Concurrent task" in load["prompt_suffix"]


def test_temperature_must_be_positive():
    with pytest.raises(ValueError):
        _orch(temperature=0.0)


def test_run_produces_at_least_ten_reps_per_cell():
    orch = _orch(reps=10)
    records = orch.run()
    # 1 item x 1 model x 2 conditions x 10 reps
    assert len(records) == 20
    assert orch.n_administrations == 20
    per_cell = {}
    for r in records:
        per_cell.setdefault((r["item_id"], r["model_id"], r["resource_condition"]), 0)
        per_cell[(r["item_id"], r["model_id"], r["resource_condition"])] += 1
    assert all(v >= 10 for v in per_cell.values())


def test_checkpoint_idempotent_resume(tmp_path):
    ckpt_path = str(tmp_path / "ckpt.jsonl")
    out_path = str(tmp_path / "results.jsonl")

    orch1 = _orch(checkpoint=Checkpoint(ckpt_path), out_path=out_path)
    recs1 = orch1.run()
    assert orch1.n_administrations == 20

    # fresh orchestrator, same checkpoint file: everything already done -> zero new calls
    adapters2 = {"anthropic": fx.FakeAdapter("anthropic")}
    orch2 = Orchestrator(
        adapters=adapters2, models=_models(), item_bank=_bank(), conditions=CONDITIONS,
        scorer=fx.fake_scorer, reps=10, temperature=0.7,
        checkpoint=Checkpoint(ckpt_path), out_path=out_path,
    )
    recs2 = orch2.run()
    assert recs2 == []
    assert orch2.n_administrations == 0
    assert adapters2["anthropic"].calls == []

    # results file still holds exactly the 20 from run 1 (no duplication)
    assert len(load_results(out_path)) == 20


def test_resume_from_partial_checkpoint(tmp_path):
    ckpt_path = str(tmp_path / "ckpt.jsonl")
    ckpt = Checkpoint(ckpt_path)
    item = _bank()[0]
    # pre-seed 2 of the 20 cells as done
    preseeded = 0
    for rep in (0, 1):
        seed = seed_for(20260706, item["item_id"], "claude-opus-4-6", "forced_immediate", rep)
        ckpt.mark(cell_key(item["item_id"], "claude-opus-4-6", "forced_immediate", seed))
        preseeded += 1

    orch = _orch(checkpoint=ckpt, base_seed=20260706)
    records = orch.run()
    assert orch.n_administrations == 20 - preseeded
    assert len(records) == 20 - preseeded


def test_refusal_recorded_as_explicit_category():
    adapters = {"anthropic": fx.FakeAdapter("anthropic", refuse_models={"claude-opus-4-6"})}
    orch = Orchestrator(
        adapters=adapters, models=_models(), item_bank=_bank(), conditions=CONDITIONS,
        scorer=fx.fake_scorer, reps=10, temperature=0.7,
    )
    records = orch.run()
    assert all(r["refusal"] is True for r in records)
    assert all(r["score"] is None for r in records)
    assert all(r["refusal_category"] == "explicit_refusal" for r in records)


def test_per_condition_sd_first_class_and_excludes_refusals():
    orch = _orch(reps=10)
    records = orch.run()
    sds = per_condition_sd(records)
    assert "claude-opus-4-6" in sds
    for cond in CONDITIONS:
        assert cond in sds["claude-opus-4-6"]
        assert sds["claude-opus-4-6"][cond] >= 0.0

    # a fully-refusing run yields no scored cells -> empty SD map
    adapters = {"anthropic": fx.FakeAdapter("anthropic", refuse_models={"claude-opus-4-6"})}
    ro = Orchestrator(
        adapters=adapters, models=_models(), item_bank=_bank(), conditions=CONDITIONS,
        scorer=fx.fake_scorer, reps=10, temperature=0.7,
    )
    assert per_condition_sd(ro.run()) == {}
