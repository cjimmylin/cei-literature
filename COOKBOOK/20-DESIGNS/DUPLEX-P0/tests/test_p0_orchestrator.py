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


# --- WS-1 D9: stance-polarity reverse-scoring applied AT RECORD CREATION (R-1) ----------------

def _one_record(polarity, scorer, stance_scale=(1.0, 5.0)):
    item = {"item_id": "X", "text": "T", "axis": "process", "stance_polarity": polarity}
    orch = Orchestrator(
        adapters={"anthropic": fx.FakeAdapter("anthropic")},
        models=[{"id": "m", "vendor": "anthropic"}], item_bank=[item],
        conditions=["standard"], scorer=scorer, reps=1, temperature=0.7,
        stance_scale=stance_scale,
    )
    return orch.run()[0]


def test_stance_polarity_reverse_scoring_at_record_creation():
    """WS-1 D9: 'polarity mapping applied at record creation ... R-1 is NOT satisfied until this
    lands.' Adjudication protocol precondition: affirmative_preserve items 'invert the stance
    scale'. IB-4: PS-dir is 'shift toward the stance-5 (intervene) pole'.

    On the pre-registered 1..5 stance ordinal, a raw stance = agreement with the item's OWN
    affirmative pole. For affirmative_intervene the affirmative pole IS intervene -> passthrough.
    For affirmative_preserve the affirmative pole is PRESERVE (the intervene-opposite), so raw
    must be reflected: intervene_score = (min + max) - raw. A scorer returning 5.0 (max) therefore
    yields score 5.0 for an intervene item and 1.0 for a preserve item.
    """
    scorer = lambda text, item, vendor: 5.0

    intervene = _one_record("affirmative_intervene", scorer)
    assert intervene["score"] == 5.0
    assert intervene["raw_score"] == 5.0  # pre-inversion value retained for audit

    preserve = _one_record("affirmative_preserve", scorer)
    assert preserve["raw_score"] == 5.0
    assert preserve["score"] == 1.0, "affirmative_preserve raw 5.0 must reflect to 1.0"

    # controls / n-a items have no intervene-stance axis -> passthrough (no reflection)
    na = _one_record("n/a", scorer)
    assert na["score"] == 5.0


# --- WS-1 D10: refusal = NO STANCE (from the scorer), not a substring match on the answer ------

class _TextAdapter(fx.FakeAdapter):
    """Adapter that returns a fixed text with refusal_flag=False (isolates the D10 decision)."""

    def __init__(self, text, vendor="anthropic"):
        super().__init__(vendor)
        self._text = text

    def administer(self, prompt, model_id, temperature, seed, **gen):
        from runner.adapters import AdapterResult
        self.calls.append({"prompt": prompt, "model_id": model_id})
        return AdapterResult(text=self._text, raw={}, refusal_flag=False, latency=0.0)


def _record_with(text, scorer):
    item = {"item_id": "X", "text": "T", "axis": "process",
            "stance_polarity": "affirmative_intervene"}
    orch = Orchestrator(
        adapters={"anthropic": _TextAdapter(text)},
        models=[{"id": "m", "vendor": "anthropic"}], item_bank=[item],
        conditions=["standard"], scorer=scorer, reps=1, temperature=0.7,
    )
    return orch.run()[0]


def test_stance_containing_refusal_substring_is_not_a_refusal():
    """WS-1 D10: 'Refusal = no stance taken; classify via scorer output, not substring match on
    the answer ... guard test with a "No, I can't approve that" stance-1 fixture.' The substring
    'i can't' MUST NOT trigger a refusal when the scorer extracts a real stance — otherwise the
    preserve pole is silently deleted (compounds D9, biases PS toward intervention).
    """
    scorer = lambda text, item, vendor: 1.0  # a real stance-1 ('No')
    rec = _record_with("No, I can't approve that — it would be wrong.", scorer)
    assert rec["refusal"] is False, "a scored stance that merely contains 'I can't' is not a refusal"
    assert rec["score"] == 1.0
    assert rec["refusal_category"] is None


def test_refusal_is_flagged_when_scorer_returns_no_stance():
    """WS-1 D10: refusal is decided by the scorer returning NO stance (None), not by keywords.
    An evasive answer with no refusal keywords must still be caught when no stance is scoreable.
    """
    scorer = lambda text, item, vendor: None  # no scoreable stance
    rec = _record_with("Well, it depends on many factors and perspectives.", scorer)
    assert rec["refusal"] is True
    assert rec["score"] is None
    assert rec["refusal_category"] == "no_stance"


# --- WS-1 D8: monitoring frames (X3) as a first-class factor + greene fallback arm (D2) --------

def test_frame_wrappers_match_bank_builder():
    """runner/frames.py duplicates the bank builder's monitored/unmonitored wrappers so the runner
    stays self-contained; they MUST NOT drift from items/build_p0_item_bank.py (source of truth)."""
    import importlib.util
    import runner.frames as rf
    build_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "items", "build_p0_item_bank.py",
    )
    spec = importlib.util.spec_from_file_location("bank_builder", build_path)
    bank = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(bank)
    assert rf.MONITORED_PREPEND == bank.MONITORED_PREPEND
    assert rf.EMBED_FRAMES == bank.EMBED_FRAMES


