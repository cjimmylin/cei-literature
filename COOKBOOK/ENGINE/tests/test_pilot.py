"""Tests for the reusable pilot-build entrypoint (shared infra for 01/05).

`publish_spec` emits the PUBLISHED spec (values, factors, fractional design,
confounding structure) — released per §3.1 "published spec; private parameter
ranges". `build_pilot_instances` emits a FRESH instance per screened cell.
Everything must be JSON-serializable so downstream designs can consume it.
"""
import json

from crux import pilot, values


def test_publish_spec_is_json_serializable_with_all_sections():
    spec = pilot.publish_spec(n_cells=60, seed=0)
    for key in ("values", "factors", "fractional_design", "confounding"):
        assert key in spec
    # value_pair tuples etc. must serialize
    dumped = json.dumps(spec)
    assert isinstance(dumped, str)
    assert len(spec["fractional_design"]) <= 60


def test_pilot_has_one_fresh_instance_per_screened_cell():
    spec = pilot.publish_spec(n_cells=60, seed=0)
    instances = pilot.build_pilot_instances(n_cells=60, seed=0, instance_seed=3)
    assert len(instances) == len(spec["fractional_design"])


def test_pilot_instances_serialize_and_reference_real_pairs():
    instances = pilot.build_pilot_instances(n_cells=12, seed=1, instance_seed=1)
    known = {frozenset(p) for p in values.value_pairs()}
    for inst in instances:
        json.dumps(inst)  # serializable (value_pair rendered as a list)
        assert frozenset((inst["value_a"], inst["value_b"])) in known
        honors = {o["honors"] for o in inst["options"]}
        assert honors == {inst["value_a"], inst["value_b"]}
