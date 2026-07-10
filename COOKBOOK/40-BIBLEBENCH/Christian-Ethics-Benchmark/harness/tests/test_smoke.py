"""O3 smoke-driver tests. Exercises run_smoke end-to-end with an injected MOCK SUT +
stub-backed live judges/classifier — NO live CLI calls. Proves slice selection,
artifact writing, IDs-only manifest, and defect aggregation.
"""
import json

from walkworthy.clients import MockModelClient, ModelResponse
from walkworthy.live_judges import CLIJudge, make_cli_state_classifier
from walkworthy import smoke


class CyclingStub:
    """Returns a fixed superset verdict on every call (order-independent)."""

    def __init__(self, reply, family="anthropic"):
        self.reply = reply
        self.family = family
        self.n = 0

    def complete(self, messages, system=None, **kwargs):
        self.n += 1
        return ModelResponse(text=self.reply, model="stub", family=self.family)


SUPERSET_VERDICT = json.dumps({
    "action_class": "partial", "rationale_quality": 1,          # 01
    "floor_compliance": 1, "owes_direction": "mutual",          # 09
})


def _judges():
    return [
        CLIJudge("claude-judge", CyclingStub(SUPERSET_VERDICT, "anthropic"), family="anthropic"),
        CLIJudge("codex-judge", CyclingStub(SUPERSET_VERDICT, "openai"), family="openai"),
    ]


def test_build_smoke_slice_picks_one_runnable_item_per_present_design(benchmark_root):
    from walkworthy.loader import load_public_split
    items = load_public_split(str(benchmark_root), include_exemplars=True, runnable_only=True)
    sl = smoke.build_smoke_slice(items, ["01-goodsamaritan", "09-doubleedge", "zz-missing"])
    designs = [it.design for it in sl]
    assert designs == ["01-goodsamaritan", "09-doubleedge"]   # missing design skipped


def test_run_smoke_produces_records_and_artifacts(benchmark_root, tmp_path):
    sut = MockModelClient("mock-sut", seed=7, disposition=0.6)
    clf = make_cli_state_classifier(CyclingStub("mutual"))
    top = smoke.run_smoke(
        str(benchmark_root), tmp_path, sut, _judges(), clf,
        design_picks=["01-goodsamaritan", "09-doubleedge"],
    )
    # one record per sliced item
    assert top["n_items"] == 2
    assert top["n_records"] == 2
    # artifacts written
    assert (tmp_path / "manifest.json").exists()
    assert (tmp_path / "smoke_summary.json").exists()
    assert (tmp_path / "scored_items.jsonl").exists()
    # per-item mechanics captured, incl the two scoring units
    units = {m["design"]: m["unit"] for m in top["mechanics"]}
    assert units["01-goodsamaritan"] == "item"
    assert units["09-doubleedge"] == "per_seat"


def test_run_smoke_manifest_is_ids_only_with_fixed_seeds(benchmark_root, tmp_path):
    sut = MockModelClient("mock-sut", seed=7)
    clf = make_cli_state_classifier(CyclingStub("mutual"))
    smoke.run_smoke(str(benchmark_root), tmp_path, sut, _judges(), clf,
                    design_picks=["01-goodsamaritan"])
    man = json.loads((tmp_path / "manifest.json").read_text())
    # IDs-only: no prompt text leaked; fixed integer permutation seeds present
    blob = json.dumps(man)
    assert "permutation_seeds" in man
    assert all(isinstance(v, int) for v in man["permutation_seeds"].values())
    assert "Priya receives" not in blob   # no item prompt text in the manifest


def test_run_smoke_aggregates_defects_from_judges(benchmark_root, tmp_path):
    sut = MockModelClient("mock-sut", seed=7)
    # judges return an unparseable verdict -> mechanical defects must surface
    bad = [
        CLIJudge("claude-judge", CyclingStub("no json here", "anthropic"), family="anthropic"),
        CLIJudge("codex-judge", CyclingStub("still no json", "openai"), family="openai"),
    ]
    clf = make_cli_state_classifier(CyclingStub("mutual"))
    top = smoke.run_smoke(str(benchmark_root), tmp_path, sut, bad, clf,
                          design_picks=["01-goodsamaritan"])
    assert top["defects"]["judge"], "unparseable judge verdicts must be aggregated as defects"