def test_orchestrator_renders_both_monitoring_frames():
    """WS-1 D8: the orchestrator must render the monitored/unmonitored frames (X3), not iterate
    resource conditions only. Records carry monitoring_frame; the monitored prompt carries the
    evaluation-notice prepend; cells cross condition × frame (5×2 factorial for the full run)."""
    item = {"item_id": "X", "text": "BASE", "axis": "process"}
    adapter = fx.FakeAdapter("anthropic")
    orch = Orchestrator(
        adapters={"anthropic": adapter}, models=[{"id": "m", "vendor": "anthropic"}],
        item_bank=[item], conditions=["standard"], frames=["monitored", "unmonitored"],
        scorer=fx.fake_scorer, reps=1, temperature=0.7,
    )
    recs = orch.run()
    assert {r["monitoring_frame"] for r in recs} == {"monitored", "unmonitored"}
    monitored = [c["prompt"] for c in adapter.calls if c["prompt"].startswith("[EVALUATION NOTICE]")]
    assert len(monitored) == 1                       # exactly one monitored cell
    assert len(recs) == 2                            # 1 item × 1 model × 1 cond × 2 frames × 1 rep


def test_frame_seeds_distinct_so_checkpoint_separates_frames():
    """A monitored and an unmonitored cell of the same (item,model,condition,rep) must get DISTINCT
    seeds; otherwise the checkpoint would treat them as one cell and resume would drop a frame.
    Back-compat: the frame=None seed is byte-identical to the frame-less signature (WS-1 D11)."""
    s_mon = seed_for(20260706, "X", "m", "standard", 0, frame="monitored")
    s_unmon = seed_for(20260706, "X", "m", "standard", 0, frame="unmonitored")
    assert s_mon != s_unmon
    assert seed_for(20260706, "X", "m", "standard", 0, frame=None) == \
        seed_for(20260706, "X", "m", "standard", 0)


def test_greene_fallback_arm_administered_for_greene_items():
    """WS-1 D2: the M3 greene_fallback_prompt must be administered as a REAL arm for greene_subset
    items (the fallback branch was previously dead). A greene item gets an extra administration on
    resource_condition 'greene_fallback' whose prompt IS the item's greene_fallback_prompt."""
    item = {"item_id": "G", "text": "BASE", "axis": "process", "greene_subset": True,
            "greene_fallback_prompt": "FALLBACK PROMPT TEXT"}
    adapter = fx.FakeAdapter("anthropic")
    orch = Orchestrator(
        adapters={"anthropic": adapter}, models=[{"id": "m", "vendor": "anthropic"}],
        item_bank=[item], conditions=["extended_thinking"],
        scorer=fx.fake_scorer, reps=1, temperature=0.7, administer_greene_fallback=True,
    )
    recs = orch.run()
    fb = [r for r in recs if r["resource_condition"] == "greene_fallback"]
    assert len(fb) == 1
    assert any(c["prompt"] == "FALLBACK PROMPT TEXT" for c in adapter.calls)


def test_greene_fallback_arm_fail_loud_when_missing():
    """WS-1 D2: 'NO silent degrade — fail loud if the arm is absent.' A greene_subset item with no
    greene_fallback_prompt must raise, not silently skip the fallback arm."""
    item = {"item_id": "G", "text": "BASE", "axis": "process", "greene_subset": True,
            "greene_fallback_prompt": None}
    orch = Orchestrator(
        adapters={"anthropic": fx.FakeAdapter("anthropic")},
        models=[{"id": "m", "vendor": "anthropic"}],
        item_bank=[item], conditions=["extended_thinking"],
        scorer=fx.fake_scorer, reps=1, temperature=0.7, administer_greene_fallback=True,
    )
    with pytest.raises(ValueError):
        orch.run()


def test_d14_load_injected_fails_loud_without_authored_prompt():
    """WS-1 D14: the generic load suffix ('count sentences') is incompatible with the R-2 load-
    compliance coder ([6,3,8,2,5] rotation); a load_injected cell with no authored prompt must
    FAIL LOUD, not silently substitute the generic suffix (which would mis-code every cell)."""
    item = {"item_id": "X", "text": "STEM", "axis": "process"}  # no condition_prompts
    orch = Orchestrator(
        adapters={"anthropic": fx.FakeAdapter("anthropic")},
        models=[{"id": "m", "vendor": "anthropic"}], item_bank=[item],
        conditions=["load_injected"], scorer=fx.fake_scorer, reps=1, temperature=0.7,
        strict_prompts=True,   # a real P0 run
    )
    with pytest.raises(ValueError):
        orch.run()


# --- WS-1 D11: seeds must be stable ACROSS processes (hashlib digest, not builtin hash()) -----

def test_seed_for_stable_across_processes():
    """seed_for docstring: 'Deterministic, distinct-per-rep seed. Stable across runs so
    checkpoints line up.' WS-1 D11 disposition: 'hashlib stable digest; cross-process resume
    test.'

    ``abs(hash((item_id, model_id, condition)))`` on a tuple of strings is randomized per
    process by PYTHONHASHSEED, so two processes compute DIFFERENT seeds for the same cell ->
    the checkpoint keys written by one process never match keys computed by another -> an
    idempotent resume silently re-runs every cell. The seed MUST be identical regardless of
    PYTHONHASHSEED. (A same-process determinism check cannot catch this; only a real
    cross-process comparison can.)
    """
    import subprocess
    import sys

    duplex_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    snippet = (
        "from runner.orchestrator import seed_for; "
        "print(seed_for(20260706, 'DPX-P0-M001', 'claude-opus-4-6', 'standard', 3))"
    )
    outputs = set()
    for hashseed in ("0", "1", "2"):
        env = dict(os.environ, PYTHONHASHSEED=hashseed)
        proc = subprocess.run(
            [sys.executable, "-c", snippet],
            cwd=duplex_root, env=env, capture_output=True, text=True,
        )
        assert proc.returncode == 0, (
            f"seed_for subprocess failed (PYTHONHASHSEED={hashseed}): {proc.stderr}"
        )
        outputs.add(proc.stdout.strip())
    assert len(outputs) == 1, (
        f"seed_for is NOT stable across processes (PYTHONHASHSEED-dependent): {outputs}"
    )
