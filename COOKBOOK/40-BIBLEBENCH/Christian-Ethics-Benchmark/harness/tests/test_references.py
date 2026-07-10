"""RED: reference_provider wiring (W4) — 06 matched-quality refs + 09 determination
anchors reach assemble_rubric_prompt so judges (and humans) score against identical
anchors. 06/09 stay PROVISIONAL until G5.
"""
import types

from walkworthy import references
from walkworthy.judges import assemble_rubric_prompt
from walkworthy.loader import load_design
from walkworthy.rubrics import spec_for


def test_06_provider_returns_reference_answers(benchmark_root):
    it = next(i for i in load_design("06-crookedpath", benchmark_root, include_exemplars=True)
              if i.extras.get("reference_answers"))
    refs = references.bank_reference_provider(it)
    assert refs and all("text" in r and "label" in r for r in refs)
    prompt = assemble_rubric_prompt(it, spec_for(it.design), "resp", references=refs)
    assert "reference" in prompt.lower()


def test_09_provider_returns_determination_anchors(benchmark_root):
    it = next(i for i in load_design("09-doubleedge", benchmark_root, include_exemplars=True)
              if i.key.get("keyed_determinations"))
    refs = references.bank_reference_provider(it)
    assert refs, "09 must supply keyed-determination / extraction anchors"
    joined = " ".join(r["text"] for r in refs)
    assert it.key["keyed_determinations"][:20] in joined or "determination" in joined.lower()


def test_non_anchored_design_returns_empty():
    it = types.SimpleNamespace(design="01-goodsamaritan", key={}, extras={})
    assert references.bank_reference_provider(it) == []
