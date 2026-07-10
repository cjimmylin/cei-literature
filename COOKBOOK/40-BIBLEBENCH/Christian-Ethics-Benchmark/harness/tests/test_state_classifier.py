"""O3 seam tests: the judge-backed branch state classifier for 02/07.

No live calls — the model boundary is a StubClient with a RECORDED reply. We test
that it (a) matches the model's pick to an allowed state, (b) recovers a state from
prose, (c) falls back to the heuristic on an unmatched reply AND logs a defect, and
(d) short-circuits an empty prior turn without a model call.
"""
from walkworthy.clients import ModelResponse
from walkworthy.executors import default_state_classifier
from walkworthy import live_judges as lj


class StubClient:
    def __init__(self, reply, family="anthropic"):
        self.reply = reply
        self.family = family
        self.calls = 0

    def complete(self, messages, system=None, **kwargs):
        self.calls += 1
        return ModelResponse(text=self.reply, model="stub", family=self.family)


def test_classifier_matches_clean_state_token():
    clf = lj.make_cli_state_classifier(StubClient("refused"))
    assert clf("I cannot do that.", ["complied", "refused"], "02-twomasters") == "refused"


def test_classifier_recovers_state_from_prose():
    clf = lj.make_cli_state_classifier(StubClient("The assistant clearly deflected here."))
    got = clf("Well, let's talk about something else.",
              ["validated", "challenged", "deflected"], "07-seventyseven")
    assert got == "deflected"


def test_classifier_falls_back_and_logs_defect_on_unmatched_reply():
    clf = lj.make_cli_state_classifier(StubClient("banana pancakes"))
    # prior response has a non-compliance marker -> heuristic fallback picks "refused"
    got = clf("I'm sorry, I cannot punch up those claims.",
              ["complied", "refused"], "02-twomasters")
    assert got == default_state_classifier("I'm sorry, I cannot punch up those claims.",
                                           ["complied", "refused"], "02-twomasters")
    assert clf.defects, "an unmatched classifier reply must be logged as a defect"


def test_classifier_short_circuits_empty_prior_without_model_call():
    stub = StubClient("refused")
    clf = lj.make_cli_state_classifier(stub)
    got = clf("   ", ["complied", "refused"], "02-twomasters")
    assert got == "complied"          # states[0]
    assert stub.calls == 0            # never hit the model


def test_classifier_is_callable_with_stateclassifier_signature():
    clf = lj.make_cli_state_classifier(StubClient("complied"))
    # (prior_response: str, states: List[str], design: str) -> str
    out = clf("some text", ["complied", "refused"], "02-twomasters")
    assert isinstance(out, str)
