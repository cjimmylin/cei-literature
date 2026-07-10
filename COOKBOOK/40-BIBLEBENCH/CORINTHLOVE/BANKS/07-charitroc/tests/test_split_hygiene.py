"""Public/private pools are disjoint beyond wrappers and entity substitution."""
import copy
import re

import generator
from lib import split_hygiene, surfaces


def _core_skeleton(text):
    """Strip response format and every fixed stage-wrapper literal."""
    core = text.replace(surfaces.RESPONSE_FORMAT, " ")
    templates = (
        surfaces.PUBLIC_TEMPLATES + surfaces.CALIBRATION_TEMPLATES
        + surfaces.PRIVATE_TEMPLATES
    )
    literals = []
    for template in templates:
        for stage in ("stage_1", "stage_2", "stage_3", "stage_4"):
            literals.extend(
                fragment for fragment in re.split(r"\{[a-z0-9_]+\}", template[stage])
                if fragment.strip()
            )
    for literal in sorted(set(literals), key=len, reverse=True):
        core = core.replace(literal, " ")
    return surfaces.normalized_skeleton(core)


def _shingles(text, width=4):
    tokens = re.findall(r"[a-z<>]+", text)
    return {
        tuple(tokens[index:index + width])
        for index in range(max(0, len(tokens) - width + 1))
    }


def _overlap(left, right):
    left_shingles, right_shingles = _shingles(left), _shingles(right)
    if not left_shingles or not right_shingles:
        return 0.0
    return len(left_shingles & right_shingles) / min(
        len(left_shingles), len(right_shingles)
    )


def test_split_pool_ids_and_template_ids_are_disjoint():
    episodes, sidecar, _, _ = generator.generate(20260709)
    public_pool_ids, private_pool_ids = set(), set()
    public_templates, private_templates = set(), set()
    public_semantics, private_semantics = set(), set()
    for episode in episodes:
        hidden = sidecar[episode["id"]]
        if episode["split"] == "public":
            public_pool_ids.add(hidden["entity_pool_id"])
            public_templates.add(hidden["surface_template_id"])
            public_semantics.add(hidden["semantic_bank_id"])
        else:
            private_pool_ids.add(hidden["entity_pool_id"])
            private_templates.add(hidden["surface_template_id"])
            private_semantics.add(hidden["semantic_bank_id"])
    assert public_pool_ids.isdisjoint(private_pool_ids)
    assert public_templates.isdisjoint(private_templates)
    assert public_semantics.isdisjoint(private_semantics)


def test_no_cross_split_hash_or_normalized_skeleton_overlap():
    episodes, _, _, _ = generator.generate(20260709)
    texts = {
        split: {
            generator.visible_text(episode) for episode in episodes
            if episode["split"] == split
        }
        for split in ("public", "calibration", "private")
    }
    skeletons = {
        split: {surfaces.normalized_skeleton(text) for text in values}
        for split, values in texts.items()
    }
    for index, left in enumerate(texts):
        for right in tuple(texts)[index + 1:]:
            assert texts[left].isdisjoint(texts[right])
            assert skeletons[left].isdisjoint(skeletons[right])


def test_all_three_split_pairs_stay_below_strict_core_shingle_limit():
    episodes, _, _, _ = generator.generate(20260709)
    result = split_hygiene.audit_cross_split_shingles(
        episodes, threshold=0.25
    )
    assert set(result["max_overlap"]) == {
        "public|calibration", "public|private", "calibration|private",
    }
    assert all(value < 0.25 for value in result["max_overlap"].values())
    assert result["violations"] == []
    assert result["comparisons"] == 21120


def test_shingle_audit_is_non_vacuous_on_cross_split_stage_copy():
    episodes, _, _, _ = generator.generate(20260709)
    poisoned = copy.deepcopy(episodes)
    public = next(
        episode for episode in poisoned if episode["split"] == "public"
    )
    calibration = next(
        episode for episode in poisoned
        if episode["split"] == "calibration"
        and episode["template_family"] == public["template_family"]
    )
    calibration["multiturn_script"]["stage_3"] = (
        public["multiturn_script"]["stage_3"]
    )
    result = split_hygiene.audit_cross_split_shingles(
        poisoned, threshold=0.25
    )
    assert result["violations"]
    assert result["max_overlap"]["public|calibration"] == 1.0
