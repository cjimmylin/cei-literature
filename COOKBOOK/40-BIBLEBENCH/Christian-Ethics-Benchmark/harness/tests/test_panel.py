"""Panel-runner tests (O4-prep). Exercise `run_panel` end-to-end with an injected
MOCK SUT fleet + stub-backed live judges/classifier — NO live HTTP calls.

Proves the four properties the panel adds on top of the (already-tested) per-item
pipeline: deterministic item selection, model fan-out, per-(item,model) checkpoint
RESUME (a killed run continues without re-calling completed cells), and cost
aggregation. The measurement logic itself (execute/score/judge) is unchanged and
tested elsewhere.
"""
import json

import pytest

from walkworthy.clients import MockModelClient, ModelResponse
from walkworthy.live_judges import CLIJudge, make_cli_state_classifier
from walkworthy import panel


# --------------------------------------------------------------------------- #
# test doubles
# --------------------------------------------------------------------------- #
SUPERSET_VERDICT = json.dumps({
    "action_class": "partial", "rationale_quality": 1,      # 01
    "rationale_honesty": 2,                                  # 05
    "floor_compliance": 1, "owes_direction": "mutual",      # 09
})


class Stub:
    """Returns a fixed verdict/state on every call; optionally bumps a cost acc."""

    def __init__(self, reply, family="anthropic", acc=None):
        self.reply = reply
        self.family = family
        self.n = 0
        self._acc = acc

    def complete(self, messages, system=None, **kwargs):
        self.n += 1
        if self._acc is not None:
            self._acc["calls"] += 1
            self._acc["cost"] += 0.01
        return ModelResponse(text=self.reply, model="stub", family=self.family)


class CountingMock(MockModelClient):
    """MockModelClient that counts complete() calls (to prove resume skips cells)."""

    def __init__(self, *a, acc=None, **kw):
        super().__init__(*a, **kw)
        self.calls = 0
        self._acc = acc

    def complete(self, messages, system=None, **kwargs):
        self.calls += 1
        if self._acc is not None:
            self._acc["calls"] += 1
            self._acc["cost"] += 0.02
        return super().complete(messages, system=system, **kwargs)


class PoisonClient(MockModelClient):
    """Raises if complete() is ever called — proves a completed cell is skipped."""

    def complete(self, messages, system=None, **kwargs):
        raise AssertionError(f"PoisonClient {self.name} must not be called (cell already done)")


class RaisingClient(MockModelClient):
    """Raises ModelCallError on every complete() — simulates a model that returns empty
    content mid-run (the real failure that crashed the qwen pilot run)."""

    def complete(self, messages, system=None, **kwargs):
        from walkworthy.cli_backends import ModelCallError
        raise ModelCallError(f"{self.name}: simulated empty content (finish=None)")


def _judges(acc=None):
    return [
        CLIJudge("judge-openai", Stub(SUPERSET_VERDICT, "openai", acc), family="openai"),
        CLIJudge("judge-google", Stub(SUPERSET_VERDICT, "google", acc), family="google"),
    ]


def _classifier(acc=None):
    return make_cli_state_classifier(Stub("mutual", "openai", acc))


TWO_DESIGNS = ["01-goodsamaritan", "09-doubleedge"]


# --------------------------------------------------------------------------- #
# item selection
# --------------------------------------------------------------------------- #
def test_select_panel_items_is_deterministic_n_per_design(benchmark_root):
    from walkworthy.loader import load_public_split
    allit = load_public_split(str(benchmark_root), include_exemplars=True, runnable_only=True)
    sel1 = panel.select_panel_items(allit, items_per_design=5)
    sel2 = panel.select_panel_items(allit, items_per_design=5)
    # reproducible
    assert [it.id for it in sel1] == [it.id for it in sel2]
    # exactly 5 per design (every design has >= 5 runnable items)
    from collections import Counter
    c = Counter(it.design for it in sel1)
    assert set(c.values()) == {5}
    assert len(c) == 10           # all ten designs present


def test_select_panel_items_none_returns_all(benchmark_root):
    from walkworthy.loader import load_public_split
    allit = load_public_split(str(benchmark_root), include_exemplars=True, runnable_only=True)
    assert len(panel.select_panel_items(allit, items_per_design=None)) == len(allit)


def test_select_panel_items_handles_design_with_fewer_than_n(benchmark_root):
    from walkworthy.loader import load_public_split
    allit = load_public_split(str(benchmark_root), include_exemplars=True, runnable_only=True)
    only07 = [it for it in allit if it.design == "07-seventyseven"]
    sel = panel.select_panel_items(only07, items_per_design=9999)
    assert len(sel) == len(only07)     # never more than available


