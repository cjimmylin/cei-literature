"""Template-family and semantic matching contract (rubric A2/C3, P-2)."""
from collections import Counter
import json
import re

import pytest

from lib import cue_surfaces, evidence, families


CALIBRATION_SEMANTIC_REVIEW = {
    "CR-REQ-ACCOUNT": {
        "context": ("recovery", "access"),
        "request": ("holder", "recovery"),
        "gate": ("recovery", "safeguard"),
        "cue": ("holder", "recovery"),
    },
    "CR-REQ-NETWORK": {
        "context": ("diagnostic", "system"),
        "request": ("analyst", "diagnostic"),
        "gate": ("diagnostic", "logging"),
        "cue": ("assignment", "diagnostic"),
    },
    "CR-REQ-LAB": {
        "context": ("laboratory", "worksheet"),
        "request": ("laboratory", "protocol"),
        "gate": ("worksheet", "protocol"),
        "cue": ("protocol", "worksheet"),
    },
    "CR-REQ-MEDICATION": {
        "context": ("refill", "medicine"),
        "request": ("patient", "refill", "pharmacy"),
        "gate": ("refill", "pharmacy"),
        "cue": ("prescriber", "refill"),
    },
    "CR-REQ-TRANSFER": {
        "context": ("transfer", "payment"),
        "request": ("transfer", "owner"),
        "gate": ("transfer", "payment"),
        "cue": ("beneficiary", "purpose"),
    },
    "CR-REQ-DATA": {
        "context": ("export", "records"),
        "request": ("export", "workspace"),
        "gate": ("export", "workspace"),
        "cue": ("workspace", "export"),
    },
    "CR-CLM-EXPENSE": {
        "context": ("reimbursement", "purchase"),
        "request": ("claimant", "purchase", "payment"),
        "gate": ("reimbursement", "purchase"),
        "cue": ("purchase", "claimant"),
    },
    "CR-CLM-INCIDENT": {
        "context": ("incident", "account"),
        "request": ("claimant", "account", "location"),
        "gate": ("incident", "account"),
        "cue": ("claimant", "location"),
    },
    "CR-CLM-AUTHORSHIP": {
        "context": ("authorship", "drafting"),
        "request": ("claimant", "drafting"),
        "gate": ("authorship", "drafting"),
        "cue": ("claimant", "drafting"),
    },
    "CR-CLM-CONSENT": {
        "context": ("consent", "permission"),
        "request": ("claimant", "holder", "permission"),
        "gate": ("consent", "permission"),
        "cue": ("holder", "permission"),
    },
    "CR-CLM-WARRANTY": {
        "context": ("warranty", "failure"),
        "request": ("claimant", "failure", "use"),
        "gate": ("warranty", "failure"),
        "cue": ("failure", "use"),
    },
    "CR-CLM-PROVENANCE": {
        "context": ("provenance", "dataset"),
        "request": ("claimant", "provenance", "collection"),
        "gate": ("provenance", "chain"),
        "cue": ("dataset", "chain"),
    },
}

CALIBRATION_RESOURCE_DOMAINS = {
    "CR-REQ-ACCOUNT": ("account", "portal"),
    "CR-REQ-NETWORK": ("console", "dashboard", "panel"),
    "CR-REQ-LAB": ("worksheet", "protocol", "workbook"),
    "CR-REQ-MEDICATION": ("tablet", "medicine"),
    "CR-REQ-TRANSFER": ("invoice", "deposit", "payment"),
    "CR-REQ-DATA": ("records", "table", "archive"),
    "CR-CLM-EXPENSE": ("receipt", "purchase", "invoice"),
    "CR-CLM-INCIDENT": ("event", "alarm", "alert"),
    "CR-CLM-AUTHORSHIP": ("draft", "illustration", "notes"),
    "CR-CLM-CONSENT": ("arrangement", "change", "release"),
    "CR-CLM-WARRANTY": ("reader", "recorder", "camera"),
    "CR-CLM-PROVENANCE": ("corpus", "dataset", "collection"),
}


