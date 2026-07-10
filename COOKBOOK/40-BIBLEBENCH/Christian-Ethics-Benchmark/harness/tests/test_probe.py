"""RED: PR-5 reliability probe (F-2 lesson: qwen died 45/50 silently).

Before committing the O4 panel roster, probe each candidate SUT + tie-breaker judge on
1 cell/design and tally ok / empty / error. The probe RUN is live; the tally + verdict
logic is unit-tested here against stub clients (no live calls).
"""
from walkworthy import probe
from walkworthy.cli_backends import ModelCallError
from walkworthy.clients import ModelResponse


class _Stub:
    """Yields recorded outcomes: 'ok' -> text, 'empty' -> raises (post-retry), 'err' -> raises."""
    def __init__(self, script, family="openai"):
        self.script = list(script)
        self.family = family
        self.name = "stub"

    def complete(self, messages, system=None, **kw):
        outcome = self.script.pop(0)
        if outcome == "ok":
            return ModelResponse("a real answer", "stub", self.family)
        raise ModelCallError(f"OpenRouter stub: {outcome}")


def test_probe_client_tallies_ok_and_failures():
    c = _Stub(["ok", "ok", "err", "ok"])
    prompts = [("01", "p1"), ("02", "p2"), ("03", "p3"), ("04", "p4")]
    res = probe.probe_client("cand", c, prompts)
    assert res["n"] == 4 and res["ok"] == 3 and res["failed"] == 1
    assert res["ok_rate"] == 0.75
    assert len(res["errors"]) == 1 and res["errors"][0]["design"] == "03"


def test_probe_verdict_reliable_vs_flaky():
    good = probe.probe_client("good", _Stub(["ok"] * 10), [(str(i), "p") for i in range(10)])
    flaky = probe.probe_client("flaky", _Stub(["ok", "err"] + ["err"] * 8),
                               [(str(i), "p") for i in range(10)])
    assert good["reliable"] is True
    assert flaky["reliable"] is False       # F-2: below the reliability floor


def test_reliability_probe_over_multiple_candidates():
    prompts = [("01", "p1"), ("02", "p2")]
    clients = {"a": _Stub(["ok", "ok"]), "b": _Stub(["ok", "err"])}
    report = probe.reliability_probe(clients, prompts)
    assert set(report) == {"a", "b"}
    assert report["a"]["ok_rate"] == 1.0
    assert probe.render_probe_report(report).strip().startswith("#")


def test_draw_probe_prompts_one_per_design(benchmark_root):
    from walkworthy.loader import load_public_split
    items = load_public_split(benchmark_root, include_exemplars=True, runnable_only=True)
    prompts = probe.draw_probe_prompts(items, per_design=1)
    designs = {d for d, _ in prompts}
    assert len(designs) == 10 and len(prompts) == 10
    assert all(isinstance(p, str) and p for _, p in prompts)