# --------------------------------------------------------------------------- #
# fan-out
# --------------------------------------------------------------------------- #
def test_run_panel_fans_out_one_record_per_item_times_model(benchmark_root, tmp_path):
    suts = [MockModelClient("sut-alpha", seed=7, disposition=0.3),
            MockModelClient("sut-bravo", seed=7, disposition=0.9)]
    top = panel.run_panel(
        str(benchmark_root), tmp_path, suts, _judges(), _classifier(),
        items_per_design=2, designs=TWO_DESIGNS,
    )
    assert top["n_models"] == 2
    assert top["n_items"] == 4                     # 2 designs x 2 items
    assert top["n_records"] == 8                    # items x models
    # both models represented, cells keyed (design, model)
    models = {m["name"] for m in top["suts"]}
    assert models == {"sut-alpha", "sut-bravo"}
    for d in TWO_DESIGNS:
        assert set(top["cells"][d].keys()) == models


def test_run_panel_manifest_is_ids_only_records_subset_and_all_models(benchmark_root, tmp_path):
    suts = [MockModelClient("sut-alpha", seed=7), MockModelClient("sut-bravo", seed=1)]
    panel.run_panel(str(benchmark_root), tmp_path, suts, _judges(), _classifier(),
                    items_per_design=3, designs=["01-goodsamaritan"])
    man = json.loads((tmp_path / "manifest.json").read_text())
    assert len(man["item_ids"]) == 3               # the selected subset, not 344
    assert {m["name"] for m in man["models"]} == {"sut-alpha", "sut-bravo"}
    assert all(isinstance(v, int) for v in man["permutation_seeds"].values())
    assert "Priya receives" not in json.dumps(man)  # no prompt text leaks


# --------------------------------------------------------------------------- #
# checkpoint / resume
# --------------------------------------------------------------------------- #
def test_run_panel_resume_skips_all_completed_cells(benchmark_root, tmp_path):
    # first run populates the checkpoint
    suts = [MockModelClient("sut-alpha", seed=7), MockModelClient("sut-bravo", seed=1)]
    first = panel.run_panel(str(benchmark_root), tmp_path, suts, _judges(), _classifier(),
                            items_per_design=2, designs=TWO_DESIGNS)
    n0 = first["n_records"]

    # second run with POISON clients of the SAME names: every cell done -> no calls
    poison = [PoisonClient("sut-alpha", seed=7), PoisonClient("sut-bravo", seed=1)]
    again = panel.run_panel(str(benchmark_root), tmp_path, poison, _judges(), _classifier(),
                            items_per_design=2, designs=TWO_DESIGNS)
    assert again["n_records"] == n0                # nothing re-run, nothing lost
    assert again["n_new_records"] == 0
    # no duplicate (item_id, model) lines in the checkpoint
    lines = [json.loads(l) for l in (tmp_path / "scored_items.jsonl").read_text().splitlines() if l.strip()]
    keys = [(r["item_id"], r["model"]) for r in lines]
    assert len(keys) == len(set(keys)) == n0


def test_run_panel_partial_resume_runs_only_missing_cells(benchmark_root, tmp_path):
    # seed the checkpoint with ONLY sut-alpha
    a_only = [MockModelClient("sut-alpha", seed=7)]
    panel.run_panel(str(benchmark_root), tmp_path, a_only, _judges(), _classifier(),
                    items_per_design=2, designs=TWO_DESIGNS)

    # resume with alpha (POISON: already done) + bravo (COUNTING: must run)
    bravo = CountingMock("sut-bravo", seed=1)
    poison_a = PoisonClient("sut-alpha", seed=7)
    top = panel.run_panel(str(benchmark_root), tmp_path, [poison_a, bravo],
                          _judges(), _classifier(), items_per_design=2, designs=TWO_DESIGNS)
    assert bravo.calls > 0                          # bravo's cells were executed
    assert top["n_new_records"] == 4                # only bravo's 4 cells are new
    assert top["n_records"] == 8                    # union: 4 alpha + 4 bravo


# --------------------------------------------------------------------------- #
# resilience: a failing cell is logged as data, the batch continues
# --------------------------------------------------------------------------- #
def test_run_panel_logs_cell_errors_and_continues(benchmark_root, tmp_path):
    good = MockModelClient("sut-good", seed=7)
    bad = RaisingClient("sut-bad", seed=7)
    top = panel.run_panel(str(benchmark_root), tmp_path, [good, bad], _judges(), _classifier(),
                          items_per_design=2, designs=TWO_DESIGNS)
    # the run COMPLETED despite sut-bad failing every cell (no crash)
    assert top["n_records"] == 4                         # only the 4 good cells scored
    assert top["n_errors"] == 4                          # every bad cell logged as an error
    assert all(e["model"] == "sut-bad" and "error" in e for e in top["errors"])
    # errored cells are NOT written as scored records
    lines = [json.loads(l) for l in (tmp_path / "scored_items.jsonl").read_text().splitlines() if l.strip()]
    assert {r["model"] for r in lines} == {"sut-good"}
    # a separate errors log is written
    assert (tmp_path / "panel_errors.jsonl").exists()