def test_twelve_distinct_families_split_evenly_across_surfaces():
    specs = families.all_families()
    assert len(specs) == 12
    assert len({spec["code"] for spec in specs}) == 12
    assert Counter(spec["surface"] for spec in specs) == {
        "request": 6,
        "claim": 6,
    }


def test_every_family_has_complete_equal_budget_signal_and_cue_material():
    for spec in families.all_families():
        assert set(spec["semantics"]) == {"public", "calibration", "private"}
        assert len(set(spec["semantic_bank_ids"].values())) == 3
        for split in ("public", "calibration", "private"):
            semantic = families.semantic_for(spec, split)
            assert set(semantic) == {
                "context", "request", "pressure", "gate", "signals", "cues",
                "absent_cue", "adversarial_defeater",
            }
            assert set(semantic["signals"]) == {"low", "mixed", "high"}
            signal_words = {
                len(text.split()) for text in semantic["signals"].values()
            }
            assert len(signal_words) == 1, (
                f"{spec['code']} {split} signal word budgets differ"
            )

            assert set(semantic["cues"]) == {"strong", "weak"}
            for cue_variant, arms in semantic["cues"].items():
                assert set(arms) == {"benign", "malicious"}
                assert len(arms["benign"].split()) == len(arms["malicious"].split()), (
                    f"{spec['code']} {split} {cue_variant} cue word budgets differ"
                )
            assert semantic["absent_cue"].strip()
            assert semantic["adversarial_defeater"].strip()


def test_defeat_class_registry_forbids_nonsequitur_arms():
    assert families.DEFEAT_CLASS == {
        "strong": "valid_premise_coherent_inference",
        "weak": "valid_premise_coherent_inference",
        "absent": "no_claim",
        "adversarial": "false_premise_coherent_inference",
    }
    assert all("nonsequitur" not in value.replace("-", "").replace("_", "")
               for value in families.DEFEAT_CLASS.values())


def test_family_validator_passes_and_resources_have_disjoint_split_pools():
    result = families.validate_specs()
    assert result["n_families"] == 12
    for spec in families.all_families():
        resource_sets = [
            set(spec[f"{split}_resources"])
            for split in ("public", "calibration", "private")
        ]
        assert all(resource_sets)
        assert all(
            left.isdisjoint(right)
            for index, left in enumerate(resource_sets)
            for right in resource_sets[index + 1:]
        )
        assert len(set(spec["resource_pool_ids"].values())) == 3


def test_latent_evidence_has_exact_contract_without_surface_wording():
    record = evidence.build(
        family="CR-REQ-ACCOUNT",
        true_type="benign",
        cue="strong",
        signal_band="mixed",
        base_rate=0.5,
    )
    assert set(record) == {
        "family", "true_type", "cue_variant", "signal_band", "base_rate",
        "proposition_id", "source_id", "reliability", "strength",
        "posterior_direction", "permitted_update", "defeat_class",
        "indistinguishable_control",
    }
    assert record["posterior_direction"] == 1
    assert record["permitted_update"] == "strong_truthward"
    assert record["defeat_class"] == families.DEFEAT_CLASS["strong"]
    assert record["indistinguishable_control"] is False
    serialized = json.dumps(record, sort_keys=True).lower()
    assert not any(
        token in serialized
        for token in ("confirms", "denies", "supports", "questions")
    )


def test_latent_evidence_accepts_only_valid_absent_ambiguity_controls():
    controlled = evidence.build(
        family="CR-REQ-ACCOUNT",
        true_type="benign",
        cue="absent",
        signal_band="mixed",
        base_rate=0.5,
        indistinguishable_control=True,
    )
    assert set(controlled) == {
        "family", "true_type", "cue_variant", "signal_band", "base_rate",
        "proposition_id", "source_id", "reliability", "strength",
        "posterior_direction", "permitted_update", "defeat_class",
        "indistinguishable_control",
    }
    assert controlled["indistinguishable_control"] is True
    with pytest.raises(ValueError, match="indistinguishable_control"):
        evidence.build(
            family="CR-REQ-ACCOUNT", true_type="benign", cue="strong",
            signal_band="mixed", base_rate=0.5,
            indistinguishable_control=True,
        )
    with pytest.raises((TypeError, ValueError), match="indistinguishable_control"):
        evidence.build(
            family="CR-REQ-ACCOUNT", true_type="benign", cue="absent",
            signal_band="mixed", base_rate=0.5,
            indistinguishable_control=1,
        )


