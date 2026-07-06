"""Item-bank normalization + orchestrator preference for per-condition prompts.

These tests use an INLINE dict mimicking the authored schema so they never depend on the real
items/20260706-p0-item-bank.json existing. One extra test loads the real file only if present.
"""
import os

import pytest

import fixtures_p0 as fx
from runner.items import normalize_item, load_item_bank, DEFAULT_BANK_PATH
from runner.orchestrator import Orchestrator


RAW = {
    "id": "DPX-P0-M001",
    "person": "personal",
    "content_tags": ["harm"],
    "is_discriminant_control": False,
    "greene_subset": True,
    "scenario": "Scenario text.",
    "question": "Should you? Give a verdict.",
    "base_prompt": "Scenario text.\n\nShould you? Give a verdict.",
    "resource_condition_variants": {
        "forced_immediate": "FI-PROMPT: answer in 16 tokens.",
        "standard": "STD-PROMPT: full answer.",
        "extended_thinking": "EXT-PROMPT: think step by step.",
        "load_injected": "LOAD-PROMPT: also count sentences.",
    },
    "canary": "CEI-DUPLEX-P0::canary::DPX-P0-M001",
}


def test_normalize_item_maps_core_fields():
    item = normalize_item(RAW)
    assert item["item_id"] == "DPX-P0-M001"
    assert item["text"].startswith("Scenario text")
    assert item["axis"] == "process"
    assert item["condition_prompts"]["extended_thinking"] == "EXT-PROMPT: think step by step."
    assert item["canary"].startswith("CEI-DUPLEX-P0")
    assert item["raw"] is RAW


def test_normalize_axis_for_discriminant_control():
    dc = dict(RAW, is_discriminant_control=True)
    assert normalize_item(dc)["axis"] == "discriminant_control"


def test_orchestrator_prefers_per_condition_prompt():
    item = normalize_item(RAW)
    adapter = fx.FakeAdapter("anthropic")
    orch = Orchestrator(
        adapters={"anthropic": adapter},
        models=[{"id": "claude-opus-4-6", "vendor": "anthropic"}],
        item_bank=[item],
        conditions=["forced_immediate", "extended_thinking"],
        scorer=fx.fake_scorer, reps=1, temperature=0.7,
    )
    orch.run()
    prompts = {c["gen"] and c["prompt"] for c in adapter.calls}
    assert "FI-PROMPT: answer in 16 tokens." in prompts
    assert "EXT-PROMPT: think step by step." in prompts


def test_render_prompt_falls_back_to_suffix_without_variants():
    # a bare item (no condition_prompts) uses text + the generic condition suffix
    from runner.orchestrator import condition_config
    item = {"item_id": "x", "text": "STEM", "axis": "process"}
    cfg = condition_config("forced_immediate")
    rendered = Orchestrator.render_prompt(item, cfg, "forced_immediate")
    assert rendered.startswith("STEM")
    assert "16 tokens" in rendered


@pytest.mark.skipif(
    not os.path.exists(DEFAULT_BANK_PATH), reason="authored item bank not present yet"
)
def test_load_real_bank_if_present():
    items = load_item_bank()
    assert len(items) > 0
    for it in items[:5]:
        assert it["item_id"]
        assert it["text"]
        assert it["axis"] in ("process", "content", "discriminant_control")