def test_run_panel_retries_errored_cells_on_resume(benchmark_root, tmp_path):
    # a model that fails every cell writes NO scored records...
    bad = RaisingClient("sut-x", seed=7)
    first = panel.run_panel(str(benchmark_root), tmp_path, [bad], _judges(), _classifier(),
                            items_per_design=2, designs=["01-goodsamaritan"])
    assert first["n_records"] == 0 and first["n_errors"] == 2
    # ...so on resume (same model name "recovers") the errored cells are RETRIED, not skipped
    good = MockModelClient("sut-x", seed=7)
    again = panel.run_panel(str(benchmark_root), tmp_path, [good], _judges(), _classifier(),
                            items_per_design=2, designs=["01-goodsamaritan"])
    assert again["n_records"] == 2                        # previously-errored cells now scored


# --------------------------------------------------------------------------- #
# cost aggregation
# --------------------------------------------------------------------------- #
def test_run_panel_tracks_cost_per_item_and_sums_totals(benchmark_root, tmp_path):
    acc = {"calls": 0, "cost": 0.0, "prompt_tokens": 0, "completion_tokens": 0}
    suts = [CountingMock("sut-alpha", seed=7, acc=acc)]
    top = panel.run_panel(
        str(benchmark_root), tmp_path, suts, _judges(acc), _classifier(acc),
        items_per_design=2, designs=TWO_DESIGNS, cost_probe=lambda: dict(acc),
    )
    # every record carries a per-item cost delta
    lines = [json.loads(l) for l in (tmp_path / "scored_items.jsonl").read_text().splitlines() if l.strip()]
    assert all("_panel_cost" in r and r["_panel_cost"]["usd"] > 0 for r in lines)
    # the run total equals the sum of per-item deltas equals the live accumulator
    assert top["cost"]["total_usd"] == pytest.approx(sum(r["_panel_cost"]["usd"] for r in lines))
    assert top["cost"]["total_usd"] == pytest.approx(acc["cost"])


def test_run_panel_cost_is_resume_safe(benchmark_root, tmp_path):
    # first run accrues cost into the checkpoint records
    acc1 = {"calls": 0, "cost": 0.0, "prompt_tokens": 0, "completion_tokens": 0}
    panel.run_panel(str(benchmark_root), tmp_path, [CountingMock("sut-alpha", seed=7, acc=acc1)],
                    _judges(acc1), _classifier(acc1), items_per_design=2, designs=TWO_DESIGNS,
                    cost_probe=lambda: dict(acc1))
    # second (fresh-process) run adds bravo; its accumulator starts at 0
    acc2 = {"calls": 0, "cost": 0.0, "prompt_tokens": 0, "completion_tokens": 0}
    top = panel.run_panel(str(benchmark_root), tmp_path, [PoisonClient("sut-alpha", seed=7),
                          CountingMock("sut-bravo", seed=1, acc=acc2)],
                          _judges(acc2), _classifier(acc2), items_per_design=2, designs=TWO_DESIGNS,
                          cost_probe=lambda: dict(acc2))
    # reported total = alpha (from checkpoint) + bravo (this process), not just acc2
    lines = [json.loads(l) for l in (tmp_path / "scored_items.jsonl").read_text().splitlines() if l.strip()]
    assert top["cost"]["total_usd"] == pytest.approx(sum(r["_panel_cost"]["usd"] for r in lines))
    assert top["cost"]["total_usd"] > acc2["cost"]   # includes the prior process's cost


# --------------------------------------------------------------------------- #
# design coverage: 05 allocation path + per-seat + artifacts
# --------------------------------------------------------------------------- #
def test_run_panel_runs_05_allocation_path(benchmark_root, tmp_path):
    top = panel.run_panel(str(benchmark_root), tmp_path, [MockModelClient("sut-alpha", seed=7)],
                          _judges(), _classifier(), items_per_design=1, designs=["05-ordoamoris"])
    lines = [json.loads(l) for l in (tmp_path / "scored_items.jsonl").read_text().splitlines() if l.strip()]
    assert all("allocation" in r for r in lines)     # 05 records carry the parsed allocation


def test_run_panel_writes_artifacts_and_judge_pair_summary(benchmark_root, tmp_path):
    suts = [MockModelClient("sut-alpha", seed=7), MockModelClient("sut-bravo", seed=1)]
    top = panel.run_panel(str(benchmark_root), tmp_path, suts, _judges(), _classifier(),
                          items_per_design=2, designs=TWO_DESIGNS)
    assert (tmp_path / "manifest.json").exists()
    assert (tmp_path / "panel_summary.json").exists()
    assert (tmp_path / "panel_report.md").exists()
    # judge-pair comparison present (the headline O4-prep finding surface)
    jp = top["judge_pair"]
    assert 0.0 <= jp["overall_agreement"] <= 1.0
    assert set(jp["by_design"].keys()) == set(TWO_DESIGNS)
    # descriptive per-design spread present (pre-gate input, NOT a pass/fail)
    for d in TWO_DESIGNS:
        assert "spread_points" in top["design_spread"][d]
    # report labelled pre-gate
    assert "pilot" in (tmp_path / "panel_report.md").read_text().lower()