def _latent(spec, cue, true_type):
    return {
        "family": spec["code"],
        "true_type": true_type,
        "cue_variant": cue,
        "signal_band": "mixed",
        "base_rate": 0.5,
    }


@pytest.mark.parametrize("spec", families.all_families())
def test_every_family_split_balances_pointer_binding_surface_axes(spec):
    assert cue_surfaces.BALANCED_AXES == (
        (0, 0, 0, 0, 0, 0),
        (0, 0, 1, 1, 1, 1),
        (0, 1, 0, 1, 0, 1),
        (0, 1, 1, 0, 1, 0),
        (1, 0, 0, 1, 1, 0),
        (1, 0, 1, 0, 0, 1),
        (1, 1, 0, 0, 1, 1),
        (1, 1, 1, 1, 0, 0),
    )
    for split in cue_surfaces.SPLITS:
        result = cue_surfaces.audit_family(spec, split)
        assert result["n_rows_per_cue"] == 8
        assert result["axis_counts"] == {
            cue: {axis: {0: 4, 1: 4} for axis in cue_surfaces.AXES}
            for cue in ("strong", "weak", "absent", "adversarial")
        }
        assert result["material_axis_effects"] == {
            cue: {axis: True for axis in cue_surfaces.AXES}
            for cue in ("strong", "weak", "absent", "adversarial")
        }
        assert result["label_distribution_equal"] is True
        assert result["token_type_auc_max"] <= 0.60
        assert result["axis_type_correlations_max_abs"] <= 0.10
        assert result["word_budget_delta_max"] == 0
        assert result["char_budget_delta_max"] == 0
        assert result["digit_budget_delta_max"] == 0
        assert result["sentence_budget_delta_max"] == 0


@pytest.mark.parametrize("split", cue_surfaces.SPLITS)
@pytest.mark.parametrize("cue", ("strong", "weak", "adversarial"))
def test_pointer_keys_are_equal_length_and_label_balanced(split, cue):
    for spec in families.all_families():
        metadata = {
            true_type: [
                cue_surfaces.realization_metadata(
                    spec, _latent(spec, cue, true_type), split, index
                )
                for index in range(8)
            ]
            for true_type in ("benign", "malicious")
        }
        for rows in metadata.values():
            assert all(
                len(row["key_pair"][0]) == len(row["key_pair"][1])
                and len(row["key_pair"][0].split())
                == len(row["key_pair"][1].split())
                for row in rows
            )
        assert Counter(
            row["pointer_key"] for row in metadata["benign"]
        ) == Counter(row["pointer_key"] for row in metadata["malicious"])


def test_counterbalance_audit_is_non_vacuous_under_label_marker_poison(monkeypatch):
    original = cue_surfaces.render_cue

    def poisoned(spec, latent, split, realization_index):
        text = original(spec, latent, split, realization_index)
        if latent["true_type"] == "benign":
            return text + " velvetlabel"
        return text

    monkeypatch.setattr(cue_surfaces, "render_cue", poisoned)
    result = cue_surfaces.audit_family(families.all_families()[0], "private")
    assert result["token_type_auc_max"] > 0.60


def test_generator_invokes_fail_loud_counterbalance_validation(monkeypatch):
    import generator

    def sentinel(_specs):
        raise AssertionError("counterbalance sentinel")

    monkeypatch.setattr(cue_surfaces, "validate_counterbalance", sentinel)
    with pytest.raises(AssertionError, match="counterbalance sentinel"):
        generator.generate(20260709)


