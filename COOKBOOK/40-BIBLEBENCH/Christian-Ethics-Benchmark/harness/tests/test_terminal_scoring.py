"""RED: per_turn judging must also score the terminal artifact (07 arc-conformance).

07 dialogues end in a forced terminal_ask ("write the note you'd send"); that terminal
response carries the arc's endpoint state (faithful_counsel vs full_validation). The
per_turn judge scores main.turns AND the terminal_response, appended as a unit flagged
`terminal: True`, so the arc-conformance metric can read the terminal state.
"""
import types

from walkworthy.clients import MockModelClient, ModelResponse
from walkworthy.executors import execute_item
from walkworthy.judges import MockJudge
from walkworthy.loader import load_design
from walkworthy.manifest import FIXED_PERMUTATION_SEEDS
from walkworthy.rubrics import spec_for
from walkworthy import live_judges as lj


def test_mock_per_turn_appends_terminal_unit_when_present(benchmark_root):
    it = load_design("07-seventyseven", benchmark_root, include_exemplars=False)[0]
    ex = execute_item(it, MockModelClient("m", seed=1), FIXED_PERMUTATION_SEEDS)
    main = next(a for a in ex.administrations if a.label == "main")
    v = MockJudge("j", family="openai").score(it, ex, spec_for(it.design))
    if main.terminal_response is not None:
        assert any(u.get("terminal") for u in v.per_unit), "terminal artifact must be scored"
        assert len(v.per_unit) == len(main.turns) + 1
    else:  # item has no separate terminal ask -> unchanged
        assert len(v.per_unit) == len(main.turns)


class _Stub:
    def __init__(self, responses, family="anthropic"):
        self.responses = list(responses)
        self.family = family
        self.prompts = []

    def complete(self, messages, system=None, **kwargs):
        self.prompts.append(messages[-1].content)
        return ModelResponse(text=self.responses.pop(0), model="stub", family=self.family)


def test_clijudge_per_turn_scores_terminal_response():
    spec = spec_for("07-seventyseven")
    item = types.SimpleNamespace(id="WW-07-X", design="07-seventyseven", area="A",
                                 stratum="a", tier="core", key={"keyed": "k"})
    ex = types.SimpleNamespace(administrations=[types.SimpleNamespace(
        label="main", kind="scripted_multi_turn",
        turns=[types.SimpleNamespace(index=1, response="I hear you."),
               types.SimpleNamespace(index=2, response="But consider ...")],
        terminal_response="Here is the note: you must reconcile.")])
    client = _Stub(['{"turn_state":"comfort_only"}',
                    '{"turn_state":"faithful_counsel"}',
                    '{"turn_state":"faithful_counsel"}'])
    v = lj.CLIJudge("j", client).score(item, ex, spec)
    assert len(v.per_unit) == 3
    assert v.per_unit[-1].get("terminal") is True
    assert len(client.prompts) == 3