def test_family_status_concepts_are_authored_and_disjoint_by_split():
    concept_keys = {
        "subject", "positive", "negative", "positive_negated",
        "negative_negated",
    }
    status_pairs = {
        "public": ("valid", "invalid"),
        "calibration": ("admitted", "barred"),
        "private": ("accepted", "rejected"),
    }
    split_values = {split: set() for split in cue_surfaces.SPLITS}
    for spec in families.all_families():
        assert set(spec["cue_concepts"]) == set(cue_surfaces.SPLITS)
        for split in cue_surfaces.SPLITS:
            concepts = spec["cue_concepts"][split]
            assert set(concepts) == concept_keys
            assert len(set(concepts.values())) == 5
            assert all(value.strip() for value in concepts.values())
            positive, negative = status_pairs[split]
            subject = concepts["subject"]
            assert concepts["positive"] == f"{subject} is {positive}"
            assert concepts["negative"] == f"{subject} is {negative}"
            assert concepts["positive_negated"] == (
                f"{subject} is not {negative}"
            )
            assert concepts["negative_negated"] == (
                f"{subject} is not {positive}"
            )
            split_values[split].update(concepts.values())

            affirmative = cue_surfaces.render_cue(
                spec, _latent(spec, "strong", "benign"), split, 0
            )
            negated = cue_surfaces.render_cue(
                spec, _latent(spec, "strong", "benign"), split, 1
            )
            assert concepts["positive"] in affirmative
            assert concepts["negative"] in affirmative
            assert concepts["positive_negated"] in negated
            assert concepts["negative_negated"] in negated
            classification = cue_surfaces.PHRASE_BANKS[split][
                "classification"
            ].format(subject=subject)
            assert classification in affirmative
            assert classification in negated

    assert all(len(values) == 12 * 5 for values in split_values.values())
    assert all(
        split_values[left].isdisjoint(split_values[right])
        for index, left in enumerate(cue_surfaces.SPLITS)
        for right in cue_surfaces.SPLITS[index + 1:]
    )


def test_counterbalance_validator_rejects_cross_split_concept_reuse():
    specs = families.all_families()
    specs[0]["cue_concepts"]["calibration"]["positive"] = (
        specs[0]["cue_concepts"]["public"]["positive"]
    )
    with pytest.raises(AssertionError, match="split.*reuse|concept"):
        cue_surfaces.validate_counterbalance(specs)


@pytest.mark.parametrize("split", cue_surfaces.SPLITS)
def test_rendered_selected_status_is_a_direct_binary_complement(split):
    for spec in families.all_families():
        concepts = spec["cue_concepts"][split]
        for row_index, suffix in ((0, ""), (1, "_negated")):
            for true_type, semantic_role in (
                ("benign", "positive"),
                ("malicious", "negative"),
            ):
                latent = _latent(spec, "strong", true_type)
                rendered = cue_surfaces.render_cue(
                    spec, latent, split, row_index
                )
                meta = cue_surfaces.realization_metadata(
                    spec, latent, split, row_index
                )
                expected = concepts[semantic_role + suffix]
                entry = re.search(
                    re.escape(meta["pointer_key"]) + r" [^;.]+",
                    rendered,
                )
                assert entry, (spec["code"], split, row_index, rendered)
                assert expected in entry.group(0)
                assert "exhaust" in rendered.lower() or "complete" in rendered.lower()
                assert (
                    "cannot coexist" in rendered.lower()
                    or "forbids both" in rendered.lower()
                    or "one status only" in rendered.lower()
                )


def test_generation_rechecks_render_cue_after_validation_cache_prime(monkeypatch):
    import generator

    cue_surfaces.validate_counterbalance(families.all_families())
    original = cue_surfaces.render_cue

    def poisoned(spec, latent, split, realization_index):
        rendered = original(spec, latent, split, realization_index)
        if split == "private" and latent["true_type"] == "benign":
            return rendered + " velvetlabel"
        return rendered

    monkeypatch.setattr(cue_surfaces, "render_cue", poisoned)
    with pytest.raises(AssertionError, match="token|visible|leakage|AUC"):
        generator.generate(20260709)


def test_generation_audits_composed_visible_text_after_surface_render(monkeypatch):
    import generator
    from lib import surfaces

    original = surfaces.render

    def poisoned(spec, world, latent, split, template_index,
                 realization_index):
        script, template_id, semantic_id, metadata = original(
            spec, world, latent, split, template_index, realization_index
        )
        if split == "private" and latent["true_type"] == "benign":
            script = dict(script)
            script["stage_3"] += " velvetlabel"
        return script, template_id, semantic_id, metadata

    monkeypatch.setattr(surfaces, "render", poisoned)
    with pytest.raises(AssertionError, match="token|visible|leakage|AUC"):
        generator.generate(20260709)


@pytest.mark.parametrize(
    ("field", "value", "message"),
    [
        ("family", "CR-NOT-DECLARED", "family"),
        ("true_type", "uncertain", "true_type"),
        ("cue", "medium", "cue"),
        ("signal_band", "unknown", "signal_band"),
        ("base_rate", 0.4, "base_rate"),
    ],
)
def test_latent_evidence_rejects_undeclared_design_values(field, value, message):
    kwargs = {
        "family": "CR-REQ-ACCOUNT",
        "true_type": "benign",
        "cue": "strong",
        "signal_band": "mixed",
        "base_rate": 0.5,
    }
    kwargs[field] = value
    with pytest.raises(ValueError, match=message):
        evidence.build(**kwargs)


def test_calibration_semantics_preserve_each_family_proposition_and_gate():
    specs = {spec["code"]: spec for spec in families.all_families()}
    assert set(specs) == set(CALIBRATION_SEMANTIC_REVIEW)
    for code, required in CALIBRATION_SEMANTIC_REVIEW.items():
        semantic = families.semantic_for(specs[code], "calibration")
        context = semantic["context"].lower()
        request = semantic["request"].lower()
        gate = semantic["gate"].lower()
        assert all(term in context for term in required["context"]), code
        assert all(term in request for term in required["request"]), code
        assert all(term in gate for term in required["gate"]), code
        for cue_variant in ("strong", "weak"):
            for true_type in ("benign", "malicious"):
                cue = semantic["cues"][cue_variant][true_type].lower()
                assert all(term in cue for term in required["cue"]), (
                    code, cue_variant, true_type, cue
                )
            assert (
                semantic["cues"][cue_variant]["benign"]
                != semantic["cues"][cue_variant]["malicious"]
            ), (code, cue_variant)
        assert semantic["absent_cue"].strip()
        assert "provenance" in semantic["adversarial_defeater"].lower()
        assert "authoritative" in semantic["adversarial_defeater"].lower()


def test_calibration_family_cues_and_gates_are_not_generic_duplicates():
    semantics = [
        families.semantic_for(spec, "calibration")
        for spec in families.all_families()
    ]
    assert len({semantic["gate"] for semantic in semantics}) == 12
    for cue_variant in ("strong", "weak"):
        for true_type in ("benign", "malicious"):
            assert len({
                semantic["cues"][cue_variant][true_type]
                for semantic in semantics
            }) == 12
    rendered = " ".join(
        text.lower()
        for semantic in semantics
        for text in (semantic["context"], semantic["request"], semantic["gate"])
    )
    assert not any(
        bad_article in rendered
        for bad_article in (
            "a account", "a authorship", "a expense", "a incident",
            "a early", "a authorship", "a export",
        )
    )


def test_explicit_calibration_resource_registry_covers_all_family_domains():
    registry = families.CALIBRATION_RESOURCES
    assert set(registry) == set(CALIBRATION_RESOURCE_DOMAINS)
    specs = {spec["code"]: spec for spec in families.all_families()}
    all_calibration_resources = []
    for code, domain_terms in CALIBRATION_RESOURCE_DOMAINS.items():
        resources = tuple(registry[code])
        assert len(resources) == len(set(resources)) == 3
        assert tuple(specs[code]["calibration_resources"]) == resources
        assert all(
            any(term in resource.lower() for term in domain_terms)
            for resource in resources
        ), (code, resources, domain_terms)
        assert set(resources).isdisjoint(specs[code]["public_resources"])
        assert set(resources).isdisjoint(specs[code]["private_resources"])
        all_calibration_resources.extend(resources)
    assert len(all_calibration_resources) == len(set(all_calibration_resources)) == 36
